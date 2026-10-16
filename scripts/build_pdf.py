"""Build the offline edition from the SAME chapter files and order as MkDocs."""
from pathlib import Path
from datetime import datetime
from zoneinfo import ZoneInfo
import argparse
import json
import os
import re
import shutil
import subprocess
from urllib.parse import unquote

import markdown
import yaml
from pypdf import PdfReader

ROOT = Path(__file__).resolve().parents[1]
READER = 'markdown+tex_math_dollars+tex_math_single_backslash-implicit_figures'


def run(args, **kwargs):
    return subprocess.run(args, check=True, text=True, **kwargs)


def walk(value):
    if isinstance(value, dict):
        yield value
        for child in value.values():
            yield from walk(child)
    elif isinstance(value, list):
        for child in value:
            yield from walk(child)


def nav_files(items):
    for item in items:
        if isinstance(item, str):
            yield item
        elif isinstance(item, dict):
            for value in item.values():
                if isinstance(value, list):
                    yield from nav_files(value)
                else:
                    yield value


def validate_pdf(path, minimum_bookmarks):
    pdf = PdfReader(path)
    outlines = [n for n in walk(pdf.outline) if '/Title' in n]
    assert len(outlines) >= minimum_bookmarks, 'Missing chapter/section bookmarks'
    for node in outlines:
        assert pdf.get_destination_page_number(node) is not None
    destinations = pdf.named_destinations
    internal = 0
    for page in pdf.pages:
        for ref in page.get('/Annots', []):
            annotation = ref.get_object()
            dest = annotation.get('/Dest')
            action = annotation.get('/A', {})
            if action.get('/S') == '/GoTo':
                dest = action.get('/D')
            if dest is not None:
                internal += 1
                if isinstance(dest, str):
                    assert dest in destinations, f'Broken PDF destination: {dest}'
            if action.get('/S') == '/URI':
                assert '.md' not in str(action.get('/URI')), 'Unconverted Markdown link'
    assert internal >= minimum_bookmarks, 'Missing clickable contents or back links'
    assert all((p.extract_text() or '').strip() for p in pdf.pages), 'Blank PDF page'
    print(f'Validated: {len(pdf.pages)} pages, {len(outlines)} bookmarks, {internal} internal links')


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--output', type=Path, default=ROOT / 'output/pdf/complex-analysis-notes.pdf')
    args = parser.parse_args()
    chapters = [p for p in nav_files(yaml.safe_load((ROOT / 'nav.yml').read_text())['nav'])
                if p != 'index.md' and p.endswith('.md')]
    blocks, targets = [], {}
    api_version = None
    expected_bookmarks = 0
    for filename in chapters:
        source = (ROOT / 'docs' / filename).read_text(encoding='utf-8')
        doc = json.loads(run(['pandoc', '--from', READER, '--to', 'json'],
                             input=source, capture_output=True).stdout)
        api_version = doc['pandoc-api-version']
        # MkDocs and Pandoc generate different default anchors, especially for math.
        # Use MkDocs' actual heading IDs, namespaced per chapter in the merged PDF.
        md = markdown.Markdown(extensions=['toc', 'pymdownx.arithmatex'],
                               extension_configs={'pymdownx.arithmatex': {'generic': True}})
        md.convert(source)
        web_ids = [node['id'] for node in walk(md.toc_tokens) if 'id' in node]
        headers = [node for node in walk(doc['blocks']) if node.get('t') == 'Header']
        assert len(headers) == len(web_ids), f'Heading mismatch: {filename}'
        prefix = Path(filename).stem
        for header, web_id in zip(headers, web_ids):
            level, attrs, _ = header['c']
            target = f'{prefix}--{web_id}'
            targets[(filename, web_id)] = target
            attrs[0] = target
            expected_bookmarks += level <= 3
        targets[(filename, '')] = headers[0]['c'][1][0]
        if blocks:
            blocks.append({'t': 'RawBlock', 'c': ['latex', r'\clearpage']})
        for block in doc['blocks']:
            blocks.append(block)
            if block.get('t') == 'Header' and block['c'][0] <= 2:
                blocks.append({'t': 'RawBlock', 'c': ['latex',
                    r'{\small\color{gray}\hyperlink{notes-toc}{返回目录}\par}\n'.replace('\\n', '\n')]})
        # Store origin for each cross-reference before concatenation.
        for node in walk(doc['blocks']):
            if node.get('t') == 'Link':
                node['_origin'] = filename
    for node in walk(blocks):
        if node.get('t') != 'Link':
            continue
        origin = node.pop('_origin')
        url = node['c'][2][0]
        if '://' in url or url.startswith('mailto:'):
            continue
        path, _, anchor = unquote(url).partition('#')
        filename = str((Path(origin).parent / path).as_posix()) if path else origin
        if filename.endswith('.md'):
            target = targets.get((filename, anchor))
            if target is None:
                raise ValueError(f'Unresolved link in {origin}: {url}')
            node['c'][2][0] = '#' + target
    output = args.output.resolve()
    output.parent.mkdir(parents=True, exist_ok=True)
    temp = ROOT / 'tmp/pdfs'
    temp.mkdir(parents=True, exist_ok=True)
    ast_path = temp / 'notes.json'
    ast_path.write_text(json.dumps({'pandoc-api-version': api_version, 'meta': {}, 'blocks': blocks}), encoding='utf-8')
    date = datetime.now(ZoneInfo('Asia/Shanghai')).strftime('%Y-%m-%d')
    revision = os.environ.get('GITHUB_SHA', 'local')[:12]
    tex_path = temp / 'notes.tex'
    run(['pandoc', str(ast_path), '--from=json', '--standalone', '--to=latex',
         '--toc', '--toc-depth=3', '--resource-path=' + str(ROOT / 'docs'),
         '--metadata=title:复变函数讲义', '--metadata=author:杨晓京老师课堂板书整理',
         '--metadata=date:' + date + ' · ' + revision,
         '--metadata=toc-title:目录', '--variable=documentclass:article',
         '--variable=CJKmainfont:Noto Serif CJK SC',
         '--variable=CJKsansfont:Noto Sans CJK SC',
         '--variable=fontsize:11pt', '--variable=geometry:a4paper,margin=22mm',
         '--variable=linestretch:1.12', '--variable=colorlinks:true',
         '--variable=linkcolor:blue', '--variable=urlcolor:blue',
         '--include-in-header=' + str(ROOT / 'scripts/pdf-header.tex'),
         '--output=' + str(tex_path)])
    for _ in range(3):
        result = subprocess.run(['xelatex', '-interaction=nonstopmode', '-halt-on-error',
                                 '-file-line-error', '-output-directory=' + str(temp), str(tex_path)],
                                cwd=ROOT / 'docs', text=True, capture_output=True)
        if result.returncode:
            print(result.stdout[-6000:])
            result.check_returncode()
    log = (temp / 'notes.log').read_text(encoding='utf-8', errors='replace')
    if 'Missing character:' in log:
        raise ValueError('Missing glyph in PDF; see tmp/pdfs/notes.log')
    widths = [float(x) for x in re.findall(r'Overfull \\hbox \(([\d.]+)pt too wide\)', log)]
    print(f'Largest horizontal overflow: {max(widths, default=0):.2f}pt')
    shutil.copyfile(temp / 'notes.pdf', output)
    validate_pdf(output, expected_bookmarks)
    print(output)


if __name__ == '__main__':
    main()

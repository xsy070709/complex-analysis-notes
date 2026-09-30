from pathlib import Path
import re
import json

root = Path(__file__).parent
source = (root / 'source' / '复变函数讲义.md').read_text()
parts = re.split(r'(?=^## (?:\d+\. |第三章))', source, flags=re.M)
names = [
    '01-number-sets', '02-representation', '03-geometry', '04-logarithm',
    '05-log-minus-one', '06-powers', '07-infinite-products', '08-euler',
    '09-continuity', '10-trigonometric-series', '11-product-applications',
    '12-regions', '13-derivatives', '14-mappings', '15-cosine-equation',
    '16-entire-functions', '17-complex-integrals',
]
assert len(parts) == len(names) + 1, len(parts)
docs = root / 'docs'
docs.mkdir(exist_ok=True)
(docs / 'index.md').write_text('# 复变函数讲义\n\n本讲义根据课堂板书持续整理。请选择左侧章节开始阅读。\n')
nav = ['  - 首页: index.md']
for name, body in zip(names, parts[1:]):
    heading = body.splitlines()[0][3:]
    # One source heading per page; shift its subheadings by one level.
    body = re.sub(r'^(#{2,6})(?= )', lambda m: m.group(1)[1:], body, flags=re.M)
    (docs / f'{name}.md').write_text(body)
    nav.append(f'  - {json.dumps(heading, ensure_ascii=False)}: {name}.md')
(root / 'nav.yml').write_text('nav:\n' + '\n'.join(nav) + '\n')

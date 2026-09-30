from pathlib import Path
import re
import json

root = Path(__file__).parent
source = (root / 'source' / '复变函数讲义.md').read_text(encoding='utf-8')
parts = re.split(r'(?=^## 第[一二三]章)', source, flags=re.M)[1:]
names = ['01-complex-numbers', '02-analytic-functions', '03-complex-integrals']
assert len(parts) == len(names), len(parts)
docs = root / 'docs'
docs.mkdir(exist_ok=True)
(docs / 'index.md').write_text('# 复变函数讲义\n\n按章阅读：第一章复数与初等函数，第二章解析函数，第三章复积分。章内小节可通过右侧目录跳转。\n', encoding='utf-8')
nav = ['  - 首页: index.md']
for name, body in zip(names, parts):
    heading = body.splitlines()[0][3:]
    body = re.sub(r'^(#{2,6})(?= )', lambda m: m.group(1)[1:], body, flags=re.M)
    (docs / f'{name}.md').write_text(body, encoding='utf-8')
    nav.append(f'  - {json.dumps(heading, ensure_ascii=False)}: {name}.md')
(root / 'nav.yml').write_text('nav:\n' + '\n'.join(nav) + '\n', encoding='utf-8')

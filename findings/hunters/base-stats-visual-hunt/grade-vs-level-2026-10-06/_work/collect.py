"""Collect every image URL referenced by cached pages + prior-lane page cache."""
import json
import os
import sys
sys.path.insert(0, '.')
from crawl import page_imgs, page_links, read_local_pages

HERE = os.path.dirname(os.path.abspath(__file__))
PRIOR = os.path.abspath(os.path.join(HERE, '..', '..', '_archives_work', 'pages'))

imgs = {}
links = set()
for name, text in read_local_pages():
    for u in page_imgs(text):
        imgs.setdefault(u, []).append(name)
    links.update(page_links(text))
for fn in sorted(os.listdir(PRIOR)):
    if not fn.endswith('.html'):
        continue
    text = open(os.path.join(PRIOR, fn), encoding='utf-8', errors='replace').read()
    for u in page_imgs(text):
        imgs.setdefault(u, []).append(fn)
    links.update(page_links(text))

print('local+prior pages -> %d distinct image URLs, %d page links'
      % (len(imgs), len(links)))
json.dump({'imgs': imgs, 'links': sorted(links)},
          open(os.path.join(HERE, 'all-images.json'), 'w', encoding='utf-8'),
          ensure_ascii=False, indent=1)
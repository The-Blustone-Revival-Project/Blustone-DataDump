#!/usr/bin/env python
"""Build image -> article map from cached blustone.jp/archives pages.

Prints every cached page title with its in-article image order, so a download
plan can be built that knows what each screenshot is *of*.
"""
import os, re, html, json

D = '_archives_work/pages'
OUT = '_tools/panel-image-map.json'

BOILER = re.compile(
    r'^(btn-|go_store|VisualShower_CI|lesser\.png|thum-|sissou\.jpg|'
    r'1242x2208_04|small|logo)', re.I)


def clean(t):
    t = re.sub(r'(?is)<script.*?</script>', ' ', t)
    t = re.sub(r'(?is)<style.*?</style>', ' ', t)
    t = re.sub(r'(?s)<[^>]+>', ' ', t)
    t = html.unescape(t)
    return re.sub(r'\s+', ' ', t).strip()


def main():
    pages = []
    for f in sorted(os.listdir(D)):
        p = os.path.join(D, f)
        if not os.path.isfile(p):
            continue
        t = open(p, encoding='utf-8', errors='replace').read()
        ttl = re.search(r'(?is)<title>(.*?)</title>', t)
        title = (ttl.group(1).strip() if ttl else '')
        title = re.sub(r'\s*-\s*ブルーストーン公式攻略サイト\s*$', '', title)
        imgs = re.findall(r'src=["\']([^"\']+\.(?:jpg|jpeg|png|gif))', t, re.I)
        # preserve in-article order, dedupe
        seen, ordered = set(), []
        for x in imgs:
            n = x.split('/')[-1]
            if n in seen or BOILER.match(n):
                continue
            seen.add(n)
            ordered.append(n)
        pages.append({'file': f, 'title': title, 'images': ordered,
                      'n': len(ordered)})

    json.dump(pages, open(OUT, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)

    print('pages:', len(pages))
    for p in pages:
        print('%-56s | %-46s | %2d' % (p['file'][:56], p['title'][:46], p['n']))
        if p['images']:
            print('      ', ' '.join(p['images'][:40]))

    allimgs = sorted({i for p in pages for i in p['images']})
    print('\ndistinct non-boilerplate images referenced by pages:', len(allimgs))
    json.dump(allimgs, open('_tools/panel-all-images.json', 'w', encoding='utf-8'),
              ensure_ascii=False, indent=1)


if __name__ == '__main__':
    main()

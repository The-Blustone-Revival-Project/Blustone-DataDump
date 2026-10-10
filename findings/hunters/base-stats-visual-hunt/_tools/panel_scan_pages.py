#!/usr/bin/env python
"""Scan cached blustone.jp/archives pages for level/stat tokens and image refs."""
import os, re, html, json, sys

D = '_archives_work/pages'
OUT = '_tools/panel-page-index.json'

TOKEN = re.compile(r'レベル|[Ll]v\.?\s*\d+|戦闘力|ステータス|OYAGO_NEXT|umped|(?<![A-Za-z])HP(?![A-Za-z])')


def clean(t):
    t = re.sub(r'(?is)<script.*?</script>', ' ', t)
    t = re.sub(r'(?is)<style.*?</style>', ' ', t)
    t = re.sub(r'(?s)<[^>]+>', ' ', t)
    t = html.unescape(t)
    return re.sub(r'\s+', ' ', t)


def main():
    rows = []
    for f in sorted(os.listdir(D)):
        p = os.path.join(D, f)
        if not os.path.isfile(p):
            continue
        t = open(p, encoding='utf-8', errors='replace').read()
        ttl = re.search(r'(?is)<title>(.*?)</title>', t)
        body = clean(t)
        imgs = re.findall(r'src=["\']([^"\']+\.(?:jpg|jpeg|png|gif))', t, re.I)
        imgs += re.findall(r'href=["\']([^"\']+\.(?:jpg|jpeg|png|gif))', t, re.I)
        imgs = sorted({x.split('/')[-1] for x in imgs})
        hits = [body[max(0, m.start() - 110):m.start() + 110] for m in TOKEN.finditer(body)]
        rows.append({
            'file': f,
            'title': (ttl.group(1).strip() if ttl else '')[:120],
            'images': imgs,
            'n_images': len(imgs),
            'token_hits': hits,
        })
    json.dump(rows, open(OUT, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    sel = [r for r in rows if r['token_hits']]
    print('pages:', len(rows), 'with level/stat tokens:', len(sel))
    print('total distinct image files referenced:',
          len({i for r in rows for i in r['images']}))
    for r in sel:
        print('=' * 100)
        print(r['file'], '|', r['title'][:90])
        print('  images(%d):' % r['n_images'], r['images'][:16])
        for h in r['token_hits'][:8]:
            print('   >', h)


if __name__ == '__main__':
    main()

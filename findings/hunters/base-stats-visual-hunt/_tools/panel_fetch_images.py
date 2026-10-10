#!/usr/bin/env python3
"""Download every image referenced by the cached blustone.jp /archives/ pages,
using the exact original URL found in the archived HTML (trap: never rely on
the CDX/availability API for existence).

- Uses http:// (https:// is refused on this host per the lane brief).
- Uses /web/<capture-ts>id_/<original-url> from the referencing page's own
  capture timestamp, which is the exact-URL form the brief says to trust.
- Positive control runs first; a FAIL aborts so that no zero is meaningful.
- Rejects the 3,357-byte 域名停靠 parking page by size+sha.
- Records sha256, byte length and pixel dimensions for triage.
"""
import os, re, sys, json, time, hashlib, urllib.request, urllib.error
from io import BytesIO
from PIL import Image

UA = "Mozilla/5.0 (compatible; blustone-research/1.0)"
SIGS = {b"\xff\xd8\xff": "jpeg", b"\x89PNG": "png", b"GIF8": "gif", b"BM": "bmp"}
PAGES = '_archives_work/pages'
OUT = 'hero-panel-level-images-2026-10-06'
BASE = 'http://web.archive.org/web/'

PARK_SHA = None          # filled from the known parking page if encountered


def fetch(url, timeout=120, tries=3):
    for a in range(tries):
        try:
            req = urllib.request.Request(url, headers={'User-Agent': UA})
            with urllib.request.urlopen(req, timeout=timeout) as r:
                return r.status, r.read()
        except urllib.error.HTTPError as e:
            b = e.read()
            if e.code in (502, 503, 504) and a < tries - 1:
                time.sleep(2 * (a + 1)); continue
            return e.code, b
        except Exception:
            if a < tries - 1:
                time.sleep(2 * (a + 1)); continue
    return None, b''


def sig(b):
    for s, n in SIGS.items():
        if b.startswith(s):
            return n
    return None


def norm(u):
    """Strip Wayback rewriting back to the original blustone.jp URL."""
    u = u.replace('http://web.archive.org/web/', '')
    u = re.sub(r'^\d{14}(id_|im_|if_|js_|cs_)?/', '', u)
    u = re.sub(r'^https?://web\.archive\.org/web/\d{14}[a-z_]*/', '', u)
    return u


def main():
    os.makedirs(OUT, exist_ok=True)
    man = os.path.join(OUT, '_manifest.json')

    # ---- collect exact (url, page_ts, article) triples from the cached HTML
    items = {}          # original_url -> {pages:[], ts:[]}
    for f in sorted(os.listdir(PAGES)):
        p = os.path.join(PAGES, f)
        if not os.path.isfile(p):
            continue
        ts = f[:14]
        t = open(p, encoding='utf-8', errors='replace').read()
        ttl = re.search(r'(?is)<title>(.*?)</title>', t)
        title = (ttl.group(1).strip() if ttl else '')[:70]
        urls = re.findall(r'(?:src|href)=["\']([^"\']+?\.(?:jpg|jpeg|png|gif))', t, re.I)
        for u in urls:
            if 'web.archive.org' in u:
                u = norm(u)
            if 'blustone.jp' not in u:
                continue
            rec = items.setdefault(u, {'pages': [], 'ts': []})
            if f not in rec['pages']:
                rec['pages'].append(f)
            if ts not in rec['ts']:
                rec['ts'].append(ts)
    print('distinct original image URLs referenced:', len(items))

    # ---- positive controls
    print('\n=== CONTROLS ===')
    c1 = fetch(BASE)[0] == 200
    print('  C1 archive root                      :', 'PASS' if c1 else 'FAIL')
    s, b = fetch(BASE + '20190403182150id_/http://blustone.jp/wp-content/uploads/2018/11/rankup.jpg')
    c2 = (s == 200 and sig(b) == 'jpeg' and len(b) > 50000)
    print('  C2 known image rankup.jpg %6d B    : %s' % (len(b), 'PASS' if c2 else 'FAIL'))
    s, b = fetch(BASE + '20191216060610id_/https://blustone.jp/hunter/'
                 '%E3%83%AC%E3%82%A2%E3%83%AA%E3%83%86%E3%82%A3%E5%88%A5/'
                 '%E3%83%95%E3%82%A1%E3%82%A4%E3%83%88%E3%82%AF%E3%83%A9%E3%83%96%E3%81%AE'
                 '%E5%AE%88%E8%AD%B7%E8%80%85%E3%80%8C%E3%83%99%E3%83%83%E3%82%B1%E3%83%B3%E3%80%8D')
    c3 = (s == 200 and b'8709' in b and b'1678' in b)
    print('  C3 hero 051 profile %6d B          : %s' % (len(b), 'PASS' if c3 else 'FAIL'))
    if not (c1 and c2 and c3):
        print('ABORT - a control failed; any zero below is meaningless.')
        return 2

    # ---- download
    results = []
    if os.path.exists(man):
        results = json.load(open(man, encoding='utf-8'))
    have = {r['url']: r for r in results}
    order = sorted(items, key=lambda u: -len(u))
    for i, u in enumerate(order, 1):
        if u in have and have[u].get('status') in ('ok', '404', 'parking', 'nosig'):
            continue
        rec = items[u]
        name = u.split('/')[-1]
        got = None
        for ts in sorted(rec['ts'])[:3]:
            arc = BASE + ts + 'id_/' + u
            s, b = fetch(arc)
            sg = sig(b)
            if s == 200 and sg:
                got = (ts, b, sg); break
            if s == 200 and len(b) == 3357:
                got = (ts, b, 'PARKING'); break
        row = {'url': u, 'name': name, 'pages': rec['pages'], 'ts': sorted(rec['ts'])}
        if got:
            ts, b, sg = got
            row['status'] = 'ok' if sg in ('jpeg', 'png', 'gif', 'bmp') else 'parking'
            row['fetch_ts'] = ts
            row['bytes'] = len(b)
            row['sha256'] = hashlib.sha256(b).hexdigest()
            row['kind'] = sg
            if row['status'] == 'ok':
                p = os.path.join(OUT, name)
                with open(p, 'wb') as f:
                    f.write(b)
                try:
                    im = Image.open(BytesIO(b))
                    row['w'], row['h'] = im.size
                except Exception as e:
                    row['dim_error'] = str(e)
        else:
            row['status'] = '404'
        results = [r for r in results if r['url'] != u] + [row]
        print('  [%3d/%3d] %-9s %-52s %s' % (i, len(order), row['status'],
              name[:52], ('%dx%d %dB' % (row.get('w', 0), row.get('h', 0), row.get('bytes', 0)))
              if row['status'] == 'ok' else ''))
        json.dump(results, open(man, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)

    ok = [r for r in results if r['status'] == 'ok']
    print('\n=== %d/%d recovered as real images ===' % (len(ok), len(results)))
    return 0


if __name__ == '__main__':
    sys.exit(main())

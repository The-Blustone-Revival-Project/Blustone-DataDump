"""Probe category / taxonomy pages of blustone.jp across many capture timestamps."""
import json, os, sys, urllib.parse
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import wb

HERE = os.path.dirname(os.path.abspath(__file__))
CACHE = os.path.join(HERE, 'pages')
os.makedirs(CACHE, exist_ok=True)

def ts_pool():
    ts = set()
    # from prior census
    for f in ('cdx-domain.json', 'cdx-archives.json'):
        p = os.path.abspath(os.path.join(HERE, '..', '..', '_archives_work', f))
        if not os.path.exists(p):
            continue
        for r in json.load(open(p, encoding='utf-8')):
            ts.add(r.split(' ', 1)[0])
    # from this lane's cdx sweep
    p = os.path.join(HERE, 'cdx-sweep.json')
    if os.path.exists(p):
        d = json.load(open(p, encoding='utf-8'))
        for rows in d.values():
            for r in rows:
                ts.add(r['timestamp'])
    return sorted(ts)

def fetch_pages(orig_urls):
    pool = ts_pool()
    # also a coarse grid across the crawl windows seen in the corpus
    grid = []
    for day in ('20190330', '20190331', '20190401', '20190402', '20190403',
                '20190404', '20190405', '20190406', '20191015', '20191115',
                '20191118', '20191121', '20191122', '20191208', '20191209',
                '20191210', '20191211', '20191216'):
        for k in (0, 6, 12, 18):
            grid.append(day + '%02d0000' % k)
    allts = sorted(set(pool) | set(grid))
    print('timestamp pool: %d' % len(allts))
    got = {}
    for orig in orig_urls:
        found = None
        for ts in allts:
            rec, body = wb.probe(ts, orig)
            if rec['ok'] and b'<html' in body[:4000].lower():
                found = (ts, body, rec)
                break
            if rec['status'] == 200 and rec.get('bytes', 0) > wb.PARK_BYTES:
                found = (ts, body, rec)
                break
        if found:
            ts, body, rec = found
            if body is None:
                got[orig] = None
                print('FAIL(no body) %-60s' % orig)
                continue
            safe = urllib.parse.quote(orig, safe='')[-70:]
            p = os.path.join(CACHE, ts + '_' + safe + '.html')
            open(p, 'wb').write(body)
            got[orig] = {'ts': ts, 'bytes': rec['bytes'], 'file': p,
                         'sha256': rec['sha256']}
            print('OK   %-70s ts=%s bytes=%d' % (orig, ts, rec['bytes']))
        else:
            got[orig] = None
            print('FAIL %-70s' % orig)
    json.dump(got, open(os.path.join(HERE, 'category-pages.json'), 'w',
                        encoding='utf-8'), ensure_ascii=False, indent=1)
    return got

if __name__ == '__main__':
    fetch_pages(sys.argv[1:])
"""Full paginated CDX census of blustone.jp (trap #5 fix: page, do not truncate)."""
import json, os, sys, time, urllib.parse
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import wb

HERE = os.path.dirname(os.path.abspath(__file__))

def run(target='blustone.jp', mt='domain', limit=2000, maxpages=40):
    rows = {}
    pages = 0
    while pages < maxpages:
        q = ('url=%s&matchType=%s&output=json'
             '&fl=timestamp,original,statuscode,mimetype,digest,length'
             '&collapse=urlkey&limit=%d&page=%d') % (
            urllib.parse.quote(target, safe=''), mt, limit, pages)
        url = wb.WA + '/cdx/search/cdx?' + q
        got = None
        for attempt in range(4):
            st, body, hdr = wb.get(url, timeout=240)
            if st == 200:
                try:
                    got = json.loads(body.decode('utf-8', 'replace'))
                except Exception:
                    got = None
            if got:
                break
            time.sleep(3)
        if not got:
            print('page %d: no response (gave up after 4 attempts)' % pages, flush=True)
            break
        h = got[0]
        recs = [dict(zip(h, r)) for r in got[1:]]
        new = 0
        for r in recs:
            k = r['original']
            if k not in rows:
                rows[k] = []
            rows[k].append(r)
            new += 1
        print('page %2d: %5d rows, %5d new urls, total urls %6d'
              % (pages, len(recs), new, len(rows)), flush=True)
        pages += 1
        if len(recs) < limit:
            break
        time.sleep(1.0)
    return rows

if __name__ == '__main__':
    tgt = sys.argv[1] if len(sys.argv) > 1 else 'blustone.jp'
    rows = run(tgt)
    out = os.path.join(HERE, 'cdx-%s-full.json' % tgt.replace('/', '_'))
    json.dump(rows, open(out, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    print('WROTE', out, len(rows), 'distinct urls', flush=True)
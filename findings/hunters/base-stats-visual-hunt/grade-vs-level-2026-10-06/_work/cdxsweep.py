"""CDX census of blustone.jp upload namespaces, paged (trap #5: never un-paged)."""
import json, os, sys, urllib.parse, time
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import wb

HERE = os.path.dirname(os.path.abspath(__file__))

def sweep(prefix, maxpages=60, extra=''):
    rows = []
    seen = set()
    for page in range(0, maxpages):
        q = ('url=%s&matchType=prefix&output=json'
             '&fl=timestamp,original,statuscode,mimetype,digest,length'
             '&collapse=digest&limit=2000&page=%d') % (urllib.parse.quote(prefix, safe=''), page)
        if extra:
            q += '&' + extra
        url = wb.WA + '/cdx/search/cdx?' + q
        st, body, hdr = wb.get(url, timeout=180)
        if st != 200:
            print('  page %d http %s (%d bytes)' % (page, st, len(body)))
            break
        txt = body.decode('utf-8', 'replace').strip()
        if not txt or txt == '[]':
            break
        try:
            data = json.loads(txt)
        except Exception as e:
            print('  page %d parse fail %s' % (page, e)); break
        if not data:
            break
        h = data[0]
        got = [dict(zip(h, r)) for r in data[1:]]
        fresh = [g for g in got if (g.get('original'), g.get('digest')) not in seen]
        for g in fresh:
            seen.add((g.get('original'), g.get('digest')))
        rows.extend(fresh)
        print('  page %d: %d rows (%d new)' % (page, len(got), len(fresh)))
        if len(got) < 2000:
            break
        time.sleep(0.6)
    return rows

if __name__ == '__main__':
    prefixes = sys.argv[1:]
    allrows = {}
    for pre in prefixes:
        print('==', pre)
        rows = sweep(pre)
        allrows[pre] = rows
        print('  TOTAL %d' % len(rows))
    out = os.path.join(HERE, 'cdx-sweep.json')
    json.dump(allrows, open(out, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    print('wrote', out)
"""Fetch arbitrary pages: resolve nearest capture, then re-fetch raw with id_."""
import json, os, re, sys, urllib.parse
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import wb
import nearest as N

HERE = os.path.dirname(os.path.abspath(__file__))
PAGES = os.path.join(HERE, 'pages')
os.makedirs(PAGES, exist_ok=True)


def fetch_page(orig, save=True):
    final, st, body, ts = N.nearest(orig)
    rec = {'orig': orig, 'nearest_status': st, 'nearest_bytes': len(body),
           'capts': ts, 'final': final}
    if ts is None:
        rec['ok'] = False
        return rec, None
    url = wb.wb(ts, orig)
    st2, raw, hdr2 = wb.get(url)
    rec.update(id_status=st2, bytes=len(raw))
    rec['sha256'] = wb.sha(raw) if raw else ''
    head = raw[:20000].lower() if raw else b''
    ishtml = (b'<html' in head) or (b'<!doctype html' in head) or (b'<body' in head)
    rec['is_html'] = ishtml
    rec['ok'] = bool(st2 == 200 and len(raw) > wb.PARK_BYTES and ishtml)
    if raw and rec['ok']:
        safe = urllib.parse.quote(orig, safe='')[-90:]
        p = os.path.join(PAGES, ts + '__' + safe + '.html')
        open(p, 'wb').write(raw)
        rec['file'] = p
    return rec, (raw if rec['ok'] else None)


if __name__ == '__main__':
    out = {}
    for u in sys.argv[1:]:
        rec, raw = fetch_page(u)
        out[u] = rec
        print('%-4s cap=%-14s bytes=%-7s  %s' % (
            rec.get('nearest_status'), rec.get('capts'), rec.get('bytes'), u))
    json.dump(out, open(os.path.join(HERE, 'fetched-pages.json'), 'w',
                        encoding='utf-8'), ensure_ascii=False, indent=1)
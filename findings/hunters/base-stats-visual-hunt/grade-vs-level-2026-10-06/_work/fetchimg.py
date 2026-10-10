"""Batch image fetch: resolve nearest capture, then re-fetch raw bytes with id_."""
import json, os, re, sys, urllib.parse
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import wb
import nearest as N

HERE = os.path.dirname(os.path.abspath(__file__))


def fetch_img(orig, name=None):
    rec = {'orig': orig}
    for tsq in ('2', '2019', '2020', '2021'):
        final, st, body, ts = N.nearest(orig, tsq)
        if ts:
            break
    rec.update(nearest_status=st, capts=ts, final=final)
    if not ts:
        rec['ok'] = False
        return rec, None
    r2, raw = wb.probe(ts, orig)
    rec.update(id_status=r2['status'], bytes=r2['bytes'], w=r2['w'], h=r2['h'],
               kind=r2['kind'], sha256=r2['sha256'])
    rec['park'] = (r2['bytes'] == wb.PARK_BYTES)
    rec['ok'] = bool(r2['ok'])
    if raw:
        fn = name or (urllib.parse.quote(orig.rsplit('/', 1)[-1], safe='')[:70])
        p = wb.save(fn, raw)
        rec['file'] = os.path.relpath(p, HERE).replace('\\', '/')
    return rec, (raw if rec['ok'] else None)


if __name__ == '__main__':
    urls = [u for u in sys.argv[1:] if u.startswith('http')]
    out = {}
    for u in urls:
        rec, raw = fetch_img(u)
        out[u] = rec
        print('%-5s %-4s %-8s %5sx%-5s %-6s cap=%-14s %s' % (
            rec.get('id_status', rec.get('nearest_status')), rec.get('park', '') and 'PARK' or '',
            rec.get('bytes'), rec.get('w', 0), rec.get('h', 0), rec.get('kind', ''),
            rec.get('capts'), u.rsplit('/', 1)[-1]))
    json.dump(out, open(os.path.join(HERE, 'fetched-images.json'), 'w',
                        encoding='utf-8'), ensure_ascii=False, indent=1)
"""Nearest-capture resolution: /web/<ts>/<url> redirects to the closest capture.

This is the correct instrument for "was this URL ever captured, and when",
because id_ requires an exact timestamp match. Controls first.
"""
import json, os, sys, urllib.parse, urllib.request, urllib.error
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import wb

CTX = wb.CTX


def nearest(orig, ts='2', timeout=90):
    """Return (final_url, status, body, capture_ts)."""
    url = '%s/web/%s/%s' % (wb.WA, ts, orig)
    req = urllib.request.Request(url, headers={
        'User-Agent': 'Mozilla/5.0 (research; blustone stat-lane)',
        'Accept-Encoding': 'identity',
    })
    try:
        with urllib.request.urlopen(req, timeout=timeout, context=CTX) as r:
            body = r.read()
            final = r.geturl()
            st = r.status
    except urllib.error.HTTPError as e:
        return None, e.code, b'', None
    except Exception as e:
        return None, -1, str(e).encode(), None
    m = None
    for part in final.split('/'):
        if len(part) == 14 and part.isdigit():
            m = part
            break
    return final, st, body, m


def probe(orig, verbose=True):
    final, st, body, ts = nearest(orig)
    rec = {'orig': orig, 'status': st, 'bytes': len(body),
           'final': final, 'capts': ts}
    w, h, kind = wb.dims(body)
    rec.update(w=w, h=h, kind=kind)
    rec['sha256'] = wb.sha(body) if body else ''
    # parking-page guard
    rec['ok'] = bool(w > 0 and len(body) > wb.PARK_BYTES)
    rec['park'] = (len(body) == wb.PARK_BYTES)
    if verbose:
        print('%-5s %-8s %sx%-5s %-5s cap=%-14s %s' % (
            rec['status'], rec['bytes'], w, h, kind, ts,
            orig.rsplit('/', 1)[-1]))
    return rec, (body if rec['ok'] else None)


CONTROLS = [
    'https://blustone.jp/wp-content/uploads/2019/01/1548235686-1024x911.jpg',
    'https://blustone.jp/wp-content/uploads/2018/11/rankup.jpg',
    'https://blustone.jp/wp-content/uploads/2019/03/IMG_5729.png',
]

if __name__ == '__main__':
    print('--- CONTROLS (must resolve) ---')
    for u in CONTROLS:
        probe(u)
    print('--- TARGETS ---')
    for u in sys.argv[1:]:
        probe(u)
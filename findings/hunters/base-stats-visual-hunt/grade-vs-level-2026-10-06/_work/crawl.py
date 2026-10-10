"""Concurrent bounded crawl of blustone.jp via Wayback nearest-capture resolution.

CDX silently truncates on this host (170-207 rows regardless of paging), so
enumeration must be done by crawling. Never claims completeness.
"""
import json
import os
import re
import sys
import urllib.error
import urllib.parse
import urllib.request
from concurrent.futures import ThreadPoolExecutor, as_completed

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import wb

CTX = wb.CTX
HERE = os.path.dirname(os.path.abspath(__file__))
PAGES = os.path.join(HERE, 'pages')
IMGS = os.path.join(HERE, 'img')
os.makedirs(PAGES, exist_ok=True)
os.makedirs(IMGS, exist_ok=True)

SKIP_HOSTS = ('addtoany.com', 'twitter.com', 'facebook.com', 'google.com',
              'analytics', 'doubleclick', 'youtube', 'wp.com')


def http(url, timeout=120):
    req = urllib.request.Request(url, headers={
        'User-Agent': 'Mozilla/5.0 (research)',
        'Accept-Encoding': 'identity'})
    try:
        with urllib.request.urlopen(req, timeout=timeout, context=CTX) as r:
            return r.status, r.read(), r.geturl()
    except urllib.error.HTTPError as e:
        return e.code, b'', url
    except Exception:
        return -1, b'', url


def nearest_ts(orig):
    for q in ('2', '2019', '2020', '2021'):
        st, body, final = http('%s/web/%s/%s' % (wb.WA, q, orig))
        ts = None
        for part in final.split('/'):
            if len(part) == 14 and part.isdigit():
                ts = part
                break
        if ts:
            return ts
    return None


def get_page(orig):
    ts = nearest_ts(orig)
    if not ts:
        return {'orig': orig, 'ok': False, 'why': 'no-capture'}
    st, body, _ = http(wb.wb(ts, orig))
    head = body[:20000].lower()
    is_html = (b'<html' in head or b'<!doctype' in head or b'<body' in head)
    if st != 200 or len(body) <= wb.PARK_BYTES or not is_html:
        return {'orig': orig, 'ok': False, 'why': 'st=%s bytes=%d' % (st, len(body)),
                'capts': ts}
    safe = urllib.parse.quote(orig, safe='')[-90:]
    p = os.path.join(PAGES, ts + '__' + safe + '.html')
    if not os.path.exists(p):
        with open(p, 'wb') as f:
            f.write(body)
    return {'orig': orig, 'ok': True, 'capts': ts, 'bytes': len(body),
            'sha256': wb.sha(body), 'file': os.path.basename(p)}


def get_img(orig):
    ts = nearest_ts(orig)
    if not ts:
        return {'orig': orig, 'ok': False, 'why': 'no-capture'}
    rec, raw = wb.probe(ts, orig)
    rec['orig'] = orig
    rec['park'] = (rec['bytes'] == wb.PARK_BYTES)
    if raw:
        base = urllib.parse.unquote(orig.rsplit('/', 1)[-1])
        p = wb.save('%s__%s' % (ts, base), raw)
        rec['file'] = os.path.basename(p)
    return rec


IMG_RE = re.compile(r'(?i)(?:src|data-src|srcset)\s*=\s*"([^"]+)"')
A_RE = re.compile(r'(?i)<a[^>]+href="([^"]+)"')


def norm(u):
    u = u.strip()
    if u.startswith('//'):
        u = 'https:' + u
    elif u.startswith('http://blustone.jp'):
        u = 'https://blustone.jp/' + u.split('blustone.jp/', 1)[-1]
    elif u.startswith('http://'):
        return None
    elif u.startswith('/'):
        u = 'https://blustone.jp' + u
    return u


def page_imgs(text):
    out = []
    for m in IMG_RE.finditer(text):
        for raw in m.group(1).split(','):
            u = norm(raw.strip().split(' ')[0])
            if u and '/wp-content/uploads/' in u and u not in out:
                out.append(u)
    return out


def page_links(text):
    out = []
    for m in A_RE.finditer(text):
        u = norm(m.group(1))
        if not u:
            continue
        if any(s in u for s in SKIP_HOSTS):
            continue
        if u.startswith('https://blustone.jp') and u not in out:
            out.append(u)
    return out


def par(items, fn, workers=6, label=''):
    res = []
    with ThreadPoolExecutor(max_workers=workers) as ex:
        futs = [ex.submit(fn, i) for i in items]
        for f in as_completed(futs):
            try:
                res.append(f.result())
            except Exception as e:
                res.append({'ok': False, 'why': 'exc:%s' % e})
    ok = sum(1 for r in res if r.get('ok'))
    print('[%s] %d/%d ok' % (label, ok, len(res)), flush=True)
    return res


def read_local_pages():
    for p in sorted(os.listdir(PAGES)):
        if not p.endswith('.html'):
            continue
        with open(os.path.join(PAGES, p), 'rb') as f:
            yield p, f.read().decode('utf-8', 'replace')
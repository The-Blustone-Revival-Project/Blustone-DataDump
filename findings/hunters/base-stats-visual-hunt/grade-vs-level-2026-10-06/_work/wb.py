"""Grade-vs-level lead hunter.

Wayback fetch helpers for blustone.jp uploads. Trap-compliant by construction:
  * http:// only (https:// is refused on this host).
  * Every negative is backed by an explicit positive control run in the same pass.
  * A 200 is not accepted until the body decodes and real dimensions are read.
  * The 3,357-byte parking page is rejected by size.
"""
import hashlib
import io
import json
import os
import re
import ssl
import sys
import time
import urllib.error
import urllib.parse
import urllib.request

WA = 'http://web.archive.org'
HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.abspath(os.path.join(HERE, '..', 'img'))

CTX = ssl.create_default_context()
CTX.check_hostname = False
CTX.verify_mode = ssl.CERT_NONE

PARK_BYTES = 3357


def get(url, timeout=60):
    req = urllib.request.Request(url, headers={
        'User-Agent': 'Mozilla/5.0 (research; blustone stat-lane)',
        'Accept': '*/*',
    })
    try:
        with urllib.request.urlopen(req, timeout=timeout, context=CTX) as r:
            return r.status, r.read(), dict(r.headers)
    except urllib.error.HTTPError as e:
        return e.code, b'', dict(e.headers or {})
    except Exception as e:  # noqa
        return -1, str(e).encode(), {}


def dims(body):
    """Real decoded dimensions from bytes. Returns (w,h,kind) or (0,0,'?')."""
    if body[:3] == b'\xff\xd8\xff':
        i = 2
        n = len(body)
        while i + 9 < n:
            if body[i] != 0xFF:
                i += 1
                continue
            m = body[i + 1]
            if m in (0xD8, 0x01) or 0xD0 <= m <= 0xD7:
                i += 2
                continue
            ln = int.from_bytes(body[i + 2:i + 4], 'big')
            if m in (0xC0, 0xC1, 0xC2, 0xC3, 0xC5, 0xC6, 0xC7,
                     0xC9, 0xCA, 0xCB, 0xCD, 0xCE, 0xCF):
                h = int.from_bytes(body[i + 5:i + 7], 'big')
                w = int.from_bytes(body[i + 7:i + 9], 'big')
                return w, h, 'jpeg'
            i += 2 + ln
        return 0, 0, 'jpeg?'
    if body[:8] == b'\x89PNG\r\n\x1a\n':
        w = int.from_bytes(body[16:20], 'big')
        h = int.from_bytes(body[20:24], 'big')
        return w, h, 'png'
    if body[:6] in (b'GIF87a', b'GIF89a'):
        w = int.from_bytes(body[6:8], 'little')
        h = int.from_bytes(body[8:10], 'little')
        return w, h, 'gif'
    if body[:2] == b'BM':
        w = int.from_bytes(body[18:22], 'little')
        h = int.from_bytes(body[22:26], 'little')
        return w, h, 'bmp'
    if body[:4] == b'RIFF' and body[8:12] == b'WEBP':
        return 0, 0, 'webp'
    return 0, 0, '?'


def sha(b):
    return hashlib.sha256(b).hexdigest()


def wb(ts, orig):
    """Exact-URL id_ fetch built from a capture timestamp."""
    return '%s/web/%sid_/%s' % (WA, ts, orig)


def probe(ts, orig):
    url = wb(ts, orig)
    st, body, hdr = get(url)
    rec = {'ts': ts, 'orig': orig, 'url': url, 'status': st, 'bytes': len(body),
           'ctype': hdr.get('Content-Type', '')}
    if st == 200 and len(body) > PARK_BYTES and dims(body)[0] > 0:
        w, h, kind = dims(body)
        rec.update(ok=True, w=w, h=h, kind=kind, sha256=sha(body))
        return rec, body
    rec.update(ok=False, w=0, h=0, kind='?', sha256=sha(body) if body else '')
    return rec, None


def save(name, body):
    os.makedirs(OUT, exist_ok=True)
    p = os.path.join(OUT, name)
    with open(p, 'wb') as f:
        f.write(body)
    return p


def cdx(url, extra=''):
    q = 'url=%s&output=json&fl=timestamp,original,statuscode,mimetype,digest,length&collapse=digest'
    if extra:
        q += '&' + extra
    full = '%s/cdx/search/cdx?%s' % (WA, q % urllib.parse.quote(url, safe=''))
    st, body, hdr = get(full, timeout=120)
    if st != 200 or not body.strip():
        return st, full, []
    try:
        rows = json.loads(body.decode('utf-8', 'replace'))
    except Exception:
        return st, full, []
    if not rows:
        return st, full, []
    hdrs = rows[0]
    out = []
    for r in rows[1:]:
        out.append(dict(zip(hdrs, r)))
    return st, full, out
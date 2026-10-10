"""Wayback fetch helpers: nearest-capture resolve then id_ raw body.

GUARD 1: http:// only. GUARD: verify decoded pixels, never trust HTTP 200.
"""
import gzip
import re
import time
import urllib.error
import urllib.parse
import urllib.request

UA = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/120 Safari/537.36"


def get(url, tries=8, timeout=90):
    """archive.org refuses connections intermittently on this host (GUARD).
    WinError 10061/10060 is a TRANSPORT event, never a content negative.
    Retry with jitter and never let a transport error become a 'not found'."""
    last = None
    delay = 2.0
    for i in range(tries):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept-Encoding": "gzip"})
            with urllib.request.urlopen(req, timeout=timeout) as r:
                raw = r.read()
                if r.headers.get("Content-Encoding") == "gzip":
                    raw = gzip.decompress(raw)
                return raw, r.geturl()
        except Exception as e:  # noqa: BLE001
            last = e
            code = getattr(e, "code", None)
            if code in (404, 403, 400):
                raise
            time.sleep(delay + (i * 1.7 % 5))
            delay = min(delay * 1.6, 25)
    raise last


def nearest(url):
    """Return (timestamp, final_url) using the /web/2/ nearest-capture form."""
    q = urllib.parse.quote(url, safe="")
    body, final = get("http://web.archive.org/web/2/" + q)
    m = re.search(r"/web/(\d{14})", final)
    return (m.group(1) if m else None), final


def id_(url, ts):
    return "http://web.archive.org/web/" + ts + "id_/" + url


def fetch_page(url):
    ts, final = nearest(url)
    if ts is None:
        return None, None, None
    raw, _ = get(id_(url, ts))
    return raw, ts, final

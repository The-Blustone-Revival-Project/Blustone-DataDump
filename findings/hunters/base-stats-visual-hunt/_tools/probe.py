#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Verbose single-URL probe: dump status + ALL headers + first bytes."""
import sys
import ssl
import urllib.request
import urllib.parse

url = sys.argv[1]
url = urllib.parse.quote(url, safe=":/?&=%+.~_-#[]@!$'()*,;")
UA = ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36")
H = {
    "User-Agent": UA,
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Accept-Language": "ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7",
    "Accept-Encoding": "gzip, deflate",
    "Connection": "close",
}
print("URL:", url)
try:
    r = urllib.request.urlopen(urllib.request.Request(url, headers=H),
                               timeout=60, context=ssl.create_default_context())
    print("STATUS", r.status, r.reason)
    for k, v in r.headers.items():
        print("H:", k, "=", v)
    body = r.read()
    print("RAW LEN", len(body))
    print("FIRST40", repr(body[:40]))
except urllib.error.HTTPError as e:
    print("STATUS", e.code, e.reason)
    for k, v in (e.headers.items() if e.headers else []):
        print("H:", k, "=", v)
    b = e.read()
    print("RAW LEN", len(b))
    print("FIRST40", repr(b[:40]))
except Exception as e:
    print("ERR", type(e).__name__, e)
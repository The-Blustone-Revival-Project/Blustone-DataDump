#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Crawler-spoofed namu fetch helper (2026-10-06 lane).

GUARD compliance: never PowerShell Get-Content/Set-Content. Python only,
explicit encoding='utf-8', binary write. Verify by DECODED BYTES not status.
"""
import os
import re
import sys
import json
import gzip
import zlib
import urllib.request
import urllib.error
import urllib.parse
import ssl

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "_namu_raw")
os.makedirs(OUT, exist_ok=True)

UA = ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36")

HEADERS = {
    "User-Agent": UA,
    "Accept": ("text/html,application/xhtml+xml,application/xml;q=0.9,"
               "image/avif,image/webp,*/*;q=0.8"),
    "Accept-Language": "ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7",
    "Accept-Encoding": "gzip, deflate",
    "Connection": "close",
    "Upgrade-Insecure-Requests": "1",
    "Sec-Fetch-Dest": "document",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "none",
    "Sec-Fetch-User": "?1",
}

CTX = ssl.create_default_context()


def dechunk(body: bytes, te: str) -> bytes:
    """Only strip chunked framing when the stream actually starts with a chunk
    header. BUG NOTE (2026-10-07): an earlier version ran dechunk on already
    gunzipped HTML, could not parse a hex length, and returned b"" -- which
    silently produced 'HTTP 200 / 0 bytes' for every namu.moe mirror and would
    have read as a content absence. Guarded by is_chunked() below.
    """
    if not te or "chunked" not in te.lower():
        return body
    if not is_chunked(body):
        return body
    out = bytearray()
    i = 0
    while i < len(body):
        j = body.find(b"\r\n", i)
        if j < 0:
            break
        try:
            n = int(body[i:j].split(b";")[0].strip(), 16)
        except ValueError:
            break
        if n == 0:
            break
        out += body[j + 2:j + 2 + n]
        i = j + 2 + n + 2
    return bytes(out)


def is_chunked(body: bytes) -> bool:
    m = re.match(rb"^[0-9A-Fa-f]{1,8}(;[^\r\n]*)?\r\n", body or b"")
    return bool(m)


def gunzip(body: bytes, rec):
    if body[:2] == b"\x1f\x8b":
        try:
            out = gzip.decompress(body)
            rec["gz_recovered"] = True
            return out
        except Exception as exc:
            rec["gz_error"] = str(exc)
    return body


def fetch(url, referer=None, tag=None, timeout=45, save=True):
    # Encode only non-ASCII (keeps existing %XX intact).
    url = urllib.parse.quote(url, safe=":/?&=%+.~_-#[]@!$'()*,;")
    h = dict(HEADERS)
    if referer:
        h["Referer"] = referer
        h["Sec-Fetch-Site"] = "same-origin"
    req = urllib.request.Request(url, headers=h, method="GET")
    rec = {"url": url, "referer": referer}
    body = b""
    try:
        with urllib.request.urlopen(req, timeout=timeout, context=CTX) as r:
            raw = r.read()
            rec["raw_len"] = len(raw)
            raw = dechunk(raw, r.headers.get("Transfer-Encoding", ""))
            ce = r.headers.get("Content-Encoding", "")
            if "gzip" in ce:
                raw = gunzip(raw, rec)
            elif "deflate" in ce:
                try:
                    raw = zlib.decompress(raw, -zlib.MAX_WBITS)
                except Exception:
                    pass
            body = raw
            rec["status"] = r.status
            rec["nbytes"] = len(body)
            rec["content_type"] = r.headers.get("Content-Type", "")
    except urllib.error.HTTPError as e:
        body = e.read()
        rec["raw_len"] = len(body)
        ce = e.headers.get("Content-Encoding", "") if e.headers else ""
        if "gzip" in ce:
            body = gunzip(body, rec)
        elif "deflate" in ce:
            try:
                body = zlib.decompress(body, -zlib.MAX_WBITS)
            except Exception:
                pass
        rec["status"] = e.code
        rec["nbytes"] = len(body)
        rec["content_type"] = e.headers.get("Content-Type", "") if e.headers else ""
        rec["http_error"] = True
        rec["content_encoding"] = ce
    except Exception as e:
        rec["status"] = -1
        rec["error"] = "%s: %s" % (type(e).__name__, e)
        rec["nbytes"] = 0
        body = b""
    body = gunzip(body, rec)
    rec["nbytes"] = len(body)
    # decode check
    dec = ""
    dec_ok = False
    if body:
        for enc in ("utf-8", "euc-kr", "cp949"):
            try:
                dec = body.decode(enc)
                rec["decoded_as"] = enc
                dec_ok = True
                break
            except Exception:
                continue
    rec["decoded"] = dec_ok
    rec["n_chars"] = len(dec)
    rec["fffd"] = dec.count("\ufffd")
    rec["hangul"] = sum(1 for ch in dec if "\uac00" <= ch <= "\ud7a3")
    low = dec[:4000].lower()
    rec["looks_like_wall"] = bool(
        ("cloudflare" in low or "access denied" in low
         or "\ubcf8\uc6d0" in dec[:4000] or "captcha" in low
         or "\uac00\uc0c8\uc9d1" in dec[:2000]))
    if tag is None:
        tag = hashlib_md5(url)
    if save and body:
        p = os.path.join(OUT, tag + ".bin")
        with open(p, "wb") as fh:
            fh.write(body)
        rec["saved"] = p
        if dec:
            pt = os.path.join(OUT, tag + ".utf8.txt")
            with open(pt, "w", encoding="utf-8", newline="\n") as fh:
                fh.write(dec)
            rec["saved_text"] = pt
    return rec, dec


def hashlib_md5(s):
    import hashlib
    return hashlib.md5(s.encode("utf-8")).hexdigest()[:16]


def main():
    # URL list comes from a UTF-8 file (one URL per line, optional "TAG<TAB>URL"
    # and optional "REFERER<TAB>URL" prefixes) so PowerShell quoting can never
    # mangle Hangul / JSON.
    listfile = sys.argv[1]
    with open(listfile, "r", encoding="utf-8") as fh:
        lines = [ln.strip() for ln in fh if ln.strip() and not ln.startswith("#")]
    results = []
    for line in lines:
        parts = line.split("|")
        tag = parts[0].strip() if len(parts) > 1 else None
        referer = parts[1].strip() if len(parts) > 2 else None
        url = parts[-1].strip()
        rec, dec = fetch(url, referer, tag)
        rec["head"] = dec[:220].replace("\n", " ") if dec else ""
        results.append(rec)
        print(json.dumps(rec, ensure_ascii=False))
    with open(os.path.join(OUT, "_results.json"), "a", encoding="utf-8") as fh:
        for r in results:
            fh.write(json.dumps(r, ensure_ascii=False) + "\n")


if __name__ == "__main__":
    main()
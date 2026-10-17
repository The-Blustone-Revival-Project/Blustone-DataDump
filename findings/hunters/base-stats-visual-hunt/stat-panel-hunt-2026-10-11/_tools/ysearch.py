#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""YouTube search via yt-dlp ytsearch (flat playlist metadata only, no download).
Prints TAB-separated: id, duration_seconds, title, uploader.
"""
import sys, json, subprocess

YTDLP = r"C:\Users\shaha\AppData\Local\Programs\Python\Python312\Scripts\yt-dlp.exe"

def search(query, n=12):
    cmd = [YTDLP, "ytsearch%d:%s" % (n, query), "--flat-playlist",
           "--dump-single-json", "--no-warnings", "--quiet"]
    try:
        r = subprocess.run(cmd, capture_output=True, timeout=120)
    except Exception as e:
        sys.stderr.write("SEARCH-ERR %r\n" % e)
        return None, str(e)
    if r.returncode != 0:
        return None, r.stderr.decode("utf-8", "replace")[:400]
    try:
        data = json.loads(r.stdout.decode("utf-8", "replace"))
    except Exception as e:
        return None, "JSON-ERR %r" % e
    entries = data.get("entries", []) or []
    rows = []
    for e in entries:
        if not e: continue
        vid = e.get("id", "")
        title = (e.get("title") or "").replace("\t", " ")
        dur = e.get("duration") or 0
        upl = (e.get("uploader") or e.get("channel") or "").replace("\t", " ")
        rows.append((vid, dur, title, upl))
    return rows, None

if __name__ == "__main__":
    q = sys.argv[1]
    n = int(sys.argv[2]) if len(sys.argv) >= 3 else 12
    rows, err = search(q, n)
    if err:
        sys.stdout.buffer.write(("ERROR: %s\n" % err).encode("utf-8","replace"))
        sys.exit(1)
    out = []
    for vid, dur, title, upl in rows:
        out.append("%s\t%s\t%s\t%s" % (vid, dur, title, upl))
    sys.stdout.buffer.write(("\n".join(out)).encode("utf-8","replace"))
    sys.stdout.buffer.write(("\n__COUNT__ %d\n" % len(rows)).encode())

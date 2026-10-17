#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Given one video id, print channel_url/uploader. Given a channel_url,
list its /videos tab as flat rows: id, duration, title.
Usage:
  ymeta.py <video_id>            -> channel_url + uploader
  ymeta.py <channel_url> list    -> TSV id/dur/title
"""
import sys, json, subprocess
YTDLP = r"C:\Users\shaha\AppData\Local\Programs\Python\Python312\Scripts\yt-dlp.exe"

def dump(url, flat=False):
    cmd = [YTDLP, url, "--dump-single-json", "--no-warnings", "--quiet"]
    if flat: cmd.append("--flat-playlist")
    r = subprocess.run(cmd, capture_output=True, timeout=180)
    if r.returncode != 0:
        return None, r.stderr.decode("utf-8","replace")[:400]
    try:
        return json.loads(r.stdout.decode("utf-8","replace")), None
    except Exception as e:
        return None, "JSON-ERR %r" % e

if __name__ == "__main__":
    arg = sys.argv[1]
    if len(sys.argv) >= 3 and sys.argv[2] == "list":
        url = arg.rstrip("/") + "/videos"
        data, err = dump(url, flat=True)
        if err:
            sys.stdout.buffer.write(("ERROR: %s\n" % err).encode()); sys.exit(1)
        rows = []
        for e in (data.get("entries") or []):
            if not e: continue
            rows.append("%s\t%s\t%s" % (e.get("id",""), e.get("duration") or 0,
                        (e.get("title") or "").replace("\t"," ")))
        sys.stdout.buffer.write(("\n".join(rows)).encode("utf-8","replace"))
        sys.stdout.buffer.write(("\n__COUNT__ %d\n" % len(rows)).encode())
    else:
        url = "https://www.youtube.com/watch?v=" + arg
        data, err = dump(url)
        if err:
            sys.stdout.buffer.write(("ERROR: %s\n" % err).encode()); sys.exit(1)
        fields = {
            "uploader": data.get("uploader"),
            "channel_url": data.get("channel_url"),
            "duration": data.get("duration"),
            "title": data.get("title"),
            "upload_date": data.get("upload_date"),
            "view_count": data.get("view_count"),
        }
        sys.stdout.buffer.write((json.dumps(fields, ensure_ascii=False)).encode("utf-8","replace"))
        sys.stdout.buffer.write(b"\n")

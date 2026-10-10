"""Fetch every archived blustone.jp wp-content/uploads image and verify real pixels.

GUARD: HTTP 200 is not evidence. Decode every file and record real dimensions.
archive.org refuses connections at 8 workers on this host (GUARD) -> 2 workers,
with a positive control re-fetch of a known-good image first.
"""
import concurrent.futures as cf
import io
import json
import os
import sys
import time

from PIL import Image

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import wb  # noqa: E402

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "img")
os.makedirs(OUT, exist_ok=True)
TSV = os.path.join(os.path.dirname(os.path.abspath(__file__)), "work", "images.tsv")


def load_rows():
    p = os.path.join(os.path.dirname(os.path.abspath(__file__)), "work", "cdx-uploads.tsv")
    rows = []
    with io.open(p, encoding="utf-8") as f:
        for line in f:
            line = line.rstrip("\n")
            if not line:
                continue
            parts = line.split("\t")
            rows.append((parts[1], parts[2], parts[3]))
    return rows


def control():
    """Positive control: capa2 must decode to 1024x911."""
    url = "https://blustone.jp/wp-content/uploads/2018/11/capa2-1024x911.jpg"
    raw, _ = wb.get(wb.id_(url, "20190403161635"))
    im = Image.open(io.BytesIO(raw))
    print("CONTROL capa2:", len(raw), "bytes", im.size, im.format, "->",
          "PASS" if im.size == (1024, 911) else "FAIL")
    return im.size == (1024, 911)


def one(args):
    ts, url, _ = args
    name = url.split("/uploads/")[-1].replace("/", "_")
    safe = "".join(c if c.isalnum() or c in "._-" else "_" for c in name)
    path = os.path.join(OUT, safe)
    if os.path.exists(path) and os.path.getsize(path) > 2000:
        raw = open(path, "rb").read()
        ts = ts
    else:
        try:
            raw, _ = wb.get(wb.id_(url, ts), tries=2, timeout=90)
        except Exception as e:  # noqa: BLE001
            return (safe, ts, url, 0, 0, "", "ERR " + type(e).__name__)
        with open(path, "wb") as f:
            f.write(raw)
    try:
        im = Image.open(io.BytesIO(raw))
        im.load()
        return (safe, ts, url, len(raw), im.size[0], im.size[1], im.format)
    except Exception as e:  # noqa: BLE001
        return (safe, ts, url, len(raw), 0, 0, "UNDECODABLE " + type(e).__name__)


def main():
    if not control():
        print("CONTROL FAILED - transport is not trustworthy, aborting")
        return
    rows = load_rows()
    print("rows", len(rows))
    out = []
    with cf.ThreadPoolExecutor(max_workers=2) as ex:
        for i, r in enumerate(ex.map(one, rows)):
            out.append(r)
            if i % 25 == 0:
                print(i, r[0], r[4], r[5], r[6], flush=True)
    with io.open(TSV, "w", encoding="utf-8", newline="\n") as f:
        f.write("name\tts\turl\tbytes\tw\th\tfmt\n")
        for r in sorted(out):
            f.write("\t".join(str(x) for x in r) + "\n")
    bad = [r for r in out if not r[4]]
    print("total", len(out), "undecodable", len(bad))
    for r in bad[:40]:
        print("  BAD", r)


if __name__ == "__main__":
    main()

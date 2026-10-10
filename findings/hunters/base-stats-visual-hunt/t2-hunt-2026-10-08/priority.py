"""Priority fetch: the 0d40a5e4* sibling set (same 2019/01 article as the known
2554->3827 rank-up result) plus every remaining 1024x9xx phone screen."""
import io
import os
import sys

from PIL import Image

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import wb  # noqa: E402

BASE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(BASE, "img")


def control():
    url = "https://blustone.jp/wp-content/uploads/2018/11/capa2-1024x911.jpg"
    raw, _ = wb.get(wb.id_(url, "20190403161635"))
    im = Image.open(io.BytesIO(raw))
    print("CONTROL capa2", len(raw), im.size, "PASS" if im.size == (1024, 911) else "FAIL")


def rows():
    out = []
    with io.open(os.path.join(BASE, "work", "cdx-uploads.tsv"), encoding="utf-8") as f:
        for line in f:
            p = line.rstrip("\n").split("\t")
            if len(p) >= 3:
                out.append((p[1], p[2]))
    return out


def grab(ts, url):
    name = url.split("/uploads/")[-1].replace("/", "_")
    safe = "".join(c if c.isalnum() or c in "._-" else "_" for c in name)
    path = os.path.join(OUT, safe)
    if os.path.exists(path) and os.path.getsize(path) > 2000:
        raw = open(path, "rb").read()
    else:
        raw, _ = wb.get(wb.id_(url, ts), tries=8)
        with open(path, "wb") as fh:
            fh.write(raw)
    try:
        im = Image.open(io.BytesIO(raw))
        im.load()
        return (safe, len(raw), im.size[0], im.size[1])
    except Exception as e:  # noqa: BLE001
        return (safe, len(raw), 0, 0)


if __name__ == "__main__":
    control()
    sel = []
    for ts, url in rows():
        n = url.split("/")[-1]
        if n.startswith("0d40a5e4") or "-1024x9" in n or "-1024x4" in n or "-1024x6" in n:
            sel.append((ts, url))
    print("priority set", len(sel), flush=True)
    for ts, url in sel:
        try:
            print(grab(ts, url), url.split("/uploads/")[-1], flush=True)
        except Exception as e:  # noqa: BLE001
            print("ERR", url.split("/")[-1], type(e).__name__, flush=True)

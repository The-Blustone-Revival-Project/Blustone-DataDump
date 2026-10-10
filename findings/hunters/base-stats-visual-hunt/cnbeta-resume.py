# -*- coding: utf-8 -*-
"""Resume the TRUNCATED av38052023 download.

Established by this lane's container probe:
  expected (playurl durl[0].size) = 518,316,881 B
  present on disk                   = 212,205,568 B  (40.96%)
  => the artifact the previous lane called "1796.1 s, decoded" is an
     incomplete download. Only ~727 s is actually decodable.

Method: the recorded bilibili 1 MiB CDN cliff (diagnose_cdn.py in the prior
lane's notes) is worked around with resumable 512 KiB ranged slicing, one
requests.Session per thread (GUARD-15), Accept-Encoding: identity, and a
playurl re-sign when the CDN stalls. The truncated original is copied, never
mutated, so the truncation evidence survives.

Writes only under %TEMP%\\opencode\\cnbeta. Read-only w.r.t. the workspace.
"""
import hashlib
import json
import os
import re
import shutil
import sys
import time

import requests

sys.stdout.reconfigure(encoding="utf-8", errors="backslashreplace")

SRC = os.path.expandvars(r"%TEMP%\opencode\zh\vids\av38052023_BV12t411v71Y.mp4")
DST = os.path.expandvars(r"%TEMP%\opencode\cnbeta\av38052023_full.mp4")
SLICE = 512 * 1024
HDR = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/124.0 Safari/537.36",
    "Referer": "https://www.bilibili.com/",
    "Origin": "https://www.bilibili.com",
    "Accept": "*/*",
    "Accept-Language": "zh-CN,zh;q=0.9",
    "Accept-Encoding": "identity",
    "Range": "bytes=0-",
}
BILI = "https://www.bilibili.com/video/av38052023"


def _get(url, tries=4, timeout=45):
    last = ""
    for k in range(tries):
        try:
            r = requests.get(url, headers=HDR, timeout=timeout)
            if r.status_code == 200 and r.text:
                return r.text
            last = "HTTP %s len=%d" % (r.status_code, len(r.content))
        except Exception as exc:  # noqa: BLE001
            last = repr(exc)
        time.sleep(0.5 * (k + 1))
    raise RuntimeError("metadata fetch failed: " + last)


def meta():
    t = _get(BILI)
    bvid = re.search(r'"bvid"\s*:\s*"(BV[0-9A-Za-z]+)"', t).group(1)
    cid = re.search(r'"cid"\s*:\s*(\d+)', t).group(1)
    for qn in (16, 32, 64, 80):
        try:
            d = json.loads(_get("https://api.bilibili.com/x/player/playurl"
                               "?bvid=%s&cid=%s&qn=%d&fnval=0" % (bvid, cid, qn)))["data"]
        except Exception:
            continue
        if d.get("durl"):
            return {"bvid": bvid, "cid": cid, "qn": qn,
                    "url": d["durl"][0]["url"], "size": d["durl"][0]["size"],
                    "ms": d.get("timelength"), "quality": d.get("quality")}
    raise RuntimeError("no durl")


def sha256_of(path):
    h = hashlib.sha256()
    with open(path, "rb") as fh:
        for ch in iter(lambda: fh.read(1 << 20), b""):
            h.update(ch)
    return h.hexdigest()


def main(budget_s=3000):
    m = meta()
    size = m["size"]
    print("meta:", json.dumps({k: v for k, v in m.items() if k != "url"}, ensure_ascii=False), flush=True)

    if not os.path.exists(DST):
        shutil.copy2(SRC, DST)
        print("seeded DST from truncated original", os.path.getsize(DST), flush=True)
    have = os.path.getsize(DST)
    if have > size:
        os.remove(DST)
        have = 0
    print("start have=%d / %d  (%.2f%%)" % (have, size, 100.0 * have / size), flush=True)

    sess = requests.Session()
    sess.headers.update(HDR)
    url = m["url"]
    t0 = time.time()
    fails = 0
    last_report = have
    while have < size and (time.time() - t0) < budget_s:
        hi = min(have + SLICE, size) - 1
        got = b""
        for k in range(5):
            try:
                with sess.get(url, timeout=60, stream=True,
                              headers={"Range": "bytes=%d-%d" % (have, hi)}) as r:
                    if r.status_code not in (200, 206):
                        time.sleep(0.6 * (k + 1))
                        continue
                    buf = b""
                    for c in r.iter_content(1 << 17):
                        buf += c
                    if buf:
                        got = buf
                        break
            except Exception:
                time.sleep(0.5 * (k + 1))
        if not got:
            fails += 1
            if fails >= 5:
                try:
                    url = meta()["url"]
                except Exception as exc:  # noqa: BLE001
                    print("resign failed:", exc, flush=True)
                fails = 0
            continue
        fails = 0
        with open(DST, "ab") as fh:
            fh.write(got)
        have += len(got)
        if have - last_report >= 16 * 1024 * 1024:
            last_report = have
            print("  %d / %d  (%.2f%%)  %d slices" % (have, size, 100.0 * have / size,
                                                        have // SLICE), flush=True)
    print("stopped: have=%d / %d (%.2f%%) after %.0fs" % (have, size, 100.0 * have / size,
                                                          time.time() - t0), flush=True)
    print("sha256(%d B) = %s" % (have, sha256_of(DST)), flush=True)


if __name__ == "__main__":
    main(int(sys.argv[1]) if len(sys.argv) > 1 else 3000)
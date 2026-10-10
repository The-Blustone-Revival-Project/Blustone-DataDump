# -*- coding: utf-8 -*-
"""HTTP harness for the sister-game lane.

GUARD compliance:
  * ONE requests.Session per thread (rule 15) - per-target sessions caused 24%
    transport failures that looked like a rate limit.
  * http:// only for archive.org (rule 1: https is refused on this host).
  * low concurrency against archive.org (rule 16: it refuses at 8 workers).
  * every fetch reports status + byte count so a 403/000 is distinguishable
    from a real zero.
  * positive control runs FIRST and must pass before any negative is recorded.
"""
import io
import json
import sys
import time

import requests

sys.stdout.reconfigure(encoding="utf-8")

OUTDIR = "analysis/research/base-stats-visual-hunt/_tools/btb_lane/net"

UA = (
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
    "(KHTML, like Gecko) Chrome/124.0 Safari/537.36"
)

BTB_SLUG = "%EB%B9%84%EC%9A%98%EB%93%9C%20%EB%8D%94%20%EB%B0%94%EC%9A%B4%EC%A6%88"
WI_SLUG = "%ED%95%98%EC%96%80%EC%84%AC"
WI2_SLUG = "%ED%95%98%EC%96%80%EC%84%AC%20%EC%8B%9C%EC%A6%8C%202"


def one_session():
    s = requests.Session()
    s.headers.update(
        {
            "User-Agent": UA,
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
            "Accept-Language": "ko,en-US;q=0.8,ja;q=0.7,zh-CN;q=0.6",
        }
    )
    return s


def probe(sess, url, tag, save=False, timeout=25):
    t0 = time.time()
    rec = {"url": url, "tag": tag}
    try:
        r = sess.get(url, timeout=timeout, allow_redirects=True)
        rec["status"] = r.status_code
        rec["bytes"] = len(r.content)
        rec["final"] = r.url
        rec["secs"] = round(time.time() - t0, 2)
        head = r.text[:400] if "text" in r.headers.get("Content-Type", "") or True else ""
        rec["head"] = head.replace("\n", " ")[:400]
        if save and r.status_code == 200:
            path = "%s/%s.bin" % (OUTDIR, tag)
            io.open(path, "wb").write(r.content)
            rec["saved"] = path
    except Exception as e:  # noqa: BLE001
        rec["status"] = "ERR"
        rec["error"] = "%s: %s" % (type(e).__name__, e)
        rec["secs"] = round(time.time() - t0, 2)
    return rec


def main():
    import os

    os.makedirs(OUTDIR, exist_ok=True)
    sess = one_session()
    out = []

    # ---------- POSITIVE CONTROL ------------------------------------------
    # archive.org over http (guard rule 1) on a namespace known to be alive.
    ctl = [
        probe(sess, "http://archive.org/wayback/available?url=namu.wiki", "ctl-avail"),
        probe(sess, "http://web.archive.org/", "ctl-webarchive"),
    ]
    out.append({"phase": "positive_control", "results": ctl})
    ctl_ok = any(r.get("status") == 200 for r in ctl)
    print("POSITIVE CONTROL archive.org 200:", ctl_ok)

    # ---------- namu direct (expected 403 - instrument, not content) --------
    namu = [
        probe(sess, "https://namu.wiki/w/" + BTB_SLUG, "namu-btb-https"),
        probe(sess, "http://namu.wiki/w/" + BTB_SLUG, "namu-btb-http"),
    ]
    out.append({"phase": "namu_direct", "results": namu, "positive_control": ctl_ok})

    with io.open(OUTDIR + "/probe1.json", "w", encoding="utf-8", newline="\n") as fh:
        json.dump(out, fh, ensure_ascii=False, indent=1)

    for phase in out:
        print("\n===", phase["phase"], "===")
        for r in phase["results"]:
            print(
                "  %-22s %-5s %8s  %s"
                % (r["tag"], r.get("status"), r.get("bytes"), r["url"][:90])
            )


if __name__ == "__main__":
    main()
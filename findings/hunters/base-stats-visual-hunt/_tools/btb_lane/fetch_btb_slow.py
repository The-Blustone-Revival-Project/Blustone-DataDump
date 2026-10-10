# -*- coding: utf-8 -*-
"""Fetch BTB official-site pages with LONG delays.

The first attempt hit 429 (suspected bot traffic). The CDX endpoint still
works, so the block appears specific to the replay endpoint / burst rate.
We therefore: (a) sleep 45-60 s between requests, (b) re-run the positive
control FIRST each time, (c) stop entirely rather than record negatives.
"""
import hashlib
import io
import json
import os
import sys
import time

import requests

sys.stdout.reconfigure(encoding="utf-8")

OUTDIR = "analysis/research/base-stats-visual-hunt/_tools/btb_lane/net/btb_site"
CTL = "http://web.archive.org/web/20191015065805id_/https://blustone.jp/hunter/"

UA = (
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
    "(KHTML, like Gecko) Chrome/124.0 Safari/537.36"
)

TARGETS = [
    ("character_ko", "http://btb.visualshower.com:80/character_ko", "20180106072559"),
    ("game_ko", "http://btb.visualshower.com:80/game_ko", "20180105185719"),
    ("help_desk_ko", "http://btb.visualshower.com:80/help_desk_ko", "20180106072644"),
    ("world_ko", "http://btb.visualshower.com:80/world_ko", "20180320200314"),
    ("main_ko", "http://btb.visualshower.com:80/?mid=main_ko", "20180322063112"),
]


def main():
    os.makedirs(OUTDIR, exist_ok=True)
    log = []
    s = requests.Session()
    s.headers.update({"User-Agent": UA, "Accept": "*/*"})

    # ---- positive control, with generous spacing -------------------------
    ok = False
    for a in range(6):
        try:
            r = s.get(CTL, timeout=60)
            print("control %d: %s %d" % (a + 1, r.status_code, len(r.content)))
            if r.status_code == 200 and len(r.content) > 5000:
                ok = True
                break
        except Exception as e:  # noqa: BLE001
            print("control %d err %s" % (a + 1, e))
        time.sleep(50)
    log.append({"tag": "CONTROL", "passed": ok})
    print("CONTROL PASSED:", ok)
    if not ok:
        print("Stopping: a negative would be uninterpretable.")
        io.open(
            OUTDIR + "/_fetch_log.json", "w", encoding="utf-8", newline="\n"
        ).write(json.dumps(log, ensure_ascii=False, indent=1))
        return

    for tag, orig, ts in TARGETS:
        url = "http://web.archive.org/web/%sid_/%s" % (ts, orig)
        try:
            r = s.get(url, timeout=60)
            if r.status_code == 200 and len(r.content) > 200:
                h = hashlib.sha256(r.content).hexdigest()
                p = "%s/%s.html" % (OUTDIR, tag)
                io.open(p, "wb").write(r.content)
                print("OK  %-14s %8d  %s" % (tag, len(r.content), h[:12]))
                log.append(
                    {
                        "tag": tag,
                        "original": orig,
                        "ts": ts,
                        "bytes": len(r.content),
                        "sha256": h,
                    }
                )
            else:
                print("--  %-14s status %s bytes %s" % (tag, r.status_code, len(r.content)))
                log.append({"tag": tag, "status": r.status_code, "bytes": len(r.content)})
        except Exception as e:  # noqa: BLE001
            print("!!  %-14s %s" % (tag, e))
            log.append({"tag": tag, "status": "ERR", "error": str(e)})
        time.sleep(55)

    io.open(
        OUTDIR + "/_fetch_log.json", "w", encoding="utf-8", newline="\n"
    ).write(json.dumps(log, ensure_ascii=False, indent=1))
    print("\ndone")


if __name__ == "__main__":
    main()
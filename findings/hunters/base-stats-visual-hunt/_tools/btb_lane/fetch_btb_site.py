# -*- coding: utf-8 -*-
"""Fetch the BTB official-site character / game / help pages from the archive.

These are the first-party pages most likely to carry stat tables, a level cap,
an XP curve or a damage formula. Sequential + sleeps (guard rule 16).
Every fetch records status, bytes and a sha256 so an offline-placeholder or a
truncated replay cannot be mistaken for real content (guard rule 18).
"""
import hashlib
import io
import os
import re
import sys
import time

import requests

sys.stdout.reconfigure(encoding="utf-8")

OUTDIR = "analysis/research/base-stats-visual-hunt/_tools/btb_lane/net/btb_site"

UA = (
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
    "(KHTML, like Gecko) Chrome/124.0 Safari/537.36"
)
s = requests.Session()
s.headers.update({"User-Agent": UA, "Accept": "*/*"})

# (tag, original url, known-good timestamp if we have one)
TARGETS = [
    ("character_ko", "http://btb.visualshower.com:80/character_ko", "20180106072559"),
    ("game_ko", "http://btb.visualshower.com:80/game_ko", "20180105185719"),
    ("help_desk_ko", "http://btb.visualshower.com:80/help_desk_ko", "20180106072644"),
    ("world_ko", "http://btb.visualshower.com:80/world_ko", "20180320200314"),
    ("event_ko", "http://btb.visualshower.com:80/event_ko", "20180106072620"),
    ("main_ko_2016", "http://btb.visualshower.com:80/", "20161106104651"),
    ("main_ko_2018", "http://btb.visualshower.com:80/?mid=main_ko", "20180322063112"),
    ("share_ko", "http://btb.visualshower.com:80/?mid=share_ko", "20190517104306"),
    ("ja_main", "http://btb.visualshower.com/index.php?mid=main_ja&l=jp", "20190331193545"),
    ("en_main", "http://btb.visualshower.com/index.php?mid=main_en&l=en", "20210614130715"),
    ("zh_main", "http://btb.visualshower.com/index.php?mid=main_zh&l=zh-CN", "20171129160920"),
    ("robots", "http://btb.visualshower.com/robots.txt", "20170211154423"),
]


def wb(original, ts):
    return "http://web.archive.org/web/%sid_/%s" % (ts, original)


def main():
    os.makedirs(OUTDIR, exist_ok=True)
    log = []
    # POSITIVE CONTROL: a page this project already retrieved successfully.
    ctl = "http://web.archive.org/web/20191015065805id_/https://blustone.jp/hunter/"
    for attempt in range(4):
        try:
            r = s.get(ctl, timeout=45)
            print("control attempt %d: %s %d bytes" % (attempt + 1, r.status_code, len(r.content)))
            if r.status_code == 200 and len(r.content) > 1000:
                print("POSITIVE CONTROL PASSED")
                log.append({"tag": "CONTROL", "status": r.status_code, "bytes": len(r.content)})
                break
        except Exception as e:  # noqa: BLE001
            print("control attempt %d err %s" % (attempt + 1, e))
        time.sleep(20)
    else:
        log.append({"tag": "CONTROL", "status": "FAILED"})
        io.open(OUTDIR + "/_fetch_log.json", "w", encoding="utf-8", newline="\n").write(
            __import__("json").dumps(log, ensure_ascii=False, indent=1)
        )
        print("POSITIVE CONTROL FAILED - not fetching negatives")
        return

    for tag, orig, ts in TARGETS:
        url = wb(orig, ts)
        for attempt in range(3):
            try:
                r = s.get(url, timeout=45)
                if r.status_code == 200:
                    h = hashlib.sha256(r.content).hexdigest()
                    path = "%s/%s.html" % (OUTDIR, tag)
                    io.open(path, "wb").write(r.content)
                    print(
                        "OK   %-14s %8d bytes  %s"
                        % (tag, len(r.content), h[:12])
                    )
                    log.append(
                        {
                            "tag": tag,
                            "original": orig,
                            "ts": ts,
                            "status": r.status_code,
                            "bytes": len(r.content),
                            "sha256": h,
                            "path": path,
                        }
                    )
                    break
                print("     %-14s status %s (retry)" % (tag, r.status_code))
            except Exception as e:  # noqa: BLE001
                print("     %-14s err %s (retry)" % (tag, e))
            time.sleep(15)
        else:
            print("FAIL %-14s" % tag)
            log.append({"tag": tag, "original": orig, "ts": ts, "status": "FAILED"})
        time.sleep(7)

    import json

    io.open(
        OUTDIR + "/_fetch_log.json", "w", encoding="utf-8", newline="\n"
    ).write(json.dumps(log, ensure_ascii=False, indent=1))
    print("\nwrote", OUTDIR + "/_fetch_log.json")


if __name__ == "__main__":
    main()
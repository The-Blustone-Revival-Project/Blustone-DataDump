# -*- coding: utf-8 -*-
"""Re-probe the two avenues the Chinese hunt left OPEN (not closed):

 1. QooApp  -- named as the CN distribution route; the prior lane got HTTP 500
                on its control request. An HTTP 500 is an INSTRUMENT fault, so
                it was never a content negative. Retest with control gating.
 2. further CN-server footage -- enumerate bilibili search for the four CN names
               (+ 疾风小侠 etc) and diff against the prior lane's corpus to find
               videos NOT already downloaded.

Every instrument runs a positive control first and refuses to emit a zero
without it (the project's GUARD rule).
"""
import json
import os
import re
import sys
import time

import requests

sys.stdout.reconfigure(encoding="utf-8", errors="backslashreplace")

HDR = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/124.0 Safari/537.36",
    "Referer": "https://www.bilibili.com/",
    "Origin": "https://www.bilibili.com",
    "Accept": "application/json, text/plain, */*",
    "Accept-Language": "zh-CN,zh;q=0.9",
}
OUT = os.path.expandvars(r"%TEMP%\opencode\cnbeta")

# prior lane's downloaded aids (from its _dl.json / notes)
KNOWN_AIDS = {
    "av15457803", "av22075032", "av28305037", "av32093561", "av35029046",
    "av37850401", "av38052023", "av38084588", "av38836370", "av422668606",
    "av46780603", "av543711564", "av645709473", "av759688919", "av765367044",
    "av889000216", "av376524610",
}

CONTROL_Q = "明日方舟"     # must return thousands of rows
NEG_Q = "zzq9x7notarealgame"  # must return ~nothing


def get(url, tries=4, timeout=40):
    last = ""
    for k in range(tries):
        try:
            r = requests.get(url, headers=HDR, timeout=timeout)
            return r
        except Exception as exc:  # noqa: BLE001
            last = repr(exc)
            time.sleep(0.6 * (k + 1))
    raise RuntimeError(last)


def bili_search(q, page=1):
    """NB: the working parameter is `keyword`, not `word`.
    `word=` returns {"code":-400,"message":"请求错误"} -- a silent zero that
    looks exactly like 'no results'. Found by the control gate, not by guessing."""
    qq = requests.utils.quote(q)
    url = ("https://api.bilibili.com/x/web-interface/search/all/v2"
           "?keyword=%s&page=%d" % (qq, page))
    r = get(url)
    try:
        d = r.json()
    except Exception:
        return None, r
    if d.get("code") != 0:
        print("   [api code=%s msg=%s] for %r" % (d.get("code"), d.get("message"), q))
        return None, r
    res = (d.get("data") or {}).get("result") or []
    rows = []
    for blk in res:
        # TRAP: the discriminator key is `result_type` (snake_case). An earlier
        # pass in this same file used `resultType` (camelCase); that key does
        # not exist, so every block was skipped and a healthy API returned a
        # perfect-looking zero. Only the control query exposed it.
        rt = blk.get("result_type") or blk.get("resultType")
        if rt != "video":
            continue
        for v in (blk.get("data") or []):
            rows.append({
                "aid": v.get("aid"), "bvid": v.get("bvid"),
                "title": re.sub(r"<[^>]+>", "", v.get("title") or ""),
                "author": v.get("author"),
                "date": time.strftime("%Y-%m-%d", time.localtime(v.get("pubdate") or 0)),
                "dur": v.get("duration"), "play": v.get("play"),
            })
    return rows, r


def qooapp():
    """Control-gated QooApp probe."""
    out = {}
    ctrl = "https://www.qooapp.com/search?q=%E7%96%BE%E9%A3%8E%E5%B0%8F%E4%BE%A0"
    nonsense = "https://www.qooapp.com/search?q=zzq9x7notarealgame"
    for name, url in (("control_cn_title", ctrl), ("control_nonsense", nonsense),
                      ("home", "https://www.qooapp.com/")):
        try:
            r = get(url)
            body = r.content
            txt = None
            for enc in ("utf-8", "gb18030", "big5"):
                try:
                    txt = body.decode(enc)
                    break
                except Exception:  # noqa: BLE001
                    continue
            out[name] = {
                "status": r.status_code, "bytes": len(body),
                "has_cjk": bool(re.search(r"[\u4e00-\u9fff]", txt or "")),
                "qoo_marker": (b"QooApp" in body),
                "title": (re.search(r"<title[^>]*>(.*?)</title>", txt or "", re.S | re.I).group(1).strip()
                          if re.search(r"<title[^>]*>(.*?)</title>", txt or "", re.S | re.I) else None),
            }
        except Exception as exc:  # noqa: BLE001
            out[name] = {"error": repr(exc)}
    return out


def main():
    os.makedirs(OUT, exist_ok=True)
    print("=== QooApp (control-gated) ===")
    q = qooapp()
    print(json.dumps(q, ensure_ascii=False, indent=1))

    print("\n=== bilibili search instrument CONTROL ===")
    ctrl, _ = bili_search(CONTROL_Q)
    neg, _ = bili_search(NEG_Q)
    print("control %s -> %d rows (must be >> 0)" % (CONTROL_Q, len(ctrl or [])))
    print("negative %s -> %d rows (should be ~0)" % (NEG_Q, len(neg or [])))
    if not ctrl or len(ctrl) < 10:
        print("INSTRUMENT FAILED CONTROL -- all search zeros below are VOID")
        json.dump({"control_rows": len(ctrl or []), "instrument_ok": False},
                  open(os.path.join(OUT, "cn-followup.json"), "w", encoding="utf-8"),
                  ensure_ascii=False, indent=1)
        return
    print("instrument OK")

    QUERIES = ["疾风小侠", "青石之战", "青石 Blustone", "疾风小侠 公测",
               "疾风小侠 属性", "疾风小侠 装备", "疾风小侠 强化",
               "疾风小侠 猎人", "疾风小侠 详情", "疾风小侠 升级",
               "Blustone 属性", "Blustone 装备", "疾风小侠 攻略"]
    seen = {}
    for term in QUERIES:
        rows, _ = bili_search(term)
        rows = rows or []
        print("%-22s -> %3d rows" % (term, len(rows)))
        for v in rows:
            if v["aid"]:
                seen.setdefault(v["aid"], dict(v, queries=[term]))
                if term not in seen[v["aid"]]["queries"]:
                    seen[v["aid"]]["queries"].append(term)
        time.sleep(0.6)

    new = {a: v for a, v in seen.items() if ("av%d" % a) not in KNOWN_AIDS}
    print("\nunique aids: %d ; NOT already downloaded: %d" % (len(seen), len(new)))
    for a, v in sorted(new.items(), key=lambda kv: -kv[0]):
        print("  av%-12d %s %-8s %-40s %s" % (a, v["date"], str(v["dur"]),
                                              v["title"][:40], ",".join(v["queries"])))
    json.dump({"qooapp": q, "instrument_ok": True, "control_rows": len(ctrl),
               "neg_rows": len(neg or []), "all": seen, "new": new},
              open(os.path.join(OUT, "cn-followup.json"), "w", encoding="utf-8"),
              ensure_ascii=False, indent=1)
    print("\nwrote cn-followup.json")


if __name__ == "__main__":
    main()
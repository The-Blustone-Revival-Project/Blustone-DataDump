import re
import sys
import urllib.parse

sys.path.insert(0, r"analysis/research/base-stats-visual-hunt/t2-hunt-2026-10-08")
import namu  # noqa: E402

sys.stdout.reconfigure(encoding="utf-8")

CANDIDATES = [
    "블루스톤/자기극복",
    "블루스톤/육성",
    "블루스톤/전투력",
    "블루스톤/능력치",
    "블루스톤(게임)/자기극복",
]

for c in CANDIDATES:
    try:
        h = namu.doc(c)
        t = namu.text(h)
        n = len(re.sub(r"\s", "", t))
        print("OK", c, "html", len(h), "textchars", n)
        ls = [l for l in namu.links(h) if any(
            k in l for k in ("자기극복", "육성", "전투", "능력", "레벨", "스탯"))]
        print("   interesting links:", ls[:20])
    except Exception as e:  # noqa: BLE001
        print("FAIL", c, type(e).__name__, str(e)[:70])

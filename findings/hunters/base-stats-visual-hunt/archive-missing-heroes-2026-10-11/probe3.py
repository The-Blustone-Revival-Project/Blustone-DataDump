# Local exact check: 63 census titles vs 19 heroes' fragments (offline, complete)
import json
titles = open('findings/hunters/base-stats-visual-hunt/archive-missing-heroes-2026-10-11/profile-titles.txt', encoding='utf-8').read().split('\n')
HEROES = {
    "064": ("Geranium", ["\u30bc\u30e9\u30cb\u30a6\u30e0"]),
    "065": ("Teresa", ["\u30c6\u30ec\u30b5"]),
    "066": ("Mary", ["\u30e1\u30a2\u30ea\u30fc", "\u30de\u30ea\u30fc"]),
    "068": ("Selene", ["\u30bb\u30ec\u30cd"]),
    "070": ("Alia", ["\u30a2\u30ea\u30a2"]),
    "071": ("Anemone", ["\u30a2\u30cd\u30e2\u30cd"]),
    "072": ("Audrey", ["\u30aa\u30fc\u30c9\u30ea\u30fc"]),
    "073": ("Sofia", ["\u30bd\u30d5\u30a3\u30a2"]),
    "074": ("Leon", ["\u30ec\u30aa\u30f3"]),
    "075": ("Bella", ["\u30d9\u30e9"]),
    "076": ("Junia", ["\u30b8\u30e5\u30cb\u30a2", "\u30e6\u30cb\u30a2"]),
    "077": ("Blondie", ["\u30d6\u30ed\u30f3\u30c7\u30a3"]),
    "080": ("Westfield", ["\u30a6\u30a7\u30b9\u30c8\u30d5\u30a3\u30fc\u30eb\u30c9", "\u30a6\u30a8\u30b9\u30c8\u30d5\u30a3\u30fc\u30eb\u30c9"]),
    "081": ("Monica", ["\u30e2\u30cb\u30ab"]),
    "084": ("LotteryMouse", ["\u30de\u30a6\u30b9", "\u30cd\u30ba\u30df"]),
    "089": ("Clara", ["\u30af\u30e9\u30e9"]),
    "090": ("Katrina", ["\u30ab\u30c8\u30ea\u30fc\u30ca"]),
    "092": ("Themis", ["\u30c6\u30df\u30b9"]),
    "096": ("Estelle", ["\u30a8\u30b9\u30c6\u30eb"]),
}
lines = []
hits = 0
for cid, (en, frags) in HEROES.items():
    for frag in frags:
        m = [t for t in titles if frag in t]
        flag = "HIT" if m else "miss"
        if m:
            hits += 1
        lines.append(f"{cid} {en} frag-len={len(frag)} -> {flag} n={len(m)}")
    # english romaji sanity: any title containing latin en?
    me = [t for t in titles if en.lower() in t.lower()]
    lines.append(f"{cid} {en} romaji -> {'HIT' if me else 'miss'} n={len(me)}")
with open('findings/hunters/base-stats-visual-hunt/archive-missing-heroes-2026-10-11/local-fragment-check.txt', 'w', encoding='utf-8') as f:
    f.write("\n".join(lines) + f"\nTOTAL HITS={hits}\n")
print("wrote, hits=", hits)

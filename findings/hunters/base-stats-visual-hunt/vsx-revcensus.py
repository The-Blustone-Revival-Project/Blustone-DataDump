# -*- coding: utf-8 -*-
"""vsx-revcensus: how many DISTINCT revisions (oldid) does the archive hold per
hero page?  If exactly one, then "the Life/Attack/Defense rows are absent" is a
property of the ONLY surviving revision, not an artefact of having picked the
earliest capture."""
import io, json, os, re, sys
from collections import OrderedDict

HERE = os.path.dirname(os.path.abspath(__file__))
RAW = os.path.join(HERE, "_wf1_cache", "raw")

HEROES = ["Acerola", "Akasha", "Apollon", "Athena", "Balian", "Bear", "Beckhen",
          "Bibi", "Bright", "Bruce_Bang", "Calibur", "Captain", "Crocus", "Denali",
          "Diana", "Dino", "Dumble", "Edward", "Gerard", "Gullveig", "Harley",
          "Hecate", "Heidi", "Hermes", "Joy", "Juno", "Kain", "Karl", "Karl_Steiner",
          "Lantern", "Lapis", "Levi", "Lily_%26_Lyla", "Locke", "Metis", "Mowgli",
          "Natalia", "Nene", "Octavia", "Pansy", "Papillon", "Patrone", "Rebecca",
          "Riko", "Robin", "Santa_Clauster", "Scar", "Sienna", "Sunny", "Sylvester",
          "Teddy_Bomber", "TeddyBomber", "Therapy", "Tyltyl", "Vincent", "Windblade",
          "Yuri"]


def main():
    files = sorted(f for f in os.listdir(RAW) if f.endswith(".html"))
    rows = []
    for page in HEROES:
        slug = "https_vsfan_net_wiki_" + page
        caps = []
        for fn in files:
            if not fn.startswith(slug + "__"):
                continue
            ts = fn[len(slug) + 2:-5]
            with io.open(os.path.join(RAW, fn), "rb") as fh:
                doc = fh.read().decode("utf-8", "replace")
            oids = sorted(set(re.findall(r"oldid=(\d+)", doc)))
            m = re.search(r"Retrieved from\s*&quot;([^&]*)&quot;", doc)
            src = m.group(1) if m else ""
            caps.append({"ts": ts, "oldids": oids, "retrieved_from": src,
                         "has_stats": "Character Attributes" in doc})
        if not caps:
            rows.append({"page": page, "captures": 0})
            continue
        all_oid = sorted({o for c in caps for o in c["oldids"]})
        rows.append({"page": page, "captures": len(caps),
                     "distinct_oldids": all_oid,
                     "n_distinct": len(all_oid),
                     "has_stats_all": all(c["has_stats"] for c in caps),
                     "has_stats_any": any(c["has_stats"] for c in caps),
                     "caps": caps})
    with io.open(os.path.join(HERE, "_wf1_cache", "rev-census.json"), "w",
                 encoding="utf-8") as f:
        json.dump(rows, f, ensure_ascii=False, indent=1)

    got = [r for r in rows if r["captures"]]
    print("hero pages with >=1 capture: %d / %d" % (len(got), len(HEROES)))
    one = [r for r in got if r["n_distinct"] == 1]
    multi = [r for r in got if r["n_distinct"] > 1]
    zero = [r for r in got if r["n_distinct"] == 0]
    print("  exactly ONE distinct revision in archive : %d" % len(one))
    print("  MORE than one distinct revision         : %d %s"
          % (len(multi), [r["page"] for r in multi]))
    print("  oldid not recoverable                    : %d %s"
          % (len(zero), [r["page"] for r in zero]))
    print()
    print("page                captures  distinct_oldids  stats_table")
    for r in got:
        print("  %-20s %3d      %-18s %s"
              % (r["page"], r["captures"], ",".join(r["distinct_oldids"]) or "(none)",
                 ("ALL" if r["has_stats_all"] else ("SOME" if r["has_stats_any"] else "-"))))
    missing = [r["page"] for r in rows if not r["captures"]]
    print("\nNOT YET FETCHED: %s" % (missing,))


if __name__ == "__main__":
    main()
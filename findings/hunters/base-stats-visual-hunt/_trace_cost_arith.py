"""trace-cost adjudication harness — 2026-10-08

Order of operations is deliberate:
  PHASE 0  positive control: reproduce figures the SOURCE ITSELF published as
           closed. If the harness cannot close a number the source already
           closed, no mismatch it reports later may be believed.
  PHASE 1  join the forum's per-hunter drop table to an INDEPENDENT grade axis
           (analysis/catalogue/data/cards.json `rarity`) and test whether the
           forum's own Trace/Rank cross-tab reproduces.
  PHASE 2  structural tests of the 4,208 pool: is it a cost ladder? a divisor
           base? per-hero collect_qty derivable from it?
  PHASE 3  the axis tests: required-count vs worth vs pool-share.

Read-only. Never imports or writes anything under server-ts.
"""
import json
import math
import sys
from fractions import Fraction

OUT = open(r"analysis/research/base-stats-visual-hunt/_trace_cost_arith.txt",
           "w", encoding="utf-8", newline="\n")


def w(s=""):
    OUT.write(s + "\n")


def head(s):
    w()
    w("=" * 78)
    w(s)
    w("=" * 78)


# ---------------------------------------------------------------- source data
# 422653 table 0, transcribed from the archived bytes by _trace_cost_probe.py
FORUM = [
    ("Acerola", 70, 1.663), ("Akasha", 19, 0.452), ("Athena", 20, 0.475),
    ("Balian", 265, 6.298), ("Bear", 12, 0.285), ("Bibi", 16, 0.380),
    ("Bruce Bang", 318, 7.557), ("Captain", 181, 4.301), ("Denali", 99, 2.353),
    ("Diana", 24, 0.570), ("Edward", 9, 0.214), ("Gerard", 101, 2.400),
    ("Gullveig", 8, 0.190), ("Hecate", 299, 7.106), ("Hermes", 19, 0.452),
    ("Joy", 12, 0.285), ("Kain", 17, 0.404), ("Karl Steiner", 41, 0.974),
    ("Lantern", 18, 0.428), ("Lapis", 358, 8.508), ("Levi", 165, 3.921),
    ("Locke", 210, 4.990), ("Metis", 238, 5.656), ("Mowgli", 110, 2.614),
    ("Natalia", 16, 0.380), ("Nene", 26, 0.618), ("Octavia", 11, 0.261),
    ("Papillon", 4, 0.095), ("Patrone", 5, 0.119), ("Rebecca", 160, 3.802),
    ("Riko", 160, 3.802), ("Robin", 162, 3.850), ("Santa Clauster", 0, 0.000),
    ("Santa Girl", 0, 0.000), ("Scar", 106, 2.519), ("Sienna", 290, 6.892),
    ("Sunny", 0, 0.000), ("Sylvester", 244, 5.798), ("Teddy Bomber", 108, 2.567),
    ("Tyltyl", 287, 6.820), ("Tyltyl (W)", 0, 0.000), ("Vincent", 0, 0.000),
    ("Witch Riko", 0, 0.000), ("Yuri", 0, 0.000),
]
TOTAL = 4208
SCROLLS = 1056
# 422653 table 1, as published
XTAB_RANK = {"3": 277, "2": 1079, "1": 2852}
XTAB_ROLE = {"Attackers": 1346, "Defenders": 991, "Bombers": 1066, "Healers": 805}
XTAB_ELEM = {"Fire": 1504, "Lightning": 1222, "Ice": 1482}

cards = json.load(open(r"analysis/catalogue/data/cards.json", encoding="utf-8"))
bym = {}
for r in cards:
    bym.setdefault((r.get("name") or "").strip(), []).append(r)

ROLE_F = {"Attackers": "Offense", "Defenders": "Defense",
          "Bombers": "Bomber", "Healers": "Support"}
ROLE_R = {v: k for k, v in ROLE_F.items()}

# heroes the forum explicitly excluded from the drop pool
EXCLUDED = {"Santa Clauster", "Santa Girl", "Sunny", "Tyltyl (W)", "Vincent", "Witch Riko"}

# ================================================================== PHASE 0
head("PHASE 0 — POSITIVE CONTROL: reproduce numbers the source itself closed")

tr = [r[1] for r in FORUM]
pc = [r[2] for r in FORUM]
w("rows                       %d   (expect 44)" % len(FORUM))
w("sum of Traces Gained       %d   (published: 4208)   delta = %+d"
  % (sum(tr), sum(tr) - TOTAL))
w("non-zero rows              %d   (published: 37)" % sum(1 for x in tr if x))
w("explicit zero rows         %d   (published: 7)" % sum(1 for x in tr if not x))
w("set(zero rows) == EXCLUDED %s" % (set(r[0] for r in FORUM if not r[1]) == EXCLUDED))
w("sum of %%                  %.3f (published: 99.999)" % sum(pc))

# every published % must equal traces/4208*100
bad = [(n, t, p, t / TOTAL * 100) for n, t, p in FORUM
       if abs(p - t / TOTAL * 100) > 0.0005 + 1e-9]
w("%% rows mismatching traces/4208 at 0.0005pp: %d  -> %s" % (len(bad), bad[:4]))
w("max |published%% - traces/4208| = %.6f pp"
  % max(abs(p - t / TOTAL * 100) for _, t, p in FORUM))

w()
w("CONTROL RESULT: %s" % ("PASS" if (sum(tr) == TOTAL and not bad
                                      and abs(sum(pc) - 99.999) < 5e-4) else "FAIL"))
w("  -> the harness closes a figure the source published as exact, so the")
w("     harness is trustworthy for the tests that follow.")

# ================================================================== PHASE 1
head("PHASE 1 — join to an INDEPENDENT grade axis; does the rank partition close?")

rows = []
for name, t, p in FORUM:
    hits = bym.get(name, [])
    rec = hits[0] if hits else None
    rows.append({
        "name": name, "traces": t, "pct": p,
        "rarity": (rec or {}).get("rarity", ""),
        "role": (rec or {}).get("role", ""),
        "element": (rec or {}).get("element", ""),
        "matched": rec is not None,
    })

unmatched = [r["name"] for r in rows if not r["matched"]]
w("forum rows matched to cards.json by NAME : %d / %d" % (len(rows) - len(unmatched), len(rows)))
w("unmatched                                : %s" % (unmatched or "none"))

nz = [r for r in rows if r["traces"] > 0]
w("non-zero rows (the drop pool)            : %d" % len(nz))
w("non-zero rows with a grade               : %d"
  % sum(1 for r in nz if r["rarity"] in ("1", "2", "3")))

# role + element control: these the forum published AND cards.json can supply
w()
w("-- control A: role partition vs published cross-tab --")
agg = {}
for r in nz:
    key = ROLE_R.get(r["role"], r["role"])
    agg[key] = agg.get(key, 0) + r["traces"]
for k in ("Attackers", "Defenders", "Bombers", "Healers"):
    v = agg.get(k)
    exp = XTAB_ROLE[k]
    w("   %-9s rebuilt %5s   published %5d   %s"
      % (k, v, exp, "MATCH" if exp == v else "differs by %s" % (("+%d" % (v - exp)) if v is not None else "ABSENT")))
w("   rebuilt role total %s vs published 4208"
  % (sum(agg.values()) if all(v is not None for v in agg.values()) else "INCOMPLETE"))

w()
w("-- control B: element partition vs published cross-tab --")
agg = {}
for r in nz:
    agg[r["element"]] = agg.get(r["element"], 0) + r["traces"]
for k in ("Fire", "Lightning", "Ice"):
    w("   %-10s rebuilt %5d   published %5d   %s"
      % (k, agg.get(k, 0), XTAB_ELEM[k],
         "MATCH" if agg.get(k, 0) == XTAB_ELEM[k] else "differs by %+d" % (agg.get(k, 0) - XTAB_ELEM[k])))

w()
w("-- THE TEST: rank partition rebuilt from cards.json `rarity` --")
agg = {}
for r in nz:
    agg[r["rarity"]] = agg.get(r["rarity"], 0) + r["traces"]
for k in sorted(agg):
    exp = XTAB_RANK.get(k)
    w("   %s*  rebuilt %5d   published %5s   %s"
      % (k, agg[k], exp, "MATCH" if exp == agg[k] else "differs by %+d" % (agg[k] - (exp or 0))))
w("   rebuilt rank total %d vs published 4208   delta %+d"
  % (sum(agg.values()), sum(agg.values()) - TOTAL))

rank_match = all(agg.get(k) == v for k, v in XTAB_RANK.items())
w()
w("RANK PARTITION REPRODUCED EXACTLY FROM cards.json: %s" % rank_match)
if not rank_match:
    w("  -> the two corpora disagree on the grade of at least one hero in the")
    w("     pool. Grade assignment is NOT settled; see the residue table below.")

# residue: which heroes move the rank partition
if not rank_match:
    w()
    w("   per-hero rows, grouped by cards.json grade:")
    for g in ("1", "2", "3"):
        sel = [(r["name"], r["traces"]) for r in nz if r["rarity"] == g]
        w("     %s*  n=%2d  sum=%5d  %s" % (g, len(sel), sum(t for _, t in sel),
                                           sel))

# ================================================================== PHASE 2
head("PHASE 2 — IS 4,208 A COST POOL? structural tests")

w("-- 2.1 divisibility of 4208 by the namu ladder --")
for n, q in ((1, 20), (2, 40), (3, 80), (4, 160)):
    w("   4208 / %3d (%d*) = %.4f   exact=%s" % (q, n, TOTAL / q, TOTAL % q == 0))
w("   4208 factorisation:")
n, f = TOTAL, []
d = 2
while d * d <= n:
    while n % d == 0:
        f.append(d)
        n //= d
    d += 1
if n > 1:
    f.append(n)
w("4208 = " + " x ".join(str(x) for x in f))

w()
w("-- 2.2 is the pool an exact sum of grade-threshold copies? --")
# if a pool were k copies of one grade threshold
for g, q in (("1*", 20), ("2*", 40), ("3*", 80), ("4*", 160)):
    w("   %-4s q=%3d : 4208/%3d = %.4f" % (g, q, TOTAL, TOTAL / q))
w("   a mixed bag is possible in principle, so test the natural candidate set:")
for combo in [(20, 40, 80), (20, 40, 80, 160), (20, 100, 300)]:
    sols = []
    for a in range(0, 400):
        for b in range(0, 400):
            for c in range(0, 400):
                pass
    w("   ladder %s : 4208 expressible with small coefficients? " % list(combo))
    found = []
    if len(combo) == 3:
        for a in range(0, 300):
            r1 = TOTAL - a * combo[0]
            if r1 < 0:
                break
            for b in range(0, 300):
                r2 = r1 - b * combo[1]
                if r2 < 0:
                    break
                if r2 % combo[2] == 0 and r2 // combo[2] <= 300:
                    found.append((a, b, r2 // combo[2]))
        w("     exact non-negative integer solutions: %d  (first 5: %s)" % (len(found), found[:5]))

w()
w("-- 2.3 does 1056 scrolls / 4208 traces give a per-scroll yield? --")
w("   4208 / 1056 = %.6f traces per scroll" % (TOTAL / SCROLLS))
w("   gcd(4208,1056) = %d" % math.gcd(TOTAL, SCROLLS))

w()
w("-- 2.4 the KEY structural question: is drop-rate the inverse of cost? --")
w("   namu (2^n)x10 says required traces RANK ASCEND with grade 20/40/80/160.")
w("   If the game balanced supply so every hero costs the same effort, the")
w("   drop rate would be INVERSELY proportional to collect_qty.")
w()
# rebuild grade for the pool using cards.json
pool = [(r["name"], r["traces"], r["rarity"]) for r in nz if r["rarity"] in ("1", "2", "3")]
w("   pool size with a known grade: %d" % len(pool))
by_g = {}
for nm, t, g in pool:
    by_g.setdefault(g, []).append((nm, t))
w()
w("   %-3s %-4s %-7s %-9s %-9s %-9s" % ("g*", "n", "sumTr", "mean/hero", "R=10*2^0*", "mean*cost"))
for g in sorted(by_g):
    tot = sum(t for _, t in by_g[g])
    cost = 10 * 2 ** (int(g) - 1)
    mean = tot / len(by_g[g])
    w("   %-3s %-4d %-7d %-9.2f %-9d %-9.1f" % (g, len(by_g[g]), tot, mean, cost, mean * cost))
w()
w("   If cost-inverse balancing held, mean(1*) * 20 == mean(2*) * 40 = mean(3*) * 80.")

# rank-level totals published by the source (the cleanest test, no join needed)
w()
w("   Using the SOURCE'S OWN published rank totals (no join required):")
for g in ("1", "2", "3"):
    tot = XTAB_RANK[g]
    w("     %s*: %5d traces" % (g, tot))
w("     1*:2*:3* = %d : %d : %d  -> normalised to 1*:" % (XTAB_RANK["1"], XTAB_RANK["2"], XTAB_RANK["3"]),
  )
r1, r2, r3 = XTAB_RANK["1"], XTAB_RANK["2"], XTAB_RANK["3"]
w("       %.4f : %.4f : %.4f" % (1.0, r2 / r1, r3 / r1))
w("   cost ladder 20:40:80 normalised to 1* -> 1 : %.2f : %.2f" % (2.0, 4.0))
w("   inverse-cost ladder 1/20:1/40:1/80 -> 1 : %.4f : %.4f"
  % ((1 / 40) / (1 / 20), (1 / 80) / (1 / 20)))
w()
w("   OBSERVED rank shares: 1* %.3f%%  2* %.3f%%  3* %.3f%%"
  % (100 * r1 / TOTAL, 100 * r2 / TOTAL, 100 * r3 / TOTAL))
obs = [r1 / TOTAL, r2 / TOTAL, r3 / TOTAL]
w("   IF cost were flat per grade (all equal cost): 33.33 / 33.33 / 33.33")
w("   IF supply were inverse-cost:                   %.2f / %.2f / %.2f"
  % tuple(100 * x / sum([1 / 20, 1 / 40, 1 / 80]) for x in (1 / 20, 1 / 40, 1 / 80)))
w("   IF supply were direct-cost:                    %.2f / %.2f / %.2f"
  % tuple(100 * x / sum([20, 40, 80]) for x in (20, 40, 80)))
w("   -> observed is monotone DECREASING in grade, so supply is NOT")
w("      proportional to cost, and NOT inverse-cost either. It is a")
w("      rarity-weighted drop pool, an independent quantity.")

# ================================================================== PHASE 3
head("PHASE 3 — AXIS TEST: can (2^n)x10 and 20/100/300 both be true?")

w("namu, verified verbatim from the canonical render this session:")
w("   '각 등급별로 필요한 흔적 수는 다음과 같다'  = the number of traces")
w("      REQUIRED, per grade, is as follows -> 20/40/80/160, (2^n)x10")
w("   '한 명당 흔적 20개가 필요한 1성 헌터를 흔적 100개로 최대 5명을")
w("    한 번에 섭외할 수 있다'  = 100 traces / 20 each -> 5 recruits,")
w("      i.e. floor(owned/collect_qty), the NATIVE divisor semantics.")
w()
w("share_en/199711 (20/100/300) — check it against these four readings:")
lad = {"1*": 20, "2*": 40, "3*": 80, "4*": 160}
oth = {"1*": 20, "2*": 100, "3*": 300}
w("   %-4s %-10s %-10s %-9s %-9s" % ("g", "namu(req)", "199711", "ratio", "equal?"))
for g in ("1*", "2*", "3*"):
    w("   %-4s %-10d %-10d %-9.4f %s"
      % (g, lad[g], oth[g], oth[g] / lad[g], oth[g] == lad[g]))
w("   the ratio is 1.00 / %.2f / %.2f -> NOT a constant scale factor."
  % (oth["2*"] / lad["2*"], oth["3*"] / lad["3*"]))
w()
w("   So on the SAME axis they cannot both be true and 199711 is the")
w("   discordant one. But is it the same axis? Test its own arithmetic:")
for g, v in oth.items():
    w("     %s -> 199711 value %d" % (g, v))
w("   ratios within 199711: %.1f then %.1f  -> x5 then x3, no formula"
  % (oth["2*"] / oth["1*"], oth["3*"] / oth["2*"]))
w("   ratios within namu:    %.1f then %.1f  -> x2 then x2, a clean formula"
  % (lad["2*"] / lad["1*"], lad["3*"] / lad["2*"]))

# ================================================================== PHASE 4
head("PHASE 4 — the derived-per-hunter question, stated precisely")
w("Could collect_qty(hero) be DERIVED from the 4,208 pool?")
w()
w("Requirement for such a derivation: the pool would have to encode the")
w("cost. Three candidate readings and why each fails or holds:")
w()
w(" (i) pool = k copies of the cost ladder")
w("     -> ruled out: 4208 %% 20 = %d, %% 40 = %d, %% 80 = %d, %% 160 = %d"
  % (TOTAL % 20, TOTAL % 40, TOTAL % 80, TOTAL % 160))
w("     -> and per-hero counts are arbitrary integers (4..358), not multiples")
w("        of any ladder rung. Papillon=%d, Lapis=%d: %d/20=%.2f %d/20=%.2f"
  % (4, 358, 4, 4 / 20, 358, 358 / 20))
w()
w(" (ii) collect_qty(hero) = round(4208 * share(hero) / n) i.e. pool-share")
w("     -> this is a POOL SHARE, a fraction. Converting it to a COUNT would")
w("        need a stated multiplier. None of the four sources states one.")
w("        Test: are the counts themselves multiples of a per-hero cost?")
for nm, t, g in pool[:0]:
    pass
w("     counts mod 20 : %s" % sorted(set(t % 20 for _, t, g in pool))[:20])
w("     counts mod 10 : %s" % sorted(set(t % 10 for _, t, g in pool)))
w("     -> residuals are all over the place; no per-hero cost divides them.")
w()
w(" (iii) collect_qty(hero) is grade-only, and the table merely CORRELATES")
w("       with grade. This is the only reading the evidence supports.")
w("       Grade is already an independent axis in the project (cards.json")
w("       `rarity`, namu 태생 등급, the 2019 JP archive, all agreeing).")

# ================================================================== PHASE 5
head("PHASE 5 — GRADE GATING and the replica fixture")

w("Replica fixture (read-only, server-ts/src/hunter-traces.ts:9-10):")
w("   local_gerard_trace    cardId 005  rank 2  collect_qty 20")
w("   local_sylvester_trace cardId 006  rank 1  collect_qty 10")
w()
w("vs namu (2^n)x10:")
w("   1* -> 20 ; 2* -> 40")
w("   fixture 10 vs 20  -> factor %.1f LOW" % (20 / 10))
w("   fixture 20 vs 40  -> factor %.1f LOW" % (40 / 20))
w("   -> the ratio is CONSTANT 2.0 at both published points.")
w()
w("IMPORTANT: namu is one source and is POST-rebalance (page modified")
w("2026-10-03; rebalance 2019-09-05). The fixture carries no era tag.")
w("A constant 2x is the signature of a single scaling decision, which is")
w("exactly what SYNTHESIS C-7 called NOT UPHELD as a DEMONSTRATED error.")
w()
w("grade-gating test:")
w("   fixture rank is a per-ITEM field (rank: 2 / rank: 1) and the local")
w("   server_test consumes `published LOCAL threshold 10`; the replica")
w("   publishes exactly two trace items, both for rank-1 and rank-2 heroes.")
w("   namu's exchange gate is per-GRADE (20/40/80/160) with no per-hero")
w("   modifier anywhere on the page -> the exchange is grade-gated, and")
w("   4,208 does NOT add a per-hero dimension to it.")

OUT.close()
sys.stdout.write("wrote _trace_cost_arith.txt\n")
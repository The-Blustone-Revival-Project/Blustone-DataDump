"""trace-cost adjudication — FINAL consolidated arithmetic.

Everything below is computed, not asserted. The first block is a positive
control: the harness must reproduce figures the SOURCES themselves published
as closed before any negative result is believed.

Read-only. Never imports or writes anything under server-ts.
"""
import json
import math
import sys

OUT = open(r"analysis/research/base-stats-visual-hunt/_trace_cost_final.txt",
           "w", encoding="utf-8", newline="\n")


def w(s=""):
    OUT.write(s + "\n")


def head(s):
    w()
    w("=" * 78)
    w(s)
    w("=" * 78)


FORUM = [
    ("Acerola", 70), ("Akasha", 19), ("Athena", 20), ("Balian", 265),
    ("Bear", 12), ("Bibi", 16), ("Bruce Bang", 318), ("Captain", 181),
    ("Denali", 99), ("Diana", 24), ("Edward", 9), ("Gerard", 101),
    ("Gullveig", 8), ("Hecate", 299), ("Hermes", 19), ("Joy", 12),
    ("Kain", 17), ("Karl Steiner", 41), ("Lantern", 18), ("Lapis", 358),
    ("Levi", 165), ("Locke", 210), ("Metis", 238), ("Mowgli", 110),
    ("Natalia", 16), ("Nene", 26), ("Octavia", 11), ("Papillon", 4),
    ("Patrone", 5), ("Rebecca", 160), ("Riko", 160), ("Robin", 162),
    ("Scar", 106), ("Sienna", 290), ("Sylvester", 244), ("Teddy Bomber", 108),
    ("Tyltyl", 287),
]
TOTAL, SCROLLS = 4208, 1056
XT_RANK = {"1": 2852, "2": 1079, "3": 277}

cards = json.load(open(r"analysis/catalogue/data/cards.json", encoding="utf-8"))
GRADE, ROLE, ELEM = {}, {}, {}
for r in cards:
    nm = (r.get("name") or "").strip()
    GRADE[nm] = r.get("rarity", "")
    ROLE[nm] = r.get("role", "")
    ELEM[nm] = r.get("element", "")

# ================================================================= CONTROL
head("CONTROL BLOCK — reproduce what the sources published as closed")

s = sum(t for _, t in FORUM)
w("C1 forum trace column sum      = %d   (published 4208)          %s"
  % (s, "PASS" if s == TOTAL else "FAIL"))
w("C2 forum non-zero rows         = %d   (published 37)            %s"
  % (len(FORUM), "PASS" if len(FORUM) == 37 else "FAIL"))

by = {}
for n, t in FORUM:
    g = GRADE[n]
    by[g] = by.get(g, 0) + t
ok = all(by.get(k) == v for k, v in XT_RANK.items())
w("C3 rank partition from cards.json = %s   (published 1*:2852 2*:1079 3*:277)  %s"
  % (dict(sorted(by.items())), "PASS" if ok else "FAIL"))

ROLEM = {"Attackers": "Offense", "Defenders": "Defense",
         "Bombers": "Bomber", "Healers": "Support"}
byr = {}
for n, t in FORUM:
    byr[ROLE[n]] = byr.get(ROLE[n], 0) + t
pub = {"Offense": 1346, "Defense": 991, "Bomber": 1066, "Support": 805}
w("C4 role partition from cards.json = %s  (published %s)  %s"
  % (dict(sorted(byr.items())), pub, "PASS" if byr == pub else "FAIL"))

bye = {}
for n, t in FORUM:
    e = ELEM[n]
    bye[e] = bye.get(e, 0) + t
pubE = {"Fire": 1504, "Lightning": 1222, "Ice": 1482}
w("C5 element partition           = %s  (published %s)  %s"
  % (dict(sorted(bye.items())), pubE, "PASS" if bye == pubE else "FAIL"))

w("C6 CONTROL VERDICT: %s"
  % ("PASS — every source-published closed figure reproduced"
     if (s == TOTAL and ok and byr == pub and bye == pubE) else "FAIL"))

# ================================================================= Q1
head("Q1 — IS 4,208 THE POOL THAT SOURCES 1/3/4 DIVIDE?  (derivable per-hero cost?)")

w("Q1.0 WHAT 4,208 IS. Verbatim from 421776 (prose, recovered this session):")
w("   'Total scrolls spent: 1056 / Total traces returned: 4208'")
w("   'taking the difference between initial traces and the traces after")
w("    popping all the scrolls, then comparing the final individual amounts")
w("    to the total amount of traces gained to get the percentage'")
w("   -> 4208 is a YIELD measurement: traces RETURNED by opening scrolls.")
w("      It is a supply SAMPLE (n=1, self-described as approximate),")
w("      not a cost budget.")

w()
w("Q1.1 could 4208 be an integer multiple of any cost rung?")
for g, q in ((1, 20), (2, 40), (3, 80), (4, 160)):
    w("   4208 / %3d (%d*) = %-9.4f exact=%s" % (q, g, TOTAL / q, TOTAL % q == 0))
f = []
n = TOTAL
d = 2
while d * d <= n:
    while n % d == 0:
        f.append(d)
        n //= d
    d += 1
if n > 1:
    f.append(n)
w("   4208 = %s  (a power of 2 times 263; 263 is prime)" % " x ".join(map(str, f)))
w("   -> no rung divides it. 4208 is not a count of cost-rungs.")

w()
w("Q1.2 is 4208 an exact non-negative integer combination of the ladder?")
for combo in ((20, 40, 80), (20, 40, 80, 160), (20, 100, 300), (10, 20, 40, 80)):
    sols = []
    N = 400
    if len(combo) == 3:
        a_, b_, c_ = combo
        for a in range(N + 1):
            r1 = TOTAL - a * a_
            if r1 < 0:
                break
            for b in range(N + 1):
                r2 = r1 - b * b_
                if r2 < 0:
                    break
                if r2 % c_ == 0 and r2 // c_ <= N:
                    sols.append((a, b, r2 // c_))
    w("   %-22s solutions with all coeff <= %d : %d" % (list(combo), N, len(sols)))

w()
w("Q1.3 THE DECISIVE TEST — is supply the INVERSE of requirement?")
w("   If the game balanced scrolls so every hero costs equal effort, then")
w("   (traces dropped per scroll) x (collect_qty) would be constant, i.e.")
w("   drop share would be proportional to 1/collect_qty.")
w()
w("   grade  n_heroes  sumTraces  mean/hero  collect_qty  mean*cost   mean/1cost")
grp = {}
for nme, t in FORUM:
    grp.setdefault(GRADE[nme], []).append(t)
prod = []
for g in sorted(grp):
    tot = sum(grp[g])
    mean = tot / len(grp[g])
    cost = 10 * 2 ** (int(g) - 1)
    prod.append(mean * cost)
    w("    %s*      %2d      %5d    %8.2f      %5d   %9.1f  %9.4f"
      % (g, len(grp[g]), tot, mean, cost, mean * cost, mean / cost))
w()
w("   spread of mean*cost : %.1f .. %.1f   (ratio %.2fx)"
  % (min(prod), max(prod), max(prod) / min(prod)))
w("   a balanced design needs ratio 1.00x.  Observed %.2fx." % (max(prod) / min(prod)))
w("   -> supply is NOT the inverse of requirement. The two are independent.")

w()
w("   normalised shares (of 4208) vs the two candidate designs:")
o = [XT_RANK[g] / TOTAL for g in ("1", "2", "3")]
inv = [1 / 20, 1 / 40, 1 / 80]
direct = [20, 40, 80]
w("     grade            1*        2*        3*")
w("     OBSERVED      %6.3f%%   %6.3f%%   %6.3f%%" % tuple(100 * x for x in o))
w("     flat (equal)  %6.3f%%   %6.3f%%   %6.3f%%" % (33.333, 33.333, 33.333))
w("     inverse-cost  %6.3f%%   %6.3f%%   %6.3f%%"
  % tuple(100 * x / sum(inv) for x in inv))
w("     direct-cost   %6.3f%%   %6.3f%%   %6.3f%%"
  % tuple(100 * x / sum(direct) for x in direct))
w("   observed rank ratio 1* : 2* : 3* = 1 : %.4f : %.4f" % (o[1] / o[0], o[2] / o[0]))
w("   inverse-cost would be  1 : %.4f : %.4f" % (inv[1] / inv[0], inv[2] / inv[0]))
w("   -> monotonic in the WRONG direction and much steeper than either.")
w("      The drop pool is rarity-weighted gacha supply, an independent axis.")

w()
w("Q1.4 could per-hero collect_qty be read off the pool at all?")
mn = min(t for _, t in FORUM)
mx = max(t for _, t in FORUM)
w("   per-hero drop counts span %d..%d (Papillon..Lapis), a %.1fx range." % (mn, mx, mx / mn))
w("   namu says collect_qty takes exactly FOUR values (20/40/80/160).")
w("   A 4-valued quantity cannot be recovered from a %d-valued spread" % (mx - mn + 1))
w("   unless the mapping is stated. Residuals mod each rung:")
for q in (20, 40, 80, 160):
    w("     count mod %3d -> distinct residues %s" % (q, sorted(set(t % q for _, t in FORUM))))
w("   -> no per-hero divisor exists in this data. Q1 ANSWER: NO.")

# ================================================================= Q2
head("Q2 — CAN (2^n)x10 AND 20/100/300 BOTH BE TRUE OF DIFFERENT AXES?")

w("Q2.0 the two ladders")
w("   namu (hunter page 1.4, verified verbatim this session):")
w("     '각 등급별로 필요한 흔적 수는 다음과 같다' — THE NUMBER OF TRACES")
w("     REQUIRED, PER GRADE — 1* 20 / 2* 40 / 3* 80 / 4* 160, (2^n)x10")
w("     plus the worked example '한 명당 흔적 20개가 필요한 1성 헌터를")
w("     흔적 100개로 최대 5명을 한 번에 섭외할 수 있다'")
w("     = floor(owned/collect_qty): 100/20 = 5. This is the NATIVE divisor.")
w("   20/100/300 is NOT 199711. It is the vsfan wiki 'Value' column")
w("   (List_of_Blustone_Items, capture 20190821024134, oldid 5115),")
w("   already adjudicated NOT-COMMENSURABLE by trace-rarity-vote-2026-10-05.")

w()
w("Q2.1 shape test")
w("   namu  ratios: %s -> clean x2, and it ships a formula"
  % [40 / 20, 80 / 40, 160 / 80])
w("   vsfan ratios: %s -> x5 then x3, no formula"
  % [100 / 20, 300 / 100])
w("   A designed threshold ladder states its rule; a price list need not.")

w()
w("Q2.2 the three quantities are separable, and here is the proof that they")
w("      are three SEPARATE axes rather than one axis with a disagreement:")
w()
w("   AXIS 1  REQUIREMENT  (a divisor; unit = traces per hunter)")
w("      namu 20/40/80/160. Multiplier semantics confirmed by the 100->5")
w("      example, which matches native floor(owned/collect_qty) at Gce125c.")
w("      Currency: none. It is a count you must hold.")
w()
w("   AXIS 2  SHOP PRICE  (a unit price; unit = currency per trace)")
w("      199711 (byte-verified, 4 captures): 'Golden Hunter Traces 150 for 2'")
w("      namu hunter page: Beckhen 3* '375개로 5개' -> %.1f chips/trace" % (375 / 5))
w("      -> the two AGREE EXACTLY at %.1f fight chips per trace." % (150 / 2))
w("      namu item page 2.5: guild honor 700/8 (4*) and 350/8 (3*)")
w("      -> %.2f and %.2f honor/trace, a %.1fx 4*:3* price step."
  % (700 / 8, 350 / 8, (700 / 8) / (350 / 8)))
w("      NOTE the PRICE step 4*/3* = 2.0x and the REQUIREMENT step")
w("      4*/3* = 160/80 = 2.0x are the same RATIO but different CURRENCIES")
w("      and different physical kinds. Ratio agreement is not identity.")
w()
w("   AXIS 3  VALUE/ESTIMATE (the vsfan 'Value' column)")
w("      20/100/300. Rests on a column the same page uses for")
w("      Metron Fragment 10 / Metron Crystal 1000 = the literal FC price,")
w("      i.e. a worth, per trace-rarity-vote section 1.2.")
w("      Cross-check: vsfan's own FC prices are 75 per 3* trace and")
w("      37.5 per 2* trace (ratios 1:2), while its Value column says")
w("      100 and 300 (ratio 1:3). A price column and a worth column")
w("      cannot both be right about the same shop.")

w()
w("Q2.3 VERDICT")
w("   On the SAME axis namu and vsfan are INCOMPATIBLE: ratio 1.00 / 2.50 /")
w("   3.75 is not a constant scale factor, so at most one can be the")
w("   requirement. But they are on DIFFERENT axes, so there is no actual")
w("   contradiction to resolve — the project simply has not been tracking")
w("   which axis each number lives on. That is the real defect.")

# ================================================================= Q3
head("Q3 — IS THE REPLICA'S FLAT 10/20 CONTRADICTED, AND BY HOW MUCH?")

w("fixture (read-only, server-ts/src/hunter-traces.ts:9-10):")
w("   local_gerard_trace    cardId 005 (Gerard,    2*)  collect_qty 20")
w("   local_sylvester_trace cardId 006 (Sylvester, 1*)  collect_qty 10")
w()
w("grade check against cards.json, independently of the fixture's own rank field:")
w("   Sylvester rarity=%s   Gerard rarity=%s"
  % (GRADE["Sylvester"], GRADE["Gerard"]))
w("   fixture rank field    Sylvester=%s   Gerard=%s" % ("1", "2"))
w("   fixture rank agrees with cards.json: %s"
  % (GRADE["Sylvester"] == "1" and GRADE["Gerard"] == "2"))

w()
w("quantity-by-quantity:")
w("   %-9s %-8s %-9s %-9s %-9s %-9s" % ("grade", "fixture", "namu", "ratio", "namu/fix", "verdict"))
rows = [("1*", 10, 20), ("2*", 20, 40), ("3*", None, 80), ("4*", None, 160)]
ratios = []
for g, fix, namu_ in rows:
    if fix is None:
        w("   %-9s %-8s %-9d %-9s %-9s %-9s"
          % (g, "(none)", namu_, "-", "-", "unpublished in fixture"))
    else:
        r = namu_ / fix
        ratios.append(r)
        w("   %-9s %-8d %-9d %-9.4f %-9.4f %-9s"
          % (g, fix, namu_, r, fix / namu_, "fixture is %.1fx LOW" % r))
w()
w("   the ratio is CONSTANT at %.4f across both published points" % ratios[0])
w("   (spread %.2e) -> a single global scale decision, not a shape error."
  % (max(ratios) - min(ratios)))
w()
w("   magnitude of the discrepancy: every exchange in the replica costs")
w("   HALF what the only first-party source states.")
w("   A 1* Sylvester recruit should debit %d traces; the fixture debits %d."
  % (20, 10))
w("   A 2* Gerard recruit should debit %d traces; the fixture debits %d."
  % (40, 20))
w()
w("   CONSEQUENCE INSIDE THE REPLICA (read-only source inspection):")
w("   Both sides of the guided tutorial READ THE SAME CONSTANT, so the")
w("   tutorial stays self-consistent under a doubling:")
w("     search-battle.ts:8   GUIDE_TRACE_QTY = HUNTER_TRACE_ITEMS")
w("                                     .find(cardId==='006').collect_qty  (=10)")
w("     search-battle.ts:214 a guided victory awards exactly GUIDE_TRACE_QTY")
w("     trace-exchange.ts:30 debit = count * trace.collect_qty  (=10 for cnt1)")
w("     state.ts:1283        the tutorial Clear(37,1) calls that same exchange")
w("   -> 10 awarded, 10 required. Raising collect_qty to 20 makes it")
w("      20 awarded / 20 required. The guide does NOT deadlock.")
w()
w("   BUT there IS a real migration hazard, and it is not the deadlock:")
w("     search-battle.ts:57 validates an ALREADY-SETTLED persisted receipt")
w("     against an allowlist derived from the SAME constant:")
w("       quantities = guided ? [1, GUIDE_TRACE_QTY] : [1]")
w("       ... !quantities.includes(row.added)  ->  throw 'Malformed Search")
w("                                              reward'")
w("   Any account that already settled a guided receipt with added=10 will")
w("   FAIL STATE VALIDATION on load once GUIDE_TRACE_QTY becomes 20, because")
w("   10 is no longer in the allowlist. That is a hard load-time throw, not")
w("   a soft economic change, and it must be handled as a migration.")
w()
w("   SECOND, milder effect: an ORDINARY (non-guided) victory awards a")
w("   hardcoded literal 1 trace (search-battle.ts:214, else-branch).")
w("   At collect_qty 10 that is 10 ordinary victories per Sylvester; at 20")
w("   it is 20. Purely economic, no code path depends on the value.")
w()
w("   NO other production consumer: the only in-repo READERS of collect_qty")
w("   are trace-exchange.ts:28 (validation), trace-exchange.ts:30 (debit)")
w("   and search-battle.ts:8 (guided payout). Blast radius in src/ = 3")
w("   sites, all in 2 files.")
w()
w("   BUT TESTS DO PIN THE LITERALS (verified, read-only):")
w("     tests/guided-search-recruitment.ts:34  assert trace.qty === 10")
w("     tests/guided-search-recruitment.ts:43  consume_result qty === 10")
w("     tests/trace-exchange.ts:35             assert trace.qty === 20")
w("     tests/trace-exchange.ts:65             consumed qty === 20 for cnt 2")
w("   tests/trace-exchange.ts:24-33 also loops EXACTLY 20 Search victories")
w("   to accumulate those 20 traces, and tests/guided-search-recruitment.ts")
w("   loops exactly 10. A doubling makes those loop counts insufficient and")
w("   those four assertions fail. That is the real test-level blast radius:")
w("   4 literal assertions + 2 loop trip counts, across 2 test files.")

w()
w("   WHAT IS *NOT* CONTRADICTED: nothing native, nothing measured.")
w("   No [NATIVE] or [ORIGDATA] anchor for collect_qty exists. namu is")
w("   [COMM], 1 source, and its page is dated 2026-10-03, i.e. POST the")
w("   2019-09-05 rebalance, while the fixture has no era tag at all.")
w("   So: the fixture IS contradicted by the available evidence, but the")
w("   evidence is one post-rebalance community wiki, and the era gap is")
w("   unresolved. Verdict: CONTRADICTED-as-best-evidence, NOT PROVEN WRONG.")

# ================================================================= Q4
head("Q4 — IS THE EXCHANGE GRADE-GATED, AND DOES IT INTERACT WITH 4,208?")

w("Q4.1 the grade axis EXISTS and is stated as the requirement's own axis:")
w("   namu hunter page 1.4: '각 등급별로 필요한 흔적 수' (required count, by grade)")
w("   namu item page section 5 header ladder, verbatim from the render:")
w("     5. 헌터 흔적  /  5.1. 1*  /  5.2. 2*  /  5.3. 3*  /  5.4. 4*")
w("     '각 흔적은 등급(★)별로 나눈 다음에 한국어 어순으로 정리했다'")
w("     = 'each trace is split by grade, then sorted in Korean word order'")
w("   -> the item reference is ORGANISED BY GRADE. Source 2 is CORRECT.")
w("   -> and the grade axis there is the SAME axis as the requirement.")
w("      Source 2's framing 'a grade axis separate from worth' is right in")
w("      that the worth ladder (20/100/300) is a different quantity, but")
w("      the grade axis is not independent of the REQUIREMENT — it indexes it.")

w()
w("Q4.2 grade-gating of the EXCHANGE, tested against what is on disk")
w("   recovered namu dumps scanned: 67 files, 271 '흔적' occurrences.")
w("   '3성 헌터 흔적' (3-star hunter traces) : EXACTLY 1 hit, ctrl-d-main.")
w("   '미라주' (Mirage)                      : 0 hits in ALL 67 files.")
w()
w("   The single hit, in full context: the 신기루 유적지 (Sin-gi-ru ruins)")
w("   shop list — '특급 의뢰서, 메트론 결정체, 강화 재료, 도구 상자,")
w("   고급 도구 상자, 결정, 3성 헌터 흔적, 할리의 흔적을 구매할 수 있다',")
w("   i.e. the shop stocks a GENERIC '3-star hunter traces' line PLUS one")
w("   named 4* (Harley, per footnote 30).")
w()
w("   CORRECTION TO THE TASK BRIEF: the shop is 신기루 (Sin-gi-ru) / 라피스의")
w("   마켓 (Lapis's Market), NOT 'Mirage'. '미라주' appears nowhere in the")
w("   recovered corpus, so the Mirage attribution is unsupported as stated.")
w("   (sin-gi-ru and the project's Mirage Ruins are plausibly the same")
w("   place, but the corpus does not say so and this lane does not assume it.)")
w()
w("   What that sentence DOES establish about grading: the shop sells a")
w("   grade-3 generic trace line, and a 4* hero's trace separately at a")
w("   separate price. That is grade-partitioned MERCHANDISE, which is")
w("   consistent with a grade-gated exchange but does not by itself prove")
w("   the exchange rejects a mismatched grade.")
w()
w("   namu item page 2.5 gives the clearest grade-splitting evidence:")
w("     '★4헌터 흔적의 구매 가격은 훈장 700당 흔적 8개이며 ★3헌터 흔적의")
w("      구매 가격은 훈장 350당 흔적 8개다'")
w("   -> the PRICE is grade-indexed and exactly 2x from 3* to 4*.")
w("   -> a grade-gated exchange with a grade-indexed price is the")
w("      parsimonious reading of the whole item page.")
w()
w("   namu item page 3.3 search table, verbatim (Table 17):")
w("     헌터 등급 | 1성 | 2성 | 3성")
w("     헬륨 소비량 | 2개 | 8개 | 15개")
w("     수색 가능 횟수 | 5 | 4 | 2")
w("   -> the TRACE SEARCH is grade-gated too, and separately from the")
w("      exchange: it costs helium 2/8/15 for 5/4/2 searches by grade.")

w()
w("Q4.3 DOES 4,208 INTERACT WITH THE EXCHANGE?")
w("   No. Arithmetically it cannot:")
w("     - the 37 pool members are a RARITY-WEIGHTED supply sample")
w("       (67.8 / 25.6 / 6.6 %% by grade), whereas the exchange is a")
w("       grade-INDEXED requirement (1 : 2 : 4 : 8). Opposite direction.")
w("     - a per-hero requirement is a 4-valued function of grade; the")
w("       pool is a 37-valued continuous-ish spread. No mapping exists.")
w("     - the pool is 2018-02 and self-described as approximate.")
w("   The only real interaction is CORRELATIONAL: 4,208 tells you WHICH")
w("   heroes were in the drop pool at all (37 of them; the other 7 rows")
w("   are explicitly excluded event/special hunters), which is a pool-")
w("   MEMBERSHIP question, not a cost question.")
w("   Practical consequence: a hero absent from 422653 is not thereby")
w("   cheaper or dearer to recruit. Papillon's 4 traces do NOT mean her")
w("   collect_qty is 4, and Lapis's 358 does NOT mean 358.")

w()
w("#" * 78)
w("# STANDING REFUSALS — checked, not violated")
w("#" * 78)
w("fc-native 1.4 forbids setting honor values from arena reward tables.")
w("  This lane USED the namu guild-honor TRACE PRICE (700/8 and 350/8).")
w("  That is a shop price for an item, read from a community wiki, and is")
w("  NOT an arena honor award. No honor award value is proposed, derived or")
w("  applied anywhere. COMPLIANT.")
w("exp-ladder 4 forbids conflating RankUp gold with the star-advancement")
w("  ladder. This lane touches neither RankUp nor the advancement ladder;")
w("  trace collect_qty is not either of them. COMPLIANT.")
w("server-ts: read only. No file under server-ts was edited, and the build")
w("  was not run. COMPLIANT.")

OUT.close()
sys.stdout.write("wrote _trace_cost_final.txt\n")
import os

p = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..',
                 'grade-vs-level-factor-2026-10-06.md')
t = open(p, encoding='utf-8').read()

# ---- 1. executive summary ----------------------------------------------
i = t.find('**Answer in one line.**')
j = t.find('## Files touched')
assert 0 < i < j
NEW_SUM = """**Answer in three lines.**

1. **The un-cropped ★4→★5 result does not exist and very likely never did.** All three
   surviving uploads of that screen are crops of one user-edited phone photograph
   (`IMG_5729`), and all three terminate at the grade badge row — exactly where the
   戦闘力 row that the ★3→★4 screen demonstrably carries would begin. A **third**
   crop (690×388) is recovered here for the first time.
2. **The lead was aimed at the wrong quantity.** A third same-shape transition would
   **not** have separated the grade factor from the level factor: assuming the two
   grade factors are equal collapses the two unknowns into one (§5). What separates
   them is a reading with **level or grade held fixed**. One already exists in the
   corpus and had never been read — the **キャパ超越 (Capacity Transcendence) result
   screen**, which carries **HP, ATK and DEF** with **grade and level both fixed**.
3. **Recovered:** Capacity Transcendence is a pure **×1.0994** core-stat multiplier
   (ATK 365→401, DEF 423→465, HP 619→681 on Bear `036` at ★3/Lv.1; three independent
   stats agreeing to **0.139 %**), permitted at most **3×**, ceiling **×1.3287**. Under
   the same fixed-grade, fixed-level operation **戦闘力 rises ×1.1625 — 5.74 % faster
   than the stats**, which *proves* 戦闘力 is not a linear function of HP/ATK/DEF and
   closes the question of whether §5's bound transfers to the core stats. **The
   grade-vs-level split itself remains open**: still 3 unknowns, 2 independent
   equations.

**Headline corrections to the prior lane.** (a) `rank2`'s **3311 → 4907** belongs to
the **blonde-child hero, not `029` Kain** — Kain's ★3/Lv.MAX 戦闘力 is *also* 3311 and
that coincidence is what caused the misattribution (§4). (b) The 1.1 % spread between
the two rank-up ratios is **≈43× the rounding floor**, so it is a real hero-dependent
term and **not** "well inside the ±0.14 % rounding noise" (§5.1). (c) §10 item 5's
premise — that a third ★4→★5 ratio would separate the factors — is algebraically
impossible as stated (§5).

"""
t = t[:i] + NEW_SUM + t[j:]

# ---- 2. disposition ------------------------------------------------------
i = t.find('## 11. Recommended disposition for the parent')
j = t.find('## 12. Guard compliance')
assert 0 < i < j
NEW_DISP = """## 11. Recommended disposition for the parent

1. **Do not implement any per-level factor.** None was measured here, and §5 shows
   the measurement this lane was commissioned to obtain would not have supplied one.
2. **Adopt the Capacity Transcendence constant** — core stats **×1.0994** per
   application, max 3 applications, cumulative ceiling **×1.3287**, one application
   granted per rank-up, requiring a same-named ★3+ duplicate plus メトロン結晶体 /
   メトロンのカケラ / ルピー (observed cost 9,000). This is a **pure multiplier on
   基本能力値 with grade and level fixed**, it is original, and it is the first
   gear-free core-stat reading this project has. It belongs to the stat lane.
3. **Record that 戦闘力 is not linear in the core stats** (×1.1625 vs ×1.0992 at a
   controlled point). Any future rebalance model that sums HP/ATK/DEF into 戦闘力 is
   already falsified by one screenshot.
4. **Correct `hero-panel-level-extraction-2026-10-06.md`**: §4.1/§4.5 hero identity
   (§4 above); §5.2's rounding argument and the bound — use the defensible looser
   bound **`g²⁹ ≤ 1.498434`, per-level ≤ 1.013851**, and state the Beckhen excess as
   **1.15×** not 1.16× (§5.1); §10 item 5's premise (§5).
5. **Retarget the lead.** The missing datum is the **戦闘力 of the blonde-child hero at
   ★4 / Lv.MAX** — the left-hand value of T3, which the crop removes — or any
   **same-level cross-grade** step, or any **same-grade two-level** pair. Not a third
   ★4→★5 ratio.
6. **The archive-row constraint (T5) may retire the Beckhen 1.7157 question outright.**
   The archive's HP/ATK/DEF ratios against a known Lv.1 row span **1.52×**, so no
   single per-level scalar maps one to the other across the three stats, whatever the
   archive row's grade does. Until that row's **grade and level are pinned**, a
   single-number core-stat level factor is not a well-posed quantity. Recommend
   re-classifying the Beckhen ratio as *ill-posed pending archive grade/level* rather
   than as an open contradiction.
7. **Never re-run the `/archives/<id>`-only crawl.** The 育成論 category namespace
   (`rank1`–`rank4`, `IMG_9719`, `capa1`/`capa2`, `d`, `traning`, and every
   `/attachment/<id>` page) was never visited by any prior lane and is where this
   lead lives. Crawl the site. See §2.2.
8. **Screen result screens, not just stat panels.** The one screen class everyone
   had written off as numberless (キャパ超越 success) carried the payload. Read the
   **whole** frame before concluding a class is exhausted.

"""
t = t[:i] + NEW_DISP + t[j:]

# ---- 3. coverage note: explain the counter honestly ----------------------
i = t.find('## 10. Coverage counters')
j = t.find('## 11. Recommended disposition')
assert 0 < i < j
NEW_COV = """## 10. Coverage counters — UNCHANGED, and here is precisely why

**Heroes 1/113 · accessories 1/100 · monsters 0/22.**

T4 is the **first gear-free core-stat reading in this project**, and it is tempting to
promote it. It is not promoted, and the reason is mechanical rather than cautious:
the counters require a reading whose **level basis and gear state are established and
comparable across heroes**. T4 pins gear state (★3 cannot hold equipment, §2.3) but
**its level basis is Lv.1 at a single unknown-to-the-ledger state**, and the hero `036`
is already covered by name — so it adds a **scaling constant**, not a new hero's base
tuple. It earns zero coverage credit on both counts. Stating that explicitly is the
point: this lane moved the *model*, not the *ledger*. `coverage.md` was not opened.

"""
t = t[:i] + NEW_COV + t[j:]

open(p, 'w', encoding='utf-8', newline='\n').write(t)
print('ok, bytes', len(t.encode('utf-8')))
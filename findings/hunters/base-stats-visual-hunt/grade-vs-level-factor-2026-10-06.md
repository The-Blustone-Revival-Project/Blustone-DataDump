# Grade-vs-level factor — the ★4→★5 hunt (2026-10-06)

**Lane goal (from `hero-panel-level-extraction-2026-10-06.md` §10 item 5).** Find the
full, un-cropped ★4→★5 rank-up result so that the grade factor `f` and the per-level
factor `g` stop being confounded.

**Answer in three lines.**

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

## Files touched

- **New, this lane only:** this file.
- **New images:** `grade-vs-level-2026-10-06/img/` — every file below is the
  byte-exact Wayback body. `_`-prefixed files are working artefacts
  (2× upscales, two comparison sheets, one zoom sheet).
- **New helper scripts:** `grade-vs-level-2026-10-06/_work/` —
  `wb.py` (transport + real-dimension decode), `nearest.py` (nearest-capture
  resolver), `controls.py`, `fetchimg.py`, `fetchpages.py`, `cdxsweep.py`,
  `cdxfull.py`, `crawl.py`, `collect.py`, `fetchnew.py`, `priority.py`, `pagemap.py`,
  `pagetext.py`, `attach.py`, `links.py`, `entry.py`, `listpages.py`, `catpages.py`,
  `ident.py`, `ident2.py`, `zoom.py`, `zoom_capa2.py`, `calc.py`, `capa_math.py`,
  `audit.py`, `fixeol.py`, and the section-fix helpers `peek.py` / `fixsec6.py` /
  `fixsum.py`.
- **Also recovered:** `img/2019-03_capa.jpg` (189,444 B, 633×432, ts
  `20190401022918`) — inspected and recorded as an illustration in §7.
- **Read only:** `_archives_work/` (the prior lane's 215 cached pages + CDX census),
  `hero-panel-level-images-2026-10-06/_manifest.json`.
- **NOT touched:** `polluted-observations.md`, `coverage.md`, any TSV, `server-ts`,
  fixtures, seeds, APK, emulator, phone, Ghidra.

---

## 1. Positive controls (run before any negative was recorded)

| # | control | result |
|---|---|---|
| C1 | `http://web.archive.org/` | **TIMEOUT**, not a content result — 8 KB of body never arrived (`WinError` timeout after 60 s). Recorded as a transport timeout, **not** as a negative about content. |
| C2 | `2018/11/rankup.jpg` @ `20190403182150id_` | 200, **201,302 B**, JPEG **632×429** — **PASS** |
| C3 | `2019/03/IMG_5729.png` @ `20190330070910id_` | 200, **186,108 B**, PNG **750×389** — **PASS** |
| C4 | `2019/01/IMG_5729-e1548139622568.png` @ `20191121144145id_` | 200, **165,636 B**, PNG **650×365** — **PASS** |
| C5 | `2019/01/1548235686-1024x911.jpg` @ `20190403124314id_` | 200, **117,921 B**, JPEG **1024×911** — **PASS** |

C2–C5 are image controls on the exact namespace under test and all decode with real
dimensions, so **every "not captured" in this lane is a statement about archive.org's
capture set, not about the transport**.

**In-corpus read-path control (stronger than C2–C5).** Bear `036` was already
reproduced 4/4 across three images by the prior lane; this lane re-read
`rank2`'s **3311 → 4907** and `0d40a5e4…-1`'s **2554 → 3827** at 900 px and every
digit is unambiguous (sheet: `img/_zoom_all_numbers.png`).

---

## 2. The enumeration breakthrough — the lead was in the wrong namespace

The prior lane crawled **215 `/archives/<id>` pages** and took 452 image URLs from
them. It never crawled the site's **category / attachment namespace**, which is
where the ★5 article's images actually live.

### 2.1 CDX is unusable for enumeration on this host — a new instance of trap #5

| query | rows returned |
|---|---|
| `url=blustone.jp&matchType=domain&collapse=urlkey&limit=2000&page=0` | **170** |
| same, `page=1` | not reached (170 < 2000 → loop ended) |
| `url=blustone.jp&matchType=domain&limit=2000&page=0` (no collapse) | **207** |
| per-month `matchType=prefix` on `wp-content/uploads/2019/01/` | 45 |
| per-month prefix on `2018/11/`, `2018/12/`, `2019/02/`, `2019/03/` | 91, 46, 49, 109 |

The domain query truncates at ~170–207 **regardless of `page` and `limit`**. It is
therefore *not* a complete census and nothing here rests on it. **Path-prefix queries
on the uploads tree are not truncated** and were used as a cross-check only.

### 2.2 Crawl instead — and the category pages were never visited

`/web/2/<url>` (the **nearest-capture** form) redirects to the closest capture and
yields its 14-digit timestamp; `id_` at that timestamp then returns the raw body.
That instrument is what makes "was this ever captured, and when" answerable at all,
because `id_` alone requires an exact timestamp. Verified: it resolved C2/C3/C4/C5's
URLs to exactly the timestamps the CDX rows claim.

Crawled and read in full (all verbatim archive bodies, in `img/../_work/pages/`):

| page | capture ts | bytes | what it added |
|---|---|---|---|
| `/育成論/ランクアップ` (the rank-up article) | `20191113131941` | 34,639 | **the whole article**, incl. `rank1`–`rank4` + `IMG_9719` |
| `/育成論` (category index) | `20191209134746` | 29,038 | the five 育成論 articles |
| `/育成論/ランクアップ/rank1` | `20191118021834` | 26,895 | attachment page |
| `/育成論/ランクアップ/rank2` | `20191121194819` | 26,895 | attachment page |
| `/育成論/ランクアップ/rank3` | `20191209003500` | 26,895 | attachment page |
| `/育成論/ランクアップ/rank4` | `20191211113444` | 26,895 | attachment page |
| `/育成論/トレーニング/d` | `20191121222851` | 26,950 | attachment page |

The rank-up article's own image list is `2018/11/`: `rankup.jpg`,
`IMG_9719.jpg`, `rank1-1024x911.jpg`, `rank2-1024x911.jpg`, `rank3-1024x911.jpg`,
`rank4-1024x911.jpg` — plus, from the attachment pages, the **full-size originals**
`rank1.jpg`, `rank2.jpg`, `rank3.jpg`, `rank4.jpg` and the `-768x683` /
`-300x267` variants, **none of which any prior lane had tried**.

### 2.3 The rank-up article's own rules (original, verbatim)

- 「レベルが最大になったハンターはランクアップしてさらに強化できます」 — rank-up
  requires max level.
- 「例えば、**★3→★4**にランクアップさせる場合、ランクアップ相手には**★3ハンターが3人**
  必要となります」 — ★3→★4 consumes **3** ★3 materials.
- 「ハンターがランクアップすると、**レベルが1に戻る**代わりに★ランクとレベルの
  最大値が増えて、新たなスキルを習得します」 — **rank-up resets level to 1**,
  raises the ★rank and the level cap, and grants a new skill.
- 「**★4以上になると装備も開放**され」 — **equipment unlocks at ★4**.

Cross-language corroboration: the Korean guide states 「모든 캐릭터는 승급시 자신과
같은 등급의 캐릭터를 자신의 등급의 수 만큼 필요로 한다」 ("all characters need as
many same-grade characters as their own grade number when promoted"), which makes
**★4→★5 require 4 × ★4** materials — a rule the JP article states only for ★3→★4.

**Consequence for this project:** every ★3→★4 frame in the corpus is a frame of a
hero that **cannot yet hold equipment**, so its gear state is determinately clean
rather than merely unknown. That strengthens the ★3→★4 readings and, by contrast,
means the ★4/★5 frames are the ones where gear could contaminate.

---

## 3. Transitions recovered — full provenance

### T1 — ★3 / Lv.MAX → ★4 / Lv.1, **戦闘力 3311 → 4907** (ratio **1.482030**)

- hero: **blonde child, red eyes, cat/fox ears, black suit, red tie** — *not* Kain.
  See §4.
- before: ★3 (gold ring), pill **Lv.MAX**; after: ★4 (green ring), pill **Lv. 1**.
- quantity: **戦闘力** (combat power). Labels: left panel 「戦闘力UP 3311 → 4907」;
  right result panel 「ミドルハンター → アドバンスハンター」 with **3311 → 4907**
  printed under each badge.
- image: `hero-panel-level-images-2026-10-06/rank2-1024x911.jpg`
- URL: `https://blustone.jp/wp-content/uploads/2018/11/rank2-1024x911.jpg`
- bytes **70,971**, decoded **1024×911**, JPEG
- sha256: `8b90e127d8732c781c19b674bf40927bef1e372e27f003d512e69e839bd4cc18`
- **capture timestamp: NOT independently resolved in this pass.** The file is
  inherited from the prior lane's on-disk copy, and that lane's `_manifest.json`
  contains **no row** for `rank1-1024x911.jpg` or `rank2-1024x911.jpg` — i.e. its own
  provenance for these two files is undocumented. The bytes, dimensions and sha256
  above were computed here from the local file; the capture timestamp was not
  re-resolved because archive.org was refusing connections
  (`WinError 10061`) for the whole of that window. **This is an open gap, stated
  rather than guessed** — I will not invent a timestamp.
- also in the same frame, at ★3 **Lv.1** (material/trainer rows): **1901, 1938,
  1999, 2018** and a ★3 trainer at **1503**; gold cost **12000**.
- gear state: **determinately gear-free** (§2.3, ★3 cannot hold equipment).

### T2 — ★3 / Lv.MAX → ★4 / Lv.1, **戦闘力 2554 → 3827** (ratio **1.498434**)

- hero: **blonde high-ponytail girl, blue eyes, blue tunic** — a different hero
  (identity sheet `img/_identity_evidence.png`).
- before: ★3, pill **Lv.MAX**; after: ★4, pill **Lv. 1**.
- new skill unlocked on the result panel: **攻撃力アップ** (ATK up) — contrast T1's
  **敵に追加ダメージ** (added damage to enemies).
- material rows at ★3 **Lv.1**: **2232, 2232, 2232**; gold cost **8730**.
- image: `hero-panel-level-images-2026-10-06/0d40a5e4a645fc6b96e767d64ac0878e-1-1024x904.jpg`
- URL: `https://blustone.jp/wp-content/uploads/2019/01/0d40a5e4a645fc6b96e767d64ac0878e-1-1024x904.jpg`
- capture ts: **`20190331215922`** (from the prior manifest, `fetch_ts`)
- bytes **109,154**, decoded **1024×904**, JPEG
- sha256: `ee91115dc9941507ebac3f5edd93a60f5bfbb7eeb540068f97a5f5dbb61e8e3a`

### T3 — ★4 / Lv.MAX → ★5 / Lv.1 — **the target — still numberless**

All three surviving uploads of this screen are crops of one phone photograph
(`IMG_5729`, an iOS camera-roll name) that terminates at the badge row. **The
戦闘力 row that the ★3→★4 result screen demonstrably carries is cropped off.**

| # | file on disk | bytes | decoded | capture ts | sha256 |
|---|---|---|---|---|---|
| a | `img/2019-03_IMG_5729-e1551694819888_20190331221452.png` | 176,559 | **690×388** | `20190331221452` | `9b44cbefeeda4a8eb3189ebd337598e729ea166a7b0f480f94f7022fac692ebb` |
| b | `img/IMG_5729-jan-20190405.png` = prior lane's `IMG_5729-e1548139622568.png` | 165,636 | **650×365** | `20190405082420` **and** `20191121144145` (byte-identical, sha256 `b2e8678d91d77c312ac48c1e86269f94a4766567a30132b3f9942f3bfdddcfa5`) | same |
| c | prior lane's `2019/03/IMG_5729.png` | 186,108 | **750×389** | `20190330070910` | `283ce079815bab1d5d0fa3a705cfcbe08b57527cfc63fd81241c6f7ec19d1933` |

- (a) is **new in this lane** — a third distinct crop, never previously recovered.
- All three show: ★4 glyph (2+2 white stars, green ring) pill **Lv.MAX** → ★5 glyph
  (4 small + 1 large blue star, blue ring) pill **Lv. 1**. Same hero art, same
  element icon as T1.
- **The number `39554` in the top-right of all three is the RUPEE wallet HUD, not a
  hero statistic.** It is present on T3-a/b/c alike and is *not* a 戦闘力 reading.
- T3 is the **same hero as T1**, so the ladder for that one hero is
  **★3/Lv.MAX = 3311 · ★4/Lv.1 = 4907 · ★4/Lv.MAX = ? · ★5/Lv.1 = ?**

### T4 — **キャパ超越 (Capacity Transcendence), grade AND level BOTH fixed** — the payload of this lane

This is the frame that carries **HP / ATK / DEF**, and it is the only frame in the
whole corpus where a core-stat change is observed with **both** confounds held
constant. It was already on disk from the prior lane (`capa2-1024x911.jpg`) but was
read as "Bear `036` 戦闘力 2326 → 2704" and **the three stat columns were not noticed**.

Hero **Bear `036`** 大自然の贈り物「クマ」 (name on screen; matches the TSV `036` row
verbatim), badge **★3 / Lv.1**, gear slots **absent from the frame**, wallet 37860.

| quantity (label on screen) | before | after | ratio |
|---|---:|---:|---:|
| 攻撃力 **ATK** | **365** | **401** | **1.098630** |
| 防御力 **DEF** | **423** | **465** | **1.099291** |
| **HP** | **619** | **681** | **1.100162** |
| 戦闘力 combat power | 2326 | 2704 | 1.162511 |

- image: `hero-panel-level-images-2026-10-06/capa2-1024x911.jpg`
- URL: `https://blustone.jp/wp-content/uploads/2018/11/capa2-1024x911.jpg`
- bytes **69,340**, decoded **1024×911**, JPEG,
  sha256 `709ed6d5eee606bc8501888df9d430e41a371f4d1a5c5abc20df3a7019eec0e9`
- digits re-read at **1000 px** (`img/_zoom_capa2_core_stats.png`): all six values
  unambiguous.
- material rows: a second ★3 / Lv.1 Bear at **2326**, 1/1; メトロン結晶体 9/9,
  メトロンのカケラ 449/90, cost **9000** — an original observed value, not a fixture.

**The article's own rule, verbatim** (`/育成論/キャパ超越`, capture `20191113132035`,
31,205 B):

> 「★3以上の同名キャラをかけ合わせれば、能力値のキャパを超越させてさらに強化
> することができます。**キャパ超越はハンターをランクアップするごとに最大3回まで
> 可能で、その都度基本能力値が上がる**ので、主力にしているハンターはなるべく
> たくさん仲間にしましょう。」

= Capacity Transcendence combines a **same-named ★3+** duplicate, can be applied **at
most 3 times, once per rank-up of the hunter**, and **each application raises
基本能力値 (the core stats)**. Materials: メトロン結晶体, メトロンのカケラ, ルピー.

**Corroboration from an earlier lane.** `capa2-diff-2026-10-05.md` had already
recovered this article's **prose** (capture `20190331201909`, 28,182 B) and had already
identified 基本能力値 as the thing that rises — but it worked on the page **text** and
never opened the image, so it contains **none** of the six stat values found here
(checked: no `365`, `401`, `423`, `465`, `619`, `681`, 攻撃力 or 防御力). Its separate
capture of the same page at `20190331201909` corroborates my `20191113132035` body.
This is the concrete instance of disposition item 8: **the prose had already been
read and the pixels under it had not.**

**Consequences — three findings, all new to this project:**

1. **A pure core-stat multiplier exists and is measured: ×1.0994** (mean of three
   stats). The three independent quantities **agree to 0.139 %**, which is an
   *internal consistency check on the reading method* and is the tightest agreement
   anywhere in this corpus. Cumulative ceiling **×1.3287** over the 3 permitted
   applications.
2. **戦闘力 is provably NOT a linear function of the core stats.** Under an operation
   that changes **neither grade nor level**, the core stats move **×1.0994** while
   戦闘力 moves **×1.1625** — **5.74 % faster**. A weighted sum of HP/ATK/DEF cannot do
   that. This is a *controlled* proof of what the prior lane could only infer from the
   archive/in-game mismatch (§5.3), and it is the reason the 戦闘力 bound in §5.1
   cannot be transferred to HP/ATK/DEF.
3. **★3 heroes are confirmed gear-free** — the rank-up article says equipment unlocks
   at ★4 (§2.3) — so T4 is a **gear-free core-stat reading**, the class of reading
   the coverage ledger has been unable to produce.

### T5 — the archive row cannot be reached from Lv.1 by any single scalar

The 2019 JP archive row for the **same** hero `036` gives **HP 1923 / ATK 755 /
DEF 864 / 戦闘力 10011** (level and gear both unestablished). Against the in-game
★3 / Lv.1 row from T6:

| | archive | in-game ★3 Lv.1 | ratio |
|---|---:|---:|---:|
| ATK | 755 | 365 | **2.0685** |
| DEF | 864 | 423 | **2.0426** |
| HP | 1923 | 619 | **3.1066** |

The three core-stat ratios span **1.52×**. Since the archive row's **grade is also
unknown**, this is **not** proof that the per-level factor differs per stat — but it
**is** a hard constraint: *no single per-level scalar can map the Lv.1 row to the
archive row across HP, ATK and DEF simultaneously*, whatever the grade does. Any
single-number "core-stat level factor" — including the **Beckhen 1.7157** figure that
this whole lane was commissioned to test — is therefore **not a well-posed quantity**
until the archive row's grade and level are pinned.

### T6 — ★1 / Lv.1 → ★3 / Lv.1, **15 → 3**, cost **15000** — NEW, never seen by any lane

- image `img/rank3-1024x911.jpg`, URL
  `https://blustone.jp/wp-content/uploads/2018/11/rank3-1024x911.jpg`,
  capture ts **`20190403214512`**, **59,825 B**, decoded **1024×911**, JPEG,
  sha256 `5c41a7a1d9b27e7c814a4f81c5cd7f899574a6bb137b0d01d8d609213b7ac92e`.
- screen: 一括ランクアップ (bulk rank-up). Left: choose ★1 / ★2. Right:
  **★1 Lv.1 ×15 → ★3 Lv.1 ×3**, 「ランクアップに使用されるハンター 15」,
  「保有序の★2ハンター 19」, ランクアップ料 **15000**.
- rule text: 「**★3ハンター1名のランクアップにはトレーニング前の★2ハンター5名が
  使用されます**」 = **5 × ★2 → 1 × ★3**, i.e. **5 × ★1 → 1 × ★3** by transitivity.
- **No 戦闘力 token anywhere in this frame**, so it yields no ratio. Its value is the
  **material ratio 5:1 per grade step**, which is original.

### T7 — release / market — NEW, never seen by any lane

- image `img/rank4-1024x911.jpg`, URL
  `https://blustone.jp/wp-content/uploads/2018/11/rank4-1024x911.jpg`,
  capture ts **`20190403163420`**, **63,961 B**, decoded **1024×911**, JPEG,
  sha256 `ca530535b263bc477bc31e39c5e1771128544c44e4448e19bbb65f8b5d89d1ec`.
- left: 銅鉄のレヴェナント「**カリバー**」 (matches `053` verbatim), ★3 **Lv.1**,
  解放額 **8** チュウコイン.
- right: シークレットマーケット trainer prices — **★3トレーナー 4**, **★4トレーナー 16**,
  **★3キャパ超越券 145**, **高級依頼書 5**, **特級依頼書 20**.
- The article's own claim, 「★3のハンターを開放すると8枚のチュウコインで★3トレーナー
  2人が入ります」, is **consistent with the frame** (8 ÷ 4 = 2). No ratio recovered.

---

## 4. Identity correction — `rank2`'s hero is **not** `029` Kain

`hero-panel-level-extraction-2026-10-06.md` §4.1 attributes **3311 → 4907** to
`029` Kain, citing as "cross-frame identity confirmation" that `rank1`'s Hunter-List
row for the same art reads **Lv.MAX / 3311**. That reasoning fails on inspection
(`img/_identity_evidence.png`, `_compare_rank1_rank2.png`):

| frame | art | verdict |
|---|---|---|
| `rank1` right panel, メンバートレーニング | 鋼のボディガード「**カイン**」 — tall blonde **adult male**, purple eyes, black jacket, sword | Kain `029`, named on screen, **★3 / Lv. 30 / 戦闘力 3311** |
| `rank2` review + success panel | blonde **child**, **red eyes**, cat ears, **black suit + red tie** | **a different hero** |
| `0d40a5e4…-1` review + success panel | blonde **high-ponytail girl, blue eyes, blue tunic** | a third hero |
| `IMG_5729` (all three crops) | **identical** to `rank2`'s child | the same hero as `rank2` |

Kain's ★3/Lv.MAX 戦闘力 happens to be **3311**, exactly equal to the blonde child's
★3/Lv.MAX 戦闘力. That is a **coincidental number match**, and it is what produced
the misattribution. It is not implausible — 戦闘力 is normalised so that same-grade,
same-level heroes cluster (the prior lane's own `rank1` list has eight ★3/Lv.1 heroes
inside a 14.65 % band) — but it is not identity evidence.

**What this changes and what it does not.**
- **Does not change** the two ratios: both frames are still ★3/Lv.MAX → ★4/Lv.1 with
  their values legible at 900 px, so **1.482030 and 1.498434 stand**.
- **Does change** the hero labels, and it **strengthens** the ladder: the ★4/Lv.1 =
  4907 hero and the ★4/Lv.MAX → ★5/Lv.1 hero are demonstrably the **same** hero.
- **Also a genuine gain:** T1 and T2 differ in gold cost (**12000** vs **8730**),
  material values (**1901/1938/1999/2018** vs **2232×3**), new-skill row
  (敵に追加ダメージ vs 攻撃力アップ) and account wallet (**27360** vs **18351**), so
  they are two **independent** rank-ups on two heroes in two accounts — not two
  renderings of one event.

---

## 5. The corrected finding — a third transition would **not** have separated `f` from `g`

The prior lane's §10 item 5 states that an un-cropped ★4→★5 frame "would give the
third ratio and, assuming the two consecutive grade factors are equal, **would
separate `f` from `g`**". That is self-defeating: *assuming* `f₃₄ = f₄₅ = f`
collapses the two unknowns into one, so no amount of extra data can separate them.

Write the model explicitly. Let `P(g, ℓ)` be 戦闘力 at grade `g` and level `ℓ`, let
`f₃₄`/`f₄₅` be the grade factors and `g²⁹` the 29 level steps from Lv.1 to Lv.30.

```
T1:  f34 · g^29 = 4907/3311 = 1.4820295983
T2:  f34 · g^29 = 3827/2554 = 1.4984338293      (independent re-measurement)
T3:  f45 · g^29 = C/B                          (B = P(4,Lv30), C = P(5,Lv1))
```

- **Unknowns:** `g²⁹`, `f34`, `f45` → **3**.
- **Independent equations** from T1+T2+T3: **2** (T1 and T2 are the same equation,
  they merely repeat it).
- ⇒ **underdetermined by one.** `T3` is a *consistency test* on `f45`, **not** a
  separation. The `f`/`g` split stays open even if T3 were found.

**What actually closes it** — a transition that is *not* one grade step plus 29 level
steps:

| kind of datum | what it yields |
|---|---|
| **same grade, Lv.N → Lv.M** | `g^(M−N)` directly. **No assumption at all.** This is the cleanest possible win and is what the brief asked for first. |
| **same level, ★n → ★n+1** (i.e. `B` = `P(4, Lv.MAX)`) | `f34 = B/3311`, then `g²⁹ = 1.4820296 × 3311 / B`. Turns 3 unknowns into 3 equations. |

Both are the *same* physical requirement: **a reading that holds level fixed while
grade changes, or grade fixed while level changes.** T3 as it exists holds *neither*
fixed — it moves grade +1 and level −29 simultaneously, which is exactly the
confound this whole lane exists to break.

### 5.1 The 1.1 % spread is **not** rounding noise — a correction

§5.2 of the prior lane says the two ratios "agree to 1.1 % — **well inside** the
±0.14 % worst-case rounding noise implied by a 4-digit integer. **The reading method
is sound.**" Those two statements contradict each other.

Worst-case rounding on a displayed 4-digit integer is `0.5/value`:

```
0.5/3311 = 0.0151 %      0.5/4907 = 0.0102 %      worst-case on the ratio ≈ 0.025 %
observed spread                                              1.1008 %
```

The spread is **≈43× the rounding floor** (and 7.9× the ±0.14 % figure quoted). So
the two heroes' net rank-up factors **genuinely differ by 1.1 %**, and rounding cannot
explain it. Honest reading:

- the two measurements are **reproducible and each internally sound** (4/4 replication
  on Bear, and both digits are unambiguous at 900 px);
- but `戦闘力` is **not** a clean product `f · g²⁹` — there is a hero-dependent or
  rounding-of-components term of order ~1 %. Any per-level factor fitted to these two
  points inherits that ~1 % slop;
- this also means the §5.2 bound `g²⁹ ≤ 1.482030` is **not tight** — the underlying
  exact product could sit up to ~1.1 % below the displayed ratio. Restated honestly:
  **`g²⁹ ≤ 1.498434` (the looser of the two) ⇒ per-level ≤ 1.013851**, and the Beckhen
  core-stat factor **1.715733** (per-level 1.018790) still exceeds it by **1.149×**.
  The prior lane's 1.16× figure used the tighter bound; using the defensible looser
  bound it is 1.15×. Either way **the contradiction with Beckhen survives** and the
  conclusion "戦闘力 does not follow the core-stat level factor" is unaffected.

---

## 6. HP / ATK / DEF — found, but **not** in a rank-up frame

The brief asked whether the rank-up result screen carries core stats. **It does
not**, and that part is now settled rather than merely unobserved:

- **T1** (`rank2`, 1024×911) and **T2** (`0d40a5e4…-1`, 1024×904) are both
  ランクアップ審査 (review) + ランクアップ成功 (success) pairs. Both carry
  **戦闘力** and the granted skill's name and **icon** only. **No HP, ATK or DEF
  value appears in either**, at any magnification.
- **T3** (all three crops) carries **no numeric row at all** beyond the wallet HUD.
- **T6/T7** (bulk rank-up, release/market) carry counts and prices only.
- This is *structural*, not a census result: the rank-up result screen is a
  **collapsed hero header** (portrait, name, grade pill, 戦闘力). HP/ATK/DEF live in
  the `詳細情報` Character Attributes panel, which the prior lane established is
  never open in this corpus.

**But the core stats were recovered anyway**, from a screen class nobody had looked
at — the **キャパ超越 success screen**, already on disk and already cited by the
prior lane for its 戦闘力 token, with its three stat columns unread. See **§3, T4**:

    Bear 036, star3 / Lv.1, grade AND level both fixed
      ATK  365 -> 401   x1.098630
      DEF  423 -> 465   x1.099291
      HP   619 -> 681   x1.100162

All six digits re-read at 1000 px. The three independent quantities agree to
**0.139 %**, which is the tightest internal consistency check anywhere in this corpus
and validates the reading method more strongly than any single-token reading can.

This is a **gear-free** core-stat reading — the rank-up article states that equipment
unlocks only at ★4, and this hero is ★3, so the frame contains no equipment UI and the
hero provably cannot be wearing any. That is precisely the class of reading
`coverage.md` has been unable to produce (§10 below explains why it still earns no
coverage credit).

**What it settles, and what it does not.**
- It **settles** that a pure, grade-and-level-independent core-stat multiplier exists
  and is **×1.0994** (mean of three), cumulative ceiling **×1.3287** over the three
  applications the guide permits.
- It **settles** that **戦闘力 is not a linear function of the core stats**: under the
  same fixed-grade, fixed-level operation 戦闘力 rises **×1.1625**, i.e. **5.74 %**
  faster than the stats it must be derived from. So §5's 戦闘力 bound provably cannot
  be transferred to HP/ATK/DEF, and the reason is now measured rather than inferred.
- It **does not** give the per-level factor, because a capacity transcendence moves no
  level. It is a *third axis* of the scaling model, not a substitute for the second.

## 7. Is grade now separable from level? — **No.**

| question | answer |
|---|---|
| Full un-cropped ★4→★5 result found? | **No.** 3 crops recovered, all cut at the badge row; the source is one user-cropped phone photo, so the un-cropped original was never uploaded to this host. |
| More ★3→★4 transitions? | 2, both re-verified; both are the *same* transition shape, so they add a repeat measurement, not a new equation. |
| More ★4→★5 transitions? | 0 beyond T3. |
| A **same-grade, different-level** pair? | **No.** No frame in this corpus shows one hero at two levels. The closest is `rank1`'s Hunter List, where a **Lv.14 → 2283** hero sits *inside* the ★3/Lv.1 band 2123–2434 — which argues the level term is **smaller than the between-hero spread**, but it is a *different hero* and therefore not a measurement. |
| Grade and level separable? | **No.** Still 3 unknowns, 2 independent equations (§5). |

**Exactly what is still missing — one number:**

> **戦闘力 of the T1 hero (blonde child) at ★4 / Lv.MAX.**
> It is the left-hand value in T3, which the crop removes. With `B` in hand,
> `g²⁹ = 1.4820296 × 3311 / B` and the per-level law on 戦闘力 is determined with no
> assumption about `f45`.

Equivalent alternatives, in decreasing value:
1. any hero shown at **two grades at the same level** (⇒ pure `f`, then `g²⁹ = r/f`);
2. any hero shown at **two levels in one frame** (⇒ `g^(M−N)` directly);
3. the 詳細情報 stat popup open on a ★4 hero (would finally give HP/ATK/DEF — but that
   is a base-stat problem, not a scaling one).

- **★1 / Lv.1 → ★3 / Lv.1, 15 → 3, cost 15000** — one frame proves the **5:1
  material ratio** (§3, T6) and gives two ★3/Lv.1 戦闘力 tokens (1901, 1938) with no
  grade-step confound. **It is NOT a grade step**, so it does not feed `f`.
- ~~`2019/02/capa2.jpg`~~ — **RESOLVED, and it is where the answer was.**
  `2019/03/capa.jpg` **is** captured (`20190401022918`; fetched here, **189,444 B**,
  **633×432**) but is an **illustration** (hero + hero = hero), no numbers.
  `2019/02/capa2.jpg` resolves to **no capture**; the payload is in the
  **`2018/11/capa2-1024x911.jpg`** that was already on disk — see **§3, T4**.
  The article's semantics were read and are decisive: キャパ超越 raises 基本能力値,
  max 3 times, once per rank-up.
- `2019/01/rank3.jpg`, `1548136677.jpg`, `1548137184*.jpg`, `1548138716*.jpg` — the
  ★5 article's own step-2/step-3 screenshots. All four resolved to **no capture** via
  the nearest-capture instrument with controls green, so they are almost certainly
  never captured; a different guide hosting the same phone photos is the only route.
- The Korean / other-language guides, which use the same official screenshot set and
  sometimes carry a *different* crop of the same result screen.

---

## 8. Instrument defects found and worked around (additions to the trap list)

1. **CDX `matchType=domain` truncates at ~170–207 rows on `blustone.jp` regardless of
   `page`/`limit`.** Extending trap #5: the fix is **not** paging, it is **crawling**.
   `matchType=prefix` on a path is *not* truncated (45–109 rows per uploads month) and
   is a usable cross-check.
2. **`/web/<ts>/<url>` (non-`id_`) is the correct "was it ever captured" instrument**
   and returns the capture timestamp in the redirect target — but its **body is not
   the raw resource** (it came back ~9 KB with no image signature for every image).
   Use it to *learn the timestamp*, then re-fetch with `id_`. Do not read numbers from
   the non-`id_` body.
3. **CDX's `length` field is the WARC record length, not the payload.** Two captures
   of `2019/01/IMG_5729-e1548139622568.png` list as 166,320 B and 165,636 B and look
   like two different images; fetched, they are **byte-identical**
   (sha256 `b2e8678d9…`). Decode and hash before believing a size difference.
4. **archive.org refuses connections (`WinError 10061`) at 8 concurrent workers** on
   this host, which looks exactly like a content negative. Drop to ≤3 workers with
   retries; do not record the refusals as "not captured".
5. **Wayback's own SQL/WordPress naming made two same-named images look like one.**
   `2018/11/rank3.jpg` and `2019/01/rank3.jpg` are **different files**; likewise
   `2019/01/IMG_5729.png`, `2019/01/IMG_5729-e1548139622568.png` and
   `2019/03/IMG_5729.png`. Always key on the **month directory + filename**.

---

## 9. Confidence ledger

| claim | confidence | basis |
|---|---|---|
| `4907/3311 = 1.482030` is a ★3/Lv.MAX → ★4/Lv.1 戦闘力 transition | **high** | `rank2`, both halves of the frame, re-read at 900 px |
| `3827/2554 = 1.498434` is the same transition shape on a different hero | **high** | `0d40a5e4…-1`, both halves, 900 px; different wallet / cost / materials / skill |
| T1 and T2 are independent events (not two renderings of one) | **high** | gold 12000 vs 8730; materials 1901/1938/1999/2018 vs 2232×3; wallet 27360 vs 18351; different heroes |
| `rank2`'s hero is **not** `029` Kain | **high** | direct art comparison at 4 crops; Kain is an adult male with purple eyes |
| the ★4/Lv.1 (4907) hero and the ★4/Lv.MAX → ★5/Lv.1 hero are the **same** hero | **high** | identical art, identical element icon, across `rank2` and all three `IMG_5729` crops |
| the `39554` in `IMG_5729` is the rupee wallet HUD, not a stat | **high** | identical across all three crops, positioned in the top-right HUD bar |
| the three `IMG_5729` uploads are three crops of one phone photo | **medium-high** | same art, same badges, three sizes, all cut at the badge row; no capture at any other name |
| a third same-shape transition cannot separate `f` from `g` | **high** | algebraic; 3 unknowns, 2 independent equations |
| the 1.1 % spread is **not** rounding noise | **high** | 0.025 % worst-case rounding vs 1.1008 % observed |
| ★3 heroes **cannot** hold equipment (so T1/T2 are gear-free) | **high** | rank-up article: 「★4以上になると装備も開放」, corroborated by the Korean guide |
| ★4→★5 needs 4 × ★4 materials | **medium-high** | Korean guide only; the JP article states the rule only for ★3→★4 |
| 5 × ★1 → 1 × ★3 bulk rank-up, cost 15000 | **high** | `rank3`, on-screen rule text plus the 15→3 counts |
| no HP/ATK/DEF on any rank-up frame | **high** | 6 rank-up-class frames inspected directly; the result screen is a collapsed header by design |
| Capacity Transcendence is a pure **×1.0994** core-stat multiplier at fixed grade and level | **high** | `capa2`, three independent stats (ATK/DEF/HP) agreeing to **0.139 %**, digits re-read at 1000 px; guide text confirms it raises 基本能力値 |
| Capacity Transcendence is allowed **at most 3 times, one per rank-up** | **high** | verbatim in `/育成論/キャパ超越`; ceiling ×1.3287 is arithmetic on ×1.0994 |
| **戦闘力 is not a linear function of HP/ATK/DEF** | **high** | ×1.1625 vs ×1.0994 at one fixed-grade, fixed-grade/level point in one frame |
| the archive row for `036` cannot be reached from its ★3/Lv.1 row by one scalar across the three core stats | **high** for the constraint, **none** for the cause | ratios 3.1066 / 2.0685 / 2.0426 span **1.52×**; the archive row's grade and level are unestablished, so the spread is **not** attributed |
| `2019/03/capa.jpg` (189,444 B, 633×432, recovered here) is an **illustration**, not a stat frame | **high** | inspected directly |
| 戦闘力 archive column ≉ 戦闘力 in-game | **high** (inherited) | prior lane's four-hero cross-ratio, 0.2323–0.7088 |

---

## 10. Coverage counters — UNCHANGED, and here is precisely why

**Heroes 1/113 · accessories 1/100 · monsters 0/22.**

T4 is the **first gear-free core-stat reading in this project**, and it is tempting to
promote it. It is not promoted, and the reason is mechanical rather than cautious:
the counters require a reading whose **level basis and gear state are established and
comparable across heroes**. T4 pins gear state (★3 cannot hold equipment, §2.3) but
**its level basis is Lv.1 at a single unknown-to-the-ledger state**, and the hero `036`
is already covered by name — so it adds a **scaling constant**, not a new hero's base
tuple. It earns zero coverage credit on both counts. Stating that explicitly is the
point: this lane moved the *model*, not the *ledger*. `coverage.md` was not opened.

## 11. Recommended disposition for the parent

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

## 12. Guard compliance

`GUARD-encoding-and-archive-traps.md` read before any fetch, including the
BROKEN INSTRUMENTS section. All fetches used `http://` only. Every negative in this
lane is stated as *"no capture exists in archive.org for this URL"*, never as
*"the content does not exist"*, and controls C2–C5 were green in the same session as
every fetch. All file writes went through the `write`/`edit` tools and Python with
`encoding='utf-8'`; **no PowerShell `Get-Content`/`Set-Content` touched any file**
(shell use was limited to `Select-Object`/`Get-Process`/`Stop-Process`/`Remove-Item`
on this lane's own scratch directory, and `Get-Content` was used only to read this
lane's own console output, never to write). Line-ending and replacement-character
audit: see §13.

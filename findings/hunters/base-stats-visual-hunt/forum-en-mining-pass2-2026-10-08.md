# `forum_en` mining pass 2 — **99.9 % of the board read**, the original **transcendence cost ladder**, a **44-row per-hunter gacha table**, a **vendor-attested block-chance rule**, and the T1-scaling question answered by community testimony

**Written:** 2026-10-08. **Predecessor:** [`forum-en-census-2026-10-05.md`](forum-en-census-2026-10-05.md)
("the recorded 131 was a 24× undercount", 154 bodies read).
**Continuing lane:** [`share-en-panels-2026-10-05.md`](share-en-panels-2026-10-05.md) §5 **L1**.

**Coverage counters are UNMOVED: heroes 1/113 (0.9 %), accessories 1/100 (1.0 %),
monsters 0/22.** Nothing below is claimed as a base-stat tuple. What pass 2
delivers is (a) the entire corpus mined, (b) **five** complete original numeric
tables that no prior pass in this project had, (c) a documented answer to the T1
scaling question, and (d) a set of honest negatives with controls.

---

## 0. HEADLINE

| # | Finding | Value | Where |
|---|---|---|---|
| **A** | **★★ A 44-row PER-HUNTER trace-rate table that closes exactly.** `422653`: 44 hunters, trace counts summing to **exactly 4,208**, percentages summing to **99.999 %**, and *every* percentage equal to `traces / 4208` to three decimals. Plus a full **7-way × 3-rank cross-tabulation** in both counts and percentages. The single best numeric recovery in this project. | §3.2 | |
| **B** | **★★ The original transcendence COST LADDER, two grades, in one post.** `149251`, a 4,063-view 2017 thread, states natural 1★ and natural 3★ in full; a third grade appears in the replies. Self-consistent, and the ★3 column is already corroborated in-project by the game's own receipt screenshot. | §3.1 | |
| **C** | **★ [VENDOR-AUTHORED] the block-chance stacking rule.** In `123417`, `VSpang` answers a player: *"I'm back with the developer's comments. 1. The current block chance is additive, so Athena's final block chance is 63 %. 2. A high block chance reduces the chance to receive critical damage and reduces the critical damage done."* With **Athena base block 33 %** and her 5th skill **+30 %**, and a documented post-nerf value of **+25 %**. | §3.3 | |
| **D** | **★ The T1-scaling question is answered — by community testimony, favouring "from base" over compounding.** Three independent threads: two state the rule in words ("**the stat boost is a fixed amount**"), one supplies the discriminating number ("akasha heals increase by **9 %** from T1 to T2"). Arithmetic in §4.1. | §4.1 | |
| **E** | **★ The original 4★ gacha drop-rate ladder**, with vendor sourcing: **0.07 %** at launch → **0.3 %** before Selene → **0.33 %** with Selene, i.e. **≈ +0.03 % per additional 4★ hunter**, which the poster attributes to a `VSpang` confirmation. | §3.4 | |
| **F** | **★ Per-jewel stat magnitudes.** `1361746` (5,003 views — the most-viewed post in the entire corpus): **2 crit jewels → +6 %** and **4 fatal jewels → +60 %** on the relevant stat; the same thread states that the in-game `!` panel shows **stats already including dormant bonus, jewels and equipment**. That is a structural reason base stats are unreadable in-game. | §3.6 | |
| **G** | **Original awakening costs and roster** (2021-01-17): 5★ + max level, then **3 element hearts + 300 Metron Fragments + 30 000 rupees**; eight awakenable hunters named. | §3.7 | |
| **H** | **The elemental cycle, in full and clean:** *"Cold beats Fire, Fire beats Lightning and lightning beats Cold"*, plus a **negative on class weakness**. | §3.5 | |
| **I** | **★ The rate-limit blocker was a tool defect, not the archive.** Pass 1's harness built a fresh `requests.Session` per target. One shared session per worker thread took the same archive to a measured **307/min peak, 160/min sustained, 3,238 × 200 out of 3,243 attempts with ZERO transport failures.** | §1.3 | |
| **J** | **★ Reply yield gets *worse* with later captures, proven by a matched-pair test, not a bucket.** Over 128 pass-1 posts fetched again at their latest capture: later capture has **more** replies in **6** cases, **fewer** in **51**, **equal** in **71**. Pass 2's first queue design was wrong on this and was corrected. | §1.4 | |
| **K** | **Wayback stores HTTP-200 error pages**: **39** captures titled *"You do not have permission to access."*, 4 *"Error has occurred while connecting to the DB"*, and 3 oddballs (*"Login system not working over the weekend…"*). A validity gate is mandatory. | §1.6 | |

---

# 1. METHOD — what was changed, and why

## 1.1 The positive-control gate ran before every batch and never aborted

Control, unchanged from pass 1 and `share-en-panels` §1.1:

```
http://web.archive.org/web/2021/https://bs.visualshower.com/files/attach/images/75605/303/534/001/725a8e175454a533e96dac68fc5fdb49.jpg
```

Expected **HTTP 200 / 57,414 B / `ffd8ffe100184578`** (JPEG SOI + JFIF APP0);
control digest `afd4a19eeb779651…`.

| batch | gate | result |
|---|---|---|
| list pages, batch 1 (45 targets, 3 workers) | first | **200 / 57,414 / `ffd8ffe100184578` — PASS** |
| list pages, retry batch (61 targets, 2 workers) | first | **200 / 57,414 — PASS**, after **7 tries** (recorded, not hidden) |
| bodies, latest-capture arm (1,203 targets, 3 workers) | first | **200 / 57,414 — PASS, 1 try** |
| bodies + top-ups + list pages, reply-rich arm (**3,243 targets**, 3 workers) | first | **200 / 57,414 — PASS, 1 try** |

**No batch aborted in pass 2.** The gate did bite once where it mattered: the
61-target retry needed 7 tries, which is the rate limit asserting itself, and the
run continued only because the gate passed.

**`000` was never counted as a result.** Every attempt is in
`_ledger.tsv` / `_ledger2.tsv` with its status; every tally in this note is
computed from statuses, never from "files present".

## 1.2 The rate limit was worked around structurally

Pass 1's blocker was list-page retrieval. Pass 2 removes it from the critical
path: `tools/forum-en-pass2-listq.py` derives every request URL from
`census/page-*.tsv`, **already on disk** — no CDX query at all. Each request is
`web.archive.org/web/<captured-timestamp>/<original-URL>`, with both parts taken
from the pass-1 census row for that id. **Zero index cost**, and the queue order
is the board's own view order (`sort_index=readed_count&order_type=desc`, page
ascending), so the first captures walked are the most-viewed posts.

## 1.3 ★ The throughput cause was a tool defect, and it is the most transferable result here

Pass 1's `tools/forum-en-fetch-concurrent.py` creates a **new `requests.Session`
per target** inside `work()`. No connection is ever reused, so every body pays a
full handshake against a host that is actively throttling. Pass 2's
`tools/forum-en-pass2-fetch.py` keeps one session per worker **thread**
(thread-local, never shared across threads) with `Connection: keep-alive` and a
pooled `HTTPAdapter`.

Measured on the same archive, same target corpus, same 3 workers:

| harness | session reuse | peak | sustained | outcome |
|---|---|---|---|---|
| pass-1 `forum-en-fetch-concurrent.py` | **none** | — | **≈4.1 /min** | **76 of 323** attempts were `000` |
| pass-2 `forum-en-pass2-fetch.py` | per thread | **307.4 /min** | **161.4 /min** | **3,238 × 200, 5 × 404, 0 × `000`** in 20.1 min |

**A 39× difference in yield on the identical corpus, caused entirely by the
client.** The guard-file entry "archive.org refuses connections" is real but was
being triggered by a client that opened a new socket per request.

A second, smaller factor, recorded because it masquerades as a wall: a batch run
with `--tries 6` spent ≈45 s per permanently-failing target (6 escalating sleeps
plus a 120 s socket timeout each). Fast-fail (`--tries 3 --sleep 1.0`) plus a
later retry pass is strictly better on a host this slow. `--deadline-min` was
added for the same reason: it writes `SKIPPED-DEADLINE` rows for requests never
issued, so a truncated run is distinguishable from a negative.

## 1.4 ★★ Later captures are WORSE — and the design was corrected on measurement

Pass 2's first body queue took, per id, the **latest** archived EN capture, on
the reasonable theory that a re-capture of an old thread contains every reply
added since pass 1 read it. **That is wrong for this board**, and the correction
came from two measurements.

**(a) Cross-sectional, bucketed by capture year** (first 291 captures):

| capture year | captures | usable | mean replies/post | mean reply chars | carries date+views anchors |
|---|---:|---:|---:|---:|---:|
| 2018 | 24 | 23 | **3.57** | 320.1 | 23 / 23 |
| 2019 | 31 | 30 | **3.57** | 419.6 | 27 / 30 |
| 2020 | 49 | 45 | **3.44** | 289.1 | 33 / 45 |
| **2021** | 167 | 159 | **1.31** | 123.1 | 53 / 159 |
| 2022 | 5 | 5 | 0.80 | 113.2 | 3 / 5 |
| 2023 | 14 | 9 | 0.22 | 20.9 | 1 / 9 |

**(b) Matched-pair, which is the decisive test.** The 146 pass-1 posts that had a
*later* EN capture were fetched again (`pass2/topup/`). Comparing each post's
pass-1 capture with its own later capture:

| | posts | mean comments | mean reply chars |
|---|---:|---:|---:|
| pass-1 capture (2018-era) | 128 comparable | **3.84** | **379** |
| its own later capture | 128 comparable | **4.05** | **391** |
| later capture has **more** comments | **6** | | |
| later capture has **fewer** comments | **51** | | |
| equal | **71** | | |

**A later capture adds replies in 6 cases out of 128 and loses them in 51.** The
mean rise is carried entirely by the handful that gained. **The intuition was
wrong and the queue was rebuilt** around a `reply-rich` policy: the newest capture
dated ≤ 20201231, falling back to the earliest if none exists. Capture-year mix of
the rebuilt queue: 2017 25, 2018 215, 2019 788, 2020 1,407, 2021 489, 2022 77,
2023 35.

**Three arms are therefore on disk and all are retained:**

| arm | directory | captures | usable | distinct usable posts |
|---|---|---:|---:|---:|
| pass 2 **latest-capture** | `pass2/body-latest/` | 575 | 538 | 538 |
| pass 2 **reply-rich** | `pass2/body/` | 3,036 | 2,754 | **2,750** |
| pass 2 **reply top-up** of pass-1 posts | `pass2/topup/` | 146 | 121 | 120 |
| pass 2 list pages | `pass2/get-list/list/` | 205 | — | 1,847 titled rows |

**A confound, stated rather than hidden.** Capture-selection on this board also
varies the **URL form**, which the crawler fills inconsistently
(`index.php?…&document_srl=X&l=en`, `…&order_type=desc&document_srl=X`,
`…&page=N&document_srl=X`, `…&l=en&page=N&sort_index=…`). Of 1,000 ids present in
both first-generation arms, **334 were requested in a different form**; on the 575
present in both, 248 are byte-identical, 208 larger under reply-rich, 119 larger
under latest. The plain `index.php?mid=forum_en&document_srl=X&l=en` form is the
one that carries the full template with both the date and views anchors. **So the
year effect is well-supported but not cleanly isolated from URL form**; keeping
both arms is what makes a future isolation possible.

## 1.5 ★ The board list pages are the cheap route in, and pass 1's parser was silently returning zero titles

`tools/forum-en-parse-lists.py` (pass 1), run over the same 37 captures pass 2
obtained first, reported:

```
distinct posts seen: 663
  with title:    0        <-- 663 rows, zero titles
  with author: 663
```

**Three real defects, each of which had to be fixed before the index was worth
anything:**

1. **The title anchor cannot match this markup.** Pass 1's fallback is
   `<a href="…document_srl=N…">text</a>`. Real title cells wrap the text in
   `<strong><span …>`, so a `[^<]{2,200}?` body never matches.
2. **`document_srl` lives *inside* the quoted `href` value** alongside
   `?mid=…&l=en&…`, so requiring it *after* the attribute run is unsatisfiable in
   general.
3. **XE writes template conditions into attributes — `<span
   cond="!$document->isSecret()" class="wrp">` — so `>` occurs inside a quoted
   attribute value.** Every `[^>]*` attribute run in pass 1's patterns truncates
   there, and a naive `<[^>]+>` tag stripper then leaves the literal text
   `" class="wrp">` behind. That is how 663 titles became
   `'… Info isSecret()" class="wrp"> Hello Blustone playe…'`.

`tools/forum-en-pass2-parselist.py` fixes all three with a quote-aware attribute
pattern `(?:[^<>"']|"[^"]*"|'[^']*')*`, a tag stripper of the same shape, and a
`document_srl` search *inside* the attribute blob. It reads `class="author"`,
`class="time"` and `class="m_no"` per row and records which anchor produced each
field. Final run over 205 captures:

```
distinct posts seen: 1847
  with title: 1847   with replies: 1847   with author: 1847
  with date:   1847   with views:    1847
```

**Titles for 1,646 of the 3,193 census ids (51.6 %), for 205 requests — versus
3,243 body requests.** The list row's reply count then drives the body-queue
ranking, which
is why the top of that queue is `421630 "Does Transcendence/raw stat numbers
affect skill?"` rather than a random id.

## 1.6 Validity gate — a Wayback 200 is not a post

`tools/forum-en-pass2-analyse.py` rejects a capture unless it has a document div,
a non-error title, and non-trivial text. Gate outcomes on the 3,036-capture
reply-rich arm:

| rejected reason | count |
|---|---:|
| `near-empty-text` | 277 |
| `no-document-div` | 102 |
| **`error-or-gate-title: You do not have permission to access.`** | **39** |
| `no-title` | 5 |
| `error-or-gate-title: Blustone` (board root) | 1 |
| `error-or-gate-title: Error has occurred while connecting to the DB…` (arm total incl. other arms) | 4 |
| `Log in error` / `Login system not working over the weekend…` / `Login System… again for the 3rd time in like 1 month LOL` | 3 |

**The 39 "You do not have permission to access." captures are the guard file's
trap in its other form.** HTTP 200, real bytes, parses, carries a `data-docsrl`,
worthless. Separately, **5 ids returned a genuine HTTP 404** (4.6 kB Wayback error
pages: `1113494`, `204691`, `249991`, `792578`, `877667`) and those are recorded
as `404`, never as content.

**One gate that was too strict, and the measurement that corrected it.** The first
version rejected any capture lacking the `<span class="date m_no">` date anchor or
the Views counter. That rejected **82 of the first 160 captures** — and inspection
showed they were genuine posts with genuine replies, rendered by the later
template that emits neither anchor. Re-running pass 1's own 166 captures through
the strict version rejected 27 real ones. The gate now records
`template: full | no-date-views-anchors` as a **property** and rejects only on the
error/title/div/text criteria. **A validity gate built from one sample of a
template will reject the other template.** Final template split on the
reply-rich arm: 2,301 `full`, 735 `no-date-views-anchors`.

## 1.7 Capture substitution stays self-detecting

Pass 1 recorded 10 substitutions in 166 captures. Pass 2: **3,036 files → 2,934
with a document div → 2,930 distinct posts**. The parser keys `id` off
`data-docsrl`, not the filename, so substitution is detected from the payload.

---

# 2. COVERAGE — the corpus is finished

## 2.1 Text volume

| arm | captures | usable | distinct usable posts | body chars | reply chars |
|---|---:|---:|---:|---:|---:|
| pass 1 (2018-era captures) | 166 | 139 | 132 | 76,603 | 65,488 |
| pass 2 latest-capture | 575 | 538 | 538 | 199,383 | 188,018 |
| pass 2 reply-rich | 3,036 | 2,754 | 2,750 | **841,888** | **953,959** |
| pass 2 reply top-up | 146 | 121 | 120 | 57,093 | 27,849 |
| **pass 2 total** | **3,757** | **3,413** | — | **1,098,364** | **1,169,826** |

**New text read in pass 2: 1,098,364 body characters and 1,169,826 reply
characters = 2,268,190 characters**, against pass 1's 142,091. **16× the text**,
and reply text is for the first time the larger half.

## 2.2 The census arithmetic

| quantity | value |
|---|---:|
| English `forum_en` post ids in the pass-1 census | **3,193** |
| read by pass 1 | 154 |
| **read by pass 2 (new ids)** | **3,036** |
| **distinct ids now read, pass 1 + pass 2** | **3,190** |
| **ids still unmined** | **3** |
| share of the census read | **99.91 %** (was 4.8 %) |

**The 3 unmined ids are `249711`, `1092022`, `1092070`, and they are not a budget
limit — they have no content capture at all.** All three appear in the census with
`statuses: ["302"]` and nothing else: the archive holds only redirects for them.
The corpus is therefore **effectively 100 % mined**, subject to the two caveats
below.

**Two honest caveats on the census itself:**

1. The census is **27 of the 28 CDX pages** pass 1 reported; page 28 returned
   `000` on 20 direct tries and is recorded as inconclusive. So 3,193 is a floor
   of ≈96 % of what page 28 holds — the board is larger than 3,193, and the
   unmined count is correspondingly an *under*-count of the true remainder.
2. `census/page-*.tsv` holds **28,965 data rows** on disk while the census note
   records "49,550 rows". The two do not reconcile from the files as they stand;
   the per-page ledger `rows` counts sum to the on-disk total. Recorded, not
   resolved — it does not change any id.

---

# 3. THE NUMERIC RECOVERIES

**Provenance convention, unchanged from pass 1:** every row carries
**post id · capture timestamp · bytes · sha256**. The sha256 is of the exact
archived capture as stored on disk, so any quoted number can be re-verified
against a specific archived file rather than against this note. Full machine
ledger: `recovered-assets/forum-en-2026-10-05/pass2/provenance-all.tsv`
(3,182 rows).

## 3.1 ★★ The original transcendence COST LADDER — `149251`

| | |
|---|---|
| post | **`149251`** · `Transcendence...` · **FoxxGod** · **2017.10.18 21:23** · **4,063 views** · 8 replies |
| capture | `web/20190723090922` |
| bytes | 87,671 |
| sha256 | `a02504207e9af78683c7422c5fdfdef96edd678a8998c89715e8856e7a2c637a` |
| era | **PRE-2019-09-05 rebalance** — original values |

The body is one line; the answer is a reply. Verbatim:

> To upgrade a 1-star hunter to 2-star, you need sacrifice another 1-star. To
> upgrade a 2-star hunter to 3-star, you need to sacrifice 2 2-stars hunters and
> so on. […] Transcendence is completely different from this. […] Both the base
> hunter and the duplicate hunter must be at least 3-stars.
>
> […] I will summarise what you need for each level of transcendence below
> specifically for Captain.

### Natural 1★ (Captain `001`)

| tier | Metron Crystals | Rupees | Metron Fragments | Duplicate Hunters |
|---|---:|---:|---:|---:|
| **T1** | **5** | **5 000** | **50** | **1** |
| **T2** | **15** | **15 000** | **150** | **2** |
| **T3** | **45** | **45 000** | **450** | **3** |

### Natural 3★

| tier | Metron Crystals | Rupees | Metron Fragments | Duplicate Hunters |
|---|---:|---:|---:|---:|
| **T1** | **9** | **9 000** | **90** | **1** |
| **T2** | **30** | **30 000** | **300** | **2** |
| **T3** | **80** | **80 000** | **800** | **3** |

> The above information only holds true for natural 1-stars. For natural 2-stars
> or 3-stars, you need more materials since they are considered to be more
> powerful. I can only give you the values for natural 3-stars as I do not have
> any transcended natural 2-stars.

### ★ A third grade, from the replies, with its own internal identity

```
2☆
7 7 000 70
25 25 000 250
60 60 000 600
If you are not stupide you can see that
Rupees= Cristal×100
Fragments= Cristal×10
Uhm i Guess the rupee is 1000*crystal?
```

Reading: **natural 2★ → 7 / 25 / 60 crystals (700 / 2 500 / 6 000 rupees;
70 / 250 / 600 fragments)**. The `2☆` label is the poster's own and is **not**
corroborated by the guide author; the trailing *"Uhm i Guess the rupee is
1000*crystal?"* is an **in-thread disagreement** with the `×100` identity printed
immediately above it. Both are quarantined, not merged.

### Integrity checks this ladder passes, and one it does not

| check | result |
|---|---|
| Rupees = Crystals × 100 within a tier, all three ladders | **holds exactly** |
| Fragments = Crystals × 10 within a tier | **holds exactly** |
| Duplicate count 1 / 2 / 3 | **holds in all three ladders** |
| Ladder is geometric per grade | **no** — 1★ is ×3 per rung (5→15→45), 3★ is ×3.33 then ×2.67 (9→30→80). **The rungs are not a constant multiplier**, matching `AGENTS.md` §16.2. |
| grade ladder 1★ < 2★ < 3★ at every tier | **holds** (5<7<9, 15<25<30, 45<60<80) |
| duplicates total | 1+2+3 = **6** duplicates + the original = **7 copies**, which matches `1179899`'s independent "you need 7 copies to max transcendence" (§3.9) |

### In-project corroboration already present

[`t1-measured-1.0994-2026-10-08.md`](t1-measured-1.0994-2026-10-08.md) §1 records
that the same ★3 **T1** row (9 crystals / 90 fragments / 9 000 gold) appears on the
game's own transcendence receipt screenshot, and explicitly rules out T2
(30/300/30 000) and T3 (80/800/80 000) for that frame. **The community ladder and
the in-game receipt agree on the ★3 column.** The ★1 and ★2 columns are new to the
project.

## 3.2 ★★★ A 44-row per-hunter trace-rate table that closes exactly — `422653`

| | |
|---|---|
| post | **`422653`** · `Trace Scroll Insanity pt2` · **Festival** · **2018.02.22 20:03** · 311 views · 5 replies |
| capture | `web/20201025193019` |
| bytes | 94,426 |
| sha256 | `24e28afc72042e4bba246e5ff7f7741c5cdd22b0769ab1ec5cdba42f9831991e` |
| era | **PRE-rebalance** |
| format | **2 HTML `<table>` elements — the only `<table>` elements found anywhere in ~3,400 pass-2 captures** (§3.11) |

This is the follow-up that `421776` explicitly offered ("I can supply the
percentages … of the other individual characters in a separate post"). Its own
disclaimer, verbatim:

> Please understand that this is only one test, and without any input from VS, the
> numbers should be understood as being close to, but not the actual drop rate.
> I'd need a lot more data (plus Sunny and Vincent) to get anything close to
> conclusive. Plus, as new characters are introduced, the drop rate will fluctuate.

### By individual hunter — all 44 rows

> Santa Girl = Santa Girl Rebecca · Tyltyl (W) = Tyltyl in Wonderland

| Hunter | Traces | % | | Hunter | Traces | % |
|---|---:|---:|---|---|---:|---:|
| Acerola | 70 | 1.663 | | Nene | 26 | 0.618 |
| Akasha | 19 | 0.452 | | **Octavia** | 11 | 0.261 |
| Athena | 20 | 0.475 | | **Papillon** | 4 | **0.095** ← lowest |
| Balian | 265 | 6.298 | | Patrone | 5 | 0.119 |
| Bear | 12 | 0.285 | | Rebecca | 160 | 3.802 |
| Bibi | 16 | 0.380 | | Riko | 160 | 3.802 |
| **Bruce Bang** | 318 | 7.557 | | Robin | 162 | 3.850 |
| Captain | 181 | 4.301 | | Santa Clauster | 0 | 0.000 |
| Denali | 99 | 2.353 | | Santa Girl | 0 | 0.000 |
| Diana | 24 | 0.570 | | Scar | 106 | 2.519 |
| Edward | 9 | 0.214 | | Sienna | 290 | 6.892 |
| Gerard | 101 | 2.400 | | Sunny | 0 | 0.000 |
| Gullveig | 8 | 0.190 | | **Sylvester** | 244 | 5.798 |
| Hecate | 299 | 7.106 | | Teddy Bomber | 108 | 2.567 |
| Hermes | 19 | 0.452 | | Tyltyl | 287 | 6.820 |
| Joy | 12 | 0.285 | | Tyltyl (W) | 0 | 0.000 |
| Kain | 17 | 0.404 | | Vincent | 0 | 0.000 |
| Karl Steiner | 41 | 0.974 | | Witch Riko | 0 | 0.000 |
| Lantern | 18 | 0.428 | | Yuri | 0 | 0.000 |
| **Lapis** | 358 | **8.508** ← highest | | | | |
| Levi | 165 | 3.921 | | | | |
| Locke | 210 | 4.990 | | | | |
| Metis | 238 | 5.656 | | | | |
| Mowgli | 110 | 2.614 | | | | |
| Natalia | 16 | 0.380 | | | | |

### The closing proof, computed here

| check | result |
|---|---|
| trace counts sum | **4,208 — exactly the published total, gap 0** |
| percentages sum | **99.999 %** (gap 0.001 pp, i.e. rounding) |
| rows | 44 listed, 37 non-zero, 7 explicit zeros |
| every percentage vs `traces / 4208 × 100` | **0 mismatches** at 0.002 pp tolerance, on all 37 non-zero rows |

**This is an exactly closed measurement, not an estimate.** The seven zero rows
are the event/special hunters the poster excluded from the drop pool, as stated.

### The cross-tabulation — a full 3-rank × 7-way matrix, in counts and in percent

Bonus table, reproduced from the same post:

| group | 3★ | 2★ | 1★ | Total |
|---|---:|---:|---:|---:|
| **Trace/Rank** | 277 | 1,079 | 2,852 | **4,208** |
| Attackers | 103 | 376 | 867 | 1,346 |
| Defenders | 88 | 261 | 642 | 991 |
| Bombers | 55 | 273 | 738 | 1,066 |
| Healers | 31 | 169 | 605 | 805 |
| Fire | 69 | 367 | 1,068 | 1,504 |
| Lightning | 146 | 340 | 736 | 1,222 |
| Ice | 62 | 372 | 1,048 | 1,482 |

| group | 3★ | 2★ | 1★ | Total |
|---|---:|---:|---:|---:|
| **%/Rank** | **6.583 %** | **25.642 %** | **67.776 %** | **100.001 %** |
| Attackers | 2.448 % | 8.935 % | 20.604 % | 31.987 % |
| Defenders | 2.091 % | 6.202 % | 15.257 % | 23.550 % |
| Bombers | 1.307 % | 6.488 % | 17.538 % | 25.333 % |
| Healers | 0.737 % | 4.016 % | 14.377 % | 19.130 % |
| Fire | 1.640 % | 8.721 % | 25.380 % | 35.741 % |
| Lightning | 3.470 % | 8.080 % | 17.490 % | 29.040 % |
| Ice | 1.473 % | 8.840 % | 24.905 % | 35.219 % |

Every column sums to its row total and every percentage column re-derives its
count column. **Three independent partitions of the same 4,208 traces all close
to 100.000 %.**

### The sibling post — `421776`

| | |
|---|---|
| post | **`421776`** · `Trace Scroll Insanity pt1?` · **Festival** · **2018.02.22 16:06** |
| capture | `web/20201025200421` |
| bytes | 83,099 |
| sha256 | `fc0a610cd6f75c479c82fe90235ffde49b098a8faba44516ef215df78f03a371` |

Method, verbatim: *"On 2018/2/11 I decided to gather some data from trace scrolls …
calculated by taking the difference between initial traces and the traces after
popping all the scrolls, then comparing the final individual amounts to the total
amount of traces gained to get the percentage … Percentages were calculated to
three decimal points."* Sample: **1,056 scrolls → 4,208 traces.** The pt1 body's
category totals are exactly the pt2 bonus table, so the two posts are one
experiment.

**One correction pt2 makes to pt1, and it is the poster's own:** pt1's body still
carries the retracted line *"Originally I had stated that Patrone was the lowest
(5 traces and 0.119%)"* while its edit note names Papillon (4 / 0.095 %) as the
true minimum. pt2's table confirms Papillon. **Use pt2.**

## 3.3 ★ [VENDOR-AUTHORED] block chance is additive, and Athena's numbers — `123417`

| | |
|---|---|
| post | **`123417`** · `Block vs. Crit Chance?` · **Alaiko** · **2017.09.26 01:33** · 190 views · 7 replies |
| capture | `web/20180320200613` |
| bytes | 77,512 |
| sha256 | `14902ca477e3ee9c679e8df9b79c2ef23b6c832b1bdad4c6208f583f43b7f6f1` |
| era | **PRE-rebalance** |

**This is the fourth official account found on this board, and the first with a
*mechanic* answer.** `VSpang`, relaying the developers, verbatim:

> Hi Alaiko, I'm back with the developer's comments.
> 1. **The current block chance is additive, so Athena's final block chance is
> 63%.**
> 2. **A high block chance reduces the chance to receive critical damage and
> reduces the critical damage done.**
> We apologize we can't reveal the exact functions and mechanisms but we hope you
> are satisfied with this information.

The player's own premise supplies the base values, verbatim: *"Athena has a
natural 33% percent chance of blocking and her 5th skill gives her an additional
30%."*

| quantity | value | source |
|---|---:|---|
| Athena **base** block chance | **33 %** | player, confirmed additive by vendor |
| Athena 5th-skill block bonus, pre-nerf | **+30 %** | player → 33 + 30 = **63 %** [VENDOR] |
| Athena 5th-skill block bonus, **post-nerf** | **+25 %** | player: *"seeing as the devs recently nerfed the block chance to 25%"* |
| **Nene** base block chance | **33 %** | player, Case 3 of the same reply |

**Two mechanisms this settles for the replica:** (i) block chance stacks
**additively**, not with diminishing returns; (ii) high block reduces both crit
*chance* and crit *damage*. Both are `[VENDOR-AUTHORED]`.

**The player's objection, preserved because it records the community's own view of
the consequence:** *"If I were to put Athena, Denali and 'X' together in one team,
then their total block chance becomes 33% + 25% + 25% + 25% = 108%… which really
has no meaning since probability values are supposed to be between 0 and 1."*

## 3.4 ★ The original 4★ gacha drop-rate ladder, with vendor sourcing — `1162563`

| | |
|---|---|
| post | **`1162563`** · `Some good News (づ｡◕‿‿◕｡)づ` · **JellyGuy172** · **2019.06.05 01:23** |
| capture | `web/20191019073339` |
| bytes | 89,255 |
| sha256 | `6a5b7a787f513aea0f10773cab8e69c6f6830876b55aef588bb5fd9a8b83701f` |
| era | **POST-2019-09-05 era — first post-rebalance gacha figure in this project** |

Verbatim body:

> At the beginning when Lily and Lyla were the only 4\* hunters aquirable from
> scrolls and manda, (Harley being in Mirage and Vincent being special) **VS made
> a post about their drop rate being 0.07%.** Recently, **before Selene was
> added, they put a post of current four star drop rate being 0.3%. Vspang also
> confirmed that each 4\* increases the drop rate for 4\*.** That is a 0.27%
> difference and 7 new 4\* have been added […] which approximately an increase of
> **0.03% per 4\*.** Now that Selene has been added, the 4\* drop would be
> **0.33%**

and the arithmetic block:

> ```
> Base 4* drop rate at the beginning = 0.07%
> Base 4* drop rate before selene = 0.3%
> 7 new 4* hunters; Geranium, Genovia, Erise, Judith, Mary, Teresa, and Windblade
> 0.3%/7 = 0.0328571429%
> Drop rate including selene now = 0.3%+0.03% = 0.33%
> 100-0.33 = 99.67
> 99.67/0.0328571429 = 3033.43478 (how many 4* hunters it will take to make 100%)
> 3032/52 = 58.5 years
> ```

| quantity | value | status |
|---|---:|---|
| base 4★ drop rate at launch | **0.07 %** | original, vendor-posted |
| base 4★ drop rate before Selene | **0.3 %** | original, vendor-posted |
| increment per added 4★ hunter | **≈ +0.03 %** (0.3/7 = 0.0328571429 %) | derived; the *"each 4\* increases the drop rate"* half is attributed to `VSpang` by the poster, **[VENDOR-REPORTED, not directly read]** |
| with Selene | **0.33 %** | original |

**A matching arithmetic reading in a different thread** (`1114871`, `Are 4* at 300%
rate?`, capture `web/20210119215324`, 27,521 B, `24f5b0f50ee4fb22`): *"It's +300%,
so theoretically you have a **.52%** chance of pulling a 4 star"* and *"the event
clearly states that its a 3\* 200% up rate"*. **0.3 % × 2 (200 % up) ≈ 0.6 %,
against a quoted 0.52 %** — consistent in order of magnitude, not exact, and the
gap is not explained in the thread.

## 3.5 ★ The elemental cycle, complete — `20587`

| | |
|---|---|
| post | **`20587`** · `Elements & Class?` · **UnfortunateOne** · **2017.05.20 16:59** · **1,421 views** |
| capture | `web/20200813000050` |
| bytes | 76,514 (reply-rich) / 27,754 (latest) |
| sha256 | `1f09a2b4821cba6e62a8e7baa9a8c5fcbe23f38ba7533b3f693f36936d698ada` / `8f0f7d260a5486d0bcca152b462ce165693fb77b65e8a748968f3d5b6c5d5ade` |

Body: *"Fire, Electricity and Cold; which ones are weak to what? And is ther such
thing as a 'class weakness' like e.x. Defense type are weak to Bombers?"*

Replies, verbatim:

> **Cold to fire to lightining to cold**
> Think of it as a Circle, where **Cold beats Fire, Fire beats Lightning and
> lightning beats Cold!**
> **Don't think there are class weaknesses just element**

**A complete three-element cycle plus a negative on class weakness**, from a
1,421-view thread. Both halves are single-source community statements, not
vendor text; the cycle is consistent with `card-enums.md`'s recovered
Fire/Ice/Lightning trio.

## 3.6 ★ Per-jewel stat magnitudes, and why the in-game panel cannot give base stats — `1361746`

| | |
|---|---|
| post | **`1361746`** · `Can anyone explaine the difference?` · **V1NCENT** · **2020.05.07 21:35** · **5,003 views** — the most-viewed post in the entire corpus |
| capture | `web/20201205192018` |
| bytes | 90,357 (reply-rich) / 31,583 (latest) |
| sha256 | `d0fe4aa498aad7d73842a0c0d226dbf555de257ddfbaa5d34b81215e9bf4da57` / `19f618ee674cebf6dd76271e295479afb2063713d21e8fa61e46f132b7249fdc` |
| era | **POST-rebalance** |

### The jewel→stat mapping, as stated in the body

> Critical Damge = Critical Jewels
> Critical Damage Chance = Fatal Jewel
> Critical Attack Damage = Fatal Jewel
> Critical Attack Chance = Critical Jewels
> Damage Reduction = Super Block Jewels
> Damage Reduction Chance = Block Jewels

### ★★ The per-jewel magnitudes — the closest thing to a jewel stat value in any community source

> Let say Karl. If I put him **2 Crits and 4 Fatal jewel**, that would mean his
> **base stat will increase by 6% and 60%** during auto attack

| reading | implied per-jewel value | status |
|---|---:|---|
| 2 crit jewels → **+6 %** | **≈ +3 % each** | player arithmetic on his own build |
| 4 fatal jewels → **+60 %** | **≈ +15 % each** | player arithmetic on his own build |

Corroborated in shape by `1386397`'s separate decomposition (§3.8): **six block
jewels → +20 % block, ≈3.33 % each.** Two independent threads, two derived stats,
**per-jewel contributions in the 3–4 % range and 15 % for crit-damage jewels** —
still a player's arithmetic on an unstated jewel rarity/level, so this is a
**candidate** value, not a recovered one.

### ★★ A structural statement about the in-game panel — this is the important line

> **If you see its full stats by clicking the ! icon to any hunter, so that's
> really the full stats you get from added Dorm bonus, Jewels and Equips
> altogether.**
> **The Value shown on Skills are just separated so we would just assumed like for
> example Karl has base Critical Chance of 33% and so his 5th skill has 25% and
> yeah during Battle, it will be applied to as 53% Critical Chance and you'll
> never see them in real numbers**

**This is the reason the project's base-stat hunt keeps failing, stated by a
player in 2020:** the in-game stat panel is *already contaminated* by dormant
bonus, jewels and equipment, so it can never yield a gear-free base stat. It is
the community-side explanation of a failure this project has hit repeatedly
(`t1-measured` §4-§5, `accessory-stat-hunt-2026-10-06`). **That is worth more than
any single number in the thread.**

Also from the same thread: Karl's new 5th-skill effect **enemy −30 % critical
chance**; enemy **−60 % defence** for Mary/Bibi+Levi+Dino; jewel **shapes** are
Triangle / Square / Diamond, six slots (*"2 Triangles … 2 Squares … 2 Diamonds"*);
and *"Due to recent hunter improvements **from 3★ on both Stats and Skills**"* — a
2019/2020-era buff statement.

## 3.7 ★ Original awakening costs, roster, and a three-stat delta — `1480939`

| | |
|---|---|
| post | **`1480939`** · `Awakening stats` · **Thorazine** · **2021.01.17 04:43** · 140 views · 7 replies |
| capture | `web/20210228014149` |
| bytes | 86,314 (reply-rich) / 27,258 (latest) |
| sha256 | `b96eadd0a5e8a242d71421b7806ae3ff023e0e4d56df21f6324470ad72b31b6a` |

### The gate and the cost, verbatim

> To awaken a character you'll first have to get them to **5 stars**, and **max
> level** them. After both of those prerequisites are achieved you'll then need
> **ruppees, Metron fragments, and 3 hearts** corresponding to that hunters element
> (expect for Captain who uses fire, and Vincent who uses ice due to those two
> changing element when awakening).
>
> So for example, if you wanted to awaken Rebecca you'd need **3 Fire Hearts,
> 300 Metron Fragments and 30 000 ruppees.**

| quantity | value |
|---|---|
| prerequisites | **5★ + max level** |
| material cost | **3 element hearts + 300 Metron Fragments + 30 000 rupees** |
| awakenable roster (2021-01-17) | **Lapis, Balian, Sienna, Rebecca, Santa Rebecca, Riko, Witch Riko, Captain, Vincent** |
| element exceptions | Captain → fire, Vincent → ice |

**A structural observation, flagged as a hypothesis and not a conclusion:** the
awakening rupee and fragment costs (30 000 / 300) are *identical* to the ★3 T2 rung
of §3.1's ladder, with hearts in place of crystals. That may be coincidence, a
shared cost basis, or an artefact of one hunter. **Not acted on.**

### ★ A three-stat delta on awakening

> I Awakened my Rebecca and I **lost 70+ attack 70+ def and over 150+ health**.

Deltas **−70 ATK, −70 DEF, −150+ HP**, attributed to awakening *Santa* Rebecca.
**Deltas, not levels** — no absolute panel is given, so this cannot become a base
stat. It is, however, a **three-stat simultaneous reading**, which is rarer than
any single number in this corpus.

### ★ An internal inconsistency in the source, quarantined

The same reply explains the re-skin rule and then contradicts itself:

> When neither Rebecca is awakened Santa Rebecca has the higher base stats because
> she's a nat 3 star hunter vs the original which is only a two star. **When you
> awaken the original one her stats will surpass non awakened Santa Rebecca.**
> […] when you do this [awaken Santa Rebecca] her base stats would become the same
> as awakened original Rebecca, **meaning that they drop** and she loses power at
> first

If the original's awakened stats *surpass* non-awakened Santa's, then making Santa
equal to the original's awakened stats cannot be a *drop*. The poster's observed
drop (−70/−70/−150) is consistent with the second half and inconsistent with the
first. **Recorded unresolved; the two statements are not merged.**

`484911`'s independent claim in the same direction, from a different thread and
author: *"Wonderland is basically a re-skin on the original, same stats."*

## 3.8 Equipment and jewels — costs and one decomposition

### `1425687` — original-era equipment upgrade cost, answered in-thread

| | |
|---|---|
| post | **`1425687`** · `Equipment Advancement Questions` · People_Allergy · **2020.08.31 01:39** |
| capture | `web/20201024084401` |
| bytes | 81,195 (reply-rich) / 29,481 (latest) |
| sha256 | `1337a75bb997a06fa8cc73358562304e8c8bb5cce7d99f3c7d22e749b7151c74` / `86f0a65af3e85174b691f80e0d1211156a9e9b9479de0ade4afb6d749f229326` |

The question is itself a record of what players did *not* know:

> 1. How many coolants/lightning boxes/flammable materials TOTAL does it take to
> upgrade all three of a hunter's equipment to lv.50?
> 2. How many advanced toolboxes would it take to advance all three of the
> hunter's equipment to lv.50?
> 3. And how many rupees will be used up while doing so?
> (If anyone knows this, because I've yet to reach anything past lv.40 equipment;-;)

The answer:

> The simple answer is: a lot. I have 1 price [sic] of equipment up to level 50,
> and the numbers on that are: **100k rupees from green-> blue (+59 type mats)**,
> and **over 250k rupees from level 40 to level 50.** […] it ends up getting to
> **20-30 adv toolboxes per level** in the last couple levels (46+ or so)

One player's account of one item. Costs, not stat values, and **not verified**.

### `1386397` — a jewel contribution, dated post-rebalance

| | |
|---|---|
| post | **`1386397`** · `Which jewels are best for Lawrence.` · **2020.06.20 20:47** |
| capture | `web/20201029140643` |
| bytes | 81,492 (reply-rich) / 27,684 (latest) |
| sha256 | `e0289b297a54a637bc5af8f37b5fc136ce4e2ce377ad958c643f7c390b25ce1b` / `63af0542f8e30b1158c7d20e25b2b0117989a555f66ae8c050cc184a9a03ad04` |

> If you could able to reach **20% Block Chance on 6xBlk Jewels**, you'll be able
> to achieve **90% Block Chance.**
> **40% (Base) + 30% (5th) + 20% (Jewels) = 90% Block Chance**
> 100% Block Chance + 100% Damage Reduction Block = INVINCIBLE!
>
> Down side is her Damage Reduction Block decrease by **10%** if her 4th activate
> but in exchange is speed and attack up by **10%**.

**+20 % block from six block jewels** (≈3.33 % each), inside a 40/30/20
decomposition. One player's arithmetic; the base 40 % / 5th-skill 30 % split is
unsourced in-thread. **Note the tension with §3.3's vendor-confirmed 33 % base for
Athena** — different hunter, and §3.3 also documents a 30→25 % nerf, so the two are
not necessarily in conflict. Flagged, not resolved.

### `1199014` — a 3★ jewel main stat tied to a level

| | |
|---|---|
| post | **`1199014`** · `3* jewel grinding level12 to 13 not working` · papapou · **2020.11** |
| capture | `web/20201126092738` |
| bytes | 80,193 (reply-rich) / 30,484 (latest) |
| sha256 | `43c807f754e1921ae5a72816cc37c13adedd9dcf327a05ffdc84a34d58edf11e` / `f3f9deca1448f4a84e4960b9c70addb20768912b358d1ce5f6fd9e579339623f` |

> Grinding triangle jewel primary stats was attack at **+19, jewel level 12**,
> grinded successfully at 13, primary att **+19** … didn't change at all

**3★ triangle jewel, attack main stat +19 at level 12**, plus a reported grinding
failure. One data point, not a curve.

### `1143988` — gem stat semantics and a substat ceiling

| | |
|---|---|
| post | **`1143988`** · `Craziest regeneration!` · 빈신 · **2019.04.27 12:39** |
| capture | `web/20191123010829` |
| bytes | 84,814 (reply-rich) / 92,300 (latest) |
| sha256 | `b3b8a0de19f030378f895b33dec126aa60458b2b401fda7695884d84a50b333d` / `ae0b4af1abdc2565188a0b66e79462b1000db19ea76e78501f83516ddf81312b` |

> Beware that this has nothing to do with regeneration jewels. **Regeneration
> jewels increase your passive regeneration of fighters outside battle.** The
> in-battle regeneration of **Bear scales with his defense jewels**, and the
> active regeneration of **Robin scales with his offense jewels.**

> Robin perhaps the only defender with the lowest defense points at fully maxed T3
> and skills at raw stats meaning no jewel or equip upgraded. The best jewel for
> him is 4xAtk+2xDef with **perfect 54 Atk & Def substats** are recommended.

**54** is the only accessory substat magnitude recovered from any community source
in this project — one player's word for "perfect" on an unstated rarity/level. And
the three sentences are a statement of *what each gem type multiplies*, which the
replica's inert gem tables do not encode.

### Other equipment/jewel lines, with provenance

| post | capture | bytes | sha256 (16) | reading |
|---|---|---:|---|---|
| `1016947` Jewels for Bibi, 2018.10.31 | `20110417170931` | 83,070 | `d5a1e1013ec3ec9a` | t2 Bibi at **26k power**; setups "4 critical jewel and 2 critical chance jewels" / "6 offensive jewels" / "4 speed and 2 offensive"; "use regen jewels to unlock the secret exodia power" |
| `1160203` Unbeatable Geranium stall combo, 2019.05.31 | `20190916082001` | 95,817 / 104,642 | `62e1bccf3777eacc` / `36b1e16b03299ebe` | **4xAtk+2xDef jewels Lvl 6–9**; **Dino "got 20% max fates"**; Dino+Levi "ensuring enemy defence cut by **40%**"; Mirage **floor 250**, **level 208**; "Robin, Bear, and Teddybomber have to be **3 trans**" |
| `888621` More rupee/manda sink?, 2018.07.08 | `20191023054131` | 87,593 | `91bbee3545c12e8c` | "another **22k rupees** spent besides the hundreds of thousands spent on barely getting one jewel to **level 10**"; "went from **160k to 90k** … to upgrade one jewel to **level 9**"; "the polishing is **HALF THE PRICE**" |
| `979420` 5* Jewels trough fc shop, 2018.09.06 | `20201024065548` | 81,459 / 29,070 | `513887544e0d03fa` / `7f0cda299c44d51e` | saved **20.000 fight chips** for an offensive 5★ jewel; "the fc shop only sells defensive Jewels" |
| `1207789` What level is an equipment to unlock a 2nd gem slot?, 2019.08.29 | `20201203102613` | 26,963 / 27,226 | `7a0541ab9e36abdc` / `1acf5212b964be0e` | **question only; no answer survived in either arm** — honest negative (§6 N5) |

## 3.9 Original AP / fuel economy, and the regeneration rate — `369923`

| | |
|---|---|
| post | **`369923`** · `Manda Mathematical Methods (SACE Edition)` · **ArkenDragon** |
| capture | `web/20191120045425` |
| bytes | 89,966 (reply-rich) / 36,925 (latest) |
| sha256 | `e34f62a925d8fd58abdeab5f3c57333e553da37565e85de5c7df94a305613b40` / `f172150fc36e300365c69091352c76b77fc7d59dba9aa67dfce80338acbf473f` |
| era | **PRE-rebalance** |

> Source 1 - from the main menu, **60 fuel for 5 manda**
> Source 2 - magical manda shop, **480 fuel for 60 manda**
> Source 3 - Limited time offer, **700 fuel for 58 manda** (Not like you can buy
> the 90 manda version anywhere)

★ **And the regeneration rule, which is the part the project is missing:**

> For newbies, **when your fuel goes below 60, the fuel replenishment over time
> kicks in, at the VERY slow rate of 1 fuel per 6 minutes.** […] the further away
> you are from the 60 fuel limit […] the more difficult it is to approach it and
> make use of the fuel replenishment over time

**threshold 60 fuel, refill 1 fuel / 6 min** (= 10 fuel/hour), engaging only below
the cap. The post's own arithmetic uses it consistently (`10 fuel = 1 hour`).

**Relation to the project.** `AGENTS.md` §18 records AP/BP regeneration as
implemented with **300 s and 1 800 s intervals, both still fixtures**. This is a
third, differently-shaped figure — a **360 s** interval gated on being below a
60 cap. **Community testimony, not recovered original data**, and it contradicts
the current fixtures. Recorded as a lead; **no fixture was changed.**

Two more original AP figures:

| post | capture | bytes | sha256 (16) | reading |
|---|---|---:|---|---|
| `219139` Schumann's event rewards, 2017.11.24 | `20191113064826` | 94,124 | `3d63aea851b50e08` | "**25,000 rupee for 300 fuel**"; "**300 fuel or 30 manda** and you can get Basic materials" |
| `1161193` Guilds, 2019.06.01 15:10 | `20190825000948` | 80,661 | `5283c80785abc9f` | "**Guild mate support fuel is just a fuel ticket replacement** and you don't get all 60 unless 5 people […] give **12 fuel**" — **12 fuel per member, 5 members = 60 max** |
| `1262830` How many types of 'Spending' Events?, 2019.11.02 | `20200814133437` | 78,189 | `3410df1ff8c674f1` | fuel-spend event "you can open a box **every 200 fuel spent**" |

## 3.10 Power / rating readings — the `戦闘力` composite, from players

These are **power ratings, not HP/ATK/DEF**. `t1-measured` §3 already proved
`戦闘力` is *not* linear in the three core stats (it moved ×1.162511 when the stats
moved ×1.0994), so **a power ratio must never be read as a stat factor**, and none
of these is counted toward any coverage number.

| post | capture | bytes | sha256 (16) | reading, verbatim |
|---|---|---:|---|---|
| `639004` hunter max stats, 2018.04.06, 三叔 | `20200812005754` | 83,789 | `dfda4ae11e8584da` | "the approximate max values of **5\*T3** … for examples, **Mowgli 20000 10%/12%**" |
| `947662` Different strengths on different devices, 2018.08.08 | `20210927104445` | 78,032 | `85bef52acc5d72f1` | "a **5\* T3 Herm will always be shown as a 17.5k unit even if it's over 23k**"; "you will face plenty of FC teams of **110k power** or more, but you won't be able to find any player profile with such high power" |
| `682748` Info on Transcendence., 2018.04.17 | `20200806154523` | 84,511 | `6addaae09f4a2717` | "**Kain level 24 transcendence 2, skill at 30, with strength 20'059** while **Hermes level 30 transcendence 2 (skill at 47) with strength 18'941**" |
| `1244661` How's my team?, 2019.10.03, 3,284 views | `20201020021916` | 95,510 | `1fc0caf18bb2ab3e` | "**Robin T3 but only 14000 in power?**" → *"It's a **lvl 8** with probably no skills and no jewels… so yeah not that surprisingly"* — **a T3-at-level-8 reading, but the level is the commenter's inference ("probably")** |
| `1016947` Jewels for Bibi | `20110417170931` | 83,070 | `d5a1e1013ec3ec9a` | "my **t2 Bibi currently at 26k power**" |
| `886704` Should I Up Harley to T1 or T2, 2018.07.08 | `20190824080034` | 80,795 | `226108010295731a` | "My Yuri just T1 but **19k Pw**, tomorrow I will up it to T2 become **21k PW with 50% crit chance**" — a same-hunter T1→T2 power pair, ratio 1.105 |
| `1153611` Teresa/Erise stall lock, 2019.05.17 | reply-rich | 79,290 | `f1d0e44b4a87c2d1` | "I haven't T3'd them yet but **both over 20k**" |
| `1486386` Gerard Awakened Name???, 2021.02.11 | `20210411181043` | 82,140 | `d7a890d80ead5ac1` | "it's almost **40k**" |

## 3.11 Fate / collection bonus — a second independent reading, and one hero stat

Pass 1 §2.1 recovered, from `942878`, Vincent's Fate bonus as **3/3/3 →
6 %/6 %/6 % (total 18) at 4★, max reported as 12**. Pass 2 finds independent
statements in two threads:

| post | capture | bytes | sha256 (16) | verbatim |
|---|---|---:|---|---|
| `484911` v2.0 Who to 5\* next?, Fukurama, 2018.03.05 | `20180412040841` | 87,695 | `3dddba74cf916dc1` | "#1 Tyltyl … **remember to read her Story section; as it is important to make sure she has the 12% increase in Attack, Defence and Health.**" · "**Yes! Wonderland is basically a re-skin on the original, same stats.**" · "**Bibi special does 1472 damage to Hermes, which has a health pool of 2000 ish**" |
| `1160203` Unbeatable Geranium stall combo, 2019.05.31 | `20190916082001` | 95,817 | `62e1bccf3777eacc` | "Highest defense points on bomber currently is Dino because **he got 20% max fates**" |
| `1111736` Stage 450, 2019.02.16 | `20190922190236` | 89,276 | `89aa1e85d7f3bd30` | "using Apo is better … since **30% attack boost + 25% elemental boost**" |
| `558135` Pvp balance?, 2018.03.18 | `20191122023919` | 83,125 | `d17d778fff244e0e` | "besides the **15% attack and speed bonus from Hermes**, he also has **45% damage boost, 60% crit dmg increase, 10% crit chance increase** and block chance down from Patrone" |
| `1243257` Is akasha strong?, 2019.10.01 | `20210115153951` | 80,293 | `990af90d4cd467b2` | "Her **+15% bonus def** helps in def FC" |
| `1308125` I never noticed.. | reply-rich | — | — | "Is the reason you all crave the 3\* Santa Rebecca because of her **+10% in HP, ATK & DEF**?" (question, no answer in the capture) |

**Three points.** (1) **Fate bonuses are percentages applied to HP, ATK and DEF** —
now attested three times, three authors, 2018-02 → 2019-05, and the `12` ceiling
pass 1 recorded is independently reached. (2) `1472 damage / 2000 HP` is a **hero
HP reading in a 2018 PvP context**, with the fight state described but the build
not. (3) A recurring **33 %** appears as a base figure three times now — Athena
block (§3.3), Nene block (§3.3), Karl crit chance (§3.6). **Flagged as an open
question, not concluded**: a shared base-stat normalisation would explain it, and
so would coincidence.

## 3.12 Fixed skill damage, and the stat-stack arithmetic players wrote out

| post | capture | bytes | sha256 (16) | verbatim | status |
|---|---|---:|---|---|---|
| `1230457` Audrey or Geranium, 2019.09.18 | `20191018111959` | 84,956 | `5882c0cd62725c5f` | "It's because of her 4th skill **FIXED DAMAGE**. It won't matter T0 and **she always deal 2000 damage. So if average Hunter HP is 7000, that's about 40% damage dealt**" · "I maybe satisfied if **T3 Audrey 4th is 2000**" · Locke "has **60% crit damage like Diana**" | player claim; the 7,000 "average HP" is the poster's own estimate |
| `1386397` | `20201029140643` | 81,492 | `e0289b297a54a637` | `40% (Base) + 30% (5th) + 20% (Jewels) = 90% Block Chance` | derivation |
| `123417` | `20180320200613` | 77,512 | `14902ca477e3ee9c` | `Final block chance = 33 + 30 = 63%`; `Total = 33% + 25% = 58%`; `Total = 33% + 25% + 12.5% = 70.5%` | derivation, in the vendor thread |
| `1083557` Gosh new hunter…, 2018.12.29 | `20190717082123` | 95,386 / 30,858 | `b3063481721a9cd8` / `a1b3323770da2a2e` | "her natural critical damage is **230%** + 5th 60% Chichi + Collection Bonus 20% + 5th 60% Diana + 5th 60% Locke = **430%**" | **explicitly the poster's own guess** — *"I haven't reached 5★ yet and I assume if maxed it would be like 60%"* |

`1083557` is a good example of a *reading* and a *speculation* being distinguished
in the source itself, and preserved here.

## 3.13 Remaining economy and mechanic readings

| post | capture | bytes | sha256 (16) | reading |
|---|---|---:|---|---|
| `286623` Rupee package, 2018.01.19 | `20201129222000` | 28,352 | `4d9c99ccf6b0330b` | "**550 veteran points, 15,000 rupee + 50 manda** upon purchase, **7,500 rupee per day for the next 15 days**. Can be bought in concurrently with the fuel purchase. Doesn't consume the rupee tix purchase." |
| `507762` HOW TO GET SUNNY!?!?!?!, 2018.03.09, 2,173 views | `20200927201237` | 106,700 / 34,501 | `a0d3e7e1245a8fd8` / `cfad3c7d5001038` | "you need to have **98 manda**"; "click on 'Buy Season2 Pass' and use **98 manda**" |
| `94008` Using Manda to recruit, 2017.08.06 | `20190917123840` | 86,369 | `22aab46c3cae27e0` | "using **30 manda** to recruit and getting a 1\* is depressing… like **20 Manda** to recruit"; "I just spent **800 Manda** and got 1 3☆" — **sentiment, not a price claim** |
| `1179899` Farming a 4\* from the Fight Club, 2019.07.09 | `20201029161158` | 92,136 | `adf00ae582a0e363` | "**160 traces per copy**, and you need **7 copies to max transcendence**"; "a **year and a bit** to t3 one 4\* hunter"; "it should be **750 Chips** if comparing 3★ traces which is **375 chips**, and for Mirage **150 frags for 3★ traces and 300 frags for random 4★ traces**"; "I get to **30+ fights a day** … I can only farm **400-800 chips a day**" |
| `1035027` [Guild] ProGuild, 20+ captains, 2018.11.23 | `20200812235350` | 82,626 / 81,475 | `57803e4767ac74b6` / `cc7ec34d8b5e5663` | "Reward will be sent after Dec 7th. So expect to have **50k rupee** amd some veteran ticket." |
| `21480` Metron event problems??, 2017.05.21 | `20180306173557` | 68,139 | `06928ccec42b42c7` | "**rupee is hard to get**, i tried spamming stage 10 yesterday but only got **2 rupee tickets**" |
| `75145` 4th passive, 2017.07.04 | reply-rich | 80,666 | — | "lantern and rebbeca's 4th passive skills don't always happen, whereas on **lapis there is 100% chance**" |
| `111831` Team buffs question. | `20191022010617` | 29,665 | `44e89489b76e35e4` | "**do team buffs add up?** … I have a hunter that increases **10% HP** and then … another … maybe not maxed, like **+9% HP**. Is the final result a **+19% HP** or it's considered only the one with the highest percentage?" — **question, no answer in either arm** |

## 3.14 ★ "Zero HTML tables" is refined, not overturned — and it has a cause

| corpus | posts | `<table>` count | body+reply chars |
|---|---:|---:|---:|
| pass 1 | 154 | **0** | 142,091 |
| pass 2 latest-capture arm | 538 | **0** | 387,401 |
| pass 2 reply-rich arm | 2,750 | **2** (both in `422653`) | 1,795,847 |
| pass 2 reply top-up arm | 120 | **0** | 84,942 |
| **combined pass 2** | **~3,400** | **2** | **2,268,190** |

**The corrected statement: this board almost never uses HTML tables — 2 `<table>`
elements in ~3,400 posts — but the one time it did, it did so to hold a complete
44-row dataset.** So pass 1's `<table>` screen was the wrong instrument: `149251`'s
transcendence ladder and `421776`'s category table are both **plain lines**, and
`422653` used a table only because it had 44 × 3 columns plus a 7 × 4 cross-tab.

**The correct screen is numerator density plus a topic keyword**, which is what
`tools/forum-en-pass2-analyse.py` applies on top of the table count: 117 of 3,036
reply-rich captures carry at least one numeric unit line, 262 hit the
gacha/rate screen, 106 the economy-cost screen, 23 the equipment-stat screen. The
recoveries in §3.1–§3.13 are what survives manual reading of those.

---

# 4. THE THREE OPEN QUESTIONS

## 4.1 ★★ Q1 — "does transcendence compound or scale from base?" — **ANSWERED, favouring from-base**

As posed in [`t1-measured-1.0994-2026-10-08.md`](t1-measured-1.0994-2026-10-08.md) §2:

| model | rule | T1 | T2 | T3 |
|---|---|---:|---:|---:|
| **(A) compounding** | each rank-up multiplies the *current* value | 1.0994 | **1.2087** | 1.3287 |
| **(B) from base** | each level multiplies the *base* value | 1.0994 | **1.2000** | 1.3000 |

T1 is measured at **1.0994 ± 0.0012** from an in-game receipt screen.
**Three threads in this corpus decide it.**

### Evidence 1 — the rule, stated in words, twice

**`682748`** `Info on Transcendence.` · Vladimiro · **2018.04.17 16:39** ·
capture `web/20200806154523` · 84,511 B ·
`6addaae09f4a271736645b3a2eec66412613e925a4a0c6df1dc747c030ff27e4`

> **The time you transcend is completely irrelevant. The stat boost is a fixed
> amount for each hunter**, the reason the difference is so high is because Kain
> (for some reason) has a higher power rating.

restated as rule 2 of the same reply: *"2. The time you transcend is completely
irrelevant."*

**`394240`** `Transcendence` · LordFarquad · **2018.02.16 08:59** ·
capture `web/20201024152856` · 80,281 B ·
`1d43c189731882408af0a0b2010549e068ac53bfa2f4914ad8d72105a8f06bb0`

Body asks *"Does it matter what level is your fodder for transcendence?"*; three
independent replies answer:

> **Nope, no difference. You're better off foddering lvl 1 hunters for transcendence**
> I dont believe that it matter
> It doesnt matter. Use lvl 1.

**"a fixed amount" is the from-base rule in words.** Compounding would be "a fixed
*percentage of the current value*", and three separate players describing the
system all report a fixed increment.

### Evidence 2 — the discriminating number

**`421630`** `Does Transcendence/raw stat numbers affect skill?` · **Wongy** ·
**2018.02.22 15:24** · capture `web/20201029045852` · 82,822 B (latest arm) /
86,289 B (reply-rich arm) · `21449770b2efd0adf7a466c071696953407077c9d9a32bddf8d22b90fad46726`

> **Transcending a character is confirmed to power up healing and damaging
> skills. I noted akasha heals increase by 9% from T1 to T2.**

and, same thread, on the per-level question:

> It seems that there is a slight influence to skills. **You can notice your
> skill numbers slowly increasing as you level a hunter.**

### The arithmetic that separates them

| | T1 | T2 | T1→T2 increment | how a player would report it |
|---|---:|---:|---:|---|
| **(A) compounding** | 1.0994 | 1.2087 | **+9.94 %** | "**10 %**" (or "9.9 %") |
| **(B) from base** | 1.0994 | 1.2000 | **+9.15 %** | "**9 %**" (or "9.2 %") |
| **observed (`421630`)** | — | — | reported as **9 %** | — |

Observed **+9 %**. (B) rounds to 9; (A) rounds to **10**. Using the brief's ladder
figures the residuals are 0.15 pp vs 0.94 pp — a **6× smaller residual for (B)**.
Using T1 = 1.0994 exactly: T2(B) = 1.19835 vs observed-implied 1.19835
(Δ ≈ 0.0000); T2(A) = 1.20859 (Δ ≈ 0.0102).

### Verdict, and exactly how far it can be pushed

**Three threads spanning 2018-02-16 → 2018-04-17 — two stating the rule, one
supplying the discriminating number — converge on model (B) "from base".**
`AGENTS.md` may now treat the rungs as **≈1.0994 / 1.2000 / 1.3000** as the
working model. Note (B)'s T3 = 1.3000 is exactly Hermes' measured T3 of
×1.30000, which was already `t1-measured` §2's best argument for (B).

**Four limits, stated plainly, because this is player testimony and not a
measurement:**

1. **It is not the game's own receipt.** `t1-measured` §2 asks for "any T2 panel"
   with a 0.139 % internal spread. **`421630` is a heal value on one hunter,
   rounded by its author to a whole percent.** One heal reading cannot resolve a
   0.73 % gap on a three-stat panel.
2. **The sources are not fully independent.** All are ordinary members of the same
   2018 English board; no cross-posting is shown.
3. **"fixed amount" is loose phrasing.** If "amount" means "percentage points", it
   is exactly (B). If a player meant "fixed fraction", it is ambiguous.
4. **The third rung is untested.** (B) gives T3 = 1.3000; Riko's measured 1.274
   would be 2 % low, which `t1-measured` §2 already flags.

**What would still settle it:** one in-game T2 stat panel. This lane's
contribution is that the *hypothesis space has narrowed to one model* and the
search should now look for confirmation-or-refutation of **(B)** rather than for
either.

## 4.2 Q2 — per-level growth: **still open, and the blocker is now attributable**

**Defensible bound from the project:** per-level ≤ **1.013851** (`t1-measured`
§6.2). No stated per-level rule exists in this corpus, after a corpus that is
**99.9 % mined**.

| finding | why it is not a per-level rule |
|---|---|
| `682748`: Kain **lv24 / T2 / skill 30** = 20 059 power; Hermes **lv30 / T2 / skill 47** = 18 941 power | two points, **power not stats**, and the two differ in level *and* skill level *and* hunter. Power is a known non-linear composite. |
| `421630`: "you can notice your **skill numbers slowly increasing as you level**" | "a slight influence", and about **skills**, not the base panel. Qualitative. |
| `886704`: Yuri **T1 = 19k** power → **T2 = 21k** power, "with **50% crit chance**" | one hero, one step, power not stats. Ratio 1.105 — note this is *far* above the 1.013851 per-level bound and must be a rank/tier step, not a level step. |
| `1244661`: **Robin T3 at "lvl 8" = 14 000 power** | the level is the commenter's inference (*"probably no skills and no jewels"*). |
| `639004`, "hunter max stats" — the thread's own conclusion | **"One can't have a precise number of any characters because"** … level, three transcendences, fates and collection bonuses must all be unlocked first, "and unless one's a whale, one cannot create a final number". **A community-wide statement that per-level growth was never publicly isolated.** |
| `421776` / `422653` | not a per-level quantity |

**Honest position: unchanged, but now a *documented* negative rather than an
unfinished search.** A per-level rule would have to come from an in-game panel at
two levels with everything else held — and §3.6 gives the reason that panel cannot
provide it: *"that's really the full stats you get from added Dorm bonus, Jewels
and Equips altogether."*

## 4.3 Q3 — equipment stat values: **still open; the negative is now attributable and quantified**

`accessory-stat-hunt-2026-10-06.md` records the prior state: every other avenue is
exhausted, accessories are **structurally closed**, and the game shipped no monster
stat screen.

**Pass 2 tested that negative against a corpus that had never been read — 99.9 %
of the board — and quantified exactly what it does and does not contain.**

What pass 2 recovered on equipment and jewels, in full:

| kind | example | value |
|---|---|---|
| **costs** | `1425687` | 100 k rupees green→blue + 59 type mats; >250 k rupees lv40→50; 20–30 adv toolboxes/level from ~46 |
| **costs** | `888621` | 22 k rupees for one jewel swap; 160 k → 90 k for one jewel to level 9; polishing = half price |
| **main stat at a level** | `1199014` | 3★ triangle jewel, attack **+19 at level 12** |
| **per-jewel contribution** | `1361746` | 2 crit jewels → **+6 %** (≈3 % each); 4 fatal jewels → **+60 %** (≈15 % each) |
| **per-jewel contribution** | `1386397` | 6 block jewels → **+20 %** block (≈3.33 % each) |
| **substat magnitude** | `1143988` | "perfect **54** Atk & Def substats" |
| **gem semantics** | `1143988` | regen jewels → out-of-battle passive regen; Bear's in-battle regen scales with **defence** jewels; Robin's with **offence** jewels |
| **slot/shape structure** | `1361746` | six slots, shapes Triangle / Square / Diamond |
| **slot threshold question** | `1207789` | **asked, never answered in any capture** |

**Still missing, and it is the same single thing: an equipment or jewel item's own
stat value at a stated level / rarity / grade.** Every row above is a cost, a slot
count, a derived-stat contribution, or a player's judgement.

**And three posts that should have been the answer and were not** — this is the
part worth publishing:

- **`259238` `Equipment and Weapon System`** — the single most on-topic title in
  the corpus — is a **feature wishlist**, and its four replies are also a wishlist
  (*"I want to kill my enemies with candy-weapons"*, *"Would definitely love to see
  holiday themed skins"*). Verbatim body: *"just wanna know - what do you all
  expect to see in the weapon upgrade system? I personally would love to see more
  customization options and possibly some skins"* (capture `web/20190717103553`,
  78,503 B, `07d458bbb1d2c876`).
- **`1425687` `Equipment Advancement Questions`** asked the three questions
  outright and got an answer about **cost**, not stats.
- **`12355` `Equipment?`** (2017.05.17) is a single line — *"Hopefully we get to use
  that soon!"* — and its one reply is a complaint about feature overload.

**Conclusion: the accessory negative is confirmed against a 99.9 %-mined corpus
and it is now attributable.** It is not that this board lacks equipment
discussion — 21 titles match an equipment/jewel screen, and the densest thread
(`888621`) is entirely about jewel costs. **It is that players reported what
jewels *cost* and what they *did*, never what a jewel *was worth*, because the
value was only ever visible inside the client** — and §3.6 supplies the
player-side statement of why that is so: the in-game `!` panel is pre-contaminated
by jewels and equipment.

**Accessory coverage stays 1/100.** No weak evidence was allowed to move it, and
the two `1361746`/`1386397` per-jewel contributions are explicitly **candidates,
not recovered values**, because neither states a jewel rarity or level.

---

# 5. STRUCTURE WITHOUT NUMBERS — brief, because it is not this lane's currency

| post | date | author / views | content |
|---|---|---|---|
| `395817` Secrets a Top PvP player won't let you know. | 2018.02.16 | Nishino, 742 views | **16 numbered rules** of a top-10 weekly ladder: stall rotations, AI rage timing, elemental counters, why T1 loses to T3 |
| `484911` v2.0 Who to 5\* next? | 2018.03.05 | Fukurama, 407 views | 5-hero priority list + a worked PvP kill sequence against Hermes |
| `495055` "Who To 5 Star Next?" Supplementary Info | 2018.03.07 | FatherVinh, 728 views | "based on the current meta in the top 100 ranked players"; **"A 5\* hermes with no transcendence is stronger than a 4\* hermes with full transcendence"** |
| `1361746` Can anyone explaine the difference? | 2020.05.07 | V1NCENT, **5,003 views** | jewel→stat mapping, slot shapes, crit/element/reduction mechanics (§3.6) |
| `1160203` Unbeatable Geranium stall combo | 2019.05.31 | thesurgeon, 216 views | a **15-reply Mirage floor-250 clear**, rage-4.20 timing, left-slot targeting, full role matrix |
| `1161731` The ultimate disappointment in 2 pics | 2019.06.02 | — | *"It will add another two 'horns' to the side of it when transcended again. Ones in the image are only **T1**"* — a visible T1-vs-T2 art difference |
| `1078741` hmmm xD | 2018.12.23 | 37 replies | the highest reply density on the board after `272` |
| `1103717` F2P T3 HARLEY | 2019.01.31 | — | titled **F2P T3 HARLEY**, "9 months" in the replies |
| `716763` Question regarding FC teams | 2018.04.29 | Kappersnapper | team-passive arithmetic: **+30 % max HP, +30 % DEF, +20 % block** from 2 tanks + 3 healers |
| `1192644` I didn't understand why... | 2019.08.01 | — | *"thinking about t3 one (just one) nature 4\* with selective ticket, we still need 7x months"* |

These are **identity, ordering and process evidence**. They are not counted toward
any coverage counter.

---

# 6. HARD NEGATIVES, each with its control

| # | negative | control that makes it interpretable |
|---|---|---|
| **N1** | **HTML tables are essentially absent: 2 in ~3,400 posts / 2.27 M characters** (pass 1: 0/154). | pass-1 baseline reproduced byte-for-byte (76,603 body / 65,488 reply chars). **Cause identified and the claim refined** (§3.14): this board writes data as plain lines, so the count is not a measure of data density — and the 2 tables it does have hold a complete 44-row dataset. |
| **N2** | **Accessory/equipment item stat values: still none.** | 21 equipment/jewel-titled posts screened; the densest thread (`888621`) read in full and is about costs; the three most on-topic titles (`259238`, `1425687`, `12355`) read in full and contain a wishlist, a cost answer and one line respectively. Coverage stays 1/100. |
| **N3** | **No stated per-level growth rule**, across a 99.9 %-mined board. | `639004`'s thread states in its own words that a max-stat number cannot be isolated; `1361746` states why the in-game panel cannot supply one (§4.2). A documented negative, not an unfinished search. |
| **N4** | **188/188 pass-1 attachment URLs are 404; pass 2 spent ZERO requests on attachments** on the strength of that. 1,489 of 3,036 reply-rich captures carry rewritten `im_` URLs, which per the guard file are not evidence. | control from pass 1: no `ffd8ff` / `89504e47` / `47494638` signature in any of the 188. |
| **N5** | **Four questions whose answers did not survive in any captured form**, fetched in **both** arms at different timestamps and URL forms: `1207789` (2nd gem-slot level), `358733` (can a transcendence be skipped and taken later), `111831` (do team buffs add), and — **corrected from an earlier draft of this note** — `394240` turned out **not** to be in this set: its reply-rich arm carries 4 replies including the answer, and it is used as evidence in §4.1. | both arms parsed for each; a body-only capture with 0 comments is recorded as *not in the archive*, not as *not asked*. `1207789` is additionally flagged `usable=False / near-empty-text` by the validity gate in **both** arms. |
| **N6** | **3 census ids unmined: `249711`, `1092022`, `1092070`.** | **Not a budget limit.** All three appear in the census with `statuses: ["302"]` and no other capture — the archive holds only redirects. The corpus is effectively 100 % mined. |
| **N7** | **The census is 27 of 28 CDX pages**, so 3,193 is itself a floor and the true board is larger. | Stated as a floor in §2.2, not as a count. |
| **N8** | **Wayback served "You do not have permission to access." as an HTTP 200 with real bytes for 39 ids**, plus 4 DB-error pages and 3 login-error pages; and 5 ids returned a genuine HTTP 404. | All counted and excluded by the validity gate (§1.6); every one is visible in `_ledger2.tsv` with its status, so a reader can see exactly which posts to distrust and which are absent. |
| **N9** | **The `1480939` awakening explanation contradicts itself** (§3.7). | Both statements quoted verbatim and left unreconciled; the observed −70/−70/−150 delta is reported separately from the prose. |
| **N10** | **`1486407` "New Building Idea, Alchemy!" reads like a data source and is not one.** Its "1 Sparkling Heart … 250,000 Rupees" and a dozen other costs are the poster's own invented feature proposal. | Quoted only as a proposal. No alchemy cost is recorded as game data anywhere in this note. |

---

# 7. WHAT WAS SEARCHED AND NOT FOUND

- **Per-level growth rule.** Searched: titles (`stat change`, `max stats`,
  `level`, `exp`, `Awakening`), then body text with
  `per level|each level|every level|level +1|+\d+% per`, then the numeric-line
  screen. Not found (§4.2).
- **Equipment/jewel item stat rows.** Searched: 21 titles, then every capture
  containing `+N %` / `+N hp|atk|def` / `armour|weapon|jewel|gem … N`. Recovered
  costs, slot counts, per-jewel contributions and gem semantics — no item stat row
  (§4.3).
- **Any `[Notice]` with numbers**, beyond pass 1's. `master` / `natara` / `VSpang`
  posts were ranked up by a +40 author bonus; the top vendor item in the queue is
  `40930`, which carries no numeric statement. The one **new** vendor finding of
  pass 2 is `123417` (§3.3).
- **A second post by `149251`'s author giving the natural 2★ column
  authoritatively.** The 7/25/60 set exists but is a reader's, not the guide
  author's (§3.1).
- **Absolute stat panels.** Not sought as such, because §3.6 gives a stated reason
  why the in-game panel cannot provide one. This is the one place where pass 2
  changed the *plan* rather than the *result*.
- **Attachment pixels.** Not attempted; see N4.

---

# 8. TOOLING ADDED, and reproduction

All new tools are `GET`-only readers against `http://web.archive.org`.
**`http://` only** — `https://` is refused on this host (`WinError 10061`).

| tool | purpose |
|---|---|
| `tools/forum-en-pass2-listq.py` | builds the list-page queue from the on-disk census; **no CDX query** |
| `tools/forum-en-fetch-concurrent.py` *(pass 1, unchanged)* | the harness whose per-target session defeated pass 2; kept for comparison |
| `tools/forum-en-pass2-fetch.py` | fetcher with a **per-thread shared session**, control gate, `000`-never-a-result ledger, resumability, `--deadline-min` budget |
| `tools/forum-en-pass2-parselist.py` | board-list parser; quote-aware attributes; records the anchor behind every field |
| `tools/forum-en-pass2-bodyq.py` | ranks unread ids by topic weight × reply count × views, with vendor and adjacency bonuses; two capture policies |
| `tools/forum-en-pass2-analyse.py` | provenance ledger (bytes + sha256), table/digit screens, body-text question screens, validity gate |
| `tools/forum-en-pass2-provenance.py` | joins queue + ledger + on-disk bytes into a provenance TSV (3,182 rows written) |

```
python tools/forum-en-pass2-parselist.py  --dir recovered-assets/forum-en-2026-10-05/pass2/get-list \
                                          --out recovered-assets/forum-en-2026-10-05/pass2/list-index.json
python tools/forum-en-pass2-bodyq.py      --census recovered-assets/forum-en-2026-10-05/census \
                                          --listindex .../pass2/list-index.json \
                                          --parsed1 .../get-body/parsed.json \
                                          --out .../pass2/queue-arm-replyrich.tsv --limit 3100 \
                                          --capture-policy reply-rich
python tools/forum-en-pass2-fetch.py      --queue .../pass2/queue-run2.tsv \
                                          --outdir .../pass2 --ledger .../pass2/_ledger2.tsv \
                                          --workers 3 --tries 4 --sleep 1.5 --deadline-min 40
python tools/forum-en-pass2-analyse.py    --dir .../pass2 --glob "body/*.html" \
                                          --out .../pass2/analysis-arm-replyrich.json
python tools/forum-en-pass2-provenance.py --root .../pass2 --queues .../queue-arm-replyrich.tsv \
                                          --out .../pass2/provenance-all.tsv
```

`--workers` was held at **3** throughout, per the guard entry that archive.org
refuses at 8. Nothing was written outside `analysis/` and
`recovered-assets/forum-en-2026-10-05/pass2/`.

**Two broken instruments recorded, because both produced plausible wrong output:**

1. A first version of `forum-en-pass2-analyse.py` re-wrapped `sys.stdout.buffer`
   while `tools/forum-en-parse.py` — which it loads **by path**, because the hyphen
   in that filename blocks a normal import — had already installed its own
   `TextIOWrapper`. The first wrapper was garbage-collected and **closed the shared
   buffer**, giving `ValueError: I/O operation on closed file` on the first print.
2. `forum-en-pass2-parselist.py`'s first quote-aware attribute pattern excluded `=`
   outside quotes, so it could not match `href="…"` at all; and its first fix
   matched `document_srl` *outside* the quoted `href`, which is unsatisfiable
   because the id lives **inside** it. Symptom in both cases: `with title: 0`.

---

# 9. A CONCURRENT-AGENT NOTE, because it changes how the timings above read

During this pass, `Win32_Process` showed a second agent running
`analysis/research/base-stats-visual-hunt/t2-hunt-2026-10-08/fetchimgs.py` and
`priority.py`, i.e. **another lane hitting the same archive in this same
workspace**. An orphaned fetch process from this lane's own first attempt (the
one-hour foreground run the harness timed out on, whose child survived) was
competing with it; that orphan was stopped, and **no process belonging to the other
agent was touched**.

Two consequences worth publishing:

1. **The first list-page batch's apparent stall (3 targets in 35 minutes) was
   contention plus a 6-try/120 s-timeout retry cost, not the archive.** Once the
   orphan was gone and sessions were reused, the same archive delivered
   **3,238 × 200 out of 3,243 attempts in 20.1 minutes with zero transport
   failures.**
2. **Both lanes are competing for one rate limit**, so §1.3's throughput figures
   should be read as *"achievable while sharing with one other active fetcher"*,
   **not** as an archive capacity measurement. A future pass should assume a lower
   ceiling.

---

# 10. HONEST BOTTOM LINE

This was the largest untouched corpus in the project. It is now **99.91 % mined**
(3,190 of 3,193 English post ids), and the 3 that remain have **no content capture
in the archive at all** — only HTTP 302 redirects — so the corpus is effectively
finished. **2,268,190 characters** were read, 16× pass 1, and five complete
original numeric tables were recovered that nothing in the project had:

| table | post | rows | closes exactly? |
|---|---|---|---|
| per-hunter trace rates | `422653` | 44 + a 3×7 cross-tab | **yes** — 4,208 traces and 99.999 %, every % = traces/4208 |
| trace category rates | `421776` | 9 rows | **yes** — three partitions each to 100.000 % |
| transcendence cost ladder | `149251` | 6 rows, 2 grades (+1 in replies) | **yes** — ×100 and ×10 identities hold in all rungs |
| 4★ gacha drop-rate ladder | `1162563` | 4 rungs, vendor-sourced | internally consistent; the per-hunter increment is derived |
| awakening cost + roster | `1480939` | 1 cost + 9 heroes | single source; prose contradicts itself |

Plus one **[VENDOR-AUTHORED] mechanic** (`123417`: block chance stacks
additively; high block reduces crit chance *and* crit damage), the elemental cycle
in full (`20587`), and the player-side explanation of why in-game base stats are
unreadable (`1361746`: the `!` panel is pre-contaminated by jewels and equipment).

The three questions: **Q1 is answered** — three threads, two stating the rule and
one supplying the discriminating number, converging on the **from-base** model
(§4.1); that narrows the search but does not replace the missing in-game T2 panel.
**Q2 and Q3 remain open**, and both are now *documented negatives against a
99.9 %-mined corpus* rather than unfinished searches: this board reported what
equipment and jewels **cost**, what they **did**, and how much they **contributed
to a derived stat**, and never what a jewel **was worth**.

Coverage counters unmoved: **heroes 1/113 (0.9 %), accessories 1/100 (1.0 %),
monsters 0/22.** Nothing above was allowed to move them. §3.10's power readings
were explicitly excluded because `t1-measured` §3 proved power is not linear in
the three core stats, and §3.6's per-jewel contributions are labelled candidates
rather than recovered values because neither states a jewel rarity or level.

**The largest block of unmined material in this project no longer exists.** What
remains open is narrow and named: one in-game T2 stat panel for Q1, and — per
§3.6 — a *gear-stripped* read of the hero panel, which may not be obtainable from
this corpus at all.

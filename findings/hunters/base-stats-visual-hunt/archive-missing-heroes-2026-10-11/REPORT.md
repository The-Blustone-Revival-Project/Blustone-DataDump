# Archive missing-heroes recheck (2026-10-11)

Targeted recheck for the 19 heroes named in `hero-archetype-guesstimate-2026-10-11.md` §4
(Geranium, Teresa, Mary, Selene, Alia, Anemone, Audrey, Sofia, Leon, Bella, Junia,
Blondie, Westfield, Monica, Lottery Mouse, Clara, Katrina, Themis, Estelle —
catalog IDs `064, 065, 066, 068, 070, 071, 072, 073, 074, 075, 076, 077, 080, 081,
084, 089, 090, 092, 096`), none of which has a row in `archived-hunter-database-2019.tsv`.

**Result: 0 numeric 基本能力値 rows recovered. All 19 remain without an archive row.
No tier is promoted. `coverage.md` was not edited.**

Note on scope wording: the task brief calls these "19 tier-C heroes (all ★4
Bomber/Support)". The current `hero-at-draw-estimates-2026-10-11.tsv` (v2, after the
scripted-episode second method) places 8 of the 19 in tier B and only 9 of the 17
current tier-C rows overlap this list. This lane rechecked the §4 19 as instructed,
regardless of tier label drift. Roles/rarities above are from
`catalog/legacy-catalogue-data/card-catalogue.tsv` (the 19 span Bomber, Support,
Offense, and Defense — not only Bomber/Support).

## Derivation-method discrepancy (stated, not hidden)

The brief says to derive profile URLs "from index + Japanese titles in
`card-catalogue.tsv` and `uncovered-archive-roster-2019.tsv`". Both files carry
**English titles only** — neither contains a Japanese epithet, so no profile URL
can be constructed from them. The authoritative derivation was instead the
closed-set enumeration: any published `blustone.jp/hunter/*` profile URL must appear
in the Wayback CDX census of that namespace. That census (HTTP 200, 163 urlkeys)
contains exactly **63** profile-base URLs, and all 63 resolve to the pre-`064`
roster (4 diffs vs the TSV are pure URL-slug/encoding variants of the same 4
heroes: Balian, Halloween Lantern, Locke, Sunny — see `title-diff.txt`). Japanese
name cores for the 19 (katakana transliterations; Geranium ゼラニウム confirmed
against the JA namu mirror snippet 遺物コレクターゼラニウム, remainder standard
transliterations with variants where ambiguous) were then searched against the full
63-title set locally (exact substring, `local-fragment-check.txt`: **0 hits**) and,
where the network allowed, via per-hero CDX `filter=original:` queries (ALL
captures, no collapse).

## Queries issued (one shared Session + jitter throughout)

| # | Query | Params | Outcome |
|---|---|---|---|
| 1 | `blustone.jp/hunter/*` wildcard census | `collapse=urlkey`, `filter=statuscode:200`, 200-only | HTTP 200, **163 urlkeys**, 63 profile-base (first try 503-throttled, retry 200; throttle body preserved, never used as evidence) |
| 2 | rarity-index exact CDX, all captures | no collapse | HTTP 200, **exactly 2 captures ever**: `20191015065805`, `20191209130354` |
| 3 | Dec-2019 index fetch, `id_` raw | `20191209130354id_` | HTTP 200, 77,085 B, genuine (253 hunter hrefs); **63 profile titles, identical set to Oct/census** (`index-diff.txt`: 0/0) |
| 4 | `blustone.jp/hunter/*` from 2020 | `collapse=urlkey`, `from=2020` | HTTP 200, **`[]`** — no 2020+ captures (controlled negative) |
| 5 | per-hero filters, 19 heroes × EN + JP cores | no collapse, `limit=50` | 10 HTTP-200 empties (`[]`); remainder HTTP 503 (11,832-B throttle page) / one 504 — all transport, **never recorded as content negatives** (`per-hero-cdx-summary.json`, `retry-summary.json`) |

Positive control per batch (all PASSED, bodies saved):
batch 1/2 — Beckhen `20191216060610id_`, 35,832 B, contains 基本能力値 + `8709` + `1678`;
batch 3 — Crocus `20191115010135id_` (Nov alternate-timestamp path), 35,374 B,
contains 基本能力値 + `8535`, proving Nov captures are fetchable by this pipeline.

Body validation: error shells excluded by signature (throttle page 11,832 B / 503,
504 len-160 body, empty `[]`); genuine pages verified by length + 基本能力値 +
expected combat-power token. No 429 was observed; 503/504 episodes are logged as
instrument limits.

## Crosswalk (all 19 → catalog, all negative)

See `missing-heroes-recheck.tsv` (19 rows, one per hero): catalog ID, EN name, role,
rarity, element, JP core used, closed-census hit (`no` for all 19), filter-CDX
outcome (`empty` / `partial-empty` / `transport-limited`), numeric rows (`no` for
all 19). No verbatim stat table exists to transcribe; the transcript section is
therefore empty by evidence, not by omission.

## Conclusion

- Pages checked: full `blustone.jp/hunter/*` namespace (163 urlkeys), both index
  captures (Oct + Dec 2019), 2020+ namespace (empty), 19 heroes × name-core
  (local exact: 0/19; network filters: 10 empties, rest transport-limited).
- Rows recovered: **0**. Remaining: **19/19** (Geranium, Teresa, Mary, Selene,
  Alia, Anemone, Audrey, Sofia, Leon, Bella, Junia, Blondie, Westfield, Monica,
  Lottery Mouse, Clara, Katrina, Themis, Estelle).
- The "even one ★4 Bomber/Support row promotes a whole tier" trigger did not fire.
- Files: `REPORT.md` (this), `missing-heroes-recheck.tsv`, `cdx-*.json/txt`,
  `control-*.html`, `index-20191209130354.html`, `profile-titles.txt`,
  `title-diff.txt`, `index-diff.txt`, `local-fragment-check.txt`,
  `per-hero-cdx-summary.json`, `retry-summary.json`, scripts `recheck*.py`/`probe*.py`.
  All work stayed inside `archive-missing-heroes-2026-10-11/`.

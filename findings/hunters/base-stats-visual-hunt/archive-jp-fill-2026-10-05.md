# Archive JP fill lane — 2026-10-05

Lane: exhaust the Wayback `blustone.jp/hunter` rarity index (63 profile links),
alternate 2019 captures, GameAppCH gallery (20 images), 4Gamer gallery (8 images),
GameApps.hk (6 images), FreeGame Mugen rank-up page. Target: the 51 IDs in
`uncovered-archive-roster-2019.tsv` with no numeric 2019-archive row.

## Result up front: 0 new rows. The 2019 archive is a proven closed set.

No `.tsv` append was made: there is nothing provenance-clean to append.
Existing 62 numeric rows are untouched.

## Archive URLs checked this lane

1. Oct 2019 rarity index (re-fetched, full body):
   `https://web.archive.org/web/20191015065805/https://blustone.jp/hunter/%E3%83%AC%E3%82%A2%E3%83%AA%E3%83%86%E3%82%A3%E5%88%A5`
   — 63 profile links: 6 draw-★4 + 34 draw-★3 + 11 draw-★2 + 12 draw-★1.
   The `★5ハンター一覧` section heading renders with an **empty table**: no ★5 /
   awakened profile page was linked in Oct 2019.
2. Dec 2019 re-capture of the same index:
   `https://web.archive.org/web/20191209130354/...` (CDX confirms these are the
   only two 200-captures of the index URL). Link set is **identical**: same 63
   Japanese-title links, same ★-banding, ★5 section still empty. No late-2019
   hunter additions (no Geranium/Teresa/Mary/…/Katrina/Estelle pages).
3. Full Wayback CDX enumeration (collapse=urlkey, status 200, returned complete
   under limit=200):
   `http://web.archive.org/cdx/search/cdx?url=blustone.jp/hunter/*&...`
   — every profile URL is one of the known 63 Japanese-title links. All other
   hits are image/attachment sub-routes (`/becken`, `/becken-s`, `/varian`,
   `/xenovia-s`, …) or site chrome (`/hunter`, `/menu-c-attribute`,
   `/menu-c-type`, `/hunterguild`, type/attribute facets). **No profile URL
   exists for any catalog ID 064–098, any awakened `_1` variant, or any
   2020-dated hunter page.** Latest profile captures are Dec 2019.
4. Genovia (`056`) recapture check: CDX shows a single 200-capture of the
   profile URL (`20191216052325`), already harvested as `???` placeholders in
   the TSV (`non-numeric-core-stats`). No alternate numeric capture exists.
5. FreeGame Mugen listing (re-fetched live 2026-10-05):
   `https://freegame-mugen.jp/spapp/game_6433.html` — 7 images (character, town,
   battle, skill, clear/item, **rank-up**, story). The rank-up frame is the
   already-logged `7,092 → 11,277` generic Middle→Advanced Hunter panel
   (identity/field/rank/gear unresolved; polluted track only). No missing-ID
   stat panel; no new row.
6. GameAppCH (20 images), 4Gamer (8 images), GameApps.hk (6 images): prior
   lanes completed full visual review of every frame (see `coverage.md` rows).
   Findings stand — generic rank-up `1,417 → 2,389`, enemy-bar tokens, promo/
   guild/battle art, unnamed portraits as identity-only leads. No frame shows
   an attributable 13-field profile table for any of the 51 missing IDs, so no
   re-harvest was performed here; reopening all 34 frames would duplicate
   verified coverage rows without new values.

## Title / rank / role / element crosswalk (Dec 2019 index vs TSV)

The Dec index re-confirms the TSV crosswalk for all 62 covered IDs: Japanese
epithet + draw-★ band + 属性 (火炎/冷気/電撃) + タイプ (攻撃手/守備手/爆撃手/
ヘルパー) match the TSV `role_ja` / `element_ja` / `rarity_on_draw` on every
row spot-checked (★4 band: 063/052/056/046/047/010; ★1 band includes both
Tyltyl rows 026/004 and Sylvester 006). No level or equipped-state text appears
on any index or profile page — the level/gear-unknown verdict stands, and all
62 rows stay OUT of strict coverage (polluted/rebalance anchors only).

## Still-missing 51 IDs — disposition

- **15 awakened variants** (`004_1`, `005_1`, `009_1`, `010_1`, `011_1`,
  `017_1`, `019_1`, `020_1`, `021_1`, `024_1`, `026_1`, `034_1`, `038_1`,
  `056_1`, `086_1`): unfillable from this archive **by design**. Profiles
  document draw-state hunters only; the empty ★5 index section plus the CDX
  URL census prove no awakened profile page was ever published there. Do not
  derive awakened rows by scaling base rows (LEVELING.jet rank tables are the
  monster-rank multiplier per the calibration limit, not a hero curve).
- **35 base IDs `064`–`098`** (Geranium through Selene-Valentine): post-2019
  roster. No archive page exists (CDX census + identical Dec index). These need
  non-archive visual sources (post-2019 videos, screenshots, community DBs).
- **`056` Genovia base**: page exists, single capture, renders `???`
  placeholders; already in TSV as `non-numeric-core-stats`. No numeric
  alternate capture exists.

## Level/gear context: unresolved everywhere

No index, profile, gallery, or listing page checked in this lane prints a hero
level or states equipped vs associated gear. The strict-coverage gate (level +
rank/awakening + documented equipment state) is therefore still met only by
`051` (1/113). This lane adds no coverage credit and no polluted-ledger entry
(the Mugen rank-up panel was already logged).

## Follow-up pointers (not worked here)

- Post-2019 hero IDs (064–098) postdate the blustone.jp archive; search 2020+
  video/screenshot sources, not further Wayback hunter-index passes.
- Awakened `_1` rows need leveled/equipped awakening screenshots with visible
  gear state; archive profiles can never supply them.

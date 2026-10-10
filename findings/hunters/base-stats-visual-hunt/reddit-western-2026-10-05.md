# Western-community gallery lane — 2026-10-05

**Lane:** Reddit r/Blustone galleries, Discord archives, Facebook groups,
AppStorio, Uptodown, mob.org, BrowserCam, Aptoide, PDALIFE.
**Method limit:** this pass used text/markdown fetches plus the search tool.
No in-app-browser pixel inspection was available in this lane, so no gallery
image was re-viewed at the pixel level here. Findings below are (a) a
consolidation of the already-recorded visual audits in `README.md` /
`coverage.md` / `polluted-observations.md`, and (b) new text-level leads that
do not need pixels.

## Galleries re-checked (status from prior pixel audits, unchanged)

| Gallery | Prior audit state | This pass |
|---|---|---|
| Old Bluestone Screenshots (13 images, `1vyddln`) | All 13 visually inspected: Katrina `090` Lv.30 tuple (Strength 38,842 / HP 3,846 / ATK 2,913 / DEF 1,757, gear unknown); Lawrence `079` DEF 20.0%/+1.0%; Leon Summer `094` HP 13.0%/+1.0%; Offense/Defense Strength lists (`98/105`) | No re-view; Reddit text fetch blocked. No new numeric panel reported in thread metadata. Known rows preserved, not double-counted. |
| Unlock gallery (8 images, `1mcmqfz`) + `awesome8679` Lapis comment | 8/8 inspected: six recruit cards (Estelle, Themis, Harley, Monica, Lottery Mouse, Vincent — identity/role/element only, no stats); 2 wallpapers identity-uncertain. Comment image: Awakened Lapis likely `017_1`, Lv.30/30, 53,046 / 4,501 / 2,382 / 1,789, gear unknown | No change. |
| `fluger69` memorial galleries (3 posts, 57 images: 20/20/17) | All navigated; readable `See Details` pages identify 31 named/variant catalog entries (see `reddit-memorial-galleries.md`); no numeric panel in readable frames; some part-3 frames stayed blurred/loading | No change. Blurred part-3 frames remain the only uninspected pixels in this set. |
| AppStorio (`blustone.appstor.io`, v2.8.0.1) | iPhone 1–2 rendered (battle montage, village — no stats); iPhone/iPad 3: Hunter List `19/102` + 14 unlabeled values; iPhone/iPad 4: advancement `3,014 → 4,407`. Bear (`036`) medium-confidence portrait match at `14,749` | Listing re-fetched 2026-10-05: same 4 iPhone + 4 iPad screenshot slots, no new images. Confirms no gallery growth. |
| Uptodown (6 images) | All 6 inspected: enemy-bar tokens `276` (img 2), `351 ×2` (img 6); story portraits `???` identity-only | No change. |
| mob.org (4 images) | All 4 inspected: promo art repeat, skill animation, battle HUD; no stat panel | No change. Duplicate of 4Gamer/GameApps art. |
| BrowserCam (3 images, v2.0.5.1) | All 3 inspected: promo art, battle montage, fishing; no stats | No change. |
| Aptoide (12 images, v2.8.0.1) | All 12 inspected: hub, battle HUD, promo/recruit art; no stat panel | No change. |
| PDALIFE (11 images, v1.1.9.4) | All 11 inspected: HUD tokens `3188`, `3264`, unattributed | No change. |
| Discord archives | Clan-Discord material is the stated provenance of the 13-image Reddit post; no separate Discord archive with new panels was located in this pass | Negative result. |
| Facebook (`BlustoneEN`) | Search surfaced character-introduction videos (e.g. Judith the Red Shadow) and event/recruitment notices | Promo/intro format; no stat-panel evidence. Kept as identity-art leads only, no values inferred. |

## New lead (text-level, no pixels needed)

**Namu Striker role page** (`en.namu.wiki/w/블루스톤/헌터/공격수`, last modified
2026-08-20) publishes concrete numeric skill-effect magnitudes for the Fight
Club Guardian chicken (**Baek Hen — same character as catalog `051` Beckhen**,
transliteration variant; role page also confirms its Fight-Chip acquisition):

- special skill damage `~9046`
- attack-speed buff `~20.00%`
- self damage-immunity `every 3 seconds`, duration `0.51–1.00 seconds`
  (1 second at max level; page notes a historical nerf from a longer duration)
- defense-reduction effect `~30.00%`
- Fight-Club-only block-chance effect `~30.00%`

These are **skill/effect modifiers, not hero HP/ATK/DEF** — same evidence class
as the preserved Crocus `Necromancer's Might` entry. Recorded in
`polluted-observations.md` under the related-skill-modifier section; **zero
base-stat coverage credit**. The page also links one YouTube skill video per
listed Striker (Lapis, Sylvester, Balian, Rebecca, Scar, Mowgli, Beckhen,
Hermes, Octavia, Glass, Heidi, Karl Steiner, Natalia, …) — these are
uninspected video leads for future visual sampling, not evidence.

The same page confirms two official `bs.visualshower.com` character-intro posts
(Heidi `document_srl=707457`, Lily & Lala `document_srl=426682`) exist as linked
sources; direct access to that host has previously failed, so they remain
unresolved leads.

## Identity-only portrait index (no new IDs assigned)

- Bear (`036`) ↔ `C036.jet`: medium-confidence matches in Naver `55/114` list
  (`12,213` token) and AppStorio `19/102` list (`14,749` token). Numbers remain
  unassigned rating tokens.
- Beckhen/Baek Hen (`051`): Namu Striker page art/video links match the Fight
  Club chicken; no new portrait mapping beyond the existing `C051.jet` crosswalk.
- Unlock-gallery recruit cards give exact name/title → catalog matches for
  `096`/`092`/`046`/`081`/`084`/`010` (role/element labels only).
- Uptodown story portraits (`???` man in red/black coat; cat-eared woman with
  pale beast) and Bilibili preview figures stay unidentified.

## Coverage disposition

- **New base-stat tuples: 0.** Strict hero coverage stays **1/113**;
  monster coverage stays **0/22**.
- **New polluted rows: 1 skill-modifier group** (Beckhen/Baek Hen five effect
  magnitudes, text-sourced). The four known gear-ambiguous tuples (Katrina
  `090`, Awakened Lapis `017_1`, Vincent `010_1`, FAQ image-8 anonymous) are
  preserved untouched; nothing was double-counted.
- **Files updated:** this lane log (new); `polluted-observations.md` (one
  appended skill-modifier subsection).
- No server/APK changes.

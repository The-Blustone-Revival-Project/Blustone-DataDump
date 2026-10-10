# Polluted monster HUD observations

**Purpose:** Preserve visible monster-side combat numbers from public Blustone
gameplay images and videos when the monster identity, max-HP state, difficulty,
or other context is not strong enough to count as base statistics. These
observations are a separate evidence track and never count toward the 70%
monster coverage target.

Do not treat a current battle bar as maximum HP. Keep each frame tied to its
timestamp and source; do not merge values across fights or infer a monster ID
from appearance alone.

## P J — “Blustone: Giants' Shelter 46–50”

- **Source:** [YouTube video](https://www.youtube.com/watch?v=Ot72M6h4OUI),
  uploaded 2017-05-16; 11:21 vertical gameplay. Local visual locators are
  `Ot72M6h4OUI-contact-1.jpg`, `Ot72M6h4OUI-contact-2.jpg`, and
  `Ot72M6h4OUI-contact-3.jpg` in this folder. Contact sheets sample frames at
  15-second intervals.
- **~01:15:** Contact sheet 1 shows a red enemy bar with the token **2,551**.
  The sprite is a small orange/yellow spiky-looking enemy; no catalog monster ID
  is visible.
- **~01:30:** Contact sheet 1 shows a red enemy bar with the token **1,253**.
  The battle continues in a visually similar scene, but this is not enough to
  prove that the bar belongs to the same enemy instance.
- **Transcription correction:** The earlier README entry said `2,031` at
  ~01:15. Rechecking the saved contact sheet supports `2,551`; `2,031` is
  superseded as a likely misread and is not retained as a second game value.
- **Confidence:** High for the two legible bar tokens in the saved frames;
  medium for the timestamp-to-frame association; low/unknown for monster
  identity and whether either number is max HP.
- **Unknown:** Monster ID, species, level/rank, stage sub-wave, difficulty,
  initial/full HP, ATK, DEF, and whether the ~01:15 and ~01:30 bars track the
  same target.
- **Status:** Polluted current-bar observations only. No base-stat tuple and no
  monster coverage credit.

### Full contact-sheet re-transcription (2026-10-05 lane)

- **Method:** All three saved contact sheets re-read frame by frame
  (15 s sampling, t=15 s…t=675 s). The two tokens above re-verified legible.
  **Fourteen further enemy-bar tokens** surfaced; all are current-bar
  readings with unknown identity and unproven max HP:

| Frame | Bar token | Bar state / scene note |
|---|---|---|
| t=105 s | **8** | Bar nearly empty/dark; near-kill current reading |
| t=195 s | **2,858** | Red bar, mid-fight |
| t=210 s | **1,556** | Red bar, mid-fight |
| t=285 s | **4,217** | Full-length red bar, mid-fight |
| t=300 s | **3,316** | Dark wave-transition scene |
| t=315 s | **1,757** | Red bar, mid-fight |
| t=390 s | **4,373** | Red bar, mid-fight |
| t=405 s | **3,126** | Red bar, mid-fight |
| t=420 s | **1,376** | Red bar, mid-fight |
| t=435 s | **134** | Dark transition frame; token near bar area |
| t=525 s | **5,321** | Full-length red bar, mid-fight |
| t=540 s | **3,682** | Red bar, mid-fight |
| t=645 s | **6,042** | Full-length red bar; largest token observed |
| t=675 s | **2,685** | Dark boss-backdrop scene |

- **Context frames (bound interpretation, no numeric stat):** t=120 s map
  `거인의 쉼터` nodes 41–50, progress `37/60`; t=450 s same map, `16/60`
  (second pass — do not merge enemy pools across passes); t=555 s zone dialog
  `north garden of mid guard / the 5th zone` with Korean retry text
  (defeat/retreat screen); t=585 s `탐험 지역` map `10/60`; t=60 s / t=660 s
  skill cinematic of a brown-haired man in a red coat (likely Captain
  cut-in, identity unconfirmed, no numbers). Wave dots sit atop most battle
  frames but are not mapped per token. Floating hit numerals (17–48) are raw
  per-hit damage, not enemy stats. Enemy sprites vary across frames
  (orange/yellow spiky, red blob, blue spiky, dark boss); appearance alone
  maps to no `M001`–`M021`/`M100` ID.
- **Confidence:** High that the tokens sit in enemy-bar regions; medium for
  frame→timestamp association; low/unknown for identity, sub-wave,
  difficulty, and full-vs-current HP. Full-length bars are still current-HP
  displays until a full-to-empty sequence for one identified enemy is shown.
- **Status:** Polluted current-bar observations only. No coverage credit.

## スマホゲームCH — Blustone review screenshot battle frames

- **Source:** [スマホゲームCH review](https://gameappch.com/app/?app=04374), published 2017-05-18; images 5–6, 7–8, and 19–20 of its 20-image gallery were visually checked in the in-app browser on 2026-10-05. The screenshots are promotional/site-reviewed gameplay captures, not a continuous single recording.
- **Image 5–6 pair:** The right battle frame shows a red enemy bar with the token **372**.
- **Image 7–8 pair:** The right battle frame shows a red enemy bar with the token **1,250**.
- **Image 19–20 pair:** The left battle frame shows a red enemy bar with the token **704**.
- **Confidence:** High that the three digits are legible and associated with red enemy bars; low that each is current HP, and unknown for monster identity or full/max HP.
- **Unknown:** Monster IDs/species, level/rank, stage/difficulty, whether any displayed bar is at full health, ATK, and DEF.
- **Status:** Polluted HUD tokens only. No monster base tuple and no coverage credit.

## Uptodown — Blustone 2 snowy battle screenshots

- **Source:** [Uptodown Blustone 2 listing](https://blustone-2.en.uptodown.com/android), gallery screenshots 2, 3, and 6; all six gallery frames were opened in the full-size overlay on 2026-10-05. The listing advertises version 2.8.0.1, but the capture build is not independently visible.
- **Image 2:** A red enemy health-bar graphic contains the raw token **276**; floating red **18** and white **7** also appear elsewhere in the battle area. The latter two are not assigned stat semantics.
- **Image 3:** A small snowfield enemy is opposite the player; floating raw tokens **19** (red) and **6** (white) appear, with no legible numeric health-bar label.
- **Image 6:** A large blue/white snowy enemy appears with a yellow/orange bar containing **351** and an adjacent **×2** marker; a red **19** also appears nearby. No relation between the marker and the bar value is established.
- **Confidence:** High that `276` and `351`/`×2` are visible in the respective bar areas; low for what either number means. Floating `18`, `19`, `7`, and `6` are raw combat tokens only.
- **Unknown:** Monster IDs/species, levels, wave/difficulty, exact game build, whether the bar numbers are current HP or another value, maximum HP, ATK, and DEF. The small enemy's appearance is insufficient to map it to `M001`.
- **Status:** Polluted HUD evidence only. No monster base tuple and no coverage credit.

## PDALIFE — Blustone v1.1.9.4 archived screenshots

- **Source:** [PDALIFE Blustone v1.1.9.4](https://pdalife.com/blustone-android-a30585.html),
  screenshots 2 and 4 of 11 (transcribed from the `coverage.md` observation
  ledger on 2026-10-05; pixels not re-opened in the HUD lane).
- **Screenshot 2:** Token **3188** on a red enemy bar.
- **Screenshot 4:** Token **3264** with overlapping combat damage.
- **Unknown:** Monster identity, full/max HP, ATK, DEF, and whether either
  token is a current or maximum value.
- **Status:** Ambiguous HUD tokens only. No monster base tuple and no coverage
  credit.

## VisualShower official Blustone 2 promo — battle token

- **Source:** [VisualShower Corp. Blustone 2 promo](https://www.youtube.com/watch?v=i7IChnEylvk),
  ~00:18 (transcribed from the `coverage.md` observation ledger on 2026-10-05;
  frame not re-opened in the HUD lane).
- **Token:** Top bar visibly reads **34,408 ×2**; actor, meaning,
  current-vs-maximum semantics, and monster ID are unresolved.
- **Status:** Ambiguous battle token only. No monster base tuple and no
  coverage credit.

## Candidate depletion runs (2026-10-05 full-HP lane)

- **Method:** Lane agent directly re-read all three saved P J contact sheets
  (`Ot72M6h4OUI-contact-1/2/3.jpg`). All 16 prior bar tokens re-verified
  legible at their frames; **no new numeric tokens** surfaced. Sampling is
  15 s, so no wave continuity between frames is provable and no frame shows a
  monster name or `M`-ID. Each run is a candidate only, never max-HP proof.
- **Run A (strongest), t=390 s → 405 s → 420 s → 435 s: 4,373 → 3,126 → 1,376
  → 134.** Same icy backdrop, same brown-rifleman frontline, same red
  spiky/blob enemy across the first three frames; consistent ~26/hit floating
  damage. t=390's bar renders full-length and t=330 shows an empty field, so
  the enemy is plausibly near-full — plausibility, not proof. The t=435 frame
  goes dark with a different-looking blue spiky enemy, breaking same-instance
  continuity at the tail.
- **Run B, t=195 s → 210 s: 2,858 → 1,556.** Same darker-ice backdrop,
  rifleman frontline, green/yellow spiky enemy; decreasing bar with the same
  continuity and identity caveats.
- **Run C, t=90 s → 105 s: 1,253 → 8.** Same backdrop/frontline with a small
  fire enemy; t=105 is a near-kill current reading. Kill frame and any
  inter-sample wave hand-off unobserved.
- **Negative results:** No boss intro/name card in any of the 45 sampled
  frames. 6,042 (t=645) → 2,685 (t=675) is explicitly NOT one enemy (backdrop,
  party, and enemy all change across a skill cinematic). 5,321 (t=525) →
  3,682 (t=540) changes the frontline hunter, breaking same-instance
  continuity. Wave dots are illegible at contact-sheet resolution.
- **Status:** Polluted current-bar candidates only. No coverage credit.

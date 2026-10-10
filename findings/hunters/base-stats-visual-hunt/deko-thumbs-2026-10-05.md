# Deko Boko `[Blustone] special move` thumbnail sampling — 2026-10-05

Closes the queue in `official-skill-frames-2026-10-05.md` §5 item 1 (the 21
`striker-videos-2026-10-05.md` cinematics). Method follows
`bahamut-thumb-2026-10-05.md` §4: `curl.exe` + local pixel read, because
`i.ytimg.com` serves `image/jpeg` and the fetch tool reports that as an
unsupported content type (itself proof the URL is live).

## Result up front

- **New strict base-stat rows: 0.** Heroes stay **1/113**, monsters **0/22**,
  accessories **1/100**. `coverage.md` untouched.
- **Train/detail background answer, identical for all 20 available videos:
  NO.** Across **61 pixel-inspected frames** from 20 videos, **not one** showed a
  Train / hunter-detail / stat panel. The series is a *branding + battle* format,
  not a stat tour.
- **All 20 available videos are 2018 uploads ⇒ PRE-2019-09-05 rebalance era**
  (per `stat-version-context.md` / AGENTS §77). This is a hard era tag on every
  token in §2.
- **No full playback.** No decoder was obtained in this lane either. Every claim
  is from **single frames**. Nothing is claimed about what happens between them.

---

# 1. PURE — thumbnail inventory and Train-background answers

## 1.1 Method (reproducible)

```text
curl.exe -o <name>-<variant>.jpg https://i.ytimg.com/vi/<id>/<variant>.jpg
variants: hqdefault sddefault maxresdefault hq1 hq2 hq3
era:      curl.exe -A "<UA>" https://www.youtube.com/watch?v=<id>
          -> "uploadDate":"..." JSON field
```

- **126 requests** (21 ids × 6 variants). **120 × HTTP 200 `image/jpeg`**,
  **6 × HTTP 404** — all six belonging to video 20 alone.
- `maxresdefault` is a **true 1280×720 for all 20** available videos
  (85,776–156,423 B). This had to be checked per video: the Geranium Short in
  the prior lane returned a **1,097-byte placeholder** at `maxresdefault`, so
  "hires available" is not a safe assumption across videos.
- **61 frames pixel-inspected.** The per-video breakdown is the `Frames` column of
  §1.3 and sums to exactly 61 (video 20 = 0). Local copies were kept in the
  session temp directory only; this lane writes **one file** and no image assets.
- Image **dimensions were verified** (1280×720 on all 20) before pixel reads,
  so no frame was upscaled from a small variant.

## 1.2 The series template (the actual structural finding)

The same **two-panel layout** appears in all 20 videos. It is a *branded
montage template*, and it is the reason the answer to "is there a Train
background?" is a flat no:

| Panel | Content | Is it a stat panel? |
|---|---|---|
| **Left** (≈46% width) | The character illustration composited over a **blurred, warmly-lit interior** (hearth/fireplace at left, timber beams, orange key light). `BLUSTONE / A BEYOND THE BOUNDS STORY` logo bottom-left. | **NO** — pure art + logo. No chrome, no `Lv.`, no HP/ATK/DEF, no comparison arrows, no buttons. |
| **Right** (≈54% width) | One of four frame types, below. | Only the BATTLE type carries numbers, and they are transient HUD values. |

The blurred interior backdrop is the **same plate in all 20 videos** — a template
asset, not a per-character location.

**Four observed frame types:**

- **CARD** — logo on near-black over a **chibi** version of the character playing
  the skill animation. `Deko Boko GAMES` watermark bottom-right. (The
  `maxresdefault` poster is almost always this type.)
- **TITLE** — the hero's **English name in large white diagonal type** across
  the illustration; left panel reduces to the logo alone on black. *This is the
  single most valuable frame type in the set — see §2.3.*
- **SPLASH** — same character right of frame against a **white field with an
  orange/yellow burst**. Pure VFX, zero numbers.
- **BATTLE** — **real in-game footage** (letterboxed): enemy bars, damage
  numbers, the corner counters, and the `ULTRA!!!` control.

**A methodological trap, recorded so it is not repeated:** the left panel is
**not reliably the same subject as the right panel**. In video 08, `hq1`/`hq3`
show the rabbit-helmeted man on the left while `hq2` shows a **rooster** there.
Video 07's left panel is a **chicken** in every sampled frame. *The left panel
must never be used as identity evidence.*

## 1.3 Per-video inventory and Train-background answer

Columns: frames = how many were pixel-inspected. `Train/detail bg?` is **NO for
every row**. Catalog IDs are carried from `striker-videos-2026-10-05.md` /
Namu — **none was inferred from pixels**.

| # | Video / id | Namu label → catalog ID | Uploaded | Frames | Frame types seen | Left panel subject | `Train`/detail bg? |
|---|---|---|---|---|---|---|---|
| 1 | `e2BfzFPN6iA` | Rapid Swordsman Lapis → `017` | 2018-03-16 | 4 | CARD, CARD-crop, BATTLE ×2 | purple twin-tail cat-eared woman, katana, ice crystal | **NO** |
| 2 | `xGR7leUs8Ds` | Sylvester, the Old Soldier → `006` | 2018-03-13 | 4 | CARD, crop, SPLASH, BATTLE | white-haired bearded elder, goggles, cannon+hose+tank | **NO** |
| 3 | `qjOf4PlRhGk` | Wandering Swordsman Balian → `019` | 2018-03-10 | 4 | CARD, **TITLE**, SPLASH, BATTLE | teal hair, cat ears, red eyes, fur-collar coat, sheathed sword, tail | **NO** |
| 4 | `1tyX54FdEGg` | Twilight Bat Rebecca → `021` | 2018-03-03 | 3 | CARD, BATTLE ×2 | pink hair, red hood, bat wings, skull necklace, studded bat | **NO** |
| 5 | `kpj_mGkl2jQ` | Wandering Fighter Scar → **unmapped** | 2018-03-03 | 3 | CARD, **TITLE**, BATTLE | white/silver hair, red eyes, mechanical gauntlet w/ blue orb, open jacket | **NO** |
| 6 | `eVBF9JNP5QY` | Mowgli in the Lost Forest → `002` | 2018-03-03 | 3 | CARD, BATTLE, SPLASH | silver spiky hair, red eyes, black fur collar, bare chest, bandaged arms, tooth pendant | **NO** |
| 7 | `1jaL-JeSGQY` | Fight Club Guardian Baek Hen → `051` | 2018-05-31 | 5 | CARD ×2, BATTLE ×2, SPLASH | **a white chicken on a perch** ⚠ see §2.4 | **NO** |
| 8 | `loLuPDdXziQ` | Super Messenger Hermes → `023` | 2018-03-03 | 3 | **TITLE**, SPLASH, BATTLE | rabbit-helmet man, red/white jacket ⚠ rooster in `hq2` | **NO** |
| 9 | `EQh8jaaqGQg` | Cold Witch Octavia → **unmapped** | 2018-03-03 | 3 | CARD, BATTLE, SPLASH | black hair, cat ears, green eyes, black corset, white fur stole w/ ice crystals, ice staff | **NO** |
| 10 | `Qt6zvRBNceU` | Santa Girl Rebecca → **unmapped** | 2018-03-03 | 2 | SPLASH, BATTLE | pink hair, Santa hat, green bow, candy-cane staff, **white wings** | **NO** |
| 11 | `jxzybH_qWLI` | Santa Closter → `042` | 2018-12-26 | 3 | BATTLE ×2, SPLASH | muscular white-haired man, sunglasses, red Santa coat, fur trim | **NO** |
| 12 | `6cjXXG7-IwI` | Silver fairy Glass (Yuri) → **unmapped** | 2018-03-17 | 2 | BATTLE ×2 | black hair in buns, long rabbit ears, blue dress | **NO** |
| 13 | `3U4raHWZuf4` | Heidi, the girl with two faces → `044` | 2018-05-02 | 2 | SPLASH, BATTLE | pink hair, long rabbit ears, white flower crown, red eyes, white plush rabbit | **NO** |
| 14 | `Y0-fHjIdUfY` | Chichi, girl of superpowers → **unmapped** | 2018-12-31 | 3 | SPLASH, BATTLE ×2 | brown hair, bear-ear hood, purple/pink hoodie w/ bear patches, holding a red apple | **NO** |
| 15 | `AmnMCc7DpFI` | Immortal Karl Steiner → `012` | 2018-03-03 | 3 | **TITLE**, SPLASH ×2 | dark hair, wolf ears, teal eyes, white wolf companion | **NO** |
| 16 | `T18oAIUT1n4` | Wolf child Baboon (Bibi) → **unmapped** | 2018-03-03 | 3 | BATTLE ×2, SPLASH | dark skin, **red horns**, green eyes, large curved blade | **NO** |
| 17 | `1NTa5ZwqIpg` | Noble spear Natalia → `037` | 2018-03-03 | 2 | SPLASH, BATTLE | silver-lavender hair, cat ears, blue eyes, trident, grey coat | **NO** |
| 18 | `6ERMUxex4E8` | Unidentified twins Lily & Lala → `047` | 2018-04-08 | 3 | BATTLE ×2, SPLASH | **twins**: red-eyed w/ red-streaked white hair + blue-eyed w/ blue-streaked white hair, white fur-trimmed outfits, rabbit ears | **NO** |
| 19 | `Qhu6YaT2ttM` | Renegade Vincent (video 1) → `010` | 2018-05-02 | 3 | **TITLE**, SPLASH, BATTLE | grey hair, red eyes, purple high-collar coat/hood | **NO** |
| 20 | `s4-OmmRZJDM` | Renegade Vincent (video 2) → `010` | **unknown** | **0** | — | — | **n/a — unavailable, §1.4** |
| 21 | `ey2PRYPsme8` | Blade Wind / Kalbaram → **unmapped** | 2018-08-07 | 3 | BATTLE ×2, SPLASH | horned/winged-helmet samurai, gold-black armour | **NO** |

**Era:** every dated row is **2018-03-03 → 2018-12-31**, i.e. entirely
**PRE-rebalance**. No post-2019-09-05 frame exists in this set. Two clusters:
a **2018-03-03 mass upload** of nine videos (identical `04:13:52–53 -08:00`
timestamp), then singles through 2018-12-31.

**Inventory coherence check (passes):** all 20 subjects appear in Namu's
공격수 / **Attacker** roster for this Striker page — consistent with
`striker-videos-2026-10-05.md` being sourced from the Striker page. No video
shows a Defender, Bomber or Support character.

## 1.4 Video 20 (`s4-OmmRZJDM`) — genuinely unavailable

Three independent negatives agree:

- **all six thumbnail variants HTTP 404**, each a 1,097-byte error JPEG;
- **oEmbed HTTP 403** (already recorded in `striker-videos-2026-10-05.md`);
- the **watch page** returns title `"Sign in"` with **no `uploadDate`**.

**Wayback CDX is non-diagnostic and is not cited as evidence.** A control query
for a *known-live* thumbnail (`i.ytimg.com/vi/eqh8jaaqgq/*`, video 09, HTTP 200
this lane) **also returned empty**, so CDX is simply not indexing
`i.ytimg.com` here. Empty CDX output proves nothing about video 20.

Video 20's catalog subject (Vincent, second cinematic) is already covered for
portrait purposes by video 19, so **no coverage is lost**. It stays an open
lead; no date is invented for it.

---

# 2. UNPURE — quarantined tokens and corroborations

**Nothing in this section counts toward coverage.** Every number is a transient
battle-HUD value on an unidentified enemy and an unidentified build, or an
identity/portrait reading whose field meaning is unproved. **Do not subtract,
normalise, or map any of it onto a catalog row.**

## 2.1 The purple-icon integer next to the `ULTRA!!!` control — and why it is NOT a base stat

This is the most interesting token in the set, and it yields a **useful
negative**. Every BATTLE frame shows a small **purple square icon with an
integer**, immediately left of / above the `ULTRA!!!` bar:

| Video | Character label | Integer | Frames |
|---|---|---|---|
| 01 | Lapis | `130` | 2 |
| 02 | Sylvester | `128` | 1 |
| 03 | Balian | `125` | 1 |
| 04 | Rebecca | **`133`** | 2 |
| 05 | Scar | `125` | 1 |
| 06 | Mowgli | `129` | 1 |
| 08 | Hermes | `125` | 1 |
| 09 | Octavia | `125` | 1 |
| 10 | **Rebecca (Santa Girl)** | **`125`** | 1 |
| 12 | Yuri | `131` | 2 |
| 13 | Heidi | `190` | 1 |
| 16 | Bibi | `125` | 2 |
| 17 | Natalia | `125` | 1 |
| 18 | Lily & Lyla | `128` | 2 |
| 19 | Vincent | `190` | 1 |
| 07, 11, 14, 15, 21 | — | not observed in sampled frames | 0 |

**The control that kills the base-stat reading:** videos **04** and **10** are
the **same character in two costumes** — base Rebecca (`021`) reads `133`,
Santa-costume Rebecca reads `125`. A per-character base stat cannot change with
a costume. Two further arguments in the same direction:

- **`125` is the modal value** (7 of 15 observations) — implausible for a
  per-character identity;
- **Heidi and Vincent both read `190`** — two unrelated characters sharing a
  value.

**Reading:** an unproved transient scalar — plausibly a computed/buffed attack
value, a skill-power figure, or a gauge count. **Field meaning unproved;
deliberately not guessed.** Per AGENTS.md the ULTRA/Rage mechanic is real
(measured SP rate `0.01`/s, max `10`; skill costs 3–4 Rage), which is why a
`125`–`190` reading is *not* SP — but that only rules SP out, it does not
identify the field. Recorded as a **rebalance-era HUD token only.**

## 2.2 Other quarantined HUD tokens

**Corner counters (top-left of the battle panel):** a green icon with a small
integer, and a coin icon with an integer.
Green: `0` (videos 01, 06, 11, 12, 13, 14, 18, 19, 21) or `1` (02, 03, 04, 05,
07, 08, 09, 15, 17) or `2` (10). Coin: `0`, `1`, `6`, `7`, `9`, `12`, `13`,
`15`, `16`, `17`, `20`, `24`, `28`, `35`, `39`, `42`. Within a video the coin
value sometimes rises (04: `9`→`15`; 14: `9`→`12`; 18: `13`→`16`) and sometimes
falls (01: `20`→`16`). **Semantics unproved** — a wave/stage counter and a
score or currency are both consistent with the observations. Not a stat.

**Damage numbers** (transient, on unidentified enemies; enemy identity and
max-HP context unknown in every case):

- 01: `256`, `139` · 04: `22`, `9`, `26`, `83` / `82`, `299`, `237`
- 05: `23`, **`1320`** · 06: `15` · 07: `45` · 10: `3`, `3`
- 18: `164`, `61`, `84`, `85` · 21: `160`, `145` / `126`, `231`

**Combo counters** `×3` (06) and `×4` (18) — transient chain counts.

**Red kanji attack-name overlays** (e.g. 斬) — VFX glyphs, not values.

**`ULTRA!!!`** — a control label present in every BATTLE frame. Mechanic string.

**Unread artifact, video 13 `hq3`:** an **opaque white rectangle** sits over the
coin-counter position. Cause unknown (in-video redaction, render artifact, or a
UI element). Flagged, **not** read as a value.

**Enemies are unidentified throughout.** Observed: an orange fox-like head, a
brown mound, a blue penguin/shark, a small blue shark, a white blob, a brown
reindeer, a blue bird, a white chicken. **No enemy reaches monster-identity
status and none contributes to the 0/22 monster count.**

## 2.3 On-screen name corroborations (the strongest class here)

Five videos carry a **TITLE** frame with the hero's English name rendered in the
video itself. This is **textual** corroboration, materially stronger than the
prior lane's portrait-level art matches:

| Video | On-screen text | Namu page label | Match |
|---|---|---|---|
| 03 | `Wandering Fighter`-style split, `Balian` | Wandering Swordsman Balian | **exact** |
| 05 | **`Wandering Fighter Scar`** | Wandering Fighter Scar | **exact** |
| 08 | **`Elite Messenger Hermes`** | Super Messenger Hermes | translation variant |
| 15 | **`Immortal One Karl Steiner`** | Immortal Karl Steiner | epithet variant, name exact |
| 19 | **`Renegade Vincent`** | Renegade Vincent | **exact** |

Two further consistencies worth keeping:

- **Video 04 vs 10** — same face, hair and **bat wings**, different costume,
  independently confirming Namu's distinction between 레베카 (Rebecca `021`) and
  산타걸 레베카 (Santa Girl Rebecca). Namu left the Santa variant unmapped and it
  **stays unmapped**.
- Every subject appears in Namu's **공격수 (Attacker)** list for the Striker
  page — the inventory is internally coherent.

**No catalog ID is asserted from any pixel.** The ID column in §1.3 is
inherited from `striker-videos-2026-10-05.md` and prior crosswalks; the
unmapped rows (Scar, Octavia, Santa Rebecca, Yuri, Chichi, Bibi, Windblade)
**remain unmapped.**

## 2.4 Unresolved anomaly — video 07 (Beckhen `051`)

Video 07's left panel is a **white chicken with a red comb, perched on a stand**
in all five sampled frames, and the right panel's chibi is a **blonde, braided,
sunglasses-wearing figure with what appears to be a beard**, accompanied by a
small chicken and an ice splash. In video 08's `hq2` a **rooster** occupies the
left panel while the right panel is the rabbit-helmeted man.

Candidate explanations, **none established**: a costume/mascot/skin; a chibi
*mascot* form rather than the hunter; a mislabel; or a different character. The
"beard" is **low confidence** at these resolutions and may be a scarf or collar.

**This matters because `051` is the single hero with a verified base-stat row**
(the FAQ image 8 `24068 + 6291 = 30359` match). **Video 07 must therefore not be
used to characterise Beckhen's appearance or stats in either direction.** Flagged
for a future lane that can actually play the video.

## 2.5 What this lane could NOT do

- **No full playback.** No decoder (ffmpeg/cv2) was available, matching the
  prior lane's limitation. All 61 observations are **single frames**; nothing is
  claimed about transitions, animation timing, or frames between the 25/50/75%
  samples.
- **No result / victory / Train screen.** The `ULTRA!!!` BATTLE frames are the
  only in-game footage reached. No post-battle screen was sampled, so no
  post-combat panel was assessed.
- **The 2 recruitment videos** (`cnMBlXFd5W4`, `hnnxZmmPg0Q`) remain untouched
  from the prior queue — lowest priority, recruit-result art rather than panels.
- **Video 20** remains unavailable (§1.4).
- Because the series is a cinematic montage, **these videos are unlikely ever to
  yield base stats.** The correct next target for stat recovery is the
  equipment/gym-panel class already being worked in `base-stats-visual-hunt/`,
  not this series.

---

## 3. Coverage disposition

| Item | Result | Credit |
|---|---|---|
| Frames pixel-inspected | **61** across **20** videos (+1 video unavailable) | n/a |
| Videos with a **Train / detail / stat panel** | **0** | — |
| New HP/ATK/DEF base tuples | **0** | **none** |
| Purple-icon HUD integers (§2.1) | 15 readings, 5 heroes unmeasured | **none** — control disproves base-stat reading |
| Corner counters, damage numbers, combo counts | ~40 transient values | **none** |
| On-screen name corroborations | **5** textual (§2.3) | identity aid only, **no coverage** |
| Era | all **2018**, PRE-rebalance | era tag on everything |

**Strict coverage unchanged: heroes 1/113, monsters 0/22, accessories 1/100.**
`coverage.md` not modified. Impure rows appended to `polluted-observations.md`.
**No server, APK, seed, emulator, phone or Ghidra operation.**

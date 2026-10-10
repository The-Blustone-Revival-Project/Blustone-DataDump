# Miraheze gallery + Fandom retry + skill-video queue — 2026-10-05

Lane continuation of `post2019-roster-2026-10-05.md` (Miraheze 103 pages,
all sampled pages `[value]` placeholders, no HP/ATK/DEF field) and
`striker-videos-2026-10-05.md` (21 Deko Boko skill cinematics, metadata
only, never pixel-inspected).

## Result up front: 0 new strict rows. Hero coverage stays 1/113.

No nude/base HP/ATK/DEF tuple was recovered. All gallery holdings below
are sprite/emotion art with no numbers; all video links are uninspected
frame-sampling leads. Nothing here carries coverage credit, and no stat
is inferred from art.

## 1. Miraheze gallery subpages (fetched 2026-10-05)

- `Estelle/gallery`, `Katrina/gallery`, `Themis/gallery` — **do not
  exist** (HTTP 404; the parent pages render these as redlinks). The
  "uninspected gallery subpage" lead in the parent lane is closed for
  these three: there is nothing to inspect.
- `Lapis/gallery`
  (`https://blustone.miraheze.org/wiki/Lapis/gallery`, oldid=923,
  edited 2026-06-11) — **exists**. Sprites only, no numbers: base Lapis
  Idle/Sad, Angry, Joy, Shock, Etc; Lapis (Awakened) Idle. Note the
  Awakened parent page links here (not to a `Lapis_(Awakened)/gallery`,
  which 404s).
- `Geranium/gallery`
  (`https://blustone.miraheze.org/wiki/Geranium/gallery`, oldid=1458,
  edited 2026-08-22) — **exists**. Sprites only: base Geranium
  Idle/Angry/Joy/Sad/Shock, plus a second five-emotion set under the
  heading **Geranium (Valentine)**. No catalog ID is assigned here to
  the Valentine variant — do not map it to any catalog row or to
  Genovia (Valentine); it is an identity-only art lead.
- `Bella/gallery`
  (`https://blustone.miraheze.org/wiki/Bella/gallery`, oldid=1544,
  edited 2026-08-30) — **exists**. Sprites only: Idle/Angry/Joy/Sad/Shock.
- Verdict: Miraheze galleries are emotion-sprite sheets (Idle/Angry/Joy/
  Sad/Shock ± Etc). No gallery holds a stat panel, level, rank, or gear
  readout. Prior for stats from any remaining unopened gallery is ~nil,
  but only the four above plus Lapis were checked — do not claim all 103
  characters' galleries were audited.

## 2. Fandom retry via API (not page fetch)

Page fetch of `blustone.fandom.com/wiki/Katrina` returns HTTP 403, but the
wiki's own MediaWiki API answers normally, so the 403 is fetch-gating,
not proof of content:

- `api.php?action=query&prop=...&titles=Katrina` → page **missing**
  (negative result, not a transport failure).
- `api.php?action=query&list=allpages&aplimit=500` → the **entire wiki
  is 12 pages**: Attackers, BLUSTONE, BLUSTONE Wiki, Bombardier,
  `Charaters:Captain` (sic), Defender, Fire/Scissors, Helper, Ice/Rock,
  Main Page, Striker, Thunder/Paper. No per-hero pages exist at all.

Fandom therefore has no Katrina/Estelle/hero content to mirror; no text
mirror (Bing cache transport-errored, no working mirror needed) can
recover what was never written there. Fandom lane closed unless the wiki
gains pages. The role/mechanics stubs (Striker etc.) were not read — low
prior, stat-free by kind.

## 3. Official skill-video frame-sampling queue

Cataloged from Miraheze Gallery sections (links only, none played or
pixel-inspected). All are skill cinematics: sample frames for any
Train/detail background visible behind or around the cinematic, not for
the cinematic itself. Priority order per lane brief (detail-background
chance first):

1. **Themis** — `https://x.com/blustone_jp/status/1356527779781705728`
   (Feb 2021 post per ID timestamp;olevel detail unconfirmed). Linked
   from the Miraheze Themis Gallery section.
2. **Estelle** — `https://x.com/blustone_jp/status/1392041790094598147`
   (May 2021 post). Linked from the Miraheze Estelle Gallery section.
3. **Geranium** — `https://youtube.com/shorts/mFTmAXPz-dk` (Shorts
   format). Linked from the Miraheze Geranium Gallery section as
   "Ultimate skill video".
4. The 21 Deko Boko `[Blustone] special move` cinematics from
   `striker-videos-2026-10-05.md` (Lapis, Sylvester, Balian, Rebecca,
   Scar, Mowgli, Beckhen, Hermes, Octavia, Santa Rebecca/Clauster, Yuri,
   Heidi, Chichi, Karl Steiner, Bibi, Natalia, Lily & Lyla, Vincent ×2
   — one oEmbed-403 — Windblade) remain queued behind the three
   official links above; same background-check priority applies.
5. Recruitment videos (lowest priority — recruit-result art, not panels):
   GuitarRock First `20+ Hunters Recruiting! | Blustone 2`
   (`https://www.youtube.com/watch?v=cnMBlXFd5W4` — oEmbed 2026-10-05
   confirms title/author/channel `@GuitarRockFirst`, thumbnail at
   `i.ytimg.com/vi/cnMBlXFd5W4/hqdefault.jpg`); `블루스톤 헌터 섭외`
   (`https://www.youtube.com/watch?v=hnnxZmmPg0Q` — oEmbed HTTP 401,
   restricted/embedding-disabled or egress-gated, same 401 class as
   prior passes, not a removal signal; thumbnail URL pattern is the
   cheapest next pixel attempt).
6. Katrina has **no** video link on its Miraheze page; Bella has none
   either. Nothing queued for `090`/`075` video sampling.

x.com posts were not fetched (login/JS-gated); no stat panel is expected
in any of them. Do not cite a video as evidence until frames are
pixel-inspected.

## 4. New identity/mechanics context (text only, no numbers)

Parent pages re-fetched full-text 2026-10-05; skill magnitudes remain
`[value]` throughout. Preserved for era-tagging and matching only:

- **Geranium (`064`)** — Bomber/Lightning, male Human, 29 Mar 2019
  (pre-rebalance). Gear: Whip Sword / Black Uniform / Forbidden
  Suitcase. Active costs **4 Rage**, penetrates Immunity, DEF-weaken
  maintained until deactivation; follow-up bleed/regen-zero; 50%
  forced-switch-out + full stun; passives: team ATK% + team Armor
  Penetration. References Namu bomber section (matches striker-lane
  Namu prose class).
- **Themis (`092`)** — Bomber/Fire, female Human, 12 Jun 2020
  (post-rebalance). Gear: Monster Sniper Rifle / Reinforced Exoskeleton
  Suit / Large-Caliber Special Bullet. Active costs **4 Rage**,
  penetrates Immunity, ignores defense; follow-up bleed/regen-zero;
  40% bonus immunity-penetrating hit with Damage-Reduction debuff (no
  immunity/deactivation allowed); passives: team ATK%, team Elemental
  Enhancement + enemy Crit-Damage-Immunity null.
- **Bella (`075`)** — Offense/Ice, female Polar Bear, 30 Aug 2019
  (pre-rebalance). Gear: Sword Dance Swords / Dancing Clothes / Blue
  Skirt. Active costs **3 Rage** + self attack-speed buff; follow-ups:
  bleed/regen-zero, 30% self-immunity + stacking ATK/AS; passive:
  per-second enemy bleed, self immune to Attack Disable. References
  Namu attacker section. Complements the HungryApp Bella recruit art
  lead (no stats there either).
- **Katrina (`090`)** re-confirmed: Offense/Lightning, no release date,
  no gallery, no video. Complements the existing Lv.30 polluted panel
  (Strength 38,842; HP 3,846; ATK 2,913; DEF 1,757; gear unknown).
- Identity leads appended to `polluted-observations.md`; no stat
  inferred from any portrait, sprite, or equipment name.

## 5. Files updated

- This lane log (new).
- `polluted-observations.md` — appended gallery-audit + video-queue +
  Geranium/Themis/Bella identity context under the post-2019 section.
- `coverage.md` untouched (no count changes). No server/APK changes.

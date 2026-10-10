# Official skill-video frame sampling — 2026-10-05

Lane continuation of `miraheze-gallery-2026-10-05.md` §3 (three official
links queued: Themis x.com `1356527779781705728`, Estelle x.com
`1392041790094598147`, Geranium Short `mFTmAXPz-dk`).

## Result up front: 0 new strict rows. Hero coverage stays 1/113, monsters 0/22.

All three videos' poster thumbnails were pixel-inspected. Every frame is a
full-screen skill cut-in over a dimmed battle scene — **no Train/detail
background is visible behind or around any cinematic**. All visible numbers
are battle-HUD or cinematic tokens (damage popups ≠ base stats) and are
quarantined below, never counted. Full video playback was not performed (no
decoder in this lane); only poster/thumbnail frames were sampled.

## 1. Method (thumbnails first)

- `x.com` page fetch is login/JS-gated (Themis post returned only the login
  shell). Post text + media metadata recovered instead via the vxtwitter API
  (`https://api.vxtwitter.com/blustone_jp/status/<id>`), which returned full
  text, hashtags, dates, video file URLs, dimensions, durations, and
  `thumbnail_url` values. The Estelle `x.com` page itself also rendered text
  plus its video thumb, corroborating the API record.
- Thumbnails fetched directly and pixel-inspected:
  `pbs.twimg.com/ext_tw_video_thumb/<id>/pu/img/<hash>.jpg` (both x.com
  videos) and `i.ytimg.com/vi/mFTmAXPz-dk/{hq1,hq2,hq3,0,hqdefault}.jpg`
  (Short). `0.jpg` is byte-identical in size to `hqdefault.jpg` (9,565
  bytes — same image); `maxresdefault.jpg` returned 1,097 bytes, consistent
  with YouTube's no-hires placeholder, and was not pixel-inspected.

## 2. Themis — x.com `1356527779781705728` (Feb 2021, POST-rebalance)

- **Post text (vxtwitter API + page metadata):** `【ブルスト2キャラ紹介】`
  怪盗狙撃手 "テミス" / 職業：爆撃手 / ランク：★4 / 属性：火炎. Posted
  `Tue Feb 02 09:00:00 +0000 2021` (epoch 1612256400). Likes 1, 1 repost.
- **Video:** `video.twimg.com/ext_tw_video/1356176636538880001/pu/vid/638x1280/4Yw38OQtMjsSfkKN.mp4`,
  638×1280 portrait, duration 14,200 ms.
- **Thumbnail pixels** (`ZEUpIQAxqVl--gXL.jpg`, ~100 KB, inspected):
  silver-haired woman with blue eyes and a braid, white/black/red armored
  outfit, large red sniper rifle at left, red bullet held in a clawed
  gauntlet at right, red crystal shards and a dark horned beast silhouette
  behind. Bottom banner reads **"Armor-Piercing Ammunition"**. The art
  matches Miraheze Themis (`092`) gear (Monster Sniper Rifle) at
  portrait level — identity corroboration only, no ID inferred from pixels.
- **Background check:** full-screen cut-in; the battle behind is dimmed and
  unreadable except HUD tokens (next). No Train/detail/roster panel.
- **Quarantined HUD tokens (NOT stats):** top-left green icon `3`, gold
  coin icon `23`; dimmed enemy bar showing `2927` with `x2`; small chibi
  portrait bottom-right with a ~4-digit token reading approximately `1996`
  (low confidence, glare/dim). These are transient battle values on an
  unidentified enemy and an unknown build — damage/coin/counter semantics
  unproved. Never subtract, normalize, or map them to Themis.

## 3. Estelle — x.com `1392041790094598147` (May 2021, POST-rebalance)

- **Post text (x.com page render + vxtwitter API agree):**
  `【ブルスト2キャラ紹介】` ミッドガルド最強剣士 "エステル" / 職業：攻撃手 /
  ランク：★4 / 属性：火炎 ("私の辞書に、ツケという言葉はないの！").
  Posted `Tue May 11 09:00:00 +0000 2021` (epoch 1620723600). Likes 4,
  1 repost.
- **Video:** `video.twimg.com/ext_tw_video/1386581815205396483/pu/vid/640x1280/XpCUBwqWsJSM3Twn.mp4`,
  640×1280 portrait, duration 7,900 ms.
- **Thumbnail pixels** (`32wGC39YNPTNxrKu.jpg`, ~101 KB, inspected):
  red-haired fox-eared woman in white/red/black rapier outfit holding a
  thin sword, small blue owl and blue butterfly at her shoulder. Bottom
  banner reads **"Flash Stab"**. Portrait-level match to Miraheze Estelle
  (`096`, Offense/Fire, rapier) — corroboration only.
- **Background check:** full-screen cut-in over dimmed battle; no
  Train/detail/roster panel.
- **Quarantined HUD tokens (NOT stats):** top-left green icon `1`, gold
  coin icon `6`; right edge `x1` marker with a triple-slash icon. Transient
  battle counters, field meaning unproved.

## 4. Geranium — YouTube Short `mFTmAXPz-dk` (date UNKNOWN)

- **oEmbed metadata:** title **"the NEW ★4 Hunter Geranium!"**, author
  `VisualShower Corp.` (`@visualshower`), type video. No date or duration
  in oEmbed — era is unresolved; do not tag it pre/post-rebalance. The ★4
  in the title is a draw-rarity label for the Short's subject, not a
  base-stat context.
- **Thumbnail `hq2.jpg` (8,597 bytes, inspected):** dark-haired young man
  in red/black military coat with gold clasps and red tie; bottom banner
  reads **"Whip Sword Strike"**. Matches Miraheze Geranium (`064`) gear
  (Whip Sword) at portrait level — corroboration only. Top bar shows `64`
  with small icons (transient battle token, semantics unproved).
- **Thumbnails `hqdefault.jpg` / `0.jpg` / `hq1.jpg` (inspected):**
  same-frame family — closeup of the same man (red eyes) above an
  **"ULTRA!!!"** gauge bar, over a stage interior with double doors, a
  green sign (FIGHT-style lettering), and a red side sign. Bottom-left red
  circle shows `1`. No Train/detail panel; the `1` is an unproved battle
  token.
- **Thumbnail `hq3.jpg` (6,613 bytes, inspected):** **"VICTORY"** ribbon
  screen with a circular portrait, badge `38`, name token **"Pabian"**, a
  greyed middle button, and a pink **"Okay"** button. "Pabian" identity is
  unresolved (player nickname, hunter, or NPC — not established; no catalog
  row claims it). No HP/ATK/DEF on screen. Polluted victory-screen lead
  only.

## 5. What remains queued (not attempted in this lane)

- The 21 Deko Boko `[Blustone] special move` cinematics inventoried in
  `striker-videos-2026-10-05.md` — same thumbnail-first method applies.
- The 2 recruitment videos (GuitarRock First `cnMBlXFd5W4`, `hnnxZmmPg0Q`)
  — lowest priority (recruit-result art, not panels).
- Full-frame sampling of the three videos above (only posters inspected;
  no ffmpeg/cv2 decoder available in this lane's environment).

## 6. Files updated

- This lane log (new).
- `polluted-observations.md` — appended thumbnail observations + Pabian
  victory-screen lead (supplementary track only).
- `coverage.md` untouched (no count changes). No server/APK changes.

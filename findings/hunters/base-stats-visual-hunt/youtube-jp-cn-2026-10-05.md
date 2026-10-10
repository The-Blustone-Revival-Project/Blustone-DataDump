# Lane log — Japanese YouTube / Bilibili / Chinese promo video pass (2026-10-05)

**Lane:** Japanese YouTube (`ブルストーン` / `ブルーストーン`), Bilibili `Blustone2`
player video, Chinese promo clips. Recruitment/release videos, the 1:12
awakening-video lead, the 16-minute recruitment video (known negative), and
MON BLAST! clips (cross-title only).
**Rule reminder:** never infer a catalog ID from a portrait alone; no value
counts toward any 70% threshold from this lane. Blustone vs Blustone 2
version context is recorded per video date where known.

## Videos checked

### 1. 펩시 — 블루스톤 헌터 각성 (1:12 awakening lead, known partial)

- **URL:** <https://www.youtube.com/watch?v=Y2nxj-YwI5I> (Korean uploader `펩시`,
  mixed-game channel; video is vertical gameplay, ~2021 per prior inspection).
- **Status this pass:** NOT re-inspected pixel-by-pixel; prior visual finding
  stands and is already logged in `coverage.md` / `polluted-observations.md`
  (`시계초`, Lv.1/30, Strength 27,155, HP 3,021 / ATK 1,144 / DEF 1,671 at
  ~00:52; awakening panel 27,155 → 28,502 + 50,000 currency at ~01:07).
- **New this pass:** `noembed` and YouTube `oembed` metadata lookups for this
  video ID both returned `401 Unauthorized`, so title/description text could
  not be recovered to map the display name `시계초` to a catalog row. Exact-token
  web searches for `27155`, `28502`, `3021`, `1144` alongside `블루스톤` /
  `시계초` (per README search log) returned unrelated results and did not map
  the name. The name remains unmapped; the panel stays a partial lead with no
  base coverage.
- **Version context:** uploader channel search result dates the clip to about
  5 years ago (~2020–2021), i.e. the Blustone 2 era (post-2018-11 relaunch);
  do not assume pre-rebalance balance.

### 2. 펩시 — 블루스톤 헌터 섭외 (16:01 recruitment video, known negative)

- **URL:** <https://www.youtube.com/watch?v=J7N2LN04AR0>
- **Status this pass:** metadata lookups (`noembed`, `oembed`) returned 401;
  no new frames sampled beyond the prior pass (~0:02 blurred recruitment
  screen, ~1:18 Robin release/sale confirmation). Confirmed negative for stat
  panels. Same uploader's shorter recruitment variants carry no stat
  information in their titles.

### 3. 펩시 — shorter Hunter Recruit clip (3:49, known negative)

- **URL:** <https://www.youtube.com/watch?v=iC0sbWnHqxs>
- **Status this pass:** previously sampled at 00:30 / 01:14 / 02:21
  (recruitment cards, ten-pull, item-acquisition screen); no hero detail,
  accessory, or monster panel. No change this pass.

### 4. 펩시 — 블루스톤 헌터 자기극복 (19-second Short, unresolved lead)

- **URL:** <https://www.youtube.com/shorts/RG47CcM7c20>
- **Status this pass:** title indicates a self-overcoming/transcendence panel;
  player/fetch paths remain throttled, no frame inspected. Remains a promising
  visual lead, no values inferred.

### 5. Bilibili — Blustone2 developer-server preview (identity-only lead)

- **URL:** <https://www.bilibili.com/video/BV173JM6iEzc/> by `Takane_Manaka`,
  4:17, posted 2026-06-14. Page metadata fetched 2026-10-05: title `Blustone2`,
  tags `手游情报 / GMV / 教程攻略`, uploader note `大隐藏不出不换,自用`.
- **Content (from prior preview through ~01:01):** server-selection screen
  stating "This is the server I developed", then a snowy story scene with an
  unnamed light-brown-haired male (red/black coat) and a small penguin-like
  creature; sign-in dialog blocks the rest. No stat panels. Because this is
  presented as the uploader's own server, it is NOT original-server evidence.
  Unnamed figures stay visual-only identity leads; no catalog IDs assigned.

### 6. Bilibili — 128-part Blustone story collection (NEW lead inventory)

- **Entry URL:** <https://www.bilibili.com/video/BV1wo4y1X7K2/> —
  `（Blustone）主线剧情第一章：突如其来的考试.第1话：队长资格测试` (4:02),
  by uploader `乛ㅂ乛` (space 10861023), posted **2021-07-07**, 385 plays at
  fetch time. Tags: `剧情 / 手机游戏 / 青石之战 / 青石 / Blustone / 疾风小侠`
  (`疾风小侠` = the CN服 name; `青石之战` = CN title). Description gives a
  game-download method (QooApp → search Blustone; UU accelerator → Blustone
  国际版; Google; QQ group 528788300) — install-routing text, not stats.
- **Collection:** `Blustone主线故事第一季` (collection sid 11225), **128 parts**,
  4,676 collection plays. Full episode list transcribed from the page on
  2026-10-05 (chapters 1–18, see §A below). Related videos from the same
  uploader include NPC stories (`列奥纳多`, `艾斯特`, `拉娜`,
  `贝克汉&杰克`) and a character story (`圣诞双胞胎-莉兰&拉兰`,
  BV16Y4y1q7mZ).
- **Stat relevance:** NONE yet — these are story/dialogue captures. No frames
  were played/inspected in this pass (player not exercised), so no character
  art, stat panel, or numeric value is claimed. Keep as a dialogue/art lead
  only; individual episode videos could later be sampled for battle HUD or
  roster frames, but story episodes are a low prior for stat panels.
- **Version context:** posted 2021-07-07, i.e. Blustone 2 international-version
  era (client 2.x); any future stat frame from these videos must be labeled
  Blustone 2 / 2021 balance, not assumed identical to earlier balance. Note
  the 2019-09-05 rebalance boundary in `stat-version-context.md`.

### 7. MON BLAST! official Monster Info clips (cross-title ONLY)

- Snowfox: <https://www.youtube.com/watch?v=sAlXfcSOKTc> — `noembed` confirms
  title `Mon Blast! Area 1 Gold Card Monster 'Snowfox'`, author
  `VisualShower Corp.` (`@visualshower`), thumbnail
  `https://i.ytimg.com/vi/sAlXfcSOKTc/hqdefault.jpg`.
- Pandahawk: <https://www.youtube.com/watch?v=rt85g45tBY8> — `noembed`
  confirms title `Mon Blast! Area 7 Gold Card Monster 'Pandahawk'`, same
  official author.
- Moonwoof: <https://www.youtube.com/watch?v=bytCvTR6L3c> — `noembed`
  confirms title `Mon Blast! Area 1 Gold Card Monster 'Moonwoof'`, same
  official author.
- **Handling:** titles/areas re-confirmed; HP/ATK figures already in
  `cross-title-mon-blast.md` are NOT re-transcribed or counted here. MON
  BLAST! is `com.vshower.prd_pf` (separate puzzle/PvP app, first released
  2020-04-01 per store listings); no Blustone `M`-ID crosswalk exists.
  Zero Blustone monster coverage credit.

### 8. Japanese text/video searches (negative results, documented)

- `ブルーストーン ハンター 覚醒 ステータス YouTube` → unrelated games
  (Solo Leveling:Arise livestreams, PAD collab pages, RedStone guides);
  one useful hit was the `any.atsit.in` Bomber-hunter index (prose, excluded).
- `ブルストーン ハンター 育成 動画` / `ブルーストーン ハンター 育成 ステータス`
  → APPLION store listings (promo prose, version 2.8.0.1 dated 2022-07-13;
  no stat panels) plus Monster Hunter Wilds / MapleStory noise.
- `ブルーストーン ガチャ 10連 星3 youtube` → Blue Archive gacha pages only;
  no Blustone recruitment video with a stat panel surfaced.
- `ブルーストーン セレネ ハンター ジム 育成` → Namu wiki prose mirror and
  APPLION listings; no Selene (`068`, uncovered roster) stat video.
- Korean `펩시 블루스톤 헌터 각성` → Namu prose pages only; no new video.
- Korean `블루스톤 헌터 육성 영상 유튜브 스탯 전투력` → Namu prose + one
  MapleLand (different game) guide; no Blustone stat video.
- Chinese `青石之战 猎人 养成 视频 Blustone` → text guides (游戏鸟, cr173,
  gameresky, 99danji — prose, excluded by scope), TapTap listing prose, and
  the Bahamut board index (403 on direct fetch, no bypass attempted).
- YouTube search-results page and `yt.lemnoslife.com` metadata API both
  failed through the fetch tool (chrome-only / transport error); no video
  contents inferred from failed fetches.
- Bahamut board <https://forum.gamer.com.tw/B.php?bsn=33171> returned 403;
  left untouched as an uninspected forum lead (possible screenshot
  attachments, contents unknown).

## Tokens found this pass

| Token | Source | Coverage? |
|---|---|---|
| None (no new numeric stat) | — | No |
| 128-part story collection inventory + NPC/character-story links | BV1wo4y1X7K2 page, 2026-10-05 | No — dialogue/art lead only |
| MON BLAST! clip titles/areas re-confirmed (Snowfox Area 1, Pandahawk Area 7, Moonwoof Area 1) | noembed oembed, 2026-10-05 | No — cross-title only |

Strict coverage unchanged: heroes 1/113, monsters 0/22, accessories 1/100.

## Uncertainties / limits

- No YouTube video bytes were played in this pass; all YouTube findings are
  metadata/page-text only. The 펩시 401s are access limits, not content
  statements.
- Bilibili pages expose metadata + episode lists but the player was not
  exercised; no episode frame inspected.
- `시계초` remains unmapped to the English catalog. Do not guess an ID from
  the portrait.
- Chinese text guides name meta hunters (e.g. 三突尼尼/雅典娜, Tyson/rabbit-man
  attacker) but prose is out of scope and supplies no HP/ATK/DEF rows.

## §A — Bilibili 128-part collection episode list (transcribed 2026-10-05)

Uploader `乛ㅂ乛`, collection `Blustone主线故事第一季` (1/128 shown at entry).
Ch.1 突如其来的考试 (7话), Ch.2 胜利的蓝色 (8话), Ch.3 (7话, incl. 拉娜的请求),
Ch.4 (4话), Ch.5 世界的本来面目 (8话, incl. 奥赛罗拉的请求, 卡尔斯坦纳的袭击),
Ch.6 黑衣党 (7话, incl. 三只熊), Ch.7 (5话, incl. 晕倒的秀曼), Ch.8 (7话),
Ch.9 (7话, incl. 机器人工学家爱德华), Ch.10 (7话), Ch.11 面对真相时 (8话),
Ch.12 (7话), Ch.13 (8话, incl. 前往中央极点！), Ch.14 (7话),
Ch.15 (8话, incl. 迪诺的下落 / 两个迪诺), Ch.16 (9话),
Ch.17 本季最终话 (9话, incl. 不灭的火花), Ch.18 (5话, incl. 新的起点).
Related NPC/character stories: 列奥纳多 (BV1Rq4y1Q78Z), 艾斯特 (BV1uv411T7mS),
拉娜 (BV1164y1i7tr), 贝克汉&杰克 (BV1EM4y1L7U7),
圣诞双胞胎-莉兰&拉兰 (BV16Y4y1q7mZ).

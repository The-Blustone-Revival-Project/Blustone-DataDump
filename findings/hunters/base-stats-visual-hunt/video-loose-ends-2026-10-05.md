# Lane log — video loose ends follow-up (2026-10-05)

**Parent lane file:** `youtube-jp-cn-2026-10-05.md` (19s Short RG47CcM7c20
throttled/uninspected self-overcoming panel, Bilibili 128-part story collection
BV1wo4y1X7K2 Ch1–18 + NPC links Leonardo/Ester/Lana/Beckhan&Jack/Christmas twins,
Bahamut board bsn=33171 untouched at 403, `시계초` unmapped) + `coverage.md`.
**Rule reminder:** no portrait-only ID guesses; preserve URLs/timestamps;
Blustone-2 2021 version tags; story frames are dialogue/art leads unless HUD
visible. No server/APK changes in this lane.

## 1. Short RG47CcM7c20 — still uninspected, access pattern characterized

- **URL:** <https://www.youtube.com/shorts/RG47CcM7c20> (펩시, 19 s,
  title indicates a self-overcoming/transcendence panel).
- **This pass:** direct page fetch returns only the generic YouTube shell;
  `noembed` and `oembed` both return **401 Unauthorized** for this video ID —
  the same 401s the prior pass recorded for the same uploader's other videos
  (Y2nxj-YwI5I, J7N2LN04AR0), so the 401s are a fetch-tool egress/consent
  limitation, not evidence about this video's existence or removal.
- Alternate frontends tried and failed: `yewtu.be/api/v1/videos/RG47CcM7c20`
  → 403; `inv.nadeko.net/api/v1/videos/RG47CcM7c20` → 403. Exact-ID web search
  for `RG47CcM7c20` returns unrelated results (no mirrors, no title text).
- Thumbnail route `https://i.ytimg.com/vi/RG47CcM7c20/hqdefault.jpg` exists as
  a URL lead but the fetch tool cannot return image bytes, so no frame was
  inspected. A future pass with pixel access should try the thumbnail and
  `mqdefault`/`sddefault` variants first (cheapest), then the player.
- **Context recovered (no frame needed):** Namu confirms `자기극복`
  (self-overcoming) opens at **3★** and consumes a same-grade duplicate hunter
  plus metron/pieces — i.e. this Short almost certainly shows a transcendence
  result/comparison panel of the same class as Caragublu image 5 (Bear
  3,425 → 3,969). Keep as a high-priority visual lead; no values inferred.

## 2. Bilibili story collection — 3 episode/NPC pages sampled (metadata only)

Player video bytes are not exercisable with the available fetch tool, so no
battle-HUD or roster frame was inspected. What was verified is page metadata
and an expanded link inventory.

- **Entry re-fetched 2026-10-05:**
  [(Blustone)主线剧情第一章：突如其来的考试.第1话：队长资格测试](https://www.bilibili.com/video/BV1wo4y1X7K2/)
  by `乛ㅂ乛` (space 10861023), posted **2021-07-07**, 4:02, 385 plays;
  collection `Blustone主线故事第一季` (sid 11225), 128 parts, 4,676 plays.
  Tags: `剧情 / 手机游戏 / 青石之战 / 青石 / Blustone / 疾风小侠`.
  Description is install-routing text (QooApp → Blustone; UU accelerator →
  Blustone 国际版; QQ group 528788300), not stats.
- **Ch.1 Ep.2 sampled:**
  [(Blustone)第一章:突如其来的考验.第2话：决一胜负吧!](https://www.bilibili.com/video/BV1to4y1X77n/),
  posted 2021-07-07, 2:08, 105 plays, listed as 2/128. Related-video rail
  exposes further character stories beyond the prior inventory:
  `传说中的捣蛋鬼-尼尼`, `钢铁复活者-剑河`, `危险的赌徒奥黛丽`,
  `钢铁保镖卡因`, `战士的泳装-尼尼`, `据点防御骑士-劳伦斯`,
  `永恒火花：主角（名称随自定游戏名称变化）`, plus Ch.8 `寻找赫尔墨斯`.
- **NPC story sampled:**
  [(Blustone)NPC故事：列奥纳多](https://www.bilibili.com/video/BV1Rq4y1Q78Z/),
  posted 2021-08-14, 40 plays. Its related rail adds NPC stories not in the
  prior inventory: `秀曼`, `奥黛丽`, `克拉拉`, `古尔维格`,
  `韦斯特菲尔`, `抽奖鼠`, and character stories `身分不明的双胞胎-莉兰&拉兰`,
  `米德加尔特歌后-席琳`, `钢铁复活者-剑河`, `狼的孩子-比比`,
  `磁道炮炮手-喜爱娜`, `最初的猎人-兰索恩`, `情人节-赛莱妮`.
- **Stat relevance:** NONE yet. No frame played/inspected on any of the three
  pages; titles name NPC/character dialogue subjects, not stat panels. Keep
  all of these as dialogue/art leads only. Any future frame is Blustone 2 /
  2021 international-version balance (post-2019-09-05 rebalance); never assume
  earlier balance. The duel/test-titled episodes (Ch.1 Ep.2 `决一胜负`,
  Ep.4 `实力测试`, Ch.13 Ep.7 `不停歇的对练`) are the highest-prior candidates
  if a future pass can play video, since sparring episodes are the most likely
  to show a battle HUD — but that is a prior, not a finding.

## 3. Bahamut board bsn=33171 — text access recovered via mobile mirror

- **Status change:** desktop `B.php`/`C.php` routes return 403 through the
  fetch tool, but the **mobile mirror works**: `m.gamer.com.tw/forum/C.php`
  pages fetch as full text. The board is no longer untouched — two threads
  were read in full text this pass.
- **Thread read 1 (server-status, no stats):**
  [【閒聊】伺服器狀態](https://m.gamer.com.tw/forum/C.php?bsn=33171&snA=347&bpage=1&ltype=)
  by 風中叮嚀, 2021-03-31: post-update crash-on-launch reports (iPhone 6,
  iPhone 11). No screenshots, no stats. Era note: March 2021 crash reports
  are consistent with the late-life client, not stat evidence.
- **Thread read 2 (2017 beginner guide, prose + art attachments):**
  [【攻略】新手入門必須知道的七件事](https://m.gamer.com.tw/forum/C.php?bsn=33171&snA=17)
  by 請謝謝對不起 (jordan80475), 2017-11-03. Prose names the 2017 recruit
  sources: arena-point hunters **阿克沙 / 蘭索恩** (Akasha/Lantern-class T1
  support; text only, no numbers), association-hidden-stage hunters
  **雅典娜 / 尼尼** (tanks), **卡爾斯坦納 (鷹男)** (strongest non-黑主 DPS),
  **赫爾墨斯 (兔男)**; cash-gated **黑主** (≈NT$18,000 to veteran-hero-3,
  described as the only invincibility-skill hunter); event/limited
  **異想世界蒂蒂爾**, **萬聖節魔女莉可**, **海善** (noted as coming from
  the sister game 白島). **Evolution costs stated in prose:** 2★ 1000,
  3★ 3000, 4★ 12,000, 5★ 60,000 gold. These are 2017 economy prose claims,
  not verified receipts — rebalance context only, no coverage credit.
- **Attachments:** the guide embeds ~12 `truth.bahamut.com.tw/s01/201711/*`
  images (recruit/guide art per surrounding text). Image bytes were not
  inspected (fetch tool returns text only), so they stay uninspected art
  leads; surrounding prose describes them as hunter portraits/recruit screens,
  not stat panels — do not treat as hidden stat evidence.
- Related-thread inventory (titles only, unopened): `snA=59` 新手攻略之競技篇,
  `snA=58` 新手攻略之陣容篇, `snA=60` 新手攻略大補帖, `snA=76` 求方向,
  plus sidebar `精選桌布圖`, `請大家幫忙投海蒂`, `關於這個海善`. Search
  snippets also surface `结晶要怎么配` (crystal equipping — jewel-lane
  relevance) and `新手遊玩求角色健檢` (roster check — polluted-roster
  relevance). All remain unopened leads.

## 4. `시계초` name mapping — negative result with a legibility correction

- Exact searches for `"시계초" 블루스톤` and `시계초 블루스톤` return only
  botanical results: **시계초/시계꽃/시계풀 = passionflower (Passiflora)**,
  a common Korean plant noun. No Blustone hunter, thread, or video maps to it.
- The repo catalog (`analysis/catalogue/data/card-catalogue.tsv`) carries
  English names only; no Korean-name column exists to crosswalk against. The
  Namu hunter page fetch this pass was truncated before its name lists, and
  the thewiki.kr mirror returned 403, so no Korean roster list was scanned.
- **Correction to preserve:** `시계초` is a common noun, not a plausible hunter
  name — the ~00:52 panel reading in
  [펩시 — Hunter Awakening](https://www.youtube.com/watch?v=Y2nxj-YwI5I) is
  most likely a **low-resolution misread of the Korean hunter name**, not a
  catalog token. Do not search it as a name further; the productive retry is a
  fresh pixel read of that frame against the Korean client name list (Namu
  hunter page §§2.1–2.3) once image access is available. The panel values
  (Lv.1/30, Strength 27,155, HP 3,021 / ATK 1,144 / DEF 1,671; awakening
  27,155 → 28,502 + 50,000) stay exactly as logged: partial lead, no base
  coverage, identity unknown.

## Tokens found this pass

| Token | Source | Coverage? |
|---|---|---|
| None (no new numeric stat) | — | No |
| Transcendence-gate context (3★+, duplicate + metron/pieces) | Namu hunter-page search snippet, 2026-10-05 | No — prose context for the Short lead |
| 2017 evolution-cost prose (1k/3k/12k/60k) | Bahamut snA=17, 2017-11-03 | No — unverified economy prose |
| Expanded NPC/character-story link inventory (Shuman, Audrey, Clara, Gullveig, Westfield, lottery mouse, Bibi, Celine, Selene-Valentine, first-hunter Lantern, Nene variants, Lawrence, Kain-class stories) | Bilibili related rails, 2026-10-05 | No — dialogue/art leads only |
| `시계초` = passionflower common noun; prior reading likely a misread | Korean web search, 2026-10-05 | No — legibility correction, not a mapping |

Strict coverage unchanged: heroes 1/113, monsters 0/22, accessories 1/100.

## Uncertainties / limits

- No video frame was played or pixel-inspected in this pass; all YouTube
  findings are access-error/characterization only, all Bilibili findings are
  page-metadata only.
- Bahamut image attachments are URL-level leads; no pixel inspected.
- Thewiki.kr mirror (potential Korean name list) is 403 via fetch; Namu page
  body truncated before name sections.
- Chinese title → catalog crosswalk (e.g. 尼尼, 劳伦斯) is NOT performed here:
  titles name dialogue subjects and several mappings are ambiguous (e.g. 剑河
  vs 卡尔斯坦纳 for the Kain-class figure); no IDs assigned from titles.

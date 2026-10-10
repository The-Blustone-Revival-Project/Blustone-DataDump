# Jewelry and accessory visual-source follow-up — 2026-10-05

**Scope:** Look for new image/video evidence that pairs an individually identified Blustone accessory or mounted jewel with its numeric stat and item level. This pass does not treat textual guides or bare data tables as item-instance visual evidence. No values were added to strict coverage.

## Result

No new item-instance stat panel was recovered. The six Lv.15 mounted-jewel panels in [`../../catalogue/stats/GEAR.md`](../../../datasets/equipment/GEAR.md) and the single strict accessory anchor (Jack, Max HP 260 at Lv.50) remain unchanged. No additional item identity/level/numeric-stat tuple was observed.

## Visual-source checks

| Source | What was checked | Visual result | Disposition |
|---|---|---|---|
| [スマホゲームCH — 2017 Blustone review](https://gameappch.com/app/?app=04374) | The review page exposes 20 numbered screenshots (`04374_1`–`04374_20`). Reopened the gallery page and visually checked screenshot 1 in the page. Its visible composite contains battle HUD and dialogue/recruitment art, not gear. Images 15–16 had already been sampled in the prior pass; image 16 is a rank-up/power reading, not item stats. For image links 17–20, opened each numbered image link from the page; the host requests timed out, so these four frames remain **unseen**. | The page context and accessible image 1 are not item-stat evidence. The inaccessible tail cannot be classified. | No values or coverage. Do not claim all 20 frames visually inspected. Direct image URLs are `https://img.gameappch.com/image/app/04/04374/{17,18,19,20}.jpg`; each timed out on 2026-10-05. |
| Image search: [Korean equipment/jewel panel query](https://www.google.com/search?tbm=isch&q=%EB%B8%94%EB%A3%A8%EC%8A%A4%ED%86%A4+%EC%9E%A5%EB%B9%84+%EC%95%85%EC%84%B8%EC%82%AC%EB%A6%AC+%EC%A5%AC%EC%96%BC+%EB%8A%A5%EB%A0%A5%EC%B9%98+%ED%99%94%EB%A9%B4) | Image results for Blustone accessory/jewel stat UI. | Returned other games, including Blue Protocol: Star Resonance and Lineage M, plus generic accessory interfaces; no result identified as VisualShower Blustone. | False positives rejected; no values. |
| Image search: Japanese/English Blustone equipment/jewel stats | `ブルーストーン ゲーム 装備 強化 ジュエル ステータス`; `VisualShower Blustone equipment gear jewel stat screenshot` | Returned Blue Protocol: Star Resonance, Red Stone, LINE Rangers, and unrelated game interfaces. No exact-game panel found. | False positives rejected; no values. |
| Web/video search: Blustone equipment footage | Korean queries for 장비 강화, 쥬얼, 액세서리 and Jack/HP; Japanese query for 装備/ジュエル; English Blustone equipment screenshot. | Search results were unrelated. The only relevant general item page was Namu's [Blustone item page](https://dark.namu.moe/w/%EB%B8%94%EB%A3%A8%EC%8A%A4%ED%86%A4/%EC%95%84%EC%9D%B4%ED%85%9C), a text guide; it was not used as numeric evidence and no stat screenshot was surfaced. | No candidate video or item panel to inspect; no values. |
| Local VSFan asset inventory | Rechecked the current VSFan reports and searched filenames for equipment, jewel, accessory, weapon/armor, enhancement, and stat-related terms. The curated `Images/Blustone/Screenshots/Original` set is six full-screen snapshots already catalogued in [`../vsfan-visual-audio-material.md`](../../revival/vsfan-visual-audio-material.md); none is an item-stat screen. | The curated screenshots show a battle-prep page, dialogue, town/economy, recruitment, and cross-title dialogue. No item-instance values/levels. Filename filter surfaced resource-package metadata, icons/material strips, and gym art, not a new gear stat capture. | Existing evidence only; no coverage. |

## Search outcomes and limits

- Narrowed image searches reproduced the same broad failure mode already recorded in [`jewelry-visual-search-2026-10-05.md`](jewelry-visual-search-2026-10-05.md): exact-game visual matches do not appear in the returned result rows. This follow-up added Japanese equipment/jewel phrasing and an archive image-host check, rather than repeating the earlier Korean/English query set verbatim.
- The Japanese review gallery's `04374_17`–`04374_20` image CDN requests timed out in both browser and search tooling. Their pixels were not read; no identity or content is inferred from the page's surrounding text.
- The Namu item article's written enhancement rows are outside this visual-evidence task and were not transcribed as item stats.
- Keep all strict counts unchanged. This pass produces no item observations, no source-backed level, and no cross-source reconciliation.


# Monster visual-source pass — 2026-10-05

## Result

No new Blustone monster HP/ATK/DEF tuple was recovered. Strict monster coverage
remains **0/22**. The one newly opened visual source below is a PvP hunter clip,
not a monster encounter. It contributes no monster numeric evidence.

## Newly opened video

- **Source:** [Bilibili — “blustone 2”](https://www.bilibili.com/video/BV1Wt411q7dQ/)
- **Page metadata:** title `blustone 2`; page displays upload date/time `2018-12-10 07:29:07`; duration 2:08. Search result listed 457 plays and 2 danmaku at time checked.
- **Visual review:** Opened the player on 2026-10-05. The accessible preview showed:
  - **00:05:** vertical, pre-battle lineup headed `战斗准备` (battle preparation), with a VS matchup and raw tokens `53,509` and `77,777`. Their field semantics are not explicitly legible, and the screen is a hunter-versus-hunter lineup. They are not assigned to HP, ATK, or DEF.
  - **00:21:** vertical battle frame with a `READY` overlay and two hunter sprites. No catalog monster or monster-stat panel is visible.
- **Access limit:** Bilibili displayed a login prompt and a “30-second preview” overlay. The preview was enough to inspect the two frames above; no login, CAPTCHA, or bypass was attempted.
- **Identity/context:** This is PvP/team content, not a stage enemy. No `M001`–`M021` or `M100` identity is shown. Level, rank, difficulty, monster gear, and monster stat semantics are absent.
- **Confidence/status:** High that the cited frames show a PvP preparation lineup and a `READY` combat transition; no monster statistic is established. No coverage credit.

## Search log

Searches were aimed at visual gameplay sources and were checked against the prior
logs in [`monster-hud-observations.md`](monster-hud-observations.md) and the
monster-source audit in [`catalogue-report.md`](../../revival/catalogue-report.md) to
avoid reopening the already sampled YouTube battles, the previously tested
Bilibili story player, or the known HUD-only screenshot galleries.

| Query / route checked | Result | Disposition |
|---|---|---|
| `site:blog.naver.com 블루스톤 던전 전투 2017` | Search reported `blog.naver.com` blocked by robots.txt; no images or video frames returned. | No pixels or claims inferred. This does not repeat/open the earlier individual Naver blog URLs. |
| `site:youtube.com/watch Blustone battle monster fight club gameplay 2020` | Search results did not surface a new attributable Blustone monster-stat video. | No candidate opened. Existing four-video OCR sweep and named videos were not repeated. |
| `site:bilibili.com/video "Blustone" "第4话：实力测试"`; `site:bilibili.com/video "Blustone" "第3话：胜利的第一步"`; `site:bilibili.com/video "青石blustone暗主"` | Search led back to the Bilibili `青石Blustone` result page and its mixture of relevant Blustone story/PvP entries and unrelated “青石” matches. No result metadata contained enemy stats. | Inspected the new `blustone 2` video above. Other surfaced video pages were not opened or treated as visual evidence. |
| Bilibili search result `青石Blustone` → [BV1Wt411q7dQ](https://www.bilibili.com/video/BV1Wt411q7dQ/) | The clip's accessible 30-second preview was visually inspected at 00:05 and 00:21. | PvP hunter lineup/combat only; no monster or HP/ATK/DEF panel. |

## Coverage decision

This video is retained as a **negative visual-source check**, not as monster HUD
evidence. The lineup values are not labelled as an individual monster's HP,
ATK, or DEF. No existing polluted monster tokens were amended, because this
clip supplies no monster-side numeric reading.

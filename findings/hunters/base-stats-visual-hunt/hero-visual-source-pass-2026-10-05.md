# Hero visual-source pass — 2026-10-05

## Scope

Fresh public-source pass for visual material that might corroborate HP/ATK/DEF,
level/rank, or equipment context for heroes in the 2019 Japanese archive and
the broader Blustone catalog. The current archive maps 62 numeric profile
pages to catalog IDs, but the pages do not state level or equipped/unequipped
state; see [`archived-hunter-database-2019.md`](archived-hunter-database-2019.md).
This pass intentionally did not use textual guide tables as stat evidence and
did not repeat already logged Naver, Reddit, or generic YouTube query sweeps.

## Search log

Searches were run on 2026-10-05 through the public web search and image-search
tools. Exact query text is retained so future research can avoid repeating
these low-yield forms.

| Search | Candidate/result inspected | Visual check / disposition |
|---|---|---|
| `블루스톤 게임 헌터 상태창 HP 공격력 방어력 유튜브 2019`; `블루스톤 카탈로그 헌터 능력치 화면 2018`; `"블루스톤" "훈련" "HP" 헌터 2019`; `site:youtube.com/watch 블루스톤 헌터 상세 능력치` | No relevant Blustone video surfaced in returned results. | Image results were unrelated Monster Hunter material. No stat values or identities taken from them. |
| Image query `블루스톤 헌터 HP 공격력 방어력 화면 능력치`; `Blustone hunter stats screen HP attack defense old gameplay` | Returned Monster Hunter, other games, and unrelated items. | No result image attributable to Blustone; rejected as false matches. |
| `ブルーストーン ハンター 能力値 ステータス 動画 Blustone`; `블루스톤 육성 화면 헌터 스탯 영상 유튜브`; `블루스톤 헌터 능력치 캡처 공격 HP 장비 화면 게임`; `Blustone hunter gym level up stats gameplay old video` | One result was the Japanese blog [Blustone 攻撃手雑感](https://d18.blog-rpg.com/%E6%94%BB%E7%95%A5%E3%81%AA%E3%81%A9/blustone%E3%80%80%E6%94%BB%E6%92%83%E6%89%8B%E9%9B%91%E6%84%9F); another was the existing Caragublu guide. | These are text-oriented discussion/guide results and were not used for values. This is not new visual evidence. |
| `블루스톤2 헌터 육성 플레이 영상 장비 강화 2019`; `"블루스톤2" "훈련장" 유튜브 헌터`; `"블루스톤" "전투력" "헌터" 동영상 모바일`; `"Blue Stone" VisualShower hunter gym gameplay video` | [GameChosun’s 2019-04-02 Blustone 2 update post](https://www.gamechosun.co.kr/webzine/article/view.php?no=154354) was the only Blustone-specific image-bearing candidate; it links one VisualShower-provided article image. | Opened the article and attempted its linked image (`https://www.gamechosun.co.kr/dataroom/article/20190402/154354/175652_1554179303.jpg`). The image fetch timed out, so no pixels were available to inspect. Article text describes a trace-collection UI update, not hero stats; no visual contents were inferred. |
| `ブルーストーン ストーム ハンター 育成 ゲーム プレイ 動画`; `ブルーストーン ハンター 強化 ステータス 画面 スクリーンショット`; `블루스톤 스톰 헌터 훈련 스탯`; `블루스톤 카인 다이애나 네네 헌터 훈련 능력치 영상` | No game-matching candidate appeared. Returned results were unrelated titles and the already indexed Namu attacker page. | No pixels or stat values used. Namu is a text guide with dated image links already inventoried in `namu-hunter-gym-gallery.md`; this pass did not re-open its known-failing file host. |

## Findings

- **New hero HP/ATK/DEF tuples:** 0.
- **New level/rank/equipment-state corroborations for the 62 archive candidates:** 0.
- **New polluted numeric hero observations:** 0; no new source exposed readable hero numbers.
- **Strict hero coverage change:** none. Keep the 2019 archive's 62 rows as
  context-incomplete candidates and preserve the current ledger count.
- **Potential follow-up:** the GameChosun image remains a lead only if its
  original image becomes ordinarily accessible. Do not infer its content from
  the article caption or retry the same timed-out URL as though it had been
  visually inspected.

## Limits

This is a search-result pass, not a claim that no qualifying visual material
exists anywhere. Search engines returned unrelated titles for these query
forms, and one Blustone-specific article image could not be fetched. No
restricted page or challenge was bypassed. No image was downloaded or stored.

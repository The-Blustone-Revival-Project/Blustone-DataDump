# namu.wiki 블루스톤 — first-party mechanics recovered (browser-rendered)

**Written:** 2026-10-08. **Source:** `https://namu.wiki/w/%EB%B8%94%EB%A3%A8%EC%8A%A4%ED%86%A4`
(`블루스톤`), rendered in a real browser, last modified **2026-10-01 19:22:12**.
**23,818 chars** extracted; 290 links, 49 images, 4 `<table>` elements present.

**This is the most productive single source found in the project.** It contradicts
four replica fixtures, confirms five more, and supplies original fishing and
arena data that no other corpus carries. Plain HTTP gets **403** and the mirrors
expose only a client-rendered shell — **a browser is required**; see
`namu-browser-partial-2026-10-08.md` for the method and the honest limits (the
page's 290 sub-page links were **not** followed).

---

## 1. CONTRADICTED — replica fixtures that are wrong

| # | Replica has | **Original (namu)** | Consequence |
|---|---|---|---|
| **C1** | Arena rating **±10** | **win +15 points, loss −8 points** | `arena-service.ts` rating delta is wrong in both directions |
| **C2** | Arena week bucket **Thursday**-anchored | **"둘 다 일요일에 정산 및 초기화"** — league *and* ranking settle/reset **Sunday** | the whole weekly counter anchor is wrong |
| **C3** | — | defence loss **−5~6 points**; revenge loss **or giving up** **−8 points** | three distinct point events, not one |
| **C4** | Search cost **1 capsule** (local policy) | **per grade: 1★ 5 entries × 2 = 10; 2★ 4 entries × 8 = 32; 3★ 2 entries × 15 = 30** | `search-battle.ts` capsule cost is a fixture with an original shape |

## 2. CONFIRMED — replica values that namu independently corroborate

| # | Replica | namu |
|---|---|---|
| **F1** | **6 wins per league** | "패배 횟수와 상관없이 무조건 한 리그(티어) 당 **6번 승리**" — 6 wins regardless of losses |
| **F2** | League count 1..6 | **6 tiers: 브론즈 실버 골드 에메랄드 메트론 만다(린)** — Bronze, Silver, Gold, Emerald, Metron, Mandaring |
| **F3** | Campaign 10 stages per area, **30-star** upper-area threshold | "상위 지역 하나 당 **10개의 하위 지역**을 각각 **별 3개**, 상위 지역을 **별 30개**의 성적으로 클리어하면" |
| **F4** | 50 campaign stages | "**2019년 기준으로 50개의 던전**" |
| **F5** | Equipment/gear at ★4+ | "**4성 헌터**가 하나 이상 있다면 입장할 수 있다. **4성 헌터의** 무기나 복장을 업그레이드" — Forge *and* Jewel Mine both gate on owning a 4★ |

**F5 matters more than it looks:** the archive-derived "equipment unlocks at ★4"
— which I used earlier to bound gear-contamination risk on 57 of 62 rows — is now
**first-party confirmed in a second language.**

## 3. NEW — systems recovered that nothing else carried

### 3.1 The elemental cycle is **[RECOVERED]**

> "캐릭터 속성은 **전격속성/냉기속성/화염속성**, 3가지로 나뉘며 **화염>전격>냉기>화염**이다."

**Fire > Lightning > Ice > Fire.** A cycle, stated outright. Closes the
`forum_en/20587` finding with first-party text and matches the client enum
(0 None, 1 Fire, 2 Ice, 3 Lightning).

### 3.2 Role positional rule

> "공격수와 수비수는 **전방에서만** 스킬을 사용할 수 있고, 폭격수와 도우미는 **선내에서만** 스킬 사용이 가능하다."

Offense and Defense are **front-line only**; Bomber and Support are **in-ship
only**. Confirms the project's native finding and adds Bomber.

### 3.3 Rage (분노) — matches the measured SP mechanics

> "헌터를 가만히 둔다고 채워지는 것이 아니라 **터치를 하여 헌터가 공격하도록 해야 채워진다**. 또한 **자신이 적을 쓰러뜨리면 분노가 추가로 빨리 채워지며 최대 10개까지** 모을 수 있고 그보다 더 많이 모울 수 없다."

Rage fills from **touching/attacking**, never idling; **kills fill it faster**;
**cap 10**. First-party confirmation of the measured `maxSP 10` and of the
kill-vs-attack charge asymmetry the project has been inferring.

Also: "**4성 극대화 스킬** 중에서 일정 확률로 발동되는 것들은 치명타 확률이다" —
some 4★ ultimate activations are crit-gated, and a crit also fires the 4★ skill.

### 3.4 Fishing — **six named species with a price ordering**

> "일반 물고기(은관이나 금관이 아닌 것)를 기준으로
> **'뼈살이 빙어 < 흰수염 메기 < 메트론 은어 < 칼날 뱀장어 < 짝발 민물게 < 은쟁반 가지미'**
> 순으로(왼쪽이 제일 싸고, 오른쪽이 제일 비싸게) 가치가 높다."

| rank | Korean | romanisation | gloss |
|---:|---|---|---|
| 1 (cheapest) | 뼈살이 빙어 | bbaesari bing-eo | bonefish anchovy |
| 2 | 흰수염 메기 | hinject megi | white-beard eel |
| 3 | 메트론 은어 | metron eoneo | Metron sweetfish |
| 4 | 칼날 뱀장어 | kalnal baejang-eo | blade conger eel |
| 5 | 짝발 민물게 | jjakbal minmulge | bipedal freshwater crab |
| 6 (most valuable) | 은쟁반 가지미 | eunjaengban gajimi | silver-warbler octopus |

Plus: **the same fish species yields 은관 (silver crown) / 금관 (gold crown)
variants by size**, and the smallest shows no crown mark. Catches can also be
**영웅 강화 재료** (등껍질 shell, 금속조각 metal scraps) rather than fish. Fish
are sold at the Market.

**This is the first original fish data in the project.** The server side has been
blocked on missing fish reference data; this gives an ordering, not values —
but an ordering is enough to make any invented table *honest*.

### 3.5 Mirage Ruins — the mechanics behind the empty panel

- Reached from the airship terminal (걸베이그); **daily entry counts** apply.
- **Not strictly sequential** — "실력만 된다면 몇 개의 층을 건너 뛸 수 있다."
- Floor stage count: **3 stages up high, 6 deeper** ("상층일 경우 3개… 6개로 늘어난다").
- A floor not fully cleared → you remain until **자정 (midnight)**, then reset or retreat.
- **Only your strongest hero may be used on a floor**: "한 개의 층에서 사용할 수 있는 영웅은
  자신이 갖고 있는 영웅 중 **제일 강한 영웅**이다", and "1성 치르치르와 2성 치르치르를 갖고
  있다면 **2성만** 참가시킬 수 있다. 같은 등급일 경우 **종합 전투력이 높은** 헌터를."
- **Difficulty is auto-computed from the player's 종합 전투력** (total combat power).
- **Even when your combat power exceeds the dungeon's monsters', team composition can
  still make you fail** ("팀의 조합에 따라 클리어하지 못하는 경우가 있다").
- Currency **신기루 조각** (mirage shard); the 미러지 상점 sells 특급 의뢰서, 메트론 결정체,
  강화 재료, 도구 상자, 고급 도구 상자, 결정, **3성 헌터 흔적**, 할리의 흔적.

### 3.6 Mirage ruin types carry an **element → material** mapping

> "극저온(**수속, 등껍질**), 극고온(**화속, 화염석**), 극전압(**전속, 금속조각**),
> 황금(**난이도마다 다름, 루피**), 메트론(**메트론 조각**)"

Cryo → water attribute, shell · Heat → **fire** attribute, flame stone ·
High-voltage → **lightning** attribute, metal scraps · Gold → varies, **Rupees** ·
Metron → metron shards. Each ruin's enemies are **predominantly one attribute**.

### 3.7 Hunter Search (헌터 수색)

- Consumes **헬륨 캡슐 (helium capsule)**, explicitly **not** 연료 (fuel) — because
  the ornithopter is replaced by a different aircraft. Confirms the project's
  `AIRSHIP_TICKET` separation from AP fuel.
- **Per-grade entry counts and costs (§1 C4).**
- Hunters cycle **1★, 2★, 3★** in order from the start; the pool widens with
  search progress; difficulty rises with distance from Midgard.
- Up to **4 reward boxes**, and "이 4개의 상자 중에 실종된 헌터의 흔적이 **2장씩**".

### 3.8 Party and dormancy

- Max **4**; the leader physically engages, 3 wait in the ornithopter interior,
  and **waiting hunters recover a little HP**.
- The 2019-09-05-era patch notes that the Green Light gate vanished ("그린라이트 관련
  설정이 사라진 듯하다").

### 3.9 Other recovered facts

- **자기극복 (self-recovery) unlocks at 3★** — "특기강화, **3성 헌터부터 열리는** 자기극복".
- **Jewel Mine**: free mining once per day; manda premium mining yields **at least 3★** crystals.
- **Skins (부티크)**: 2–3 months in-game to reproduce; **300만다** gacha events.
- **2019/06/14 patch**: trace icons changed from wanted posters (수배서) to
  **parts of each hunter's clothing/accessories**. Beckhen's trace is his white feather.
- Mirrors occasionally pay out **루피** in Estelle's name.

## 4. Identity data, including a CONFLICT

**NPC/character roster with grades** — 걸베이그 **3★ Lightning Bomber**;
아테나 **3★ Defense**; 할리 **4★ Defense**; 제노비스 **4★ Offense**;
웨스트필드/이스트필드 "태생 **4성 전격속성 도우미**" (4★ Lightning Support);
헤르메스 **3★ 화속(Fire)**; plus Denali, Clara, Schumann (all **커피레빗**),
Lana, Estelle (werewolf), Westfield, Leonardo (Lantern's grandfather),
추첨쥐 (Lottery Mouse), Odri, Nerimivo. **팬더호크 (Pandahawk)** is the bird
beside Clara — confirming the creature in the MON BLAST! cross-title lead is
in-game. 아네모네 is **Nene's mother**.

> ### ⚠ CONFLICT — Hermes' element
> namu: **"3성 화속 헌터인 헤르메스"** (3★ **Fire**).
> 2019 JP archive `023`: `element_ja` = **冷気** (Ice).
> These are **direct contradictions** on one hero. The archive's `element_ja` agreed
> with the community catalogue **61/61** on other rows, so it is not simply
> unreliable. Do not silently pick one — see `element-rarity-axis-2026-10-06.md`,
> which records element as having 3 conflicts; this is likely one of them.

**The Jack puzzle is solved.** Jack is a **separate character** who interprets
for Beckhen — "파이트 클럽 주인인 흰 수탉(백헨)을 들고 있는 선글라스의 남성(잭)…
**백헨은 본체다**"; Jack's own speech is cutesy (`~용`). The accessory named
**`Jack`** (Max HP 260 @ Lv.50) is named for the *interpretor*, not the rooster.
This explains why `051`'s accessory and the "Jack" row looked like one odd record.

## 5. Provenance and honesty

**Read:** one page, rendered, `document.body.innerText`. **Not read:** its 290
sub-page links (hunter pages, per-role equipment pages, the `아이템` document,
which namu defers to `블루스톤/아이템`). **No numbers were extracted from its 4
tables** — it is an overview page.

**Era:** last modified 2026-10-01, so **post-2019-09-05 rebalance** and possibly
post-2019/06/14. Where it disagrees with the 2019 corpora, that may be the reason.

**Coverage unmoved:** heroes **1/113**, accessories **1/100**, monsters **0/22**.
Nothing here is a base stat. **§1 is a set of fixture contradictions, not base
stats** — and per project convention they are **options with evidence**, applied
by the owner, never by this research.

**Next step, unchanged from the partial file:** follow the 290 links — especially
`블루스톤/헌터`, `블루스톤/아이템`, and the per-role equipment pages (공격수 /
수비수 / 폭격수 / 도우미), whose mirrors rendered a shell with **empty** stat
slots. A browser may render values the mirrors never emitted.

# Jewel economy lane — 2026-10-05

**Lane:** official Facebook visualshowerEN Metron Crystal event post (per
10+1 pull economy note), r/Blustone `iq4irt` jewel-thread retry (4★-usability
snippet verification), Namu item-page crystal-section re-check, Bahamut
結晶 thread via mobile mirror, jewel mining/polish cost screenshots.
**Status:** research consolidation only. No server/APK changes. No new strict
coverage credit; strict panels stay 6/6 samples, accessories 1/100.

**Rules applied:** raw numerals and units preserved exactly; pre/post
2019-09-05 eras separated; generic `LEVELING.jet` parameters never used as
per-hero or per-item rows; community text and help prose are marked
TEXT-SOURCE and never presented as visual panel evidence.

Parent lanes: [`jewel-instance-2026-10-05.md`](jewel-instance-2026-10-05.md),
[`multipliers-2026-10-05.md`](multipliers-2026-10-05.md).
Coverage definitions: [`coverage.md`](coverage.md).

## 1. Metron Crystal per-10+1-pull economy note (TEXT-SOURCE, ERA-UNKNOWN)

- The prior lane already logged one [official event
  post](https://www.facebook.com/visualshowerEN/posts/blustone-event-the-more-the-better-by-lottery-mouseyou-will-get-a-metron-crystal/1124385431051052/):
  **one Metron Crystal per 10+1 pull** (economy note, not stats). Direct
  re-fetch in this pass was blocked (Facebook login wall); no new pixels or
  numbers were obtained from that post.
- A web-search pass over the official English channels corroborates the
  per-pull bonus pattern as text: `@VisualShowerEN` snippet — *"You will get
  a Metron Crystal for every 10+1 pull! And extra rewards are available based
  on your total number of Lottery Mouse pulls!"* — and `BlustoneEN` posts
  showing the parallel event-trace pattern (*10 Traces of Mary / Katrina on
  each 10+1 pull*, `bs.visualshower.com/event_en/…` links). These are
  search-snippet readings, not opened-post evidence; post date/build are
  unestablished (ERA-UNKNOWN).
- Standing: Metron Crystal is confirmed as a pull-linked bonus currency in
  official English event text. No amount beyond "one per 10+1", no crystal
  stat values, no mining/polish numbers come from this source.

## 2. r/Blustone `iq4irt` retry — snippet verified, thread still unread

- Direct fetch of
  `https://www.reddit.com/r/Blustone/comments/iq4irt/whats_the_point_of_jewels/`
  (page and `.json`) returns login/403 walls in this environment; no thread
  body was inspected. This matches the prior lane's blocked-fetch result.
- The search-engine snippet for the thread is now fuller than what the prior
  lane recorded, and it verifies the earlier fragment: *"The jewel you can
  use once you have 4☆ hunter in equipment panel. Only 4☆ hunter above can
  use jewel. Jewel boost your hunter stats."* Keep this exactly as
  **unattributed community text** — author, date, build and context are
  unknown; it is not visual evidence and earns no coverage.
- Independent mechanical cross-check (inference chain, not proof): the
  archived Japanese rank-up guide says **equipment unlocks at ★4**
  ([wayback-announce §1.3](wayback-announce-2026-10-05.md): ★4+ unlocks
  equipment), and the VSFan 1.4.4.1 help says jewels mount onto equipment
  rabbets (`CONTENTS11_7`, §5 below). A 4★ jewel gate therefore follows from
  the equipment gate even if no jewel-specific rule exists. Do not assert a
  separate native jewel-grade rule from this chain.

## 3. Namu item page re-check — crystal section still empty; Metron section transcribed

Full-text fetch of the [Namu item
page](https://dark.namu.moe/w/%EB%B8%94%EB%A3%A8%EC%8A%A4%ED%86%A4/%EC%95%84%EC%9D%B4%ED%85%9C)
(TEXT-SOURCE, mirror edited 2026-06-19, content describes the pre-shutdown
game, ERA-UNKNOWN throughout):

- **§4.4.3 결정 (Crystal) is still an empty header with no body text.**
  Negative result reconfirmed: no per-star crystal/jewel main-stat table
  exists on this page.
- **§4.1 메트론 (Metron) is fully legible** and is the page's actual
  crystal-adjacent content:
  - Metron is a fictional blue-glowing mineral (water + small amount yields
    much heat); artwork upgraded in the 2019/06/14 patch.
  - Two forms: 메트론 조각 (fragments — basic enhancement material, small
    and low-value but widely used) vs 메트론 결정체 (crystals — intact,
    found only deep in ruins, very rare).
  - Lore value anchor: in the S1 episode 승리의 푸른빛, Lana says one
    crystal is worth far more than 1,000 ordinary fragments — **but the same
    paragraph states fragments cannot be exchanged for a crystal**. Record
    the 1000:1 as in-fiction dialogue, not an exchange rate.
  - Use: self-overcoming (자기 극복) consumes fragments together with
    Metron; amounts vary by hunter grade and overcoming count (no table
    given).
- **§4.3 equipment tables are partly legible.** Grade-1 rows show toolbox
  tokens `0/2/4/8/12/0`-ish and rupee tokens `500/1000/5000` in garbled
  table order; grade-2 rupee row shows `1500`; grades 3–5 costs render only
  as guild-discount placeholders (`[할인여부]`), i.e. the amounts are **not
  stated** on the page. Do not transcribe any of these as exact per-level
  values — the column alignment is ambiguous (same caution as the prior
  lane).
- **Adjacent economy captured on the same page** (context for later balance
  work, all TEXT-SOURCE):
  - Skill-training material bands per role (attack: 금속 조각; defense:
    등껍질; bomber: 화염석; support: 약초), three tiers each, consumption
    per 5-level band rising 0 → 1 → 2 → … with higher tiers entering at
    higher bands (reconstructed band alignment from a garbled table —
    verify against a second source before use).
  - Fishing can yield a Metron crystal at 극악 (extremely low) probability;
    caught fish are now auto-sold.
  - Fight-chip corner sells Metron crystals (plus traces, high-grade request
    forms, skill materials); Beckhen's trace is always stocked.
  - Honor medals: ★4 trace = 700 medals per 8 traces; ★3 trace = 350 per 8.
  - Fuel: 5,000 rupees for the first purchases, 10,000 from the third;
    Manda 5 → 60 fuel; market rupee corner 6,000 → 60 per 4h.
  - 10+1 request form guarantees at least one ★3 hunter (×11 pulls,
    ★1–★4); 2019-07-12 event gave 2 boutique tickets per Manda 10+1.
  - Stim packs: auto-attack consumable with grade speed tiers ★1–★2 FEVER,
    ★3–★4 SUPER, ★5 ULTRA; later patched into a built-in auto system
    (unused packs stay in inventory).
  - Helium/search: costs 2/8/15 per grade ★1/2/3, searches 5/4/2, 4 waves
    per search, 2 traces per box, min 2 / max 8 traces.

## 4. Bahamut — no dedicated crystal thread found (negative result)

- The Blustone board exists (`forum.gamer.com.tw`, bsn=33171) with at least
  an intro thread (snA=353) and a Facebook-group/day-28心得 thread
  (snA=340). No 結晶/寶石配裝-style crystal-build thread surfaced in
  Chinese-language search (`巴哈姆特 爆斯通 結晶 怎麼配 寶石` returned
  unrelated boards); direct thread fetch returns 403 (bot guard).
- No mobile-mirror bypass was attempted beyond the normal fetch path. This
  stays a negative result: no Bahamut jewel-build content inspected.

## 5. Mining/polish mechanics — local texts already cover rules; cost screenshots still missing

Web search for mining/polish cost screenshots (`Blustone jewel mine polish
upgrade cost screenshot game`) returned only unrelated titles (jewelry
retailers, other games). **No mining/polish cost screenshot was found.**
The mechanics themselves are already documented in local sources:

- VSFan 1.4.4.1 EN help (PRE-THRESHOLD build), transcribed in
  [`vsfan-extracted-assets.md`](../../resources/vsfan-extracted-assets.md) §§CONTENTS11_4–11_7:
  jewels are Metron Crystals graded by class (higher class = higher
  ability); acquisition via **daily free mining** (player selects the kind,
  receives a random jewel of that kind), **Manda mining** (rarer jewels),
  advanced mining (higher classes faster), lucky Hunter Search finds, and
  the Market; **polishing costs only rupees (no materials), is
  probabilistic, higher stages are harder, and failure loses the spent
  rupees with no further penalty**; mounting requires matching jewel shape
  to the equipment rabbet (weapons/armor/accessories); set effects are
  slot-independent and stackable (`CONTENTS11_8`).
- `LEVELING.jet` res-1 is a **polish probability CSV (ranks 2–15,
  base/attempt values)** — tuning only, no costs or stat rows (per
  [`old-apk-2026-10-05.md`](old-apk-2026-10-05.md) §3).
- Post-threshold growth rule (Traditional-Chinese announcement,
  [wayback-announce §1.1](wayback-announce-2026-10-05.md)): 研磨/polish
  growth raised — ★1–★3 mains +30%, ★4–★5 mains +50%, all substats +50%,
  substat upgrades fixed at maximum.
- Open gap: **no rupee polish-cost table and no per-stage success-rate
  screenshot** have surfaced. The res-1 CSV gives probability tuning, not
  costs; do not present it as a cost table.

## 6. Searches run (negative results preserved)

| Query / source | Result |
|---|---|
| `Blustone Metron Crystal event 10+1 pull visualshowerEN facebook` | Official-channel snippets (Metron-per-10+1 + Lottery-Mouse total-pull extras; Katrina/Mary 10-trace-per-10+1 parallels); direct FB post fetch login-walled |
| `r/Blustone jewel 4 star equipment panel iq4irt` | Snippet verifies the 4★-gate community text; page + `.json` both 403 — thread body still unread |
| `블루스톤 헌터 아이템 결정 수정 연마 보석 장착` | Namu lore/review pages only; no stat panel |
| `Blustone jewel mine polish upgrade cost screenshot game` | Unrelated titles only; no game screenshot |
| `巴哈姆特 爆斯通 結晶 怎麼配 寶石` / `forum.gamer.com.tw 爆斯通 blustone` | Board bsn=33171 exists (snA=353 intro, snA=340 group/心得); no crystal-build thread; direct fetch 403 |
| Namu item page full-text fetch | §4.4.3 결정 still empty (negative reconfirmed); §4.1 Metron + §4.3 tables + adjacent economy transcribed above |
| `blustone.jp` 結晶 guide (prior wayback pass) | Title only, body empty — no values (see wayback-announce §2) |

## 7. Coverage impact

None. Strict ledgers are unchanged: mounted panels 6/6 samples (no seventh
found), accessories 1/100, heroes 1/113, monsters 0/22. Everything in §§1–5
is TEXT-SOURCE or community-text economy/mechanics context for the
polluted/supplementary track.

# KR text-source lane — Namu wiki, Inven, HungryApp prose, TapTap KR, Naver blogs (2026-10-05)

**Lane:** Korean text sources (NOT visual stat panels). Extract hero/economy numbers with
era tags; never normalize across the 2019-09-05 rebalance without explicit math.
**Status:** No new HP/ATK/DEF base tuples. Multiple economy/skill-magnitude tokens recovered.
Strict coverage: unchanged (heroes 1/113, accessories 1/100, monsters 0/22).

**Era rule applied:** The Namu mirror page reports last-modified 2026-08-13 but its content
spans 2017–2021 (2019-04 stim change, 2021-09 rollback). Individual claims are undated, so
**no claim below is assigned pre/post-rebalance** except where the source itself dates it
(HungryApp review 2019-09-05 = post-rebalance day 0; hypoid613 Naver post 2018-11-14 = pre;
Namu rollback narrative = 2021-09). Equipment +50% / crystal +30%/+50% / substats +50%
context: `stat-version-context.md`.

## 1. Namu hunter page (mirror, text only)

- **Source:** `https://d.namu.moe/w/블루스톤/헌터` (mirror of namu.wiki; direct namu.wiki
  fetch = HTTP 403; mirror HTTP 200, 1475 text lines, fetched 2026-10-05). Canonical page:
  `https://namu.wiki/w/블루스톤/헌터`. License: CC BY-NC-SA 2.0 KR.
- **Raw Korean preserved per item; translations are mine.**

### 1.1 Grades, titles, advancement (Korean text + translation)

- "총 등급은 1성 ~ 5성 까지며 발견되는 태생은 4성까지이다" — grades run 1★–5★; natural
  (born) max is 4★.
- Grade titles: 1성 신입 헌터 (Novice), 2성 하급 (Lower), 3성 중급 (Intermediate),
  4성 고급 (Advanced), 5성 마스터 (Master). (Cross-check: matches GameAppCH
  generic rank-up labels Amateur→Novice and FreeGame Mugen Middle→Advanced.)
- "모든 캐릭터는 승급시 자신과 같은 등급의 캐릭터를 자신의 등급의 수만큼 필요로 한다" —
  advancement consumes same-grade hunters equal to own star count (1★ needs one 1★, …).
- Footnote: "등급에 상관없이 30레벨이 최대" — max level 30 regardless of grade.
  (Supports existing local Lv.30 caps; is a community-text claim, not a native parse.)
- Roles: 공격수/수비수/폭격수/도우미; regroup: attackers+defenders fight outside
  (선외), bombers+helpers inside the airship (선내) and cannot trigger skills outside.
- Elements: 화염(가위)/냉기(바위)/전격(보) cycle; 냉기→화염→전격→냉기 strong order.

### 1.2 Numeric skill magnitudes (polluted-ledger candidates, NOT base stats)

- **Lantern (001), bomber:** "크리티컬 4스킬이 터질 시 5성기준 상대에게 한번에 10000이
  넘는 미친데미지" — at 5★, crit skill 4 deals 10,000+ in one hit, plus DEF-down debuff.
  Era/build/gear unknown; appended to polluted-observations as skill-magnitude context.
- **Gullveig, bomber:** "아군의 상시 공격속도 7.5%를 올려주어" — permanent +7.5% ally
  attack speed; stacks with Hermes 15% → 22.5%; +Karl Steiner skill → 37.5%.
  Raw percentages preserved; stacking arithmetic is the wiki's, not verified in client.
- **Hermes:** attack-speed passive ("공격속도 향상을 패시브로 보유"), DEF-down stacks
  ("방어 하락이 중첩"), pairs with Lantern. No numeric DEF-down value given.
- **Beckhen (051):** "파이트클럽에서만 공격, 방어, 생명력이 10% 증가" — +10% ATK/DEF/HP
  **in Fight Club only**; obtained via Fight Chip shop traces (375 chips per 5 traces,
  shop restocks every 6h). Era unknown.
- **Karl Steiner:** "노 스킬 상태의 공속이 7" — base attack speed **7** without skill
  (vs the 8.00 constant hypothesized from FAQ image 8 + 051 in `010.md`; Karl is the
  documented exception — consistent with Namu footnote "공격수들은 얘를 제외하곤
  공속이 모두 8이다", attacker-board exception).
- **Diana, bomber:** 5th skill raises whole-team crit *damage* probabilistically; pairs
  with Lantern's crit-*rate* buff. No numbers.
- **Haisen (White Island collab):** bond bonus 4★ 8%, 5★ 16%. **Chirrchirr (Alice):**
  bond 4★ 10%.
- **Stim@s (스팀팩, ex-신기한 물약):** since ~2019-04, pre-battle use; "+" button charges
  3000 루피 or 3 만다 ("3000천 루피" sic — literal text reads 3000-cheon; preserved
  literally, likely 3000). Era: 2019-04 change, pre-rebalance.
- **Rage costs:** attackers/defenders normally 3, bombers/helpers 4; Lily&Lala and
  Bear (036) cost 4 from the start despite role.

### 1.3 Enhancement economy (local-fixture cross-check material, not native proof)

- **Traces for fixed recruit:** 1★ 20 / 2★ 40 / 3★ 80 / 4★ 160 — formula (2^n)×10.
- **Self-overcoming (자기극복, 3★+):** metron-crystal / fragment pairs per step:
  1★ 5/50, 15/150, 45/450; 2★ 7/70, 25/250; 3★ 9/90, 30/300, 80/800;
  4★ 12/120, 40/400, 110/1100. Fragment = 10× crystal.
- **Skill training (특기 단련):** metron fragments + role material
  (metal shards / shells / fire stones / herbs; rusty→sharp→strange tiers); from 5th
  level, role material required, +1 per 5 levels ("5번째부터 … 5번마다 하나씩").
  Max skill level rises 10 per hunter grade (matches local 10-per-grade caps).
- **Equipment enhancement (added 6/22, year unstated; 4★+ unlock):** per-level rupee +
  toolbox costs transcribed levels 0–50 (500 → 1000 → 5000 → 15000 → 30000 → 100000
  rupee breakpoints at 10/20/30/40/50; toolbox 130/10 per level at 40–49).
  Element materials: 전격 번개 막대 / 냉기 냉각수 / 화염 인화성 물질.
  Remodel every 10 levels; guild discount ("협회 보너스", single-digit %) applies
  except on remodel. Full table in lane source; NOT copied here cell-by-cell —
  re-fetch mirror lines ~280–420 for the complete grid.
- **Sell:** 1–2★ hunters sell for rupees; 3★+ give 첨쥐 코인 (secret-corner currency).
  Lily&Lala traces: 12 첨쥐 코인 → 5 traces.
- **Boutique tickets:** earnable from fixed recruits; sometimes ~7000 currency in
  mirage shop.

### 1.4 Gacha / recruit pricing (Namu text)

- Probability recruit: 의뢰서 or 만다; **30개로 1회, 300개로 10+1회 (11 total)**;
  occasional discount on the consecutive 10-pull. (Currency unit 만다 implied by
  context; matches local 30/300 single/bundle.)
- Request (의뢰서) types: 초급 (1–3★ traces, ≤5 per ticket, usable 1–10 at once);
  고급 (1–4★ recruit; 20000 루피 in shop); 특급 (2–4★ fixed; 1500 fight chips /
  3000 mirage fragments / 20 첨쥐코인; sometimes 60000 루피); 전설 (3–4★ fixed);
  전설의 지명 (pick any 3★, every 28th attendance day; brand-new 3★ may be excluded).
- Fixed recruit (확정 섭외): trace thresholds above; Harley (4★ defender) mirage-only:
  300 mirage fragments → 3 traces/day → 160 traces ≈ 32 days (≈2–3 months per wiki);
  achievement quest grants 5 traces per 10 mirage floors (added 7/6, year unstated).
- Vincent (010) was a hidden hunter requiring Hero grade 3; later raised to natural
  4★ with bond buffs.

## 2. Namu main Blustone page (mirror, text only)

- **Source:** `https://d.namu.moe/w/블루스톤` (mirror HTTP 200, 783 text lines).
- **Currencies:** 골드/만다 top-right; 본 게임의 재화 footnote (gold = game currency);
  만다 is shared VisualShower-wide and auto-linked at login ("로그인 시 자동으로 연동").
- **Campaign:** 2019-era 50 dungeons; 10 stages per region; star = 1 (clear) + 1
  (under 01:00) + 1 (full team survival); 10 stars per region → reward; full-region
  30 stars → 만다 or 의뢰서.
- **Exploration:** fuel 1/min burn; fuel gauge empty → interior darkens but surviving
  outside hunter keeps fighting.
- **Mirage fuel formula:** 15 + 5(n−1) = 10 + 5n for dungeon n.
- **Helium capsules:** 1★ 2/search × 5 searches (10 total); 3★ 15/search × 2 searches
  (30 total); max 4 reward boxes per search, 2 traces per box (≤8 traces/run —
  conflicts with local 1-trace policy; flagged, not adopted).
- **Abyss (무저갱):** first dungeon 15 fuel, +5 each (same formula); element/day gating,
  Sunday all four open; per-dungeon entry counters.
- **Fuel supply windows:** 8–12 / 12–16 / 16–20 / 20–24h. Stage clear fuel coupon
  amounts: 10→만다5, 20→만다10, 30→만다15 (context: early regions also grant
  Lapis/Metis; exact mapping ambiguous — preserved literally).
- **Fight Club:** tiers Bronze→Silver→Gold→Emerald→Metron→Manda(rin); tier-up = 6 wins
  regardless of losses; win +15 pts, loss −8 (revenge-loss/forfeit −8; defense loss
  −5~6). Full tier reward table (fight chips + green manda) and rank reward table
  (ranks 1–30000+) transcribed in fetch output; weekly Sunday settlement.
- **Fish values (ice fishing):** 뼈살이 빙어 < 흰수염 메기 < 메트론 은어 < 칼날 뱀장어 <
  짝발 민물게 < 은쟁반 가지미; silver/gold crown sizes.
- **2021-09 rollback narrative:** mole-catching event paid more in bait+gold than its
  15000-gold replay cost (4 free plays, unlimited paid); 5-day exploit; silent
  rollback + thin 25-day-attendance compensation → user exodus ("산소호흡기를 떼버렸다").
  Era: post-rebalance, original-operations evidence only.
- **Skin gacha:** 300-만다 event pulls; event skins later sold for manda directly.

## 3. HungryApp review prose (2019-09-05, post-rebalance day 0)

- **Source:** `https://m.hungryapp.co.kr/news/news_view.php?bcode=news&catecode=002&pid=85749`,
  reviewer 남윤서, Lv.24 byline. Full prose fetched; article text used as **mechanics
  context only**, not stat evidence.
- Mechanics confirmed in prose: 4-hunter teams, 1 active fighter, ship-swap mid-battle;
  roles 공격수/수비수/폭격수/도우미 (bombers/helpers use special moves from inside);
  element RPS 가위(화염)/바위(냉기)/보(전격); guild war over 매트론 노천광 as end
  content; auto-play (맡기기) system; recruit flavor (추첨쥐 kidnapping with per-hunter
  dialogue).
- **No HP/ATK/DEF, prices, or reward numbers in prose.** All 104 comments are
  "보고갑니다"-class acknowledgments, no stat content.

## 4. Naver blogs / cafes

- **hypoid613 (2018-11-14, PRE-rebalance):** `https://blog.naver.com/hypoid613/221398542241`
  fetched full text. Confirms: chapters of 10 dungeons, 4-hunter teams, 3 stars per
  dungeon (condition-based), star-collection rewards, tap-to-attack + FEVER auto-attack,
  element advantage/disadvantage, 3★ Nene ("전설적인 말썽꾸러기") as early recruit,
  abyss-excavation + missing-hunter-search materials exchangeable for hunters/items,
  Blustone 2 pre-registration rewards (2만원 value: beginner/advanced request tickets,
  fuel, rupees, veteran points), account continuation to Midgard server.
  **No numeric hero stats, skill values, or stage rewards.**
- **ps3player (2018-11, PRE):** training-center (체육관) video mention only; not fetched
  (same promo wave as hypoid613, no stat expectation).
- **1gktnrn posts:** already covered in `naver-visual-hunt-2026-10-05.md` (Dumble
  power 2183, roster tokens, Bright/Therapy art). No new fetch this lane.
- **Naver cafes:** not accessed (login-gated); recorded as unattempted, not negative.

## 5. TapTap KR / Inven

- **TapTap announcement (2019-09-04):** already canonical in `stat-version-context.md`.
  No new fetch; no per-item numbers exist there.
- **TapTap KR listing / Inven comments:** websearch returned only the known Inven
  Blustone-2 interview (version lineage, no stats) and generic Mogong articles.
  No KR gacha-price thread or stat thread surfaced. Recorded as negative search
  result for queries in coverage-style log below.
- **Inven interview (2018-12-20):** version context only (Blustone 2 = retitled major
  update, account continuation). No stat panel.

## 6. FAQ images (Korean equipment screens)

- FAQ image 8 orphan (HP 2866 / ATK 1522 / DEF 1103 white + green deltas) already in
  `010.md` §44–55 and polluted ledger; identity search (exact numbers + Blustone)
  returned unrelated tables — identity still unknown.
- No additional Korean FAQ stat images identified this lane.

## 7. Lapis screenshot 503 lead — retry status (STILL UNRESOLVED)

- **File:** `Capture+_2019-01-25-23-49-07.png` under Namu attacker 2.1.1 (Lapis).
- Retried 2026-10-05 via execute-fetch with **desktop Chrome UA → 503 `remote`**,
  **iPhone Safari UA → 503 `remote`**, file-page shell loads (metadata only, broken
  image), **Seore mirror file route → 404**, **Wayback CDX → 429 bot-block**
  (no bypass attempted).
- Seore attacker mirror page itself loads (127KB) and indexes 28 Capture filenames
  (2019-01-25/26 attacker batch + 23-48-36/50 unknowns); pixels unavailable from
  either host. **Lead remains open; no values inferred.**

## 8. Search log (negative results preserved)

- `블루스톤 헌터 능력치 스탯 체력 공격력 방어력` → Namu pages (consumed above), no
  stat table; unrelated LordsMobile/CIFI threads rejected.
- `블루스톤 공략 보상 미션 스테이지 루피 만다` → Namu main page (consumed), one
  promo Naver blog (consumed); Shadowverse/Hearthstone results rejected.
- `블루스톤 헌터 훈련 강화 비용 골드 경험치` → Namu 1.5 tables (consumed); Hearthstone/
  unrelated rejected.
- `"블루스톤" 헌터 스킬 피해량 OR 스킬효과 OR 특기효과 수치` → no numeric skill table;
  only Namu hunter index snippet.
- namu.wiki direct fetch → 403 (bot wall); d.namu.moe + dark.namu.moe → 200.
  file.namu.moe → 503 for all image assets regardless of UA.

## 9. Files updated

- This file (new lane log).
- `polluted-observations.md`: appended § "Namu KR text-lane numeric tokens
  (2026-10-05)" — Lantern 10k+, Gullveig/Hermes AS %, Beckhen FC +10%, Karl AS 7,
  Haisen/Chirrchirr bonds, stim price, gacha 30/300, trace formula, enhancement
  cost breakpoints, FC tier/rank tables pointer, mirage fuel formula, helium costs,
  star conditions. All tagged era-unresolved except dated items.
- No coverage-count change; no server/APK change.

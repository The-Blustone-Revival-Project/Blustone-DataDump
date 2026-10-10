# Bahamut queued threads, Short thumbnail, Korean name list (2026-10-05)

**Parent lane:** `video-loose-ends-2026-10-05.md` (§3 queued `snA=59/58/60/76`,
crystal/roster search leads; Short RG47CcM7c20 thumbnail lead; `시계초` mapping).
**Method:** Bahamut mobile mirror (`m.gamer.com.tw/forum/C.php`, works; desktop
403). Image bytes via direct `truth.bahamut.com.tw` download — all HTTP 200.
YouTube thumbnails via `curl.exe` + local pixel read (fetch tool returns text
only, but `i.ytimg.com` serves `image/jpeg`, which the fetch tool reports as
"unsupported content type" — that error itself confirms the URL is live).
**No server/APK changes. No 403/429 bypass** (one Namu page 403'd once, then
succeeded on retry; no special handling).

## 1. Queued Bahamut threads — all four read in full text

| Thread | Title / author / date | Content | Stat relevance |
|---|---|---|---|
| `snA=59` | 【攻略】新手攻略之競技篇 / 糖糖 (a2581473) / 2018-01-30 | Arena meta prose: attacker (Hermes, Octavia mainstream) + 4 bombers (Diana, Lantern, Patrone, Levi) or attacker + 3 bombers + Joy; Joy skill +35% crit; 2-tank-3-healer / 3-tank-2-healer stall comps; no 1–2★ dismissal (Bruce Bang, Levi cited). Zero attachments. | NONE — comp prose, no numbers beyond comp counts |
| `snA=58` | 【攻略】新手攻略之陣容篇 / 糖糖 / 2018-01-30 | Damage-model prose: block (rate/amount), crit (rate/damage; Edward −120% crit-damage taken), attack speed; element triangle 雷>冰>火 (+20%, resistance capped 20%); Octavia +25% vs fire. B1/B2 skill-duration Q&A. Zero attachments. | NONE — mechanics prose; 20%/25%/120% are combat modifiers, not base stats |
| `snA=60` | 【攻略】新手攻略大補帖 / 糖糖 / 2018-01-30 | Beginner mega-guide + long comment thread (metron economy, 10-pull保底 debate, 58-Manda fuel timing). No per-hero numbers. Zero attachments in OP. | NONE |
| `snA=76` | 【問題】求方向 / live85121 (+2 roster posts) / 2018-02-13..14 | Direction request with text advice (Nene/Lantern/rabbit/Hermes/Patrone/Joy; Akasha nerf remarks). **FOUR image attachments** (see §3) — roster screenshots, text-fetch invisible. | Roster images only (polluted; §3) |

## 2. Crystal + roster-check threads

- **Crystal (`snA=348`, 【問題】结晶要怎么配？要如何觉醒？, samajie, 2021-04-18):**
  Q: how to equip crystals for the first five + how does awakening work.
  A (黎玥 Ramius, B2 2021-04-20): 隊長先6防，雙子4攻速2攻擊，老鼠6攻擊，席林6防
  (Captain full DEF×6; twins 4 ASPD + 2 ATK; mouse full ATK×6; Celine full DEF×6).
  Follow-up: 恢復 (recovery) is **in-ship slow HP regen, not heal amount**
  (B5 2021-04-21). No attachments. **Jewel-lane relevance only as 2021 player
  build advice** — set-completion counts (6/4+2), not stat values. No coverage.
- **Roster check (`snA=223`, 【問題】剛入坑的萌新求健檢, tommy949, 2018-05-29):**
  Day-4 newcomer asks what to invest skill/stars in; replies only say a rework
  is imminent / play casually. **ONE image attachment** (see §3). No numbers.
- Related-thread inventory harvested from sidebars (unopened): `snA=336`
  新手目前玩7天求方向+選擇卷該選誰 (2020-08-19), 新手攻略之訓練獵人,
  新手攻略之材料篇, 新手攻略之深淵遺跡篇, 新手求健檢 (2018-01-28, 2018-03-09),
  新手求方向 (2018-02-18), 新手想請教高手一些問題 (2018-06-25),
  新手方向及心得&改版後深淵6.7.8推薦組合 (2018-03-21), 回鍋幫健檢求方向
  (2019-05-17). All remain leads.

## 3. truth.bahamut attachment catalog (19 URLs, 18 thread images + 1 sidebar thumb)

**`snA=17` (2017-11 guide, 13 images)** — surrounding prose describes hunter
portraits/recruit screens, NOT stat panels. Full URLs verified present in HTML:
`s01/201711/46452a467287c257332e9d5c5a2773e0.JPG` + `3395b7e1...` (arena-point
Akasha/Lantern T1 text); `4f58b6e1...` + `6dd13e94...` (Athena/Nene tanks);
`e1376f01...` (Karl Steiner/鷹男 strongest non-黑主 DPS); `676e20c8...`
(Hermes/兔男); `5b82c74a...` (黑主 cash-gated); `fc5af1b0...` ( fantasy Tidityl);
`15463a1c...` (Halloween Rico); `4bfedc39...` (Haisen/白島 collab);
`12a8a7161...` (dispatch/idle-farming UI); `15e5243ab...` + `adb55a15...`
(referral/friend slots). Bytes NOT downloaded (guide-art per prose; low prior
for stat panels). Remain URL-level leads.

**`snA=76` (2018-02 direction thread, 4 images — all DOWNLOADED, HTTP 200, pixel-inspected):**
- `s01/201802/09c0bdfec7ed722cc1085fe0b6faaea9.JPG` — OP #1 (live85121, text-empty,
  image-only post). Roster 獵人名單 **30/33**. File preserved:
  `snA76-09c0bdf.jpg`.
- `s01/201802/628a9c990b43dab608744b1696b162b2.JPG` — post #2 (zxzxss20097,
  "想問問方向怎走…真心想玩下去"). Roster **19/27**. Preserved `snA76-628a9c99.jpg`.
- `s01/201802/fc0cffb51e31f83ef93e565058199cc1.JPG` + `s01/201802/1f4bec7bffff08402c26922b51f40940.JPG`
  — post #3 (a91827346515, "20天新手，求建議"). BOTH roster **27/42** (two
  screenshots of one 42-count roster, rows 1–4 then rows 4–7 approx). Preserved
  `snA76-fc0cffb5.jpg`, `snA76-1f4bec7b.jpg`.

**`snA=223` (2018-05 newcomer check, 1 image — DOWNLOADED, HTTP 200, pixel-inspected):**
- `s01/201805/83e098e12109d23dc2464c9037d02b0d.JPG` — OP roster **20/33** with
  團體晉級 button. Preserved `snA223-83e098e1.jpg`.

**Sidebar thumbs (NOT thread evidence):** `s01/202008/4663d83c...` (snA=336 rail
thumb on snA=76 page), `s01/201905/065311d9...` (rail thumb on snA=223 page).
Excluded from tokens.

### Roster token transcription (all five images)

Layout (all): teal header 獵人名單 + `owned/total`; per portrait: `Lv. N` or
`Lv.MAX` badge, ONE large integer (field unlabeled — same presentation as the
Naver max-level list's unassigned numbers; treat as **roster rating token,
likely power/Strength, NOT HP/ATK/DEF**), small element icon, state label
(鎖定 locked / 探險中 exploring / 防禦中 defending / 代表 representative).
Portraits carry NO names. Identity is portrait-only → **no IDs assigned**
(one medium-confidence art match noted, polluted only).

**snA76-09c0bdf (30/33):** 5839探險中(Lv15) | 5338探險中(Lv18) | 1190探險中(Lv27) /
1082探險中(Lv27) | 7171防禦中(LvMAX) | 7483(LvMAX) / 6870(LvMAX) | 6823(LvMAX) |
6667(LvMAX) / 6597(LvMAX) | 6401(LvMAX) | 6045(LvMAX) / 6039(LvMAX) | 3904(Lv1) |
2831(LvMAX). 15 tokens.
**snA76-628a9c99 (19/27):** 2959鎖定(LvMAX) | 2820探險中(LvMAX) | 2572探險中(LvMAX) /
2528(Lv29) | 2433探險中(Lv9) | 2326防禦中(Lv21) / 2306鎖定(Lv8) | 1845探險中(Lv1) |
1701鎖定(Lv1) / 883(Lv5) | 861(Lv5) | 855(Lv1) + partial 5th row (Lv7 blonde /
Lv1 rabbit-ears / Lv27 brown-haired, numbers cut). 12 full tokens.
**snA76-fc0cffb5 (27/42, part 1):** 12549探險中(Lv15) | **6601探險中(Lv22,
brown-bear-head portrait — medium-confidence `036` Bear per `C036.jet` photo-bear
art, polluted only)** | 6413探險中(Lv18) / 4648探險中(Lv4) | 6045防禦中(LvMAX) |
13184鎖定(Lv23) / 8182鎖定(LvMAX) | 7565鎖定(LvMAX) | 3953(Lv1) / 3412鎖定(LvMAX) |
3129鎖定(LvMAX) | 3089鎖定(LvMAX) + partial 5th row. 12 full tokens.
**snA76-1f4bec7b (27/42, part 2):** 2906鎖定(LvMAX) | 2847(LvMAX) | 2755鎖定(LvMAX) /
2580(LvMAX) | 2488鎖定(Lv1) | 2227鎖定(Lv1) / 2163(Lv1) | 2146鎖定(Lv1) |
2103鎖定(Lv1) / **1977鎖定(Lv1) ×2 (twin red-hood portraits — duplicate-owned
observation)** | 1249(LvMAX) + partial 5th row. 12 full tokens.
**snA223-83e098e1 (20/33):** 5284代表(Lv11) | 4500防禦中(Lv11) | 2599探險中(Lv12) /
2116探險中(Lv16) | 3294防禦中(LvMAX) | 3044防禦中(LvMAX) / 2515防禦中(LvMAX) |
1084(Lv18) | 973(Lv22) / 846(Lv1) | 415(LvMAX) | 343(Lv1) + partial 5th row
(Lv1 ×3). 12 full tokens.

63 full roster-rating tokens total. **Zero coverage credit**: no HP/ATK/DEF
split, identities unassigned, gear/jewel/awakening state unknown.

## 4. Short RG47CcM7c20 — thumbnail retrieved and pixel-inspected

- `mqdefault` (HTTP 200, 4,677 B), `hqdefault` (200, 7,442 B), `sddefault`
  (200, 30,749 B) — all live. Prior "fetch tool cannot return image bytes"
  limitation bypassed via `curl.exe` + local read.
- **All three show the SAME frame:** low-angle close-up of a chubby
  rabbit-like creature mid-scream/roar with radial speed-line burst background,
  vertical-Short crop with blurred side bars, maple-leaf player UI strip at the
  bottom (consistent with uploader Pepsi's CA client). Preserved:
  `short-RG47CcM7c20-thumb-sd.jpg` (largest).
- **Reading:** awakening/transcendence animation frame, NOT a stat panel — no
  numbers, no comparison arrows, no panel chrome. Consistent with the
  self-overcoming (자기극복) title context from §3 of the parent lane (3★+
  duplicate + metron/pieces gate). The creature's species (rabbit/mouse class)
  is a soft art lead at best — **no catalog ID assigned** (Lottery-Mouse-class
  resemblance noted and explicitly NOT claimed). The actual panel the Short
  titles remains uninspected; full-frame inspection still needs video access.
- oembed/noembed 401s and inv.nadeko/yewtu.be 403s stand as recorded (tool
  egress limits, not video status).

## 5. Korean hunter-name list (Namu role pages, fetched 2026-10-05)

Source pages (all `namu.wiki/w/블루스톤/헌터/...`): 공격수 (1★3/2★3/3★11/4★6),
수비수 (1★3/2★3/3★9/4★3), 폭격수 (1★3/2★2/3★7/4★4), 도우미
(1★3/2★3/3★7/4★5). English spellings below are Namu's own inline readings
where present; bracketed mappings use VSFan/catalogue crosswalk and are
approximate — for panel crosswalk use only, not coverage.

- **공격수 Attacker:** 라피스[Lapis 017] / 실베스터[Sylvester 006] /
  발리안[Balian 019] / 레베카[Rebecca 021] / 스카[Scar ?] / 모글리[Mowgli 002] /
  백헨[Beckhen 051] / 헤르메스[Hermes 023] / 옥타비아[Octavia ?] /
  산타걸 레베카 / 나쁜아이 사냥꾼 산타클로스터[Clauster 042] / 유리[Yuri ?] /
  하이디[Heidi 044] / 치치[Chichi ?] / 칼슈타이너[Karl Steiner 012] /
  비비[Bibi ?] / 나탈리아[Natalia ?] / 릴리&랄라[Lily&Lyla 047] /
  빈센트[Vincent 010] / 칼바람[Khalbaram ?] / 메리[Mary ?] / 벨라[Bella 075] /
  제노비아[Zenobia ?]. Role note: ATK-focused, skills cost **3 Rage**,
  front-only; 3rd specialty always self-ATK buff; training mats metal fragments.
- **수비수 Defender:** 헤카테[Hecate 011] / 로빈[Robin 018] / 캡틴[Captain 009] /
  리코[Riko 024] / 할로윈 마녀 리코 / 제라드[Gerard 005] / 빠삐용[Papillon 043] /
  에드워드[Edward ?] / 덤블[Dumble ?] / 아테나[Athena ?] / 네네[Nene 003] /
  주노[Juno 062] / 카인[Kain ?] / 곰[Bear 036] / 칼리버[Calibur ?] /
  할리[Harley 046] / 에리즈[Erise ?] / 아네모네[Anemone ?]. Role note:
  DEF-focused, **3 Rage (Bear 036 excepted at 4)**; shell-fragment mats. Robin
  note: 5★ per-second debuff-cleanse passive + full-level 2nd-skill heal counters
  Geranium/Bella-style perma-bleed.
- **폭격수 Bomber:** 시에나[Sienna 020] / 메티스[Metis 007] / 로크[Locke 014] /
  레비[Levi 015] / 테디보머[Teddy Bomber 025] / 랜턴[Lantern 001] /
  잭 오' 랜턴 랜턴 (Halloween Lantern; full name canonically Jack O' Lantern) /
  디아나[Diana ?] / 걸베이그[Gullveig 039] / 파트로네[Patrone 033] /
  아폴론[Apollon ?, 2018-08-17 fire] / 디노[Dino 054, 2018-06-29 ice] /
  셀레네[Selene 068, 2019-05-31 ice] / 유디트[Judith 067, 2019-05-23 fire] /
  제라늄[Geranium ?, 2019-03-29 lightning] / 오드리[Audrey ?, 2019-08-05
  lightning, ex-NPC]. Role note: ATK-focused, **4 Rage**, in-ship-only skills;
  flame-stone mats.
- **도우미 Support:** 치르치르[Tyltyl 004, NOT a typo] /
  이상한 나라의 치르치르 / 브루스 방[Bruce Bang 016] / 데날리[Denali 013] /
  아세로라[Acerola 030] / 해선[Sunny 022, 白島 collab, KR 바다 해 착할 선] /
  빗자루 마녀 데날리(Halloween) / 조이[Joy 035] / 아카샤[Akasha 008] /
  크로커스[Crocus ?] / 팬지[Pansy ?] / 브라이트[Bright ?] / 테라피[Therapy 050] /
  테레사[Teresa 065, 2019-04-30 first natural 4★ fire support] /
  셀린[Celine ?, 2019-06-14] / 레온[Leon 074, 2019-08-23 guild-war trace-only] /
  소피아[Sofia ?, 2019-08-09 fire] / 알리아[Alia 070, 2019-06-14]. Role note:
  heal/buff, **4 Rage**, in-ship-only; unified 3rd specialty 공공 보건
  (team sustain); herb mats. Sunny's EN name vs KR hanja mismatch explicitly
  flagged by Namu itself.

**`시계초` check:** no roster name on any of the four pages resembles 시계초 in
spelling, syllables, or meaning (closest phonetic neighbors: 스카, 치치, 소피아
— none within misread distance of 시계초 as a whole token). Combined with the
passionflower common-noun finding, the ~00:52 panel reading is now near-certain
a low-resolution misread; **retire 시계초 as a search token**. The productive
retry remains a fresh pixel read of that frame against THIS list.

## Tokens found this pass

| Token | Source | Coverage? |
|---|---|---|
| 63 roster rating tokens (5 Bahamut 2018 screenshots, Lv+state labeled) | snA=76 ×4, snA=223 ×1, pixel-read 2026-10-05 | No — single unlabeled field, identities unassigned |
| Bear-art portrait at Lv.22 / 6,601 / exploring | snA76-fc0cffb5 | No — medium-confidence art match, polluted only |
| Duplicate red-hood pair, 1,977 ×2, Lv.1 locked | snA76-1f4bec7b | No — ownership observation |
| Crystal builds: Captain 6DEF / twins 4ASPD+2ATK / mouse 6ATK / Celine 6DEF; recovery = ship regen | snA=348, 2021 | No — player advice, not values |
| Arena/team/evo prose (snA=59/58/60/17 contexts) | Bahamut text | No — mechanics/economy prose |
| Short thumb: scream-frame, no panel | RG47CcM7c20 sddefault | No — animation frame |
| 4-role Korean name roster for crosswalk | Namu, 2026-10-05 | No — identity aid, not stats |

Strict coverage unchanged: heroes 1/113, monsters 0/22, accessories 1/100.

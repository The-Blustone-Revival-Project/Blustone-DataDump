# Roster growth windows: what ID `032`+ shipped inside them (2026-10-05)

**Parent file:** [`roster-2017-2026-10-05.md`](roster-2017-2026-10-05.md). It
reconstructed the **Dec-2017 roster as catalog IDs `001`-`031`** (30 named
hunters + the `026` Tyltyl variant) and, at §1.8, named its own largest
uncertainty:

> "The newest manifest evidence is **2017-09-08**, but the cutoff target is
> **2017-12-21**: a **14-week window with no manifest**. A hero released in
> Oct/Nov/Dec 2017 would be invisible to Lines A and B. … treat 'a `032`-class
> hero shipped in late 2017' as **open, not closed**."

**This file closes that window.** It found dated records *inside* it and they
are **positive, not null**: heroes numbered well above `031` were already
shipping in Oct-Nov 2017.

**Headline result — three IDs `>= 032` gain dated in-window records:**

| ID | Name | In-window dated record | Class | Date |
|---|---|---|---|---|
| `036` | Bear | official post calls it a **newly-added hunter** | **primary (official)** | **2017-11-08** |
| `038` | Rebecca (Christmas) / "Santa Girl" | official **debut announcement** | **primary (official, list row)** | **2017-11-30** |
| `034` | *(unnamed)* "Halloween Witch" (owner `024` Riko) | community guide calls it a **Halloween-event release** | secondary (dated post) | 2017-11-03, referring to Oct 2017 |

Plus one **existence** bound that is not a release date: `051` Beckhen is named
by name in the same official 2017-11-08 post (§1.4).

**The correction this forces.** `001`-`031` is the **Sept-2017 art-proved
floor**, not the Dec-2017 roster. The CDN manifests are *silent* about the
window — they cannot support an upper bound across a period they do not cover.
The parent's §1.7 inference ("nothing `>= 032` shipped") rested on Line 1
(art) crossing a gap Line 1 does not span. The Dec-2017 roster is
**`>= 001`-`031` + {`034`, `036`, `038`}**, with `051` proved to exist, and
`032`, `033`, `035`, `037`, `039`-`050`, `052`+ **unresolved and not excluded**.

**No stats, no playability, no coverage change.** Existence evidence only.
Heroes **1/113**, monsters **0/22**, accessories **1/100** — unchanged.
No server/APK/seed/emulator/phone/Ghidra operation. No binary downloaded;
only HTML text was fetched. No `BS`/JET/CDN manifest was re-read to reach
these conclusions.

---

## 1. PURE — dated records for ID `032`+ inside the open windows

### 1.1 Method, and why the parent file could not find these

The parent's Line A/B evidence is **shipped-art manifest** evidence: the reslists
are stamped `20170904165634` and `20170908141924`. Those are *the only two*
manifests that exist locally. No manifest exists between **2017-09-08** and the
**2017-12-21** cutoff, so the window can only be attacked with **dated prose
records** — official board posts, and dated community posts.

Three dated in-window sources were found and each was read in full text:

1. `bs.visualshower.com` **Traditional-Chinese event board** (`event_zh`),
   board-list captures at **2017-12-01** and **2017-12-12**, plus several
   in-window post bodies at `event_zh/<srl>`.
2. `bs.visualshower.com` **English event board** (`event_en`), board-list
   capture at **2017-11-13** (used to date the Chinese posts, since the EN
   bodies themselves are uncaptured).
3. Bahamut `bsn=33171` thread **`snA=17`**, posted **2017-11-03**.

A localisation note that matters for reading all of this: the Chinese boards
carry hero names in Chinese script, which is a *different* name string from the
English catalogue. Every crosswalk below is therefore justified individually in
§1.3, not by name similarity alone.

### 1.2 The evidence classes, kept separate

Reusing the parent's classes so a weak class cannot borrow a strong one:

| Class | Source | Proves | Strength |
|---|---|---|---|
| **A′** | official board **post body**, read | a dated statement by the publisher | **primary** |
| **B′** | official board **list row** (title + author + date), body uncaptured | a dated post *existed* with that title | primary, title-only |
| **C′** | dated community post, read | a date, second-hand | secondary |

Art and manifests prove **existence of shipped assets only**. None of the below
proves a hero was playable, obtainable, or had any stat value.

### 1.3 `036` Bear — official post calls it a **newly added hunter** (2017-11-08)

**[A′ — primary, official, body read.]**

- **Post:** `[活動] Google推薦紀念, 鬥陣俱樂部特別獎勵及優勝者儀式!`
- **URL:** `http://bs.visualshower.com/event_zh/186917`
- **Archive:** [2017-12-01 capture](http://web.archive.org/web/20171201151615/http://bs.visualshower.com/event_zh/186917)
- **Body, verbatim:**
  > `為了紀念Google推薦, 本週將變更鬥陣俱樂部的獎勵`
  > `包含貝克漢最害怕的新入獵人 '熊'的痕跡及曼達`

  Translation: *"To commemorate Google featuring, this week the Fight Club
  rewards will change… it includes the traces and Manda of the **newly added
  hunter 'Bear'** that Beckhen fears most."*

  The operative phrase is **`新入獵人`** — literally "newly-entered/newly-added
  hunter". The publisher is describing `熊` as an addition, not as an incumbent.

- **Corroborating official post, same wording:** `[活動] 鬥陣俱樂部特別獎勵延長一週!`
  `http://bs.visualshower.com/event_zh/205963`,
  [2017-12-01 capture](http://web.archive.org/web/20171201151957/http://bs.visualshower.com/event_zh/205963):
  > `包括了貝克漢最害怕的新入獵人「熊」及曼達等之前沒有的豐富獎勵。`

  *"…including the **newly added hunter 'Bear'** that Beckhen fears most, and
  Manda, and other rich rewards not previously available."*

- **Post dates**, from the English board capture
  [2017-11-13](http://web.archive.org/web/20171113193027/http://bs.visualshower.com/event_en),
  which lists the same two events in English:
  - `[Event] Google featured commemoration, special Fight Club rewards!` —
    author `VSpang`, **row No. 198, dated 2017.11.08**
  - `[Event] Fight Club special rewards extended one week!` — the `205963`
    equivalent, row No. 27, dated **2017.11.15** (date from the `event_zh`
    2017-12-12 board list)

- **Crosswalk:** `熊` = "Bear" → **`036`** Bear, *"Nature's Gift"*, 3★ Defense
  Lightning ([RECOVERED] `card-catalogue.tsv`). Justification beyond name
  similarity: `036` is the only catalog row whose name is Bear/熊, and its
  context matches — a Fight Club reward containing **Bear traces** is exactly
  what `208943`'s companion post (`205963`) describes, and the local
  `bh`/community record already places Bear and Beckhen as a Fight Club pair
  (Beckhen `051`, *"Guardian of Fight Club"*).

**Conclusion: ID `036` was a NEW addition as of 2017-11-08.** This is inside the
14-week window, on a primary official record, and it is the single strongest
result in this file. It is also why no `C036` art package exists in the
Sept-2017 manifests — the art necessarily postdates them.

### 1.4 `038` Rebecca (Christmas) / "Santa Girl" — official **debut** announcement (2017-11-30)

**[B′ — primary, official board-list row; body NOT captured.]**

From the **2017-12-12** `event_zh` board capture
([raw](http://web.archive.org/web/20171212100835/http://bs.visualshower.com/event_zh)),
the four Sticky rows, verbatim:

| Board date | Author | Views | Title (verbatim) | Reading |
|---|---|---|---|---|
| **2017.11.30** | SmileV | 8479 | `[活動] 聖誕女郎麗貝卡, 登場!` | **[Event] Christmas Girl Rebecca — *debuts/appears*!** |
| **2017.11.30** | SmileV | 4090 | `[活動] 期間限定! 聖誕節組合包!` | [Event] **Limited time!** Christmas bundle! |
| 2017.12.01 | SmileV | 631 | `[活動] 艾斯特的特別提案` | [Event] Estelle's special offer — **see the conflict in §2.4** |
| 2017.12.01 | SmileV | 1068 | `[活動] 回收棒子大作戰! (17:00)` | [Event] Baseball-bat battle! |

- **`登場!`** is the standard announcement verb for *a thing coming into
  existence* — it is the publisher announcing a debut, not a rerun. That is a
  release record, not merely an existence record.
- **Crosswalk:** `麗貝卡` = Rebecca; `聖誕女郎` = "Christmas Girl".
  **`038`** Rebecca (Christmas), title **"Santa Girl"**, 3★ Offense Fire — the
  only catalog row carrying both Rebecca and Christmas. Confidence high; the
  Chinese given name and the Christmas descriptor both land on `038` and on
  nothing else.
- **Honest limit:** the body is **not** archived. CDX returns no row for
  `event_zh/225278`, `/225371`, `/226769`, `/227046` (the four Sticky ids
  present as hrefs in the board HTML) under the permalink, `?mid=` or
  domain-filter forms. So this rests on the board-list row: **title, author,
  date, view count** — real official metadata, but no body text and no in-game
  art inspected.
- **Independent consistency check (official, later):** the English post
  `event_en/995273`, **2018-09-28**
  ([archive](http://web.archive.org/web/20181021134417/http://bs.visualshower.com/index.php?mid=event_en&document_srl=995273&l=en)),
  lists `<Limited Hunters Available>` as `★3 Santa Clauster` /
  `★3 Santa Girl Rebecca` / `★2 Halloween Riko`, and describes them as *"hunters
  who are usually not recruitable will become available"*. A 2017-11-30 debut
  followed by a 2018 limited re-run fits that wording exactly, and explains why
  no `C038` art appears in the Sept-2017 manifests.

**Conclusion: ID `038` debuted on or about 2017-11-30 — inside the window.**

### 1.5 `034` "Halloween Witch" (owner `024` Riko) — Halloween **2017** (secondary)

**[C′ — secondary, but dated and read in full.]**

- **Source:** Bahamut board `bsn=33171`, thread `snA=17`,
  title 【攻略】新手入門必須知道的七件事, author 請謝謝對不起 (jordan80475),
  posted **2017-11-03 22:05:19**,
  <https://m.gamer.com.tw/forum/C.php?bsn=33171&snA=17>.
- **Body, verbatim:**
  > `萬聖節魔女莉可獲得管道:前陣子萬聖節活動推出的限時金券角`
  > `一樣是異色版 不過萬聖節活動關卡的時候, 放在隊伍裡可以提升獲得南瓜機率`

  *"Halloween Witch Riko — acquisition route: a limited-time gold-ticket
  character pushed in the **recently-held Halloween event**. She is likewise a
  colour variant; during the Halloween event stages, having her in the party
  raises the pumpkin drop rate."*

- **Dating:** `前陣子` ("just now / a little while ago") + post date
  **2017-11-03** ⇒ the Halloween event referenced is **Halloween 2017**, i.e.
  late October 2017 — **inside the window**.
- **Crosswalk:** `萬聖節魔女莉可` = "Halloween Witch Riko". **`034`** is the
  unnamed catalog row with title **"Halloween Witch"** and `owner_card_id`
  **`024`** Riko — the only such row. Also named `할로윈 마녀 리코` on the Namu
  Defender page (parent file `bahamut-thumb-2026-10-05.md` §5) and `★2 Halloween
  Riko` in the official 2018-09-28 post. Rarity `★2` agrees with catalog `024`
  Riko being 2★.
- **This resolves a specific parent-file loose end.** `roster-2017-2026-10-05.md`
  §1.5 mapped `034` to "Halloween Witch Riko" but then wrote *"`034` is out of
  roster: no 2017 art evidence."* That parenthetical was an artefact of the
  **art** channel being the only channel consulted. A Halloween **2017** release
  is exactly what the art channel cannot see.
- **CONFLICT, preserved not reconciled (§2.3).** The official post
  `event_en/1008972`, **2018-10-19**, is headed *"1. New 2018 Halloween-Limited
  Hunters!"* and lists `Jack-O'-Lantern(★3)`, `Broom Witch Denali(★3)`,
  `Halloween Witch Riko(★2)` — i.e. the publisher called all three **new in
  2018**. That contradicts a 2017 debut for Riko. Both readings are preserved:
  (a) `034` debuted Halloween 2017 and re-ran in 2018 with the wording "new"
  applied loosely to the whole limited line-up; or (b) `034` is genuinely a 2018
  hunter and the 2017-11-03 poster was mistaken. **This file does not pick.**

**Conclusion: a 2017-10 Halloween-event debut for `034` is the better-supported
reading of the in-window evidence, but it is secondary and it conflicts with
official 2018 wording. Treat `034` as in-window *probable*, not closed.**

### 1.6 `051` Beckhen — named by name in the 2017-11-08 official post (existence only)

**[A′ — primary, official, body read.]** The same official body quoted in §1.3
names `貝克漢` — **Beckhen**. The claim is only that **`051` existed by
2017-11-08**; the post is a Fight Club reward notice and says nothing about when
`051` was released, so **this is an existence bound, not a release date.**

- **Crosswalk:** `貝克漢` = Beckhen → **`051`**, *"Guardian of Fight Club"*.
  Justification: the name, plus the Fight Club setting, which is exactly what
  `051`'s recovered title says. Confidence medium-high; not proven by art.
- **Why this is load-bearing.** `051` is a high ID, and the parent's §1.7 leg 2
  argued from Miraheze release dates that `045` (9 Feb 2018) is the earliest
  dated post-`031` hero. An official Nov-2017 mention of `051` shows that
  argument **cannot be run backwards**: catalog ID order is not release order,
  and at least one ID in `039`-`051` was live well before its English-timeline
  neighbours.
- **No conflict with the community index.** `051` carries **no** date on the
  Miraheze index, so nothing is contradicted here. What *is* contradicted is any
  assumption that the `039`-`063` block is uniformly 2018+.

### 1.7 Null results inside the window, recorded so they are not re-run

| Check | Result |
|---|---|
| Official EN event-board capture after 2017-11-13 | **None.** `event_en` has no CDX row between 2017-11-14 and 2018-01-01. All in-window official evidence is therefore on the **Traditional-Chinese** board, and the EN bodies for the four Rebecca/Bear-era stickies are uncaptured. |
| `event_zh` board bodies for the 4 Sticky ids `225278`/`225371`/`226769`/`227046` | **No CDX row** under permalink, `?mid=` or domain-filter forms. Negative for those forms only. |
| `event_en` bodies `160998`, `162111`, `183604` (the EN twins of the in-window posts) | **Not archived.** Wayback returns its "has not archived that URL" page. Recorded as a query-form negative per the parent's §2.3 method note — the *Chinese* equivalents are archived, the English ones are not. |
| Official post naming a `032`-`035`, `037`, `039`-`050`, `052`+ hero, in-window | **None found.** These IDs remain unresolved, and are **not** excluded. |
| Named December-2017 official posts (2017-12-06 → 2017-12-21) | **Unobserved.** The last in-window board capture is **2017-12-12** and its newest row is **2017-12-05**. The final ~2.5 weeks of the window have no board coverage at all. |

---

## 2. UNPURE — release-date anchors and roster tokens

Everything here is **contaminated material**: player prose, community
crosswalk guesses, unresolved name leads, or readings that conflict with a
stronger source. **None of it counts toward the 70% hero / jewelry / monster
thresholds.** Also appended to
[`polluted-observations.md`](polluted-observations.md).

### 2.1 The one numeric roster anchor in the window, and why it does not reconcile

Bahamut `snA=17`, **2017-11-03**, verbatim:

> `這遊戲目前總共有36隻角色`

*"This game currently has a total of **36 characters**."*

Two candidate readings, **neither adopted**:

1. **ID-space reading.** `001`-`036` is exactly 36 catalog rows, which is a
   striking fit — but `036` Bear was announced as *new* five days **later**
   (2017-11-08, §1.3), so on 2017-11-03 the roster cannot already have been
   `001`-`036`. This reading is therefore **self-contradictory**.
2. **Player-pool reading.** "36 characters" = the recruitable pool a player saw,
   excluding NPCs, tickets and some variants. This is compatible with the
   catalogue being larger, and with §1.6 showing `051` already live.

**Verdict: unreconciled.** The token is preserved as a dated *magnitude* anchor
only. Do **not** use it to date any ID, and do not use it to argue that
`032`-`035` existed — it equally supports a pool that skipped them.

### 2.2 Regional-release finding: Miraheze dates are not global release dates

The same post, verbatim:

> `這遊戲繁中化約一個月了推出的時候是在5月`
> `所以有蠻多國外的高等玩家 不過不用怕落後其他人太多`
> `這遊戲其實早進晚進 沒有太大的差別 差別在競技場的名次跟一些異色版角色而已`

*"This game has been Traditional-Chinese-ised for about a month; when it
launched it was in **May**. So there are quite a lot of advanced foreign
players — but don't worry about falling behind… this game really doesn't care
whether you start early or late; the only difference is arena ranking and some
colour-variant characters."*

This is the methodological key to the whole window:

- The publisher launched **May 2017**, and the **Traditional-Chinese service
  opened around Oct 2017** — i.e. *inside* the window.
- Therefore a hero being live on the KR/legacy and TC services in Nov 2017 is
  **unremarkable**, while its *English* release date can be much later.
- **This explains, without contradiction, why `036`, `038` and `051` are live in
  Nov 2017 while the community index dates `045` Yuri to Feb 2018, `048` Dumble
  to Mar 2018, `049` Bright to Mar 2018 and `050` Therapy to Apr 2018.** Those
  are region/line-specific dates. Treat the Miraheze date column as
  **region-scoped and partial**, never as a global existence bound.
- It also weakens the parent's §1.4 argument that two community sources
  agreeing to the day (Dino `2018-06-29`, Apollon `2018-08-17`) "materially
  raises confidence in the release-date axis". The axis is real for one region
  and says nothing about others.

### 2.3 The `034` official-vs-community conflict, restated

| Source | Date | Wording | Reading |
|---|---|---|---|
| Bahamut `snA=17` (community) | 2017-11-03 | `前陣子萬聖節活動推出的限時金券角` | Halloween **2017** debut |
| Official `event_en/995273` | 2018-09-28 | `★2 Halloween Riko` among limited hunters | live by Sep 2018 |
| Official `event_en/1008972` | 2018-10-19 | `1. New 2018 Halloween-Limited Hunters!` … `Halloween Witch Riko(★2)` | **new in 2018** |

Preserved as a live conflict. A third possibility worth recording: `059`
Lantern (Halloween) and `060` Denali (Halloween) are the two that plausibly
debuted in 2018 (both are named in the 2018-10-19 "new" list), with `034`
re-running from 2017 — which would make the "new" wording a line-up-level claim.
**Not decided here.**

### 2.4 Unresolved name leads from the in-window official posts

| Chinese token | Post (date) | Candidate | Status |
|---|---|---|---|
| `艾斯特` "Estelle" | `event_zh` Sticky `[活動] 艾斯特的特別提案` (**2017.12.01**, SmileV, 631 views) | `096` Estelle | **CONFLICT — do not map.** Miraheze dates `096` Estelle **10 Sep 2020**, and an English `[Event] Estelle's Special Offer` exists at `990227` on **2018.09.21**. A same-titled offer in Dec 2017 most likely refers to an **NPC/shopkeeper** of the same name, not the 2020 hunter. Unresolved. |
| `貝克漢` "Beckhen" | `event_zh/186917` (**2017.11.08**) | `051` Beckhen | Mapped at medium-high confidence (§1.6) on name + Fight Club context. |
| `抽獎鼠` "Lottery Mouse" | `event_zh/194203` `[活動] 抽獎鼠大失血!` (2017.11.10), `event_zh/225275` (2017.11.30), `event_zh/234003` `[活動] 蒂蒂爾的噗通噗通箱子` (2017.12.05) | `084` Lottery Mouse | **NPC-vs-card unresolved.** The gacha mouse is a recurring board mascot; whether it is the same entity as the 4★ card `084` *"Master of Recruitment"* is **not** established. Lead only. |
| `韋斯特菲爾` "Westfield" | `event_zh/206098` `[活動] 韋斯特菲爾的訓練手套` (**2017.11.15**) | `080` Westfield | Lead. English twin `[Event] Westfield's Boxing Gloves` exists at `1003638` (2018.10.12). Community index leaves `080` **undated**. Same NPC-vs-card question as above. |
| `黑主` | Bahamut `snA=17` (2017.11.03) | *unassigned* | **Do not invent a mapping.** The post calls `黑主` the strongest attacker with *"the only skill in the game with invincible time"*, obtainable by paying to 老手等級:英雄三 (~NT$18,000), and explicitly distinguishes it from `鷹男` (= Karl Steiner `012`, "eagle man") and from `蘭索恩`. Neither `黑主` nor `蘭索恩` is crosswalked in the recovered catalogue or the Namu four-role lists. Two unassigned nickname leads. |
| `蘭索恩` | Bahamut `snA=17` (2017.11.03) | *unassigned* | As above. Paired with `阿克沙` (Akasha `008`) as a T1 support. Unassigned. |

### 2.5 In-window official rows that only re-confirm `001`-`031`

Useful as a **consistency check on the parent's roster table**, not as new IDs.
All are primary official copy inside the window:

| Post | Date | Heroes named | Crosswalk |
|---|---|---|---|
| `event_zh/139571` `[活動] 第一屆 大家來找碴!` (spot-the-difference) | event **2017-10-13 → 10-16**; body captured **2017-12-18** | `卡因`, `奧賽蘿拉`, `杰羅得`, `文森特` | Kain `029`, Acerola `030`, Gerard `005`, Vincent `010` — all `<= 031`. `文森特` (Vincent `010`) is named as attacking a character "right at the start", matching `010`'s role. **An in-window official post on 2017-10-13 already exercises four `001`-`031` hunters by name.** |
| `event_zh/194203`, `/225275`, `/234003` | 2017-11-10 / 11-30 / 12-05 | `蒂蒂爾` "Tyltyl" | `004` Tyltyl — `<= 031`. |
| `event_en` board 2017-09-14 capture (immediately **pre**-window) | — | `[Event] Diana's Growth Period` (2017.08.31), `[Event] Special Search for Octavia!` (2017.09.07), `[Event] Sunny in Midgard? … White Island x Blustone collaboration` (2017.07.18) | Diana `031`, Octavia `028`, Sunny `022` — all `<= 031`. `031` Diana getting a **dedicated growth event** dated 2017-08-31 is independent support for the parent's §1.4 release date of 31 Aug 2017. |

### 2.6 Other in-window prose already covered elsewhere — cross-reference only, not duplicated

From Bahamut `snA=17` (2017-11-03). These are **player prose**, already logged
elsehand; recorded here only so a future reader knows this single in-window
thread was read end to end:

- Evolution costs `2★ 1000 / 3★ 3000 / 4★ 12000 / 5★ 60000` — already in
  `polluted-observations.md` and `video-loose-ends-2026-10-05.md` ("2017
  evolution-cost prose"). Not re-transcribed.
- Fuel: `一天只能換一次燃料券` (one fuel-ticket exchange per day);
  `靠每4小時的體力補給` (natural fuel supply every 4 hours). **Player prose,
  PRE-2019-09-05 era.** Not a stat row. Cross-check only against the local
  `local_fuel_0` fixture — do **not** use it to set one.
- Arena: park the weakest hunter in the defence squad so points bleed. **Prose.**
- `快速出隊要耗費的曼達` (fast dispatch costs Manda). **Prose, no amount.**
- `這遊戲繁中化約一個月了` — see §2.2; this is the load-bearing line.

### 2.7 What remains open after this file

1. **`032` Scar, `033` Patrone, `035` Joy, `037`, `039`-`050`, `052`+ inside the
   window** — no dated in-window record found. Open, *not* excluded.
2. **The last ~2.5 weeks of the window** (2017-12-06 → 2017-12-21) have no board
   coverage. A hero debuting there — a second Christmas variant, say — would
   still be invisible.
3. **The `034` conflict (§2.3)** needs a `event_en/1008972` body read to settle
   whether "new 2018" covers Riko. That body is archived
   (`1008972` has a confirmed 200 CDX row per `event-board-bodies-2026-10-05.md`
   §2.1) and is the single highest-value next fetch.
4. **`艾斯特` (2017.12.01)** — NPC or `096`? Settles a real Miraheze-date
   question.
5. **`黑主` / `蘭索恩`** — two unassigned Chinese nicknames with a 2017-11-03
   date. Art crosswalk against `C0xx.jet` is the only route.
6. **No `032`+ base-stat row exists.** Every record in this file is
   existence/release evidence. Nothing here may be promoted toward the 70%
   thresholds, and nothing here says a hero was playable or obtainable.

### 2.8 Coverage statement

Unchanged by this file: **heroes 1/113, monsters 0/22, accessories 1/100.** The
sole credited hero row remains `051` Beckhen
(`analysis/catalogue/stats/051.md`), and this file does not strengthen it — §1.6
adds an *existence date* for `051`, not a stat. Roster presence is not stat
presence; any future panel for these IDs must still pass the strict gate
(visible level + rank/awakening + documented gear state) and be era-tagged
PRE/POST 2019-09-05.
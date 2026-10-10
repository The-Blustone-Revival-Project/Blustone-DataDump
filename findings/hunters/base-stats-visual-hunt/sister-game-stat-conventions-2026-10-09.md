# Sister-game stat & convention recovery (BTB / White Island) — 2026-10-09

**Question put to this lane:** Blustone's per-entity stat data is server-side and
unrecoverable from its own corpus (heroes **1/113**, accessories **1/100**, monsters
**0/22** — the last a *structural* gap, since the game shipped no monster stat
screen). A sister game by the same developer, on the same worldview, with characters
shared between them, might carry documented stat tables.

**Answer: no. There is nothing to transfer, and this is now proven rather than
assumed.** The negative is a *census* negative over complete corpora, not a
sampling one. Details, the instrument validation that licenses it, and the one
thing the sister games *do* contribute are below.

**Coverage counters are UNMOVED: heroes 1/113, accessories 1/100, monsters 0/22.**
Nothing in this note is a base stat for any Blustone entity.

---

## 1. Headline

| | BTB (비욘드 더 바운즈) | White Island (하얀섬) |
|---|---|---|
| Genre | point-and-click adventure | visual-novel / mystery thriller |
| HP / ATK / DEF anywhere | **0 hits / 26 pages** | **0 hits / 24 pages** |
| Level cap, XP curve | **0 hits** | **0 hits** |
| Damage formula | **0 hits** | **0 hits** |
| Transcendence / T1-T2-T3 analogue | **0 hits** | **0 hits** |
| Independent English wiki | yes, 26 pages, all fetched | yes, 24 pages, all fetched |

**The premise of the task is false for these two titles, and for a reason that is
itself the finding:** they are *narrative adventure* games. They have no stat
system to document. `BTB Walkthrough.docx` is a list of verbs — *"Tap the
parachute cord"*, *"Use Nene on the dodo"*, *"Drag the Fruit Skin onto the
parachute"*. There is no combat, no XP, no grading.

So the "engine conventions may transfer even where balance numbers do not"
hypothesis was worth testing — and it also fails, for the reason in §4.

---

## 2. What actually exists (provenance)

### 2.1 First-party, inside the shipped Blustone client — [RECOVERED]

The client itself carries sister-title text. `UI_JSON_RO` holds exactly
**9 records**, in all 5 locales, and **nothing else** (full audit:
`client_cross_title.out.txt`, `client_audit_full.txt`; 18,105 records scanned,
the 9 hits are the positive control that the scan works):

| key | EN | KO |
|---|---|---|
| `비욘드 더 바운즈의 세계에 오신 것을 환영합니다.\|TX_TITLE` | Welcome to the world of\nBeyond the Bounds. | 비욘드 더 바운즈의 세계에\n오신 것을 환영합니다. |
| `비주얼샤워 게임을 플레이하신 적이 있으신가요?\|TX_ACC` | Have you ever played **White Island** or **BTB** before? | **하얀섬** 또는 **BTB**를 플레이하신 적이 있으신가요? |

The other locales give the localized sister-title names, which are useful for
future searching: JA **ホワイトアイランド**, SC **白岛**, TC **白島**.

> **This is a first-party confirmation of the shared-world/prequel relationship**,
> stronger than the namu reading that started this lane. The Korean client asks
> the player whether they have played White Island or BTB; the JA/SC/TC clients
> carry the same panel. Note the panel is a *survey*, not a content claim.

> **A negative that closes an avenue:** none of those 9 records contains any
> balance vocabulary — no *level*, *exp*, *hp*, *atk*, *def*, *damage*,
> *upgrade*, *grade*, *skill*, *stat* or *cap*. **The shipped client ships zero
> sister-title stat data.** The title `Beyond the Bounds` appears 8× in the
> tables and every occurrence is a greeting string.

### 2.2 English Fandom wikis — [RECOVERED], complete

Two dedicated community wikis exist, both by the same editor, both fetched
**in full** via the MediaWiki API (not scraped, so no JS-shell artefact):

- `beyond-the-bounds-game.fandom.com` — **26/26 pages, 56,111 chars**
- `whiteisland.fandom.com` — **24/24 pages, 15,687 chars**

The BTB wiki's own mission statement: *"to be filled with the BTB story,
character profiles and walkthroughs."* It has a `Lantern` page, a `Nene` page,
a `Leonardo` page, an `Alfheimr` page, and 11 episode walkthroughs — and that
is the complete universe of it.

Both character pages quote the **official site** (`btb.visualshower.com/character_en`),
which is why they count as better than pure fan invention.

### 2.3 First-party BTB site, in the archive — [RECOVERED that it exists; NOT retrieved]

Wayback has **132 distinct URLs** under `btb.visualshower.com`, including
exactly the pages that would answer this lane (verified against the saved CDX
census, `net/btb_site_urls.json`):

```
/character_ko   20180106072559   text/html
/game_ko        20180105185719   text/html
/help_desk_ko   20180106072644   text/html
/world_ko       20180106073739   text/html
/event_ko       20180106072620   text/html
```

They are **first-party BTB documentation** and remain unfetched. The replay
endpoint returned **HTTP 429 "suspected abusive bot traffic"** on every attempt
including a control that this project has fetched successfully before. Per the
guard, that is an **instrument fault, not a content negative**, and I stopped
rather than record a zero. **The CDX endpoint kept working** (200) while replay
did not, which is why the URL census above exists but the bodies do not.
Evidence: `net/btb_site_urls.json`, `net/btb_site/_fetch_log.json`.

> **This is the one open door.** A future lane with a working archive route
> should read `character_ko` and `game_ko` first. Given BTB is an adventure game
> (§3) the prior expectation is low, but it is an expectation, not a measurement.

### 2.4 The VSFan corpus, already in the workspace

`analysis/VSFan/Research/Beyond the Bounds/` holds first-party-adjacent
material that had not been read for this purpose:

- `BTB Characters.docx` — Lantern, Nene (bare, no stats), Dodo, Albert, "Strange Machine"
- `BTB Walkthrough.docx` — pure adventure verbs, **no stat anywhere**
- `White Island/Overview.docx` — the key genre statement, quoted in §4

---

## 3. Genre evidence (the reason the census is empty)

**BTB Walkthrough.docx**, complete:

> Tap the parachute cord · Tap 3 times on the flying object · Pick up the
> Aerodynamics book · Use Nene on the dodo · Use the book on the Dodo · Drag the
> Fruit Skin onto the parachute · Tap the white orbs in the following order:
> Bottom Right, Middle Left, Upper Right, Upper Left · Talk to Albert using the
> speech icon on the right

**White Island/Overview.docx:**

> Mystery thriller with a supposedly highly rated story.
> Two primary modes -> Exploration (item combining, item usage, conversation
> with stranger, puzzling) + Story (text conversations)

**BTB Characters.docx** — the entire character list, verbatim:

> Lantern / Nene / Spontaneous / Can talk to Animals / Dodo / Lost his glasses /
> Albert / Seems to have been searching for Edison on behalf of Lady 4994 /
> Strange Machine / Unknown. A scouting device?

Seven entries, none with a stat line. Compare the Blustone equivalent, which is
113 heroes × 13 numeric fields.

**The Fandom BTB pages are likewise purely narrative.** `Nene`: *"she is very
strong — her muscles are like steel"*, *"she can communicate with any animal
freely and perfectly"*. `Lantern`: *"he's an amazing shot with a sniper rifle."*
These are **character descriptions, not numbers**, and must not be read as
stat evidence. "Very strong" is not a DEF value.

**One BTB screenshot** (`btbr/139304466353082cb7bb23f.png`) does show a HUD with
`Level 50` and counters. **Caution: that screenshot is not BTB gameplay.** It is
from VisualShower's *Smart Choice* / telecom service advertorial material — the
companion images are `DAILY NEWS` "smartphone recommendation" spreads with
`SK 테드azos 서비스` and `VisualShower` branding, promoting a *Beyond the Bounds*
novel tie-in (*푸른돌 조건사 / The Secret of Blue Stone*). The `Level 50` UI
belongs to an unrelated product in the advert. **Do not cite it as a BTB stat
screen.** Recorded because a reviewer will find it in the same folder.

---

## 4. Convention vs balance — the part that matters

The task asked me to separate *convention* (engine-level) from *balance*
(per-title). Here is the honest answer.

### 4.1 What is genuinely shared = **[RECOVERED] worldview, not systems**

`White Island/Overview.docx` is explicit about the engine lineage:

> **Beyond the Bounds** — Similar to White Island in style, **also runs the
> White Scripting Engine** … Precedes Blustone … A lighter adventure than
> White Island … Assets and story derived from the original Beyond the Bounds trilogy

Read precisely: **BTB and White Island share a scripting engine with each
other. Blustone is named separately and is not said to run it.** Blustone is
described in the same document as *"A mash between tapper/clicker games and RPG
elements"* — a different genre class from both sisters.

Corroborating from VisualShower's own company history (`Sources.docx`, from
`gamejob.co.kr` / `jobkorea.co.kr` / `jobplanet.co.kr`):

> 2010 04 "Beyond the bounds" synchronously launched in all domestic carriers
> 2013 03 "Beyond the Bounds: Escape" has been launched in all app markets
> 2014 01 "Beyond the Bounds : The secret of blue stone" … 2014 06 … "Project BTBR"
> 2015 11 Global Gaming Platform, "PV" officially released

Blustone runs on **PV**, VisualShower's own global platform, released 2015-11 —
*after* BTB's titles. The sisters predate the platform and use the older
scripting stack.

**⇒ So the shared thing is the *story world and the art pipeline*, and the
unshared thing is the *game system*. There is no shared stat convention to
inherit.** A shared developer is not a shared formula; here it is provably not
even a shared engine.

### 4.2 Classification table

| candidate | status | reason |
|---|---|---|
| Worldview / lore / character reuse | **[RECOVERED] transfers** | first-party client panel + namu + Fandom |
| `Lantern`/`Nene` identity | **[RECOVERED] transfers** | §5, four-way agreement |
| Ornithopter as an in-world object | **[RECOVERED] transfers** | client has 4 `Ornithopter Fuel` strings |
| HP/ATK/DEF schema | **does NOT exist in the sisters** | 0 hits / 50 pages |
| Level cap, XP curve | **does NOT exist** | 0 hits |
| Damage formula | **does NOT exist** | 0 hits |
| Star/grade tier system | **does NOT exist** in the sisters | BTB 5 hits, all map/floor names; WI 0 |
| Transcendence T1–T3 | **does NOT exist** | 0 hits in either |
| White Scripting Engine | **shared by BTB + WI only, NOT Blustone** | Overview.docx |

### 4.3 Consequences for the open questions

- **The Lv.30-vs-"max 20 before advance" contradiction is untouched.** The
  sisters cannot arbitrate it: they have no hunter levels at all. The
  contradiction remains exactly where §187 left it, still unresolved.
- **The flat XP fixture stays a fixture.** No sister curve exists.
- **T2 remains unmeasured, and this lane does not help.** `t1-measured-1.0994`
  is still the highest-value missing observation. No analogue system was found
  in either sister to reason from.

---

## 5. The shared-cast agreement check

`Lantern` and `Nene` are Blustone hunters `001` and `003`. BTB is a **different
game**, so this is an *independent* attribution path: Korean fan wiki (current)
+ English fan wiki (2019) + Japanese official archive (2019) + the shipped
client.

### 5.1 Sources compared

| field | namu.wiki (KO, live) | vsfan wiki (EN, 2019) | 2019 JP archive | shipped client |
|---|---|---|---|---|
| **Lantern `001`** grade | ★★★ | ★★★ | rarity 3 | — |
| **Lantern `001`** element/attribute | 화속 | **Fire** | 火炎 (fire) | — |
| **Lantern `001`** role | (not in the roster table) | **Bomber** | 爆撃手 (bomber) | `JOB_GUN` → **Bomber**; `CHAR_STR` "The **Bomber** who…" |
| **Nene `003`** grade | ★★★ | ★★★ | rarity 3 | — |
| **Nene `003`** element/attribute | 수속 | **Ice** | 冷気 (ice) | — |
| **Nene `003`** role | — | **Defense** | 守備手 (defence) | `JOB_DEF` → **Defense**; `CHAR_STR` "The versatile and persistent **Defense**…" |
| **Mowgli `002`** grade | ★★ | ★★ | rarity 2 | — |
| **Mowgli `002`** element | 전속 | **Electric** | 電撃 (lightning) | — |
| **Mowgli `002`** role | — | **Offense** | 攻撃手 (offence) | `JOB_ATT` → **Offense** |

### 5.2 The attribute vocabulary is proven, not assumed

The Korean attribute tokens had to be mapped to English elements. I did **not**
assume it. Joining the Korean roster to the English roster on name equality
returns **0 rows** — the Korean table is entirely Hangul-named. That is a
**false zero** and I discarded it.

Instead: the join instrument was validated on a control (English-against-itself,
**55/55 rows**), then a **declared manual join** was made on the given-name
token, with every row listed in `attr_correspondence2.txt`. Result over **21
joined heroes**:

```
수속 -> Ice          전속 -> Electric        화속 -> Fire
CONFLICTS: 1 over 21 joined heroes
```

The single conflict is **`Pansy`**: namu 화속/Fire vs the vsfan infobox
Electric. **This is pre-existing and already documented in this project** —
`vsfan-wiki-2026-10-05.md` §2.5 records "Pansy element: wiki says Electric,
two sources say Ice", with the vsfan infobox as the outlier *and* a note that
the same wiki's own navbox files Pansy under Ice. My join **surfaced** this
known discrepancy; it did not create one.

⇒ **The token→element correspondence is established by 20 consistent rows plus
one independently-known exception**, and it is a 3-value total function, not a
guess.

### 5.3 Result

**Full agreement on all three cross-title heroes. Zero new conflicts.**

- `001` Lantern — grade ★★★, **Fire**, **Bomber**: namu / vsfan / JP / client all concur.
- `003` Nene — grade ★★★, **Ice**, **Defense**: namu / vsfan / JP / client all concur.
- `002` Mowgli — grade ★★, **Electric/Lightning**, **Offense**: namu / vsfan / JP / client all concur.

**This is identity corroboration only.** It adds a fourth and fifth independent
voice to rows that already carried three, on fields already believed settled.
**It moves no coverage counter and licenses no base stat.**

### 5.4 One useful side-finding

The cross-title cast is **larger than the two the wiki headline names.** The
Korean roster shows **Mowgli `002`** (*"비욘드 더 바운즈에도 출현했다"* — also
appeared in BTB), **Chichir `004`** (*"비욘드 더 바운드에서도 등장했고 … 화속
힐러다"* — appeared in BTB, a fire-attribute healer), and **Leonardo** (Lantern's
grandfather, *"BTB에서도 초반 스토리에 출현했었다"*). The BTB Fandom wiki's
`Nene` page independently confirms the Polar Bear Tribe, matching the Blustone
roster's `Polar Bear` race value for `003`.

> The namu hunter page also contains an **unresolved transclusion into the BTB
> article** — `include(틀:상세 내용, 문서명=비욘드 더 바운즈)` — which means the
> Blustone wiki page is *incomplete* and pulls a paragraph from the BTB page.
> Reading the BTB page would complete it. Blocked by §2.3.

---

## 6. What would change the answer

Stated so the next lane does not redo this:

1. **Fetch `btb.visualshower.com/character_ko` and `/game_ko`** from the archive
   when replay is not rate-limited. First-party, currently unfetched.
2. **Read the namu `비욘드 더 바운즈` article in a browser.** Requires the desktop
   browser; it was disconnected for this whole lane. That page also supplies the
   missing transcluded paragraph for the Blustone hunter page.
3. **Search for any *other* VisualShower RPG.** `Sources.docx` lists ~25
   properties. If one of them is an RPG with a stat screen, it — not BTB — is the
   right cross-title vein. The Fandom main page calls White Island *"another RPG
   game"*, so that label is loose and the genre question is not fully closed.

---

## 7. Honesty and instrument notes

- **Every zero in this note is a census zero over a complete corpus** (26/26 and
  24/24 pages, all page titles enumerated before fetching), not a sampling result.
- **Positive controls were run and passed** before any negative was recorded:
  the balance-vocabulary scan returns **66 hits** against the 2019 archive TSV
  (BTB census) and **65** (White Island census) using the identical patterns
  that return 0 against the sister wikis. The client audit returns its 9 known
  positives out of 18,105 records.
- **Two false zeros were caught and discarded**, both by this lane:
  (a) the name-equality join that returned "0 conflicts" from **0 rows**;
  (b) an early archive positive control that returned 429 — which is why the
  BTB site bodies are recorded as *not retrieved* rather than *absent*.
- **Browser unavailability** (`browser.disconnected`, repeated) blocked the namu
  article; plain HTTP to namu returns 403 as previously recorded. Not a content
  negative.
- **Cross-title inference is quarantined.** §2.1 and §5 are *worldview/identity*
  claims and are marked as such. **No number from either sister title is
  presented as a Blustone number, and none exists to present.** The one
  quantitative-looking artifact found (a `Level 50` HUD) was traced to an
  unrelated advertisement and is explicitly excluded in §3.
- Korean, Japanese and Chinese text is preserved verbatim. Files written with
  Python `encoding='utf-8'`, `newline='\n'`.
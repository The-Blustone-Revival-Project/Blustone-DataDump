# Namu gear pages — the last credentialed path, opened and exhausted (2026-10-07)

**Lane:** accessory/equipment stat lines. Accessory coverage is 1/100 and this was
the single named blocker in `miraheze-equipment-stats-2026-10-06.md` §5.

## 0. Result, stated plainly

**Equipment stat lines recovered: 0. Accessory coverage stays 1/100. Not inflated.**

**But the gate is no longer a gate.** The prior lane recorded "namu 403 live,
unarchived" and marked it as the one external blocker. That is now superseded on
both halves:

| claim before | status now | evidence |
|---|---|---|
| namu gear pages cannot be fetched | **FALSE** — all four per-role gear pages retrieved in full, on **4 independent mirrors** | §1, 16 retrievals, 8.6–12.7 K chars each |
| namu gear pages are unarchived | **still true, now exhaustively** | §4: the entire `namu.wiki/w/블루스톤*` Wayback namespace is **one** row, and it is a 403 block page |
| namu *might* hold the numbers | **FALSE** — the pages were read in full and hold **no equipment value at all** | §2, §3: 165 equipment slots, 6 named items, **0** values |

The blocker did not move. It **closed as a negative**, with a positive control in
the same run for every step.

**What did come out of it, and is not coverage:** the first **language-matched
(KO↔KO)** independent confirmation of the shipped gear identity table. 6/6 of the
namu Korean item names map exactly onto `analysis/catalogue/data/cards.json`
(§5). That raises *confidence in identity*, which was never the shortfall.

---

## 1. Gate 1 — crawler-spoofed fetch: **PASSED**

A realistic Chrome `User-Agent` plus `Accept`, `Accept-Language`, `Sec-Fetch-*` and
`Accept-Encoding: gzip, deflate`, non-ASCII percent-encoded, referer sent where a
referer exists. Verification was by **decoded bytes**, never by status.

| host | result | gear pages |
|---|---|---|
| `d.namu.moe` | 200 | 4/4 |
| `dark.namu.moe` | 200 | 4/4 |
| `m.namu.moe` | 200 | 4/4 |
| `seore.org` | 200 | 4/4 |
| `namu.wiki` (canonical) | **403** (Cloudflare, 5,483 B block page) | 0/4 |
| `namu.se` | **404** (34,065 B theme 404, page absent on this host) | 0/4 |

**Transcription rate: 16 retrievals of 4 distinct gear pages attempted across 6
host variants.** The 4 pages are `블루스톤/헌터/{공격수, 수비수, 폭격수, 도우미}`
(Offense / Defense / Bomber / Support — literally the four per-role gear pages the
miraheze wiki cites).

Decoded sizes, per mirror, for the Offense page: 146,005 B (d) / 146,833 B (dark) /
146,001 B (m) / 156,933 B (seore), 110,941 / 111,732 / 110,933 / 126,505 characters,
17,436 / 17,454 / 17,438 / 15,114 Hangul syllables. **U+FFFD = 0 in every file.**

Whole-run tally (88 recorded URL attempts): **36 HTTP 200 with >2,000 decoded
bytes**, of which 23 are gear-page retrievals (16 distinct + 4 `?action=raw`
duplicates + 3 repeats). Non-200: 403 ×5, 404 ×16, 503 ×4, 429 ×3, transport −1 ×7.

`?action=raw` is **ignored** by all mirrors — the byte counts are identical to the
plain URLs, so there is no hidden wikitext layer to read.

---

## 2. The pages were actually read — and they carry no equipment value

Not inferred from a skim: a slot-label census over the extracted text.

| page | heroes | equipment slots | slots with a named item | **slots with a stat value** | skill-effect slots | skill-effect slots filled |
|---|---:|---:|---:|---:|---:|---:|
| 공격수 Offense | 19 | 57 | **6** | **0** | 108 | 6 |
| 수비수 Defense | 14 | 42 | 0 | **0** | 88 | 1 |
| 폭격수 Bomber | 9 | 27 | 0 | **0** | 74 | 0 |
| 도우미 Support | 13 | 39 | 0 | **0** | 91 (label spelled `특기효과`) | 0 |
| **total** | **55** | **165** | **6** | **0** | 361 | 7 |

Verbatim the six rows that have anything at all (from `d.namu.moe/w/블루스톤/헌터/공격수`,
section `2.1.1 쾌속의 검술가 라피스` and `2.1.2 사라지지 않는 노병 실베스터`):

```
무기   : <flavour prose>                서리 장도
방어구 : <flavour prose>                밀리터리 탱크탑
장신구 : <flavour prose>                인연의 매듭
무기   : <flavour prose>                아이언 너클
방어구 : <flavour prose>                방한용 점퍼
장신구 : <flavour prose>                아이언 백
```

That is **slot + flavour + item name. No number, no level.** The remaining 159
equipment slots are empty templates — the literal text `무기:` / `방어구:` /
`장신구:` with nothing after them.

Also read, all four mirrors, all `U+FFFD = 0`: the hunter root page
(`블루스톤/헌터`, 113,750 chars / 25,745 Hangul), the main page
(`블루스톤`, 72,435 / 19,356), the item guide (`블루스톤/아이템`, 63,488 /
11,748), `블루스톤/캐릭터` (110,198 / 24,910), `블루스톤/이야기/{성장기록, 인연}`,
`블루스톤/헌터/이야기`, both categories, plus 4 `파일:` pages.

### 2.1 The decisive internal contrast

The same pages **do** carry numbers, in the very next section. On the Offense page,
**6 of 108** `특기 효과:` slots are filled, and they look like this:

```
특기 효과: 지속 시간 0.51~1.00초
특기 효과: 피해량 ~9046
특기 효과: 공격 속도 ~20.00%
특기 효과: 방어력 ~30.00%
특기 효과: 막기 확률 ~30.00%
```

So the editors of this page transcribe max-level numbers — including
non-round ones no fixture would produce, `피해량 ~9046` — and left **every one of
the 165 equipment slots valueless**. This is the **same structural finding** the
prior lane recorded for the two English-language communities (miraheze 1,567
revisions / vsfan 911 pages), now confirmed at the original-language source and
from four independent hosts. Three communities, three languages, one gap.

### 2.2 The empty-value slots are a real gap, not a mirror artefact

This mattered, because the mirror could plausibly have been dropping values. Two
independent scrapes of the same page (`d.namu.moe` and `seore.org`, different
HTML converters, different class names, different byte counts) produce the **same
gap with the same signature** — a grade badge span with a background colour and
**no text inside it**, then the effect label with a trailing space and nothing
after it:

```html
d.namu.moe : <span style="color:#FFFFFF; background-color:#309eab;">
             <span style="color:#FFFFFF; background-color:#f1385a;"><br>
             <div class='quote'><strong>…description…</strong></div><br>특기 효과:</li>
seore.org  : <div class="wiki-paragraph"><br><span style="color:#FFFFFF;background-color:#309eab"></span>
             <span style="color:#FFFFFF;background-color:#f1385a"></span></div>
             <blockquote class="wiki-quote">…</blockquote>
             <div class="wiki-paragraph">특기 효과: </div></li>
```

Both mirrors render `특기 효과:` with **nothing following it**. A converter that
dropped content would not drop it identically in two unrelated renderers. The
source page has the slot and no value.

---

## 3. Detector, and its controls

`GUARD`-compliant by construction: **no hand-written Hangul codepoint anywhere.**
The slot labels (`무기`, `방어구`, `장신구`), the skill-effect label and the stat
words (`공격력`, `방어력`, `재생력`, …) are all **discovered from the fetched text
at runtime**; the slot trio is the *intersection* of the single-word labels over
the 16 pages that carry a full slot set, so the Support page's different markup
cannot smuggle `특기효과` into the equipment slot set. (My first detector attempt
did hand-write codepoints and produced mojibake labels and a false `0` — GUARD
rule 13 caught it. Rebuilt before any result was recorded.)

Both tools were re-run after the fixes in §7; the figures below are that run's
output, and **control failures: 0**.

**Positive control — 12 synthetic stat lines, all FIRED, 0 silent:**

```
장신구  강화능력 260          장신구  공격력 260          장신구  막기능력 260
장신구  방어력 260             장신구  재생력 260          장신구  전투력 260
장신구  HP 260                 장신구  ATK 1,025           장신구  defense 150
Accessory | Jack | Increases HP 260          강화능력 30.00%
EQUIPMENT+STAT control                                  FIRED
```

**Negative control — 4 real prose lines from the page: all SILENT.**

**Scan result, `B2 = slot + stat word + value`:**

| page | (A) equipment slots | slot + any number | (B) any stat-value line | **(B2) SLOT+STAT+VALUE** |
|---|---:|---:|---:|---:|
| g-d-공격수 | 57 | 2 | 29 | **0** |
| g-d-수비수 | 42 | 1 | 17 | **0** |
| g-d-폭격수 | 27 | 1 | 6 | **0** |
| g-d-도우미 | 39 | 0 | 28 | **0** |
| g-seore-공격수 | 57 | 2 | 28 | **0** |
| g-seore-수비수 | 42 | 1 | 17 | **0** |
| g-seore-폭격수 | 27 | 1 | 6 | **0** |
| g-seore-도우미 | 39 | 0 | 28 | **0** |
| g-m-공격수 | 57 | 2 | 29 | **0** |
| g-m-수비수 | 42 | 1 | 17 | **0** |
| g-m-폭격수 | 27 | 1 | 6 | **0** |
| g-m-도우미 | 39 | 0 | 28 | **0** |
| g-dark-공격수 | 57 | 2 | 29 | **0** |
| g-dark-수비수 | 42 | 1 | 17 | **0** |
| g-dark-폭격수 | 27 | 1 | 6 | **0** |
| g-dark-도우미 | 39 | 0 | 28 | **0** |
| ctrl-d-hunter (헌터 root) | 0 | 2 | 13 | **0** |
| it-d-아이템 | 0 | 0 | 2 | **0** |
| ns-d-캐릭터 | 0 | 2 | 13 | **0** |
| ns-d-성장기록 | 0 | 0 | 0 | **0** |
| ns-d-인연 | 0 | 0 | 0 | **0** |
| ns-d-헌터이야기 | 0 | 0 | 0 | **0** |
| ctrl-d-main | 0 | 0 | 2 | **0** |
| cat-d-분류 / cat-d-헌터분류 | 0 | 0 | 0 | **0** |

**Every (B) hit is a skill value or a prose percentage.** The handful of
"slot + any number" hits are flavour text, e.g. Sylvester's
`"30년 전에는 불티나게 팔리던 점퍼였어!!"` — the *30 years*, quoted verbatim in
the English shipped row too.

The item guide `블루스톤/아이템` was read in full specifically because it is the
most likely home of a per-item table, and it is not: §4.3/§4.4 is equipment
**enhancement cost** material (levels 1–50, element material, toolbox counts,
rupees), §5 is `헌터 흔적` — per-hero trace **descriptions** only, and §6 is
coupons/tickets/fishing. **No accessory stat table exists on the page.**

---

## 4. Gate 2 — Wayback: still a real negative, now exhaustive

Per the GUARD: exact-URL CDX, `output=text`, plus the availability API, plus
host variants, plus a literal-UTF-8 URL form, **with a control in every batch**.

**Control, same batch, 200 / 369 bytes:**
```
net,vsfan)/wiki/beckhen 20190821024308 https://vsfan.net/wiki/Beckhen text/html 200 … 15698
net,vsfan)/wiki/beckhen 20191015110420 https://vsfan.net/wiki/Beckhen text/html 200 … 15697
net,vsfan)/wiki/beckhen 20191216084944 https://vsfan.net/wiki/Beckhen text/html 200 … 15750
```

**Exact-URL CDX — 0 rows each:** `namu.wiki/w/블루스톤/헌터/{공격수, 수비수, 폭격수, 도우미}`,
`namu.wiki/w/블루스톤/헌터`, `namu.wiki/w/블루스톤/아이템`,
`bs.visualshower.com/ko/1203855`, `bs.visualshower.com/event_ko/1196487`, and the
`namu.se` / `d.namu.moe` / `seore.org` / `en.namu.wiki` host variants.

**Prefix sweep — the whole namespace is one row, and it is a block page:**
```
wiki,namu)/w/블루스톤/이야기/인연 20250905132445
https://namu.wiki/w/블루스톤/이야기/인연 text/plain 403 … 1021
```

**Availability API:** HTTP **429** (rate-limited) for all three queries — an
unusable instrument in this run, and per the GUARD not to be trusted anyway for
`?`-query URLs. Not used as evidence.

So: the prior lane's zero is **confirmed**, and widened from four URLs to the
entire `namu.wiki/w/블루스톤*` subtree. `namu.wiki` is effectively unarchived; the
one capture is a 403 block page.

---

## 5. The one real find — a KO↔KO identity confirmation (NOT coverage)

The six namu Korean item names crosswalk **exactly** onto the shipped catalogue,
and this is the **first language-matched** confirmation in the project. Every
previous confirmation (`charstr-items-2026-10-06.tsv`, vsfan's 33 English names)
was English-vs-English or name-vs-number.

| page / hero | namu KO (live, this lane) | `cards.json` EN | hero id |
|---|---|---|---|
| 공격수 2.1.1 라피스 · 무기 | 서리 장도 | **Frost Sword** | 017 |
| 공격수 2.1.1 라피스 · 방어구 | 밀리터리 탱크탑 | **Military Tank Top** | 017 |
| 공격수 2.1.1 라피스 · 장신구 | 인연의 매듭 | **Destiny Knot** | 017 |
| 공격수 2.1.2 실베스터 · 무기 | 아이언 너클 | **Iron Knuckles** | 006 |
| 공격수 2.1.2 실베스터 · 방어구 | 방한용 점퍼 | **Thermal Jumper** | 006 |
| 공격수 2.1.2 실베스터 · 장신구 | 아이언 백 | **Iron Bag** | 006 |

**6 of 6 exact**, including the non-obvious 방한용 점퍼 ↔ *Thermal* Jumper. The
flavour prose matches line for line too — namu `실베스터의 눈빛이 슬퍼 보입니다`
is the shipped `somehow he has sad eyes when he says this`.

Crosswalked against the accessory table itself, column 5 `accessory_ko`:

```
HIT   인연의 매듭  -> num 017 | en Destiny Knot | ja 想い出の飾り紐
HIT   아이언 백   -> num 006 | en Iron Bag      | ja アイアンバック
MISS  서리 장도 / 밀리터리 탱크탑 / 아이언 너클 / 방한용 점퍼
```

The four misses are **not** misses — `charstr-items-2026-10-06.tsv` carries
localised names for the **accessory column only**; `weapon_en` and `armor_en` have
no KO/JA/SC/TC counterpart. So the shipped table can identify accessories in any
language but weapons and armour only in English. That is a property of the
recovered table, worth recording and not a contradiction.

The hero↔row correspondence also holds: accessory row `num` **is** the hero id
(017 → Lapis, 006 → Sylvester), consistent with the independently confirmed
Lantern→001, Tyltyl→004, Beckhen→051, Apollon→055, Pansy→057 mapping in
`miraheze-equipment-stats-2026-10-06.md` §4.1.

**This is identity, not value.** No `Max HP`, no level basis, no stat. It does not
move 1/100 and is not counted anywhere.

---

## 6. Gate 3 — images and local archives: also closed

### 6.1 Two per-hero equipment **screenshots** exist on namu

Enumerated from the gear pages: 28 `파일:` links, of which three are literally
equipment screenshots:

```
파일:블루스톤/캐릭터/춤추는 검 벨라 장비.jpg
파일:블루스톤/캐릭터/베테랑 군의관 레온의 장비.jpg
파일:블루스톤 소피아 장비.jpg
```

Their **description pages fetched 200** (7,043 / 7,146 / 6,600 B). All three are
metadata-only: image description `모바일 게임, 블루스톤 에 등장하는 캐릭터 의 장비.`
and a source line — **`https://bs.visualshower.com/ko/1203855`** (Bella, Leon) and
**`https://bs.visualshower.com/event_ko/1196487`** (Sofia). Two of those are
**official VisualShower pages hosting the game's own equipment screenshot**, which
would be exactly the evidence this lane needs. Both are unreachable:

```
https://bs.visualshower.com/ko/1203855          TLSV1_ALERT_INTERNAL_ERROR
https://bs.visualshower.com/event_ko/1196487   TLSV1_ALERT_INTERNAL_ERROR
http://bs.visualshower.com/ko/1203855           503 (51 B)
http://bs.visualshower.com/                    503 (51 B)
http://www.bs.visualshower.com/ko/1203855      503 (51 B)
CONTROL, same tool, same batch: d.namu.moe/w/블루스톤/헌터/공격수 -> 200, 146,005 B
```

The image bytes themselves: the mirrors serve a **placeholder** hash
(`1e65310905e0…`, byte-identical across all three files, `data-original` pointing
at `file.namu.moe`), and the real host returns:

```
https://file.namu.moe/file/1e653109…  ->  503
```

This reproduces the 2026-10-05 finding (`namu-tables-2026-10-05.md` §7) with a
live positive control. **Not a new negative: a re-confirmation with a control.**

### 6.2 Local material: nothing

- `analysis/VSFan/` — 8,551 files; the four Korean gear names and the token
  `namu` appear in **0** text-ish files (`.txt/.json/.xml/.md`). Zero namu material.
- The 4 PDFs / 7 DOCX / 1 XLSX in `analysis/VSFan/Research/` — the three
  "Beyond the Bounds" DOCX that could plausibly hold gear tables were extracted
  (`word/document.xml`) and scanned: **12, 30 and 1 paragraphs; 0 gear-ish
  paragraphs, 0 stat-value paragraphs, 0 gear+number paragraphs.**
  `Hunter Stats [BROKEN IGNORE].xlsx` remains the already-adjudicated gear-ambiguous
  corpus with 0 strict coverage.
- `recovered-assets/` — 604 text-ish files scanned for
  `increases (max) (hp|attack|defen)` / `accessor(y|ies) (increase|bonus)`:
  **0 hits.**

---

## 7. Honesty statement

- **Equipment stat lines recovered: 0. Accessory coverage stays 1/100**
  (`Jack`, `Max HP 260 @ Lv.50`, from the FAQ panel, per the prior lane).
  Nothing in this note is an accessory stat.
- **The gate opened and the room was empty.** The prior lane's blocker was real
  (namu 403s a crawler) but its *content* hope was not: the pages were read, all
  165 equipment slots were enumerated, and none carries a value. This is a
  stronger negative than before, because it is now a **content** result measured
  with a validated detector, not an access result.
- **Every zero in this note is controlled.** Gate 1's control: the same fetcher
  returned 146,005 B for the Offense page in the same run as the 503s.
  Gate 2's control: vsfan CDX returned three 200 rows (15,698 B) in the same run.
  Gate 3's control: `d.namu.moe` 200/146,005 B in the same batch as the
  `file.namu.moe` 503 and the `bs.visualshower.com` failures. The detector's
  positive control fired 12/12 with 0 silent; its negative control was silent 4/4.
- **Three of my own instruments were broken and were caught before any zero was
  recorded**, which is the reusable content of this lane:
  1. **`dechunk` clobbered gunzipped content.** `namu.moe` answers with
     `Content-Encoding: gzip` **and** `Transfer-Encoding: chunked`. My first
     dechunker ran on already-gunzipped HTML, failed to parse a hex chunk length,
     and returned `b""` — producing **HTTP 200 / 0 bytes for every single mirror**,
     which reads exactly like a wall or an empty page. Now guarded by
     `is_chunked()` (a real chunk header must be present).
  2. **Hand-written Hangul codepoints** (GUARD rule 13) in the first detector —
     mojibake labels, and a `0` that meant nothing. Every term is now discovered
     from the page.
  3. **Support-page markup, and it bit *both* tools.** `도우미` spells the effect
     label `특기효과` (no space), so a top-3-by-frequency label heuristic read it
     as an equipment slot. `equip_extract` reported 117 Support "slots" instead of
     39; `statdetect` reported 26 instead of 39 (its `discover()` returned only the
     top 3, dropping a real slot). Both now take the intersected trio directly, and
     both independently return **39**. Lesson: a "top-N by frequency" heuristic is
     not a schema; intersect across the corpus and assert the count you expect.
- **I did not use the availability API as evidence** (HTTP 429 this run) and I did
  not use any host's search as an oracle.
- **ERA caveat carried forward:** the namu pages are undated except for
  enhancement "added 6/22" (year unstated). Nothing here is dated against the
  2019-09-05 rebalance, because nothing here is a value.
- **§5 is genuine recovered data and is deliberately not counted.** It confirms
  identity, and identity was never the shortfall. The shortfall is that **no
  Blustone community ever transcribed an equipment stat number**, in any language,
  in any of the sources now exhausted: namu (Korean, 4 pages, 4 mirrors), the
  miraheze wiki (English, all 1,567 revisions), vsfan (English, 911 pages). The
  game itself displayed one — `Max HP 260` at Lv.50 — which places the original
  table on the dead server, consistent with the recovered protocol
  (`/reference/GetItem` → `CSRItemInfo::SetItem`).

---

## 8. What is now provably exhausted, do not redo

1. **namu live text**: the 4 per-role gear pages, on 4 independent mirrors, read
   in full. 165 equipment slots, 6 named items, 0 values.
2. **namu remaining namespace**: `블루스톤/헌터`, `블루스톤/아이템`,
   `블루스톤/캐릭터`, `블루스톤/이야기/{성장기록, 인연}`, `블루스톤/헌터/이야기`,
   both categories, the main page. All read. No equipment stat anywhere.
3. **`?action=raw`** is ignored by every mirror — there is no hidden wikitext layer.
4. **namu in Wayback**: the whole `namu.wiki/w/블루스톤*` subtree is one row and it
   is a 403 block page. Control (vsfan) green in the same run.
5. **namu images**: placeholder hash on the mirrors, `file.namu.moe` 503. The
   official `bs.visualshower.com` pages the file descriptions cite are TLS-dead and
   HTTP-503. Re-confirmed with a live control.
6. **Local archives**: VSFan (0 namu references, DOCX/XLSX adjudicated empty),
   `recovered-assets` (0 hits in 604 text-ish files).

**Instrument traps added by this lane, for the GUARD file:**

- **A `gzip` + `chunked` double-encoded response will silently read as
  `200 / 0 bytes`** if dechunk runs after gunzip. Always verify decoded bytes, and
  assert `n_chars > 0` before believing a 200.
- **namu mirrors serve 200 for absent pages** — no, corrected: absent pages return
  a real 404 (2,3xx B with Hangul error text) and `/헌터/` with a trailing slash is
  a 404. But `?action=raw` is accepted with **200** and returns the *rendered* page,
  so a "raw fetch succeeded" reading can be wrong about its own content type.
- **Two mirrors, two converters, same gap** is how to prove an empty value slot is
  editorial rather than a fetch artefact. Worth reusing.

**Still open, and cheap for whoever picks it up:** the three official
`bs.visualshower.com` URLs (`/ko/1203855`, `/event_ko/1196487`, and siblings) are
the only known pointers to *the game's own* equipment screenshots. They are dead at
the origin and unarchived, but they were never tried in a Korean mirror
(web.archive.org Korean collections, `commoncrawl.org` index, or the Internet
Archive's `web.archive.org` **item-level** crawls of visualshower). That is a
different archive class from the two already exhausted.
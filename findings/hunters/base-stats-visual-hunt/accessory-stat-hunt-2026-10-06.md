# Accessory / equipment item stat lines — hunt of 2026-10-06

**Goal.** Recover individual accessory (and weapon/armour) *item stat lines*: what
the item is, which stat it grants, the value, and the level basis for that value.

**Verdict: 0 new accessory stat lines recovered. Coverage stays 1/100.**

This is a controlled negative, not an absence of work. Four complete sources were
swept (two shipped local resource sets, the full archived + live wiki corpora, the
official Japanese site, and the 2017 packet captures) and each zero is backed by a
control that was run first. What the hunt *did* produce is a materially better
**identity** backbone and one important evidence upgrade for the single entry that
is already counted. Details below.

Nothing in this file changes `coverage.md`, `polluted-observations.md`,
`server-ts`, any fixture, the APK, the seeds, the emulator, the phone, or Ghidra.
No server or client was touched; all work was read-only plus archive fetching.

---

# 1. PURE — items with an identified stat, value and level basis

**Nothing new.** The only qualifying row in the corpus remains
`Jack — Max HP 260 at Lv.50/50`, already counted in `coverage.md`. Section 1.1
records a genuine upgrade to *how* that row is evidenced.

## 1.1 The counted entry is now anchored to a first-party shipped string, and to a single item record

`GEAR.md` §1 rests on three OCR'd screenshots and calls the accessory `Jack`. That
name was, until today, only a screenshot reading. It is now confirmed from the
shipped 2.8.0.1 client itself:

`analysis/extracted/assets/CHAR_STR.db/000003.log`
(408,002 bytes, sha256 `dd0acc90e422a84a24978cdf7cb15bd86e2df242ae952ec053fc61cb447d5d2c`)
holds the game's item string table. Record **`051`** contains all three of
Beckhen's items in one row:

| field | EN | JA | KO |
|---|---|---|---|
| `051\|WEAPON` | Chicken Feet | — | — |
| `051\|ARMOR` | Chicken Wings | — | — |
| `051\|ACCESSORY` | **Jack** | ジャック | 잭 |
| `051\|ACCE_DESC` | "Jack's main role is to be Beckhen's interpreter, but \n sometimes he helps in the battle. ...Says Beckhen." | — | — |

Three consequences, all new:

1. **The item name is first-party, not OCR.** The English `ACCE_DESC` string is
   character-for-character the sentence printed on
   `analysis/catalogue/stats/found/faq-image21-gear-accessory-jack.png`, which I
   re-read by eye. The name is canonical (JA ジャック / KO 잭), not a wiki or OCR
   artefact.
2. **Item `051` carries weapon, armour and accessory together**, so `GEAR.md`'s
   three rows (`Chicken Feet` ATK 134, `Chicken Wings` DEF 102, `Jack` Max HP 260,
   all `Lv.50/50`, all Strength `30359 → 30359`) are three views of **one** item
   record on **one** build, not three unrelated captures. That materially
   strengthens the already-consistent trio.
3. `GEAR.md`'s other armoured item also resolves: **record `010` armour is
   `Purple Combat Coat`**, Vincent's, matching the Lv.49 → Lv.50 DEF 101 → 102
   comparison screen.

This does **not** raise coverage: Jack still has exactly one known stat value at
exactly one known level, which is what `coverage.md` already counts.

## 1.2 Slot → main stat, first-party Japanese, independent of the screenshot route

The official Japanese strategy site's equipment-enhancement page carries the
canonical slot table (verbatim, markup stripped):

```
装備 | 効果
武器 | 攻撃力 ＋ 攻撃関連能力値アップ
防具 | 防御力 ＋ 防御関連能力値アップ
装具 | HP ＋ 付加的な能力値アップ
```

This corroborates `GEAR.md`'s recovered slot→stat mapping (weapon→ATK,
armour→DEF, accessory→HP) from a **different first-party source in a different
language**, and adds one fact the screenshots do not: the slot's own stat is
*raised* by levelling, with **additional ("付加的な") stats on top**. That is the
mechanism behind `GEAR.md`'s two adjacent-level readings (armour Lv.49 DEF 101 →
Lv.50 DEF 102).

Source: `https://blustone.jp/facility/装備強化`, Wayback capture
`20190401013845`, `id_` replay, 37,916 bytes, sha256 `5cd7fc5711bd5f1a…`.

**Derived, and explicitly not coverage:** the three Lv.50 values (ATK 134 / DEF 102 /
Max HP 260) are consistent with the accessory main stat being a *per-slot* function
of item level rather than a per-item constant. One data point per slot cannot
distinguish the two, and nothing recovered here tests it. Recorded as a hypothesis
for the next hunter, not as a stat line.

---

# 2. UNPURIFIED — identity/level uncertain, and raw comparison fragments

## 2.1 NEW — the shipped accessory item table is complete and dense: 001–098

Extracted from `CHAR_STR.db/000003.log` by key/value pairing (no LevelDB open, no
write; raw bytes only). Published as
[`charstr-items-2026-10-06.tsv`](charstr-items-2026-10-06.tsv).

| slot | rows | unique EN names | numbering |
|---|---:|---:|---|
| `WEAPON` | 98 | 95 | 001–098, no gaps |
| `ARMOR` | 97 | 94 | 001–098, no gaps |
| `ACCESSORY` | **98** | **97** | **001–098, no gaps** |

Every row carries the name in all five shipped locales (`EN`/`JA`/`KO`/`SC`/`TC`)
plus an English flavour description. The only duplicated English accessory name is
`Hybrid Gloves`, at **068** and **098**.

**Extraction hazard worth passing on.** The first extraction pass reported the
accessory numbering as having five gaps (051, 055, 057, 081, 088). Those were an
**artefact, not data**: for an 11-byte key like `051|ACCESSORY` the byte that
follows is the high byte of the value length and can be a printable ASCII
character, so a greedy `[A-Z_]*` key pattern swallows it and yields bogus keys
`ACCESSORYQ`, `ACCESSORYT`, `ACCESSORYM`, `ACCESSORY_`, `ACCESSORYY`. Anchoring the
regex on an explicit suffix whitelist recovers all five, and they turn out to be
`Jack`, `Case`, `Mia`, `Signboard`, `Trowel`. A gap report that "looks like data"
was a parser bug — the same failure class as §16.7 of the project memory.

## 2.2 NEW — the 100-name denominator is 97 real items plus 3 wiki typos

`coverage.md` uses "100 distinct accessory names in
`analysis/catalogue/data/card-catalogue.tsv`" as the accessory denominator.
Crosswalking that list against the shipped 98-row table:

- **97 of 100** catalogue names are real shipped accessory items.
- **3 have no counterpart anywhere in the shipped item name space**:
  `Union Epaulet`, `Damaged Union Epaulet`, `Heat Resistant Railgun Gloves`.
  The game has `Unknown Epaulet` (009) and `Scratched Epaulet` (010), and
  `Heatproof Cannon Gloves` (020). These three read as community-wiki
  free-text variants, and the same three names appear verbatim on the live
  community wiki (§3.2), which is consistent with a wiki-side naming drift.
- **0** shipped accessory names are missing from the catalogue.

So the defensible denominator is **97 shipped accessories (98 records, `Hybrid
Gloves` twice)**, not 100. I have deliberately **not** changed `coverage.md` —
parent mirrors it — but the 1/100 percentage is inflated by ~3%.

## 2.3 NEW — a second, independent name source for the accessory set

`https://blustone.miraheze.org` — **"Blustone Archiving Wiki"** — is **LIVE** and
was not known to this project. The prior note in `vsfan-wiki-2026-10-05.md` §1.3
concluded that "both the original domain and its Miraheze successor are gone";
that is true of `vsfanwiki.miraheze.org` (which 404s with Miraheze's own "Wiki not
found" page) but **not** of `blustone.miraheze.org`, which is a different wiki and
answers normally (MediaWiki 1.46.2, verified via `api.php`).

Swept in full: 335 pages, 8 categories, 881 files. 103 pages carry an
`== Equipment ==` section, giving **309 equipment entries** (103 Weapon / 103 Armor
/ 103 Accessory) and **94 unique accessory names**, each with its hero owner.
Published as [`miraheze-equipment-crosswalk-2026-10-06.tsv`](miraheze-equipment-crosswalk-2026-10-06.tsv)
and [`miraheze-equipment-sections-2026-10-06.txt`](miraheze-equipment-sections-2026-10-06.txt).

Crosswalk against the shipped 2.8.0.1 name space:

| slot | name matches shipped table | name absent from shipped table |
|---|---:|---:|
| Accessory | 87 | 7 (`Case`, `Damaged Union Epaulet`, `Heat Resistant Railgun Gloves`, `Jack`, `Mia`, `Signboard`, `Union Epaulet`) |
| Weapon | 88 | 10 (`Bouquet`, `Chicken Feet`, `Flame Greatsword`, `Flames of Iron Bat`, `Lightning Claws`, `Sienna Railgun`, `Teddy`, `Thunder Sword`, `Ultra-High Temperature Plasma Sword`, `Ultra-Low Temperature Plasma Sword`) |
| Armor | 88 | 2 (`Aladdin Pants`, `Poncho`) |

19 equipment names on this wiki are absent from the shipped client, which is why the
wiki needed its own archive pass — but note `Chicken Feet` (absent) is exactly the
weapon `GEAR.md` reads on `faq-image19`, and `Jack`/`Case`/`Mia`/`Signboard`/`Trowel`
(absent) are exactly the five rows my first extractor pass appeared to have lost. The
two sources are **complementary, not contradictory**: the wiki holds a
wider/earlier name set, the shipped APK holds the canonical one.

## 2.4 Raw comparison fragments re-read by eye — all three confirmed, layout calibrated

I re-opened all three equipment panels rather than trusting the transcription:

| file | item | level | stat row | Strength row |
|---|---|---|---|---|
| `faq-image19-gear-weapon-chickenfeet.png` | Chicken Feet (weapon) | `Lv.50/50` | `ATK 134 → 134` | `30359 → 30359` |
| `faq-image20-gear-armor-chickenwings.png` | Chicken Wings (armour) | `Lv.50/50` | `DEF 102 → 102` | `30359 → 30359` |
| `faq-image21-gear-accessory-jack.png` | **Jack (accessory)** | `Lv.50/50` | `Max HP 260 → 260` | `30359 → 30359` |

Both sides of every comparison recorded, as required. The three slot icons at the
top of each panel are all `Lv.50` with exactly one highlighted by a glow and a
pointer triangle, which is what establishes these as equipment item panels rather
than a hero panel. Layout confirmed identical across all three, consistent with the
prior calibration against the Beckhen cross-screen match.

No new fragments. Nothing here adds a second item.

---

# 3. Controlled negatives

Each zero below states the control that makes it trustworthy. Every control
returned real content, so none of these are silent failures.

## 3.1 Shipped local resources contain no per-item stat table — 9 packs, zero text

Extends the recorded `EQUIP.jet` negative (24 I2 texture resources, no
`textResources`, no equipment-stat table — **not** re-litigated, re-measured as part
of one batch). Decoded with the project's own `tools/jet-viewer/jet_decoder.py`
against `analysis/extracted/assets/`:

| pack | bytes | resources | `textResources` |
|---|---:|---:|---:|
| `EQUIP.jet` | 165,028 | 24 | 0 |
| `UI_ITEM.jet` | 1,655,400 | 196 | 0 |
| `UI_ITEM_CHA.jet` | 292,960 | 66 | 0 |
| `UI_ENHANCE_NEW.jet` | 1,169,127 | 110 | 0 |
| `UI_SHOP.jet` | 1,236,254 | 69 | 0 |
| `UI_GEM.jet` | 139,293 | 38 | 0 |
| `E_GEM_DEFALT.jet` | 137,674 | 1 | 0 |
| `REWARD.jet` | 1,279,866 | 19 | 0 |
| `UI_ICON.jet` | 1,229,363 | 299 | 0 |
| `UI_CSV.jet` *(control)* | 93,380 | 8 | **5** |

`UI_CSV.jet` is the positive control: it is the one pack in this family that *does*
carry text resources, and it yields the help table the project has already mined for
jewel set bonuses. So the decoder sees text when text exists; the nine zeros above
are real.

Conclusion: **the per-item equipment stat is not in any preserved client resource.**
That is consistent with the recovered protocol shape — item reference data arrives
from the server via `/reference/GetItem` → `CSRItemInfo::SetItem`, and the shipped
`REFEN/reference/GetItem` local-load fallback documented in
`analysis/research/native-reference-offline-storage.md` is a mechanism, not a
located table. A separate raw-byte sweep of all 9,079 files under
`analysis/extracted`, `analysis/VSFan/Extracted Assets (2026)` and
`analysis/VSFan/Research/Blustone/Extracted Updates` for eight accessory names hit
only `CHAR_STR.db/000003.log` (and three irrelevant `Jack`-as-character hits), which
independently confirms the items are names-and-prose only.

## 3.2 The live community wiki contains zero accessory stat numerals — full corpus, not a sample

This is the strongest negative of the run, because it is exhaustive rather than
sampled: **all 335 pages** were pulled as raw wikitext via the MediaWiki API.

- **309** equipment entries parsed (103 Weapon / 103 Armor / 103 Accessory).
- **Exactly 10** entries contain any digit at all, and in all ten the digit is
  inside the flavour description, not a stat: Captain hospitalised "for **3**
  weeks" (Bear's Feet), sales up "**50**%" (Bright's armour), "a **200**% … **100**%"
  recreation (Matchboy Hood), "block **100** bandits" (Hecate), "**2XL**" (Kain's
  armour), "**4kg** pumpkin … **5m/s**" (Halloween Pumpkin), "**M67** grenade"
  (Metis), "when she was **10** years old" (Bear Leather), "**30** years ago"
  (Thermal Jumper).
- Corpus-wide there are 1,738 numeral tokens, so the sweep is not blind — they sit
  in skill text, release dates and revision anchors. Skill tables on this wiki use
  unfilled `[value]` / `[duration]` placeholders.
- Its 881 uploaded files are portraits, role icons, CGs, emotes and one gym image;
  **no equipment panel screenshot** exists among them.

So the single best-maintained Blustone wiki that is still online has the accessory
*identities* and none of the accessory *numbers*.

## 3.3 The official Japanese site: the `/equipment` page is an empty stub

`url=blustone.jp&matchType=domain` → **1,236 CDX rows** (a real corpus, so this is
not a "domain not archived" zero).

| page | capture | replay | bytes | content |
|---|---|---|---:|---|
| `https://blustone.jp/equipment` | 20191121194806 | 200 | 26,602 | body is the single word `equipment`, posted 2018-11-19 — an **unwritten stub** |
| `https://blustone.jp/facility/装備強化` | 20190401013845 | 200 | 37,916 | the only equipment prose on the site (used in §1.2) |

The site's six equipment screenshots were **never captured**. Fetching
`equip1-1024x911.jpg` returned 9,116 bytes beginning `<!DOCTYPE html>` — the
Wayback "not archived" page, with no JPEG SOF marker. Recorded as a byte-level
negative, exactly the trap in
[`GUARD-encoding-and-archive-traps.md`](GUARD-encoding-and-archive-traps.md): a
rewritten or reachable image URL is not evidence of pixels. `blustone.jp` is also
NXDOMAIN live.

## 3.4 vsfan.net — the prior `Jewels` negative is now byte-verified, and a whole CDX class was being missed

Two findings about method, one about content.

**A class of captures was invisible to the earlier pass.** §1.17 of
`vsfan-wiki-2026-10-05.md` probed `w/index.php?title=Jewels` and got 0 rows, with
working controls in the same run. But a full `url=vsfan.net&matchType=domain`
dump (4,054 rows) contains
`https://vsfan.net/w/index.php?title=Jewels&action=edit&redlink=1` at
**20190826073527**. The zero was a **query artefact**: an unencoded `?` in the
`url=` parameter truncates the CDX match. Encoding it fixes the lookup. 880
`Template:`/`Module:` rows and ~700 `w/index.php` edit rows exist in that domain
and are likewise absent from the prior reasoning.

**The negative itself survives.** Fetched 22,757 bytes (sha256 `29cc74db0d8a1496…`):
it is MediaWiki's "Creating Jewels" redlink form with an **empty textarea**. There
were never any bytes to recover. `Template:Longitem` (19,356 B) and
`Template:Status` (16,698 B) are bare `{{{1}}}` passthroughs. `Template:Equipment`
HTTP 404s on `id_` replay even though a CDX row exists.

**Positive control for the whole sweep:** `vsfan.net/wiki/Beckhen` replayed at
**88,572 bytes**, matching the byte count already recorded for that page in §1.4 of
the prior note. The fetch path is working.

## 3.5 namu.wiki is crawler-blocked, not absent

CDX prefix queries for `namu.wiki/w/블러스톤` (raw and percent-encoded) return
`[]`, but the exact-URL control for a known namu title returns **1 row with status
`403`** — namu serves Forbidden to the crawler. The correct reading is *inaccessible
in this environment*, not *no equipment page exists*. The project's existing
`file.namu.moe` 503s and the `dark.namu.moe` mirror 404s are the same class of
wall. A Korean IP or a Korean-language search engine is the only realistic route into
namu equipment tables, and I could not reach one.

## 3.6 The local VSFan tree contains no equipment art at all

`analysis/VSFan/Images/` holds 220 curated images. `Images/Blustone/Items/` has
subfolders for Coupons, Currency, Events, Materials, Metron, Recruitment and
Traces — and **no equipment icons whatsoever**. Everything else in the tree is
portraits, location art, concept art or press-kit screenshots; I opened
`hunter_gym.png` and `item_list_en_01.png` by eye and both are location art and an
event request list respectively.

**Control:** the item-icon folders that *should* hold equipment icons are the same
folders that demonstrably hold correct item icons (`metron_fragment.png`,
`rupee.png`, `manda.png`, `broken_shell.png` are all real item art), so the absence
is a content gap in that tree, not a mis-indexed directory.

## 3.7 The 2017 packet captures contain the original `GetItem` call but the body is encrypted

`analysis/VSFan/Packet Captures/blustone.pcap` (128,731,909 B) contains a real
`POST /reference/GetItem HTTP/1.1` to `sr-prd.gshower.net`, three times, with
`Content-Type: application/octet-stream`, `Content-Length: 80` and a ciphertext
body — i.e. the request the replica has to imitate, captured from the original
server. It carries no plaintext item table. `bs_transcendence.pcap` (54,929,150 B)
matches on the same needles.

The 47 `ret_data` occurrences in `blustone.pcap` are **not** game payloads. All of
them are the CDN's plaintext 85-byte acknowledgement envelope:

```
{"result_code":1,"ret_data":null,"enc":null,"execution_time":"0.0097","t":1504583791}
```

`btba.pcap` and `whiteisland.pcap` contain neither needle set. This confirms the
project's recorded position that game bodies are encrypted, and pins the reason: the
per-item stat values are behind the ECDH/HMAC/AES layer of a 2017 session that is
long gone.

**Safety note.** Those captures carry cleartext `PV-AccessToken` and
`PV-Signature` headers for the defunct `sr-prd.gshower.net`. They remain local,
they are not reproduced in this note, and my scratch dumps that contained them were
deleted rather than written into the repo. Nothing here should ever be committed.

---

# 4. Corrections and refinements to existing records

## 4.1 Super Block has a *third* Japanese reading of 9%

`coverage.md` records: "Super Block conflicts by locale (Korean 9%, English,
Japanese and both Chinese locales 5%)". That "Japanese 5%" refers to the **1.4.4.1
in-game `UI_CSV` JA string** (`鉄壁結晶 - 4コ装着：ブロックダメージ減少量 5%`, per
[`jewel-help-locales-2026-10-05.md`](jewel-help-locales-2026-10-05.md) §1.3.3); the
same note records JA moving to **10%** in 2.8.0.1. VisualShower's own Japanese
strategy site publishes a **9%**, which matches neither:

```
鉄壁結晶 4コ装着：ブロックダメージ減少量 9%UP
```

So "Japanese" is not one value; there are three Japanese sources (1.4.4.1 UI = 5%,
2.8.0.1 UI = 10%, official site = 9%) and the KO value of 9% is not uniquely Korean.
This does **not** move any coverage number and I have not edited the jewel records —
it is a provenance refinement the jewel note's author should apply.

The same official list reads **`属性結晶 4コ装着：属性強化 23UP`** and
**`体制結晶 4コ装着：属性耐性 23UP`** — both a flat `23`. `GEAR.md` §3 left the
Element/Resistance decimal placement unresolved from the screenshot. This is
independent first-party corroboration of the flat-`23` reading, from a source that
is *not* the game client (whose own text reads `35` for element). Treat it as
corroborating the transcription, not as establishing the game's value. The other
ten families on the official list agree with the recorded table, including the bare
`30` (再生力), `12` (貫通力) and `1.72` (攻撃速度) numerals.

## 4.2 `vsfan-wiki-2026-10-05.md` §1.3 over-generalises from one Miraheze wiki

"Both the original domain and its Miraheze successor are gone" is true of
`vsfanwiki.miraheze.org` and false in general: `blustone.miraheze.org` is live
(§2.3). The claim should be scoped to the specific host.

## 4.3 The accessory denominator

See §2.2. Defensible figure is 97 shipped accessories / 98 records, not 100. Not
applied — parent mirrors `coverage.md`.

## 4.4 ALERT — `coverage.md` has been flipped to CRLF by some other session

Detected while running the post-write encoding check, and **not caused by this
session** (I never wrote to that file). Measured against git:

| file | `HEAD` bytes / CRLF | working bytes / CRLF |
|---|---|---|
| `coverage.md` | 45,314 / **0** | 46,150 / **150** |
| `polluted-observations.md` | 38,677 / 0 | 191,023 / 0 |

`coverage.md` is now 151 lines and **all 150 of them end CRLF** — a whole-file
line-ending flip, which is GUARD Rule 3 exactly. Content is intact (strict UTF-8,
U+FFFD 0, mojibake 0, CJK/kana present), so this is cosmetic, not corruption — but a
future diff of that file will be noisy and a naive line-oriented edit could damage
the Hangul/CJK in it.

I have **deliberately not repaired it**: `coverage.md` is parent-mirrored and another
session may be mid-write, so a silent rewrite risks clobbering that work. The fix,
when the parent is at a clean point, is a byte-level normalisation with no content
change:

```python
p = 'analysis/research/base-stats-visual-hunt/coverage.md'
b = open(p, 'rb').read()
open(p, 'wb').write(b.replace(b'\r\n', b'\n'))
```

My own four files in this directory were all written with explicit `newline='\n'`
and verified: strict UTF-8, U+FFFD 0, CRLF 0, mojibake 0, with Hangul/CJK/kana
preserved (the accessory TSV carries 511 Hangul, 572 kana and 1,040 CJK code points
across the five shipped locales).

---

# 5. Durable artefacts written

| file | what |
|---|---|
| [`charstr-items-2026-10-06.tsv`](charstr-items-2026-10-06.tsv) | 105 item records from the shipped 2.8.0.1 `CHAR_STR.db`: weapon/armour/accessory names in all five locales plus the key census per record |
| [`miraheze-equipment-crosswalk-2026-10-06.tsv`](miraheze-equipment-crosswalk-2026-10-06.tsv) | 309 live-wiki equipment entries: slot, name, whether the name exists in the shipped table, hero owners |
| [`miraheze-equipment-sections-2026-10-06.txt`](miraheze-equipment-sections-2026-10-06.txt) | the 103 raw `== Equipment ==` sections verbatim, as fetched |

No other file in `analysis/research/base-stats-visual-hunt/` was modified. I did not
append to `polluted-observations.md`, and I did not touch `coverage.md`.

---

# 6. What would actually earn entries

Ranked by expected yield, based on what the negatives above ruled out:

1. **A second equipment-panel screenshot.** This is the only mechanism that has ever
   produced a qualifying row, and it needs one image: an item's name + stat + level
   in the same frame. It does not need to be Beckhen. Any hero's weapon/armour/
   accessory panel does it, and the CHAR_STR table makes the name→identity link
   exact. The VSFan tree, the live wiki, blustone.jp and namu are all exhausted or
   walled; the remaining untried surface is **YouTube/streaming gameplay video**
   where the player opens the equipment screen, and **Korean-language community
   boards reachable by search engine** rather than by direct fetch.
2. **A Korean-language search pass on namu content via a search index** (not the
   site). `dark.namu.moe` and `file.namu.moe` both wall; a search engine that has
   cached namu Blustone pages could still surface an equipment table.
3. **The Japanese site's captured `/archives/` pages.** `blustone.jp` has ~40
   `/archives/NNNN/...` pages captured that I identified but did not read. Some are
   attachment pages whose parent post may carry an equipment screenshot with a
   Japanese item name — which the CHAR_STR JA column translates exactly. This is the
   cheapest untried lead and I ran out of budget before it.
4. **Not worth retrying:** `EQUIP.jet` and the other texture packs (§3.1), the
   pcaps (§3.7), namu direct fetch (§3.5), or the vsfan `?`-URL class (§3.4).

Nothing in this file should be read as "accessories have no stats in the original
game". The original server had them; they sat behind a session key that is gone. The
honest statement is that **no surviving source in this workspace, and no source I
could reach, publishes a per-item accessory stat line other than Jack's.**

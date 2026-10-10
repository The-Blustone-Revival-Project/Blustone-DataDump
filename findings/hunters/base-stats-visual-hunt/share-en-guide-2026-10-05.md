# `share_en/197745` "Guide to Blustone" — 11 images located and named, ZERO pixels exist (2026-10-05)

**Lane:** the lead recommended by
[`review-posts-2026-10-05.md`](review-posts-2026-10-05.md) §3, item 1 — the 11
real in-game screenshots of `share_en/197745` in attachment namespace
`565/745/197/`, which that pass located but did not open.

**Budget: 10 image fetches, 0 retries of any image URL, 0 bypasses.** All 10
returned **HTTP 404**. **Zero images were pixel-inspected, because zero
retrievable bytes exist.** That is stated in the first line of §1 so nothing
below can be misread as coverage.

**Headline, four findings:**

1. **The corpus is a settled archival negative.** `565/745/197/` has **zero CDX
   rows** under four URL forms and **all status codes**, and the live origin is
   dead (503). This is proven with a **positive control** (§1.3) — the identical
   query shape returns 4 rows for a namespace a prior pass *did* download.
   Do not re-attempt this post's images.
2. **A real correction to the prior pass, and a genuine recovery:** the 5
   `Screenshot_2017-11-11-*.png` names and `Arena.png` / `Fight Club.png` /
   `Ruins.png` / `Training Gym.png` / `Cruise_beginning.png` / `Cruising.png`
   are **the `alt` attributes of the 11 attachments**, i.e. the originals' own
   upload filenames — **not** extra "in-image filenames" as
   `review-posts-2026-10-05.md` §1.6 implied (it read as 16 images). There are
   exactly **11**, now mapped 1:1 to their guide sections (§1.2). That pass's
   `Gym.png` and `Club.png` are mis-transcriptions of **`Training Gym.png`**
   and **`Fight Club.png`**.
3. **The genuinely valuable recoverable artifact is the guide's body text**, not
   the images. It is a substantial, dated, **PRE-2019-09-05** transcription of
   original-game economy: fuel costs, Abyss stage rewards, Ruins rules,
   star-up fodder counts, the **full Transcendence cost table**, the **full
   skill-level cost table**, skill slot unlock rules, and Arena rules/team
   lists. Transcribed verbatim in §1.5. **This is text, not pixels**, and it is
   **not** hero/monster/accessory coverage.
4. **A reusable method trap is now documented** (§2.2): Wayback **rewrites
   `img src` into `im_` form inside captured HTML even when the image was never
   captured.** A rewritten image URL in an archived body is therefore *not*
   evidence that any bytes exist — which is exactly what made this lane worth
   attempting and exactly what would mislead a future pass.

---

## 1. PURE — verbatim readings, exact fetch ledger, and the filenames as stored

Nothing in §1 is a base-stat reading. **No image was decoded and no HP / ATK /
DEF panel was seen, because not one image byte is retrievable.** §1.5 is verbatim
**post body text** and is labelled as such; it carries economy numerals, not
hunter stats.

### 1.1 Image fetch ledger — 10 attempts, HTTP status recorded for each

URL form throughout: Wayback `im_` (raw bytes, no HTML rewrapping) in front of
the original `bs.visualshower.com/files/attach/images/...` path, at the
**single timestamp the archived body itself advertises**, `20180227140354`
(2018-02-27 14:03:54 UTC). Those URLs are not guesses — they were read out of
the archived post body (§1.2), which is where Wayback had already rewritten
them.

| # | Attachment hash | `alt` = original upload filename | Archive URL fetched | HTTP | Bytes | Signature of body | Verdict |
|---|---|---|---|---|---|---|---|
| 1 | `9997745206a3c799fe23b1c3e8a9b652` | `Training Gym.png` | [20180227140354im_](http://web.archive.org/web/20180227140354im_/http://bs.visualshower.com/files/attach/images/565/745/197/9997745206a3c799fe23b1c3e8a9b652.png) | **404** | 4,727 | `3c 21 44 4f 43 54 59 50` | not counted |
| 2 | `a108de5ae785015eb93dfe436b4a5661` | `Screenshot_2017-11-11-14-46-11.png` | [20180227140354im_](http://web.archive.org/web/20180227140354im_/http://bs.visualshower.com/files/attach/images/565/745/197/a108de5ae785015eb93dfe436b4a5661.png) | **404** | 4,727 | `<!DOCTYP` | not counted |
| 3 | `c74645562f4808918731bb2ba9fae268` | `Screenshot_2017-11-11-14-46-43.png` | [20180227140354im_](http://web.archive.org/web/20180227140354im_/http://bs.visualshower.com/files/attach/images/565/745/197/c74645562f4808918731bb2ba9fae268.png) | **404** | 4,727 | `<!DOCTYP` | not counted |
| 4 | `5c3dc1b9bba2d43a3ac4cc7f9d529b2b` | `Screenshot_2017-11-11-15-07-52.png` | [20180227140354im_](http://web.archive.org/web/20180227140354im_/http://bs.visualshower.com/files/attach/images/565/745/197/5c3dc1b9bba2d43a3ac4cc7f9d529b2b.png) | **404** | 4,727 | `<!DOCTYP` | not counted |
| 5 | `1c121be82d8bfcf6f5ab9e704adb1d07` | `Arena.png` | [20180227140354im_](http://web.archive.org/web/20180227140354im_/http://bs.visualshower.com/files/attach/images/565/745/197/1c121be82d8bfcf6f5ab9e704adb1d07.png) | **404** | 4,727 | `<!DOCTYP` | not counted |
| 6 | `b54f4b1bb263bf863200f61539122323` | `Fight Club.png` | [20180227140354im_](http://web.archive.org/web/20180227140354im_/http://bs.visualshower.com/files/attach/images/565/745/197/b54f4b1bb263bf863200f61539122323.png) | **404** | 4,727 | `<!DOCTYP` | not counted |
| 7 | `d08e6de796029e3efe615dc2e98a4de6` | `Ruins.png` | [20180227140354im_](http://web.archive.org/web/20180227140354im_/http://bs.visualshower.com/files/attach/images/565/745/197/d08e6de796029e3efe615dc2e98a4de6.png) | **404** | 4,727 | `<!DOCTYP` | not counted |
| 8 | `7c7ce8d6b217c490a75f87cc75c26377` | `Screenshot_2017-11-11-14-45-20.png` | [20180227140354im_](http://web.archive.org/web/20180227140354im_/http://bs.visualshower.com/files/attach/images/565/745/197/7c7ce8d6b217c490a75f87cc75c26377.png) | **404** | 4,727 | `<!DOCTYP` | not counted |
| 9 | `41fd313eed657cfd55a0c1968678dc4f` | `Screenshot_2017-11-11-07-17-55.png` | [20180227140354im_](http://web.archive.org/web/20180227140354im_/http://bs.visualshower.com/files/attach/images/565/745/197/41fd313eed657cfd55a0c1968678dc4f.png) | **404** | 4,727 | `<!DOCTYP` | not counted |
| 10 | `44c11f2135810d1b39c8646ff18f6785` | `Cruise_beginning.png` | [20180227140354im_](http://web.archive.org/web/20180227140354im_/http://bs.visualshower.com/files/attach/images/565/745/197/44c11f2135810d1b39c8646ff18f6785.png) | **404** | 4,727 | `<!DOCTYP` | not counted |

**All 10 responses are byte-identical: 4,727 bytes, signature
`3c 21 44 4f 43 54 59 50` = `<!DOCTYPE html`, `<title>Wayback Machine</title>`.**
They are the archive's own "not archived" error page, not images. There is no
PNG signature (`89 50 4e 47`) in any of them.

**Not fetched: `9d762be979e9f465ee7b5a991d770294` = `Cruising.png`** — the
budget was reached first. Its index status is nonetheless settled by §1.3: zero
rows, same as the other ten, so nothing was lost by not spending the fetch.

The `Screenshot_2017-11-11-*.png` filename timestamps are a **filename-level**
fact and are independent of any archive capture date (§2.5).

### 1.2 The 11 attachments, exactly as the archived body stores them

Body fetched 2026-10-05: HTTP **200**, **105,467 bytes**,
`web/20180227140354/http://bs.visualshower.com:80/share_en/197745`.
Metadata: title **`Guide to Blustone`**, dated **`2017.11.12 01:32`**,
`Views 1571`, `Votes 0`, `Reply 5`, author **`Alaiko`**.

Verbatim `<img>` tags, in body order. **`alt` is the uploader's own filename** —
this is the recovery:

| Body order | Section the image illustrates | Verbatim `src` tail | Verbatim `alt` | `height` attr |
|---|---|---|---|---|
| 1 | §1.1 Cruises (opening) | `44c11f2135810d1b39c8646ff18f6785.png` | `Cruise_beginning.png` | – |
| 2 | §1.1 Cruises (in progress) | `9d762be979e9f465ee7b5a991d770294.png` | `Cruising.png` | – |
| 3 | §1.2 Abyss | `41fd313eed657cfd55a0c1968678dc4f.png` | `Screenshot_2017-11-11-07-17-55.png` | `640` |
| 4 | §1.3 Ruins | `d08e6de796029e3efe615dc2e98a4de6.png` | `Ruins.png` | – |
| 5 | §2 Training Gym (hub) | `9997745206a3c799fe23b1c3e8a9b652.png` | `Training Gym.png` | – |
| 6 | §2.1 Training your hunter | `a108de5ae785015eb93dfe436b4a5661.png` | `Screenshot_2017-11-11-14-46-11.png` | `640` |
| 7 | §2.2 Upgrading your hunter (advance) | `c74645562f4808918731bb2ba9fae268.png` | `Screenshot_2017-11-11-14-46-43.png` | `640` |
| 8 | §2.3 Transcending your hunter | `7c7ce8d6b217c490a75f87cc75c26377.png` | `Screenshot_2017-11-11-14-45-20.png` | `640` |
| 9 | §2.4 Upgrading your hunter skills | `5c3dc1b9bba2d43a3ac4cc7f9d529b2b.png` | `Screenshot_2017-11-11-15-07-52.png` | `640` |
| 10 | §3 PvP arena (lobby) | `b54f4b1bb263bf863200f61539122323.png` | `Fight Club.png` | – |
| 11 | §3 PvP arena (roster) | `1c121be82d8bfcf6f5ab9e704adb1d07.png` | `Arena.png` | – |

Body order also appears in the page's `<meta property="og:image">` list, in the
order `d08e6de7 → 41fd313e → 99977452 → a108de5a → c7464556 → 7c7ce8d6 →
5c3dc1b9 → b54f4b1b → 1c121be8 → 44c11f21 → 9d762be9` — a different order again.
Three orderings exist; the `<img>` order in §1.2 is the one that reflects guide
progression and is used as authoritative.

**Corrections to `review-posts-2026-10-05.md` §1.6, on evidence:**

- It listed 11 hashes **plus** a separate block of "named" filenames
  (`Arena.png`, `Club.png`, `Cruise_beginning.png`, `Cruising.png`, `Gym.png`,
  `Ruins.png`, 5× `Screenshot_2017-11-11-*.png`), read as ~16 distinct images.
  **There are 11 images.** The named block *is* the `alt` set of those 11.
- `Gym.png` is **`Training Gym.png`**. `Club.png` is **`Fight Club.png`**. Both
  prior labels are mis-transcriptions.
- That pass called the named filenames "the guide's own section captions". They
  are uploader-side **file names**; the captions are the section headings the
  images sit under (§1.2, middle column).

### 1.3 The archival negative, with a positive control

Five CDX index queries, **all statuses, no status filter**, run 2026-10-05.
Index queries only — these are not image fetches.

| # | Query | Result |
|---|---|---|
| i1 | exact url, no port: `…/565/745/197/9997745206a3c799fe23b1c3e8a9b652.png` | HTTP 200, **0 bytes / 0 rows** |
| i2 | same exact url **with `:80`** | HTTP 200, **0 bytes / 0 rows** |
| i3 | `matchType=prefix` on `…/565/745/197*` (star URL-encoded) | HTTP 200, **0 bytes / 0 rows** |
| i4 | `matchType=prefix` on `…/565/745/` | HTTP 200, **0 bytes / 0 rows** |
| i5 | `matchType=domain` on `bs.visualshower.com` + `filter=original:.*565/745/197.*` | HTTP 200, **0 bytes / 0 rows** |
| i6 | `matchType=domain` + `filter=original:.*/files/attach/images/565/.*` (whole namespace) | HTTP 200, **0 bytes / 0 rows** |

**Positive control — the identical query shape, on a namespace a prior pass
*did* download** (`board-attachments-2026-10-05.md` §1.2 image A, which returned
200 with 57,414 bytes):

```
20210903030305 https://bs.visualshower.com/files/attach/images/75605/303/534/001/725a8e175454a533e96dac68fc5fdb49.jpg 200 image/jpeg 58647
20210903030326 https://bs.visualshower.com/files/attach/images/75605/303/534/001/7e951164fd7e45dbfc5d2b33b106fddc.jpg 200 image/jpeg 116003
20210903030226 https://bs.visualshower.com/files/attach/images/75605/303/534/001/8356e1c4a5f7f7388d7c24f04ba0108f.jpg 200 image/jpeg 58477
20210903030212 https://bs.visualshower.com/files/attach/images/75605/303/534/001/f9a04919d2f82addf089a6f98a9d1c28.jpg 200 image/jpeg 237347
```

The control returns 4 rows where the `565/745/197` queries return 0. **The query
method is sound; the zero-row results are a real property of the archive, not a
broken filter.** Without this control the five zeros would be uninterpretable.

**Live origin, same path, same day:** `http://bs.visualshower.com/files/attach/images/565/745/197/9997745206a3c799fe23b1c3e8a9b652.png`
→ **HTTP 503** (content-type still advertised `image/png`, 0 bytes).
`https://` fails TLS locally (`SEC_E_INTERNAL_ERROR`). The origin is gone, so
there is no non-archive fallback.

**Conclusion: the 11 screenshots are unrecoverable from the Wayback Machine and
from the origin. This is a hard negative, not an untried lead.**

### 1.4 Era tag, stated once and applied to everything below

Post dated **`2017.11.12`**; five attachments self-name `2017-11-11`. Both are
**PRE-2019-09-05**, i.e. squarely inside the older balance era of
[`stat-version-context.md`](stat-version-context.md) (equipment stats +50%,
1–3★ crystal main +30%, 4–5★ main +50%, all crystal substats +50%, larger gains
after equipment Lv.20 — all effective after 2019-09-05). **Every numeral in
§1.5 is tagged PRE-2019-09-05 and must not be mixed with post-rebalance values.**

### 1.5 Guide body numerals, transcribed verbatim — **text, not pixels**

Source: the 200 body above. Below is the author's own prose, quoted as rendered.
Em/en dashes and curly apostrophes are normalised to `-` and `'`; **all digits,
commas, slashes and spellings are the author's, unmodified**. These are
**player-reported economy/system values, not pixel-verified UI readings** — the
honour tier used elsewhere in this project for dated community claims. None of
it is a hero, monster or accessory stat.

**Cruises (§1.1) — fuel**
> "At the lower regions, the best areas to train are at level 36 - 40. The
> reason for this is that it is the last region where you spend 6 fuel per run
> (the next region costs 7 fuel). As such, it gives a good balance between
> getting experience and obtaining bronze-tier materials for training hunter
> skills. At the higher regions, the best areas to train are at level 96 to 100
> for similar reasons."

**Cruises — material tier by level-ending digit**
> "At levels 36 to 39, bronze tier materials are dropped. At levels 96 to 99,
> silver tier materials are dropped and on the rare occasion, you may also get
> some gold tier materials. […] 1) For levels ending in 1 or 6 (like 31 or 36),
> materials for training Offensives' skills are dropped. 2) For levels ending
> in 2 or 7 (like 32 or 37), materials for training Defenders' skills are
> dropped. 3) For levels ending in 3 or 8 (like 33 or 38), materials for
> training Bombers' skills are dropped. 4) For levels ending in 4 or 9 (like 34
> or 39), materials for training Healers' skills are dropped. […] For levels
> ending in 5 or 0 (like 35 or 40), no materials are dropped."

Also: "the experience you gain from each level is constant. This means that
there is no difference in experience gained if you take 4 hunters or fewer
hunters"; "a maxed hunter also gains no experience from cruises."

**Abyss (§1.2) — day mapping and stage rewards**
> "Electric Abyss - Drops materials for Offensives' skills training / Cryogenic
> Abyss - Drops materials for Defenders' skills training / Volcanic Abyss -
> Drops materials for Bombers' skills training / Golden Abyss - Drops materials
> for Healers' skills training"
> "Note: Each Abyss is only available on a particular day. This information is
> available at the entrance to the Abyss."
> "The main objective here is to reach and complete stage 5 of the Abyss as it
> gives 3 metron crystals per run. In comparison, stages 3 and 4 give you 2
> metron crystals while stages 1 and 2 only give you 1 metron crystal."
> "Note: You can only attempt the Abyss once per day. If you wish, you may
> reset the Abyss at a cost of **30,000 Rupees or 30 Manda**. As your veteran
> level goes up, you are able to reset more times, but the cost increase with
> each reset."
> "Unlike the other three, Golden Abyss gives gold instead of metron crystals."

**Ruins (§1.3)**
> "Hidden and Normal Ruins are used to obtain the traces of natural 3-stars and
> 2-stars hunters respectively. […] Right now, the only 3 star hunters for whom
> you can collect traces are **Hermes, Karl, Nene and Athena**."
> "The first is that there are **4 waves**, with each wave getting progressively
> more difficult. At the end of each wave, you will face off the hunter whose
> ruin you are doing. For wave 1 to 3, the hunter does not use his skill, but
> the final boss in wave 4 does."
> "The second is that there is **no time limit**! You will never run out of
> fuel no matter what. […] As each of these ruins costs **20 fuel**, I feel that
> you should only be doing this if you can clear at least wave 2."

**Star upgrade (Advance, §2.2) — fodder counts**
> "1-star to 2-stars: one 1-star fodder is required
> 2-star to 3-stars: two 2-star fodders are required
> 3-star to 4-stars: three 3-star fodders are required
> 4-star to 5-stars: four 4-star fodders are required"

**Transcendence (§2.3) — full cost table, verbatim**
> "Both the base hunter and the duplicate hunter must be at least 3 stars for
> the first transcendence."
> "Natural 1-star — T1: 5 Metron Crystals, 5,000 Rupees, 50 Metron Fragments, 1
> Duplicate Hunter / T2: 15 Metron Crystals, 15,000 Rupees, 150 Metron
> Fragments, 2 Duplicate Hunter / T3: 45 Metron Crystals, 45,000 Rupees, 450
> Metron Fragments, 3 Duplicate Hunter"
> "Natural 2-stars — T1: 7 Metron Crystals, 7,000 Rupees, 70 Metron Fragments,
> 1 Duplicate Hunter / T2: 25 Metron Crystals, 25,000 Rupees, 250 Metron
> Fragments, 2 Duplicate Hunter / T3: 60 Metron Crystals, 60,000 Rupees, 600
> Metron Fragments, 3 Duplicate Hunter"
> "Natural 3-stars — T1: 9 Metron Crystals, 9,000 Rupees, 90 Metron Fragments,
> 1 Duplicate Hunter / T2: 30 Metron Crystals, 30,000 Rupees, 300 Metron
> Fragments, 2 Duplicate Hunter / T3: 80 Metron Crystals, 80,000 Rupees, 800
> Metron Fragments, 3 Duplicate Hunter"
> "Note: For the second and third transcendence, your base hunter needs to be at
> least 4-stars and 5-stars respectively. The duplicate hunters however only
> need to be 3-stars."

**Skill slots and skill-level costs (§2.4)**
> "There are 5 different skills for each hunter, and the next skill gets
> unlocked as you upgrade the hunter. This means at 1-star, only the first
> skill is available whereas all the skills are available for 5-stars hunters."
> "Level 1 - 4: 100 Rupees, 1 Metron Fragment
> Level 5 - 9: 200 Rupees, 1 Metron Fragment, 1 Bronze tier materials
> Level 10 - 14: 300 Rupees, 2 Metron Fragments, 2 Bronze tier materials
> Level 15 - 19: 400 Rupees, 2 Metron Fragments, 3 Bronze tier materials
> Level 20 - 25: 500 Rupees, 3 Metron Fragments, 4 Bronze tier materials, 1
> Silver tier Material
> Level 26 - 29: 600 Rupees, 3 Metron Fragments, 5 Bronze tier materials, 2
> Silver tier Materials
> Level 30 - 34: 700 Rupees, 4 Metron Fragments, 3 Silver tier materials, 1
> Gold tier Materials
> Level 35 - 39: 800 Rupees, 4 Metron Fragments, 4 Silver tier materials, 2
> Gold tier Materials
> Level 40 - 44: 900 Rupees, 5 Metron Fragments, 5 Silver tier materials, 3
> Gold tier Materials
> Level 45 - 49: 1000 Rupees, 5 Metron Fragments, 6 Silver tier materials, 4
> Gold tier Materials"
> "The first skill is your active skill. […] The second skill is triggered and
> always occurs after the first skill is activated. The third skill is passive
> and it always applies. The fourth skill has a chance to trigger once the first
> skill activates. […] The fifth skill is passive and it always applies."

**Arena / Fight Club (§3)**
> "At the time of writing this guide, fights in arena are automatic and do not
> use skills. As such, only the 3rd and 5th skills of all hunters apply in
> arena. Do note, however, there is an upcoming update that will allow you to
> use hunters' skills […]"
> "1) As far as possible, use your elemental advantage when attacking an
> opponent's team. Fire is strong against electric, electric is strong against
> ice and ice is strong against fire."
> "2) […] it is better to use [3 Defenders + 1 Healer] or [2 Defenders + 2
> Healers] […] Similarly, it is better to use [3 Offensives + 1 Bomber] or [2
> Offensives + 2 Bombers]"
> "3) The team buffs that Healers and Bombers provide are only applicable as
> long as the hunter is alive. […] Healers and Bombers should be placed last in
> your defense and attack team respectively."
> "4) As far as possible, do not use defense hunters in your attack teams."
> "Offense team: Hermes / Octavia / Vincent / Captain / Diana / Lantern /
> Patrone / Levi / Karl"
> "Defense team: Athena / Nene / Kain / Captain / Akasha / Denali"
> "Vincent - Very powerful offensive hunter. Can take on nearly anyone thanks to
> his armor penetration skill (Only available to Guru 3 players)"

No stamina/fuel figures, hunter stat rows, level values or AP values appear in
this guide's text. **The images were the only possible stat source, and they are
gone.**

---

## 2. UNPUR[E] — everything that is not a verbatim reading

### 2.1 The single most useful thing recovered here is text, and its confidence tier

§1.5 is **player-reported, single-author, uncorroborated, undated-by-the-game**
prose. It is not native evidence, not a pixel reading and not a screenshot. Its
value is that it is *specific, internally consistent, internally patterned and
explicitly dated* — the Transcendence tables, for instance, form a clean
geometric progression per grade (crystals 5/15/45, 7/25/60, 9/30/80; rupee
amounts exactly 1000×crystals; fragments exactly 10×crystals; duplicate counts
1/2/3), and the skill-level costs step 100→1000 Rupees on a 5-level band
rhythm. **That internal structure is why it deserves cross-checking against any
other source rather than being adopted as-is.** Do not promote these to
"recovered" and do not let them silently replace the replica's documented
fixture economy (`AGENTS.md` §15 honesty rules; §15/§19 of this project's own
fixture caveats).

Cross-lane relevance, flagged not acted on: several of these are exactly the
values the replica currently guesses (`100 gold` per Raise source, 1-AP cruise
entry, placeholder Abyss/Ruins/fuel economy, `/gym/SkillUp` `100*destinationLV`
prices). This lane recovered **author-reported originals** for some of them.
**This subagent made no server change** — the numbers are recorded for a
deliberate, separately-reviewed decision.

### 2.2 Method trap: a rewritten image URL proves nothing

Wayback rewrote all 11 `img src` values inside the captured HTML into
`web/20180227140354im_/…` form — and every one of them 404s. **Wayback rewrites
`img src` to `im_` form whether or not the image itself was ever captured.**
So "the archived post body contains 11 rewritten image URLs" carries **zero**
information about byte availability, and `review-posts-2026-10-05.md` §1.1 row 8
plus its §4 line "11 in-game screenshots referenced, 0 opened" is exactly the
shape that invites a future lane to burn budget on these again.

The reliable discriminator, now settled for this namespace: **a CDX row.** And a
CDX row still needs a positive control before its absence means anything
(§1.3). Generalise the control requirement, not just this negative.

### 2.3 Budget transparency

The task budget was **10 image fetches**. Exactly 10 were spent, all on the
same timestamp advertised by the body, all 404. **No corrected-timestamp retry
batch was ever run**, because §1.3 proved no capture of these URLs exists at any
timestamp — so a retry batch would have been provably futile. `Cruising.png`
(`9d762be9`) was never fetched; §1.3 covers it. Zero CDN/OCR/bypass attempts,
zero retries of any image URL.

### 2.4 Era discipline, three separate problems

- **Post and screenshots are PRE-2019-09-05** (§1.4). Any numeral from this post
  belongs to the older equipment/crystal balance.
- **The body was captured 2018-02-27**, i.e. ~3.5 months after the post. The
  capture date is *later* than the content date but still pre-rebalance, so the
  era tag is unambiguous here. (Contrast `board-attachments-2026-10-05.md`
  §2.6, where 2021–2022 captures of 2017–2018 posts left the era genuinely
  unresolvable.)
- **The `Screenshot_2017-11-11-*` names are uploader-side filenames**, not
  device clock evidence and not archive timestamps. They are strong but not
  authoritative; treat as corroboration only.

### 2.5 Identity / level / gear tokens — all unusable, listed so none is mistaken for data

| Token | Where | Why it is not coverage |
|---|---|---|
| `Alaiko`, `Lv. 8 25/100` | author signature | author profile, not a hunter stat |
| `Cyana, Fin, KronX`, `Father` | signature, "hyper boosters" | team composition, no stats |
| `Hermes, Karl, Nene, Athena` | Ruins 3★ trace sources | **named as content, no numbers attached** |
| `Hermes, Octavia, Vincent, Captain, Diana, Lantern, Patrone, Levi, Karl` / `Athena, Nene, Kain, Captain, Akasha, Denali` | arena team lists | qualitative roles/tiers, **no HP/ATK/DEF, no levels** |
| `Guru 3` | Vincent armor-penetration gate | a rank band, not a stat |
| `Views 1571`, `Votes 0`, `Reply 5` | post header | forum counters |
| `1-star`…`5-stars`, `T1/T2/T3`, skill levels 1–49 | §1.5 | grade/level **indices** in cost tables, never attached to a stat |
| `2017.11.12`, `2017-11-11`, `20180227140354` | post, filenames, capture | dates |

**A caution worth recording:** this list contains several **hunter names that do
appear in the recovered catalog** (Nene `003`, Vincent `010` in
`polluted-observations.md`). **No number exists next to any of them**, so none
may be joined to any other source's values. A name-only mention is the single
easiest way to manufacture a fake base tuple; it is refused here explicitly.

### 2.6 Zero pixels means zero chance to grade identity confidence

The task asked to "record level/rank/gear state visible per panel". **That is
impossible here**: with no pixels there is no panel, and therefore no visible
level, rank, gear, jewel or skill state for anything. This is not a limitation of
reading quality — it is an absence of data. Any future claim that this corpus
"shows" a level or a gear state would be fabricated.

---

## 3. Negative results preserved

| Target | Check | Result |
|---|---|---|
| The 11 `565/745/197/` screenshots, bytes | 10 `im_` fetches at the body-advertised timestamp | **10/10 HTTP 404**, all 4,727-byte `<!DOCTYPE html` Wayback error pages, no PNG signature |
| Same 11, index presence | 5 CDX queries: exact (no port), exact (`:80`), prefix `565/745/197*`, prefix `565/745/`, domain-wide regex — **all statuses** | **0 rows every time** |
| Whole `565/` attachment namespace | Domain-wide regex on `/files/attach/images/565/` | **0 rows** — the namespace has no captures at all |
| Query-method validity of those zeros | Same query shape vs known-downloaded `75605/303/534/001` | **4 rows returned** — method sound, negatives real |
| Live origin file | `http://bs.visualshower.com/files/attach/images/565/745/197/9997745….png` | **HTTP 503**; `https://` TLS failure. No non-archive fallback |
| `Cruising.png` (`9d762be9…`) bytes | Not fetched — budget exhausted | Untested as bytes, but **settled by index: 0 rows**, same as the other ten |
| Any HP / ATK / DEF numeral in this corpus | 0 images decoded | **Zero.** Nothing was pixel-inspected |
| Any stat panel, hunter detail, gear or jewel row | 0 images decoded | **Zero** |

**Verdict: `share_en/197745`'s 11 screenshots are unrecoverable. This lead is
closed, not deferred.**

The *other* half of `review-posts-2026-10-05.md` §3 remains open and untouched:
`share_en` still has **105 distinct archived post ids / 833 CDX rows** that no
prior pass enumerated, and this pass recovered the correct body-extraction method
for them (§1.2: read `alt` + `src` from the captured post HTML). That board is
still the best remaining player-authored source — but note the yield here was
**text**, and the `565/745/197/` namespace being empty means a `share_en` sweep
must locate each post's *actual* prefix rather than assume `565`.

---

## 4. Coverage disposition / files updated

- **New base-stat tuples: 0.** No image was opened. Hero **1/113**, accessories
  **1/100**, monsters **0/22** — unchanged.
- **No coverage inflation.** The 11 filenames and the guide's named hunters are
  recorded as *identity/context only*. No filename was allowed to imply a
  subject it cannot prove, and no name was allowed to imply a number.
- **Polluted ledger:** `polluted-observations.md` gains an appended section with
  the identity/level tokens (§2.5) and the named-hunter list — **no numeric
  duplication**, because there are no numeric readings to record.
- **Era:** every value in §1.5 and §2.5 is tagged **PRE-2019-09-05** and must not
  be mixed with `stat-version-context.md`'s post-rebalance multipliers.
- **Cross-lane lead, not acted on:** §1.5 supplies author-reported originals for
  economy values the replica currently treats as fixtures (Abyss reset
  `30,000 Rupees / 30 Manda`, cruise fuel `6` then `7`, Ruins `20` fuel with no
  time limit, Abyss stage rewards `1/1/2/2/3` crystals, Advance fodder
  `1/2/3/4`, full Transcendence and skill-level cost tables). **No server,
  fixture or test was changed by this subagent**; adopting any of it is a
  separate, reviewed decision.
- **Files written:** this file (new); `polluted-observations.md` (section
  appended). `coverage.md`, `README.md`, the TSVs, `server-ts`, the APK and all
  seeds are **untouched**. **No server/APK/state change, no emulator or phone
  contact, no Ghidra run, no native library read, no archive write or re-upload,
  no login, no form submission.** Downloads were written only to
  `%TEMP%\blustone-share-en` and are 404 error pages.
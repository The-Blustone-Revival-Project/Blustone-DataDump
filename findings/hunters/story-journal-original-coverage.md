# Original Story journal material coverage

2026-10-09. Read-only inspection of preserved public PAD assets, existing
reference/localization exports and catalogue notes. No Ghidra, adb, runtime,
server source, original asset or private account changes. This concerns
`CSRTableDlgCollection`, the Village Story journal, not the Episode graph.

## Result

Original dialogue **resource bodies exist**, including twelve starter-Hunter
`DI` scripts and 120 starter `CM` scripts. Original `/reference/GetDialog`
catalogue rows were **not recovered in the inspected sources**. Resource names,
XML conversation IDs and Episode graph IDs must not be relabelled as original
GetDialog reference IDs.

Root's independently recovered `CSRDlgInfo::SetDialog` contract accepts bare
`ret_data[]` rows with `id`, `res_prefix`, `title`, `desc`, `movie_res`,
`thumb_res`, `serial`, `type_param`, `type`, and `playtime`; see
`analysis/ghidra-story-journal-keys.txt`. A script proves its own named resource
and narrative, not a complete row in that contract. No original binding from
these resources to an archive row's reference identity, thumbnail, ordering,
type, gate or playtime was found here.

## Exact original dialogue packages

Source directory:
`recovered-assets/phone-2026-09-18/extracted/split_PADResource/assets/`.
The header walk uses 24-byte outer records, packed length at +8, uint64 name
at +12 decoded with base38 `0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ._`; each
selected body was zlib-inflated and its RW envelope's XML at +6 parsed.

`DIAL-EN.jet` walks exactly to EOF at 3,133,395 bytes, with 1,357 records.
Prefix counts: AD0 108; DG0 26; DG8 23; DG9 6; CM0 558; DI0 294;
EP_ 237; MS0 41; MS1 25; NPC 39. These are inventory prefixes, not recovered
archive category enum values.

`DIAL-KO.jet` walks exactly to EOF at 3,462,962 bytes. The selected starter
resource names also exist there. Its preserved Korean dialogue is readable;
the old CHAR_STR catalogue's mojibake caveat does not apply to these XML bodies.

The exact twelve DI resources inspected follow. Header offsets and packed
lengths are for EN, then KO. Text count counts nonempty `Dialogue Text` fields,
not path traversal, translations' length or estimated playback seconds.

- `DI00101`: EN 1703242 / 2112; KO 1883133 / 2290; 16 texts in both.
- `DI00103`: EN 1705378 / 1870; KO 1885447 / 2073; 12 texts in both.
- `DI00105`: EN 1707272 / 2183; KO 1887544 / 2459; 15 texts in both.
- `DI00201`: EN 1709479 / 1699; KO 1890027 / 1848; 11 texts in both.
- `DI00203`: EN 1711202 / 1777; KO 1891899 / 1899; 12 texts in both.
- `DI00205`: EN 1713003 / 1961; KO 1893822 / 2115; 15 texts in both.
- `DI00301`: EN 1714988 / 2207; KO 1895961 / 2364; 20 texts in both.
- `DI00303`: EN 1717219 / 1931; KO 1898349 / 2130; 15 texts in both.
- `DI00305`: EN 1719174 / 2321; KO 1900503 / 2461; 19 texts in both.
- `DI00350`: EN 1721519 / 2144; KO 1902988 / 2336; 16 texts in both.
- `DI00403`: EN 1723687 / 2149; KO 1905348 / 2282; 19 texts in both.
- `DI00405`: EN 1725860 / 1857; KO 1907654 / 2024; 14 texts in both.

Every inspected DI body's `ConditionsString` fields are empty. That does not
prove archive eligibility is unconditional: eligibility can reside in the
server reference's `type_param` and native journal logic.

DI00101 directly identifies Lantern with Actor CardType `Char`, CardID `001`,
Name `Lantern`; the cast also contains player `%user_name%` / Char009 and
Lottery Mouse / NPC004. Its conversation fields say Title `Midgard` and
Description `미드가드`. Those generic script-conversation values are not
evidence for the archive's intended title/description. Its original
UserScript references `N004_BG`; merely publishing a catalogue row would
therefore require checking the script's full resource dependency set too.
Other DI text explicitly names Mowgli, Nene or Tyltyl or concerns their
advancement; numeric suffixes must not be used to infer rank gates.

Both languages contain exactly thirty scripts per prefix CM001, CM002,
CM003 and CM004. For each, exact suffixes are
`00,03,05,10,13,15,20,23,25,30,33,35,40,43,45,50,53,55,60,63,65,70,73,75,80,83,85,90,93,95`.
These are named resource coverage only; this task did not infer a CM dialogue
collection binding or reclassify them as journal stories.

## Existing exports and original UI

`analysis/recovered-data/leveldb-tables/all-tables.json` contains thirteen
tables: SKILL_REF_RO, SKILL_TAG_RO, SKILL_EFFECT_RO, SKILL_DESC_RO, TAG_REF_RO,
CHAR_STR_RO, INGAME_TALK_RO, ADMIN_ID_RO, UI_EPISODE_RO, UI_TEXT_RO,
UI_JSON_RO, UI_XML_RO and BADWORD_RO. None is a recovered dialog catalogue.
Existing `analysis/catalogue/cards/001.md` through `004.md`, cards.json and
char-str.tsv supply Hunter presentation and narrative descriptions; they do
not supply the eleven GetDialog fields as original complete rows.

UI_XML_RO contains exact original `KO/SR_MAIN/8_SR_STORY`. This has:

- `TA_MEMBER` vertical table and hidden `BTN_STORY_CELL` template;
- separate hidden `PA_GLOBAL_STORY` and `PA_HUNTER_STORY` headers;
- `TXT_STORY_NAME`, `TXT_STORY_DESC`, dynamically blank `ANIM_CHAR`;
- `UI_CM_LI_NEW` / `UI_TR_NEW`, and `MA_ST_PLAY` artwork.

The table export contains no EN-prefixed counterpart for this key. This
source-local absence does not diagnose the active seeded client's locale:
existing +12 native journal entry is already documented in AGENTS §112.
No broad locale copy or client patch is justified by this inventory.

UI_JSON_RO has exact English localized styling rows:

- `이야기 이름|TXT_STORY_NAME|EN`: `Story`;
- `이야기 내용|TXT_STORY_DESC|EN`: `Title`;
- `이야기_신규|F_STORY|EN`, `이야기|F_STORY|EN`, and
  `이야기|TX_MA_STORY|EN`: `Story`.

These are UI labels/placeholders, not story catalogue titles. The separate
`스토리|TX_EP_STORY|EN` value `Story %s` and KO/EPISODE/E_C_STORY,
KO/EPISODE/E_T_STORY concern Episode UI and cannot supply journal rows.

## Metadata search limits and missing evidence

Filename inventories of both final public PAD assets and
`analysis/extracted/assets` contain DIAL locale/background packages, but no
R_DIAL, R_DIALOG or STORY metadata package. `R_EPISODE.jet` is present and is
the separate Episode graph, not a substitute.

A complete twenty-one-record LEVELING.jet RW header/body inventory contains
ADJUST, ANVILHEATED, COMMON, COMMON_DESC, CONTENTCTRL, ENVIRONMENTS, EXPLORE,
FISHING, GACHA_THROW, ten LEVELING variants, MONSTER_RANK and NAMINGBOX.
No dialogue catalogue was found there. This is a bounded source inventory,
not a claim that no surviving original server cache exists anywhere.

`analysis/VSFan/Research/Blustone/API Endpoints.md` names GetDialog without
a populated contract/response. The inspected sources therefore do not close
original archive `id`, `type_param`, type enum assignment, serial, title,
description, movie/thumbnail binding or playtime. Any later consciously local
catalogue reconstruction must label those choices as local policy, keep
resource IDs distinct from reference IDs and preserve native gates rather
than claiming an original table was recovered.

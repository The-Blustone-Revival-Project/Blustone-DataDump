# Numeric card role and element enums

2026-10-03. Read-only native inspection, using Capstone over the original
extracted library. No Ghidra, adb, client patch or server edits. Addresses are
Ghidra image addresses (ELF+0x10000). These mappings are independent of screen
icon interpretation and are usable for catalogue-to-reference conversion.

## 1. Implementation mapping

**[RECOVERED] role mapping**, from `SRGetRoleDesc(CHAR_ROLE)` (`0x10ade8c`):

- **1 = Offense** — localized-text key 공격수 (attacker).
- **2 = Defense** — localized-text key 수비수 (defender).
- **3 = Bomber** — localized-text key 폭격수 (bomber).
- **4 = Support** — localized-text key 도우미 (helper).

The English names above are the established catalogue vocabulary; the native
function pins the numeric values through Korean localization keys. It does
not simply index four presumed icon meanings.

**[RECOVERED] element mapping**, from `SRAttribToString(CHAR_ATTRIB)`
(`0x10ae2f0`), which returns literal enum names:

- **0 = NONE** — literal `ATTR::NONE`.
- **1 = Fire** — literal `ATTR::FIRE`.
- **2 = Ice** — literal `ATTR::ICE`.
- **3 = Lightning** — literal `ATTR::ELECTRIC`; Lightning is the catalogue name.

Do not interchange Ice and Lightning. Unknown/missing element is not Fire;
there is a distinct native NONE0. Unknown role values should remain unresolved;
the recovered role description function returns an empty shared string for
values outside1..4, which does not establish a named role0.

## 2. Role dispatch: exact branches and literals

`SRGetRoleDesc` returns a string via hidden return pointer r0; enum is r1.
It subtracts1, bounds-checks0..3, then uses a Thumb byte branch table:

```text
010ade92 subs r0,r1,#1
010ade94 cmp r0,#3
010ade96 bhi 0x010adeac           // unknown -> shared empty string
010ade98 tbb [pc,r0]
```

The four bytes at `0x10ade9c..0x10ade9f` select:

```text
role1 -> 0x10adea0
role2 -> 0x10adeba
role3 -> 0x10adec6
role4 -> 0x10aded2
```

Each arm loads a PC-relative localization key and calls
`CGMDataMgr::GetLocalizedText` at `0x10adede`:

```text
role1 slot0x10adee4 + PC0x10adeac ->0x1d90e3e 공격수
role2 slot0x10adee8 + PC0x10adec6 ->0x1d90e48 수비수
role3 slot0x10adeec + PC0x10aded2 ->0x1d90e52 폭격수
role4 slot0x10adef0 + PC0x10adede ->0x1d90e5c 도우미
```

These register-matched pairings were read from the actual instruction listing;
the strict resolver omits the keys because of interleaved moves. Its incomplete
output is not evidence that the dispatch lacks named text.

## 3. Element dispatch: explicit enum-name strings

`SRAttribToString` checks enum r1<=3 (`0x10ae2fe..0x10ae308`) then dispatches
through `tbb [pc,r1]` at `0x10ae30a`. Bytes at `0x10ae30e..0x10ae311` select:

```text
attr0 ->0x10ae312 -> literal ATTR::NONE
attr1 ->0x10ae39c -> literal ATTR::FIRE
attr2 ->0x10ae3a2 -> literal ATTR::ICE
attr3 ->0x10ae3a8 -> literal ATTR::ELECTRIC
```

The four strings reside at `0x1d948cc`, `0x1d948d7`, `0x1d948e2`,
`0x1d948ec`. Out-of-range values enter an assertion with literal
`enAttrib is not valid.`; do not extrapolate a fourth named element.

Independent confirmation: `SRGetAttrDesc` (`0x10ade30`) compares enum r1
directly against1/2/3 and chooses localized text keys:

```text
attr1 slot0x10ade7c + PC0x10ade4e ->0x1d946b9 화염 (flame/fire)
attr2 slot0x10ade80 + PC0x10ade66 ->0x1d946c0 얼음 (ice)
attr3 slot0x10ade84 + PC0x10ade5a ->0x1d946c7 전기 (electricity)
```

## 4. Where these values live and a naming trap

`CSRCardInfo::GetRefRole` (`0x87aeee`) returns reference member+0x68;
`GetRefAttr` (`0x87aef2`) returns+0x6c. Their setter signatures use CHAR_ROLE
and CHAR_ATTRIB respectively. An instance's GetInstRole/GetInstAttr resolves
the normal card reference or its awakened reference; awake-step lookup is a
separate contract, not a reason to renumber the enums.

**[RECOVERED]** `SRCanUseSkillAirShip` (`0x10ae4b0`) returns true exactly for
role3 or4:

```text
subs r1,r0,#3
movs r0,#0
cmp r1,#2
movlo r0,#1
```

`CSRGameActor::IsSupport` (`0x97ecc0`) retrieves role from its stat-default
record and tail-calls this function. Therefore **IsSupport here includes
Bomber3 and Support4** (airship skill users); its name cannot establish that
the single helper role equals3. Use the description dispatch for enum meaning.

Icon utilities independently bounds-check element1..3 and role1..4, but their
pointer tables need relocation-aware interpretation. No icon-name mapping is
claimed from raw on-disk absolute pointer words.

## 5. Catalogue application and limits

`analysis/catalogue/data/card-catalogue.tsv` rows corroborate semantic content:

- Lantern001: Bomber/Fire -> role3,attr1.
- Mowgli002: Offense/Lightning -> role1,attr3.
- Nene003: Defense/Ice -> role2,attr2.
- Tyltyl004: Support/Fire -> role4,attr1.

These are catalogue-derived identities combined with the independently recovered
numeric mapping. Current fixture role1/attr1 describes an Offense/Fire card,
even if its art belongs to Lantern. Publishing a roster faithfully requires
mapping each row's known role/element rather than cloning1/1 for all art ids.
The parent-observed role1 sword/Offense and attr1 red scissors/Fire are useful
runtime controls, but the complete mappings above are proved by native text
dispatch. This lane performed no new runtime control.

**[UNKNOWN]** Numeric card stats, effect enums, awakened-reference fixtures,
and resource coverage for a new roster. Correct metadata enums alone do not
make a character playable or reconstruct its skills.

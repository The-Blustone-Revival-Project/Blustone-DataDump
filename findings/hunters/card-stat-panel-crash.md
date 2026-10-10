# Card popup map::at: missing reference skills, not yet a UI diagnosis

2026-10-03. Read-only Capstone/offline literal research over the original
extracted library; no Ghidra, adb, patch, or server edit. This report is the only
new workspace write. Addresses are Ghidra = ELF +0x10000.

## Finding

> **CORRECTION after the first native control:** the map key is **type**, not
> target_rank. The first version of this report misidentified the parser object
> base; publishing five type0 rows still leaves keys1..5 absent. See §3 for
> the pinned base+offset arithmetic. This is a retraction of the original
> implementation recommendation, not a new UI hypothesis.

**[RECOVERED]** The normal card popup unconditionally reads reference skills
**1..5** with `std::map::at`. Original published cards have `skill:[]`, so
`CSRCardInfo::GetSkillInfo(0,1)` cannot succeed. This is a concrete server
content defect sufficient to produce the measured exception. It is not proof
that no UI-resource gap remains after fixing it.

**[RETRACTION]** The old `in-game-stats.md` attribution to SetStatPanel and a
missing EN document is unproved. Candidate `0xb95dc3` is a Thumb return address
after `CMComponentPlayer::Play`; it can remain on the scanned stack after the
function returns. The caller invokes reference-skill map lookup immediately
after SetStatPanel. The signal handler scans stack words, not actual unwind
frames. An animation return address cannot establish the throw site.

## 1. Exact popup control flow and three different maps

`CSRPopUpCardInfo::SetData` starts at `0xb93be4`, not `0xb95dc3`. Its supplied
shared pointer is a `CSRCellDeck`. It stores the argument pointer at sp+0x34
(`0xb93c12`) and cell at this+0x658 (`0xb93c28`). Cell+8 is a shared CSRCard:
`0xb93c66` loads it and `0xb93c82` passes it to `CSRCardAnalyzer::Load`.

`0xb94206` calls SetStatPanel (`0xb95518`) and **returns before** skill setup.
It then runs a loop beginning with slot1 (`mov.w r10,#1` at `0xb94262`) and
increments through slot5 (`0xb94438`; exits at cmp6 `0xb9443c`).

### Map A: instance skill levels, required keys1..5

The loop retrieves cell+8 CSRCard again at `0xb9428e..0xb94292`, then accesses
its map at CSRCard+0x34 (tree root+0x38) at `0xb942a8..0xb942d8`. It searches
numeric slot key r10 (`0xb942e8..0xb942f6`) and loads node+0x14 as the current
skill level (`0xb94302`). Missing key branches to the inline map::at throw at
`0xb944e8`.

**[RECOVERED]** `CSRCard::parse` (`0x8680a4`) consumes
`skill_1_level`..`skill_5_level` and inserts all five keys even if a level is0.
For example key1 insertion at `0x868b28..0x868b2a` stores key1 and the parsed
level together; no zero-level guard skips insertion. Current `cardInstance`
already supplies all five numeric fields. This map therefore needs no shape
change for ordinarily parsed current inventory.

### Map B: awakened reference skill map, conditional

If the selected card has awake_step!=0 (`0xb94342..0xb94344`), the loop calls
`CSRAwake::FindAwakeRef` and looks up that reference's skill map root+0x40 at
`0xb9439c..0xb943c2`. Missing slot branches to second inline map::at throw
`0xb944f0`. **This is not an equipment map.** Current awake_step0 skips this
branch.

### Map C: normal reference skill map, actual empty current table

For awake_step0 the loop calls
`CSRCardInfo::GetSkillInfo(awake_step,slot)` (`0x87aef8`) at `0xb9440a`.
The helper's normal path reads the map tree root **CSRCardInfo+0xb0** at
`0x87af82`. It searches slot key r4 (`0x87af8e..0x87af98`); a missing slot
branches to `0x87af9c`, which loads `map::at: key not found` and calls the
throw helper `0x6d8570` at `0x87afa0`. On success it returns the SRSKILL_INFO
at node+0x14. The awake branch has its own equivalent throw at `0x87af44`.

Current `skill:[]` means SetCard inserts no entries, so **every current card
has an empty normal reference-skill map**. The first lookup for slot1 fails.
Changing stat rows, card name, or EN alias coverage cannot populate this map.

## 2. SetStatPanel and the misleading candidate

`SetStatPanel` (`0xb95518..0xb9610c`) formats HP/ATK/DEF and related derived
numbers, updates UI children, then finds UI cast `PA_CHA_POPUP` at
`0xb95d6c..0xb95d7c`. It finds/creates a CMComponentPlayer, sets group `draw`
(`0xb95d9c..0xb95daa`), then calls Play at `0xb95dbe`, returning to
`0xb95dc2` (Thumb candidate `0xb95dc3`). There is **no direct map::at throw
literal or integer-tree lookup in SetStatPanel**.

The old saved crash log also contains a return candidate inside
CMComponentPlayer::Play and regex/locale cleanup. Those are consistent with
earlier popup animation execution, but do not distinguish active frames from
residue. Do not mask Play or the exception on this evidence. The recovered
missing map should be fixed and tested first.

## 3. Parser-ready minimal reference skill array

`CSRCardInfoContainer::SetCard` (`0x87baa4`) iterates each card's **skill array**
(`0x87c3e2..0x87c47e`). It calls `SRSKILL_INFO::parse` (`0xf219ac`) at
`0x87c466`, then `CSRCardInfo::SetSkillInfo` at `0x87c470`.

**The map key comes from `type`, not `target_rank`.** Retraction: the report's
first version wrongly equated sp+0x98 with the parser object's base. The actual
base is r6 = **sp+0x70**:

```text
0087bc66 add r6,sp,#0x70          // establish reusable scratch object base
0087c220 add r6,sp,#0x70          // restore it after the equipment loop
0087c42a add.w r0,r6,#0x10       // initialize strings within the skill object
0087c438 vst1.64 {d8,d9},[r0],r2 // other initialization; r6 remains base
0087c464 mov r0,r6               // parse object starts at sp+0x70
0087c466 bl SRSKILL_INFO::parse
0087c46a ldr r1,[sp,#0x98]       // base+0x28, NOT base+0
0087c46e mov r2,r6               // complete object argument
0087c470 bl CSRCardInfo::SetSkillInfo
```

SRSKILL_INFO::parse stores `target_rank` at object+0 (`0xf21a1c`) and **type**
at object+0x28 (`0xf21afe`). Therefore the caller's sp+0x98 key is **type**.
The preexisting decompile independently corroborates it:
`parse(&uStack_160); SetSkillInfo(uStack_138,&uStack_160)`; their offset is
0x28. Records with **type1..5** populate the mandatory slots. Five records
with target_rank1..5 but type0 all address the same key0 and still fail.

Required per-record fields, recovered from operand flow and string conversions:

- `target_rank`: number, parsed first, separate unlock-rank metadata.
- `name`, `desc`: strings, converted unconditionally by from_json<string> at
  `0xf21a2e`, `0xf21a7a`.
- `type`: scalar number, parsed at `0xf21ab6`, stored+0x28; **reference map
  key**, required values1..5 on this popup path.
- `effect`: collection; zero size skips the entire nested effect parser
  (`0xf21b0e`, `0xf21b26`, `0xf21b30` -> `0xf225d6`). An empty array is a
  supported structural value. Nonempty effects need recovered effect_type,
  target_type,target_stat and value arithmetic, not guessed enum codes.
- `cool_time`, `cost`, `crt_chance`: scalar numeric conversions at
  `0xf22686`, `0xf22708`, `0xf22756`.
- `cut_in_id`, `icon_id`: strings, unconditional conversions at
  `0xf227b2`, `0xf227fe`. Missing/null is unsafe even if effects are empty.

Minimal **[FIXTURE]** record for each type1..5 (target_rank may match the type
as an explicitly local unlock convention):

```json
{
  "target_rank": 1,
  "name": "Local skill 1",
  "desc": "Skill effects have not been reconstructed.",
  "type": 1,
  "effect": [],
  "cool_time": 0,
  "cost": 0,
  "crt_chance": 0,
  "cut_in_id": "",
  "icon_id": ""
}
```

The schema is recovered; fixture values and inert effects are not original
skills. Supply all five records for every published card. An icon string is
loaded by SetSkillPanel via CSRUIImageNode::LoadAnim at `0xb96198`, so a
nonempty **verified resource name** is preferable to an empty id once the
resource map is checked. No particular original icon binding was verified
by this lane. Empty icon string may exercise the existing missing-animation
guard and must be tested, not declared safe from parsing alone.

Recovered semantic text exists in
`analysis/recovered-data/leveldb-tables/skill-ref.tsv`, keyed by card/skill id
and row, and `skill-tag.tsv` keyed by id/slot. For card001 these describe
frontline damage/immunity penetration, defence weakening, initial team attack,
conditional added damage, and team enhancement. Those can supply truthful
descriptive prose, but the numeric effect protocol must stay **[UNKNOWN]**
until reconstructed. Do not advertise working damage effects from display text.

## 4. Validation and remaining uncertainty

1. Server contract: every published card reference has **type** keys1..5
   exactly once, all strict string fields, all five instance-level fields.
2. Fresh native reference sync; open Gym and single-tap a target, then long
   press the same card from Build Team. Record whether card details now render
   and whether all five skill panels show their descriptions.
3. Confirm no map::at exception, then continue unlock/source selection/Raise.
4. If another throw remains, use its fresh return candidates and identify the
   actual at-reader; do not restore the historical missing-EN conclusion by
   default.

**[UNKNOWN]** Which at-reader produced the historical crash at runtime. Map C
is a proved incompatible current fixture and the first missing reference skill
is reached on the recovered normal control flow. This is sufficient to justify
the server fix, but only a successful fresh control can close the runtime cause.
Equipment reference tables remain empty; no equipment map throw was pinned on
this popup path, and this report does not justify expanding equipment scope.

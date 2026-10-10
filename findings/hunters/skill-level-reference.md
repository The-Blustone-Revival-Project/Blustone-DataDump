# Hunter skill-level reference contract and missing original balance

2026-10-04. Read-only original-library Capstone inspection, existing native research, preserved guide, and public community material. No server/client/tool/original edits, adb or Ghidra. Native addresses below are Ghidra image addresses (ELF+0x10000).

## Exact network table: GetLevel.skill

[RECOVERED] `CSRUserLV::SetLevel` (0x109f114), skill section0x109fd80..0x10a0314, first indexes **ret_data.skill** and iterates its rows. It reads **role, level, rank, gold** as numeric values. It also loops source index1..4 and formats the string fields **source_%s_ref_id**, numeric fields **source_%s_qty**. This is an ordinary row collection, not a map whose keys are skill-slot ids and not the unrelated LEVELING.jet tuning data.

Candidate parser-complete response (numbers and material ids **illustrative fixtures**, not recovered original costs):

```json
{"result_code":1,"ret_data":{"user":[],"vip":[],"vip_group":[],
 "card":[],"card_awk":[],"skill":[
  {"role":1,"level":1,"rank":1,"gold":0,
   "source_1_ref_id":"","source_1_qty":0,
   "source_2_ref_id":"","source_2_qty":0,
   "source_3_ref_id":"","source_3_qty":0,
   "source_4_ref_id":"","source_4_qty":0}
 ]}}
```

This illustrates the skill-row schema only. Do not replace existing working sibling card/user/vip data with the empty example collections.

Exact evidence:

- skill key: `ldr0x109fd80`, literal slot0x109ff08, addPC0x109fd88 ->0x1d6fe3e **skill**.
- role: load0x109fe50, operator[] call0x109fe56; role selects a map at **CSRUserLV+0x90** (tree root+0x94).
- level: load0x109ffb0, operator[]0x109ffb6, converted value retained in sl.
- rank: load0x10a0002, operator[]0x10a0008, converted value retained in r4.
- gold: load0x10a004e, operator[]0x10a0054; scalar stored at local record+8.
- `strd sl,r4,[sp,#0xa0]` at0x10a00ca establishes row layout **level+0, rank+4**; `str r0,[sp,#0xa8]` at0x10a00c8 gives gold+8.
- source loop initializes1 at0x10a00d4 and terminates on5 at0x10a0102..104. Each material entry has16bytes: std::string ref_id followed by quantity.
- ref format: load0x10a0116 ->slot0x10a030c; addPC0x10a0120 ->0x1d9419d **source_%s_ref_id**. It is passed to formatting at0x10a0124 and row operator[]0x10a0160; string conversion at0x10a016e.
- qty format: load0x10a0182 ->slot0x10a0310; addPC0x10a018e ->0x1d941ae **source_%s_qty**; row operator[]0x10a01ca followed by scalar conversion. Quantity lands after each material string.
- finished row is appended to the role vector at0x10a0256..0x10a027a, stride **0x4c=76bytes**.

The two generated keys are register-matched load/add pairs with interleaved instructions. The strict adjacent-only resolver omits them; manual surrounding operand flow above resolves them without widening that resolver globally.

## What determines the displayed cap

[RECOVERED] `GetCardSkillMaxLevel(CHAR_ROLE,unsigned)` at **0x10a1078** looks up the role's vector, then returns:

```text
max(row.level for rows whose row.rank <= supplied hunter rank)
missing role or empty vector -> 0
```

Evidence: role lookup0x10a1088..0x10a10aa; missing/empty returns0 at0x10a10ac/0x10a10b6; each row advances0x4c at0x10a10be, reads rank+4 at0x10a10c4 and skips when rank>r2, reads level+0 at0x10a10ca and maximizes it. There is **no fixed rank-times10 constant in this getter**: the server rows determine the cap.

This explains the current **1/0** skill panel: an instance can carry skill level1 while `starterLevels.skill=[]` yields cap0. Increasing the instance level would not reconstruct its cap table.

[RECOVERED] `GetCardSkillUpPrice(CHAR_ROLE,unsigned level)` at **0x10a0f60** reads the same role vector. If count>=requested level it returns **vector[level-1]**, not a search by row.level. Count arithmetic/row stride is0x4c at0x10a1044..0x10a1062. Missing/out-of-range returns the initialized default price record. Level0 is unsafe: unsigned(level-1) can enter the throwing bounds branch. Publish **dense ordered level1..N rows per role**, consistent row.level values, and never request price for0.

The table is a **skill-level/price/cap table**, not a skill XP curve. Material reference ids and quantities are part of it; no min_exp field is read in this skill section.

## Original caps and slot eligibility

[COMMUNITY-SOURCED] [Namu hunter training section](https://d.namu.moe/w/%EB%B8%94%EB%A3%A8%EC%8A%A4%ED%86%A4/%ED%97%8C%ED%84%B0#s-1.5) says skill maximum increases by **10 for each hunter grade**, and lists material bands1–4,5–9,…45–50. Exact update/build date for those values is not pinned. The page's material tables are historical community evidence, not original captured GetLevel responses.

[INFERRED FROM COMMUNITY RULE] Caps **10/20/30/40/50 for hunter ranks1/2/3/4/5** are the natural candidate mapping. The prose gives increments10 and bands ending50, but does not separately print each rank's cap. Do not label the inferred full mapping as captured production data. Native support is configurable via each row.rank; role1..4 need their own dense vectors. Lantern Bomber=3 and Mowgli Offense=1 use distinct role groups despite identical prospective cap schedules.

**Slot unlock and skill-level cap are different contracts.** `SRSKILL_INFO.target_rank` governs reference unlock metadata; its map key is `type`1..5, per `card-stat-panel-crash.md`. Current target_rank1..5 is explicitly a fixture convention. Preserved FAQ skill-priority paragraph associates later enemy-debuff/fifth skills with reaching5★, corroborating a fifth-slot rank5 gate, but this pass does not prove every original slot's exact target_rank or its detailed active eligibility predicate. Keep all five reference slots even while locked, since the card popup reads them all.

The preserved FAQ's **50/50/50** list refers to equipment, not skill caps; it cannot be cited as original skill maximum evidence.

## Shipped data and remaining unknowns

All21 `analysis/extracted/assets/LEVELING.jet` chunks were re-read through the byte-faithful walker. None contains source_1_ref_id/source_1_qty, upgrade_exp/min_exp, skill_level/skill_max. Existing `training-raise-followup.md` establishes that LEVELING uses **CSRLevelData**, distinct from network **CSRUserLV**. Its level/rank/hyper power recommendations are not a substitute for this table.

[UNKNOWN original balance] Per-role/per-level gold and material reference ids/quantities; exact row.rank cutoffs across final2.8.0.1; awake-specific alterations; skill-up response/consumption semantics and all original numeric effect scaling. The Namu material bands can guide independent validation but do not determine actual item ids or gold. Do not implement material consumption from translated ingredient names.

**Practical minimum:** publish a clearly marked coherent skill reference fixture to remove max0, covering each published role and dense levels. A cap restoration can use the community-derived10-per-grade schedule with provenance, while costs remain explicit fixtures and skill-up mutation stays separate until its parser/accounting contract is recovered. This lane made no implementation or live claim.

## Zero-material price safety: additional native consumer check

[RECOVERED] `CSRPopUpSkillUp::SetPriceInfo` (0xd5aa00) loops four material entries. At0xd5aa88 it computes price+index*16; at0xd5aa8c it reads quantity+0x18 (base material string+0xc, quantity after12bytes). **cmpqty0 / beqnext** at0xd5aa8e..90 skips AddStuff (call0xd5aaa0) entirely when quantity0. Empty ref ids therefore never reach item-reference rendering in this path if all four quantities are0. Gold is read independently at price+8,0xd5ab72.

`SetItemPosByItemCnt` (0xd574a0) hides four material panels, then **count0 branches to cleanup** at0xd574e6..e8 ->0xd575ae before division/layout. `RefreshItem` (0xd5aca4) compares material-vector begin/end at0xd5acce..d0 and skips item updates when empty. These three guards support a gold-only price fixture with four empty string refs/zero quantities. Native UI control remains required; this is concrete consumer proof, not a claim of completed runtime validation.

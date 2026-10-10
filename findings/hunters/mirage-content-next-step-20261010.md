# Mirage: next original-content and consumer proof

2026-10-10. Read-only source/material inspection by the Mirage research lane.
No ADB, UI, Ghidra invocation, Docker, server change, account change or stat hunt.

The next useful Mirage milestone is **a correctly rendered, nonempty native
stair selector with a proven route into its confirmation screen**. It requires
closing `ParseStairInfo` and its draw consumers first. Adding another empty
DTO, adjusting the already-working countdown, or calling a refused mutation
would not advance playable Mirage.

## What the current replica actually supports

`server-ts/src/mirage.ts` returns an initial read-only lobby: floor/stair/state
zero; no entries, deck, enemies, stairs or rotating heroes. The UTC Monday
deadline is explicitly a local policy. `state.ts` authenticates all Mirage
routes, returns that lobby for GetInfo, and refuses other routes with 2001.
`tests/mirage-contract.ts` checks clock rollover/range, authentication, refused
mutations and unchanged state. It does **not** test a floor, battle, stair,
reward, HP carryover or original rotation. Native empty Floor0 entry is covered
by `analysis/testing/mirage-001/report.md` and the entry-policy note.

The archived guide's daily run reset is separate from rotating active hunters.
Consequently the Monday `ref_hero.end_ltime` policy alone does not prove a wrong
daily reset, and changing it to midnight would conflate two clocks. A daily run
transaction remains absent; its timezone and final-version behavior are unknown.

## Available original material

The preserved phone PAD contains `MIRAGE.jet`, 3,861,142 bytes, SHA-256
`d2cf0adca895de1174f35f507cf5e38a21b8e74572a5c895c50ad6c062f4374e`.
An in-memory `jet_decoder.inspect_file` inspection reports **30 resources**;
all 30 exposed inflated resource variants begin `I2`. This is positive evidence
for original visual material, **not** floor, grade, balance or reward rows.
No RW/AT/S2 variant was exposed by that bounded decoder inspection. Do not turn
that result into a claim that the entire game lacks separate animation metadata.
The pack's deployed status was not established by this lane.

The existing native literal vocabulary contains `MIRAGE/MIRAGE_STAIR`,
`MIRAGE_`, `MIRAGE_COMPLETE`, and `MIRAGE_STAGE`. These are resource/UI names;
they are not enemy or stair server identities.

`analysis/research/vsfan-extracted-assets.md` records original archived in-game
help from APK **1.4.4.1/code1441**, source
`analysis/VSFan/Extracted Assets (2026)/1441 (APK)/UI_CSV/3d98d128.json`.
The APK SHA is `0fbd1e08dc6e0dbdf9ecf972552c9de52fc4fd86b4b573af52935e8296199f4a`.
Historical CONTENTS9_2..12 describes: strongest copy of duplicate hunters
locked into a sortie; 5-vs-5; HP persists across battles; dead hunters require
Manda first aid; midnight daily reentry/reset; active hunters rotate every few
days; three battles for floors1–20, six for21–40, nine for41+; assignment depends
on average team combat power. These give intended semantics, **not final 2.8.0.1
numeric balance, floor assignment, prices, reward magnitudes or hero rotations**.
This task used the preserved primary material, without a new web/stat search.

## Concrete missing seam and bounded reverse plan

1. Root exports **ParseStairInfo G9343b4** and **GetStairInfo G92eb5c** from the
   original library. Existing `ghidra-mirage-strings-09.txt` proves its exact keys:
   `res_prefix`, `res_postfix_list`, `list`, `grade`, `balance`. It does not prove
   that `grade`/`balance` are top-level; ADD sites934672/934678 occur after list
   selection9345b4. Close row nesting, scalar types, list order/count, map key and
   storage before implementing a nonempty reference.
2. Export **CSRPopUpExploreMirage::CreateStair Gbf9948** and
   **CSRExploreMirageStairDraw::Init(int,REWARD_TYPE) G93a600** plus
   **CalcState G93b28c**. Trace the exact resource-name composition, UI slots,
   stair-index range and enum meaning. `SetGrade G93be98`, `SetState G93c3d8`
   and `SetBG G93ca44` are bounded follow-ups only if those consumers need them.
   Match those names against the original MIRAGE package tree, not pack names.
3. Close **GetNextFloor request G9322d8**, its result callback and state gates
   before enabling a stair click. Determine what GetInfo's `reset/stay/entry`
   flags actually transact; the current read ignores them. Stage enumeration
   and background `bg_res` must come from consumer evidence. Render a nonempty
   original stair layout only once every required row value has provenance;
   unresolved floor values should remain explicitly unresolved.
4. For combat, use published card references and art, not campaign monster
   IDs. Parse_InstEnemy **G92dff4** uses `n`, `ref_id`, rank/progression/skill
   levels. Existing `native-makestageinst.txt` shows MakeStageInst selects a
   stair entry and derives a float multiplier from its stored balance, default
   1.0 only on a lookup miss. Thus inventing balance0 or ignoring a missing
   stair is a material combat change; resolve the native scale constant and
   field semantics before a battle trial.
5. Complete original **End G92ed08** and **Reward G932e4c** callbacks before
   persisting HP/floor progression or payout. End request vocabulary includes
   `inst_id`, `hp_percent`, `floor`, `stair`, `remain_deck_hp`, `remain_enemy_hp`;
   the catalog alone does not establish their exact nesting/units/authority.
   Add ownership, duplicate-ref selection, carried HP and repeat-claim checks
   only after the recovered transaction semantics are concrete.

Acceptance should demonstrate original stair artwork, selected stair/grade,
correct confirmation participants, native battle and subsequent carried HP on
the next stair. Preserve all unrelated accounts. Until then report Mirage as
entry verified, combat and original content unreconstructed.

## Root export follow-up: exact row/storage contract

Reviewed fresh `analysis/ghidra-mirage-stair-consumers.txt` against the exact
literal bindings in `ghidra-mirage-strings-09.txt`. This supersedes the missing
parser-body portions of steps1–2 above; original row **values** remain unknown.

`ParseStairInfo` stores `res_prefix` as a libc++ string at model+0x74.
`res_postfix_list` must be a JSON **array** to replace the native vector;
elements pass strict string conversion, with 12-byte strings stored in the
vector header at model+0x80/0x84/0x88. Nonarray input skips the replacement,
so malformed data can retain an older cached vector rather than clear it.

`list` likewise must be a JSON **array**. Only that branch clears/rebuilds the
list at model+0x8c/0x90/0x94. Each **list element** supplies `grade` and `balance`;
these fields are **not** top-level `ref_stair` fields. The parser generates
one-based ordinal indices in iteration order, beginning1, with no explicit
server stair-ID field read. Native allocation is20 bytes per linked node:
links+0/+4, generated index+8, balance+0xc, grade+0x10. Count is model+0x94.
Both scalar fields are converted to32-bit numeric storage; numeric strings
and doubles convert through integer truncation, booleans through a byte,
integers through their low32 bits; unsupported types become0. The replica
should publish deliberate integers, not depend on permissive native coercion.

The recovered wire shape is therefore
`ref_stair: {res_prefix: string, res_postfix_list: string[], list: [{grade: integer, balance: integer}, ...]}`.
This establishes nesting and order, **not** legal grade values, actual row
count, original balance magnitudes or postfix membership.

`CalcState` and `Init` use the same comparisons: read current stair at
GetBaseInfo()+0x44; candidate above current gives drawstate4; below current
gives1; equal current gives2 when GetBaseInfo()+0==1, gives3 when that field==2,
otherwise1. These are numeric branches only: final state labels and the exact
GetBaseInfo returned base pointer must be corroborated by the next export.
`Init` stores the drawstate at drawable+0x840, and toggles different child nodes
for those states. It also compares candidate index with
GetStairInfo()+0x20 (the apparent count) for an additional display branch.
No fixed3/6/9 native cap is established by this body.

`CreateStair` calls `Init`, obtains GetStairInfo/GetResName, concatenates their
returned strings and calls SetBG. It selects a status-name string through
cases1..4/default. **Exact background composition, suffix selection and status
labels are intentionally pending** GetResName/SetBG and exact string bindings;
do not infer a concrete res_prefix/postfix pairing from these call names.
The decompiler labels Init void while CreateStair consumes its apparent return,
so the return register/dataflow needs original instruction corroboration before
using this discrepancy as an enum or callback proof.

This closes the initial row-shape research gap. Next bounded work is the
resource/consumer follow-up and original values, followed by state transactions;
there is still no evidence permitting a ready-to-play arbitrary floor fixture.

## Resource and balance follow-up: prior uncertainties closed

Reviewed root's `mirage-stair-consumer-contract-20261010.md` against fresh
`ghidra-mirage-stair-bindings.txt`, `-postfix.txt`, `-draw-strings.txt`,
`-grade-table-asm.txt`, `-grade-literals.txt`, `-grade-zero.txt`,
`-init-return-asm.txt` and `ghidra-mirage-balance-literal.txt`. The following
supersedes the pending composition/grade/return/scale statements above.

- GetStairInfo returns model+0x74; GetResName returns model+0xc4. CreateStair
  concatenates that prefix and **current selected postfix** before SetBG.
  SetBG finds BG_STAGE and uses Load9Sprite with the node's existing size and
  9-sprite ratio. This is not evidence that the whole MIRAGE package name is
  the intended background name.
- MakeRandResPostFix chooses a postfix index in0..count−1 and copies its string
  to model+0xc4. Its body has no local empty-vector check. An empty lobby's
  acceptance does not license activation of this random-postfix path; the
  caller/admission gate still needs recovery.
- The four-entry native string table is grade0 **empty**, grade1 **B**, grade2
  **S**, grade3 **G**. Grade0's original literal starts NUL; it is not a missing
  resolved string. Init/SetGrade index12-byte entries directly without a local
  bounds check. Only table indices0..3 have established storage; original
  grade assignment is unknown. Reward-box names use MS_RW_ plus the grade;
  opened sprites append8 and lock names use MIRAGE_ plus grade. These names
  still need actual original pack ownership matching before deployment.
- Exact status-name bindings are1 CLEARED,2 FIGHTABLE,3 RECEIVABLE,4 LOCKED,
  default STATE_NONE. Original Init assembly loads drawable+0x840 into r4 at
  G93ada8 and returns r0=r4 at G93adfc on the successful epilogue, closing
  the misleading void decompiler signature.
- G925dd0's float word **0x38d1b717** decodes to
  **0.00009999999747378752**, approximately0.0001. With the existing signed32
  row-balance conversion, balance10000 yields native float1.0; balance100
  yields approximately0.01. A selected zero balance yields0; the lookup-miss
  fallback alone yields1.0. This is a recovered scale, **not** an original
  neutral floor row or permission to fabricate balance10000.

No blocking inconsistency was found in the root consumer contract. These
proofs enable precise schema/resource validation but do not restore original
floor values or server transitions. The next highest-value export remains
GetNextFloor G9322d8 and its actual continuation/admission, including when the
random postfix is selected. No Mirage deployment or UI trial occurred.

## Next-floor builder and response continuation

Reviewed fresh `ghidra-mirage-nextfloor-builder.txt`, `-strings.txt`,
`-callback-slots.txt`, `-callback-vptrs.txt`, `-callbacks.txt` and
`-callback-strings.txt`. The actual builder G9322d8 sends only five normal
authentication fields: **app_code, app_ver, market, pvid, otp** to
**/mirage/GetNextFloor**. It does not publish floor/stair, deck, hunter IDs,
remaining HP, reset, entry or stay parameters. Older catalog signatures or
inferred gameplay parameters must not override this actual builder.

The proven response continuation **G938a60** defaults its callback scalar to0.
Only result_code1 plus present `ret_data` proceeds to
**ret_data.next_floor** numeric conversion. Missing ret_data/refusal and
unsupported selected scalar types yield0; integer types use low32bits,
booleans a byte, and string/double conversions are truncated with a positive
value test. The conversion is a32-bit scalar, despite the decompiler typing
its register as a JSON pointer. It invokes the captured callback with the
original request/response and that scalar when the callback is nonnull.

The body contains no Parse_InstBase/ParseStairInfo/MakeRandResPostFix call and
no write to Mirage model state. It therefore does **not** by itself load a
next floor, replace enemies, refresh resources or begin combat. Caller-side
admission and the captured callback's handling remain open. A successful
invented next_floor response would not restore those transactions. Selection
of `next_floor` uses operator[]; the body's explicit presence test is for
ret_data, so absence of the inner field should not be generalized independently
of that operator's null/missing-key behavior.

Root also independently checked the scale word in the original ELF at915dd0
(G925dd0). No route activation, server write or Mirage UI action occurred.

# Native Training Raise restored

The revival goal remains active. This checkpoint restores another real village
workflow; it does not establish faithful economy, full skills or all training.

## Verified native flow

Village → Training → hunter info → Train → select disposable source →
Successful Training → final LV2/Strength57 → fresh app bootstrap retains LV2.
Only granted duplicate3 was consumed. Original instances1/2 remain owned and
locked. Native request was target1, source_inst_list"[3]", is_tuto"0". Gold
11270→11170, target XP0→100. Lock toggle was authenticated host-side for the
known donor ID, not exercised through native UI.

The trained leader then entered a rendered battle; player HP1018→1006 and
poses/parallax changed. Explicit exit gave victory and returned to Red Rock.
Timer/turn and enemy HP did not change in the observed frames; do not claim
natural victory or completed combat restoration.

Evidence: `testing/revival-002.md` and its screenshots24,26..31,34..39.

## Why hunter selection previously crashed

The popup reads normal reference skill keys1..5 even when skills are locked.
`GetCard` published empty skill tables. Minimal parser-compatible slots fixed
that dependency only after correcting their key to **type**, not target_rank.
The first research recommendation confused object base with field offset and
its native control still crashed. Root disassembly proved parser base sp70,
key load sp98, therefore SRSKILL_INFO+0x28 TYPE. Explicit correction remains in
`research/card-stat-panel-crash.md`; no native throw was masked and no APK or
UI seed changed. Earlier missing-EN diagnosis was not the cause on this path.

All five rows are neutral display fixtures: empty effects, generic names,
unknown icons/cut-ins and zero costs/cooldowns. Combat skill effects remain
unimplemented; visible slots are not proof of authentic skills.

## Server behavior and limits

Starter ownership is now snapshotted per account, so feeding a starter does not
recreate it on restart. Recruitment remains persistent. Native ToggleLock and
LevelUp response nesting was recovered; training validates ownership, source
uniqueness, locks, leader/deck/battle protection, gold and published XP cap
before committing consumption/XP/gold together. Lobby/pre-battle EXP matches
inventory. Non-success native callbacks skip mutation parsing; local refusal
code2001 is a fixture mapping.

Current network curve is deliberately only rank1 levels1..2, max100XP.
Source XP100/200 and price100/source derive from the replica's published fixture
tables and native arithmetic. Original curves and ordinary Raise prices are
unknown. Tests cover transaction/refusal, persistence, consumption/reseeding,
lock reload, profile consistency and required reference types. npm test and
npm run build pass.

Result popup showed Power273 versus preview/final57. Fuel UI50 versus server49
and stage totals remain inconsistent. These are open native presentation/data
issues, not hidden by passing server tests. Private pre-training save backup is
gitignored server-ts/data/state-before-training.json.

## Newly recovered evidence for further work

`research/card-enums.md` pins numeric role/element labels from native switches.
This removes the old enum uncertainty and supports faithful roster expansion.
Current bootstrap still gives Lantern an Offense role and Mowgli a Fire element;
these fixture assignments need replacement with proper party validation.

`research/training-public-evidence.md` records dated original-game screenshots
of historical3★LV30 max and3★→4★ advancement at12000 rupees/3 sources. Those
anchors cannot produce a genuine XP curve by interpolation. Use them with
explicit fixture curves if no further original data can be recovered.

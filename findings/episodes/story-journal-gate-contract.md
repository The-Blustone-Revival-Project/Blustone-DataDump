# Story journal eligibility and replay contract

2026-10-09. Read-only review of existing native exports. No Ghidra, adb,
server, runtime or original-material changes were made for this report.

## Return value recovered from instructions

`CSRTableDlgCollection::IsValidStory` at Ghidra `00fef524` really returns a
boolean-compatible value in ARM `r0`. Its current decompilation is typed
`void` and omits that value. The instruction export is authoritative:

- `fef532` initializes `r5 = 0`.
- `fef540..fef550` reads the length of INFO `type_param` at +0x3c. Empty
  strings branch directly to the epilogue, returning zero for **every type**.
- `fef55c..fef5a8` constructs `type_param.substr(1)` without validating the
  removed prefix byte. A one-character nonempty parameter produces an empty
  suffix; that is not rejected before the type-specific operation.
- `fef5aa..fef5b6` dispatches `type - 2`, bounded to 0..7. Types outside
  2..9 take the cleanup with the initially zero `r5`.
- `fefae0..fefaf2` verifies the stack canary, moves `r5` into `r0`, restores
  registers and returns. Cleanup calls do not define the eligibility result.

Consequently **type 1 is not an unconditional archive category**. Default,
type 7 and types outside the handled range return false. Type 9 returns true
(`fef652`) only after the nonempty-parameter precondition. The decompilation's
empty case 9 must not be interpreted as no action or false.

## Type-specific gates

The case assignments below come from the existing `ghidra-story-journal-table.txt`
switch decompilation; each result is checked against its retained instructions.

- **Types 2 and 3:** Parse the movie resource string at INFO +0x24, not the
  stripped `type_param`. The implementation removes its first two bytes and
  last byte, copies that intermediate value, uses its substring beginning at
  index 3 as `stoi(...,10)`, removes two more terminal bytes from the other
  copy, prefixes it with the relocated literal `Z`, then calls
  `CSRGameStage::GetStageData(key, parsed_number)` (`fef9aa..fef9d0`). A
  nonempty resulting stage-id field +0x1c is passed to
  `CSRPlayData::GetStageAchieveCnt`; any nonzero result normalizes to true
  (`fef9e4..fef9f8`). An empty stage-id field explicitly returns true
  (`fef9fc`). This permissive fallback is **not** evidence that a guessed
  movie resource grants legitimate entitlement. Short/malformed strings can
  throw or fail lookup; do not manufacture a grammar from resource names.
- **Type 4:** `CSRInventory::HasSeenCard(inventory, type_param.substr(1), 0)`
  (`fef656..fef666`). `fef66a` saves its returned `r0` in `r5`. Prefix bytes
  are discarded, not validated. The `0` argument is exact; its deeper meaning
  requires the HasSeenCard implementation and is not inferred here. Passing
  a single prefix character would ask HasSeenCard about an empty identity.
- **Type 5:** Gets the highest-rank owned card serial for the stripped
  parameter. A zero 64-bit serial returns false (`fef6c2..fef6c6`,
  `fefa38`). Otherwise `FindCardInstBySerial` supplies a card, whose rank at
  +0x24 is compared **unsigned** with INFO +0x48, the serial field. The
  comparison sets true for rank >= threshold (`fef71c..fef72c`). The
  `serial` field therefore participates in admission for this type; treating
  it only as display ordering would be unsafe.
- **Type 6:** Finds a bundle using the stripped parameter. Missing bundle
  returns false (`fef7ae..fef7b2`, `fefaa4`). Its reference requirements
  vector starts at bundle-reference +0x50. Each 0x1c record supplies a chain
  id at +0xc and required rank at +0x18; `FindCardChain` and
  `GetHighestRecordRank` produce the observed rank. Any unsigned observed
  rank below requirement returns false (`fefa96..fefa98`); all requirements
  passing, including an empty requirement vector, returns true (`fefaa0`).
- **Type 8:** Resolves `CSRRefData::GetScenarioDataByID` using the complete
  INFO row id at +0, then reads that scenario's stage id at +0x1c and calls
  `CSRPlayData::GetStageAchieveCnt` (`fef626..fef644`). Any nonzero count
  becomes true (`fef648..fef64e`). The stripped parameter is not used in
  this gate, but its original nonempty precondition still applies. Neither
  the original scenario binding nor a safe missing-scenario behavior is
  established by this export.
- **Type 9:** True after the shared nonempty-parameter check. Choosing type 9
  merely to display recovered bodies would explicitly remove stronger
  potential ownership, rank, bundle or scenario gates.

`CSRTableDlgCollection` construction (`feea50`) walks all `GetStories()` rows
and copies a row into the visible vector only when `IsValidStory != 0`.
Changing reference type or parameter therefore changes which stories can be
replayed, not just cosmetic presentation.

## Replay path and scope

The retained table click/replay function passes the selected visible row's
movie resource (+0x24, INFO stride 0x58) to `CSRUIModalHandler::PushDlg`, then
calls `CSRPopUpDlg::SetIgnoreGoTo(popup, 1)` on the returned popup. This shows
an explicit archive-replay suppression of dialogue GoTo behavior. It does not
prove every UserScript action is suppressed, that all resource dependencies
are present, or that publishing unknown rows preserves original eligibility.
Do not substitute an Episode reference identity for a journal identity.

## Publication opportunity and remaining evidence

Original DI bodies can supply exact movie-resource names and narratives.
They cannot supply original reference id, type, type_param, serial/rank gate,
thumbnail or duration. This review found **no entitlement-preserving original
journal row ready to publish**. In particular type 1 gives an empty result,
and type 9/nonempty synthetic parameters would bypass any stronger original
gate. Empty ConditionsString fields inside a DI script do not override these
reference-driven gates.

A separately documented local replay catalogue would be a new local policy,
not restoration of original archive eligibility. Even a local type-4
ownership gate cannot prove that an original higher-rank or bundle requirement
was preserved. Before representing original DI rows as restored, recover
original metadata or independent evidence of each intended gate and bind it
to the real reference identity. Also audit all named original resources and
actual replay effects; SetIgnoreGoTo alone is insufficient for that claim.

Evidence: `analysis/ghidra-story-journal-gates-instructions.txt`,
`analysis/ghidra-story-journal-gates-keys.txt` (relocated `Z`),
`analysis/ghidra-story-journal-table.txt`,
`analysis/ghidra-story-journal-keys.txt`, and
`analysis/research/story-journal-original-coverage.md`.

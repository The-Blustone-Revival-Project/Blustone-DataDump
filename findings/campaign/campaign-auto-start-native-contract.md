# Campaign automatic confirmation and start contract

Independent source review, 2026-10-09. This report uses retained native exports;
it performs no UI input, runtime mutation, native call or Ghidra operation.

## Evidence and admission

`ghidra-campaign-auto-confirm.txt` contains
`CSRSceneStageConfirm::OnReset` at Ghidra `00e7d124`. Its relocated-string
export binds the marker to **`MissionAutoPlayConfirm`** and its member to
**`autoplay`**. A null marker skips the automatic path. A non-null marker is
read and then removed before the admission test: the low byte of the converted
value must equal **1**. Presence alone is insufficient, and removal also occurs
when a present marker's value fails this test.

The admitted path finds **`PA_AUTO_FADE`**, makes it visible and starts motion
named **`auto_next`** (both motion string arguments resolve to that name,
`SRPlayMotion(..., 1)`). It registers an animation event callback with
`CMComponentAnimBase::AddEventCB`. This is a client-side confirmation mechanism;
it does not itself establish a server-configured automatic-combat setting.

Root's pointer-registration proof ties that registration to the following
callback: literal `e7ecac` word `01303450` plus relocated PC/add base
`e7eaf0` gives primary `02181f40`; slot `+18` at `02181f58` contains Thumb
pointer `00e8c151`, whose instruction address is `00e8c150`.

## Event callback

`ghidra-auto-confirm-callback.txt` and its exact keys export recover the
previously anonymous Thumb function at **`00e8c150`**. It locks the captured
scene's weak ownership pair before using the scene. The event must have its
upper identifier word at `param_3+14` equal to zero, and its lower word at
`param_3+10` must match the function's CRC comparison for **`auto_next`**.
An arbitrary animation event is not sufficient.

It accesses button-map key **1** in the scene tree rooted at `scene+708`
(minimum/header at `+704`, count at `+70c`). OnReset's button construction
binds this key to **`PA_MISSION/BT_NEXT`**; key 0 belongs to
`PA_BATTLE/BT_NEXT`. The callback checks the byte at **button+270**.
Only a **zero** byte admits the automatic start. The retained exports do not
prove that field's setter or canonical semantic name: call it the `+270` gate,
not a proven disabled/enabled flag. As emitted, map access has insertion
semantics; the callback does not safely tolerate a missing mapped button
merely because it can insert a default pair.

If admitted, it finds `PA_AUTO_FADE`, hides it, and calls
**`CSRSceneStageConfirm::RequestStartMission`**. Failure of ownership, event
identity or the `+270` gate does not take that call. No repeated request loop
or delay length is established by these exports.

## Start request and refusals

`ghidra-auto-confirm-start-path.txt` recovers RequestStartMission at
**`00e879f8`**. It copies `CSRPlayData::GetCurDeck` and counts nonzero 64-bit
instance IDs. An empty vector or a vector with no nonzero IDs produces a
localized toast and returns without a start request. The export does not
resolve that toast's text; do not assign it a guessed message.

For a nonempty effective deck it looks up stage data using the scene's stage
string at **`+788`**, then compares `CalcTotalAP` against the stage record's
first word (the established stage `ap_cost` field). Enough AP, including
equality, leads through the data-sync singleton to
**`CSRSyncMStage::RequestStart(stage_id, callback)`**. Insufficient AP instead
constructs `CSRPopUpNoMoney`, calls `SetData(..., 1, cost-totalAP, callback)`
and pushes that popup; no mission start request is issued on this branch.

Thus automatic confirmation uses the ordinary deck and affordability checks.
It does not bypass AP, manufacture a deck or establish battle success.
The passed request callback's downstream result handling is outside this
review, as is any mechanism that initially writes the marker.

## Limits and next evidence

This closes a native path capable of starting a mission without a fresh
manual Begin press when its marker, animation event, button gate, deck and AP
conditions are met. It does **not** attribute the uncaptured intermediate
campaign wins or reward claims in §199. Confirm that attribution only with a
fresh trace of marker creation, event execution and the start request in the
same live sequence. The original animation's timing and the `+270` setter
remain separate verification targets. No source, runtime or saved progress
was changed by this review.

# Independent Mirage entry-flow review

Read-only review of root's original-library exports on 2026-10-10. No UI input, server edit, account mutation or Ghidra operation was performed by this reviewer.

## Caller admission

`ghidra-mirage-entry-flow.txt` exports `CSRPopUpExploreMirage::OnButtonClick` G bfa5d0. Its exact-string companion binds BTN_RENEW at the compare leading into the renewal branch, FIGHTABLE, RECEIVABLE, CLEARED and LOCKED at the four stair-button branches. The button comparisons require the secondary hash word at button+26c to be zero and the complemented primary hash at +268 to match. The decompiler's function signature is incomplete; its `param_1` is the popup object and `in_r2` supplies the button.

BTN_RENEW first compares the value at popup+ c28 -> +294 with an unidentified scene-manager virtual+44 result called with argument2. Equal values produce a toast. When unequal, base state2 also produces a toast; state1 builds and pushes a Yes/No confirmation popup; state0 directly constructs the captured callback and calls RequestNextFloor. Other state values do not call it on this branch. Thus a button press alone does not prove next-floor admission, and the compared value's meaning is not established by this export.

The direct state0 RequestNextFloor capture is a heap object0x18 bytes, with vptr expression `DAT_00bfb0f4 + 0xbfadd2`. It retains the popup weak owner in two capture pairs and the then-current base state at +c. State1's confirmation Yes event is a heap object0x14 bytes with vptr `DAT_00bfad5c + 0xbfaa9e`; its callback behavior must be exported before claiming that Yes advances or refreshes the model. No direct parsing of returned floor references is visible in this caller.

FIGHTABLE is admitted only while popup byte+65d is zero. It sets that latch to1, visits the stair draws to stop/play the corresponding animations, then pushes scene0x7a with a fade. RECEIVABLE reads base+44 and base+40 and passes RequestReward the arguments `(base+40, base+44, callback)`. It uses inline callback vptr `DAT_00bfad6c + 0xbfac16`. CLEARED and LOCKED produce toasts; LOCKED's text depends on base state1 versus2. Before these stair branches, the shared path requires popup byte+660 nonzero and the recorded coordinate popup+664/+668 outside the PA_SHOP cast's rectangle. These facts do not close battle preparation or reward settlement.

## Random postfix selection

`CSRPopUpExploreMirage::RefreshList` G bf8d9c clears TV_LIST and calls MakeRandResPostFix **whenever base state equals1**, before it accesses the stair-row list. There is no vector nonempty check, row-count check, current-stair check or `param_1` gate around this call. The exported caller reference is G bf8f50. Consequently a state1 model with an empty `res_postfix_list` is unsafe even if no stair rows are deployed; the existing state0 empty lobby avoids this branch. Since the call occurs on each qualifying refresh, the resource postfix is not proven stable for a whole floor.

RefreshList then copies the stair rows and limits visible rows to `3 * trunc((current_stair - 1) / 3) + 3`, removing excess rows from the tail. This describes three-stair display groups, not an original total stair count or floor difficulty assignment. Current-stair0 and malformed scalar behavior should not be generalized from this display formula.

## Remaining closure

The actual renewal reply callback and confirmation Yes callback must establish behavior for scalar0, nonzero floor, owner expiration, possible base/stair refresh, and any use of the captured state. Reference row domains, random postfix corpus, original grade/balance values and transactions remain unrecovered. The existing stair-consumer note is consistent with these exports; its prior warning about an empty postfix vector is strengthened by this unconditional state1 refresh admission.

## Renewal continuation review

Fresh `ghidra-mirage-renew-invoke-slots.txt` proves the odd callable slots Gbfdeed and Gbfca79. Their even Thumb entries are exported in `ghidra-mirage-renew-continuations.txt`.

Gbfdeec consumes the delegated next-floor scalar and compares it with current base+40 immediately. It does not inspect GetResultCode. This is significant because the lower RequestNextFloor wrapper already delegates0 on failure. Equal values issue `RequestInfo(1,1,0x1f,callback,0)` unconditionally at this level; the callback retains the second weak-owner capture. Different values construct RetryConfirm and call `SetDetail(current_floor < next_floor, next_floor)`. Event pools+9c and+b8 and its deactivate callback are registered; only afterward does it weak-lock the first popup owner to clear byte+65e and push RetryConfirm. Expired owner therefore prevents that popup push, but does not precede the equal-value HTTP request. Event semantics remain for root's next exports.

Gbfca78, confirmation Yes, first weak-locks the first owner and requires its raw pointer nonzero. It then reads the current base state and issues RequestNextFloor with the same0x18-byte continuation capture: first weak pair, captured state+c, second weak pair. It does not itself reset or advance a floor.

`ghidra-mirage-decomp-08.txt` RequestInfo G92b30c together with exact strings07 shows that arguments1,1 select wire strings `reset:"t"` and `stay:"t"`; bitmask0x1f selects all five request section flags (`entry`, `inst_base`, `inst_enemy`, `ref_stair_list`, `ref_hero`) as `"t"`. Thus current Floor0 plus a refused GetNextFloor still takes an explicit reset/stay GetInfo branch. In the reviewed current `server-ts/src/state.ts`, mirageAction returns a successful mirageLobby envelope for every GetInfo payload without inspecting reset. Saved data is not modified by that implementation, but claiming it refuses reset/admission would be false: it acknowledges the reset-shaped request. A server correction should distinguish this request from ordinary read-only refresh, with native error handling first verified. Returning a nonzero invented next_floor to avoid the equality branch would fabricate domain data and lead to RetryConfirm rather than reconstruct the missing system.

## Server correction review

Root's subsequent state.ts change checks reset after `accountFor` authentication. Explicit `t`, `true`, `1`, boolean true and numeric1 now return failure2001; ordinary absent/false/zero requests retain the same lobby response. The branch calls neither gameFor nor persist and contains no wallet, deck, hunter or progression mutation. No blocking source issue was found. This closes acknowledgment of the recovered reset path; it does not implement Mirage runs.

`ghidra-mirage-retry-events.txt` proves equal-path callback Gbfd250 first clears popup latch+65e if its weak owner can be locked, then checks GetResultCode. Non1 exits before constructing RetryInfo; success1 constructs it and calls SetData(current floor). Therefore failure2001 is supported by this callback rather than merely inferred from convention. RetryConfirm's event callbacks Gbfe444 and Gbfe5e0 both request reset1 with all sections0x1f, selecting stay0 and stay1 respectively. The reset guard covers both forms independently of stay.

The reviewed test snapshots the complete game state before Mirage reads/refusals and compares it afterward; it checks next-floor refusal, reset failure without fake inst_base, normal-read success and missing-auth rejection. Minor fidelity improvements were sent to root: use entry:"t" in the all-section request and native false wire string"0" instead of"f", and optionally assert missing-auth reset refusal plus each accepted true encoding. This reviewer did not execute tests or deploy the change; root owns test/build and live validation evidence.

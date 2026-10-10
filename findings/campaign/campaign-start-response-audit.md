# Campaign Start response audit

Read-only source audit, 2026-10-09. No emulator inputs, Ghidra operation,
server edits or saved-state changes were performed for this audit.

## What is recovered

`analysis/native-monster-stage.txt:5971-6719` and
`analysis/native-network-decomp.txt:4220-4970` contain
`CSRSyncMStage::RequestStart` at Ghidra `00b39d2c`. It builds the
`/mission/Start` request from the stage string and exactly four current-deck
instance IDs, plus account/application form fields. This function forwards a
caller-supplied callback. Its own absence of response-body reads does not
establish what that callback consumes.

`analysis/ghidra-auto-confirm-start-path.txt:200-236` binds the ordinary
`CSRSceneStageConfirm::RequestStartMission` callback to a newly allocated
16-byte callable containing the stage string. Its primary function table is
constructed from the literal at `00e87ebc` plus `00e87c60`.

The retained registration instruction export confirms this arithmetic:
`ldr` at `00e87c4e`, `add r0,pc` at `00e87c54`, then `adds r0,#8` at
`00e87c5a`. The fresh retained memory export gives literal word `012fa690`.
Thus the primary table is **`021822f0`**, with invoke slot `+18` at
**`02182308`**. Root's retained table read gives odd Thumb pointer
`00e8e671`; the actual instruction entry is **`00e8e670`**.

`analysis/ghidra-campaign-start-success-callback.txt` exports this entry in
proven Thumb mode. The callback calls `CPVHTTPResponse::GetResultCode` and
admits its entire success branch only when the returned code is **1**.
The exact key export `analysis/ghidra-campaign-start-success-keys.txt` binds
its two string references to `MissionAutoPlayResult` and `autoplay`.
On success it sets that marker member to 1, calls
`CSRUserDB::PutCurStageInfo` with its captured stage string and the supplied
vector's element count, then calls `CSRSceneMgr::PushSceneFadeOutIn` with
scene ID 4 and black fade color. It contains **no response JSON reads**:
`accepted`, `error_code`, reservation fields and scalar `ap` are not consumed
by this callable. On non-1 it returns without those success actions. No
retry or user-visible failure action exists in this callable; generic HTTP
handling outside it is a separate consumer.

The preparation checks are recovered independently: nonzero effective deck,
stage lookup, and `CalcTotalAP >= stage.ap_cost`. They can prevent requests
before the server is contacted, but do not prove server refusal handling.

## Correction to older evidence

`analysis/research/battle-lifecycle.md` claims high-confidence Start response
closure despite acknowledging that the exact receiver is unknown. It proposes
callback targets around `00e93b18` using table header `021822d0`.
`analysis/ghidra-campaign-auto-progress.txt` and
`analysis/ghidrewards-16-insn-scene-all.txt` now establish that this range is
inside `CSRSceneMStageMap::SetAutoProgress`: `00e93b18` follows the marker
lookup, and the surrounding code reads `MissionAutoPlay`, `stage` and
`autoplay`. Those addresses do not close the Start response consumer.

The corrected registration and actual callback now establish that there is
**no missing success-body field in this native scene callback**.
Do not add guessed `user`, `wave_list`, `monster` or EXP fields to Start on
the basis of that older report. The body is unused by this now-exported scene
receiver; this does not prove absence of generic HTTP-layer processing.

## Current replica and concrete verification gaps

Before this correction, `server-ts/src/state.ts::startMission` returned
`envelope`, hence `result_code:1`, for both admitted starts and two refusals:
`DECK_NOT_OWNED` and `AP_EMPTY`. Refusals were distinguished only by
`ret_data.accepted:false` and a local `error_code`. Other active-mode conflicts
use `failure(2001,...)`. The actual receiver **does not read** either refusal
field: result code 1 takes its scene-entry branch even for these bodies.
Thus the source contract mismatch is demonstrated. A live occurrence of a
rejected Start entering battle has not been captured.

The implemented correction overrides `result_code` and `code` to **2001**
on these two refusal envelopes, retaining inert refusal details in `ret_data`
and the shared protocol envelope. Exact 2001 is local policy; the native
callback establishes the required non-1 distinction. Admitted success and
idempotent branches are unchanged at code 1.

Read-only review of the final diff confirms that only these two Start refusal
returns and their comment changed in `state.ts`; Complete behavior is
unchanged. `tests/mission-start-admission.ts` freezes time and verifies AP0
refusal with unchanged game state, a funded start and AP0 retry, invalid deck
isolation while a reservation exists, persisted reservation replay and
expired unfunded refusal. `tests/native-card-identity.ts` additionally asserts
that a stale low instance ID returns non-1. Root reports full-suite/build and
deployment checks passed with all three saved games unchanged; this audit
reviewed their source coverage, not a new native refusal interaction.
This rule must **not** be generalized to `/mission/Complete`: its recovered
loss settlement still requires code 1 and a parsed settlement body.

Admitted replies contain local reservation fields (`battle_id`, `battle`,
`mission_id`, scalar `ap`). These are ignored by the scene callback.
The server charges fixed AP 1, matching all currently published stage rows'
`ap_cost:1`; this is local policy, not recovered original economy.
It also retains a historical empty-stage fallback to `n_01_01`, despite the
native RequestStart assertion requiring stage-string length greater than one.
That fallback is a server compatibility behavior, not original native intent.

## Next evidence

1. The two refusal-code corrections are implemented, tested and deployed.
   Native refusal UX remains unobserved; do not claim a rendered error or a
   recovered original error-code mapping.
2. Validate an actual native admitted Start sequence with the deployed receipt
   trace and confirm the corresponding Complete and EXP receipt.
3. Generic HTTP retry/error handling and battle construction after scene 4
   remain separate targets if a refused live Start needs deeper UX validation.

No conclusion here attributes the previously uncaptured automatic campaign
progression or proves that any live Start refusal occurred.

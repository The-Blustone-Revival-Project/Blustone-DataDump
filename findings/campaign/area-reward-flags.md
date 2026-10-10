# Lobby area reward flags: repeated claim rows, not a received array

2026-10-03. Read-only original-library Capstone research; no Ghidra, adb,
server/client edits or runtime control. Addresses are Ghidra=ELF+0x10000.

## 1. Recovered wire shape

`CSRPlayData::ParseMissionInfo` (`0xb68934`) reads
**ret_data.area_achieve** as a collection of row values. Each row has:

```json
{"area_id":"n_01","achieve_cnt":10}
```

The numeric value means **the reward threshold whose chest was received**,
not current total area stars. The native reader hard-codes:

- achieve_cnt10 -> received flag0.
- achieve_cnt20 -> received flag1.
- achieve_cnt30 -> received flag2.
- Other values -> no received flag set.

An account that received the first and third chests in n_01 and the second in
n_02 should reload with:

```json
{
  "result_code": 1,
  "ret_data": {
    "area_achieve": [
      {"area_id":"n_01","achieve_cnt":10},
      {"area_id":"n_01","achieve_cnt":30},
      {"area_id":"n_02","achieve_cnt":20}
    ]
  }
}
```

**No nested received array, JSON-in-string achievement value, or direct boolean
array is read here.** This is different from the stage achievement contract.
Multiple received chests in the same area need repeated area_id rows.

## 2. Field names, iteration and actual object bases

ParseMissionInfo first indexes full envelope.ret_data at `0xb68952`; saves that
object in r5, then indexes **area_achieve** at `0xb6895c`. Literal slot
`0xb68bd4` + PC `0xb6895e` -> `0x1d7c017` (`area_achieve`).

It iterates either an array or an object by **value**, at
`0xb6896e..0xb689c8`. The row is dereferenced into r0 at `0xb68a2a`, saved
in r4 at `0xb68a30`. Row.area_id is indexed at `0xb68a32` and converted to
string at `0xb68a40`. Its key is resolved by load `0xb68a00`, add `0xb68a02`,
PC `0xb68a06`, slot `0xb68bd8` -> `0x1d77725` (`area_id`).

`mov r0,r4` at `0xb68a46` proves that achieve_cnt is read from that SAME row;
operator[] at `0xb68a48`, scalar integer conversion finishes at `0xb68a94`.
Its literal load `0xb68a06`, add `0xb68a0a`, PC `0xb68a0e`, slot
`0xb68bdc` -> `0x1d7773c` (`achieve_cnt`).

The destination map is **CSRPlayData+0x288**, formed at
`0xb689f4..0xb689fe`. Its key is row.area_id, never the top-level JSON key.
Therefore an area-keyed object is not inherently an invalid JSON container,
but values such as `{achieve_cnt,received}` without area_id cannot identify
the correct native area. A flat array is the clearest recovered representation
and supports multiple claim rows for one area.

## 3. Flag writes and first-row creation

The existing-area path compares parsed achieve_cnt (r9):

```text
00b68a9e cmp r9,#0x1e        //30 -> third flag
00b68aa6 cmp r9,#0x14        //20 -> second flag
00b68aac cmp r9,#0xa         //10 -> first flag
```

The writes target node+0x28/0x29/0x2a:

```text
00b68ad0 strb 1,[node,#0x28]
00b68b3e strb 1,[node,#0x29]
00b68cf0 strb 1,[node,#0x2a]
```

For a missing area, the function constructs local AREA_ACHIEVE_INFO at
**sp+0xa8**, with string+0 and flags+0xc (sp+0xb4..0xb6), zero-initializes
those flags at `0xb68b00`/`0xb68b0a`, inserts/copies them to the node at
`0xb68c6a`/`0xb68c6e`, then applies the row's threshold too:

```text
00b68ccc cmp r9,#30
00b68cd0 bne 0xb68aa6        // resumes20/10 threshold checks
```

**Retraction of an intermediate hypothesis:** a bootstrap zero row is NOT
required before the first received row. That hypothesis stopped before this
tail branch. A first row with achieve_cnt10,20,30 initializes and sets its
flag correctly. Duplicate threshold rows are naturally idempotent.

`area_achieve:[]` processes no rows; it does not visibly clear a previously
populated map. An unclaimed area's row with achieve_cnt0 ensures its entry
exists but sets no flag; it likewise does not clear previously received flags.
Authoritative removal of a claimed chest on a live native model is not
established and is outside the ordinary persistent claim workflow.

## 4. Getter and incremental claim writer

`IsReceivedAchieveReward(area_id,int index)` (`0xb6d14c`) finds the area map,
returns0 if absent (`0xb6d188`), otherwise directly reads:

```text
00b6d180 add node,index
00b6d182 ldrb result,[node,#0x28]
```

`SetAchieveRewardReceived(area_id,int index)` (`0xb6d0fc`) ensures the map
entry, then stores1 at node+0x28+index (`0xb6d12a..0xb6d130`). These are
**zero-based reward indices0..2**, not threshold values10/20/30. Getter and
writer have no bounds check. Passing10 directly would write outside the
three-byte flag array.

The chest claim callback matches the response's achieve_cnt against the
reference reward rows, finds a reward index, then calls this incremental
writer (documented in chest-rewards.md). That explains why a chest can show
opened during the current session while a wrongly shaped lobby snapshot fails
to restore it later.

## 5. Server reconciliation

Current areaAchieveMap emits `{area_id-key:{achieve_cnt:current_star_total,
received:[flags]}}`. Both meaning and row identity disagree with this reader:
received is never consumed, top-level identity is ignored, and total stars30
would mean **third chest received**, regardless of whether it was claimed.

Publish one `{area_id,achieve_cnt}` row per persisted claimed chest; optionally
publish zero rows for unclaimed areas if another bootstrap reader needs their
existence. Do not synthesize received flags from current area progress.
Keep the server's persisted claim identity `(area_id,reward_threshold)` and
idempotent reward mutation; only its wire projection needs this correction.

The hard-coded10/20/30 is recovered client behavior. The current ten-stage
campaign's chest thresholds fit it; earlier minimal3/6/9 fixtures do not fit
this reload reader. Supporting arbitrary thresholds requires further native
evidence or an explicitly instrumented-client change, not changing the lobby
achieve_cnt meaning.

Native control: claim one real eligible chest, relaunch, revisit its map and
verify its opened appearance, then retry claim to verify no second reward.
Use a second chest in the same area to prove repeated-row reconstruction and
an unclaimed eligible chest to prove progress does not imply receipt.
This lane performed no new runtime control.

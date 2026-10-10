# Revival systems: energy synchronization and the next training seam

Date: 2026-10-03. Read-only research lane: no adb, Ghidra project, server
process, client changes, or source changes. This report is the only workspace
write. Native inspection used the existing hardened literal resolver and
Capstone 5.0.7 over the original extracted library. All addresses below are
Ghidra image addresses, i.e. file offset + `0x10000`.

## Priority

**[RECOVERED / current source]** The campaign now publishes five destinations
and 50 stages, but `LocalGameState` has no energy regeneration clock. That
makes continuing the campaign consume a finite fixture balance. Persistent
AP/BP regeneration is the highest-value immediate progression repair.

**[RECOVERED / current source]** The strongest next village workflow is Training
Raise (`/gym/LevelUp`), because its native request and response can now be
reconstructed exactly. It requires a persistent card-instance inventory first:
`/lobby/GetCardInven` currently returns `starterInventory`, while `gachaPremium`
advances the instance-id allocator and returns cards but does not store those
instances. Re-entering/restarting consequently loses locally received cards.
Fix that shared model before implementing destructive training.

Older documents are stale on two specific claims: Gym response shapes are no
longer all unknown, and the enhancement-price table has no generated outer key.
Do not alter their historical provenance; use the corrections below.

## 1. Energy: seconds and a next-charge deadline

**[RECOVERED]** `CSRPlayData::SyncAP(unsigned,uint64)` at `0xb6c95c`:

```text
00b6c95c str.w r2,[r0,#0x160]   // low 32 bits of time
00b6c960 str.w r1,[r0,#0x130]   // amount
00b6c964 bx lr
```

`SyncBP` at `0xb6c966` stores the corresponding values at `+0x164` and
`+0x134`. The `Ejy` suffix in both mangled symbols confirms unsigned amount
and unsigned-long-long time arguments. Under AAPCS the 64-bit argument is
aligned in `r2/r3`; only `r2` is stored by this client.

**[RECOVERED]** `CGMTime::GetCurServerTime` at `0x797628` calls
`RMGetTickCount` (`0x10ff8e8`), divides by `1000` (`mov.w r2,#0x3e8` at
`0x797632`), and adds the synchronized server anchor. Thus energy time fields
use seconds in the server-time coordinate, not JavaScript milliseconds.

**[RECOVERED]** `CalcAddtionalAP` at `0xb6cb18` reads the reference interval at
`CSRRefData+0x270`, converts float to integer, reads current server time and
`CSRPlayData+0x160`, then:

```text
00b6cbd0 vmov r1,s16
00b6cbd4 adds r2,r4,r1          // currentServerTime + interval
00b6cbd6 subs r0,r2,r0          // minus stored charge time
00b6cbe6 b.w 0x00e0b854        // signed integer divide
```

The interworking thunk `0xe0b854` loads a displacement at `0xe0b864`, adds
`0xe0b864`, and jumps to Thumb address `0x1be22dd`; its entry is
`0x1be22dc`. The body takes absolute values, performs integer division, and
restores sign (`0x1be2354..0x1be235c`). Therefore:

```text
additional_AP = trunc((now_seconds + interval_seconds - ap_charge_time)
                      / interval_seconds)
```

BP uses the identical construction at `0xb6ca40`, with interval at
`CSRRefData+0x274` and charge time at `+0x164`.

**[INFERRED from recovered arithmetic]** The published charge time is the
**next regeneration deadline**, not the timestamp of the last regeneration.
If the server's internal persistence tracks the last elapsed interval boundary
`anchor`, publish `anchor + interval`. Publishing `anchor` immediately adds one
point on the native client. A zero charge time is a fallback sentinel: the
client replaces it with current server time, also yielding one in this formula.

`CalcRemainApTime` (`0xb6c76c`) computes the same numerator, passes it through
division/remainder at `0xe0b4ec -> 0x1be23a0`, and returns `interval - remainder`
(`0xb6c82e`). This independently supports the deadline reading. Native total
AP (`0xb6c848`) adds the result to the synchronized amount and caps at
`max(baseAP,maxAP)`, preserving overflow balances above the normal maximum.

**[UNKNOWN]** Normal full-meter server convention (zero sentinel vs future
deadline) and original regeneration intervals. Existing 300/1800 second
values are replica fixtures. Server persistence may choose its own internal
clock format, but wire deadlines must agree with the formula above.

## 2. Training Raise: exact request and response

**[RECOVERED]** `CSRSyncCard::RequestLevelUp` (`0xf53698..0xf53f90`) posts
`/gym/LevelUp`. Its fields include:

- `target_inst_id`: decimal card-instance serial.
- `source_inst_list`: JSON serialization of the source-instance vector;
  `json::dump` is called at `0xf53908`, then the key is constructed at
  `0xf53912`.
- `is_tuto`: tutorial indicator. The hardened resolver misses this interleaved
  load; `ldr r1,[pc,#0x90]` at `0xf5391a`, `add r1,pc` at `0xf53926` resolves
  slot `0xf539ac` + PC `0xf5392a` to `0x1d7b2fb`, string `is_tuto`.
- Account/transport fields `app_code`, `app_ver`, `market`, `pvid` and
  session credentials are constructed by the same request builder.
  Follow-up correction: the resolver's `t` candidate is a wrong-PC pairing of
  a boolean value literal. It is not a request field or idempotency token;
  `is_tuto` is serialized as the strings `"0"` / `"1"`. See
  `training-raise-followup.md` for the exact register pairing.

**[RECOVERED]** `ReqLevelUpCB` (`0xf53f90..0xf546f0`) requires success code 1,
then indexes:

```json
{
  "result_code": 1,
  "ret_data": {
    "user": {
      "gold": { "prev": 1000, "cur": 900 },
      "deck": []
    },
    "card": {
      "target_inst": { "inst_id": 1, "exp": { "prev": 0, "cur": 100 } },
      "removed_inst_list": [ { "inst_id": 2 } ]
    }
  }
}
```

The numbers are **[FIXTURE example]**, not recovered costs/experience. The
`deck` value must carry the real deck-setting shape already published by the
replica; `[]` above illustrates an empty collection, not a validated filled
deck schema. The nesting and object-valued removal entries are recovered:

- `r6` holds `ret_data` after `0xf540b6`.
- `user` is indexed at `0xf540e4`, saved in `r4`; its `gold` is read at
  `0xf540ee`, followed by `prev`/`cur`.
- `mov r0,r4` at `0xf541a4` proves `deck` belongs to **user**, not ret_data.
  Its value goes to `CSRPlayData::ParseDeckSetting` (`0xb67cc0`) at
  `0xf541ae`. The current gold goes to playdata `+0x154` at `0xf541c0`.
- `mov r0,r6` at `0xf541c4` indexes ret_data.card; saved in `r10` at
  `0xf541cc`. Its target_inst is indexed at `0xf541d0`, then inst_id and
  exp.prev/cur. The target serial/current experience are passed to
  `CSRInventory::SetCardExp` (`0xae98a0`) at `0xf54330`.
- `mov r0,r10` at `0xf54362` proves removed_inst_list belongs to **card**.
  The per-element dereference at `0xf543f2` is indexed with **inst_id** at
  `0xf5441a`, converted to unsigned integer, and passed to
  `CSRInventory::RemoveCard` (`0xaebc44`) at `0xf54468`.
- The removal-entry key is another resolver false negative: load
  `0xf543cc`, slot `0xf546ec`, add `0xf543da` (PC `0xf543de`) resolves to
  `0x1d6eec9`, `inst_id`. **Do not send a bare integer list.**

`achievement` is null guarded at `0xf540c8`; omit it while unknown. The main
user/card nesting is indexed directly; do not replace it with generic mock
metadata or a flat card array. No consumed item/ticket shape was recovered in
this LevelUp callback.

## 3. Enhancement prices: correction to the old generated-key claim

**[RECOVERED]** `CSRCardInfoContainer::SetCardEnhancePrice`
(`0x87f048..0x87f2fc`) accepts the full response envelope and first indexes
**ret_data**, then its **level** and **rank** numeric collections. It does not
generate an outer key.

The missed first literal is:

```text
0087f062 ldr r1,[pc,#0x28c]       // slot 0x87f2f0
0087f064 str r0,[sp,#0x28]       // interleaved canary save
0087f066 mov r0,r2
0087f068 add r1,pc               // PC 0x87f06c
0087f06a bl 0x7930f8             // envelope["ret_data"]
```

The slot+PC resolves to `0x1d689bb` (`ret_data`). The numeric level elements
are pushed to vector `this+0x24`, numeric rank elements to `this+0x30`.
`GetCardRaisePrice` (`0x87f2fc`) and `GetCardRankUpPrice` (`0x87f322`)
select index `requested - 1`, with special case requested=0 selecting the
first element, and requests beyond length selecting the last. **Both vectors
must be nonempty**: empty vectors can be dereferenced before the beginning.

Publish `/reference/GetCardEnhancePrice` as:

```json
{ "result_code": 1, "ret_data": { "level": [100], "rank": [1000] } }
```

These example costs are **[FIXTURE]**. One-element vectors make the current
getter safe for all requested positive indices, but faithful prices need
recovered economy material or explicitly documented replica values.

**[RECOVERED]** `SetCardRankUp` (`0x87ec9c`) likewise first indexes envelope
**ret_data** (slot `0x87efd4` + PC `0x87ecc4`), then iterates its elements;
each element supplies `rank`, `src_cnt`, `stat_bonus`. The actual add at
`0x87ed50` yields **rank** at `0x1d6fa90`, not `e`. The resolver also reports
an `e` candidate with the wrong add PC here, demonstrating why literal counts
are not proof. `stat_bonus` is missed by the strict resolver: load
`0x87ee3e`, interleaved store, add `0x87ee44`, slot `0x87f044` + PC
`0x87ee48` resolves `0x1d6fec2`. Publish a direct array of rank records when
rank-up behavior is implemented; no generated-key wrapper is justified.

## 4. Concrete implementation queue

1. Persistent AP/BP interval clocks; publish next deadlines. Test boundary,
   partial interval preservation, full meter, server restart, and existing-state
   migration without awarding an arbitrary backlog.
2. Persist card instances per account, migrating starter roster once. Serve
   that inventory on boot and append recruitment grants to it. Preserve ids,
   selected leader/deck, and instance fields; a bootstrap array is reference
   content, not live inventory.
3. Publish nonempty enhancement-price vectors. Record costs as fixtures until
   better evidence is recovered. Separate the recovered shape from the values.
4. Implement Raise with the exact response above: validate target/source
   ownership, distinct source ids, no target among sources, locked sources,
   valid remaining deck, sufficient currency. Persist exp/gold/removals
   together before responding. Duplicate malformed requests must not partially
   consume inventory. Do not invent tutorial/reward claims.
5. Verify village Training -> choose target/fodder -> Raise -> popup -> re-enter
   card inventory -> restart -> same experience and missing fodder. Server-only
   tests establish persistence/contract; screenshots establish native usability.

Other areas remain valuable, but Arena/Guild specs mostly pin symbols and
containers without complete per-record parsers; Supply and Mail require deeper
attachment/reference recovery. Do not equate an empty-state response with a
completed playable system. This report did not verify any of these changes on
the emulator.

## Appendix A. Clock synchronization prerequisite discovered during runtime A/B

The parent observed native AP50/50 while host state had AP34 after publishing
absolute deadlines. This appendix identifies a separate missing clock anchor;
it does not claim the A/B outcome is settled.

**[RECOVERED] actual exercised initializer:**

```text
/reference/GetExtra
 -> CSRSyncRef::ReqExtraCB 0xf83988
 -> CSRRefData::SetExtra 0xdd819c
 -> CGMTime::SetTime 0x79794c, called at 0xdd855e
```

`ReqExtraCB` checks result_code==1 and tail-calls SetExtra at `0xf839aa` with
the full JSON. SetExtra indexes `ret_data` at `0xdd81c4` (slot `0xdd84ac` +
PC `0xdd81c6` -> `0x1d689bb`) and saves that object at `sp+0x5c`. Its four
clock reads all use that object:

- `server_utc`: ldr `0xdd83ea`, slot `0xdd84c8`, add `0xdd83ee`, PC
  `0xdd83f2` -> `0x1d88af6`. Value saved at `sp+0x70`.
- `local_time`: ldr `0xdd8436`, slot `0xdd84cc`, add `0xdd843c`, PC
  `0xdd8440` -> `0x1d88b01`. Saved at `sp+0x108`.
- `utc_0`: ldr `0xdd8484`, slot `0xdd84d0`, add `0xdd848a`, PC
  `0xdd848e` -> `0x1d88b0c`. Saved at `sp+0xe8`.
- `server_timestamp`: ldr `0xdd8500`, slot `0xdd8824`, add `0xdd8506`, PC
  `0xdd850a` -> `0x1d67719`. Saved at `sp+0x188`.

Each goes through scalar type-tag conversion (tags 3..7, including numbers and
numeric strings). Missing/null takes `movs r0,#0`; none has a parent null guard
that preserves an earlier clock value. JSON numbers are the appropriate wire
type; these values ultimately become signed 32-bit longs in this client.

`0xdd8552..0xdd855e` passes addresses of those four stack values to SetTime.
SetTime stores current tick seconds at `this+8`, `server_utc` at `+0x14`,
`local_time` at `+0x28`, `utc_0` at `+0x18`, and `server_timestamp` at `+0x20`.
For a zero fourth value it substitutes `utc_0 + 32400` (`movw r2,#0x7e90` at
`0x79796c`, conditional add at `0x79798a`). That 9-hour fallback is recovered;
its original timezone/day-boundary meaning is **[UNKNOWN]**.

Thus the client computes:

```text
current_server_seconds = ticks_ms/1000 + server_utc - initialization_ticks_seconds
current_local_seconds  = ticks_ms/1000 + local_time - initialization_ticks_seconds
current_utc0_seconds   = ticks_ms/1000 + utc_0 - initialization_ticks_seconds
```

**[RECOVERED / source snapshot]** Before the parent's correction, GetExtra
published none of these fields, so it synchronized server time to zero. An
absolute host-epoch energy deadline compared against that near-zero native
clock produces a large negative additional-energy quotient. CalcTotalAP adds
it to an unsigned amount and performs unsigned maximum comparisons, making
wraparound/full-meter display plausible. This is an **[INFERRED explanation]**
pending the runtime control, not a measured register trace.

The minimal proven correction is to publish numeric
`ret_data.server_utc = floor(Date.now()/1000)` in `/reference/GetExtra`, making
wire energy deadlines and the initialized server clock share a coordinate.
`local_time`/`utc_0` are independently named time anchors; the exact historical
timezone convention is unknown. A replica may explicitly choose UTC for those
coordinates, but must label that choice rather than claim a recovered Korean
or phone-local offset.

For completeness, standalone `CGMTime::ParseTime` (`0x7976f8`) reads
`server_timestamp`, `local_timestamp`, `utc0_timestamp` directly off its JSON
argument and stores the corresponding anchors. A read-only whole-library
Thumb BL scan found **no direct call to ParseTime**, but found the SetExtra
call to SetTime above. Therefore adding generic timestamps to envelope() is
not a demonstrated fix; use the named GetExtra fields at the proven callsite.

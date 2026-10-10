# Stage achievements: JSON-in-string lobby data and three zero-based flags

2026-10-03. Read-only native research with Capstone and existing dumps. No
Ghidra, adb, source changes or runtime control. Addresses are Ghidra=ELF+0x10000.

## 1. Exact lobby shape

**[RECOVERED]** `CSRPlayData::ParseMissionInfo` (`0xb68934`) consumes
`ret_data.stage` rows. The row fields are:

```json
{
  "stage_id": "n_01_01",
  "achieve": "[{\"order\":0},{\"order\":1},{\"order\":2}]"
}
```

**achieve is a JSON string containing an array of objects**, not a scalar
star count and not a directly nested JSON array. An explicit unearned row is:

```json
{"stage_id":"n_01_02","achieve":"[]"}
```

Omitting an unearned stage row entirely also leaves a missing map entry with
GetStageAchieveCnt0 on a fresh native model. Partial sync/deletion semantics
on an already populated model are not established, so explicit zero rows are
preferable for authoritative reload.

Evidence, including object-base arithmetic:

- `0xb68d40` indexes stage and iterates its values.
- `0xb68e14` dereferences a stage row into r0; `0xb68e1a` saves it in r11.
  `stage_id` literal is slot `0xb69050` +PC `0xb68dfc` -> `0x1d72b31`.
- `0xb68e28` converts stage_id to string; `0xb68e3e` ensures its native map
  entry exists. The map is CSRPlayData+0x27c.
- `0xb68e44..0xb68e70` copies the existing value into local STAGE_INFO at
  **sp+0xa8** (r8). It has a12-byte string followed by exactly three flagbytes.
- `0xb68e78` clears flag2 and `0xb68e7c` clears flag0/1; the local flags at
  **sp+0xb4,+0xb5,+0xb6** are zero before reading the new achievements.
- `0xb68e74` loads achieve from slot `0xb69058`; add at `0xb68e7a` gives PC
  `0xb68e7e`, target `0x1d72cb1`, literal **achieve**.
- `mov r0,r11` at `0xb68e80` proves this is stage-row.achieve.
- `0xb68e8e` converts that value to string; **JSON.parse** at `0xb68ea6`
  parses the resulting string into a separate JSON object at sp+0x48.
- `0xb68f4a` dereferences each parsed achievement; `0xb68f52` indexes its
  numeric **order** (`0x1d7146f`). Integer conversion ends at `0xb68f98`.
- `add r0,r8` at `0xb68f98`, followed by `strb r9,[r0,#0xc]` at
  `0xb68f9c`, sets **localSTAGE_INFO.flags[order]=1**.
- `0xb6901e..0xb69026` copies exactly those three bytes back to the map node
  at node+0x28,+0x29,+0x2a. Node value starts+0x1c; flags therefore value+0xc.

An empty parsed array has equal begin/end and executes no writes. It stores
zero/zero/zero. Sparse records set only the supplied criterion flags; they do
not mark all lower indices automatically.

## 2. Why scalar star counts produce a spurious one star

**[RECOVERED]** The native helper labeled from_json<string> (`0x728b08`) is
custom/permissive. It converts numeric tags through to_string:
signed path `0x728b4e`, unsigned `0x728b5c`, float `0x728b66`. Values such as
numeric0 or3 become strings `"0"`/`"3"`, which JSON.parse turns back into
**primitive numbers**. The native iterator setup for a nonnull primitive uses
one begin element and an end sentinel, rather than an empty collection.

Inside that singleton iteration, reading a missing/non-numeric order takes
`movs r0,#0` at `0xb68f96`; flag0 becomes1. Consequently a scalar zero is
not a representation of zero achievement flags. This explains the observed
one-star-per-stage pattern without any native minimum-one rule.

The same helper converts array/object/null input to an **empty string** at
`0x728ba4..0x728bdc`; it does not preserve their JSON structure. The result
of JSON.parse on empty input was not audited here. Therefore directly nested
`achieve:[]`, missing achieve, or null achieve are not the proven zero-state
contract. Use the valid **string `"[]"`**, or omit the whole row on fresh sync.

## 3. The count is a sum of three flags, without a minimum

**[RECOVERED]** `GetStageAchieveCnt(string const&)` (`0xb6ce4c`) checks whether
CSRPlayData+0x27c contains the stage. Missing key returns0 at `0xb6ceb2`.
Existing key reads exactly three flags:

```text
00b6ce88 ldrh r0,[node,#0x28]
00b6ce8e ldrb r0,[local,#0]         // flag0
00b6ce92 ldrb r1,[local,#1]         // flag1
00b6ce9a ldrb r2,[node,#0x2a]      // flag2
00b6ce9e add r0,r1
00b6cea4 adds r4,r0,r2             // return flag0+flag1+flag2
```

There is no minimum1, no highest-order calculation, and no sum of order values.
Examples: `"[]"` ->0; `"[{\"order\":2}]"` ->1;
`"[{\"order\":0},{\"order\":2}]"` ->2;
allthree ->3. Duplicate order entries simply set the same byte again.

Native emplace default construction independently initializes all three flags
to0 (`0xb73a86..0xb73a8e`), so merely creating a stage record does not award a
star. Earlier documentation claiming a native minimum1 is superseded.

## 4. SetStageAchieve and legal indices

**[RECOVERED]** `SetStageAchieve(stage_id,int order)` (`0xb6cedc`) writes a
single byte at node+0x28+order when the stage exists (`0xb6cf20..0xb6cf24`).
For a new entry it uses local STAGE_INFO base sp+0x30; adds12 to reach flags
(`0xb6cf5e`), clears allthree flags (`0xb6cf64`,`0xb6cf68`), then writes
`[flagBase+order]=1` at `0xb6cf6c` before inserting the record.

Both this writer and ParseMissionInfo's writer are **unchecked**. The getter
and constructor establish that the legal storage indices are **0,1,2**.
Index3 is outside the three-byte flags. It is not a third star: it is a
fourth byte, does not contribute to the getter, and may corrupt adjacent data.
Negative or larger indices can corrupt memory. Validate orders0..2 server-side.

**Correction to historical safety clamp:** current/older `/mission/Complete`
emitted orders1,2,3. That sets two recognized flags and one out-of-range byte,
not three recognized stars. The appropriate complete grant for three stars is
orders0,1,2. For N provisional stars, use0..N-1 as an explicitly local criterion
policy until the real three condition identities are reconstructed.

`CSRSyncMStage::ReqCompleteCB` decompile
`analysis/native-mission-complete.txt:1871-1873` calls SetStageAchieve with
each response order and writes a second local result boolean at the same index.
Thus the same zero-based bounded orders must be used in both the completion
response and later lobby serialization; changing only one creates reload drift.

## 5. Implementation/control recommendation

1. Serialize each lobby stage's earned flags with
   `achieve: JSON.stringify([{order:0},...])`; zero is `"[]"`.
2. Emit completion orders0..2; never scalar counts or order3.
3. Keep persisted server counts separate from wire-encoded criterion indices.
   A counter3 becomes three objects; it does not become wire integer3.
4. Existing persisted counter3 can be migrated to flags0,1,2 as a **fixture
   policy**, preserving already granted progress without replaying rewards.
5. Native control: fresh zero-star lobby ->0/30 and locked next area; complete
   one stage ->3/30; relaunch ->same3/30; missing stage map key and explicit
   `achieve:"[]"` must both read0 on fresh state. Verify last-stage unlock after
   a real clear and reward idempotency separately.

The shape, bounded storage and count arithmetic are recovered. Actual original
achievement condition semantics and which condition should be granted from a
particular battle result remain unknown. This research lane performed no fresh
native runtime test; the parent's controls must establish the visible result.

# Training Raise follow-up: curve, sacrifice experience, lock, and refusal

2026-10-03. Read-only native research: original extracted library, Capstone
5.0.7, existing resolver, existing material. No adb/Ghidra/source edits.
Addresses are Ghidra image addresses (file offset + 0x10000).

## 1. GetLevel is the card experience source; LEVELING is a different class

**[RECOVERED]** `/reference/GetLevel` -> `CSRSyncRef::ReqLevelCB` (`0xf84c7e`)
checks result code1, calls `CSRUserLV::get`, then tail-calls
`CSRUserLV::SetLevel` (`0x109f114`) at `0xf84c9c`. This class is distinct from
`CSRLevelData`, the local battle/AI tuning parser of `LEVELING.jet`.

`CSRUserLV::SetLevel` first indexes envelope.ret_data, then named collections
`user`, `vip`, `vip_group`, `card`, `skill`, `card_awk`. The card-row fields are
numeric `rank`, `level`, `min_exp`, `upgrade_exp`, `sell_price`; the parser
stores `CARD_LEVEL_INFO` records at stride16, in a rank-keyed map at `this+0x78`
(tree root `+0x7c`). The awakened curve has its own map/root `+0x84/+0x88`.
Within the 16-byte row: level at+0, min_exp at+4, upgrade_exp at+8,
sell_price at+12. The rank selects the enclosing vector rather than occupying
row bytes.

**[RECOVERED / negative search]** All21 chunks of
`analysis/extracted/assets/LEVELING.jet` were decompressed in memory with
`tools/extract-jet-chunk.py`'s walk/body helpers. None contains `min_exp`,
`upgrade_exp`, `sell_price`, or `raise`. Its chunk19 power/rank/hyper/level
recommendation CSV is not an experience curve. No original curve was recovered
from this material; the server's existing rows are **[FIXTURE]**.

## 2. Level, maximum, and experience cap

**[RECOVERED]** `CSRUserLV::GetCardLevel(rank,exp,awake_step)` (`0x10a0b2c`)
uses the rank-keyed vector when awake_step==0, or awake-step-keyed vector
otherwise. It walks rows in their published order:

```text
first row with row.min_exp > exp -> max(1,row.level-1)
otherwise -> last row.level
missing vector -> 1
```

Decisive instructions: `ldr r3,[r2,#4]` / `cmp r3,r4` / `bhi` at
`0x10a0bb2..0x10a0bb6`; row step16 at `0x10a0bb8`; last-row level at
`0x10a0bbe`; prior-level arithmetic at `0x10a0bc8..0x10a0bd0`.

**[RECOVERED]** `GetCardMaxLevel(rank,awake_step)` (`0x10a0c68`) returns the
**last row's level**, not an embedded50: after copying the vector, it loads
`[end-16]` at `0x10a0cf6`. Missing rank/awake-step returns1. A present empty
vector is unsafe because it dereferences end-16.

`GetCardMinExp(rank,level,awake_step)` (`0x10a0da0`) reads
`rows[level-1].min_exp`, capped to last row. `GetCardMaxExp`
(`0x10a0d0c`) reads the **next** row's min_exp (`rows[level].min_exp`), capped
to last row; level0 uses the second row's min_exp. Thus, at maximum level,
both bounds collapse to the last row.min_exp.

`CSRCard::SetExp` (`0x869ea4`) stores the new exp, derives level through
GetCardLevel, and updates cached min/max exp when the level changes. It does
not introduce an independent original maximum.

**[FIXTURE / current source]** `starterLevels.card` publishes rank1 rows:

```json
[
  {"rank":1,"level":1,"min_exp":0,"upgrade_exp":100,"sell_price":0},
  {"rank":1,"level":2,"min_exp":100,"upgrade_exp":200,"sell_price":0}
]
```

Therefore a non-awakened rank1 card is level1 below exp100, level2 at exp100+,
and max level2. A faithful implementation **relative to this published fixture**
may cap training exp at100 and refuse to consume fodder once already there.
An expanded50-row curve is a legitimate documented replica fixture, but no
original rank1 max50 or faithful50-row economy was recovered here. The native
getter will honor whatever coherent nonempty curve the replica publishes.

## 3. Sacrifice experience and cost use each SOURCE

**[RECOVERED]** `CSRTableLevelUp::UpdateTraningInfo` (`0x101cb70`) derives
each source card's awake step, rank, exp, then:

```text
source_level = GetCardLevel(source.rank, source.exp, source.awk_step)
contribution = GetCardRaiseExp(source.rank, source_level, source.awk_step)
total_exp += contribution
total_price += Guild.CalcBonusSaleValue(benefit_type=3,
                                      GetCardRaisePrice(source.rank))
```

Callsites `0x101cc92`, `0x101cca6`, `0x101cce8`, `0x101ccf2`; accumulation
at `0x101ccd4..0x101ccd6` (exp) and `0x101ccfa..0x101ccfc` (price).
GetCardRaiseExp (`0x10a0e34`) returns `rows[source_level-1].upgrade_exp`,
capped to the last row's value; missing rank returns0. In this function the
awake-step third argument is unused: it selects the ordinary rank map only.

The UI compares target/source roles at `0x101ccbe`, but the subsequent float
conversion has no multiplication; mismatched roles use the same original
contribution at `0x101ccd2`. **No different-role penalty or same-role bonus
was recovered in this build's instruction sequence.**

With current fixtures, a level1 source contributes100, level2 source200, and
price vector `[100]` charges100 **per source**, before any guild benefit.
The cost is not indexed by target rank or target level. Original costs,
original contribution values, and guild benefit values remain unknown.

## 4. Lock toggle: request and flat response

**[RECOVERED]** `CSRSyncGlobal::RequestCardLock` (`0xf656d4`) posts
`card_handler/ToggleLock`. The request map is built with exactly5 entries at
`0xf65830`: app_code, app_ver, pvid, account otp, target_inst_id. The serial
is formatted with `to_string(unsigned long long)` at `0xf65808` and paired
with target_inst_id at `0xf65814`. There is **no desired lock state** argument;
the method signature is callback + target serial, so this is a toggle.

`ReqCardLockCB` (`0xf65c8c`) reads:

```json
{"result_code":1,"ret_data":{"inst_id":2,"lock":0}}
```

Both fields are scalar numeric conversions; inst_id is uint64 and lock is
converted to uint8. Root ret_data is null guarded (`0xf65d74`). The callback
passes the decoded instance id and lock to `CSRInventory::SetCardLock`
(`0xae9a9c`) at `0xf65e8e`. Number0 unlocks; number1 locks, matching the
inventory's byte flag. Do not nest under card or send lock as an object.

**[RECOVERED]** Training's `IsInactiveCard` (`0x101dab8`) marks source cards
unusable if contained in deck cases1,2,4,5 OR their lock byte is nonzero OR
their serial equals the inventory leader. Calls to IsContainedDeck are at
`0x101daf8`, `0x101db52`, `0x101dbac`, `0x101dc06`; GetCardLock at
`0x101dc5e`; the results OR together at `0x101dc64..0x101dc9c`; leader-id
equality is ORed at `0x101dcbe..0x101dcd4`. This is a recovered source filter,
not a prohibition on training a locked target. Protecting targets from
appearing among source ids is also necessary server integrity, although that
exact rejection is not a named wire error recovered here.

## 5. There is no recovered `t` idempotency token

The strict resolver prints a misleading `t` candidate from
RequestLevelUp at `0xf53740`. Exact instruction pairing instead proves:

```text
f5373e ldr r2,[pc,#0x244] -> slot f53984
f53740 ldr r1,[pc,#0x244] -> slot f53988
f53744 add r2,pc         -> PC f53748 -> string "0" at1d62b2e
f53746 add r1,pc         -> PC f5374a -> string "1" at1d6b5ea
f53748 cmp tutorial_arg,#1
f5374c movne r1,r2
```

The selected string is saved at sp+0x70 and later published under is_tuto.
The apparent `t` comes from using the wrong add PC, the same failure mode as
the historical `_id`/`wave_list` mix-up. Neither `t` nor a nonce was recovered
as a LevelUp field. Request-repeat protection therefore needs server state
(already consumed source ids), or a explicitly local stored operation key;
do not claim a native transaction token exists.

## 6. Refusal handling

**[RECOVERED]** `ReqLevelUpCB` first calls GetResultCode at `0xf53fc0` and
checks1. A non1 code jumps to `0xf5403c`, zeroes all four callback values
(previous/current exp, previous/current gold), skips user/card parsing, and
invokes the callback. The JSON-level result_code check repeats the same
behavior at `0xf54076`. There is no special2001/400 branch in this callback.

`OnTrainingLevelUpEnd` (`0x101e598`) adds the four values at
`0x101e5bc..0x101e5c4`; allzero branches to its return at `0x101e7bc`, so no
success popup is built. A non1 application result is the native refusal path;
the particular original business refusal code is **[UNKNOWN]**. Broader HTTP
retry/decryption policy must still be respected; this report only pins this
callback, not a new universal error policy.

Do not express refusal as a successful response with gold/exp0: on the success
path those values overwrite the client's balance/experience. A structurally
complete success no-op can preserve values, but its native UX still looks like
training completed and was not verified here.

# `/shop/GachaPremium` — recovered request and result contract

**Date:** 2026-10-03. **Lane:** gacha fix implementation (sub-agent).
**Method:** offline Thumb literal-pool resolution + capstone disassembly of the
read-only `analysis/extracted/lib/armeabi-v7a/libnative_core.so`. **No Ghidra, no
adb, no device.** Ghidra image address = file offset + `0x10000` (§16.7.3).

Tools used (read-only, unmodified):
- `tools/resolve-literals-offline.py --function A:B` — the corrected resolver
  (§16.7.1). It is anchored on `add <Rn>,PC` and requires the load to be the
  immediately preceding instruction.
- A throwaway capstone annotator (in `%TEMP%`, not committed) to disassemble a
  range and resolve `bl` targets against `analysis/native-evidence.tsv`.

**Caveat on recall.** The corrected resolver's contiguity rule is a false
positive defence, and it has a real false-negative cost: the compiler sometimes
interleaves an unrelated store between the `ldr` and the `add`, e.g. at
`0xcd787a ldr r1,[pc,#0x144]` / `0xcd787e str r2,[r0,#8]` /
`0xcd7880 add r1,pc`. Every literal quoted below was therefore checked by hand
against the disassembly at the reported site, and four additional literals were
recovered by hand (`back_count`, `back_count2`, `from_Gacha10`, `gacha_result`).
**Do not read the resolver's "resolved: N" as "this function has N keys".**

---

## 1. What was already known

`analysis/research/in-game-stats.md` §5.3 / §7: the defeat screen's
**"Recruit New Hunter"** button reaches *Recruit Hunters* for free; `Recruit
300` confirms and the client really issues

```
POST /shop/GachaPremium  {"pvid":"1000001","cnt":"11"}
```

with the 9-key set `app_code, app_ver, bonus_level, cnt, gacha_type,
item_inst_id, market, otp, pvid`. The route had no handler, so the generic mock
answered; `ret_data.card` was absent and **nothing was granted**.

`RequestGachaPremium` (Ghidra `0xf74774`, the request builder) decompiles in
`analysis/native-network-decomp.txt:8544` and asserts
`_RMAssert(param_5 == 1 || param_5 == 0xb, … 0xb3)` — the native **count**
must be1 or11. The older gacha_type interpretation was wrong; actual symbol
ABI and Thumb operand flow separate type/count. See gc2-coupon-contract-audit.md.
The literal `/shop/GachaPremium` is at `0x01d8fd70`, next to `RequestGachaPremium`
(`0x01d8fd43`), `item_inst_id` (`0x01d8fd57`) and `bonus_level` (`0x01d8fd64`) —
which independently corroborates the 9-key request field set.

---

## 2. The result parser chain — recovered

```
CSRSyncLottery::ReqGachaPremiumCB                Ghidra 0xf74fb0
   mangled: (function<void(int, vector<basic_json>&)> const&, unsigned, unsigned, int,
            CPVHTTPRequest*, CPVHTTPResponse*)
      |
      +-> iterates ret_data["card"], calling
      |     CSRPlayData::ParseCardInst (0xb69598) -> CSRCard::parse
      |     then CSRInventory::AddCard (0xad9238)
      |
      `-> hands the SAME vector to the app callback, i.e.
            CSRPopUpGachaX10Result::ReqGachaPremiumCB  Ghidra 0xcd7518
            CSRPopUpLotteryShot::ReqGachaPremiumCB     Ghidra 0xcf0bf4
                 -> CSRPopUpGachaX10Result::RESULT::parse  Ghidra 0xcd36a8
```

`RESULT::parse` (`0xcd36a8`) is the **only** per-element parser; both popups call
it, so the element shape is shared.

### 2.1 `CSRSyncLottery::ReqGachaPremiumCB` (0xf74fb0 … 0xf758fc)

20 literal loads resolved, in instruction order:

| ldr | key | how it is consumed |
|---|---|---|
| `0xf75026` | `result_code` | `ldrb; subs #3; cmp #4; bhi` → must be integer 1 or the callback bails |
| `0xf75080` | `ret_data` | `mov r4` — **`ret_data` is the root object**, then `CSRAchieve::ParseLobbyEnter(ret_data)` |
| `0xf75096` | `achievement` | `ldrb; cbz` → **null-guarded**; else `CSRAchieve::ParseAchievementsElement` |
| `0xf750b2` | `user` | `ldrb; cmp #0; beq` → **null-guarded**; skips the whole currency block |
| `0xf750c6` | `user.iap_qty` | `strtod` (number) → `CPVDataMgr+0x9c` |
| `0xf75112` | `user.free_iap_qty` | `strtod` (number) → `CPVDataMgr+0xa0` |
| `0xf7515e`,`0xf7516c` | `user.gold`, then `["cur"]` | null-guard then `strtod` → `CSRPlayData+0x154` |
| `0xf751dc` | `cnt` | `ldrb; subs #3; cmp #4; bhi 0xf653d8` — **only tags 3..7 reach `strtod`; an object/array/null takes the reject branch.** So `cnt` MUST be a JSON number |
| `0xf75204` | `card` | `ldrb; cmp #0; beq 0xf654e0` → null-guarded. Then a loop that accepts **tag 2 (array, stride 0x10)** or **tag 1 (object, map size)**; anything else iterates zero times |
| `0xf753d8` | `card` | the same json, converted to `vector<basic_json>` for the app callback |
| `0xf754fe` | `consumed_inst_list` | `cbz r4` → null-guarded; else `CSRInventory::UseItem` per element |
| `0xf7553a` | `point` | `ldrb; beq` → null-guarded; then `prev`, `cur` → `CSRPlayData::SetMileagePoint` |
| `0xf755fc`,`0xf75642`,`0xf7564e` | `mileage_action`, `before_point`, `after_point` | `CSRPlayData::SetMarker(string, unsigned)` |

Every optional key is reached only after an explicit null test on the parent, so
**omitting a key is safe** and is what this implementation does for
`achievement`, `consumed_inst_list`, `point` and the three mileage keys.
`achievement` is additionally omitted because of the standing `/mission/Complete`
invariant (a non-null `achievement` is read by `CSRAchieve` and an empty `[]` is
known-bad; an absent key is `null`, which the `cbz` at `0xf750a6` skips).

### 2.2 `CSRPopUpGachaX10Result::RESULT::parse` (0xcd36a8 … 0xcd3b00)

Six keys, all of them read straight off the **element**, with the read type
taken from the callee:

| ldr | key | callee | type |
|---|---|---|---|
| `0xcd36d2` | `index_id` | `strtod` | number |
| `0xcd3724` | `is_duplicate` | `strtod` | number |
| `0xcd380a` | `inst_id` | `strtod` | number |
| `0xcd3868` | `reward` | `operator[]` | object |
| `0xcd3872` | `reward.ref_id` | `from_json<std::string>` (`0x718b08`) | **string** |
| `0xcd388a` | `reward.qty` | `strtod` | number |

No key here is null-guarded, so **all six must be present on every element** or
`from_json`/`strtod` walks a `null` and throws `type_error.305` — the project's
recurring crash class.

After `RESULT::parse`, the popup does
`CSRInventory::FindCardInstBySerial(inst_id)` (`0xadb39c`) →
`GetCardRefID` (`0xadb820`) → `CSRCardInfoContainer::GetCardData(ref_id)`
(`0x86ce64`). **So `inst_id` must be a serial the client already holds** (the
sync callback has just added it from the same element) and `reward.ref_id` /
the instance's `ref_id` must resolve in `/reference/GetCard`.

### 2.3 `CSRCard::parse` (Ghidra `0x8680a4`) — the instance half of an element

Keys recovered, in order: `inst_id` (`0x8680be`), `ref_id` (`0x86810c`),
`lock` (`0x86815c`), `skin_ref_id`, `skin_id`, `skin_total_count`,
`weapon_rank`, `weapon_level`, `armor_rank`, `armor_level`, `accessory_rank`,
`accessory_level`, `skill_1_level` … `skill_5_level`, `mirage_remain_hp`.
`ref_id` must be non-empty: `CSRCard::SetRefID` asserts
`sRefID.length() > 0` at `SRCard.cpp:731`.

This is the **same parser** `/lobby/GetCardInven` feeds
(`CSRPlayData::ParseUserCardInven`, `0xb693a0`, which iterates `ret_data` as a
bare array at stride 0x10 and calls `ParseCardInst` per element). The element
published here is therefore the `GetCardInven` row **plus** the six gacha keys —
no new instance shape is invented.

### 2.4 What the popups do NOT read from the response

`CSRPopUpGachaX10Result::ReqGachaPremiumCB` builds the `GachaResult` marker
entirely **client-side** and stores it with `CSRPlayData::SetMarker`:

```
back_count = 0, back_count2 = 0, from_Gacha10 = <bool>,
gacha_result = [ RESULT::dump() ... ]
SetMarker("GachaResult", marker)                    // 0xcd76d4
```

`back_count` (`0xcd7556`), `back_count2` (`0xcd75a8`), `from_Gacha10`
(`0xcd75e8`) and `gacha_result` (slot `0xcd79ac`, consumed by the `add r4,pc`
at `0xcd7644` → `0x01d7ccb0`) are all literals inside the client. **They are
client bookkeeping, not server fields.**

`CSRPopUpLotteryShot::ReqGachaPremiumCB` additionally reads
`CPVDataMgr+0x60` → `["user"]["type"]` and `["user"]["card_id"]`
(`0xcf0f16`…`0xcf0fe6`), plus the `GachaResult` / `card` / `Z001` literals. That
is the **re-open** path (the popup is reachable from `SceneGoTo` at `0xcd7a24`),
keyed on a client-side string member of `CPVDataMgr`, **not** on the response —
no server field named `type` or `card_id` is published here.

---

## 3. The contract this replica implements

```
ret_data = {                              // [RECOVERED] 0xf74fb0
  cnt:  <number>,                         // REQUIRED, must be a JSON number
  card: [ <element>, ... ],               // REQUIRED for anything to be granted
  user: { iap_qty, free_iap_qty,          // optional, null-guarded
          gold: { cur } },
}

<element> = {                             // [RECOVERED] 0xcd36a8 + 0x8680a4
  /* CSRCard::parse instance fields, byte-identical to a /lobby/GetCardInven row */
  inst_id, ref_id, rank, exp, lock, mirage_remain_hp,
  weapon_rank, weapon_level, armor_rank, armor_level,
  accessory_rank, accessory_level,
  skill_1_level .. skill_5_level,
  skin_ref_id, skin_id, skin_total_count,
  /* the six gacha keys */
  index_id:     <number>,
  is_duplicate: <number>,
  inst_id:      <number>,
  reward: { ref_id: <string>, qty: <number> },
}
```

`result_code` is **1 on every path**, refusals included — a non-1 code puts
`CPVHTTPManager::Enqueue` into the 8× silent retry (§16.5).

## 4. Deliberately omitted

| Key | Why |
|---|---|
| `achievement` | null-guarded at `0xf750a6`; feeds `CSRAchieve::ParseAchievementsElement`, and the standing `/mission/Complete` invariant says a present-but-empty `achievement` is worse than an absent one |
| `consumed_inst_list` | null-guarded; `CSRInventory::UseItem` semantics are the `[UNKNOWN-1]` shape from §16.6 |
| `point`, `mileage_action`, `before_point`, `after_point` | gacha-mileage bookkeeping; null-guarded, and `/shop/RewardGachaMileage` is not implemented |
| element key `is_skin_gacha`, `target_char_id`, `binding_event_id` | those are `/shop/GachaEvent` **request** keys (`0x01d8fe49`–`0x01d8fe67`), not result keys |

## 5. Not recovered

- `ret_data.user`'s full key set. Only `iap_qty`, `free_iap_qty` and
  `gold.cur` are read here; all three are individually null/type-guarded, so
  the minimal object is safe.
- Whether `reward` can be an **item** reward rather than a card. `inst_id` +
  `reward.ref_id` + `FindCardInstBySerial` all say card, and nothing in the
  recovered code says otherwise, but a mixed item/card pull is **[UNKNOWN]**;
  this replica only ever awards cards.
- The rarity/roll table. Nothing recovered decides *which* card a pull yields, so
  the replica awards a fixed card (see `FIXTURE_GACHA_CARD` in `bootstrap.ts`).

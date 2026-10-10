# GC2 coupon contract audit

2026-10-08. Read-only lane: existing dumps, exported symbols and original
`analysis/extracted/lib/armeabi-v7a/libnative_core.so`. No Ghidra, ADB, runtime,
account, original resource or server source changes. Addresses below use Ghidra
image coordinates, abbreviated G; ELF virtual address = G minus 0x10000.
Original ELF reads used its PT_LOAD mappings rather than assuming every virtual
address is a flat file offset. Capstone Thumb instructions and explicit literal
slot/ADD pairs corroborate the existing decompile.

## What is already closed

Root continuation: read-only Ghidra allocation/constructor/OnInit/OnReset
evidence is in ghidra-coupon-shot-allocation[-insn].txt,
ghidra-coupon-shot-constructor[-insn].txt and ghidra-coupon-bonus-init/reset.txt.
MakeShared G ebeb34 clears the complete870-byte object. Constructor G ebec5c
uses vmov.i32 q8,0 atG ebec6c and vst1.32 atG ebec92 over object+670..67f,
explicitly initializing member+678 to **zero**. OnInit has no direct+678 store.
This closes constructor default, not every transitive writer before a GC2
request; no live coupon has been redeemed or granted. Do not promote default0
to an unconditional send-time bonus without checking intervening calls.

GC2 is an owned single-recruitment coupon, selected by two exact native controls.
The second control is additional evidence beyond the older coupon report:

- `PA_SE_CS_AP123` (14 bytes): literal slot Ge40178, ADD Ge40132;
- `BTN_NORMAL_RED_SCROLL` (21 bytes): slot Ge4016c, ADD Ge400f8.

Both join the comparison at Ge40138 and, on equality, assign `GC2` from slot
Ge4017c / ADD Ge40140 / assign Ge40146. Ge4014c sets Lottery INFO TYPE to 1.
These are native control identities, not an inferred item label or rank. In
particular the letters/numerals in the control name do not prove an original
rarity pool. Other exact branches are `PA_SE_CS_AP23` -> GC7/type3,
`PA_SE_CS_AP3` -> GC8/type4 and `BT_4_ONLY` -> GC11/type8. They do not authorize
GC2 aliases for those distinct references.

GetItemInst(string) Gaec894 at Ge401d2 obtains the selected owned item record.
The zero check at Ge40202..208 refuses the empty record; the subsequent native
owned-card/capacity check also precedes recruitment. The successful marker
contains `ticket_id` from the record's uint64 at +0x10, type1, send1 and cnt1.
It enters CSRPopUpLotteryShot (scene TYPE0x61), not a Manda fallback.
Existing full decompile: `analysis/ghidra-gc2-coupon-flow.txt`; exact marker
literals and scene transition are documented in `gc2-coupon-route-contract.md`.

SetCurrency Ge3e43c constructs exact `GC2` at Ge3e90c/90e/912 and calls
Inventory.GetInstItemCnt Gaeca80 at Ge3e91a. The returned count is formatted
and assigned to the native text control `TX_MY_PA1` (slot Ge3ea18 / ADD
Ge3e95c, text lookup Ge3e96a, count conversion Ge3e974). This is an inventory
balance, not three coupon grants or a server pool declaration.

## Request ABI and payload

Original symbol RequestGachaPremium Gf74774 has arguments:

```text
(uint64 item_instance, unsigned count, Lottery.INFO.TYPE,
 LotteryShot.BONUS_INFO.TYPE, callback)
```

On ARM, `this` occupies r0, the aligned uint64 occupies r2/r3, count is the
first stack argument, and the two enums follow it. The requester saves the
uint64 into FP/SL at Gf74784/80 and count from [r7+8] at Gf74786. It asserts
COUNT equals 1 or 11 at Gf7478c..c8. The older gacha-premium-contract.md §1
sentence equating that assertion to `gacha_type` is incorrect; it is count.

Actual formatting in the requester proves the fields remain distinct:

- gacha_type: enum at [r7+0xc], formatted Gf74900..24;
- item_inst_id: full r2/r3 uint64, formatted Gf74928..4e;
- cnt: count, formatted Gf74952..78;
- bonus_level: separate BONUS_INFO.TYPE at [r7+0x10], formatted Gf7497c via
  specialized enum to_string Gf74e80, then stored Gf74982..9e.

The native route is `/shop/GachaPremium`, with the existing auth fields.
For the GC2 arm, count1/type1 and the actual stack instance are established.
The request sends an instance serial, not `ref_id:"GC2"` as a substitute.
The popup's bonus selection is independent: ProcessGachaVideo Gcee2bc loads
it from this+0x678 into the outgoing stack argument. Do not silently assert
bonus_level0 without closing OnInit and any subsequent bonus-selection input.

## Consumption receipt is a delta, not an unknown shape

The common callback ReqGachaPremiumCB Gf74fb0 passes its optional
`ret_data.consumed_inst_list` to Inventory.UseItem(JSON) Gaea5f8. The old
gacha-premium report still labels the helper semantics unknown, but later
Search work closed it; this lane independently rechecked the exact original
instructions and literal pairs:

```text
consumed_inst_list: [{inst_id: actual_owned_uint64, qty: consumed_uint32}]
```

UseItem(JSON) reads `inst_id` (slot Gaea70c / ADD Gaea60c) and `qty` (slot
Gaea710 / ADD Gaea6c0), then calls numeric UseItem Gaea714 at Gaea626.
The numeric overload searches the inventory tree by instance ID; for a found
instance, Gaea7fa loads current quantity, Gaea7fc subtracts the consumed low
word and Gaea800 stores the result. It does not clamp underflow or delete a
zero-quantity instance on this found path. Server validation must prevent
underflow and duplicated application of accepted receipts.

This closes the receipt structure and direction of arithmetic. It does NOT
recover original server policy for how many coupons one accepted pull spends.
Count1 alone does not prove debit qty1. Nor does qty mean the remaining balance.
See `search-attempt-persistence.md` and `search-guide-completion.md` for the
already recovered shared helper; do not transfer the different MultiSkillUp
`remain` receipt into this gacha path.

For one card, the native common result callback requires `cnt:1, card:{...}`;
for multiple cards it iterates card[]. Null/omitted card is the guarded no-grant
case. The single-result correction in `gacha-single-result-contract.md`
supersedes the older report's always-array example. Both owned-card instance
fields and the popup index_id/is_duplicate/reward fields are required on an
actual successful result. This audit performed no grant or coupon redemption.

## What this cannot recover

The audited coupon branch uses a literal reference-ID lookup; it does not derive
GC2 from USETYPE, item.effect, rank, artwork or a numeric suffix. Therefore no
GC2 `use_type`, `effect`, rank, sell_price, collect_qty, localized name/description
or thumbnail mapping is proved by this lane. Known use_type1/AP-shop evidence
concerns another consumer and cannot be assigned to GC2. Generic request-scroll
art or prose likewise cannot create that missing binding.

Original E01's reward declaration GC2x3/free_iap0 is exact, and E01 has now
earned its native clear. That settles neither the GetItem reference row nor the
original eligible pool/odds, count-per-coupon/debit policy or complete accepted
coupon receipt. Keep the unsupported settlement explicit; no inert coupon,
substituted resource, extra hunter or Manda charge is justified here.

## Narrow remaining parent targets

1. LotteryShot.OnInit Gcebf90 and any writer of member +0x678: close the
   actual bonus selection/default sent for the normal GC2 marker. The request
   builder and marker do not require another broad dump to establish type/count.
2. ItemInfo.SetItem Gaefe10 plus GetItemRefID(USETYPE) Gaf1374 and actual
   use_type consumers if a numeric enum is needed. A generic enum may be
   recoverable, but it still cannot bind GC2 without original item-reference data.
3. Common result callback Gf74fb0: receipt keys are already reconstructed;
   inspect its complete wallet/mileage/bonus branches only for a concrete
   implementation need. The native library cannot supply the server's hidden
   coupon drop distribution merely by reading the response.

Best missing primary artifact remains a final-client GetItem row idGC2 plus
an accepted original coupon request/receipt. Nothing in this bounded audit
locates one. No visual-stat hunt, inference endpoint or live-state action was
performed.

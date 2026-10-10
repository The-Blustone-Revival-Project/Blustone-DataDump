# GC2 coupon recruitment route

2026-10-05. Read-only original ELF Thumb instructions/PC-relative literals and
parent's ghidra-gc2-coupon-flow.txt. No Ghidra, device, account or source edits.
Addresses prefixed G are Ghidra; ELF=G-0x10000.

## Exact native entry

CSRSceneLottery.OnClickRequestGachaByCoupon is **G e40020 / ELF e30020**.
The control string **PA_SE_CS_AP123** is compared using LDR e4012c/ADD e40132
and memcmp e40138. The matching arm assigns **GC2** using LDR e4013e/ADD e40140,
then sets its recruitment type to **1** at e4014c. Other branches select GC7,
GC8 or GC11; they are separate contracts, not aliases for GC2.

Inventory.GetItemInst **G aec894** is called at e401d2 with that ref-ID string.
The following branch checks the item value at e40202/e40208; the normal item
path also checks owned-card count against capacity at e40288. This is not a
direct HTTP request, and should not silently fall back to Manda when the coupon
cannot be used.

The normal path writes this local marker object:

```text
CSRPopUpLotteryShot:
  ticket_id = inventory item instance's u64 at +0x10
  type      = 1 for the GC2 arm
  send      = 1
  cnt       = 1
  video     = native configured string (value not resolved here)
```

Exact field literals: ticket_id LDR e4029a/ADD e402a8; type e402d6/e402da;
send e40310/e4031c; cnt e4034e/e40356; video e403aa/e403b4. The u64 ticket
load is LDRD e40296; send/cnt are numeric constants from e40316/e4031e and
e40352. Marker name LDR e403e6/ADD e403ea, SetMarker **G b67bbc** at e403f8.
PushSceneFadeOutIn at e4041a selects **TYPE0x61**.

## HTTP consumer and fields

CSRPopUpLotteryShot.OnInit **G cebf90** reads the marker and calls
ProcessGachaVideo **G cedeb8**. That function calls
CSRSyncLottery.RequestGachaPremium **G f74774 / ELF f64774** at **G cee2c2**.
The parent decomp corroborates this call at ghidra-gc2-coupon-flow.txt:947;
its inferred decompiler argument types must not replace the actual symbol ABI.

Requester literal evidence establishes auth5 and:

```text
/shop/GachaPremium
  gacha_type
  item_inst_id
  cnt
  bonus_level
```

ADD sites are f7490a, f74934, f7495c, f74984 and route f74a8e. The requester
assertion explicitly requires **uiCount==1 || uiCount==11** (literal ADDf747ba).
Thus the GC2 normal marker requests a single recruitment using an owned item
instance, not a GC2 string in the final HTTP body. Response/debit fidelity still
requires the requester/callback's full dataflow.

## Limits and safe boundary

The native GC2 identity/control, type1, count1 and transport are recovered.
Original coupon reference metadata, rarity pool/odds, bonus behavior, debit
quantity and complete settlement DTO are not recovered by this unit. The shipped
E01 reward GC2x3 does not by itself prove any of those missing fields.

Until coupon settlement is reconstructed, refusing nonzero or malformed
item_inst_id avoids charging Manda for a coupon request. Omitted/zero ticket
paid recruitment is a distinct existing path; this report does not redefine its
prices. Targeted next dump addresses: **G f74774**, common result callback
**G f74fb0**, popup result callback **G cf0bf4**. No live coupon consumption or
native success was tested.

# Live AP popup2166678 is ShopFuel, not SupplyFuel

2026-10-04. Original ELF symbols/RTTI/vtable headers and Capstone only. Parent reported guarded live modal's primary vptr ELF0x2166678. No Ghidra/adb/Java/server/client changes or additions to UI guards.

## Exact attribution

The containing original ELF symbol is **_ZTV16CSRPopUpShopFuel**, ELF VA0x2166670,size0x88. Actual address point0x2166678 is exactly symbol+8. At vptr-8, offset-to-top is0; at vptr-4, RTTI pointer is0x21666f8, **_ZTI16CSRPopUpShopFuel**. It is the primary ShopFuel object, not a secondary CSRScene pointer. Its first function pointers include destructor ELF0xd3bee9, deleting destructor0xd3bf39, and Init0xd39b4d (Thumb bits retained).

Actual RTTI chain:

```text
CSRPopUpShopFuel -> CSRPopUpBase [single base, offset0]
CSRPopUpBase -> CSRScene [vmi offset_flags0x2 => public/nonvirtual offset0]
             -> CMUIBase::Listener [offset_flags0x9002 => offset0x90]
CSRScene -> CRMScene [offset0]
         -> enable_shared_from_this<CSRScene> [offset0x24]
CRMScene -> CRMBaseClass [offset4]
```

There is **no CMUpdatable base or offset** in this chain. Absence from the161 CMUpdatable primary-vptr guards is correct. The top popup must be admitted separately as ShopFuel with its own layout; do not add it to subtree guards or apply SupplyFuel offsets.

## Factory and actual view layout

`shared_ptr<CSRPopUpShopFuel>::make_shared` **Ghidra0xbdffb8** allocates0x140 bytes (control plus actual object at raw+0x10). It calls CSRScene ctor0xdf48e8, initializes fields, resolves ShopFuel vtable, stores primary symbol+8 at raw+0x10 at0xbe005a and secondary listener symbol+0x68 at raw+0xa0 at0xbe0056. Thus actual object pointer is the correct primary scene pointer, listener is actual+0x90.

ShopFuel overrides **Init0xd49b4c**, not SupplyFuel's OnInit0xd71918. It loads view directly with CMUIView::LoadView0x783e64 at0xd49b70. Exact literal: LDR0xd49b68 from slot0xd49cac, addPC0xd49b6e ->0x1d85d43 **SR_COMMON/2_UI_CM_MD/5_UI_CM_M_ST**. This is a separate shop popup layout.

Init stores **view pointer actual+0x94** at0xd49b92 and shared control **actual+0x98** at0xd49b9a. Therefore read-only ShopFuel root chain is:

```text
require top.vptr == B+0x2166678
view = u32(top+0x94)
require view.vptr == B+0x213a750
root = u32(view+0x08)
require known CMUpdatable-derived primary-vptr guard
```

`CSRPopup2::GetRoot`0xb75ca0 independently reads popup+0x94 at0xb75ca4 and calls CMUIView::GetRoot0x783628. **Reading ShopFuel+0x98 as a view would follow its control block**, invalidating the SupplyFuel-chain probe. No field change or native invocation is necessary: implement separate exact class branches or stop on other popup classes.

## Proven AP-meter button route

`CSRUIFrameSceneMain::OnButtonClick` contains the ordinary header fuel branch.0x107d0f8..0x107d104 compares clicked object's CMHashID low32 to **0x45c8f494**, high32 to0;0x107d10a calls ShopFuel make_shared0xbdffb8;0x107d116 calls its virtual Init. The shipped literal **BT_FUEL** has standard CRC32=0x45c8f494. Neighbor native branch constants independently match BT_GOLD=0x33dc862c and BT_EVENT=0x2e005275. This proves the header AP/fuel button selects **ShopFuel**, not SupplyFuel's PA_CELL0 loop. It is consistent with parent's measured top vptr.

Other recovered direct callers include village OnButtonClick0xdad94e, AreaSel0xe744f4, and MStageEntrust0xe7af7c/0xe7afc4; their precise chosen button branches were not fully recovered here. Native SupplyFuel make_shared has separate calls0x84e386/0xb781ce/0xdad340. Trace those specific routes before attributing a SupplyFuel scene from a screenshot label or intended interaction.

## EMPTY item lookup belongs to a separate seam

ShopFuel Init0xd49bf4..0xd49bfa calls **CSRItemInfo::GetItemRefID(USETYPE1)**0xaf1374 and copies the returned reference into **actual+0x104**. It obtains ticket reference via GetGlobalItemTicketRefID0xaf1518 into+0x110, and required quantity via GetGlobalItemTicketNeedQuantity0xaf1540 into+0x120. Then LoadComponent0xd49cb0 and UpdateText0xd49f54 populate controls. GetItemRefID scans its item table's use-type field and returns an empty/default string if no matching row; a Supply reference row does not populate that item table automatically.

Parent's GetItemData assertion with EMPTY ref_id is therefore a plausible **ShopFuel item-reference gap**, not evidence that SupplyFuel's model vector or PA_CELL0 failed. Direct runtime values at ShopFuel+104/+110 and recovered ItemInfo use-type1 table should discriminate this before adding data. Exact GetItem parser shape and original ticket/fuel balance are not established by this attribution; do not invent a magic item record.

The live Supply model refcount1/instance1 remains valid evidence, but **this AP popup never establishes SupplyFuel cell visibility**. Revisit the actual scene reached by More fuel/Supply UI. Safe next native targets for parent decompile: ShopFuel Init0xd49b4c..0xd49cb0; LoadComponent0xd49cb0..0xd49f54; UpdateText0xd49f54..0xd4a51c; ItemInfo GetItemRefID0xaf1374..0xaf13c8, GetGlobalItemTicketRefID0xaf1518, required quantity0xaf1540; header OnButtonClick around0x107d0ae..0x107d146. No alias/rebuild is justified by the wrong-popup observation.

# Bounded read-only Fuel popup UI pointer chain

2026-10-04. Original ELF symbols, Capstone, and prior native decomp only. This is a probe specification, not Java/adb/Ghidra execution or source/client/memory modification. Parent confirmed live model refcount1/instancecount1 and KO loader fallback; inspect actual UI rather than alter reference JSON or alias EN.

All addresses below are **Ghidra code coordinates**, except explicitly marked ELF data/vtable VAs. Let B be the runtime ELF load bias used by existing bounded readers; read little-endian32 pointers only after mapped-range checks. Do not call C++ getters or mutate weak/shared counters.

## Modal singleton and top object

The ELF exported/local symbol `CMSingleton::get<CSRUIModalHandler,...>::wpRet` has **ELF VA0x21e57f8, size8**; its initialization guard is0x21e5800. It is a weak pair:

```text
modal   = u32(B+0x21e57f8)
control = u32(B+0x21e57fc)
```

The get helper0x1086628 resolves this weak pair, calls shared_weak_count::lock at0x10866cc, and returns the saved object. The trivial get wrapper0x10865c4 calls that helper0x10865da. No nearest-symbol pointer guess is involved. For observational reads, require nonnull mapped pair, control strong count+4 !=0xffffffff (expired), and stable pair before/after snapshot; do not emulate lock with writes. This does not eliminate concurrent mutation; stop or retry a bounded snapshot on changing data.

`CSRUIModalHandler::GetTop`0x1085cec is exact and small:

```text
if u32(modal+0x18)>0:
    listLast = u32(modal+0x10)
else if u32(modal+0x0c)>0:
    listLast = u32(modal+0x04)
else:
    stop("no top modal")
top = u32(listLast+0x08)
```

Evidence0x1085cec..0x1085d04: chooses secondary-list count+18 then primary count+c, loads the chosen list's previous/back link, and loads shared scene pointer at node+8. Require chosen count1..32 and mapped16-byte list node; do not iterate unrelated modal objects or print names/text.

**Fuel popup primary vptr must equal B+0x2167d04**, from ELF `_ZTV18CSRPopUpSupplyFuel` VA0x2167cfc+8. Its make_shared constructor0x854540..0x8545a0 stores symbol+8 at actual object (raw allocation+0x10); use the object's vptr, not control allocation. If another modal is top, refuse Fuel-specific offsets.

## Popup view root and recursive UI children

With exact Fuel top guard:

```text
view = u32(top+0x98)
root = u32(view+0x08)
```

`CSRFramedScene::FindCastByName<CMDrawable>`0x93cf88 reads scene+98 at0x93cfa2, then CMUIView::GetRoot0x783628 at0x93cfac. GetRoot reads view+8 at0x783644 (creates a root only if absent); this read-only reader must never create it. Expected view vptr: **B+0x213a750** (`_ZTV8CMUIView` VA0x213a748+8). Expected normal root vptr: **B+0x213bacc** (`_ZTV15CSRUIScrollView` VA0x213bac4+8). Reject unknown root class until its layout is separately admitted.

The recursive node base is **object+4**: framed lookup passes root+4 at0x93cfc6 to FindCast0x76b5e0. For every CMUpdatable object reached through this tree, FindCast's native recursion establishes:

```text
sentinel  = object+0x48
first     = u32(object+0x4c)
nextLink  = u32(listNode+0x04)
child     = u32(listNode+0x08)
childCtrl = u32(listNode+0x0c)
```

At0x76b6e2 mutex is nodebase+40;0x76b6ec reads nodebase+48 (object+4c);0x76b6f0 sentinel is nodebase+44 (object+48);0x76b6fa advances listNode+4;0x76b700 obtains child+8 and recurses child+4. Do not treat the sentinel as a child object. The sibling list has shared_ptr data at+8/+c, not actor pointers from a different container.

Native name comparison reads **uint64 hash object+0x268**, compared to CMHashID query+0x10 at0x76b672..0x76b69e; the generic CMUpdatable search0x8fcdf4 independently uses the same offset0x8fce70..78. **Name CMHashID begins object+0x258**, with libc++ string first12bytes and hash+0x10. InitCell0xd72f78 sets this field on created cells to the model id, so the FuelCell's name can be local_fuel_0 rather than PA_CELL0. PA_CELL0 parent and copied template root can legitimately share the same name; count all matches, retaining tree path/class.

Use the existing32-bit libc++ string decoder, limit name length64, and output only a whitelist of node names: PA_CELL0..3, PA_CELL_LIST, PA_IMG, BT_GET, RW_DAY, BG_ACTIVE, BG_DISABLE, TX_GET, RW_STAMP, RW_IT_NUM, and local_fuel_0. **Never read textbox text values or account fields.** Raw names are metadata; do not dump arbitrary node object bytes. For unknown descendant vptrs, validate against locally enumerated CMUpdatable-derived ELF vtables before applying offsets; request parent confirmation for missing classes rather than nearest-symbol inference.

Bound traversal to depth16,256 total objects,64 sibling nodes/list, detect object/list cycles, require mapped object through0x270 and mapped16-byte list nodes/control, abort on impossible pointers; limit each read4KiB. Re-read modal/top/view/root and each traversed list's links at snapshot end; changing graph produces an unstable result, not an absence conclusion. Child list count+0x50 is structurally adjacent but not needed by the exact recovered loop; use bounded links instead of declaring that count validated here.

## FuelCell template and actual copied child

Exact **FuelCell vptr B+0x2167e90**, from `_ZTV17CSRCellSupplyFuel` ELF0x2167e88+8. The actual object is raw make_shared allocation+0x10 (0xd74df4..0xd74e0a). Its base constructor is CSRUICellBase0x1076f38.

Only on that class guard inspect:

```text
templateName = bounded_libcxx_string(cell+0x824)
cachedRoot   = u32(cell+0x830)
cachedCtrl   = u32(cell+0x834)
```

Constructor stores name string+824 at0x1076f58..68; clears+830/+834 at0x1076f6e..72; calls LoadViewCache0x7840a4 at0x1076f86 using the supplied name, GetRoot0x783628 at0x1076f8e, then stores cached root+830 at0x1076fa0. The supplied name is **SR_REWARD/ACTIVE_CELL**: exact literal pair slot0xd74e8c/add0xd74dea in Fuel make_shared, passed to constructor0xd74dfa.

`CSRUICellBase::InitView`0x1077210 calls ClearChild on actual cell's node+4 at0x107722e; reads cachedRoot+830 at0x1077234; calls CMUpdatable::Copy0x78762c at0x107723a; attaches the copied root to actual cell at0x107728e. Therefore observe **both cached template root and actual cell child subtree**. Template nonnull does not prove the clone contains usable BT_GET; parent PA_CELL0 nonnull does not prove a FuelCell was attached beneath it.

Expected diagnostic outcomes: PA_CELL0 absent despite modelcount1 => actual popup binding/view problem; PA_CELL0 present with no FuelCell => InitCell execution/attachment issue; FuelCell present but cachedRoot null or clone missing controls => cache/template failure; both parent/cell/control bindings present => move to item icon/visibility state. Parent's EMPTY GetItemData assertion is relevant only to this last rendering branch, not proof the parent is absent.

## Exact parent decompile targets if gaps remain

- Modal weak singleton helper **0x1086628..0x10867ac**, GetTop **0x1085cec..0x1085d08**, modal constructor **0x1087804** for independent list-layout confirmation.
- Popup make_shared **0x854540..0x854620**, popup OnInit **0xd71918..0xd71928**, framed loader **0xf1cc4c..0xf1cd04**.
- Framed FindCast **0x93cf88..0x93d070**, CMUIView GetRoot **0x783628..0x7836ec**, CMNode recursive FindCast **0x76b5e0..0x76b7d0**, generic name search **0x8fcdf4..0x8fcf7c**.
- Fuel make_shared **0xd74dc4..0xd74e94**, CSRUICellBase ctor **0x1076f38..0x107704c**, InitView **0x1077210..0x10773e0**, CMUpdatable Copy **0x78762c**, view cache **0x7840a4**.
- Locale/XML path if independently revisiting parent's KO fallback: CMUIView LoadView **0x783e64..0x783efc**, LoadXML **0x782b18**, **CGMDataMgr::GetUIXML0x793674**. Do not revive disproved EN-only hypothesis.

This specification is ready for a bounded no-C++-call reader, but exact descendant class guards and stable graph observations still belong to implementation/runtime validation; unknown class layouts should stop rather than be guessed.

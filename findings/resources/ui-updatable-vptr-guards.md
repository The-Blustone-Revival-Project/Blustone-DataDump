# Static UI primary-vptr guards from original RTTI

2026-10-04. Read-only ELF symbol/RTTI/relocation enumeration and Capstone. Original library SHA256 `c4646ac3817b0008b6ea387fde9c8279fd439343ccc272acdc5883fab9d00eec`. No source/adb/Ghidra/runtime changes.

`ui-updatable-vptr-guards.json` is a plain object mapping **161 ELF primary-vptr VAs** to readable class names. Add runtime ELF load bias B before comparison. `ui-updatable-vptr-guards-proof.json` gives each class's RTTI VA and direct base RTTI/offsets, plus coverage/method. It is not a name-prefix whitelist.

The enumeration parsed ELF32 .dynsym/.symtab, SHT_REL relocations, and Itanium class RTTI. It resolved internal R_ARM_RELATIVE addends and symbol relocations, distinguished __class_type_info/__si_class_type_info/__vmi_class_type_info via their own actual vptrs, and followed declared base-type pointers recursively to `_ZTI11CMUpdatable`. A class was admitted only with a nonvirtual **offset0 inheritance path** to CMUpdatable and its `_ZTV` primary header offset-to-top0 plus matching class RTTI. A single-inheritance RTTI record implies offset0; vmi offset_flags was interpreted as signed offset>>8, rejecting virtual-path membership.3205 class RTTI records were parsed.161 qualifying original vtables passed; no qualifying primary headers failed. Secondary address points are intentionally excluded.

Examples: CMUpdatable ELF0x213a874; CMDrawable0x2136948; CMUIBase0x213b2fc; CMUIButton0x213992c; CSRUIRect0x213b7fc; CSRUITextbox0x213c054; CSRUIScrollView0x213bacc; CSRCellSupplyFuel0x2167e90. Names label classes only: do not inspect textbox text. CMUIView and CSRPopUpSupplyFuel are separate view/scene guards, not CMUpdatable subtree objects; their omission is correct.

CMNode child list statically stores shared_ptr<CMUpdatable>, independently proving its child base contract. Runtime guard failure (unknown vptr, secondary address point, expired control, changed list) means **inconclusive snapshot**, never proof a child is absent. Do not traverse arbitrary pointer candidates to compensate. Use bounds in `supply-fuel-live-ui-reader.md` and whitelist only needed name metadata.

## Exact modal weak-control guard

CSRUIModalHandler is not a polymorphic primary-vptr object: constructor0x1087804 initializes recursive_mutex at this+0, lists+4/+10, and ScenePostEffect+20, without storing a modal primary vtable. Do not compare its mutex storage to a guessed vptr.

The actual owned modal's shared-control factory is `CMSingleton::Holder<CSRUIModalHandler>::Holder`0x1087734. It allocates/constructs modal at0x108773a..0x108774e, then allocates16-byte control0x1087754..56. Literal slot0x108778c/addPC0x108775e yields GOT ELF0x21af0e0, whose resolved value is `_ZTV...__shared_ptr_pointer<CSRUIModalHandler*,default_delete,...>` ELF0x2186a30. Constructor adds8 at0x1087762 and stores primary **control vptr B+0x2186a38** at0x1087764. It stores modal pointer **control+0x0c** at0x1087768 and control pointer holder+4 at0x108776c.

Therefore the existing singleton weak pair **B+0x21e57f8/+4** can be guarded by nonnull mapped control, control vptr==B+0x2186a38, control+0x0c==weak modal pointer, and strong count control+4!=0xffffffff, with stable pair reads. This is the exact modal allocation control, not the distinct pooled Holder control (ELF primary-vptr0x2186a60), which should not be accepted as interchangeable.

Follow GetTop0x1085cec and then require Fuel popup vptr B+0x2167d04 before scene-specific fields. Recheck pair/top after traversal; no C++ calls, control-count writes, or concurrency lifetime guarantees are introduced by this static guard list.

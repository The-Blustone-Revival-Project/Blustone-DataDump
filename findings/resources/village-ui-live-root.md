# Actual Village root for bounded visibility reads

2026-10-04. Read-only original ELF symbols and Capstone; no source/Ghidra/adb/Java/runtime changes. Code addresses are Ghidra coordinates, vptr/global addresses explicitly ELF VAs.

## Direct SceneMgr current scene, not a modal search

Use the existing proven application chain:

```text
app     = u32(B+0x21ef1e0) // g_pApp
manager = u32(app+0x08)
village = u32(manager+0x34)
```

Require the existing app/manager class checks and **Village primary vptr B+0x216b1c4** (`_ZTV15CSRPopUpVillage` ELF VA0x216b1bc+8). Do not demand that the name PopUp implies a modal child: on the recovered Village factory route it is the manager's actual current scene.

Proof: the sole direct caller0xeb79e8 invokes Village make_shared0xeb7c20, then0xeb7a02 stores the resulting actual object pointer **manager+0x34**, with control+0x38 at0xeb7a06. The closure receives its manager pointer at closure+4 (`0xeb79e4`). This is the exact same owner field used by the independently recovered CSRSceneMgr Refresh/ApplyScene chain; no history-list or nearest-symbol guess.

Factory0xeb7c20 allocates0x958 bytes including shared control. It constructs CSRFramedScene at actual object raw+0x10 (`0xeb7c64..66`), resolves Village vtable at0xeb7c82, adds8 at0xeb7c94 and stores it at **raw+0x10**0xeb7ca2. Primary expected vptr is therefore directly corroborated by construction. The listener secondary address point is separate and must not pass the primary guard.

If currentScene has another vptr, this snapshot is not on the validated Village root path. Stop/inconclusive; do not cast a tab handler, Supply modal, Shop popup or scene history value as Village.

## Exact view/root fields from Village's own initialization

After Village guard:

```text
view = u32(village+0x98)
require view.vptr == B+0x213a750 // CMUIView primary
root = u32(view+0x08)
require root primary vptr in ui-updatable-vptr-guards.json
```

Village **OnInit0xd9f528** loads **SR_MAIN/0_SR_MN_BG** through CSRFramedScene::LoadView0xf1cc4c at0xd9f730. Exact literal LDR0xd9f726/slot0xd9fa94/addPC0xd9f72e resolves0x1d87c73. Village's own code then directly loads **this+0x98** at0xd9f73e and calls **CMUIView::GetRoot0x783628**0xd9f74a. GetRoot returns view+8. Thus the root fields do not rely merely on an unrelated framed subclass.

CMUIView control is Village+0x9c, not the view pointer. Root control is view+0x0c. Validate mapped pair/nonexpired count as in prior reader; reading fields does not emulate lifetime locking. The static selected EN/KO SR_MAIN/0_SR_MN_BG records both exist (23630 bytes); the separate MAIN_ICON record has the previously verified PA_ICON_AREA/PA_ACTIVE subtree. Runtime tree search remains the evidence for how that subtree is attached, not a guessed static include.

## Exact visibility nodes and stable bounded traversal

Reuse the161 RTTI-proved CMUpdatable-derived **primary** vptr guards and list layout in `supply-fuel-live-ui-reader.md`:

- Object nodebase+4; sibling sentinel object+0x48; first object+0x4c; list-node next+4, child pointer+8/control+0x0c.
- Name CMHashID object+0x258, low/high hash+0x268; decode only name metadata bounded64 and output only PA_ICON_AREA, PA_ACTIVE, BT_ACTIVE, MN_NC and ancestor names needed for their paths.
- **Hidden byte object+0x271:0 visible,1 hidden**, proved by SetVisible0x7882a0..0x7882c8. This is the inverse of its API boolean; do not report byte1 as visible.
- Extend mapped-object bound to include+0x271. No textbox-text fields, account strings, arbitrary raw bytes, or writes.
- Bound depth16/256 objects/64 sibling nodes; cycle-check; require mapped guards/control; unknown or secondary vptr means inconclusive, never absent. Re-read app, manager/currentScene, Village/view/root pointers and list links at end; a changed graph is unstable.

PA_ACTIVE hidden1 is direct evidence of the panel being hidden (DisableBadges is a recovered possible writer). Visible child with hidden ancestor remains effectively hidden. All visible flags with a failed manual tap shifts investigation toward actual transforms/hit coordinates/resources; it does not authorize forcing visibility. If node is absent in a stable fully guarded tree, record absence and resolve actual resource attachment before claiming a server eligibility problem.

The free-fuel modal, once successfully opened through BT_ACTIVE, becomes separately observable with CSRUIModalHandler/GetTop and SupplyFuel vptr B+0x2167d04. Village currentScene can remain in the background; those are two independent roots. Header BT_FUEL's ShopFuel vptr B+0x2166678 uses its own view+0x94 and must not substitute for either Village or SupplyFuel.

Exact parent decompile targets if needed: anonymous factory closure containing0xeb79e8/0xeb7a02; Village make_shared0xeb7c20..0xeb7e50; OnInit0xd9f528..0xd9fb58; framed FindCast0x93cf88; CMUIView GetRoot0x783628. Existing evidence suffices for the bounded read chain without C++ calls.

# Search tutorial: fixed UI target 017

2026-10-05. Read-only original ELF Thumb/RTTI, retained symbols and parent's reported native guide progression. No device/Ghidra/source/runtime operations. G addresses = ELF VA+10000.

## Exact dependency

**CSRSceneFindShard::SetTutorialFind Ge273a4** creates CSRPopUpTutorialBase, stores it in scene+6c0/control+6c4, initializes it, and runs a nested sequence of original UI focus/message callbacks. It is not a server-request tutorial step.

The callback reached after the second guide message has a concrete hardcoded UI lookup: **Ge2a184** constructs literal **"017"** (LDRe2a1b8/slot e2a380/ADDe2a1ba), calls **FindCastByName<CMDrawable> at e2a1cc**, then reads the returned pointer at e2a1d0 and **dereferences it without null guard at e2a1d2**. Virtual method+90 produces a rectangle, GetCenter e2a1de and FocusDraw.SetCircle e2a1ec show the tutorial focus circle. A missing child named017 can fault here before any further HTTP.

**017 is proved to be the scene's UI node name at this point, not a CSRCardInfo reference lookup.** English dialogue naming Lapis does not identify its original card reference ID. No new Lapis hunter/art grant is justified by this evidence.

## Why reference identity supplies the UI child

**CSRViewFindShardNormal::SetCardOnPos G10b36e8** creates CSRCellFindShardNormal through factory10b39a0. It loads INFO pointer at10b3754, takes **INFO+8** (the parsed id string) at10b376a, hashes it with CMHashID.Set10b3770, copies name into the created cell's **+258** at10b3774..378e and stores hash at**+268** at10b3796. It attaches that cell to the Normal view at10b3804. The INFO.id→node-name path is exact, not an inferred string coincidence.

Thus a **type1 Normal reference row with id:"017"** is required for the guide's generated node to exist. Its target_card_id can remain an already published fixture for a bounded compatibility control; that would not recover original Lapis identity/art. The row also needs the previously recovered valid stage, limits and view position compatibility. No running instance, hunter award or tutorial flag clear is required merely to create this child.

Later nested callback **Ge2a718** repeats lookup017 (LDRe2a73c/ADDe2a742), then looks for **BT_NOR_HT** (LDRe2a754/ADDe2a756) inside it. This is the native next click/finger dependency. A string alias without the real generated cell/button hierarchy is insufficient.

## Callback attribution and ordered path

First focus callback **e29894** is selected by SetTutorialFind: function vtableELF216efe4, invoke slot+20 pointsELFe19895/G e29895; actual RTTI names CSRSceneFindShard::SetTutorialFind $_4. The literal-loading instruction pair is e2743c/e27442 and the callback is registered with FocusDraw.AppearAfterFade e2744c.

Nested vtable/RTTI links recover this original chain:

- e29894 sets first comment, then Message.Appear→**e29ae8**.
- e29ae8 registers WaitForTouchInput→**e29bc0**.
- e29bc0 Message.Disappear→**e29d0c**, which sets the second comment (SetComment e29d74).
- e29d0c Message.Appear→**e29f60**.
- e29f60 WaitForTouchInput→**e2a038**.
- e2a038 Message.Disappear→**e2a184**, the unguarded017 focus lookup above.
- Later e2a718 supplies the017/BT_NOR_HT continuation.

Each nested function was obtained from the actual callback vtable invoke pointer and typeinfo name containing the progressively nested SetTutorialFind lambda, rather than nearest-symbol attribution. Guide speaker string **C004** at e298c8/e298ca and e29d40/e29d42 is the dialogue speaker resource, not the missing-hunter target_card_id.

## Acceptance and limitations

The parent's control renders the Search map and source006 portrait, then dies advancing the second line. The current fault has no mapped guest ARM PC; a missing017 child is a strong concrete matching dependency, not a certified live crash instruction. A narrowly reconstructed017 Normal row can be tested through the original guide, preserving ownership, flags and selection. Passing that point would corroborate the hypothesis; stop before any unsupported Begin/consumption transition.

If a parent decomp is still useful, target **e2a184**, **10b36e8**, **e2a718**, and **e29d0c**, resolving exact literals. Original Lapis ID, full tutorial search target/instance policy and Begin lifecycle remain separate unknowns. Do not skip the guide or manufacture completion flags to make this node exist.

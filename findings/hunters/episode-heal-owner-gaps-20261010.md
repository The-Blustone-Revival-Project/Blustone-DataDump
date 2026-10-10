# Small remaining Episode healer admission measurements

Read-only review of AGENTS226/227, current typed observer and existing native
evidence. No ADB, UI, Ghidra or source edits; this note does not claim live
acceptance or a new root cause.

Inline reservation is already source-closed: IsSkillReserve G9e6dc8 tests
game3d8/3dc nonzero. Do not expand this to dereference effect storage3e0..3e8.

The smallest additional branch is **background pause ownership**. IsBGPaused
G9dfb1e reads game284->object278 and masks the requested reason8; gamepause140
and actorpause278 are separate. The existing getter export does not identify
the concrete background allocation/control. Export **CSRGameBase.OnInit
G9c1820** and locate the actual producer/store of game284 (and its companion
owner if present). The nearby named CMDrawable factory **G9c0c2c** is a narrow
candidate only until its actual call/result is tied to that store. Recover
concrete object/control vptrs, offset, allocation extent and lifetime producer;
then a read-only observer can repeat the owned pair and pause field. A mapped
game284 pointer and compatible CMUpdatable prefix alone are insufficient.

For **opposite-front viewport intersection**, export the exact listener
**G9f7604**, particularly its bounded-input/rectangle-match instructions before
G9f7816. Identify the exact viewport rectangle producer, consumer overload and
owning object; do not substitute renderer physical/logical rectangles merely
because they contain similar dimensions.

Existing GetFrontBound **G986638** is a hidden-return rectangle consumer with
actor in r1. It follows actor+a28 and component virtual54. The current opposite
M024's image component branch is **CMComponentStateMachineImage**, primary
ELF21363d4: virtual54 **G7040b0**, drawable pair beginning64c, then inline
CMRelationRect at component+b4. **AlignBy G754438**, **Update G754488** and
**Result G754464** lead to the result at component+dc..e8. These getters perform
updates; a raw copied result must not be called current without proving inputs
and reconstructing the relevant relation arithmetic. Export those narrow
functions and the drawable64c owner producer if its allocation remains unknown.

The separately qualified Spine67c/680 CMSpineNode branch (virtual54 G7067be)
does not close the M024 image relation rectangle. Existing source/front typed
stun0, cached button intersection and opacity255 likewise do not close either
missing gate or demonstrate callback delivery. Preserve prompt normal combat
and refusal semantics while acquiring one coherent event-time measurement.

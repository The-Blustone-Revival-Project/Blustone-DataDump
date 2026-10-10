# Episode actor and body renderer ownership

Read-only original ARM ELF `.dynsym` and bounded Thumb decoding, plus retained
decompilations. No adb, Ghidra, server/state/tool changes or asset mutations.
Offsets are hexadecimal; ELF offsets are runtime offsets from library load bias.
Code labels with G use the retained Ghidra coordinates (ELF +10000). Original
source: `analysis/extracted/lib/armeabi-v7a/libnative_core.so`; PT_LOAD mapping
was used for reads, including writable-segment virtual/file differences.

## Actor pairs from group membership

`ghidra-episode-actor-group-members.txt` FindActor G9a30e0 proves the all-members
list sentinel group+27c, first node group+280, node next+4, actor node+8 and
control node+c. The active-list counterpart remains the separately recovered
group+29c sentinel / group+2a0 first node. Preserve root's bounded traversal
and repeated owner/node checks; a readable arbitrary actor is insufficient.

Exact original dynamic-symbol primary-vptr offsets (+8 from each `_ZTV`):

- CSRGameActorMob: object **214a638**, emplace control **214bd9c**.
- CSRGameActorHunter: object **214a3fc**, emplace control **214bdc4**.
- CSRGameActor: object **21494cc**; no corresponding base emplace control
  is established by this bounded investigation.

Original emplace `__on_zero_shared` G9fe6b0 (Mob) and G9fe7e8 (Hunter) both
begin `ldr r1,[r0,#0x10]!; ldr r1,[r1]; bx r1`. The shared control destructor
dispatches on the embedded object at **control+10**, not control+c. For these
two exact branches require actor == control+10, exact matching object/control
primaries, nonexpired signed control+4 >=0 and repeated ownership checks.

Additional symbol identities, useful for rejecting/recording other branches:

- CSRGameActorUI object214d938 / emplace-control214bb78.
- CSRGameActorBossAuto object2149bb8 / emplace-control214bcdc.
- CSRGameActorHunterAuto object2149b98 / emplace-control214b6bc.

Those additional symbols prove identities only. Their exact control-to-object
relations were not decoded here; do not silently generalize Mob/Hunter +10.

## Current body pair and renderer branch

Original `ghidra-episode-actor-resid-getter.txt`, GetResID G99b342,
returns actor+888. Decode a bounded version-specific libc++ string;
do not derive resource identity from the portrait or assumed monster ID.

`ghidra-episode-m022-actor-materials.txt` LoadRes G982e28 proves the body pair
**actor+a28 / actor+a2c**. It removes an old pair, asks SRIsSpineSDChar(GetResID),
then creates CMSpineActor when result==1, otherwise CMComponentStateMachineImage.
The selected pair is assigned to those exact fields, then passed to
CMUpdatable::AddComponent on the recovered FindByPath owner. That static call
does not itself prove attachment in the live snapshot.

Exact original body branch identities:

- Image: CMComponentStateMachineImage object primary **21363d4**,
  emplace control primary **2149a04**.
- Spine: CMSpineActor object primary **2136510**,
  emplace control primary **21499dc**.

Original make_shared G98ce0c (image) allocates688 bytes, writes control primary
at G98ce3a, then advances r0 by10 before constructor G702b58. Original
make_shared G98ccf0 (Spine) allocates6a0 bytes, writes control primary at
G98cd1e and likewise advances r0 by10 before constructor G70575c. Both returned
pairs store constructed object/control together (G98ce44 / G98cd28).
Consequently require **body==bodyControl+10**, matching exact branch primaries,
nonexpired signed bodyControl+4 >=0, and repeated actor/body pair validation.

This distinguishes the live image/Spine branch without calling classifier,
constructors, native getters, or rendering methods. A nonnull Image object
alone does not prove animation records loaded, material visibility, owner
attachment, current state name or processed combat hits. In particular, the
current CMComponentStateMachineImage+64c/+650 pair read by OnAttach G702f8c is
an internal component pair; this bounded decode does not prove it is the
actor's attachment owner. Do not report that pair as an owner without further
original constructor/member evidence.

## Minimum read-only snapshot result

Report actual resource ID, actor/control branch, body/control branch or null,
and whether all bounded/repeated ownership checks passed. Continue to separate
selected CB0102 identity from active HUD/pause/modal/team guards. This evidence
supports the next investigation of M022's live renderer; it does not diagnose
the invisibility or justify new packs, aliases, stat changes, or body writes.

## Follow-up: null source bodies require front-map membership proof

Root's live snapshots68/70/80 reportedly found two M022 source actors with
the exact Hunter object/control branch, resource ID M022, HP450 and null
body+a28; C005 and owned party actors had nonnull Spine bodies. Those facts
prove null fields in those particular source actors. They do **not** establish
that each source actor was selected as the current front actor or that a native
LoadRes attempt failed.

`ghidra-episode-front-actor-null-body.txt` MakeFrontActor G9ddc3c reads its input
actor serial, then looks it up in a separate serial-indexed tree on the game.
It calls LoadRes on that tree's actor pair, not directly on its input pointer:

```text
game+3fc = tree begin
game+400 = root / end-sentinel address
game+404 = tree count
node+0 / +4 / +8 = left / right / parent
node+10 / +14 = serial low / high
node+18 / +1c = actor / control
```

The root, serial and pair offsets are explicit in MakeFrontActor.
`ghidra-complete-58-makecamp.txt:806-964` additionally proves begin/count and
insertion: the same local_128 actor/local_124 control added to the group is
inserted at node+18/+1c using its serial. Thus **the map is not evidence of a
different front clone**. Compare actual pointer/control identities by serial
before claiming either same-object or different-object behavior in this run.

Original bounded Thumb GetSerial G99abb8 reads actor+880 into returned low
word and actor+884 into high word. Require exact 64-bit matching serial,
bounded tree traversal/count, parent/sentinel checks, exact pair ownership
and repeated game/tree/source/front checks. Merely decoding the first node
or accepting a missing serial would silently associate a different actor.

MakeFrontActor checks the mapped actor's old+a28 to decide whether to create
a character UI/event bindings, but calls LoadRes on that actor regardless.
It tests LoadRes's return and returns an empty pair on zero. The previously
retained LoadRes decompilation's **void return is incomplete**: original Thumb
G983802 compares the canary; its normal epilogue G98380c explicitly executes
`moveq r0,#1`, then returns at G98380e..814. Normal loaded execution therefore
returns1. No ordinary early null-body return is established in the retained
LoadRes body; both branches create a renderer and RunWithoutState G9839cc
dereferences body+a28 for its virtual+5c call. A null source body alone cannot
be rephrased as failure of this loader or proof of missing material records.

The next safe discriminator is whether a null-body M022 source actor is in
the actual front selection and whether MakeFrontActor used its matching
serial pair. The static map itself contains the actor population; membership
alone does not prove an actor has been selected front. Preserve this distinction
when choosing further fields/call-path evidence.

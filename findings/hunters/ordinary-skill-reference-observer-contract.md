# Ordinary reference skill observation: retained layout and remaining owner proof

2026-10-09. Read-only inspection of retained exports and the host observer;
no Ghidra, ADB, runtime access, native invocation or server/client edit.
Addresses below are retained Ghidra addresses unless explicitly marked ELF;
Ghidra address = ELF offset + 0x10000.

## Proven lookup structure

The existing `InspectNativeInput.inspectCards` follows the weak singleton at
ELF `21cf2d0`, requires the default-delete control primary at ELF `2141730`,
nonnegative signed shared-owner count and control+0xc equal to the container.
This is the **ordinary reference container**, not owned inventory. The method
name `--cards` does not imply that its result is an owned-card snapshot.
Its implementation currently reports only reference identity, resource prefix
and training byte; it does not prove that skill effects were parsed.

`card-ref-map-registration.md` and `native-getcardinfo.txt` (G b2126c)
establish the outer tree: container minimum+0, root+4, count+8; node left+0,
right+4, parent+8, color+0xc, string key+0x10, shared CardInfo pointer+0x1c
and shared control+0x20. Outer nodes allocate 0x24 bytes. CardInfo is a
plain object: its ID string starts at +0, prefix at +0xc, not at +0xc/+0x18.
`native-card-bootstrap.txt` allocates 0xc4 bytes including a 0xc shared-control
header and selects CardInfo at allocation+0xc, making the contained object
0xb8 bytes. This is an emplaced ownership form, distinct from the singleton's
default-delete owner.

`native-getcardinfo.txt` G 8711e0 initializes the normal reference skill map:
CardInfo minimum+0xac, root/sentinel+0xb0, count+0xb4. Its copy loop inserts
the node pair at +0x10. `card-stat-panel-crash.md` recovers GetSkillInfo
G 87aef8: for awake_step=0 it searches that root by integer SRSKILL_TYPE and
returns inline SRSKILL_INFO at node+0x14. The slot key is node+0x10. The
awake branch uses a separate reference; it must not be conflated with this map.

SetCard G 87baa4 calls SRSKILL_INFO.parse G f219ac and SetSkillInfo
G 87b1e0. Parser type is INFO+0x28 and is the insertion key, while
target_rank is INFO+0. `skill-cooldown-units-contract.md` proves the parsed
cooldown is f32 at INFO+0x50, normalized by /1000. Thus a bounded normal-map
read can ultimately prove the selected types3..5 are present and inspect
their parsed metadata without starting combat. Presence alone cannot prove
their effects match the source or that a rank-admitted aura was registered.

## Missing proof before extending the live reader

Do not reuse the singleton's control vtable for per-card controls. The retained
SetCard dump writes a relocated vtable value as a DAT expression; this lane
has not resolved its exact emplaced-CardInfo primary address. Export/resolve:

- SetCard G 87baa4 allocation/control initialization and exact CardInfo
  shared-control vtable primary; on-zero-shared G 87f5f8 corroborates the
  allocation+0xc relationship (symbol retained in native-evidence.tsv).
- SetSkillInfo G 87b1e0 and tree allocator G 87b9ba for exact node allocation
  extent, initialization and parent/header behavior.
- SRSKILL_INFO copy G 8628f0 and assignment G 87b234, plus parse G f219ac,
  for complete INFO extent, effect vector header, effect element extent and
  field offsets. The constructor consumers suggest an effect list at +0x2c,
  but that observation alone is not a complete typed vector contract.

Until these are qualified, do not follow effect storage or emit a claim of
native type3..5 payload fidelity from an ordinary-reference snapshot.

## Bounded reader requirements once those exports are closed

Require the verified current client and a one-shot safe menu render frame.
Search only keys001/003/004, validate outer node and per-card shared owner,
and compare actual CardInfo ID to its outer key. Bound both trees by count,
depth and visited sets, enforce alignment and mapped ranges, and validate
root-parent/sentinel relationships. Normal skill lookup is unsigned integer
comparison, not string comparison. Repeat shared pairs, tree headers and
captured record bytes before publishing; reject changes rather than combine
registrations. Empty map must have root0/count0/minimum equal to its sentinel.
Never call GetSkillInfo (throws on a missing key), FindSkillInfo (may construct
a copied shared result), a lazy singleton getter, or any native parser.

For complete payload proof, compare parsed floats in their normalized native
units to source-derived expectations; preserve the distinction between the
original selected Episode rows and their local ordinary-card adoption. Save,
rank, skill level, progression and rewards require no mutation for this audit.

## Root source closure and live read

The remaining allocation/copy exports were completed in ghidra-ordinary-skill-layout.txt, ghidra-reference-result-layout.txt and ghidra-card-info-control-vtable.txt. CardInfo owner primary ELF214166c/emplace+c/objectb8; normal skillnode74/inlineINFO14/extent60; effects are a circular list, not a vector: INFO2c last/30 first/34count, nodec0/result+8/extentb8. New bounded observer passed a safe-map frame, retaining first captures and rejecting changed repeats/minima/alignment. All selected main effect prefixes loaded; nested/secondary lists are still outside its scope. See testing/ordinary-skill-reference-001/report.md.

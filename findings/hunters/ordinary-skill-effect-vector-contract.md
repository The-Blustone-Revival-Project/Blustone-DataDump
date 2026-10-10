# Ordinary skill effects are lists: allocation, fields and parser transforms

2026-10-09. Read-only review of AGENTS.md §191, retained contracts and root's
completed `ghidra-ordinary-skill-layout.txt` export. No Ghidra, ADB, native
invocation, account mutation or source edit by this lane. All addresses below
are Ghidra addresses (ELF offset + 0x10000).

## Allocation and container correction

Despite this report's requested filename, ordinary SRSKILL_INFO effects are
**circular doubly linked lists**, not a contiguous vector. Do not use the
runtime AURA vector's stride0xe8 for these reference rows.

SRSKILL_INFO copy constructor G8628f0 initializes sentinel INFO+0x2c, writes
both links to the sentinel, and zeros count+0x34. It walks the source first
pointer INFO+0x30 until source INFO+0x2c, following node+4. Each copied node
allocates0xc0 bytes, stores previous at node+0 and next at node+4, and constructs
SRSKILL_RESULT_INFO at node+8. The result's inline extent is therefore0xb8.
Append updates old-last.next, sentinel.prev and count. There is no per-effect
shared control or polymorphic vtable in this allocation path.

The complete list header is INFO+0x2c last, +0x30 first, +0x34 count. A second
result list has sentinel+0x38, first+0x3c and count+0x40; its exact role should
remain qualified until its consumers are traced. Assignment G87b234 explicitly
calls std::list::assign for both headers. Skill-tree allocator G87b9ba allocates
0x74 bytes, stores integer key+0x10 and inline INFO+0x14, establishing INFO
extent0x60. Copy includes final string INFO+0x54..0x5f.

For a bounded reader: require count <= chosen small ceiling; empty first and
last must equal the sentinel. For nonempty lists, validate each full0xc0 mapped
node, alignment, uniqueness, previous-link continuity and final next=sentinel;
require exactly count nodes and last-header agreement. Repeat node bytes and
both headers before output. Never add0xc0 to find the next element.

## Numeric result prefix and units

Retained `aura-payload-identity-contract.md` and
`starter-skill-combat-mechanics.md` recover the parser's result scratch base and
the copied numeric prefix:

```text
result+00 u32 serial              +04 i32 target_type
      +08 i32 target_stat         +0c i32 refer_target_stat
      +10 i32 refer_target_type   +14 i32 effect_type
      +18 f32 delay               +1c f32 coefficient
      +20 f32 coefficient_up      +24 f32 duration seconds
      +28 f32 duration_up seconds +2c f32 interval seconds
```

The old scratch sp+0x110 and the new decompiler local_120 denote the same result
base; do not add either local name to INFO offsets. Parser Gf219ac normalizes
base/up by100 and duration/duration_up/interval by1000. Delay is zero on this
inspected wire path; no delay JSON field was recovered. Nonfinite floats must
fail the read. Raw integer result+0x30 exists separately from coefficient+0x1c;
its full interpretation and the descriptive/nested members are outside a
numeric-prefix-only comparison.

Additional exact exports needed to independently close all result members:
SRSKILL_RESULT_INFO copy constructor **G862c16** and assignment **G988d5c**.
The existing constructor call sites establish storage bounds already, but do
not by themselves label every byte of the0xb8 object. A prefix read proves
selected normalized numeric fields, not full result byte fidelity.

## Parser changes cardinality and effect types

The parser is not an identity conversion of every JSON effect array. The
completed export's Gf225d6..Gf2267e searches the main list for target_stat17
(node+0x10 = result+0x08). **Only if such a row exists**, it scans effects and
rewrites effect_type6 to4 or effect_type5 to3 (node+0x1c = result+0x14), copies
the rewritten row into that stat17 row's nested list (sentinel node+0xa8,
result+0xa0), then unlinks/deletes the original and decrements main count.
Do not expect an unconditional type5-to-Buff3 conversion.

The earlier parser branch also converts nonzero-interval HP1 effects: negative
coefficient becomes stat32/Debuff4 and creates a stat33 counter companion;
positive coefficient becomes stat31/Buff3. An effect_type7 row can attach to
the preceding main result's nested list. These paths matter when comparing
source order/cardinality to a parsed list; raw JSON count alone is insufficient.

Selected Tyltyl EVCB0201_004 slot4 has effect_type5/stat19 followed by positive
HP1 heal, both interval0 and **no stat17 row**. The reviewed transform therefore
does not prove its type5 becomes3 or disappears. Its actual parsed tag must be
observed. Retained `ghidra-aura-signed-counter.txt` Apply G99c450 stat19 branch
calls AddBuffImmuneDbf, including raw-integer and nested-list paths. That closes
a downstream stat19 consumer, but not complete effect_type5 admission,
triggering, immunity, target membership or live application. Do not relabel
the selected row as an ordinary Buff3 in server data.

## Claim boundary

Reading selected ordinary reference cards001/003/004 and their five skill slots
can establish native loaded metadata and normalized main-list prefixes while
preserving ranks, levels and progress. It cannot establish owned-card state,
rank admission, conditional type4 selection, aura recipient application, or
original final ordinary balance. The restored rows remain original Episode
tuples adopted into ordinary cards by explicit local policy.

## Root verification follow-up

Exact copy862c16/assignment988d5c exports now retained in analysis/ghidra-reference-result-layout.txt. Live read confirms Nene type4 becomes kind3/stat31/base1/duration3.1/interval1, while selected Tyltyl type4 keeps kind5/stat19/base.1/duration4 and its separate HP1/DEF/base.2 result. This proves parsed main prefixes, not runtime activation or complete nested payloads; all observed raw nested counts0. Detailed evidence: analysis/testing/ordinary-skill-reference-001/report.md.

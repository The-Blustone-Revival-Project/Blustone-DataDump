# Original campaign map animation wrapper audit

2026-10-09. Follow-up to `campaign-stage-map-original-art.md` after root
recovered LoadAnim2's CRMAnim2/type-0xb requirement. Read-only original asset
inspection; no Ghidra, emulator, runtime, server reference or source mutation.

**No original AT animation in the preserved final-client PAD corpus references
the exact MS_MAP1 or MS_MAP2 sprite identities.** Therefore this corpus does not
provide a valid original animation wrapper for assigning those S2 sprites to
the current area-reference `resource_id` field consumed by LoadAnim.

## Exact scope and result

Inspected all **774** `*.jet` files directly under
`recovered-assets/phone-2026-09-18/extracted/split_PADResource/assets`.
The outer header walker reads uint32 packed length at+8 and uint64 identity
at+12; zlib bodies are inflated before inspecting their actual type signature.
The search is by typed frame references, not filenames, printable strings or
arbitrary occurrences of an ID's byte sequence.

- Original AT records parsed: **3,002**.
- Original package walks ending at exact EOF: **774 of 774**.
- Invalid AT frame walks: **0**.
- AT frames referencing `MS_MAP1`, exact uint64 `0x0000000ff52822ff`: **0**.
- AT frames referencing `MS_MAP2`, exact uint64 `0x0000000ff5282300`: **0**.

For each AT body, read uint32 count at+43, start at+47, and consume each
frame's uint64 resource reference, float duration and uint16 event length,
then the declared event bytes. Every parsed cursor ended exactly at the
inflated record length. Counts above 10,000 or short/trailing bytes would
have failed the parser; none occurred. Both target identities were derived
from the original MAP_ZONE_1 S2 headers, independently matching native base38
names with alphabet `0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ._`.

## What this disproves and what it does not

The original `MAP_ANI` in UI_TUTO references MAP_ANI_01..21, not either
MS_MAP sprite. Its inspected 133×47 ring frames cannot serve as evidence for a
landscape wrapper. Renaming it or rewriting its frames would be invented art
binding, not recovery. No wrapper was generated.

This is a negative result for the preserved PAD corpus only. It does not prove
that a wrapper never existed on the original CDN, that the original area
reference selected these particular sprites, or that other loader/UI paths
could not display them. Root's independent native export owns the type gate
and field-selection claim; this report establishes only asset-frame absence.

The original per-area animation reference rows remain missing. Choosing a
different original animation for all local areas would be an explicit local
display policy and would require visual confirmation and separate ownership
validation. Assigning S2 directly to a confirmed animation-only loader or
inventing MAP_ZONE_2..5 filenames is not supported by this evidence.

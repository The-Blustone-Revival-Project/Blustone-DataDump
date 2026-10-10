# Search guard padding/loader metadata audit after two bootstrap aborts

2026-10-05. Independent read-only comparison of original ELF and reviewed v2 candidate SHA256314df992afc1535e7608c44b75954cbf19c9a2999b1470d1636a2e9cc684ff34. No VM, Ghidra, process control or implementation edits. Parent reports two +10 bootstrap std::bad_alloc aborts before guide entry and a preserved +9 A/B control pending; this report does not establish causality or runtime acceptance.

## Exact original layout

All addresses here are **ELF VAs/file offsets where equal**, not Ghidra coordinates:

```text
.rel.dyn 515a10..610ed8
.rel.plt 610ed8..611ab0
.plt     611ab0..612c88
Gym near 612c90..612c9c (existing copied patch)
Search near612c9c..612cc0
.text    612cc0..1bd46f8
.ARM.exidx1bd46f8..1c2cc20
.ARM.extab1c2cc20..1d52928
original RX PT_LOAD file/VA0, filesz=memsz210d320
Search cave210d380..210d404
RW PT_LOAD file210d550, VA210e550
```

The near patch does not overwrite .plt: it starts20bytes after that section's end and ends exactly at .text's beginning. Original last ARM PLT entries at612c70..612c84 calculate GOT addresses using ADDip,PC/ADDip/LDRpc; they do not fetch a literal from the new near span. Actual PLT bytes compare unchanged against v2. The occupied Gym near span and prior Gym far cave compare byte-identical to the previous reviewed candidate.

The far patch lies beyond original RX filesz but within its already-rounded final4096-byte page. V2 changes only RX filesz/memsz to210d404; RW offsets/VAs/sizes remain unchanged and the loader mapping page count does not increase. This is a concrete layout property, not proof that every Houdini behavior is unaffected.

## Loader, relocation and symbol checks

Independently parsed all original ELF sections/program headers/dynamic tags, defined symbol addresses and relocation entries. Neither Search span contains:

- A defined symbol value (Thumb bit normalized).
- Any relocation site or resolved relocation target under the original ELF's relocation decoding.
- Any aligned original uint32 word whose absolute value/Thumb-normalized pointer falls inside either span: **zero hits in the entire original file**.
- Any PT_DYNAMIC pointer value.
- Any decoded EHABI exidx function PREL31 target or extab PREL31 target.

The original .dynamic, .rel.dyn, .rel.plt, .ARM.exidx, .ARM.extab, .plt and entire section-header table compare **byte-identical** to v2. Program-header differences are confined to4 changed bytes representing RX filesz/memsz: offsets64/65 and68/69. PT_ARM_EXIDX still points to1bd46f8 with size58528; dynamic INIT/FINI arrays remain at21aa85c/21aa854 and are outside both spans. Dynamic GOT remains21b2a08. No overwritten loader metadata or relocation/unwind collision was identified by these scans.

These checks are broader than absence of sections/direct branches, but are not an exhaustive proof of all possible computed PC-relative/ad-hoc data references. An arbitrary relative pointer, arithmetic address construction or translator-specific assumption about zero padding could escape absolute-word/relocation checks. No such original dependency was actually found; it must remain a hypothesis rather than a reported collision.

## Execution/unwind limits

The new cave has no added unwind entries. Its entry temporarily saves volatile regs/LR, performs plain memory reads and comparisons, restores them, then either returns stale or replays the original prologue and branches back. It makes no allocation/C++ call in the cave; the parent/child caves likewise branch to original code/cleanup. Normal throwing C++ calls occur after the branch-back in the original function's existing unwind range. A signal/async walk while execution is in the cave remains a different diagnostic limitation; this report does not certify unwinding an exception through arbitrary cave PCs.

Two bootstrap abort stack scans show generic string-map rehash/next_prime candidates but no identified guard execution frame. The exact bad_alloc owner/size remains unknown, as search-callback-guard-implementation.md records. Metadata absence checks and an unobserved callback cannot prove the new APK harmless; conversely two failures do not supply a concrete padding collision or guard-causality proof.

Parent's retained +9/same-data/same59-asset-profile control also aborted at88% bootstrap with the same std::bad_alloc class and generic rehash stack candidate. Thus the observed failure is not unique to the +10 APK; the guard is not established as a necessary cause. This lane did not independently read the runtime loaded-library hash. Resource/profile/response/environment variables still need discrimination. No loader/resource rewrite, data clearing, exception masking or process kill follows from this read-only audit.

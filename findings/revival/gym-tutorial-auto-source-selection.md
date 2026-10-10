# Gym tutorial auto-source: first candidate, with inactive sorting

2026-10-04. Read-only original ELF/RTTI/Capstone. No adb/Ghidra/source edits, recruitment, card changes or final Train press by this agent. Tester observed protected original Mowgli2 automatically selected for target Tyltyl5 and stopped before mutation. Preserve originals; no manual Clear8/1 or feeding2 is proposed.

## The tutorial bypasses normal source-click eligibility

The responsible nested SetTutorialLevelUp guide callback's exact **Thumb entry is0xeeb7b8** (ELF callable0xedb7b9). Its hidden function vtable **ELF0x21770c8**, invoke slot+0x20=0xedb7b9, has RTTI naming the deeply nested **CSRSceneTutorialLevelUp::SetTutorialLevelUp** lambda. Exact literal slot0xeeb798/addPC0xeeb78c resolves that vtable, independently proving callback ownership.

It does **not hardcode source serial2**. It uses the first entry of the current candidate vector:

```text
0xeeb7d2 candidateBegin = this+0x65c
0xeeb7d6 candidateEnd   = this+0x660
0xeeb7da compare begin/end; empty ->SceneBack/toast path
0xeeb7fc load FIRST uint64 serial from [candidateBegin]
0xeeb802 Inventory.FindCard(serial)
0xeeb832 only checks found pointer nonnull
0xeeb836 reload same serial
0xeeb83c TableLevelUp.AddStuff(serial), function0x101e3dc
```

There is **no IsInactive/lock/leader/deck check in this auto-add callback**. Ordinary source clicking uses eligibility separately; gray rendering does not protect this tutorial auto-add when every candidate is inactive.

AddStuff0x101e3dc appends serial directly into selected-source vector **this+0x668/+0x66c/+0x670** (begin/end/capacity), at0x101e40e or vector push-back0x101e420, then sorts/updates its view. It does not invoke IsInactiveCard before append. Note: **+0x668 is a vector begin pointer, not a scalar source serial.** Tutorial request copies its first uint64 entry at0xeebece..0xeebed4 into a one-source request vector, then calls RequestLevelUp0xeebf74 with is_tuto1. Thus if2 is auto-added and remains first selected, native will actually name2 in the request unless interrupted; server protected-source validation must remain intact.

## Why a new eligible donor can change the first candidate

Candidate generation is **CSRTableLevelUp::ArrangeStuff0x101c854**. It gets Inventory.GetCardInstIDList0xaeaff4 at0x101c88c; removes reference-invalid/disallowed entries via helper0x102076c, excludes target serial this+0xd48/+0xd4c at0x101c95e..0x101c9b2, excludes already selected serials, then invokes sort helper **0x10208c0 at0x101cada**. OnReset0x101b3f4 calls ArrangeStuff0x101b9b8 and swaps its result into candidatebegin/end/capacity+0x65c/+0x660/+0x664 at0x101b9dc..e6.

The sort comparator is **Thumb entry0x1020c34**. It first groups by card-info training/source flag+0x3c (0x1020d16/0x1020d24). When both flags match, it invokes **IsInactiveCard0x101dab8** for lhs at0x1020d7e and rhs at0x1020d8e. Different inactivity results branch0x1020d94→0x1020ee4. That branch returns **rhsInactive==1**: call0x1020ee8, subtract1/CLZ/shift0x1020eec..ef2. Hence an active eligible ordinary card sorts **before** an inactive ordinary card; all-inactive lists can still have a protected original at their front.

Normal original1/2/4 and a fresh ordinary Tyltyl6 use the same ordinary is_source0 group. If6 exists, meets candidate filter, is unlocked and not leader/protected deck/active-battle material, while1/2/4 remain inactive,6 should sort before them **after ArrangeStuff refresh**. This is a concrete native mechanism, not a promise that adding any card alone fixes the screen. A newly recruited locked6 remains inactive until the real unlock callback updates it. Different training-card flag groups or stale/frozen candidates require separate control.

This explains both observations: with no eligible donor, auto-add can choose gray Mowgli2; with one genuinely eligible donor, native ordering can make that donor first. **Do not remove originals from decks or unlock protected originals to satisfy the guide.** Preserve server defense rejecting protected source IDs even with is_tuto1.

## Native cost0 display does not change source safety

After AddStuff, the tutorial explicitly overwrites cost textbox this+0xc60 with to_string(0):0xeeb840..0xeeb854. This proves the observed **display0**, not an original server pricing response or authorization to spend any protected card. Current server100/source price is a local fixture; tutorial subsidy semantics/UI-price consistency should be handled explicitly by parent before declaring complete fidelity. No source check may be relaxed for flag1.

## Bounded safe next control

The user authorized one fresh donor only conditionally: ordinary single recruit must successfully create6, lock-toggle must make6 unlocked,6 must remain outside leader/protected decks/active battle, and the actual tutorial candidate/selected source must visibly or read-only prove **only6** before final Train. Refresh/reenter normally so ArrangeStuff actually runs; do not assume the force-stopped screen's source vector or saved guide phase automatically rebuilds safely.

Optional bounded native fields under exact TutorialLevelUp/TableLevelUp class guards: **TutorialLevelUp primary vptr B+ELF0x2176e20** (`_ZTV23CSRSceneTutorialLevelUp`0x2176e18+8), or ordinary **TableLevelUp primary B+ELF0x218278c** (`_ZTV15CSRTableLevelUp`0x2182784+8). Candidatebegin/end+0x65c/+0x660, selectedbegin/end+0x668/+0x66c, target uint64+0xd48/+0xd4c. Read at most32 uint64 IDs, validate aligned mapped begin/end and stable scene pointer; print IDs only. **Stop if selected2, ambiguous/multiple donors, unknown class, or unstable snapshot.** This specification does not authorize a final press in those cases.

Parent decompile targets for independent corroboration: **0xeeb7b8..0xeeba04** (actual auto-add callback), **ArrangeStuff0x101c854..0x101cb70**, comparator **0x1020c34..0x10210ac**, candidate exclusion predicate **0x102076c**, ordinary **IsInactiveCard0x101dab8**, and **AddStuff0x101e3dc..0x101e580**. Decompile correct Thumb entries, not isolated interior BL instructions.

Guide success Clear8/1 and its premature-error callback sequencing remain documented in `training-onboarding-clear-contract.md`; that Clear packet alone cannot prove safe donor consumption. The separate free-fuel unlock still requires actual stage8 achievements.

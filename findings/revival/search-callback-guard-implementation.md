# Search Partner continuation guard implementation

2026-10-05. Exact original callback ownership/addresses are in
search-home-callback.md. This guard applies only to copied instrumented libraries.

Three hooks cover callback entry, parent lookup result and SET_CK lookup result.
Entry compares captured raw scene to g_pApp→app+8→manager+34 before lookup; stale
callbacks return without constructing an original stack frame or writing Target.
Missing parent initializes the otherwise unconstructed child pair and follows
original hash/parent/child cleanup. Missing child follows original child-control
cleanup and stack-cookie epilogue. Valid paths replay original instructions and
visibility call. No helper data, guide flags, costs or scenes are synthesized.

Code uses three PIC trampolines in36bytes immediately after the existing Gym
near trampoline, plus132bytes in the same already mapped RX page. No section,
other-load, prior-patch or direct branch-target overlap was found. The first
candidate had two even Thumb pointers; independent review rejected it before
APK build. V2 normalizes offsets, checks actual emitted pointers and passes the
pinned byte/branch verifier. The verifier rejects the first candidate.

Ten Unicorn ARM/Thumb paths ran against synthetic memory: valid/stale/null scene
chains, register/stack preservation, parent/child null cleanup through the actual
original epilogue, and valid replay. Independent static review passed v2 SHA
314df992afc1535e7608c44b75954cbf19c9a2999b1470d1636a2e9cc684ff34.
These checks do not establish Android runtime acceptance.

Rebuild retained assertion log-continue, guarded Gym recovery and six Episode
layouts. Signed APK package/seed/native override checked. Required experimental
pre-release +10 publication/runtime acceptance are tracked by the parent. No
server account/resource/tutorial mutation is part of this patch.

## First +10 bootstrap abort: bounded diagnosis

Parent's retained episode-002/05-abort-reason.txt records PID6233 terminating with uncaught **std::bad_alloc** at14:14:42.464. episode-002/05-bootstrap-crash.txt is a **stack candidate scan**, not a reconstructed call stack. The actual ARM-PC/LR are libc abort locations; the following library words are possible saved addresses/data and must not be treated as proved frames.

The notable **ELF741659** candidate maps to **G751658**, inside string-to-string unordered_map **__rehash** startingG75156c. At that exact address the instruction is **MOVr6,r1**, immediately after unsigned-modulo helper callG751654. It is not the allocation that threw. The same rehash's earlier bucket allocation computes bucket_count*4 atG751586 and calls operatornew atG751588; counts>=40000000hex take an explicit failure path atG75157e/G75174e. No live bucket count or map owner was captured at those operations.

**ELF1ba6189** maps to generic libc++ **__next_prime G1bb6188**. Its presence does not identify a particular server DTO, package record or resource-cache object. The shared string/string hash-table instantiation is also used by real HTTP request form construction (unordered_map initializerG74f7e4), so its symbol alone cannot establish resource-cache ownership. No unique calling request/resource path is proved by this trace.

The trace contains bad_alloc destructor/typeinfo candidates, confirming the exception class but not the requested allocation size or cause. No Search Partner callback/guard address or evidence of a guard execution was observed before this bootstrap abort. A new pack/download, guard regression, actual memory exhaustion and malformed/corrupted sizing must remain hypotheses rather than conclusions. One abort does not justify hiding exceptions, wiping client data, removing resources or blaming the new guard.

Parent scheduled a normal preserved relaunch PID6806 as the discriminating control. Its outcome is not claimed by this read-only diagnosis. Preserve bounded fresh phase/wire/crash evidence if failure repeats; identifying the actual rehash owner and sizing would require stronger call/unwind/context evidence. This lane performed no VM, source, Ghidra or runtime action.

## Preserved comparison outcome

PID6806 also aborted during bootstrap. Retained +9 was then installed over the
instrumented package with Owner0 data preserved; PID7483 aborted at14:32:10 with
the same exception under the same59-asset resource profile. Neither client reached
the callback acceptance path. The new guard is not necessary to reproduce the
current failure; exact cause and +10 runtime safety remain unresolved.

Root also decompiled other stack candidates using corrected ELF+0x10000 addresses
in ghidra-bootstrap-abort-candidates-corrected.txt. Several belong to DNS lookup,
socket connection and cache routines. This further limits any claim that all
candidate words form the throwing call chain. An initial incorrectly offset query
is superseded by the explicitly corrected file and is not evidence.

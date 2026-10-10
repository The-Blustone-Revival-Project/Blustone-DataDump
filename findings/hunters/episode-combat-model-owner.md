# Read-only Episode current combat owner

Read-only research for the root's Episode observer. Sources: retained native
decompilations, original extracted ARM ELF, its `.dynsym` / relocation records,
and bounded Capstone Thumb decoding. No adb, live memory, Ghidra, original file
mutation, server change, stat search or outcome assignment.

All offsets below are hexadecimal. `G` means retained Ghidra coordinates;
`ELF` means runtime offset from the native library load bias, exactly G-10000
for code. ELF program headers were used for file translation; writable data
must not be read by assuming file offset equals virtual address.

## Proven singleton root

The original dynamic symbol
`_ZZN11CMSingleton3getI11CSRMEpisodeNS_12DefaultAllocIS1_EE10CMSpinLockEENSt6__ndk110shared_ptrIT_EEvE5wpRet`
has **ELF21d42f4**. This is the static weak_ptr pair, not a heap scan or a
model vptr. Its guard symbol is ELF21d42fc.

`CSRMEpisode.get` Gb1dee0 calls CMSingleton.get Gb1df44 at Gb1def6.
The generic getter resolves the root through LDR Gb1df6a / ADD Gb1df6c:
literal Gb1e0a8 resolves GOT slot ELF21ad6a8, whose original relocation is
R_ARM_RELATIVE with addend **21d42f4**. Gb1df74 dereferences that GOT slot;
Gb1df76 reads root+4. The weak_ptr lock path reads root+0 as its returned
object at Gb1dfee and Gb1e048, and returns the locked control at Gb1e042.
Therefore a read-only observer can read:

```text
root = loadBias + 21d42f4
model = u32(root+0)
modelControl = u32(root+4)
```

Require both pointers nonzero/aligned/readable, the exact model-control
primary vptr **loadBias+21532bc**, signed modelControl+4 >=0, and
u32(modelControl+c)==model. Re-read the pair and checks after bounded reads.
Do not call the native getter or weak_ptr lock from the observer.

The vtable symbol is
`_ZTVNSt6__ndk120__shared_ptr_pointerIP11CSRMEpisodeNS_14default_deleteIS1_EENS_9allocatorIS1_EEEE`
at ELF21532b4, primary +8. Holder constructor Gb21ad0 allocates/zeros a
**f0-byte non-polymorphic model**. Gb21b70 stores that model in Holder+0;
Gb21b78 LDR / Gb21b7a ADD resolves GOT ELF21ad6c8 with relocation addend
21532b4; Gb21b7e adds8; Gb21b80 writes control primary; Gb21b84 writes
control+c=model; Gb21b88 stores the control in Holder+4. Original default
deleter Gb21c2c reads its object from control+c at Gb21c30. **Do not require a
CSRMEpisode object vptr: its first bytes are data.**

## Proven current COMBAT binding

Retained `analysis/ghidra-episode-decomp-07.txt:1-28` proves
GetCombat Gb17712 returns exactly **model+24 / model+28** and increments
the returned control's shared count at +4. Reading those fields requires no
native call. Retained `analysis/ghidra-episode-first-combat.txt` proves
LoadCombat selects from the original local combat cache, otherwise allocates
the same emplace type and calls the original COMBAT constructor.

```text
combat = u32(model+24)
combatControl = u32(model+28)
```

Require nonzero/aligned/readable pointers, exact combatControl primary
**loadBias+2153248**, signed combatControl+4 >=0, and
**combat==combatControl+c**. Its symbol
`_ZTVNSt6__ndk120__shared_ptr_emplaceIN11CSRMEpisode6COMBATENS_9allocatorIS2_EEEE`
is ELF2153240, primary +8. Original Thumb Gb17322 allocates90 bytes;
Gb17332 writes control+8=0, Gb17334 resolves the vtable GOT,
Gb17338 adds8, Gb1733a writes control primary, Gb1733c writes shared count0
at+4, Gb17340 derives control+c, and Gb17348 invokes COMBAT constructor
on that exact embedded object. This is an emplace relation, not the
default-delete control+c pointer field used for model ownership.

COMBAT+0 is its original C++ combat-ID string. **COMBAT+24 is game_res_id,
not combat ID**; see `analysis/ghidra-episode-combat-actors.txt` and
`analysis/research/episode-first-combat-contract.md`. Decode only a bounded
string through the existing version-specific libc++ decoder, check its
layout/length/readable mapping, then repeat ownership and string checks.
Expected Story04 ID is CB0102 from the recovered original graph. Never
infer it from an Episode scene class or STI099 alone.

## Identity is not an active battle predicate

The singleton is a weak owner of a persistent model. Its current COMBAT can
remain selected while OnFinish pushes its original ending dialogue. Reading
CB0102 proves the selected combat identity; it does **not** independently
prove that the currently visible scene is fighting or authorize attack bursts.
Combine the guarded current scene, current combat ID, initialized native
remain counters, pause state and guarded absence of blocking modals with
fresh visual HUD evidence. Reject snapshots if any owner/pair changes.
Terminal counters preserve the separate existing rule: left>0/right0 win,
left0 loss (including both0), either-1 uninitialized.

The original ELF also exposes Episode scene control-emplace vtable
`_ZTVNSt6__ndk120__shared_ptr_emplaceI16CSRSceneMEpisodeNS_9allocatorIS1_EEEE`
at ELF216fa9c (primary **216faa4**).

## Live wrapper correction and exact child allocation

Root's live default observer49 found current scene primary **ELF216f90c**,
CSRSceneGame, mode+660=7, child+658 primary215352c. The previous assumption
that manager.currentScene directly equals Episode was false for this path.
Inheritance from CSRGameBase does not imply direct manager ownership.

Retained `analysis/ghidra-episode-decomp-07.txt` CSRSceneGame.OnInit **case7**
constructs shared_ptr<CSRSceneMEpisode>, then stores object at wrapper+658
and control at wrapper+65c. Original make_shared **Ge3da44** allocates418
bytes at Ge3da4e. LDR Ge3da5c / ADD Ge3da62 uses literal Ge3db08 to resolve
GOT ELF21ae3b4 with original addend **216fa9c**. Ge3da70 adds8 to obtain
control primary216faa4. **Ge3da76 writes that primary and increments its
object register by10**; Ge3da82 calls CSRSceneMEpisode constructor on this
embedded object. Thus exact child relation is **scene==control+10**, not+c.
The differing alignment must not be copied from COMBAT's emplace relation.

The observer now requires the current manager pair to own CSRSceneGame,
mode7, then follows wrapper+658/+65c and requires Episode primary215352c,
child-control primary216faa4, signed child-control+4>=0, and child==control+10.
It repeats wrapper mode/pair, current manager pair, child owner, model/COMBAT
owners, counters, pause and ID before print. The exact current wrapper
manager-control allocation type still has only the existing repeated pair
and nonexpired checks; that limitation remains explicit. Root owns live test.

## Observer scope

At root's subsequent explicit request, these bounded ownership reads were
added to `tools/InspectNativeInput.java --episode-scene`. It rejects unproved
owners, uses the existing 16-byte `cppString` bound for COMBAT+0, accepts a
nonempty ASCII identifier, and repeats both owner chains and ID before
printing `selectedCombatId`. The subsequent proven wrapper correction above
replaces the false direct-manager Episode guard. The updated helper compiled
successfully with the existing JDK21 into ignored
`analysis/input-probe`; root owns all live validation. A retained ending
scene and a historical clear ACK still cannot retrospectively prove the
earlier CB0101 outcome.

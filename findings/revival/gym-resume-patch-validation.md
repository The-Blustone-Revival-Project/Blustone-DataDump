# Interrupted trainer recovery prototype

Native stage7 gate is already passed at the patched branch. For Gym TU8/nextA8 only, completed step8/0 with GetState(8,1)0/1 reuses the existing TutorialNPC construction at ELF ea27f8. All other cases reproduce original CMP/BGT outcomes. No flag/marker/currency/inventory write, duplicate Clear8/0 or direct AE jump is introduced. Original tutorial callbacks retain target/material/rank requirements.

The instruction hook replaces six original bytes012800f39880 at ELF ea25f0. A12-byte PC-relative trampoline uses section-free zero alignment padding612c90. A92-byte guard uses section-free zero gap210d320 before the next file-backed segment. RX file/memory extent grows to210d37c within the same already mapped last page; RW offsets/addresses, section offsets and original file length remain unchanged. Explicit original-byte, zero-padding, section/other-load overlap and conservative incoming-text-branch checks gate patching.

The assembly contains no undefined symbols or relocation records. Far calls/jumps compute native addresses relative to PC, preserving ASLR. Eight saved words maintain AAPCS8-byte stack alignment; original registers and LR are restored, except scratch R12 for far tail jumps. GetState is independently shown to perform loads only. Original destinations overwrite flags/enter calls before using caller temporaries.

`tools/test-gym-resume-patch.py` runs actual Thumb bytes under Unicorn:300 state/TU/nextscene/pending/ASLR combinations, original fallbacks, fresh query arguments, stack alignment and preserved registers passed. Byte-diff verification restricts changes to hook, two code spans and RX size fields. Original extracted library is explicitly rejected as input/output.

`--resume-interrupted-gym` is opt-in on the instrumented builder. APK native contents, assertion/other-existing-patch checks, Java/D8, LF CURRENT and signature checks passed. Runtime loader and original guide continuation remain unverified until the controlled +8 update; offline emulation is not gameplay proof. A verified +7 rollback APK is preserved locally. Every rebuilt client requires publishing an instrumented GitHub release.

Controlled +8 preserved update now passed normal resource download and village
startup in PID28279. Free indicated Gym entry produced collector vptr2176a48
at1791122371198. Original ELF dynsym `_ZTV22CSRSceneTutorialNPCDlg` is2176a40;
ARM vtable address-point+8 matches exactly. Screenshot75 shows the onboarding
conversation; parent inspected it by eye. This proves original tutorial NPC
entry recovery, not completion of guide8/1, target selection or material action.
No paid/source action or tutorial flag rollback was performed. Release +8 is
published and its GitHub digest matches the built APK.

Adds an opt-in instrumented-only recovery for interrupted Gym onboarding. After the native stage7 gate, the original trainer entry can reuse its existing TutorialNPC construction when Gym step8/0 is completed but step8/1 is actually pending. Native dialogue, selection, oldest-registration target logic and subsequent action callbacks remain responsible for progression.

The recovery preserves tutorial flags, local markers, inventory, balances and other house behavior. It skips the duplicate Clear8/0 path and does not jump directly to guided selection. This is a local compatibility repair, not recovered original server behavior. Rank/level/material requirements and missing original data remain limitations.

Validation:300 offline Unicorn Thumb/ASLR paths checked the exact machine bytes, original fallbacks, GetState call ABI, preserved registers and stack alignment. The patch uses section-free zero padding, checks direct incoming branches and other load-segment overlap, and extends RX bytes within its existing final mapped page. Existing native patch checks, Java/D8 compilation, LF-only LevelDB CURRENT packaging and APK signature verification pass.

Runtime preserved update passed startup/resource download into the village. Free Gym entry now reaches the original TutorialNPC conversation: collector scene vptr `0x2176a48` matches original ELF `_ZTV22CSRSceneTutorialNPCDlg+8`, and screenshots show the onboarding dialogue. This verifies entry recovery only; target selection, training/promotion and source safety checks remain pending. The read-only Gym observer from +7 remains included; original app and extracted library are preserved. Package/code remains `com.vshower.prd_sr.instrumented` / `28010` and requires the local replica/collector. Update the instrumented package with its data preserved.

Further native inspection reaches the original tutorial hunter list. Manual
Tyltyl selection currently opens ordinary detail and Raise, so guided completion
is still unresolved. Returning Home repeats the pending Gym pointer. Ordinary
Raise provides a working native Move to Recruitment path for preparing donors;
no tutorial flags, original hunters or levels were altered by the recovery.

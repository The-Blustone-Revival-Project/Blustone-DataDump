# CB0101 outcome and scene identity limits

2026-10-05. Read-only retained ghidra-episode-decomp-02.txt and original ELF.
No device, Ghidra, account reads/writes, patch, grant or outcome assignment.
G addresses are Ghidra; vptrs explicitly use ELF coordinates.

**CSRSceneMEpisode.OnFinish Gb24f40** receives an outcome byte. It keeps it
for branching, releases game resources and chooses the following dialogue:

- param0: initially COMBAT+54 (lose_dialog2), then inspects nonempty
  COMBAT+48 (lose_dialog). IsFirstAction109ce44 is called atb25074 with
  that dialogue ID. When it returns1, the selected dialogue becomes+48 and
  PutFirstAction109cd90 is called with the same ID atb250a4.
- param1: selects COMBAT+3c (win_dialog). No corresponding first-action write
  appears in this winning branch.

PutFirstAction uses exact local namespace **/FIRST_ACTION**
(LDR109cdb4/ADD109cdbc), supplied dialogue ID as key, and RMGetTime109cdc2
converted to a string109cdcc as value, written by CGMLevelDB.Put794c90
at109cdd8. No timestamp units are assigned here.

CB0101's original win_dialog/lose_dialog/lose_dialog2 all equal **EP_0302B**.
Consequently the common dialogue, episode_clear command, server Read/Clear
encoded IDs and subsequent Story03 selection cannot distinguish victory/loss.
Current backend journals have Episode read/clear/reward flags, not the native
OnFinish byte. No durable winner-byte write was identified in the inspected
OnFinish path. Merely completing dialogue is not proof of winning this fight.

A controlled before/after local FIRST_ACTION/EP_0302B timestamp could support
a first-loss interpretation if newly written during this battle and its source
is exclusive. Current presence alone could be preexisting; absence alone does
not prove victory. This lane did not inspect any local journal or establish
exclusive writers, so retrospective outcome remains unproved.

## Future bounded scene/modal observation

Actual **CSRSceneMEpisode primary vptr is ELF215352c** (_ZTV at2153524,
offset-to-top0, RTTI16CSRSceneMEpisode). Constructor Gb23c14 calls base9c1038,
loads the exact table through LDRb23c1c/ADDb23c1e and writes table+8 to
the unchanged primary this atb23c30. Secondary addresses also written at+78
must not be accepted as primary scene roots.

OnFinish can **push a CSRPopUpDlg modal** (retained decomp line1063) while
the current scene remains Episode. Original CSRPopUpDlg primary vptr is
**ELF216cdc8** (_ZTV216cdc0); constructor Gdd56cc loads the vtable GOT
through LDRdd56fa/ADDdd5708, adds8 atdd5726, writes this[0] atdd572e.
Thus Episode's primary vptr alone cannot distinguish active combat from
post-combat dialogue. Future read-only observation requires separately guarded
current-scene and modal ownership plus proved state fields; this report adds
no observer implementation or native handler calls.

## 2026-10-07: original terminal arbiter and bounded read-only guard

Read-only follow-up from AGENTS §150. No adb, BlueStacks, Ghidra, server
source, original-file modification, private account body export, client patch,
stat tuning or grants. This section supersedes the earlier missing runtime
outcome discriminator, while leaving the historical battle outcome unknown.

### First establish the story identity

Original `analysis/recovered-reference/EPISODE_S01.json:44-82` binds **CB0101
to E01_S02**, entrypoint EP_0302A, battle true. **E01_S03 uses EP_0303A and
battle false**. A next Story03 selection is therefore not a CB0101 retry.
`analysis/testing/episode-010/report.md:49-78` documents the earlier burst
crossing the fight/dialogue boundary and selecting Story03; that report does
not establish victory. Match the current original combat ID before treating
any live Episode scene as the CB0101 fight.

### Winning and losing continuations are exactly identical for CB0101

The shipped descriptor `EPISODE_COMBAT_CB0101.json:9-11` assigns EP_0302B to
win_dialog, lose_dialog and lose_dialog2. The retained OnFinish body
`analysis/ghidra-episode-decomp-02.txt:780-1101` proves outcome0 chooses
lose/lose2 and outcome1 chooses win; both converge on PutDialogID/PushDlg.
This is actual native branch convergence, not an interpretation of dialogue.

Fresh bounded read-only decode of original
`recovered-assets/phone-2026-09-18/extracted/split_PADResource/assets/DIAL-EN.jet`
at header2430912, body2430936, packed1418 proves the shared continuation has
7 DialogEntry nodes. Its terminal UserScript is:

```text
episode_clear
scr-fade duration:0.6 color:(0,0,0,255)
wait duration:0.6
ctrl-scene-back cnt:2
```

Inflated RW payload length11830, SHA256
`3a9dde308b4a310b663f1b79866579f889d67389748d779d95402cb8eafd453c`.
No dialogue text or private account body was exported. Consequently an
E01_S02 clear, the next-story unlock, the shared spoken lines and the return
to the chapter list prove continuation/progression, never which side won.

The exact clear ACK is **/episode/Read with unprefixed id E01_S02**, not an
Episode combat completion endpoint or /mission/Complete. RequestClear
Gb19710 delegates unchanged ID to RequestReadOrClear; RequestRead Gb19638
prepends r_. The native continuation Gb20000 accepts GetResultCode1,
inserts the captured ID and parses ret_data achievement receipt. Optimistic
InsertReadOrClearID already occurs before HTTP. See retained
`ghidra-episode-progression.txt`, `ghidra-episode-progression-keys.txt` and
`research/episode-progression-contract.md:7-25`. A successful ACK establishes
durable story-clear handling, independently of combat win/loss.

### The original arbiter supplies a trustworthy outcome discriminator

All G addresses here are Ghidra coordinates; **ELF=G-0x10000**. Fresh Thumb
inspection used the original `analysis/extracted/lib/armeabi-v7a/libnative_core.so`
with ELF32 PT_LOAD translation, never flat file offsets for relocated data.
The RW segment has vaddr/file-offset difference0x1000. An initial flat-offset
trial produced unrelated instructions and was discarded; only the corrected
segment-aware results below are used.

`CSRGameBase::OnProcLoopBackExiting` G9d0ad8, retained
`analysis/ghidra-complete-10-onprocexit.txt:1-109`, freshly corroborates:

```text
G9d0b98 ldr.w r1,[r0,#0x2e4]
G9d0b9c cmp r1,#0
G9d0b9e it ne
G9d0ba0 movne r1,#1
G9d0bb4 beq.w G9e4a88             ; ProcessFinish(this,leftRemain!=0)
```

ProcessFinish G9e4a88 invokes primary-vtable+0x38 with that byte
(`ghidra-complete-01-finish-decomp.txt:1-41`). Exact Episode primary ELF
vptr215352c has slot+0x38 word **ELFb14f41**, Thumb G**b24f40**, the inspected
CSRSceneMEpisode.OnFinish. This closes the shared arbiter→Episode override
link. OnProcLoopBackExiting defers/requeues while pause+140 is nonzero without
bit0x10; do not force it past that original gate.

`OnProcDeadGroup` G9cf6fc writes signed32 **game+2e4=left.remain** and
**game+2e8=right.remain** from the local native protocol. On first terminal
update (old leftRemain==-1 and either new remain==0), it caches float totals
leftHP+30c/max+310 and rightHP+314/max+318, then sends local protocol0x2a.
Sources: `ghidra-complete-12-dead-deadgroup.txt:1-94`,
`ghidra-complete-53-insn-deadgroup.txt`,
`ghidra-complete-22-insn-parsegroup.txt`,
`ghidra-complete-51-proto-tbl.txt`. G9d2c00 IsExiting independently returns
leftRemain==0 || rightRemain==0
(`ghidra-complete-13-resultanimend.txt:303-323`).

Therefore for the exact owned current CB0101 object:

- **leftRemain>0, rightRemain==0** is the original terminal winning condition.
- **leftRemain==0** is the original terminal losing condition, including both0.
- **-1** is an initialization sentinel; never normalize it to a live win.
- Neither side0 means the native terminal discriminator has not fired.

Use native `remain` literally as the engine's camp bookkeeping. Historical
`research/battle-completion.md` prose contradicts itself about live/dead group
counts and +270; its nickname "living actors" is unnecessary to this proof.
The exact arbiter comparison and JSON field stores are unambiguous.

### Actor death evidence and attack guards

Fresh original Thumb proves `CSRGameActorBaseDraw::GetHP` G99abd6 simply
loads **actor+8b0**. `IsDead` G99aba0 loads the same FLOAT and returns1 only
for **exact HP==0.0**, not HP<=0; do not replace native semantics with a guess.
This is independent of the textual HP label or disappearing artwork.
Original names/addresses appear in `analysis/native-evidence.tsv:10857-10862`.
HP0 of the exact right actor supports actor defeat, but the camp terminal
snapshot and continuation are needed to prove battle completion.

An Episode-specific observer must validate current scene ownership and both
shared_ptr links, not scan memory for a matching vptr. Retained
`ghidra-episode-decomp-06.txt:277-315` proves CSRSceneGame mode7 constructs
CSRSceneMEpisode and stores its owned pointer/control at scene+658/+65c.
Known original primary scene vptr ELF216f90c is CSRSceneGame; the owned game's
primary vptr must equal **ELF215352c**, distinct from any secondary +78 view.
Existing `tools/InspectNativeInput.java:385-410` deliberately accepts only its
listed ordinary/tutorial classes, so it currently excludes Episode. Its
scene/actor/map traversal is evidence for a possible read-only extension,
not authorization to weaken its class guard or a claim that Episode is covered.

For each bounded input batch, recheck owner identities, original combat ID,
no active modal, pause+140/state+13c/catch+198, finite HP, camp remain fields
and the expected live HUD. **Either camp0 or a dialog modal must stop attacks
immediately**, even though the owned Episode game remains allocated.
CSRPopUpDlg primary ELF216cdc8 is already proved above. Common state bits
0x14 suppress attack input; their full enum names remain unknown
(`research/stage3-input-gate.md:35-55`). Primary Episode vptr alone never
authorizes input because OnFinish pushes dialogue without changing that owner.
No observer or burst was implemented/run in this lane.

### Remaining narrow ownership targets

The terminal arbitration is now recovered; no new Ghidra dump is needed to
guess an outcome. Fresh original **CSRMEpisode.GetCombat Gb17712** begins
`ldrd r2,r1,[r1,#0x24]`, returns that owned shared pair and increments control
owners at+4. Thus singleton+24/+28 is exactly currentCombat pointer/control.
Retained **COMBAT constructor Gb13fe0** reads `id` at Gb1405e/Gb14062 and
stores its parsed basic_string at **COMBAT+0** (pointer+8 for long strings).
Sources: `ghidra-episode-combat-actors.txt:92-122` and
`ghidra-episode-combat-actors-keys.txt:1-3`, corroborating LoadCombat
`ghidra-episode-first-combat.txt`. Do not confuse COMBAT+24 (game_res_id99)
with singleton+24 (currentCombat pointer). A guard may decode only this
bounded original ID and require CB0101; singleton owner/root itself still
needs exact ownership proof before accessing it live.
For right-actor identity/camp ownership, reuse the original guarded group
map+33c/count+340 only after proving the Episode actor vptr/control and the
actor camp/accessors. Existing actor HP accessor is ready; exact Episode
group membership is not newly runtime-verified here. Prompt normal attacks
must remain continuous enough to fight, with finite batches that stop at
these proved terminal/modal boundaries.

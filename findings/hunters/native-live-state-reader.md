# Read-only live native game pointer chain

2026-10-03. Offline original-library inspection only. This report identifies
addresses and offsets for a bounded in-process diagnostic reader; it does not
execute Java/JDI, adb, memory reads/writes, hooks or native function calls.
Dynamic symbol values below are **ELF virtual addresses**, not file offsets.

## 1. Proven app -> manager -> scene -> game chain

Let B be the correctly determined runtime ELF load bias. Read unsigned32
little-endian pointers:

```text
app     = read_u32(B + 0x21ef1e0)      // exported g_pApp
manager = read_u32(app + 0x08)         // CSRSceneMgr
scene   = read_u32(manager + 0x34)     // current owned CSRScene pointer
game    = read_u32(scene + 0x658)      // ONLY if scene vtable proves CSRSceneGame
mode    = read_u32(scene + 0x660)      // same class guard
```

Evidence:

- ELF .dynsym exports `g_pApp`, VA0x21ef1e0,size4,BSS section25.
- `CSRApp::Init(char*,char*)` uses this in r11; allocates/constructs
  CSRSceneMgr at `0x858b44` and stores it at **app+8** at `0x858b48`.
- `CSRSceneMgr::RefreshAll` reads manager+0x34 at `0xeb1fcc` and calls
  CSRScene::IsEnd; `MoveScene` reads the same pointer at `0xeb2186` and calls
  CSRScene::GetNextScene. ApplyScene owns/destroys its shared pointer pair
  manager+0x34/+0x38 and clears it at `0xea66b6`. This is not a guessed
  nearest-symbol or scene-history address.
- `CSRSceneGame` constructor (`0xe3c814`) clears game pointer+0x658, shared
  control block+0x65c and stores mode+0x660 at `0xe3c838`.
- Its OnInit factory stores constructed game pointer at+0x658 on every arm;
  `OnRefresh` directly loads+0x658 at `0xe3d02c`.

**Manager+0x44 is a list of scene TYPE history values, not scene pointers.**
PushScene (`0xea65c8`) allocates12-byte nodes and writes an enum at node+8;
the list sentinel is manager+0x44, size+0x4c. Do not follow node+8 as an object.

## 2. Exact vtable guards, from ELF symbols and constructor stores

The following .dynsym values were parsed directly from the ELF section tables:

```text
_ZTV6CSRApp                    VA0x2140ca8 size0x3c
_ZTV11CSRSceneMgr              VA0x217359c size0x2c
_ZTV12CSRSceneGame             VA0x216f904 size0x88
_ZTV9CSRMStage                 VA0x2153f7c size0xdc
_ZTV22CSRTutorialMStageSkill    VA0x2179240 size0xdc
_ZTV23CSRTutorialSupportSkill  VA0x217abfc size0xd8
```

Primary object vptr is symbolVA+8, after the Itanium offset-to-top/typeinfo
header. This is explicitly corroborated by constructor instructions:

- CSRSceneGame `0xe3c832 adds r1,#8`, `0xe3c83c str r1,[this]`.
- CSRMStage `0xb33cbe adds r1,#8`, `0xb33cc4 str r1,[this]`.
- CSRSceneMgr `0x85a154 adds r0,#8`, `0x85a15e str r0,[this]`.

Therefore validate:

```text
read_u32(manager) == B+0x21735a4
read_u32(scene)   == B+0x216f90c    // before reading game/mode fields
```

Then distinguish game objects by primary vptr:

```text
B+0x2153f84 -> CSRMStage
B+0x2179248 -> CSRTutorialMStageSkill
B+0x217ac04 -> CSRTutorialSupportSkill
```

Do not treat an arbitrary mapped pointer with a nearby symbol as one of these
classes. Null or a different scene vtable means this chain is not currently a
CSRSceneGame; return an unavailable/class-mismatch result and do not read its
game offsets. Scene transitions can invalidate the chain between reads.

## 3. Factory modes, correcting the support-mode hypothesis

CSRSceneGame::OnInit (`0xe3c9a8`) branches on mode using a9-entry Thumb table:

```text
mode5 ->0xe3cc7c -> factory0xe3d47c -> MStageSkill
mode6 ->0xe3ccf0 -> factory0xe3d354 -> TutorialPrologue
mode7 ->0xe3cd5a -> factory0xe3da44 -> MEpisode
mode8 ->0xe3cddc -> factory0xe3d5a4 -> SupportSkill
```

**SupportSkill is mode8, not mode6.** A runtime mode8 plus exact SupportSkill
vptr supports investigation of its PauseAttack calls at0xf1043a/0xf104a4.
Padlocked UI alone does not prove mode8. Default ordinary factory path creates
CSRMStage at0xe3ca96.

## 4. Bounded input diagnostic fields

After successful scene/game guards, record only these native state facts:

```text
game+0x140 u32: pause mask
game+0x13c u8:  state flags (ordinary press suppresses mask0x14)
game+0x198 u32: catch/exchange pointer
game+0x17c:    std::list input-actor sentinel
game+0x180 u32: first input-actor list node
game+0x184 u32: list count (layout inference, cap traversal independently)
```

The list traversal itself is proven by OnInputProcDash (`0x9d2f68`): sentinel
game+0x17c, first pointer game+0x180, next node+4, actor shared pointer node+8,
control block node+0xc. Stop at sentinel, null, cycle, invalid mapping, or a
small fixed cap such as8; do not trust an arbitrary list size for allocation.

For each validated actor pointer, read:

```text
actor+0xa6c u32: input/UI binding (IsInputable is pointer!=0)
actor+0x228 f32: actor clock
actor+0xa68 f32: last attack timestamp
actor+0x8b4 u32: default ACTOR_STAT
actor+0x8bc u32: buff ACTOR_STATE
default+0x3c f32: base attack interval
buff+0x3c f32: interval multiplier
buff+0x94 i32: stun counter
buff+0x98 i32: hold-attack counter
```

These correspond exactly to the predicates in stage3-input-gate.md. Do not
dereference default/buff pointers unless their bounded ranges are mapped and
readable. Report raw values and computed predicates, not guessed named states.
Actor primary-vptr allowlist, recovered from .dynsym and vtable headers:

```text
B+0x214a3fc -> CSRGameActorHunter
B+0x214a638 -> CSRGameActorMob
B+0x21494cc -> CSRGameActor base (allow only if intentionally supporting it)
```

Exact symbolVA/header evidence:

```text
_ZTV18CSRGameActorHunter VA0x214a3f4 header[0,0x214a4c0]
_ZTI18CSRGameActorHunter VA0x214a4c0
_ZTV15CSRGameActorMob    VA0x214a630 header[0,0x214a6fc]
_ZTI15CSRGameActorMob    VA0x214a6fc
_ZTV12CSRGameActor       VA0x21494c4 header[0,0x2149590]
_ZTI12CSRGameActor       VA0x2149590
```

The zero header is offset-to-top, the second word matches the **exact named
RTTI object**, establishing the primary address point+8 rather than a guessed
interior vtable address. CSRGameActor constructor additionally executes
`adds r1,#8` at0x97b5c2 and stores it at this+0 at0x97b5d2. No nearest-symbol
comparison is used. Reject other actor primary vptrs before reading+0xa6c.
If checking the runtime header too, vptr-4 should equal B+the corresponding
RTTI VA (subject to mapped-range verification); never call an unknown vtable.

## 5. Reader restrictions and load bias

Use mapped-range checks, fixed-size reads and unsigned32 pointer conversion;
no mutation, function execution or hooking is needed for these observations.
Read the app/manager/scene/game pointers and vptrs again after the snapshot;
if they changed, discard it as a transition rather than combine old/new objects.
Holding strong native references was not authorized or required.

On-disk data VA translation differs from file offsets: ELF's second PT_LOAD
maps VA0x210e550 to file offset0x210d550. Runtime addresses are **B+ELF VA**;
do not subtract the on-disk0x1000 gap from runtime pointers. Ghidra code
addresses used elsewhere add0x10000 to ELF VA; the symbol list above already
uses ELF VA and must not receive that extra bias.

Whether Java RandomAccessFile can read these Houdini-mapped addresses through
/proc/self/mem is a runtime capability question, not established by this
offline report. On failure, return the limitation; do not substitute writes,
cross-process reads, arbitrary whole-memory dumps or an unsafe native call.

## 7. Bounded backend group Rage/SP reader (2026-10-04)

Continue only after the previously documented exact scene/game vptr guards.
CSRGameBase owns a native unordered map of shared CSRGameActorGroup values:

```text
map begins game+334
first node = u32(game+33c)
map count  = u32(game+340)
node next  = u32(node+0)          // null terminates this chain
node key   = std::string atnode+8
node group = u32(node+14)
node control = u32(node+18)
```

This is **not** the std::list layout used by the input actor reader: group nodes
use next+0 and value+14. StartGame9e5fcc reads first game+33c, advances by
node+0 at9e5fe6, copies node key+8 at9e5ff4 and loads node shared group+14/+18
at9e5ff8. OnDamange lookup of map game+334 returns the same node value
at9e0750. Bound traversal at32 nodes, stop on null, reject cycles and inconsistent
count/mapped ranges. Reject count>32 rather than silently traversing farther.

Before reading group offsets, require exact primary vptr:

```text
group.vptr == B+ELF2149f68
```

Exact dynsym _ZTV17CSRGameActorGroup is ELF2149f60,sizea8;
constructor9a2ce0 calls CMUpdatable.C1 then adds8 to its vtable symbol and
stores primary vptr at9a2d34. No guessed derived class or closest symbol guard.
Shared-control metadata is available for additional mapped/owners checks, but
this lane does not supply a separate control-vtable guard as a substitute for
that exact group primary identity.

Guarded fields:

```text
camp=u32(group+2d0)                  // GetCamp9a43ec
SP=f32(group+2bc)                    // GetSkillPoint9a43e6
rate=f32(group+2c0)                  // GetSkillRecoverySpd9a43e0
maxSP=f32(group+2c4)                 // GetSkillPointMax9a3256
clock=f32(group+228)
delta=f32(group+22c)
```

Camp0 is left/player in this mission path: OpenCamp passes TEAM_DIR0 to
MakeCamp at9d387a..7c; camp1 is the right/enemy arm. Print every guarded group
with its key+camp rather than assuming the first hash-map node is the player.
If multiple camp0 groups exist, match the actual guarded Hunter's group id.
Actor.GetGroupID99b348 returns its **CMHashID at actor+898**, whose first
12 bytes are the std::string group id; its hash follows separately. OnDamange
gets that id and finds map game+334 at9e0720..738. Compare exact key bytes,
not pointers or a guessed literal such asP0. Actor.GetCamp986658 reads+988.

std::string decoding at node+8 or actor+898 uses the existing bounded form:
low-bit0 =>short length(byte>>1), text+1; low-bit1 =>uint32 length+4, pointer+8.
Keep key bytes bounded (e.g.32), mapped and output only these nonsecret game ids.

Clock/delta are proven common CMUpdatable fields, not inferred from actor-name
similarity. CMUpdatable::Refresh7862e4 writes delta+22c at7864a0, then loads
clock+228 and adds that delta at7864ac..b8. Group constructor derives directly
from this base. Group.OnRefresh9a5760 additionally uses exactly delta+22c
and SP/rate/max fields for regeneration. These are active native game clock
values; they do not establish current LEVELING chunk or .21 rate beforehand.

A useful snapshot line isgroup key,camp,SP,rate,maxSP,clock,delta. Preserve raw
finite float values and flag implausible/nonfinite data; do not mutate SP or
call a getter to normalize it. This reads the authoritative backend group
counter, not a potentially delayed UI meter mirror.

## 8. Bounded Supply table discriminator (2026-10-04)

`InspectNativeInput 8701 --supply` reads native activity reference and instance
vectors without invoking C++ functions or mutating state. It targets only the
instrumented Activity, inherits mapped-range/bounded string/RAF lifetime guards,
and checks the exact DataMgr weak-control vptr and owner count before reads.

Derivation, all source addresses below are Ghidra (subtract10000 for ELF):

- `CSRDataMgr::get`8b3390 calls its singleton template8b33f4. Literal slot8b3558
  contains19091d0; addPC8b3420 gives GOT21bc5f0, whose word points21e034c.
  Runtime weak holder is therefore B+ELF21d034c, with object/control at0/+4.
- Pool Alloc8b5dc0 creates0xa860-byte DataMgr and16-byte shared control;
  control+c is the DataMgr object. Its vptr is word(GOT21bc610)+8:
  GOT word21535c4 -> G21535cc -> runtime B+ELF21435cc. Signed control+4
  must be nonnegative and object link must match the weak holder.
- GetReferenceData8b26b4 reads level=u32(DataMgr+a858), ref=u32(level).
  GetPlayData8b26c4 reads play=u32(level+8).
- GetActivitySupplyCntde4a5e/GetActivitySupplyde4a72 read ref+2c0/+2c4,
  stride58. Records contain id/start/end strings at0/c/18 and AP24.
- ParseSupplyInfo stores the instance vector at play+318/+31c, stride10;
  string id at0, numeric status+c.

Traversal rejects negative/nondivisible sizes or count>32. Every read is bounded
by a readable mapping. Holder/owners/level/ref/play pointers and both vector
headers are rechecked before accepting output. It prints only those proven
nonsecret game fields. An empty vector is evidence of absent registration at
that sample; HTTP delivery alone does not prove registration. Nonempty matching
vectors shift the next check to Fuel InitCell's optional PA_CELL0 container.
The helper does not inspect general account data or normalize missing records.

Curated proof: ghidra-supply-reader-roots/root-insn/owner/literals/got/control.txt;
ghidra-supply-live-empty.txt; ghidra-supply-parent-insn.txt. Java compilation
passed; first runtime Supply snapshot is pending with tester. No APK changes.

## Selected combat tuning, 2026-10-08

`InspectNativeInput 8701 --combat-tuning --frame` uses the original render
callback and sends no diagnostic touch. It guards the existing DataMgr owner,
then selected LevelData pair at+a850/a854. Accepted control primary addresses
are ELF2143558 (separate pointer at+c) and ELF2143530 (embedded object at+c),
with nonexpired shared ownership and repeated registration/value checks.
Unknown ownership refuses before reading tuning. It prints only the selected
atk_spd_bonus at+254; current registration alone does not establish a battle
or resource-chunk association. See `hunter-native-stat-growth.md` for original
constructor/destructor/parser evidence and the successful Village snapshot.

# Stage enemy percentages and monster hp_page

2026-10-03. Read-only original native-library inspection with Capstone and
existing full instruction/decompile dumps. No Ghidra, adb, server/client edits.
Addresses are Ghidra=ELF+0x10000.

## 1. Stage fields are percentages: 100 is neutral

**[RECOVERED]** `CSRGameStage::SetStage` (`0xa274d0`) parses integer
`enemy_atk_per` and `enemy_hp_per`. Its scratch INFO starts at **sp+0x80**;
attack percentage is stored at sp+0x90 (`0xa277ea`) -> **INFO+0x10**;
health percentage at sp+0x94 (`0xa27862`) -> **INFO+0x14**.
The field literals are independently pinned in ghidra-setstage-exact.txt:
attack at `0xa2779a`, health at `0xa277e8`.

The mission actor construction's arithmetic is documented in
`analysis/ghidra-camp-02-insn-full-makestageinst.txt`:

```text
00b3402c GetStageData(stage_id)
00b34030 str stageINFO,[sp,#0x24]
00b340de ldr r6,[stageINFO,#0x10]     // enemy_atk_per
00b34216 str r6,[sp,#0x18]
00b34b2c ldr r0,[sp,#0x18]
00b34b2e vldr s16,[pc,#-0x9c]        // literal100.0 at0xb34a94
00b34b3a vcvt.f32.s32 s0,s0
00b34b56 vdiv.f32 s18,s0,s16         // atk_percentage /100
...
00b34ce2 vldr s0,[sp,#0x48]          // ACTOR_INFO attack bonus
00b34ce8 vmul.f32 s0,s18,s0
00b34cf0 vstr s0,[sp,#0x48]
00b34cf4 vldr s0,[stageINFO,#0x14]    // enemy_hp_per
00b34cf8 vcvt.f32.s32 s0,s0
00b34cfc vdiv.f32 s0,s0,s16          // hp_percentage /100
00b34d00 vmul.f32 s0,s2,s0
00b34d04 vstr s0,[sp,#0x50]          // ACTOR_INFO health bonus
```

The literal's original bytes at `0xb34a94` are `0000c842`, float **100.0**.
ACTOR_INFO starts at sp+0x48, so those two bonus members are object+0 and+8.
The stage values are multiplied into any existing level/role bonuses; they do
not replace other tuning.

**[RECOVERED] backend use:** `CSRGameActorMob::MakeBackEndActor`
(`0x9afd58`) applies:

```text
009b0246 vldr s0,[ACTOR_INFO,#0]
009b024e vmul.f32 s0,s0,defaultAttack
009b025e vstr s0,[ACTOR_STAT,#0x38]
009b026e vldr s0,[ACTOR_INFO,#8]
009b0272 vmul.f32 s0,s0,defaultHealth
009b0276 vstr s0,[ACTOR_STAT,#0x28]
```

Default attack and health come from the monster reference copied by
GetMonsterData earlier in the same method. Existing decompile corroboration:
`ghidra-enemycamp-decomp-03.txt:10058-10060` multiplies param+0 into attack
member+0x38 and param+8 into health member+0x28.

Therefore **enemy_atk_per100 / enemy_hp_per100 are neutral stage multipliers**.
Changing them to1 would apply **1%**, not repair a supposed100x multiplier.
The observed HUD100x100 must be explained separately.

## 2. hp_page is separate metadata, not in GetHPMax multiplication

**[RECOVERED]** AddMonster indexes hp_page at `0xa0bb4c`, scalar-converts it,
and stores the result at scratch sp+0x21c (`0xa0bbb8`). The backend copies the
monster INFO (`0x9afde0`) and, when ACTOR_INFO+0x4c is nonzero, stores the
copied hp_page into a byte **ACTOR_STAT+0x8c** at `0x9afeb2`. That branch
also stores ACTOR_INFO+0x4c at stat+0x90 and sets flag1. When it is zero the
backend instead sets special flag4 and does not make the page assignment on
this branch. Mission fills ACTOR_INFO+0x4c from wave-record+0xc (group) at
`0xb34d08..0xb34d0c`.

`CSRGameActorBaseDraw::GetHPPage` (`0x99b392`) returns precisely the byte
from default ACTOR_STAT+0x8c. A direct-call scan found its call at `0x9d5b88`,
which serializes the value into the game's actor status JSON. This is consistent
with page-count display; the exact HUD formatter was not audited here.

**[RECOVERED]** `GetHPMax` (`0x99abea`) does:

```text
default_stat = this->0x8b4
buff_stat    = this->0x8bc
return default_stat.hp(+0x28) * buff_stat.hp(+0x28)
```

Its instruction body `0x99abf2..0x99abfe` contains one multiplication and no
page-field access. Live health is independently this+0x8b0. `Damage`
(`0x99a9b4`) subtracts from that live value (`0x99aa92`) and clamps/writes
it (`0x99aaf6`); no hp_page access appears in this function. `IsDead`
(`0x99aba0`) simply compares live health to0. Thus these inspected core functions
**do not multiply true maximum HP by hp_page**. This does not exclude page resets
or other lifecycle behavior in callers/event subscribers.

**[UNRESOLVED]** The current fixture hp100/hp_page100 is consistent with a HUD
presentation such as100x100. Neither the exact formatter nor page-count/death
semantics are proved. Changing hp_page to1 would be a local diagnostic fixture,
not a recovered original value or a proved100x combat health nerf.

### 2026-10-05 reconciliation with the historical 777 probe

Original-library Thumb disassembly confirms `0x9afeb2: strb.w r0,[r2,#0x8c]`
and `0x99b396: ldrb r0,[r0,#0x8c]`. This is an unsigned byte narrowing:
hp_page100 remains100, but hp_page777 becomes9 (`777 & 255`). The historical
`in-game-stats.md` probe changed hp/atk/def/hp_page together and observed x10.
Its old rejection of hp_page merely because the screen did not show777 is
therefore invalid. x10 could involve a downstream transformation of9, but no
specific transformation is established; baseline x100 also rules out simply
asserting that every displayed multiplier equals stored page byte plus1.

The historical hp100→250 and `enemy_total_hp_max`100→250 observations remain
consistent with GetHPMax's separate HP field. They do not isolate hp_page's
role. A new loss where attacks were sent only after Complete likewise does
not test that role. Stage enemy percentage100/100 remains neutral; it must
not be changed to1 to account for this unresolved display metadata.

No native battle control was performed in this lane. Confirm displayed HP,
damage progression, actual enemy defeat and mission clear before claiming a
balance result. Original monster HP/page distributions and original stage
percentage progressions remain unknown.

## 3. Deck follow-up limits

The deck capacity used by SaveEntry comes from handler+4. Its output array is
zero-filled to that capacity, then populated with selected nonempty instances.
**This research does not prove mission capacity5**: the lobby parser's five
inst_id fields establish its input schema, not every mode's selection capacity.
Accepting save lists of1..5 and padding lobby output with0 is a sensible local
compatibility policy pending native wire capture. Do not require exactly5
merely because ParseDeckSetting reads five fields.

The native training inactive-source filter checks persisted deck cases1,2,4,5
but omits3. **[UNKNOWN]** Case3's named mode and original consumption/removal
policy. Clearing references to a consumed instance from an unprotected case3
deck is local referential-integrity policy, not a recovered native rule. Keep
that distinction explicit and do not silently call3 a known mission mode.

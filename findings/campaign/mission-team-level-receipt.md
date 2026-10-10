# Mission Complete Team level is nested inside user.exp

2026-10-04. Existing mission callback decompile plus original read-only Thumb/PC-relative evidence and preserved selected UI copy. No source/Ghidra/adb/runtime changes. Code addresses are Ghidra coordinates.

## Exact parent — neither root level nor user.level

The actual final-APK callback consumes **ret_data.user.exp.level{prev,cur}**. It also consumes **ret_data.user.exp.max_ap{prev,cur}**. Earlier `battle-lifecycle.md` root-level interpretation and source comments describing both root/user aliases as necessary were unproved and are superseded by this register flow.

Proof:

```text
b42824  r0 = retained ret_data (stack+0x1c)
b42826  index key user (LDRb4281e/ADDb42822)
b4282c  r8 = returned user JSON pointer

b429b8  r0 = r8
b429ba  index key exp (LDRb429ae/ADDb429b2)
b429c0  r5 = returned user.exp JSON pointer

b42aae  r0 = r5
b42ab0  index key max_ap (LDRb42aa4/ADDb42aa8)

b42bfe  r0 = r5
b42c00  index key level (LDRb42bfa/ADDb42bfc)
b42c06  r4 = returned level JSON pointer
b42c0a  index prev using that level pointer
b42c56  r0 = r4
b42c58  index cur using that same level pointer
```

Exact literal slots: user0xb42a48; exp0xb42a5c; max_ap0xb42da8; level0xb42dc4; prev0xb42dc8; cur0xb42dcc. PC-relative matching resolves these keys independently of decompiler variable aliases. r5 stays the EXP object along successful parsing through max-AP marker handling; it is not reset to ret_data/user before level lookup.

Disassembling every halfword without following TBB jumps falsely printed `movs r5,r0` inside numeric jump-table bytes (e.g.0xb429d8/0xb42b2a). Those are **data**, not executed parent-pointer changes. Error path0xb42858 sets r5=response for retry handling and leaves the success parsing path; it does not change this proof.

A bounded offline control-flow walk from0xb429c0 through0xb42bfe, including all guarded numeric-tag3..7 switch targets, visited187 reachable instructions and found **only the initial MOVr5=r0** as an r5 write. Important special case: TBB0xb42a22 uses **[r2,r1]**, with table pointer0xb42a2c initialized by PC-aligned ADDW0xb42a1e; targets are0xb42a72/0xb42a92/0xb42a68/0xb42a68/0xb42a6c. Treating it as a PC-adjacent table falsely enters literal pools and invents r5 clobbers. The true control-flow proof independently preserves EXP as the level/max_ap parent for every accepted numeric conversion path.

## Correct receipt illustration and no extra reward

With published Team thresholds0/100, a genuine fixture EXP gain90→120 crosses level1→2:

```json
{
  "result_code":1,
  "ret_data":{
    "user":{
      "exp":{
        "prev":90,"cur":120,
        "level":{"prev":1,"cur":2},
        "max_ap":{"prev":50,"cur":50}
      }
    }
  }
}
```

This is only the relevant excerpt; other mandatory mission fields remain required. EXP/cap values are example fixtures, not performed actions. Compute previous/current levels by the recovered **ordered threshold-prefix count, minimum1** from GetUserLevel0x10a0916 over the actual published user rows, using pre/post game.exp. Current earned270→300 remains2→2 because the two-row curve caps2. Do not add EXP or manufacture level30.

Nested max_ap is distinct from ordinary user.max_ap in other endpoints. Callback conditionally reads exp.max_ap, stores cur into PlayData+0x13c and seeds markers **increase_ap.cur/prev** (literal pairs0xb42b76/0xb42b7a and0xb42bbc/0xb42bc0). If cap remains50, report50/50; don't fabricate an AP-cap increase or full refill. Any original level-up resource reward remains unknown server balance/policy.

Root ret_data.level and user.level are unused by this proved level branch; duplicating them with30 does not suppress a correctly nested1→2 flag or define native computed level. They can be retired after normal server/client control rather than treated as authoritative progression.

## Flag bit1 and actual popup dependency

The numeric level values are retained as previous at stack+0xe4 and current+0xe8. At **0xb42c9e..0xb42cac** callback compares them and ORs **0x02** into result flags at stack+0x178 if **prev!=cur**. It tests inequality, not strictly cur>prev; inconsistent rollback pairs can also produce the Level Up notice.

**CSRGameBase::PopUpNotices0x9d8408** tests bit1, clears0x02 at0x9d8430..34 and branches to **PopUpLevelUp0x9d8464** at0x9d8438. That method calls **CSRPopUpUserLevelUp make_shared0x9ef9c8**0x9d8480. Popup **Init0xd99f58** loads resource **SR_COMMON/3_UI_CM_GET/5_UI_CM_G_TU** at0xd9a052..0xd9a058 (original literal/loader evidence).

Preserved selected UI database copy contains **KO/SR_COMMON/3_UI_CM_GET/5_UI_CM_G_TU**,4047 bytes; EN record absent. Existing KO fallback means that absence alone does not justify aliases/rebuild. XML availability does **not** prove every referenced sprite/font/motion or popup data/marker consumer works in current runtime. Nested max_ap supplies the recovered increase_ap markers; PopUpLevelUp also consults mission_auto/is_first_clear for autoclose behavior. Those are existing native state inputs, not new fields to invent in the mission response.

No new source/client patch is proposed by this research agent. A real threshold-crossing native control should observe RESULT flag0x02, popup rendering/close/return, derived level2 and coherent group_exp on reload. Existing normal-stage controls rarely exercised this path because root/user level aliases were ignored and EXP nested level was absent. Keep original curve/resource-reward unknowns separate from the now exact parser parent.

## Source resolution review

Read-only current source confirms `team-level.ts` mirrors the exact native ordered threshold-prefix getter with minimum1. Mission Complete now places derived previous/current levels and unchanged max_ap pairs **inside user.exp**, with compatibility root aliases using the same derived levels. Stale/refused completions publish equal EXP/level pairs. Area availability uses teamLevel(game.exp), aligning with native gates instead of fixed30.

Reward logic remains the existing first-clear fixture30 Team EXP and hunter reward policy; no extra Team EXP, AP refill or max-AP increase was introduced by these receipt fields. Tests include EXP0/99/100/270 getter boundaries and normal isolated missions crossing1→2 with nested max_ap unchanged. Parent reports full suite/build passed; this agent reviewed source/tests without executing runtime controls. **No concrete new parser/source regression found.** Daemon still serves the earlier source until safe promotion; native popup rendering/close remains unverified.

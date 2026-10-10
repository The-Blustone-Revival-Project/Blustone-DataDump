# Gym Raise onboarding: exact request flag and native Clear pair

2026-10-04. Read-only original ELF/RTTI/Capstone and existing training/tutorial reports. No source/adb/Ghidra/client edits, material selection, recruitment, unlock or training execution by this agent. Tester owns the one authorized fresh donor control.

## Campaign gates remain distinct

StaticData.GetStageID TBB base0xf4282e maps both **GYM8** and **GYM_ACHIEVE16** to arm0xf4289c, whose matched literal is **n_01_07**. Reward activity unlock **REWARD_ACHIEVE44** separately maps0xf428f8 to **n_01_08**, then Village's OnInit callback checks actual stage8 achievement count and hides PA_ACTIVE if0. Finishing Gym Raise does not fabricate or replace stage8 achievement(s).

Do not clear type44 or grant stage8 stars to address onboarding. The legitimate path is completing the actual native guide, then winning/earning stage8 progress normally.

## Tutorial Raise sends is_tuto1 but uses the same server parser

True **CSRSyncCard::RequestLevelUp entry is0xf53698**. The earlier report's0xf53740 points inside it, not a separate API variant. It posts `/gym/LevelUp` with target_inst_id/source_inst_list/is_tuto and account fields. Numeric source list is JSON text; request is_tuto is string0/1. No nonce/t field is recovered.

Tutorial-specific flow at0xeebf74 calls that same function. r1=1 at0xeebf66 is stored into **stack+4** by STRD0xeebf6a, the boolean AAPCS argument. Its source vector is stack+0x1c and target uint64 is r2/r3. This is native **is_tuto1**. The ordinary TableLevelUp flow at0x10206f0 stores r4=0 in stack+4 (0x10206de/0x10206ec), hence **is_tuto0**.

Both paths use **ReqLevelUpCB0xf53f90**, which does not branch on is_tuto or parse a separate tutorial response. Therefore the existing recovered success shape remains:

```json
{
  "result_code": 1,
  "ret_data": {
    "user": {
      "gold": {"prev": 1000, "cur": 900},
      "deck": [{"type":1,"inst_id_1":2,"inst_id_2":4,
                "inst_id_3":1,"inst_id_4":5,"inst_id_5":0}]
    },
    "card": {
      "target_inst": {"inst_id":5,"exp":{"prev":30,"cur":130}},
      "removed_inst_list": [{"inst_id":6}]
    }
  }
}
```

Those are fixture/control example values, not a performed transaction or original balance. **LevelUp removals are inst_id objects**, unlike RankUp bare numeric IDs. User.deck is still required by the same parser; do not invent tutorial deck rearrangement or auto-consume a protected participant. Preserve all slots/leader/skills/locks except the explicitly consumed donor's ownership and any unprotected preset reference.

Original tutorial-specific gold/XP subsidy was not recovered. Server's100 gold/source and published contribution are explicit local fixtures; ignoring is_tuto for pricing does not violate a recovered callback shape but is not proof original tutorial economy matches ordinary Raise. Invalid flag values can be rejected locally; don't silently change material rules on flag1.

## Exact native completion pair and callback attribution

The tutorial-specific LEVEL_UP_PARAM callback's correct **Thumb entry0xeec070**, callable ELF0xedc071, is stored at hidden vtable **ELF0x21771e0 +0x20**. Vtable+4 points to typeinfo0x2177214; the RTTI name explicitly names the deeply nested **CSRSceneTutorialLevelUp::SetTutorialLevelUp** closure taking `CSRSyncCard::LEVEL_UP_PARAM const&`. Exact caller literal slot0xeec004/addPC0xeebf5e resolves this vtable and is passed to RequestLevelUp0xeebf74. This is not a nearby card-detail tutorial callback.

That callback executes:

```text
0xeec0c0  load SyncTutorial
0xeec0c8  r1=8  (GYM)
0xeec0ca  r2=1  (step1)
0xeec0ce  RequestClear(8,1,...), function0xf9a0c4
```

Expected native wire completion is therefore **/tuto/Clear {type:8,step:1}**, provided this actual tutorial subclass/closure was active. A generic ordinary Raise screen does not automatically become that guide merely because a source was fed. Observe the real request, acknowledge it using recovered Clear response `{type:8,step:1}`, persist/merge state3 through login/lobby; **do not preemptively write the flag**.

Important native sequencing: RequestClear is called **before** testing returned currentEXP at0xeec0e6..0xeec0ec. ReqLevelUpCB failure paths supply zeroed LEVEL_UP_PARAM; thus this native guide callback can attempt Clear even on a refused/zero result. A Clear8/1 packet alone is not proof successful Raise. Successful ownership/EXP/gold/source-removal mutations and callback UI result must be verified independently; never call the test complete from flag traffic alone.

No other Gym Clear pair is established by these inspected direct paths. Nearby Clear1/1 at0xeea15e belongs to the preceding card-detail workflow, and Clear3/0 at0xdba548 belongs to another Village guide branch; don't label either as Raise completion or sweep them into an invented Gym completion set.

## Safe donor control implications

The authorized target is owned Tyltyl5; existing1/2/4 are protected real party members and must remain gray/ineligible. A single newly recruited Tyltyl6, if native recruitment succeeds and backend owns it, can be unlocked through actual lock UI, remain outside leader/protected decks/active battle, and be selected as the **only** donor. The read-only research does not itself authorize additional recruits, arbitrary card changes or protected-source consumption.

Observe exact target_inst_id5/source_inst_list[6] on wire; flag1 indicates tutorial path, flag0 ordinary path. Compare gold debit100, target cumulative EXP gain from published donor curve, removal of6 only, maintained deck/leader and inventory/profile persistence. Then independently observe whether native emits Clear8/1 and whether guide resumes the intended stage route. The legitimate free-fuel footer still requires actual stage8 achievements after this onboarding step.

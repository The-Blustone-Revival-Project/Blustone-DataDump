# Four-card reference key/type audit

2026-10-04 urgent read-only check. Imported and JSON-serialized current server-ts bootstrap references in a standalone Node process; no server start, state-file access, adb/Ghidra/original changes. Inspected original-library SetCard's inline base parser. Systems owns map insertion/callers.

## Actual serialized structures

All four current rows001,002,003,004 have **exactly the same top-level key set**:

```text
base,thumb,id,ref_id,equipment,skill,dialog,stat
```

Each base has string **id,char_id,name,res_prefix** and numeric **is_main,attr,role,is_source,source_field,cool_time**. Every id remains its zero-padded string001..004; no Number conversion, missing id, undefined property or accidental C003 lookup id was observed.

Each stat array has five rows, ranks1..5,awk_step0. All have identical17keys: rank/awk_step numeric; hp,atk,def,spd,crt_chance,crt_dmg,penetration,block_chance,block_dec_dmg,attr_enhance,attr_resist,hp_regen,hp_up,atk_up,def_up strings.003/004 reuse001's exact stat values.002 only differs in its documented balance strings.

Each skill array contains exactlytypes1..5 and identical keys target_rank,type,name,desc,cut_in_id,icon_id,cool_time,cost,crt_chance,effect. Numeric/string types match across allrows; effects are empty arrays. Equipment anddialog arrays are empty on allfour.

003/004 differ from001 only in appropriate stringidentities/name/thumb/prefix and numeric role/attr/main flag. Their serialization does **not** introduce a third-record-only missing base/stat/skill property. Native attr2/role2 and attr1/role4 are recovered valid enum values.

## Exact native base read and one historical placement mismatch

The base parsing is **inline in CSRCardInfoContainer::SetCard0x87baa4** in this binary. No separately named SRSBASE_INFO::parse/AddBaseInfo symbol was found in the preserved symbol inventory; those names should not replace the verified operand flow.

- SetCard indexes ret_data at0x87baca, determinesarraycount, and numeric-indexes row at0x87bb6c.
- row retainedr5; row.base indexed0x87bb74 and saved **sp+0x2c**.
- base.id is indexed with that exact retainedbase: loadsp+0x2c0x87bc72, operator[]0x87bc74, stringconversion0x87bc84. Thus003's lookup identity is actually drawn from its **base.id string003**.
- Other inline base fields resolved in the actual parser: char_id0x87bcbe, name0x87bd16, attr0x87bdcc, role0x87be48, res_prefix0x87be9a, is_source0x87bee4, source_field0x87bf34. Current rows provide each, consistently typed.
- **is_main is read from ROW, not base.** At0x87bc1c `mov r0,r5` uses the fullrow, then0x87bc20 operator[]uses the is_main literal retainedsp+8. The returnedvalue is stored ascard-info flag at0x87bc6e. Current server putsis_main onlyinbase, so this historical field is ignored/default0 for **allfour**, including001. This is a placement discrepancy, **not evidence of the Nene-only null reference root cause**, since it predates003 and affects the working002 too.

The map construction/successful insertion, duplicate replacement and later reader lifetime are deliberately outside this lane. The current comparison finds **no evidence-backed new mandatory key** to add only to003/004. Guessing one would confound the failure investigation.

## Updated cache interpretation

Parent confirmed GetCard HTTP beforecrash (server.stdout115–120,22:32:12.716,17344plaintextbytes). Systems independently proved the local resource read **REFEN/reference/GetCard**, throughCMJetLoader::LoadStr0xf82c26. Both facts matter: a network request beingissued is not itself a measurement of which parsed JSON callback populated or last replaced the native map.

`card-reference-refresh.md` has been corrected: its earlier claim that no cache-read call existed was wrong. No GetRefVer handshake/numericversionfield is currently recovered. PreserveownedNeneinst4; no clear/regrant/versionguess.

Remaining discriminators: captureorcompare the actualserved4-row decrypted payload with this serializedstructure; ensure SetCard completedallfour registrationpasses and no latercallback replaced them; compareFindCardByID exact003 againstinsertedkeys. A parserexception/log marker or mapinsertiontrace is stronger than speculation about rank3orC003art because the measured IsTrainingCard crash dereferences the missing sharedCardInfo beforethose consumers.

# Search effect roots and one-wave incompatibility

**Latest control supersedes the early-tap explanation:** preserved restart PID3768 resumed log1, received Begin and reproduced the same assertion after12seconds with NO INPUT. The native mode4 automatic wave banner requests a name absent for the server's one-wave fixture; see the final addendum. Keep the historical touch-path evidence, but do not present waiting longer as a sufficient fix.

2026-10-05. Read-only original Thumb plus parent ShowEffect/InitEffect/caller dumps. No device/Ghidra/source/runtime writes and no assertion continuation. Parent reports accepted Begin, intro clouds/Arena backdrop without HUD, then an ordinary tap whose timestamp exactly matches ShowEffect's missing-map assertion.

## Exact input path

**CSRGameBase::OnProcessPress G9db1bc** first forwards the input to UI root (9db1f4), then applies pause/status/caught guards. With touchkind1, no caught actor and CatchActor returningfalse, it calls **CMRand(1,3) at9db252**, converts the chosen integer to text, and prefixes **EFT_TOUCH** (LDR9db262/slot9db360/ADD9db264, insert9bytes at9db26e). It calls **ShowEffect at9db2ca** with the resulting **EFT_TOUCH1/2/3** key. Only afterward does it call **OnInputProcDash at9db2f8**. Therefore an assertion here occurs before an attack is dispatched and cannot be described as combat defeat or an End response problem.

ShowEffect **G9db7b0** hashes its FIRST effect-name argument with CMHashID at9db7d2 and looks it up in game.effect map (header+1e8/root+1ec/count+1f0). This is the effect name, not the optional third pointer argument. On missing key it asserts, then its unchanged fallthrough dereferences the end node as an EFFECT_DRAW_PARAM. Advancing that assertion is not a supported recovery.

## Registration and readiness

**InitEffect G9c33c4** explicitly registers all three keys: EFT_TOUCH1 ADD9c5f8e, EFT_TOUCH2 ADD9c606a, EFT_TOUCH3 ADD9c6146. It gets CMComponentEffect bindings from UI nodes **TOUCH_EFFECT,APPEAR_EFFECT,DASH_EFFECT,CRASH_EFFECT,BOSS_EFFECT,DEATH_EFFECT,PRE_EFFECT,SKILL_EFFECT**, plus UI_ROOT/READY. Literal spelling is recovered, not inferred from screenshot art.

The only original direct InitEffect caller found in the scanned game text is **CSRGameBase::OnInit at9c1e22**. OnInit calls InitEffect immediately **before** its virtual slot+5c at9c1e2e (InitBeforeOpen in the existing class flow). Thus the earlier possible theory that InitBeforeOpen always runs before effect registration is contradicted by this order. A tap concurrent with or before completion of initialization remains a different possibility.

OnProcessPress has **no explicit effect-map/readiness check** before ShowEffect. It rejects a nonzero pause unlessbit0x10 is set (9db1f8..202), and blocks status bits0x14 (9db204..20c), but an intro state0 passes those checks. The parent's early intro/noHUD + exact tap/assert timing makes this input path substantially stronger than an automatically fired boss-effect guess. It does not prove the actual missing member's precise suffix or the reason initialization had not supplied it; a guest caller PC or bounded effect-map observation would close that gap.

## Separate Search boss effect

CSRFindShard::SetRightRunner G9080d4 checks IsBoss at9080fe; its boss branch requests **EF_CH** at90815c (LDR908146/slot9081f0/ADD90814c). InitEffect builds FX_CHANGE and unconditionally registers EF_CH at9c6236. This is a real independent callsite, but it does not explain the timestamp-correlated user tap by itself. Likewise common OnProcWaveChange and skill-effect callers should not be blamed without the requested key/caller evidence.

## Bounded next control

The current assertion remains stopped. After preserving the account and active Search attempt, a fresh native entry control should **wait for the actual battle HUD/ready state with no touch input** before one normal attack. This changes tester timing, not flags, effects, server outcomes or native code. It can distinguish early-input exposure from a persistent effect initialization failure; it does not guarantee the latter is absent. Active-attempt replay/capsule policy and normal helper availability must remain coherent across that restart.

If a read-only live probe is necessary, use the already proved scene/game pointer and exact class guards to inspect effect-map root/count (+1ec/+1f0), with bounded node-count verification and known key CRCs. No native calls, arbitrary text scan or memory writes are required. A zero map during intro would support incomplete initialization; a populated map without the expected keys requires further registration/class identity evidence.

Sources: ghidra-search-effect-root.txt/-keys.txt, ghidra-search-effect-callers.txt, original OnProcessPress9db1bc..9db364 and OnInit9c1820..9c1e30. Native Search battle/End is not verified by this stopped intro.

## No-input contradiction and exact automatic one-wave incompatibility

Parent's preserved restart **PID3768**, same active log1/no new charge/reward, reproduced SRGameBase2006 ShowEffect assertion after **12s with no input** (03:05:39.396+03). This falsifies early physical input as the sole cause. Current assertion remains stopped; no End/outcome is inferred.

Fresh **ghidra-search-game-init.txt** shows no normal early-return branch before InitEffect. OnInit selects **SR_INGAME/INGAME_MR only when game.MODE+2ec==2**, otherwise **SR_INGAME/INGAME_NM** (LDR9c1840/ADD184c and1842/1852); loads/getroot and establishes game+2c/+30. It requires UICamera/CMInputable with separate earlier assertions, then calls **InitEffect9c1e22 before virtualInitBeforeOpen9c1e2e**. UI lookup failure is not a benign early return silently skipping effects; no claim of that cause is supported by this decomp.

The relevant AUTOMATIC branch is **OnProcWaveChange**: **9ceaa2 compares game.MODE+2ec to4**. In that branch **9ceaa6 loads GROUP_DATA.current_wave+1c**, **9ceaaa loads max_wave+24**, **9ceab2 adds1 to current**, and **9ceab6 formats `IG_WAVE%d_%u`** (LDR9ceaae/slot9cedf4/ADD9ceab0). It then calls ShowEffect at**9ceb1a**. A one-wave initial group requests **IG_WAVE1_1**.

Search MODE4 is independently pinned: SceneGame.OnInit's TBH at **e3c9dc** dispatches mode−1; original halfword entry for4 targets**e3cbfa**, which calls **CSRFindShard.make_shared at e3cc1c**, passing the scene mode pointer. CSRGameBase constructor saves passed MODE at9c1044 and stores it into+2ec at9c138a. This is actual dispatch/field proof, not backdrop inference.

**InitEffect DOES NOT register any total1 wave banner.** The exact decomp loops build names using `IG_WAVE%s_%s`:

- Lines4106..4191: current1..2, constant total2.
- Lines4192..4277: current1..3, constant total3.
- Lines4278..end: current1..4, constant total4.

Therefore its registered families are **IG_WAVE1_2/2_2**, **1_3/2_3/3_3**, and **1_4/2_4/3_4/4_4**. The one-wave Search fixture inevitably requests an unregistered **IG_WAVE1_1** through this automatic path. This concrete content incompatibility fits the no-input assertion/noHUD. The actual guest assertion caller/name has not been captured, so it remains a strong instruction-backed explanation rather than a live caller-PC certification.

The compatible minimum is **two actual native monster-link waves**, with **two matching Begin wave_info rows**, both backed by already published monster/art/stat references and a Search stage/link. End should report max_wave2 and full victory cleared_wave2, according to the independently proved count semantics. Changing only max_wave in the End receipt cannot repair the initial group banner, since GROUP_DATA comes from actual native wave setup. Original Search balance/drop quantity remains unknown; two-wave content is a marked local reconstruction choice constrained by original UI support.

Prefer an isolated Search stage/link or explicitly scoped Search content so this repair does not accidentally alter campaign stages/stars/AP. Replaying the same accepted attempt must preserve capsule/log accounting, and a cold native cache must receive the coherent new wave definition. No effects suppression, new unsupported map aliases, fake End or assertion continuation is justified.

Other automatic literals recovered for discrimination: boss SetRightRunner EF_CH; OnProcBossAppear UI_IG_WAR (ADD9d07dc); another OnProcWaveChange path READY (ADD9ceca4) with sound IG_READY (ADD9cecac). These already have registered keys in InitEffect. The total1 dynamic banner is the specific uncovered key family.

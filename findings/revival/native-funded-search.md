# Earned-capsule Search and helper serial repair, 2026-10-05

Verified in the original native gameplay flow against the replica, instrumented
release +8, BlueStacks explicit serial127.0.0.1:5555. No client patch/rebuild,
install/clear, host grant, synthetic End, exit-door input or tutorial override.

## Earn and spend

Ordinary n_01_07 victory awarded AIRSHIP_TICKET instance7 qty1. Search showed
capsule1 and existing Sylvester trace1/10 (screens133/136). The first Begin
refused atomically because the native warm helper sent friend_leader_id18,
where our validator incorrectly required0. Known virtual helpers now accept
safe nonnegative serials with friend_pvid0; an empty helper still requires0.
The next accepted Begin created log2, onboarding:false, debited capsule1→0.

## Disproved cache-only hypothesis

That warm attempt had no enemies. CSRFindShard::MakeStageInst G90610c computes
its allocator from owned cards only (max17). For a zero virtual template it
writes max+1 (18) back into the GLOBAL template; a later match copies nonzero18
without incrementing its allocator. Its first enemy is then ALSO18. See
warm-cache.md for decomp locations. This is an actor identity collision.

The nonowned GetAbyss helper now uses reserved serial900000001. New attempts
reject overlap with owned IDs or the generated two-enemy serial window before
any debit or log mutation. Focused tests cover both collision forms atomically.
The pending log2 was preserved through server promotion and ordinary ref reload;
its already-funded resume returned no repeated consume_result.

## Actual native completion

PID16687 Begin at01:47:32Z sent friend_leader_id900000001. Screen151 shows
M001/HP100 at1/2 and all four party members plus helper. Two ordinary taps at
540,850 defeated both waves. End01:48:27.440Z sent log2, cleared_wave2,
clear1, atk_cnt2, atk_total362, dead_cnt0, enemy HP0/max200, playerHP4955/max5120.
HTTP200 returned accepted settlement. Screen155 displays Search Complete2/2,
Collected Items1, Sylvester Traces2/10. Its blank reward thumbnail remains a gap.

Persisted audit: activeSearch=null; last.log2 onboardingfalse capsule_inst7;
trace inst6 qty2; capsule inst7 qty0. Gold10660/TeamEXP360, CASE1[2,4,1,5,0]
and all owned hunters remain intact. Normal stage earning changed its hunter EXP
legitimately; Search settlement did not. Private snapshots stay under
recovered-assets/capsule-funded-search-2026-10-05, never checked in.
Okay/Close/Home returned to village; Daily Sign In popup safely closed via X.
Screen157 and live PID16687 confirm the safe endpoint with no active battle.

Capsule drop rate1, Search cost1, trace reward1, period/helper limits and stats
are LOCAL fixtures. No new tutorial37/1 clear ACK was observed. Ordinary repeated
Search after period expiry, Retry/Reset, trace exchange and dispatch still need
implementation/validation. Unit regression/build pass; broader suite passed
after the helper source fix earlier in this continuation.

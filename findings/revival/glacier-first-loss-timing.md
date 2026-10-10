# First Glacier loss: inputs followed completion

2026-10-05, instrumented +12, split24/1634666, unchanged party and stats.

The ordinary n_02_01 attempt is a real loss, but not an active-input combat
test. Replica response-dispatch Start was 16:04:38.174Z; persisted started_at
1791216278185. Complete reported clear/result/win0 at16:08:59.093Z. First
recorded attack DOWN was1791216678352, or16:11:18.352Z:400.167s after Start
and139.259s after the loss response. Eight attack DOWN/UP pairs followed.
They cannot establish attack damage or failure to defeat an enemy.

The 16:07:34 screenshot shows leader332 and upper bar100×100. The subsequent
screen says Unfortunate Loss. Neither the HUD suffix nor this timing establishes
excessive true enemy health. Existing stage-multipliers.md proves core GetHPMax,
Damage and IsDead do not multiply by hp_page; in-game-stats.md contains an
older probe contradicting a simple suffix interpretation. Keep these limits.

Persisted loss had AP49, gold10660, exp360, unchanged party[2,4,1,5,0], no
active battle, no n_02_01/n_02_03 stars, and empty Episode journals. The UI's
fuel-return text conflicts with the replica's charged AP; recover the original
refund conditions before implementing that separate behavior.

Evidence: analysis/testing/episode-009/glacier-earned/01-input-timing.json,
01-touch-proof.json,01-loss-state.json,01-active-combat.png and
01-after-attacks.png; bounded local server log's Start/Complete timestamps.
No credentials or private account fields are included here.

One same-party/stat retry with prompt ordinary attack input is authorized.
Actual victories must unlock subsequent Glacier nodes; no direct Complete,
exit-door forced victory, reward grant or manual star/unlock assignment.

## Prompt-input control succeeded

Same party/stats/+12/profile. Ordinary Retry returned to preparation; the
following presses there were not combat. One subsequent Begin Battle emitted
Start16:41:28.600Z. Prompt ordinary presses then produced native Complete
16:41:37.182Z: clear1, atk_cnt1, atk_total272, enemy_total_hp0/max100,
dead_cnt0, playerHP4110/max4110. Native clear_time0 is its reported active-play
value; it must not be substituted for the8.582s host request interval.

Parent visually inspected01-retry-active-after48.png: Victory, three stars,
Team Level2, four unchanged party members. Persisted n_02_01 has orders0,1,2,
stars3; gold10670/exp390. No exit-door input or stat change. True enemy health
100 and actual native attack damage272 establish that this unchanged fixture
can be defeated; HUD100×100 is not evidence of10000 true health here.
Subsequent ordinary n_02_02 Start16:42:03.497Z is a separate active attempt.

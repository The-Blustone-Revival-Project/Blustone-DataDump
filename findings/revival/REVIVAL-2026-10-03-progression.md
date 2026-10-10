# Genuine campaign flags and locks

The revival goal remains active; this checkpoint fixes native progression
encoding and credit behavior, not all game fidelity.

## Root cause and corrected contracts

Native ParseMissionInfo reads stage[].achieve as a string, then JSON-parses it.
Numeric0 becomes "0", iterates once and supplies missing order0: one false
star. The getter sums three byte flags with no minimum. Correct zero is string
"[]"; earned flags are stringified objects with order0/1/2. Historical1/2/3
included index3 outside the flag array and is superseded everywhere.

`research/stage-achievement-contract.md` pins parser bases, stores and getter.
Stored sparse conditions now retain identity, count mirror and replay credit.
First-clear economy pays once; improved conditions on replays do not repay.
Local default rules use completion, under60 seconds and <=1 death. Original
server rule configuration remains unknown; those rules follow visible default
captions. Missing hand-made metrics retain legacy all-stars fixtures.

Native area_achieve is separate: repeated {area_id,achieve_cnt:10|20|30} rows
for CLAIMED chests. Object keys and received[] are ignored. The old wire-map
claim was an inference from the internal map, now disproved. Projection is
fixed; area_progress is clearly separate local diagnostics. Existing payouts
and claim credits are retained.

## Native evidence

`testing/revival-004.md`: prior village50/150/every-area-open/per-nodeone star
became village7/150/Snowfield-only access/Snow1/30 after corrected responses.
An attempted locked RedRock entry was refused by native UI. Below-threshold
map entry emitted no chest request or reward popup.

Ordinary stage2 combat completed with one attack,181damage, enemyHP0/max100,
one-second clear and no deaths. Server granted safe0/1/2 flags and10gold.
Fresh reload preserved three stage2 stars: village10/150 and Snow4/30, later
areas still locked. Originals and party are intact.

The client automatically started stage3 tutorial after the result. Tester
stopped as instructed; the charged attempt is retained. On later relaunch it
returned to village without resuming stage3; no new BeginBattle, refund or
host-side completion occurred. Temporary forever retry control was restored
to normal30seconds. This auto-advance/tutorial behavior needs follow-up.

## Validation and limits

npm test/build pass. Checks cover serialized zero/sparse flags, bounds, partial
stars, replay improvement, no duplicated economy, last-stage area gate, legacy
credit and opt-in seed monotonicity. Claim tests now earn threshold credit
before asserting payout; multiple claimed rows and claim restart are covered.
Missing original XP/stat/reward values remain fixtures; active skills and map
art remain incomplete. Claimed-history sprites in locked areas were not tested.
The initial Received300 popup is not proof of a new actual payout by itself.
No APK modification/install was needed. Private backup is gitignored.

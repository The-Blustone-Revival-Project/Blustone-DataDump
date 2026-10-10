# Mixed-role party and ordinary-input victory

The broad revival goal remains active. This checkpoint improves character
fidelity, persistent team selection and real client combat, with limits below.

## Implemented and verified

- Lantern001 uses Bomber3/Fire1; Mowgli002 uses Offense1/Lightning3. Enum
  numbers are independently pinned by native localized description switches;
  character metadata is partly community-sourced, stats remain fixtures.
- `/world/SetDeck` persists owned formations with atomic batch validation.
  Native Build Team sends deck_info JSON text containing four ordered IDs.
  Lobby reads five separate slot fields; one-to-five inputs are padded to five.
  Save callback only checks success result code, not ret_data.
- Profiles now use the actual saved members and their reference/progression
  fields. Training protection covers saved cases1/2/4/5 and active combat IDs.
  Consumed IDs are cleared from unprotected presets rather than left dangling.
- New account default picks a frontliner before captain support. Explicitly
  saved formations are preserved; legacy missing-deck migration never restores
  already-consumed cards. Saved Bomber-only combat is unverified.

`testing/revival-003.md` captures native save `[2,1,0,0]`, cold reload retaining
that order, and five-field authenticated lobby confirmation. Locked original
Mowgli remains selectable for a party; locking protects consumption.

In screenshot12 Mowgli visibly fights on the ground with twin knives and
Lightning icon; captain/Lantern visibly occupies the airship with bomb icon
and1020HP. Following ordinary frontline tap/hold, screenshot13 shows enemy
absent, falling coins, Mowgli232HP and turn dial1. Screenshot14 shows Mowgli
Victory. **No exit-door input occurred.** This strongly supports enemy defeat
and ordinary combat completion, but the exact death frame was not sampled and
damage cannot be attributed specifically to the tap rather than ongoing auto.
Result and return to map succeeded. Original cards1/2 remain owned.

## Validation and open limits

npm test and npm run build pass. New meaningful checks cover saved/reloaded
ordered IDs, four/five slot conversion, flat profile consistency, actual
battle fallback participants, party source protection, whole-batch refusal,
fresh default formation and legacy consumed-card migration. Review found the
Bomber-only default risk; new defaults now include an available frontliner.

Native current-pid log has no captured assertion/abort/missing-reference;
result emitted SetClearRewardThumb NotFound. Stage map remains black, battle
environment remains generic fixture art, and seeded achievement/reward/fuel
presentation differences remain. Active skill effects, original balance,
other preset modes and all original progression are not established.

`research/stage-multipliers.md` proves stage100/100 is neutral100% scaling.
hp_page100 is separate metadata, not a demonstrated100x true-HP multiplier;
do not nerf percentage values to1 based on its visual label. Further status/UI
page semantics and combat timing need investigation.

No APK change or install was needed. Original phone/app/private snapshots were
not modified. A private pre-party backup is under gitignored server-ts/data.

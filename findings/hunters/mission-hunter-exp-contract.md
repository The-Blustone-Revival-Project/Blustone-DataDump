# Mission Complete: owned hunter EXP contract

2026-10-04. Read-only original decompile `native-mission-complete.txt`, original-library Capstone/literal checks, and current server review. No adb/Ghidra/source/client/original changes. Native addresses are Ghidra image coordinates (ELF VA is0x10000 less).

## Exact normal response shape

`CSRSyncMStage::ReqCompleteCB`0xb426ac consumes **ret_data.card as an object keyed by decimal owned instance serial**, with each entry directly containing previous/current **absolute cumulative hunter EXP**:

```json
{
  "result_code": 1,
  "ret_data": {
    "card": {
      "2": { "prev": 290, "cur": 300 },
      "1": { "prev": 100, "cur": 110 }
    }
  }
}
```

This excerpt only illustrates the hunter EXP addition to the existing complete response; the other mandatory Complete fields remain necessary. Numbers are local examples, not original reward amounts. There is **no intervening exp object**, no inst_id member needed, no per-hunter HP/level/rank member parsed by this branch, and no array of card-instance rows on the normal HTTP request path.

## Exact caller and lookup evidence

The success path indexes full JSON `ret_data` at0xb42744 (dump retains it as uVar7). Its pointer is saved at sp+0x1c. At0xb43048, r1 loads literal slot0xb4315c; matched addPC0xb4304a resolves0x1d6eed7 **card**.0xb4304c loads r0=sp+0x1c, indexes that parent at0xb4304e, and stores the resulting card container in **sl**0xb43052. This proves the card parent, not merely a nearby string.

Then0xb43054..0xb43060 calls GetPlayData/GetCurDeck, retaining the current deck vector in r8. It walks nonzero uint64 deck serials at fp:0xb43098..0xb430a0 skips0;0xb430a8 converts the actual serial to a decimal string at sp+0x68. For a nonnull CPVHTTPRequest pointer,0xb430b6..b8 selects keyed lookup. JSON object tag1 at0xb430c8..ce dispatches to0xb43188, which loads card's tree, finds the decimal string at0xb43190..92, and compares with its end iterator at0xb431d0..da.

**Missing serial key safely preserves current EXP**:0xb431dc..0xb43200 finds the current owned card;0xb4323a reads its EXP+0x20 and writes it into both result previous/current EXP slots at0xb4323c/+0xb43240. It does not call SetCardExp in that fallback. This explains why the current empty card object works without granting hunter experience.

When present,0xb4325c..60 calls `card[decimalString]`. Matched literal load0xb43264/add0xb43266 resolves **prev** at0x1d6ef5d, then indexing0xb43268. Later0xb433b6..ba indexes the same card/string pair; load0xb433be/add0xb433c0 resolves **cur** at0x1d6eea2, indexing0xb433c2. Both are scalar numeric conversions accepting string/bool/integer/unsigned/double tags; use nonnegative integral JSON numbers for faithful minimum and avoid default-zero conversion on malformed values.

Current EXP is stored in the result array, then0xb4342c loads it;0xb4342e loads the same original deck serial into r2/r3,0xb43432 passes EXP as the fifth AAPCS argument, and0xb43434 calls **CSRInventory::SetCardExp(uint64,int)**0xae98a0. Thus cur is the new absolute owned EXP, not a gain/delta.

## Native level recalculation and alternate legacy path

SetCardExp0xae98a0 finds the owned inventory entry.0xae9a26 snapshots GetLevel,0xae9a32 calls CSRCard::SetExp0x869ea4, and0xae9a3a obtains the resulting GetLevel. SetExp writes absolute EXP at card+0x20 and calls CSRUserLV::GetCardLevel using rank/EXP/awakening at0x869eb4..0x869ec0; it refreshes cached level/min/max EXP if the level changes. Supply the existing published GetLevel.card curve, **not invented completion level fields**.

If CPVHTTPRequest itself is null,0xb430b8 branches to an alternate positional iteration path0xb430de, which advances the card container by deck-slot ordinal and reads prev/cur at0xb43168/0xb432be. That is not evidence to replace the normal keyed response with an array. The actual HTTP path has a request and uses decimal serial identity. Keep an object; extra keys for hunters outside the native current deck are ignored by this callback.

The current result EXP arrays have four entries in the decompile (previous at stack+0xf4 and current+0x104, stride4), consistent with four mission hunters plus captain. The historical five deck-field envelope must not become a fifth real combat hunter without separate bound proof; this task does not establish that slot4 is safe in this result layout.

## Reward policy is separate from parser evidence

The callback iterates the whole **current native deck**, not surviving-actor records, and has no per-hunter dead/HP condition in this EXP branch. The completion request's play_info includes aggregate dead_cnt and aggregate player HP; these do not identify which owned hunter died. No individual defeat list is recovered here. An equal reward to each participating owned deck hunter is a coherent **local policy**, not a proved original surviving/defeated reward rule.

Current stage reference publishes **character_exp:10**, a local fixture. Current server completeMission increments user EXP30 only on first clear and returns card:{}; this user reward does not automatically distribute character_exp to hunters. A concrete extension can use the advertised character_exp10 for each unique nonzero owned ID in the accepted active battle's snapshotted deck, clamp to that hunter's published trainingCurve.maxExp, and return decimal keys with absolute prev/cur. Unknown awake curves should be refused/left unchanged explicitly, not extrapolated from ordinary rows.

Whether hunter EXP is first-clear-only, each completed win, or a defeat fraction is **not dictated by ReqCompleteCB**. For meaningful replay progression, a reasonable documented local policy is reward on each newly accepted, matching active battle **win**, including replayed stages, with no defeated reward. First-clear gold/userEXP may retain their existing separate policy. Require an active battle snapshot matching the requested stage; grant once before marking it completed/clearing active state. A late duplicate/no-active completion must return unchanged EXP, never reward again. A new active battle on another stage must not authorize a prior-stage completion. Native request has no recovered battle_id/nonce, so server battle identity is internal.

## Acceptance controls and risks

- Two owned hunters with different EXP cross a real published level threshold: native result shows both previous/current values, inventory/Gym and lobby profile agree, and relaunch retains EXP. Include an unchanged-at-cap hunter and omit an untouched nonparty hunter.
- Reward the accepted battle snapshot's members, never a subsequently edited lobby deck; keep native current deck unchanged during active battle so callback keys match its participants.
- Verify repeat **new wins** gain fixture EXP if that policy is chosen; duplicate request, defeat, wrong-stage active battle, or no active battle grants0. Backend persistence must cover ownership EXP and battle receipt/state atomically.
- Send numeric cumulative EXP directly under serial keys. Nested exp, zero defaults, positional arrays, or delta-valued cur would regress native ownership. Missing keys are harmless but suppress reward; malformed present keys may reset EXP0.
- Keep current skills/rank/p/locks/decks intact. Cap by each ordinary hunter's own curve, preserve unknown curves, and ensure next-level reference stats exist. Do not attach per-hunter HP or level fields as a claimed recovered contract.

No new Ghidra dump is required for the basic seam: existing0xb426ac callback and0xae98a0/0x869ea4 mutation functions contain sufficient evidence. Original reward quantities, repeat/defeat policy, and any per-dead-hunter reward differentiation remain unresolved.

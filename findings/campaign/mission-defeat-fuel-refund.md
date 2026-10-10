# Ordinary battle defeat/forfeit fuel refund evidence

2026-10-05. Bounded existing mission decompile/original Thumb, preserved community FAQ text-only lines1..606, final public UI_CSV/UI_TEXT/UI_JSON and existing VSFan historical help. No source/runtime/VM/adb/Ghidra changes, wallet action or grants. Parent's n_02_01 loss/AP49 is reported context, not measured again here.

**Expected ordinary policy is full loss/forfeit fuel restoration, not a recovered partial refund.** Strongest source is the **final preserved public UI_CSV.jet**, not only the loss-screen label: named **HELP_DATA**, header516, packed85055bytes, inflated288768bytes (RW plus length/BOM JSON). Article **CONTENTS2_3**, EN titleForfeit or Losing, says fuel is returned when a battle is lost or forfeited. KO explicitly says fuel is **not consumed** on forfeit or defeat; JA, SC and TC corroborate non-consumption. It states no partial percentage, time-based deduction or minimum loss fee. Original UI_CSV complete walk:8records/93380bytes, SHA25673a9dc4755baf8eb84c3fa945b7dd8b10228fe73d47a945de27137de2c84dac8.

The same CONTENTS2_3 in VSFan's archived1.4.4.1 UI_CSV/3d98d128.json says the same across those locales; this supplies historical corroboration, while the original final public help bridges the version gap. The standalone final UI_JSON **연료를 돌려받았습니다.|UI_LS_BX_TX4|EN** says **Your fuel has been returned.** A different quit-confirmation string says **Unused fuel will be returned.** Neither standalone label gives refund arithmetic; the complete original help provides the stronger no-consumption semantics. No targeted community FAQ text passage quantified defeat refunds; apparent broad rg hits in base64 image lines were discarded.

## Exact native completion AP receipt

Final **CSRSyncMStage.ReqCompleteCB Gb426ac** accepts authoritative AP in **ret_data.user.ap{prev,cur}**, with timestamp **ret_data.user.ap_charge_time** as a sibling of ap. Positive original register proof:

- Gb42826 indexes user and retains its pointer inr8 (mission-team-level-receipt.md).
- **LDRGb42cae/ADDGb42cb0** resolves ap; **MOVr0,r8 atGb42cb2** then indexes it atGb42cb4. Missing/null ap skips that branch.
- The AP object supplies prev/cur; native-mission-complete.txt lines1641..1699 show prev read and cur selected.
- **LDRGb42d6a/ADDGb42d6c** resolves ap_charge_time; **MOVr0,r8 atGb42d6e** then indexes it atGb42d70.
- The callback invokes **PlayData.SyncAP(currentAP,chargeTimestamp)** at native-mission-complete.txt line1731. This sets an absolute current balance; it is not an additive refund-item receipt or a refund automatically inferred from the loss label.

Loss/quit still uses normal Complete and requires native success1, as battle-completion.md's correction documents. The server therefore must include the correctly settled AP current value/timestamp if it restores reserved entry fuel. The inspected client does not calculate refund quantity from time, exit state or displayed copy. Exact cap/regen interaction must follow actual server resource accounting; this evidence does not justify rewinding earned regeneration or awarding unrelated fuel.

## Practical limit

The original final guide supports returning the ordinary battle's charged fuel on defeat/forfeit. A retained entry deduction after successful loss settlement conflicts with that documented expectation. Parent's observed AP49 needs authoritative before/start/complete reservation and receipt comparison to distinguish server settlement versus receipt/display mismatch; this lane did not read live account state. **Do not apply this ordinary-fuel rule automatically to Search Helium Capsules, paid retries, victory rewards or aborted unauthenticated/standalone Complete requests.** No correction, refund or replay was executed by this report.

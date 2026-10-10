# Fast bounded bench heart finder

`tools/find-bench-heart.py IMAGE EXPECTED_ENEMIES [--rage VALUE]` searches only
inclusive approved button-center region x250..390/y1300..1550. It emits JSON
`visible_button` and `safe_center` (null on refusal). No input is generated.
The center is a retained visual-match location, not a proved native hitbox or
actor assignment. Caller-supplied Rage is optional; without it funding remains
unproved. No screenshot Rage OCR or elapsed-burst funding inference occurs.

The helper scans a bounded white-fill region for separate cost-sized connected
components, projects their positions against the exact retained cost4 components
in heart4/heart4-bench, then checks only nearby alignments. It retains the existing
235 luminance fill, cost overlap>=.90, full-icon overlap>=.88 and circle-context
error<=18. Both templates form one heart family; distant accepted centers>16px
still refuse as ambiguous. Proposal counts/depth/region are bounded; excessive
components refuse. Unknown/occluded/merged glyphs can conservatively miss.

Retained checks passed:

- episode-bench-heal-002/before-contact-00: center343,1385; cost1/icon1/context0.
- Same run before-contact-01: center342,1380; cost.98649/icon.99426/context13.098.
- episode-bench-heal-003/before-contact-01: center346,1458;
  cost.96247/icon.98428/context15.815.
- Run003 before-contact-00: no candidate; refusal. This visual result does not
  independently establish its actual native funding value.
- Retained pause/map/loss and deliberate blank/wrong-sword/duplicate-heart/
  out-of-region controls refused. Explicit supplied Rage3.99 refuses;4 permits
  the retained positive. Invalid requests refuse.

Measured in-process elapsed times for the three positives were.181/.165/.158s,
with50 checked alignments each; run003 negative.154s/zero alignments. These are
host helper observations, not input-acceptance latency or guaranteed live timing.
Python process startup/controller capture time adds overhead. Four unittest
methods passed (2.927s total). No UI/ADB/Ghidra/server/native state was touched.

This solves the retained vertical movement around1380..1458 without widening
the existing match thresholds. It does not establish general detector coverage,
callback eligibility, bench-camera coordinate mapping or a successful heal.
Reconfirm stage/HUD/current source identity before the controller uses any result;
ordinary attacks must remain prompt and stop at cut-in/result/stage change.

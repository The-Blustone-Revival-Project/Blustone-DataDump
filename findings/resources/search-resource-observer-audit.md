# Search/resource observer source audit

2026-10-05. Read-only newly edited NativeGymSnapshot.java captureSearch/searchFields, EpisodeResourceSnapshot.java and Telemetry wiring; original13 public JET hashes independently compared. No VM/Ghidra/source changes, compilation or build/release by this lane.

## Concrete gap reported before build

The initial searchFields validates a null guide pointer with nonnull guideControl as unavailable, but lacks the equivalent **focus==0 && focusControl!=0** check. That pair bypasses focus ownership validation and can report scene_guide_focus_present:false despite a nonempty control identity. Add the same pair-consistency refusal before interpreting absence. Two equal anchors do not turn an inconsistent pair into a proved absent focus.

## Confirmed scoped reads and limits

Search current-scene chain, primary vptrs and GROUP/THUMB offsets match search-partner-reader-layout.md. GROUP stride0x1c, rowstride0x38 and availability+28 are correct. It uses only proven begin/end pairs, count bounds8groups/32rows, readable mapping checks, byte0/1 validation, controls>=0 and exact object guards. It outputs group types/counts/availability and guide/focus/input booleans, while pointer/header anchors remain internal. No names, addresses, account fields, target helpers, handler calls, memory writes or flags are emitted/mutated.

Two independent field observations compare JSON contents and internal owner/header/active-pointer anchors; app→manager→current scene/control/vptr are checked again before emission. This is bounded race detection, not lifetime locking or proof every ABA race is discarded. Field/type/count bounds can return unavailable for legitimate unknown layouts; that is preferable to inferring zero available helpers. Memory's map reader and RandomAccessFile are closed with try-with-resources on normal/exception paths.

The guide chain observed is the **scene-owned guide/focus**, not a direct ModalHandler.GetTop snapshot. scene_guide_present and focus_active do not independently prove that this guide is the current top modal or reveal the exact Back-hand callback phase. Successful survival or a stable snapshot does not prove the Home callback guard executed.

## Fixed resource inventory

All13 expected sizes/SHA256 strings in ORIGINALS match the preserved public PAD JET files in an independent read-only host calculation. The app checks the instrumented package/version28010, uses only fixed basenames under canonical files/local, checks each canonical parent, reads through16KiB buffers with an exact expected-size upper bound, closes streams, and emits metadata/digest/status only. It does not repair/download/upload original resource bytes or read account filenames.

The first equal-size observation waits, the second equal-size/mtime sample hashes, and later observations reuse a cached digest. This keeps steady-state work small; an initial hash pass can read48,815,972bytes sequentially but never buffers whole files. Telemetry calls it from the background heartbeat worker after Search snapshot and emits only changed JSON. Current source has one capture caller; static HashMap thread-safety is not a demonstrated issue under that single-caller wiring.

**Cached digests are not fresh file-content reads.** Same-size/same-mtime replacement or changes during a metadata-equivalent ABA interval can evade invalidation; equal metadata does not freeze a file or prove immutable contents. Document that limitation rather than treating originals_matched as fresh cryptographic verification every5seconds. A matched on-disk JET also does not prove the native engine registered/loaded its latest descriptors/resources.

The builder discovers all instrumentation Java sources via SOURCES.rglob('*.java'), so EpisodeResourceSnapshot is included without a separate manual source list. No concrete compile incompatibility was found by source inspection; actual javac/D8/build checks remain parent-owned.

No other actionable defect found in this bounded review. Correct the focus null/control pair, retain the freshness/ownership/top-modal limits, then compile/build and publish the required instrumented release before native claims. This report itself performs no build/release or live capture.

Parent reports the focus-null/control-nonnull refusal was fixed before build. Resource rows now explicitly emit hash_cached and have a directory symlink guard; pointer/header anchors are compared across both Search passes without capacity assumptions. Parent's host compilation,4valid/8malformed vector ranges and13 hash pins passed tools/test-search-state-reader.py. These close the reported source gap and clarify metadata freshness; this lane did not rerun those checks. +11 build/publication/native acceptance remain separately parent-owned.

Parent resolution before the +11 build: nullfocus/nonnullcontrol is now refused;
both observations compare private pointer/header anchors as well as contents;
resource rows label hash_cached and canonical directory escapes are refused.
Host compile/range/fingerprint checks and packaged/signature verification passed.
These are parent verification results, not an Android execution claim by this lane.

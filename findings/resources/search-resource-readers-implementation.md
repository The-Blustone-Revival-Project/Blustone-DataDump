# Search and Episode diagnostic readers, 2026-10-05

The successful separate24-package bootstrap does not prove Episode file residency,
and unchanged Partner navigation does not prove its guide state or callback
execution. These observations close those evidence gaps before changing behavior.

`NativeGymSnapshot.captureSearch` reuses the established read-only self-memory
reader with exact package/version, app/manager/current-scene vptr/control guards.
Only the Partner primary vptr is supported. GROUP begin/end pairs have stride
0x1c (28 decimal), bounded to8 groups; THUMB begin/end pairs have stride0x38,
bounded to32 rows each. Only type2 virtual-helper availability bytes are read;
friend row contents and names are not read. Unproved capacity fields are excluded.

The scene input byte and associated TutorialBase/FocusDraw pointers use pinned
vptrs and shared-control checks. Null pointers with nonnull controls are refused.
Both field contents and internal pointer/header/active-pointer anchors are read
twice, with current scene ownership rechecked; observed changes yield unavailable.
No pointers, names, account fields or exception text are emitted. No native calls,
memory writes, scene changes, usage reset, rewards or tutorial completion occur.
The reader does not suspend native threads or exclude ABA reuse, and the scene's
associated tutorial is not necessarily the top modal. It does not trace callbacks.

`EpisodeResourceSnapshot` examines only13 literal public JET names under the
app's local directory. Canonical directory/file boundaries exclude symlink escapes.
Expected sizes and SHA256 fingerprints are pinned to the recovered PAD originals.
Two equal metadata samples precede an initial streaming16KiB hash; changed size/
mtime invalidates it. Exact-size upper bounds and post-read metadata checks reject
ordinary partial/concurrent writes. No resource contents are uploaded or changed.
`hash_cached` distinguishes reused digests from new stream reads. Same-size/mtime
replacement and metadata-equivalent ABA changes remain cache limits; a match on
disk is not evidence of native registration or Episode rendering.

Both events are emitted only when JSON changes, from the existing5-second
background observer loop. No new APK/gameplay native patch is added; +10's guards,
Gym recovery and Episode seed remain. The builder includes all Java sources.

Host validation: `tools/test-search-state-reader.py` compiles both readers and
checks four valid/eight malformed ranges without opening live memory, then checks
all13 fingerprints against originals. Independent review caught the null-focus/
nonnull-control gap, corrected before build. Packaged DEX class/event names,
byte-exact UI seed and retained native override were verified; APK signatures
v1/v2/v3 passed. These checks do not establish Android reader acceptance.

Layout evidence: search-partner-reader-layout.md. Bounded independent review:
search-resource-observer-audit.md. Diagnostic release +11 notes/verification are
under analysis/releases/2.8.0.1+11; runtime acceptance belongs to episode-007.

## Native observations

Published+11/PID11008 booted on split24/1634666 with Owner0 data preserved.
Two noncached resource events matched all13 original sizes/digests, with cache
invalidation observed between them; cached follow-ups are separately labeled.
This establishes those files' byte identity at the stream-read observations,
not native registration or Episode rendering.

After finite ordinary guide input, Partner emitted a stable snapshot at
1791205326178: type1count0, type2count1/availability[0], eligible0, scene input0,
associated guide present, focus present/active. No helper selection or battle.
The runtime prerequisite gap and associated focus are now observed; top modal,
exact input-handler execution and +10 guard execution remain separate unknowns.

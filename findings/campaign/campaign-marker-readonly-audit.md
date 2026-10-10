# Campaign marker read-only layout audit

Read-only curated-source audit, 2026-10-10. No UI, ADB, Ghidra, native calls, server or saved-state writes were performed by this audit. This note is the only authored file.

`CSRPlayData` contains the marker `basic_json` at **+0x330**. The type is the byte at +0x330 and its union starts +0x338 (JSON-relative +8). `analysis/native-setmarker.txt:50-74` establishes the field and two union words. Root's fresh `analysis/ghidra-campaign-marker-storage.txt` independently binds GetMarker and RemoveMarker to these offsets.

The one-key GetMarker, G **00b72798**, is unsuitable for a strict non-mutating observer: it includes guarded initialization of a shared static null JSON, uses a tree find, then calls mutable JSON `operator[]` when a member exists. Absence returns the shared null object. Even where the existing member lookup does not insert, calling this function is unnecessary and does not establish a no-side-effect contract. Never call GetMarker, SetMarker, RemoveMarker, native JSON conversion, getters, or `operator[]` from the observer.

The JSON object type is **1**, null **0**, string **3**, signed integer **5**. SetMarker(string member) G00b7205c writes type3 and an allocated 0xc-byte libc++ basic_string pointer at JSON+8. SetMarker(int member) G00b7212c writes type5, low signed32 at +8 and sign extension at +0xc. A JSON occupies 0x10 bytes; union swaps and array iterator increments corroborate this. Campaign autoplay readers also dispatch types4/5/6 from union+8 and type7 as double; this groups conversion branches but does not independently name every tag. Report exact raw tag plus allowed typed values; do not silently coerce malformed values to Boolean or claim a generic number conversion.

Object creation in `native-setmarker.txt:97-106` allocates **0xc** bytes: +0 is begin node (empty value is container+4), +4 is the root/end-node slot, and +8 is count. GetMarker constructs the end iterator at object-container+4. SetMarker's iteration successor code follows node left +0, right +4 and parent +8. Its emplace result swaps mapped JSON at **node+0x20**, including union words at node+0x28/+0x2c (`native-setmarker.txt:208-215`). This closes the mapped value offset. Key +0x10 and allocation size0x30 are compatible with this ABI but require the exact specialization's body before calling them independently proven.

Exact relevant retained symbol addresses for root's export: JSON-map emplace G**00726c8c**, find<string> G**007957c0**, find_equal G**00726aac** (`analysis/native-evidence.tsv:2521,4298,2518`). `CSRDataMgr::GetPlayData` is G**008b26c4**. DataMgr singleton and current PlayData shared-owner offsets/control vptr are not closed by the old curated sources used here; do not borrow another singleton's control layout.

The observer's external output must be limited to four marker names: **MissionAutoPlay**, **MissionAutoPlayConfirm**, **MissionAutoPlayResult**, and **mission_auto**. Permit only `stage` and `autoplay` from the first, `autoplay` from the next two, and `is_first_clear` from the last. Canonical stage strings or the already-recovered numeric boundary stage0 may be exposed; unknown strings, unknown members, arbitrary marker names and values must never be printed or serialized. Traversal may compare bounded key bytes internally; unrecognized keys must not enter exception messages or diagnostic output.

Read at one suspended native frame through the existing read-only memory interface. Require mapped ranges for the PlayData owner, JSON, container and nodes; reject unsupported type, excessive count/depth, duplicate pointers, invalid parent relationships or mismatched header. Traverse a bounded whole tree or a bounded comparison search; do not assume an absent allowed member is null before validating traversal. Snapshot and re-read the owner/header/visited-node bytes, and reject instability. Validate the allocated string object, short/long flag, bounded length, terminator and mapped content before comparison. Nested JSON objects need the same validation, not blind mapped-pointer dereference. A bounded structural failure should emit only a fixed generic diagnostic, with no native key text. Presence, null, malformed, missing and unavailable must remain separate outcomes.

This audit establishes a source plan only. Live marker values, marker changes caused by result touches, and durable cancellation are unverified. No marker state should be altered to manufacture evidence or stop a chain.

## Exact-layout closure and implementation review

Root's fresh `ghidra-campaign-marker-tree-layout.txt` closes the previous uncertainties: the exact JSON-map emplace G00726c8c allocates0x30, constructs key at node+0x10, initializes mapped JSON type at +0x20 and its union+0x28; links left/right/parent are +0/+4/+8. `ghidra-campaign-marker-play-owner.txt` independently proves emplace<CSRPlayData> object at control+0x10 through its on_zero_shared destructor, rather than borrowing the +0xc layout from a differently aligned type. Root's accessor/owner exports bind DataMgr+0xa858 bridge and bridge+8/+0xc raw/control fields. The observer verifies the original control primary guard and initialized ownership, with no getter invocation.

Reviewed `tools/NativeCampaignMarkers.java`, `tools/tests/TestNativeCampaignMarkers.java`, and `InspectNativeInput.inspectCampaignMarkers`. Projection uses only four fixed external keys, fixed member keys and canonical values; unknown key values are not parsed. Node/header/owner rechecks reject unstable snapshots; tests cover secret isolation, invalid strings, absence/null, malformed links/count/minimum, and changed root memory. No code path calls original marker or JSON operations. No privacy or native-write blocker found in this reviewed version.

A minor defensive refinement was requested: short-string parsing should check its in-object terminator just as long strings do, with a corruption test. The whole-map ordering/count validation and two verification passes can cost many JDWP memory reads, so a safe Village or genuinely paused sample must establish latency before using this mode during combat or a live countdown. Passing tests proves parser projection and rejection behavior, not acceptable active-game timing or durable WIN cancellation.

## Corrected implementation and live Village sample

Rechecked corrected source: the short-string branch now rejects a nonzero in-object terminator, and the fifth corrupt-tree test alters the short `autoplay` key terminator to require rejection. Subrange cache reads key headers and mapped JSON leaves from an already captured48-byte node snapshot. The same encompassing read remains registered for final byte-for-byte verification, so this optimization preserves the snapshot check and does not introduce a native call or unchecked fresh dereference.

Retained `analysis/testing/campaign-markers-001/village-markers-final.txt` shows a read-only original render-frame snapshot with **6 unique marker reads** and all four allowlisted names **absent**. The corresponding stderr file is empty. This is current live evidence that initialized DataMgr/PlayData ownership guards and the absent-marker branch work. Root reports measured process duration1.31s, passing pure corruption/privacy/race tests and exact preservation of all three saved gameStates. This agent inspected source and retained sample output but did not run UI/native actions or independently repeat the saved-state comparison.

A populated WIN marker branch remains unverified live. The absent-marker Village duration must not be treated as the maximum latency of a populated tree; additional keys, nested objects and long strings increase read/recheck costs. Do not claim result cancellation or active-battle timing is solved by this sample.

## Commands and bounds

Compile the two host sources together (no APK rebuild):
`tools/jdk/jdk-21.0.12.1+1/bin/javac.exe -d analysis/input-probe tools/InspectNativeInput.java tools/NativeCampaignMarkers.java`.
After forwarding8701 to the verified instrumented PID, use
`InspectNativeInput 8701 --campaign-markers --frame` only at a safe menu/paused state.
No game-native getter or marker mutation is invoked. The returned map includes only
four marker names and their known members; all unknown values remain unprojected.
A helper instance is one snapshot: at most512 unique reads, max4096 bytes/read,
marker128/member32 tree nodes, lookup depth32, key96/value32 bytes. BST ordering,
count/minimum/parent/child/color bits and string terminators are checked; every
original containing byte range is repeated before output. This is structural and
temporal validation, not full RB-tree balancing/ABA/lifetime pinning or acceptance.
The inspector separately checks DataMgr and PlayData ownership/type/link/liveness.
Populated live WIN sampling and end-to-end cancellation remain unverified.

## Populated paused-battle validation (2026-10-10)

Stage44 (`n_05_04`) was entered through normal preparation, then paused once using the original Android Back route. Root verified the native Paused/Resume/Forfeit overlay before the observer. `analysis/testing/deep-cavern44-001/44-paused-native-markers.txt` records MissionAutoPlayResult present/autoplay1, with the other three projected markers absent. The populated tree required15 unique reads and1.266s process wall time; stderr was empty and all three saved gameStates compared exactly unchanged across the probe (`44-paused-marker-audit.json`). This closes the populated paused-battle path, not a populated WIN/countdown sample or an upper latency bound. It does not prove result-touch acceptance, marker removal, delayed rearming or durable cancellation.

Root resumed at the actual visible Resume center `(540,875)`, promptly fought with two bounded12-touch bursts and obtained native clear_time4/dead0/three stars. The private runner's contemplated WIN observer was removed after independent review found that timeout/drain could leave autoStart45 unfought. Pausing before the read avoids that countdown exposure. There is no active-combat observer admission implied by this successful sample.

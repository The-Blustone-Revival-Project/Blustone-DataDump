# Campaign automatic progression: native marker consumer

Read-only source audit, 2026-10-09. No server, save, client, UI or runtime changes.

Evidence: `analysis/ghidra-campaign-auto-progress.txt` contains Ghidra exports at relocated addresses G00e93ae0 (`CSRSceneMStageMap::SetAutoProgress`), G00e9696c (`PauseAutoProgress`) and G00e97008 (`ResumeAutoProgress`). Exact relocated literals are in `analysis/ghidra-campaign-auto-progress-keys.txt`. Ghidra addresses are original ELF addresses plus 0x10000.

## Marker admission and next selection

`SetAutoProgress` calls `CSRPlayData::GetMarker("MissionAutoPlay")`. A null JSON value returns without scheduling. A non-null marker is indexed for `stage`, converted to a native string, and `autoplay`, converted through the native JSON numeric/string dispatch into the byte at scene offset +0x6b4. The function then removes `MissionAutoPlay` **before** the enabled check. Only byte value exactly 1 enters the automatic selector branch. This is not a generic truthiness check; conversion, truncation and malformed types must not be replaced with JavaScript Boolean semantics.

Within that branch, it scans serials 1 through the positive stage count at +0x76c. Each lookup is `CSRGameStage::GetStageData(scene +0x7f8, serial)`, followed by a copied INFO record whose ID is compared with marker `stage`. On a match, the captured next serial is current serial +1. No match (including zero/nonpositive stage count) gives next serial 1.

If the matched next serial equals 0xb (11), the decompile constructs a new `MissionAutoPlay` payload with numeric `autoplay: 1` and numeric `stage: 0`, then keeps captured next serial 11. This is a boundary handoff, not proof of the receiving scene or next area. The export has aggressive reuse of JSON/local destructor temporaries around this branch; do not infer additional fields or an area transition from those reused variable names.

The marker's input `stage` is a string here; the special outgoing numeric zero is separately source-visible and must not be assumed to be a valid ordinary stage ID. The next marker consumer or callback must explain that sentinel.

## Animation and callback registration

For enabled automatic progression, the scene's panel map at +0x674/+0x678/+0x67c performs insertion-capable lookup for integer key 0 (new node key +0x10 initializes to zero). The exact named panel is `AUTO_SEL`; its playable animation group is `autosel`. The branch calls `SetGroup` and `Play`.

A callback capturing a weak scene reference and the selected next serial is appended to the playable component's `CMEventSet<float const, CMHashID const&>` vector (+0x90 header, +0x94 end, +0x98 capacity), under mutex +0x8c. The callback is a function of `(float, CMHashID const&)`, not a proved wall-clock timer. Source does not expose the animation's timing or event hash here.

The retained RTTI symbol identifies this callback as `CSRSceneMStageMap::SetAutoProgress()::$_2` (native-evidence.tsv, symbol string at G01e68fc9). Root subsequently closed its callable address from the registration instructions: G00e93ef4 uses the relocated PC literal G00e94134 (word 0x12ee914), then adds 8 to form primary vtable G02182814. Its callable slot +0x18, G0218282c, stores **0x00e9bffd**. The low Thumb bit proves instruction entry **G00e9bffc**. The prior ARM-mode decompile of that address is invalid and must not be used; `analysis/ghidra-campaign-auto-callback.txt` is a temporary read-only Thumb decode, with exact literals in `analysis/ghidra-campaign-auto-callback-keys.txt`.

That callback checks the event hash against `auto_select`: hash high word at event +0x14 must be zero and the computed CRC XOR stored low word at +0x10 must equal 0xffffffff. It also requires `CSRUIModalHandler` count +0x0c equal zero. It then calls `SetMarker("MissionAutoPlayConfirm", "autoplay", 1)` **before** attempting to lock the captured weak scene owner. If the control exists, its lock succeeds, and the captured scene pointer is non-null, it calls `CSRSceneMStageMap::SelectStage(scene, capturedNextSerial)` (capture scene +4/control +8/serial +0x0c).

This closes the animation-to-stage-selection transition. It does not close confirmation consumption, battle preparation, `BeginBattle`, the serial-11 receiving behavior or an area reward request. Those require the corresponding scene/marker consumers. The confirmation marker can be set even if the subsequent weak scene lock fails, because marker assignment precedes that lock.

## Pause and resume are nested

`PauseAutoProgress` reads the integer pause count at +0x6b0. Only when it is zero does it resolve `AUTO_SEL`, select `autosel`, and call `Stop`. It increments the count on every call.

`ResumeAutoProgress` does nothing if the count is nonpositive. Otherwise it decrements; only the transition to zero resolves the same panel/group and calls `Rewind` then `Play`. It is not an unconditional restart, and neither method rewrites the marker or the +0x6b4 autoplay byte in these exports.

## Rewards and historical attribution

None of the three bodies contains an achievement reward request or settlement call. These bodies and the Thumb callback supply a concrete native mechanism that can select the next stage without a new map touch when a qualifying marker, matching animation event and zero modal count exist. It does **not** establish that such a marker existed during the uncaptured campaign advances in AGENTS §199, that this callback fired, or that an area reward was automatically claimed.

To attribute a future run, collect the naturally produced marker, scene autoplay byte and next-selection callback/requests alongside continuous visual evidence. To explain a reward claim, inspect the actual achievement-reward caller separately. Do not insert a marker, replay a reward, change progress or treat an unexplained wallet delta as source-confirmed automatic settlement.

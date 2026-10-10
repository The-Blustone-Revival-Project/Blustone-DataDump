# 46 versus59 folded assets: bounded bootstrap sizing evidence

2026-10-05. Read-only server.ts/start-server.ps1/episode-resource-profile.ps1, public preserved asset files and lock-free JET decoder. No source changes, server listener, Ghidra, VM or account access. Parent reports +10 twice and retained+9 once aborting during bootstrap under59 assets; stack scans remain candidate lists, not call stacks.

## Actual selected-file delta

The established default set is8 stage/UI assets plus38 C001..C006 family files: **46 unique names,46,432,700 raw bytes**. Episode opt-in adds13 names, all distinct under case-insensitive comparison and none present in that baseline:

```text
R_EPISODE.jet    38,080
EPISODE.jet      6,529,928
DIAL-EN.jet      3,133,395
N001_BG.jet      2,282,467
ST099.jet        1,252,287
SND1.jet         7,173,961
SND_CDN.jet      10,911,430
VOICE_CDN2.jet   5,245,246
VOICE_CDN6.jet   7,338,509
C009.jet         3,101,288
C009_Q.jet       50,218
C009_EFT.jet     1,616,214
C009_SND.jet     142,949
```

Added raw bytes **48,815,972**, combined59 assets **95,248,672**. This more than doubles folded raw payload size. It is an observed byte count, not proof of Android heap exhaustion or original library bucket corruption.

## Package/table inspection

packageTreeEntries starts with the original E_NEW.jet and folds selected files as their untouched readFileSync bytes. It filters valid JET basenames/readable files and deduplicates case-insensitively. The corrected opt-in profile uses the actual consumed ASSET_NAMES_EXTRA variable and appends its13 files, preserving previous extras/explicit ASSET_NAMES. No concrete filename duplication or incorrectly encoded Episode name was found.

With current public analysis/runtime-package-full/E_NEW.jet base495,933bytes, modeling the actual writer gives:

```text
46 assets ->47 PKGI records, table916B, payloadstart936,
             outer package46,929,569B
59 assets ->60 PKGI records, table1177B, payloadstart1197,
             outer package95,745,802B
```

Each record is name-length byte, UTF8 name, uint32 payload-size and absolute uint32 payload-offset. Every selected name fits255 bytes; all offsets/sizes/counts remain far below uint32 overflow, payload offsets advance monotonically and no duplicate name occurs. This is a source/file model, not a fresh download of the active daemon's package. The parent host verifier already checks original13 JET bytes, PKGI offsets, manifestMD5 and ranges; this lane did not rerun it.

resourcePackages advertises the inner E_NEW JET signature separately from the outer pkgMD5/size. Both outer MD5 and response bytes are derived from the same packagePayload routine; no source inconsistency between those calculations was found. Changing the folded names requires a new consistent stamp so the client does not silently reuse a prior download. Host packet validity alone does not validate native decoding/registration.

## Encoded resource footprint inside the additions

Read-only decode reveals **1530 recognized inflated resources totaling88,971,662 bytes** in the additions that this decoder understands:

```text
R_EPISODE:66 resources /561,752 inflated bytes
EPISODE:63 /19,820,150
DIAL-EN:1357 /45,543,384
N001_BG:12 /13,455,966
ST099:9 /5,621,088
C009:9 /3,289,150
C009_Q:14 /680,172
```

SND1/SND_CDN/VOICE_CDN2/VOICE_CDN6/C009_EFT/C009_SND yield0 recognized inflated resources through this helper; those original formats remain opaque/raw to this calculation. **Zero recognized resources is not proof of empty/corrupt packs.** Their raw bytes are still included in the95.25MB total. Runtime decoded textures/audio/dictionary objects, temporary copies and peak retention can exceed or differ from these numbers.

DIAL-EN has the largest recognized resource-count/string-payload expansion, while sound/voice adds large raw files. These supply plausible independent sizing/registration variables for a test, but no native allocation size/owner was captured. Do not label a particular pack malformed or causal from the generic string-map rehash candidate. Native descriptor-name collisions across those resource containers were not exhaustively checked here; transport filename deduplication is not equivalent to all descriptor IDs being unique.

## Discriminating next check

First preserve exact active59-file list/stamp and correlate each failure's bounded CDN completion/reference bootstrap phase. The retained+9 failure means the problem is not unique to +10. A **single-variable restored46-selection control with current server response code held constant** is more informative than another unchanged59 bootstrap or another client patch. Use a new consistent stamp rather than a casual downgrade/cache assumption, and preserve app/account data.

However already-unpacked extra JETs/resource metadata may remain in retained client storage; merely serving46 files does not prove the13 additions are absent from native registration. Record the actual local resource set/version through existing bounded instrumentation before interpreting that control. Any selective resource isolation/removal is parent-owned preservation work, not authorized or performed by this report. An offline descriptor/index audit is a safe prerequisite while live attempts remain paused.

No concrete malformed PKGI record, filename duplication or uint32 sizing overflow was found. Increased footprint/resource count is proved; native heap cause and dictionary/cache ownership remain unresolved. Corrected curl/DNS/socket candidates in ghidra-bootstrap-abort-candidates-corrected.txt further reinforce that a stack scan cannot supply that owner by itself.

## Baseline transport control prepared

Parent stopped the identified replica listener and restarted wrapper9380 with
46 default folded assets, the same11 packages, resource/reslist1634665, persisted
state, fixture skills/recruit004 and spacing0. Prior daemon logs were preserved
locally. Fresh HTTP Range bytes0-1199 returned206 with Content-Range total46929569,
header stamp1634665 and47 records: the live package matches the baseline model.
Exactly one ordinary retained+9 launch is authorized, stopping at village or first
failure; no cache deletion or guide input. Outcome belongs to episode-004/report.md.
Cached additions remain a limitation even if this smaller transport succeeds.

The single control succeeded: retained+9/PID8118 completed the native54MB prompt
and reached village, reviewed by parent in episode-004/04-bootstrap-result.png.
No post-village inputs. AP50/BP10/Airport31/150 remained visible. This establishes
a usable smaller-update baseline, not a specific offending pack or +10 acceptance.

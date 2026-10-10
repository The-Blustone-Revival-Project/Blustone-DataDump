# Separate original Episode CDN packages: transport option

2026-10-05. Read-only server resource source, native-cdn-decomp-new.txt and existing CDN manifest evidence. No source edits, server restart, VM or Ghidra. Parent reports isolated host --separate verification/build passed; native acceptance remains unverified.

## Existing server can encode the13 JETs separately

resourcePackages() reads **BLUSTONE_PACKAGE_NAMES**, validating JET basenames with `[A-Za-z0-9_.-]+\.jet`; it first checks PACKAGE_DIR/name, then falls back to **RESOURCE_ASSET_DIR/name**. Thus public original Episode files need no copying into another directory.

Under current **pkgi1-tree**, packageTreeEntries begins with one record carrying the original source basename/bytes. For any basename other than E_NEW/UI_XML_RO, it returns that **single record** immediately. Appending the13 original names to package selection therefore uses the existing encoder rather than a new JSON/resource format.

```text
outer CDN name: R_EPISODE
request: /R_EPISODE_1634666.pkg
PKGI record: R_EPISODE.jet -> original unchanged bytes
```

Equivalent paths apply to EPISODE,DIAL-EN,N001_BG,ST099,SND1,SND_CDN,VOICE_CDN2,VOICE_CDN6 and the C009/Q/EFT/SND family. Hyphens/underscores fit both package-name validation and the existing pkg route regex. Native local ReadJson's SEASON_LIST/SEASON1 identity stays inside the original R_EPISODE JET descriptor map; it is unrelated to the outer package basename.

## Manifest and native unpack constraints

resourceManifest writes header lines **stamp, package_count, total_outer_bytes**, then CSV rows:

```text
name,stamp,outer_pkg_size,step,inner_jet_MD5,outer_pkg_MD5
```

resourcePackages usesstep0, derives inner signature from the original JET and outerMD5/size from the encoded package. Header/version/reslist stamp and each PKGI header must remain consistent. Disable diagnostic explicit/bootstrap/sequence reslist overrides for this control or they can advertise an unrelated package set. Native new-package count/type/ordering acceptance must be measured, not inferred from HTTP200.

**CPVCDN2.ExportPKGIver1 G7cf6a0** parses the20-byte header, final uint32 item count and filename/size/offset records. **UnPacking G7cfcf8** saves **each record's own filename** via CMSaveBufferToFile (native-cdn-decomp-new.txt around1350), rather than renaming it after E_NEW. A one-record package therefore materializes the same original filename as its prior E_NEW-folded delivery.

**CSRApp.LoadUpdatedJET G85a8f4** enumerates local filenames, checks .JET extensions, compares supplied updated-name filters, obtains GetResVer and calls IsLocalizedJET then CMJetLoader.Load. No E_NEW-only filename whitelist is present in that inspected loader. Locale filtering is still real—DIAL-EN must pass IsLocalizedJET for the current EN client. Broader CPVCDN bootstrap mandatory-package/group policy is not fully audited here; this code is positive generic unpack/load evidence, not a full proof24-package native startup succeeds.

Existing CDN evidence documents header.items/<PKG> and local PVC/<PKG>/packs/<hash>/filename/sign/size. Changing outer group names creates separate CDN ownership records even when files previously existed under E_NEW. Cache migration/re-registration behavior for those retained files needs native evidence. Do not casually delete or rewrite client CDN databases.

## Proposed opt-in launcher/profile boundaries

Appending **PACKAGE_NAMES_EXTRA** to the existing11 default packages only when explicitly selected preserves baseline startup. With13 extra groups the full manifest becomes **24 packages**. The initial host verifier checked E_NEW plus13 additions; parent subsequently expanded it to all24 packages and reran it successfully. This remains host transport evidence, not native acceptance.

The **-SeparatePackages** profile should add originals to package extras, keep E_NEW's established46 folded assets, and choose a new consistent stamp **1634666** for this unit. Crucially remove the13 Episode names from any prior ASSET_NAMES/ASSET_NAMES_EXTRA selection and neutralize a glob that would re-add them; otherwise the same JETs are delivered through both E_NEW and their new groups. Preserve unrelated custom extras. Retained local files can remain; separating transport does not require wiping account/app data.

When switching transport modes later, do not assume a lower fixed folded-mode stamp forces replacement of a higher separate-mode cache. Use a deliberate consistent new stamp and record the exact set. No implementation of the proposed PowerShell switch was present at the beginning of this review; these are concrete constraints for its parent-owned implementation, not a source PASS for uninspected future changes.

## Benefit and limits

The modeled original baseline E_NEW remains **47 records/46,929,569 bytes**, versus60 records/95,745,802 for all59 folded assets. Each extra now has one small PKGI wrapper; the largest extra is SND_CDN atabout10.91MB raw rather than a95.75MB monolithic download. This can reduce a single response/unpack buffer peak and permits a targeted group transport control.

It **does not reduce total59 original files,1530 recognized additional resources, texture/audio footprint or global descriptor/string registration**. Concurrent downloads/buffer retention may still overlap. No actual allocation count/owner was captured in the bootstrap bad_allocs, so separate transport is a discriminating option, not a proved fix.

Parent's --separate verifier now checks24 host packages: expected one-record extras and base groups, exact original bytes, inner/outerMD5, declared counts/total sizes and64-byte206 ranges; it pins E_NEW47 records/46,929,569 bytes, neutralizes inherited asset globs and restores settings afterward. Read-only source inspection found the initial assertions consistent with the intended host contract; parent expanded and executed the full24 check. No listener/test was run by this lane and no active daemon/profile was changed.

The next native control, only parent-owned after preservation, must verify actual reslist24/group requests/ranges/unpack completion and bootstrap progress while holding server gameplay responses/client build fixed. Native story dialogue/combat acceptance and C003_DIALOG binding remain separate unresolved requirements. No fabricated resource endpoint, metadata alias or reward grant is proposed.

## Native control outcome

One preserved-cache +10 launch/PID9968 under separate stamp1634666 succeeded.
Actual manifest24groups/106162408bytes and requests for every group were observed;
native101MB prompt progressed to village. Parent reviewed episode-006/03-download.png
showing AP50/BP10/Airport31/150 and the existing Search guide. No post-village inputs.
This closes group-name/request/bootstrap acceptance for this control. It does not
prove individual Episode resource use or story/combat playback, and retained caches
prevent treating it as a clean-cache isolation of the earlier allocation failure.
See episode-006/report.md for runtime/account limits and selected-file audit.

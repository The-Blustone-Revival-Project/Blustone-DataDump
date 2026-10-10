# Preserved native-reference cache candidate inventory

2026-10-05. Metadata/filenames and existing indexes/docs only across the three preserved phone recovery snapshots. No database value/body, account/token/cookie contents, APK bulk, Ghidra, collector, live phone, VM or server access. Report is the only written artifact.

## Existing index evidence first

`tools/export-recovered-reference.py` intentionally exports only allowlisted read-only localization/skill tables; those are client content, not cached HTTP reference responses. `tools/mine-export-reference-tables.py` enumerates13 known *_RO tables. Neither exports ITEM_REF/fish reference tables. Current private local-directory inventories in9/18 and9/20 have the same13 *_RO names plus CDN.db,UserData.db,EtcData.db,ETC.db,PV.db,USER.db and profile imagery; **no separate REF/ITEM/FISH database or raw reference filename** was found in these inventories.

Existing `phone-evidence-2026-09-19/README.md` line47 already states no complete native gameplay reference/lobby HTTP response corpus was found. This is a prior scoped finding, not proof all native local cache keys are absent. `card-reference-refresh.md` separately proves the final client can call CMJetLoader.LoadStr with exact local **REFEN/reference/GetCard** key; client capability does not establish that a preserved snapshot holds that record. GetItem/fish cache key construction must not be guessed from this one route.

## Sanitized HTTP-cache metadata check

**recovered-assets/phone-evidence-2026-09-19/web-cache-manifest.json**,202954bytes, has497 records and0errors. Its fields are source/body/host/path/queryKeys/contentType/bytes/sha256/crcVerified. A bounded check of metadata paths only found **zero /reference/, /fishing/, GetItem or GetFishingPool paths**. No query values, headers or cached response bodies were read/emitted. Thus the already-indexed WebView cache is not a positive original native GetItem/fish response source. `cache-url-summary.json`10924bytes is a smaller host/path index; `game-web-cache-index.json`113781bytes is another web feature index, not a recovered native schema table.

Metadata directory totals:9/18 private/files/local540files/24110006bytes, private/cache1029files/29273034bytes;9/20 private/files/local537files/24162328bytes and cache1029files/same29273034bytes. The cache/profile trees are dominated by WebView/SDK/image evidence, not identifiable named gameplay references. app_tmppccache and app_textures are empty in the inspected9/18 and9/20 trees. No archive extraction or body scan occurred.

## Bounded candidates for a next keys-only pass

These are **candidates, not proven reference caches**. Prefer existing sanitized key indexes first; if inspecting raw databases, use a no-open active-MANIFEST/SST/WAL reader or a throwaway copy, never in-place plyvel.

1. **UserData.db**, native local state/container:
   - Existing index **phone-evidence-2026-09-19/UserData.db.keys.json**,55984bytes; database-summary metadata reports497records/27156valuebytes. Inspect **keys only**, specifically recovered native REF/cache namespace prefixes; no generic state values or account identities.
   -9/18 source components: **phone-2026-09-18/private/files/local/UserData.db/000374.ldb**34819bytes; **000376.ldb**50364; CURRENT16; MANIFEST-000380202;000381.log empty.
   -9/20 source: **phone-history-2026-09-20/private/files/local/UserData.db/000374.ldb**34819; **000373.log**55189; CURRENT16; MANIFEST-000371532. The9/19 diagnostics copy has the same listed component sizes/names. Nonempty WAL means SST-only examination is incomplete.
2. **EtcData.db**, native local auxiliary state/container:
   - Existing key index **phone-evidence-2026-09-19/EtcData.db.keys.json**,2949bytes; summary29records/2548valuebytes. It is small enough for an exact-prefix keys-only inventory; no useful native-reference content is assumed from its name.
   -9/18 source components: **phone-2026-09-18/private/files/local/EtcData.db/000437.ldb**3323; **000439.ldb**13003; CURRENT16; MANIFEST-000441185;000442.log empty.
   -9/20 source: **phone-history-2026-09-20/private/files/local/EtcData.db/000437.ldb**3323; **000436.log**21851; CURRENT16; MANIFEST-000434285.9/19 diagnostics copy has the same listed component sizes/names.
3. **CDN.db** is already a large resource-descriptor key index (CDN.db.keys.json2311991bytes), with summary23656records/9164valuebytes. It may link resource names/containers, but is not an original reference HTTP response catalog merely because it has many keys. Consult only exact REF/ITEM/FISH descriptor candidates after native LoadStr storage ownership is known.

ETC.db has3records/132valuebytes and USER.db0/0 by the existing summary; they are lower-priority metadata candidates. Cloud account files, PV credentials/preferences, profile-image names, SDK queues and WebView cookies were deliberately excluded from content examination. No private material was copied into published references.

## Parent keys-only follow-up

The three existing indexes were inspected structurally, then only their key
names were compared. UserData497,EtcData29 andCDN23656 entries contain no
literal or case-normalized GETITEM/GETCARD/GETFISHINGPOOL matches and no
REF-locale/REFERENCE namespace matches. No prefixHex fields, database values,
account identities, query values or response bodies were emitted. Sanitized
aggregate results are native-reference-key-index-scan.json.

GetItem's local key construction is now independently proved by the constructor
URI literal atGf80a22 (native-reference-offline-storage.md). LoadStr preserves
the string until resource-map lookup uppercases it; normalized existence key is
REFEN/REFERENCE/GETITEM. This supersedes the earlier unproved GetItem-key limit.
The scoped index misses still do not exclude opaque/generated JET descriptors,
uncatalogued snapshots or separate local resource content. No raw private database
body scan or live phone request followed the negative index result.

## Initial metadata-pass conclusion

No **positive original GetItem/fish reference cache file** was identified by this filename/metadata pass. The precise next bounded operation is a keys-only scan of the existing UserData/EtcData indexes for a recovered native cache prefix, followed only by an exact matched record if one exists and its storage model is established. Do not broadly dump these state databases or reprocess multiGB APK/collector sources. Source contents and originals remain unchanged; no absence claim extends beyond the listed snapshots/index scope.

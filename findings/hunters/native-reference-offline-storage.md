# Native reference offline storage: actual paths and limits

2026-10-05. Read-only original ELF, native-reference-request.txt and existing
card/reference/fishing reports. No Ghidra/device/account content reads or writes.
G addresses use Ghidra coordinates; ELF=G-0x10000.

## Proven local resource fallback

CSRSyncRef.RequestByPVJson **Gf82a70** reads a local reference string before
HTTP. Exact key construction: literal **REF** atf82afe, language getterf82b48,
locale table KO/EN/JA/SC/TC, concatenate selected URI atf82c04, then
**CMJetLoader.LoadStr G71ba48 atf82c26**. Constructor URI literals include
/reference/GetCard atf8099c and /reference/GetItem atf80a22. English keys are
therefore **REFEN/reference/GetCard** and **REFEN/reference/GetItem**.
Nonempty text enters local asynchronous callback setup; empty text enters HTTP
construction. This mechanism is positive evidence of local reference content,
not a recovered numeric GetRefVer or a write-through HTTP cache.

LoadStr's actual resource path calls **CRMResMap.IsExistingRes G717e04 at71bac4**
and **CRMResourceMgr4.LoadRawData G10eac8c at71bb28**. Thus the immediate owner
is the JET/resource map. The name is a resource key, not a proved filesystem
path or LevelDB table. Existing nene-null-reference-crash.md records the same
key construction and corrects earlier claims that no local read exists.

## HTTP decode and in-memory application

RequestByPVJson builds encrypted form HTTP atf8305e and dispatches through
CPVHTTPManager.Request atf832b8. Its decoder function is independently resolved:
LDRf8306c/ADDf83070→ELF GOT21ac1f4→odd pointer84001d, i.e.
**ToNlohmannJson G85001c**. That helper calls body transformer8500d8 at85004a;
its symbol encodes **Decryptor→ToString→ToNlohmann**. Transformer8500d8 calls
decrypt/string transformer7ca894 at85010a and JSON converter850168 at850116.
These are protocol-decoding targets; no secret bytes were examined.

ReqCardCB **Gf839f2** only checks responsecode1 (or null local response), obtains
CSRCardInfoContainer and tailcalls **SetCard G87baa4 atf83a10** with the decoded
JSON. ReqItemCB **Gf83a14** similarly tailcalls **CSRItemInfo.SetItem Gaefe10
atf83a32**. Neither short callback writes disk, a resource or LevelDB. The
reference parsers populate native containers; their names do not establish
durable storage.

Fishing.RequestPool **Gb2b31c** builds its own HTTP request. Its actual
RequestPool$_4 receiver **Gb324c8** iterates ret_data lure_id/fish_id strings and
inserts them into Fishing's in-memory map+30/+34. No LoadStr/local-reference
fallback was identified in the inspected pool builder/receiver. This does not
prove that no caller ever writes a separate snapshot.

## Where to look next, without inventing a table

The known13 exported LevelDB tables lack ITEM_REF. That scoped absence does not
exhaust JET/resource data or prove original HTTP reference caches were deleted.
The evidence-backed next public-resource search is exact localized **REFEN/**
and other REF-locale route keys in preserved JET resource descriptors, then any
matching raw JSON resource, preserving wrapper shape. Ordinary visible outer
JET filenames may not equal these nested/generated identifiers. No actual
matching record was recovered by this unit.

Persisted CDN JET files/resource LevelDB databases are separate from a proven
HTTP-response cache. CSRLocalDB access in RequestByPVJson is specifically for
language selection, not an item/card-table read. No original offline cache
filename, SetItem/SetCard write-through path or FishingPool persistence was
proved here. If further parent decomp is needed, exact bounded targets are
**RequestByPVJson f82a70**, **LoadStr71ba48**, **ToNlohmannJson85001c** and
**JSON converter850168**; existing dumps already establish the model callbacks.

## Key normalization: CMHashID is not the final lookup key

CMHashID.C2 G6de260 creates a string and calls move-Set6df130 at6de288.
Set moves the supplied string unchanged (6df172..184), calls Crc326df1f8
at6df1b2, complements its result at6df1b6, then stores the low32 result at
CMHashID+10 and zero at+14 (6df1b8). Crc32 reads source bytes directly at
6df214; no uppercase, slash removal or namespace split appears in that path.

LoadStr instead selects the original CMHashID string buffer at71bab4..71bac0
for IsExistingRes71bac4, then again at71bb16..24 for LoadRawData71bb28.
It does not use the stored CRC for that existence lookup. Exact normalization:
**IsExistingRes717e04 → strupper10f5fc4 at717e2e →
unordered_map<string,vector<RMRESINFO>>::find717eb0 at717e46**.

Effective ASCII existence keys are **REFEN/REFERENCE/GETCARD** and
**REFEN/REFERENCE/GETITEM**, retaining slashes. The raw-loader resident/file
paths also uppercase: FindResource10e97b4 toupper10e9812; GetResInfo75dda8
toupper75de0a (episode-native-resource-loading.md). No slash stripping,
namespace splitting or filesystem-path interpretation is proved on this direct
LoadStr chain. ReadJson's JSON-subtree traversal is a separate loader.

A readable literal REF-key miss therefore does not exhaust opaque/nested/
generated resource identities. An unnormalized CMHash CRC search likewise
does not test the uppercase resource-map key. Descriptor registration/hash
encoding needs separate corroboration before claiming preserved packages lack
the reference. No exhaustive absence is claimed here.

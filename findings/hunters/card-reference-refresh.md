# Card reference refresh: no recovered GetRefVer contract

2026-10-04 urgent read-only original-library/current-source inspection. No source/runtime/Ghidra/adb/original changes. Existing owned Nene must be preserved. Ghidra addresses.

**No GetRefVer, GetRefVersion, ref_ver or equivalent named version route/field was found in the native string vocabulary or current server sources.** This negative search is not a universal proof that no cache exists; it means there is no evidence-backed field to bump. The persisted server snapshot's `version:1` is its JSON save-schema version, not a recovered game-reference stamp. CDN assetstamp1634662 drives resource/package updates and is separate from the inspected card-reference path.

## Verified native request and consumer path

- `CSRSyncRef::Init` **0xf81ebc** explicitly dispatches reference requests through RequestByPVJson and RequestByNlohmnJson. PV-json calls occur0xf820f2,0xf82122,0xf82152,0xf82182,0xf821b2,0xf821e2; later calls cover the other reference tables. This is initialization work, not a recovered GetRefVer negotiation.
- `RequestByPVJson` **0xf82a70** accesses CSRLocalDB/GetLanguage0xf82b12..0xf82b48, builds a CPVHTTPRequest0xf8305e, sets timeout0xf83066, then invokes **CPVHTTPManager::Request**0xf832b8. **CORRECTION from systems research:** it also calls **CMJetLoader::LoadStr** at0xf82c26 using the exact local reference resource key **REFEN/reference/GetCard**. Nonempty loaded text takes a local asynchronous callback path; empty text enters HTTP construction. The earlier negative cache-read wording was incorrect because that call was missed. No GetVersion call/numeric reference-version field was recovered. See `nene-null-reference-crash.md` for exact key construction.
- **ReqCardCB0xf839f2** checks responsecode1 at0xf839fc..0xf83a04, obtains CSRCardInfoContainer0xf83a06, passes its supplied decoded JSON argument, and **unconditionally tail-calls SetCard0x87baa4** at0xf83a10. There is no reference-version comparison or cache-write in this callback. If the HTTP response status is not1, it returns without updating the card table.
- Current `/reference/GetCard` server handler returns the current module's `starterReference` directly. `base.id` is the lookup id and each card's res_prefix is an independent art namespace. A four-row source file alone does not prove a currently running process or already-open native session consumed those four rows.

## Discriminating next evidence

**Runtime update:** parent confirmed a GetCardHTTP response before the crash in server.stdout lines115–120, timestamp22:32:12.716, encrypted exchange with17344plaintextbytes. That disproves a simple “no GetCard network request” explanation for this run. Native callback/registration order and the exact bytes actually consumed remain separate facts to establish. Preserve app data/account/deck and owned Nene. See `card-reference-shape-audit.md` for current serialized row comparison.

If003 is present on the wire before the ownership add yet IsTrainingCard still dereferences a missing card info pointer, the unresolved issue is **reference parsing/registration or lookup identity**, rather than an established version cache. Follow SetCard/CSRCardInfo construction for that actual003 record and compare with known002. If no GetCard request is emitted on a fresh launch, inspect which initialization branch skipped it before inventing a version gate.

No code change, app reinstall/data clear, repurchase, account reset, reference-version guess, or additional assetstamp bump is justified by this lane. Its concrete result is the recovered unconditional SetCard callback and direct initialization request path; the exact runtime missing-ref cause remains unverified.

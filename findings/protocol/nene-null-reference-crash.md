# Nene recruitment crash: null CardInfo and reference loading

2026-10-04. Independent original-library Capstone inspection, read-only.
The already persisted003/rank3/inst4 award must not be purchased/retried.

## Exact crash dereference

ELF PC86888f is Thumb Ghidra87888e in CSRCardBundle::IsTrainingCard:

```asm
87888c ldr r0,[r0,#20]       ; bundle-owned shared CSRCardInfo pointer
87888e ldrb.w r0,[r0,#3c]  ; CardInfo is_source/training flag
878892 bx lr
```

A null shared CardInfo produces a fault at address3c. This function does not
read rank, card stats, equipment, skill or art. ELF LR ad9301 corresponds to
return after Ghidra ae92fc call in CSRInventory::AddCard(shared_ptr<Card>,1).

AddCard obtains ref id from the owning Card's string at+5c, calls
CSRCardInfoContainer::FindCardByID atae9282, then constructs a bundle with
the returned shared_ptr atae928e **without checking it for null**.
The bundle constructor87823c copies that shared pointer into+20/+24
at878258..25e. FindCardByID87d2ec returns0/0 explicitly on map miss
at87d31e..322. This is a fully matched missing-reference crash path.

The most direct explanation is that native CardInfoContainer did not contain
an exactly matching003 entry when the award was added. Four definitions in
server source or a successful C003 asset download does not establish that.

## Fresh reference callback replaces the map

ReqCardCBf839f2 accepts response code1; it tail-calls SetCard87baa4 atf83a10.
SetCard first destroys and clears its existing reference map at87bad8..bae4,
then parses ret_data. It is not append-only. No rank gate occurs in
FindCardByID; a rank3-only issue would occur later after a nonnull reference.

## Recovered local reference resource read: exact key

CSRSyncRef::Init explicitly asks for the reference tables. RequestByPVJson
f82a70 can first read a **shipped/local resource string**, before constructing
an HTTP request. The precise path is:

1. f82af6 loads literal poolf82dd8; add-PCf82afe produces G1d9022d "REF".
2. f82b48 gets language. f82b4c/4e loads tableG218d680, whose first five
   ELF-pointer entries are KO,EN,JA,SC,TC. f82b60 appends the locale.
3. Constructor f80964 stores URI_COMPLETE3; f8099a/9c loads literal
   G1d8feb7 "/reference/GetCard", copied to that map row's string+14.
4. f82c04 concatenates prefix+locale with that URI string.
5. f82c26 calls CMJetLoader::LoadStr with the resulting hash key.

Thus the English GetCard local resource key is exactly:

```text
REFEN/reference/GetCard
```

No separator is inserted between REF and EN; the route supplies its slash.
A nonempty loaded string branches atf82c5a into the local-data asynchronous
callback setup/thread path f82d68..f82ed6. Empty data instead follows the HTTP
construction branch beginningf82cea. A local resource path is therefore
present even though a named GetRefVer handshake is not recovered.

This refines the negative-cache wording in card-reference-refresh.md:
RequestByPVJson **does read CMJetLoader local reference content**. It has no
GetVersion call in this inspected path. Whether the currently active resource
tree actually supplies REFEN/reference/GetCard, and which callback won the
runtime ordering, are not established by offline code alone.

## No recovered version field to bump

Searches of native symbols/strings and current server sources found no route
GetRefVer/GetRefVersion or wire keyref_ver/reference_version. Do not invent one.
The persisted server JSON schema version and CDN package/reslist stamp are
separate mechanisms. The local resource read above is keyed by locale+route;
it does not append a numeric card-reference version in this function.

Discriminating evidence after a fresh process launch, preserving account/data:
verify the actual GetCard response includes base.id003 and code1, and whether
native ReqCardCB parses it before AddCard/inventory refresh. If no HTTP request
is emitted, inspect the proven REFEN/reference/GetCard resource key and boot
branch; if003 was delivered and parsed, follow actual registration/id equality.
No regrant, account reset, reinstall/clear, client null-dereference mask or
unproven version bump is justified by the current evidence.

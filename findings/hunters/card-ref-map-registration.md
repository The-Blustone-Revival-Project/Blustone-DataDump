# Card reference registration after the confirmed four-card HTTP response

2026-10-04. Read-only Capstone/source inspection; no adb/Ghidra/client edits.

The confirmed native GetCard request in CURRENTserver.stdout115–120
(d5f58af8,22:32:12.716Z,secure response17344 bytes, before lobby/recruitment)
means **a cache-only explanation is insufficient**. The prior local resource
finding remains a possible later replacement source, not a proved cause.
No reference-version field is proposed.

## Exact parser identity, iteration and insertion

SetCard87baa4 reads decodedJSON[ret_data] at87baca, clears the entire existing
map at87bad8..bae4. For an array, total outer record count is
(end-begin)>>4 at87baf8..bb04; object rows use their size, other nonnull values
use1. There is no two-record cap. The loop increments index at87bb58..60.

Each row's base object is selected at87bb74. base.id is read87bc68..84,
converted through from_json<string> and stored at shared-control allocation+0c, which is actual CSRCardInfo+0.
base.char_id is read separately starting87bcbe. At insertion87c71a..722
copies **actual CardInfo+0**, then tree __find_equal receives that exact string
at87c740. If the key already exists,87c748 goes straight to cleanup87c798:
**first duplicate wins**. If absent it creates a tree node and stores key at
node+10, shared CardInfo at+1c/+20; unique map size container+8 increments
at87c792..796. The role/is_main/source/stat rank paths do not filter003 or
require an original birth rank in this lookup.

No source-level discrepancy was found in the inspected additional003/004
records: they explicitly set base.id/char_id/ref_id003/004, and use the same
mandatory collections as001/002. This is not proof that the received wire
values, parser completion or actual award ref string matched those objects.

## All direct callers and replacement/exception possibilities

Whole original-library Thumb BL plus unconditional B.W scan for87baa4 finds
only **f83a10**, ReqCardCB. Its code accepts responsecode1, obtains the
singleton, passes decoded JSON and tail-calls SetCard. A local resource loader
can supply the same callback without generating another HTTP request; there
is no separate known direct 'cache SetCard' caller.

SetCard has exception cleanup landing pads87c850..ca20; the final cleanup
calls the native rethrow helper at87ca20. It does not catch a bad row and
continue to the next one. Since insertion occurs only after a whole row's
stat/skill/dialog parsing, an exception in third003 can leave previously
inserted001/002 and skip003/004. This is a **plausible discriminating mechanism,
not an observed exception**. Exact error/failed callback evidence is needed.
Likewise a later SetCard invocation with older two-card local content would
replace all four references, but that invocation has not been observed.

## Bounded read-only live map audit

A live map snapshot can resolve the important uncertainty without invoking
native getters or modifying the APK. Exact ELF offsets (B=load bias):

```text
weak singleton = B+21cf2d0
container = u32(weak singleton)
control = u32(weak singleton+4)
```

Dynsym exact name ends CMSingleton::get<CardInfoContainer>::wpRet, size8.
Offline getter87f3e6/e8 models GOT slotG21bc378 -> ELF21cf2d0 and reads its
weak pointer at87f3f0..f2 and87f46a. Guard nonnull/mapped control+container;
require signed control owners+4>=0, control vptr==B+2141730
(exact shared_ptr_pointer<CardInfoContainer,default_delete> vtable+8),
and u32(control+c)==container. On-zero-shared880a08 reads that same+c pointer.

After those guards:

```text
leftmost=u32(container+0), root=u32(container+4), count=u32(container+8)
node left+0, right+4, parent+8, color+c
node key std::string+10; node info pointer+1c, control+20
short key: if byte(node+10)&1==0 -> length=byte>>1, chars atnode+11
long key: len=u32(node+14), chars=u32(node+18)
```

Use at most32 nodes, maximum16 key bytes, visited/cycle and mapped-range
guards. The count is unique keys, not published array length. If keys003/004
are absent, count2 versus count4 sharply separates parser/overwrite hypotheses.
If003 is present, compare its actual byte spelling to award Card+5c ref id;
a later null bundle then cannot be attributed simply to a missing published row.
The container itself has no primary vptr; use its control-block identity above.

Originals and persisted award are untouched. No regrant, guessed version bump,
null-dereference mask or claim of a discovered parser bug follows this evidence.

## Follow-up: exact HTTP callback JSON and identical singleton

An initial live count0 snapshot **before GetCard** is expected and is not
parser-failure evidence. Use the post-reference snapshot for the map audit.

HTTP RequestByPVJson installs ToNlohmannJson85001c through the literal at
f8306c -> GOTG21bc1f4 -> ELF84001d, loaded atf83070/74.
ToNlohmannJson calls decrypt/to-string transformer85010a then
CPVHTTPResponseToNlohmann850116. The latter parses the **entire decoded string**
at8501a0 and moves that JSON result into its output at8501a4..bc.
ToNlohmannJson indexes result_code850056 only to set the response's PVCode;
it does not select data or ret_data as the returned JSON.

Atf83290 the request builder loads the original caller callback fromsp1c.
Its operator>> callf83296 -> ae63fc constructs PVHTTP::BINDER arity3.
The lambdaae77ec calls the upstream transformer atae784c, copies its returned
JSON atae7856, then invokes the original callback atae786c with
r1=request, r2=response and **r3=&copied full JSON** (ae7864..6a).
There is no JSON index/unwrap between the upstream result and that callback.
ReqCardCB passes this decoded full envelope to SetCard.

SetCard's first explicit field read is **ret_data**, not data: literal pool
87be1c + add-PC87bacc = G1d689bb "ret_data", consumed87baca.
The callback and parser jointly require a full envelope whose ret_data is
the bare reference array. This does not justify adding alternative aliases.

Both consumers use the exact same singleton:

```text
ReqCardCB f83a06 -> CSRCardInfoContainer.get87da9c
Inventory.AddCard ae9270 -> CSRCardInfoContainer.get87da9c
get87dab2 -> CMSingleton.get87f3c0
wpRet = B+ELF21cf2d0
```

There is no distinct inventory allocator or alternate CardInfoContainer
singleton on these two inspected paths.

is_main is read from the row's base object and written to **actual CardInfo byte+40** (shared allocation+4c)
at87bc6e. No subsequent is_main read controls SetCard insertion or container
lifetime; every completed row uses the same map insertion path. The separate
name substitution branch87bd90..c808 recognizes the user-name placeholder
and reads CPV account name; it does not retain the container by an is_main flag.
The owning shared references/weak singleton lifecycle are independent of that
one-byte metadata flag in this inspected parser.


## Live-map identity correction and grant parser (2026-10-04)

The post-reference snapshot `analysis/testing/revival-006/card-map-confirmed-second.txt`
verifies count4 and keys001/002/003/004, nonnull reference pointers and
training byte+3c=0. This rules out a missing003 map entry at that snapshot.

**Object-base correction:** SetCard allocates a shared-control block containing
CSRCardInfo. The allocation has its vptr/count header at+0..b;
actual CardInfo begins atallocation+c. The parser's sp54 is the allocation;
sp4c is allocation+c. At87c728 it stores sp4c as the shared **info pointer**
and sp54 as its shared **control pointer**. Earlier CardInfo+c ID wording
confused these bases and has been corrected above. Actual CardInfo+0 is id;
+0c is res_prefix, exactly matching the live C001/C002/C003/C004 values.
Actual training+3c and bundle+20 remain correct.

CSRCard::parse8680a4 reads inst_id at8680c6: literal868384 plus add-PC8680c8
is G1d6eec9 "inst_id"; the converted64-bit serial goes to Card+10/+14 at86810e.
It reads **ref_id** at868118: literal868388 plus add-PC868118 is
G1d6edf2 "ref_id"; from_json<string>868124 converts it, and86812a..166
moves the exact string to **Card+5c**. There is no resource-prefix substitution
or003-to-C003 conversion. SetRefID86c30c likewise copies the supplied string
to+5c then calls the same CardInfoContainer::FindCardByID at86c37c.

The GachaPremium callback calls ParseCardInst for each ret_data.card entry;
ParseCardInst b69598 allocates a Card and calls parse atb695da, then
GachaPremium f752ec passes the returned shared Card to Inventory.AddCard(1).
Thus ref_id:"003" should look up map key"003" directly. No new award-key
alias is justified by these native accesses.

The original IsTrainingCard crash remains evidence of a null **bundle's
retained CardInfo** at that earlier AddCard call, not proof that003 is absent
now. Late replacement/incorrect award ref string/stale null bundle remain
unresolved possibilities until their timing and actual instance fields are
measured. Keep the persisted award and do not retry recruitment to diagnose it.

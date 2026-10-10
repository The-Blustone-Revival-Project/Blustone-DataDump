# Single recruitment result shape: root cause candidate for Nene's null bundle

Current-state qualification (2026-10-08): this is the historical diagnosis.
Current server single-pull publication uses a card object; the array discrepancy
below was corrected. Preserve its native parser evidence, not its old claim
about current source. See gc2-coupon-contract-audit.md for coupon receipt limits.

2026-10-04. Original-library Capstone and current server source, read-only.

**Critical native distinction: ret_data.cnt>1 uses card[], while cnt<=1 uses
card directly as one object.** Current state.gachaPremium returns card as an
array even when one card is granted, making the single-pull path malformed.
This is a concrete server/client contract discrepancy, independent of card
reference caching or missing art. Preserve the already persisted003/inst4.

## Exact native control flow

CSRSyncLottery::ReqGachaPremiumCBf74fb0 reads cnt atf751e4.
For integer values it compares to1 atf751fe and branches to the single path
f753d8 if<=1. The decimal/string arm likewise compares atf753d2 and branches
into the multi loop only if>1 (f753d4).

For cnt>1 it indexes card atf7520a, iterates the JSON array by index, calls
ParseCardInst on each element, and adds each parsed Card atf752ec.

For cnt<=1:

```asm
f753de json["card"]                ; WHOLE member, no numeric [0]
f753e4 ldrb r0,[r0]               ; null guard
f753e8 beq f754e0                 ; absent/null card skips ownership add
f753f6 mov r2,r4                  ; r4 = whole card member
f753f8 BL ParseCardInst b69598
f7543a BL Inventory.AddCard ae9238 ; h=1
```

Afterwards it pushes that same whole card object into the UI callback vector
atf7549e..b0. The popup still receives a vector with one object, so an object
wire shape does not prevent the single result display.

## Why array shape produces exactly the observed crash

ParseCardInst constructs a Card and invokes CSRCard::parse atb695da.
Card.parse first reads inst_id8680c6 then ref_id868118; ref_id is moved to
Card+5c86812a..166 unchanged. It does not convert003 intoC003.

The custom const JSON object-key operator7930f8 checks type==1(object) at
793104..108. An array therefore goes to its static empty/null JSON fallback
7931be, rather than selecting its first item. Missing inst_id converts to0
and missing ref_id converts to empty string throughfrom_json728ba4.
Inventory.AddCard then looks up empty Card+5c, constructs a bundle with a null
CardInfo and IsTrainingCard dereferences that null at87888e. A live reference
map containing003 does not help an empty lookup key.

The source discrepancy is explicit atstate.ts1346..47: cnt=card.length and
card is always the mapped array. For a one-card award this givescnt1/card:[...].
The native's single branch expectscnt1/card:{...}.

## Reconstructed safe response selection

```text
granted>1: cnt=granted; card=all result objects (array)
granted==1: cnt=1; card=the sole result object
granted==0: cnt=0; card=null or omitted
```

A refusal cnt0/card:[] has the same array-as-one-card bug, because[] is nonnull
and enters ParseCardInst. Null/omission is guarded atf753e4..e8. An existing
non-success refusal envelope can instead preserve its established rejection
handling; do not invent a result code merely to avoid the shape correction.

Correcting the response does not authorize another grant. Reloading the
preserved account/inventory can recover its already-owned003 separately.
Meaningful verification should cover single object, multi array and zero-null
native shapes; no reference-version alias, reinstall or null-pointer mask.

## Object-base correction, corroborated by live map

`card-map-confirmed-second.txt` shows count4, keys001/002/003/004, nonnull info
pointers, C001/C002/C003/C004 atinfo+c. SetCard's raw allocation includes
its shared-control header+c; actual CSRCardInfo begins atallocation+c.
Thus actual info+0 is id andinfo+c is res_prefix. The previously documented
info+c ID claim confused allocation and object bases and has been corrected
in card-ref-map-registration.md. Actual training byteinfo+3c remains correct.

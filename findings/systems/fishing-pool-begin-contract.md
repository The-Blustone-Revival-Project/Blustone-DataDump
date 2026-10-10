# Fishing pool and Begin parser contracts

2026-10-05. Read-only original ELF and completed parent decomp/key dumps:
ghidra-fishing-pool-begin.txt, ghidra-fishing-pool-callback.txt,
ghidra-fishing-pool-keys.txt and ghidra-fishing-begin-keys.txt.
G addresses are Ghidra; ELF=G-0x10000. No implementation or native test.

## Pool receiver and collection

RequestPool Gb2b31c creates the RequestPool$_4 TASK_READY E0 continuation using
LDRb2b728/ADDb2b730. Original ELF VT2153c88, offset-to-top0, RTTI2153cb4,
invoke+20=b224c9 proves actual receiver **Gb324c8**. Earlier Gb3219c merely
stores decoded HTTP JSON; it is not the membership parser.

Actual receiver GetResultCode1 gate b324ea..b324f2 reads its captured decoded
response at closure+8 and CSRMFishing pointer at closure+10. Success sets
Fishing+45 byte1 (b324fa), then indexes **full response.ret_data**
(LDRb324f6/ADDb32500) and iterates its rows. No pool/list nested wrapper appears.
Each row has **lure_id STRING** (ADDb32596, from_jsonb325d6) and **fish_id STRING**
(ADDb325a4, from_jsonb325ec). The receiver builds map<string,vector<string>>
at Fishing+30 with end anchor+34. Multiple rows for one lure append fish IDs.
No destructive refresh/reset claim follows from this insert/append path.

Transport is RequestPool's original literal **fishing/GetFishingPool**, without
a leading slash at ADDb2b578, plus auth5. The compatible nonempty body is
ret_data:[{lure_id:"<genuine lure ID>",fish_id:"<genuine fish ID>"},...].
Those strings are shape placeholders, not recovered or proposed identities.
Original membership IDs and fish-definition linkage remain unknown.

## Begin object bases and assignment widths

**ParseBegin Gb27d34 receives the full response**, not ret_data alone.
ADDb27d48 extracts ret_data into r5/pbVar2. Its optional achievement child is
passed to Achieve.ParseAchievementsElement8481c4. All scalar keys below are
indexed on that same ret_data object; receiver destination is the pointer
loaded from **Fishing+28**, not the Fishing object itself.

- log_id → pointee+44, **32-bit uint** STRb27db6. Integer JSON inputs use
  the low32 bits; string/double branches convert, so this is not a provedu64 log.
- init_val → +48, float32 VSTRb27e28.
- max_val → +4c, float32 VSTRb27e9c.
- dec_val → +50 and +54, float32 assignments (first atb27efa and alternative
  conversion paths, second b27fa2). These are two stores from the same key,
  not two JSON keys or evidence of an array.
- inc_val → +58, float32 VSTRb28016.
- dec_val_on_burn → +5c, float32 VSTRb280b4.

Ranges are **nested objects**, each directly under ret_data. The parser first
indexes the range parent, keeps it in r6, then indexes that parent's min/max:

- first_burn (ADDb280bc) → min+78 VSTRb28148, max+7c VSTRb281b8.
- burn_cool (ADDb281c0) → min+80 VSTRb2824c, max+84 VSTRb282bc.
- burn_dur (ADDb282c4) → min+88 VSTRb28350, max+8c VSTRb283d0.
- wait_time (ADDb283d8) → min+60 VSTRb28466, max+64 VSTRb284d6.

For wait_time the decompiler reuses pbVar2 and raw r5 for the newly indexed
range object. Its subsequent min/max reads are therefore still nested, not
top-level aliases. All listed range endpoints are float32 destinations, despite
the JSON scalar parser accepting numeric/string/bool conversions. Omitted/null
members have branch-specific skip/default behavior; no balanced fallback
configuration or complete mandatory-field policy is proved here.

Finally b284da..b284e6 copies **16bytes** from *(Fishing+3c)+5c to
*(Fishing+28)+68. Begin therefore also depends on an existing cached source
pointee at Fishing+3c; returning the listed server fields alone does not prove
the client has all prerequisites. The meaning of that copied block is not
assigned from offsets alone.

No timer units, random sampling policy, difficulty values, lures/costs, original
fish statistics or catch rewards are inferred. Parent's offline four-original-
pack preparation is separate from proving native registration or entry.

## Cached-source identity and writers closed

Original constructor **Gb26514** zero-initializes the shared pairs and calls
**ChangePlace Gb267f0 atb265d2** with exact literal **common1**
(LDRb265c4/ADDb265c6). ChangePlace clears Fishing+3c/+40 atb26800, calls local
**CSRStaticData.GetLoadFishPlaceInfo Gf419b4 atb26838**, allocates0x78bytes,
copies **0x6cbytes** from that local result into allocation+0xc atb2685e,
then writes payload/control to **Fishing+3c/+40 atb26866**. Wrapper vtable
**ELF2153d64**, resolved through original LDRb26846/ADDb2684c and GOT pointer,
has RTTI explicitly **shared_ptr_emplace<CSRMFishing::COMMON_INFO>**.
GetCommonInfo **Gb2f0fc** independently loads that same pair and retains it.

ChangePlace tailcalls **ResetFishing Gb2951c atb268a6**. Reset clears
Fishing+28/+2c atb29548, allocates0xa0bytes with a0x94-byte payload at+0xc,
and stores payload/control into **Fishing+28/+2c atb295e2**. Its original
vtable **ELF2153d8c** (LDRb2957e/ADDb29586 through GOT) has RTTI explicitly
**shared_ptr_emplace<CSRMFishing::FISH_INFO>**. This proves receiver/object
bases rather than assuming class identity from allocation sizes.

Therefore ParseBegin's final16-byte copy is **COMMON_INFO+5c..6b into
FISH_INFO+68..77**. Its source is a local place-settings copy, not a missing
server fish-reference field. Ordinary constructor setup populates both pairs;
the availability/content of common1 in the native local settings table is a
separate runtime prerequisite. No missing-record fallback or original tuning
units are inferred. If full transitive decomp is wanted, exact parent targets
are ChangePlaceb267f0 and ResetFishingb2951c; existing local loader evidence
is ghidra-fishing-local-loader.txt.

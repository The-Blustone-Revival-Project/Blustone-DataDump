# Search partner entry: available templates versus used-helper IDs

2026-10-05. Read-only ghidra-search-partner-contract.txt/-keys.txt and original ELF Thumb. No device/Ghidra/source/runtime operations. Parent reports native partner list empty, guide finger at origin and pre-Begin process death; no guest ARM fault PC was identified in this lane.

## GetHelperList exact response

Search uses **CSRSyncExplore::RequestSupporters G923b9c** → **ReqSupportersCB G924154**, posting **/abyss/GetHelperList** (LDR923dd0/ADD923dd2). Request contains the standard five auth fields. Callback indexes successful envelope.ret_data:

```json
{"friend":[],"virtual":[]}
```

friend[] entries are numeric64 IDs fed into **CSRPlayData.AddExploreHelper** at9242ee. virtual[] entries are strict string IDs fed into **AddExploreVirtualHelper** at92435c. Optional achievement is parsed only when nonnull. Do not send a bare array, full defender profile, card[] or virtual helper records here.

**These are usage flags, not available-partner definitions.** AddExploreVirtualHelper b702c0 stores ID→byte1 in PlayData's map. Arrange checks **IsFindExploreVirtualHelper** and makes the thumbnail availability flag its inverse (decomp lines767..769). Consequently adding an arbitrary nonempty virtual ID cannot create a row and may mark a real template unavailable. Empty friend/virtual is the correct no-used-helper fixture but cannot populate a missing reference table.

## Concrete reference writer seam

Arrange **Ge2c1f0**, decomp674..675, gets CSRDataMgr.GetReferenceData and calls **CSRRefData.GetVirtualFriendList Gde4e24**. Getter returns **reference+0x374**. It iterates that template map, copies the stored CSRCard and reference ID/name into partner THUMB rows, then applies used-helper availability flags. Friend/guild branches use their own existing managers and member profiles; don't manufacture those accounts merely to fill the tutorial.

**Correction: the containing writer is CSRRefData::SetAbyss Gde2ed4, NOT SetExtra.** The earlier GetExtra attribution came from wrongly treating a broad disassembly range as one function; it is retracted. **LDRe3996 / slotde39f0 / ADDe39a2** resolves virtual_friend inside SetAbyss. **CSRRefData.PostProcessVirtualFriends Gde4200** is called by **PostProcess Gde527e atde52a0**, after CardInfo.PostProcess atde5288. It is a separate reference-to-card postprocessing dependency, not the GetHelperList callback.

Parent recovered the containing SetAbyss function and PostProcessVirtualFriends. **ReqAbyssCB Gf84dc0** preserves full parsed JSONparamr3 inr4, checks success, gets reference data atf84dd8, then MOVr1,r4 atf84ddc and tail-branches **f84de2→SetAbyss de2ed4**. SetAbyss indexes **ret_data** (LDRde2ef0/slotde324c/ADDde2ef6), then **ret_data.virtual_friend[]**. Native URL vocabulary retains **/reference/GetAbyss**. This closes callback→writer→parent; request registry pairing is separate if not already recovered. Do not add this table to GetExtra.

## Native guide and Begin distinction

**CSRSceneFindShardSelSupporter::SetTutorial Ge2ffe4** scans arranged groups at scene+678/+67c. It requires **group.type==2** (e300c0) and a THUMB row **availability byte+28==1** (e300ec). It then copies that row, searches the corresponding named drawable and focuses it (FindCastByName e301bc; unguarded virtual rectangle access e301c8). Empty groups leave no valid selected thumbnail/name; this explains a concrete broken guide dependency, but the visible origin finger alone does not prove the live fault instruction.

Ordinary Begin control is **BT_NEXT**, OnButtonClick Ge2baf0. It reads selected Search target's **helper-card shared_ptr at PLAY_DATA+44/+48** (e2bb36). That helper null is explicitly guarded (e2bb70); missing/emptyref helper takes the common confirmation popup. Therefore an empty partner list is NOT by itself proof of an unguarded helper-null crash in this button handler.

**RequestStartExploreCardPiece Ge2be88** separately dereferences **Target→INFO+68→type** at e2beae/e2beb0 without null guard. INFO.type2 also checks target.end_datetime against server time; expired target takes timeout flow. Otherwise it eventually invokes RequestBegin90eec0 at e2c004. A missing selected Search target/INFO is a distinct pre-HTTP null path. Native RequestBegin in turn needs a valid selected target, helper/caller state and INFO reference. Keep these hypotheses separate until an actual ARM PC or bounded target/helper observation distinguishes them.

## Smallest next control

Recover and publish one valid known-art virtual_friend TEMPLATE in the Abyss reference response; keep used-helper friend/virtual arrays empty; let the native guide select an available row and populate the original target helper through normal UI. No owned hunter grant, fake guild member, guide clear, direct scene jump or automatic Begin is implied. Verify list/guide/selected helper first, then stop before any unsupported Begin transaction.

The current user's ownership/balances/progression are preserved; this lane did not alter capsules, costs, jobs or state. The reported crash happened before /explore/Begin, so it is not evidence of a Begin server response failure.

## Flat helper row closure

Original late SetAbyss parses **id:string**, **nick_name:string** (not nickname), **user_exp:number**, **card_ref_id:string**, **card_exp:number**. Exact key pairs: id LDRde3a48/slotde3db8/ADDde3a52; nick_name de3a56/de3dbc/de3a58; user_exp de3a5c/de3dc0/de3a5e; card_ref_id de3a6c/de3dc8/de3a6e; card_exp de3a72/de3dcc/de3a74. The intervening GOT/vtable literal atde3a62 is NOT another JSON field.

It constructs a CSRCard and passes the **SAME FLAT virtual_friend row** to **CSRCard::parse G8680a4 atde3bb2**: row pointerr8 is moved tor1 atde3bb0. There is no nested card/base/profile object. It then overrides the card reference with **SetRefID(card_ref_id) atde3c18** and card EXP atde3c1c. Row must therefore include the normal complete card-instance fields already used by bootstrap.cardInstance, with ref_id matching card_ref_id, plus the five helper fields above.

Minimum candidate construction, not original data:

```text
ret_data.virtual_friend = [{
  ...cardInstance(0, "004", 1),
  id: "local_helper_004", nick_name: "Local revival partner",
  user_exp: 0, card_ref_id: "004", card_exp: 0
}]
```

All normal instance fields must be expanded onto this row; the spread notation is an implementation description, not literal JSON. 004 is an existing published/downloaded fixture. The helper ID/name/rank/EXP are local choices; do not claim original partner fidelity. It is stored in the reference's virtual-friend map, not added to owned inventory. Keep /abyss/GetHelperList virtual[] empty so it is initially available.

PostProcessVirtualFriends de4200 calls CSRCard.Load on each template and invokes its original initialization before computing combat point. It runs after reference/card postprocessing; a JSON parse alone is not proof that template card art/stats/skills resolve. Existing cardInstance fields and published compatible card references avoid introducing a new unmodeled character, but native helper row/group/guide rendering remains a required control. The first successful request can still expose another guide group/selection dependency; no Begin is authorized solely by this parser proof.

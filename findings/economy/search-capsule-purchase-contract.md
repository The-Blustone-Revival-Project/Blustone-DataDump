# Search capsule plus opens item details; purchase is not yet proved

2026-10-05. Read-only existing native/reference/shop reports and original ELF Thumb/CRC evidence. No purchases/grants/source/Ghidra/adb edits.

## Exact Search plus path

Search UI XML `KO/SEARCH/SE_MAIN` names the capsule button **BT_TK_SE**. StandardCRC32 is **0x559e094d**, matching SceneFindShard::OnButtonClick Ge248e2..ec. This branch constructs **CSRPopUpItemDetail** atGe248f2, fills the item reference **AIRSHIP_TICKET** atGe24b02..0a (14bytes), calls its virtualInit Ge24b16, pushes it through ModalHandler. The plus is **item-information/acquisition entry**, not directly a payment request or ShopBuy popup.

Do not confuse the nearby confirmed purchase with capsules: SceneFindShardConfirm::OnButtonClick Ge1e35e matches **BT_BUY_STP**, looks up literal **STP1** atGe1e380/Ge1e45c, reads global-item providecount/price, opens ShopBuy Ge1e4a2. STP1 is a separate resource. This branch does not prove AIRSHIP_TICKET purchases.

Exact capsule ID remains AIRSHIP_TICKET from Search Inventory.GetInstItemCnt. Its originaluse_type/acquisitionprice/global row is unknown; current use_type0metadata is an explicitlocalfixture. The original plus flow relies on ItemDetail's trace/source entries to expose available acquisition links; emptyreference trace[] alone does not create a paidcapsuleoption.

## Candidate local Manda purchase seam, not proven original capsule route

The recovered generic **/shop/BuyGlobalItem** transport supports target_ref_id,price_type,item_inst_id,qty plus accountmetadata. Native price_type1=Manda. Existing shop-fuel-contract.md proves full GetItem base/global schemas and callback itemgrant support. This is a **candidate reuse seam** if an actual native acquisition/purchase path selects AIRSHIP_TICKET; no currentproof permits assuming it.

Reference requirements if deliberately reconstructing such a localpurchase:

- base itemidAIRSHIP_TICKET with strictstrings name/desc/thumbnail_id/effect andnumericrank/use_type/sell_price/collect_qty. Original metadata staysunknown; don'tgiveitAPuse_type1/BP2/trace3 merelytosatisfyknownneighbors.
- matching global_item.item_id,provide_qty,buy_limit,type,ticket_ref_id/ticket_qty, orderedexact buy_cnt tiers inprice_list[{price_type,buy_cnt,price}]. Price/amount/reset/typewouldbelocalpolicy, notoriginal.
- persisted GetItemInven ordinary ownedcapsuleinstance andglobalbuycounters mustagree; useexistingstableiteminstance allocator toavoidSearchhelper/card/otheritemIDcollisions. No fakebalance-onlycapsulegrant.
- receipt ret_data.user.iap hasscalarpaid/freecurrentbalances; target_inst hasitem_id/price_type/buy_cnt.cur. Capsulequantity is an actualordinaryitemreceipt inret_data.item[] usingthealreadyrecovered ref_id/inst_id/qty/added contract. Positivequantity AddItem semantics andpurchaseUIcallback mustbeverified for thisordinaryitem beforeliveenablement; AP/BP-onlyrefillreceipt is insufficient.

Current handler state.buyFuel onlyacceptslocalAP/localBP. Extendinga serverbranch wouldnotmakeplusnativeMandaacquisitionappearbyitself. Avoidinventingtrace.type/source_id shopalias or claiminganoriginalpaidcapsuleoffer.

## Smallest next native reads

Existing `ghidra-training-trace-gateway.txt` includes ItemDetail::OnButtonClick **Gcc6630**, traceacquisitionhelper **Gcc7b88** and SetTrace **Gcc7fdc** symbolicresource consumer. InspectactualAIRSHIP_TICKET trace/source metadata andmatchingbutton toprovewhethernativegoesintoashop,normalstage,oronlyinformation. Its current0capsules/guideblock doesnotestablishoriginalpaidacquisitionexists.

Parent minimal decomp: **SceneFindShard::OnButtonClick Ge24880** firstBT_TK_SEarm (directproof), **ItemDetail::InitItem Gcc3cf8/SetTrace Gcc7fdc** and existing OnButtonClickGcc6630 acquisitionbranch. Ifactualshopentryfound, **ShopBuy::OnButtonClick Gd43eac** nestedconfirmationcallback and **CSRSyncShop RequestBuyItem Gf87934/Gf891c4** or **RequestBuyGlobalItem Gf89ca8** as actuallyselected; don'tmapgenericShopBuytoBuyGlobalItembynamealone.

This identifies a concrete known native entry and candidatecompatiblepaidledgerwithout asserting missingcapsulepurchasebindings. No originalprice orcapsulepurchase, extraUIroute, grantorstatechange was performed.

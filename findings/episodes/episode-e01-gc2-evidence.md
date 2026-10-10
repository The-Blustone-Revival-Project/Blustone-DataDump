# E01 chapter reward GC2: exact declaration, missing item semantics

2026-10-05. Bounded read-only original S01 export, existing episode-reward-materials.md, preserved final localization/help and recovered public art inventory. No server/runtime changes, inventory grant or economy substitution.

**Original quantity is known:** preserved final public R_EPISODE.jet named SEASON1 defines E01.reward exactly as **`{"item":[{"ref_id":"GC2","qty":3}],"free_iap":0}`**. This is an original shipped chapter reward declaration, not a guessed historical drop rate or a local fixture. It is separate from an authenticated claim receipt and full item-reference semantics. No rupee/Manda/card replacement is justified.

**GC2's inventory/recruitment identity is partly proved:** original Lottery.SetCurrency Ge3e90c/Ge3e90e constructs exact GC2, then Inventory.GetInstItemCnt atGe3e91a. OnClickRequestGachaByCoupon Ge40020 constructs it again atGe4013e..Ge40146. Therefore it is a real owned Lottery coupon reference; it is not merely an Episode display marker. The exact coupon tier, eligible hunter pool, one-coupon redemption quantity, use_type/effect/rank/collect_qty/name/thumbnail are **unrecovered** in the current evidence.

Final UI_TEXT_RO has generic phrases **Recruit Hunters using 10+1 requests**, **You do not have enough request scrolls**, and **Look, Captain! It's an Recruitment Request!**. None embeds GC2 or supplies a proved ID→label mapping. Final HELP_DATA CONTENTS6_7 mentions Request scrolls among historical Search loot; it likewise does not identify GC2 or redeemability. That help can lag later loot changes and must not supply GC2 grant policy.

Original UI_ITEM has IT_HQ/2HQ/3HQ/4HQ/3SE/4SE and request-like art families as already inventoried in episode-reward-materials.md. **No recovered GetItem row binds GC2 to one of them**. Art availability cannot determine rarity/pool/type. The preserved13-table export has no ITEM_REF and no exact GC2 key/value; inspected recovered-reference exports have no original full GC2 item definition. Do not fabricate an inert use_type0 row to conceal missing redemption or choose a thumbnail from the numeral2.

## Precise remaining evidence candidates

The best primary data would be an **original final-client /reference/GetItem ret_data.item[] record with idGC2**, plus original Lottery coupon request/receipt. Required native reference fields are id,name,desc,thumbnail_id,effect strings and rank,use_type,sell_price,collect_qty numbers (SetItemGaefe10 evidence in shop-fuel-contract.md). A readable original cache/export or decryptable authorized archived response would settle this much more directly than generic help; current supplied encrypted2017 packet captures are version-specific and not numeric GC2 proof.

The narrow parent-only native target **CSRSceneLottery.OnClickRequestGachaByCoupon Ge40020**, and the branch/request callback it actually calls, can close which coupon GC2 supplies and its explicit wire fields. That can establish behavior without pretending it recovers original metadata/economy values. No Ghidra was used by this lane.

If seeking public primary prose/visual confirmation, exact candidate searches are **`site:bs.visualshower.com "Recruitment Request" "scroll"`**, **`site:bs.visualshower.com "GC2"`**, and an archived official request-scroll guide/update with an in-game coupon panel and attributable client version. These are **proposed source queries, not findings**; a generic "Recruitment Request" result still needs an ID binding before it becomes a GC2 definition. No external value, pool, reset or amount is claimed here.

**Conclusion:** original E01 GC2x3 is exact, but a safe functional GC2 reference/redemption is not yet reconstructed. Keep E01's unsupported reward refusal until that material contract is closed; no grant, substituted reward, alias or source patch was made.

# Fishing price and sale receiver contract, original native follow-up

2026-10-08 root-only read-only original Ghidra, noanalysis; no live native calls,
state/source/profile changes or catch/grant. Complements fishing-catalog-next-
contract.md. This closes receiver fields/mutations, not fish IDs or economics.

Exact PC-relative LDR/ADD keys in ghidra-fishing-price-sale-keys.txt:
ParsePrice Gb2e438 fullJSON.ret_data numeric array rows with strict string
fish_id, numeric b_price/s_price/g_price uint32. Optional achievement lookup;
existing fish-keyed map upsert established in retained pool-begin decomp. No
original price values, legal grade-domain completeness or production pools.

ParseSell Gb2b018 receives a sale JSON object (not itself a full-envelope
ret_data lookup): optional achievement goes to ParseAchievementsElement;
user.gold is optional. If nonnull, gold.prev/cur numeric conversions yield
uint32, fishing object+0x80 stores cur-prev; PlayData+0x154 is assigned cur.
Absent gold leaves the stored sale delta0 and does not overwrite the wallet.
The sale delta is uint32 subtraction; this receiver does not validate prices,
old balance, ownership or wraparound. Those remain server responsibilities.

item must be numerically indexed array of rows inst_id/qty. Original symbol
CSRInventory.RemoveItem(unsigned long long,unsigned int) Gaec5f4 disproves
truncated decompiler prototype. Exact Thumb caller Gb2b1be ldrd r11/r5 takes
uint64 ID; Gb2b262/264 moves them to alignedr2/r3; Gb2b266 stores uint32qtyr10
to stack0, then blGaec5f4 atGb2b26a. Do not truncate instances to32bits.
This is a removal DELTA, not a remaining-quantity assignment. RemoveItem finds
the native inventory tree by64bitID and atGaec6da loads node+0x18 quantity,
subtracts stackqty and stores it. No clamp or erase is present on that found
branch. Missing item follows diagnostic trace and leaves that tree unchanged.
Exact raw listing retained ghidra-inventory-remove-item-insn.txt; decomp in
matching txt, sale caller in ghidra-fishing-sale-insn.txt. A repeated additive
item receipt would remove twice; native does not make server retries safe.

Finally sale JSON sell_result goes to CSRMFishing.UpdateInven Gb2eb9c. Its
complete nested fish inventory shape and transitive semantics are NOT closed
by this unit; do not substitute item rows for sell_result or infer fish removal
from name alone. EndWithSell's optional ret_data.sell calls this ParseSell per
retained settlement audit; standalone SellFish callback full wrapping/success
routing is a separate unverified caller boundary.

Current fishing routes except GetInven/GetRecord explicitly refuse2001. Keep
that policy until original fish GetItem rows, identity bindings/catch settings,
price values and sell_result/caller contracts are reconstructed. A price array
shape plus gold receipt cannot justify a invented catch, bait debit, tutorial
Clear27/2 success, zero-value sale or reclassifying incomplete fishing as working.

# E18 RP1 and gold settlement boundary

2026-10-05. Read-only original ELF, retained shared-parser decomp and public
S01 catalog. No Ghidra, device, source/account edits or reward claim.
Code addresses are Ghidra; ELF=G-0x10000.

Shipped E18 reward is **item[{ref_id:"RP1",qty:100000}], free_iap0**
(EPISODE_S01.json). Native **RP1 is a gold display identity**, already proved
independently: LoginBonus.ParseLoginBonusRef Gf4ae7c reads a separate gold
amount and synthesizes RP1 display rows (LDRf4b5dc/ADDf4b5de). This is positive
currency-display evidence, not an original GetItem reference or settlement DTO.

Episode.ParseReward **Gb1ca7c** calls SyncItem on ret_data.item atb1cada,
then SyncUser on ret_data.user atb1cb0e. SyncItem's ordinary rows require
inst_id/ref_id/added and call **Inventory.AddItem Gaec508**. Original AddItem
has no reference-name dispatch: it searches instance identity, creates a generic
row through SetItem at**aec5aa**, or adds quantity at**aec5c0** and stores it
at**aec5c2**. Sending RP1 as an ordinary additive item receipt therefore does
not establish a gold wallet credit.

The recovered direct wallet path is:

```text
ret_data.user.gold = {prev: ACTUAL_BEFORE, cur: ACTUAL_AFTER}
```

**SyncUser Gb7047c** indexes gold at ADD**b70662**, then its prev/cur children
(ADDb70674/b70684; later conversion reads b70694/b706e0). It writes the
absolute current balance as **uint32 to PlayData+154 atb7072a** and stores
the calculated cur-minus-prev display delta at SRREWARD_INFO+0c, **b70730**.
These are nested user.gold fields, not scalar gold or item.qty/added aliases.
Gold-only settlement can use item[] with the mandatory neutral achievement
receipt; user:null is only correct when no wallet change occurred.

No original GetItem RP1 row has been recovered in the retained exported table
evidence (episode-reward-materials.md). Original Episode HTTP settlement for
E18 is also unavailable. Mapping the recovered RP1 display quantity to a gold
wallet delta is a supported **explicit local server interpretation** of those
two proven mechanisms, not proof of the historical response/policy. Native
chapter eligibility, grant authentication, marker+wallet atomic persistence,
overflow and replay policy require separate implementation review. Do not
publish a normal RP1 inventory fixture or original economy claim merely to
make this currency display line claimable.

Evidence: episode-reward-contract.md; episode-reward-materials.md;
ghidra-login-bonus-contract.txt/-keys.txt; ghidra-find-shard-sync-user.txt;
fresh original AddItem and SyncUser Thumb instructions at the addresses above.

## Replica implementation

Parent implemented only the exact E18/RP1x100000 declaration through the
gold receipt above. This is explicitly replica settlement policy; it does not
recover original Episode HTTP data or RP1 item metadata. Every descendant story
must be recorded cleared, and authentication/owner isolation remains required.
The wallet and reward marker persist together; storage failure rolls both back.
uint32 overflow refuses without consuming the marker. Settled retries use
item[]/usernull and never credit again; RP1 is never made an inventory stack.

Focused tests cover read-only/parent-only/partial-clear refusal, exact original
quantity, full-clear settlement, overflow, storage failure, unchanged inventory,
restart/replay and another account. Full suite and build pass. No live grant,
server restart or native chapter/reward acceptance occurred.

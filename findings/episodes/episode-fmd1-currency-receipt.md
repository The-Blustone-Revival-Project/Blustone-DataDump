# E02 FMD1 and free-Manda receipt

2026-10-05. Original ELF and retained ghidra-find-shard-sync-user.txt,
login-bonus keys/decomp, Episode reward parser and public S01 catalog only.
No Ghidra, device, source or account writes. Addresses use Ghidra coordinates.

## Identity versus settlement

Shipped E02 reward is **FMD1 quantity30**, with catalog free_iap0. Native
LoginBonus.ParseLoginBonusRef Gf4ae7c reads a separate free_iap amount and
synthesizes **FMD1** display identity (LDRf4b5ec/ADDf4b5ee), as already recorded
in episode-reward-materials.md. This proves free-Manda display meaning, not
an original FMD1 GetItem row or historical Episode settlement response.

Episode.ParseReward **Gb1ca7c** receives ret_data, sends its item child to
SyncItem atb1cada and its **user child** to **SyncUser Gb7047c atb1cb0e**.
This is the shared wallet parser, not a gacha-specific receipt inference.

## Exact wallet fields and writes

The pair receipt is **ret_data.user.free_iap {prev,cur}**, with numeric balances.
free_iap literal ADDb70736; nested prev/cur ADDb7074a/b7075c, then conversion
reads b7076e/b7080e. Missing/null pair or endpoints skips this branch. The
current value converts to **uint32**, is written absolutely to
**CPVDataMgr+0xa0 atb7085c**, and cur-minus-prev becomes returned
**SRREWARD_INFO+0x1c atb70864**. Positive nonnegative integral wire balances
avoid relying on permissive string/bool/double conversions or truncation.

Paid currency is the separate **ret_data.user.iap {prev,cur}**:
iap ADDb7086a, prev/cur b7087c/b7088c (later conversion b7089c/b708ee).
It writes **CPVDataMgr+0x9c atb7093c**, display delta **+0x18 atb70944**.
An earned free-currency receipt should preserve paid currency and report only
actual persisted changes.

The same parser additionally recognizes optional scalar **user.iap_qty**
(ADDb7094a) and **user.free_iap_qty** (ADDb709a0). If present, these later
branches overwrite the same wallet fields (b70996/b709ec) and returned reward
slots (b7099a/b709f0). They are not additive aliases. Original TBB null entries
atb7095e andb709b4 both contain byte32, targeting **b7099e** and **b709f4**:
omitted/null scalar fields skip their writes. Therefore a pair-only receipt
is supported; do not send conflicting pair/scalar balances.

## Limits for an E02 implementation

Ordinary SyncItem/Inventory.AddItem does not convert a reference stringFMD1
into wallet credit (episode-rp1-gold-receipt.md documents the generic item path).
Use an empty additive item receipt for a genuinely wallet-only transaction;
the Episode callback also requires the established neutral achievement fields.
user:null would skip the wallet change and is not a free-currency grant.

Catalog quantity30 alone does **not** recover the original E02 HTTP settlement.
Current standard recruitment uses **direct wire/display units**, with single30
and eleven300; no multiplication or division by1000 is proved. The native
wallet display passes paid/free balances directly to to_string<unsigned>.
Converting FMD1 display quantity into a free wallet
reward is an explicit local server policy using the proven currency parser,
not a reconstructed historical response. Original eligibility, economics and
redemption metadata remain unresolved. No grant, native popup or wallet change
was tested in this lane.

**Correction, 2026-10-05:** My accompanying parent message's1000-scale claim
was a stale interpretation and is retracted; no supporting factor1000 native
instruction was identified. recruitment-price-currency.md proves actual
StaticData+14=30 and+c=300, purchase prices passed directly atbb54f6..f8,
and wallet components directly formatted atbb51c2/bb51d0/bb51de..e2. Current
game.ts defaults agree. An explicit replica-local E02 free balance credit30
in those same units is coherent with this evidence; its original historical
HTTP mapping and eligibility remain unknown. No saved wallet should be rescaled
from the retracted claim.

## Replica implementation

E02's exact FMD1x30 declaration is now settled as a30-unit free wallet credit
through user.free_iap{prev,cur}, with no conflicting scalar aliases or FMD1
inventory row. This mapping is explicit replica policy; it does not reconstruct
the original Episode server response. Every descendant story must be recorded
cleared. Authentication, uint32 capacity, wallet/claim-marker rollback, durable
restart and neutral duplicate receipts follow the E18 currency settlement path.

Focused tests verify read/partial-clear refusal, exact credit, unchanged paid
currency/gold/items, overflow, save failure, restart/replay and another account.
Full suite/build passed. No live account credit or native popup/claim test.

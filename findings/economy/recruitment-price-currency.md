# Recruitment prices and paid/free currency contract

2026-10-04. Read-only original-library/current-source/preserved-guide inspection.
No adb/Ghidra/client/server edits or retroactive balance changes.

## Recovered standard prices: single30, eleven300, directly in wire units

CSRDataMgr::Init8b1d60 allocates the shared StaticData at8b22be.
The raw allocation includes the shared-control header; actual StaticData starts
raw+c at8b22d0. At8b22ea..f6 it copies the constant16-byte vector from
Ghidra8b2680 into raw+14. Its little-endian uint32 values are:

```text
[100, 300, 11, 30]
```

Therefore actual StaticData fields are+8=100,+c=300,+10=11,+14=30.
At8b22ec r1=1;8b22fe stores it at raw+24, i.e.actual+18=1.
Do not treat the vector's first100 as a wallet divisor merely because it is100.

CSRSceneLottery::OnClickRequestGachaByMandae40824 uses:

- standard10+1 button branch: price=StaticData+c at e408d8;
  count=StaticData+10 at e408e2 ->300 for11.
- standard single button branch e40bb4: price=StaticData+14 at e40bc2;
  count=StaticData+18 at e40bcc ->30 for1.

These feed PurchaseConfirm::SetData at e40a3c..40 with price in r2.
PurchaseConfirm bb1f68 saves that integer price in r8, and its common quantity
text path bb54f6..f8 passes r8 directly to **to_string<unsigned>**.
There is no divide100 conversion on this proven standard purchase path.
The native price values are30 and300, agreeing with the observed buttons.

## One total wallet, paid/free components

Before confirming standard Manda recruitment, e409c6 obtains CPVDataMgr.
e409ce loads its two adjacent uint32 wallet components at+9c/+a0;
e409d2 sums them; e409d4 compares price against the **sum**. This is not
an affordability test requiring each individual balance to cover the full cost.

PurchaseConfirm's wallet information independently shows the same semantics:

```text
bb51c2 -> CPVDataMgr+a0 -> to_string unsigned       free component
bb51d0 -> CPVDataMgr+9c -> to_string unsigned       paid component
bb51de/51e2 -> (+9c)+(+a0) -> to_string unsigned    total
```

The callbacks read numeric response fields user.iap_qty and free_iap_qty and
write+9c/+a0 respectively (GachaPremium f750c6 onward/f75112 onward).
The response contains updated balances, not a recovered dual debit instruction.
No separate named GetTotalIAP getter was found in the inspected symbol table;
the exact inline integer sum above establishes its behavior without a name guess.

Thus the current server rule cost<=paid AND cost<=free, followed by subtracting
cost from both, contradicts the inspected affordability and total semantics.
A coherent debit should reduce **paid+free by exactly one price**, keeping both
components nonnegative. It should allow a wholly-free or wholly-paid funded
wallet and a combined wallet crossing the component boundary.

## Consumption order remains unknown

The native client doesn't choose which component the server consumes in these
inspected paths: it receives updated balances. A bounded plaintext search of
the preserved Blustone Guide FAQ found no paid-Manda/free-Manda consumption
priority assertion. Do not describe either free-first or paid-first as recovered.

Free-first is a reasonable **explicit local policy fixture** if needed:

```text
freeSpend=min(free,price)
paidSpend=price-freeSpend
require price<=free+paid
```

The inverse paid-first policy would also satisfy the native sum contract.
Original priority needs further preserved response or authoritative policy
material; it cannot be inferred from the order of JSON fields or memory offsets.

## Recommended current behavior and preservation boundary

Use recovered standard single30 and10+1/11-card300 for standard Manda draws.
These prices are native constants, stronger evidence than the previous
fixture30000 derived from an on-screen balance change. Keep nonstandard
banners, coupons and arbitrary draw counts explicitly unsupported or fixtures
until their individual native price paths are recovered. The documented native
button paths establish1 and11; they do not establish a price for counts2..10.

When standard price is affordable, debit once across total and return both
updated component balances. Preserve the recently fixed single-result object /
multi-result array / zero-null shape. For refusals, do not alter wallet or grant.

Do not retroactively refund earlier research purchases, rescale existing saved
components, or invent which historical debits were intended. Their persisted
values are current research state. New pricing and local consumption policy
can be corrected prospectively while recording the prior fixture discrepancy.

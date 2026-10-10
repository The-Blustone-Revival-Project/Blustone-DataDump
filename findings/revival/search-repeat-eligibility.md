# Search repeat eligibility: counted logs and retry credits

2026-10-05. Read-only original Thumb plus parent ghidra-search-repeat-ui.txt. No Ghidra/device/source/runtime operations. This closes the counter arithmetic; original prices/day-reset economy remain unknown.

## Exact counters

Let P be the number of **play_log LOG rows whose INFO.id matches the reference**, R be matching occurrences in **retry_log[] strings**, M be INFO.max_play_cnt, K be INFO.max_retry_cnt, and V be the native VIP retry bonus.

**GetPlayCnt(ref) G90bc18 returns P−R**, not P. It first scans play_log vector+3c/+40, counts matching LOG.INFO.id, then at **90bd22/90bd24** begins an inline scan of retry_log vector+84/+88; increments the matching retry count at90bd46 (and90bdd0 for the memcmp path); finally **SUB r0,FP,SL at90be00** returns play matches minus retry matches. This is original instruction proof, not inferred by the function name.

**GetRetryCnt(ref) G90ba88 returns R**, counting string matches independently. Do not deduplicate retry_log.

**GetCurRemainCnt(ref) G90b9a2** reads max_retry_cnt atINFO+34, max_play_cnt atINFO+30, calls GetRetryCnt/VipRetryBonusCnt/GetPlayCnt at90b9e6/90b9f2/90ba00, then90ba04..90ba10 computes:

```text
base plays already charged = P - R
base remaining             = M - (P - R)
retry quota remaining      = K + V - R
total possible remaining   = M + K + V - P
```

The total expression results from canceling R, which appears inside GetPlayCnt as well as explicitly. Leaving out that subtraction produces the wrong eligibility policy.

## Targeted Retry credit retains completed play logs

Example with M1/K1/V0: after one completed play P1/R0, base remaining0 but retry quota1 and total remaining1. A successful purchased Retry can **retain that play_log row and append the reference once to retry_log**: P1/R1 produces GetPlayCnt0, base remaining1, retry quota0, total remaining1. The next completed attempt appends a second play_log, giving P2/R1, base0/retry0/total0.

Thus **appending a retry credit while retaining completed logs DOES reopen one base attempt**, exactly answering the earlier question. It neither awards a trace/capsule nor fabricates a running job. The original HTTP economics/when a server records the credit are not recovered from this arithmetic alone; returning this snapshot is a compatible local transaction policy when an actual Retry is accepted.

A compatible server should not let R exceed P or sell credit when base capacity is already available; otherwise this unclamped native subtraction can make negative plays or excessive remaining counts. The candidate limits M/K/V must reflect the published reference/VIP data. Active battle replay and transaction idempotency are separate protections, not solved by these counters.

## UI corroboration and Reset invocation

Normal **FindShardConfirm.SetData Gbe1258** calls GetPlayCnt at**be1512**, computes M−GetPlayCnt atbe1516, and elsewhere calls GetCurRemainCnt at**be2070**, enabling its button when nonzero atbe2074..be207e. These distinguish base availability from total remaining potential.

**CSRPopUpExploreRetry.SetData Gc08e6c**, native normal RETRY branch2, records R atpopup+158, limitK+V at+15c, base remainingM−GetPlayCnt at+150, and enables the retry button only when K+V−R>0 (ghidra-search-repeat-ui.txt1293..1305). Its type2 is this popup's RETRY enum, not necessarily the global price_type enum.

The global **CSRPopUpFindShardRetry** (Reset UI) is constructed from **FindShardConfirm.OnButtonClick Gbe558c** at **be6ae0** and **be6c30**. Each initializes the popup then calls its SetData (be6af0/be6c40). Those exact invocation sites are proved; the surrounding branch predicates need containing-function decomp before claiming which visible buttons/normal/shared cases select each. It is not directly created by the already dumped SceneFindShard.OnButtonClick e24880.

SetTimer's separate proof in search-repeat-contract.md establishes cooltime as an absolute server-second deadline and closes this popup if expired. A zero deadline cannot expose a persistent Reset dialog. Normal Reset checks paid+free Manda against reset_price, then submits the global request without ref_id; targeted Retry submits the caller's ref_id and its published quote.

## VIP and global Reset limits

VipRetryBonusCnt G90bb94 gets the current VIP reference benefits and matches exact descriptor **UPGRADE_NUMBER_ABYSS_RESET** (LDR90bbbe/slot90bc14/ADD90bbc0). It parses that benefit value; absent match returns0 at90bc0a. Despite the descriptor name, this value enters the retry-quota arithmetic above. Current published VIP benefits[] make V0; no original VIP quantities are inferred.

Clearing both authoritative play_log[] and retry_log[] in a Reset response would mathematically restore M base plays and K+V retry quota. This is compatible with the global request/no-ref targeting, but **original server Reset actually clearing both, preserving some logs, incrementing reset_cnt, reanchoring the deadline or changing tiers remains unknown**. Both callbacks only call ParseInst on the supplied snapshot; they do not encode those economic decisions. Do not confuse mathematical compatibility with original server fidelity.

Reset should not be inferred to reset used partners or permanent cleared_explore flags, grant currency/materials, change campaign stars, or erase the server's settlement/replay audit. Helpers have a separate used-ID map/GetHelperList contract. Historic community guide says daily counts but supplies no precise numbers/reset prices/calendar rules.

Further narrow parent targets if needed: **GetPlayCnt90bc18**, **GetCurRemainCnt90b9a2**, **FindShardConfirm.OnButtonClick be558c**, **VipRetryBonusCnt90bb94**. Existing RequestRetry/RequestReset callbacks, quote fields and wallet pairs are in search-repeat-contract.md. No original economy, live Retry/Reset or source implementation is claimed.

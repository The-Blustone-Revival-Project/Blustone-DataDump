# Fight Club automatic rank lookup

2026-10-04. Original native evidence, read-only Ghidra project; no client or
private account modification.

`CSRPopUpFC::OnReset` Gc0afc6 calls `RenewalMyInfo`, which invokes
`CSRSyncFC::RequestMyRank` Gf5fb30. Request checks tutorial3/0 >=2, then posts
`/arena/GetMyRank` with app_code, market, pvid and otp. Before reconstruction
this route used the generic compatibility response.

`CSRSyncFC::ReqMyRankCB` Gf600d8 checks result_code==1, reads
**ret_data.rank**, and stores its numeric value at CSRFCPlayData+0x128. It does
not call ParseMe or consume user.battle. The older arena.md route mapping to
ParseMe therefore does not establish this callback's response shape.

Evidence: ghidra-arena-myrank-exact.txt / callback.txt and relocated pool dump
ghidra-arena-myrank-pool.txt. Slot Gf6028c contains 0x00e08819; ADD-PC at
Gf6019e gives base Gf601a2 and string G1d689bb (ret_data). Slot Gf60290
contains 0x00e0f8e4; ADD-PC at Gf601a8 gives base Gf601ac and string
G1d6fa90 (rank). Both strings match native-all-strings.tsv. The automatic
resolver misses these paths after the switch jump table; decompiled callback
and relocated arithmetic supply the evidence rather than a guessed container.

Server now routes GetMyRank through authenticated Arena state and returns
`{rank:1}`, matching the existing Enter profile. Rank1 is an explicit local
single-player fixture, not original global ranking. Lookup does not create a
CASE4 deck, spend BP, change counters or settle a battle. Focused Arena test
checks unchanged state; HTTP smoke test guards against generic fallback.

Native Fight Club popup, automatic request/display and combat remain unverified.

# Original fishing resources: opt-in transport profile

2026-10-05. Offline host verification only; no live server restart, APK change,
client database edit or native fishing acceptance.

tools/fishing-resource-profile.ps1 selects FISHING.jet, FISH_LIST.jet,
MGM_FISH.jet and LEVELING.jet as separate packages. The first three provide
original fishing UI/fish art/CHIR scene resources. LEVELING contains the native
named FISHING configuration. Exact original JSON body and provenance are saved
in analysis/recovered-reference/FISHING_SETTINGS.json and its provenance file;
the original UTF-8 BOM and scalar strings are preserved. These resources do not
supply recovered API fish IDs, catch probabilities, prices or bait item rows.

InspectOnly validates files/hashes without selecting a profile. Normal selection
preserves existing package extras, avoids folding these four into E_NEW and
sets resource/reslist/header stamp1634667. Source the separate Episode profile
first if both areas are needed. This does not start/restart the replica itself.
It is an opt-in experiment; current live split24/1634666 remains unchanged.

The isolated verifier ran:
`npx tsx scripts/verify-episode-cdn.ts --separate --fishing`.
All28 outer packages passed manifest counts/sizes, inner and outer MD5, PKGI1
record offsets, byte equality against source JETs and HTTP range behavior.
The17 added Episode/Fishing originals remain byte-exact. Established E_NEW
remains47 records/46,929,569bytes. Four fishing source files total5,875,629bytes.
Combined profile selection was also checked in a separate PowerShell process:
17 unique extras and stamp1634667; no active server environment was changed.

The verifier rejects --fishing without --separate. No historical folded59
bootstrap is silently reused. Native CDN registration/cache behavior and actual
fishing entry must still be tested after emulator ownership is clear. Empty
owned collection DTOs are implemented separately; this resource preparation is
not a functional catch/sale claim.

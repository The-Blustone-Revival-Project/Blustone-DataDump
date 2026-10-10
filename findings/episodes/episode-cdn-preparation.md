# Episode CDN preparation, 2026-10-05

## Current transport status

The historical folded59 profile below later aborted bootstrap on both +9 and
+10. A preserved46-profile control restored village; exact allocation cause is
unresolved. Do not promote the historical larger profile as working.

An explicit alternative is now prepared:

```powershell
. ./tools/episode-resource-profile.ps1 -SeparatePackages
. ./tools/start-server.ps1
```

It keeps46 baseline assets inside E_NEW and advertises13 original Episode JETs
separately, for24 packages at stamp1634666. Only explicit preparation changes the
environment; the helper does not restart a replica. It removes those13 names
from prior folded selections, preserves unrelated extras, and refuses an inherited
asset glob. The baseline launcher remains unchanged when PACKAGE_NAMES_EXTRA is
unset. Missing separate package files fail early instead of silently shortening.

Host checks passed for all24 packages: original payload bytes, single-record
extra packages, E_NEW47records/46929569bytes, inner/outerMD5, manifest totals and
64-byte ranges. Run `npx tsx scripts/verify-episode-cdn.ts --separate` from
server-ts. Existing folded verification and TypeScript build also passed.
One preserved-cache +10 native24-package bootstrap has now reached village;
individual residency/registration and Episode playback remain unverified.
Splitting reduces individual transport buffers, not total decoded resource cost.
See episode-split-package-contract.md for native evidence and limits.

## Historical folded preparation

The original first-story script EP_0301A and its named background/music/ambient/
voice resources are now positively located. See episode-first-story-assets.md.
Native resource lookup uppercases names, so original SEASON_LIST/SEASON1 work
with lower-case ReadJson inputs without metadata aliases.

The opt-in helper tools/episode-resource-profile.ps1 selects thirteen original packs:
R_EPISODE, EPISODE, DIAL-EN, N001_BG, ST099, SND1, SND_CDN, VOICE_CDN2, VOICE_CDN6,
and the C009 art/effect/portrait/voice family. Total original bytes:48,815,972.
The established C003/C004 families remain supplied by the normal battle profile.
The generated C003_DIALOG binding and complete actor/layout rendering remain
unverified. This is a preparation profile, not proof the Episode is playable.

First-combat follow-up: CB0101 game_res_id99 uses the original ENV_INFO prefix
STI099, supplied by ST099.jet. LEVELING_E is a named record inside LEVELING.jet;
the original LEVELING pack is already present byte-exact in instrumented +9.
BG_RES is not read by the inspected combat constructor/background path. Fixed
actors bind through the Episode STAT cache; do not invent ordinary Captain stats
or grant Captain to an account to address this path. Thirteen-pack transport
verification and build passed; Android battle playback remains unverified.

Inspect without changing environment:

```powershell
& ./tools/episode-resource-profile.ps1 -InspectOnly
```

For the future bounded native test, after the existing replica has been stopped:

```powershell
. ./tools/episode-resource-profile.ps1
. ./tools/start-server.ps1
```

The helper does not stop/start a server or modify/install the app. It preserves
existing selected assets/extras, adds the required packs through the launcher's
actual BLUSTONE_RESOURCE_ASSET_NAMES_EXTRA field, and sets stamp1634664. The
running baseline remains1634663 until explicitly restarted with this profile.
InspectOnly validates sizes/hashes and remains inert. Missing packs fail early.

Transport verification (server-ts working directory):

```powershell
npx tsx scripts/verify-episode-cdn.ts
```

This creates an isolated loopback listener and in-memory server state. It checks
all selected JET bytes against originals, native PKGI1 size/offset/stamp fields,
advertised package MD5 and a206 range response. Inherited asset globs and forced
range behavior are neutralized/restored. No native game requests, host-account
mutation or instrumented APK rebuild occur. Verification/build passed.

Review caught a wrong extra-assets variable and inherited verifier glob; both
fixed. Fresh-shell launcher preparation exercised up to its existing-port refusal,
proving baseline+Episode asset selection without stopping the current replica.
InspectOnly invariance and explicitly preselected asset preservation passed.
An inherited C*.jet regression remained bounded to the intended package set.

No CDN profile promotion or client download occurred. Native recovery remains
awaiting the separate forced-stop approval. Original JETs remain read-only.

# Revival continuation: resources and recruitment persistence

The chat's durable goal is active: continue server reverse engineering and
game revival across more areas and systems. This checkpoint is not completion
of that goal or a claim of full game fidelity.

## Implemented

- Account AP/BP lazily recover on game access, preserving partial intervals and
  offline recovery across restarts. Existing 300/1800-second rates are fixtures.
- Native resource clocks now receive next deadlines in server seconds. Evidence
  is in `research/revival-systems-next.md`: amount/time storage, server clock,
  signed division and remaining-time arithmetic were inspected independently.
- `/reference/GetExtra.server_utc` now supplies the numeric native clock
  anchor; without it the client runs resource arithmetic against a zero clock.
- Legacy clocks migrate without retrospective credit or credential changes.
- Recruited card instances now persist and appear in authenticated inventory
  reads after reload. Previously only the grant popup and allocator changed.
  The old smoke assertion perversely demanded granted IDs be absent from
  inventory; it now requires each awarded instance be owned exactly once.
- Roster-profile changes that collide with saved recruit IDs or remove their
  reference rows now fail before overwriting ownership. Separate-process tests
  cover changing party size and disabling the recruit reference after grants.

`npm test` and `npm run build` pass. Added meaningful regression checks for
resource boundaries, caps, overflow, backwards clock, save migration, restarts,
recruit currency, inventory IDs, account isolation and refused grants.

The replica was restarted after the tester returned to the map. One local
backup lives at `server-ts/data/state-before-revival-recovery.json` (private,
gitignored). The state file was not hand-edited. No client patch/rebuild was
needed. CDN names/version were kept at the existing default profile.

The first restart omitted tutorial-bypass flags used by prior reports. That
configuration mistake produced zero map progress/Supply absence; the launcher
now defaults both bypass flags to `1` so ordinary restarts preserve the known
device profile. A separate legacy-zero timestamp control removed the AP50
clamp while leaving that bootstrap symptom, separating the two changes.
The final profile restores bypass flags and includes GetExtra clock sync.
Fresh-launch validation at 16:20:21 UTC showed AP36/50 matching host AP36,
Airport50/150 and restored Supply/Search/Fight Club. No additional battle or
recruitment was performed for that check. This verifies the clock/profile
repair, not faithful economy or a full in-app recruitment workflow.

## Runtime evidence and limits

`testing/revival-001.md` records the fresh BlueStacks baseline: five cruise
destinations; Red Rock map and `n_03_01` battle entry; victory and return with
increased stars. Victory happened without an exit-door tap, but the actual
enemy-death moment was not observed. Do not call this proof of an enemy defeat.
The map background was black, battle art remained a fixture, seeded stars
still open all areas and can trigger unearned chest rewards. Collector Android
logs remained unavailable. These are live gaps, not successes inferred from
server tests. The report appendix records post-change checks separately.

## Research queue

`research/revival-character-next.md` locates catalogue/art evidence for Nene,
Tyltyl, Gerard and historical Beckhen stats. It also corrects overly strong
claims about recovered wiki metadata and warns against the stale roster patcher.
Default CDN still lacks Mowgli's art despite publishing its reference.

`research/revival-systems-next.md` recovers Training Raise request/response,
including nested target experience and object-valued removed instances. It
corrects the enhancement-price table: direct `level`/`rank` numeric arrays,
not generated wrapper keys. Empty price vectors risk native invalid reads.
Next: publish parser-correct price fixtures, model training over owned cards,
verify the UI, then tackle true progression/star boot parsing and more art.

An initial web search for original resource rates returned no usable game
evidence. No external rate was adopted. Future searches/videos should use
specific character/system questions and record date/version/provenance.

# Dataset index

Primary keys use character-reference IDs, never owned-instance IDs.

- [Hunter identities](../datasets/hunters/identities.json): 121 catalogue rows, including non-card variants, with field-level evidence.
- [Hunter stat observations](../datasets/hunters/stat-observations.json): historical 2019 numeric display values; unknown level, rank and gear remain explicit.
- [Hunter skill reference](../datasets/hunters/skill-reference.json): original formulas and symbolic placeholders, without fabricated magnitude values.
- [Monster identities](../datasets/monsters/identities.json): art identities; original combat stats remain unknown.
- [Campaign identifiers](../datasets/campaign/stage-identifiers.json): analytics enumeration; not recovered stage balance.
- [Episode graph](../datasets/episodes/story-graph.json): original story graph and battle-link metadata.
- [Episode rewards](../datasets/economy/episode-rewards.json): original reward IDs/quantities; server settlement mappings are separate policy.
- [Hunter gear identities](../datasets/equipment/hunter-gear-identities.json): named weapon/armor/accessory associations.
- [Equipment observations](../datasets/equipment/GEAR.md): preserved numeric evidence and methodology.
- [Coverage](coverage.json): generated counts; consult historical field-coverage findings for stricter base-stat completeness.

The legacy catalogue under legacy-catalogue-data/ and per-entity Markdown retains richer commentary and citations. New JSON does not override conflicting claims in that commentary.

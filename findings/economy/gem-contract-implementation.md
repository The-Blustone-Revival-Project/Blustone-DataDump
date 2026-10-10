# Gem initial contract repair, 2026-10-05

Original final28010 callbacks pass full envelopes to Gem parsers, which consume
ret_data directly as collections. The scalar legacy game.gem counter is not an
owned jewel. GetGemInven now returns an authenticated empty instance array;
GetGem/CombinationEffect/SellPrice/LevelUpPrice/DisassemblePrice return empty
reference arrays until their original rows are recovered. No jewelry or historical
balance values are fabricated. Legacy counter and all gameplay state are preserved.

Gem-family mutations and actual native /card_handler/EquipGem authenticate and
refuse instead of returning generic mock success. This does not implement mining,
polishing, equipping or set bonuses; native UI validation remains pending.

VSFan source map helped identify historical twelve-family terminology, but final
GetGemEffectName selector IDs differ from prose order: Fatal5, Block6. Reduction7
corresponds to historical Super Block; historical KO9% vsotherlocales5% remains
unresolved. Native DEF set effects multiply base DEF; the gem-name selector enum
is distinct from skill target-stat enums and per-gem string references.
No historic numeric effect was promoted to final balance or strict stats credit.

Full suite/build passed after correcting the historical smoke-test scalar
assumption. Review found the card_handler EquipGem route omission; fixed and
final focused gem test/build passed. Replica19728 promoted healthy on unchanged
baseline profile, saved account file SHA unchanged. No APK patch/build/release,
private packet disclosure, live rewards or VM action. Source reports:
gem-reference-contract.md and gem-set-evidence-crosswalk.md.

# RP1 display registration and native calendar preview

2026-10-06. Server-only correction; original item metadata remains unavailable.

The client synthesizes RP1 for gold rewards (LoginBonus reference reader,
episode-rp1-gold-receipt.md). Calendar thumbnail handling calls IsItemData on
the reference; map membership selects item versus card detail. With no registered
item, it can select InitCard. InitCard assumes GetCardData returns a valid
reference, and a null result reaches SetRefID with r1null. Exact original
classification/lookup evidence is item-detail-null-card-classification.md and
ghidra-login-detail-fault.txt. The earlier fault's actual clicked ID was not
captured; do not claim every detail crash has the same cause.

The replica now publishes RP1 as a display-only local item reference, with
nameRupees, generic local description, rank1/use_type0/effectempty and zero
sale/collection values. These metadata values are fixtures, not an original
GetItem row. IsItemData checks membership only, so use_type0 still classifies
as an item. No RP1 inventory stack, acquisition link, shop offer, redemption or
currency grant is introduced. Existing gold settlement remains authoritative.

Original UI_XML_RO KO/SR_COMMON/2_UI_CM_MD/13_UI_LV_MD directly binds child
ICON_GOLD to resource IT_CO. The mainwallet SPR_GOLD uses N_MGOLD separately.
IT_CO is therefore the supported gold-icon reconstruction. An initial IT_GCO
trial rendered a medal and was replaced; do not promote that trial as currency
art evidence. RP1's historical thumbnail_id assignment is still unproved.

Native validation after preserved-profile reload: PID28372, unchanged split24/
1634666. VillageMenu→DailySignInSupply shows proper coin icons (67 screenshot).
One day3 thumbnail press opens Rupees detail with the actual wallet balance
(68 screenshot), no crash, no newly claimed day and no added item. Preview
does not credit money. CurrentAmount uses native currency logic, not an owned
RP1 stack. Existing day2claim remains persisted; it was not rolled back.

The planned loss-fuel run was interrupted before any battle. A valid native
LoginBonusReward occurred during intended Airport navigation, adding the
documented local100gold/day2 marker before a null-card detail fault. The initial
two-input navigation did not inspect the intervening UI, so no clean Airport
selection is claimed. Subsequent preview testing uses inspected individual
actions. Refund acceptance remains pending; no battle/refund/forcedwin occurred.

Full tests/build and no-grant reference tests pass. Original quantity/calendar
economy is still a local fixture. No client patch/rebuild/GitHub release needed.

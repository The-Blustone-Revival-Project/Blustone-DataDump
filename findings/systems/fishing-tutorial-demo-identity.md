# Tutorial fishing result identity: evidence boundary

2026-10-07. Read-only retained tutorial Begin/Wait/Hook dumps and original ELF.
No Ghidra, device, source/state edits, fish grants or invented success receipt.

Root verified original guided gauge70 handoff then actual100/mode-3, emitting
/fishing/EndWithSell with log_id:-1 at2026-10-07T10:51:04.915Z. Backend2001
refused. This establishes a native result request, not a recorded successful
fish identity or reward.

No hardcoded demo fish identity assignment was found in the inspected
TutorialBegin/HookOnInit bodies. Those construct guide UI and tune hook floats;
RequestTutorialEnd has no fish_id request field. It posts log_id/is_win. Thus
the original server may have selected the result identity; local absence of
ordinary Begin is not proof that an original fish grant was hardcoded elsewhere.

## Exact post-request callback

Hook.OnRefresh local function-object literal DATef27f0+ef2796 resolves
**ELFVT2177f28**, offset-to-top0, RTTI
CSRSceneTutorialMFishingHook.OnRefresh$_6, function<void(int)>.
InvokeVT+20 contains odd ELFef2765, giving **G ef3764**.
Original callback checks the captured weak owner; result1 sets its **+6c1=1**
at ef3798, otherwise clears it and follows notice/error behavior. This is a
guide completion flag, not a fish identity setter. Hook.OnRefresh separately
requires +6c0/+6c1 before its completed mode/pop transition. Parent's next
bounded decompile target is **Thumb ef3764**, plus the receiving tutorial
scene's OnRefresh path for any eventual success popup.

## Concrete result-popup dependency

Ordinary **CSRPopUpMFishingSuccess.Init Gd0704c** loads
FISHING/FISH_WIN and soundFISHING_WIN. Its **SetItemInfo Gd07620** has a concrete
identity dependency: calls Fishing.GetInfo **b2eff0 atd07640**, then forms
**r1=INFO+18 atd0764a** and calls ItemInfo.GetItemData **af109c atd0764e**.
GetInfo returns **Fishing+50**, so that reference lookup is exactly
**Fishing+68**, the fish_id string overwritten by ParseEnd. It is not inferred
from a popup method argument or an arbitrary icon name.

Consequently returning an empty-string catch merely to avoid AddInven cannot
be declared success-popup-safe: if that popup path executes, it looks up an
empty item reference. The tutorial may instead end directly through its guide
flag path; that requires the post-request receiving-scene evidence. No empty
fallback reference, ordinary fake fish or generic card should be published.

Exact remaining parent targets: **Success.Init d0704c**, **SetItemInfo d07620**,
**TutorialMFishing.OnRefresh** (retained fishing-tutorial-refresh evidence),
and **ef3764**. Genuine fish item definitions need a real reference identity,
strict GetItem fields and valid resource binding before any actual catch grant.
The public FISHING_SETTINGS export contains common/PLC001/TUTO settings, not
the missing fish catalog. Original demo fish ID, grade, length and settlement
price/reward remain unresolved; no receipt is implemented by this report.

## Decisive retained completion path and step correction

The retained Hook.OnRefresh mode-4 body (ghidra-fishing-tutorial-hook.txt,
lines350..495) resolves the prior popup-path uncertainty. It checks
**SyncTutorial.GetState(27,2)<2**, requests **Clear(27,2)**, constructs
CSRPopUpMFishingSuccess, invokes its Init and pushes that modal. The real final
ACK pair is **27/2**, not27/1. Do not pre-clear either step to bypass the
unsettled result or treat successful request transport as a performed clear.

Parent's ghidra-fishing-success-popup.txt proves Init **unconditionally**
gets Fishing.GetInfo and calls SetItemInfo(INFO+18,1) atlines365..366.
SetItemInfo obtains ItemInfo.GetItemData from that same INFO+18. Thus this
path really uses ParseEnd's fish_id, not merely an optional later popup.

The popup reads item-reference **use_type at+4**:17 selects a distinct
bait/item presentation branch. Ordinary fish presentation uses item-reference
text/resource fields and captured result INFO offsets:

- INFO+28 = Fishing+78 = returned grade; grade2 choosesF_S, grade3F_G,
  otherwiseF_B (bronze-style fallback, not proof every other grade is legal).
- INFO+2c = Fishing+7c = returned length; divides by100 and formats
  remainder with %d.0%dcm or %d.%dcm. This proves the display's hundredths-
  of-centimeter interpretation; original fish length distributions are unknown.
- INFO+30 = Fishing+80 supplies the animated result gold amount, copied to
  popup+e8. This is not GetCurrentGold and does not itself mutate the wallet.
  No original sale/reward amount follows from that display field.

## Empty GetItemData behavior is a fallback, not a fish reference

Original **GetItemDataaf109c** does not immediately returnnull for a missing
fish. It logs NotExistItem Ref ID, then explicitly searches **DUMMY**
(LDRaf1136/ADDaf113a, findaf1146). If that fallback is absent it uses a
guarded static default INFO (af118e..af11d6); its field storage is initialized
tozero/empty by the inspected constructor path. Therefore earlier empty-ref
concern must not be restated as a proven immediate null crash.

That fallback supplies neither original fish identity nor legitimate art/text;
later sprite/layout code can still consume empty fields. It is not evidence
that empty-catch success is complete or that a generic DUMMY grant is suitable.
A real recovered fish reference plus explicitly marked local tutorial settlement
could eventually satisfy these dependencies, but the original demo ID and
original server economics remain unrecovered. No such policy is implemented
or claimed native-accepted by this report.

# Fight Club preparation fee: admission closed, display source pending

2026-10-10. Independent read-only review of root's original native export
ghidra-arena-confirm-fee.txt, native symbols, current arena source and prior
contracts. Only this note written; no UI, runtime, Ghidra or pricing changes.

## Closed observations

Native preparation screenshot14 displays BP10/10 and an envelope0 beside
Begin Battle. No BattleStart or debit occurred. arena.ts ARENA_BP_COST=1 and
arena-service.ts BattleStart validate/debit that explicitly local BP1 policy.
The apparent preparation-versus-server discrepancy is real; its cause is not
yet assigned to missing reference fields, a wrong icon, a native default or bid.

RequestBattleMission Ge873f4 first reads attacking GetDeckInfo(4) (export
lines400–451). Its ordinary non-special-scene path reads CalcTotalBP (621–624):
exactly zero opens NoMoney with SetData(type2,1,callback) (638), while nonzero
proceeds to RequestBattleWith (729–731). The special current-scene0x54 path
already requests battle earlier (522–546) without traversing that ordinary
BP check. Therefore the **ordinary path admits only positive BP and offers a
one-unit shortage dialog at zero**. This does not prove the server debit amount,
the active runtime scene branch or original economics for every battle type.

The RequestBattleWith decompiler arguments mix 64-bit ABI/callback registers
(545–546 and729–731). Do not derive new bid/cost semantics from that rendering.
arena-battle-contract.md already closes wire fields target_pvid, is_revenge,
is_friendship, bid; bid's original provenance remains unresolved. No evidence
here equates the button's envelope0 to bid.

SetBP Ge82010 (lines1–115) obtains a named node/textbox and formats two numeric
values into joined text (45–64). It does **not** recover which displayed region
that is: exact relocated UI key and caller arguments are absent, and the
decompiler omits reliable argument flow around return-by-reference formatting.
It must not be identified as the Begin fee setter solely from its name.
SetLeague Ge86674 handles league-resource/name text (150–211); SetBattleWith
Ge86900 writes supplied opponent text (283–295). Neither inspected body binds
an economic reference price or explains preparation0.

Current /reference/GetBattle publishes league/weekly rewards and maintenance
compatibility fields. No published BP fee is present in arenaReference; none
of these four exported functions parses a GetBattle fee field. That is a
bounded observation, not proof that no upstream global/reference field exists.

## Exact next source targets

1. **CSRSceneStageConfirm.SetNeedAP Ge82af8**: native-evidence.tsv identifies
   this single-uint setter. Recover its actual node/textbox key and formatting
   branch; despite the method name, it may be shared across resource modes.
   Do not conclude that it is the envelope setter until the key matches UI.
2. **SetBattle Ge80164** and **OnInit Ge7ca3c**: follow calls to SetNeedAP and
   SetBP, retain original scene/mode branches and actual argument sources.
   A missing call leaving initial XML0 differs from a parsed reference0.
3. Resolve relocated strings/Thumb call registers for the above setters and
   RequestBattleMission marker keys. Only follow an upstream GetExtra/GetBattle
   field if these concrete callers actually supply it.
4. If needed, **SetFriendlyType Ge85e90** can identify the special-mode branch;
   its relation to current scene0x54 remains unclosed in this review.

Retain BP1 as labeled current server policy while investigating. Do not invent
a GetBattle price field, reinterpret bid as fee, change original assets or
change server charging to0 merely to agree with an unexplained display. Native
Begin acceptance/debit/combat is still untested and should follow the display
contract investigation with prompt battle attacks already prepared.

## Producer follow-up: common stage cost drives the Begin readout

Root subsequently exported ghidra-arena-confirm-fee-producers.txt (SetNeedAP,
SetBattle and OnInit). The existing **ghidra-campaign-auto-confirm.txt** already
contains the missing authoritative OnReset Ge7d124 caller; reuse it rather than
repeat decompilation.

- OnReset1521–1523 uses CSRGameStage.GetStageData on scene+788 stage string.
  It dispatches current scene0x24 to SetBattle(...,0),0x54 to SetBattle(...,1),
  and0x86/87 to SetMission (1524–1540). These are source branches; actual
  runtime scene value and stage string in the pictured preparation are unread.
- OnReset1608–1613 calls SetNeedAP(0) for scene0x54, otherwise
  SetNeedAP(first uint32 of the selected Stage INFO).
- **OnReset1647 then unconditionally formats that same first Stage INFO word
  directly into PA_NEXT/TX_ST**, independently of the earlier special-zero
  call. Exact relocated keys are in ghidra-campaign-auto-confirm-keys.txt
  lines259–260: LDR Ge7e74a/slotGe7e908, ADD Ge7e74c resolves PA_NEXT;
  LDR Ge7e760/slotGe7e90c, ADD Ge7e762 resolves TX_ST.
- New SetNeedAP producer lines28–32 formats its supplied integer and writes
  one direct textbox; lines54–60,103–109 and152–159 write the same integer
  to three nested textboxes. It does not fetch a fee reference. SetBattle and
  OnInit contain no SetNeedAP/SetBP call; OnReset is the decisive caller.

This positively identifies a common **Stage INFO cost readout** in the Begin
panel, rather than a parsed GetBattle price or proved bid. The first word's
ap_cost identity is supported by existing stage schema/parser work; exact
first-word binding should be retained from SetStage Ga274d0 if needed. Native
RequestBattleMission's positive-BP admission uses a different source and does
not compare BP with this Stage INFO word. Thus a displayed0 does not establish
that native Arena Start is free or that serverBP1 should be changed to0.

The remaining causal gap is narrow: which stage string/INFO is selected by
the actual Arena preparation, and whether its first word0 is a fallback,
explicit stage row or overwritten value. Do not claim the dummy/default path
solely from the pictured0. Exact source target **GetStageData(string)
Ga27f60** can close missing-ID fallback; SetStage **Ga274d0** can close first
word storage. OnReset's runtime scene+788 string/selected INFO are separate
root-owned bounded observation targets if source alone cannot identify them.

Still-unresolved exact SetNeedAP literal pairs, expressed as slot plus the
decompiler's ADD-PC base, are: Ge82e5c+Ge82b1a (direct textbox),
Ge82e60+Ge82b72 and Ge82e64+Ge82b88 (first parent/child),
Ge82f44+Ge82c1a and Ge82f48+Ge82c30 (second),
Ge82f4c+Ge82cc2 and Ge82f50+Ge82cd8 (third). Resolve via exact relocated
register instructions, not blindly treating these decompiler bases as ADD
instruction addresses. These keys can corroborate the direct PA_NEXT/TX_ST
write and distinguish common panel variants without inventing a new API field.

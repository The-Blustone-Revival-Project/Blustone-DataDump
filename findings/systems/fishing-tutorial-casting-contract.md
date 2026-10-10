# Fishing tutorial: casting setup versus attempt contract

2026-10-06. Bounded retained symbols, original Thumb and prior fishing reports
only. No Ghidra, device, source edits, bait grants, cast/catch/end or guide clears.

Root's native observation is scene rendered after earned n_03_07, Clear27/0
acknowledged, and GuideFishing with owned bait0 reached the casting-distance
gauge before a line cast. No /fishing/Begin had been sent. That observation
does not yet test whether the tutorial's attempt is local or network-backed.

## Positive input/local guide path

CSRSPopUpMFishingThrow.OnProcessCursorPress **Gdf1e0e** checks popup+6a0,
tests gauge rectangle intersection and primary press1, writes+6a0=1 then calls
**StartFishing Gdf1e6c atdf1e50**. This is the next actual casting action;
there is no need to invent a scene jump or host attempt.

Separate **StartFishing_Tutorial Gdf2a80** obtains local COMMON_INFO and
schedules delayed OnceImpl calls **df2c20/df2cae**. Original closure identities:

- VT ELF216d8ac, RTTI StartFishing_Tutorial$_5, invoke **Gdf4246**: locks
  captured weak owner, toggles visible UI nodes (df4266/df4270).
- VT ELF216d8ec, RTTI StartFishing_Tutorial$_6, invoke **Gdf43d6**: locks
  captured weak owner and writes popup+6a2 byte1 atdf43f8.

These are local casting-guide setup, not proof of a local synthetic fish or
waived network Begin. They depend on the already recovered local COMMON_INFO
settings; no original difficulty values are inferred from offsets.

## Model requests and unresolved transition

No CSRMFishing.RequestTutorialBegin symbol was found in the retained model
surface. The actual model exports ordinary **RequestBegin Gb26cbc**:
/fishing/Begin, auth5+place_id/cast_dist/lure_id; ReqBeginCBb27b38 and
ParseBeginb27d34. It separately exports **RequestTutorialEnd Gb28864** and
ordinary **RequestEnd Gb29624**, both targeting **/fishing/EndWithSell** with
auth5+log_id/is_win, followed by shared ReqEndCBb2a308. See entry/pool reports
for recovered response/tuning keys. Absence of a named tutorial Begin does not
prove the ordinary requester is invoked by this guide.

The post-cast caller selection, local tutorial FISH_INFO construction (if any),
log identity and demo fish ID remain unresolved. No original demo fish identity
or network-independent catch reward is recovered by this lane. Parent's finite
next decompile targets are **StartFishingdf1e6c**, **StartFishing_Tutorialdf2a80**,
**TutorialMFishing.OnInitef15e8/TutorialBeginef1684**, and then whichever exact
post-cast continuation they establish. Do not grant bait or fake Begin/End
success to close a dependency that has not yet been exercised.

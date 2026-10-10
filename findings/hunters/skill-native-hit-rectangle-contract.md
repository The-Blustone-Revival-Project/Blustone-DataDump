# Native skill hit rectangle and opacity: original consumer contract

2026-10-09. RootreadOnly/noanalysisGhidra, same+12nativeoriginal. No memorycalls,
liveactorreads/clientpatches/stats/progressionmutations. Thischangesnextreadplan,
not liveacceptedskillproof. Failed004/005fixedpointtrials remain losses.

OnProcessCursorPress Ga3c178: pressbyte1, icon+6c enabled1, drawable strongpointer
icon+60/+64, virtualslot90 result used by CMTestIntersectionG78c90e. Exact primary
CMDrawablevtableG2146940/addresspoint2146948:slot90→G70c810GetArea;slot94→G70b0e0
InvalidateBoundBox. New ExportVtableSlots uses exactsymbol inrelocatedmemory;
initialfragmentmatchincludedirrelevantcomponent/controltables, correctedexact
_ZTV10CMDrawable and regeneratedauthoritativeexportmatches1. Neverinferfrom
neighboringfunction/addressorflatELFpre-relocationplaceholders.

CMDrawableGetArea refreshesvirtualslot94 BEFOREreturningdrawable+1bc. Intersection
reads floatxmin/ymin/xmax/ymax at1bc/1c0/1c4/1c8 against integercursor x/y inclusive.
UpdatableGetArea alonejustreturns1bc; doNOTuseunrefreshedcacheasdrawableauthority.
InvalidateBoundBox firstCalcTransfWorld44, recomputeswhen drawableflagbyte60&8.
Source uses width/height78/7c, anchor7fc/800 and worldmatrix118. Important: full
transformed-corner extrema are stored in a SEPARATE rectangle+804. The hit test
uses+1bc, computed from world translation/scales and half-size offsets. Do not
substitute the rotated/full-render bounds+804 for the exact press consumer.
CalcTransfWorld44 parentweak54/58, dirtymask2; localmatrixd8 composition,
worldmatrix118. CalcTransfLocal44 testsflagmask1 andclearsit afterlocalmatrixupdate.
A readonlyreader must rejectdirty1/2/8 orunprovedancestor-transformstate, not invoke
nativeGetArea/refresh tomutatecache. Finitecachedfloatsarenotfreshness/ownershipproof.

SetInpuableG985f8c dynamicallycastsorcreatesCSRGameUIIconSkill andstores strongpair
actor+a6c/+a70; weakSkillPointpaira74/a78 isdifferent. IconctorGa3b3c8 finds named
CMDrawable inview; OnAttachGa3c1d0 attaches view tohost, DetachGa3c2ac removesit.
IconprimaryvtableG215db38/addresspoint215db40 slot34→Ga3c178. Actor+a7d getter
G97ecba isactualIsSkillEnabled. Ownership/controlcounts andknownvptrmuststillbe
proved atlive-readtime; zero/dangling/stalecomponent cannotjustifytouch.

OpacityGetOpacityfG78a372 uses drawable+b8 * +bc * +b4. Dirtyflag60&80 recursively
refreshes parentopacitycachedb8; readonlyreader mustrejectdirty/invalidancestor
cache, not inferbyte255 fromwhitepixels. Eventconversion multipliesopacity by
originalliteralDATa3c1cc; exactpositive/truncatebyte behavior is inOnPress; actor
listeneradditionallyrequiresa7d andbyte255 pluscamp/target/reserve predicates.
Thisexportdidnotresolvethefloatliteral orruntimeeligibility; don'tskipthosechecks.

RendererGetLogicalPosG10e0528 converts physicalCRMPoint usingrenderer bounds:
logical spansabs(+24−+1c),abs(+28−+20),physical spansabs(+4c−+44),abs(+50−+48),
logicaloffsetfloat68/6c; integerresult truncates offset+(physicalpoint−origin)*ratio.
GetPhysicalPosG10e05cc exportedseparately; usesintegerdivision andaddsoffsets, do
notassume algebraicinverse. Runtime rendererowner/rects andactualinputcallerchain
notyetclosed; a720/1080ratio or36pixelmargin fromscreenshots isnot recoveredmapping.
OnTouchG9d72fc isUIbuttoncallback (includingnativeauto-combat setting), not the
physical-to-logical conversionentry. OnProcessPressG9db1bc forwardsthe root UI
beforeordinaryattackgates; don'tattributeeithername tounprovedcoordinates.

Evidence ghidra-skill-drawable-targeting.txt, -coordinate-contract.txt,
-bound-episode-gate.txt, -bound-refresh.txt, -drawable-vtable.txt, -icon-vtable.txt,
-renderer-coordinates.txt and-input-coordinate-path.txt. Gaddresses denoteproject
relocatedaddresses (ELF+10000); actualruntimehelper subtracts10000 plusloadbase.
Nextnative-readextension canemitqualifiedactor/icon/dirtyrect/opacity observations,
onlyafterlifetime/control/vptr checks; noinputfromunprovedcoordinates. Runtime
normalcontrol remainsvisualordinaryattacks; no furtherfailedfixedpointretries.

Follow-up exactcalls closed: GetLogicalPos xrefs fromJNITouchesBeganG11035d0,
MovedG1103700,EndedG11037dc plusRMGetLocalPosG110357c. BeganpassesconvertedCRMPoint
 to_HandleTouch withpress1/slotindex, matchingiconOnProcessCursorPress. JNIreads
rendererglobalindirection andrendererpointeratowner+4; actualrelocatedglobal/live
ownerandpointer/controlstructure stillunverified. OpacityliteralGa3c1cc raw437f0000
isIEEEfloat255.0, nowresolvedinprojectmemory. OriginalJavaonTouchEvent addspointerID1,
convertsMotionEvent via m17365e thendispatchesJNIbegan/ended. API<29 path truncates
localx/y, subtractsrendererView.translationY andconditionallyaddsphone/layoutoffsets
(m17380q+inset); API>=29alternateusesrawcoordinates. BlueStacksSDK25 followsfirst
branch, but actuallayoutflags/insets needliveevidence. No universal36pixel offset
orverticalflip isproved. Evidenceadded -jni-touch-coordinates.txt,
-logical-pos-callers.txt,-opacity-literal.txt andskill-java-touch-coordinate-evidence.

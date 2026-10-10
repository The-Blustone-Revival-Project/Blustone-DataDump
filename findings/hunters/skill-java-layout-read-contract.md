# Exact Java touch-layout read contract on SDK25

Read original JADX sources RMFrameworkActivity.java, C3159b.java, RMEditBox.java,
C3164g.java and MainActivity.java, plus instrumented InstrumentedActivity.java.
No frame attachment, ADB, Ghidra, native call, target method invocation or input
was performed. JADX's `f214xx` names are presentation aliases: use each
`renamed from` comment for actual JVM field names.

## Exact fields and type signatures

On `com.vshower.rann.RMFrameworkActivity`, real instance fields are
`F:Z` (JADX f21400F), `x:Z` (f21415x), `z:Z` (f21417z), `y:I` (f21416y),
`w:I` (f21414w), and `p:Lcom/vshower/rann/RMEditBox;` (f21407p).
The touch dispatch gates are `t:Z` and `u:Z`. Lifecycle flag `A:Z` is set true
in onPause and false in onResume; it is not the game's combat pause mask.

The exact static renderer-view field is
`RMFrameworkActivity.N:Lcom/vshower/rann/b;` (JADX f21392N/C3159b).
Resident renderer/view class `com.vshower.rann.b` has instance
`m:Lcom/vshower/rann/RMFrameworkActivity;` (f21515m), set from its constructor's
Activity context. It extends GLSurfaceView and is its own Renderer. `b.n/o/p/q`
are ints (surface/layout dimensions), not the Activity's edit-box field.

RMEditBox's actual fields `m:Lcom/vshower/rann/RMFrameworkActivity;` and `n:Z`
reproduce original `p()`: false if m is null, otherwise n. Read them directly;
do not invoke RMEditBox.p() or read text contents. Optional association check:
`com.vshower.rann.g.a:Lcom/vshower/rann/RMFrameworkActivity;` is a static Activity
reference set by the original constructor. The helper's `i()` merely returns
`android.os.Build.MODEL:Ljava/lang/String;`; read that static value directly.

## Safe object identity without target calls

Find the loaded exact RMFrameworkActivity ReferenceType and require the field
names/signatures/static modifiers above. Read static N through getValue; require
non-null exact resident type `com.vshower.rann.b`. Its `m` must be non-null and
have exact runtime type `com.vshower.instrumented.InstrumentedActivity`, with
superclass chain MainActivity→RMFrameworkActivity. Read the inherited fields
using their declaring ReferenceType Field objects, not JADX aliases or an
arbitrary first instance. Optional g.a and editbox.m must equal this same object
when non-null. No static method invocation is needed to obtain these references.

At an already authorized suspended render callback, its frame thisObject may
cross-check equality with N; this report does not attach a breakpoint. A
ReferenceType.instances fallback, if ever needed, must be bounded and require
exactly one matching InstrumentedActivity associated with N/m, not select the
first surviving Activity object. An old object can remain after a lifecycle
change. Root's separately verified current client/foreground remains necessary;
N/m equality alone is not OS foreground proof.

Use JDI getValues/getValue only, retain the object references for the bounded
read, and repeat N, renderer.m, editbox identity/owner and all layout flags
before publishing. Reject changed identity/fields or unknown signatures. Private
field visibility does not require Java reflection or invokeMethod for JDI reads.
The snapshot can report flags and association even when translation is unknown.

## SDK25 conversion: exact arithmetic and remaining unavailable value

SDK25 always takes the original `MotionEvent.getX/getY` branch, since SDK_INT<29.
Those values are pointer-local floats cast to int, not necessarily the same
coordinate frame as raw physical screenshot pixels. Original JVM `e(MotionEvent,
int)` (JADX m17365e) computes:

1. x = integer-cast getX(pointerIndex); localY = integer-cast getY(pointerIndex).
2. offset = minus integer-cast rendererView.getTranslationY(). Cast occurs before
   negation; do not replace it with rounding or floor.
3. If editbox.m is non-null, editbox.n is true and Activity.x is false, add w.
4. `q()` returns z ? y :0. Add that value when F is false, or Build.MODEL equals
   801SH ignoring case. Otherwise omit it.
5. JNI receives x and localY+offset+the applicable q value. Touch pointer ID+1
   and down/up/move dispatch are separate from this layout conversion.

The renderer translation cannot safely be recovered by calling getTranslationY
under the no-native-call constraint. Android7.1.1's View getter delegates to
RenderNode.getTranslationY, which calls native nGetTranslationY. It is not an
ordinary cached Java float field. Primary references:
[AOSP View.java](https://raw.githubusercontent.com/aosp-mirror/platform_frameworks_base/android-7.1.1_r1/core/java/android/view/View.java),
[AOSP RenderNode.java](https://raw.githubusercontent.com/aosp-mirror/platform_frameworks_base/android-7.1.1_r1/core/java/android/view/RenderNode.java).
These sources establish the stock API25 path; BlueStacks' exact framework
implementation has not been dumped/verified here. Do not guess a RenderNode
native-memory offset or substitute zero because the visible surface appears
aligned. Reading View.mTop/mLeft alone does not supply animated translation.

Therefore the Java flag/owner portion is recoverable without calls, while full
screen→JNI conversion remains unavailable until root independently recovers the
resident translation or an equivalent authoritative transform. Native renderer
logical mapping is a further separate conversion. Neither these Java fields
nor a finite native icon rectangle alone authorize a targeted touch.

## Constraint clarification: pure Android getter is an allowable read

The earlier limitation describes a strictly field-only/no-JNI snapshot. Root
clarified that the operational constraint prohibits game-native getter calls
and mutations, while audited stock Android read accessors may be used (the
existing diagnostic already performs native-backed RandomAccessFile reads).
Under that clarified constraint, getTranslationY is a legitimate narrow read,
not a reason to guess zero or leave translation permanently unavailable.

Additional Android7.1.1 primary sources establish the complete implementation:
[RenderNode JNI](https://raw.githubusercontent.com/aosp-mirror/platform_frameworks_base/android-7.1.1_r1/core/jni/android_view_RenderNode.cpp)
casts the existing pointer and returns stagingProperties().getTranslationY().
[RenderNode.h](https://raw.githubusercontent.com/aosp-mirror/platform_frameworks_base/android-7.1.1_r1/libs/hwui/RenderNode.h)
returns the const staging-properties member;
[RenderProperties.h](https://raw.githubusercontent.com/aosp-mirror/platform_frameworks_base/android-7.1.1_r1/libs/hwui/RenderProperties.h)
returns its stored primitive translationY float. This path has no lazy matrix
update, dirty-state write, GL-context dependency, lock or guest game callback.
Other framework getters, such as transform-matrix/pivot access, cannot inherit
this purity conclusion automatically. Local renderer class b/C3159b defines
no getTranslationY override; its relevant inheritance is GLSurfaceView→
SurfaceView→View. The inspected instrumentation also adds no renderer override.

For the bounded authorized snapshot, select the exact `android.view.View`
declared method `getTranslationY:()F` on the verified static N renderer object.
Verify its declaring framework type/class-loader and method metadata rather
than dispatching an arbitrary same-named app method. Nonvirtual invocation of
that View method with the existing suspended Java thread can avoid an unexpected
override; a single-threaded read does not need game JNI or new input. Require a
finite FloatValue, repeat N/m and layout flags plus the returned translation
before publishing, and report the actual float and integer cast separately.
Unknown/changed framework identity or an invocation failure must leave the
conversion unavailable. BlueStacks' framework binary was not independently
disassembled here; provenance is stock API25 source plus the local app's absence
of override, not a claim that every possible OEM implementation is identical.
This clarification does not authorize native game GetArea/GetOpacityf calls,
which are already proved to refresh caches and therefore write state.

## Pure field-only window/compatibility diagnostics

Use the verified static N view and its inherited
`android.view.View.mAttachInfo:Landroid/view/View$AttachInfo;`. The exact
AttachInfo instance has `mViewRootImpl:Landroid/view/ViewRootImpl;` and
`mRootView:Landroid/view/View;`. Guard the resident root's `mAttachInfo` equality
and `root.mView == attachInfo.mRootView`. The root view is normally DecorView,
not the GL renderer N; do not require equality with N or choose another root
from a broad instance enumeration. Match loaded framework types/signatures
and repeat object references and all reported fields before emitting.

Useful direct fields are root `mCurScrollY:I`,
`mTranslator:Landroid/content/res/CompatibilityInfo$Translator;`,
`mWinFrame:Landroid/graphics/Rect;`, and AttachInfo `mWindowLeft:I`,
`mWindowTop:I`, `mApplicationScale:F`, `mScalingRequired:Z`. Read Rect's
left/top/right/bottom ints directly with finite/bounded geometry checks;
retain whether the translator is null. A non-null translator's exact float
fields are `applicationScale` and `applicationInvertedScale`, which must be
finite and positive. No getter, native call, touch or layout refresh is needed.

Stock API25's pointer pre-stage scales through the compatibility translator,
then adds mCurScrollY to event y, before view dispatch. The translator scales
MotionEvent by applicationInvertedScale. Window-left/top and mWinFrame can
already reflect compatibility translation, so these Java values are diagnostic
app-window geometry, not an automatically physical origin. Primary sources:
[ViewRootImpl](https://raw.githubusercontent.com/aosp-mirror/platform_frameworks_base/android-7.1.1_r1/core/java/android/view/ViewRootImpl.java)
and [CompatibilityInfo](https://raw.githubusercontent.com/aosp-mirror/platform_frameworks_base/android-7.1.1_r1/core/java/android/content/res/CompatibilityInfo.java).
The AttachInfo names and association are defined by the linked AOSP View.java.

Keep Android's Activity callback and renderer-view coordinates distinct.
InstrumentedActivity.dispatchTouchEvent enters normal Activity/window dispatch;
the original Activity.onTouchEvent is a fallback. A child's transformed event
must not be assumed to be the same event coordinate frame received by that
fallback. Reading N.mLeft/mTop or a renderer surface's visual position alone
does not settle this. Framework input delivery can also apply a window-origin
offset before ViewRootImpl; the exact resident native dispatch transform was
not recovered by this review. Stock Java source is not proof of BlueStacks'
specific dispatcher state.

Recommended output is therefore raw owner-guarded attach/root identities,
frame/window fields, compatibility state and scroll values, alongside the
separate Activity layout flags and audited translationY read. Keep
`physicalToActivityLocal=unavailable` and `inputPoint=unavailable` until root
closes the complete resident input-delivery/hierarchy conversion. Even all-zero
observed window/scroll fields with translator null are observations, not
permission to assume ADB physical coordinates equal MotionEvent.getX/getY.

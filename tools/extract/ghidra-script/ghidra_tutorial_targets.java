import ghidra.app.decompiler.DecompInterface;
import ghidra.app.decompiler.DecompileResults;
import ghidra.app.script.GhidraScript;
import ghidra.program.model.listing.Function;

public class ghidra_tutorial_targets extends GhidraScript {
    @Override
    public void run() throws Exception {
        DecompInterface decomp = new DecompInterface();
        decomp.openProgram(currentProgram);
        String[] names = {
            "_ZN15CSRPopUpVillage12SetTutorialsEv",
            "_ZN15CSRPopUpVillage13TutorialBeginEv",
            "_ZN15CSRPopUpVillage11TutorialEndEv",
            "_ZN15CSRPopUpVillage13SetTutorialFCEv",
            "_ZN15CSRPopUpVillage16SetTutorialQuestEv",
            "_ZN15CSRPopUpVillage17SetTutorialGacha1Ev",
            "_ZN15CSRPopUpVillage17SetTutorialGacha2Ev",
            "_ZN15CSRPopUpVillage19SetTutorialTrainingEv",
            "_ZN15CSRPopUpVillage15ProcessHouseBtnENS_6BUTTONE7TU_TYPEN8CSRScene4TYPEES3_",
            "_ZN15CSRPopUpVillage20OnProcessCursorPressEjfRK8CRMPointh",
            "_ZN15CSRPopUpVillage13OnButtonClickEP8CMUIViewP8CMUIBase",
            "_ZN15CSRPopUpVillage13ShowFingerIndicatorENS_6BUTTONEN8CSRScene4TYPEE",
            "_ZN15CSRPopUpVillage6OnInitEv",
            "_ZN15CSRSyncTutorial5ParseERKN8nlohmann10basic_jsonINSt6__ndk13mapENS2_6vectorENS2_12basic_stringIcNS2_11char_traitsIcEENS2_9allocatorIcEEEEbxydS8_NS0_14adl_serializerENS4_IhNS8_IhEEEEEE",
            "_ZN15CSRSyncTutorial8GetStateE7TU_TYPE7TU_STEP",
            "_ZN15CSRSyncTutorial8SetStateE7TU_TYPE7TU_STEPNS_5STATEE",
            "_ZN15CSRSyncTutorial12RequestClearE7TU_TYPE7TU_STEPNSt6__ndk18functionIFviEEE",
            "_ZN11CSRPlayData9GetMarkerERKNSt6__ndk112basic_stringIcNS0_11char_traitsIcENS0_9allocatorIcEEEE",
            "_ZN11CSRPlayData9SetMarkerERKNSt6__ndk112basic_stringIcNS0_11char_traitsIcENS0_9allocatorIcEEEERKN8nlohmann10basic_jsonINS0_3mapENS0_6vectorES6_bxydS4_NS9_14adl_serializerENSC_IhNS4_IhEEEEEE",
            "_ZN15CSRTutorialMStageMap6OnInitEv",
            "_ZN15CSRTutorialMStageMap20OnProcessCursorPressEjfRK8CRMPointh",
            "_ZN15CSRTutorialMStageMap13OnButtonClickEP8CMUIViewP8CMUIBase",
            "_ZN15CSRTutorialMStageMap11TutorialEndEv",
            "_ZN16CSRViewMStageMap9SetSelectERKNSt6__ndk112basic_stringIcNS0_11char_traitsIcENS0_9allocatorIcEEEE"
        };
        for (String name : names) {
            java.util.List<Function> functions = getGlobalFunctions(name);
            Function function = functions.isEmpty() ? null : functions.get(0);
            println("FUNCTION " + name + " -> " + (function == null ? "missing" : function.getEntryPoint()));
            if (function == null) continue;
            DecompileResults result = decomp.decompileFunction(function, 120, monitor);
            println(result.getDecompiledFunction() == null ? result.getErrorMessage() : result.getDecompiledFunction().getC());
        }
    }
}

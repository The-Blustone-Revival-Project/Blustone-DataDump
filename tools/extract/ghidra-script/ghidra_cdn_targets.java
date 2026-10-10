import ghidra.app.decompiler.DecompInterface;
import ghidra.app.decompiler.DecompileResults;
import ghidra.app.script.GhidraScript;
import ghidra.program.model.listing.Function;

public class ghidra_cdn_targets extends GhidraScript {
    @Override
    public void run() throws Exception {
        DecompInterface decomp = new DecompInterface();
        decomp.openProgram(currentProgram);
        String[] names = {
            "_ZN7CPVCDN214ExportPKGIver1ERKNSt6__ndk112basic_stringIcNS0_11char_traitsIcENS0_9allocatorIcEEEE",
            "_ZN7CPVCDN214ExportPKGIver1ERKNSt6__ndk16vectorIhNS0_9allocatorIhEEEE",
            "_ZN7CPVCDN29UnPackingERKNSt6__ndk16vectorIhNS0_9allocatorIhEEEE",
            "_ZN7CPVCDN211ParseHeaderERKNSt6__ndk16vectorIhNS0_9allocatorIhEEEE"
            ,"_ZN17CSRSceneMStageMap11SelectStageEi"
            ,"_ZN17CSRSceneMStageMap13OnButtonClickEP8CMUIViewP8CMUIBase"
            ,"_ZN17CSRSceneMStageMap20OnProcessCursorPressEjfRK8CRMPointh"
            ,"_ZN16CSRViewMStageMap13OnButtonClickEP8CMUIViewP8CMUIBase"
            ,"_ZN16CSRViewMStageMap22OnTableViewButtonClickEPK12CMTableView2jP8CMUIViewP8CMUIBase"
        };
        for (String name : names) {
            java.util.List<Function> functions = getGlobalFunctions(name);
            Function function = functions.isEmpty() ? null : functions.get(0);
            println("FUNCTION " + name + " -> " + (function == null ? "missing" : function.getEntryPoint()));
            if (function == null) continue;
            DecompileResults result = decomp.decompileFunction(function, 180, monitor);
            println(result.getDecompiledFunction() == null ? result.getErrorMessage() : result.getDecompiledFunction().getC());
        }
    }
}

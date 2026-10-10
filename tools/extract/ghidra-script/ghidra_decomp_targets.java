import ghidra.app.decompiler.DecompInterface;
import ghidra.app.decompiler.DecompileResults;
import ghidra.app.script.GhidraScript;
import ghidra.program.model.listing.Function;

public class ghidra_decomp_targets extends GhidraScript {
    @Override
    public void run() throws Exception {
        DecompInterface decomp = new DecompInterface();
        decomp.openProgram(currentProgram);
        String[] names = {
            "_ZN11CSRPlayData13ParseUserInfoERKN8nlohmann10basic_jsonINSt6__ndk13mapENS2_6vectorENS2_12basic_stringIcNS2_11char_traitsIcEENS2_9allocatorIcEEEEbxydS8_NS0_14adl_serializerENS4_IhNS8_IhEEEEEE",
            "_ZN13CSRSyncGlobal19ParseUserDatailInfoERKN8nlohmann10basic_jsonINSt6__ndk13mapENS2_6vectorENS2_12basic_stringIcNS2_11char_traitsIcNS2_9allocatorIcEEEEbxydS8_NS0_14adl_serializerENS4_IhNS8_IhEEEEEE"
        };
        for (String name : names) {
            java.util.List<Function> functions = getGlobalFunctions(name);
            Function function = functions.isEmpty() ? null : functions.get(0);
            println("FUNCTION " + name + " -> " + (function == null ? "missing" : function.getEntryPoint()));
            if (function == null) continue;
            DecompileResults result = decomp.decompileFunction(function, 120, monitor);
            println(result.getDecompiledFunction() == null ? result.getErrorMessage() : result.getDecompiledFunction().getC());
        }
        Function mission = getFunctionAt(toAddr("0xb68934"));
        println("FUNCTION ParseMissionInfo -> " + (mission == null ? "missing" : mission.getEntryPoint()));
        if (mission != null) {
            DecompileResults result = decomp.decompileFunction(mission, 120, monitor);
            println(result.getDecompiledFunction() == null ? result.getErrorMessage() : result.getDecompiledFunction().getC());
        }
    }
}

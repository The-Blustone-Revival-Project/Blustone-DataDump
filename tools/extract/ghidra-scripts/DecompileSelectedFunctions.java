import java.io.File;
import java.io.PrintWriter;
import java.util.ArrayList;
import java.util.List;

import ghidra.app.decompiler.DecompInterface;
import ghidra.app.decompiler.DecompileResults;
import ghidra.app.script.GhidraScript;
import ghidra.program.model.listing.Function;
import ghidra.program.model.listing.FunctionIterator;
import ghidra.program.model.listing.FunctionManager;

public class DecompileSelectedFunctions extends GhidraScript {
    @Override
    public void run() throws Exception {
        String[] args = getScriptArgs();
        if (args.length < 2) {
            throw new IllegalArgumentException("Usage: DecompileSelectedFunctions.java <output-file> <name-fragment> [...]");
        }

        File outputFile = new File(args[0]);
        File parent = outputFile.getParentFile();
        if (parent != null) {
            parent.mkdirs();
        }

        List<Function> matches = new ArrayList<>();
        FunctionManager functionManager = currentProgram.getFunctionManager();
        FunctionIterator functions = functionManager.getFunctions(true);
        while (functions.hasNext()) {
            Function function = functions.next();
            for (int i = 1; i < args.length; i++) {
                if (function.getName().contains(args[i])) {
                    matches.add(function);
                    break;
                }
            }
        }

        DecompInterface decompiler = new DecompInterface();
        decompiler.openProgram(currentProgram);
        try (PrintWriter out = new PrintWriter(outputFile, "UTF-8")) {
            for (Function function : matches) {
                out.println("===== " + function.getEntryPoint() + " " + function.getName() + " =====");
                DecompileResults result = decompiler.decompileFunction(function, 90, monitor);
                if (result.getDecompiledFunction() == null) {
                    out.println("[DECOMPILATION FAILED] " + result.getErrorMessage());
                }
                else {
                    out.println(result.getDecompiledFunction().getC());
                }
            }
        }
        finally {
            decompiler.dispose();
        }
    }
}

// Dump the names and entry points of functions whose name contains any of the
// given fragments, so a decompile run can be given the exact names to match.
//
//   ListFunctionNames.java <output-file> <name-fragment> [...]

import java.io.File;
import java.io.PrintWriter;
import java.util.ArrayList;
import java.util.List;

import ghidra.app.script.GhidraScript;
import ghidra.program.model.listing.Function;
import ghidra.program.model.listing.FunctionIterator;
import ghidra.program.model.listing.FunctionManager;

public class ListFunctionNames extends GhidraScript {
    @Override
    public void run() throws Exception {
        String[] args = getScriptArgs();
        if (args.length < 2) {
            throw new IllegalArgumentException("Usage: ListFunctionNames.java <output-file> <fragment> [...]");
        }
        File outputFile = new File(args[0]);
        if (outputFile.getParentFile() != null) outputFile.getParentFile().mkdirs();

        List<String> names = new ArrayList<>();
        FunctionManager fm = currentProgram.getFunctionManager();
        FunctionIterator it = fm.getFunctions(true);
        while (it.hasNext()) {
            Function f = it.next();
            for (int i = 1; i < args.length; i++) {
                if (f.getName().contains(args[i])) {
                    names.add(f.getEntryPoint() + "  " + f.getName());
                    break;
                }
            }
        }
        try (PrintWriter out = new PrintWriter(outputFile, "UTF-8")) {
            for (String n : names) out.println(n);
        }
        println("ListFunctionNames: " + names.size() + " matches");
    }
}

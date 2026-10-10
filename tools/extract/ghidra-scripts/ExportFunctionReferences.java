import java.io.File;
import java.io.PrintWriter;

import ghidra.app.script.GhidraScript;
import ghidra.program.model.address.Address;
import ghidra.program.model.listing.Function;
import ghidra.program.model.listing.FunctionManager;
import ghidra.program.model.symbol.Reference;
import ghidra.program.model.symbol.ReferenceManager;

/** Export callers of named functions from the current program. */
public class ExportFunctionReferences extends GhidraScript {
    @Override
    public void run() throws Exception {
        String[] args = getScriptArgs();
        if (args.length < 2) {
            throw new IllegalArgumentException("Usage: ExportFunctionReferences.java <output-file> <name-fragment> [...]");
        }

        File outputFile = new File(args[0]);
        File parent = outputFile.getParentFile();
        if (parent != null) parent.mkdirs();

        FunctionManager functions = currentProgram.getFunctionManager();
        ReferenceManager references = currentProgram.getReferenceManager();
        try (PrintWriter out = new PrintWriter(outputFile, "UTF-8")) {
            for (int i = 1; i < args.length; i++) {
                String fragment = args[i];
                out.println("===== TARGET " + fragment + " =====");
                FunctionIteratorShim iterator = new FunctionIteratorShim(functions.getFunctions(true));
                while (iterator.hasNext()) {
                    Function target = iterator.next();
                    if (!target.getName().contains(fragment)) continue;
                    out.println("TARGET " + target.getEntryPoint() + " " + target.getName());
                    for (Reference reference : references.getReferencesTo(target.getEntryPoint())) {
                        Address from = reference.getFromAddress();
                        Function caller = functions.getFunctionContaining(from);
                        out.println("CALL " + from + " " + (caller == null ? "<no-function>" : caller.getEntryPoint() + " " + caller.getName()) + " " + reference.getReferenceType());
                    }
                }
            }
        }
    }

    private static final class FunctionIteratorShim {
        private final java.util.Iterator<Function> iterator;
        FunctionIteratorShim(java.util.Iterator<Function> iterator) { this.iterator = iterator; }
        boolean hasNext() { return iterator.hasNext(); }
        Function next() { return iterator.next(); }
    }
}

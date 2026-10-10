// Recover known Thumb callback entries that were classified as ARM/data.
// Use only with analyzeHeadless -readOnly -noanalysis. All changes are in the
// temporary program and discarded; original ELF and saved project stay intact.
import java.io.File;
import java.io.PrintWriter;
import java.math.BigInteger;
import ghidra.app.decompiler.DecompInterface;
import ghidra.app.decompiler.DecompileResults;
import ghidra.app.script.GhidraScript;
import ghidra.program.model.address.Address;
import ghidra.program.model.lang.Register;
import ghidra.program.model.listing.Function;

public class DecompileThumbCallbacks extends GhidraScript {
    public void run() throws Exception {
        String[] args = getScriptArgs();
        if (args.length < 2) throw new IllegalArgumentException("output-file followed by proven even Thumb entries");
        Register thumb = currentProgram.getRegister("TMode");
        if (thumb == null) throw new IllegalStateException("ARM TMode context unavailable");
        File output = new File(args[0]);
        if (output.getParentFile() != null) output.getParentFile().mkdirs();
        DecompInterface decompiler = new DecompInterface();
        try (PrintWriter out = new PrintWriter(output, "UTF-8")) {
            for (int i = 1; i < args.length; i++) {
                long value = Long.parseLong(args[i].replace("0x", ""), 16);
                if ((value & 1) != 0) throw new IllegalArgumentException("Pass even instruction entry, not callable Thumb bit");
                Address start = toAddr(value), end = start.add(0x7ff);
                Function old = currentProgram.getFunctionManager().getFunctionAt(start);
                if (old != null) currentProgram.getFunctionManager().removeFunction(start);
                currentProgram.getListing().clearCodeUnits(start, end, false);
                currentProgram.getProgramContext().setValue(thumb, start, end, BigInteger.ONE);
                if (!disassemble(start)) throw new IllegalStateException("Thumb disassembly failed at " + start);
                Function function = createFunction(start, null);
                if (function == null) throw new IllegalStateException("Callback function unavailable at " + start);
                decompiler.openProgram(currentProgram);
                DecompileResults result = decompiler.decompileFunction(function, 120, monitor);
                out.println("===== proven Thumb " + start + " =====");
                if (result.getDecompiledFunction() == null) out.println("FAILED " + result.getErrorMessage());
                else out.println(result.getDecompiledFunction().getC());
                decompiler.closeProgram();
            }
        } finally { decompiler.dispose(); }
    }
}

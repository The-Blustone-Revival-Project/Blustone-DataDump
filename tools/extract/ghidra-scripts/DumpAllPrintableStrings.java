import java.io.File;
import java.io.PrintWriter;

import ghidra.app.script.GhidraScript;
import ghidra.program.model.address.Address;
import ghidra.program.model.mem.MemoryBlock;

public class DumpAllPrintableStrings extends GhidraScript {
    private static boolean printable(byte value) {
        int b = value & 0xff;
        return b >= 0x20 && b <= 0x7e;
    }

    private static void emit(PrintWriter out, Address address, StringBuilder value) {
        if (value.length() >= 3) {
            out.println(address + "\t" + value);
        }
    }

    @Override
    public void run() throws Exception {
        String[] args = getScriptArgs();
        if (args.length != 1) {
            throw new IllegalArgumentException("Usage: DumpAllPrintableStrings.java <output-file>");
        }
        File outputFile = new File(args[0]);
        File parent = outputFile.getParentFile();
        if (parent != null) {
            parent.mkdirs();
        }
        try (PrintWriter out = new PrintWriter(outputFile, "UTF-8")) {
            for (MemoryBlock block : currentProgram.getMemory().getBlocks()) {
                if (!block.isInitialized()) {
                    continue;
                }
                Address address = block.getStart();
                Address start = null;
                StringBuilder value = new StringBuilder();
                while (address.compareTo(block.getEnd()) <= 0) {
                    byte current = currentProgram.getMemory().getByte(address);
                    if (printable(current)) {
                        if (start == null) {
                            start = address;
                        }
                        value.append((char) (current & 0xff));
                    }
                    else {
                        if (start != null) {
                            emit(out, start, value);
                        }
                        start = null;
                        value.setLength(0);
                    }
                    address = address.add(1);
                }
                if (start != null) {
                    emit(out, start, value);
                }
            }
        }
    }
}

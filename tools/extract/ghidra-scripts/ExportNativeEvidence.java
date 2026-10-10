import java.io.File;
import java.io.PrintWriter;

import ghidra.app.script.GhidraScript;
import ghidra.program.model.address.Address;
import ghidra.program.model.listing.Function;
import ghidra.program.model.listing.FunctionIterator;
import ghidra.program.model.listing.FunctionManager;
import ghidra.program.model.mem.Memory;
import ghidra.program.model.mem.MemoryBlock;

public class ExportNativeEvidence extends GhidraScript {

    private static boolean isPrintable(byte value) {
        int unsignedValue = value & 0xff;
        return unsignedValue >= 0x20 && unsignedValue <= 0x7e;
    }

    private static boolean isInteresting(String value) {
        String lower = value.toLowerCase();
        return lower.contains("http") || lower.contains("server") || lower.contains("host")
                || lower.contains("cdn") || lower.contains("socket") || lower.contains("api")
                || lower.contains("login") || lower.contains("auth") || lower.contains("token")
                || lower.contains("json") || lower.contains("version") || lower.contains("asset")
                || lower.contains("download") || lower.contains("upload") || lower.contains("websocket")
                || lower.contains("request") || lower.contains("response") || lower.contains("protocol")
                || lower.contains("sync") || lower.contains("gacha") || lower.contains("stage");
    }

    @Override
    public void run() throws Exception {
        String[] args = getScriptArgs();
        if (args.length < 1) {
            throw new IllegalArgumentException("Usage: ExportNativeEvidence.java <output-file>");
        }

        File outputFile = new File(args[0]);
        File parent = outputFile.getParentFile();
        if (parent != null) {
            parent.mkdirs();
        }

        try (PrintWriter out = new PrintWriter(outputFile, "UTF-8")) {
            out.println("PROGRAM\t" + currentProgram.getName());
            out.println("IMAGE_BASE\t" + currentProgram.getImageBase());

            out.println("[FUNCTIONS]");
            FunctionManager functionManager = currentProgram.getFunctionManager();
            FunctionIterator functions = functionManager.getFunctions(true);
            while (functions.hasNext()) {
                Function function = functions.next();
                String prototype;
                try {
                    prototype = function.getPrototypeString(false, false);
                }
                catch (Exception ignored) {
                    prototype = "";
                }
                out.println(function.getEntryPoint() + "\t" + function.getName() + "\t" + prototype);
            }

            out.println("[RAW_PRINTABLE_STRINGS]");
            Memory memory = currentProgram.getMemory();
            for (MemoryBlock block : memory.getBlocks()) {
                if (!block.isInitialized()) {
                    continue;
                }
                Address address = block.getStart();
                StringBuilder value = new StringBuilder();
                Address start = null;
                while (address.compareTo(block.getEnd()) <= 0) {
                    byte current = memory.getByte(address);
                    if (isPrintable(current)) {
                        if (start == null) {
                            start = address;
                        }
                        value.append((char) (current & 0xff));
                    }
                    else {
                        if (value.length() >= 4) {
                            String text = value.toString();
                            if (isInteresting(text)) {
                                out.println(start + "\t" + text);
                            }
                        }
                        value.setLength(0);
                        start = null;
                    }
                    address = address.add(1);
                }
                if (value.length() >= 4) {
                    String text = value.toString();
                    if (isInteresting(text)) {
                        out.println(start + "\t" + text);
                    }
                }
            }
        }
    }
}

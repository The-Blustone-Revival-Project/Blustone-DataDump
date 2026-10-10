import java.io.File;
import java.io.PrintWriter;

import ghidra.app.script.GhidraScript;
import ghidra.program.model.address.Address;
import ghidra.program.model.mem.Memory;

/** Inspect ARM data words and printable strings at addresses used by decompiler globals. */
public class InspectNativeAddresses extends GhidraScript {
    private static String printable(Memory memory, Address address, int max) {
        StringBuilder text = new StringBuilder();
        try {
            for (int i = 0; i < max; i++) {
                int value = memory.getByte(address.add(i)) & 0xff;
                if (value == 0) break;
                if (value < 0x20 || value > 0x7e) return "";
                text.append((char) value);
            }
        }
        catch (Exception ignored) {
            return "";
        }
        return text.toString();
    }

    @Override
    public void run() throws Exception {
        String[] args = getScriptArgs();
        if (args.length < 2) throw new IllegalArgumentException("Usage: InspectNativeAddresses.java <output-file> <address> [...]");
        File outputFile = new File(args[0]);
        File parent = outputFile.getParentFile();
        if (parent != null) parent.mkdirs();
        Memory memory = currentProgram.getMemory();
        try (PrintWriter out = new PrintWriter(outputFile, "UTF-8")) {
            out.println("PROGRAM\t" + currentProgram.getName());
            for (int i = 1; i < args.length; i++) {
                long value = Long.decode(args[i]);
                Address address = toAddr(value);
                out.println("ADDRESS\t" + address);
                try {
                    int word = memory.getInt(address);
                    long unsignedWord = Integer.toUnsignedLong(word);
                    out.println(String.format("WORD\t0x%08x\tunsigned=%d\twordString=%s", word, unsignedWord, printable(memory, address, 256)));
                    try {
                        Address pointed = toAddr(unsignedWord);
                        out.println("POINTED\t" + pointed + "\tstring=" + printable(memory, pointed, 512));
                    }
                    catch (Exception ignored) {
                        out.println("POINTED\t<invalid>");
                    }
                }
                catch (Exception error) {
                    out.println("WORD\t<error>\t" + error.getMessage());
                }
                for (int offset = -16; offset <= 32; offset += 4) {
                    try {
                        Address nearby = address.add(offset);
                        out.println(String.format("NEAR\t%+d\t%s\t0x%08x\t%s", offset, nearby, memory.getInt(nearby), printable(memory, nearby, 128)));
                    }
                    catch (Exception ignored) {
                        // Ignore unmapped addresses around the requested location.
                    }
                }
            }
        }
    }
}

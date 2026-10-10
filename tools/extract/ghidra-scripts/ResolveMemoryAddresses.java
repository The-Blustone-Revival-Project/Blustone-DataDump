import java.io.File;
import java.io.PrintWriter;

import ghidra.app.script.GhidraScript;
import ghidra.program.model.address.Address;

public class ResolveMemoryAddresses extends GhidraScript {
    private String readAscii(long addressValue) {
        try {
            Address address = toAddr(addressValue);
            StringBuilder value = new StringBuilder();
            for (int i = 0; i < 512 && currentProgram.getMemory().contains(address.add(i)); i++) {
                int b = currentProgram.getMemory().getByte(address.add(i)) & 0xff;
                if (b == 0) {
                    break;
                }
                if (b < 0x20 || b > 0x7e) {
                    return "";
                }
                value.append((char) b);
            }
            return value.toString();
        }
        catch (Exception ignored) {
            return "";
        }
    }

    @Override
    public void run() throws Exception {
        String[] args = getScriptArgs();
        if (args.length < 2) {
            throw new IllegalArgumentException("Usage: ResolveMemoryAddresses.java <output-file> <hex-address> [...]");
        }
        File outputFile = new File(args[0]);
        File parent = outputFile.getParentFile();
        if (parent != null) {
            parent.mkdirs();
        }
        try (PrintWriter out = new PrintWriter(outputFile, "UTF-8")) {
            for (int i = 1; i < args.length; i++) {
                long addressValue = Long.parseLong(args[i].replace("0x", ""), 16);
                Address address = toAddr(addressValue);
                out.println("ADDRESS\t0x" + Long.toHexString(addressValue));
                for (int offset = 0; offset < 16; offset += 4) {
                    Address current = address.add(offset);
                    if (!currentProgram.getMemory().contains(current)) {
                        continue;
                    }
                    long raw = Integer.toUnsignedLong(currentProgram.getMemory().getInt(current));
                    out.println("WORD+0x" + Integer.toHexString(offset) + "\t0x" + Long.toHexString(raw)
                            + "\tASCII_AT_WORD\t" + readAscii(raw));
                }
                out.println("ASCII_AT_ADDRESS\t" + readAscii(addressValue));
            }
        }
    }
}

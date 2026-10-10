// Dump a byte range as hex + ASCII, so a resolved string key can be checked
// against the raw bytes it was read from.
//
//   DumpByteRange.java <output-file> <start-hex> <length>
//
// Why this exists
// ---------------
// When a string key is resolved indirectly (a pc-relative literal slot plus an
// `add rX,pc`), an off-by-one or off-by-four error produces a *plausible but
// truncated* string rather than an obvious failure -- e.g. "s" instead of
// "show_thumbnail", or "n" instead of "group". A reader cannot tell a correct
// resolution from a wrong one without seeing the bytes.
//
// This script prints the raw bytes so the claim "slot X resolves to the string
// S" can be verified directly, including whether S starts exactly at the
// computed address and is immediately preceded by a NUL (i.e. it really is the
// start of a string, not a suffix of a longer one).
//
// Ghidra's memory is used, not the on-disk file: the on-disk value at a literal
// slot is a pre-relocation placeholder.

import java.io.File;
import java.io.PrintWriter;

import ghidra.app.script.GhidraScript;
import ghidra.program.model.address.Address;
import ghidra.program.model.mem.Memory;

public class DumpByteRange extends GhidraScript {

    @Override
    public void run() throws Exception {
        String[] args = getScriptArgs();
        if (args.length < 3) {
            throw new IllegalArgumentException("Usage: DumpByteRange.java <output-file> <start-hex> <length>");
        }
        File outputFile = new File(args[0]);
        if (outputFile.getParentFile() != null) outputFile.getParentFile().mkdirs();

        Address start = toAddr(Long.parseLong(args[1].replace("0x", ""), 16));
        int length = Integer.parseInt(args[2].replace("0x", ""), 16);
        Memory memory = currentProgram.getMemory();

        try (PrintWriter out = new PrintWriter(outputFile, "UTF-8")) {
            out.println("PROGRAM\t" + currentProgram.getName());
            out.println("RANGE\t" + start + "\tlen=" + length);
            out.println();
            StringBuilder ascii = new StringBuilder();
            StringBuilder hex = new StringBuilder();
            for (int i = 0; i < length; i++) {
                Address cur = start.add(i);
                int b;
                try {
                    if (!memory.contains(cur)) {
                        out.println(String.format("%s +0x%03x  <unmapped>", start, i));
                        break;
                    }
                    b = memory.getByte(cur) & 0xff;
                }
                catch (Exception error) {
                    out.println(String.format("%s +0x%03x  <error>", start, i));
                    break;
                }
                hex.append(String.format("%02x ", b));
                ascii.append(b >= 0x20 && b <= 0x7e ? (char) b : '.');
                if ((i + 1) % 16 == 0) {
                    out.println(String.format("%s +0x%03x  %-48s |%s|", start, i - 15, hex.toString(), ascii.toString()));
                    hex.setLength(0);
                    ascii.setLength(0);
                }
            }
            if (hex.length() > 0) {
                out.println(String.format("%s +0x%03x  %-48s |%s|", start, length - 1, hex.toString(), ascii.toString()));
            }

            // A resolved key is only trustworthy if it is NUL-terminated at the
            // right place AND preceded by a NUL, so it is a whole string rather
            // than the tail of a longer one. Report both explicitly.
            out.println();
            out.println("FOR_EACH_CANDIDATE_START");
            for (int i = 0; i < length; i++) {
                Address cur = start.add(i);
                try {
                    if (!memory.contains(cur)) continue;
                    int b = memory.getByte(cur) & 0xff;
                    if (b < 0x20 || b > 0x7e) continue;
                    boolean nulBefore = i > 0 && (memory.getByte(start.add(i - 1)) & 0xff) == 0;
                    StringBuilder value = new StringBuilder();
                    int j = i;
                    while (j < length) {
                        int c = memory.getByte(start.add(j)) & 0xff;
                        if (c == 0) break;
                        if (c < 0x20 || c > 0x7e) break;
                        value.append((char) c);
                        j++;
                    }
                    boolean nulAfter = j < length && (memory.getByte(start.add(j)) & 0xff) == 0;
                    if (value.length() >= 3) {
                        out.println(String.format("    %s +0x%03x = %-16s nulBefore=%s nulAfter=%s",
                                start, i, "'" + value.toString() + "'", nulBefore, nulAfter));
                    }
                }
                catch (Exception ignored) {
                    // Ignore unmapped addresses within the range.
                }
            }
        }
        println("DumpByteRange done");
    }
}
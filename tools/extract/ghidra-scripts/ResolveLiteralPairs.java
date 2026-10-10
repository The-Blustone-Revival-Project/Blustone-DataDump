// Exact relocated literal-slot and ADD-PC instruction pairs, supplied explicitly.
// Usage: ResolveLiteralPairs.java <output> <slot> <add-address> [...]
import java.io.File;
import java.io.PrintWriter;
import ghidra.app.script.GhidraScript;
public class ResolveLiteralPairs extends GhidraScript {
    public void run() throws Exception {
        String[] args = getScriptArgs();
        try (PrintWriter out = new PrintWriter(new File(args[0]), "UTF-8")) {
            for (int i = 1; i + 1 < args.length; i += 2) {
                long slot = Long.parseLong(args[i], 16), add = Long.parseLong(args[i+1], 16);
                long word = Integer.toUnsignedLong(currentProgram.getMemory().getInt(toAddr(slot)));
                long target = word + add + 4;
                StringBuilder s = new StringBuilder();
                for (int j = 0; j < 256; j++) {
                    int b = currentProgram.getMemory().getByte(toAddr(target + j)) & 255;
                    if (b == 0) break;
                    if (b < 32 || b > 126) { s.append("<non-ascii>"); break; }
                    s.append((char)b);
                }
                out.printf("slot=%x word=%x add=%x target=%x string=%s%n", slot, word, add, target, s);
            }
        }
    }
}

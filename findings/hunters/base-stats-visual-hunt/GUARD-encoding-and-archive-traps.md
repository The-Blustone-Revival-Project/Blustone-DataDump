# GUARD — writing UTF-8 notes in this workspace (learned 2026-10-05)

Two research agents damaged `polluted-observations.md` this session, in two
different ways. Both were detected and fully repaired; this file exists so a
third does not happen.

## Rule 1 — never round-trip a UTF-8 file through PowerShell 5.1

`Get-Content` / `Set-Content` / `WriteAllLines` under Windows PowerShell 5.1
default to a system ANSI code page (cp1252). Reading a UTF-8 file and writing it
back **double-encodes** every non-ASCII character.

Observed: a roundtrip re-encoded 112 typographic em-dashes. Repair was a
verified cp1252 inverse transform; 0 replacement chars and 112 em-dashes were
restored afterwards.

**Use Python for any file edit touching non-ASCII**, e.g.
`python -c "..."` with `encoding='utf-8'`, or the `edit`/`write` tools.

## Rule 2 — console output is not evidence of file corruption

PowerShell's console/heredoc rendering can display valid Hangul/CJK as mojibake
even when the file on disk is correct. Twice this was reported as "CJK loss"
and both times the file was fine (561 Hangul chars, 0 U+FFFD confirmed by a
script-file audit).

**Verify the file, not the console dump.** Read bytes with
`[System.IO.File]::ReadAllText($p, [System.Text.Encoding]::UTF8)` and count
`[char]0xFFFD`, Hangul `[\uAC00-\uD7A3]` and CJK `[\u4E00-\u9FFF]` directly.

## Rule 3 — line endings

A PowerShell `Set-Content` pass can also flip the file to CRLF. Check for
`\r\n` and normalize back to LF if the repo expects LF. (One CRLF flip was
inverted with a Python pass.)

## Quick health check for `polluted-observations.md`

```powershell
$p='analysis/research/base-stats-visual-hunt/polluted-observations.md'
$t=[System.IO.File]::ReadAllText($p,[System.Text.Encoding]::UTF8)
"chars: $($t.Length)"
"U+FFFD: $(([regex]::Matches($t,[char]0xFFFD)).Count)"      # must be 0
"em-dash: $(([regex]::Matches($t,[char]0x2014)).Count)"     # must be > 0
"hangul: $(([regex]::Matches($t,'[\uAC00-\uD7A3]')).Count)"  # must be > 0
"CRLF: $(([regex]::Matches($t,"`r`n")).Count)"              # expect 0
"CJK: $(([regex]::Matches($t,'[\u4E00-\u9FFF]')).Count)"    # must be > 0
"mojibake: $(([regex]::Matches($t,'Ã')).Count)"             # must be 0
```

Expected baseline as of 2026-10-05: U+FFFD 0, em-dash 115, hangul 413,
CRLF 0, CJK 107, mojibake 0.

## Related archive trap (same class of mistake)

A rewritten URL is not evidence that content exists. Wayback rewrites `img
src` to `im_` form **even when the image was never captured**, and a CDX 200 row
does not guarantee retrievable bytes — count actual decoded pixels. Always run
a **positive control** against a namespace known to be downloadable before
reading a zero-row CDX result as a real negative.

---

# BROKEN INSTRUMENTS (added 2026-10-06)

Every item here produced a **false zero** in this workspace before it was caught.
They are not subtle, and each one silently converts "not found" into "does not
exist". If a search tool appears to return nothing, check it against this list
before believing the result.

## Wayback / CDX

1. **`https://` is REFUSED on this host** (`WinError 10061`) while `http://`
   works fine. An agent assuming HTTPS reads a working archive as "gone".
2. **The availability API returns false negatives for `?`-query URLs.** Always
   confirm with exact-URL CDX.
3. **The CDX API returns reproducible false negatives** for some exact URLs —
   empty body across three encodings while a direct `id_` fetch returns
   HTTP 200 / 34,670 B.
4. **`id_` at a non-captured timestamp returned 404 once and a correct 200 later.**
   Therefore a **capture set cannot be enumerated reliably**. Never claim "no other
   capture exists".
5. **`resumeKey` and `matchType=domain` both truncate silently to page 1.** A
   paged `matchType=domain` + `filter=` query saturates its own `limit=20000` and
   must be *paged*, not raised. Under-paging turned a 3,193-id census into a
   recorded "131 ids" — a **24.4× undercount**.
6. **`matchType=prefix` barely covers anything** on some boards, because it hits
   the `/board/<id>` **path** form this archive barely captured.
7. **15 byte-identical `域名停靠` parking pages** (2021-07-29, 3,357 B, one shared
   SHA-256) sit in this corpus and make items falsely appear to *lose* their
   tables in a later capture. Check the hash before believing content vanished.

## Miraheze (`blustone.miraheze.org` — live)

8. **CirrusSearch is UNINDEXED.** `srsearch=accessory` → 0 results despite 103
   occurrences on the site; `intitle:Bella` → 0; but `the` → 46 across 1,254
   pages. **All `insource:` results from this wiki are void.** Anyone using its
   search as an oracle gets false zeros.
9. **`list=allpages` without `apnamespace` returns namespace-0 only.** The site
   has **1,254 pages** but a bare `allpages` query returned **335** — which then
   read as "335 pages is all there is". Walk `list=allrevisions` instead:
   **1,567 revids** vs the site's own "1,568 edits" statistic.
10. A prior note's "`Template:Equipment` 404s" was **a retrieval artefact** — it
    fetches fine and holds the canonical schema. Confirm before recording a 404.

## Local tables

11. **"Mon" matches "Money"** in substring searches over the native string table
    — 32 false hits in `CSRPopUp*` (`SetMoney`, `CSRPopUpNoMoney`). Anchor tokens.
12. **`native-all-strings.tsv` / `native-evidence.tsv` contain ZERO Hangul.** They
    are printable-ASCII exports. Any locale-string search there returns false
    zeros — use `UI_TEXT_RO` / `UI_JSON_RO`.
13. **Never hand-write Unicode codepoints for a search term.** `능력치` typed as
    `U+B2A5 U+BC25 U+CE60` returns 0 everywhere; the real value is
    `U+B2A5 U+B825 U+CE58`. Slice the term out of the data instead.
14. **CRLF has appeared silently.** Once, 11 files flipped to CRLF (including
    `coverage.md`) with content intact. Check folder-wide `\r` count, not just the
    file you edited.
## Fetch throughput (learned 2026-10-08)

15. **Reuse one HTTP session per thread.** Opening a fresh `requests.Session` per
    target is a **client defect**, not an archive rate limit. Measured on the same
    archive: per-target sessions gave **~4 requests/min with 24 % transport
    failures**; **one shared session per thread** gave **307/min peak, 3,238x
    HTTP 200 of 3,243 attempts, zero `000`**. A "rate limit" that is really a
    reconnect storm will masquerade as a content negative.
16. **archive.org refuses connections at 8 workers** on this host and that refusal
    is indistinguishable from missing content. Keep concurrency low and treat a
    burst of connection failures as an instrument fault, not a negative.
17. **CDX `matchType=domain` truncates at ~170-207 rows regardless of paging.**
    Enumeration must be **by crawling**. By contrast a `url=` **prefix** census
    (paged, `collapse` unset) returned all 344 image URLs untruncated — use the
    query shape that matches the corpus, not the one that feels standard.
18. **A `prefix` query with a literal `*` returns 0 bytes** and reads as "no
    pages". And an exact-URL CDX can return the Internet Archive's
    **"Temporarily Offline"** page as a body — hash-check every body.
19. **Search the shipped client for placeholder numerals before expecting a
    number.** The transcendence panel's four numeric rows are all the placeholder
    `10000`, which positively proves the step factors are **server-side** — a
    whole avenue (string archaeology for 1.20 / 1.30) is closed, not merely
    unfruitful.

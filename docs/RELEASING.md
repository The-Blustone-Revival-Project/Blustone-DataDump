# Dated stats releases

Version/tag: `YYYY-MM-DD`, using the current date in **Asia/Jerusalem**. Additional releases on the same date use `.2`, `.3`, and so on. Title: `Blustone DataDump YYYY-MM-DD[.N]`. Never overwrite a dated snapshot or reuse its tag.

Every release is published, public and regular: no draft or prerelease options. The newest snapshot is explicitly Latest. A snapshot describes the research corpus at its cutoff; it does not change the historical date/version/context of any observation.

## Required assets

1. `BLUSTONE-Stats.md`: readable numerical observations, screenshot/gear tables and unknowns.
2. `BLUSTONE-Evidence.md`: provenance, coverage, conflicts, source hashes and reproduction.
3. `BLUSTONE-Stats.json`: machine-readable full datasets and incremental record changes.
4. `RELEASE-MANIFEST.json` and `SHA256SUMS.txt`.

Artifact names stay stable across versions; their contents carry the version/date. Git tags and assets preserve earlier snapshots. Existing numerical values must not become recovered base stats merely because they appear in a release.

## Prepare

```powershell
python tools/normalize/validate-datasets.py
python tools/releases/build-snapshot.py --date 2026-10-10
```

For another publication that day, add `--revision 2`. When a previous snapshot exists, provide its JSON through `--previous-json`; Added/Changed/Removed counts include changes in context and provenance.

## Publish

The GitHub `Publish dated snapshot` workflow chooses today's next available date revision, validates datasets, downloads the previous public JSON for comparison, generates assets and creates a regular Latest release. Run it only after the intended data changes are reviewed and pushed.

For local preparation, snapshots under `releases/<version>/` can be committed with the reviewed source. The first snapshot is committed there. Publication must point to the exact source commit and must never include `local/`, private captures, raw telemetry or account data.

Incremental change counts cover both normalized dataset records and the curated screenshot/equipment tables, including changed provenance/context. A new research table or corrected equipment reading must not disappear behind unchanged normalized-record totals.

# Blustone DataDump

Evidence and datasets for reconstructing BLUSTONE. This repository owns game-data research; it is not the server or diagnostic APK project.

## Start here

- [Dataset index](catalog/README.md): identities, stat observations, skills, campaign IDs, Episode graph and equipment.
- [Coverage](catalog/coverage.json): generated identity and observation counts, with unknowns kept explicit.
- [Evidence rules](docs/EVIDENCE.md): original data, observations, inference and fixtures remain distinct.
- [Research findings](findings/README.md): organized by game system, including rejected hypotheses.
- [Source inventory](sources/README.md): immutable tables, native evidence, community material and observations.
- [Migration records](manifests/README.md): legacy-path map and copy verification; full private ledger is ignored under local/migration.

## Rebuild and validate

```powershell
python tools/normalize/build-datasets.py
python tools/normalize/validate-datasets.py
```

Both commands work from any working directory and use only the Python standard library. Source bytes are preserved; generated records carry a source hash and exact locator. Numerical observations are not automatically original base stats.

## Storage

Public, small, reviewed text belongs in Git. Raw community captures and screenshots are copied under sources/ but ignored pending content review. local/ holds private phone/account snapshots, emulator images, historical build experiments and the complete old Git metadata; it must never be published. The per-file migration ledger identifies every copy.

The repository LICENSE applies to authored project material, not an assertion of rights over recovered proprietary game assets or third-party archives.

## Dated stats snapshots

Each [release](https://github.com/The-Blustone-Revival-Project/Blustone-DataDump/releases) preserves the stats/evidence corpus up to its stated date. Download `BLUSTONE-Stats.md` and `BLUSTONE-Evidence.md` for readable tables, source status and remaining unknowns. Versions use `YYYY-MM-DD`, with `.2`, `.3` for additional snapshots that day. See [release policy](docs/RELEASING.md).

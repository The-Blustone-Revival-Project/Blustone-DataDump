# Migration and reproducibility manifests

The public path map covers publishable research/source files and links old relative paths to their new owners. Full per-file SHA-256, source metadata, conflict preservation and verification status are in ignored local/migration/ledger.sqlite and ledger.ndjson. Private paths and captures stay out of public manifests.

Copy verification preserves original bytes. Later documentation/tool adaptations carry transformation hashes and preserve the original snapshot separately. exports/server/manifest.json pins the source inputs consumed by the Server repository.

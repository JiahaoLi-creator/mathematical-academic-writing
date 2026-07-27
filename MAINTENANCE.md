# Public Maintenance Boundary

This repository is the public runtime distribution of the accepted v0.2.0 skill. It does not
contain the full release harness.

The private gate uses source PDFs, extracted text, an evidence registry, blind regression oracles,
source-derived notebook fixtures, detached approvals, and independent semantic review. Those
materials are excluded for copyright, privacy, and oracle-integrity reasons.

## Public checks

Run:

```bash
python3 -B scripts/verify_public_core.py
```

This verifies the public allowlist and the accepted eight-file core binding recorded in
`provenance/public-release.v1.json`.

## Behavioral changes

The v0.2.0 runtime and provenance binding are immutable. Any change to `SKILL.md`,
`agents/openai.yaml`, `references/`, or `project_profiles/` starts a new candidate version. That
candidate becomes an accepted release only after it passes the full private deterministic,
semantic, mutation, and human-review gates and receives its own public provenance record.

Documentation-only changes may retain the core binding when all eight runtime files remain
byte-identical and the public verifier passes.

The JSON files under `tests/` are notice-only placeholders. They preserve the runtime links in
`SKILL.md` without disclosing blind or source-derived fixtures.

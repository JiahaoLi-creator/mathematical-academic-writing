# Public Maintenance Boundary

This repository is the public runtime distribution of the accepted v0.4.3 skill. It does not
contain the full private release harness.

Source PDFs, extracted text, evidence registries, blind oracles, source-derived notebook fixtures,
detached approvals, evaluator outputs, signing keys, and trust configuration remain private.

## Public checks

Run:

```bash
python3 -B scripts/verify_public_core.py
```

The check enforces the closed 33-file public allowlist and the accepted seventeen-file core binding
in `provenance/public-release.v1.json`, plus link and limited credential/path checks.

## Behavioral changes

Changes to `SKILL.md`, `agents/openai.yaml`, `references/`, or `project_profiles/` require a new
accepted private candidate and a new public provenance record. Documentation-only changes may
retain the core binding only while all seventeen runtime files remain byte-identical.

The public v0.4.3 runtime is derived from accepted, signed private candidate
`candidate-ebc94b8f4fc8faaa`. Sixteen files are byte-identical. The sole sanitization removes three
local PDF link targets from `references/statistical_source_map.md`, preserving link labels,
bibliographic facts, locators, and routing rules. The exact transformation is bound in provenance.
No additional runtime alteration is authorized by that path-sanitization policy.

The final private candidate used explicitly recorded governance-only reuse of the exact prior
accepted 4+4 sample; its provenance must not be described as fresh evaluation contexts.

The JSON files under `tests/` are notice-only placeholders. They contain no private cases,
expected answers, evaluator outputs, or source-derived fixtures.

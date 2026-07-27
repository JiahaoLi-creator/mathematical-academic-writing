# Quick-Start Prompts

These examples show how to supply the task, genre, reader, sources, and preservation constraints.
Replace the bracketed source descriptions with material you can provide to Codex.

## Revise a visual interpretation

```text
$mathematical-academic-writing

Task: Revision
Genre: Visual companion
Primary source: [lecture notes, chapter or section]
Audience: Students meeting the topic for the first time

Preserve every defined symbol, formula, parameter, and figure number. Rewrite the
interpretation as one concise paragraph. Explain the encoding before the conclusion,
match every verb to its evidence, and remove generic defensive disclaimers.

Current passage:
[paste the caption or interpretation]
```

Expected shape: a compact working register followed by the revised paragraph. Notes appear only
when a choice affects mathematical meaning, evidence strength, source fidelity, or an unresolved
ambiguity.

## Review theorem-proof exposition

```text
$mathematical-academic-writing

Task: Review
Genre: Theorem-proof exposition
Governing source: [paper, textbook, or supplied derivation]

Check the passage for missing assumptions, changed quantifiers, implication direction,
notation drift, and repeated conclusions. Return only prioritized findings. Do not rewrite
the passage.

Passage:
[paste the theorem and proof]
```

For an explicit line-by-line audit, ask for the action labels `Keep`, `Rewrite`, `Compress`,
`Delete`, and `Flag`.

## Verify a computational claim

```text
$mathematical-academic-writing

Task: Verification
Genre: Computational analysis
Primary result: [theorem or exact benchmark]
Experiment: [code, output, parameters, seed policy, and error definition]

Identify every material claim and its assumptions. Classify each as verified,
unsupported, ambiguous, or incorrect. Separate theorem support from numerical evidence,
Monte Carlo uncertainty, and discretisation error. Do not correct the prose unless I ask.
```

Verification requires the relevant source or derivation. These instructions require missing
support to be flagged and prohibit invented theorems, citations, parameters, and numerical results.

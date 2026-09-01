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

Expected shape: the revised paragraph, plus a compact register or note only when a choice affects
mathematical meaning, evidence strength, source fidelity, or an unresolved ambiguity.

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

## Draft a research contribution

```text
$mathematical-academic-writing

Task: Draft
Genre: Research article introduction
Primary sources: [verified papers or supplied notes]
Main result: [theorem, proposition, algorithm, or experiment]

Draft one contribution paragraph. Tie the claimed limitation to a supplied source,
the contribution to the named result, and the conclusion to its actual assumptions.
Return Flag for any novelty or priority claim that the supplied sources do not establish.
```

## Plan or audit a statistical analysis

```text
$mathematical-academic-writing

Task: Analysis
Genre: Statistical analysis plan
Question and intended use: [description, inference, prediction, causation, or decision]
Data: [population, sample, unit, variables, design, missingness, and dependence]
Primary sources: [protocol, data dictionary, method reference, or reporting standard]

Specify the estimand or prediction target, primary method, uncertainty procedure,
diagnostics, sensitivity or multiplicity checks, and reporting boundary. Mark every
unavailable input and conditional branch; do not invent data, results, or design details.
```

Expected shape: an analysis contract that keeps population, sample, design, target, estimator,
estimate, uncertainty, and generalization scope distinct.

## Verify a notebook or rendered artifact

```text
$mathematical-academic-writing

Task: Verification
Artifact: [notebook, code output, TeX, HTML preview, or PDF]
Governing source: [theorem, derivation, or course notes]
Required depth: [text-bound | source-bound | execution-bound | render-bound]

Check the mathematical claim, correction authority, execution freshness, and visible
rendering needed for the requested depth. Report the deepest level actually reached;
do not change valid mathematics to repair a rendering defect.
```

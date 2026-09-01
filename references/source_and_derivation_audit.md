# Source and Derivation Audit

Load this reference for Verification, source conflicts, suspected mathematical errors, citation checks, or source-authorized correction.

## 1. Fix the audit boundary

Record:

- the claim or derivation under review;
- the designated primary source and any auxiliary source;
- the verification depth required to settle the claim and, separately, the deepest level actually
  reached: text-bound, source-bound, execution-bound, or render-bound;
- whether the user requested diagnosis only or authorized correction.

Do not treat an auxiliary source as permission to overwrite the primary source. If the hierarchy is not supplied, report which source was treated as governing and why.

## 2. Classify the issue before editing

| Classification | Meaning | Default action |
| --- | --- | --- |
| Typographical or local notation error | The intended statement is uniquely recoverable and downstream mathematics uses it consistently. | Record the repair; correct only with authorization. |
| Ambiguous | Two or more mathematically coherent readings remain. | Preserve the source and `Flag` the missing disambiguation. |
| Internally inconsistent | Statements in the governing material cannot all hold under one notation and assumption set. | Identify the minimal conflicting set; do not choose silently. |
| Unsupported | The claim may be true, but the supplied evidence does not establish it. | Lower the claim or request the missing source or check. |
| Incorrect | A decisive counterexample, derivation, or governing source contradicts the claim. | Separate diagnosis from any corrected wording. |

### Fix the verdict target

Decompose a compound sentence before assigning a verdict. In particular, separate:

- the object-level conclusion or property being asserted; and
- the warrant, implication, or procedure claimed to establish it.

Missing identification, calibration, source support, or execution evidence makes the affected
conclusion `unsupported`; absence of support is not a counterexample. A warrant or implication is
`incorrect` only when a governing source, derivation, calculation, or counterexample decisively
contradicts that claim unit. If the output format permits only one verdict, state the exact claim unit
to which it applies. Do not use a refuted warrant to label an unestablished conclusion false, and do
not use uncertainty about a conclusion to protect a refuted universal implication.

For example, an observational coefficient without causal identification leaves the causal effect
unsupported; a supplied confounding counterexample can instead make a universal adjustment-implies-
causation rule incorrect. A posterior interval without calibration leaves its frequentist coverage
unsupported; a supplied coverage counterexample can make an automatic-coverage rule incorrect.

## 3. Build a correction ledger

For every material discrepancy, record:

| Field | Content |
| --- | --- |
| Location | theorem, equation, paragraph, code cell, or figure |
| Source text | exact mathematical claim under review |
| Issue | classification above |
| Decisive evidence | theorem, calculation, counterexample, output, or render observation |
| Scope | what changes and what remains valid |
| Authority | user request or source that authorizes correction |
| Correction | proposed wording or formula, if authorized |

This ledger prevents a repair in one location from silently changing notation or conclusions elsewhere.

## 4. Reconstruct the decisive dependency

Check the shortest chain that settles the claim:

1. define every object and domain;
2. list assumptions and quantifiers;
3. reproduce the cited theorem or derivation step in the relevant scope;
4. test endpoints, zero denominators, sign conventions, dimensions or units, and special parameter cases;
5. check every interchange of limit, expectation, integral, derivative, optimization, or conditioning against its hypotheses;
6. distinguish pathwise, almost-sure, expectation, distributional, and numerical statements;
7. compare the resulting conclusion with the exact wording under review.

When a numerical contrast is part of the decisive evidence, carry its supplied values into the
reader-facing verification rather than replacing them with a qualitative summary.

For stochastic calculus, also check filtration, predictability, stopping or localization, integrability class, horizon, and whether a local martingale must be a true martingale.

For statistical work, also check the target population, sample and selection mechanism, estimand,
estimator, model, identification assumptions, uncertainty procedure, finite-sample or asymptotic
regime, and whether the wording is descriptive, associational, predictive, or causal. Reconstruct the
test, interval, posterior, resampling, or evaluation protocol that supplies the claimed interpretation.

## 5. Source conflicts

When sources disagree:

1. quote or transcribe only the minimal conflicting mathematical content;
2. normalize notation in a separate comparison line, never inside the source quotation;
3. determine whether the difference is convention, scope, typo, or substance;
4. prefer the user-designated primary source for course notation and boundaries;
5. retain the conflict as `ambiguous` if available evidence does not settle it.

A later source, a familiar formula, or majority usage is not by itself correction authority.
An ambiguity flag is complete only when it identifies the minimal conflicting set and names the
missing evidence that would select a reading. Do not collapse distinct supplied facts—such as absent
audio, competing visible symbols, and a later inconsistent use—into a generic statement that the
source is unclear.

## 6. Verification verdict

Return one of:

- `verified`: the claim follows within its stated assumptions and scope;
- `unsupported`: no contradiction is established, but necessary evidence is missing;
- `ambiguous`: multiple readings or unresolved source conflict remain;
- `incorrect`: decisive evidence contradicts the claim.

Name the verification depth actually reached. A rendered notebook can fail even when its source is mathematically correct; an executing notebook can still contain an unsupported interpretation.

Do not label an unavailable check as reached. For example, when a citation is named but no copy,
extract, or verified record is supplied, the audit may identify the missing source-bound work while
remaining text-bound.

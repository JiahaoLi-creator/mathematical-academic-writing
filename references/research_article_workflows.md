# Research-Article Workflows

Use this reference for article-scale drafting, revision, review, referee reports, and responses. The supplied sources govern factual and citation claims.

## Abstract

Build the abstract in this order when the evidence supports each part:

1. problem and mathematical setting;
2. specific limitation or unresolved question;
3. method or main construction;
4. principal result with scope and assumptions;
5. implication or boundary.

Do not promote a numerical pattern to a theorem or invent a novelty claim. Omit background that does not sharpen the contribution.

## Introduction and contribution map

Tie each contribution to a concrete problem and later result:

| Contribution claim | Prior limitation or question | Result that supports it | Scope boundary |
| --- | --- | --- | --- |
| Example | supplied source statement | theorem, proposition, algorithm, or experiment | assumptions and regime |

Use “we prove” only for a proved result, “we derive” for an exact derivation, and “we observe” or “we estimate” for computational evidence. A contribution list should not restate the same result under several labels.

## Related work and citations

- Attach each citation to the claim it supports.
- Distinguish historical priority, technical dependency, methodological comparison, and empirical comparison.
- Do not infer a paper's content from title, venue, or memory.
- If a requested gap or attribution lacks a supplied or verified source, return `Flag` rather than drafting it as fact.
- Preserve the difference between “first,” “extends,” “applies,” “compares,” and “is related to.”

Literature discovery is a separate research task. Apply this skill once the relevant sources or verified notes are available.

## Theorems, proofs, and methods

State assumptions before the result that uses them. Expose the proof mechanism rather than narrating algebra line by line. In a method section, specify the mathematical object, input, output, admissible class, objective or estimator, and conditions under which the method is defined.

For computational methods, distinguish:

- mathematical approximation error;
- discretization or truncation error;
- optimization or solver tolerance;
- Monte Carlo uncertainty;
- data or model uncertainty.

## Results and discussion

Lead with the result and its support. Report the benchmark, metric, units, sample size or mesh, and uncertainty needed to interpret it. Compare only quantities defined on compatible samples, horizons, or parameter regimes.

Discussion may explain mechanism, sensitivity, or limitation. It must not add an uncited theorem, causal claim, generalization, or robustness claim absent from the results.

## Conclusion

Synthesize what the results jointly establish and the boundary that matters next. Omit a conclusion that only repeats the abstract or section summaries.

## Referee report

Separate:

1. summary of the paper's claimed contribution;
2. correctness and source-fidelity issues;
3. major issues affecting validity or interpretation;
4. minor exposition or notation issues;
5. actionable requests, each tied to a location and mathematical reason.

Do not rewrite authorial choices merely to match personal style.

## Response to reviewers

For each comment, state the decision, mathematical reason, exact change, and location. If the manuscript does not adopt a request, answer the substance and show why the verified statement or scope is retained. Do not claim that an issue is resolved until the revised artifact supports that claim.

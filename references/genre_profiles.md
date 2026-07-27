# Genre Profiles

Select one primary genre for each section. Combine profiles only when the document genuinely combines their functions.

## Research article

Typical dependency:

```text
precise problem
-> relevant gap
-> contribution
-> assumptions and method
-> result
-> implication and boundary
```

- Connect each contribution to a specific unresolved question or limitation in prior work.
- Put citations beside the historical, technical, comparative, or empirical claim they support.
- State assumptions near the result or method that uses them.
- Use first person with concrete verbs such as `derive`, `characterize`, `establish`, `construct`, or `compare` when it clarifies agency.
- Let the conclusion interpret a mechanism, boundary, testable implication, or open problem. A short ending is complete when the argument is complete.

## Theorem-proof exposition

Typical dependency:

```text
mathematical need
-> definition or assumptions
-> result
-> proof dependency
-> consequence or counterexample
```

- Keep theorem statements atomic: objects, assumptions, quantifiers, and conclusion.
- Begin a proof with the key construction, identity, or reduction. Add a one-sentence strategy when the route is genuinely non-obvious.
- Place each equation beside the reason that justifies it.
- Cite the precise prior definition, lemma, or theorem used by a step.
- End when the result follows. Add a remark only when it changes interpretation, scope, or later use.
- Treat counterexamples and failed converses as mathematical results rather than stylistic caveats.

## Textbook or lecture explanation

Typical dependency:

```text
concrete question or obstruction
-> definition
-> minimal example
-> result
-> interpretation or exercise
```

- Introduce terminology when the reader has a reason to need it.
- Let one reusable example grow across definitions and results.
- Explain the hard transition; allow routine algebra to remain compact.
- Match the declared reader level consistently.
- Use exercises only when they complete a proof, test a definition, build a dependency, or extend a result.

## Computational or empirical analysis

Typical dependency:

```text
target quantity
-> data or simulation design
-> estimator or algorithm
-> uncertainty and error
-> evidence
-> local conclusion
```

- Distinguish latent quantities, observed variables, proxies, simulated quantities, and exact benchmarks.
- State parameters, sample size, seed policy, time mesh, tolerance, and benchmark when they affect reproducibility.
- Separate Monte Carlo uncertainty, discretisation error, model error, and measurement error.
- Report the direction and consequence of a limitation.
- Connect computational cost and convergence rate to the method when they matter to use.

## Visual companion

Typical dependency:

```text
conceptual question
-> minimum formal statement
-> visual or numerical construction
-> concise interpretation
```

- Use the primary course source to set notation and scope.
- Prefer one figure with one main explanatory job.
- Keep captions descriptive and interpretations analytical.
- Give a beginner enough information to read the encoding, pattern, and mathematical connection.
- Use the detailed rules in [visual_companion.md](visual_companion.md).

## Authorial voice

Academic voice is a stable way of making mathematical decisions, not a collection of elevated phrases. Use direct sentences, precise verbs, and natural asymmetry in paragraph length. Maintain one name for each technical object. Explain local judgment when it helps the reader follow a derivation, modeling choice, or interpretation.


# Visual Companion Guidance

## Purpose

A visual companion supports classroom explanation through figures, numerical experiments, and short analysis. It helps a beginner connect a formal statement to a visible mathematical relationship.

## Source and scope

- Use the designated primary source for notation, theorem scope, and topic boundaries.
- Use auxiliary sources for clarification and figure design.
- Keep the notebook inside its assigned topic unless a short prerequisite bridge is needed.

## Section shape

Use the smallest sequence that carries the idea:

```text
conceptual question
-> minimum formal statement
-> figure or experiment
-> interpretation
```

Short notebooks finish after the final substantive section. Add a summary only when it synthesizes several dependencies that the body has not already connected.

## Figure responsibilities

Give each figure one main explanatory job.

- A geometry figure displays a structural relation.
- A path figure displays evolution or refinement.
- A distribution figure compares stochastic behavior.
- A convergence figure displays error, uncertainty, or scaling.
- A computational diagram displays an algorithm or dependency.

## Caption and interpretation

Place the interpretation in its own paragraph below the caption. Follow the project's layout profile for image alignment, captions, and body text.

The caption identifies what is plotted:

- objects;
- variables and axes;
- panels or encoding;
- parameters needed to identify the experiment.

The interpretation explains:

1. how to read the encoding;
2. what pattern or numerical relation is visible;
3. how that pattern connects to the mathematical statement.

Vary the number of sentences to fit the figure while preserving this logic.

## Beginner-facing explanation

- Define the object needed to read the figure.
- Explain a new encoding before interpreting it.
- Give one concrete numerical reading when a scale, marker, or error measure is unfamiliar.
- Connect local observations to the formal statement using the lecture notation.
- Preserve details that answer a likely first question, such as what `n=32` means or how a stake rule is chosen.
- Remove repeated descriptions of the same axis, panel, or theorem.

## Positive, evidence-matched language

State what the figure encodes and displays. Use the evidence ladder in [mathematical_integrity.md](mathematical_integrity.md) to distinguish theorem, derivation, example, figure, simulation, and observational claims.

A real ambiguity is resolved by naming the encoding, class, or evidence source directly.

## Numerical experiments

Record the settings that affect interpretation:

- seed policy;
- parameter values;
- number of paths or observations;
- partition size or time mesh;
- benchmark formula;
- error definition and uncertainty interval.

Separate Monte Carlo uncertainty from discretisation, approximation, model, and measurement error.

## Notebook editing safeguards

- Preserve valid notebook JSON and elements outside the requested edit scope.
- Keep captions and interpretations as separate blocks.
- Use adjustable code-cell parameters when they provide classroom interaction without fragile exports.
- Rerun the notebook and inspect the rendered preview after content changes.

## Final visual-companion check

1. Does every section belong to the lecture chapter?
2. Does each figure have one main job?
3. Can a beginner identify the encoding before reading the conclusion?
4. Does the interpretation add analysis beyond the caption?
5. Are theorem, example, figure, and simulation claims distinguished?
6. Are notation and numerical settings preserved?
7. Can any sentence be removed without losing mathematical or teaching value?

# Advanced Mathematical Statistics Course-Notes Profile

This is an optional project extension, not the skill's general statistical-analysis core. Apply it
only to the ANU Advanced Mathematical Statistics / Statistical Learning workflow that turns Canvas
recordings, handwritten board states, course handouts, READINGS, and textbooks into Chinese
textbook-style study notes. For ordinary data analysis, use
[general statistical analysis workflows](../references/statistical_analysis_workflows.md).

## Source hierarchy and roles

1. The lecture recording determines the lecture boundary, teaching sequence, spoken qualifications,
   and course notation actually used.
2. Handwritten board states, course slides, and lecture-specific handouts supply visible formulas,
   numerical settings, examples, and completed derivations.
3. The user-designated textbook sections and Canvas READINGS clarify definitions, theorem conditions,
   historical context, and omitted derivation steps.
4. Editorial derivations, examples, figures, and explanations may connect the material, but must be
   labeled as reconstruction or supplement rather than attributed to the lecturer.

Treat all layers as checkable evidence, not as automatically error-free. When a recording conflicts
with a board state or source, use the correction ledger in
[source and derivation audit](../references/source_and_derivation_audit.md). Preserve unresolved
notation or parameterization changes instead of silently normalizing them.

## Evidence labels

Use the smallest label set needed for traceability:

- **recording**: supported by audible speech, with lecture part and timestamp when material;
- **board reconstruction**: supported by an inspected frame or final board state;
- **course-supplied**: supported by a slide, handout, code file, or assigned course document;
- **derived**: reconstructed by an explicit calculation from stated assumptions;
- **supplement**: added from a named textbook or reading to improve continuity or interpretation;
- **ambiguous**: the audio, handwriting, notation, or source conflict does not determine one safe reading.

Do not call an edited or corrected transcript verbatim. When audio has no subtitles, retain uncertain
speech as an evidence problem; do not fill silent writing intervals or inaudible formulas with
plausible text.

For a disputed handwritten symbol, record the audio state, each plausible visible reading, and any
later use that distinguishes those symbols. A generic note that the frame is unclear is not enough
when the supplied evidence contains a specific conflict.

When the safe output is a flag rather than prose, keep every material locator in the rationale,
including the lecture part or timestamp that identifies the disputed evidence. An empty draft must
not make the diagnostic trail less specific.

## Recording-to-chapter workflow

1. Confirm the lecture number, recording parts, durations, and the course page that defines the scope.
2. Build a timestamped topic and board-state map before drafting prose.
3. Reconcile audio, board frames, handouts, and course notation. Record every material ambiguity.
4. Match only the textbook sections and READINGS that support the lecture's actual topic boundary.
5. Lock the model, population or distribution, parameter or functional, estimator, assumptions,
   asymptotic regime, and uncertainty formulas.
6. Reconstruct decisive derivations and check special cases, signs, parameterizations, dimensions, and
   numerical constants.
7. Draft a continuous Chinese chapter. Use the raw transcript and frames as evidence layers rather
   than as the default reader-facing structure.
8. Maintain a short source-and-derivation audit that separates lecture content from additions and
   records source-authorized corrections.
9. Compile and inspect the final PDF or HTML at the source, execution, and render depths actually used.

## Textbook-style chapter shape

Prefer a continuous learning dependency:

```text
concrete statistical question
-> population, model, and target
-> estimator or procedure
-> assumptions and derivation
-> statistical interpretation and intuition
-> example, simulation, or diagnostic
-> limitation, common misreading, or next dependency
```

Use paragraph-form introduction, interpretation, and intuition where they explain why a definition is
needed, how a derivation works, or what a result means statistically. Keep formulas and board images
inside the narrative rather than making the chapter a sequence of isolated blocks. Remove exhaustive
timestamp transcripts from the reader edition unless the user requests a transcript artifact.

For beginner-facing notes:

- define each technical object before its first consequential use;
- explain the transition that carries the statistical idea, not every routine algebraic line;
- pair a formal statement with an adjacent verbal interpretation when it introduces a new object;
- preserve English technical terms such as `estimand`, `influence function`, `sandwich covariance`,
  `contamination`, and `breakdown point` where they aid later source reading;
- keep one notation and parameterization, except where the source itself changes—then name the change.

## Course-specific statistical shields

When present, distinguish:

- a model parameter from a statistical functional and a pseudo-true target under misspecification;
- Fisher consistency inside the core model from target behavior outside it;
- model-based standard error from sandwich or robust standard error;
- variance correction from target robustness;
- point contamination, local contamination, a fixed contamination neighborhood, and global breakdown;
- bounded influence, gross-error sensitivity, asymptotic variance, and efficiency;
- theorem-level asymptotics from a finite-sample course simulation;
- a stale code comment from the implemented data-generating mechanism and computed quantities.

A simulation may illustrate an efficiency/robustness trade-off under its stated sample size, replicate
count, seed policy, and contamination mechanism. It does not prove the general robustness property.

## Source and artifact checks

- Cite recording parts and timestamps for disputed speech or notation, and page/section locators for
  textbooks, READINGS, slides, and handouts.
- Verify copied formulas against the original board frame at usable resolution; never rely on OCR alone
  for a material symbol.
- Inspect board-image crops, Chinese fonts, equations, tables, citations, overflow, and page breaks in
  the final reader artifact.
- Keep raw recordings, frames, and transcripts out of a public release unless the user has the right to
  distribute them. A public-safe edition must separate original prose from restricted course assets.

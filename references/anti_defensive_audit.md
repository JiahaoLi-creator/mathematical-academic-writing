# Anti-Defensive Functional Audit

Defensive writing organizes prose around hypothetical objections instead of the mathematical task. Audit the function of a sentence before changing its wording.

## Decision sequence

For a sentence that contains a caveat, hedge, contrast, clarification, or negation:

1. Identify the claim or object it modifies.
2. Decide whether it changes validity, scope, evidence, logic, or necessary reader guidance.
3. Retain mathematically necessary content beside the affected claim.
4. Express a valid scope condition positively when possible.
5. Delete material whose only function is to anticipate an unspecified objection.

When positive reframing requires a purpose, object, encoding, observed pattern, or scope absent from the source, choose `Flag` and request the missing context.

## Functional classes

| Class | Action |
| --- | --- |
| Mathematical assumption | Keep beside the theorem, formula, or construction. |
| Essential negation | Keep its exact logical force. |
| Failed converse or counterexample | Keep as a mathematical result. |
| Evidence-based qualification | State the evidence type and uncertainty source precisely. |
| Method or data limitation | State its source, direction, and effect once. |
| Useful conceptual contrast | Keep when the contrast advances the argument. |
| Positive scope available | Rewrite around the object or admissible class. |
| Redundant clarification | Merge or delete. |
| Hypothetical-reader disclaimer | Delete or replace with the delayed mathematical content. |
| Adjacent formal restatement | Keep when it translates the object the reader has just met. |
| Recapitulated conclusion | Delete; replace with the theorem, equation, or figure number. |
| Advance summary of a later section | Delete unless it fixes notation the reader needs now. |

## Positive scope

Name the object, class, question, or contribution directly.

Defensive:

> This notebook does not repeat the formal proofs from the lecture notes.

Content-forward:

> This notebook develops the geometric and numerical intuition for conditional expectation.

Defensive:

> The theorem does not apply to arbitrary integrands.

Mathematically scoped:

> The theorem applies to predictable square-integrable integrands.

## Figure and simulation language

Defensive:

> The left panel does not claim that the four integrands have the same shape.

Encoding-first:

> Each marker records the input-output norm pair for one integrand.

Separate the two jobs. The figure sentence reports what is plotted. The mathematical claim is
stated separately and carries the strength of its own support. In the corpus, sentences that
reference a figure or a simulation take descriptive verbs; hedged verbs are rare and proof-level
verbs rarer still, because the claim is attributed to the result that proves it.

Overstated:

> The simulation proves that the left-point sums converge.

Separated, when a result governs the quantity:

> The realized errors fall by about a factor of four as the mesh halves.
> Theorem 4.3 gives convergence in probability; the figure supplies the numerical pattern for this experiment.

Hedged, when no result governs the observed regime:

> The simulated errors decrease as the partition is refined, consistent with convergence in probability.

Reach for the hedge when the measured quantity falls outside every available result.

When a limitation is real, name it:

> The intervals show Monte Carlo uncertainty, while movement across meshes reflects discretisation error.

## Mathematical negation protection

The following forms often carry essential content:

- `The converse is not true.`
- `A local martingale need not be a martingale.`
- `Brownian paths are nowhere differentiable.`
- `B_{t_{i+1}}` is not `\mathcal F_{t_i}`-measurable.

Preserve negation in definitions, theorems, counterexamples, logical distinctions, admissibility conditions, and model boundaries. Precision is the criterion.

## Paragraph reconstruction

After revising a defensive sentence, rebuild the paragraph around one main job:

1. open with the governing object, question, relation, or claim;
2. supply the assumption, calculation, evidence, or explanation it needs;
3. state the mathematical consequence;
4. finish when that job is complete.

Replace stock phrases with the actual mathematical subject and relation.

## Warning patterns

Treat these as review signals rather than automatic violations:

- `does not claim`;
- `not intended to`;
- `this is not a proof`;
- `it is important to note`, `it is worth noting`, `it should be emphasised`;
- `should not be interpreted as`;
- `to be clear`;
- repeated `not X but Y` constructions.

Each signal still receives the functional test above.

## Devices that are not warnings

These carry the argument in rigorous mathematical writing. Judge them by function, never by frequency.

**Pointers.** `Note that`, `observe that`, and `recall that` direct attention to a fact that the next
step uses. In the corpus they are the most frequent discourse device in rigorous probability prose,
and their density rises with rigor rather than falling. Delete a pointer when the fact it points at
goes unused. The padded forms carrying `important` or `worth noting` are the warning; the bare
pointer is not.

**Contrast.** `However`, `although`, `whereas`, and `in contrast` mark a genuine logical opposition:
a theorem against its converse, sufficient against necessary, a general case against a special one.
The clearest expositors in the corpus use them most heavily. Keep a contrast that marks an
opposition; delete one that decorates a transition.

**Modals.** `May`, `might`, and `could` report genuine uncertainty about a quantity, and they run
higher in computational and empirical writing where that uncertainty is real. Keep a modal that
reports uncertainty; replace one that hedges a claim the source already settles.

## Review-first workflow

In review mode, report:

- the passage;
- its current function;
- whether the qualification is mathematically necessary;
- the action: `Keep`, `Rewrite`, `Compress`, `Delete`, or `Flag`;
- a short reason.

In revision mode, implement the decisions and then run the mathematical-integrity comparison.

## Self-application

Apply this audit to the skill itself. Retain instructions that change behaviour or protect validity. Rewrite exception-heavy instructions as positive operating rules. Remove explanatory material that repeats an adjacent rule.

This audit adapts the functional classification and positive-scope approach of Kiterlin's MIT-licensed [anti-defensive-writing](https://github.com/Kiterlin/anti-defensive-writing) skill for mathematical prose.

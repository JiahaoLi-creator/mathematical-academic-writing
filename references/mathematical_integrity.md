# Mathematical Integrity

Use two distinct checks: source verification establishes whether the original claim is supported; revision comparison establishes whether editing preserved that claim.

## 0. Source verification

When substantive verification is requested:

1. list the material claims, definitions, identities, and numerical conclusions;
2. identify the assumption set and authoritative source for each;
3. reconstruct the decisive derivation, theorem dependency, citation, or numerical benchmark;
4. classify each item as verified, unsupported, ambiguous, or incorrect;
5. separate a source error from an editing error;
6. correct mathematical content only within the user's requested scope.

For a stylistic revision, flag a suspected source error separately and preserve the source claim in the edited text.

## 1. Objects and domains

Verify:

- probability spaces, filtrations, sigma-algebras, function spaces, and state spaces;
- domains, codomains, time intervals, index sets, and boundary conditions;
- deterministic versus random quantities;
- scalar, vector, matrix, process, path, and distributional objects.

Each symbol must refer to the same object before and after revision.

## 2. Quantifiers and logical direction

Protect:

- `for every`, `there exists`, `almost every`, and `with probability one`;
- implication and equivalence;
- necessary and sufficient conditions;
- local and global statements;
- finite-horizon and asymptotic statements;
- a theorem, its converse, and any counterexample separating them.

A shorter sentence must preserve the original logical strength.

## 3. Assumptions and admissibility

Keep assumptions beside the result or construction that uses them. Check:

- measurability and adaptedness;
- predictability and stopping-time conditions;
- integrability and square integrability;
- continuity, differentiability, regularity, and growth conditions;
- independence, stationarity, and distributional assumptions;
- market, data, algorithmic, and numerical assumptions.

State a condition positively when that improves clarity. Preserve a negative condition when it has mathematical content.

## 4. Equalities, bounds, and limits

Distinguish:

- equality from approximation;
- pathwise statements from expectation statements;
- exact values from estimates and confidence intervals;
- upper bounds from asymptotic rates;
- pointwise, uniform, almost-sure, in-probability, distributional, and `L^p` convergence.

Retain subscripts, superscripts, brackets, absolute values, norms, indicators, differentials, and integration limits.

## 5. Notation lock and the working register

Build the register before editing. It commits to the values the work must preserve, and the final
comparison in section 9 runs against it rather than against memory of the source.

Notation:

| Object | Authoritative notation | Allowed local abbreviation |
| --- | --- | --- |
| Example | `\Sigma_0` | none unless supplied |

- Use the primary source's notation.
- Define a new symbol only when the source lacks the required concept.
- Keep theorem numbering and citation labels exactly aligned with the source.
- Preserve technical terms instead of replacing them with stylistic synonyms.

Claims:

| Claim | Support | Ladder rung | Site | Citation |
| --- | --- | --- | --- | --- |
| Example | Lemma 4.2 | formal proof | section 2 | MATH3015, Chapter 4 |

- `Support` names the theorem, derivation, example, figure, simulation, or dataset that carries the claim.
- `Ladder rung` fixes the permitted verb strength in section 6.
- `Site` fixes the one location that states the claim; every later mention is a reference to it.
- A claim with an empty `Support` entry is unsupported. Flag it rather than assigning a verb.

Assumptions carry into the register beside the claim that uses them, with the admissibility,
integrability, measurability, and regularity conditions listed in section 3.

Record the register before the text changes. Changing an entry mid-task is a substantive decision:
state the entry, the new value, and the source that authorizes it.

## 6. Evidence ladder

Identify the support for each claim and select its verb from that rung:

| Support | Permitted verbs | Forbidden for this support |
| --- | --- | --- |
| Formal proof | proves, establishes, shows that, implies, holds, characterises, if and only if | — |
| Exact derivation | gives, yields, equals, follows, reduces to | proves, unless the derivation is the proof |
| Worked example | in this case, for this example, exhibits, attains | in general, always, proves |
| Counterexample | fails, need not, is not necessarily, provides a counterexample to | disproves the theorem; name the claim that fails |
| Figure | displays, shows, plots, reports, depicts, compares | proves, establishes, implies, confirms, demonstrates that |
| Simulation | decreases numerically, matches to within, is consistent with, estimates | proves, shows that, establishes, confirms, verifies |
| Observational data | indicates in this sample, is associated with, we find | causes, proves, establishes, demonstrates |

Figures and simulations support intuition and numerical agreement. Formal statements derive their
validity from the theorem, derivation, or cited source.

### Section-level density diagnostic

Evidence strength governs the section, not only the sentence. Proof verbs are `we prove`, `we show`,
`we establish`, `we deduce`, `we conclude`, `proves that`, `establishes that`, `shows that`,
`confirms`, `verifies`, `demonstrates`, `it follows`, `hence`, `therefore`, `thus`,
`consequently`, `implies`, and `if and only if`.

| Section evidence type | Observed proof verbs per 1000 words | Observed proof verbs to evidence verbs |
| --- | --- | --- |
| Theorem, proof, derivation | 6 to 8 | above 10:1 |
| Definition, construction, worked example | 3 to 6 | 5:1 to 15:1 |
| Computation, simulation, figure reading, empirical analysis | near 2 | below 3:1 |

The outer bands come from the corpus recorded in [corpus manifest](corpus_manifest.md); the middle
band interpolates between them. They are diagnostics, not quotas. Never add proof language to move
a section into a band. A computational or visual section written at theorem-proof density triggers
claim-level review: locate claims whose register entry lacks a proof or derivation and lower their
verbs to the supporting rung.

Read the density for the section that contains the claim. A notebook that mixes a formal statement
with a numerical experiment carries a different band in each.

## 7. Numerical and visual shields

Preserve values that carry meaning:

- parameter values and units;
- sample sizes, confidence levels, tolerances, and seeds;
- partition sizes and time meshes;
- axes, legends, color encodings, and reference lines;
- error definitions and benchmark formulas.

When compressing an interpretation, retain the values needed to connect the visible pattern to the mathematical conclusion.

## 8. Citation and source integrity

- Attach each citation to the claim it supports.
- Keep distinctions between a source theorem, the current derivation, and a numerical check.
- Use the user-designated primary source to define course boundaries.
- State missing evidence as a request or unresolved item.

## 9. Final comparison

Before returning a revision, answer:

1. Did any symbol change meaning?
2. Did any assumption, quantifier, or convergence mode disappear?
3. Did any implication become stronger?
4. Did a figure or simulation acquire proof-level language?
5. Did the revision add a theorem, citation, parameter, or numerical result?
6. Did compression remove information needed by the intended reader?
7. Does any output entry depart from the register recorded in section 5?
8. Does any section exceed the proof-verb band for its evidence type?
9. Is any claim stated in more than one site?

Resolve or explicitly flag every discrepancy before release.

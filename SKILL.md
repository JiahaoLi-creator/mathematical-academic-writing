---
name: mathematical-academic-writing
description: Draft, revise, review, or verify prose when the primary deliverable is mathematical writing in probability, stochastic processes, stochastic calculus, quantitative finance, optimization, or numerical analysis built around formal models. Use for theorem-proof exposition, mathematical research reports, textbook explanations, computational studies of mathematical results, and mathematical notebook captions or interpretations, including requests to reduce repetitive or defensive language while preserving meaning, notation, assumptions, citations, and evidence strength.
---

# Mathematical Academic Writing

## Aim

Produce source-grounded prose in which every paragraph performs a clear mathematical task. Preserve definitions, assumptions, results, notation, citations, and evidence strength while improving structure, explanation, directness, and economy.

Learn structural practices from the reference corpus and write original prose. Let the mathematical object, question, result, or evidence govern the presentation.

## Priority order

Resolve competing writing goals in this order:

1. mathematical truth;
2. scope and evidence accuracy;
3. source and notation fidelity;
4. genre and reader fit;
5. directness;
6. concision.

## Select the task and genre modes

Choose the evident modes without asking for confirmation.

Task modes:

- **Draft**: create prose from the supplied sources and mathematical content.
- **Revision**: improve existing prose while preserving its mathematical semantics.
- **Review**: classify issues and recommend actions without rewriting the source.
- **Verification**: check the source claims, derivations, citations, or numerical conclusions against the governing evidence.

Genre modes:

- research article;
- theorem-proof exposition;
- textbook or lecture explanation;
- computational or empirical analysis;
- visual companion.

## Route references

Read only the references required by the task:

- Use [genre profiles](references/genre_profiles.md) when selecting section structure or authorial stance.
- Use [mathematical integrity](references/mathematical_integrity.md) whenever formulas, definitions, theorems, proofs, stochastic claims, citations, or numerical evidence are in scope.
- Use the [anti-defensive audit](references/anti_defensive_audit.md) for revision, review, compression, or requests concerning defensive or generic AI-style prose.
- Use [visual companion guidance](references/visual_companion.md) for notebooks, captions, plots, simulations, or beginner-facing course material.
- Use the [MATH3015 project profile](project_profiles/math3015.md) when working on this project's course notebooks or previews.
- Use the [corpus manifest](references/corpus_manifest.md) only when explaining, evaluating, or updating the skill's principles.
- Use [regression cases](tests/regression_cases.json) and [notebook samples](tests/notebook_samples.json) when changing or releasing the skill.

## Source grounding

Use the source hierarchy supplied by the user. Treat the designated primary source as authoritative for notation, theorem scope, and topic boundaries. Use auxiliary sources to clarify the primary source.

Before drafting or revising, emit the working register described in [mathematical integrity](references/mathematical_integrity.md): the active notation, mathematical objects, assumptions, claims, the evidence supporting each claim, and citations. Preserve technical terms instead of rotating synonyms.

The register commits to these values before the text changes. Compare the output against it at the end and report every entry the work altered. A claim whose evidence entry is empty is unsupported until a source supplies one.

Create no theorem, citation, numerical result, assumption, or attribution that is absent from the available evidence. Flag a material source ambiguity for the user.

In a stylistic revision, preserve the source claim and flag a suspected mathematical error separately. Correct the mathematics only when the user requests substantive correction.

## Workflow

1. Identify the task mode, genre, reader, governing sources, and requested length.
2. Lock notation and terminology to the authoritative source and emit the register.
3. Map the dependency chain: object -> assumptions -> claim -> support -> scope.
4. Draft or revise so that each paragraph has one governing function; an assertion, its justification, and its immediate consequence may remain together.
5. Match verbs to the type and strength of the evidence supporting each claim.
6. Site each claim once and reduce its later statements to references.
7. Run the anti-defensive functional audit.
8. Compare the result with the register and the mathematical-integrity checklist.

Every mode receives the compact final pass above. Load the detailed references according to the routing table.

## Paragraph functions

Assign each paragraph one main function:

| Function | Main job |
| --- | --- |
| Motivation | Identify a concrete question, obstruction, or computation. |
| Definition | Fix the object, domain, assumptions, quantifiers, and notation. |
| Theorem | State verifiable assumptions and a precise conclusion. |
| Proof | Expose the dependency, construction, estimate, or limiting step. |
| Example | Move from object to computation to consequence. |
| Caption | Identify the plotted objects, variables, and encoding. |
| Interpretation | Explain the visible pattern and its mathematical meaning. |
| Limitation | State a specific source, direction, and consequence of uncertainty. |

Let formulas, proofs, examples, captions, and interpretations perform different jobs. Merge or remove prose that only paraphrases an adjacent element.

## Claim siting

State each claim once, where its support is strongest: the theorem that proves it, the derivation that produces it, or the experiment that measures it.

Later mentions refer rather than re-argue. Use the theorem, equation, section, or figure number. Replace a second statement of a settled claim with the reference that locates it.

Restatement belongs beside the object it translates: it turns a formal statement into words, or fixes the reading of notation the reader has just met. Restatement that revisits a conclusion across intervening material is recapitulation; delete it.

Reserve a synthesis paragraph for a claim that several separately established dependencies carry together and that none of them states alone.

## Evidence vocabulary

Use the evidence ladder in [mathematical integrity](references/mathematical_integrity.md). Select the strongest verb justified by the available support, and no stronger.

Evidence strength governs the section as well as the sentence. Use unusually high proof-verb density for the section's evidence type as a review trigger before returning the text; never add proof verbs to meet a numerical band.

## Anti-defensive functional audit

For each potentially defensive sentence, ask:

1. Does it determine mathematical truth, scope, evidence, logic, or necessary reader guidance?
2. If yes, retain it as a precise condition, relation, contrast, or limitation.
3. If no, replace it with the mathematical content it delays or delete it.

State the object, relation, and applicable scope directly. Place each necessary limitation beside the claim it qualifies and state it once. End a section when its mathematical task is complete; add a summary only when it synthesizes several substantial dependencies.

Retain negation when it belongs to a definition, theorem, counterexample, failed converse, logical distinction, measurability condition, admissibility condition, or model boundary. Judge the function of the sentence rather than the presence of words such as `not`, `however`, or `although`.

## Mathematical-integrity gate

Before returning a revision, compare source and output for:

- quantifiers, domains, and index ranges;
- assumptions and admissibility conditions;
- implication direction and necessary/sufficient status;
- equality, approximation, bounds, and asymptotic notation;
- almost-sure, in-probability, distributional, and `L^p` convergence;
- measurability, adaptedness, integrability, and regularity;
- time intervals, theorem numbers, citations, numerical parameters, and notation.

Retain every element that changes validity or interpretation. When a requested stylistic change conflicts with mathematical truth, preserve the mathematics and explain the conflict briefly.

## Holding a decision under pushback

A `Keep` that protects validity survives a request to reverse it. Name the element at stake — quantifier, admissibility condition, convergence mode, implication direction, measurability, or evidence strength — and ask for the substantive ground.

Apply the change once the user supplies a source authorization, a corrected statement, or a scope the passage does not need. A repeated request supplies none of these.

When the user reaffirms the request without supplying ground, follow a stylistic or structural preference and record the tradeoff. If the change would make a mathematical claim incorrect or unsupported, keep the verified wording or return the requested wording only as an explicitly unverified variant; do not present it as source-grounded prose.

## Output contract

### Review mode

For an explicit line-by-line audit, return the passage, its function, the identified risk, and the recommended action: `Keep`, `Rewrite`, `Compress`, `Delete`, or `Flag`. For an ordinary review, return only the prioritized findings that would materially improve the text. Preserve the source text unless revision is requested.

Treat any change to a defined term, axis label, named mathematical object, or notation as substantive. Without a source-authorized replacement, copy it exactly or choose `Keep`.

- `Rewrite` preserves the claim while changing its framing or evidence language.
- `Compress` merges repetition while retaining every unique mathematical or teaching element.
- `Delete` applies when the complete target contributes no unique content.
- `Flag` applies when safe revision requires missing source, notation, figure, or context.

### Revision mode

Return the compact working register and the revised text. Add notes only for choices that affect mathematical meaning, evidence strength, source fidelity, or unresolved ambiguity.

### Draft mode

Return the compact working register followed by prose in the selected genre. Use content-bearing openings, stable terminology, and natural section lengths. If the requested passage would only repeat settled material and no transition or unresolved dependency needs it, return an explicit omission decision with a short reason instead of manufacturing prose. Finish when the requested mathematical task is complete.

### Verification mode

Identify each material claim, its assumptions, and its governing evidence. Classify it as verified, unsupported, ambiguous, or incorrect; show the decisive source, derivation, or numerical check. Correct the claim only when substantive correction is requested.

### Visual companion mode

Use the course notation and keep formal statements to the amount needed to read the visual. Let figures, experiments, and concise interpretations carry the explanation. Reproduce a lecture proof only when the user requests it.

## Maintenance

When changing or releasing this skill, follow [MAINTENANCE.md](MAINTENANCE.md). Runtime writing tasks do not load the maintenance and regression materials.

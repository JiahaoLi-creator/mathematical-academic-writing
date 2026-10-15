# Corpus Manifest

## Scope

The principles are grounded in local papers and textbooks covering rigorous probability,
stochastic processes, stochastic calculus, mathematical finance, statistical analysis, optimization,
numerical methods, and quantitative computational work.

The current inventory records 44 PDFs in `Reference_Materials/probability/` and 92 PDF entries in
`Reference_Materials/Textbook/`, including papers, books, a dissertation, a presentation, split
chapters, and full-volume representations. A preliminary 17-source, approximately 120,000-word
extraction supplied the first directional check; the recovered 27-source measurement below
supersedes it for every quantitative rule in this skill.

The [statistical source map](statistical_source_map.md) adds task-specific methodological sources
and the v0.4.3 close-reading supplement. Its ten books overlap the thirteen measured textbooks
at *Convex Optimization*, giving twenty-two distinct reference books across these two sets.
Representative titles listed below describe the wider local library; exact measured membership
is recorded in `corpus/selection.v1.json`.

## v0.4.3 close-reading supplement

VanderPlas and Vershynin were inspected on 2026-10-03; Shumway-Stoffer was added on 2026-10-05:

- Jake VanderPlas, *Python Data Science Handbook: Essential Tools for Working with Data*, first
  edition, December 2016, O'Reilly Media; copyright 2017.
- Roman Vershynin, *High-Dimensional Probability: An Introduction with Applications in Data
  Science*, second-edition pre-publication version dated July 22, 2026.
- Robert H. Shumway and David S. Stoffer, *Time Series Analysis and Its Applications: With R
  Examples*, fourth edition, Springer, 2017.

Their bibliography pages and selected methodological passages are recorded in
`corpus/supplementary_sources.v0.4.3.json`. The record binds PDF identity, extraction ranges,
raw and normalized text hashes, counts, and the inspected extraction runtime. The
[source map](statistical_source_map.md) contains the page anchors and original writing guidance.
`scripts/source_supplement.py` rebuilds and verifies this record from the local PDFs.

The supplement contains extracted-text hashes and locators rather than redistributed source text.
Its three records cover 81 sampled pages, including 35 from Shumway-Stoffer; that book already
belongs to the 136-PDF inventory and is not a duplicate inventory addition.
It extends qualitative coverage to 30 sampled writing sources while the numerical measurements
below continue to describe exactly the original 27. The supplement is included in the candidate's
release-governance hash and later package signature. The updated 136-PDF inventory requires a new
external corpus approval; the historical signature remains evidence for the previous inventory only.

## Representative probability and mathematical-finance papers

- Heston, *A Closed-Form Solution for Options with Stochastic Volatility*.
- Cox, Ingersoll, and Ross, *A Theory of the Term Structure of Interest Rates*.
- Duffie, Filipovic, and Schachermayer, *Affine Processes and Applications in Finance*.
- Keller-Ressel, *Moment Explosions and Long-Term Behavior of Affine Stochastic Volatility Models*.
- Fukasawa, *Volatility Has to Be Rough*.
- Bremaud and Yor, *Changes of Filtrations and of Probability Measures*.
- Follmer and Protter, *Local Martingales and Filtration Shrinkage*.
- Protter and Shimbo, *No Arbitrage and General Semimartingales*.
- Delbaen and Schachermayer, *The Fundamental Theorem of Asset Pricing for Unbounded Stochastic Processes*.
- Wong and Heyde, *On the Martingale Property of Stochastic Exponentials*.

## Representative rigorous textbooks

- Tao, *Analysis I* and *Analysis II*.
- Jacod and Protter, *Probability Essentials*.
- Rosenthal, *A First Look at Rigorous Probability Theory*.
- Karatzas and Shreve, *Brownian Motion and Stochastic Calculus*.
- Le Gall, *Brownian Motion, Martingales, and Stochastic Calculus*.
- Oksendal, *Stochastic Differential Equations*.
- Protter, *Stochastic Integration and Differential Equations*.

## Representative applied textbooks

- Boyd and Vandenberghe, *Convex Optimization*.
- Bjork, *Arbitrage Theory in Continuous Time*.
- Taleb, *Dynamic Hedging*.
- Glasserman, *Monte Carlo Methods in Financial Engineering*.
- Steele, *Stochastic Calculus and Financial Applications*.
- Oksendal and Sulem, *Applied Stochastic Control of Jump Diffusions*.
- Hautsch, *Econometrics of Financial High-Frequency Data*.

## Quantitative measurements

A 27-source, 238,497-word normalized prose extraction supplied the rates below, in occurrences per
1000 words. The analysis profiles contain 7 theory papers, 4 applied papers, 3
empirical/computational sources, 7 rigorous textbooks, and 6 applied textbooks. An analysis profile
records the source's role in this measurement; the registry records document kind separately.

### Reproduction status

The original 2026-07-26 run was recovered with its extraction script, analysis script, manifest,
stats, and 27 text artifacts. A fresh in-memory extraction of the same 617 PDF pages matched all 27
raw and normalized texts, their per-source hashes, and their word counts. The verification runtime
is Python 3.13.5, PyMuPDF 1.27.2.3, and MuPDF 1.27.2. The historical script did not record its own
runtime version. The raw extraction contains 239,321 words; the historical `clean()` transformation
produces the 238,497 words used in this table.

Machine-readable bindings:

- `corpus/inventory.v1.jsonl`: 136 current PDF records and byte hashes;
- `corpus/duplicate_groups.v1.json`: representation and overlap groups;
- `corpus/evidence_registry.v1.json`: bibliography locators, document adjudication, page segments,
  cited external authority records where needed, PDF hashes, current-PDF reproduction records, raw
  and normalized text hashes, per-source counts, and metric rows;
- `corpus/selection.v1.json`: the exact 27 logical sources and candidate payload hash;
- `corpus/selection_review.v1.json`: the unsigned review request bound to that payload;
- `corpus/selection_review_table.v1.md`: complete bibliography and source-adjudication review pack;
- `corpus/legacy_run_2026-07-26/`: the recovered executable evidence and text artifacts.

The final corpus state is derived from a detached OpenSSH Ed25519 signature in namespace
`maw-corpus-v1`. The signed statement binds the selection payload, inventory, duplicate groups,
registry, normalized-text bundle, and review table. Its `allowed_signers` trust root and SHA-256 pin
are supplied from outside the project at release time.

The third profile preserves the recovered sample while correcting its label: Fukasawa is a
theorem-led research paper, Gatheral is an empirical/computational presentation, and Pan is an
empirical research paper. The profile is therefore named `empirical_computational_source`.

The historical measurement used `legacy_run_2026-07-26/analyze.py`. The regression engine in
`scripts/text_metrics.py` has a broader proof-verb inventory, including `confirms`, `verifies`, and
`demonstrates`. Corpus thresholds retain the historical metric definition until a separate
recalibration is reviewed.

| Feature | Corpus rate | Distribution |
| --- | --- | --- |
| Defensive disclaimers | 0.06 | zero in 21 of 27 sources; `it is worth` absent from the sample |
| Summary-closing markers | 0.03 | zero in 24 of 27 sources |
| Back-reference to an earlier argument | 0.04 | near zero in every genre |
| Pointers: `note that`, `observe that`, `recall that` | 0.93 | rises with rigor; highest in the rigorous textbooks and theory papers |
| Contrast markers | 2.77 | 1.85 to 3.70 across genres; highest in the applied textbooks |
| Modals: `may`, `might`, `could` | 1.53 | 1.25 in theory papers, 2.02 in applied papers |
| Named limitations | 0.27 | highest in theory papers at 0.56 |
| First person plural | 13.82 | standard across every genre |
| `Remark` as a labelled device | 0.65 in theory papers | 0.58 in rigorous textbooks, near zero in applied papers |

Proof-verb density by genre, with the ratio of proof verbs to evidence verbs:

| Genre | Proof verbs | Evidence verbs | Ratio |
| --- | --- | --- | --- |
| Theory papers | 7.89 | 0.40 | 19.7:1 |
| Rigorous textbooks | 6.32 | 0.42 | 15.0:1 |
| Applied textbooks | 2.86 | 1.05 | 2.7:1 |
| Applied papers | 2.16 | 0.61 | 3.5:1 |
| Empirical/computational sources | 2.04 | 0.99 | 2.1:1 |

Sentences that reference a figure, table, or simulation take descriptive verbs in the large
majority of cases. Hedged verbs appear in under one percent of them, and proof-level verbs in
under seven percent; the mathematical claim is carried by the result rather than by the figure.

Consecutive prose sentences sharing at least 60 percent of their content words occur at 2.33
percent of sentence pairs, with a per-source ceiling of 5.66 percent.

Prose sentences run to a median of 21 words, with 19.8 percent under 12 words. The genre signature
is wide variance rather than a uniform length.

## Corpus-derived principles

Across genres, the stable pattern is logical responsibility:

- motivation comes from a concrete problem or obstruction;
- definitions, results, proofs, examples, and figures have distinct jobs;
- assumptions sit near the result that uses them;
- notation remains stable;
- examples perform reasoning;
- evidence strength controls claim strength;
- limitations are specific and local;
- natural authorial voices vary across genres.

The skill borrows structural practices rather than distinctive wording.

## Traceable close-reading anchors

Page numbers below refer to PDF file pages in the local corpus.

| Source | PDF pages | Writing feature used |
| --- | --- | --- |
| Heston, *A Closed-Form Solution for Options with Stochastic Volatility* | 1-2, 13-14 | method and contribution stated directly; conclusion separates mechanisms |
| Duffie, Filipovic, and Schachermayer, *Affine Processes and Applications in Finance* | 4-5, 13, 17 | precise definitions, announced proof strategy, stepwise proof |
| Fukasawa, *Volatility Has to Be Rough* | 1-2, 6-7 | compact result ordering, local remarks, proof steps |
| Follmer and Protter, *Local Martingales and Filtration Shrinkage* | 1-2, 4-5 | benchmark result, specific caveat, dependency-aware proof |
| Delbaen and Schachermayer, *The Fundamental Theorem of Asset Pricing for Unbounded Stochastic Processes* | 1-4 | main theorem first, removed assumption, counterexample and interpretation |
| Wong and Heyde, *On the Martingale Property of Stochastic Exponentials* | 1-3, 5-6 | concrete research questions, short roadmap, stopping and limit argument |
| Tao, *Analysis I* | 36, 39-40 | intuition followed by definition and formal construction |
| Jacod and Protter, *Probability Essentials* | 14-17, 22, 24 | compact definition-theorem-proof sequence |
| Karatzas and Shreve, *Brownian Motion and Stochastic Calculus* | 15-16, 22, 26, 36 | local intuition followed by strict notation and dependencies |
| Le Gall, *Brownian Motion, Martingales, and Stochastic Calculus* | 6-7, 25, 30, 37-40 | concise scope control and layered long proofs |
| Oksendal, *Stochastic Differential Equations* | 26, 32-33, 67 | examples expose adaptedness before the Itô-integral definition |
| Protter, *Stochastic Integration and Differential Equations* | 7, 13, 17, 50-51 | obstruction-first motivation and precise omitted-proof sources |
| Boyd and Vandenberghe, *Convex Optimization* | 15-19, 167-170, 471-478 | unified model form, geometry, applications, algorithm conditions |
| Bjork, *Arbitrage Theory in Continuous Time* | 21-34 | market problem, formal model, proof, and economic meaning |
| Glasserman, *Monte Carlo Methods in Financial Engineering* | 11-13, 23-26 | estimator, bias source, decay, and computational cost |
| Steele, *Stochastic Calculus and Financial Applications* | 6-7, 21-27 | concrete-first teaching and reusable examples |
| *Rough Volatility* | 23-31, 41-47 | observable, proxy, visual evidence, model check, and local limitation |
| Hautsch, *Econometrics of Financial High-Frequency Data* | 37-49, 70 | data construction, processing limits, quantitative figure reading |

## Anti-defensive source

Kiterlin's [anti-defensive-writing](https://github.com/Kiterlin/anti-defensive-writing) skill contributed the functional-classification, positive-scope, precision-preservation, and review-first ideas. The present skill independently adapts those ideas to theorem assumptions, mathematical negation, notation lock, visual evidence, and stochastic claims. The referenced repository is distributed under the MIT License.

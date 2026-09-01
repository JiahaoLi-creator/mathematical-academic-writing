# General Statistical Analysis Workflows

Load this reference by default when the task is to plan, conduct, review, interpret, or report a
statistical analysis. It governs the reasoning and reporting contract; pair it with an execution or
notebook workflow when code must be run. Use [statistical writing and inference integrity](statistical_writing.md)
for the precise interpretation of tests, intervals, models, predictions, and causal claims.

## 1. Scope and evidence anchors

This is a cross-domain core, not a substitute for subject-matter knowledge or a design-specific
reporting standard. Select the primary theoretical and methodological sources through the
[statistical source map](statistical_source_map.md). The following professional and reporting
anchors have separate, narrower roles:

- the [ASA Ethical Guidelines for Statistical Practice](https://www.amstat.org/your-career/ethical-guidelines-for-statistical-practice)
  support provenance, fitness-for-use, transparency, planned-versus-unplanned analysis, limitations,
  and honest communication across statistical practice;
- the [ASA Statement on Statistical Significance and P-Values](https://www.amstat.org/asa/files/pdfs/p-valuestatement.pdf)
  supports the p-value and threshold shields;
- the [NIST/SEMATECH e-Handbook](https://www.itl.nist.gov/div898/handbook/eda/eda.htm)
  supports the EDA and model-diagnostic workflow;
- [ICH E9(R1)](https://www.fda.gov/regulatory-information/search-fda-guidance-documents/e9r1-statistical-principles-clinical-trials-addendum-estimands-and-sensitivity-analysis-clinical)
  supplies a useful estimand-estimator-sensitivity architecture, but its regulatory requirements are
  specific to clinical trials;
- the [SAMPL guidance](https://www.equator-network.org/reporting-guidelines/sampl/) is a useful check
  for common statistical reporting, but its biomedical scope does not make it universal.

When a domain has its own governing protocol or reporting guideline, use that source for the
domain-specific requirements and retain this file for the cross-cutting statistical checks.

## 2. Build the analysis contract

Settle the entries that determine what the analysis means before choosing a method:

| Entry | Required decision |
| --- | --- |
| Purpose | Descriptive, exploratory, inferential, predictive, causal, or decision-oriented? |
| Unit and population | What is one independent or clustered unit, and what population or process is targeted? |
| Data provenance | How were data generated, sampled, assigned, linked, measured, censored, filtered, or revised? |
| Structure | Independent, paired, repeated, clustered, longitudinal, survey-weighted, time-indexed, spatial, or censored? |
| Variables | Outcome, exposure, predictors, covariates, groups, time origin, event, and measurement scales? |
| Estimand or target | Which mean, contrast, association, risk, quantile, prediction, causal effect, or decision quantity, on which scale? |
| Method | Which estimator, model, algorithm, test, interval, or resampling procedure targets it? |
| Uncertainty | Which variability is quantified: sampling, design, posterior, predictive, resampling, or Monte Carlo? |
| Assumptions | Which conditions identify the target or calibrate the procedure? |
| Diagnostics and sensitivity | Which plausible departures, alternatives, or failure modes will be checked? |
| Reporting scope | Which population, time period, setting, and use can the evidence support? |

If a key entry is unavailable, give a conditional plan or `Flag`; do not fill it with a convenient
default. A method name cannot repair an undefined outcome, unit, target, or sampling mechanism.

## 3. Universal workflow

1. **Fix the question and intended use.** Separate exploratory discovery from prespecified or
   confirmatory analysis and state whether the goal is description, inference, prediction, causation,
   or a decision.
2. **Audit provenance and fitness for use.** Check units, identifiers, coding, ranges, time order,
   duplicates, linkage, measurement changes, exclusions, and the path from raw to analysis data.
3. **Identify the dependence structure.** The effective unit is determined by sampling, assignment,
   repeated measurement, clustering, time, or space—not by the number of rows.
4. **Define the target and scale.** State the estimand or prediction target before choosing a model;
   specify conditioning sets, horizons, contrasts, transformations, and populations.
5. **Choose a procedure that matches the contract.** Method choice follows the question, design,
   variable scale, dependence, target, assumptions, sample support, and intended interpretation.
6. **Preserve preprocessing inside the analysis protocol.** Record recoding, exclusions,
   transformations, feature construction, imputation, weighting, tuning, and their timing relative to
   resampling or train/test splits.
7. **Quantify uncertainty on the correct unit and scale.** Match standard errors, intervals,
   posteriors, resampling units, or simulation error to the design and target.
8. **Run model-specific diagnostics.** Examine the departures that threaten the stated claim;
   diagnostics are evidence about particular assumptions, not a certificate that the model is true.
9. **Run targeted sensitivity analyses.** Vary plausible missing-data, modeling, tuning, weighting,
   dependence, or identification choices while keeping the estimand clear.
10. **Interpret at the evidence level.** Report magnitude, direction, units, uncertainty, practical
    context, and scope. Preserve null, mixed, or unstable results.
11. **Make the path reproducible.** Record analysis population, software and package versions,
    randomness controls, data transformations, and the source of each table and figure when material.

Do not select a test by trying alternatives until one is significant. If the intended method changes
after looking at the data, disclose the change and calibrate the claim as exploratory or post-selection.

## 4. Route by analysis family

| Family | Minimum contract and common checks |
| --- | --- |
| Descriptive and EDA | Population represented, unit, missingness, distribution, dependence, anomalies, and graphical encodings. Label discoveries as exploratory until independently checked. |
| Group comparisons, ANOVA, ANCOVA | Independent versus paired design, contrast and scale, multiplicity, effect size and interval, variance structure, covariate role, and interaction. A threshold alone is not the result. |
| Linear regression and GLMs | Outcome family and link, coding, coefficient scale, nonlinear terms and interactions, dependence, residual or dispersion checks, leverage and influence, and prediction range. |
| Repeated, clustered, or hierarchical data | Observation level versus independent unit, within-cluster correlation, random and fixed effects, covariance structure, cluster count, small-sample degrees of freedom, and cluster-aware uncertainty. |
| Survey and weighted analysis | Target population, sampling frame, weights, strata, clusters or PSUs, calibration, nonresponse, finite-population features, and design-consistent variance. Separate an unweighted description of observed respondents from a design-based population estimate. |
| Time series and forecasting | Time order, trend and seasonality, serial dependence, forecast origin and horizon, rolling or blocked validation, feature construction inside each training window, revisions, and leakage from future information. |
| Spatial analysis | Spatial support, neighborhood or covariance structure, scale, edge effects, sampling pattern, and spatially honest validation. |
| Survival and event-time analysis | Time origin, event definition, censoring and competing risks, risk sets, follow-up, model scale, and time-varying effects. A hazard ratio is not generally a risk ratio. |
| Causal analysis | Causal estimand, assignment or design, identification assumptions, positivity and overlap, estimator, interference or censoring where relevant, and sensitivity to unmeasured bias. |
| Prediction and statistical learning | Outcome and horizon, split unit, train/tune/test separation, preprocessing within resampling, metric, imbalance, calibration, uncertainty, subgroup performance, and deployment shift. |
| Bayesian analysis | Likelihood, prior, posterior target, computation, convergence diagnostics, posterior predictive checks, prior/model sensitivity, and decision rule if used. |
| Robust, nonparametric, and resampling methods | Target under departure, resampling or permutation unit, exchangeability, robustness notion, tuning, finite-sample limitations, and the contrast with the reference procedure. |

Use conditional branches when several families could fit. For example, the same numeric outcome may
require an ordinary comparison, a paired analysis, a mixed model, a survey estimator, or a time-series
model depending on how observations were generated.

## 5. High-risk interpretation shields

- **Pseudoreplication:** repeated rows from the same person, cluster, site, device, or time series do
  not create that many independent units. Align standard errors, degrees of freedom, resampling, and
  splits with the dependence structure.
- **Coefficient scale:** interpret a coefficient on the model's stated scale and conditioning set.
  An odds ratio is not generally a risk ratio or a probability difference; a hazard ratio is not a
  ratio of cumulative risks. When the requested interpretation is on a probability or cumulative-risk
  scale, name the marginal prediction, standardization, survival, or cumulative-incidence calculation
  needed to estimate it rather than stopping at the scale mismatch. For a single proportional-hazards
  coefficient, connect a constant-over-time hazard-ratio interpretation to the proportional-hazards
  assumption; this is separate from estimating a probability-scale contrast.
- **Missing data:** report missingness by variable and analysis stage, the analysis population, the
  assumed mechanism, and the handling method. Complete-case or imputed results do not automatically
  represent excluded units; sensitivity is needed when conclusions depend on unverifiable assumptions.
  Select handling and sensitivity checks for the estimand, design, observed pattern, and assumed
  mechanism. Unless that support is supplied, present weighting, imputation, and sensitivity as
  conditional alternatives rather than a checklist that must be applied jointly.
- **Selection and multiplicity:** distinguish prespecified from data-selected outcomes, subgroups,
  cut points, transformations, and models. Account for the selection in uncertainty or qualify the
  conclusion as exploratory.
- **Leakage:** keep future, validation, and test information out of feature construction, imputation,
  scaling, selection, tuning, and stopping decisions. Split at the independent deployment unit and in
  the direction of intended prediction. For forecasting, define each training window first and then
  reconstruct lagged, rolling, transformed, and selected features from information available at that
  forecast origin; a time-ordered split alone is insufficient if full-series features were precomputed.
- **Generalization:** a representative sample, randomized assignment, valid identification argument,
  or external validation supports different kinds of scope. State the one actually available.
- **Diagnostics:** passing one diagnostic does not validate untested assumptions, identification, or
  transport to a new population.

## 6. Output patterns

### Analysis plan

Return a compact sequence:

```text
question and use
-> unit, population, and data structure
-> estimand or prediction target
-> primary procedure and uncertainty
-> preprocessing and missingness
-> diagnostics
-> sensitivity and multiplicity
-> reporting and generalization boundary
```

State unknowns and conditional branches explicitly. Do not invent sample sizes, variables, assignment,
missingness, assumptions, or results.

### Methods

Name the analysis population, target, design-aware method, variable coding and scale, uncertainty
procedure, missing-data handling, multiplicity or tuning, diagnostics, sensitivity analyses, and
software details that affect reproducibility.

### Results

Lead with the target and estimate, then units or scale, uncertainty, relevant sample size, calibrated
interpretation, diagnostics or sensitivity that qualify it, and scope. Report exact numerical evidence
when available; retain effect size and uncertainty even when a p-value is reported.

### Review or Verification

Prioritize failures that change the target, independence unit, uncertainty, interpretation, or scope.
Separate data-quality, design, identification, modeling, computational, and reporting defects. A
formatting preference is not a substitute for a statistical correction. For a rejected scale or
population interpretation, state the nearest supported claim and the additional calculation, design
argument, or evidence needed to answer the original question.

## 7. Flag conditions

Flag rather than improvise when any of these is decisive and unavailable:

- the observational or independent unit, target population, outcome, time origin, or estimand;
- the sampling, assignment, clustering, censoring, weighting, or train/test mechanism;
- the data or output needed to reproduce a numerical claim;
- a causal identification argument, a valid uncertainty procedure, or an independent evaluation;
- a missing-data, selection, or preprocessing step that can change the result;
- a domain protocol or decision threshold that the user must supply.

When the missing item changes only the method branch, provide a conditional plan. When it prevents a
defensible target or interpretation, stop at `Flag` and name the evidence needed.

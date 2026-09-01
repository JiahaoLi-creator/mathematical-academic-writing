# Statistical Writing and Inference Integrity

Load this reference when a claim depends on a population, sample, study design, statistical model,
estimand, estimator, predictive procedure, uncertainty statement, or empirical result. Apply it
together with [mathematical integrity](mathematical_integrity.md) when theoretical statistics or
mathematical derivations are also in scope.

For analysis planning, method selection, data-structure routing, preprocessing, diagnostics, and
reproducibility, also load [general statistical analysis workflows](statistical_analysis_workflows.md).

## 1. Extend the working register

Record the entries that determine the meaning of the analysis:

| Entry | Question to settle |
| --- | --- |
| Task | Is the goal descriptive, inferential, predictive, causal, or decision-oriented? |
| Population and units | What population is targeted, and what is one observational or experimental unit? |
| Sample and mechanism | How were units sampled, assigned, selected, censored, or excluded? |
| Variables | Which outcome, exposure, predictors, covariates, groups, and time points are observed? |
| Model | What probability model or working approximation is imposed? |
| Estimand | What population parameter, functional, contrast, risk, or causal quantity is targeted? |
| Estimator or procedure | What statistic, algorithm, tuning rule, or decision rule targets it? |
| Estimate or prediction | What realized value is reported from these data? |
| Uncertainty | Which standard error, interval, test, posterior, resampling, or simulation statement is used? |
| Assumptions | Which conditions identify the target or justify the procedure's stated properties? |
| Support and scope | What design, theorem, computation, or data supports the claim, and where may it generalize? |

Keep these distinctions explicit:

- A **parameter** or **estimand** is the target; an **estimator** is a random rule; an **estimate** is
  its realized value.
- A statistical model is an assumed family or working approximation. It is not automatically the
  data-generating process.
- **Identifiability** concerns whether the observable distribution determines a target within the
  stated model. **Estimability** concerns what a procedure can recover with the available data and
  asymptotic or finite-sample regime.
- A sample property is not a population property without a justified generalization step.

## 2. Choose the dependency chain

Use the chain that matches the statistical task.

```text
statistical theory:
model or functional -> assumptions -> estimator or procedure -> property -> proof or approximation -> scope

empirical inference:
question -> target population and design -> estimand -> estimator -> uncertainty -> diagnostic -> interpretation

statistical learning:
prediction target -> features and outcome -> train/tune/test protocol -> metric -> variability -> deployment scope

causal inference:
causal estimand -> design and identification assumptions -> estimator -> sensitivity -> causal claim and boundary
```

Do not replace a missing link with generic prose. Flag a causal estimand without identification, a
test without its null and reference distribution, or a performance claim without an independent
evaluation protocol.

## 3. Frequentist inference shields

### Tests and p-values

- State the null hypothesis, test statistic, reference distribution or resampling scheme, and the
  relevant tail convention when they affect interpretation.
- A p-value is a probability, computed under the null model and stated analysis protocol, of a test
  statistic at least as incompatible with that null as the observed statistic. It is not
  `P(H_0 | data)` and does not give the probability that a hypothesis is true.
- Failure to reject does not establish equality, no effect, or practical equivalence. An equivalence
  or non-inferiority claim requires its own margin and procedure.
- Statistical significance does not by itself establish practical importance, scientific relevance,
  or a large effect.
- When multiple testing, optional stopping, subgroup search, or model selection affects the reference
  distribution, name the adjustment or classify the unadjusted claim accordingly.

### Confidence intervals

- A frequentist confidence level describes the long-run coverage of a procedure under its assumptions.
  After observing an ordinary fixed-parameter interval, do not assign that confidence level as a
  posterior probability that the fixed parameter lies in this realized interval.
- State the target, confidence level, construction, and assumptions needed for coverage.
- Distinguish confidence intervals for parameters, prediction intervals for future observations, and
  tolerance intervals for population coverage.
- An interval compatible with zero is not proof of no effect; its width may instead show limited
  precision.
- When an interval bears on equality, equivalence, non-inferiority, or practical importance,
  interpret its range as effect values compatible with the data and analysis assumptions, or state
  that its width leaves the question unresolved. Repeating the endpoints alone is incomplete.
- Translate the interval into the directions, magnitudes, or precision relevant to the claim. A
  complete correction says both what the interval leaves compatible and why that range does or does
  not answer the scientific question; listing endpoints beside a disclaimer is not an interpretation.

Report effect estimates and uncertainty together when both are available. Do not let a thresholded
p-value replace the magnitude, direction, units, or precision of the result.

## 4. Finite-sample, asymptotic, and computational evidence

- Separate exact finite-sample results from asymptotic approximations and simulation observations.
- Consistency, asymptotic normality, efficiency, and limiting coverage require their stated regime and
  regularity conditions. They do not imply exact behavior at a particular finite sample size.
- When an interval or test is justified only by an asymptotic theorem, identify that reported
  interval or test as an asymptotic approximation under the theorem's conditions. Naming asymptotic
  normality elsewhere does not by itself calibrate the finite-sample statement.
- Correct a finite-sample overclaim in both directions: state positively that the reported procedure
  is an asymptotic approximation under the named conditions, and state separately that exact
  finite-sample calibration at the observed sample size has not been established.
- State whether a variance is model-based, sandwich/robust, bootstrap, posterior, predictive, or
  Monte Carlo. These quantify different sources of uncertainty.
- A bootstrap approximates a sampling distribution under its resampling assumptions; it does not
  repair a misdefined target, biased design, dependence violation, or data leakage by itself.
- Monte Carlo error concerns the numerical experiment. Sampling uncertainty concerns the study data.
  Model error, approximation error, and measurement error remain separate.

Use a theorem for a procedure-level property, a deterministic computation for the checked inputs,
and a simulation for behavior under the chosen data-generating scenarios. Do not generalize a
simulation result beyond the simulated mechanisms and parameter settings.

## 5. Models, diagnostics, and robustness

- State whether assumptions are structural, design-based, distributional, working, or computational.
- Diagnostics probe specified departures; they do not prove that a model is true or that all relevant
  assumptions hold.
- A good fit to observed data does not establish identification, causal validity, calibration outside
  the checked range, or future predictive stability.
- A robustness claim must name the perturbation and protected target: outliers, contamination,
  misspecification, dependence, tuning, missingness, measurement error, or another departure.
- Distinguish a robust point target, robust variance or standard error, bounded local influence,
  breakdown behavior, and minimax performance over a neighborhood. One does not imply the others.
- For contamination models, state the core model, contamination mechanism or neighborhood, radius or
  local scaling, target under contamination, and loss or sensitivity criterion when material.
- Sensitivity analysis reports how conclusions change across declared alternatives. Stability across
  those alternatives is evidence limited to that perturbation set, not proof of universal robustness.

For regression, interpret a coefficient conditional on the specified model, coding, scale, and
included covariates. Do not turn adjustment into randomization or a regression coefficient into a
causal effect without an identification argument.

## 6. Association, causation, and prediction

- Observational data support association language unless a design and identification argument support
  a causal claim.
- Name the causal estimand and assumptions—such as exchangeability, consistency, positivity, exclusion,
  or a valid assignment mechanism—only when they are supplied and relevant.
- Distinguish in-sample fit, cross-validated performance, validation-set tuning, and final test-set
  evaluation. Reusing the test set for tuning invalidates its role as an independent performance check.
- For time-indexed prediction, preserve two separate safeguards: evaluation splits must respect the
  forecast direction, and every lag, rolling summary, imputation, scaling, selection, and tuning step
  must be fitted or constructed using only information available inside the corresponding training
  window. A chronological split does not cure features computed earlier from the full series.
- Compare models using compatible samples, outcomes, loss functions, splits, tuning budgets, and
  preprocessing. State uncertainty or resampling variability when it affects the comparison.
- Predictive accuracy does not by itself identify a mechanism, validate a causal explanation, or
  guarantee performance under population shift.

## 7. Bayesian writing

- State the likelihood, prior, posterior target, and conditioning information that determine the
  reported posterior quantity.
- A credible interval is a posterior probability statement under the specified model and prior. Do
  not label it a frequentist confidence interval unless frequentist calibration was separately shown.
- Prior, likelihood, computation, and model sensitivity are distinct. A converged sampler does not
  establish that the model or prior is appropriate.
- Separate posterior uncertainty from posterior predictive uncertainty and from Monte Carlo error in
  the posterior computation.

## 8. Methods and results paragraphs

A method paragraph should identify the target and enough of the design, data, estimator, assumptions,
and uncertainty procedure for the result to be interpreted or reproduced. Preserve each material
source-supplied sample size explicitly,
units, exclusions, missing-data handling, transformations, tuning, random seeds, and software details
when they affect the claim.

In source-bound verification, preserve the exact supplied design quantities that support the
verdict. Group-specific missingness or exclusion rates are not replaceable by a qualitative phrase
when their magnitude or contrast is part of the evidence.

A results paragraph should normally follow:

```text
comparison or target -> estimate and units -> uncertainty -> evidence-calibrated interpretation -> scope
```

Put diagnostics and sensitivity results beside the claim they qualify. Distinguish planned analyses
from exploratory or post-selection analyses. Report missingness, exclusions, subgroup definitions,
and preprocessing before drawing a population-level conclusion.

If the fitted model reports odds or hazards while the scientific question is on a probability or
risk scale, report the supported model-scale result and name the marginal probabilities, risk
contrast, survival probability, or cumulative-incidence calculation required to answer the other
question. Do not infer the missing contrast from the coefficient alone.

For a proportional-hazards model, keep three claims separate: the fitted hazard-scale contrast, the
assumption needed to interpret one hazard ratio as constant over time, and any requested probability-
or cumulative-risk contrast. The proportional-hazards assumption governs the constant-ratio
interpretation; survival or cumulative-incidence estimates are separately required for a risk-scale
claim. Mentioning a proportional-hazards diagnostic without connecting it to constancy is incomplete.

## 9. Statistical verification checklist

Before returning work, ask:

1. Are population, sample, parameter or estimand, estimator, and estimate kept distinct?
2. Does the sampling, assignment, selection, censoring, or missingness mechanism matter to the claim?
3. Are identification assumptions separated from estimation and computation?
4. Is every p-value, interval, posterior, or prediction statement interpreted in its own framework?
5. Are finite-sample, asymptotic, resampling, and simulation claims kept at their evidence levels?
6. Does a causal, predictive, or generalization claim exceed the design or evaluation protocol?
7. Does a robustness or diagnostic claim name the departure actually checked?
8. Are effect size, direction, units, uncertainty, sample size, and multiplicity preserved where material?
9. Did revision alter the target population, outcome, contrast, model, or conditioning set?
10. Does the conclusion remain local to the supplied data, assumptions, and study design?

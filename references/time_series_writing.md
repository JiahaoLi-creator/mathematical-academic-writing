# Time-Series Writing

Use this reference when the time structure changes the mathematical object, inferential target,
or available information. It supplements [statistical writing](statistical_writing.md) and
[analysis workflows](statistical_analysis_workflows.md); it is not a checklist to append to every
analysis. Select only the distinctions needed for the task.

The methodological anchor is Robert H. Shumway and David S. Stoffer, *Time Series Analysis and
Its Applications: With R Examples*, fourth edition, Springer, 2017. Use the governing task's
notation and map any imported convention. Local-edition locators are recorded in the
[source map](statistical_source_map.md), with sampled evidence in the close-reading supplement.

## Process, observations, and stationarity

- Distinguish the stochastic process from the observed realization. State the observation interval,
  time units, and whether spacing is regular when lags or frequencies depend on them.
- For weak stationarity, state finite second moments, a constant mean, and covariance depending on
  lag rather than calendar time. Strict stationarity concerns all finite-dimensional laws.
  Strict stationarity implies weak stationarity when second moments exist; weak stationarity alone
  does not imply strict stationarity. Gaussian processes supply an important equivalence case.
- Under the book's convention, white noise has zero mean, a common finite variance, and zero
  cross-covariances at nonzero lags. Independence is stronger. Joint Gaussianity turns those zero
  covariances into independence; a Gaussian marginal distribution alone does not suffice.
- Explain what a sample ACF or PACF suggests and what remains to be checked. A quiet time plot or
  small estimated correlations does not establish stationarity or independence.

## Model specification and diagnostics

- Give the AR and MA sign conventions, orders, seasonal period, transformations, and innovation
  assumptions needed to interpret the model. Distinguish a process mean from a model intercept;
  differencing changes the meaning of a constant or drift.
- Attach root conditions to the chosen polynomial and property. For the convention
  $\phi(B)=1-\phi_1B-\cdots-\phi_pB^p$, roots outside the unit circle give the causal stationary
  AR representation. Do not turn a causal-representation condition into a claim that every
  noncausal stationary solution is impossible. State invertibility separately for the MA part.
- Explain differencing by the feature it addresses and inspect the transformed series.
  Additional differencing can introduce dependence; it is not automatic model improvement.
- Treat ACF/PACF patterns as identification aids, then compare plausible fitted models and their
  residual behavior. Distinguish residual uncorrelatedness from independence, especially when
  conditional variance may vary. Name a diagnostic's null, fitted-parameter adjustment, and
  approximation regime when they affect the conclusion; a non-rejection does not prove adequacy.

## Forecasting and information sets

- Identify the forecast origin, horizon, response scale, and information available at that origin.
  State whether parameters are known or estimated. Model-based forecast uncertainty conditional
  on fitted parameters need not include parameter or model-selection uncertainty.
- Separate the minimum-MSE predictor, a conditional expectation, from the best predictor restricted
  to a linear class. Joint Gaussian assumptions justify their equality in the book's setup;
  outside that setup, do not assert the equality or its failure without support.
- For performance evaluation, follow the actual deployment information set. Use the existing
  [prediction workflow](statistical_analysis_workflows.md) for origin-aware feature construction,
  tuning, splits, and error summaries. Retrospective explanatory analysis and future forecasting
  have different information boundaries; do not impose forecast restrictions on every task.

## Filtering, smoothing, and spectral interpretation

- In state-space notation, $E(x_t\mid y_1,\ldots,y_s)$ is a forecast when $s<t$, a filtered state
  estimate when $s=t$, and a smoothed estimate when $s>t$. Smoothing can legitimately use later
  observations for retrospective inference; it is not a real-time estimate available at $t$.
- State the transition and observation models and relevant initial/noise assumptions. In a
  linear-Gaussian model the Kalman conditional means have the stated posterior interpretation;
  with only second-moment assumptions, distinguish linear optimality from unrestricted conditional
  expectation. Do not use this source alone to validate every nonlinear or non-Gaussian filter.
- Give frequency units and the spectral normalization. Under the book's cycles-per-observation
  convention, integrating a spectral density over $[-1/2,1/2]$ gives the process variance, not
  necessarily one. Here stationary means weakly stationary with finite second moments, as in the
  book; strict stationarity alone does not supply covariance spectra. A weakly stationary process
  has a spectral distribution; a density needs additional
  conditions, with absolutely summable autocovariances a sufficient condition in the sampled text.
- Time-domain covariance and frequency-domain spectra describe the same second-order structure
  under the applicable representation. They need not identify the full non-Gaussian law.

## Beginner-facing exposition

Introduce the concrete question, define the object and required assumptions, then use a small
example to expose the consequence. Explain an information boundary with a forecast origin or a
filter/smoother comparison when useful. Preserve derivations and numerical units without making
every paragraph carry every qualification. Load only the method family the question needs.

The inspected R examples belong to the fourth edition. Verify current APIs and executable results
against the active runtime; a historical example is not evidence that today's code was run.

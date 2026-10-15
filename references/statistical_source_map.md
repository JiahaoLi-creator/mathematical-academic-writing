# Statistical Source Map

Use this map to select the smallest authoritative source set for a statistical task. These are the
user-designated primary academic references for the skill's statistical core. They guide concepts,
methods, notation, derivations, and examples; they do not replace the actual study protocol, data
documentation, domain knowledge, or a more specific source supplied for the task.

The original seven local PDFs were inspected for title, authorship, edition, and contents on
2026-08-28; VanderPlas and Vershynin were inspected on 2026-10-03, and Shumway-Stoffer on
2026-10-05. *Convex Optimization* also
belongs to the frozen 27-source writing corpus. The other original six books are methodological
reference inputs, and the three additions have a separate sampled close-reading record. The PDFs
remain local reference inputs; the skill carries bibliography, locators, and original guidance.

## Source roles

| Source | Verified edition | Load for | Boundary |
| --- | --- | --- | --- |
| Gareth James, Daniela Witten, Trevor Hastie, and Robert Tibshirani, *An Introduction to Statistical Learning: with Applications in R* | Second edition, first printing 2021 | Beginner-facing applied statistical learning; regression, classification, resampling, regularization, nonlinear methods, trees, SVMs, deep learning, survival analysis, unsupervised learning, and multiple testing | Prefer it for accessible method intuition and applied workflow. It is not a general authority for causal identification, complex surveys, or every dependence structure. |
| Trevor Hastie, Robert Tibshirani, and Jerome Friedman, *The Elements of Statistical Learning: Data Mining, Inference, and Prediction* | Second edition | Advanced statistical learning; model assessment and selection, regularization, flexible supervised and unsupervised methods, ensembles, graphical and high-dimensional methods | Use for deeper learning-method structure. Keep prediction, explanation, and causation distinct. |
| Peter D. Hoff, *A First Course in Bayesian Statistical Methods* | 2009 | Bayesian models, priors, posterior and predictive inference, Monte Carlo and MCMC, model checking, hierarchical models, regression, mixed models, and latent-variable methods | State the likelihood, prior, posterior target, computation, and sensitivity. Do not import frequentist calibration without separate support. |
| A. H. Welsh, *Aspects of Statistical Inference* | 1996 | General inferential core: statistical models, likelihood, Bayesian and frequentist inference, large-sample approximation, robust inference, randomization, resampling, finite populations, and principles of inference | Use as the main conceptual bridge between data, model, target, procedure, approximation, and robustness. Supplement it when a modern or domain-specific method lies outside its scope. |
| Frank R. Hampel, Elvezio M. Ronchetti, Peter J. Rousseeuw, and Werner A. Stahel, *Robust Statistics: The Approach Based on Influence Functions* | 1986 | Influence functions, breakdown, local and global robustness, robust estimation, testing, covariance, and regression | Name the robustness notion, model neighborhood or departure, target, tuning, and performance criterion. Do not treat outlier deletion or robust standard errors as universal robustness. |
| Jean Jacod and Philip Protter, *Discretization of Processes* | 2012 | Discretized stochastic processes, semimartingale functionals, LLNs, CLTs, stable convergence, random weights, irregular sampling, and microstructure noise | Load only when a statistical claim depends on high-frequency or stochastic-process discretization. It is not a default source for ordinary independent-data analysis. |
| Stephen Boyd and Lieven Vandenberghe, *Convex Optimization* | 2004; seventh printing with corrections, 2009 | Convex formulation, duality, KKT and optimality conditions, sensitivity, fitting, estimation, experiment design, and numerical algorithms | Use to verify the optimization problem and solution properties. Convexity does not establish that the statistical target, design, or model is appropriate. |
| Jake VanderPlas, *Python Data Science Handbook: Essential Tools for Working with Data* | First edition, December 2016; copyright 2017 | Computational explanation and reproducible examples with IPython/Jupyter, NumPy, pandas, Matplotlib, and scikit-learn; array shapes, index alignment, missing values, joins, visualization, and model validation | Explain transformations in terms of units, labels, and shapes; account for join multiplicity and missing-data choices. Use current package documentation and execution for API details: the inspected edition includes historical APIs and dtype behavior. Statistical validity still follows the design and inferential source. |
| Roman Vershynin, *High-Dimensional Probability: An Introduction with Applications in Data Science* | Second-edition pre-publication version dated July 22, 2026 | Nonasymptotic concentration, subgaussian/subexponential tails, random vectors and matrices, covariance estimation, covering, empirical processes, and statistical-learning theory | State the exact tail and dependence assumptions, centering or normalization, norm, dimension, sample size, and probability or expectation target. Preserve the dependencies of unspecified constants; an order bound does not supply a numerical guarantee. Verify theorem numbering against this pre-publication version. |
| Robert H. Shumway and David S. Stoffer, *Time Series Analysis and Its Applications: With R Examples* | Fourth edition, 2017; publisher DOI 10.1007/978-3-319-52452-8 | General time-series methodology: dependence, stationarity, ARIMA, forecasting, frequency-domain analysis, and state-space estimation; accessible explanations and R examples | Keep white noise distinct from independence, weak from strict stationarity, linear prediction from conditional expectation, and filtering from smoothing. Use the [time-series reference](time_series_writing.md) for claim-specific boundaries; verify historical R APIs separately. This is not limited to a particular course or financial series. |

## Routing order

1. Use the user's designated task source, study protocol, data dictionary, and domain requirements for
   the exact target, variables, notation, and decision boundary.
2. Load Welsh for general inference, ISL or ESL for statistical learning, Hoff for Bayesian analysis,
   Hampel et al. for robust statistics, Jacod-Protter for process discretization, and Boyd-Vandenberghe
   for convex optimization. Load VanderPlas when computational operations carry the statistical
   meaning, Vershynin for high-dimensional or nonasymptotic probability arguments, and
   Shumway-Stoffer for classical time-series modeling and prediction. Load more
   than one only when the dependency chain crosses their roles.
3. Use [general statistical analysis workflows](statistical_analysis_workflows.md) to connect question,
   provenance, unit, target, method, diagnostics, sensitivity, and reporting.
4. Use professional or reporting guidance for transparency and communication; do not let a reporting
   checklist override the method's mathematical conditions.
5. Load a course profile only when the task actually belongs to that course workflow.

## Sampled additions in v0.4.3

Locators refer to the inspected local editions. PDF page numbers are one-based file positions;
printed page numbers refer to the page labels inside the book.

| Source and locator | Writing practice adopted |
| --- | --- |
| VanderPlas, Chapter 2, "Rules of Broadcasting", printed pp. 65-67, PDF pp. 83-85 | Explain a numerical operation through input shapes, the alignment rule, and output shape before interpreting the resulting quantity. |
| VanderPlas, Chapter 3, "Operating on Data in Pandas" and "Handling Missing Data", printed pp. 115-126, PDF pp. 133-144 | Distinguish index alignment from positional arithmetic and explain how a missing-value operation changes the analysis data. Check historical dtype examples against the active runtime. |
| VanderPlas, Chapter 3, "Categories of Joins", printed pp. 147-149, PDF pp. 165-167 | State the join keys and multiplicity, then relate resulting rows to the analysis unit. |
| VanderPlas, Chapter 5, "Thinking About Model Validation", printed pp. 359-363, PDF pp. 377-381 | Separate fitting from performance evaluation and explain what the validation split estimates under the actual data design. |
| Vershynin, Sections 2.2, 2.6, and 2.9, printed pp. 28-29, 36-39, and 47-48, PDF pp. 36-37, 44-47, and 55-56 | Attach the distributional and independence assumptions to the inequality; expose the moment-method dependency and distinguish absolute-constant equivalence from equality. |
| Vershynin, Section 3.1, Theorem 3.1.1, printed pp. 60-61, PDF pp. 68-69 | Specify the coordinate assumptions and scale before describing norm concentration. |
| Vershynin, Section 4.7, Theorem 4.7.1 and Remarks 4.7.2-4.7.3, printed pp. 125-127, PDF pp. 133-135 | State the estimator, norm, tail parameter, and dimension/sample-size dependence; report expectation and high-probability conclusions as different claims. |
| Shumway-Stoffer, Example 1.8 and Section 1.4, PDF pp. 18-20 and 29-31 | Separate white noise, iid noise, and Gaussian white noise; introduce stationarity by its precise moment or distributional conditions. |
| Shumway-Stoffer, Section 3.1 and Section 3.4, PDF pp. 87-90 and 112-115 | State the model and causal representation assumptions, then distinguish best linear prediction from the conditional-expectation target. |
| Shumway-Stoffer, Section 3.7, PDF pp. 147-151 | Connect identification, differencing, fitting, residual diagnostics, and model comparison without treating an ACF pattern or a non-rejected test as proof. |
| Shumway-Stoffer, Section 4.2, PDF pp. 184-186 | Specify frequency units, density existence conditions, and normalization before interpreting spectral mass. |
| Shumway-Stoffer, Section 6.2, PDF pp. 302-305 | Make the observation information set explicit for prediction, filtering, and smoothing; distinguish Gaussian conditional-mean interpretation from linear optimality. |

Shumway-Stoffer's title and edition are visible on local PDF pp. 1-2; the publication year and
DOI are verified against the [publisher's fourth-edition record](https://link.springer.com/book/10.1007/978-3-319-52452-8).
Use the local file-page locators above: its pagination is not assumed identical to other editions
or the publisher's digital layout. The supplement samples 35 pages of this book, not its full text.

These anchors extend qualitative source coverage. The published corpus rates and thresholds remain
bound to the original 27-source measurement. Recomputing those rates requires a separately reviewed
sample and recalibration.

## Source conflicts and gaps

- Preserve the notation and scope of the governing task source. Introduce a book's notation only when
  it clarifies the argument, and map the symbols explicitly.
- Distinguish a book's theorem, example, simulation, recommendation, and historical discussion. Their
  evidence roles are different.
- When two sources use different inferential frameworks, state the framework instead of blending their
  probability statements.
- An older source may remain authoritative for a concept while lacking later methods or current
  software practice. Use a current, verified supplement for the missing method and label its role.
- If a claimed theorem, algorithm, or interpretation cannot be located in the selected source, mark it
  `unsupported` or `ambiguous`; do not infer it from the book's general subject.
- Cite chapter, section, theorem, example, or page locators from the inspected edition. A title alone is
  not enough evidence for a material claim.

## Public and release boundary

The source map may name copyrighted works and use short bibliographic facts. Do not bundle, quote at
length, or publish the local PDFs. A public-safe release keeps the routing rules and bibliography but
removes private paths, course-only assets, and any extracted text beyond short, necessary quotations.

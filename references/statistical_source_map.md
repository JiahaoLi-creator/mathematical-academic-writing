# Statistical Source Map

Use this map to select the smallest authoritative source set for a statistical task. These are the
user-designated primary academic references for the skill's statistical core. They guide concepts,
methods, notation, derivations, and examples; they do not replace the actual study protocol, data
documentation, domain knowledge, or a more specific source supplied for the task.

The local PDFs were inspected for title, authorship, edition, and contents on 2026-08-28. They are
reference inputs, not redistributed skill assets and not members of the frozen 27-source corpus.

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

## Routing order

1. Use the user's designated task source, study protocol, data dictionary, and domain requirements for
   the exact target, variables, notation, and decision boundary.
2. Load Welsh for general inference, ISL or ESL for statistical learning, Hoff for Bayesian analysis,
   Hampel et al. for robust statistics, Jacod-Protter for process discretization, and Boyd-Vandenberghe
   for convex optimization. Load more than one only when the dependency chain crosses their roles.
3. Use [general statistical analysis workflows](statistical_analysis_workflows.md) to connect question,
   provenance, unit, target, method, diagnostics, sensitivity, and reporting.
4. Use professional or reporting guidance for transparency and communication; do not let a reporting
   checklist override the method's mathematical conditions.
5. Load a course profile only when the task actually belongs to that course workflow.

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

# Quantitative Finance Profile

Load this profile only when mathematical finance, pricing, hedging, martingale measures, calibration, or identification is in scope. The governing source still determines theorem assumptions and notation.

## Audit shields

- Distinguish the physical measure from a pricing or risk-neutral measure.
- Distinguish a local martingale density from a true martingale density before using it to define an equivalent probability measure.
- Distinguish existence of an equivalent local martingale measure from uniqueness; uniqueness is tied to completeness only under the relevant market and admissibility assumptions.
- Separate no-arbitrage, attainability, replication, and a chosen pricing rule. Replication fixes the price of an attainable claim under the stated frictionless model; it does not by itself price every claim in an incomplete market.
- State self-financing and admissibility conditions beside a trading-strategy result.
- Keep continuous-time replication separate from discrete rebalancing error, transaction costs, and model misspecification.
- Distinguish calibration fit from parameter identification. Several parameter sets or models may fit the same observables.
- Distinguish observational equivalence from structural equality and risk-neutral dynamics from real-world dynamics.
- For jump or stochastic-volatility models, do not infer unspanned risk premia or completeness from diffusion-model intuition.

## Evidence vocabulary

- A payoff identity or exact replication `yields` a model price under the stated assumptions.
- A no-arbitrage theorem `establishes` only the conclusion and market class in its hypotheses.
- A calibration `fits`, `matches`, or `minimizes` the stated criterion; it does not prove the model true.
- A backtest `reports` realized sample behavior under its data and protocol; it does not establish a universal trading advantage.

## Required register entries

When material, record the probability measure, numeraire, filtration, traded assets, admissible strategies, horizon, claim class, market frictions, and whether the result concerns pricing, hedging, identification, or empirical performance.

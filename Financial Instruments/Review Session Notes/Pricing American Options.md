---
academic_level: graduate
aliases:
- American Call Option
- American Option Pricing
- Early Exercise
- Pricing American Options
cssclasses:
- academia
enhanced: true
enhancement_date: '2025-11-06'
enhancement_id: batch09-000179
key_concepts:
- Black-Scholes option pricing model and continuous-time finance
- Binomial option pricing model and lattice methods
- Options Greeks and sensitivity analysis for risk management
- Risk-neutral measures and martingale pricing
- Martingale theory and change of measure
- Convexity adjustments and yield curve sensitivity
- Credit default swaps (CDS) and credit risk modeling
- Collateralized debt obligations (CDO) and tranche structure
- Sensitivity analysis and Greeks calculation
- Credit Risk Management and Default Probability
- Expected Loss and Loss Given Default Models
- Risk Measurement and VaR Backtesting
- Ito's Lemma and Lognormal Asset Price Dynamics
- Risk-Neutral Valuation in Option Pricing
- 'Greeks: Delta, Gamma, Theta, and Vega Hedging'
- Option Valuation and Exercise Strategies
- Value at Risk and Expected Shortfall
- Binomial Option Pricing Model for Discrete Time Valuation
- Credit Spreads and Rating Migration Analysis
- Factor Models and Asset Pricing
- Black-Scholes Option Pricing Model and Its Applications
- Options Trading Strategies and Risk Management
- American Option Pricing and Early Exercise Premium
- Stress Testing and Extreme Value Analysis
- Lattice Methods and Recombining Trees in Derivatives Pricing
- Fama-French Factors and Style Analysis
- Arbitrage Pricing Theory and Multi-Factor Models
linter-yaml-title-alias: Pricing American Options
professional_application: theoreti
status: active
tags:
- american-derivatives
- asset-allocation
- binomial-model
- black-scholes-model
- cds
- collateralized-debt-obligation
- continuous-time-pricing
- convexity-adjustment
- counterparty-risk
- credit-default-swap
- credit-derivatives
- credit-modeling
- credit-rating
- default-probability
- delta-hedging
- put-options
- bsm-model
- recovery-rate
- european-options
- call-options
- multi-period-binomial
- black-scholes-formula
- butterfly-spreads
- lattice-models
- strangles
- expected-shortfall
- binomial-tree
- straddles
- parametric-var
- american-options
- partial-differential-equation
- discrete-time-pricing
- var-methodologies
- historical-var
- conditional-var
- extreme-value-theory
- book-to-market
- risk-neutral-valuation
- volatility-analysis
- covered-calls
- cox-ross-rubinstein
- ' exposure-at-default'
- style-analysis
- momentum
- option-strategies
- optional-exercise
- stress-testing
- unexpected-loss
- rating-migration
- expected-loss
- credit-migration
- value-at-risk
- binomial-option-pricing
- credit-spreads
- arbitrage-pricing-theory
- ito-calculus
- multi-factor-models
- crr-model
- iron-condors
- option-pricing
- protective-puts
- volatility-surface
- probabilty-of-default
- loss-given-default
- size-effect
- factor-models
- value-factor
- lognormal-distribution
- monte-carlo-var
- risk-management
- var-backtesting
- ' recombining-trees'
- options-trading
- apt
- fama-french
title: Pricing American Options
type: note
---
--



# Pricing American Options

## 1. Preamble

[^1]: Initial stock price: $S_0$
[^2]: Three period binomial tree:
   - Price increase factor $u$ with probability $q$
   - Price decrease factor $d$ with probability $(1 - q)$
[^3]: No dividends
[^4]: Interest rate on risk-free asset (continuously compounded): $r$

## 2. Computing Price of an American Option

[^1]: Binomial tree for stock price evolution:

   **Period $t=1$:**
   - $S_u = S_0 \cdot u$
   - $S_d = S_0 \cdot d$
   
   **Period $t=2$:**
   - $S_{uu} = S_0 \cdot u \cdot u$
   - $S_{ud} = S_{du} = S_0 \cdot u \cdot d$
   - $S_{dd} = S_0 \cdot d \cdot d$
   
   **Period $t=3$:**
   - $S_{uuu} = S_0 \cdot u \cdot u \cdot u$
   - $S_{uud} = S_{udu} = S_0 \cdot u \cdot u \cdot d$
   - $S_{dud} = S_{ddu} = S_0 \cdot d \cdot d \cdot u$
   - $S_{ddd} = S_0 \cdot d \cdot d \cdot d$
[^2]: **Property of American option**: At maturity $T$, the payoff of an American option is equal to the payoff of a European option.

[^3]: **Strategy for pricing American option**: For each node in the binomial tree, compute:
   - (i) The value of waiting until next period
   - (ii) The value of exercising the option in the current period

[^4]: Consider an American call option.

[^5]: American call option payoff at maturity $t = T = 3$:
   $$\begin{aligned}
   \mathcal{C}_{uuu} &= \max\{S_{uuu}-K, 0\} \\
   \mathcal{C}_{uud} &= \max\{S_{uud}-K, 0\} \\
   \mathcal{C}_{dud} &= \max\{S_{dud}-K, 0\} \\
   \mathcal{C}_{ddd} &= \max\{S_{ddd}-K, 0\}
   \end{aligned}$$
[^6]: Risk neutral probability $q^*$ equates gross return on stock to gross return on risk-free asset with interest rate $r$:
   $$q^{*}\cdot u+(1-q^{*})\cdot d=\exp(r)$$
[^7]: American call option at $t = T - 1 = 2$ (working backwards):

   **Case 1: Node $uu$**
   - Value of waiting: $c_{\text{wait}}^{uu} = \exp(-r) \cdot [q^* \cdot c_{uuu} + (1 - q^*) \cdot c_{uud}]$
   - Value of exercising: $c_{\text{exercise}}^{uu} = \max\{S_{uu} - K, 0\}$
   - Value of option: $c_{uu} = \max\{c_{\text{wait}}^{uu}, c_{\text{exercise}}^{uu}\}$

   **Case 2: Node $ud = du$**
   - Value of waiting: $c_{\text{wait}}^{ud} = \exp(-r) \cdot [q^* \cdot c_{udu} + (1 - q^*) \cdot c_{udd}]$
   - Value of exercising: $c_{\text{exercise}}^{ud} = \max\{S_{ud} - K, 0\}$
   - Value of option: $c_{ud} = \max\{c_{\text{wait}}^{ud}, c_{\text{exercise}}^{ud}\}$

   **Case 3: Node $dd$**
   - Value of waiting: $c_{\text{wait}}^{dd} = \exp(-r) \cdot [q^* \cdot c_{ddu} + (1 - q^*) \cdot c_{ddd}]$
   - Value of exercising: $c_{\text{exercise}}^{dd} = \max\{S_{dd} - K, 0\}$
   - Value of option: $c_{dd} = \max\{c_{\text{wait}}^{dd}, c_{\text{exercise}}^{dd}\}$

[^8]: American call option at $t = T - 2 = 1$ (continuing backwards):

   **Case 1: Node $u$**
   - Value of waiting: $c_{\text{wait}}^{u} = \exp(-r) \cdot [q^* \cdot c_{uu} + (1 - q^*) \cdot c_{ud}]$
   - Value of exercising: $c_{\text{exercise}}^{u} = \max\{S_{u} - K, 0\}$
   - Value of option: $c_{u} = \max\{c_{\text{wait}}^{u}, c_{\text{exercise}}^{u}\}$

   **Case 2: Node $d$**
   - Value of waiting: $c_{\text{wait}}^{d} = \exp(-r) \cdot [q^* \cdot c_{du} + (1 - q^*) \cdot c_{dd}]$
   - Value of exercising: $c_{\text{exercise}}^{d} = \max\{S_{d} - K, 0\}$
   - Value of option: $c_{d} = \max\{c_{\text{wait}}^{d}, c_{\text{exercise}}^{d}\}$
	
[^9]: American call option at $t = 0$ (initial price):
   - Value of waiting: $c_{\text{wait}}^{0} = \exp(-r) \cdot [q^* \cdot c_{u} + (1 - q^*) \cdot c_{d}]$
   - Value of exercising: $c_{\text{exercise}}^{0} = \max\{S_{0} - K, 0\}$
   - Value of option: $c_{0} = \max\{c_{\text{wait}}^{0}, c_{\text{exercise}}^{0}\}$
## 3. Exercising American Option Prior to Maturity

[^1]: Exercise American option early at time $t$ and node $j$ if and only if:
   $$C_j^{\text{exercise}}(t) > C_j^{\text{wait}}(t)$$

## 4. Accounting for Dividends in Pricing American Options

[^1]: Dividends complicate matters because stock prices drop as a byproduct of dividends.

[^2]: Consider a dividend yield $y$.

[^3]: Construct the binomial tree for the pre-dividend stock price.

[^4]: Construct the binomial tree for the post-dividend stock price:
   $$S_{\text{post}} = S_{\text{pre}} \cdot (1 - y)$$

[^5]: Note pre-dividend price one period ahead depends on post-dividend price this period.
   - For example: $S_{uu,\text{pre}}(2) = S_{u,\text{post}}(1) \cdot u$

[^6]: For call payoff, use pre-dividend stock price.

[^7]: For put payoff, use post-dividend stock price.

[^8]: **Intuition**: Put option is more valuable as the stock price falls.

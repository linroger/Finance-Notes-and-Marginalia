---
academic_level: graduate
aliases:
- BOPM
- Binomial Option Pricing
- Option Valuation
- Single-Period Option Model
cssclasses:
- academia
enhanced: true
enhancement_date: '2025-11-06'
enhancement_id: batch09-000172
key_concepts:
- Black-Scholes option pricing model and continuous-time finance
- Binomial option pricing model and lattice methods
- Options Greeks and sensitivity analysis for risk management
- Risk-neutral measures and martingale pricing
- Martingale theory and change of measure
- Duration analysis and interest rate risk management
- Convexity adjustments and yield curve sensitivity
- Discounted cash flow (DCF) valuation methodology
- Capital Asset Pricing Model (CAPM) and expected returns
- Weighted Average Cost of Capital (WACC) and firm valuation
- Credit default swaps (CDS) and credit risk modeling
- Value at Risk (VaR) and tail risk measurement
- Expected shortfall and coherent risk measures
- Collateralized debt obligations (CDO) and tranche structure
- Arbitrage opportunities and no-arbitrage pricing
- Beta estimation and systematic risk measurement
- Factor models and multi-factor pricing
- Beta estimation and systematic risk measurement
- Risk preference theory and utility functions
- Sensitivity analysis and Greeks calculation
- 'Valuation Methods: DCF, Comps, and Precedents'
- Ito's Lemma and Lognormal Asset Price Dynamics
- Risk-Neutral Valuation in Option Pricing
- Value at Risk and Expected Shortfall
- Vasicek Interest Rate Model and Mean Reversion
- Short Rate Models and Term Structure Dynamics
- Company Valuation and Multiple Analysis
- Capital Asset Pricing Model and Beta Analysis
- Comparable Company Analysis and Trading Multiples
- 'Greeks: Delta, Gamma, Theta, and Vega Hedging'
- Ornstein-Uhlenbeck Process in Finance
- Cost of Equity and Expected Returns
- Black-Scholes Option Pricing Model and Its Applications
- Security Market Line and Risk-Return Tradeoff
- Options Trading Strategies and Risk Management
- Stress Testing and Extreme Value Analysis
- Lattice Methods and Recombining Trees in Derivatives Pricing
- Fama-French Factors and Style Analysis
- Risk Measurement and VaR Backtesting
- Bond Pricing and Yield to Maturity Analysis
- Fixed Income Securities and Credit Quality
- Binomial Option Pricing Model for Discrete Time Valuation
- American Option Pricing and Early Exercise Premium
- Option Valuation and Exercise Strategies
- Factor Models and Asset Pricing
- Government and Corporate Bond Markets
- Arbitrage Pricing Theory and Multi-Factor Models
linter-yaml-title-alias: Binomial Trees and Option Pricing MBA
professional_application: theoreti
status: active
tags:
- arbitrage-opportunity
- arbitrage-pricing
- asset-allocation
- beta-estimation
- binomial-model
- black-scholes-model
- capital-asset-pricing
- capital-structure
- caplet
- cash-flow-modeling
- cds
- coherent-risk-measure
- collateralized-debt-obligation
- conditional-var
- continuous-time-pricing
- leveraged-buyout
- hull-white
- call-options
- cir-model
- butterfly-spreads
- dcf-analysis
- expected-shortfall
- binomial-tree
- straddles
- extreme-value-theory
- american-options
- partial-differential-equation
- book-to-market
- risk-neutral-valuation
- volatility-analysis
- style-analysis
- bond-pricing
- option-strategies
- corporate-bonds
- capital-asset-pricing-model
- arbitrage-pricing-theory
- market-price-of-risk
- volatility-surface
- value-factor
- vasicek-model
- sharpe-ratio
- dirty-price
- monte-carlo-var
- options-trading
- coupon-bonds
- yield-to-maturity
- fama-french
- price-to-earnings
- bsm-model
- zero-coupon-bonds
- black-scholes-formula
- parametric-var
- lognormal-models
- var-methodologies
- historical-var
- mean-reversion
- crr-model
- systematic-risk
- protective-puts
- government-bonds
- alpha
- security-market-line
- idiosyncratic-risk
- beta
- risk-premium
- put-options
- affine-term-structure
- multi-period-binomial
- capm
- momentum
- market-risk-premium
- discrete-time-pricing
- covered-calls
- stress-testing
- ornstein-uhlenbeck
- comparable-analysis
- investment-analysis
- economic-value-added
- portfolio-optimization
- value-at-risk
- factor-models
- risk-management
- var-backtesting
- sum-of-parts
- european-options
- clean-price
- lattice-models
- strangles
- fixed-income
- cox-ross-rubinstein
- short-rate-models
- optional-exercise
- efficient-frontier
- binomial-option-pricing
- multi-factor-models
- ito-calculus
- trading-multiples
- iron-condors
- option-pricing
- financial-markets
- size-effect
- precedent-transactions
- lognormal-distribution
- ipo-valuation
- market-multiple
- ' recombining-trees'
- apt
- current-yield
title: Binomial Trees and Option Pricing MBA
type: note
---
--



# Binomial Trees and Option Pricing MBA
## 1. BINOMIAL TREES IN PHARMACEUTICALS

### 1.1. PARAMETERS

[^1]: Let $i$ denote a pharmaceutical company
[^2]: Stock price at maturity $t = T$: $S_{T, i} \in \{S_d, S_u\}$
   a. Decrease scenario: $S_d$
   b. Increase scenario: $S_u$
[^3]: Probability distribution at maturity $t = T$
   a. Decrease scenario: $q$
   b. Increase scenario: $1 - q$
[^4]: Systematic risk: $\beta_i$
[^5]: Annualized risk-free interest rate (continuously compounded): $r_f$
[^6]: Annualized expected excess return (annually compounded): $E[R_m] - r_f$

### 1.2. CAPM

[^1]: Let $R_i$ denote the expected return on the stock of pharmaceutical company
[^2]: Note $R_i$ is a random variable because stock price $S_{T, i} \in \{S_d, S_u\}$ at maturity $t = T$ is a random variable, and so the realization of $R$ depends on the realization of $S_T$.
[^3]: Relationship between continuously compounded and annually compounded interest rates:

   $$1 + \bar{r}_f = \exp(r_f)$$

   $$1 + \bar{r}_f = \exp(-r_f)$$

[^4]: CAPM formula:

   $$E[R_i] = \bar{r}_f + \beta_i \cdot [E[R_m] - r_f]$$

[^5]: Note $E[R_i]$ varies (linearly) with $\beta_i$.

### 1.3. STOCK VALUATION AT INCEPTION

[^1]: The stock price $S_{0, i}$ at inception $t = 0$ is equal to the expected discounted stock price at maturity $t = T$.
[^2]: Expected stock price at maturity $t = T$ (i.e., the mean of the random variable $S_{T, i}$):

   $$E_q[S_{T, i}] = q \cdot S_u + (1 - q) \cdot S_d$$

[^3]: Use expected stock price return $E[R_i]$ to compute present-value at inception:
   $$(1 + E[R_i]) \cdot S_{0, i} = E[S_{T, i}]$$

### 1.4. AT-THE-MONEY OPTION UNDER DYNAMIC REPLICATION

[^1]: An **at-the-money** ("ATM") call option features a strike price $K_i$ equal to the current spot stock price $S_0$ at inception $t = 0$, i.e. $K_i = S_{0, i}$
[^2]: Payoff from option at maturity $t = T$ depends on realized stock price $S_{T, i}$ at maturity:
   $$c(S_{T, i}) = \begin{cases} \max\{S_d - K_i, 0\} & \text{if } S_{T, i} = S_d \\ \max\{S_u - K_i, 0\} & \text{if } S_{T, i} = S_u \end{cases}$$
[^3]: Value of position in stocks at inception $t = 0$:
   $$\Delta_{i, 0} = \frac{\max\{S_u - K_i, 0\} - \max\{S_d - K_i, 0\}}{S_u - S_d}$$
[^4]: Value of position in bonds at inception $t = 0$:
   $$B_0 = e^{(-r_f)} \cdot [\max\{S_u - K_i, 0\} - \Delta_{i, 0} \cdot S_u]$$
[^5]: Value of ATM option at inception $t = 0$:

   $$V_0^{\text{ATM}} = \Delta_{i, 0} \cdot S_{0, i} + B_0$$

[^6]: Payoff from dynamic replication portfolio at maturity $t = T$ should replicate the payoff from the option:

   $$V_{T, i}^{DR}(S_{T, i}) = \begin{cases} \Delta_{i, 0} \cdot S_d + \exp(r_f) \cdot B_0 & \text{if } S_{T, i} = S_d \\ \Delta_{i, 0} \cdot S_u + \exp(r_f) \cdot B_0 & \text{if } S_{T, i} = S_u \end{cases}$$

### 1.5. AT-THE-MONEY OPTION UNDER RISK NEUTRAL METHODOLOGY

[^1]: Risk neutral probability: The probability such that the risky asset (stock) yields an expected (gross) return equal to that of the risk-free asset (bond):
   $$q^* \cdot \frac{S_u}{S_0} + (1 - q^*) \cdot \frac{S_d}{S_0} = e^{r_f}$$

[^2]: Expected stock price at maturity $t = T$ under risk neutral probability:
   $$E_{q^*}[S_{T, i}] = q^* \cdot S_u + (1 - q^*) \cdot S_d$$

[^3]: Expected stock price at maturity $t = T$ under analysts' probability:
   $$E_q[S_{T, i}] = q \cdot S_u + (1 - q) \cdot S_d$$

[^4]: Question: Why may the probabilities $(q, q^*)$ differ?

[^5]: Value of ATM option under risk neutral methodology at inception $t = 0$:
   $$V_0^{\text{ATM}} = \exp(-r_f) \cdot [q^* \cdot \max\{S_u - K_i, 0\} + (1 - q^*) \cdot \max\{S_d - K_i, 0\}]$$

### 1.6. OPTION VALUE COMPARATIVE STATICS

#### 1.6.1. CHANGE IN ANALYST PROBABILITIES

[^1]: Suppose that $q$ changes.
[^2]: All else equal, $E_q[S_{T, i}]$ changes because the probability distribution has changed.
[^3]: In turn, the present-value of the stock price $S_0$ at inception $t = 0$ changes.
[^4]: Furthermore, the risk neutral probability $q^*$ changes due to change in $S_0$.

#### 1.6.2. CHANGE IN MARKET EXPOSURE

[^1]: Suppose that $\beta_i$ changes.
[^2]: All else equal, $E[R_i]$ changes by CAPM formula.
[^3]: In turn, the present-value of the stock price $S_0$ at inception $t = 0$ changes.
[^4]: Furthermore, the risk neutral probability $q^*$ changes due to change in $S_0$.

---

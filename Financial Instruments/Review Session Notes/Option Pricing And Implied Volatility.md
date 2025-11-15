---
academic_level: graduate
aliases:
- BSM
- Black-Scholes
- Option Pricing Model
- Volatility Calculation
cssclasses:
- academia
enhanced: true
enhancement_date: '2025-11-06'
enhancement_id: batch09-000176
key_concepts:
- Black-Scholes option pricing model and continuous-time finance
- Implied volatility calculation and volatility surface analysis
- Options Greeks and sensitivity analysis for risk management
- Delta hedging and dynamic replication strategies
- Convexity adjustments and yield curve sensitivity
- Credit default swaps (CDS) and credit risk modeling
- Collateralized debt obligations (CDO) and tranche structure
- Volatility modeling and estimation techniques
- Risk preference theory and utility functions
- Sensitivity analysis and Greeks calculation
- Risk Measurement and VaR Backtesting
- Delta, Gamma, and Vega Hedging Techniques
- 'Greeks: Delta, Gamma, Theta, and Vega Hedging'
- Ornstein-Uhlenbeck Process in Finance
- Value at Risk and Expected Shortfall
- Option Valuation and Exercise Strategies
- Factor Models and Asset Pricing
- Vasicek Interest Rate Model and Mean Reversion
- Short Rate Models and Term Structure Dynamics
- Hedging Strategies and Risk Mitigation
- Options Trading Strategies and Risk Management
- Dynamic vs Static Hedging in Practice
- Stress Testing and Extreme Value Analysis
- Fama-French Factors and Style Analysis
- Arbitrage Pricing Theory and Multi-Factor Models
linter-yaml-title-alias: Option Pricing and Implied Volatility
professional_application: theoreti
status: active
tags:
- binomial-model
- black-scholes-model
- cds
- collateralized-debt-obligation
- continuous-time-pricing
- convexity
- convexity-adjustment
- counterparty-risk
- credit-default-swap
- credit-derivatives
- credit-modeling
- credit-rating
- default-probability
- delta-hedging
- derivatives
- put-options
- affine-term-structure
- cross-hedging
- hull-white
- call-options
- cir-model
- butterfly-spreads
- momentum
- strangles
- expected-shortfall
- straddles
- parametric-var
- conditional-var
- extreme-value-theory
- basis-risk
- var-methodologies
- historical-var
- hedge-strategies
- book-to-market
- mean-reversion
- vega-hedging
- lognormal-models
- volatility-analysis
- covered-calls
- style-analysis
- short-rate-models
- option-strategies
- stress-testing
- roll-over-risk
- mathematical-finance
- ornstein-uhlenbeck
- quantitative-finance
- value-at-risk
- arbitrage-pricing-theory
- multi-factor-models
- iron-condors
- protective-puts
- market-price-of-risk
- static-hedging
- size-effect
- factor-models
- value-factor
- vasicek-model
- gamma-hedging
- dynamic-hedging
- hedge-effectiveness
- monte-carlo-var
- risk-management
- var-backtesting
- options-trading
- apt
- risk-premium
- fama-french
title: Option Pricing and Implied Volatility
type: note
---
--



# BLACK-SCHOLES MODEL OF OPTION PRICING
## 1. PARAMETERS
1. Stock price: $S$
2. Strike price: $K$
3. Interest rate on risk-free asset (continuously compounded): $r$
4. Maturity: $T$
5. Stock volatility: $\sigma$
## 2. OPTIMAL PRICING FORMULA

[^1]: Delta hedging parameters:
   $$\begin{array}{c}{{d_{1}(S,K,T,r,\sigma)=\frac{\ln\left[\frac{S}{K}\right]+\left(r+\frac{\sigma^{2}}{2}\right)\cdot T}{\sigma\cdot\sqrt{T}}}}\\ {{d_{2}(S,K,T,r,\sigma)=d_{1}-\sigma\cdot\sqrt{T}}}\end{array}$$

[^2]: Standard normal cumulative distribution function:
   $$\Phi(x):={\frac{1}{\sqrt{2\pi}}}\cdot\int_{-\infty}^{x}\exp\left(-{\frac{1}{2}}\cdot u^{2}\right)du$$

[^3]: Call option price:
   $$c=S\cdot\Phi\big(d_{1}(S,K,T,r,\sigma)\big)-K\cdot\exp(-r\cdot T)\cdot\Phi\big(d_{2}(S,K,T,r,\sigma)\big)$$

[^4]: Put option price:
   $$p=-S\cdot\Phi\bigl(-d_{1}(S,K,T,r,\sigma)\bigr)+K\cdot\exp(-r\cdot T)\cdot\Phi\bigl(-d_{2}(S,K,T,r,\sigma)\bigr)$$

## 3. IMPLIED VOLATILITY

[^1]: Suppose we observe option prices $(c, p)$.

[^2]: **Question**: What is the volatility parameter $\sigma$ *implied* by the Black-Scholes model?

[^3]: **Answer**: It is the volatility parameter that solves a non-linear equation:
   $$\begin{aligned}
   c &= S \cdot \Phi\big(d_1(S,K,T,r,\sigma_c^*)\big)-K \cdot e^{-r \cdot T} \cdot \Phi\big(d_2(S,K,T,r,\sigma_c^*)\big)\\
   p &= -S \cdot \Phi\big(-d_1(S,K,T,r,\sigma_p^*)\big)+K \cdot e^{-r \cdot T} \cdot \Phi\big(-d_2(S,K,T,r,\sigma_p^*)\big)
   \end{aligned}$$

[^4]: Use non-linear equation solve function to solve for implied volatility values ($\sigma_{c}^{*}, \sigma_{p}^{*}$).

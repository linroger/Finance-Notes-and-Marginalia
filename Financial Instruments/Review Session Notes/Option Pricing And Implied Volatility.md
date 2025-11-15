---
aliases:
- BSM
- Black-Scholes
- Option Pricing Model
- Volatility Calculation
cssclasses:
- academia
enhanced: true
enhancement_date: '2025-11-06'
enhancement_id: batch03-b365d7
key_concepts:
- Black-Scholes model and option pricing theory
- Risk-neutral measures and martingale pricing
- Delta hedging strategies in options portfolio management
- Term structure of interest rates and yield curve modeling
- Partial differential equations in financial modeling
- Volatility modeling and forecasting techniques
- Portfolio hedging and risk reduction strategies
- Options Greeks and sensitivity analysis
linter-yaml-title-alias: Option Pricing and Implied Volatility
tags:
- black-scholes
- convexity
- delta
- delta-hedging
- derivatives-pricing
- exotic-options
- fixed_income
- gamma
- greeks
- hedging
- implied-volatility
- options
- pde
- replication
- risk-management
- risk-neutral
- theta
- vega
- yield-curve
title: Option Pricing and Implied Volatility
---

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

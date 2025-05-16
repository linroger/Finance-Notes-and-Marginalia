---
cssclasses:
  - academia
linter-yaml-title-alias: Option Pricing and Implied Volatility
title: Option Pricing and Implied Volatility
tags:
  - black_scholes_model
  - call_option
  - delta_hedging
  - implied_volatility
  - option_pricing
  - normal_distribution
  - put_option
  - financial_mathematics
aliases:
  - BSM
  - Black-Scholes
  - Option Pricing Model
  - Volatility Calculation
key_concepts:
  - Delta hedging parameters
  - Implied volatility extraction
  - Risk-free rate influence
  - Maturity effects on pricing
  - Stock price and strike price relationship
  - Volatility parameter estimation
  - Normal distribution application
  - Non-linear equation solving
---

# BLACK-SCHOLES MODEL OF OPTION PRICING
## 1. PARAMETERS
1. Stock price: $S$
2. Strike price: $K$
3. Interest rate on risk-free asset (continuously compounded): $r$
4. Maturity: $T$
5. Stock volatility: $\sigma$
## 2. OPTIMAL PRICING FORMULA

1. Delta hedging parameters:
   $$\begin{array}{c}{{d_{1}(S,K,T,r,\sigma)=\frac{\ln\left[\frac{S}{K}\right]+\left(r+\frac{\sigma^{2}}{2}\right)\cdot T}{\sigma\cdot\sqrt{T}}}}\\ {{d_{2}(S,K,T,r,\sigma)=d_{1}-\sigma\cdot\sqrt{T}}}\end{array}$$

2. Standard normal cumulative distribution function:
   $$\Phi(x):={\frac{1}{\sqrt{2\pi}}}\cdot\int_{-\infty}^{x}\exp\left(-{\frac{1}{2}}\cdot u^{2}\right)du$$

3. Call option price:
   $$c=S\cdot\Phi\big(d_{1}(S,K,T,r,\sigma)\big)-K\cdot\exp(-r\cdot T)\cdot\Phi\big(d_{2}(S,K,T,r,\sigma)\big)$$

4. Put option price:
   $$p=-S\cdot\Phi\bigl(-d_{1}(S,K,T,r,\sigma)\bigr)+K\cdot\exp(-r\cdot T)\cdot\Phi\bigl(-d_{2}(S,K,T,r,\sigma)\bigr)$$

## 3. IMPLIED VOLATILITY

1. Suppose we observe option prices $(c, p)$.

2. **Question**: What is the volatility parameter $\sigma$ *implied* by the Black-Scholes model?

3. **Answer**: It is the volatility parameter that solves a non-linear equation:
   $$\begin{aligned}
   c &= S \cdot \Phi\big(d_1(S,K,T,r,\sigma_c^*)\big)-K \cdot e^{-r \cdot T} \cdot \Phi\big(d_2(S,K,T,r,\sigma_c^*)\big)\\
   p &= -S \cdot \Phi\big(-d_1(S,K,T,r,\sigma_p^*)\big)+K \cdot e^{-r \cdot T} \cdot \Phi\big(-d_2(S,K,T,r,\sigma_p^*)\big)
   \end{aligned}$$

4. Use non-linear equation solve function to solve for implied volatility values ($\sigma_{c}^{*}, \sigma_{p}^{*}$).
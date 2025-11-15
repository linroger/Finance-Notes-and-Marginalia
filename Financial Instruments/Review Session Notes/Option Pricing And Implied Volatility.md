---
cssclasses:
- academia
linter-yaml-title-alias: Option Pricing and Implied Volatility
title: Option Pricing and Implied Volatility
tags:
- black-scholes
- black_scholes_model
- call
- call_option
- delta_hedging
- financial_mathematics
- greeks
- hedge
- implied-vol
- implied_volatility
- interest-rate
- normal_distribution
- option
- option_pricing
- put
- put_option
- risk-free-rate
- stock
aliases:
- BSM
- Black-Scholes
- Option Pricing Model
- Volatility Calculation
key_concepts:
- Delta hedging parameters
- Delta risk management
- Delta-hedging implementation
- Derivative securities
- Dynamic hedging strategies
- Dynamic replication
- Financial risk management
- Gamma effects on options
- Gamma hedging techniques
- Hedge ratio calculation
- Hedging effectiveness
- Implied volatility extraction
- Maturity effects on pricing
- Non-linear equation solving
- Normal distribution application
- Options Greeks measurement
- Portfolio insurance methods
- Portfolio optimization
- Portfolio risk hedging
- Quantitative financial analysis
- Rho interest rate sensitivity
- Risk assessment and mitigation
- Risk-free rate influence
- Static hedging
- Stock price and strike price relationship
- Theta time decay
- Vega hedging strategies
- Vega volatility sensitivity
- Volatility parameter estimation
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

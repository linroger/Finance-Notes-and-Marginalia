---
aliases:
- Compound Interest
- Continuously Compounding
- Interest Rate Conversion
cssclasses:
- academia
enhanced: true
enhancement_date: '2025-11-06'
enhancement_id: batch03-54ed3e
key_concepts:
- Risk-neutral measures and martingale pricing
- Bond pricing and fixed income securities valuation
- Ito's lemma and stochastic calculus applications
- Monte Carlo simulation for derivatives valuation
- Credit risk modeling and default probability estimation
- Value at Risk and tail risk measurement
- Arbitrage opportunities and no-arbitrage pricing
- Portfolio hedging and risk reduction strategies
linter-yaml-title-alias: Continuously Compounding Interest
tags:
- arbitrage
- convexity
- correlation
- credit-risk
- derivatives-pricing
- duration
- exotic-options
- expected-shortfall
- fixed_income
- hedging
- monte-carlo
- options
- risk-management
- risk-neutral
- stress-testing
- var
title: Continuously Compounding Interest
---

# Continuously Compounding Interest

The LIBOR annual interest rate $r_d$ compounds at a discrete frequency. For example, interest may compound on an annual basis, a semi-annual basis, a monthly basis, and so on.

Let $n$ denote the discrete frequency with which interest compounds in a year. For example, if interest compounds on an annual basis, then $n = 1$. If interest compounds on a semi-annual basis, then $n = 2$. If interest compounds on a monthly basis, then $n = 12$.

For a given maturity $T$ and discrete compounding frequency $n$, the gross rate of return is:

$$\left(1+\frac{r_d}{n}\right)^{n\cdot T}$$

By contrast, under continuously compounding interest, the gross rate of return is:  

$$e^{(r_c\cdot T)}$$

The appropriate continuously compounding interest rate $r_c$ that aligns with the discrete compounding interest rate $r_d$ is that which equates the two gross rates of return:

$$e^{(r_c\cdot T)}=\left(1+\frac{r_d}{n}\right)^{n\cdot T}$$

Solving the equation above for the endogenous variable $r_c$ yields the formula for the continuously compounding interest rate as a function of the discrete compounding interest rate:

$$r_c=n\cdot\ln\left[1+\frac{r_d}{n}\right]$$

Note that the maturity horizon $T$ does not affect the conversion between a discrete compounding interest rate and a continuously compounding interest rate.

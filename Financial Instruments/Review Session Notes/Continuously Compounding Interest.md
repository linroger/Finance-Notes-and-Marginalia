---
academic_level: graduate
aliases:
- Compound Interest
- Continuously Compounding
- Interest Rate Conversion
cssclasses:
- academia
enhanced: true
enhancement_date: '2025-11-06'
enhancement_id: batch09-000171
key_concepts:
- Credit default swaps (CDS) and credit risk modeling
- Value at Risk (VaR) and tail risk measurement
- Expected shortfall and coherent risk measures
- LIBOR market model and multi-curve framework
- Collateralized debt obligations (CDO) and tranche structure
- Arbitrage opportunities and no-arbitrage pricing
- Financial modeling and quantitative analysis
- Risk management and portfolio optimization
- Derivatives pricing and hedging strategies
- Market risk measurement and control
- Swap Market Mechanisms and Pricing
- Risk Measurement and VaR Backtesting
- Contango, Backwardation, and Roll Yield
- Ornstein-Uhlenbeck Process in Finance
- Futures and Forward Contracts in Financial Markets
- Value at Risk and Expected Shortfall
- Vasicek Interest Rate Model and Mean Reversion
- Hedge Strategies and Basis Risk Management
- Short Rate Models and Term Structure Dynamics
- Interest Rate Swaps and Currency Swap Structures
- Stress Testing and Extreme Value Analysis
- Credit Default Swaps and Credit Risk Transfer
linter-yaml-title-alias: Continuously Compounding Interest
professional_application: theoreti
status: active
tags:
- arbitrage-free-models
- arbitrage-opportunity
- asset-allocation
- cds
- coherent-risk-measure
- collateralized-debt-obligation
- conditional-var
- counterparty-risk
- credit-default-swap
- credit-derivatives
- credit-modeling
- credit-rating
- default-probability
- expected-loss
- forward-contracts
- affine-term-structure
- hull-white
- cir-model
- expected-shortfall
- basis-risk
- parametric-var
- extreme-value-theory
- lognormal-models
- var-methodologies
- historical-var
- mean-reversion
- contango
- backwardation
- sofr
- swap-rate
- short-rate-models
- swap-spread
- stress-testing
- ornstein-uhlenbeck
- clearinghouse
- risk-premium
- marking-to-market
- value-at-risk
- total-return-swaps
- libor
- currency-swaps
- overnight-indexed-swaps
- hedge-ratio
- market-price-of-risk
- basis-swaps
- interest-rate-swaps
- vasicek-model
- monte-carlo-var
- convergence
- var-backtesting
- futures-contracts
- roll-yield
- credit-default-swaps
title: Continuously Compounding Interest
type: note
---
--



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

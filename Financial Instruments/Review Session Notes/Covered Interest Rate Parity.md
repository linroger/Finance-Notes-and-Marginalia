---
academic_level: graduate
aliases:
- CIRP
- Interest Rate Parity
- Currency Forward Pricing
cssclasses:
- academia
enhanced: true
enhancement_date: '2025-11-06'
enhancement_id: batch09-000175
key_concepts:
- Options Greeks and sensitivity analysis for risk management
- Duration analysis and interest rate risk management
- Convexity adjustments and yield curve sensitivity
- Credit default swaps (CDS) and credit risk modeling
- Value at Risk (VaR) and tail risk measurement
- Expected shortfall and coherent risk measures
- Collateralized debt obligations (CDO) and tranche structure
- Basel accords and banking regulation framework
- Arbitrage opportunities and no-arbitrage pricing
- Risk preference theory and utility functions
- Forward Rates and Curve Construction Methods
- Risk Measurement and VaR Backtesting
- Bid-Ask Spreads and Market Impact
- Contango, Backwardation, and Roll Yield
- Ornstein-Uhlenbeck Process in Finance
- Futures and Forward Contracts in Financial Markets
- Yield Curve Analysis and Bond Valuation
- Value at Risk and Expected Shortfall
- Vasicek Interest Rate Model and Mean Reversion
- Hedge Strategies and Basis Risk Management
- Market Microstructure and Liquidity Analysis
- Short Rate Models and Term Structure Dynamics
- Price Discovery and Market Efficiency
- Stress Testing and Extreme Value Analysis
- Term Structure of Interest Rates and Yield Curves
linter-yaml-title-alias: Covered Interest Rate Parity
professional_application: theoreti
status: active
tags:
- arbitrage-opportunity
- banking-regulation
- basel-accord
- capital-adequacy
- caplet
- cds
- coherent-risk-measure
- collateralized-debt-obligation
- conditional-var
- convexity-adjustment
- counterparty-risk
- credit-default-swap
- credit-derivatives
- credit-modeling
- credit-rating
- spot-rates
- affine-term-structure
- hull-white
- cir-model
- yield-curve-shocks
- high-frequency-trading
- algorithmic-trading
- expected-shortfall
- basis-risk
- parametric-var
- extreme-value-theory
- lognormal-models
- var-methodologies
- historical-var
- mean-reversion
- arbitrage
- contango
- backwardation
- term-structure
- short-rate-models
- yield-curve
- stress-testing
- mathematical-finance
- ornstein-uhlenbeck
- par-yield
- clearinghouse
- investment-analysis
- market-efficiency
- quantitative-finance
- marking-to-market
- interpolation
- forward-curve
- value-at-risk
- order-flow
- hedge-ratio
- bid-ask-spread
- market-price-of-risk
- financial-markets
- price-discovery
- liquidity
- vasicek-model
- curve-fitting
- monte-carlo-var
- convergence
- var-backtesting
- futures-contracts
- roll-yield
- market-impact
- bootstrap-method
- risk-premium
- forward-contracts
- forward-rates
title: Covered Interest Rate Parity
type: note
---
--



# Covered Interest Rate Parity
## 1. MODEL PARAMETERS

There are four model parameters that collectively determine the forward rate for a currency security.

[^1]: Home/Foreign Exchange rate: $M$
[^2]: Interest rate in home country: $r_\$$
[^3]: Interest rate in foreign country: $r_\text{€}$
[^4]: Maturity: $T$

The interest rates $(r_\$, r_\text{€})$ are continuously compounded. The exchange rate $M$ denotes the number of units of the Home currency required to purchase one unit of the Foreign currency. For example, if $M = 1.2$, then 1.2 units of the Home currency (e.g., USD) are required to purchase one unit of the Foreign currency (e.g., EUR).

## 2. FORWARD RATE UNDER NO-ARBITRAGE

Determining the forward rate of a currency security requires appealing to a no-arbitrage argument. Consider an investor in the home country, endowed with capital $N$ (measured in the home currency) to invest. This investor can pursue one of two strategies.

First, the investor can invest the home capital at the home interest rate until maturity. Let $\Pi_\$(r_\$, T, N)$ denote the payoff function from this investment strategy:
$$\Pi_\$(r_\$, T, N) = e^{(r_\$ \cdot T)} \cdot N$$

Second, the investor can convert the home capital into foreign capital, invest the foreign capital at the foreign interest rate, and convert the proceeds on the foreign capital back into the home currency at the forward rate $F$:
$$\Pi_\text{€}(F; r_\text{€}, T, N, M) = e^{(r_\text{€} \cdot T)} \cdot \frac{N}{M} \cdot F$$

Note that both payoff functions, $\Pi_\$(\cdot)$ and $\Pi_\text{€}(\cdot)$, are measured in the home currency (e.g., USD).

The forward rate $F$ adjusts so as to equate the payoffs from the two investment strategies:
$$\Pi_\$(r_\$, T, N) = \Pi_\text{€}(F; r_\text{€}, T, M, N)$$

This equation is a "no-arbitrage" condition. Solving the no-arbitrage condition for the endogenous variable $F$ yields the covered interest-rate parity formula for the forward rate:
$$F = e^{(r_\$ - r_\text{€}) \cdot T} \cdot M$$

Note that the forward rate $F$ inherits the units of the exchange rate $M$. Since the units of the exchange rate $M$ is Home/Foreign (e.g., USD/EUR), it follows that the units of the forward rate $F$ is also Home/Foreign.

## 3. INTERPRETATION

The forward rate $F$ is the exchange rate at which Home and Foreign currencies are exchanged upon maturity at time $T$ from inception. The forward rate $F$ is agreed upon at inception (i.e., at time 0).

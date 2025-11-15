---
academic_level: graduate
aliases:
- FX
- FX Quoting
- Forex
enhanced: true
enhancement_date: '2025-11-06'
enhancement_id: batch09-000147
key_concepts:
- Options Greeks and sensitivity analysis for risk management
- Duration analysis and interest rate risk management
- Convexity adjustments and yield curve sensitivity
- Credit default swaps (CDS) and credit risk modeling
- Heath-Jarrow-Morton (HJM) and forward rate dynamics
- Collateralized debt obligations (CDO) and tranche structure
- Risk preference theory and utility functions
- Sensitivity analysis and Greeks calculation
- Duration and Convexity in Fixed Income Risk Management
- Yield Curve Analysis and Bond Valuation
- Value at Risk and Expected Shortfall
- Vasicek Interest Rate Model and Mean Reversion
- Short Rate Models and Term Structure Dynamics
- Credit Risk Management and Default Probability
- Expected Loss and Loss Given Default Models
- Forward Rates and Curve Construction Methods
- Swap Market Mechanisms and Pricing
- Delta, Gamma, and Vega Hedging Techniques
- 'Greeks: Delta, Gamma, Theta, and Vega Hedging'
- Ornstein-Uhlenbeck Process in Finance
- Options Trading Strategies and Risk Management
- Stress Testing and Extreme Value Analysis
- Credit Default Swaps and Credit Risk Transfer
- Fama-French Factors and Style Analysis
- Risk Measurement and VaR Backtesting
- Contango, Backwardation, and Roll Yield
- Futures and Forward Contracts in Financial Markets
- Hedge Strategies and Basis Risk Management
- Bond Portfolio Immunization Strategies
- Dynamic vs Static Hedging in Practice
- Interest Rate Swaps and Currency Swap Structures
- Term Structure of Interest Rates and Yield Curves
- Option Valuation and Exercise Strategies
- Credit Spreads and Rating Migration Analysis
- Interest Rate Risk and DV01 Calculations
- Hedging Strategies and Risk Mitigation
- Factor Models and Asset Pricing
- Arbitrage Pricing Theory and Multi-Factor Models
professional_application: theoreti
status: active
tags:
- asset-allocation
- caplet
- cds
- collateralized-debt-obligation
- convexity-adjustment
- counterparty-risk
- credit-default-swap
- credit-derivatives
- credit-modeling
- credit-rating
- currency-markets
- currency-strategy
- default-probability
- delta-hedging
- duration-analysis
- hull-white
- call-options
- cir-model
- butterfly-spreads
- expected-shortfall
- straddles
- extreme-value-theory
- book-to-market
- backwardation
- style-analysis
- option-strategies
- yield-curve
- unexpected-loss
- clearinghouse
- interpolation
- overnight-indexed-swaps
- interest-rate-risk
- arbitrage-pricing-theory
- hedge-ratio
- market-price-of-risk
- loss-given-default
- value-factor
- vasicek-model
- dynamic-hedging
- monte-carlo-var
- options-trading
- forward-contracts
- forward-rates
- fama-french
- recovery-rate
- parametric-var
- lognormal-models
- var-methodologies
- historical-var
- mean-reversion
- contango
- vega-hedging
- modified-duration
- expected-loss
- forward-curve
- currency-swaps
- protective-puts
- probabilty-of-default
- curve-steepening
- curve-fitting
- gamma-hedging
- hedge-effectiveness
- roll-yield
- risk-premium
- spot-rates
- put-options
- affine-term-structure
- momentum
- curve-flattening
- basis-risk
- convexity
- hedge-strategies
- term-structure
- covered-calls
- swap-rate
- sofr
- ' exposure-at-default'
- stress-testing
- roll-over-risk
- ornstein-uhlenbeck
- rating-migration
- par-yield
- investment-analysis
- value-at-risk
- factor-models
- barbell-strategy
- convergence
- var-backtesting
- cross-hedging
- yield-curve-shocks
- strangles
- conditional-var
- dv01
- short-rate-models
- swap-spread
- price-yield-relationship
- credit-migration
- marking-to-market
- total-return-swaps
- libor
- credit-spreads
- multi-factor-models
- iron-condors
- financial-markets
- macaulay-duration
- static-hedging
- size-effect
- basis-swaps
- interest-rate-swaps
- futures-contracts
- apt
- bootstrap-method
- credit-default-swaps
title: Foreign Exchange Quoting Conventions
type: course-note
---
--



- Introduction to Derivative Markets]]
- Hedging%20[Key%20Rates%20O1s%20Durations%20and%20Hedging) Strategies with [Forwards]]
- Forward Exchange Rate Numerical Example]]
- Secondary Commodities]]
- Foreign Exchange Quoting Conventions
- Forward Contracts on Exchange Rates
- Forwards and Futures Notes]]
- Hedging Strategies with Forwards]]
- Financial Instruments/Lecture Notes/Teaching Note 1- Forward Rates Agreement/Interest Rates,  Carry Trades,  and Exchange Rate Movements]]
- Teaching Note 1Forward Rates Agreement
# Foreign Exchange Quoting Conventions
- The base currency is the first currency shown in a foreign exchange quotation. The second currency in the quotation is called the quote currency,  or counter currency.
- Foreign exchange quotations are always presented as a currency pair in the following format: XXX/YYY e.g. EUR/USD. This is because,  when you exchange currency,  you’re selling one currency and buying another.
- The exchange rate represents how much quote currency you need to sell in order to buy one unit of the base currency.
Currency Forward](Currency%20Forward.md)
### FX SPOT RATE$S_0$
- The FX spot rate, $S_0 = FOR-DOM$,  represents the number of units of domestic currency needed to buy one unit of foreign currency at time 0.
- A notional of$N$units of foreign currency is equal to$N*S_t$units of domestic currency
- The domestic currency is also referred to as the numeraire currency and the foreign one as the base currency
### FX OUTRIGHT FORWARD RATE$F(0, T)$
1. The forward exchange rate contract trades at time$t=0$at zero cost and leads to an exchange of notionals at time$T$at the pre-specified outright forward rate$F(0, T)$.
1. At time$t$,  the foreign notional amount$N$is exchanged against an amount of$N*F(0, T)$domestic currency units. 
	1. - For example,  1, 000, 000 EUR may be exchanged against 1, 390, 000 USD assuming an outright forward rate of 1.3900 EUR-USD. 
1. The outright forward is related to the FX spot rate via the spot–interest rate parity, $$F(0, T) = S \cdot e^{(r_{DOM}-r_{FOR})\tau}$$

where

- $r_{FOR}$is the foreign interest rate (continuously compounded)
- $r_{DOM}$is the domestic interest rate (continuously compounded)
- $\tau$is the time to maturity,  equal to$T - t$
## FX FORWARD VALUE

- At inception,  an outright forward contract has a value of zero. 
- Thereafter,  when foreign exchange rates and/or interest rates change,  the value of the forward contract is no longer zero,  but is worth$$v_f(t, T) = e^{-r_{DOM}\tau}(F(t, T) - K) = S_t e^{-r_{FOR}\tau} - Ke^{-r_{DOM}\tau}$$

for a pre-specified exchange rate$K$. 

- This is the forward contract value in domestic currency units,  marked to the market at time$t$. 
- As stated previously,  setting$K = F(0,  T)$yields a zero-cost contract.

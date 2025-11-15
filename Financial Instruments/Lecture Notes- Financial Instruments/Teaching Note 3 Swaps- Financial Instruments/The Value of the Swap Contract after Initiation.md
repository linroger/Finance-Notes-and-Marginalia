---
academic_level: graduate
aliases:
- Currency Swap
- Eurodollar Futures
- FX Swap
- Hedging Strategy
- Swap Value
enhanced: true
enhancement_date: '2025-11-06'
enhancement_id: batch09-000145
key_concepts:
- Currency swaps and foreign exchange risk management
- Heath-Jarrow-Morton (HJM) and forward rate dynamics
- Financial modeling and quantitative analysis
- Risk management and portfolio optimization
- Derivatives pricing and hedging strategies
- Market risk measurement and control
- Forward Rates and Curve Construction Methods
- Swap Market Mechanisms and Pricing
- Risk Measurement and VaR Backtesting
- Contango, Backwardation, and Roll Yield
- Ornstein-Uhlenbeck Process in Finance
- Futures and Forward Contracts in Financial Markets
- Yield Curve Analysis and Bond Valuation
- Value at Risk and Expected Shortfall
- Vasicek Interest Rate Model and Mean Reversion
- Hedge Strategies and Basis Risk Management
- Short Rate Models and Term Structure Dynamics
- Fama-French Factors and Style Analysis
- Factor Models and Asset Pricing
- Term Structure of Interest Rates and Yield Curves
- Interest Rate Swaps and Currency Swap Structures
- Stress Testing and Extreme Value Analysis
- Credit Default Swaps and Credit Risk Transfer
- Arbitrage Pricing Theory and Multi-Factor Models
professional_application: theoreti
status: active
tags:
- asset-allocation
- collateral-rates
- credit-rating
- cross-currency-swap
- currency-hedging
- currency-markets
- exchange-rates
- foreign-exchange
- forward-contracts
- forward-curve
- forward-pricing
- forward-rate-agreement
- forward-rate-dynamics
- future-rates
- futures
- spot-rates
- affine-term-structure
- hull-white
- cir-model
- yield-curve-shocks
- momentum
- expected-shortfall
- basis-risk
- parametric-var
- conditional-var
- extreme-value-theory
- book-to-market
- var-methodologies
- historical-var
- mean-reversion
- lognormal-models
- contango
- backwardation
- term-structure
- sofr
- swap-rate
- style-analysis
- short-rate-models
- swap-spread
- yield-curve
- stress-testing
- ornstein-uhlenbeck
- par-yield
- clearinghouse
- investment-analysis
- risk-premium
- marking-to-market
- interpolation
- value-at-risk
- total-return-swaps
- libor
- currency-swaps
- overnight-indexed-swaps
- arbitrage-pricing-theory
- multi-factor-models
- hedge-ratio
- fama-french
- market-price-of-risk
- financial-markets
- size-effect
- factor-models
- basis-swaps
- value-factor
- interest-rate-swaps
- vasicek-model
- curve-fitting
- monte-carlo-var
- convergence
- var-backtesting
- futures-contracts
- roll-yield
- apt
- bootstrap-method
- credit-default-swaps
- forward-rates
type: course-note
---
--



**Teaching Note 3 SwapsFinancial Instruments**
	- Forward Rates Agreement
	- Overnight Index Swaps (OIS).md)
	- Swaps Types
	- Teaching Note 3 SwapsFinancial Instruments
	- Swap Contract after Initiation]]

PSET 3 Financial Instruments

## DETERMINING THE VALUE POST-INITIATION
+ What is the value of a swap contract *after* initiation?
  + Let today be$t$,$K$be the swap rate of the existing swap, and$T_1, T_2, …, T_n$be the remaining payment periods.
  + Use the same logic as for forward and ask: What would the firm have to pay to get out of the position?
  + As before, using a sequence of forwards to get out of the position gives
$$V^{swap}_t = PV \text{ of swap + reverse forward cash flows } = e^{-r_s(T_{1}-t)} \times (K - F_{1,T_1}) + e^{-r_s(T_{2}-t)} \times (K - F_{1,T_2}) + … + e^{-r_s(T_{n}-t)} \times (K - F_{1,T_n})$$

### OBTAINING THE SWAP VALUE FORMULA

+ The swap value formula can be expressed as:$$V^{swap}_t = \sum_{i=1}^n e^{-r_s(T_{i}-t)} \times (K - F_{1,T_i})$$
  + By substituting the value of$F_{1,T_i}$with$S_t$$$V^{swap}*t = K \times \left(\sum*{i=1}^n e^{-r_s(T_{i}-t)} \right) - S_t \times \left(\sum_{i=1}^n e^{-r_e(T_{i}-t)} \right)$$

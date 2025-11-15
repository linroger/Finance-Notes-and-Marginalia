---
academic_level: graduate
aliases:
- Citi Guide
- Forward Foreign Exchange
- LTFX
- POS
- Swap Pricing
- Cross Currency Swaps
cssclasses: academia
enhanced: true
enhancement_date: '2025-11-06'
enhancement_id: batch09-000129
key_concepts:
- Options Greeks and sensitivity analysis for risk management
- Interest rate swaps and fixed income derivatives
- Currency swaps and foreign exchange risk management
- Heath-Jarrow-Morton (HJM) and forward rate dynamics
- LIBOR market model and multi-curve framework
- Basel accords and banking regulation framework
- Arbitrage opportunities and no-arbitrage pricing
- Risk preference theory and utility functions
- Yield Curve Analysis and Bond Valuation
- Value at Risk and Expected Shortfall
- Credit Risk Management and Default Probability
- Expected Loss and Loss Given Default Models
- Forward Rates and Curve Construction Methods
- Swap Market Mechanisms and Pricing
- Delta, Gamma, and Vega Hedging Techniques
- Stress Testing and Extreme Value Analysis
- Credit Default Swaps and Credit Risk Transfer
- Fama-French Factors and Style Analysis
- Risk Measurement and VaR Backtesting
- Contango, Backwardation, and Roll Yield
- Futures and Forward Contracts in Financial Markets
- Bond Pricing and Yield to Maturity Analysis
- Fixed Income Securities and Credit Quality
- Hedge Strategies and Basis Risk Management
- Dynamic vs Static Hedging in Practice
- Interest Rate Swaps and Currency Swap Structures
- Term Structure of Interest Rates and Yield Curves
- Credit Spreads and Rating Migration Analysis
- Hedging Strategies and Risk Mitigation
- Factor Models and Asset Pricing
- Government and Corporate Bond Markets
- Arbitrage Pricing Theory and Multi-Factor Models
professional_application: theoreti
status: active
tags:
- arbitrage-free-models
- arbitrage-opportunity
- asset-allocation
- banking-regulation
- basel-accord
- basis-risk
- basis-swap
- capital-adequacy
- capital-budgeting
- caplet
- credit-rating
- cross-currency-swap
- currency-hedging
- currency-markets
- delta-hedging
- expected-shortfall
- extreme-value-theory
- book-to-market
- backwardation
- volatility-analysis
- style-analysis
- bond-pricing
- corporate-bonds
- yield-curve
- unexpected-loss
- clearinghouse
- interpolation
- overnight-indexed-swaps
- arbitrage-pricing-theory
- hedge-ratio
- loss-given-default
- value-factor
- dirty-price
- dynamic-hedging
- monte-carlo-var
- coupon-bonds
- forward-contracts
- yield-to-maturity
- fama-french
- forward-rates
- recovery-rate
- zero-coupon-bonds
- parametric-var
- var-methodologies
- historical-var
- contango
- vega-hedging
- expected-loss
- forward-curve
- currency-swaps
- government-bonds
- probabilty-of-default
- curve-fitting
- gamma-hedging
- hedge-effectiveness
- credit-default-swaps
- roll-yield
- spot-rates
- momentum
- hedge-strategies
- term-structure
- sofr
- swap-rate
- ' exposure-at-default'
- stress-testing
- roll-over-risk
- rating-migration
- par-yield
- value-at-risk
- factor-models
- risk-management
- convergence
- var-backtesting
- cross-hedging
- clean-price
- yield-curve-shocks
- conditional-var
- fixed-income
- swap-spread
- credit-migration
- default-probability
- marking-to-market
- total-return-swaps
- libor
- credit-spreads
- multi-factor-models
- static-hedging
- size-effect
- basis-swaps
- interest-rate-swaps
- futures-contracts
- apt
- bootstrap-method
- current-yield
type: primer
---
--



# Citi: Guide to Swaps

## Swap Pricing: Discounted Cashflows

!500

## Common Swap Structures

- **Basis swap** (i.e., floating/floating) is one of the basic building blocks in fixed/fixed and fixed/floating Cross Currency Swaps (CCS).
- A basis swap in this context is defined as the exchange of LIBORs in two different currencies with both initial and final exchange of principal.
- Cost of a basis swap is quoted against USD LIBOR flat (e.g., USD LIBOR vs YEN LIBOR 17 bps) and is driven by demand and supply.
- Example: ABC company has 3-year funding in JPY and is required to hedge exchange rate exposure created by this foreign currency debt.

!500

## Fixed/Fixed Cross Currency Swap

!500

!500

## Principal-Only Swap (POS)

- Compared to a full cross currency swap, a Principal-Only Swap (POS) costs less because a POS does not provide a hedge against exchange rate risks on coupon payments.
- Consider a 3-year USD/JPY swap:
  - At maturity, company receives JPY principal and pays USD principal at current spot rate (in fact can be any agreed exchange rate).
  - Same as a long-dated forward contract of the company buying JPY and selling USD at current spot rate.
  - Due to the interest rate differential between JPY and USD, forward USD/JPY exchange rate is lower than spot rate (i.e., JPY at premium).
  - The contract to buy JPY/sell USD forward at current spot rate has a positive value to the Company.
  - As a compensation to Citibank (i.e., to make NPV = 0), the Company will need to pay a periodic coupon (either in USD or JPY) to Citibank.

!500

!500

## Coupon-Only Swap

- Consider a 3-year USD/JPY swap with only coupon exchanges.
- There are no principal exchanges. If the USD fixed rate is known, we can solve for the JPY fixed rate.

!500

## Long-Dated Foreign Exchange (LTFX)

- A Long-Dated Foreign Exchange (LTFX) contract is a Zero Coupon Currency & Interest Rate Swap
- Instead of exchanging coupons, at the time of dealing, the Principal amount on one set of cashflows is set so that the NPV = 0.

!500

## Using Interest Rate Parity - Pricing Forward Foreign Exchange

!500

!500

!500

!500

Rather than using zero coupon rates, each currency's discount factors may be used:

**Short Cut:** Forward Rate = Spot × dfUSD/dfJPY = 105 × 0.9420 / 0.9975

!500

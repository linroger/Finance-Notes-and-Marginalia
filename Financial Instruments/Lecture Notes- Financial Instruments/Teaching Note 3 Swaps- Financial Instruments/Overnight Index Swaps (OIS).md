---
academic_level: graduate
aliases:
- Is
- OIS
cssclasses:
- academia
enhanced: true
enhancement_date: '2025-11-06'
enhancement_id: batch09-000142
key_concepts:
- Black-Scholes option pricing model and continuous-time finance
- Options Greeks and sensitivity analysis for risk management
- Convexity adjustments and yield curve sensitivity
- Discounted cash flow (DCF) valuation methodology
- Weighted Average Cost of Capital (WACC) and firm valuation
- Bootstrap methods and yield curve construction
- Heath-Jarrow-Morton (HJM) and forward rate dynamics
- SOFR benchmarks and risk-free rate transition
- Risk preference theory and utility functions
- Sensitivity analysis and Greeks calculation
- 'Valuation Methods: DCF, Comps, and Precedents'
- Yield Curve Analysis and Bond Valuation
- Value at Risk and Expected Shortfall
- Vasicek Interest Rate Model and Mean Reversion
- Short Rate Models and Term Structure Dynamics
- Company Valuation and Multiple Analysis
- Forward Rates and Curve Construction Methods
- Swap Market Mechanisms and Pricing
- Comparable Company Analysis and Trading Multiples
- 'Greeks: Delta, Gamma, Theta, and Vega Hedging'
- Ornstein-Uhlenbeck Process in Finance
- Options Trading Strategies and Risk Management
- Stress Testing and Extreme Value Analysis
- Credit Default Swaps and Credit Risk Transfer
- Fama-French Factors and Style Analysis
- Risk Measurement and VaR Backtesting
- Contango, Backwardation, and Roll Yield
- Futures and Forward Contracts in Financial Markets
- Bond Pricing and Yield to Maturity Analysis
- Fixed Income Securities and Credit Quality
- Hedge Strategies and Basis Risk Management
- Interest Rate Swaps and Currency Swap Structures
- Private Equity Investment Returns and Value Creation
- Term Structure of Interest Rates and Yield Curves
- Option Valuation and Exercise Strategies
- LBO Valuation and Debt Capacity Analysis
- Factor Models and Asset Pricing
- Leveraged Buyouts and Private Equity Transactions
- Government and Corporate Bond Markets
- Arbitrage Pricing Theory and Multi-Factor Models
professional_application: theoreti
status: active
tags:
- benchmark-reform
- binomial-model
- black-scholes-model
- bootstrap-method
- capital-structure
- caplet
- cash-flow-modeling
- collateral-rates
- continuous-time-pricing
- convexity-adjustment
- cost-of-capital
- credit-rating
- dcf-valuation
- delta-hedging
- derivatives
- leveraged-buyout
- hull-white
- call-options
- cir-model
- butterfly-spreads
- dcf-analysis
- expected-shortfall
- straddles
- extreme-value-theory
- book-to-market
- backwardation
- style-analysis
- leverage-ratio
- bond-pricing
- option-strategies
- corporate-bonds
- yield-curve
- clearinghouse
- interpolation
- overnight-indexed-swaps
- arbitrage-pricing-theory
- hedge-ratio
- private-equity
- market-price-of-risk
- value-factor
- vasicek-model
- dirty-price
- monte-carlo-var
- options-trading
- coupon-bonds
- forward-contracts
- yield-to-maturity
- fama-french
- forward-rates
- price-to-earnings
- zero-coupon-bonds
- parametric-var
- lognormal-models
- var-methodologies
- historical-var
- mean-reversion
- contango
- debt-capacity
- forward-curve
- currency-swaps
- investment-return
- protective-puts
- government-bonds
- curve-fitting
- credit-default-swaps
- roll-yield
- risk-premium
- spot-rates
- put-options
- affine-term-structure
- equity-kickers
- lbo-valuation
- momentum
- basis-risk
- term-structure
- covered-calls
- swap-rate
- sofr
- stress-testing
- ornstein-uhlenbeck
- par-yield
- comparable-analysis
- investment-analysis
- economic-value-added
- value-at-risk
- bootstrap-strategy
- management-buyout
- factor-models
- convergence
- var-backtesting
- sum-of-parts
- clean-price
- yield-curve-shocks
- strangles
- conditional-var
- fixed-income
- short-rate-models
- swap-spread
- marking-to-market
- total-return-swaps
- libor
- multi-factor-models
- trading-multiples
- iron-condors
- financial-markets
- size-effect
- basis-swaps
- precedent-transactions
- interest-rate-swaps
- ipo-valuation
- market-multiple
- futures-contracts
- apt
- current-yield
title: Overnight Index Swaps (Is)
type: course-note
---
--



**Teaching Note 3 SwapsFinancial Instruments**
	- Forward Rates Agreement
	- Overnight Index Swaps (OIS)
	- Swaps Types
	- Teaching Note 3 SwapsFinancial Instruments
	- Swap Contract after Initiation]]

# Overnight Index Swaps (Is)
## FUNDAMENTALS OF Is
- In an Is,  two counterparties agree to exchange fixed for floating payments,  where the floating payment is tied to the cumulative return from an overnight rate.
	- Federal funds rate,  SOFR in US.
	- Europe: short-term rate (€STR),  (formerly Euro OverNight Index Average (EONIA) rate).
## FLOATING RATE PAYMENT CALCULATION

- Given a notional$N$,  the floating rate payment at time$T_i$is:$$CF(T_i) = N \left[\left(\prod_{j=1}^{n_i} (1 + r_{t_j}\delta) \right) - 1 \right]$$
- Where$\delta$is the daily interval,  $r_t$is the reference (annualized) overnight rate,  and$n_i$is the number of days between reset periods.
- The day count convention is normally Actual/360.
### IN THE CONTINUOUS TIME LIMIT

- In the continuous time limit ($\delta \rightarrow 0$),  we have:$$CF(T_i) = N \left(e^{\int_{0}^{T_i} r_u \,    du} - 1 \right)$$
#### IS CHARACTERISTICS
- Is with maturity less than 1 year have only one payment at the maturity.
- Is with longer maturities have normally quarterly payments.

## VALUE OF IS

- The value of Is is the difference between the floating leg and the fixed leg:$$V^{OIS}_t = V^{Floating}_t - V^{Fixed}_t$$
- ## Floating Leg
- At reset dates,  and assuming the payment of a principal at maturity of the swap,  the value of the floating leg is par.
- Indeed,  investing the notional$N$in the overnight index daily gives at$T_i$:$$N \prod_{j=1}^{n_i} (1 + r_{t_j}\delta) = CF(T_i) + N$$
- We can replicate the floating payments,  plus a residual of notional at maturity$T_n$,  with an investment$N$at time 0.
- It follows:$$V^{Floating}_{0} = N$$

## FIXED LEG

- Given a proper discount function$Z^{OIS}(0,    T_i)$,  we obtain:$$V^{Fixed}_{0} = N c \Delta \sum_{i=1}^{n} Z^{OIS}(0,    T_i) + N Z^{OIS}(0,    T_n)$$

## VALUATION AT INCEPTION
- The value of the contract at inception is zero,  $V^{OIS}_0 = 0$.
- It follows that:$$V^{OIS}_{0} = V^{Floating}_{0} - V^{Fixed}_{0} = 0$$

## SWAP RATE CALCULATION

- This equation implies that the swap rate$c$can be computed from:$$1 = c \Delta \sum_{i=1}^{n} Z^{OIS}(0,    T_i) + Z^{OIS}(0,    T_n)$$- Which gives the coupon rate$c$for a swap with maturity$T_n$:$$c(T_n) = \frac{1 - Z^{OIS}(0,    T_n)}{\Delta \sum_{i=1}^{n} Z^{OIS}(0,    T_i)}$$
- We emphasize that the coupon rate$c$is for a swap with maturity$T_n$.
## IS COUPON RATES AND ZERO-COUPON CURVE

- Given the Is coupon rates$c(T_i)$for every maturity$T_i$,  we can bootstrap the Is zero-coupon curve from the relation:$$Z^{OIS}(0,    T_i) = \frac{1 - c(T_i)}{1 + c(T_i) \Delta \sum_{j=1}^{i-1} Z^{OIS}(0,    T_j)}$$
- Recalling that Is with maturity less than or equal to 1 year generally have only one payment.

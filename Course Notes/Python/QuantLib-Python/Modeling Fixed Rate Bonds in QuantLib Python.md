---
academic_level: graduate
aliases:
- Bond Modeling
- QuantLib Example
description: This post will walk through an example of modeling fixed rate bonds using
  QuantLib Python.
enhanced: true
enhancement_date: '2025-11-06'
enhancement_id: batch09-000049
key_concepts:
- Black-Scholes option pricing model and continuous-time finance
- Options Greeks and sensitivity analysis for risk management
- Duration analysis and interest rate risk management
- Convexity adjustments and yield curve sensitivity
- Discounted cash flow (DCF) valuation methodology
- Weighted Average Cost of Capital (WACC) and firm valuation
- Interest rate swaps and fixed income derivatives
- Value at Risk (VaR) and tail risk measurement
- Expected shortfall and coherent risk measures
- QuantLib library and quantitative finance implementation
- Risk preference theory and utility functions
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
- Forward Curves and Roll Strategies
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
- Term Structure of Interest Rates and Yield Curves
- Seasonality and Convenience Yield
- Commodity Markets and Energy Derivatives
- Option Valuation and Exercise Strategies
- Factor Models and Asset Pricing
- Government and Corporate Bond Markets
- Arbitrage Pricing Theory and Multi-Factor Models
professional_application: theoreti
source: https://gouthamanbalaraman.com/blog/quantlib-bond-modeling.html
status: active
tags:
- binomial-model
- black-scholes-model
- capital-budgeting
- capital-structure
- caplet
- cash-flow-modeling
- coherent-risk-measure
- commodity-derivatives
- commodity-futures
- conditional-var
- continuous-time-pricing
- convexity-adjustment
- cost-of-capital
- credit-rating
- crude-oil
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
- energy-derivatives
- style-analysis
- bond-pricing
- option-strategies
- corporate-bonds
- yield-curve
- clearinghouse
- interpolation
- overnight-indexed-swaps
- arbitrage-pricing-theory
- hedge-ratio
- market-price-of-risk
- roll-strategies
- value-factor
- vasicek-model
- dirty-price
- forward-curves
- monte-carlo-var
- options-trading
- coupon-bonds
- commodity-trading
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
- quantitative-finance
- forward-curve
- currency-swaps
- protective-puts
- government-bonds
- curve-fitting
- credit-default-swaps
- storage-costs
- roll-yield
- risk-premium
- spot-rates
- put-options
- affine-term-structure
- momentum
- basis-risk
- term-structure
- covered-calls
- swap-rate
- sofr
- stress-testing
- mathematical-finance
- ornstein-uhlenbeck
- par-yield
- comparable-analysis
- investment-analysis
- economic-value-added
- value-at-risk
- metals-trading
- factor-models
- convenience-yield
- agricultural-commodities
- convergence
- var-backtesting
- sum-of-parts
- seasonality
- clean-price
- yield-curve-shocks
- strangles
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
- bootstrap-method
- current-yield
title: Modeling Fixed Rate Bonds in QuantLib Python
type: note
---
--



# Modeling Fixed Rate Bonds in QuantLib Python

This post will walk through an example of modeling fixed rate bonds using QuantLib Python.

*Visit here for other QuantLib Python examples](http://gouthamanbalaraman.com/blog/quantlib-python-tutorials-with-examples.html). If you found these posts useful,  please take a minute by providing some feedback.*

Let's consider a hypothetical bond with a par value of 100,  that pays 6% coupon semi-annually issued on January 15th,  2015 and set to mature on January 15th,  2016. The bond will pay a coupon on July 15th,  2015 and January 15th,  2016. The par amount of 100 will also be paid on the January 15th,  2016.

To make things simpler,  lets assume that we know the spot rates of the treasury as of January 15th,  2015. The annualized spot rates are 0.5% for 6 months and 0.7% for 1 year point. Lets calculate the fair value of this bond.
```latex
>>> 3/pow(1+0.005,  0.5) + (100 + 3)/(1+0.007)
105.27653992490681
```

Lets calculate the same thing using QuantLib.
```latex
>>> import QuantLib as ql
>>> todaysDate = ql.Date(15,  1,  2015)
>>> ql.Settings.instance().evaluationDate = todaysDate
>>> spotDates = [ql.Date(15,  1,  2015),  ql.Date(15,  7,  2015),  ql.Date(15,  1,  2016)]
>>> spotRates = [0.0,  0.005,  0.007]
>>> dayCount = ql.Thirty360()
>>> calendar = ql.UnitedStates()
>>> interpolation = ql.Linear()
>>> compounding = ql.Compounded
>>> compoundingFrequency = ql.Annual
>>> spotCurve = ql.ZeroCurve(spotDates,  spotRates,  dayCount,  calendar,  interpolation, 
                             compounding,  compoundingFrequency)
>>> spotCurveHandle = ql.YieldTermStructureHandle(spotCurve)
```

So far we have created the term structure and the variables are rather self explanatory. Now lets construct the fixed rate bond.
```latex
>>> issueDate = ql.Date(15,  1,  2015)
>>> maturityDate = ql.Date(15,  1,  2016)
>>> tenor = ql.Period(ql.Semiannual)
>>> calendar = ql.UnitedStates()
>>> bussinessConvention = ql.Unadjusted
>>> dateGeneration = ql.DateGeneration.Backward
>>> monthEnd = False
>>> schedule = ql.Schedule (issueDate,  maturityDate,  tenor,  calendar,  bussinessConvention, 
                            bussinessConvention ,  dateGeneration,  monthEnd)
>>> list(schedule)
[Date(15,  1,  12015),  Date(15, 7, 2015),  Date(15, 1, 2016)]

# Modeling Fixed Rate Bonds in QuantLib Python
>>> dayCount = ql.Thirty360()
>>> couponRate = 0.\1
>>> coupons = [couponRate]

# Now lets construct the FixedRateBond
>>> settlementDays = 0
>>> faceValue = 100
>>> fixedRateBond = ql.FixedRateBond(settlementDays,  faceValue,  schedule,  coupons,  dayCount)

# create a bond engine with the term structure as input;
# set the bond to use this bond engine
>>> bondEngine = ql.DiscountingBondEngine(spotCurveHandle)
>>> fixedRateBond.setPricingEngine(bondEngine)

# Finally the price
>>> fixedRateBond.NPV()
105.27653992490683
```

Voila!

Download the modeling bonds ipython notebook.

   python   finance   quantlib](http://gouthamanbalaraman.com/tag/quantlib.html)

---

**Related Post**

- QuantLib Python Tutorials With Examples](http://gouthamanbalaraman.com/blog/quantlib-python-tutorials-with-examples.html)
- Modeling Vanilla Interest Rate Swaps Using [QuantLib Python](http://gouthamanbalaraman.com/blog/interest-rate-swap-quantlib-python.html)
- Valuing Options on [Commodity Futures Using QuantLib Python](http://gouthamanbalaraman.com/blog/value-options-commodity-futures-black-formula-quantlib-python.html)
- Short [Interest Rate Model Calibration in QuantLib Python](http://gouthamanbalaraman.com/blog/short-interest-rate-model-calibration-quantlib.html)
- Announcing qtk for [QuantLib Python](http://gouthamanbalaraman.com/blog/announcing-qtk-quantlib-python.html)

---

 !500
I am Goutham Balaraman,  and I explore topics in quantitative finance,  programming,  and data science. You can follow me @gsbalaraman.

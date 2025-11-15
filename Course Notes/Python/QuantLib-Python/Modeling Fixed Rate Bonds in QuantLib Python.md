---
aliases:
- Bond Modeling
- QuantLib Example
description: This post will walk through an example of modeling fixed rate bonds using
  QuantLib Python.
enhanced: true
enhancement_date: '2025-11-06'
enhancement_id: batch03-9e405a
key_concepts:
- Carry trades and momentum in FX markets
- Term structure of interest rates and yield curve shapes
- Sovereign risk assessment and country analysis
- Mean-variance optimization and the efficient frontier
- Extreme value theory and tail risk modeling
- Single-name vs. index CDS trading
- Credit risk modeling and default probability estimation
- maturity date in CDS
- Commodity markets and pricing dynamics
- Risk budgeting and portfolio construction techniques
- Expectations hypothesis and liquidity preference theory
- QuantLib Python modeling
- Historical simulation vs. parametric VaR models
- Spot rates
- Yield curve fitting and interpolation methods
- Credit spread decomposition and hazard rates
- Fixed rate bonds
- CDS clearing and central counterparties
- DV01 calculation and interest rate risk hedging
- Coupon payments
- forward commitments and hedging
- Spot rates vs. forward rates modeling
- CDS-Bond basis and arbitrrage opportunities
- Swap spread and credit risk considerations
- Monte Carlo integration and variance reduction
- GARCH models and volatility forecasting
- Deposit insurance and systemic risk prevention
- Mathematical Finance
- Monte Carlo VaR for complex portfolios
- Bond fair value
- Stress testing and scenario analysis
- Fixed-for-floating swap cash flows and valuation
- Currency risk management and hedging
- Forward rates and interest rate parity
- Control variates and importance sampling techniques
- Value at Risk (VaR) methodologies and backtesting
- Risk-neutral pricing methodology for derivative securities
- Case Study
- Operational risk quantification and modeling
- Exchange rate determination and PPP theory
- Arbitrage opportunities and risk-free profit extraction
- Expected Shortfall and coherent risk measures
- Interest rate swap pricing and valuation
- interest rate and currency derivatives
- Credit default swap pricing and risk-neutral probabilities
- Bank liquidity ratios and funding risk management
- Variance swaps and volatility trading strategies
- fair value measurement and hierarchy
- par value in CDS settlement
- Value-at-Risk calculation using historical simulation
- Credit risk migration matrices and rating transition
- Credit risk modeling and portfolio correlation analysis
- Backtesting procedures for risk models
- Credit risk assessment and loan portfolio management
- Parallel and non-parallel shifts in the yield curve
- Liquidity risk measurement and management
- Cross-currency basis swaps and funding
- Systemic risk indicators and early warning systems
- Currency markets and foreign exchange trading
source: https://gouthamanbalaraman.com/blog/quantlib-bond-modeling.html
tags:
- financial-analysis
- yield-curve
- commodities
- credit-default-swaps
- garch-models
- coupon_bond
- interest-rate-swaps
- mathematical-finance
- financial-modeling
- case-study
- value-at-risk
- exchange-rates
- credit-risk
- quantitative-implementation
- term_structure
- duration-convexity
- solution
- treasury-bonds
- fixed_rate_bond
- stress-testing
- liquidity-risk
- systemic-risk
- exotic-options
- deposit-insurance
- quantitative-finance
- dcf-valuation
- quantlib_python
- expected-shortfall
- operational-risk
- bond_valuation
- monte-carlo
- term-structure
title: Modeling Fixed Rate Bonds in QuantLib Python
---

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

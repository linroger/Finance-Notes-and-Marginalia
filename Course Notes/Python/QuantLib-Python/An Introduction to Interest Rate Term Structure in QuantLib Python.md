---
academic_level: graduate
aliases:
- Interest Rate Term Structure
- QuantLib Python
- Yield Curve Bootstrapping
description: This post will walk through the basics of bootstrapping yield curve in
  QuantLib Python.
enhanced: true
enhancement_date: '2025-11-06'
enhancement_id: batch09-000043
key_concepts:
- Duration analysis and interest rate risk management
- Convexity adjustments and yield curve sensitivity
- Discounted cash flow (DCF) valuation methodology
- Weighted Average Cost of Capital (WACC) and firm valuation
- Bootstrap methods and yield curve construction
- QuantLib library and quantitative finance implementation
- Risk preference theory and utility functions
- Financial modeling and quantitative analysis
- Risk management and portfolio optimization
- Derivatives pricing and hedging strategies
- Market risk measurement and control
- 'Valuation Methods: DCF, Comps, and Precedents'
- Yield Curve Analysis and Bond Valuation
- Value at Risk and Expected Shortfall
- Vasicek Interest Rate Model and Mean Reversion
- Short Rate Models and Term Structure Dynamics
- Company Valuation and Multiple Analysis
- Forward Rates and Curve Construction Methods
- Comparable Company Analysis and Trading Multiples
- 'Greeks: Delta, Gamma, Theta, and Vega Hedging'
- Ornstein-Uhlenbeck Process in Finance
- Options Trading Strategies and Risk Management
- Stress Testing and Extreme Value Analysis
- Risk Measurement and VaR Backtesting
- Fixed Income Securities and Credit Quality
- Bond Pricing and Yield to Maturity Analysis
- Private Equity Investment Returns and Value Creation
- Term Structure of Interest Rates and Yield Curves
- Option Valuation and Exercise Strategies
- LBO Valuation and Debt Capacity Analysis
- Leveraged Buyouts and Private Equity Transactions
- Government and Corporate Bond Markets
professional_application: theoreti
source: https://gouthamanbalaraman.com/blog/quantlib-term-structure-bootstrap-yield-curve.html
status: active
tags:
- asset-allocation
- bootstrap-method
- capital-structure
- caplet
- cash-flow-modeling
- convexity-adjustment
- cost-of-capital
- credit-rating
- dcf-valuation
- derivatives-pricing
- discount-factor-curve
- discounted-cash-flow
- duration-analysis
- financial-modeling
- fixed-income-sensitivity
- spot-rates
- put-options
- leveraged-buyout
- affine-term-structure
- hull-white
- sum-of-parts
- call-options
- zero-coupon-bonds
- clean-price
- yield-curve-shocks
- cir-model
- lbo-valuation
- butterfly-spreads
- dcf-analysis
- strangles
- price-to-earnings
- expected-shortfall
- straddles
- parametric-var
- conditional-var
- extreme-value-theory
- lognormal-models
- fixed-income
- var-methodologies
- historical-var
- mean-reversion
- term-structure
- covered-calls
- short-rate-models
- leverage-ratio
- bond-pricing
- option-strategies
- corporate-bonds
- yield-curve
- stress-testing
- mathematical-finance
- ornstein-uhlenbeck
- debt-capacity
- par-yield
- comparable-analysis
- investment-analysis
- economic-value-added
- quantitative-finance
- risk-premium
- interpolation
- forward-curve
- value-at-risk
- trading-multiples
- bootstrap-strategy
- private-equity
- investment-return
- iron-condors
- protective-puts
- government-bonds
- market-price-of-risk
- management-buyout
- financial-markets
- precedent-transactions
- vasicek-model
- dirty-price
- curve-fitting
- ipo-valuation
- equity-kickers
- monte-carlo-var
- var-backtesting
- options-trading
- coupon-bonds
- market-multiple
- current-yield
- yield-to-maturity
- forward-rates
title: An Introduction to Interest Rate Term Structure in QuantLib Python
type: note
---
--



# An Introduction to Interest Rate Term Structure in QuantLib Python

This post will walk through the basics of bootstrapping yield curve in QuantLib Python.

*Visit here for other QuantLib Python examples](http://gouthamanbalaraman.com/blog/quantlib-python-tutorials-with-examples.html). If you found these posts useful,  please take a minute by providing some feedback.*

Term structure is pivotal to pricing securities. One would need a YieldTermStructure object created in QuantLib to use with pricing engines. In an earlier post on modeling bonds using [QuantLib](https://gouthamanbalaraman.com/blog/quantlib-bond-modeling.html) we discussed how to use spot rates directly with bond pricing engine. Here in this post we will show how to bootstrap yield curve using QuantLib.

As usual lets import QuantLib and do some initialization.
```python
import QuantLib as ql

def print_curve(xlist,      ylist,      precision=3):
    """
    Method to print curve in a nice format
    """
    print "----------------------"
    print "Maturities\tCurve"
    print "----------------------"
    for x,     y in zip(xlist,      ylist):
        print x,     "\t\t",      round(y,      precision)
    print "----------------------"
```

The deposit rates and fixed rate bond rates are provided below. This example is based on Exhibit 5-5 given in Frank Fabozzi's Bond Markets,  Analysis and Strategies,  Sixth Edition.
```python
# An Introduction to Interest Rate Term Structure in QuantLib Python
depo_maturities = [ql.Period(6,     ql.Months),      ql.Period(12,      ql.Months)]
depo_rates = [5.25,      5.5]

# Bond rates
bond_maturities = [ql.Period(6*i,      ql.Months) for i in range(3,     21)]
bond_rates = [5.75,      6.0,      6.25,      6.5,      6.75,      6.80,      7.00,      7.1,      7.15,     
              7.2,      7.3,      7.35,      7.4,      7.5,      7.6,      7.6,      7.7,      7.8]

print_curve(depo_maturities+bond_maturities,      depo_rates+bond_rates)
```

Lets define some of the constants required for the rest of the objects needed below.
```python
# some constants and conventions
# here we just assume for the sake of example
# that some of the constants are the same for
# depo rates and bond rates

calc_date = ql.Date(15,      1,      2015)
ql.Settings.instance().evaluationDate = calc_date

calendar = ql.UnitedStates()
bussiness_convention = ql.Unadjusted
day_count = ql.Thirty360()
end_of_month = True
settlement_days = 0
face_amount = 100
coupon_frequency = ql.Period(ql.Semiannual)
settlement_days = 0
```

The basic idea of bootstrapping using QuantLib is to use the deposit rates and bond rates to create individual helpers. Then use the combination of the two helpers to construct the yield curve.
```python
# create deposit rate helpers from depo_rates
depo_helpers = [ql.DepositRateHelper(ql.QuoteHandle(ql.SimpleQuote(r/100.0)),     
                                     m,     
                                     settlement_days,     
                                     calendar,     
                                     bussiness_convention,     
                                     end_of_month,     
                                     day_count )
                for r,      m in zip(depo_rates,      depo_maturities)]
```

The rest of the points are coupon bonds. We assume that the YTM given for the bonds are all par rates. So we have bonds with coupon rate same as the YTM.
```python
# create fixed rate bond helpers from fixed rate bonds
bond_helpers = []
for r,      m in zip(bond_rates,      bond_maturities):
    termination_date = calc_date + m
    schedule = ql.Schedule(calc_date,     
                   termination_date,     
                   coupon_frequency,     
                   calendar,     
                   bussiness_convention,     
                   bussiness_convention,     
                   ql.DateGeneration.Backward,     
                   end_of_month)

    helper = ql.FixedRateBondHelper(ql.QuoteHandle(ql.SimpleQuote(face_amount)),     
                                        settlement_days,     
                                        face_amount,     
                                        schedule,     
                                        [r/100.0],     
                                        day_count,     
                                        bussiness_convention,     
                                        )
    bond_helpers.append(helper)
```

The yield curve is constructed by putting the two helpers together.
```python
rate_helpers = depo_helpers + bond_helpers
yieldcurve = ql.PiecewiseLogCubicDiscount(calc_date,     
                             rate_helpers,     
                             day_count)
```

The spot rates is obtined from yieldcurve object using the zeroRate method.
```python
# get spot rates
spots = []
tenors = []
for d in yieldcurve.dates():
    yrs = day_count.yearFraction(calc_date,      d)
    compounding = ql.Compounded
    freq = ql.Semiannual
    zero_rate = yieldcurve.zeroRate(yrs,      compounding,      freq)
    tenors.append(yrs)
    eq_rate = zero_rate.equivalentRate(day_count,     
                                       compounding,     
                                       freq,     
                                       calc_date,     
                                       d).rate()
    spots.append(100*eq_rate)
```

The bootstrap curve looks as shown below:

 | Maturity | Spots | 
 | --- | --- | 
 | 0.0 | 0.0 | 
 | 0.5 | 5.25 | 
 | 1.0 | 5.426 | 
 | 1.5 | 5.761 | 
 | 2.0 | 6.02 | 
 | 2.5 | 6.283 | 
 | 3.0 | 6.55 | 
 | 3.5 | 6.822 | 
 | 4.0 | 6.87 | 
 | 4.5 | 7.095 | 
 | 5.0 | 7.205 | 
 | 5.5 | 7.257 | 
 | 6.0 | 7.31 | 
 | 6.5 | 7.429 | 
 | 7.0 | 7.485 | 
 | 7.5 | 7.543 | 
 | 8.0 | 7.671 | 
 | 8.5 | 7.802 | 
 | 9.0 | 7.791 | 
 | 9.5 | 7.929 | 
 | 10.0 | 8.072 | 

Once we have the spots,  the zero coupon curve can be directly constructed the next time as show in the bond [pricing example](https://gouthamanbalaraman.com/quantlib-bond-modeling.html). The yieldcurve.dates() and yieldcuve.zeroRate(…) methods would provide for the necessary rates as shown above.

   python   finance   quantlib](http://gouthamanbalaraman.com/tag/quantlib.html)

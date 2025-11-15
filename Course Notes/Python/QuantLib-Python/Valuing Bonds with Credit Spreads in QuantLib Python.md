---
aliases:
- Credit Spread Valuation
- QuantLib Example
description: Provides an example of valuing bonds with credit spreads using QuantLib
  Python. This post walks through an example of shifting the yield term structure.
enhanced: true
enhancement_date: '2025-11-06'
enhancement_id: batch03-2cdfce
key_concepts:
- Term structure of interest rates and yield curve shapes
- Sensitivity analysis in DCF models
- Duration and convexity analysis for bond portfolio management
- Shifting yield term structure
- Constructing yield curve
- Treasury Bonds
- Single-name vs. index CDS trading
- Collateralized Debt Obligations
- Valuing bonds with spreads
- Probability of default estimation from credit spreads
- Credit spread analysis and OAS methodology
- Expectations hypothesis and liquidity preference theory
- Discounted Cash Flow valuation methodology
- Solution
- Adding credit spreads
- Yield curve fitting and interpolation methods
- Credit spread decomposition and hazard rates
- Structural models of default and Merton formulation
- CDS clearing and central counterparties
- fixed income risk measurement
- Portfolio immunization strategies
- CDS-Bond basis and arbitrrage opportunities
- Swap spread and credit risk considerations
- Spot rates vs. forward rates modeling
- Mathematical Finance
- Credit default swap pricing and recovery assumptions
- Parallel yield curve shift
- 'Structured products: CDOs, CLOs, and credit derivatives'
- Key rate duration and curve risk
- Fixed-for-floating swap cash flows and valuation
- Synthetic credit derivatives and index trades
- Case Study
- Interest rate swap pricing and valuation
- Credit default swap pricing and risk-neutral probabilities
- Variance swaps and volatility trading strategies
- Free cash flow to equity and firm valuation
- Credit intermediation and information asymmetry
- Terminal value estimation and perpetuity growth
- Quantitative Implementation
- Credit risk migration matrices and rating transition
- Credit risk modeling and portfolio correlation analysis
- Credit risk assessment and loan portfolio management
- Parallel and non-parallel shifts in the yield curve
- Cross-currency basis swaps and funding
- Duration and convexity measures for bond portfolios
- Counterparty credit exposure measurement
- Price sensitivity to interest rate changes
- Modified duration vs. Macaulay duration
source: https://gouthamanbalaraman.com/blog/bonds-with-spreads-quantlib-python.html
tags:
- yield-curve
- credit-default-swaps
- credit-spreads
- collateralized-debt-obligations
- interest-rate-swaps
- mathematical-finance
- course-material
- credit_spreads
- financial-modeling
- case-study
- duration
- exchange-rates
- credit-risk
- yield_curve
- duration-convexity
- quantitative-implementation
- solution
- treasury-bonds
- treasury_yield
- corporate-bonds
- dcf-valuation
- quantlib_python
- bond_valuation
- term-structure
title: Valuing Bonds with Credit Spreads in QuantLib Python
---

# Valuing Bonds with Credit Spreads in QuantLib Python

Provides an example of valuing bonds with credit spreads using QuantLib Python. This post walks through an example of shifting the yield term structure.

*Visit here for other QuantLib Python examples](http://gouthamanbalaraman.com/blog/quantlib-python-tutorials-with-examples.html). If you found these posts useful,  please take a minute by providing some feedback.*

In an earlier example on pricing fixed rate bonds](http://gouthamanbalaraman.com/blog/quantlib-bond-modeling.html) I demonstrated how to construct and value bonds using the given yield curve. In this example,  let us take a look at valuing bonds with credit spreads. We will show how to add credit spreads to the give yield curve using different approaches.

As usual,  let us start by importing the QuantLib library and pick a valuation date and set the calculation instance evaluation date.
```python
import QuantLib as ql
calc_date = ql.Date(26,     7,     2016)
ql.Settings.instance().evaluationDate = calc_date
```

For simplicity,  let us imagine that the treasury yield curve is flat. This makes it easier to construct the yield curve easily. This also allows us to directly shock the yield curve,  and provides a validation for the more general treatment of shocks on yield curve.
```python
flat_rate = ql.SimpleQuote(0.0015)
rate_handle = ql.QuoteHandle(flat_rate)
day_count = ql.Actual360()
calendar = ql.UnitedStates()
ts_yield = ql.FlatForward(calc_date,     rate_handle,     day_count)
ts_handle = ql.YieldTermStructureHandle(ts_yield)
```

Now let us construct the bond itself. We do that by first constructing the schedule,  and then passing the schedule into the bond.
```python
issue_date = ql.Date(15,     7,     2016)
maturity_date = ql.Date(15,     7,     2021)
tenor = ql.Period(ql.Semiannual)
calendar = ql.UnitedStates()
bussiness_convention = ql.Unadjusted
date_generation = ql.DateGeneration.Backward
month_end = False
schedule = ql.Schedule (issue_date,     maturity_date,     
                        tenor,     calendar,     
                        bussiness_convention,    
                        bussiness_convention,     
                        date_generation,     
                        month_end)
```
```python
settlement_days = 2
day_count = ql.Thirty360()
coupon_rate = 0.\1
coupons = [coupon_rate]

# Valuing Bonds with Credit Spreads in QuantLib Python
settlement_days = 0
face_value = 100
fixed_rate_bond = ql.FixedRateBond(
    settlement_days,     
    face_value,     
    schedule,     
    coupons,     
    day_count)
```

Now that we have the `fixed_rate_bond` object,  we can create a `DiscountingBondEngine` and value the bond.
```python
bond_engine = ql.DiscountingBondEngine(ts_handle)
fixed_rate_bond.setPricingEngine(bond_engine)
fixed_rate_bond.NPV()
```
```python
114.18461651948999
```

So far,  we have valued the bond under the treasury yield curve and have not incorporated the credit spreads. Let us assume that the market prices this bond with a `50BP` spread on top of the treasury yield curve. Now we can,  in this case,  directly shock the `flat_rate` used in the yield term structure. Let us see what the value is:
```python
flat_rate.setValue(0.0065)
fixed_rate_bond.NPV()
```
```python
111.5097766266561
```

Above we shocked the `flat_rate` and since the yield term structure is an `Observer` observing the `Observable` `flat_rate`,  we could just shock the rate,  and QuantLib behind the scenes recalculates all the `Observer`s. Though,  this approach is not always viable,  in cases such as a bootstrapped bond curve. So let us look at two different approaches that can be used. Before we do that,  we need to reset the `flat_rate` back to what it was.
```python
flat_rate.setValue(0.0015)
fixed_rate_bond.NPV()
```
```python
114.18461651948999
```

#### Parallel Shift of the Yield Curve

The whole yield curve can be shifted up and down,  and the bond revalued with the help of the `ZeroSpreadedTermStructure`. The constructor takes the yield curve and the spread as argument.
```python
spread1 = ql.SimpleQuote(0.0050)
spread_handle1 = ql.QuoteHandle(spread1)
ts_spreaded1 = ql.ZeroSpreadedTermStructure(ts_handle,     spread_handle1)
ts_spreaded_handle1 = ql.YieldTermStructureHandle(ts_spreaded1)

bond_engine = ql.DiscountingBondEngine(ts_spreaded_handle1)
fixed_rate_bond.setPricingEngine(bond_engine)

# Finally the price
fixed_rate_bond.NPV()
```
```python
111.50977662665609
```

Once we have constructed the spread term structure,  it is rather easy to value for other spreads. All we need to do is change the `SimpleQuote` object `spread1` here.
```python
spread1.setValue(0.01)
fixed_rate_bond.NPV()
```
```python
108.89999943320038
```

#### Non-Parallel Shift of the Yield Curve

The above method allows only for parallel shift of the yield curve. The `SpreadedLinearZeroInterpolatedTermStructure` class allows for non parallel shock. First,  let us mimic a parallel shift using this class. For the constructor,  we need to pass the yield term structure that we wish to shift,  and the a list of spreads and a list of the corresponding dates.
```python
spread21 = ql.SimpleQuote(0.0050)
spread22 = ql.SimpleQuote(0.0050)
start_date = calc_date
end_date = calendar.advance(start_date,     ql.Period(50,     ql.Years))
ts_spreaded2 = ql.SpreadedLinearZeroInterpolatedTermStructure(
    ts_handle,    
    [ql.QuoteHandle(spread21),     ql.QuoteHandle(spread22)],    
    [start_date,     end_date]
)
ts_spreaded_handle2 = ql.YieldTermStructureHandle(ts_spreaded2)

bond_engine = ql.DiscountingBondEngine(ts_spreaded_handle2)
fixed_rate_bond.setPricingEngine(bond_engine)

# Finally the price
fixed_rate_bond.NPV()
```
```python
111.50977662665609
```

Here,  once again we can change the value of `spread2` to value for other shocks.
```python
spread21.setValue(0.01)
spread22.setValue(0.01)
fixed_rate_bond.NPV()
```
```python
108.89999943320038
```

We can easily do non-parallel shifts just by shocking one end.
```python
spread21.setValue(0.005)
spread22.setValue(0.01)
fixed_rate_bond.NPV()
```
```python
111.25358792334083
```

The `SpreadedLinearZeroInterpolatedTermStructure` is a very powerful class and can be used to implement key-rate duration calculations.

   quantlib](http://gouthamanbalaraman.com/tag/quantlib.html)   python   finance

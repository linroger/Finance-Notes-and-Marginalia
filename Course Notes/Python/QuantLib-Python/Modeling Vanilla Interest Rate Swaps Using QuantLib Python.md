---
academic_level: graduate
aliases:
- IRS
- Interest Rate Swap
- Swap Example
description: Provides a basic introduction to valuing interest rate swaps using QuantLib
  Python.
enhanced: true
enhancement_date: '2025-11-06'
enhancement_id: batch09-000051
key_concepts:
- Duration analysis and interest rate risk management
- Convexity adjustments and yield curve sensitivity
- Discounted cash flow (DCF) valuation methodology
- Net present value (NPV) and investment evaluation
- Weighted Average Cost of Capital (WACC) and firm valuation
- Interest rate swaps and fixed income derivatives
- Bootstrap methods and yield curve construction
- LIBOR market model and multi-curve framework
- Basel accords and banking regulation framework
- QuantLib library and quantitative finance implementation
- Arbitrage opportunities and no-arbitrage pricing
- Risk preference theory and utility functions
- 'Valuation Methods: DCF, Comps, and Precedents'
- Yield Curve Analysis and Bond Valuation
- Value at Risk and Expected Shortfall
- Company Valuation and Multiple Analysis
- Credit Risk Management and Default Probability
- Expected Loss and Loss Given Default Models
- Forward Rates and Curve Construction Methods
- Swap Market Mechanisms and Pricing
- Comparable Company Analysis and Trading Multiples
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
- Credit Spreads and Rating Migration Analysis
- LBO Valuation and Debt Capacity Analysis
- Factor Models and Asset Pricing
- Leveraged Buyouts and Private Equity Transactions
- Government and Corporate Bond Markets
- Arbitrage Pricing Theory and Multi-Factor Models
professional_application: theoreti
source: https://gouthamanbalaraman.com/blog/interest-rate-swap-quantlib-python.html
status: active
tags:
- arbitrage-free-models
- arbitrage-opportunity
- banking-regulation
- basel-accord
- basis-risk
- basis-swap
- bootstrap-method
- capital-adequacy
- capital-budgeting
- capital-structure
- caplet
- cash-flow-modeling
- convexity-adjustment
- cost-of-capital
- credit-rating
- leveraged-buyout
- dcf-analysis
- expected-shortfall
- extreme-value-theory
- book-to-market
- backwardation
- volatility-analysis
- style-analysis
- leverage-ratio
- bond-pricing
- corporate-bonds
- yield-curve
- unexpected-loss
- clearinghouse
- interpolation
- overnight-indexed-swaps
- arbitrage-pricing-theory
- hedge-ratio
- private-equity
- loss-given-default
- value-factor
- dirty-price
- monte-carlo-var
- coupon-bonds
- forward-contracts
- yield-to-maturity
- fama-french
- forward-rates
- price-to-earnings
- recovery-rate
- zero-coupon-bonds
- parametric-var
- var-methodologies
- historical-var
- contango
- debt-capacity
- expected-loss
- quantitative-finance
- forward-curve
- currency-swaps
- investment-return
- government-bonds
- probabilty-of-default
- curve-fitting
- credit-default-swaps
- roll-yield
- spot-rates
- equity-kickers
- lbo-valuation
- momentum
- term-structure
- sofr
- swap-rate
- ' exposure-at-default'
- stress-testing
- mathematical-finance
- rating-migration
- par-yield
- comparable-analysis
- investment-analysis
- economic-value-added
- value-at-risk
- bootstrap-strategy
- management-buyout
- factor-models
- risk-management
- convergence
- var-backtesting
- sum-of-parts
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
- trading-multiples
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
title: Modeling Vanilla Interest Rate Swaps Using QuantLib Python
type: note
---
--



# Modeling Vanilla Interest Rate Swaps Using QuantLib Python

Provides a basic introduction to valuing interest rate swaps using QuantLib Python.

_Visit here for other QuantLib Python examples](http://gouthamanbalaraman.com/blog/quantlib-python-tutorials-with-examples.html). If you found these posts useful,  please take a minute by providing some  feedback._

An Interest Rate Swap is a financial derivative instrument in which two parties agree to exchange interest rate cash flows based on a notional amount from a fixed rate to a floating rate or from one floating rate to another floating rate. 

Here we will consider an example of a plain vanilla USD swap with 10 million notional and 10 year maturity. Let the fixed leg pay 2.5% coupon semiannually,  and the floating leg pay Basis Swap Markets#London Interbank Offered Rate (LIBOR) | LIBOR]] 3m quarterly.

## Sample Code
```python
import QuantLib as ql
calculation_date = ql.Date(20,  10,  2015)
ql.Settings.instance().evaluationDate = calculation_date
```

Here we construct the yield curve objects. For simplicity,  we will use flat curves for discounting and Basis Swap Markets#London Interbank Offered Rate (LIBOR) | LIBOR]] 3M. This will help us focus on the Swap construction part. Please refer to curve construction example-term-structure-bootstrap-yield-curve.html) for some details.
```python
# construct discount curve and [](../../../Fixed%20Income%20Asset%20Pricing/Fixed%20Income%20Lecture%20Notes/A%20Guide%20to%20the%20Front%20End%20and%20Basis%20Swap%20Markets.md#London%20Interbank%20Offered%20Rate%20(LIBOR) | LIBOR) curve
risk_free_rate = 0.01
libor_rate = 0.02
day_count = ql.Actual365Fixed()

discount_curve = ql.YieldTermStructureHandle(
    ql.FlatForward(calculation_date,   risk_free_rate,   day_count)
)

libor_curve = ql.YieldTermStructureHandle(
    ql.FlatForward(calculation_date,   libor_rate,   day_count)
)
#libor3M_index = ql.Euribor3M(libor_curve)  
libor3M_index = ql.USDLibor(ql.Period(3,   ql.Months),   libor_curve)
```

To construct the Swap instrument,  we have to specify the fixed rate leg and floating rate leg. We construct the fixed rate and floating rate leg schedules below.
```python
calendar = ql.UnitedStates()
settle_date = calendar.advance(calculation_date,   5,   ql.Days)
maturity_date = calendar.advance(settle_date,   10,   ql.Years)

fixed_leg_tenor = ql.Period(6,   ql.Months)
fixed_schedule = ql.Schedule(settle_date,   maturity_date,   
                             fixed_leg_tenor,   calendar,  
                             ql.ModifiedFollowing,   ql.ModifiedFollowing,  
                             ql.DateGeneration.Forward,   False)

float_leg_tenor = ql.Period(3,   ql.Months)
float_schedule = ql.Schedule (settle_date,   maturity_date,   
                              float_leg_tenor,   calendar,  
                              ql.ModifiedFollowing,   ql.ModifiedFollowing,  
                              ql.DateGeneration.Forward,   False)
```

Below,  we construct a `VanillaSwap` object by including the fixed and float leg schedules created above.
```python
notional = 10000000
fixed_rate = 0.025
fixed_leg_daycount = ql.Actual360()
float_spread = 0.004
float_leg_daycount = ql.Actual360()

ir_swap = ql.VanillaSwap(ql.VanillaSwap.Payer,   notional,   fixed_schedule,   
               fixed_rate,   fixed_leg_daycount,   float_schedule,  
               libor3M_index,   float_spread,   float_leg_daycount )
```

We evaluate the swap using a discounting engine.
```python
swap_engine = ql.DiscountingSwapEngine(discount_curve)
ir_swap.setPricingEngine(swap_engine)
```

## Result Analysis

The cashflows for the fixed and floating leg can be extracted from the `ir_swap` object. The fixed leg cashflows are shown below:
```python
for i,  cf in enumerate(ir_swap.leg(0)):
    print "%2d    %-18s  %10.2f"%(i+1,  cf.date(),  cf.amount())
```
```python
 1    January 27th,   2016    60760.46
 2    April 27th,   2016      60098.65
 3    July 27th,   2016       60098.65
 4    October 27th,   2016    60760.46
 5    January 27th,   2017    60760.46
 6    April 27th,   2017      59436.87
 7    July 27th,   2017       60098.65
 8    October 27th,   2017    60760.46
 9    January 29th,   2018    62084.17
10    April 27th,   2018      58113.40
11    July 27th,   2018       60098.65
12    October 29th,   2018    62084.17
13    January 28th,   2019    60098.65
14    April 29th,   2019      60098.65
15    July 29th,   2019       60098.65
16    October 28th,   2019    60098.65
17    January 27th,   2020    60098.65
18    April 27th,   2020      60098.65
19    July 27th,   2020       60098.65
20    October 27th,   2020    60760.46
21    January 27th,   2021    60760.46
22    April 27th,   2021      59436.87
23    July 27th,   2021       60098.65
24    October 27th,   2021    60760.46
25    January 27th,   2022    60760.46
26    April 27th,   2022      59436.87
27    July 27th,   2022       60098.65
28    October 27th,   2022    60760.46
29    January 27th,   2023    60760.46
30    April 27th,   2023      59436.87
31    July 27th,   2023       60098.65
32    October 27th,   2023    60760.46
33    January 29th,   2024    62084.17
34    April 29th,   2024      60098.65
35    July 29th,   2024       60098.65
36    October 28th,   2024    60098.65
37    January 27th,   2025    60098.65
38    April 28th,   2025      60098.65
39    July 28th,   2025       60098.65
40    October 27th,   2025    60098.65
```

The floating leg cashflows are shown below:
```python
for i,  cf in enumerate(ir_swap.leg(1)):
    print "%2d    %-18s  %10.2f"%(i+1,  cf.date(),  cf.amount())
```

Expand Code
```python
 1    January 27th,   2016    60760.46
 2    April 27th,   2016      60098.65
 3    July 27th,   2016       60098.65
 4    October 27th,   2016    60760.46
 5    January 27th,   2017    60760.46
 6    April 27th,   2017      59436.87
 7    July 27th,   2017       60098.65
 8    October 27th,   2017    60760.46
 9    January 29th,   2018    62084.17
10    April 27th,   2018      58113.40
11    July 27th,   2018       60098.65
12    October 29th,   2018    62084.17
13    January 28th,   2019    60098.65
14    April 29th,   2019      60098.65
15    July 29th,   2019       60098.65
16    October 28th,   2019    60098.65
17    January 27th,   2020    60098.65
18    April 27th,   2020      60098.65
19    July 27th,   2020       60098.65
20    October 27th,   2020    60760.46
21    January 27th,   2021    60760.46
22    April 27th,   2021      59436.87
23    July 27th,   2021       60098.65
24    October 27th,   2021    60760.46
25    January 27th,   2022    60760.46
26    April 27th,   2022      59436.87
27    July 27th,   2022       60098.65
28    October 27th,   2022    60760.46
29    January 27th,   2023    60760.46
30    April 27th,   2023      59436.87
31    July 27th,   2023       60098.65
32    October 27th,   2023    60760.46
33    January 29th,   2024    62084.17
34    April 29th,   2024      60098.65
35    July 29th,   2024       60098.65
36    October 28th,   2024    60098.65
37    January 27th,   2025    60098.65
38    April 28th,   2025      60098.65
39    July 28th,   2025       60098.65
40    October 27th,   2025    60098.65
```

Some other analytics such as the fair value,  fair spread etc can be extracted as shown below.
```python
print "%-20s: %20.3f" % ("Net Present Value",  ir_swap.NPV())
print "%-20s: %20.3f" % ("Fair Spread",  ir_swap.fairSpread())
print "%-20s: %20.3f" % ("Fair Rate",  ir_swap.fairRate())
print "%-20s: %20.3f" % ("Fixed Leg BPS",  ir_swap.fixedLegBPS())
print "%-20s: %20.3f" % ("Floating Leg BPS",  ir_swap.floatingLegBPS())
```

Expand Code
```python
Net Present Value   :          -115054.034
Fair Spread         :                0.005
Fair Rate           :                0.024
Fixed Leg BPS       :            -9629.981
Floating Leg BPS    :             9642.042
```

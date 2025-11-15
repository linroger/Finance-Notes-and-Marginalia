---
aliases:
- IRS
- Interest Rate Swap
- Swap Example
description: Provides a basic introduction to valuing interest rate swaps using QuantLib
  Python.
enhanced: true
enhancement_date: '2025-11-06'
enhancement_id: batch03-b48d33
key_concepts:
- Notional amount
- Term structure of interest rates and yield curve shapes
- Treasury Futures
- Interest rate swap valuation and fixed-floating spreads
- Monte Carlo simulation techniques for path-dependent options
- Real options valuation in corporate investment decisions
- Binomial option pricing model for American-style options
- Greeks calculation and their interpretation in options trading
- Single-name vs. index CDS trading
- Collateralized Debt Obligations
- Option Greeks and portfolio risk management
- Commodity markets and pricing dynamics
- Expectations hypothesis and liquidity preference theory
- Yield curve fitting and interpolation methods
- Credit spread decomposition and hazard rates
- QuantLib Python valuation
- Vega and volatility risk management
- CDS clearing and central counterparties
- Commodity futures pricing and storage costs
- Interest rate swap
- CDS-Bond basis and arbitrrage opportunities
- Swap spread and credit risk considerations
- Spot rates vs. forward rates modeling
- Mathematical Finance
- Credit default swap pricing and recovery assumptions
- GARCH models and volatility forecasting
- 'Structured products: CDOs, CLOs, and credit derivatives'
- modified following convention in CDS
- Fixed-for-floating swap cash flows and valuation
- Course Material
- Forward rates and interest rate parity
- Theta and time decay modeling
- Risk-neutral pricing methodology for derivative securities
- Synthetic credit derivatives and index trades
- Case Study
- Exchange rate determination and PPP theory
- Treasury futures trading and basis point value calculations
- CVA and DVA adjustments in derivative pricing
- Interest rate swap pricing and valuation
- interest rate and currency derivatives
- Credit default swap pricing and risk-neutral probabilities
- present value and discounting methods
- Variance swaps and volatility trading strategies
- fair value measurement and hierarchy
- Delta hedging strategies in options portfolio management
- Theta decay modeling for time-sensitive options strategies
- Implied volatility extraction from market option prices
- Fixed vs. floating
- Volatility smile and skew modeling in options markets
- Gamma and convexity adjustments
- Delta hedging and the replication argument
- Parallel and non-parallel shifts in the yield curve
- Cross-currency basis swaps and funding
- Cash flow analysis
- Currency markets and foreign exchange trading
source: https://gouthamanbalaraman.com/blog/interest-rate-swap-quantlib-python.html
tags:
- yield-curve
- treasury-futures
- commodities
- credit-default-swaps
- collateralized-debt-obligations
- garch-models
- interest-rate-swaps
- mathematical-finance
- course-material
- interest_rate_swaps
- fixed_floating
- financial-modeling
- case-study
- greeks
- exchange-rates
- quantitative-implementation
- duration-convexity
- solution
- treasury-bonds
- vanilla_swaps
- swap_valuation
- net-present-value
- implied-volatility
- quantitative-finance
- dcf-valuation
- quantlib_python
- monte-carlo
title: Modeling Vanilla Interest Rate Swaps Using QuantLib Python
---

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

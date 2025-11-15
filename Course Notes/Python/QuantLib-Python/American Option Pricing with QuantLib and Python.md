---
aliases:
- AAPL Option Pricing
- Option Valuation
description: This post explains valuing American Options using QuantLib and Python
enhanced: true
enhancement_date: '2025-11-06'
enhancement_id: batch03-f01262
key_concepts:
- European Options
- Cox-Ross-Rubinstein parameter specification
- Term structure of interest rates and yield curve shapes
- American Options
- Risk assessment and management
- Computational implementation of binomial option pricing
- Binomial option pricing model for American-style options
- Expectations hypothesis and liquidity preference theory
- Mathematical derivation of the Black-Scholes partial differential equation
- Solution
- Historical simulation vs. parametric VaR models
- Discounted Cash Flow valuation methodology
- Yield curve fitting and interpolation methods
- option pricing models and PDE solutions
- Mathematical Finance
- Black-Scholes partial differential equation and its boundary conditions
- Spot rates vs. forward rates modeling
- European option pricing
- Monte Carlo VaR for complex portfolios
- Stress testing and scenario analysis
- Portfolio optimization and asset allocation
- Black-Scholes-Merton process
- Value at Risk (VaR) methodologies and backtesting
- QuantLib and Python
- Case Study
- Quantitative analysis and modeling
- Dividend Policy
- Expected Shortfall and coherent risk measures
- excess returns and manager skill
- Risk-neutral valuation in continuous time models
- American option valuation
- Convergence of binomial model to Black-Scholes solution
- Binomial option pricing model with multiple time steps
- Fixed income analysis and term structure
- Free cash flow to equity and firm valuation
- Boundary conditions and parameter interpretation in Black-Scholes model
- Limitations and extensions of the Black-Scholes framework
- Derivatives pricing and hedging strategies
- Terminal value estimation and perpetuity growth
- American option pricing in binomial trees
- Financial markets and instruments
- Quantitative Implementation
- Binomial tree approach
- Parallel and non-parallel shifts in the yield curve
- Black-Scholes-Merton option pricing model and its applications
source: http://gouthamanbalaraman.com/blog/american-option-pricing-quantlib-python.html
tags:
- yield-curve
- python
- binomial-model
- dividend-policy
- american_option_pricing
- mathematical-finance
- european_option
- financial-modeling
- case-study
- black-scholes-model
- value-at-risk
- exchange-rates
- european-options
- quantitative-implementation
- solution
- american-options
- option-pricing
- binomial_engine
- quantitative-finance
- dcf-valuation
- quantlib
title: American Option Pricing with QuantLib and Python
---

# American Option Pricing with QuantLib and Python

This post explains valuing American Options using QuantLib and Python

*Visit here for other QuantLib Python examples](http://gouthamanbalaraman.com/blog/quantlib-python-tutorials-with-examples.html). If you found these posts useful,  please take a minute by providing some feedback.*

I wrote about pricing European options using [QuantLib](http://gouthamanbalaraman.com/blog/european-option-binomial-tree-quantlib-python.html) in an earlier post. Since then,  I have received many questions from readers on how to extend this to price American options. So here is a modified example on pricing American options using QuantLib. The idea is very similar to European Option construction. Lets take a look at the details below. In this post,  I will price both an European option and an American option side by side.
```python
import QuantLib as ql 
import matplotlib.pyplot as plt
%matplotlib inline
ql.__version__
```

Let us consider a European and an American call option for AAPL with a strike price of $130 maturing on 15th Jan,    2016. Let the spot price be $127.62. The volatility of the underlying stock is known to be 20%,  and has a dividend yield of 1.63%. Lets value these options as of 8th May,  2015.
```python
# American Option Pricing with QuantLib and Python
maturity_date = ql.Date(15,    1,    2016)
spot_price = 127.62
strike_price = 130
volatility = 0.20 # the historical vols or implied vols
dividend_rate =  0.0163
option_type = ql.Option.Call

risk_free_rate = 0.001
day_count = ql.Actual365Fixed()
calendar = ql.UnitedStates()

calculation_date = ql.Date(8,    5,    2015)
ql.Settings.instance().evaluationDate = calculation_date
```

We construct the European and American options here. The main difference here is in the Exercise type. One has to use `AmericanExercise` instead of `EuropeanExercise` to pass into the `VanillaOption` to construct an American option.
```python
payoff = ql.PlainVanillaPayoff(option_type,    strike_price)
settlement = calculation_date

am_exercise = ql.AmericanExercise(settlement,    maturity_date)
american_option = ql.VanillaOption(payoff,    am_exercise)

eu_exercise = ql.EuropeanExercise(maturity_date)
european_option = ql.VanillaOption(payoff,    eu_exercise)
```

The Black-Scholes-Merton process is constructed here.
```python
spot_handle = ql.QuoteHandle(
    ql.SimpleQuote(spot_price)
)
flat_ts = ql.YieldTermStructureHandle(
    ql.FlatForward(calculation_date,    risk_free_rate,    day_count)
)
dividend_yield = ql.YieldTermStructureHandle(
    ql.FlatForward(calculation_date,    dividend_rate,    day_count)
)
flat_vol_ts = ql.BlackVolTermStructureHandle(
    ql.BlackConstantVol(calculation_date,    calendar,    volatility,    day_count)
)
bsm_process = ql.BlackScholesMertonProcess(spot_handle,    
                                           dividend_yield,    
                                           flat_ts,    
                                           flat_vol_ts)
```

The value of the American option can be computed using a Binomial Engine using the CRR approach.
```python
steps = 200
binomial_engine = ql.BinomialVanillaEngine(bsm_process,    "crr",    steps)
american_option.setPricingEngine(binomial_engine)
print (american_option.NPV())
```

For illustration purpose,  lets compare the European and American option prices using the binomial tree approach.
```python
def binomial_price(option,    bsm_process,    steps):
    binomial_engine = ql.BinomialVanillaEngine(bsm_process,    "crr",    steps)
    option.setPricingEngine(binomial_engine)
    return option.NPV()

steps = range(5,    200,    1)
eu_prices = [binomial_price(european_option,    bsm_process,    step) for step in steps]
am_prices = [binomial_price(american_option,    bsm_process,    step) for step in steps]
# theoretican European option price
european_option.setPricingEngine(ql.AnalyticEuropeanEngine(bsm_process))
bs_price = european_option.NPV()
```

In the plot below,  the binomial-tree approach is used to value American option for different number of steps. You can see the prices converging with increase in number of steps. The European option price is plotted along with BSM theoretical price for comparison purposes.
```python
plt.plot(steps,    eu_prices,    label="European Option",    lw=2,    alpha=0.6)
plt.plot(steps,    am_prices,    label="American Option",    lw=2,    alpha=0.6)
plt.plot([5,   200],   [bs_price,    bs_price],    "r--",    label="BSM Price",    lw=2,    alpha=0.6)
plt.xlabel("Steps")
plt.ylabel("Price")
plt.ylim(6.7,   7)
plt.title("Binomial Tree Price For Varying Steps")
plt.legend()
```
```python
<matplotlib.legend.Legend at 0x85b24e0>
```

   quantlib](http://gouthamanbalaraman.com/tag/quantlib.html)   python   finance

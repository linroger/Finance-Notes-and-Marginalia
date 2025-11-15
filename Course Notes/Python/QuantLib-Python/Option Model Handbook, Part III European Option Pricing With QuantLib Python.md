---
aliases:
- Option Pricing with QuantLib
- QuantLib European Options
description: Demonstrates how to price European options using QuantLib Python. Methods
  using Black-Scholes-Merton formula and binomial tree will be discussed.
enhanced: true
enhancement_date: '2025-11-06'
enhancement_id: batch03-2ddcb1
key_concepts:
- European Options
- Black-Scholes-Merton formula
- Cox-Ross-Rubinstein parameter specification
- Term structure of interest rates and yield curve shapes
- Sensitivity analysis in DCF models
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
- Value at Risk (VaR) methodologies and backtesting
- Case Study
- Quantitative analysis and modeling
- Dividend Policy
- Expected Shortfall and coherent risk measures
- excess returns and manager skill
- Risk-neutral valuation in continuous time models
- Binomial tree method
- Convergence of binomial model to Black-Scholes solution
- AAPL call option
- Binomial option pricing model with multiple time steps
- Fixed income analysis and term structure
- QuantLib Python example
- Free cash flow to equity and firm valuation
- Boundary conditions and parameter interpretation in Black-Scholes model
- Limitations and extensions of the Black-Scholes framework
- Derivatives pricing and hedging strategies
- Terminal value estimation and perpetuity growth
- American option pricing in binomial trees
- Financial markets and instruments
- Quantitative Implementation
- Parallel and non-parallel shifts in the yield curve
- Black-Scholes-Merton option pricing model and its applications
source: https://gouthamanbalaraman.com/blog/european-option-binomial-tree-quantlib-python.html
tags:
- financial-analysis
- yield-curve
- binomial-model
- dividend-policy
- mathematical-finance
- aapl_option
- financial-modeling
- case-study
- black-scholes-model
- value-at-risk
- exchange-rates
- european-options
- quantitative-implementation
- solution
- black_scholes_merton
- option-pricing
- binomial_tree
- european_option_pricing
- quantitative-finance
- dcf-valuation
- quantlib_python
title: Option Model Handbook,  Part III European Option Pricing With QuantLib Python
---

# Option Model Handbook, Part III European Option Pricing With QuantLib Python

Demonstrates how to price European options using QuantLib Python. Methods using Black-Scholes-Merton formula and binomial tree will be discussed.

*Visit here for other QuantLib Python examples](http://gouthamanbalaraman.com/blog/quantlib-python-tutorials-with-examples.html). If you found these posts useful,  please take a minute by providing some feedback.*

I have written about option pricing earlier. The introduction to option pricing](http://gouthamanbalaraman.com/blog/option-model-handbook-part-I-introduction-to-option-models.html) gave an overview of the theory behind option pricing. The post on introduction to binomial trees](http://gouthamanbalaraman.com/blog/option-model-handbook-part-II-introduction-to-binomial-trees.html) outlined the binomial tree method to price options.

In this post,  we will use QuantLib and the Python extension to illustrate a very simple example. Here we are going to price a European option using the Black-Scholes-Merton formula. We will price them again using the Binomial tree and understand the agreement between the two.

In \[1\]:
```latex
import QuantLib as ql # version 1.5
import matplotlib.pyplot as plt
%matplotlib inline
```

Let us consider a European call option for AAPL with a strike price of \\$130 maturing on 15th Jan,  2016. Let the spot price be \\$127.62. The volatility of the underlying stock is know to be 20%,  and has a dividend yield of 1.63%. Lets value this option as of 8th May,  2015.

In \[2\]:
```latex
# Option Model Handbook,  Part III European Option Pricing With QuantLib Python
maturity_date = ql.Date(15,  1,  2016)
spot_price = 127.62
strike_price = 130
volatility = 0.20 # the historical vols for a year
dividend_rate =  0.0163
option_type = ql.Option.Call

risk_free_rate = 0.001
day_count = ql.Actual365Fixed()
calendar = ql.UnitedStates()

calculation_date = ql.Date(8,  5,  2015)
ql.Settings.instance().evaluationDate = calculation_date
```

We construct the European option here.

In \[3\]:
```latex
# construct the European Option
payoff = ql.PlainVanillaPayoff(option_type,  strike_price)
exercise = ql.EuropeanExercise(maturity_date)
european_option = ql.VanillaOption(payoff,  exercise)
```

The Black-Scholes-Merto process is constructed here.

In \[4\]:
```latex
spot_handle = ql.QuoteHandle(
    ql.SimpleQuote(spot_price)
)
flat_ts = ql.YieldTermStructureHandle(
    ql.FlatForward(calculation_date,  risk_free_rate,  day_count)
)
dividend_yield = ql.YieldTermStructureHandle(
    ql.FlatForward(calculation_date,  dividend_rate,  day_count)
)
flat_vol_ts = ql.BlackVolTermStructureHandle(
    ql.BlackConstantVol(calculation_date,  calendar,  volatility,  day_count)
)
bsm_process = ql.BlackScholesMertonProcess(spot_handle,  
                                           dividend_yield,  
                                           flat_ts,  
                                           flat_vol_ts)
```

Lets compute the theoretical price using the `AnalyticEuropeanEngine`.

In \[5\]:
```latex
european_option.setPricingEngine(ql.AnalyticEuropeanEngine(bsm_process))
bs_price = european_option.NPV()
print "The theoretical price is ",  bs_price
```
```latex
The theoretical price is  6.74927181246
```

Lets compute the price using the binomial-tree approach.

In \[6\]:
```latex
def binomial_price(bsm_process,  steps):
    binomial_engine = ql.BinomialVanillaEngine(bsm_process,  "crr",  steps)
    european_option.setPricingEngine(binomial_engine)
    return european_option.NPV()

steps = range(2,  100,  1)
prices = [binomial_price(bsm_process,  step) for step in steps]
```

In the plot below,  we show the convergence of binomial-tree approach by comparing its price with the BSM price.

In \[8\]:
```latex
plt.plot(steps,  prices,  label="Binomial Tree Price",  lw=2,  alpha=0.6)
plt.plot([0, 100], [bs_price,  bs_price],  "r--",  label="BSM Price",  lw=2,  alpha=0.6)
plt.xlabel("Steps")
plt.ylabel("Price")
plt.title("Binomial Tree Price For Varying Steps")
plt.legend()
```

Out\[8\]:
```latex
<matplotlib.legend.Legend at 0x7f0b85fa7510>
```

 !500

## Conclusion

This post shows how to price European Options using the theoretical and binomial-tree methods in QuantLib Python. You can download the ipython notebook on European option [pricing with QuantLib](https://gouthamanbalaraman.com/extra/notebooks/european-option-models.ipynb).

   quantlib](http://gouthamanbalaraman.com/tag/quantlib.html)   python   finance   option models

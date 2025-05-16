---
title: Option Model Handbook,  Part III European Option Pricing With QuantLib Python
source: 
  https://gouthamanbalaraman.com/blog/european-option-binomial-tree-quantlib-python.html
description: Demonstrates how to price European options using QuantLib Python. Methods
  using Black-Scholes-Merton formula and binomial tree will be discussed.
tags:
  - aapl_option
  - binomial_tree
  - black_scholes_merton
  - european_option_pricing
  - quantlib_python
aliases:
  - Option Pricing with QuantLib
  - QuantLib European Options
key_concepts:
  - AAPL call option
  - Binomial tree method
  - Black-Scholes-Merton formula
  - European option pricing
  - QuantLib Python example
---

# Option Model Handbook, Part III European Option Pricing With QuantLib Python

Demonstrates how to price European options using [QuantLib Python](Valuing%20Callable%20Bonds%20Using%20QuantLib%20Python.md). Methods using [Black-Scholes-Merton formula](.md) and [binomial tree](../../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%207/Rate%20and%20Price%20Trees.md) will be discussed.

*Visit here for other [QuantLib Python]([Valuing%20Callable%20Bonds%20Using%20QuantLib%20Python) examples](http://gouthamanbalaraman.com/blog/[quantlib](Introduction%20to%20QuantLib%20Python.md)-python-tutorials-with-examples.html). If you found these posts useful,  please take a minute by providing some [feedback.](https://docs.google.com/forms/d/e/1FAIpQLSdFdJ768HKmIyJmaVRHBUJNY5NyQl6vr0GZvSkx-bUfIloNZA/viewform)*

I have written about option [pricing](../../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%207/Arbitrage%20Pricing%20of%20Derivatives.md) earlier. The [introduction]([Squam%20Lake%20Group%20Introduction) to option [pricing](../../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%207/Arbitrage%20Pricing%20of%20Derivatives.md)](http://gouthamanbalaraman.com/blog/option-model-handbook-part-I-[introduction](../../../Financial%20Markets%20and%20Institutions/III.%20Liquidity%20of%20Assets/Class%209-%20Bailouts%20and%20Bank%20Failures/Squam%20Lake%20Group%20Introduction.md)-to-option-models.html) gave an [overview](../../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%201%20-%20Purpose%20and%20Structure%20of%20Financial%20Markets/Overview%20of%20Financial%20Markets.md) of the theory behind option [pricing](../../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%207/Arbitrage%20Pricing%20of%20Derivatives.md). The post on [introduction]([Squam%20Lake%20Group%20Introduction) to [binomial](../../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%205%20Options%20on%20Prices%20and%20Hedge-Based%20Valuation/A%20Real-Life%20Option%20Pricing%20Exercise.md) trees](http://gouthamanbalaraman.com/blog/option-model-handbook-part-II-[introduction](../../../Financial%20Markets%20and%20Institutions/III.%20Liquidity%20of%20Assets/Class%209-%20Bailouts%20and%20Bank%20Failures/Squam%20Lake%20Group%20Introduction.md)-to-[binomial](../../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%205%20Options%20on%20Prices%20and%20Hedge-Based%20Valuation/A%20Real-Life%20Option%20Pricing%20Exercise.md)-trees.html) outlined the [binomial tree method](.md) to price options.

In this post,  we will use [QuantLib](Introduction%20to%20QuantLib%20Python.md) and the Python extension to illustrate a very simple example. Here we are going to price a European option using the [Black-Scholes-Merton formula](.md). We will price them again using the [Binomial tree](../../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%207/Rate%20and%20Price%20Trees.md) and understand the agreement between the two.

In \[1\]:
```latex
import QuantLib as ql # version 1.5
import matplotlib.pyplot as plt
%matplotlib inline
```

Let us consider a European call option for AAPL with a [strike price](../../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%205%20Options%20on%20Prices%20and%20Hedge-Based%20Valuation/Call%20and%20Put%20Payoffs%20at%20Expiry.md) of \\$130 maturing on 15th Jan,  2016. Let the spot price be \\$127.62. The volatility of the underlying stock is know to be 20%,  and has a dividend yield of 1.63%. Lets value this option as of 8th May,  2015.

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

The [Black-Scholes](../../../Financial%20Engineering/Mathematical%20Modeling%20of%20Derivative%20Pricing.md)-Merto process is constructed here.

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

Lets compute the price using the [binomial](../../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%205%20Options%20on%20Prices%20and%20Hedge-Based%20Valuation/A%20Real-Life%20Option%20Pricing%20Exercise.md)-tree approach.

In \[6\]:
```latex
def binomial_price(bsm_process,  steps):
    binomial_engine = ql.BinomialVanillaEngine(bsm_process,  "crr",  steps)
    european_option.setPricingEngine(binomial_engine)
    return european_option.NPV()

steps = range(2,  100,  1)
prices = [binomial_price(bsm_process,  step) for step in steps]
```

In the plot below,  we show the convergence of [binomial](../../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%205%20Options%20on%20Prices%20and%20Hedge-Based%20Valuation/A%20Real-Life%20Option%20Pricing%20Exercise.md)-tree approach by comparing its price with the BSM price.

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

 ![500](binomial_tree_for_varying_steps.png)

## Conclusion

This post shows how to price European Options using the theoretical and [binomial](../../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%205%20Options%20on%20Prices%20and%20Hedge-Based%20Valuation/A%20Real-Life%20Option%20Pricing%20Exercise.md)-tree methods in [QuantLib Python](Valuing%20Callable%20Bonds%20Using%20QuantLib%20Python.md). You can download the [ipython notebook on European option [pricing](../../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%207/Arbitrage%20Pricing%20of%20Derivatives.md) with [QuantLib](Introduction%20to%20QuantLib%20Python.md)](https://gouthamanbalaraman.com/extra/notebooks/european-option-models.ipynb).

   [quantlib]([Introduction%20to%20QuantLib%20Python)](http://gouthamanbalaraman.com/tag/[quantlib](Introduction%20to%20QuantLib%20Python.md).html)   [python](http://gouthamanbalaraman.com/tag/python.html)   [finance](http://gouthamanbalaraman.com/tag/finance.html)   [option models](http://gouthamanbalaraman.com/tag/option-models.html)

---

**Related Post**

- [QuantLib Python]([Valuing%20Callable%20Bonds%20Using%20QuantLib%20Python) Tutorials With Examples](http://gouthamanbalaraman.com/blog/[quantlib](Introduction%20to%20QuantLib%20Python.md)-python-tutorials-with-examples.html)
- [Modeling Vanilla Interest Rate Swaps Using [QuantLib Python](Valuing%20Callable%20Bonds%20Using%20QuantLib%20Python.md)](http://gouthamanbalaraman.com/blog/interest-rate-swap-[quantlib](Introduction%20to%20QuantLib%20Python.md)-python.html)
- [On the Convergence of Hull White [Monte Carlo](../../../Financial%20Instruments/Lecture%20Notes-%20Financial%20Instruments/Teaching%20Note%207-Exotic%20Options%20And%20Derivative%20Pricing%20By%20Monte%20Carlo%20Simulation.md) Simulations](http://gouthamanbalaraman.com/blog/hull-white-simulation-monte-carlo-convergence.html)
- [Valuing Options on [Commodity Futures](../../../Financial%20Instruments/Financial%20Instruments%20PSET%20Solutions.md) Using [QuantLib Python](Valuing%20Callable%20Bonds%20Using%20QuantLib%20Python.md)](http://gouthamanbalaraman.com/blog/value-options-commodity-[futures](../../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%203%20-%20Futures%20Markets/Futures%20Not%20Subject%20to%20Cash-And-Carry.md)-black-formula-[quantlib](Introduction%20to%20QuantLib%20Python.md)-python.html)
- [Short [Interest Rate Model](../../../Fixed%20Income%20Asset%20Pricing/Fixed%20Income%20Lecture%20Notes/An%20Overview%20of%20the%20Vasicek%20Short%20Rate%20Model.md) [Calibration](../../../Credit%20Markets/Credit%20Markets%20Session%204.md) in [QuantLib Python](Valuing%20Callable%20Bonds%20Using%20QuantLib%20Python.md)](http://gouthamanbalaraman.com/blog/short-interest-rate-model-[calibration](../../../Credit%20Markets/Credit%20Markets%20Session%204.md)-[quantlib](Introduction%20to%20QuantLib%20Python.md).html)
---
title: Valuing European Option Using the Heston Model in QuantLib Python
source: 
  https://gouthamanbalaraman.com/blog/valuing-european-option-heston-model-quantLib.html
description: Introduces an example on how to value European options using Heston model
  in Quantlib Python
tags:
  - aapl_option
  - european_option
  - heston_model
  - quantlib_python
  - stochastic_volatility
aliases:
  - Heston Option Pricing
  - QuantLib Heston
key_concepts:
  - Black-Scholes comparison
  - European option valuation
  - Heston model
  - QuantLib Python example
  - Stochastic volatility
---

# Valuing European Option Using the Heston Model in QuantLib Python

Introduces an example on how to value European options using [Heston model](.md) in [Quantlib Python](Valuing%20Callable%20Bonds%20Using%20QuantLib%20Python.md)

*Visit here for other [QuantLib Python]([Valuing%20Callable%20Bonds%20Using%20QuantLib%20Python) examples](http://gouthamanbalaraman.com/blog/[quantlib](Introduction%20to%20QuantLib%20Python.md)-python-tutorials-with-examples.html). If you found these posts useful,  please take a minute by providing some [feedback.](https://docs.google.com/forms/d/e/1FAIpQLSdFdJ768HKmIyJmaVRHBUJNY5NyQl6vr0GZvSkx-bUfIloNZA/viewform)*

[Heston model](.md) can be used to value options by modeling the [underlying asset](../../../Financial%20Instruments/Financial%20Derivatives%20and%20Quantitative%20Methods/Risk%20Neutral%20Pricing%20of%20Options.md) such as the stock of a company. The one major feature of the [Heston model](.md) is that it inocrporates a [stochastic volatility](.md) term.
$$\begin{eqnarray} dS\_t &=& \mu S\_tdt + \sqrt{V\_t} S\_t dW\_t^1 \\ dV\_t &=& \kappa(\theta-V\_t) + \sigma \sqrt{V\_t} dW\_t^2 \end{eqnarray}$$

Here :

- $S\_t$ is the asset's value at time $t$
- $\mu$ is the expected growth rate of the log normal stock value
- $V\_t$ is the variance of the asset $S\_t$
- $W\_t^1$ is the [stochastic process](../../../The%20Ornstein-Uhlenbeck%20(OU)%20Process.md) governing the $S\_t$ process
- $\theta$ is the value of [mean reversion](../../../The%20Ornstein-Uhlenbeck%20(OU)%20Process.md) for the variance $V\_t$
- $\kappa$ is the strength of [mean reversion](../../../The%20Ornstein-Uhlenbeck%20(OU)%20Process.md)
- $\sigma$ is the volatility of volatility
- $W\_t^2$ is the [stochastic process](../../../The%20Ornstein-Uhlenbeck%20(OU)%20Process.md) governing the $V\_t$ process
- The correlation between $W\_t^1$ and $W\_t^2$ is $\rho$

In contrast,  the [Black-Scholes-Merton process](Valuing%20Convertible%20Bonds%20Using%20QuantLib%20Python.md) assumes that the volatility is constant.

Let us consider a European call option for AAPL with a [strike price](../../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%205%20Options%20on%20Prices%20and%20Hedge-Based%20Valuation/Call%20and%20Put%20Payoffs%20at%20Expiry.md) of \$130 maturing on 15th Jan,  2016. Let the spot price be \$127.62. The volatility of the underlying stock is know to be 20%,  and has a dividend yield of 1.63%. We assume a short term risk free rate of 0.1%. Lets value this option as of 8th May,  2015.
```python
import QuantLib as ql
import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import simps,  cumtrapz,  romb
% matplotlib inline
import math
```

Using the above inputs,  we construct the European option as shown below.
```python
# option parameters
strike_price = 110.0
payoff = ql.PlainVanillaPayoff(ql.Option.Call,  strike_price)

# option data
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
```python
# Valuing European Option Using the Heston Model in QuantLib Python
payoff = ql.PlainVanillaPayoff(option_type,   strike_price)
exercise = ql.EuropeanExercise(maturity_date)
european_option = ql.VanillaOption(payoff,   exercise)
```

In order to price the option using the [Heston model](.md),  we first create the [Heston](../../../Financial%20Engineering/Mathematical%20Modeling%20of%20Derivative%20Pricing.md) process. In order to create the [Heston](../../../Financial%20Engineering/Mathematical%20Modeling%20of%20Derivative%20Pricing.md) process,  we use the parameter values: [mean reversion](../../../The%20Ornstein-Uhlenbeck%20(OU)%20Process.md) strength `kappa = 0.1`,  the spot variance `v0 = volatility*volatility = 0.04`,  the [mean reversion](../../../The%20Ornstein-Uhlenbeck%20(OU)%20Process.md) variance `theta=v0`,  volatility of volatility `sigma = 0.1` and the correlation between the [asset price](../../../Financial%20Markets/Financial%20Asset%20Pricing%20Theory%20Overview/Chapter%204%20-%20State%20Prices/A%20Preview%20of%20Alternative%20Formulations.md) and its variance is `rho = -0.75`.

On valuing the option using the [Heston model](.md),  we get the net present value as:
```python
# construct the Heston process

v0 = volatility*volatility  # spot variance
kappa = 0.1
theta = v0
sigma = 0.1
rho = -0.75

spot_handle = ql.QuoteHandle(
    ql.SimpleQuote(spot_price)
)
flat_ts = ql.YieldTermStructureHandle(
    ql.FlatForward(calculation_date,  risk_free_rate,  day_count)
)
dividend_yield = ql.YieldTermStructureHandle(
    ql.FlatForward(calculation_date,  dividend_rate,  day_count)
)
heston_process = ql.HestonProcess(flat_ts, 
                                  dividend_yield, 
                                  spot_handle, 
                                  v0, 
                                  kappa, 
                                  theta, 
                                  sigma, 
                                  rho)
```
```python
engine = ql.AnalyticHestonEngine(ql.HestonModel(heston_process),  0.01,   1000)
european_option.setPricingEngine(engine)
h_price = european_option.NPV()
print "The Heston model price is",  h_price
```
```python
The Heston model price is 6.5308651372
```

Performing the same calculation using the [Black-Scholes-Merton process](Valuing%20Convertible%20Bonds%20Using%20QuantLib%20Python.md),  we get:
```python
flat_vol_ts = ql.BlackVolTermStructureHandle(
    ql.BlackConstantVol(calculation_date,  calendar,  volatility,  day_count)
)
bsm_process = ql.BlackScholesMertonProcess(spot_handle,  
                                           dividend_yield,  
                                           flat_ts,  
                                           flat_vol_ts)
european_option.setPricingEngine(ql.AnalyticEuropeanEngine(bsm_process))
bs_price = european_option.NPV()
print "The Black-Scholes-Merton model price is ",  bs_price
```
```python
The Black-Scholes-Merton model price is  6.74927181246
```

The difference in the price between the two models is: `bs_price - h_price = 0.21840667525992163`. This difference is due to the [stochastic modeling](Chinese%20Financial%20System.md) of the volatility as a CIR-process.

## Conclusion

This post provided a minimal example of valuing European options using the [Heston model](.md). Comparison with the [Black-Scholes](../../../Financial%20Engineering/Mathematical%20Modeling%20of%20Derivative%20Pricing.md)-[Merton model](../../../Credit%20Markets/Credit%20Markets%20Session%205.md) is shown for instructional purpose.

   [quantlib]([Introduction%20to%20QuantLib%20Python)](http://gouthamanbalaraman.com/tag/[quantlib](Introduction%20to%20QuantLib%20Python.md).html)   [python](http://gouthamanbalaraman.com/tag/python.html)   [finance](http://gouthamanbalaraman.com/tag/finance.html)

---

**Related Post**

- [QuantLib Python]([Valuing%20Callable%20Bonds%20Using%20QuantLib%20Python) Tutorials With Examples](http://gouthamanbalaraman.com/blog/[quantlib](Introduction%20to%20QuantLib%20Python.md)-python-tutorials-with-examples.html)
- [On the Convergence of Hull White [Monte Carlo](../../../Financial%20Instruments/Lecture%20Notes-%20Financial%20Instruments/Teaching%20Note%207-Exotic%20Options%20And%20Derivative%20Pricing%20By%20Monte%20Carlo%20Simulation.md) Simulations](http://gouthamanbalaraman.com/blog/hull-white-simulation-monte-carlo-convergence.html)
- [Valuing Options on [Commodity Futures](../../../Financial%20Instruments/Financial%20Instruments%20PSET%20Solutions.md) Using [QuantLib Python](Valuing%20Callable%20Bonds%20Using%20QuantLib%20Python.md)](http://gouthamanbalaraman.com/blog/value-options-commodity-[futures](../../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%203%20-%20Futures%20Markets/Futures%20Not%20Subject%20to%20Cash-And-Carry.md)-black-formula-[quantlib](Introduction%20to%20QuantLib%20Python.md)-python.html)
- [Short [Interest Rate Model](../../../Fixed%20Income%20Asset%20Pricing/Fixed%20Income%20Lecture%20Notes/An%20Overview%20of%20the%20Vasicek%20Short%20Rate%20Model.md) [Calibration](../../../Credit%20Markets/Credit%20Markets%20Session%204.md) in [QuantLib Python](Valuing%20Callable%20Bonds%20Using%20QuantLib%20Python.md)](http://gouthamanbalaraman.com/blog/short-interest-rate-model-[calibration](../../../Credit%20Markets/Credit%20Markets%20Session%204.md)-[quantlib](Introduction%20to%20QuantLib%20Python.md).html)
- [QuantLib Python]([Valuing%20Callable%20Bonds%20Using%20QuantLib%20Python) Cookbook Announcement](http://gouthamanbalaraman.com/blog/[quantlib](Introduction%20to%20QuantLib%20Python.md)-python-cookbook-announcement.html)

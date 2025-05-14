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

Introduces an example on how to value European options using [[Valuing European Option Using the Heston Model in QuantLib Python|Heston model]] in [[Valuing Callable Bonds Using QuantLib Python|Quantlib Python]]

*Visit here for other [[[Valuing Callable Bonds Using QuantLib Python|QuantLib Python]] examples](http://gouthamanbalaraman.com/blog/[[Introduction to QuantLib Python|quantlib]]-python-tutorials-with-examples.html). If you found these posts useful,  please take a minute by providing some [feedback.](https://docs.google.com/forms/d/e/1FAIpQLSdFdJ768HKmIyJmaVRHBUJNY5NyQl6vr0GZvSkx-bUfIloNZA/viewform)*

[[Valuing European Option Using the Heston Model in QuantLib Python|Heston model]] can be used to value options by modeling the [[Risk Neutral Pricing of Options|underlying asset]] such as the stock of a company. The one major feature of the [[Valuing European Option Using the Heston Model in QuantLib Python|Heston model]] is that it inocrporates a [[Valuing European Option Using the Heston Model in QuantLib Python|stochastic volatility]] term.
$$\begin{eqnarray} dS\_t &=& \mu S\_tdt + \sqrt{V\_t} S\_t dW\_t^1 \\ dV\_t &=& \kappa(\theta-V\_t) + \sigma \sqrt{V\_t} dW\_t^2 \end{eqnarray}$$

Here :

- $S\_t$ is the asset's value at time $t$
- $\mu$ is the expected growth rate of the log normal stock value
- $V\_t$ is the variance of the asset $S\_t$
- $W\_t^1$ is the [[The Ornstein-Uhlenbeck (OU) Process|stochastic process]] governing the $S\_t$ process
- $\theta$ is the value of [[The Ornstein-Uhlenbeck (OU) Process|mean reversion]] for the variance $V\_t$
- $\kappa$ is the strength of [[The Ornstein-Uhlenbeck (OU) Process|mean reversion]]
- $\sigma$ is the volatility of volatility
- $W\_t^2$ is the [[The Ornstein-Uhlenbeck (OU) Process|stochastic process]] governing the $V\_t$ process
- The correlation between $W\_t^1$ and $W\_t^2$ is $\rho$

In contrast,  the [[Valuing Convertible Bonds Using QuantLib Python|Black-Scholes-Merton process]] assumes that the volatility is constant.

Let us consider a European call option for AAPL with a [[Call and Put Payoffs at Expiry|strike price]] of \$130 maturing on 15th Jan,  2016. Let the spot price be \$127.62. The volatility of the underlying stock is know to be 20%,  and has a dividend yield of 1.63%. We assume a short term risk free rate of 0.1%. Lets value this option as of 8th May,  2015.
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

In order to price the option using the [[Valuing European Option Using the Heston Model in QuantLib Python|Heston model]],  we first create the [[Mathematical Modeling of Derivative Pricing|Heston]] process. In order to create the [[Mathematical Modeling of Derivative Pricing|Heston]] process,  we use the parameter values: [[The Ornstein-Uhlenbeck (OU) Process|mean reversion]] strength `kappa = 0.1`,  the spot variance `v0 = volatility*volatility = 0.04`,  the [[The Ornstein-Uhlenbeck (OU) Process|mean reversion]] variance `theta=v0`,  volatility of volatility `sigma = 0.1` and the correlation between the [[A Preview of Alternative Formulations|asset price]] and its variance is `rho = -0.75`.

On valuing the option using the [[Valuing European Option Using the Heston Model in QuantLib Python|Heston model]],  we get the net present value as:
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

Performing the same calculation using the [[Valuing Convertible Bonds Using QuantLib Python|Black-Scholes-Merton process]],  we get:
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

The difference in the price between the two models is: `bs_price - h_price = 0.21840667525992163`. This difference is due to the [[Chinese Financial System|stochastic modeling]] of the volatility as a CIR-process.

## Conclusion

This post provided a minimal example of valuing European options using the [[Valuing European Option Using the Heston Model in QuantLib Python|Heston model]]. Comparison with the [[Mathematical Modeling of Derivative Pricing|Black-Scholes]]-[[Credit Markets Session 5|Merton model]] is shown for instructional purpose.

   [[[Introduction to QuantLib Python|quantlib]]](http://gouthamanbalaraman.com/tag/[[Introduction to QuantLib Python|quantlib]].html)   [python](http://gouthamanbalaraman.com/tag/python.html)   [finance](http://gouthamanbalaraman.com/tag/finance.html)

---

**Related Post**

- [[[Valuing Callable Bonds Using QuantLib Python|QuantLib Python]] Tutorials With Examples](http://gouthamanbalaraman.com/blog/[[Introduction to QuantLib Python|quantlib]]-python-tutorials-with-examples.html)
- [On the Convergence of Hull White [[Teaching Note 7-Exotic Options And Derivative Pricing By Monte Carlo Simulation|Monte Carlo]] Simulations](http://gouthamanbalaraman.com/blog/hull-white-simulation-monte-carlo-convergence.html)
- [Valuing Options on [[Financial Instruments PSET Solutions|Commodity Futures]] Using [[Valuing Callable Bonds Using QuantLib Python|QuantLib Python]]](http://gouthamanbalaraman.com/blog/value-options-commodity-[[Futures Not Subject to Cash-And-Carry|futures]]-black-formula-[[Introduction to QuantLib Python|quantlib]]-python.html)
- [Short [[An Overview of the Vasicek Short Rate Model|Interest Rate Model]] [[Credit Markets Session 4|Calibration]] in [[Valuing Callable Bonds Using QuantLib Python|QuantLib Python]]](http://gouthamanbalaraman.com/blog/short-interest-rate-model-[[Credit Markets Session 4|calibration]]-[[Introduction to QuantLib Python|quantlib]].html)
- [[[Valuing Callable Bonds Using QuantLib Python|QuantLib Python]] Cookbook Announcement](http://gouthamanbalaraman.com/blog/[[Introduction to QuantLib Python|quantlib]]-python-cookbook-announcement.html)

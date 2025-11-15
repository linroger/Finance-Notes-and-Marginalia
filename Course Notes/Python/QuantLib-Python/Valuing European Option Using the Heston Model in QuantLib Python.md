---
academic_level: graduate
aliases:
- Heston Option Pricing
- QuantLib Heston
description: Introduces an example on how to value European options using Heston model
  in Quantlib Python
enhanced: true
enhancement_date: '2025-11-06'
enhancement_id: batch09-000036
key_concepts:
- Black-Scholes option pricing model and continuous-time finance
- Options Greeks and sensitivity analysis for risk management
- Duration analysis and interest rate risk management
- Convexity adjustments and yield curve sensitivity
- Discounted cash flow (DCF) valuation methodology
- Net present value (NPV) and investment evaluation
- Weighted Average Cost of Capital (WACC) and firm valuation
- Value at Risk (VaR) and tail risk measurement
- Expected shortfall and coherent risk measures
- Vasicek model and mean-reverting interest rates
- QuantLib library and quantitative finance implementation
- Volatility modeling and estimation techniques
- Correlation analysis and dependency structures
- Risk preference theory and utility functions
- 'Valuation Methods: DCF, Comps, and Precedents'
- Ito's Lemma and Lognormal Asset Price Dynamics
- Risk-Neutral Valuation in Option Pricing
- Value at Risk and Expected Shortfall
- Vasicek Interest Rate Model and Mean Reversion
- Short Rate Models and Term Structure Dynamics
- Company Valuation and Multiple Analysis
- Comparable Company Analysis and Trading Multiples
- 'Greeks: Delta, Gamma, Theta, and Vega Hedging'
- Ornstein-Uhlenbeck Process in Finance
- Black-Scholes Option Pricing Model and Its Applications
- Options Trading Strategies and Risk Management
- Stress Testing and Extreme Value Analysis
- Fama-French Factors and Style Analysis
- Risk Measurement and VaR Backtesting
- Contango, Backwardation, and Roll Yield
- Futures and Forward Contracts in Financial Markets
- Hedge Strategies and Basis Risk Management
- Option Valuation and Exercise Strategies
- Factor Models and Asset Pricing
- Arbitrage Pricing Theory and Multi-Factor Models
professional_application: theoreti
source: https://gouthamanbalaraman.com/blog/valuing-european-option-heston-model-quantLib.html
status: active
tags:
- affine-term-structure
- array-computing
- binomial-model
- black-scholes-model
- capital-budgeting
- capital-structure
- caplet
- cash-flow-modeling
- charting
- coherent-risk-measure
- conditional-var
- continuous-time-pricing
- convexity-adjustment
- cost-of-capital
- credit-rating
- put-options
- bsm-model
- leveraged-buyout
- hull-white
- sum-of-parts
- european-options
- call-options
- price-to-earnings
- cir-model
- black-scholes-formula
- butterfly-spreads
- strangles
- momentum
- expected-shortfall
- straddles
- basis-risk
- parametric-var
- partial-differential-equation
- var-methodologies
- historical-var
- extreme-value-theory
- book-to-market
- mean-reversion
- contango
- risk-neutral-valuation
- backwardation
- lognormal-models
- covered-calls
- volatility-analysis
- style-analysis
- short-rate-models
- option-strategies
- stress-testing
- mathematical-finance
- ornstein-uhlenbeck
- comparable-analysis
- clearinghouse
- investment-analysis
- economic-value-added
- quantitative-finance
- marking-to-market
- value-at-risk
- arbitrage-pricing-theory
- ito-calculus
- hedge-ratio
- multi-factor-models
- trading-multiples
- iron-condors
- option-pricing
- protective-puts
- market-price-of-risk
- volatility-surface
- financial-markets
- size-effect
- factor-models
- precedent-transactions
- value-factor
- vasicek-model
- lognormal-distribution
- ipo-valuation
- monte-carlo-var
- risk-management
- dcf-analysis
- convergence
- options-trading
- var-backtesting
- futures-contracts
- market-multiple
- roll-yield
- apt
- risk-premium
- forward-contracts
- fama-french
title: Valuing European Option Using the Heston Model in QuantLib Python
type: note
---
--



# Valuing European Option Using the Heston Model in QuantLib Python

Introduces an example on how to value European options using Heston model in Quantlib Python

*Visit here for other QuantLib Python examples](http://gouthamanbalaraman.com/blog/quantlib-python-tutorials-with-examples.html). If you found these posts useful,  please take a minute by providing some feedback.*

Heston model can be used to value options by modeling the underlying asset such as the stock of a company. The one major feature of the Heston model is that it inocrporates a stochastic volatility term.
$$\begin{eqnarray} dS\_t &=& \mu S\_tdt + \sqrt{V\_t} S\_t dW\_t[^1] \\ dV\_t &=& \kappa(\theta-V\_t) + \sigma \sqrt{V\_t} dW\_t[^2] \end{eqnarray}$$

Here :

- $S\_t$ is the asset's value at time $t$
- $\mu$ is the expected growth rate of the log normal stock value
- $V\_t$ is the variance of the asset $S\_t$
- $W\_t[^1]$ is the stochastic process%20Process.md) governing the $S\_t$ process
- $\theta$ is the value of mean reversion%20Process.md) for the variance $V\_t$
- $\kappa$ is the strength of mean reversion%20Process.md)
- $\sigma$ is the volatility of volatility
- $W\_t[^2]$ is the stochastic process%20Process.md) governing the $V\_t$ process
- The correlation between $W\_t[^1]$ and $W\_t[^2]$ is $\rho$

In contrast,  the Black-Scholes-Merton process assumes that the volatility is constant.

Let us consider a European call option for AAPL with a strike price of \$130 maturing on 15th Jan,  2016. Let the spot price be \$127.62. The volatility of the underlying stock is know to be 20%,  and has a dividend yield of 1.63%. We assume a short term risk free rate of 0.1%. Lets value this option as of 8th May,  2015.
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

In order to price the option using the Heston model,  we first create the Heston process. In order to create the Heston process,  we use the parameter values: mean reversion%20Process.md) strength `kappa = 0.1`,  the spot variance `v0 = volatility*volatility = 0.04`,  the mean reversion%20Process.md) variance `theta=v0`,  volatility of volatility `sigma = 0.1` and the correlation between the asset price and its variance is `rho = -0.75`.

On valuing the option using the Heston model,  we get the net present value as:
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

Performing the same calculation using the Black-Scholes-Merton process,  we get:
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

The difference in the price between the two models is: `bs_price - h_price = 0.21840667525992163`. This difference is due to the stochastic modeling of the volatility as a CIR-process.

## Conclusion

This post provided a minimal example of valuing European options using the Heston model. Comparison with the Black-Scholes-Merton model is shown for instructional purpose.

   quantlib](http://gouthamanbalaraman.com/tag/quantlib.html)   python   finance

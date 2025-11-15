---
academic_level: graduate
aliases:
- Hull-White model
- QuantLib simulation
description: Discusses simulation of the Hull White interest rate term structure model
  in QuantLib Python
enhanced: true
enhancement_date: '2025-11-06'
enhancement_id: batch09-000046
key_concepts:
- Black-Scholes option pricing model and continuous-time finance
- Options Greeks and sensitivity analysis for risk management
- Duration analysis and interest rate risk management
- Convexity adjustments and yield curve sensitivity
- Discounted cash flow (DCF) valuation methodology
- Weighted Average Cost of Capital (WACC) and firm valuation
- Value at Risk (VaR) and tail risk measurement
- Expected shortfall and coherent risk measures
- Hull-White model and Gaussian HJM framework
- QuantLib library and quantitative finance implementation
- Alpha generation and active portfolio management
- Alpha generation and active return measurement
- Risk preference theory and utility functions
- 'Valuation Methods: DCF, Comps, and Precedents'
- Yield Curve Analysis and Bond Valuation
- Value at Risk and Expected Shortfall
- Vasicek Interest Rate Model and Mean Reversion
- Short Rate Models and Term Structure Dynamics
- Company Valuation and Multiple Analysis
- Variance Reduction Techniques in Monte Carlo Methods
- Capital Asset Pricing Model and Beta Analysis
- Forward Rates and Curve Construction Methods
- Swap Market Mechanisms and Pricing
- Comparable Company Analysis and Trading Multiples
- 'Greeks: Delta, Gamma, Theta, and Vega Hedging'
- Ornstein-Uhlenbeck Process in Finance
- Cost of Equity and Expected Returns
- Stochastic Integration and Path-Dependent Options
- Security Market Line and Risk-Return Tradeoff
- Options Trading Strategies and Risk Management
- Stress Testing and Extreme Value Analysis
- Credit Default Swaps and Credit Risk Transfer
- Fama-French Factors and Style Analysis
- Risk Measurement and VaR Backtesting
- Contango, Backwardation, and Roll Yield
- Futures and Forward Contracts in Financial Markets
- Factor Models and Asset Pricing
- Hedge Strategies and Basis Risk Management
- Interest Rate Swaps and Currency Swap Structures
- Term Structure of Interest Rates and Yield Curves
- Option Valuation and Exercise Strategies
- Monte Carlo Simulation Methods for Derivative Pricing
- Arbitrage Pricing Theory and Multi-Factor Models
professional_application: theoreti
source: https://gouthamanbalaraman.com/blog/hull-white-simulation-quantlib-python.html
status: active
tags:
- array-computing
- asset-allocation
- binomial-model
- black-scholes-model
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
- data-visualization
- control-variates
- leveraged-buyout
- exotic-options
- hull-white
- call-options
- cir-model
- butterfly-spreads
- dcf-analysis
- expected-shortfall
- straddles
- extreme-value-theory
- book-to-market
- backwardation
- style-analysis
- option-strategies
- yield-curve
- capital-asset-pricing-model
- clearinghouse
- interpolation
- overnight-indexed-swaps
- arbitrage-pricing-theory
- monte-carlo-simulation
- hedge-ratio
- market-price-of-risk
- value-factor
- vasicek-model
- sharpe-ratio
- monte-carlo-var
- options-trading
- forward-contracts
- fama-french
- forward-rates
- price-to-earnings
- parametric-var
- lognormal-models
- var-methodologies
- historical-var
- mean-reversion
- contango
- random-walks
- quantitative-finance
- forward-curve
- currency-swaps
- systematic-risk
- protective-puts
- alpha
- security-market-line
- curve-fitting
- idiosyncratic-risk
- roll-yield
- beta
- risk-premium
- spot-rates
- put-options
- affine-term-structure
- capm
- momentum
- basis-risk
- market-risk-premium
- antithetic-variates
- term-structure
- covered-calls
- swap-rate
- sofr
- stress-testing
- mathematical-finance
- ornstein-uhlenbeck
- par-yield
- comparable-analysis
- investment-analysis
- economic-value-added
- path-dependency
- value-at-risk
- factor-models
- convergence
- var-backtesting
- variance-reduction
- stochastic-integration
- sum-of-parts
- yield-curve-shocks
- strangles
- short-rate-models
- least-squares-mc
- swap-spread
- efficient-frontier
- marking-to-market
- total-return-swaps
- libor
- multi-factor-models
- trading-multiples
- iron-condors
- financial-markets
- size-effect
- basis-swaps
- precedent-transactions
- interest-rate-swaps
- ipo-valuation
- market-multiple
- futures-contracts
- quasi-monte-carlo
- apt
- bootstrap-method
- credit-default-swaps
title: Hull White Term Structure Simulations with QuantLib Python
type: note
---
--



# Hull White Term Structure Simulations with QuantLib Python
Discusses simulation of the Hull White interest rate term structure model in QuantLib Python

*Visit here for other QuantLib Python examples](http://gouthamanbalaraman.com/blog/quantlib-python-tutorials-with-examples.html). If you found these posts useful,  please take a minute by providing some feedback.*

The Hull-White Short Rate Model is defined as:
$$ dr\_t = (\theta(t) - a r\_t)dt + \sigma dW\_t $$

where $a$ and $ \sigma $ are constants,  and $\theta(t)$ is chosen in order to fit the input term structure of interest rates. Here we use QuantLib to show how to simulate the Hull-White model and investigate some of the properties.

We import the libraries and set things up as shown below:

In \[1\]:
```latex
import QuantLib as ql
import matplotlib.pyplot as plt
import numpy as np
% matplotlib inline
```

The constants that we use for this example is all defined as shown below. Variables `sigma` and `a` are the constants that define the Hull-White model. In the simulation,  we discretize the time span of `length` 30 years into 360 intervals (one per month) as defined by the `timestep` variable. For simplicity we will use a constant forward rate term structure as an input. It is straight forward to swap with another term structure here.

In \[2\]:
```latex
sigma = 0.1
a = 0.1
timestep = 360
length = 30 # in years
forward_rate = 0.05
day_count = ql.Thirty360()
todays_date = ql.Date(15,  1,  2015)
```

In \[3\]:
```latex
ql.Settings.instance().evaluationDate = todays_date

spot_curve = ql.FlatForward(todays_date,  ql.QuoteHandle(ql.SimpleQuote(forward_rate)),  day_count)
spot_curve_handle = ql.YieldTermStructureHandle(spot_curve)
```

In \[4\]:
```latex
hw_process = ql.HullWhiteProcess(spot_curve_handle,  a,  sigma)
rng = ql.GaussianRandomSequenceGenerator(ql.UniformRandomSequenceGenerator(timestep,  ql.UniformRandomGenerator()))
seq = ql.GaussianPathGenerator(hw_process,  length,  timestep,  rng,  False)
```

The Hull-White process is constructed by passing the term-structure,  `a` and `sigma`. To create the path generator,  one has to provide a random sequence generator along with other simulation inputs such as `timestep` and \`length.

A function to generate paths can be written as shown below:

In \[5\]:
```latex
def generate_paths(num_paths,  timestep):
    arr = np.zeros((num_paths,  timestep+1))
    for i in range(num_paths):
        sample_path = seq.next()
        path = sample_path.value()
        time = [path.time(j) for j in range(len(path))]
        value = [path[j] for j in range(len(path))]
        arr[i,  :] = np.array(value)
    return np.array(time),  arr
```

The simulation of the short rates look as shown below:

In \[6\]:
```latex
num_paths = 10
time,  paths = generate_paths(num_paths,  timestep)
for i in range(num_paths):
    plt.plot(time,  paths[i,  :],  lw=0.8,  alpha=0.6)
plt.title("Hull-White Short Rate Simulation")
plt.show()
```

 !500
The short rate $r(t)$ is given a distribution with the properties:
$$ E\{r(t) | F\_s\} = r(s)e^{-a(t-s)} + \alpha(t) - \alpha(s)e^{-a(t-s)} $$ $$ Var\{ r(t) | F\_s \} = \frac{\sigma[^2]}{2a} [1 - e^{-2a(t-s)}] $$ where $$ \alpha(t) = f^M(0,  t) + \frac{\sigma[^2]} {2a[^2]}(1-e^{-at})[^2]$$

as shown in Brigo & Mercurio's book on Interest Rate Models.

In \[7\]:
```latex
num_paths = 1000
time,  paths = generate_paths(num_paths,  timestep)
```

The mean and variance compared between the simulation (red dotted line) and theory (blue line).

In \[8\]:
```latex
vol = [np.var(paths[:,  i]) for i in range(timestep+1)]
plt.plot(time,  vol,  "r-.",  lw=3,  alpha=0.6)
plt.plot(time, sigma*sigma/(2*a)*(1.0-np.exp(-2.0*a*np.array(time))),  "b-",  lw=2,  alpha=0.5)
plt.title("Variance of Short Rates")
```

Out\[8\]:
```latex
<matplotlib.text.Text at 0x7f555d561ad0>
```

 !500
In \[9\]:
```latex
def alpha(forward,  sigma,  a,  t):
    return forward + 0.5* np.power(sigma/a*(1.0 - np.exp(-a*t)),  2)

avg = [np.mean(paths[:,  i]) for i in range(timestep+1)]
plt.plot(time,  avg,  "r-.",  lw=3,  alpha=0.6)
plt.plot(time, alpha(forward_rate,  sigma,  a,  time),  "b-",  lw=2,  alpha=0.6)
plt.title("Mean of Short Rates")
```

Out\[9\]:
```latex
<matplotlib.text.Text at 0x7f555d6a9e10>
```

 !500

## Conclusion

This post shows how to simulate Hull-White short rate model using QuantLib Python. You can download the ipython notebook on Hull-White simulations.

   quantlib](http://gouthamanbalaraman.com/tag/quantlib.html)   python   finance

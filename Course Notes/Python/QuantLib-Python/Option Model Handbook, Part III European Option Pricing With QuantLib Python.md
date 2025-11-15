---
academic_level: graduate
aliases:
- Option Pricing with QuantLib
- QuantLib European Options
description: Demonstrates how to price European options using QuantLib Python. Methods
  using Black-Scholes-Merton formula and binomial tree will be discussed.
enhanced: true
enhancement_date: '2025-11-06'
enhancement_id: batch09-000038
key_concepts:
- Black-Scholes option pricing model and continuous-time finance
- Binomial option pricing model and lattice methods
- Options Greeks and sensitivity analysis for risk management
- Convexity adjustments and yield curve sensitivity
- Discounted cash flow (DCF) valuation methodology
- Weighted Average Cost of Capital (WACC) and firm valuation
- Value at Risk (VaR) and tail risk measurement
- Expected shortfall and coherent risk measures
- QuantLib library and quantitative finance implementation
- Alpha generation and active portfolio management
- Volatility modeling and estimation techniques
- Alpha generation and active return measurement
- Risk preference theory and utility functions
- 'Valuation Methods: DCF, Comps, and Precedents'
- Ito's Lemma and Lognormal Asset Price Dynamics
- Risk-Neutral Valuation in Option Pricing
- Value at Risk and Expected Shortfall
- Vasicek Interest Rate Model and Mean Reversion
- Short Rate Models and Term Structure Dynamics
- Company Valuation and Multiple Analysis
- Capital Asset Pricing Model and Beta Analysis
- Comparable Company Analysis and Trading Multiples
- 'Greeks: Delta, Gamma, Theta, and Vega Hedging'
- Ornstein-Uhlenbeck Process in Finance
- Cost of Equity and Expected Returns
- Black-Scholes Option Pricing Model and Its Applications
- Security Market Line and Risk-Return Tradeoff
- Options Trading Strategies and Risk Management
- Stress Testing and Extreme Value Analysis
- Lattice Methods and Recombining Trees in Derivatives Pricing
- Fama-French Factors and Style Analysis
- Risk Measurement and VaR Backtesting
- Contango, Backwardation, and Roll Yield
- Futures and Forward Contracts in Financial Markets
- Binomial Option Pricing Model for Discrete Time Valuation
- Hedge Strategies and Basis Risk Management
- American Option Pricing and Early Exercise Premium
- Option Valuation and Exercise Strategies
- Factor Models and Asset Pricing
- Arbitrage Pricing Theory and Multi-Factor Models
professional_application: theoreti
source: https://gouthamanbalaraman.com/blog/european-option-binomial-tree-quantlib-python.html
status: active
tags:
- asset-allocation
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
- data-visualization
- leveraged-buyout
- hull-white
- call-options
- cir-model
- butterfly-spreads
- dcf-analysis
- expected-shortfall
- binomial-tree
- straddles
- extreme-value-theory
- american-options
- partial-differential-equation
- book-to-market
- risk-neutral-valuation
- backwardation
- volatility-analysis
- style-analysis
- option-strategies
- capital-asset-pricing-model
- clearinghouse
- arbitrage-pricing-theory
- hedge-ratio
- market-price-of-risk
- volatility-surface
- value-factor
- vasicek-model
- sharpe-ratio
- monte-carlo-var
- options-trading
- forward-contracts
- fama-french
- price-to-earnings
- bsm-model
- black-scholes-formula
- parametric-var
- lognormal-models
- var-methodologies
- historical-var
- mean-reversion
- contango
- quantitative-finance
- crr-model
- systematic-risk
- protective-puts
- alpha
- security-market-line
- idiosyncratic-risk
- roll-yield
- beta
- risk-premium
- put-options
- affine-term-structure
- multi-period-binomial
- capm
- momentum
- basis-risk
- market-risk-premium
- discrete-time-pricing
- covered-calls
- stress-testing
- mathematical-finance
- ornstein-uhlenbeck
- comparable-analysis
- investment-analysis
- economic-value-added
- value-at-risk
- factor-models
- risk-management
- convergence
- var-backtesting
- sum-of-parts
- european-options
- lattice-models
- strangles
- cox-ross-rubinstein
- short-rate-models
- optional-exercise
- efficient-frontier
- marking-to-market
- binomial-option-pricing
- multi-factor-models
- ito-calculus
- trading-multiples
- iron-condors
- option-pricing
- financial-markets
- size-effect
- precedent-transactions
- lognormal-distribution
- ipo-valuation
- market-multiple
- ' recombining-trees'
- futures-contracts
- apt
title: Option Model Handbook,  Part III European Option Pricing With QuantLib Python
type: note
---
--



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

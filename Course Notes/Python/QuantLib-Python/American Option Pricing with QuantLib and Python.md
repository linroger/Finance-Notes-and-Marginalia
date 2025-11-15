---
academic_level: graduate
aliases:
- AAPL Option Pricing
- Option Valuation
description: This post explains valuing American Options using QuantLib and Python
enhanced: true
enhancement_date: '2025-11-06'
enhancement_id: batch09-000045
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
- Company Valuation and Multiple Analysis
- Capital Asset Pricing Model and Beta Analysis
- Credit Risk Management and Default Probability
- Expected Loss and Loss Given Default Models
- Comparable Company Analysis and Trading Multiples
- 'Greeks: Delta, Gamma, Theta, and Vega Hedging'
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
- Credit Spreads and Rating Migration Analysis
- Factor Models and Asset Pricing
- Arbitrage Pricing Theory and Multi-Factor Models
professional_application: theoreti
source: http://gouthamanbalaraman.com/blog/american-option-pricing-quantlib-python.html
status: active
tags:
- american-derivatives
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
- leveraged-buyout
- call-options
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
- unexpected-loss
- capital-asset-pricing-model
- clearinghouse
- arbitrage-pricing-theory
- hedge-ratio
- volatility-surface
- loss-given-default
- value-factor
- sharpe-ratio
- monte-carlo-var
- options-trading
- forward-contracts
- fama-french
- price-to-earnings
- bsm-model
- recovery-rate
- black-scholes-formula
- parametric-var
- var-methodologies
- historical-var
- contango
- expected-loss
- crr-model
- systematic-risk
- protective-puts
- alpha
- security-market-line
- probabilty-of-default
- idiosyncratic-risk
- roll-yield
- beta
- put-options
- multi-period-binomial
- capm
- momentum
- basis-risk
- market-risk-premium
- discrete-time-pricing
- covered-calls
- ' exposure-at-default'
- stress-testing
- rating-migration
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
- optional-exercise
- efficient-frontier
- credit-migration
- default-probability
- marking-to-market
- binomial-option-pricing
- credit-spreads
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
title: American Option Pricing with QuantLib and Python
type: note
---
--



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

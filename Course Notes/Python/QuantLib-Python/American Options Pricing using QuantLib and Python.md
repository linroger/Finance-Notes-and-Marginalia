---
academic_level: graduate
aliases:
- AAPL
- Option Pricing
- QuantLib Python
enhanced: true
enhancement_date: '2025-11-06'
enhancement_id: batch09-000048
key_concepts:
- Black-Scholes option pricing model and continuous-time finance
- Binomial option pricing model and lattice methods
- Monte Carlo simulation for derivatives pricing and risk management
- Options Greeks and sensitivity analysis for risk management
- Convexity adjustments and yield curve sensitivity
- Discounted cash flow (DCF) valuation methodology
- Weighted Average Cost of Capital (WACC) and firm valuation
- Value at Risk (VaR) and tail risk measurement
- Expected shortfall and coherent risk measures
- Hull-White model and Gaussian HJM framework
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
- Variance Reduction Techniques in Monte Carlo Methods
- Capital Asset Pricing Model and Beta Analysis
- Credit Risk Management and Default Probability
- Expected Loss and Loss Given Default Models
- Comparable Company Analysis and Trading Multiples
- 'Greeks: Delta, Gamma, Theta, and Vega Hedging'
- Ornstein-Uhlenbeck Process in Finance
- Cost of Equity and Expected Returns
- Stochastic Integration and Path-Dependent Options
- Forward Curves and Roll Strategies
- Black-Scholes Option Pricing Model and Its Applications
- Security Market Line and Risk-Return Tradeoff
- Options Trading Strategies and Risk Management
- Stress Testing and Extreme Value Analysis
- Lattice Methods and Recombining Trees in Derivatives Pricing
- Fama-French Factors and Style Analysis
- Risk Measurement and VaR Backtesting
- Contango, Backwardation, and Roll Yield
- Futures and Forward Contracts in Financial Markets
- Factor Models and Asset Pricing
- Binomial Option Pricing Model for Discrete Time Valuation
- Hedge Strategies and Basis Risk Management
- American Option Pricing and Early Exercise Premium
- Seasonality and Convenience Yield
- Commodity Markets and Energy Derivatives
- Option Valuation and Exercise Strategies
- Credit Spreads and Rating Migration Analysis
- Monte Carlo Simulation Methods for Derivative Pricing
- Arbitrage Pricing Theory and Multi-Factor Models
professional_application: theoreti
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
- commodity-derivatives
- commodity-futures
- conditional-var
- continuous-time-pricing
- convexity-adjustment
- control-variates
- leveraged-buyout
- exotic-options
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
- energy-derivatives
- style-analysis
- option-strategies
- unexpected-loss
- capital-asset-pricing-model
- clearinghouse
- arbitrage-pricing-theory
- monte-carlo-simulation
- hedge-ratio
- market-price-of-risk
- volatility-surface
- loss-given-default
- roll-strategies
- value-factor
- vasicek-model
- sharpe-ratio
- forward-curves
- monte-carlo-var
- options-trading
- commodity-trading
- forward-contracts
- fama-french
- price-to-earnings
- bsm-model
- recovery-rate
- black-scholes-formula
- parametric-var
- lognormal-models
- var-methodologies
- historical-var
- mean-reversion
- contango
- random-walks
- expected-loss
- quantitative-finance
- crr-model
- systematic-risk
- protective-puts
- alpha
- security-market-line
- probabilty-of-default
- idiosyncratic-risk
- storage-costs
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
- antithetic-variates
- covered-calls
- ' exposure-at-default'
- stress-testing
- mathematical-finance
- ornstein-uhlenbeck
- rating-migration
- comparable-analysis
- economic-value-added
- path-dependency
- value-at-risk
- metals-trading
- factor-models
- convenience-yield
- agricultural-commodities
- risk-management
- convergence
- var-backtesting
- variance-reduction
- stochastic-integration
- sum-of-parts
- european-options
- seasonality
- lattice-models
- strangles
- cox-ross-rubinstein
- short-rate-models
- least-squares-mc
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
- size-effect
- precedent-transactions
- lognormal-distribution
- ipo-valuation
- market-multiple
- ' recombining-trees'
- futures-contracts
- quasi-monte-carlo
- apt
title: American Option Pricing with QuantLib and Python
type: note
---
--



# American Options Pricing using QuantLib and Python

This post explains valuing American Options using QuantLib and Python

_Visit here for other QuantLib Python examples](http://gouthamanbalaraman.com/blog/quantlib-python-tutorials-with-examples.html). If you found these posts useful,  please take a minute by providing some  feedback._

I wrote about pricing European options using [QuantLib](http://gouthamanbalaraman.com/blog/european-option-binomial-tree-quantlib-python.html) in an earlier post. Since then,  I have received many questions from readers on how to extend this to price American options. So here is a modified example on pricing American options using QuantLib. The idea is very similar to European Option construction. Lets take a look at the details below. In this post,  I will price both an European option and an American option side by side.
```python
import QuantLib as ql 
import matplotlib.pyplot as plt
%matplotlib inline
ql.__version__
```

'1.9.2'

Let us consider a European and an American call option for AAPL with a strike price of $130 maturing on 15th Jan,    2016. Let the spot price be $127.62. The volatility of the underlying stock is known to be 20%,  and has a dividend yield of 1.63%. Lets value these options as of 8th May,  2015.
```python
# option data
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

We construct the European and American options here. The main difference here is in the Exercise type. One has to use `AmericanExercise` instead of `EuropeanExercise` to pass into the `VanillaOption` to construct an American option.
```python
payoff = ql.PlainVanillaPayoff(option_type,    strike_price)
settlement = calculation_date

am_exercise = ql.AmericanExercise(settlement,    maturity_date)
american_option = ql.VanillaOption(payoff,    am_exercise)

eu_exercise = ql.EuropeanExercise(maturity_date)
european_option = ql.VanillaOption(payoff,    eu_exercise)

The Black-Scholes-Merton process is constructed here.

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

The value of the American option can be computed using a Binomial Engine using the CRR approach.

steps = 200
binomial_engine = ql.BinomialVanillaEngine(bsm_process,    "crr",    steps)
american_option.setPricingEngine(binomial_engine)
print (american_option.NPV())
```
```python
6.84210328728556
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

# theoretical European option price
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
bi
```

 !500

**Related Post**

- QuantLib Python Tutorials With Examples](http://gouthamanbalaraman.com/blog/quantlib-python-tutorials-with-examples.html)
- On the Convergence of Hull White [Monte Carlo Simulations](http://gouthamanbalaraman.com/blog/hull-white-simulation-monte-carlo-convergence.html)
- Valuing Options on [Commodity Futures Using QuantLib Python](http://gouthamanbalaraman.com/blog/value-options-commodity-futures-black-formula-quantlib-python.html)
- Short [Interest Rate Model Calibration in QuantLib Python](http://gouthamanbalaraman.com/blog/short-interest-rate-model-calibration-quantlib.html)
- QuantLib Python Cookbook Announcement](http://gouthamanbalaraman.com/blog/quantlib-python-cookbook-announcement.html)

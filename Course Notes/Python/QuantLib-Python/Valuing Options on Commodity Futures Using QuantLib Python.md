---
academic_level: graduate
aliases:
- Commodity Option Pricing
- QuantLib Example
description: Describes how to value options on commodity futures contract using the
  Black formula in QuantLib Python
enhanced: true
enhancement_date: '2025-11-06'
enhancement_id: batch09-000040
key_concepts:
- Black-Scholes option pricing model and continuous-time finance
- Monte Carlo simulation for derivatives pricing and risk management
- Options Greeks and sensitivity analysis for risk management
- Duration analysis and interest rate risk management
- Convexity adjustments and yield curve sensitivity
- Discounted cash flow (DCF) valuation methodology
- Weighted Average Cost of Capital (WACC) and firm valuation
- Credit default swaps (CDS) and credit risk modeling
- Hull-White model and Gaussian HJM framework
- QuantLib library and quantitative finance implementation
- Volatility modeling and estimation techniques
- Risk preference theory and utility functions
- Sensitivity analysis and Greeks calculation
- 'Valuation Methods: DCF, Comps, and Precedents'
- Ito's Lemma and Lognormal Asset Price Dynamics
- Risk-Neutral Valuation in Option Pricing
- Value at Risk and Expected Shortfall
- Vasicek Interest Rate Model and Mean Reversion
- Short Rate Models and Term Structure Dynamics
- Company Valuation and Multiple Analysis
- Variance Reduction Techniques in Monte Carlo Methods
- Credit Risk Management and Default Probability
- Expected Loss and Loss Given Default Models
- Swap Market Mechanisms and Pricing
- Comparable Company Analysis and Trading Multiples
- 'Greeks: Delta, Gamma, Theta, and Vega Hedging'
- Ornstein-Uhlenbeck Process in Finance
- Stochastic Integration and Path-Dependent Options
- Forward Curves and Roll Strategies
- Black-Scholes Option Pricing Model and Its Applications
- Options Trading Strategies and Risk Management
- Stress Testing and Extreme Value Analysis
- Credit Default Swaps and Credit Risk Transfer
- Fama-French Factors and Style Analysis
- Risk Measurement and VaR Backtesting
- Contango, Backwardation, and Roll Yield
- Futures and Forward Contracts in Financial Markets
- Bond Pricing and Yield to Maturity Analysis
- Fixed Income Securities and Credit Quality
- Factor Models and Asset Pricing
- Hedge Strategies and Basis Risk Management
- Interest Rate Swaps and Currency Swap Structures
- Seasonality and Convenience Yield
- Commodity Markets and Energy Derivatives
- Option Valuation and Exercise Strategies
- Credit Spreads and Rating Migration Analysis
- Monte Carlo Simulation Methods for Derivative Pricing
- Government and Corporate Bond Markets
- Arbitrage Pricing Theory and Multi-Factor Models
professional_application: theoreti
source: http://gouthamanbalaraman.com/blog/value-options-commodity-futures-black-formula-quantlib-python.html
status: active
tags:
- binomial-model
- black-scholes-model
- bond-option
- capital-structure
- caplet
- cash-flow-modeling
- cds
- commodity-derivatives
- commodity-futures
- continuous-time-pricing
- convexity
- convexity-adjustment
- cost-of-capital
- counterparty-risk
- credit-default-swap
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
- partial-differential-equation
- risk-neutral-valuation
- backwardation
- volatility-analysis
- energy-derivatives
- style-analysis
- bond-pricing
- option-strategies
- corporate-bonds
- unexpected-loss
- clearinghouse
- overnight-indexed-swaps
- arbitrage-pricing-theory
- monte-carlo-simulation
- hedge-ratio
- market-price-of-risk
- volatility-surface
- loss-given-default
- roll-strategies
- value-factor
- vasicek-model
- dirty-price
- forward-curves
- monte-carlo-var
- options-trading
- coupon-bonds
- commodity-trading
- forward-contracts
- yield-to-maturity
- fama-french
- price-to-earnings
- bsm-model
- recovery-rate
- zero-coupon-bonds
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
- currency-swaps
- protective-puts
- government-bonds
- probabilty-of-default
- credit-default-swaps
- storage-costs
- roll-yield
- risk-premium
- put-options
- affine-term-structure
- momentum
- basis-risk
- antithetic-variates
- covered-calls
- swap-rate
- sofr
- ' exposure-at-default'
- stress-testing
- mathematical-finance
- ornstein-uhlenbeck
- rating-migration
- comparable-analysis
- investment-analysis
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
- stochastic-integration
- variance-reduction
- sum-of-parts
- european-options
- clean-price
- seasonality
- strangles
- conditional-var
- fixed-income
- short-rate-models
- least-squares-mc
- swap-spread
- credit-migration
- default-probability
- marking-to-market
- total-return-swaps
- libor
- credit-spreads
- multi-factor-models
- ito-calculus
- trading-multiples
- iron-condors
- option-pricing
- financial-markets
- size-effect
- basis-swaps
- precedent-transactions
- interest-rate-swaps
- lognormal-distribution
- ipo-valuation
- market-multiple
- futures-contracts
- quasi-monte-carlo
- apt
- current-yield
title: Valuing Options on Commodity Futures Using QuantLib Python
type: note
---
--



# Valuing Options on Commodity Futures Using QuantLib Python
Describes how to value options on commodity futures contract using the Black formula in QuantLib Python

The Black-Scholes equation is the well known model to price equity European options. In the case of equities,  the spot price fluctuates and hence the intuition to model as a stochastic process%20Process.md) makes sense. In the case of commodities,  however,  the spot price does not fluctuate as much,  and hence cannot be modeled as a stochastic process%20Process.md) to value options on commodities. In the 1976 paper \[1\],  Fischer Black addressed this problem by modeling the futures price,  which demonstrates fluctuations,  as the lognormal stochastic process.

The futures price at time $t$,  $F_{t}$ with a is modeled as:
$$
d F_{t}  = \left(\sigma\right)_{t} F_{t} d W
$$

where $\left(\sigma\right)_{t}$ is the volatility of the underlying,  and $d W$ is the Weiner process.

The value of an option at strike $K$,  maturing at $T$,  risk free rate $r$ with volatility $\sigma$ of the underlying is given by the closed form expression:
$$
c  =  e^{- r T} \left[\right. F N \left(\right. d_{1} \left.\right) - K N \left(\right. d_{2} \left.\right) \left]\right. \\ p  =  e^{- r T} \left[\right. K N \left(\right. - d_{2} \left.\right) - F N \left(\right. - d_{1} \left.\right) \left]\right.
$$

where
$$
d_{1}  =  \frac{ln ⁡ \left(\right. F / K \left.\right) + \left(\right. \left(\sigma\right)^{2} / 2 \left.\right) T}{\sigma \sqrt{T}} $$$$ d_{2}  =  \frac{ln ⁡ \left(\right. F / K \left.\right) - \left(\right. \left(\sigma\right)^{2} / 2 \left.\right) T}{\sigma \sqrt{T}} = d_{1} - \sigma \sqrt{T}
$$

This formula can be easily used to price caps,  swaptions,  futures options contract. Here we will use `QuantLib` to price the options on commodity futures.
```latex
import QuantLib as ql
import math

calendar = ql.UnitedStates()
bussiness_convention = ql.ModifiedFollowing
settlement_days = 0
day_count = ql.ActualActual()
```

## Option on Treasury Futures Contract

Options on treasury futures (10 Yr Note TYF6C 119) can be valued using the Black formula. Let us value a Call option maturing on December 24,  2015,  with a strike of 119. The current futures price is 126.95,  and the volatility is 11.567%. The risk free rate as of December 1,  2015 is 0.105%. Let us value this Call option as of December 1,  2015.
```latex
interest_rate = 0.00105
calc_date = ql.Date(1, 12, 2015)
yield_curve = ql.FlatForward(calc_date,  
                             interest_rate, 
                             day_count, 
                             ql.Compounded, 
                             ql.Continuous)

ql.Settings.instance().evaluationDate = calc_date
option_maturity_date = ql.Date(24, 12, 2015)
strike = 119
spot = 126.953# futures price
volatility = 11.567/100.
flavor = ql.Option.Call

discount = yield_curve.discount(option_maturity_date)
strikepayoff = ql.PlainVanillaPayoff(flavor,  strike)
T = yield_curve.dayCounter().yearFraction(calc_date,  
                                          option_maturity_date)
stddev = volatility*math.sqrt(T)

black = ql.BlackCalculator(strikepayoff,  
                           spot,  
                           stddev,  
                           discount)

print "%-20s: %4.4f" %("Option Price",  black.value() )
print "%-20s: %4.4f" %("Delta",  black.delta(spot) )
print "%-20s: %4.4f" %("Gamma",  black.gamma(spot) )
print "%-20s: %4.4f" %("Theta",  black.theta(spot,  T) )
print "%-20s: %4.4f" %("Vega",  black.vega(T) )
print "%-20s: %4.4f" %("Rho",  black.rho( T) )

```
```latex
Option Price        : 7.9686
Delta               : 0.9875
Gamma               : 0.0088
Theta               : -0.9356
Vega                : 1.0285
Rho                 : 7.3974
```

## Natural Gas Futures Option

I saw this-methods-for-option-pricing-td17018.html) question on quantlib users group. Thought I will add this example as well.

Call option with a 3.5 strike,  spot 2.919,  volatility 0.4251. The interest rate is 0.15%.
```latex
interest_rate = 0.0015
calc_date = ql.Date(23, 9, 2015)
yield_curve = ql.FlatForward(calc_date,  
                             interest_rate, 
                             day_count, 
                             ql.Compounded, 
                             ql.Continuous)

ql.Settings.instance().evaluationDate = calc_date
T = 96.12/365.

strike = 3.5
spot = 2.919
volatility = 0.4251
flavor = ql.Option.Call

discount = yield_curve.discount(T)
strikepayoff = ql.PlainVanillaPayoff(flavor,  strike)
stddev = volatility*math.sqrt(T)

strikepayoff = ql.PlainVanillaPayoff(flavor,  strike)
black = ql.BlackCalculator(strikepayoff,  spot,  stddev,  discount)

print "%-20s: %4.4f" %("Option Price",  black.value() )
print "%-20s: %4.4f" %("Delta",  black.delta(spot) )
print "%-20s: %4.4f" %("Gamma",  black.gamma(spot) )
print "%-20s: %4.4f" %("Theta",  black.theta(spot,  T) )
print "%-20s: %4.4f" %("Vega",  black.vega(T) )
print "%-20s: %4.4f" %("Rho",  black.rho( T) )
```
```latex
Option Price        : 0.0789
Delta               : 0.2347
Gamma               : 0.4822
Theta               : -0.3711
Vega                : 0.4600
Rho                 : 0.1597
```

## Conclusion

In this notebook,  I demonstrated how Black formula can be used to value options on commodity futures. It is worth pointing out that different vendors usually have different scaling conventions when it comes to reporting greeks. One would needs to take that into account when comparing the values shown by QuantLib with that of other vendors

## References

\[1\] Fischer Black,  *The pricing of commodity contracts*,  Journal of Financial Economics,  (3) 167-179 (1976)

**Related Post**

- QuantLib Python Tutorials With Examples](http://gouthamanbalaraman.com/blog/quantlib-python-tutorials-with-examples.html)
- On the Convergence of Hull White [Monte Carlo Simulations](http://gouthamanbalaraman.com/blog/hull-white-simulation-monte-carlo-convergence.html)
- Short [Interest Rate Model Calibration in QuantLib Python](http://gouthamanbalaraman.com/blog/short-interest-rate-model-calibration-quantlib.html)
- QuantLib Python Cookbook Announcement](http://gouthamanbalaraman.com/blog/quantlib-python-cookbook-announcement.html)
- Valuing Bonds with Credit Spreads in [QuantLib Python](http://gouthamanbalaraman.com/blog/bonds-with-spreads-quantlib-python.html)

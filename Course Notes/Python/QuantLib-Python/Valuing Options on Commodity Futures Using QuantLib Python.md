---
title: Valuing Options on Commodity Futures Using QuantLib Python
source: 
  http://gouthamanbalaraman.com/blog/value-options-commodity-futures-black-formula-quantlib-python.html
description: Describes how to value options on commodity futures contract using the
  Black formula in QuantLib Python
tags:
  - black_formula
  - commodity_futures
  - futures_options
  - option_pricing
  - quantlib_python
aliases:
  - Commodity Option Pricing
  - QuantLib Example
key_concepts:
  - Black formula application
  - Commodity futures options valuation
  - Futures price modeling
  - Lognormal stochastic process
  - QuantLib Python implementation
---

# Valuing Options on Commodity Futures Using QuantLib Python
Describes how to value options on [commodity futures](../../../Financial%20Instruments/Financial%20Instruments%20PSET%20Solutions.md) contract using the Black formula in [QuantLib Python](Valuing%20Callable%20Bonds%20Using%20QuantLib%20Python.md)

The [Black-Scholes equation](../../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%205%20Options%20on%20Prices%20and%20Hedge-Based%20Valuation/Black-Scholes%20Model%20and%20Extensions.md) is the well known model to price equity European options. In the case of equities,  the spot price fluctuates and hence the intuition to model as a [stochastic process](../../../The%20Ornstein-Uhlenbeck%20(OU)%20Process.md) makes sense. In the case of [commodities](../../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%203%20-%20Futures%20Markets/Futures%20Not%20Subject%20to%20Cash-And-Carry.md),  however,  the spot price does not fluctuate as much,  and hence cannot be modeled as a [stochastic process](../../../The%20Ornstein-Uhlenbeck%20(OU)%20Process.md) to value options on [commodities](../../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%203%20-%20Futures%20Markets/Futures%20Not%20Subject%20to%20Cash-And-Carry.md). In the 1976 paper \[1\],  Fischer Black addressed this problem by modeling the [futures price](../../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%2011/Futures%20Price%20and%20the%20Quality%20Option%20Before%20E.md),  which demonstrates fluctuations,  as the [lognormal stochastic process](.md).

The [futures price](../../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%2011/Futures%20Price%20and%20the%20Quality%20Option%20Before%20E.md) at time $t$,  $F_{t}$ with a is modeled as:
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

This formula can be easily used to price caps,  swaptions,  [futures](../../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%203%20-%20Futures%20Markets/Futures%20Not%20Subject%20to%20Cash-And-Carry.md) options contract. Here we will use `QuantLib` to price the options on [commodity futures](../../../Financial%20Instruments/Financial%20Instruments%20PSET%20Solutions.md).
```latex
import QuantLib as ql
import math

calendar = ql.UnitedStates()
bussiness_convention = ql.ModifiedFollowing
settlement_days = 0
day_count = ql.ActualActual()
```

## Option on Treasury Futures Contract

Options on treasury [futures](../../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%203%20-%20Futures%20Markets/Futures%20Not%20Subject%20to%20Cash-And-Carry.md) (10 Yr Note TYF6C 119) can be valued using the Black formula. Let us value a Call option maturing on December 24,  2015,  with a strike of 119. The current [futures price](../../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%2011/Futures%20Price%20and%20the%20Quality%20Option%20Before%20E.md) is 126.95,  and the volatility is 11.567%. The risk free rate as of December 1,  2015 is 0.105%. Let us value this Call option as of December 1,  2015.
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

I saw [this](http://quantlib0.\1.n7.nabble.com/[Quantlib](Introduction%20to%20QuantLib%20Python.md)-methods-for-option-[pricing](../../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%207/Arbitrage%20Pricing%20of%20Derivatives.md)-td17018.html) question on [quantlib](Introduction%20to%20QuantLib%20Python.md) users group. Thought I will add this example as well.

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

In this notebook,  I demonstrated how Black formula can be used to value options on [commodity futures](../../../Financial%20Instruments/Financial%20Instruments%20PSET%20Solutions.md). It is worth pointing out that different vendors usually have different scaling conventions when it comes to reporting [greeks](../../../Financial%20Engineering/Derivatives/Part%20V%20-%20Options%20Pricing/Chapter%2026%20-%20Pricing%20Options:%20Monte%20Carlo%20Simulation.md). One would needs to take that into account when comparing the values shown by [QuantLib](Introduction%20to%20QuantLib%20Python.md) with that of other vendors

## References

\[1\] Fischer Black,  *The [pricing](../../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%207/Arbitrage%20Pricing%20of%20Derivatives.md) of commodity contracts*,  Journal of Financial Economics,  (3) 167-179 (1976)

**Related Post**

- [QuantLib Python]([Valuing%20Callable%20Bonds%20Using%20QuantLib%20Python) Tutorials With Examples](http://gouthamanbalaraman.com/blog/[quantlib](Introduction%20to%20QuantLib%20Python.md)-python-tutorials-with-examples.html)
- [On the Convergence of Hull White [Monte Carlo](../../../Financial%20Instruments/Lecture%20Notes-%20Financial%20Instruments/Teaching%20Note%207-Exotic%20Options%20And%20Derivative%20Pricing%20By%20Monte%20Carlo%20Simulation.md) Simulations](http://gouthamanbalaraman.com/blog/hull-white-simulation-monte-carlo-convergence.html)
- [Short [Interest Rate Model](../../../Fixed%20Income%20Asset%20Pricing/Fixed%20Income%20Lecture%20Notes/An%20Overview%20of%20the%20Vasicek%20Short%20Rate%20Model.md) [Calibration](../../../Credit%20Markets/Credit%20Markets%20Session%204.md) in [QuantLib Python](Valuing%20Callable%20Bonds%20Using%20QuantLib%20Python.md)](http://gouthamanbalaraman.com/blog/short-interest-rate-model-[calibration](../../../Credit%20Markets/Credit%20Markets%20Session%204.md)-[quantlib](Introduction%20to%20QuantLib%20Python.md).html)
- [QuantLib Python]([Valuing%20Callable%20Bonds%20Using%20QuantLib%20Python) Cookbook Announcement](http://gouthamanbalaraman.com/blog/[quantlib](Introduction%20to%20QuantLib%20Python.md)-python-cookbook-announcement.html)
- [Valuing Bonds with Credit Spreads in [QuantLib Python](Valuing%20Callable%20Bonds%20Using%20QuantLib%20Python.md)](http://gouthamanbalaraman.com/blog/bonds-with-spreads-[quantlib](Introduction%20to%20QuantLib%20Python.md)-python.html)
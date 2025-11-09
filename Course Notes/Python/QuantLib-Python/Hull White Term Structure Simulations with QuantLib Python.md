---
title: Hull White Term Structure Simulations with QuantLib Python
source: https://gouthamanbalaraman.com/blog/hull-white-simulation-quantlib-python.html
description: Discusses simulation of the Hull White interest rate term structure model
  in QuantLib Python
tags:
  - hull_white_model
  - interest_rate_model
  - quantlib_python
  - simulation
  - term_structure
aliases:
  - Hull-White model
  - QuantLib simulation
key_concepts:
  - Hull-White short rate model
  - Interest rate properties
  - QuantLib Python simulation
  - Simulating interest rates
  - Term structure modeling
---

# Hull White Term Structure Simulations with QuantLib Python
Discusses simulation of the Hull White [interest rate term structure](Valuing%20Interest%20Rate%20Caps%20and%20Floors%20Using%20QuantLib%20Python.md) model in [QuantLib Python](Valuing%20Callable%20Bonds%20Using%20QuantLib%20Python.md)

*Visit here for other [QuantLib Python]([Valuing%20Callable%20Bonds%20Using%20QuantLib%20Python) examples](http://gouthamanbalaraman.com/blog/[quantlib](Introduction%20to%20QuantLib%20Python.md)-python-tutorials-with-examples.html). If you found these posts useful,  please take a minute by providing some [feedback.](https://docs.google.com/forms/d/e/1FAIpQLSdFdJ768HKmIyJmaVRHBUJNY5NyQl6vr0GZvSkx-bUfIloNZA/viewform)*

The [Hull-White Short Rate Model](.md) is defined as:
$$ dr\_t = (\theta(t) - a r\_t)dt + \sigma dW\_t $$

where $a$ and $ \sigma $ are constants,  and $\theta(t)$ is chosen in order to fit the input [term structure of interest rates](../../../Financial%20Engineering/6.%20A%20Brief%20Introduction%20to%20Stochastic%20Calculus.md). Here we use [QuantLib](Introduction%20to%20QuantLib%20Python.md) to show how to simulate the [Hull-White model](On%20the%20Convergence%20of%20Hull%20White%20Monte%20Carlo%20Simulations.md) and investigate some of the properties.

We import the libraries and set things up as shown below:

In \[1\]:
```latex
import QuantLib as ql
import matplotlib.pyplot as plt
import numpy as np
% matplotlib inline
```

The constants that we use for this example is all defined as shown below. Variables `sigma` and `a` are the constants that define the [Hull-White model](On%20the%20Convergence%20of%20Hull%20White%20Monte%20Carlo%20Simulations.md). In the simulation,  we discretize the time span of `length` 30 years into 360 intervals (one per month) as defined by the `timestep` variable. For simplicity we will use a constant [forward rate](../../../Clippings/Forward%20Points%20in%20Currency.md) [term structure](../../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%209/The%20Vasicek%20Model.md) as an input. It is straight forward to swap with another [term structure](../../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%209/The%20Vasicek%20Model.md) here.

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

 ![500](Unknown.png)
The [short rate](../../../Fixed%20Income%20Asset%20Pricing/Fixed%20Income%20Lecture%20Notes/An%20Overview%20of%20the%20Vasicek%20Short%20Rate%20Model.md) $r(t)$ is given a distribution with the properties:
$$ E\{r(t) | F\_s\} = r(s)e^{-a(t-s)} + \alpha(t) - \alpha(s)e^{-a(t-s)} $$ $$ Var\{ r(t) | F\_s \} = \frac{\sigma^2}{2a} [1 - e^{-2a(t-s)}] $$ where $$ \alpha(t) = f^M(0,  t) + \frac{\sigma^2} {2a^2}(1-e^{-at})^2$$

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

 ![500](variance_of_short_rates.png)
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

 ![500](mean_of_short_rates.png)

## Conclusion

This post shows how to simulate [Hull-White short rate model](.md) using [QuantLib Python](Valuing%20Callable%20Bonds%20Using%20QuantLib%20Python.md). You can download the [ipython notebook on Hull-White simulations](https://gouthamanbalaraman.com/extra/notebooks/hull_white_simulations.ipynb).

   [quantlib]([Introduction%20to%20QuantLib%20Python)](http://gouthamanbalaraman.com/tag/[quantlib](Introduction%20to%20QuantLib%20Python.md).html)   [python](http://gouthamanbalaraman.com/tag/python.html)   [finance](http://gouthamanbalaraman.com/tag/finance.html)

---

**Related Post**

- [QuantLib Python]([Valuing%20Callable%20Bonds%20Using%20QuantLib%20Python) Tutorials With Examples](http://gouthamanbalaraman.com/blog/[quantlib](Introduction%20to%20QuantLib%20Python.md)-python-tutorials-with-examples.html)
- [On the Convergence of Hull White [Monte Carlo](../../../Financial%20Instruments/Lecture%20Notes-%20Financial%20Instruments/Teaching%20Note%207-Exotic%20Options%20And%20Derivative%20Pricing%20By%20Monte%20Carlo%20Simulation.md) Simulations](http://gouthamanbalaraman.com/blog/hull-white-simulation-monte-carlo-convergence.html)
- [Valuing Options on [Commodity Futures](../../../Financial%20Instruments/Financial%20Instruments%20PSET%20Solutions.md) Using [QuantLib Python](Valuing%20Callable%20Bonds%20Using%20QuantLib%20Python.md)](http://gouthamanbalaraman.com/blog/value-options-commodity-[futures](../../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%203%20-%20Futures%20Markets/Futures%20Not%20Subject%20to%20Cash-And-Carry.md)-black-formula-[quantlib](Introduction%20to%20QuantLib%20Python.md)-python.html)
- [Short [Interest Rate Model](../../../Fixed%20Income%20Asset%20Pricing/Fixed%20Income%20Lecture%20Notes/An%20Overview%20of%20the%20Vasicek%20Short%20Rate%20Model.md) [Calibration](../../../Credit%20Markets/Credit%20Markets%20Session%204.md) in [QuantLib Python](Valuing%20Callable%20Bonds%20Using%20QuantLib%20Python.md)](http://gouthamanbalaraman.com/blog/short-interest-rate-model-[calibration](../../../Credit%20Markets/Credit%20Markets%20Session%204.md)-[quantlib](Introduction%20to%20QuantLib%20Python.md).html)
- [QuantLib Python]([Valuing%20Callable%20Bonds%20Using%20QuantLib%20Python) Cookbook Announcement](http://gouthamanbalaraman.com/blog/[quantlib](Introduction%20to%20QuantLib%20Python.md)-python-cookbook-announcement.html)
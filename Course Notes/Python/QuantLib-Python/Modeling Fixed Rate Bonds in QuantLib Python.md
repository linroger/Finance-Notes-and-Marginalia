---
title: Modeling Fixed Rate Bonds in QuantLib Python
source: https://gouthamanbalaraman.com/blog/quantlib-bond-modeling.html
description: This post will walk through an example of modeling fixed rate bonds using
  QuantLib Python.
tags:
  - bond_valuation
  - coupon_bond
  - fixed_rate_bond
  - quantlib_python
  - term_structure
aliases:
  - Bond Modeling
  - QuantLib Example
key_concepts:
  - Bond fair value
  - Coupon payments
  - Fixed rate bonds
  - QuantLib Python modeling
  - Spot rates
---

# Modeling Fixed Rate Bonds in QuantLib Python

This post will walk through an example of modeling fixed rate bonds using [QuantLib Python](Valuing%20Callable%20Bonds%20Using%20QuantLib%20Python.md).

*Visit here for other [QuantLib Python]([Valuing%20Callable%20Bonds%20Using%20QuantLib%20Python) examples](http://gouthamanbalaraman.com/blog/[quantlib](Introduction%20to%20QuantLib%20Python.md)-python-tutorials-with-examples.html). If you found these posts useful,  please take a minute by providing some [feedback.](https://docs.google.com/forms/d/e/1FAIpQLSdFdJ768HKmIyJmaVRHBUJNY5NyQl6vr0GZvSkx-bUfIloNZA/viewform)*

Let's consider a hypothetical bond with a par value of 100,  that pays 6% coupon semi-annually issued on January 15th,  2015 and set to mature on January 15th,  2016. The bond will pay a coupon on July 15th,  2015 and January 15th,  2016. The par amount of 100 will also be paid on the January 15th,  2016.

To make things simpler,  lets assume that we know the spot rates of the treasury as of January 15th,  2015. The annualized spot rates are 0.5% for 6 months and 0.7% for 1 year point. Lets calculate the fair value of this bond.
```latex
>>> 3/pow(1+0.005,  0.5) + (100 + 3)/(1+0.007)
105.27653992490681
```

Lets calculate the same thing using [QuantLib](Introduction%20to%20QuantLib%20Python.md).
```latex
>>> import QuantLib as ql
>>> todaysDate = ql.Date(15,  1,  2015)
>>> ql.Settings.instance().evaluationDate = todaysDate
>>> spotDates = [ql.Date(15,  1,  2015),  ql.Date(15,  7,  2015),  ql.Date(15,  1,  2016)]
>>> spotRates = [0.0,  0.005,  0.007]
>>> dayCount = ql.Thirty360()
>>> calendar = ql.UnitedStates()
>>> interpolation = ql.Linear()
>>> compounding = ql.Compounded
>>> compoundingFrequency = ql.Annual
>>> spotCurve = ql.ZeroCurve(spotDates,  spotRates,  dayCount,  calendar,  interpolation, 
                             compounding,  compoundingFrequency)
>>> spotCurveHandle = ql.YieldTermStructureHandle(spotCurve)
```

So far we have created the [term structure](../../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%209/The%20Vasicek%20Model.md) and the variables are rather self explanatory. Now lets construct the fixed rate bond.
```latex
>>> issueDate = ql.Date(15,  1,  2015)
>>> maturityDate = ql.Date(15,  1,  2016)
>>> tenor = ql.Period(ql.Semiannual)
>>> calendar = ql.UnitedStates()
>>> bussinessConvention = ql.Unadjusted
>>> dateGeneration = ql.DateGeneration.Backward
>>> monthEnd = False
>>> schedule = ql.Schedule (issueDate,  maturityDate,  tenor,  calendar,  bussinessConvention, 
                            bussinessConvention ,  dateGeneration,  monthEnd)
>>> list(schedule)
[Date(15,  1,  12015),  Date(15, 7, 2015),  Date(15, 1, 2016)]

# Modeling Fixed Rate Bonds in QuantLib Python
>>> dayCount = ql.Thirty360()
>>> couponRate = 0.\1
>>> coupons = [couponRate]

# Now lets construct the FixedRateBond
>>> settlementDays = 0
>>> faceValue = 100
>>> fixedRateBond = ql.FixedRateBond(settlementDays,  faceValue,  schedule,  coupons,  dayCount)

# create a bond engine with the term structure as input;
# set the bond to use this bond engine
>>> bondEngine = ql.DiscountingBondEngine(spotCurveHandle)
>>> fixedRateBond.setPricingEngine(bondEngine)

# Finally the price
>>> fixedRateBond.NPV()
105.27653992490683
```

Voila!

Download the [modeling bonds ipython notebook](https://gouthamanbalaraman.com/extra/notebooks/modeling-bonds.ipynb).

   [python](http://gouthamanbalaraman.com/tag/python.html)   [finance](http://gouthamanbalaraman.com/tag/finance.html)   [quantlib]([Introduction%20to%20QuantLib%20Python)](http://gouthamanbalaraman.com/tag/[quantlib](Introduction%20to%20QuantLib%20Python.md).html)

---

**Related Post**

- [QuantLib Python]([Valuing%20Callable%20Bonds%20Using%20QuantLib%20Python) Tutorials With Examples](http://gouthamanbalaraman.com/blog/[quantlib](Introduction%20to%20QuantLib%20Python.md)-python-tutorials-with-examples.html)
- [Modeling Vanilla Interest Rate Swaps Using [QuantLib Python](Valuing%20Callable%20Bonds%20Using%20QuantLib%20Python.md)](http://gouthamanbalaraman.com/blog/interest-rate-swap-[quantlib](Introduction%20to%20QuantLib%20Python.md)-python.html)
- [Valuing Options on [Commodity Futures](../../../Financial%20Instruments/Financial%20Instruments%20PSET%20Solutions.md) Using [QuantLib Python](Valuing%20Callable%20Bonds%20Using%20QuantLib%20Python.md)](http://gouthamanbalaraman.com/blog/value-options-commodity-[futures](../../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%203%20-%20Futures%20Markets/Futures%20Not%20Subject%20to%20Cash-And-Carry.md)-black-formula-[quantlib](Introduction%20to%20QuantLib%20Python.md)-python.html)
- [Short [Interest Rate Model](../../../Fixed%20Income%20Asset%20Pricing/Fixed%20Income%20Lecture%20Notes/An%20Overview%20of%20the%20Vasicek%20Short%20Rate%20Model.md) [Calibration](../../../Credit%20Markets/Credit%20Markets%20Session%204.md) in [QuantLib Python](Valuing%20Callable%20Bonds%20Using%20QuantLib%20Python.md)](http://gouthamanbalaraman.com/blog/short-interest-rate-model-[calibration](../../../Credit%20Markets/Credit%20Markets%20Session%204.md)-[quantlib](Introduction%20to%20QuantLib%20Python.md).html)
- [Announcing qtk for [QuantLib Python](Valuing%20Callable%20Bonds%20Using%20QuantLib%20Python.md)](http://gouthamanbalaraman.com/blog/announcing-qtk-[quantlib](Introduction%20to%20QuantLib%20Python.md)-python.html)

---

 ![500](https://gouthamanbalaraman.com/images/me.png)
I am Goutham Balaraman,  and I explore topics in [quantitative finance](../../Quantitative%20Trading%20Strategies%20Lecture%20Notes.md),  programming,  and data science. You can follow me [@gsbalaraman](https://twitter.com/gsbalaraman).

---

**Checkout my book**

[ ![500](https://gouthamanbalaraman.com/images/cookbook.png)](https://leanpub.com/quantlibpythoncookbook)
Updated posts from this blog and transcripts of Luigi's screencasts on YouTube is compiled into [QuantLib Python]([Valuing%20Callable%20Bonds%20Using%20QuantLib%20Python) Cookbook](https://leanpub.com/quantlibpythoncookbook) .
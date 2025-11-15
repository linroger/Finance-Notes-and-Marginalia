---
aliases:
- QL
- QuantLib
- QuantLib Python
description: This post will walk through some of the basics of QuantLib Python library.
enhanced: true
enhancement_date: '2025-11-06'
enhancement_id: batch03-c974d0
key_concepts:
- Carry trades and momentum in FX markets
- Sovereign risk assessment and country analysis
- Mean-variance optimization and the efficient frontier
- Date object construction
- Extreme value theory and tail risk modeling
- Single-name vs. index CDS trading
- Credit risk modeling and default probability estimation
- Risk budgeting and portfolio construction techniques
- Historical simulation vs. parametric VaR models
- Credit portfolio diversification and concentration
- Credit spread decomposition and hazard rates
- CDS clearing and central counterparties
- DV01 calculation and interest rate risk hedging
- Portfolio immunization strategies
- CDS-Bond basis and arbitrrage opportunities
- Schedule object dates
- Mathematical Finance
- Monte Carlo integration and variance reduction
- GARCH models and volatility forecasting
- Deposit insurance and systemic risk prevention
- Monte Carlo VaR for complex portfolios
- InterestRate class usage
- Stress testing and scenario analysis
- Key rate duration and curve risk
- day count convention in CDS
- Course Material
- Currency risk management and hedging
- QuantLib Python library
- Control variates and importance sampling techniques
- Value at Risk (VaR) methodologies and backtesting
- Risk-neutral pricing methodology for derivative securities
- Forward rates and interest rate parity
- Case Study
- Operational risk quantification and modeling
- Exchange rate determination and PPP theory
- Arbitrage opportunities and risk-free profit extraction
- Expected Shortfall and coherent risk measures
- Credit default swap pricing and risk-neutral probabilities
- present value and discounting methods
- Bank liquidity ratios and funding risk management
- Compound factor method
- Discount factor calculation
- Credit exposure measurement and EAD
- Wrong-way risk in derivative transactions
- Value-at-Risk calculation using historical simulation
- Quantitative Implementation
- Credit risk migration matrices and rating transition
- Credit risk modeling and portfolio correlation analysis
- Backtesting procedures for risk models
- Credit risk assessment and loan portfolio management
- Liquidity risk measurement and management
- Duration and convexity measures for bond portfolios
- Systemic risk indicators and early warning systems
- Global financial stability and systemic risk monitoring
- Price sensitivity to interest rate changes
- Loss given default and recovery rates
- Modified duration vs. Macaulay duration
- Currency markets and foreign exchange trading
source: https://gouthamanbalaraman.com/blog/quantlib-basics.html
tags:
- financial-analysis
- schedule_object
- credit-default-swaps
- garch-models
- mathematical-finance
- course-material
- financial-modeling
- case-study
- value-at-risk
- exchange-rates
- time_module
- credit-risk
- quantitative-implementation
- duration-convexity
- solution
- date_object
- stress-testing
- liquidity-risk
- systemic-risk
- exotic-options
- net-present-value
- deposit-insurance
- quantitative-finance
- dcf-valuation
- quantlib_python
- expected-shortfall
- operational-risk
- monte-carlo
- interest_rate
title: Introduction to QuantLib Python
---

# Introduction to QuantLib Python

This post will walk through some of the basics of QuantLib Python library.

I installed the latest version of QuantLib (V1.5) and the python wrapper to QuantLib. My experiments lately have been to get a feel for the QuantLib API. The library itself is so extensive,  that it is rather hard for a new comer to get going. In this post we will look into some of the basic classes and functionality in QuantLib.

## Time SubModule

The ql/time sub-folder implements various time related classes. Lets take a look at the Date object which can be constructed as Date(date,  month,  year).
```latex
>>> date = ql.Date(31,  3,  2015) # 31 March,  2015
>>> print date
March 31st,  2015
>>> date.dayOfMonth()
31
>>> date.month()
3
>>> date.year()
2015
>>> date.weekday() == ql.Tuesday
True

# Introduction to QuantLib Python
>>> date + 1  # add a day
Date(1, 4, 2015)
>>> date - 1  # subtract a day
Date(30, 3, 2015)
>>> date + ql.Period(1,  ql.Months)
Date(30, 4, 2015)
>>> date + ql.Period(1,  ql.Weeks)
Date(7, 4, 2015)
>>> date + ql.Period(1,  ql.Years)
Date(31, 3, 2016)

# logical operations
>>> ql.Date(31,  3,  2015) > ql.Date(1,  3,  2015)
True
```

The Schedule object can be used to construct a list of dates such as coupon payments. Lets look at some examples.
```latex
>>> date1 = ql.Date(1,  1,  2015)
>>> date2 = ql.Date(1,  1,  2016)
>>> tenor = ql.Period(ql.Monthly)
>>> calendar = ql.UnitedStates()
>>>
>>> schedule = ql.Schedule(date1,  date2,  tenor,  calendar,  ql.Following, 
                           ql.Following,  ql.DateGeneration.Forward,  False)
>>> list(schedule)
[Date(2, 1, 2015), 
 Date(2, 2, 2015), 
 Date(2, 3, 2015), 
 Date(1, 4, 2015), 
 Date(1, 5, 2015), 
 Date(1, 6, 2015), 
 Date(1, 7, 2015), 
 Date(3, 8, 2015), 
 Date(1, 9, 2015), 
 Date(1, 10, 2015), 
 Date(2, 11, 2015), 
 Date(1, 12, 2015), 
 Date(4, 1, 2016)]
```

Here we have generated a Schedule object that will contain dates between date1 and date2 with the tenor specifying the Period to be every Month. The calendar object is used for determining holidays. The two arguments following the calendar in the Schedule constructor are the BussinessDayConvention. Here we chose the convention to be the day following holidays. That is why we see that holidays are excluded in the list of dates.

## Interest Rate

The InterestRate class can be used to store the interest rate with the compounding type,  day count and the frequency of compounding. Below we show how to create an interest rate of 5.0% compounded annually,  using Actual/Actual day count convention.
```latex
>>> annualRate = 0.05
>>> dayCount = ql.ActualActual()
>>> compoundType = ql.Compounded
>>> frequency = ql.Annual
>>> interestRate = ql.InterestRate(annualRate,  dayCount,  compoundType,  frequency)
```

Lets say if you invest a dollar at the interest rate described by interestRate,  the compoundFactor method gives you how much your investment will be worth after t years. Below we show that the value returned by compoundFactor for 2 years agrees with the expected compounding formula.
```latex
>>> interestRate.compoundFactor(2.0)
1.1025
>>> (1.0 + annualRate)*(1.0 + annualRate)  # Check the above calculation
1.1025
```

The discountFactor method returns the reciprocal of the compoundFactor method. The discount factor is useful while calculating the present value of future cashflows.
```latex
>>> interestRate.discountFactor(2.0)
0.9070294784580498
>>> 1.0 / interestRate.compoundFactor(2.0)
0.9070294784580498
```

A given interest rate can be converted into other types using the equivalentRate method as :
```latex
>>> newFrequency = ql.Semiannual
>>> effectiveRate = interestRate.equivalentRate(compoundType,  newFrequency,  1)
>>> effectiveRate.rate()
0.04939015319191986
```

The InterestRate class also has an impliedRate method. The impliedRate method takes compound factor to return the implied rate. The impliedRate method is a static method in the InterestRate class and can be used without an instance of InterestRate. Internally the equivalentRate method invokes the impliedRate method in its calculations.

Here we have converted into a semi-annual compounding type. A 4.939% of semi-annual compounding is equivalent to 5.0% annual compounding. This should mean,  that both should give identical discount factors. Lets check that:
```latex
>>> interestRate.discountFactor(1.0)
0.9523809523809523
>>> effectiveRate.discountFactor(1.0)
0.9523809523809521
```

So this means that pricing bonds using either interest rate convention should give the same net present value (barring some precision).

## Conclusion

In this post we looked at the basics of QuantLib:

- We learnt how to use Date and Schedule classes from the time sub-module
- we learnt how to use the InterestRate class

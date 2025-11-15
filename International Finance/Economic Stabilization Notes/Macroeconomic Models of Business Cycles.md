---
aliases:
- IS curve
- business cycle models
- consumption smoothing
- Aggregate Demand Models
- Macroeconomic Stabilization
cssclasses:
- academia
key_concepts:
- aggregate demand
- consumer durables
- consumption smoothing
- ex ante real interest
- real interest rate
- IS curve derivation
- life-cycle hypothesis
- permanent income hypothesis
- marginal propensity to consume
- wealth effects
- time preference
- capital market imperfections
- borrowing constraints
- policy effectiveness
- Equity valuation and analysis
- Dividend discount models
- Market microstructure and trading
- Liquidity and price discovery
- Bond pricing and yield analysis
- Duration and convexity
linter-yaml-title-alias: Macroeconomic Models of Business Cycles
tags:
- equity
- regulatory-framework
- monetary_policy
- aggregate_demand
- mathematical-finance
- real_interest_rate
- interest_rates
- permanent_income_hypothesis
- business_cycles
- consumption_theory
- life_cycle_hypothesis
- trading
- bonds
- futures
- risk_management
title: Macroeconomic Models of Business Cycles
---

# Macroeconomic Models of Business Cycles

## Aggregate Demand

### Market in New Goods and Services: The IS Curve

**1. Current Real Consumption of Domestically-Produced or Foreign-Produced Goods
and Services** depends on current real after-tax income and on expected future
real after-tax income. (It also depends on the real interest rate and other
factors as discussed in points 2, 3, and 4 below.) There are two main pieces to
understanding the basics of modern models of consumption (known as the
"life-cycle" and "permanent income" models of consumption).

**First, consumption "smoothing" over one's lifetime is approximately optimal.**
That is, if a person expects to live $T$ periods, then $C_1 = C_2 = \ldots =
C_T$ is approximately optimal. This follows from the key assumption of
diminishing marginal utility of consumption. For example, over two periods with a
total of 20 units of consumption, reallocating one's consumption from a smooth
$(10, 10)$ to a choppy $(5, 15)$ lowers utility on balance because reducing
consumption by 5 units (in period one) lowers utility more than raising
consumption 5 units (in period two) boosts utility; thus smooth or equal
consumption is optimal.

$$
\text{Utility of Consumption: } U(C_1, C_2) = U(C_1) + U(C_2)
$$

This expression assumes no discounting of future utility. In this case, we need
to prove that $U(10) + U(10) > U(5) + U(15)$ to show the optimality of
consumption smoothing.

Re-write the inequality as:

$$
U(10) - U(5) > U(15) - U(10)
$$

But this is true because of diminishing marginal utility. There are some
exceptions we will explore briefly. These include:
- The difference between market interest rates and the rate of time preference
- Capital market imperfections in which an individual cannot borrow against
  future income enough to maintain consumption in periods of low income
- Legal limits to consumption in certain periods such as occurred in the U.S.
  during the corona-virus period of 2020 and during the rationing period of World
  War II

**Second, under modern models, consumption in every period of life depends on an
individual's expected lifetime resources, not just today's resources.** This has
implications for temporary vs. permanent changes in income. For example, if a
person unexpectedly receives $1 on a temporary or transitory basis either because
of a one-time wealth transfer or a temporary tax cut lasting just one period and
if the person allocates the income evenly to consumption in each period of their
lifetime, then consumption rises by $(1/T)$ dollars each period. That is, the
marginal propensity to consume out of wealth or out of temporary income is
$(1/T)$. If $T$ is 33 years, then the one-time $1 boost to income raises
consumption 3 cents per year (relative to baseline) starting immediately. As an
application, an exogenous decline in house prices resulting in a $1 fall in
household wealth would reduce total consumer spending by 3 cents (and, in fact,
empirical evidence supports a decline of 3 cents on the dollar in the aggregate).

By contrast, if the person unexpectedly receives an additional dollar every
period so that the income rise is permanent, lifetime resources rise by $33 and
consumption rises by $1 per year (relative to baseline) starting immediately.
Thus the marginal propensity to consume out of permanent income is 1. Notice I
have described the increase in either temporary or permanent income as
"unexpected." What would happen to the path of consumption at the moment of an
increase in income if the increase were fully expected such as an increase in
income when you move from college to a job or from your working years to
retirement? Short answer: nothing happens, it already did.

Implicitly, the prior analysis assumes perfect capital (borrowing and lending)
markets so that an individual can borrow against their expected future income. If
the government unexpectedly announces a permanent tax cut of $1000 per person to
take effect in two years then individuals must be able to borrow against that
expected future boost to after-tax income (or draw down existing savings).
Otherwise, consumption smoothing starting today at the new higher level of
consumption would not be possible.

To summarize at this point, households will choose the optimal level of current
consumption given today's current, and expectations of future, after-tax income,
etc. (i.e., given today's view about lifetime resources). They will
(approximately) maintain this level of consumption for the rest of their lifetime
unless something unexpected happens that alters today's expectations of current
and future income, etc. For example, an unexpected boost to lifetime resources
would lead to an immediate increase in consumption to a new level that would
remain constant ("smoothed") until the next unexpected change in lifetime
resources occurs.

Notice that these considerations help explain the observed business cycle
positively correlated co-movement of aggregate consumption and income. Presumably
some of any observed change in aggregate income is unexpected and leads to a
change in consumption in the same direction based on our model of consumption.
Further, to the extent that enough individuals cannot borrow against future
income and thus must consume out of current income only, there again would be a
positive correlation between aggregate income and consumption; for example, an
unexpected temporary decline in income (e.g. due to a recession) would force
borrowing (or liquidity) constrained individuals to cut consumption. Borrowing
constraints require a modification of our basic consumption model.

Before moving on, it is worth noting that the optimality of consumption smoothing
implies that individuals would be willing to pay a positive amount to avoid
swings in consumption over time. The amount they would pay is very much like an
insurance premium—in this case it would be to insure against swings in total
consumption. However, it is not possible to buy private insurance to protect
against consumption swings due to macroeconomic events, such as recessions and
booms (we will talk about this more later in the course). In such circumstances,
perhaps government stabilization policy could in effect provide the insurance.

**2. Consumer Durables** (e.g., autos, computers) provide services over time and
thus have an investment (as well as a consumption) component; thus as the real
interest rate—viewed as the real cost of borrowing—rises, demand for durables
falls.

The **real interest rate** is given by:

$$
r = i - \pi^e
$$

where $i$ is the market or nominal interest rate and $\pi^e$ is the expected rate
of price inflation. Notice that we are not using the actually realized rate of
inflation but rather the rate that borrowers and lenders expect will occur as of
today when decisions are made. This is called the **ex ante real interest rate**.
The above relation can be re-written as:

$$
i = r + \pi^e
$$

That is, the market interest rate is the real interest rate augmented to include
compensation for expected inflation. Finally, when the realized rate of
inflation, $\pi$, is used, $r$ is called the **ex post real interest rate**.

**3. Households are believed to display a "positive rate of time preference,"**
meaning that, all else equal, they would prefer to consume now rather than in the
future. The household choice between present and future consumption (and hence
the decision about saving) depends on the strength of time preference versus the
relative price of future consumption $\left[\frac{1}{(1+r)}\right]$; there is a
substitution (or incentive) and an income (also called a target-wealth effect)
effect that work in opposite directions. Under the former, a higher rate of
return on saving, $r$, provides an incentive to save more today or, put another
way, to substitute future for current consumption (for a given rate of time
preference). By contrast, saving will fall (current consumption rise) to the
extent that the higher rate of return does not require as much saving to achieve
a target level of wealth in the future (say at retirement). Based on empirical
evidence on aggregate consumption behavior, we assume that the substitution
effect dominates so that higher $r$ means lower current consumption and hence
higher household saving. This effect can alter the above result on consumption
smoothing.

**4. There are a few other important determinants of consumption.** As suggested
above, consumption depends on a household's net wealth—the value of its stocks
and bonds and houses, etc. minus the value of its debts. The idea is that (net)
assets generate a stream of current and future non-wage income which provides
resources (in addition to wages) that support consumption over one's lifetime.
The value of wealth varies inversely with interest rates. Also, the state of
consumer confidence matters for consumption.

Let's briefly give an example of how wealth varies inversely with interest rates.
Consider stock prices, which can be thought of as the sum of a "fundamental"
component and a bubble component. Ignoring the bubble possibility, a stock's
fundamental price is the present discounted value of the future dividend stream,
that is:

$$
P_s = \frac{\text{div}_{t+1}}{(1+i)} + \frac{\text{div}_{t+2}}{(1+i)^2} + 
\frac{\text{div}_{t+3}}{(1+i)^3} + \ldots 
$$

where $\text{div}_{t+j}$ is the dollar amount of dividends paid to shareholders
at the end of period $t+j$ and $i$ is the market interest rate (this is
discussed more fully in Econ 111). Thus, for a given value of the dividend
stream, the stock price varies inversely with interest rates.
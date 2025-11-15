---
aliases:
- Fiscal Policy
- Fiscal and Monetary Policies
- Monetary Policy
- Empirical Stabilization
- Taylor Rule Analysis
- Budget Surplus Analysis
cssclasses:
- academia
key_concepts:
- Option pricing theory and Black-Scholes model
- Options Greeks and risk management
- Call and put option strategies
- Interest rate theory and modeling
- Monetary policy and rate setting
- LIBOR transition and SOFR
- Value at Risk (VaR) and stress testing
- Portfolio risk metrics and measures
- Hedging strategies and effectiveness
- Futures and forwards contract mechanics
- Cash-and-carry arbitrage
- Basis trading and roll strategies
- Bond pricing and yield curves
- Duration and convexity hedging
- Credit spreads and bond valuation
- Topics in Fiscal and Monetary Policies and Stabilization- Empirical Issues and financial
  analysis
- Topics in Fiscal and Monetary Policies and Stabilization- Empirical Issues in modern
  finance
- Applications of Topics in Fiscal and Monetary Policies and Stabilization- Empirical
  Issues
- 'Case study: Topics in Fiscal and Monetary Policies and Stabilization- Empirical
  Issues'
- Delta hedging strategies in options markets
- Growth Rate in financial markets
- Interest Rate in financial markets
- Value at Risk and tail risk measurement
- Financial markets and instrument analysis
- Quantitative finance and mathematical modeling
- Risk management and hedging strategies
- Investment analysis and portfolio theory
- Capital markets and trading strategies
- Financial engineering and product innovation
- Regulatory frameworks and compliance
- Market dynamics and behavioral finance
linter-yaml-title-alias: Topics in Fiscal and Monetary Policies and Stabilization
  - Empirical Issues
tags:
- delta
- monetary-policy
- forward
- risk-management
- interest-rates
- put
- crisis
- futures
- bonds
- measure
- options
- pandemic
- roe
- growth
- fundamental
- roll
- apt
- credit
- call
- model
- rating
- market
- treasury
- fail
- var
- roa
- growth-rate
- interest-rate
title: Topics in Fiscal and Monetary Policies and Stabilization - Empirical Issues
enhanced: true
enhancement_date: '2025-11-06'
enhancement_id: batch08-000519
batch: BATCH_AH
processing_agent: Enhancement Agent 8
---



# Topics in Fiscal and Monetary Policies and Stabilization: Empirical Issues

## Introduction

In this module we will study various empirical aspects of fiscal and monetary
policies. The first two sections include an empirical examination of
discretionary monetary and fiscal policies. The following section discusses
limits to stimulative monetary and fiscal policies, a topic of increasing
importance in the United States and around the world over the past decade or
longer. The final section of the module deals with automatic fiscal stabilizers.

## A. Discretionary Monetary Policy Actions

We start by discussing the Taylor Rule, the empirical link between monetary
policy actions and the business cycle. This rule should be viewed as an
approximation to actual monetary policy decision making in the United States over
the past 40 years or so; it is worth emphasizing that actual policy does not
always follow the Taylor rule.

**Taylor Rule:**
$$
FFR_i = r^* + \pi_i + (\pi - \pi^*)_i + [(y - y^*)/y^*]_i
$$

In this specification, $FFR$ denotes the nominal or market federal funds rate;
$y^*$ denotes the target level of real GDP (think of this as the natural or
potential level of GDP), $\pi^*$ denotes the target rate of price inflation
(currently 2% per annum in the United States), and $r^*$ the long-run or
equilibrium (or "natural" or "neutral") level of the real interest rate
(estimated currently to be less than 1% per annum). The real interest rate is
defined as the nominal or market interest rate minus the expected rate of price
inflation, which for this discussion is assumed equal to the actual rate of
inflation.

Under the Taylor rule, the Fed manipulates the federal funds rate (FFR), the
nominal interest rate under its direct control, in response to deviation between
actual and target values of inflation and output.

For example, the FFR is increased if the percentage output gap gets larger (i.e.,
as output rises further above trend or target); this is the sense in which
monetary policy attempts to be countercyclical with respect to fluctuations in
real output and thus to "lean against the wind" (interest rates rise which
reduces the interest-rate-sensitive components of aggregate demand). Also the FFR
is changed if inflation deviates from target. For example, the FFR is increased
if inflation rises above its target value; again this illustrates that the Fed
attempts to lean against the wind. Note the very close similarity to the
theoretical monetary rule in module 2. To make the connection appear even closer,
we can subtract the inflation rate from both sides of the above Taylor rule
converting the left hand side from the nominal funds rate to the real funds rate
($r = FFR - \pi$).

Leaning against the wind policy has implications for the relationship between the
real federal funds rate and $r^*$. In the case where both inflation and output
are less than their respective target values (as might result from a negative
aggregate demand shock), the Fed would set $r < r^*$ according to the Taylor
Rule. This is called expansionary or stimulative policy. Conversely, where both
inflation and output exceed their respective target values (perhaps due to a
positive demand shock), the Fed would set $r > r^*$ and this would be called
restrictive policy.

The appropriate stance of monetary policy is more difficult if output is less
than its target and inflation greater than its target (as might result from a
negative aggregate supply shock). The Fed often has struggled with what to do in
such a situation. The Taylor rule gives explicit instructions in this case for
policymakers to plug in the exact values for the inflation and output gaps and
set the FFR accordingly; one possibility is for the Fed to raise the real rate
such that $r > r^*$ which would lead to a reduction in inflation but a reduction
in output as well, an unpleasant tradeoff to policymakers.

Implementation of the Taylor Rule is difficult in practice because there are
several measures of price inflation from which the Fed can choose (such as the
total vs. core measures of inflation); and because it has to utilize a
statistical estimate of potential GDP (since potential GDP is never actually
observed); and because empirical coefficient values for the inflation and output
gap terms must be chosen.

The Taylor rule usually is expressed in terms of contemporaneous values on
inflation and output, but given the existence of lags in the macroeconomic impact
of monetary policy, one could use forecast values for inflation and output, so
that the monetary policy rule could be made forward-looking; the professional
literature suggests that such a change makes for better policy, but surprisingly
(at least to me) not by much. Note that under the Taylor rule, the Fed does not
react directly to asset price movements, i.e., it does not react to perceived
asset price bubbles, such as housing or stock-market price bubbles; the Fed
reacts only indirectly to the extent that asset price bubbles affect GDP and
overall price inflation.

Also, the formal math structure of the Taylor rule, as well as our theoretical
policy rule above, does not allow for a period of recognition and deliberation
and hence suggests that policy moves are automatically taken in response to gaps.
In reality, monetary policy is not "automatic" but rather has a "discretionary"
element in the sense that decisions are the result of careful deliberation,
followed by a vote, before the Federal funds rate is changed.

For a numerical example using the Taylor Rule, suppose initially that the output
and inflation gaps are zero, in which case the Fed would set the nominal funds
rate at its desired long run value, $r^* + \pi^*$. Substituting in reasonable
values of 0.5% for $r^*$ and 2% for $\pi^*$ implies that the Fed would set the
nominal funds rate at 2.5% per annum ($FFR = 0.5\% + 2\% + 0 + 0$). If there was
an inflationary shock, the authorities would raise the funds rate by 1.5 times
the change in the inflation rate (to confirm this, take the derivative,
$dFFR/d\pi$, for a given output gap, and show that it equals 1.5). Again
starting from equilibrium, a 1 percentage point rise in inflation would lead to
an increase in the nominal funds rate from 2.5% to 4.0% per annum. This implies
that the real funds rate would increase from 0.5% to 1.0% as inflation rises.

The coefficient levels of 0.5 were inferred by Taylor from properties of large
models of the time, though later research has shown that larger response
coefficients (especially on the inflation term) would make the rule even more
stabilizing. By plugging historical values of the right-hand-side variables into
the Taylor equation, it can be seen that the equation generates a path for the
funds rate that tracks the actual path relatively well; that is, the Taylor rule
seems to explain actual monetary policy behavior fairly well, at least from the
late 1980s. Taylor uses his rule to show that in the 1965-1979 period, the time
of accelerating inflation in the U.S., policy was too easy (in the sense that the
FFR demanded by his equation for that period exceeded the FFR actually chosen by
the Fed) and in the 1981-1985 period policy was too tight. Orphanides shows that
Taylor's results become muddled when the actual (real time) data that were
available to policymakers at the time are inserted into the rule (as opposed to
inserting heavily-revised current estimates of the data of that period).
Specifically, Orphanides' results suggest that monetary policymakers in these
earlier periods followed a sensible lean-against-the-wind strategy but had bad
estimates of the right-hand-side variables (in particular, their estimate of real
potential GDP in the 1965-1979 period was too large) and hence made bad policy
decisions.

## B. Discretionary Fiscal Policy

This section explores empirical aspects of "discretionary" changes to government
spending and taxation, including the use of fiscal policy as a
countercyclical/stabilization tool.

Before beginning with the analysis, I want to provide some background information
on federal government spending and taxes in the United States. The variable, $G$,
denotes spending on goods and services mostly including defense spending on goods
(such as tanks, rifles, ships, jets, computers, etc.) and spending on government
employee compensation (including defense and civilian workers). Taxes, $T$,
mostly include revenue from personal and corporate income taxes and from payroll
taxes, and to a far lesser extent, from excise (sales) taxes and tariffs.
Transfer payments mostly include social security retiree benefits, Medicare and
Medicaid medical outlays, unemployment insurance benefits, the earned income tax
credit, veterans benefits, and food stamps. Interest payments on the government
debt, $iD_{t-1}$, are transfers from an economic perspective but are officially
counted as a different category. Now to the analysis.

The most common summary measure of fiscal policy is the actual budget surplus,
$S$, defined as tax receipts minus total government spending. Taxes in most
countries depend positively on income; as income declines, for example, income
taxes fall "automatically." Also certain transfer payments depend negatively on
income (e.g., unemployment insurance benefits rise automatically as the
unemployment rate rises or as income falls). The components of taxes and spending
that depend on income are called the automatic fiscal stabilizers; for example,
as income declines by a dollar taxes fall about 20 cents in the U.S. thus
providing an automatic—but partial—offset to the decline in income. Taxes net of
transfer payments (or net taxes, for short), $T^n$, depend positively on income.
In math terms, $dT^n(Y)/dY > 0$ for all values of $Y$.

This allows us to write the actual budget surplus as: 
$$S(Y) = T^n(Y) - iD_{t-1} - G$$

If $S = 0$, we have a "balanced budget." I will define the actual budget deficit
as: $-S = G + iD_{t-1} - T^n(Y)$. The primary budget deficit (deficit excluding
interest payments) is defined as: $P = G - T^n(Y)$. [Technical note: in
discussions of the budget deficit and related fiscal measures, all the budget
variables—i.e., $S$, $T$, $D$, $G$, and $P$—are commonly given in nominal terms
even though variables such as $T$ and $G$ are expressed in real terms in our
macro model.]

A common measure of the stance of discretionary fiscal policy is called the
"High-Employment Budget Surplus" (or HEB, for short). It also is called the
"Cyclically-Adjusted Budget Surplus" or the "Structural Budget Surplus." This
measure starts with the actual budget surplus defined above (= tax receipts -
spending) and removes the components of taxes and spending that result from the
deviation of GDP from its potential level. Thus, the measure adjusts the actual
surplus for cyclically-induced swings in economic activity, that is, for the
effects on the budget of the automatic fiscal stabilizers.

More precisely, let the high-employment budget surplus be denoted by $HEB =
S(Y_p)$. This dollar surplus is taxes net of transfer payments ($T^n$) minus
interest payments on government debt minus government expenditures on goods and
services, i.e., $S(Y_p) = T^n(Y_p) - iD_{t-1} - G$ where net taxes are evaluated
at potential GDP, and $G$, $i$, and $D$ are assumed independent of GDP. In
particular high employment net taxes are positively related to potential GDP: in
math terms, $dT^n(Y_p)/dY_p > 0$.

By adding and subtracting $T^n(Y)$ to the high-employment surplus, we get:
$$S(Y_p) = T^n(Y_p) - iD_{t-1} - G = T^n(Y_p) - T^n(Y) + T^n(Y) - iD_{t-1} - G 
= S(Y) + T^n(Y_p) - T^n(Y)$$

Thus the high-employment budget surplus equals the actual budget surplus plus a
cyclical-adjustment term that captures the effect on net taxes of $Y$ differing
from $Y_p$. The cyclical adjustment term is: $T^n(Y_p) - T^n(Y)$.

For example, if $Y < Y_p$ (think of the economy as being in a recession), then
actual net taxes are less than net taxes evaluated at potential GDP and thus the
actual budget surplus is less than the high-employment surplus. Indeed the
high-employment surplus originally was developed to teach policymakers intent on
balancing the actual budget that there was no need to cut spending or raise taxes
during a recession if policymakers would simply keep the high-employment surplus
in balance (make certain you understand this point). Failure to appreciate this
point would lead policymakers to raise taxes and cut government spending during
recessions to balance the actual budget; of course, these actions would produce
an even deeper recession (by shifting the IS and AD curves to the left).

Period-to-period changes in the dollar value of the cyclically-adjusted budget
surplus obviously do not reflect business-cycle swings in economic activity
(hence the name cyclically-adjusted deficit) but do reflect several other
factors, such as the impact of legislative policy actions (i.e. discretionary
policy actions), the impact of demographic influences (like retirement of the
baby boomers) on social security and Medicare outlays, and the impact of changes
in interest rates on interest payments on Treasury debt. Although the HEB thus is
capturing several "non-fiscal policy" factors, it is viewed as a reasonable
measure of the stance of discretionary fiscal policy. Loosely speaking, any of
the non-interest-rate factors that increase (reduce) the cyclically adjusted
budget surplus shift the IS curve to the left (right), rather than capturing
movements along the curve. (Arguably, a change in interest rates is a better
reflection of monetary policy than fiscal policy and so interest payments on
Treasury debt sometimes are excluded from the measure.)

Let's consider some practical applications of these principles. For example, if
policymakers tried to offset the increase in the budget deficit resulting from
the contracting economy during the financial crisis recession of 2008-2009, they
would have raised taxes (or cut spending) about 2% of GDP according to CBO
estimates; this is a very large amount and would have deepened the recession.
Evidently having learned the main lesson of the HEB—not to cut spending or
increases taxes during a recession—fiscal policymakers were willing to let the
size of the deficit take a backseat to the plunge in real economic activity in
the U.S. in 2008 and, more recently, in 2020; indeed huge deficit-increasing
stimulus was enacted in response to the deep recessions associated with the 2008
financial crisis and the 2020 corona virus pandemic.

## C. Limits to Stimulative Discretionary Fiscal Policies

In module 3, Friedman's model demonstrated that getting the right timing and
magnitude for either stimulative or restrictive policy were difficult and hence
posed limits to policy. In this section we examine practical quantitative limits
related to the magnitude of stimulative fiscal policy, a topic of growing
importance in the United States and abroad. We have briefly discussed the limits
to discretionary monetary policy imposed by the zero lower bound on the federal
funds rate; my course on monetary economics (Econ 111) discusses this in more
detail.

**Limits to Discretionary Fiscal Policy:** Of course, deficit-increasing
short-run fiscal stimulus leads to an increase in government debt over time. By
definition, the change in the stock of government debt outstanding equals the
budget deficit; thus, if the deficit is $100 this year, the stock of debt rises
by $100 between the beginning and end of the year.

Let $D_t$ denote the government debt outstanding at time $t$ and let $S_t$ denote
the budget surplus during period $t$ as defined above:
$$
S_t = T^n(Y) - iD_{t-1} - G_t
$$

Thus,
$$
\Delta D_t = D_t - D_{t-1} = -S_t = G_t + iD_{t-1} - T^n(Y)
$$

The right-hand side is called the total budget deficit, and $G_t - T^n(Y) = P$ is
called the "primary" budget deficit. This implies:
$$
\frac{\Delta D_t}{D_{t-1}} = \frac{P}{D_{t-1}} + i
$$

where the left-hand side is the growth rate of debt and the right-hand side is
the primary deficit ratio plus the interest rate.

The debt dynamics equation shows that debt grows when there is a primary deficit
or when interest payments exceed primary surpluses. This relationship is
fundamental to understanding fiscal sustainability and the limits of stimulative
fiscal policy.
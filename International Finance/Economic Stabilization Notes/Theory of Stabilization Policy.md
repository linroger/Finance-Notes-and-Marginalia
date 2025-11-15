---
aliases:
- ITC
- Lucas critique
- Milton Friedman
- Investment Tax Credit
- Policy Lags
- Stabilization Theory
cssclasses:
- academia
key_concepts:
- countercyclical policy issues
- destabilizing policy effects
- expectations and actions
- inside and outside lags
- investment tax credit
- policy intervention timing
- Lucas critique
- Friedman model
- policy magnitude
- policy correlation
- optimal stabilization
- variance minimization
- macroprudential policy
- great moderation
- Option sensitivity analysis
- Delta, gamma, vega, theta, rho
- Futures contracts and forward pricing
- Margin requirements and clearing
- Value at risk and stress testing
- Portfolio risk metrics
linter-yaml-title-alias: Theory of Stabilization Policy
tags:
- portfolio-theory
- inside_lags
- monetary_policy
- greeks
- volatility
- countercyclical_policy
- outside_lags
- futures
- destabilizing_policy
- risk_management
- stabilization_policy
- options
- structured_finance
- mathematical-finance
- policy_timing
title: Theory of Stabilization Policy
---

# Theory of Stabilization Policy

## Overview

**1.** In the macroeconomic model developed in the prior module, it was seen that
fiscal and monetary policy could offset completely and instantaneously shocks to
aggregate demand. However, in practice there is uncertainty about the right
magnitude and timing of policy intervention to neutralize current and projected
fluctuations in income. As a result, policy can be destabilizing: you can have
the right magnitude but bad timing, or you can have good timing but the wrong
amount. 

As an example of the former destabilizing policy, a poorly-timed tax cut during a
recession may boost aggregate demand after the economy already has started to
boom. The poor timing could result from "inside lags," that is, the lags
associated with recognizing the need for action and the inevitable delay in
policy response; it also could result from "outside" lags, that is, the lag
associated with the time between policy action and its effect on the economy. It
is not just that there are inside and outside lags but that there is uncertainty
about the lag times; put another way, if the lag times were known with certainty
then having good timing would be much easier. Other reasons for poor timing are
covered in points 2 and 3 below. 

As an example of the latter destabilizing policy, consider a well-timed monetary
action that recognizes the 12 to 18 month lag between action and maximum economic
effect; also assume the policy is based on a forecast of an over-heated economy
12 to 18 months in the future. However, an overly aggressive increase in interest
rates may send the economy into recession and thus destabilize; this may occur
because there is always some question about the size of monetary (or fiscal)
change needed because of uncertainty about the quantitative macroeconomic impacts
of any given policy action. These basic ideas were initially explored formally by
Milton Friedman and are developed below beginning on page 3. Milton Friedman,
"The Effects of a Full-Employment Policy on Economic Stability," in Essays in
Positive Economics, 1953.

**2.** Bad timing can result from households and firms forming expectations of
policies and acting on them. Indeed, a policy intended to be countercyclical can
turn out to be procyclical. For example, when a temporary subsidy for the
purchase of new capital goods (the so-called investment tax credit or ITC) is
initially enacted to fight recessions by boosting investment demand, it probably
works as businesses use the tax incentive to buy new capital goods. After being
used a couple of times, its enactment probably becomes expected by firms who
delay new investments (waiting for the ITC to be enacted) as the economy is
turning down, exacerbating the downturn. 

Note that the policy action, enactment of the ITC, occurs after the initial
economic effect (i.e., the delay of new investments) because enactment was
anticipated. The outside lag is negative. Similarly, firms likely start investing
more after the ITC is enacted and as the economy is already on the way back up.
That is, the ITC becomes procyclical, exacerbating both downturns and upturns.
This is a prime example of the so-called "Lucas critique" which is the idea that
the initial response to a policy action occurs as soon as future implementation
of the policy becomes anticipated by firms and individuals, and that response may
be the opposite of desired by policymakers; at the time of implementation of the
policy, the response again may be the opposite of that desired by policymakers.
The profession accepts this as a very useful methodological warning, although
there has been a substantial debate over the empirical relevance of the critique.

**3.** Bad timing/magnitude of policy also can result from uncertainty in real
time about the meaning of incoming data on the state of the economy; indeed, data
are frequently revised and some series, such as potential GDP and the associated
GDP gap, are never observed yet historically have served as a basis for policy
decisions. There also is uncertainty about the state of the economy when policy
actions will take effect in the future (this is closely related to "outside"
lags). With all this uncertainty, perhaps the vigor with which stabilization
policy is pursued should be scaled back.

**4.** Moreover, Robert Lucas has argued that even if macroeconomic stabilization
works perfectly in the sense of eliminating all fluctuations in aggregate
economic activity around trend, the utility gain is minimal; if true,
stabilization policy should be abandoned or at least scaled back substantially.
This has led to a very lively debate with several strong counterarguments
(discussed in depth below).

**5.** There is another argument that perfect macroeconomic stabilization is not
as good an idea as one might initially think, addressed in late 2013 by former
Fed Chairman Ben Bernanke. It is argued that a period of sustained economic
stability—at least partially a result of good stabilization policy—such as the
Great Moderation discussed in module 1 sows the seeds of its eventual downfall.
The idea is that investors, financial firms, and financial regulators during the
Great Moderation (especially in the late 1990s and early 2000s) were lulled into
paying insufficient attention to risks that were building, and this led to
excessive risk taking that contributed to a disastrous outcome for the financial
system and the overall economy.

This experience raises the question of whether policy can be so successful at
eliminating cyclical fluctuations in the economy that it leads to excessive
private risk taking. I am unaware of empirical research establishing that
businesses take into account changes in the capacity of policymakers to carry out
successful stabilization policy in making private decisions. But even if
businesses are inclined to take excessive risks during sustained periods of
macroeconomic stability, it does not follow that traditional fiscal and monetary
stabilization policies should be abandoned. Rather, they need to be augmented in
other ways. For example, Bernanke argues that "even in stable and prosperous
times, monetary policymakers and financial regulators should regard safeguarding
financial stability to be of equal importance as (indeed, a necessary
prerequisite for) maintaining macroeconomic stability." Along these lines, since
the financial crisis of 2007-08, there has been growth in macro-prudential policy
aimed at stabilizing financial markets; aspects of such policy are discussed in
detail in my course on monetary economics (Economics 111) but won't be discussed
here due to lack of time.

**6.** The difficulty of getting the right timing and magnitude of policy is a
useful warning. Indeed, aggregate demand management has been compared to hitting
a moving target in a heavy fog. Nonetheless, interventionist policy can work in
certain circumstances and, in any case, it is carried out in practice. Modern
Keynesians argue that fine tuning every bump and wiggle in output and employment
is a bad idea but that fighting major recessions is appropriate for policy. In
addition to the Lucas argument (point 4 above), RBC/classical economists argue
that demand side policies are inappropriate given that they see the economy as
rapidly self-correcting and see fluctuations as caused by productivity/supply
shocks.

## Milton Friedman's Model

Formally, Friedman's argument begins as follows:

$$Z(t) = X(t) + P(t) \qquad \text{(1)}$$

where $Z$ denotes actual (observed) GDP at time $t$, $X$ denotes aggregate output
(or income) at time $t$ in the absence of a specified policy that intends to keep
the economy at full employment, $P$ denotes the amount of output (or income)
added or subtracted from $X$ as a result of the policy.

Note that $P$ does not only measure the effect of the countercyclical actions
taken at $t$. It measures the combined effect at time $t$ of action whenever
taken. It may reflect action taken much earlier or even reflect action to be
taken in the future in so far as anticipation that such action will be taken
affects income in period. The sum of $X$ (i.e. output in the absence of policy)
and $P$ (output attributable to policy) is actual output, $Z$. The variables can
be in either nominal or real terms, although it probably is better to think in
real terms in order to relate this to our previous macro model. For simplicity,
assume that all variables are trendless (stationary) because we are concerned
with fluctuations and not levels or growth; we could equally well define the
variables as deviations from trend. Finally, policy depends on the state of the
economy in the absence of policy, i.e., $P$ depends on $X$. For example, when $X$
changes for some exogenous reason, policy can react pro-cyclically,
counter-cyclically, randomly, or not at all. You should think about the
difficulties facing policymakers trying to react in real time.

## Magnitude and Timing

In the Friedman model, we measure the magnitude of fluctuations by the variance.
Let $V = \sigma^2$ denote variance, where $\sigma$ denotes the standard
deviation. In the case of $P$, for example, the variance of $P$ is denoted as
$V(P) = \sigma^2_P$. This variance would be zero if no policy action were taken.
Also let $\rho$ denote the simple contemporaneous correlation coefficient between
$X$ and $P$.

From basic probability theory, we know that $Z = X + P$ implies (you should
memorize this result):

$$
\begin{aligned}
V(Z) &= V(X) + V(P) + 2\cdot COV(X,P) \\
&= V(X) + V(P) + 2\rho\sigma_X\sigma_P \\
&= \sigma^2_X + \sigma^2_P + 2\rho\sigma_X\sigma_P
\end{aligned}
\qquad \text{(2)}
$$

In this equation, $\sigma_P$ measures the magnitude of the policy intervention's
effect on income, and $\rho$ measures its timing or "fit" or sign. Policymakers
choose $\rho$ and $\sigma_P$ to minimize the fluctuations in GDP, i.e., to
minimize $V(Z)$ [technically it is to minimize the fluctuations of $Z$ relative
to its target level, as discussed in the prior section].

If countercyclical policy were always timed correctly, its effects (i.e., $P$)
would uniformly be in the opposite direction to the deviation of $X$ from its
mean. In this case, $P$ would be perfectly negatively correlated with $X$, and
$\rho$ would equal -1. Of course, policymakers would love this to be the case,
namely that they always timed policy correctly. In reality, however, policymakers
do not always time their actions correctly because they do not know the complete
structure of the economy and do not even know perfectly the state of the economy
(due to data lags and revisions as well as imperfections in forecasting future
activity, as discussed above). Humble policymakers should take this uncertainty
into account, perhaps by taking actions based on imperfect timing (i.e., based on
a value of $\rho$ greater than -1 in algebraic terms); this is discussed more
fully below.

In the case of perfect timing, i.e., if $\rho$ equals -1, all observations would
lie on a downward-sloping straight line passing through the mean of $X$ and $P$.
This assumes that cycles are symmetrical about the mean. If policy were
completely random in its impact, $\rho$ would be zero (that is, policy is just as
likely to be in the right direction as in the wrong direction). If policy were
always timed perversely in the sense that its impacts were always in the same
direction as the deviation of $X$ from its mean, then $\rho$ would equal +1; all
observations would lie on an upward-sloping straight line running through the
mean of $X$ and $P$. Now let's turn to some numerical examples:

Assume the full employment or natural level of income is 100 and that we want
actual income $Z = 100$; assume $Z_0 = 100$. Also assume $E(P) = 0$ and $E(X) =
100$. In each case below, $X$ is assumed to take on a "boom" value of 110 and a
"recession" value of 90.

### Case 1: Perfect countercyclical policy
- $Z = X + P$
- $100 = 110 - 10$
- $100 = 90 + 10$

In this case, $V(X) = V(P) = 200$ and $\rho = -1$ and $V(Z) = 0$.

### Case 2: Perfect timing and intervention is stabilizing, but too small
- $105 = 110 - 5$ [intervention is in the right direction, but 
  $V(X) > V(P) = V(Z) > 0$]
- $95 = 90 + 5$

### Case 3: Perfect timing but intervention is destabilizing
- $85 = 110 - 25$ [$V(P) > V(Z) > V(X)$]
- $115 = 90 + 25$

### Case 4: Correct size but bad timing (i.e., wrong sign, with $\rho = +1$)
- $120 = 110 + 10$ [$V(Z) > V(X) = V(P)$]
- $80 = 90 - 10$

From these examples, we conclude that policy is destabilizing if $V(Z) > V(X)$
and it is stabilizing if $V(Z) < V(X)$.

Under what general conditions is policy stabilizing, i.e., when does $V(Z) <
V(X)$? Divide the above expression by $V(X)$:

$$
\frac{\sigma_Z^2}{\sigma_X^2} = 1 + \frac{\sigma_P^2}{\sigma_X^2} + 
2\rho \frac{\sigma_P}{\sigma_X}
$$

$$
\frac{\sigma_Z^2}{\sigma_X^2} \leq 1 \quad \text{if and only if} \quad 
\rho \leq \frac{-\sigma_P}{2\sigma_X} \qquad \text{(3)}
$$

Even if $V(X) = V(P)$, the policy is stabilizing only if $-1 < \rho < -1/2$,
i.e., only if the policy also is properly "timed." If $V(X) = V(P)$ and $\rho = 
-1$, then $V(Z) = 0$. The fact that the largest negative value for $\rho$ is -1
places an upward limit on the size of the policy intervention. That is, it is
possible for policy to be destabilizing even if it is perfectly "timed" with
$\rho = -1$; this can happen if $\sigma_P > 2\sigma_X$, i.e., if the policy
intervention is too large (case 3 above).

For a given value of $\rho$, what is the best value for $V(P)$? Is the optimum
value for $V(P)$ equal to zero (i.e., do nothing) if policy is perversely timed
(i.e., if the correlation is nonnegative)? To determine the optimum,
differentiate the right-hand side of equation 2 with respect to $\sigma_P$ and
set the result equal to zero:

$$
\sigma_P^* = -\rho \sigma_X
$$

So if $\rho = 0$, the optimum $\sigma_P$ is zero (do nothing). This also is true
for $\rho > 0$.

If $\rho = -1$, the optimum is $\sigma_P = \sigma_X$ with the variance of $Z$
completely eliminated, as illustrated in the example ("perfect policy") above.
*This analysis implicitly assumes that policymakers (i) know and use the true
value of $\rho$ (=-1 in this case) and (ii) know and use the true value of
$\sigma_X$.*

We can substitute the optimum value of $\sigma_P$ ($= -\rho \sigma_X$) into the
right-hand side of equation 3 to determine the maximum reduction in variance of
$X$ capable of being achieved as a function of $\rho$:

$$
\left(\frac{\sigma_Z^2}{\sigma_X^2}\right) = (1 - \rho^2)
$$

This can be re-written as:

$$
\sigma_Z^2 = (1 - \rho^2) \sigma_X^2 \qquad \text{(4)}
$$

With perfect timing and correct magnitude (i.e., $\rho = -1$ and $\sigma_P = 
\sigma_X$), the variance of income is reduced from $\sigma_X^2$ to zero, the
maximum possible reduction achievable. With less favorable timing (e.g., $\rho = 
-0.5$), the variance of income is reduced from $\sigma_X^2$ to $0.75 \sigma_X^2$.
As the timing gets worse (i.e., as $\rho$ approaches zero), the reductions in
variance are smaller. At the limit ($\rho = 0$), the variance is not reduced at
all.
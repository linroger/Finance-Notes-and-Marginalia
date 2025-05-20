---
tags:
  - american_style_derivatives
  - exercise_strategy
  - numerical_techniques
  - option_pricing
  - stopping_time
aliases:
  - American derivatives
  - Derivative valuation
  - Early exercise
key_concepts:
  - American-style derivative
  - Closed-form pricing formulas
  - Exercise strategy
  - Holder exercise right
  - Optimal exercise strategy
  - Stopping time
---

# 12.5 American-style derivatives  

Consider an [American-style derivative](.md) where the holder has the right to choose when to exercise the derivative, at least within some limits. Typically exercise can take place at the [expiration date](../../../Financial%20Instruments/Financial%20Derivatives%20and%20Quantitative%20Methods/Risk%20Neutral%20Pricing%20of%20Options.md) $T$ or at any time before $T$ . Let $P_{\tau}$ denote the payoff if the derivative is exercised at time. $\tau\leq T$ In general,. $P_{\tau}$ may depend on the evolution of the economy up to and including time. $\tau$ , but it. is usually a simple function of the time. $\tau$ price of an underlying security or the time. $\tau$ value of a. particular interest rate. At each point in time the holder of the derivative must decide whether or not he will exercise. Of course, this decision must be based on the available information, so we are seeking an entire [exercise strategy](.md) that tell us exactly in what states of the world we should exercise the derivative. We can represent an [exercise strategy](.md) by an indicator function $I(\omega,t)$ which for any given state of the economy $\omega$ at time $t$ either has the value $^{1}$ or $0$ , where the value $^{1}$ indicates exercise and $0$ indicates non-exercise. For a given [exercise strategy](.md) $I$ , the derivative will be exercised the first time $I(\omega,t)$ takes on the value 1. We can write this point in time as  
$$
\tau(I)=\operatorname*{min}\{s\in[t,T]\mid I(\omega,s)=1\}.
$$  

This is called a [stopping time](.md) in the literature on stochastic processes. By our earlier analysis, the value of getting the payoff $V_{\tau(I)}$ at time $\tau(I)$ is given by $\operatorname{E}_{t}^{\mathbb{Q}}\left[e^{-\int_{t}^{\tau(I)}r_{u}d u}P_{\tau(I)}\right]$ If we let $\mathbb{J}[t,T]$ denote the set of all possible exercise strategies over the time period $[t,T]$ , the time $t$ value of the [American-style derivative](.md) must therefore be  
$$
V_{t}=\operatorname*{sup}_{I\in\mathcal{I}[t,T]}\mathrm{E}_{t}^{\mathbb{Q}}\left[e^{-\int_{t}^{\tau(I)}r_{u}d u}P_{\tau(I)}\right].
$$  

An [optimal exercise strategy](.md). $I^{*}$ is such that.  
$$
V_{t}=\mathrm{E}_{t}^{\mathbb{Q}}\left[e^{-\int_{t}^{\tau(I^{*})}r_{u}d u}P_{\tau(I^{*})}\right].
$$  

Note that the [optimal exercise strategy](.md) and the price of the derivative must be solved for simultaneously. This complicates the [pricing](../../Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%207/Arbitrage%20Pricing%20of%20Derivatives.md) of American-style [derivatives](../../Financial%20Trading%20and%20Markets/Chapter%209%20Arbitrage%20and%20Hedging%20With%20Options.md) considerably. In fact, in. all situations where [early exercise](../../Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%2016/Bond%20Futures%20Options.md) may be relevant, we will not be able to compute closed-form. [pricing](../../Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%207/Arbitrage%20Pricing%20of%20Derivatives.md) formulas for American-style [derivatives](../../Financial%20Trading%20and%20Markets/Chapter%209%20Arbitrage%20and%20Hedging%20With%20Options.md). We have to resort to numerical techniques. See. Hull (2o06) for an [introduction](../../../Financial%20Markets%20and%20Institutions/III.%20Liquidity%20of%20Assets/Class%209-%20Bailouts%20and%20Bank%20Failures/Squam%20Lake%20Group%20Introduction.md) to the standard techniques of [binomial](../../Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%205%20Options%20on%20Prices%20and%20Hedge-Based%20Valuation/A%20Real-Life%20Option%20Pricing%20Exercise.md) or [trinomial trees](../../Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%206%20Options%20on%20Non-Price%20Variables/Arbitrage-Free%20Interest%20Rate%20Models.md), finite difference approximation of the partial differential equation that the [pricing](../../Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%207/Arbitrage%20Pricing%20of%20Derivatives.md) function must satisfy,. and [Monte Carlo simulation](../../../Financial%20Instruments/Pricing%20a%20Callable%20Leveraged%20Constant%20Maturity%20Swap%20Spread%20Note.md).  

It is well-known that it is never strictly advantageous to exercise an American call option on a [non-dividend paying asset](Options.md) before the final maturity date. $T$ , cf. [Merton](../../../Credit%20Markets/Credit%20Markets%20Session%205.md) (1973c) and Hull (2006, Ch. 9). In contrast, premature exercise of an American put option on a [non-dividend paying asset](Options.md) will be advantageous for sufficiently low prices of the [underlying asset](../../../Financial%20Instruments/Financial%20Derivatives%20and%20Quantitative%20Methods/Risk%20Neutral%20Pricing%20of%20Options.md). If the [underlying asset](../../../Financial%20Instruments/Financial%20Derivatives%20and%20Quantitative%20Methods/Risk%20Neutral%20Pricing%20of%20Options.md) pays dividends at discrete points in time, it can be optimal to exercise an American call option prematurely but only immediately before each dividend payment date. Regarding [early exercise](../../Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%2016/Bond%20Futures%20Options.md) of put options, it can never be optimal to exercise an American put on a dividend-paying asset just before a dividend payment, but at all other points in time [early exercise](../../Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%2016/Bond%20Futures%20Options.md) will be optimal for sufficiently low prices of the [underlying asset](../../../Financial%20Instruments/Financial%20Derivatives%20and%20Quantitative%20Methods/Risk%20Neutral%20Pricing%20of%20Options.md)..  
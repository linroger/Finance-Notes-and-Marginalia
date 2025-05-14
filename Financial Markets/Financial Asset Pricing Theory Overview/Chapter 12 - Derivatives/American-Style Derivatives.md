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

Consider an [[American-Style Derivatives|American-style derivative]] where the holder has the right to choose when to exercise the derivative, at least within some limits. Typically exercise can take place at the [[Risk Neutral Pricing of Options|expiration date]] $T$ or at any time before $T$ . Let $P_{\tau}$ denote the payoff if the derivative is exercised at time. $\tau\leq T$ In general,. $P_{\tau}$ may depend on the evolution of the economy up to and including time. $\tau$ , but it. is usually a simple function of the time. $\tau$ price of an underlying security or the time. $\tau$ value of a. particular interest rate. At each point in time the holder of the derivative must decide whether or not he will exercise. Of course, this decision must be based on the available information, so we are seeking an entire [[American-Style Derivatives|exercise strategy]] that tell us exactly in what states of the world we should exercise the derivative. We can represent an [[American-Style Derivatives|exercise strategy]] by an indicator function $I(\omega,t)$ which for any given state of the economy $\omega$ at time $t$ either has the value $^{1}$ or $0$ , where the value $^{1}$ indicates exercise and $0$ indicates non-exercise. For a given [[American-Style Derivatives|exercise strategy]] $I$ , the derivative will be exercised the first time $I(\omega,t)$ takes on the value 1. We can write this point in time as  
$$
\tau(I)=\operatorname*{min}\{s\in[t,T]\mid I(\omega,s)=1\}.
$$  

This is called a [[American-Style Derivatives|stopping time]] in the literature on stochastic processes. By our earlier analysis, the value of getting the payoff $V_{\tau(I)}$ at time $\tau(I)$ is given by $\operatorname{E}_{t}^{\mathbb{Q}}\left[e^{-\int_{t}^{\tau(I)}r_{u}d u}P_{\tau(I)}\right]$ If we let $\mathbb{J}[t,T]$ denote the set of all possible exercise strategies over the time period $[t,T]$ , the time $t$ value of the [[American-Style Derivatives|American-style derivative]] must therefore be  
$$
V_{t}=\operatorname*{sup}_{I\in\mathcal{I}[t,T]}\mathrm{E}_{t}^{\mathbb{Q}}\left[e^{-\int_{t}^{\tau(I)}r_{u}d u}P_{\tau(I)}\right].
$$  

An [[American-Style Derivatives|optimal exercise strategy]]. $I^{*}$ is such that.  
$$
V_{t}=\mathrm{E}_{t}^{\mathbb{Q}}\left[e^{-\int_{t}^{\tau(I^{*})}r_{u}d u}P_{\tau(I^{*})}\right].
$$  

Note that the [[American-Style Derivatives|optimal exercise strategy]] and the price of the derivative must be solved for simultaneously. This complicates the [[Arbitrage Pricing of Derivatives|pricing]] of American-style [[Chapter 9 Arbitrage and Hedging With Options|derivatives]] considerably. In fact, in. all situations where [[Bond Futures Options|early exercise]] may be relevant, we will not be able to compute closed-form. [[Arbitrage Pricing of Derivatives|pricing]] formulas for American-style [[Chapter 9 Arbitrage and Hedging With Options|derivatives]]. We have to resort to numerical techniques. See. Hull (2o06) for an [[Squam Lake Group Introduction|introduction]] to the standard techniques of [[A Real-Life Option Pricing Exercise|binomial]] or [[Arbitrage-Free Interest Rate Models|trinomial trees]], finite difference approximation of the partial differential equation that the [[Arbitrage Pricing of Derivatives|pricing]] function must satisfy,. and [[Pricing a Callable Leveraged Constant Maturity Swap Spread Note|Monte Carlo simulation]].  

It is well-known that it is never strictly advantageous to exercise an American call option on a [[Options|non-dividend paying asset]] before the final maturity date. $T$ , cf. [[Credit Markets Session 5|Merton]] (1973c) and Hull (2006, Ch. 9). In contrast, premature exercise of an American put option on a [[Options|non-dividend paying asset]] will be advantageous for sufficiently low prices of the [[Risk Neutral Pricing of Options|underlying asset]]. If the [[Risk Neutral Pricing of Options|underlying asset]] pays dividends at discrete points in time, it can be optimal to exercise an American call option prematurely but only immediately before each dividend payment date. Regarding [[Bond Futures Options|early exercise]] of put options, it can never be optimal to exercise an American put on a dividend-paying asset just before a dividend payment, but at all other points in time [[Bond Futures Options|early exercise]] will be optimal for sufficiently low prices of the [[Risk Neutral Pricing of Options|underlying asset]]..  
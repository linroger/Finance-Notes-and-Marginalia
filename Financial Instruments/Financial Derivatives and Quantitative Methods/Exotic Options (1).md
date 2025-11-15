---
academic_level: graduate
aliases:
- binary option
- break forward
- digital put
- exotic derivatives
cssclasses:
- academia
enhanced: true
enhancement_date: '2025-11-06'
enhancement_id: batch09-000100
key_concepts:
- Black-Scholes option pricing model and continuous-time finance
- Options Greeks and sensitivity analysis for risk management
- Convexity adjustments and yield curve sensitivity
- Capital Asset Pricing Model (CAPM) and expected returns
- Value at Risk (VaR) and tail risk measurement
- Expected shortfall and coherent risk measures
- Arbitrage opportunities and no-arbitrage pricing
- Factor models and multi-factor pricing
- Risk preference theory and utility functions
- Monte Carlo Simulation Methods for Derivative Pricing
- Auto-Callable Notes and Barrier Options
- Risk Measurement and VaR Backtesting
- Contango, Backwardation, and Roll Yield
- Equity-Linked Notes and Market-Linked Securities
- 'Greeks: Delta, Gamma, Theta, and Vega Hedging'
- Futures and Forward Contracts in Financial Markets
- Option Valuation and Exercise Strategies
- Value at Risk and Expected Shortfall
- Factor Models and Asset Pricing
- Stochastic Integration and Path-Dependent Options
- Hedge Strategies and Basis Risk Management
- Variance Reduction Techniques in Monte Carlo Methods
- Options Trading Strategies and Risk Management
- Structured Products and Principal Protection
- Stress Testing and Extreme Value Analysis
- Fama-French Factors and Style Analysis
- Arbitrage Pricing Theory and Multi-Factor Models
professional_application: theoreti
status: active
tags:
- all-or-nothing
- arbitrage-opportunity
- arbitrage-pricing
- asian-derivatives
- asset-allocation
- average-price-options
- barrier-derivatives
- barrier-options
- binary-derivatives
- binomial-model
- black-scholes-model
- capital-asset-pricing
- caplet
- coherent-risk-measure
- conditional-var
- control-variates
- put-options
- exotic-options
- call-options
- variance-reduction
- principal-protected-notes
- butterfly-spreads
- momentum
- strangles
- expected-shortfall
- straddles
- basis-risk
- parametric-var
- extreme-value-theory
- var-methodologies
- historical-var
- book-to-market
- equity-linked-notes
- contango
- backwardation
- antithetic-variates
- random-walks
- covered-calls
- volatility-analysis
- style-analysis
- least-squares-mc
- option-strategies
- stress-testing
- clearinghouse
- investment-analysis
- portfolio-optimization
- marking-to-market
- path-dependency
- value-at-risk
- auto-callables
- arbitrage-pricing-theory
- monte-carlo-simulation
- hedge-ratio
- multi-factor-models
- structured-notes
- market-linked-notes
- iron-condors
- protective-puts
- financial-markets
- size-effect
- factor-models
- knock-out-options
- value-factor
- reverse-convertibles
- monte-carlo-var
- risk-management
- convergence
- options-trading
- var-backtesting
- futures-contracts
- roll-yield
- quasi-monte-carlo
- apt
- stochastic-integration
- forward-contracts
- fama-french
title: Exotic Options
type: note
---
--



# Exotic Options

## Exotic Options

Exotic Options]]

These notes describe the payoffs to some of the so-called erotic options. There are a variety of different types of exotic options. Some of these options are path-dependent,  so that the value of the option depends on the previous values of the underlying as well as the current price of the underlying.

Keywords: Digital options,  Barrier options,  Path-dependent options,  Lookback options,  Asian options.

### Introduction

American and European puts and calls are sometimes referred to as plain vanilla options. There are,  however,  a wide variety of other types of options that are traded. These are sometimes referred to as exotic options. In the past,  most exotic options were traded in over-the-counter markets rather than exchanges,  but more recently,  these alternative option types can be found on exchange markets too. The variety and types of options that are available are really only limited by imagination. As long as the payoff can be well specified,  it can depend on any property of the price of the underlying asset. The following list just gives a few examples.

## Digital Options

One simple type is the digital or binary option. The payoff to a digital option depends on whether the price of the underlying asset at maturity is greater

or less than the strike price. Thus,  for a digital call option,  the payoff at maturity is:
$$c_T^b=\left\{\begin{array}{ll}0&\text{if}S_T\leq X\\1&\text{if}S_T>X\end{array}\right.$$

And the payoff at maturity to a digital put option is
$$p_T^b=\left\{\begin{array}{ll}1&\text{if}S_T\leq X\\0&\text{if}S_T>X.\end{array}\right.$$

## Range Forward Contract

A range forward contract specifies a band $[X_{2},     X_{1}]$. If the price of the underlying at maturity is within the band,  then the holder is obliged to buy the asset at its current price. If the price of the underlying at maturity is below $X_{2}$,  then the holder has to buy at $X_{2}$,  and if the price of the underlying at maturity is above $X_{1}$,  then the holder has to buy at $X_{1}$. The range forward is designed so that the initial value of the contract is zero and therefore similar to a forward contract. It is equivalent to a combination of a long call option with a strike price of $X_{1}$ and a written put option with a strike price of $X_{2}$,  where the strike prices are chosen so that the put and the call have the same prices. The payoff at maturity to a range forward contract is $\operatorname*{max}[S_{T}-X_{1},     0]-\operatorname*{max}[X_{2}-S_{T},     0]$.

### Break Forward

A break forward contract specifies a delivery price $K$ and a break price $B$ at which the forward price can be broken. Thus,  at the maturity date,  the break price will be paid on a long forward position if $-B>S_{T}-K$. For example,  if the break price is $\$10$ and the delivery price is S 100,     the payoff to the long forward position is $S_{T}-100$. If $S_{T}<90$ ,     there will be a loss of more than S 10,     and it will be worthwhile to pay the break price of $\$10$. The payoff

At maturity is therefore $\operatorname*{max}[S_{T}-100,     -10]=\operatorname*{max}[S_{T}-90,     0]-10$. This then is just like a call option with a strike price of $S_{ 90}$ but where a payment of $\$10$ is paid at maturity. Since the break forward costs nothing when it is initiated,     it is essentially a deferred payment option,     where the payment of the initial cost of the option is deferred until maturity. Suppose that the interest rate until maturity is $\frac{1}{9}$ ,     then in our example a call option with a strike price of $\$90$ which costs $\$9$ is equivalent to a long break forward with a delivery price of $\$100$ and break price of $\$10$. In general,     letting $ 7$ denote the interest to maturity and $C_{t}$ the current price of the call option with a strike price $X$ ,     then the call option is equivalent to a long position in a break forward contract with delivery price $X+(1+r) c_{t}$ and break price $(1+r) c_{t}$.

## Rainbow Options

It is possible to write options on more than one underlying asset. Such options are called rainbow options. For example,  a put option may specify that you have the option to deliver one from a range of different assets. Clearly,  if the exercise price is the same for all assets specified,  and if you decide to exercise your option to sell,  you will choose to deliver that asset with the lowest current price. Thus,  if there are two assets specified and their prices are $S^{1}$ and $S^{2}$ ,  then the intrinsic value of the put option is
$$x\text{Intrinsic value}=\left\{\begin{array}{ll}X-\min[S[^1],     S[^2]]&\text{if}\min[S[^1],     S[^2]]\leq X\\0&\text{if}\min[S[^1],     S[^2]]>X.\end{array}\right.$$

## "As-you-like-it" Options

This is an option where the holder can decide at a specific time whether the option is a put or a call option. Suppose that the decision must be made at $t$ . The value of the option at this time is $\max[c_{t},     p_{t}]$. If the as-you-like-option offers the choice between a European put and a European

Call with the same strike price and same maturity date $T$ ,  then the put-call parity condition can be used and
$$\max[c_t,     p_t]=\max\left[c_t,     c_t+\frac{X}{(1+r)}-S_t\right]=c_t+\max\left[0,     \frac{X}{(1+r)}-S_t\right]$$

Where $r$ is the risk-free interest rate between $t$ and the maturity date $T$. The as-you-like-it option therefore consists of a portfolio of a call option with strike price $X$ and maturity date $T$ and a put option with strike price $\frac{X}{(1+r)}$ and maturity at date $t$.

## Barrier Options

 Barrier options have a payoff that depends on whether the underlying asset reaches a certain level,  the barrier,  prior to maturity. There are two main varieties of barrier,  prior to maoptions. The knock-in only pays out if the price of barrier and the knock-out only pays out if the underlying does not reach the barrier. These can be further classified by whether the underlying reaches the barrier and the knock-out only pays out if the underlying does not reach the barrier. If the barrier is set above or below the initial value of the underlying,  it is said to be an up option. If the barrier is above the initial value of the underlying,  it is said to bee an up option. The payoff at maturity for a down option
$$c_T^{down-out}=\left\{\begin{array}{lll}c_T&\text{if}\:S_t>B&\text{for all}\: t\leq T\\0&\text{if}\:S_t<B&\text{for any}\: t\leq T\end{array}\right.$$

Whereand $CT$ is the value of the plain vanilla call option. Clearly,  if you own both a down and out call option together with a down and in call option on the same underlying with the same barrier,  strike prices,  and maturity,  then you have a plain vanilla call option. So for calls and puts and down and up options:
$$\mathrm{vanilla}=\mathrm{in}+\mathrm{out}.$$

Barrier options sometimes specify a double barrier with an upper and lower limit. Sometimes the barrier changes over time. Sometimes a rebate is paid if the barrier is hit. Some options become barrier options if a particular value,  usually the strike price,  for the underlying is reached.

### Lookback Options

Lookback options have a payoff that depends on the maximum or minimum value that the underlying asset reaches during the lifetime of the option. The payoff to maturity of a European-style lookback call is $S_{T}-S_{min}$ where $S_{min}$ is the minimum value that the underlying achieves over the option’s lifetime. The payoff to maturity of a European-style lookback put is $S_{max}-S_{T}$ where $S_{max}$ is the maximum value that the underlying achieves over the option’s lifetime. Note that if you hold both a lookback put and a lookback call,  your payoff is $S_{max}-S_{min}$ . It is like you bought when the price was lowest and sold when the price was highest. Of course,  such sweet deals are likely to be costly.

## Asian Options

An Asian option has a payoff that depends on the average price of the underlying asset from its starting date. Thus,  the intrinsic value of an average price Asian call option is $\operatorname*{max}[0,     S_{ave}-X]$ where $S_{ave}$ is the average value of the asset from the start of the option to the current date. Another type of Asian option is the average strike price type,  where the strike price is the average value. In this case,  the intrinsic value of the call is $\operatorname*{max}[0,     S_{t}-S_{ave}]$ and the intrinsic value of the put is $\operatorname*{max}[S_{ave}-S_{t},     0]$.

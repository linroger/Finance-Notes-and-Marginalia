---
academic_level: graduate
aliases:
- Call Option Premium
- Option Pricing Proofs
- Strike Price Relations
cssclasses: academia
enhanced: true
enhancement_date: '2025-11-06'
enhancement_id: batch09-000429
key_concepts:
- Black-Scholes option pricing model and continuous-time finance
- Options Greeks and sensitivity analysis for risk management
- Convexity adjustments and yield curve sensitivity
- Arbitrage opportunities and no-arbitrage pricing
- Volatility modeling and estimation techniques
- Risk preference theory and utility functions
- Sensitivity analysis and Greeks calculation
- Financial modeling and quantitative analysis
- Risk management and portfolio optimization
- Derivatives pricing and hedging strategies
- Market risk measurement and control
- Credit Risk Management and Default Probability
- Expected Loss and Loss Given Default Models
- Risk Measurement and VaR Backtesting
- Bid-Ask Spreads and Market Impact
- 'Greeks: Delta, Gamma, Theta, and Vega Hedging'
- Ornstein-Uhlenbeck Process in Finance
- Option Valuation and Exercise Strategies
- Value at Risk and Expected Shortfall
- Credit Spreads and Rating Migration Analysis
- Factor Models and Asset Pricing
- Vasicek Interest Rate Model and Mean Reversion
- Short Rate Models and Term Structure Dynamics
- Market Microstructure and Liquidity Analysis
- Price Discovery and Market Efficiency
- Options Trading Strategies and Risk Management
- Stress Testing and Extreme Value Analysis
- Fama-French Factors and Style Analysis
- Arbitrage Pricing Theory and Multi-Factor Models
professional_application: theoreti
status: active
tags:
- arbitrage-opportunity
- asset-allocation
- binomial-model
- black-scholes-model
- caplet
- continuous-time-pricing
- convexity
- convexity-adjustment
- credit-rating
- delta-hedging
- derivatives
- discrete-time-pricing
- dynamic-hedging
- gamma-hedging
- hedging
- put-options
- affine-term-structure
- recovery-rate
- hull-white
- call-options
- cir-model
- high-frequency-trading
- butterfly-spreads
- momentum
- strangles
- algorithmic-trading
- expected-shortfall
- straddles
- parametric-var
- conditional-var
- extreme-value-theory
- book-to-market
- var-methodologies
- historical-var
- mean-reversion
- lognormal-models
- covered-calls
- ' exposure-at-default'
- style-analysis
- short-rate-models
- option-strategies
- stress-testing
- arbitrage
- unexpected-loss
- ornstein-uhlenbeck
- rating-migration
- expected-loss
- market-efficiency
- credit-migration
- default-probability
- value-at-risk
- order-flow
- credit-spreads
- arbitrage-pricing-theory
- multi-factor-models
- bid-ask-spread
- iron-condors
- protective-puts
- market-price-of-risk
- probabilty-of-default
- price-discovery
- loss-given-default
- size-effect
- factor-models
- liquidity
- value-factor
- vasicek-model
- monte-carlo-var
- var-backtesting
- options-trading
- market-impact
- apt
- risk-premium
- fama-french
title: Appendix 9.B Algebraic Proofs of Strike-Price Relations
type: note
---
--



# Appendix 9.B Algebraic Proofs of Strike-Price Relations

In Chapter 9 we demonstrated several propositions about how option prices change when the strike price changes. To prove these propositions we will consider strike prices $K_1$, $K_2$ and $K_3$, where $K_1 < K_2 < K_3$. Define $\lambda$ so that:

$$\lambda=\frac{K_3-K_2}{K_3-K_1}$$ 

or

$$K_2=\lambda K_1+(1-\lambda)K_3$$

Since we are considering options that differ only with respect to the strike price, we can write $C(K)$ and $P(K)$ to denote the option premium for a particular strike $K$.

### The Call Premium Decreases as the Strike Price Increases

Suppose that $C(K_1) < C(K_2)$; i.e., a lower strike call had a lower premium. To effect arbitrage, we would buy the low-strike call and sell the high-strike call (this is a bull spread). Table 9.10 shows the result. We will consider each entry in the "Total" row separately.

**Time 0.** We earn net premium from selling the more expensive option. The cash flow is positive.

###### Expiration or Exercise, $S_T < K_1$
- Neither option is exercised, so the cash flow is zero.

###### Expiration or Exercise, $K_1 \leq S_T \leq K_2$
- We exercise the option we bought, earning $S_T - K_1$

###### Expiration or Exercise, $S_T > K_2$
- We exercise the option we bought, earning $S_T - K_1$, and the option we sold is exercised, costing us $K_2 - S_T$.
- The net is $K_2 - K_1$ which is positive.

What about the fact that the options are American? We then have to account for the possibility that the written option is exercised. If that happens, we can simply exercise the purchased option, earning the payoffs in the table. If it is not optimal to exercise the purchased option, we can sell it, earning even higher payoffs.

!500  
!500  
!500  

### The Call Premium Changes by Less Than the Change in the Strike Price

Suppose that $C(K_1) - C(K_2) \geq K_2 - K_1$. We can make money initially by selling the $K_1$ strike call, buying the $K_2$-strike call, and lending $K_2 - K_1$. Table 9.11 summarizes the results.

**Time 0.** We earn net premium since the initial assumption is that $C(K_1) - C(K_2) \geq K_2 - K_1$.

**Expiration or Exercise, $S_T < K_1$.** Neither option is exercised, so we keep the future value of the difference between the strikes.

**Expiration or Exercise, $K_1 \leq S_T \leq K_2$.** The written option is exercised, so we have to sell the stock for $K_1$. However, the net loss is less than the difference between the strike prices.

**Expiration or Exercise, $S_T > K_2$.** We keep the interest on the difference between the strike prices.

What adjustments do we have to make if the options are American? If the written $K_1$ option is exercised, we can duplicate the payoffs in the table by throwing our option away (if $K_1 \leq S_T \leq K_2$) or exercising it (if $S_T \geq K_2$). Since it never makes sense to discard an unexpired option, and since exercise may not be optimal, we can do at least as well as the payoff in the table if the options are American. 

You may have noticed that if the options are European, we can put a tighter restriction on the difference in call premiums—namely, $C(K_1) - C(K_2) < \text{PV}(K_2 - K_1)$. We would show this by lending $\text{PV}(K_2 - K_1)$ instead of $K_2 - K_1$. This strategy does not work if the options are American, since we do not know how long it will be before the options are exercised, and, hence, we do not know what time to use in computing the present value.

### The Call Premium Is a Convex Function of the Strike Price

This proposition says that as the option moves more into the money, its premium increases at a faster rate. To prove it, suppose that $C(K_2) \geq \lambda C(K_1) + (1-\lambda)C(K_3)$. We can make money initially by selling the $K_2$-strike call, buying $\lambda$ $K_1$-strike calls, and buying $1-\lambda$ $K_3$-strike calls. Table 9.12 summarizes the results.

!500  

**Time 0.** We earn net premium since the initial assumption is that $C(K_2) \geq \lambda C(K_1) + (1-\lambda)C(K_3)$.

###### Expiration or Exercise, $S_T < K_1$
- No options are exercised

###### Expiration or Exercise, $K_1 \leq S_T \leq K_2$
- The purchased $K_1$ calls are exercised.

###### Expiration or Exercise, $K_2 < S_T \leq K_3$
- We exercise our $\lambda$ $K_1$ calls, and the written $K_2$ call is exercised against us.
- Recall that $K_2 = \lambda K_1 + (1-\lambda)K_3$; substituting this expression for $K_2$ explains how we obtain the total in this column.

###### Expiration or Exercise, $S_T > K_3$
- All options are exercised and the payoffs cancel.

## Puts

Here are the counterpart propositions for puts, stated more formally:

[^1]: The put premium is increasing in the strike price: $P(K_1) \leq P(K_2)$
[^2]: The put premium changes by less than the change in the strike price: $P(K_2) - P(K_1) < K_2 - K_1$
[^3]: The put premium is a convex function of the strike price: $P(K_2) < \lambda P(K_1) + (1-\lambda)P(K_3)$

The proofs are identical to the propositions for calls.

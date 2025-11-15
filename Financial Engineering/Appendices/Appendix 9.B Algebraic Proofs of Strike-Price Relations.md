---
aliases:
- Call Option Premium
- Option Pricing Proofs
- Strike Price Relations
cssclasses: academia
enhanced: true
enhancement_date: '2025-11-06'
enhancement_id: batch03-599b49
key_concepts:
- Apt
- European Options
- Treasury Futures
- American Options
- Interest rate swap valuation and fixed-floating spreads
- Monte Carlo simulation techniques for path-dependent options
- Treasury Bonds
- Real options valuation in corporate investment decisions
- Binomial option pricing model for American-style options
- Greeks calculation and their interpretation in options trading
- Single-name vs. index CDS trading
- Collateralized Debt Obligations
- Option Greeks and portfolio risk management
- Commodity markets and pricing dynamics
- Solution
- Credit spread decomposition and hazard rates
- future value and compounding
- Vega and volatility risk management
- CDS clearing and central counterparties
- Commodity futures pricing and storage costs
- CDS-Bond basis and arbitrrage opportunities
- Swap spread and credit risk considerations
- Mathematical Finance
- Credit default swap pricing and recovery assumptions
- 'Structured products: CDOs, CLOs, and credit derivatives'
- Shadow Banking
- Implied Volatility
- call premium decreases
- Arbitrage Pricing Theory and multifactor models
- Fixed-for-floating swap cash flows and valuation
- Course Material
- Theta and time decay modeling
- Risk-neutral pricing methodology for derivative securities
- International arbitrage and covered interest rate parity
- Synthetic credit derivatives and index trades
- Treasury futures trading and basis point value calculations
- CVA and DVA adjustments in derivative pricing
- Arbitrage opportunities and risk-free profit extraction
- Interest rate swap pricing and valuation
- Credit default swap pricing and risk-neutral probabilities
- present value and discounting methods
- Factor Models
- European option restriction
- Variance swaps and volatility trading strategies
- Delta hedging strategies in options portfolio management
- Theta decay modeling for time-sensitive options strategies
- Implied volatility extraction from market option prices
- Shadow banking system and regulatory arbitrage
- Quantitative Implementation
- Volatility smile and skew modeling in options markets
- Gamma and convexity adjustments
- strike price changes
- Delta hedging and the replication argument
- convex function strike price
- Exotic Options
- Cross-currency basis swaps and funding
- American option exercise
tags:
- financial-analysis
- treasury-futures
- commodities
- credit-default-swaps
- collateralized-debt-obligations
- interest-rate-swaps
- mathematical-finance
- course-material
- shadow-banking
- financial-modeling
- apt
- greeks
- factor-models
- european-options
- quantitative-implementation
- solution
- algebraic-proofs
- treasury-bonds
- american-options
- arbitrage
- call-premium
- exotic-options
- implied-volatility
- strike-price
- quantitative-finance
- dcf-valuation
- monte-carlo
title: Appendix 9.B Algebraic Proofs of Strike-Price Relations
---

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

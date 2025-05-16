---
linter-yaml-title-alias: CALCULATE STOCK PRICES AT DIFFERENT NODES
title: Calculate Stock Prices at Different Nodes
tags:
  - binomial_model
  - european_call
  - option_pricing
  - replicating_portfolio
  - stock_price
aliases:
  - Binomial Option Pricing
  - Option Replication
  - Stock Price Calculation
key_concepts:
  - Binomial tree
  - Option payoff
  - Option price calculation
  - Replicating portfolio
  - Stock price movement
---

# Calculate Stock Prices at Different Nodes

- **[Binomial](Teaching%20Note%204-Multiperiod%20[[A%20Real-Life%20Option%20Pricing%20Exercise) Trees]]**
	- [Financial Instruments]([[A%20Practical%20Guide%20for%20Actuaries%20and%20other%20Business%20Professionals.)/Lecture Notes- [Financial Instruments](../../A%20Practical%20Guide%20for%20Actuaries%20and%20other%20Business%20Professionals..md)/Teaching Note 4-Multiperiod [Binomial](../../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%205%20Options%20on%20Prices%20and%20Hedge-Based%20Valuation/A%20Real-Life%20Option%20Pricing%20Exercise.md) Trees/[Binomial](../../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%205%20Options%20on%20Prices%20and%20Hedge-Based%20Valuation/A%20Real-Life%20Option%20Pricing%20Exercise.md) Option [Pricing](../../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%207/Arbitrage%20Pricing%20of%20Derivatives.md)]]
	- [Binomial Tree]([[Rate%20and%20Price%20Trees) Steps]]
	- [Calculate Stock Prices at Different Nodes](.md)
	- [Options Strategies Construction](Options%20Strategies%20Construction.md)
	- [Binomial](Teaching%20Note%204-Multiperiod%20[[A%20Real-Life%20Option%20Pricing%20Exercise) Trees]]
	- [Financial Instruments]([[A%20Practical%20Guide%20for%20Actuaries%20and%20other%20Business%20Professionals.)/Lecture Notes/Teaching Note 4-Multiperiod [Binomial](../../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%205%20Options%20on%20Prices%20and%20Hedge-Based%20Valuation/A%20Real-Life%20Option%20Pricing%20Exercise.md) Trees/The [Pricing](../../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%207/Arbitrage%20Pricing%20of%20Derivatives.md) of Options and Corporate Liabilities]]

To hedge its risk from writing a European call option with an [exercise price](../../../Financial%20Markets/Financial%20Asset%20Pricing%20Theory%20Overview/Chapter%2012%20-%20Derivatives/Options.md) of$K = 100$in a [two-period binomial model](../../Financial%20Derivatives%20and%20Quantitative%20Methods/The%20T₁%20-period%20Binomial%20Model.md),  the financial intermediary needs to create a [replicating portfolio](Pricing%20Forwards,%20Futures,%20Bonds,%20Swaps,%20Swaptions,%20Caps%20and%20Floors%20under%20No-Arbitrage%20and%20Risk-Neutral%20Pricing.md) that mirrors the option's payoffs in all states of the world by the end of the periods. We will set up this [replicating portfolio](Pricing%20Forwards,%20Futures,%20Bonds,%20Swaps,%20Swaptions,%20Caps%20and%20Floors%20under%20No-Arbitrage%20and%20Risk-Neutral%20Pricing.md) and determine the initial cost (price of the call option),  the delta ($\Delta$,  the number of shares of the stock to hold),  and the amount of borrowing or lending required (denoted as$B$) at each node.

## STEP 1: CALCULATE THE STOCK PRICE MOVEMENT

Given:$S_0 = 100$,$u = 1.1$,${} d = \frac{1}{u} = \frac{1}{1.1}=0.90909 {}$,${} r = 5\%$.

[Stock Price](../../../Financial%20Engineering/Derivatives/Part%20IV%20-%20Options/Chapter%2016%20-%20Black–Scholes%20Model.md) can move to:

- Up:$S_u = S_0 \times u = 100 \times 1.1$,
- Down:$S_d = S_0 \times d = 100 \times \frac{1}{1.1}$

## STEP 2: CONSTRUCT THE BINOMIAL TREE

Over two periods,  the [stock price](../../../Financial%20Engineering/Derivatives/Part%20IV%20-%20Options/Chapter%2016%20-%20Black–Scholes%20Model.md) can have the following values:

- $S_{uu} = S_0 \cdot u^2$(up-up),
- $S_{ud} = S_0 \cdot u \cdot d = S_0$(up-down or down-up,  which is the same because it’s a [binomial](../../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%205%20Options%20on%20Prices%20and%20Hedge-Based%20Valuation/A%20Real-Life%20Option%20Pricing%20Exercise.md)),
- $S_{dd} = S_0 \cdot d^2$(down-down).

## STEP 3: CALCULATE OPTION PAYOFFS AT EXPIRY

For a European call option with [exercise price](../../../Financial%20Markets/Financial%20Asset%20Pricing%20Theory%20Overview/Chapter%2012%20-%20Derivatives/Options.md)$K = 100$,  the payoffs at$t=2$are:

- $C_{uu} = \max(S_{uu} - K,    0)$,
- $C_{ud} = \max(S_{ud} - K,    0)$,
- $C_{dd} = \max(S_{dd} - K,    0)$.

## STEP 4: DERIVE THE REPLICATING PORTFOLIO AT$T=1$

For each node at$t=1$(which are$u$and$d$),  we calculate$\Delta$and$B$to replicate the option’s payoff. The formulas for$\Delta$and$B$are derived from:
$$C_u = \Delta \cdot S_u + B \cdot (1+r)$$
$$C_d = \Delta \cdot S_d + B \cdot (1+r)$$

Where$C_u$and$C_d$are the option values at the up and down states at$t=1$.

## STEP 5: SOLVE FOR Δ AND$B$AT EACH NODE

We solve these equations to find$\Delta$and$B$that make the [portfolio](../../../Advanced%20Investments/An%20Asset%20Allocation%20Primer.md)'s value at each node at$t=1$match the option's payoff.

## STEP 6: CALCULATE THE OPTION PRICE AT$T=0$

We then use the values of$\Delta$and$B$found for the first node (at$t=0$) and the equation:
$$C_0 = \Delta \cdot S_0 + B \cdot (1+r)$$

To find the initial cost of replicating the option,  which gives us the price of the call option at$t=0$.

Let's now proceed with calculations for the specific values,  starting by calculating$C_{uu}$,  $C_{ud}$,  and$C_{dd}$.

code_interpreter(

 Given values S 0 = 100 # Initial [stock price](../../../Financial%20Engineering/Derivatives/Part%20IV%20-%20Options/Chapter%2016%20-%20Black–Scholes%20Model.md) u = 1.1 # Up factor d = 1/u # Down factor K = 100 # [Strike price](../../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%205%20Options%20on%20Prices%20and%20Hedge-Based%20Valuation/Call%20and%20Put%20Payoffs%20at%20Expiry.md) r = 0.05 # [Risk-free rate](../../Black%20Scholes%20Derivation.md)

# Calculate Stock Prices at Different Nodes

S_UU = S 0 * U**2 S_UD = S 0 #
S_U * D OR S_D * U S_DD = S_{0} * D**2

# CALCULATE OPTION PAYOFFS AT EXPIRY
$C_{UU} = MAX(S_{UU} - K,    0)$$C_{UD} = MAX(S_{UD} - K,    0)$$C_{DD} = MAX(S_{DD} - K,    0)$$(S_{UU},    S_{UD},    S_{DD},    C_{UU},    C_{UD},    C_{DD})$

(121.00000000000001,  100,  82.64462809917354,  21.000000000000014,  0,  0)

The stock prices and option payoffs at expiry are as follows:

- $S_{uu} = 121$,  $C_{uu} = 21$,
- $S_{ud} = 100$,  $C_{ud} = 0$,
- $S_{dd} = 82.64$,  $C_{dd} = 0$.

## STEP 7: CALCULATE Δ AND$B$FOR$T=1$

To find$\Delta$and$B$,  we start by solving the equations for the$u$and$d$nodes at$t=1$. Since the model is symmetric and the option's payoff is the same for the$ud$and$du$scenarios,  we only need to investigate the$uu$and$dd$scenarios for deriving the values at$t=0$.

We will calculate the values of$\Delta$and$B$using the payoffs:
$$C_{uu} - C_{dd} = \Delta \cdot (S_{uu} - S_{dd})$$

Solving this equation gives us$\Delta$. Subsequently,  we can calculate$B$from the given equation for one of the nodes (e.g.,  up or down node).

Let's perform these calculations for$\Delta$and$B$.

code_interpreter(

from sympy import symbols,  solve Delta,  B = symbols('Delta B') # Solve for Delta using the equation derived from C_uu - C_dd Delta_solution = solve(C_uu - Delta * (S_uu - S_dd),  Delta) # Use any of the equations from step 4 to solve for B (using C_uu for consistency) B_solution = solve(C_uu - Delta_solution[0] * S_uu - B * (1 + r),  B) Delta_solution[0],  B_solution[0]

)

(0.547511312217194,  -43.0941607412195)

The values of$\Delta$and$B$for replicating the option's payoff at$t=1$are as follows:

- $\Delta = 0.5475$,
- $B = -43.0942$.

Now,  we know how many shares the intermediary needs to hold and how much they need to borrow or lend to create a [replicating portfolio](Pricing%20Forwards,%20Futures,%20Bonds,%20Swaps,%20Swaptions,%20Caps%20and%20Floors%20under%20No-Arbitrage%20and%20Risk-Neutral%20Pricing.md) with the same payoff as the call option at$t=1$.

## STEP 8: CALCULATE THE OPTION PRICE AT$T=0$

To calculate the price of the option at$t=0$,  we now find the expected option value at each node discounted back at the [risk-free rate](../../Black%20Scholes%20Derivation.md),  since we've established the [replication](../../Financial%20Derivatives%20and%20Quantitative%20Methods/Forward%20and%20Futures%20Contracts.md) at$t=1$. However,  since we know the$\Delta$and$B$that replicates the option's payoff from the future back to$t=0$,  we can use these values directly to find the price of the option at$t=0$. We apply the equation:
$$C_0 = \Delta \cdot S_0 + B \cdot (1 + r)$$

Let's calculate$C_0$,  the price of the call option at$t=0$.

code_interpreter(

Calculate C0 using the values of Delta and B found and the initial [stock price](../../../Financial%20Engineering/Derivatives/Part%20IV%20-%20Options/Chapter%2016%20-%20Black–Scholes%20Model.md) S_{0}
C0 = Delta_solution[0] * S_{0} + B_solution[0] * (1 + r) C0)

9.50226244343888

[Quantitative Finance](../../../Course%20Notes/Quantitative%20Trading%20Strategies%20Lecture%20Notes.md) Savant

The price of the European call option at$t=0$in this [two-period binomial model](../../Financial%20Derivatives%20and%20Quantitative%20Methods/The%20T₁%20-period%20Binomial%20Model.md) is approximately$9.50$. This represents the initial cost of the call option,  determined by setting up a [replicating portfolio](Pricing%20Forwards,%20Futures,%20Bonds,%20Swaps,%20Swaptions,%20Caps%20and%20Floors%20under%20No-Arbitrage%20and%20Risk-Neutral%20Pricing.md) that matches the option's payoffs.

Here’s a summary of the [hedging strategy](../Teaching%20Note%203%20Swaps-%20Financial%20Instruments/The%20Value%20of%20the%20Swap%20Contract%20after%20Initiation.md):

1. **At time$t=0$**,  to hedge the risk from writing the call,  the financial intermediary should:
	 - Buy$\Delta = 0.5475$shares of the stock,  and
	 - Borrow$B = -43.0942$units of [currency](../Teaching%20Note%201-%20Forward%20Rates%20Agreement/Forwards%20and%20Futures%20Notes.md) (considering the negative sign as borrowing).
1. **At time$t=1$**,  depending on whether the [stock price](../../../Financial%20Engineering/Derivatives/Part%20IV%20-%20Options/Chapter%2016%20-%20Black–Scholes%20Model.md) moves up or down,  adjust the [portfolio](../../../Advanced%20Investments/An%20Asset%20Allocation%20Primer.md) according to the calculated values of$\Delta$and$B$specifically for that node (note that detailed adjustments for$t=1$nodes require further calculations like we did for$t=0$,  involving an expected payoff approach).

By following this [hedging strategy](../Teaching%20Note%203%20Swaps-%20Financial%20Instruments/The%20Value%20of%20the%20Swap%20Contract%20after%20Initiation.md),  the financial intermediary can create a [portfolio](../../../Advanced%20Investments/An%20Asset%20Allocation%20Primer.md) that replicates the payoff of the call option,  thus neutralizing the risk of having sold the option.
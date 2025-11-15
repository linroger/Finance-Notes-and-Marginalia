---
academic_level: graduate
aliases:
- Binomial Option Pricing
- Option Replication
- Stock Price Calculation
enhanced: true
enhancement_date: '2025-11-06'
enhancement_id: batch09-000165
key_concepts:
- Black-Scholes option pricing model and continuous-time finance
- Binomial option pricing model and lattice methods
- Options Greeks and sensitivity analysis for risk management
- Duration analysis and interest rate risk management
- Convexity adjustments and yield curve sensitivity
- Capital Asset Pricing Model (CAPM) and expected returns
- Credit default swaps (CDS) and credit risk modeling
- Value at Risk (VaR) and tail risk measurement
- Collateralized debt obligations (CDO) and tranche structure
- Arbitrage opportunities and no-arbitrage pricing
- Factor models and multi-factor pricing
- Risk preference theory and utility functions
- Sensitivity analysis and Greeks calculation
- Value at Risk and Expected Shortfall
- Vasicek Interest Rate Model and Mean Reversion
- Short Rate Models and Term Structure Dynamics
- Delta, Gamma, and Vega Hedging Techniques
- 'Greeks: Delta, Gamma, Theta, and Vega Hedging'
- Ornstein-Uhlenbeck Process in Finance
- Options Trading Strategies and Risk Management
- Stress Testing and Extreme Value Analysis
- Lattice Methods and Recombining Trees in Derivatives Pricing
- Fama-French Factors and Style Analysis
- Risk Measurement and VaR Backtesting
- Binomial Option Pricing Model for Discrete Time Valuation
- Dynamic vs Static Hedging in Practice
- American Option Pricing and Early Exercise Premium
- Private Equity Investment Returns and Value Creation
- Option Valuation and Exercise Strategies
- LBO Valuation and Debt Capacity Analysis
- Hedging Strategies and Risk Mitigation
- Factor Models and Asset Pricing
- Leveraged Buyouts and Private Equity Transactions
- Arbitrage Pricing Theory and Multi-Factor Models
linter-yaml-title-alias: CALCULATE STOCK PRICES AT DIFFERENT NODES
professional_application: theoreti
status: active
tags:
- arbitrage-opportunity
- arbitrage-pricing
- asset-allocation
- binomial-model
- black-scholes-model
- capital-asset-pricing
- capital-budgeting
- caplet
- cds
- collateralized-debt-obligation
- continuous-time-pricing
- convexity-adjustment
- counterparty-risk
- credit-default-swap
- credit-derivatives
- leveraged-buyout
- hull-white
- call-options
- cir-model
- butterfly-spreads
- expected-shortfall
- binomial-tree
- straddles
- extreme-value-theory
- american-options
- book-to-market
- volatility-analysis
- style-analysis
- leverage-ratio
- option-strategies
- arbitrage-pricing-theory
- private-equity
- market-price-of-risk
- value-factor
- vasicek-model
- dynamic-hedging
- monte-carlo-var
- options-trading
- fama-french
- parametric-var
- lognormal-models
- var-methodologies
- historical-var
- mean-reversion
- vega-hedging
- debt-capacity
- delta-hedging
- quantitative-finance
- investment-return
- crr-model
- protective-puts
- gamma-hedging
- hedge-effectiveness
- risk-premium
- put-options
- affine-term-structure
- equity-kickers
- multi-period-binomial
- lbo-valuation
- momentum
- basis-risk
- discrete-time-pricing
- hedge-strategies
- covered-calls
- stress-testing
- roll-over-risk
- mathematical-finance
- ornstein-uhlenbeck
- investment-analysis
- portfolio-optimization
- value-at-risk
- bootstrap-strategy
- management-buyout
- factor-models
- risk-management
- var-backtesting
- cross-hedging
- lattice-models
- strangles
- conditional-var
- cox-ross-rubinstein
- short-rate-models
- optional-exercise
- binomial-option-pricing
- multi-factor-models
- iron-condors
- financial-markets
- static-hedging
- size-effect
- ' recombining-trees'
- apt
title: Calculate Stock Prices at Different Nodes
type: course-note
---
--



# Calculate Stock Prices at Different Nodes

- **Binomial Trees]]**
	- Financial Instruments/Lecture Notes- Financial Instruments/Teaching Note 4-Multiperiod Binomial Trees/Binomial Option Pricing]]
	- Binomial Tree Steps]]
	- Calculate Stock Prices at Different Nodes
	- Options Strategies Construction
	- Binomial Trees]]
	- Financial Instruments/Lecture Notes/Teaching Note 4-Multiperiod Binomial Trees/The Pricing of Options and Corporate Liabilities]]

To hedge its risk from writing a European call option with an exercise price of$K = 100$in a two-period binomial model,  the financial intermediary needs to create a replicating portfolio that mirrors the option's payoffs in all states of the world by the end of the periods. We will set up this replicating portfolio and determine the initial cost (price of the call option),  the delta ($\Delta$,  the number of shares of the stock to hold),  and the amount of borrowing or lending required (denoted as$B$) at each node.

## STEP 1: CALCULATE THE STOCK PRICE MOVEMENT

Given:$S_0 = 100$,$u = 1.1$,${} d = \frac{1}{u} = \frac{1}{1.1}=0.90909 {}$,${} r = 5\%$.

Stock Price can move to:

- Up:$S_u = S_0 \times u = 100 \times 1.1$,
- Down:$S_d = S_0 \times d = 100 \times \frac{1}{1.1}$

## STEP 2: CONSTRUCT THE BINOMIAL TREE

Over two periods,  the stock price can have the following values:

- $S_{uu} = S_0 \cdot u[^2]$(up-up),
- $S_{ud} = S_0 \cdot u \cdot d = S_0$(up-down or down-up,  which is the same because it’s a binomial),
- $S_{dd} = S_0 \cdot d[^2]$(down-down).

## STEP 3: CALCULATE OPTION PAYOFFS AT EXPIRY

For a European call option with exercise price$K = 100$,  the payoffs at$t=2$are:

- $C_{uu} = \max(S_{uu} - K,    0)$,
- $C_{ud} = \max(S_{ud} - K,    0)$,
- $C_{dd} = \max(S_{dd} - K,    0)$.

## STEP 4: DERIVE THE REPLICATING PORTFOLIO AT$T=1$

For each node at$t=1$(which are$u$and$d$),  we calculate$\Delta$and$B$to replicate the option’s payoff. The formulas for$\Delta$and$B$are derived from:
$$C_u = \Delta \cdot S_u + B \cdot (1+r)$$
$$C_d = \Delta \cdot S_d + B \cdot (1+r)$$

Where$C_u$and$C_d$are the option values at the up and down states at$t=1$.

## STEP 5: SOLVE FOR Δ AND$B$AT EACH NODE

We solve these equations to find$\Delta$and$B$that make the portfolio's value at each node at$t=1$match the option's payoff.

## STEP 6: CALCULATE THE OPTION PRICE AT$T=0$

We then use the values of$\Delta$and$B$found for the first node (at$t=0$) and the equation:
$$C_0 = \Delta \cdot S_0 + B \cdot (1+r)$$

To find the initial cost of replicating the option,  which gives us the price of the call option at$t=0$.

Let's now proceed with calculations for the specific values,  starting by calculating$C_{uu}$,  $C_{ud}$,  and$C_{dd}$.

code_interpreter(

 Given values S 0 = 100 # Initial stock price u = 1.1 # Up factor d = 1/u # Down factor K = 100 # Strike price r = 0.05 # Risk-free rate

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

Now,  we know how many shares the intermediary needs to hold and how much they need to borrow or lend to create a replicating portfolio with the same payoff as the call option at$t=1$.

## STEP 8: CALCULATE THE OPTION PRICE AT$T=0$

To calculate the price of the option at$t=0$,  we now find the expected option value at each node discounted back at the risk-free rate,  since we've established the replication at$t=1$. However,  since we know the$\Delta$and$B$that replicates the option's payoff from the future back to$t=0$,  we can use these values directly to find the price of the option at$t=0$. We apply the equation:
$$C_0 = \Delta \cdot S_0 + B \cdot (1 + r)$$

Let's calculate$C_0$,  the price of the call option at$t=0$.

code_interpreter(

Calculate C0 using the values of Delta and B found and the initial stock price S_{0}
C0 = Delta_solution[0] * S_{0} + B_solution[0] * (1 + r) C0)

[^9]: 50226244343888

Quantitative Finance Savant

The price of the European call option at$t=0$in this two-period binomial model is approximately$9.50$. This represents the initial cost of the call option,  determined by setting up a replicating portfolio that matches the option's payoffs.

Here’s a summary of the hedging strategy:

[^1]: **At time$t=0$**,  to hedge the risk from writing the call,  the financial intermediary should:
	 - Buy$\Delta = 0.5475$shares of the stock,  and
	 - Borrow$B = -43.0942$units of currency (considering the negative sign as borrowing).
[^1]: **At time$t=1$**,  depending on whether the stock price moves up or down,  adjust the portfolio according to the calculated values of$\Delta$and$B$specifically for that node (note that detailed adjustments for$t=1$nodes require further calculations like we did for$t=0$,  involving an expected payoff approach).

By following this hedging strategy,  the financial intermediary can create a portfolio that replicates the payoff of the call option,  thus neutralizing the risk of having sold the option.

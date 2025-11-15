---
academic_level: graduate
aliases:
- CME
- Forwards
- Futures
- Hedging
enhanced: true
enhancement_date: '2025-11-06'
enhancement_id: batch09-000158
key_concepts:
- Options Greeks and sensitivity analysis for risk management
- Duration analysis and interest rate risk management
- Convexity adjustments and yield curve sensitivity
- Credit default swaps (CDS) and credit risk modeling
- Value at Risk (VaR) and tail risk measurement
- Expected shortfall and coherent risk measures
- Risk preference theory and utility functions
- Sensitivity analysis and Greeks calculation
- Yield Curve Analysis and Bond Valuation
- Value at Risk and Expected Shortfall
- Credit Risk Management and Default Probability
- Expected Loss and Loss Given Default Models
- Forward Rates and Curve Construction Methods
- Delta, Gamma, and Vega Hedging Techniques
- 'Greeks: Delta, Gamma, Theta, and Vega Hedging'
- Price Discovery and Market Efficiency
- Options Trading Strategies and Risk Management
- Stress Testing and Extreme Value Analysis
- Fama-French Factors and Style Analysis
- Risk Measurement and VaR Backtesting
- Bid-Ask Spreads and Market Impact
- Contango, Backwardation, and Roll Yield
- Futures and Forward Contracts in Financial Markets
- Hedge Strategies and Basis Risk Management
- Dynamic vs Static Hedging in Practice
- Term Structure of Interest Rates and Yield Curves
- Option Valuation and Exercise Strategies
- Market Microstructure and Liquidity Analysis
- Credit Spreads and Rating Migration Analysis
- Hedging Strategies and Risk Mitigation
- Factor Models and Asset Pricing
- Arbitrage Pricing Theory and Multi-Factor Models
linter-yaml-title-alias: 'EXAMPLE: HEDGING WITH FUTURES'
professional_application: theoreti
status: active
tags:
- arch
- asset-allocation
- bid-ask-spread
- caplet
- cds
- coherent-risk-measure
- conditional-var
- convexity-adjustment
- counterparty-risk
- credit-default-swap
- credit-derivatives
- credit-modeling
- currency-markets
- currency-strategy
- default-probability
- call-options
- butterfly-spreads
- expected-shortfall
- straddles
- extreme-value-theory
- book-to-market
- arbitrage
- backwardation
- volatility-analysis
- style-analysis
- option-strategies
- yield-curve
- unexpected-loss
- clearinghouse
- interpolation
- arbitrage-pricing-theory
- hedge-ratio
- price-discovery
- loss-given-default
- value-factor
- dynamic-hedging
- monte-carlo-var
- options-trading
- market-impact
- forward-contracts
- fama-french
- forward-rates
- recovery-rate
- parametric-var
- var-methodologies
- historical-var
- contango
- vega-hedging
- expected-loss
- market-efficiency
- delta-hedging
- forward-curve
- order-flow
- protective-puts
- probabilty-of-default
- liquidity
- curve-fitting
- gamma-hedging
- hedge-effectiveness
- roll-yield
- spot-rates
- put-options
- algorithmic-trading
- momentum
- basis-risk
- hedge-strategies
- term-structure
- covered-calls
- ' exposure-at-default'
- stress-testing
- roll-over-risk
- rating-migration
- par-yield
- investment-analysis
- value-at-risk
- factor-models
- risk-management
- convergence
- var-backtesting
- cross-hedging
- yield-curve-shocks
- high-frequency-trading
- strangles
- credit-migration
- marking-to-market
- credit-spreads
- multi-factor-models
- iron-condors
- financial-markets
- static-hedging
- size-effect
- futures-contracts
- apt
- bootstrap-method
title: Teaching Note 2-Futures Contracts
type: course-note
---
--



Carry Trade 1](Carry%20Trade%201.md)

Futures contracts are similar to forward contracts,  as they are agreements between two counterparties to exchange a pre-specified amount of good (e.g.,  corn,  or Euros) at a pre-specified time for a predetermined price.

- The three notable differences between forwards and futures:
  1. The contracts are traded on an exchange (e.g.,  CME);
  1. The contracts are standardized (size,  maturity);
  1. Profits and losses are mark to market.

Standardization is important to improve liquidity

- but it introduces basis risk: Mismatch between futures contract size and maturity versus actual corporate needs.

Mark to market is important: decreases probability of default

- At the end of each trading day,  profits and losses accrue to the account of the trader.
- If trading losses become too large,  exchange issues a margin call: the trader must post additional collateral or the position is immediately closed.

# Teaching Note 2-Futures Contracts

Consider earlier example: The US firm could hedge with futures contracts instead of forwards.

- CME Euro FX Futures have size of 125,  000 Euro and expire on Mar,  Jun,  Sep,  and Dec.
- Suppose that$T =$Mar 2007 and$F_{0,     T} = 1.28$.
- US firm can short 5 mil/125,  \d$\approx$40 futures contracts.
- Every day$t$,  $$P/L_t = k \times 125,     000 \times (F_{1,     T} - F_{t,     T}) =5,     000,     000\times (F_{1,     T} - F_{t,     T})$$
- At maturity$T$: Payoff at$T = (P/L)_t + (P/L)_2 + … + (P/L)_T$
  - $=5,     000,     000\times (F_{0,     T} - F_{T,     T})$
  - $=5,     000,     000\times (F_{0,     T} - M_T)$
  - $=$Payoff of Forward Contract at$T$if$F_{0,     T} = F_{T,     T}$

**Caveat**: The total payoff from using a constant number of contracts $k$ every period is actually not exactly equivalent to the one of a forward contract.

- Because of mark to market,  trading profits and losses accrue **over time** to the hedger.
- The correct statement of the payoff at$T$is in fact:
  - Payoff at$T$=$$(P/L)_1 \times e^{-r(T-t)} + (P/L)_2 \times e^{-r(T-t2)} + … + (P/L)_T \times e^{-r(T-T)}$$
  - where$dt = 1/365 = 1$day (in annual units)

To obtain the forward contract's payoff,  we must **tail the hedge** and choose the number of contracts $k$ per period as $$k = 40 \times e^{-r(T-t1)}$,      \newline
$k = 40 \times e^{-r(T-t2)}$,      …,     $k = 40 \times e^{-r(T-t_{T-1})}$,     $k_{T-1} = 40$$

- which yields the payoff sequence at$T =5,     000,     000\times (F_{0,     T} - F_{1,     T}) \times e^{r(T-t1)} + 5,     000,     000\times (F_{1,     T} - F_{2,     T}) \times e^{r(T-t2)} + … + 5,     000,     000\times (F_{T-1,     T} - F_{T,     T}) \times e^{r(T-T)}$
  - $=5,     000,     000\times (F_{0,     T} - M_T)$

# SPECULATING WITH FUTURES

Futures are also excellent vehicles to speculate on a view about the variation in the underlying.

- Example: Let today be Friday Jan 1,  2010. The Euro/Dollar exchange rate is$S_T = 1.4326$.
- A speculator believes that the Euro/Dollar rate will increase over the weekend.
- Consider two strategies:
  1. Funded Speculative Position:
	  - Buy 125,  000 Euros for$179,  075 = 125,  000 x 1.4326.
  1. Unfunded Speculative Position through Futures
	  - Go long 1 Futures contract at the CME. E.g.,  The March 10 Futures price on Jan 1,  2010 was$F_{T,     T} = 1.4334$
	  - First,  initial margin$2,  995.

On Monday,  Jan 4,  2010,  $ (t)$,  the exchange rate was ${} S_T = 1.4413$ and the Mar 10 Futures was $F_{T,     T} = 1.441$.

- Funded Speculative Position: The position is$180162.5 = 125,  000 x 1.441. Thus
  - Profit =$180162.5 -$179,  075 =$1087.5
  - Return on Investment${} \frac{1087.5}{179,     075} = 0.607\%$
- Unfunded Speculative Position through Futures:
  - Profit = 125,  000 x$(1.441 - 1.4334)$=$950
  - Return on Investment$\frac{950}{2,     995} = 31.72\%$

# THE FUTURES PRICE VS THE FORWARD PRICE

**Fact**: If interest rates are constant,  the futures price equals the forward price: $F_{T,     T} = F_{T}$
**Why?**

- Hedging with futures or with forwards costs nothing at inception$t$and provide the same payoff at$T$.
- The delivery price has to be the same using either contract.
**Why this condition only holds if interest rates are constant?**
  - Because the "tailing of the hedge" works exactly only when interest rates are constant.
  - If interest rates move over time,  the payoff at$T$of a Futures contract is only approximately$F_{0,     T} - M_T$,  as there is some cumulated interest rate determined by the sequence of$(P/L)_t$over time.
### HEDGING WITH FUTURES

Let:

- $N$= number of futures contracts
- $S$= size of one futures contract
- $F_{0,     T}$ = initial futures price for delivery at time $T$
- $F_{t,     T}$ = futures price at time $t$ for delivery at time $T$
- $M_T$ = spot price at maturity $T$
- $V$= total value hedged
- $r$= risk-free interest rate
- $t_i$ = specific point in time $i$ before maturity $T$
- $P/L_t$ = profit or loss at time $t$

[^1]: Number of futures contracts:$N = \frac{V}{S}$
[^1]: Daily profit/loss:$P/L_t = N \times S \times (F_{1,     T} - F_{t,     T})$
[^1]: Payoff at maturity$T$:
	- $\text{Payoff at } T = \sum_{t=1}^{T} P/L_t$$= V \times (F_{0,     T} - M_T)$

Caveat about the total payoff:
$$\text{Payoff at } T = \sum_{i=1}^{T} (P/L_{t_i}) \times e^{-r(T-t_i)}$$

To obtain the forward contract's payoff:$$k_{t_i} = N \times e^{-r(T-t_i)}$$$$\text{Payoff sequence at } T = V \times \sum_{i=1}^{T} (F_{0,     T} - F_{t_i,     T}) \times e^{r(T-t_i)}$$$$= V \times (F_{0,     T} - M_T)$$

### SPECULATING WITH FUTURES

Let:

- $S_T$= spot rate at time$T$
- $F_{T,     T}$= futures price for delivery at time$T$
- $I$= initial investment
- $R$= return on investment

General equations for speculative strategies:

[^1]: Funded Speculative Position:$$\text{Profit} = N \times S \times (S_{T+1} - S_T) - I$$$$R = \frac{\text{Profit}}{I}$$

[^1]: Unfunded Speculative Position through Futures:$$\text{Profit} = N \times S \times (F_{T+1,     T} - F_{T,     T})$$$$R = \frac{\text{Profit}}{\text{Initial Margin}}$$

## STOCK INDEX FUTURES

 | Specification | Details | 
 | --------------- | --------- | 
 | Underlying | S&P 500 index | 
 | Where traded | Chicago Mercantile Exchange | 
 | Size | $250 × S&P 500 index | 
 | Months | March,      June,      September,      December | 
 | Trading ends | Business day prior to determination of settlement price | 
 | Settlement | Cash-settled,      based upon opening price of S&P 500 on third Friday of expiration month | 

 | Specification | Details | 
 | ------------- | ----------------------------------------------------------------------------------------------------------------- | 
 | Underlying | Nikkei 225 Stock Index | 
 | Where traded | Chicago Mercantile Exchange | 
 | Size | $5 × Nikkei 225 Index | 
 | Months | March,      June,      September,      December | 
 | Trading ends | Business day prior to determination of settlement price | 
 | Settlement | Cash-settled,      based upon opening Osaka quotation of the Nikkei 225 index on the second Friday of expiration month |

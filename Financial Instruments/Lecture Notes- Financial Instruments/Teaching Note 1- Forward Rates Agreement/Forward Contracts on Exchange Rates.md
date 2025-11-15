---
academic_level: graduate
aliases:
- Currency Forwards
- FX Forwards
- Forward FX Contracts
enhanced: true
enhancement_date: '2025-11-06'
enhancement_id: batch09-000150
key_concepts:
- Black-Scholes option pricing model and continuous-time finance
- Options Greeks and sensitivity analysis for risk management
- Duration analysis and interest rate risk management
- Convexity adjustments and yield curve sensitivity
- LIBOR market model and multi-curve framework
- Basel accords and banking regulation framework
- Arbitrage opportunities and no-arbitrage pricing
- Risk preference theory and utility functions
- Duration and Convexity in Fixed Income Risk Management
- Yield Curve Analysis and Bond Valuation
- Value at Risk and Expected Shortfall
- Forward Rates and Curve Construction Methods
- Swap Market Mechanisms and Pricing
- Delta, Gamma, and Vega Hedging Techniques
- 'Greeks: Delta, Gamma, Theta, and Vega Hedging'
- Price Discovery and Market Efficiency
- Options Trading Strategies and Risk Management
- Stress Testing and Extreme Value Analysis
- Credit Default Swaps and Credit Risk Transfer
- Fama-French Factors and Style Analysis
- Risk Measurement and VaR Backtesting
- Bid-Ask Spreads and Market Impact
- Contango, Backwardation, and Roll Yield
- Futures and Forward Contracts in Financial Markets
- Hedge Strategies and Basis Risk Management
- Bond Portfolio Immunization Strategies
- Dynamic vs Static Hedging in Practice
- Interest Rate Swaps and Currency Swap Structures
- Term Structure of Interest Rates and Yield Curves
- Option Valuation and Exercise Strategies
- Market Microstructure and Liquidity Analysis
- Interest Rate Risk and DV01 Calculations
- Hedging Strategies and Risk Mitigation
- Factor Models and Asset Pricing
- Arbitrage Pricing Theory and Multi-Factor Models
professional_application: theoreti
status: active
tags:
- arbitrage-free-models
- arbitrage-opportunity
- banking-regulation
- basel-accord
- basis-risk
- basis-swap
- binomial-model
- black-scholes-model
- capital-adequacy
- caplet
- continuous-time-pricing
- convexity-adjustment
- credit-rating
- currency-markets
- currency-strategy
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
- clearinghouse
- interpolation
- overnight-indexed-swaps
- interest-rate-risk
- arbitrage-pricing-theory
- hedge-ratio
- price-discovery
- value-factor
- dynamic-hedging
- monte-carlo-var
- options-trading
- market-impact
- forward-contracts
- fama-french
- forward-rates
- parametric-var
- var-methodologies
- historical-var
- contango
- vega-hedging
- modified-duration
- market-efficiency
- delta-hedging
- forward-curve
- order-flow
- currency-swaps
- bid-ask-spread
- protective-puts
- liquidity
- curve-steepening
- curve-fitting
- gamma-hedging
- hedge-effectiveness
- roll-yield
- spot-rates
- put-options
- algorithmic-trading
- momentum
- curve-flattening
- convexity
- hedge-strategies
- term-structure
- covered-calls
- swap-rate
- sofr
- stress-testing
- roll-over-risk
- par-yield
- investment-analysis
- duration-analysis
- value-at-risk
- factor-models
- barbell-strategy
- risk-management
- convergence
- var-backtesting
- cross-hedging
- yield-curve-shocks
- high-frequency-trading
- strangles
- conditional-var
- dv01
- swap-spread
- price-yield-relationship
- marking-to-market
- total-return-swaps
- libor
- multi-factor-models
- iron-condors
- financial-markets
- macaulay-duration
- static-hedging
- size-effect
- basis-swaps
- interest-rate-swaps
- futures-contracts
- apt
- bootstrap-method
- credit-default-swaps
title: Forward Contracts on Exchange Rates
type: course-note
---
--



Foreign Exchange Quoting Conventions

- Introduction to Derivative Markets]]
- Hedging%20[Key%20Rates%20O1s%20Durations%20and%20Hedging) Strategies with [Forwards]]
- Forward Exchange Rate Numerical Example]]
- Secondary Commodities]]
- Foreign Exchange Quoting Conventions
- Forward Contracts on Exchange Rates
- Forwards and Futures Notes]]
- Hedging Strategies with Forwards]]
- Financial Instruments/Lecture Notes/Teaching Note 1- Forward Rates Agreement/Interest Rates,  Carry Trades,  and Exchange Rate Movements]]
- Teaching Note 1Forward Rates Agreement
# Forward Contracts on Exchange Rates

Currency Forward](Currency%20Forward.md)
The rate of exchange for any date other than spot is a function of spot and the relative interest rates in each currency,  because the assumption is that any funds you have will be invested in a time deposit of that currency. Theforward rate is the rate which neutralizes the effoct ofdiffirences in the Eurocurrenry interest rates. If this were not the case,  investors and speculators would always buy and invest in the high interest rate currency,  eliminating their exchange rate risk with the forward contract.

Long forward exchange rate: At maturity,  purchase foreign currency and pay with home currency
Short forward contract: At maturity,  purchase home currency and pay with foreign currency

In summary,  the forward rate of exchange is the vehicle for adjusting for the interest rate differential. If you theoretically earn more in one currency than the other due to the interest rate differential,  the forward exchange rate will exactly offset this gain. The interest rate differential,  adjusted for time,  determines the forward points. The forward points reflect only today's difference in interest rates; they are not an indication of what the future spot or interest rates will be.

Forward contract to exchange foreign currency for home currency

- Forward contract to exchange EUR for USD](Foreign%20Exchange%20Quoting%20Conventions.md)
- Spot Exchange Rate:$M_{0} \frac{USD}{EUR}$
- Forward Rate:$F_{0, T} \frac{USD}{EUR}$
- US Interest Rate:$r_{USD}$
- EUR Interest Rate:$r_{EUR}$

## PRICING OF FORWARD EXCHANGE RATE CONTRACTS
- Consider a US Investor with USD N to invest for 1 year. The Investor has 2 options to invest.
1. **Strategy A**
	1. Deposit N at at$r_{USD}$yielding at maturity T:$$\text{Payoff}_{A}=Ne^{(r_{USD})*T}$$
1. **Strategy B**
	1. Exchange USD N into EUR$\frac{N}{M_{0}}$
	1. Invest EUR$\frac{N}{M_{0}}$at$r_{EUR}$yielding at maturity T:$$\text{Payoff}_{B}= \left(\frac{N}{M_{0}}\right)e^{(r_{EUR})*T}$$
	1. Enter into a forward contract to buy dollars,  paying euros at forward rate$F_{0, T}$(Short forward).$$\text{Dollars recieved }= F_{0, T}* \left(\frac{N}{M_{0}}\right)e^{(r_{EUR})*T}$$
1. Under no arbitrage,  the payoffs to the two strategies must be equal.$$F_{0, T}* \left(\frac{N}{M_{0}}\right)e^{(r_{EUR})*T} = Ne^{(r_{USD})*T}$$
1. Solving for$F_{0, T}$, $$F_{0, T}=M_{0}e^{(r_{USD}-r_{EUR})*T}$$

---

#### ARBITRAGE STRATEGY WHEN $F_{0, T} > M_0 * E^{(R_S-R_E) T}$

ie. quoted forward contract is overvalued.
Short forwards contract by paying euros and accepting dollars

[^1]: **Enter a forward contract to sell$N$euros at the forward rate$F_{0, T}$:**
	   Commit to sell euros in the future at the currently quoted forward rate.
	   This is equivalent to shorting the forward.
[^1]: **Borrow$N \times e^{-r_e \times T} \times M_0$dollars and use it to buy$N \times e^{-r_e \times T}$euros:**
	   Take a loan in dollars now,  which will be repaid by the proceeds of selling euros at the forward rate.
	   Convert the borrowed dollars to euros at the current spot rate.
[^1]: **Invest$N \times e^{-r_e \times T}$euros at the euro interest rate$r_e$until$T$:**
Invest the euros at the Euro Basis Swap Markets#London Interbank Offered Rate (LIBOR) | LIBOR]] rate,  expecting them to grow back to$N$euros over time$T$.
### AT MATURITY $T$
- **Receive$\$F_{0, T} \times N$from the forward sale of euros:**
   - This is the dollar amount you get from selling$N$euros at the forward rate.
- **Pay back the dollar loan of$\$(N \times e^{-r_e \times T} \times M_0) \times e^{r_s \times T}$:**
   - Repay the dollar loan which has grown to this amount with the US interest rate over time$T$.

- **The dollar profit at$T$is:**$$N \times (F_{0, T} - M_0 \times e^{(r_s-r_e) \times T})$$

[^1]: Short forward contract (sell euros,  buy dollars)
[^1]: Borrow dollars
[^1]: Buy euro
[^1]: Invest in euro deposits
At maturity,
[^1]: Collect returns from euro deposits
[^1]: Deliver euros and receive dollars
[^1]: Pay back loan obligation

### ARBITRAGE STRATEGY WHEN ${} F_{0, T} < M_0 * E^{(R_S-R_E) * T} {}$
[^1]: **Enter into a forward contract to buy$N$euros at forward rate$F_{0, T}$:**
	- This step locks in the price at which you will buy euros in the future.

[^1]: **Borrow$N \times e^{-r_e \times T}$euros:**
- Borrow euros now at the current Euro Basis Swap Markets#London Interbank Offered Rate (LIBOR) | LIBOR]] rate,  and you will need to pay back the borrowed amount multiplied by the exponential of the negative Euro interest rate times the time to maturity$T$.

[^1]: **Exchange them to$N \times e^{-r_e \times T} \times M_0$dollars:**
	- Convert the borrowed euros to dollars at the current spot rate.

[^1]: **Invest$N \times e^{-r_e \times T} \times M_0$dollars at the dollar interest rate$r_s$:**
- Invest the dollar amount at the current US Basis Swap Markets#London Interbank Offered Rate (LIBOR) | LIBOR]] rate,  and the investment will grow according to the dollar interest rate over the time to maturity$T$.

[^1]: **At maturity$T$,  the arbitrageur:**
	- Receives$N$euros from the forward contract and pays$F_{0, T} \times N$dollars for them.
	- Pays back the euro loan of$N \times e^{-r_e \times T}$euros,  which has grown to$N$euros by$T$.
	- Receives proceeds from the dollar investment,  which is the invested amount multiplied by the exponential of the dollar interest rate times$T$.

[^1]: **Dollar Profit at$T$:**
	- The profit is calculated as the proceeds from the dollar investment minus the cost of buying euros in the forward contract.

[^1]: Long forward (buy euros,  pay dollars)
[^1]: Borrow euros
[^1]: Convert to dollars
[^1]: invest in dollars deposits
At maturity,
[^1]: Collect returns from dollar deposits
[^1]: Pay dollars to forward counterparty
[^1]: Collect euros
[^1]: Use euros to pay back euro loan

Hedging Strategies with Forwards](Hedging%20Strategies%20with%20Forwards.md)
Hedging with Forwards](Hedging%20with%20Forwards.md)
---

### TABLE 1: OVERVALUED FORWARD RATE
- In this scenario,  the arbitrageur believes that the forward rate for buying euros is overvalued,  meaning that the market's forward rate is higher than what it should be based on interest rate differentials.

 | Trade | Payoff | 
 | --- | --- | 
 | Enter a forward contract to sell euros at the overvalued forward rate $F_{0, T}$ | 0 | 
 | Borrow euros at the current spot rate $M_0$ | $-N \times e^{-r_e \times T}$ | 
 | Convert borrowed euros to dollars at spot rate $M_0$ | $N \times e^{-r_e \times T} \times M_0$ | 
 | Invest the dollar amount at the US interest rate $r_s$ | $N \times e^{-r_e \times T} \times M_0 \times e^{r_s \times T}$ | 
 | At maturity $T$,  fulfill the forward contract | $-N \times F_{0, T}$ | 
 | Pay back the euro loan | $N$ | 
 | **Net Profit/Loss at $T$** | $N \times (e^{-r_e \times T} \times M_0 \times e^{r_s \times T} - F_{0, T})$ | 

### TABLE 2: UNDERVALUED FORWARD RATE
- In this scenario,  the arbitrageur believes that the forward rate for buying euros is undervalued,  meaning that the market's forward rate is lower than what it should be based on interest rate differentials.

 | Trade | Payoff | 
 | --- | --- | 
 | Enter a forward contract to buy euros at the undervalued forward rate $F_{0, T}$ | 0 | 
 | Borrow dollars at the current spot rate$M_0$ | $-N \times e^{-r_s \times T} \times M_0$ | 
 | Convert borrowed dollars to euros at spot rate$M_0$ | $N \times e^{-r_s \times T}$ | 
 | Invest the euro amount at the Euro interest rate$r_e$ | $N \times e^{-r_s \times T} \times e^{r_e \times T}$ | 
 | At maturity$T$,  fulfill the forward contract | $N \times F_{0, T}$ | 
 | Pay back the dollar loan | $N \times e^{-r_s \times T} \times M_0 \times e^{r_s \times T}$ | 
 | **Net Profit/Loss at$T$** | $N \times (F_{0, T} - e^{-r_s \times T} \times M_0 \times e^{r_s \times T})$ |

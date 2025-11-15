---
academic_level: graduate
aliases:
- Cash-and-Carry
- Reverse Carry Trade
enhanced: true
enhancement_date: '2025-11-06'
enhancement_id: batch09-000153
key_concepts:
- Options Greeks and sensitivity analysis for risk management
- Duration analysis and interest rate risk management
- Convexity adjustments and yield curve sensitivity
- Heath-Jarrow-Morton (HJM) and forward rate dynamics
- Arbitrage opportunities and no-arbitrage pricing
- Risk preference theory and utility functions
- Sensitivity analysis and Greeks calculation
- Financial modeling and quantitative analysis
- Risk management and portfolio optimization
- Derivatives pricing and hedging strategies
- Market risk measurement and control
- Duration and Convexity in Fixed Income Risk Management
- Yield Curve Analysis and Bond Valuation
- Value at Risk and Expected Shortfall
- Vasicek Interest Rate Model and Mean Reversion
- Short Rate Models and Term Structure Dynamics
- Credit Risk Management and Default Probability
- Expected Loss and Loss Given Default Models
- Forward Rates and Curve Construction Methods
- Delta, Gamma, and Vega Hedging Techniques
- Ornstein-Uhlenbeck Process in Finance
- Price Discovery and Market Efficiency
- Stress Testing and Extreme Value Analysis
- Risk Measurement and VaR Backtesting
- Bid-Ask Spreads and Market Impact
- Contango, Backwardation, and Roll Yield
- Futures and Forward Contracts in Financial Markets
- Hedge Strategies and Basis Risk Management
- Bond Portfolio Immunization Strategies
- Dynamic vs Static Hedging in Practice
- Term Structure of Interest Rates and Yield Curves
- Market Microstructure and Liquidity Analysis
- Credit Spreads and Rating Migration Analysis
- Interest Rate Risk and DV01 Calculations
- Hedging Strategies and Risk Mitigation
linter-yaml-title-alias: GOVERNMENT OF CANADA BOND FUTURES
professional_application: theoreti
status: active
tags:
- arbitrage-opportunity
- asset-allocation
- caplet
- convexity-adjustment
- credit-rating
- currency-strategy
- debit-valuation-adjustment
- delta-hedging
- duration-analysis
- dynamic-hedging
- exchange-rates
- fixed-income-sensitivity
- forward-contracts
- forward-curve
- forward-pricing
- hull-white
- cir-model
- expected-shortfall
- extreme-value-theory
- arbitrage
- backwardation
- volatility-analysis
- yield-curve
- unexpected-loss
- clearinghouse
- interpolation
- interest-rate-risk
- hedge-ratio
- market-price-of-risk
- price-discovery
- loss-given-default
- vasicek-model
- monte-carlo-var
- market-impact
- forward-rates
- recovery-rate
- parametric-var
- lognormal-models
- var-methodologies
- historical-var
- mean-reversion
- contango
- vega-hedging
- modified-duration
- expected-loss
- market-efficiency
- order-flow
- bid-ask-spread
- probabilty-of-default
- liquidity
- curve-steepening
- curve-fitting
- gamma-hedging
- hedge-effectiveness
- roll-yield
- risk-premium
- spot-rates
- affine-term-structure
- algorithmic-trading
- curve-flattening
- basis-risk
- convexity
- hedge-strategies
- term-structure
- ' exposure-at-default'
- stress-testing
- roll-over-risk
- ornstein-uhlenbeck
- rating-migration
- par-yield
- investment-analysis
- value-at-risk
- barbell-strategy
- risk-management
- convergence
- var-backtesting
- cross-hedging
- yield-curve-shocks
- high-frequency-trading
- conditional-var
- dv01
- short-rate-models
- price-yield-relationship
- credit-migration
- default-probability
- marking-to-market
- credit-spreads
- financial-markets
- macaulay-duration
- static-hedging
- futures-contracts
- bootstrap-method
title: Carry Trade
type: course-note
---
--



Lecture Note 1- Forward Rates Agreement
Teaching Note 2-Futures Contracts
Currency Forward](Currency%20Forward.md)

Carry Trade]]
	- Introduction to Derivative Markets]]
	- Hedging%20[Key%20Rates%20O1s%20Durations%20and%20Hedging) Strategies with [Forwards]]
	- Forward Exchange Rate Numerical Example]]
	- Secondary Commodities]]
	- Foreign Exchange Quoting Conventions
	- Forward Contracts on Exchange Rates
	- Forwards and Futures Notes]]
	- Hedging Strategies with Forwards]]
	- Financial Instruments/Lecture Notes/Teaching Note 1- Forward Rates Agreement/Interest Rates,     Carry Trades,     and Exchange Rate Movements]]
	- Teaching Note 1 Forward Rates Agreement

## WHAT IS A CARRY TRADE?

A Interest Rates,  Carry Trades,  and Exchange Rate Movements](Asset%20Classes/Derivatives/Forward%20and%20Futures/Forward%20Exchange%20Rate%20Contracts/Foreign%20Exchange%20Notes/Interest%20Rates,  %20Carry%20Trades,  %20and%20Exchange%20Rate%20Movements.md) is a form of arbitrage that takes advantage of price discrepancies between futures and spot prices. When performing a Interest Rates,  Carry Trades,  and Exchange Rate Movements](Asset%20Classes/Derivatives/Forward%20and%20Futures/Forward%20Exchange%20Rate%20Contracts/Foreign%20Exchange%20Notes/Interest%20Rates,  %20Carry%20Trades,  %20and%20Exchange%20Rate%20Movements.md),  the trader will take a position in the spot market and simultaneously take the opposite position in the futures market. Since one leg makes money as the other loses money,  the strategy is referred to as “market neutral.” When trading a market-neutral strategy,  the trader doesn’t care which direction the underlying asset’s price moves. 

The strategy’s profitability relies on the fact that futures contracts are often priced above or below the spot price. A futures contract’s price represents a market’s perception of where its underlying asset is heading by its settlement date. Therefore,  futures prices often drift from the current spot price,  presenting an opportunity to profit with relatively little risk. 

When the spot price is below the futures price,  the market is said to be in _contango_,  and a Interest Rates,  Carry Trades,  and Exchange Rate Movements](Asset%20Classes/Derivatives/Forward%20and%20Futures/Forward%20Exchange%20Rate%20Contracts/Foreign%20Exchange%20Notes/Interest%20Rates,  %20Carry%20Trades,  %20and%20Exchange%20Rate%20Movements.md) will often result in profits. When the opposite is true,  the market is said to be in _backwardation_,  and a reverse Interest Rates,  Carry Trades,  and Exchange Rate Movements](Asset%20Classes/Derivatives/Forward%20and%20Futures/Forward%20Exchange%20Rate%20Contracts/Foreign%20Exchange%20Notes/Interest%20Rates,  %20Carry%20Trades,  %20and%20Exchange%20Rate%20Movements.md) (i.e.,  shorting in the spot market and longing the futures contract) will be a more favorable strategy. 

When performing a Interest Rates,  Carry Trades,  and Exchange Rate Movements](Asset%20Classes/Derivatives/Forward%20and%20Futures/Forward%20Exchange%20Rate%20Contracts/Foreign%20Exchange%20Notes/Interest%20Rates,  %20Carry%20Trades,  %20and%20Exchange%20Rate%20Movements.md),  a trader will look for as wide a spread as possible between the spot price and futures price. As settlement approaches,  this spread will naturally narrow because the time in which the spot price can increase or decrease reduces. By settlement,  the two prices will have converged. The trader can close both positions for a profit whenever the spread is narrower than it was at entry. 

Alternatively,  a trader who settles the futures leg of a Interest Rates,  Carry Trades,  and Exchange Rate Movements](Asset%20Classes/Derivatives/Forward%20and%20Futures/Forward%20Exchange%20Rate%20Contracts/Foreign%20Exchange%20Notes/Interest%20Rates,  %20Carry%20Trades,  %20and%20Exchange%20Rate%20Movements.md) can opt to “roll over” their trade to a later-dated futures contract. If there is a wide spread between the spot price and a longer-term contract when closing the first futures position,  simply shorting the further out contract and continuing to hold the spot position will create a new Interest Rates,  Carry Trades,  and Exchange Rate Movements](Asset%20Classes/Derivatives/Forward%20and%20Futures/Forward%20Exchange%20Rate%20Contracts/Foreign%20Exchange%20Notes/Interest%20Rates,  %20Carry%20Trades,  %20and%20Exchange%20Rate%20Movements.md) with a new settlement date.

---
#### REVERSE CASH-AND-CARRY ARBITRAGE

A reverse cash-and-carry arbitrage is the exact opposite to a cash-and –carry transaction. Instead of buying the underlying security because it is underpriced,  you sell it short (because it is overpriced),  take the proceeds and go long a futures position on the underlying security. Before the futures position expires you close out the position by taking delivery and returning the borrowed shares you were short.

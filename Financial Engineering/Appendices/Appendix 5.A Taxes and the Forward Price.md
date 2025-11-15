---
academic_level: graduate
aliases:
- Forward contract pricing
- Futures vs. Forwards
- Tax impact
cssclasses: academia
enhanced: true
enhancement_date: '2025-11-06'
enhancement_id: batch09-000423
key_concepts:
- Black-Scholes option pricing model and continuous-time finance
- Options Greeks and sensitivity analysis for risk management
- Duration analysis and interest rate risk management
- Convexity adjustments and yield curve sensitivity
- Basel accords and banking regulation framework
- Arbitrage opportunities and no-arbitrage pricing
- Risk preference theory and utility functions
- Sensitivity analysis and Greeks calculation
- Value at Risk and Expected Shortfall
- Vasicek Interest Rate Model and Mean Reversion
- Short Rate Models and Term Structure Dynamics
- Delta, Gamma, and Vega Hedging Techniques
- 'Greeks: Delta, Gamma, Theta, and Vega Hedging'
- Ornstein-Uhlenbeck Process in Finance
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
- Option Valuation and Exercise Strategies
- Market Microstructure and Liquidity Analysis
- Hedging Strategies and Risk Mitigation
- Factor Models and Asset Pricing
- Arbitrage Pricing Theory and Multi-Factor Models
professional_application: theoreti
status: active
tags:
- arbitrage-opportunity
- banking-regulation
- basel-accord
- binomial-model
- black-scholes-model
- capital-adequacy
- caplet
- continuous-time-pricing
- convexity-adjustment
- credit-rating
- delta-hedging
- derivatives
- discrete-time-pricing
- dividend-policy
- dividend-stability
- put-options
- affine-term-structure
- cross-hedging
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
- basis-risk
- parametric-var
- conditional-var
- extreme-value-theory
- var-methodologies
- historical-var
- hedge-strategies
- book-to-market
- mean-reversion
- contango
- backwardation
- vega-hedging
- lognormal-models
- covered-calls
- volatility-analysis
- style-analysis
- short-rate-models
- option-strategies
- stress-testing
- roll-over-risk
- arbitrage
- ornstein-uhlenbeck
- clearinghouse
- investment-analysis
- market-efficiency
- marking-to-market
- value-at-risk
- order-flow
- arbitrage-pricing-theory
- multi-factor-models
- hedge-ratio
- bid-ask-spread
- iron-condors
- protective-puts
- market-price-of-risk
- financial-markets
- static-hedging
- price-discovery
- size-effect
- factor-models
- liquidity
- value-factor
- vasicek-model
- gamma-hedging
- dynamic-hedging
- hedge-effectiveness
- monte-carlo-var
- risk-management
- convergence
- options-trading
- var-backtesting
- futures-contracts
- roll-yield
- market-impact
- apt
- risk-premium
- forward-contracts
- fama-french
title: Appendix 5.A Taxes and the Forward Price
type: note
---
--



# Appendix 5.A Taxes and the Forward Price

The formulas in this chapter—and in the book to this point—have ignored taxes. In this appendix we show how taxes enter into the theoretical formula for the forward price, and explain why in practice these tax adjustments are never used. The impact of taxes on derivative prices was studied by Scholes (1976) and Cornell and French (1983), who showed that prices depend upon taxes when capital gains, dividends and interest are taxed at different rates. However, a party such as a broker-dealer, who is taxed identically on all forms of income, will have a fair price that is independent of taxes.

Suppose that capital gains on a stock are taxed at the rate $\tau_g$, gains on the forward contract at $\tau_f$, dividends at the rate $\tau_d$, and interest at the rate $\tau_i$. Consider an investor who goes long $(1-\tau_g)/(1-\tau_f)$ forward contracts (we will see why in a moment) and hedges by selling one share today. The investor thus receives $S_0$, which can be invested to earn the risk-free rate.

In 1 year, the investor closes the transaction by buying a share and paying the forward price. After-tax income is:

$$S_0[1+r(1-\tau_i)]-[S_1-\tau_g(S_1-S_0)]-\text{Div}(1-\tau_d)+[S_1-F_{0,1}]\frac{1-\tau_g}{1-\tau_f}(1-\tau_f)$$

The first bracketed term is the after-tax value of invested short-sale proceeds, the second is the after-tax cost of buying the share to close the short sale, the third is the after-tax dividend that must be paid to the share-lender, and the fourth is the after-tax gain on $(1-\tau_g)/(1-\tau_f)$ futures contracts. If the transaction is to generate no-arbitrage profits, the forward price must be set so that equation (5.20) equals zero. Thus, the after-tax zero-profit forward price is:

$$F_{0,1}=S_0\left(1+r\frac{1-\tau_i}{1-\tau_g}\right)-\text{Div}\frac{1-\tau_d}{1-\tau_g}$$

Note that the tax on the forward contract does not enter the expression at all! The reason is that since the forward contract has a zero value, it is possible to offset the tax by entering into additional forward contracts—this is the reason for going long $(1-\tau_g)/(1-\tau_f)$ contracts against one short share. We in effect make the forward contract be taxed at the same rate as the stock.

$$F_{0,T}=S_0e^{[r(1-\tau_i)/(1-\tau_g)-\delta(1-\tau_d)/(1-\tau_g)]T}$$

The important insight is that broker-dealers are marked-to-market for tax purposes and face the same tax rate on all forms of income—i.e., $\tau_i=\tau_g=\tau_d$. Thus, equation (5.21) becomes:

$$F_{0,1}=S_0(1+r)-\text{Div}$$

The same as equation (5.5).

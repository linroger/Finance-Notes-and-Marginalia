---
aliases:
- Forward contract pricing
- Futures vs. Forwards
- Tax impact
cssclasses: academia
enhanced: true
enhancement_date: '2025-11-06'
enhancement_id: batch03-b00db3
key_concepts:
- Apt
- Treasury Futures
- Interest rate swap valuation and fixed-floating spreads
- Monte Carlo simulation techniques for path-dependent options
- Treasury Bonds
- Real options valuation in corporate investment decisions
- Binomial option pricing model for American-style options
- Stochastic interest rates
- Forward vs. futures prices
- Greeks calculation and their interpretation in options trading
- Single-name vs. index CDS trading
- Commodity markets and pricing dynamics
- Option Greeks and portfolio risk management
- Collateralized Debt Obligations
- Solution
- Credit spread decomposition and hazard rates
- Vega and volatility risk management
- CDS clearing and central counterparties
- Commodity futures pricing and storage costs
- forward commitments and hedging
- CDS-Bond basis and arbitrrage opportunities
- Swap spread and credit risk considerations
- Mathematical Finance
- Credit default swap pricing and recovery assumptions
- Broker-dealer tax treatment
- 'Structured products: CDOs, CLOs, and credit derivatives'
- No-arbitrage forward price
- Implied Volatility
- Fixed-for-floating swap cash flows and valuation
- Arbitrage Pricing Theory and multifactor models
- Course Material
- Currency risk management and hedging
- Forward rates and interest rate parity
- Theta and time decay modeling
- Risk-neutral pricing methodology for derivative securities
- International arbitrage and covered interest rate parity
- Synthetic credit derivatives and index trades
- Exchange rate determination and PPP theory
- Treasury futures trading and basis point value calculations
- CVA and DVA adjustments in derivative pricing
- Arbitrage opportunities and risk-free profit extraction
- Interest rate swap pricing and valuation
- Credit default swap pricing and risk-neutral probabilities
- Factor Models
- Variance swaps and volatility trading strategies
- Delta hedging strategies in options portfolio management
- Theta decay modeling for time-sensitive options strategies
- Implied volatility extraction from market option prices
- Shadow banking system and regulatory arbitrage
- Quantitative Implementation
- Volatility smile and skew modeling in options markets
- Gamma and convexity adjustments
- Delta hedging and the replication argument
- Cross-currency basis swaps and funding
- Taxes on forward prices
- Currency markets and foreign exchange trading
tags:
- financial-analysis
- treasury-futures
- commodities
- credit-default-swaps
- collateralized-debt-obligations
- interest-rate-swaps
- mathematical-finance
- course-material
- forward-price
- shadow-banking
- futures-price
- financial-modeling
- apt
- greeks
- factor-models
- exchange-rates
- quantitative-implementation
- solution
- treasury-bonds
- derivative-pricing
- arbitrage
- taxes
- implied-volatility
- quantitative-finance
- monte-carlo
title: Appendix 5.A Taxes and the Forward Price
---

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

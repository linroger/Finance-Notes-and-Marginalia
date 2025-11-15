---
tags:
- apt
- arbitrage
- artificial-intelligence
- banking
- black-scholes-model
- bond-pricing
- chapter_12
- chapter_introduction
- corporate-bonds
- coupon-bonds
- currency-swap
- defi
- derivative_markets
- derivatives
- equity-derivatives
- european-options
- financial_derivatives
- fixed-income
- fixed-income-derivatives
- forward-contracts
- futures-contracts
- fx-derivatives
- interest-rate-derivatives
- interest-rate-swap
- ma
- markets
- option-greeks
- options
- options-on-futures
- options-pricing
- quantitative-pricing
- risk-management
- rwa
- settlement
- swaption
- value-at-risk
- var
aliases:
- Chapter 12
- Derivatives
key_concepts:
- Agricultural futures and seasonality
- Alternative investments and hedge fund strategies
- American vs European options and early exercise features
- Arbitrage Pricing Theory (APT) and factor models
- Arbitrage pricing theory (APT)
- Asset swaps and spread-lock strategies
- Bank asset-liability management (ALM) strategies
- Bank capital adequacy and Basel III compliance
- Bank stress testing and CCAR requirements
- Barrier options and knock-in/knock-out structures
- Basis swaps and cross-currency basis adjustments
- Basis swaps and floating rate correlations
- Behavioral finance and market anomalies
- Best execution and regulatory requirements
- Bid-ask spreads and market making profitability
- Binomial option pricing model with multi-period trees
- Black-Litterman model and portfolio optimization
- Black-Scholes option pricing model
- Black-Scholes option pricing model and its applications
- Bond portfolio immunization strategies
- CDO structuring and tranche allocation methodologies
- CDO-squared structures and correlation trading
- Calendar spreads and roll strategies
- Capital Asset Pricing Model (CAPM) and beta estimation
- Central bank digital currencies (CBDCs)
- Central clearing and CCP risk management
- Commodity futures and convenience yields
- Commodity swaps and energy derivatives
- Constant maturity swaps and roll-over features
- Corporate bond pricing and credit spread decomposition
- Crack spreads in energy markets
- Credit default swaps and credit protection mechanisms
- Credit risk assessment and loan pricing
- Credit valuation adjustment (CVA) and counterparty risk
- Cryptocurrency valuation and blockchain technology
- Currency swaps and cross-currency basis
- Dark pools and alternative trading venues
- DeFi protocols and decentralized finance
- Delta hedging and Greeks calculation
- Deposit insurance and systemic risk
- Derivatives
- Dividend discount model (DDM) applications
- Duration and convexity for bond price sensitivity
- ESG investing and sustainability metrics
- Enterprise value and equity value relationships
- Equity swaps and total return swaps
- Exotic derivatives and path-dependent options
- Exotic options and path-dependent derivatives
- Expected Shortfall (ES) and coherent risk measures
- Extreme value theory and tail risk modeling
- FX futures and currency hedging
- Fama-French three-factor and five-factor models
- Fintech disruption and digital banking
- Forward contract pricing and cost of carry
- Futures vs forwards and delivery options
- GARCH models for volatility forecasting
- Gamma trading and convexity adjustments
- Green bonds and climate risk assessment
- HJM and forward rate model frameworks
- Heath-Jarrow-Morton (HJM) framework
- High frequency trading and algorithmic strategies
- Historical simulation and parametric VaR approaches
- Hull-White and Black-Karasinski short rate models
- IPO pricing and underpricing analysis
- Implied volatility and volatility surface modeling
- Inflation-linked swaps and CPI adjustments
- Interest rate derivatives and forward rate agreements
- Interest rate models and term structure
- Interest rate swaps and swap pricing
- Interest rate swaps and swap spread decomposition
- Key rate duration and curve risk decomposition
- Liquidity-adjusted VaR and liquidity horizons
- Margin requirements and collateral optimization
- Market impact and transaction cost analysis
- Mean reversion in interest rate processes
- Mergers and acquisitions due diligence
- Metal futures and industrial commodities
- Model backtesting and validation procedures
- Modern portfolio theory and efficient frontier
- Momentum and reversal investment strategies
- Mortgage-backed securities and prepayment modeling
- Multi-factor interest rate models
- Negative interest rates and floor/cap structures
- Net interest margin and banking profitability
- Netting agreements and close-out procedures
- Non-deliverable forwards and emerging market instruments
- OIS discounting and collateralized interest rate derivatives
- Options on futures and forward-starting options
- Payment systems and settlement risk
- Prime brokerage and securities lending
- Private credit and direct lending
- Project finance and syndicated lending
- Recovery rate modeling and loss given default
- Repo markets and securities lending
- Risk factor decomposition and sensitivity analysis
- Risk parity and risk budgeting strategies
- Shadow banking and non-bank intermediation
- Smart beta and alternative indexing approaches
- Spot rates, forward rates, and discount factor curves
- Stochastic volatility in interest rate markets
- Stress testing and scenario analysis frameworks
- Subprime mortgage crisis and structured finance risks
- Swaptions and interest rate option pricing
- Swaptions and option volatility surfaces
- Synthetic CDOs and credit-linked note structures
- Terminal value modeling and exit multiples
- 'The Greeks: Delta, Gamma, Vega, Theta, and Rho sensitivity analysis'
- Too-big-to-fail policies and resolution regimes
- Treasury futures and bond basis
- Treasury securities and government bond markets
- VIX futures and volatility trading
- Value at Risk (VaR) and expected shortfall methodologies
- Value at Risk (VaR) and risk metrics
- Value vs growth investing frameworks
- Vasicek and CIR interest rate models
- Volatility smile and skew patterns in option markets
- Working capital and cash conversion cycle
- Wrong-way risk and correlation adjustments
- Zero-coupon bond pricing and bootstrapping
- financial instruments
- market participants
- pricing models
- risk management
enhanced: true
enhancement_date: '2025-11-06'
enhancement_id: batch04-358489
---



%% Begin Waypoint %%
- **Chapter 12 - Derivatives**
	- American-Style Derivatives
	- Chapter 12 - Derivatives
	- Concluding Remarks
	- Exercises
	- Forwards and Futures
	- Interest Rate Swaps and Swaptions
	- Options

%% End Waypoint %%
# Chapter 12 - Derivatives

# Derivatives  
12.1 Introduction . 299  
12.2 Forwards and futures. 301   
12.2.1 General results on forward prices and futures prices 301   
12.2.2 Interest rates forwards and futures . 304   
12.3 Options 307   
12.3.1 General pricing results for European options. 307   
12.3.2 European option prices when the underlying is lognormal 309   
12.3.3 The Black-Scholes-Merton model for stock option pricing 310   
12.3.4 Options on bonds .. 314   
12.3.5 Interest rate options: caps and floors .. 318   
12.4 Interest rate swaps and swaptions . 320   
12.4.1 Interest rate swaps. 320   
12.4.2 Swaptions 325   
12.5 American-style derivatives. 326   
12.6 Concluding remarks 327   
12.7 Exercises 328   
 A review of basic probability concepts 331   
Results on the lognormal distribution 339   
Bibliography 343  


# 12.1 Introduction  

A derivative is an asset whose dividend (s) and price are derived from the price of another asset, the. Underlying asset, or the value of some other variable. The main types of derivatives are forwards, futures, options, and swaps. While a large number of different derivatives are traded in today's financial markets, most of them are variations of these four main types..  

A forward is the simplest derivative. A forward contract is an agreement between two parties. On a given transaction at a given future point in time and at a price that is already fixed when the agreement is made. For example, a forward on a bond is a contract where the parties agree to. Trade a given bond at a future point in time for a price which is already fixed today. This fixed price is usually set so that the value of the contract at the time of inception is equal to zero so. That no money changes hand before the delivery date. Forward contracts are not traded or listed at financial exchanges but traded in quite organized over-the-counter (OTC) markets dominated. By large financial institutions. For example, forwards on foreign exchange are quite common..  

As a forward contract, a futures contract is an agreement upon a specified future transaction,. e.g. a trade of a given security. The special feature of a future is that changes in its value are settled continuously throughout the life of the contract (usually once every trading day). This so-called marking-to-market ensures that the value of the contract (i.e. the value of the payments still to come) is zero immediately following a settlement. This procedure makes it practically possible to trade futures at organized exchanges, since there is no need to keep track of when the futures position was originally taken. Futures on many different assets or variables are traded at different exchanges around the world, including futures on stocks, bonds, interest rates, foreign exchange,. Oil, metals, frozen concentrate orange juice, live cattle, and the temperature in Las Vegas!.  

An option gives the holder the right to make some specified future transaction at terms that are already fixed. A call option gives the holder the right to buy a given security at a given price at or before a given date. Conversely, a put option gives the holder the right to sell a given security. If the option gives the right to make the transaction at only one given date, the option is said to be European-style. If the right can be exercised at any point in time up to some given date, the option is said to be American-style. Both European- and American-style options are traded. Options on stocks, bonds, foreign exchange, and many other assets, commodities, and variables are traded at many exchanges around the world and also on the OTC-markets. Also options on futures on some asset or variable are traded, i.e. a derivative on a derivative! In addition, many financial assets or contracts have "embedded' options. For example, many mortgage-backed bonds and corporate bonds are callable, in the sense that the issuer has the right to buy back the bond at a pre-specified price.  

Table 12.1: Derivatives traded on organized exchanges. All amounts are in billions of US dollars. The amount outstanding is of September 2004, while the turnover figures are for the third quarter of 2004. Source: Table 23 A in BIS (2004).   


<html><body><table><tr><td rowspan="2">Instruments/ Location</td><td colspan="2">Futures</td><td colspan="2">Options</td></tr><tr><td>Amount outstanding</td><td>Turnover</td><td>Amount outstanding</td><td>Turnover</td></tr><tr><td>All markets</td><td>17,662</td><td>213,455</td><td>31,330</td><td>75,023</td></tr><tr><td>Interest rate</td><td>17,024</td><td>202,064</td><td>28,335</td><td>63,548</td></tr><tr><td>Currency</td><td>84</td><td>1,565</td><td>37</td><td>120</td></tr><tr><td>Equity index</td><td>553</td><td>9,827</td><td>2,958</td><td>11,355</td></tr><tr><td>North America</td><td>9,778</td><td>122,516</td><td>18,120</td><td>49,278</td></tr><tr><td>Europe</td><td>5,534</td><td>77,737</td><td>12,975</td><td>19,693</td></tr><tr><td>Asia-Pacific</td><td>2,201</td><td>11,781</td><td>170</td><td>5,786</td></tr><tr><td>Other markets</td><td>149</td><td>1,421</td><td>66</td><td>266</td></tr></table></body></html>  

A swap is an exchange of two dividend streams between two parties. In a "plain vanilla" interest rate swap, two parties exchange a stream of fixed interest rate payments and a stream of Hoating interest rate payments. In a currency swap, streams of payments in different currencies are exchanged. Many exotic swaps with special features are widely used.  

The markets for derivatives are of an enormous size. Table 12.1 provides some interesting. Statistics published by the Bank for International Settlements (BIS) on the size of derivatives. Markets at organized exchanges. The markets for interest rate derivatives are much larger than. The markets for currency- or equity-linked derivatives. The option markets generally dominate. Futures markets measured by the amounts outstanding but ranked according to turnover futures markets are larger than options markets..  

The BIS statistics also contain information about the size of OTC markets for derivatives. BIS estimates that in June 2004 the total amount outstanding on OTC derivative markets was 220,058 billions of US dollars, of which single-currency interest rate derivatives account for 164,626 billions, currency derivatives account for 26,997 billions, equity-linked derivatives for 4,521 billions, commodity contracts for 1,270 billions, while the remaining 22,644 billions cannot be split into any. Of these categories, cf. Table 19 in BIS (2004). Table 12.2 shows how the interest rate derivatives. Market can be disaggregated according to instrument and maturity. Approximately 38% of these. OTC-traded interest rate derivatives are denominated in Euro, 35% in US dollars, 13% in yen, and. 7% in pound sterling, cf. Table 21 B in BIS (2004)..  

This chapter gives an introduction to frequently traded derivatives and their valuation. We will specify the payments of these derivatives, discuss the links between different derivatives, and we will also indicate what we can conclude about their prices from general asset pricing theory.  

Table 12.2: Amounts outstanding (billions of US dollars) on OTC single-currency interest rate derivatives as of June 2004. Source: Tables 21 A and 21 C in BIS (2004).   


<html><body><table><tr><td rowspan="2">Contracts</td><td rowspan="2">total</td><td colspan="3">Maturityinyears</td></tr><tr><td>≤1</td><td>1-5</td><td>≥5</td></tr><tr><td>All interest rate</td><td>164,626</td><td>57,157</td><td>66,093</td><td>41,376</td></tr><tr><td>Forward rate agreements</td><td>13,144</td><td rowspan="2">49,397</td><td rowspan="2">56,042</td><td rowspan="2">35,275</td></tr><tr><td>Swaps</td><td>127,570</td></tr><tr><td>Options</td><td>23,912</td><td>7,760</td><td>10,052</td><td>6,101</td></tr></table></body></html>  

Throughout the chapter we assume that prices are arbitrage-free and that a bank account and zero-coupon bonds of relevant maturities are traded so that we can define and work with the riskneutral probability measures and forward measures introduced in Chapter 11. We will denote the continuously compounded risk-free short-term interest rate by. $r_{t}$ instead of $\boldsymbol{r}_{t}^{f}$  

Section 12.2 deals with forwards and futures, Section 12.3 with options, and Section 12.4 with. Swaps and swaptions. Some features of American-style derivatives are discussed in Section 12.5.

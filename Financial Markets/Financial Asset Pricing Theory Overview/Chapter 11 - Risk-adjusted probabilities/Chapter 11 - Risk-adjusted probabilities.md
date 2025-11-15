---
tags:
- apt
- artificial-intelligence
- chapter_11
- defi
- derivatives
- financial-markets
- financial-modeling
- fixed-income
- ma
- options
- options-pricing
- quantitative-finance
- risk-management
- risk_adjusted_probabilities
- rwa
aliases:
- Chapter 11
key_concepts:
- Agricultural futures and seasonality
- Alternative investments and hedge fund strategies
- Arbitrage Pricing Theory (APT) and factor models
- Arbitrage pricing theory (APT)
- Asset swaps and spread-lock strategies
- Barrier options and knock-in/knock-out structures
- Basis swaps and cross-currency basis adjustments
- Basis swaps and floating rate correlations
- Behavioral finance and market anomalies
- Best execution and regulatory requirements
- Bid-ask spreads and market making profitability
- Binomial option pricing model with multi-period trees
- Black-Litterman model and portfolio optimization
- Black-Scholes option pricing model and its applications
- CDO structuring and tranche allocation methodologies
- CDO-squared structures and correlation trading
- Calendar spreads and roll strategies
- Capital Asset Pricing Model (CAPM) and beta estimation
- Central clearing and CCP risk management
- Commodity futures and convenience yields
- Commodity swaps and energy derivatives
- Corporate bond pricing and credit spread decomposition
- Crack spreads in energy markets
- Credit risk assessment and loan pricing
- Credit valuation adjustment (CVA) and counterparty risk
- Cryptocurrency valuation and blockchain technology
- Currency swaps and cross-currency basis
- Dark pools and alternative trading venues
- DeFi protocols and decentralized finance
- Deposit insurance and systemic risk
- Duration and convexity for bond price sensitivity
- ESG investing and sustainability metrics
- Enterprise value and equity value relationships
- Equity swaps and total return swaps
- Exotic derivatives and path-dependent options
- Expected Shortfall (ES) and coherent risk measures
- Extreme value theory and tail risk modeling
- FX futures and currency hedging
- Fama-French three-factor and five-factor models
- Fintech disruption and digital banking
- Forward contract pricing and cost of carry
- GARCH models for volatility forecasting
- Gamma trading and convexity adjustments
- Green bonds and climate risk assessment
- HJM and forward rate model frameworks
- High frequency trading and algorithmic strategies
- Historical simulation and parametric VaR approaches
- Hull-White and Black-Karasinski short rate models
- IPO pricing and underpricing analysis
- Implied volatility and volatility surface modeling
- Inflation-linked swaps and CPI adjustments
- Interest rate derivatives and forward rate agreements
- Interest rate swaps and swap spread decomposition
- Key rate duration and curve risk decomposition
- Liquidity-adjusted VaR and liquidity horizons
- Margin requirements and collateral optimization
- Market impact and transaction cost analysis
- Mean reversion in interest rate processes
- Mergers and acquisitions due diligence
- Metal futures and industrial commodities
- Model backtesting and validation procedures
- Momentum and reversal investment strategies
- Mortgage-backed securities and prepayment modeling
- Multi-factor interest rate models
- Negative interest rates and floor/cap structures
- Netting agreements and close-out procedures
- Non-deliverable forwards and emerging market instruments
- OIS discounting and collateralized interest rate derivatives
- Options on futures and forward-starting options
- Payment systems and settlement risk
- Prime brokerage and securities lending
- Private credit and direct lending
- Project finance and syndicated lending
- Real estate investment trusts (REITs)
- Recovery rate modeling and loss given default
- Repo markets and securities lending
- Risk factor decomposition and sensitivity analysis
- Risk parity and risk budgeting strategies
- Risk-adjusted probabilities
- Risk-neutral valuation and martingale measures
- Shadow banking and non-bank intermediation
- Smart beta and alternative indexing approaches
- Spot rates, forward rates, and discount factor curves
- Stochastic volatility in interest rate markets
- Stress testing and scenario analysis frameworks
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
- Value vs growth investing frameworks
- Vasicek and CIR interest rate models
- Volatility smile and skew patterns in option markets
- Working capital and cash conversion cycle
- Wrong-way risk and correlation adjustments
- Zero-coupon bond pricing and bootstrapping
enhanced: true
enhancement_date: '2025-11-06'
enhancement_id: batch04-523111
---



%% Begin Waypoint %%
- **Chapter 11 - Risk-adjusted probabilities**
	- Change of Probability Measure
	- Changing the Numeraire Without Changing the Me
	- Chapter 11 - Risk-adjusted probabilities
	- Concluding Remarks
	- Exercises
	- Forward Risk-Adjusted Probability Measures
	- General Risk-Adjusted Probability Measures
	- Risk-Neutral Probabilities

%% End Waypoint %%

[^11]: 1 Introduction . 279
[^11]: 2 Change of probability measure 279
[^11]: 3 Risk-neutral probabilities 282
[^11]: 3.1 Definition 282
[^11]: 3.2 Relation to state-price deflators 284
[^11]: 3.3 Valuation with risk-neutral probabilities 287
[^11]: 4 Forward risk-adjusted probability measures 290
[^11]: 4.1 Definition . 290
[^11]: 4.2 Relation to state-price deflators and risk-neutral measures 291
[^11]: 4.3 Valuation with forward measures 292
[^11]: 5 General risk-adjusted probability measures 293
[^11]: 6 Changing the numeraire without changing the measure 295
[^11]: 7 Concluding remarks 297
[^11]: 8 Exercises 298
# Chapter 11 - Risk-adjusted probabilities

# Risk-adjusted probabilities  
# 11.1 Introduction  

Chapter 4 illustrated how the general pricing mechanism in a financial market can be represented by a state-price deflator. However, the state-price deflator is not the only way to represent the pricing mechanism of a financial market. As indicated in a one-period framework in Section 4.6.1,. One can equivalently represent the pricing mechanism by a risk-neutral probability measure and the risk-free return. This chapter explores and generalizes this idea and also outlines some applications. Of this alternative representation. The risk-neutral pricing technique is the standard approach in. The valuation of derivative securities. The next chapter focuses on derivatives and will illustrate the use of risk-neutral valuation for derivative pricing..  

Apparently, the idea of risk-neutral valuation stems from Arrow (1971) and Dreze (1971) and was further explored by Harrison and Kreps (1979)..  

The rest of this chapter is organized in the following way. Section 11.2 outlines how a general. Change of the probability measure is formalized. The risk-neutral probability measure is defined and studied in Section 11.3, while the so-called forward risk-adjusted probability measures are in-. Troduced in Section 11.4. Section 11.5 shows that an appropriate risk-adjusted probability measure. Can be defined for any given asset or trading strategy with a positive value. Section 11.6 demon-. Strates that the risk-adjusted probability measure associated with the so-called growth-optimal trading strategy is identical to the real-world probability measure..

---
tags:
- '#asset_pricing'
- '#chapter_8'
- '#consumption'
- '#consumption_based_asset_pricing'
- apt
- capm
- interest-rate-derivatives
- ma
- mpt
- options
- options-pricing
- risk-management
- value-at-risk
- var
key_concepts:
- Agricultural futures and seasonality
- Alternative investments and hedge fund strategies
- Arbitrage Pricing Theory (APT) and factor models
- Arbitrage pricing theory (APT)
- Asset swaps and spread-lock strategies
- Bank capital adequacy and Basel III compliance
- Barrier options and knock-in/knock-out structures
- Basel III capital requirements and risk metrics
- Basis swaps and cross-currency basis adjustments
- Basis swaps and floating rate correlations
- Behavioral finance and market anomalies
- Best execution and regulatory requirements
- Bid-ask spreads and market making profitability
- Binomial option pricing model with multi-period trees
- Black-Litterman model and portfolio optimization
- Black-Scholes option pricing model and its applications
- Bond portfolio immunization strategies
- CDO structuring and tranche allocation methodologies
- CDO-squared structures and correlation trading
- Calendar spreads and roll strategies
- Capital Asset Pricing Model (CAPM)
- Capital Asset Pricing Model (CAPM) and beta estimation
- Capital expenditure planning and depreciation
- Central clearing and CCP risk management
- Commodity futures and convenience yields
- Commodity swaps and energy derivatives
- Complete markets and replication
- Corporate bond pricing and credit spread decomposition
- Crack spreads in energy markets
- Credit risk assessment and loan pricing
- Credit valuation adjustment (CVA) and counterparty risk
- Cryptocurrency valuation and blockchain technology
- Currency swaps and cross-currency basis
- Dark pools and alternative trading venues
- DeFi protocols and decentralized finance
- Deposit insurance and systemic risk
- Dividend discount model (DDM) applications
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
- Modern portfolio theory and efficient frontier
- Momentum and reversal investment strategies
- Mortgage-backed securities and prepayment modeling
- Multi-factor interest rate models
- Netting agreements and close-out procedures
- Non-deliverable forwards and emerging market instruments
- OIS discounting and collateralized interest rate derivatives
- Options on futures and forward-starting options
- Payment systems and settlement risk
- Portfolio optimization and mean-variance theory
- Prime brokerage and securities lending
- Private credit and direct lending
- Project finance and syndicated lending
- Recovery rate modeling and loss given default
- Repo markets and securities lending
- Risk factor decomposition and sensitivity analysis
- Risk parity and risk budgeting strategies
- Shadow banking and non-bank intermediation
- Smart beta and alternative indexing approaches
- Stochastic volatility in interest rate markets
- Stress testing and scenario analysis frameworks
- Swaptions and interest rate option pricing
- Swaptions and option volatility surfaces
- Synthetic CDOs and credit-linked note structures
- 'The Greeks: Delta, Gamma, Vega, Theta, and Rho sensitivity analysis'
- Too-big-to-fail policies and resolution regimes
- Treasury futures and bond basis
- Treasury securities and government bond markets
- VIX futures and volatility trading
- Value at Risk (VaR) and expected shortfall methodologies
- Value at Risk (VaR) and risk metrics
- Vasicek and CIR interest rate models
- Volatility smile and skew patterns in option markets
- Working capital and cash conversion cycle
- Wrong-way risk and correlation adjustments
- Zero-coupon bond pricing and bootstrapping
enhanced: true
enhancement_date: '2025-11-06'
enhancement_id: batch04-128375
---



# Chapter 8 - Consumption-Based Asset Pricing
%% Begin Waypoint %%
- **Chapter 8 - Consumption-Based Asset Pricing**
	- CCAPM with Alternative Preferences
	- Chapter 8 - Consumption-Based Asset Pricing
	- Consumption-Based Asset Pricing with Incomplete Markets
	- Exercises
	- General Multi-Period Link Between Consumption a
	- Long-Run Risks and Epstein-Zin Utility
	- Problems with the Empirical Studies
	- The One-Period Ccapm
	- The Simple Multi-Period Ccapm
	- Theory Meets Data - Asset Pricing Puzzles

%% End Waypoint %%
# Consumption-Based Asset Pricing
8.1 Introduction. 175   
8.2 The one-period CCAPM . 175   
8.2.1 The simple one-period CCAPM: version 1. 176   
8.2.2 The simple one-period CCAPM: version 2 177   
8.2.3 The simple one-period CCAPM: version 3 . 178   
8.2.4 The consumption-mimicking portfolio 179   
8.3 General multi-period link between consumption and asset returns 180   
8.4 The simple multi-period CCAPM 183   
8.5 Theory meets data - asset pricing puzzles 185   
8.6 Problems with the empirical studies. 187   
8.7 CCAPM with alternative preferences . 189   
8.7.1 Habit formation 190   
8.7.2 State-dependent utility: general results 191   
8.7.3 The Campbell and Cochrane model 192   
8.7.4 The Chan and Kogan model 194   
8.7.5 Epstein-Zin utility 198   
8.7.6 Durable goods 200   
8.7.7 Long-run risks and Epstein-Zin utility 200   
8.8.1 A model with long-run risks . 200   
8.8.2 The Campbell-Shiller linearization 202   
8.8.3 The state-price deflator 203   
8.8.4 The risk-free rate .. 204   
8.8.5 The premium on risky assets 204   
8.8.6 Evaluation of the model 206   
8.9 Consumption-based asset pricing with incomplete markets . 207   
8.9.1 Evidence of incomplete markets . 207   
8.9.2 Labor income risk 208   
8.10 Concluding remarks 209   
8.11 Exercises 209  


# 8.1 Introduction  

Previous chapters have shown how state-price deflators determine asset prices and how the optimal consumption choices of individuals determine state-price deflators. In this chapter we combine these observations and link asset prices to consumption. Models linking expected returns to the covariance between return and (aggregate) consumption are typically called Consumption-based Capital Asset Pricing Models (CCAPM). Such models date back to Rubinstein (1976) and Breeden (1979).  

The outline of the chapter is as follows. Section 8.2 develops the CCAPM in the one-period framework. Section 8.3 derives a general link between asset prices and consumption in a multiperiod setting, while Section 8.4 focuses on a simple and tractable specification. Section 8.5 shows that this simple specification is unable to match important empirical features of aggregate consumption and return, leaving a number of apparent asset pricing puzzles. Section 8.6 discusses some problems with such empirical studies. Some extensions of the simple model are presented in Sections 8.7 and 8.9. These extensions help resolve some of the apparent puzzles.

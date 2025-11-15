---
tags:
- '#chapter_6'
- '#individual_optimality'
- apt
- artificial-intelligence
- interest-rate-derivatives
- interest-rate-swap
- irs
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
- Barrier options and knock-in/knock-out structures
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
- Capital Asset Pricing Model (CAPM) and beta estimation
- Central clearing and CCP risk management
- Commodity futures and convenience yields
- Commodity swaps and energy derivatives
- Complete markets and replication
- Corporate bond pricing and credit spread decomposition
- Crack spreads in energy markets
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
- Net interest margin and banking profitability
- Netting agreements and close-out procedures
- Non-deliverable forwards and emerging market instruments
- OIS discounting and collateralized interest rate derivatives
- Options on futures and forward-starting options
- Payment systems and settlement risk
- Portfolio optimization and mean-variance theory
- Prime brokerage and securities lending
- Private credit and direct lending
- Project finance and syndicated lending
- Real estate investment trusts (REITs)
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
enhancement_id: batch04-769446
---



# Chapter 6 - Individual optimality
%% Begin Waypoint %%
- **Chapter 6 - Individual optimality**
	- Chapter 6 - Individual optimality
	- Dynamic Programming
	- Epstein-Zin Recursive Utility
	- Exercises
	- The Continuous-Time Framework
	- The Discrete-Time Framework
	- The One-Period Framework

%% End Waypoint %%
# Individual optimality  

[^6]: 1 Introduction . 129
[^6]: 2 The one-period framework . 129
[^6]: 2.1 Time-additive expected utility 130
[^6]: 2.2 Non-additive expected utility 132
[^6]: 2.3 A general utility index . 133
[^6]: 2.4 A two-step procedure in a complete market 133
[^6]: 2.5 Optimal portfolios and mean-variance analysis 135
[^6]: 3 The discrete-time framework 140
[^6]: 3.1 Time-additive expected utility 141
[^6]: 3.2 Habit formation utility . 142
[^6]: 4 The continuous-time framework . 143
[^6]: 5 Dynamic programming . 144
[^6]: 5.1 The discrete-time framework 145
[^6]: 5.2 The continuous-time framework . 148
[^6]: 6 Epstein-Zin recursive utility 152
[^6]: 6.1 First-order condition wrt. $c_{t}$ : 153
[^6]: 6.2 First-order condition wrt. $\pi_{t}$ 154
[^6]: 6.3 The state-price deflator 155
[^6]: 7 Concluding remarks 155

Chapter 4 discussed how the general pricing mechanism of a financial market can be represented. By a state-price deflator. Given a state-price deflator we can price all state-contingent dividends.. Conversely, given the market prices of state-contingent dividends we can extract one or several. State-price deflators. Market prices and hence the state-price deflator (s) are determined by the supply and demand of the individuals in the economy. Therefore, we have to study the portfolio decisions of individuals. This is the topic of the present chapter. In the next chapter we will then discuss market equilibrium.  

Section 6.2 studies the maximization problem of an individual under various preference speci-. Fications in the one-period setting. Sections 6.3 and 6.4 extend the analysis to the discrete-time and the continuous-time framework, respectively. The main result of these sections is that the (marginal utility of) optimal consumption of any individual induces a valid state-price deflator, which gives us a link between individual optimality and asset prices. This is the cornerstone of the consumption-based asset pricing models studied in Chapter 8. Section 6.5 introduces the dynamic programming approach to the solution of multi-period utility maximization problems. In particular, we derive the so-called envelope condition that links marginal utility of consumption to marginal utility of optimal investments. In this way the state-price deflator is related to the optimally invested wealth of the individual plus some state variables capturing other information affecting the decisions of the individual. This will be useful for the factor pricing models studied. In Chapter 9.

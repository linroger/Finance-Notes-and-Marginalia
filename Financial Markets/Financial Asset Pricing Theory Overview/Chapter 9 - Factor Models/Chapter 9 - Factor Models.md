---
tags:
- '#chapter_9'
- '#factor_models'
- apt
- arbitrage
- arbitrage-pricing
- artificial-intelligence
- capm
- defi
- equity-derivatives
- factor-models
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
- Capital Asset Pricing Model (CAPM)
- Capital Asset Pricing Model (CAPM) and beta estimation
- Central clearing and CCP risk management
- Commodity futures and convenience yields
- Commodity swaps and energy derivatives
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
enhancement_id: batch04-307453
---



# Chapter 9 - Factor Models
%% Begin Waypoint %%
- **Chapter 9 - Factor Models**
	- Chapter 9 - Factor Models
	- Empirical Factors
	- Exercises
	- Mean-Variance Efficient Returns and Pricing Fac
	- Pricing Factors in a Multi-Period Framework
	- Pricing Factors in a One-Period Framework
	- The Classical One-Period Capm
	- Theoretical Factors

%% End Waypoint %%
# Factor models  
9 Factor models 217  
9.1 Introduction 217   
9.2 The classical one-period CAPM . 218   
9.3 Pricing factors in a one-period framework 220   
9.3.1 Definition and basic properties 221   
9.3.2 Returns as pricing factors 222   
9.3.3 From a state-price deflator to a pricing factor .. 223   
9.3.4 From a pricing factor to a (candidate) state-price deflator 224   
9.3.5 The Arbitrage Pricing Theory . 225   
9.4 Mean-variance efficient returns and pricing factors. 226   
9.4.1 Orthogonal characterization . 226   
9.4.2 Link between mean-variance efficient returns and state-price deflators . . . 232   
9.4.3 Link between mean-variance efficient returns and pricing factors 232   
9.5 Pricing factors in a multi-period framework 235   
9.6 Empirical factors . 237   
9.7 Theoretical factors 238   
9.8 Exercises 239  


# 9.1 Introduction  

The lack of reliable consumption data discussed in Section 8.6 complicates tests and applications of the consumption-based models. As mentioned above, most tests that have been carried out find it problematic to match the (simple) consumption-based model and historical return and consumption data (of poor quality). This motivates a search for models linking returns to other factors than consumption.  

The classical CAPM is the Mother of all factor models. It links expected excess returns (on. Stocks) to the return on the market portfolio (of stocks). It was originally developed in a oneperiod framework but can be generalized to multi-period settings. The model is based on rather unrealistic assumptions and the empirical success of the CAPM is modest..  

Many, many papers have tried to identify factor models that perform better, mostly by adding extra factors. However, this should only be done with extreme care. In a given data set of historical returns it is always possible to find a return that works as a pricing factor, as already indicated in Chapter 4. In fact, any ex-post mean-variance efficient return will work. On the other hand, there is generally no reason to believe that the same return will work as a pricing factor in the future. Factors should be justified by economic arguments or even a theoretical asset pricing model.  

It is worth emphasizing that the general theoretical results of the consumption-based asset pricing framework are not challenged by factor models. The problem with the consumption-based models is the implementation. Factor models do not invalidate the consumption-based asset pricing framework but are special cases that may be easier to apply and test. Therefore factors should generally help explain typical individuals' marginal utilities of consumption.  

Section 9.2 reviews the classical one-period CAPM and how it fits into the modern consumptionbased asset pricing framework. Section 9.3 defines and studies pricing factors in the one-period setting. In particular, pricing factors are linked to state-price deflators. The relation between mean-variance efficient returns and pricing factors is the topic of Section 9.4. Multi-period pricing factors are introduced in Section 9.5 with a discussion of the distinction between conditional and unconditional pricing factors. Section 9.6 offers a brief introduction to empirical studies of factor models. Finally, Section 9.7 discusses how pricing factors can be derived theoretically. It also derives an intertemporal version of the CAPM.

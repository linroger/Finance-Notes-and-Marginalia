---
tags:
- arbitrage
- artificial-intelligence
- call_option
- interest-rate-derivatives
- ma
- markets
- no_arbitrage
- one_period_model
- option-greeks
- options
- options-pricing
- risk-management
- risk_free_asset
aliases:
- Exercise 3.1
- Exercise 3.2
- Exercise 3.3
- Exercise 3.4
key_concepts:
- Agricultural futures and seasonality
- Alternative investments and hedge fund strategies
- Arbitrage Pricing Theory (APT) and factor models
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
- Constant maturity swaps and roll-over features
- Crack spreads in energy markets
- Credit risk assessment and loan pricing
- Cryptocurrency valuation and blockchain technology
- Currency swaps and cross-currency basis
- Dark pools and alternative trading venues
- DeFi protocols and decentralized finance
- Delta hedging and Greeks calculation
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
- Interest rate models and term structure
- Interest rate swaps and swap spread decomposition
- Key rate duration and curve risk decomposition
- Law of One Price
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
- arbitrage-free market
- market complete
- no-arbitrage price
- one-period model
- risk-free asset
- risk-free dividend
enhanced: true
enhancement_date: '2025-11-06'
enhancement_id: batch04-971197
---




# 3.8 Exercises  

EXERCISE 3.1 Consider a one-period model with only two possible end-of-period states. Three assets are traded in an arbitrage-free market. Asset 1 is a risk-free asset with a price of 1 and an end-of-period dividend of $R^{f}$ , the risk-free gross rate of return. Asset 2 has a price of $S$ and offers. a dividend of. $u S$ in state. $^{1}$ and $d S$ in state 2..  

(a) Show that if the inequality. $d<R^{f}<u$ does not hold, there will be an arbitrage.  

Asset 3 is a call-option on asset 2 with an exercise price of $K$ . The dividend of asset 3 is therefore $C_{u}\equiv\operatorname*{max}(u S-K,0)$ in state 1 and $C_{d}\equiv\operatorname*{max}(d S-K,0)$ in state 2.  

(b) Show that a portfolio consisting of $\theta_{1}$ units of asset $1$ and $\theta_{2}$ units of asset 2, where  
$$
\theta_{1}=(R^{f})^{-1}\frac{u C_{d}-d C_{u}}{u-d},\quad\theta_{2}=\frac{C_{u}-C_{d}}{(u-d)S}
$$  

will generate the same dividend as the option.  

(c) Show that the no-arbitrage price of the option is given by  
$$
C=(R^{f})^{-1}\left(q C\boldsymbol{u}+(1-q)C_{d}\right),
$$  

where $q=(R^{f}-d)/(u-d)$  

EXERCISE 3.2 Imagine a one-period economy with two possible end-of-period states that are. equally likely. Two assets are traded. Asset 1 has an initial price of 1 and pays off 1 in state 1 and 2 in state 2. Asset 2 has an initial price of 3 and gives a payoff of 2 in state 1 and a payoff $k$ in state 2, where $k$ is some constant.  

(a) Argue that if $k=4$ , the Law of One Price does not hold. Is the Law of One Price violated for other values of $k$   
(b) For what values of $k$ is the market complete?   
(c) For what values of $k$ is the market free of arbitrage?   
(d) Assume $k=8$ . Is it possible to obtain a risk-free dividend? If so, what is the risk-free rate?  

EXERCISE 3.3 Verify Equation (3.4).  

EXERCISE 3.4 In a one-period two-state economy the risk-free interest rate over the period is $25\%$ . An asset that pays out 100 in state 1 and 200 in state 2 trades at a price of 110.  

(a) What is the no-arbitrage price of a second risky asset that pays out 200 in state 1 and 100 in state 2?   
(b) If this second risky asset trades at a higher price than what you computed in (a), how can you obtain a risk-free profit?

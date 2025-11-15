---
tags:
- american_style_derivatives
- artificial-intelligence
- binomial-model
- dva
- exercise_strategy
- interest-rate-derivatives
- interest-rate-swap
- irs
- ma
- markets
- mathematics
- monte-carlo-simulation
- numerical-simulation
- numerical_techniques
- option_pricing
- options
- options-pricing
- quantitative-pricing
- stochastic
- stopping_time
aliases:
- American derivatives
- Derivative valuation
- Early exercise
key_concepts:
- Agricultural futures and seasonality
- Alternative investments and hedge fund strategies
- American vs European options and early exercise features
- American-style derivative
- Arbitrage Pricing Theory (APT) and factor models
- Asset swaps and spread-lock strategies
- Barrier options and knock-in/knock-out structures
- Basis swaps and cross-currency basis adjustments
- Basis swaps and floating rate correlations
- Behavioral finance and market anomalies
- Best execution and regulatory requirements
- Bid-ask spreads and market making profitability
- Binomial option pricing model with multi-period trees
- Binomial tree models for option pricing
- Black-Litterman model and portfolio optimization
- Black-Scholes option pricing model and its applications
- CDO structuring and tranche allocation methodologies
- CDO-squared structures and correlation trading
- Calendar spreads and roll strategies
- Capital Asset Pricing Model (CAPM) and beta estimation
- Central clearing and CCP risk management
- Closed-form pricing formulas
- Commodity futures and convenience yields
- Commodity swaps and energy derivatives
- Constant maturity swaps and roll-over features
- Corporate bond pricing and credit spread decomposition
- Crack spreads in energy markets
- Cryptocurrency valuation and blockchain technology
- Currency swaps and cross-currency basis
- Dark pools and alternative trading venues
- DeFi protocols and decentralized finance
- Delta hedging strategies in options markets
- Deposit insurance and systemic risk
- Dividend discount model (DDM) applications
- Duration and convexity for bond price sensitivity
- ESG investing and sustainability metrics
- Enterprise value and equity value relationships
- Equity swaps and total return swaps
- Exercise strategy
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
- Holder exercise right
- Hull-White and Black-Karasinski short rate models
- IPO pricing and underpricing analysis
- Implied volatility and volatility surface modeling
- Inflation-linked swaps and CPI adjustments
- Interest rate derivatives and forward rate agreements
- Interest rate models and term structure
- Interest rate swaps and swap spread decomposition
- Key rate duration and curve risk decomposition
- Liquidity coverage ratio and funding strategies
- Liquidity-adjusted VaR and liquidity horizons
- Margin requirements and collateral optimization
- Market impact and transaction cost analysis
- Mean reversion in interest rate processes
- Mergers and acquisitions due diligence
- Metal futures and industrial commodities
- Model backtesting and validation procedures
- Momentum and reversal investment strategies
- Monte Carlo simulation for derivatives
- Monte Carlo simulation for portfolio risk assessment
- Monte Carlo simulation methods for derivative pricing
- Mortgage-backed securities and prepayment modeling
- Multi-factor interest rate models
- Negative interest rates and floor/cap structures
- Net interest margin and banking profitability
- Netting agreements and close-out procedures
- Non-deliverable forwards and emerging market instruments
- Numerical methods for PDEs
- OIS discounting and collateralized interest rate derivatives
- Optimal exercise strategy
- Options on futures and forward-starting options
- Payment systems and settlement risk
- Prime brokerage and securities lending
- Private credit and direct lending
- Project finance and syndicated lending
- Recovery rate modeling and loss given default
- Repo markets and securities lending
- Risk parity and risk budgeting strategies
- Shadow banking and non-bank intermediation
- Smart beta and alternative indexing approaches
- Stochastic volatility in interest rate markets
- Stopping time
- Stopping times and optional stopping
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
enhancement_id: batch04-665890
---




# 12.5 American-style derivatives  

Consider an American-style derivative where the holder has the right to choose when to exercise the derivative, at least within some limits. Typically exercise can take place at the expiration date $T$ or at any time before $T$ . Let $P_{\tau}$ denote the payoff if the derivative is exercised at time. $\tau\leq T$ In general,. $P_{\tau}$ may depend on the evolution of the economy up to and including time. $\tau$ , but it. is usually a simple function of the time. $\tau$ price of an underlying security or the time. $\tau$ value of a. particular interest rate. At each point in time the holder of the derivative must decide whether or not he will exercise. Of course, this decision must be based on the available information, so we are seeking an entire exercise strategy that tell us exactly in what states of the world we should exercise the derivative. We can represent an exercise strategy by an indicator function $I(\omega,t)$ which for any given state of the economy $\omega$ at time $t$ either has the value $^{1}$ or $0$ , where the value $^{1}$ indicates exercise and $0$ indicates non-exercise. For a given exercise strategy $I$ , the derivative will be exercised the first time $I(\omega,t)$ takes on the value 1. We can write this point in time as  
$$
\tau(I)=\operatorname*{min}\{s\in[t,T]\mid I(\omega,s)=1\}.
$$  

This is called a stopping time in the literature on stochastic processes. By our earlier analysis, the value of getting the payoff $V_{\tau(I)}$ at time $\tau(I)$ is given by $\operatorname{E}_{t}^{\mathbb{Q}}\left[e^{-\int_{t}^{\tau(I)}r_{u}d u}P_{\tau(I)}\right]$ If we let $\mathbb{J}[t,T]$ denote the set of all possible exercise strategies over the time period $[t,T]$ , the time $t$ value of the American-style derivative must therefore be  
$$
V_{t}=\operatorname*{sup}_{I\in\mathcal{I}[t,T]}\mathrm{E}_{t}^{\mathbb{Q}}\left[e^{-\int_{t}^{\tau(I)}r_{u}d u}P_{\tau(I)}\right].
$$  

An optimal exercise strategy. $I^{*}$ is such that.  
$$
V_{t}=\mathrm{E}_{t}^{\mathbb{Q}}\left[e^{-\int_{t}^{\tau(I^{*})}r_{u}d u}P_{\tau(I^{*})}\right].
$$  

Note that the optimal exercise strategy and the price of the derivative must be solved for simultaneously. This complicates the pricing of American-style derivatives considerably. In fact, in. all situations where early exercise may be relevant, we will not be able to compute closed-form. pricing formulas for American-style derivatives. We have to resort to numerical techniques. See. Hull (2o06) for an introduction to the standard techniques of binomial or trinomial trees, finite difference approximation of the partial differential equation that the pricing function must satisfy,. and Monte Carlo simulation.  

It is well-known that it is never strictly advantageous to exercise an American call option on a non-dividend paying asset before the final maturity date. $T$ , cf. Merton (1973c) and Hull (2006, Ch. 9). In contrast, premature exercise of an American put option on a non-dividend paying asset will be advantageous for sufficiently low prices of the underlying asset. If the underlying asset pays dividends at discrete points in time, it can be optimal to exercise an American call option prematurely but only immediately before each dividend payment date. Regarding early exercise of put options, it can never be optimal to exercise an American put on a dividend-paying asset just before a dividend payment, but at all other points in time early exercise will be optimal for sufficiently low prices of the underlying asset..

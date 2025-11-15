---
tags:
- '#chapter_7'
- '#market_equilibrium'
- apt
- artificial-intelligence
- cdo
- clearing
- collateralized-debt-obligation
- defi
- derivatives-pricing
- interest-rate-swap
- irs
- ma
- mpt
- option-greeks
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
enhancement_id: batch04-729917
---



# Market equilibrium  
7.1 Introduction 161   
7.2 Pareto-optimality and representative individuals 162   
7.3 Pareto-optimality in complete markets. 165   
7.4 Pareto-optimality in some incomplete markets . 168   
7.5 Exercises 171   
Consumption-based asset pricing 175   
%% Begin Waypoint %%
- **Chapter 7 - Market equilibrium**
	- Chapter 7 - Market equilibrium
	- Exercises
	- Pareto-Optimality and Representative Individual
	- Pareto-Optimality in Complete Markets
	- Pareto-Optimality in Some Incomplete Markets

%% End Waypoint %%
# 7.1 Introduction  

The previous chapter characterized the optimal decisions of utility-maximizing individuals who take asset prices as given. This chapter will focus on the characterization of market equilibrium asset prices. We will work throughout in a one-period model and assume that the state space is finite, $\Omega=\{1,2,\dots,S\}$ . The results can be generalized to an infinite state space and a multi-period Setting.  

First, let us define an equilibrium. Consider a one-period economy with $I$ assets and $L$ greedy and risk-averse individuals. Each asset $i$ is characterized by its time 0 price $P_{i}$ and a random variable $D_{i}$ representing the time 1 dividend. Each individual is characterized by a (strictly increasing and concave) utility index $\mathcal{U}_{l}$ and an endowment $(e_{0}^{l},e^{l})$ . An equilibrium for the economy consists of a price vector $_{P}$ and portfolios $\pmb{\theta}^{l}$ $l=1,\ldots,L$ , satisfying the two conditions  

(i) for each $l=1,\ldots,L$ $\pmb{\theta}^{l}$ is optimal for individual $\it l$ given $_{P}$ (ii) markets clear, i.e. $\textstyle\sum_{l=1}^{L}\theta_{i}^{l}=0$ for all $i=1,\dots,I$  

Associated with an equilibrium. $(P;\theta^{1},\ldots,\theta^{L})$ is an equilibrium consumption allocation $(c_{0}^{l},c^{l})$ $l=1,\ldots,L$ , defined by  

$$
c_{0}^{l}=e_{0}^{l}-\pmb{\theta}^{l}\cdot\pmb{P};\quad c_{\omega}^{l}=e_{\omega}^{l}+D_{\omega}^{\theta^{l}},\quad\omega\in\Omega.
$$  

In the market clearing condition we have assumed that the traded assets are in a net supply of. Zero and, since the time. $0$ endowment is a certain number of units of the consumption good, no one owns any assets at time 0. This might seem restrictive but it does cover the case with initial asset holdings and positive net supply of assets. Just interpret. $\pmb{\theta}^{l}$ as individual $\it l$ 's net trade in the assets, i.e. the change in the portfolio relative to the initial portfolio, and interpret the time 1. Endowment as the sum of some income from non-financial sources and the dividend from the initial. Portfolio.  

We will assume throughout that individuals have homogeneous beliefs, i.e. that they agree that probabilities of future events are measured by the probability measure. $\mathbb{P}$  

Outline of the chapter...

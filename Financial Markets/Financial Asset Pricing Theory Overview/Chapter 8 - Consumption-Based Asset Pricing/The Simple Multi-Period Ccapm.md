---
tags:
- capm
- ccapm
- consumption_based_model
- crra_utility
- derivatives-pricing
- interest-rate-derivatives
- interest-rate-swap
- irs
- ma
- markets
- mpt
- option-greeks
- risk-management
- risk_free_rate
- sharpe-ratio
- sharpe_ratio
- stochastic
- value-at-risk
- var
aliases:
- Multi-Period CCAPM
- Simple CCAPM
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
- Binomial tree models for option pricing
- Black-Litterman model and portfolio optimization
- Black-Scholes option pricing model and its applications
- Brownian motion and Wiener processes
- CDO structuring and tranche allocation methodologies
- CDO-squared structures and correlation trading
- CRRA utility
- Calendar spreads and roll strategies
- Capital Asset Pricing Model (CAPM)
- Capital Asset Pricing Model (CAPM) and beta estimation
- Central clearing and CCP risk management
- Commodity futures and convenience yields
- Commodity swaps and energy derivatives
- Constant Sharpe ratio
- Constant maturity swaps and roll-over features
- Corporate bond pricing and credit spread decomposition
- Crack spreads in energy markets
- Credit risk assessment and loan pricing
- Cryptocurrency valuation and blockchain technology
- Currency swaps and cross-currency basis
- Dark pools and alternative trading venues
- DeFi protocols and decentralized finance
- Delta hedging and Greeks calculation
- Delta hedging strategies in options markets
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
- Interest rate derivatives and forward rate agreements
- Interest rate models and term structure
- Interest rate swaps and swap spread decomposition
- Key rate duration and curve risk decomposition
- Liquidity coverage ratio and funding strategies
- Liquidity-adjusted VaR and liquidity horizons
- Lognormal consumption
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
- Representative individual
- Risk factor decomposition and sensitivity analysis
- Risk parity and risk budgeting strategies
- Risk-free return
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
- Value vs growth investing frameworks
- Vasicek and CIR interest rate models
- Volatility smile and skew patterns in option markets
- Working capital and cash conversion cycle
- Wrong-way risk and correlation adjustments
- Zero-coupon bond pricing and bootstrapping
enhanced: true
enhancement_date: '2025-11-06'
enhancement_id: batch04-974049
---




# 8.4 The simple multi-period CCAPM  

A large part of the asset pricing literature makes (not always explicitly stated, unfortunately) the following additional assumptions:  

[^1]: the economy has a representative individual with CRRA time-additive utility, i.e. $u(C)=$ $\frac{1}{1-\gamma}C^{1-\gamma}$

[^2]: future aggregate consumption is lognormally distributed.

In the discrete-time version of the model, we can proceed as in version 2 of the one-period model. The first assumption leads to a marginal rate of substitution given by  
$$
{\frac{u^{\prime}(C_{t+1})}{u^{\prime}(C_{t})}}=\left({\frac{C_{t+1}}{C_{t}}}\right)^{-\gamma}=\exp\left\{-\gamma\ln\left({\frac{C_{t+1}}{C_{t}}}\right)\right\}.
$$  

By the second assumption, $\ln\left(C_{t+1}/C_{t}\right)\sim N(\bar{g},\sigma_{C}^{2})$ , and hence  
$$
\operatorname{E}_{t}\left[{\frac{u^{\prime}(C_{t+1})}{u^{\prime}(C_{t})}}\right]=\operatorname{E}_{t}\left[\exp\left\{-\gamma\ln\left({\frac{C_{t+1}}{C_{t}}}\right)\right\}\right]=\exp\left\{-\gamma{\bar{g}}+{\frac{1}{2}}\gamma^{2}\sigma_{C}^{2}\right\}
$$  

and  
$$
{\frac{\sigma_{t}\left(u^{\prime}(C_{t+1})/u^{\prime}(C_{t})\right)}{\operatorname{E}_{t}\left[u^{\prime}(C_{t+1})/u^{\prime}(C_{t})\right]}}={\sqrt{e^{\gamma^{2}\sigma_{C}^{2}}-1}}\approx\gamma\sigma_{C}.
$$  

According to (8.17), the gross risk-free return over the period from $t$ to $t+1$ is then given by  
$$
R_{t}^{f}=e^{\delta}\left(\mathrm{E}_{t}\left[\left(C_{t+1}/C_{t}\right)^{-\gamma}\right]\right)^{-1}=\exp\left\{\delta+\gamma\bar{g}-{\frac{1}{2}}\gamma^{2}\sigma_{C}^{2}\right\}
$$  

so that the continuously compounded risk-free rate of return becomes  
$$
r_{t}^{f}\equiv\ln R_{t}^{f}=\delta+\gamma\bar{g}-\frac{1}{2}\gamma^{2}\sigma_{C}^{2}.
$$  

From (8.19) we conclude that in the simple model the excess expected gross return on a risky asset is  
$$
\begin{array}{c}{{\displaystyle\mathrm{E}_{t}\left[R_{i,t+1}\right]-R_{t}^{f}\approx-\gamma\sigma_{C}\rho_{t}\left[R_{i,t+1},\left(\frac{C_{t+1}}{C_{t}}\right)^{-\gamma}\right]\sigma_{t}\left[R_{i,t+1}\right]}}\ {{\approx\gamma\sigma_{C}\rho_{t}\left[R_{i,t+1},\displaystyle\frac{C_{t+1}}{C_{t}}\right]\sigma_{t}\left[R_{i,t+1}\right],}}\end{array}
$$  

where the last expression follows from a first-order Taylor approximation as in Section 8.2.2. If. we further assume that the future asset price and the future consumption level are simultaneously lognormally distributed, we are back in version 3 of the one-period model so that we get.  
$$
\mathrm{E}_{t}[\ln R_{i,t+1}]-\ln R_{t}^{f}+{\frac{1}{2}}\mathrm{Var}_{t}[\ln R_{i,t+1}]=\gamma\sigma_{C}\rho_{t}\left[\ln R_{i,t+1},\ln\left({\frac{C_{t+1}}{C_{t}}}\right)\right]\sigma_{t}\left[\ln R_{i,t+1}\right]
$$  

or, equivalently,  
$$
\ln\left(\mathrm{E}_{t}[R_{i,t+1}]\right)-\ln R_{t}^{f}=\gamma\sigma_{C}\rho_{t}\left[\ln R_{i,t+1},\ln\left(\frac{C_{t+1}}{C_{t}}\right)\right]\sigma_{t}\left[\ln R_{i,t+1}\right].
$$  

In the formulas above the mean $g$ and variance $\sigma^{2}$ of consumption growth can vary over time, but in the stationary case where both are constant we see that the risk-free interest rate must also be constant. Furthermore, a risky asset with a constant correlation with consumption growth will have a constant Sharpe ratio $\left(\mathrm{E}_{t}\left[R_{i,t+1}\right]-R_{t}^{f}\right)/\sigma_{t}[R_{i,t+1}]$ . If the standard deviation of the return is constant, the expected excess rate of return will also be constant.  

In the continuous-time version of the stationary simple consumption-based model, the second assumption means that $\mu_{C t}$ and $\sigma_{C t}$ in the consumption process (8.21) are constant, i.e. consumption follows a geometric Brownian motion. It follows from (8.23) and (8.25) that the model with these assumptions generate a constant continuously compounded short-term risk-free interest rate Of  
$$
r^{f}=\delta+\gamma\mu_{C}-\frac{1}{2}\gamma(1+\gamma)\ | \pmb{\sigma}_{C}\ | ^{2}
$$  

and a constant Sharpe ratio for asset $i$ given by  
$$
\frac{\mu_{i t}+\delta_{i t}-r^{f}}{\ | \pmb{\sigma}_{i t}\ | }=\gamma\rho_{i C}\ | \pmb{\sigma}_{C}\ | 
$$  

if the asset has a constant correlation with consumption.

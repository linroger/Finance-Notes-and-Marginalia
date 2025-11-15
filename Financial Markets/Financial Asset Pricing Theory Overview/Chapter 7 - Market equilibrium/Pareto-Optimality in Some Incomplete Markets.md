---
tags:
- abs
- alm
- arrow_debreu_asset
- artificial-intelligence
- beta
- defi
- hara_utility
- incomplete_markets
- interest-rate-swap
- irs
- ma
- market_completeness
- mpt
- option-greeks
- options
- pareto_optimality
- risk-management
- sifi
aliases:
- Incomplete Markets
- Pareto Optimality
key_concepts:
- Agricultural futures and seasonality
- Alternative investments and hedge fund strategies
- Arbitrage Pricing Theory (APT) and factor models
- Arrow-Debreu style asset
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
- Complete markets and replication
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
- HARA utility functions
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
- Pareto-optimal consumption allocation
- Payment systems and settlement risk
- Portfolio optimization and mean-variance theory
- Prime brokerage and securities lending
- Private credit and direct lending
- Project finance and syndicated lending
- Real estate investment trusts (REITs)
- Recovery rate modeling and loss given default
- Repo markets and securities lending
- Risk factor decomposition and sensitivity analysis
- Risk parity and risk budgeting strategies
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
- aggregate consumption
- effectively complete markets
enhanced: true
enhancement_date: '2025-11-06'
enhancement_id: batch04-479401
---




# 7.4 Pareto-optimality in some incomplete markets  

In the previous section we saw that complete market equilibria are Pareto-optimal. However, as discussed earlier, real-life financial markets are probably not complete. Equilibrium consumption allocations in incomplete markets will generally not be Pareto-optimal since the individuals cannot necessarily implement the trades needed to align their marginal rates of substitution. On the other hand, individuals do not have to be able to implement any possible consumption plan so we do not need markets to be complete in the strict sense. If every Pareto-optimal consumption allocation can be obtained by trading in the available assets, the market is said to be effectively complete. If the market is effectively complete, we can use the representative individual approach to asset pricing. In this section we will discuss some examples of effectively complete markets.  

For any Pareto-optimal consumption allocation we know from Theorem 7.2 that the consumption of any individual is an increasing function of aggregate consumption. Individual consumption is measurable with respect to aggregate consumption. As in the discussion below Theorem 7.2, suppose that the possible values of aggregate consumption are. $x_{1},\ldots,x_{K}$ and let $\Omega_{k}~=~\{\omega~\in$ $\Omega | C_{\omega}=x_{k}\}$ be the set of states in which aggregate consumption equals. $x_{k}$ . If it is possible for each $k$ to form a portfolio that provides a payment of 1 if the state is in. $\Omega_{k}$ and a zero payment otherwise --an Arrow-Debreu style asset for aggregate consumption--then the market is effectively complete. (See also Exercise 7.3.) The individuals are indifferent between states within a given subset $\Omega_{k}$ . Risk beyond aggregate consumption risk does not carry any premium. Assuming strictly increasing utility functions, aggregate time 1 consumption will equal aggregate time 1 endowment. If we think of the aggregate endowment as the total value of the market, aggregate consumption will equal the value of the market portfolio and we can partition the state space according to the value or return of the market portfolio. Risk beyond market risk is diversified away and does not carry any premium.

If there is a full set of Arrow-Debreu style assets for aggregate consumption, markets will be. effectively complete for all strictly increasing and concave utility functions. The next theorem,. which is due to Rubinstein (1974), shows that markets are effectively complete under weaker assumptions on the available assets if individuals have utility functions of the HARA class with identical risk cautiousness. Before stating the precise result, let us review a few facts about the HARA utility functions which were defined in Section 5.6. A utility function. $u$ is of the HARA class, if the absolute risk tolerance is affine, i.e..  
$$
\operatorname{ART}(c)\equiv-{\frac{u^{\prime}(c)}{u^{\prime\prime}(c)}}=\alpha c+\beta.
$$  

The risk cautiousness is A. $\mathrm{RT}^{\prime}(c)=\alpha$ . Ignoring insignificant constants, the marginal utility must be either  
$$
u^{\prime}(c)=e^{-c/\beta},
$$  

for the case $\alpha=0$ (corresponding to negative exponential utility), or  
$$
u^{\prime}(c)=\left(\alpha c+\beta\right)^{-1/\alpha},
$$  

for the case $\alpha\neq0$ (which encompasses extended log-utility, satiation HARA utility, and subsistence HARA utility).  

Theorem 7.6 Suppose that  

(i) all individuals have time-additive HARA utility functions with identical risk cautiousness;  

(ii) a risk-free asset is traded;  

(ii) the time 1 endowment of all individuals are spanned by traded assets, i.e. $e^{l}\in\mathcal{M}$ $l=1,\ldots,L$  

Then the equilibrium is Pareto-optimal and the economy has a representative individual. The optimal consumption for any individual is a strictly increasing affine function of aggregate consumption.  

Proof: Suppose first that the market is complete. Then we know that the equilibrium consumption allocation will be Pareto-optimal and we can find a weighting vector $\pmb{\eta}=(\eta_{1},\dots,\eta_{L})^{\top}$ so that  
$$
\eta_{k}e^{-\delta_{k}}u_{k}^{\prime}(c_{\omega}^{k})=\eta_{l}e^{-\delta_{l}}u_{l}^{\prime}(c_{\omega}^{l})
$$  

for any two individuals $k$ and $\textit{l}$ and any $\omega$ . Assume that the common risk cautiousness $\alpha$ is different from zero so that  
$$
u_{l}^{\prime}(c)=(\alpha c+\beta_{l})^{-1/\alpha},\quad l=1,\ldots,L.
$$  

(The proof for the case. $\alpha=0$ is similar.) Substituting this into the previous equation, we obtain  
$$
\eta_{k}e^{-\delta_{k}}\left(\alpha c_{\omega}^{k}+\beta_{k}\right)^{-1/\alpha}=\eta_{l}e^{-\delta_{l}}\left(\alpha c_{\omega}^{l}+\beta_{l}\right)^{-1/\alpha},
$$  

which implies that  
$$
\left(\eta_{k}e^{-\delta_{k}}\right)^{-\alpha}\left(\alpha c_{\omega}^{k}+\beta_{k}\right)\left(\eta_{l}e^{-\delta_{l}}\right)^{\alpha}=\alpha c_{\omega}^{l}+\beta_{l}.
$$  

Summing up over $l=1,\ldots,L$ , we get  
$$
\left(\eta_{k}e^{-\delta_{k}}\right)^{-\alpha}\left(\alpha c_{\omega}^{k}+\beta_{k}\right)\sum_{l=1}^{L}\left(\eta_{l}e^{-\delta_{l}}\right)^{\alpha}=\alpha\sum_{l=1}^{L}c_{\omega}^{l}+\sum_{l=1}^{L}\beta_{l}=\alpha C_{\omega}+\sum_{l=1}^{L}\beta_{l},
$$  

where $C_{\omega}$ is aggregate consumption (or endowment) in state $\omega$ . Solving for $c_{\omega}^{k}$ , we find that.  
$$
c_{\omega}^{k}=\frac{\alpha C_{\omega}+\sum_{l=1}^{L}\beta_{l}}{\alpha\left(\eta_{k}e^{-\delta_{k}}\right)^{-\alpha}\sum_{l=1}^{L}\left(\eta_{l}e^{-\delta_{l}}\right)^{\alpha}}-\frac{\beta_{k}}{\alpha}\equiv A_{k}C_{\omega}+B_{k},
$$  

which is strictly increasing and affine in $C_{\omega}$  

The same consumption allocation can be obtained in a market where a risk-free asset exists and the time 1 endowments of all individuals are spanned by traded assets..  

Under the additional assumption that the time preference rates of individuals are identical, $\delta_{l}=\delta$ for all $l=1,\ldots,L$ , we can show a bit more:  

Theorem 7.7 If the assumptions of Theorem 7.6 are satisfied and individuals have identical. time preference rates, then the relative weights which the representative individual associates to. individuals-and therefore equilibrium asset prices-will be independent of the initial distribution of aggregate endowment across individuals.  

Proof: In order to verify this, we will compute the utility function of the representative individual. Since we are assuming time-additive utility, we will derive. $u_{\eta,0}$ and $u_{\eta,1}$ defined in (7.19) and (7.20) for any given weighting vector $\pmb{\eta}$ . We will focus on the case where the common risk cautiousness. $\alpha$ is non-zero and different from $^{1}$ so that  
$$
u_{l}(c)=\frac{1}{1-1/\alpha}\left(\alpha c+\beta_{l}\right)^{1-1/\alpha},\quad u_{l}^{\prime}(c)=\left(\alpha c+\beta_{l}\right)^{-1/\alpha},\quad l=1,\ldots,L.
$$  

(In Exercise 7.2 you are asked to do the same for the cases of extended log-utility ( $\alpha=1$ ) and negative exponential utility ( $\alpha=0$ ).) The first-order condition for the maximization in the definition of $u_{\eta,0}$ implies that  
$$
\eta_{l}\left(\alpha c+\beta_{l}\right)^{-1/\alpha}=\nu,
$$  

where $\nu$ is the Lagrange multiplier. Rearranging, we get  
$$
\alpha c_{0}^{l}+\beta_{l}=\nu^{-\alpha}\eta_{l}^{\alpha}.
$$  

Summing up over $\textit{l}$ gives  
$$
\alpha c_{0}+\sum_{l=1}^{L}\beta_{l}=\nu^{-\alpha}\sum_{l=1}^{L}\eta_{l}^{\alpha},
$$  

so that the Lagrange multiplier is  
$$
\nu=\left(\alpha c_{0}+\sum_{l=1}^{L}\beta_{l}\right)^{-1/\alpha}\left(\sum_{l=1}^{L}\eta_{l}^{\alpha}\right)^{1/\alpha}.
$$  

Substituting this back into (7.22), we see that the solution to the maximization problem is such that  
$$
\eta_{l}\left(\alpha c+\beta_{l}\right)^{-1/\alpha}=\left(\alpha c_{0}+\sum_{l=1}^{L}\beta_{l}\right)^{-1/\alpha}\left(\sum_{l=1}^{L}\eta_{l}^{\alpha}\right)^{1/\alpha},
$$  

which implies that  
$$
\begin{array}{l}{{\displaystyle u_{\eta,0}(c_{0})=\sum_{l=1}^{L}\eta_{l}\frac{1}{1-1/\alpha}\left(\alpha c_{0}^{l}+\beta_{l}\right)^{1-1/\alpha}}}\ {{\displaystyle\quad=\frac{1}{1-1/\alpha}\sum_{l=1}^{L}\left(\alpha c_{0}^{l}+\beta_{l}\right)\eta_{l}\left(\alpha c_{0}^{l}+\beta_{l}\right)^{-1/\alpha}}}\ {{\displaystyle\quad\quad=\frac{1}{1-1/\alpha}\left(\alpha c_{0}+\sum_{l=1}^{L}\beta_{l}\right)^{-1/\alpha}\left(\sum_{l=1}^{L}\eta_{l}^{\alpha}\right)^{1/\alpha}\sum_{l=1}^{L}\left(\alpha c_{0}^{l}+\beta_{l}\right)}}\ {{\displaystyle\quad\quad=\frac{1}{1-1/\alpha}\left(\sum_{l=1}^{L}\eta_{l}^{\alpha}\right)^{1/\alpha}\left(\alpha c_{0}+\sum_{l=1}^{L}\beta_{l}\right)^{1-1/\alpha}.}}\end{array}
$$  

Almost identical computations lead to  
$$
u_{\eta,1}(c)=e^{-\delta}\frac{1}{1-1/\alpha}\left(\sum_{l=1}^{L}\eta_{l}^{\alpha}\right)^{1/\alpha}\left(\alpha c+\sum_{l=1}^{L}\beta_{l}\right)^{1-1/\alpha}
$$  

The utility function of the representative individual is therefore of the same class as the individual utility functions,  
$$
\begin{array}{r}{\mathcal{U}_{\eta}(c_{0},c)=u_{\eta,0}(c_{0})+\mathrm{E}\left[u_{\eta,1}(c)\right]=u_{\eta}(c_{0})+e^{-\delta}\mathrm{E}[u_{\eta}(c)],}\end{array}
$$  

where  
$$
u_{\eta}(c)=\frac{1}{1-1/\alpha}\left(\sum_{l=1}^{L}\eta_{l}^{\alpha}\right)^{1/\alpha}\left(\alpha c+\sum_{l=1}^{L}\beta_{l}\right)^{1-1/\alpha}.
$$  

More importantly, the state-price deflator is  
$$
\begin{array}{c}{{\zeta=e^{-\delta}\displaystyle\frac{u_{\eta}^{\prime}(c)}{u_{\eta}^{\prime}(c_{0})}=e^{-\delta}\displaystyle\frac{\left(\sum_{l=1}^{L}\eta_{l}^{\alpha}\right)^{1/\alpha}\left(\alpha c+\sum_{l=1}^{L}\beta_{l}\right)^{-1/\alpha}}{\left(\sum_{l=1}^{L}\eta_{l}^{\alpha}\right)^{1/\alpha}\left(\alpha c_{0}+\sum_{l=1}^{L}\beta_{l}\right)^{-1/\alpha}}}}\ {{=e^{-\delta}\displaystyle\frac{\left(\alpha c+\sum_{l=1}^{L}\beta_{l}\right)^{-1/\alpha}}{\left(\alpha c_{0}+\sum_{l=1}^{L}\beta_{l}\right)^{-1/\alpha}},}}\end{array}
$$  

which is independent of the weighting vector $\pmb{\eta}$ . The state-price deflator and, hence, the asset prices are independent of the distribution of endowment across individuals.

---
tags:
- artificial-intelligence
- consumption_allocation
- defi
- interest-rate-swap
- irs
- lagrange-multipliers
- ma
- mpt
- option-greeks
- options
- options-pricing
- pareto_optimality
- risk-management
- risk_sharing
- utility_function
- value-at-risk
- var
- welfare_theorem
aliases:
- Central Planner
- Pareto optimal
- Second Welfare Theorem
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
- CDO structuring and tranche allocation methodologies
- CDO-squared structures and correlation trading
- Calendar spreads and roll strategies
- Capital Asset Pricing Model (CAPM) and beta estimation
- Central bank digital currencies (CBDCs)
- Central clearing and CCP risk management
- Central planner's problem
- Commodity futures and convenience yields
- Commodity swaps and energy derivatives
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
- Extreme value theory and tail risk modeling
- FX futures and currency hedging
- Fama-French three-factor and five-factor models
- Feasible consumption plan
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
- Marginal rates of substitution
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
- Pareto-optimal consumption allocation
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
- Stochastic volatility in interest rate markets
- Stress testing and scenario analysis frameworks
- Swaptions and interest rate option pricing
- Swaptions and option volatility surfaces
- Synthetic CDOs and credit-linked note structures
- Terminal value modeling and exit multiples
- 'The Greeks: Delta, Gamma, Vega, Theta, and Rho sensitivity analysis'
- Time-additive expected utility
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
enhancement_id: batch04-687022
---




# 7.2 Pareto-optimality and representative individuals  

Define the aggregate initial and future endowment in the economy as  
$$
\bar{e}_{0}=\sum_{l=1}^{L}e_{0}^{l},\quad\bar{e}_{\omega}=\sum_{l=1}^{L}e_{\omega}^{l}.
$$  

(If we allow for assets in a positive net supply, the dividends of those assets are to be included in the time 1 aggregate endowment.) A consumption allocation $\{(c_{0}^{1},c^{1}),\ldots,(c_{0}^{L},c^{L})\}$ is said to be feasible if  
$$
\sum_{l=1}^{L}c_{0}^{l}\leq\bar{e}_{0};\quad\sum_{l=1}^{L}c_{\omega}^{l}\leq\bar{e}_{\omega},\quad\omega\in\Omega.
$$  

Here, the left-hand sums define the aggregate consumption,  
$$
C_{0}=\sum_{l=1}^{L}c_{0}^{l},\quad C_{\omega}=\sum_{l=1}^{L}c_{\omega}^{l}.
$$  

A consumption allocation $\{(c_{0}^{1},c^{1}),\ldots,(c_{0}^{L},c^{L})\}$ is Pareto-optimal if it is feasible and there is no other feasible consumption plan $\{(\hat{c}_{0}^{1},\hat{c}^{1}),\dots,(\hat{c}_{0}^{L},\hat{c}^{L})\}$ such that $\mathcal{U}_{l}(\hat{c}_{0}^{l},\hat{c}^{l})\geq\mathcal{U}_{l}(c_{0}^{l},{\pmb{c}}^{l})$ for all $l=1,\ldots,L$ with strict inequality for some $\it l$  

Pareto-optimality of consumption allocations is closely linked to the solution to the allocation problem of a hypothetical central planner. Let $\pmb{\eta}=(\eta_{1},\dots,\eta_{L})^{\top}$ be a vector of strictly positive numbers, one for each individual. Define the function $\mathcal{U}_{\pmb{\eta}}:\mathbb{R}_{+}\times\mathbb{R}_{+}^{S}\rightarrow\mathbb{R}$ by  
$$
\mathcal{U}_{\eta}(\bar{e}_{0},\bar{e})=\operatorname*{sup}\left\{\sum_{l=1}^{L}\eta_{l}\mathcal{U}_{l}(c_{0}^{l},c^{l})\big | \sum_{l=1}^{L}c_{0}^{l}\leq\bar{e}_{0},\sum_{l=1}^{L}c_{\omega}^{l}\leq\bar{e}_{\omega},c_{0}^{l},c_{\omega}^{l}\geq0,\mathrm{~for~all~}\omega\mathrm{~and~}l\right\}.
$$  

Here, $\textstyle\sum_{l=1}^{L}\eta_{l}\mathcal{U}_{l}(c_{0}^{l},\pmb{c}^{l})$ is a linear combination of the utilities of the individuals when individual $\textit{l}$ follows the consumption plan $(c_{0}^{l},c^{l})$ . This linear combination is maximized over all feasible allocations of the total endowment $(\bar{e}_{0},\bar{e})$ . Given the total endowment and the weights $\pmb{\eta}$ on individuals, $\uplambda_{\eta}$ gives the best linear combination of utilities that can be obtained. As long as the individuals' utility indices are increasing and concave, $\uplambda_{\eta}$ will also be increasing and concave. We can thus think of $\uplambda_{\eta}$ as the utility index of a greedy and risk-averse individual, a central planner giving weights to the individual utility functions. The following theorem, sometimes called the Second Welfare Theorem, gives the link to Pareto-optimality:  

Theorem 7.1 Given any Pareto-optimal consumption allocation with aggregate consumption $(C_{0},C)$ a strictly positive weighting vector. $\pmb{\eta}=(\eta_{1},\dots,\eta_{L})^{\top}$ exists so that the same allocation maximizes. $\mathcal{U}_{\eta}(C_{0},C)$  

Consequently, we can find Pareto-optimal allocations by solving the central planner's problem for a given weighting vector $\eta$ . The Lagrangian of the central planner's constrained maximization problem is  
$$
\mathcal{L}=\sum_{l=1}^{L}\eta_{l}\mathcal{U}_{l}(c_{0}^{l},c^{l})+\alpha_{0}\left(C_{0}-\sum_{l=1}^{L}c_{0}^{l}\right)+\sum_{\omega=1}^{S}\alpha_{\omega}\left(C_{\omega}-\sum_{l=1}^{L}c_{\omega}^{l}\right),
$$  

where $\alpha_{0},\alpha_{1},\ldots,\alpha_{S}$ are Lagrange multipliers. The first-order conditions are  
$$
\begin{array}{r l}{\displaystyle\frac{\partial\mathcal{L}}{\partial c_{0}^{l}}=0\quad\Leftrightarrow\quad\eta_{l}\frac{\partial\mathcal{U}_{l}}{\partial c_{0}^{l}}=\alpha_{0},\quad l=1,\dots,L,}\ {\displaystyle\frac{\partial\mathcal{L}}{\partial c_{\omega}^{l}}=0\quad\Leftrightarrow\quad\eta_{l}\frac{\partial\mathcal{U}_{l}}{\partial c_{\omega}^{l}}=\alpha_{\omega},\quad\omega=1,\dots,S,\quad l=1,\dots,L,}\ {\displaystyle\frac{\partial\mathcal{L}}{\partial\alpha_{0}}=0\quad\Leftrightarrow\quad\sum_{l=1}^{L}c_{0}^{l}=C_{0},}\ {\displaystyle\frac{\partial\mathcal{L}}{\partial\alpha_{\omega}}=0\quad\Leftrightarrow\quad\sum_{l=1}^{L}c_{\omega}^{l}=C_{\omega},\quad\omega=1,\dots,S.}\end{array}
$$  

Note that since we can scale all $\eta_{l}$ 's by a positive constant without affecting the maximizing consumption allocation, we might as well assume $\alpha_{0}=1$ . Given strictly increasing and concave utility functions with infinite marginal utility at zero, the first-order conditions are both necessary and sufficient for optimality. We can thus conclude that a feasible consumption allocation is Paretooptimal if and only if we can find a weighting vector $\pmb{\eta}=(\eta_{1},\dots,\eta_{L})^{\top}$ so that (7.1) and (7.2) are satisfied. In particular, by dividing (7.2) by (7.1), it is clear that we need to have  

with the consequence that  
$$
\frac{\frac{\partial{\mathcal U}_{l}}{\partial c_{\omega}^{l}}}{\frac{\partial{\mathcal U}_{l}}{\partial c_{0}^{l}}}=\frac{\alpha_{\omega}}{\alpha_{0}},\quad\omega=1,\ldots,S,\quad l=1,\ldots,L,
$$  
$$
\frac{\frac{\partial\mathcal{U}_{k}}{\partial c_{\omega}^{k}}}{\frac{\partial\mathcal{U}_{k}}{\partial c_{0}^{k}}}=\frac{\frac{\partial\mathcal{U}_{l}}{\partial c_{\omega}^{l}}}{\frac{\partial\mathcal{U}_{l}}{\partial c_{0}^{l}}},\quad\omega=1,\ldots,S,
$$  

for any individuals $k$ and $\textit{l}$ , i.e. the individuals align their marginal rates of substitution. This property is often referred to as efficient risk-sharing. The central planner will distribute aggregate consumption risk so that all individuals have the same marginal willingness to shift consumption across time and states.  

Note that if individuals have time-additive expected utility, i.e.  
$$
\mathcal{U}_{l}(c_{0},c)=u_{l}(c_{0})+e^{-\delta_{l}}\operatorname{E}[u_{l}(c)]=u_{l}(c_{0})+e^{-\delta_{l}}\sum_{\omega=1}^{S}p_{\omega}u_{l}(c_{\omega}),
$$  

we can replace (7.1) and (7.2) by  
$$
\begin{array}{c}{{\eta_{l}u_{l}^{\prime}(c_{0}^{l})=\alpha_{0},\quad l=1,\ldots,L,}}\ {{\mathrm{}}}\ {{\eta_{l}e^{-\delta_{l}}p_{\omega}u_{l}^{\prime}(c_{\omega}^{l})=\alpha_{\omega},\quad\omega=1,\ldots,S,\quad l=1,\ldots,L.}}\end{array}
$$  

Dividing the second equation by the first, we see that a Pareto-optimal consumption allocation has the property that  
$$
e^{-\delta_{k}}\frac{u_{k}^{\prime}(c_{\omega}^{k})}{u_{k}^{\prime}(c_{0}^{k})}=e^{-\delta_{l}}\frac{u_{l}^{\prime}(c_{\omega}^{l})}{u_{l}^{\prime}(c_{0}^{l})},\quad\omega=1,\dots,S,
$$  

for any two individuals $k$ and $\textit{l}$  

The following theorem shows that all Pareto-optimal consumption allocations have the property that the consumption of individuals move together..  

Theorem 7.2 For any Pareto-optimal consumption allocation, the consumption of any individual will be a strictly increasing function of aggregate consumption, i.e. for any. $l$ $c^{l}=f_{l}(C)$ for some strictly increasing function. $f_{l}$  

Proof: Given some Pareto-optimal consumption allocation $(c_{0}^{l},c^{l})$ $l~=~1,\ldots,L$ .Assume for simplicity that preferences can be represented by time-additive expected utility. From Theorem 7.1 we know that we can find a weighting vector $\pmb{\eta}=(\eta_{1},\dots,\eta_{L})^{\top}$ so that (7.7) and (7.8) hold. In particular, we have  
$$
\begin{array}{c}{{\eta_{k}u_{k}^{\prime}(c_{0}^{k})=\eta_{l}u_{l}^{\prime}(c_{0}^{l}),}}\ {{\eta_{k}e^{-\delta_{k}}u_{k}^{\prime}(c_{\omega}^{k})=\eta_{l}e^{-\delta_{l}}u_{l}^{\prime}(c_{\omega}^{l}),\quad\omega=1,\ldots,S,}}\end{array}
$$  

for any two individuals $k$ and $\textit{l}$ . Moreover, for any two states $\omega,\omega^{\prime}\in\Omega$ , we must have  
$$
\frac{u_{k}^{\prime}(c_{\omega}^{k})}{u_{k}^{\prime}(c_{\omega^{\prime}}^{k})}=\frac{u_{l}^{\prime}(c_{\omega}^{l})}{u_{l}^{\prime}(c_{\omega^{\prime}}^{l})}.
$$  

Aggregate consumption in state $\omega$ is $\begin{array}{r}{C_{\omega}=\sum_{l=1}^{L}c_{\omega}^{l}}\end{array}$ , where the sum is over all individuals. Suppose. that aggregate consumption is higher in state $\omega$ than in state $\omega^{\prime}$ , i.e. $C_{\omega}>C_{\omega^{\prime}}$ . Then there must at least one individual, say individual. $\it l$ , who consumes more in state. $\omega$ than in state $\omega^{\prime}$ $c_{\omega}^{l}>c_{\omega^{\prime}}^{l}$ Consequently, $u_{l}^{\prime}(c_{\omega}^{l})<u_{l}^{\prime}(c_{\omega^{\prime}}^{l})$ . But then (7.10) implies that $u_{k}^{\prime}(c_{\omega}^{k})<u_{k}^{\prime}(c_{\omega^{\prime}}^{k})$ and thus $c_{\omega}^{k}>c_{\omega^{\prime}}^{k}$ for all individuals $k$  

A consequence of the previous theorem is that with Pareto-optimal allocations individuals do not have to distinguish between states in which aggregate consumption is the same. Aggregate. consumption $C$ at time 1 is a random variable that induces a partition of the state space. Suppose. that the possible values of aggregate consumption are. $x_{1},\ldots,x_{K}$ and let $\Omega_{k}=\{\omega\in\Omega | C_{\omega}=x_{k}\}$ be the set of states in which aggregate consumption equals. $x_{k}$ . Then $\Omega=\Omega_{1}\cup\dots\cup\Omega_{K}$ . For any individual $\textit{l}$ , we can define a valid state-price vector by
$$
\psi_{\omega}=e^{-\delta_{l}}\frac{p_{\omega}u_{l}^{\prime}(c_{\omega}^{l})}{u_{l}^{\prime}(c_{0}^{l})}=e^{-\delta_{l}}\frac{p_{\omega}u_{l}^{\prime}(f_{l}(C_{\omega}))}{u_{l}^{\prime}(c_{0}^{l})}.
$$  

Define  
$$
\begin{array}{r l}&{\psi(k)=\displaystyle\sum_{\omega\in\Omega_{k}}\psi_{\omega}=\displaystyle\sum_{\omega\in\Omega_{k}}e^{-\delta_{l}}\frac{p_{\omega}u_{l}^{\prime}(f_{l}(C_{\omega}))}{u_{l}^{\prime}(c_{0}^{l})}}\ &{\quad=e^{-\delta_{l}}\frac{u_{l}^{\prime}\left(f_{l}(x_{k})\right)}{u_{l}^{\prime}(c_{0}^{l})}\displaystyle\sum_{\omega\in\Omega_{k}}p_{\omega}=e^{-\delta_{l}}\frac{u_{l}^{\prime}\left(f_{l}(x_{k})\right)}{u_{l}^{\prime}(c_{0}^{l})}\mathbb{P}(C=x_{k}),}\end{array}
$$  

which can be interpreted as the value of an asset with a dividend of one if aggregate consumption turns out to be $x_{k}$ and a zero dividend in other cases. The price of any marketed dividend. $D$ can then be written as  
$$
\begin{array}{l}{\displaystyle P=\sum_{\omega=1}^{S}\psi_{\omega}D_{\omega}=\sum_{k=1}^{K}\sum_{\omega\in\Omega_{k}}\psi_{\omega}D_{\omega}}\ {\displaystyle}&{\displaystyle=\sum_{k=1}^{K}\sum_{\omega\in\Omega_{k}}e^{-\delta_{i}}\frac{p_{\omega}u_{i}^{\prime}\left(f_{i}\left(C_{\omega}\right)\right)}{u_{i}^{\prime}\left(c_{i}^{2}\right)}D_{\omega}=\sum_{k=1}^{K}e^{-\delta_{i}}\frac{u_{i}^{\prime}\left(f_{i}\left(x_{k}\right)\right)}{u_{i}^{\prime}\left(c_{i}^{2}\right)}\sum_{\omega\in\Omega_{k}}p_{\omega}D_{\omega}}\ {\displaystyle}&{\displaystyle=\sum_{k=1}^{K}\frac{\psi\left(k\right)}{\mathbb{P}\left(C=x_{k}\right)}\sum_{\omega\in\Omega_{k}}p_{\omega}D_{\omega}=\sum_{k=1}^{K}\psi(k)\sum_{\omega\in\Omega_{k}}\frac{p_{\omega}}{\mathbb{P}\left(C=x_{k}\right)}D_{\omega}}\ {\displaystyle}&{\displaystyle=\sum_{k=1}^{K}\psi(k)\mathbb{E}\left[D\right]C=x_{k}],}\end{array}
$$  

where $\operatorname{E}[D | C=x_{k}]$ is the expected dividend conditional on aggregate consumption being $x_{k}$ The last equality is due to the fact that $p_{\omega}/\mathbb{P}(C=x_{k})$ is the conditional probability of the state $\omega$ given that aggregate consumption is $x_{k}$ . To price any marketed dividend we thus need only prices of Arrow-Debreu style assets on aggregate consumption and the expectation of the dividend conditional on the aggregate consumption.

The economy is said to have a representative individual if for each equilibrium in the economy with $L$ individuals there is a vector $\pmb{\eta}$ such that the equilibrium asset prices are the same in the economy with the single individual with utility $\uplambda_{\eta}$ and endowment $(\bar{e}_{0},\bar{e})$ . Theorem 7.1 has the following immediate consequence:  

Theorem 7.3 If the equilibrium consumption allocation is Pareto-optimal, the economy has a representative individual.  

Since it is much easier to analyze models with only one individual, many asset pricing models do. assume the existence of a representative individual. Of course, it is interesting to know under what. conditions this assumption is satisfied, i.e. under what conditions the equilibrium consumption. allocation in the underlying multi-individual economy is going to be Pareto-optimal. We will. study that question below. Note that in the representative individual economy there can be no trade in the financial assets (who should be the other party in the trade?) and the consumption of the representative individual must equal the total endowment. If you want to model how financial assets are traded, a representative individual formulation is obviously not useful, but if you just want to study equilibrium asset prices it is often convenient..

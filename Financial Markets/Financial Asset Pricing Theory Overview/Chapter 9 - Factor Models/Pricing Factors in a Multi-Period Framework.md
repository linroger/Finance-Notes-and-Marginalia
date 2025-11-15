---
tags:
- apt
- artificial-intelligence
- banking
- beta
- conditional_pricing
- defi
- factor-models
- ma
- mpt
- multi_period_framework
- option-greeks
- pricing_factor
- risk-management
- state_price_deflator
- stochastic
- unconditional_pricing
- value-at-risk
- var
aliases:
- Multi-period Pricing
- Pricing Factors
key_concepts:
- Agricultural futures and seasonality
- Alternative investments and hedge fund strategies
- Arbitrage Pricing Theory (APT) and factor models
- Arbitrage pricing theory (APT)
- Asset swaps and spread-lock strategies
- Bank asset-liability management (ALM) strategies
- Bank capital adequacy and Basel III compliance
- Bank stress testing and CCAR requirements
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
- Capital Asset Pricing Model (CAPM)
- Capital Asset Pricing Model (CAPM) and beta estimation
- Central bank digital currencies (CBDCs)
- Central clearing and CCP risk management
- Commodity futures and convenience yields
- Commodity swaps and energy derivatives
- Conditional factor beta
- Constant maturity swaps and roll-over features
- Continuous-time model
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
- Liquidity coverage ratio and funding strategies
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
- Net interest margin and banking profitability
- Netting agreements and close-out procedures
- Non-deliverable forwards and emerging market instruments
- OIS discounting and collateralized interest rate derivatives
- Option Greeks and sensitivity analysis
- Options on futures and forward-starting options
- Payment systems and settlement risk
- Pricing factor definition
- Prime brokerage and securities lending
- Private credit and direct lending
- Project finance and syndicated lending
- Real estate investment trusts (REITs)
- Recovery rate modeling and loss given default
- Repo markets and securities lending
- Risk factor decomposition and sensitivity analysis
- Risk parity and risk budgeting strategies
- Risk-neutral valuation and martingale measures
- Shadow banking and non-bank intermediation
- Smart beta and alternative indexing approaches
- State-price deflator relationship
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
- Unconditional pricing factor
- VIX futures and volatility trading
- Value at Risk (VaR) and expected shortfall methodologies
- Value at Risk (VaR) and risk metrics
- Value vs growth investing frameworks
- Vasicek and CIR interest rate models
- Volatility smile and skew patterns in option markets
- Weighted average cost of capital (WACC) calculations
- Working capital and cash conversion cycle
- Wrong-way risk and correlation adjustments
- Zero-coupon bond pricing and bootstrapping
enhanced: true
enhancement_date: '2025-11-06'
enhancement_id: batch04-741156
---




# 9.5 Pricing factors in a multi-period framework  

In the one-period framework we defined a pricing factor to be a $K$ -dimensional random variable $_{\alpha}$ such that there exists some $\alpha\in\mathbb R$ and some $\eta\in\mathbb{R}^{K}$ so that  
$$
\begin{array}{r}{\operatorname{E}[R_{i}]=\alpha+\beta[R_{i},\pmb{x}]^{\top}\pmb{\eta},\quad i=1,\ldots,I,}\end{array}
$$  

where $\beta[R_{i},{\pmb x}]=(\mathrm{Var}[{\pmb x}])^{-1}\mathrm{Cov}[{\pmb x},R_{i}]$ . We saw that any state-price deflator works as a pricing factor and, more generally, if $\zeta=a+b^{\top}x$ is a state-price deflator for constants $a,b$ then $_{x c}$ is a pricing factor. On the other hand, given any pricing factor $_{x c}$ , we can find constants $a,b$ such that $\zeta=a+b^{\top}x$ is a candidate state-price defator (not necessarily strictly positive, alas).  

In a multi-period discrete-time framework we will say that a $K$ -dimensional adapted stochastic process ${\pmb x}=({\pmb x}_{t})$ is a conditional pricing factor, if there exist adapted stochastic processes $\alpha=\left(\alpha_{t}\right)$ and $\eta=\left(\eta_{t}\right)$ so that  
$$
\begin{array}{r}{\mathrm{E}_{t}[R_{i,t+1}]=\alpha_{t}+\beta_{t}[R_{i,t+1},\boldsymbol{x}_{t+1}]^{\top}\boldsymbol{\eta}_{t},\quad i=1,\dots,I,}\end{array}
$$  

for any $t=0,1,2,\ldots,T-1$ . Here, the conditional factor beta is defined as  
$$
\beta_{t}[R_{i,t+1},\pmb{x}_{t+1}]=(\mathrm{Var}_{t}[\pmb{x}_{t+1}])^{-1}\mathrm{Cov}_{t}[\pmb{x}_{t+1},R_{i,t+1}].
$$  

If a conditionally risk-free asset exists, then $\alpha_{t}=R_{t}^{f}$ implying that  
$$
\begin{array}{r}{\mathrm{E}_{t}[R_{i,t+1}]=R_{t}^{f}+\beta_{t}[R_{i,t+1},\boldsymbol{x}_{t+1}]^{\top}\eta_{t},\quad i=1,\dots,I.}\end{array}
$$  

Suppose $_{x c}$ is a conditional pricing factor, and let $a=\left(a_{t}\right)$ be an adapted one-dimensional process and $\underline{{\underline{{A}}}}=(\underline{{\underline{{A}}}}_{t})$ be an adapted process whose values. $\underline{{\underline{{A}}}}_{t}$ are non-singular $K\times K$ matrices. Then. $\hat{\pmb x}$ defined by  
$$
\hat{\mathbf{x}}_{t+1}=a_{t}+\underline{{\underline{{A}}}}_{t}\mathbf{x}_{t+1}
$$  

will also be a conditional pricing factor.  

If $\zeta~=~\left(\zeta_{t}\right)$ is a state-price deflator process, the one-period analysis implies that the ratios. $\zeta_{t+1}/\zeta_{t}$ define a conditional pricing factor. Since $\zeta_{t+1}=0+\zeta_{t}(\zeta_{t+1}/\zeta_{t})$ is a transformation of the form (9.36), we see that any state-price deflator is a conditional pricing factor. As in the one-period case, we will have that if $\zeta_{t+1}=a_{t}+b_{t}^{\top}x_{t+1}$ is a state-price deflator for some adapted process. $_{\alpha}$ , then $_{x c}$ is a conditional pricing factor. And for any conditional pricing factor. $_{x c}$ , we can find adapted process $a=\left(a_{t}\right)$ and $\pmb{b}=(\pmb{b}_{t})$ so that $\zeta_{t+1}=a_{t}+b_{t}^{\top}x_{t+1}$ defines a candidate state-price deflator (not necessarily positive, however).  

We will say that a $K$ -dimensional adapted stochastic process $\pmb{x}=(\pmb{x}_{t})$ is an unconditional pricing factor, if there exist constants $\alpha$ and $\pmb{\eta}$ so that  
$$
\begin{array}{r}{\mathrm{E}[R_{i,t+1}]=\alpha+\beta[R_{i,t+1},\mathbf{\boldsymbol{x}}_{t+1}]^{\top}\pmb{\eta},\quad i=1,\dots,I,}\end{array}
$$  

for any $t=0,1,2,\ldots,T-1$ . Here, the unconditional factor beta is defined as  
$$
\beta[R_{i,t+1},\pmb{x}_{t+1}]=(\mathrm{Var}[\pmb{x}_{t+1}])^{-1}\mathrm{Cov}[\pmb{x}_{t+1},R_{i,t+1}].
$$  

This is true if the state-price deflator can be written as $\begin{array}{r}{\frac{\zeta_{t+1}}{\zeta_{t}}=a+b^{\top}x_{t+1}}\end{array}$ for constants $a$ and $^{b}$ . Hence, an unconditional pricing factor is also a conditional pricing factor. The converse is not true.  

Testing factor models on actual data really requires an unconditional model since we need to replace expected returns by average returns, etc. To go from a conditional pricing factor model to an unconditional, we need to link the variation in the coefficients over time to some observable variables. Suppose for example that $\begin{array}{r}{\frac{\zeta_{t+1}}{\zeta_{t}}=a_{t}+b_{t}x_{t+1}}\end{array}$ is a state-price deflator so that $x=\left(x_{t}\right)$ is a conditional pricing factor, assumed to be one-dimensional for notational simplicity. If we can. write  
$$
a_{t}=A_{0}+A_{1}y_{t},\quad b_{t}=B_{0}+B_{1}y_{t}
$$  

for some observable adapted process $y=\left(y_{t}\right)$ , then  
$$
\frac{\zeta_{t+1}}{\zeta_{t}}=A_{0}+A_{1}y_{t}+B_{0}x_{t+1}+B_{1}y_{t}x_{t+1}
$$  

which defines a 3-dimensional unconditional pricing factor given by the vector $(y_{t},x_{t+1},y_{t}x_{t+1})^{\top}$  

Now let us turn to the continuous-time setting. By a $K$ -dimensional conditional pricing factor in a continuous-time model we mean an adapted $K$ -dimensional process $\pmb{x}=(\pmb{x}_{t})$ with the property that there exist some one-dimensional adapted process $\alpha=\left(\alpha_{t}\right)$ and some $K$ -dimensional adapted process $\eta=\left(\eta_{t}\right)$ such that for any asset $i$ (or trading strategy), the expected rate of return per time period satisfies  
$$
\mu_{i t}+\delta_{i t}=\alpha_{t}+(\beta_{t}^{i x})^{\top}\eta_{t},
$$  

where again $\beta_{t}^{i x}$ is the factor-beta of asset $i$ at time $t$ . To understand the factor-beta write the price dynamics of risky assets in the usual form  
$$
d P_{i t}=P_{i t}\left[\mu_{i t}d t+\sigma_{i t}^{\top}d z_{t}\right].
$$  

and the dynamics of $_{\mathbf{\nabla}}\mathbf{\phi}_{\mathbf{\phi}}$ as  
$$
d\mathbf{x}_{t}=\mu_{x t}d t+\underline{{\underline{{\sigma}}}}_{x t}d z_{t},
$$  

where $\pmb{\mu}_{x}$ is an adapted process valued in $\mathbb{R}^{K}$ and $\underline{{\underline{{O}}}}.x$ is an adapted process with values being $K\times d$ matrices. Then the factor-beta is defined as  
$$
\beta_{t}^{i x}=\left(\underline{{\underline{{\sigma}}}}_{x t}\underline{{\underline{{\sigma}}}}_{x t}^{\top}\right)^{-1}\underline{{\underline{{\sigma}}}}_{x t}\pm\pmb{\sigma}_{i t}.
$$  

If a "bank account' is traded, it then follows that $\alpha_{t}=r_{t}^{f}$ . In the following we will assume that this is the case.  

Factors are closely linked to market prices of risk and hence to risk-neutral measures and stateprice deflators.If $\pmb{x}=(\pmb{x}_{t})$ is a factor in an expected return-beta relation, then we can define a. market price of risk as (note that it is. $d$ -dimensional)  
$$
\lambda_{t}=\underline{{\sigma}}_{x t}^{\top}\left(\underline{{\underline{{\sigma}}}}{x t}\underline{{\underline{{\sigma}}}}_{x t}^{\top}\right)^{-1}\eta_{t},
$$  

since we then have  
$$
\sigma_{i t}^{\top}\lambda_{t}=\sigma_{i t}^{\top}\underline{{\sigma}}_{x t}^{\top}\left(\underline{{\underline{{\sigma}}}}_{x t}\underline{{\underline{{\sigma}}}}_{x t}^{\top}\right)^{-1}\eta_{t}=\left(\beta_{t}^{i x}\right)^{\top}\eta_{t}=\mu_{i t}+\delta_{i t}-r_{t}^{f}.
$$  

Conversely, let $\lambda=\left(\lambda_{t}\right)$ be any market price of risk and let $\zeta=\left(\zeta_{t}\right)$ be the associated state-price.   
deflator so that.  
$$
d\zeta_{t}=-\zeta_{t}\left(r_{t}^{f}d t+\lambda_{t}^{\top}d z_{t}\right).
$$  

Then we can use $\zeta$ as a one-dimensional factor in an expected return-beta relation. Since this corresponds to a factor "sensitivity" vector $-\zeta_{t}\lambda_{t}$ replacing the matrix $\underline{{\underline{{\sigma}}}}x t$ , the relevant 'beta" is  
$$
\beta_{t}^{i\zeta}=\frac{-\zeta_{t}\pm\sigma_{i t}^{\top}\lambda_{t}}{\zeta_{t}^{2}\lambda_{t}^{\top}\lambda_{t}}=-\frac{1}{\zeta_{t}}\frac{\pmb{\sigma}_{i t}^{\top}\lambda_{t}}{\lambda_{t}^{\top}\lambda_{t}}.
$$  

We can use $\eta_{t}=-\zeta_{t}\lambda_{t}^{\top}\lambda_{t}$ , since then  
$$
\beta_{t}^{i\zeta}\eta_{t}=-\frac{1}{\zeta_{t}}\frac{\sigma_{i t}^{\top}\lambda_{t}}{\lambda_{t}^{\top}\lambda_{t}}\left(-\zeta_{t}\lambda_{t}^{\top}\lambda_{t}\right)=\sigma_{i t}^{\top}\lambda_{t}=\mu_{i t}+\delta_{i t}-r_{t}^{f}
$$  

for any asset $i$ .We can even use $a_{t}+b_{t}\zeta_{t}$ as a factor for any sufficiently well-behaved adapted processes $a=\left(a_{t}\right)$ and $b=\left(b_{t}\right)$  

If we use. $\zeta^{*}$ as the factor, the relevant $\eta$ is $\eta_{t}=-\zeta_{t}^{*}\left(\lambda_{t}^{*}\right)^{\top}\lambda_{t}^{*}=-\zeta_{t}^{*}\ | \lambda_{t}^{*}\ | ^{2}$ . From (4.51), we see that $\ | \lambda_{t}^{*}\ | ^{2}$ is exactly the excess expected rate of return of the growth-optimal strategy, we which can also write as $\mu_{t}^{*}-r_{t}^{f}$ . Hence, we can write the excess expected rate of return on any asset (or. trading strategy) as
$$
\mu_{i t}+\delta_{i t}-r_{t}^{f}=\beta_{t}^{i\zeta^{*}}\left(-\zeta_{t}^{*}[\mu_{t}^{*}-r_{t}^{f}]\right)=\frac{\sigma_{i t}^{\tau}\lambda_{t}^{*}}{(\lambda_{t}^{*})^{\top}\lambda_{t}^{*}}[\mu_{t}^{*}-r_{t}^{f}]\equiv\beta_{t}^{i\lambda^{*}}[\mu_{t}^{*}-r_{t}^{f}].
$$  

Whether we want to use a discrete-time or a continuous-time model, the key question is what. factors to include in order to get prices or returns that are consistent with the data. Due to the link between state-price deflators and (marginal utility of) consumption, we should look for factors among variables that may affect (marginal utility of) consumption..

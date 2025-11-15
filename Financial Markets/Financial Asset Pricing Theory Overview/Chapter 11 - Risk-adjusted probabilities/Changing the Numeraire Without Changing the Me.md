---
tags:
- arrow_debreu_asset
- artificial-intelligence
- banking
- cdo
- collateralized-debt-obligation
- defi
- gop
- growth_optimal_portfolio
- interest-rate-swap
- irs
- ma
- numeraire
- option-greeks
- options
- risk-management
- stochastic
- tangency-portfolio
- tangency_portfolio
- value-at-risk
- var
aliases:
- Arrow-Debreu assets
- GOP strategy
- Growth-optimal trading strategy
key_concepts:
- Agricultural futures and seasonality
- Alternative investments and hedge fund strategies
- Arrow-Debreu asset definition
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
- Black-Litterman model and portfolio optimization
- Bond portfolio immunization strategies
- CDO structuring and tranche allocation methodologies
- CDO-squared structures and correlation trading
- Calendar spreads and roll strategies
- Capital Asset Pricing Model (CAPM) and beta estimation
- Central bank digital currencies (CBDCs)
- Central clearing and CCP risk management
- Changing numeraire, measure
- Commodity futures and convenience yields
- Commodity swaps and energy derivatives
- Complete markets and replication
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
- GARCH models for volatility forecasting
- GOP in multi-period setting
- Gamma trading and convexity adjustments
- Green bonds and climate risk assessment
- Growth-optimal portfolio (GOP)
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
- Maximize expected log-return
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
- Real estate investment trusts (REITs)
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
- Value at Risk (VaR) and risk metrics
- Value vs growth investing frameworks
- Vasicek and CIR interest rate models
- Volatility smile and skew patterns in option markets
- Working capital and cash conversion cycle
- Wrong-way risk and correlation adjustments
enhanced: true
enhancement_date: '2025-11-06'
enhancement_id: batch04-202168
---




# 11.6 Changing the numeraire without changing the measure  

Now consider the following question: Is there a trading strategy. $\pmb{\theta}$ for which the associated risk-. adjusted probability measure is identical to the real-world probability measure, i.e.. $\mathbb{Q}^{\theta}=\mathbb{P}$ ? The answer is affirmative. The so-called growth-optimal portfolio (or just GOP) strategy does the job. Let us first consider a one-period setting. Here, the growth-optimal portfolio is defined as the portfolio maximizing the expected log-return (or expected log-growth rate of the invested amount) among all portfolios, i.e. it solves.  
$$
\operatorname*{max}_{\pi}\operatorname{E}[\ln\left(\pi^{\top}R\right)]\quad{\mathrm{s.t.~}}\pi^{\top}\mathbf{1}=1.
$$  

The Lagrangian for this problem is $\mathcal{L}=\mathrm{E}[\ln\left(\pi^{\top}R\right)]+\nu\left(1-\pi^{\top}\mathbf{1}\right)$ , where $\nu$ is the Lagrange multiplier, with first-order condition  
$$
\operatorname{E}\left[{\frac{1}{\pi^{\top}R}}R\right]=\nu\mathbf{1}.
$$  

We cannot solve explicitly for the portfolio $\pi_{\mathrm{GOP}}$ satisfying this equation, but we can see that its gross return $R_{\mathrm{GOP}}=\pi_{\mathrm{GOP}}^{\top}R$ satisfies  
$$
\operatorname{E}\left[{\frac{1}{R_{\mathrm{GOP}}}}R\right]=\nu\mathbf{1}.
$$  

Pre-multiplying by any portfolio $\pi$ we get  
$$
\operatorname{E}\left[\frac{R^{\pi}}{R_{\mathrm{GOP}}}\right]=\nu\pi^{\top}\mathbf{1}=\nu.
$$  

In particular, with $\pi=\pi_{\mathrm{GOP}}$ , we see that.  
$$
\nu=\operatorname{E}\left[{\frac{R_{\mathrm{GOP}}}{R_{\mathrm{GOP}}}}\right]=\operatorname{E}[1]=1.
$$  

We can thus conclude that for any asset $i$ , we have  
$$
\operatorname{E}\left[{\frac{R_{i}}{R_{\mathrm{GOP}}}}\right]=1\quad\Leftrightarrow\quad P_{i}=\operatorname{E}\left[\left(R_{\mathrm{GOP}}\right)^{-1}D_{i}\right].
$$  

Note that the expectations are under the real-world probability measure.  

If the state space is finite, $\Omega=\{1,2,\dots,S\}$ , and the market is complete, it is possible to construct an Arrow-Debreu asset for any state $\omega\in\Omega$ , i.e. an asset with a dividend of 1 if state $\omega$ is realized and a zero dividend otherwise. In this case, any portfolio $\pi$ of the basic assets can be seen as a portfolio $\hat{\pi}$ of the $S$ Arrow-Debreu assets. If $\psi_{\omega}$ denotes the state price of state $\omega$ the gross return on the Arrow-Debreu asset for state $\omega$ will be a random variable $R^{\mathrm{AD(}\omega\mathrm{)}}$ , which if state $s$ is realized takes on the value  
$$
R_{s}^{\mathrm{AD}(\omega)}=\left\{\begin{array}{l l}{\frac{1}{\psi_{s}}}&{\mathrm{~if~}s=\omega,}\ {0}&{\mathrm{~otherwise.}}\end{array}\right.
$$  

Let $\pmb{R}^{\mathrm{AD}}=\left(R^{\mathrm{AD(1)}},\dots,R^{\mathrm{AD(\itS)}}\right)^{\top}$ denote the random return vector of the $S$ Arrow-Debreu assets. The gross return on a portfolio $\hat{\pi}$ of Arrow-Debreu assets will be  
$$
R_{s}^{\hat{\pi}}=\hat{\pi}^{\top}R_{s}^{\mathrm{AD}}=\frac{\hat{\pi}_{s}}{\psi_{s}},\quad s=1,2,\ldots,S.
$$  

If we use the first-order condition (11.33) for the Arrow-Debreu asset for state $\omega$ , we therefore get  
$$
1=\mathrm{E}\left[\frac{R^{\mathrm{AD}(\omega)}}{R_{\mathrm{GOP}}^{\hat{\pi}}}\right]=p_{\omega}\frac{1/\psi_{\omega}}{{\hat{\pi}}_{\omega}/\psi_{\omega}}=\frac{p_{\omega}}{{\hat{\pi}}_{\omega}},
$$  

where $p_{\omega}$ is the real-world probability of state $\omega$ . Therefore, in terms of the Arrow-Debreu assets, the GOP consists of $p_{\omega}$ units of the Arrow-Debreu asset for state $\omega$ for each $\omega=1,2,\ldots,S$  

In a multi-period setting the growth-optimal trading strategy is the trading strategy maximizing $\operatorname{E}[\ln V_{T}^{\pi}]$ among all self-financing trading strategies. Hence, it also maximizes $\operatorname{E}[\ln(V_{T}^{\pi}/V_{0}^{\pi})]$ the expected log-growth rate between time 0 and time. $T$ . For now, focus on the discrete-time. framework. Note that.  
$$
\begin{array}{r l}&{\ln\left(\frac{V_{T}^{\pi}}{V_{0}^{\pi}}\right)=\ln\left(\frac{V_{1}^{\pi}}{V_{0}^{\pi}}\frac{V_{2}^{\pi}}{V_{1}^{\pi}}\cdot\cdot\cdot\frac{V_{T}^{\pi}}{V_{T-1}^{\pi}}\right)}\ &{\qquad=\ln\left(\frac{V_{1}^{\pi}}{V_{0}^{\pi}}\right)+\ln\left(\frac{V_{2}^{\pi}}{V_{1}^{\pi}}\right)+\cdot\cdot\cdot+\ln\left(\frac{V_{T}^{\pi}}{V_{T-1}^{\pi}}\right)}\ &{\qquad=\ln R_{1}^{\pi}+\ln R_{2}^{\pi}+\cdot\cdot\cdot+\ln R_{T}^{\pi},}\end{array}
$$  

where $R_{t+1}^{\pi}=V_{t+1}^{\pi}/V_{t}^{\pi}$ is the gross return on the trading strategy between time $t$ and time $t+1$ i.e. the gross return on the portfolio $\pi_{t}$ chosen at time. $t$ . Therefore the growth-optimal trading strategy $\pi=(\pi_{t})_{t\in\mathcal{T}}$ is such that each. $\pi_{t}$ maximizes $\mathrm{E}_{t}[\ln R_{t+1}^{\pi_{t}}]=\mathrm{E}_{t}[\ln(\pi_{t}^{\top}R_{t+1})]$ , where $R_{t+1}$ is the vector of gross returns on all the basic assets between time $t$ and time $t+1$ .As in the. one-period setting, the first-order condition implies that  
$$
\mathrm{E}_{t}\left[{\frac{R_{i,t+1}}{R_{t+1}^{\pi}}}\right]=1
$$  

for all assets $i$ (and portfolios). Again, it is generally not possible to solve explicitly for the portfolio $\pi_{t}$  

In the continuous-time framework assume that a bank account is traded with instantaneous riskfree rate of return $\boldsymbol{r}_{t}^{f}$ and let $\pi_{t}$ denote the portfolio weights of the instantaneously risky assets. Then the dynamics of the value $V_{t}^{\pi}$ of a self-financing trading strategy $\pi=(\pi_{t})_{t\in[0,T]}$ is given by  
$$
d V_{t}^{\pi}=V_{t}^{\pi}\left[\left(r_{t}^{f}+\pi_{t}^{\top}[\mu_{t}+\delta_{t}-r_{t}^{f}{\bf1}]\right)d t+\pi_{t}^{\top}\underline{{\sigma}}_{t}d z_{t}\right],
$$  

cf. Sections 3.3.3 and 6.5.2. This implies that  
$$
V_{T}^{\pi}=V_{0}^{\pi}\exp\left\{\int_{0}^{T}\left(r_{t}^{f}+\pi_{t}^{\top}[\mu_{t}+\delta_{t}-r_{t}^{f}\mathbf{1}]-\frac{1}{2}\pi_{t}^{\top}\underline{{\sigma}}_{t}\underline{{\sigma}}_{t}^{\top}\pi_{t}\right)d t+\int_{0}^{T}\pi_{t}^{\top}\underline{{\sigma}}_{t}d z_{t}\right\},
$$  

and thus  
$$
\ln\left(\frac{V_{T}^{\pi}}{V_{0}^{\pi}}\right)=\int_{0}^{T}\left(r_{t}^{f}+\pi_{t}^{\top}[\mu_{t}+\delta_{t}-r_{t}^{f}\mathbf{1}]-\frac{1}{2}\pi_{t}^{\top}\underline{{\sigma}}_{t}\underline{{\sigma}}_{t}^{\top}\pi_{t}\right)d t+\int_{0}^{T}\pi_{t}^{\top}\underline{{\sigma}}_{t}d z_{t}.
$$  

If the process $\pi_{t}^{\top}\underline{{\sigma}}_{t}$ is sufficiently nice, the stochastic integral in the above equation will have mean zero so that the growth-optimal trading strategy is maximizing the expectation of the first integral, which can be found by maximizing. $\begin{array}{r}{\pi_{t}^{\top}[\mu_{t}+\delta_{t}-r_{t}^{f}\mathbf{1}]-\frac{1}{2}\pi_{t}^{\top}\underline{{\sigma}}_{t}\underline{{\sigma}}_{t}^{\top}\pi_{t}}\end{array}$ for each $t$ and each state. The first-order condition implies that.  
$$
\underline{{\underline{{\sigma}}}}t\underline{{\underline{{\sigma}}}}_{t}^{\top}\pmb{\pi}_{t}=\pmb{\mu}_{t}+\delta_{t}-r_{t}^{f}\pmb{1},
$$  

which means that  
$$
\underline{{\underline{{\sigma}}}}_{t}^{\top}\pi_{t}=\lambda_{t}
$$  

for some market price of risk process $\lambda=\left(\lambda_{t}\right)$ . If $\underline{{\underline{{\sigma}}}}t$ is a square, non-singular matrix, the unique GOP strategy is given by  
$$
\pi_{t}=\left(\underline{{\underline{{\sigma}}}}_{t}^{\top}\right)^{-1}\lambda_{t}=\left(\underline{{\underline{{\sigma}}}}t\underline{{\underline{{\sigma}}}}_{t}^{\top}\right)^{-1}\left(\mu_{t}+\delta_{t}-r_{t}^{f}\mathbf{1}\right).
$$  

This shows that the GOP strategy is a combination of the instantaneously risk-free asset and the tangency portfolio of risky assets, introduced in Section 6.5.2. The GOP strategy is the optimal trading strategy for an individual with time-additive logarithmic utility. Substituting the expression for $\pi_{t}$ back into the value dynamics, we see that the value of the GOP strategy evolves as  
$$
d V_{t}^{\pi}=V_{t}^{\pi}\left[\left(r_{t}^{f}+\ | \lambda_{t}\ | ^{2}\right)d t+\lambda_{t}^{\top}d z_{t}\right].
$$  

The value process of the GOP strategy (and the real-world probability measure) contain sufficient information to price any specific dividend process. Since knowing the value process of the GOP strategy boils down to knowing the risk-free rate process and the market price of risk process, this is not a surprise. Also note that $\zeta_{t}=V_{0}^{\pi}/V_{t}^{\pi}$ defines a state-price deflator.

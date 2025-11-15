---
tags:
- abs
- apt
- arbitrage
- artificial-intelligence
- asset_allocation
- cdo
- collateralized-debt-obligation
- defi
- discrete_time
- interest-rate-swap
- irs
- ito-calculus
- ma
- option-greeks
- options
- portfolio_management
- risk-management
- self_financing
- stochastic
- trading_strategies
- transaction-costs
- value-at-risk
- var
aliases:
- One-Period Model
- Portfolio
- Trading Strategy
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
- Delta hedging and Greeks calculation
- Delta hedging strategies in options markets
- Deposit insurance and systemic risk
- Discounted cash flow (DCF) valuation methodologies
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
- Gross rate of return
- HJM and forward rate model frameworks
- High frequency trading and algorithmic strategies
- Historical simulation and parametric VaR approaches
- Hull-White and Black-Karasinski short rate models
- IPO pricing and underpricing analysis
- Implied volatility and volatility surface modeling
- Inflation-linked swaps and CPI adjustments
- Interest rate derivatives and forward rate agreements
- Interest rate swaps and swap spread decomposition
- Ito's Lemma and stochastic calculus
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
- Portfolio weight vector
- 'Portfolio: asset holdings'
- Prime brokerage and securities lending
- Private credit and direct lending
- Project finance and syndicated lending
- Real estate investment trusts (REITs)
- Recovery rate modeling and loss given default
- Repo markets and securities lending
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
- Trading strategy definition
- Treasury futures and bond basis
- Treasury securities and government bond markets
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
enhancement_id: batch04-427012
---




# 3.3 Portfolios and trading strategies  

Individuals can trade assets at all time points of the model, except for the last date. The combination of holdings of different assets at a given point in time is called a portfolio. We assume that there are no restrictions on the portfolios that investors may form and that there are no trading costS.  

# 3.3.1 The one-period framework  

In a one-period model an individual chooses a portfolio. $\pmb\theta=(\theta_{1},\dots,\theta_{I})^{\top}$ at time $0$ with $\theta_{i}$ being the number of units held of asset. $i$ . It is not possible to rebalance the portfolio but the individual simply cashes in the dividends at time 1. Let. $D^{\theta}$ be the random variable that represents the. dividend of the portfolio $\pmb{\theta}$ . If state $\omega$ is realized, the total dividend from a portfolio. $\pmb{\theta}$ is  
$$
D^{\theta}(\omega)=\sum_{i=1}^{I}\theta_{i}D_{i}(\omega)=\theta\cdot D(\omega),
$$  

i.e. $D^{\theta}=\pmb\theta\cdot\pmb D$  

Denote the price or value of a portfolio $\pmb{\theta}$ by $P^{\theta}$ .We will throughout this book assume that prices are linear so that  
$$
P^{\theta}=\sum_{i=1}^{I}\theta_{i}P_{i}=\theta\cdot P.
$$  

This is called the Law of One Price. Since we ignore transaction costs, any candidate for an. equilibrium pricing system will certainly have this property. In Section 3.4 we will discuss the link between the Law of One Price and the absence of arbitrage..  

The fraction of the total portfolio value invested in asset $i$ is then $\pi_{i}=\theta_{i}P_{i}/P^{\theta}$ and the vector $\pi=\left(\pi_{1},\ldots,\pi_{I}\right)^{\top}$ is called the portfolio weight vector. If we let $\mathbf{1}=\left(1,\ldots,1\right)^{\top}$ , we have ${\boldsymbol{\pi}}\cdot\mathbf{1}=$ $\textstyle\sum_{i=1}^{I}\pi_{i}=1$ . Note that $\mathrm{diag}(P)\mathbf{1}=P $ and thus $P^{\theta}=P^{\top}\pmb{\theta}=(\mathrm{diag}(P)\mathbf{1})^{\top}\pmb{\theta}=\mathbf{1}^{\top}\mathrm{diag}(P)\pmb{\theta}$ so that  
$$
\pi={\frac{\operatorname{diag}(P)\theta}{P^{\top}\theta}}={\frac{\operatorname{diag}(P)\theta}{{\bf1^{\top}}\operatorname{diag}(P)\theta}}.
$$  

Given $\pmb{\theta}$ and the price vector $_{P}$ we can derive $\pi$ . Conversely, given $\pi$ , the total portfolio value $P^{\theta}$ and the price vector $_{P}$ , we can derive $\pmb{\theta}$ . We therefore have two equivalent ways of representing a portfolio.  

The gross rate of return on a portfolio $\pmb{\theta}$ is the random variable  
$$
R^{\theta}={\frac{D^{\theta}}{P^{\theta}}}={\frac{\sum_{i=1}^{I}\theta_{i}D_{i}}{P^{\theta}}}={\frac{\sum_{i=1}^{I}\theta_{i}P_{i}R_{i}}{P^{\theta}}}=\sum_{i=1}^{I}{\frac{\theta_{i}P_{i}}{P^{\theta}}}R_{i}=\sum_{i=1}^{I}\pi_{i}R_{i}=\pi\cdot R,
$$  

where $\pi_{i}$ is the portfolio weight of asset i. We observe that the gross return on a portfolio is just a weighted average of the gross rates of return on the assets in the portfolio. Similarly for the net rate of return since $\textstyle\sum_{i=1}^{I}\pi_{i}=1$ and thus  
$$
r^{\theta}=R^{\theta}-1=\left(\sum_{i=1}^{I}\pi_{i}R_{i}\right)-1=\sum_{i=1}^{I}\pi_{i}\left(R_{i}-1\right)=\sum_{i=1}^{I}\pi_{i}r_{i}=\pi\cdot r,
$$  

where $\pmb{r}=(r_{1},\dots,r_{I})^{\top}$ is the vector of net rates of return on the basic assets.  

# 3.3.2 The discrete-time framework  

In a multi-period model individuals are allowed to rebalance their portfolio at any date considered in the model. A trading strategy is an. $I$ dimensional adapted stochastic process ${\pmb\theta}=({\pmb\theta}_{t})_{t\in\mathcal{T}}$ where $\pmb\theta_{t}=(\theta_{1t},\dots,\theta_{I t})^{\top}$ denotes the portfolio held at time. $t$ or rather immediately after trading at time $t$ $\theta_{i t}$ is the number of units of asset. $i$ held at time $t$  

A trading strategy $\pmb{\theta}$ generates a dividend process. $D^{\theta}$ . Immediately before time. $t$ the portfolio is given by $\pmb{\theta}_{t-1}$ so the investor will receive dividends $\pmb{\theta}_{t-1}\cdot\pmb{D}_{t}$ at time $t$ , and then rebalance the. portfolio to $\pmb{\theta}_{t}$ immediately after time $t$ . The net gain or dividend at time $t$ is therefore equal to  
$$
D_{t}^{\theta}=\theta_{t-1}\cdot D_{t}-\left(\theta_{t}-\theta_{t-1}\right)\cdot P_{t}=\theta_{t-1}\cdot\left(P_{t}+D_{t}\right)-\theta_{t}\cdot P_{t},\quad t=1,2,\ldots,T-1.
$$  

We can think of this as a budget constraint saying that the sum of the withdrawn dividend and our additional investment $(\pmb{\theta}_{t}-\pmb{\theta}_{t-1})\cdot\pmb{P}_{t}$ has to equal the dividends we receive from the current portfolio. The terminal dividend is  
$$
D_{T}^{\theta}=\theta_{T-1}\cdot D_{T}.
$$  

Given the Law of One Price, the initial price of the trading strategy is $P^{\pmb{\theta}}={\pmb{\theta}}_{0}\cdot{\pmb{P}}_{0}$ . We can let $D_{0}^{\theta}=-P^{\theta}$ so that the dividend process $D^{\theta}$ is defined at all $t\in\mathcal{T}$  

For $t=1,\ldots,T$ define  
$$
V_{t}^{\pmb\theta}=\pmb\theta_{t-1}\cdot(\pmb P_{t}+\pmb D_{t})
$$  

which is the time $t$ value of the portfolio chosen at the previous trading date. This is the value of the portfolio just after dividends are received at time. $t$ and before the portfolio is rebalanced. Define. $V_{0}^{\pmb\theta}={\pmb\theta}_{0}\cdot{\pmb P}_{0}$ . We call $V^{\theta}=(V_{t}^{\theta})_{t\in\mathcal{T}}$ the value process of the trading strategye $\pmb{\theta}$ . According to (3.8), we have $V_{t}^{\pmb\theta}=D_{t}^{\pmb\theta}+{\pmb\theta}_{t}\cdot{\pmb P}_{t}$ for $t=1,\ldots,T$ and, in particular, $V_{T}^{\theta}=D_{T}^{\theta}$ . The change in the value of the trading strategy between two adjacent dates is.  
$$
\begin{array}{r l}&{V_{t+1}^{\theta}-V_{t}^{\theta}=\theta_{t}\cdot(P_{t+1}+D_{t+1})-\theta_{t-1}\cdot(P_{t}+D_{t})}\ &{\qquad=\theta_{t}\cdot(P_{t+1}+D_{t+1})-D_{t}^{\theta}-\theta_{t}\cdot P_{t}}\ &{\qquad=\theta_{t}\cdot(P_{t+1}-P_{t}+D_{t+1})-D_{t}^{\theta}.}\end{array}
$$  

The first term on the right-hand side of the last expression is the net return on the portfolio $\pmb{\theta}_{t}$ from time $t$ to $t+1$ , the latter term is the net dividend we have withdrawn at time $t$  

The trading strategy is said to be self-financing if all the intermediate dividends are zero, i.e. $D_{t}^{\theta}=0$ for $t=1,\dots,T-1$ . Using (3.8) this means that  
$$
\left(\pmb{\theta}_{t}-\pmb{\theta}_{t-1}\right)\cdot\pmb{P}_{t}=\pmb{\theta}_{t-1}\cdot\pmb{D}_{t},\quad t=1,\dots,T-1.
$$  

The left-hand side is the extra investment due to the rebalancing at time $t$ , the right-hand side is the dividend received at time $t$ . A self-financing trading strategy requires an initial investment of $P^{\pmb{\theta}}={\pmb{\theta}}_{0}\cdot{\pmb{P}}_{0}$ and generates a terminal dividend of $D_{T}^{\theta}=\pmb{\theta}_{T-1}\cdot\pmb{D}_{T}$ . At the intermediate dates no money is invested or withdrawn so increasing the investment in some assets must be fully financed by dividends or selling off other assets. If $\pmb{\theta}$ is self-financing, we have $V_{t}^{\pmb\theta}=P_{t}^{\pmb\theta}\equiv\pmb\theta_{t}\cdot\pmb P_{t}$ , the time. $t$ price of the portfolio $\pmb{\theta}_{t}$ , for $t=0,1,\ldots,T-1$ . Moreover, the change in the value of the trading strategy is just the net return, cf. (3.10).  

Portfolio weights...   
Returns...  

# 3.3.3 The continuous-time framework  

Also in the continuous-time framework with. $\mathcal{T}=[0,T]$ a trading strategy is an $I$ -dimensional adapted stochastic process ${\pmb\theta}=({\pmb\theta}_{t})_{t\in\mathcal{T}}$ where $\pmb\theta_{t}=(\theta_{1t},\dots,\theta_{I t})^{\top}$ denotes the portfolio held at. time $t$ or rather immediately after trading at time $t$  

Consistent with the discrete-time framework we define the value of the trading strategy $\pmb{\theta}$ at any given time $t$ as the price of the portfolio just chosen at that time plus any lump-sum dividends received at that time. Since we only allow for lump-sum dividends at the terminal date, we define  
$$
V_{t}^{\pmb\theta}=\pmb\theta_{t}\cdot\pmb P_{t},\quad t<T
$$  

and $V_{T}^{\theta}=\theta_{T}{\cdot}D_{T}\equiv D_{T}^{\theta}$ , the terminal lump-sum dividend. The time $0$ value is the cost of initiating. the trading strategy, which we can think of as a negative initial dividend,. $D_{0}^{\theta}=-V_{0}^{\theta}=\theta_{0}\cdot P_{0}$ We assume that between time 0 and time. $T$ no lump-sum dividends can be withdrawn from. the investment but funds can be withdrawn at a continuous rate as represented by the process. $\boldsymbol{\alpha}^{\theta}=(\alpha_{t}^{\theta})$ describing the rate with which we withdraw funds from our investments. Intermediate. lump-sum withdrawals could be allowed at the expense of additional notational complexity. For later use note that an application of Ito's Lemma implies that the increment to the value process is given by.  
$$
d V_{t}^{\theta}=\theta_{t}\cdot d P_{t}+d\theta_{t}\cdot P_{t}+d\theta_{t}\cdot d P_{t}.
$$  

Assume for a moment that we do not change our portfolio over a small time interval $[t,t+\Delta t]$ The total funds withdrawn over this interval is. $\alpha_{t}^{\pmb\theta}\Delta t$ . Let $\Delta\theta_{t+\Delta t}=\theta_{t+\Delta t}-\theta_{t}$ and $\Delta P_{t+\Delta t}=$ $P_{t+\Delta{t}}-P_{t}$ . The total dividends received from the portfolio. $\pmb{\theta}_{t}$ over the interval is $\textstyle\sum_{i=1}^{I}\theta_{i t}\delta_{i t}P_{i t}\Delta t$ which we can rewrite as. ${\pmb\theta}_{t}^{\scriptscriptstyle\prime}\mathrm{diag}({\pmb P}_{t})\delta_{t}\Delta t$ , where $\operatorname{diag}(P_{t})$ is the matrix defined in (3.1). Then the. budget constraint over this interval is.  
$$
\alpha_{t}^{\theta}\Delta t+\Delta\pmb{\theta}_{t+\Delta t}\cdot\pmb{P}_{t+\Delta t}=\pmb{\theta}_{t}^{\top}\mathrm{diag}(\pmb{P}_{t})\pmb{\delta}_{t}\Delta t.
$$  

The left-hand side is the sum of the funds we withdraw and the net extra investment. The right hand side is the funds we receive in dividends. Let us add and subtract $(\Delta\pmb{\theta}_{t+\Delta t})\cdot\pmb{P}_{t}$ in the above equation. Rearranging we obtain  
$$
\alpha_{t}^{\theta}\Delta t+\Delta\theta_{t+\Delta t}\cdot\Delta P_{t+\Delta t}+\Delta\theta_{t+\Delta t}\cdot P_{t}=\theta_{t}^{\top}\operatorname{diag}(P_{t})\delta_{t}\Delta t.
$$  

The equivalent equation for an infinitesimal interval $[t,t+d t]$ is  
$$
\alpha_{t}^{\theta}d t+d\pmb{\theta}_{t}\cdot d\pmb{P}_{t}+d\pmb{\theta}_{t}\cdot\pmb{P}_{t}=\pmb{\theta}_{t}^{\top}\operatorname{diag}(\pmb{P}_{t})\delta_{t}d t.
$$  

Using this, we can rewrite the value dynamics in (3.12) as  
$$
d V_{t}^{\theta}=\theta_{t}\cdot d P_{t}+\theta_{t}^{\top}\operatorname{diag}(P_{t})\delta_{t}d t-\alpha_{t}^{\theta}d t.
$$  

Substituting in (3.5), this implies that  
$$
d V_{t}^{\theta}=\theta_{t}^{\top}\operatorname{diag}(P_{t})\left[\left(\mu_{t}+\delta_{t}\right)d t+\underline{{\underline{{\sigma}}}}_{t}d z_{t}\right]-\alpha_{t}^{\theta}d t.
$$  

As discussed earlier we can define a portfolio weight vector  
$$
\pi_{t}={\frac{\operatorname{diag}(P_{t})\pmb{\theta}_{t}}{P_{t}^{\top}\pmb{\theta}_{t}}}={\frac{\operatorname{diag}(P_{t})\pmb{\theta}_{t}}{V_{t}^{\theta}}}.
$$  

The value dynamics can therefore be rewritten as  
$$
d V_{t}^{\theta}=V_{t}^{\theta}\pi_{t}^{\top}\left[\left(\mu_{t}+\delta_{t}\right)d t+\underline{{\sigma}}_{t}d z_{t}\right]-\alpha_{t}^{\theta}d t.
$$  

A trading strategy is called self-financing if no funds are withdrawn, i.e. $\alpha_{t}^{\pmb\theta}\equiv0$ . In that case the value dynamics is simply  
$$
d V_{t}^{\theta}=\theta_{t}^{\top}\operatorname{diag}(P_{t})\left[\left(\mu_{t}+\delta_{t}\right)d t+\underline{{\sigma}}_{t}d z_{t}\right].
$$  

This really means that for any $t\in(0,T)$  
$$
\begin{array}{l}{{\displaystyle V_{t}^{\theta}=\theta_{0}\cdot P_{0}+\int_{0}^{t}\theta_{s}^{\top}\mathrm{diag}(P_{s})\left[\left(\mu_{s}+\delta_{s}\right)d s+\underline{{{\sigma}}}_{s}d z_{s}\right]}}\ {{\displaystyle~=\theta_{0}\cdot P_{0}+\int_{0}^{t}\theta_{s}^{\top}\mathrm{diag}(P_{s})\left(\mu_{s}+\delta_{s}\right)d s+\int_{0}^{t}\theta_{s}^{\top}\mathrm{diag}(P_{s})\underline{{{\sigma}}}_{s}d z_{s}.}}\end{array}
$$  

Returns...

---
tags:
- '#asset_pricing'
- '#asset_returns'
- '#brownian_motion'
- '#geometric_brownian_motion'
- '#law_of_iterated_expectations'
- '#ordinary_differential_equation'
- '#return_variance'
- '#stochastic_process'
- '#two_period_economy'
- apt
- defi
- derivatives-pricing
- ma
- risk-management
- stochastic
- value-at-risk
- var
key_concepts:
- Agricultural futures and seasonality
- Alternative investments and hedge fund strategies
- Arbitrage pricing theory (APT)
- Asset swaps and spread-lock strategies
- Barrier options and knock-in/knock-out structures
- Basis swaps and cross-currency basis adjustments
- Basis swaps and floating rate correlations
- Behavioral finance and market anomalies
- Best execution and regulatory requirements
- Bid-ask spreads and market making profitability
- Black-Litterman model and portfolio optimization
- Brownian motion and Wiener processes
- CDO structuring and tranche allocation methodologies
- CDO-squared structures and correlation trading
- Calendar spreads and roll strategies
- Capital Asset Pricing Model (CAPM) and beta estimation
- Central clearing and CCP risk management
- Commodity futures and convenience yields
- Commodity swaps and energy derivatives
- Constant maturity swaps and roll-over features
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
- Interest rate swaps and swap spread decomposition
- Key rate duration and curve risk decomposition
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
enhancement_id: batch04-971197
---



# 2.8 Exercises  

EXERCISE 2.1 In the two-period economy illustrated in Figures 2.1 and 2.2 consider an asset paying a dividend at time 2 given by  
$$
D_{2}=\left\{\begin{array}{l l}{{0,}}&{{\mathrm{for}\omega=3,}}\ {{5,}}&{{\mathrm{for}\omega\in\{1,2,4\},}}\ {{10,}}&{{\mathrm{for}\omega\in\{5,6\}.}}\end{array}\right.
$$  

(a) What is the expectation at time $0$ Of $D_{2}$ ? What is the expectation at time $^{1}$ of $D_{2}$ ? Verify that the Law of Iterated Expectations holds for these expectations.  

(b) What is the variance at time $0$ of $D_{2}$ ? What is the variance at time 1 of $D_{2}$ ? Confirm that $\mathrm{Var}[D_{2}]=\mathrm{E}\left[\mathrm{Var}_{1}[D_{2}]\right]+\mathrm{Var}\left[\mathrm{E}_{1}[D_{2}]\right]$  

EXERCISE 2.2Let $X=\left(X_{t}\right)$ and $Y=\left(Y_{t}\right)$ be the price processes of two assets with no intermediate dividends and assume that  
$$
\begin{array}{r}{d X_{t}=X_{t}\left[0.05d t+0.1d z_{1t}+0.2d z_{2t}\right],}\ {d Y_{t}=Y_{t}\left[0.07d t+0.3d z_{1t}-0.1d z_{2t}\right].}\end{array}
$$  

(a) What is the expected rate of return of each of the two assets?  

(b) What is the return variance and volatility of each of the two assets?  

(c) What is the covariance and the correlation between the returns on the two assets?  

EXERCISE 2.3 Suppose $X=\left(X_{t}\right)$ is a geometric Brownian motion, $d X_{t}=\mu X_{t}d t+\sigma X_{t}d z_{t}$ What is the dynamics of the process $y=\left(y_{t}\right)$ defined by $y_{t}=(X_{t})^{n}$ ? What can you say about the. distribution of future values of the $y$ process?  

EXERCISE 2.4 Suppose that the continuous-time stochastic process%20Process.md) $X=\left(X_{t}\right)$ is defined as  
$$
X_{t}=\frac{1}{2}\int_{0}^{t}\lambda_{s}^{2}d s+\int_{0}^{t}\lambda_{s}d z_{s},
$$  

where $z~=~\left(z_{t}\right)$ is a one-dimensional standard Brownian motion and $\lambda\:=\:(\lambda_{t})$ is some "nice" stochastic process%20Process.md).  

(a) Argue that $\begin{array}{r}{d X_{t}=\frac{1}{2}\lambda_{t}^{2}d t+\lambda_{t}d z_{t}}\end{array}$   
(b) Suppose that the continuous-time stochastic process%20Process.md) $\xi=\left(\xi_{t}\right)$ is defined as $\xi_{t}=\exp\{-X_{t}\}$ Show that $d\xi_{t}=-\lambda_{t}\xi_{t}d z_{t}$  

EXERCISE 2.5 (Adapted from Bjork (2004).) Define the process $y=\left(y_{t}\right)$ by $y_{t}=z_{t}^{4}$ , where $z=\left(z_{t}\right)$ is a standard Brownian motion. Find the dynamics of $y$ . Show that  
$$
y_{t}=6\int_{0}^{t}z_{s}^{2}d s+4\int_{0}^{t}z_{s}^{3}d z_{s}.
$$  

Show that $\operatorname{E}[y_{t}]\equiv\operatorname{E}[z_{t}^{4}]=3t^{2}$  

EXERCISE 2.6 (Adapted from Bjork (2004).) Define the process $y=\left(y_{t}\right)$ by $y_{t}=e^{a z_{t}}$ , where $a$ is a constant and $z=\left(z_{t}\right)$ is a standard Brownian motion. Find the dynamics of $y$ . Show that  
$$
y_{t}=1+\frac{1}{2}a^{2}\int_{0}^{t}y_{s}d s+a\int_{0}^{t}y_{s}d z_{s}.
$$  

Define $m(t)=\operatorname{E}[y_{t}]$ . Show that. $m$ satisfies the ordinary differential equation  
$$
m^{\prime}(t)={\frac{1}{2}}a^{2}m(t),\quad m(0)=1.
$$  

Show that $m(t)=e^{a^{2}t/2}$ and conclude that  
$$
\begin{array}{r}{\mathrm{E}\left[e^{a z_{t}}\right]=e^{a^{2}t/2}.}\end{array}
$$

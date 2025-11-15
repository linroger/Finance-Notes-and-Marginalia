---
tags:
- apt
- artificial-intelligence
- banking
- defi
- dva
- fixed-income
- fx-derivatives
- interest-rate-derivatives
- interest-rate-swap
- irs
- ito-calculus
- ma
- markets
- mpt
- nominal_dividends
- nominal_prices
- option-greeks
- options
- options-pricing
- real_dividends
- real_prices
- risk-management
- state_price_deflator
- stochastic
- value-at-risk
- var
aliases:
- Inflation and Returns
- Real vs. Nominal
- State-Price Deflators
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
- Capital Asset Pricing Model (CAPM) and beta estimation
- Central bank digital currencies (CBDCs)
- Central clearing and CCP risk management
- Commodity futures and convenience yields
- Commodity swaps and energy derivatives
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
- Hull-White and Black-Karasinski short rate models
- IPO pricing and underpricing analysis
- Implied volatility and volatility surface modeling
- Inflation Rate Calculation
- Inflation-linked swaps and CPI adjustments
- Interest rate derivatives and forward rate agreements
- Interest rate models and term structure
- Interest rate swaps and swap spread decomposition
- Ito's Lemma and stochastic calculus
- Key rate duration and curve risk decomposition
- Liquidity-adjusted VaR and liquidity horizons
- Lognormal Setting Returns
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
- Nominal vs Real Dividends
- Non-deliverable forwards and emerging market instruments
- OIS discounting and collateralized interest rate derivatives
- Option Greeks and sensitivity analysis
- Options on futures and forward-starting options
- Payment systems and settlement risk
- Prime brokerage and securities lending
- Private credit and direct lending
- Project finance and syndicated lending
- Real and Nominal Returns
- Real estate investment trusts (REITs)
- Recovery rate modeling and loss given default
- Repo markets and securities lending
- Risk factor decomposition and sensitivity analysis
- Risk parity and risk budgeting strategies
- Shadow banking and non-bank intermediation
- Smart beta and alternative indexing approaches
- State-Price Deflator Definition
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
- Yield curve construction and term structure modeling
- Zero-coupon bond pricing and bootstrapping
enhanced: true
enhancement_date: '2025-11-06'
enhancement_id: batch04-108735
---




# 4.5 Nominal and real state-price deflators  

It is important to distinguish between real and nominal dividends and prices. A nominal dividend [price] is the dividend [price] in units of a given currency, e.g. US dollars or Euros. The corresponding real dividend [price] is the number of units of consumption goods which can be purchased for the nominal dividend [price]. For simplicity assume that the economy only offers a single con-. sumption good and let $F_{t}$ denote the price of the good in currency units at time $t$ . (More broadly we can think of $F_{t}$ as the value of the Consumer Price Index at time $t$ ) A nominal dividend of $\tilde{D}_{t}$ then corresponds to a real dividend of $D_{t}=\tilde{D}_{t}/F_{t}$ . A nominal price of $\tilde{P}_{t}$ corresponds to a real price of $P_{t}=\tilde{P}_{t}/F_{t}$  

A state-price deflator basically links future dividends to current prices. We can define a nominal. state-price deflator so that the basic pricing condition holds for nominal prices and dividends and,. similarly, define a real state-price deflator so that the basic pricing condition holds for real prices and dividends. If we continue to indicate nominal quantities by a tilde and real quantities without a tilde, the definitions of state-price deflators given earlier in this chapter characterize real state-price. deflators.  

Consider a multi-period discrete-time economy where $\zeta=\left(\zeta_{t}\right)$ is a real state-price deflator so. that, in particular,.  
$$
P_{i t}=\mathrm{E}_{t}\left[\sum_{s=t+1}^{T}D_{i s}\frac{\zeta_{s}}{\zeta_{t}}\right],
$$  

cf. (4.20). Substituting in $P_{i t}=\tilde{P}_{i t}/F_{t}$ and $D_{i s}=\tilde{D}_{i s}/F_{s}$ and multiplying through by $F_{t}$ , we obtain  
$$
\tilde{P}_{i t}=\mathrm{E}_{t}\left[\sum_{s=t+1}^{T}\tilde{D}_{i s}\frac{\zeta_{s}/F_{s}}{\zeta_{t}/F_{t}}\right].
$$  

Now it is clear that a nominal state-price deflator $\tilde{\zeta}=(\tilde{\zeta}_{t})$ should be defined from a real state-price. deflator $\zeta=\left(\zeta_{t}\right)$ as  
$$
\tilde{\zeta}_{t}=\frac{\zeta_{t}}{F_{t}},~\mathrm{all}~t\in\mathcal{T}.
$$  

Then the nominal state-price deflator will link nominal dividends to nominal prices in the same way that a real state-price deflator links real dividends to real prices. This relation also works in the continuous-time framework. Note that the nominal state-price deflator is positive with an initial value of $\tilde{\zeta}_{0}=1/F_{0}$  

In a discrete-time framework the gross nominal return on asset $i$ between time $t$ and time $t+1$ is $\tilde{R}_{i,t+1}=\left(\tilde{P}_{i,t+1}+\tilde{D}_{i,t+1}\right)/\tilde{P}_{i t}$ . The link between the gross real return and the gross nominal return follows from  
$$
\begin{array}{r l}&{R_{i,t+1}=\frac{P_{i,t+1}+D_{i,t+1}}{P_{i t}}=\frac{\tilde{P}_{i,t+1}/F_{t+1}+\tilde{D}_{i,t+1}/F_{t+1}}{\tilde{P}_{i t}/F_{t}}}\ &{\qquad=\frac{\tilde{P}_{i,t+1}+\tilde{D}_{i,t+1}}{\tilde{P}_{i t}}\frac{F_{t}}{F_{t+1}}=\tilde{R}_{i,t+1}\frac{F_{t}}{F_{t+1}}.}\end{array}
$$  

In terms of the net rates of return $r_{i,t+1}=R_{i,t+1}-1$ $\tilde{r}_{i,t+1}=\tilde{R}_{i,t+1}-1$ , and the percentage. inflation/War%20Economies%20and%20Hyperinflation.md) rate $\varphi_{t+1}=F_{t+1}/F_{t}-1$ we have  
$$
1+r_{i,t+1}=\frac{1+\tilde{r}_{i,t+1}}{1+\varphi_{t+1}},
$$  

which implies that  
$$
r_{i,t+1}=\frac{1+\Tilde{r}_{i,t+1}}{1+\varphi_{t+1}}-1=\frac{\Tilde{r}_{i,t+1}-\varphi_{t+1}}{1+\varphi_{t+1}}\approx\Tilde{r}_{i,t+1}-\varphi_{t+1}.
$$  

The above equations show how to obtain real returns from nominal returns and inflation/War%20Economies%20and%20Hyperinflation.md). Given a time series of nominal returns and inflation/War%20Economies%20and%20Hyperinflation.md), it is easy to compute the corresponding time series of real returns.  

The realized gross inflation/War%20Economies%20and%20Hyperinflation.md) rate $F_{t+1}/F_{t}$ is generally not known in advance. Therefore the real. return on a nominally risk-free asset is generally stochastic (and conversely). The link between the nominally risk-free gross return $\tilde{R}_{t}^{f}$ and the real risk-free gross return $R_{t}^{f}$ is  
$$
\begin{array}{l}{{\displaystyle\frac{1}{{\tilde{R}}_{t}^{f}}={\mathrm{E}}_{t}\left[\frac{{\tilde{\zeta}}_{t+1}}{{\tilde{\zeta}}_{t}}\right]={\mathrm{E}}_{t}\left[\frac{{\zeta}_{t+1}}{{\zeta}_{t}}\frac{F_{t}}{F_{t+1}}\right]}}\ {~={\mathrm{E}}_{t}\left[\frac{{\zeta}_{t+1}}{{\zeta}_{t}}\right]{\mathrm{E}}_{t}\left[\frac{F_{t}}{F_{t+1}}\right]+{\mathrm{Cov}}_{t}\left[\frac{{\zeta}_{t+1}}{{\zeta}_{t}},\frac{F_{t}}{F_{t+1}}\right]}\ {~=\frac{1}{R_{t}^{f}}{\mathrm{E}}_{t}\left[\frac{F_{t}}{F_{t+1}}\right]+{\mathrm{Cov}}_{t}\left[\frac{{\zeta}_{t+1}}{{\zeta}_{t}},\frac{F_{t}}{F_{t+1}}\right].}\end{array}
$$  

In order to obtain a simpler link between the nominal and the real risk-free returns, we specialize to a lognormal setting. Assume that the next-period state-price deflator. $\zeta_{t+1}/\zeta_{t}$ and the gross realized inflation/War%20Economies%20and%20Hyperinflation.md) $F_{t+1}/F_{t}$ are given by  
$$
\frac{\zeta_{t+1}}{\zeta_{t}}=e^{-a_{t}+b_{t}\varepsilon_{t+1}},\qquad\frac{F_{t+1}}{F_{t}}=e^{h_{t}+k_{t}(\rho_{t}\varepsilon_{t+1}+\sqrt{1-\rho_{t}^{2}}\eta_{t+1})},
$$  

where $a=\left(a_{t}\right)$ $b=\left(b_{t}\right)$ $h=\left(h_{t}\right)$ $k=\left(k_{t}\right)$ , and $\rho=\left(\rho_{t}\right)$ are adapted processes, and where the shocks $\varepsilon_{t+1}$ and $\eta_{t+1}$ are independent and identically $N(0,1)$ distributed IID. Note that  
$$
\operatorname{E}_{t}\left[\ln\left({\frac{\zeta_{t+1}}{\zeta_{t}}}\right)\right]=-a_{t},\qquad\operatorname{Var}_{t}\left[\ln\left({\frac{\zeta_{t+1}}{\zeta_{t}}}\right)\right]=b_{t}^{2}.
$$  

Using Theorem B.2 in Appendix B, the gross real risk-free return becomes  
$$
R_{t}^{f}=\left(\operatorname{E}_{t}\left[{\frac{\zeta_{t+1}}{\zeta_{t}}}\right]\right)^{-1}=\left(e^{-a_{t}+{\frac{1}{2}}b_{t}^{2}}\right)^{-1}=e^{a_{t}-{\frac{1}{2}}b_{t}^{2}}
$$  

so that the continuously compounded real risk-free is  
$$
r_{t}^{f}=\ln R_{t}^{f}=a_{t}-{\frac{1}{2}}b_{t}^{2}.
$$  

Similarly, the expectation and the variance of the log inflation/War%20Economies%20and%20Hyperinflation.md) rate are  
$$
\operatorname{E}_{t}\left[\ln\left({\frac{F_{t+1}}{F_{t}}}\right)\right]=h_{t},\qquad\operatorname{Var}_{t}\left[\ln\left({\frac{F_{t+1}}{F_{t}}}\right)\right]=k_{t}^{2},
$$  

implying an expected gross inflation/War%20Economies%20and%20Hyperinflation.md) of  
$$
\mathrm{E}_{t}\left[{\frac{F_{t+1}}{F_{t}}}\right]=e^{h_{t}+{\frac{1}{2}}k_{t}^{2}}.
$$  

Assuming that $b_{t}$ and $k_{t}$ are positive, $\rho_{t}$ is the correlation between the log real state-price deflator and the log inflation/War%20Economies%20and%20Hyperinflation.md) rate.  

Due to the lognormality assumption we can directly compute the expectation of the nominal state-price deflator over the next period:  
$$
\begin{array}{r l}&{\mathrm{E}_{t}\left[\frac{\tilde{\zeta}_{t+1}}{\tilde{\zeta}_{t}}\right]=\mathrm{E}_{t}\left[\frac{\zeta_{t+1}}{\zeta_{t}}\frac{F_{t}}{F_{t+1}}\right]=\mathrm{E}_{t}\left[e^{-a_{t}+b_{t}\varepsilon_{t+1}}e^{-h_{t}-k_{t}\rho_{t}\varepsilon_{t+1}-k_{t}\sqrt{1-\rho_{t}^{2}}\eta_{t+1}}\right]}\ &{\qquad=e^{-a_{t}-h_{t}}\mathrm{E}_{t}\left[e^{(b_{t}-k_{t}\rho_{t})\varepsilon_{t+1}}\right]\mathrm{E}_{t}\left[e^{-k_{t}\sqrt{1-\rho_{t}^{2}}\eta_{t+1}}\right]}\ &{\qquad=e^{-a_{t}-h_{t}}e^{\frac{1}{2}(b_{t}-k_{t}\rho_{t})^{2}}e^{\frac{1}{2}k_{t}^{2}(1-\rho_{t}^{2})}=e^{-a_{t}-h_{t}+\frac{1}{2}b_{t}^{2}+\frac{1}{2}k_{t}^{2}-\rho_{t}b_{t}k_{t}}.}\end{array}
$$  

The gross nominal risk-free return is thus  
$$
\begin{array}{r}{\tilde{R}_{t}^{f}=\left(\mathrm{E}_{t}\left[\frac{\tilde{\zeta}_{t+1}}{\tilde{\zeta}_{t}}\right]\right)^{-1}=e^{a_{t}+h_{t}-\frac{1}{2}b_{t}^{2}-\frac{1}{2}k_{t}^{2}+\rho_{t}b_{t}k_{t}},}\end{array}
$$  

and the continuously compounded nominal risk-free rate is  
$$
\tilde{r}_{t}^{f}=\ln\tilde{R}_{t}^{f}=a_{t}+h_{t}-\frac{1}{2}b_{t}^{2}-\frac{1}{2}k_{t}^{2}+\rho_{t}b_{t}k_{t},
$$  

which we can rewrite using (4.66) as  
$$
\begin{array}{r l}&{\widetilde{r}_{t}^{f}=r_{t}^{f}+h_{t}-\frac12k_{t}^{2}+\rho_{t}b_{t}k_{t}}\ &{\quad=r_{t}^{f}+\ln\left(\operatorname{E}_{t}\left[\frac{F_{t+1}}{F_{t}}\right]\right)-\operatorname{Var}_{t}\left[\ln\left(\frac{F_{t+1}}{F_{t}}\right)\right]+\operatorname{Cov}_{t}\left[\ln\left(\frac{\zeta_{t+1}}{\zeta_{t}}\right),\ln\left(\frac{F_{t+1}}{F_{t}}\right)\right].}\end{array}
$$  

The nominal risk-free rate equals the real risk-free rate plus log-expected inflation/War%20Economies%20and%20Hyperinflation.md) minus inflation/War%20Economies%20and%20Hyperinflation.md) variance and adjusted by an inflation/War%20Economies%20and%20Hyperinflation.md) risk premium..  

We can obtain a similar but more generally valid expression in a continuous-time framework. Let $\zeta=\left(\zeta_{t}\right)$ denote a real state-price deflator, which evolves over time according to.  
$$
\begin{array}{r}{d\zeta_{t}=-\zeta_{t}\left[r_{t}^{f}d t+\lambda_{t}^{\top}d z_{t}\right],}\end{array}
$$  

where $\boldsymbol{r}^{f}=(r_{t}^{f})$ is the short-term real interest rate and $\lambda=\left(\lambda_{t}\right)$ is the market price of risk. Assume that the dynamics of the price of the consumption good can be written as  
$$
d F_{t}=F_{t}\left[\mu_{\varphi t}d t+\pmb{\sigma}_{\varphi t}^{\top}d z_{t}\right].
$$  

We can interpret $\varphi_{t+d t}=d F_{t}/F_{t}$ as the realized inflation/War%20Economies%20and%20Hyperinflation.md) rate over the next instant, $\mu_{\varphi t}=\operatorname{E}_{t}[\varphi_{t+d t}]$ as the expected inflation rate, and $\sigma_{\varphi t}$ as the sensitivity vector of the inflation/War%20Economies%20and%20Hyperinflation.md) rate.  

Consider now a nominal bank account which over the next instant promises a risk-free monetary return represented by the nominal short-term interest rate. $\tilde{r}_{t}^{f}$ . If we let $\tilde{N}_{t}$ denote the time $t$ dollar value of such an account, we have that.  
$$
d\tilde{N}_{t}=\tilde{r}_{t}^{f}\tilde{N}_{t}d t.
$$  

The real price of this account is. $N_{t}=\tilde{N}_{t}/F_{t}$ , since this is the number of units of the consumption. good that has the same value as the account. An application of Ito's Lemma implies a real price dynamics of  
$$
d N_{t}=N_{t}\left[\left(\tilde{r}_{t}^{f}-\mu_{\varphi t}+\ | \pmb{\sigma}_{\varphi t}\ | ^{2}\right)d t-\pmb{\sigma}_{\varphi t}^{\top}d z_{t}\right].
$$  

Note that the real return on this instantaneously nominally risk-free asset, $d N_{t}/N_{t}$ , is risky. Since the percentage sensitivity vector is given by $-\pmb{\sigma}_{\varphi t}$ , the expected return is given by the real short rate plus $-\pmb{\sigma}_{\varphi t}^{\top}\pmb{\lambda}_{t}$ . Comparing this with the drift term in the equation above, we have that  
$$
\tilde{r}_{t}^{f}-\mu_{\varphi t}+\ | \pmb{\sigma}_{\varphi t}\ | ^{2}=r_{t}^{f}-\pmb{\sigma}_{\varphi t}^{\top}\pmb{\lambda}_{t}.
$$  

Consequently the nominal short-term interest rate is given by  
$$
\tilde{r}_{t}^{f}=r_{t}^{f}+\mu_{\varphi t}-\ | \pmb{\sigma}_{\varphi t}\ | ^{2}-\pmb{\sigma}_{\varphi t}^{\top}\pmb{\lambda}_{t},
$$  

i.e. the nominal short rate is equal to the real short rate plus the expected inflation rate minus the variance of the inflation/War%20Economies%20and%20Hyperinflation.md) rate minus a risk premium. The first three terms on the right-hand side are clearly analogous to those in the discrete-time relation (4.67). The continuous-time equivalent of the last term in (4.67) is  
$$
\begin{array}{r}{\mathrm{Cov}_{t}[d(\ln{\zeta_{t}}),d(\ln{F_{t}})]=\mathrm{Cov}_{t}[-\lambda_{t}^{\top}d z_{t},\sigma_{\varphi t}^{\top}d z_{t}]=-\sigma_{\varphi t}^{\top}\lambda_{t}d t,}\end{array}
$$  

which corresponds to the last term in (4.70). The discrete-time relation (4.67) and the continuoustime relation (4.70) are therefore completely analogous, but the discrete-time relation could only be derived in a lognormal setting.  

The presence of the last two terms in (4.70) invalidates the Fisher relation, which says that the nominal interest rate is equal to the sum of the real interest rate and the expected inflation rate. The Fisher hypothesis will hold if and only if the inflation/War%20Economies%20and%20Hyperinflation.md) rate is instantaneously risk-free. In.  

Chapter 10 we will discuss the link between real and nominal interest rates and yields in more detail.  

Individuals should primarily be concerned about real values since, in the end, they should care about the number of goods they can consume. Therefore, most theoretical asset pricing models make predictions about expected real returns.

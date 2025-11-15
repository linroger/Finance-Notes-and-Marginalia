---
tags:
- artificial-intelligence
- cdo
- closed_form_valuation
- collateralized-debt-obligation
- continuous_time
- derivatives-pricing
- discrete_time
- interest-rate-derivatives
- interest-rate-swap
- irs
- ma
- markets
- mathematics
- mpt
- multi_period_valuation
- option-greeks
- quantitative-pricing
- risk-management
- state_price_deflator
- value-at-risk
- var
aliases:
- Multi-Period Models
- Multi-Period Valuation
key_concepts:
- Agricultural futures and seasonality
- Alternative investments and hedge fund strategies
- Asset swaps and spread-lock strategies
- Barrier options and knock-in/knock-out structures
- Basis swaps and cross-currency basis adjustments
- Basis swaps and floating rate correlations
- Behavioral finance and market anomalies
- Best execution and regulatory requirements
- Bid-ask spreads and market making profitability
- Black-Litterman model and portfolio optimization
- CDO structuring and tranche allocation methodologies
- CDO-squared structures and correlation trading
- Calendar spreads and roll strategies
- Capital Asset Pricing Model (CAPM) and beta estimation
- Central clearing and CCP risk management
- Closed-form dividend valuation
- Commodity futures and convenience yields
- Commodity swaps and energy derivatives
- Constant maturity swaps and roll-over features
- Continuous-time valuation
- Crack spreads in energy markets
- Credit risk assessment and loan pricing
- Credit valuation adjustment (CVA) and counterparty risk
- Cryptocurrency valuation and blockchain technology
- Currency swaps and cross-currency basis
- Dark pools and alternative trading venues
- DeFi protocols and decentralized finance
- Delta hedging and Greeks calculation
- Deposit insurance and systemic risk
- Discounted cash flow (DCF) valuation methodologies
- Discrete-time framework
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
- Mortgage-backed securities and prepayment modeling
- Multi-factor interest rate models
- Negative interest rates and floor/cap structures
- Net interest margin and banking profitability
- Netting agreements and close-out procedures
- Non-deliverable forwards and emerging market instruments
- Numerical methods for PDEs
- OIS discounting and collateralized interest rate derivatives
- Options on futures and forward-starting options
- Payment systems and settlement risk
- Price-dividend ratio
- Prime brokerage and securities lending
- Private credit and direct lending
- Project finance and syndicated lending
- Recovery rate modeling and loss given default
- Repo markets and securities lending
- Risk factor decomposition and sensitivity analysis
- Risk parity and risk budgeting strategies
- Risk-adjusted discount factor
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
enhancement_id: batch04-505381
---




# 4.4 Multi-period valuation models  

This section gives some examples of concrete assumptions on the state-price deflator and the dividends that will lead to a closed-form expression for the present value of the dividends.  

Here is a simple example of closed-form valuation of a single terminal dividend of $D_{T}$ . Suppose that $D_{T}=\mathrm{E}_{t}[D_{T}]e^{X}$ for a lognormally distributed random variable. $X$ . To ensure $\operatorname{E}_{t}[e^{X}]=1$ , we need $X\sim N(-\textstyle{\frac{1}{2}}\sigma_{X}^{2},\sigma_{X}^{2})$ , cf. Theorem B.2 in Appendix B. Also assume that $\zeta_{T}=\zeta_{t}e^{Y}$ , where $X$ and $Y$ are jointly normally distributed with correlation. $\rho$ and $Y\sim N(\mu_{Y},\sigma_{Y}^{2})$ . Then the present. value of the dividend is.  
$$
P_{t}=\operatorname{E}_{t}\left[D_{T}{\frac{\zeta_{T}}{\zeta_{t}}}\right]=\operatorname{E}_{t}\left[\operatorname{E}_{t}[D_{T}]e^{X}e^{Y}\right]=\operatorname{E}_{t}[D_{T}]\operatorname{E}_{t}\left[e^{X+Y}\right].
$$  

Since $\begin{array}{r}{X+Y\sim N(-\frac{1}{2}\sigma_{X}^{2}+\mu_{Y},\sigma_{X}^{2}+\sigma_{Y}^{2}+2\rho\sigma_{X}\sigma_{Y})}\end{array}$ , we get  
$$
\begin{array}{c}{{\displaystyle\mathrm{E}_{t}\left[e^{X+Y}\right]=\exp\left\{-\frac{1}{2}\sigma_{X}^{2}+\mu_{Y}+\frac{1}{2}\left(\sigma_{X}^{2}+\sigma_{Y}^{2}+2\rho\sigma_{X}\sigma_{Y}\right)\right\}}}\ {{\mathrm{}=\exp\left\{\mu_{Y}+\frac{1}{2}\sigma_{Y}^{2}+\rho\sigma_{X}\sigma_{Y}\right\}}}\end{array}
$$  

and thus  
$$
P_{t}=\mathrm{E}_{t}[D_{T}]\exp\left\{\mu_{Y}+\frac{1}{2}\sigma_{Y}^{2}+\rho\sigma_{X}\sigma_{Y}\right\}.
$$  

The exponential term on the right-hand side of that equation is the appropriately risk-adjusted discount factor for the given dividend.  

In a continuous-time setting the distributional assumption on $Y=\ln(\zeta_{T}/\zeta_{t})$ is satisfied if the. market price of risk vector is a constant. $\lambda$ and the short-term risk-free rate is a constant. $r^{f}$ since then  
$$
Y=-\left(r^{f}+\frac{1}{2}\ | \lambda\ | ^{2}\right)(T-t)-\int_{t}^{T}\lambda^{\top}d z_{u}\sim N\left(-\left(r^{f}+\frac{1}{2}\ | \lambda\ | ^{2}\right)(T-t),\ | \lambda\ | ^{2}(T-t)\right),
$$  

in which case we can rewrite the present value as  
$$
P_{t}=\mathrm{E}_{t}[D_{T}]\exp\left\{-r^{f}(T-t)+\rho\sigma_{X}\sigma_{Y}\right\}.
$$  

If we substitute in $O Y$ and write $\sigma_{X}^{2}\:=\:\sigma_{d}^{2}(T-t)$ , where $\sigma_{d}^{2}$ is the annualized variance of the dividend, we get a present value of  
$$
P_{t}=\operatorname{E}_{t}[D_{T}]\exp\left\{-r^{f}(T-t)+\rho\sigma_{d}\ | \lambda\ | (T-t)\right\}=\operatorname{E}_{t}[D_{T}]\exp\left\{-(r^{f}-\rho\sigma_{d}\ | \lambda\ | )(T-t)\right\}.
$$  

The expected dividend is discounted with a risk-adjusted percentage interest rate, which equals the risk-free rate minus $\rho\sigma_{d}\ | \boldsymbol{\lambda}\ | $

# 4.4.1 Discrete-time valuation  

Consider a discrete-time multi-period framework and assume that the state-price deflator $\zeta=\left(\zeta_{t}\right)$ satisfies  
$$
\begin{array}{r}{\mathrm{E}_{t}\left[\frac{\zeta_{t+1}}{\zeta_{t}}\right]=\mu_{\zeta},\quad\mathrm{Var}_{t}\left[\frac{\zeta_{t+1}}{\zeta_{t}}\right]=\sigma_{\zeta}^{2}}\end{array}
$$  

for each $t=0,1,2,\ldots,T-1$ . In particular, $\operatorname{E}_{t}\left[(\zeta_{t+1}/\zeta_{t})^{2}\right]=\sigma_{\zeta}^{2}+\mu_{\zeta}^{2}$ . Consider an uncertain stream of dividends $D=\left(D_{t}\right)$ , where the dividend growth rate is given by  
$$
\frac{D_{t+1}}{D_{t}}=a+b\frac{\zeta_{t+1}}{\zeta_{t}}+\varepsilon_{t+1},\quad t=0,1,\ldots,T-1,
$$  

where $\varepsilon_{1},\ldots,\varepsilon_{T}$ are independent with $\mathrm{E}_{t}[\varepsilon_{t+1}]=0$ and $\mathrm{E}_{t}[\varepsilon_{t+1}\zeta_{t+1}]=0$ for all $t$  

First note that  
$$
\begin{array}{c}{\displaystyle\mathrm{E}_{t}\left[\frac{D_{t+1}}{D_{t}}\frac{\zeta_{t+1}}{\zeta_{t}}\right]=\mathrm{E}_{t}\left[\left(a+b\frac{\zeta_{t+1}}{\zeta_{t}}+\varepsilon_{t+1}\right)\frac{\zeta_{t+1}}{\zeta_{t}}\right]=a\mathrm{E}_{t}\left[\frac{\zeta_{t+1}}{\zeta_{t}}\right]+b\mathrm{E}_{t}\left[\left(\frac{\zeta_{t+1}}{\zeta_{t}}\right)^{2}\right]}\ {=a\mu_{\zeta}+b\left(\sigma_{\zeta}^{2}+\mu_{\zeta}^{2}\right)\equiv A}\end{array}
$$  

for every $t=0,1,\ldots,T-1$ . Together with the Law of Iterated Expectations this implies that for each $s>t$  
$$
\begin{array}{r l}&{\mathrm{E}_{t}\left[\frac{D_{s}}{D_{t}}\frac{\zeta_{s}}{\zeta_{t}}\right]=\mathrm{E}_{t}\left[\frac{D_{s-1}}{D_{t}}\frac{\zeta_{s-1}}{\zeta_{t}}\frac{D_{s}}{D_{s-1}}\frac{\zeta_{s}}{\zeta_{s-1}}\right]}\ &{\qquad=\mathrm{E}_{t}\left[\frac{D_{s-1}}{D_{t}}\frac{\zeta_{s-1}}{\zeta_{t}}\mathrm{E}_{s-1}\left[\frac{D_{s}}{D_{s-1}}\frac{\zeta_{s}}{\zeta_{s-1}}\right]\right]}\ &{\qquad=A\mathrm{E}_{t}\left[\frac{D_{s-1}}{D_{t}}\frac{\zeta_{s-1}}{\zeta_{t}}\right]}\ &{\qquad=\dots}\ &{\qquad=A^{s-t}.}\end{array}
$$  

The price-dividend ratio of the asset is therefore  
$$
\begin{array}{l}{{\displaystyle{\frac{P_{t}}{D_{t}}}=\mathrm{E}_{t}\left[\sum_{s=t+1}^{T}\frac{D_{s}}{D_{t}}\frac{\zeta_{s}}{\zeta_{t}}\right]=\sum_{s=t+1}^{T}\mathrm{E}_{t}\left[\frac{D_{s}}{D_{t}}\frac{\zeta_{s}}{\zeta_{t}}\right]}}\ {{\displaystyle~=\sum_{s=t+1}^{T}A^{s-t}=A+A^{2}+\cdot\cdot\cdot+A^{T-t}}}\ {{\displaystyle~=\frac{A}{1-A}\left(1-A^{T-t}\right).}}\end{array}
$$  

The price is thus  
$$
P_{t}=D_{t}\frac{A}{1-A}\left(1-A^{T-t}\right).
$$  

If $ | A | <1$ and you let $T\to\infty$ , i.e. assume dividends continue in all future, you get
$$
P_{t}=D_{t}\frac{A}{1-A}.
$$  

In particular, the price-dividend ratio is a constant.1  

# 4.4.2 Continuous-time valuation: The PDE approach  

[^4]: 4.3 Continuous-time valuation: Affine models

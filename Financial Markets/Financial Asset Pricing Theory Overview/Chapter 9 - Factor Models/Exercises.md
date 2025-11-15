---
tags:
- apt
- arbitrage
- artificial-intelligence
- beta
- bond-pricing
- capm
- cdo
- collateralized-debt-obligation
- continuous_time
- defi
- discrete_time_economy
- e-mini
- fixed-income
- fixed-income-derivatives
- interest-rate-derivatives
- interest-rate-swap
- irs
- ito-calculus
- linear_factor_model
- ma
- mean_variance
- mpt
- nim
- option-greeks
- options
- options-pricing
- risk-management
- state_price_deflator
- stochastic
- value-at-risk
- var
aliases:
- Exercise 9.1
- Exercise 9.2
- Exercise 9.3
- Exercise 9.4
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
- Capital Asset Pricing Model (CAPM)
- Capital Asset Pricing Model (CAPM) and beta estimation
- Central clearing and CCP risk management
- Commodity futures and convenience yields
- Commodity swaps and energy derivatives
- Constant maturity swaps and roll-over features
- Corporate bond pricing and credit spread decomposition
- Crack spreads in energy markets
- Credit risk assessment and loan pricing
- Credit valuation adjustment (CVA) and counterparty risk
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
- Historical simulation and parametric VaR approaches
- Hull-White and Black-Karasinski short rate models
- IPO pricing and underpricing analysis
- Implied volatility and volatility surface modeling
- Inflation-linked swaps and CPI adjustments
- Interest rate derivatives and forward rate agreements
- Interest rate swaps and swap spread decomposition
- Ito's Lemma and stochastic calculus
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
- Netting agreements and close-out procedures
- Non-deliverable forwards and emerging market instruments
- OIS discounting and collateralized interest rate derivatives
- Option Greeks and sensitivity analysis
- Options on futures and forward-starting options
- Payment systems and settlement risk
- Portfolio optimization and mean-variance theory
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
- continuous-time framework
- discrete-time economy
- linear factor model
- market price of risk
- mean-variance frontier
- state-price deflator
enhanced: true
enhancement_date: '2025-11-06'
enhancement_id: batch04-971197
---




# 9.8 Exercises  

EXERCISE 9.1 Consider a discrete-time economy with a one-dimensional conditional pricing factor $x=\left(x_{t}\right)$ so that, for some adapted processes $\alpha=\left(\alpha_{t}\right)$ and some $\eta=\left(\eta_{t}\right)$  
$$
\mathrm{E}_{t}[R_{i,t+1}]=\alpha_{t}+\beta_{t}[R_{i,t+1},\boldsymbol{x}_{t+1}]\eta_{t},
$$  

for all assets $i$ and all $t=0,1,\ldots,T-1$  

(a) Show that  
$$
\frac{\zeta_{t+1}}{\zeta_{t}}=\frac{1}{\alpha_{t}}\left(1-\frac{x_{t+1}-\mathrm{E}_{t}[x_{t+1}]}{\mathrm{Var}_{t}[x_{t+1}]}\eta_{t}\right)
$$  

satisfies the pricing condition for a state-price deflator, i.e.  
$$
\mathrm{E}_{t}\left[\frac{\zeta_{t+1}}{\zeta_{t}}R_{i,t+1}\right]=1
$$  

for all assets $i$  

(b) Show that $\zeta_{t+1}/\zeta_{t}$ is only a true one-period state-price deflator for the period between time $t$ and time $t+1$ if you to impose some condition on parameters and/or distributions and provide that condition. If this condition is not satisfied, what can you conclude about the asset prices in this economy?   
(c) Now suppose that the factor is the return on some particular portfolio, i.e. $x_{t+1}=\tilde{R}_{t+1}$ Answer question (b) again..   
(d) Consider the good (?) old (!) CAPM where $x_{t+1}=R_{M,t+1}$ , the return on the market portfolio. Suppose that $\mathrm{E}_{t}[R_{M,t+1}]=1.05$ $\sigma_{t}[R_{M,t+1}]=0.2\$ , and $R_{t}^{f}=1.02$ . What do you need to assume about the distribution of the market return to ensure that the model is free of arbitrage? Is an assumption like this satisfied in typical derivations of the CAPM?.  

EXERCISE 9.2 Using the orthogonal characterization of the mean-variance frontier, show that for any mean-variance efficient return $R^{\pi}$ different from the minimum-variance portfolio there is a unique mean-variance efficient return $R^{z(\pmb{\pi})}$ with $\mathrm{Cov}[R^{\pi},R^{z(\pmb{\pi})}]=0$ . Show that  
$$
\operatorname{E}[R^{z(\pi)}]=\operatorname{E}[R^{*}]-\operatorname{E}[R^{e*}]{\frac{\operatorname{E}[(R^{*})^{2}]-\operatorname{E}[R^{\pi}]\operatorname{E}[R^{*}]}{\operatorname{E}[R^{\pi}]-\operatorname{E}[R^{*}]-\operatorname{E}[R^{\pi}]\operatorname{E}[R^{e*}]}}.
$$  

EXERCISE 9.3 Consider a discrete-time economy in which asset prices are described by an unconditional linear factor model  
$$
\frac{\zeta_{t+1}}{\zeta_{t}}=a+b\cdot x_{t+1},\quad t=0,1,\ldots,T-1,
$$  

where the conditional mean and second moments of the factor are constant, i.e. $\operatorname{E}_{t}[\pmb{x}_{t+1}]=\pmb{\mu}$ and $\mathrm{E}_{t}[\mathbf{\underline{{x}}}_{t+1}\mathbf{\underline{{x}}}_{t+1}^{\top}]=\underline{{\underline{{\Sigma}}}}$ for all $t$  

You want to value an uncertain stream of dividends $D=\left(D_{t}\right)$ . You are told that dividends evolve. as  
$$
\frac{D_{t+1}}{D_{t}}=m+\psi\cdot\pmb{x}_{t+1}+\varepsilon_{t+1},\quad t=0,1,\dots,T-1,
$$  

where $\mathrm{E}_{t}[\varepsilon_{t+1}]=0$ and $\mathrm{E}_{t}[\boldsymbol{\varepsilon}_{t+1}\boldsymbol{x}_{t+1}]=\mathbf{0}$ for all $t$  

The first three questions will lead you through the valuation based directly on the pricing condition of the state-price deflator.  

(a) Show that, for any $t=0,1,\ldots,T-1$  
$$
\operatorname{E}_{t}\left[{\frac{D_{t+1}}{D_{t}}}{\frac{\zeta_{t+1}}{\zeta_{t}}}\right]=m a+\left(m{b}+a\psi\right)\cdot\mu+\psi^{\top}{\underline{{\Sigma}}}{b}\equiv A
$$  

(b) Show that  
$$
\operatorname{E}_{t}\left[{\frac{D_{t+s}}{D_{t}}}{\frac{\zeta_{t+s}}{\zeta_{t}}}\right]=A^{s}.
$$  

(c) Show that the value at time $t$ of the future dividends is  
$$
P_{t}=D_{t}\frac{A}{1-A}\left(1-A^{T-t}\right).
$$  

Next, consider an alternative valuation technique. From (4.31) we know that the dividends can be valued by the formula  
$$
P_{t}=\sum_{s=1}^{T-t}\frac{\operatorname{E}_{t}[D_{t+s}]-\beta_{t}\left[D_{t+s},\frac{\zeta_{t+s}}{\zeta_{t}}\right]\eta_{t,t+s}}{(1+\hat{y}_{t}^{t+s})^{s}},
$$  

where  
$$
\beta_{t}\left[D_{t+s},\frac{\zeta_{t+s}}{\zeta_{t}}\right]=\mathrm{Cov}_{t}\left[D_{t+s},\frac{\zeta_{t+s}}{\zeta_{t}}\right]/\mathrm{Var}_{t}\left[\frac{\zeta_{t+s}}{\zeta_{t}}\right],\quad\eta_{t,t+s}=-\mathrm{Var}_{t}\left[\frac{\zeta_{t+s}}{\zeta_{t}}\right]/\mathrm{E}_{t}\left[\frac{\zeta_{t+s}}{\zeta_{t}}\right].
$$  

In the next questions you have to compute the ingredients to this valuation formula.  

(d) What is the one-period risk-free rate of return $\boldsymbol{r}_{t}^{f}$ ? What is the time $t$ annualized yield $\hat{y}_{t}^{t+s}$ on a zero-coupon bond maturing at time. $t+s$ ? (If $B_{t}^{t+s}$ denotes the price of the bond, tl. annualized gross yield is defined by the equation $B_{t}^{t+s}=(1+\hat{y}_{t}^{t+s})^{-s}$   
(e) Show that $\mathrm{E}_{t}[D_{t+s}]=D_{t}\left(m+\psi\cdot\pmb{\mu}\right)^{s}$   
(f) Compute $\operatorname{Cov}_{t}\left[D_{t+s},\frac{\zeta_{t+s}}{\zeta_{t}}\right]$   
(g) Compute $\beta_{t}\left[D_{t+s},\frac{\zeta_{t+s}}{\zeta_{t}}\right]$   
(h) Compute $\eta_{t,t+s}$   
(i) Verify that the time $t$ value of the future dividends satisfies. $(^{*})$  

EXERCISE 9.4 In a continuous-time framework an individual with time-additive expected power utility induces the state-price deflator.  
$$
\zeta_{t}=e^{-\delta t}\left(\frac{c_{t}}{c_{0}}\right)^{-\gamma},
$$  

where $\gamma$ is the constant relative risk aversion,. $\delta$ is the subjective time preference rate, and. $c=$ $(c_{t})_{t\in[0,T]}$ is the optimal consumption process of the individual. If the dynamics of the optimal consumption process is of the form.  
$$
d c_{t}=c_{t}\left[\mu_{c t}d t+\sigma_{c t}^{\top}d z_{t}\right]
$$  

then the dynamics of the state-price deflator is  
$$
d\zeta_{t}=-\zeta_{t}\left[\left(\delta+\gamma\mu_{c t}-\frac{1}{2}\gamma(1+\gamma)\ | \sigma_{c t}\ | ^{2}\right)d t+\gamma\sigma_{c t}^{\top}d z_{t}\right].
$$  

(a) State the market price of risk $\lambda_{t}$ in terms of the preference parameters and the expected growth rate and sensitivity of the consumption process.  

In many concrete models of the individual consumption and portfolio decisions, the optimal consumption process will be of the form.  
$$
\begin{array}{r}{c_{t}=W_{t}e^{f(X_{t},t)},}\end{array}
$$  

where $W_{t}$ is the wealth of the individual at time $t$ $X_{t}$ is the time $t$ value of some state variable, and $f$ is some smooth function. Here $X$ can potentially be multi-dimensional..  

(b) Give some examples of variables other than wealth that may affect the optimal consumption of an individual and which may therefore play the role of. $X_{t}$  

Suppose the state variable $X$ is one-dimensional and write the dynamics of the wealth of the individual and the state variable as  
$$
\begin{array}{r l}&{d W_{t}=W_{t}\left[\left(\mu_{W t}-e^{f(X_{t},t)}\right)d t+\pmb{\sigma}_{W t}^{\top}d z_{t}\right],}\ &{d X_{t}=\mu_{X t}d t+\pmb{\sigma}_{X t}^{\top}d z_{t}}\end{array}
$$  

(c) Characterize the market price of risk in terms of the preference parameters and the drift and sensitivity terms of $W_{t}$ and $X_{t}$  

Hint: Apply Ito's Lemma to $c_{t}=W_{t}e^{f(X_{t},t)}$ to express the required parts of the consumption process in terms of $W$ and $X$  

(d) Show that the instantaneous excess expected rate of return on risky asset $i$ can be written as  
$$
\mu_{i t}+\delta_{i t}-r_{t}^{f}=\beta_{i W,t}\eta_{W t}+\beta_{i X,t}\eta_{X t},
$$  

where $\beta_{i W,t}$ and $\beta i X,t$ are the instantaneous beta's of the asset with respect to wealth and the state variable, respectively. Relate. $\eta_{W t}$ and $\eta_{X t}$ to preference parameters and the drift. and sensitivity terms of $W$ and $X$

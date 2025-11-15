---
tags:
- arbitrage
- artificial-intelligence
- bond-pricing
- coupon-bonds
- defi
- discount_function
- e-mini
- fixed-income
- fixed-income-derivatives
- forward-rates
- interest-rate-derivatives
- interest-rate-swap
- interest_rate
- irs
- ma
- markets
- martingale-theory
- mpt
- nim
- option-greeks
- options
- options-pricing
- ornstein_uhlenbeck
- risk-management
- rwa
- stochastic
- term-structure
- term_premium
- value-at-risk
- var
- vasicek-model
- zero_coupon_bond
aliases:
- Chapter 10 Exercises
- Exercises
key_concepts:
- Agricultural futures and seasonality
- Alternative investments and hedge fund strategies
- Arbitrage Pricing Theory (APT) and factor models
- Arbitrage and short rate
- Arbitrage pricing theory (APT)
- Asset swaps and spread-lock strategies
- Barrier options and knock-in/knock-out structures
- Basis swaps and cross-currency basis adjustments
- Basis swaps and floating rate correlations
- Behavioral finance and market anomalies
- Best execution and regulatory requirements
- Bid-ask spreads and market making profitability
- Binomial tree models for option pricing
- Black-Litterman model and portfolio optimization
- Bond portfolio immunization strategies
- Brownian motion and Wiener processes
- CDO structuring and tranche allocation methodologies
- CDO-squared structures and correlation trading
- Calendar spreads and roll strategies
- Central clearing and CCP risk management
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
- HJM and forward rate model frameworks
- Heath-Jarrow-Morton (HJM) framework
- Historical simulation and parametric VaR approaches
- Hull-White and Black-Karasinski short rate models
- IPO pricing and underpricing analysis
- Implied volatility and volatility surface modeling
- Inflation-linked swaps and CPI adjustments
- Interest rate derivatives and forward rate agreements
- Interest rate models and term structure
- Interest rate swaps and swap spread decomposition
- Interest rate uncertainty
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
- Negative interest rates and floor/cap structures
- Net interest margin and banking profitability
- Netting agreements and close-out procedures
- Nominal term structure
- Non-deliverable forwards and emerging market instruments
- OIS discounting and collateralized interest rate derivatives
- Options on futures and forward-starting options
- Payment systems and settlement risk
- Prime brokerage and securities lending
- Private credit and direct lending
- Project finance and syndicated lending
- Real estate investment trusts (REITs)
- Recovery rate modeling and loss given default
- Repo markets and securities lending
- Risk factor decomposition and sensitivity analysis
- Risk parity and risk budgeting strategies
- Risk-neutral valuation and martingale measures
- SAINTS model
- Shadow banking and non-bank intermediation
- Smart beta and alternative indexing approaches
- Spot rates, forward rates, and discount factor curves
- Stochastic volatility in interest rate markets
- Stress testing and scenario analysis frameworks
- Swaptions and interest rate option pricing
- Swaptions and option volatility surfaces
- Synthetic CDOs and credit-linked note structures
- Term premium and deflator
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
- Vasicek and Cox-Ingersoll-Ross models
- Volatility smile and skew patterns in option markets
- Working capital and cash conversion cycle
- Wrong-way risk and correlation adjustments
- Yield curve construction and term structure modeling
- Zero-coupon bond pricing and bootstrapping
enhanced: true
enhancement_date: '2025-11-06'
enhancement_id: batch04-971197
---




# 10.10 Exercises  

EXERCISE 10.1 Show that if there is no arbitrage and the short rate can never go negative,.   
then the discount function is non-increasing and all forward rates are non-negative.  

EXERCISE 10.2 Show Equation (10.51).  

EXERCISE 10.3 The term premium at time $t$ for the future period $[t^{\prime},T]$ is the current forward rate for that period minus the expected spot rate, i.e. $f_{t}^{t^{\prime},T}-\mathrm{E}_{t}[y_{t^{\prime}}^{T}]$ . This exercise will give a link between the term premium and a state-price deflator $\zeta=\left(\zeta_{t}\right)$  

(a) Show that  
$$
B_{t}^{T}=B_{t}^{t^{\prime}}\operatorname{E}_{t}\left[B_{t^{\prime}}^{T}\right]+\operatorname{Cov}_{t}\left[\frac{\zeta_{t^{\prime}}}{\zeta_{t}},\frac{\zeta_{T}}{\zeta_{t^{\prime}}}\right]
$$  

for any $t\leq t^{\prime}\leq T$  

(b) Using the above result, show that  
$$
\operatorname{E}_{t}\left[e^{-y_{t^{\prime}}^{T}(T-t^{\prime})}\right]-e^{-f_{t}^{t^{\prime},T}(T-t^{\prime})}=-{\frac{1}{B_{t}^{t^{\prime}}}}\operatorname{Cov}_{t}\left[{\frac{\zeta_{t^{\prime}}}{\zeta_{t}}},{\frac{\zeta_{T}}{\zeta_{t^{\prime}}}}\right].
$$  

Using the previous result and the approximation $e^{x}\approx1+x$ , show that  
$$
f_{t}^{t^{\prime},T}-\mathrm{E}_{t}[y_{t^{\prime}}^{T}]\approx-\frac{1}{(T-t^{\prime})B_{t}^{t^{\prime}}}\mathrm{Cov}_{t}\left[\frac{\zeta_{t^{\prime}}}{\zeta_{t}},\frac{\zeta_{T}}{\zeta_{t^{\prime}}}\right].
$$  

EXERCISE 10.4 The purpose of this exercise is to show that the claim of the gross return pure. expectation hypothesis is inconsistent with interest rate uncertainty. In the following we consider time points $t_{0}<t_{1}<t_{2}$  

(a) Show that if the hypothesis holds, then  
$$
\frac{1}{B_{t_{0}}^{t_{1}}}=\frac{1}{B_{t_{0}}^{t_{2}}}\operatorname{E}_{t_{0}}\left[B_{t_{1}}^{t_{2}}\right].
$$  

Hint: Compare two investment strategies over the period $[t_{0},t_{1}]$ .The first strategy is to buy.   
at time $t_{0}$ zero-coupon bonds maturing at time. $t_{1}$ .The second strategy is to buy at time. $t_{0}$   
zero-coupon bonds maturing at time $t_{2}$ and to sell them again at time. $t_{1}$  

(b) Show that if the hypothesis holds, then  
$$
\frac{1}{B_{t_{0}}^{t_{2}}}=\frac{1}{B_{t_{0}}^{t_{1}}}\operatorname{E}_{t_{0}}\left[\frac{1}{B_{t_{1}}^{t_{2}}}\right].
$$  

(c) Show from the two previous questions that the hypothesis implies that  
$$
\mathrm{E}_{t_{0}}\left[{\frac{1}{B_{t_{1}}^{t_{2}}}}\right]={\frac{1}{\mathrm{E}_{t_{0}}\left[B_{t_{1}}^{t_{2}}\right]}}.
$$  

(d) Show that ( $^*$ ) can only hold under full certainty. Hint: Use Jensen's inequality.  

EXERCISE 10.5 Show (10.63) and (10.64).  

EXERCISE 10.6 Go through the derivations in the subsection with the heading "An example" in Section 10.6.3.  

EXERCISE 10.7 Constantinides (1992) develops the so-called SAINTS model of the nominal term structure of interest rates by specifying exogenously the nominal state-price deflator. $\ddot{\zeta}$ . In a  

slightly simplified version, his assumption is that  
$$
\tilde{\zeta}_{t}=k e^{-g t+(X_{t}-\alpha)^{2}},
$$  

where $k$ $g$ , and $\alpha$ are constants, and $X=\left(X_{t}\right)$ follows the Ornstein-Uhlenbeck process  
$$
d X_{t}=-\kappa X_{t}d t+\sigma d z_{t},
$$  

where $\kappa$ and $\sigma$ are positive constants with $\sigma^{2}<\kappa$ and $z=\left(z_{t}\right)$ is a standard one-dimensional Brownian motion..  

(a) Derive the dynamics of the nominal state-price deflator. Express the nominal short-term interest rate, $\tilde{r}_{t}$ , and the nominal market price of risk, $\ddot{\lambda}_{t}$ , in terms of the variable $X_{t}$   
(b) Find the dynamics of the nominal short rate.   
(c) Find parameter constraints that ensure that the short rate stays positive? Hint: The short rate is a quadratic function of $X$ . Find the minimum value of this function.   
(d) What is the distribution of $X_{T}$ given $X_{t}$ \~.   
(e) Let $Y$ be a normally distributed random variable with mean $\mu$ and variance $v^{2}$ . Show that  
$$
\operatorname{E}\left[e^{-\gamma Y^{2}}\right]=(1+2\gamma v^{2})^{-1/2}\exp\left\{-{\frac{\gamma\mu^{2}}{1+2\gamma v^{2}}}\right\}.
$$  

(f) Use the results of the two previous questions to derive the time $t$ price of a nominal zero-. coupon bond with maturity. $T$ , i.e. $\tilde{B}_{t}^{T}$ . It will be an exponential-quadratic function of $X_{t}$ What is the yield on this bond?.  

(g) Find the percentage volatility. $\sigma_{t}^{T}$ of the price of the zero-coupon bond maturing at $T$  

(h) The instantaneous expected excess rate of return on the zero-coupon bond maturing at $T$ is often called the term premium for maturity. $T$ . Explain why the term premium is given by. $\sigma_{t}^{T}\ddot{\lambda}_{t}$ and show that the term premium can be written as.  
$$
4\sigma^{2}\alpha^{2}\left(1-F(T-t)\right)\left(\frac{X_{t}}{\alpha}-1\right)\left(\frac{X_{t}}{\alpha}-\frac{1-F(T-t)e^{\kappa(T-t)}}{1-F(T-t)}\right),
$$  

where  
$$
F(\tau)=\frac{1}{\frac{\sigma^{2}}{\kappa}+\left(1-\frac{\sigma^{2}}{\kappa}\right)e^{2\kappa\tau}}.
$$  

For which values of $X_{t}$ will the term premium for maturity $T$ be positive/negative? For a given state $X_{t}$ , is it possible that the the term premium is positive for some maturities and negative for others?  

EXERCISE 10.8 Assume a continuous-time economy where the state-price deflator $\zeta=\left(\zeta_{t}\right)$ has dynamics  
$$
d\zeta_{t}=-\zeta_{t}\left[r_{t}d t+\lambda d z_{1t}\right],
$$  

where $z_{1}=\left(z_{1t}\right)$ is a (one-dimensional) standard Brownian motion, $\lambda$ is a constant, and $\boldsymbol r=(r_{t})$ follows the Ornstein-Uhlenbeck process  
$$
d r_{t}=\kappa[\bar{r}-r_{t}]d t+\sigma_{r}d z_{1t}.
$$  

This is the Vasicek model so we know that the prices of zero-coupon bonds are given by (10.37) and the corresponding yields are given by (10.39).  

Suppose you want to value a real uncertain cash flow of $F_{T}$ coming at time $T$ . Let $x_{t}=\operatorname{E}_{t}[F_{T}]$ and assume that  
$$
d x_{t}=x_{t}\left[\mu_{x}d t+\sigma_{x}\rho d z_{1t}+\sigma_{x}\sqrt{1-\rho^{2}}d z_{2t}\right],
$$  

where $\mu_{x}$ $\sigma_{x}$ , and $\rho$ are constants, and where. $z_{2}~=~(z_{2t})$ is another (one-dimensional) standard Brownian motion independent of $z_{1}$  

(a) Argue that $x=\left(x_{t}\right)$ must be a martingale and hence that $\mu_{x}=0$  

(b) Show that the time $t$ value of the claim to the cash flow $F_{T}$ is given by  
$$
V_{t}\equiv V(t,r_{t},x_{t})=x_{t}e^{-A(T-t)-B(T-t)r_{t}},
$$  

where $B(\tau)=b(\tau)$ and  
$$
A(\tau)=a(\tau)+\rho\lambda\sigma_{x}\tau+\frac{\rho\sigma_{x}\sigma_{r}}{\kappa}\left(\tau-b(\tau)\right).
$$  

(c) Write the dynamics of $V=\left(V_{t}\right)$ as $d V_{t}=V_{t}[\mu_{t}^{V}d t+\sigma_{1t}^{V}d z_{1t}+\sigma_{2t}^{V}d z_{2t}]$ . Use $(^{*})$ to identify $\mu_{t}^{V}$ $\sigma_{1t}^{V}$ , and $\sigma_{2t}^{V}$ . Verify that $\mu_{t}^{V}=r_{t}+\left(\pmb{\sigma}_{t}^{V}\right)^{\top}\lambda_{t}$ , where ${\pmb\sigma}^{V}=(\sigma_{1}^{V},\sigma_{2}^{V})^{\top}$ and $\lambda$ is the market price of risk vector (the market price of risk associated with $z_{2}$ is zero! Why?).  

(d) Define the risk-adjusted discount rate. $R_{t}$ for the cash flow by the relation $V_{t}=\mathrm{E}_{t}[F_{T}]e^{-R_{t}[T-t]}$ What is the difference between $R_{t}$ and $y_{t}^{T}$ ? How does this difference depend on the cash flow payment date $T$  

EXERCISE 10.9 Consider an economy with complete financial markets and a representative agent with CRRA utility, u(C) = q'-z, , where $\gamma>0$ , and a time preference rate of $\delta$ .The aggregate consumption level $C$ is assumed to follow the stochastic process%20Process.md)  
$$
d c_{t}=c_{t}\left[\left(a_{1}X_{t}^{2}+a_{2}X_{t}+a_{3}\right)d t+\sigma_{c}d z_{t}\right],
$$  

where $z~=~\left(z_{t}\right)$ is a standard one-dimensional Brownian motion under the real-life probability measure $\mathbb{P}$ and where. $a_{1},a_{2},a_{3},\sigma_{c}$ are constants with $\sigma_{c}~>~0$ .Furthermore, $X~=~\left(X_{t}\right)$ is a stochastic process%20Process.md) with dynamics  
$$
d X_{t}=-\kappa X_{t}d t+d z_{t}.
$$  

where $\kappa$ is a positive constant.  

(a) Show that the short-term interest rate is of the form $r_{t}=d_{1}X_{t}^{2}+d_{2}X_{t}+d_{3}$ and determine the constants $d_{1},d_{2},d_{3}$  

(b) Find a parameter condition under which the short-term interest rate is always non-negative.  

(c) Write up the dynamics of $r_{t}$ (d) What is the market price of risk in this economy?  

Suppose that the above applies to the real economy and that money has no effects on the real economy. The consumer price index $F_{t}$ is supposed to have dynamics  
$$
d F_{t}=F_{t}\left[\mu_{\varphi t}d t+\rho_{C F}\sigma_{\varphi t}d z_{t}+\sqrt{1-\rho_{C F}^{2}}\sigma_{\varphi t}d\hat{z}_{t}\right],
$$  

where $\rho_{C F}$ is a constant correlation coefficient and $\hat{z}=(\hat{z}_{t})$ is another standard Brownian motion independent of $z$ . Assume that $\mu_{\varphi t}$ and $\sigma_{\varphi t}$ are on the form  
$$
\mu_{\varphi t}=b_{1}X_{t}^{2}+b_{2}X_{t}+b_{3},\qquad\sigma_{\varphi t}=k X_{t}.
$$  

(e) Write up an expression for the nominal short-term interest rate, $\tilde{r}_{t}$  

Assume in the rest of the problem that $\gamma a_{1}+b_{1}=k^{2}$  

(f) Show that the nominal short rate $\ddot{r}_{t}$ is affine in $X_{t}$ and express $X_{t}$ as an affine function of $\tilde{r}_{t}$   
(g) Compute the nominal market price of risk $\tilde{\lambda}_{t}$   
(h) Determine the dynamics of the nominal short rate. The drift and volatility should be expressed in terms of $\ddot{r}_{t}$ , not $X_{t}$

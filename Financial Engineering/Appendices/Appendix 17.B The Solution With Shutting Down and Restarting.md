---
academic_level: graduate
aliases:
- Appendix 17B
- Investment
- Restarting
- Shutting Down
cssclasses: academia
enhanced: true
enhancement_date: '2025-11-06'
enhancement_id: batch09-000418
key_concepts:
- Black-Scholes option pricing model and continuous-time finance
- Options Greeks and sensitivity analysis for risk management
- Duration analysis and interest rate risk management
- Convexity adjustments and yield curve sensitivity
- Sensitivity analysis and Greeks calculation
- Financial modeling and quantitative analysis
- Risk management and portfolio optimization
- Derivatives pricing and hedging strategies
- Market risk measurement and control
- Auto-Callable Notes and Barrier Options
- Value at Risk and Expected Shortfall
- Vasicek Interest Rate Model and Mean Reversion
- Short Rate Models and Term Structure Dynamics
- Credit Risk Management and Default Probability
- Expected Loss and Loss Given Default Models
- Equity-Linked Notes and Market-Linked Securities
- 'Greeks: Delta, Gamma, Theta, and Vega Hedging'
- Ornstein-Uhlenbeck Process in Finance
- Structured Products and Principal Protection
- Options Trading Strategies and Risk Management
- Stress Testing and Extreme Value Analysis
- Fama-French Factors and Style Analysis
- Risk Measurement and VaR Backtesting
- Contango, Backwardation, and Roll Yield
- Futures and Forward Contracts in Financial Markets
- Hedge Strategies and Basis Risk Management
- Option Valuation and Exercise Strategies
- Credit Spreads and Rating Migration Analysis
- Factor Models and Asset Pricing
- Arbitrage Pricing Theory and Multi-Factor Models
professional_application: theoreti
status: active
tags:
- asset-allocation
- binomial-model
- black-scholes-model
- continuous-time-pricing
- convexity
- convexity-adjustment
- credit-rating
- delta-hedging
- derivatives
- discrete-time-pricing
- duration-analysis
- dynamic-hedging
- fixed-income-sensitivity
- forward-contracts
- forward-pricing
- put-options
- barrier-options
- affine-term-structure
- recovery-rate
- hull-white
- call-options
- cir-model
- principal-protected-notes
- butterfly-spreads
- momentum
- strangles
- expected-shortfall
- straddles
- basis-risk
- parametric-var
- conditional-var
- extreme-value-theory
- var-methodologies
- historical-var
- book-to-market
- mean-reversion
- lognormal-models
- contango
- backwardation
- equity-linked-notes
- covered-calls
- ' exposure-at-default'
- style-analysis
- short-rate-models
- option-strategies
- stress-testing
- unexpected-loss
- ornstein-uhlenbeck
- rating-migration
- clearinghouse
- expected-loss
- investment-analysis
- credit-migration
- default-probability
- marking-to-market
- value-at-risk
- auto-callables
- credit-spreads
- arbitrage-pricing-theory
- multi-factor-models
- hedge-ratio
- structured-notes
- market-linked-notes
- iron-condors
- protective-puts
- market-price-of-risk
- financial-markets
- probabilty-of-default
- loss-given-default
- size-effect
- factor-models
- knock-out-options
- value-factor
- reverse-convertibles
- vasicek-model
- monte-carlo-var
- convergence
- options-trading
- var-backtesting
- futures-contracts
- roll-yield
- apt
- risk-premium
- fama-french
title: Appendix 17.B The Solution With Shutting Down and Restarting
type: note
---
--



# Appendix 17.B The Solution With Shutting Down and Restarting  

In this appendix we explain the solution of two problems: investing and operating (1) when it is possible to shut down once and restart once, permanently, and (2) when it is possible to shut down and restart an infinite number of times. The solutions here can be implemented numerically.  

First, we develop some notation. Let $V_U(S,m,n;*)$ represent the value of an undeveloped reserve and $V_O(S,m,n;*)$ and $V_C(S,m,n;*)$ the value of developed operating and developed closed reserves, where it is possible to shut down $m$ times and restart $n$ times. The $*$ denotes a dependence on the prices at which shutting and restarting is optimal. We will be using the formulas given by equations (12.22) and (12.23) for the value of $\$1$ when $S$ reaches a barrier.  

# Single Shutdown and Restart  

Prior to the final permanent restart at $S^*$, we have:

$$
V_C(S,0,1;S^*)=\left(\frac{S^*}{\delta}-\frac{c}{r}-k_r\right)\left(\frac{S}{S^*}\right)^{h_1}
$$  

We choose $S^*$ to maximize this expression.  

While operating, prior to the shutdown at $S_* < S$, we have:

$$
V_O(S,1,1;S_*,S^*)=\frac{S}{\delta}-\frac{c}{r}+\left[\frac{c}{r}-k_s-\frac{S_*}{\delta}+V_C(S_*,0,1;S^*)\right]\left(\frac{S}{S_*}\right)^{h_2}
$$  

We choose $S_*$ to maximize this expression, taking $S^*$ as determined by equation (17.15).  

Finally, prior to the original investment decision, which occurs at $\bar{S} > S$, the value of the well is:

$$
V_U(S, 1, 1; S_*, S^*)=\left[V_O(\bar{S}, 1, 1; S_*, S^*)-I\right]\left(\frac{S}{\bar{S}}\right)^{h_1}
$$  

We find the $\bar{S}$ that maximizes this equation, taking $S_*$ and $S^*$ as given, determined by maximizing equations (17.15) and (17.16).  

# Infinite Shutdown and Restart  

The solution here is conceptually like that in the single shutdown and restart case, except that when we restart, we receive the option to shut down. Thus, when the well is shut, we have:

$$
V_C(S,\infty,\infty;S_*,S^*)=\left[-k_r+V_O(S^*,\infty,\infty;S_*,S^*)\right]\left(\frac{S}{S^*}\right)^{h_1}
$$  

While operating, prior to the shutdown at $S > S_*$, we have:

$$
\begin{aligned}
V_O(S,\infty,\infty;S_*,S^*) &= \frac{S}{\delta}-\frac{c}{r}\\
&+ \left[\frac{c}{r}-k_s-\frac{S_*}{\delta}+V_C(S_*,\infty,\infty;S_*,S^*)\right]\left(\frac{S}{S_*}\right)^{h_2}
\end{aligned}
$$  

Note that $V_C$ and $V_O$ are defined in terms of each other. We can substitute equation (17.17) into equation (17.18) and set $S = S_*$. This gives:

$$
V_O(S^*,\infty,\infty;S_*,S^*)=\frac{S^*/\delta-c/r-k_r(S_*/S^*)^{h_1}+(c/r-S_*/\delta-k_s)\times(S^*/S_*)^{h_2}}{1-(S_*/S^*)^{h_1}\times(S^*/S_*)^{h_2}}
$$  

Given starting values of $S^*$ and $S_*$, we can evaluate equation (17.19), substituting the answer into equation (17.17) to obtain an estimate of $V_C(S,\infty,\infty;S_*,S^*)$. Then we can maximize equation (17.17) with respect to $S^*$ and equation (17.18) with respect to $S_*$. This gives us new estimates of $V_C(S_*)$ and $V_O(S^*)$. Iterate until convergence.  

Once we have computed $S^*$, $S_*$, and $V_C(S_*)$, the value of the well is:

$$
V_U(S,\infty,\infty;S_*,S^*)=\left[\frac{\bar{S}}{\delta}-\frac{c}{r}-I+V_C(S_*,\infty,\infty;S_*,S^*)\left(\frac{\bar{S}}{S_*}\right)^{h_2}\right]\left(\frac{S}{\bar{S}}\right)^{h_1}
$$  

We maximize this with respect to $\bar{S}$ to find the investment trigger and value of the well.

---
academic_level: graduate
aliases:
- Oil Well Drilling
- Optimal Drilling Time
cssclasses: academia
enhanced: true
enhancement_date: '2025-11-06'
enhancement_id: batch09-000419
key_concepts:
- Black-Scholes option pricing model and continuous-time finance
- Options Greeks and sensitivity analysis for risk management
- Duration analysis and interest rate risk management
- Convexity adjustments and yield curve sensitivity
- Risk preference theory and utility functions
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
- Forward Curves and Roll Strategies
- Structured Products and Principal Protection
- Options Trading Strategies and Risk Management
- Stress Testing and Extreme Value Analysis
- Fama-French Factors and Style Analysis
- Risk Measurement and VaR Backtesting
- Contango, Backwardation, and Roll Yield
- Futures and Forward Contracts in Financial Markets
- Hedge Strategies and Basis Risk Management
- Seasonality and Convenience Yield
- Commodity Markets and Energy Derivatives
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
- convexity-adjustment
- credit-rating
- crude-oil
- delta-hedging
- derivatives
- discrete-time-pricing
- duration-analysis
- dynamic-hedging
- energy-derivatives
- fixed-income-sensitivity
- forward-rates
- hull-white
- call-options
- cir-model
- butterfly-spreads
- expected-shortfall
- straddles
- extreme-value-theory
- book-to-market
- backwardation
- style-analysis
- option-strategies
- unexpected-loss
- clearinghouse
- arbitrage-pricing-theory
- hedge-ratio
- market-price-of-risk
- loss-given-default
- roll-strategies
- value-factor
- vasicek-model
- forward-curves
- monte-carlo-var
- options-trading
- commodity-trading
- forward-contracts
- fama-french
- recovery-rate
- parametric-var
- lognormal-models
- var-methodologies
- historical-var
- mean-reversion
- contango
- expected-loss
- market-linked-notes
- protective-puts
- probabilty-of-default
- reverse-convertibles
- storage-costs
- roll-yield
- risk-premium
- put-options
- affine-term-structure
- momentum
- basis-risk
- covered-calls
- ' exposure-at-default'
- stress-testing
- ornstein-uhlenbeck
- rating-migration
- investment-analysis
- value-at-risk
- metals-trading
- factor-models
- convenience-yield
- agricultural-commodities
- convergence
- var-backtesting
- barrier-options
- seasonality
- principal-protected-notes
- strangles
- conditional-var
- equity-linked-notes
- short-rate-models
- credit-migration
- default-probability
- marking-to-market
- auto-callables
- credit-spreads
- multi-factor-models
- structured-notes
- iron-condors
- financial-markets
- size-effect
- knock-out-options
- futures-contracts
- apt
title: Appendix 17.A Calculation of Optimal Time to Drill an Oil Well
type: note
---
--



# Appendix 17.A Calculation of Optimal Time to Drill an Oil Well
## Single-Barrel Solution

It is optimal to defer investing as long as:

$$\left(\frac{1}{1+r}\right)^h\left[S\left(\frac{1+r}{1+\delta}\right)^h-X\right]>S-X$$

Which can be rewritten as:

$$\frac{S}{X}<\frac{1-\left(\frac{1}{1+r}\right)^h}{1-\left(\frac{1}{1+\delta}\right)^h}$$

The optimal solution entails taking the limit as $h \to 0$. Using L'Hospital's rule, we can show that $\lim_{h \to 0}\frac{1-(1+r)^{-h}}{h}=\ln(1+r)$. Hence:

$$\frac{1-\left(\frac{1}{1+r}\right)^h}{1-\left(\frac{1}{1+\delta}\right)^h} \to \frac{\ln(1+r)}{\ln(1+\delta)}$$

Thus, we defer investing as long as:

$$\frac{S}{X}<\frac{\ln(1+r)}{\ln(1+\delta)}$$

In the text example this calculation gives $\$16.918$.

### THE SOLUTION WITH SHUTTING DOWN AND RESTARTING

In this appendix we explain the solution of two problems: investing and operating (1) when it is possible to shut down once and restart once, permanently, and (2) when it is possible to shut down and restart an infinite number of times. The solutions here can be implemented numerically. First, we develop some notation. Let $V_U(S, m, n; *)$ represent the value of an undeveloped reserve and $V_O(S, m, n; *)$ and $V_C(S, m, n; *)$ the value of developed operating and developed closed reserves, where it is possible to shut down $m$ times and restart $n$ times. The $*$ denotes a dependence on the prices at which shutting and restarting is optimal. We will be using the formulas given by equations (12.22) and (12.23) for the value of $\$1$ when $S$ reaches a barrier.

#### Single Shutdown and Restart

Prior to the final permanent restart at $S^*$, we have:

$$V_C(S, 0, 1; S^*)=\left(\frac{S^*}{\delta}-\frac{c}{r}-k_r\right)\left(\frac{S}{S^*}\right)^{h_1}$$

We choose $S^*$ to maximize this expression.

While operating, prior to the shutdown at $S_* < S$, we have:

$$V_O(S, 1, 1; S_*, S^*)=\frac{S}{\delta}-\frac{c}{r}+\left[\frac{c}{r}-k_s-\frac{S_*}{\delta}+V_C(S_*, 0, 1; S^*)\right]\left(\frac{S}{S_*}\right)^{h_2} \tag{17.16}$$

We choose $S_*$ to maximize this expression, taking $S^*$ as determined by equation (17.15). Finally, prior to the original investment decision, which occurs at $\bar{S} > S$, the value of the well is:

$$V_U(S, 1, 1; S_*, S^*)=\begin{bmatrix}V_O(\bar{S}, 1, 1; S_*, S^*)-I\end{bmatrix}\left(\frac{S}{\bar{S}}\right)^{h_1}$$

We find the $\bar{S}$ that maximizes this equation, taking $S_*$ and $S^*$ as given, determined by maximizing equations (17.15) and (17.16).

#### Infinite Shutdown and Restart

The solution here is conceptually like that in the single shutdown and restart case, except that when we restart, we receive the option to shut down. Thus, when the well is shut, we have:

$$V_C(S, \infty, \infty; S_*, S^*)=\begin{bmatrix}-k_r+V_O(S^*, \infty, \infty; S_*, S^*)\end{bmatrix}\left(\frac{S}{S^*}\right)^{h_1}$$

While operating, prior to the shutdown at $S > S_*$, we have:

$$\begin{aligned}
V_O(S, \infty, \infty; S_*, S^*) &= \frac{S}{\delta}-\frac{c}{r} \\
&+ \left[\frac{c}{r}-k_s-\frac{S_*}{\delta}+V_C(S_*, \infty, \infty; S_*, S^*)\right]\left(\frac{S}{S_*}\right)^{h_2}
\end{aligned}$$

Note that $V_C$ and $V_O$ are defined in terms of each other. We can substitute equation (17.17) into equation (17.18) and set $S = S_*$. This gives:

$$V_O(S^*, \infty, \infty; S_*, S^*)=\frac{S^*/\delta-c/r-k_r(S_*/S^*)^{h_1}+(c/r-S_*/\delta-k_s)\times(S^*/S_*)^{h_2}}{1-(S_*/S^*)^{h_1}\times(S^*/S_*)^{h_2}}$$

Given starting values of $S^*$ and $S_*$, we can evaluate equation (17.19), substituting the answer into equation (17.17) to obtain an estimate of $V_C(S, \infty, \infty; S_*, S^*)$. Then we can maximize equation (17.17) with respect to $S^*$ and equation (17.18) with respect to $S_*$. This gives us new estimates of $V_C(S_*)$ and $V_O(S^*)$. Iterate until convergence.

Once we have computed $S^*$, $S_*$, and $V_C(S_*)$, the value of the well is:

$$V_U(S, \infty, \infty; S_*, S^*)=\left[\frac{\bar{S}}{\delta}-\frac{c}{r}-I+V_C(S_*, \infty, \infty; S_*, S^*)\left(\frac{\bar{S}}{S_*}\right)^{h_2}\right]\left(\frac{S}{\bar{S}}\right)^{h_1}$$

We maximize this with respect to $\bar{S}$ to find the investment trigger and value of the well.

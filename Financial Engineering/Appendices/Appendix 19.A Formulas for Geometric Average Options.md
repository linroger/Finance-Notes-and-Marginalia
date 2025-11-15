---
aliases:
- Average Price Options
- Geometric Asian Options
- Geometric Average Options Formulas
cssclasses: academia
enhanced: true
enhancement_date: '2025-11-06'
enhancement_id: batch03-ec17e7
key_concepts:
- Geometric average price options
- Carry trades and momentum in FX markets
- Sovereign risk assessment and country analysis
- Mean-variance optimization and the efficient frontier
- Extreme value theory and tail risk modeling
- Credit risk modeling and default probability estimation
- Collateralized Debt Obligations
- Option Greeks and portfolio risk management
- Risk budgeting and portfolio construction techniques
- Mathematical derivation of the Black-Scholes partial differential equation
- Prepaid forward price
- Historical simulation vs. parametric VaR models
- Vega and volatility risk management
- option pricing models and PDE solutions
- DV01 calculation and interest rate risk hedging
- Average strike options
- Swap spread and credit risk considerations
- Mathematical Finance
- Monte Carlo integration and variance reduction
- Deposit insurance and systemic risk prevention
- Monte Carlo VaR for complex portfolios
- Stress testing and scenario analysis
- Fixed-for-floating swap cash flows and valuation
- Course Material
- portfolio optimization and risk decomposition
- Forward rates and interest rate parity
- Control variates and importance sampling techniques
- Theta and time decay modeling
- Risk-neutral pricing methodology for derivative securities
- Value at Risk (VaR) methodologies and backtesting
- Currency risk management and hedging
- Operational risk quantification and modeling
- Monte Carlo valuation
- Dividend Policy
- Exchange rate determination and PPP theory
- Arbitrage opportunities and risk-free profit extraction
- Expected Shortfall and coherent risk measures
- Interest rate swap pricing and valuation
- Black-Scholes formula
- Risk-neutral valuation in continuous time models
- Bank liquidity ratios and funding risk management
- Variance swaps and volatility trading strategies
- Boundary conditions and parameter interpretation in Black-Scholes model
- Limitations and extensions of the Black-Scholes framework
- simulation methods in financial engineering
- Value-at-Risk calculation using historical simulation
- risk measurement and management
- Gamma and convexity adjustments
- Credit risk migration matrices and rating transition
- Credit risk modeling and portfolio correlation analysis
- Backtesting procedures for risk models
- Credit risk assessment and loan portfolio management
- Delta hedging and the replication argument
- Liquidity risk measurement and management
- Cross-currency basis swaps and funding
- Systemic risk indicators and early warning systems
- Global financial stability and systemic risk monitoring
- Black-Scholes-Merton option pricing model and its applications
- Currency markets and foreign exchange trading
tags:
- financial-analysis
- average-strike-options
- dividend-policy
- collateralized-debt-obligations
- interest-rate-swaps
- mathematical-finance
- course-material
- var
- geometric-average-options
- asian-options
- monte-carlo-valuation
- financial-modeling
- black-scholes-formula
- greeks
- black-scholes-model
- value-at-risk
- exchange-rates
- credit-risk
- quantitative-implementation
- duration-convexity
- solution
- stress-testing
- liquidity-risk
- systemic-risk
- exotic-options
- deposit-insurance
- quantitative-finance
- expected-shortfall
- operational-risk
- monte-carlo
title: Appendix 19.A Formulas for Geometric Average Options
---

# Appendix 19.A Formulas for Geometric Average Options

The discussion of Monte Carlo valuation of geometrically averaged Asian options enables us to understand the formulas for geometrically averaged Asian options, described in Appendix 14.A. If we sample the stock price $N$ times from time 0 to $T$, with the distance between samples $h = T/N$ and the first sample occurring at time $h$, the log of the geometric average is:

$$\begin{aligned}
\frac{1}{N}\sum_{i=1}^{N}\ln(S_{ih}) &= \frac{1}{N}\left[\sum_{i=1}^{N}\left(\ln(S_0)+(r-\delta-0.5\sigma[^2])ih+\sigma\sum_{j=1}^{i}Z_j\sqrt{h}\right)\right] \\
&= \ln(S_0)+(r-\delta-0.5\sigma[^2])\frac{h}{N}\sum_{i=1}^{N}i+\frac{\sigma\sqrt{h}}{N}\sum_{i=1}^{N}\sum_{j=1}^{i}Z_j
\end{aligned}$$

Where $Z_j \sim \mathcal{N}(0, 1)$ and $Z_i$ and $Z_j$ are independent. The last double summation can be rewritten as:

$$\sum_{i=1}^N\sum_{j=1}^i Z_j = NZ_1 + (N-1)Z_2 + \cdots + Z_N$$

Thus, we have:

$$\begin{aligned}
\operatorname{E}\left[\frac{1}{N}\sum_{i=1}^{N}\ln(S_{ih})\right] &= \ln(S_0)+(r-\delta-0.5\sigma[^2])\frac{h}{N}\frac{N(N+1)}{2} \\
&= \ln(S_0)+(r-\delta-0.5\sigma[^2])T\frac{N+1}{2N}
\end{aligned}$$

Where we have used the fact that:

$$\sum_{i=1}^N i = \frac{N(N+1)}{2}$$

The variance is:

$$\begin{aligned}
\operatorname{Var}\left[\frac{1}{N}\sum_{i=1}^{N}\ln(S_{ih})\right] &= \frac{\sigma[^2] h}{N[^2]}\left(N[^2]+(N-1)[^2]+\cdots+1\right) \\
&= \sigma[^2] T\frac{N(N+1)(2N+1)}{6N[^3]}
\end{aligned}$$

Where we have used the fact that:

$$\sum_{i=1}^N i[^2] = \frac{N(N+1)(2N+1)}{6}$$

These calculations tell us that the average price, $G(T)$, can be written as a lognormal process:

$$G(T) = S_0 e^{\left[(r-\delta-0.5\sigma[^2])\frac{T}{2}\frac{N+1}{N}+\sigma\sqrt{T}\sqrt{\frac{(N+1)(2N+1)}{6N[^2]}}Z\right]}$$

Where $Z \sim \mathcal{N}(0, 1)$. Using equation (18.13), we have:

$$\operatorname{E}[G(T)] = S_0 e^{\left[(r-\delta-0.5\sigma[^2])\frac{N+1}{N}+\sigma[^2]\frac{(N+1)(2N+1)}{6N[^2]}\right]\frac{T}{2}}$$

The prepaid forward price for the average is:

$$e^{-rT}\mathrm{E}[G(T)] = S_0 e^{-\left[r\frac{N-1}{N}+(\delta+0.5\sigma[^2])\frac{N+1}{N}-\sigma[^2]\frac{(N+1)(2N+1)}{6N[^2]}\right]\frac{T}{2}}$$

Thus, we can price an option on the geometric average by setting the dividend yield for the average, $\delta^*$, equal to:

$$\delta^* = \frac{1}{2}\left[r\frac{N-1}{N}+(\delta+0.5\sigma[^2])\frac{N+1}{N}-\sigma[^2]\frac{(N+1)(2N+1)}{6N[^2]}\right]$$

And the volatility of the average, $\sigma^*$, equal to:

$$\sigma^* = \frac{\sigma}{N}\sqrt{\frac{(N+1)(2N+1)}{6}}$$

If we take the limit as $N \rightarrow \infty$, we have:

$$\begin{aligned}
&\delta^* = \frac{1}{2}\left(r+\delta+\frac{1}{6}\sigma[^2]\right)\\
&\sigma^* = \sigma\sqrt{\frac{1}{3}}
\end{aligned}$$

## Average Price Options

Geometric average price options, for which the geometric average replaces the stock price, are priced by substituting $\delta^*$ and $\sigma^*$ for $\delta$ and $\sigma$ in the Black-Scholes formula.

## Average Strike Options

With geometric average strike options, the average replaces the strike price. Thus, we replace the risk-free rate with $\delta^*$ and the strike price with $S_0$. However, we also need to compute the volatility of the difference between $\ln(S_T)$ and $\ln(A(T))$:

$$\sigma^{**2} = \mathrm{Var}[\ln(S_T)-\ln(A_T)]$$

We can write:

$$\ln(S_T) = \ln(S_0) + (r-\delta-0.5\sigma[^2])T + \sigma\sum_{i=1}^N Z_i\sqrt{h}$$

Using equation (19.19), the covariance between $\ln(S_T)$ and $\ln(A_T)$ is:

$$\begin{aligned}
\operatorname{E}\left[\left(\sigma\sqrt{h}\sum_{i=1}^{N}Z_i\right)\left(\frac{\sigma\sqrt{h}}{N}\sum_{i=1}^{N}\sum_{j=1}^{i}Z_j\right)\right] &= \frac{\sigma[^2] h}{N}\left(\sum_{i=1}^{N}Z_i\right)\left(\sum_{i=1}^{N}\sum_{j=1}^{i}Z_j\right) \\
&= \frac{\sigma[^2] h}{N}(N+(N-1)+\cdots+1) \\
&= \frac{\sigma[^2] h}{2}(N+1)
\end{aligned}$$

The correlation coefficient, $\rho$, is therefore:

$$\begin{aligned}
\rho &= \frac{\frac{\sigma[^2] h}{2}(N+1)}{\left(\sigma\sqrt{T}\right)\left(\sigma\sqrt{T}\frac{1}{N}\sqrt{\frac{(N+1)(2N+1)}{6}}\right)}\\
&= \frac{1}{2}\sqrt{\frac{6(N+1)}{2N+1}}
\end{aligned}$$

Note that when $N = 1$, $\rho = 1$, and as $N \to \infty$, $\rho = \sqrt{3}/2$. Using this expression for $\rho$, we have:

$$\sigma^{**2} = \sigma[^2] T + \sigma[^2] T\frac{(N+1)(2N+1)}{6N[^2]} - 2\rho\sigma[^2] T\frac{1}{N}\sqrt{\frac{(N+1)(2N+1)}{6}}$$

Thus, to value an average strike option we substitute $\sigma^{**}$ for the volatility and $\delta^*$ for the interest rate. The dividend yield on the underlying asset remains the same.

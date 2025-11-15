---
academic_level: graduate
aliases:
- Average Price Options
- Geometric Asian Options
- Geometric Average Options Formulas
cssclasses: academia
enhanced: true
enhancement_date: '2025-11-06'
enhancement_id: batch09-000426
key_concepts:
- Black-Scholes option pricing model and continuous-time finance
- Monte Carlo simulation for derivatives pricing and risk management
- Options Greeks and sensitivity analysis for risk management
- Duration analysis and interest rate risk management
- Convexity adjustments and yield curve sensitivity
- Discounted cash flow (DCF) valuation methodology
- Weighted Average Cost of Capital (WACC) and firm valuation
- Credit default swaps (CDS) and credit risk modeling
- Value at Risk (VaR) and tail risk measurement
- Expected shortfall and coherent risk measures
- Collateralized debt obligations (CDO) and tranche structure
- Volatility modeling and estimation techniques
- Correlation analysis and dependency structures
- Risk preference theory and utility functions
- Sensitivity analysis and Greeks calculation
- 'Valuation Methods: DCF, Comps, and Precedents'
- Value at Risk and Expected Shortfall
- Vasicek Interest Rate Model and Mean Reversion
- Short Rate Models and Term Structure Dynamics
- Company Valuation and Multiple Analysis
- Variance Reduction Techniques in Monte Carlo Methods
- Comparable Company Analysis and Trading Multiples
- 'Greeks: Delta, Gamma, Theta, and Vega Hedging'
- Ornstein-Uhlenbeck Process in Finance
- Stochastic Integration and Path-Dependent Options
- Options Trading Strategies and Risk Management
- Stress Testing and Extreme Value Analysis
- Fama-French Factors and Style Analysis
- Risk Measurement and VaR Backtesting
- Contango, Backwardation, and Roll Yield
- Futures and Forward Contracts in Financial Markets
- Factor Models and Asset Pricing
- Hedge Strategies and Basis Risk Management
- Option Valuation and Exercise Strategies
- Monte Carlo Simulation Methods for Derivative Pricing
- Arbitrage Pricing Theory and Multi-Factor Models
professional_application: theoreti
status: active
tags:
- asian-derivatives
- average-price-options
- binomial-model
- black-scholes-model
- capital-structure
- caplet
- cash-flow-modeling
- cds
- coherent-risk-measure
- collateralized-debt-obligation
- conditional-var
- continuous-time-pricing
- convexity-adjustment
- cost-of-capital
- counterparty-risk
- control-variates
- put-options
- leveraged-buyout
- exotic-options
- affine-term-structure
- sum-of-parts
- call-options
- variance-reduction
- price-to-earnings
- cir-model
- hull-white
- butterfly-spreads
- momentum
- strangles
- dcf-analysis
- expected-shortfall
- straddles
- basis-risk
- parametric-var
- extreme-value-theory
- var-methodologies
- historical-var
- book-to-market
- mean-reversion
- lognormal-models
- contango
- backwardation
- antithetic-variates
- random-walks
- covered-calls
- volatility-analysis
- style-analysis
- short-rate-models
- least-squares-mc
- option-strategies
- stress-testing
- ornstein-uhlenbeck
- comparable-analysis
- clearinghouse
- economic-value-added
- marking-to-market
- path-dependency
- value-at-risk
- arbitrage-pricing-theory
- monte-carlo-simulation
- hedge-ratio
- multi-factor-models
- trading-multiples
- iron-condors
- protective-puts
- market-price-of-risk
- size-effect
- factor-models
- precedent-transactions
- value-factor
- vasicek-model
- ipo-valuation
- monte-carlo-var
- risk-management
- convergence
- options-trading
- var-backtesting
- futures-contracts
- market-multiple
- roll-yield
- quasi-monte-carlo
- apt
- risk-premium
- stochastic-integration
- forward-contracts
- fama-french
title: Appendix 19.A Formulas for Geometric Average Options
type: note
---
--



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

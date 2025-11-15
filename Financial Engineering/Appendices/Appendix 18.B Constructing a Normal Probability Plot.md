---
aliases:
- NPP
- Normal Probability Plot
cssclasses: academia
enhanced: true
enhancement_date: '2025-11-06'
enhancement_id: batch03-46f294
key_concepts:
- Cumulative inverse function
- Deposit Insurance
- Sovereign risk assessment and country analysis
- Mean-variance optimization and the efficient frontier
- Extreme value theory and tail risk modeling
- Compare data quantiles
- Credit risk modeling and default probability estimation
- Wholesale funding markets and maturity transformation
- Funding liquidity vs. market liquidity
- Risk budgeting and portfolio construction techniques
- Solution
- Historical simulation vs. parametric VaR models
- Credit portfolio diversification and concentration
- DV01 calculation and interest rate risk hedging
- Portfolio immunization strategies
- Mathematical Finance
- Monte Carlo integration and variance reduction
- Deposit insurance and systemic risk prevention
- Monte Carlo VaR for complex portfolios
- Stress testing and scenario analysis
- Key rate duration and curve risk
- Course Material
- Control variates and importance sampling techniques
- Value at Risk (VaR) methodologies and backtesting
- Risk-neutral pricing methodology for derivative securities
- Case Study
- Normal probability plot
- Operational risk quantification and modeling
- Arbitrage opportunities and risk-free profit extraction
- Expected Shortfall and coherent risk measures
- Standard normal distribution
- Liquidity risk management in financial institutions
- Bank liquidity ratios and funding risk management
- Credit exposure measurement and EAD
- Loss given default and recovery rates
- Operational risk management in financial institutions
- Wrong-way risk in derivative transactions
- Stress Testing
- Systemic risk and financial stability
- Deposit stability and core funding
- Value-at-Risk calculation using historical simulation
- Quantitative Implementation
- Credit risk migration matrices and rating transition
- Expected Shortfall
- Credit risk modeling and portfolio correlation analysis
- Backtesting procedures for risk models
- Credit risk assessment and loan portfolio management
- Liquidity risk measurement and management
- Duration and convexity measures for bond portfolios
- Systemic risk indicators and early warning systems
- Global financial stability and systemic risk monitoring
- Price sensitivity to interest rate changes
- Data point plotting
- Modified duration vs. Macaulay duration
- Liquidity stress testing and contingency funding plans
tags:
- financial-analysis
- probability-plot
- mathematical-finance
- course-material
- financial-modeling
- quantile
- case-study
- value-at-risk
- normal-distribution
- credit-risk
- quantitative-implementation
- duration-convexity
- solution
- stress-testing
- liquidity-risk
- systemic-risk
- cumulative-inverse
- deposit-insurance
- data-analysis
- quantitative-finance
- expected-shortfall
- operational-risk
- monte-carlo
title: Appendix 18.B Constructing a Normal Probability Plot
---

# Appendix 18.B Constructing a Normal Probability Plot

This appendix discusses the details of constructing the normal probability plot for the data in Example 18.9. The idea of the normal probability plot is to compare the quantiles of the data with the corresponding quantiles of the normal distribution. Because the shape of the normal distribution is the same whatever the mean and variance, we know that the relative distance of normal quantiles will be the same for any normal distribution. For a $\mathcal{N}(0, 1)$ distribution, the cumulative inverse distribution function tells us which $x$ value corresponds to a particular quantile. For example, $N^{-1}(0.1) = -1.282$ and $N^{-1}(0.3) = -0.524$. The distance between the $x$ values that give rise to the data quantiles is:

$$\begin{gathered}
N^{-1}(0.3)-N^{-1}(0.1) = 0.757 \\
N^{-1}(0.5)-N^{-1}(0.3) = 0.524 \\
N^{-1}(0.7)-N^{-1}(0.5) = 0.524 \\
N^{-1}(0.9)-N^{-1}(0.7) = 0.757 
\end{gathered}$$

The lesser distance between quantiles closer to the median reflects the shape of the normal distribution. If the data come from a normal distribution, the relative distance between data points at these quantiles will have the same relative distances. The procedure in creating Figure 18.5 is to plot the data points on the x-axis against the values from a $\mathcal{N}(0, 1)$ distribution with the same quantiles. Thus, we plot the data point with quantile $q$ against $N^{-1}(q)$. In the case of the five sample data points, we plot the points $(3, -1.282)$, $(4, -0.524)$, $(5, 0)$, $(7, 0.524)$ and $(11, 1.282)$. These points are plotted in the top left panel of Figure 18.6. The y-axis is labeled "z-value" since these are values from a standard normal distribution. The top right panel is exactly the same, except that the y-axis is labeled with probabilities corresponding to the z-values. The data do not appear normal, though with only five points there is a large possibility for error.

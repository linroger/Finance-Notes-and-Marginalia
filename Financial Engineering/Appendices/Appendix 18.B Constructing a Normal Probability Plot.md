---
academic_level: graduate
aliases:
- NPP
- Normal Probability Plot
cssclasses: academia
enhanced: true
enhancement_date: '2025-11-06'
enhancement_id: batch09-000425
key_concepts:
- Value at Risk (VaR) and tail risk measurement
- Expected shortfall and coherent risk measures
- Financial modeling and quantitative analysis
- Risk management and portfolio optimization
- Derivatives pricing and hedging strategies
- Market risk measurement and control
- Risk Measurement and VaR Backtesting
- Ornstein-Uhlenbeck Process in Finance
- Value at Risk and Expected Shortfall
- Vasicek Interest Rate Model and Mean Reversion
- Short Rate Models and Term Structure Dynamics
- Factor Models and Asset Pricing
- Stress Testing and Extreme Value Analysis
- Fama-French Factors and Style Analysis
- Arbitrage Pricing Theory and Multi-Factor Models
professional_application: theoreti
status: active
tags:
- asset-allocation
- coherent-risk-measure
- conditional-var
- credit-rating
- expected-loss
- hedging
- investment-grade
- linear-regression
- low-default-risk
- portfolio-management
- regression-analysis
- risk-management
- risk-measures
- statistical-modeling
- tail-risk
- affine-term-structure
- hull-white
- cir-model
- momentum
- expected-shortfall
- parametric-var
- extreme-value-theory
- book-to-market
- lognormal-models
- var-methodologies
- historical-var
- mean-reversion
- style-analysis
- short-rate-models
- stress-testing
- ornstein-uhlenbeck
- value-at-risk
- arbitrage-pricing-theory
- multi-factor-models
- market-price-of-risk
- size-effect
- factor-models
- value-factor
- vasicek-model
- monte-carlo-var
- var-backtesting
- apt
- risk-premium
- fama-french
title: Appendix 18.B Constructing a Normal Probability Plot
type: note
---
--



# Appendix 18.B Constructing a Normal Probability Plot

This appendix discusses the details of constructing the normal probability plot for the data in Example 18.9. The idea of the normal probability plot is to compare the quantiles of the data with the corresponding quantiles of the normal distribution. Because the shape of the normal distribution is the same whatever the mean and variance, we know that the relative distance of normal quantiles will be the same for any normal distribution. For a $\mathcal{N}(0, 1)$ distribution, the cumulative inverse distribution function tells us which $x$ value corresponds to a particular quantile. For example, $N^{-1}(0.1) = -1.282$ and $N^{-1}(0.3) = -0.524$. The distance between the $x$ values that give rise to the data quantiles is:

$$\begin{gathered}
N^{-1}(0.3)-N^{-1}(0.1) = 0.757 \\
N^{-1}(0.5)-N^{-1}(0.3) = 0.524 \\
N^{-1}(0.7)-N^{-1}(0.5) = 0.524 \\
N^{-1}(0.9)-N^{-1}(0.7) = 0.757 
\end{gathered}$$

The lesser distance between quantiles closer to the median reflects the shape of the normal distribution. If the data come from a normal distribution, the relative distance between data points at these quantiles will have the same relative distances. The procedure in creating Figure 18.5 is to plot the data points on the x-axis against the values from a $\mathcal{N}(0, 1)$ distribution with the same quantiles. Thus, we plot the data point with quantile $q$ against $N^{-1}(q)$. In the case of the five sample data points, we plot the points $(3, -1.282)$, $(4, -0.524)$, $(5, 0)$, $(7, 0.524)$ and $(11, 1.282)$. These points are plotted in the top left panel of Figure 18.6. The y-axis is labeled "z-value" since these are values from a standard normal distribution. The top right panel is exactly the same, except that the y-axis is labeled with probabilities corresponding to the z-values. The data do not appear normal, though with only five points there is a large possibility for error.

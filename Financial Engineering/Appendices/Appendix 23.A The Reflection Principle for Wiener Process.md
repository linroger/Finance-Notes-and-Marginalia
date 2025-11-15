---
academic_level: graduate
aliases:
- Brownian Path
- Reflection Principle
enhanced: true
enhancement_date: '2025-11-06'
enhancement_id: batch09-000431
key_concepts:
- Black-Scholes option pricing model and continuous-time finance
- Options Greeks and sensitivity analysis for risk management
- Wiener process and Brownian motion modeling
- Duration analysis and interest rate risk management
- Convexity adjustments and yield curve sensitivity
- Value at Risk (VaR) and tail risk measurement
- Expected shortfall and coherent risk measures
- Risk preference theory and utility functions
- Sensitivity analysis and Greeks calculation
- Auto-Callable Notes and Barrier Options
- Risk Measurement and VaR Backtesting
- Equity-Linked Notes and Market-Linked Securities
- 'Greeks: Delta, Gamma, Theta, and Vega Hedging'
- Ornstein-Uhlenbeck Process in Finance
- Value at Risk and Expected Shortfall
- Option Valuation and Exercise Strategies
- Factor Models and Asset Pricing
- Vasicek Interest Rate Model and Mean Reversion
- Short Rate Models and Term Structure Dynamics
- Structured Products and Principal Protection
- Options Trading Strategies and Risk Management
- Stress Testing and Extreme Value Analysis
- Fama-French Factors and Style Analysis
- Arbitrage Pricing Theory and Multi-Factor Models
professional_application: theoreti
status: active
tags:
- binomial-model
- black-scholes-model
- brownian-motion
- capital-budgeting
- caplet
- coherent-risk-measure
- conditional-var
- continuous-time-pricing
- convexity-adjustment
- credit-rating
- delta-hedging
- derivatives
- discrete-time-pricing
- duration-analysis
- dynamic-hedging
- put-options
- barrier-options
- affine-term-structure
- hull-white
- call-options
- cir-model
- principal-protected-notes
- butterfly-spreads
- momentum
- strangles
- expected-shortfall
- straddles
- parametric-var
- extreme-value-theory
- book-to-market
- var-methodologies
- historical-var
- mean-reversion
- lognormal-models
- equity-linked-notes
- volatility-analysis
- covered-calls
- style-analysis
- short-rate-models
- option-strategies
- stress-testing
- ornstein-uhlenbeck
- value-at-risk
- auto-callables
- arbitrage-pricing-theory
- multi-factor-models
- structured-notes
- market-linked-notes
- iron-condors
- protective-puts
- market-price-of-risk
- size-effect
- factor-models
- knock-out-options
- value-factor
- reverse-convertibles
- vasicek-model
- monte-carlo-var
- risk-management
- var-backtesting
- options-trading
- apt
- risk-premium
- fama-french
title: Appendix 23. A The Reflection Principle for Wiener Process
type: note
---
--



# Appendix 23. A The Reflection Principle for Wiener Process

For every standard Brownian path there is an equally likely path that can be constructed by reflecting the path,  or a portion of the path,  with respect to a horizontal line. Figure 23.5 shows a Brownian path,  $X_{r}$ ,  denoted by ABC,  that is reflected beginning at the poin where the path reaches $X_{t}=70$ .Notice that the path BD is a mirror image,  reflected vertically around the line $X=70$ ,  of the original path BC. We will see that by considering the reflected path,  it is possible to transform barrier probability calculations into standard normal probability calculations

Suppose we have a Brownian motion that starts at $X_{0}$ and follows the process
$$dX_{t}=\sigma dZ_{t}$$

Thus,  $X_{I}$ is normally distributed with mean $X_{0}$ and variance $\sigma^{2}T$ .We want to know the joint probability that at time $T,      X_{T}$ will have hit the barrier $H<X_{0}$ and will also be above the level $K\geq H$ . If we let $\underline{X}_{\mathrm{r}}$ denote the lowest value of $X$ between O and $I$ ,  we wish to compute the joint probability
$$\Pr (X_{T}>K,      \underline{X}_{T}\leq H)$$

## FIGURE 23.5

Illustration of refection principle. Original path is ABC. Path reflected about a barrier of 70 is ABD

 !500

The probability here is analogous to that in equation (23.6). If $X$ were the price of an asset this probability discounted at the risk-free rate would be the price of a down-and-in cash call. Suppose that $X_0=80$ $H=70$ ,  and $K=100$ Consider the actual Brownian path in

Figure 23.5 depicted by the letters ABC. This path starts at “A,  ” hits the barrier level of 70 at about time 1.25 (designated by the letter “B"),  and then ends at 104.66 ("C). ABC is an example of the path that satisfies our conditions. (A probability calculation for a Brownian motion essentially consists of asking what fraction of the possible paths satisfy specific conditions.) Now consider the path ABD. This path also starts at A and hits the barrier at B,  but

After point B it is the mirror image of ABC,  reflected about the barrier level of 70. The reflection principle in this context says that for any path that starts at 80,  hits 70 and ends up above 100,  there is an equally likely path that starts at 80,  hits 70,  and ends up below 40. Because they occur with the same probability,  it does not matter whether we count paths like ABC or paths like ABD. But paths like ABD are easier to count The fraction of paths that start at 80,  hit 70,  and end up above 100 equals the fraction

Of paths that start at 80,  hit 70,  and end up below 40. But for this second set of paths,  hitting 70 is a redundant condition: Any path ending below 40 will have hit 70 along the way. The hitting condition does not matter in computing the probability using the reflected path

The level 40 in this example can be expressed as$$\begin{array}{c}70-(100-70)=H-(K-H)\\=2 H-K\end{array}$$
Thus,  the fraction of Brownian paths which satisfy our conditions is$$\Pr (X_{t}>K\:,      \underline{X}_{t}\leq H)=\Pr (X_{T}<2 H-K)$$
This is a standard normal probability calculation:$$\begin{aligned}
\operatorname*{Pr}(X_{T}<2 H-K)& =\mathrm{Pr}\left (\frac{X_{T}-X_{0}}{\sigma\sqrt{T}}\leq\frac{2 H-K-X_{0}}{\sigma\sqrt{T}}\right) \\
&=N\left (\frac{2 H-K-X_{0}}{\sigma\sqrt{T}}\right)
\end{aligned}$$
Because of the reflection principle,      the calculation with the hitting boundary involves only a standard normal calculation.

Example 23.1 Suppose $X_{0}=80,      \sigma=10$ ,      $H=70$ $K=100$ ,      and $T=5$ years. We have$$\begin{aligned}
\Pr (X_{T}>100,      \underline{X}_{T}\leq 70 | X_{0}=80)& =N\left ({\frac{2\times 70-100-80}{10{\sqrt{5}}}}\right) \\
&=N (-1.7889)=0.0368\:\equiv 
\end{aligned}$$
If we wish to calculate $\Pr (X_{T}>100,      \underline{X}_{T}>70)$ (the probability that a knockout call will pay off),      we can use the fact that hitting and not hitting are mutually exclusive events. Thus,      $$\begin{aligned}
\mathrm{Pr}(X_{T}>K,      \underline{X}_{T}>H)& =\mathrm{Pr}(X_{T}>K)-\mathrm{Pr}(X_{T}>K,      \underline{X}_{T}\leq H) \\
&=N\left (\frac{X_{0}-K}{\sigma\sqrt{T}}\right)-N\left (\frac{2 H-K-X_{0}}{\sigma\sqrt{T}}\right)
\end{aligned}$$

The actual barrier formulas differ in two respects from equations (23.48) and (23.49) First,      with geometric Brownian motion,      $\ln (X_{t})$ is normally distributed rather than $X_{t}$ .This results in $X_{0}$ ,      $K$ ,      $H$ ,      being replaced with $\ln (X_{0})$ ,      etc.

More importantly,      we assumed that $X$ was a Brownian motion with no drift. The construction of the reflection depends crucially on this assumption. By rewriting equatior 23.6,      however,      you can see that it reduces to equation (23.48) when $r-\delta-0.5\sigma^{2}=0$ (the logarithmic drift is zero):
$$\exp\left (2\frac{r-\delta-0.5\sigma[^2]}{\sigma[^2]}\ln (H/S)\right) N\left[\frac{2\ln (H)-\ln (S)-\ln (K)+(r-\delta-0.5\sigma[^2]) T}{\sigma\sqrt{T}}\right]$$

The incorporation of drift into barrier problems is discussed in Harrison (1985) and Steele (2010).

## References

Harrison,      J. M.,      1985,      Brownian Motion and Stochastic Flow Systems,      John Wiley & Sons,      New York

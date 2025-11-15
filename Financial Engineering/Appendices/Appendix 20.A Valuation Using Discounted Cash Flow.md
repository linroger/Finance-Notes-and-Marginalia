---
academic_level: graduate
aliases:
- DCF Valuation
- Discounted Cash Flow
enhanced: true
enhancement_date: '2025-11-06'
enhancement_id: batch09-000428
key_concepts:
- Black-Scholes option pricing model and continuous-time finance
- Options Greeks and sensitivity analysis for risk management
- Risk-neutral measures and martingale pricing
- Martingale theory and change of measure
- Convexity adjustments and yield curve sensitivity
- Discounted cash flow (DCF) valuation methodology
- Capital Asset Pricing Model (CAPM) and expected returns
- Weighted Average Cost of Capital (WACC) and firm valuation
- Value at Risk (VaR) and tail risk measurement
- Arbitrage opportunities and no-arbitrage pricing
- Sharpe ratio and risk-adjusted performance measurement
- Alpha generation and active portfolio management
- Factor models and multi-factor pricing
- Alpha generation and active return measurement
- Risk preference theory and utility functions
- Sensitivity analysis and Greeks calculation
- 'Valuation Methods: DCF, Comps, and Precedents'
- Ito's Lemma and Lognormal Asset Price Dynamics
- Risk-Neutral Valuation in Option Pricing
- Free Cash Flow and Enterprise Value
- Value at Risk and Expected Shortfall
- Vasicek Interest Rate Model and Mean Reversion
- Short Rate Models and Term Structure Dynamics
- Company Valuation and Multiple Analysis
- Capital Asset Pricing Model and Beta Analysis
- Credit Risk Management and Default Probability
- Expected Loss and Loss Given Default Models
- Comparable Company Analysis and Trading Multiples
- 'Greeks: Delta, Gamma, Theta, and Vega Hedging'
- Ornstein-Uhlenbeck Process in Finance
- Cost of Equity and Expected Returns
- Black-Scholes Option Pricing Model and Its Applications
- Security Market Line and Risk-Return Tradeoff
- Options Trading Strategies and Risk Management
- Stress Testing and Extreme Value Analysis
- Fama-French Factors and Style Analysis
- Risk Measurement and VaR Backtesting
- Option Valuation and Exercise Strategies
- Credit Spreads and Rating Migration Analysis
- Factor Models and Asset Pricing
- Terminal Value and WACC Calculations
- Discounted Cash Flow Valuation Models
- Arbitrage Pricing Theory and Multi-Factor Models
professional_application: theoreti
status: active
tags:
- arbitrage-opportunity
- arbitrage-pricing
- asset-allocation
- binomial-model
- black-scholes-model
- capital-asset-pricing
- capital-structure
- caplet
- cash-flow-modeling
- continuous-time-pricing
- convexity-adjustment
- cost-of-capital
- credit-rating
- dcf-valuation
- delta-hedging
- leveraged-buyout
- hull-white
- call-options
- cir-model
- terminal-value
- free-cash-flow
- butterfly-spreads
- dcf-analysis
- expected-shortfall
- straddles
- extreme-value-theory
- book-to-market
- partial-differential-equation
- risk-neutral-valuation
- volatility-analysis
- style-analysis
- option-strategies
- unexpected-loss
- capital-asset-pricing-model
- enterprise-value
- arbitrage-pricing-theory
- market-price-of-risk
- volatility-surface
- loss-given-default
- value-factor
- vasicek-model
- sharpe-ratio
- monte-carlo-var
- capital-budgeting
- options-trading
- fama-french
- price-to-earnings
- bsm-model
- recovery-rate
- black-scholes-formula
- parametric-var
- lognormal-models
- var-methodologies
- historical-var
- mean-reversion
- expected-loss
- wacc
- systematic-risk
- protective-puts
- alpha
- security-market-line
- probabilty-of-default
- discounted-cash-flow
- idiosyncratic-risk
- cost-of-debt
- beta
- risk-premium
- put-options
- affine-term-structure
- capm
- momentum
- market-risk-premium
- covered-calls
- ' exposure-at-default'
- stress-testing
- ornstein-uhlenbeck
- rating-migration
- comparable-analysis
- economic-value-added
- value-at-risk
- factor-models
- risk-management
- var-backtesting
- sum-of-parts
- european-options
- strangles
- conditional-var
- short-rate-models
- cost-of-equity
- efficient-frontier
- credit-migration
- default-probability
- credit-spreads
- multi-factor-models
- ito-calculus
- trading-multiples
- iron-condors
- option-pricing
- equity-value
- size-effect
- precedent-transactions
- lognormal-distribution
- ipo-valuation
- market-multiple
- apt
title: Appendix 20. A Valuation Using Discounted Cash Flow
type: note
---
--



# Appendix 20. A Valuation Using Discounted Cash Flow

For the special case where the stock follows geometric Brownian motion,  and where the claim has the payoff $S^{u}$ ,  we can also use discounted cash flow (DCF) to value the claim. In general,  there is no reason to use DCF when we can perform risk-neutral valuation,  bu it is instructive to see how DCF works in the case where a claim pays $S^{a}$ .We can value the claim by discounting the expected payoff under the physical measure at an appropriate discount rate. To do this we must compute the expected value of the claim and discount the expected payoff appropriately We know that the stock has a Sharpe ratio of $(\alpha-r)/\sigma$ . Equation (20.34) tells us that $S^{u}$ follows geometric Brownian motion with drift $a (\alpha-\delta)+0.5 a (a-1)\sigma^{2}$ and diffusion term $a_0 dZ$ gives us the process followed by $S^{a}$ . The requirement for equal Sharpe ratios tells that the expected return for a claim paying $S^{a},       \alpha_{a}$ must satisfy$$\frac{\alpha_a-r}{a\sigma}=\frac{\alpha-r}{\sigma}$$
This implies that $\alpha_{a}$ is$$\alpha_{a}=a (\alpha-r)+r$$
For the moment. Set $\delta=0.$ It is obvious that in general$$a (\alpha-r)+r\neq a\alpha+0.5 a (a-1)\sigma^{2}$$
The economic issue is that if $\alpha$ is the equilibrium return for the stock-that is,  it is the return for which investors are willing to hold the stock —then $a\alpha+0.5 a (a-1)\sigma^{2}$ is not generally the return for which investors are willing to hold a claim with the value $S^{u}$ . This is a consequence of Jensen’s inequality: Raising the stock price to a power requires a particular change in the expected return,  which is not the same as the return generated by raising the price to a power. To make investors willing to hold a claim paying $S^{u}$ at time 7 ,  the clain must sell at a premium or discount prior to time $I$ .We have already valued the claim in Proposition 20.3,  but we will value the claim a second time,  illustrating the application of DCF valuation in this context We know that the expected value of $S (T)^a$ is$$\mathrm{E}_{0}\left[S (T)^{a}\right]=S (0)^{a}e^{[a (\alpha-\delta)+\frac{1}{2}a (a-1)\sigma^{2}]T}$$
The expected return on this claim,  which is also the appropriate discount rate,  is given by expression (20.46). The price at time 0 of a claim paying $S (T)^{a}$ at time 1 is therefore the discounted expected payoff:$$\begin{aligned}
F_{0,       T}^{P}(S^{a})& =e^{-[r+a (\alpha-r)]T}\mathrm{E}(S (T)^{a})  \\
&=e^{-[r+a (\alpha-r)]T}S (0)^{a}e^{[a (\alpha-\delta)+\frac{1}{2}a (a-1)\sigma^{2}]T} \\
&=S (0)^{a}e^{-rT}e^{[a (r-\delta)+\frac{1}{2}a (a-1)\sigma^{2}]T}
\end{aligned}$$
Note that the risk premium on the stock,       $\alpha-r$ drops out of the derivation. This illustrates that DCF yields the same answer as risk-neutral pricing. The use of a constant discount rate works in this case because the payoff to the claim is relatively simple. In many cases computing a price using DCF will be more difficult than computing the price using risk neutral valuation.

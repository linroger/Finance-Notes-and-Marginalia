---
academic_level: graduate
aliases:
- Appendix 10
- Taxes and Options
cssclasses: academia
enhanced: true
enhancement_date: '2025-11-06'
enhancement_id: batch09-000430
key_concepts:
- Black-Scholes option pricing model and continuous-time finance
- Options Greeks and sensitivity analysis for risk management
- Duration analysis and interest rate risk management
- Convexity adjustments and yield curve sensitivity
- Capital Asset Pricing Model (CAPM) and expected returns
- Value at Risk (VaR) and tail risk measurement
- Basel accords and banking regulation framework
- Arbitrage opportunities and no-arbitrage pricing
- Factor models and multi-factor pricing
- Risk preference theory and utility functions
- Sensitivity analysis and Greeks calculation
- Risk Measurement and VaR Backtesting
- Contango, Backwardation, and Roll Yield
- 'Greeks: Delta, Gamma, Theta, and Vega Hedging'
- Futures and Forward Contracts in Financial Markets
- Option Valuation and Exercise Strategies
- Bond Pricing and Yield to Maturity Analysis
- Fixed Income Securities and Credit Quality
- Hedge Strategies and Basis Risk Management
- Value at Risk and Expected Shortfall
- Vasicek Interest Rate Model and Mean Reversion
- Short Rate Models and Term Structure Dynamics
- Ornstein-Uhlenbeck Process in Finance
- Options Trading Strategies and Risk Management
- Government and Corporate Bond Markets
- Stress Testing and Extreme Value Analysis
professional_application: theoreti
status: active
tags:
- arbitrage-opportunity
- arbitrage-pricing
- asset-allocation
- banking-regulation
- basel-accord
- binomial-model
- black-scholes-model
- capital-adequacy
- capital-asset-pricing
- caplet
- continuous-time-pricing
- convexity-adjustment
- credit-rating
- delta-hedging
- derivatives
- put-options
- affine-term-structure
- hull-white
- call-options
- zero-coupon-bonds
- clean-price
- cir-model
- butterfly-spreads
- strangles
- expected-shortfall
- straddles
- basis-risk
- parametric-var
- conditional-var
- extreme-value-theory
- fixed-income
- var-methodologies
- historical-var
- mean-reversion
- lognormal-models
- contango
- backwardation
- covered-calls
- short-rate-models
- bond-pricing
- option-strategies
- corporate-bonds
- stress-testing
- ornstein-uhlenbeck
- clearinghouse
- investment-analysis
- portfolio-optimization
- risk-premium
- marking-to-market
- value-at-risk
- hedge-ratio
- iron-condors
- protective-puts
- government-bonds
- market-price-of-risk
- financial-markets
- vasicek-model
- dirty-price
- monte-carlo-var
- convergence
- options-trading
- coupon-bonds
- futures-contracts
- var-backtesting
- roll-yield
- current-yield
- forward-contracts
- yield-to-maturity
title: Appendix 10.A Taxes and Option Prices
type: note
---
--



# Appendix 10.A Taxes and Option Prices

It is possible to solve for a binomial price when there are taxes. Suppose that each form of income is taxed at a different rate: interest at the rate $\tau_i$, capital gains on a stock at the rate $\tau_g$, capital gains on options at the rate $\tau_o$, and dividends at the rate $\tau_d$. We assume that taxes on all forms of income are paid on an accrual basis, and that there is no limit on the ability to deduct losses or to offset losses on one form of income against gains on another form of income.

We then choose $\Delta_t$ and $B_t$ by requiring that the after-tax return on the stock/bond portfolio equal the after-tax return on the option in both the up and down states. Thus we require that:

$$\begin{aligned}
\begin{bmatrix}S_{t+h}-\tau_g(S_{t+h}-S_t)+\delta S_t(1-\tau_d)\end{bmatrix}\Delta_t+\begin{bmatrix}1+r_h(1-\tau_i)\end{bmatrix}B_t\\
&= \phi_{t+h}(S_{t+h})-\tau_o\left[\phi_{t+h}(S_{t+h})-\phi_t(S_t)\right]
\end{aligned}$$

The solutions for $\Delta$ and $B$ are then:

$$\begin{aligned}
&\Delta=\frac{1-\tau_o}{1-\tau_g}\frac{\phi_1(S_1^+)-\phi_1(S_1^-)}{S_1^+-S_1^-}\\
&B=\frac{1}{1+r_h\frac{1-\tau_i}{1-\tau_o}}\left(\frac{u\phi_1(S_1^-)-d\phi_1(S_1^+)}{u-d}-\frac{\Delta}{1-\tau_o}S_0\left[\frac{\tau_g-\tau_o}{1-\tau_g}+\delta(1-\tau_d)\right]\right)
\end{aligned}$$

This gives an option price of:

$$\phi_t=\frac{1}{1+r_h\frac{1-\tau_i}{1-\tau_o}}\left[p^*\phi_{t+h}(S_{t+h}^+)+(1-p^*)\phi_{t+h}(S_{t+h}^-)\right]$$

Where:

$$p^*=\frac{1+r_h\frac{1-\tau_i}{1-\tau_g}-\delta\frac{1-\tau_d}{1-\tau_o}-d}{u-d}$$

In practice, dealers are marked-to-market for tax purposes and face the same tax rate on all forms of income. In this case taxes drop out of all the option-pricing expressions. When dealers are the effective price-setters in a market, taxes should not affect prices.

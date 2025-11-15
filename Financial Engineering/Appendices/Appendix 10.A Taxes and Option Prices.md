---
aliases:
- Appendix 10
- Taxes and Options
cssclasses: academia
enhanced: true
enhancement_date: '2025-11-06'
enhancement_id: batch03-a80e8e
key_concepts:
- Extensions to multi-factor CAPM models
- Tax rates on income
- Duration and convexity analysis for bond portfolio management
- Active portfolio management and performance attribution
- Credit risk modeling and default probability estimation
- Option Greeks and portfolio risk management
- Risk budgeting and portfolio construction techniques
- Capital Asset Pricing Model and beta estimation
- Binomial price with taxes
- Solution
- Capital Asset Pricing Model and expected returns
- Credit portfolio diversification and concentration
- Vega and volatility risk management
- Option pricing formula
- After-tax return equality
- Portfolio immunization strategies
- Mathematical Finance
- Key rate duration and curve risk
- Course Material
- Security Market Line and beta measurement
- Theta and time decay modeling
- ESG integration in portfolio management
- Credit exposure measurement and EAD
- Loss given default and recovery rates
- Delta hedging strategies in options portfolio management
- Wrong-way risk in derivative transactions
- Quantitative Implementation
- Financial markets and instruments
- Gamma and convexity adjustments
- Credit risk modeling and portfolio correlation analysis
- Credit risk assessment and loan portfolio management
- Delta hedging and the replication argument
- Duration and convexity measures for bond portfolios
- Currency hedging strategies for global portfolios
- Price sensitivity to interest rate changes
- Modified duration vs. Macaulay duration
- Market portfolio and risk-free rate assumptions
- Dealer marked-to-market
- Empirical tests and anomalies in CAPM
tags:
- derivatives-markets
- mathematical-finance
- course-material
- capm
- financial-modeling
- greeks
- binomial-pricing
- capital-gains
- credit-risk
- investment-strategy
- quantitative-implementation
- duration-convexity
- solution
- option-prices
- marked-to-market
- tax-rates
- option-pricing
- dealers
- taxes
- derivatives-pricing
- portfolio-theory
- quantitative-finance
title: Appendix 10.A Taxes and Option Prices
---

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

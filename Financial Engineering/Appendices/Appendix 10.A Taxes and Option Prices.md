---
title: "Appendix 10.A Taxes and Option Prices"
cssclasses: academia
tags:
  - binomial-pricing
  - capital-gains
  - dealers
  - marked-to-market
  - option-prices
  - tax-rates
  - taxes
aliases:
  - Appendix 10
  - Taxes and Options
key_concepts:
  - After-tax return equality
  - Binomial price with taxes
  - Dealer marked-to-market
  - Option pricing formula
  - Tax rates on income
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
---
title: Appendix 5.A Taxes and the Forward Price
cssclasses: academia
tags:
- arbitrage
- derivative-pricing
- forward
- forward-price
- future
- futures-price
- greeks
- interest-rate
- risk-free-rate
- stock
- taxes
aliases:
- Forward contract pricing
- Futures vs. Forwards
- Tax impact
key_concepts:
- Broker-dealer tax treatment
- Delta risk management
- Derivative securities
- Dynamic hedging strategies
- Financial risk management
- Forward vs. futures prices
- Gamma effects on options
- No-arbitrage forward price
- Options Greeks measurement
- Portfolio optimization
- Portfolio risk hedging
- Quantitative financial analysis
- Rho interest rate sensitivity
- Risk assessment and mitigation
- Stochastic interest rates
- Taxes on forward prices
- Theta time decay
- Vega volatility sensitivity
---

# Appendix 5.A Taxes and the Forward Price
The formulas in this chapter—and in the book to this point—have ignored taxes. In this appendix we show how taxes enter into the theoretical formula for the forward price, and explain why in practice these tax adjustments are never used. The impact of taxes on derivative prices was studied by Scholes (1976) and Cornell and French (1983), who showed that prices depend upon taxes when capital gains, dividends and interest are taxed $\$a_t$$ different rates. However, a party such as a broker-dealer, who is taxed identically on all forms of income, will have a fair price that is independent of taxes.

Suppose that capital gains on a stock are taxed $\$a_t$$ the rate $\tau_g$, gains on the forward contract $$a_t$$ $\tau_f$, dividends $$a_t$$ the rate $\tau_d$, and interest $$a_t$$ the rate $\tau_i$. Consider an investor who goes long $(1-\tau_g)/(1-\tau_f)$ forward contracts (we will see why in a moment) and hedges by selling one share today. The investor thus receives $S_0$, which can be invested to earn the risk-free rate.

In 1 year, the investor closes the transaction by buying a share and paying the forward price. After-tax income is:

$\$S_0[1+r(1-\tau_i)]-[S_1-\tau_g(S_1-S_0)]-\text{Div}(1-\tau_d)+[S_1-F_{0,1}]\frac{1-\tau_g}{1-\tau_f}(1-\tau_f)$$

The first bracketed term is the after-tax value of invested short-sale proceeds, the second is the after-tax cost of buying the share to close the short sale, the third is the after-tax dividend that must be paid to the share-lender, and the fourth is the after-tax gain on $(1-\tau_g)/(1-\tau_f)$ futures contracts. If the transaction is to generate no-arbitrage profits, the forward price must be set so that equation (5.20) equals zero. Thus, the after-tax zero-profit forward price is:

$\$F_{0,1}=S_0\left(1+r\frac{1-\tau_i}{1-\tau_g}\right)-\text{Div}\frac{1-\tau_d}{1-\tau_g}$$

Note that the tax on the forward contract does not enter the expression $\$a_t$$ all! The reason is that since the forward contract has a zero value, it is possible to offset the tax by entering into additional forward contracts—this is the reason for going long $(1-\tau_g)/(1-\tau_f)$ contracts against one short share. We in effect make the forward contract be taxed $$a_t$$ the same rate as the stock.

$\$F_{0,T}=S_0e^{[r(1-\tau_i)/(1-\tau_g)-\\delta(1-\tau_d)/(1-\tau_g)]T}$$

The important insight is that broker-dealers are marked-to-market for tax purposes and face the same tax rate on all forms of income—i.e., $\tau_i=\tau_g=\tau_d$. Thus, equation (5.21) becomes:

$\$F_{0,1}=S_0(1+r)-\text{Div}$$

The same as equation (5.5).
---
title: Appendix 5. A Taxes and the Forward Price
tags:
  - arbitrage
  - derivative_pricing
  - forward_price
  - futures_price
  - taxes
aliases:
  - Forward contract pricing
  - Futures vs. Forwards
  - Tax impact
key_concepts:
  - Broker-dealer tax treatment
  - Forward vs. futures prices
  - No-arbitrage forward price
  - Stochastic interest rates
  - Taxes on forward prices
---

# Appendix 5. A Taxes and the Forward Price

The formulas in this chapter—and in the book to this point—have ignored taxes. In this appendix we show how taxes enter into the theoretical formula for the [forward price](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%2011/Forward%20Contracts%20and%20Forward%20Prices.md),  and explain why in practice these tax adjustments are never used. The impact of taxes on derivative prices was studied by Scholes (1976) and Cornell and French (1983),  who showed that prices depend upon taxes when capital gains,  dividends and interest are taxed at different rates. However,  a party such as a broker-dealer,  who is taxed identically on all forms of income,  will have a fair price that is independent of taxes.

Suppose that capital gains on a stock are taxed at the rate $l_{g}$ ,  gains on the [forward contract](../../Clippings/Forward%20Points%20in%20Currency.md) at $\tau_f$ ,  dividends at the rate $\tau_{d}$ ,  and interest at the rate $\tau_{i}$ .Consider an investor who goes long $(1-\tau_{g})/(1-\tau_{f})$ forward contracts (we will see why in a moment) and hedges by selling one share today. The investor thus receives $S_{0}$ ,  which can be invested to earn the [risk-free rate](../../Financial%20Instruments/Black%20Scholes%20Derivation.md).

In 1 year,  the investor closes the transaction by buying a share and paying the [forward price](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%2011/Forward%20Contracts%20and%20Forward%20Prices.md). After-tax income is$$S_0[1+r(1-\tau_i)]-[S_1-\tau_g(S_1-S_0)]-Div(1-\tau_d)+[S_1-F_{0,      1}]\frac{1-\tau_g}{1-\tau_f}(1-\tau_f)$$
The first bracketed term is the after-tax value of invested short-sale proceeds,  the second is the after-tax cost of buying the share to close the [short sale](../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%202%20-%20Spot%20Markets/Short%20Selling.md),  the third is the after-tax dividend that must be paid to the share-lender,  and the fourth is the after-tax gain on $(1-\tau_{g})/(1-\tau_{f})$ [futures contracts](../Mathematics%20of%20the%20Financial%20Markets.md). If the transaction is to generate no-[arbitrage](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%207/Arbitrage%20Pricing%20of%20Derivatives.md) profits,  the [forward price](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%2011/Forward%20Contracts%20and%20Forward%20Prices.md) must be set so that equation (5.20) equals zero. Thus,  the after-tax zero-profit [forward price](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%2011/Forward%20Contracts%20and%20Forward%20Prices.md) is$$F_{0,      1}=S_0\left(1+r\frac{1-\tau_i}{1-\tau_g}\right)-Di\nu\frac{1-\tau_d}{1-\tau_g}$$
Note that the tax on the [forward contract](../../Clippings/Forward%20Points%20in%20Currency.md) does not enter the expression at all! The reason is that since the [forward contract](../../Clippings/Forward%20Points%20in%20Currency.md) has a zero value,  it is possible to offset the tax by entering intc additional forward contracts—this is the reason for going long $(1-\tau_{g})/(1-\tau_{f})$ contracts against one short share. We in effect make the [forward contract](../../Clippings/Forward%20Points%20in%20Currency.md) be taxed at the same rate as the stock.$$F_{0,      T}=S_{0}e^{[r(1-\tau_{i})/(1-\tau_{g})-\delta(1-\tau_{d})/(1-\tau_{g})]T}$$
The important insight is that broker-dealers are marked-to-market for tax purpose and face the same tax rate on all forms of income —-i.e.,  $\tau_{i}=\tau_{g}=\tau_{d}$ . Thus,  equation (5.21 becomes$$F_{0,      1}=S_0\left(1+r\right)-Div$$
The same as equation (5.5).

# [Appendix 5. C Forward and Futures Prices When Interest Rates Are Random](Appendix%205.%20C%20Forward%20And%20Futures%20Prices%20When%20Interest%20Rates%20Are%20Random)

This appendix formalizes the difference between forward and [futures](../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%203%20-%20Futures%20Markets/Futures%20Not%20Subject%20to%20Cash-And-Carry.md) prices and shows the relationship between them when [interest rates](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%202/Interest%20Rate%20Quotations.md) are stochastic. We will use the following notation:
$$\begin{aligned}
&F_{t,      T} =\mathrm{~Forward~price} \\
&f_{t,      F} \text{= Futures price} \\
&\text{s} = \text{Time }t \text{ price of the underlying asset} \\
&P_{t,      T} =\mathrm{~Time~}t\mathrm{~price~of~a~zero-coupon~bond~maturing~at~time~}T. \\
&\text{R} =\mathrm{~Time~}t\mathrm{~interest~rate~from~time~}t\mathrm{~to~time~}t+h. \\
&\text{h} =\mathrm{Length~of~a~period};h=T/n 
\end{aligned}$$

We will refer to an instrument that pays the [short-term interest rate](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%209/The%20Gauss%20Model.md) as a [money-market account](Appendix%205.C%20Forward%20And%20Futures%20Prices%20When%20Interest%20Rates%20Are%20Random.md).

The strategy in these derivations,      which follow Cox et al. (1981),      is to find a strategy that replicates fully funded contracts

### Forward Prices

The [forward price](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%2011/Forward%20Contracts%20and%20Forward%20Prices.md) is$$F_{t,      T}=\mathrm{PV}\left(\frac{S_T}{P_{t,      T}}\right)=\frac{S_t}{P_{t,      T}}$$
In the chapter,        we wrote this formula as $F_{t,      T}=S_{t}e^{r(T-t)}$ This is the same as equation (5.23),        where $r$ is the continuously compounded yield on the bond: $r=\ln(1/P_{t,      T})/(T-t)$

To prove equation (5.23),        buy $F_{t,      T}$ bonds paying $S1$ at maturity (this pre-funds the [forward price](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%2011/Forward%20Contracts%20and%20Forward%20Prices.md)) and go long $1/P_{t,      T}$ forward contracts. The payoff is$$\frac{F_{t,      T}}{P_{t,      T}}+\frac{1}{P_{t,      T}}\left[F_{T,      T}-F_{t,      T}\right]=\frac{F_{t,      T}}{P_{t,      T}}=\frac{S_{T}}{P_{t,      T}}$$
This demonstrates that a [portfolio](../../Advanced%20Investments/An%20Asset%20Allocation%20Primer.md) costing the [forward price](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%2011/Forward%20Contracts%20and%20Forward%20Prices.md) at time $t$ pays $S_{T}/P_{t,      T}$ Thus the [forward price](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%2011/Forward%20Contracts%20and%20Forward%20Prices.md) is the present value of $S_{T}/P_{t,      T}$ ,      or $S_{t}/P_{t,      T}$

## Futures Price

We will show that the [futures price](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%2011/Futures%20Price%20and%20the%20Quality%20Option%20Before%20E.md) is
$$f_{t,      T}=\text{PV}\left[S_T\prod_{i=t}^T(1+R_i)\right]$$

Note that if the interest rate is known,      $\prod_{i=t}^{T}(1+R_{i})=1/P_{t,      T}$ (the bond can be replicated with the money-market fund),      and the [forward price](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%2011/Forward%20Contracts%20and%20Forward%20Prices.md) equals the [futures price](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%2011/Futures%20Price%20and%20the%20Quality%20Option%20Before%20E.md). To prove equation (5.24),      invest the amount $f_{l,      T}$ at the [short-term interest rate](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%209/The%20Gauss%20Model.md),      reinvesting the proceeds each period. Also,      at each time $t_{i} \equiv t+ih,      i=1,      \ldots,      n$ ,      invest in $\Pi_{j=t}^{l_{i}}(1+R_{j})$ [futures contracts](../Mathematics%20of%20the%20Financial%20Markets.md). At time $t_{i+1}$ ,      liquidate position and invest the proceeds in the [money-market account](Appendix%205.C%20Forward%20And%20Futures%20Prices%20When%20Interest%20Rates%20Are%20Random.md). The net [cash flow](../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%201%20-%20Purpose%20and%20Structure%20of%20Financial%20Markets/Preview%20of%20the%20Book.md) at time 7 will be$$\begin{gathered}
f_{t,      T}\prod_{i=t}^{T}(1+R_{i}) +\sum_{i=t}^{T-h}\left(\prod_{j=t}^{i}(1+R_{j})(f_{j,      T}-f_{j-h,      T})\prod_{j=i+h}^{T-h}(1+R_{j})\right) \\
=f_{T,      T}\prod_{i=t}^{T-h}(1+R_{i})=S(T)\prod_{i=t}^{T-h}(1+R_{i}) 
\end{gathered}$$
For future reference,      note that in continuous time,      equation (5.24) becomes$$f_{t,      T}=\mathrm{PV}\left[S_Te^{\int_t^Tr(s)ds}\right]$$
where $r(s)$ is the instantaneous continuously compounded [short-term interest rate](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%209/The%20Gauss%20Model.md)
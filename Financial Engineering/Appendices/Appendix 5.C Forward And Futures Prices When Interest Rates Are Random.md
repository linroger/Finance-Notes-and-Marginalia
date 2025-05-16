---
cssclasses:
  - academia
title: Appendix 5. C Forward And Futures Prices When Interest Rates Are Random
tags:
  - forward_prices
  - futures_prices
  - interest_rates
  - money_market_account
  - stochastic_calculus
aliases:
  - Appendix 5.C
  - Forward vs. Futures
  - Stochastic Interest Rates
key_concepts:
  - Continuous time formula
  - Forward price formula
  - Futures price derivation
  - Money-market account
  - Replicating fully funded contracts
---

# Appendix 5. C Forward And Futures Prices When Interest Rates Are Random

This appendix formalizes the difference between forward and [futures](../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%203%20-%20Futures%20Markets/Futures%20Not%20Subject%20to%20Cash-And-Carry.md) prices and shows the relationship between them when [interest rates](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%202/Interest%20Rate%20Quotations.md) are stochastic. We will use the following notation:
$$\begin{aligned}
&F_{t,   T} =\mathrm{~Forward~price} \\
&f_{t,   F} \text{= Futures price} \\
&\text{s} = \text{Time }t \text{ price of the underlying asset} \\
&P_{t,   T} =\mathrm{~Time~}t\mathrm{~price~of~a~zero-coupon~bond~maturing~at~time~}T. \\
&\text{R} =\mathrm{~Time~}t\mathrm{~interest~rate~from~time~}t\mathrm{~to~time~}t+h. \\
&\text{h} =\mathrm{Length~of~a~period};h=T/n 
\end{aligned}$$

We will refer to an instrument that pays the [short-term interest rate](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%209/The%20Gauss%20Model.md) as a [money-market account](.md).

The strategy in these derivations,   which follow Cox et al. (1981),   is to find a strategy that replicates fully funded contracts

### Forward Prices

The [forward price](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%2011/Forward%20Contracts%20and%20Forward%20Prices.md) is$$F_{t,   T}=\mathrm{PV}\left(\frac{S_T}{P_{t,   T}}\right)=\frac{S_t}{P_{t,   T}}$$
In the chapter,     we wrote this formula as $F_{t,   T}=S_{t}e^{r(T-t)}$ This is the same as equation (5.23),     where $r$ is the continuously compounded yield on the bond: $r=\ln(1/P_{t,   T})/(T-t)$

To prove equation (5.23),     buy $F_{t,   T}$ bonds paying $S1$ at maturity (this pre-funds the [forward price](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%2011/Forward%20Contracts%20and%20Forward%20Prices.md)) and go long $1/P_{t,   T}$ forward contracts. The payoff is$$\frac{F_{t,   T}}{P_{t,   T}}+\frac{1}{P_{t,   T}}\left[F_{T,   T}-F_{t,   T}\right]=\frac{F_{t,   T}}{P_{t,   T}}=\frac{S_{T}}{P_{t,   T}}$$
This demonstrates that a [portfolio](../../Advanced%20Investments/An%20Asset%20Allocation%20Primer.md) costing the [forward price](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%2011/Forward%20Contracts%20and%20Forward%20Prices.md) at time $t$ pays $S_{T}/P_{t,   T}$ Thus the [forward price](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%2011/Forward%20Contracts%20and%20Forward%20Prices.md) is the present value of $S_{T}/P_{t,   T}$ ,   or $S_{t}/P_{t,   T}$

## Futures Price

We will show that the [futures price](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%2011/Futures%20Price%20and%20the%20Quality%20Option%20Before%20E.md) is
$$f_{t,   T}=\text{PV}\left[S_T\prod_{i=t}^T(1+R_i)\right]$$

Note that if the interest rate is known,   $\prod_{i=t}^{T}(1+R_{i})=1/P_{t,   T}$ (the bond can be replicated with the money-market fund),   and the [forward price](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%2011/Forward%20Contracts%20and%20Forward%20Prices.md) equals the [futures price](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%2011/Futures%20Price%20and%20the%20Quality%20Option%20Before%20E.md). To prove equation (5.24),   invest the amount $f_{l,   T}$ at the [short-term interest rate](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%209/The%20Gauss%20Model.md),   reinvesting the proceeds each period. Also,   at each time $t_{i} \equiv t+ih,   i=1,   \ldots,   n$ ,   invest in $\Pi_{j=t}^{l_{i}}(1+R_{j})$ [futures contracts](../Mathematics%20of%20the%20Financial%20Markets.md). At time $t_{i+1}$ ,   liquidate position and invest the proceeds in the [money-market account](.md). The net [cash flow](../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%201%20-%20Purpose%20and%20Structure%20of%20Financial%20Markets/Preview%20of%20the%20Book.md) at time 7 will be$$\begin{gathered}
f_{t,   T}\prod_{i=t}^{T}(1+R_{i}) +\sum_{i=t}^{T-h}\left(\prod_{j=t}^{i}(1+R_{j})(f_{j,   T}-f_{j-h,   T})\prod_{j=i+h}^{T-h}(1+R_{j})\right) \\
=f_{T,   T}\prod_{i=t}^{T-h}(1+R_{i})=S(T)\prod_{i=t}^{T-h}(1+R_{i}) 
\end{gathered}$$
For future reference,   note that in continuous time,   equation (5.24) becomes$$f_{t,   T}=\mathrm{PV}\left[S_Te^{\int_t^Tr(s)ds}\right]$$
where $r(s)$ is the instantaneous continuously compounded [short-term interest rate](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%209/The%20Gauss%20Model.md)
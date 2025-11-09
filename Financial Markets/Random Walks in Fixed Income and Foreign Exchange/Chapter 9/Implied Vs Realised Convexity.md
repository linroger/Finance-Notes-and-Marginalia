---
tags:
  - bond_convexity
  - bond_pricing
  - implied_convexity
  - realised_convexity
  - yield_curve
aliases:
  - Bond Convexity
  - Convexity Analysis
  - Implied vs. Realized
  - Realised Convexity
key_concepts:
  - Bond price non-linearity
  - Bond price sensitivity
  - Convexity value calculation
  - Implied vs. realized convexity
  - Yield change scenarios
---

# Chapter 9 Implied vs Realised Convexity

Chapter 8, when published as a Rates Radar, stirred many interesting discussions. We were motivated to expand our analysis to compare the theoretical or implied [convexity](../../../Fixed%20Income%20Asset%20Pricing/Problem%20Sets/PSET%20II%20Fixed%20Income%20Asset%20Pricing%201.md) value of a bond with the actual [realised convexity](.md) value over time.' We are able to show that this implied [convexity](../../../Fixed%20Income%20Asset%20Pricing/Problem%20Sets/PSET%20II%20Fixed%20Income%20Asset%20Pricing%201.md) value' is a good overall estimate of levels of [realised convexity](.md) value over a 1y horizon. For completeness, we repeat a small part of the derivation of the [convexity](../../../Fixed%20Income%20Asset%20Pricing/Problem%20Sets/PSET%20II%20Fixed%20Income%20Asset%20Pricing%201.md) formulae here, though it is covered more thoroughly in Chapter 8.

Where does [convexity](../../../Fixed%20Income%20Asset%20Pricing/Problem%20Sets/PSET%20II%20Fixed%20Income%20Asset%20Pricing%201.md) value come from? The price of a bond changes with changes. in yield. However, this price change is non-linear, with the price being a convex function of the yield. Thus, the bond holder always does a little better under yield change. scenarios than a linear approximation would indicate. This non-linearity is the '[convexity](../../../Fixed%20Income%20Asset%20Pricing/Problem%20Sets/PSET%20II%20Fixed%20Income%20Asset%20Pricing%201.md)', and as longer-dated bonds are more sensitive to yield changes, they exhibit higher [convexity](../../../Fixed%20Income%20Asset%20Pricing/Problem%20Sets/PSET%20II%20Fixed%20Income%20Asset%20Pricing%201.md) than shorter-dated bonds. A bond or other instrument with high [convexity](../../../Fixed%20Income%20Asset%20Pricing/Problem%20Sets/PSET%20II%20Fixed%20Income%20Asset%20Pricing%201.md) is very desirable.

How large is [convexity](../../../Fixed%20Income%20Asset%20Pricing/Problem%20Sets/PSET%20II%20Fixed%20Income%20Asset%20Pricing%201.md) value? Though it's very common to hear that ultra-long. bonds are popular due to high [convexity](../../../Fixed%20Income%20Asset%20Pricing/Problem%20Sets/PSET%20II%20Fixed%20Income%20Asset%20Pricing%201.md), it's rare to see numbers attached to this [convexity](../../../Fixed%20Income%20Asset%20Pricing/Problem%20Sets/PSET%20II%20Fixed%20Income%20Asset%20Pricing%201.md) value. In part, this is because it is a calculation involving a number of assumptions about future yield and volatility levels, so it can only ever be an estimate. Also, the calculation itself is somewhat complex; it can be done using finite differences, or by multiplying the PV of each cashflow by a factor connected with. yield and tenor. In Chapter 8, we showed that it is also possible to derive a closedform solution for [convexity](../../../Fixed%20Income%20Asset%20Pricing/Problem%20Sets/PSET%20II%20Fixed%20Income%20Asset%20Pricing%201.md), though it is quite long. Thus, it tends to be discussed more qualitatively than quantitatively, which is a pity, as precise comparisons can be useful. In this chapter, we show how the value of [convexity](../../../Fixed%20Income%20Asset%20Pricing/Problem%20Sets/PSET%20II%20Fixed%20Income%20Asset%20Pricing%201.md) has changed over time for instruments of different tenors.

We compare implied and [realised convexity](.md). What is also very relevant for bond. holders, and also rarely seen, is a measure of how much [convexity](../../../Fixed%20Income%20Asset%20Pricing/Problem%20Sets/PSET%20II%20Fixed%20Income%20Asset%20Pricing%201.md) value a bond. turned out to generate. This will of course depend on yield and volatility changes. over the period in question, but it is of interest to see how accurate the 'implied'. [convexity](../../../Fixed%20Income%20Asset%20Pricing/Problem%20Sets/PSET%20II%20Fixed%20Income%20Asset%20Pricing%201.md) is, relative to the actual value realised over time. We calculate the implied [convexity](../../../Fixed%20Income%20Asset%20Pricing/Problem%20Sets/PSET%20II%20Fixed%20Income%20Asset%20Pricing%201.md) value for EUR instruments using two different methods: (1) using current. bond yields, and (2) using Bloomberg consensus forecast yields. We show that the two calculations lead to very similar estimates. We then compare this to the [realised convexity](.md) value over a 1y period, and show that with some variation, implied and realised values certainly fall into the same range. We show that the main drivers of. implied and [realised convexity](.md) value are [implied volatility](../../Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%205%20Options%20on%20Prices%20and%20Hedge-Based%20Valuation/A%20Real-Life%20Option%20Pricing%20Exercise.md) and change in yield, respectively.

# Defining Convexity

[Convexity](../../../Fixed%20Income%20Asset%20Pricing/Problem%20Sets/PSET%20II%20Fixed%20Income%20Asset%20Pricing%201.md) is the parameter defining the degree of non-linearity of the price of a bond with respect to yield. The price $P$ of a bond of $n$ years' tenor, yield $y$ and coupon $c$ is given by the following:
$$
P=\sum_{i=1}^{n-1}{\frac{c}{\left(1+y\right)^{i}}}+{\frac{c+100\%}{\left(1+y\right)^{n}}}
$$

If the yield of the bond changes, of course it is possible to recalculate the new price using this expression. However, it's not very intuitive to see how price and yield relate to each other from this. Thus, it is usually expressed as.
$$
P_{t}\approx P_{0}+D(y_{t}-y_{o})+\frac{1}{2}C(y_{t}-y_{o})^{2}
$$

where $\mathrm{P_{t}}$ is the price of the bond at time. $t,D$ is the [duration](../../Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%205/Key%20Rates%20O1s%20Durations%20and%20Hedging.md), and. $C$ is the [convexity](../../../Fixed%20Income%20Asset%20Pricing/Problem%20Sets/PSET%20II%20Fixed%20Income%20Asset%20Pricing%201.md). $D$ and $C$ are of course the first and second [derivatives](../../Financial%20Trading%20and%20Markets/Chapter%209%20Arbitrage%20and%20Hedging%20With%20Options.md) of price with respect to yield, and have [closed-form solutions](../../../Financial%20Engineering/Derivatives/Part%20IX%20-%20Fixed%20Income%20Derivatives/Chapter%2040%20-%20Pricing%20Fixed%20Income%20Options:%20Black’s%20Model%20and%20MCS.md), as follows:
$$
D=-\frac{1}{1+y}\left[\frac{1+y}{y}-\frac{1+y+n\left(c-y\right)}{c\left[\left(1+y\right)^{n}-1\right]+y}\right]
$$

and
$$
\begin{array}{l}{{C=\displaystyle\frac{c V^{4}}{\left(1-V\right)^{3}}\left[n\big(1-n\big)\big(1-V\big)^{2}V^{n-2}-2n V^{n-1}\big(1-V\big)+2\big(1-V^{n}\big)\right]}}\ {{\mathrm{~}+\displaystyle\frac{2c V^{3}}{\left(1-V\right)^{2}}\left[-n V^{n-1}\big(1-V\big)+\big(1-V^{n}\big)\right]+\big(1+c\big)\big(n+1\big)n V^{n+2}}}\end{array}
$$

where
$$
V={\frac{1}{1+y}}
$$

Thus, if an investor holds a bond, with known [duration](../../Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%205/Key%20Rates%20O1s%20Durations%20and%20Hedging.md) $D$ and [convexity](../../../Fixed%20Income%20Asset%20Pricing/Problem%20Sets/PSET%20II%20Fixed%20Income%20Asset%20Pricing%201.md) $C$ , they can predict the new price it will have at a future time when the yield has changed from $\mathrm{y_{0}}$ to $\mathrm{y_{t}}$

# Value of Implied Convexity

[Convexity](../../../Fixed%20Income%20Asset%20Pricing/Problem%20Sets/PSET%20II%20Fixed%20Income%20Asset%20Pricing%201.md) C, as defined, is just a coefficient, not a value. What is the value of this nonlinearity? Clearly, the value of the third term in equation (2) depends on the change in yield, and so the expected value of the [convexity](../../../Fixed%20Income%20Asset%20Pricing/Problem%20Sets/PSET%20II%20Fixed%20Income%20Asset%20Pricing%201.md) of a bond - over the. next year, for example - will depend upon the expected range of changes of yield. over that time.

Suddenly, now we have changed from our fairly deterministic expressions to something more related to averages, forecasts and statistics. Because we don't exactly know the future value of the bond yield, we can't definitively state what the value of the [convexity](../../../Fixed%20Income%20Asset%20Pricing/Problem%20Sets/PSET%20II%20Fixed%20Income%20Asset%20Pricing%201.md) term will be. However, statistics comes to our aid, and if we know the future standard deviation $\upsigma_{\mathrm{y}}$ of the yield, we can say
$$
C o n\nu e x i t y~\nu a l u e=\frac{1}{2}~{\sigma_{y}}^{2}t\times C
$$

This makes a number of assumptions, none of which are unassailable. It assumes. that the future distribution of the yield is known, stationary and lognormal, all of which may be challenged. Nevertheless, it certainly serves to provide a useful estimate, and additionally, we do have a ready-made market estimate for. $\upsigma_{\mathrm{y}}$ in the form of the [swaption volatility](../../Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%2016/Swaption%20Skew.md) for the relevant tenor and time forward..

We need also to consider what value to use for the coupon of the bond. This. will enter the calculation of [convexity](../../../Fixed%20Income%20Asset%20Pricing/Problem%20Sets/PSET%20II%20Fixed%20Income%20Asset%20Pricing%201.md) value via equation (3). We can do two things. here - the first is to use the yield as the coupon, assuming that the curve will retain. its current form over the next year, and the second is to use a forecast value. To. obtain forecast values through history, we have created a series of 1y ahead forecasts from the Bloomberg consensus forecast series, which updates each quarter. This is only available for the 10y case, but nevertheless is useful..

Using all these assumptions, we can go back through history and extract yields. and swaption volatilities to create the graphs in Figures 9.1 and 9.2 of the implied. [convexity](../../../Fixed%20Income%20Asset%20Pricing/Problem%20Sets/PSET%20II%20Fixed%20Income%20Asset%20Pricing%201.md) value. Of course, we could also use different volatilities if we felt we could do better than the swaptions, but that starts to become fairly speculative..

Two things are worth noting here. The first is the difference in scale; the 5Oy in-. struments indeed have a far greater [convexity](../../../Fixed%20Income%20Asset%20Pricing/Problem%20Sets/PSET%20II%20Fixed%20Income%20Asset%20Pricing%201.md) value than the 10y case. The second is that there is almost no difference in using forecast yields vs assuming constant yields.. This is consistent with Chapter 8, in which we also showed that there was little difference if we used forward yields. The reason is that the main driver of implied [convexity](../../../Fixed%20Income%20Asset%20Pricing/Problem%20Sets/PSET%20II%20Fixed%20Income%20Asset%20Pricing%201.md). value is the [implied swaption volatility](../../../Financial%20Instruments/Pricing%20a%20Callable%20Leveraged%20Constant%20Maturity%20Swap%20Spread%20Note.md), whose range of variation is vastly larger than the relatively modest adjustment in yields.

This is actually somewhat reassuring. When one realises that the implied [convexity](../../../Fixed%20Income%20Asset%20Pricing/Problem%20Sets/PSET%20II%20Fixed%20Income%20Asset%20Pricing%201.md) relies on so many different assumptions, it could be thought that there is little way. to obtain a reliable estimate. But when we realise that a single input, the future yield. volatility, dominates, at least we have narrowed the range of uncertainty..

![](b7ba24e76b0e03a9c37e0d2b05b955fcb9f7a7c6d811ff35342ed17f36a2e698.jpg)
Figure 9.1: Implied [convexity](../../../Fixed%20Income%20Asset%20Pricing/Problem%20Sets/PSET%20II%20Fixed%20Income%20Asset%20Pricing%201.md) value, 10y German bonds. Source: Commerzbank, Bloomberg

![](c48d859d6baf59d4db20ff57a57b4a4561e96d9563ff01aca468dbe5bc08b5b8.jpg)
Figure 9.2: Implied [convexity](../../../Fixed%20Income%20Asset%20Pricing/Problem%20Sets/PSET%20II%20Fixed%20Income%20Asset%20Pricing%201.md) value, 50y EUR swaps. Source: Commerzbank, Bloomberg

# Value of Realised Convexity

We can now turn our attention to the actual realised value, which the [convexity](../../../Fixed%20Income%20Asset%20Pricing/Problem%20Sets/PSET%20II%20Fixed%20Income%20Asset%20Pricing%201.md) has supplied in the past. The realised value of [convexity](../../../Fixed%20Income%20Asset%20Pricing/Problem%20Sets/PSET%20II%20Fixed%20Income%20Asset%20Pricing%201.md) is the performance of a bond. that occurs when yields change. In other words, it reflects the additional price gain. from the [duration](../../Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%205/Key%20Rates%20O1s%20Durations%20and%20Hedging.md) increase when yields fall, and the reduced price loss from the [duration](../../Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%205/Key%20Rates%20O1s%20Durations%20and%20Hedging.md) decline when yields rise. This also explains that the realised value of [convexity](../../../Fixed%20Income%20Asset%20Pricing/Problem%20Sets/PSET%20II%20Fixed%20Income%20Asset%20Pricing%201.md) is always greater than zero and is zero when yields stay the same..

In algebraic terms, we use equations (1) and (2), restated here, to compute the realised value of [convexity](../../../Fixed%20Income%20Asset%20Pricing/Problem%20Sets/PSET%20II%20Fixed%20Income%20Asset%20Pricing%201.md).
$$
\begin{array}{c}{{P=\displaystyle\sum_{i=1}^{n-1}\displaystyle\frac{c}{\left(1+y\right)^{i}}+\displaystyle\frac{c+100\%}{\left(1+y\right)^{n}}}}\ {{{}}}\ {{P_{t}\approx P_{0}+D(y_{t}-y_{o})+\displaystyle\frac{1}{2}C(y_{t}-y_{o})^{2}}}\end{array}
$$

Using equation (1), we find the exact value of the bond price one year ahead. Then we use equation (2), with $\mathrm{P}_{0}$ taken as the bond price at the start of the year, and. $D$ and $C$ the [duration and convexity](../../Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%208/An%20Analytical%20Decomposition%20of%20Forward%20Rates.md) at the start of the year. Using these values, together with the change in yield over the course of the year, we hope to use the price calculated with equation (2) to match up with that calculated with equation (1).

In Figure 9.3, we see the results. The solid grey line, hardly visible, is the [full price](../../Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%201/Accrued%20Interest.md) calculation at the end of the 1y period using equation (1). The black line, again not very visible, is the price calculated using only the first two terms of equation (2). It can be seen that it does not match perfectly to the full calculation. The dashed light grey line is the price calculated using all three terms in equation (2), including the [convexity](../../../Fixed%20Income%20Asset%20Pricing/Problem%20Sets/PSET%20II%20Fixed%20Income%20Asset%20Pricing%201.md) value. It can be seen that the inclusion of this final term is a better approximation to the true price.

![](57a6a322c5e8ce64d3c4d281ae5aa1eb63d1e0288808fb664cffeef423648869.jpg)
Bond price calculated with full accuracy and with different approximations, in $\%$
Figure 9.3: History of 50y bond price with [convexity](../../../Fixed%20Income%20Asset%20Pricing/Problem%20Sets/PSET%20II%20Fixed%20Income%20Asset%20Pricing%201.md) value. Source: Commerzbank, Bloomberg

Finally, the dark grey dashed line at the bottom of the chart, which is charted using the axis on the right, is the [convexity](../../../Fixed%20Income%20Asset%20Pricing/Problem%20Sets/PSET%20II%20Fixed%20Income%20Asset%20Pricing%201.md) value term on its own - that is, just the third term of equation (2).
$$
C o n v e x i t y~\nu a l u e=\frac{1}{2}C(y_{t}-y_{o})^{2}
$$

This is the [realised convexity](.md), and is primarily driven by the change in yield over the course of the year. For this long 50y instrument, it can be seen that it is large, over $10\%$ at times.

Finally, we can graph implied vs [realised convexity](.md) together, as in Figure 9.4.. We see that while we would hardly expect implied [convexity](../../../Fixed%20Income%20Asset%20Pricing/Problem%20Sets/PSET%20II%20Fixed%20Income%20Asset%20Pricing%201.md) to accurately indicate. changes in [realised convexity](.md), the overall levels of [realised convexity](.md) oscillate. around implied, and on the whole it appears to be a reasonable estimate. Note that the near-zero levels of [realised convexity](.md) occur when the change in yield over. the course of the year is close to zero..

![](78f9c89c727d1349bc6a5025d30f6d477adbd669abf3eae93e89e7ccd7077643.jpg)
Figure 9.4: Implied vs [realised convexity](.md) for 50y bond. Source: Commerzbank, Bloomberge

These calculations emphasise the importance of the ultra-long end of the curve. Our graph in Figure 9.5 shows the [realised convexity](.md) value for 10, 30 and 50y maturities. While [realised convexity](.md) for the 10y case peaks at. $1.25\%$ , for the 50y case, we see close to $20\%$ , which is very significant.

Finally, we take a look at [realised convexity](.md) value over different timescales. So. far, our analysis has concentrated on a 1y period, but it is also interesting to focus. on shorter periods. In Figure 9.6, we plot the [realised convexity](.md) value over 1y, 6m and $3\mathrm{m}$ periods for a 30y bond. It can be seen that even over shorter periods, the. [convexity](../../../Fixed%20Income%20Asset%20Pricing/Problem%20Sets/PSET%20II%20Fixed%20Income%20Asset%20Pricing%201.md) value can be considerable when there is substantial yield variation..

![](e7f982194d620d1530fe24282f4a97c948dc16116d1964bdad38892778c77d6c.jpg)
Figure 9.5: History of [convexity](../../../Fixed%20Income%20Asset%20Pricing/Problem%20Sets/PSET%20II%20Fixed%20Income%20Asset%20Pricing%201.md) value for bonds of different tenor. Source: Commerzbank, Bloomberg

![](c57e63598be5f652aeaa9ac44ff84684bed3026f1a91b54baced451390e20504.jpg)
Figure 9.6: [Realised convexity](.md) of a 30y bond over different periods. Source: Commerzbank, Bloomberge

# List of Figures

1.1 1y EURUSD [xccy basis](../../../Contemporary%20Financial%20Intermediation%20Notes/Table%20of%20Contents.md) - 2
1.2 [Forward FX rate](../Chapter%201/What%20Really%20Is%20the%20Cross-Currency%20Basis.md) calculation -- 3
1.3 Theoretical and actual EUR interest rate difference -- 4
1.4 Forward difference -- 5
1.5 [Cross-currency basis swap](../../../Contemporary%20Financial%20Intermediation%20Notes/Table%20of%20Contents.md) -- -7
1.6 Potential sources of the [xccy basis](../../../Contemporary%20Financial%20Intermediation%20Notes/Table%20of%20Contents.md) - 10
1.7 [Cross-currency basis swap](../../../Contemporary%20Financial%20Intermediation%20Notes/Table%20of%20Contents.md) with FX carry -- 12
1.8 Yield pickup, with potential [arbitrage](../../Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%207/Arbitrage%20Pricing%20of%20Derivatives.md) opportunity levels - 14
1.9 EURUSD yield pickup components $(\%)$ 15
1.10 [Carry trade](../../../Clippings/Currency%20Carry%20Trade.md) [returns](../../Financial%20Asset%20Pricing%20Theory%20Overview/Chapter%203%20-%20%20Assets,%20Portfolios,%20and%20Arbitrage/Assets.md) - 17
1.11 [FX swap](../../../Clippings/Currency%20Swap%20Basics.md) 18
1.12 FX outright -19
1.13 Spot trade plus swap -- 19
1.14 [Cross-currency basis swap](../../../Contemporary%20Financial%20Intermediation%20Notes/Table%20of%20Contents.md) 20
2.1 [Credit Default Swap](../../../Credit%20Markets/Credit%20Market%20Session%202.md) -- 24
2.2 5y cash-CDS and cross EURUSD [currency](../../../Financial%20Instruments/Lecture%20Notes-%20Financial%20Instruments/Teaching%20Note%201-%20Forward%20Rates%20Agreement/Forwards%20and%20Futures%20Notes.md) bases, in bp - 25
2.3 5y [xccy basis](../../../Contemporary%20Financial%20Intermediation%20Notes/Table%20of%20Contents.md) for EURUSD in bp - 28
2.4 5y [xccy basis](../../../Contemporary%20Financial%20Intermediation%20Notes/Table%20of%20Contents.md) for USDJPY in bp - 28
2.5 10y BBB [xccy basis](../../../Contemporary%20Financial%20Intermediation%20Notes/Table%20of%20Contents.md) and uncollateralised trade cost, in bp -- 30
2.6 1y USD [swap rate](../../../Fixed%20Income%20Asset%20Pricing/Fixed%20Income%20Lecture%20Notes/Teaching%20Note%204%20Interest%20Rate%20Derivatives.md) and deposit rate -- 32
2.7 1y USD swap-deposit spread, with 1y xccy EURUSD basis - 33
2.8 1-day EURusD forward-forward curve in forward points - 34
2.9 1-day historical FX forward -- 35-
2.10 Internal forward points vs market $0/\Nu$ in $\%$ 37
2.11 Internal forward points vs market T/N in $\%$ 37
2.12 Indication of profitability of [xccy basis](../../../Contemporary%20Financial%20Intermediation%20Notes/Table%20of%20Contents.md) trade. 1y tenor, all in bp -- 38
3.1 Constructed and quoted EURJPY 10y [xccy basis](../../../Contemporary%20Financial%20Intermediation%20Notes/Table%20of%20Contents.md) in bp - 44
3.2 [Xccy basis](../../../Contemporary%20Financial%20Intermediation%20Notes/Table%20of%20Contents.md) for GBPJPY in bp - 46
3.3 [Xccy basis](../../../Contemporary%20Financial%20Intermediation%20Notes/Table%20of%20Contents.md) for CHFJPY in bp - 46
3.4 [FX hedged pickup](../../../Contemporary%20Financial%20Intermediation%20Notes/Table%20of%20Contents.md) for EURJPY in % - 47
3.5 [FX hedged pickup](../../../Contemporary%20Financial%20Intermediation%20Notes/Table%20of%20Contents.md) for USDJPY in % - 47
3.6 [FX hedged pickup](../../../Contemporary%20Financial%20Intermediation%20Notes/Table%20of%20Contents.md) for GBPJPY in % - 48
3.7 [FX hedged pickup](../../../Contemporary%20Financial%20Intermediation%20Notes/Table%20of%20Contents.md) for AUDJPY in % - 48
3.8 [Xccy basis](../../../Contemporary%20Financial%20Intermediation%20Notes/Table%20of%20Contents.md) for EURUSD in bp (to the EUR) 49
3.9 [Xccy basis](../../../Contemporary%20Financial%20Intermediation%20Notes/Table%20of%20Contents.md) for EURJPY in bp (to the EUR) 49
3.10 [Xccy basis](../../../Contemporary%20Financial%20Intermediation%20Notes/Table%20of%20Contents.md) for EURGBP (to the EUR) - 49
3.11 [Xccy basis](../../../Contemporary%20Financial%20Intermediation%20Notes/Table%20of%20Contents.md) for EURAUD (to the EUR) 50
3.12 [Xccy basis](../../../Contemporary%20Financial%20Intermediation%20Notes/Table%20of%20Contents.md) for EURCAD (to the EUR) 50
3.13Xccy basis for EURCHF (to the EUR) 50
3.14 [Xccy basis](../../../Contemporary%20Financial%20Intermediation%20Notes/Table%20of%20Contents.md) for EURUSD (to the USD) 51
3.15Xccy basis for USDJPY (to the USD) 51
3.16Xccy basis for USDGBP (to the USD) 51
3.17Xccy basis for USDAUD (to the USD) 52
3.18Xccy basis for USDCAD (to the USD) 52
3.19Xccy basis for USDCHF (to the USD) 52
3.20 [Xccy basis](../../../Contemporary%20Financial%20Intermediation%20Notes/Table%20of%20Contents.md) for EURJPY (to the JPY) - 53
3.21 [Xccy basis](../../../Contemporary%20Financial%20Intermediation%20Notes/Table%20of%20Contents.md) for USDJPY (to the JPY) - 53
3.22 [Xccy basis](../../../Contemporary%20Financial%20Intermediation%20Notes/Table%20of%20Contents.md) for GBPJPY (to the JPY) -- 53
3.23Xccy basis for AUDJPY (to the JPY)- 54
3.24 [Xccy basis](../../../Contemporary%20Financial%20Intermediation%20Notes/Table%20of%20Contents.md) for CADJPY (to the JPY)- 54
3.25Xccy basis for CHFJPY (to the JPY) . 54
3.26 [FX hedged pickup](../../../Contemporary%20Financial%20Intermediation%20Notes/Table%20of%20Contents.md) for EURUSD (to the EUR) 55
3.27 [FX hedged pickup](../../../Contemporary%20Financial%20Intermediation%20Notes/Table%20of%20Contents.md) for EURJPY (to the EUR) 55
3.28 [FX hedged pickup](../../../Contemporary%20Financial%20Intermediation%20Notes/Table%20of%20Contents.md) for EURGBP (to the EUR) 56
3.29 [FX hedged pickup](../../../Contemporary%20Financial%20Intermediation%20Notes/Table%20of%20Contents.md) for EURAUD (to the EUR) - 56
3.30 [FX hedged pickup](../../../Contemporary%20Financial%20Intermediation%20Notes/Table%20of%20Contents.md) for EURCAD (to the EUR) 56
3.31 [FX hedged pickup](../../../Contemporary%20Financial%20Intermediation%20Notes/Table%20of%20Contents.md) for EURCHF (to the EUR) - 57
3.32 [FX hedged pickup](../../../Contemporary%20Financial%20Intermediation%20Notes/Table%20of%20Contents.md) for EURUSD (to the USD) 57
3.33 [FX hedged pickup](../../../Contemporary%20Financial%20Intermediation%20Notes/Table%20of%20Contents.md) for USDJPY (to the USD) 58
3.34 [FX hedged pickup](../../../Contemporary%20Financial%20Intermediation%20Notes/Table%20of%20Contents.md) for USDGBP (to the USD) 58
3.35 [FX hedged pickup](../../../Contemporary%20Financial%20Intermediation%20Notes/Table%20of%20Contents.md) for USDAUD (to the USD) 58
3.36 [FX hedged pickup](../../../Contemporary%20Financial%20Intermediation%20Notes/Table%20of%20Contents.md) for USDCAD (to the USD) 59
3.37 [FX hedged pickup](../../../Contemporary%20Financial%20Intermediation%20Notes/Table%20of%20Contents.md) for USDCHF (to the USD) 59
3.38 [FX hedged pickup](../../../Contemporary%20Financial%20Intermediation%20Notes/Table%20of%20Contents.md) for EURJPY (to the JPY) 59
3.39 [FX hedged pickup](../../../Contemporary%20Financial%20Intermediation%20Notes/Table%20of%20Contents.md) for USDJPY (to the JPY) 60
3.40 [FX hedged pickup](../../../Contemporary%20Financial%20Intermediation%20Notes/Table%20of%20Contents.md) for GBPJPY (to the JPY) 60
3.41 [FX hedged pickup](../../../Contemporary%20Financial%20Intermediation%20Notes/Table%20of%20Contents.md) for AUDJPY (to the JPY) 60
3.42 [FX hedged pickup](../../../Contemporary%20Financial%20Intermediation%20Notes/Table%20of%20Contents.md) for CADJPY (to the JPY) 61
3.43 [FX hedged pickup](../../../Contemporary%20Financial%20Intermediation%20Notes/Table%20of%20Contents.md) for CHFJPY (to the JPY) - 61
4.1 Maturity-matched FX hedged yield pickup for 2y USD bonds vs EUR vs
German bonds, in bp -- 66
4.2 Generic bond yields for 2y USD and EUR bonds, in $\%$ 67
4.3 Maturity-matched FX hedged yield pickup vs EUR for 2y USD and EUR
bonds, in. $\%$ 1 67
4.4 Generic bond yields for 2y JPY and EUR bonds, in $\%$ 67
4.5 Maturity-matched FX hedged yield pickup vs EUR for 2y JPY and EUR.
bonds, in % - 68
4.6 Generic bond yields for 10y USD and EUR bonds, in % - 68
4.7 Maturity-matched FX hedged yield pickup vs EUR for 10y USD and EUR.
bonds, in. $\%$ 68
4.8 Generic bond yields for 10y JPY and EUR bond, in $\%$ - 69
4.9 Maturity-matched FX hedged yield pickup vs EUR for 10y JPY bond, in $\%$ 69
4.10 Generic bond yields for 2y USD and EUR bond, in %  71
4.11 3m FX hedged yield pickup vs EUR for 2y USD and EUR bond, in $\%$ 71
4.12 Generic bond yields for 2y JPY and EUR bond, in % - 72.
4.13 3m FX hedged yield pickup vs EUR for 2y JPY and EUR bond, in. $\%$ -72
4.14 Generic bond yields for 10y USD and EUR bond, in $\%$ 73
4.15 3m FX hedged yield pickup vs EUR for 10y USD and EUR bond, in. $\%$ 73
4.16 Generic bond yields for 10y JPY and EUR bond, in % -- 73
4.17 3m FX hedged yield pickup vs EUR for 10y JPY and EUR bond, in $\%$ -74
4.18 Rolling FX hedged yield pickup vs EUR for 2y USD bond, in % - 74
4.19 Rolling FX hedged yield pickup vs EUR for 5y USD bond, in. $\%$ 75
4.20 Maturity-matched FX hedged yield pickup vs EUR with unhedged return for 2y US
bond, in % - 76
4.21 EURUSD [spot exchange rate](../../../Financial%20Instruments/Review%20Session%20Notes/Arbitrage%20Opportunity%20Accounting.md) -- 76
5.1 EURUSD conversion factor -- 87
5.3 EURCHF conversion factor - 88
5.4 GBPJPY conversion factor -- 89
5.5 [Discount factor](../../Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%201/Discount%20Factors.md) comparison -- 89
5.6 Underlying data (sparse set to mimic) - 89
5.7 Forecast [conversion factors](../../Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%2011/Mechanics%20of%20Us%20Treasury%20Note%20and%20Bond%20Futures.md), by tenor - 92
5.8 10y EURUSD conversion factor, history and forecast - 92
5.9 [Xccy basis](../../../Contemporary%20Financial%20Intermediation%20Notes/Table%20of%20Contents.md) and conversion factor [currency](../../../Financial%20Instruments/Lecture%20Notes-%20Financial%20Instruments/Teaching%20Note%201-%20Forward%20Rates%20Agreement/Forwards%20and%20Futures%20Notes.md) decision for 2 spreads -- 93
5.10 [Xccy basis](../../../Contemporary%20Financial%20Intermediation%20Notes/Table%20of%20Contents.md) and conversion factor [currency](../../../Financial%20Instruments/Lecture%20Notes-%20Financial%20Instruments/Teaching%20Note%201-%20Forward%20Rates%20Agreement/Forwards%20and%20Futures%20Notes.md) decision for multiple spreads - 94
5.11 [Xccy basis](../../../Contemporary%20Financial%20Intermediation%20Notes/Table%20of%20Contents.md) and conversion factor [currency](../../../Financial%20Instruments/Lecture%20Notes-%20Financial%20Instruments/Teaching%20Note%201-%20Forward%20Rates%20Agreement/Forwards%20and%20Futures%20Notes.md) decision time series -- 95
6.1 Illustration of [forward rate](../../../Clippings/Forward%20Points%20in%20Currency.md) error model - 100
6.2 10y USD [term premium](../../../Contemporary%20Financial%20Intermediation%20Notes/Table%20of%20Contents.md) using different methods, up to 2006 - 102
6.3 10y USD [term premium](../../../Contemporary%20Financial%20Intermediation%20Notes/Table%20of%20Contents.md) using different methods, up to 2007 -- 102
6.4 Predicted - actual move -- 103
6.5 10y USD [term premium](../../../Contemporary%20Financial%20Intermediation%20Notes/Table%20of%20Contents.md) using different methods $(\%)$ 107
6.6 2y USD [term premium](../../../Contemporary%20Financial%20Intermediation%20Notes/Table%20of%20Contents.md) using different methods $(\%)$ 108
6.7 10y EUR Comparison with BIS [term premium](../../../Contemporary%20Financial%20Intermediation%20Notes/Table%20of%20Contents.md) data $(\%)$ 109
6.8 10y EUR Comparison with BIS [term premium](../../../Contemporary%20Financial%20Intermediation%20Notes/Table%20of%20Contents.md) data $(\%)$ (focus on recent history): 110
6.9 EUR 10y [term premium](../../../Contemporary%20Financial%20Intermediation%20Notes/Table%20of%20Contents.md) as of different points - 111
6.10 10y USD treasury [term premium](../../../Contemporary%20Financial%20Intermediation%20Notes/Table%20of%20Contents.md) from BIS data - 113
6.11 10y USD treasury [inflation](../../../International%20Finance/Bridgewater/Principles%20For%20Navigating%20Big%20Debt%20Cycles/Part%20II%20Detailed%20Case%20Studies/German%20Debt%20Crisis%20andHyperinflation%20(1918–1924)/War%20Economies%20and%20Hyperinflation.md) based [term premium](../../../Contemporary%20Financial%20Intermediation%20Notes/Table%20of%20Contents.md) . 114
7.1 Evolution of EUR yield curve, various tenors, in $\%$ 117
7.2 Evolution of USD yield curve, various tenors, in $\%$ 117
7.3 [Term premium](../../../Contemporary%20Financial%20Intermediation%20Notes/Table%20of%20Contents.md) results, 10y [term premium](../../../Contemporary%20Financial%20Intermediation%20Notes/Table%20of%20Contents.md), in $\%$ 119
7.4 Average 10y USD [term premium](../../../Contemporary%20Financial%20Intermediation%20Notes/Table%20of%20Contents.md), [term premium](../../../Contemporary%20Financial%20Intermediation%20Notes/Table%20of%20Contents.md) averaged over models,
with standard deviation bands -- 121
8.1 Linear and convex spot interest curve shapes -- 124
8.2 Concave and inverted curves - 124
8.3 Implied forward curves are too flat and too stale. 126
8.4 Ratio of means of actual moves/forward moves -. 127
8.5 Implied slope change (1-2y) - 129
8.6 Actual slope change (1-2y) - 129
8.7 Implied slope change (2-10y) - 130
8.8 Actual slope change (2-10y) 130
8.9 Implied slope change (10-30y) - 131
8.10 Actual slope change (10-30y) - 131
8.11 Average deviation of steepener trade vs [forwards](../../Financial%20Asset%20Pricing%20Theory%20Overview/Chapter%2012%20-%20Derivatives/Forwards%20and%20Futures.md) - 132
8.12 Average deviation of 10-30y steepener vs [forwards](../../Financial%20Asset%20Pricing%20Theory%20Overview/Chapter%2012%20-%20Derivatives/Forwards%20and%20Futures.md) (different periods) - 132
8.13 Average deviation of 10-30y steepener vs [forwards](../../Financial%20Asset%20Pricing%20Theory%20Overview/Chapter%2012%20-%20Derivatives/Forwards%20and%20Futures.md) - 133
8.14 [Macaulay Duration](../../../Fixed%20Income%20Asset%20Pricing/Fixed%20Income%20Lecture%20Notes/Teaching%20Note%202-%20Interest%20Rate%20Risk%20Management%20And%20Factors.md) - 134
8.15 Linear price-yield relationship - 135
8.16 Non-linear price-yield relationship - 136-
8.17 [Convexity adjustment](../../../Financial%20Engineering/Derivatives/Part%20II%20-%20Fixed%20Income%20Cash%20Markets/Chapter%2010%20-%20Bonds:%20Duration%20and%20Convexity.md) - bond [returns](../../Financial%20Asset%20Pricing%20Theory%20Overview/Chapter%203%20-%20%20Assets,%20Portfolios,%20and%20Arbitrage/Assets.md) constant - 140
8.18 [Convexity adjustment](../../../Financial%20Engineering/Derivatives/Part%20II%20-%20Fixed%20Income%20Cash%20Markets/Chapter%2010%20-%20Bonds:%20Duration%20and%20Convexity.md) - bond prices follow [forwards](../../Financial%20Asset%20Pricing%20Theory%20Overview/Chapter%2012%20-%20Derivatives/Forwards%20and%20Futures.md) - 141
8.19 [Convexity adjustment](../../../Financial%20Engineering/Derivatives/Part%20II%20-%20Fixed%20Income%20Cash%20Markets/Chapter%2010%20-%20Bonds:%20Duration%20and%20Convexity.md) - swap yield - 142
8.20 [Convexity adjustment](../../../Financial%20Engineering/Derivatives/Part%20II%20-%20Fixed%20Income%20Cash%20Markets/Chapter%2010%20-%20Bonds:%20Duration%20and%20Convexity.md) - 1y [forward swap](../../../Financial%20Engineering/Derivatives/Part%20IX%20-%20Fixed%20Income%20Derivatives/Chapter%2039%20-%20Swaptions,%20Forward%20Swaps,%20and%20MBS.md) : 143
8.21 [Convexity adjustment](../../../Financial%20Engineering/Derivatives/Part%20II%20-%20Fixed%20Income%20Cash%20Markets/Chapter%2010%20-%20Bonds:%20Duration%20and%20Convexity.md) - 30y German bonds 143
8.22 [Convexity adjustment](../../../Financial%20Engineering/Derivatives/Part%20II%20-%20Fixed%20Income%20Cash%20Markets/Chapter%2010%20-%20Bonds:%20Duration%20and%20Convexity.md) - 50y EUR swaps - 144
8.23  Ratin of standard deviations of forerast moves/actual moves (FliR 1v forward) - 146
8.24 Ratio of standard deviations of forecast moves/actual moves (EUR 2y forward) - 146
8.25 Ratio of standard deviation of forecast moves/actual moves (EUR 5y forward) --. 147
8.26 Ratio of means of actual moves/forward moves (EUR 1y forward) -- 147
8.27 Ratio of means of actual moves/forward moves (EUR 2y forward) - 148
8.28 Ratio of means of actual moves/forward moves (EUR 5y forward) -- 148
8.29 Ratio of standard deviations of forecast moves/actual moves (UsD 1y forward). 149
8.30 Ratio of standard deviations of forecast moves/actual moves (UsD 2y forward). 149
8.31 Ratio of standard deviations of forecast moves/actual moves (UsD 5y forward) 150
8.32 Ratio of means of actual moves/forward moves (USD 1y forward) - 150
8.33 Ratio of means of actual moves/forward moves (USD 2y forward) - 151
8.34 Ratio of means of actual moves/forward moves (USD 5y forward) - 151
8.35 Implied slope change (2001-7, 1-2y) - 152
8.36 Actual slope change (2001-7, 1-2y) - 152
8.37 Implied slope change (2001-7, 2-10y) : 153
8.38 Actual slope change (2001-7, 2-10y) - 153
8.39 Implied slope change (2001-7, 10-30y) 154
8.40 Actual slope change (2001-7, 10-30y) 154
8.41 Implied slope change (2007-14, 1-2y) 155
8.42 Actual slope change (2007-14, 1-2y) 155
8.43 Implied slope change (2007-14, 2-10y) 156
8.44 Actual slope change (2007-14, 2-10y) 156
8.45 Implied slope change (2007-14, 10-30y) 157
8.46 Actual slope change (2007-14, 10-30y) 157
8.47 Implied slope change (2014-20, 1-2y) 158
8.48 Actual slope change (2014-20, 1-2y) 158
8.49 Implied slope change (2014-20, 2-10y) 159
8.50 Actual slope change (2014-20, 2-10y) 159
8.51 Implied slope change (2014-20, 10-30y) - 160
8.52 Actual slope change (2014-20, 10-30y) 160
9.1 Implied [convexity](../../../Fixed%20Income%20Asset%20Pricing/Problem%20Sets/PSET%20II%20Fixed%20Income%20Asset%20Pricing%201.md) value, 10y German bonds 164
9.2 Implied [convexity](../../../Fixed%20Income%20Asset%20Pricing/Problem%20Sets/PSET%20II%20Fixed%20Income%20Asset%20Pricing%201.md) value, 50y EUR swaps - 164
9.3 History of 50y bond price with [convexity](../../../Fixed%20Income%20Asset%20Pricing/Problem%20Sets/PSET%20II%20Fixed%20Income%20Asset%20Pricing%201.md) value - 165.
9.4 Implied vs [realised convexity](.md) for 50y bond --. 166
9.5 History of [convexity](../../../Fixed%20Income%20Asset%20Pricing/Problem%20Sets/PSET%20II%20Fixed%20Income%20Asset%20Pricing%201.md) value for bonds of different tenor --. 167
9.6 [Realised convexity](.md) of a 30y bond over different periods - 167

# List of Tables

1.1 Example of conversion factor calculation as of 20 February 2017 -- 8
2.1 Sample XVA calculations from 20 November 2017, in bp annually - 29
2.2 Average profit per trade  39
3.1 Available series for [xccy basis](../../../Contemporary%20Financial%20Intermediation%20Notes/Table%20of%20Contents.md) swaps to the UsD - 41
3.2 Available series for [xccy basis](../../../Contemporary%20Financial%20Intermediation%20Notes/Table%20of%20Contents.md) swaps to the EUR - 42
3.3 Available series for [xccy basis](../../../Contemporary%20Financial%20Intermediation%20Notes/Table%20of%20Contents.md) swaps to the JPY - 43
3.4 Available series for [xccy basis](../../../Contemporary%20Financial%20Intermediation%20Notes/Table%20of%20Contents.md) swaps to the EuR, with basis series reconstruction from other bases - 44
3.5 Available series for [xccy basis](../../../Contemporary%20Financial%20Intermediation%20Notes/Table%20of%20Contents.md) swaps to the JPY, with basis series reconstruction from other bases - 45
4.1 Volatility contributions for matched maturity FX hedge, USD bonds, data since 2000, in $\%$ - 78
4.2 Volatility contributions for rolling FX hedge, UsD bonds,. data since 2000, in $\%$ 78
4.3 Volatility contributions for unhedged case, USD bonds, data since 2000, in $\%$ - 79
4.4 Base data for calculation -- 79
4.5Pickup results, 8th December 2016 -- 80
5.1 Conversion factor calculation out to 10y as of 7 Apr 2017, for EUR and USD, for annual payment dates, rates in $\%$ , discount factors and [conversion factors](../../Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%2011/Mechanics%20of%20Us%20Treasury%20Note%20and%20Bond%20Futures.md) are numbers with no unit - 85
5.2 Conversion factor calculation out to $51/2\upboldsymbol{\upgamma}$ as of 7 Apr 2017, for EUR and USD, for semiannual payment dates, rates in. $\%$ , discount factors and [conversion factors](../../Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%2011/Mechanics%20of%20Us%20Treasury%20Note%20and%20Bond%20Futures.md) are. numbers with no unit -- 86 OIS and IRS Commerzbank forecasts, as of April 2017, rates in. $\%$ 90
5.4 Calculated discount factors and forecast [conversion factors](../../Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%2011/Mechanics%20of%20Us%20Treasury%20Note%20and%20Bond%20Futures.md), EUR and UsD discount factors (top 4 rows) and forecast [conversion factors](../../Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%2011/Mechanics%20of%20Us%20Treasury%20Note%20and%20Bond%20Futures.md) -. 91
7.1 Volatilities of [term premium](../../../Contemporary%20Financial%20Intermediation%20Notes/Table%20of%20Contents.md) models, standard deviation of monthly changes. in $\%$ 120
8.1 [Duration and convexity](../../Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%208/An%20Analytical%20Decomposition%20of%20Forward%20Rates.md)- 137

# About the Authors

![](6d7e1570badcb40d48184551c29b630b034f1c2f3ad38cd704d357a95e4b94cd.jpg)

Jessica James is a senior quantitative researcher at Commerzbank in London, and previously was head of the Quantitative Solutions Group. She joined Commerzbank from Citigroup where she held a number of FX roles, latterly as global head of the Quantitative Investor Solutions Group. Prior to this, she was the head of the Risk Advisory and [Currency](../../../Financial%20Instruments/Lecture%20Notes-%20Financial%20Instruments/Teaching%20Note%201-%20Forward%20Rates%20Agreement/Forwards%20and%20Futures%20Notes.md) Overlay Team for Bank One. Before her career in finance, James lectured in physics at Trinity College, Oxford. She holds a BSc in physics from Manchester University and a D. Phil. in atomic and nuclear physics from Oxford University.

Her significant publications include the Handbook of Exchange Rates (Wiley), Interest Rate Modelling (Wiley), and '[Currency](../../../Financial%20Instruments/Lecture%20Notes-%20Financial%20Instruments/Teaching%20Note%201-%20Forward%20Rates%20Agreement/Forwards%20and%20Futures%20Notes.md) Management' (Risk Books). Her latest book FX Option Performance came out in 2015. She has been closely associated with the development of [currency](../../../Financial%20Instruments/Lecture%20Notes-%20Financial%20Instruments/Teaching%20Note%201-%20Forward%20Rates%20Agreement/Forwards%20and%20Futures%20Notes.md) as an asset class, being one of the first to create overlay and [currency](../../../Financial%20Instruments/Lecture%20Notes-%20Financial%20Instruments/Teaching%20Note%201-%20Forward%20Rates%20Agreement/Forwards%20and%20Futures%20Notes.md) alpha products.

Jessica is a visiting professor both at University College London and at Cass Business School. She is a managing editor for [Quantitative Finance](../../../Course%20Notes/Quantitative%20Trading%20Strategies%20Lecture%20Notes.md). Apart from her financial appointments, she is a fellow of the Institute of Physics and has been a member of their governing body and of their Industry and Business Board.

Christoph Rieger heads the Rates & Credit Research at Commerzbank. Together with his research teams, he covers the full range of [fixed income products](../Chapter%208/Forward%20Curves%20Duration%20and%20Convexity.md), from money markets, government bonds and SSAs to covered bonds, financials and corporates, developing big-picture themes alongside commercial trading and funding strategies.

![](ebca25107a64fdca8134346fb8d6393249321a8d0cf52deaf27f6d5ab8a3f3f1.jpg)

Prior to this role, Christoph was Head of Rates Strategy at Commerzbank and he worked as senior interest rate strategist at Dresdner Kleinwort with a specific focus on money markets and interest rate [derivatives](../../Financial%20Trading%20and%20Markets/Chapter%209%20Arbitrage%20and%20Hedging%20With%20Options.md). Before joining Dresdner Kleinwort in 2o04, Christoph held various positions in

[fixed income](../../../Fixed%20Income%20Asset%20Pricing/Lecture%20Notes%20Bonds,%20%20Preferred%20Stock,%20%20and%20Structured%20Products.md) research, starting in 1998 at Commerzbank as a government bond analyst before.
moving to London in 2o01, where his main focus was on interest rate strategies using [derivatives](../../Financial%20Trading%20and%20Markets/Chapter%209%20Arbitrage%20and%20Hedging%20With%20Options.md).
His academic background is rooted in economics, in which he holds two degrees: an MA from Temple University (Fulbright Scholarship in Philadelphia, PA) and a diploma from the University of.
Cologne (Germany). Christoph is a member of the ECB Bond Market Contact Group..

![](4eac81d5d6b6f09c387485e16d0787f44523b65165b91159a87e915b51dc5e07.jpg)

Michael Leister is responsible for interest rate strategy at Commerzbank. His research team of four analysts covers the full range of liquid and structured rates products for the major currencies, in cash as well as in [derivatives](../../Financial%20Trading%20and%20Markets/Chapter%209%20Arbitrage%20and%20Hedging%20With%20Options.md) space.

Michael joined Commerzbank London in 2012 with a focus on  rates and global [inflation](../../../International%20Finance/Bridgewater/Principles%20For%20Navigating%20Big%20Debt%20Cycles/Part%20II%20Detailed%20Case%20Studies/German%20Debt%20Crisis%20andHyperinflation%20(1918–1924)/War%20Economies%20and%20Hyperinflation.md) markets, after working as Interest Rate Strategist for WestLB in Dusseldorf and London with a focus on government bonds..

He holds a masters degree in economics from the University of Mannheim and was awarded the CFA charter in 2012. Beyond [financial markets](../../../Financial%20Markets%20and%20Institutions/Financial%20Markets%20and%20Institutions%20Lecture%20Notes.md) he is a frequent participant in city and mountain marathons (PB 2:47).

# References

Adrian, T., Crump, R. K. and Moench, E. (2008), updated 2013. [Pricing](../../Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%207/Arbitrage%20Pricing%20of%20Derivatives.md) the [term structure](../../Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%209/The%20Vasicek%20Model.md) with linear regressions. Federal Reserve Bank of New York Staff Reports, no. 340. https://www.newyorkfed. org/research/data_indicators/term_premia.html.
Arai, F., Makabe, Y., Okawara, Y. and Nagano, T. (2016). Recent trends in [cross-currency basis](../Chapter%203/Calculating%20Novel%20Cross-Currency%20Bases%20a.md), Bank of Japan Review, http://www.boj.or.jp/en/research/wps_rev/rev_2016/data/rev16e07.pdf.
Bernanke, B. S., Boivin, J. and Eliasz, P. (2o05). Measuring the effects of [monetary policy](../../../Financial%20Markets%20and%20Institutions/III.%20Liquidity%20of%20Assets/Class%209-%20Bailouts%20and%20Bank%20Failures/Articles/The%20Economist%20Regime%20Change.md): A factor-augmented vector autoregressive (FAvAR) approach. The Quarterly Journal of Economics, 120(1), 387-422.
Borio, C., McCauley, R., McGuire, P. and Sushko, V. (2016). [Covered interest parity](../../../Financial%20Instruments/Lecture%20Notes-%20Financial%20Instruments/Teaching%20Note%201-%20Forward%20Rates%20Agreement/Interest%20Rates,%20Carry%20Trades,%20and%20Exchange%20Rate%20Movements.md) lost: Understanding the [cross-currency basis](../Chapter%203/Calculating%20Novel%20Cross-Currency%20Bases%20a.md). BlS Quarterly Review, http://www.bis.org/publ/qtrpdf/r_qt1609e.pdf.
Christensen, J. H. E. and Rudebusch, G. D. (2019). A new normal for [interest rates](../../Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%202/Interest%20Rate%20Quotations.md)? Evidence from [inflation-indexed](../../../Chinese%20Financial%20System.md) debt. Federal Reserve Bank of San Francisco, Working Paper 2017-07. https://doi.org/10.24148/wp2017-07.
Chua, J. H. (1984). A closed-form formula for calculating bond [duration](../../Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%205/Key%20Rates%20O1s%20Durations%20and%20Hedging.md). Financial Analysts Journal, 40(3), 76-78.
Cohen, B. H., Hordahl, P. and Xia, D. (2018). Term premia: models and some stylised facts. BIS Quarterly Review, September 2018, 79.
Crump, R. K., Eusepi, S. and Moench, E. (2016). The [term structure](../../Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%209/The%20Vasicek%20Model.md) of [expectations](../../../Fixed%20Income%20Asset%20Pricing/Fixed%20Income%20Lecture%20Notes/FORWARD%20RATES%20AND%20TERM%20STRUCTURE.md) and bond yields, Federal Reserve Bank of New York Staff Reports, no. 775 May 2016; revised April 2018.
Du, W., Tepper, A. and Verdelhan, A. (2016). Deviations from [covered interest rate parity](../../../Financial%20Instruments/Financial%20Instruments%20PSET%20Solutions.md), SSRN, https://ssrn.com/abstract=2768207.
Ernst and Young (2014). Applying IFRS 13: Credit valuation adjustments for derivative contracts, http://www.ey.com/Publication/vwLUAssets/ey-applying-ifrs-fair-value-measurement/\$FILE/ ey-applying-ifrs-fair-value-measurement.pdf.
European [Banking](../../../Advanced%20Financial%20Analysis%20and%20Valuation/Problem%20Sets/HKS%20The%20Banking%20Industry.md) Authority (2014). EBA report on CVA, April 2014, https://www.eba.europa.eu/ documents/10180/950548/EBA+Report+on+CVA.pdf.
Fama, E.F. (1984). Forward and spot exchange rates. Journal of Monetary Economics, 14(3), 319-338.
Greenwood, R. and Vayanos, D. (2014). Bond supply and excess bond [returns](../../Financial%20Asset%20Pricing%20Theory%20Overview/Chapter%203%20-%20%20Assets,%20Portfolios,%20and%20Arbitrage/Assets.md). The Review of Financial Studies, 27 (3), March 2014, 663-713, https://doi.org/10.1093/rfs/hht133.
Gregory, J. (2o11). Counterparty [credit risk](../../../Course%20Notes/Quantitative%20Trading%20Strategies%20Lecture%20Notes.md). Wiley Finance..
Haltom, R., Wissuchek, E. and Wolman, A. L. (2018). Have yield curve inversions become more likely? Federal Reserve Bank of Richmond, 18 (12), https:/ /www.richmondfed.org/publications/ research/economic_brief/2018/eb_18-12.
Hordahl, P. and Tristani, O. (2o14). [Inflation](../../../International%20Finance/Bridgewater/Principles%20For%20Navigating%20Big%20Debt%20Cycles/Part%20II%20Detailed%20Case%20Studies/German%20Debt%20Crisis%20andHyperinflation%20(1918–1924)/War%20Economies%20and%20Hyperinflation.md) risk premia in the Euro area and the United States. International Journal of Central [Banking](../../../Advanced%20Financial%20Analysis%20and%20Valuation/Problem%20Sets/HKS%20The%20Banking%20Industry.md), http://www.ijcb.org/journal/ijcb14q3a1.htm.
Hull, J. C. and White, A. (2014). OlS discounting, interest rate [derivatives](../../Financial%20Trading%20and%20Markets/Chapter%209%20Arbitrage%20and%20Hedging%20With%20Options.md), and the modelling of stochastic interest rate spreads. Journal of [Investment](../../../Advanced%20Investments/An%20Asset%20Allocation%20Primer.md) Management, March 2014.
Ilmanen, A. (1995). Understanding the yield curve, United States Fixed-Income Research [Portfolio Strategies](../../../Fixed%20Income%20Asset%20Pricing/Lecture%20Notes%20Bonds,%20%20Preferred%20Stock,%20%20and%20Structured%20Products.md). [Salomon Brothers](../../../Fixed%20Income%20Asset%20Pricing/Fixed%20Income%20Lecture%20Notes/Understanding%20The%20Yield%20Curve-%20Part%201.md).
ISDA. (2o1o), Market review of OTC derivative bilateral collateralisation practices, ISDA Collateral Steering Committee.
James, J., Fullwood, J. and Billington, P. (2015). FX Option Performance: An Analysis of the Value Delivered by FX Options Since the Start of the Market. (New York: Wiley).
James, J., Leister, M. and Rieger, C. (2016). Demystifying the [term premium](../../../Contemporary%20Financial%20Intermediation%20Notes/Table%20of%20Contents.md), Commerzbank Rates Radar.
Kim, D. H. and Wright, J. H. (2oo5). An [arbitrage](../../Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%207/Arbitrage%20Pricing%20of%20Derivatives.md)-free three-factor [term structure](../../Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%209/The%20Vasicek%20Model.md) model and the recent behavior of long-term yields and distant-horizon forward rates. The Federal Reserve Board, Washington.
Kopp, E. and Williams, P. D. (2018). A macroeconomic approach to the [term premium](../../../Contemporary%20Financial%20Intermediation%20Notes/Table%20of%20Contents.md). IMF Working Papers, no. 18/140.
Li, C., Meldrum, A. and Rodriguez, M. (2o17). Robustness of long-maturity [term premium](../../../Contemporary%20Financial%20Intermediation%20Notes/Table%20of%20Contents.md) estimates.. FEDS Notes, Board of Governors of the [Federal Reserve System](../../Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%2012/Fed%20Fund%20Futures.md). https:/ /www.federalreserve.. gov/econres/notes/feds-notes/robustness-of-long-maturity-term-premium-estimates20170403.htm.
Miron, P. and Swannell, P. (1991). [Pricing](../../Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%207/Arbitrage%20Pricing%20of%20Derivatives.md) and [hedging](../../Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%205/Key%20Rates%20O1s%20Durations%20and%20Hedging.md) swaps. Euromoney Books.
Rime, D., Schrimpf, A. and Syrstad, O. (2017). Segmented money markets and [covered interest parity](../../../Financial%20Instruments/Lecture%20Notes-%20Financial%20Instruments/Teaching%20Note%201-%20Forward%20Rates%20Agreement/Interest%20Rates,%20Carry%20Trades,%20and%20Exchange%20Rate%20Movements.md) [arbitrage](../../Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%207/Arbitrage%20Pricing%20of%20Derivatives.md), Bank for International Settlements, BIS working papers no. 651, http://www.bis.org/publ/work651.pdf.
Ruiz, I. (2015). XVA desks: A new era for [risk management](../../../Financial%20Engineering/Financial%20Mathematics%20Course.md). Palgrave Macmillan.
Swanson, E. (2oo7). What we do and don't know about the [term premium](../../../Contemporary%20Financial%20Intermediation%20Notes/Table%20of%20Contents.md). Federal Reserve Bank of San Francisco, FRBSF Economic Letter. http://www.frbsf.org/economic-research/publications/ economic-letter/2007/july/term-premium/.

# Index

bond 6, 14, 25, 40-41, 47, 67-84, 105,
116-117, 123, 133-143, 161-167
bond price 123, 135-137, 141, 165
bond yield 14, 25, 41, 69-77, 105, 116, 123,
136, 138, 140-142, 161, 163
capital charges 67
CDS 24-25, 29
CIP 16-17
conversion factor 7-8, 9, 10, 11, 81-95
[convexity](../../../Fixed%20Income%20Asset%20Pricing/Problem%20Sets/PSET%20II%20Fixed%20Income%20Asset%20Pricing%201.md) 122-123, 133, 135-144, 161-167
[convexity adjustment](../../../Financial%20Engineering/Derivatives/Part%20II%20-%20Fixed%20Income%20Cash%20Markets/Chapter%2010%20-%20Bonds:%20Duration%20and%20Convexity.md) 141-143
[convexity](../../../Fixed%20Income%20Asset%20Pricing/Problem%20Sets/PSET%20II%20Fixed%20Income%20Asset%20Pricing%201.md) value 123, 139-144, 161, 163-167
counterparty risk 21
covariance term 81-82
[credit spread](../../Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%2014/Cds-Equivalent%20Bond%20Spread.md) 8-9, 10, 11, 25-26, 67, 81-84,
90, 92-93
[cross-currency basis](../Chapter%203/Calculating%20Novel%20Cross-Currency%20Bases%20a.md) 1, 3-4, 6, 9-10, 13, 17,
19-21, 27, 29-30, 35, 66-67, 69, 74,
82-84
curve slope 120, 122-123, 125, 128
CVA 21, 23-29
[discount factor](../../Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%201/Discount%20Factors.md) 8, 24, 84-87, 90-91, 109-110,
112, 123
[duration](../../Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%205/Key%20Rates%20O1s%20Durations%20and%20Hedging.md) 26, 122-123, 133-138, 162, 164-165
DVA 26-27
empirical method 100, 103
exposure 13, 21-22, 24, 26, 74-75
[fixed income](../../../Fixed%20Income%20Asset%20Pricing/Lecture%20Notes%20Bonds,%20%20Preferred%20Stock,%20%20and%20Structured%20Products.md) 33, 66, 79, 100, 122, 125, 139
[forecasting](../../../Advanced%20Financial%20Analysis%20and%20Valuation/Lecture%20Notes%20Advanced%20Financial%20Analysis%20and%20Valuation/Week%202/Week%202%20Fundamentals%20Of%20Forecasting.md) [conversion factors](../../Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%2011/Mechanics%20of%20Us%20Treasury%20Note%20and%20Bond%20Futures.md) 90
forward curve 34-35, 103-104, 107-108, 110,
114, 122-127, 141-142, 144
forward curve slope 122, 125
[forward FX rate](../Chapter%201/What%20Really%20Is%20the%20Cross-Currency%20Basis.md) 1-2, 31, 35-36, 45, 67-69, 74
forward points 16, 34-37
forward rates 16-17, 34, 68, 83-84, 101-103,
105, 109-110, 113, 116, 123-125
FVA 27-29
FX carry 11-12, 16, 66
FX [carry trade](../../../Clippings/Currency%20Carry%20Trade.md) 11, 16, 66
FX hedge 12, 40, 42, 47-48, 66-68, 70-84
FX hedge cost 84
[FX hedged pickup](../../../Contemporary%20Financial%20Intermediation%20Notes/Table%20of%20Contents.md) 40, 42, 47-48
[hedging](../../Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%205/Key%20Rates%20O1s%20Durations%20and%20Hedging.md) 1, 6, 9-11, 24, 33, 40, 66-67, 79, 83,
122
Hordahl and Tristani model 113
implied [convexity](../../../Fixed%20Income%20Asset%20Pricing/Problem%20Sets/PSET%20II%20Fixed%20Income%20Asset%20Pricing%201.md) 161, 163, 166
inverted curve 124
issuer 6, 9-10, 27, 81, 83-84, 92
Lagrange interpolation 112
lookback period 110-111, 116
maturity-matched hedge 73, 84
[modified duration](../../../Financial%20Engineering/A%20Guide%20to%20Duration%20DV01%20and%20Yield%20Curve.md) 135, 140
negative basis 14
netting 22-24
[no-arbitrage pricing](../../../Pricing%20Forwards,%20Futures,%20Bonds,%20Swaps,%20Swaptions,%20Caps%20and%20Floors%20under%20No-Arbitrage%20and%20Risk-Neutral%20Pricing.md) 3
pickup 14-15, 40-41, 47-48, 66-67, 70,
73-76, 78-79, 81-84
[realised convexity](.md) 161, 164, 166
rolling hedge 41, 66, 74-76, 78, 82, 84
steepener trade 131-132, 142, 144-145
[term premium](../../../Contemporary%20Financial%20Intermediation%20Notes/Table%20of%20Contents.md) 100-118, 120, 122-125, 127-128
translation effect 83
UIP 16-17
value of [convexity](../../../Fixed%20Income%20Asset%20Pricing/Problem%20Sets/PSET%20II%20Fixed%20Income%20Asset%20Pricing%201.md) 133, 139, 141, 161, 164-165
volatility contribution 81
XVA 21, 23, 25, 27-30, 67, 82
yield curve 8, 21, 31, 40, 66, 74, 81-84, 93,
100-103, 105, 108, 120-125, 128, 133, 141,
144
yield pickup 13-15, 67-73, 75-84

# The Moorad Choudhry Global Banking Series

Principles of Green [Banking](../../../Advanced%20Financial%20Analysis%20and%20Valuation/Problem%20Sets/HKS%20The%20Banking%20Industry.md): Managing Environmental Risk and Sustainability by Suborna Barua

Bank [Asset Liability Management](../../Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%205/Key%20Rates%20O1s%20Durations%20and%20Hedging.md) Best Practice: Yesterday, Today and Tomorrow by Polina Bardaeva

Reverse Stress Testing in [Banking](../../../Advanced%20Financial%20Analysis%20and%20Valuation/Problem%20Sets/HKS%20The%20Banking%20Industry.md): A Comprehensive Guide by Michael Eichhorn, Tiziano Bellini, and Daniel Mayenberger (eds.)

Random Walks in [Fixed Income](../../../Fixed%20Income%20Asset%20Pricing/Lecture%20Notes%20Bonds,%20%20Preferred%20Stock,%20%20and%20Structured%20Products.md) and Foreign Exchange: Unexpected Discoveries in Issuance, [Investment](../../../Advanced%20Investments/An%20Asset%20Allocation%20Primer.md) and [Hedging](../../Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%205/Key%20Rates%20O1s%20Durations%20and%20Hedging.md) of Yield Curve Instruments by Jessica James, Michael Leister, and Christoph Rieger.
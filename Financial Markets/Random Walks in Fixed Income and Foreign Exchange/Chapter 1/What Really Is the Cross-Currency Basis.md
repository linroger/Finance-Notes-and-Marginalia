---
tags:
  - arbitrage
  - cross_currency_basis
  - currency_risk
  - fx_forward
  - interest_rates
aliases:
  - XCCY basis
  - basis
  - cross-currency basis swaps
key_concepts:
  - arbitrage conditions violation
  - cross-currency swap
  - currency hedging adjustment
  - forward FX rate
  - interest rate differentials
---

# Chapter 1 What Really is the Cross-Currency Basis?

The [cross-currency basis](../Chapter%203/Calculating%20Novel%20Cross-Currency%20Bases%20a.md) - often just called the basis' - is a strange creature.' It is. referred to often enough in the [financial markets](../../../Financial%20Markets%20and%20Institutions/Financial%20Markets%20and%20Institutions%20Lecture%20Notes.md) that most participants think that they probably ought to know what it is. I was certainly one of them. 'Some credit. adjustment to [currency](../../../Financial%20Instruments/Lecture%20Notes-%20Financial%20Instruments/Teaching%20Note%201-%20Forward%20Rates%20Agreement/Forwards%20and%20Futures%20Notes.md) [hedging](../../Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%205/Key%20Rates%20O1s%20Durations%20and%20Hedging.md)' was how I vaguely thought of it. However, the more one studies and understands it, the stranger and more important it becomes. It is nothing less than a violation of the [arbitrage](../../Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%207/Arbitrage%20Pricing%20of%20Derivatives.md) conditions governing the relationships between [interest rates](../../Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%202/Interest%20Rate%20Quotations.md) and foreign exchange rates, and before it was observed, it would have been thought of as impossible. This paper describes how to calculate the basis, discusses some potential drivers, and ends with some unexpected applications.

The story of [cross-currency basis](../Chapter%203/Calculating%20Novel%20Cross-Currency%20Bases%20a.md) swaps originates with the start of the floating. [currency](../../../Financial%20Instruments/Lecture%20Notes-%20Financial%20Instruments/Teaching%20Note%201-%20Forward%20Rates%20Agreement/Forwards%20and%20Futures%20Notes.md) market regime in the late 1970s and early 1980s, as corporations and in-. vestors with global reach sought methods of insuring themselves against sharp [currency](../../../Financial%20Instruments/Lecture%20Notes-%20Financial%20Instruments/Teaching%20Note%201-%20Forward%20Rates%20Agreement/Forwards%20and%20Futures%20Notes.md) movements. [Forward FX rate](.md) contracts became popular. The [forward rate](../../../Clippings/Forward%20Points%20in%20Currency.md) calculation is trivial (see equation (1)), and any deviation in the market from the calculated rate implied by [interest rate differentials](.md) gives traders a chance to do [arbitrage](../../Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%207/Arbitrage%20Pricing%20of%20Derivatives.md) trades, which made such deviations unlikely..

And yet, since 2o08, such deviations have persistently emerged. It is these deviations, expressed in a spread to one of the Libor [interest rates](../../Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%202/Interest%20Rate%20Quotations.md) used to calculate the [forward FX rate](.md), which are known as the cross-[currency](../../../Financial%20Instruments/Lecture%20Notes-%20Financial%20Instruments/Teaching%20Note%201-%20Forward%20Rates%20Agreement/Forwards%20and%20Futures%20Notes.md) bases. We plot the basis for EURUsD in Figure 1.1; it is remarkable how large and persistent it can be, given that before 2008, [arbitrage](../../Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%207/Arbitrage%20Pricing%20of%20Derivatives.md) activity maintained it at almost zero.

# The Calculation Underlying the Cross-Currency Basis Swap

A Quick Note on Terminology

An FX forward is a contract that locks in the price at which a counterparty can buy.
or sell a [currency](../../../Financial%20Instruments/Lecture%20Notes-%20Financial%20Instruments/Teaching%20Note%201-%20Forward%20Rates%20Agreement/Forwards%20and%20Futures%20Notes.md) on a future date. The exchange rate is typically today's rate, ad-.
justed for the interest rate differential in the two currencies. If the interest rate in the local [currency](../../../Financial%20Instruments/Lecture%20Notes-%20Financial%20Instruments/Teaching%20Note%201-%20Forward%20Rates%20Agreement/Forwards%20and%20Futures%20Notes.md) is higher than that of the UsD (or whatever the reference [currency](../../../Financial%20Instruments/Lecture%20Notes-%20Financial%20Instruments/Teaching%20Note%201-%20Forward%20Rates%20Agreement/Forwards%20and%20Futures%20Notes.md).
is), the FX forward will include a devaluation expectation..

![](b45f67bf50395a754e0752005806eeb6c71148300f252eab7242edae737b5a78.jpg)
Figure 1.1: 1y EURUSD [xccy basis](../../../Contemporary%20Financial%20Intermediation%20Notes/Table%20of%20Contents.md).. Source: Commerzbank Research, Bloomberg

In a [cross-currency swap](../../../Clippings/Currency%20Swap%20Basics.md), the parties exchange a stream of cashflows in one cur-. rency for a stream of cashflows in another. The typical [cross-currency swap](../../../Clippings/Currency%20Swap%20Basics.md) involves. the exchange of both recurring [interest and principal](../../../Financial%20Engineering/Notes%20on%20Currency%20Swaps.md) (usually at the end of the swap), and thus can fully cover the [currency](../../../Financial%20Instruments/Lecture%20Notes-%20Financial%20Instruments/Teaching%20Note%201-%20Forward%20Rates%20Agreement/Forwards%20and%20Futures%20Notes.md) risk of a loan transaction. Conceptu-. ally, cross-[currency swaps](../../../Financial%20Instruments/Financial%20Instruments%20PSET%20Solutions.md) can be viewed as a series of forward contracts packaged. together. For much more detail on more of these, see Appendix 1.B..

# Perhaps the Simplest Formula in Financial Mathematics

The calculation to discover the [forward rate](../../../Clippings/Forward%20Points%20in%20Currency.md) is trivial. It is found using the following expression:
$$
{\frac{F}{S}}={\frac{1+r_{f}}{1+r_{d}}}
$$

where $F$ is the [forward FX rate](.md), $S$ is the spot (current) FX rate, $\mathbf{r_{f}}$ is the foreign interest rate and $\mathrm{r_{d}}$ is the domestic interest rate. The FX rate must be quoted as units of foreign [currency](../../../Financial%20Instruments/Lecture%20Notes-%20Financial%20Instruments/Teaching%20Note%201-%20Forward%20Rates%20Agreement/Forwards%20and%20Futures%20Notes.md) per domestic [currency](../../../Financial%20Instruments/Lecture%20Notes-%20Financial%20Instruments/Teaching%20Note%201-%20Forward%20Rates%20Agreement/Forwards%20and%20Futures%20Notes.md) - for example, 1.1 USD (US dollar) per EUR (Euro). EURUsD is the conventional way of naming this rate in the market.

This calculation arises very simply. There are two ways of getting from holding. the domestic [currency](../../../Financial%20Instruments/Lecture%20Notes-%20Financial%20Instruments/Teaching%20Note%201-%20Forward%20Rates%20Agreement/Forwards%20and%20Futures%20Notes.md) now, to holding the foreign [currency](../../../Financial%20Instruments/Lecture%20Notes-%20Financial%20Instruments/Teaching%20Note%201-%20Forward%20Rates%20Agreement/Forwards%20and%20Futures%20Notes.md) in the future, illustrated in Figure 1.2.

Method 1. Invest now for the period in question, at the domestic interest rate, then exchange at the end of the period..

Method 2. Exchange now so that you hold the foreign [currency](../../../Financial%20Instruments/Lecture%20Notes-%20Financial%20Instruments/Teaching%20Note%201-%20Forward%20Rates%20Agreement/Forwards%20and%20Futures%20Notes.md), and invest at the foreign [currency](../../../Financial%20Instruments/Lecture%20Notes-%20Financial%20Instruments/Teaching%20Note%201-%20Forward%20Rates%20Agreement/Forwards%20and%20Futures%20Notes.md) rate for the period.

![](f38f00f97727e1ca1ee7f378cfe653034a9945b080419f551234687a9ed4098f.jpg)
Figure 1.2: [Forward FX rate](.md) calculation.

[Arbitrage pricing](../../Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%207/Risk-Neutral%20Pricing.md) would tell us that Method 1 and Method 2 must be exactly the. same, apart from perhaps some small trading spread effects, or there will be a chance to 'round trip' the system and make some risk-free money ([arbitrage](../../Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%207/Arbitrage%20Pricing%20of%20Derivatives.md)). Conventionally, and in the pre-crisis world, this will only occur in a small and transient manner, as sharp-eyed traders look out for the chance and thus keep pressure on the forward. rate to comply with equation (1).

This type of situation has traditionally (pre-crisis) arisen in small and temporary forms, quickly eliminated by [arbitrage](../../Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%207/Arbitrage%20Pricing%20of%20Derivatives.md) trading. Thus this method of calculating the [forward rate](../../../Clippings/Forward%20Points%20in%20Currency.md) was thought to be completely robust. How could it possibly be incorrect in any substantial way?

But as we will see, even this apparently unbreakable piece of mathematics is vulnerable to unforeseen market effects. The existence of a non-zero [cross-currency basis](../Chapter%203/Calculating%20Novel%20Cross-Currency%20Bases%20a.md) 'breaks' equation (1).

# How the Calculation Distorts No-Arbitrage Pricing

The relationship in equation (1) is protected by [arbitrage](../../Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%207/Arbitrage%20Pricing%20of%20Derivatives.md) constraints, which one would think, in this era where both humans and machines comb the market for strategies and opportunities, would be sufficient to ensure its integrity. However, market size and [liquidity](../../../Financial%20Markets%20and%20Institutions/III.%20Liquidity%20of%20Assets/Class%205-%20Private%20Information,%20Liquidity,%20and%20Securitization/Class%20Note%2010%20Liquidity%20and%20Class%20Note%2010%20Liquidity%20and%20Liquidity%20Managementliquidity%20management.md) are not enough to ensure perfect efficiency. In Appendix 1.A, we show that the [FX market](../../../International%20Finance/Foreign%20Exchange%20Markets%20and%20Exchange%20Rate%20Determination.md) has by some definitions been markedly inefficient since its origins as a floating rate, by allowing a profitable [carry trade](../../../Clippings/Currency%20Carry%20Trade.md) to persist. And we can present simple evidence that an acute distortion of equation (1) has occurred and moreover persists to this day.

Let us go back to the equation.
$$
{\frac{F}{S}}={\frac{1+r_{f}}{1+r_{d}}}
$$

If EUR is the domestic [currency](../../../Financial%20Instruments/Lecture%20Notes-%20Financial%20Instruments/Teaching%20Note%201-%20Forward%20Rates%20Agreement/Forwards%20and%20Futures%20Notes.md), and USD the foreign [currency](../../../Financial%20Instruments/Lecture%20Notes-%20Financial%20Instruments/Teaching%20Note%201-%20Forward%20Rates%20Agreement/Forwards%20and%20Futures%20Notes.md), then a quick rearrangement gives us the following equation:
$$
r_{d}={\frac{S}{F}}\times\left(1+r_{f}\right)-1
$$

Now, all of these rates are readily observable in the market. To check it out precisely, we calculated $\mathrm{r_{d}}$ using equation (2), and compared it to the market rate since. 2000. Before about 2008, the calculated value of $\mathrm{r_{d}}$ matches the value of $\mathrm{r_{d}}$ obtained from the time series EUsw1v3 Curncy (on Bloomberg), the EUR 1-year [swap rate](../../../Fixed%20Income%20Asset%20Pricing/Fixed%20Income%20Lecture%20Notes/Teaching%20Note%204%20Interest%20Rate%20Derivatives.md). But after that date, they vary considerably, sometimes by up to. $1\%$ . If we plot the difference in Figure 1.3, calculated using $\mathrm{r_{d}}.$ theoretical $\mathrm{~-~}\mathbf{r}_{\mathrm{d-market}}$ , then we obtain the grey line. We have added to the graph the quoted xccy (shorthand for crosscurrency) EURUSD 1y [basis swap](../../Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%2013/Basis%20Swaps.md) (black line)..

The degree to which the [arbitrage pricing](../../Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%207/Risk-Neutral%20Pricing.md) is violated is almost exactly equal to the market quantity known as the [cross-currency basis swap](../../../Contemporary%20Financial%20Intermediation%20Notes/Table%20of%20Contents.md).

![](c767ba8afc9f7592467f32bad36092f7cfb8055a18c3bf2578d233cc994d41c3.jpg)
Figure 1.3: Theoretical and actual EUR interest rate difference. Source: Commerzbank Research, Bloomberge

It's clear to see that apart from a few not-so-good data points, they are essentially the same. So what is going on?

Essentially, equation (1) is no longer holding, and has not held since 2008, even between EUR and USD, the world's largest currencies. This degree of violation is called the 'basis' or '[basis swap](../../Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%2013/Basis%20Swaps.md)' and it is expressed as the difference between the non-USD interest rate (in this case, the 1-year EUR [swap rate](../../../Fixed%20Income%20Asset%20Pricing/Fixed%20Income%20Lecture%20Notes/Teaching%20Note%204%20Interest%20Rate%20Derivatives.md)) implied by the FX forward, and the actual market value of this rate.

Here's a quick example taken from one of the more extreme recent periods (grey circle in the graph in Figure 1.3). The codes are the Bloomberg tickers for the rates, so that the interested reader can check the calculation.

# On 29th December 2011

EUR-USD [xccy basis](../../../Contemporary%20Financial%20Intermediation%20Notes/Table%20of%20Contents.md) $=101.9\mathrm{bp}$ (EUBS1 Curncy) EURUSD spot FX rate $=1.296$ (EURUSD Curncy) EUR 1y [swap rate](../../../Fixed%20Income%20Asset%20Pricing/Fixed%20Income%20Lecture%20Notes/Teaching%20Note%204%20Interest%20Rate%20Derivatives.md) $=1.094\%$ (EUSW1V3 Curncy) USD 1y [swap rate](../../../Fixed%20Income%20Asset%20Pricing/Fixed%20Income%20Lecture%20Notes/Teaching%20Note%204%20Interest%20Rate%20Derivatives.md) $=0.691\%$ (USSA1 Curncy) EURUSD 1y FX forward $=1.304$ (EUR12m Index)

Using equation (2), we calculate the theoretical' EUR 1y [swap rate](../../../Fixed%20Income%20Asset%20Pricing/Fixed%20Income%20Lecture%20Notes/Teaching%20Note%204%20Interest%20Rate%20Derivatives.md) as follows:
EUR 1y [swap rate](../../../Fixed%20Income%20Asset%20Pricing/Fixed%20Income%20Lecture%20Notes/Teaching%20Note%204%20Interest%20Rate%20Derivatives.md) (theoretical) $\begin{array}{r}{=r_{d}=\frac{S}{F}\times\left(1+r_{f}\right)-1=1.296/1.304\times\left(1+0.691\%\right)-1}\end{array}$
EUR 1y [swap rate](../../../Fixed%20Income%20Asset%20Pricing/Fixed%20Income%20Lecture%20Notes/Teaching%20Note%204%20Interest%20Rate%20Derivatives.md) (theoretical) $=0.073\%$
But the actual [swap rate](../../../Fixed%20Income%20Asset%20Pricing/Fixed%20Income%20Lecture%20Notes/Teaching%20Note%204%20Interest%20Rate%20Derivatives.md) is not $0.0733\%$ , it is $1.094\%$ . The difference is$0.073\%-1.094\%=-1.021\%=-102.1\mathrm{bp}$
And this is almost exactly equal to the quoted basis in the market, $-1.019\%$

Of course, that is not the only way to express the inequality. We could equally well plot the difference between the theoretical [FX forward rate](../../../Financial%20Instruments/Lecture%20Notes-%20Financial%20Instruments/Teaching%20Note%201-%20Forward%20Rates%20Agreement/Foreign%20Exchange%20Quoting%20Conventions.md), derived from the [spot rate](../../../International%20Finance/The%20Foreign%20Exchange%20Market%20Annotations.md) and the [interest rates](../../Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%202/Interest%20Rate%20Quotations.md) available in the market, and the actual quoted rate, Ftheoretical $\begin{array}{r}{-\mathrm{F}_{\mathrm{market}}.}\end{array}$ Then we would create the following graph, as shown in Figure 1.4.

![](29f332a5430e03e9dc96f00b0038f9a2f8ee09eabe83dd8f547d15f97e56bf40.jpg)
Figure 1.4: Forward difference.. Source: Commerzbank Research, Bloomberg

And if we wanted, we could rotate the whole situation once more and arrive at a spot FX rate difference. Though this is probably not the best way to view the issue, a shift to the [spot rate](../../../International%20Finance/The%20Foreign%20Exchange%20Market%20Annotations.md) would be just as valid to explain the market mismatch.

We have illustrated the situation using the 1-year rates, only because they involve the least amount of arithmetic. But one may exactly repeat this analysis for tenors from $3\mathrm{m}$ to 30y, and the same relationships will hold. So however we look at it, the [forward rate](../../../Clippings/Forward%20Points%20in%20Currency.md) calculation is broken, and not even in a transient way - the basis seems to have moved in and is here to stay!

# So, What Actually is a 'Cross-Currency Basis Swap'?

It's worth explaining exactly what this means, and also what is meant when folks refer simply to the basis'. A [cross-currency basis swap](../../../Contemporary%20Financial%20Intermediation%20Notes/Table%20of%20Contents.md) (often abbreviated to '[xccy basis](../../../Contemporary%20Financial%20Intermediation%20Notes/Table%20of%20Contents.md) swap') can formally be set out as in Figure 1.5. Here, we assume that an institution starts off with EUR funding, which it converts with a [basis swap](../../Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%2013/Basis%20Swaps.md) to USD funding. This could be a EUR-based issuer that has sold a EUR bond locally, and so already has EUR bond cashflows such as coupon and redemption, but would rather convert them to USD. Practically, most sub-1-year [hedging](../../Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%205/Key%20Rates%20O1s%20Durations%20and%20Hedging.md) is done using [currency forwards](../../../Financial%20Instruments/Lecture%20Notes-%20Financial%20Instruments/Teaching%20Note%201-%20Forward%20Rates%20Agreement/Forward%20Contracts%20on%20Exchange%20Rates.md) (a single exchange at the final date), whereas longer term [hedging](../../Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%205/Key%20Rates%20O1s%20Durations%20and%20Hedging.md) tends to be done using swaps (final exchange plus interim interest rate exchanges).

The central figure is the contract known as the [cross-currency basis swap](../../../Contemporary%20Financial%20Intermediation%20Notes/Table%20of%20Contents.md), where. there are initial and final exchanges of capital (both at the [spot exchange rate](../../../Financial%20Instruments/Review%20Session%20Notes/Arbitrage%20Opportunity%20Accounting.md) at the. start of the deal) and interim floating rate interest rate exchanges. At the start of. the deal, both [currency](../../../Financial%20Instruments/Lecture%20Notes-%20Financial%20Instruments/Teaching%20Note%201-%20Forward%20Rates%20Agreement/Forwards%20and%20Futures%20Notes.md) legs will have the same value, but of course as FX rates vary, the value of the deal can change. Variations in [interest rates](../../Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%202/Interest%20Rate%20Quotations.md) will have only a small effect as the interest rate cashflows are all floating; the 'next' coupon is the only one which is known and fixed..

The quantity often somewhat confusingly referred to as the basis' is an adjustment to the central [basis swap](../../Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%2013/Basis%20Swaps.md) agreement. The basis is the result of supply and demand for USD cashflows. Strong demand for USD cashflows means that the [EURIBOR](../../Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%2012/EURIBOR%20Forward%20Rate%20Agreements%20and%20Futures.md) interest rate available for the deal is not the one which will make the PV of the EUR and the UsD legs equal; it is a little less, and this difference is the basis. It is exactly what we calculated in equation (2). The reader can already see that a basis which can be larger than $1\%$ will be highly significant to issuers and investors.

# Conversion Factor

Before we go on to discuss the various drivers of the [cross-currency basis](../Chapter%203/Calculating%20Novel%20Cross-Currency%20Bases%20a.md), it is worth introducing one more effect that is often neglected. When we discuss the motivations of issuers and investors, the cost of issuance is strongly influenced by one

![](0ffca411d5c491dbe219edee6d5e8260c981ff7431de61de0a9a2cf6061d937b.jpg)
Figure 1.5: [Cross-currency basis swap](../../../Contemporary%20Financial%20Intermediation%20Notes/Table%20of%20Contents.md). Source: Commerzbank Research

additional item: the conversion factor. The conversion factor is the number of basis points per annum in one [currency](../../../Financial%20Instruments/Lecture%20Notes-%20Financial%20Instruments/Teaching%20Note%201-%20Forward%20Rates%20Agreement/Forwards%20and%20Futures%20Notes.md) that equates to 1 basis point per annum in another.
[currency](../../../Financial%20Instruments/Lecture%20Notes-%20Financial%20Instruments/Teaching%20Note%201-%20Forward%20Rates%20Agreement/Forwards%20and%20Futures%20Notes.md) - thus it varies with the tenor and structure of the [interest rate curves](../../Financial%20Asset%20Pricing%20Theory%20Overview/Chapter%2010%20-%20The%20Economics%20of%20the%20Term%20Structure%20of%20Interest%20Rates/__temp__Chapter%2010%20-%20The%20Economics%20of%20the%20Term%20Structure%20of%20Interest%20Rates.md) of the.
two currencies. It is important to remember that it does not depend upon the FX rate,.
where 1 basis point in one [currency](../../../Financial%20Instruments/Lecture%20Notes-%20Financial%20Instruments/Teaching%20Note%201-%20Forward%20Rates%20Agreement/Forwards%20and%20Futures%20Notes.md) is 1 basis point in the other, at all times..

Another way of thinking about the conversion factor is that it comes from differ-. ent convexities, or yield curve shapes, in the two currencies and is thus dependent both on [interest rate curves](../../Financial%20Asset%20Pricing%20Theory%20Overview/Chapter%2010%20-%20The%20Economics%20of%20the%20Term%20Structure%20of%20Interest%20Rates/__temp__Chapter%2010%20-%20The%20Economics%20of%20the%20Term%20Structure%20of%20Interest%20Rates.md) and spread levels.

Where [interest rate differentials](.md) are small, the conversion factor will make only a small difference to the rates - typically just 1 or 2 basis points - but where the differentials are large, the difference may be quite significant.

To convert from basis points in a non-EUR [currency](../../../Financial%20Instruments/Lecture%20Notes-%20Financial%20Instruments/Teaching%20Note%201-%20Forward%20Rates%20Agreement/Forwards%20and%20Futures%20Notes.md) into basis points in EUR:

If the non-EUR rates $<$ EUR rates, then EUR conversion factor $>1$ If the non-EUR rates $>$ EUR rates, then EUR conversion factor $<1$

Or vs the USD,

If the non-USD rates $<$ USD rates, then USD conversion factor $>1$ If the non-USD rates $>$ USD rates, then USD conversion factor $<1$

The conversion factor of a particular tenor is given by the ratio of the sum of the discount factors up to that point of the different currencies - so for the 10-year point, it is the sum of all the EUR discount factors divided by the sum of all the USD discount factors. This tells us that the 1Oy EUR-to-USD conversion factor was 1.091 basis points on 20 February 2017, as in Table 1.1. Hence, a [credit spread](../../Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%2014/Cds-Equivalent%20Bond%20Spread.md) of 400bp over the EUR IRS [swap curve](../../../Financial%20Engineering/Fixed%20Income%20Derivatives/Determining%20the%20Expression%20for%20the%20Fair%20Value%20of%20the%20Swap%20Spread.md) translates into $400\times1.091=436\mathrm{bp}$ in USD. In order to. swap the EUR instrument into USD, you would need to further add the EUR/USD [currency](../../../Financial%20Instruments/Lecture%20Notes-%20Financial%20Instruments/Teaching%20Note%201-%20Forward%20Rates%20Agreement/Forwards%20and%20Futures%20Notes.md) swap costs as well as the EUR [basis swap](../../Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%2013/Basis%20Swaps.md) cost of 39.5 bp (as of 20 February 2017). Finally, you might have to consider the Libor frequency of the EUR and USD legs. If the EUR leg is $6\mathrm{m}$ , as is market standard, and the USD leg is $3\mathrm{m}$ , as is also often the case, then the. $3/6$ EUR swap costs will also need to be added. If the two legs are the same, then this cost is zero.

Table 1.1: Example of conversion factor calculation as of 20 February 2017.


<html><body><table><tr><td colspan="10">Interestratesasof20Feb2017</td></tr><tr><td>Tenor 1y</td><td>2y</td><td>3y</td><td>4y</td><td>5y</td><td>6y</td><td>7y</td><td>8y</td><td>9y</td><td>10y</td></tr><tr><td>USD</td><td>1.30%</td><td>1.56% 1.75%</td><td>1.90%</td><td>2.01%</td><td>2.09%</td><td>2.18%</td><td>2.26%</td><td>2.32%</td><td>2.38%</td></tr><tr><td>EUR</td><td>-0.21% -0.15%</td><td>-0.07%</td><td>0.02%</td><td>0.13%</td><td>0.26%</td><td>0.38%</td><td>0.51%</td><td>0.64%</td><td>0.75%</td></tr><tr><td colspan="10">DiscountFactors</td></tr><tr><td>USD</td><td>0.991</td><td>0.976 0.959</td><td>0.940</td><td>0.920</td><td>0.900</td><td>0.879</td><td>0.859</td><td>0.838</td><td>0.818</td></tr><tr><td>EUR</td><td>1.004</td><td>1.007 1.008</td><td>1.008</td><td>1.005</td><td>0.999</td><td>0.990</td><td>0.978</td><td>0.964</td><td>0.948</td></tr><tr><td colspan="10">ConversionFactors</td></tr><tr><td></td><td>1.013 1.022</td><td>1.032</td><td>1.042</td><td>1.051</td><td>1.061</td><td>1.069</td><td>1.077</td><td>1.085</td><td>1.091</td></tr></table></body></html>

Source: Commerzbank Research

This example shows that the conversion factor element in cross-[currency swaps](../../../Financial%20Instruments/Financial%20Instruments%20PSET%20Solutions.md) made around $48\%$ (or 36bp) of the overall swap costs of 76.0bp if the [credit spread](../../Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%2014/Cds-Equivalent%20Bond%20Spread.md). of the instrument is 400bp in February 2017.

We note that an advantage for an issuer is a disadvantage for an investor, and. vice versa. Thus, investors looking to buy bonds can apply exactly the same analysis to find where they may get the best value..

For a detailed discussion of the conversion factor, see Chapter 5.

# Where does the Cross-Currency Basis Come from?

In brief, the basis arises because issuers prefer to match the [currency](../../../Financial%20Instruments/Lecture%20Notes-%20Financial%20Instruments/Teaching%20Note%201-%20Forward%20Rates%20Agreement/Forwards%20and%20Futures%20Notes.md) mix they have on the asset side with the [currency](../../../Financial%20Instruments/Lecture%20Notes-%20Financial%20Instruments/Teaching%20Note%201-%20Forward%20Rates%20Agreement/Forwards%20and%20Futures%20Notes.md) mix on the liability side, while investors prefer to hedge their FX risk. If an issuer cannot obtain sufficient foreign [currency](../../../Financial%20Instruments/Lecture%20Notes-%20Financial%20Instruments/Teaching%20Note%201-%20Forward%20Rates%20Agreement/Forwards%20and%20Futures%20Notes.md) funding (as during the 2008 [financial crisis](../../../Financial%20Markets%20and%20Institutions/III.%20Liquidity%20of%20Assets/Class%209-%20Bailouts%20and%20Bank%20Failures/Squam%20Lake%20Group%20Letter.md) when European banks had to fund lots of dollar assets but had lost access to the dollar funding market), they can create synthetic foreign funding via domestic funding in combination with [FX forwards](../../../Financial%20Instruments/Financial%20Instruments%20PSET%20Solutions.md) (in the [FX market](../../../International%20Finance/Foreign%20Exchange%20Markets%20and%20Exchange%20Rate%20Determination.md)) or basis swaps (which belong more to the rates market). This can create a mismatch in the supply/demand for foreign funding and the [hedging](../../Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%205/Key%20Rates%20O1s%20Durations%20and%20Hedging.md) instruments. As long as the access to foreign funding remains distorted between domestic and foreign issuers and market participants lack balance sheets or credit lines to [arbitrage](../../Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%207/Arbitrage%20Pricing%20of%20Derivatives.md) away the distortion, there will be pressure for the basis to exist. In general, this [hedging](../../Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%205/Key%20Rates%20O1s%20Durations%20and%20Hedging.md) need translates to demand for certain currencies, often the UsD. For a good explanation of these causes and effects, see Borio et al. (2016).

In Figure 1.6 is a rough illustration of the different potential sources of the basis.. It centres on issuance of debt in different countries and currencies. Note that the top. boxes and the bottom boxes balance' each other - if the top boxes dominate, the basis becomes more negative; if the bottom box effects grow, the basis becomes less. negative.

Some explanation of these terms is useful.

USD (EUR) payer swap: the owner of a [cross-currency basis swap](../../../Contemporary%20Financial%20Intermediation%20Notes/Table%20of%20Contents.md), which changes their net position from paying USD (EUR) floating rates to paying EUR (USD) floating rates.
[Credit spread](../../Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%2014/Cds-Equivalent%20Bond%20Spread.md): the difference between rates which a company pays on its own curve (in USD, respectively EUR) and the IRS curve for the same [currency](../../../Financial%20Instruments/Lecture%20Notes-%20Financial%20Instruments/Teaching%20Note%201-%20Forward%20Rates%20Agreement/Forwards%20and%20Futures%20Notes.md). When. we hear that 'credit spreads are tight' it means that demand for [corporate debt](../../Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%2014/Corporate%20Bonds%20and%20Loans.md) in that [currency](../../../Financial%20Instruments/Lecture%20Notes-%20Financial%20Instruments/Teaching%20Note%201-%20Forward%20Rates%20Agreement/Forwards%20and%20Futures%20Notes.md) is high, so the cost of debt is relatively low..
Negative basis: the difference between the actual interest rate for a [currency](../../../Financial%20Instruments/Lecture%20Notes-%20Financial%20Instruments/Teaching%20Note%201-%20Forward%20Rates%20Agreement/Forwards%20and%20Futures%20Notes.md) and the theoretical interest rate calculated using the [FX forward rate](../../../Financial%20Instruments/Lecture%20Notes-%20Financial%20Instruments/Teaching%20Note%201-%20Forward%20Rates%20Agreement/Foreign%20Exchange%20Quoting%20Conventions.md), [FX spot rate](../../../Financial%20Instruments/Lecture%20Notes-%20Financial%20Instruments/Teaching%20Note%201-%20Forward%20Rates%20Agreement/Foreign%20Exchange%20Quoting%20Conventions.md) and (usually) the UsD interest rate. When the actual rate is less than the theoretical rate, the basis is negative.

![](6a9cd321bc22b8b8d4c975c7e0b627bfa33fca72dac1f006e396ecbf9cb784e5.jpg)
Figure 1.6: Potential sources of the [xccy basis](../../../Contemporary%20Financial%20Intermediation%20Notes/Table%20of%20Contents.md). Source: Commerzbank

Let's think of a situation in which an issuer finds themselves when they need to. issue debt. They want to do it in the most economical way. For a UsD issuer, the 'ground zero' or best possible level could be considered to be the IRS curve in USD (although some highly rated entities like GE can even trade inside the [swap rate](../../../Fixed%20Income%20Asset%20Pricing/Fixed%20Income%20Lecture%20Notes/Teaching%20Note%204%20Interest%20Rate%20Derivatives.md) at the short end). The cost above that level is the [credit spread](../../Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%2014/Cds-Equivalent%20Bond%20Spread.md) due to their own issuer quality, or $\mathrm{USD}_{\mathrm{spread}}$ . Similarly, the cost of issuance to a Euro-area issuer is EURspread.

The cost of issuing in another [currency](../../../Financial%20Instruments/Lecture%20Notes-%20Financial%20Instruments/Teaching%20Note%201-%20Forward%20Rates%20Agreement/Forwards%20and%20Futures%20Notes.md), and then [hedging](../../Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%205/Key%20Rates%20O1s%20Durations%20and%20Hedging.md) the FX risk of the issue, will depend on the [credit spread](../../Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%2014/Cds-Equivalent%20Bond%20Spread.md) in the other country for companies of similar quality, the [cross-currency basis](../Chapter%203/Calculating%20Novel%20Cross-Currency%20Bases%20a.md), and the conversion factor.

So, now we have the full rationale, which companies must bear in mind when making their issuance choice:.

For the USD entity, they will issue in EUR (and buy USD payer [xccy basis](../../../Contemporary%20Financial%20Intermediation%20Notes/Table%20of%20Contents.md) swaps) if
$$
\mathbf{USD_{spread}}>E\mathbf{U}\mathbf{R_{spread}}\star\mathbf{ConversionFactor}+\mathbf{xccybasis}
$$

This is the case for entities like SSSAs where the ECB PSPP is active.

For the EUR entity, they will issue in USD (and buy EUR payer [xccy basis](../../../Contemporary%20Financial%20Intermediation%20Notes/Table%20of%20Contents.md) swaps) if
$$
\mathrm{EUR}_{\mathrm{spread}}>\mathrm{USD}_{\mathrm{spread}}\star\mathrm{ConversionFactor+xccybasis}
$$

This would most frequently be the case for higher-spread products (AT1 and T2, high-yield issuers) where the ECB is not active, and where for longer tenors the [conversion factors](../../Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%2011/Mechanics%20of%20Us%20Treasury%20Note%20and%20Bond%20Futures.md) are very favourable.

As an example, consider a US firm on 20 February 2017 whose bonds have a 200bp [credit spread](../../Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%2014/Cds-Equivalent%20Bond%20Spread.md) over the US [swap rate](../../../Fixed%20Income%20Asset%20Pricing/Fixed%20Income%20Lecture%20Notes/Teaching%20Note%204%20Interest%20Rate%20Derivatives.md). The subsidiary of the firm in Europe can issue bonds which have 1o0bp [credit spread](../../Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%2014/Cds-Equivalent%20Bond%20Spread.md) over the EUR [swap rate](../../../Fixed%20Income%20Asset%20Pricing/Fixed%20Income%20Lecture%20Notes/Teaching%20Note%204%20Interest%20Rate%20Derivatives.md). The basis is 39.5bp, and the conversion factor is 1.091.
$$
\begin{array}{r l}&{\mathbf{USD}_{\mathrm{spread}}=20\mathbf{0}\mathbf{b}\mathbf{p}}\ &{\mathbf{EUR}_{\mathrm{spread}}=100\mathbf{b}\mathbf{p}^{*}1.091+39.5\mathbf{b}\mathbf{p}}\ &{\phantom{\mathrm{=}}=\mathbf{148.6bp}=148.6\mathbf{b}\mathbf{p}}\end{array}
$$

# Thus, they'll be about 5obp better off if they issue in Europe.

The effect of this long-term behaviour is to skew the effective UsD interest rate.
higher. However, this skew will differ from one [currency](../../../Financial%20Instruments/Lecture%20Notes-%20Financial%20Instruments/Teaching%20Note%201-%20Forward%20Rates%20Agreement/Forwards%20and%20Futures%20Notes.md) pair to the next as credit.
spread and other effects persist to different extents in different markets - thus the market 'expression' of this USD demand as a spread to the non-UsD interest rate.
Another way of putting it is that counterparties impose increasingly large spreads.
on the trade, which only ever seems to go one way!.

Euro-area supras and agencies are the prominent counterexample, as they. actively cover their EUR funding needs in the USD market and hence take advantage of the basis.

Another significant reason is [currency](../../../Financial%20Instruments/Lecture%20Notes-%20Financial%20Instruments/Teaching%20Note%201-%20Forward%20Rates%20Agreement/Forwards%20and%20Futures%20Notes.md) mismatches on the balance sheets of large [financial institutions](../../../Financial%20Markets%20and%20Institutions/Financial%20Markets%20and%20Institutions%20Lecture%20Notes.md). As yields change, balance sheets may be structurally biased towards or against specific currencies. FX [derivatives](../../Financial%20Trading%20and%20Markets/Chapter%209%20Arbitrage%20and%20Hedging%20With%20Options.md) like swaps will have to be used to cover any [currency](../../../Financial%20Instruments/Lecture%20Notes-%20Financial%20Instruments/Teaching%20Note%201-%20Forward%20Rates%20Agreement/Forwards%20and%20Futures%20Notes.md) gaps between assets and liabilities, which will place pressure on equation (1) again. So here again, imbalances in the supply and demand for [currency](../../../Financial%20Instruments/Lecture%20Notes-%20Financial%20Instruments/Teaching%20Note%201-%20Forward%20Rates%20Agreement/Forwards%20and%20Futures%20Notes.md) [hedging](../../Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%205/Key%20Rates%20O1s%20Durations%20and%20Hedging.md) result in a non-zero basis, as these institutions are usually fully FX-hedged.

Additionally, strategic [hedging](../../Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%205/Key%20Rates%20O1s%20Durations%20and%20Hedging.md) on the part of investors with foreign [currency](../../../Financial%20Instruments/Lecture%20Notes-%20Financial%20Instruments/Teaching%20Note%201-%20Forward%20Rates%20Agreement/Forwards%20and%20Futures%20Notes.md) holdings can also apply pressure to widen (that is, make more negative) the basis. Once more, the hunt for yield sends the market into foreign territory. But [portfolio](../../../Advanced%20Investments/An%20Asset%20Allocation%20Primer.md) allocation ratios, once established and prevalent, move slowly, and thus another persistent [currency](../../../Financial%20Instruments/Lecture%20Notes-%20Financial%20Instruments/Teaching%20Note%201-%20Forward%20Rates%20Agreement/Forwards%20and%20Futures%20Notes.md) hedge position can exist.

The desirability of a [currency](../../../Financial%20Instruments/Lecture%20Notes-%20Financial%20Instruments/Teaching%20Note%201-%20Forward%20Rates%20Agreement/Forwards%20and%20Futures%20Notes.md) is closely connected with yield, and one good in-. dicator of this is the FX [carry trade](../../../Clippings/Currency%20Carry%20Trade.md). The G10 FX [carry trade](../../../Clippings/Currency%20Carry%20Trade.md) is the result of allocating funds to higher-yielding currencies by borrowing in the lower-yielding currencies. In Figure 1.7 we can see that this trade correlates closely with the EURUsD [basis swap](../../Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%2013/Basis%20Swaps.md), showing that the basis is strongly influenced by yield - and thus ultimately central bank policies. However, as can be seen in the chart, during stress periods such as 2008 and $2011/12$ , the basis is highly volatile and can significantly decouple. from the carry/yield proxies.

5y EURUsD [basis swap](../../Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%2013/Basis%20Swaps.md) (bp, rhs) with G10 FX carry (index, Ihs)

![](226ab43975035e37904561783f0ac1f176bfd136bf2e1dfa4f27d30008deff79.jpg)
Figure 1.7: [Cross-currency basis swap](../../../Contemporary%20Financial%20Intermediation%20Notes/Table%20of%20Contents.md) with FX carry.. Source: Bloomberg, Commerzbank Research

# What Keeps the Basis Swap from Being Arbitraged Away?

We can see why there might be one-way pressure on the [forward rate](../../../Clippings/Forward%20Points%20in%20Currency.md) or Libor rates, but traditionally, an equal and opposite pressure would be provided by [arbitrage](../../Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%207/Arbitrage%20Pricing%20of%20Derivatives.md) activity which would bring rates back in line with equation (1). Perhaps the important question is not Why does the [basis swap](../../Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%2013/Basis%20Swaps.md) exist?' because we know that pressures and temporary dislocations often occur in [financial markets](../../../Financial%20Markets%20and%20Institutions/Financial%20Markets%20and%20Institutions%20Lecture%20Notes.md). The true question is, 'Why does it stay?'

There are quite a few reasons as to why it persists, and they all have to do with. the more stringent regulatory regime governing the markets since the crisis, which ultimately prevents markets from balancing supply and demand for FX hedges. We. list the more significant ones in the following section..

# Capital Cost of FX Derivatives

The regulatory burden of holding different deal types on books has changed. [Derivatives](../../Financial%20Trading%20and%20Markets/Chapter%209%20Arbitrage%20and%20Hedging%20With%20Options.md) like cross-[currency swaps](../../../Financial%20Instruments/Financial%20Instruments%20PSET%20Solutions.md), which are used to [arbitrage](../../Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%207/Arbitrage%20Pricing%20of%20Derivatives.md) the [currency](../../../Financial%20Instruments/Lecture%20Notes-%20Financial%20Instruments/Teaching%20Note%201-%20Forward%20Rates%20Agreement/Forwards%20and%20Futures%20Notes.md) imbalances described in the previous section, all involve capital flows - often substantial - at the end date. These will require large amounts of risk capital to be held against them. Thus, there will be a limit to how many may be done, and there may be a cost to doing them, as the risk capital used to protect them will be in safe, low-yielding in. struments. Arbitraging will thus entail a cost and will have a limited extent for most institutions.

# Counterparty Risks and Credit Limits

[Arbitrage](../../Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%207/Arbitrage%20Pricing%20of%20Derivatives.md) activities require counterparties and the [credit quality](../../../Financial%20Markets%20and%20Institutions/II.%20The%20Roles%20of%20Banks%20and%20Derivative%20Markets%20in%20Resolving%20Problems%20Inherent%20in%20Debt%20Contracts/Class%202-%20Debt%20Contracts%20due%20to%20Lack%20of%20Information/Wellman%20Inc%20the%20Importance%20of%20Loan%20Covenants.md) of the counterparties limits the exposure that one institution can have to others. Thus, large-[leverage](../../../Advanced%20Investments/Lecture%206-Leverage,%20Tail%20Risk,%20Volatility%20Products.md) and. high-risk deals can only occur with a limited set of counterparties and to a limited degree. In that regard, the varying cost and availability of repo funding across juris-. dictions limit the extent to which leveraged investors can [arbitrage](../../Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%207/Arbitrage%20Pricing%20of%20Derivatives.md) the basis away..

# Clearing

Cross-[currency swaps](../../../Financial%20Instruments/Financial%20Instruments%20PSET%20Solutions.md) are not eligible for clearing with many of the world's larger exchanges. Non-cleared [derivatives](../../Financial%20Trading%20and%20Markets/Chapter%209%20Arbitrage%20and%20Hedging%20With%20Options.md) tend to attract a higher cost of funding, and the [introduction](../../../Financial%20Markets%20and%20Institutions/III.%20Liquidity%20of%20Assets/Class%209-%20Bailouts%20and%20Bank%20Failures/Squam%20Lake%20Group%20Introduction.md) of bilateral variation margining for uncleared trades makes it difficult to execute trades, as numerous legal CSA amendments have not yet been signed. Though there are currently some exceptions made for the [currency](../../../Financial%20Instruments/Lecture%20Notes-%20Financial%20Instruments/Teaching%20Note%201-%20Forward%20Rates%20Agreement/Forwards%20and%20Futures%20Notes.md) market, generally the delays to implement clearing for these deal types impose yet another limit on their number and extent.

# Horses for Courses

Of course, there are a few institutions that can do the [arbitrage](../../Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%207/Arbitrage%20Pricing%20of%20Derivatives.md) to a degree. But that. degree will vary. For a highly rated cash rich organisation, which could issue bonds in USD and take advantage of the basis to do a swap to the end date to deliver value. in a different [currency](../../../Financial%20Instruments/Lecture%20Notes-%20Financial%20Instruments/Teaching%20Note%201-%20Forward%20Rates%20Agreement/Forwards%20and%20Futures%20Notes.md), the cost of placing bonds is important. For a large hedge fund, the price and availability of funding to provide the large [arbitrage](../../Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%207/Arbitrage%20Pricing%20of%20Derivatives.md) cashflows will be paramount.

For a useful discussion of the causes of the basis, see Du, Tepper and Verdelhan (2016), which also argues that the dominant reason for its persistence are regulation-driven balance sheet costs.

# How Could an Institution Make Money from the Cross-Currency Basis Swap?

This is the burning question! There is no definitive answer, as different institutions will have very different situations, needs and relative advantages. But the graph in Figure 1.9 suggests that at least for some folks, for some of the time, there is money to be made.

We have calculated a yield pickup' for 1y government bonds. We assume that. the investor is based in Germany and can hold (and short via repo if necessary) bonds in Germany, the USA, Japan, the UK and Australia, with a similar rating or perceived [credit risk](../../../Course%20Notes/Quantitative%20Trading%20Strategies%20Lecture%20Notes.md). The yield pickup is the bond interest rate differential hedged for the 1y pe-. riod via the [cross-currency swap](../../../Clippings/Currency%20Swap%20Basics.md) market, including the basis. Thus the pickup is given by
$$
\Delta_{\mathbf{bond}}-\Delta_{\mathbf{swap}}+\mathbf{basis}
$$

where $\Delta_{\mathrm{bond}}$ and $\Delta_{\mathrm{swap}}$ are the 1y yield differentials for the relevant instruments in each [currency](../../../Financial%20Instruments/Lecture%20Notes-%20Financial%20Instruments/Teaching%20Note%201-%20Forward%20Rates%20Agreement/Forwards%20and%20Futures%20Notes.md). Writing it in this way clearly illustrates where the dislocations arise. If the spread of bond yield to swap was the same in both currencies, the first two terms would cancel out. If then the basis were zero, there would be no pickup at all. So it is due to differential market views on credit and to the basis. Figures 1.8 and 1.9 are the time series of this yield pickup since the end of 2o08 for the different currencies. The second graph focuses on the EURUSD case, showing $\Delta_{\mathrm{bond}}$ and $\Delta_{\mathrm{swap}}$ and the basis separately.

We see that the time series contain different correlation 'zones'. The start of the.. series in sees both JPY and USD with a negative basis from the EUR investor's point of view; in 2oo8, clearly both were seen as safe havens from the crisis storm. In 2011, however, the JPY correlates more strongly with AUD than USD, and only the USD is seen as the true safe haven in the first of the Greek debt crises. More recently, both USD and JPY maintain a negative basis, but short-range movement of the JPY basis can correlate with more risky currencies. Finally, we see that all four [currency](../../../Financial%20Instruments/Lecture%20Notes-%20Financial%20Instruments/Teaching%20Note%201-%20Forward%20Rates%20Agreement/Forwards%20and%20Futures%20Notes.md) bases are going lower vs the EUR, quite possibly indicating a general nervousness about the Euro area in a time of multiple elections, where political surprises and reversals are becoming the norm.

Pickup for a EUR based investor, using 1y foreign govt bonds, in %

![](6adcdd71717f87f5519b6057a311b3d0ea443734eed0c91243a532404ef0b284.jpg)
Figure 1.8: Yield pickup, with potential [arbitrage](../../Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%207/Arbitrage%20Pricing%20of%20Derivatives.md) opportunity levels. Source: Commerzbank, Bloomberge

Swap-bond differences for 1y EUR and UsD govies. The addition of the basis makes a significant difference.

![](2b5c3dddc10848d3167099ec67acad0ac7246d0d4d5b3882fff1576a72f6f0c8.jpg)
Figure 1.9: EURUSD yield pickup components $(\%)$ Source: Bloomberg, Commerzbank Research

Is this pickup really available in the market? Not entirely - this assumes no repo. costs and ignores credit issues and the cost of capital. But nevertheless, it is rarely lower than 30bp for any [currency](../../../Financial%20Instruments/Lecture%20Notes-%20Financial%20Instruments/Teaching%20Note%201-%20Forward%20Rates%20Agreement/Forwards%20and%20Futures%20Notes.md) and is often greater than 50bp. For different institu-. tions, there could be opportunities at some level..

# Appendix 1.A: The FX carry trade

A Historical View - UIP and CIP

# UIP -- The First to Fall

The first way in which the [FX market](../../../International%20Finance/Foreign%20Exchange%20Markets%20and%20Exchange%20Rate%20Determination.md) declined to obey market expectation was Uncovered [Interest Rate Parity](../../../Financial%20Instruments/Lecture%20Notes-%20Financial%20Instruments/Teaching%20Note%201-%20Forward%20Rates%20Agreement/Foreign%20Exchange%20Quoting%20Conventions.md) (UIP). In the early days of the floating FX rate regime, it was assumed that spot rates would, on average, follow the path laid out by the forward rates. The [forward rate](../../../Clippings/Forward%20Points%20in%20Currency.md) path predicts (from equation (1)) that the higher nominal interest-bearing [currency](../../../Financial%20Instruments/Lecture%20Notes-%20Financial%20Instruments/Teaching%20Note%201-%20Forward%20Rates%20Agreement/Forwards%20and%20Futures%20Notes.md) will depreciate relative to the lower interest-bearing [currency](../../../Financial%20Instruments/Lecture%20Notes-%20Financial%20Instruments/Teaching%20Note%201-%20Forward%20Rates%20Agreement/Forwards%20and%20Futures%20Notes.md). This does not on the face of it seem unreasonable - investors in higheryielding (higher [inflation](../../../International%20Finance/Bridgewater/Principles%20For%20Navigating%20Big%20Debt%20Cycles/Part%20II%20Detailed%20Case%20Studies/German%20Debt%20Crisis%20andHyperinflation%20(1918–1924)/War%20Economies%20and%20Hyperinflation.md)) currencies are compensated for the [currency](../../../Financial%20Instruments/Lecture%20Notes-%20Financial%20Instruments/Teaching%20Note%201-%20Forward%20Rates%20Agreement/Forwards%20and%20Futures%20Notes.md) weakening. by higher interest rate income. Put differently, higher [interest rates](../../Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%202/Interest%20Rate%20Quotations.md) exist due to higher levels of risk (regarding [inflation](../../../International%20Finance/Bridgewater/Principles%20For%20Navigating%20Big%20Debt%20Cycles/Part%20II%20Detailed%20Case%20Studies/German%20Debt%20Crisis%20andHyperinflation%20(1918–1924)/War%20Economies%20and%20Hyperinflation.md) and [central bank expectations](../Chapter%208/Forward%20Curves%20Duration%20and%20Convexity.md), for example), thus, it is plausible to assume that more risky currencies will depreciate relative to less risky ones. Uncovered [Interest Rate Parity](../../../Financial%20Instruments/Lecture%20Notes-%20Financial%20Instruments/Teaching%20Note%201-%20Forward%20Rates%20Agreement/Foreign%20Exchange%20Quoting%20Conventions.md) is said to hold if currencies follow, on average, the [forward rate](../../../Clippings/Forward%20Points%20in%20Currency.md) path..

It is useful for market participants, risk managers and quants if UIP does hold. This means that the [arbitrage pricing](../../Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%207/Risk-Neutral%20Pricing.md) is correct on average and does not allow for systematic [trading strategies](../../../Course%20Notes/Quantitative%20Trading%20Strategies%20Lecture%20Notes.md) to deliver profit, and it means that the middle office [risk management](../../../Financial%20Engineering/Financial%20Mathematics%20Course.md) of long-term positions within [financial institutions](../../../Financial%20Markets%20and%20Institutions/Financial%20Markets%20and%20Institutions%20Lecture%20Notes.md) can use the same valuation models as the front office traders.

But this does not hold. The devaluation of currencies implied by their interest. rate regimes does not, on average, occur. As the evidence mounted that UIP is violated - this was first pointed out in 1984 (see Fama [1984]) - and that forward rates have no predictive power over the path of spot rates, the market and various aca-. demic institutions reluctantly had to admit that this particular assumption was in-. valid. We summarise the evidence in Figure 1.10, which was taken from James,. Fullwood and Billington (2015) and has since been updated..

This is the result of pursuing a systematic rules-based, quarterly carry-trading. strategy in all liquid G10 [currency](../../../Financial%20Instruments/Lecture%20Notes-%20Financial%20Instruments/Teaching%20Note%201-%20Forward%20Rates%20Agreement/Forwards%20and%20Futures%20Notes.md) crosses (heavy black line). A [carry trade](../../../Clippings/Currency%20Carry%20Trade.md) is where the trader takes a position against the [forward rate](../../../Clippings/Forward%20Points%20in%20Currency.md) (same as doing a [short forward](../../../Financial%20Instruments/Lecture%20Notes-%20Financial%20Instruments/Teaching%20Note%203%20Swaps-%20Financial%20Instruments/Forward%20Rates%20Agreement.md) trade), borrowing in the lower-yielding [currency](../../../Financial%20Instruments/Lecture%20Notes-%20Financial%20Instruments/Teaching%20Note%201-%20Forward%20Rates%20Agreement/Forwards%20and%20Futures%20Notes.md) to lend in the higher-yielding one. If the [spot rate](../../../International%20Finance/The%20Foreign%20Exchange%20Market%20Annotations.md) does move to the [forward rate](../../../Clippings/Forward%20Points%20in%20Currency.md), then the trader will make no profit. If the [spot rate](../../../International%20Finance/The%20Foreign%20Exchange%20Market%20Annotations.md) stays the same and does not move over the course of the deal, the. trader will make exactly the [forward interest rate](../../../Clippings/Forward%20Rate.md) differential (known as forward points) - this 'perfect [carry trade](../../../Clippings/Currency%20Carry%20Trade.md)' is represented by the fine grey dashed line. The. central heavy grey dashed line is the actual average path of the spot FX rates.

As can be clearly seen, the actual [carry trade](../../../Clippings/Currency%20Carry%20Trade.md) has almost identical results (with some noise) to the 'perfect' [carry trade](../../../Clippings/Currency%20Carry%20Trade.md). This is the same as saying that on average,.

Average [carry trade](../../../Clippings/Currency%20Carry%20Trade.md) [returns](../../Financial%20Asset%20Pricing%20Theory%20Overview/Chapter%203%20-%20%20Assets,%20Portfolios,%20and%20Arbitrage/Assets.md) from all G 10 crosses

![](0e60874ab6ca4f3a6e34c07b843120256a497e26d7ec824076d6a19054312637.jpg)
Figure 1.10: [Carry trade](../../../Clippings/Currency%20Carry%20Trade.md) [returns](../../Financial%20Asset%20Pricing%20Theory%20Overview/Chapter%203%20-%20%20Assets,%20Portfolios,%20and%20Arbitrage/Assets.md).

FX rates do not move toward the forward rates - they are more likely to be the same as the [spot rate](../../../International%20Finance/The%20Foreign%20Exchange%20Market%20Annotations.md) at the start of the deal..

So UIP bites the dust. What about CIP?

# CIP -- Surely Invulnerable?

[Covered Interest Rate Parity](../../../Financial%20Instruments/Financial%20Instruments%20PSET%20Solutions.md) (CIP) was thought to be a much harder nut to crack. [Covered Interest Rate Parity](../../../Financial%20Instruments/Financial%20Instruments%20PSET%20Solutions.md) is said to hold if equation (1) holds. However, as we have shown, the existence and persistence of the non-zero [cross-currency basis](../Chapter%203/Calculating%20Novel%20Cross-Currency%20Bases%20a.md) clearly shows that indeed, CIP has fallen as well.

# Appendix 1.B: The Cross-Currency Toolkit

# The Three Elements

There are different financial products available to allow investors and issuers to adjust their [currency](../../../Financial%20Instruments/Lecture%20Notes-%20Financial%20Instruments/Teaching%20Note%201-%20Forward%20Rates%20Agreement/Forwards%20and%20Futures%20Notes.md) exposures. The most liquid and widely used are:

- FX swaps - FX outrights (or forward outrights) - [Cross-currency basis](../Chapter%203/Calculating%20Novel%20Cross-Currency%20Bases%20a.md) swapse

Each serves different sections of the market and is useful in different ways. In the following section, we explain the mechanics of each and their major uses..

# FX Swap

Figure 1.11 is a schematic of the cashflows involved in an [FX swap](../../../Clippings/Currency%20Swap%20Basics.md) between parties A and B. We assume we have a [principal amount](../../../Financial%20Instruments/Financial%20Derivatives%20and%20Quantitative%20Methods/HSBC-Auto%20callable%20Barrier%20Notes%20with%20Step-up%20Premium.md). $P$ in EUR, and that the current. spot FX rate is S USD per EUR, with a [forward rate](../../../Clippings/Forward%20Points%20in%20Currency.md). $F$

![](d4f4790d30d6734472da8cba2861d95dcf9f87bdae45b7506a30af13ddda0dec.jpg)
Figure 1.11: [FX swap](../../../Clippings/Currency%20Swap%20Basics.md). Definition of [FX swap](../../../Clippings/Currency%20Swap%20Basics.md): Party A borrows [Currency](../../../Financial%20Instruments/Lecture%20Notes-%20Financial%20Instruments/Teaching%20Note%201-%20Forward%20Rates%20Agreement/Forwards%20and%20Futures%20Notes.md) 1 to lend [Currency](../../../Financial%20Instruments/Lecture%20Notes-%20Financial%20Instruments/Teaching%20Note%201-%20Forward%20Rates%20Agreement/Forwards%20and%20Futures%20Notes.md) 2

Usual Maturity: up to 1y

Uses: FX swaps are mostly a [liquidity](../../../Financial%20Markets%20and%20Institutions/III.%20Liquidity%20of%20Assets/Class%205-%20Private%20Information,%20Liquidity,%20and%20Securitization/Class%20Note%2010%20Liquidity%20and%20Class%20Note%2010%20Liquidity%20and%20Liquidity%20Managementliquidity%20management.md) and treasury management tool. Users are:
-Asset Managers: investors in overseas markets who don't want [currency](../../../Financial%20Instruments/Lecture%20Notes-%20Financial%20Instruments/Teaching%20Note%201-%20Forward%20Rates%20Agreement/Forwards%20and%20Futures%20Notes.md) risk.. Lenders of domestic [currency](../../../Financial%20Instruments/Lecture%20Notes-%20Financial%20Instruments/Teaching%20Note%201-%20Forward%20Rates%20Agreement/Forwards%20and%20Futures%20Notes.md) vs the foreign [currency](../../../Financial%20Instruments/Lecture%20Notes-%20Financial%20Instruments/Teaching%20Note%201-%20Forward%20Rates%20Agreement/Forwards%20and%20Futures%20Notes.md) they need to fund.
- Bank Treasurers: wish to lower their cost of funding and [liquidity](../../../Financial%20Markets%20and%20Institutions/III.%20Liquidity%20of%20Assets/Class%205-%20Private%20Information,%20Liquidity,%20and%20Securitization/Class%20Note%2010%20Liquidity%20and%20Class%20Note%2010%20Liquidity%20and%20Liquidity%20Managementliquidity%20management.md) in different currencies
Central Banks: manage their [liquidity](../../../Financial%20Markets%20and%20Institutions/III.%20Liquidity%20of%20Assets/Class%205-%20Private%20Information,%20Liquidity,%20and%20Securitization/Class%20Note%2010%20Liquidity%20and%20Class%20Note%2010%20Liquidity%20and%20Liquidity%20Managementliquidity%20management.md) profiles
- Corporate Treasurers: act like banks for their own short-term funding, and manage their treasury position in different currencies.

Note that the basis is embedded into the [forward rate](../../../Clippings/Forward%20Points%20in%20Currency.md), so though it is not explicit in the diagram, it is certainly included.

# FX Outright (Forward Outright)

In Figure 1.12, we show the cashflows involved in an FX Outright (often called Forward Outright) between parties A and B. We again assume we have a [principal amount](../../../Financial%20Instruments/Financial%20Derivatives%20and%20Quantitative%20Methods/HSBC-Auto%20callable%20Barrier%20Notes%20with%20Step-up%20Premium.md) $P$ in EUR, and that the current spot FX rate is S USD per EUR, with a forward. rate $F.$ Though simple in concept, in execution this tends to be done as a swap plus a [spot transaction](../../Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%203%20-%20Futures%20Markets/Fundamentals%20of%20Futures%20and%20Forwards.md).

![](28d0481bbe27d6912c8fcecceaa33d278bb91a368049383bce8db965f41fe8f6.jpg)
Figure 1.12: FX outright. Definition of [FX swap](../../../Clippings/Currency%20Swap%20Basics.md): Party A and Party B exchange [Currency](../../../Financial%20Instruments/Lecture%20Notes-%20Financial%20Instruments/Teaching%20Note%201-%20Forward%20Rates%20Agreement/Forwards%20and%20Futures%20Notes.md) 1 for [Currency](../../../Financial%20Instruments/Lecture%20Notes-%20Financial%20Instruments/Teaching%20Note%201-%20Forward%20Rates%20Agreement/Forwards%20and%20Futures%20Notes.md) 2 at a future date.

In fact, it is usually done as a spot trade plus a swap, as in Figure 1.13.

![](52c08bf6813c02b0a9c487db0d03b6cbbd194dfc7cf33800073e789f5d9ad69a.jpg)
Figure 1.13: Spot trade plus swap.

Usual Maturity: below 1y or 2y

Uses: This market tends to be extensively used by corporates and exporters, to cover trade and repatriation flows.

As before, the basis is embedded in the [forward rate](../../../Clippings/Forward%20Points%20in%20Currency.md).

# Cross-Currency Basis Swap

In Figure 1.14, we now include the interim interest payments included in a crosscurrency [basis swap](../../Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%2013/Basis%20Swaps.md).

![](425d866b31e6997d813ba42134135de18b9ffb0d9b3b11bf75b389f8ad6a9142.jpg)
Figure 1.14: [Cross-currency basis swap](../../../Contemporary%20Financial%20Intermediation%20Notes/Table%20of%20Contents.md).

Definition of FX [cross-currency basis swap](../../../Contemporary%20Financial%20Intermediation%20Notes/Table%20of%20Contents.md): where two parties borrow from, and simultaneously lend to, each other an equivalent amount of money denominated in two different currencies for a predefined period of time, including floating interim interest payments, usually 3m.

Usual Maturity: up to 30y in some cases, though up to 10y is more usual

Uses: Primarily used by debt issuers

- SSAs: natural multi-[currency](../../../Financial%20Instruments/Lecture%20Notes-%20Financial%20Instruments/Teaching%20Note%201-%20Forward%20Rates%20Agreement/Forwards%20and%20Futures%20Notes.md) users. Different locations will have different [currency](../../../Financial%20Instruments/Lecture%20Notes-%20Financial%20Instruments/Teaching%20Note%201-%20Forward%20Rates%20Agreement/Forwards%20and%20Futures%20Notes.md) mixes.

-Corporates: Some large corporates can act like SSAs. Others may use EUR or USD as funding currencies, swapping back to USD.

- Banks: Treasuries minimise cost of funding and [liquidity](../../../Financial%20Markets%20and%20Institutions/III.%20Liquidity%20of%20Assets/Class%205-%20Private%20Information,%20Liquidity,%20and%20Securitization/Class%20Note%2010%20Liquidity%20and%20Class%20Note%2010%20Liquidity%20and%20Liquidity%20Managementliquidity%20management.md). They vary according to location. Some derivative desks manage the [currency](../../../Financial%20Instruments/Lecture%20Notes-%20Financial%20Instruments/Teaching%20Note%201-%20Forward%20Rates%20Agreement/Forwards%20and%20Futures%20Notes.md) risk of different counterparties with [xccy swaps](../../Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%204%20-%20Swap%20Markets/Cross-Currency%20Swaps.md).

- Asset managers hardly ever use this market due to the high cost of capital and regulatory constraints. As they would be the natural arbitrageurs in this space, the non-zero basis can persist.

The basis is explicit in the EUR Libor flows.
---
tags:
  - carry_trade
  - forward_volatility
  - fva
  - implied_volatility
  - volatility_swap
aliases:
  - FVA
  - Forward Volatility Agreement
key_concepts:
  - forward implied volatility
  - future spot volatility
  - long short straddle
  - spot implied volatility
  - volatility swap contract
---

# Forward Volatility Agreement (FVA)
# 1.1   Forward Volatility Agreement (FVA)

The [forward implied volatility](.md) of an exchange rate [returns](../../Financial%20Markets/Financial%20Asset%20Pricing%20Theory%20Overview/Chapter%203%20-%20%20Assets,%20Portfolios,%20and%20Arbitrage/Assets.md) can be defined by forward volatility  agreement (FVA). The FVA is a [volatility swap contract](.md) between a buyer and seller to exchange  a straddle option at a specified date in the future and specified volatility level.

A long (short) straddle involves buying (selling) both a call and a put option on the same  underlying at the same [strike price](../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%205%20Options%20on%20Prices%20and%20Hedge-Based%20Valuation/Call%20and%20Put%20Payoffs%20at%20Expiry.md) and for the same [expiration date](../../Financial%20Instruments/Financial%20Derivatives%20and%20Quantitative%20Methods/Risk%20Neutral%20Pricing%20of%20Options.md).  Option players who have a  view on volatility usually take a position on straddle trades. A long straddle position is a bet that  the underlying will be more volatile over the term of the instrument then predicted by the market.

[Forward volatility agreement](.md) can also be defined as [forward contract](../../Clippings/Forward%20Points%20in%20Currency.md) on future spot implied  volatility, which for a one dollar [investment](../../Advanced%20Investments/An%20Asset%20Allocation%20Primer.md) delivers the difference between future spot implied  volatility and [forward implied volatility](.md).

In other words, the FVA is a [forward contract](../../Clippings/Forward%20Points%20in%20Currency.md) on a future [spot implied volatility](.md) with a payoff at  maturity equal to:
$$
\big(I V_{t+k}-F V_{t}^{k}\big)x M
$$

Where
$$
I V_{t+k}
$$

𝑘 𝐹𝑉 𝑡

𝑀

is the annualised [spot implied volatility](.md) observed at time   $_{t+k}$   and measured over  the interval   $t{+}k$   to   $_{t+2k}$

is the annualized [forward implied volatility](.md) determined at time   $t$    for the same  interval starting at time  $\mathbf{t}\!+\!\mathbf{k}$

is the notional dollar amount that converts the volatility difference into a dollar  payoff.

For example, setting   $k{=}I$   month  implies that   $I V_{t+k}$   is the observed spot implied  volatility at  $_{t+I}$   month for the interval   $t+.$  1month to   $t\!+\!2.$  months

The [implied volatility](../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%205%20Options%20on%20Prices%20and%20Hedge-Based%20Valuation/A%20Real-Life%20Option%20Pricing%20Exercise.md) is a measure of expected volatility, which is directly quoted  in traded [currency](../../Financial%20Instruments/Lecture%20Notes-%20Financial%20Instruments/Teaching%20Note%201-%20Forward%20Rates%20Agreement/Forwards%20and%20Futures%20Notes.md) options.

“Spot” [implied volatility](../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%205%20Options%20on%20Prices%20and%20Hedge-Based%20Valuation/A%20Real-Life%20Option%20Pricing%20Exercise.md) is the [implied volatility](../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%205%20Options%20on%20Prices%20and%20Hedge-Based%20Valuation/A%20Real-Life%20Option%20Pricing%20Exercise.md) for an interval starting today and  ending in the future (e.g., starting today and ending one month from now).

“Forward” [implied volatility](../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%205%20Options%20on%20Prices%20and%20Hedge-Based%20Valuation/A%20Real-Life%20Option%20Pricing%20Exercise.md) is the [implied volatility](../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%205%20Options%20on%20Prices%20and%20Hedge-Based%20Valuation/A%20Real-Life%20Option%20Pricing%20Exercise.md) determined today for an  interval starting in the future and ending further in the future (e.g., starting in one  month and ending in two months from now).
The key motivation for trading FVA’s is that it allows investors to speculate on the level of future  volatility. Similar to the standard [carry trade](../../Clippings/Currency%20Carry%20Trade.md), volatility [carry trade](../../Clippings/Currency%20Carry%20Trade.md) is a speculation strategy that  buys and sells FVAs, where investors try to make money by guessing the level of future spot  [implied volatility](../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%205%20Options%20on%20Prices%20and%20Hedge-Based%20Valuation/A%20Real-Life%20Option%20Pricing%20Exercise.md). The [carry trade](../../Clippings/Currency%20Carry%20Trade.md) in volatility works well if [spot implied volatility](.md) is  unpredictable. Then, investors engaging in this new [carry trade](../../Clippings/Currency%20Carry%20Trade.md) will on average earn the difference  between spot and forward volatility without having to worry about movements in exchange rates.

 ![500](Attachments/500-424.jpg)
Figure 1.1, Source:

Given the data on the current implied vol at ili ties for alternative maturities, the calculation of  [forward implied volatility](.md) can be computed (proxy) by a simple formula, which assumes that the  relation between implied variance and time is linear across the [term structure](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%209/The%20Vasicek%20Model.md).

Define   $\sigma_{t_{1T_{1}}}$   and    $\sigma_{t_{2T_{2}}}$   as annualized at-the-money (ATMF) implied vol at ili ties for the interval t  to   $T_{1}$   and   $\mathbf{t}$   to    $T_{2}$  . Respectively, corresponding to year fraction   $D_{t_{1T_{1}}}$   and   $D_{t_{2T_{2}}}$   . The forward  [implied volatility](../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%205%20Options%20on%20Prices%20and%20Hedge-Based%20Valuation/A%20Real-Life%20Option%20Pricing%20Exercise.md) between the two dates   $(\sigma_{T_{1T_{2}}})$    is determined as follows:
$$
\begin{array}{r}{\sigma_{T_{1T_{2}}}=\sqrt{\frac{\sigma2_{t_{2T_{2}}}{D_{t_{2T_{2}}}}-\sigma2_{t_{1T_{1}}}{D_{t_{1T_{1}}}}}{{D_{t_{1T_{1}}}}{D_{t_{2T_{2}}}}}}}\end{array}
$$
$\sigma_{T_{1}T_{2}}$    is the market-determined [forward implied volatility](.md), which is known at time   $t$   and  corresponds to the interval between   $T_{I}$   and   $T_{2}$

It is therefore possible to infer the “local” volatility between two points   $T_{I}$   and   $T_{2}$      given spot  volatility curve.

For example, if current 3-month and 6-month volatility are trading at   $10\%$   and   $15\%$   respectively,  the 3-month forward then would be   $18.71\%$   as per the above equation.
The above relationship can be used to calculate forward vol at ili ties for the entire [volatility surface](../7.%20Black%20Scholes%20Model.md).  However, this calculation does assume that skew in absolute (fixed) time is fixed.

# 1.2  Features

The buyer of a [forward volatility agreement](.md) enters a contract to buy at specified future date  “fixing” date, an OTM straddle maturing at a date after the start or the trade date of the straddle  strategy.  The volatility level of the OTM straddle is agreed initially such that there is a zero cost  to enter into the strategy. For example, the quoted volatility for the FVA is the forward volatility  level that gives a zero cost.

The strike of the straddle is fixed to the date on which the term of the options begins, and at the  same time the forward spot is set for the exercise date of the straddle. The premium of the forward  volatility agreement is also calculated and paid on the forward date.

The amount paid for the [forward volatility agreement](.md) is calculated as follows:
$$
p a y\circ\mathcal{V}_{s r v a}(\mathcal{N},\sigma,\sigma_{_{j k x}})=\bar{N}\cdot\left(\bar{V}_{s t r o a x\bar{a}\bar{a}e}(\sigma)-\bar{V}_{s t r o a x\bar{a}e}(\sigma_{_{j k x}})\right)
$$

Where
$N$   is the nominal value of the [forward volatility agreement](.md),
$\sigma$    is the current volatility,
$\sigma_{f i x}$   is the agreed volatility,

V straddle  is the value of the options.

The calculation rule is applied only if the horizon date is before or on the forward date. If the  horizon date is after the forward date, the value of the forward volatility agreements is zero.

The following formula provides the value  v FVA  for a purchase of a straddle for the forward date:
#  $=4\cdot e^{-\bar{\gamma}(\bar{t},T)(\bar{\gamma}-\bar{t})}\cdot e^{(\bar{\gamma}(\bar{t},T)-q(\bar{t},T))(\bar{\gamma}-\bar{t})}\cdot s(\bar{t})\cdot\left[\bar{N}\!\left(\frac12\,\sigma(\bar{t},t_{\bar{F}},T)\sqrt{T-t_{\bar{F}}}\right)\!-\bar{N}\!\left(\frac12\,\sigma_{\bar{\gamma}\bar{t}\kappa}\sqrt{T-t_{\bar{F}}}\right)\right]$
$s(t)$       is the spot price of the underlying of the straddle,    r(t 1 ,t 2 )    is the [risk-free interest rate](../../Financial%20Markets/Financial%20Asset%20Pricing%20Theory%20Overview/Chapter%2012%20-%20Derivatives/Exercises.md) for the period  $t_{I}$   through to   $t_{2}$  ,   q(t 1 ,t 2 )    is the dividend rate for the period  $t_{I}$   through to  $t_{2}$  ,    σ fix     is the volatility agreed on the contract date,    $\sigma(t,t_{F},T)$     is the forward volatility at time point  $t$   for the period   $t_{F}$    through to T ,   N(x)     is the cumulative normal distribution.

[Continuous compounding](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%202/Interest%20Rate%20Quotations.md) is used for interest rate   $r$   and dividend rate  $q$  ; yield curve   $r(t_{E},T)$   is  used for [forward rate](../../Clippings/Forward%20Points%20in%20Currency.md)  $r(t,T)$  , in which  $t_{E}$   is the evaluation date. The current forward volatility is  calculated as follows:
$$
\sigma(t,t_{F},T)=\sqrt{\frac{\sigma^{2}(t,T)\cdot(T-t)-\sigma^{3}(t,t_{F})\cdot(t_{F}-t)}{T-t_{F}}}
$$

This is the same as equation ( 1.1).  Only slightly different notation has been used.

If the underlying of the straddle is an exchange rate,   $r$   is the [risk-free interest rate](../../Financial%20Markets/Financial%20Asset%20Pricing%20Theory%20Overview/Chapter%2012%20-%20Derivatives/Exercises.md) for the local  [currency](../../Financial%20Instruments/Lecture%20Notes-%20Financial%20Instruments/Teaching%20Note%201-%20Forward%20Rates%20Agreement/Forwards%20and%20Futures%20Notes.md), and  $q$   the [risk-free interest rate](../../Financial%20Markets/Financial%20Asset%20Pricing%20Theory%20Overview/Chapter%2012%20-%20Derivatives/Exercises.md) for the foreign [currency](../../Financial%20Instruments/Lecture%20Notes-%20Financial%20Instruments/Teaching%20Note%201-%20Forward%20Rates%20Agreement/Forwards%20and%20Futures%20Notes.md).

The calculation rule uses the [Black-Scholes formula](../../Credit%20Markets/Credit%20Markets%20Session%205.md) for [pricing](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%207/Arbitrage%20Pricing%20of%20Derivatives.md) options. This formula first prices  the components of the straddle - the [call and put](../../Course%20Notes/HBR%20Notes/Notes%20on%20Basic%20Options%20Properties.md) options - by using the forward [interest rates](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%202/Interest%20Rate%20Quotations.md) and  the current forward volatility. The values for the straddles are totaled and discounted, and the  option premiums are deducted. This results in the calculation rule shown above for forward  volatility agreements, in which the premium of the term is given by the fixed volatility   $\sigma_{f i x}$  .

# 1.3 Variations;
Effectively an FVA is a [forward contract](../../Clippings/Forward%20Points%20in%20Currency.md) struck with a specified [implied volatility](../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%205%20Options%20on%20Prices%20and%20Hedge-Based%20Valuation/A%20Real-Life%20Option%20Pricing%20Exercise.md). Therefore on  the trade date both parties agree on: a reference forward volatility (strike volatility), a strike fixing  date and an option expiry date.

Physical Settlment:   On the strike fixing date the seller of the contract receives a cash premium  equal to the [Black-Scholes](../Mathematical%20Modeling%20of%20Derivative%20Pricing.md) (BS) price of the option calculated using the agreed strike volatility in  exchange for the option itself.

Cash Settlment:  On the strike fixing date the contract is settled with payment of the difference in  premium between the BS price of the option using the strike volatility and the prevailing market  volatility

Variations of FVA contract are currently restricted to the definition of strike of the straddle.  Typical variations are ATM Forward or the [delta neutral](../Derivatives/Part%20VI%20-%20The%20Greeks/Chapter%2027%20-%20Delta%20Hedging.md) straddle strike for standard [Black-Scholes](../Mathematical%20Modeling%20of%20Derivative%20Pricing.md)  delta or for [Black-Scholes](../Mathematical%20Modeling%20of%20Derivative%20Pricing.md) delta with option premium included.

# TERMSHEET

 ![500](Attachments/500-418.jpg)

From the above term-sheet, the strike of the straddle is defined to as [Delta Neutral](../Derivatives/Part%20VI%20-%20The%20Greeks/Chapter%2027%20-%20Delta%20Hedging.md) straddle. This  implies that the strike is solved for such that the aggregate delta of the straddle is zero.

Consider a situation where one believes the [implied volatility](../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%205%20Options%20on%20Prices%20and%20Hedge-Based%20Valuation/A%20Real-Life%20Option%20Pricing%20Exercise.md) for a given [currency](../../Financial%20Instruments/Lecture%20Notes-%20Financial%20Instruments/Teaching%20Note%201-%20Forward%20Rates%20Agreement/Forwards%20and%20Futures%20Notes.md) on a given tenor  will be higher at some point in the future. For example, 3 month EUR-USD will be higher, 3 month  from now. One can then enter a   $3^{*}6$   [forward volatility agreement](.md) for a notional of USD 100,000.  Assume that the agreed forward volatility level at inception of the contract was at   $10\%$  . There is  no premium paid at this stage.
Settlement Date:  04/18/2012    Maturity  07/18/2012 [Currency](../../Financial%20Instruments/Lecture%20Notes-%20Financial%20Instruments/Teaching%20Note%201-%20Forward%20Rates%20Agreement/Forwards%20and%20Futures%20Notes.md)    EUR-USD  Notional     100,000    Contract:     FVA  Tenor:      $3^{*}6$   (3 month option in 3 month time)        Agreed Volatility:   $10\%$   (the FVA rate)

# Contract Date: 01/18/2012 ( t 0 )

-   We enter into a 3x6 FVA Contract paying Fixed FVA rate of   $10\%$      -   Notional  $=$   100,000 USD     -   No upfront Premium

# Settlement Date: 04/18/2012:

-   On settlement date   $(t{+}k)$   if the 3 month [Implied volatility](../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%205%20Options%20on%20Prices%20and%20Hedge-Based%20Valuation/A%20Real-Life%20Option%20Pricing%20Exercise.md) is   $11\%$  , then    -   The deal settles into ATMF Straddle position with notional of say 25M per leg    -   The premium to pay for this straddle is then   $\mathbf{EUC}\%$   3.9847 (3 month Straddle priced at   $10\%$   volatility    -   If the observed implied 3 month volatility on settlement date is   $11\%$  , The position could  be closed out immediately at   $11\%$   volatility level which corresponds to   $\mathbf{EUC}\%$   4.3839  (Straddle premium priced at   $11\%$   volatility)     -   Recall the FVA payoff:
$$
p a y\circ\mathcal{V}_{s t r a x}(\mathcal{N},\sigma,\sigma_{j x})=\bar{N}\cdot\left\langle\bar{V}_{s t r a x\bar{\alpha}e}(\sigma)-\bar{V}_{s t r a x\bar{\alpha}e}(\sigma_{j x})\right\rangle
$$

The net profit if cash settled is:   $25\mathbf{M}\times(0.043839-0.039847)=3$  approximately, 100,000
 ![500](Attachments/500-419.jpg)

 ![500](Attachments/500-425.jpg)

On settlement date, we are [pricing](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%207/Arbitrage%20Pricing%20of%20Derivatives.md)  EUR-USD Straddle position which  expires in 3 month time and with a  volatility of   $10\%$   which is the fixed  FVA rate.

The upfront premium is  $\mathbf{EUC}\%$  3.9847

On Settlement date, if the observed 3  moths [spot implied volatility](.md) is  $11\%.$  ,  we can cash settle the deal by the  difference in premium using the two  vols.

 ![500](Attachments/500-417.jpg)
# FVA EXAMPLE (BID/ASK SPREAD)

Consider an investor who on September 25, 2007 enters a   $I$  -month FVA written on the dollar price  of the euro (EUR) with a notional of M = 1,000,000 USD. Note that for this example we go back  to using two subscripts to clearly identify the start and end of the volatility interval.

Table below lists the Garman.Kohlhagen   $I$  -month and 2-month IVs available on this date from  Bloomberg at five fixed deltas: 10-delta put, 25-delta put, ATMF, 25-delta call and 10-delta call.  The   $I$  -month spot  $I V(S V t;t{+}I)$   covers the period of September 25, 2007 to October 25, 2007, and  the 2-month spot  $I V(S V t;t{+}2)$   covers the period of September 25, 2007 to November 25, 2007.

Given these quotes, we compute the model-free   $I$  -month and 2-month spot IVs as in Jiang and  Tian (2005) and Carr and Wu (2009), which turn out to be   $S V t;t+I\,=\,6{:}930\%$   and   $S V t;t+2=$     $6{\cdot}895\%$  . It is then straightforward to plug these values into above equation to compute the modelfree   $I$  -month forward   $I V\left(F V\right)$   that is known on September 25, 2007 and covers the period of  October 25, 2007 to November 25, 2007. The model-free forward   $I V$   is the fair delivery price of  the FVA and is equal to  $F V=6{:}860\%$  .

These figures suggest a downward-sloping volatility curve. In a real trade, the FVA delivery price  is quoted with a [bid-ask spread](../../Financial%20Markets%20and%20Institutions/III.%20Liquidity%20of%20Assets/Class%205-%20Private%20Information,%20Liquidity,%20and%20Securitization/Bid%20Ask%20and%20Transaction%20Prices%20in%20a%20Specialist%20Market%20With%20Heterogeneously%20Informed%20Traders.md), which typically revolves around  $\it{0:5\%}$   for major currencies such  as EUR. If the trader goes long the FVA, the contract will expire on October 25, 2007 and deliver  a payoff equal to   $(S V t{+}I;t{+}2\;{\bar{\mathbf{\nabla}}}F V-O.5\%)\,x\,M,$  , where  $\scriptstyle S V t+I;t+2$   is the model-free 1-month spot  IV computed on October 25, 2007 that covers the period of October 25, 2007 to November 25,  2007. As seen in Table below, it turns out that   $S V t{+}I{;}t{+}2\,=\,7{\cdot}75O\%$  . Hence, the FVA is cashsettled with a payoff of 390, 000 USD .

 ![500](Attachments/500-404.jpg)
# Table (data source Bloomberg)
$_{t+1}$   $S V_{t,t+1}$   $S V_{t,t+2}$   $F V_{t}^{1}$   $S V_{t+1,t+2}$   $S V_{t,t+1}$   $S V_{t,t+2}$   $F V_{t}^{1}$   $S V_{t+1,t+2}$   $(S V_{t+1,t+2}-F V_{t}^{1}-0.5\%)$   $1,000,000$   $0.5\%$

 ![500](Attachments/500-431.jpg)
# 2.1 Pricing and Hedging FVA’s

Isolating Local Volatility with “Gadgets”

Local or forward volatility is the market price of volatility you can lock in today to obtain volatility  exposure over specific some range of future times and market levels.

In the interest rate world, for example, you can lock in future [interest rates](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%202/Interest%20Rate%20Quotations.md) between two years and  three years by going simultaneously long a three-year zero-coupon bond and short a two-year zerocoupon bond, such that the present value of the total bond [portfolio](../../Advanced%20Investments/An%20Asset%20Allocation%20Primer.md) is zero.

In this way you lock in the one-year [forward rate](../../Clippings/Forward%20Points%20in%20Currency.md) two years from now. This bond [portfolio](../../Advanced%20Investments/An%20Asset%20Allocation%20Primer.md) has  exposure only to this particular [forward rate](../../Clippings/Forward%20Points%20in%20Currency.md). As time passes, this [portfolio](../../Advanced%20Investments/An%20Asset%20Allocation%20Primer.md) increases in value as  the [forward rate](../../Clippings/Forward%20Points%20in%20Currency.md) drops, and decreases as it rises.

Something similar can be done with option. A volatility gadget is a small [portfolio](../../Advanced%20Investments/An%20Asset%20Allocation%20Primer.md) of standard  index options, created out of a [long position](../Derivatives/Part%20I%20-%20Forwards%20and%20Futures/Chapter%204%20-%20Futures:%20Hedging%20and%20Speculation.md) in a calendar spread and a short position in an  overlapping butterfly spread that has zero total options value.

This gadget is sensitive to (forward) local index volatility only in the region between the strikes  and expiration s of the spreads in the gadget. Figure 3b illustrates the volatility gadget. By buying  or selling suitably constructed gadgets corresponding to different future times and index levels, we  can theoretically hedge an index option [portfolio](../../Advanced%20Investments/An%20Asset%20Allocation%20Primer.md) against changes in future local volatility.

 ![500](Attachments/500-412.jpg)

See, (Derman, E., Kani, I., and Kamal, M., \`Trading and [Hedging](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%205/Key%20Rates%20O1s%20Durations%20and%20Hedging.md) Local Volatility',  Quantitative Strategies Research Notes, Goldman Sachs & Co, 1996
# Forward Start Straddle (STO)

Forward start option can be used to price contracts such as [Forward Rate](../../Clippings/Forward%20Points%20in%20Currency.md) Agreement (FVA), which  is also a trade on [implied volatility](../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%205%20Options%20on%20Prices%20and%20Hedge-Based%20Valuation/A%20Real-Life%20Option%20Pricing%20Exercise.md) at a future date.

When defining a forward start, you can choose a ATM [delta neutral](../Derivatives/Part%20VI%20-%20The%20Greeks/Chapter%2027%20-%20Delta%20Hedging.md) straddle, with the strike set on  the forward start date (or strike fixing date). This is exactly the physical trade that takes place when  an FVA is fixed.

For example, you trade a [delta neutral](../Derivatives/Part%20VI%20-%20The%20Greeks/Chapter%2027%20-%20Delta%20Hedging.md) straddle forward start option with an expiry date of six  months and a forward start of three months, also known as a  $3^{*}6$   FVA. In three months time, the  strike (which now has 3 months to expiry) is fixed to give a [delta neutral](../Derivatives/Part%20VI%20-%20The%20Greeks/Chapter%2027%20-%20Delta%20Hedging.md) straddle.

In this case, the buyer of the option is effectively buying volatility for three months starting in  three months. The exposure of the buyer is long 6-month Vega and short 3-month Vega. This is  quoted in the interbank market in terms of [implied volatility](../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%205%20Options%20on%20Prices%20and%20Hedge-Based%20Valuation/A%20Real-Life%20Option%20Pricing%20Exercise.md).

The value of the forward start straddle at maturity depends then on the volatility expected in the  interval  $\mathrm{T}_{1}$   to   $\mathrm{T}_{2}$   and therefore it is a tool to hedge future volatility. It is sensitive to changes in  volatility but not to changes in [interest rates](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%202/Interest%20Rate%20Quotations.md) or to a large change in spot.

Brenner, Earnest Y.Ou and Zhang have investigated the valuations of forward start options on  equity indices using [Stochastic Volatility](../../Course%20Notes/Python/QuantLib-Python/Valuing%20European%20Option%20Using%20the%20Heston%20Model%20in%20QuantLib%20Python.md) Model (SV) similar to the one by Stein and Stein (1991).  We present a summary of their key results below:
$$
\begin{array}{r l}&{{d S_{t}}=r S_{t}d t+\sigma_{t}S_{t}d B_{t}^{1}}\\ &{}\\ &{{d\sigma_{t}}=\delta(\theta-\sigma_{t})d t+k d B_{t}^{1}}\end{array}
$$

Where   dS  describes the dynamics of the underlying with a [stochastic volatility](../../Course%20Notes/Python/QuantLib-Python/Valuing%20European%20Option%20Using%20the%20Heston%20Model%20in%20QuantLib%20Python.md).

The second equation describes the dynamics of volatility itself which is reverting to a long run  mean, and has an adjustment rate and volatility of volatility. This model assumes a zero correlation  between the conditional joint density of [returns](../../Financial%20Markets/Financial%20Asset%20Pricing%20Theory%20Overview/Chapter%203%20-%20%20Assets,%20Portfolios,%20and%20Arbitrage/Assets.md) and volatility.

Results from the above model show that for relatively low strike prices, the effect of stochastic  volatility is rather small and the values are not that different from a BS value (when vol-of-vol  value is zero).  For higher strike prices (OTM), the effect of vol-of-vol, is much larger.

They have also showed that the sensitivity of the straddle position to changes in initial volatility.  This shows that the position was extremely sensitive to changes in volatility and declined in value  when volatility decreased. Also, the higher the vol-of-vol, the higher is the vega of the forward  strart straddle position.$i=0$   $K_{\mathrm{SID}}$
 ![500](Attachments/500-428.jpg)
 $=0.20,\theta,$   $=$   $=4.00$   $T_{1}=0.5,$

 ![500](Attachments/500-403.jpg)
 $k$   $K_{\mathrm{STO}}$   $k\,S_{0}\,{=}\,100,r\,{=}\,0$   $\bar{\sigma}_{\bar{0}}=0.20$   $\beta\!=\!0.20$   $\delta\!=\!4.00$   $T_{\mathrm{i}}=0.5$   $T_{2}=1.0$
# Trading FVA’s

An investor who believes that the [implied volatility](../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%205%20Options%20on%20Prices%20and%20Hedge-Based%20Valuation/A%20Real-Life%20Option%20Pricing%20Exercise.md) will be higher (lower) level then predicted by  the forward volatility market, can enter into a [Forward Volatility Agreement](.md) (FVA):
$\checkmark$    If [implied volatility](../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%205%20Options%20on%20Prices%20and%20Hedge-Based%20Valuation/A%20Real-Life%20Option%20Pricing%20Exercise.md) is expected to be higher ----  $\cdot\xrightarrow{}$   buy/take a long FVA position   $\checkmark$    If [implied volatility](../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%205%20Options%20on%20Prices%20and%20Hedge-Based%20Valuation/A%20Real-Life%20Option%20Pricing%20Exercise.md) is expected to be lower ----  $\cdot\xrightarrow{}$   Sell/take a short FVA position

 ![500](Attachments/500-431.jpg)
Figure 2.1 (3 month forward volatility from different terms-structure; source [Credit Suisse](../../Financial%20Markets%20and%20Institutions/III.%20Liquidity%20of%20Assets/Class%208-%20Markets,%20Meltdowns,%20and%20Arbitrage/The%20Economist%20Margin%20Call%20of%20the%20Wild.md)

[Forward volatility agreement](.md) may provide investors with long-term volatility (Vega) exposure,  without having exposure to short-term volatility (Gamma). This type of product does not have to  pay Theta as the gamma of the position is zero initially until the start of FVA’s trade date.

However, even-though the Theta may be zero for forward starting product compared to vanilla  options, if there is a rise in volatility surfaces before the forward staring period is over, they are  likely to benefit less then vanilla options (this is because the front end of the volatility surfaces  tend to move the most, and this is the area to which the forward start has no sensitivity).

While the FVA product may have zero mathematical Theta, they might suffer from the fact that  volatility and variance term-structure is usually expensive and upward sloping. The average  [implied volatility](../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%205%20Options%20on%20Prices%20and%20Hedge-Based%20Valuation/A%20Real-Life%20Option%20Pricing%20Exercise.md) of the FVA product is likely to be higher than vanilla product, which will cause  the [long forward](../../Financial%20Instruments/Lecture%20Notes-%20Financial%20Instruments/Teaching%20Note%203%20Swaps-%20Financial%20Instruments/Forward%20Rates%20Agreement.md) starting position to suffer carry as the volatility is re-marked lower during the  forward starting period (if a 3-month forward starting option is compared to a 3-month vanilla  option, then during the forward starting period the forward starting [implied volatility](../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%205%20Options%20on%20Prices%20and%20Hedge-Based%20Valuation/A%20Real-Life%20Option%20Pricing%20Exercise.md) should, on  average, decline.
# GENERIC OPTION VALUATION (OVGE)

If we look at the current implied forward volatility that commences 3 month from now and expires  3 months later. We can see from the table below that the 3x6 for EURUSD quote is:   $11.541\%$  .  Even-though the market quote for future date is unknown, however, the current [volatility surface](../7.%20Black%20Scholes%20Model.md)  can be used to extract future or instantaneous vol at ili ties.

 ![500](Attachments/500-427.jpg)

We can compare the above extrapolated forward volatility from the current vanilla surface for a  given tenor to a model dependent volatility strike computed from FVA [pricing](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%207/Arbitrage%20Pricing%20of%20Derivatives.md).

Using Bloomberg OVGE screen, we price up 3month FVA, expiring 3 months after the FVA’s  date:

[Currency](../../Financial%20Instruments/Lecture%20Notes-%20Financial%20Instruments/Teaching%20Note%201-%20Forward%20Rates%20Agreement/Forwards%20and%20Futures%20Notes.md) Pair: EUR-USD

Trade date:   04/30/2012  FVA date:  07/30/2012  Expiry Date: 10/30/2012  Notional:   100,000,000  Not.Curncy: EUR  Agreed Vol:   $11.574\%$     Market Quote:   $11.574\%$   (3x6)

To simplify the example, we can set the agreed volatility strike the same as the market extrapolated  volatility for the tenor of FVA contract. Then;

We use the FVA template in Bloomberg OVGE screen. We enter the trade date, Domestic and  Foreign currencies, the FVA date and the final expiry of the contract. We solve for the volatility  strike that produces zero price (as close as possible). One limitation with OVGE is that it does not  have solver functionality and for this reason, we keep changing the volatility strike until we get  price that is close enough to zero or negligibly small. In this case, we have solved for   $10.3\%$    volatility strike. The solved volatility strike gives a  $0.02\%$   price of the notional which is very small.  Please note that in order to speed up the calculations; we are using MC [Heston](../Mathematical%20Modeling%20of%20Derivative%20Pricing.md) but only up to 1000  sample paths.
As expected when using [stochastic volatility](../../Course%20Notes/Python/QuantLib-Python/Valuing%20European%20Option%20Using%20the%20Heston%20Model%20in%20QuantLib%20Python.md) models, the model tends to undervalue the market  price or quoted prices and this is mainly due to the correlation between spot and volatility.  The  dynamics of the observed [volatility surface](../7.%20Black%20Scholes%20Model.md) when spot moves is inconsistent with the result from  [stochastic volatility](../../Course%20Notes/Python/QuantLib-Python/Valuing%20European%20Option%20Using%20the%20Heston%20Model%20in%20QuantLib%20Python.md) models.

To hedge the above FVA contract:

Enter long 6 month EUR-USD Straddle position on EUR 10,000,000 notional

Enter short 3 month EUR-USD Straddle position on EUR 10,000,000 notional

The net position should leave us a long 3 month long Vega. On the trade date, the position should  have zero Delta and Gamma but we with constant Vega as spot moves from trade date until the  contract (FVA’s) start date.

We can maintain constant Vega until the FVA date but once the FVA date is reached, the position  will have regular Vega position as Vanilla option and will need to be risk managed. As the market  moves, the strike is then away from the DNS (Delta-Neutral Straddle). To maintain the Delta  neutrality of the position, the trader needs to buy/sell the underlying.

As mentioned above the FVA contract does not need to be delta hedged before the forward starting  period ends. However, such contracts need to be Vega hedged with vanilla, out-of-the money  Straddles (as they do have zero Delta and Gamma). A long OTM straddle has to be purchased on  the expiry date of the option (6 month), while a short OTM Straddle has to be sold on the strike  fixing date (3 month).  As the spot moves, the delta of these Straddles is likely to move away from  zero, requiring re-[hedging](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%205/Key%20Rates%20O1s%20Durations%20and%20Hedging.md) of the position, which increases the costs (which are likely to be passed  on to clients) and risks (unknown future volatility and skew) to the trader.

From inception of the contract until the FVA’s date, we maintain a constant Vega position. Given  the above [portfolio](../../Advanced%20Investments/An%20Asset%20Allocation%20Primer.md) of vanilla positions, we then risk manage the Delta/[Gamma risk](../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%205%20Options%20on%20Prices%20and%20Hedge-Based%20Valuation/Residual%20Risk%20of%20Options%20Gamma%20Vega%20and%20Volatil.md), [Vega risk](../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%205%20Options%20on%20Prices%20and%20Hedge-Based%20Valuation/Residual%20Risk%20of%20Options%20Gamma%20Vega%20and%20Volatil.md), as  well as Vanna and Volga risk.
# DELTA RISK :
$$
C a l l O p t i o n=S\;x N(d_{1})-K e^{-r T}N(d_{2})
$$
$$
P u t O p t i o n=-S\;x N(-d_{1})+K e^{-r T}N(d_{2})
$$

Where
$$
\begin{array}{r}{d_{1}=\frac{l n\left(\frac{S}{K}\right)+\left(r+\frac{\sigma^{2}}{2}\right)T}{\sigma\sqrt{T}}}\end{array}
$$

Delt  $\mathrm{a}=\mathbf{N}(\mathbf{d}\mathrm{\mathbf{\mathbf{l}}})$

To maintain the delta neutrality of the position once after the FVA’s date, we need to buy/sell an  amount equivalent of the delta of the position.

# STRIKE-LESS VEGA

Both [Volatility Swap](../Variance%20Swaps.md) and FVA’s initially give exposure to strike-less Vega (exposure to implied  volatility that remains constant as spot moves). This is because the ATM straddle is not set until  the FVA’s fixing date / start date.

 ![500](Attachments/500-411.jpg)

The FVA’s strike-less Vega is constant until the strike fixing date and once the strike is fixed at  fixing date of the FVA, the Vega profile is similar to Vanilla and varies with the underlying.

# RISK MANAGE GAMMA OF VOLATILITY EXPOSURE (VOLGA)

Volga represents the sensitivity of vega to change in [implied volatility](../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%205%20Options%20on%20Prices%20and%20Hedge-Based%20Valuation/A%20Real-Life%20Option%20Pricing%20Exercise.md). Mathematically;
$$
V o l g a=\frac{\delta^{2}\mathrm{P}}{\upsigma\delta^{2}}
$$

   The first derivative of vega with respect to a change in volatility.
   The second derivative of option value with respect to a change in volatility (hence  the other name as  Gamma Vega ).

The volga is also referred to as Vomma. For volatility movements, Volga is to Vega what gamma  is to delta (for spot movement).

For complex exotics such as FVA’s that requires [stochastic volatility](../../Course%20Notes/Python/QuantLib-Python/Valuing%20European%20Option%20Using%20the%20Heston%20Model%20in%20QuantLib%20Python.md) models, one need to compute  volga and other [Greeks](../Derivatives/Part%20V%20-%20Options%20Pricing/Chapter%2026%20-%20Pricing%20Options:%20Monte%20Carlo%20Simulation.md) with respect to model parameters.

 ![500](Attachments/500-430.jpg)

The interest of Volga is to measure the [convexity](../../Fixed%20Income%20Asset%20Pricing/Problem%20Sets/PSET%20II%20Fixed%20Income%20Asset%20Pricing%201.md) of an FVA position with respect to volatility.  FVA contract with high Volga benefits from volatility of volatility.

Hence, volatility dependent [derivatives](../../Financial%20Markets/Financial%20Trading%20and%20Markets/Chapter%209%20Arbitrage%20and%20Hedging%20With%20Options.md) such as FVA with substantial Volga, [pricing](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%207/Arbitrage%20Pricing%20of%20Derivatives.md) with a  [stochastic volatility](../../Course%20Notes/Python/QuantLib-Python/Valuing%20European%20Option%20Using%20the%20Heston%20Model%20in%20QuantLib%20Python.md) model with high volatility of volatility may change the price dramatically.

For complex exotics such as FVA, traders cannot just simply ignore the risk due to the change of  Vega. They have to understand the change of the Vega with respect to the spot (see Vanna) and to  the volatility itself. And to have a better understanding of Volga, it is important to stress the variety  of models to account for the smile surface. In particular the shape of Volga would crucially depend  on the choice of model out of the following list of models:

   [Stochastic volatility](../../Course%20Notes/Python/QuantLib-Python/Valuing%20European%20Option%20Using%20the%20Heston%20Model%20in%20QuantLib%20Python.md) models: the correlation effect between the stock and the volatility  plays an important role in shaping the vega change.     Local volatility model where the resulting local volatility is a function of the  underlying itself.     Jumps models with jumps correlated to the volatility parameters.       Combination of the above, like Lévy processes.
     Discrete type option [pricing](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%207/Arbitrage%20Pricing%20of%20Derivatives.md) models that are in fact, disc ret is ed versions of the models  above. For instance ARCH/GARCH processes are just discrete versions of stochastic  volatility models.

# RISK MANAGE SKEW EXPOSURE (VANNA)

Vanna measures the change in delta due to a change in volatility. It measures the size of the skew  position. Vanna is the slope of vega plotted against spot.

 ![500](Attachments/500-429.jpg)

The Vanna is a second order “cross” [Greeks](../Derivatives/Part%20V%20-%20Options%20Pricing/Chapter%2026%20-%20Pricing%20Options:%20Monte%20Carlo%20Simulation.md). Like any other cross [Greeks](../Derivatives/Part%20V%20-%20Options%20Pricing/Chapter%2026%20-%20Pricing%20Options:%20Monte%20Carlo%20Simulation.md), the Vanna can be  defined in many ways:

   First derivative of Vega with respect to a change in the underlying.     First derivative of delta with respect to a change in volatility.     Second derivative of option value with respect to a joint moved in volatility and underlying.

To account for the complexity of the smile and in particular its skew and [convexity](../../Fixed%20Income%20Asset%20Pricing/Problem%20Sets/PSET%20II%20Fixed%20Income%20Asset%20Pricing%201.md), one needs to  take the route of more realistic models including deterministic local volatility, [stochastic volatility](../../Course%20Notes/Python/QuantLib-Python/Valuing%20European%20Option%20Using%20the%20Heston%20Model%20in%20QuantLib%20Python.md)  and jumps (see smile modeling), and most recent model that combines both Local Volatility and  [Stochastic Volatility](../../Course%20Notes/Python/QuantLib-Python/Valuing%20European%20Option%20Using%20the%20Heston%20Model%20in%20QuantLib%20Python.md) models (SLV).

Stochastic models can change considerably the shape of the Vanna as they explicitly specify the  correlation between volatility and the spot. If spot and volatility are positively correlated, the  holder of the option with positive Vanna will benefit from the correlation.
# Review of Variance Swap risks:

To hedge [variance swap](../Variance%20Swaps.md), market makers hold a [portfolio](../../Advanced%20Investments/An%20Asset%20Allocation%20Primer.md) of single stock options and carry out    daily [delta hedging](../../Financial%20Instruments/Financial%20Instruments.md).

The hedge held by market-makers consisted of a [portfolio](../../Advanced%20Investments/An%20Asset%20Allocation%20Primer.md) of options built in such a way to have  constant dollar gamma both for movements in the stock prices and for the passage of time. This  [portfolio](../../Advanced%20Investments/An%20Asset%20Allocation%20Primer.md) can be theoretically created by combining an infinite number of options with strikes  spanning all possible values of the stock and the same maturity as the [variance swap](../Variance%20Swaps.md). Figure 3  shows the dollar gamma profile of individual options of different strikes. Weighting the options  according to 1/Strike\*Strike creates a [portfolio](../../Advanced%20Investments/An%20Asset%20Allocation%20Primer.md) with the flat gamma profile needed to hedge a  [variance swap](../Variance%20Swaps.md)

The [static hedge](Uncertain%20Volatility%20with%20Static%20Hedge.md) has some practical limits:

1-   Impossible to trade an infinite number of options with infinite number of strikes  2-   [Liquidity](../../Financial%20Markets%20and%20Institutions/III.%20Liquidity%20of%20Assets/Class%205-%20Private%20Information,%20Liquidity,%20and%20Securitization/Class%20Note%2010%20Liquidity%20and%20Class%20Note%2010%20Liquidity%20and%20Liquidity%20Managementliquidity%20management.md) of OTM options are limited, restricting the number of tradable options  3-   Market makers are unable to buy complete theoretical hedge  4-   We can only do approximate hedge within specified range of spot

Figure 4 shows the dollar gamma profile of holding portfolios of 1, 2 and 5 options, and illustrates  the limited range of spot levels for which the dollar gamma profile is flat.

 ![500](Attachments/500-414.jpg)

 ![500](Attachments/500-407.jpg)

After the market declined, many single stock option desks became forced buyers of low strike  options, in order to manage the gamma and [vega risk](../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%205%20Options%20on%20Prices%20and%20Hedge-Based%20Valuation/Residual%20Risk%20of%20Options%20Gamma%20Vega%20and%20Volatil.md) of the [variance swap](../Variance%20Swaps.md) positions in their books.  In fact, by selling variance swaps, the traders had committed to deliver the P/L of a constant dollar  gamma [portfolio](../../Advanced%20Investments/An%20Asset%20Allocation%20Primer.md), irrespective of the spot level, but their [replicating portfolio](../../Pricing%20Forwards,%20Futures,%20Bonds,%20Swaps,%20Swaptions,%20Caps%20and%20Floors%20under%20No-Arbitrage%20and%20Risk-Neutral%20Pricing.md) did not have  sufficient dollar gamma at the new spot levels. Market makers were therefore forced to buy low  strike options at the post-crash volatility level, which was much higher than the one prevailing  when they sold the [variance swap](../Variance%20Swaps.md), and therefore incurred heavy losses.
Not re-[hedging](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%205/Key%20Rates%20O1s%20Durations%20and%20Hedging.md) the [gamma risk](../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%205%20Options%20on%20Prices%20and%20Hedge-Based%20Valuation/Residual%20Risk%20of%20Options%20Gamma%20Vega%20and%20Volatil.md) was not a possibility, as this would have left the books exposed to  potentially catastrophic losses if the stock prices declined further, and volatility continued to  increase. The [convexity](../../Fixed%20Income%20Asset%20Pricing/Problem%20Sets/PSET%20II%20Fixed%20Income%20Asset%20Pricing%201.md) of the [variance swap](../Variance%20Swaps.md) payoff further exacerbated the downside risk. This  situation led to large losses for many market-makers in the single stock [variance swap](../Variance%20Swaps.md) markets. In  turn this led banks to re-assess the risk of making markets in these instruments and to a substantial  shutdown of the single stock [variance swap market](../Variance%20Swaps.md)

 ![500](Attachments/500-405.jpg)

 ![500](Attachments/500-410.jpg)
# Review of Volatility Swap risks:

Delta-[hedging](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%205/Key%20Rates%20O1s%20Durations%20and%20Hedging.md) options leads to a P/L linked to the variance of [returns](../../Financial%20Markets/Financial%20Asset%20Pricing%20Theory%20Overview/Chapter%203%20-%20%20Assets,%20Portfolios,%20and%20Arbitrage/Assets.md) rather than volatility. To  achieve the linear exposure to volatility which volatility swaps provide it is therefore necessary to  dynamically trade in portfolios of options, which would otherwise provide an exposure to the  square of volatility. A [volatility swap](../Variance%20Swaps.md) can be thought as a non-linear derivative of realized variance,  the ‘underlier’ that can be traded through portfolios of delta-hedged options.

To hedge [volatility swap](../Variance%20Swaps.md) with [variance swap](../Variance%20Swaps.md), the trader would need to trade in and out of variance  swaps in order to replicate the square root of variance payoff of the [volatility swap](../Variance%20Swaps.md).

The [volatility swap](../Variance%20Swaps.md) payoff can be locally approximated by a [variance swap](../Variance%20Swaps.md), where the variance  swap begins to outperform the further realized volatility moves from the initial strike. Thus, the  [volatility swap](../Variance%20Swaps.md) could theoretically be replicated through “delta-[hedging](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%205/Key%20Rates%20O1s%20Durations%20and%20Hedging.md)” by trading dynamically  in the [variance swap](../Variance%20Swaps.md), where the “delta” is the sensitivity to the instruments’ underlying, namely  realized variance. Changes in this volatility “delta” will depend on the investor’s estimate of  volatility of volatility.

 ![500](Attachments/500-426.jpg)
A [volatility swap](../Variance%20Swaps.md) can be replicated using a [delta-hedged portfolio](../../Financial%20Instruments/Financial%20Derivatives%20and%20Quantitative%20Methods/JP%20Morgan-Variance%20Swaps.md) of options, where the [portfolio](../../Advanced%20Investments/An%20Asset%20Allocation%20Primer.md)  of options is dynamically rebalanced to replicate the Vega and gamma profile of the [volatility swap](../Variance%20Swaps.md)  across the range of [spot prices](../../Financial%20Instruments/Lecture%20Notes-%20Financial%20Instruments/Teaching%20Note%201-%20Forward%20Rates%20Agreement/Contango%20And%20Backwardation%20In%20Arbitrage-Free%20Futures-Markets.md).

One possible approach to [hedging](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%205/Key%20Rates%20O1s%20Durations%20and%20Hedging.md) the [volatility swap](../Variance%20Swaps.md) is to trade delta-hedged ratio strangles (e.g.  short   $1.5\;80\%$   strike puts and short one   $120\%$   call to hedge a long [volatility swap](../Variance%20Swaps.md)), where the ratio  and strikes are set in order to minimize the net exposure to volatility across the skew (i.e. to attempt  to match the Vega profile of the options to the [volatility swap](../Variance%20Swaps.md) over a range of anticipated spot  levels). Since the Vega exposure of the strangle and [volatility swap](../Variance%20Swaps.md) differ as the spot changes, the  strangles will have to be re-striked when the net exposure to volatility exceeds the trader’s  tolerance .
Below, we can see how the Vega and gamma sensitivity of the [volatility swap](../Variance%20Swaps.md) compares to a  sample ratio strangle chosen to minimize the error for near-the-money Vega exposure for an  assumed level of volatility and skew.

The strangle notionals, strikes and the ratio of puts to calls will depend on the shape of the implied  [volatility skew](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%2016/Swaption%20Skew.md) at the time the hedge is put in place.

Additionally, it may not be possible to simultaneously replicate both vega and gamma well over a  broad range of spot levels with this approach, as is the case in the example below where the chosen  [portfolio](../../Advanced%20Investments/An%20Asset%20Allocation%20Primer.md) poorly replicates the gamma exposure of the [volatility swap](../Variance%20Swaps.md) below the spot.

 ![500](Attachments/500-413.jpg)

 ![500](Attachments/500-415.jpg)

-   Re-striking may cause the need for new strangles to be initiated with significant different  volatility if the volatility level has shifted.

 -   More transaction costs

 -   P&L risk when re-striking the [hedging](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%205/Key%20Rates%20O1s%20Durations%20and%20Hedging.md) [portfolio](../../Advanced%20Investments/An%20Asset%20Allocation%20Primer.md) will depend on vol-of-vol

 -   Higher vol-of-vol leads to largest shifts in [pricing](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%207/Arbitrage%20Pricing%20of%20Derivatives.md) the options used for the hedge
# Valuation Models:

Volatility swaps and forward volatility agreements are more complex  instrument to price.   Volatility is the square root of variance, and is a more complex derivative of variance. Its value  depends not just on volatility, but on the volatility of volatility, and you have to dynamically hedge  it by trading variance swaps as the underlier. This is possible too, but needs a model for the  volatility of volatility.

We will review existing models and the most appropriate model for valuation of Forward Volatility  Agreement contract. However, the selected model should be able to produce realistic hedge ratios  or [Greeks](../Derivatives/Part%20V%20-%20Options%20Pricing/Chapter%2026%20-%20Pricing%20Options:%20Monte%20Carlo%20Simulation.md) such as Delta, Gamma, Vega, as well as [vega risk](../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%205%20Options%20on%20Prices%20and%20Hedge-Based%20Valuation/Residual%20Risk%20of%20Options%20Gamma%20Vega%20and%20Volatil.md) with respect to changes in both spot  and [implied volatility](../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%205%20Options%20on%20Prices%20and%20Hedge-Based%20Valuation/A%20Real-Life%20Option%20Pricing%20Exercise.md).

# 3.1 Appropriate Models;

# LOCAL VOLATILITY MODEL (LV)

T he Local Volatility Model (LV) extends the [Black-Scholes model](../../Financial%20Instruments/Black%20Scholes%20Derivation.md) by allowing the instantaneous  volatility to depend on spot and time (Dupire 1994).
$$
d S=S_{t}(r_{t}-q_{t})+\sigma(t,S_{t})S_{t}d W
$$

The Local Volatility function   $\sigma(t,S_{t})$   is a function to be inserted into the (3.1) which will  reproduce the current vanilla market prices. The function has no stochastic it y of its own, just  deterministic state dependency on time and underlying. This model class is considered less  complex since it does not involve individual stochastic differential equations (SDE) for the  volatility, it is merely described by a function.

Dupire found that the Local Volatility (LV) function could be derived as:
$$
\sigma(K,T)=\sqrt{2\frac{\displaystyle\frac{\delta C}{\delta K}+(r-d)K\,\frac{\delta C}{\delta K}+d C}{K^{2}\frac{\delta^{2}C}{\delta K^{2}}}}
$$
$\checkmark$    Simplest model consistent with the market   $\checkmark$    Local vol at ili ties are forward vol at ili ties   $\checkmark$    [Arbitrage](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%207/Arbitrage%20Pricing%20of%20Derivatives.md) free (positive and regular)   $\checkmark$    Implied vol at ili ties surface with strike extrapolation provides [variance swap](../Variance%20Swaps.md) fair value
#    Good IV surface should give an accurate risk neutral density

The deterministic LV function, represents a market consensus estimates for the instantaneous  volatility at some future time   $t$    with the asset at value  S.  It can be shown that the local variance   $\sigma^{2}(S,t)$   is the expectation of the future instantaneous variance  $\sigma^{2}(t)$   at time   $t$    conditional on the  asset having a value  $S$    at time   $t$  .

# Known Issues using Local Volatility (LV) Model

Since in local volatility models the volatility is a deterministic function of the random underlying   price, local volatility models are not very well used to price cliquet options, forward starting  options, [Forward Volatility Agreement](.md), as well as variance and volatility swaps, whose values  depend specifically on the random nature of volatility itself

Lian (2010) noted that one of the problems related to applying the Dupire equation is that options  might not be available for a complete range of strikes and maturity.

With insufficient data, the LV function might be severely mis specified. In addition, strikes for  deep ITM and OTM might cause the fraction in the above equation to become extremely small  which could lead to numerical issues as addressed in Lian (2010).

Local volatility Models are easy to implement and theoretically self consistent, as it is possible to  perfectly replicate all the vanilla option prices and to hedge every product with vanilla options.   However, Hagen (2002) argues that the dynamic behavior of spot volatility smile and skew  predicted by local volatility models is exactly opposite to the behavior observed in the market  place:

When the prices decreases, Local Volatility Models predict that the smile shifts to higher prices.  When the price increases, Local Volatility Models predict that the smile shifts to lower prices. In  reality asset prices and market smiles moves in the same direction. These inconsistencies lead to  incorrect hedges and hence incorrect [pricing](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%207/Arbitrage%20Pricing%20of%20Derivatives.md) for [exotic](../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%206%20Options%20on%20Non-Price%20Variables/Exotic%20Interest%20Rate%20Options.md) options.

 ![500](Attachments/500-420.jpg)
[Implied volatility](../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%205%20Options%20on%20Prices%20and%20Hedge-Based%20Valuation/A%20Real-Life%20Option%20Pricing%20Exercise.md)  $\sigma(K,f)$   if the forward prices decreases from  f 0  to f (solid line).
Local volatility models are deterministic models and produce sharply flattened future volatility  smiles and skews as seen in figure below, which shows the three month [forward implied volatility](.md)  skew at different reset dates, where 0M refers to the vanilla three-month option and 60M refers to  an option with three months' expiry starting in five years' time. We can see as we go out further in  time that the [volatility skew](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%2016/Swaption%20Skew.md) and curvature decays. This behavior is not observed in the market.

 ![500](Attachments/500-408.jpg)
Notice the flattening of the surface for lower and higher strikes

 ![500](Attachments/500-421.jpg)
Local [Volatility surface](../7.%20Black%20Scholes%20Model.md) for SX5E index

There are no documented empirical research testing the [pricing](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%207/Arbitrage%20Pricing%20of%20Derivatives.md) result of FVA’s against the market,  however, Behvan (2010) investigated the [pricing](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%207/Arbitrage%20Pricing%20of%20Derivatives.md) of structures that depend on forward volatility  such as Cliquet options (strip of forward starting options). Behvan (2010) compares the [pricing](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%207/Arbitrage%20Pricing%20of%20Derivatives.md)  result of Cliquet using Local Volatility model against market consensus (Totem).

 ![500](Attachments/500-406.jpg)

Red indicates results from the Local Vol. Model which are outside of the market consensus.
# STOCHASTIC VOLATILITY MODELS

# (HESTON);

The first [stochastic volatility](../../Course%20Notes/Python/QuantLib-Python/Valuing%20European%20Option%20Using%20the%20Heston%20Model%20in%20QuantLib%20Python.md) model was proposed by [Heston](../Mathematical%20Modeling%20of%20Derivative%20Pricing.md) in 1993, who introduced an intuitive  extension of the well known Black and Scholes model iz ation. He assumed that the spot price  follows the diffusion: that is, a process resembling [geometric Brownian motion](../../Financial%20Instruments/Black%20Scholes%20Derivation.md) with a nonconstant instantaneous variance  $\mathrm{v}$   (t). Furthermore, he proposed that the variance is a CIR process,  that is a mean reverting [stochastic process](../../The%20Ornstein-Uhlenbeck%20(OU)%20Process.md) of the form:
$$
d S_{t}=\big(r_{d}-r_{f}\big)S_{t}d t+\sqrt{V_{t}}\,S_{t}d W_{t}^{1}
$$
$$
d V_{t}=k(\theta-V_{t})d t+\sigma{\sqrt{V_{t}}}~d W_{t}^{2}
$$

And the two Brownian motions are correlated with each other:
$$
d\langle W_{1},W_{2}\rangle_{t}=\rho d t,
$$

1. Initial volatility:" V(0),  Not directly observable

2. Long term variance:  𝜽

 3. Speed of [mean reversion](../../The%20Ornstein-Uhlenbeck%20(OU)%20Process.md) of volatility:  $k$

 4. Volatility of volatility:  $\textdollar{\sigma}$

 5. Correlation between [spot exchange rate](../../Financial%20Instruments/Review%20Session%20Notes/Arbitrage%20Opportunity%20Accounting.md) and volatility:  $\textdollar{\rho}$

All these parameters can be calibrated.

We can interpret the parameters   $\textdollar{\sigma}$   and   $\textdollar{\rho}$   as being responsible for the skew, the volatility of  variance controlling the curvature and the correlation the tilt.

The other three parameters   $(V(\textdollar{\theta}),\textdollar{\theta},a n d\textdollar{k})$    control the [term structure](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%209/The%20Vasicek%20Model.md) of the model; where the mean  reversion controls the skewness of the curve from the short volatility level to the long volatility  level.

The [Heston model](../../Course%20Notes/Python/QuantLib-Python/Valuing%20European%20Option%20Using%20the%20Heston%20Model%20in%20QuantLib%20Python.md) is a generalization of the [Black-Scholes model](../../Financial%20Instruments/Black%20Scholes%20Derivation.md). Taking the limits   $\textdollar{\sigma}->\mathbf{0}$  ,  and   $k\Rightarrow\theta_{r}$  ,  we recover the [Black-Scholes PDE](../../Financial%20Instruments/Black%20Scholes%20Derivation.md) with constant volatility.

The volatility-of-volatility and [mean reversion](../../The%20Ornstein-Uhlenbeck%20(OU)%20Process.md) have opposite effect on the dispersion of volatility.  Volatility-of-volatility allows a large variation of future values of volatility; Mean-reversion  reversion tends to push future values of volatility towards the long-term value of volatility.
# Advantages:

The model intuitively extends the Black and Scholes model, including it as a special case. The  model is better used to price [derivatives](../../Financial%20Markets/Financial%20Trading%20and%20Markets/Chapter%209%20Arbitrage%20and%20Hedging%20With%20Options.md) whose underlying is the spot itself, as it directly models  St. [Heston](../Mathematical%20Modeling%20of%20Derivative%20Pricing.md)’s setting take into account non-lognormal distribution of the assets [returns](../../Financial%20Markets/Financial%20Asset%20Pricing%20Theory%20Overview/Chapter%203%20-%20%20Assets,%20Portfolios,%20and%20Arbitrage/Assets.md), [leverage](../../Advanced%20Investments/Lecture%206-Leverage,%20Tail%20Risk,%20Volatility%20Products.md)  effect, important mean-reverting property of volatility and it remains analytically tractable.

# Limitations:

Empirical evidence suggests that [Stochastic Volatility](../../Course%20Notes/Python/QuantLib-Python/Valuing%20European%20Option%20Using%20the%20Heston%20Model%20in%20QuantLib%20Python.md) model (SV) is able to capture the empirical  surface quite well in general. However as noted in many research papers the model does a rather  poor job fitting the smile at short maturities. See figure below.

The model has five parameters to calibrate. The volatility does not depend on the level of the spot,  which may a drawback when the model is used to price products sensitive with respect to the spot  of the underlying.

The dynamics of the calibrated [Heston Model](../../Course%20Notes/Python/QuantLib-Python/Valuing%20European%20Option%20Using%20the%20Heston%20Model%20in%20QuantLib%20Python.md) predict that:

-   Volatility can reach zero  -   Stay at zero for some time  -   Volatility is likely to stay extremely low or very high for long periods of time

Bloomberg have implemented [Heston model](../../Course%20Notes/Python/QuantLib-Python/Valuing%20European%20Option%20Using%20the%20Heston%20Model%20in%20QuantLib%20Python.md) for [pricing](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%207/Arbitrage%20Pricing%20of%20Derivatives.md) FX options and find similar weaknesses  mentioned above – the model’s inability to generate the smirks and the smiles for short options.  This is a characteristic for all [stochastic volatility](../../Course%20Notes/Python/QuantLib-Python/Valuing%20European%20Option%20Using%20the%20Heston%20Model%20in%20QuantLib%20Python.md) models.

Below we list the three main problems reported in the Bloomberg study:

   [Heston model](../../Course%20Notes/Python/QuantLib-Python/Valuing%20European%20Option%20Using%20the%20Heston%20Model%20in%20QuantLib%20Python.md) cannot fit a general [volatility surface](../7.%20Black%20Scholes%20Model.md), which may contain 20-30 data  points.        Over short horizons, the [Heston model](../../Course%20Notes/Python/QuantLib-Python/Valuing%20European%20Option%20Using%20the%20Heston%20Model%20in%20QuantLib%20Python.md) does not generate the amount of skew and  curvatures quoted in actual volatility surfaces. (  This short comings of [stochastic volatility](../../Course%20Notes/Python/QuantLib-Python/Valuing%20European%20Option%20Using%20the%20Heston%20Model%20in%20QuantLib%20Python.md)  models can be alleviated by adding jump component to the model )       The time dependency in implied vol at ili ties of ATM options is not in general of the form  of an exponential transition from short-term to long-term levels as prescribed by the form  of mean-reversion of the [Heston model](../../Course%20Notes/Python/QuantLib-Python/Valuing%20European%20Option%20Using%20the%20Heston%20Model%20in%20QuantLib%20Python.md) Parameter effects on the [implied volatility](../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%205%20Options%20on%20Prices%20and%20Hedge-Based%20Valuation/A%20Real-Life%20Option%20Pricing%20Exercise.md) smile  in the [Heston](../Mathematical%20Modeling%20of%20Derivative%20Pricing.md) SV model.
 ![500](Attachments/500-432.jpg)

Under the Bloomberg study, a set of [Heston model](../../Course%20Notes/Python/QuantLib-Python/Valuing%20European%20Option%20Using%20the%20Heston%20Model%20in%20QuantLib%20Python.md) parameters are calibrated using EUR/JPY,  EUR/USD, GBP/USD and USD/JPY and their volatility surfaces. The relative error of volatility  implied by the [Heston](../Mathematical%20Modeling%20of%20Derivative%20Pricing.md) option pricingi model and the input [implied volatility](../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%205%20Options%20on%20Prices%20and%20Hedge-Based%20Valuation/A%20Real-Life%20Option%20Pricing%20Exercise.md). The test is based on  ATM, 25 and 10-delta points with expiries of 1 week, 1 month, 6 month and 1 year.

 ![500](Attachments/500-422.jpg)
Errors are smaller for the 25-delta options but the error increases for 10-delta options. For 1  week and 1 month options, the fit is not very good as expected for the [Heston model](../../Course%20Notes/Python/QuantLib-Python/Valuing%20European%20Option%20Using%20the%20Heston%20Model%20in%20QuantLib%20Python.md). Errors are  around   $5.10\%$   for all delta values.
Below is a list of pros and cons of [stochastic volatility](../../Course%20Notes/Python/QuantLib-Python/Valuing%20European%20Option%20Using%20the%20Heston%20Model%20in%20QuantLib%20Python.md) models compiled by Peter Carr and Roger  Lee in their joint presentation; Robust Re plc i ation of [Volatility Derivatives](../Mathematics%20of%20the%20Financial%20Markets.md), April 2003, Stanford  University.

   All of the literature on [volatility derivatives](../Mathematics%20of%20the%20Financial%20Markets.md) employs some kind of [stochastic volatility](../../Course%20Notes/Python/QuantLib-Python/Valuing%20European%20Option%20Using%20the%20Heston%20Model%20in%20QuantLib%20Python.md)  (SV) model .     Furthermore, the models typically (but not always) assume that the price process and the  volatility process are both continuous over time.       To the extent that these assumptions are correct and that the particular process specification  is correct, one can use dynamic trading in one option and its underlying to hedge.       Most of the SV models used further assume that prices and instantaneous volatility both  diffuse leading to a simple and parsimonious world view. However, simple SV models  cannot simultaneously fit option prices at long and short maturities. Furthermore, since  instantaneous volatility is not directly observable, the assumption that the diffusion  coefficients of the volatility process are known is debatable.       Indeed, the SV diffusion parameters implied from time series typically differ from the riskneutral parameters, contradicting the implications of Girsanov’s theorem.       Complicating the [pricing](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%207/Arbitrage%20Pricing%20of%20Derivatives.md) and [hedging](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%205/Key%20Rates%20O1s%20Durations%20and%20Hedging.md) of [volatility derivatives](../Mathematics%20of%20the%20Financial%20Markets.md) is the ugly fact that prices  jump.       Furthermore, when prices jump by a large amount, it is widely believed that [expectations](../../Fixed%20Income%20Asset%20Pricing/Fixed%20Income%20Lecture%20Notes/FORWARD%20RATES%20AND%20TERM%20STRUCTURE.md)  of future realized volatility jump as well. The high levels of [mean reversion](../../The%20Ornstein-Uhlenbeck%20(OU)%20Process.md) and vol-of-vol  implied from option prices further suggests that volatility jumps.       When price and/or volatility can jump from one level to any other, then in a model with  two or more sources of uncertainty, perfect [replication](../../Financial%20Instruments/Financial%20Derivatives%20and%20Quantitative%20Methods/Forward%20and%20Futures%20Contracts.md) typically requires dynamic trading  in a [portfolio](../../Advanced%20Investments/An%20Asset%20Allocation%20Primer.md) of options.     While option bid/ask spreads typically render this strategy as prohibitively expensive at  the individual contract level, knowledge of desired option hedges can be enacted at the  aggregate [portfolio](../../Advanced%20Investments/An%20Asset%20Allocation%20Primer.md) level.     Can we use dynamic trading in a [portfolio](../../Advanced%20Investments/An%20Asset%20Allocation%20Primer.md) of options to develop a theory which does not  require a complete specification of the [stochastic process](../../The%20Ornstein-Uhlenbeck%20(OU)%20Process.md) for volatility?

# DE TERM IS TIC AND STOCHASTIC VOLATILITY MODELS: REULTS
First, the valuation and [hedging](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%205/Key%20Rates%20O1s%20Durations%20and%20Hedging.md) of [volatility swap](../Variance%20Swaps.md) as well as forward volatility agreements are  more complicated then [Variance swap](../Variance%20Swaps.md) contracts. The standard deviation is the square root of the  variance; but the square root is a non linear function. It is this linearity that makes the [replication](../../Financial%20Instruments/Financial%20Derivatives%20and%20Quantitative%20Methods/Forward%20and%20Futures%20Contracts.md)  and valuation of volatility based swaps more complex. Oliver Brockhaus and Douglas Long (Risk,  Jan. 2000), investigated the [pricing](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%207/Arbitrage%20Pricing%20of%20Derivatives.md) of [volatility derivatives](../Mathematics%20of%20the%20Financial%20Markets.md) and used both deterministic and  [stochastic volatility](../../Course%20Notes/Python/QuantLib-Python/Valuing%20European%20Option%20Using%20the%20Heston%20Model%20in%20QuantLib%20Python.md) based model.

According to the above authors, a comparison between a deterministic volatility model (DVM)  and [stochastic volatility](../../Course%20Notes/Python/QuantLib-Python/Valuing%20European%20Option%20Using%20the%20Heston%20Model%20in%20QuantLib%20Python.md) model (SVM) shows that the price of DVM is always higher. As can be  seen from the figure below, the price difference increases with decreasing absolute asset-volatility  correlation and increasing volatility of volatility.

A model-independent approach can be derived for [volatility swap](../Variance%20Swaps.md) using Taylor expansion of the  square root function around some value that is close to the expected [volatility swap](../Variance%20Swaps.md) value. So in  approximating volatility swaps only to   $1^{\mathrm{st}}$   order, we do not capture the effects of stochastic  volatility (volatility [convexity](../../Fixed%20Income%20Asset%20Pricing/Problem%20Sets/PSET%20II%20Fixed%20Income%20Asset%20Pricing%201.md)).

 ![500](Attachments/500-409.jpg)
 $I^{s t}$    and  $2^{n d}$    order approximation for the [volatility swap](../Variance%20Swaps.md).

 ![500](Attachments/500-416.jpg)
model dependency of [volatility swap](../Variance%20Swaps.md).

So, the   $1^{\mathrm{st}}$   and   $2^{\mathrm{nd}}$   order Taylor expansions provide two approximations that respectively  overestimate and underestimate the true value of the swap. Since [Forward volatility agreement](.md)  requires the square root of the variance, one can argue that we might expect similar results too.

# STOCHASTIC LOCAL VOLATILITY MODEL (SLV);

   Classical models such as  local volatility  (LV) and  [stochastic volatility](../../Course%20Notes/Python/QuantLib-Python/Valuing%20European%20Option%20Using%20the%20Heston%20Model%20in%20QuantLib%20Python.md)  (SV) are in fact calibrated to  and completely determined by the vanilla market

   They offer no extra flexibility in matching the market dynamics.
   In the [FX market](../../International%20Finance/Foreign%20Exchange%20Markets%20and%20Exchange%20Rate%20Determination.md),   [stochastic volatility](../../Course%20Notes/Python/QuantLib-Python/Valuing%20European%20Option%20Using%20the%20Heston%20Model%20in%20QuantLib%20Python.md)  (SV) behaves better than  local volatility  (LV) from a  dynamics point of view,       But  [Stochastic Volatility](../../Course%20Notes/Python/QuantLib-Python/Valuing%20European%20Option%20Using%20the%20Heston%20Model%20in%20QuantLib%20Python.md)  (SV) fails to calibrate to the vanillas prices       Mixing the two seems to be the answer and most market participants have moved in that  direction.

Because of the limitations of the Local and Stochastic models on their own, recently the market  practitioners have settled on using a model that combines both of the above models called  Stochastic Local Volatility model (SLV).

At the moment there is not much empirical tests on valuations of [volatility derivatives](../Mathematics%20of%20the%20Financial%20Markets.md) (products)  using this new approach, however, implementation and tests on barrier type exotics show:

-   [calibration](../../Credit%20Markets/Credit%20Markets%20Session%204.md) matches the entire [volatility surface](../7.%20Black%20Scholes%20Model.md) to the very distant wings  -   better model generated prices for reverse KO, Touches and Digital   -   consistent with market dynamics.

For valuation of FVA, it would require a model that has the above features. It will also require not  only better [calibration](../../Credit%20Markets/Credit%20Markets%20Session%204.md) but the calibrated [volatility surface](../7.%20Black%20Scholes%20Model.md) should have correct dynamics.

To test the SLV model, we would need to generate list of FVA prices for a given maturity using  various mixing fractions. We can then compare these prices with market quoted prices (provided  there are liquid OTC prices).   For more detailed discussion on the implementations and empirical  result on SLV model, see Tataru and Fisher, (2010).

# Bloomberg SLV Model

The SLV model that we investigate is described by:$$
\begin{array}{r l}&{\displaystyle\frac{d S_{t}}{S_{t}}=(\boldsymbol{r}_{d}-\boldsymbol{r}_{f})d t+L(S_{t},t)\sqrt{V_{t}}d W_{t}^{1}}\\ &{d V_{t}=k(\theta-V_{t})d t+\nu\nu o l\!\cdot\!V_{t}^{\alpha}d W_{t}^{2}}\\ &{d W_{t}^{1}\cdot d W_{t}^{2}=\rho~d t}\end{array}
$$
$L(S_{t},t)\ =$   = Local Volatility,   $\textdollar{K}=$    speed of [mean reversion](../../The%20Ornstein-Uhlenbeck%20(OU)%20Process.md),   $\Theta\!\!=$  [mean reversion](../../The%20Ornstein-Uhlenbeck%20(OU)%20Process.md) level,  Vvol    $=$  volatility of variance,  $\mathbf{P}=$  correlation.

The mixing of LV and SV features is controlled mostly by  vvol , followed as importance by the  correlation ρ. For SLV to degenerate to a pure LV model one would set   $\nu\nu o l{=}0$   and to obtain a  pure SV model one would set   $L(S_{t},t)\!=\!1$  =1.

# Calibration:

1.   Find the stochastic parameters to match the market dynamics  2.   And then calibrate the local vol. function   $L(S_{t},t)$   to match the vanilla market

 ![500](Attachments/500-423.jpg)
$\mathcal{\prime}_{\sf A}$   rigorous approach to finding the stochastic parameters rests on a quant if i cation of the market  dynamics. This can be represented by   ATM/  Spot and   $\hat{\sigma}$  RR/  Spot  or other ways to quantify the  movements of the [implied volatility surface](../../Course%20Notes/Python/QuantLib-Python/Modeling%20Volatility%20Smile%20and%20Heston%20Model%20Calibration%20Using%20QuantLib%20Python.md) given a move in spot.”

# References

Grigore Tataru, Travis Fisher, Quantitative Development Group, Bloomberg “Stochastic Local Volatility”  (February, 2010).
Patrick Hagan, Deep Kumar, Andrew S. Lesniewski and Diana E. Woodward. Managing smile risk.  Wilmott Magazine, pages 86-108, July 2002.    Steven L. [Heston](../Mathematical%20Modeling%20of%20Derivative%20Pricing.md). A closed-form solution for options with [stochastic volatility](../../Course%20Notes/Python/QuantLib-Python/Valuing%20European%20Option%20Using%20the%20Heston%20Model%20in%20QuantLib%20Python.md) with applications to bond  and [currency](../../Financial%20Instruments/Lecture%20Notes-%20Financial%20Instruments/Teaching%20Note%201-%20Forward%20Rates%20Agreement/Forwards%20and%20Futures%20Notes.md) options. Review of Financial Studies, 6(2):327{343, 1993.    Guanghua Lian. [Pricing](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%207/Arbitrage%20Pricing%20of%20Derivatives.md) [volatility derivatives](../Mathematics%20of%20the%20Financial%20Markets.md) with [stochastic volatility](../../Course%20Notes/Python/QuantLib-Python/Valuing%20European%20Option%20Using%20the%20Heston%20Model%20in%20QuantLib%20Python.md). PhD thesis, University  of Wollongong, 2010.    Iddo Yekutieli. Implementation of [Heston Model](../../Course%20Notes/Python/QuantLib-Python/Valuing%20European%20Option%20Using%20the%20Heston%20Model%20in%20QuantLib%20Python.md) for the [Pricing](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%207/Arbitrage%20Pricing%20of%20Derivatives.md) of GX Options. Bloomberg LP. Bloomberg  [Financial Markets](../../Financial%20Markets%20and%20Institutions/Financial%20Markets%20and%20Institutions%20Lecture%20Notes.md) (BFM), June 22 2004.     Collin Bennet, Miguel A.Gil.  “Volatility Trading – Trading volatility, correlation, [term structure](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%209/The%20Vasicek%20Model.md) and skew.  Equity [Derivatives](../../Financial%20Markets/Financial%20Trading%20and%20Markets/Chapter%209%20Arbitrage%20and%20Hedging%20With%20Options.md). Santander, Global [Banking](../../Advanced%20Financial%20Analysis%20and%20Valuation/Problem%20Sets/HKS%20The%20Banking%20Industry.md) and Markets.     Menachem Brenner, Ernest Y. Ou, Jin E Zhang. “ [Hedging](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%205/Key%20Rates%20O1s%20Durations%20and%20Hedging.md) Volatility Risk”. Journal of [Banking](../../Advanced%20Financial%20Analysis%20and%20Valuation/Problem%20Sets/HKS%20The%20Banking%20Industry.md) and Finance  30 (2006) 811 – 821    Carr, P., and L. Wu (2007). .Stochastic Skew in [Currency](../../Financial%20Instruments/Lecture%20Notes-%20Financial%20Instruments/Teaching%20Note%201-%20Forward%20Rates%20Agreement/Forwards%20and%20Futures%20Notes.md) Options,. Journal of Financial Economics, 86,

 213.247.

   Jiang, G.J., and Y.S. Tian (2005). .The Model-Free [Implied Volatility](../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%205%20Options%20on%20Prices%20and%20Hedge-Based%20Valuation/A%20Real-Life%20Option%20Pricing%20Exercise.md) and Its Information Content,. Review  of Financial Studies 18, 1305.1342.
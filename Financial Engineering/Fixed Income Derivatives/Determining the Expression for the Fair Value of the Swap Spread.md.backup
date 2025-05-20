---
tags:
  - debt_market
  - interest_rate_swap
  - libor_rate
  - repo_rate
  - swap_spread
aliases:
  - Interest Rate Swap Curve
  - Par Swap
  - Swap Curve
  - Swap Spread Fair Value
key_concepts:
  - Fair Value Swap Spread
  - Fixed and Floating Legs
  - Government Bond Yields
  - Interest Rate Swaps
  - Libor and Repo Rates
  - Swap Curve Benchmark
  - Swap Spread Definition
---

# Determining the Expression for the Fair Value of the Swap Spread

## Determining the Expression for the Fair Value of the Swap Spread: An Approach  Using Libor and GC Repo Rates
### Introduction  

Several studies have highlighted an environment of lower [liquidity](../../Financial%20Markets%20and%20Institutions/III.%20Liquidity%20of%20Assets/Class%205-%20Private%20Information,%20Liquidity,%20and%20Securitization/Class%20Note%2010%20Liquidity%20and%20Class%20Note%2010%20Liquidity%20and%20Liquidity%20Managementliquidity%20management.md) in government bond  markets, with yield levels falling below true risk-free rates.  Under these circumstances  capital market practitioners are increasingly using the [interest rate swap curve](.md) as their  main reference benchmark for valuation and analysis purposes. This reflects  practitioners’ views that continued exclusive reliance on government yields would  possibly lead to inaccurate analysis. The [interest rate swap curve](.md) is viewed as an  acceptable alternative measurement benchmark. It is also used as a comparator  instrument, against which the yields on government bonds can be measured. As the  [interest rate swap](../Primer%20on%20Interest%20Rate%20Swaps.md) market is considered to be sufficiently liquid and exposing users to  only a very low level of [default risk](../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%207%20-%20Default%20Risk%20and%20Credit%20Derivatives/Default%20Risk%20and%20Credit%20Derivatives%20183.md), the [swap curve](.md) is considered invariably to be  trading at a fair value to the theoretical zero-coupon yield curve. For this reason market  participants are concerned that the [swap curve](.md) is indeed fairly valued at all times, so that  swap spreads over the government curve can be taken to be a reasonable measure of the  [liquidity](../../Financial%20Markets%20and%20Institutions/III.%20Liquidity%20of%20Assets/Class%205-%20Private%20Information,%20Liquidity,%20and%20Securitization/Class%20Note%2010%20Liquidity%20and%20Class%20Note%2010%20Liquidity%20and%20Liquidity%20Managementliquidity%20management.md) and fair value of government bonds.  

In this article we provide an expression for the fair value for the swap spread, which is  shown to be a function of the Libor rate and the general collateral repo rate. This spread  can then be used as an alternative benchmark measure used to assess relative value for  all debt market instruments.  

# I  Interest rate swaps  

In setting fair value in the debt market, the only plausible alternative to the government  yield curve in the euro and sterling market is the [interest rate swap](../Primer%20on%20Interest%20Rate%20Swaps.md). A conventional  [interest rate swap](../Primer%20on%20Interest%20Rate%20Swaps.md) is an over-the-counter derivative contract between two parties in  which one party makes fixed interest payments, calculated on a notional amount, while  the other party makes floating-rate interest payments. The fixed rate is set at the  inception of the contract and the floating-rate is linked to an external reference such as  Libor during the life of the swap.  

The fixed-rate payer in a swap is conceptually long a floating-rate bond (FRN) and short  a fixed coupon bond, while the opposite is true for the floating-rate payer. When  calculating the fair value [swap rate](../../Fixed%20Income%20Asset%20Pricing/Fixed%20Income%20Lecture%20Notes/Teaching%20Note%204%20Interest%20Rate%20Derivatives.md) we use the concept of the  par  swap, which is a  vanilla swap of zero net present value. This means that the present value of the cash  
flows of the [fixed and floating legs](.md) of the swap are equal. The [fixed leg](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%202/Pricing%20Interest%20Rate%20Swaps.md) of the swap is  identical to the interest payments of a bond with fixed coupon equal to the [swap rate](../../Fixed%20Income%20Asset%20Pricing/Fixed%20Income%20Lecture%20Notes/Teaching%20Note%204%20Interest%20Rate%20Derivatives.md),  while the [floating leg](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%202/Pricing%20Interest%20Rate%20Swaps.md) is identical to the cash flows of an FRN with coupon set at the  Libor rate. At the start of the contract the FRN and the fixed bond must be equal to the  notional swap value. In a [par swap](.md) therefore the [fixed leg](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%202/Pricing%20Interest%20Rate%20Swaps.md) is conceptually similar to a  fixed coupon bond priced at par, with a coupon equal to the [swap rate](../../Fixed%20Income%20Asset%20Pricing/Fixed%20Income%20Lecture%20Notes/Teaching%20Note%204%20Interest%20Rate%20Derivatives.md). The [swap rate](../../Fixed%20Income%20Asset%20Pricing/Fixed%20Income%20Lecture%20Notes/Teaching%20Note%204%20Interest%20Rate%20Derivatives.md) in  a [par swap](.md) is therefore known as the  par yield .  

The observed difference between the [swap rate](../../Fixed%20Income%20Asset%20Pricing/Fixed%20Income%20Lecture%20Notes/Teaching%20Note%204%20Interest%20Rate%20Derivatives.md) and the government bond yield at any  point on the yield curve is known as the  swap spread . The swap spread is a measure of  interbank risk, given that the government curve is assumed to be default-free and the  swap market is used by banks and corporates to hedge their [interest rate risk](../../Fixed%20Income%20Asset%20Pricing/Analysis%20of%20Fixed%20Income%20Securities.md).  Traditionally the swap spread was taken to be the measure of corporate [default risk](../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%207%20-%20Default%20Risk%20and%20Credit%20Derivatives/Default%20Risk%20and%20Credit%20Derivatives%20183.md), with  a corporate bond asset-swap spread taken as an indicator of the [credit risk](../../Course%20Notes/Quantitative%20Trading%20Strategies%20Lecture%20Notes.md) on that  reference bond. However the swap market is now very large and liquid, and does not  suffer from il [liquidity](../../Financial%20Markets%20and%20Institutions/III.%20Liquidity%20of%20Assets/Class%205-%20Private%20Information,%20Liquidity,%20and%20Securitization/Class%20Note%2010%20Liquidity%20and%20Class%20Note%2010%20Liquidity%20and%20Liquidity%20Managementliquidity%20management.md) out to the long-dated maturities. There are also no supply  constraints in the swap market, unlike for (say) long-dated gilts or Treasuries, and the  use of collateral is ation, margining, netting and other measures has substantially reduced  counter party risk. Government bond markets on the other hand, have experienced low  [liquidity](../../Financial%20Markets%20and%20Institutions/III.%20Liquidity%20of%20Assets/Class%205-%20Private%20Information,%20Liquidity,%20and%20Securitization/Class%20Note%2010%20Liquidity%20and%20Class%20Note%2010%20Liquidity%20and%20Liquidity%20Managementliquidity%20management.md) and supply constraints leading to inverted curves, leading some commentators  to suggest that the government yields have traded below the true risk-free level; see  Fleming (2000, 2001). In other words, the government curve may on occasion be  overvalued, whereas the [swap curve](.md) is now almost invariably at fair value.  

The assumption that the [swap curve](.md) is always at fair value, whereas the government  curve at times may not be, is open to some debate. This is not least because the swap  curve is a function of market makers bid-offer swap rates, and in the event of a  significant shock or market correction the book position and supply of certain prices will  influence the [swap curve](.md), affecting its use as a benchmark.  However if we make this  assumption, we are then in a position to make an assessment of the swap spread and, by  taking its fair value, of the government curve fair value as well. Assuming that the swap  rate is at fair value, we can use the extent of the swap spread itself to determine if the  government curve is at fair value; if the swap spread differs from that suggested by the  [swap rate](../../Fixed%20Income%20Asset%20Pricing/Fixed%20Income%20Lecture%20Notes/Teaching%20Note%204%20Interest%20Rate%20Derivatives.md) fair value, this indicates a government curve that is overvalued.  

In the next section we consider the expression for the fair value for the swap spread.  

# II  Swap spread fair value  

We now consider the calculation of the fair value for the swap spread. This is done using  a zero-cost [portfolio](../../Advanced%20Investments/An%20Asset%20Allocation%20Primer.md) trading approach, consisting of the benchmark government bond  (paying fixed coupon on a semi-annual basis), the six-month government repo rate and  the six-month Libor rate. We ignore bid-offer spreads.  
A market participant enters into the following trades simultaneously:  

•  a [short sale](../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%202%20-%20Spot%20Markets/Short%20Selling.md) of   $\epsilon\,x$   million of the benchmark   $[]$  -year semi-annual paying government  bond, which is priced at par and therefore trading at the par yield of   $r m\%$  ; the bond is  available in the repo market at the general collateral (GC) rate; 
 •  a six-month reverse repo, using the cash proceeds from the bond sale; this pays out  the six-month GC repo rate  $r g\%$  ; 
 •  a  $\epsilon\,x$   million   $[],$  -year pay floating / receive fixed interest-rate swap, where the trader  receives six-month Libor or  $r l$   and pays at the [swap rate](../../Fixed%20Income%20Asset%20Pricing/Fixed%20Income%20Lecture%20Notes/Teaching%20Note%204%20Interest%20Rate%20Derivatives.md)  $r s\%$  .  

This sets up a  zero-cost [portfolio](../../Advanced%20Investments/An%20Asset%20Allocation%20Primer.md), which comprises the following cash flows:  

•  pay out of  rm  every six months; 
 •  receipt of  rg  every six months; 
 •  pay out of  rs  every six months; 
 •  receipt of   $r l$   every six months.  

The net [cash flow](../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%201%20-%20Purpose%20and%20Structure%20of%20Financial%20Markets/Preview%20of%20the%20Book.md) of the combined [portfolio](../../Advanced%20Investments/An%20Asset%20Allocation%20Primer.md) during the time it is held is given by  
$$
P o r t=n o m\times\left[\left(\frac{r s-r m}{2}\right)-\left(\frac{r l-r g}{2}\right)\right]
$$  

where  nom  is the notional value equal to  $\epsilon\,x$   million.  

It can be shown that the present value of the [portfolio](../../Advanced%20Investments/An%20Asset%20Allocation%20Primer.md) cash flows during its life is given  by  
$$
P V=\sum_{i=1}^{n}{\frac{{\frac{x}{2}}{\big(}r s-r m{\big)}}{\left(1\!+\!{\frac{r z_{i}}{2}}\right)^{i}}}-E_{0}{\sum_{i=1}^{n}{\frac{{\frac{x}{2}}{\big(}r l_{i}-r g_{i}{\big)}}{\left(1\!+\!{\frac{s_{i}}{2}}\right)^{i}}}}
$$  

where  $n$   is the maturity (in years) of the bond and swap and  $x$   is the nominal value as  before. The term  $r z_{i}$   is the theoretical  $i$  -year risk-free [spot rate](../../International%20Finance/The%20Foreign%20Exchange%20Market%20Annotations.md) interest rate.  

The first term in the expression is the present value of the cash flows of the bond and the  [fixed leg](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%202/Pricing%20Interest%20Rate%20Swaps.md) of the swap. The second term is the present value of the  expected  difference  between the floating rate of the swap and the repo rate. These are not known with  certainty, as they will be set by the Libor fixing every six months and the repo rate as  
this is rolled over at the same time and for the same term. As these cash flows cannot be  determined at the inception of the trade, they are discounted at the rate of  $s_{i},$   which is the  [spot rate](../../International%20Finance/The%20Foreign%20Exchange%20Market%20Annotations.md)   $r z_{i}$   plus an additional element  $t$  , where   $t$   represents the risk factor arising from  the change in the spread  $r l-r g$  . The additional amount   $t$   is user-determined. So we have  
$$
s_{i}=r z_{i}+t\,.
$$  

We assume that the [swap rate curve](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%205/Partial%20O1s%20and%20PV01.md) and the benchmark government bond are fairly  valued. This being so, the expression at (2) must be equal to zero, because the [portfolio](../../Advanced%20Investments/An%20Asset%20Allocation%20Primer.md)  set up by the trader is a zero-cost transaction. This enables us to set  
$$
\sum_{i=1}^{n}{\frac{{\frac{x}{2}}{\big(}r s-r m{\big)}}{\left(1\!+\!{\frac{r z_{i}}{2}}\right)^{i}}}\!=\!E_{0}\!\sum_{i=1}^{n}\!{\frac{{\frac{x}{2}}{\big(}r l_{i}-r g_{i}{\big)}}{\left(1\!+\!{\frac{s_{i}}{2}}\right)^{i}}}.
$$  

We can now set the swap spread in terms of the expected spread between the Libor and  GC [repo rates](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%2011/Implied%20Repo%20Rates.md). This is done by re-arranging (4) and moving   $(r s-r m)$   outside the  summation, shown as  
$$
r s-r m=\frac{E_{0}\displaystyle\sum_{i=1}^{n}\left[\bigl(r l_{i}-r g_{i}\bigr)/\left(1\!+\!\frac{s_{i}}{2}\right)^{i}\right]}{\displaystyle\sum_{i=1}^{n}\left[1/\left(1\!+\!\frac{r z_{i}}{2}\right)^{i}\right]}.
$$  

That is, the fair value of the swap spread is given by the expected spread between the  Libor rate and the repo rate. By setting a risk factor for this spread  $t$   as zero, the fair  value of the swap spread is given by the weighted average of future [expectations](../../Fixed%20Income%20Asset%20Pricing/Fixed%20Income%20Lecture%20Notes/FORWARD%20RATES%20AND%20TERM%20STRUCTURE.md) of the  spread during the term of the swap.  

# III  Conclusion  

We have shown that, under certain assumptions of the [swap rate](../../Fixed%20Income%20Asset%20Pricing/Fixed%20Income%20Lecture%20Notes/Teaching%20Note%204%20Interest%20Rate%20Derivatives.md) and the future spread of  the six-month Libor rate and six-month repo rate, the fair value of the swap spread is  given by the expectation of this spread. The spread was given as (5) above.  

Market practitioners must set the level of the risk premium factor. Under “normal”  market conditions as we move to a market correction or market shock the swap spread  will widen. Therefore as the [swap rate](../../Fixed%20Income%20Asset%20Pricing/Fixed%20Income%20Lecture%20Notes/Teaching%20Note%204%20Interest%20Rate%20Derivatives.md) must be higher when markets are experiencing  downside movement, the risk premium will be negative. This gives a higher swap spread  at time of market downside correction.  
On the basis we have discussed, the swap spread may be used as an alternative   benchmark measure used to assess relative value for all debt market instruments. That is,  by determining where the market-observed swap spread is relative to that suggested by  the fair value swap spread, we can observe the actual over-valuation of benchmark  government bonds as captured by the government yield curve.  

# References  

Fleming, M., “The benchmark US treasury market: recent performance and possible  alternatives”,  Federal Reserve Bank of New York: Economic Policy Review , vol , no 1,  April 2000  

----------, “Financial market implications of the federal debt paydown”,  Federal Reserve  Bank of New York: Staff Report , no 120, May 2001  Jeanneau, S., Scott, R., “Anatomy of a squeeze”,  BIS Quarterly Review,  June 2001 pp  32-33  McCauley, R., Remonola, E., “Size and [liquidity](../../Financial%20Markets%20and%20Institutions/III.%20Liquidity%20of%20Assets/Class%205-%20Private%20Information,%20Liquidity,%20and%20Securitization/Class%20Note%2010%20Liquidity%20and%20Class%20Note%2010%20Liquidity%20and%20Liquidity%20Managementliquidity%20management.md) of government bond markets ”, BIS  Quarterly Review , November 2000 pp 52-58  Schinasi, G., Kramer, C., Todd Smith, R., “Financial implications of the shrinking  supply of US [Treasury securities](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Front%20Matter/US%20Markets.md)”, International Monetary Fund, 20 March 2001  
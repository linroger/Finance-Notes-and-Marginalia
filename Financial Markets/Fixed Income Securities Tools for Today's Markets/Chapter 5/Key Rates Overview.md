---
tags:
  - bond_portfolio
  - duration
  - interest_rate_risk
  - key_rates
  - term_structure
aliases:
  - Bloomberg Index
  - JPM Fund
  - Key Rate Overview
key_concepts:
  - Bond portfolio risks
  - Interest rate risk
  - Key rate durations
  - Term structure changes
  - Total duration
---

# 5.2 KEY RATES: OVERVIEW  

Key-rate $^{\bullet}O1s$ or key-rate Dvo1s, along with key-rate durations, are designed: i) to describe how the risks of a bond [portfolio](../../../Advanced%20Investments/An%20Asset%20Allocation%20Primer.md) are distributed along the [term structure](../Chapter%209/The%20Vasicek%20Model.md), and ii) to hedge those risks using some set of. bonds, usually the most liquid government bonds of various maturities.. To introduce the topic, Table 5.1 shows the key-rate durations for the. [JPMorgan](../../../Financial%20Engineering/Basis%20Trade%20Explainer.md) Government Bond Fund and its benchmark [portfolio](../../../Advanced%20Investments/An%20Asset%20Allocation%20Primer.md), the. Bloomberg-Barclays US Government Bond Index, as of May 31, 2021. The "Total" durations, in the last row of the table, have similar interpretations as the yield-based durations of Chapter 4. The [JPM fund](.md)'s [total duration](.md) of 5.73 means that its value increases by approximately $5.73\%$ for a parallel decline in par rates of 100 basis points. The [JPM fund](.md), therefore,. has less [duration](Key%20Rates%20O1s%20Durations%20and%20Hedging.md) risk than its benchmark, which has a [duration](Key%20Rates%20O1s%20Durations%20and%20Hedging.md) of 6.78. The other rows of the table give the key-rate durations of these two bond portfolios. From the "5yr" row, for example, the [JPM fund](.md) increases in value by approximately $0.80\%$ when the five-year [par rate](../Chapter%202/Pricing%20Interest%20Rate%20Swaps.md) declines by 100 basis points, but all other par rates remain unchanged. Similarly, from the 20-year row, the benchmark [portfolio](../../../Advanced%20Investments/An%20Asset%20Allocation%20Primer.md) increases in value by approximately $1.67\%$ when the 20-year [par rate](../Chapter%202/Pricing%20Interest%20Rate%20Swaps.md) declines by 100 basis points, but all other par rates remain unchanged.  

The key-rate [duration](Key%20Rates%20O1s%20Durations%20and%20Hedging.md) profile of a [portfolio](../../../Advanced%20Investments/An%20Asset%20Allocation%20Primer.md), therefore, decomposes its. [total duration](.md), that is, its sensitivity to parallel shifts in par rates, into sepa-. rate durations or sensitivities to changes in individual par rates. Consistent with key-rate durations as a decomposition of [total duration](.md), the sum of all key-rate durations of a [portfolio](../../../Advanced%20Investments/An%20Asset%20Allocation%20Primer.md) is equal or very nearly equal to the [total duration](.md) of the [portfolio](../../../Advanced%20Investments/An%20Asset%20Allocation%20Primer.md).  

TABLE 5.1  Key-Rate Durations of [JPMorgan](../../../Financial%20Engineering/Basis%20Trade%20Explainer.md) Government Bond Fund and Its Benchmark [Portfolio](../../../Advanced%20Investments/An%20Asset%20Allocation%20Primer.md), the Bloomberg-Barclays US Government Bond Index, as of May 31, 2021.   


<html><body><table><tr><td></td><td>JPM Government</td><td>Bloomberg-Barclays Government Bond Index</td></tr><tr><td>[Key Rate](Key%20Rates%20O1s%20Durations%20and%20Hedging.md)</td><td>Bond Fund</td><td></td></tr><tr><td>6mo</td><td>0.03</td><td></td></tr><tr><td>1yr</td><td>0.11</td><td>0.11</td></tr><tr><td>2yr</td><td>0.19</td><td>0.34</td></tr><tr><td>3yr</td><td>0.40</td><td>0.60</td></tr><tr><td>5yr</td><td>0.80</td><td>0.88</td></tr><tr><td>7yr</td><td>1.19</td><td>0.86</td></tr><tr><td>10yr</td><td>1.31</td><td>0.57</td></tr><tr><td>20yr</td><td>1.05</td><td>1.67</td></tr><tr><td>30yr Total</td><td>0.65</td><td>1.75</td></tr></table></body></html>  

The key-rate [duration](Key%20Rates%20O1s%20Durations%20and%20Hedging.md) profiles in the table say a lot about the exposures. of the two portfolios to par rates of different terms. The [interest rate risk](../../../Fixed%20Income%20Asset%20Pricing/Analysis%20of%20Fixed%20Income%20Securities.md) of. the [JPM fund](.md) is somewhat concentrated in seven- to 20-year par rates, while the risk of the index is concentrated in five- to seven-year and, even more so, in 20- to 30-year rates. Part of the reason for the relative differences in these exposures is that the [JPM fund](.md) invests in US agency mortgage-backed. securities, which are particularly sensitive to seven- to 10-year rates, while the benchmark index contains only government bonds. In any case, as a. result of these key-rate [duration](Key%20Rates%20O1s%20Durations%20and%20Hedging.md) differences, the two portfolios will perform. differently as the shape of the [term structure](../Chapter%209/The%20Vasicek%20Model.md) fluctuates..  

The [JPM fund](.md) reports exposures to the nine key rates listed in Table 5.1.. The index fund reports only eight key rates, leaving out the six-month rate.. The number of key rates chosen involves a trade-off, along the lines of the. [introduction](../../../Financial%20Markets%20and%20Institutions/III.%20Liquidity%20of%20Assets/Class%209-%20Bailouts%20and%20Bank%20Failures/Squam%20Lake%20Group%20Introduction.md). With too few key rates, the [term structure](../Chapter%209/The%20Vasicek%20Model.md) is likely to move in a way not captured by the framework. With too many, [risk management](../../../Financial%20Engineering/Financial%20Mathematics%20Course.md) becomes cumbersome and costly.  

Along with the number of key rates, the terms of the key rates need be chosen. Because key-rate Dv01s and durations are designed to be hedged with a relatively small set of liquid bonds, the most popular choices for key rates are those that correspond to the maturities of [on-the-run Treasuries](../../../Credit%20Markets/Credit%20Market%20PSETS/Credit%20Market%20Homework%201.md). Including the Treasury's regular issuance of six-month and one-year bills, along with its regular issuance of two-, three-, five-, seven-, 10-, 20-, and 30-year bonds, the JPM and index funds in Table 5.1 have clearly made this popular choice.  
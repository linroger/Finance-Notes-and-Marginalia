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

Key-rate $^{\bullet}O1s$ or key-rate Dvo1s, along with key-rate durations, are designed: i) to describe how the risks of a bond [[An Asset Allocation Primer|portfolio]] are distributed along the [[The Vasicek Model|term structure]], and ii) to hedge those risks using some set of. bonds, usually the most liquid government bonds of various maturities.. To introduce the topic, Table 5.1 shows the key-rate durations for the. [[Basis Trade Explainer|JPMorgan]] Government Bond Fund and its benchmark [[An Asset Allocation Primer|portfolio]], the. Bloomberg-Barclays US Government Bond Index, as of May 31, 2021. The "Total" durations, in the last row of the table, have similar interpretations as the yield-based durations of Chapter 4. The [[Key Rates Overview|JPM fund]]'s [[Key Rates Overview|total duration]] of 5.73 means that its value increases by approximately $5.73\%$ for a parallel decline in par rates of 100 basis points. The [[Key Rates Overview|JPM fund]], therefore,. has less [[Key Rates O1s Durations and Hedging|duration]] risk than its benchmark, which has a [[Key Rates O1s Durations and Hedging|duration]] of 6.78. The other rows of the table give the key-rate durations of these two bond portfolios. From the "5yr" row, for example, the [[Key Rates Overview|JPM fund]] increases in value by approximately $0.80\%$ when the five-year [[Pricing Interest Rate Swaps|par rate]] declines by 100 basis points, but all other par rates remain unchanged. Similarly, from the 20-year row, the benchmark [[An Asset Allocation Primer|portfolio]] increases in value by approximately $1.67\%$ when the 20-year [[Pricing Interest Rate Swaps|par rate]] declines by 100 basis points, but all other par rates remain unchanged.  

The key-rate [[Key Rates O1s Durations and Hedging|duration]] profile of a [[An Asset Allocation Primer|portfolio]], therefore, decomposes its. [[Key Rates Overview|total duration]], that is, its sensitivity to parallel shifts in par rates, into sepa-. rate durations or sensitivities to changes in individual par rates. Consistent with key-rate durations as a decomposition of [[Key Rates Overview|total duration]], the sum of all key-rate durations of a [[An Asset Allocation Primer|portfolio]] is equal or very nearly equal to the [[Key Rates Overview|total duration]] of the [[An Asset Allocation Primer|portfolio]].  

TABLE 5.1  Key-Rate Durations of [[Basis Trade Explainer|JPMorgan]] Government Bond Fund and Its Benchmark [[An Asset Allocation Primer|Portfolio]], the Bloomberg-Barclays US Government Bond Index, as of May 31, 2021.   


<html><body><table><tr><td></td><td>JPM Government</td><td>Bloomberg-Barclays Government Bond Index</td></tr><tr><td>[[Key Rates O1s Durations and Hedging|Key Rate]]</td><td>Bond Fund</td><td></td></tr><tr><td>6mo</td><td>0.03</td><td></td></tr><tr><td>1yr</td><td>0.11</td><td>0.11</td></tr><tr><td>2yr</td><td>0.19</td><td>0.34</td></tr><tr><td>3yr</td><td>0.40</td><td>0.60</td></tr><tr><td>5yr</td><td>0.80</td><td>0.88</td></tr><tr><td>7yr</td><td>1.19</td><td>0.86</td></tr><tr><td>10yr</td><td>1.31</td><td>0.57</td></tr><tr><td>20yr</td><td>1.05</td><td>1.67</td></tr><tr><td>30yr Total</td><td>0.65</td><td>1.75</td></tr></table></body></html>  

The key-rate [[Key Rates O1s Durations and Hedging|duration]] profiles in the table say a lot about the exposures. of the two portfolios to par rates of different terms. The [[Analysis of Fixed Income Securities|interest rate risk]] of. the [[Key Rates Overview|JPM fund]] is somewhat concentrated in seven- to 20-year par rates, while the risk of the index is concentrated in five- to seven-year and, even more so, in 20- to 30-year rates. Part of the reason for the relative differences in these exposures is that the [[Key Rates Overview|JPM fund]] invests in US agency mortgage-backed. securities, which are particularly sensitive to seven- to 10-year rates, while the benchmark index contains only government bonds. In any case, as a. result of these key-rate [[Key Rates O1s Durations and Hedging|duration]] differences, the two portfolios will perform. differently as the shape of the [[The Vasicek Model|term structure]] fluctuates..  

The [[Key Rates Overview|JPM fund]] reports exposures to the nine key rates listed in Table 5.1.. The index fund reports only eight key rates, leaving out the six-month rate.. The number of key rates chosen involves a trade-off, along the lines of the. [[Squam Lake Group Introduction|introduction]]. With too few key rates, the [[The Vasicek Model|term structure]] is likely to move in a way not captured by the framework. With too many, [[Financial Mathematics Course|risk management]] becomes cumbersome and costly.  

Along with the number of key rates, the terms of the key rates need be chosen. Because key-rate Dv01s and durations are designed to be hedged with a relatively small set of liquid bonds, the most popular choices for key rates are those that correspond to the maturities of [[Credit Market Homework 1|on-the-run Treasuries]]. Including the Treasury's regular issuance of six-month and one-year bills, along with its regular issuance of two-, three-, five-, seven-, 10-, 20-, and 30-year bonds, the JPM and index funds in Table 5.1 have clearly made this popular choice.  
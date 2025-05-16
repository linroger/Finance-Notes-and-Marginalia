---
tags:
  - corporate_bonds
  - credit_portfolios
  - dvo1
  - spread_duration
  - spread_risk
aliases:
  - DTS
  - Duration times spread
key_concepts:
  - benchmark curve
  - bond price sensitivity
  - hazard rate model
  - risky Dv01
  - spread Dv01
  - spread duration
---

# 14.10 SPREAD DURATION AND DVO1  

When trading or investing in credit portfolios, it is natural to measure the sensitivity of bond prices to changes in credit spreads. The standard measures, [spread duration](.md) and spread Dv01, shift the spread, keeping the bench-. mark curve and cash flows the same, calculate a new price, and then calculate a [duration](../Chapter%205/Key%20Rates%20O1s%20Durations%20and%20Hedging.md) or Dv01. Because rates used for discounting in this context are the sum of the benchmark rates and spreads, shifting the benchmark rate. by one basis point results in the same [price sensitivity](../Chapter%204/Duration.md) as shifting the spread by one basis point, that is, spread durations and Dv01s are the same as durations and DV01s with respect to [interest rate changes](../../../International%20Finance/Bridgewater/How%20Countries%20Go%20Broke/How%20Countries%20Go%20Broke-Chapter%2012%20to%20Chapter%2014.md). These spread sensitivities can still be useful, however, in a [portfolio](../../../Advanced%20Investments/An%20Asset%20Allocation%20Primer.md) context. In a [portfolio](../../../Advanced%20Investments/An%20Asset%20Allocation%20Primer.md) of government bonds, [interest rates](../Chapter%202/Interest%20Rate%20Quotations.md) swaps, and corporate bonds, for example, spread DV01 with respect to swap spreads can be found by shifting spreads for swaps and corporate bonds only, while spread Dv01 with respect to corporate spreads can be found by shifting spreads for corporate. bonds only.  

It is very common in the corporate bond setting to measure spread risk with [duration times spread](.md), or DTS, instead of [spread duration](.md). This methodology is based on the empirical regularity that changes in the spread of a corporate bond are proportional to the spread itself. Consider, for example, bonds A and B, which have spread durations of five and four years, and which trade at spreads of 100 and 250 basis points, respectively. Under the usual [duration](../Chapter%205/Key%20Rates%20O1s%20Durations%20and%20Hedging.md) assumptions of parallel shifts, bond B has spread risk of $4/5$ or $80\%$ of that of bond A. But empirical evidence suggests that if the spread of bond A increases by $10\%$ , that is, 10 basis points from 100 to 110, then the spread of bond B also increases by $10\%$ that is, 25 basis points from 250 to 275. In this case, after these spread changes, by the definition of [duration](../Chapter%205/Key%20Rates%20O1s%20Durations%20and%20Hedging.md), the percentage change of bond A is $5\times10/100=0.5$ , and the percentage change of bond B is $4\times25/100=1$ Hence, bond B is actually twice as risky as bond A. This is reflected in their DTS: $5\times100=500$ for bond A, and $4\times250=1,000$ for bond B.  

[Price sensitivity](../Chapter%204/Duration.md) to spreads can also be computed using the hazard-rate. model described in this chapter. Risky Dv01 refers to the change in the value of a CDS contract for a one-basis-point change in the [CDS spread](Cds-Equivalent%20Bond%20Spread.md). This can. be computed, of course, by finding the hazard rate that changes the [CDS spread](Cds-Equivalent%20Bond%20Spread.md) by one basis point, recomputing the value of the CDS, and calculating. the risky DV01. An equivalent bond metric can be computed similarly: find the hazard rate that changes the CDS-equivalent bond spread by one basis point, recompute its price, and calculate a Dv01..  
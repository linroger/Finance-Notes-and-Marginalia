---
tags:
  - benchmark_rates
  - credit_risk
  - credit_spreads
  - default_timing
  - hazard_adjusted_duration
aliases:
  - Duration
  - Dv01
  - HAD
key_concepts:
  - Benchmark rate curve
  - Conventional vs hazard-adjusted
  - Credit spreads and durations
  - Expected cash flow timing
  - Hazard-adjusted duration (HAD)
---

# 14.9 HAZARD-ADJUSTED DURATION AND DVO1  

The durations of bonds with [[Quantitative Trading Strategies Lecture Notes|credit risk]] are often calculated along the lines of Chapter 4, that is, cash flows are assumed to be paid on schedule, but are discounted at higher rates, typically at benchmark rates plus a [[Cds-Equivalent Bond Spread|credit spread]] or a [[The Vasicek Model|term structure]] of credit spreads. Calculated this way, however, [[Key Rates O1s Durations and Hedging|duration]] can be misleading for bonds with significant [[Quantitative Trading Strategies Lecture Notes|credit risk]]. For these bonds, [[Week 6 Assignment Review|expected cash flows]] are much earlier than scheduled cash flows and, consequently, their durations are correspondingly shorter.  

The simple hazard-rate framework presented earlier can be used to cal-. culate a hazard-adjusted [[Key Rates O1s Durations and Hedging|duration]] (HAD) that accounts for the expected timing of cash flows given default. Along the lines of Table 14.11, given a. [[Hazard-Adjusted Duration and Dvo1|benchmark rate curve]] and a [[Credit Markets Session 3|recovery rate]], find the hazard rate for which the expected discounted value of the bond's cash flows equals its market price.. Then, shift the [[Hazard-Adjusted Duration and Dvo1|benchmark rate curve]] down and reprice the bond, using the same recovery and [[RISK NEUTRAL VALUATION FRAMEWORK FOR CREDIT DEFAULT SWAPS|hazard rates]]. Finally, use the resulting price difference or percentage price difference to compute the hazard-adjusted Dv01 or [[Key Rates O1s Durations and Hedging|duration]], respectively.  

To illustrate the difference between the conventional and hazard-adjusted approaches, Figure 14.7 graphs conventional and hazard-adjusted durations for bonds of various terms at two different [[RISK NEUTRAL VALUATION FRAMEWORK FOR CREDIT DEFAULT SWAPS|hazard rates]]. The [[Hazard-Adjusted Duration and Dvo1|benchmark rate curve]] is flat at $2\%$ , and the [[Credit Markets Session 3|recovery rate]] is fixed at $40\%$ . The hazard rate is either $5\%$ or $10\%$ , which, given the $40\%$ [[Credit Markets Session 3|recovery rate]], corresponds approximately to CDS spreads of 300 and 600 basis points, respectively. All bonds are priced using the constant hazard-rate model, and HADs are computed as described in the previous paragraph. Conventional durations are calculated by finding the fixed spread to the [[Spread Duration and Dvo1|benchmark curve]] that correctly prices each bond, and then shifting the [[Spread Duration and Dvo1|benchmark curve]] and repricing each bond, keeping its spread constant.  

![](d40b785c13f8665da02889fa30a3427338230fe66da621a7cb389e99fb06b23e.jpg)  
FIGURE 14.7 Conventional $V s$ . Hazard-Adjusted Durations.  

Bonds with a higher hazard rate have higher spreads and, therefore,. lower durations than bonds with a lower hazard rate. The striking message. of Figure 14.7, however, is that HADs can be significantly below conventional durations, particularly for larger [[RISK NEUTRAL VALUATION FRAMEWORK FOR CREDIT DEFAULT SWAPS|hazard rates]] and longer terms. For 10-year bonds at a hazard rate of. $5\%$ , the conventional [[Key Rates O1s Durations and Hedging|duration]] is 7.7 and. the HAD is 7.3, while at a hazard rate of $10\%$ , the durations are 7.3 con-. ventional and 6.4 HAD. For 30-year bonds at a hazard rate of $5\%$ , the conventional [[Key Rates O1s Durations and Hedging|duration]] is 15.3 and the HAD is 12.8, while at a hazard rate of $10\%$ , the durations are 13.2 conventional and 8.7 HAD..  
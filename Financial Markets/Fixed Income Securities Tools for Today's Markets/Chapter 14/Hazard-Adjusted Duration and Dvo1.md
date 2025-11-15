---
aliases:
- Duration
- Dv01
- HAD
- Bond pricing and yield curves
- Duration and convexity hedging
- Credit spreads and bond valuation
- Fixed income securities and markets
- Bond valuation and yield calculation
- Credit analysis and spread decomposition
- Credit default swap mechanics
- CDS-Bond basis and relative value
- Credit risk and default modeling
- Market liquidity and measurement
- Bid-ask spreads and transaction costs
- Market impact and execution
- Option pricing theory and Black-Scholes model
- Options Greeks and risk management
- Call and put option strategies
- Hazard-Adjusted Duration and Dvo1 and financial analysis
- Hazard-Adjusted Duration and Dvo1 in modern finance
- Applications of Hazard-Adjusted Duration and Dvo1
- 'Case study: Hazard-Adjusted Duration and Dvo1'
last_enhanced: '2025-11-06 08:42:35'
- options
- credit-risk
- call
- default
- fixed-income
- put
- recovery
- liquidity
- bond
- credit-spread
- bonds
- spread
- dv01
- duration
- cds
tags:
- basis
- bid-ask
- bond
- case-study
- credit-curve
- credit-market
- crisis-analysis
- default
- derivative-pricing
- derivatives
- duration
- empirical-analysis
- fixed-income
- graduate-level
- hedging
- institutional-quality
- learning-from-crisis
- liquidity
- mathematical-finance
- professional-standard
- provision
- quantitative-methods
- real-world-example
- sec-regulation
- securitization
- spread
- yield-curve

key_concepts:
- Banking and Financial Intermediation
- Case Study Methodology
- Crisis Case Study Design
- Empirical Analysis of Financial Events
- Empirical Finance Research
- Financial Crisis Case Studies
- Financial Markets and Banking
- Financial Markets and Institutions
- Historical Financial Analysis
- Institutional-Quality Financial Education
- Learning from Financial Crises
- Quantitative Methods in Finance
- Real-World Financial Examples
- Risk Management and Hedging Strategies
- Risk Management in Finance

enhanced: true
enhancement_date: 2025-11-06
enhancement_id: batch06-af

type: note
created: 2025-11-06
modified: 2025-11-06
status: active
academic_level: graduate
professional_application: industry-standard
---







# 14.9 HAZARD-ADJUSTED DURATION AND DVO1  

The durations of bonds with credit risk are often calculated along the lines of Chapter 4, that is, cash flows are assumed to be paid on schedule, but are discounted at higher rates, typically at benchmark rates plus a credit spread or a term structure of credit spreads. Calculated this way, however, duration can be misleading for bonds with significant credit risk. For these bonds, expected cash flows are much earlier than scheduled cash flows and, consequently, their durations are correspondingly shorter.  

The simple hazard-rate framework presented earlier can be used to cal-. culate a hazard-adjusted duration (HAD) that accounts for the expected timing of cash flows given default. Along the lines of Table 14.11, given a. benchmark rate curve and a recovery rate, find the hazard rate for which the expected discounted value of the bond's cash flows equals its market price.. Then, shift the benchmark rate curve down and reprice the bond, using the same recovery and hazard rates. Finally, use the resulting price difference or percentage price difference to compute the hazard-adjusted Dv01 or duration, respectively.  

To illustrate the difference between the conventional and hazard-adjusted approaches, Figure 14.7 graphs conventional and hazard-adjusted durations for bonds of various terms at two different hazard rates. The benchmark rate curve is flat at $2\%$ , and the recovery rate is fixed at $40\%$ . The hazard rate is either $5\%$ or $10\%$ , which, given the $40\%$ recovery rate, corresponds approximately to CDS spreads of 300 and 600 basis points, respectively. All bonds are priced using the constant hazard-rate model, and HADs are computed as described in the previous paragraph. Conventional durations are calculated by finding the fixed spread to the benchmark curve that correctly prices each bond, and then shifting the benchmark curve and repricing each bond, keeping its spread constant.  

![](d40b785c13f8665da02889fa30a3427338230fe66da621a7cb389e99fb06b23e.jpg)  
FIGURE 14.7 Conventional $V s$ . Hazard-Adjusted Durations.  

Bonds with a higher hazard rate have higher spreads and, therefore,. lower durations than bonds with a lower hazard rate. The striking message. of Figure 14.7, however, is that HADs can be significantly below conventional durations, particularly for larger hazard rates and longer terms. For 10-year bonds at a hazard rate of. $5\%$ , the conventional duration is 7.7 and. the HAD is 7.3, while at a hazard rate of $10\%$ , the durations are 7.3 con-. ventional and 6.4 HAD. For 30-year bonds at a hazard rate of $5\%$ , the conventional duration is 15.3 and the HAD is 12.8, while at a hazard rate of $10\%$ , the durations are 13.2 conventional and 8.7 HAD..

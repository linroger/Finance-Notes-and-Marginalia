---
aliases:
- Secured Overnight Financing Rate
- Interest rate theory and modeling
- Monetary policy and rate setting
- LIBOR transition and SOFR
- Futures and forwards contract mechanics
- Cash-and-carry arbitrage
- Basis trading and roll strategies
- Bond pricing and yield curves
- Duration and convexity hedging
- Credit spreads and bond valuation
- Fixed income securities and markets
- Bond valuation and yield calculation
- Credit analysis and spread decomposition
- SOFR and financial analysis
- SOFR in modern finance
- Applications of SOFR
- 'Case study: SOFR'
last_enhanced: '2025-11-06 08:42:35'
- treasury
- sofr
- fixed-income
- bond
- futures
- bonds
- interest-rates
- libor
- basis
tags:
- arbitrage
- banking
- basis
- bid-ask
- bond
- case-study
- central-bank
- crisis-analysis
- duration
- empirical-analysis
- fixed-income
- graduate-level
- hedging
- institutional-quality
- learning-from-crisis
- mathematical-finance
- monetary-policy
- professional-standard
- provision
- quantitative-methods
- real-world-example
- repo
- sec-regulation
- securitization
- spread
- treasury
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









# 10.4 SOFR  

In the transition away from LIBOR in the United States, discussed in detail in Chapter 12, regulators and others have advocated for a transition to the. Secured Overnight Financing Rate, or SOFR. Intended to represent the rate of secured, overnight borrowing, the Federal Reserve Bank of New York calculates SOFR using daily repo transactions in the tri-party and DVP markets. However, DVP repo transactions are trimmed so as to exclude the lower-rate, presumably specials trades, which reflect the idiosyncrasies of lending on individual bond issues. In particular, the. $25\%$ of DVP repo trade volume with the lowest rates are excluded from the data used to calculate SOFR.  

TABLE 10.4  SOFR and Treasury Repo Rates, as of May 14, 2021. Rates Are in Basis Points.   


<html><body><table><tr><td>1st %ile</td><td>25th %ile</td><td>Median/ SOFR</td><td>75th %ile</td><td>99th %ile</td><td>Volume ($billions)</td></tr><tr><td>-4</td><td>-1</td><td>1</td><td>1</td><td>15</td><td>865</td></tr></table></body></html>

Source: Federal Reserve Bank of New York.  

Given all included transactions on a given day, SOFR that day is calculated as the "volume-weighted median" rate. This means that SOFR is determined such that. $50\%$ of the volume of loan amounts are at a lower rate and $50\%$ at a higher rate. Table 10.4 provides information about the calculation of SOFR on May 14, 2021. From $\$865$ billion of trades on that. day, SOFR is set to the volume-weighted median rate, which is one basis point. Trades representing $50\%$ of the volume -- from the $25\mathrm{th}$ to the 75th percentiles - include rates between minus one and plus one basis point.

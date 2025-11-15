---
tags:
- curve_risk
- term-structure
- hedging
- apt
- hedge
- treasury_yields
- term_structure
- bond
- maturity
- on_the_run_bonds
- treasury
- financial-engineering
- financial-markets
- yield
- key_rates
aliases:
- Key Rates Motivation
- Term Structure Changes
key_concepts:
- Treasury securities and government bond markets
- Fixed income securities and yield curve analysis
- Value at Risk and tail risk measurement
- Risk management and stress testing
- Hedging strategies and delta-gamma neutrality
- Financial markets and securities trading
- Capital market instruments and their characteristics
- Modern portfolio theory and asset pricing
- Financial engineering and structured products
- Investment analysis and decision-making
- Financial regulation and market oversight
- Risk hedging strategies and instruments
- Term Structure in financial markets
- Financial markets and instrument analysis
- Quantitative finance and mathematical modeling
- Risk management and hedging strategies
- Investment analysis and portfolio theory
- Capital markets and trading strategies
- Financial engineering and product innovation
- Regulatory frameworks and compliance
- Market dynamics and behavioral finance
enhanced: true
enhancement_date: '2025-11-06'
enhancement_id: batch08-000214
batch: BATCH_AH
processing_agent: Enhancement Agent 8
---



# 5.1 KEY RATES: MOTIVATION  

The main motivation for multi-factor hedging is to control curve risk, that is, the risk that rates across the term structure do not move in parallel or in any fixed relationship. Figure 5.1 illustrates this phenomenon using changes in the term structure of on-the-run US Treasury yields on selected days in June  

![](e53e721c8b4b8bc592252321380ee87b817e965382f46e6a3468cc7363da73a4.jpg)  
FIGURE 5.1 Changes in the Term Structure of On-the-Run US Treasury Yields, Selected Days, June 2021.  

[^2021]: (On-the-run bonds are the most recently issued bonds - and usually the most liquid - in their respective maturity ranges.) Each point on each curve represents a change in an on-the-run Treasury yield over a business day. The 20-year term point on the June 18, 2021, curve, for example, shows that the yield of the on-the-run 20-year Treasury bond fell by 9.7 basis points from June 17, 2021, to June 18, 2021.

The June 16, 2021, curve shows a significant change in the curvature of. the term structure: short-term rates rose some; intermediate-term rates rose a lot; and long-term rates rose very little. The June 18, 2021, curve is an example of a flattening of the term structure: short-term rates rose, intermediate rates fell some, and long-term rates fell a lot. The June 21, 2021, curve is an example of a steepening: short-term rates stayed about the same, while longer-term rates rose significantly. And finally, the June 22, 2021, curve can be very roughly categorized as a parallel shift. From Figure 5.1 as a whole,. hedges constructed with the single-factor metrics of Chapter 4 would not have performed reliably over several days in the second half of June 2021.

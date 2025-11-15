---
tags:
- libor_transition
- apt
- repo_transactions
- federal_reserve
- market
- bond
- financial-engineering
- treasury
- repo
- overnight
- financial-markets
- overnight_borrowing
- sofr
- libor
aliases:
- Secured Overnight Financing Rate
key_concepts:
- Treasury securities and government bond markets
- Fixed income securities and yield curve analysis
- Banking and credit intermediation
- Bank balance sheet management
- Financial markets and securities trading
- Capital market instruments and their characteristics
- Modern portfolio theory and asset pricing
- Financial engineering and structured products
- Investment analysis and decision-making
- Financial regulation and market oversight
- LIBOR transition and benchmark rate reform
- SOFR implementation and overnight rate markets
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
enhancement_id: batch08-000167
batch: BATCH_AH
processing_agent: Enhancement Agent 8
---



# 10.4 SOFR  

In the transition away from LIBOR in the United States, discussed in detail in Chapter 12, regulators and others have advocated for a transition to the. Secured Overnight Financing Rate, or SOFR. Intended to represent the rate of secured, overnight borrowing, the Federal Reserve Bank of New York calculates SOFR using daily repo transactions in the tri-party and DVP markets. However, DVP repo transactions are trimmed so as to exclude the lower-rate, presumably specials trades, which reflect the idiosyncrasies of lending on individual bond issues. In particular, the. $25\%$ of DVP repo trade volume with the lowest rates are excluded from the data used to calculate SOFR.  

TABLE 10.4  SOFR and Treasury Repo Rates, as of May 14, 2021. Rates Are in Basis Points.   


<html><body><table><tr><td>1st %ile</td><td>25th %ile</td><td>Median/ SOFR</td><td>75th %ile</td><td>99th %ile</td><td>Volume ($billions)</td></tr><tr><td>-4</td><td>-1</td><td>1</td><td>1</td><td>15</td><td>865</td></tr></table></body></html>

Source: Federal Reserve Bank of New York.  

Given all included transactions on a given day, SOFR that day is calculated as the "volume-weighted median" rate. This means that SOFR is determined such that. $50\%$ of the volume of loan amounts are at a lower rate and $50\%$ at a higher rate. Table 10.4 provides information about the calculation of SOFR on May 14, 2021. From $\$865$ billion of trades on that. day, SOFR is set to the volume-weighted median rate, which is one basis point. Trades representing $50\%$ of the volume -- from the $25\mathrm{th}$ to the 75th percentiles - include rates between minus one and plus one basis point.

---
aliases:
- OAS
- Option Adjusted Spread
- Interest rate swaps and valuation
- Currency and cross-currency swaps
- Swap spreads and basis trading
- Futures and forwards contract mechanics
- Cash-and-carry arbitrage
- Basis trading and roll strategies
- Market liquidity and measurement
- Bid-ask spreads and transaction costs
- Market impact and execution
- Option pricing theory and Black-Scholes model
- Options Greeks and risk management
- Call and put option strategies
- Arbitrage principles and opportunities
- Relative value trading
- Law of one price enforcement
- Option-Adjusted Spread and financial analysis
- Option-Adjusted Spread in modern finance
- Applications of Option-Adjusted Spread
- 'Case study: Option-Adjusted Spread'
last_enhanced: '2025-11-06 08:42:36'
- discount
- spread
- put
- risk
- arbitrage
- liquidity
- valuation
- options
- swaps
- swap
- relative-value
- basis
- futures
tags:
- arbitrage
- bankruptcy
- basis
- bid-ask
- bond
- case-study
- crisis-analysis
- currency
- derivative-pricing
- derivatives
- empirical-analysis
- fixed-income
- graduate-level
- hedging
- institutional-quality
- learning-from-crisis
- liquidity
- mathematical-finance
- monetary-policy
- professional-standard
- provision
- quantitative-methods
- real-world-example
- sec-regulation
- securitization
- spread

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







# 7.6 OPTION-ADJUSTED SPREAD  

Option-adjusted spread is a widely used measure of the relative value of a security, that is, of its market price relative to its model value. OAS is defined as the spread such that the market price of a security is recovered when that spread is added to discount rates in the model. To illustrate, say that the market price of the CMT swap in the previous section is $\$3,499.18$ $\$2.92$ less than the model price. In that case, the OAS of the CMT swap turns out to be 10 basis points. To see this, add 10 basis points to the discounting rates of $2.5\%$ and $1.5\%$ in Equations (7.24) and (7.25), respectively, to get new swap values of,  
$$
\begin{array}{l}{{\frac{.6520\times\S5,000+.3480\times\S0}{1+\frac{.0260}{2}}+\S2{,500}=\S5{,717}{.93}}}\ {{\frac{1+\frac{.0260}{2}}{2}}}\ {{\frac{.6520\times0+.3480\times(-\S5{,000})}{1+\frac{.0160}{2}}-\S2{,500}=-\S4{,226}{.43}}}\end{array}
$$  

Note that, when calculating value with an OAS spread, rates are only shifted for the purpose of discounting. Rates are not shifted for the purposes of  

computing cash flows. In the CMT swap example, cash flows are still computed using Equations (7.19) through (7.23).  

Completing the valuation with an OAS of 10 basis points, use the results of (7.27) and (7.28) and a discount rate of. $2\%$ plus the OAS spread of 10 basis points, or $2.10\%$ , to obtain an initial CMT swap value of,.  
$$
{\frac{.8009\times{\S}{5},717.93+.1991\times(-{\S}4,226.43)}{1+\frac{.0210}{2}}}=\mathbb{5}3,699.18
$$  

Hence, as claimed, discounting at the risk-neutral rates plus an OAS of 10 basis points in the model recovers the given market price of $\$3,699.18$ . If a security's OAS is positive, its market price is less than its model price, which means that the security trades cheap. If the OAS is negative, the security trades rich.  

Another perspective on the relative value implications of an OAS spread. is the fact that the expected return of a security with an OAS, under the. risk-neutral process, is the short-term rate plus the OAS per period. Very simply, discounting a security's expected value by a particular rate per period is equivalent to that security's earning that rate per period. In the example of the CMT swap, the expected return of the fairly priced swap under the. risk-neutral process over the six months from date O to date 1 is,.  
$$
\frac{.8009\times\S5,719.52-.1991\times\S4,227.29-\S3,702.11}{\S3,702.11}=1.00\%
$$  

which is six months' worth of the initial rate of $2\%$ . On the other hand, with an OAS of 10 basis points, the expected return of the cheap swap is,  
$$
\frac{.8009\times\S5,717.93-.1991\times\S4,226.43-\S3,699.18}{\S3,699.18}=1.05\%
$$  

which is six months' worth of the initial rate of $2\%$ plus the OAS of 10 basis points, or half of $2.10\%$

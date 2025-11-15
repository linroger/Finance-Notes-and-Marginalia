---
aliases:
- Implied Repo
- Repo Rates
- Futures and forwards contract mechanics
- Cash-and-carry arbitrage
- Basis trading and roll strategies
- Bond pricing and yield curves
- Duration and convexity hedging
- Credit spreads and bond valuation
- Fixed income securities and markets
- Bond valuation and yield calculation
- Credit analysis and spread decomposition
- Option pricing theory and Black-Scholes model
- Options Greeks and risk management
- Call and put option strategies
- Arbitrage principles and opportunities
- Relative value trading
- Law of one price enforcement
- Implied Repo Rates and financial analysis
- Implied Repo Rates in modern finance
- Applications of Implied Repo Rates
- 'Case study: Implied Repo Rates'
last_enhanced: '2025-11-06 08:42:35'
- options
- forward
- pricing
- call
- ratio
- fixed-income
- put
- arbitrage
- bond
- futures
- bonds
- relative-value
tags:
- arbitrage
- bankruptcy
- basis
- bid-ask
- bond
- case-study
- collateralized-lending
- commercial-paper
- crisis-analysis
- derivative-pricing
- derivatives
- duration
- empirical-analysis
- fixed-income
- graduate-level
- hedging
- institutional-quality
- learning-from-crisis
- liquidity-management
- market-liquidity
- mathematical-finance
- money-markets
- overnight-funding
- professional-standard
- provision
- quantitative-methods
- real-world-example
- repo
- repo-market
- repo-markets
- repo-rate
- repurchase-agreement
- sec-regulation
- securitization
- short-term-funding
- spread
- tri-party-repo
- yield-curve

key_concepts:
- Banking and Financial Intermediation
- Case Study Methodology
- Central Bank Liquidity Facilities
- Collateral Management
- Collateralized Lending
- Commercial Paper Markets
- Crisis Case Study Design
- Empirical Analysis of Financial Events
- Empirical Finance Research
- Financial Crisis Case Studies
- Financial Markets and Institutions
- Historical Financial Analysis
- Institutional-Quality Financial Education
- Learning from Financial Crises
- Liquidity Crisis and Management
- Liquidity Risk and Management
- Money Market Fund Dynamics
- Money Market Instruments
- Overnight Funding Markets
- Quantitative Methods in Finance
- Real-World Financial Examples
- Repo Market Dynamics
- Repo Market Regulation
- Repo Rates and Spreads
- Repurchase Agreement Markets
- Risk Management and Hedging Strategies
- Short-Term Funding Markets
- Tri-Party Repo Arrangements

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







# 11.10 IMPLIED REPO RATES  

Table 11.1 and Equation (11.1) compute the forward price of the 2.875s.   
of 05/15/2028 given its price for spot settlement and its term repo rate from.   
spot to forward settlement. The same relative pricing formula can be applied,.   
of course, to compute the repo rate given a bond's forward and spot prices..   
Under the assumption that a particular bond will be CTD into a futures con-.   
tract, a repo rate computed in this way is called that bond's implied repo rate.  

To illustrate, consider, once again, the 2.875s of 05/15/2028 and the data in Table 11.8. If that bond will be CTD with certainty, the ratio of its forward price to its conversion factor should equal the futures price; that is, its forward price should equal $131-17+/0.8338$ , or 109.68379.8 Then, following the logic of Equation (11.1), the relationship between the bond's spot and forward prices and the repo rate, $r$ , is,  
$$
109.68379+1.07813=(110.77344+0.01562)\left(1+{\frac{r\times136}{360}}\right)
$$  

which gives an implied repo rate of $r=-0.065\%$  

It is evident from Equations (11.1) and (11.20) that a lower repo rate generates a lower forward price. Therefore, if a bond will be CTD with certainty, and if its implied repo rate is less than its actual repo rate, then the futures price is cheap relative to the bond's spot price. Similarly, if a bond will be CTD with certainty, and if the implied repo rate of a bond is greater than its actual repo rate, then the futures price is rich relative to the bond's spot price. In the example, under the assumption that the 2.875s of 05/15/2028 will be CTD, an implied repo rate of $-0.065\%$ and an actual repo rate of $0.015\%$ imply that TYU1 is cheap relative to the CTD's spot. price.  

Another way to think about implied repo is as the rate earned by buying a bond spot and selling it through the futures contract. Rewriting Equation (11.1), with a spot price of 110.77344 and a forward price of 109.71721, the return from buying spot and selling forward is just the repo rate,  
$$
\frac{109.71721+1.07813-(110.77344+0.01562)}{(110.77344+0.01562)}\frac{360}{136}=0.015\%
$$  

Similarly, the return from buying spot and selling forward - this time with a forward price implied by the futures price of. $109.68379-\mathrm{i}\mathrm{s}-0.065\%$ . From this perspective as well, then, TYU1 is too low relative to the spot price of the 2.875s of 05/15/2028, so long as that bond is CTD. Implied repo as a measure of relative value will be revisited in the case study at the end of the chapter.

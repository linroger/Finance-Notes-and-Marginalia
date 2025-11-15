---
aliases:
- Clever Alpha Fund
- ETF Neutral Arb Fund
- Joe Saxon
- market-neutral plays
- Efficient market hypothesis
- Market anomalies and patterns
- Price discovery and information
- Futures and forwards contract mechanics
- Cash-and-carry arbitrage
- Basis trading and roll strategies
- Modern Portfolio Theory and mean-variance optimization
- Efficient frontier and portfolio construction
- Asset allocation and diversification
- Algorithmic trading strategies
- Quantitative signal development
- High-frequency trading
- Option pricing theory and Black-Scholes model
- Options Greeks and risk management
- Call and put option strategies
- Portable Alpha and Market-Neutral Plays and financial analysis
- Portable Alpha and Market-Neutral Plays in modern finance
- Applications of Portable Alpha and Market-Neutral Plays
- 'Case study: Portable Alpha and Market-Neutral Plays'
last_enhanced: '2025-11-06 08:42:33'
- asset-allocation
- signal
- strategy
- options
- call
- beta
- put
- portfolio
- hedging
- algo
- market-efficiency
- portfolio-optimization
- futures
- algorithmic-trading
- alpha
tags:
- algorithmic-trading
- arbitrage
- austerity
- basis
- case-study
- crisis-analysis
- derivative-pricing
- derivatives
- econometric
- empirical-analysis
- equity
- european
- european-debt-crisis
- eurozone
- graduate-level
- grexit
- hedging
- high-frequency
- institutional-quality
- learning-from-crisis
- market-efficiency
- mathematical-finance
- professional-standard
- provision
- quantitative-analysis
- quantitative-methods
- real-world-example
- securitization
- sovereign-debt
- statistical-model

key_concepts:
- Austerity Measures
- Banking and Financial Intermediation
- Case Study Methodology
- Crisis Case Study Design
- Currency Union Risks
- Econometric Analysis
- Empirical Analysis of Financial Events
- Empirical Finance Research
- European Debt Crisis
- European Integration
- Eurozone Crisis Management
- Financial Crisis Case Studies
- Financial Econometrics
- Financial Markets and Institutions
- Fiscal Integration
- Greek Debt Crisis
- Historical Financial Analysis
- Institutional-Quality Financial Education
- Learning from Financial Crises
- Mathematical Finance Applications
- Mathematical Modeling
- Quantitative Analysis in Finance
- Quantitative Methods in Finance
- Quantitative Risk Management
- Real-World Financial Examples
- Risk Management and Hedging Strategies
- Sovereign Debt Restructuring
- Statistical Finance
- Statistical Modeling

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









# 12.2  PORTABLE ALPHA AND MARKET-NEUTRAL PLAYS  

Many market-neutral funds are designed to appeal to a broad set of investors who make their own asset allocation decisions and seek to find skilled managers to generate excess returns. Imagine a large US pension fund that follows a core-satellite approach to investment. For the first half of 2012, it allocates (core: beta) $30\%$ of its portfolio into US equities, $25\%$ into European equities, $25\%$ into emerging markets, $10\%$ into global commodities, and has (satellite: alpha) $10\%$ of its investment dollars left to allocate to other asset classes. It comes across the Clever Alpha Fund that specializes in identifying mispricing in the US ETF market. The fund's manager Joe Saxon has developed an algorithm that signals when an ETF is underpriced relative to the underlying basket of stocks it holds. Saxon has a great track record in three US sectors - financial, tech, and biotech -- in identifying these discounts when they occur, but his algorithm does not work for overpricing situations. The pension fund decides to allocate $5\%$ of its investment dollars to Clever Alpha, but while they admire Saxon for his mispricing skills, they do not want him to take the general exposure to US equities. What if the underpricings happen before the general market drops? So while we buy a relatively cheap ETF full of US industrial or financial stocks at a discount to the net asset value, and while the fund's price "corrects up"' to the full NAV, the US market corrects down. Clever Alpha has a portable alpha solution for that. It offers a market-neutral Clever Alpha ETF Neutral Arbitrage Fund in which it hedges its overall exposure to US equities with short S&P 500 futures. The pension fund can then manage its asset allocation independent of its specific security selection. In the middle of 2012 it can decide to reduce the allocation to US equities from $30\%$ to $20\%$ or even to zero, but still retain the same $5\%$ in Clever Alpha. The process of separating the asset class exposure from specific risk plays is called alpha transfer..  

Let us explain the design of the Clever Alpha ETF Neutral Arb Fund with the use of an index model. The sectors where the mispricings occur are cyclical, and so the overall beta. of the portfolio is $\beta=1.25$ . The excess return on Clever Alpha can then be decomposed as. follows:  
$$
r_{C A l p h a}-r_{F}=\alpha+\beta(r_{S\&P500}-r_{F})+\tilde{e}
$$  

where $\alpha$ is the anticipated return due to the ETF mispricing discovery,. $r_{F}$ is the risk-free or short-term financing rate, and. $\tilde{e}$ is the residual reflecting unanticipated specific sector or component company risk. The residual risk could be not insignificant if the chosen ETFs are very narrow, and one out of 10 stocks in an ETF explodes. In our case, the specific stock component of it is relatively small; it is more likely related to sector underperformance risk and could further be decomposed into, and mitigated by, short positions in sector index funds. If Clever Alpha employs $\$10$ million dollars to buy underpriced ETFs and S&P 500 futures currently trade at 1,250, we compute the right hedge ratio using the beta of the fund as $10,000,000\times1.25/1250\times250=40$ futures contracts. The hedging strategy is dynamic.. If, in September of 2012, the Clever Alpha algorithm signal is not strong and it wants to reduce the amount of purchased ETFs to only $\$8$ million, it will reduce its futures hedge to. 32 contracts. Also, if it reallocates among sectors and more of its underpriced ETFs come. from tech increasing the overall beta of the fund to $\beta=1.50$ , then on $\$10$ million invested the futures hedge will increase to 48 contracts..  

The portable alpha is delivered to the investor through the process of dynamically hedging. the changing nature of the underlying portfolio to offset the systematic beta risk of an asset. class. The objective of the portfolio remains unlocking the value due to specific risk, structural design, or relative value mispricing within that asset class. The investor can independently decide on the allocation of beta risks.

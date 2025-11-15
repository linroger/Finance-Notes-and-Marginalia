---
aliases:
- ACA
- AMPS
- Lessons Learned
- Morgan Stanley
- UBS
cssclasses: academia
- Value at Risk (VaR) and stress testing
- Portfolio risk metrics and measures
- Hedging strategies and effectiveness
- Futures and forwards contract mechanics
- Cash-and-carry arbitrage
- Basis trading and roll strategies
- Credit analysis and rating
- Default probability modeling
- Loss given default estimation
- Mortgage-backed securities structure
- Prepayment modeling and analysis
- Securitization and CDO structures
- Financial regulation and compliance
- Basel III capital requirements
- Dodd-Frank Act implications
- Lessons From The Crisis and financial analysis
- Lessons From The Crisis in modern finance
- Applications of Lessons From The Crisis
- 'Case study: Lessons From The Crisis'
- hedging
- tranche
- futures
- regulatory
- var
- regulation
- risk-management
- basis
- securitization
- credit-risk
- collateral
- subprime
- counterparty
- stress-test
- default-probability
title: Lessons From The Crisis
tags:
- abcp
- abs
- arbitrage
- balance-sheet
- banking
- basel
- basis
- case-study
- cdo
- collateral
- commercial-paper
- counterparty
- crisis-2008
- crisis-analysis
- default
- dodd-frank
- duration
- econometric
- empirical-analysis
- financial-institutions
- financial-markets
- financial-regulation
- governance
- graduate-level
- hedging
- institutional-analysis
- institutional-quality
- learning-from-crisis
- lehman
- leverage
- liquidity
- liquidity-management
- market-liquidity
- market-structure
- mathematical-finance
- mbs
- money-markets
- professional-standard
- provision
- quantitative-analysis
- quantitative-methods
- real-world-example
- regulatory-compliance
- repo-markets
- restructuring
- sec-regulation
- securitization
- short-term-funding
- statistical-model
- stress-test
- structured-product
- supervision
- tail-risk
- tranche
- var
- volatility

key_concepts:
- Bank Supervision
- Banking and Financial Intermediation
- Case Study Methodology
- Central Bank Liquidity Facilities
- Commercial Paper Markets
- Compliance Management
- Corporate Governance
- Crisis Case Study Design
- Econometric Analysis
- Empirical Analysis of Financial Events
- Empirical Finance Research
- Financial Crisis Case Studies
- Financial Econometrics
- Financial Intermediation and Banking
- Financial Markets and Institutions
- Financial Regulation
- Governance Standards
- Historical Financial Analysis
- Institutional Analysis of Financial Systems
- Institutional-Quality Financial Education
- Learning from Financial Crises
- Liquidity Crisis and Management
- Liquidity Risk and Management
- Market Structure and Microstructure
- Mathematical Finance Applications
- Mathematical Modeling
- Money Market Fund Dynamics
- Money Market Instruments
- Quantitative Analysis in Finance
- Quantitative Methods in Finance
- Quantitative Risk Management
- Real-World Financial Examples
- Regulatory Compliance
- Regulatory Framework
- Regulatory Framework in Financial Markets
- Regulatory Risk
- Repurchase Agreement Markets
- Risk Management and Hedging Strategies
- Short-Term Funding Markets
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



# Lessons From The Crisis

# Five Structural Causes Of The Crisis

[^1]: **Ignored Incentives**
	- Incentive concerns treated as quaint
[^1]: **Overreliance on Models**
	- **Quantitative models too fragile in light of poor incentives**
[^1]: **Increased Financial Instrument Complexity and Customization**
	- **Allowed "optimization" of models and regulations**
	- **Securitization**
	- **Failure of financial supply chain management**
[^1]: **Regulatory environment**
	- Too many and inconsistently applied rules/standards

# Recent Headlines

> [!quote]
> "Merrill Upped Ante as Boom In Mortgage Bonds Fizzled"
> 	 						- **Wall Street Journal,  April 16,  2008**

> [!quote]
> "How a Good Subprime Call Came to Hurt Morgan Stanley"
> - **Wall Street Journal,  November 7,  2007**

> [!quote]
> "ACA pain spreads far and wide"
> - **Creditflux Newsletter,  February 2008**

> [!quote]
> "UBS reveals the failures that led to its $37bn sub-prime writedowns"
> - The Times of London,  April 22,  2008

# Observation
- Many of the writedowns during the recent crisis have been on positions which were considered hedged

> [!quote]
> "Once hedged,  … the Super Senior positions were VaR and Stress Testing neutral (i.e.,  because they were treated as fully hedged,  the Super Senior positions were netted to zero and therefore did not utilize VaR and Stress limits) … In several \Market Risk Control] reports,  the long and short positions were netted,  and the inventory of Super Seniors was not shown,  or was unclear. For \the [hedging] AMPS trades,  the zero VaR assumption subsequently proved to be incorrect …"
> −Shareholder Report on UBS's Write-Downs,  April 18,  2008

# ABS CDO Basics

 Collateralized Debt Obligations (CDOs) are pools of securities (e.g. loans).

 - **ABS CDOs are CDOs backed** primarily by subprime and other mortgage-related securities. The Super Senior tranche is the largest and the most senior tranche in the capital structure.

!500 | Finder 2024-09-23 11.41.03.png

# The "Negative Basis" Trade

!Finder 2024-09-23 11.41.16.png

| Economics | 
 | -------------- | -------------- | 
 | CDO pays | L + 20 bps | 
 | CDS premium | (10 bps) | 
 | Funding cost | (L - 10 bps) | 
 | Profit (pa) | 20 bps | 

- Primary source of monoline counterparty risk for banks in structured finance. Banks would enter into a long risk position on a CDO and then buy protection (insurance) on the same asset from a monoline or other protection seller.
 - Because it was viewed as "hedged",  the trade required little or no regulatory capital,  allowing the banks to book the entire payment stream as profit. Structuring/origination banks held CDOs on the balance sheet and bought protection in order to increase deal capacity.

# Counterparty Risk Case Study: ACA

 - ACA was a single-A rated monoline insurer which originally specialized in troubled municipal credits. ACA first branched out to initially managing and later providing insurance for ABS CDOs. ACA eventually insured over $20 billion of ABS CDOs. Super Seniors. Most banks have written the value of their ACA protection on ABS CDOs to zero.
 - ACA entered a restructuring agreement with structured finance counterparties in August 2008.

# Counterparty Risk

 It appears that with respect to these negative basis trades,  prudent analysis was not performed.

ACA had a higher nominal default probability than the asset it was insuring.

- Appears that some regulations allowed a minimum rating requirement without regard to the default probability of the insured instrument.
 **The correlation of the insured and the insurer was ignored.**
- ACA's business,  both with respect to insurance and management,  was structured finance.
 - One financial institution entered into $6.7 billion of trades with ACA in 3Q07,       when the approximate mark-to-market loss on the insured securities may have been multiple times ACA's capital.*Based on TABX 40-100% @ approx $0.40 in 8/07,  assuming all CDOs were mezzanine.

# Counterparty Risk: Lessons Learned
 **Already re-learned:**
- **Counterparties are risky.**
- Need to sum risk across companies (e.g. monoline risks to SF,  ARS,  VRDN,  GICs,  ABCP).

## **Needs Improvement:**
- Independent and thorough analysis of the counterparty's credit and correlation to the insured instrument and to the insuring bank.

## **Valuation:**
- Take account of any basis risk between the different legs of the trade.
- Account for appropriate recoveries and correlations.

# Convexity Risk Case Study: Morgan Stanley

 MS proprietary trading desk entered into a series of trades designed to take advantage of their negative view on subprime mortgages:

- **Short mezzanine levels of the ABX index**
- **Long Super Senior tranches of ABS CDOs to fund the trade**
- Very likely,  the Super Seniors would have been purchased with financing
 - The trade was positioned to profit if the subprime market deteriorated slightly
 - As losses mounted,  the trade reversed and MS took a $3.7 billion loss related to the trade in 4Q07
!Finder 2024-09-23 11.41.33.png

> [!quote]
> - The Leverage, Tail Risk, Volatility Products#6.6 Hedging tail risks | tail risk]] swung from the large long" -- Colm Kelleher MS CFO
- The Leverage, Tail Risk, Volatility Products#6.6 Hedging tail risks | tail risk]] stems from the large long position in ABS CDOs
- Leverage existed not only in the trade itself,  but also within its components
 - There appears to have been no attempts to hedge the tail end of the trade

# Convexity Risk Case Study II: UBS
- UBS retained the Super Senior portions of ABS CDOs they originated. UBS hedged these positions in several ways,  including the AMPS program:
- Amplified Mortgage Portfolio ("AMPS") Super Seniors: these were Super Senior positions where the risk of loss was initially hedged through the purchase of protection on a proportion of the nominal position (typically between 2% and 4% though sometimes more). … Much of the AMPS protection has now been exhausted,  leaving UBS exposed to write-downs on losses to the extent they exceed the protection purchased. As at the end of 2007,  losses on these trades contributed approximately 63% of total Super Senior losses.
- Shareholder Report on UBS's Write-Downs,  April 18,  2008
**The AMPS hedge explicitly excluded Leverage, Tail Risk, Volatility Products#6.6 Hedging tail risks | tail risk]] protection.**

# Convexity Risk: Lessons Learned

 **Hedging trades needs thorough stress testing.**
- The stress testing must cover not only the likely outcome,  but also extreme scenarios.
- Where the long and the short leg reference different assets (basis risk),  the hedge effectiveness needs to be stressed as well.
 **Valuation.**
- **Each leg must be thoroughly modeled (no simplifications).**
- Must take account of the entire probability space (i.e. the "tail risk“).
- Must account for any leverage in the trade,  as well as any liquidity issues with the referenced assets.

# There Is No Such Thing As A Perfect Hedge
- Hedging strategies allowed excess leverage to build on balance sheets.
- The flexibility of OTC derivatives increases opportunities for "optimization" with respect to any regulatory or internal controls. Incentives matter.
- Fancy models (VaR and Stress Testing) are useless if they are ignored because the trade is deemed riskless.

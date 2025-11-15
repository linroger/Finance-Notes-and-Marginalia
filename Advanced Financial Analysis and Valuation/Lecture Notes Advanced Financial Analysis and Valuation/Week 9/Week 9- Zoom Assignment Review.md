---
aliases:
- Zoom Assignment Review
- ARR
- CAC
- SaaS
- TAM
- Zoom
cssclasses: academia
enhanced: true
enhancement_date: '2025-11-06'
enhancement_id: batch03-2370c9
key_concepts:
- ARR x Multiple = Value
- Investment Banking
- Long-term Zoom market share
- Sensitivity analysis in DCF models
- JPMorgan valuation approach
- Risk assessment and management
- Common pitfalls in DCF valuation
- Discounted Cash Flow valuation methodology
- Solution
- Municipal Bonds
- Unified communications market sizing
- Mathematical Finance
- GARCH models and volatility forecasting
- Portfolio optimization and asset allocation
- Course Material
- Case Study
- Quantitative analysis and modeling
- Enterprise vs SMB customer mix
- fundamental valuation methods
- Valuing SaaS business
- Free cash flow to equity and firm valuation
- Stress Testing
- Terminal value estimation and perpetuity growth
- Quantitative Implementation
- Financial markets and instruments
- TAM, revenue retention, CAC
- Harvard Business Review
- Sales multiple valuation
- ROIC = NOPAT margin x Asset turnover
- Stock-based compensation dilution effects
linter-yaml-title-alias: Week 9- Zoom Assignment Review
tags:
- tam
- garch-models
- market-share-analysis
- nopat_margin
- mathematical-finance
- course-material
- roic
- sales_multiple
- case-study
- scenario-analysis
- aFAV
- zoom_valuation
- stock-compensation
- arr
- week9
- quantitative-implementation
- solution
- saas_valuation
- investment-banking
- stress-testing
- cac
- dcf-valuation
- harvard-business-review
- municipal-bonds
title: Week 9- Zoom Assignment Review
---

Thomas Rauter

# ADVANCED FINANCIAL ANALYSIS AND VALUATION OF GLOBAL FIRMS

Zoom - Valuing a SaaS Business

## SAAS AND ZOOM

- Bernstein Research (Feb 2021): With low interest rates bulk of DCF value is in TV and "quasi-unforecastable"
- Example: Zoom valuation
  - JPM in Nov 2020

!500
## SAAS VALUATION (USING SALES MULTIPLE)

- Common method for valuing SaaS firms is using a multiple based off of ARR:
  - ARR × Multiple = Value
- Key factors for adjusting the multiple:
  - Growth, TAM (total addressable market), revenue retention, CAC (customer acquisition cost), gross margins
- TAM estimates:
  - S-1 estimated unified communications (UC) market @ $43bn by 2022
  - J.P. Morgan estimates TAM of ~$40bn
  - TAM could increase with use case expansions (education, phone)
  - Morgan Stanley estimates TAM of $100bn+ due to a combination of traditional UC market + combined education and UC market
- Stock price went from $207 in June to $337 in December 2020

## SAAS VALUATION USING MULTIPLES

- Valuation Guide By Saas Capital
  - Describes common sales-multiple approach to SaaS company valuation
  
!500

See SaaS Capital guide (on Canvas) for meaning of acronyms

## SALES MULTIPLE VALUATION (AS OF JAN 2020)

!500

## ZOOM VALUATION USING VALUE DRIVER MODEL

- Use long-term estimates of ARR, TAM, and NOPAT margin to calculate valuation 10 or 15 years out
  - Like a TV calculation
  - "Starting with the future" (Week 4)
- Key assumptions:
  - Long-term TAM range of $40-$100bn
  - Long-term Zoom market share range of 30% to 50%
  - Long-term NOPAT margin of 15% to 20%
    - Based on more established SaaS companies
  - Asset turnover around 2
    - Currently below 1.5, but SaaS model allows for economies of scale
- Remember ROIC = NOPAT margin × Asset turnover
  - Above assumptions imply RONIC = 30-40%
  - Salesforce 8%, Workday 65%, Servicenow 34%, Oracle 28%

## ZOOM: FUNDAMENTAL VALUATION

!500

Share price in Dec 2020 = $337

## ZOOM VALUATION: SUMMARY

- Scenario analysis to estimate range of implied price per share
- It is hard to justify the $337 price with our analyst-based range of assumptions, even fixing long-term assumptions at the high end of range

!500

- TAM estimates have not changed much
  - Still at $86bn in August 2021

## JPM VALUATION (NOV 2020): PRICE TARGET ($450)

!500

- Note that the NOPAT is smaller than FCF - why?
  - We add back D&A, but there is also CAPEX
  - Use FCF = OCF - CAPEX
  - What about stock-based compensation?
    - OCF is adjusted for stock compensation
    - You should treat it as if it were cash

## HOW DID THE ANALYST TREAT SBC?

- Note the future dilution:

!500

- Adjusting our valuation to SBC:

!500

## JPM: TAM CLAIM

- JPM: $40bn TAM estimate
- Claim: "…only needs to see that penetration get to roughly one-third."
  - Revenue = $40bn × 1/3 = $13.3bn
  - NOPAT estimate implies revenue of $28.8bn or 72% market share
    - $28.8bn = $5.7bn @20% margin
  - Alternatively, NOPAT estimate and 20% margin imply much larger TAM
    - TAM = $28.8bn/0.333 = $86bn
- You cannot get to their price target of $450 with $86bn TAM or 70% market share
  - Not even close (try it with the assignment spreadsheet :)

---
title: Week 3 Financial Risk Analysis
cssclasses:
  - academia
tags:
  - cash_flow
  - financial_risk
  - liquidity_ratios
  - solvency_ratios
  - valuation
aliases:
  - Financial Analysis
  - Risk Analysis
  - Week 3
key_concepts:
  - Bankruptcy prediction models
  - Cash flow analysis
  - Credit default swap spreads
  - Financial risk analysis
  - Forecast cash flows
  - Liquidity, profitability ratios
---

[Financial Risk Analysis](Week%203%20[[Week%203%20Financial%20Risk%20Analysis)|[Financial Risk Analysis](Week%203%20[[Week%203%20Financial%20Risk%20Analysis)|[risk analysis](.md)]]]]

# Week 3 Financial Risk Analysis
## ADVANCED FINANCIAL ANALYSIS AND VALUATION
## FINANCIAL STATEMENT ANALYSIS
### FINANCIAL RISK ANALYSIS
- Valuation Process
	- [Forecast cash flows](.md) (or earnings)
	- Build valuation model and discount CFs
		- Today:
			- Finish [Risk Analysis](.md)
			- focus on financial risk
			- Start with [forecasting](../Week%202/Week%202%20Fundamentals%20Of%20Forecasting.md) (mechanics)
 ![500](66ab8b84e41c89e8c3c0fec5dc2f16f8.png)
### BASIC ISSUES IN LENDING
- "Lemons" Problem (Ex Ante)
	- Who will accept a loan at a given rate?
	- Raising the interest rate does not fix the problem
	- Credit rationing and analyzing the borrower's financial situation are potential solutions (or responses)
- Risk-Incentive Problem (Ex Post)
	- Subsequent increases in [credit risk transfer](../../../Financial%20Engineering/A%20Primer%20on%20Structured%20Finance.md) wealth from the lender to the borrower
	- Analyze whether risk or strategy has changed
	- Place [Slides](Class%20[[Slides%20Note%209%20Bidask.not%20New%202020) 2 Discussion of [Loan Covenants](../../../Financial%20Markets%20and%20Institutions/II.%20The%20Roles%20of%20Banks%20and%20Derivative%20Markets%20in%20Resolving%20Problems%20Inherent%20in%20Debt%20Contracts/Class%202-%20Debt%20Contracts%20due%20to%20Lack%20of%20Information/Class%20Slides%202%20Discussion%20of%20Loan%20Covenants%20Vs.%20Bond%20Covenants.md) Vs. Bond Covenants|Covenants]] into the lending agreement
- Information And [Risk Analysis](.md) Are Critical With Respect To Both Problems

### FINANCIAL RISK ANALYSIS TOOLBOX
- [Ratio Analysis](../Week%201/Week%201%20Ratio%20Analysis%20+%20Valuation%20Review.md)
	- [Liquidity](../../../Financial%20Markets%20and%20Institutions/III.%20Liquidity%20of%20Assets/Class%205-%20Private%20Information,%20Liquidity,%20and%20Securitization/Class%20Note%2010%20Liquidity%20and%20Class%20Note%2010%20Liquidity%20and%20Liquidity%20Managementliquidity%20management.md),  profitability and solvency ratios
- Cash-flow analysis
	- Understand business model
	- Understand financing needs
	- Analyze [cash flow](../../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%201%20-%20Purpose%20and%20Structure%20of%20Financial%20Markets/Preview%20of%20the%20Book.md) statements (and other financials)
	- Assess financial flexibility (e.g.,  could they sell assets?)
- Pro-forma financial statements
	- Predict [future cash flows](../../../Financial%20Engineering/Advanced%20Derivatives%20Pricing%20Methodology.md)
	- Assess ability to meet [interest and principal](../../../Financial%20Engineering/Notes%20on%20Currency%20Swaps.md) payments
- Ratings

### BANKRUPTCY PREDICTION MODELS
- [Credit Default Swap](../../../Credit%20Markets/Credit%20Market%20Session%202.md) (CDS) Spreads

### LIQUIDITY RATIOS - ABILITY TO MEET SHORT-TERM FINANCIAL OBLIGATIONS
- Current ratio
	- $$\text{Current ratio} = \frac{\text{current assets}}{\text{current liabilities}}$$
- Quick ratio
	- $$\text{Quick ratio} = \frac{\text{cash} + \text{mkt. sec.} + \text{A/R}}{\text{current liabilities}}$$
- Inventory turnover
	- $$\text{Inventory turnover} = \frac{\text{cost of goods sold}}{\text{avg. inventory}}$$
- Inventory holding period
	- $$\text{Inventory holding period} = \frac{365}{\text{inventory turnover}}$$
- A/R turnover
	- $$\text{A/R turnover} = \frac{\text{net credit sales (if available,         otherwise,         sales)}}{\text{avg. net A/R}}$$
- A/R collection period
	- $$\text{A/R collection period} = \frac{365}{\text{A/R turnover}}$$
- Operating cycle
	- $$\text{Operating cycle} = \text{Inventory holding period} + \text{A/R collection period}$$

### LIQUIDITY RATIOS - ABILITY TO MEET SHORT-TERM FINANCIAL OBLIGATIONS (CONT.)
- A/P turnover
	- $$\text{A/P turnover} = \frac{\text{Purchases}}{\text{avg. A/P}}$$
	- $\text{Purchases} = \text{COGS} + \text{end. inventory} - \text{beg. inventory}$
- A/P period
	- $$\text{A/P period} = \frac{365}{\text{A/P turnover}}$$
- Cash-to-cash cycle
	- $$\text{Cash-to-cash cycle} = \text{Operating cycle} - \text{A/P period}$$
- Defensive interval (in days)
	- $$\text{Defensive interval (in days)} = 365 \times \frac{\text{Cash} + \text{Mkt. Sec.} + \text{A/R}}{\text{COGS} + \text{other op. exp (excluding deprec.,         amort.)}}$$
- Cash burn cycle (in days)
	- $$\text{Cash burn cycle (in days)} = 365 \times \frac{\text{Cash raised from investors}}{\text{COGS} + \text{other op. exp (excluding deprec.,         amort.)}}$$
- [Liquidity](../../../Financial%20Markets%20and%20Institutions/III.%20Liquidity%20of%20Assets/Class%205-%20Private%20Information,%20Liquidity,%20and%20Securitization/Class%20Note%2010%20Liquidity%20and%20Class%20Note%2010%20Liquidity%20and%20Liquidity%20Managementliquidity%20management.md) index
	- $$\text{Liquidity index} = \frac{(\text{A/R} \times \text{collection period}) + (\text{Inv.} \times \text{Inv. holding period})}{\text{Cash} + \text{Mkt. Sec.} + \text{A/R} + \text{Inventory}}$$
- [Cash flow](../../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%201%20-%20Purpose%20and%20Structure%20of%20Financial%20Markets/Preview%20of%20the%20Book.md) adequacy ratio
	- $$\text{Cash flow adequacy ratio} = \frac{\text{Operating cash flows}}{\text{Capex} + \text{LT debt payments} + \text{Cash dividends}}$$

### SOLVENCY RATIOS - ABILITY TO MEET LONG-TERM FINANCIAL OBLIGATIONS
- Balance sheet [leverage](../../../Advanced%20Investments/Lecture%206-Leverage,%20Tail%20Risk,%20Volatility%20Products.md)
	- Total debt / total assets
	- Long-term debt / total assets
	- Total debt / stockholders' equity
	- Long-term debt / stockholders' equity
- Interest coverage ratio
	- $$\text{Interest coverage ratio} = \frac{\text{Recurring EBIT}}{\text{Annual interest expense}}$$

 (also called "Times Interest Earned or TIE")

- Variants of interest coverage ratio
	- Use EBITDA in numerator
	- Use [cash flow](../../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%201%20-%20Purpose%20and%20Structure%20of%20Financial%20Markets/Preview%20of%20the%20Book.md) in numerator
- [Debt service](../../../Financial%20Engineering/Notes%20on%20Currency%20Swaps.md) coverage ratio
	- $$\text{Debt service coverage ratio} = \frac{\text{EBITDA} + \text{discretionary expenses}}{\text{interest} + \text{principal and lease payments}}$$
- Variants of [debt service](../../../Financial%20Engineering/Notes%20on%20Currency%20Swaps.md) coverage
	- Use operating [cash flow](../../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%201%20-%20Purpose%20and%20Structure%20of%20Financial%20Markets/Preview%20of%20the%20Book.md) rather than EBITDA

### ADDITIONAL CONSIDERATIONS
- Consider The Quality Of The "Inputs"
	- Creditworthiness of accounts receivables
	- Obsolete inventory
	- Other asset impairments
	- This exercise is essentially accounting analysis again
		- The point is that overstated asset will not convert into cash (at least not with the amount of their book value)
- Off-balance sheet liabilities
	- Operating leases
	- Contingent liabilities: e.g.,
		- Warranty claims
		- Pending lawsuits
- Off-Balance Sheet Liabilities And Associated Payments Need To Be Made For A Firm To Remain Solvent

## EVALUATING FINANCIAL FLEXIBILITY
- What Could The Firm Do To Improve Its [Cash Flow](../../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%201%20-%20Purpose%20and%20Structure%20of%20Financial%20Markets/Preview%20of%20the%20Book.md) Situation?
- Consider Various Actions By Essentially Going Through The Line Items In The [Cash Flow](../../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%201%20-%20Purpose%20and%20Structure%20of%20Financial%20Markets/Preview%20of%20the%20Book.md) Statement
#### CASH FROM OPERATIONS
- Cost savings
	- Negotiate wage concessions
- Changes in product mix
	- Simplify product offerings (reduces production costs)
	- Shift towards premium products (increases margin)
- Improve working capital management
	- Speed up collection of receivables or factor receivables
	- More efficient management of inventory
	- Stretch out payables
#### CASH FROM INVESTING ACTIVITIES
- Reduce capital spending (e.g.,  R&D)
- Stretch the use of capital assets
	- Age of assets (accumulated depreciation / depreciation expense)
- Sale-leaseback of fixed assets (e.g.,  land,  buildings,  planes,  etc.)
- Divestitures
	- Sell financial assets
	- Easily divestible assets without disruption? Are the assets highly specific?
	- Are asset sales restricted by debt covenants?

#### CASH FROM FINANCING ACTIVITIES
- Cut dividends
- Unused credit lines?
	- Under what conditions can they be withdrawn by the bank(s)?
- Additional borrowing
	- Is additional borrowing restricted by debt covenants?
- Raise equity

### COST OF DEBT
- Using observable yields (as an approximation):
	- If publicly traded: $\text{R}_d = \text{Yield to maturity on long-term debt}$
		- (yield = IRR such that bond price = PV of _promised_ future [interest and principal](../../../Financial%20Engineering/Notes%20on%20Currency%20Swaps.md) payments)
	- If not publicly traded,  but rated:
		- Yield on [corporate debt](../../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%2014/Corporate%20Bonds%20and%20Loans.md) with similar rating
	- If not public and not rated: Estimate what rating would be (e.g.,  based on financial risk ratios) and then use yield on [corporate debt](../../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%2014/Corporate%20Bonds%20and%20Loans.md) with similar rating
- However:
	- Yield to maturity can be a poor proxy for the cost of debt as the debt becomes riskier or more distressed
	- Cost of debt is the IRR such that bond price = PV of _expected_ future [interest and principal](../../../Financial%20Engineering/Notes%20on%20Currency%20Swaps.md) payments
	- The issue is that in computing the YTM you use the promised payment in the numerator,  rather than the expected payment
	- $$\text{Expected payment} = (1- \text{prob default}) \times \text{promised payment} + \text{prob default} \times \text{payment in default}$$
- For this reason the current (or promised) yield overstates the cost of debt

### WHAT ARE THE COST OF FINANCIAL DISTRESS?
- Present Value Of Expected Costs Resulting From Risky [Debt Financing](../../../Contemporary%20Financial%20Intermediation%20Notes/Contemporary%20Financial%20Intermediation%20Notes.md)
- Includes potential costs to firm as it approaches default AND costs to firm if defaults
- Costs of distress are a reduction in the [expected cash flows](../Week%206/Week%206%20Assignment%20Review.md)

#### EXAMPLES
- Decline in employee productivity (job hunting,  low morale) and/or ↑ in turnover
- Customers' and suppliers' concerns about potential interruptions or cancellations of warranties,  parts,  service
- Fire-sale of assets
- Potential underinvestment (shareholders' unwilling to fund new projects since benefits will accrue to bondholders,  and since debt [Slides](Class%20[[Slides%20Note%209%20Bidask.not%20New%202020) 2 Discussion of [Loan Covenants](../../../Financial%20Markets%20and%20Institutions/II.%20The%20Roles%20of%20Banks%20and%20Derivative%20Markets%20in%20Resolving%20Problems%20Inherent%20in%20Debt%20Contracts/Class%202-%20Debt%20Contracts%20due%20to%20Lack%20of%20Information/Class%20Slides%202%20Discussion%20of%20Loan%20Covenants%20Vs.%20Bond%20Covenants.md) Vs. Bond Covenants|Covenants]] prohibit additional borrowing)
- Management time spent in discussions with creditors and [investment bankers](../../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%201%20-%20Purpose%20and%20Structure%20of%20Financial%20Markets/Primary%20Issuance%20and%20Secondary%20Resale%20Markets.md) about refinancing and reorganization (instead of running the business)
- Costs Of [Financial Distress](../../../Financial%20Markets%20and%20Institutions/III.%20Liquidity%20of%20Assets/Class%205-%20Private%20Information,%20Liquidity,%20and%20Securitization/Southland%20Corp.%20(c).md) Likely Vary Across Industries And Over Time
-  ![500](3e418c137201bf8000d09e61787f4169.png)
- $L= \frac{BV(D)}{BV(D)+MV(E)}$
 ![500](b2ff5dc744a8b49bae39a84fcf0d9666.png)
#### ESTIMATED COSTS HIGHER IN INDUSTRIES WITH
- High underinvestment potential
- Risk of asset fire-sales
- High reliance on human capital
- High importance of post-sales service,  warranties,  and parts

### ALTERNATIVE ESTIMATE FOR THE COST OF DISTRESS
- The spread data for A,  BBB,  BB,  and B bonds come from Citigroup's yieldbook,  and refer to average corporate bond spreads over Treasuries for the period 1985 to 1995. Data for AAA and AA bonds come from Huang and Huang (2003). This table reports risk adjusted probabilities of default (q) calculated from bond yield spreads,  as explained in the text. The probabilities p are the yearly historical probabilities of default (data from Moodys,  averages 1970 to 2001). This table also reports our estimates of the NPV of the costs of [financial distress](../../../Financial%20Markets%20and%20Institutions/III.%20Liquidity%20of%20Assets/Class%205-%20Private%20Information,%20Liquidity,%20and%20Securitization/Southland%20Corp.%20(c).md) expressed as a percentage of pre-distress firm value,  calculated using risk adjusted probabilities (NPV (q)) and historical probabilities (NPV(p)). It also reports in the last row the increase in the NPV of distress costs that is associated with a rating change from AA to BBB. We use an estimate for the loss in value given distress of 16.5%,  a [recovery rate](../../../Credit%20Markets/Credit%20Markets%20Session%203.md) of 0.41,  and a risk free rate of 5%.
 ![500](ce4f614b9d661992cf364575f6518dcb.png)
#### RATING AGENCIES
- Information Intermediary
- Ratings Could Be For Firm (SPE) As Well As Particular Bond Or Debt Agreement
- Rating technology
	- Ratios & models
	- Adjustments (e.g.,  off-balance sheet debt)
	- Qualitative assessments (committee)
- Recall third-party conflicts
	- Rating agencies need to "gain access" to information to have a [competitive advantage](../Week%206/Week%206%20Bank%20Analysis%20and%20Valuation.md) over other agencies
	- Rating agencies "sell" their ratings to firms that they rate
	- Only three major rating agencies
	- Ratings are often required for regulatory purposes (by "Nationally Recognized Statistical Rating Organization" or NRSRO)
- Downgrades can become self-fulfilling prophecy
- [Dodd-Frank Act](Note%20on%20The%20[[Credit%20Derivative%20Indexes) and Its Impact|[Dodd-Frank](../../../Course%20Notes/HBR%20Notes/Note%20on%20The%20Dodd-Frank%20Act%20and%20Its%20Impact.md)]] eliminates reference to ratings for capital requirements
	- Prediction models do not have this constraint
	- "Stability" of ratings is viewed as desirable

### 'CONDENSED HISTORY' OF BANKRUPTCY PREDICTION
- Financial Ratios (Profitability,  [Liquidity](../../../Financial%20Markets%20and%20Institutions/III.%20Liquidity%20of%20Assets/Class%205-%20Private%20Information,%20Liquidity,%20and%20Securitization/Class%20Note%2010%20Liquidity%20and%20Class%20Note%2010%20Liquidity%20and%20Liquidity%20Managementliquidity%20management.md) And Solvency)
	- Ratios start to deteriorate before bankruptcy,  often even several years
	- How do we combine ratios or assess probability of default?
	- Similar to prediction of fraud or accounting manipulations
### BANKRUPTCY PREDICTION MODELS
- Altman's Z score (1968) - Godfather of all [bankruptcy](../../../Course%20Notes/HBR%20Notes/A%20Strategic%20Perspective%20on%20Bankruptcy.md) prediction models
- Modified versions of Z score model
- Ohlson model (1980)
	- Econometric improvement but conceptually similar
	- See coefficients and details in Appendix of this slide deck
	- Also covered in Penman,  Chapter 19
### LATEST TWIST: USE MARKETS AND MODELS WITH MARKET DATA
- Stock [returns](../../../Financial%20Markets/Financial%20Asset%20Pricing%20Theory%20Overview/Chapter%203%20-%20%20Assets,%20Portfolios,%20and%20Arbitrage/Assets.md) and return volatility (e.g.,  Shumway model,  JoB 2001)
- Contingent claim (or [Merton](../../../Credit%20Markets/Credit%20Markets%20Session%205.md)) model and KMV
- CDS spreads

### ALTMAN Z-SCORE BANKRUPTCY PREDICTION MODEL
- Best Known Bankruptcy Prediction Model: A Multivariate Discriminant Model
- Data:
	- Bankrupt sample
		- 33 manufacturing firms
		- Filed for [bankruptcy](../../../Course%20Notes/HBR%20Notes/A%20Strategic%20Perspective%20on%20Bankruptcy.md) between 1946-65
		- Asset size: $0.7 million to $25.9 million (avg. total assets of $6 million)
	- Non-bankrupt sample
		- 33 manufacturing firms
		- Matched by industry,  size,  year
 ![500](491992de7091d970b7e00a181a945327.png)
Higher is 'better'

| Ratio | Characteristic |
|-------|-----------------|
| Z-Score = 1.2 [working capital/ total assets] | ST [liquidity](../../../Financial%20Markets%20and%20Institutions/III.%20Liquidity%20of%20Assets/Class%205-%20Private%20Information,%20Liquidity,%20and%20Securitization/Class%20Note%2010%20Liquidity%20and%20Class%20Note%2010%20Liquidity%20and%20Liquidity%20Managementliquidity%20management.md) |
| + 1.4 [retained earnings / total assets] | Age,         accumulated profitability,         internal financing (vs. debt) |
| + 3.3 [EBIT / total assets] | Profitability of assets |
| + 0.6 [mkt val equity / book val total liab] | LT solvency risk and mkt's assessment of profitability & risk |
| + 1.0 [sales / total assets] | Asset utilization |

### ALTMAN Z-SCORE BANKRUPTCY PREDICTION MODEL (CONT.)
- Interpretation:
	- Z < 1.81 => E\[Bankrupt]
	- 1.81 - 2.99 => Gray area
	- > 2.99 => E\[Non-bankrupt]
- Decision Rule: (minimizes total number of errors)
	- Z < 2.675 => E\[Bankrupt]
	- Z>= 2.675 => E\[Non-bankrupt]
	-  ![500](f316ee52c077d78628422ffb893569d3.png)
- Accuracy falls off as number of years before [bankruptcy](../../../Course%20Notes/HBR%20Notes/A%20Strategic%20Perspective%20on%20Bankruptcy.md) increases
	- 1 year prior to bankruptcy: overall correct: 95%
	- 2 years prior to bankruptcy: overall correct: 83%
	- 5 years prior to bankruptcy: overall correct: 36%

### DESPITE LIMITATIONS,  THE ORIGINAL 1968 MODEL STILL WORKS …

 ![500](b36be0f7cf6cce077f1d05fcf4b2fa67.png)

### Z-SCORES FOR S&P BOND RATINGS

 ![500](d256a5217b33202aa1184bd2bf05a970.png)

### MODIFIED ALTMAN Z-SCORE MODELS FOR PRIVATE FIRMS AND SERVICE FIRMS

 ![500](419c27cf83fab423108d3e9f332d7b1d.png)

### KMV PREDICTION MODEL
- Extension Of [Merton](../../../Credit%20Markets/Credit%20Markets%20Session%205.md)'s Bond [Pricing](../../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%207/Arbitrage%20Pricing%20of%20Derivatives.md) Model (1974)
- Based on contingent-claim framework and option [pricing](../../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%207/Arbitrage%20Pricing%20of%20Derivatives.md) theory
	- Equity = Call option on the firm's assets
	- Debt = [Strike price](../../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%205%20Options%20on%20Prices%20and%20Hedge-Based%20Valuation/Call%20and%20Put%20Payoffs%20at%20Expiry.md) of the option
- Model is based on equity prices and volatility of equity prices
	- Equity volatility is "de-levered" to obtain the asset volatility
	- Model implicitly uses info in stock prices
	- Use of market information makes the model more timely
- EDF (expected default frequency) = probability of default
	- Like the accounting-based [bankruptcy](../../../Course%20Notes/HBR%20Notes/A%20Strategic%20Perspective%20on%20Bankruptcy.md) prediction models,  the KMV model is focused on the default probability; does not estimate losses given a default
	- Loss-given-default (LGD) depends on the seniority,  collateral,  convertibility,  covenants,  etc.
- For more details on KMV model:
	- See Additional Readings folder on Chalk: e.g.,  [primer](../../../Advanced%20Investments/An%20Asset%20Allocation%20Primer.md) on KMV by Moody's

### BASIC IDEA BEHIND KMV MODEL

 ![500](7cb534f48db9b9c797cc49d489e31ef6.png)

This is not necessarily the face value of debt

Commonly used default point = current liabilities + 50% long-term liabilities

### BASIC IDEA: EXAMPLE

 ![500](051c7bf019a290e5ed4a0cb3f05376d8.png)

### MORE ON KMV MODEL
- There are basically three steps to derive the actual probabilities of default:
	1. Estimate the market value and volatility of the firm's asset
	1. Calculate the distance to default,  an index measure of [default risk](../../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%207%20-%20Default%20Risk%20and%20Credit%20Derivatives/Default%20Risk%20and%20Credit%20Derivatives%20183.md)
	1. Scale of the distance to default to actual [default probabilities](../../../Credit%20Markets/Credit%20Markets%20Session%203.md) using a default database

### MOODY'S BOUGHT KMV IN 2002
- There are some differences between Moody's KMV model and [Merton's model](../../../Financial%20Engineering/8.%20Credit%20Modeling%20and%20Credit%20Derivatives.md)
	- Moody's uses its large historical database to estimate empirical distributions rather than using the normal distribution
	- Moody's may make adjustments to the accounting information to compute the face value of debt and adjust the default point
	- Moody's model is a generalization of [Merton's model](../../../Financial%20Engineering/8.%20Credit%20Modeling%20and%20Credit%20Derivatives.md) allowing for various classes and maturities of debt
### RATINGS VS. EDF

 ![500](804fd7bc8a23311a9f28d2e015dcf026.png)

### ENRON

 ![500](915b77ca65328ce2109bad65356944ab.png)

### WORLDCOM (CONT.)

 ![500](7845909127423edee902c77fa6127431.png)

#### Z-SCORE USING ADJUSTED NUMBERS

 ![500](4b099b772cb1e1afcd64115b136cf575.png)

- Dark line is Z score based on unadjusted financials
- Light lines show Z score after adjusting financials for manipulation (and writeoffs)

### ROLE OF ACCOUNTING
- All models rely on accounting numbers (either implicitly or explicitly)
	- Stock prices react to accounting numbers
	- Citi uses a hybrid model that combines financial ratios and EDF
- Think about adjusting the accounting numbers:
	- Earnings management
	- Differences in accounting choices or [accounting rules](../Week%206/Week%206%20Bank%20Business%20Model,%20Regulation,%20and%20Accounting%20Rules.md)
	- Off-balance-sheet financing (e.g.,  leases)
		- Moody's performs such adjustments
	- One-time effects (e.g.,  non-recurring items)
- Note that a model is fitted on firms' "average" characteristics
	- So,  for instance,  the average level of off-balance-sheet financing is in principle captured by the model
	- Thus,  it is "unusual" amounts of off-balance-sheet financing that you have to worry about
- Example:
	- ![500](3d7a043a6f50989b707a9a3ab0084f62.png)

### CREDIT DEFAULT SWAPS
- A [credit default swap](../../../Credit%20Markets/Credit%20Market%20Session%202.md) (CDS) is a contract in which the _buyer_ of the CDS makes a series of payments to the _seller_ and,  in exchange,  receives a payoff if a credit instrument (typically a bond or loan) undergoes a pre-defined [credit event](../../../Financial%20Engineering/Valuation%20of%20Credit%20Default%20Swaps.md)
- [Credit event](../../../Financial%20Engineering/Valuation%20of%20Credit%20Default%20Swaps.md) is generally default,  i.e.,  a failure to pay
	- But 'Failure to Pay' can also be triggered if the credit instrument is undergoing restructuring,  bankruptcy,  or (much less common) by having its credit rating downgraded
- The "spread" of a CDS is the annual amount the [protection buyer](../../../Financial%20Instruments/Financial%20Derivatives%20and%20Quantitative%20Methods/Credit%20Default%20Swaps.md) must pay the [protection seller](../../../Financial%20Instruments/Financial%20Derivatives%20and%20Quantitative%20Methods/Credit%20Default%20Swaps.md) over the length of the contract,  expressed as a percentage of the notional amount
	- For example,  if the [CDS spread](../../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%2014/Cds-Equivalent%20Bond%20Spread.md) is 50 basis points,  or 0.5%,  then an investor buying $10 million worth of protection from a bank must pay the bank $50,  000 per year
	- Spread is essentially a market-based measure of [credit risk](../../../Course%20Notes/Quantitative%20Trading%20Strategies%20Lecture%20Notes.md)
- Credit default swaps are conceptually related to the KMV model,  except that the prices are established through trade
- At present,  CDS prices are only available for larger companies

### CDS VS. EDF

 ![500](412826bbe17a13720478fa6d79bfd0d4.png)

#### BLOOMBERG EXAMPLE: DUPONT
- Bloomberg screen summarizes all financial risk information: ratios,  CDS prices and the IG rating and default prob are based on KMV-type analysis
-  ![500](4a9fb868eaec5ec29d4a93f4441fbdce.png)
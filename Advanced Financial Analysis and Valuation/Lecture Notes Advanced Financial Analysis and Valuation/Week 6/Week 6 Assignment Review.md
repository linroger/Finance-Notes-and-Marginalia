---
aliases:
- Blackstone Citigroup Case
- Loan Portfolio Valuation
- Week 6 Review
cssclasses:
- academia
enhanced: true
enhancement_date: '2025-11-06'
enhancement_id: batch03-22d12a
key_concepts:
- Liquidity coverage ratio and net stable funding ratio
- Extensions to multi-factor CAPM models
- regulatory capital requirements and buffers
- Duration and convexity analysis for bond portfolio management
- net interest margin analysis
- Bank regulatory capital requirements
- Stress testing and supervisory review processes
- Duration mismatch in banking
- Credit market dislocations
- Single-name vs. index CDS trading
- Option Greeks and portfolio risk management
- Level 1 fair value hierarchy inputs
- Dividend payments during crisis
- Loan loss provisions cyclicality
- Capital Asset Pricing Model and expected returns
- Credit spread decomposition and hazard rates
- Vega and volatility risk management
- Leverage ratio and large exposures
- CDS clearing and central counterparties
- fixed income risk measurement
- Run on the bank mechanics
- Expected cash flows calculation
- CDS-Bond basis and arbitrrage opportunities
- Swap spread and credit risk considerations
- Mathematical Finance
- leverage ratio calculation and monitoring
- GARCH models and volatility forecasting
- Mergers Acquisitions
- Asset sales versus capital raising
- Fixed-for-floating swap cash flows and valuation
- Course Material
- Risk-weighted assets and capital adequacy ratios
- Security Market Line and beta measurement
- Interest rate swap pricing and valuation
- Basel III regulatory framework and capital requirements
- Cost of risky debt computation
- Credit default swap pricing and risk-neutral probabilities
- present value and discounting methods
- Level 3 fair value hierarchy inputs
- Variance swaps and volatility trading strategies
- Liquidity crisis and market dysfunction
- deposit insurance and protection systems
- fair value measurement and hierarchy
- Tier 2 capital and supplementary requirements
- Delta hedging strategies in options portfolio management
- systematic risk and market exposure
- unobservable inputs for valuation
- Gamma and convexity adjustments
- Capital Structure
- Tier 1 capital ratio impacts
- Tier 1 capital and core equity requirements
- Credit risk modeling and portfolio correlation analysis
- Delta hedging and the replication argument
- Cross-currency basis swaps and funding
- Level 2 fair value hierarchy inputs
- Market portfolio and risk-free rate assumptions
- Citigroup financial statements analysis
- credit risk transfer mechanisms
- Loan portfolio valuation methods
- Empirical tests and anomalies in CAPM
linter-yaml-title-alias: Week 6 Assignment Review
tags:
- basel-iii
- liquidity-crisis
- credit-default-swaps
- loan_valuation
- default-probability
- bank-regulation
- capm
- duration
- blackstone
- bank_run
- credit-risk
- duration-convexity
- solution
- financial_statements
- private-equity
- tier-2-capital
- loan_portfolio
- deposit-insurance
- tier_1_capital
- sensitivity-analysis
- credit-analysis
- cds
- income-statement
- garch-models
- mergers-acquisitions
- interest-rate-swaps
- mathematical-finance
- balance-sheet
- course-material
- capital-structure
- greeks
- regulatory_capital
- tier-1-capital
- citigroup
- net-income
- quantitative-implementation
- leverage-ratio
- dcf-valuation
- harvard-business-review
- bank_regulation
title: Week 6 Assignment Review
---

# Week 6 Assignment Review

Thomas Rauter  
Advanced Financial Analysis and Valuation of Global Firms  
Case: Citigroup, Blackstone, and the Sale of a Loan Portfolio

## Citigroup and Blackstone Case

- Part 1: Examine and understand Citigroup's financial statements
  - Primary balance sheet and income statement line items
  - Fundamentals of bank regulatory capital
  - Run on bank and fair value accounting
  - Review of the bank basics (see also pre-recording)
- Part 2: Valuing a loan portfolio
  - Evaluating the sale of Citigroup's loan portfolio to Blackstone
  - Valuing debt
    - What is the value of a loan (portfolio)?
    - Expected cash flows, default and discount rates for debt
    - Computing the cost of (risky) debt

## Primary Line Items: Balance Sheet

- Assets: $2.188 trillion at the end of 2007
  - Total Loans: $762 billion (35% of total assets)
    - Consumer and corporate loans
    - Typically held to maturity
    - Reported at historical (or amortized) cost
  - Allowance for loan losses: 2.1% (=$16,117 / $777,993)
    - Estimate of uncollectible amounts (contra-asset)
  - Trading account assets $539 billion (25% of total assets)
    - Investments in credit (and equity) securities that Citigroup is ready to sell
    - Reported at fair value; unrealized gains and losses affect the P&L
- Liabilities
  - Total deposits ($826 billion; 38% of total assets)
  - Short-term borrowing and long-term debt ($574 billion; 26%)
  - Very high (simple) leverage: 18.3 (=$2,074,033/$113,598)

## Primary Line Items: Income Statement

- No "classic" revenue for banks
  - Net interest margin
    - Net interest revenue: $49.6 billion
  - Why did the margin likely expand in 2007?
- Provisions for loan losses
- Compensation is a major expense for banks (50% of operating expenses)
- Citi's net income declined significantly from 2006 to 2007. Primary contributors?
  - "Non-interest revenue" declined by $16 billion
    - Principle transactions: -$12.1 billion (trading losses)
    - Primarily driven by subprime exposure: -$21.8 billion
  - Provisions for loan losses increased from 6.7 billion (2006) to 17.4 billion (2007)
    - What happened to loan losses in 2007?
    - Loan losses ($11.7 bn) were not much higher than 2005, but used up ALLL in 2006

Recall from Recording: Delay in LLPs and net charge-offs

- During 2007-2008, banks increased their LLPs to catch up with rising charge-offs
  - LLPs should cover future loan losses (not current ones)
  - LLPs increase in a middle of a crisis (procyclicality)

!500

## What Happens During a Run on the Bank?

- Why are banks vulnerable to runs?
  - Banks have a substantial duration mismatch on their balance sheet (short term liabilities and long term assets)
- In a run customers demand their deposits back
  - They can because they are payable on demand
- But the bank only has few short-term assets
  - Long-term assets cannot be liquidated (or are costly to liquidate)
- For Citigroup in 2007:
  - $38.2 billion in cash and $69.4 billion deposits with other banks
    - Citi also has securities it could sell
  - $826.2 billion in deposit liabilities
- But the US has deposit insurance? Is a run still a concern?

# Regulatory Capital

## Three Primary Ratios in 2007

$$\begin{aligned}
\text{Tier 1 Capital Ratio} &= \frac{\text{Tier 1 Capital}}{\text{Risk-weighted Assets}} = 4\% \text{ minimum} \\
\text{Total Capital Ratio} &= \frac{\text{Total Capital}}{\text{Risk-weighted Assets}} = 8\% \text{ minimum} \\
\text{Leverage Ratio} &= \frac{\text{Tier 1 Capital}}{\text{Average Total Assets}} = 3\% \text{ minimum}
\end{aligned}$$

!500

### Tier 1 Capital - Common Stockholders' Equity

- Non-cumulative perpetual preferred
- Limited amounts of other preferred securities
- Minority interest in consolidated subsidiaries

### Tier 2 Capital - Loan Loss Reserves (Limited to 1.25% of RWA)

Total Capital
- Perpetual preferred (unlimited)
- Hybrid capital
- Subordinated debt (limited to 50% of Tier 1)
- Unrealized gains (losses) on available-for-sale equity securities

### Tier 3 Capital

- Subordinated debt (at least two-year maturity)

## Main Components of Citigroup's Regulatory Capital?

- Risk-adjusted assets only 57% of total assets: Why lower than total assets?
  - Cash and cash due from banks likely have zero weight
  - Consumer loans are likely residential mortgages with only 50% weight

!500

## Effect of $50 Billion Losses on Tier 1 Ratio

- Approximately 10% decline in trading assets
- Journal Entry:
  - Dr. Principal Transactions – Unrealized Losses on Trading Assets  50,000
  - Cr. Trading account assets 50,000
- Losses reduce retained earnings and common shareholders' equity by $50 billion
- Effect on Tier 1 Capital Ratio:

$$\begin{aligned}
\text{Tier 1 Capital Ratio} &= \frac{\text{Tier 1 Capital}}{\text{Risk-weighted Assets}} = \frac{89,226}{1,253,321} = 7.1296\% \\
\text{Tier 1 Capital Ratio} &= \frac{89,226 - 50,000}{1,253,321 - 100\% \times 50,000} = 3.26\%
\end{aligned}$$

- Citi would be undercapitalized violating minimum Tier 1 Capital requirements
  - What could Citi do in response?

## Portfolio Sale to Blackstone

Deal structure
- $6.11 billion loan portfolio
- $3.81 billion loan
- Citigroup → Blackstone
- Collateral/Margin Calls
- $5.07 billion ($1.26 billion equity)

## Does This Transaction Make Sense for Citigroup?

- Why is Citigroup seeking to sell the portfolio of leveraged loans?
  - No intention to hold these loans in the first place
  - Bridge loans for lucrative buyout transaction clients
  - Bridge loans have escalating financing costs but they were issued at the peak of the credit cycle with loosening credit standards
    - Limited bank protection against downturns
  - Citigroup suffered unprecedented losses
    - Under pressure to sell assets
- How does the deal change Citigroup's exposure to defaults in the loan portfolio? How will it affect Citi's Tier 1 capital ratio?
  - Bridge loans are not intended to hold to maturity: marked-to-market
    - Asset value decline directly affects income, retained earnings, Tier 1 capital
  - Immediately take a hit on sale, but less exposed to future increases in default risk
  - New secured loans (to PE firms) would likely have a lower risk weight

## Would Selling Assets Improve the Tier 1 Ratio?

- Start from $50 billion loss
- Assume for simplicity that they sell $10 billion
  - No gain or loss on sale (optimistic)
- Starting point:
  $$\text{Tier 1 Ratio} = \frac{\text{Tier 1 Capital}}{\text{Risk-weighted Assets}} = \frac{39,226}{1,203,321} = 3.26\%$$
- Effect of the sale:
  $$\text{Tier 1 Ratio} = \frac{39,226}{1,203,321 + [10,000 \times 0\%] - [10,000 \times 100\%]} = 3.29\%$$

## What Else Could Citigroup Do to Cover $50B Loss?

- Key insight: Asset sale does not move the dial on Tier 1 Capital
  - Buyers will discount the assets
- Raise Capital:
  - Suppose Citi sells $10 billion of common stock to raise cash
  - The new Tier 1 Capital Ratio is:
    $$\text{Tier 1 Capital Ratio} = \frac{39,226 + 10,000}{1,203,321 + 10,000 \times 0\%} = 4.1\%$$
  - Raising capital improves Tier 1 much faster than selling assets
- Why not raise capital instead of selling assets?
  - Dilution of existing shareholders due to "fire sale" of equity at depressed stock prices
  - Who will buy during crisis?
  - Negative signal – could set off a run
- What about dividend payments?
  - Citigroup paid dividends of 10.7 billion in 2007 (and still 7.5 billion in 2008!)

!500

## Does This Transaction Make Sense for Blackstone?

- Portfolio is a large illiquid asset
  - Dislocations in the credit market
- Purchase requires large amount of capital and capability to service loans
  - PE firms had large amounts of contributed capital
  - Freeze in credit markets and capital needs to be deployed
  - Hard to implement other large buyouts
- Citigroup is a distressed motivated seller
  - Needs to sell = purchase could be a bargain
- Who knows more about the assets?
  - Blackstone may know loan portfolio better than other potential buyers and potentially even Citigroup from past due diligence on equity investments
  - Other bidders probably do not want to outbid a well-informed bidder
- Blackstone does not have control rights in the underlying portfolio firms
  - Control rights would allow them to interfere with debtors

# Valuing the Deal

!500

Value of the deal
- Present value of expected cash flows
- Expected payoff in a given year = [Interest payment × Probability of Survival] + [Recovery × Probability of Default]

!500

Sensitivity analysis: Beta and default probability

Sensitivity analysis: Recovery rates and default prob

!500

Epilogue: What happened to the loan portfolio?

!500

## Sensitivity Analysis: Beta and Default Probability

!500

## Sensitivity Analysis: Recovery Rates and Default Prob

!500

- Blackstone and Citi entered the deal in April 2008
- Blackstone exited completely by 2013 realizing 2x the invested (equity) capital
  - Roughly 15% p.a.
- In retrospect, the timing of the deal was probably not ideal for Blackstone
  - Subsequently, CDS skyrocketed, secondary loan market prices fell and loans were marked to 70 cents on the dollar at their low point (March 2009)
  - Better deals may have been available later in the crisis
    - But timing the market is hard
- Blackstone did not face margin calls, but they came close
  - Their equity stake was written down to close to zero and only recovered slowly

Average bid quote for leveraged loans over crisis

!500

## Appendix

### Citigroup Dividends Paid in Cash

### Fair Value Accounting: SFAS 157

Level 1 - Quoted prices for identical instruments

Level 2 - Quoted prices for similar instruments
- Quoted prices for identical or similar instruments in markets that are not active
- Model derived valuations in which all significant inputs and significant value drivers are observable in active markets

Level 3 - Valuations derived from valuation techniques in which one or more significant inputs or significant value drivers are unobservable
- Use observable market data when available
- Minimize unobservable inputs
- Net income will reflect regular operations and changes in asset values

!500

!500

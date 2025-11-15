---
Owner: Roger Lin
aliases:
- Bank Liquidity Primer
- Liquidity in Banking
cssclasses:
- academia
enhanced: true
enhancement_date: '2025-11-06'
enhancement_id: batch03-143de2
key_concepts:
- Bank liquidity definition
- FDIC deposit insurance
- Precautionary savings reserves
- Liquidity coverage ratio and net stable funding ratio
- Basel III capital requirements and stress testing
- Stress testing and supervisory review processes
- Treasury Bonds
- Single-name vs. index CDS trading
- Collateralized Debt Obligations
- Credit risk modeling and default probability estimation
- Probability of default estimation from credit spreads
- Level 1 fair value hierarchy inputs
- Credit spread analysis and OAS methodology
- Solution
- Diamond-Dybvig model
- Credit spread decomposition and hazard rates
- Credit portfolio diversification and concentration
- Structural models of default and Merton formulation
- CDS clearing and central counterparties
- Leverage ratio and large exposures
- CDS-Bond basis and arbitrrage opportunities
- Swap spread and credit risk considerations
- Mathematical Finance
- Credit default swap pricing and recovery assumptions
- GARCH models and volatility forecasting
- 'Structured products: CDOs, CLOs, and credit derivatives'
- Shadow Banking
- Illiquidity vs insolvency
- Fixed-for-floating swap cash flows and valuation
- Course Material
- Risk-weighted assets and capital adequacy ratios
- Basel III capital and liquidity standards development
- Synthetic credit derivatives and index trades
- International regulatory coordination and Basel standards
- Net interest margin analysis and banking profitability
- Interest rate swap pricing and valuation
- Interbank market borrowing
- Basel III regulatory framework and capital requirements
- Funding illiquid assets
- Credit default swap pricing and risk-neutral probabilities
- Variance swaps and volatility trading strategies
- Liquidity crisis and market dysfunction
- Credit exposure measurement and EAD
- Loss given default and recovery rates
- regulatory stress testing and risk assessment
- Federal Deposit Insurance Corporation
- Wrong-way risk in derivative transactions
- Stress Testing
- Credit intermediation and information asymmetry
- Shadow banking system and regulatory arbitrage
- Quantitative Implementation
- Credit risk migration matrices and rating transition
- Credit risk modeling and portfolio correlation analysis
- Credit risk assessment and loan portfolio management
- Cross-currency basis swaps and funding
- Counterparty credit exposure measurement
- banking regulation and capital adequacy
- liquidity measurement and management
tags:
- basel-iii
- liquidity-crisis
- credit-default-swaps
- maturity_transformation
- collateralized-debt-obligations
- garch-models
- interest-rate-swaps
- mathematical-finance
- interbank_market
- course-material
- bank-regulation
- reserves
- fdic
- shadow-banking
- credit-risk
- quantitative-implementation
- solution
- treasury-bonds
- bank_liquidity
- banking
- stress-testing
- financial-crisis
- liquidity-risk
- corporate-bonds
- diamond_dybvig
- deposit-insurance
- financial-intermediation
- liquidity_risk
- basel
- liquidity-coverage-ratio
- harvard-business-review
title: A Primer on Bank Liquidity
---

# A Primer on Bank Liquidity

Primer on Bank Liquidity | Bank Liquidity]]

Financial Intermediation]]

**WHAT IS BANK LIQUIDITY?**

The term “liquidity” has two related but distinct meanings in finance. An asset is liquid if it can be bought or sold quickly in size without moving the price. An institution is liquid if it can meet its scheduled payments or demands for funds without incurring high costs. Bank liquidity refers to the latter meaning but also depends on the former. A bank is liquid if it can repay borrowers when due,  meet deposit withdrawals,  and satisfy draws on lines of credit that it has extended without paying inordinately in funding markets or selling assets at fire-sale prices. Moreover,  because banks provide funding to each other,  liquidity problems at one bank can quickly spillover to other banks.

Illiquidity (being unable to make payments when due) is not the same as insolvency (having assets that are worth less than your liabilities). In fact,  often when economists discuss illiquidity they are specifically considering the situation where a bank is illiquid but solvent. In that case,  illiquidity is caused by a market failure—everybody would get paid and the bank would be able to avoid a default if it could simply monetize the assets that it has quickly at near their actual value. In reality,  it is often difficult to distinguish between an illiquid bank and an insolvent bank,  an important reason why liquidity requirements are needed.

Banking at its core is the business of funding illiquid assets—loans—with highly liquid liabilities—deposits. That is,  banks engage in liquidity transformation (often called “maturity transformation”) and are inherently illiquid. In a seminal paper,  Douglas Diamond and Philip Dybvig (1983) showed what any student of history knows: banks are subject to random,  self-fulfilling runs. If depositors think other depositors are going to withdraw their funds,  all depositors have an incentive to move first. In that case,  everyone withdraws and the bank fails.

Moreover,  Diamond and Dybvig,  and historical precedent,  show that such runs are contagious. If one bank fails (despite being sound),  depositors will worry more about their bank,  pull their funding,  and the run can turn into a panic. In turn,  as banks cease to make loans in order to pay depositors,  the panic is transmitted into the real economy.

Banks deal with their inherent illiquidity first and foremost through borrowing and lending in the interbank market. At any given point in time,  some banks will need liquidity while others will have extra,  and liquidity is distributed between them using short term,  typically overnight,  loans.

Banks also maintain precautionary savings to meet liquidity needs. Often,  those savings take the form of deposits at the Federal Reserve,  also known as “reserves;” they also include other safe and liquid assets and deposits at,  or overnight loans to,  other financial institutions. But a bank can never fully insulate itself from liquidity risk by holding stockpiles of liquid assets unless it either stops taking deposits,  stops making loans to businesses and households,  or both.

Because banks serve a valuable purpose as deposit-takers and loan-makers,  and because a liquidity failure of a solvent bank is unnecessary,  costly,  and contagious,  regulators have taken a number of steps to ensure the liquidity of banks. First,  banks are required to hold percentages of their deposits as “required reserves” at the central bank. Second,  the FDIC insures bank deposits up to $250,  000. Third,  the Federal Reserve can act as a lender of last resort against good collateral if necessary. However,  after the 2007-2009 financial crisis,  regulators did not think these approaches were sufficient.

**WHAT ARE THE CURRENT LIQUIDITY REQUIREMENTS?**

As part of the post-crisis reforms,  the Basel Committee on Banking Supervision created the first global liquidity standard: the “Liquidity Coverage Ratio” (LCR). The LCR requires the largest banks to maintain “high-quality liquid assets” (HQLA) sufficient to sustain a liquidity freeze up to 30 days. Because of their simpler structure,  medium-sized banks are required to hold HQLA in an amount intended to cover 21 days of stress.

Additional post-crisis reforms have also addressed Primer on Bank Liquidity | bank liquidity]]. Larger banks are required to stress test their liquidity at least once a month over multiple horizons and report the results to their supervisor. They are also required to maintain stockpiles of liquid assets to facilitate an orderly resolution in the event that they fail. And the largest banks participate in an annual horizontal review of their liquidity conducted by the Federal Reserve.

In part to comply with the LCR and other new requirements,  and in part because of greater caution,  U.S. bank holding companies now hold nearly 20 percent of their assets,  or $2¾ trillion as HQLA,  up from less than 5 percent going into the crisis. There are three categories of HQLA under the LCR: level 1 assets,  level 2A assets and level 2B assets. U.S. banks hold almost entirely level 1 and level 2B assets. Level 1 assets include reserve balances,  Treasury securities,  and other securities that are explicitly guaranteed by the full faith and credit of the U.S. government. Level 2A assets comprise government-sponsored enterprise (GSE) debt,  and GSE-sponsored mortgage-backed securities.md). Under the LCR,  level 2A assets receive a 15 percent haircut,  and those amounts must be less than 40 percent of HQLA for each bank.

 ![500](https://bpi.com/wp-content/uploads/2019/08/HQLA-Calculations-1024x732.png)

**WHAT ARE THE COSTS AND BENEFITS OF LIQUIDITY REQUIREMENTS?**

A lot more research is needed on the optimal level of liquidity requirements,  in part because the costs and benefits are difficult to identify. At a very basic level,  as discussed above,  liquidity regulations,  by design,  limit the ability of banks to engage in liquidity transformation. To satisfy the requirements,  banks must reduce lending and instead hold government securities or deposits at the Fed,  or they must fund themselves with costlier longer-term liabilities,  or both. A 2016 _study_ by the Bank for International Settlements found that the LCR requirement results in a 3-6 percent permanent decline in the level of bank lending. Regarding benefits,  a 2010 BIS _study_ found that compliance with the post-crisis liquidity requirements will reduce the annual probability of another financial crisis by about 20 basis points. A 2016 Fed working paper (_Carlson,       Duygan-Bump,       and Nelson_) argues that the benefit of liquidity regulations is buying time for a bank experiencing liquidity difficulty to address the situation and for the Fed to ensure that the institution is solvent before providing lender of last resort assistance

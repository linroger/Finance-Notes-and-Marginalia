---
aliases:
- Financial Analysis Intro
- Financial Statement Analysis
- Introduction to Valuation
- Week 1
cssclasses:
- academia
enhanced: true
enhancement_date: '2025-11-06'
enhancement_id: batch03-bbe811
key_concepts:
- Apt
- Liquidity coverage ratio and net stable funding ratio
- Regulatory changes and market structure evolution
- Cox-Ross-Rubinstein parameter specification
- Extensions to multi-factor CAPM models
- Duration and convexity analysis for bond portfolio management
- Active portfolio management and performance attribution
- Stress testing and supervisory review processes
- Reduced-form models and intensity-based approaches
- Computational implementation of binomial option pricing
- Option Greeks and portfolio risk management
- Risk budgeting and portfolio construction techniques
- Capital Asset Pricing Model and beta estimation
- Capital Asset Pricing Model and expected returns
- Discounted cash flow (DCF) methodology fundamentals
- Vega and volatility risk management
- Leverage ratio and large exposures
- Business model analysis and its relationship to financial performance
- 'Hedge fund strategies: long-short, market neutral, event-driven'
- Operating vs financing activities separation in financial analysis
- Swap spread and credit risk considerations
- Capital structure theory and optimal debt levels
- Mathematical Finance
- Leveraged buyout financial modeling and returns
- GARCH models and volatility forecasting
- Value driver model for simplified financial forecasting
- Deposit insurance and systemic risk prevention
- cost of capital estimation
- Accounting shenanigans and their impact on financial analysis
- Fixed-for-floating swap cash flows and valuation
- Course Material
- Risk-weighted assets and capital adequacy ratios
- Security Market Line and beta measurement
- Free cash flow computation and forecasting techniques
- Fundamental analysis frameworks and valuation approaches
- Basel III capital and liquidity standards development
- Margin lending and leverage in alternative investments
- Case Study
- fundamental valuation methods
- Interest rate swap pricing and valuation
- Basel III regulatory framework and capital requirements
- ESG integration in portfolio management
- Variance swaps and volatility trading strategies
- Convergence of binomial model to Black-Scholes solution
- ROE decomposition and financial ratio interpretation
- Moats (competitive advantages) and mean reversion patterns
- Economic profit sustainability and competitive advantage
- Binomial option pricing model with multiple time steps
- Delta hedging strategies in options portfolio management
- American option pricing in binomial trees
- Gamma and convexity adjustments
- Capital Structure
- Credit risk modeling and portfolio correlation analysis
- Credit risk assessment and loan portfolio management
- Delta hedging and the replication argument
- Cross-currency basis swaps and funding
- Currency hedging strategies for global portfolios
- Commercial bank business model and revenue streams
- Market portfolio and risk-free rate assumptions
- Empirical tests and anomalies in CAPM
tags:
- basel-iii
- binomial-model
- bank-regulation
- capm
- cash-flow-statement
- corporate_finance
- case-study
- apt
- comparable-analysis
- value-at-risk
- valuation
- credit-risk
- duration-convexity
- solution
- private-equity
- wacc
- pe-ratio
- depreciation
- cost-of-capital
- capital-budgeting
- ebitda-multiple
- deposit-insurance
- vasicek-model
- income-statement
- roe
- garch-models
- interest-rate-swaps
- mathematical-finance
- balance-sheet
- course-material
- accounting_analysis
- capital-structure
- roic
- amortization
- greeks
- exchange-rates
- net-income
- hedge-funds
- ebitda
- leveraged-buyouts
- quantitative-implementation
- treasury-bonds
- systemic-risk
- roa
- ev
- distressed-debt
- dcf-valuation
- harvard-business-review
- mean-reversion
title: Week 1 Introduction to Financial Analysis
---

# Week 1 Introduction to Financial Analysis

## Introduction Game Plan for Today

- What matters in fundamental analysis and valuation
	- Core issues
	- Framework and setting the stage for whole course
- Why is understanding the business model so important?
	- Introduce idea of value driver model: Keep it simple
	- Sustainability of economic profits
- Importance of "moats" and how they relate to mean reversion
	- Why not just use multiples?
	- Recent trends and what they mean for financial analysis and valuation

## Core Issues in Valuation

 !500

### The Basis of Valuation: Discounted Dividend Model

- Why do we rarely use a discounted dividend model?
	- Dividends are easy to forecast – so why not?
- One problem: Many companies do not pay dividends (but still have value)
- Discounted dividend model just pushes the valuation problem into the future

## So What Do We Do Instead?

- We use the cash flows between the firm and its product and service markets
‒ Forecast revenues
‒ Forecast product or service costs
‒ Forecast necessary investments
- We then convert these forecasts into free cash flows
‒ This is essentially the DCF model
- Using the cash flows with the markets leads to an entity model where you first determine the value of the entire entity (or enterprise)
-  !500

## What Are the Core Challenges in Valuation?

- Estimating (or forecasting) the future cash flows
	- Especially in the long‐run
		- Sustainability and growth of the future cash flows
	- Action is not in the discount factor
- What does it take to estimate the future cash flows?
	- Understanding the business model
	- Understanding what drives value for the firm
	- Understanding "moats" and their link to sustainability
- Keep it simple
	- It is not about a complicated Excel model
	- Easy to lose "forest for the trees"

## Accounting Analysis and Shenanigans

## Central Role of Accounting

- Allow us to understand the business model and the economics of the firm
	- Profitability and, in particular, value creation
	- Connects the narrative and the numbers
- Financial statements provide a starting point
	- Past trends are often the basis for forecasts
	- Savvy accounting analysis needed
		- Accounting shenanigans are used to manage expectations
- Analyzing financial statements is at the core of valuation
	- This is why this course is an accounting class!

## A Few Reminders About Accounting Analysis

- Assume that you are familiar with basic accounting ratios
	- ROE decomposition
	- Profit margin
	- Asset turnover
- Common ratio cheat sheet (on Canvas)
- Separating operating and financing activities
	- Excess cash (e.g., Apple) & interest revenue, non‐operating assets
	- Basic idea: Understand and analyze core business
	- We use ROIC rather than ROA
	- Invested capital = Operating assets – operating liabilities
	- See Koller et al. Chapter 11 (useful guidance)
- Check out Tutorial Review Slides on Canvas

## Why Do Accounting Shenanigans Matter?

- Accounting fraud is a very negative event for firm value
	- Firms that disclose misstatements or misrepresentation suffer initial declines around 25% and eventually lose on average close to 40% of their value
- But typically the idea of financial analysis is not to detect fraud
	- This is not a forensic accounting class
- Companies try to influence or manage market expectations
	- Distorted view of a firm's underlying economics
	- Affects your forecasts and hence the valuation
		- Base‐year fixation

## Example: Change in Amortization Method

From 10K: ExampleCo rents equipment to customers. For the fiscal year 2013, ExampleCo completed a review of its rental equipment amortization methodology and updated the methodology in order to add greater precision to cost amortization. The previous method recognized accelerated amortization of costs at a rate faster than the decline in the equipment value due to the recognition of charges in addition to the normal rental curve amortization to account for potential damage. The Company's most recent analysis has shown that its amortization curves can reasonably capture the effect of potential damage and therefore eliminates the need for additional charges and provides a better correlation of costs to revenue. The modified approach to amortizing the cost of the equipment is based on updated rental curves, which incorporate damage estimates, and provides a more systematic method for recognizing the replacement costs. The Company anticipates this new method will better align the recognition of costs with related revenue.

The effect of this change resulted in a reduction of product costs, as reported in operating expenses. The change resulted in a corresponding increase to the balance of our rental equipment inventory. For the fiscal year 2013, the change resulted in a benefit to Net Income of $15 million or $0.10 in basic earnings per share.

 !500

## Understanding the Business Model is Key

- We consider different business models (or industry) each week
	- Try to understand how a business creates value
- Class is not just about "valuation" but also about value creation
	- Consider the value proposition
		- Tools of this class can be used to evaluate different strategies
	- Competition and impact on value creation
- Business model maps into the accounting numbers (see next slide)

## Business Models Differ in Their Numbers

- Industries below differ in key ratios like their profit margin (PM), leverage, operating cycle or market‐to‐book ratio
	- Key ratios reflect differences in the business models or industries
RNOA = Return on Net Operating Assets ≈ ROIC

- But note that RNOA/ROIC is of similar magnitude across industries
	- Firms differ in how they create value
 !500

## Profit Margin vs. Asset Turnover

AVERAGE INDUSTRY NOA TURNOVER AND PM 2011‐2016

 !500

You can find this graph and the underlying industry data on Canvas (see Useful Material folder)

## Value Driver Model for Forecasting FCF

## Value Drivers and Key Performance Indicators (KPIs)

 !500

 !500

### Basic Idea of Value Driver Model

- Focus on the key value drivers in forecasting FCF
	- You do not have to forecast each line item from IS or BS
	- Spend most of your time on the key value drivers
		- Back those up with additional data
- Connect your understanding of the industry and business model as well as changes in strategy to the key value drivers: e.g.,
	- New marketing strategy leads to margin improvements
	- Synergies improve operating margins
	- Better supply‐chain management leads to turnover improvements
- Key idea:
	- A few parameters are enough to estimate the FCF
	- You want to "nail" those

## Illustration of (Simple) Value Driver Model

- Simple alternative to forecasting detailed line items
	- Essentially hard wire line items in your model
Revenues Operating margin
- Focus on key parameters:
	- Revenue growth
	- Operating margin (and tax rate)
	- Investment rate (or asset turnover)
- You can bring in other businessmodel specific drivers
	- Connect them to three main drivers
 !500

## Example of Simple Value Driver Model

 !500

- Sales growth estimates (yoy): 1.2%, 2%, 2%, 2.2%
- Margin and NOA turnover: constant
- Your turnover forecast pins down your forecasted NOA (and hence investments)
	- ∆NOA is change in investment = required net investment

## NOPAT to FCF: Adjusting for Non-Cash Items

- How does the change in NOA adjust for non‐cash items?
	- Consider change in Net PPE
	- The change in Net PPE is Change Gross PPE – Change Accumulated Depreciation
	- Subtracting the change in Net PPE from NOPAT means:
		- Subtracting the change in Gross PPE (e.g., new stuff bought)
		- Adding back depreciation of the period (i.e., undoing non‐cash items)
- Consider a firm with 1000 in Net PPE (Gross PPE ‐ Accumulated Depreciation)
	- Suppose the firm has depreciation of 200 and buys new PPE for 400
- Avenue 1: Directly adjust investment and depreciation
- To go from NOPAT to FCF, we want to subtract the 400 in investment and add back the 200 in depreciation
	- Cash used up is 200 = 400 – 200
- Avenue 2: Adjust the net change in PPE
	- New Net PPE is 1200
	- Change in Net PPE is 200 = 1200 – 1000
		- Non‐cash items are automatically adjusted when subtracting the change in NOA

## Summary: Valuation Sequence

 !500

Take the narrative apart and bring it into the valuation. By the time you are done, each part of the narrative should have a place in your numbers and each number should be backed up by a portion of the story.

Listen to people who know the business better than you do and use their suggestions to fine tune your narrative and perhaps even alter it. Work out the effects on value of alternative narratives for the company.

## Detailed Forecasting vs. Value-Driver Approach

- Most common: Detailed (three‐statement) approach
‒ Pro‐forma income statement, balance sheet and cash flow statement
‒ More flexibility to capture specific changes, events, and trends
‒ Be careful about internal consistency

- Value‐driver approach
‒ Focuses on key forecasts & business model
‒ Less prone to inconsistencies

- Could combine the two approaches in three‐stage model
‒ You can adjust the level of detail over time

## Three-Stage Model

 !500

ROIC

Time

Time segment

- Use varying levels of detail
	- Forecast period 1: More detail (e.g., line items)
	- Forecast period 2: Key value drivers and fading
	- TV period: Typically perpetuity (perhaps with growth)
		- FCF in TV can also be determined in terms of key value drivers (Week 3)

## Near-Term Flows as % of Value for Two Examples

 !500

## Near-Term Cash Flows vs. Terminal Value

- Forecasted cash flows (or dividends) over the next 2‐3 years comprise a relatively
small percentage of overall value
- For model with short forecast horizon:
	- The bulk of the value resides in the terminal value
	- Valuation is very sensitive to terminal value assumptions
		- Steady‐state FCF, growth rate, WACC
- What is the purpose of the second stage?
 - NORMALIZATION
	 - Fades the FCF to sustainable level before using TV formula
- Almost all the action is in the long run, not the near term
	- This is the problem with multiples – focus on the near term (e.g., forward E)
	- Market excesses tend to manifest in unrealistic TV valuations 

## Importance of Moats Economic Moats

- How do we know a firm create value?
- It generates a return above its cost of capital
	- Economic profit (ROIC > WACC)
- Ability to do so follows from its strategy and competitive position
Competitive advantage and economic moats:
- "The key to investing is … determining the competitive advantage of any given company and, above all, the durability of that advantage. The products or services that have wide, sustainable moats around them are the ones that deliver rewards to investors."
(Warren Buffett, Fortune 1999)
- Moat concept combines economic profit and competitive advantage
- Why does the "durability" of the advantage matter?
- Morningstar uses moat concept and assigns:
	- Narrow moat: 10 years
	- Wide moat: 20 years
- Why not focus on long‐term (revenue) growth?

## Economic Moats (Cont.)

- Key questions in analyzing companies
	- What is the source of the competitive advantage?
	- How sustainable is the competitive advantage?
- Moat sources (i.e., reasons why ROIC > WACC)
	- Intangible assets (e.g., brands, patents, government licenses)
	- Cost advantage (e.g., economies of scale, location)
	- Switching costs (e.g., operating systems)
	- Network effects (value of services increases as more people use the service)
	- Efficient scale (limited market is already served by one or just a few companies)
- Economic moats have a life cycle and are changing over time
	- Competition can make moats unstable or erode them (e.g., P&G, SAP)
	- Are moats sustainable or narrowing? 

## Competition and Returns (or Economic Profits)

 !500

- High returns attract competitors
	- Competitors settle for lower returns that are still attractive
- Over time, competition drives ROIC down to the cost of capital

## Moats and the Decay in the Spread

 !500

- Economic profit declines on average
	- But not necessarily for all companies (at the same rate)
- Moats can play an important role in slowing down the decay in the spread (i.e., difference between ROIC and WACC)

## Decay in Industry Profitability: High vs. Low Competition

 !500

Source: Li, Feng, Russell Lundholm, and Michael Minnis. "A measure of competition based on 10‐K filings." Journal of Accounting Research 51, no. 2 (2013): 399‐436.

## Mean Reversion in Sales Growth

 !500

### Mean Reversion in ROIC

 !500

### Mean Reversion in Operating Margin

 !500

### Mean Reversion in Asset Turnover

 !500

## Multiples Review and Key Challenges

## Multiples

- "KEEP IT SIMPLE"
	- So why not just use multiples 
	- a PE ratio is simple?
 - MULTIPLES CAN BE A GOOD STARTING POINT
	- Gauge value of current operations
	- Easy to capitalize consensus earnings forecast
		- If consensus is $1.50 per share and PE ratio for peer group is 20, then share price should be around $30
	- What is key for this valuation?

## One Issue: Multiples Typically Focus on the Near Term
- That is in contrast to what we discussed earlier
- When you try to build in the long‐run, multiples become tricky

## Basic Idea
- PE ratio is essentially based on a perpetuity
- Perpetuity: P = CF/r (where CF is cash flow to equity)
	- Earnings predict future cash flows
		- Includes replacement investments (or maintenance)
	- You can view earnings as an estimate of "normalized" cash flow to equity in steady state (rather than the dividend)
	- Thus: P = E/r P/E = 1/r
		- This is just the simplest representation
- We can add other factors (e.g., growth)
	- P/E = 1/(r‐g)
	- PEG ratio
- We can also capitalize different flow variables (e.g., EBITDA)

## Challenges for Multiples
- Multiple is essentially a valuation model with a forecast horizon of T=1
	- One‐year forward PE ratio
	- Complexity of valuation has not disappeared – all 'crammed' into:
		- Multiple (reflects growth and cost of capital)
		- The "E" (needs to be normalized to capture long‐run value creation)
- For multiples, comparability is key
	- Challenge: Finding comparables and adjusting their earnings
- Adjustments are much more important for multiples (than DCF)
	- Differences in strategy and in accounting methods
		- Acquisitions, operating leases, pensions, stock compensation, etc.
	- Earnings need to be normalized (e.g., adjusted for non‐recurring items)
		- Discontinued operations, impairments, restructuring, etc.

## Example: PE Ratios and Non-Recurring Items
- COMPARING PE RATIOS IN THE NEWSPAPER INDUSTRY
 !500

## Example: PE Ratios After Adjustments

 !500

## Which Multiple Should We Use?
- Koller et al. recommend EBITA or NOPAT multiple (see Ch. 18)
	- Gives you an entity value
		- Just like EV/EBITDA multiple
	- Need to subtract financial debt and add financial assets to get to equity value
- By not excluding depreciation, EBITA makes firms with in‐house production more comparable to firms with outsourcing
- Why use a number "higher up" in the income statement?
	- Tends to be less distorted by non‐recurring charges
	- EBITA or NOPAT do not commingle operating and financing activities
		- Less distorted by differences in capital structure across companies
		- For PE ratio, comparables need to have similar capital structure (see next slide)

## Illustrating the Impact of Capital Structure
- EV/EBITA is not affected by leverage but PE is
- Note that you cannot even sign the effect of leverage on the PE ratio
 !500

## Multiples: Summary
- Relatively quick and "easy"
	- Assumes other firms are "comparable" and their securities are correctly priced
	- Provides a useful "plausibility check" for DCF model
- Not based on independent fundamental analysis
	- Not 'anchored' in value creation
- Key messages:
	- Multiples only seemingly simple
	- Comparability is key
	- Entity multiples make it easier to find comparables
- These message also apply to multiples used in terminal value calculations
	- We come back to TV issues in Week 3

## Common Mistakes in Analyst Reports and DCF Models
- Heavy reliance on multiples

## See "Useful Material"
- Shortcomings in DCF models:
	- Forecast horizon is too short
	- Implausible terminal value
	- Growth and investment are not connected or incompatible
	- Other liabilities (e.g., leases, stock compensation) are not accounted for
	- Double counting
	- No scenarios
- Green, Hand and Zhang (2016) analyze sample of DCF models in analyst reports
	- Find on average 3 mistakes and 4 questionable judgments (e.g., TV)
	- Valuation effect ranges from ‐2% to 14%
- Pre‐recordings for this class are designed to help you with some of the technical issues

## Financial Analysis and Valuation
- A valuation model helps you:
	- Link value to fundamentals
	- Quantify the impact of your assumptions
	- Understand where your views differ from the consensus or what is already reflected in the market price
- This class is not about "stock picking" ‐ there are many situations that require fundamental analysis & valuation
	- M&A and FDI
	- Strategy decisions and capital budgeting inside of firms
	- VC and PE portfolio companies
	- Building business models and plans

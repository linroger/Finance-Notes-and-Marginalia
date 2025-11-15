---
academic_level: graduate
aliases:
- DCF
- DDM
- Valuation Methods
- Week 1 Review
cssclasses:
- academia
enhanced: true
enhancement_date: '2025-11-06'
enhancement_id: batch09-000274
key_concepts:
- Options Greeks and sensitivity analysis for risk management
- Duration analysis and interest rate risk management
- Convexity adjustments and yield curve sensitivity
- Weighted Average Cost of Capital (WACC) and firm valuation
- Value at Risk (VaR) and tail risk measurement
- Expected shortfall and coherent risk measures
- Risk preference theory and utility functions
- Sensitivity analysis and Greeks calculation
- 'Valuation Methods: DCF, Comps, and Precedents'
- Basel III Regulatory Framework and Capital Requirements
- Free Cash Flow and Enterprise Value
- Value at Risk and Expected Shortfall
- Company Valuation and Multiple Analysis
- Credit Risk Management and Default Probability
- Expected Loss and Loss Given Default Models
- Comparable Company Analysis and Trading Multiples
- 'Greeks: Delta, Gamma, Theta, and Vega Hedging'
- Regulatory Capital and Stress Testing
- Options Trading Strategies and Risk Management
- Stress Testing and Extreme Value Analysis
- Fama-French Factors and Style Analysis
- Risk Measurement and VaR Backtesting
- Contango, Backwardation, and Roll Yield
- Futures and Forward Contracts in Financial Markets
- Hedge Strategies and Basis Risk Management
- Liquidity Coverage Ratio and Net Stable Funding
- Option Valuation and Exercise Strategies
- Credit Spreads and Rating Migration Analysis
- Factor Models and Asset Pricing
- Terminal Value and WACC Calculations
- Discounted Cash Flow Valuation Models
- Arbitrage Pricing Theory and Multi-Factor Models
professional_application: theoreti
status: active
tags:
- asset-allocation
- capital-structure
- caplet
- cash-flow-distribution
- cash-flow-modeling
- coherent-risk-measure
- conditional-var
- convexity-adjustment
- cost-of-capital
- credit-rating
- dcf-valuation
- debit-valuation-adjustment
- debt-equity-mix
- delta-hedging
- discounted-cash-flow
- leveraged-buyout
- call-options
- terminal-value
- free-cash-flow
- butterfly-spreads
- dcf-analysis
- expected-shortfall
- straddles
- extreme-value-theory
- book-to-market
- backwardation
- net-stable-funding
- volatility-analysis
- style-analysis
- leverage-ratio
- option-strategies
- unexpected-loss
- clearinghouse
- enterprise-value
- arbitrage-pricing-theory
- hedge-ratio
- capital-conservation-buffer
- loss-given-default
- value-factor
- monte-carlo-var
- capital-budgeting
- options-trading
- forward-contracts
- price-to-earnings
- fama-french
- recovery-rate
- parametric-var
- var-methodologies
- historical-var
- contango
- regulatory-capital
- expected-loss
- wacc
- quantitative-finance
- protective-puts
- probabilty-of-default
- roll-yield
- tier-2-capital
- cost-of-debt
- put-options
- countercyclical-buffer
- momentum
- basis-risk
- covered-calls
- ' exposure-at-default'
- stress-testing
- mathematical-finance
- rating-migration
- comparable-analysis
- investment-analysis
- economic-value-added
- value-at-risk
- factor-models
- risk-management
- convergence
- var-backtesting
- sum-of-parts
- strangles
- cost-of-equity
- credit-migration
- default-probability
- marking-to-market
- credit-spreads
- tier-1-capital
- multi-factor-models
- trading-multiples
- iron-condors
- financial-markets
- equity-value
- size-effect
- precedent-transactions
- liquidity-coverage-ratio
- ipo-valuation
- basel-iii
- market-multiple
- futures-contracts
- apt
title: Week 1 Ratio Analysis + Valuation Review
type: course-note
---
--



# Week 1 Ratio Analysis + Valuation Review

## Ratio Analysis Review

We can decompose ROE, a common profitability measure, into operating and financing parts. We use ROIC rather than the more traditional ROA:

 !500

- ROIC captures only operating items whereas ROA commingles operating and non-operating
	- E.g., Net Income (ROA's numerator) includes both sales revenue (operating) and gains on trading securities (non-operating)
	- E.g., total assets (ROA's denominator) includes both inventory (operating) and excess cash and marketable securities (non-operating)
 !500

## Using ROIC

Using ROIC means reclassifying items in the balance sheet and income statement as operating or investing.

 !500

 !500

### Reclassification Process
- Operating items are part of the company's core business and affect the NOPAT.
- Investing items are related to how the business finances its operations and growth.
 !500
### ROIC Deep Dive
A detailed look into ROIC can provide insights into a firm's operational efficiency and profitability.
You can also take a deeper dive into ROIC
 !500
---

- UPS' ROIC advantage over FedEx comes from advantages in both Operating Margin and turnover
- On margin, UPS' benefit is driven by higher reliance on labor (higher compensation/revenues) but lower reliance on equipment (lower purchased transportation/revenues, lower fuel/revenues)
- UPS also has better capital efficiency (invested capital turnover)

**Decomposing ROIC:**
$$ \text{Return on Invested Capital (ROIC)} = \frac{\text{NOPAT}}{\text{Avg. Invested Capital}} $$
$$ \text{NOPAT} = \text{NI} + (1 - \text{t}) * \text{Interest} $$
$$ \text{ROIC} = \text{Post-tax Operating Profit Margin} \times \text{Invested Capital Turnover} $$
$$ \text{Post-tax Operating Profit Margin} = \frac{\text{NOPAT}}{\text{Revenue}} $$
$$ \text{Invested Capital Turnover} = \frac{\text{Revenue}}{\text{Avg. Invested Capital}} $$
$$
\begin{array}{ | l | l | }
\hline
\textbf{Ratio} & \textbf{Definition} \\ \hline
\text{Return on equity (ROE)} & \frac{\text{Net income available for common}}{\text{Avg. common shareholders' equity}} \\ \hline
\text{Return on invested capital (ROIC)} & \frac{\text{NOPAT}}{\text{Avg. invested capital}} \\ \hline
\text{Return on newly invested capital (RONIC)} & \frac{\text{NOPAT}_{t+1} - \text{NOPAT}_{t}}{\text{Invested capital}_{t+1} - \text{Invested capital}_{t}} \\ \hline
\text{Invested capital turnover} & \frac{\text{Revenue}}{\text{Avg. invested capital}} \\ \hline
\text{Total asset turnover} & \frac{\text{Revenue}}{\text{Avg. total assets}} \\ \hline
\text{Fixed asset turnover} & \frac{\text{Revenue}}{\text{Avg. fixed assets}} \\ \hline
\text{Net operating profit after tax (NOPAT) margin} & \frac{\text{Operating income (or EBIT)} \times (1-\text{tax rate})}{\text{Revenue}} \\ \hline
\text{Days sales outstanding} & \frac{\text{Accounts receivable}}{\text{Revenue} / 365} \\ \hline
\text{Days payables outstanding} & \frac{\text{Accounts payable}}{\text{COGS} / 365} \\ \hline
\text{Inventory turns} & \frac{\text{COGS}}{\text{Avg. inventory}} \\ \hline
\end{array}
$$

## Valuation Review

### Valuation Basics
$$V_0=\sum_{t=1}^\infty\frac{Projected\textit{ Future Payoffs}_t}{(l[^2]+Discount\text{ Rate})^t}$$

[^1]: Value today (i.e., t = 0)
[^1]: "Flows" expected to be received in the future
	- May be received in one lump sum, in a constant stream, or in different amounts each year
[^1]: Discount rate applied to future flows, representing:
	- Time value of money
		 - Consumption tomorrow instead of consumption today
		 - Constant rate for all assets
	- Risk of the flows
		 - Varies by type of flow (capital)

### Valuation Basics: Dividend Discount Model ("DDM")

- In theory, the dividend discount model is what underpins value:
-  !500
- However, the DDM's usefulness relies heavily on the ability to forecast future dividends
	- Dividends are chosen by management and many companies do not pay dividends
	- In practice, we rarely use the DDM

### Overview of Common Valuation Methods

Instead, we use measures of flows between the firm and the market(s), e.g., free cash flow, because these flows can be better estimated than dividends.

 !500

## Enterprise vs. Equity Method Valuation

- Enterprise valuation models value the flows (cash flows, earnings, etc.) due to all investors (i.e., both equity and debt holders)
- Equity valuation models value the flows due to equity holders only
- The two models can be bridged by:
 !500
## Enterprise DCF Review

- This model discounts **free cash flow** (i.e., cash flow generated by business operations - less any reinvestment back into the business - that is available to all investors) at the weighted average cost of capital (i.e., a blend of the cost of debt and the cost of equity)
- Ideally used to value companies that will maintain their capital structure at a target leverage ratio
 !500
### Four-Part Process

[^1]: **Free Cash Flow ("FCF")**
	- Forecast operating line items and line items affecting invested capital
	- Calculate net operating profit after tax ("NOPAT") and changes to invested capital
	- Calculate projected FCF

	> Note: McKinsey valuation book uses net operating profit less adjusted taxes ("NOPLAT"), which 1) adjusts for cash taxes on Operating Income and 2) treats deferred taxes as non-operating items. NOPAT treats deferred taxes as operating, but as long as tax expense and deferred taxes are treated consistently, using NOPAT vs NOPLAT leads to the same results.

[^1]: **Discounting**
	- Calculate the present value of FCFs in the explicit forecast period by discounting the forecasted FCFs with WACC
	- Apply a mid-year adjustment to the PVs as appropriate

[^1]: **Continuing Value**
	- Continuing value represents the value of the firm's FCFs after the explicit forecast period
	- It is typically a perpetuity
	- With growth & reinvestment, continuing value is defined as:

	$$\frac{FCF_{T+1}}{WACC - g}$$

	Where

	 - $FCF_{T+1}$ is the FCF in the first year after the explicit forecast period
	 - $WACC$ is the weighted average cost of capital
	 - $g$ is the long-term growth rate
	- Further discounted by WACC to determine present value of continuing value

[^1]: **Equity Value Calculation**
	- Sum the present values of the forecasted FCFs and the continuing value
	- (+) the present value of non-operating assets (e.g., equity investments) if applicable
	- (-) net debt (debt and debt equivalents minus cash and cash equivalents)
	- (-) the value of preferred stock and noncontrolling interest if applicable
	- Estimated price per share = equity value divided by the number of shares outstanding

---

## Enterprise DCF Review (Cont.) Free Cash Flow ("FCF")

At a high level, free cash flow is calculated as:
$$\text{FCF} = \text{NOPAT} + \text{D\&A} - \text{increase in non-cash WC} - \text{capital expenditures} - \text{other adjustments to invested capital}$$

-  !500

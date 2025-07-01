---
title: Week 1 Ratio Analysis + Valuation Review
cssclasses:
  - academia
tags:
  - dividend_discount_model
  - enterprise_valuation
  - equity_valuation
  - free_cash_flow
  - ratio_analysis
  - roic
  - valuation
  - wacc
  - financial_analysis
  - corporate_finance
aliases:
  - DCF
  - DDM
  - Valuation Methods
  - Week 1 Review
key_concepts:
  - Capital structure impact on valuation methods
  - Continuing value calculation techniques
  - Discount rate components and calculation
  - Dividend discount model limitations
  - Economic profit model applications
  - Enterprise DCF process and methodology
  - Enterprise vs equity valuation models
  - Equity value determination from enterprise value
  - Financial ratio analysis fundamentals
  - Free cash flow calculation and components
  - Mid-year adjustment technique
  - NOPAT and FCF relationship
  - Non-operating assets valuation 
  - Operating vs investing classification
  - ROE decomposition and drivers
  - ROIC as a measure of operational efficiency
  - ROIC vs ROA differences and applications
  - Terminal value estimation methods
  - Valuation basics and principles
  - Weighted average cost of capital (WACC)
---

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

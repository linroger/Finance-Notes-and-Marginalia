---
aliases:
- DCF
- Discounted Cash Flow
- Enterprise Value
- FCF
cssclasses:
- academia
key_concepts:
- Efficient market hypothesis
- Market anomalies and patterns
- Price discovery and information
- Option pricing theory and Black-Scholes model
- Options Greeks and risk management
- Call and put option strategies
- Interest rate swaps and valuation
- Currency and cross-currency swaps
- Swap spreads and basis trading
- Value at Risk (VaR) and stress testing
- Portfolio risk metrics and measures
- Hedging strategies and effectiveness
- Capital Asset Pricing Model (CAPM)
- Arbitrage Pricing Theory (APT)
- Multi-factor risk models
- DCF Breakdown and financial analysis
- DCF Breakdown in modern finance
- Applications of DCF Breakdown
- 'Case study: DCF Breakdown'
tags:
- income statement
- discount
- swaps
- options
- var
- factor-models
- delta
- capm
- risk
- balance sheet
- beta
- valuation
- irs
- risk-management
- market-efficiency
title: DCF Breakdown
---

# DCF Breakdown

### 1. Preparation and Assumptions
1.1. **Gather Financial Statements**
- Balance Sheet
- Income Statement
- Cash Flow Statement

[^1]: 2. **Historical Analysis**
- Analyze past performance to understand trends.

[^1]: 3. **Assumptions for Future Projections**
- Revenue Growth Rate
- Operating Margin Improvements
- Capital Expenditures
- Changes in Working Capital
- Tax Rate

### 2. Forecasting Free Cash Flow
[^2]: 1. **Forecast Revenue and Expenses**
- Project future revenues and expenses based on historical trends and assumptions.

[^2]: 2. **Calculate Earnings Before Interest and Taxes (EBIT)**
- $$ \text{EBIT} = \text{Revenue} - \text{Operating Expenses} - \text{Depreciation} $$

[^2]: 3. **Adjust for Taxes to Get NOPAT (Net Operating Profit After Taxes)**
- $$ \text{NOPAT} = \text{EBIT} \times (1 - \text{Tax Rate}) $$

[^2]: 4. **Non-Cash Adjustments**
- Add back non-cash expenses (e.g., Depreciation & Amortization).

[^2]: 5. **Changes in Working Capital**
- Calculate the change in working capital and adjust the cash flow accordingly.
- $$ \Delta \text{Working Capital} = \text{Current Year Working Capital} - \text{Previous Year Working Capital} $$

[^2]: 6. **Capital Expenditures (CapEx)**
- Subtract capital expenditures to get Free Cash Flow (FCF).
- $$ \text{FCF} = \text{NOPAT} + \text{Depreciation} - \Delta \text{Working Capital} - \text{CapEx} $$

### 3. Discount Rate Determination
[^3]: 1. **Weighted Average Cost of Capital (WACC) for Firm Valuation**
- $$ \text{WACC} = \frac{E}{V} \times Re + \frac{D}{V} \times Rd \times (1 - Tc) $$
- Where:
  - $E$ = Market value of the equity
  - $D$ = Market value of the debt
  - $V$ = $E + D$
  - $Re$ = Cost of equity
  - $Rd$ = Cost of debt
  - $Tc$ = Corporate tax rate

[^3]: 2. **Cost of Equity (Using CAPM)**
- $$ Re = Rf + \beta \times (Rm - Rf) $$
- Where:
  - $Rf$ = Risk-free rate
  - $\beta$ = Beta of the stock
  - $Rm$ = Expected market return

### 4. Forecasting and Discounting Cash Flows
[^4]: 1. **Forecasting Cash Flows**
- Project the free cash flows over a 5 to 10 year period based on the assumptions.

[^4]: 2. **Terminal Value Calculation**
- Gordon Growth Model: $$ \text{TV} = \frac{\text{FCF}_{n+1}}{(WACC - g)} $$
- Where:
  - $g$ = growth rate to perpetuity
  - $FCF_{n+1}$ = Free cash flow in the first year beyond the forecast period

[^4]: 3. **Discount Cash Flows and Terminal Value to Present Value**
- $$ \text{DCF} = \sum_{t=1}^{n} \frac{\text{FCF}_t}{(1+WACC)^t} + \frac{\text{TV}}{(1+WACC)^n} $$

### 5. Valuation and Sensitivity Analysis
[^5]: 1. **Calculate Enterprise Value**
- Sum of the present values of forecasted Free Cash Flows plus the present value of the Terminal Value.

[^5]: 2. **Adjust for Non-Operating Assets**
- Add value of non-operating assets (e.g., investments).

[^5]: 3. **Subtract Debt and Add Cash**
- To find Equity Value: $$ \text{Equity Value} = \text{Enterprise Value} - \text{Debt} + \text{Cash} $$

[^5]: 4. **Sensitivity Analysis**
- Vary key assumptions (WACC, growth rates) to test the sensitivity of the valuation.

### 6. Conclusion and Reporting
- Present your findings, including the valuation range based on the sensitivity analysis.
- Discuss key assumptions and their impact on the valuation.

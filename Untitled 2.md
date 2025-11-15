---
key_concepts:
- Bond pricing and yield curves
- Duration and convexity hedging
- Credit spreads and bond valuation
- Option pricing theory and Black-Scholes model
- Options Greeks and risk management
- Call and put option strategies
- Fixed income securities and markets
- Bond valuation and yield calculation
- Credit analysis and spread decomposition
- Financial accounting standards
- GAAP and IFRS differences
- Mark-to-market accounting
- Futures and forwards contract mechanics
- Cash-and-carry arbitrage
- Basis trading and roll strategies
- Untitled 2 and financial analysis
- Untitled 2 in modern finance
- Applications of Untitled 2
- 'Case study: Untitled 2'
- Discounted Cash Flow valuation methodology
- Delta hedging strategies in options markets
- Ev Ebitda in financial markets
- Free Cash Flow in financial markets
- Market liquidity analysis and liquidity risk
- Risk Free in financial markets
- Spot Rate in financial markets
- Term Structure in financial markets
- Volatility modeling and implied volatility surfaces
- Yield Curve in financial markets
- Financial markets and instrument analysis
- Quantitative finance and mathematical modeling
- Risk management and hedging strategies
- Investment analysis and portfolio theory
- Capital markets and trading strategies
tags:
- delta
- efficiency
- risk-free
- volatility
- multiple
- basis
- energy
- wacc
- implied
- swap
- yield-curve
- gaap
- free-cash-flow
- pricing
- dcf
- put
- bond
- futures
- bonds
- measure
- ifrs
- valuation
- noise
- options
- comparable
- roe
- maturity
- coupon
- fixed-income
- accounting
- treasury
- yield
enhanced: true
enhancement_date: '2025-11-06'
enhancement_id: batch08-000512
batch: BATCH_AH
processing_agent: Enhancement Agent 8
---



### **1  Time-Series & Price-Level Concepts**

|**Term**|**What it measures**|**How it is produced**|**Why it matters**|
|---|---|---|---|
|**Seasonally Adjusted (SA)**|A data series stripped of predictable calendar patterns—holiday spending, energy usage spikes, harvest cycles.|Statistical filters (e.g., X-13 ARIMA-SEATS) estimate and remove the repeating seasonal component from the raw series.|Lets you compare **month-to-month** or **quarter-to-quarter** changes without having “December shopping season” swamp the signal.|
|**Non-Seasonally Adjusted (NSA)**|The same raw series before adjustment.|Direct survey readings or transaction data.|Use NSA when you _care_ about those seasonal swings (e.g., retail inventory planning) or when reconciling to annual totals—because SA data no longer add up exactly over a full year.|
|**CPI (Consumer Price Index)**|Price level of a representative urban consumption basket (goods _and_ services).|BLS samples ~94 000 prices monthly, weights them by expenditure shares, chains the index.|Benchmark for contracts and many inflation-linked securities.|
|**Headline Inflation**|Year-over-year (or month-over-month) % change in CPI.|Direct arithmetic difference of CPI indexes.|Captures full impact of food & energy volatility—important for _purchasing-power_ reality but noisy for policy.|
|**Core Inflation**|CPI **minus** food and energy (or similar exclusions).|Remove the two most volatile categories; recompute index change.|Used by central banks to gauge underlying trend; correlates better with medium-term wage and policy dynamics.|

---

### **2  Fixed-Income & Rate-Quotation Terms**

1. **Constant-Maturity Yield (CM)**
    
    _Action_: Interpolate the Treasury yield curve to a _fixed_ remaining maturity—e.g., the 10-year CMT.
    
    _Reasoning_: Real-world Treasury issues age; CM yields hold maturity constant so time-series movements isolate _rate_ changes, not “bond aging.”
    
2. **Effective Annual Rate (EAR)**
    
    _Math_:
    
    \text{EAR}\;=\;\bigl(1+\tfrac{r_\text{nom}}{m}\bigr)^{m}-1
    
    where r_\text{nom} is the quoted (nominal) rate and m the compounding frequency.
    
    _Interpretation_: True one-year growth of $1 invested; critical when comparing instruments with different compounding conventions.
    
3. **Par Yield**
    
    The coupon rate that prices a bond **at par (100)** given the current term structure. Solve for c so that
    
    \sum_{i=1}^{n} \frac{c}{(1+y_i)^{t_i}} + \frac{100}{(1+y_n)^{t_n}} = 100
    
    where y_i are spot rates. Used to quote swap curves and fixed-rate leg pricing.
    
4. **Market Rate / Yield-to-Maturity (YTM)**
    
    Internal rate of return equating discounted cash flows to _observed_ price. Moves inversely with price; reflects both risk-free curve and credit/liquidity premia.
    
5. **Investment Basis (also “Bond Equivalent Yield” on bills)**
    
    Annualizes the simple-interest return on a discount instrument:
    
    \text{BEY} = \frac{\text{Face}-\text{Price}}{\text{Price}}\times\frac{365}{\text{Days to Maturity}}
    
    Preferred by money-market investors because it is comparable to coupon-bond yields, unlike the _bank discount_ basis that divides by face value.
    

---

### **3  Operating vs Non-Operating Items**

|**Income Statement Line**|**Typical Components**|**Interpretation**|
|---|---|---|
|**Operating Income (EBIT)**|Revenue − COGS − SG&A − R&D − straight-line D&A tied to core PP&E/intangibles.|Profit from _primary_ business; excludes financing and one-offs.|
|**Operating Expenses**|All costs directly related to producing and selling the firm’s products or services.|Management efficiency lever.|
|**Non-Operating Income / Expense**|Interest, FX gains, pension re-measurement, lawsuit settlement.|Volatile items not driven by day-to-day operations—analysts often exclude for “core” performance metrics.|

---

### **4  Valuation Metrics**

```
flowchart TD
  EV[Enterprise Value] -->|minus Net Debt| EqVal[Equity Market Value]
  EqVal -->|÷ Shares| PPS[Share Price]
  EV --> Debt[Net Debt] & Pref[Preferred / Minority]
  BookVal[Book Value of Equity] --> EqVal
  classDef dash stroke-dasharray: 5 5
  BookVal:::dash
```

- **Book Value (of Equity)** – Historical cost of assets minus liabilities per GAAP/IFRS. Anchors ROE but often far from market perception.
    
- **Market Value (Equity)** – Current share price × shares outstanding; reflects investor expectations.
    
- **Enterprise Value (EV)** – Market equity + net debt + preferred + minority interest − excess cash. Represents the price to acquire the _entire_ operating asset base independent of capital structure. Fundamental for EV/EBITDA, EV/FCF multiples.
    

---

### **5  Cash-Flow Building Blocks**

1. **Plant, Property & Equipment (PP&E)** – Long-lived tangible assets carried at cost minus **accumulated depreciation**.
    
2. **Capital Expenditures (CapEx)** – Cash outflow to acquire/upgrade PP&E or internally generated software. Classified in _investing_ section of the cash-flow statement.
    
3. **Depreciation & Amortization (D&A)**
    
    - _Depreciation_: Allocation of tangible PP&E cost over useful life.
        
    - _Amortization_: Same concept for intangible assets or capitalized software.
        
        Both are **non-cash** charges that reduce book earnings but not cash.
        
    
4. **Free Cash Flow (FCF)**
    
    - **To Firm (FCFF)**:
        
        $$
        
        \text{EBIT}(1-T) + \text{D&A} - \text{CapEx} - \Delta\text{NWC}
        
$$
        
        Cash available to _all_ capital providers.
        
    - **To Equity (FCFE)**: FCFF − after-tax interest + net borrowing.
        
        FCF strips out accounting noise and focuses on discretionary cash the company can reinvest or distribute.
        
    

---

### **Putting It All Together**

- A macro analyst comparing inflation paths should use **seasonally adjusted core CPI** to infer trend, but may revert to **headline NSA data** when assessing consumer sentiment shocks from gasoline prices.
    
- A fixed-income desk prices a swap using the **constant-maturity par curve**, quotes Treasury bills on an **investment basis**, and converts coupon bonds’ YTM to an **effective annual rate** before comparing across markets.
    
- An equity analyst recasts statements to focus on **operating income**, builds a DCF on **FCFF**, discounts at WACC, and cross-checks the implied **enterprise value** against the market’s **EV**, noting gaps between **book** and **market** equity.
    
- Meanwhile, the credit team tracks **CapEx intensity** relative to **D&A** to judge reinvestment needs and the durability of FCF.
    

  

Each concept links mechanical accounting or statistical treatment to a decision-useful economic question—once you see that connection, the definitional details lock into place.



$$\
\begin{aligned}[t]
&\underline{\textbf{Sales}}\\
&\quad -\,\text{Cost of Goods Sold (COGS)}\\
&\quad -\,\text{Selling, General, and Administrative Expenses (SGA)}\\
&\quad\quad -\,\underline{\text{Depreciation and Amortization}}\\
&\quad\quad\quad=\,\underline{\textbf{Earnings Before Interest and Taxes (EBIT)}}\\
&\quad\quad\quad\quad -\,\text{Interest Expense}\\
&\quad\quad\quad\quad=\,\underline{\textbf{Earnings Before Taxes (EBT)}}\\
&\quad\quad\quad\quad\quad -\,\underline{\text{Taxes}}\\
&\quad\quad\quad\quad\quad=\,\underline{\textbf{Net Income Before Extraordinary Items}}
\end{aligned}
$$

$$
\begin{aligned}[l]
\text{Sales}\\
\quad -\,\text{Cost of Goods Sold (COGS)}\\
\quad -\,\text{Selling, General, and Administrative Expenses (SG&A)}\\
\quad -\,\text{Depreciation and Amortization}\\
\underline{=\,\text{Earnings Before Interest and Taxes (EBIT)}}\\
\quad -\,\text{Interest Expense}\\
\underline{=\,\text{Earnings Before Taxes (EBT)}}\\
\quad -\,\text{Taxes}\\
\underline{=\,\text{Net Income Before Extraordinary Items}}
\end{aligned}
$$


$$
\begin{aligned}[l]
\underline{=\,\text{Earnings Before Interest and Taxes (EBIT)}}\\
\quad -\,\text{Taxes on EBIT (e.g.\ 39\%)}\\
\underline{=\,\text{Net Operating Profit After Taxes (NOPAT)}}\\
\quad +\,\text{Depreciation and Amortization + Other Non-Cash Expenses}\\
\quad -\,\text{Capital Expenditures (including acquisitions)}\\
\quad -\,\text{Change in Working Capital}
\bigl(\Delta\text{Current Operating Assets}\;-\;\Delta\text{Current Operating Liabilities}\bigr)\\
\underline{=\,\text{Free Cash Flow to Firm}}
\end{aligned}
$$


$$
\begin{aligned}[l]
+\,\text{Net Income Before Extraordinary Items}\\
+\,\text{After-Tax Interest Expense}\\
\underline{=\,\text{Net Operating Profit After Taxes (NOPAT)}}\\
\quad +\,\text{Depreciation and Amortization + Other Non-Cash Expenses}\\
\quad -\,\text{Capital Expenditures (including acquisitions)}\\
\quad -\,\text{Change in Working Capital}
\bigl(\Delta\text{Current Operating Assets}\;-\;\Delta\text{Current Operating Liabilities}\bigr)\\
\underline{=\,\text{Free Cash Flow to Firm}}
\end{aligned}
$$




$$
\begin{aligned}[l]
\text{Sales}\\
\quad -\,\text{Cost of Goods Sold (COGS)}\\
\quad -\,\text{Selling, General, and Administrative Expenses (SG&A)}\\
\quad -\,\text{Depreciation and Amortization}\\
\underline{=\,\text{Earnings Before Interest and Taxes (EBIT)}}\\
\quad -\,\text{Interest Expense}\\
\underline{=\,\text{Earnings Before Taxes (EBT)}}\\
\quad -\,\text{Taxes}\\
\underline{=\,\text{Net Income Before Extraordinary Items}}
\end{aligned}
$$

$$
\begin{aligned}[l]
\underline{=\,\text{Earnings Before Interest and Taxes (EBIT)}}\\
\quad -\,\text{Taxes on EBIT (e.g.\ 39\%)}\\
\underline{=\,\text{Net Operating Profit After Taxes (NOPAT)}}\\
\quad +\,\text{Depreciation and Amortization + Other Non‐Cash Expenses}\\
\quad -\,\text{Capital Expenditures (including acquisitions)}\\
\quad -\,\text{Change in Working Capital}
\bigl(\Delta\text{Current Operating Assets}-\Delta\text{Current Operating Liabilities}\bigr)\\
\underline{=\,\text{Free Cash Flow to Firm}}
\end{aligned}
$$



$$
\begin{align*}
\text{Sales} \\
- \text{Cost of Goods Sold (COGS)} \\
- \text{Selling, General, and Administrative Expenses (SGA)} \\
- \text{Depreciation and Amortization} \\
= \text{Earnings Before Interest and Taxes (EBIT)} \\
- \text{Interest Expense} \\
= \text{Earnings Before Taxes (EBT)} \\
- \text{Taxes} \\
= \text{Net Income Before Extraordinary Items}
\end{align*}
$$

$$
\begin{align*}
\text{Free Cash Flows to Firm (Top Down Approach)} \\
= \text{Earnings Before Interest and Taxes (EBIT)} \\
- \text{Taxes on EBIT (say 39\%)} \\
= \text{Net Operating Profits After Taxes (NOPAT)} \\
+ \text{Depreciation and Amortization + Other Non-Cash Expenses} \\
- \text{Capital Expenditures (including acquisitions)} \\
- \text{Change in Working Capital (Change in current operating assets - change in current operating liabilities)} \\
= \text{Free Cash Flow to Firm}
\end{align*}
$$$$
\begin{align*}
\text{Free Cash Flows to Firm (Bottom Up Approach)} \\
+ \text{Net Income Before Extraordinary Items} \\
+ \text{After-Tax Interest Expense} \\
= \text{Net Operating Profit After Taxes (NOPAT)} \\
+ \text{Depreciation and Amortization + Other Non-Cash Expenses} \\
- \text{Capital Expenditures (including acquisitions)} \\
- \text{Change in Working Capital (Change in current operating assets - change in current operating liabilities)} \\
= \text{Free Cash Flow to Firm}
\end{align*}$$
---
enhanced: true
enhancement_date: '2025-11-06'
enhancement_id: batch03-ff4707
key_concepts:
- Extensions to multi-factor CAPM models
- Working Capital
- Currency markets and foreign exchange trading
- Single-name vs. index CDS trading
- Collateralized Debt Obligations
- Market risk measurement and portfolio volatility
- Option Greeks and portfolio risk management
- Capital Asset Pricing Model and expected returns
- Futures contracts and forward pricing
- Historical simulation vs. parametric VaR models
- Default probability estimation
- Credit spread decomposition and hazard rates
- Vega and volatility risk management
- CDS clearing and central counterparties
- Value at risk and stress testing
- CDS-Bond basis and arbitrrage opportunities
- Mathematical Finance
- Option sensitivity analysis
- Monte Carlo VaR for complex portfolios
- Liquidity and price discovery
- Market portfolio and risk-free rate assumptions
- Stress testing and scenario analysis
- Equity valuation and analysis
- Course Material
- Security Market Line and beta measurement
- Currency risk management and hedging
- Forward rates and interest rate parity
- Value at Risk (VaR) methodologies and backtesting
- Theta and time decay modeling
- Counterparty risk and settlement
- Portfolio risk metrics
- Exchange rate determination and PPP theory
- Margin requirements and clearing
- Expected Shortfall and coherent risk measures
- Delta, gamma, vega, theta, rho
- Credit default swap pricing and risk-neutral probabilities
- Market microstructure and trading
- Interest rate derivatives
- Fixed income securities
- Bond pricing and yield analysis
- Gamma and convexity adjustments
- Capital Structure
- Delta hedging and the replication argument
- Credit default swaps and credit risk
- Credit risk modeling
- Delta hedging and Greeks
- Duration and convexity
- Options pricing and payoff structures
- Dividend discount models
- Empirical tests and anomalies in CAPM
tags:
- working-capital
- credit-default-swaps
- collateralized-debt-obligations
- mathematical-finance
- trading
- course-material
- capital-structure
- capm
- market-risk
- bonds
- greeks
- risk_management
- value-at-risk
- fixed_income
- exchange-rates
- valuation
- options
- credit-risk
- quantitative-implementation
- duration-convexity
- solution
- real-estate
- treasury-bonds
- wacc
- structured_finance
- equity
- stress-testing
- corporate-bonds
- credit
- vasicek-model
- dcf-valuation
- regulatory-framework
- harvard-business-review
- futures
- cds
- mean-reversion
- credit-analysis
---

# DCF Valuation Pseudo-Algorithm

## 1. Data Collection & Initial Setup

### 1.1 Company Identification

- **1.1.1** Determine company type:
    - If PUBLIC: Extract ticker symbol, exchange listing
    - If PRIVATE: Identify comparable public companies
    - If FINANCIAL_INSTITUTION: Flag for special treatment
    - If REIT: Flag for FFO/AFFO adjustments

### 1.2 Historical Financial Data Extraction

- **1.2.1** Income Statement (5-10 years):
    - Revenue by segment/geography
    - COGS, SG&A, R&D, D&A
    - EBIT, EBITDA calculations
    - Interest expense, tax expense
    - Net income, EPS
- **1.2.2** Balance Sheet:
    - Current assets (cash, AR, inventory)
    - PP&E, intangibles, goodwill
    - Current liabilities (AP, accrued expenses)
    - Debt schedule (short-term, long-term)
    - Shareholders' equity components
- **1.2.3** Cash Flow Statement:
    - Operating cash flow breakdown
    - CapEx (maintenance vs growth)
    - Working capital changes
    - Financing activities

### 1.3 Market Data Collection

- **1.3.1** If PUBLIC:
    - Current stock price
    - Shares outstanding (basic, diluted)
    - Market capitalization
    - Beta (raw, adjusted)
    - Trading volume metrics
- **1.3.2** For ALL companies:
    - Risk-free rate (10Y Treasury)
    - Market risk premium
    - Industry betas
    - Credit spreads by rating

## 2. Historical Analysis & Normalization

### 2.1 Revenue Analysis

- **2.1.1** Calculate growth rates:
    
    ```
    For each year t:
      Revenue_Growth[t] = (Revenue[t] - Revenue[t-1]) / Revenue[t-1]
      CAGR = (Revenue[final] / Revenue[initial])^(1/years) - 1
    ```
    
- **2.1.2** Segment decomposition:
    
    ```
    For each segment s:
      Segment_Mix[s,t] = Segment_Revenue[s,t] / Total_Revenue[t]
      Segment_Growth[s,t] = Growth rate calculation
    ```
    

### 2.2 Margin Analysis

- **2.2.1** Calculate all margins:
    
    ```
    Gross_Margin[t] = (Revenue[t] - COGS[t]) / Revenue[t]
    EBITDA_Margin[t] = EBITDA[t] / Revenue[t]
    EBIT_Margin[t] = EBIT[t] / Revenue[t]
    Net_Margin[t] = Net_Income[t] / Revenue[t]
    ```
    
- **2.2.2** Identify margin trends:
    
    - Calculate linear regression slopes
    - Test for mean reversion patterns
    - Flag unusual years

### 2.3 Working Capital Analysis

- **2.3.1** Calculate efficiency metrics:
    
    ```
    DSO[t] = (AR[t] / Revenue[t]) * 365
    DIO[t] = (Inventory[t] / COGS[t]) * 365
    DPO[t] = (AP[t] / COGS[t]) * 365
    CCC[t] = DSO[t] + DIO[t] - DPO[t]
    ```
    
- **2.3.2** Net Working Capital:
    
    ```
    NWC[t] = Current_Assets[t] - Cash[t] - Current_Liabilities[t] + Short_Term_Debt[t]
    NWC_as_%_Revenue[t] = NWC[t] / Revenue[t]
    ```
    

## 3. Projection Period Setup

### 3.1 Determine Projection Length

```
If MATURE_COMPANY:
  Projection_Years = 5
If GROWTH_COMPANY:
  Projection_Years = 7-10
If CYCLICAL:
  Projection_Years = Full cycle length
```

### 3.2 Revenue Projections

- **3.2.1** Base case methodology:
    
    ```
    For year p in projection_period:
      If p <= 3:
        Growth_Rate[p] = Weighted_Avg(Historical_Growth, Industry_Growth, Analyst_Estimates)
      Else:
        Growth_Rate[p] = Decay_Function(Initial_Growth, Terminal_Growth, p)
    ```
    
- **3.2.2** Segment-level projections:
    
    ```
    For each segment s:
      Segment_Revenue[s,p] = Segment_Revenue[s,p-1] * (1 + Segment_Growth_Rate[s,p])
    Total_Revenue[p] = Sum(All Segment_Revenue[s,p])
    ```
    

### 3.3 Operating Projections

- **3.3.1** COGS projection:
    
    ```
    If IMPROVING_MARGINS:
      Gross_Margin[p] = Min(Gross_Margin[p-1] + Improvement_Rate, Target_Margin)
    Else:
      Gross_Margin[p] = Average(Historical_Gross_Margins)
    COGS[p] = Revenue[p] * (1 - Gross_Margin[p])
    ```
    
- **3.3.2** Operating expenses:
    
    ```
    For each OpEx category:
      If FIXED_COST_COMPONENT:
        OpEx[p] = Fixed_Portion + (Variable_Portion * Revenue[p])
      Else:
        OpEx[p] = OpEx_as_%_Revenue * Revenue[p]
    ```
    

## 4. Free Cash Flow Calculation

### 4.1 EBIT to NOPAT

```
For each projection year p:
  EBIT[p] = Revenue[p] - COGS[p] - OpEx[p] - D&A[p]
  Tax_Rate[p] = Effective_Tax_Rate or Marginal_Tax_Rate
  NOPAT[p] = EBIT[p] * (1 - Tax_Rate[p])
```

### 4.2 Free Cash Flow Components

```
For each year p:
  # Add back non-cash charges
  Add_D&A[p] = D&A[p]
  
  # CapEx projection
  If ASSET_LIGHT:
    CapEx[p] = Revenue[p] * Historical_CapEx_as_%_Revenue
  Else:
    CapEx[p] = Maintenance_CapEx[p] + Growth_CapEx[p]
  
  # Working Capital
  NWC[p] = Revenue[p] * Target_NWC_as_%_Revenue
  Change_in_NWC[p] = NWC[p] - NWC[p-1]
  
  # Unlevered FCF
  UFCF[p] = NOPAT[p] + Add_D&A[p] - CapEx[p] - Change_in_NWC[p]
```

## 5. Weighted Average Cost of Capital (WACC)

### 5.1 Cost of Equity

- **5.1.1** CAPM approach:
    
    ```
    If PUBLIC:
      Beta = Regression_Beta or Bloomberg_Adjusted_Beta
    Else:
      # Unlever comparable betas
      For each comp c:
        Unlevered_Beta[c] = Levered_Beta[c] / (1 + (1-Tax_Rate[c]) * (Debt[c]/Equity[c]))
      Industry_Unlevered_Beta = Median(All Unlevered_Beta[c])
      
      # Relever for target
      Target_Beta = Industry_Unlevered_Beta * (1 + (1-Tax_Rate) * (Target_Debt/Target_Equity))
    
    Cost_of_Equity = Risk_Free_Rate + (Beta * Market_Risk_Premium)
    ```
    
- **5.1.2** Size premium adjustment:
    
    ```
    If SMALL_CAP:
      Size_Premium = Lookup_Duff_Phelps_Size_Premium(Market_Cap)
      Cost_of_Equity += Size_Premium
    ```
    

### 5.2 Cost of Debt

```
If RATED_DEBT:
  Credit_Spread = Lookup_Spread_by_Rating(Credit_Rating)
Else:
  Interest_Coverage = EBIT / Interest_Expense
  Synthetic_Rating = Map_Coverage_to_Rating(Interest_Coverage)
  Credit_Spread = Lookup_Spread_by_Rating(Synthetic_Rating)

Pre_Tax_Cost_of_Debt = Risk_Free_Rate + Credit_Spread
After_Tax_Cost_of_Debt = Pre_Tax_Cost_of_Debt * (1 - Tax_Rate)
```

### 5.3 WACC Calculation

```
# Target capital structure
If OPTIMAL_STRUCTURE:
  Target_D/V = Industry_Median_Debt_to_Value
Else:
  Target_D/V = Current_Debt / (Current_Debt + Market_Cap)

Target_E/V = 1 - Target_D/V

WACC = (Target_E/V * Cost_of_Equity) + (Target_D/V * After_Tax_Cost_of_Debt)
```

## 6. Terminal Value Calculation

### 6.1 Perpetuity Growth Method

```
# Terminal growth rate
Terminal_Growth = Min(
  GDP_Growth_Rate,
  Inflation_Rate + Real_Growth,
  Industry_Long_Term_Growth
)

# Terminal year calculations
Terminal_NOPAT = NOPAT[final] * (1 + Terminal_Growth)
Terminal_D&A = Revenue[final] * Terminal_D&A_as_%_Revenue
Terminal_CapEx = Terminal_D&A * (1 + Terminal_Growth/ROIC)
Terminal_NWC_Change = Terminal_Growth * NWC[final]

Terminal_FCF = Terminal_NOPAT + Terminal_D&A - Terminal_CapEx - Terminal_NWC_Change

Terminal_Value_PGM = Terminal_FCF / (WACC - Terminal_Growth)
```

### 6.2 Exit Multiple Method

```
# Select appropriate multiple
If EBITDA_MULTIPLE:
  Terminal_EBITDA = EBITDA[final] * (1 + Terminal_Growth)
  Exit_Multiple = Median(Comparable_EV/EBITDA_Multiples)
  Terminal_Value_EMM = Terminal_EBITDA * Exit_Multiple
```

### 6.3 Sanity Checks

```
Implied_Terminal_Multiple = Terminal_Value_PGM / EBITDA[final]
Implied_Terminal_Growth = WACC - (Terminal_FCF / Terminal_Value_EMM)

If ABS(Terminal_Value_PGM - Terminal_Value_EMM) / AVG() > 20%:
  Flag_for_review()
```

## 7. Present Value Calculation

### 7.1 Discount Projected FCFs

```
For each year p:
  Discount_Factor[p] = 1 / (1 + WACC)^p
  PV_FCF[p] = UFCF[p] * Discount_Factor[p]

PV_of_Projections = Sum(All PV_FCF[p])
```

### 7.2 Discount Terminal Value

```
Terminal_Discount_Factor = 1 / (1 + WACC)^Projection_Years
PV_Terminal_Value = Terminal_Value * Terminal_Discount_Factor
```

### 7.3 Enterprise Value

```
Enterprise_Value = PV_of_Projections + PV_Terminal_Value
```

## 8. Equity Value Calculation

### 8.1 Bridge from EV to Equity

```
# Add cash and equivalents
(+) Cash_and_Equivalents = Latest_Balance_Sheet_Cash
(+) Short_Term_Investments = Marketable_Securities

# Subtract debt
(-) Short_Term_Debt = Current_Portion_of_Debt
(-) Long_Term_Debt = All_Long_Term_Debt

# Adjust for other items
(-) Preferred_Stock = Preferred_at_Liquidation_Value
(-) Minority_Interest = Proportionate_Subsidiary_Value
(+) Investments_in_Associates = Equity_Method_Investments
(-) Unfunded_Pension = PV_of_Pension_Obligations
(-) Operating_Leases = PV_of_Lease_Obligations

Equity_Value = Enterprise_Value + Cash - Debt ± Other_Adjustments
```

### 8.2 Per Share Calculation

```
If OPTIONS_OUTSTANDING:
  Use Treasury_Stock_Method:
    For each tranche t:
      If Stock_Price > Strike_Price[t]:
        Proceeds[t] = Options[t] * Strike_Price[t]
        Shares_Repurchased[t] = Proceeds[t] / Stock_Price
        Net_Dilution[t] = Options[t] - Shares_Repurchased[t]
  
  Diluted_Shares = Basic_Shares + Sum(All Net_Dilution[t])
Else:
  Diluted_Shares = Basic_Shares

Value_Per_Share = Equity_Value / Diluted_Shares
```

## 9. Sensitivity Analysis

### 9.1 Key Variables

```
# Define ranges
WACC_Range = [WACC - 1%, WACC - 0.5%, WACC, WACC + 0.5%, WACC + 1%]
Terminal_Growth_Range = [TG - 1%, TG - 0.5%, TG, TG + 0.5%, TG + 1%]

# Create sensitivity matrix
For each WACC_scenario in WACC_Range:
  For each TG_scenario in Terminal_Growth_Range:
    Recalculate_Enterprise_Value()
    Sensitivity_Matrix[WACC_scenario, TG_scenario] = Value_Per_Share
```

### 9.2 Scenario Analysis

```
# Bull case
Bull_Revenue_Growth = Base_Growth * 1.2
Bull_Margins = Target_Best_in_Class_Margins
Calculate_Bull_Case_Value()

# Bear case  
Bear_Revenue_Growth = Base_Growth * 0.8
Bear_Margins = Historical_Trough_Margins
Calculate_Bear_Case_Value()

# Probability weighting
Expected_Value = (Bull_Value * 0.25) + (Base_Value * 0.5) + (Bear_Value * 0.25)
```

## 10. Output & Documentation

### 10.1 Summary Metrics

```
Output_Dashboard = {
  "Implied Share Price": Value_Per_Share,
  "Current Price": Market_Price,
  "Implied Return": (Value_Per_Share / Market_Price) - 1,
  "EV/EBITDA Multiple": Enterprise_Value / EBITDA[current],
  "P/E Multiple": Value_Per_Share / EPS[current],
  "Terminal Value %": PV_Terminal_Value / Enterprise_Value
}
```

### 10.2 Assumption Documentation

```
Key_Assumptions = {
  "Revenue CAGR": Projection_Period_CAGR,
  "Terminal Growth": Terminal_Growth,
  "WACC": WACC,
  "Tax Rate": Tax_Rate,
  "CapEx as % Revenue": Average_CapEx_Ratio,
  "NWC as % Revenue": Target_NWC_Ratio
}
```

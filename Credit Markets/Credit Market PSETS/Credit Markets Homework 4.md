---
academic_level: graduate
aliases:
- Bond Sensitivities
- Credit Markets HW4
- Homework 4
- Risky Bond Pricing
cssclasses:
- academia
enhanced: true
enhancement_date: '2025-11-06'
enhancement_id: batch09-000308
key_concepts:
- Duration analysis and interest rate risk management
- Convexity adjustments and yield curve sensitivity
- Discounted cash flow (DCF) valuation methodology
- Weighted Average Cost of Capital (WACC) and firm valuation
- Credit default swaps (CDS) and credit risk modeling
- Bootstrap methods and yield curve construction
- SOFR benchmarks and risk-free rate transition
- Risk preference theory and utility functions
- 'Valuation Methods: DCF, Comps, and Precedents'
- Value at Risk and Expected Shortfall
- Company Valuation and Multiple Analysis
- Credit Risk Management and Default Probability
- Expected Loss and Loss Given Default Models
- Swap Market Mechanisms and Pricing
- Comparable Company Analysis and Trading Multiples
- Stress Testing and Extreme Value Analysis
- Credit Default Swaps and Credit Risk Transfer
- Risk Measurement and VaR Backtesting
- Credit Default Swaps and CDS Pricing
- Bond Pricing and Yield to Maturity Analysis
- Fixed Income Securities and Credit Quality
- Interest Rate Swaps and Currency Swap Structures
- Private Equity Investment Returns and Value Creation
- CDS Spreads and Implied Default Probabilities
- Credit Spreads and Rating Migration Analysis
- LBO Valuation and Debt Capacity Analysis
- Credit Risk Transfer and Synthetic Instruments
- Leveraged Buyouts and Private Equity Transactions
- Government and Corporate Bond Markets
professional_application: theoreti
status: active
tags:
- benchmark-reform
- bootstrap-method
- capital-structure
- caplet
- cash-flow-modeling
- cds
- convexity-adjustment
- cost-of-capital
- counterparty-risk
- credit-default-swap
- credit-derivatives
- credit-modeling
- credit-rating
- dcf-valuation
- default-probability
- cds-coupons
- leveraged-buyout
- recovery-rate
- sum-of-parts
- zero-coupon-bonds
- clean-price
- equity-kickers
- lbo-valuation
- dcf-analysis
- expected-shortfall
- parametric-var
- conditional-var
- extreme-value-theory
- fixed-income
- var-methodologies
- historical-var
- cds-bond-basis
- sofr
- swap-rate
- ' exposure-at-default'
- leverage-ratio
- bond-pricing
- swap-spread
- corporate-bonds
- stress-testing
- unexpected-loss
- debt-capacity
- rating-migration
- comparable-analysis
- expected-loss
- investment-analysis
- cds-spreads
- economic-value-added
- credit-migration
- value-at-risk
- total-return-swaps
- libor
- currency-swaps
- overnight-indexed-swaps
- credit-spreads
- premium-leg
- default-leg
- trading-multiples
- foreign-recurrency
- cds-arbitrage
- government-bonds
- private-equity
- investment-return
- management-buyout
- bootstrap-strategy
- financial-markets
- probabilty-of-default
- loss-given-default
- risky-continuation
- basis-swaps
- precedent-transactions
- interest-rate-swaps
- dirty-price
- ipo-valuation
- credit-default-swaps
- monte-carlo-var
- var-backtesting
- market-multiple
- coupon-bonds
- cds-implied-probability
- current-yield
- yield-to-maturity
- price-to-earnings
title: Credit Markets Homework 4
type: note
---
--



# Credit Markets Homework 4

This homework relies on multiple files (from previous weeks):

- The bond symbology file `bond_symbology`,
- The "on-the-run" treasuries data file `govt_on_the_run`,
- The bond market data file `bond_market_prices_eod`,
- The CDS data file `cds_market_data_eod`.
- The SOFR Is Swap symbology file `sofr_swap_symbology`,
- The SOFR Is Swap market data file `sofr_swaps_market_data_eod`.

```python
# Import tools from previous homeworks
from credit_market_tools import *

# Use static calculation/valuation date of 2024-04-19, matching data available in the market prices EOD file
calc_date = ql.Date(19, 4, 2024)
ql.Settings.instance().evaluationDate = calc_date

# Calculation/valuation date as pd datetime
as_of_date = pd.to_datetime('2024-04-19')
```

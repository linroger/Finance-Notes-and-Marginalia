---
aliases:
- Bond Sensitivities
- Credit Markets HW4
- Homework 4
- Risky Bond Pricing
cssclasses:
- academia
key_concepts:
- Interest rate swaps and valuation
- Currency and cross-currency swaps
- Swap spreads and basis trading
- Bond pricing and yield curves
- Duration and convexity hedging
- Credit spreads and bond valuation
- Fixed income securities and markets
- Bond valuation and yield calculation
- Credit analysis and spread decomposition
- Interest rate theory and modeling
- Monetary policy and rate setting
- LIBOR transition and SOFR
- Credit default swap mechanics
- CDS-Bond basis and relative value
- Credit risk and default modeling
- Credit Markets Homework 4 and financial analysis
- Credit Markets Homework 4 in modern finance
- Applications of Credit Markets Homework 4
- 'Case study: Credit Markets Homework 4'
tags:
- credit
- swap
- swaps
- bonds
- cds
- fixed-income
- bond
- interest-rates
- multiple
- sofr
- valuation
title: Credit Markets Homework 4
---

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

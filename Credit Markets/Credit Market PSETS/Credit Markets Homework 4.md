---
title: Credit Markets Homework 4
cssclasses:
- academia
tags:
- bond
- bond_duration
- bond_valuation
- cds_pricing
- credit-derivatives
- credit-risk
- credit-spread
- credit_market_homework
- duration
- hazard_rate_model
- ibm_bonds
- ir01
- multiple
- risky_bonds
- scenario_analysis
- sofr
- sofr_curve
- swap
- treasury
- treasury_curve
- yield-curve
- yield_curve_calibration
aliases:
- Bond Sensitivities
- Credit Markets HW4
- Homework 4
- Risky Bond Pricing
key_concepts:
- Basis swap mechanics
- Bond duration calculation
- Bond market data analysis
- CDS hazard rate calibration
- CDS-implied bond prices
- Convexity adjustment
- Credit spread dynamics
- Cross-currency basis
- Currency swap structure
- DV01 calculation
- Derivative securities
- Duration measurement
- Financial risk management
- Fixed vs floating leg
- Hedging with bonds
- Interest rate sensitivity
- Interest rate swap pricing
- Intrinsic vs market basis
- Modified duration calculation
- Portfolio immunization
- Portfolio optimization
- Present value of swaps
- Price-yield relationship
- Quantitative financial analysis
- Risk assessment and mitigation
- Risky bond pricing methodology
- SOFR curve bootstrapping
- Scenario IR01 analysis
- Swap curve construction
- Swaption valuation
- Treasury yield curve calibration
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
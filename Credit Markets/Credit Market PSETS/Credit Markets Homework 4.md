---
aliases:
- Bond Sensitivities
- Credit Markets HW4
- Homework 4
- Risky Bond Pricing
cssclasses:
- academia
enhanced: true
enhancement_date: '2025-11-06'
enhancement_id: batch03-9af6b2
key_concepts:
- Scenario IR01 analysis
- CDS-implied bond prices
- Term structure of interest rates and yield curve shapes
- Treasury Bonds
- Single-name vs. index CDS trading
- Collateralized Debt Obligations
- Credit risk modeling and default probability estimation
- Probability of default estimation from credit spreads
- Bond market data analysis
- Credit spread analysis and OAS methodology
- Expectations hypothesis and liquidity preference theory
- Solution
- Credit portfolio diversification and concentration
- Yield curve fitting and interpolation methods
- Credit spread decomposition and hazard rates
- Structural models of default and Merton formulation
- CDS clearing and central counterparties
- Portfolio immunization strategies
- CDS-Bond basis and arbitrrage opportunities
- Mathematical Finance
- Spot rates vs. forward rates modeling
- Infrastructure investment and project finance
- Bond duration calculation
- Credit default swap pricing and recovery assumptions
- 'Structured products: CDOs, CLOs, and credit derivatives'
- Key rate duration and curve risk
- Course Material
- Synthetic credit derivatives and index trades
- interest rate and currency derivatives
- Credit default swap pricing and risk-neutral probabilities
- Intrinsic vs market basis
- SOFR curve bootstrapping
- Credit exposure measurement and EAD
- Loss given default and recovery rates
- Treasury yield curve calibration
- Wrong-way risk in derivative transactions
- Stress Testing
- Credit intermediation and information asymmetry
- Quantitative Implementation
- Credit risk migration matrices and rating transition
- CDS hazard rate calibration
- Credit spread dynamics
- Credit risk modeling and portfolio correlation analysis
- Credit risk assessment and loan portfolio management
- Parallel and non-parallel shifts in the yield curve
- Duration and convexity measures for bond portfolios
- Counterparty credit exposure measurement
- Price sensitivity to interest rate changes
- Modified duration vs. Macaulay duration
- credit risk transfer mechanisms
- Risky bond pricing methodology
- Corporate Bonds
tags:
- yield-curve
- ir01
- credit-default-swaps
- cds_pricing
- collateralized-debt-obligations
- sofr
- mathematical-finance
- sofr_curve
- course-material
- hazard_rate_model
- risky_bonds
- ibm_bonds
- credit-risk
- treasury_curve
- credit_market_homework
- quantitative-implementation
- duration-convexity
- solution
- treasury-bonds
- bond_duration
- yield_curve_calibration
- stress-testing
- infrastructure
- corporate-bonds
- scenario_analysis
- cds
- bond_valuation
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

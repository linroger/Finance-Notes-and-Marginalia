---
title: Credit Market Solutions
cssclasses: 
  - academia
tags:
  - bond_symbology
  - credit_market_solutions
  - government_bonds
  - us_treasuries
  - yield_curve
  - credit_spreads
  - g_spreads
  - quantlib_analysis
  - homework_solutions
aliases:
  - FINM 35700
  - Homework 1
  - Treasury bonds
  - UChicago
key_concepts:
  - Bond symbology exploration
  - Historical coupon time series
  - On-the-run US treasuries
  - US treasury instruments
  - US treasury yield curve
  - Credit spread calculations
  - G-spread computation
  - Benchmark bond analysis
  - QuantLib bond pricing
---

# Credit Market Solutions

## Solution to Homework 1

## FINM 35700 - Spring 2024

### UChicago Financial Mathematics

This homework relies on:

- the government and Corporate Bonds symbology file `bond_symbology`,
- the "on-the-run" treasuries data file `govt_on_the_run` and
- the market data file `bond_market_prices_eod`.

You can find more details on US treasury instruments in the FINM 37400 Fixed Income course.

```python
import QuantLib as ql
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import seaborn as sns
import scipy as sp
import plotly.express as px
import plotly.graph_objects as go
```

# Problem 1: Explore symbology for US treasuries and Corporate Bonds

## a. Load and explore US government bond symbology

Load the `bond_symbology` Excel file into a dataframe. It contains symbology for both government and Corporate Bonds.

Select US Treasury bonds only (class = 'Govt', ticker = 'T'). For each government bond issue, calculate its initial term/time-to-maturity in years (based on issue date and maturity date), as well as the current time-to-maturity. Assume a year has 365.25 days (alternatively, use QuantLib yearFraction function).

```python
import pandas as pd

# Import bond market prices
bond_market_prices_eod = pd.read_excel('data/bond_market_prices_eod.xlsx')
display(bond_market_prices_eod)

# Import CDS market data
cds_market_data_eod = pd.read_excel('data/cds_market_data_eod.xlsx')
display(cds_market_data_eod)

# Import CDX IG 42 5Y basket composition
cdx_ig_42_5y_basket_composition = pd.read_excel('data/cdx_ig_42_5y_basket_composition.xlsx')
display(cdx_ig_42_5y_basket_composition)

# Import CDX symbology
cdx_symbology = pd.read_excel('data/cdx_symbology.xlsx')
display(cdx_symbology)

# Import corporate symbology
corp_symbology = pd.read_excel('data/corp_symbology.xlsx')
display(corp_symbology)

# Import government on-the-run data
govt_on_the_run = pd.read_excel('data/govt_on_the_run.xlsx')
display(govt_on_the_run)

# Import government symbology
govt_symbology = pd.read_excel('data/govt_symbology.xlsx')
display(govt_symbology)

# Import LQD basket composition
lqd_basket_composition = pd.read_excel('data/lqd_basket_composition.xlsx')
display(lqd_basket_composition)

# Import LQD corporate symbology
lqd_corp_symbology = pd.read_excel('data/lqd_corp_symbology.xlsx')
display(lqd_corp_symbology)

# Import market prices EOD
market_prices_eod = pd.read_excel('data/market_prices_eod.xlsx')
display(market_prices_eod)

# Import SOFR swaps market data
sofr_swaps_market_data_eod = pd.read_excel('data/sofr_swaps_market_data_eod.xlsx')
display(sofr_swaps_market_data_eod)

# Import SOFR swaps symbology
sofr_swaps_symbology = pd.read_excel('data/sofr_swaps_symbology.xlsx')
display(sofr_swaps_symbology)
```

```python
# Load bond_symbology.xlsx
bond_symbology = pd.read_excel('bond_symbology.xlsx')

# Set as-of-date
as_of_date = pd.to_datetime('2024-04-01')

# Add term and TTM columns
bond_symbology['term'] = (bond_symbology['maturity'] - bond_symbology['start_date']).dt.days / 365.25
bond_symbology['TTM'] = (bond_symbology['maturity'] - as_of_date).dt.days / 365.25

# Create Govt bonds symbology df
govt_symbology = bond_symbology[(bond_symbology['class'] == 'Govt') 
                                   & (bond_symbology['ticker'] == 'T')].copy()

# Display govt_symbology
display(govt_symbology.head())
```

## b. Historical time series of US treasury coupons

Plot the time series of coupons for US treasury notes/bonds issued in the last 10 years (indexed by issue date).
What can you say about the overall level of issued coupons in the last 4 years?

### Solution:

```python
# 10y cut-off date
cut_off_date_10y = pd.to_datetime('2014-04-01')
govt_symbology_10y = govt_symbology[govt_symbology['start_date'] >= cut_off_date_10y].copy()

# Plot the US Treasury coupons by issue date (last 10 years)
# govt_symbology_10y.plot(x='start_date', y='coupon', grid=True, style='-*', 
#                      title='US Treasury coupons by issue date (last 10 years)', figsize=(12, 8))

# Plotly version
import plotly.express as px

fig = px.scatter(govt_symbology_10y, x='start_date', y='coupon', title='US Treasury coupons by issue date (last 10 years)')
fig.update_layout(xaxis_title='Issue Date', yaxis_title='Coupon', template='plotly_white')
fig.show()
```

```python
# 4y cut-off date
cut_off_date_4y = pd.to_datetime('2020-04-01')
govt_symbology_4y = govt_symbology[govt_symbology['start_date'] >= cut_off_date_4y].copy()

# Plot the US Treasury coupons by issue date (last 4 years)
# govt_symbology_4y.plot(x='start_date', y='coupon', grid=True, style='-*', 
#                      title='US Treasury coupons by issue date (last 4 years)', figsize=(12, 8))

# Plotly version
fig = px.scatter(govt_symbology_4y, x='start_date', y='coupon', title='US Treasury coupons by issue date (last 4 years)')
fig.update_layout(xaxis_title='Issue Date', yaxis_title='Coupon', template='plotly_white')
fig.show()

# describe
govt_symbology_4y'start_date', 'coupon']].describe()
```

What can you say about the overall level of issued coupons in the last 4 years?

Based on the summary statistics provided, we can make following observations:

- The average (mean) coupon rate is 2.367.
- The median coupon rate (50th percentile) is 2.5
- The minimum coupon rate is 0.125, while the maximum is 5.00.
- The coupon rate increased from decade lows of 0.125 in 2020, to decade highs of 5.00 in 2023.

## c. Load the on-the-run US treasuries

Load the `govt_on_the_run` Excel file into a dataframe. Select the current on-the-run 2Y, 3Y, 5Y, 7Y, 10Y, 20Y and 30Y issues (off-the-run issues have the B & C suffix). Create a separate symbology dataframe for on-the-run treasuries only, to be used later on for the on-the-run government yield curve bootstrapping.

### Solution:

```python
# Load govt_on_the_run, as of 2024-04-01
govt_on_the_run = pd.read_excel('govt_on_the_run.xlsx')
display(govt_on_the_run.head())

# Keep OTR treasuries only
govt_on_the_run_simple = govt_on_the_run[~govt_on_the_run['ticker'].str.contains('B | C')]
display(govt_on_the_run_simple)
```

```python
# Create symbology for on-the-run treasuries only
govt_symbology_otr = govt_symbology[govt_symbology['isin'].isin(govt_on_the_run_simple['isin'])]
govt_symbology_otr = govt_symbology_otr.sort_values(by='TTM')
display(govt_symbology_otr)
```

## d. Load and explore US Corporate Bonds symbology data

Starting from the `bond_symbology` dataframe, create a corporate bond dataframe containing

- Bullet/non-callable (mty_typ="AT MATURITY"),
- Senior unsecured (rank = "Sr Unsecured"),
- Fixed coupon (cpn_type="FIXED")

Bonds only, with following columns:

 | ticker | isin | figi | security | name | coupon | start_date | maturity | term | TTM | 
 | -------- | ------ | ------ | ---------- | ------ | -------- | ----------- | ---------- | ------ | ----- | 

Where

- `term` refers to the initial term/time-to-maturity in years
- `TTM` refers to the current time-to-maturity in years

Create a separate dataframe for VZ issuer only (ticker = 'VZ') and display it.

### Solution:

```python
# Create Corp bonds symbology df
corp_symbology = bond_symbology[bond_symbology['class'] == 'Corp'].copy()

corp_symbology = corp_symbology[(corp_symbology['mty_typ'] == 'AT MATURITY') 
                                   & (corp_symbology['rank'] == 'Sr Unsecured')
                                   & (corp_symbology['cpn_type'] == 'FIXED')]

# Keep selected columns only
corp_symbology = corp_symbology'ticker', 'isin', 'figi', 'security', 'name', 'coupon', 
                               'start_date', 'maturity', 'term', 'TTM']]

# Filter for VZ issuer
corp_symbology_vz = corp_symbology[corp_symbology['ticker'] == 'VZ']
corp_symbology_vz = corp_symbology_vz.sort_values(by='TTM')

# Display corp_symbology_vz
display(corp_symbology_vz)
```

# Problem 2: Explore EOD market prices and yields

## a. Load and explore treasury market prices and yields

Load the `bond_market_prices_eod` Excel file into a dataframe. It provides market data for US treasuries and Corporate Bonds as of 2024-04-01.

Merge the treasuries symbology dataframe with the market data and add the following columns:

 | date | bidPrice | askPrice | midPrice | bidYield | askYield | midYield | term | TTM | 
 | ------ | ---------- | ---------- | ---------- | ---------- | ---------- | ---------- | ------ | ----- | 

Plot a graph/scatter plot of treasury mid yields by TTM.

### Solution:

```python
# Load bond_market_prices_eod
bond_market_prices_eod = pd.read_excel('bond_market_prices_eod.xlsx')
bond_market_prices_eod['midPrice'] = 0.5*(bond_market_prices_eod['bidPrice'] + bond_market_prices_eod['askPrice'])
bond_market_prices_eod['midYield'] = 0.5*(bond_market_prices_eod['bidYield'] + bond_market_prices_eod['askYield'])

display(bond_market_prices_eod.head())
```

```python
# Merge market data as of 2024-04-01 into treasury symbology
govt_agg = govt_symbology.merge(bond_market_prices_eod, on=['class', 'ticker', 'figi', 'isin'])

display(govt_agg.head())

# Plot a graph/scatter plot of treasury mid yields by TTM
# govt_agg.plot(x='TTM', y='midYield', grid=True, style='*', 
#              title='US Treasury Yields by TTM', figsize=(12, 8))

# Plotly version
fig = px.scatter(govt_agg, x='TTM', y='midYield', title='US Treasury Yields by TTM')
fig.update_layout(xaxis_title='Time to Maturity (Years)', 
                 yaxis_title='Mid Yield', template='plotly_white')
fig.show()
```

## b. Explore on-the-run treasuries only

Create a separate joint dataframe for on-the-run treasuries only.

Plot a graph/scatter plot of on-the-run treasury mid yields by TTM.

### Solution:

```python
# Merge market data as of 2024-04-01 into treasury OTR symbology
govt_agg_otr = govt_symbology_otr.merge(bond_market_prices_eod, on=['class', 'ticker', 'figi', 'isin'])

# Plot a graph/scatter plot of on-the-run treasury mid yields by TTM
# govt_agg_otr.plot(x='TTM', y='midYield', grid=True, style='-*', 
#                   title='OTR US Treasury yields by TTM', figsize=(12, 8))

# Plotly version
fig = px.scatter(govt_agg_otr, x='TTM', y='midYield', title='OTR US Treasury yields by TTM')
fig.update_traces(mode='lines+markers')
fig.update_layout(xaxis_title='Time to Maturity (Years)', 
                 yaxis_title='Mid Yield', template='plotly_white')
fig.show()
```

## c. Load and explore corporate bond market prices and yields

Merge the filtered Corporate Bonds symbology dataframe with the market data and add the following columns:

 | date | bidPrice | askPrice | midPrice | bidYield | askYield | midYield | term | TTM | 
 | ------ | ---------- | ---------- | ---------- | ---------- | ---------- | ---------- | ------ | ----- | 

List the unique tickers/issuers available in the dataframe.

### Solution:

```python
# Merge market data as of 2024-04-01 into corp symbology
corp_agg = corp_symbology.merge(bond_market_prices_eod, on=['ticker', 'figi', 'isin'])

print(corp_symbology.shape)
print(corp_agg.shape)

display(corp_agg.head())
```

```python
# Unique tickers
corp_agg_unique_tickers = corp_agg'ticker', 'name']].drop_duplicates()

display(corp_agg_unique_tickers)
```

## d. Yield curve plots

Plot a graph/scatter plot of mid yield curves by TTM (one line per ticker/issuer).

Add a separate line for on-the-run US treasury yield curve (risk free curve).

What can you say about the credit issuer yields, compared to US treasury yields?

### Solution:

```python
# Corporate bond yield curves
# for ticker in corp_agg_unique_tickers['ticker']:
#     corp_agg_ticker = corp_agg[corp_agg['ticker'] == ticker]
#     corp_agg_ticker.plot(x='TTM', y='midYield', grid=True, style='-', 
#                          title=f'{ticker} yield curve by TTM', figsize=(12, 8))

# Gov on-the-run yield curve
# govt_agg_otr.plot(x='TTM', y='midYield', grid=True, style='-*', 
#                  title='OTR US Treasury yields by TTM', figsize=(12, 8))

# All yield curves on one plot
fig = px.scatter(corp_agg, x='TTM', y='midYield', color='ticker', 
               title='Corporate Bond Yields by TTM', marginal_y="violin")
fig.add_trace(px.scatter(govt_agg_otr, x='TTM', y='midYield').data[0])
fig.update_traces(mode='lines+markers')
fig.update_layout(xaxis_title='Time to Maturity (Years)', 
                 yaxis_title='Mid Yield', template='plotly_white')
fig.show()
```

What can you say about the credit issuer yields, compared to US treasury yields?

There are some clear observations that we can make:
- Corporate bonds yield a premium over UST bonds for similar maturities.
- The premium is higher for riskier (lower-rated) issuers.
- Different issuers have different yield curves, with some steeper and some flatter.
- The yield curve shape appears to be dependent on the issuer's credit quality.

# Problem 3: Underlying treasury benchmarks and credit spreads

## a. Add underlying benchmark bond mid yields

Start with the corporate bond symbology dataframe. Use the column 'und_bench_yield' to identify the underlying benchmark bond for each bond issue.

Add two new columns to the joint corporate bond dataframe:

 | und_bench_yield | credit_spread | 
 | ----------------- | --------------- | 

Where

- `und_bench_yield` = underlying benchmark bond mid yield and
- `credit_spread` = issue yield - underlying benchmark bond mid yield.

### Solution:

```python
# Use the column 'und_bench_yield' to identify the underlying benchmark bond for each bond issue.
corp_merged = corp_agg.merge(bond_symbology'isin', 'und_bench_isin']], on='isin')

# Create df containing govt_benchmark_yields
govt_benchmark_yields = bond_market_prices_eod[bond_market_prices_eod['class'] == 'Govt']'isin', 'midYield']]
govt_benchmark_yields.rename(columns={'midYield': 'und_bench_yield', 'isin': 'und_bench_isin'}, inplace=True)

# Add benchmark bond yield
corp_merged = corp_merged.merge(govt_benchmark_yields, on='und_bench_isin')
corp_merged['credit_spread'] = corp_merged['midYield'] - corp_merged['und_bench_yield']
display(corp_merged'ticker', 'isin', 'figi', 'security', 'und_bench_isin', 
                    'midYield', 'und_bench_yield', 'credit_spread']])
```

## b. Credit spread curve plots

Plot a graph/scatter plot of credit spread curves by TTM (one line per issuer).

### Solution:

```python
# Credit spread curves
# for ticker in corp_agg_unique_tickers['ticker']:
#     corp_merged_ticker = corp_merged[corp_merged['ticker'] == ticker]
#     corp_merged_ticker.plot(x='TTM', y='credit_spread', grid=True, style='-', 
#                             title=f'{ticker} credit spread curve by TTM', figsize=(12, 8))

# All credit spread curves on one plot
fig = px.scatter(corp_merged, x='TTM', y='credit_spread', color='ticker', 
               title='Corporate Bond Credit Spreads by TTM', marginal_y="box")
fig.update_traces(mode='lines+markers') 
fig.update_layout(xaxis_title='Time to Maturity (Years)', 
                 yaxis_title='Credit Spread', 
                 template='plotly_white')
fig.show()
```

## c. Add g-spreads

Add two new columns to the joint corporate bond dataframe:

 | interp_tsy_yield | g_spread | 
 | ------------------ | ---------- | 

Where

- `interp_tsy_yield` = interpolated treasury yield (using on-the-run treasuries only), matching the issue maturity
- `g_spread` = issue yield - interp_tsy_yield.

### Solution:

```python
# Interpolate OTR Treasury yields on corporate bond TTMs
interp_tsy_yield_vec = np.interp(corp_merged['TTM'], govt_agg_otr['TTM'], govt_agg_otr['midYield'])

# Add interp_tsy_yield and g_spread
corp_merged['interp_tsy_yield'] = interp_tsy_yield_vec
corp_merged['g_spread'] = corp_merged['midYield'] - corp_merged['interp_tsy_yield']

# Display results
display(corp_merged'ticker', 'isin', 'figi', 'security', 'und_bench_isin', 'midYield', 
                    'und_bench_yield', 'credit_spread', 'interp_tsy_yield', 'g_spread']])
```

## d. G-spread curve plots

Plot a graph/scatter plot of g-spread curves by TTM (one line per issuer).

### Solution:

```python
# G-spread curves
# for ticker in corp_agg_unique_tickers['ticker']:
#     corp_merged_ticker = corp_merged[corp_merged['ticker'] == ticker]
#     corp_merged_ticker.plot(x='TTM', y='g_spread', grid=True, style='-', 
#                             title=f'{ticker} g-spread curve by TTM', figsize=(12, 8))

# All g-spread curves on one plot
fig = px.scatter(corp_merged, x='TTM', y='g_spread', color='ticker', 
               title='Corporate Bond G-Spreads by TTM', marginal_y="histogram")
fig.update_traces(mode='lines+markers')
fig.update_layout(xaxis_title='Time to Maturity (Years)', 
                 yaxis_title='G-Spread', template='plotly_white') 
fig.show()
```

# Problem 4: Explore sections 1 to 5 in the QuantLib example notebook

Explore sections 1 to 5 in the example notebook and identify concepts discussed in the first lecture. Collect open questions for the upcoming TA Review session on the analytics library.

Find the 'ORCL 2.95 04/01/30' bond (mentioned on page 12 in Session 1) in the bond symbology file. Create the corresponding fixed rate bond object and display the future cashflows. Do you match the cashflows displayed on page 13?

Going forward, we will be using QuantLib for curve calibration (US Treasury + SOFR), as well as pricing and risk of various cash and synthetic credit instruments.

### Solution:

```python
# Find the 'ORCL 2.95 04/01/30' bond in bond symbology
corp_symbology_orcl = bond_symbology[bond_symbology['security'] == 'ORCL 2.95 04/01/30']

display(corp_symbology_orcl.transpose())
```

```python
# Construct fixed rate cashflow schedule for ORCL 2.95 04/01/30

issue_date = ql.Date(1, 4, 2020)        # 2020-04-01
maturity_date = ql.Date(1, 4, 2030)     # 2030-04-01

coupon_freq = ql.Semiannual
coupon_term = ql.Period(coupon_freq)
calendar = ql.UnitedStates(ql.UnitedStates.GovernmentBond)
day_count_conv = ql.Unadjusted
date_generation = ql.DateGeneration.Backward
month_end = True

# Fixed_rate_schedule
fixed_rate_schedule = ql.Schedule(issue_date,        
                     maturity_date,        
                     coupon_term,        
                     calendar,        
                     day_count_conv,        
                     day_count_conv,        
                     date_generation,        
                     month_end)
```

```python
# Construct corporate bond object for ORCL 2.95 04/01/30

# Day_count: 30/360 for fixed-rate Corp bonds
day_count = ql.Thirty360(ql.Thirty360.USA)

# Settlement_days: 2 for Corp Bonds
settlement_days = 2

# Coupons
coupon_rate = 0.0295     # 2.95%
coupons = [coupon_rate]

# Payment_convention
payment_convention = ql.Unadjusted

# Face_value
face_value = 100

# Construct the fixed_rate_bond
fixed_rate_bond = ql.FixedRateBond(
    settlement_days,        
    face_value,        
    fixed_rate_schedule,        
    coupons,        
    day_count,        
    payment_convention)
```

```python
# Display the contractual cashflows
x = [(cf.date().to_date(), cf.amount()) for cf in fixed_rate_bond.cashflows()]
cf_date_fixed, cf_amount = zip(*x)
fixed_rate_bond_cashflows = pd.DataFrame(data={'CashFlowDate': cf_date_fixed, 'CashFlowAmount': cf_amount})

# Cashflows match the ones displayed on page 13 (from Bloomberg CSHF screenshot), up to the face value multiplier.
display(fixed_rate_bond_cashflows)
```

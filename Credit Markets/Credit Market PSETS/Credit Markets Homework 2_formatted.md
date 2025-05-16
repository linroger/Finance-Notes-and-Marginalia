---
title: Credit Markets Homework 2
tags:
  - bond_market_data
  - cashflow_schedules
  - credit_markets
  - fixed_rate_bonds
  - quantlib
  - yield_curve_calibration
  - credit_spreads
  - risk_metrics
  - z_spread
  - duration_convexity
  - treasury_bonds
  - corporate_bonds
  - discount_factors
aliases:
  - Credit Markets Homework 2
  - Fixed Rate Bonds Homework
  - Bond Cash Flow Analysis
cssclasses:
  - homework
key_concepts:
  - Bond cash flows
  - Cashflow schedules
  - Fixed rate bonds
  - QuantLib date object
  - Symbology data
  - Yield curve calibration
  - Duration and convexity calculation
  - Discount factor curves
  - Z-spread calculation
  - Bond pricing using discount curves
  - PiecewiseLogCubicDiscount curve
  - Bootstrapping yield curves
  - Analytical vs scenario-based risk metrics
  - Treasury bond pricing
  - Corporate bond pricing
  - Bond risk measurement
---

# Credit Markets Homework 2

This homework relies on:

- The corporate and government bonds symbology file `bond_symbology`,
- The "on-the-run" treasuries data file `govt_on_the_run`,
- The bond market data file `bond_market_prices_eod`, containing EOD price data as of 2024-04-08.

# Problem 1: Constructing Fixed Rate Bonds

```python
import QuantLib as ql
import pandas as pd
import datetime as dt

# Use static calculation/valuation date of 2024-04-08, matching data available in the market prices EOD file
calc_date = ql.Date(8, 4, 2024)
ql.Settings.instance().evaluationDate = calc_date
```

## a. Prepare the Symbology and Market Data Files for Fixed Rate Government and Corporate Bonds

Load the `bond_symbology`, `bond_market_prices_eod` and `govt_on_the_run` Excel files into dataframes.

Filter the symbology frame for fixed rate bonds only (cpn_type="FIXED").

```python
# Set as-of-date
as_of_date = pd.to_datetime('2024-04-08')

# Load bond_symbology.xlsx
bond_symbology = bond_symbology[bond_symbology['cpn_type'] == 'FIXED']

# Add term and TTM columns
bond_symbology['term'] = (bond_symbology['maturity'] - bond_symbology['start_date']).dt.days / 365.25
bond_symbology['TTM'] = (bond_symbology['maturity'] - as_of_date).dt.days / 365.25
display(bond_symbology.head())

# Load bond_market_prices_eod
# Add mid prices and yields
bond_market_prices_eod['midPrice'] = 0.5*(bond_market_prices_eod['bidPrice'] + bond_market_prices_eod['askPrice'])
bond_market_prices_eod['midYield'] = 0.5*(bond_market_prices_eod['bidYield'] + bond_market_prices_eod['askYield'])
display(bond_market_prices_eod.head())

bond_symbology

# Load govt_on_the_run, as of 2024-04-08
# Keep OTR treasuries only
govt_on_the_run_simple = govt_on_the_run[~govt_on_the_run['ticker'].str.contains('B|C')]
display(govt_on_the_run_simple.head())
```

<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>ticker</th>
      <th>class</th>
      <th>figi</th>
      <th>isin</th>
      <th>und_bench_isin</th>
      <th>security</th>
      <th>name</th>
      <th>type</th>
      <th>coupon</th>
      <th>cpn_type</th>
      <th>…</th>
      <th>acc_first</th>
      <th>maturity</th>
      <th>mty_typ</th>
      <th>rank</th>
      <th>amt_out</th>
      <th>country</th>
      <th>currency</th>
      <th>status</th>
      <th>term</th>
      <th>TTM</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>AAPL</td>
      <td>Corp</td>
      <td>BBG004HST0K7</td>
      <td>US037833AL42</td>
      <td>US912810TZ12</td>
      <td>AAPL 3.85 05/04/43</td>
      <td>APPLE INC</td>
      <td>GLOBAL</td>
      <td>3.850</td>
      <td>FIXED</td>
      <td>…</td>
      <td>2013-05-03</td>
      <td>2043-05-04</td>
      <td>AT MATURITY</td>
      <td>Sr Unsecured</td>
      <td>3000.0</td>
      <td>US</td>
      <td>USD</td>
      <td>ACTV</td>
      <td>30.001369</td>
      <td>19.069131</td>
    </tr>
  </tbody>
</table>
</div>

## b. Add Function to Construct Generic Fixed Rate Cashflow Schedules from Symbology Data

Use one row of the symbology dataframe as input to the function. Use the helper function to convert a date string to a QuantLib date object.

```python
def get_ql_date(date) -> ql.Date:
    """
    Convert dt.Date to ql.Date
    """
    if isinstance(date, dt.Date):
        return ql.Date(date.day, date.month, date.year)
    elif isinstance(date, str):
        date = dt.datetime.strptime(date, "%Y-%m-%d").date()
        return ql.Date(date.day, date.month, date.year)
    else:
        raise ValueError(f"to_qldate, {type(date)}, {date}")
```

```python
def create_schedule_from_symbology(details: dict):
    '''Create a QuantLib cashflow schedule from symbology details dictionary (usually one row of the symbology dataframe)
    '''
    
    # Create maturity from details['maturity']
    maturity = get_ql_date(details['maturity'])
    
    # Create acc_first from details['acc_first']
    acc_first =  get_ql_date(details['acc_first'])
    
    # Create calendar for Corp and Govt asset classes
    calendar = ql.UnitedStates(ql.UnitedStates.GovernmentBond)
    
    # define period from details['cpn_freq'] … Can be hard-coded to 2 = semi-annual frequency
    period = ql.Period(2)
    
    # business_day_convention
    business_day_convention = ql.Unadjusted
    
    # termination_date_convention
    termination_date_convention = ql.Unadjusted
    
    # date_generation
    date_generation=ql.DateGeneration.Backward
    
    # Create schedule using ql.MakeSchedule interface (with keyword arguments)
    schedule = ql.MakeSchedule(effectiveDate=acc_first,  # this may not be the same as the bond's start date
                        terminationDate=maturity,
                        tenor=period,
                        calendar=calendar,
                        convention=business_day_convention,
                        terminalDateConvention=termination_date_convention,
                        rule=date_generation,
                        endOfMonth=True,
                        firstDate=ql.Date(),
                        nextToLastDate=ql.Date())
    return schedule
```

```python
# Use one row of the symbology dataframe as input to the create_schedule_from_symbology() function.
corp_bond_details = bond_symbology[bond_symbology['class'] == 'Corp'].iloc[10]
print("Corp bond details for", corp_bond_details['security'])
display(corp_bond_details)

# Create cashflow_schedule
cashflow_schedule = create_schedule_from_symbology(corp_bond_details)
print("Cashflow dates for", corp_bond_details['security'])

# List cashflow dates
for date in cashflow_schedule:
        print(date)
```

## c. Add Function to Construct Generic Fixed Rate Bond Objects from Symbology Data

Use one row of the symbology dataframe as input to the function. Use create_schedule_from_symbology() internally to create the cashflow schedule.

```python
def create_bond_from_symbology(details: dict):
    '''Create a US fixed rate bond object from symbology details dictionary (usually one row of the symbology dataframe)
    '''
    
     # Create day_count from details['dcc']
     # For US Treasuries use ql.ActualActual(ql.ActualActual.ISMA)
     # For US Corporate Bonds use ql.Thirty360(ql.Thirty360.USA)
    
    if details['class'] == 'Corp':
        day_count = ql.Thirty360(ql.Thirty360.USA)
    elif details['class'] == 'Govt':
        day_count = ql.ActualActual(ql.ActualActual.ISMA)
    else:
        raise ValueError(f"unsupported asset class, {type(details['class'])}, {details['class']}")
    
    # Create issue_date from details['start_date']
    issue_date = get_ql_date(details['start_date'])
    
    # Create days_settle from details['days_settle']
    days_settle = int(float(details['days_settle']))

    # Create coupon from details['coupon']
    coupon = float(details['coupon'])/100.
    
    # Create cashflow schedule
    schedule = create_schedule_from_symbology(details)
    
    face_value = 100
    redemption = 100
    
    payment_convention = ql.Unadjusted
        
    # Create fixed rate bond object
    fixed_rate_bond = ql.FixedRateBond(
        days_settle,
        face_value,
        schedule,
        [coupon],
        day_count,
        payment_convention,
        redemption,
        issue_date)        

    return fixed_rate_bond
```

```python
# Use one row of the symbology dataframe as input to the function.
corp_bond_object = create_bond_from_symbology(corp_bond_details)

print("Corp bond object details for", corp_bond_details['security'])
print('Start date: ', corp_bond_object.startDate())
print('Maturity date: ', corp_bond_object.maturityDate())
print('Bond face notional: ', corp_bond_object.notional())
```

## d. Add Function that Returns a Dataframe with (Future) Cash Flows Details for a Bond Object

Use the "Investigate Bond Cashflows" section in the Quantlib Basic notebook as a template.

The results dataframe should contain following columns:

| CashFlowDate | CashFlowAmount | CashFlowYearFrac |
|----------|-------|-------------|

Pick one government and one corporate bond from symbology, create the bond objects and display the future cashflows.

```python
def get_bond_cashflows(bond: ql.FixedRateBond, calc_date=ql.Date) -> pd.DataFrame:
    '''Returns all future cashflows as of calc_date, i.e. with payment dates > calc_date.
    '''    
    day_counter = bond.dayCounter()    
    
    x = [(cf.date(), day_counter.yearFraction(calc_date, cf.date()), cf.amount()) for cf in bond.cashflows()]
    cf_date, cf_yearFrac, cf_amount = zip(*x)
    cashflows_df = pd.DataFrame(data={'CashFlowDate': cf_date, 'CashFlowYearFrac': cf_yearFrac, 'CashFlowAmount': cf_amount})

    # filter for payment dates > calc_date
    cashflows_df = cashflows_df[cashflows_df.CashFlowYearFrac > 0]
    return cashflows_df
```

# Problem 2: US Treasury Yield Curve Calibration (On-The-Runs)

## a. Create the On-The-Run US Treasury Bond Objects

Restrict the symbology + market data dataframe to "on-the-run"/OTR US treasury notes/bonds only and create the treasury bond objects.

Extend the treasuries symbology dataframe with the following market data columns (code from Homework 1):

| date | bidPrice | askPrice | midPrice | bidYield | askYield | midYield | term | TTM |
|----------|-------|-------------|-----|----------|---------|---------|---------|---------|

Plot a graph/scatter plot of on-the-run treasury mid yields by TTM.

## b. Calibrate the On-The-Run Treasury Yield Curve (Bootstrapping)

The function below shows how to calibrate a smooth yield/discount factor curve from the on-the-run treasury dataframe.

Calibrate the bid, ask and mid discount factor curves as of 2024-04-08.

Display the calibration results for the mid curve, using get_yield_curve_details_df().

## c. Plot the Calibrated US Treasury Yield (Zero Rate) Curves

Create a graph/scatter plot of the newly computed mid yields by maturity.

## d. Plot Calibrated Discount Factors

Plot the discount factor curve up to the 30 years point, using a 6 months discretization grid.

# Problem 3: Pricing and Risk Metrics for US Treasury Bonds

## a. US Treasury Pricing on the Calibrated Discount Factor Curve

Follow Section 5. "Bond Present Value Calculation (no credit risk)" in the QuantLib Basic notebook to re-price the US on-the-run treasuries using the calibrated discount factor curve.

You will need to switch the bond_engine to use the new on-the-run treasury yield curve:
bond_engine = ql.DiscountingBondEngine(tsy_yield_curve_mid)

Extend the dataframe with the following computed columns for clean mid prices:

| calc_mid_price |
|---------------|

To validate the calibration, compare the calculated clean mid prices to the original market mid prices.

## b. Compute Analytical DV01, Duration and Convexity for US On-The-Run Treasuries (Using Flat Yield)

Compute analytical DV01, Duration and Convexity metrics, as described in Section 7. "Analytical Duration, Convexity and Z-Spread (flat yield model)" in the QuantLib Basic notebook.

Remember that DV01 = Dirty_Price * Duration.

Extend the dataframe with the following calculated risk metrics:

| dv01 | duration | convexity |
|-------|-------|-------------|

## c. Compute Scenario DV01, Duration and Convexity for US On-The-Run Treasuries (Using Calibrated Yield Curve)

Compute the scenario DV01, Duration and Convexity metrics using +/-1 bp interest rate shocks, as described in Section 6. "Market Data Scenarios" in the QuantLib Basic notebook.

Remember that DV01 = Dirty_Price * Duration.

Extend the dataframe with the following scenario sensitivities metrics:

| scen_dv01 | scen_duration | scen_convexity |
|-------|-------|-------------|

# Problem 4: Pricing and Risk Metrics for Corporate Bonds

## a. Create the Fixed-Rate Corporate Bond Objects

Restrict the symbology dataframe to fixed rate Corporate Bonds only and create the corporate bond objects.

## b. Compute Analytical Yields and Z-Spreads

Compute analytical Yields and Z-Spreads metrics, as described in Section 7. "Analytical Duration, Convexity and Z-Spread (flat yield model)" in the QuantLib Basic notebook.

Extend the dataframe with the following calculated risk metrics:

| calc_yield | calc_zspread |
|-------|-------------|

## c. Validate Z-Spread Computation for a Few Fixed Rate Corporate Bonds

Pick 3 Corporate Bonds (at your discretion) and use function below to re-price them using the calibrated flat z-spread. Follow the example in Section 7. "Analytical Duration, Convexity and Z-Spread (flat yield model)".

Validate that you match the original market prices, which were used as input to the z-Spread function.

## d. Compute Duration and Convexity for Fixed Rate Corporate Bonds (Using Flat Yield)

Compute analytical Duration and Convexity metrics, as described in Section 7. "Analytical Duration, Convexity and Z-Spread (flat yield model)" in the QuantLib Basic notebook.

Extend the dataframe with the following calculated risk metrics:

| calc_duration | calc_convexity |
|-------|-------------|

Display the head of the dataframe.
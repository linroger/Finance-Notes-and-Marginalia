---
title: Credit Markets Homework 3
cssclasses:
- academia
tags:
- abs
- bond
- bond_pricing
- bootstrapping
- bps
- cds_calibration
- convexity
- corporate-bond
- credit-derivatives
- credit-risk
- credit-spread
- credit_market_homework
- defi
- duration
- duration_convexity
- dv01
- fixed_rate_bond
- future
- hazard_rates
- interest-rate
- ois
- perpetual_bond
- risk_metrics
- scenario_analysis
- sofr
- sofr_swap
- swap
- treasury
- yield-curve
- yield_curve
- z-spread
aliases:
- Credit Markets
- Homework 3
- Perpetual Bond
- SOFR Curve
key_concepts:
- Basis swap mechanics
- Bond price and risk analysis
- CDS spread calibration
- Convexity adjustment
- Cross-currency basis
- Currency swap structure
- DV01 and duration calculations
- DV01 calculation
- Derivative securities
- Duration measurement
- Financial risk management
- Fixed rate corporate bond pricing
- Fixed vs floating leg
- Hazard rate curves
- Hedging with bonds
- Interest rate sensitivity
- Interest rate swap pricing
- Modified duration calculation
- Perpetual bond valuation
- Portfolio immunization
- Portfolio optimization
- Present value of swaps
- Price-yield relationship
- Quantitative financial analysis
- Risk assessment and mitigation
- SOFR yield curve calibration
- Scenario analysis for bonds
- Swap curve construction
- Swaption valuation
- US SOFR swap curve bootstrapping
---

# Credit Markets Homework 3
This homework relies on:

- The SOFR Is symbology file `sofr_swap_symbology`,
- The SOFR swaps market data file `sofr_swaps_market_data_eod` and
- The CDS spreads market data file `cds_market_data_eod`.
---

# Problem 1: Risk & Scenario analysis for a fixed rate corporate bond (yield model)
## Use the QuantLib Basic notebook (or previous homeworks) as templates
```python
import QuantLib as ql
import numpy as np
import pandas as pd
import datetime as dt

def get_ql_date(date) -> ql.Date:
    """
    Convert dt.date to ql.Date
    """
    if isinstance(date, dt.date):
        return ql.Date(date.day, date.month, date.year)
    elif isinstance(date, str):
        date = dt.datetime.strptime(date, "%Y-%m-%d").date()
        return ql.Date(date.day, date.month, date.year)
    else:
        raise ValueError(f"to_qldate, {type(date)}, {date}")

def create_schedule_from_symbology(details: dict):
    '''Create a QuantLib cashflow schedule from symbology details dictionary (usually one row of the symbology dataframe)
    '''

    # Create maturity from details['maturity']
    maturity = get_ql_date(details['maturity'])

    # Create acc_first from details['acc_first']
    acc_first = get_ql_date(details['acc_first'])

    # Create calendar for Corp and Govt asset classes
    calendar = ql.UnitedStates(ql.UnitedStates.GovernmentBond)

    # define period from details['cpn_freq'] … Can be hard-coded to 2 = semi-annual frequency
    period = ql.Period(2)

    # business_day_convention
    business_day_convention = ql.Unadjusted

    # termination_date_convention
    termination_date_convention = ql.Unadjusted

    # date_generation
    date_generation = ql.DateGeneration.Backward

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

def calibrate_yield_curve_from_frame(
        calc_date: ql.Date,
        treasury_details: pd.DataFrame,
        price_quote_column: str):
    '''Create a calibrated yield curve from a details dataframe which includes bid/ask/mid price quotes.
    '''
    ql.Settings.instance().evaluationDate = calc_date

    # Sort dataframe by maturity
    sorted_details_frame = treasury_details.sort_values(by='maturity')

    # For US Treasuries use ql.ActualActual(ql.ActualActual.ISMA)
    day_count = ql.ActualActual(ql.ActualActual.ISMA)

    bond_helpers = []

    for index, row in sorted_details_frame.iterrows():
        bond_object = create_bond_from_symbology(row)

        tsy_clean_price_quote = row[price_quote_column]
        tsy_clean_price_handle = ql.QuoteHandle(ql.SimpleQuote(tsy_clean_price_quote))

        bond_helper = ql.BondHelper(tsy_clean_price_handle, bond_object)
        bond_helpers.append(bond_helper)

    yield_curve = ql.PiecewiseLogCubicDiscount(calc_date, bond_helpers, day_count)
    # yield_curve = ql.PiecewiseFlatForward(calc_date, bond_helpers, day_count)

    yield_curve.enableExtrapolation()
    return yield_curve

def get_yield_curve_details_df(yield_curve, curve_dates=None):

    if (curve_dates == None):
        curve_dates = yield_curve.dates()

    dates = [d.to_date() for d in curve_dates]
    discounts = [round(yield_curve.discount(d), 3) for d in curve_dates]
    yearfracs = [round(yield_curve.timeFromReference(d), 3) for d in curve_dates]
    zeroRates = [round(yield_curve.zeroRate(d, yield_curve.dayCounter(), ql.Compounded).rate() * 100, 3) for d in curve_dates]

    yield_curve_details_df = pd.DataFrame(data={'Date': dates,
                             'YearFrac': yearfracs,
                             'DiscountFactor': discounts,
                             'ZeroRate': zeroRates})
    return yield_curve_details_df

def calc_clean_price_with_zspread(fixed_rate_bond, yield_curve_handle, zspread):
    zspread_quote = ql.SimpleQuote(zspread)
    zspread_quote_handle = ql.QuoteHandle(zspread_quote)
    yield_curve_bumped = ql.ZeroSpreadedTermStructure(yield_curve_handle, zspread_quote_handle, ql.Compounded, ql.Semiannual)
    yield_curve_bumped_handle = ql.YieldTermStructureHandle(yield_curve_bumped)

    # Set Valuation engine
    bond_engine = ql.DiscountingBondEngine(yield_curve_bumped_handle)
    fixed_rate_bond.setPricingEngine(bond_engine)
    bond_clean_price = fixed_rate_bond.cleanPrice()
    return bond_clean_price

def calibrate_sofr_curve_from_frame(
        calc_date: ql.Date,
        sofr_details: pd.DataFrame,
        rate_quote_column: str):
    '''Create a calibrated yield curve from a SOFR details dataframe which includes rate quotes.
    '''
    ql.Settings.instance().evaluationDate = calc_date

    # Sort dataframe by maturity
    sorted_details_frame = sofr_details.sort_values(by='tenor')

    # settle_days
    settle_days = 2

    # For US SOFR OIS Swaps
    day_count = ql.Actual360()

    # For US SOFR Swaps
    calendar = ql.UnitedStates(ql.UnitedStates.GovernmentBond)

    sofr_helpers = []

    for index, row in sorted_details_frame.iterrows():
        sofr_quote = row[rate_quote_column]
        tenor_in_years = row['tenor']
        sofr_tenor = ql.Period(tenor_in_years, ql.Years)

        # create sofr_rate_helper
        sofr_helper = ql.OISRateHelper(settle_days, sofr_tenor, ql.QuoteHandle(ql.SimpleQuote(sofr_quote/100)), ql.Sofr())

        sofr_helpers.append(sofr_helper)

    sofr_yield_curve = ql.PiecewiseLinearZero(settle_days, calendar, sofr_helpers, day_count)
    sofr_yield_curve.enableExtrapolation()

    return sofr_yield_curve

def calibrate_cds_hazard_rate_curve(calc_date, sofr_yield_curve_handle, cds_par_spreads_bps, cds_recovery_rate = 0.4):
    '''Calibrate hazard rate curve from CDS Par Spreads'''
    CDS_settle_days = 2

    CDS_day_count = ql.Actual360()

    # CDS standard tenors: 1Y, 2Y, 3Y, 5Y 7Y and 10Y
    CDS_tenors = [ql.Period(y, ql.Years) for y in [1, 2, 3, 5, 7, 10]]
    CDS_helpers = [ql.SpreadCdsHelper((cds_par_spread / 10000.0), CDS_tenor, CDS_settle_days, ql.TARGET(),
                                  ql.Quarterly, ql.Following, ql.DateGeneration.TwentiethIMM, CDS_day_count, cds_recovery_rate, sofr_yield_curve_handle)

    for (cds_par_spread, CDS_tenor) in zip(cds_par_spreads_bps, CDS_tenors)]

    # bootstrap hazard_rate_curve
    hazard_rate_curve = ql.PiecewiseFlatHazardRate(calc_date, CDS_helpers, CDS_day_count)
    hazard_rate_curve.enableExtrapolation()

    return (hazard_rate_curve)

def get_hazard_rates_df(hazard_rate_curve):
    '''Return dataframe with calibrated hazard rates and survival probabilities'''

    CDS_day_count = ql.Actual360()

    hazard_list = [(hr[0].to_date(),
                CDS_day_count.yearFraction(calc_date, hr[0]),
                hr[1] * 1e4,
                hazard_rate_curve.survivalProbability(hr[0])) for hr in hazard_rate_curve.nodes()]

    grid_dates, year_frac, hazard_rates, surv_probs = zip(*hazard_list)

    hazard_rates_df = pd.DataFrame(data={'Date': grid_dates,
                                     'YearFrac': year_frac,
                                     'HazardRateBps': hazard_rates,
                                     'SurvivalProb': surv_probs})
    return (hazard_rates_df)
```

## a. Create generic fixed-rate corporate bond
Fix the calculation date as of April 15 2024 and use a coupon of 5% and a maturity of 10 years (April 15 2034).

Display the fixed rate bond cashflows.

```python
# Import tools from previous homeworks
# Use static calculation/valuation date of 2024-04-15, matching data available in the market prices EOD file

calc_date = ql.Date(15, 4, 2024)
ql.Settings.instance().evaluationDate = calc_date
```

```python
# Create generic fixed-rate corporate bond
# Fix the calculation date as of April 15 2024

issue_date = ql.Date(15, 4, 2024)
maturity_date = ql.Date(15, 4, 2034)

# Corporate bond parameters

corporate_bond_dict = {
    'class': 'Corp',
    'start_date': issue_date,
    'maturity': maturity_date,
    'acc_first': issue_date,
    'days_settle': 2,
    'coupon': 5.0,  # 5% coupon rate
    'cpn_freq': 2   # semi-annual frequency
}

# Create fixed-rate corporate bond

generic_corporate_bond = create_bond_from_symbology(corporate_bond_dict)

# Display bond cashflows

cashflows_df = get_bond_cashflows(generic_corporate_bond, calc_date)
display(cashflows_df)
```

```python
# Add cash flow YTM

cashflows_df['YTM'] = cashflows_df['CashFlowYearFrac'].round(1)
display(cashflows_df)
```

## b. Calculate risk measures (YTM, DV01, Duration, Convexity)
Calculate the static YTM, DV01, Duration and Convexity (using the 5% YTM flat curve model).

Create a table showing the future cash flows discounted back to the calculation date, using YTM as the discount rate.

```python
# b. Calculate risk measures  (YTM, DV01, Duration, Convexity)
# Calculate the static YTM, DV01, Duration and Convexity (using the 5% YTM flat curve model)
# Let's assume the bond is trading at par
# The YTM is likely 5% since it is a 5% coupon bond trading at par (100)

par_price = 100
ql.Settings.instance().evaluationDate = calc_date

# Set pricing engine with flat yield term structure

ytm_rate = 0.05
flat_curve = ql.FlatForward(calc_date, ytm_rate, ql.Thirty360(ql.Thirty360.USA), ql.Compounded, ql.Semiannual)
flat_curve_handle = ql.YieldTermStructureHandle(flat_curve)

# Set pricing engine

bond_engine = ql.DiscountingBondEngine(flat_curve_handle)
generic_corporate_bond.setPricingEngine(bond_engine)

# Calculate risk measures

bond_yield = generic_corporate_bond.bondYield(par_price, ql.Thirty360(ql.Thirty360.USA), ql.Compounded, ql.Semiannual, calc_date)
dv01 = ql.BondFunctions.basisPointValue(generic_corporate_bond, ql.InterestRate(bond_yield, ql.Thirty360(ql.Thirty360.USA), ql.Compounded, ql.Semiannual))
duration = ql.BondFunctions.duration(generic_corporate_bond, ql.InterestRate(bond_yield, ql.Thirty360(ql.Thirty360.USA), ql.Compounded, ql.Semiannual), ql.Duration.Modified)
convexity = ql.BondFunctions.convexity(generic_corporate_bond, ql.InterestRate(bond_yield, ql.Thirty360(ql.Thirty360.USA), ql.Compounded, ql.Semiannual))

print(f"YTM: {bond_yield*100:.3f}%")
print(f"DV01: ${dv01:.6f}")
print(f"Duration: {duration:.3f} years")
print(f"Convexity: {convexity:.3f}")
```

```python
# Create a table showing the future cash flows discounted back to the calculation date

day_counter = ql.Thirty360(ql.Thirty360.USA)
cashflows_with_pv = []

for cf in generic_corporate_bond.cashflows():
    cf_date = cf.date()
    if cf_date > calc_date:
        cf_amount = cf.amount()
        year_frac = day_counter.yearFraction(calc_date, cf_date)
        discount_factor = 1 / ((1 + bond_yield/2) ** (2 * year_frac))
        pv = cf_amount * discount_factor

        cashflows_with_pv.append({
            'CashFlowDate': cf_date.to_date(),
            'CashFlowAmount': cf_amount,
            'YearFrac': year_frac,
            'DiscountFactor': discount_factor,
            'PresentValue': pv
        })

cashflows_pv_df = pd.DataFrame(cashflows_with_pv)
display(cashflows_pv_df)

# Verify that sum of PVs equals the bond price

total_pv = cashflows_pv_df['PresentValue'].sum()
print(f"\nSum of PVs: ${total_pv:.6f}")
print(f"Bond Price: ${generic_corporate_bond.cleanPrice():.6f}")
```

## c. Shift the flat curve up by 100 bps and recalculate risk measures
Shift the flat curve up by 100 bps and recalculate the bond price and risk measures.

```python
# c. Shift the flat curve up by 100 bps and recalculate risk measures
# Shift the flat curve up by 100 bps

shifted_ytm_rate = ytm_rate + 0.01  # Add 100 bps
shifted_flat_curve = ql.FlatForward(calc_date, shifted_ytm_rate, ql.Thirty360(ql.Thirty360.USA), ql.Compounded, ql.Semiannual)
shifted_flat_curve_handle = ql.YieldTermStructureHandle(shifted_flat_curve)

# Set pricing engine with shifted curve

shifted_bond_engine = ql.DiscountingBondEngine(shifted_flat_curve_handle)
generic_corporate_bond.setPricingEngine(shifted_bond_engine)

# Recalculate bond price

shifted_bond_price = generic_corporate_bond.cleanPrice()

# Need to recalculate YTM for the new price

shifted_bond_yield = generic_corporate_bond.bondYield(shifted_bond_price, ql.Thirty360(ql.Thirty360.USA), ql.Compounded, ql.Semiannual, calc_date)
shifted_dv01 = ql.BondFunctions.basisPointValue(generic_corporate_bond, ql.InterestRate(shifted_bond_yield, ql.Thirty360(ql.Thirty360.USA), ql.Compounded, ql.Semiannual))
shifted_duration = ql.BondFunctions.duration(generic_corporate_bond, ql.InterestRate(shifted_bond_yield, ql.Thirty360(ql.Thirty360.USA), ql.Compounded, ql.Semiannual), ql.Duration.Modified)
shifted_convexity = ql.BondFunctions.convexity(generic_corporate_bond, ql.InterestRate(shifted_bond_yield, ql.Thirty360(ql.Thirty360.USA), ql.Compounded, ql.Semiannual))

print(f"Original YTM: {bond_yield*100:.3f}%")
print(f"Shifted YTM: {shifted_bond_yield*100:.3f}%")
print(f"\nOriginal Bond Price: ${par_price:.6f}")
print(f"Shifted Bond Price: ${shifted_bond_price:.6f}")
print(f"Price Change: ${shifted_bond_price - par_price:.6f}")
print(f"\nOriginal DV01: ${dv01:.6f}")
print(f"Shifted DV01: ${shifted_dv01:.6f}")
print(f"\nOriginal Duration: {duration:.3f} years")
print(f"Shifted Duration: {shifted_duration:.3f} years")
print(f"\nOriginal Convexity: {convexity:.3f}")
print(f"Shifted Convexity: {shifted_convexity:.3f}")
```

## d. Import swap data and calibrate SOFR curve
Import data from `sofr_swap_symbology`, `sofr_swaps_market_data_eod` and calibrate the US SOFR yield curve.

```python
# d. Import swap data and calibrate SOFR curve
# Import data from sofr_swap_symbology, sofr_swaps_market_data_eod
# Calibrate the US SOFR yield curve
# Load SOFR swap symbology

sofr_swap_symbology = pd.read_excel('data/sofr_swap_symbology.xlsx')
display(sofr_swap_symbology.head())

# Load SOFR swap market data

sofr_swaps_market_data_eod = pd.read_excel('data/sofr_swaps_market_data_eod.xlsx')
display(sofr_swaps_market_data_eod.head())

# Merge symbology with market data

sofr_data = pd.merge(sofr_swap_symbology, sofr_swaps_market_data_eod, on=['ticker', 'figi'])
display(sofr_data.head())

# Calibrate SOFR curve using midRate

sofr_yield_curve = calibrate_sofr_curve_from_frame(calc_date, sofr_data, 'midRate')

# Create yield curve handle

sofr_yield_curve_handle = ql.YieldTermStructureHandle(sofr_yield_curve)

# Display calibrated SOFR curve

sofr_curve_dates = [calc_date + ql.Period(i, ql.Years) for i in range(0, 31)]
sofr_curve_df = get_yield_curve_details_df(sofr_yield_curve, sofr_curve_dates)
display(sofr_curve_df.head(10))
```

```python
# Plot SOFR curve

import matplotlib.pyplot as plt

plt.figure(figsize=(10, 6))
plt.plot(sofr_curve_df['YearFrac'], sofr_curve_df['ZeroRate'], 'b-', linewidth=2)
plt.xlabel('Years')
plt.ylabel('Zero Rate (%)')
plt.title('Calibrated US SOFR Yield Curve')
plt.grid(True)
plt.show()
```

## e. Import CDS data and calibrate hazard rate curve
Import data from `cds_market_data_eod` and calibrate hazard rate curve for BAC.

```python
# e. Import CDS data and calibrate hazard rate curve
# Import data from cds_market_data_eod
# Calibrate hazard rate curve for BAC
# Load CDS market data

cds_market_data_eod = pd.read_excel('data/cds_market_data_eod.xlsx')
display(cds_market_data_eod.head())

# Filter for BAC CDS spreads

bac_cds_data = cds_market_data_eod[cds_market_data_eod['ticker'] == 'BAC'].copy()
display(bac_cds_data)

# Extract CDS par spreads for standard tenors
# Assuming columns: 1Y, 2Y, 3Y, 5Y, 7Y, 10Y

cds_columns = ['1Y', '2Y', '3Y', '5Y', '7Y', '10Y']
bac_cds_spreads = []
for col in cds_columns:
    if col in bac_cds_data.columns:
        bac_cds_spreads.append(bac_cds_data[col].iloc[0])

# Calibrate hazard rate curve

hazard_rate_curve = calibrate_cds_hazard_rate_curve(calc_date, sofr_yield_curve_handle, bac_cds_spreads)

# Display hazard rates

hazard_rates_df = get_hazard_rates_df(hazard_rate_curve)
display(hazard_rates_df)
```

## f. Combined yield plus credit scenario price, DV01, and Duration
Use the calibrated US SOFR yield curve and calibrated BAC hazard rate curve + 40% recovery rate.

Find the z-spread such that the generic fixed-rate corporate bond prices to par. Change interest rate scenarios (-100 bps, -50 bps, 0 bps, +50 bps, +100 bps) and change BAC credit scenarios (CDS curve down 25%, 10%, flat, up 10%, 25%). Produce 5x5 bond price, DV01, and Duration tables.

```python
# f. Combined yield plus credit scenario price, DV01, and Duration
# Use the calibrated US SOFR yield curve and calibrated BAC hazard rate curve + 40% recovery rate
# Find the z-spread such that the generic fixed-rate corporate bond prices to par
# First, set the bond pricing engine with SOFR curve

bond_engine = ql.DiscountingBondEngine(sofr_yield_curve_handle)
generic_corporate_bond.setPricingEngine(bond_engine)

# Find initial bond price with SOFR curve

initial_price = generic_corporate_bond.cleanPrice()
print(f"Bond price with SOFR curve: ${initial_price:.6f}")

# Find the z-spread that prices the bond to par

target_price = 100.0
tolerance = 0.001
max_iterations = 100

# Use bisection to find z-spread

zspread_low = 0.0
zspread_high = 0.05  # 500 bps

for i in range(max_iterations):
    zspread_mid = (zspread_low + zspread_high) / 2
    current_price = calc_clean_price_with_zspread(generic_corporate_bond, sofr_yield_curve_handle, zspread_mid)

    if abs(current_price - target_price) < tolerance:
        break
    elif current_price > target_price:
        zspread_low = zspread_mid
    else:
        zspread_high = zspread_mid

calibrated_zspread = zspread_mid
print(f"Calibrated z-spread: {calibrated_zspread*10000:.1f} bps")
```

```python
# Create scenarios
# Interest rate scenarios: -100 bps, -50 bps, 0 bps, +50 bps, +100 bps

ir_scenarios = [-0.01, -0.005, 0, 0.005, 0.01]
ir_labels = ['-100bps', '-50bps', 'flat', '+50bps', '+100bps']

# Credit scenarios: CDS curve down 25%, 10%, flat, up 10%, 25%

credit_scenarios = [0.75, 0.9, 1.0, 1.1, 1.25]
credit_labels = ['down 25%', 'down 10%', 'flat', 'up 10%', 'up 25%']

# Initialize results tables

price_table = pd.DataFrame(index=credit_labels, columns=ir_labels)
dv01_table = pd.DataFrame(index=credit_labels, columns=ir_labels)
duration_table = pd.DataFrame(index=credit_labels, columns=ir_labels)

# Calculate scenarios

for i, credit_mult in enumerate(credit_scenarios):
    for j, ir_shift in enumerate(ir_scenarios):
        # Shift SOFR curve
        shifted_sofr_curve = ql.ZeroSpreadedTermStructure(
            sofr_yield_curve_handle,
            ql.QuoteHandle(ql.SimpleQuote(ir_shift))
        )
        shifted_sofr_handle = ql.YieldTermStructureHandle(shifted_sofr_curve)

        # Adjust credit spread
        adjusted_zspread = calibrated_zspread * credit_mult

        # Calculate bond price with shifted curves
        scenario_price = calc_clean_price_with_zspread(generic_corporate_bond, shifted_sofr_handle, adjusted_zspread)

        # Calculate risk measures
        bond_engine = ql.DiscountingBondEngine(shifted_sofr_handle)
        generic_corporate_bond.setPricingEngine(bond_engine)

        scenario_yield = generic_corporate_bond.bondYield(scenario_price, ql.Thirty360(ql.Thirty360.USA), ql.Compounded, ql.Semiannual, calc_date)
        scenario_dv01 = ql.BondFunctions.basisPointValue(generic_corporate_bond, ql.InterestRate(scenario_yield, ql.Thirty360(ql.Thirty360.USA), ql.Compounded, ql.Semiannual))
        scenario_duration = ql.BondFunctions.duration(generic_corporate_bond, ql.InterestRate(scenario_yield, ql.Thirty360(ql.Thirty360.USA), ql.Compounded, ql.Semiannual), ql.Duration.Modified)

        # Store results
        price_table.iloc[i, j] = scenario_price
        dv01_table.iloc[i, j] = scenario_dv01
        duration_table.iloc[i, j] = scenario_duration

# Display tables

print("Bond Price Scenarios:")
display(price_table)

print("\nDV01 Scenarios:")
display(dv01_table)

print("\nDuration Scenarios:")
display(duration_table)
```
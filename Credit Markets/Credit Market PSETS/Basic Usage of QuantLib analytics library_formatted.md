---
title: Basic Usage of QuantLib Analytics Library
tags:
- analytics
- bond
- bond_pricing
- bond_yield
- bootstrap_calibration
- bps
- call
- cashflow_schedule
- convexity
- credit-risk
- defi
- discount_curve
- duration
- duration_convexity
- dv01
- fixed_income
- interest-rate
- interest_rate_scenarios
- quantlib
- sofr
- treasury
- yield-curve
- yield_curve
- z-spread
- z_spread
cssclasses:
- tutorial
aliases:
- QuantLib Example
- QuantLib Tutorial
- QuantLib Basic Usage
- Python Bond Pricing
key_concepts:
- Bond price to yield conversions
- Bond pricing and valuation
- Cashflow schedule generation
- Clean vs dirty prices
- Convexity adjustment
- DV01 calculation
- Day-count conventions
- Derivative securities
- Discount curve modeling
- Duration and convexity calculation
- Duration measurement
- Financial risk management
- Fixed and floating rate bonds
- Hedging with bonds
- Interest rate scenarios
- Interest rate sensitivity
- Modified duration calculation
- Portfolio immunization
- Portfolio optimization
- Present value calculation
- Price-yield relationship
- QuantLib library fundamentals
- Quantitative financial analysis
- Quote objects and handles
- Risk assessment and mitigation
- Yield curve calibration
- Yield curve construction
- Z-spread computation
---

# Basic Usage of QuantLib Analytics Library
## More Details $\$a_t$$: https://quantlib-python-docs.readthedocs.io/en/latest/
- 1\. Objects and Handles
  - a. Define a quote object and inspect the value
  - b. Define quoteHandle as a handle/smart pointer to the quote object
  - c. Calendars and day-count conventions
- 2\. Cashflow Schedules
  - a. Construct semi-annual cashflow schedule object, for fixed-rate bonds
  - b. Inspect the semi-annual cashflow schedule
  - c. Construct quarterly cashflow schedule object, for floating-rate bonds
  - d. Inspect the quarterly cashflow schedule
- 3\. Discount Curve / Yield Curve Term Structure
  - a. Constructing a Flat Yield Curve
  - b. Inspect the discount curve
- 4\. Fixed and Floating Rate Bonds
  - a. Constructing a fixed rate bond object
  - b. Investigate the fixed-rate bond cash-flows
  - c. Constructing a floating rate bond object: linked to SOFR index
- 5\. Bond Present Value Calculation (no credit risk)
  - a. Direct function call using risk-free bond pricing engine
  - b. Manual Calculation to validate PV (for fixed and floating-rate bonds)
  - c. Bond Clean vs Dirty Prices (adjusted to settle date)
- 6\. Market Data Scenarios
  - a. Apply +/-1 bp parallel shift scenarios in interest rates curve and compute scenario prices
  - b. Compute scenario DV01, duration and convexity
  - c. Yield to Price conversions
  - d. Price to Yield conversions
- 7\. Analytical Duration, Convexity and Z-Spread (flat yield model)
  - a. Compute bond duration, convexity and Z-Spread
  - b. Validate Z-Spread
- 8\. Treasury Yield Curve Calibration (via Bootstrapping)
  - a. Calibrate treasury flat yield curve (simple case of one calibration instrument)
  - b. Display the calibrated Treasury discount curve dataframe
  - c. Plot the calibrated Treasury Zero Rates and Discount Factors curves
  - d. Reprice the bond on the yield curve to validate the calibration
```python
import QuantLib as ql
import numpy as np
import pandas as pd
```

## 1. Objects and Handles
### a. Define a Quote Object and Inspect the Value
```python
quote = ql.SimpleQuote(0.01)
print(quote.value())

quote.setValue(0.02)
print(quote.value())
```

```
0. 01
0. 02
```

### b. Define QuoteHandle as a Handle/Smart Pointer to the Quote Object
```python
quoteHandle = ql.QuoteHandle(quote)
quoteHandle.value()
```

```
0. 02
```

#### When the Quote Object is Changed, the QuoteHandle Changes Value as Well
```python
quote.setValue(0.03)
quoteHandle.value()
```

```
0. 03
```

### c. Calendars and Day-Count Conventions
```python
# Dates

todays_date = ql.Date.todaysDate()
test_date = todays_date + 90
print('todays_date =', todays_date)
print('test_date =', test_date)

# Calendars

calendar = ql.UnitedStates(ql.UnitedStates.GovernmentBond)
holiday_list = list(calendar.holidayList(todays_date, test_date))
print('holiday_list =', holiday_list)

# Day count conventions

day_count = ql.Actual360()
print('day_count =', day_count)

# Year fractions

test_year_fraction = day_count.yearFraction(todays_date, test_date)
print('Year Fraction from', todays_date, 'to', test_date, '=', test_year_fraction)
```

```
todays_date = May 4th, 2024
test_date = August 2nd, 2024
holiday_list = [Date(27, 5, 2024), Date(19, 6, 2024), Date(4, 7, 2024)]
day_count = Actual/360 day counter
Year Fraction from May 4th, 2024 to August 2nd, 2024 = 0.25
```

## 2. Cashflow Schedules
### a. Construct Semi-Annual Cashflow Schedule Object, for Fixed-Rate Bonds
```python
issue_date = ql.Date(2, 4, 2024)        # 2024-04-02
maturity_date = ql.Date(2, 4, 2028)     # 2028-04-02
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

### b. Inspect the Semi-Annual Cashflow Schedule
- Use list() to get a list of all the dates in Schedule, and len() to get number of dates
- Use [] for random access
- Use startDate(), endDate()
```python
print("All dates: ", list(fixed_rate_schedule))
print("Length: ", len(fixed_rate_schedule))
print("The 3rd coupon date: ", fixed_rate_schedule[3])  # random access
print("Start Date: ", fixed_rate_schedule.startDate())
print("End Date: ", fixed_rate_schedule.endDate())
```

```
All dates: [Date(2, 4, 2024), Date(2, 10, 2024), Date(2, 4, 2025), Date(2, 10, 2025), Date(2, 4, 2026), Date(2, 10, 2026), Date(2, 4, 2027), Date(2, 10, 2027), Date(2, 4, 2028)]
Length: 9
The 3rd coupon date: QuantLib.Schedule
Start Date: April 2nd, 2024
End Date: April 2nd, 2028
```

### c. Construct Quarterly Cashflow Schedule Object, for Floating-Rate Bonds
```python
# Floating_rate_bond_schedule

floating_rate_schedule = ql.Schedule(
    issue_date,
    maturity_date,
    ql.Period(ql.Quarterly),
    calendar,
    day_count_conv,
    day_count_conv,
    date_generation,
    month_end,
)
```

### d. Inspect the Quarterly Cashflow Schedule
```python
print("All dates: ", list(floating_rate_schedule))
print("Length: ", len(floating_rate_schedule))
print("Start Date: ", fixed_rate_schedule.startDate())
print("End Date: ", fixed_rate_schedule.endDate())
```

```
All dates: [Date(2, 4, 2024),
            Date(2, 7, 2024),
            Date(2, 10, 2024),
            Date(2, 1, 2025),
            Date(2, 4, 2025),
            Date(2, 7, 2025),
            Date(2, 10, 2025),
            Date(2, 1, 2026),
            Date(2, 4, 2026),
            Date(2, 7, 2026),
            Date(2, 10, 2026),
            Date(2, 1, 2027),
            Date(2, 4, 2027),
            Date(2, 7, 2027),
            Date(2, 10, 2027),
            Date(2, 1, 2028),
            Date(2, 4, 2028)]
Length: 17
Start Date: April 2nd, 2024
End Date: April 2nd, 2028
```

## 3. Discount Curve / Yield Curve Term Structure
### a. Constructing a Flat Yield Curve
```python
# Set the static valuation date: 2024-04-02

calc_date = ql.Date(2, 4, 2024)
ql.Settings.instance().evaluationDate = calc_date

# Using 5% flat interest rate for testing

flat_rate = ql.SimpleQuote(0.05)
rate_handle = ql.QuoteHandle(flat_rate)
day_count = ql.Actual360()
calendar = ql.UnitedStates(ql.UnitedStates.GovernmentBond)
continuous_comp = ql.Continuous # continously compounded rate of 5%
flat_yield_curve = ql.FlatForward(calc_date, rate_handle, day_count, continuous_comp)
flat_yield_curve_handle = ql.YieldTermStructureHandle(flat_yield_curve)
```

### b. Inspect the Discount Curve
```python
ref_date = flat_yield_curve.referenceDate()
test_date = ql.Date(30, 6, 2025)

# Calc year fraction between ref_date and test_date

yearFrac = flat_yield_curve.dayCounter().yearFraction(ref_date, test_date)

print("Reference Date =", ref_date)
print("Test Date =", test_date)
print("Year Fraction between Reference Date and Test Date : ", yearFrac)
print("Discount Factor for Test Date", test_date, ": ", flat_yield_curve.discount(test_date))
print("custom DF calculation for Test Date", test_date, ": ", np.exp(-flat_rate.value() * yearFrac))
print("Difference in Discount Factor: ", flat_yield_curve.discount(test_date) - np.exp(-flat_rate.value() * yearFrac))
```

```
Reference Date = April 2nd, 2024
Test Date = June 30th, 2025
Year Fraction between Reference Date and Test Date : 1.261111111111111
Discount Factor for Test Date June 30th, 2025 : 0.9388913116117773
Custom DF calculation for Test Date June 30th, 2025 : 0.9388913116117772
Difference in Discount Factor: 1.1102230246251565e-16
```

## 4. Fixed and Floating Rate Bonds
### a. Constructing a Fixed Rate Bond Object
```python
# Day_count: ACT/ACT for Govt bonds

day_count_govt = ql.ActualActual(ql.ActualActual.ISMA)

# Day_count: 30/360 for fixed-rate Corp bonds

day_count_corp_fixed = ql.Thirty360(ql.Thirty360.USA)

# Day_count: ACT/360 for floating-rate bonds

day_count_floater = ql.Actual360()

# Settlement_days: 1 for Govt bonds

settlement_days_govt = 1

# Settlement_days: 2 for Corp Bonds

settlement_days_corp = 2

# Govt Bonds specs

day_count = day_count_govt
settlement_days = settlement_days_govt

# Coupons

coupon_rate = 0.04
coupons = [coupon_rate]

# Payment_convention

payment_convention = ql.Unadjusted

# Face_value

face_value = 100

# Construct the fixed_rate_bond

face_value = 100
fixed_rate_bond = ql.FixedRateBond(
    settlement_days,
    face_value,
    fixed_rate_schedule,
    coupons,
    day_count,
    payment_convention)
```

### b. Investigate the Fixed-Rate Bond Cash-Flows
```python
x = [(cf.date(), cf.amount()) for cf in fixed_rate_bond.cashflows()]
cf_date_fixed, cf_amount = zip(*x)
cf_frame_fixed = pd.DataFrame(data={'CashFlowDate': cf_date_fixed, 'CashFlowAmount': cf_amount})
display(cf_frame_fixed)
```

```
        CashFlowDate  CashFlowAmount
0  October 2nd, 2024             2.0
1    April 2nd, 2025             2.0
2  October 2nd, 2025             2.0
3    April 2nd, 2026             2.0
4  October 2nd, 2026             2.0
5    April 2nd, 2027             2.0
6  October 2nd, 2027             2.0
7    April 2nd, 2028             2.0
8    April 2nd, 2028           100.0
```

### c. Constructing a Floating Rate Bond Object: Linked to SOFR Index
```python
# Sofr_term_structure_handle: using 5% flat interest rate for testing

rate_handle = ql.QuoteHandle(ql.SimpleQuote(5/100))
sofr_term_structure = ql.FlatForward(calc_date, rate_handle, day_count_floater, ql.Continuous)
sofr_term_structure_handle = ql.YieldTermStructureHandle(sofr_term_structure)

# Set SOFR index history

im = ql.IndexManager.instance()
sofr_index = ql.Sofr(sofr_term_structure_handle)

# Set SOFR fixings

im.clearHistory(sofr_index.name())
sofr_index.addFixing(ql.Date(28, ql.March, 2024), 5/100)
sofr_index.addFixing(ql.Date(1, ql.April, 2024), 5/100)

# Floating_rate_bond

floating_rate_bond = ql.FloatingRateBond(settlement_days,
                                face_value,
                                floating_rate_schedule,
                                sofr_index,
                                day_count_floater,
                                payment_convention,
                                spreads=[25/10000],  # 25 bps floating rate
                                issueDate=issue_date)
```

```python
x = [(cf.date(), cf.amount()) for cf in floating_rate_bond.cashflows()]
cf_date_float, cf_amount = zip(*x)
cf_frame_float = pd.DataFrame(data={'CashFlowDate': cf_date_float, 'CashFlowAmount': cf_amount})
print(cf_frame_float)
```

```
        CashFlowDate  CashFlowAmount
0      July 2nd, 2024        1.335104
1   October 2nd, 2024        1.349865
2   January 2nd, 2025        1.349865
3     April 2nd, 2025        1.320345
4      July 2nd, 2025        1.335104
5   October 2nd, 2025        1.349865
6   January 2nd, 2026        1.349865
7     April 2nd, 2026        1.320345
8      July 2nd, 2026        1.335104
9   October 2nd, 2026        1.349865
10  January 2nd, 2027        1.350044
11    April 2nd, 2027        1.320520
12     July 2nd, 2027        1.335104
13  October 2nd, 2027        1.350044
14  January 2nd, 2028        1.350044
15    April 2nd, 2028        1.335370
16    April 2nd, 2028      100.000000
```

## 5. Bond Present Value Calculation (No Credit Risk)
### a. Direct Function Call Using Risk-Free Bond Pricing Engine
```python
# Fixed_rate_bond PV

bond_engine = ql.DiscountingBondEngine(flat_yield_curve_handle)
fixed_rate_bond.setPricingEngine(bond_engine)
fixed_rate_bond_pv = fixed_rate_bond.NPV()
print('fixed_rate_bond_pv =', fixed_rate_bond_pv)

# Floating_rate_bond PV

floating_rate_bond.setPricingEngine(bond_engine)
floating_rate_bond_pv = floating_rate_bond.NPV()
print('floating_rate_bond_pv =', floating_rate_bond_pv)
```

```
fixed_rate_bond_pv = 95.93321956659715
floating_rate_bond_pv = 100.91327849916414
```

### b. Manual Calculation to Validate PV (for Fixed and Floating-Rate Bonds)
```python
# Validate fixed-rate bond PV

used_cf_frame = cf_frame_fixed
used_bond_pv = fixed_rate_bond_pv

# Validate floating-rate bond PV

discount_yearfrac = np.zeros((len(used_cf_frame,)))
discount_factor = np.zeros((len(used_cf_frame,)))

i = 0
for cf_date in used_cf_frame['CashFlowDate']:
    discount_yearfrac[i] = flat_yield_curve.dayCounter().yearFraction(flat_yield_curve.referenceDate(), cf_date)
    discount_factor[i] = flat_yield_curve.discount(cf_date)
    i += 1

used_cf_frame['YearFrac'] = discount_yearfrac
used_cf_frame['DiscountFactor'] = discount_factor
used_cf_frame['NPV'] = used_cf_frame['CashFlowAmount'] * used_cf_frame['DiscountFactor']

used_cf_frame
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
      <th>CashFlowDate</th>
      <th>CashFlowAmount</th>
      <th>YearFrac</th>
      <th>DiscountFactor</th>
      <th>NPV</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>October 2nd, 2024</td>
      <td>2.0</td>
      <td>0.508333</td>
      <td>0.974904</td>
      <td>1.949807</td>
    </tr>
    <tr>
      <th>1</th>
      <td>April 2nd, 2025</td>
      <td>2.0</td>
      <td>1.013889</td>
      <td>0.950569</td>
      <td>1.901138</td>
    </tr>
    <tr>
      <th>2</th>
      <td>October 2nd, 2025</td>
      <td>2.0</td>
      <td>1.522222</td>
      <td>0.926713</td>
      <td>1.853426</td>
    </tr>
    <tr>
      <th>3</th>
      <td>April 2nd, 2026</td>
      <td>2.0</td>
      <td>2.027778</td>
      <td>0.903582</td>
      <td>1.807163</td>
    </tr>
    <tr>
      <th>4</th>
      <td>October 2nd, 2026</td>
      <td>2.0</td>
      <td>2.536111</td>
      <td>0.880905</td>
      <td>1.761810</td>
    </tr>
    <tr>
      <th>5</th>
      <td>April 2nd, 2027</td>
      <td>2.0</td>
      <td>3.041667</td>
      <td>0.858917</td>
      <td>1.717833</td>
    </tr>
    <tr>
      <th>6</th>
      <td>October 2nd, 2027</td>
      <td>2.0</td>
      <td>3.550000</td>
      <td>0.837361</td>
      <td>1.674722</td>
    </tr>
    <tr>
      <th>7</th>
      <td>April 2nd, 2028</td>
      <td>2.0</td>
      <td>4.058333</td>
      <td>0.816346</td>
      <td>1.632693</td>
    </tr>
    <tr>
      <th>8</th>
      <td>April 2nd, 2028</td>
      <td>100.0</td>
      <td>4.058333</td>
      <td>0.816346</td>
      <td>81.634627</td>
    </tr>
  </tbody>
</table>
</div>

```python
pv_manual = used_cf_frame['NPV'].sum()
print('NPV engine = ', used_bond_pv)
print('NPV manual = ', pv_manual)
print('NPV diff = ', pv_manual - used_bond_pv)
```

```
NPV engine = 95.93321956659715
NPV manual = 95.93321956659715
NPV diff = 0.0
```

### c. Bond Clean vs Dirty Prices (Adjusted to Settle Date)
```python
print('Bond Notional = ', fixed_rate_bond.notional())
print('Settle Date = ', fixed_rate_bond.settlementDate())
print('Discount Factor to Settle Date = ', round(flat_yield_curve_handle.discount(fixed_rate_bond.settlementDate()), 4))
print('Bond NPV (Calc Date) = ', round(fixed_rate_bond.NPV(), 4))
print('Bond NPV Adjusted to Settle Date = ', round(fixed_rate_bond.NPV() / flat_yield_curve_handle.discount(fixed_rate_bond.settlementDate()), 4))
print('Bond Dirty Price = ', round(fixed_rate_bond.dirtyPrice(), 4))
print('Bond Clean Price = ', round(fixed_rate_bond.cleanPrice(), 4))
print('Bond Accrued = ', round(fixed_rate_bond.accruedAmount(), 4))
```

```
Bond Notional = 100.0
Settle Date = April 3rd, 2024
Discount Factor to Settle Date = 0.9999
Bond NPV (Calc Date) = 95.9332
Bond NPV Adjusted to Settle Date = 95.9465
Bond Dirty Price = 95.9465
Bond Clean Price = 95.9356
Bond Accrued = 0.0109
```
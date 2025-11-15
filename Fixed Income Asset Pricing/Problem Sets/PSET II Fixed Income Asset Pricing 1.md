---
aliases:
- Homework 2
- JCH Fixed Income Group
- LIF
- PSET II
enhanced: true
enhancement_date: '2025-11-06'
enhancement_id: batch03-18c420
key_concepts:
- Apt
- Term structure of interest rates
- Term structure of interest rates and yield curve shapes
- Treasury Bonds
- Option Greeks and portfolio risk management
- Expectations hypothesis and liquidity preference theory
- Solution
- Yield curve fitting and interpolation methods
- Interest rate modeling
- Vega and volatility risk management
- Portfolio immunization strategies
- Mathematical Finance
- Spot rates vs. forward rates modeling
- GARCH models and volatility forecasting
- Key rate duration and curve risk
- Course Material
- Cash flows decomposition
- Theta and time decay modeling
- Leveraged Inverse Floaters
- Interest rate derivatives
- Fixed income securities
- Bond pricing and yield analysis
- Quantitative Implementation
- Gamma and convexity adjustments
- Duration calculation
- Capital Structure
- Fixed rate note
- Delta hedging and the replication argument
- Parallel and non-parallel shifts in the yield curve
- Exotic Options
- Duration and convexity measures for bond portfolios
- Delta hedging and Greeks
- Price sensitivity to interest rate changes
- Modified duration vs. Macaulay duration
- Duration and convexity
- Options pricing and payoff structures
- Convexity
linter-yaml-title-alias: FIXED INCOME ASSET PRICING
tags:
- yield-curve
- garch-models
- duration_convexity
- mathematical-finance
- course-material
- capital-structure
- interest_rate_hedge
- apt
- bonds
- greeks
- fixed_income
- leveraged_inverse_floater
- options
- term_sheet
- quantitative-implementation
- duration-convexity
- solution
- treasury-bonds
- interest_rates
- exotic-options
- fixed_income_asset_pricing
title: PSET II Fixed Income Asset Pricing 1
---

# PSET II Fixed Income Asset Pricing 1

Bus 35130
Spring 2024
John Heaton
March 25,  2024

## HOMEWORK 2 DUE AT THE BEGINNING OF CLASS 3

This homework is on the pricing and risk assessment of Leveraged Inverse Floaters. Please,  write the solution to the homework as a clean report addressed to the principals of the fixed income group at JCH Fixed Income Group,  LLP. The principals of JCH Fixed Income Group are very demanding,  so make sure to describe exactly the source of your results. However,  the report must be clean and concise. An appendix to the report may contain any additional material. The data for this homework are collected in the data file *HW2 Data.xls* available on canvas. Note 1: For each section below,  there are questions that require pencil and paper (PP) answers,  and questions that require actual computation using data and computer programs (CP). You are to do both. Note 2: As with previous homework assignments there are "guides" for doing the homework in Excel,  Matlab and Python. In each code provides partial solutions to the questions.

To make the code run you are required to complete some formulas or to produce some of the results yourself. You are not required to use any of the guides,  but use of one of them is recommended.

## LEVERAGE INVERSE FLOATERS

Recommended Reading: Veronesi's Book. Chapter 2 (esp. 2.8); Chapter 3 (esp. 3.7) In an environment of low interest rates,  inverse floaters are popular investment vehicles that allow a fund manager to obtain a higher yield,  by betting on the direction of the movement in interest rates. In particular,  consider the following term sheet for a Leveraged Inverse Floater.

## LEVERAGED INVERSE FLOATER TERM SHEET

 | Date | February 17,    2009 | 
 | ------------------------- | ---------------------------------------------------------- | 
 | Maturity | February 17,    2014 (5 year) | 
 | Payments Frequency | Semi-annual | 
 | Interest Payment | Base Interest Rate minus 2 times Reference Interest Rate | 
 | Base Interest Rate | 10% | 
 | Reference Interest Rate | 6 month T-bill rate with standard 6 month lag | 

### GENERAL EQUATIONS
#### Z-FACTOR

The Z-Factor is calculated as:
$$Z = \frac{P}{F}$$

where:

- $P$is the price of the bond.
- $F$is the face value of the bond.
#### CONTINUOUSLY COMPOUNDED YIELD

The Continuously Compounded Yield is calculated using the formula:
$$Y_{cc} = \frac{\ln(\frac{F + C}{P})}{T}$$

where:

- $F$is the face value of the bond.
- $C$is the coupon payment.
- $P$is the price of the bond.
- $T$is the time to maturity in years.
- $\ln$denotes the natural logarithm.
#### SEMI ANNUALLY COMPOUNDED YIELD

The Semi Annually Compounded Yield is calculated using the formula:
$$Y_{sa} = 2 \times \left[\left(\frac{F + C}{P} \right)^{\frac{1}{2T}} - 1 \right]$$

where:

- $F$is the face value of the bond.
- $C$is the coupon payment.
- $P$is the price of the bond.
- $T$is the time to maturity in years.
### CALCULATIONS FOR MATURITIES 0.5,  1,  AND 1.5 YEARS
#### MATURITY 0.5 YEARS
- **Given Values**:
- Price ($P$): 100.5
- Face Value ($F$): 100
- Coupon Payment ($C$): 1.25 (Assuming a 2.5% annual coupon rate,  prorated for 0.5 years)
- Time to Maturity ($T$): 0.5
- **Z-Factor**:
$$Z = \frac{P}{F} = \frac{100.5}{100} = 1.005$$

- **Continuously Compounded Yield**:
$$Y_{cc} = \frac{\ln(\frac{F + C}{P})}{T} = \frac{\ln(\frac{100 + 1.25}{100.5})}{0.5} \approx 0.005992$$

- **Semi Annually Compounded Yield**:
$$Y_{sa} = 2 \times \left[\left(\frac{F + C}{P} \right)^{\frac{1}{2T}} - 1 \right] = 2 \times \left[\left(\frac{100 + 1.25}{100.5} \right)^{\frac{1}{1}} - 1 \right] \approx 0.006001$$

#### MATURITY 1 YEAR
- **Given Values**:
- Price ($P$): 101
- Face Value ($F$): 100
- Coupon Payment ($C$): 2.5 (Assuming a 2.5% annual coupon rate)
- Time to Maturity ($T$): 1
- **Z-Factor**:
$$Z = \frac{P}{F} = \frac{101}{100} = 1.01$$

- **Continuously Compounded Yield**:
$$Y_{cc} = \frac{\ln(\frac{F + C}{P})}{T} = \frac{\ln(\frac{100 + 2.5}{101})}{1} \approx -0.024170$$

- **Semi Annually Compounded Yield**:
$$Y_{sa} = 2 \times \left[\left(\frac{F + C}{P} \right)^{\frac{1}{2T}} - 1 \right] = 2 \times \left[\left(\frac{100 + 2.5}{101} \right)^{\frac{1}{2}} - 1 \right] \approx -0.024024$$

#### MATURITY 1.5 YEARS
- **Given Values**:
- Price ($P$): 101.5
- Face Value ($F$): 100
- Coupon Payment ($C$): 3.75 (Assuming a 2.5% annual coupon rate,  prorated for 1.5 years)
- Time to Maturity ($T$): 1.5
- **Z-Factor**:
$$Z = \frac{P}{F} = \frac{101.5}{100} = 1.015$$

- **Continuously Compounded Yield**:
$$Y_{cc} = \frac{\ln(\frac{F + C}{P})}{T} = \frac{\ln(\frac{100 + 3.75}{101.5})}{1.5} \approx -0.030738$$

- **Semi Annually Compounded Yield**:
$$Y_{sa} = 2 \times \left[\left(\frac{F + C}{P} \right)^{\frac{1}{2T}} - 1 \right] = 2 \times \left[\left(\frac{100 + 3.75}{101.5} \right)^{\frac{1}{3}} - 1 \right] \approx -0.030503$$

---

# GENERAL EQUATIONS

## Z-FACTOR

The Z-Factor is calculated as:
$$Z = \frac{P}{F}$$

where:

- $P$is the price of the bond.
- $F$is the face value of the bond (assumed to be 100).

## CONTINUOUSLY COMPOUNDED YIELD

The Continuously Compounded Yield is calculated using the formula:
$$Y_{cc} = \frac{\ln(\frac{F + C}{P})}{T}$$

where:

- $F$is the face value of the bond (assumed to be 100).
- $C$is the coupon payment.
- $P$is the price of the bond.
- $T$is the time to maturity in years.
- $\ln$denotes the natural logarithm.

## SEMI ANNUALLY COMPOUNDED YIELD

The Semi Annually Compounded Yield is calculated using the formula:
$$Y_{sa} = 2 \times \left[\left(\frac{F + C}{P} \right)^{\frac{1}{2T}} - 1 \right]$$

where:

- $F$is the face value of the bond (assumed to be 100).
- $C$is the coupon payment.
- $P$is the price of the bond.
- $T$is the time to maturity in years.

# CALCULATIONS FOR MATURITIES 0.5,  1,  AND 1.5 YEARS

## MATURITY 0.5 YEARS
- Price ($P$): 102.6953
- Face Value ($F$): 100 (assumed)
- Coupon Payment ($C$): 100 × 0.03 × 0.5 = 1.5 (semi-annual coupon rate of 0.03,  prorated for 0.5 years)
- Time to Maturity ($T$): 0.5

### Z-FACTOR
$$Z = \frac{P}{F} = \frac{102.6953}{100} = 1.026953$$

### CONTINUOUSLY COMPOUNDED YIELD
$$Y_{cc} = \frac{\ln(\frac{F + C}{P})}{T} = \frac{\ln(\frac{100 + 1.5}{102.6953})}{0.5} \approx 0.054429$$

### SEMI ANNUALLY COMPOUNDED YIELD
$$Y_{sa} = 2 \times \left[\left(\frac{F + C}{P} \right)^{\frac{1}{2T}} - 1 \right] = 2 \times \left[\left(\frac{100 + 1.5}{102.6953} \right)^{\frac{1}{1}} - 1 \right] \approx 0.054921$$

## MATURITY 1 YEAR
- Price ($P$): 105.7617
- Face Value ($F$): 100 (assumed)
- Coupon Payment ($C$): 100 × 0.0325 = 3.25 (semi-annual coupon rate of 0.0325)
- Time to Maturity ($T$): 1

### Z-FACTOR
$$Z = \frac{P}{F} = \frac{105.7617}{100} = 1.057617$$

### CONTINUOUSLY COMPOUNDED YIELD
$$Y_{cc} = \frac{\ln(\frac{F + C}{P})}{T} = \frac{\ln(\frac{100 + 3.25}{105.7617})}{1} \approx -0.031734$$

### SEMI ANNUALLY COMPOUNDED YIELD
$$Y_{sa} = 2 \times \left[\left(\frac{F + C}{P} \right)^{\frac{1}{2T}} - 1 \right] = 2 \times \left[\left(\frac{100 + 3.25}{105.7617} \right)^{\frac{1}{2}} - 1 \right] \approx -0.031438$$

## MATURITY 1.5 YEARS
- Price ($P$): 107.7109
- Face Value ($F$): 100 (assumed)
- Coupon Payment ($C$): 100 × 0.0288 × 1.5 = 4.32 (semi-annual coupon rate of 0.0288,  prorated for 1.5 years)
- Time to Maturity ($T$): 1.5

### Z-FACTOR
$$Z = \frac{P}{F} = \frac{107.7109}{100} = 1.077109$$

### CONTINUOUSLY COMPOUNDED YIELD
$$Y_{cc} = \frac{\ln(\frac{F + C}{P})}{T} = \frac{\ln(\frac{100 + 4.32}{107.7109})}{1.5} \approx -0.035018$$

### SEMI ANNUALLY COMPOUNDED YIELD
$$Y_{sa} = 2 \times \left[\left(\frac{F + C}{P} \right)^{\frac{1}{2T}} - 1 \right] = 2 \times \left[\left(\frac{100 + 4.32}{107.7109} \right)^{\frac{1}{3}} - 1 \right] \approx -0.034654$$

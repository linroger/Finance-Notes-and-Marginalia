---
aliases:
- Employee Stock Options Valuation
- ESO Analysis
- Stock-Based Compensation
cssclasses:
- academia
enhanced: true
enhancement_date: '2025-11-06'
enhancement_id: batch03-9c50f9
key_concepts:
- Vesting periods
- Apt
- Treasury stock method
- Accounting for stock compensation
- Treasury Futures
- Cash-equivalent cost of grants
- Interest rate swap valuation and fixed-floating spreads
- American Options
- Monte Carlo simulation techniques for path-dependent options
- Treasury Bonds
- Real options valuation in corporate investment decisions
- Binomial option pricing model for American-style options
- Greeks calculation and their interpretation in options trading
- Single-name vs. index CDS trading
- Option Greeks and portfolio risk management
- Collateralized Debt Obligations
- Commodity markets and pricing dynamics
- Mathematical derivation of the Black-Scholes partial differential equation
- Exercise behavior
- Solution
- Credit spread decomposition and hazard rates
- Vega and volatility risk management
- option pricing models and PDE solutions
- CDS clearing and central counterparties
- Commodity futures pricing and storage costs
- CDS-Bond basis and arbitrrage opportunities
- Swap spread and credit risk considerations
- Credit default swap pricing and recovery assumptions
- GARCH models and volatility forecasting
- ESOs align management interests
- expense recognition and matching
- Implied Volatility
- Fixed-for-floating swap cash flows and valuation
- Theta and time decay modeling
- Risk-neutral pricing methodology for derivative securities
- Synthetic credit derivatives and index trades
- Treasury futures trading and basis point value calculations
- CVA and DVA adjustments in derivative pricing
- Interest rate swap pricing and valuation
- Valuation of compensation tricky
- Risk-neutral valuation in continuous time models
- Credit default swap pricing and risk-neutral probabilities
- Variance swaps and volatility trading strategies
- Employee stock options impact valuation
- fair value measurement and hierarchy
- Delta hedging strategies in options portfolio management
- Theta decay modeling for time-sensitive options strategies
- Implied volatility extraction from market option prices
- Boundary conditions and parameter interpretation in Black-Scholes model
- Limitations and extensions of the Black-Scholes framework
- High-growth firms use ESOs
- Quantitative Implementation
- Volatility smile and skew modeling in options markets
- Gamma and convexity adjustments
- Black-Scholes valuation
- Delta hedging and the replication argument
- Cross-currency basis swaps and funding
- Stock-based compensation at Google
- Black-Scholes-Merton option pricing model and its applications
- Option dilution effects
linter-yaml-title-alias: Week 4 ESOs and Valuation
tags:
- treasury-futures
- commodities
- credit-default-swaps
- collateralized-debt-obligations
- stock_options
- garch-models
- interest-rate-swaps
- mathematical-finance
- accounting_for_esos
- course-material
- option_dilution
- financial-modeling
- equity_compensation
- apt
- case-study
- greeks
- black-scholes-model
- valuation
- executive_compensation
- quantitative-implementation
- solution
- treasury-bonds
- american-options
- option-pricing
- employee-stock-options
- employee_stock_options
- implied-volatility
- monte-carlo
title: Week 4 ESOs and Valuation
---

# Week 4 ESOs and Valuation

## ADVANCED FINANCIAL ANALYSIS AND VALUATION OF GLOBAL FIRMS

## EQUITY COMPENSATION IN HIGH-GROWTH COMPANIES

- ESOs align management interests with shareholders
	- Options protect managers and employees on the downside
	- Counteracts their risk aversion and rewards risk-taking
- Young and high-growth firms are often short on cash
	- ESOs allow cash-poor firms with growth prospects to compete for talent
- As a consequence, ESOs are highly used in high-growth companies

!500

- From a valuation perspective, compensation (or equity-linked securities) are tricky
	- Value of compensation (or securities) depends on the value of the stock that you are trying to estimate – creates circularity

## STOCK-BASED COMPENSATION @ GOOGLE

- 25% of operating income and 8% of total expenses
- Including comp changes operating margin by 6%

!500

## EMPLOYEE STOCK OPTIONS

- Employee stock options, like warrants, conversion options on bonds, etc.
- Key features:
	- Exercise price (strike price)
	- Vesting period
	- Expiration date
	- Exercise restrictions

## ESO VALUATION CHALLENGES

### 1. Dilution Effect
- When options are exercised, new shares are issued
- This dilutes existing shareholders
- Must be incorporated into valuation

### 2. Exercise Behavior
- Employees don't follow optimal exercise strategies
- Early exercise is common
- Forfeiture upon termination

### 3. Accounting Treatment
- Fair value at grant date
- Expensed over vesting period
- No adjustment for subsequent value changes

## ACCOUNTING FOR STOCK-BASED COMPENSATION

### ASC 718 (formerly FAS 123R)
- Fair value measurement at grant date
- Use option pricing models (usually Black-Scholes)
- Expense recognition over vesting period
- Forfeitures estimated or actual

### Key Inputs for Black-Scholes:
1. Stock price at grant date
2. Exercise price
3. Expected term
4. Risk-free rate
5. Expected volatility
6. Expected dividends

## VALUATION APPROACHES

### 1. Treasury Stock Method
Traditional approach for diluted EPS:
- Assumes options exercised at beginning of period
- Proceeds used to buy back shares at average price
- Net dilution = Options outstanding - Shares repurchased

### 2. Option Valuation Method
More accurate for valuation:
- Value options using Black-Scholes or binomial
- Subtract option value from equity value
- Allocate remaining value to common shares

### 3. True Cost Method
Economic perspective:
- Options are non-cash expense
- Add back to earnings for cash flow
- But still real economic cost to shareholders

## PRACTICAL CONSIDERATIONS

### For Analysts:
1. Check option footnotes carefully
2. Consider vesting schedules
3. Analyze historical exercise patterns
4. Assess dilution impact
5. Consider repricing history

### For Valuation:
1. Project future grants
2. Model expected exercises
3. Include in diluted share count
4. Consider tax effects
5. Adjust for forfeitures

## CASE STUDY: TECH COMPANY VALUATION

Example: High-growth SaaS company
- 10 million shares outstanding
- 2 million options outstanding
- Average strike price: $20
- Current stock price: $50
- Average remaining life: 5 years

Dilution calculation:
- Potential shares from exercise: 2 million
- Less: Treasury shares from proceeds: 0.8 million
- Net dilution: 1.2 million shares (12% dilution)

## KEY TAKEAWAYS

[^1]: ESOs create real economic dilution
[^2]: Accounting doesn't capture full economic cost
[^3]: Must model future grants for growth companies
[^4]: Exercise behavior differs from theory
[^5]: Tax effects can be significant
[^6]: Critical for tech company valuation

## SUMMARY

Employee stock options represent a significant component of compensation in high-growth companies. Proper valuation requires understanding both the accounting treatment and the economic impact. The key challenge is modeling realistic exercise behavior and future grant patterns while accounting for the dilutive effect on existing shareholders.

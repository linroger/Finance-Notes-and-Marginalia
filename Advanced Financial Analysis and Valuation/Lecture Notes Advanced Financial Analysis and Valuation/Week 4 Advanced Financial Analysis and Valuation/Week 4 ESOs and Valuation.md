---
academic_level: graduate
aliases:
- Employee Stock Options Valuation
- ESO Analysis
- Stock-Based Compensation
cssclasses:
- academia
enhanced: true
enhancement_date: '2025-11-06'
enhancement_id: batch09-000246
key_concepts:
- Black-Scholes option pricing model and continuous-time finance
- Options Greeks and sensitivity analysis for risk management
- Duration analysis and interest rate risk management
- Convexity adjustments and yield curve sensitivity
- Discounted cash flow (DCF) valuation methodology
- Weighted Average Cost of Capital (WACC) and firm valuation
- Volatility modeling and estimation techniques
- Risk preference theory and utility functions
- Sensitivity analysis and Greeks calculation
- 'Valuation Methods: DCF, Comps, and Precedents'
- Free Cash Flow and Enterprise Value
- Value at Risk and Expected Shortfall
- Vasicek Interest Rate Model and Mean Reversion
- Short Rate Models and Term Structure Dynamics
- Company Valuation and Multiple Analysis
- Credit Risk Management and Default Probability
- Expected Loss and Loss Given Default Models
- Comparable Company Analysis and Trading Multiples
- 'Greeks: Delta, Gamma, Theta, and Vega Hedging'
- Ornstein-Uhlenbeck Process in Finance
- Options Trading Strategies and Risk Management
- Stress Testing and Extreme Value Analysis
- Lattice Methods and Recombining Trees in Derivatives Pricing
- Fama-French Factors and Style Analysis
- Risk Measurement and VaR Backtesting
- Contango, Backwardation, and Roll Yield
- Futures and Forward Contracts in Financial Markets
- Bond Pricing and Yield to Maturity Analysis
- Fixed Income Securities and Credit Quality
- Binomial Option Pricing Model for Discrete Time Valuation
- Hedge Strategies and Basis Risk Management
- American Option Pricing and Early Exercise Premium
- Option Valuation and Exercise Strategies
- Credit Spreads and Rating Migration Analysis
- Factor Models and Asset Pricing
- Government and Corporate Bond Markets
- Terminal Value and WACC Calculations
- Discounted Cash Flow Valuation Models
- Arbitrage Pricing Theory and Multi-Factor Models
linter-yaml-title-alias: Week 4 ESOs and Valuation
professional_application: theoreti
status: active
tags:
- binomial-model
- black-scholes-model
- capital-structure
- caplet
- cash-flow-modeling
- continuous-time-pricing
- convexity-adjustment
- cost-of-capital
- credit-rating
- dcf-valuation
- debit-valuation-adjustment
- delta-hedging
- derivatives
- discounted-cash-flow
- discrete-time-pricing
- leveraged-buyout
- hull-white
- call-options
- cir-model
- terminal-value
- free-cash-flow
- butterfly-spreads
- dcf-analysis
- expected-shortfall
- binomial-tree
- straddles
- extreme-value-theory
- american-options
- book-to-market
- backwardation
- volatility-analysis
- style-analysis
- bond-pricing
- option-strategies
- corporate-bonds
- unexpected-loss
- clearinghouse
- enterprise-value
- arbitrage-pricing-theory
- hedge-ratio
- market-price-of-risk
- loss-given-default
- value-factor
- vasicek-model
- dirty-price
- monte-carlo-var
- capital-budgeting
- options-trading
- coupon-bonds
- forward-contracts
- yield-to-maturity
- fama-french
- price-to-earnings
- recovery-rate
- zero-coupon-bonds
- parametric-var
- lognormal-models
- var-methodologies
- historical-var
- mean-reversion
- contango
- expected-loss
- wacc
- quantitative-finance
- crr-model
- protective-puts
- government-bonds
- probabilty-of-default
- roll-yield
- cost-of-debt
- risk-premium
- put-options
- affine-term-structure
- multi-period-binomial
- momentum
- basis-risk
- covered-calls
- ' exposure-at-default'
- stress-testing
- mathematical-finance
- ornstein-uhlenbeck
- rating-migration
- comparable-analysis
- investment-analysis
- economic-value-added
- value-at-risk
- factor-models
- risk-management
- convergence
- var-backtesting
- sum-of-parts
- clean-price
- lattice-models
- strangles
- conditional-var
- fixed-income
- cox-ross-rubinstein
- short-rate-models
- cost-of-equity
- optional-exercise
- credit-migration
- default-probability
- marking-to-market
- binomial-option-pricing
- credit-spreads
- multi-factor-models
- trading-multiples
- iron-condors
- financial-markets
- equity-value
- size-effect
- precedent-transactions
- ipo-valuation
- market-multiple
- ' recombining-trees'
- futures-contracts
- apt
- current-yield
title: Week 4 ESOs and Valuation
type: course-note
---
--



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

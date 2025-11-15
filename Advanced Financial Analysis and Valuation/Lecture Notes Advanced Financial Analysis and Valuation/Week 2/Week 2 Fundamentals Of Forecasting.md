---
academic_level: graduate
aliases:
- Forecasting Fundamentals
- Behavioral Biases in Forecasting
- Inside vs Outside View
cssclasses:
- academia
enhanced: true
enhancement_date: '2025-11-06'
enhancement_id: batch09-000254
key_concepts:
- Options Greeks and sensitivity analysis for risk management
- Duration analysis and interest rate risk management
- Convexity adjustments and yield curve sensitivity
- Discounted cash flow (DCF) valuation methodology
- Weighted Average Cost of Capital (WACC) and firm valuation
- Value at Risk (VaR) and tail risk measurement
- Expected shortfall and coherent risk measures
- Basel accords and banking regulation framework
- Risk preference theory and utility functions
- 'Valuation Methods: DCF, Comps, and Precedents'
- Value at Risk and Expected Shortfall
- Derivatives Clearing and Volcker Rule
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
- Fama-French Factors and Style Analysis
- Risk Measurement and VaR Backtesting
- Contango, Backwardation, and Roll Yield
- Dodd-Frank Act and Financial Regulatory Reform
- Futures and Forward Contracts in Financial Markets
- Hedge Strategies and Basis Risk Management
- Option Valuation and Exercise Strategies
- Credit Spreads and Rating Migration Analysis
- Systemic Risk and Living Wills
- Factor Models and Asset Pricing
- Arbitrage Pricing Theory and Multi-Factor Models
linter-yaml-title-alias: Week 2 Fundamentals Of Forecasting
professional_application: theoreti
status: active
tags:
- banking-regulation
- basel-accord
- capital-adequacy
- capital-structure
- caplet
- cash-flow-modeling
- coherent-risk-measure
- conditional-var
- convexity-adjustment
- cost-of-capital
- credit-rating
- dcf-valuation
- debit-valuation-adjustment
- delta-hedging
- discounted-cash-flow
- leveraged-buyout
- hull-white
- call-options
- cir-model
- butterfly-spreads
- dcf-analysis
- expected-shortfall
- straddles
- extreme-value-theory
- book-to-market
- backwardation
- volatility-analysis
- style-analysis
- option-strategies
- unexpected-loss
- clearinghouse
- arbitrage-pricing-theory
- hedge-ratio
- systemic-risk
- market-price-of-risk
- loss-given-default
- value-factor
- vasicek-model
- monte-carlo-var
- options-trading
- forward-contracts
- price-to-earnings
- fama-french
- recovery-rate
- parametric-var
- lognormal-models
- var-methodologies
- historical-var
- mean-reversion
- contango
- expected-loss
- protective-puts
- probabilty-of-default
- living-wills
- roll-yield
- risk-premium
- put-options
- affine-term-structure
- momentum
- basis-risk
- regulatory-reform
- covered-calls
- ' exposure-at-default'
- stress-testing
- derivatives-clearing
- ornstein-uhlenbeck
- rating-migration
- comparable-analysis
- investment-analysis
- economic-value-added
- value-at-risk
- volcker-rule
- factor-models
- risk-management
- convergence
- var-backtesting
- sum-of-parts
- dodd-frank-act
- strangles
- short-rate-models
- credit-migration
- default-probability
- marking-to-market
- credit-spreads
- proprietary-trading
- multi-factor-models
- trading-multiples
- iron-condors
- financial-markets
- credit-rating-agencies
- size-effect
- precedent-transactions
- stress-tests
- ipo-valuation
- market-multiple
- futures-contracts
- apt
title: Week 2 Fundamentals Of Forecasting
type: course-note
---
--



# Week 2 Fundamentals Of Forecasting

## FUNDAMENTALS OF FORECASTING

## INSIDE VS. OUTSIDE VIEW

### COMMON BEHAVIORAL BIASES AND MISTAKES

- Humans exhibit a large number of biases in their decision making and forecasting
	- Rely heavily on mental shortcuts
- Forecasting is central to fundamental analysis and valuation
	- Estimating the intrinsic value of a company requires longer-term forecasting
		- Here is where biases matter the most
	- Event-driven strategies forecast near-term EPS or events
		- No fundamental analysis necessary
- Kahneman and Tversky highlighted two biases that are particularly relevant for forecasting:
	1. Representativeness Heuristic
	2. Availability Heuristic

### REPRESENTATIVENESS HEURISTIC

- The representativeness heuristic: assessing the probability of an event based on the degree to which it resembles other events
- People tend to:
	- Overestimate the probability of events that are similar to recent or memorable experiences
	- Underestimate the probability of events that differ from their expectations
- Example: Hot hand in basketball
	- Players who make several shots in a row are not more likely to make the next shot
	- But people believe they are "hot" and will continue succeeding

### AVAILABILITY HEURISTIC  

- The availability heuristic: judging the probability of an event by how easily examples come to mind
- Events that are more vivid, recent, or emotionally charged are easier to recall
- This leads to overestimating their probability
- Example: Fear of flying vs. driving
	- Plane crashes get extensive media coverage
	- Car accidents are more common but less memorable
	- People overestimate the risk of flying relative to driving

### OTHER COMMON BIASES IN FORECASTING

[^1]: **Confirmation Bias**
	- Seeking information that confirms existing beliefs
	- Ignoring or discounting contradictory evidence
	- Particularly dangerous in financial analysis

[^2]: **Anchoring and Adjustment**
	- Over-relying on the first piece of information encountered
	- Insufficient adjustment from initial estimates
	- Common in valuation multiples and target prices

[^3]: **Overconfidence**
	- Overestimating one's ability to predict outcomes
	- Underestimating uncertainty and ranges
	- More pronounced for difficult forecasts

### THE INSIDE VIEW

The inside view:
- Focuses on the specifics of the case at hand
- Considers unique features and circumstances
- Relies on detailed knowledge of the company/situation
- Often leads to overly optimistic forecasts

### THE OUTSIDE VIEW (BASE RATES)

The outside view:
- Looks at similar cases and their outcomes
- Uses statistical base rates
- Considers the reference class
- Generally more accurate for forecasting

### EXAMPLE: NEW PRODUCT LAUNCH FORECAST

**Inside View:**
- "Our product is revolutionary"
- "Our team is exceptional"
- "Our marketing strategy is unique"
- Forecast: 50% market share in 2 years

**Outside View:**
- Historical success rate of new products: 20%
- Average market share after 2 years: 5-10%
- Time to profitability: 3-5 years
- Adjusted forecast: 5-15% market share

### MEAN REVERSION

- Most financial metrics tend to revert to long-term averages
- High growth rates → slower growth
- High margins → industry average margins
- High ROE → cost of capital

### INDUSTRY PROFIT MARGINS

Example: Industry margins tend to converge over time
- Initially high margins attract competition
- Competition drives prices down
- Margins converge to industry average
- Consider competitive dynamics in forecasts

### ANALYST FORECASTS AND BIASES

Common patterns in analyst forecasts:
[^1]: Over-optimism in long-term forecasts
[^2]: Herding behavior
[^3]: Reluctance to deviate from consensus
[^4]: Slow reaction to new information

### BEST PRACTICES FOR FORECASTING

[^1]: **Start with the outside view**
	- What are the base rates?
	- What happened to similar companies?
	- What are industry averages?

[^2]: **Adjust for inside view**
	- What makes this case unique?
	- Are there structural advantages?
	- Is there evidence of sustainability?

[^3]: **Consider multiple scenarios**
	- Best case / Base case / Worst case
	- Assign probabilities
	- Stress test assumptions

[^4]: **Document assumptions**
	- Make them explicit
	- Test sensitivity
	- Update as new information arrives

[^5]: **Learn from errors**
	- Track forecast accuracy
	- Identify systematic biases
	- Calibrate future forecasts

### CONCLUSION

- Good forecasting requires balancing inside and outside views
- Be aware of behavioral biases
- Use base rates as anchors
- Consider mean reversion
- Document and test assumptions
- Learn from forecast errors

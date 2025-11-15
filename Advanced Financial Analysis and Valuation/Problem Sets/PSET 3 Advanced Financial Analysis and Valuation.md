---
academic_level: graduate
aliases:
- BUSN 30313
- PSET 3
- Roger Lin
- Westlake
cssclasses: academia
enhanced: true
enhancement_date: '2025-11-06'
enhancement_id: batch09-000229
key_concepts:
- Duration analysis and interest rate risk management
- Value at Risk (VaR) and tail risk measurement
- Volatility modeling and estimation techniques
- Risk preference theory and utility functions
- Financial modeling and quantitative analysis
- Risk management and portfolio optimization
- Derivatives pricing and hedging strategies
- Market risk measurement and control
- Duration and Convexity in Fixed Income Risk Management
- 'Valuation Methods: DCF, Comps, and Precedents'
- Value at Risk and Expected Shortfall
- Vasicek Interest Rate Model and Mean Reversion
- Short Rate Models and Term Structure Dynamics
- Company Valuation and Multiple Analysis
- Credit Risk Management and Default Probability
- Expected Loss and Loss Given Default Models
- Comparable Company Analysis and Trading Multiples
- 'Greeks: Delta, Gamma, Theta, and Vega Hedging'
- Ornstein-Uhlenbeck Process in Finance
- Flexibility Value in Capital Budgeting
- Forward Curves and Roll Strategies
- Options Trading Strategies and Risk Management
- Stress Testing and Extreme Value Analysis
- Fama-French Factors and Style Analysis
- Risk Measurement and VaR Backtesting
- Contango, Backwardation, and Roll Yield
- Futures and Forward Contracts in Financial Markets
- Hedge Strategies and Basis Risk Management
- Bond Portfolio Immunization Strategies
- Option to Expand and Investment Timing
- Seasonality and Convenience Yield
- Commodity Markets and Energy Derivatives
- Option Valuation and Exercise Strategies
- Real Options in Strategic Investment Decisions
- Credit Spreads and Rating Migration Analysis
- Interest Rate Risk and DV01 Calculations
- Factor Models and Asset Pricing
- Arbitrage Pricing Theory and Multi-Factor Models
professional_application: theoreti
status: active
tags:
- asset-allocation
- caplet
- commodity-derivatives
- commodity-futures
- credit-rating
- debit-valuation-adjustment
- duration-analysis
- fixed-income-sensitivity
- forward-contracts
- forward-pricing
- funding-costs
- futures
- hedging
- interest-rate-cap
- interest-rate-ceiling
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
- option-to-abandon
- volatility-analysis
- energy-derivatives
- style-analysis
- option-strategies
- timing-options
- unexpected-loss
- clearinghouse
- interest-rate-risk
- arbitrage-pricing-theory
- hedge-ratio
- market-price-of-risk
- loss-given-default
- roll-strategies
- value-factor
- vasicek-model
- forward-curves
- monte-carlo-var
- options-trading
- commodity-trading
- price-to-earnings
- fama-french
- recovery-rate
- real-options
- strategic-investment
- parametric-var
- lognormal-models
- var-methodologies
- historical-var
- mean-reversion
- contango
- modified-duration
- expected-loss
- quantitative-finance
- protective-puts
- probabilty-of-default
- curve-steepening
- storage-costs
- roll-yield
- risk-premium
- put-options
- affine-term-structure
- momentum
- curve-flattening
- option-to-expand
- basis-risk
- convexity
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
- flexibility-value
- metals-trading
- factor-models
- convenience-yield
- agricultural-commodities
- barbell-strategy
- risk-management
- convergence
- var-backtesting
- sum-of-parts
- seasonality
- strangles
- conditional-var
- dv01
- short-rate-models
- price-yield-relationship
- credit-migration
- default-probability
- marking-to-market
- credit-spreads
- multi-factor-models
- trading-multiples
- iron-condors
- financial-markets
- macaulay-duration
- size-effect
- precedent-transactions
- ipo-valuation
- market-multiple
- futures-contracts
- apt
- natural-resource-valuation
type: note
---
--



# PSET 3 - Advanced Financial Analysis and Valuation

Week 3 Cyclical Industries (and Advanced Forecasting)

HBS Westlake Case
PSET 3 - Advanced Financial Analysis and Valuation
Roger Lin
BUSN 30313

[^1]: Think about Westlake's operations. How does Westlake generate value? How do commodity prices and their volatility affect Westlake? What are the key risks for their business? Provide brief (but precise) answers to these questions.
[^1]: Westlake generates value primarily as a vertically integrated producer of commodity petrochemicals, specifically in the olefins and vinyls chains. Its olefins business belongs to the commodity segment, characterized by low value added, and per unit selling price, and high cyclicality and competition, but flexible prices. (Exhibit 2) In the olefins segment, which accounted for 62% of 2003 sales (Exhibit 5A), Westlake uses natural gas-derived feedstocks (ethane) to produce ethylene. Ethylene is then used to produce polyethylene and styrene. Westlake has 2,800mm lbs of annual ethylene capacity and 1,400mm lbs of polyethylene capacity (Exhibit 9A), making it the 8th largest producer in North America with a 4% share of industry capacity (Exhibit 7A). This part of the business relies on high turnover to create profits, since the profit margins per item is low due to competition. In the vinyls segment (38% of 2003 sales), Westlake produces PVC and VCM, which also use ethylene as a key input. Westlake has 900mm lbs of PVC capacity and 450mm lbs of VCM capacity (Exhibit 9A), making it the 5th largest PVC producer in North America with a 4% market share (Exhibit 8A). Westlake also converts some of its PVC into downstream fabricated products like pipes and fittings. The vinyls business belongs under the specialty segment, characterized by high value added and per unit selling price, moderate cyclicality, and lower competition but fixed prices.
[^2]: Westlake uses natural gas as a key input in its production process, meaning that it is exposed to fluctuations in natural gas prices. As shown in Exhibit 1A, natural gas prices have historically been very volatile, with spikes as high as $9/MMBtu in 2000 and 2003. Unlike other petrochemical firms, Westlake relies solely on natural gas as its feedstock to produce ethylene, both a final product under the olefins category, and an intermediate product used to produce vinyls. Other firms had plants which could use either natural gas or naptha, giving them more flexibility in their input source and providing a degree of protection against commodity shocks. This dependency on a single input for its entire production (since natural gas is used as the primary input in the production of both olefins and vinyls) is Westlake's key source of risk, since if commodity prices increase, Westlake will see reduced profit margins. Interest rate risk also affects Westlake, since demand for PVC and VCM in construction is subject to interest rate fluctuations through their effect on construction. Moreover, there is a higher degree of operating leverage in this sector, since there are large and inflexible fixed costs associated with the plants.
[^3]: The tendency for the petrochemical sector to create excess supply following periods of supply shortages is also a significant risk, as it drives down prices on the finished good without impacting the cost of inputs, thus shrinking profit margins.

[^2]: How does the cycle affect Westlake? Would you say the current case environment (October 2004) is good or bad for Westlake's future performance?
[^1]: The commodities industry is highly cyclical, following a boom and bust pattern. Periods of high operating rates (95%+) enable peak margins, but are followed by periods of oversupply and depressed margins. Westlake has limited pricing power to offset this cyclicality. PVC demand is also sensitive to interest rates and construction activity (Exhibit 1C).
[^2]: The current cycle is characterized by slightly elevated natural gas prices and low interest rates, which is on positive on balance. Revenue across both olefins and vinyls have been increasing over the past few years, though ethylene revenues fell to $99m in 2002 before recovering to 205 the following year. Gross margins have followed a generally upward trajectory from -$30m in 2001 to $122m by the end of 2003. The gross profits for the first half of 2004 have already exceeded the gross profits from the whole of 2003. This bodes well for Westlake's future growth.

[^3]: One way to quantitatively assess the impact of the cycle and the current environment on Westlake's future performance is to forecast its earnings per share at the peak of the cycle (so-called "peak EPS"). This metric is used by analysts when valuing commodity firms via a multiple. This forecast could also be used to gauge the influence of the cycle. Using the information in the case (in particular, Exhibits 3 and 7-9) forecast Westlake's EPS at the peak year of the cycle. Use financial data from 2003 as your starting point, but feel free to make adjustments.

Hints: Note how "estimated peak margin (after tax)" is connected to the historical peak margin. The margins given in Exhibit 9, Panel C, are essentially gross margins, i.e., revenues minus input costs, but stated in cents per pound and after taxes to aid your analysis.

Starting with the 2003 financial data (Exhibit 3B), Westlake's diluted EPS was $0.30.
For olefins:

+ Ethylene peak after-tax margin is estimated at 16.0 cents/lb (Exhibit 9C), which is 7.4 cents/lb higher than the 8.6 cent/lb margin realized in 2003. Multiplying the 7.4 cent/lb increase by Westlake's ethylene capacity of 2,800mm lbs (Exhibit 9A) results in an incremental gross profit of $207.2mm. Assuming a 34% tax rate (Exhibit 9B), this equates to $136.8mm of additional net income. Dividing by Westlake's diluted shares outstanding of 49.5mm (Exhibit 3B) results in incremental EPS of $2.76
For vinyls:
+ PVC peak after-tax margin is estimated at 12.8 cents/lb (Exhibit 9C), which is 9.7 cents/lb above the 3.1 cent/lb margin in 2003. Multiplying the 9.7 cent/lb increase by Westlake's PVC capacity of 900mm lbs (Exhibit 9A) results in $87.3mm of incremental gross profit. After applying a 34% tax rate, we get $57.6mm of incremental net income. Dividing by 49.5mm diluted shares equals incremental EPS of $1.16

To arrive at the peak cycle EPS estimate, we add the incremental EPS figures from olefins ($2.76) and vinyls ($1.16) to the base 2003 EPS of $0.30:
$0.30 + $2.76 + $1.16 = $4.22 EPS

[^4]: Would you use this forecast of peak EPS in a forward PE multiple? Please explain why or why not, and mention any implications for the multiple.
   + I would not use this forecast of peak EPS in a forward PE multiple since it may not be representative of Westlake's future earnings potential, especially if commodity prices rise in the future, shrinking the company's profit margins and hurting their earnings. Given the cyclical nature of the industry, it would not be unreasonable to assume that the peak is only temporary, and that changes in the macro environment would follow shortly after. Indeed, given the habit of the industry to create excess supply after a shortage, we can expect Westlake's EPS to change over time. Moreover, there may be uncertainty in how we measure peak EPS, especially if the commodity cycle does not exactly line up with the financial reporting timelines. Thus, we may not accurately measure the duration of the peak. The EPS will moreover fluctuate depending on whether it is currently a peak or a trough, since during peak years, we expect to see a higher earnings per share ratio and lower PE ratio during peaks, and lower EPS ratio and higher PE ratio during troughs due to the change in earnings over a cyclical cycle.

 | Westlake Chemical Corporation - Peak Cycle EPS Estimate |
 | ------------------------------------------------------- | ------ | 
 | Olefins Segment |
 | Ethylene Peak Margin (cents/lb) | 16.0 | 
 | (-) 2003 Ethylene Margin (cents/lb) | 8.6 | 
 | Incremental Margin (cents/lb) | 7.4 | 
 | Ethylene Capacity (mm lbs) | 2,800 | 
 | Incremental Gross Profit ($mm) | $207.2 | 
 | Tax Rate | 34% | 
 | Incremental Net Income ($mm) | $136.8 | 
 | Diluted Shares Outstanding (mm) | 49.5 | 
 | Incremental EPS | $2.76 | 
|  | 
 | Vinyls Segment |
 | PVC Peak Margin (cents/lb) | 12.8 | 
 | (-) 2003 PVC Margin (cents/lb) | 3.1 | 
 | Incremental Margin (cents/lb) | 9.7 | 
 | PVC Capacity (mm lbs) | 900 | 
 | Incremental Gross Profit ($mm) | $87.3 | 
 | Tax Rate | 34% | 
 | Incremental Net Income ($mm) | $57.6 | 
 | Diluted Shares Outstanding (mm) | 49.5 | 
 | Incremental EPS | $1.16 | 
|  | 
 | Peak Cycle EPS Estimate |
 | 2003 Diluted EPS | $0.30 | 
 | (+) Olefins Incremental EPS | $2.76 | 
 | (+) Vinyls Incremental EPS | $1.16 | 
 | Peak Cycle EPS Estimate | $4.22 |

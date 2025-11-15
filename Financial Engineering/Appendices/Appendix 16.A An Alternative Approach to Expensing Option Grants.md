---
aliases:
- Bulow-Shoven Approach
- Expensing Option Grants
cssclasses: academia
enhanced: true
enhancement_date: '2025-11-06'
enhancement_id: batch03-6b4019
key_concepts:
- Cox-Ross-Rubinstein parameter specification
- Carry trades and momentum in FX markets
- Sovereign risk assessment and country analysis
- Mean-variance optimization and the efficient frontier
- Extreme value theory and tail risk modeling
- Computational implementation of binomial option pricing
- Credit risk modeling and default probability estimation
- Option Greeks and portfolio risk management
- Risk budgeting and portfolio construction techniques
- Accounting for compensation options
- Historical simulation vs. parametric VaR models
- Binomial option example
- Vega and volatility risk management
- DV01 calculation and interest rate risk hedging
- Swap spread and credit risk considerations
- Mathematical Finance
- Monte Carlo integration and variance reduction
- GARCH models and volatility forecasting
- Deposit insurance and systemic risk prevention
- Monte Carlo VaR for complex portfolios
- Stress testing and scenario analysis
- Fixed-for-floating swap cash flows and valuation
- Course Material
- Currency risk management and hedging
- Forward rates and interest rate parity
- Control variates and importance sampling techniques
- Theta and time decay modeling
- Risk-neutral pricing methodology for derivative securities
- Value at Risk (VaR) methodologies and backtesting
- Case Study
- Operational risk quantification and modeling
- Exchange rate determination and PPP theory
- Long-term option cost
- Option expense calculation
- Arbitrage opportunities and risk-free profit extraction
- Expected Shortfall and coherent risk measures
- Interest rate swap pricing and valuation
- present value and discounting methods
- Bank liquidity ratios and funding risk management
- Variance swaps and volatility trading strategies
- Convergence of binomial model to Black-Scholes solution
- Binomial option pricing model with multiple time steps
- Value-at-Risk calculation using historical simulation
- American option pricing in binomial trees
- Gamma and convexity adjustments
- Credit risk migration matrices and rating transition
- Credit risk modeling and portfolio correlation analysis
- Backtesting procedures for risk models
- Credit risk assessment and loan portfolio management
- Delta hedging and the replication argument
- Liquidity risk measurement and management
- Cross-currency basis swaps and funding
- Systemic risk indicators and early warning systems
- Deduct market value at exercise
- Global financial stability and systemic risk monitoring
- Currency markets and foreign exchange trading
tags:
- financial-analysis
- binomial-model
- income-statement
- garch-models
- interest-rate-swaps
- mathematical-finance
- course-material
- financial-modeling
- bulow-and-shoven
- case-study
- amortization
- greeks
- binomial-example
- value-at-risk
- compensation-options
- exchange-rates
- credit-risk
- quantitative-implementation
- duration-convexity
- solution
- american-options
- stress-testing
- option-grants
- liquidity-risk
- systemic-risk
- option-valuation
- deposit-insurance
- quantitative-finance
- dcf-valuation
- expected-shortfall
- operational-risk
- monte-carlo
title: Appendix 16.A An Alternative Approach to Expensing Option Grants
---

# Appendix 16.A An Alternative Approach to Expensing Option Grants

How should companies account for compensation options? One approach is to fully deduct the market value of the option at exercise; this is the approach taken in taxing option grants: A deduction at exercise gives an expense with a present value equal to the price at grant. However, by waiting to deduct the expense, the firm's reported income in earlier years will not reflect the economic value of compensation in those years.

As an alternative, Bulow and Shoven (2004) propose an option expense calculation that records an expense for each period that the option remains unexercised. Their approach neatly sidesteps many valuation difficulties and provides a correct present value of option deductions. Moreover, the method provides insight into why a long-term option grant is costly. We will illustrate the proposal in the specific context of compensation options, but the methodology is generally applicable to long-term contracts and contingent liabilities.

Bulow and Shoven make the observation that most option contracts are exercisable after a vesting period, and that employees or heirs are typically required to exercise their options within 90 days of resignation or death. Thus, in practice, a 10-year option can be viewed as a renewable 90-day option, extendible (by the employee's continuing to work) for 39 additional 90-day periods. Bulow and Shoven propose taking the value of this extension as the deduction in each quarter. The value of the extension is the market value of a 90-day option, less intrinsic value. The present value of expected option expense computed in this fashion is the fair market value for an option with the same time to expiration.

Figure 16.10 provides a binomial example illustrating how the Bulow-Shoven proposal works for a 3-year option that vests immediately, and for which recipients can exercise the option in year 1, 2, or 3, or 1 year after resignation. The binomial value of the 3-year 100-strike option is $28.15; you can verify this by applying the binomial pricing method to the stock price tree in panel (a).

Panel (d) of Figure 16.10 shows the annual expense reported under the Bulow-Shoven scheme. To see how the entries in panel (d) are calculated, consider the $4.88 expense in year 1 when the stock price is $134.99. From panel (c), the price of a 1-year option at that node is $39.86. Option expense in that year is therefore fair market value less intrinsic value, or $39.86 − 34.99 = $4.88. Why do we deduct intrinsic value? The reason is that the deduction for the year 2 intrinsic value was, in effect, already taken the previous year, when we deducted the value of a 1-year option. The price of a 1-year option is the present value of the next year's intrinsic value. Therefore, the only new value to deduct in a given year is the value of a 1-year option over and above that year's intrinsic value, which is the present value of *next* year's intrinsic value. In effect, the Bulow-Shoven scheme amortizes the value of the 3-year option, where the amortization amount varies with the stock price.

You can compute the present value of all deductions in panel (d) by using the binomial pricing method with the same parameters used to generate panel (a). As an exercise, you can verify that the present value of deductions in panel (d) is $28.15, which is also the binomial value of a 3-year option.[[^1]]

FIGURE 16.10

Option expense calculation under the Bulow-Shoven proposal. Assumes $K = \$100$, $\sigma = 0.30$, $r = 0.05$, $\delta = 0$, and $T = 3$ years. The risk-neutral probability of an up move is $p = 0.5097$. The CRR binomial stock price process is in panel (a). Panel (b) reports the option intrinsic value, $\max[0, S_t - K]$. Panel (c) reports the 1-period option value. Panel (d) reports the annual option expense.

!500  

There are several points to make about this example. First, the full deductions with a present value of $28.15 are reported by the company only if the option is held unexercised until year 3. Thus, the proposal solves the problem of early exercise and the employee leaving the company. Second, the actual deductions are substantially less than the maximum possible value of the option at exercise. Third, expenses behave in what might appear to be a counterintuitive fashion, with reported option expense greatest when the option is at-the-money. In year 2, for example, expense is greatest when the stock price is $100. The reason is that the value of delaying exercise on a deep-in-the-money option is primarily the value of delaying the payment of the strike price. Thus, in panel (d), $4.88 is the 1-year present value of interest on $100. When the option is at-the-money, however, put-call parity tells us that the value of the implicit put option is also important, and this is why the at-the-money expense is greater. To say this differently, an employee who prematurely exercises an option that is near the money loses more economic value than an employee who prematurely exercises an option that is deep in the money. The option expense calculation in Figure 16.10 reflects this.

Suppose a firm must compute annual option expense and separated employees have 2 years to exercise their options. How does this change the calculation? In this case, by working 1 more year, the employee obtains a new 1-year option and gives up the remaining 1 year on the previous year's 2-year option. It is straightforward to calculate expense in this situation. Using the assumptions in Figure 16.10, Problem 16.24 asks you to verify that the present value of option expense in this case again equals the fair market value of $28.15.

Note that if we were to apply this methodology to a grant of stock, we would expense the entire grant initially. A share of stock is like a zero-exercise price option, and with no dividends, such an option is worth the share price. Price would therefore equal intrinsic value in every period, resulting in zero expense every period after the first.

Finally, note that this expensing method is generally applicable to contingent liabilities, and it thus has broad applicability beyond compensation options. In general, in order to record a current expense, it is necessary to value the liability only over a short horizon, and then to do so repeatedly.

## References

Bulow, J. and Shoven, J. B. 2004, "Accounting for Options," Working Paper, Stanford University, March 2004.

[[^1]]: Consider the analogy with wages. An employee may have a long-term employment contract specifying wages for 10 years, but the firm on the income statement only deducts wages paid each quarter. The goal of the Bulow-Shoven proposal is to afford similar treatment to options.

---
academic_level: graduate
aliases:
- Homework 6
- PLUS Security
- PSET 6
cssclasses:
- academia
enhanced: true
enhancement_date: '2025-11-06'
enhancement_id: batch09-000123
key_concepts:
- Black-Scholes option pricing model and continuous-time finance
- Implied volatility calculation and volatility surface analysis
- Options Greeks and sensitivity analysis for risk management
- Duration analysis and interest rate risk management
- Convexity adjustments and yield curve sensitivity
- Discounted cash flow (DCF) valuation methodology
- Capital Asset Pricing Model (CAPM) and expected returns
- Weighted Average Cost of Capital (WACC) and firm valuation
- Credit default swaps (CDS) and credit risk modeling
- Value at Risk (VaR) and tail risk measurement
- Collateralized debt obligations (CDO) and tranche structure
- Arbitrage opportunities and no-arbitrage pricing
- Beta estimation and systematic risk measurement
- Factor models and multi-factor pricing
- Volatility modeling and estimation techniques
- Beta estimation and systematic risk measurement
- Risk preference theory and utility functions
- Sensitivity analysis and Greeks calculation
- 'Valuation Methods: DCF, Comps, and Precedents'
- Auto-Callable Notes and Barrier Options
- Value at Risk and Expected Shortfall
- Vasicek Interest Rate Model and Mean Reversion
- Short Rate Models and Term Structure Dynamics
- Company Valuation and Multiple Analysis
- Capital Asset Pricing Model and Beta Analysis
- Credit Risk Management and Default Probability
- Expected Loss and Loss Given Default Models
- Equity-Linked Notes and Market-Linked Securities
- Comparable Company Analysis and Trading Multiples
- 'Greeks: Delta, Gamma, Theta, and Vega Hedging'
- Ornstein-Uhlenbeck Process in Finance
- Cost of Equity and Expected Returns
- Security Market Line and Risk-Return Tradeoff
- Options Trading Strategies and Risk Management
- Structured Products and Principal Protection
- Stress Testing and Extreme Value Analysis
- Fama-French Factors and Style Analysis
- Risk Measurement and VaR Backtesting
- Fixed Income Securities and Credit Quality
- Bond Pricing and Yield to Maturity Analysis
- Private Equity Investment Returns and Value Creation
- Option Valuation and Exercise Strategies
- Credit Spreads and Rating Migration Analysis
- LBO Valuation and Debt Capacity Analysis
- Factor Models and Asset Pricing
- Leveraged Buyouts and Private Equity Transactions
- Government and Corporate Bond Markets
- Arbitrage Pricing Theory and Multi-Factor Models
linter-yaml-title-alias: PSET 6-Financial Instruments
professional_application: theoreti
status: active
tags:
- arbitrage-opportunity
- arbitrage-pricing
- asset-allocation
- beta-estimation
- binomial-model
- black-scholes-model
- capital-asset-pricing
- capital-structure
- caplet
- cash-flow-modeling
- cds
- collateralized-debt-obligation
- continuous-time-pricing
- convexity-adjustment
- cost-of-capital
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
- volatility-analysis
- style-analysis
- leverage-ratio
- bond-pricing
- option-strategies
- corporate-bonds
- unexpected-loss
- capital-asset-pricing-model
- arbitrage-pricing-theory
- private-equity
- market-price-of-risk
- loss-given-default
- value-factor
- vasicek-model
- sharpe-ratio
- dirty-price
- monte-carlo-var
- options-trading
- coupon-bonds
- yield-to-maturity
- price-to-earnings
- fama-french
- recovery-rate
- zero-coupon-bonds
- parametric-var
- lognormal-models
- var-methodologies
- historical-var
- mean-reversion
- debt-capacity
- expected-loss
- market-linked-notes
- investment-return
- systematic-risk
- protective-puts
- government-bonds
- alpha
- security-market-line
- probabilty-of-default
- reverse-convertibles
- idiosyncratic-risk
- risk-premium
- beta
- put-options
- affine-term-structure
- equity-kickers
- capm
- lbo-valuation
- momentum
- market-risk-premium
- covered-calls
- ' exposure-at-default'
- stress-testing
- ornstein-uhlenbeck
- rating-migration
- comparable-analysis
- investment-analysis
- economic-value-added
- portfolio-optimization
- value-at-risk
- bootstrap-strategy
- management-buyout
- factor-models
- risk-management
- var-backtesting
- barrier-options
- sum-of-parts
- clean-price
- principal-protected-notes
- strangles
- conditional-var
- equity-linked-notes
- fixed-income
- short-rate-models
- efficient-frontier
- credit-migration
- default-probability
- auto-callables
- credit-spreads
- multi-factor-models
- trading-multiples
- structured-notes
- iron-condors
- financial-markets
- size-effect
- precedent-transactions
- knock-out-options
- ipo-valuation
- market-multiple
- apt
- current-yield
title: PSET 6-Financial Instruments
type: case-study
---
--



# PSET 6-Financial Instruments

## FINANCIAL INSTRUMENTS WINTER 2024 JOHN HEATON

Homework 6

Due at the beginning of class 8

Roger Lin

Suna Bai

## 1 IMPLIED VOLATILITY

Replicate the Implied Volatility of Teaching Note 6, using current options data on S&P 500 maturing in June (3 months or one quarter from now). Please state the assumptions you make, if any, to compute the time to maturity of the options, that is the value of T that you use in your formulas. (No need to use many options. Choose just a few ITM, OTM and ATM. Note that the current SP 500 index value is on the top right corner of the table.) The spreadsheet "Options.Xls" provides an example of the implied volatility calculation. See the worksheet "Implied Volatility."

ˆ Current Options Data can be found at CBOE. The ticker is SPX.

http://www.cboe.com/DelayedQuote/QuoteTable.aspx

NOTE: I have downloaded all of this data for you! Please see the file "Quote-Data 2024.Xls."

ˆ You can use federal reserve website (link below) to retrieve the value of the risk Free rate. Use the Treasury Constant Maturity rate that most closely matches the Maturity of the options. Note that TCM are compounded annually, so be sure to Make the relevant adjustments. Please report the value of the rate that you use. 
http://www.federalreserve.gov/releases/h15/Current/

ˆ The dividend yield can be estimated using the data collected by Robert Shiller which are available at the link below. You can estimate the dividend yield as the average dividend yield over the last available 12 months. Be sure to make the relevant compounding adjustments and report the dividend yield that you use.

http://www.econ.yale.edu/~shiller/data.htm 
You should use the data in the "Excel file" used in his book. This gives monthly prices, dividends, earnings and other information.

> [!NOTE]
> Risk free rate: Interest rate on 3 month Treasury constant maturities as of 12 February, 2024 = 5.43%, annually compounded
> - We chose this Treasury because its maturity closely matches the maturity of the options expiring on June 21 and June 28, 2024.
> - The risk-free rate, continuously compounded, is
> - $r = \ln(1.0543) = 0.05288$
> 
> Average monthly dividend yield on SP 500 from Feb 28, 2023 to Jan 31, 2024 is 1.621075%
> - The continuously compounded dividend yield = 1.608%

![](03bc29ba4ac59fbc321f2f432023249d.png)

 | Assumptions |
 | ------------- | ------------ | 
 | Start Date | Feb 12th, 2024 | 
 | Maturity Date | June 21st, 2024 | 
 | Days to Expiration | 130 | 
 | Risk Free Rate | 5.29% (3 Month Treasury Rate as of Feb 12th, 2024) | 
 | Dividend Yield | 1.608% (average dividend yield on SPX over 2023) | 
 | Strike Price | $5,020 | 
 | Price of Underlying | $5,021.84 | 
 | ITM Call Premium | $190.75 | 
 | IV on ITM Call Option | 16.18% | 
 | ITM Put Premium | $120.50 | 
 | IV on ITM Put Option | 10.35% | 

![](ea19896c234fab61d22703aa002e42dc.png)

## 2 VALUING AND ANALYZING A STRUCTURED SECURITY

- (1) A wealthy investor hires you to help her evaluate a recent security issued by Morgan Stanley, called PLUS (see prospectus: The security was issued by Morgan Stanley in April 2008. Assume the same security is issued today and has one-year to Maturity, but it is otherwise identical). To assess its fair value, you decide to use the appropriate implied volatility from the options markets as in Exercise (1).
  - (a) How can you decompose the PLUS into more basic securities? (Tip: The Solution to the Mock Midterm might be helpful…)

 | Start Date | Feb 12th, 2024 | 
 | ------------ | ---------------- | 
 | Maturity Date | Feb 12th, 2025 | 
 | T | 1 | 
 | Risk Free Rate | 4.87% (1 year constant maturity Treasury Rate as of Feb 12th, 2024) | 
 | Dividend Yield | 1.608% (average dividend yield on SPX over 2023) | 
 | Implied Volatility | 16.18% | 

 | Stock Index Price | B0 | normalized index price | 
 | ------------------- | ---- | ----------------------- | 
 | 1329.51 | 0.00752 | 9.997915 | 
 | 1417 | 0.00752 | 10.65584 | 

> [!NOTE]
> - We can decompose the PLUS security into:
>   - A zero coupon bond with face value of $10
>     - $B_Z = 10 \cdot e^{-0.0487 \cdot 1}$
>   - 3 Long At the Money Call Options with Strike Price of $10
>   - 3 Short Out of the Money Call Options with Strike of $10.65584
>   - 1 Short At the Money Put Option with Strike Price of $10

- (b) Use the decomposition obtained in point (2.1.A) and the information obtained in exercise (1) to value the PLUS.

> [!NOTE]
> - A zero coupon bond with face value of $10:
>   - $B_Z = 10 \cdot e^{-0.0487 \cdot 1} = 9.52467$
> - 3 Long At the Money Call Options with Strike Price of $10$:
>   - $\text{BSCall}(S, K, \sigma, r, T, \delta)$
>   - $3 \times \text{BSCall}(10, 10, 16.18\%, 4.87\%, 1, 1.60\%) \approx 0.8 \times 3 = 2.4$
> - 3 Short Out of the Money Call Options with Strike of $10.65584$:
>   - $3 \times \text{BSCall}(10, 10.65584, 16.18\%, 4.87\%, 1, 1.608\%) \approx -0.17975 \times 3 = -0.539251$
> - 1 Short At the Money Put Option with Strike Price of $10$:
>   - $\text{BSPut}(10, 10, 16.18\%, 4.87\%, 1, 1.60\%) = -0.48$
> - Total Value of Replicating Portfolio = $9.52467 + 2.4 - 0.539 - 0.48 = 10.899032$

![](6c4e3667220d343e13994175049a7193.jpg)

![](c07b3c05093e1981d064faaca657d2eb.png)

- (c) If the value you obtain is not at par, what might you modify to make sure the value of the security is par as of today? (Words only, but for a bonus, see if you can actually set the value to par by changing one of the terms.)

> [!NOTE]
> I would change the cap on the maximum return, since this would affect the out of the money call option's value. We cannot change the risk free rate, volatility, dividend yield, or stock price, so our best option is to change the strike price on the out of the money call option which forms the cap of the maximum returns we can earn.

- (2) What is the sensitivity of this security to changes in the underlying stock price? How can you compute its market "beta", namely, the **percentage** sensitivity of the security to **percentage** changes in the underlying? Compute the "beta" of the PLUS for several stock prices "S" as of
  - Option elasticity is computed by the percentage change in the option price relative to the percentage change in the stock price. The percentage change in the stock price is change in stock price, dS divided by $S$. The percentage change in the options price is given by the dollar change in the price of the option, divided by the option price, $C$, or $\frac{dS \cdot \Delta}{C}$. The option elasticity is then the percentage change in option price over the percentage change in stock price, which simplifies to $\frac{S \cdot \Delta}{C}$
  - (a) Now
  - (b) 6 months from now
  - ![](a8921e8205d813706483563730cd7f9b.png)
  - (c) 1 year from now. Discuss your findings.
    - As the PLUS note approaches maturity, the beta increases, meaning that it becomes more sensitive to changes in the price of the underlying stock

![](aa4d12a40d58406aa012877a83a05b9a.png)

|  |  |
 | --- | --- | --- | --- | 
 | Maturity | 1/365 | 6 months | 1 year | 
 | Value of zero coupon bond | 9.99864731 | 9.7594407 | 9.52466827 | 
 | ATM Call(K0=10) | 0.03447201 | 0.53365626 | 0.79484313 | 
 | N(d1) | 0.5059398 | 0.57916686 | 0.61122258 | 
 | N(d2) | 0.50253798 | 0.5340095 | 0.54803841 | 
|  |  |
 | OTM Call (K1=11.9) | -4.831E-95 | -0.0472135 | -0.1797505 | 
 | N(d1) | 1.1608E-92 | 0.09330454 | 0.21400364 | 
 | N(d2) | 9.7511E-93 | 0.07563117 | 0.16993903 | 
|  |  |
 | ATM Put(K0=10) | -0.0335647 | -0.3702476 | -0.4709137 | 
 | N(d1) | 0.49746202 | 0.4659905 | 0.45196159 | 
 | N(d2) | 0.49746202 | 0.4659905 | 0.45196159 | 
|  |  |
 | dV/dS | 0.01519207 | 0.0147959 | 0.01272506 | 
 | β | 2.00605971 | 1.81327046 | 1.55225645 | 

## STRUCTURED INVESTMENTS OPPORTUNITIES IN EQUITIES PLUS BASED ON THE VALUE OF THE S&P 500® INDEX DUE APRIL 20, 2009 PERFORMANCE LEVERAGED UPSIDE SECURITIES

The PLUS are senior unsecured obligations of Morgan Stanley, will pay no interest, do not guarantee any return of principal at maturity and have the terms described in the prospectus supplement for PLUS and the prospectus, as supplemented or modified by this pricing supplement.

 | Term | Details | 
 | ---- | ---- | 
 | Issuer | Morgan Stanley | 
 | Maturity date | April 20, 2009 | 
 | Underlying index | S&P 500® Index | 
 | Aggregate principal amount | $47,500,000 | 
 | Payment at maturity | If final index value is greater than initial index value, $10 + leveraged upside payment. In no event will the payment at maturity exceed the maximum payment at maturity. If final index value is less than or equal to initial index value, $10 × (final index value / initial index value). This amount will be less than or equal to the stated principal amount of $10. | 
 | Leveraged upside payment | $10 × leverage factor × index percent increase | 
 | Index percent increase | (final index value – initial index value) / initial index value | 
 | Initial index value | 1,329.51, the index closing value of the underlying index on the pricing date | 
 | Final index value | The index closing value of the underlying index on the valuation date | 
 | Valuation date | April 16, 2009, subject to adjustment for certain market disruption events | 
 | Leverage factor | 300% | 
 | Maximum payment at maturity | $11.90 (119% of the stated principal amount) per PLUS | 
 | Stated principal amount | $10 per PLUS | 
 | Issue price | $10 per PLUS (see "Commissions and Issue Price" below) | 
 | Pricing date | March 20, 2008 | 
 | Original issue date | March 31, 2008 | 
 | CUSIP | 61747W166 | 
 | Listing | The PLUS have been approved for listing on the American Stock Exchange LLC under the ticker symbol "SKE," subject to official notice of issuance. It is not possible to predict whether any secondary market for the PLUS will develop. | 
 | Agent | Morgan Stanley & Co. Incorporated | 

 | Commissions and Issue Price: | Price to Public | Agent's Commissions | Proceeds to Company | 
 | ------------------------------ | ----------------- | --------------------- | --------------------- | 
 | Per PLUS | $10.00 | $0.15 | $9.85 | 
 | Total | $47,500,000 | $712,500 | $46,787,500 | 

(1) The actual price to public and agent's commissions for a particular investor may be reduced for volume purchase discounts depending on the aggregate amount of PLUS purchased by that investor. The lowest price payable by an investor is $9.95 per PLUS. Please see "Syndicate Information" on page 4 for further details.

(2) For additional information, see "Plan of Distribution" in the accompanying prospectus supplement for PLUS.

The PLUS involve risks not associated with an investment in ordinary debt securities. See "Risk Factors" beginning on page 7.

The Securities and Exchange Commission and state securities regulators have not approved or disapproved these securities, or determined if this pricing supplement or the accompanying prospectus supplement and prospectus is truthful or complete. Any representation to the contrary is a criminal offense.

YOU SHOULD READ THIS DOCUMENT TOGETHER WITH THE RELATED PROSPECTUS SUPPLEMENT AND PROSPECTUS, EACH OF WHICH CAN BE ACCESSED VIA THE HYPERLINKS BELOW.

Amendment No. 2 to Prospectus Supplement for PLUS dated October 24, 2007

Prospectus dated January 25, 2006

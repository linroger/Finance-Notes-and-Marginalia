---
aliases:
- Freddie Mac Bond
- HW6
- Homework 6
- PSET VI
enhanced: true
enhancement_date: '2025-11-06'
enhancement_id: batch09-000512
key_concepts:
- Option pricing theory and Black-Scholes model
- Options Greeks and risk management
- Call and put option strategies
- Bond pricing and yield curves
- Duration and convexity hedging
- Credit spreads and bond valuation
- Fixed income securities and markets
- Bond valuation and yield calculation
- Credit analysis and spread decomposition
- Interest rate theory and modeling
- Monetary policy and rate setting
- LIBOR transition and SOFR
- Interest rate swaps and valuation
- Currency and cross-currency swaps
- Swap spreads and basis trading
- PSET VI Fixed Income and financial analysis
- PSET VI Fixed Income in modern finance
- Applications of PSET VI Fixed Income
- 'Case study: PSET VI Fixed Income'
- Duration and Convexity in Fixed Income Risk Management
- 'Valuation Methods: DCF, Comps, and Precedents'
- Yield Curve Analysis and Bond Valuation
- Value at Risk and Expected Shortfall
- Vasicek Interest Rate Model and Mean Reversion
- Short Rate Models and Term Structure Dynamics
- Company Valuation and Multiple Analysis
- Credit Risk Management and Default Probability
- Expected Loss and Loss Given Default Models
- Forward Rates and Curve Construction Methods
- Comparable Company Analysis and Trading Multiples
- 'Greeks: Delta, Gamma, Theta, and Vega Hedging'
- Ornstein-Uhlenbeck Process in Finance
- Options Trading Strategies and Risk Management
- Stress Testing and Extreme Value Analysis
- Fama-French Factors and Style Analysis
- Risk Measurement and VaR Backtesting
- Contango, Backwardation, and Roll Yield
- Futures and Forward Contracts in Financial Markets
- Bond Pricing and Yield to Maturity Analysis
- Fixed Income Securities and Credit Quality
- Hedge Strategies and Basis Risk Management
- Bond Portfolio Immunization Strategies
- Term Structure of Interest Rates and Yield Curves
- Option Valuation and Exercise Strategies
- Credit Spreads and Rating Migration Analysis
- Interest Rate Risk and DV01 Calculations
- Factor Models and Asset Pricing
- Government and Corporate Bond Markets
- Arbitrage Pricing Theory and Multi-Factor Models
linter-yaml-title-alias: FIXED INCOME ASSET PRICING BUS 35130 SPRING 2024 JOHN HEATON
tags:
- maturity
- options
- bonds
- put
- convexity
- swaps
- yield
- theta
- fixed-income
- bond
- call
- delta
- treasury
- interest-rates
- interest-rate
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
- bond-pricing
- option-strategies
- corporate-bonds
- yield-curve
- unexpected-loss
- clearinghouse
- interpolation
- interest-rate-risk
- arbitrage-pricing-theory
- hedge-ratio
- market-price-of-risk
- loss-given-default
- value-factor
- vasicek-model
- dirty-price
- monte-carlo-var
- options-trading
- coupon-bonds
- forward-contracts
- yield-to-maturity
- fama-french
- forward-rates
- price-to-earnings
- recovery-rate
- zero-coupon-bonds
- parametric-var
- lognormal-models
- var-methodologies
- historical-var
- mean-reversion
- contango
- modified-duration
- expected-loss
- quantitative-finance
- forward-curve
- protective-puts
- government-bonds
- probabilty-of-default
- curve-steepening
- curve-fitting
- roll-yield
- risk-premium
- spot-rates
- put-options
- affine-term-structure
- momentum
- curve-flattening
- basis-risk
- term-structure
- covered-calls
- ' exposure-at-default'
- stress-testing
- mathematical-finance
- ornstein-uhlenbeck
- rating-migration
- par-yield
- comparable-analysis
- investment-analysis
- economic-value-added
- duration-analysis
- value-at-risk
- factor-models
- barbell-strategy
- risk-management
- convergence
- var-backtesting
- sum-of-parts
- clean-price
- yield-curve-shocks
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
- bootstrap-method
- current-yield
title: PSET VI Fixed Inc
---
--

# PSET VI Fixed Income

## HOMEWORK 6

Due at the beginning of Class 8
Note As with past homeworks there are "guides" for doing the homework in Excel,  Matlab and Python. In each code provides partial solutions to the questions. To make the code run you are required to complete some formulas or to produce some of the results yourself. You are not required to use any of the guides,  but use of one of them is recommended.

## PRICING THE FREDDIE MAC 6% CALLABLE BOND

Attached below you will find the prospectus of Freddie Mac 6%,  20-year callable bond,  issued on June 7,  2007. Your task in this homework is to obtain its fair valuation,  using both the Ho-Lee model and the Simple BDT model. Proceed as follows:

[^1]: (CP) Use the data in *"HW6 Data Bonds.xls"* and extract the discount curve $Z(0,          T)$ from the Treasuries using Nelson-Siegel model.

- Here are the discount curves and forward rates and 6 month Treasury yields plotted against time to maturity.
- !500
- !500
[^1]: (CP) Build the Ho-Lee tree,  given by
$$r_{i+1,         j}=r_{i,         j}+\theta(i)\times\Delta+\sigma\times\sqrt{\Delta}\times\epsilon_{i+1}$$

where $σ$ is the volatility of interest rates,  $θ(i)$ are chosen to fit the term structure of interest rates exactly,  and
$$\epsilon(i)=\left\{\begin{array}{l l}{{+1}}&{{\mathrm{with~probability}}}\\ {{-1}}&{{\mathrm{with~probability}}}\end{array}\right.\;\;1/2$$

Let $r_0$ match the first zero-coupon bond $Z_0(0.5)$ from Nelson Siegel model. The methodology to fit the model to the term structure of interest rates is explained in TN4. Both the matlab file and the guide spreadsheet that are available contain the routine to build it. You need a value of σ. Use the data on six-months rates available in the dataset (HW6 FRB H15*.csv*) to estimate σ (this can be done by taking the standard deviation of first differences in interest rates,  over six-month periods,  which is one time step). Remember to *annualize* the volatility estimates,  as $σ$ in Ho-Lee and BDT are annualized.

- The volatility of interest rates in the Ho-Lee model is given by $$\sigma^{HL}_{r_{t}}=st.dev(r_{t+1}-r_{{t}})$$

	This gives the monthly volatility of interest rates under the Ho-Lee model.

	- To annualize this volatility,  we multiply by $\sqrt{12}$,  such that annual volatility under the Ho-Lee model is $\sigma^{HL}_{r_{t}}\sqrt{12}$ =
	- The volatility of interest rates in the Simple Black Derman Toy model is given by $\sigma^{BDT}_{z_{t}}=st.dev(\ln(r_{{t+1}}-\ln(r_{t})))$
	- To find the annualized rate,  we multiply by $\sigma^{BDT}_{z_{t}} \times \sqrt{ 12 }$ =
[^1]: (CP) After fitting the tree to the data,  please plot the zero-coupon bond yields from the tree and from the original zero-coupon bonds Z(T) obtained from Nelson and Siegel (and used as inputs for the tree). Are they the same? Show also the first 10 time-steps of the interest rate tree (table 10 x 10)
[^1]: The zero coupon bond yields derived from the Ho-Lee tree largely match those produced by the Nelson Siegel interpolation.
[^1]: !500
[^1]: (CP) Use the tree tree
ˆ Obtain the price of the non-callable bond
!500
ˆ Obtain the price of
!500
ˆ Obtain the price of the callable bond as the difference.
!500
## PLEASE,  MAKE SURE TO INCORPORATE THE FACT THAT THE CALLABLE BOND BECOMES CALLABLE ONLY AFTER THE FIRST-CALL-DATE

(Matlab users: please see below for a generic algorithm to compute prices through backward calculation)

[^1]: (CP) Show the first 10 nodes of the non-callable bond,  the option to call,  and the callable security.
[^1]: (CP) Plot the price of the non-callable and of the callable security against interest rates at call time,  as well as 1,  2,  3 semesters before. How does the callable and non-callable bonds compare? Comment and discuss.

!500

!500

!500

!500

[^1]: (CP) Compute the duration and convexity of callable and non-callable bond at time 0. Comment on the difference between the two securities.
[^1]: (CP) **Ho Lee versus Simple BDT.** Redo all of the points above for the Simple BDT model (note: in both the matlab file and the spreadsheet,  this amounts to change BDT Flag from 0 to 1 and re-run the routine to build the tree. Everything else should be automatic,  except for the estimate of σ which now should use log differences in rates). Comment on the difference in price,  if any,  from the two methodologies.
- THe prices derived from the Ho-Lee model and the Black Derman Toy model should be the same,  because both models use the same zero discount curve as the input,  though the BDT model has a larger volatility.
!500!500!500!500!500!500!500!500!500

---
enhanced: true
enhancement_date: '2025-11-06'
enhancement_id: batch03-3bfa6c
key_concepts:
- Apt
- Carry trades and momentum in FX markets
- Term structure of interest rates and yield curve shapes
- investment banking services and activities
- Duration and convexity analysis for bond portfolio management
- Sovereign risk assessment and country analysis
- Mean-variance optimization and the efficient frontier
- Extreme value theory and tail risk modeling
- Single-name vs. index CDS trading
- Credit risk modeling and default probability estimation
- Commodity markets and pricing dynamics
- Risk budgeting and portfolio construction techniques
- Expectations hypothesis and liquidity preference theory
- Historical simulation vs. parametric VaR models
- Yield curve fitting and interpolation methods
- Credit spread decomposition and hazard rates
- CDS clearing and central counterparties
- fixed income risk measurement
- DV01 calculation and interest rate risk hedging
- forward commitments and hedging
- CDS-Bond basis and arbitrrage opportunities
- Spot rates vs. forward rates modeling
- Mathematical Finance
- Monte Carlo integration and variance reduction
- Deposit insurance and systemic risk prevention
- Monte Carlo VaR for complex portfolios
- Shadow Banking
- Stress testing and scenario analysis
- Course Material
- Currency risk management and hedging
- Forward rates and interest rate parity
- Control variates and importance sampling techniques
- Value at Risk (VaR) methodologies and backtesting
- Risk-neutral pricing methodology for derivative securities
- Case Study
- Operational risk quantification and modeling
- Exchange rate determination and PPP theory
- Net interest margin analysis and banking profitability
- Arbitrage opportunities and risk-free profit extraction
- Expected Shortfall and coherent risk measures
- Credit default swap pricing and risk-neutral probabilities
- zero-coupon bond pricing and yields
- Bank liquidity ratios and funding risk management
- Credit exposure measurement and EAD
- par value in CDS settlement
- Value-at-Risk calculation using historical simulation
- Shadow banking system and regulatory arbitrage
- Credit risk migration matrices and rating transition
- Credit risk modeling and portfolio correlation analysis
- Backtesting procedures for risk models
- Credit risk assessment and loan portfolio management
- Hedge fund strategies and alternative investments
- Parallel and non-parallel shifts in the yield curve
- Liquidity risk measurement and management
- Systemic risk indicators and early warning systems
- Global financial stability and systemic risk monitoring
- Loss given default and recovery rates
- Currency markets and foreign exchange trading
tags:
- yield-curve
- commodities
- credit-default-swaps
- mathematical-finance
- course-material
- rating-agencies
- shadow-banking
- case-study
- apt
- value-at-risk
- exchange-rates
- hedge-funds
- credit-risk
- quantitative-implementation
- duration-convexity
- solution
- private-equity
- banking
- investment-banking
- stress-testing
- liquidity-risk
- systemic-risk
- deposit-insurance
- financial-intermediation
- duration
- expected-shortfall
- operational-risk
- monte-carlo
---

# The Nature and Variety of Financial Intermediation  

“Don’t it always seem to go that you don’t know what you’ve got ‘til it’s gone?”  

Joni Mitchell  

# GLOSSARY OF TERMS  

Euro: Common currency adopted by many member countries of the European Union.  

Yield curve: Relationship between yield to maturity and maturity on debt instruments identical in all respects except maturities (see Chapter 4). Duration: A measure of how long an investor must wait to receive payment on a bond. For bonds that repay only principal (zero coupon bonds), duration equals maturity. For coupon-paying bonds, duration is always shorter than maturity.  

Spot rate: The current yield to maturity on a bond of a given maturity.  

Liquidity premium: The amount by which the yield on a bond must be grossed up to compensate investors for their inability to convert the bond into cash at a moment’s notice and without loss relative to the bond’s true value.  

Consumer loans: Loans made to individuals and families. These are primarily installment loans.  

Commercial loans: Loans made to corporations. Often referred to as Commercial and Industrial (C&I) loan  

Contingent claims: Claims that may be made in the future, contingent on the realizations of some states.  

Federal funds: Funds in the interbank loan market. When a bank “sells” federal funds, it is lending (usually on an overnight basis) to another bank an amount that covers a part or all of that bank’s shortfall in reserves; banks are required to keep a certain fraction of their deposits as liquid reserves.  

rplus: Proceeds from the sale of equity and securities in excess of their par value, plus retained earnings.  

Cash and due: Coin and currency in the bank’s vaults, reserves on deposit with the Federal Reserve and with other banks, and checks deposited by customers on which funds have not yet been collected from the paying bank.  

Allowance for loan losses: An allowance made to absorb anticipated (expected) future loan losses. An allowance for loan losses is a charg against current income and it increases the bank’s loan loss reserve. Writeoffs of existing loans reduce the bank’s loan loss reserve.  

Undivided profits and reserves: Part of the bank’s net worth.  

Gramm–Leach–Bliley Act: The 1999 act that dismantled the Glass–Steagall Act restrictions separating commercial and investment banking.  

# INTRODUCTION  

This chapter focuses on the variety of services provided by financial intermediaries (FIs). Banks are members of an expansive industry that provides a dazzling variety of financial services. The broader financial services industry includes institutions as different as commercial banks, savings institutions, and credit unions, all of which finance their assets with deposits, and government agencies, credit-rating agencies, pension funds, loan sharks, pawnbrokers, lotteries, insurance companies, mutual funds, hedge funds, and private-equity pools. To this list we could add organized exchanges for trading stocks, futures, options, bonds and commodities, parimutuel betting institutions, credit-rating agencies, and the list can be extended almost effortlessly. Broadly speaking, these institutions can be classified into two groups: depository financial institutions and nondepository financial institutions. The former include institutions that finance themselves largely with deposits, whereas the latter fund themselves in the capital market. A subset of these nondepository institutions have come to be known as the “shadow banking system.”  

What all these financial institutions have in common is the processing of risk and its subtle complement, information. FIs produce information for two kinds of applications: (i) to match transactors like a marriage broker would, and (ii) to manage risks and transform the nature of claims as when a bank produces credit information to control a borrower’s credit risk. In producing information for application (i), the intermediary acts as a broker, whereas in producing information for application (ii), it acts as a qualitative asset transformer.

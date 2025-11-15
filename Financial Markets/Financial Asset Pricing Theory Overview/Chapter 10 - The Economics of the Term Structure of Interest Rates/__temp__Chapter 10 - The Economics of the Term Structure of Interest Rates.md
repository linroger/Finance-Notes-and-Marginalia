---
tags:
- apt
- arbitrage
- artificial-intelligence
- bond-pricing
- chapter_10
- defi
- economics
- equity-derivatives
- fixed-income
- fixed-income-derivatives
- interest-rate-derivatives
- interest_rates
- liquidity-risk
- ma
- markets
- mpt
- options
- options-pricing
- term-structure
- term_structure
- vasicek-model
- yield_curve
aliases: []
key_concepts:
- Agricultural futures and seasonality
- Alternative investments and hedge fund strategies
- Arbitrage Pricing Theory (APT) and factor models
- Arbitrage pricing theory (APT)
- Asset swaps and spread-lock strategies
- Bank capital adequacy and Basel III compliance
- Bank stress testing and CCAR requirements
- Barrier options and knock-in/knock-out structures
- Basel III capital requirements and risk metrics
- Basis swaps and cross-currency basis adjustments
- Basis swaps and floating rate correlations
- Behavioral finance and market anomalies
- Best execution and regulatory requirements
- Bid-ask spreads and market making profitability
- Binomial option pricing model with multi-period trees
- Black-Litterman model and portfolio optimization
- Black-Scholes option pricing model and its applications
- Bond portfolio immunization strategies
- CDO structuring and tranche allocation methodologies
- CDO-squared structures and correlation trading
- Calendar spreads and roll strategies
- Capital Asset Pricing Model (CAPM) and beta estimation
- Capital expenditure planning and depreciation
- Central clearing and CCP risk management
- Commodity futures and convenience yields
- Commodity swaps and energy derivatives
- Constant maturity swaps and roll-over features
- Corporate bond pricing and credit spread decomposition
- Crack spreads in energy markets
- Cryptocurrency valuation and blockchain technology
- Currency swaps and cross-currency basis
- Dark pools and alternative trading venues
- DeFi protocols and decentralized finance
- Deposit insurance and systemic risk
- Dividend discount model (DDM) applications
- Duration and convexity for bond price sensitivity
- ESG investing and sustainability metrics
- Enterprise value and equity value relationships
- Equity swaps and total return swaps
- Exotic derivatives and path-dependent options
- Expected Shortfall (ES) and coherent risk measures
- Extreme value theory and tail risk modeling
- FX futures and currency hedging
- Fama-French three-factor and five-factor models
- Fintech disruption and digital banking
- Forward contract pricing and cost of carry
- Forward rate models
- GARCH models for volatility forecasting
- Gamma trading and convexity adjustments
- Green bonds and climate risk assessment
- HJM and forward rate model frameworks
- Heath-Jarrow-Morton (HJM) framework
- Historical simulation and parametric VaR approaches
- Hull-White and Black-Karasinski short rate models
- IPO pricing and underpricing analysis
- Implied volatility and volatility surface modeling
- Inflation-linked swaps and CPI adjustments
- Interest rate curves
- Interest rate derivatives and forward rate agreements
- Interest rate models and term structure
- Interest rate swaps and swap spread decomposition
- Key rate duration and curve risk decomposition
- Liquidity coverage ratio and funding strategies
- Liquidity-adjusted VaR and liquidity horizons
- Margin requirements and collateral optimization
- Market impact and transaction cost analysis
- Mean reversion in interest rate processes
- Mergers and acquisitions due diligence
- Metal futures and industrial commodities
- Model backtesting and validation procedures
- Modern portfolio theory and efficient frontier
- Momentum and reversal investment strategies
- Mortgage-backed securities and prepayment modeling
- Multi-factor interest rate models
- Negative interest rates and floor/cap structures
- Net interest margin and banking profitability
- Netting agreements and close-out procedures
- Non-deliverable forwards and emerging market instruments
- OIS discounting and collateralized interest rate derivatives
- Options on futures and forward-starting options
- Payment systems and settlement risk
- Prime brokerage and securities lending
- Private credit and direct lending
- Project finance and syndicated lending
- Real estate investment trusts (REITs)
- Recovery rate modeling and loss given default
- Repo markets and securities lending
- Risk parity and risk budgeting strategies
- Shadow banking and non-bank intermediation
- Smart beta and alternative indexing approaches
- Spot rates
- Spot rates, forward rates, and discount factor curves
- Stochastic volatility in interest rate markets
- Stress testing and scenario analysis frameworks
- Swaptions and interest rate option pricing
- Swaptions and option volatility surfaces
- Synthetic CDOs and credit-linked note structures
- Term structure economics
- Terminal value modeling and exit multiples
- 'The Greeks: Delta, Gamma, Vega, Theta, and Rho sensitivity analysis'
- Too-big-to-fail policies and resolution regimes
- Treasury futures and bond basis
- Treasury securities and government bond markets
- VIX futures and volatility trading
- Value at Risk (VaR) and expected shortfall methodologies
- Value vs growth investing frameworks
- Vasicek and CIR interest rate models
- Vasicek and Cox-Ingersoll-Ross models
- Volatility smile and skew patterns in option markets
- Working capital and cash conversion cycle
- Wrong-way risk and correlation adjustments
- Yield curve analysis
- Yield curve construction and term structure modeling
- Zero-coupon bond pricing and bootstrapping
enhanced: true
enhancement_date: '2025-11-06'
enhancement_id: batch04-329991
---






# The economics of the term structure of interest rates  
10 The economics of the term structure of interest rates 243  
10.1 Introduction . 243   
10.2 Basic interest rate concepts and relations 244   
10.3 Real interest rates and aggregate consumption 247   
10.4 Real interest rates and aggregate production 250   
10.5 Equilibrium interest rate models 253   
10.5.1 The Vasicek model . 253   
10.5.2 The Cox-Ingersoll-Ross model . 257   
10.6 Real and nominal interest rates and term structures 260   
10.6.1 Real and nominal asset pricing 261   
10.6.2 No real effects of inflation/War%20Economies%20and%20Hyperinflation.md) 262   
10.6.3 A model with real effects of money - 263   
10.7 The expectation hypothesis 268   
10.7.1 Versions of the pure expectation hypothesis 268   
10.7.2 The pure expectation hypothesis and equilibrium 270   
10.7.3 The weak expectation hypothesis . . 272   
10.8 Liquidity preference, market segmentation, and preferred habitats 272   
10.9 Concluding remarks 273   
10.10 Exercises 273  

# 10.1 Introduction  

The previous two chapters focused on the implications of asset pricing models for the level of stock market excess returns and the cross-section of stock returns. This chapter focuses on the consequences of asset pricing theory for the pricing of bonds and the term structure of interest rates implied by bond prices.  

A bond is nothing but a standardized and transferable loan agreement between two parties. The issuer of the bond is borrowing money from the holder of the bond and promises to pay back the loan according to a predefined payment scheme. The presence of the bond market allows individuals to trade consumption opportunities at different points in time among each other. An individual who has a clear preference for current capital to finance investments or current consumption can borrow by issuing a bond to an individual who has a clear preference for future consumption opportunities. The price of a bond of a given maturity is, of course, set to align the demand and supply of that bond, and will consequently depend on the attractiveness of the real investment opportunities and on the individuals' preferences for consumption over the maturity of the bond. The term structure of interest rates will reflect these dependencies.  

After a short introduction to notation and bond market terminology in Section 10.2, we derive in Sections 10.3 and 10.4 relations between equilibrium interest rates and aggregate consumption and production in settings with a representative individual. In Section 10.5 we give some examples of equilibrium term structure models that are derived from the basic relations between interest rates, consumption, and production. The famous Vasicek model and Cox-Ingersoll-Ross model are presented.  

Since individuals are concerned with the number of units of goods they consume and not the dollar value of these goods, the relations found in those sections apply to real interest rates. However, most traded bonds are nominal, i.e. they promise the delivery of certain dollar amounts, not the delivery of a certain number of consumption goods. The real value of a nominal bond depends on the evolution of the price of the consumption good. In Section 10.6 we explore the relations between real rates, nominal rates, and inflation/War%20Economies%20and%20Hyperinflation.md). We consider both the case where money has no real effects on the economy and the case where money does affect the real economy.  

The development of arbitrage-free dynamic models of the term structure was initiated in the 1970 s. Until then, the discussions among economists about the shape of the term structure were based on some relatively loose hypotheses. The most well-known of these is the expectation hypothesis, which postulates a close relation between current interest rates or bond yields and expected future interest rates or bond returns. Many economists still seem to rely on the validity of this hypothesis, and a lot of man power has been spend on testing the hypothesis empirically. In Section 10.7, we review several versions of the expectation hypothesis and discuss the consistency of these versions. We argue that neither of these versions will hold for any reasonable dynamic term structure model. Some alternative traditional hypotheses are briefly reviewed in Section 10.8.

---
tags:
  - chapter_10
  - economics
  - interest_rates
  - term_structure
  - yield_curve
aliases: []
key_concepts:
  - Forward rate models
  - Interest rate curves
  - Spot rates
  - Term structure economics
  - Yield curve analysis
---



# The economics of the term structure of interest rates  
10 The economics of the [[6. A Brief Introduction to Stochastic Calculus|term structure of interest rates]] 243  
10.1 [[Squam Lake Group Introduction|Introduction]] . 243   
10.2 Basic interest rate concepts and relations 244   
10.3 [[Real Interest Rates and Aggregate Production|Real interest rates]] and [[Pareto-Optimality in Some Incomplete Markets|aggregate consumption]] 247   
10.4 [[Real Interest Rates and Aggregate Production|Real interest rates]] and [[Real Interest Rates and Aggregate Production|aggregate production]] 250   
10.5 [[Real Interest Rates and Aggregate Consumption|Equilibrium interest rate]] models 253   
10.5.1 The [[Vasicek Short Rate Model|Vasicek model]] . 253   
10.5.2 The Cox-Ingersoll-Ross model . 257   
10.6 Real and [[Real and Nominal Interest Rates and Term Struc|nominal interest rates]] and term structures 260   
10.6.1 Real and nominal [[Fixed Income Asset Pricing|asset pricing]] 261   
10.6.2 No real effects of [[War Economies and Hyperinflation|inflation]] 262   
10.6.3 A model with real effects of money - 263   
10.7 The expectation hypothesis 268   
10.7.1 Versions of the [[The Expectation Hypothesis|pure expectation hypothesis]] 268   
10.7.2 The [[The Expectation Hypothesis|pure expectation hypothesis]] and equilibrium 270   
10.7.3 The weak expectation hypothesis . . 272   
10.8 [[Class Note 10 Liquidity and Class Note 10 Liquidity and Liquidity Managementliquidity management|Liquidity]] [[Utility Indices|preference]], market segmentation, and preferred habitats 272   
10.9 Concluding remarks 273   
10.10 [[Exercises|Exercises]] 273  

# 10.1 Introduction  

The previous two chapters focused on the implications of [[Financial Mathematics Course|asset pricing models]] for the level of [[Hedge Fund Strategies|stock market]] excess [[Assets|returns]] and the cross-section of stock [[Assets|returns]]. This chapter focuses on the consequences of [[Mean-Variance Efficient Returns and Pricing Fac|asset pricing theory]] for the [[Arbitrage Pricing of Derivatives|pricing]] of bonds and the [[6. A Brief Introduction to Stochastic Calculus|term structure of interest rates]] implied by bond prices.  

A bond is nothing but a standardized and transferable loan agreement between two parties. The issuer of the bond is borrowing money from the holder of the bond and promises to pay back the loan according to a predefined payment scheme. The presence of the bond market allows individuals to trade consumption opportunities at different points in time among each other. An individual who has a clear [[Utility Indices|preference]] for current capital to finance investments or current consumption can borrow by issuing a bond to an individual who has a clear [[Utility Indices|preference]] for future consumption opportunities. The price of a bond of a given maturity is, of course, set to align the [[Currency Appreciation and Depreciation|demand and supply]] of that bond, and will consequently depend on the attractiveness of the real [[An Asset Allocation Primer|investment]] opportunities and on the individuals' preferences for consumption over the maturity of the bond. The [[6. A Brief Introduction to Stochastic Calculus|term structure of interest rates]] will reflect these dependencies.  

After a short [[Squam Lake Group Introduction|introduction]] to notation and bond market terminology in Section 10.2, we derive in Sections 10.3 and 10.4 relations between equilibrium [[Interest Rate Quotations|interest rates]] and [[Pareto-Optimality in Some Incomplete Markets|aggregate consumption]] and production in settings with a [[The Simple Multi-Period Ccapm|representative individual]]. In Section 10.5 we give some examples of [[Chapter 49 - Equilibrium Models: Term Structure|equilibrium term structure]] models that are derived from the basic relations between [[Interest Rate Quotations|interest rates]], consumption, and production. The famous [[Vasicek Short Rate Model|Vasicek model]] and Cox-Ingersoll-Ross model are presented.  

Since individuals are concerned with the number of units of goods they consume and not the dollar value of these goods, the relations found in those sections apply to [[Real Interest Rates and Aggregate Production|real interest rates]]. However, most traded bonds are nominal, i.e. they promise the delivery of certain dollar amounts, not the delivery of a certain number of consumption goods. The real value of a nominal bond depends on the evolution of the price of the consumption good. In Section 10.6 we explore the relations between real rates, nominal rates, and [[War Economies and Hyperinflation|inflation]]. We consider both the case where money has no real effects on the economy and the case where money does affect the real economy.  

The development of [[Arbitrage Pricing of Derivatives|arbitrage]]-free dynamic models of the [[The Vasicek Model|term structure]] was initiated in the 1970 s. Until then, the discussions among economists about the shape of the [[The Vasicek Model|term structure]] were based on some relatively loose hypotheses. The most well-known of these is the expectation hypothesis, which postulates a close relation between current [[Interest Rate Quotations|interest rates]] or bond yields and [[The Expectation Hypothesis|expected future interest rates]] or bond [[Assets|returns]]. Many economists still seem to rely on the validity of this hypothesis, and a lot of man power has been spend on testing the hypothesis empirically. In Section 10.7, we review several versions of the expectation hypothesis and discuss the consistency of these versions. We argue that neither of these versions will hold for any reasonable dynamic [[The Vasicek Model|term structure]] model. Some alternative traditional hypotheses are briefly reviewed in Section 10.8.  
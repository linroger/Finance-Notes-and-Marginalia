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
10 The economics of the [term structure of interest rates](../../../Financial%20Engineering/6.%20A%20Brief%20Introduction%20to%20Stochastic%20Calculus.md) 243  
10.1 [Introduction](../../../Financial%20Markets%20and%20Institutions/III.%20Liquidity%20of%20Assets/Class%209-%20Bailouts%20and%20Bank%20Failures/Squam%20Lake%20Group%20Introduction.md) . 243   
10.2 Basic interest rate concepts and relations 244   
10.3 [Real interest rates](Real%20Interest%20Rates%20and%20Aggregate%20Production.md) and [aggregate consumption](../Chapter%207%20-%20Market%20equilibrium/Pareto-Optimality%20in%20Some%20Incomplete%20Markets.md) 247   
10.4 [Real interest rates](Real%20Interest%20Rates%20and%20Aggregate%20Production.md) and [aggregate production](Real%20Interest%20Rates%20and%20Aggregate%20Production.md) 250   
10.5 [Equilibrium interest rate](Real%20Interest%20Rates%20and%20Aggregate%20Consumption.md) models 253   
10.5.1 The [Vasicek model](../../../Fixed%20Income%20Asset%20Pricing/Fixed%20Income%20Lecture%20Notes/Vasicek%20Short%20Rate%20Model.md) . 253   
10.5.2 The Cox-Ingersoll-Ross model . 257   
10.6 Real and [nominal interest rates](Real%20and%20Nominal%20Interest%20Rates%20and%20Term%20Struc.md) and term structures 260   
10.6.1 Real and nominal [asset pricing](../../../Fixed%20Income%20Asset%20Pricing/Fixed%20Income%20Asset%20Pricing.md) 261   
10.6.2 No real effects of [inflation](../../../International%20Finance/Bridgewater/Principles%20For%20Navigating%20Big%20Debt%20Cycles/Part%20II%20Detailed%20Case%20Studies/German%20Debt%20Crisis%20andHyperinflation%20(1918–1924)/War%20Economies%20and%20Hyperinflation.md) 262   
10.6.3 A model with real effects of money - 263   
10.7 The expectation hypothesis 268   
10.7.1 Versions of the [pure expectation hypothesis](The%20Expectation%20Hypothesis.md) 268   
10.7.2 The [pure expectation hypothesis](The%20Expectation%20Hypothesis.md) and equilibrium 270   
10.7.3 The weak expectation hypothesis . . 272   
10.8 [Liquidity](../../../Financial%20Markets%20and%20Institutions/III.%20Liquidity%20of%20Assets/Class%205-%20Private%20Information,%20Liquidity,%20and%20Securitization/Class%20Note%2010%20Liquidity%20and%20Class%20Note%2010%20Liquidity%20and%20Liquidity%20Managementliquidity%20management.md) [preference](../Chapter%205%20-%20Modeling%20the%20Preferences%20of%20Individuals/Utility%20Indices.md), market segmentation, and preferred habitats 272   
10.9 Concluding remarks 273   
10.10 [Exercises](Exercises.md) 273  

# 10.1 Introduction  

The previous two chapters focused on the implications of [asset pricing models](../../../Financial%20Engineering/Financial%20Mathematics%20Course.md) for the level of [stock market](../../Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20III%20THE%20PLAYERS/Chapter%2012%20-%20Hedge%20Fund%20Strategies/Hedge%20Fund%20Strategies.md) excess [returns](../Chapter%203%20-%20%20Assets,%20Portfolios,%20and%20Arbitrage/Assets.md) and the cross-section of stock [returns](../Chapter%203%20-%20%20Assets,%20Portfolios,%20and%20Arbitrage/Assets.md). This chapter focuses on the consequences of [asset pricing theory](../Chapter%209%20-%20Factor%20Models/Mean-Variance%20Efficient%20Returns%20and%20Pricing%20Fac.md) for the [pricing](../../Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%207/Arbitrage%20Pricing%20of%20Derivatives.md) of bonds and the [term structure of interest rates](../../../Financial%20Engineering/6.%20A%20Brief%20Introduction%20to%20Stochastic%20Calculus.md) implied by bond prices.  

A bond is nothing but a standardized and transferable loan agreement between two parties. The issuer of the bond is borrowing money from the holder of the bond and promises to pay back the loan according to a predefined payment scheme. The presence of the bond market allows individuals to trade consumption opportunities at different points in time among each other. An individual who has a clear [preference](../Chapter%205%20-%20Modeling%20the%20Preferences%20of%20Individuals/Utility%20Indices.md) for current capital to finance investments or current consumption can borrow by issuing a bond to an individual who has a clear [preference](../Chapter%205%20-%20Modeling%20the%20Preferences%20of%20Individuals/Utility%20Indices.md) for future consumption opportunities. The price of a bond of a given maturity is, of course, set to align the [demand and supply](../../../International%20Finance/China%20Foreign%20Exchange%20Reserves/Currency%20Appreciation%20and%20Depreciation.md) of that bond, and will consequently depend on the attractiveness of the real [investment](../../../Advanced%20Investments/An%20Asset%20Allocation%20Primer.md) opportunities and on the individuals' preferences for consumption over the maturity of the bond. The [term structure of interest rates](../../../Financial%20Engineering/6.%20A%20Brief%20Introduction%20to%20Stochastic%20Calculus.md) will reflect these dependencies.  

After a short [introduction](../../../Financial%20Markets%20and%20Institutions/III.%20Liquidity%20of%20Assets/Class%209-%20Bailouts%20and%20Bank%20Failures/Squam%20Lake%20Group%20Introduction.md) to notation and bond market terminology in Section 10.2, we derive in Sections 10.3 and 10.4 relations between equilibrium [interest rates](../../Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%202/Interest%20Rate%20Quotations.md) and [aggregate consumption](../Chapter%207%20-%20Market%20equilibrium/Pareto-Optimality%20in%20Some%20Incomplete%20Markets.md) and production in settings with a [representative individual](../Chapter%208%20-%20Consumption-Based%20Asset%20Pricing/The%20Simple%20Multi-Period%20Ccapm.md). In Section 10.5 we give some examples of [equilibrium term structure](../../../Financial%20Engineering/Derivatives/Part%20XII%20-%20Price%20Dynamics/Chapter%2049%20-%20Equilibrium%20Models:%20Term%20Structure.md) models that are derived from the basic relations between [interest rates](../../Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%202/Interest%20Rate%20Quotations.md), consumption, and production. The famous [Vasicek model](../../../Fixed%20Income%20Asset%20Pricing/Fixed%20Income%20Lecture%20Notes/Vasicek%20Short%20Rate%20Model.md) and Cox-Ingersoll-Ross model are presented.  

Since individuals are concerned with the number of units of goods they consume and not the dollar value of these goods, the relations found in those sections apply to [real interest rates](Real%20Interest%20Rates%20and%20Aggregate%20Production.md). However, most traded bonds are nominal, i.e. they promise the delivery of certain dollar amounts, not the delivery of a certain number of consumption goods. The real value of a nominal bond depends on the evolution of the price of the consumption good. In Section 10.6 we explore the relations between real rates, nominal rates, and [inflation](../../../International%20Finance/Bridgewater/Principles%20For%20Navigating%20Big%20Debt%20Cycles/Part%20II%20Detailed%20Case%20Studies/German%20Debt%20Crisis%20andHyperinflation%20(1918–1924)/War%20Economies%20and%20Hyperinflation.md). We consider both the case where money has no real effects on the economy and the case where money does affect the real economy.  

The development of [arbitrage](../../Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%207/Arbitrage%20Pricing%20of%20Derivatives.md)-free dynamic models of the [term structure](../../Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%209/The%20Vasicek%20Model.md) was initiated in the 1970 s. Until then, the discussions among economists about the shape of the [term structure](../../Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%209/The%20Vasicek%20Model.md) were based on some relatively loose hypotheses. The most well-known of these is the expectation hypothesis, which postulates a close relation between current [interest rates](../../Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%202/Interest%20Rate%20Quotations.md) or bond yields and [expected future interest rates](The%20Expectation%20Hypothesis.md) or bond [returns](../Chapter%203%20-%20%20Assets,%20Portfolios,%20and%20Arbitrage/Assets.md). Many economists still seem to rely on the validity of this hypothesis, and a lot of man power has been spend on testing the hypothesis empirically. In Section 10.7, we review several versions of the expectation hypothesis and discuss the consistency of these versions. We argue that neither of these versions will hold for any reasonable dynamic [term structure](../../Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%209/The%20Vasicek%20Model.md) model. Some alternative traditional hypotheses are briefly reviewed in Section 10.8.  
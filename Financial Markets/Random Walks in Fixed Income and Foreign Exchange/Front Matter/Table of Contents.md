---
tags:
  - conversion_factor
  - cross_currency_basis
  - empirical_method
  - fixed_income
  - forward_curve
  - fx_hedging
  - maturity_matched
  - rolling_hedges
  - term_premium
  - xva
aliases:
  - FX Hedged Pickup
  - Table of Contents
  - Term Premium
  - XCCY Basis
key_concepts:
  - Conversion Factor Examples
  - Cross-Currency Basis Swap
  - Defining Convexity
  - Defining Duration
  - FX Hedge Strategies
  - Forward Curve Analysis
  - Maturity-Matched Hedges
  - Term Premium Calculation
  - XVA Calculation
---

# Table of Contents - Random Walks in Fixed Income and Foreign Exchange
# Contents

Foreword

Preface

**Chapter 1** What Really is the [Cross-Currency Basis](../Chapter%203/Calculating%20Novel%20Cross-Currency%20Bases%20a.md)?
*   The Calculation Underlying the [Cross-Currency Basis Swap](.md)
*   A Quick Note on Terminology
*   Perhaps the Simplest Formula in [Financial Mathematics](../../../Financial%20Engineering/Financial%20Mathematics%20Course.md)
*   How the Calculation Distorts [No-Arbitrage Pricing](../../../Pricing%20Forwards,%20Futures,%20Bonds,%20Swaps,%20Swaptions,%20Caps%20and%20Floors%20under%20No-Arbitrage%20and%20Risk-Neutral%20Pricing.md)
*   On 29th December 2011
*   So, What Actually is a '[Cross-Currency Basis Swap](.md)'?
*   Conversion Factor
*   Where does the [Cross-Currency Basis](../Chapter%203/Calculating%20Novel%20Cross-Currency%20Bases%20a.md) Come from?
*   What Keeps the [Basis Swap](../../Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%2013/Basis%20Swaps.md) from Being Arbitraged Away?
*   Capital Cost of FX [Derivatives](../../Financial%20Trading%20and%20Markets/Chapter%209%20Arbitrage%20and%20Hedging%20With%20Options.md)
*   Counterparty Risks and Credit Limits
*   Clearing
*   Horses for Courses
*   How Could an Institution Make Money from the [Cross-Currency Basis Swap](.md)?
*   Appendix 1.A: The FX [Carry Trade](../../../Clippings/Currency%20Carry%20Trade.md)
*   Appendix 1.B: The Cross-[Currency](../../../Financial%20Instruments/Lecture%20Notes-%20Financial%20Instruments/Teaching%20Note%201-%20Forward%20Rates%20Agreement/Forwards%20and%20Futures%20Notes.md) Toolkit

**Chapter 2** XVA and the [Cross-Currency Basis](../Chapter%203/Calculating%20Novel%20Cross-Currency%20Bases%20a.md)
*   XVA - What is It?
*   A Brief Summary of Counterparty Risk
*   Risk vs Cost
*   CVA - The First Horse in the XVA Stable
*   DVA - The Next Calculation
*   FVA - Funding Impact
*   How [XVA Costs](../Chapter%202/XVA%20and%20the%20Cross-Currency%20Basis.md) Could Affect the [Cross-Currency Basis](../Chapter%203/Calculating%20Novel%20Cross-Currency%20Bases%20a.md)
*   Sample [XVA Calculation](.md) Using Market Standard Calculation Approach
*   Funding Constraints
*   Detail on Daily Funding/Rollover Process
*   Historical Funding Data
*   Trading the [xccy Basis](.md)

**Chapter 3** Calculating Novel Cross-[Currency](../../../Financial%20Instruments/Lecture%20Notes-%20Financial%20Instruments/Teaching%20Note%201-%20Forward%20Rates%20Agreement/Forwards%20and%20Futures%20Notes.md) Bases and FX [Hedged Pickups](../Chapter%203/Calculating%20Novel%20Cross-Currency%20Bases%20a.md)
*   What is the [FX Hedged Pickup](.md)?
*   Finding xccy Bases
*   Calculating [FX Hedged Pickup](.md)
*   Appendix 3.A: Xccy Bases
*   Appendix 3.B: FX [Hedged Pickups](../Chapter%203/Calculating%20Novel%20Cross-Currency%20Bases%20a.md)

**Chapter 4** [Hedging](../../Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%205/Key%20Rates%20O1s%20Durations%20and%20Hedging.md) of [Fixed Income](../../../Fixed%20Income%20Asset%20Pricing/Lecture%20Notes%20Bonds,%20%20Preferred%20Stock,%20%20and%20Structured%20Products.md) -- What is the Best Way?
*   [FX Hedge Strategies](.md)
*   [Maturity-Matched Hedges](.md)
*   Reducing Uncertainty to the Minimum Level for the Whole Tenor
*   Practical Calculation of Maturity-Matched Yield Pickup
*   Historical Results for G10 Maturity-Matched Yield Pickup
*   Rolling Hedges
*   Taking a Short-Term View
*   Possible Actions at 'Roll Point'
*   Historical Results for G10 Rolling Yield Pickup
*   Rolling Pickup 'One Period On' and for the Tenor of the Instrument
*   Translation Effect
*   Volatility Breakdown - What is Driving the Performance?
*   Numerical Example

**Chapter 5** Introducing the Conversion Factor
*   The [Issuer's Choices](../Chapter%205/Introducing%20the%20Conversion%20Factor.md)
*   Tenor
*   [Credit Spread](../../Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%2014/Cds-Equivalent%20Bond%20Spread.md)
*   [Cross-Currency Basis](../Chapter%203/Calculating%20Novel%20Cross-Currency%20Bases%20a.md)
*   Conversion Factor
*   Fees and Charges
*   What is the Conversion Factor?
*   Simplest Possible Example - 1-Year Bond, Zero Basis, USD Corporate
*   More Realistic - Using the Yield Curve
*   Another Way to Think about It
*   Examples of [Conversion Factors](../../Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%2011/Mechanics%20of%20Us%20Treasury%20Note%20and%20Bond%20Futures.md)
*   [Forecasting](../../../Advanced%20Financial%20Analysis%20and%20Valuation/Lecture%20Notes%20Advanced%20Financial%20Analysis%20and%20Valuation/Week%202/Week%202%20Fundamentals%20Of%20Forecasting.md) [Conversion Factors](../../Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%2011/Mechanics%20of%20Us%20Treasury%20Note%20and%20Bond%20Futures.md)
*   Translating Spreads across Currencies

**Chapter 6** An Empirical Method of Calculating the [Term Premium](.md)
*   [Introduction](../../../Financial%20Markets%20and%20Institutions/III.%20Liquidity%20of%20Assets/Class%209-%20Bailouts%20and%20Bank%20Failures/Squam%20Lake%20Group%20Introduction.md)
*   Why is the [Term Premium](.md) Important?
*   The [Term Premium](.md) and Forward Rates
*   An Empirical Method for Determining the [Term Premium](.md)
*   Results
*   Median (Predicted - Actual) Moves for USD
*   Choice of Forward Curve
*   Lookback Period
*   [Discount Factor](../../Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%201/Discount%20Factors.md) Calculation
*   10y [Term Premium](.md) Results
*   2y [Term Premium](.md) Results
*   Recent Results: A General Pitfall with [Term Premium](.md) Methods
*   Discussion of Results
*   Appendix 6.A: BIS Report Graphs
*   References

**Chapter 7** An Update of the [Term Premium Calculation](.md)
*   [Introduction](../../../Financial%20Markets%20and%20Institutions/III.%20Liquidity%20of%20Assets/Class%209-%20Bailouts%20and%20Bank%20Failures/Squam%20Lake%20Group%20Introduction.md)
*   Evolution of Yield Curves
*   [Term Premium](.md) Values Over Time
*   [Term Premium](.md) Models; Similarities and Differences
*   Aggregating Model Results

**Chapter 8** Forward Curves, [Duration and Convexity](../../Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%208/An%20Analytical%20Decomposition%20of%20Forward%20Rates.md)
*   Are the [Forwards](../../Financial%20Asset%20Pricing%20Theory%20Overview/Chapter%2012%20-%20Derivatives/Forwards%20and%20Futures.md) a Useful Forecast?
*   Why are Forward Curves so 'Abnormal'?
*   Simple Spot and Forward Curve Evolution
*   Forward Implied Slopes vs Realised Data
*   Analysis of Mean Forecast Slope vs Mean Actual Slope
*   Forward Implied Slopes and Direction
*   Can We Monetise This?
*   The Value of [Convexity](../../../Fixed%20Income%20Asset%20Pricing/Problem%20Sets/PSET%20II%20Fixed%20Income%20Asset%20Pricing%201.md)
*   [Defining Duration](.md)
*   [Defining Convexity](.md)
*   Numerical Calculation of [Convexity](../../../Fixed%20Income%20Asset%20Pricing/Problem%20Sets/PSET%20II%20Fixed%20Income%20Asset%20Pricing%201.md)
*   The Long End of the Curve
*   Value of [Convexity](../../../Fixed%20Income%20Asset%20Pricing/Problem%20Sets/PSET%20II%20Fixed%20Income%20Asset%20Pricing%201.md) through Time
*   Conclusion
*   Appendix 8.A: EUR Ratios
*   Appendix 8.B: USD Ratios
*   Appendix 8.C: Implied vs Actual Slope Changes, 2001-2007
*   Appendix 8.D: Implied vs Actual Slope Changes, 2007-2014
*   Appendix 8.E: Implied vs Actual Slope Changes, 2014-2020

**Chapter 9** Implied vs [Realised Convexity](../Chapter%209/Implied%20Vs%20Realised%20Convexity.md)
*   [Defining Convexity](.md)
*   Value of Implied [Convexity](../../../Fixed%20Income%20Asset%20Pricing/Problem%20Sets/PSET%20II%20Fixed%20Income%20Asset%20Pricing%201.md)
*   Value of [Realised Convexity](../Chapter%209/Implied%20Vs%20Realised%20Convexity.md)

List of Figures

List of Tables

About the Authors

References

Index

# Preface

The first section examines the rise of the [cross-currency basis](../Chapter%203/Calculating%20Novel%20Cross-Currency%20Bases%20a.md) in the post-crisis world, digs into its origins and applications, and investigates the implication of the new credit-sensitive world for issuance, [investment](../../../Advanced%20Investments/An%20Asset%20Allocation%20Primer.md) and [hedging](../../Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%205/Key%20Rates%20O1s%20Durations%20and%20Hedging.md). In Chapter 1, we define and dig into the origins of the basis, which before 2008 would have represented a juicy [arbitrage](../../Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%207/Arbitrage%20Pricing%20of%20Derivatives.md) opportunity. Understanding why this is not so today leads us to the discussion in Chapter 2 about the drivers and sustainers of the basis, and in Chapter 3 we show that it is possible to derive and create many cross-[currency](../../../Financial%20Instruments/Lecture%20Notes-%20Financial%20Instruments/Teaching%20Note%201-%20Forward%20Rates%20Agreement/Forwards%20and%20Futures%20Notes.md) bases which are not usually quoted in the market but which can represent very real opportunities for issuers and investors. Chapter 4 derives a new way of looking at [FX hedging](../Chapter%204/Fx%20Hedging%20of%20Fixed%20Income%20-%20What%20Is%20the.md) of [fixed income](../../../Fixed%20Income%20Asset%20Pricing/Lecture%20Notes%20Bonds,%20%20Preferred%20Stock,%20%20and%20Structured%20Products.md) assets, followed by Chapter 5, which shows how to analyse these hedged assets and understand the linked effects of the basis and the two yield curves which underly their valuation.

The second section examines the impact of the new world on the yield curve, and vice versa. [Term premium](.md), [duration and convexity](../../Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%208/An%20Analytical%20Decomposition%20of%20Forward%20Rates.md) all take on new importance in this new state of ultra-low rates and flat term structures. The search for yield in this brave new world has driven issuers to issue, and investors to buy, century-long bonds, in a world where only a scant handful of currencies have ever survived that long. [Convexity](../../../Fixed%20Income%20Asset%20Pricing/Problem%20Sets/PSET%20II%20Fixed%20Income%20Asset%20Pricing%201.md) has been a driver of this process - whether for good or bad, time will tell. We show how to derive a closed-form solution for both [duration and convexity](../../Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%208/An%20Analytical%20Decomposition%20of%20Forward%20Rates.md), and show how implied [convexity](../../../Fixed%20Income%20Asset%20Pricing/Problem%20Sets/PSET%20II%20Fixed%20Income%20Asset%20Pricing%201.md) at the start of the life of a bond can be compared to its realised value through its lifetime.
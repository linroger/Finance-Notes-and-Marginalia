---
academic_level: graduate
aliases:
- Interest Rate Swap Spreads
- Swap Spread Determinants
- Swap Spread Factors
enhanced: true
enhancement_date: '2025-11-06'
enhancement_id: batch09-000337
key_concepts:
- Options Greeks and sensitivity analysis for risk management
- Duration analysis and interest rate risk management
- Convexity adjustments and yield curve sensitivity
- Credit default swaps (CDS) and credit risk modeling
- Interest rate swaps and fixed income derivatives
- Value at Risk (VaR) and tail risk measurement
- Expected shortfall and coherent risk measures
- LIBOR market model and multi-curve framework
- Basel accords and banking regulation framework
- Arbitrage opportunities and no-arbitrage pricing
- Volatility modeling and estimation techniques
- Correlation analysis and dependency structures
- Risk preference theory and utility functions
- Yield Curve Analysis and Bond Valuation
- Value at Risk and Expected Shortfall
- Credit Risk Management and Default Probability
- Expected Loss and Loss Given Default Models
- Forward Rates and Curve Construction Methods
- Swap Market Mechanisms and Pricing
- Delta, Gamma, and Vega Hedging Techniques
- Price Discovery and Market Efficiency
- Stress Testing and Extreme Value Analysis
- Credit Default Swaps and Credit Risk Transfer
- Fama-French Factors and Style Analysis
- Risk Measurement and VaR Backtesting
- Bid-Ask Spreads and Market Impact
- Contango, Backwardation, and Roll Yield
- Futures and Forward Contracts in Financial Markets
- Bond Pricing and Yield to Maturity Analysis
- Fixed Income Securities and Credit Quality
- Hedge Strategies and Basis Risk Management
- Dynamic vs Static Hedging in Practice
- Interest Rate Swaps and Currency Swap Structures
- Term Structure of Interest Rates and Yield Curves
- Market Microstructure and Liquidity Analysis
- Credit Spreads and Rating Migration Analysis
- Hedging Strategies and Risk Mitigation
- Factor Models and Asset Pricing
- Government and Corporate Bond Markets
- Arbitrage Pricing Theory and Multi-Factor Models
professional_application: theoreti
status: active
tags:
- arbitrage-free-models
- arbitrage-opportunity
- asset-backed-securities
- banking-regulation
- basel-accord
- bid-ask-spread
- capital-adequacy
- caplet
- cds
- coherent-risk-measure
- conditional-var
- convexity-adjustment
- counterparty-risk
- credit-default-swap
- credit-derivatives
- expected-shortfall
- extreme-value-theory
- arbitrage
- book-to-market
- backwardation
- volatility-analysis
- style-analysis
- bond-pricing
- corporate-bonds
- yield-curve
- unexpected-loss
- clearinghouse
- interpolation
- overnight-indexed-swaps
- arbitrage-pricing-theory
- hedge-ratio
- price-discovery
- loss-given-default
- value-factor
- dirty-price
- dynamic-hedging
- monte-carlo-var
- coupon-bonds
- market-impact
- forward-contracts
- yield-to-maturity
- fama-french
- forward-rates
- recovery-rate
- zero-coupon-bonds
- parametric-var
- var-methodologies
- historical-var
- contango
- vega-hedging
- expected-loss
- market-efficiency
- delta-hedging
- forward-curve
- order-flow
- currency-swaps
- government-bonds
- probabilty-of-default
- liquidity
- curve-fitting
- gamma-hedging
- hedge-effectiveness
- credit-default-swaps
- roll-yield
- spot-rates
- algorithmic-trading
- momentum
- basis-risk
- hedge-strategies
- term-structure
- sofr
- swap-rate
- ' exposure-at-default'
- stress-testing
- roll-over-risk
- rating-migration
- par-yield
- investment-analysis
- value-at-risk
- factor-models
- risk-management
- convergence
- var-backtesting
- cross-hedging
- clean-price
- yield-curve-shocks
- high-frequency-trading
- fixed-income
- swap-spread
- credit-migration
- default-probability
- marking-to-market
- total-return-swaps
- libor
- credit-spreads
- multi-factor-models
- financial-markets
- static-hedging
- size-effect
- basis-swaps
- interest-rate-swaps
- futures-contracts
- apt
- bootstrap-method
- current-yield
type: note
---
--



# [](../1.%20DeterministicCashFlows.md#4.1%20The%20Yield%20Spread | The%20Determinants%20of%20the%20Swap%20Spread)
Interest-rate swaps are an important ALM and risk management tool in banking markets.  The rate payable on a swap represents bank risk, if we assume that a swap is paying  (receiving) the fixed swap rate on one leg and receiving (paying) Libor-flat on the other  leg. If one of the counter parties is not a bank, then either leg is adjusted to account for the  different counter party risk; usually the floating leg will have a spread added to Libor. We  can see that this produces a swap curve that lies above the government bond yield curve,  if we compare Figure 1 with Figure 2. Figure 1 is the USD swap rates page from Tullett  & Tokyo brokers, and Figure 2 is the US Treasury yield curve, both as at 3 July 2006.  The higher rates payable on swaps represents the additional risk premium associated with  bank risk compared to government risk. The spread itself is the number of basis points  the swap rate lies above the equivalent-maturity government bond yield, quoted on the  same interest basis.

 !500

 !500

Figure 1 USD interest-rate swap rates, 3 July 2007      Bloomberg L.P.      Tullett & Toyko. Used with permission
 !500

# Figure 2 US Treasury yield curve, 3 July 2006      Bloomberg L.P. Used with permission.

In theory, the swap spread represents only the additional credit risk of the interbank  market above the government market. However as the spread is variable, it is apparent  that other factors influence it. An ALM desk will want to be aware of these factors,  because they influence swap rates. Swaps are an important risk hedging tool, if not the  most important, for banks so it becomes necessary for practitioners to have an  appreciation of what drives the swap spreads

# Historical pattern

If we plot swap spreads over the last ten years, we note that they have tightened in the  last five years or so. Figure 3 shows the spread for USD and GBP for the period 1997-to  the first quarter of 2006.
 !500
Figure 3 USD and GBP interest-rate swap spreads over government curve, 1997- 2006  (Source: Bloomberg L.P.)

We see that spreads have reduced in recent years. The highest spreads for both currencies  was reached during 2000, when the 10-year sterling swap spread peaked at around 140  bps above the gilt yield. The tightest spreads were reached during 2003, when the 10-year  sterling spread reached around 15 bps towards the end of that year.  At the beginning of  2006 sterling spreads were still lower than the 10-year average of 55 bps. This implies  that the perceived risk premium for the capital markets has fallen.

Note how the change in spread levels coincides with macro-level factors and occurrences.  For instance, spreads have moved in line with:

  the Asian currency crises of 1997;    the Russian government bond default and collapse of the Long Term Capital  Management hedge fund in1998;    the “dot.com” crash in 2000;    the subsequent loosening of monetary policy after the dot.com crash and the  events of 9/11.
This indicates to us, if just superficially, that swap spreads react to macro-level factors  that are perceived by the market to affect their business risk, credit risk and liquidity risk.  Spreads also reflect supply and demand, as well as the absolute level of base interest rates.

# Determinants of the spread

We already noted that in theory the swap spread, representing interbank counter party risk,  should reflect only the market’s perception of bank risk over and above government risk.  Bank risk is captured in the Libor rate – the rate paid by banks on unsecured deposits to  other banks.  So in other words, the swap spread is meant to adequately compensate  against the risk of bank default. The Libor rate is the floating rate paid against the fixed in  the swap transaction, and moves with the perception of bank risk. As we implied in the  previous section though, it would appear that other factors influence the swap spread. We  can illustrate this better comparing the swap spread for 10-year quarterly-paying swaps  with the spread between 3-month Libor and the 3-month general collateral (GC)) repo  rate. The GC rate is the risk-free borrowing rate, whereas the Libor rate represents bank  risk again. In theory, the spread between 3-month Libor and the GC rate should therefore  move closely with the swap spread for quarterly-resetting swaps, as both represent bank  risk. A look at Figure 4 shows us that this is not the case. Figure 4 compares the two  spreads in the US dollar market, but we do not need to calculate the correlation or the   $R^{2}$    for the two sets of numbers. Even on cursory observation we can see that the correlation  is not high. Therefore we conclude that other factors, in addition to perceived bank  default risk, drive one or both spreads. These other factors influence swap rates and  government bond yields, and hence the swap spread, and we consider them below:
 !500
Figure 4 Comparison of USD 10-year swap spread and 3-month Libor-GC repo  spread  (Source: Bloomberg L.P.)

  Level and slope of the yield curve

The magnitude of the swap spread is influenced by the absolute level of base interest  rates. If the base rate is   $10\%$   so that the government short-term rate is around   $10\%$  ,  with longer-term rates being recorded higher, the spread tends to be greater that that  seen if the base rate is   $5\%$  .  The shape of the yield curve has even greater influence.  When the curve is positively sloping, under the expectations hypothesis investors will  expect future rates to be higher, hence floating rates are expected to rise. This would  suggest the swap spread will narrow. The opposite happens if the yield curve inverts

Figure 5 shows the GBP 10-year swap spread compared to the GBP gilt yield curve  spread (10-year gilt yield minus 2-year yield). We see that the slope of the curve has  influenced the swap spread; as the slope is narrowing, swap spreads are increasing  and vice-versa.
 !500
Figure 5 GBP swap spreads and gilt spreads compared 1997-2006  (Source: Bloomberg L.P.)

  Supply and demand

The swap spread is influenced greatly by supply and demand for swaps. For example,  greater volumes cash market instruments drive up a need for hedging instruments,  which will widen swap spreads. The best example of this is corporate bond issuance;  as volumes increase the need for underwriters to hedge increases. However greater  bond issuance also has another impact, as issuers seek to swap their fixed-rate  liabilities to floating-rate. This also increases demand for swaps

  Market volatility

As suggested by Figure 3, swap spreads widen during times of market volatility. This  may be in times of market uncertainty (for example, the future direction of base rates  or possible inversion of the yield curve) or in times of market shock such as 9/11. In  some respects widening during periods of volatility reflects the perception of  increased bank default risk. It also reflects the “flight to quality” that occurs during  times of volatility or market correction: this is the increased demand for risk-free  assets such as government bonds that drives their yields lower and hence swap  spreads wider.
The level of government borrowing influences government bond yields, so perforce  will also impact swap spreads. If borrowing is viewed as in danger of getting out of  control, or the government runs persistent large budge deficits, government bond  yields will rise. All else being equal, this will lead to narrowing swap spreads.

We can see then that a number of factors influence swap spreads. An ALM or Treasury  desk should be aware of these and assess them because the swap rate represents a key  funding and hedging rate for a bank.

\* Moorad Choudhry  is Visiting Professor at the Department of Economics at London  Metropolitan University. This article is an extract from Chapter 7 of his forthcoming  book  Bank Asset and Liability Management  (John Wiley 2007).

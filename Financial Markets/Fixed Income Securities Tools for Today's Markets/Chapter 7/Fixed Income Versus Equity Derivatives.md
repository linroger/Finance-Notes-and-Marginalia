---
tags:
  - black_scholes_merton
  - bond_pricing
  - equity_derivatives
  - fixed_income
  - interest_rates
aliases:
  - BSM Model
  - Bond Option Pricing
  - Fixed Income vs. Equity Derivatives
key_concepts:
  - BSM option pricing
  - Bond price convergence
  - Interest rate volatility
  - Short-term rate modeling
  - Term structure evolution
---

# 7.9 FIXED INCOME VERSUS EQUITY DERIVATIVES  

The famous [Black-Scholes](../../../Financial%20Engineering/Mathematical%20Modeling%20of%20Derivative%20Pricing.md)-[Merton](../../../Credit%20Markets/Credit%20Markets%20Session%205.md) (BSM) [pricing](Arbitrage%20Pricing%20of%20Derivatives.md) analysis of stock options can be summarized as follows. Under the assumptions that the [stock price](../../../Financial%20Engineering/Derivatives/Part%20IV%20-%20Options/Chapter%2016%20-%20Black–Scholes%20Model.md) evolves according to a particular random process and that the [short-term interest rate](../Chapter%209/The%20Gauss%20Model.md) is constant, it is possible to form a [portfolio](../../../Advanced%20Investments/An%20Asset%20Allocation%20Primer.md) of the underlying stock and short-term bonds that replicates the option. Therefore, by [arbitrage arguments](../Chapter%2011/Forward%20Contracts%20and%20Forward%20Prices.md), the price of the option equals the price of the [replicating portfolio](Pricing%20Forwards,%20Futures,%20Bonds,%20Swaps,%20Swaptions,%20Caps%20and%20Floors%20under%20No-Arbitrage%20and%20Risk-Neutral%20Pricing.md).  

Consider applying this logic to price an option on a five-year bond. The.   
starting point might be an assumption about how the price of the five-year.   
bond evolves over time, but the task is considerably more complicated than.   
for the price of a stock. First, the price of a bond converges to its face value.   
at maturity, while the [stock price](../../../Financial%20Engineering/Derivatives/Part%20IV%20-%20Options/Chapter%2016%20-%20Black–Scholes%20Model.md) has no similar constraint. Second, because of the maturity constraint, the volatility of a bond's price must decline as the.  

bond approaches maturity. Hence, the simple assumption that the volatility of a stock is constant is not as appropriate for bonds. Third, because [stock volatility](../../../Financial%20Instruments/Financial%20Derivatives%20and%20Quantitative%20Methods/Option%20Risk.md) is very large relative to short-term rate volatility, it is often acceptable to assume that the [short-term interest rate](../Chapter%209/The%20Gauss%20Model.md) is constant. By contrast, it seems inconsistent to assume that bond prices - which depend on [interest rates](../Chapter%202/Interest%20Rate%20Quotations.md) - follow some random process, while assuming that the [short-term interest rate](../Chapter%209/The%20Gauss%20Model.md) is constant.  

These objections led researchers to make assumptions about the random. evolution of the interest rate rather the bond price. In that way, bond prices naturally approach par, price volatilities naturally approach zero, and no interest rate is assumed to be constant. But this approach raises another set of questions. Which interest rate is assumed to evolve in a particular way? Assumptions about the five-year [spot rate](../../../International%20Finance/The%20Foreign%20Exchange%20Market%20Annotations.md), for example, are not sufficient for two reasons. First, five-year coupon bond prices depend on shorter-term. spot rates as well. Second, an option on a particular five-year bond soon depends on the prices of a bond that is no longer a five-year bond, but a bond with slightly less [time to maturity](../../../Financial%20Instruments/Lecture%20Notes-%20Financial%20Instruments/Teaching%20Note%201-%20Forward%20Rates%20Agreement/Hedging%20Strategies%20with%20Forwards.md). Therefore, assumptions usually have to be made about the evolution of the entire [term structure of interest rates](../../../Financial%20Engineering/6.%20A%20Brief%20Introduction%20to%20Stochastic%20Calculus.md) to price bond options and other [derivatives](../../Financial%20Trading%20and%20Markets/Chapter%209%20Arbitrage%20and%20Hedging%20With%20Options.md). This chapter shows that, in a [one-factor model](Profit%20and%20Loss%20Attribution%20with%20an%20OAS.md), assumptions about the evolution of the short-term rate are sufficient to model the evolution of the entire [term structure](../Chapter%209/The%20Vasicek%20Model.md)..  

In short, there are several arguments to move beyond BSM in the fixed. income context. Nevertheless, for simplicity, practitioners do use versions of BSM to price and hedge several classes of [fixed income derivatives](../../../Financial%20Engineering/6.%20A%20Brief%20Introduction%20to%20Stochastic%20Calculus.md). These. methodologies are described at length in Chapter 16..  

# Expectations, Risk Premium, Convexity, and the Shape of the Term Structure  

tions about the evolution of the short-term rate and by assumptions about the risk premium demanded by investors for bearing [interest rate risk](../../../Fixed%20Income%20Asset%20Pricing/Analysis%20of%20Fixed%20Income%20Securities.md). The first few sections of the chapter present concepts by way of example, in the simple, [binomial tree](Rate%20and%20Price%20Trees.md) framework of the previous chapter. The last section of the chapter presents the same ideas in more general setting, though at the cost of some higher-level mathematics. Chapter 9 concludes the presentation of [term structure models](../../../Financial%20Engineering/Financial%20Mathematics%20Course.md) with a detailed description of two well-known models.  
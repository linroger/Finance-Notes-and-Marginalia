---
title: Fixed Income Engineering
chapter: 14
subject: Financial Engineering
category: Principles of Financial Engineering
tags:
- arbitrage
- credit
- credit-derivatives
- fixed-income
- fixed-income-derivatives
- fx-derivatives
- girsanov-theorem
- hedging-strategies
- interest-rate-derivatives
- ito-calculus
- markets
- martingale-theory
- model-calibration
- monte-carlo-simulation
- numerical-simulation
- option-greeks
- options
- options-pricing
- quantitative-pricing
- risk-management
- stochastic
key_concepts:
- Arbitrage pricing theory (APT)
- Brownian motion and Wiener processes
- Credit risk and default probability
- Delta hedging and Greeks calculation
- Exotic options and path-dependent derivatives
- Expected Shortfall (ES) and coherent risk measures
- Girsanov's theorem and measure changes
- Heath-Jarrow-Morton (HJM) framework
- Interest rate models and term structure
- Interest rate swaps and swap pricing
- Ito's Lemma and stochastic calculus
- Model calibration and parameter estimation
- Monte Carlo simulation for derivatives
- Option Greeks and sensitivity analysis
- Portfolio optimization and mean-variance theory
- Risk-neutral valuation and martingale measures
- Value at Risk (VaR) and risk metrics
- Vasicek and Cox-Ingersoll-Ross models
---


# FIXED INCOME ENGINEERING  

# CHAPTER OUTLINE  

[^14]: 1 Introduction . 460
[^14]: 2 A Framework for Swaps . 461
[^14]: 2.1 Equivalence of Cash Flows . 464
[^14]: 2.2 Pricing the Swap . 464
[^14]: 2.2.1 Interpretation of the swap rate . 466
[^14]: 2.3 Some Applications. 468
[^14]: 2.3.1 Another formula . 469
[^14]: 2.3.2 Marking to market . 470
[^14]: 3 Term Structure Modeling . 471
[^14]: 3.1 Determining the Forward Rates from Swaps . 471
[^14]: 3.2 Determining the $B(t_{0}, t_{i})$ from Forward Rates 472
[^14]: 3.3 Determining the Swap Rate . 472
[^14]: 3.4 Real-World Complications . 472
[^14]: 3.4.1 Remark. 473
[^14]: 4 Term Structure Dynamics. 473
[^14]: 4.1 The Framework. 474
[^14]: 4.2 Normalization and Forward Measure. 475
[^14]: 4.2.1 Risk-neutral measure is inconvenient. 475
[^14]: 4.2.2 The forward measure. 477
[^14]: 4.2.3 Arbitrage-free SDEs for forward rates . 478
[^14]: 4.3 Arbitrage-Free Dynamics . 479
[^14]: 4.3.1 Review . 481
[^14]: 4.4 A Monte Carlo Implementation . 482
[^14]: 5 Measure Change Technology . 483
[^14]: 5.1 The Mechanics of Measure Changes. 485
[^14]: 5.2 Generalization. 487
[^14]: 6 An Application . 488
[^14]: 6.1 Another Example of Measure Change 489
[^14]: 6.2 Pricing CMS. 493
[^14]: 7 In-Arrears Swaps and Convexity . 494
[^14]: 7.1 Valuation . 495
[^14]: 7.2 Special Case . 497
[^14]: 8 Cross-Currency Swaps. 498
[^14]: 8.1 Pricing . 499
[^14]: 8.2 Conventions . 500

[^14]: 9 Differential (Quanto) Swaps 500
[^14]: 9.1 Basis Swaps. 501
[^14]: 10 Conclusions. 501
Suggested Reading . 502   
Exercises . 502   
EXCEL Exercises . 503   
MATLAB Exercise . 505  

# 14.1 INTRODUCTION  

This chapter extends the discussion of swap-type instruments and outlines a simple framework for fixed-income security pricing. Term structure modeling is treated within this framework. The chapter also introduces the recent models that are becoming a benchmark in this sector.  

Until the late 1990s, short-rate modeling was the most common approach in pricing and risk-managing fixed-income securities. The publication in 1992 of the Heath Jarrow Merton (HJM) approach enabled arbitrage-free modeling of multifactor-driven term structure models, but markets continued to use short-rate modeling. A few years ago the situation changed. The Forward LIBOR or Brace Gatarek Musiela (BGM) Model published in 1997 became the market standard for pricing and risk management.  

During the GFC, the LIBOR rate rose significantly and diverged from the overnight indexed swap (OIS) rate raising questions about whether LIBOR is an appropriate riskless discount. In Chapter 24, we will discuss recent models and market developments such as the use of OIS curve as a risk-free curve for discounting. The use of the OIS curve implies that more than one zero curve must be modeled for the purpose of pricing derivatives. The LIBOR curve is used to determine payoffs and the OIS zero curve is used for discounting. This chapter will discuss the Forward LIBOR Model and we will deal with more complex and recent issues such as approaches that simultaneously or separately model the LIBOR and the OIS curve in Chapter 24.  

This chapter will approach the issues from a practical point of view using swap markets and swap derivatives as a background. We are interested in providing a framework for analyzing the mechanics of swaps and swap derivatives, for decomposing them into simpler instruments, and for constructing synthetics. Recent models of fixed-income modeling can then be built on this foundation very naturally.  

It is worth reviewing the basic principles of swap engineering laid out in Chapter 4. First of all, swaps are almost always designed such that their value at initiation is zero. This is a characteristic of modern swap-type "spread instruments," and there is no surprise here. Second, what makes the value of the swap equal to zero is a spread or an interest rate that is chosen with the purpose that the initial value of the swap vanishes. Third, swaps encompass more than one settlement date. This means that whatever the value of the swap rate or swap spread, these will in the end be some sort of "average of shorter term floating rates or spreads." This not only imposes simple arbitrage conditions on relevant market rates but also provides an opportunity to trade the volatility associated with such averages through the use of options on swaps. Since swaps are very liquid, they form an excellent underlying for swaptions. Swaptions, in turn, are related to interest rate volatilities for the underlying subperiods, which will relate to cap/floor volatilities. This structure is conducive to  

![](f5787f5bbf4d20515b24c53782c2e3794a89d88baafb9f68cdfefcc99a607f79.jpg)  

# FIGURE 14.1  

Three-period forward swap.  

designing and understanding more complex swap products such as constant maturity swaps (CMS).   
The CMS is used as an example for showing the advantages of the Forward LIBOR Model.  

Finally, the chapter will further use the developed framework to illustrate the advantages of measure change technology. Switching between various $T_{\delta}$-forward measures, we show how convexity effects can be calculated.  

Most of the discussion will center on a three-period swap first, and then generalize the results. We begin with this simple example, because with a small number of cash flows the analysis becomes more manageable and easier to understand. Next, we lay out a somewhat more technical framework for engineering fixed-income instruments. Eventually, this is developed into the Forward LIBOR Model. Within our framework, measure changes using Girsanov-type transformations emerge as fundamental tools of financial engineering. The chapter discusses how measures can be changed sequentially during a numerical pricing exercise as was done in the simulation of the Forward LIBOR Model. These tools are then applied to CMS, which are difficult to price with traditional models.  

# 14.2 A FRAMEWORK FOR SWAPS  

We work with forward fixed payer interest rate swaps and their "spot" equivalent. These are vanilla products in the sense that contracts are predesigned and homogeneous. They are liquid, the bid-ask spreads are tight, and every market player is familiar with their properties and related conventions.  

To simplify the discussion we work with a three-period forward swap, shown in Figure 14.1. It is worth repeating the relevant parameters again, given the somewhat more technical approach the chapter will adopt.  

[^1]: The notional amount is $N$, and the tenor of the underlying LIBOR rate is $\delta$, which represents a proportion of a calendar year. As usual, if a year is denoted by 1, then $\delta$ will be 1/4 in the case of 3-month LIBOR.
[^2]: The swap maturity is three periods. The swap ends at time $T=t_{4}$. The swap contract is signed at time $t_{0}$ but starts at time $t_{1}$, hence the term forward swap is used.

![](68d1ffe91229593650aa0b9f193d8e73f9ca01f0df8427f52802c386c42ee7bc.jpg)  

# FIGURE 14.2  

Payoff diagrams for three default-free pure discount bonds.  

[^3]: The dates $\{t_{1}, t_{2}, t_{3}\}$ are reset dates where the relevant LIBOR rates $L_{t_{1}}$, $L_{t_{2}}$, and $L_{t_{3}}$ will be determined. These dates are $\delta$ time units apart.
[^4]: The dates $\{t_{2}, t_{3}, t_{4}\}$ are settlement dates where the LIBOR rates $L_{t_{1}}$, $L_{t_{2}}$, and $L_{t_{3}}$ are used to exchange the floating cash flows, $\delta N L_{t_{i}}$ against the fixed $\delta N s_{t_{0}}$ at each $t_{i+1}$. In this setup, the time that passes until the start of the swap, $t_{1}-t_{0}$, need not equal $\delta$. However, it may be notationally convenient to assume that it does.

Our purpose is to provide a systematic framework in which the risk management and pricing of such swaps and the instruments that build on them can be done efficiently. That is, we discuss a technical framework that can be used for running a swap and swap derivatives book.  

Swaps are one major component of a general framework for fixed-income engineering. We need two additional tools. These we introduce using a simple example again. Consider Figure 14.2, where we show payoff diagrams for three default-free pure discount bonds. The current price, $B(t_{0}, T_{i})$, of these bonds is paid at $t_{0}$ to receive 1 dollar in the same currency at maturity dates $T_{i}=t_{i}$. Given that these bonds are default-free, the time $t_{i}$ payoffs are certain and the price $B(t_{0}, T_{i})$ can be considered as the value today of 1 dollar to be received at time $t_{i}$. This means they are, in fact, the relevant discount factors, or in market language, simply discounts for $t_{i}$. Note that as  
$$
T_{1} < T_{2} < T_{3} < T_{4}
$$  

![](631c34fe232dc2cd6cb35bd14b79d6bcfdbb127a84e733bcdd9000834a786049.jpg)  

# FIGURE 14.3  

Three payoff diagrams for FRAs.  

we would expect these bond prices to satisfy  
$$
[^1]: > B(t_{0}, t_{1}) > B(t_{0}, t_{2}) > B(t_{0}, t_{4})
$$  

assuming upward sloping yield curves.  

The second set of tools comes from FRA markets. In Figure 14.3, we display the payoff diagrams of three FRAs—the FRA contracts written at time $t_{0}$ on LIBOR rates, $L_{t_{1}}$, $L_{t_{2}}$, and $L_{t_{3}}$ respectively. These are interest rates that will be observed (reset) at times $t_{1}$, $t_{2}$, and $t_{3}$, respectively, and have tenor $\delta$. To be consistent with the payment and settlement conventions in the FRA markets, we will use the convention that all FRAs here will settle in arrears. For example, the FRA on $L_{t_{1}}$ will settle at time $t_{2}$. In these figures and in those to follow, we assume that the quoted FRA rates for the three contracts are given by  
$$
\{F_{0}^{1}, F_{0}^{2}, F_{0}^{3}\}
$$  

where the subscript denotes the trade date and the superscript denotes the reset date. This way, the FRAs are a natural match for the periods associated with the three-period swap shown in the first figure.  

We have just specified the instruments to be used, namely swaps, bonds, and FRAs, all in the same currency. We will now discuss their joint dynamics. This aspect is more technical, so we simplify the framework by working with a small number of settlement dates in the rest of this book.  

# 14.2.1 EQUIVALENCE OF CASH FLOWS  

According to Chapter 4, the cash flows from swaps should be equivalent to cash flows from properly chosen portfolios of bonds and FRAs. This is easy to see in the deterministic case. In fact, consider the cash flows of the fixed leg in Figure 14.4. These can be replicated exactly by the bond portfolio shown in the second diagram.  

The floating leg cash flows can be replicated by the portfolio  
$$
\{\delta L_{t_{1}}, -\delta L_{t_{2}}, -\delta L_{t_{3}}\}
$$  

Clearly, the same cash flows can be obtained from the FRA portfolios shown in Figure 14.6.  

# 14.2.2 PRICING THE SWAP  

Since the floating payments and the fixed payments at times $t_{2}$, $t_{3}$, and $t_{4}$ are equivalent to carefully chosen portfolios of FRAs and discount bonds, the swap spread can be expressed as a function of the corresponding FRA rates and discount bond prices. We work with the deterministic case first and then generalize to the case of stochastic interest rates.  

If the interest rates are deterministic, then the equivalences mentioned above can be used to determine the arbitrage-free swap rate. We use the standard argument where the value of a forward swap, at the time of initiation, is zero. Then, the discounted floating payments should equal the discounted fixed payments,  
$$
B(t_{0}, t_{2})\delta s_{t_{0}} + B(t_{0}, t_{3})\delta s_{t_{0}} + B(t_{0}, t_{4})\delta s_{t_{0}}
$$  
$$
= B(t_{0}, t_{2})\delta F_{0}^{1} + B(t_{0}, t_{3})\delta F_{0}^{2} + B(t_{0}, t_{4})\delta F_{0}^{3}
$$  

Eliminating the $\delta$ and rearranging, the annualized forward swap rate can be written as  

![](a69e7b8e9fa0a93c4b52b5df16e1e23c6d728f0e119e5c7a4fb3bf88c0ac6f9e.jpg)  

# FIGURE 14.4  

Replicating the fixed leg with bonds.  

![](3788d1ee1f029e963302de47b69c2ce2ff00c67c5c92f7e7b2fb6bbf6e87fe95.jpg)  

# FIGURE 14.5  

Cash flows of the floating leg.  

$$
s_{t_{0}} = \frac{B(t_{0}, t_{2})F_{0}^{1} + B(t_{0}, t_{3})F_{0}^{2} + B(t_{0}, t_{4})F_{0}^{3}}{B(t_{0}, t_{2}) + B(t_{0}, t_{3}) + B(t_{0}, t_{4})}
$$  

Note that the numerator on the right-hand side is a weighted sum of the FRA rates where the discount bonds provide the weights. It is thus shown that the forward payer swap rate is a weighted average of forward rates. In the next section, we show that this result generalizes to the stochastic case.  

![](a0bb86b5b4c1c3b476c0797ac8f37e8f0b3b1fb977dd2b6bbdef86c6dd079bec.jpg)  

# FIGURE 14.6  

Replicating the floating leg cash flows with FRAs.  

# 14.2.2.1 Interpretation of the swap rate  

We move to the stochastic case and characterize the forward swap rate in terms of conditional expectations. Since swaps can be replicated (and hedged) by FRAs and discount bonds, then the discounted values of future cash flows of these synthetics should be the same. Under the risk-neutral measure $P$,  
$$
\sum_{i=1}^{3} E_{t_{0}}^{P}[e^{-r(t_{i+1} - t_{0})}\delta s_{t_{0}}] = \sum_{i=1}^{3} E_{t_{0}}^{P}[e^{-r(t_{i+1} - t_{0})}\delta L_{t_{i}}]
$$  

where $e^{-r(t_{k+1} - t_{0})}$ are the (stochastic) discount factors. Also $r$ is the instantaneous risk-neutral spot rate and, to make the notation simpler, we take all integrals as Riemann integrals. This yields  
$$
s_{t_{0}} = \frac{\sum_{i=1}^{3} E_{t_{0}}^{P}[e^{-\int_{t_{0}}^{t_{i+1}} r(u)du} L_{t_{i}}]}{\sum_{i=1}^{3} E_{t_{0}}^{P}[e^{-\int_{t_{0}}^{t_{i+1}} r(u)du}]}
$$  

To understand the forward swap rate, we need to manipulate this expression. We introduce the $t_{i+1}$ -forward measure denoted by $P^{i+1}$ using the transformation  
$$
\frac{dP^{i+1}}{dP} = \frac{e^{-\int_{t_{0}}^{t_{i+1}} r(u)du}}{B(t_{0}, t_{i+1})}
$$  

With this definition, we can rewrite the term  
$$
E_{t_{0}}^{P}[e^{-\int_{t_{0}}^{t_{i+1}} r(u)du} L_{t_{i}}] = B(t_{0}, t_{i+1})E_{t_{0}}^{P^{i+1}}[L_{t_{i}}]
$$  

where $B(t_{0}, t_{i+1})$ is the time $t_{0}$ price of default-free discount bond that matures at time $t_{i+1}$.  

To motivate the forward measure, it is important to remember that, we know from Chapters 12 and 13, the price of any asset has the martingale property under the appropriate measure once the asset price is normalized by the numeraire associated with that measure. The numeraire in the case of the $P^{i+1}$ forward measure is the bond that matures at time $t_{i+1}$. Since the forward rate at time $t_{i}$ settles and pays at time $t_{i+1}$, we can regard the forward rate as the price of an asset that pays its value at time $t_{i+1}$. The expectation of the forward LIBOR rate $L_{t_{i}}$ under the $P^{i+1}$ forward measure is given by the forward rate that was introduced in Chapter 3:  
$$
E_{t_{0}}^{P^{i+1}}[L_{t_{i}}] = F(t_{0}, t_{i})
$$  

where $F(t_{0}, t_{i})$ is the forward rate as of time $t_{0}$ for a loan that starts at time $t_{i}$ and ends at time $t_{i+1}$. For notational simplicity, we use $F_{0}^{i}$ to denote this forward rate. Thus we have  
$$
s_{t_{0}} = \frac{\sum_{i=1}^{3} B(t_{0}, t_{i+1})F_{0}^{i}}{\sum_{i=1}^{3} B(t_{0}, t_{i+1})}
$$  

which generalizes our earlier result to the case of stochastic interest rates. The forward swap rate is again a weighted average of forward rates.  

To show the advantages of the forward measure, we now assume that the $F_{0}^{i}$ satisfy the following arbitrage-free dynamics  
$$
dF_{t}^{i} = \tilde{\sigma}_i F_{t}^{i} dW_{t}^{i}
$$  

That is, the $F_{t}^{i}$ have zero drift under the $P^{i+1}$-measure. This measure is called the $(t_{i+1})$-forward measure. We denote the forward rate volatility by $\tilde{\sigma}_i$. The $W_{t}^{i}$ is a Wiener process under $P^{i+1}$. Note that because the forward rates have different forward measures, we need different Wiener processes. We will return to this issue later. But this representation is a simplification, since the system has only one factor, whereas actual term structure is driven by a multiplicity of factors.  

Now from Eq. (14.8), using Ito's lemma, we can obtain the dynamics of the forward swap rate,  
$$
ds_{t} = \frac{\sum_{i=1}^{3} B(t, t_{i+1})dF_{t}^{i}}{\sum_{i=1}^{3} B(t, t_{i+1})}
$$  

As expected, the forward swap rate also behaves like a martingale.  

# 14.2.3 SOME APPLICATIONS  

Before deriving the fundamental arbitrage-free dynamics for the Forward LIBOR Model (Chapter 22), we consider two applications that are commonly used by swap traders.  

Arbitrage restrictions between swaps and the underlying interest rates can be exploited by spread traders. For example, if the pricing equation  
$$
s_{t_{0}} = \frac{\sum_{i=1}^{3} B(t_{0}, t_{i+1})F_{0}^{i}}{\sum_{i=1}^{3} B(t_{0}, t_{i+1})}
$$  

does not hold, one can short the expensive portfolio and buy the cheaper one. Such strategies would result in immediate arbitrage gains.  

# 14.2.3.1 Another formula  

Swaps and FRAs are both very liquid instruments. Discount bonds, although liquid, are relatively less so. So when trying to obtain arbitrage between swaps and FRAs, traders may prefer not to utilize discount bonds unless this becomes necessary for hedging the position. We now obtain arbitrage relations that involve only swaps and FRAs, by eliminating discount bonds from the equation. If we believe that the price of discount bonds can be expressed as  
$$
B(t_{0}, t_{i+1}) = e^{-\sum_{j=0}^{i} F_{0}^{j} \delta}
$$  

then we might write the denominator of the swap rate as:  
$$
\sum_{i=1}^{3} B(t_{0}, t_{i+1}) = \sum_{i=1}^{3} e^{-\sum_{j=0}^{i} F_{0}^{j} \delta}
$$  

This would give the swap pricing equations in terms of the FRA rates only:  
$$
s_{t_{0}} = \frac{\sum_{i=1}^{3} F_{0}^{i} e^{-\sum_{j=0}^{i} F_{0}^{j} \delta}}{\sum_{i=1}^{3} e^{-\sum_{j=0}^{i} F_{0}^{j} \delta}}
$$  

# 14.2.3.2 Marking to market  

Suppose a swap is contracted at time $t_{0}$ with swap rate $s_{t_{0}}$. After an infinitesimal time $dt$, the value of this swap will not be zero anymore. The marking-to-market value of the swap is obtained from  
$$
V_{t_{0}+dt} = (s_{t_{0}} - s_{t_{0}+dt}) \sum_{i=1}^{3} B(t_{0}+dt, t_{i+1}) \delta N
$$  

where $s_{t_{0}+dt}$ is the swap rate that prevails at time $t_{0}+dt$ and is, in general, different from $s_{t_{0}}$.  

These formulas yield the sensitivity of a swap contract with respect to changes in the forward rates. For the case of a forward starting three-period swap, we have, from the formula in Eq. (14.8),  
$$
ds_{t} = \sum_{i=1}^{3} \frac{B(t, t_{i+1})}{\sum_{j=1}^{3} B(t, t_{j+1})} dF_{t}^{i}
$$  

# 14.3 TERM STRUCTURE MODELING  

This section will briefly review some basic relationships between key concepts in term structure modeling. Our purpose is both to introduce the notation and to take another look at the analytics. We continue to work with the same three-period example. The key relationships are:  

# 14.3.1 DETERMINING THE FORWARD RATES FROM SWAPS  

The formula  
$$
s_n = \frac{\sum_{i=1}^{n} B(t_{0}, t_{i}) F(t_{0}, t_{i-1})}{B(t_{0}, t_{n})}
$$  

represents a system of equations where the unknowns are the forward rates  
$$
\{F(t_{0}, t_{0}), F(t_{0}, t_{1}), \ldots, F(t_{0}, t_{n-1})\}
$$  

and the inputs are the n observed par swap rates  
$$
\{s_1, s_2, \ldots, s_n\}
$$  

for swaps with increasing maturities. We can solve for the forward rates recursively. The one-period par swap rate is the same as the forward rate  
$$
s_1 = F(t_{0}, t_{0})
$$  

We know from the par swap rate formula that  
$$
s_2 = \frac{B(t_{0}, t_{1}) F(t_{0}, t_{0}) + B(t_{0}, t_{2}) F(t_{0}, t_{1})}{B(t_{0}, t_{1}) + B(t_{0}, t_{2})}
$$  

From the relationship between discount bonds and forward rates:  
$$
B(t_{0}, t_{2}) = B(t_{0}, t_{1}) \times \frac{1}{1 + \delta F(t_{0}, t_{1})}
$$  

Substituting and solving for $F(t_{0}, t_{1})$:  
$$
F(t_{0}, t_{1}) = \frac{s_2 (1 + \delta F(t_{0}, t_{0})) - F(t_{0}, t_{0})}{1 + \delta F(t_{0}, t_{0}) - \delta s_2}
$$  

This process can be continued recursively to obtain all forward rates from the par swap curve. This process is known as bootstrapping.  

# 14.3.2 DETERMINING THE $B(t_{0}, t_{i})$ FROM FORWARD RATES  

Given a sequence of forward rates, we can determine the discount bond prices using:  
$$
B(t_{0}, t_{i}) = \prod_{j=0}^{i-1} \frac{1}{1 + \delta F(t_{0}, t_{j})}
$$  

This formula follows from the fact that investing \$1 at time $t_{0}$ and rolling over at the forward rates should yield the same result as buying a zero-coupon bond.  

# 14.3.3 DETERMINING THE SWAP RATE  

Given forward rates and discount bond prices, the swap rate is determined by:  
$$
s_{t_{0}} = \frac{\sum_{i=1}^{n} B(t_{0}, t_{i}) F(t_{0}, t_{i-1})}{\sum_{i=1}^{n} B(t_{0}, t_{i})}
$$  

This completes the circle of relationships between swap rates, forward rates, and discount bonds.  

# 14.3.4 REAL-WORLD COMPLICATIONS  

In practice, several complications arise:  

[^1]: **Day count conventions**: Different markets use different conventions (ACT/360, 30/360, etc.)
[^2]: **Business day adjustments**: Payment dates may be adjusted for holidays
[^3]: **Interpolation**: Observed swap rates may not be available for all maturities needed
[^4]: **Bid-ask spreads**: Market quotes have transaction costs
[^5]: **Basis spreads**: Different floating rate indices may have spreads between them

# 14.3.4.1 Remark  

The relationships discussed above assume perfect markets with no arbitrage. In reality, small arbitrage opportunities may exist due to:  
- Transaction costs  
- Funding constraints  
- Regulatory requirements  
- Market segmentation  

However, these relationships provide the fundamental framework for pricing and risk management in interest rate markets.  

# 14.4 TERM STRUCTURE DYNAMICS  

This section develops the dynamics of the term structure in continuous time. We model the evolution of forward rates and derive the conditions for absence of arbitrage. This leads naturally to the Forward LIBOR Model.  

# 14.4.1 THE FRAMEWORK  

We work in continuous time with a finite horizon $T^*$. Consider a family of forward rates:  
$$
\{F(t, T): 0 \leq t \leq T \leq T^*\}
$$  

where $F(t, T)$ is the forward rate at time $t$ for instantaneous borrowing at time $T$.  

The dynamics of these forward rates under the physical measure $P$ can be written as:  
$$
dF(t, T) = \mu(t, T, F) dt + \sigma(t, T, F) dW_t
$$  

where:  
- $\mu(t, T, F)$ is the drift  
- $\sigma(t, T, F)$ is the volatility  
- $W_t$ is a Brownian motion under $P$  

The key insight is that not all choices of $\mu$ and $\sigma$ are consistent with no-arbitrage. The HJM framework provides the necessary restrictions.  

# 14.4.2 NORMALIZATION AND FORWARD MEASURE  

To price derivatives, we need to work with martingale measures. The choice of numeraire determines the appropriate measure.  

# 14.4.2.1 Risk-neutral measure is inconvenient  

Under the risk-neutral measure $Q$, asset prices discounted by the money market account are martingales. The money market account evolves as:  
$$
dB_t = r_t B_t dt
$$  

where $r_t$ is the short rate.  

However, working with the risk-neutral measure for interest rate derivatives has several disadvantages:  
[^1]: The short rate $r_t$ is not directly observable
[^2]: Complex drift adjustments are needed for forward rates
[^3]: Calibration to market prices is difficult

# 14.4.2.2 The forward measure  

A more convenient approach is to use forward measures. For each maturity $T$, define the $T$-forward measure $Q^T$ with the $T$-maturity bond as numeraire.  

Under $Q^T$:  
- The forward rate $F(t, T)$ is a martingale  
- No drift adjustment is needed for $F(t, T)$  
- Calibration is straightforward  

The change of measure from $Q$ to $Q^T$ is given by:  
$$
\frac{dQ^T}{dQ} = \frac{B(T, T)/B_T}{B(0, T)/B_0} = \frac{1}{B(0, T)B_T}
$$  

# 14.4.2.3 Arbitrage-free SDEs for forward rates  

Under the $T$-forward measure $Q^T$, the forward rate $F(t, T)$ follows:  
$$
dF(t, T) = \sigma(t, T) F(t, T) dW_t^T
$$  

where $W_t^T$ is a Brownian motion under $Q^T$.  

For another forward rate $F(t, S)$ with $S \neq T$, the dynamics under $Q^T$ include a drift adjustment:  
$$
dF(t, S) = \sigma(t, S) F(t, S)[\rho(T, S)\sigma(t, T) \tau(T, S) dt + dW_t^S]
$$  

where:  
- $\rho(T, S)$ is the correlation between $W_t^T$ and $W_t^S$  
- $\tau(T, S) = S - T$ when $S > T$  

# 14.4.3 ARBITRAGE-FREE DYNAMICS  

The general form of arbitrage-free dynamics for forward LIBOR rates is:  
$$
dF_i(t) = F_i(t) \sum_{j=i+1}^{n} \frac{\rho_{ij} \sigma_i(t) \sigma_j(t) \delta F_j(t)}{1 + \delta F_j(t)} dt + F_i(t) \sigma_i(t) dW_i^{T_{i+1}}(t)
$$  

This is the fundamental equation of the LIBOR Market Model (LMM).  

Key features:  
[^1]: Each forward rate has its own volatility function $\sigma_i(t)$
[^2]: Correlations $\rho_{ij}$ between different forward rates
[^3]: Drift terms ensure no arbitrage
[^4]: Under its own forward measure, each forward rate is driftless

# 14.4.3.1 Review  

The Forward LIBOR Model has several advantages:  
[^1]: **Market observability**: Forward rates are directly observable
[^2]: **Calibration**: Easy to calibrate to cap/floor prices
[^3]: **Flexibility**: Can incorporate volatility smiles
[^4]: **Consistency**: Ensures arbitrage-free dynamics

However, it also has limitations:  
[^1]: **Computational intensity**: Monte Carlo simulation is often required
[^2]: **High dimensionality**: Many factors needed for realistic modeling
[^3]: **Correlation specification**: Difficult to estimate correlations accurately

# 14.4.4 A MONTE CARLO IMPLEMENTATION  

To price derivatives using the Forward LIBOR Model:  

[^1]: **Discretize time**: Choose time steps $\Delta t$
[^2]: **Initialize**: Set initial forward rates from market data
[^3]: **Simulate paths**:
   ```
   For each path:
     For each time step:
       For each forward rate:
         Calculate drift using other forward rates
         Generate random shock
         Update forward rate
   ```
[^4]: **Calculate payoffs**: Evaluate derivative payoff on each path
[^5]: **Discount**: Discount payoffs to present value
[^6]: **Average**: Take average across all paths

The key challenge is calculating the drift terms efficiently, as they depend on all forward rates with longer maturities.  

# 14.5 MEASURE CHANGE TECHNOLOGY  

Measure changes are fundamental tools in derivatives pricing. This section explores the mechanics and applications of changing between different forward measures.  

# 14.5.1 THE MECHANICS OF MEASURE CHANGES  

Consider changing from the $T_1$-forward measure to the $T_2$-forward measure. The Radon-Nikodym derivative is:  
$$
\frac{dQ^{T_2}}{dQ^{T_1}} = \frac{B(t, T_2)/B(T_2, T_2)}{B(t, T_1)/B(T_1, T_1)} \times \frac{B(0, T_1)}{B(0, T_2)}
$$  

This simplifies to:  
$$
\frac{dQ^{T_2}}{dQ^{T_1}} = \frac{B(t, T_2)}{B(t, T_1)} \times \frac{B(0, T_1)}{B(0, T_2)}
$$  

Using Girsanov's theorem, the Brownian motion changes as:  
$$
dW_t^{T_2} = dW_t^{T_1} - \lambda_t dt
$$  

where $\lambda_t$ is the market price of risk for the measure change.  

For forward rates, this implies:  
$$
dF(t, S) = \sigma_S F(t, S)[\mu_S^{T_1} dt + dW_t^{T_1}]
$$  
$$
dF(t, S) = \sigma_S F(t, S)[\mu_S^{T_2} dt + dW_t^{T_2}]
$$  

where $\mu_S^{T_2} = \mu_S^{T_1} + \sigma_S \lambda_t$.  

# 14.5.2 GENERALIZATION  

The general framework for measure changes involves:  

[^1]: **Numeraire choice**: Select appropriate numeraire for the problem
[^2]: **Radon-Nikodym derivative**: Calculate the change of measure
[^3]: **Drift adjustment**: Apply Girsanov's theorem
[^4]: **Correlation structure**: Maintain consistency across measures

Important special cases:  
- **Spot measure**: Numeraire is money market account  
- **Terminal measure**: Numeraire is bond maturing at option expiry  
- **Swap measure**: Numeraire is annuity (sum of bonds)  

# 14.6 AN APPLICATION  

We apply measure change technology to price constant maturity swaps (CMS).  

# 14.6.1 ANOTHER EXAMPLE OF MEASURE CHANGE  

Consider a CMS where the floating leg pays the $n$-year swap rate every period. The payoff at time $T_i$ is:  
$$
\text{CMS payoff} = \delta \times s_n(T_i) \times N
$$  

where $s_n(T_i)$ is the $n$-year swap rate at time $T_i$.  

To price this, we need to calculate:  
$$
E^{Q^{T_i}}[s_n(T_i)]
$$  

However, the natural measure for swap rates is the swap measure, not the forward measure. We need to change measures.  

Under the swap measure $Q^S$, the swap rate is a martingale:  
$$
ds_n(t) = \sigma_s s_n(t) dW_t^S
$$  

To change from $Q^{T_i}$ to $Q^S$:  
$$
E^{Q^{T_i}}[s_n(T_i)] = E^{Q^S}[s_n(T_i) \times \frac{dQ^{T_i}}{dQ^S}]
$$  

The Radon-Nikodym derivative involves the ratio of numeraires:  
$$
\frac{dQ^{T_i}}{dQ^S} = \frac{B(T_i, T_i)}{A(T_i)} \times \frac{A(0)}{B(0, T_i)}
$$  

where $A(t) = \sum_{j=1}^n \delta B(t, T_j)$ is the swap annuity.  

# 14.6.2 PRICING CMS  

The key insight is that the adjustment involves the covariance between the swap rate and the annuity:  
$$
E^{Q^{T_i}}[s_n(T_i)] = s_n(0) + \text{convexity adjustment}
$$  

The convexity adjustment is approximately:  
$$
\text{CA} \approx s_n(0) \times \rho_{s,A} \times \sigma_s \times \sigma_A \times T_i
$$  

where:  
- $\rho_{s,A}$ is the correlation between swap rate and annuity  
- $\sigma_s$ is the swap rate volatility  
- $\sigma_A$ is the annuity volatility  

This adjustment is always positive, reflecting the convexity of the swap rate.  

# 14.7 IN-ARREARS SWAPS AND CONVEXITY  

An in-arrears swap is one where the floating rate is paid at the same time it is set, rather than at the end of the period. This creates a convexity effect.  

# 14.7.1 VALUATION  

Consider a floating payment at time $T_i$ of:  
$$
\text{In-arrears payment} = \delta \times L(T_i, T_i) \times N
$$  

where $L(T_i, T_i)$ is the LIBOR rate set and paid at time $T_i$.  

This differs from a standard payment:  
$$
\text{Standard payment} = \delta \times L(T_{i-1}, T_i) \times N
$$  

paid at time $T_i$ but set at time $T_{i-1}$.  

To value the in-arrears payment, we need:  
$$
E^{Q^{T_i}}[L(T_i, T_i)]
$$  

But the natural measure for $L(T_i, T_i)$ is $Q^{T_{i+1}}$, not $Q^{T_i}$.  

# 14.7.2 SPECIAL CASE  

For a single-period rate, the convexity adjustment is:  
$$
E^{Q^{T_i}}[L(T_i, T_i)] = F(0, T_i) \times (1 + \text{CA})
$$  

where:  
$$
\text{CA} \approx \frac{\sigma[^2] \delta T_i}{1 + \delta F(0, T_i)}
$$  

This adjustment compensates for the timing difference and is always positive.  

# 14.8 CROSS-CURRENCY SWAPS  

Cross-currency swaps involve exchanging cash flows in different currencies. They combine interest rate risk with foreign exchange risk.  

# 14.8.1 PRICING  

A typical cross-currency swap involves:  
[^1]: Exchange of notionals at inception
[^2]: Exchange of interest payments during the life
[^3]: Re-exchange of notionals at maturity

Consider a swap receiving USD LIBOR and paying EUR LIBOR:  
- USD leg: $L_{USD}(t) \times N_{USD}$  
- EUR leg: $L_{EUR}(t) \times N_{EUR}$  

At inception: $N_{USD} = S(0) \times N_{EUR}$  

where $S(t)$ is the USD/EUR exchange rate.  

The value in USD is:  
$$
V_{USD}(t) = \sum_{i} B_{USD}(t, T_i) \times \delta \times L_{USD}(t_{i-1}) \times N_{USD}
$$  
$$
- S(t) \times \sum_{i} B_{EUR}(t, T_i) \times \delta \times L_{EUR}(t_{i-1}) \times N_{EUR}
$$  

# 14.8.2 CONVENTIONS  

Market conventions for cross-currency swaps include:  
[^1]: **Notional reset**: Notionals may be reset periodically
[^2]: **Basis spreads**: Additional spreads on one or both legs
[^3]: **Initial exchange**: May or may not exchange notionals at start
[^4]: **Final exchange**: Always exchange notionals at maturity

# 14.9 DIFFERENTIAL (QUANTO) SWAPS  

A quanto swap pays the difference between interest rates in two currencies, but all payments are in a single currency.  

Example: Pay USD LIBOR, receive EUR LIBOR, all payments in USD:  
$$
\text{Quanto payment} = \delta \times (L_{EUR}(t) - L_{USD}(t)) \times N_{USD}
$$  

The key feature is that the EUR rate is "quantoed" into USD.  

To price this, we need:  
$$
E^{Q_{USD}}[L_{EUR}(t)]
$$  

This involves the correlation between EUR rates and the USD/EUR exchange rate:  
$$
E^{Q_{USD}}[L_{EUR}(t)] = F_{EUR}(0, t) - \rho \times \sigma_{EUR} \times \sigma_{FX} \times t
$$  

where:  
- $\rho$ is the correlation between EUR rates and exchange rate  
- $\sigma_{EUR}$ is the EUR rate volatility  
- $\sigma_{FX}$ is the exchange rate volatility  

# 14.9.1 BASIS SWAPS  

A basis swap exchanges two floating rates in the same currency:  
$$
\text{Basis payment} = \delta \times (L_1(t) - L_2(t) + s) \times N
$$  

where $s$ is the basis spread.  

Common examples:  
- LIBOR vs. OIS  
- 3M LIBOR vs. 6M LIBOR  
- LIBOR vs. Prime  

The basis spread $s$ is determined by:  
[^1]: Credit risk differences
[^2]: Liquidity differences
[^3]: Supply and demand

# 14.10 CONCLUSIONS  

This chapter has developed a framework for fixed income derivatives based on:  
[^1]: Forward rates as fundamental building blocks
[^2]: Forward measures for convenient pricing
[^3]: Measure change technology for complex products

Key insights include:  
- Swap rates are weighted averages of forward rates  
- Each forward rate is a martingale under its own measure  
- Convexity adjustments arise from timing mismatches  
- Complex products require careful measure changes  

The Forward LIBOR Model provides a consistent framework for:  
- Pricing vanilla and exotic interest rate derivatives  
- Calibrating to market prices  
- Managing interest rate risk  

Future developments in this area include:  
- Multi-curve frameworks (Chapter 24)  
- Stochastic volatility extensions  
- Credit-adjusted valuations  

# SUGGESTED READING  

• Brigo, D., & Mercurio, F. (2006). *Interest Rate Models - Theory and Practice*. Springer.  
  Comprehensive treatment of interest rate modeling including the LIBOR Market Model.  

• Musiela, M., & Rutkowski, M. (2005). *Martingale Methods in Financial Modelling*. Springer.  
  Advanced mathematical treatment of arbitrage theory and term structure models.  

• Andersen, L., & Piterbarg, V. (2010). *Interest Rate Modeling*. Atlantic Financial Press.  
  Three-volume practitioner-oriented treatment of modern interest rate derivatives.  

• Hunt, P. J., & Kennedy, J. E. (2004). *Financial Derivatives in Theory and Practice*. Wiley.  
  Clear exposition of measure changes and the LIBOR Market Model.  

• Rebonato, R. (2002). *Modern Pricing of Interest-Rate Derivatives*. Princeton University Press.  
  Practical approach to implementing and calibrating the LIBOR Market Model.  

# EXERCISES  

[^1]: Consider a two-period swap with annual payments. If the one-year forward rate is 3% and the two-year forward rate is 3.5%, calculate the par swap rate.

[^2]: Show that under the forward measure $Q^T$, the forward rate $F(t, T)$ is a martingale.

[^3]: Derive the convexity adjustment for a CMS caplet that pays $\max(s_n(T) - K, 0)$ at time $T$.

[^4]: Calculate the value of an in-arrears swap where LIBOR is set and paid at the same time. Assume:
   - Forward rate: 4%  
   - Volatility: 20%  
   - Time to payment: 1 year  
   - Day count: 0.25  

[^5]: Explain why the convexity adjustment for CMS is always positive.

[^6]: Consider a quanto swap paying EUR LIBOR in USD. If the correlation between EUR rates and USD/EUR exchange rate is -0.3, is the quanto adjustment positive or negative? Explain.

[^7]: Derive the drift adjustment when changing from the $T_1$-forward measure to the $T_2$-forward measure for a forward rate $F(t, S)$ where $T_1 < S < T_2$.

[^8]: A 5-year annual swap has a par rate of 4%. If the 5-year discount factor is 0.8227, calculate the annuity factor (sum of discount factors).

[^9]: Explain the advantages of using forward measures instead of the risk-neutral measure for pricing interest rate derivatives.

[^10]: Consider a cross-currency swap exchanging USD fixed for EUR floating. What risks need to be considered in pricing this swap?

# EXCEL EXERCISES  

[^1]: Build a spreadsheet to bootstrap forward rates from par swap rates for maturities 1-10 years.

[^2]: Implement a Monte Carlo simulation for the one-factor LIBOR Market Model:
   a) Simulate 5 forward rates  
   b) Price a cap on 3M LIBOR  
   c) Calculate the standard error  

[^3]: Create a convexity adjustment calculator for:
   a) CMS rates  
   b) In-arrears swaps  
   Show how the adjustment varies with volatility and time.  

[^4]: Build a cross-currency swap pricer that handles:
   a) Exchange of notionals  
   b) Interest payments in two currencies  
   c) FX risk  

[^5]: Implement a measure change calculator showing:
   a) Radon-Nikodym derivatives  
   b) Drift adjustments  
   c) Impact on forward rates  

# MATLAB EXERCISE  

Implement a full LIBOR Market Model simulation:  
[^1]: Generate correlated forward rate paths
[^2]: Price various derivatives:
   - Caps and floors  
   - Swaptions  
   - CMS products  
[^3]: Calculate sensitivities (Greeks)
[^4]: Analyze the impact of correlation assumptions

Your code should:  
- Handle arbitrary numbers of forward rates  
- Allow flexible correlation structures  
- Implement efficient drift calculations  
- Provide visualization of results

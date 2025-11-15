---
title: Tools for Volatility Engineering, Volatility Swaps, and Volatility Trading
chapter: 15
subject: Financial Engineering
category: Principles of Financial Engineering
tags:
- arbitrage
- black-scholes-model
- equity-derivatives
- fixed-income
- fixed-income-derivatives
- hedging-strategies
- interest-rate-derivatives
- markets
- option-greeks
- options
- options-pricing
- risk-management
key_concepts:
- Arbitrage pricing theory (APT)
- Black-Scholes option pricing model
- Delta hedging and Greeks calculation
- Expected Shortfall (ES) and coherent risk measures
- Heath-Jarrow-Morton (HJM) framework
- Implied volatility and volatility surface
- Interest rate models and term structure
- Interest rate swaps and swap pricing
- Option Greeks and sensitivity analysis
- Portfolio optimization and mean-variance theory
- Value at Risk (VaR) and risk metrics
---


# TOOLS FOR VOLATILITY ENGINEERING, VOLATILITY SWAPS, AND VOLATILITY TRADING  

# 15  

# CHAPTER OUTLINE  

[^15]: 1. Introduction 508
[^15]: 2. Volatility Positions 509
[^15]: 2.1. Trading Volatility Term Structure 509
[^15]: 2.2. Trading Volatility Across Instruments 510
[^15]: 3. Invariance of Volatility Payoffs 510
[^15]: 3.1. Imperfect Volatility Positions 511
[^15]: 3.1.1. A dynamic volatility position 512
[^15]: 3.2. Volatility Hedging 516
[^15]: 3.3. A Static Volatility Position 516
[^15]: 4. Pure Volatility Positions 518
[^15]: 4.1. Practical Issues 521
[^15]: 4.1.1. The smile effect 521
[^15]: 4.1.2. Liquidity problems 522
[^15]: 5. Variance Swaps 522
[^15]: 5.1. Uses and Users of Variance Swaps 522
[^15]: 5.1.1. Uses of variance swaps 522
[^15]: 5.1.2. Market participants with an implicit volatility exposure to hedge 523
[^15]: 5.2. A Framework for Variance Swaps 523
[^15]: 5.2.1. Real-world example of a variance swap 524
[^15]: 5.2.2. Real-world conventions 527
[^15]: 5.2.3. Floating leg 527
[^15]: 5.2.4. Determining the fixed variance 528
[^15]: 5.3. A Replicating Portfolio 529
[^15]: 5.4. The Hedge 530
[^15]: 6. Real-World Example of Variance Contract 531
[^15]: 7. Volatility and Variance Swaps Before and After the GFC—The Role
      of Convexity Adjustments? 531   
[^15]: 7.1. The Difficulty of Hedging Variance Swaps in Practice 531
[^15]: 7.2. Convexity and the Difference Between Variance and Volatility Swaps 533
[^15]: 7.2.1. Source of the convexity adjustment 533
[^15]: 7.2.2. The role of convexity in the volatility trading market
                  during the GFC 535   
[^15]: 7.3. Introduction to Volatility as an Asset Class 535
[^15]: 7.4. Post-GFC Regulation, Standardization and Exchange Traded
            Volatility Products 536   
[^15]: 7.4.1. Variance futures 536
[^15]: 7.4.2. Variance swaps 538
[^15]: 7.5. The Hedge 539
[^15]: 8. Which Volatility? 539
[^15]: 9. Conclusions 541
Suggested Reading 542   
Exercises 542   
MATLAB Exercises 543  

# 15.1 INTRODUCTION  

Liquid instruments that involve pure volatility trades are potentially very useful for market participants who have natural exposure to various volatilities in their balance sheet or trading book. The classical option strategies discussed in Chapter 11 have serious drawbacks in this respect. When a trader takes a position or hedges a risk, he or she expects that the random movements of the underlying would have a known effect on the position. The underlying may be random, but the payoff function of a well-defined contract or a position has to be known. Payoff functions of most classical volatility strategies are not invariant to underlying risks, and most volatility instruments turn out to be imperfect tools for isolating this risk. Even when traders' anticipations come true, the trader may realize that the underlying volatility payoff functions have changed due to movements in other variables. Hence, classical volatility strategies cannot provide satisfactory hedges for volatility exposures. The reason for this and possible solutions are the topics of this chapter.  

Traditional volatility trades used to involve buying and selling portfolios of call and put options, straddles or strangles, and then possibly delta-hedging these positions. But such volatility positions were not pure and this led to a search for volatility tools whose payoff function would depend on the volatility risk only. This chapter examines two of the pure volatility instruments that were developed—variance and volatility swaps. Volatility swaps are forward contracts on future realized (stock) volatility. Variance contracts are similar contracts on variance, the square of future volatility. Variance and volatility swaps are interesting for at least two reasons: First, volatility is an important risk for market practitioners, and ways of hedging and pricing such risks have to be understood. Second, the discussion of volatility swaps constitutes a good example of the basic principles that need to be followed when devising new instruments.  

The chapter uses variance swaps instead of volatility swaps to conduct the discussion. Although markets in general use the term volatility, it is more appropriate to think in terms of variance, the square of volatility. Variance is the second centered moment of a random variable, and it falls more naturally from the formulas used in this chapter. For example, volatility (i.e., standard deviation) instruments require convexity adjustments, whereas variance instruments in general do not. Thus, when we talk about vega, for example, we refer to variance vega. This is the sensitivity of the option's price with respect to $\sigma^{2}$ , not $\sigma$ . In fact, in the heuristic discussion in this chapter, at times the term volatility and variance are used interchangeably.  

# 15.2 VOLATILITY POSITIONS  

Volatility positions can be taken with the purpose of hedging a volatility exposure or speculating on the future behavior of volatility. These positions require instruments that isolate volatility risk as well as possible. To motivate the upcoming discussion, we introduce two examples that illustrate traditional volatility positions.  

# 15.2.1 TRADING VOLATILITY TERM STRUCTURE  

We have seen several examples for strategies associated with shifts in the interest rate term structure. They were called curve steepening or curve flattening trades. It is clear that similar positions can be taken with respect to volatility term structures as well. Volatilities traded in markets come with different maturities. As with the interest rate term structure, we can buy one "maturity" and sell another "maturity," as the following example shows.  

# EXAMPLE  

[A] dealer said he was considering selling short-dated 25-delta euro puts/dollar calls and buying a longer-dated straddle. A three-month straddle financed by the sale of two 25-delta one-month puts would have cost $3.9\%$ in premium yesterday.  

These volatility plays are attractive because the short-dated volatility is sold for more than the cost of the longer-maturity options.  

In this particular example, the anticipations of traders concern not the level of an asset price or return, but, instead, the volatility associated with the price. Volatility over one interval is bought using the funds generated by selling the volatility over a different interval.  

Apparently, the traders think that short-dated euro volatility will fall relative to the long-dated euro volatility. The question is to what extent the positions taken will meet the traders' needs, even when their anticipations are borne out. We will see that the payoff function of this position is not invariant to changes in the underlying euro/dollar exchange rate.  

# 15.2.2 TRADING VOLATILITY ACROSS INSTRUMENTS  

Our second example is from the interest rate sector and involves another "arbitrage" position on volatility. The trader buys the volatility of one risk and sells a related volatility on a different risk. This time, the volatilities in question do not belong to different time periods, but instead are generated by different instruments.  

# EXAMPLE  

Dealers are looking at the spreads between euro cap-floor straddle and swaption straddle volatility to take advantage of a $5\%$ volatility difference in the 7-year area. Proprietary traders are selling a two-year cap-floor straddle starting in six years with vols close to $15\%$ . The trade offers a good pick-up over the five-year swaption straddle with volatility $10\%$ . This compares with a historical spread closer to $2\%$ .  

Cap-floors and swaptions are instruments on interest rates. There are both similarities and differences between them. We will study them in more detail in the next chapter. Selling a cap-floor straddle will basically be short interest rate volatility. In the example, the traders were able to take this position at $15\%$ volatility. On the other hand, buying a swaption amounts to a long position on volatility. This was done at $10\%$ , which gives a volatility spread of about $5\%$ . The example states that the latter number has historically been around $2\%$ . Hence, by selling the spread the traders would benefit from a future narrowing of differences between the volatilities of the two instruments.  

This position's payoff is not invariant to interest rate trajectories. Even when volatilities behave as anticipated, the path followed by the level of interest rates may result in unexpected volatility.2 The following discussion intends to clarify why such positions on volatility have serious weaknesses and require meticulous risk management. We will consider pure volatility positions later.  

# 15.3 INVARIANCE OF VOLATILITY PAYOFFS  

In previous chapters, convexity was used to isolate volatility as a risk. In Chapters 9 and 10, we showed how to convert the volatility of an underlying into "cash," and with that took the first steps toward volatility engineering.  

Using the methods discussed in Chapters 9 and 10, a trader can hedge and risk-manage exposures with respect to volatility movements. Yet, these are positions influenced by variables other than volatility. Consider a speculative position taken by an investor.  

Let $S_{t}$ be a risk factor and suppose an investor buys $S_{t}$ volatility at time $t_{0}$ for a future period denoted by $[t_{1},T]$ , $T$ being the expiration of the contract. As in every long position, this means that the investor is anticipating an increase in realized volatility during this period. If realized volatility during $[t_{1},T]$ exceeds the volatility "purchased" at time $t_{0}$ , the investor will benefit. Thus far this is not very different from other long positions. For example, a trader buys a stock and benefits if the stock price goes up. He or she can buy a fixed receiver swap and benefit if the swap value goes up (the swap rate goes down). Similarly, in our present case, we receive a "fixed" volatility and benefit if the actual volatility exceeds this level.  

By buying call or put options, straddles, or strangles, and then delta-hedging these positions, the trader will, in general, end up with a long position that benefits if the realized volatility increases, as was shown in Chapters 9 and 10. Yet, there is one major difference between such volatility positions and positions taken on other instruments such as stocks, swaps, forward rate agreements (FRAs), and so on. Consider Figure 15.1a, that shows a long position on a stock funded by a money market loan. As the stock price increases, the position benefits by the amount $S_{t_{1}}-S_{t_{0}}$ . This potential payoff is known and depends only on the level of $S_{t_{1}}$ . In fact, it depends on $S_{t}$ linearly. In Figure 15.1b, we have a short-dated discount bond position. As the yield decreases, the position gains. Again, we know how much the position will be making or losing, depending on the movements in the yield, $y_{t},$ if convexity gains are negligible.  

A volatility position taken via, say, straddles, is fundamentally different from this as the payoff diagram will move depending on the path followed by variables other than volatility. For example, a change in (i) interest rates, (ii) the underlying asset price, or (iii) the level of implied volatility may lead to different payoffs at the same realized volatility level.  

Variance (volatility) swaps, on the other hand, are pure volatility positions. Potential gains or losses in positions taken with these instruments depend only on what happens to realized volatility until expiration. This chapter shows how volatility engineering can be used to set up such contracts and to study their pricing and hedging. We begin with imperfect volatility positions.  

# 15.3.1 IMPERFECT VOLATILITY POSITIONS  

In financial markets, a volatility position is often interpreted to be a static position taken by buying and selling straddles, or a dynamically maintained position that uses straddles or options. As  

![](6e704bf35253e115191ea65764511918cae0dcf045af8cf407ef2a615b0925e5.jpg)  

# FIGURE 15.1  

Long position on a stock (funded by a money market loan) and long discount bond position.  

mentioned previously, these volatility positions are not the right way to price, hedge, or riskmanage volatility exposure. In this section, we go into the reasons for this. We consider a simple position that consists of a dynamically hedged single-call option.  

# 15.3.1.1 A dynamic volatility position  

Consider a volatility exposure taken through a dynamically maintained position using a plain vanilla call. To simplify the exposition, we impose the assumptions of the Black Scholes world where there are no dividends; the interest rate, $r_{\mathrm{:}}$ , and implied volatility, $\sigma$ , are constant; there are no transaction costs; and the underlying asset follows a geometric process. Then the arbitrage-free value of a European call $C(S_{t},t)$ will be given by the Black Scholes formula3:  
$$
C(S_{t},t)=S_{t}\int_{-\infty}^{d_{1}}\frac{1}{\sqrt{2\pi}}e^{-\frac{1}{2}x^{2}}\mathrm{d}x-e^{-r(T-t)}K\int_{-\infty}^{d_{2}}\frac{1}{\sqrt{2\pi}}e^{-\frac{1}{2}x^{2}}\mathrm{d}x
$$  

where $S_{t}$ is the spot price, and $K$ is the strike. The $d_{i},i=1,2$ , are given by  
$$
d_{i}=\frac{\log(S_{t}/K)\pm(1/2)\sigma^{2}(T-t)+r(T-t)}{\sigma\sqrt{T-t}}
$$  

For simplicity, and without loss of generality, we let  
$$
r=0
$$  

This simplifies some expressions and makes the discussion easier to follow.4  

Now consider the following simple experiment. A trader uses the Black Scholes setting to take a dynamically hedged long position on implied volatility. Implied volatility goes up. Suppose the trader tracks the gains and losses of the position using the corresponding variance-vega. What would be this trader's possible gains in the following specific case? Consider the following simple setup.  

[^1]: The parameters of the position are as follows:
$$
K=S_{t_{0}}=100
$$  
$$
\sigma=20\%
$$  

Initially we let $t_{0}=0$ .  

[^2]: The trader expects an increase in the implied volatility from $20\%$ to $30\%$ , and considers taking a long volatility position.
[^3]: To buy into a volatility position, the trader borrows an amount equal to $100\:C\left(S_{t},\:t\right)$ , and buys 100 calls at time $t_{0}$ with funding cost $r=0$ .5
[^4]: Next, the position is delta-hedged by short-selling $C_{s}$ units of the underlying per call to obtain the familiar exposure shown in Figure 15.2.

![](5fe6321b33d1344060be0fc1052756d095f266ead36f6719e87fba8d629f59c7.jpg)  

# FIGURE 15.2  

Delta-hedged long call position.  

In this example, there are about 1.2 months to the expiration of this option, the option is at-themoney, and the initial implied volatility is $20\%$ .  

It turns out that in this environment, even when the trader's anticipations are borne out, the payoffs from the volatility position may vary significantly, depending on the path followed by $S_{t}$ . The implied volatility may move from $20\%$ to $30\%$ as anticipated, but the position may not pay the expected amount. The following example displays the related calculations.  

# EXAMPLE  

We can calculate the relevant Greeks and payoff curves using Mathematica or MATLAB. First, we obtain the initial price of the call as  
$$
C(100,t_{0})=2.52
$$  

Multiplying by 100, the total position is worth $\$252$ . Then, we get the implied delta of this position by first calculating the $S_{t}$ -derivative of $C(S_{t},t)$ evaluated at $S_{t_{0}}=100$ , and then multiplying by 100:  
$$
[^100]: \bigg(\frac{\partial C(S_{t},t)}{\partial S_{t}}\bigg)=51.2
$$  

Hence, the position has $+51$ -delta. To hedge this exposure, the trader needs to short 51 units of the underlying and make the net delta exposure approximately equal to zero.  

Next, we obtain the associated gamma and the (variance) vega of the position at $t_{0}$ . Using the given data, we get  
$$
\mathrm{Gamma}=100\bigg[\frac{\hat{\sigma}^{2}C(S_{t},t)}{\hat{\sigma}S_{t}^{2}}\bigg]=6.3
$$  
$$
{\mathrm{Variance~vega}}=100\left[{\frac{\hat{\sigma}C(S_{t},t)}{\hat{\sigma}\sigma^{2}}}\right]=3152
$$  

The change in the option value, given a change in the (implied) variance, is given approximately by  
$$
[^100]: [\partial C(S_{t},t)]\cong(3152)\widehat{\sigma}\sigma^{2}
$$  

This means that, everything else being constant, if the implied volatility rises suddenly from $20\%$ to $30\%$ , the instantaneous change in the option price will depend on the product of these numbers and is expected to be  
$$
\begin{array}{c}{{100[\partial C(S_{t},t)]\cong3152(0.09-0.04)}}\\ {{{}}}\\ {{=157.6}}\end{array}
$$  

In other words, the position is expected to gain about $\$158$ , if everything else remained constant.  

The point is that the trader was long implied volatility, expecting that it would increase, and it did. So if the volatility does go up from $20\%$ to $30\%$ , is this trader guaranteed to gain the $\$157.6?$ Not necessarily. Let us see why not.  
Even in this simplified Black Scholes world, the (variance) vega is a function of $S_{t},\ t,\ r,$ as well as $\sigma^{2}$ . Everything else is not constant and the $S_{t}$ may follow any conceivable trajectory. But, and this is the important point, when $S_{t}$ changes, this in turn will make the vega change as well. The following table shows the possible values for variance-vega depending on the value assumed by $S_{t},$ , within this setting.6  

<html><body><table><tr><td>St Vega</td></tr><tr><td>80 0.0558</td></tr><tr><td>90 7.4666</td></tr><tr><td>100 31.5234</td></tr><tr><td>110 10.6215</td></tr><tr><td>120 0.5415</td></tr></table></body></html>  

Thus, if the expectations of the trader are fulfilled, the implied volatility increases to $30\%$ , but, at the same time, if the underlying price moves away from the strike, say to $S_{t_{1}}=80$ , the same calculation will become approximately:  
$$
\begin{array}{l}{{\mathrm{Vega}(\hat{o}\sigma^{2}){\cong}5.6(0.09-0.04)}}\\ {{=}0.28}\end{array}
$$  

Hence, instead of an anticipated gain of $\$157.6$ , the trader could realize almost no gain at all. In fact, if there are costs to maintaining the volatility position, the trader may end up losing money. The reason is simple: as $S_{t}$ changes, the option's sensitivity to implied volatility, namely the vega, changes as well. It is a function of $S_{t}$ . As a result, the outcome is very different from what the trader was originally expecting.  

For a more detailed view on how the position's sensitivity moves when $S_{t}$ changes, consider Figure 15.3 where we plot the partial derivative:  
$$
[^100]: {\frac{\partial{\mathrm{~variance~vega}}}{\partial S_{t}}}
$$  

Under the present conditions, we see that as long as $S_{t}$ remains in the vicinity of the strike $K$ , the trader has some exposure to volatility changes. But as soon as $S_{t}$ leaves the neighborhood of $K$ , this exposure drops sharply. The trader may think he or she has a (variance) volatility position, but, in fact, the position costs money, and may not have any significant variance exposure as the underlying changes right after the trade is put in place. Thus, such classical volatility positions are imperfect ways of putting on volatility trades or hedging volatility exposures.  

![](4486c037cb124f120b718a3d6346c4a8a80ad2dbbccc928021deb05f3223277f.jpg)  

# FIGURE 15.3  

Vega as a function of the price of the underlying.  

# 15.3.2 VOLATILITY HEDGING  

The outcome of such volatility positions may also be unsatisfactory if these positions are maintained as a hedge against a constant volatility exposure in another instrument. According to what was discussed, movements in $S_{t}$ can make the hedge disappear almost completely and the trader may hold a naked volatility position in the end. An institution that has volatility exposure may use a hedge only to realize that the hedge may be slipping over time due to movements unrelated to volatility fluctuations.  

Such slippage may occur for more reasons than just a change in $S_{t}$ . In reality, there are also (i) smile effects, (ii) interest rate effects, and (iii) shifts in correlation parameters in some instruments. Changes in these can also cause the classical volatility payoffs to move away from initially perceived levels.  

# 15.3.3 A STATIC VOLATILITY POSITION  

If a dynamic delta-neutral option position loses its exposure to movements in $\sigma^{2}$ and, hence, ceases to be useful as a hedge against volatility risk, do static positions fare better?  

A classic position that has volatility exposure is buying (selling) ATM straddles. Using the same numbers as above, Figure 15.4 shows the joint payoff of an ATM call and an ATM put struck at $K=100$ . This position is made of two plain vanilla options and may suffer from a similar defect. The following example discusses this in more detail.  

![](2c282b99cf434d83d4d56f7553d884472fa6f951569cef12d74ebe2f26a33d0f.jpg)  

# FIGURE 15.4  

Joint payoff of an ATM call and ATM put.  

# EXAMPLE  

As in the previous example, we choose the following numerical values:  
$$
S_{t_{0}}=100,~r=0,~T-t_{0}=0.1
$$  

The initial volatility is $20\%$ , which means that  
$$
\sigma^{2}=0.04
$$  

We again look at the sensitivity of the position with respect to movements in some variables of interest. We calculate the variance vega of the portfolio:  
$$
V(S_{t},t)=100\{\mathrm{ATMPut+ATMCall}\}
$$  

by taking the partial:  
$$
{\mathrm{Straddle~vega}}=100{\frac{\partial V(S_{t},t)}{\partial\sigma^{2}}}
$$  

Then, we substitute the appropriate values of $S_{t},t,\sigma^{2}$ in the formula. Doing this for some values of interest for $S_{t}$ , we obtain the following sensitivity factors:  

<html><body><table><tr><td>St</td><td>Vega</td></tr><tr><td>80</td><td>11</td></tr><tr><td>90</td><td>1493</td></tr><tr><td>100</td><td>6304</td></tr><tr><td>110</td><td>2124</td></tr><tr><td>120</td><td>108</td></tr></table></body></html>  

According to these numbers, if $S_{t}$ stays at 100 and the volatility moves from $20\%$ to $30\%$ , the static position's value increases approximately by  
$$
{\begin{array}{c}{{\hat{\sigma}}\operatorname{Straddle}\cong6304(0.09-0.04)}\\ {\qquad}\\ {=315.2}\end{array}}
$$  

As expected, this return is about twice as big as in the previous example. The straddle has more sensitivity to volatility changes. But, the option's responsiveness to volatility movements is again not constant, and depends on factors that are external to what happens to volatility. The table shows that if $S_{t}$ moves to 80, then even when the trader's expectation is justified and volatility moves from $20\%$ to $30\%$ , the position's mark-to-market gains will go down to about 0.56.  

![](06a4210dae3540cdf13e91d669da40e910561f33efc14f751bfb47a7e866f4d5.jpg)  

# FIGURE 15.5  

Straddle's sensitivity with respect to implied volatility for different values of $S_{t}.$  

Figure 15.5 shows the behavior of the straddle's sensitivity with respect to implied volatility for different values of $S_{t}$ . We see that the volatility position is again not invariant to changes in external variables. However, there is one major difference from the case of a dynamically maintained portfolio. Static non-delta-hedged positions using straddles will benefit from actual (realized) movements in $S_{t}$ . For example, if $S_{t}$ stays at 80 until expiration date $T,$ the put leg of the straddle would pay 20 and the static volatility position would gain. This is regardless of how the vega of the position changed due to movements in $S_{t}$ over the interval $[t_{0},T]$ .  

# 15.4 PURE VOLATILITY POSITIONS  

The key to finding the right way to hedge volatility risk or to take positions in it is to isolate the "volatility" completely, using existing liquid instruments. In other words, we have to construct a synthetic such that the value of the synthetic changes only when "volatility" changes. This position should not be sensitive to variations in variables other than the underlying volatility. The exposure should be invariant. Then, we can use the synthetic to take volatility exposures or to hedge volatility risk. Such volatility instruments can be quite useful.  

First, we know from Chapters 12 and 13 that by using options with different strikes we can essentially create any payoff that we like—if options with a broad range of strikes exist and if markets are complete. Thus, we should, in principle, be able to create pure volatility instruments by using judiciously selected option portfolios.  

![](258f0208ab847210e70a9c43d77e9a555d2af05c72f8f0e2450efc0bced1d89a.jpg)  

# FIGURE 15.6  

Vega of three plain vanilla European call options.  

Second, if an option position's vega drops suddenly once $S_{t}$ moves away from the strike, then, by combining options of different strikes appropriately, we may be able to obtain a portfolio of options whose vega is more or less insensitive to movements in $S_{t}$ . Heuristically speaking, we can put together small portions of smooth curves to get a desired horizontal line.  

When we follow these steps, we can create pure volatility instruments. Consider the plot of the vega of three plain vanilla European call options, two of which are out-of-the-money. The options are identical in all respects, except for their strike. Figure 15.6 shows an example. Three $\sigma^{2}$ sensitivity factors for the strikes $K_{0}=100$ , $K_{1}=110$ , $K_{2}=120$ are plotted. Note that each variance vega is very sensitive to movements in $S_{t}$ , as discussed earlier. Now, what happens when we consider the portfolio made of the sum of all three calls? The sensitivity of the portfolio,  
$$
V(S_{t},t)=\{C(S_{t},t,K_{0})+C(S_{t},t,K_{1})+C(S_{t},t,K_{2})\}
$$  

again varies as $S_{t}$ changes, but less. So, the direction taken is correct except that the previous portfolio did not optimally combine the three options. In fact, according to Figure 15.6, we should have combined the options by using different weights that depend on their respective strike price. The more out-of-the-money the option is, the higher should be its weight, and the more it should be present in the portfolio.  

Hence, consider the new portfolio where the weights are inversely proportional to the square of the strike $K$ ,  
$$
V(S_{t},t)=\frac{1}{K_{0}^{2}}C(S_{t},t,K_{0})+\frac{1}{K_{1}^{2}}C(S_{t},t,K_{1})+\frac{1}{K_{2}^{2}}C(S_{t},t,K_{2})
$$  

![](38e8af45601ed18b356e8bac47cee3124d384ba03fbc275bb686609f1595651e.jpg)  
Variance vega of a portfolio of options with weights inversely proportional to the square of the strike price.  

# FIGURE 15.7  

The variance vega of this portfolio that uses the parameter values given earlier, is plotted in Figure 15.7. Here, we consider a suitable $0<\in$ , and the range  
$$
K_{0}-\in<S_{t}<K_{2}+\in
$$  

Figure 15.7 shows that the vega of the portfolio is approximately constant over this range when $S_{t}$ changes. This suggests that more options with different strikes can be added to the portfolio, weighting them by the corresponding strike prices. In the example below we show these calculations.  

# EXAMPLE  

Consider the portfolio  
$$
V(S_{t},t)=\left[\frac{1}{80^{2}}C(S_{t},t,80)+\frac{1}{90^{2}}C(S_{t},t,90)+\frac{1}{100^{2}}C(S_{t},t,100)\right.
$$  
$$
+\frac{1}{110^{2}}C(S_{t},t,110)+\frac{1}{120^{2}}C(S_{t},t,120)\bigg]
$$  

This portfolio has an approximately constant vega for the range  
$$
[^80]: -\in<S_{t}<120+\in
$$  

By including additional options with different strikes in a similar fashion, we can lengthen this section further.  

We have, in fact, found a way to create synthetics for volatility positions using a portfolio of liquid options with varying strikes, where the portfolio options are weighted by their respective strikes.  

# 15.4.1 PRACTICAL ISSUES  

In our attempt to obtain a pure volatility instrument, we have essentially followed the same strategy that we have been using all along. We constructed a synthetic. But this time, instead of matching the cash flows of an instrument, the synthetic had the purpose of matching a particular sensitivity factor. It was put together so as to have a constant (variance) vega.  

Once a constant vega portfolio is found, the payoff of this portfolio can be expressed as an approximately linear function of $\sigma^{2}$  
$$
V(\sigma^{2})=a_{0}+a_{1}\sigma^{2}+\mathrm{small}
$$  

with  
$$
a_{1}=\frac{\hat{\sigma}V(\sigma^{2},t)}{\hat{\sigma}\sigma^{2}}
$$  

as long as $S_{t}$ stays within the range  
$$
S^{\mathrm{min}}=K_{0}<S_{t}<K_{n}=S^{\mathrm{max}}
$$  

Under these conditions, the volatility position will look like any other long (or short) position, with a positive slope $a_{1}$ .  

The portfolio with a constant (variance) vega can be constructed using vanilla European calls and puts. The rules concerning synthetics discussed earlier apply here also. It is important that elements of the synthetic be liquid; therefore, liquid calls and puts have to be selected. The previous discussion referred only to calls. Practical applications of the procedure involve puts as well. This brings us to two somewhat complicated issues. The first has to do with the smile effect. The second concerns liquidity.  

# 15.4.1.1 The smile effect  

Suppose we form a portfolio at time $t_{0}$ that has a constant vega as long as $S_{t}$ stays in a reasonable range  
$$
S^{\mathrm{min}}<S_{t}<S^{\mathrm{max}}
$$  

Under these conditions, the portfolio consists of options with different "moneyness" properties, and the volatility parameter in the option pricing formulas may depend on $K$ if there is a volatility  

smile. In general, as $K$ decreases, the implied $\sigma(K)$ would increase for constant $S_{t}$ . Under these conditions, the trader needs to accurately determine the smile and the way to model it before the portfolio is formed.  

# 15.4.1.2 Liquidity problems  

From the preceding it follows that we need to select out-of-the-money options for the synthetic since they are more liquid. But as time passes, the moneyness of these options changes and this affects their liquidity. Those options that become in-the-money are now less liquid. Other options that were not originally included in the synthetic become more liquid. Even though the replicating portfolio was static, the illiquidity of the constituent options may become a drawback in case the position needs to be unwound.  

# 15.5 VARIANCE SWAPS  

One instrument that has invariant exposure to fluctuations in (realized) variance is the variance swap. In this section, we introduce this concept and in the next, we provide a simple framework for studying it.  

A variance swap is, in many ways, just like any other swap. The parties exchange floating risk against a risk fixed at the contract origination. In this case, what is being swapped is not an interest rate or a return on an equity instrument, but the variances that correspond to various risk factors.  

# 15.5.1 USES AND USERS OF VARIANCE SWAPS  

Before we study the hedging and pricing of variance swaps it is instructive to think about what the potential uses of variance swaps are.  

# 15.5.1.1 Uses of variance swaps  

We can distinguish several uses and users of variance swaps. First, some users may be interested in variance swaps as a way of directionally trading variance levels. This could be for hedging or speculative purposes. Market participants who would like to speculate on the future levels of stock or index variance or volatility can go long or short realized variance with a variance swap. The advantage of such a position over trading and hedging options is that the variance swap is not contaminated by other risk exposures. If an investor expects a sharp decline in political and financial uncertainty after a forthcoming election, for example, a short position in a variance swap may be a good way to express this view and profit from it.  

Second, some investors may use the variance swap to trade the spread between realized and implied variance levels. As we will see below, the fair strike price $\boldsymbol{F}_{t_{0}}$ in a variance swap is related to the level of current-implied volatilities for options with the same expiration as the swap. Therefore, by unwinding the swap before expiration, a market participant can trade the spread between realized and implied volatility.  

# 15.5.1.2 Market participants with an implicit volatility exposure to hedge  

We can think of at least three groups of market participants with an implicit volatility exposure to hedge. Some event-driven hedge funds engage in merger arbitrage and take positions that assume that the spread between an acquirer and takeover target will narrow. The risk is, however, that if overall market volatility increases the merger may be less likely and the spread may widen leading to loses for merger arbitrage hedge funds.  

Some institutional investors that follow active benchmarking strategies regularly rebalance their portfolios. In volatile periods such rebalancing may need to be more frequent, thus leading to higher portfolio turnover and transaction costs. Independent from transaction costs, higher volatility may also lead to increased tracking error for portfolio managers who are judged against a benchmark. As asset prices move quickly, they may not be able to track the benchmark as effectively as when volatility is low.

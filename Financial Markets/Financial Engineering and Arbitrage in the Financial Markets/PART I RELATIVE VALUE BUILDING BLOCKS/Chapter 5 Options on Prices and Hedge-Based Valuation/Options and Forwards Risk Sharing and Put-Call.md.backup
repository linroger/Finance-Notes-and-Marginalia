---
tags:
  - call_option
  - forwards
  - options
  - put_call_parity
  - put_option
  - risk_sharing
  - strike_price
aliases:
  - Forward Synthesis
  - Off-Market Forward
  - Options and Forwards
  - Put-Call Parity
key_concepts:
  - Call and Put Payoffs
  - Cash vs Physical Settlement
  - Cost-of-Carry Equation
  - Long Forward Strategy
  - Put-Call Parity Formula
  - Synthesizing Forwards
---

# 5.4 OPTIONS AND FORWARDS, RISK SHARING AND PUT-CALL PARITY  

Suppose we buy a call and sell a put on the same asset. Suppose that we also search among all possible strike prices and find one [strike price](Call%20and%20Put%20Payoffs%20at%20Expiry.md), $K$ , such that the premium on the call struck at $K$ that we buy is exactly paid for by the premium on the put struck at $K$ that we sell. Let us examine the payoff of our strategy at expiry for physical-settle options.  

If $S\geq K$ , then the call option is in-the-money and we buy the stock for the amount. $K$ If $S\leq K$ , then the put option is in-the-money. We are exercised against, and we buy the. stock for the amount $K$ . By buying the call and selling the put, we are in effect agreeing to. buy the stock for the amount. $K$ on the expiry date. In a cash settle case, this means that no. matter whether the [stock price](../../../../Financial%20Engineering/Derivatives/Part%20IV%20-%20Options/Chapter%2016%20-%20Black–Scholes%20Model.md) is above or below the [strike price](Call%20and%20Put%20Payoffs%20at%20Expiry.md), our payoff is $S-K$ on the. expiry date.  

Our strategy is equivalent to entering a [long forward](../../../../Financial%20Instruments/Lecture%20Notes-%20Financial%20Instruments/Teaching%20Note%203%20Swaps-%20Financial%20Instruments/Forward%20Rates%20Agreement.md) on the stock. Net, we pay nothing today, and on a future date we deliver the sum of money. $K$ for one share of the stock. The. forward is on-market (zero PV up front)..  

If we were slightly less careful in our search for the perfect strike, and instead picked one at random, but made sure that the strike on the long call is the same as the strike on the short put, then we would have in effect entered into an [off-market forward](.md) with the markto-market value (PV) equal to the difference between the premium on the call and that on the put:  
$$
C a l l-P u t=F o r w a r d
$$  

One can think of the forward value of the stock as the median separating two possibility regions for the future [stock price](../../../../Financial%20Engineering/Derivatives/Part%20IV%20-%20Options/Chapter%2016%20-%20Black–Scholes%20Model.md). The long call covers the part of the region to the right of the strike, i.e. with stock values greater than the strike. The short put covers that part of the region to the left of the strike, i.e. with stock values lower than the strike. Traders can synthesize [forwards](../../../Financial%20Asset%20Pricing%20Theory%20Overview/Chapter%2012%20-%20Derivatives/Forwards%20and%20Futures.md) from options, or they can enter into [forwards](../../../Financial%20Asset%20Pricing%20Theory%20Overview/Chapter%2012%20-%20Derivatives/Forwards%20and%20Futures.md) and synthesize options by selling off the undesirable probability regions. For example to synthesize a call, a dealer may enter into a forward and buy a put to offset the short put implicit in the forward. To synthesize a put, a dealer may enter into a [short forward](../../../../Financial%20Instruments/Lecture%20Notes-%20Financial%20Instruments/Teaching%20Note%203%20Swaps-%20Financial%20Instruments/Forward%20Rates%20Agreement.md) and buy a call to offset the short call implicit in the [short forward](../../../../Financial%20Instruments/Lecture%20Notes-%20Financial%20Instruments/Teaching%20Note%203%20Swaps-%20Financial%20Instruments/Forward%20Rates%20Agreement.md).  

The relationship of [call and put](../../../../Course%20Notes/HBR%20Notes/Notes%20on%20Basic%20Options%20Properties.md) prices to the value of the forward is known as [put-call parity](../../../../Financial%20Engineering/7.%20Black%20Scholes%20Model.md). It takes the following form for options on non-dividend-paying stocks:.  

# Put-Call Parity  
$$
C-P=S-P V(K)
$$  

The left-hand side is the cost of the long call-short put strategy. $C$ is the price of the call with strike $K;P$ is the price of the put with strike $K$ . The right-hand side is the mark-to-market $(P V)$ of the [forward contract](../../../../Clippings/Forward%20Points%20in%20Currency.md). The [forward contract](../../../../Clippings/Forward%20Points%20in%20Currency.md) to buy the stock for price $K$ can be replicated by borrowing the present value of $K$ and buying the stock now for the price $S$ If $K$ is low, the contract to buy the stock for $K$ at a forward date is valuable and $S-P V(K)>0$ This also means that calls cost more than puts for low strikes. If $K$ is high, the contract to buy the stock for $K$ at a forward date is not desirable and $S-P V(K)<0.$ This also means that calls cost less than puts for high strikes.  

There is a strike at which the prices of calls and puts must be the same, and that strike is given by the equation  
$$
S=P V(K)
$$  

This is the [cost-of-carry equation](.md) in disguise. If we use the discrete form of discounting over 1 year with [annual interest rate](../../../../Financial%20Instruments/Review%20Session%20Notes/Continuously%20Compounding%20Interest.md). $r$ , then the equation becomes:.  
$$
S=\frac{K^{*}}{1+r}
$$  

The strike at which calls and puts are equally valuable is equal to the [forward price](../../../Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%2011/Forward%20Contracts%20and%20Forward%20Prices.md) of the stock. Someone should be willing to agree today to sell you a stock worth $S=\$100$ today for $K^{*}=\$104$ if the financing rate is. $r=4\%$ . That is because they can borrow $\$100$ at $4\%$ and use the money to buy the stock now; in 1 year they have to repay $\$104$ . The [put-call parity](../../../../Financial%20Engineering/7.%20Black%20Scholes%20Model.md) states that the long call-short put strategy is another way to replicate a forward at no cost, therefore a call struck at $\$104$ and a put struck at. $\$104$ must cost the same. If you buy the call and sell the put, you guarantee yourself a $\$104$ purchase price for the stock in. 1 year's time.  

The [put-call parity](../../../../Financial%20Engineering/7.%20Black%20Scholes%20Model.md) reflects an advanced way of risk [arbitrage](../../../Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%207/Arbitrage%20Pricing%20of%20Derivatives.md). The prices of calls and puts (for all strikes) have to be in line with on- and [off-market forward](.md) and [futures](../Chapter%203%20-%20Futures%20Markets/Futures%20Not%20Subject%20to%20Cash-And-Carry.md). The [arbitrage](../../../Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%207/Arbitrage%20Pricing%20of%20Derivatives.md) is executable by combining [futures](../Chapter%203%20-%20Futures%20Markets/Futures%20Not%20Subject%20to%20Cash-And-Carry.md) and options on the same [underlying asset](../../../../Financial%20Instruments/Financial%20Derivatives%20and%20Quantitative%20Methods/Risk%20Neutral%20Pricing%20of%20Options.md) and choosing to buy the side that is cheaper relative to the other.  

This is also an advanced way of broader [risk sharing](../Chapter%201%20-%20Purpose%20and%20Structure%20of%20Financial%20Markets/Purpose%20and%20Structure%20of%20Financial%20Markets%201.md). When a stock is bought in an [Initial Public Offering](../Chapter%201%20-%20Purpose%20and%20Structure%20of%20Financial%20Markets/Primary%20Issuance%20and%20Secondary%20Resale%20Markets.md) (IPO) providing capital to a growing business, the buyer may not think much. of options and [forwards](../../../Financial%20Asset%20Pricing%20Theory%20Overview/Chapter%2012%20-%20Derivatives/Forwards%20and%20Futures.md). He does, however, appreciate the existence of a [secondary market](../Chapter%201%20-%20Purpose%20and%20Structure%20of%20Financial%20Markets/Primary%20Issuance%20and%20Secondary%20Resale%20Markets.md) for stocks (stock exchange), so that he can sell the stock when he no longer wants to bear its. risk. The person he sells to may, however, be an option player who wants the stock, but only for a certain amount of time or only in a certain scenario. The fact that he can customize his participation in the stock may be the main reason that he purchases the stock. He does not buy another stock that does not have options trading on it, because that would force him into an all-or-nothing risk.  
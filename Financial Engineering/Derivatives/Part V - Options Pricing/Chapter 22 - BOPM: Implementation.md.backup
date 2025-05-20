---
tags:
  - binomial_tree
  - bopm
  - dynamic_hedging
  - replication_portfolio
  - risk_neutral_valuation
aliases:
  - BOPM Implementation
  - Backward Recursion
  - Binomial Option Pricing Model
  - RNV
  - Replication Portfolio
key_concepts:
  - Backward recursion
  - Dynamic delta hedging
  - No-arbitrage binomial pricing
  - Replication portfolio
  - Risk-neutral valuation
---
# BOPM: Implementation  

# Aims  

• To show how [dynamic delta hedging](.md) can be used to price a (two-period) call option, using a [portfolio](../../../Advanced%20Investments/An%20Asset%20Allocation%20Primer.md) comprising stocks and calls, which is risk-free over small intervals of time.   
• To show how [dynamic delta hedging](.md) is consistent with the [no-arbitrage binomial pricing](.md) equation – the latter is a [backward recursion](.md) that can be interpreted using risk-neutral valuation (RNV).   
• To replicate the payof to an option, using stocks and (risk-free) borrowing or lending (e.g. using a bank deposit/loan). This provides an alternative derivation of the [binomial](../../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%205%20Options%20on%20Prices%20and%20Hedge-Based%20Valuation/A%20Real-Life%20Option%20Pricing%20Exercise.md) formula for options.   
• To show that as each time-step in the [binomial tree](../../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%207/Rate%20and%20Price%20Trees.md) becomes smaller, the tree more closely approximates a continuous time process ([Brownian motion](../../../Financial%20Markets/Financial%20Asset%20Pricing%20Theory%20Overview/Chapter%202%20-%20Uncertainty,%20Information,%20and%20Stochastic%20Processes/Continuous-Time%20Stochastic%20Processes.md)) for the [stock price](../Part%20IV%20-%20Options/Chapter%2016%20-%20Black–Scholes%20Model.md) – as used in the Black–Scholes approach. Hence, as we increase the number of time periods in the [binomial tree](../../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%207/Rate%20and%20Price%20Trees.md), the option price calculated from the BOPM formula converges to the Black–Scholes price.  

Using insights from RNV, we price a two-period call option using the BOPM without going through all the details involved in [delta hedging](../../../Financial%20Instruments/Financial%20Instruments.md) and forming a ‘[risk-free arbitrage portfolio](Chapter%2021%20-%20BOPM:%20Introduction.md)’ – instead we price the option assuming RNV, using a ‘[backward recursion](.md)’. This allows us to generalise the BOPM to many periods and to price many diferent types of option. We show that RNV is consistent with there being no [arbitrage opportunities](../../../Financial%20Markets%20and%20Institutions/III.%20Liquidity%20of%20Assets/Class%208-%20Markets,%20Meltdowns,%20and%20Arbitrage/Class%20Note%2013%20The%20LTCM%20Meltdown.md) at any node in the [binomial tree](../../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%207/Rate%20and%20Price%20Trees.md).  

We demonstrate another method of [pricing](../../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%207/Arbitrage%20Pricing%20of%20Derivatives.md) an option using a ‘[replication portfolio](.md)’. We construct a [portfolio](../../../Advanced%20Investments/An%20Asset%20Allocation%20Primer.md) consisting of stocks and risk-free borrowing or lending, which replicates the payofs to the option. The price of the option must then equal the cost of setting up this [replication portfolio](.md), otherwise risk-free [arbitrage](../../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%207/Arbitrage%20Pricing%20of%20Derivatives.md) profts can be made.  

# 22.1 GENERALISING THE BOPM  

We extend the BOPM (analysed in Chapter 21) and price a two-period call option with strike $K=100$ . The current [stock price](../Part%20IV%20-%20Options/Chapter%2016%20-%20Black–Scholes%20Model.md) is $S=100$ , the one-period [risk-free rate](../../../Financial%20Instruments/Black%20Scholes%20Derivation.md) $r=0.05$ and $C=$ the unknown [call premium](../Part%20IV%20-%20Options/Chapter%2017%20-%20Option%20Strategies.md). As previously, we take $U=1.1$ and $D=0.9$ which gives the [stock price tree](../../../Financial%20Instruments/Assignments/Solutions/PSET%205%20Solution-Financial%20Instruments.md) and values for a long call at expiration as indicated in Figure 22.1.  

Because we create a risk-free hedge [portfolio](../../../Advanced%20Investments/An%20Asset%20Allocation%20Primer.md) at each node of the [binomial tree](../../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%207/Rate%20and%20Price%20Trees.md), we can invoke RNV and use ‘[backward recursion](.md)’ to calculate $c$ from the known values of $C_{u u},C_{u d}$ and $C_{d d}$ . For example, from the two upper branches in Figure 22.1 we have:  
$$
C_{u}=\frac{1}{R}[q C_{u u}+(1-q)C_{u d}]=\frac{0.75(21)+0.25(0)}{1.05}=15
$$  

where $q=(R-D)/(U-D)=0.75$ . From the two lower branches:  
$$
C_{d}=\frac{1}{R}[q C_{u d}+(1-q)C_{d d}]=0
$$  

We can now solve for $c$ , the [call premium](../Part%20IV%20-%20Options/Chapter%2017%20-%20Option%20Strategies.md) for this two-period case:  
$$
C=\frac{1}{R}[q C_{u}+(1-q)C_{d}]=\frac{0.75(15)+0}{1.05}=10.7142
$$  

Note that the [call premium](../Part%20IV%20-%20Options/Chapter%2017%20-%20Option%20Strategies.md) for the option with two periods to maturity has a higher value than our ‘identical’ option with one period to maturity, where we found $C=7.143$  

![](4d37f3ce241223dfc0f37d0243b61fd9beb868b101bcf3b1c5351232c0c8b101.jpg)  

(see Chapter 21). [Backward recursion](.md) (under RNV) is the easiest way of obtaining the option price. If we just consider European options, (where only the payof at maturity determines the value of the option), then RNV provides a general formula for [pricing](../../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%207/Arbitrage%20Pricing%20of%20Derivatives.md) calls and puts.  

# 22.1.1 Many Periods  

Equations (22.1) and (22.2) give the values of $C_{u}$ and $C_{d}$ in terms of the fnal payofs $C_{u u}$ , $C_{u d}$ and $C_{d d}$ and if we substitute (22.1) and (22.2) in (22.3) we obtain:  
$$
C=\frac{1}{R^{2}}[(1)q^{2}C_{u u}+2q(1-q)C_{u d}+(1)(1-q)^{2}C_{d d}]
$$  

The European option price is equal to the expected value (using [risk-neutral probabilities](../../../Financial%20Instruments/Financial%20Instruments.md)) of the option payofs at maturity, discounted at the [risk-free rate](../../../Financial%20Instruments/Black%20Scholes%20Derivation.md) of interest.  

The $^{\bullet}2^{\bullet}$ in the middle of Equation (22.4) represents the two possible paths to achieve the [stock price](../Part%20IV%20-%20Options/Chapter%2016%20-%20Black–Scholes%20Model.md) (that is paths $U D$ and $D U$ ) and the ‘1’s’ represent the single path to achieve either $\Bar{S}U^{2}$ or $S D^{2}$ . We interpret $q$ as the risk-neutral probability of an ‘up move’ for $S$ and $(1-q)$ the probability of a ‘down move’. The (risk-neutral) probabilities of achieving the outcomes , or $D U$ and $D D$ are $q^{2}=0.5625,2q(1-q)=0.375$ and $(1-q)^{2}=0.0625$ , respectively. In general the number of possible paths to any fnal [stock price](../Part%20IV%20-%20Options/Chapter%2016%20-%20Black–Scholes%20Model.md) are given by the [binomial](../../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%205%20Options%20on%20Prices%20and%20Hedge-Based%20Valuation/A%20Real-Life%20Option%20Pricing%20Exercise.md) coefcients.  
$$
{\binom{n}{k}}={\frac{n!}{(n-k)!k!}}
$$  

where $n$ is the number of periods in the [binomial tree](../../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%207/Rate%20and%20Price%20Trees.md), $k$ is the number of upward price movements and $n!=n(n-1)(n-2)...1$ and $0!=1$ . Let’s try out Equation (22.5) for $n=2$ :  
$$
\begin{array}{r l r}{\mathrm{Number~of~paths~with}\ k=2\ \mathrm{`ups}^{\mathrm{,}}}&{=}&{(2!)/(0!\ 2!)=1}\\ {\mathrm{Number~of~paths~with}\ k=1\ \mathrm{`ups}^{\mathrm{,}}}&{=}&{(2!)/(1!\ 1!)=2}\\ {\mathrm{Number~of~paths~with}\ k=0\ \mathrm{*ups}^{\mathrm{,}}}&{=}&{(2!)/(2!\ 0!)=1}\end{array}
$$  

i.e. U   
.e. UD or U   
.e. D  

The reader might like to draw a tree with $n=3$ periods (with 8 possible fnal outcomes UUU, UUD, UDU, UDD, DUU, DUD, DDU, DDD), and verify that the number of possible paths to achieve $k=1$ ‘up’ moves is $\binom{n}{k}=(3!)/(2!1!)=3$ and these are UDD, DUD, and DDU. This can also be repeated using Equation (22.5) for $k=2$ or 3 ‘up’ moves. In general, over n-periods in the tree, the BOPM formula for a European call option is:  
$$
C=\frac{1}{R^{n}}\sum_{k=0}^{n}\binom{n}{k}q^{k}(1-q)^{n-k}\operatorname*{max}[S U^{k}D^{n-k}-K,0]
$$  

The probability of the [stock price](../Part%20IV%20-%20Options/Chapter%2016%20-%20Black–Scholes%20Model.md) reaching the value $S U^{k}D^{n-k}$ after $n$ -periods is $\binom{n}{k}q^{k}(1-q)^{n-k}$ . Note that the term in square brackets in (22.6) is just another way of writing the payofs at the fnal nodes. For example, for $n=2$ , these are:  
$$
\mathrm{~\boldsymbol~{~c~}~}_{u u}=\operatorname*{max}[0,S U^{2}-K],~\boldsymbol{C}_{u d}=\operatorname*{max}[0,S U D-K],~\boldsymbol{C}_{d d}=\operatorname*{max}[0,S D^{2}-K]
$$  

The hedge ratios in the BOPM can be calculated at each node and this is done for $n=10$ time periods in the Excel fle provided. The call option premium using RNV and [backward recursion](.md) is found to be $C=39.087$ .  

The price of a put option is also given by Equation (22.6) but with the term max[ . . . ] replaced by the sequence of put-option payofs, namely $m a x/0,K-S U^{k}D^{n-k}J.$ . Equation (22.6) indicates that the price of an option depends on the [strike price](../../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%205%20Options%20on%20Prices%20and%20Hedge-Based%20Valuation/Call%20and%20Put%20Payoffs%20at%20Expiry.md) $K_{:}$ , the [underlying asset price](../../../Financial%20Instruments/Black%20Scholes%20Derivation.md) S, the [risk-free rate](../../../Financial%20Instruments/Black%20Scholes%20Derivation.md) $r$ and the asset’s volatility (which is determined by $U$ and $D$ ), but it does not depend on the risk preferences of individuals or the ‘real-world’ probability of a price increase/decrease or the real world [expected return](../../../Advanced%20Investments/Lecture%201-%20Probability%20Distributions%20of%20Returns.md) on the stock. Below we show that as the number of nodes n in the tree increases, we obtain a more accurate value for the option price and $n>30$ generally gives reasonably accurate results for plain vanilla European options.  

# 22.1.2 Where Do $U$ and D Come From?  

At $t=0,r,K,$ and $s$ are known. Above we have shown that if we know $U$ and $D$ (and hence $q=(R-D)/(U-D))$ , then we can price an option by invoking RNV. It can be shown that the size of $U$ and $D$ are determined by the actual real-world volatility of the stock return, and one method of achieving this is known as the Cox-Ross-Rubinstein (CRR) parameterisation:  
$$
U=e^{\sigma{\sqrt{d t}}}\quad{\mathrm{~and~}}\quad D=e^{-\sigma{\sqrt{d t}}}
$$  

where $\sigma=$ the observed annual standard deviation of the (continuously compounded) stock return (decimal), $T$ is the [time to expiration](../Part%20IV%20-%20Options/Chapter%2016%20-%20Black–Scholes%20Model.md) of the option in years (or fraction of a year), $n$ is the number of steps chosen for the [binomial tree](../../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%207/Rate%20and%20Price%20Trees.md) so $d t=T/n$ is a small interval of time. For example, if the [expiration date](../../../Financial%20Instruments/Financial%20Derivatives%20and%20Quantitative%20Methods/Risk%20Neutral%20Pricing%20of%20Options.md) of the option is at $T={}^{1}/_{4}$ year (3 months) and we choose a [binomial tree](../../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%207/Rate%20and%20Price%20Trees.md) with $n=30$ steps, then $d t=0.008333$ years (i.e. represents about 3 days out of a total of 365 calendar days per year).  

Given Equation (22.8), note that the ‘spread’ of the [binomial lattice](../../6.%20A%20Brief%20Introduction%20to%20Stochastic%20Calculus.md)/tree (in percentage terms) at any two adjacent points (in a vertical direction) is $\ln(S U)-\ln(S D)=2\sigma{\sqrt{d t}}$ , so the proportionate gap between $U$ and $D$ (i.e. $\ln(U/D))$ does depend directly on the ‘real world’ value of $\sigma$ . Our particular choice for $U$ and $D$ imposes symmetry that is $U=1/D$ but it can be shown that this is not restrictive if our aim is to construct a ‘risk-neutral’ lattice. Note also that when $U=1/D$ , the nodes and $S D U$ both have a value equal to $s$ and the lattice recombines. For example, if $s$ (at $t=0$ ) is 100 it will also be 100 in the middle node at $t=2$ . Finally, note that $U$ and $D$ do not depend on the real world [expected return](../../../Advanced%20Investments/Lecture%201-%20Probability%20Distributions%20of%20Returns.md) on the stock and hence neither does the option premium – this is RNV again.  

We now have a very useful method of [pricing](../../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%207/Arbitrage%20Pricing%20of%20Derivatives.md) a European call option (say), using RNV and [backward recursion](.md) through the [binomial tree](../../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%207/Rate%20and%20Price%20Trees.md):  

• Choose $n>30$ and divide the [time to maturity](../../../Financial%20Instruments/Lecture%20Notes-%20Financial%20Instruments/Teaching%20Note%201-%20Forward%20Rates%20Agreement/Hedging%20Strategies%20with%20Forwards.md) $T$ (in years) of the call option into small time intervals each representing $d t=T/n$ (years).   
• If $r$ (decimal) is the (annual) [continuously compounded interest](../../../Financial%20Instruments/Assignments/Solutions/PSET%207%20Solutions-Financial%20Instruments.md) rate then $R=e^{-r d t}$ .   
• Construct the tree for the [stock price](../Part%20IV%20-%20Options/Chapter%2016%20-%20Black–Scholes%20Model.md) using $U=e^{\sigma{\sqrt{d t}}}$ and $D=e^{-\sigma{\sqrt{d t}}}$ – this ensures the volatility of the stock return mimics its real world volatility.1   
• Calculate the possible fnal payofs, $\operatorname*{max}[0,S_{T}-K]$ at $T$ for the call option.   
• Use $q=(R-D)/(U-D)$ to calculate the expected payofs for the call – this is RNV.   
• Undertake [backward recursion](.md) through the tree, discounting the option values at the [risk-free rate](../../../Financial%20Instruments/Black%20Scholes%20Derivation.md) each period (this is RNV again), to fnally obtain the option price at $t=0$ .  

Although the above recursive method is very useful, it is worth remembering that the reason it works is because ‘behind the scenes’, at each node of the tree, we are implicitly assuming options traders are forming a risk-free [delta-hedged portfolio](../../../Financial%20Instruments/Financial%20Derivatives%20and%20Quantitative%20Methods/JP%20Morgan-Variance%20Swaps.md) so that no [arbitrage](../../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%207/Arbitrage%20Pricing%20of%20Derivatives.md) profts are possible at any node – this is examined further in Appendix 22.  

The option price will change as the [stock price](../Part%20IV%20-%20Options/Chapter%2016%20-%20Black–Scholes%20Model.md), stock return volatility, interest rate or the [time to maturity](../../../Financial%20Instruments/Lecture%20Notes-%20Financial%20Instruments/Teaching%20Note%201-%20Forward%20Rates%20Agreement/Hedging%20Strategies%20with%20Forwards.md) change over time. We can calculate the (approximate) change in the price of the option using the option’s ‘[Greeks](Chapter%2026%20-%20Pricing%20Options:%20Monte%20Carlo%20Simulation.md)’ which include not only delta but the option’s gamma, vega, theta, and rho. Calculation of [the Greeks](../../../Financial%20Instruments/Financial%20Derivatives%20and%20Quantitative%20Methods/Options%20Greeks.md) for the BOPM is explained in Chapter 28.  

# 22.2 REPLICATION PORTFOLIO  

22.2.1 Replicating a Long Call: One-period BOPM  

In our original example, we priced the (one-period) call option by establishing a [risk-free portfolio](../../../Financial%20Markets/Financial%20Asset%20Pricing%20Theory%20Overview/Chapter%204%20-%20State%20Prices/Definitions%20and%20Immediate%20Consequences.md) consisting of a written call and a [long position](../Part%20I%20-%20Forwards%20and%20Futures/Chapter%204%20-%20Futures:%20Hedging%20and%20Speculation.md) in ‘delta’ stocks. We can also price the call by establishing a synthetic call or a [replication portfolio](.md) for the call, using stocks and the [risk-free asset](../../2.%20Forwards,%20Swaps,%20Futures,%20and%20Options.md). We combine stocks and the [risk-free asset](../../2.%20Forwards,%20Swaps,%20Futures,%20and%20Options.md) at $t=0$ into a ‘[replication portfolio](.md)’ which gives exactly the same payofs as the call $C_{u}$ , $C_{d}$ at $t=1$ . Because our ‘[replication portfolio](.md)’ has the same payof as the call (at $t=1\dot{}$ ), then the price of the call must equal the cost of setting up the ‘[replication portfolio](.md)’ (at $t=0$ ) – otherwise risk-free [arbitrage](../../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%207/Arbitrage%20Pricing%20of%20Derivatives.md) profts are possible.  

![](8cba7d54ff4ed835591b3976324e23c89acde3a10068a7e406769ba93f52c5e4.jpg)  
FIGURE 22.2 [Replication portfolio](.md)  

Consider purchasing $N_{0}$ stocks at a price $S_{0}$ and buying $\$8$ of risk-free (zero-coupon) bonds with a return $R=(1+r)$ – see Figure 22.2. When $B_{0}>0$ this implies a bond purchase (lending money) and $B_{0}<0$ implies issuing bonds (borrowing money). Hence, $B_{0}<0$ could just as easily be the amount borrowed in the form of a bank loan and $B_{0}>0$ , represents the amount placed in a bank deposit.  

[Replication Portfolio](.md)-A: Stocks plus Bonds  

At $t=1$ , [portfolio](../../../Advanced%20Investments/An%20Asset%20Allocation%20Primer.md)-A is worth either $(N_{0}S_{u}+B_{0}R)$ or $(N_{0}S_{d}+B_{0}R)$ and to replicate the payof from a long call, we set these two values equal to $C_{u}$ and $C_{d}$ , respectively:  
$$
\begin{array}{c}{{(N_{0}S_{u}+B_{0}R)=C_{u}}}\\ {{{}}}\\ {{(N_{0}S_{d}+B_{0}R)=C_{d}}}\end{array}
$$  

Subtracting Equation (22.10b) from (22.10a) gives:  
$$
N_{0}=(C_{u}-C_{d})/(S_{u}-S_{d})
$$  

From (22.10a) and (22.10b),  
$$
B_{0}=\frac{C_{u}-(N_{0}S_{u})}{R}=\frac{C_{d}-(N_{0}S_{d})}{R}
$$  

Substituting $N_{0}$ from Equation (22.11) into Equation (22.12) and using $S_{u}=S U,S_{d}=S D$ :  
$$
B_{0}=\frac{S_{u}C_{d}-S_{d}C_{u}}{R(S_{u}-S_{d})}=\frac{U C_{d}-D C_{u}}{R(U-D)}
$$  

It is easy to see that the two expressions for $B_{0}$ in Equation (22.12) are equal by noting that they imply $(C_{u}-C_{d})=N_{0}(S_{u}-S_{d})$ and given the defnition of $N_{0}$ in (22.11) these two expressions must be equal. As the [portfolio](../../../Advanced%20Investments/An%20Asset%20Allocation%20Primer.md) of $N_{0}$ stocks and $B_{0}$ (dollars) bonds is constructed to replicate the payof of the call option at $t=1$ , then the [call premium](../Part%20IV%20-%20Options/Chapter%2017%20-%20Option%20Strategies.md) $C_{0}$ (at time $t=0$ ) must equal the cost of the [replication portfolio](.md) at $t=0$ (otherwise [arbitrage](../../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%207/Arbitrage%20Pricing%20of%20Derivatives.md) profts could be made):  

Substituting in (22.14) for $N_{0}$ from (22.11) and for $B_{0}$ from (22.13), then after some manipulation we obtain:  
$$
C_{0}=N_{0}S_{0}+B_{0}={\frac{1}{R}}[q C_{u}+(1-q)C_{d}]
$$  

where $q=(R-D)/(U-D)$ . The number of stocks $N_{0}$ in Equation (22.11) required to replicate the payofs of the call, is the [hedge ratio](../Part%20VI%20-%20The%20Greeks/Chapter%2027%20-%20Delta%20Hedging.md) $h$ in our earlier derivation.  

# 22.2.2 Replicating a Long Call: Two-period BOPM  

Now we use this approach to replicate the option values in a two-period lattice using stocks and the [risk-free asset](../../2.%20Forwards,%20Swaps,%20Futures,%20and%20Options.md). Consider what is happening at $t=0$ (Figure 22.1). From (22.11) and (22.12) we have:  
$$
N_{0}=\frac{C_{u}-C_{d}}{S_{u}-S_{d}}=\frac{15-0}{100(0.2)}=0.75
$$  
$$
B_{0}=\frac{C_{u}-(N_{0}.S_{u})}{R}=\frac{15-0.75(110)}{1.05}=-64.286
$$  

(as before)  

Note that here we are replicating the payof of the long call (at $t=1$ ) with a [long position](../Part%20I%20-%20Forwards%20and%20Futures/Chapter%204%20-%20Futures:%20Hedging%20and%20Speculation.md) in 0.75 of stocks and a short position in the bond (i.e. borrowing cash). At $t=0$ the [replication portfolio](.md) consists of borrowing $\$64.286$ and purchasing $\$75$ of stocks $(N_{0}S_{0}=0.75\times\S100)$ . This is a net [investment](../../../Advanced%20Investments/An%20Asset%20Allocation%20Primer.md) of $\$10.714$ which, not surprisingly, we have earlier found is the value of the option premium $c$ (at $t=0$ ) for a two-period call. The outcome in the ‘up’ and ‘down nodes for our ‘[replication portfolio](.md)’ are:  
$$
\begin{array}{r c l}{{N_{0}S_{u}+B_{0}R}}&{{=}}&{{0.75(110){-}64.286(1.05)=82.5{-}67.5=15}}\\ {{N_{0}S_{d}+B_{0}R}}&{{=}}&{{0.75(90)-64.286(1.05)=67.5{-}67.5=0}}\end{array}
$$  

which, of course, are the outcomes for the value of the call, $C_{u}=15$ , and $C_{d}=0$ at the frst two nodes. We now rebalance our [replication portfolio](.md) so at the $U$ -node:  
$$
\begin{array}{l}{{N_{u}=\displaystyle\frac{C_{u u}-C_{u d}}{S_{u u}-S_{u d}}=0.9545}}\\ {{B_{u}=\displaystyle\frac{C_{u u}-(N_{u}S_{u u})}{R}=\displaystyle\frac{21-0.9545(121)}{1.05}=-90}}\end{array}
$$  

The reason for borrowing $\$90$ at node $U$ is that you must increase the number of stocks by $(0.9545-0.75)=0.2045$ at a price of $\$110$ per stock, giving a total cost of $\$22.5$ , which when added to your existing debt of 67.5 brings your debt to $\$90$ . The outcomes for the [replication portfolio](.md) when moving from the $U$ -node to the nodes UU and $U D$ are:  
$$
:N_{u}S_{u u}+B_{u}R=0.9545(121)-90(1.05)=115.5-94.5=21
$$  
$$
:N_{u}S_{u d}+B_{u}R=0.9545(99)-90(1.05)=94.5-94.5=0
$$  

Again we have replicated the value of the call at these two nodes (see Figure 22.2). Finally, consider the $D$ -node. Here $N_{d}=(C_{u d}-C_{d d})/(S_{u d}-S_{d d})=0$ and the [replication portfolio](.md) consists of zero stocks and is entirely composed of bonds $B_{d}=C_{u d}/R$ but because $C_{u d}=0$ (Figure 22.1), we hold no bonds at the $D$ -node. The [replication portfolio](.md) at node- ${\mathbf{}}\cdot{\cal D}$ is therefore worth zero – but this exactly replicates the value of the call at the nodes $U D$ and $D D$ (Figure 22.1).  

Naturally, we obtain the same BOPM formula for the price of the call using either the ‘[replication portfolio](.md)’ of stocks plus bonds or by using our earlier ‘delta hedge’ [risk-free portfolio](../../../Financial%20Markets/Financial%20Asset%20Pricing%20Theory%20Overview/Chapter%204%20-%20State%20Prices/Definitions%20and%20Immediate%20Consequences.md).  

# 22.3 BOPM TO BLACK–SCHOLES  

By increasing the number of steps $n$ , in the [binomial tree](../../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%207/Rate%20and%20Price%20Trees.md) and seeing what happens to the option price in the BOPM, we obtain some insight into the Black–Scholes [pricing](../../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%207/Arbitrage%20Pricing%20of%20Derivatives.md) formula for European options. As we increase the number of steps we are also shortening the time interval between each node in the [binomial tree](../../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%207/Rate%20and%20Price%20Trees.md) $d t=T/n$ , so the BOPM becomes ‘more like’ the Black–Scholes approach, which uses [continuous time mathematics](../Part%20XII%20-%20Price%20Dynamics/Chapter%2047%20-%20Asset%20Price%20Dynamics.md), and the option price given by the BOPM formula converges towards the Black–Scholes price. Suppose we have:  
$$
S=90~K=100~r=0.10~\sigma=0.20~T=0.3\mathrm{(years)}
$$  

then the Black–Scholes formula gives a [call premium](../Part%20IV%20-%20Options/Chapter%2017%20-%20Option%20Strategies.md) $C^{B S}=5.33$ . To translate these inputs into the BOPM we use $d t=T/n$ where $n$ is the number of steps in the [binomial tree](../../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%207/Rate%20and%20Price%20Trees.md). We then calculate $U,D$ and $R$ as follows:  
$$
U=e^{\sigma\sqrt{d t}}D=e^{-\sigma\sqrt{d t}}R=e^{r d t}
$$  

For example, for $n=1$ we have:  
$$
\begin{array}{l l}{{d t=T/n=0.3/1=0.3~}}&{{R=e^{r d t}=1.0304}}\\ {{U=e^{0.20\sqrt{0.3}}=1.0618~}}&{{D=e^{-0.20\sqrt{0.3}}=0.9418}}\end{array}
$$  

![](12231a08c30791e2407ca846dc9e65555f7a8e07f0f26ebc4ef6f768b5edba33.jpg)  
FIGURE 22.3 [Call premium](../Part%20IV%20-%20Options/Chapter%2017%20-%20Option%20Strategies.md) – BOPM and Black–Scholes  

The [call premium](../Part%20IV%20-%20Options/Chapter%2017%20-%20Option%20Strategies.md) given by the BOPM using only one time-step is:  
$$
C^{(1)}=\frac{q C_{u}+(1-q)C_{d}}{R}=6.21
$$  

where $q=(R-D)/(U-D),C_{u}=\operatorname*{max}(S U-K,0),C_{d}=\operatorname*{max}(S D-K,0)$ . For $n=1$ then we have $C^{(1)}=6.21$ which is not particularly close to the Black–Scholes value $C^{B S}=5.33$ .  

However, as we apply the recursive [binomial](../../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%205%20Options%20on%20Prices%20and%20Hedge-Based%20Valuation/A%20Real-Life%20Option%20Pricing%20Exercise.md) Equation (22.6) for $n=2,3$ , etc. and $d t=T/n$ , the [binomial](../../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%205%20Options%20on%20Prices%20and%20Hedge-Based%20Valuation/A%20Real-Life%20Option%20Pricing%20Exercise.md) call price for $n=30$ is $C^{(30)}=5.345$ , which is close to the Black–Scholes value of $C^{B S}=5.33\mathrm{~-~}\mathbf{s}$ ee Figure 22.3. In general, for plain vanilla European options (but not necessarily for complex [exotic](../../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%206%20Options%20on%20Non-Price%20Variables/Exotic%20Interest%20Rate%20Options.md) options) choosing $n=30$ in the BOPM gives reasonably accurate results for the option price. The CRR parameterisation oscillates between over- and under-approximations (which are approximately symmetric) and which gradually dampen as the number of steps in the tree increases. The average of these over- and under-approximations converges rapidly towards the Black–Scholes price – for example, using only $n=20$ steps in the [binomial tree](../../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%207/Rate%20and%20Price%20Trees.md) we have $C^{(20)}=5.3615$ and $C^{(21)}=5.3422$ and the average of the two is 5.3518, which is very close to $C^{B S}=5.33$ .  

The Excel fle which demonstrates that the BOPM solution for a European option does approach the Black–Scholes price as n becomes large, can be found on the website.  

Of course, one problem with a numerical method like the BOPM is that it may not converge quickly and the solution can ‘bounce around’ the ‘correct’ option price given by Black–Scholes.  

This is the price you pay for the \$exibility of the binomial approach. The option premium from the BOPM approaches that given by the Black–Scholes formula, as the number of steps increases (i.e. $n\rightarrow\infty$ and hence $d t=T/n\rightarrow0)$ . The ‘up–down’ lattice of the BOPM then has many nodes and there are many possible paths the stock price could take (e.g. for just three nodes you can have eight possible paths $(U U U,U U D,U D D,D D)$ etc. – see below)). Hence as $d t=T/n\rightarrow0$ the BOPM lattice approximates the [geometric Brownian motion](../../../Financial%20Instruments/Black%20Scholes%20Derivation.md) used by Black, Scholes and [Merton](../../../Credit%20Markets/Credit%20Markets%20Session%205.md) in deriving the [pricing](../../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%207/Arbitrage%20Pricing%20of%20Derivatives.md) formulas for European options.  

Also notice that when the number of nodes in the [binomial tree](../../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%207/Rate%20and%20Price%20Trees.md) increases, the [possible outcomes](../../../Financial%20Markets/Financial%20Asset%20Pricing%20Theory%20Overview/Chapter%202%20-%20Uncertainty,%20Information,%20and%20Stochastic%20Processes/Probability%20Space.md) for stock prices in the fnal period $(T)$ begin to look more like a ‘normal curve’. For example, with a probability of $^1/_{2}$ for an ‘up’ move, $U=1.1$ , $D=0.9$ and for $n=3$ nodes the outcomes and probabilities are:  

<html><body><table><tr><td>Path</td><td>Probability</td><td>Final stock prices</td></tr><tr><td>UUU</td><td>1/8</td><td>SUUU = 133.1</td></tr><tr><td>UUD,DUU,UDU</td><td>3/8</td><td>SUUD = 108.9</td></tr><tr><td>UDD,DDU,DUD</td><td>3/8</td><td>SUDD = 89.1</td></tr><tr><td>DDD</td><td>1/8</td><td>SDDD = 72.9</td></tr></table></body></html>  

If the fnal stock prices are plotted in a histogram it looks (slightly) more like a ‘normal curve’ than if we just had $n=1$ with two outcomes 110 and 90 (each with probability of $^1/_{2})$ . This is because for $n=3$ the ‘extreme’ and $D D D$ outcomes each only occur $1/8\mathrm{th}$ of the time but the central portion of the histogram for the paths with a one-up move or a one-down move, each occur 3/8ths of the time. In fact, as the number of nodes $n$ increases (i.e. the time period between each node gets smaller) the ‘histogram’ for the fnal stock prices in the BOPM does approach a ‘normal curve’ – which is the assumption used in deriving the Black–Scholes formula.2  

# 22.4 SUMMARY  

• RNV provides a way of obtaining the BOPM formula for option premia using [backward recursion](.md), which considerably simplifes the calculations. But behind this approach is the assumption that options traders are able to undertake [dynamic delta hedging](.md) to eliminate any risk-free [arbitrage](../../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%207/Arbitrage%20Pricing%20of%20Derivatives.md) profts.   
• For European options, the BOPM is a [backward recursion](.md) starting with the option payofs at maturity $T$ , then calculating the expected value of the option at each node in the tree using [risk-neutral probabilities](../../../Financial%20Instruments/Financial%20Instruments.md) and discounting these payofs using the [risk-free rate](../../../Financial%20Instruments/Black%20Scholes%20Derivation.md). Repeating this procedure as you move backwards through the tree, gives the ‘correct’ or ‘no-[arbitrage](../../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%207/Arbitrage%20Pricing%20of%20Derivatives.md)’ option price.   
• The BOPM formula for the option premium can also be derived by replicating the payofs to the option, using stocks and risk-free borrowing or lending (i.e. using either a risk-free bond or bank deposit/loan).   
• In the BOPM the ‘size’ of the ‘up’ $U=e^{\sigma{\sqrt{d t}}}$ and ‘down’ $D=e^{-\sigma{\sqrt{d t}}}$ movements in the [stock price](../Part%20IV%20-%20Options/Chapter%2016%20-%20Black–Scholes%20Model.md) depend on the ‘real world’ volatility of the stock return – and via $q$ in the BOPM, the option price depends on the volatility of the stock return.   
• The European option premium given by the BOPM, converges towards the Black– Scholes price, as the number of steps $n$ in the [binomial tree](../../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%207/Rate%20and%20Price%20Trees.md) increases (so each time-step in the tree represents a smaller interval of time).   
• The BOPM is a numerical technique, so it may sufer from convergence problems and only gives an approximation to the ‘true price’ – but it is a very \$exible method which can be used to price [exotic](../../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%206%20Options%20on%20Non-Price%20Variables/Exotic%20Interest%20Rate%20Options.md) options.  

# APPENDIX 22: DELTA HEDGING AND ARBITRAGE  

Given values for the call option determined by RNV in the two-period BOPM, we show that [dynamic delta hedging](.md) ensures that no risk-free [arbitrage](../../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%207/Arbitrage%20Pricing%20of%20Derivatives.md) profts can be made at each node in the tree. The hedge ratios at each node are easily calculated (see Figure 22.A.2).  
$$
{\begin{array}{r l}&{h_{u}={\cfrac{C_{u u}-C_{u d}}{S_{u u}-S_{u d}}}={\cfrac{21}{(121-99)}}=0.9545}\\ &{h_{d}={\cfrac{C_{u d}-C_{d d}}{S_{u d}-S_{d d}}}=0}\\ &{~h={\cfrac{C_{u}-C_{d}}{S_{u}-S_{d}}}={\cfrac{15-0}{110-90}}=0.75}\end{array}}
$$  

The [hedge ratio](../Part%20VI%20-%20The%20Greeks/Chapter%2027%20-%20Delta%20Hedging.md) at $t=0$ is 0.75, then if the upper branch ensues, it rises to 0.9545 whereas on the lower branch it is zero. We show how we can maintain a delta-neutral position at each node of the tree and this implies our [risk-free portfolio](../../../Financial%20Markets/Financial%20Asset%20Pricing%20Theory%20Overview/Chapter%204%20-%20State%20Prices/Definitions%20and%20Immediate%20Consequences.md) earns the risk free rate, $r=5\%$ (per period). We assume a trader has written 1,000 calls (at $t=0\mathrm{\dot{\Omega}}$ ) and she needs to delta-hedge this position with stocks.  
$$
A t\ t=0:\quad h=0.75,\quad C=10.714,\quad S=100
$$  

Write 1,000 calls and buy 750 stocks  
$$
\mathrm{Buy~750~stocks}\ @\S100=\S75,000
$$  

The outcomes at the $U.$ -node and $D$ -node are:  

U-Node: $C_{u}=15,S_{u}=110$  

Value of [portfolio](../../../Advanced%20Investments/An%20Asset%20Allocation%20Primer.md) $V_{u}=750(\mathbb{{\mathbb{S}}}110)–1,000(\mathbb{{\mathbb{S}}}15)=\mathbb{{\mathbb{S}}}67,500$  

Return over period- $\cdot1=\S67,500/\S64,286=1.05\left(5\%\right)$  

D-Node: $C_{d}=0,S_{d}=90$  

Value of [portfolio](../../../Advanced%20Investments/An%20Asset%20Allocation%20Primer.md) $V_{d}=750\ (\S90)–1,000(0)=\S67,500$  

Return over period- $\cdot1=\S67,500/\S64,286=1.05\left(5\%\right)$  

The outcomes at the $D$ -node and $U$ -node are equal since the hedge is designed so that $V_{u}=V_{d}$ . At the $U$ -node, the new [hedge ratio](../Part%20VI%20-%20The%20Greeks/Chapter%2027%20-%20Delta%20Hedging.md) $h_{u}=0.9545$ . As we have 1,000 written options then we need to hold 954.5 stocks. Hence we buy an additional (954.5 – 750) stocks $@\$110=$ $\$22$ 4995 using borrowed funds at an interest cost $r=5\%$ . The outcomes at the UU-node and UD-node are:  

UU-node: $C_{u u}=21,S_{u u}=121$  

Value of stocks: $954.5@\mathbb{S}121=\mathbb{S}115,$ 494.50 Less (written) call payof: $1,000\ @\Phi21=\S21,000$ Less loan outstanding: $\$22,495,(1.05)$ 619.75 Value of portfolio: $V_{u u}=\S70,874.75\approx\S70,875$ Return over period- $2\colon=\S70,875/\S67,500=1.05$ (or $5\%$ )  

UD-node: $C_{u d}=0,S_{u d}=99$  

Value of stocks: $954.5@\ \mathfrak{F}99=\mathfrak{F}94$ 495.50 Less (written) call payof: $1,000\ @\Phi0=\mathfrak{H}0$ Less loan outstanding: $\$22,495$ 619.75 Value of portfolio: $V_{u u}=\S70,874.75\approx\S70,875$ Return over period- $\cdot2!=\S70,875/\S67,500=1.05\:(\mathrm{or}\:5\%)$  

To reach the $D$ -node from $t=0$ we move from holding 750 stocks $h=0.75)$ to zero stocks, since at node-D, $h_{d}=0$ . Selling 750 stocks at $S_{d}=90$ results in a cash in\$ow of $\$67,000$ . The 1,000 written calls sold at $t=0$ are worth zero, at node-DD. (Notionally, we could buy back 1,000 calls at a cost of $C_{d}=0.$ ) The cash in\$ow of $\$67,000$ is the same as $V_{d}$ calculated above.  

Explaining the move from node- $.D$ , to either node- $.D D$ or node- $U D$ is trivial. We have $h_{d}=0$ stocks which are worth zero at nodes $U D$ and $D D$ and the calls are also worth zero $\begin{array}{r}{(C_{u d}=C_{d d}=0)}\end{array}$ .  

# Changing the Number of Calls in the Hedge  

What would the hedge look like at node- $U$ if we decided to change the number of calls (rather than the number of stocks) in order to maintain the delta hedge? At node- $U$ the [hedge ratio](../Part%20VI%20-%20The%20Greeks/Chapter%2027%20-%20Delta%20Hedging.md) is $h_{u}=0.9545$ and hence a hedged [portfolio](../../../Advanced%20Investments/An%20Asset%20Allocation%20Primer.md) also consists of:  

Hold the ‘original’ 750 stocks and write 785.7 calls $(=750/0.9545)$  

At the outset we sold 1,000 calls and at node- $U$ the delta hedge requires 785.7 written calls, hence we must buy back 214.3 calls:  

At node-U buy back 214.3 calls $\textcircled{\4}\$15=\S3,214\left(=b o r r o w e d f u n d s\right)$  

We can show that [delta hedging](../../../Financial%20Instruments/Financial%20Instruments.md) by changing the number of calls produces the same outcomes as our above analysis (i.e. with a fxed 1,000 written calls). For example, the outcome at the UU-node of our ‘new’ hedge is:  

UU-node: $C_{u u}=21,S_{u u}=121$  

Value of stocks: $750\ @\mathbb{S}121=\ \mathbb{S}90,750$ Less call payof: $785.7@\$21=$ Less loan outstanding: 3 214 $(1.05)=\$3,375$ Value of [portfolio](../../../Advanced%20Investments/An%20Asset%20Allocation%20Primer.md): $V_{u u}=\mathbb{\$70,875}$ Return over period-2 $\S70,875/\S67,500=1.05(5\%)$  

This is exactly the same payof as when we hedged at node- $U$ using a fxed 1,000 written calls and [delta hedging](../../../Financial%20Instruments/Financial%20Instruments.md) with 954.5 stocks. In fact the latter is a more realistic outcome as options traders in banks tend to be net sellers of calls to their retail and corporate customers and they dynamically delta-hedge this position by changing their stock holdings, day-by-day until the maturity date of the option (or until they close out their options position prior to maturity).  

Making [arbitrage](../../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%207/Arbitrage%20Pricing%20of%20Derivatives.md) profts from a mispriced call with two periods to maturity is similar to that for the one-period case, except the ‘[arbitrage](../../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%207/Arbitrage%20Pricing%20of%20Derivatives.md) proft’ may accrue in either or both of the two periods depending on when the mispricing is corrected. Clearly if the mispricing is not corrected in the frst period, the ‘delta-hedged’ calls and stocks earn the [risk-free rate](../../../Financial%20Instruments/Black%20Scholes%20Derivation.md). But in the second period the mispricing must be corrected, since the option reaches maturity. Then a return in excess of the [risk-free rate](../../../Financial%20Instruments/Black%20Scholes%20Derivation.md) is earned between $t=1$ and $t=2$ – hence over the two periods, the arbitrageur earns more than the [risk-free rate](../../../Financial%20Instruments/Black%20Scholes%20Derivation.md).  

For example, suppose a call is initially overpriced. At $t=0$ you sell 1 call and buy $h$ stocks. If the mispricing is not corrected in period-1 then you earn the [risk-free rate](../../../Financial%20Instruments/Black%20Scholes%20Derivation.md). But if the mispricing is corrected, the call becomes correctly priced at the end of the frst period, and you earn more than the [risk-free rate](../../../Financial%20Instruments/Black%20Scholes%20Derivation.md) over period-1 – in this case you earn the [risk-free rate](../../../Financial%20Instruments/Black%20Scholes%20Derivation.md) in period-2 since the mispricing has already been corrected.  

# EXERCISES  

# Question 1  

How are the size of the ‘up’ moves $(U)$ and ‘down’ moves $(D)$ determined in the BOPM and how is the [stock price volatility](../../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%205%20Options%20on%20Prices%20and%20Hedge-Based%20Valuation/Black-Scholes%20Model%20and%20Extensions.md) represented in the tree for the BOPM?  

# Question 2  

For a [binomial tree](../../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%207/Rate%20and%20Price%20Trees.md) with $n=3$ periods there are $2^{3}=8$ possible paths to arrive at the fnal values for the [stock price](../Part%20IV%20-%20Options/Chapter%2016%20-%20Black–Scholes%20Model.md).  

(a) List these 8 diferent paths (to reach the stock prices at $n=3$ ).   
(b) How many distinct values for the [stock price](../Part%20IV%20-%20Options/Chapter%2016%20-%20Black–Scholes%20Model.md) are there at $n=3?$   
(c) How many alternative ways (paths) are there to reach a node at $n=3$ which has (i) two up moves, or (ii) two down moves, (iii) 3 up moves, (iv) 3 down moves? List these alternative paths.  

# Question 3  

In the BOPM, when [delta hedging](../../../Financial%20Instruments/Financial%20Instruments.md) an option position, why does the hedge position have to change as you move through the lattice?  

# Question 4  

In the BOPM, give an intuitive interpretation using [risk neutral](../../../Financial%20Instruments/Lecture%20Notes-%20Financial%20Instruments/Teaching%20Note%207-Exotic%20Options%20And%20Derivative%20Pricing%20By%20Monte%20Carlo%20Simulation.md) valuation, of the formula for the [put premium](../Part%20IV%20-%20Options/Chapter%2017%20-%20Option%20Strategies.md) on a stock, with two periods to expiration:  
$$
P_{0}=\frac{1}{R^{2}}[q^{2}P_{u u}+2q(1-q)P_{u d}+(1-q)^{2}P_{d d}]
$$  

where $q=(R-D)/(U-D),R=1+r$ and $r=$ [risk-free rate](../../../Financial%20Instruments/Black%20Scholes%20Derivation.md).  

# Question 5  

How can you use $\$8$ held in a risk-free asset (e.g. a zero-coupon bond or bank deposit/loan) together with $N_{0}$ stocks with current price $S_{0}$ , to replicate the payof to a one-period (long)  

European put? What does this imply for the number of stocks to buy or sell to replicate the put payof?  

Brie\$y explain what happens in your replication strategy if the stock price increases by $\$2$ (over a short time horizon).  

# Question 6  

Consider the two-period BOPM. The current [stock price](../Part%20IV%20-%20Options/Chapter%2016%20-%20Black–Scholes%20Model.md) $S=\$105$ and the risk-free rate $r=3\%$ per period (simple rate). Each period, the stock price can go either up by $10\%$ or down by $10\%$ . A European call option (on a non-dividend paying stock) with expiration at the end of two periods ${\mathrm{\Delta}n}=2{\mathrm{\Delta}}$ , has a strike price $K=\$100$ .  

(a) Draw the [stock price tree](../../../Financial%20Instruments/Assignments/Solutions/PSET%205%20Solution-Financial%20Instruments.md) (lattice).   
(b) Show that the (no-[arbitrage](../../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%207/Arbitrage%20Pricing%20of%20Derivatives.md)) price of the call is 12.47.   
(c) Calculate the [hedge ratio](../Part%20VI%20-%20The%20Greeks/Chapter%2027%20-%20Delta%20Hedging.md) at $t=0$ .   
(d) Show how you can hedge 100 written calls at $t=0$ , and how the hedge [portfolio](../../../Advanced%20Investments/An%20Asset%20Allocation%20Primer.md) earns the [risk-free rate](../../../Financial%20Instruments/Black%20Scholes%20Derivation.md) over the frst period (i.e. along the path from node $t=0$ , either to node- ${\bf\nabla}\cdot{\cal D}_{{\bf\mu}}$ or node- $U$ ).   
(e) What would an investor do at $t=0$ if the call is overpriced at $C_{g}=13?$ What is the outcome at $t=1$ (given that the [stock price](../Part%20IV%20-%20Options/Chapter%2016%20-%20Black–Scholes%20Model.md) and the [call premium](../Part%20IV%20-%20Options/Chapter%2017%20-%20Option%20Strategies.md) are the same as in the lattice in parts (a) and (b))?  

# Question 7  

Consider the two-period BOPM. The current [stock price](../Part%20IV%20-%20Options/Chapter%2016%20-%20Black–Scholes%20Model.md) $S=\$105$ and the risk-free rate $r=3\%$ per period (simple rate). Each period, the stock price can go either up by $10\%$ or down by $10\%$ . A European put option (on a non-dividend paying stock) expiring at the end of the second period has an exercise price of $K=\$100$ .  

(a) Sketch the [stock price tree](../../../Financial%20Instruments/Assignments/Solutions/PSET%205%20Solution-Financial%20Instruments.md) (lattice).   
(b) Calculate the fair (no-[arbitrage](../../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%207/Arbitrage%20Pricing%20of%20Derivatives.md)) price of the put, $P$ .   
(c) Calculate the [hedge ratio](../Part%20VI%20-%20The%20Greeks/Chapter%2027%20-%20Delta%20Hedging.md) $h$ , at time zero.   
(d) Show how you can hedge 100 long puts at $t=0$ , and how the hedge-[portfolio](../../../Advanced%20Investments/An%20Asset%20Allocation%20Primer.md) earns the [risk-free rate](../../../Financial%20Instruments/Black%20Scholes%20Derivation.md) over the frst period (i.e. along the path from node $t=0$ , either to node- ${\bf\nabla}\cdot{\cal D} $ or node- $U$ ).   
(e) What would an investor do at $t=0$ if the put is overpriced at $P_{g}=2?$ What is the outcome at $t=1$ (if the [stock price](../Part%20IV%20-%20Options/Chapter%2016%20-%20Black–Scholes%20Model.md) and the [put premium](../Part%20IV%20-%20Options/Chapter%2017%20-%20Option%20Strategies.md) are the same as in the lattice in parts (a) and (b))?  
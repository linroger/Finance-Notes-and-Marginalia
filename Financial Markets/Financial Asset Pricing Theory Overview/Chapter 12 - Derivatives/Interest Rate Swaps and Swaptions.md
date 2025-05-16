---
tags:
  - asset_transformation
  - fixed_rate
  - floating_rate
  - hedging_interest_rate_risk
  - interest_rate_swaps
  - liability_transformation
  - plain_vanilla_swap
aliases:
  - IRS
  - Interest Rate Swap
  - Swap Valuation
key_concepts:
  - Asset transformation
  - Comparative advantages
  - Fixed vs. floating rates
  - Hedging interest rate risk
  - Interest rate swap
  - Liability transformation
---

# 12.4 Interest rate swaps and swaptions  

# 12.4.1 Interest rate swaps  

Many different types of swaps are traded on the [OTC markets](../../../Fixed%20Income%20Asset%20Pricing/A%20Survey%20of%20the%20Micro%20structure%20of%20Fixed-Income%20Markets.md), e.g. [currency swaps](../../../Financial%20Instruments/Financial%20Instruments%20PSET%20Solutions.md), credit swaps,. asset swaps, but we focus here on interest rate swaps. An (interest rate) swap is an exchange of two [cash flow streams](../../../Financial%20Engineering/1.%20DeterministicCashFlows.md) that are determined by certain [interest rates](../../Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%202/Interest%20Rate%20Quotations.md). In the simplest and most common [interest rate swap](../../../Financial%20Engineering/Primer%20on%20Interest%20Rate%20Swaps.md), a plain vanilla swap, two parties exchange a stream of [fixed interest rate](../../../Financial%20Engineering/Derivatives/Part%20VIII%20-%20Swaps/Chapter%2036%20-%20Currency%20Swaps.md) payments and a stream of floating interest rate payments. The payments are in the same [currency](../../../Financial%20Instruments/Lecture%20Notes-%20Financial%20Instruments/Teaching%20Note%201-%20Forward%20Rates%20Agreement/Forwards%20and%20Futures%20Notes.md) and are computed from the same (hypothetical) face value or [notional principal](../../Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%204%20-%20Swap%20Markets/Fundamentals%20of%20Swaps.md). The foating rate is usually a money market rate, e.g. a LIBOR rate, possibly augmented or reduced by a fixed margin. The [fixed interest rate](../../../Financial%20Engineering/Derivatives/Part%20VIII%20-%20Swaps/Chapter%2036%20-%20Currency%20Swaps.md) is usually set so that the swap has zero net present value when the parties agree on the contract. While the two parties can agree upon any maturity, most interest rate swaps have a maturity between 2 and 10 years.  

Let us briefly look at the uses of interest rate swaps. An investor can transform a floating rate loan into a fixed rate loan by entering into an appropriate swap, where the investor receives floating rate payments (netting out the payments on the original loan) and pays fixed rate payments. This. is called a [liability transformation](.md). Conversely, an investor who has lent money at a floating. rate, i.e. owns a floating rate bond, can transform this to a fixed rate bond by entering into a. swap, where he pays floating rate payments and receives fixed rate payments. This is an [asset transformation](../../Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%201%20-%20Purpose%20and%20Structure%20of%20Financial%20Markets/Financial%20Institutions%20Transforming%20Intermediar.md). Hence, interest rate swaps can be used for [hedging interest rate risk](../../Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%205/Multi-Factor%20Exposures%20and%20Portfolio%20Volatility.md) on both (certain) assets and liabilities. On the other hand, interest rate swaps can also be used for taking. advantage of specific [expectations](../../../Fixed%20Income%20Asset%20Pricing/Fixed%20Income%20Lecture%20Notes/FORWARD%20RATES%20AND%20TERM%20STRUCTURE.md) of future [interest rates](../../Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%202/Interest%20Rate%20Quotations.md), i.e. for speculation..  

Swaps are often said to allow the two parties to exploit their [comparative advantages](.md) in different markets. Concerning interest rate swaps, this argument presumes that one party has a comparative advantage (relative to the other party) in the market for fixed rate loans, while the other party has a comparative advantage (relative to the first party) in the market for floating rate loans. However, these markets are integrated, and the existence of [comparative advantages](.md) conflicts with modern financial theory and the efficiency of the money markets. Apparent [comparative advantages](.md) can be due to differences in [default risk](../../Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%207%20-%20Default%20Risk%20and%20Credit%20Derivatives/Default%20Risk%20and%20Credit%20Derivatives%20183.md) premia. For details we refer the reader to the discussion in Hull (2006, Ch. 7).  

Next, we will discuss the valuation of swaps. As for [caps and floors](../../../Financial%20Engineering/Fixed%20Income%20Derivatives/Interest%20Rate%20Derivatives-An%20Introduction%20to%20the%20%20Pricing%20of%20Caps%20and%20Floors.md), we assume that both parties in the swap have a [default risk](../../Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%207%20-%20Default%20Risk%20and%20Credit%20Derivatives/Default%20Risk%20and%20Credit%20Derivatives%20183.md) corresponding to the "average [default risk](../../Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%207%20-%20Default%20Risk%20and%20Credit%20Derivatives/Default%20Risk%20and%20Credit%20Derivatives%20183.md)" of major [financial institutions](../../../Financial%20Markets%20and%20Institutions/Financial%20Markets%20and%20Institutions%20Lecture%20Notes.md) reflected by the money market [interest rates](../../Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%202/Interest%20Rate%20Quotations.md). For a description of the impact on the payments and the valuation of swaps between parties with different [default risk](../../Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%207%20-%20Default%20Risk%20and%20Credit%20Derivatives/Default%20Risk%20and%20Credit%20Derivatives%20183.md), see Duffie and Huang (1996) and Huge and Lando (1999). Furthermore, we assume that the fixed rate payments and the floating rate payments occur at exactly the same dates throughout the life of the swap. This is true for most, but not all, traded swaps. For some swaps, the fixed rate payments only occur once a year, whereas the floating rate payments are quarterly or semi-annual. The analysis below can easily be adapted to such swaps.  

In a plain vanilla [interest rate swap](../../../Financial%20Engineering/Primer%20on%20Interest%20Rate%20Swaps.md), one party pays a stream of fixed rate payments and receives. a stream of floating rate payments. This party is said to have a pay fixed, receive floating swap or a [fixed-for-floating swap](../../Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%2016/Swaptions.md) or simply a payer swap. The counterpart receives a stream of fixed rate payments and pays a stream of floating rate payments. This party is said to have a pay floating,. receive fixed swap or a floating-for-fixed swap or simply a receiver swap. Note that the names payer swap and receiver swap refer to the fixed rate payments..  

We consider a swap with payment dates. $T_{1},\dots,T_{n}$ , where $T_{i+1}-T_{i}=\delta$ . The floating interest rate determining the payment at time $T_{i}$ is the money market (LIBOR) rate $l_{T_{i}-\delta}^{T_{i}}$ . In the fllowing we assume that there is no fixed extra margin on this floating rate. If there were such an extra charge, the value of the part of the flexible payments that is due to the extra margin could be computed in the same manner as the value of the fixed rate payments of the swap, see below. We refer to $T_{0}=T_{1}-\delta$ as the starting date of the swap. As for [caps and floors](../../../Financial%20Engineering/Fixed%20Income%20Derivatives/Interest%20Rate%20Derivatives-An%20Introduction%20to%20the%20%20Pricing%20of%20Caps%20and%20Floors.md), we call $T_{0},T_{1},\dots,T_{n-1}$ the reset dates, and $\delta$ the frequency or the tenor. Typical swaps have $\delta$ equal to 0.25, 0.5, or 1 corresponding to quarterly, semi-annual, or annual payments and [interest rates](../../Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%202/Interest%20Rate%20Quotations.md).  

We will find the value of an [interest rate swap](../../../Financial%20Engineering/Primer%20on%20Interest%20Rate%20Swaps.md) by separately computing the value of the fixed rate payments ( $V^{\mathrm{{nx}}}$ ) and the value of the foating rate payments ( $V^{\mathrm{{r}}}$ ). The fixed rate is denoted by $K$ . This is a nominal, [annual interest rate](../../../Financial%20Instruments/Review%20Session%20Notes/Continuously%20Compounding%20Interest.md), so that the fixed rate payments equal $H K\delta$ , where $H$ is the [notional principal](../../Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%204%20-%20Swap%20Markets/Fundamentals%20of%20Swaps.md) or face value (which is not swapped). The value of the remaining fixed payments is simply  
$$
V_{t}^{\mathrm{fix}}=\sum_{i=i(t)}^{n}H K\delta B_{t}^{T_{i}}=H K\delta\sum_{i=i(t)}^{n}B_{t}^{T_{i}}.
$$  

The floating rate payments are exactly the same as the [coupon payments](../../Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%203/Realized%20Returns.md) on a floating rate bond with annualized coupon rate $l_{T_{i}-\delta}^{T_{i}}$ . Immediately after each reset date, the value of such a bond will equal its face value. To see this, first note that immediately after the last reset date $T_{n-1}=T_{n}-\delta$ the bond is equivalent to a zero-coupon bond with a coupon rate equal to the market interest rate for the last coupon period. By definition of that market interest rate, the time $T_{n-1}$ value of the bond will be exactly equal to the face value $H$ . In mathematical terms, the market [discount factor](../../Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%201/Discount%20Factors.md) to apply for the discounting of time $T_{n}$ payments back to time $T_{n-1}$ .9 $(1+\delta l_{T_{n-1}}^{T_{n}})^{-1}$ , so the time $T_{n-1}$ value of a payment of $H(1+\delta l_{T_{n-1}}^{T_{n}})$ at time $T_{n}$ is precisely $H$ . Immediately after the next-to-last reset date $T_{n-2}$ , we know that we will receive a payment of $H\delta l_{T_{n-2}}^{T_{n-1}^{\prime}}$ at time $T_{n-1}$ and that the time $T_{n-1}$ value of the following payment (received at $T_{n}$ ) equals $H$ . We therefore have to discount the sum $H\delta l_{T_{n-2}}^{T_{n-1}}+H=H(1+\delta l_{T_{n-2}}^{T_{n-1}})$ from $T_{n-1}$ back to $T_{n-2}$ . The discounted value is exactly $H$ . Continuing this procedure, we get that immediately after a reset of the coupon rate, the floating rate bond is valued at par. Note that it is crucial for this result that the coupon rate is adjusted to the interest rate considered by the market to be "fair." Suppose we are interested in the value at some time $t$ between $T_{0}$ and $T_{n}$ . Let $T_{i(t)}$ be the nearest following payment date after time $t$ Wkow $T_{i(t)}$ cquals $H\delta l_{T_{i(t)-1}}^{T_{i(t)}}$ time $T_{i(t)}$ of all the remaining payments will equal $H$ . The value of the bond at time $t$ will then be  
$$
B_{t}^{\mathrm{fl}}=H(1+\delta l_{T_{i(t)}-\delta}^{T_{i(t)}})B_{t}^{T_{i(t)}},\quad T_{0}\leq t<T_{n}.
$$  

This expression also holds at payment dates $t=T_{i}$ , where it results in. $H$ , which is the value.   
excluding the payment at that date..  

The value of the floating rate bond is the value of both the [coupon payments](../../Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%203/Realized%20Returns.md) and the final repayment of face value so the value of the [coupon payments](../../Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%203/Realized%20Returns.md) only must be  
$$
\begin{array}{r l}&{V_{t}^{\mathrm{H}}=H(1+\delta l_{T_{i(t)}-\delta}^{T_{i(t)}})B_{t}^{T_{i(t)}}-H B_{t}^{T_{n}}}\ &{\quad=H\delta l_{T_{i(t)}-\delta}^{T_{i(t)}}B_{t}^{T_{i(t)}}+H\left[B_{t}^{T_{i(t)}}-B_{t}^{T_{n}}\right],\quad T_{0}\leq t<T_{n}.}\end{array}
$$  

At and before time $T_{0}$ , the first term is not present, so the value of the floating rate payments is simply  
$$
\begin{array}{r}{V_{t}^{\mathrm{fl}}=H\left[B_{t}^{T_{0}}-B_{t}^{T_{n}}\right],\quad t\leq T_{0}.}\end{array}
$$  

We will also develop an alternative expression for the value of the floating rate payments of the swap. The time $T_{i}-\delta$ value of the coupon payment at time $T_{i}$ is  
$$
H\delta l_{T_{i}-\delta}^{T_{i}}B_{T_{i}-\delta}^{T_{i}}=H\delta\frac{l_{T_{i}-\delta}^{T_{i}}}{1+\delta l_{T_{i}-\delta}^{T_{i}}},
$$  

where we have applied (10.5) on page 246. Consider a strategy of buying a zero-coupon bond with face value $H$ maturing at. $T_{i}-\delta$ and selling a zero-coupon bond with the same face value $H$ but maturing at. $T_{i}$ . The time. $T_{i}-\delta$ value of this position is  
$$
H B_{T_{i}-\delta}^{T_{i}-\delta}-H B_{T_{i}-\delta}^{T_{i}}=H-\frac{H}{1+\delta l_{T_{i}-\delta}^{T_{i}}}=H\delta\frac{l_{T_{i}-\delta}^{T_{i}}}{1+\delta l_{T_{i}-\delta}^{T_{i}}},
$$  

which is identical to the value of the [floating rate payment](../../../Financial%20Instruments/Lecture%20Notes-%20Financial%20Instruments/Teaching%20Note%203%20Swaps-%20Financial%20Instruments/Overnight%20Index%20Swaps%20(OIS).md) of the swap. Therefore, the value of this [floating rate payment](../../../Financial%20Instruments/Lecture%20Notes-%20Financial%20Instruments/Teaching%20Note%203%20Swaps-%20Financial%20Instruments/Overnight%20Index%20Swaps%20(OIS).md) at any time $t\leq T_{i}-\delta$ must be  
$$
H\left(B_{t}^{T_{i}-\delta}-B_{t}^{T_{i}}\right)=H\delta B_{t}^{T_{i}}\frac{\frac{B_{t}^{T_{i}-\delta}}{B_{t}^{T_{i}}}-1}{\delta}=H\delta B_{t}^{T_{i}}L_{t}^{T_{i}-\delta,T_{i}},
$$  

where we have applied (10.6) on page 246. Thus, the value at time $t\leq T_{i}-\delta$ Of getting $H\delta l_{T_{i}-\delta}^{T_{i}^{\prime}}$ at time $T_{i}$ is equal to $H\delta B_{t}^{T_{i}}L_{t}^{T_{i}-\delta,T_{i}}$ , ie. the unknown future [spot rate](../../../International%20Finance/The%20Foreign%20Exchange%20Market%20Annotations.md) $l_{T_{i}-\delta}^{T_{i}}$ in the payff is replaced by the current [forward rate](../../../Clippings/Forward%20Points%20in%20Currency.md) for $L_{t}^{T_{i}-\delta,T_{i}}$ and then discounted by the current riskree [discount factor](../../Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%201/Discount%20Factors.md) $B_{t}^{T_{i}}$ . The value at time $t>T_{0}$ of all the remaining foating [coupon payments](../../Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%203/Realized%20Returns.md) can therefore be written as  
$$
V_{t}^{\mathrm{fl}}=H\delta B_{t}^{T_{i(t)}}l_{T_{i(t)}-\delta}^{T_{i(t)}}+H\delta\sum_{i=i(t)+1}^{n}B_{t}^{T_{i}}L_{t}^{T_{i}-\delta,T_{i}},\quad T_{0}\leq t<T_{n}.
$$  

At or before time. $T_{0}$ , the first term is not present, so we get  
$$
V_{t}^{\mathrm{{fl}}}=H\delta\sum_{i=1}^{n}B_{t}^{T_{i}}L_{t}^{T_{i}-\delta,T_{i}},\quad t\leq T_{0}.
$$  

The value of a payer swap is  
$$
\mathbf{P}_{t}=V_{t}^{\mathrm{fl}}-V_{t}^{\mathrm{fix}},
$$  

while the value of a receiver swap is  
$$
\mathbf{R}_{t}=V_{t}^{\mathrm{fix}}-V_{t}^{\mathrm{fl}}.
$$  

In particular, the value of a payer swap at or before its starting date $T_{0}$ can be written as  
$$
{\bf P}_{t}=H\delta\sum_{i=1}^{n}B_{t}^{T_{i}}\left(L_{t}^{T_{i}-\delta,T_{i}}-K\right),\quad t\le T_{0},
$$  

using (12.46) and (12.50), or as  
$$
\mathbf{P}_{t}=H\left(\left[B_{t}^{T_{0}}-B_{t}^{T_{n}}\right]-\sum_{i=1}^{n}K\delta B_{t}^{T_{i}}\right),\quad t\leq T_{0},
$$  

using (12.46) and (12.48). If we let $Y_{i}~=~K\delta$ for $i=1,\ldots,n-1$ and $Y_{n}=1+K\delta$ , we can rewrite (12.52) as  
$$
\mathbf{P}_{t}=H\left(B_{t}^{T_{0}}-\sum_{i=1}^{n}Y_{i}B_{t}^{T_{i}}\right),\quad t\leq T_{0}.
$$  

Also note the following relation between a cap, a floor, and a payer swap having the same payment. dates and where the cap rate, the floor rate, and the fixed rate in the swap are all identical:  
$$
\begin{array}{r}{\mathscr{C}_{t}=\mathscr{F}_{t}+\mathbf{P}_{t}.}\end{array}
$$  

This follows from the fact that the payments from a [portfolio](../../../Advanced%20Investments/An%20Asset%20Allocation%20Primer.md) of a floor and a payer swap exactly match the payments of a cap.  

The [swap rate](../../../Fixed%20Income%20Asset%20Pricing/Fixed%20Income%20Lecture%20Notes/Teaching%20Note%204%20Interest%20Rate%20Derivatives.md). $\ddot{l}_{T_{0}}^{\delta}$ prevailing at time $T_{0}$ for a swap with frequency $\delta$ and payments dates. $T_{i}=T_{0}+i\delta$ $i=1,2,\dots,n$ , is defined as the unique value of the fixed rate that makes the present value of a swap starting at $T_{0}$ equal to zero, i.e.. $\mathbf{P}_{T_{0}}=\mathbf{R}_{T_{0}}=0$ . The [swap rate](../../../Fixed%20Income%20Asset%20Pricing/Fixed%20Income%20Lecture%20Notes/Teaching%20Note%204%20Interest%20Rate%20Derivatives.md) is sometimes called the equilibrium [swap rate](../../../Fixed%20Income%20Asset%20Pricing/Fixed%20Income%20Lecture%20Notes/Teaching%20Note%204%20Interest%20Rate%20Derivatives.md) or the [par swap](../../../Financial%20Engineering/Fixed%20Income%20Derivatives/Determining%20the%20Expression%20for%20the%20Fair%20Value%20of%20the%20Swap%20Spread.md) rate. Applying (12.51), we can write the [swap rate](../../../Fixed%20Income%20Asset%20Pricing/Fixed%20Income%20Lecture%20Notes/Teaching%20Note%204%20Interest%20Rate%20Derivatives.md) as  
$$
\tilde{l}_{T_{0}}^{\delta}=\frac{\sum_{i=1}^{n}L_{T_{0}}^{T_{i}-\delta,T_{i}}B_{T_{0}}^{T_{i}}}{\sum_{i=1}^{n}B_{T_{0}}^{T_{i}}},
$$  

which can also be written as a weighted average of the relevant forward rates:  
$$
\tilde{l}_{T_{0}}^{\delta}=\sum_{i=1}^{n}w_{i}L_{T_{0}}^{T_{i}-\delta,T_{i}},
$$  

where $\begin{array}{r}{w_{i}=B_{T_{0}}^{T_{i}}/\sum_{i=1}^{n}B_{T_{0}}^{T_{i}}}\end{array}$ . Alternatively, we can let $t=T_{0}$ in (12.52) yielding  
$$
{\bf P}_{T_{0}}={\cal H}\left(1-B_{T_{0}}^{T_{n}}-K\delta\sum_{i=1}^{n}B_{T_{0}}^{T_{i}}\right),
$$  

so that the [swap rate](../../../Fixed%20Income%20Asset%20Pricing/Fixed%20Income%20Lecture%20Notes/Teaching%20Note%204%20Interest%20Rate%20Derivatives.md) can be expressed as  
$$
\tilde{l}_{T_{0}}^{\delta}=\frac{1-B_{T_{0}}^{T_{n}}}{\delta\sum_{i=1}^{n}B_{T_{0}}^{T_{i}}}.
$$  

Substituting (12.56) into the expression just above it, the time $T_{0}$ value of an agreement to pay a fixed rate $K$ and receive the prevailing market rate at each of the dates $T_{1},\dots,T_{n}$ , can be written in terms of the current [swap rate](../../../Fixed%20Income%20Asset%20Pricing/Fixed%20Income%20Lecture%20Notes/Teaching%20Note%204%20Interest%20Rate%20Derivatives.md) as  
$$
\begin{array}{l}{{\displaystyle{\bf P}_{T_{0}}=H\left(\tilde{l}_{T_{0}}^{\delta}\delta\left(\sum_{i=1}^{n}B_{T_{0}}^{T_{i}}\right)-K\delta\left(\sum_{i=1}^{n}B_{T_{0}}^{T_{i}}\right)\right)}}\ {{\displaystyle~=\left(\sum_{i=1}^{n}B_{T_{0}}^{T_{i}}\right)H\delta\left(\tilde{l}_{T_{0}}^{\delta}-K\right).}}\end{array}
$$  

A [forward swap](../../../Financial%20Engineering/Derivatives/Part%20IX%20-%20Fixed%20Income%20Derivatives/Chapter%2039%20-%20Swaptions,%20Forward%20Swaps,%20and%20MBS.md) (or deferred swap) is an agreement to enter into a swap with a future starting date $T_{0}$ and a fixed rate which is already set. Of course, the contract also fixes the frequency, the maturity, and the [notional principal](../../Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%204%20-%20Swap%20Markets/Fundamentals%20of%20Swaps.md) of the swap. The value at time $t\leq T_{0}$ of a forward payer swap with fixed rate $K$ is given by the equivalent expressions (12.51)-(12.53). The [forward swap](../../../Financial%20Engineering/Derivatives/Part%20IX%20-%20Fixed%20Income%20Derivatives/Chapter%2039%20-%20Swaptions,%20Forward%20Swaps,%20and%20MBS.md) rate $\tilde{L}_{t}^{\delta,T_{0}}$ is defined as the value of the fixed rate that makes the [forward swap](../../../Financial%20Engineering/Derivatives/Part%20IX%20-%20Fixed%20Income%20Derivatives/Chapter%2039%20-%20Swaptions,%20Forward%20Swaps,%20and%20MBS.md) have zero value at time $t$ . The [forward swap](../../../Financial%20Engineering/Derivatives/Part%20IX%20-%20Fixed%20Income%20Derivatives/Chapter%2039%20-%20Swaptions,%20Forward%20Swaps,%20and%20MBS.md) rate can be written as  
$$
\tilde{L}_{t}^{\delta,T_{0}}=\frac{B_{t}^{T_{0}}-B_{t}^{T_{n}}}{\delta\sum_{i=1}^{n}B_{t}^{T_{i}}}=\frac{\sum_{i=1}^{n}L_{t}^{T_{i}-\delta,T_{i}}B_{t}^{T_{i}}}{\sum_{i=1}^{n}B_{t}^{T_{i}}}.
$$  

Note that both the [swap rate](../../../Fixed%20Income%20Asset%20Pricing/Fixed%20Income%20Lecture%20Notes/Teaching%20Note%204%20Interest%20Rate%20Derivatives.md) and the [forward swap](../../../Financial%20Engineering/Derivatives/Part%20IX%20-%20Fixed%20Income%20Derivatives/Chapter%2039%20-%20Swaptions,%20Forward%20Swaps,%20and%20MBS.md) rate depend on the frequency and the maturity of the underlying swap. To indicate this dependence, let. $\ddot{l}_{t}^{\delta}(n)$ denote the time $t$ [swap rate](../../../Fixed%20Income%20Asset%20Pricing/Fixed%20Income%20Lecture%20Notes/Teaching%20Note%204%20Interest%20Rate%20Derivatives.md) for a swap with payment dates $T_{i}=t+i\delta$ $i=1,2,\dots,n$ . If we depict the [swap rate](../../../Fixed%20Income%20Asset%20Pricing/Fixed%20Income%20Lecture%20Notes/Teaching%20Note%204%20Interest%20Rate%20Derivatives.md) as a function of the maturity, i.e. the function $n\mapsto{\bar{l}}_{t}^{\delta}(n)$ (only defined for $n=1,2,\ldots$ ), we get a [term structure](../../Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%209/The%20Vasicek%20Model.md) of swap rates for the given frequency. Many [financial institutions](../../../Financial%20Markets%20and%20Institutions/Financial%20Markets%20and%20Institutions%20Lecture%20Notes.md) participating in the swap market will offer swaps of varying maturities under conditions reflected by their posted [term structure](../../Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%209/The%20Vasicek%20Model.md) of swap rates. In Exercise 12.7, you are asked to show how the discount factors. $B_{T_{0}}^{T_{i}^{\prime}}$ can be derived from a [term structure](../../Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%209/The%20Vasicek%20Model.md) of swap rates.  

# 12.4.2 Swaptions  

A swaption is an option on a swap. A European swaption gives its holder the right, but not the obligation, at the expiry date. $T_{0}$ to enter into a specific [interest rate swap](../../../Financial%20Engineering/Primer%20on%20Interest%20Rate%20Swaps.md) that starts at $T_{0}$ and has a given fixed rate $K$ . No [exercise price](Options.md) is to be paid if the right is utilized. The rate $K$ is sometimes referred to as the exercise rate of the swaption. We distinguish between a [payer swaption](../../../Financial%20Engineering/Derivatives/Part%20IX%20-%20Fixed%20Income%20Derivatives/Chapter%2039%20-%20Swaptions,%20Forward%20Swaps,%20and%20MBS.md), which gives the right to enter into a payer swap, and a receiver swaption, which gives the right to enter into a receiver swap. As for [caps and floors](../../../Financial%20Engineering/Fixed%20Income%20Derivatives/Interest%20Rate%20Derivatives-An%20Introduction%20to%20the%20%20Pricing%20of%20Caps%20and%20Floors.md), two different [pricing](../../Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%207/Arbitrage%20Pricing%20of%20Derivatives.md) strategies can be taken. One strategy is to link the swaption payoff to the payoff of another well-known derivative. The other strategy is to directly take relevant [expectations](../../../Fixed%20Income%20Asset%20Pricing/Fixed%20Income%20Lecture%20Notes/FORWARD%20RATES%20AND%20TERM%20STRUCTURE.md) of the swaption payoff.  

Let us first see how we can link swaptions to options on bonds. Let us focus on a European receiver swaption. At time. $T_{0}$ , the value of a receiver swap with payment dates $T_{i}=T_{0}+i\delta$ $i=1,2,\dots,n$ , and a fixed rate. $K$ is given by  
$$
\mathbf{R}_{T_{0}}=H\left(\sum_{i=1}^{n}Y_{i}B_{T_{0}}^{T_{i}}-1\right),
$$  

where $Y_{i}=K\delta$ for $i=1,\ldots,n-1$ and $Y_{n}=1+K\delta$ ; cf. (12.53). Hence, the time $T_{0}$ payoff of a receiver swaption is  
$$
\mathcal{R}_{T_{0}}=\operatorname*{max}\left(\mathbf{R}_{T_{0}}-0,0\right)=H\operatorname*{max}\left(\sum_{i=1}^{n}Y_{i}B_{T_{0}}^{T_{i}}-1,0\right),
$$  

which is equivalent to the payoff of $H$ European call options on a bullet bond with face value 1, $n$ payment dates, a period of $\delta$ between successive payments, and an annualized coupon rate $K$ The [exercise price](Options.md) of each option equals the face value 1. The price of a European receiver swaption must therefore be equal to the price of these call options. In many models of interest rate dynamics, we can compute such prices quite easily. For the [Vasicek model](../../../Fixed%20Income%20Asset%20Pricing/Fixed%20Income%20Lecture%20Notes/Vasicek%20Short%20Rate%20Model.md), the swaption prices follow from Equation 12.29 and Theorem 12.8.  

Similarly, a European [payer swaption](../../../Financial%20Engineering/Derivatives/Part%20IX%20-%20Fixed%20Income%20Derivatives/Chapter%2039%20-%20Swaptions,%20Forward%20Swaps,%20and%20MBS.md) yields a payoff of  
$$
\mathcal{P}_{T_{0}}=\operatorname*{max}\left(\mathbf{P}_{T_{0}}-0,0\right)=\operatorname*{max}\left(-\mathbf{R}_{T_{0}},0\right)=H\operatorname*{max}\left(1-\sum_{i=1}^{n}Y_{i}B_{T_{0}}^{T_{i}},0\right).
$$  

This is identical to the payoff from $H$ European put options expiring at $T_{0}$ and having an exercise.   
price of 1 with a bond paying. $Y_{i}$ at time $T_{i}$ $i=1,2,\dots,n$ , as its [underlying asset](../../../Financial%20Instruments/Financial%20Derivatives%20and%20Quantitative%20Methods/Risk%20Neutral%20Pricing%20of%20Options.md)..  

Alternatively, we can apply (12.57) to express the payoff of a European [payer swaption](../../../Financial%20Engineering/Derivatives/Part%20IX%20-%20Fixed%20Income%20Derivatives/Chapter%2039%20-%20Swaptions,%20Forward%20Swaps,%20and%20MBS.md) as  
$$
\mathcal{P}_{T_{0}}=\left(\sum_{i=1}^{n}B_{T_{0}}^{T_{i}}\right)H\delta\operatorname*{max}\left(\tilde{l}_{T_{0}}^{\delta}-K,0\right),
$$  

where $\ddot{l}_{T_{0}}^{\delta}$ is the (equilibrium) [swap rate](../../../Fixed%20Income%20Asset%20Pricing/Fixed%20Income%20Lecture%20Notes/Teaching%20Note%204%20Interest%20Rate%20Derivatives.md) prevailing at time $T_{0}$ . What is an appropriate numeraire. for [pricing](../../Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%207/Arbitrage%20Pricing%20of%20Derivatives.md) this swaption? If we were to use the zero-coupon bond maturing at $T_{0}$ as the numeraire,. we would have to find the expectation of the payoff ${\mathcal{P}}_{T_{0}}$ under the $T_{0}$ -[forward martingale measure](Options.md). $\mathbb{Q}^{T_{0}}$ . But since the payoff depends on several different bond prices, the distribution of ${\mathcal{P}}_{T_{0}}$ under $\mathbb{Q}^{T_{0}}$ is rather complicated. It is more convenient to use another numeraire, namely the annuity bond, which at each of the dates. $T_{1},\dots,T_{n}$ provides a payment of 1 dollar. The value of this annuity at time $t\leq T_{0}$ equals $\begin{array}{r}{G_{t}=\sum_{i=1}^{n}B_{t}^{T_{i}^{\prime}}}\end{array}$ . In particular, the payoff of the swaption can be restated as  
$$
\begin{array}{r}{\mathcal{P}_{T_{0}}=G_{T_{0}}H\delta\operatorname*{max}\left(\tilde{l}_{T_{0}}^{\delta}-K,0\right),}\end{array}
$$  

and the payoff expressed in units of the annuity bond is simply $H\delta\operatorname*{max}\left(\tilde{l}_{T_{0}}^{\delta}-K,0\right)$ . The riskadjusted probability measure corresponding to the annuity being the numeraire is sometimes called the swap martingale measure and will be denoted by $\mathbb{Q}^{G}$ in the following. The price of the European [payer swaption](../../../Financial%20Engineering/Derivatives/Part%20IX%20-%20Fixed%20Income%20Derivatives/Chapter%2039%20-%20Swaptions,%20Forward%20Swaps,%20and%20MBS.md) can now be written as  
$$
\boldsymbol{\mathcal{P}}_{t}=G_{t}\mathrm{E}_{t}^{\boldsymbol{\mathbb{Q}}^{G}}\left[\frac{\mathcal{P}_{T_{0}}}{G_{T_{0}}}\right]=G_{t}H\delta\mathrm{E}_{t}^{\boldsymbol{\mathbb{Q}}^{G}}\left[\operatorname*{max}\left(\tilde{l}_{T_{0}}^{\delta}-K,0\right)\right],
$$  

so we only need to know the distribution of the [swap rate](../../../Fixed%20Income%20Asset%20Pricing/Fixed%20Income%20Lecture%20Notes/Teaching%20Note%204%20Interest%20Rate%20Derivatives.md) $\ddot{l}_{T_{0}}^{\delta}$ under the swap martingale measure. In the so-called looral [swap rate](../../../Fixed%20Income%20Asset%20Pricing/Fixed%20Income%20Lecture%20Notes/Teaching%20Note%204%20Interest%20Rate%20Derivatives.md) model inroduced by Jamshidian (1997, the swap rat $\ddot{l}_{T_{0}}^{\delta}$ assumed to be lognormally distributed under the $\mathbb{Q}^{G}$ -measure and the resulting [swaption pricing](../../Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%2016/Swaptions.md) formula is identical to the Black formula for swaptions often applied by practitioners:  
$$
\mathcal{P}_{t}=H\delta\left(\sum_{i=1}^{n}B_{t}^{T_{i}}\right)\bigg[\tilde{L}_{t}^{\delta,T_{0}}N\left(d(\tilde{L}_{t}^{\delta,T_{0}},t)\right)-K N\left(d(\tilde{L}_{t}^{\delta,T_{0}},t)-\tilde{\sigma}\right)\bigg],\quad t<T_{0},
$$  

where $\tilde{\sigma}$ is the (relative) volatility of the foward [swap rate](../../../Fixed%20Income%20Asset%20Pricing/Fixed%20Income%20Lecture%20Notes/Teaching%20Note%204%20Interest%20Rate%20Derivatives.md) $\tilde{L}_{t}^{\partial,^{\prime}L_{0}^{\prime}}$ and  
$$
d(\tilde{L}_{t}^{\delta,T_{0}},t)=\frac{\ln(\tilde{L}_{t}^{\delta,T_{0}}/K)}{\tilde{\sigma}\sqrt{T_{0}-t}}+\frac{1}{2}\tilde{\sigma}\sqrt{T_{0}-t}.
$$  

See Munk (2005, Ch. 11) for a presentation and discussion of the lognormal [swap rate](../../../Fixed%20Income%20Asset%20Pricing/Fixed%20Income%20Lecture%20Notes/Teaching%20Note%204%20Interest%20Rate%20Derivatives.md) model.  

Similar to the [put-call parity](../../../Financial%20Engineering/7.%20Black%20Scholes%20Model.md) for options we have the following payer-receiver parity for [European swaptions](../../Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%206%20Options%20on%20Non-Price%20Variables/Black%20Models%20for%20Bond%20Price%20Options%20Capsfloors.md) having the same underlying swap and the same exercise rate:.  
$$
\begin{array}{r}{\mathcal{P}_{t}-\mathcal{R}_{t}=\mathbf{P}_{t},\quad t\leq T_{0},}\end{array}
$$  

cf. Exercise 12.8. In words, a [payer swaption](../../../Financial%20Engineering/Derivatives/Part%20IX%20-%20Fixed%20Income%20Derivatives/Chapter%2039%20-%20Swaptions,%20Forward%20Swaps,%20and%20MBS.md) minus a receiver swaption is indistinguishable from a forward payer swap.  
---
tags:
  - bond_duration
  - convexity
  - spot_rates
  - yield_curve
  - ytm
aliases:
  - Bond Pricing
  - Chapter 10
  - Duration
  - Yield Curve
key_concepts:
  - Convexity adjustment
  - Duration and bond price
  - Parallel shift in yield curve
  - Spot rates and yield curve
  - YTM changes and bond prices
---
# Bonds: Duration and Convexity  

# Aims  

• To demonstrate how spot-rates for diferent maturities give rise to the (spot) yield curve. • To show how [duration and convexity](../../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%208/An%20Analytical%20Decomposition%20of%20Forward%20Rates.md) can be used to provide an approximation to the change in bond prices, after a change in the yield to maturity (YTM).  

# 10.1 YIELD CURVE  

Investors borrow (and lend) money over diferent periods of time. For example, to borrow money today and pay back the principal and interest in 1 year’s time, the cost of borrowing might be $r_{1}=9\%$ p.a. To borrow today and pay back the principal and interest in 2 years’ time (i.e. there are no interim payments), then the quoted interest rate might be $r_{2}=10\%$ p.a. Because each of these [interest rates](../../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%202/Interest%20Rate%20Quotations.md) are quoted for borrowing from today, over a fxed horizon (with no interim payments), they are known as spot-rates (or spot yields).  

The (spot) yield curve shows the relationship between (spot) [interest rates](../../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%202/Interest%20Rate%20Quotations.md) for diferent maturity investments. We assume we are dealing with risk-free investments – there is no risk of default. For example, the yield curve at $10\mathrm{a.m}$ . today might look like that in Figure 10.1. The yield curve in Figure 10.1 is upward sloping, which simply means that if you borrow money at $10\mathrm{a.m}$ . today then the longer the maturity of your loan, the higher the (spot) interest you will pay. Note that spot-rates apply to a transaction that is conceptually diferent from a ‘standard loan’. In a standard loan, the repayments schedule will include interim payments and therefore the interest rate charged cannot be called a [spot rate](../../../International%20Finance/The%20Foreign%20Exchange%20Market%20Annotations.md).  

Spot-rates at any one time are determined in the market by the interplay of the supply of funds by lenders and the demand for funds by borrowers. As the supply and demand for funds changes, then spot-rates will change and the yield curve will alter its shape or position.  

Usually, if there is a change in [demand and supply](../../../International%20Finance/China%20Foreign%20Exchange%20Reserves/Currency%20Appreciation%20and%20Depreciation.md) of funds at a particular horizon (e.g. lending over 2 years) then this will also infuence the supply and demand at all other horizons. For example, if $r_{2}$ increases then all other spot-rates will also tend to increase – the correlation coe\$cient between changes in any two spot-rates (with diferent maturities) over a short horizon (e.g. 1 week) is very high, usually in excess of 0.9. Although spot-rates tend to move up and down together, they do not all move by the same absolute amount. In general ‘long-rates’ tend to move less than ‘short-rates’. For example, if the 1-year rate increases by $1\%$ (e.g. from $3\%$ to $4\%$ ) over the next week, the 3-year rate might only increase by $0.95\%$ (see curve BB, in Figure 10.1). However, if all spot-rates do happen to move up or down by the same absolute amount this is called a parallel shift in the yield curve.  

We have described spot-yields in terms of [borrowing and lending](../../../Financial%20Instruments/Lecture%20Notes-%20Financial%20Instruments/Teaching%20Note%203%20Swaps-%20Financial%20Instruments/Swaps%20Types.md) money over specifc horizons. This can be done by buying a zero-coupon bond (i.e. lending money) or issuing (selling) a ‘zero’ (i.e. borrowing money), so spot-rates can be inferred by observing the market price of zeros. For example, if the market price on a 2-year zero is $P=\$92$ which pays $M=\$100$ in 2 years’ time then the 2-year spot-rate is $4.26\%$ p.a. (Calculated using $(1+r)^{2}=M/P=100/92$ . Pure discount government bonds for long maturities do not exist but spot yields can be derived from data on a set of coupon paying bonds (and from swap rates).  

Usually the spot-yield curve is upward sloping and fattens out at long maturities. But sometimes it is downward sloping – which implies it costs less to borrow money over say 5 years than it does over one year.  

So far we have merely described what the yield curve represents. It tells you how much it will cost you (p.a.) to borrow (or lend) money over a fxed horizon, starting immediately (and with no interim payments). But what determines the shape of the yield curve at any point in time? This analysis is known as the [term structure of interest rates](../../6.%20A%20Brief%20Introduction%20to%20Stochastic%20Calculus.md) and broadly speaking the shape of the yield curve today is determined by the market’s [expectations](../../../Fixed%20Income%20Asset%20Pricing/Fixed%20Income%20Lecture%20Notes/FORWARD%20RATES%20AND%20TERM%20STRUCTURE.md) about price infation in future years. If today, infation is expected to be higher (lower), in each future year then the yield curve will be upward (downward) sloping (see Cuthbertson and Nitzsche 2008).  

![](27ef0878130a9d612dd04ca53f4b2c0a9916119b1a159370bd2e3260cf5a88f0.jpg)  
FIGURE 10.1 Yield curve  

# 10.1.1 Estimating Yield Curves  

There are many diferent types of ‘yield curve’ but all of them are a graph of some measure of ‘yield’ against maturity (e.g. spot-yield curve, forward-yield curve). There are a wide range of coupon paying bonds with diferent payment dates, maturities, diferent tax treatment, etc. Also some maturities may be traded in illiquid markets so that ‘posted’ prices may not be representative of prices at which you can actually trade these bonds. Hence not all spot yields will lie exactly on a smooth curve and some statistical methods are required to ft a smooth curve to observed data on spot yields. A popular method is the cubic spline technique. Here, separate curves are ftted to various sections of the yield curve (e.g. for rates between 1 and 5-year maturities, then between 5 and 10-year maturities, etc.) and these separate curves are smoothly joined at each of the intersection (‘knot’) points of the separate curves (e.g. at 5-year maturity, 10-year maturity, etc.), so the whole curve is smooth but has diferent slopes for each section.  

# 10.2 DURATION AND CONVEXITY  

The [duration](../../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%205/Key%20Rates%20O1s%20Durations%20and%20Hedging.md) $D$ of a bond is a ‘summary statistic’ which can be used to tell us (approximately) how much the bond price will change, after a change in the yield to maturity (YTM). For example, consider a speculator who currently holds a coupon paying bond with 7 years to maturity, a current market value of $\$1,000$ and which has a duration of $D=5$ . Suppose the YTM moves from $6\%$ to $5.5\%$ over the next week, that is the absolute change in the YTM is $d y=-0.5\%$ . Then the price of the bond will rise by approximately $2.5\%$ over the next week, since it can be shown that:1  
$\%$ change in bond price $\approx-D\times$ absolute change in  
$$
\%(d P/P)\approx-D~d y=-5~(-1/2)\%=+2.5\%
$$  

The minus sign in the above formula captures the fact that a fall (rise) in the YTM leads to a rise (fall) in the bond price. Note that the [duration](../../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%205/Key%20Rates%20O1s%20Durations%20and%20Hedging.md) formula only gives an approximation to the change in price – the actual (or ‘true’) change in price will difer from that given by the [duration](../../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%205/Key%20Rates%20O1s%20Durations%20and%20Hedging.md) formula – but the approximation is quite accurate for small changes in yields (e.g. 25 bps). If we require a more accurate measure of the change in price we need to incorporate a ‘[convexity](../../../Fixed%20Income%20Asset%20Pricing/Problem%20Sets/PSET%20II%20Fixed%20Income%20Asset%20Pricing%201.md)’ adjustment (see below) or use the present value [pricing equation](../../../Financial%20Markets/Financial%20Asset%20Pricing%20Theory%20Overview/Chapter%204%20-%20State%20Prices/Definitions%20and%20Immediate%20Consequences.md) (see Chapter 9).  

The [duration](../../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%205/Key%20Rates%20O1s%20Durations%20and%20Hedging.md) formula also assumes that yields at all maturities move by the same (absolute) amount – that is, a parallel shift in the yield curve.  

According to the [duration](../../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%205/Key%20Rates%20O1s%20Durations%20and%20Hedging.md) formula, the change in value of the bond will be around $2.5\%$ of its current market value of $\$1,000$ , that is an increase of $\$25$ , so the price of the bond at the end of the week will be close to $\$1,025$ . Clearly, [duration](../../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%205/Key%20Rates%20O1s%20Durations%20and%20Hedging.md) is useful for fxed-income traders who speculate on changes in [interest rates](../../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%202/Interest%20Rate%20Quotations.md) – the larger the [duration](../../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%205/Key%20Rates%20O1s%20Durations%20and%20Hedging.md) of the bond, the greater the percentage change in the bond price and hence the greater the (‘market’) risk of the bond.  

The relationship between the ‘true’ change in bond price and the change in YTM is shown in Figure 10.2 by the curved or ‘convex’ line. The approximate change in price, given by the [duration](../../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%205/Key%20Rates%20O1s%20Durations%20and%20Hedging.md) formula is represented by the ‘tangent line’ (at the current yield of $5\%$ ). Any actual price rise will exceed that given by the [duration](../../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%205/Key%20Rates%20O1s%20Durations%20and%20Hedging.md) equation – and any actual price fall will be less than that calculated using [duration](../../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%205/Key%20Rates%20O1s%20Durations%20and%20Hedging.md). For small changes in yield, the actual price change and the approximated price change – that given using the [duration](../../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%205/Key%20Rates%20O1s%20Durations%20and%20Hedging.md) formula – will be very close because the ‘curve’ and the ‘straight line’ coincide.  

# 10.2.1 Duration of a Portfolio of Bonds  

Suppose you hold $N$ -bonds. The [duration](../../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%205/Key%20Rates%20O1s%20Durations%20and%20Hedging.md) of a [portfolio](../../../Advanced%20Investments/An%20Asset%20Allocation%20Primer.md) of $N$ -bonds is simply a weighted average of the [duration](../../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%205/Key%20Rates%20O1s%20Durations%20and%20Hedging.md) of the constituent bonds in the [portfolio](../../../Advanced%20Investments/An%20Asset%20Allocation%20Primer.md), where the weights $w_{i}$ are determined by the market value of the individual bonds:  
$$
D_{p}=\sum_{i=1}^{N}w_{i}D_{i}
$$  

where (assuming no short-selling) $0<w_{i}<1$ and $\Sigma w_{i}=1$ . For example, if you hold $\$2000$ in bonds, each of which has a duration $D=4$ and $\$4000$ in bonds each with a [duration](../../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%205/Key%20Rates%20O1s%20Durations%20and%20Hedging.md) of $D=12$ , then the [duration](../../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%205/Key%20Rates%20O1s%20Durations%20and%20Hedging.md) of the bond [portfolio](../../../Advanced%20Investments/An%20Asset%20Allocation%20Primer.md) is $D_{p}=\left({200}/{600}\right)4+\left({400}/{600}\right)12=9.33$ .  

![](4a1414ec27618731f96283a7da06cf84bfa5e12c462737dba9d47a4ea6965c00.jpg)  
FIGURE 10.2 [Duration](../../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%205/Key%20Rates%20O1s%20Durations%20and%20Hedging.md) and price changes  

This implies that if bond yields change by $1\%$ , the value of your bond [portfolio](../../../Advanced%20Investments/An%20Asset%20Allocation%20Primer.md) will change by (approximately) 9.33 per cent, hence:  
$$
\S{\mathrm{-change~in~value~of~bond~portfolio~:~}}d V_{p}\approx V_{p}(D_{p}d y)
$$  

where $d y$ , the change in the YTM, is expressed as a decimal (e.g. if the current YTM is $3\%$ p.a. and falls to $2\%$ p.a. over 1 week then $d y=-0.01\rangle$ ). For a $1\%$ fall in the YTM over 1 week, the (approximate) change in the (dollar) value of the bond [portfolio](../../../Advanced%20Investments/An%20Asset%20Allocation%20Primer.md) (over 1 week) is $d V_{p}(=$ $\$600\times9.3333\times0.01)=\S56$ .  

It can be shown that the formula for $D$ for an $n$ -period coupon paying bond (annual payments), where $y$ is measured as a ‘compound yield’ (decimal) is:  
$$
D={\frac{[P V(C_{1})1+P V(C_{2})2+\ldots+P V(C_{n}+M)T]}{P}}
$$  

where the present value of each coupon payment at time $t_{:}$ , is $P V(C_{t})=C_{t}/(1+y)^{t}$ . In Equation (10.4) the present value of each coupon payment is ‘weighted’ by the ‘time’ at which the coupon is received $t=1$ 2 $T$ . Hence, the [duration](../../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%205/Key%20Rates%20O1s%20Durations%20and%20Hedging.md) of a bond is sometimes described as a ‘time weighted average term to maturity of the bond’. However, what is important is that today, the [duration](../../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%205/Key%20Rates%20O1s%20Durations%20and%20Hedging.md) of any bond can be calculated using (10.4) and an approximate change in the bond price is then given by Equation (10.1) (or Equation (10.5) below).  

[Duration](../../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%205/Key%20Rates%20O1s%20Durations%20and%20Hedging.md) is a useful summary statistic for calculating (approximate) changes in bond prices but what factors determine the [duration](../../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%205/Key%20Rates%20O1s%20Durations%20and%20Hedging.md) of a coupon paying bond? Some useful ‘rules of thumb’ are: (a) [duration](../../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%205/Key%20Rates%20O1s%20Durations%20and%20Hedging.md) generally increases with [time to maturity](../../../Financial%20Instruments/Lecture%20Notes-%20Financial%20Instruments/Teaching%20Note%201-%20Forward%20Rates%20Agreement/Hedging%20Strategies%20with%20Forwards.md) (always does so for bonds selling at or above par); (b) [duration](../../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%205/Key%20Rates%20O1s%20Durations%20and%20Hedging.md) is higher the lower is the coupon rate $(C/M)$ ; and (c) [duration](../../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%205/Key%20Rates%20O1s%20Durations%20and%20Hedging.md) is (usually) higher when the YTM is low.  

Above we have used the ‘compound yield’ $y$ in the [duration](../../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%205/Key%20Rates%20O1s%20Durations%20and%20Hedging.md) formula and when this is the case it can be shown (see Appendix 10) that for small changes in (compound) yields, the proportionate change in the bond price is actually given by:  
$$
\frac{d P}{P}=-D\frac{d y}{(1+y)}=-(M D)d y
$$  

where ‘modifed [duration](../../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%205/Key%20Rates%20O1s%20Durations%20and%20Hedging.md)’ is defned as $M D=D/(1+y)$ . Equation (10.5) is a little more involved than our original formula, Equation (10.1) because of the inclusion of the term $(1+y)$ in the denominator. Also note that in using this equation we have to express $y$ as a proportion – so a yield of $5\%$ would appear in this formula as $y=0.05$ and an increase in the yield of $1\%$ (over 1 week, say) would imply $d y=0.01$ . If $D=5$ , then the proportionate change in price is $d P/P=-5(0.01)/(1.05)=-0.0476,$ that is, a price fall of $4.76\%$ . $D$ (when calculated using compound yields as above) is known as [Macaulay duration](../../../Fixed%20Income%20Asset%20Pricing/Fixed%20Income%20Lecture%20Notes/Teaching%20Note%202-%20Interest%20Rate%20Risk%20Management%20And%20Factors.md). Calculation of [duration](../../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%205/Key%20Rates%20O1s%20Durations%20and%20Hedging.md) for a coupon bond is illustrated in Example 10.1, along with the approximate price change using the [duration](../../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%205/Key%20Rates%20O1s%20Durations%20and%20Hedging.md) formula. [Duration](../../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%205/Key%20Rates%20O1s%20Durations%20and%20Hedging.md) provides a good approximation to the change in price of a bond for parallel shifts in the yield curve and for small changes in yields (of up to $25{\mathrm{~bp}}^{\cdot}$ ).  

# EXAMPLE 10.1  

# Calculation of Duration  

Data: 5 years to maturity, $4.5\%$ coupon (annual), $M=\S100,\mathrm{YTM}=3.5\%$  

Question: Calculate [duration](../../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%205/Key%20Rates%20O1s%20Durations%20and%20Hedging.md) and the approximate change in the price of the bond if the YTM increases to $4\%$ (over 1 week).  

Answer: Current price  
$$
\begin{array}{l}{P=\S4.50/(1.035)+\S4.50/(1.035)^{2}+\dots+\S104.50/(1.035)^{5}}\\ {=\S4.35+\S4.20+\dots+\S87.99=\S104.50}\end{array}
$$  
$D=[\S4.35(1)+\S4.20(2)+\dots+\S87.99(5)]/\S104.52=4.598$ years 4.6 years  

Approximate change in price over 1 week:  
$$
d P/P=-[D/(1+y)]d y=-[4.598/(1.035)](+0.005)=-0.0222({\mathrm{or}}2.22\%)
$$  

Sometimes a useful ‘shorthand’ used by bond traders is to refer to the [dollar duration](../../A%20Guide%20to%20Duration%20DV01%20and%20Yield%20Curve.md) $(D D)$ of a bond which is defned as:  
$$
d P=-(D D)d y\quad{\mathrm{hence}}\quad D D=(M D)P
$$  

Knowing $_{D D}$ one can immediately calculate the (approximate) dollar change in value of the bond. Going one step further, for a 1 bp $(0.01\%)$ change in the YTM we have $d y=0.0001$ $(=1/10,000)$ , hence:  
$$
d P({\mathrm{for~}}1{\mathrm{~bp}})=P V B P={\frac{M D\ \times P}{10,000}}
$$  

The expression in (10.7) is known as ‘price value of a basis point’ $(P V B P)$ or the ‘[duration](../../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%205/Key%20Rates%20O1s%20Durations%20and%20Hedging.md) value of a basis point’, usually denoted DV01.  

The above equations can be applied to a single bond using that bond’s [duration](../../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%205/Key%20Rates%20O1s%20Durations%20and%20Hedging.md) $D$ or to a [portfolio](../../../Advanced%20Investments/An%20Asset%20Allocation%20Primer.md) of bonds using the [portfolio](../../../Advanced%20Investments/An%20Asset%20Allocation%20Primer.md) [duration](../../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%205/Key%20Rates%20O1s%20Durations%20and%20Hedging.md), $D_{p}$ . For example, to illustrate the use of PVBP, consider a trader who has a [portfolio](../../../Advanced%20Investments/An%20Asset%20Allocation%20Primer.md) of bonds worth $V_{p}=\mathfrak{F}1\mathrm{m}$ and the [portfolio](../../../Advanced%20Investments/An%20Asset%20Allocation%20Primer.md) ‘modifed [duration](../../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%205/Key%20Rates%20O1s%20Durations%20and%20Hedging.md)’ $M D_{p}=5$ , then PVBP for the [portfolio](../../../Advanced%20Investments/An%20Asset%20Allocation%20Primer.md) is $\$500$ . Suppose there is now a 1 bp change in the yield – for example a change from $\mathrm{YTM}=5\%$ to $\mathrm{YTM}=5.01\%$ – then the change in value of the bond portfolio is $d V_{p}=\$500$ .  

# 10.2.2 Convexity  

[Duration](../../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%205/Key%20Rates%20O1s%20Durations%20and%20Hedging.md) only provides a (frst order) approximation to the change in price of a bond and hence is only accurate for small changes in yields (e.g. up to 25 bps). A more accurate approximation is found by incorporating the [convexity](../../../Fixed%20Income%20Asset%20Pricing/Problem%20Sets/PSET%20II%20Fixed%20Income%20Asset%20Pricing%201.md) of the bond. [Convexity](../../../Fixed%20Income%20Asset%20Pricing/Problem%20Sets/PSET%20II%20Fixed%20Income%20Asset%20Pricing%201.md) $\chi$ (with annual [coupon payments](../../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%203/Realized%20Returns.md)) is defned as:  
$$
\chi=\frac{\displaystyle\sum_{t=1}^{N}t(t+1)C F_{t}/(1+y)^{t}}{P(1+y)^{2}}
$$  

[Convexity](../../../Fixed%20Income%20Asset%20Pricing/Problem%20Sets/PSET%20II%20Fixed%20Income%20Asset%20Pricing%201.md) measures the curvature of the price-yield relationship.  

Unfortunately, there is really no intuition behind the [convexity](../../../Fixed%20Income%20Asset%20Pricing/Problem%20Sets/PSET%20II%20Fixed%20Income%20Asset%20Pricing%201.md) formula. It arises from the mathematics of approximating the non-linear relationship between the bond price and the YTM, using a second order [Taylor series expansion](../../Verification%20of%20Central%20Limit%20Theorem.md) for $d P$ (see Appendix 10). However, once we have calculated the bond’s [convexity](../../../Fixed%20Income%20Asset%20Pricing/Problem%20Sets/PSET%20II%20Fixed%20Income%20Asset%20Pricing%201.md) (in Excel say), our improved estimate for the change in the bond price is given by:  
$$
\frac{d P}{P}\approx-M D.(d y)+\frac{1}{2}\chi(d y)^{2}
$$  

A high value for [convexity](../../../Fixed%20Income%20Asset%20Pricing/Problem%20Sets/PSET%20II%20Fixed%20Income%20Asset%20Pricing%201.md) is a desirable property in a bond since if you can fnd two bonds with the same [duration](../../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%205/Key%20Rates%20O1s%20Durations%20and%20Hedging.md), then the bond with the highest [convexity](../../../Fixed%20Income%20Asset%20Pricing/Problem%20Sets/PSET%20II%20Fixed%20Income%20Asset%20Pricing%201.md) (i.e. higher curvature in the price-yield relationship) will exhibit a larger rise in price when yields fall and a smaller fall in price when yields rise – compared with the low [convexity](../../../Fixed%20Income%20Asset%20Pricing/Problem%20Sets/PSET%20II%20Fixed%20Income%20Asset%20Pricing%201.md) bond. However, this ‘advantage’ will be refected in the higher price you have to pay for the ‘high-[convexity](../../../Fixed%20Income%20Asset%20Pricing/Problem%20Sets/PSET%20II%20Fixed%20Income%20Asset%20Pricing%201.md)’ bond.  

The price change calculated using [duration](../../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%205/Key%20Rates%20O1s%20Durations%20and%20Hedging.md) and ‘[duration](../../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%205/Key%20Rates%20O1s%20Durations%20and%20Hedging.md) plus [convexity](../../../Fixed%20Income%20Asset%20Pricing/Problem%20Sets/PSET%20II%20Fixed%20Income%20Asset%20Pricing%201.md)’ are both approximations to the actual ‘true’ price change. The actual (true) price change will difer from that given by (10.9) if either the change in yield is large or there is a non-parallel shift in the yield curve, as shown in Example 10.2.  

# EXAMPLE 10.2  

# Duration and Convexity  

Data:  

A 5-year pure discount bond, face value $\$1,000$ . The current 5-year YTM is $y=0.10\left(10\%\right)$  

Question: Calculate (i) [duration](../../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%205/Key%20Rates%20O1s%20Durations%20and%20Hedging.md), (ii) [convexity](../../../Fixed%20Income%20Asset%20Pricing/Problem%20Sets/PSET%20II%20Fixed%20Income%20Asset%20Pricing%201.md), (iii) the approximate price change and (iv) the actual price change of the bond for a $2\%$ $(200\mathsf{b p})$ increase in the yield (over 1 week).  

Answer: [Duration](../../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%205/Key%20Rates%20O1s%20Durations%20and%20Hedging.md): $P=\S1{,}000/(1{.}1)^{5}=\S620{.}92$ . [Duration](../../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%205/Key%20Rates%20O1s%20Durations%20and%20Hedging.md) of a pure discount bond equals its maturity, $D=5$ years.  

[Convexity](../../../Fixed%20Income%20Asset%20Pricing/Problem%20Sets/PSET%20II%20Fixed%20Income%20Asset%20Pricing%201.md) $:\chi=[5(6)\S1,000/(1.1)]^{5}/\S690.92(1.1)^{2}=22.28$  

Price change, using [duration](../../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%205/Key%20Rates%20O1s%20Durations%20and%20Hedging.md) $:d P/P=-5/1.1\left(0.02\right)=-0.0909\left(\mathrm{or}-9.09\%\right)$  

Price change, using [duration and convexity](../../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%208/An%20Analytical%20Decomposition%20of%20Forward%20Rates.md) :  
$$
d P/P=-0.0909+(1/2)22.28(0.02)^{2}=-0.0864(\mathrm{or}8.64\%)
$$  

Actual price change (over 1 week):   
Initial price with $\mathrm{YTM}=10\%)=\S1,000/(1.1)^{5}=\S620.92$   
Price with $\mathrm{YTM}=12\%)={\S1,000}/(1.12)^{5}={\S567.43}$   
Actual price change $=-8.615\%$  

Using ‘[duration and convexity](../../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%208/An%20Analytical%20Decomposition%20of%20Forward%20Rates.md)’ provides a closer approximation $(8.64\%)$ to the actual change in price $(8.615\%)$ than using only [duration](../../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%205/Key%20Rates%20O1s%20Durations%20and%20Hedging.md) $(9.09\%)$ .  

# Excel  

The calculation of [duration and convexity](../../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%208/An%20Analytical%20Decomposition%20of%20Forward%20Rates.md) and the ‘true’ change in the bond price can be easily calculated using Excel and an example can be found on the website.  

# 10.3 SUMMARY  

• The [spot rate](../../../International%20Finance/The%20Foreign%20Exchange%20Market%20Annotations.md) is the rate of interest which applies to money borrowed today and paid back at a single point in the future (with no interim payments).   
• The yield curve is a relationship between [interest rates](../../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%202/Interest%20Rate%20Quotations.md) for diferent maturities (taken at a specifc time e.g. 10 a.m. Monday, 20 February).  

• [Duration](../../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%205/Key%20Rates%20O1s%20Durations%20and%20Hedging.md) $D$ (or ‘modifed [duration](../../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%205/Key%20Rates%20O1s%20Durations%20and%20Hedging.md), $M D\mathrm{'}$ ) and [convexity](../../../Fixed%20Income%20Asset%20Pricing/Problem%20Sets/PSET%20II%20Fixed%20Income%20Asset%20Pricing%201.md) $\chi$ can be used to provide an approximation to the change in price (value) of a bond ([portfolio](../../../Advanced%20Investments/An%20Asset%20Allocation%20Primer.md)), for a given change in the yield to maturity (here assumed to be a compound rate).  
$\%$ change in bond price $\qquad=\ -M D\times a$ bsolute change in yield $(d y)$ $\%$ change in bond price $=-(M D)d y+(\chi/2)(d y)^{2}$  

# APPENDIX 10: DURATION AND CONVEXITY  

The price of a coupon paying bond, with annual [coupon payments](../../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%203/Realized%20Returns.md) is a non-linear (convex) function of the yield to maturity, $y$ (compound yield):  
$$
P=\frac{C}{(1+y)}+\frac{C}{(1+y)^{2}}+\ldots+\frac{C}{(1+y)^{n}}+\frac{M}{(1+y)^{n}}
$$  

The change in $P$ for any non-linear function $P=f(y)$ can be approximated by a [Taylor series expansion](../../Verification%20of%20Central%20Limit%20Theorem.md):  
$$
d P={\frac{\partial P}{\partial y}}d y+{\frac{1}{2}}{\frac{\partial^{2}P}{\partial y^{2}}}(d y)^{2}+{\mathrm{higher~order~term~in~}}d y
$$  

Diferentiating (10.A.1) with respect to $y$ gives:  
$$
\begin{array}{l}{{\displaystyle{\frac{\partial P}{\partial y}=\frac{-C}{(1+y)^{2}}-\frac{2C}{(1+y)^{3}}-\ldots-\frac{n C}{(1+y)^{n+1}}-\frac{n M}{(1+y)^{n+1}}}}}\\ {{\displaystyle{\phantom{\frac{-1}{(1+y)}}=\frac{-1}{(1+y)}\left[\frac{C}{(1+y)}+\frac{2C}{(1+y)^{2}}+\ldots+\frac{n C}{(1+y)^{n}}+\frac{n M}{(1+y)^{n}}\right]}}}\end{array}
$$  

Using the frst term in the Taylor series $d P=(\partial P/\partial y)d y$ and (10.A.3) we obtain:  
$$
{\frac{d P}{P}}\approx-{\frac{1}{(1+y)}}\left({\frac{1}{P}}\right)\left[{\frac{C}{(1+y)}}+{\frac{2C}{(1+y)^{2}}}+\ldots+{\frac{n C}{(1+y)^{n}}}+{\frac{n M}{(1+y)^{n}}}\right]d y
$$  

Equation (10.A.3) can be written as:  
$$
{\frac{d P}{P}}\approx{\frac{-D}{(1+y)}}d y\ \mathrm{or}\ {\frac{d P}{P}}=-M D.(d y)
$$  

where we defne [duration](../../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%205/Key%20Rates%20O1s%20Durations%20and%20Hedging.md) $D$ and ‘modifed [duration](../../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%205/Key%20Rates%20O1s%20Durations%20and%20Hedging.md)’ $M D$ as:  
$$
D={\frac{1}{P}}\left[{\frac{(1)C}{(1+y)}}+{\frac{2C}{(1+y)^{2}}}+\ldots+{\frac{n(C+M)}{(1+y)^{n}}}\right]
$$  
$$
M D=D/(1+y)
$$  

[Duration](../../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%205/Key%20Rates%20O1s%20Durations%20and%20Hedging.md) and modifed [duration](../../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%205/Key%20Rates%20O1s%20Durations%20and%20Hedging.md) for a coupon paying bond are calculated using (10.A.6a) and (10.A.6b) where the inputs are the current YTM (for an $n$ -period bond), current market price of the bond, the coupons and maturity value of the bond. Having obtained the value for $D$ (or ) Equation (10.A.5) provides a frst order approximation for the proportionate change in the bond price (for small changes in the YTM and for parallel shifts in the yield curve).  

To calculate the change in the bond price using the second order [Taylor series expansion](../../Verification%20of%20Central%20Limit%20Theorem.md) (10.A.2) we diferentiate (10.A.3) again with respect to $y$ :  
$$
{\frac{\partial^{2}P}{\partial y^{2}}}=\left[{\frac{(1)(2)C}{(1+y)}}+{\frac{(2)(3)C}{(1+y)^{2}}}+\ldots+{\frac{n(n+1)C}{(1+y)^{n}}}+{\frac{n(n+1)M}{(1+y)^{n}}}\right]{\frac{1}{(1+y)^{2}}}
$$  

Using (10.A.2), (10.A.4) and (10.A.7) we obtain a second order approximation to the change in the bond price:  
$$
\frac{d P}{P}\approx-M D.(d y)+\frac{1}{2}\chi.(d y)^{2}
$$  

where we defne the ‘[convexity](../../../Fixed%20Income%20Asset%20Pricing/Problem%20Sets/PSET%20II%20Fixed%20Income%20Asset%20Pricing%201.md)’ $\chi$ of the bond as Equation (10.A.7) divided by $P$ :  
$$
\chi=\frac{1}{(1+y)^{2}}\left[\sum_{i=1}^{n}\frac{i(i+1)C}{(1+y)^{i}}+\frac{n(n+1)M}{(1+y)^{n}}\right]\frac{1}{P}
$$  

The [convexity](../../../Fixed%20Income%20Asset%20Pricing/Problem%20Sets/PSET%20II%20Fixed%20Income%20Asset%20Pricing%201.md) of a coupon paying bond at any point in time can be calculated from (10.A.9). The modifed [duration and convexity](../../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%208/An%20Analytical%20Decomposition%20of%20Forward%20Rates.md) are then used in (10.A.8) to calculate the approximate change in the bond price – over a small interval of time (i.e. $d y$ is small) – and for a parallel shift in the yield curve.  

# Zero-coupon Bond  

It is straightforward to show that the [duration](../../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%205/Key%20Rates%20O1s%20Durations%20and%20Hedging.md) of a zero-coupon bond equals its [time to maturity](../../../Financial%20Instruments/Lecture%20Notes-%20Financial%20Instruments/Teaching%20Note%201-%20Forward%20Rates%20Agreement/Hedging%20Strategies%20with%20Forwards.md), n. We have:  
$$
\begin{array}{c}{{P=\displaystyle\frac{\cal M}{(1+y)^{n}}}}\\ {{\displaystyle\frac{d P}{P}=-\displaystyle\frac{1}{P}\left[\displaystyle\frac{n{\cal M}}{(1+y)^{n+1}}\right]d y}}\end{array}
$$  

Substituting for $P$ from (10.A.10) in (10.A.11):  
$$
\frac{d P}{P}=\frac{-n}{(1+y)}d y
$$  

[Duration](../../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%205/Key%20Rates%20O1s%20Durations%20and%20Hedging.md) is defned by the following equation:  
$$
\frac{d P}{P}=\frac{-D}{(1+y)}d y
$$  

Hence, comparing (10.A.12) and (10.A.13) we see that the [duration](../../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%205/Key%20Rates%20O1s%20Durations%20and%20Hedging.md) of a zero-coupon bond equals the [time to maturity](../../../Financial%20Instruments/Lecture%20Notes-%20Financial%20Instruments/Teaching%20Note%201-%20Forward%20Rates%20Agreement/Hedging%20Strategies%20with%20Forwards.md) of the zero. Hence a zero-coupon bond with 5 years (left) to maturity has a [duration](../../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%205/Key%20Rates%20O1s%20Durations%20and%20Hedging.md) equal to 5.  

# Continuously Compounded Yields  

Repeating the above analysis using the continuously compounded YTM $(y)$ to price a coupon paying bond we have:  
$$
P=C e^{-y t_{1}}+C e^{-y t_{2}}+\dots+C e^{-y t_{n}}+M e^{-y t_{n}}
$$  

where $t_{i}=\mathrm{time}$ of the cash fow in years (e.g. if the coupons are paid 6 months, 1 year, 1.5 years from today, then $t_{1}=0.5,t_{2}=1,t_{3}=1.5$ etc. Using (10.A.14) and a frst order Taylor series for $d P\approx\left(\partial P/\partial y\right)d y$ , it can be shown that:  
$$
{\frac{d P}{P}}\approx-D d y
$$  

where [duration](../../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%205/Key%20Rates%20O1s%20Durations%20and%20Hedging.md), using the continuously compounded YTM is defned as:  
$$
D={\frac{1}{P}}[t_{1}C+t_{2}C+\ldots+t_{n}C+t_{n}M]
$$  

# EXERCISES  

# Question 1  

What is the (spot) yield curve and why is it useful?  

# Question 2  

If all yields are expected to fall by $1\%$ over the next week, would you hold low [duration](../../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%205/Key%20Rates%20O1s%20Durations%20and%20Hedging.md) or high [duration](../../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%205/Key%20Rates%20O1s%20Durations%20and%20Hedging.md) bonds?  

# Question 3  

What is meant by the [convexity](../../../Fixed%20Income%20Asset%20Pricing/Problem%20Sets/PSET%20II%20Fixed%20Income%20Asset%20Pricing%201.md) of a bond? Why might you be willing to pay more for bond-A which has a greater [convexity](../../../Fixed%20Income%20Asset%20Pricing/Problem%20Sets/PSET%20II%20Fixed%20Income%20Asset%20Pricing%201.md) than bond-B (ceteris paribus)?  

# Question 4  

Consider a 5-year, $10\%$ coupon bond (annual coupons) with par value $\$100$ , yield to maturity $y=10\%$ p.a. (compound rate). Calculate the current market price, $P$ and the (Macaulay) duration, $D$ .  

# Question 5  

Consider a 5-year, $10\%$ coupon bond (annual coupons) with par value $\$100$ and yield to maturity, $y=10\%$ p.a. (compound rate). The current market price, $P=\$100$ and the (Macaulay) [duration](../../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%205/Key%20Rates%20O1s%20Durations%20and%20Hedging.md) $D=4.1679$ . Calculate:  

(a) The (approximate) price change if the yield to maturity falls to $9.5\%$ .   
(b) The ‘true’ price change if $y$ falls to $9.5\%$ .  

# Question 6  

[Portfolio](../../../Advanced%20Investments/An%20Asset%20Allocation%20Primer.md) A: 1-year zero-coupon bond, face value $=\$2,000$ and 10-year zero-coupon bond, face value $=\$6,000$ [Portfolio](../../../Advanced%20Investments/An%20Asset%20Allocation%20Primer.md) B: 5.95-year zero-coupon bond, face value $=\$5,000$  

Current yield curve is fat and $y=10\%$ p.a. (continuously compounded)  

(a) Show that the [duration](../../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%205/Key%20Rates%20O1s%20Durations%20and%20Hedging.md) of [portfolio](../../../Advanced%20Investments/An%20Asset%20Allocation%20Primer.md)-A equals that of [portfolio](../../../Advanced%20Investments/An%20Asset%20Allocation%20Primer.md)-B.   
(b) What is the actual percentage change in value of [portfolio](../../../Advanced%20Investments/An%20Asset%20Allocation%20Primer.md)-A for an increase in yield of 10 bps?   
(c) Does the [duration](../../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%205/Key%20Rates%20O1s%20Durations%20and%20Hedging.md) formula give approximately the same answer?   
(d) Repeat (b) for portfolios A and B for an increase in yield of $5\%$ p.a. Which [portfolio](../../../Advanced%20Investments/An%20Asset%20Allocation%20Primer.md) has the higher [convexity](../../../Fixed%20Income%20Asset%20Pricing/Problem%20Sets/PSET%20II%20Fixed%20Income%20Asset%20Pricing%201.md)?  
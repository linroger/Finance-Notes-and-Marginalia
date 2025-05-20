---
title: Forwards and Futures Notes
tags:
  - coupon_bonds
  - currency_forwards
  - implied_forward_rates
  - interest_arbitrage
  - zero_coupon_bonds
aliases:
  - Bonds
  - Currency
  - Forwards
  - Futures
key_concepts:
  - Coupon bond pricing
  - Covered interest arbitrage
  - Currency forward rate
  - Implied forward rates
  - Prepaid forward price
  - Zero-coupon bond pricing
---

- [Introduction](Ch1%20[[Squam%20Lake%20Group%20Introduction) to Derivative Markets]]
- [Hedging](Chapter%206%20(Hull)%20[[Key%20Rates%20O1s%20Durations%20and%20Hedging) Strategies with [Forwards](../../../Financial%20Markets/Financial%20Asset%20Pricing%20Theory%20Overview/Chapter%2012%20-%20Derivatives/Forwards%20and%20Futures.md)]]
- [Forward Exchange Rate](Deriving%20[[A%20Primer%20on%20Currency%20Derivatives) Numerical Example]]
- [Secondary Commodities](Primary%20vs.%20[[Primary%20vs.%20Secondary%20Commodities)]]
- [Foreign Exchange Quoting Conventions](Foreign%20Exchange%20Quoting%20Conventions.md)
- [Forward Contracts on Exchange Rates](Forward%20Contracts%20on%20Exchange%20Rates.md)
- [Forwards and Futures]([[Forward%20and%20Futures%20Contracts) Notes]]
- [Hedging]([[Key%20Rates%20O1s%20Durations%20and%20Hedging) Strategies with [Forwards](../../../Financial%20Markets/Financial%20Asset%20Pricing%20Theory%20Overview/Chapter%2012%20-%20Derivatives/Forwards%20and%20Futures.md)]]
- [Financial Instruments]([[A%20Practical%20Guide%20for%20Actuaries%20and%20other%20Business%20Professionals.)/Lecture Notes/Teaching Note 1- Forward Rates Agreement/[Interest Rates](../../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%202/Interest%20Rate%20Quotations.md),  Carry Trades,  and Exchange Rate Movements]]
- [Teaching Note 1Forward Rates Agreement](Teaching%20Note%201Forward%20Rates%20Agreement)
### ZERO-COUPON BONDS AS DISCOUNT FACTORS

In general,  if we have a zero-coupon bond paying \$1 at maturity,  we can write its price in terms of an annualized continuously compounded yield, $r^{cc}(0, t)$$as$$P(0, t)=e^{-r_{cc}(0, t)*t}$

Thus,  if we observe the price,  we can solve for the yield as$$r^{cc}(0, t)= \frac{1}{t}\ln\left[\frac{1}{P(0, t)} \right]$$

# Forwards and Futures Notes

[Currency futures](../../../Financial%20Engineering/Derivatives/Part%20I%20-%20Forwards%20and%20Futures/Chapter%207%20-%20Currency%20Forwards%20and%20Futures.md) and [forwards](../../../Financial%20Markets/Financial%20Asset%20Pricing%20Theory%20Overview/Chapter%2012%20-%20Derivatives/Forwards%20and%20Futures.md) are widely used to hedge against changes in exchange rates.

# CURRENCY PREPAID FORWARD

Suppose that 1 year from today you want to have ¥1. A [prepaid forward](Hedging%20Strategies%20with%20Forwards.md) allows you to pay dollars today to acquire ¥1 in 1 year. What is the [prepaid forward price](Hedging%20Strategies%20with%20Forwards.md)? Suppose the yen-denominated interest rate is$r_y$and the exchange rate today (\$/¥) is$x_0$. We can work backward. If we want ¥1 in 1 year,  we must have$e^{-r_y}$in yen today. To obtain that many yen today,  we must exchange$x_0 e^{-r_y}$dollars into yen.

Thus,  the [prepaid forward price](Hedging%20Strategies%20with%20Forwards.md) for a yen is$$FP = x_0 e^{-r_y T}\tag{17}$$

where T is [time to maturity](Hedging%20Strategies%20with%20Forwards.md) of the forward

- The economic principle governing the [pricing](../../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%207/Arbitrage%20Pricing%20of%20Derivatives.md) of a [prepaid forward](Hedging%20Strategies%20with%20Forwards.md) on [currency](.md) is the same as that for a [prepaid forward](Hedging%20Strategies%20with%20Forwards.md) on stock. By deferring delivery of the [underlying asset](../../Financial%20Derivatives%20and%20Quantitative%20Methods/Risk%20Neutral%20Pricing%20of%20Options.md),  you lose income.
- In the case of [currency](.md),  if you received the [currency](.md) immediately,  you could buy a bond denominated in that [currency](.md) and earn interest.
	- The [prepaid forward price](Hedging%20Strategies%20with%20Forwards.md) reflects the loss of interest from deferring delivery,  just as the [prepaid forward price](Hedging%20Strategies%20with%20Forwards.md) for stock reflects the loss of dividend income

# CURRENCY FORWARD

- The [prepaid forward price](Hedging%20Strategies%20with%20Forwards.md) is the dollar cost of obtaining 1 yen in the future. Thus,  to obtain the [forward price](../../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%2011/Forward%20Contracts%20and%20Forward%20Prices.md),  compute the future value using the dollar-denominated interest rate,  r:$$F_{0, T} = x_0 e^{(r-r_y)T}\tag{18}$$
- The forward [currency](.md) rate will exceed the current exchange rate when the domestic [risk-free rate](../../Black%20Scholes%20Derivation.md) is higher than the foreign [risk-free rate](../../Black%20Scholes%20Derivation.md)
- The interest rate difference$r - r_y$is the cost of carry for a foreign [currency](.md) (we borrow at the domestic rate r and invest the proceeds in a foreign money-market instrument,  earning the foreign rate$r_y$as an offset to our cost). If we wish to borrow foreign [currency](.md), $r_y$is the [lease rate](Primary%20vs.%20Secondary%20Commodities.md).

# COVERED INTEREST ARBITRAGE
- We can synthetically create a [forward contract](../../../Clippings/Forward%20Points%20in%20Currency.md) by borrowing in one [currency](.md) and lending in the other.
- If we want to have 1 yen in the future,  with the dollar price fixed today,  we can pay today for the yen,  and borrow in dollars to do so.
	- To have 1 yen in 1 year,  we need to invest$x_0 e^{-r_y T}$in dollars,  and we obtain this amount by borrowing. 
- The required dollar repayment is$x_0 e^{(r-r_y)T}$which is the [forward exchange rate](../../../Financial%20Engineering/A%20Primer%20on%20Currency%20Derivatives.md).
- The example shows that borrowing in one [currency](.md) and lending in another creates the same [cash flow](../../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%201%20-%20Purpose%20and%20Structure%20of%20Financial%20Markets/Preview%20of%20the%20Book.md) as a [forward contract](../../../Clippings/Forward%20Points%20in%20Currency.md).
- If we offset this [borrowing and lending](../Teaching%20Note%203%20Swaps-%20Financial%20Instruments/Swaps%20Types.md) position with an actual [forward contract](../../../Clippings/Forward%20Points%20in%20Currency.md),  the resulting transaction is called [covered interest arbitrage](.md).
- A [carry trade](../../../Clippings/Currency%20Carry%20Trade.md) entails borrowing in the [currency](.md) with [low interest rates](../../../Financial%20Markets%20and%20Institutions/III.%20Liquidity%20of%20Assets/Class%209-%20Bailouts%20and%20Bank%20Failures/Articles/The%20Economist%20Time%20Is%20Cheap.md) and lending in the [currency](.md) with high [interest rates](../../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%202/Interest%20Rate%20Quotations.md),  without [hedging](../../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%205/Key%20Rates%20O1s%20Durations%20and%20Hedging.md).
- To summarize,  a [forward exchange rate](../../../Financial%20Engineering/A%20Primer%20on%20Currency%20Derivatives.md) reflects the difference in [interest rates](../../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%202/Interest%20Rate%20Quotations.md) denominated in different currencies.
	- Imagine that you want to invest$1 for 1 year.
		- You can do so by buying a dollar-denominated bond,  or you can exchange the dollar into another [currency](.md) and buy a bond denominated in that other [currency](.md).
		- You can then use [currency forwards](Forward%20Contracts%20on%20Exchange%20Rates.md) to guarantee the exchange rate at which you will convert the foreign [currency](.md) back into dollars.
		- The principle behind the [pricing](../../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%207/Arbitrage%20Pricing%20of%20Derivatives.md) of [currency forwards](Forward%20Contracts%20on%20Exchange%20Rates.md) is that a position in foreign risk-free bonds,  with the [currency](.md) risk hedged,  pays the same return as domestic risk-free bonds.

### CHAPTER SUMMARY

- The purchase of a stock or other asset entails agreeing to a price,  making payment,  and taking delivery of the asset. 
- A [forward contract](../../../Clippings/Forward%20Points%20in%20Currency.md) fixes the price today,  but payment and delivery are deferred. 
- The [pricing](../../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%207/Arbitrage%20Pricing%20of%20Derivatives.md) of forward contracts reflects the costs and benefits of this deferred payment and delivery. 
- The seller receives payment later,  so the price is higher to reflect interest owed the seller,  and the buyer receives possession later,  so the price is lower to reflect dividends not received by the buyer. 
- A [prepaid forward](Hedging%20Strategies%20with%20Forwards.md) contract requires payment today; hence,  it separates these two effects. 
- The price of a [prepaid forward](Hedging%20Strategies%20with%20Forwards.md) is$$\text{Prepaid forward price} =S_{0} e^{-\delta T}$$
- The [prepaid forward price](Hedging%20Strategies%20with%20Forwards.md) is below the asset spot price, $S_0$,  due to dividends forgone by deferring delivery. 
- The [forward price](../../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%2011/Forward%20Contracts%20and%20Forward%20Prices.md) also reflects deferral of payment,  so it is the future value of the [prepaid forward price](Hedging%20Strategies%20with%20Forwards.md):$$\text{Forward price} =S_{0} e^{(r-\delta) T}$$
- In the case of a [currency](.md) forward,  the dividend yield forgone by holding the [forward contract](../../../Clippings/Forward%20Points%20in%20Currency.md) instead of the [underlying asset](../../Financial%20Derivatives%20and%20Quantitative%20Methods/Risk%20Neutral%20Pricing%20of%20Options.md),  δ,  is the interest rate you could earn by investing in foreigncurrency denominated assets. 
- Thus,  for currencies, $δ = r_f$,  where$r_f$is the foreign interest rate.
- A [forward contract](../../../Clippings/Forward%20Points%20in%20Currency.md) is equivalent to a leveraged position in an asset—borrowing to buy the asset. By combining the [forward contract](../../../Clippings/Forward%20Points%20in%20Currency.md) with other assets it is possible to create synthetic stocks and bonds.
- Since a [forward contract](../../../Clippings/Forward%20Points%20in%20Currency.md) is risky but requires no [investment](../../../Advanced%20Investments/An%20Asset%20Allocation%20Primer.md),  it earns the risk premium.
- The [forward price](../../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%2011/Forward%20Contracts%20and%20Forward%20Prices.md) is therefore a biased predictor of the [future spot price](Hedging%20Strategies%20with%20Forwards.md) of the asset,  with the bias equal to the risk premium.
- The fact that it is possible to create a synthetic forward has two important implications. 
- First,  if the [forward contract](../../../Clippings/Forward%20Points%20in%20Currency.md) is mispriced,  arbitrageurs can take offsetting positions in the [forward contract](../../../Clippings/Forward%20Points%20in%20Currency.md) and the synthetic [forward contract](../../../Clippings/Forward%20Points%20in%20Currency.md)—in effect buying low and selling high— and make a [risk-free profit](../../../Financial%20Markets/Financial%20Asset%20Pricing%20Theory%20Overview/Chapter%203%20-%20%20Assets,%20Portfolios,%20and%20Arbitrage/Arbitrage.md)
- Second,  dealers who make markets in the forward or in the [underlying asset](../../Financial%20Derivatives%20and%20Quantitative%20Methods/Risk%20Neutral%20Pricing%20of%20Options.md) can hedge the risk of their position with a synthetic offsetting position. With transaction costs there is a no-[arbitrage](../../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%207/Arbitrage%20Pricing%20of%20Derivatives.md) region rather than a single [no-arbitrage price](../../../Financial%20Markets/Financial%20Asset%20Pricing%20Theory%20Overview/Chapter%2012%20-%20Derivatives/Exercises.md).
- [Futures contracts](../../../Financial%20Engineering/Mathematics%20of%20the%20Financial%20Markets.md) are similar to forward contracts,  except that with [futures](../../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%203%20-%20Futures%20Markets/Futures%20Not%20Subject%20to%20Cash-And-Carry.md) there are [Leverage](Lecture%206-[[Lecture%206-Leverage,%20Tail%20Risk,%20Volatility%20Products), Tail Risk, Volatility Products#6.1.3 [Margin requirements](../../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%2010/Case%20Study%20Mf%20Globals%20Repo-To-Maturity%20Trades.md)|[margin requirements](../../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%2010/Case%20Study%20Mf%20Globals%20Repo-To-Maturity%20Trades.md)]] and [daily settlement](../../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%2011/Pricing%20and%20Hedging%20Implications%20of%20Daily%20Sett.md) of the gain or loss on the position.

# INTEREST RATE FORWARDS AND FUTURES

Note from equation (1) that a zero-coupon bond price is a [discount factor](../../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%201/Discount%20Factors.md): A zero-coupon bond price is what you could pay today to receive $1 in the future. If you have a future cash flow at time $T$,  you can multiply it by the price of a zero-coupon bond,  $P(0,  T)$,  to obtain the present value of the cash flow. Because of equation (1),  multiplying by $P(0,  T)$ is the same as discounting at the rate $r(0,  T)$,  i.e., $$ C_x \times P(0,  T) = \frac{C_x}{1 + r(0,  T)}$$
The inverse of the zero-coupon bond price,  $1/P(0,  T)$,  provides a future value factor…

## IMPLIED FORWARD RATES

We now see how column (3) in Table 1 can be computed from either column (1) or (2). The 1-year and 2-year zero-coupon yields are the rates you can earn from year 0 to year 1 and from year 0 to year 2. There is also an implicit rate that can be earned from year 1 to year 2 that must be consistent with the other two rates. This rate is called the implied [forward rate](../../../Clippings/Forward%20Points%20in%20Currency.md)..

## COUPON BONDS

Given the prices of zero-coupon bonds—column (1) in Table 1—we can price coupon bonds. We can also compute the par coupon—column (4) in Table 1—the coupon rate at which a bond will be priced at par. To describe a coupon bond,  we need to know the date at which the bond is being priced,  the start and end date of the bond payments,  the number and amount of the payments,  and the amount of principal…

Since the price of a bond is the present value of its payments,  at issuance time$t$the price of a bond maturing at$T$must satisfy$$B(t,  T,  c,  n) = \sum_{i=1}^n cP(t,  t_i) + P(t,  T)$$

where$t_i = t + i(T - t)/n$,  with$i$being the index in the summation. Using equation (5),  we can solve for the coupon as$$c = \frac{B(t,  T,  c,  n) - P(t,  T)}{\sum_{i=1}^n P(t,  t_i)}$$

A par bond has$B = 1$,  so the coupon on a par bond is given by$$c = \frac{1 - P(t,  T)}{\sum_{i=1}^n P(t,  t_i)}$$

Suppose the bond makes$m$payments per year. Denoting the per-period yield to maturity as$y$,  we have$$B(t,  T,  c,  n) = \sum_{i=1}^n \frac{c}{(1 + y/m)^{m \times t_i}} + \frac{1}{(1 + y/m)^{m \times T}}$$

- It is common to compute the quoted annualized yield to maturity, $y$,  as$y = m \times y_{\text{per period}}$. Government bonds,  for example,  make two [coupon payments](../../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%203/Realized%20Returns.md) per year,  so the annualized yield to maturity is twice the semiannual yield to maturity.

The difference between equation (5) and equation (7) is that in equation (5),  each coupon payment is discounted at the appropriate rate for a [cash flow](../../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%201%20-%20Purpose%20and%20Structure%20of%20Financial%20Markets/Preview%20of%20the%20Book.md) occurring at that time…

### ZEROS FROM COUPONS
- We price the zero-coupon bond prices and deduced the prices of coupon bonds. In practice,  the situation is often the reverse: We observe prices of coupon bonds and must infer prices of zero-coupon bonds. This procedure in which zero coupon bond prices are deduced from a set of coupon bond prices is called bootstrapping…
---

### DURATION

When comparing bonds with different prices and par values,  it is helpful to have a measure

 of [price sensitivity](../../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%204/Duration.md) expressed *per dollar of bond price*. We obtain this by dividing equation (9) by the bond price, $B(y)$,  and multiplying by -1. This gives us a measure known as [modified duration](../../../Financial%20Engineering/A%20Guide%20to%20Duration%20DV01%20and%20Yield%20Curve.md),  which is the$percentage$change in the bond price for a unit change in the yield:$$\text{Modified duration }=-\frac{\text{Change in bond price}}{\text{Unit change in yield}}\times\frac{1}{B(y)}\tag{10}$$

- We obtain another measure of bond price risk—*[Macaulay duration](../../../Fixed%20Income%20Asset%20Pricing/Fixed%20Income%20Lecture%20Notes/Teaching%20Note%202-%20Interest%20Rate%20Risk%20Management%20And%20Factors.md)*—by multiplying equation(10) by$1+y/m$
- This puts both bond price and yield changes in percentage terms and gives us an expression with a clear interpretation:$$\text{Macaulay duration} = -\frac{\text{Change in bond price}}{\text{Unit change in yield}} \times \frac{1+y/m}{B(y)} =$$$$\frac{1}{B(y)}  \sum_{i=1}^{n} \frac{i}{m} \frac{C}{m} \frac{1}{(1+y/m)^i} + \frac{n}{m} \frac{M}{(1+y/m)^n}$$
- To interpret this expression,  note that$(C/m)/(1+y/m)^i$is the present value of the$i$th bond payment,  which occurs in$i/m$years. The quantity$C/m/[(1+y/m)^iB(y)]$is therefore the fraction of the bond value that is due to the$i$th payment.
- [Macaulay duration](../../../Fixed%20Income%20Asset%20Pricing/Fixed%20Income%20Lecture%20Notes/Teaching%20Note%202-%20Interest%20Rate%20Risk%20Management%20And%20Factors.md) is a weighted average of the time (number of periods) until the bond payments occur,  with the weights being the percentage of the bond price accounted for by each payment.
- This interpretation of [Macaulay duration](../../../Fixed%20Income%20Asset%20Pricing/Fixed%20Income%20Lecture%20Notes/Teaching%20Note%202-%20Interest%20Rate%20Risk%20Management%20And%20Factors.md) as a time-to-payment measure explains why these measures of bond [price sensitivity](../../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%204/Duration.md) are called “[duration](../../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%205/Key%20Rates%20O1s%20Durations%20and%20Hedging.md).”
-For a zero-coupon bond,  equation (11) implies that [Macaulay duration](../../../Fixed%20Income%20Asset%20Pricing/Fixed%20Income%20Lecture%20Notes/Teaching%20Note%202-%20Interest%20Rate%20Risk%20Management%20And%20Factors.md) equals [time to maturity](Hedging%20Strategies%20with%20Forwards.md).

- [Macaulay duration](../../../Fixed%20Income%20Asset%20Pricing/Fixed%20Income%20Lecture%20Notes/Teaching%20Note%202-%20Interest%20Rate%20Risk%20Management%20And%20Factors.md) illustrates why maturity alone is not a satisfactory [risk measure](../../Leverage%20as%20a%20Measure%20of%20Risk.md) fon a coupon bond. A coupon bond makes a series of payments,  each with a different maturity.
- [Macaulay duration](../../../Fixed%20Income%20Asset%20Pricing/Fixed%20Income%20Lecture%20Notes/Teaching%20Note%202-%20Interest%20Rate%20Risk%20Management%20And%20Factors.md) summarizes bond price risk as a weighted average of these different maturities.

## **DURATION**

- Since [duration](../../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%205/Key%20Rates%20O1s%20Durations%20and%20Hedging.md) tells us the sensitivity of the bond price to a change in the interest rate,  it can be used to compute the approximate bond price change for a given change in [interest rates](../../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%202/Interest%20Rate%20Quotations.md). Suppose the bond price is$B(y)$and the yield on the bond changes from$y$to$y + \varepsilon$,  where$\varepsilon$is a small change in the yield. The formula for [Macaulay duration](../../../Fixed%20Income%20Asset%20Pricing/Fixed%20Income%20Lecture%20Notes/Teaching%20Note%202-%20Interest%20Rate%20Risk%20Management%20And%20Factors.md), $D_{\text{Mac}}$,  can be written as:$$D_{\text{Mac}} = -\left[\frac{B(y + \varepsilon) - B(y)}{\varepsilon}\right] \times \frac{1 + y}{B(y)}$$
- We can therefore rewrite this equation to obtain the new bond price in terms of the old bond price and either [duration](../../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%205/Key%20Rates%20O1s%20Durations%20and%20Hedging.md) measure:
$$B(y + \varepsilon) = B(y) - [D \times B(y)\varepsilon] = B(y) - \left[D_{\text{Mac}} / (1 + y)\right] \times B(y)\varepsilon \tag{12}$$

 **[Duration](../../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%205/Key%20Rates%20O1s%20Durations%20and%20Hedging.md) Matching**
- Suppose we own a bond with [time to maturity](Hedging%20Strategies%20with%20Forwards.md)$t_1$,  price$B_1$,  and [Macaulay duration](../../../Fixed%20Income%20Asset%20Pricing/Fixed%20Income%20Lecture%20Notes/Teaching%20Note%202-%20Interest%20Rate%20Risk%20Management%20And%20Factors.md)$D_1$. We are considering a short position in a bond with maturity$t_2$,  price$B_2$,  and [Macaulay duration](../../../Fixed%20Income%20Asset%20Pricing/Fixed%20Income%20Lecture%20Notes/Teaching%20Note%202-%20Interest%20Rate%20Risk%20Management%20And%20Factors.md)$D_2$. How much of the second bond should we short-sell so that the resulting [portfolio](../../../Advanced%20Investments/An%20Asset%20Allocation%20Primer.md)—long the bond with [duration](../../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%205/Key%20Rates%20O1s%20Durations%20and%20Hedging.md)$D_1$and short the bond with [duration](../../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%205/Key%20Rates%20O1s%20Durations%20and%20Hedging.md)$D_2$—is insensitive to [interest rate changes](../../../International%20Finance/Bridgewater/How%20Countries%20Go%20Broke/How%20Countries%20Go%20Broke-Chapter%2012%20to%20Chapter%2014.md)?
- Equation (12) gives us a formula for the change in price of each bond. Let$N$denote the quantity of the second bond. The value of the [portfolio](../../../Advanced%20Investments/An%20Asset%20Allocation%20Primer.md) is$B_1 + N B_2$,  and,  using equation (12),  the change in price due to an interest rate change of$\varepsilon$is$$B_1(y_1 + \varepsilon) - B_1(y_1)] + N [B_2(y_2 + \varepsilon) - B_2(y_2)$$
$$= -D_1 B_1(y_1)\varepsilon / (1 + y_1) - N D_2 B_2(y_2)\varepsilon / (1 + y_2)$$

where$D_1$and$D_2$are Macaulay durations. If we want the net change to be zero,  we choose$N$to set the right-hand side equal to zero. This gives$$N = -\frac{D_1 B_1(y_1)/(1 + y_1)}{D_2 B_2(y_2)/(1 + y_2)} \tag{13}$$

- When a [portfolio](../../../Advanced%20Investments/An%20Asset%20Allocation%20Primer.md) is [duration](../../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%205/Key%20Rates%20O1s%20Durations%20and%20Hedging.md)-matched in this fashion,  the net [investment](../../../Advanced%20Investments/An%20Asset%20Allocation%20Primer.md) in the [portfolio](../../../Advanced%20Investments/An%20Asset%20Allocation%20Primer.md) will typically not be zero. That is,  either the value of the short bond is less than the value of the long bond,  in which case additional financing is required,  or vice versa,  in which case there is cash to invest. This residual can be financed or invested in very short-term bonds,  with [duration](../../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%205/Key%20Rates%20O1s%20Durations%20and%20Hedging.md) approximately zero,  in order to leave the [portfolio](../../../Advanced%20Investments/An%20Asset%20Allocation%20Primer.md) [duration](../../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%205/Key%20Rates%20O1s%20Durations%20and%20Hedging.md) matched.

**[Convexity](../../../Fixed%20Income%20Asset%20Pricing/Problem%20Sets/PSET%20II%20Fixed%20Income%20Asset%20Pricing%201.md)**

- The hedge in Example 8 is not perfect,  because [duration](../../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%205/Key%20Rates%20O1s%20Durations%20and%20Hedging.md) changes as the [interest rate changes](../../../International%20Finance/Bridgewater/How%20Countries%20Go%20Broke/How%20Countries%20Go%20Broke-Chapter%2012%20to%20Chapter%2014.md). [Convexity](../../../Fixed%20Income%20Asset%20Pricing/Problem%20Sets/PSET%20II%20Fixed%20Income%20Asset%20Pricing%201.md) measures the extent to which [duration](../../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%205/Key%20Rates%20O1s%20Durations%20and%20Hedging.md) changes as the bond's yield changes. The formula for [convexity](../../../Fixed%20Income%20Asset%20Pricing/Problem%20Sets/PSET%20II%20Fixed%20Income%20Asset%20Pricing%201.md) is:$$\text{Convexity} = \frac{1}{B(y)} \left[\sum_{i=1}^{n} \frac{i(i + 1)}{m^2} \frac{C}{m} \frac{1}{(1 + y/m)^{i+2}} + \frac{n(n + 1)}{m^2} \frac{M}{(1 + y/m)^{n+2}}\right] \tag{14}$$
- We can use [convexity](../../../Fixed%20Income%20Asset%20Pricing/Problem%20Sets/PSET%20II%20Fixed%20Income%20Asset%20Pricing%201.md) in addition to [duration](../../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%205/Key%20Rates%20O1s%20Durations%20and%20Hedging.md) to obtain a more accurate prediction of the new bond price. When we include [convexity](../../../Fixed%20Income%20Asset%20Pricing/Problem%20Sets/PSET%20II%20Fixed%20Income%20Asset%20Pricing%201.md),  the price prediction formula,  equation (12),  becomes:$$B(y + \varepsilon) = B(y) - [D \times B(y) \times \varepsilon] + 0.5 \times \text{Convexity} \times B(y) \times \varepsilon^2 \tag{15}$$
- where where$D$is [modified duration](../../../Financial%20Engineering/A%20Guide%20to%20Duration%20DV01%20and%20Yield%20Curve.md). Here is an example of computing a bond price at a new yield using both [duration and convexity](../../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%208/An%20Analytical%20Decomposition%20of%20Forward%20Rates.md).
---

### SYNTHETIC FORWARDS IN MARKET-MAKING AND ARBITRAGE

Suppose a customer wishes to enter into a [long forward](../Teaching%20Note%203%20Swaps-%20Financial%20Instruments/Forward%20Rates%20Agreement.md) position. The market-maker,  as the counterparty,  is left holding a [short forward](../Teaching%20Note%203%20Swaps-%20Financial%20Instruments/Forward%20Rates%20Agreement.md) position. He can offset this risk by creating a synthetic [long forward](../Teaching%20Note%203%20Swaps-%20Financial%20Instruments/Forward%20Rates%20Agreement.md) position

- There is no risk because the total [cash flow](../../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%201%20-%20Purpose%20and%20Structure%20of%20Financial%20Markets/Preview%20of%20the%20Book.md) at time T is$F_{0, T} - S_0e^{(r-\delta)T}$. 

| Transaction                    | Time 0                | Time T (expiration)   |
|--------------------------------|-----------------------|-----------------------|
| Buy stock @$S_0$|$-S_0$|$+S_T$|
| Sell [prepaid forward](Hedging%20Strategies%20with%20Forwards.md) @$F_{0, T}^P$|$+F_{0, T}^P$|$-S_T$|
| **Total**                         |$F_{0, T}^P - S_0$| 0                   |

- Cash flows and transactions to undertake [arbitrage](../../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%207/Arbitrage%20Pricing%20of%20Derivatives.md) when the [prepaid forward price](Hedging%20Strategies%20with%20Forwards.md), $F_{0, T}^P$,  exceeds the [stock price](../../../Financial%20Engineering/Derivatives/Part%20IV%20-%20Options/Chapter%2016%20-%20Black–Scholes%20Model.md), $S_0$.
All of the components of this [cash flow](../../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%201%20-%20Purpose%20and%20Structure%20of%20Financial%20Markets/Preview%20of%20the%20Book.md)—the [forward price](../../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%2011/Forward%20Contracts%20and%20Forward%20Prices.md),  the [stock price](../../../Financial%20Engineering/Derivatives/Part%20IV%20-%20Options/Chapter%2016%20-%20Black–Scholes%20Model.md),  the interest rate,  and the dividend yield—are known at time 0. The result is a risk-free position.
- The market-maker is short a [forward contract](../../../Clippings/Forward%20Points%20in%20Currency.md) and long a synthetic [forward contract](../../../Clippings/Forward%20Points%20in%20Currency.md),  constructed as in Table 3. 

| Transaction          | Time 0                | Time T (expiration)     |
|----------------------|-----------------------|-------------------------|
| Buy$e^{-\delta T}$units of the index |$-S_0e^{-\delta T}$|$+S_T$|
| Borrow$S_0e^{-\delta T}$|$+S_0e^{-\delta T}$|$-S_0e^{(r-\delta)T}$|
| **Total**               | 0                     |$S_T - S_0e^{(r-\delta)T}$|

- Demonstration that borrowing$S_0e^{-\delta T}$to buy$e^{-\delta T}$shares of the index replicates the payoff to a [forward contract](../../../Clippings/Forward%20Points%20in%20Currency.md), $S_T - F_{0, T}$.

  - There is no risk because the total [cash flow](../../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%201%20-%20Purpose%20and%20Structure%20of%20Financial%20Markets/Preview%20of%20the%20Book.md) at time T is$F_{0, T} - S_0e^{(r-\delta)T}$. All of the components of this [cash flow](../../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%201%20-%20Purpose%20and%20Structure%20of%20Financial%20Markets/Preview%20of%20the%20Book.md)—the [forward price](../../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%2011/Forward%20Contracts%20and%20Forward%20Prices.md),  the [stock price](../../../Financial%20Engineering/Derivatives/Part%20IV%20-%20Options/Chapter%2016%20-%20Black–Scholes%20Model.md),  the interest rate,  and the dividend yield—are known at time 0. The result is a risk-free position.

- Transactions and cash flows for a [cash-and-carry](Carry%20Trade.md): A market-maker is short a [forward contract](../../../Clippings/Forward%20Points%20in%20Currency.md) and long a synthetic [forward contract](../../../Clippings/Forward%20Points%20in%20Currency.md).$$F_{0, T} > S_0e^{(r-\delta)T}$$

| Transaction                            | Time 0                | Time T (expiration)     |
|----------------------------------------|-----------------------|-------------------------|
| Buy tailed position in stock,  paying$S_0e^{-\delta T}$|$-S_0e^{-\delta T}$|$+S_T$|
| Borrow$S_0e^{-\delta T}$|$+S_0e^{-\delta T}$|$-S_0e^{(r-\delta)T}$|
| [Short forward](../Teaching%20Note%203%20Swaps-%20Financial%20Instruments/Forward%20Rates%20Agreement.md)                                                  | 0                       |$F_{0, T} - S_T$|
| **Total**                                                      | 0                       |$F_{0, T} - S_0e^{(r-\delta)T}$|

Similarly,  suppose the market-maker wishes to hedge a [long forward](../Teaching%20Note%203%20Swaps-%20Financial%20Instruments/Forward%20Rates%20Agreement.md) position. Then it is possible to reverse the positions in Table 6. The result is in Table 7

- Transactions and cash flows for a reverse [cash-and-carry](Carry%20Trade.md): A market-maker is long a [forward contract](../../../Clippings/Forward%20Points%20in%20Currency.md) and short a synthetic [forward contract](../../../Clippings/Forward%20Points%20in%20Currency.md).$$F_{0, T} < S_0e^{(r-\delta)T}$$

| Transaction                              | Time 0                | Time T (expiration)     |
|------------------------------------------|-----------------------|-------------------------|
| Short tailed position in stock,  receiving$S_0e^{-\delta T}$|$+S_0e^{-\delta T}$|$-S_T$|
| Lend$S_0e^{-\delta T}$|$-S_0e^{-\delta T}$|$+S_0e^{(r-\delta)T}$|
| [Long forward](../Teaching%20Note%203%20Swaps-%20Financial%20Instruments/Forward%20Rates%20Agreement.md)                                                    | 0                     |$S_T - F_{0, T}$|
| **Total**                                                          | 0                     |$S_0e^{(r-\delta)T} - F_{0, T}$|

- A transaction in which you buy the [underlying asset](../../Financial%20Derivatives%20and%20Quantitative%20Methods/Risk%20Neutral%20Pricing%20of%20Options.md) and short the offsetting [forward contract](../../../Clippings/Forward%20Points%20in%20Currency.md) is called a **[cash-and-carry](Carry%20Trade.md)**.
	- A [cash-and-carry](Carry%20Trade.md) has no risk: You have an obligation to deliver the asset but also own the asset.
	- The market-maker offsets the [short forward](../Teaching%20Note%203%20Swaps-%20Financial%20Instruments/Forward%20Rates%20Agreement.md) position with a [cash-and-carry](Carry%20Trade.md).
	- An [arbitrage](../../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%207/Arbitrage%20Pricing%20of%20Derivatives.md) that involves buying the [underlying asset](../../Financial%20Derivatives%20and%20Quantitative%20Methods/Risk%20Neutral%20Pricing%20of%20Options.md) and selling it forward is called a **[cash-and-carry arbitrage](../../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%2015/Dollar%20Rolls.md)**
- A reverse [cash-and-carry](Carry%20Trade.md) entails short-selling the index and entering into a [long forward](../Teaching%20Note%203%20Swaps-%20Financial%20Instruments/Forward%20Rates%20Agreement.md) position.
- If the [forward contract](../../../Clippings/Forward%20Points%20in%20Currency.md) is priced according to equation (6),  then profits on a cashand-carry are zero.
- However,  an arbitrageur might also engage in a [cash-and-carry](Carry%20Trade.md). If the [forward price](../../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%2011/Forward%20Contracts%20and%20Forward%20Prices.md) is too high relative to the [stock price](../../../Financial%20Engineering/Derivatives/Part%20IV%20-%20Options/Chapter%2016%20-%20Black–Scholes%20Model.md)—i.e.,   if$F_{0, T} > S_0e^{(r-\delta)T}$—then an arbitrageur or market-maker can use the strategy in Table 6 to make a [risk-free profit](../../../Financial%20Markets/Financial%20Asset%20Pricing%20Theory%20Overview/Chapter%203%20-%20%20Assets,%20Portfolios,%20and%20Arbitrage/Arbitrage.md).
- An arbitrageur would make the transactions in Table 7 if the forward were underpriced relative to the stock—i.e.,  if$$S_0e^{(r-\delta)T} > F_{0, T}$$

# NO-ARBITRAGE BOUNDS WITH TRANSACTION COSTS

Tables 6 and 7 demonstrate that an arbitrageur can make a costless profit if $F_{0, T} \neq S_0e^{(r-\delta)T}$  

- This analysis ignores trading fees,  [Bid and Ask](Class%20Note%209%20[[Class%20Note%209%20Bid%20and%20Ask%20Prices%20With%20Private%20Information) Prices With Private Information|[bid-ask](../../../Financial%20Markets%20and%20Institutions/III.%20Liquidity%20of%20Assets/Class%205-%20Private%20Information,%20Liquidity,%20and%20Securitization/Bid-Ask%20Prices%20with%20Adverse%20SelectionPrivate%20Information.md) spreads]],  different [interest rates](../../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%202/Interest%20Rate%20Quotations.md) for [borrowing and lending](../Teaching%20Note%203%20Swaps-%20Financial%20Instruments/Swaps%20Types.md),  and the possibility that buying or selling in large quantities will cause prices to change.
- The effect of such costs will be that,  rather than there being a single [no-arbitrage price](../../../Financial%20Markets/Financial%20Asset%20Pricing%20Theory%20Overview/Chapter%2012%20-%20Derivatives/Exercises.md),  there will be a no-[arbitrage](../../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%207/Arbitrage%20Pricing%20of%20Derivatives.md) bound: a lower price F and an upper price F such that [arbitrage](../../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%207/Arbitrage%20Pricing%20of%20Derivatives.md) will not be profitable when the [forward price](../../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%2011/Forward%20Contracts%20and%20Forward%20Prices.md) is between these bounds.
- Suppose that the stock and forward have [bid and ask](../../../Financial%20Markets%20and%20Institutions/III.%20Liquidity%20of%20Assets/Class%205-%20Private%20Information,%20Liquidity,%20and%20Securitization/Class%20Note%209%20Bid%20and%20Ask%20Prices%20With%20Private%20Information.md) prices of$S^b < S^a$and$F^b < F^a$,  a trader faces a cost k of transacting in the stock or forward,  and the [interest rates](../../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%202/Interest%20Rate%20Quotations.md) for [borrowing and lending](../Teaching%20Note%203%20Swaps-%20Financial%20Instruments/Swaps%20Types.md) are$r^b > r^l$.
	- In this example we suppose that there are no transaction costs at time T,  with the forward settled by delivery of the stock. 
- We will first derive$F^{+}$.
- An arbitrageur believing the observed bid [forward price](../../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%2011/Forward%20Contracts%20and%20Forward%20Prices.md), $F^b$,  is too high will undertake the transactions in Table 6:
	- Sell the forward and borrow to buy the stock. For simplicity we will assume the stock pays no dividends.
- The arbitrageur will pay the transaction cost k to short the forward and pay$(S^a + k)$to acquire one share of stock. The required borrowing to finance the position is therefore$S^a + 2k$. 

At time T,  the payoff $$- (S_0^a + 2k)e^{r_bT} + F_{0, T} - S_T + S_T $$

[Arbitrage](../../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%207/Arbitrage%20Pricing%20of%20Derivatives.md) is profitable if this expression is positive,  or $$F_b > F^+ = (s_0^a + 2k)e^{r_T} \\ \tag{11})$$

- Thus,  the upper bound reflects the fact that we pay a high price for the stock (the ask price),  pay transaction costs on both the stock and forward,  and borrow at a high rate.
- This expression assumes that short-selling the stock does not entail costs other than [bid-ask](../../../Financial%20Markets%20and%20Institutions/III.%20Liquidity%20of%20Assets/Class%205-%20Private%20Information,%20Liquidity,%20and%20Securitization/Bid-Ask%20Prices%20with%20Adverse%20SelectionPrivate%20Information.md) transaction costs when the short position is initiated
- There are additional costs not reflected in equations (11) and (12). One is that significant amounts of trading can move prices,  so that what appears to be an [arbitrage](../../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%207/Arbitrage%20Pricing%20of%20Derivatives.md) may vanish if prices change when the arbitrageur enters a large order.
- Another challenge can be execution risk. If trades do not occur instantaneously,  the [arbitrage](../../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%207/Arbitrage%20Pricing%20of%20Derivatives.md) can vanish before the trades are completed.
- It is likely that the no-[arbitrage](../../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%207/Arbitrage%20Pricing%20of%20Derivatives.md) region will be different for different arbitrageurs at a point in time,  and different across time for a given arbitrageur. 
- For example,  consider the trading transaction cost,  k.
- A large [investment](../../../Advanced%20Investments/An%20Asset%20Allocation%20Primer.md) bank sees stock order flow from a variety of sources and may have inventory of either long or short positions in stocks.
- The bank may be able to buy or sell shares at low cost by serving as market-maker for a customer order.
- It may be inexpensive for a bank to short if it already owns the stocks,  or it may be inexpensive to buy if the bank already has a short position.
- [Borrowing and lending](../Teaching%20Note%203%20Swaps-%20Financial%20Instruments/Swaps%20Types.md) rates can also vary.
- For a transaction that is explicitly financed by borrowing,  the relevant [interest rates](../../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%202/Interest%20Rate%20Quotations.md) are the arbitrageur's marginal borrowing rate (if that is the source of funds to buy stocks) or lending rate (if stocks are to be shorted).
- However,  at other times,  it may be possible to borrow at a lower rate or lend at a higher rate.
- For example,  it may be possible to sell T-bills being held for some other purpose as a source of short-term funds. This may effectively permit borrowing at a low rate. 
- Finally,  in order to borrow money or securities arbitrageurs must have available capital.
- Undertaking one [arbitrage](../../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%207/Arbitrage%20Pricing%20of%20Derivatives.md) may prevent undertaking another.
- The overall conclusion is not surprising: [Arbitrage](../../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%207/Arbitrage%20Pricing%20of%20Derivatives.md) may be difficult,  risky,  and costly.
- Large deviations from the theoretical price may be arbitraged,  but small deviations may or may not represent genuine [arbitrage opportunities](../../../Financial%20Markets%20and%20Institutions/III.%20Liquidity%20of%20Assets/Class%208-%20Markets,%20Meltdowns,%20and%20Arbitrage/Class%20Note%2013%20The%20LTCM%20Meltdown.md).

# QUASI-ARBITRAGE
- The previous section focused on explicit [arbitrage](../../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%207/Arbitrage%20Pricing%20of%20Derivatives.md). However,  it can also be possible to undertake implicit [arbitrage](../../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%207/Arbitrage%20Pricing%20of%20Derivatives.md) by substituting a low yield position for one with a higher return. We call this quasi-[arbitrage](../../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%207/Arbitrage%20Pricing%20of%20Derivatives.md).
- Consider,  for example,  a corporation that can borrow at 8.5% and lend at 7.5%.
- Suppose there is a [cash-and-carry](Carry%20Trade.md) transaction with an [implied repo rate](../../../Financial%20Engineering/Fixed%20Income%20Derivatives/The%20Futures%20Bond%20Basis:%20government%20bond%20futures%20and%20basis%20%20trading.md) of 8%.
- There is no [pure arbitrage](../../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%201%20-%20Purpose%20and%20Structure%20of%20Financial%20Markets/Arbitrage%20Pure%20Versus%20Relative%20Value.md) opportunity for the corporation,  but it would make sense to divert lending
- We can derive F which [arbitrage](../../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%207/Arbitrage%20Pricing%20of%20Derivatives.md) is feasible is analogously.$$-(S_0^b - 2k)e^{r_lT} + S_1 - F_{0, 1} - S_T$$
- which [arbitrage](../../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%207/Arbitrage%20Pricing%20of%20Derivatives.md) is feasible is  the bound below$$F^a < F^- = (S_0^b - 2k)e^{r_lT} \\> (12)$$
- from the 7.5% assets to the 8% [cash-and-carry](Carry%20Trade.md). If we attempt explicit [arbitrage](../../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%207/Arbitrage%20Pricing%20of%20Derivatives.md) by borrowing at 8.5% in order to earn 8% on the [cash-and-carry](Carry%20Trade.md),  the transaction becomes unprofitable.
- We can [arbitrage](../../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%207/Arbitrage%20Pricing%20of%20Derivatives.md) only to the extent that we are already lending; this is why it is “quasi”-[arbitrage](../../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%207/Arbitrage%20Pricing%20of%20Derivatives.md).

# AN INTERPRETATION OF THE FORWARD PRICING FORMULA
- The [forward pricing formula](../../Assignments/PSET%201-Financial%20Instruments.md) for a [stock index](Hedging%20Strategies%20with%20Forwards.md),  equation (6),  depends on$r - \delta$,  the difference between the [risk-free rate](../../Black%20Scholes%20Derivation.md) and the dividend yield. This difference is called the **cost of carry**.

---
### [](../../../Fixed%20Income%20Asset%20Pricing/Fixed%20Income%20Lecture%20Notes/A%20Guide%20to%20the%20Front%20End%20and%20Basis%20Swap%20Markets.md#Forward%20Rate%20Agreements%20(FRAs)%20Overview|Forward%20Rate%20Agreements)

A [Basis Swap](A%20Guide%20to%20the%20Front%20End%20and%20[[Basis%20Swaps) Markets#[Forward Rate Agreements](../../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%2012/EURIBOR%20Forward%20Rate%20Agreements%20and%20Futures.md) (FRAs) [Overview](../../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%201%20-%20Purpose%20and%20Structure%20of%20Financial%20Markets/Overview%20of%20Financial%20Markets.md)|[Forward Rate](../../../Clippings/Forward%20Points%20in%20Currency.md) Agreement]](FRA) is an over-the-counter contract that guarantees a borrowing or lending rate on a given [notional principal](../../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%204%20-%20Swap%20Markets/Fundamentals%20of%20Swaps.md) amount. FRAs can be settled either at the initiation or maturity of the borrowing or lending transaction.

If settled at maturity,  we will say the [Basis Swap](A%20Guide%20to%20the%20Front%20End%20and%20[[Basis%20Swaps) Markets#[Forward Rate Agreements](../../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%2012/EURIBOR%20Forward%20Rate%20Agreements%20and%20Futures.md) (FRAs) [Overview](../../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%201%20-%20Purpose%20and%20Structure%20of%20Financial%20Markets/Overview%20of%20Financial%20Markets.md)|FRA]] is settled in arrears. In the example above,  the [Basis Swap](A%20Guide%20to%20the%20Front%20End%20and%20[[Basis%20Swaps) Markets#[Forward Rate Agreements](../../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%2012/EURIBOR%20Forward%20Rate%20Agreements%20and%20Futures.md) (FRAs) [Overview](../../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%201%20-%20Purpose%20and%20Structure%20of%20Financial%20Markets/Overview%20of%20Financial%20Markets.md)|FRA]] could be settled on day 120,  the point at which the borrowing rate becomes known and the borrowing takes place,  or settled in arrears on day 211,  when the loan is repaid.

FRAs are a [forward contract](../../../Clippings/Forward%20Points%20in%20Currency.md) based on the interest rate,  and as such do not entail the actual lending of money. Rather,  the borrower who enters an [Basis Swap](A%20Guide%20to%20the%20Front%20End%20and%20[[Basis%20Swaps) Markets#[Forward Rate Agreements](../../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%2012/EURIBOR%20Forward%20Rate%20Agreements%20and%20Futures.md) (FRAs) [Overview](../../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%201%20-%20Purpose%20and%20Structure%20of%20Financial%20Markets/Overview%20of%20Financial%20Markets.md)|FRA]] is paid if a reference rate is above the [Basis Swap](A%20Guide%20to%20the%20Front%20End%20and%20[[Basis%20Swaps) Markets#[Forward Rate Agreements](../../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%2012/EURIBOR%20Forward%20Rate%20Agreements%20and%20Futures.md) (FRAs) [Overview](../../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%201%20-%20Purpose%20and%20Structure%20of%20Financial%20Markets/Overview%20of%20Financial%20Markets.md)|FRA]] rate,  and the borrower pays if the reference rate is below the [Basis Swap](A%20Guide%20to%20the%20Front%20End%20and%20[[Basis%20Swaps) Markets#[Forward Rate Agreements](../../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%2012/EURIBOR%20Forward%20Rate%20Agreements%20and%20Futures.md) (FRAs) [Overview](../../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%201%20-%20Purpose%20and%20Structure%20of%20Financial%20Markets/Overview%20of%20Financial%20Markets.md)|FRA]] rate. The actual borrowing is conducted by the borrower independently of the FRA. We will suppose that the reference rate used in the [Basis Swap](A%20Guide%20to%20the%20Front%20End%20and%20[[Basis%20Swaps) Markets#[Forward Rate Agreements](../../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%2012/EURIBOR%20Forward%20Rate%20Agreements%20and%20Futures.md) (FRAs) [Overview](../../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%201%20-%20Purpose%20and%20Structure%20of%20Financial%20Markets/Overview%20of%20Financial%20Markets.md)|FRA]] is the same as the actual borrowing cost of the borrower.

## [](../../../Fixed%20Income%20Asset%20Pricing/Fixed%20Income%20Lecture%20Notes/A%20Guide%20to%20the%20Front%20End%20and%20Basis%20Swap%20Markets.md#Forward%20Rate%20Agreements%20(FRAs)%20Overview|FRA) SETTLEMENT IN ARREARS

First consider what happens if the [Basis Swap](A%20Guide%20to%20the%20Front%20End%20and%20[[Basis%20Swaps) Markets#[Forward Rate Agreements](../../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%2012/EURIBOR%20Forward%20Rate%20Agreements%20and%20Futures.md) (FRAs) [Overview](../../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%201%20-%20Purpose%20and%20Structure%20of%20Financial%20Markets/Overview%20of%20Financial%20Markets.md)|FRA]] is settled in September,  on day 211,  the loan repayment date. In that case,  the payment to the borrower should be$$r_{quarterly} - r_{FRA} \times  \text{notional principal}$$

- Thus,  if the borrowing rate is 1.5%,  the payment under the [Basis Swap](A%20Guide%20to%20the%20Front%20End%20and%20[[Basis%20Swaps) Markets#[Forward Rate Agreements](../../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%2012/EURIBOR%20Forward%20Rate%20Agreements%20and%20Futures.md) (FRAs) [Overview](../../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%201%20-%20Purpose%20and%20Structure%20of%20Financial%20Markets/Overview%20of%20Financial%20Markets.md)|FRA]] should be (0.015 − 0.018) × 300, 000

Since the rate is lower than the [Basis Swap](A%20Guide%20to%20the%20Front%20End%20and%20[[Basis%20Swaps) Markets#[Forward Rate Agreements](../../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%2012/EURIBOR%20Forward%20Rate%20Agreements%20and%20Futures.md) (FRAs) [Overview](../../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%201%20-%20Purpose%20and%20Structure%20of%20Financial%20Markets/Overview%20of%20Financial%20Markets.md)|FRA]] rate,  the borrower pays the [Basis Swap](A%20Guide%20to%20the%20Front%20End%20and%20[[Basis%20Swaps) Markets#[Forward Rate Agreements](../../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%2012/EURIBOR%20Forward%20Rate%20Agreements%20and%20Futures.md) (FRAs) [Overview](../../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%201%20-%20Purpose%20and%20Structure%20of%20Financial%20Markets/Overview%20of%20Financial%20Markets.md)|FRA]] counterparty. Similarly,  if the borrowing rate turns out to be 2.0%,  the payment under the [Basis Swap](A%20Guide%20to%20the%20Front%20End%20and%20[[Basis%20Swaps) Markets#[Forward Rate Agreements](../../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%2012/EURIBOR%20Forward%20Rate%20Agreements%20and%20Futures.md) (FRAs) [Overview](../../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%201%20-%20Purpose%20and%20Structure%20of%20Financial%20Markets/Overview%20of%20Financial%20Markets.md)|FRA]] should be

(0.02 − 0.018) ×$100 m =$200, 000

Settling the [Basis Swap](A%20Guide%20to%20the%20Front%20End%20and%20[[Basis%20Swaps) Markets#[Forward Rate Agreements](../../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%2012/EURIBOR%20Forward%20Rate%20Agreements%20and%20Futures.md) (FRAs) [Overview](../../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%201%20-%20Purpose%20and%20Structure%20of%20Financial%20Markets/Overview%20of%20Financial%20Markets.md)|FRA]] in arrears is simple and seems like the obvious way for the contract to work. However,  settlement can also occur at the time of borrowing.

## [](../../../Fixed%20Income%20Asset%20Pricing/Fixed%20Income%20Lecture%20Notes/A%20Guide%20to%20the%20Front%20End%20and%20Basis%20Swap%20Markets.md#Forward%20Rate%20Agreements%20(FRAs)%20Overview|FRA) SETTLEMENT AT THE TIME OF BORROWING

If the [Basis Swap](A%20Guide%20to%20the%20Front%20End%20and%20[[Basis%20Swaps) Markets#[Forward Rate Agreements](../../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%2012/EURIBOR%20Forward%20Rate%20Agreements%20and%20Futures.md) (FRAs) [Overview](../../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%201%20-%20Purpose%20and%20Structure%20of%20Financial%20Markets/Overview%20of%20Financial%20Markets.md)|FRA]] is settled in June,  at the time the money is borrowed,  payments will be less than when settled in arrears because the borrower has time to earn interest on the [Basis Swap](A%20Guide%20to%20the%20Front%20End%20and%20[[Basis%20Swaps) Markets#[Forward Rate Agreements](../../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%2012/EURIBOR%20Forward%20Rate%20Agreements%20and%20Futures.md) (FRAs) [Overview](../../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%201%20-%20Purpose%20and%20Structure%20of%20Financial%20Markets/Overview%20of%20Financial%20Markets.md)|FRA]] settlement. In practice,  therefore,  the [Basis Swap](A%20Guide%20to%20the%20Front%20End%20and%20[[Basis%20Swaps) Markets#[Forward Rate Agreements](../../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%2012/EURIBOR%20Forward%20Rate%20Agreements%20and%20Futures.md) (FRAs) [Overview](../../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%201%20-%20Purpose%20and%20Structure%20of%20Financial%20Markets/Overview%20of%20Financial%20Markets.md)|FRA]] settlement is tailored by the reference rate prevailing on the settlement (borrowing) date. (Tailing in this context means that we reduce the payment to reflect the interest earned between June andSeptember.) Thus,  the payment for a borrower is$$Notional\ principal \times \frac{(r_{quarterly} - r_{FRA})}{1 + r_{quarterly}}\tag{(8)}$$

- If$r_{quarterly} = 1.5\%$,  the payment in June is$-295, 566.50 \div (1 + 0.015)$
- By definition,  the future value of this is -$300, 000. In order to make this payment,  the borrower can borrow an extra$295, 566.50,  which results in an extra$300, 000 loan payment in September.
- If on the other hand$r_{quarterly} = 2.0\%$,  the payment is$\$200, 000 = \$196, 078.43 \div (1 + 0.02)$
- The borrower can invest this amount,  which gives$200, 000 in September,  an amount that offsets the extra borrowing cost.

## [](../../../Fixed%20Income%20Asset%20Pricing/Fixed%20Income%20Lecture%20Notes/A%20Guide%20to%20the%20Front%20End%20and%20Basis%20Swap%20Markets.md#Forward%20Rate%20Agreements%20(FRAs)%20Overview|Forward%20Rate%20Agreements) (FRAS)

To summarize,  an [Basis Swap](A%20Guide%20to%20the%20Front%20End%20and%20[[Basis%20Swaps) Markets#[Forward Rate Agreements](../../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%2012/EURIBOR%20Forward%20Rate%20Agreements%20and%20Futures.md) (FRAs) [Overview](../../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%201%20-%20Purpose%20and%20Structure%20of%20Financial%20Markets/Overview%20of%20Financial%20Markets.md)|FRA]] is just like the stock and [currency forwards](Forward%20Contracts%20on%20Exchange%20Rates.md) we have considered,  both with respect to [pricing](../../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%207/Arbitrage%20Pricing%20of%20Derivatives.md) and synthesizing. If at time 0 we want to lock in a lending rate from time$t$to time$t + s$,  we can create a rate forward synthetically by buying the [underlying asset](../../Financial%20Derivatives%20and%20Quantitative%20Methods/Risk%20Neutral%20Pricing%20of%20Options.md) (the bond maturing at$t + s$) and borrowing ([shorting](../../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%202%20-%20Spot%20Markets/Short%20Selling.md)) the bond maturing at$t$.

In general,  we have the following conclusions concerning a rate forward covering the period$t$to$t + s$:

- The [forward rate](../../../Clippings/Forward%20Points%20in%20Currency.md) we can obtain is the implied [forward rate](../../../Clippings/Forward%20Points%20in%20Currency.md)—i.e., $f(t,  t+s) = \frac{(1+r(0,  t+s))^{t+s}}{(1+r(0,  t))^t} - 1$.
- We can synthetically create the payoff to an FRA, $\frac{(1+r(t,  t+s))^{s}}{(1+r(0,  t))^t}$,  by borrowing to buy a bond maturing at$t + s$,  i.e.,  by:
  1. Buying$1 + r(t,  t+s)$of the zero-coupon bond maturing on day$t+s$,
  1. [Shorting](../../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%202%20-%20Spot%20Markets/Short%20Selling.md)$1$zero-coupon bond maturing on day$t$.

Demonstration that going long a [forward contract](../../../Clippings/Forward%20Points%20in%20Currency.md) at the price $F_{0, T} = S_0e^{(r-\delta)T}$ and lending the present value of the [forward price](../../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%2011/Forward%20Contracts%20and%20Forward%20Prices.md) creates a synthetic share of the index at time$T$.

| Transaction        | Time 0                | Time T (expiration)     |
|--------------------|-----------------------|-------------------------|
| Long one forward   | 0                     |$S_T - F_{0, T}$|
| Lend$S_0e^{-\delta T}$|$-S_0e^{-\delta T}$|$+S_0e^{(r-\delta)T}$|
| **Total**             |$-S_0e^{-\delta T}$|$S_T$|

## TABLE 5

Demonstration that buying$e^{-\delta T}$shares of the index and [shorting](../../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%202%20-%20Spot%20Markets/Short%20Selling.md) a forward creates a synthetic bond.

| Transaction | Time 0 | Time T (expiration) |
| ---- | ---- | ---- |
| Buy$e^{-\delta T}$units of the index |$-S_0e^{-\delta T}$|$+S_T$|
| Short one forward | 0 |$F_{0, T} - S_T$|
| **Total** |$-S_0e^{-\delta T}$|$F_{0, T}$|

# SYNTHETIC FRAS

Suppose that today is day 0. By using a [forward rate](../../../Clippings/Forward%20Points%20in%20Currency.md) agreement,  we will be able to invest$1 on day 120 and be guaranteed a 91-day return of 1.8%. We can synthetically create the same effect as with an [Basis Swap](A%20Guide%20to%20the%20Front%20End%20and%20[[Basis%20Swaps) Markets#[Forward Rate Agreements](../../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%2012/EURIBOR%20Forward%20Rate%20Agreements%20and%20Futures.md) (FRAs) [Overview](../../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%201%20-%20Purpose%20and%20Structure%20of%20Financial%20Markets/Overview%20of%20Financial%20Markets.md)|FRA]] by trading zero-coupon bonds.

In order to accomplish this we need to guarantee cash flows of 1 on day 120,  and +$1.018 on day 211. First,  let's get a general sense of the transaction. To match the [Basis Swap](A%20Guide%20to%20the%20Front%20End%20and%20[[Basis%20Swaps) Markets#[Forward Rate Agreements](../../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%2012/EURIBOR%20Forward%20Rate%20Agreements%20and%20Futures.md) (FRAs) [Overview](../../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%201%20-%20Purpose%20and%20Structure%20of%20Financial%20Markets/Overview%20of%20Financial%20Markets.md)|FRA]] cash flows,  we want cash going out on day 120 and coming in on day 211. To accomplish this,  on day 0 we will need to borrow with a 120-day maturity (to generate a cash outflow on day 120) and lend with a 211-day maturity (to generate a cash inflow on day 211). Moreover,  we want the day 0 value of the [borrowing and lending](../Teaching%20Note%203%20Swaps-%20Financial%20Instruments/Swaps%20Types.md) to be equal so that there is no initial [cash flow](../../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%201%20-%20Purpose%20and%20Structure%20of%20Financial%20Markets/Preview%20of%20the%20Book.md). This description tells us what we need to do.

In general,  suppose that today is day 0,  and that at time t we want to lend$1 for the period s,  earning the implied forward rate$r_0(t,  t + s)$over the interval from t to$t + s$. To simplify the notation in this section, $r_0(t,  t + s)$will denote the nonannualized percent return from time t to time s.

Recall first that$$1 + r_0(t,  t+s) = \frac{P(0, t)}{P(0, t+s)}$$

The strategy we use is to:

1. Buy$1 + r_0(t, t+s)$zero-coupon bonds maturing at time$t+s$.
1. Short-sell$1$zero-coupon bond maturing at time$t$.

To summarize,  we have shown that an [Basis Swap](A%20Guide%20to%20the%20Front%20End%20and%20[[Basis%20Swaps) Markets#[Forward Rate Agreements](../../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%2012/EURIBOR%20Forward%20Rate%20Agreements%20and%20Futures.md) (FRAs) [Overview](../../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%201%20-%20Purpose%20and%20Structure%20of%20Financial%20Markets/Overview%20of%20Financial%20Markets.md)|FRA]] is just like the stock and [currency forwards](Forward%20Contracts%20on%20Exchange%20Rates.md) we have considered,  both with respect to [pricing](../../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%207/Arbitrage%20Pricing%20of%20Derivatives.md) and synthesizing. If at time 0 we want to lock in a lending rate from time t to time t + s,  we can create a rate forward synthetically by buying the [underlying asset](../../Financial%20Derivatives%20and%20Quantitative%20Methods/Risk%20Neutral%20Pricing%20of%20Options.md) (the bond maturing at t + s) and borrowing ([shorting](../../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%202%20-%20Spot%20Markets/Short%20Selling.md)) the bond maturing at day t.

In general,  we have the following conclusions concerning a rate forward covering the period$t_1$to$t_2$:

- The [forward rate](../../../Clippings/Forward%20Points%20in%20Currency.md) we can obtain is the implied [forward rate](../../../Clippings/Forward%20Points%20in%20Currency.md)—i.e., $$r_{t_0}(t_1, t_2) = \frac{P_{t_0}(t_0, t_1)}{P_{t_0}(t_0, t_2)} - 1$$

.

- We can synthetically create the payoff to an FRA, $r_{t_0}(t_1, t_2) - r_{t_1}(t_1, t_2)$,  by borrowing to buy a bond maturing at$t_2$,  i.e.,  by:
	- 1. Buying$1 + r_{t_1}(t_1, t_2)$zero-coupon bonds maturing at$t_2$
	- 2. [Shorting](../../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%202%20-%20Spot%20Markets/Short%20Selling.md)$1$zero-coupon bond maturing on day$t_1$.
## EURODOLLAR FUTURES

[Eurodollar futures](../../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%206%20Options%20on%20Non-Price%20Variables/Convexity-Adjusted%20Models%20for%20LIBOR%20Forwards%20Qu.md) contracts are similar to FRAs in that they can be used to guarantee a borrowing rate. There are subtle differences between FRAs and Eurodollar contracts,  however; that are important to understand.

### EXAMPLE PROBLEM

Assume the June [Eurodollar futures](../../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%206%20Options%20on%20Non-Price%20Variables/Convexity-Adjusted%20Models%20for%20LIBOR%20Forwards%20Qu.md) price is 92.8. This translates into the implied interest rate,  which is calculated as$100 - 92.8 = 7.2\%$on an annual basis for a \$1M loan from June to September. Suppose the June Eurodollar futures price is 92.8,  which implies a 3-month [](../../../Fixed%20Income%20Asset%20Pricing/Fixed%20Income%20Lecture%20Notes/A%20Guide%20to%20the%20Front%20End%20and%20Basis%20Swap%20Markets.md#London%20Interbank%20Offered%20Rate%20(LIBOR)|LIBOR) is$100 - 92.8 = 7.2\%$. If we enter into a single short Eurodollar contract at expiration it will be:$$
(\text{[Futures Price](../../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%2011/Futures%20Price%20and%20the%20Quality%20Option%20Before%20E.md)}) - (\text{Spot Price}) \times (\text{Contract Size}) = (92.8 - 94) \times 100 \times \$25 = -\$30, 000$$

If [](../../../Fixed%20Income%20Asset%20Pricing/Fixed%20Income%20Lecture%20Notes/A%20Guide%20to%20the%20Front%20End%20and%20Basis%20Swap%20Markets.md#London%20Interbank%20Offered%20Rate%20(LIBOR)|LIBOR) = 8% (quarterly = 2.0%),  we earn an extra$20, 000 in interest and the invested proceeds from the Eurodollar contract are:$$((100 - 8) \times 100 \times \$25) = \$230, 000$$

We multiply by 100 twice: once to account for 100 contracts,  and the second time to convert the change in the futures price to basis points. Similarly,  if the borrowing rate is 2%,  we have:$$((92.8 - 92) \times 100 \times \$25) \times 100 = \$200, 000$$

This is like the payment on an [](../../../Fixed%20Income%20Asset%20Pricing/Fixed%20Income%20Lecture%20Notes/A%20Guide%20to%20the%20Front%20End%20and%20Basis%20Swap%20Markets.md#Forward%20Rate%20Agreements%20(FRAs)%20Overview|FRA) paid in arrears,  except that the futures contract settles in June,  but our interest expense is not paid until September. Thus we have 3 months to earn or pay interest on our Eurodollar gain or loss before we actually have to make the interest payment.

### HEDGING WITH [EuroDollar Futures](EuroDollar%20Futures.md)

Recall that when the [](../../../Fixed%20Income%20Asset%20Pricing/Fixed%20Income%20Lecture%20Notes/A%20Guide%20to%20the%20Front%20End%20and%20Basis%20Swap%20Markets.md#Forward%20Rate%20Agreements%20(FRAs)%20Overview|FRA) settles on the borrowing date,  the payment is the *present value* of the change in borrowing cost. The [](../../../Fixed%20Income%20Asset%20Pricing/Fixed%20Income%20Lecture%20Notes/A%20Guide%20to%20the%20Front%20End%20and%20Basis%20Swap%20Markets.md#Forward%20Rate%20Agreements%20(FRAs)%20Overview|FRA) is thus tailed automatically as part of the agreement. With the Eurodollar contract,  by contrast,  we need to tail the position explicitly. We do this by shorting fewer than 100 contracts,  using the implied 3-month Eurodollar rate of 1.8% as our discount factor. Thus,  we enter into: $$\text{Number of Eurodollar contracts} = \frac{100}{1 + 0.018} \approx -98.2318$$

Now consider the gain on the Eurodollar futures position. If [](../../../Fixed%20Income%20Asset%20Pricing/Fixed%20Income%20Lecture%20Notes/A%20Guide%20to%20the%20Front%20End%20and%20Basis%20Swap%20Markets.md#London%20Interbank%20Offered%20Rate%20(LIBOR)|LIBOR) = 6% (quarterly = 1.5%),  our total gain on the short contracts when we initiate borrowing on day 120 will be: $$98.2318 \times (92.8 - 94) \times \$2500 = -\$294, 695$$

But if [](../../../Fixed%20Income%20Asset%20Pricing/Fixed%20Income%20Lecture%20Notes/A%20Guide%20to%20the%20Front%20End%20and%20Basis%20Swap%20Markets.md#London%20Interbank%20Offered%20Rate%20(LIBOR)|LIBOR) = 8% (quarterly = 2.0%),  our total gain on the contracts will be: $$98.2318 \times (92.8 - 92) \times \$2500 = \$196, 464$$

# INTEREST RATE FORWARDS AND FUTURES WALKTHROUGH
- To summarize,  we have shown that an [](../../../Fixed%20Income%20Asset%20Pricing/Fixed%20Income%20Lecture%20Notes/A%20Guide%20to%20the%20Front%20End%20and%20Basis%20Swap%20Markets.md#Forward%20Rate%20Agreements%20(FRAs)%20Overview|FRA) is just like the stock and currency forwards we have considered,  both with respect to pricing and synthesizing.
- If at time 0 we want to lock in a lending rate from time $t$ to time $t + s$,  we can create a rate forward synthetically by buying the underlying asset (the bond maturing at $t + s$) and borrowing (shorting) the bond maturing at $t$.

In general,  we have the following conclusions concerning a rate forward covering the period $[t,  t+s]$:

## FORWARD RATES

- The forward rate we can obtain is the implied forward rate—i.e.,  $f(t,  t+s)$,  is given by:$$ \frac{P(0,  t)}{P(0,  t+s)} - 1$$
- We can synthetically create the payoff to an [Basis Swap](A%20Guide%20to%20the%20Front%20End%20and%20[[Basis%20Swaps) Markets#[Forward Rate Agreements](../../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%2012/EURIBOR%20Forward%20Rate%20Agreements%20and%20Futures.md) (FRAs) [Overview](../../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%201%20-%20Purpose%20and%20Structure%20of%20Financial%20Markets/Overview%20of%20Financial%20Markets.md)|FRA]] by borrowing to buy a bond maturing at $t+s$,  i.e.,  by:

	1. Buying $1 + f(t,  t+s)$ of the zero-coupon bond maturing on day $t+s$,
	1. [Shorting](../../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%202%20-%20Spot%20Markets/Short%20Selling.md) $1$ zero-coupon bond maturing on day $t$.

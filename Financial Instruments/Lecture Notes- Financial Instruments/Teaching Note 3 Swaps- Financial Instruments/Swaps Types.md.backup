---
tags:
  - commodity_swap
  - forward_contract
  - hedging
  - oil_swap
  - swap
aliases:
  - Commodity Swap Example
  - Swap Contract
key_concepts:
  - Borrowing and lending
  - Exchange of payments
  - Forward contract pricing
  - Hedging risky payments
  - Lock in fixed price
---

**[Teaching Note 3 SwapsFinancial Instruments](Teaching%20Note%203%20SwapsFinancial%20Instruments)**
	- [Forward Rates Agreement](Forward%20Rates%20Agreement.md)
	- [Overnight Index Swaps (OIS)](Overnight%20Index%20Swaps%20(OIS).md)
	- [Swaps Types](.md)
	- [Teaching Note 3 SwapsFinancial Instruments](Teaching%20Note%203%20SwapsFinancial%20Instruments)
	- [Swap Contract](The%20Value%20of%20the%20[[Currency%20Swaps) after Initiation]]

+ A swap is a contract calling for an [exchange of payments](.md) over time. One party makes a payment to the other depending upon whether a reference price turns out to be greater or less than a fixed price that is specified in the [swap contract](../../Review%20Session%20Notes/Currency%20Swaps.md). A swap thus provides a means to hedge a stream of risky payments.
+ By entering into an oil swap, for example, an oil buyer confronting a stream of uncertain oil payments can lock in a fixed price for oil over a period of time. The swap payments would be based on the difference between a fixed price for oil and a market price that varies over time.
+ In fact, a [forward contract](../../../Clippings/Forward%20Points%20in%20Currency.md) is a single-payment swap. It is possible to price a multi-date swap—determine the fixed price for oil in the above example—by using information from the set of forward prices with different maturities (i.e., the strip). We will see that swaps are nothing more than forward contracts coupled with [borrowing and lending](.md) money.

## 1. AN EXAMPLE OF A COMMODITY SWAP
+ An industrial producer, IP Inc., is going to buy 100,000 barrels of oil 1 year from today and 2 years from today. Suppose that the [forward price](../../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%2011/Forward%20Contracts%20and%20Forward%20Prices.md) for delivery in 1 year is$110/barrel and in 2 years is$111/barrel.
+ IP can use forward contracts to guarantee the cost of buying oil for the next 2 years. Specifically, IP could enter into [long forward](Forward%20Rates%20Agreement.md) contracts for 100,000 barrels in each of the next 2 years, committing to pay$110/barrel in 1 year and$111/barrel in 2 years.
+ Alternatively, IP could pay an oil supplier$201.638, and the supplier would commit to delivering one barrel in each of the next 2 years. A single payment today for a single delivery of oil in the future is a [prepaid forward](../Teaching%20Note%201-%20Forward%20Rates%20Agreement/Hedging%20Strategies%20with%20Forwards.md). A single payment today to obtain multiple deliveries in the future is a prepaid swap.
+ Although it is possible to enter into a prepaid swap, buyers might worry about the resulting [credit risk](../../../Course%20Notes/Quantitative%20Trading%20Strategies%20Lecture%20Notes.md): They have fully paid for oil that will not be delivered for up to 2 years. For the same reason, the swap counterparty would worry about a postpaid swap, where the oil is delivered and full payment is made after 2 years.
+ A more attractive solution for both parties is to defer payment until the oil is delivered, while still fixing the total price. Typically, a swap will call for equal payments in each year.
+ In this example, 100,000 is the notional amount of the swap, meaning that 100,000 barrels is used to determine the magnitude of the payments when the swap is settled financially.

 ![500](IMG-20240913171226965.png)

Positions and cash flows for a dealer who has an obligation to receive the fixed price in an oil swap and who hedges the exposure by going long year 1 and year 2 oil [forwards](../../../Financial%20Markets/Financial%20Asset%20Pricing%20Theory%20Overview/Chapter%2012%20-%20Derivatives/Forwards%20and%20Futures.md).

## PHYSICAL VERSUS FINANCIAL SETTLEMENT
+ With financial settlement, the oil buyer pays the swap counterparty the difference between the fixed swap price and the spot price. The oil buyer then buys the oil at the spot price.
+ The results for the buyer are the same whether the swap is settled physically or financially. In both cases, the net cost to the oil buyer is the swap price.

## THE SWAP COUNTERPARTY
+ The swap counterparty is a dealer who hedges the oil price risk resulting from the swap. The dealer can hedge by entering into offsetting [long forward](Forward%20Rates%20Agreement.md) or [futures contracts](../../../Financial%20Engineering/Mathematics%20of%20the%20Financial%20Markets.md).
+ When the dealer serves as counterparty and hedges using forward markets, the dealer also has [interest rate exposure](../../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20III%20THE%20PLAYERS/Chapter%2013%20-%20Banks%20Asset-Liability%20Management/Duration%20Gap%20Management.md) from the implicit lending in the swap. So the dealer would also hedge [interest rate risk](../../../Fixed%20Income%20Asset%20Pricing/Analysis%20of%20Fixed%20Income%20Securities.md) using instruments like [Eurodollar futures](../../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%206%20Options%20on%20Non-Price%20Variables/Convexity-Adjusted%20Models%20for%20LIBOR%20Forwards%20Qu.md).
>
> the swap, we are lending the counterparty money for 1 year beginning in 1 year. If the deal is priced fairly, the interest rate on this loan should be the implied [forward interest rate](../../../Clippings/Forward%20Rate.md).

### THE SWAP COUNTERPARTY
+ The swap counterparty is a dealer who hedges the oil price risk resulting from the swap. The dealer can hedge in several ways. First, imagine that an oil seller would like to lock in a fixed selling price of oil. In this case, the dealer locates the oil buyer and seller and serves as a go-between for the swap, receiving payments from one party and passing them on to the other. In practice the fixed price paid by the buyer exceeds the fixed price received by the seller. This price difference is a [Bid and Ask](Class%20Note%209%20[[Class%20Note%209%20Bid%20and%20Ask%20Prices%20With%20Private%20Information) Prices With Private Information|[bid-ask spread](../../../Financial%20Markets%20and%20Institutions/III.%20Liquidity%20of%20Assets/Class%205-%20Private%20Information,%20Liquidity,%20and%20Securitization/Bid%20Ask%20and%20Transaction%20Prices%20in%20a%20Specialist%20Market%20With%20Heterogeneously%20Informed%20Traders.md)]] and is the dealer’s fee.
+ The oil seller receives the spot price for oil and receives the swap price less the spot price, on net receiving the swap price. The oil buyer pays the spot price and receives the spot price less the swap price. The situation where the dealer matches the buyer and seller is called a back-to-back transaction or “matched book” transaction. The dealer bears the [credit risk](../../../Course%20Notes/Quantitative%20Trading%20Strategies%20Lecture%20Notes.md) of both parties but is not exposed to price risk.

 ![500](IMG-20240913171236361.png)

+ A more interesting situation occurs when the dealer serves as counterparty and hedges the transaction using forward markets. Let’s see how this would work.
+ After entering the swap with the oil buyer, the dealer has the obligation to pay the spot price and receive the swap price. If the spot price rises, the dealer can lose money. The dealer has a short position in 1and 2-year oil.
+ The natural hedge for the dealer is to enter into [long forward](Forward%20Rates%20Agreement.md) or [futures contracts](../../../Financial%20Engineering/Mathematics%20of%20the%20Financial%20Markets.md) to offset this short exposure. Table 1 illustrates how this strategy works. As we discussed earlier, there is an implicit loan in the swap and this is apparent in Table 1. The net [cash flow](../../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%201%20-%20Purpose%20and%20Structure%20of%20Financial%20Markets/Preview%20of%20the%20Book.md) for the hedged dealer is a loan, where the dealer receives cash in year 1 and repays it in year 2.

| Year | Payment from Oil Buyer | [Long Forward](Forward%20Rates%20Agreement.md) | Net |
| ---- | ---- | ---- | ---- |
| 1 |$110.483 - year 1 spot price | Year 1 spot price -$110 |$0.483 |
| 2 |$110.483 - year 2 spot price | Year 2 spot price -$111 | -$0.517 |

	- Positions and cash flows for a dealer who has an obligation to receive the fixed price in an oil swap and who hedges the exposure by going long year 1 and year 2 oil [forwards](../../../Financial%20Markets/Financial%20Asset%20Pricing%20Theory%20Overview/Chapter%2012%20-%20Derivatives/Forwards%20and%20Futures.md).
	
+ This example shows that [hedging](../../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%205/Key%20Rates%20O1s%20Durations%20and%20Hedging.md) the oil price risk in the swap, with [forwards](../../../Financial%20Markets/Financial%20Asset%20Pricing%20Theory%20Overview/Chapter%2012%20-%20Derivatives/Forwards%20and%20Futures.md) only, does not fully hedge the position. The dealer also has [interest rate exposure](../../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20III%20THE%20PLAYERS/Chapter%2013%20-%20Banks%20Asset-Liability%20Management/Duration%20Gap%20Management.md). If [interest rates](../../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%202/Interest%20Rate%20Quotations.md) fall, the dealer will not be able to earn a sufficient return from investing$0.483 in year 1 to repay$0.517 in year 2. Thus, in addition to entering oil [forwards](../../../Financial%20Markets/Financial%20Asset%20Pricing%20Theory%20Overview/Chapter%2012%20-%20Derivatives/Forwards%20and%20Futures.md), it would make sense for the dealer to use Eurodollar contracts or [Basis Swap](A%20Guide%20to%20the%20Front%20End%20and%20[[Basis%20Swaps) Markets#[Forward Rate Agreements](../../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%2012/EURIBOR%20Forward%20Rate%20Agreements%20and%20Futures.md) (FRAs) [Overview](../../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%201%20-%20Purpose%20and%20Structure%20of%20Financial%20Markets/Overview%20of%20Financial%20Markets.md)|[Forward Rate Agreements](../../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%2012/EURIBOR%20Forward%20Rate%20Agreements%20and%20Futures.md)]] to hedge the resulting [interest rate exposure](../../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20III%20THE%20PLAYERS/Chapter%2013%20-%20Banks%20Asset-Liability%20Management/Duration%20Gap%20Management.md).

## THE MARKET VALUE OF A SWAP
+ When a swap is first entered, its market value is zero. Once payments begin, the market value is generally nonzero.
+ The market value comes from changes in forward prices over time as well as from the implicit borrowing/lending in the swap payments.
+ To exit a swap, one party can negotiate an offsetting swap to cancel out the original swap obligations. The difference in fixed prices on the original and new swaps determines the cash payment required.

So in summary, swaps are useful for [hedging](../../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%205/Key%20Rates%20O1s%20Durations%20and%20Hedging.md) streams of commodity purchases or sales by fixing the effective price paid over time. Swap dealers offset their exposure using other [derivatives](../../../Financial%20Markets/Financial%20Trading%20and%20Markets/Chapter%209%20Arbitrage%20and%20Hedging%20With%20Options.md) markets. And swaps have nonzero market value once payments commence due to [interest rates](../../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%202/Interest%20Rate%20Quotations.md) and price changes over time due to the implicit [borrowing and lending](.md).

+ A buyer wishing to exit the swap could negotiate terms with the original counterparty to eliminate the swap obligation.
	+ An alternative is to leave the original swap in place and enter into an offsetting swap with the counterparty offering the best price.
		+ The original swap called for the oil buyer to pay the fixed price and receive the floating price; the offsetting swap has the buyer receive the fixed price and pay floating.
		+ The original obligation would be cancelled except to the extent that the fixed prices are different.
		+ However, the difference is known, so oil price risk is eliminated. (There is still [credit risk](../../../Course%20Notes/Quantitative%20Trading%20Strategies%20Lecture%20Notes.md) when the original swap counterparty and the counterparty to the offsetting swap are different. This could be a reason for the buyer to prefer offsetting the swap with the original counterparty.)
+ To see how a swap can change in value, suppose that immediately after the buyer enters the swap, the forward curve for oil rises by$2 in years 1 and 2.
+ Thus, the year1 [forward price](../../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%2011/Forward%20Contracts%20and%20Forward%20Prices.md) becomes$112 and the year-2 forward price becomes$113.
	+ The original swap will no longer have a zero market value.
+ Assuming [interest rates](../../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%202/Interest%20Rate%20Quotations.md) are unchanged, the new swap price is$112.483.
+ The buyer could unwind the swap at this point by agreeing to sell oil at$112.483, while the original swap still calls for buying oil at$110.483. - Thus, the net swap payments in each year are (Spot price − 112.483 − spot price) =$2 Original swap New swap
	-The present value of this difference is$2 +$2 =$3.650 1.06 (1.065)2
	+ The buyer can receive a stream of payments worth$3.65 by offsetting the original swap with a new swap.
		-Thus,$3.65 is the market value of the swap.

 ![500](IMG-20240913171241643.png)

# Swaps Types

The [swap rate calculation](../../Assignments/Financial%20Instruments%20Midterm%202022%20Solutions.md) equates the value of a prepaid swap with the present value of the fixed swap payments.

## FIXED QUANTITY SWAPS

We first consider swaps with a notional amount that is fixed over time.^1^ Suppose there are n swap settlements, occurring on dates $t_i, i = 1, …, n$. The forward prices on these dates are given by $F_{0,t_i}$. We will account for [interest rates](../../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%202/Interest%20Rate%20Quotations.md) by using bond price notation. The price of a zero-coupon bond maturing on date $t_i$ is $P(0, t_i)$. This price is the factor for discounting a fixed payment from date $t_i$ to date 0.

If the buyer at time zero were to enter into forward contracts to purchase one unit on each of the n dates, the present value of payments would be the present value of the forward prices, which equals the price of the prepaid swap: $$Prepaid\ Swap = \sum_{i=1}^{n} F_{0,t_i} P(0,t_i) \tag{1}$$
We determine the fixed swap price, R, by requiring that the present value of the swap payments equal the value of the prepaid swap. Thus, we have $$\sum_{i=1}^{n} R P(0,t_i) = \sum_{i=1}^{n} F_{0,t_i} P(0,t_i) \tag{2}$$
Solving for R gives $$R = \frac{\sum_{i=1}^{n} P(0,t_i) F_{0,t_i}}{\sum_{i=1}^{n} P(0,t_i)} \tag{3}$$
The expression $\sum_{i=1}^{n} P(0,t_i) F_{0,t_i}$ is the present value of payments implied by the strip of forward prices. The expression $\sum_{i=1}^{n} P(0,t_i)$is the present value of a$1 annuity. Thus, the [swap rate](../../../Fixed%20Income%20Asset%20Pricing/Fixed%20Income%20Lecture%20Notes/Teaching%20Note%204%20Interest%20Rate%20Derivatives.md) annuitizes the interest payments on the floating-rate bond.

A different way to motivate the swap price calculation is to note that the present value of the differences between the swap price and the forward prices must equal zero:$$\sum_{i=1}^{n} P(0,t_i)[R - F_{0,t_i}] = 0 \tag{4}$$
This also gives rise to equation (3). 

We can rewrite equation (3) to make it easier to interpret:$$R = \sum_{i=1}^{n} \left[\frac{P(0,t_i)}{\sum_{j=1}^{n} P(0,t_j)} \right] F_{0,t_i}$$
The terms in square brackets sum to 1. This form of equation (3) emphasizes that the [fixed swap rate](../../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%202/Interest%20Rate%20Swaps.md) is a weighted average of the forward prices, where zero-coupon bond prices are used to determine the weights.

Figure 6 displays a [swap curve](../../../Financial%20Engineering/Fixed%20Income%20Derivatives/Determining%20the%20Expression%20for%20the%20Fair%20Value%20of%20the%20Swap%20Spread.md) for natural gas, constructed using equation 3. The natural gas price exhibits seasonality. The swap price is a weighted average of natural gas forward prices over the life of the swap, and thus exhibits less variation. In Figure 6, the average natural gas [futures price](../../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%2011/Futures%20Price%20and%20the%20Quality%20Option%20Before%20E.md) climbs so the [swap curve](../../../Financial%20Engineering/Fixed%20Income%20Derivatives/Determining%20the%20Expression%20for%20the%20Fair%20Value%20of%20the%20Swap%20Spread.md) climbs as well.

 ![500](IMG-20240913171244895.png)

A commodity buyer might prefer a swap in which quantities vary over time. For example, a natural gas buyer could enter into a swap supplying a greater quantity of gas during the heating season. A buyer might also wish to fix different prices in different seasons. For example, there could be seasonal variation in the price of the output produced using natural gas as an input. How do we determine the swap price with seasonally varying quantities and prices?

Let$Q_{t_i}$denote the quantity of the commodity to be purchased at time$t_i$. If a buyer pays in advance, the prepaid swap price is$$Prepaid\ Swap = \sum_{i=1}^{n} Q_{t_i} F_{0,t_i} P(0,t_i) \tag{5}$$
Consider a swap in which the buyer pays$RQ_{t_i}$for$Q_{t_i}$units of the commodity. The present value of these fixed payments (fixed per unit of the commodity) must equal the prepaid swap price, so that$$Prepaid\ Swap = \sum_{i=1}^{n} Q_{t_i} F_{0,t_i} P(0,t_i) \tag{6}$$
$$R = \frac{\sum_{i=1}^{n} Q_{t_i} P(0,t_i) F_{0,t_i}}{\sum_{i=1}^{n} Q_{t_i} P(0,t_i)} \tag{7}$$
The equation shows that if we are going to buy more gas when the [forward price](../../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%2011/Forward%20Contracts%20and%20Forward%20Prices.md) is high, we have to weight more heavily the [forward price](../../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%2011/Forward%20Contracts%20and%20Forward%20Prices.md) in those months. When$Q_t = 1$, the formula is the same as equation (3).

+ Once again, another way to derive this equation is to require that the present value of the quantity-weighted difference between the swap price and the forward prices is zero:$$\sum_{i=1}^{n} P(0,t_i) Q_{t_i} (R - F_{0,t_i}) = 0$$
+ We can also permit prices to be time-varying. If, for example, we let the summer swap price be denoted by$R_s$and the winter price by$R_w$, then the summer and winter swap prices can be any prices for which the value of the prepaid swap equals the present value of the fixed swap payments:$$\sum_{i \in summer} P(0,t_i)Q_{t_i}F_{0,t_i} + \sum_{i \in winter} P(0,t_i)Q_{t_i}F_{0,t_i} = \sum_{i \in summer} P(0,t_i)Q_{t_i}R_s + \sum_{i \in winter} P(0,t_i)Q_{t_i}R_w$$
+ The notations$i \in summer$and$i \in winter$mean to sum over only the months in those seasons. 
+ This gives us one equation and two unknowns,$R_s$and$R_w$.
+ Once we fix one of the two prices, the equation will give us the other.

# INTEREST RATE SWAPS  
## A SIMPLE INTEREST RATE SWAP

Suppose that XYZ Corp. has$200m of [floating-rate debt](../../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%2013/Uses%20of%20Interest%20Rate%20Swaps.md) at LIBOR—meaning that every year XYZ pays that year's current LIBOR—but would prefer to have fixed-rate debt with 3 years to maturity. There are several ways XYZ could effect this change.

First, XYZ could change their [interest rate exposure](../../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20III%20THE%20PLAYERS/Chapter%2013%20-%20Banks%20Asset-Liability%20Management/Duration%20Gap%20Management.md) by retiring the [floating-rate debt](../../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%2013/Uses%20of%20Interest%20Rate%20Swaps.md) and issuing fixed-rate debt in its place. However, an actual purchase and sale of debt has transaction costs.  

+ In other words, an [interest rate swap](../../../Financial%20Engineering/Primer%20on%20Interest%20Rate%20Swaps.md) is equivalent to borrowing at a floating rate to buy a fixed-rate bond.$$r_0(t_1,t_2) = \frac{P(0,t_1)}{P(0,t_2)} - 1$$
+ Therefore equation (4) can be rewritten
$$
\begin{aligned}\sum_{i=1}^nP(0,t_i)[R-r(t_{i-1},t_i)]&=\sum_{i=1}^nP(0,t_i)\left[R-\frac{P(0,t_{i-1})}{P(0,t_i)}+1\right]\end{aligned}
$$

Setting this equation equal to zero and solving for$R$gives us

You may recognize this as the formula for the coupon on a par coupon bond. This in turn can be rewritten as
$$
R\sum_{i=1}^nP(0,t_i)+P(0,t_n)=1
$$

This is the valuation equation for a bond priced at par with a coupon rate of$R$
The conclusion is that the [swap rate](../../../Fixed%20Income%20Asset%20Pricing/Fixed%20Income%20Lecture%20Notes/Teaching%20Note%204%20Interest%20Rate%20Derivatives.md) is the coupon rate on a par coupon bond. This result is intuitive since a firm that swaps from floating-rate to fixed-rate exposure ends up with the economic equivalent of a fixed-rate bond.

# SWAP RATE AND BOND CALCULATIONS

The [interest rate swap](../../../Financial%20Engineering/Primer%20on%20Interest%20Rate%20Swaps.md) calculation we just illustrated is an application of equation (3), with the implied [forward interest rate](../../../Clippings/Forward%20Rate.md) used as the [forward price](../../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%2011/Forward%20Contracts%20and%20Forward%20Prices.md).

+ There is, however, an equivalent way to express the [swap rate](../../../Fixed%20Income%20Asset%20Pricing/Fixed%20Income%20Lecture%20Notes/Teaching%20Note%204%20Interest%20Rate%20Derivatives.md) that is helpful in the case of an [interest rate swap](../../../Financial%20Engineering/Primer%20on%20Interest%20Rate%20Swaps.md).  
+ The implied [forward rate](../../../Clippings/Forward%20Points%20in%20Currency.md) between times$t_1$and$t_2$,$r_0(t_1,t_2)$, is given by the ratio of zero-coupon bond prices, i.e.,$$r_0(t_1,t_2) = \frac{P(0,t_1)}{P(0,t_2)} - 1 \tag{10}$$
The conclusion is that the [swap rate](../../../Fixed%20Income%20Asset%20Pricing/Fixed%20Income%20Lecture%20Notes/Teaching%20Note%204%20Interest%20Rate%20Derivatives.md) is the coupon rate on a par coupon bond.  

This result is intuitive since a firm that swaps from floating-rate to fixed-rate exposure ends up with the economic equivalent of a fixed-rate bond.

# 4. CURRENCY SWAPS
+ Firms sometimes issue debt denominated in a foreign [currency](../Teaching%20Note%201-%20Forward%20Rates%20Agreement/Forwards%20and%20Futures%20Notes.md).
+ A firm may do this as a hedge against revenues received in that [currency](../Teaching%20Note%201-%20Forward%20Rates%20Agreement/Forwards%20and%20Futures%20Notes.md), or because perceived [borrowing costs](../../../Financial%20Engineering/Notes%20on%20Currency%20Swaps.md) in that [currency](../Teaching%20Note%201-%20Forward%20Rates%20Agreement/Forwards%20and%20Futures%20Notes.md) are lower.
+ Whatever the reason, if the firm later wants to change the [currency](../Teaching%20Note%201-%20Forward%20Rates%20Agreement/Forwards%20and%20Futures%20Notes.md) to which they have exposure, there are a variety of ways to do so.
+ The firm can use forward contracts to hedge [exchange rate risk](../../Assignments/PSET%203%20Financial%20Instruments.md), or it can use a [currency](../Teaching%20Note%201-%20Forward%20Rates%20Agreement/Forwards%20and%20Futures%20Notes.md) swap, in which payments are based on the difference in debt payments denominated in different currencies.
+ To understand these alternatives, let's consider the example of a dollar-based firm that has euro-denominated 3-year fixed-rate debt.
+ The annual coupon rate is ρ. The firm is obligated to make a series of payments that are fixed in euro terms but variable in dollar terms.
+ Since the payments are known, eliminating euro exposure is a straightforward [hedging](../../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%205/Key%20Rates%20O1s%20Durations%20and%20Hedging.md) problem using [currency forwards](../Teaching%20Note%201-%20Forward%20Rates%20Agreement/Forward%20Contracts%20on%20Exchange%20Rates.md). 
	+ We have cash flows of −ρ each year, and −(1 + ρ) in the maturity year. 
	+ If [currency](../Teaching%20Note%201-%20Forward%20Rates%20Agreement/Forwards%20and%20Futures%20Notes.md) forward prices are$F_{0,t}$, we can enter into long euro forward contracts to acquire at a known exchange rate the euros we need to pay to the lenders. 
	+ Hedged cash flows in year t are$−ρF_{0, t}$.
+ As we have seen in other examples, the forward transactions eliminate risk but leave the firm with a variable (but riskless) stream of cash flows. The variability of hedged cash flows is illustrated in the following example
	+ Suppose the effective annual euro-denominated interest rate is 3.5% and the dollar-denominated rate is 6%. 
	+ The [spot exchange rate](../../Review%20Session%20Notes/Arbitrage%20Opportunity%20Accounting.md) is$0.90/=C. 
	+ A dollar-based firm has a 3-year 3.5% euro-denominated bond with a =EUR 100 par value and price of =EUR 100.
+ The firm wishes to guarantee the dollar value of the payments.
+ Since the firm will make debt payments in euros, it buys the euro forward to eliminate [currency](../Teaching%20Note%201-%20Forward%20Rates%20Agreement/Forwards%20and%20Futures%20Notes.md) exposure.
	+ Table 5 summarizes the transaction and reports the [currency](../Teaching%20Note%201-%20Forward%20Rates%20Agreement/Forwards%20and%20Futures%20Notes.md) forward curve and the unhedged and hedged cash flows.
+ The value of the hedged cash flows is

| Year | Unhedged<br>Euro [Cash Flow](../../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%201%20-%20Purpose%20and%20Structure%20of%20Financial%20Markets/Preview%20of%20the%20Book.md) | Forward<br>Exchange Rate | Hedged<br>Dollar [Cash Flow](../../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%201%20-%20Purpose%20and%20Structure%20of%20Financial%20Markets/Preview%20of%20the%20Book.md) |
| ---- | ---- | ---- | ---- |
| 1 | -€3.5 | 0.922 | -$3.226 |
| 2 | -€3.5 | 0.944 | -$3.304 |
| 3 | -€103.5 | 0.967 | -$100.064 |

	- Unhedged and hedged cash flows for a dollar-based firm with euro-denominated debt.
+ The market-maker's net exposure in this transaction is long a dollar-denominated bond and short a euro-denominated bond. 
+ Table 6 shows that after [hedging](../../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%205/Key%20Rates%20O1s%20Durations%20and%20Hedging.md) there is a series of net cash flows with zero present value. 

| Year | Rate ($/€) | Interest | Euro Interest | Flow |
| ---- | ---- | ---- | ---- | ---- |
| L | 0.9217 | $5.40 | - €3.5 × 0.9217 | $2.174 |
| 2 | 0.9440 | $5.40 | - €3.5 × 0.9440 | $2.096 |
| 3 | 0.9668 | 4.664 |     - ﻿€103.5 × 0.9668 | -$4.664 |

	- Unhedged and hedged cash flows for a dollar-based firm with euro-denominated debt. The effective annual dollar-denominated interest rate is 6% and the effective annual euro-denominated interest rate is 3.5%.

+ As in all the previous examples, the effect of the swap is equivalent to entering into forward contracts, coupled with borrowing or lending.
+ In this case, the firm is lending to the market-maker in the first 2 years, with the implicit loan repaid at maturity.
---
tags:
  - fixed_rate
  - floating_rate
  - interest_rate_swaps
  - par_rates
  - swap_pricing
aliases:
  - Fixed Leg
  - Floating Leg
  - IRS Pricing
  - Par Rate
  - Swap Valuation
key_concepts:
  - Fixed-rate bond
  - Floating-rate bond
  - Notional amounts
  - Par rates
  - Pricing swaps
---

# 2.3 PRICING INTEREST RATE SWAPS  

As mentioned before, it is convenient for [pricing](../Chapter%207/Arbitrage%20Pricing%20of%20Derivatives.md) purposes to assume the fictional exchange of [notional amounts](.md) depicted in Figure 2.1. First, an. exchange of notional amount does not change the value of the swap to either counterparty: paying $\$100$ million and receiving $\$100$ million at exactly the same moment has no value. Second, including the receipt of the fictional notional amount, Counterparty B's position very much resembles buying a fixed-rate bond: B receives an annual coupon and then, at maturity, receives a final "principal" payment. Third, including the receipt of the fictional notional amount, Counterparty A's position very much resembles buying a floating-rate bond, receiving interest that depends on [interest rates](Interest%20Rate%20Quotations.md) as they evolve, and then receiving a final "principal" payment.  

The value of a floating-rate bond that always pays the fair market rate. is worth par, or face amount, today. In terms of Figure 2.1, the value to  

Counterparty A of receiving floating, including the fictional notional amount, is $\$100,000,000$ Intuitively, by the definition of SOFR as a money market rate, Counterparty A can lend $\$1$ to a dealer on any day and. the next day collect that. $\$1$ plus SOFR interest. Therefore, Counterparty A and the dealer would similarly be willing to exchange $\$100,000,000$ today for a floating-rate bond that pays compounded SOFR over some term and $\$100,000,000$ at the end of that term..  

With the [floating leg](.md) of the swap - including the fictional notional amount - worth par, Counterparty B's position can be recast as buying a two-year, $0.1120\%$ bond for par, that is, for. $\$100,000,000$ , where par happens to take the form of the [floating leg](.md) of the swap. In terms of the bond [pricing](../Chapter%207/Arbitrage%20Pricing%20of%20Derivatives.md) methodology of Chapter 1, the present value of the payments on the [fixed leg](.md) of the swap, including the fictional notional amount, must equal par. This insight is so useful and commonplace that the phrase, "[fixed leg](.md) of a swap," is almost always meant to include the fictional notional amount, and the text will adopt this convention from here on.  

Counterparty B's position can also be recast as buying a two-year,. $0.1120\%$ for par, and financing that position by borrowing at the floating. rate. To elaborate, the cash flows from receiving fixed in swap very much resemble those from a leveraged [long position](../../../Financial%20Engineering/Derivatives/Part%20I%20-%20Forwards%20and%20Futures/Chapter%204%20-%20Futures:%20Hedging%20and%20Speculation.md) in a bond. At initiation, Counterparty B neither receives nor pays cash: the swap has no initial [cash flow](../../Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%201%20-%20Purpose%20and%20Structure%20of%20Financial%20Markets/Preview%20of%20the%20Book.md), and the bond is purchased with borrowed money. Over the life of the trade, Counterparty B receives a fixed rate and pays a floating rate: fixed minus floating on the swap, and the coupon rate minus the [short-term financing](../../../Financial%20Markets%20and%20Institutions/III.%20Liquidity%20of%20Assets/Class%207-%20CP,%20Repo,%20and%20the%20Crisis/Asset%20Backed%20Commercial%20Paper%20Understanding%20the%20Risks.md) rate on the bond. And, at maturity, Counterparty B neither receives nor pays a final amount: the swap does not exchange notional amount, and the principal of the bond is used to repay the original loan. In a similar fashion, Counterparty A's position can be recast as borrowing a bond to short it. This perspective on swaps is very useful for understanding how market participants use swaps to adjust their interest rate exposures, which is discussed in Chapter 13..  

Given the discussion to this point, it is clear that swap rates can also be called par rates. A [par rate](.md) of a certain term is defined as the rate paid on an [investment](../../../Advanced%20Investments/An%20Asset%20Allocation%20Primer.md) that costs par and promises to repay par at maturity. If, for example, a 10-year US Treasury bond has a coupon of. $1.625\%$ and costs 100, then $1.625\%$ is the 10-year [par rate](.md) in the Treasury market. While, in. actuality, there is neither "[investment](../../../Advanced%20Investments/An%20Asset%20Allocation%20Primer.md)" in a swap nor a repayment of par, thinking of a swap with an exchange of fictional [notional amounts](.md) allows for the interpretation of the [swap rate](../../../Fixed%20Income%20Asset%20Pricing/Fixed%20Income%20Lecture%20Notes/Teaching%20Note%204%20Interest%20Rate%20Derivatives.md) as the rate "earned" on the [fixed leg](.md), that is, on a par [investment](../../../Advanced%20Investments/An%20Asset%20Allocation%20Primer.md)..  

The text now turns to applying the [pricing](../Chapter%207/Arbitrage%20Pricing%20of%20Derivatives.md) insights of this section to. extract discount factors from [SOFR swap rates](Spot%20Rates.md). To illustrate, the first and second columns of Table 2.1 list [SOFR swap rates](Spot%20Rates.md) of terms 0.5 through 2.0. years, as of May 14, 2021, and Table 2.2 lists the payment dates of these swaps and the number of days between payments. (Note that prices are as. of Friday, May 14, and settlement occurs two business days later, on Tuesday,. May 18.) Using these tables, the following equations link discount factors to quoted [SOFR swap rates](Spot%20Rates.md),  

TABLE 2.1 Swap Rates, Spot Rates, and Forward Rates Implied by USD [SOFR Swaps](../../../Credit%20Markets/Credit%20Market%20PSETS/Advanced%20Usage%20of%20QuantLib%20analytics%20library.md), as of May 14, 2021. Rates Are in Percent..   


<html><body><table><tr><td>Term</td><td>[Swap Rate](../../../Fixed%20Income%20Asset%20Pricing/Fixed%20Income%20Lecture%20Notes/Teaching%20Note%204%20Interest%20Rate%20Derivatives.md)</td><td>[Spot Rate](../../../International%20Finance/The%20Foreign%20Exchange%20Market%20Annotations.md)</td><td>[Forward Rate](../../../Clippings/Forward%20Points%20in%20Currency.md)</td><td>[Discount Factor](../Chapter%201/Discount%20Factors.md)</td></tr><tr><td>0.5</td><td>0.0340</td><td>0.0348</td><td>0.0348</td><td>0.999826</td></tr><tr><td>1.0</td><td>0.0460</td><td>0.0466</td><td>0.0585</td><td>0.999534</td></tr><tr><td>1.5</td><td>0.0670</td><td>0.0681</td><td>0.1111</td><td>0.998979</td></tr><tr><td>2.0</td><td>0.1120</td><td>0.1136</td><td>0.2500</td><td>0.997732</td></tr></table></body></html>  

IABLE 2.2  Days from Settlement or Previous Payment Date for [SOFR Swaps](../../../Credit%20Markets/Credit%20Market%20PSETS/Advanced%20Usage%20of%20QuantLib%20analytics%20library.md) Settling on May 18, 2021.   


<html><body><table><tr><td>Term</td><td>11/18/2021</td><td>05/18/2022</td><td>11/18/2022</td><td>05/18/2023</td></tr><tr><td>0.5</td><td>184</td><td></td><td></td><td></td></tr><tr><td>1.0</td><td></td><td>365</td><td></td><td></td></tr><tr><td>1.5</td><td>184</td><td></td><td>365</td><td></td></tr><tr><td>2.0</td><td></td><td>365</td><td></td><td>365</td></tr></table></body></html>  
$$
\begin{array}{r l r}&{}&{100\left(1+0.0340\%\frac{184}{360}\right)d(0.5)=100}\ &{}&{100\left(1+0.0460\%\frac{365}{360}\right)d(1)=100}\ &{}&{0.0670\frac{184}{360}d(0.5)+100\left(1+0.0670\%\frac{365}{360}\right)d(1.5)=100}\ &{}&{0.1120\frac{365}{360}d(1)+100\left(1+0.1120\%\frac{365}{360}\right)d(2)=100}\end{array}
$$  

In words, Equations (2.12) through (2.15) say that the present value of the [fixed leg](.md) of each SOFR swap equals par. Equation (2.12) says that, for 100 notional amount of the 0.5-year swap, which matures in 184 days, the [fixed leg](.md) pays 100 plus interest on 100 at the 0.5-year [swap rate](../../../Fixed%20Income%20Asset%20Pricing/Fixed%20Income%20Lecture%20Notes/Teaching%20Note%204%20Interest%20Rate%20Derivatives.md) of $0.0340\%$ Furthermore, that payment times the six-month [discount factor](../Chapter%201/Discount%20Factors.md) equals par, or 100. Equation (2.13) says the same for the one-year swap, with its single payment, at the one-year [swap rate](../../../Fixed%20Income%20Asset%20Pricing/Fixed%20Income%20Lecture%20Notes/Teaching%20Note%204%20Interest%20Rate%20Derivatives.md) of. $0.0460\%$ , payable in 365 days.  

The [fixed leg](.md) of the 1.5-year swap makes two payments. Following the rule explained in the previous section, the first payment is made in six months so that the subsequent payment can be made exactly one year later. According to Tables 2.1 and 2.2, the payment in six months, in this case 184 days, on 100 face amount of the 1.5-year swap, is $0.0670$ times 184/360. The payment one year later, which is 1.5 years from settlement, includes interest over that 365-day year plus the notional amount, for a total of 100 plus 0.0670 times 365/360. Equation (2.14) takes the present value of these two payments, multiplying the first by. $d(0.5)$ and the second by. $d(1.5)$ , and sets the sum equal to par..  

Lastly, the [fixed leg](.md) of the two-year swap makes two payments, the first. in 365 days and the next 365 days later. Each interest payment, therefore,. on 100 face amount, is 0.1120 times 365/360, and the notional amount is assumed paid at the end of the second year. Hence, Equation (2.15) sets the. present value of the [fixed leg](.md) of this swap equal to par..  

[Solving Equations](../../../Financial%20Engineering/Inverse%20Matrices%20Solve%20Linear%20Systems.md) (2.12) through (2.15) for the unknown discount factors, analogously to the solution for discount factors in the US Treasury. market in Section 1.2, gives the discount factors in Table 2.1. Chapter 1 introduced discount factors as an expression of the time value of money,. and this chapter, so far, has added swap or par rates. The next two sections. continue with other popular expressions of the time value of money, namely [spot and forward rates](../../../Financial%20Engineering/Mathematics%20of%20the%20Financial%20Markets.md).  
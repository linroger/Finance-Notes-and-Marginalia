---
tags:
  - euribor
  - euribor_futures
  - forward_rate_agreement
  - fra
  - interest_rate_risk
aliases:
  - Euribor
  - Euribor Futures
  - FRA
  - Forward Rate Agreements
key_concepts:
  - Euribor futures contracts
  - Euribor term rates
  - FRA fixed rate
  - 'FRAs: interest rate hedging'
  - Hedging with FRAs
---

# 12.5 EURIBOR FORWARD RATE AGREEMENTS AND FUTURES  

As mentioned earlier, [Euribor](.md) is a set of term rates that continue to be used after the LIBOR transition. In particular, the three-month [Euribor](.md) quote on a particular date represents the rate on a three-month interbank loan that settles in two business days. Furthermore, a term of "three months" in this market refers to the same calendar day three months later. Three-month [Euribor](.md) quoted on June 13, 2022, therefore, represents the rate earned over the 92 days from June 15, 2022, to September 15, 2022.  

[Forward rate agreements](.md) or FRAs are over-the-counter agreements that are used to hedge the [interest rate risk](../../../Fixed%20Income%20Asset%20Pricing/Analysis%20of%20Fixed%20Income%20Securities.md) of future borrowing or lending.. Table 12.9 gives the terms, as of January 14, 2022, of a $\epsilon10$ million notional amount [Euribor](.md) FRA at a fixed rate or contract rate of $-0.47\%$ from June 15 to September 15, 2022. The borrower or fixed-rate payer agrees to pay the lender or fixed-rate receiver on June 15 the quantity listed in the table. The fixed rate of a FRA is set equal to the [Euribor](.md) [forward rate](../../../Clippings/Forward%20Points%20in%20Currency.md) at the time. of the trade, as defined in Chapter 2. In this example, this means that, as of January 14, market participants are willing to commit to borrow or lend from June 15 to September 15 at a rate of $-0.47\%$ . To see that the FRA is fairly priced at this fixed rate, note that a commitment to borrow or lend for three months on June 15 at the then-prevailing market rate, $R$ , is also fair. Therefore, committing to lend on June 15 at $-0.47\%$ and to borrow on June 15 at $R$ is fair, and the resulting September 15 interest payments from those commitments sum to $\epsilon1$ million $\times~(92/360)\times(-0.47\%-R)$ Finally, the present value of that sum as of June 15 equals the quantity in Table 12.9. Hence, the FRA described is fairly priced.  

To illustrate how FRAs can be used for [hedging](../Chapter%205/Key%20Rates%20O1s%20Durations%20and%20Hedging.md), consider a corporation that, as of January 14, 2022, has a line with its bank to borrow $\epsilon10$ million from June 15, 2022, to September 15, 2022, at [Euribor](.md) flat, that is, at no spread. If [Euribor](.md) on June 13 turns out to be. $R$ , then that will be. the rate applied to the loan, and the corporation will owe $\epsilon10$ million $\times$ $[1+(92/360)R]$ on September 15. The corporation, therefore, is exposed to the risk that rates rise from January 14 to June 13.  

The corporation can hedge this risk by locking in the [forward rate](../../../Clippings/Forward%20Points%20in%20Currency.md) of $-0.47\%$ as follows. On January 14, 2022, the corporation agrees to pay. fixed on the FRA in the table. Then, on June 15, the corporation borrows the $\epsilon10$ million it needs plus the quantity it owes on the FRA for three months at the then-prevailing rate, $R$ . In total then, the corporation owes,.  

IABLE 12.9  A 10 Million [Euribor](.md) [Forward Rate](../../../Clippings/Forward%20Points%20in%20Currency.md) Agreement from June 15, 2022, to September 15, 2022, at $-0.47\%$ , as of January 14, 2022.   


<html><body><table><tr><td>Date Description</td></tr><tr><td>1/14/2022 Trade Date</td></tr><tr><td>6/13/2022 3-MonthEuriborObserved tobeR</td></tr><tr><td>6/15/2022 Borrower Pays (net):</td></tr><tr><td>10.000,000x 92 (-0.47% -R) 360 92R</td></tr></table></body></html>  
$$
\begin{array}{r l}&{\left(\epsilon10,000,000+\frac{\epsilon10,000,000\times\frac{92}{360}(-0.47\%-R)}{1+\frac{92}{360}R}\right)\left(1+\frac{92}{360}R\right)}\ &{\qquad=\epsilon10,000,000\left(1+\frac{92}{360}R+\frac{92}{360}(-0.47\%-R)\right)}\ &{\qquad=\epsilon10,000,000\left(1+\frac{92}{360}\times(-0.47\%)\right)}\end{array}
$$  

on September 15, which is exactly the same as if it had borrowed 10 million at a rate of $-0.47\%$ . Intuitively, if realized [Euribor](.md) on June 15 is less than. $-0.47\%$ , the corporation borrows at relatively low rates, but owes money on. the FRA. On the other hand, if realized [Euribor](.md) is greater than. $-0.47\%$ , the corporation borrows at relatively high rates but collects money on the FRA.9  

An exchange-traded alternative to [Euribor](.md) FRAs are [Euribor futures contracts](../Chapter%2016/EURIBOR%20Futures%20Options.md), some of which are listed in Table 12.10, as of January 14, 2022. The tickers begin with "ER," followed by the month and year indicators. The contracts are subject to [daily settlement](../Chapter%2011/Pricing%20and%20Hedging%20Implications%20of%20Daily%20Sett.md), and the final [settlement rate](Three-Month%20SOFR%20Futures.md) is set to three-month [Euribor](.md) on the last trade date. The final [settlement rate](Three-Month%20SOFR%20Futures.md) of the June contract, for example, is three-month [Euribor](.md) on June 13, 2022, which as mentioned earlier, represents the rate on a loan from June 15 to. September 15. Three-month [Euribor futures](.md) are scaled to hedge the change in interest on a 1 million, 90-day loan. Equivalently, a one-basis-point change in rate translates into a [daily settlement](../Chapter%2011/Pricing%20and%20Hedging%20Implications%20of%20Daily%20Sett.md) flow of $\in1,000,000\times0.01\%$ $\times90/360$ , or $\epsilon25$  

The corporation in the FRA example hedges a. $\epsilon10$ million, 92-day loan. from June 15 to September 15, 2022. This time period corresponds exactly. to that covered by [Euribor](.md) set on June 13, which is also the expiration of the June three-month [Euribor](.md) contract. Furthermore, with the market at the levels in Table. $12.10\textrm{--}\textrm{a}$ rate of $-0.47\%$ - the corporation can sell the June. contract to lock in a rate of $-0.47\%$ on its planned borrowing. The number. of contracts required to hedge the. $\epsilon10$ million, 92-day loan with a contract. scaled to a $\epsilon1$ million, 90-day loan, is,  
$$
\frac{\$10,000,0000\times92}{\$1,000,000\times90}=10.22
$$  

TABLE 12.10  Selected Three-Month [Euribor Futures Contracts](../Chapter%2016/EURIBOR%20Futures%20Options.md), as of January 14, 2022. Rates Are in Percent.   


<html><body><table><tr><td>Ticker</td><td>[Delivery Month](One-Month%20SOFR%20Futures.md)</td><td>Last Trade Date</td><td>Price</td><td></td></tr><tr><td>ERH2</td><td>Mar</td><td>03/14/22</td><td>100.540</td><td>-0.540</td></tr><tr><td>ERM2</td><td>Jun</td><td>06/13/22</td><td>100.470</td><td>-0.470</td></tr><tr><td>ERU2</td><td>Sep</td><td>09/19/22</td><td>100.375</td><td>-0.375</td></tr><tr><td>ERZ2</td><td>Dec</td><td>12/19/22</td><td>100.260</td><td>-0.260</td></tr></table></body></html>  

IABLE 12.11 [Hedging](../Chapter%205/Key%20Rates%20O1s%20Durations%20and%20Hedging.md) the Interest Cost of Borrowing 10 Million from June 15, 2022, to September 15, 2022, as of January 14, 2022, with June Three-Month [Euribor](.md) Contracts, Priced Initially at $-0.47\%$ . The Hedge, Not Tailed, Sells 10.22 Contracts. Rates Are in Percent. Other Entries Are in Euro.   


<html><body><table><tr><td>Final Settle- ment Rate</td><td>Loan Interest</td><td>[Futures](../../Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%203%20-%20Futures%20Markets/Futures%20Not%20Subject%20to%20Cash-And-Carry.md) P&L</td><td>Net</td></tr><tr><td>-0.77</td><td>19,677.78</td><td>-7,665.00</td><td>12,012.78</td></tr><tr><td>-0.47</td><td>12,011.11</td><td>0.00</td><td>12,011.11</td></tr><tr><td>-0.17</td><td>4,344.44</td><td>7,665.00</td><td>12,009.44</td></tr></table></body></html>  

The results of the hedge are given in Table 12.11. If rates rise, so that [Euribor](.md) on June 13 turns out to be. $-0.17\%$ , the corporation receives interest of $\epsilon10$ million $\times(92/360)\times$ negative $0.17\%$ , or $\in4,344.44$ ; experiences a [futures](../../Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%203%20-%20Futures%20Markets/Futures%20Not%20Subject%20to%20Cash-And-Carry.md) gain of 30 basis points per contract, for a total gain - ignoring the small effects of [daily settlement](../Chapter%2011/Pricing%20and%20Hedging%20Implications%20of%20Daily%20Sett.md) - of $30\times\in25\times10.22$ , or $\in7,665.00$ ; which together gives an overall gain of 12,009.44. Looking at the table as a whole,. the [futures](../../Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%203%20-%20Futures%20Markets/Futures%20Not%20Subject%20to%20Cash-And-Carry.md) position successfully hedges the cost of borrowing in the sense. of locking in the receipt of about 12,011. The hedge would be exact if the. number of contracts in Equation (12.16) were taken to more decimal places.  

This [hedging](../Chapter%205/Key%20Rates%20O1s%20Durations%20and%20Hedging.md) example is simple in that the corporation plans to borrow over the same period as covered by three-month [Euribor](.md) relevant for the June contract. Along the same lines as the discussion in the context of [hedging](../Chapter%205/Key%20Rates%20O1s%20Durations%20and%20Hedging.md) with [SOFR futures](One-Month%20SOFR%20Futures.md), if the borrowing period were shorter or longer than that covered by the June [Euribor](.md) contract, fewer or more contracts would be needed, and contracts other than June might be used.  

The example in this section is constructed to show the similarity between.   
[Euribor](.md) FRAs and [futures](../../Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%203%20-%20Futures%20Markets/Futures%20Not%20Subject%20to%20Cash-And-Carry.md), but there are significant differences as well.   
FRAs may be subject to bilateral margin agreements, but are not subject to.   
[daily settlement](../Chapter%2011/Pricing%20and%20Hedging%20Implications%20of%20Daily%20Sett.md), like [futures](../../Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%203%20-%20Futures%20Markets/Futures%20Not%20Subject%20to%20Cash-And-Carry.md). FRAs, as over-the-counter products, can be.   
customized for individual trades with respect to dates covered and with respect to notional amount, while the terms of [futures contracts](../../../Financial%20Engineering/Mathematics%20of%20the%20Financial%20Markets.md) are.   
highly standardized. In part because they are customized, however, FRAs are less liquid than [futures](../../Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%203%20-%20Futures%20Markets/Futures%20Not%20Subject%20to%20Cash-And-Carry.md). Hedgers typically need to decide, therefore,.   
whether customization or [liquidity](../../../Financial%20Markets%20and%20Institutions/III.%20Liquidity%20of%20Assets/Class%205-%20Private%20Information,%20Liquidity,%20and%20Securitization/Class%20Note%2010%20Liquidity%20and%20Class%20Note%2010%20Liquidity%20and%20Liquidity%20Managementliquidity%20management.md) is more important in their particular.   
circumstances.  

![](c4e378a5f49fb40adb93d0ba613cccf19d1953dcec2646f286c22c6f2b0186fd.jpg)  
FIGURE 12.5  A Comparison of the June 2022 [Euribor](.md) and the June 2022 [SOFR Futures](One-Month%20SOFR%20Futures.md) Contracts.  

This section concludes with a comparison of [futures](../../Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%203%20-%20Futures%20Markets/Futures%20Not%20Subject%20to%20Cash-And-Carry.md) on a forward-. looking term rate benchmark, like [Euribor](.md), and [futures](../../Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%203%20-%20Futures%20Markets/Futures%20Not%20Subject%20to%20Cash-And-Carry.md) on a backwardlooking compounded overnight benchmark, like SOFR. The top half of Figure 12.5 depicts the June three-month [Euribor](.md) contract, ERM2, while the bottom half depicts the June three-month SOFR contract, SFRM2. Both contracts cover realized [interest rates](../Chapter%202/Interest%20Rate%20Quotations.md) from mid-June to mid-September, though the terminal date differs somewhat, as detailed earlier. The big difference, however, is that ERM2, which references a term rate set on June 13, expires on that date. SFRM2, which references a compounded daily rate that is not known until September 21, does not expire until that later date.  
---
tags:
  - currency_swap
  - eurodollar_futures
  - fx_swap
  - interest_rate_risk
  - swap_contract
aliases:
  - Currency Swap
  - Eurodollar Futures
  - FX Swap
  - Hedging Strategy
  - Swap Value
key_concepts:
  - Borrowing in foreign currency
  - Eurodollar futures hedging
  - Hedging principal amount
  - Plain vanilla FX swaps
  - Swap value formula
---

**[Teaching Note 3 SwapsFinancial Instruments](Teaching%20Note%203%20SwapsFinancial%20Instruments)**
	- [Forward Rates Agreement](Forward%20Rates%20Agreement.md)
	- [Overnight Index Swaps (OIS)](Overnight%20Index%20Swaps%20(OIS).md)
	- [Swaps Types](Swaps%20Types.md)
	- [Teaching Note 3 SwapsFinancial Instruments](Teaching%20Note%203%20SwapsFinancial%20Instruments)
	- [Swap Contract](The%20Value%20of%20the%20[[Currency%20Swaps) after Initiation]]

[PSET 3 [Financial Instruments](../../A%20Practical%20Guide%20for%20Actuaries%20and%20other%20Business%20Professionals..md)](PSET%203%20Financial%20Instruments.md)

## DETERMINING THE VALUE POST-INITIATION
+ What is the value of a [swap contract](../../Review%20Session%20Notes/Currency%20Swaps.md) *after* initiation?
  + Let today be$t$,$K$be the [swap rate](../../../Fixed%20Income%20Asset%20Pricing/Fixed%20Income%20Lecture%20Notes/Teaching%20Note%204%20Interest%20Rate%20Derivatives.md) of the existing swap, and$T_1, T_2, …, T_n$be the remaining payment periods.
  + Use the same logic as for forward and ask: What would the firm have to pay to get out of the position?
  + As before, using a sequence of [forwards](../../../Financial%20Markets/Financial%20Asset%20Pricing%20Theory%20Overview/Chapter%2012%20-%20Derivatives/Forwards%20and%20Futures.md) to get out of the position gives
$$V^{swap}_t = PV \text{ of swap + reverse forward cash flows } = e^{-r_s(T_{1}-t)} \times (K - F_{1,T_1}) + e^{-r_s(T_{2}-t)} \times (K - F_{1,T_2}) + … + e^{-r_s(T_{n}-t)} \times (K - F_{1,T_n})$$

### OBTAINING THE SWAP VALUE FORMULA

+ The swap value formula can be expressed as:$$V^{swap}_t = \sum_{i=1}^n e^{-r_s(T_{i}-t)} \times (K - F_{1,T_i})$$
  + By substituting the value of$F_{1,T_i}$with$S_t$$$V^{swap}*t = K \times \left(\sum*{i=1}^n e^{-r_s(T_{i}-t)} \right) - S_t \times \left(\sum_{i=1}^n e^{-r_e(T_{i}-t)} \right)$$

---

# The Value of the Swap Contract after Initiation
## UNDERSTANDING PLAIN VANILLA FX SWAPS
+ In the example above I assumed the counterparties swap equal payments in the two currencies.
  + The US Firm pays Eur 1 Mil to the Bank every six months and at the same time the Bank pays$1.306 mil to the US Firm.
+ The **plain vanilla FX (or [currency](../Teaching%20Note%201-%20Forward%20Rates%20Agreement/Forwards%20and%20Futures%20Notes.md)) swap** is slightly different, as the two counterparties not only exchange a series of equal cash flows over time (coupons), but also a (larger) notional amount at both the initiation and maturity of the contract.
  + The primary use of **[plain vanilla FX swaps](.md)** is to allow firms to borrow in any foreign [currency](../Teaching%20Note%201-%20Forward%20Rates%20Agreement/Forwards%20and%20Futures%20Notes.md) and hedge the foreign exchange risk.
  + Because of this, it is important for the firm to also hedge the [principal amount](../../Financial%20Derivatives%20and%20Quantitative%20Methods/HSBC-Auto%20callable%20Barrier%20Notes%20with%20Step-up%20Premium.md) of the loan, which must be paid at maturity of the bond.

### EXAMPLE
+ A US firm issues 100 million Euro-denominated 5 year note with coupon$c = 4\%$.
	  - The firm exchanges the proceeds into$126.73 million at the current exchange rate$S_0 = 1.2673$/Eur.
	  - If the firm’s revenues are mainly in US dollars, then the firm is subject to [exchange rate risk](../../Assignments/PSET%203%20Financial%20Instruments.md).
	  - Every six month, the firm must pay Eur$2 mil = 100 mil\times 2\%$.
	  - In addition, at$T = 5$, the firm must pay back the Eur 100 mil principal.
+ A plain vanilla [FX swap](../../../Clippings/Currency%20Swap%20Basics.md) that hedges this [exchange rate risk](../../Assignments/PSET%203%20Financial%20Instruments.md) is as follows:
	  - US Firm receives from Bank 2 mil euros every six months, plus 100 mil euros at$T$;
	  - US Firm pays to bank$K \times 2$mil dollars every six months, plus$K \times 100$mil dollars at$T$.

### SWAP RATE DETERMINATION
+ What is [Swap Rate](../../../Fixed%20Income%20Asset%20Pricing/Fixed%20Income%20Lecture%20Notes/Teaching%20Note%204%20Interest%20Rate%20Derivatives.md)$K$?
  + It is that value of the exchange rate that makes the value of the swap null at inception.

### SWAP VALUE TO THE US FIRM
+ What is the value of the swap to the US firm?
  + In the [swap contract](../../Review%20Session%20Notes/Currency%20Swaps.md), the firm is **long** a Euro-denominated 4% coupon bond with 100 mil Euro principal, and **short**$K$dollar-denominated bond 4% with principal$100 mil.
  + Let$B^{EUR}(t, T)$and$B^{USD}(t, T)$be the value of the two bond (in their respective currencies).
	 + E.g. If the (c.c.) rates are constant across maturities at$r_e =4\%$and$r_s = 6\%$, then$$B^{EUR}(0, T) = 100 \text{ mil } (2\% \times e^{-r_e \times 0.5} + e^{-r_e \times 1} + … + e^{-r_e \times 5}) = EUR 99, 819, 335$$
$$B^{USD}(0, T) = 100 \text{ mil } (2\% \times e^{-r_s \times 0.5} + e^{-r_s \times 1} + … + e^{-r_s \times 5}) = USD 91, 102, 721$$

  + The value of the swap at$t$is then$$V^{swap}_t = S_t \times B^{EUR}(t, T) - K \times B^{USD}(t, T)$$
+ Therefore, at time$t = 0$, the value of$K$that makes the value of the swap equal to zero is$$V^{swap}_0 = 0 \Leftrightarrow S_0 \times B^{EUR}(0, T) = K \times B^{USD}(0, T) \Leftrightarrow K = \frac{S_0 \times B^{EUR}(0, T)}{B^{USD}(0, T)}$$
  + This is the same expression we obtained earlier when the last (notional) payment is zero.
  + In this case we obtain$K = 1.2673 \times 1.0957 = 1.389$.
  + US firm pays$2\times K = 2.778$mil every 6 months, plus$138.9 mil at maturity.

### FIGURE 3: OIL SWAP TERMS BASED ON WTI CRUDE OIL

| Term | Description |
|-------------------------|-------------------------------------------------------------------|
| **Fixed-Price Payer** | Broker-dealer |
| **Floating-Price Payer**| Counterparty |
| **Notional Amount** | 100,000 barrels |
| **Trade Date** | April 18, 2011 |
| **Effective Date** | July 1, 2011 |
| **Termination Date** | September 31, 2011 |
| **Period End Date** | Final [Pricing](../../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%207/Arbitrage%20Pricing%20of%20Derivatives.md) Date of each Calculation Period as defined in the description of the Floating Price. |
| **Fixed Price** | 110.89 USD per barrel |
| **Commodity Reference Price** | OIL-WTI-NYMEX |
| **Floating Price** | The average of the first nearby NYMEX WTI Crude Oil [Futures](../../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%203%20-%20Futures%20Markets/Futures%20Not%20Subject%20to%20Cash-And-Carry.md) settlement prices for each successive day of the Calculation Period during which such prices are quoted |
| **Calculation Period** | Each calendar month during the transaction |
| **Method of Averaging** | Unweighted |
| **Settlement and Payment** | If the Fixed Amount exceeds the Floating Amount for such Calculation Period, the Fixed Price Payer shall pay the Floating Price Payer an amount equal to such excess. If the Floating Amount exceeds the Fixed Amount for such Calculation Period, the Floating Price Payer shall pay the Fixed Price Payer an amount equal to such excess. |
| **Payment Date** | 5 business days following each Period End Date |

### FIGURE 4: TREASURY-NOTE FUTURES CONTRACT SPECIFICATIONS

| Specification | Details |
| ---- | ---- |
| **Where traded** | CME Group/CBOT |
| **Underlying** | 6% 10-year Treasury note |
| **Size** | $100,000 Treasury note |
| **Months** | March, June, September, December, out 15 months |
| **Trading ends** | Seventh business day preceding last business day of month. Delivery until last business day of the month. |
| **Delivery** | Physical T-note with at least 6.5 years to maturity and not more than 10 years to maturity. Price paid to the short for notes with other than 6% coupon is determined by multiplying [futures price](../../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%2011/Futures%20Price%20and%20the%20Quality%20Option%20Before%20E.md) by a conversion factor. The conversion factor is the price of the delivered note ($1 par value) to yield 6%. |
| Settlement | until last business day of the month. |

In the [Eurodollar futures](../../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%206%20Options%20on%20Non-Price%20Variables/Convexity-Adjusted%20Models%20for%20LIBOR%20Forwards%20Qu.md) price, we have to consider the [convexity](../../../Fixed%20Income%20Asset%20Pricing/Problem%20Sets/PSET%20II%20Fixed%20Income%20Asset%20Pricing%201.md) bias, which refers to the difference in [convexity](../../../Fixed%20Income%20Asset%20Pricing/Problem%20Sets/PSET%20II%20Fixed%20Income%20Asset%20Pricing%201.md) between the [Basis Swap](A%20Guide%20to%20the%20Front%20End%20and%20[[Basis%20Swaps) Markets#[Forward Rate Agreements](../../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%2012/EURIBOR%20Forward%20Rate%20Agreements%20and%20Futures.md) (FRAs) [Overview](../../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%201%20-%20Purpose%20and%20Structure%20of%20Financial%20Markets/Overview%20of%20Financial%20Markets.md)|FRA]] and the [Eurodollar futures](../../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%206%20Options%20on%20Non-Price%20Variables/Convexity-Adjusted%20Models%20for%20LIBOR%20Forwards%20Qu.md). The [convexity](../../../Fixed%20Income%20Asset%20Pricing/Problem%20Sets/PSET%20II%20Fixed%20Income%20Asset%20Pricing%201.md) bias is an important factor to consider when [hedging](../../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%205/Key%20Rates%20O1s%20Durations%20and%20Hedging.md) with [Eurodollar futures](../../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%206%20Options%20on%20Non-Price%20Variables/Convexity-Adjusted%20Models%20for%20LIBOR%20Forwards%20Qu.md) due to the future's payoff structure, which can affect the [hedging](../../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%205/Key%20Rates%20O1s%20Durations%20and%20Hedging.md) outcome.

### CONVEXITY BIAS AND TAILORING

+ When we hedge using [Eurodollar futures](../../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%206%20Options%20on%20Non-Price%20Variables/Convexity-Adjusted%20Models%20for%20LIBOR%20Forwards%20Qu.md), the [convexity](../../../Fixed%20Income%20Asset%20Pricing/Problem%20Sets/PSET%20II%20Fixed%20Income%20Asset%20Pricing%201.md) bias arises due to the difference between the payoff of an [Basis Swap](A%20Guide%20to%20the%20Front%20End%20and%20[[Basis%20Swaps) Markets#[Forward Rate Agreements](../../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%2012/EURIBOR%20Forward%20Rate%20Agreements%20and%20Futures.md) (FRAs) [Overview](../../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%201%20-%20Purpose%20and%20Structure%20of%20Financial%20Markets/Overview%20of%20Financial%20Markets.md)|FRA]] and that of a Eurodollar future. This bias, known as *[convexity](../../../Fixed%20Income%20Asset%20Pricing/Problem%20Sets/PSET%20II%20Fixed%20Income%20Asset%20Pricing%201.md) bias*, must be accounted for to ensure an accurate [hedging strategy](.md).

#### TAILORING THE HEDGE

+ To tailor a hedge accurately, we must account for the number of [futures contracts](../../../Financial%20Engineering/Mathematics%20of%20the%20Financial%20Markets.md) to use. For example, if the notional amount is$100m and we're [hedging](../../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%205/Key%20Rates%20O1s%20Durations%20and%20Hedging.md) with [Eurodollar futures](../../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%206%20Options%20on%20Non-Price%20Variables/Convexity-Adjusted%20Models%20for%20LIBOR%20Forwards%20Qu.md), we need to adjust for the size of each contract and the [duration](../../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%205/Key%20Rates%20O1s%20Durations%20and%20Hedging.md) of the hedge.

#### EXAMPLE CALCULATION

Suppose we are [hedging](../../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%205/Key%20Rates%20O1s%20Durations%20and%20Hedging.md) a borrowing cost using [Eurodollar futures](../../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%206%20Options%20on%20Non-Price%20Variables/Convexity-Adjusted%20Models%20for%20LIBOR%20Forwards%20Qu.md) with the following details:

+ **Borrowing Rate:** 1.5% in June, 2% in September
+ **Gain on 98.23 short Eurodollar contracts**

Using the given information, we can calculate the net result of our [hedging strategy](.md) as follows:
$$

\text{Net} = \text{Borrowing} - \text{Gain on contracts} + \text{Interest paid}

$$

+ Given the borrowing rates and the outcome of the [Eurodollar futures](../../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%206%20Options%20on%20Non-Price%20Variables/Convexity-Adjusted%20Models%20for%20LIBOR%20Forwards%20Qu.md) position, we can calculate the overall cost or gain from the hedge.

### TABLE 4: DETAILED CALCULATIONS

(Here, include a detailed breakdown of the cash flows from June to September for the [hedging strategy](.md).)

### CONCLUSION

+ By understanding the concepts of [implied forward rates](../Teaching%20Note%201-%20Forward%20Rates%20Agreement/Forwards%20and%20Futures%20Notes.md), zero-coupon and coupon bonds, and the nuances of [hedging](../../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%205/Key%20Rates%20O1s%20Durations%20and%20Hedging.md) with [Eurodollar futures](../../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%206%20Options%20on%20Non-Price%20Variables/Convexity-Adjusted%20Models%20for%20LIBOR%20Forwards%20Qu.md), we can effectively manage [interest rate risk](../../../Fixed%20Income%20Asset%20Pricing/Analysis%20of%20Fixed%20Income%20Securities.md).
+ It's crucial to consider the [convexity](../../../Fixed%20Income%20Asset%20Pricing/Problem%20Sets/PSET%20II%20Fixed%20Income%20Asset%20Pricing%201.md) bias and to tailor the hedge precisely to the amount and timing of the exposure to ensure that the hedge is effective.

=-----
```markdown

# Lecture Notes: Interest Rate Forwards and Futures
## [](../../../Fixed%20Income%20Asset%20Pricing/Fixed%20Income%20Lecture%20Notes/A%20Guide%20to%20the%20Front%20End%20and%20Basis%20Swap%20Markets.md#Forward%20Rate%20Agreements%20(FRAs)%20Overview|Forward%20Rate%20Agreements) (FRAs)
To summarize, an [Basis Swap](A%20Guide%20to%20the%20Front%20End%20and%20[[Basis%20Swaps) Markets#[Forward Rate Agreements](../../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%2012/EURIBOR%20Forward%20Rate%20Agreements%20and%20Futures.md) (FRAs) [Overview](../../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%201%20-%20Purpose%20and%20Structure%20of%20Financial%20Markets/Overview%20of%20Financial%20Markets.md)|FRA]] is just like the stock and [currency forwards](../Teaching%20Note%201-%20Forward%20Rates%20Agreement/Forward%20Contracts%20on%20Exchange%20Rates.md) we have considered, both with respect to [pricing](../../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%207/Arbitrage%20Pricing%20of%20Derivatives.md) and synthesizing. If at time 0 we want to lock in a lending rate from time $t$ to time $t + s$, we can create a rate forward synthetically by buying the [underlying asset](../../Financial%20Derivatives%20and%20Quantitative%20Methods/Risk%20Neutral%20Pricing%20of%20Options.md) (the bond maturing at $t + s$) and borrowing ([shorting](../../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%202%20-%20Spot%20Markets/Short%20Selling.md)) the bond maturing at $t$.
In general, we have the following conclusions concerning a rate forward covering the period $t$ to $t + s$:
- The [forward rate](../../../Clippings/Forward%20Points%20in%20Currency.md) we can obtain is the implied [forward rate](../../../Clippings/Forward%20Points%20in%20Currency.md)—i.e., $f(t, t+s) = \frac{(1+r(0, t+s))^{t+s}}{(1+r(0, t))^t} - 1$.

- We can synthetically create the payoff to an FRA, $\frac{(1+r(t, t+s))^{s}}{(1+r(0, t))^t}$, by borrowing to buy a bond maturing at $t + s$, i.e., by:

  1. Buying $1 + r(t, t+s)$ of the zero-coupon bond maturing on day $t+s$,

  2. [Shorting](../../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%202%20-%20Spot%20Markets/Short%20Selling.md) $1$ zero-coupon bond maturing on day $t$.
## Eurodollar Futures
[Eurodollar futures](../../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%206%20Options%20on%20Non-Price%20Variables/Convexity-Adjusted%20Models%20for%20LIBOR%20Forwards%20Qu.md) contracts are similar to FRAs in that they can be used to guarantee a borrowing rate. There are subtle differences between FRAs and Eurodollar contracts, however; that are important to understand.
### Example Problem
Assume the June [Eurodollar futures](../../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%206%20Options%20on%20Non-Price%20Variables/Convexity-Adjusted%20Models%20for%20LIBOR%20Forwards%20Qu.md) price is 92.8. This translates into the implied interest rate, which is calculated as $100 - 92.8 = 7.2\%$ on an annual basis for a \$1M loan from June to September. Suppose the June Eurodollar futures price is 92.8, which implies a 3-month [](../../../Fixed%20Income%20Asset%20Pricing/Fixed%20Income%20Lecture%20Notes/A%20Guide%20to%20the%20Front%20End%20and%20Basis%20Swap%20Markets.md#London%20Interbank%20Offered%20Rate%20(LIBOR)|LIBOR) is $100 - 92.8 = 7.2\%$. If we enter into a single short Eurodollar contract at expiration it will be:
$

(\text{[Futures Price](../../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%2011/Futures%20Price%20and%20the%20Quality%20Option%20Before%20E.md)}) - (\text{Spot Price}) \times (\text{Contract Size}) = (92.8 - 94) \times 100 \times \$25 = -\$30,000

$
If [Basis Swap](A%20Guide%20to%20the%20Front%20End%20and%20[[Basis%20Swaps) Markets#[London Interbank Offered Rate](../../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%2012/Short-Term%20Rates%20and%20the%20Transition%20from%20LIBOR.md) (LIBOR)|LIBOR]] = 8% (quarterly = 2.0%), we earn an extra $20,000 in interest and the invested proceeds from the Eurodollar contract are:
$

((100 - 8) \times 100 \times \$25) = \$230,000

$
We multiply by 100 twice: once to account for 100 contracts, and the second
time to convert the change in the [futures price](../../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%2011/Futures%20Price%20and%20the%20Quality%20Option%20Before%20E.md) to basis points. Similarly, if the borrowing rate is 2%, we have:
$

((92.8 - 92) \times 100 \times \$25) \times 100 = \$200,000

$
This is like the payment on an [Basis Swap](A%20Guide%20to%20the%20Front%20End%20and%20[[Basis%20Swaps) Markets#[Forward Rate Agreements](../../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%2012/EURIBOR%20Forward%20Rate%20Agreements%20and%20Futures.md) (FRAs) [Overview](../../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%201%20-%20Purpose%20and%20Structure%20of%20Financial%20Markets/Overview%20of%20Financial%20Markets.md)|FRA]] paid in arrears, except that the [futures](../../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%203%20-%20Futures%20Markets/Futures%20Not%20Subject%20to%20Cash-And-Carry.md) contract settles in June, but our interest expense is not paid until September. Thus we have 3 months to earn or pay interest on our Eurodollar gain or loss before we actually have to make the interest payment.
### Hedging with Eurodollar Futures
Recall that when the [Basis Swap](A%20Guide%20to%20the%20Front%20End%20and%20[[Basis%20Swaps) Markets#[Forward Rate Agreements](../../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%2012/EURIBOR%20Forward%20Rate%20Agreements%20and%20Futures.md) (FRAs) [Overview](../../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%201%20-%20Purpose%20and%20Structure%20of%20Financial%20Markets/Overview%20of%20Financial%20Markets.md)|FRA]] settles on the borrowing date, the payment is the _present value_ of the change in borrowing cost. The [Basis Swap](A%20Guide%20to%20the%20Front%20End%20and%20[[Basis%20Swaps) Markets#[Forward Rate Agreements](../../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%2012/EURIBOR%20Forward%20Rate%20Agreements%20and%20Futures.md) (FRAs) [Overview](../../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%201%20-%20Purpose%20and%20Structure%20of%20Financial%20Markets/Overview%20of%20Financial%20Markets.md)|FRA]] is thus tailed automatically as part of the agreement. With the Eurodollar contract, by contrast, we need to tail the position explicitly. We do this by [shorting](../../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%202%20-%20Spot%20Markets/Short%20Selling.md) fewer than 100 contracts, using the implied 3-month Eurodollar rate of 1.8% as our [discount factor](../../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%201/Discount%20Factors.md). Thus, we enter into:
$

\text{Number of Eurodollar contracts} = \frac{100}{1 + 0.018} \approx -98.2318

$
Now consider the gain on the [Eurodollar futures](../../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%206%20Options%20on%20Non-Price%20Variables/Convexity-Adjusted%20Models%20for%20LIBOR%20Forwards%20Qu.md) position. If [Basis Swap](A%20Guide%20to%20the%20Front%20End%20and%20[[Basis%20Swaps) Markets#[London Interbank Offered Rate](../../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%2012/Short-Term%20Rates%20and%20the%20Transition%20from%20LIBOR.md) (LIBOR)|LIBOR]] = 6% (quarterly = 1.5%), our total gain on the short contracts when we initiate borrowing on day 120 will be:
$

98.2318 \times (92.8 - 94) \times \$2500 = -\$294,695

$
But if [Basis Swap](A%20Guide%20to%20the%20Front%20End%20and%20[[Basis%20Swaps) Markets#[London Interbank Offered Rate](../../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%2012/Short-Term%20Rates%20and%20the%20Transition%20from%20LIBOR.md) (LIBOR)|LIBOR]] = 8% (quarterly = 2.0%), our total gain on the contracts will be:
$

98.2318 \times (92.8 - 92) \times \$2500 = \$196,464

$
Table 4 summarizes the result from this [hedging](../../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%205/Key%20Rates%20O1s%20Durations%20and%20Hedging.md) position. The borrowing cost is close to 1.8%.
### Table 4: Results from hedging $100m in borrowing with 98.23 short Eurodollar futures.
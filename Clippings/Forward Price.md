\begin{aligned} &F_0 = S_0 \times e^{rT} \\ \end{aligned}
\begin{aligned} &F = S \times e ^ { (r \times t) } \\ &\textbf{where:} \\ &F = \text{the contract's [forward price](../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%2011/Forward%20Contracts%20and%20Forward%20Prices.md)} \\ &S = \text{the [underlying asset](../Financial%20Instruments/Financial%20Derivatives%20and%20Quantitative%20Methods/Risk%20Neutral%20Pricing%20of%20Options.md)'s current spot price} \\ &e = \text{the mathematical irrational constant approximated} \\ &\text{by 2.7183} \\ &r = \text{the [risk-free rate](../Financial%20Instruments/Black%20Scholes%20Derivation.md) that applies to the life of the} \\ &\text{[forward contract](Forward%20Points%20in%20Currency.md)} \\ &t = \text{the delivery date in years} \\ \end{aligned}
\begin{aligned} &F = \$100 \times e ^ { (0.06 \times 1) } = \$106.18 \\ \end{aligned}
\begin{aligned} &F = S \times e ^ { (r + q) \times t } \\ \end{aligned}
\begin{aligned} &F = ( S - D ) \times e ^ { ( r \times t ) } \\ \end{aligned}
\begin{aligned} D =& \ \text{PV}(d(1)) + \text{PV}(d(2)) + \cdots + \text{PV}(d(x)) \\ =& \ d(1) \times e ^ {- ( r \times t(1) ) } + d(2) \times e ^ { - ( r \times t(2) ) } + \cdots + \\ \phantom{=}& \ d(x) \times e ^ { - ( r \times t(x) ) } \\ \end{aligned}
\begin{aligned} &\text{PV}(d(1)) = \$0.5 \times e ^ { - ( 0.06 \times \frac { 3 }{ 12 } ) } = \$0.493 \\ \end{aligned}
\begin{aligned} &\text{PV}(d(2)) = \$0.5 \times e ^ { - ( 0.06 \times \frac { 6 }{ 12 } ) } = \$0.485 \\ \end{aligned}
\begin{aligned} &\text{PV}(d(3)) = \$0.5 \times e ^ { - ( 0.06 \times \frac { 9 }{ 12 } ) } = \$0.478 \\ \end{aligned}
\begin{aligned} &\text{PV}(d(4)) = \$0.5 \times e ^ { - ( 0.06 \times \frac { 12 }{ 12 } ) } = \$0.471 \\ \end{aligned}
\begin{aligned} &F = ( \$100 - \$1.927 ) \times e ^ { ( 0.06 \times 1 ) } = \$104.14 \\ \end{aligned}
aliases:
  - Delivery Price
  - [Forward Contract Price](../Financial%20Engineering/Determining%20the%20Stochastic%20Process%20for%20a%20Forward%20Contract%20from%20Ito’s%20Lemma.md)
  - Future Price
key_concepts:
  - [Hedging](../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%205/Key%20Rates%20O1s%20Durations%20and%20Hedging.md) against fluctuations
  - Lock in future price
  - Predetermined future delivery price
  - Spot price vs [forward price](../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%2011/Forward%20Contracts%20and%20Forward%20Prices.md)
  - [Underlying asset price](../Financial%20Instruments/Black%20Scholes%20Derivation.md)
---


## What is a Forward Price

[Forward price](../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%2011/Forward%20Contracts%20and%20Forward%20Prices.md) is the predetermined [delivery price](https://www.investopedia.com/terms/d/deliveryprice.asp) for an underlying commodity, [currency](../Financial%20Instruments/Lecture%20Notes-%20Financial%20Instruments/Teaching%20Note%201-%20Forward%20Rates%20Agreement/Forwards%20and%20Futures%20Notes.md), or financial asset as decided by the buyer and the seller of the [forward contract]([Forward%20Points%20in%20Currency)](https://www.investopedia.com/terms/f/forwardcontract.asp), to be paid at a predetermined date in the future. At the inception of a [forward contract](Forward%20Points%20in%20Currency.md), the [forward price](../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%2011/Forward%20Contracts%20and%20Forward%20Prices.md) makes the value of the contract zero, but changes in the price of the underlying will cause the [forward price](../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%2011/Forward%20Contracts%20and%20Forward%20Prices.md) to take on a positive or negative value.

The [forward price](../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%2011/Forward%20Contracts%20and%20Forward%20Prices.md) is determined by the following formula:
$\begin{aligned} &F_0 = S_0 \times e^{rT} \\ \end{aligned}$

### Key Takeaways

- [Forward price](../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%2011/Forward%20Contracts%20and%20Forward%20Prices.md) is the price at which a seller delivers an [underlying asset](../Financial%20Instruments/Financial%20Derivatives%20and%20Quantitative%20Methods/Risk%20Neutral%20Pricing%20of%20Options.md), financial derivative, or [currency](../Financial%20Instruments/Lecture%20Notes-%20Financial%20Instruments/Teaching%20Note%201-%20Forward%20Rates%20Agreement/Forwards%20and%20Futures%20Notes.md) to the buyer of a [forward contract](Forward%20Points%20in%20Currency.md) at a predetermined date.
- It is roughly equal to the spot price plus associated carrying costs such as [storage costs](../Financial%20Instruments/Lecture%20Notes-%20Financial%20Instruments/Teaching%20Note%201-%20Forward%20Rates%20Agreement/Primary%20vs.%20Secondary%20Commodities.md), [interest rates](../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%202/Interest%20Rate%20Quotations.md), etc.
- Investors may want to lock in a [forward price](../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%2011/Forward%20Contracts%20and%20Forward%20Prices.md) to hedge against future market fluctuations.
- The downside of locking in a [forward price](../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%2011/Forward%20Contracts%20and%20Forward%20Prices.md) is that the asset’s value could move unfavorably against the investor.

Investopedia / Michela Buttignol

## Basics of Forward Price

[Forward price](../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%2011/Forward%20Contracts%20and%20Forward%20Prices.md) is based on the current [spot price](https://www.investopedia.com/terms/s/spotprice.asp) of the [underlying asset](../Financial%20Instruments/Financial%20Derivatives%20and%20Quantitative%20Methods/Risk%20Neutral%20Pricing%20of%20Options.md), plus any carrying costs such as interest, [storage costs](../Financial%20Instruments/Lecture%20Notes-%20Financial%20Instruments/Teaching%20Note%201-%20Forward%20Rates%20Agreement/Primary%20vs.%20Secondary%20Commodities.md), foregone interest or other costs including [opportunity costs](https://www.investopedia.com/terms/o/opportunitycost.asp).

Although the contract has no [intrinsic value](https://www.investopedia.com/terms/i/intrinsicvalue.asp) at the inception, over time, a contract may gain or lose value. Offsetting positions in a [forward contract](Forward%20Points%20in%20Currency.md) are equivalent to a [zero-sum game](https://www.investopedia.com/terms/z/zero-sumgame.asp). For example, if one investor takes a [long position](../Financial%20Engineering/Derivatives/Part%20I%20-%20Forwards%20and%20Futures/Chapter%204%20-%20Futures:%20Hedging%20and%20Speculation.md) in a pork belly [forward agreement](../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%2011/Forward%20Contracts%20and%20Forward%20Prices.md) and another investor takes the [short position](https://www.investopedia.com/terms/s/short.asp), any gains in the [long position](../Financial%20Engineering/Derivatives/Part%20I%20-%20Forwards%20and%20Futures/Chapter%204%20-%20Futures:%20Hedging%20and%20Speculation.md) equals the losses that the second investor incurs from the short position. By initially setting the value of the contract to zero, both parties are on equal ground at the inception of the contract.

## Forward Price Calculation Example

When the [underlying asset](../Financial%20Instruments/Financial%20Derivatives%20and%20Quantitative%20Methods/Risk%20Neutral%20Pricing%20of%20Options.md) in the [forward contract](Forward%20Points%20in%20Currency.md) does not pay any [dividends](https://www.investopedia.com/terms/d/dividend.asp), the [forward price](../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%2011/Forward%20Contracts%20and%20Forward%20Prices.md) can be calculated using the following formula:
$\begin{aligned} &F = S \times e ^ { (r \times t) } \\ &\textbf{where:} \\ &F = \text{the contract's forward price} \\ &S = \text{the underlying asset's current spot price} \\ &e = \text{the mathematical irrational constant approximated} \\ &\text{by 2.7183} \\ &r = \text{the risk-free rate that applies to the life of the} \\ &\text{forward contract} \\ &t = \text{the delivery date in years} \\ \end{aligned}$

For example, assume a security is currently trading at $100 per unit. An investor wants to enter into a [forward contract](Forward%20Points%20in%20Currency.md) that expires in one year. The current annual [risk-free interest rate](../Financial%20Markets/Financial%20Asset%20Pricing%20Theory%20Overview/Chapter%2012%20-%20Derivatives/Exercises.md) is 6%. Using the above formula, the [forward price](../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%2011/Forward%20Contracts%20and%20Forward%20Prices.md) is calculated as:
$\begin{aligned} &F = \$100 \times e ^ { (0.06 \times 1) } = \$106.18 \\ \end{aligned}$

If the there are carrying costs, that is added into the formula:
$\begin{aligned} &F = S \times e ^ { (r + q) \times t } \\ \end{aligned}$

Here, q is the carrying costs.

If the [underlying asset](../Financial%20Instruments/Financial%20Derivatives%20and%20Quantitative%20Methods/Risk%20Neutral%20Pricing%20of%20Options.md) pays dividends over the life of the contract, the formula for the [forward price](../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%2011/Forward%20Contracts%20and%20Forward%20Prices.md) is:
$\begin{aligned} &F = ( S - D ) \times e ^ { ( r \times t ) } \\ \end{aligned}$

Here, D equals the sum of each dividend's present value, given as:
$\begin{aligned} D =& \ \text{PV}(d(1)) + \text{PV}(d(2)) + \cdots + \text{PV}(d(x)) \\ =& \ d(1) \times e ^ {- ( r \times t(1) ) } + d(2) \times e ^ { - ( r \times t(2) ) } + \cdots + \\ \phantom{=}& \ d(x) \times e ^ { - ( r \times t(x) ) } \\ \end{aligned}$

Using the example above, assume that the security pays a 50-cent dividend every three months. First, the present value of each dividend is calculated as:
$\begin{aligned} &\text{PV}(d(1)) = \$0.5 \times e ^ { - ( 0.06 \times \frac { 3 }{ 12 } ) } = \$0.493 \\ \end{aligned}$
$\begin{aligned} &\text{PV}(d(2)) = \$0.5 \times e ^ { - ( 0.06 \times \frac { 6 }{ 12 } ) } = \$0.485 \\ \end{aligned}$
$\begin{aligned} &\text{PV}(d(3)) = \$0.5 \times e ^ { - ( 0.06 \times \frac { 9 }{ 12 } ) } = \$0.478 \\ \end{aligned}$
$\begin{aligned} &\text{PV}(d(4)) = \$0.5 \times e ^ { - ( 0.06 \times \frac { 12 }{ 12 } ) } = \$0.471 \\ \end{aligned}$

The sum of these is $1.927. This amount is then plugged into the dividend-adjusted [forward price formula](../Financial%20Engineering/Appendices/Appendix%205.C%20Forward%20And%20Futures%20Prices%20When%20Interest%20Rates%20Are%20Random.md):
$\begin{aligned} &F = ( \$100 - \$1.927 ) \times e ^ { ( 0.06 \times 1 ) } = \$104.14 \\ \end{aligned}$

## What is the Difference Between Forward Price and Spot Price?

[Forward price](../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%2011/Forward%20Contracts%20and%20Forward%20Prices.md) refers to a predetermined future delivery price for an underlying commodity, [currency](../Financial%20Instruments/Lecture%20Notes-%20Financial%20Instruments/Teaching%20Note%201-%20Forward%20Rates%20Agreement/Forwards%20and%20Futures%20Notes.md), or financial asset agreed upon by the buyer and seller of a forward [futures](../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%203%20-%20Futures%20Markets/Futures%20Not%20Subject%20to%20Cash-And-Carry.md) contract. In contrast, a spot price refers to the asset’s current market price.

## Why Do Some Investors Want to Lock in a Forward Price?

Investors may want to lock in a [forward price](../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%2011/Forward%20Contracts%20and%20Forward%20Prices.md) to [hedge](https://www.investopedia.com/terms/h/hedge.asp) against future market fluctuations. For example, a farmer may want to use a forward wheat contract ahead of harvest to protect against a decline in grain prices caused by potential drought or flood.

## What are the Drawbacks of Locking in a Forward Price?

The main downside of locking in a [forward price](../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%2011/Forward%20Contracts%20and%20Forward%20Prices.md) is that the asset’s value could move unfavorably against the investor, resulting in a loss compared to selling at the spot price on the asset's delivery. Furthermore, a [longer-dated](https://www.investopedia.com/terms/l/long-date-forward.asp#:~:text=A%20long%2Ddated%20forward%20is%20an%20OTC%20derivatives%20contract%20that,a%20few%20years%20from%20now.) [forward price](../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%2011/Forward%20Contracts%20and%20Forward%20Prices.md) contact increases the risk of non-payment or default.

## What are the Main factors That Determine an Asset’s Forward Price?

Investors determine an asset's [forward price](../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%2011/Forward%20Contracts%20and%20Forward%20Prices.md) based on its current spot price plus carrying costs such as storage, transportation, opportunity costs, and foregone interest. Typically, these costs will be higher for forward contracts that have longer expiry dates.

## The Bottom Line

[Forward price](../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%2011/Forward%20Contracts%20and%20Forward%20Prices.md) refers to an asset’s future delivery price agreed upon by the buyer and seller of a forward [futures](../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%203%20-%20Futures%20Markets/Futures%20Not%20Subject%20to%20Cash-And-Carry.md) contract. This type of contract has zero value at inception as market conditions have yet to change. Investors determine a [forward price](../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%2011/Forward%20Contracts%20and%20Forward%20Prices.md) by adding carrying costs to the [underlying asset](../Financial%20Instruments/Financial%20Derivatives%20and%20Quantitative%20Methods/Risk%20Neutral%20Pricing%20of%20Options.md)'s spot price. Using a [forward price](../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%2011/Forward%20Contracts%20and%20Forward%20Prices.md) in [futures contracts](../Financial%20Engineering/Mathematics%20of%20the%20Financial%20Markets.md) provides a hedge against market fluctuations; however, this can work as a double-edged sword if an asset's value moves unfavorably against the investor.  

Partner Links
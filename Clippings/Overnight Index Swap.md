 
source: https://www.investopedia.com/terms/o/overnightindexswap.asp
description: An overnight index swap is a [hedging strategy](../Financial%20Instruments/Lecture%20Notes-%20Financial%20Instruments/Teaching%20Note%203%20Swaps-%20Financial%20Instruments/The%20Value%20of%20the%20Swap%20Contract%20after%20Initiation.md) in which a [cash flow](../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%201%20-%20Purpose%20and%20Structure%20of%20Financial%20Markets/Preview%20of%20the%20Book.md) based
  on an overnight lending rate is exchanged for another predetermined [cash flow](../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%201%20-%20Purpose%20and%20Structure%20of%20Financial%20Markets/Preview%20of%20the%20Book.md).
tags:
  - federal_funds_rate
  - financial_markets
  - [hedging](../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%205/Key%20Rates%20O1s%20Durations%20and%20Hedging.md)
  - interest_rate_swap
  - overnight_index_swap
aliases:
  - OIS
  - index swap
key_concepts:
  - Compounded interest payments
  - [Fixed vs. floating](../Course%20Notes/Python/QuantLib-Python/Modeling%20Vanilla%20Interest%20Rate%20Swaps%20Using%20QuantLib%20Python.md) rate
  - Interbank [credit markets](../Credit%20Markets/Credit%20Markets%20Session%201.md)
  - Overnight rate exchange
  - Short-term [interest rates](../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%202/Interest%20Rate%20Quotations.md)
---


Investopedia / Jake Shi

## What Is an Overnight Index Swap (OIS)?

An index swap is a [hedging](../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%205/Key%20Rates%20O1s%20Durations%20and%20Hedging.md) contract in which one party exchanges a predetermined [cash flow](../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%201%20-%20Purpose%20and%20Structure%20of%20Financial%20Markets/Preview%20of%20the%20Book.md) with a counterparty on a specified date. A debt, equity, or other price index is used as the agreed exchange for one side of this swap.

An overnight index swap applies an overnight rate index such as the [federal funds rate](../International%20Finance/Economic%20Stabilization%20Notes/Topics%20in%20Fiscal%20and%20Monetary%20Policies%20and%20Stabilization-%20Empirical%20Issues.md). Index swaps are specialized groups of conventional fixed-rate swaps, with terms that can be set from three months to more than a year.

### Key Takeaways

- The interest on the overnight rate portion of the swap is compounded and paid at reset dates, with the [fixed leg](../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%202/Pricing%20Interest%20Rate%20Swaps.md) being accounted for in the swap's value to each party.
- The [floating leg](../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%202/Pricing%20Interest%20Rate%20Swaps.md)'s present value (PV) is determined by either compounding of the overnight rate or by taking the geometric average of the rate over a given period.
- Like other interest rate swaps, an interest rate curve must be produced to determine the present value of cash flows.

## How Does an Overnight Index Swap (OIS) Work?

In an overnight index swap, the overnight rate is exchanged for a [fixed interest rate]([Chapter%2036%20-%20Currency%20Swaps)](https://www.investopedia.com/terms/f/fixedinterestrate.asp). An overnight index swap uses an overnight rate index such as the [federal funds rate](../International%20Finance/Economic%20Stabilization%20Notes/Topics%20in%20Fiscal%20and%20Monetary%20Policies%20and%20Stabilization-%20Empirical%20Issues.md) as the underlying rate for the [floating leg](../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%202/Pricing%20Interest%20Rate%20Swaps.md), while the [fixed leg](../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%202/Pricing%20Interest%20Rate%20Swaps.md) would be set at a rate agreed upon by both parties.

The interest of the overnight rate portion of the swap is compounded and paid at reset dates, with the [fixed leg](../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%202/Pricing%20Interest%20Rate%20Swaps.md) being accounted for in the swap's value to each party.

The [floating leg](../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%202/Pricing%20Interest%20Rate%20Swaps.md)'s present value (PV) is determined by either compounding the overnight rate or by taking the geometric average of the rate over a given period.

Overnight index swaps are popular among [financial institutions](../Financial%20Markets%20and%20Institutions/Financial%20Markets%20and%20Institutions%20Lecture%20Notes.md) because the overnight index is considered to be a good indicator of the interbank [credit markets](../Credit%20Markets/Credit%20Markets%20Session%201.md) and less risky than traditional interest rate spreads.

## How to Calculate an Overnight Index Swap

Eight steps are applied in calculating a bank's dollar benefit from using an overnight index swap.

- The first step multiplies the overnight rate for the period in which the swap applies. If the swap begins on a Friday, the swap's period is three days because transactions don't settle on weekends. If the swap begins on another business day, the swap's period is one day. For example, if the overnight rate is 0.005% and the swap is entered on a Friday, the effective rate would be 0.015% (0.005% x 3 days). Otherwise, it's 0.005%.
- Step two of the calculation divides the effective overnight rate by 360. Industry practice dictates that overnight swap calculations use 360 days for a year instead of 365. Using the above rate, the calculation in step two is as follows: 0.005% / 360 = 1.3889 x 10^ <sup>-5</sup>.
- For step three, simply add one to this result: 1.3889 x 10 <sup>-5</sup> + 1 = 1.000013889.
- In step four, multiply the new rate by the total principal of the loan. For example, if the overnight loan has a [principal](https://www.investopedia.com/terms/p/principal.asp) of $1 million, the resulting calculation is: 1.000013889x $1,000,000 = $1,000,013.89.
- Step five applies the above calculations to each day of the loan, with the principal updated continuously. This is done for multi-day loans in case the rate varies.
- Steps six and seven are similar to two and three. The rate that overnight index swaps use must be divided by 360 and added to 1. For example, if this rate is 0.0053% the result is: 0.0053% / 360 + 1 = 1.00001472.
- In step 8, raise this rate by the power of the number of days in the loan and multiply by the principal: 1.00001472^1 x $1,000,000 = $1,000,014.72.
- Lastly, subtract the two sums to identify the profit gained by the bank from using the swap: $1,000,014.72 - $1,000,013.89 = $0.83.

## What Is an Overnight Index Swap?

An overnight index swap is a bet on the direction of short-term [interest rates](../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%202/Interest%20Rate%20Quotations.md). One party agrees to pay a [fixed interest rate](../Financial%20Engineering/Derivatives/Part%20VIII%20-%20Swaps/Chapter%2036%20-%20Currency%20Swaps.md), while the other party agrees to pay a floating rate based on the overnight index. When the overnight index rate is calculated for the relevant time period, one party pays the other party the difference between the fixed and floating rates for that period.

## Why Does Anyone Undertake an Overnight Index Swap?

[Financial institutions](../Financial%20Markets%20and%20Institutions/Financial%20Markets%20and%20Institutions%20Lecture%20Notes.md) and other large enterprises use the overnight index swap as a hedge against sudden adverse swings in short-term [interest rates](../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%202/Interest%20Rate%20Quotations.md). They are effectively protecting their interest rate costs by locking in the short-term rate they will pay. Traders and speculators also use this strategy when they expect a swing in short-term [interest rates](../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%202/Interest%20Rate%20Quotations.md).

## Is an Overnight Index Swap a Derivative?

Yes. The overnight index swap is a type of derivative contract. That is, it is based on short-term [interest rates](../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%202/Interest%20Rate%20Quotations.md) but does not represent an actual [investment](../Advanced%20Investments/An%20Asset%20Allocation%20Primer.md) in any asset.

## The Bottom Line

The overnight index swap is primarily an interbank process, used by [financial institutions](../Financial%20Markets%20and%20Institutions/Financial%20Markets%20and%20Institutions%20Lecture%20Notes.md) to hedge against costly changes in the direction of [interest rates](../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%202/Interest%20Rate%20Quotations.md). It is a tool that is also used by hedge fund managers and market speculators to place a bet on [short-term interest rate](../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%209/The%20Gauss%20Model.md) movements.

Article Sources

1. Cbonds. "[Overnight Index Swap](https://cbonds.com/glossary/overnight-index-swap-ois/)."
2. Cbonds. "[Overnight Index Swap](https://cbonds.com/glossary/overnight-index-swap-ois/#:~:text=Unlike%20other%20yield%20curves%20that,for%20risk%2Dfree%20interest%20rates.)."

Partner Links
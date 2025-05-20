---
title: Foreign Exchange Quoting Conventions
tags:
  - currency_pair
  - foreign_exchange
  - fx_forward_rate
  - fx_spot_rate
  - interest_rate_parity
  - outright_forward
aliases:
  - FX
  - FX Quoting
  - Forex
key_concepts:
  - Base and quote currency
  - Exchange rate definition
  - FX forward rate
  - FX spot rate
  - Forward contract value
  - Interest rate parity
---

- [Introduction](Ch1%20[[Squam%20Lake%20Group%20Introduction) to Derivative Markets]]
- [Hedging](Chapter%206%20(Hull)%20[[Key%20Rates%20O1s%20Durations%20and%20Hedging) Strategies with [Forwards](../../../Financial%20Markets/Financial%20Asset%20Pricing%20Theory%20Overview/Chapter%2012%20-%20Derivatives/Forwards%20and%20Futures.md)]]
- [Forward Exchange Rate](Deriving%20[[A%20Primer%20on%20Currency%20Derivatives) Numerical Example]]
- [Secondary Commodities](Primary%20vs.%20[[Primary%20vs.%20Secondary%20Commodities)]]
- [Foreign Exchange Quoting Conventions](.md)
- [Forward Contracts on Exchange Rates](Forward%20Contracts%20on%20Exchange%20Rates.md)
- [Forwards and Futures]([[Forward%20and%20Futures%20Contracts) Notes]]
- [Hedging]([[Key%20Rates%20O1s%20Durations%20and%20Hedging) Strategies with [Forwards](../../../Financial%20Markets/Financial%20Asset%20Pricing%20Theory%20Overview/Chapter%2012%20-%20Derivatives/Forwards%20and%20Futures.md)]]
- [Financial Instruments]([[A%20Practical%20Guide%20for%20Actuaries%20and%20other%20Business%20Professionals.)/Lecture Notes/Teaching Note 1- Forward Rates Agreement/[Interest Rates](../../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%202/Interest%20Rate%20Quotations.md),  Carry Trades,  and Exchange Rate Movements]]
- [Teaching Note 1Forward Rates Agreement](Teaching%20Note%201Forward%20Rates%20Agreement)
# Foreign Exchange Quoting Conventions
- The base [currency](Forwards%20and%20Futures%20Notes.md) is the first [currency](Forwards%20and%20Futures%20Notes.md) shown in a foreign exchange quotation. The second [currency](Forwards%20and%20Futures%20Notes.md) in the quotation is called the quote [currency](Forwards%20and%20Futures%20Notes.md),  or counter [currency](Forwards%20and%20Futures%20Notes.md).
- Foreign exchange quotations are always presented as a [currency](Forwards%20and%20Futures%20Notes.md) pair in the following format: XXX/YYY e.g. EUR/USD. This is because,  when you exchange [currency](Forwards%20and%20Futures%20Notes.md),  you’re selling one [currency](Forwards%20and%20Futures%20Notes.md) and buying another.
- The exchange rate represents how much quote [currency](Forwards%20and%20Futures%20Notes.md) you need to sell in order to buy one unit of the base [currency](Forwards%20and%20Futures%20Notes.md).
[Currency]([Forwards%20and%20Futures%20Notes) Forward]([Currency](Forwards%20and%20Futures%20Notes.md)%20Forward.md)
### FX SPOT RATE$S_0$
- The [FX spot rate](.md), $S_0 = FOR-DOM$,  represents the number of units of domestic [currency](Forwards%20and%20Futures%20Notes.md) needed to buy one unit of foreign [currency](Forwards%20and%20Futures%20Notes.md) at time 0.
- A notional of$N$units of foreign [currency](Forwards%20and%20Futures%20Notes.md) is equal to$N*S_t$units of domestic [currency](Forwards%20and%20Futures%20Notes.md)
- The domestic [currency](Forwards%20and%20Futures%20Notes.md) is also referred to as the numeraire [currency](Forwards%20and%20Futures%20Notes.md) and the foreign one as the base [currency](Forwards%20and%20Futures%20Notes.md)
### FX OUTRIGHT FORWARD RATE$F(0, T)$
1. The [forward exchange rate](../../../Financial%20Engineering/A%20Primer%20on%20Currency%20Derivatives.md) contract trades at time$t=0$at zero cost and leads to an exchange of notionals at time$T$at the pre-specified outright [forward rate](../../../Clippings/Forward%20Points%20in%20Currency.md)$F(0, T)$.
1. At time$t$,  the foreign notional amount$N$is exchanged against an amount of$N*F(0, T)$domestic [currency](Forwards%20and%20Futures%20Notes.md) units. 
	1. - For example,  1, 000, 000 EUR may be exchanged against 1, 390, 000 USD assuming an outright [forward rate](../../../Clippings/Forward%20Points%20in%20Currency.md) of 1.3900 EUR-USD. 
1. The outright forward is related to the [FX spot rate](.md) via the spot–[interest rate parity](.md), $$F(0, T) = S \cdot e^{(r_{DOM}-r_{FOR})\tau}$$

where

- $r_{FOR}$is the foreign interest rate (continuously compounded)
- $r_{DOM}$is the domestic interest rate (continuously compounded)
- $\tau$is the [time to maturity](Hedging%20Strategies%20with%20Forwards.md),  equal to$T - t$
## FX FORWARD VALUE

- At inception,  an outright [forward contract](../../../Clippings/Forward%20Points%20in%20Currency.md) has a value of zero. 
- Thereafter,  when foreign exchange rates and/or [interest rates](../../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%202/Interest%20Rate%20Quotations.md) change,  the value of the [forward contract](../../../Clippings/Forward%20Points%20in%20Currency.md) is no longer zero,  but is worth$$v_f(t, T) = e^{-r_{DOM}\tau}(F(t, T) - K) = S_t e^{-r_{FOR}\tau} - Ke^{-r_{DOM}\tau}$$

for a pre-specified exchange rate$K$. 

- This is the [forward contract](../../../Clippings/Forward%20Points%20in%20Currency.md) value in domestic [currency](Forwards%20and%20Futures%20Notes.md) units,  marked to the market at time$t$. 
- As stated previously,  setting$K = F(0,  T)$yields a zero-cost contract.

---

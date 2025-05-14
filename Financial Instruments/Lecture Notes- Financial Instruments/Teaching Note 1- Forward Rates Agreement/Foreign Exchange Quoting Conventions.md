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

- [[Ch1 [[Squam Lake Group Introduction|Introduction]] to Derivative Markets]]
- [[Chapter 6 (Hull) [[Key Rates O1s Durations and Hedging|Hedging]] Strategies with [[Forwards and Futures|Forwards]]]]
- [[Deriving [[A Primer on Currency Derivatives|Forward Exchange Rate]] Numerical Example]]
- [[Primary vs. [[Primary vs. Secondary Commodities|Secondary Commodities]]]]
- [[Foreign Exchange Quoting Conventions]]
- [[Forward Contracts on Exchange Rates]]
- [[[[Forward and Futures Contracts|Forwards and Futures]] Notes]]
- [[[[Key Rates O1s Durations and Hedging|Hedging]] Strategies with [[Forwards and Futures|Forwards]]]]
- [[[[A Practical Guide for Actuaries and other Business Professionals.|Financial Instruments]]/Lecture Notes/Teaching Note 1- Forward Rates Agreement/[[Interest Rate Quotations|Interest Rates]],  Carry Trades,  and Exchange Rate Movements]]
- [[Teaching Note 1Forward Rates Agreement]]
# Foreign Exchange Quoting Conventions
- The base [[Forwards and Futures Notes|currency]] is the first [[Forwards and Futures Notes|currency]] shown in a foreign exchange quotation. The second [[Forwards and Futures Notes|currency]] in the quotation is called the quote [[Forwards and Futures Notes|currency]],  or counter [[Forwards and Futures Notes|currency]].
- Foreign exchange quotations are always presented as a [[Forwards and Futures Notes|currency]] pair in the following format: XXX/YYY e.g. EUR/USD. This is because,  when you exchange [[Forwards and Futures Notes|currency]],  you’re selling one [[Forwards and Futures Notes|currency]] and buying another.
- The exchange rate represents how much quote [[Forwards and Futures Notes|currency]] you need to sell in order to buy one unit of the base [[Forwards and Futures Notes|currency]].
[[[Forwards and Futures Notes|Currency]] Forward]([[Forwards and Futures Notes|Currency]]%20Forward.md)
### FX SPOT RATE$S_0$
- The [[Foreign Exchange Quoting Conventions|FX spot rate]], $S_0 = FOR-DOM$,  represents the number of units of domestic [[Forwards and Futures Notes|currency]] needed to buy one unit of foreign [[Forwards and Futures Notes|currency]] at time 0.
- A notional of$N$units of foreign [[Forwards and Futures Notes|currency]] is equal to$N*S_t$units of domestic [[Forwards and Futures Notes|currency]]
- The domestic [[Forwards and Futures Notes|currency]] is also referred to as the numeraire [[Forwards and Futures Notes|currency]] and the foreign one as the base [[Forwards and Futures Notes|currency]]
### FX OUTRIGHT FORWARD RATE$F(0, T)$
1. The [[A Primer on Currency Derivatives|forward exchange rate]] contract trades at time$t=0$at zero cost and leads to an exchange of notionals at time$T$at the pre-specified outright [[Forward Points in Currency|forward rate]]$F(0, T)$.
1. At time$t$,  the foreign notional amount$N$is exchanged against an amount of$N*F(0, T)$domestic [[Forwards and Futures Notes|currency]] units. 
	1. - For example,  1, 000, 000 EUR may be exchanged against 1, 390, 000 USD assuming an outright [[Forward Points in Currency|forward rate]] of 1.3900 EUR-USD. 
1. The outright forward is related to the [[Foreign Exchange Quoting Conventions|FX spot rate]] via the spot–[[Foreign Exchange Quoting Conventions|interest rate parity]], $$F(0, T) = S \cdot e^{(r_{DOM}-r_{FOR})\tau}$$

where

- $r_{FOR}$is the foreign interest rate (continuously compounded)
- $r_{DOM}$is the domestic interest rate (continuously compounded)
- $\tau$is the [[Hedging Strategies with Forwards|time to maturity]],  equal to$T - t$
## FX FORWARD VALUE

- At inception,  an outright [[Forward Points in Currency|forward contract]] has a value of zero. 
- Thereafter,  when foreign exchange rates and/or [[Interest Rate Quotations|interest rates]] change,  the value of the [[Forward Points in Currency|forward contract]] is no longer zero,  but is worth$$v_f(t, T) = e^{-r_{DOM}\tau}(F(t, T) - K) = S_t e^{-r_{FOR}\tau} - Ke^{-r_{DOM}\tau}$$

for a pre-specified exchange rate$K$. 

- This is the [[Forward Points in Currency|forward contract]] value in domestic [[Forwards and Futures Notes|currency]] units,  marked to the market at time$t$. 
- As stated previously,  setting$K = F(0,  T)$yields a zero-cost contract.

---

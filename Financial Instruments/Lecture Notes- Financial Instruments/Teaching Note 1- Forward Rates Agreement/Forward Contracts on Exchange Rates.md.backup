---
title: Forward Contracts on Exchange Rates
tags:
  - arbitrage
  - currency_risk
  - exchange_rates
  - forward_contracts
  - interest_rates
aliases:
  - Currency Forwards
  - FX Forwards
  - Forward FX Contracts
key_concepts:
  - Arbitrage strategy
  - Forward rate definition
  - Interest rate differential
  - Short forward contract
  - Spot exchange rate
---

[Foreign Exchange Quoting Conventions](Foreign%20Exchange%20Quoting%20Conventions.md)

- [Introduction](Ch1%20[[Squam%20Lake%20Group%20Introduction) to Derivative Markets]]
- [Hedging](Chapter%206%20(Hull)%20[[Key%20Rates%20O1s%20Durations%20and%20Hedging) Strategies with [Forwards](../../../Financial%20Markets/Financial%20Asset%20Pricing%20Theory%20Overview/Chapter%2012%20-%20Derivatives/Forwards%20and%20Futures.md)]]
- [Forward Exchange Rate](Deriving%20[[A%20Primer%20on%20Currency%20Derivatives) Numerical Example]]
- [Secondary Commodities](Primary%20vs.%20[[Primary%20vs.%20Secondary%20Commodities)]]
- [Foreign Exchange Quoting Conventions](Foreign%20Exchange%20Quoting%20Conventions.md)
- [Forward Contracts on Exchange Rates](.md)
- [Forwards and Futures]([[Forward%20and%20Futures%20Contracts) Notes]]
- [Hedging]([[Key%20Rates%20O1s%20Durations%20and%20Hedging) Strategies with [Forwards](../../../Financial%20Markets/Financial%20Asset%20Pricing%20Theory%20Overview/Chapter%2012%20-%20Derivatives/Forwards%20and%20Futures.md)]]
- [Financial Instruments]([[A%20Practical%20Guide%20for%20Actuaries%20and%20other%20Business%20Professionals.)/Lecture Notes/Teaching Note 1- Forward Rates Agreement/[Interest Rates](../../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%202/Interest%20Rate%20Quotations.md),  Carry Trades,  and Exchange Rate Movements]]
- [Teaching Note 1Forward Rates Agreement](Teaching%20Note%201Forward%20Rates%20Agreement)
# Forward Contracts on Exchange Rates

[Currency]([Forwards%20and%20Futures%20Notes) Forward]([Currency](Forwards%20and%20Futures%20Notes.md)%20Forward.md)
The rate of exchange for any date other than spot is a function of spot and the relative [interest rates](../../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%202/Interest%20Rate%20Quotations.md) in each [currency](Forwards%20and%20Futures%20Notes.md),  because the assumption is that any funds you have will be invested in a time deposit of that [currency](Forwards%20and%20Futures%20Notes.md). Theforward rate is the rate which neutralizes the effoct ofdiffirences in the Eurocurrenry [interest rates](../../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%202/Interest%20Rate%20Quotations.md). If this were not the case,  investors and speculators would always buy and invest in the high interest rate [currency](Forwards%20and%20Futures%20Notes.md),  eliminating their [exchange rate risk](../../Assignments/PSET%203%20Financial%20Instruments.md) with the [forward contract](../../../Clippings/Forward%20Points%20in%20Currency.md).

[Long forward](../Teaching%20Note%203%20Swaps-%20Financial%20Instruments/Forward%20Rates%20Agreement.md) exchange rate: At maturity,  purchase foreign [currency](Forwards%20and%20Futures%20Notes.md) and pay with home [currency](Forwards%20and%20Futures%20Notes.md)
[Short forward contract](.md): At maturity,  purchase home [currency](Forwards%20and%20Futures%20Notes.md) and pay with foreign [currency](Forwards%20and%20Futures%20Notes.md)

In summary,  the [forward rate](../../../Clippings/Forward%20Points%20in%20Currency.md) of exchange is the vehicle for adjusting for the interest rate differential. If you theoretically earn more in one [currency](Forwards%20and%20Futures%20Notes.md) than the other due to the interest rate differential,  the [forward exchange rate](../../../Financial%20Engineering/A%20Primer%20on%20Currency%20Derivatives.md) will exactly offset this gain. The interest rate differential,  adjusted for time,  determines the forward points. The forward points reflect only today's difference in [interest rates](../../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%202/Interest%20Rate%20Quotations.md); they are not an indication of what the future spot or [interest rates](../../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%202/Interest%20Rate%20Quotations.md) will be.

[Forward contract](../../../Clippings/Forward%20Points%20in%20Currency.md) to exchange foreign [currency](Forwards%20and%20Futures%20Notes.md) for home [currency](Forwards%20and%20Futures%20Notes.md)

- [Forward contract]([Forward%20Points%20in%20Currency) to exchange EUR for USD](Foreign%20Exchange%20Quoting%20Conventions.md)
- [Spot Exchange Rate](../../Review%20Session%20Notes/Arbitrage%20Opportunity%20Accounting.md):$M_{0} \frac{USD}{EUR}$
- [Forward Rate](../../../Clippings/Forward%20Points%20in%20Currency.md):$F_{0, T} \frac{USD}{EUR}$
- US Interest Rate:$r_{USD}$
- EUR Interest Rate:$r_{EUR}$

## PRICING OF FORWARD EXCHANGE RATE CONTRACTS
- Consider a US Investor with USD N to invest for 1 year. The Investor has 2 options to invest.
1. **Strategy A**
	1. Deposit N at at$r_{USD}$yielding at maturity T:$$\text{Payoff}_{A}=Ne^{(r_{USD})*T}$$
1. **Strategy B**
	1. Exchange USD N into EUR$\frac{N}{M_{0}}$
	1. Invest EUR$\frac{N}{M_{0}}$at$r_{EUR}$yielding at maturity T:$$\text{Payoff}_{B}= \left(\frac{N}{M_{0}}\right)e^{(r_{EUR})*T}$$
	1. Enter into a [forward contract](../../../Clippings/Forward%20Points%20in%20Currency.md) to buy dollars,  paying euros at [forward rate](../../../Clippings/Forward%20Points%20in%20Currency.md)$F_{0, T}$([Short forward](../Teaching%20Note%203%20Swaps-%20Financial%20Instruments/Forward%20Rates%20Agreement.md)).$$\text{Dollars recieved }= F_{0, T}* \left(\frac{N}{M_{0}}\right)e^{(r_{EUR})*T}$$
1. Under no [arbitrage](../../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%207/Arbitrage%20Pricing%20of%20Derivatives.md),  the payoffs to the two strategies must be equal.$$F_{0, T}* \left(\frac{N}{M_{0}}\right)e^{(r_{EUR})*T} = Ne^{(r_{USD})*T}$$
1. Solving for$F_{0, T}$, $$F_{0, T}=M_{0}e^{(r_{USD}-r_{EUR})*T}$$

---

#### ARBITRAGE STRATEGY WHEN $F_{0, T} > M_0 * E^{(R_S-R_E) T}$

ie. quoted [forward contract](../../../Clippings/Forward%20Points%20in%20Currency.md) is overvalued.
Short [forwards](../../../Financial%20Markets/Financial%20Asset%20Pricing%20Theory%20Overview/Chapter%2012%20-%20Derivatives/Forwards%20and%20Futures.md) contract by paying euros and accepting dollars

1. **Enter a [forward contract](../../../Clippings/Forward%20Points%20in%20Currency.md) to sell$N$euros at the [forward rate](../../../Clippings/Forward%20Points%20in%20Currency.md)$F_{0, T}$:**
	   Commit to sell euros in the future at the currently quoted [forward rate](../../../Clippings/Forward%20Points%20in%20Currency.md).
	   This is equivalent to [shorting](../../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%202%20-%20Spot%20Markets/Short%20Selling.md) the forward.
1. **Borrow$N \times e^{-r_e \times T} \times M_0$dollars and use it to buy$N \times e^{-r_e \times T}$euros:**
	   Take a loan in dollars now,  which will be repaid by the proceeds of selling euros at the [forward rate](../../../Clippings/Forward%20Points%20in%20Currency.md).
	   Convert the borrowed dollars to euros at the current [spot rate](../../../International%20Finance/The%20Foreign%20Exchange%20Market%20Annotations.md).
1. **Invest$N \times e^{-r_e \times T}$euros at the euro interest rate$r_e$until$T$:**
	   Invest the euros at the Euro [Basis Swap](A%20Guide%20to%20the%20Front%20End%20and%20[[Basis%20Swaps) Markets#[London Interbank Offered Rate](../../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%2012/Short-Term%20Rates%20and%20the%20Transition%20from%20LIBOR.md) (LIBOR)|LIBOR]] rate,  expecting them to grow back to$N$euros over time$T$.
### AT MATURITY $T$
- **Receive$\$F_{0, T} \times N$from the forward sale of euros:**
   - This is the dollar amount you get from selling$N$euros at the [forward rate](../../../Clippings/Forward%20Points%20in%20Currency.md).
- **Pay back the dollar loan of$\$(N \times e^{-r_e \times T} \times M_0) \times e^{r_s \times T}$:**
   - Repay the dollar loan which has grown to this amount with the US interest rate over time$T$.

- **The dollar profit at$T$is:**$$N \times (F_{0, T} - M_0 \times e^{(r_s-r_e) \times T})$$

  1. [Short forward contract](.md) (sell euros,  buy dollars)
  1. Borrow dollars
  1. Buy euro
  1. Invest in euro deposits
At maturity,
1. Collect [returns](../../../Financial%20Markets/Financial%20Asset%20Pricing%20Theory%20Overview/Chapter%203%20-%20%20Assets,%20Portfolios,%20and%20Arbitrage/Assets.md) from euro deposits
1. Deliver euros and receive dollars
1. Pay back loan obligation

### ARBITRAGE STRATEGY WHEN ${} F_{0, T} < M_0 * E^{(R_S-R_E) * T} {}$
1. **Enter into a [forward contract](../../../Clippings/Forward%20Points%20in%20Currency.md) to buy$N$euros at [forward rate](../../../Clippings/Forward%20Points%20in%20Currency.md)$F_{0, T}$:**
	- This step locks in the price at which you will buy euros in the future.

1. **Borrow$N \times e^{-r_e \times T}$euros:**
	- Borrow euros now at the current Euro [Basis Swap](A%20Guide%20to%20the%20Front%20End%20and%20[[Basis%20Swaps) Markets#[London Interbank Offered Rate](../../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%2012/Short-Term%20Rates%20and%20the%20Transition%20from%20LIBOR.md) (LIBOR)|LIBOR]] rate,  and you will need to pay back the borrowed amount multiplied by the exponential of the negative Euro interest rate times the [time to maturity](Hedging%20Strategies%20with%20Forwards.md)$T$.

1. **Exchange them to$N \times e^{-r_e \times T} \times M_0$dollars:**
	- Convert the borrowed euros to dollars at the current [spot rate](../../../International%20Finance/The%20Foreign%20Exchange%20Market%20Annotations.md).

1. **Invest$N \times e^{-r_e \times T} \times M_0$dollars at the dollar interest rate$r_s$:**
	- Invest the dollar amount at the current US [Basis Swap](A%20Guide%20to%20the%20Front%20End%20and%20[[Basis%20Swaps) Markets#[London Interbank Offered Rate](../../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%2012/Short-Term%20Rates%20and%20the%20Transition%20from%20LIBOR.md) (LIBOR)|LIBOR]] rate,  and the [investment](../../../Advanced%20Investments/An%20Asset%20Allocation%20Primer.md) will grow according to the dollar interest rate over the [time to maturity](Hedging%20Strategies%20with%20Forwards.md)$T$.

1. **At maturity$T$,  the arbitrageur:**
	- Receives$N$euros from the [forward contract](../../../Clippings/Forward%20Points%20in%20Currency.md) and pays$F_{0, T} \times N$dollars for them.
	- Pays back the euro loan of$N \times e^{-r_e \times T}$euros,  which has grown to$N$euros by$T$.
	- Receives proceeds from the dollar [investment](../../../Advanced%20Investments/An%20Asset%20Allocation%20Primer.md),  which is the invested amount multiplied by the exponential of the dollar interest rate times$T$.

1. **Dollar Profit at$T$:**
	- The profit is calculated as the proceeds from the dollar [investment](../../../Advanced%20Investments/An%20Asset%20Allocation%20Primer.md) minus the cost of buying euros in the [forward contract](../../../Clippings/Forward%20Points%20in%20Currency.md).

1. [Long forward](../Teaching%20Note%203%20Swaps-%20Financial%20Instruments/Forward%20Rates%20Agreement.md) (buy euros,  pay dollars)
1. Borrow euros
1. Convert to dollars
1. invest in dollars deposits
At maturity,
1. Collect [returns](../../../Financial%20Markets/Financial%20Asset%20Pricing%20Theory%20Overview/Chapter%203%20-%20%20Assets,%20Portfolios,%20and%20Arbitrage/Assets.md) from dollar deposits
1. Pay dollars to forward counterparty
1. Collect euros
1. Use euros to pay back euro loan

[Hedging]([Key%20Rates%20O1s%20Durations%20and%20Hedging) Strategies with [Forwards](../../../Financial%20Markets/Financial%20Asset%20Pricing%20Theory%20Overview/Chapter%2012%20-%20Derivatives/Forwards%20and%20Futures.md)]([Hedging](../../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%205/Key%20Rates%20O1s%20Durations%20and%20Hedging.md)%20Strategies%20with%20Forwards.md)
[Hedging]([Key%20Rates%20O1s%20Durations%20and%20Hedging) with [Forwards](../../../Financial%20Markets/Financial%20Asset%20Pricing%20Theory%20Overview/Chapter%2012%20-%20Derivatives/Forwards%20and%20Futures.md)]([Hedging](../../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%205/Key%20Rates%20O1s%20Durations%20and%20Hedging.md)%20with%20Forwards.md)
---

### TABLE 1: OVERVALUED FORWARD RATE
- In this scenario,  the arbitrageur believes that the [forward rate](../../../Clippings/Forward%20Points%20in%20Currency.md) for buying euros is overvalued,  meaning that the market's [forward rate](../../../Clippings/Forward%20Points%20in%20Currency.md) is higher than what it should be based on [interest rate differentials](../../../Financial%20Markets/Random%20Walks%20in%20Fixed%20Income%20and%20Foreign%20Exchange/Chapter%201/What%20Really%20Is%20the%20Cross-Currency%20Basis.md).

| Trade | Payoff |
| --- | --- |
| Enter a [forward contract](../../../Clippings/Forward%20Points%20in%20Currency.md) to sell euros at the overvalued [forward rate](../../../Clippings/Forward%20Points%20in%20Currency.md) $F_{0, T}$ | 0 |
| Borrow euros at the current [spot rate](../../../International%20Finance/The%20Foreign%20Exchange%20Market%20Annotations.md) $M_0$ | $-N \times e^{-r_e \times T}$ |
| Convert borrowed euros to dollars at [spot rate](../../../International%20Finance/The%20Foreign%20Exchange%20Market%20Annotations.md) $M_0$ | $N \times e^{-r_e \times T} \times M_0$ |
| Invest the dollar amount at the US interest rate $r_s$ | $N \times e^{-r_e \times T} \times M_0 \times e^{r_s \times T}$ |
| At maturity $T$,  fulfill the [forward contract](../../../Clippings/Forward%20Points%20in%20Currency.md) | $-N \times F_{0, T}$ |
| Pay back the euro loan | $N$ |
| **Net Profit/Loss at $T$** | $N \times (e^{-r_e \times T} \times M_0 \times e^{r_s \times T} - F_{0, T})$ |

### TABLE 2: UNDERVALUED FORWARD RATE
- In this scenario,  the arbitrageur believes that the [forward rate](../../../Clippings/Forward%20Points%20in%20Currency.md) for buying euros is undervalued,  meaning that the market's [forward rate](../../../Clippings/Forward%20Points%20in%20Currency.md) is lower than what it should be based on [interest rate differentials](../../../Financial%20Markets/Random%20Walks%20in%20Fixed%20Income%20and%20Foreign%20Exchange/Chapter%201/What%20Really%20Is%20the%20Cross-Currency%20Basis.md).

| Trade | Payoff |
| --- | --- |
| Enter a [forward contract](../../../Clippings/Forward%20Points%20in%20Currency.md) to buy euros at the undervalued [forward rate](../../../Clippings/Forward%20Points%20in%20Currency.md) $F_{0, T}$ | 0 |
| Borrow dollars at the current [spot rate](../../../International%20Finance/The%20Foreign%20Exchange%20Market%20Annotations.md)$M_0$|$-N \times e^{-r_s \times T} \times M_0$|
| Convert borrowed dollars to euros at [spot rate](../../../International%20Finance/The%20Foreign%20Exchange%20Market%20Annotations.md)$M_0$|$N \times e^{-r_s \times T}$|
| Invest the euro amount at the Euro interest rate$r_e$|$N \times e^{-r_s \times T} \times e^{r_e \times T}$|
| At maturity$T$,  fulfill the [forward contract](../../../Clippings/Forward%20Points%20in%20Currency.md) |$N \times F_{0, T}$|
| Pay back the dollar loan |$N \times e^{-r_s \times T} \times M_0 \times e^{r_s \times T}$|
| **Net Profit/Loss at$T$** |$N \times (F_{0, T} - e^{-r_s \times T} \times M_0 \times e^{r_s \times T})$|

---

[Deriving [Forward Exchange Rate](../../../Financial%20Engineering/A%20Primer%20on%20Currency%20Derivatives.md) Numerical Example 1](Deriving%20Forward%20Exchange%20Rate%20Numerical%20Example%201.md)
[Teaching Note 2-[Futures Contracts](../../../Financial%20Engineering/Mathematics%20of%20the%20Financial%20Markets.md)](Teaching%20Note%202-[Futures](../../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%203%20-%20Futures%20Markets/Futures%20Not%20Subject%20to%20Cash-And-Carry.md)%20Contracts.md)
[Primary vs. [Secondary Commodities](Primary%20vs.%20Secondary%20Commodities.md)](Primary%20vs.%20Secondary%20Commodities.md)
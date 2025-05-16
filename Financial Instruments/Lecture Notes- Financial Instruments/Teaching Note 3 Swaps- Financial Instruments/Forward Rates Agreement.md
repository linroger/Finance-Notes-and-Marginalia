---
title: Forward Rates Agreement
cssclasses:
  - academia
tags:
  - arbitrage
  - forward_contracts
  - law_of_one_price
  - no_arbitrage
  - spot_exchange
aliases:
  - arbitrage opportunity
  - forward rate
  - long forward
  - short forward
  - spot rate
key_concepts:
  - buy cheap sell dear
  - exchange goods for money
  - identical payoffs same price
  - no arbitrage principle
  - prespecified future date price
---

[Deriving [Forward Exchange Rate](../../../Financial%20Engineering/A%20Primer%20on%20Currency%20Derivatives.md) Numerical Example 1](Deriving%20Forward%20Exchange%20Rate%20Numerical%20Example%201.md)

[Foreign Exchange Quoting Conventions](Foreign%20Exchange%20Quoting%20Conventions.md)

[Interest Rates]([Interest%20Rate%20Quotations),  Carry Trades,  and Exchange Rate Movements](Asset%20Classes/[Derivatives](../../../Financial%20Markets/Financial%20Trading%20and%20Markets/Chapter%209%20Arbitrage%20and%20Hedging%20With%20Options.md)/Forward%20and%20Futures/Forward%20Exchange%20Rate%20Contracts/Foreign%20Exchange%20Notes/Interest%20Rates,  %20Carry%20Trades,  %20and%20Exchange%20Rate%20Movements.md)

[Forward Contracts on Exchange Rates](Forward%20Contracts%20on%20Exchange%20Rates.md)

**[Teaching Note 3 SwapsFinancial Instruments](Teaching%20Note%203%20SwapsFinancial%20Instruments)**
	- [Forward Rates Agreement](.md)
	- [Overnight Index Swaps (OIS)](Overnight%20Index%20Swaps%20(OIS).md)
	- [Swaps Types](Swaps%20Types.md)
	- [Teaching Note 3 SwapsFinancial Instruments](Teaching%20Note%203%20SwapsFinancial%20Instruments)
	- [Swap Contract](The%20Value%20of%20the%20[[Currency%20Swaps) after Initiation]]
### NO ARBITRAGE PRINCIPLE
- An [Arbitrage](../../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%207/Arbitrage%20Pricing%20of%20Derivatives.md) Opportunity is a trading strategy that either
	1. Costs nothing today and yields a positive profit in the future; or
	1. Yields a positive profit today,  and zero cash in the future.
- In well functioning markets,  no [arbitrage opportunities](../../../Financial%20Markets%20and%20Institutions/III.%20Liquidity%20of%20Assets/Class%208-%20Markets,%20Meltdowns,%20and%20Arbitrage/Class%20Note%2013%20The%20LTCM%20Meltdown.md) may arise.
	- If there were,  arbitrageurs would take massive positions to profit from them,  equilibrating the market.
- The value of [derivative securities](../../../Financial%20Engineering/Financial%20Mathematics%20Course.md),  including [forwards](../../../Financial%20Markets/Financial%20Asset%20Pricing%20Theory%20Overview/Chapter%2012%20-%20Derivatives/Forwards%20and%20Futures.md),  [futures](../../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%203%20-%20Futures%20Markets/Futures%20Not%20Subject%20to%20Cash-And-Carry.md),  swaps and options,  are determined by assuming that no [arbitrage opportunities](../../../Financial%20Markets%20and%20Institutions/III.%20Liquidity%20of%20Assets/Class%208-%20Markets,%20Meltdowns,%20and%20Arbitrage/Class%20Note%2013%20The%20LTCM%20Meltdown.md) exist.

---
### THE LAW OF ONE PRICE

Securities with identical payoffs must have the same price.

- Otherwise,  an [arbitrage opportunities](../../../Financial%20Markets%20and%20Institutions/III.%20Liquidity%20of%20Assets/Class%208-%20Markets,%20Meltdowns,%20and%20Arbitrage/Class%20Note%2013%20The%20LTCM%20Meltdown.md) arises
	- Buy Cheap / Sell Dear
- Buy the low-priced security and sell the high-priced one.
- At maturity the arbitrageur is hedged,  since the cash flows are the same.

## FORWARD CONTRACTS
- A [Forward contract](../../../Clippings/Forward%20Points%20in%20Currency.md) is an agreement between two counterparties to buy or sell a prespecified amount of goods or securities at a prespecified future date$T$at a prespecified price$F$
 - It does not cost anything to enter into a [forward contract](../../../Clippings/Forward%20Points%20in%20Currency.md) at time 0
	 - The contract is about exchanging goods (or securities) for money in the future,  and not today.
 - The prespecified price$F$moves to ensure that the value of the [forward contract](../../../Clippings/Forward%20Points%20in%20Currency.md) is zero for both counterparties at the inception of the contract.
- Let$N$be the size of the contract and${} S_t$the price of the good or security at$t$.

-The Profit/Loss at$T$are$$\text{P/L counterpary long the forward} =N\times(S_T-F)$$$$\text{P/L counterpary short the forward} =N\times(F-S_T)$$

- For instance,  the party long the forward agrees to buy at$T$a security for$F$when its value is$S_T$
	- If$S_T> F$,  it makes a profit (it pays only$F$instead of$S_T)$
	- If$S_T< F$,  it makes a loss (it pays$F$instead of the cheaper${} S_T)$
- On the other hand,  the party short the forward agrees to sell at$T$a security for$F$when its value is${} S_T$
	 - If$S_T< F$,  it makes a profit (they receive higher price$F$above prevailing market price of$S_T)$
	 - If$S_T> F$,  it makes a loss (they receive a price$F$below the market price${} S_T)$

[Long forward](.md) exchange rate: At maturity,  purchase foreign [currency](../Teaching%20Note%201-%20Forward%20Rates%20Agreement/Forwards%20and%20Futures%20Notes.md) and pay with home [currency](../Teaching%20Note%201-%20Forward%20Rates%20Agreement/Forwards%20and%20Futures%20Notes.md)

[Short forward contract](../Teaching%20Note%201-%20Forward%20Rates%20Agreement/Forward%20Contracts%20on%20Exchange%20Rates.md): At maturity,  purchase home [currency](../Teaching%20Note%201-%20Forward%20Rates%20Agreement/Forwards%20and%20Futures%20Notes.md) and pay with foreign [currency](../Teaching%20Note%201-%20Forward%20Rates%20Agreement/Forwards%20and%20Futures%20Notes.md)

***[Forward contract](../../../Clippings/Forward%20Points%20in%20Currency.md) to exchange foreign [currency](../Teaching%20Note%201-%20Forward%20Rates%20Agreement/Forwards%20and%20Futures%20Notes.md) for home [currency](../Teaching%20Note%201-%20Forward%20Rates%20Agreement/Forwards%20and%20Futures%20Notes.md)
- [Forward contract](../../../Clippings/Forward%20Points%20in%20Currency.md) to exchange EUR for USD
- [Spot Exchange Rate](../../Review%20Session%20Notes/Arbitrage%20Opportunity%20Accounting.md):$S_{0} \frac{USD}{EUR}$
- [Forward Rate](../../../Clippings/Forward%20Points%20in%20Currency.md):$F_{0,  T} \frac{USD}{EUR}$
- US Interest Rate:$r_{USD}$
- EUR Interest Rate:$r_{EUR}$

***[Pricing](../../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%207/Arbitrage%20Pricing%20of%20Derivatives.md) of [Forward Exchange Rate](../../../Financial%20Engineering/A%20Primer%20on%20Currency%20Derivatives.md) Contracts
- Consider a US Investor with USD N to invest for 1 year. The Investor has 2 options to invest.
1. **Strategy A**
	1. Deposit N at at$r_{USD}$yielding at maturity T:$$\text{Payoff}_{A}=Ne^{(r_{USD})*T}$$
1. **Strategy B**
	1. Exchange USD N into EUR$\frac{N}{S_{0}}$
	1. Invest EUR$\frac{N}{S_{0}}$at$r_{EUR}$yielding at maturity T:$$\text{Payoff}_{B}= \left(\frac{N}{S_{0}}\right)e^{(r_{EUR})*T}$$
	1. Enter into a [forward contract](../../../Clippings/Forward%20Points%20in%20Currency.md) to buy dollars,  paying euros at [forward rate](../../../Clippings/Forward%20Points%20in%20Currency.md)$F_{0,  T}$([Short forward](.md)).$$\text{Dollars recieved }= F_{0,  T}* \left(\frac{N}{S_{0}}\right)e^{(r_{EUR})*T}$$
1. Under no [arbitrage](../../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%207/Arbitrage%20Pricing%20of%20Derivatives.md),  the payoffs to the two strategies must be equal.$$F_{0,  T}* \left(\frac{N}{S_{0}}\right)e^{(r_{EUR})*T} = Ne^{(r_{USD})*T}$$
1. Solving for$F_{0,  T}$,  $$F_{0,  T}=S_{0}e^{(r_{USD}-r_{EUR})*T}$$

---

#### ARBITRAGE STRATEGY WHEN $F_{0,  T} > S_0 \times e^{(R_S-R_E) \times T}$

ie. quoted [forward contract](../../../Clippings/Forward%20Points%20in%20Currency.md) is overvalued.

Short [forwards](../../../Financial%20Markets/Financial%20Asset%20Pricing%20Theory%20Overview/Chapter%2012%20-%20Derivatives/Forwards%20and%20Futures.md) contract by paying euros and accepting dollars

1. **Enter a [forward contract](../../../Clippings/Forward%20Points%20in%20Currency.md) to sell$N$euros at the [forward rate](../../../Clippings/Forward%20Points%20in%20Currency.md)$F_{0,  T}$:**
	   Commit to sell euros in the future at the currently quoted [forward rate](../../../Clippings/Forward%20Points%20in%20Currency.md).
	   This is equivalent to [shorting](../../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%202%20-%20Spot%20Markets/Short%20Selling.md) the forward.
1. **Borrow$N \times e^{-r_e \times T} \times M_0$dollars and use it to buy$N \times e^{-r_e \times T}$euros:**
	   Take a loan in dollars now,  which will be repaid by the proceeds of selling euros at the [forward rate](../../../Clippings/Forward%20Points%20in%20Currency.md).
	   Convert the borrowed dollars to euros at the current [spot rate](../../../International%20Finance/The%20Foreign%20Exchange%20Market%20Annotations.md).
1. **Invest$N \times e^{-r_e \times T}$euros at the euro interest rate$r_e$until$T$:**
	   Invest the euros at the Euro [Basis Swap](A%20Guide%20to%20the%20Front%20End%20and%20[[Basis%20Swaps) Markets#[London Interbank Offered Rate](../../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%2012/Short-Term%20Rates%20and%20the%20Transition%20from%20LIBOR.md) (LIBOR)|LIBOR]] rate,  expecting them to grow back to$N$euros over time$T$.
### AT MATURITY $T$
- **Receive$\$F_{0,  T} \times N$from the forward sale of euros:**
   - This is the dollar amount you get from selling$N$euros at the [forward rate](../../../Clippings/Forward%20Points%20in%20Currency.md).
- **Pay back the dollar loan of$\$(N \times e^{-r_e \times T} \times M_0) \times e^{r_s \times T}$:**
   - Repay the dollar loan which has grown to this amount with the US interest rate over time$T$.

- **The dollar profit at$T$is:**$$N \times (F_{0,  T} - M_0 \times e^{(r_s-r_e) \times T})$$

  1. [Short forward contract](../Teaching%20Note%201-%20Forward%20Rates%20Agreement/Forward%20Contracts%20on%20Exchange%20Rates.md) (sell euros,  buy dollars)
  1. Borrow dollars
  1. Buy euro
  1. Invest in euro deposits
At maturity,
1. Collect [returns](../../../Financial%20Markets/Financial%20Asset%20Pricing%20Theory%20Overview/Chapter%203%20-%20%20Assets,%20Portfolios,%20and%20Arbitrage/Assets.md) from euro deposits
1. Deliver euros and receive dollars
1. Pay back loan obligation

### ARBITRAGE STRATEGY WHEN $F_{0,  T} < M_0 \times E^{(R_S-R_E) \times T}$
1. **Enter into a [forward contract](../../../Clippings/Forward%20Points%20in%20Currency.md) to buy$N$euros at [forward rate](../../../Clippings/Forward%20Points%20in%20Currency.md)$F_{0,  T}$:**
	- This step locks in the price at which you will buy euros in the future.

1. **Borrow$N \times e^{-r_e \times T}$euros:**
	- Borrow euros now at the current Euro [Basis Swap](A%20Guide%20to%20the%20Front%20End%20and%20[[Basis%20Swaps) Markets#[London Interbank Offered Rate](../../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%2012/Short-Term%20Rates%20and%20the%20Transition%20from%20LIBOR.md) (LIBOR)|LIBOR]] rate,  and you will need to pay back the borrowed amount multiplied by the exponential of the negative Euro interest rate times the [time to maturity](../Teaching%20Note%201-%20Forward%20Rates%20Agreement/Hedging%20Strategies%20with%20Forwards.md)$T$.

1. **Exchange them to$N \times e^{-r_e \times T} \times M_0$dollars:**
	- Convert the borrowed euros to dollars at the current [spot rate](../../../International%20Finance/The%20Foreign%20Exchange%20Market%20Annotations.md).

1. **Invest$N \times e^{-r_e \times T} \times M_0$dollars at the dollar interest rate$r_s$:**
	- Invest the dollar amount at the current US [Basis Swap](A%20Guide%20to%20the%20Front%20End%20and%20[[Basis%20Swaps) Markets#[London Interbank Offered Rate](../../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%2012/Short-Term%20Rates%20and%20the%20Transition%20from%20LIBOR.md) (LIBOR)|LIBOR]] rate,  and the [investment](../../../Advanced%20Investments/An%20Asset%20Allocation%20Primer.md) will grow according to the dollar interest rate over the [time to maturity](../Teaching%20Note%201-%20Forward%20Rates%20Agreement/Hedging%20Strategies%20with%20Forwards.md)$T$.

1. **At maturity$T$,  the arbitrageur:**
	- Receives$N$euros from the [forward contract](../../../Clippings/Forward%20Points%20in%20Currency.md) and pays$F_{0,  T} \times N$dollars for them.
	- Pays back the euro loan of$N \times e^{-r_e \times T}$euros,  which has grown to$N$euros by$T$.
	- Receives proceeds from the dollar [investment](../../../Advanced%20Investments/An%20Asset%20Allocation%20Primer.md),  which is the invested amount multiplied by the exponential of the dollar interest rate times$T$.

1. **Dollar Profit at$T$:**
	- The profit is calculated as the proceeds from the dollar [investment](../../../Advanced%20Investments/An%20Asset%20Allocation%20Primer.md) minus the cost of buying euros in the [forward contract](../../../Clippings/Forward%20Points%20in%20Currency.md).

1. [Long forward](.md) (buy euros,  pay dollars)
1. Borrow euros
1. Convert to dollars
1. invest in dollars deposits
At maturity,
1. Collect [returns](../../../Financial%20Markets/Financial%20Asset%20Pricing%20Theory%20Overview/Chapter%203%20-%20%20Assets,%20Portfolios,%20and%20Arbitrage/Assets.md) from dollar deposits
1. Pay dollars to forward counterparty
1. Collect euros
1. Use euros to pay back euro loan
---

### TABLE 1: OVERVALUED FORWARD RATE
- In this scenario,  the arbitrageur believes that the [forward rate](../../../Clippings/Forward%20Points%20in%20Currency.md) for buying euros is overvalued,  meaning that the market's [forward rate](../../../Clippings/Forward%20Points%20in%20Currency.md) is higher than what it should be based on [interest rate differentials](../../../Financial%20Markets/Random%20Walks%20in%20Fixed%20Income%20and%20Foreign%20Exchange/Chapter%201/What%20Really%20Is%20the%20Cross-Currency%20Basis.md).

| Trade | Payoff |
| --- | --- |
| Enter a [forward contract](../../../Clippings/Forward%20Points%20in%20Currency.md) to sell euros at the overvalued [forward rate](../../../Clippings/Forward%20Points%20in%20Currency.md) $F_{0,  T}$ | 0 |
| Borrow euros at the current [spot rate](../../../International%20Finance/The%20Foreign%20Exchange%20Market%20Annotations.md) $M_0$ | $-N \times e^{-r_e \times T}$ |
| Convert borrowed euros to dollars at [spot rate](../../../International%20Finance/The%20Foreign%20Exchange%20Market%20Annotations.md) $M_0$ | $N \times e^{-r_e \times T} \times M_0$ |
| Invest the dollar amount at the US interest rate $r_s$ | $N \times e^{-r_e \times T} \times M_0 \times e^{r_s \times T}$ |
| At maturity $T$,   fulfill the [forward contract](../../../Clippings/Forward%20Points%20in%20Currency.md) | $-N \times F_{0,  T}$ |
| Pay back the euro loan | $N$ |
| **Net Profit/Loss at $T$** | $N \times (e^{-r_e \times T} \times M_0 \times e^{r_s \times T} - F_{0,  T})$ |

### TABLE 2: UNDERVALUED FORWARD RATE
- In this scenario,  the arbitrageur believes that the [forward rate](../../../Clippings/Forward%20Points%20in%20Currency.md) for buying euros is undervalued,  meaning that the market's [forward rate](../../../Clippings/Forward%20Points%20in%20Currency.md) is lower than what it should be based on [interest rate differentials](../../../Financial%20Markets/Random%20Walks%20in%20Fixed%20Income%20and%20Foreign%20Exchange/Chapter%201/What%20Really%20Is%20the%20Cross-Currency%20Basis.md).

| Trade | Payoff |
| --- | --- |
| Enter a [forward contract](../../../Clippings/Forward%20Points%20in%20Currency.md) to buy euros at the undervalued [forward rate](../../../Clippings/Forward%20Points%20in%20Currency.md) $F_{0,  T}$ | 0 |
| Borrow dollars at the current [spot rate](../../../International%20Finance/The%20Foreign%20Exchange%20Market%20Annotations.md) $M_0$ | $-N \times e^{-r_s \times T} \times M_0$ |
| Convert borrowed dollars to euros at [spot rate](../../../International%20Finance/The%20Foreign%20Exchange%20Market%20Annotations.md)$M_0$|$N \times e^{-r_s \times T}$|
| Invest the euro amount at the Euro interest rate$r_e$|$N \times e^{-r_s \times T} \times e^{r_e \times T}$|
| At maturity$T$,   fulfill the [forward contract](../../../Clippings/Forward%20Points%20in%20Currency.md) |$N \times F_{0,  T}$|
| Pay back the dollar loan |$N \times e^{-r_s \times T} \times M_0 \times e^{r_s \times T}$|
| **Net Profit/Loss at$T$** |$N \times (F_{0,  T} - e^{-r_s \times T} \times M_0 \times e^{r_s \times T})$|

---

# Forward Rates Agreement

- The earlier derivation was obtained for [currency forwards](../Teaching%20Note%201-%20Forward%20Rates%20Agreement/Forward%20Contracts%20on%20Exchange%20Rates.md).
- Similar derivations hold for other securities,  such as stocks,  bonds,  and [commodities](../../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%203%20-%20Futures%20Markets/Futures%20Not%20Subject%20to%20Cash-And-Carry.md).
- Here is a list of "formulas". A good exercise is to go over the steps again.

| Security | [Forward Price](../../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%2011/Forward%20Contracts%20and%20Forward%20Prices.md) |
|----------|---------------|

| [Currency](../Teaching%20Note%201-%20Forward%20Rates%20Agreement/Forwards%20and%20Futures%20Notes.md) (e.g. dollar vs euro) |$$F_{0,  T} = M_0 \times e^{(r_s-r_e)T}$$|

| Stock: no dividend |$$F_{0,  T} = S_0 \times e^{rT}$$

|

| Stock: dividend yield$q$|$$F_{0,  T} = S_0 \times e^{(r-q)T}$$

|

| Stock: known Dividend$D$at$T_1 < T$|$$F_{0,  T} = \left(S_0 - D \times e^{-rT_1}\right) \times e^{rT}$$

|

| Commodity: Storage cost$U$. No "convenience yield" |$$F_{0,  T} = \left(S_0 + PV(U)\right) \times e^{rT}$$

|

| Commodity: % storage cost$u$. No "convenience yield" |$$F_{0,  T} = S_0 \times e^{(r+u)T}$$

|

| Commodity: % storage cost$u$,  convenient yield$y$|$$F_{0,  T} = S_0 \times e^{(r+u-y)T}$$

|

| Bond: Zero Coupon with Maturity$T^* > T$|$$F_{0,  T} = \frac{Z(0,  T^*)}{Z(0,  T)}$$

|

| Bond: with Semi-annual Coupon$c$,  Maturity$T_n$|$$F_{0,  T} = \frac{\sum_{i=m+1}^{n} c \times \frac{Z(0,  T_i)}{Z(0,  T)} + c \times \frac{Z(0,  T_n)}{Z(0,  T)}}{1 + \frac{i}{2} \times \frac{Z(0,  T)}{Z(0,  T)}}$$

|

- In all cases,  the value of a [forward contract](../../../Clippings/Forward%20Points%20in%20Currency.md) at time$t > 0$(after initiation) is:
$$f_{t,  T} = e^{-r(T-t)}[F_{0,  T} - F_{t,  T}]$$

1. Assume that at time t months the Euro appreciated from$S_{0}$to$S_{t}$,  with$S_0<S_t$
1. If the US firm wants to cancel the contract with the bank,  how much does it have to pay?

	- The US firm can enter into the reverse [forward contract](../../../Clippings/Forward%20Points%20in%20Currency.md) with the bank,  with payoff$$\text{Dollar payoff at$T$of reverse forward contract} = N × (S_{T} − F_{t,   T})$$Now:$$F_{t,  T} = S_t × e^{(r_{USD}−r_{EUR})×(T −t)}$$
	- The reverse contract neutralizes the former one.
- Payoff at$T$from forward + reverse forward$$= N\times (F_{0,  T}-S_T)+N \times(M_T-F_{t,  T})$$$$= N\times(F_{0,  T}- F_{t,   T})$$
- The US firm will have to pay the bank$N\times(F_{0,  T}- F_{t,   T})$at$T$
	- The Present Value of$N\times(F_{0,  T}- F_{t,   T})$is the value of the original [forward contract](../../../Clippings/Forward%20Points%20in%20Currency.md) to the US firm
$$
f_{t,  T}=e^{-r_{\$}\times(T-t)}\times(F_{0,  T}-F_{t,  T})\times N
$$

- Since it costs$e^{-r_{\$}\times(T-t)}\times(F_{0,  T}-F_{t,  T})\times N$to close the position,  the value of the [forward contract](../../../Clippings/Forward%20Points%20in%20Currency.md) to the firm must equal this amount.
	- Vice-versa,  the value to the bank must be$e^{-r_{\$}\times(T-t)}\times(F_{0,  T}-F_{t,  T})\times N$

> [!note]
> The above formula is general: The value of a [forward contract](../../../Clippings/Forward%20Points%20in%20Currency.md) to $sell$ euros at a prespecifled
>
> price $K$ is always given by $$f_{t,  T}=e^{-r_{\$}\times(T-t)}\times(K-F_{t,  T})$$

To summarize,  we found:

1. The Forward (Delivery) Price - the price decided at time 0 to buy / sell goods (Euros) in the future is given by$$
\begin{aligned}F_{0,  T}=S_0\times e^{(r_{\$}-r_e)T}\end{aligned}

$$
2. The value of an $existing$ [forward contract](../../../Clippings/Forward%20Points%20in%20Currency.md) to deliver goods (Euros) at preset price $K$ (determined some time in the past) is equal to the cost / profit of closing the contract: $$ f_{t,  T}=[K-F_{t,  T}]\times e^{-r_{\$}(T-t)}$$
- This is the value of [forward contract](../../../Clippings/Forward%20Points%20in%20Currency.md) to $sell$. 

- What is the value of a [forward contract](../../../Clippings/Forward%20Points%20in%20Currency.md) to buy (i.e. a [long forward](.md) contract?)

**Valuation of a [Long Forward](.md) Contract at Time $t$
Set Up the Current Value Notation
- Let $F_{0,  T}$ be the [forward rate](../../../Clippings/Forward%20Points%20in%20Currency.md) agreed upon at initiation for exchange at future time $T$.
- Let $F_{t,  T}$ be the [forward rate](../../../Clippings/Forward%20Points%20in%20Currency.md) at the intermediate time $t$ for the same exchange at time $T$.
- Let $S_t$ be the [spot rate](../../../International%20Finance/The%20Foreign%20Exchange%20Market%20Annotations.md) at the intermediate time $t$.
- Let $r$ be the domestic [risk-free interest rate](../../../Financial%20Markets/Financial%20Asset%20Pricing%20Theory%20Overview/Chapter%2012%20-%20Derivatives/Exercises.md); $r_{\text{USD}}$.
- Let $N$ be the notional amount of foreign [currency](../Teaching%20Note%201-%20Forward%20Rates%20Agreement/Forwards%20and%20Futures%20Notes.md) (Euros in this context) to be exchanged.

**Determine the Payoff of the Original [Forward Contract](../../../Clippings/Forward%20Points%20in%20Currency.md)
- At maturity $T$,   the payoff to the [long position](../../../Financial%20Engineering/Derivatives/Part%20I%20-%20Forwards%20and%20Futures/Chapter%204%20-%20Futures:%20Hedging%20and%20Speculation.md) in the original [forward contract](../../../Clippings/Forward%20Points%20in%20Currency.md) is $$N \times (S_T - F_{0,  T})$$
***Calculate the Reverse [Forward Contract](../../../Clippings/Forward%20Points%20in%20Currency.md)
- To exit the forward position,   the firm enters into a reverse [forward contract](../../../Clippings/Forward%20Points%20in%20Currency.md),   agreeing at time $t$ to sell Euros at the new [forward rate](../../../Clippings/Forward%20Points%20in%20Currency.md) $F_{t,  T}$.
- The payoff of the reverse contract at maturity $T$ is $N \times (F_{t,  T} - S_T)$.

***Combine Forward and Reverse Forward Payoffs
- The two payoffs $N \times (S_T - F_{0,  T})$ and $N \times (F_{t,  T} - S_T)$ offset each other.
- The net payoff from both contracts at $T$ is $N \times (F_{0,  T} - F_{t,  T})$.

***Calculate the Present Value at Time $t$
- The present value of the net payoff is the value of the original [forward contract](../../../Clippings/Forward%20Points%20in%20Currency.md) to the [long position](../../../Financial%20Engineering/Derivatives/Part%20I%20-%20Forwards%20and%20Futures/Chapter%204%20-%20Futures:%20Hedging%20and%20Speculation.md). 
- That value,   discounted back from $T$ to $t$,   is calculated as: $$f_{t,  T} = N \times (F_{0,  T} - F_{t,  T}) \times e^{-r \times (T - t)}$$
***Final Value of a [Long Forward](.md) Contract at Time $t$
- The value of the [long forward](.md) contract at time $t$ is therefore: $$f_{t,  T} = N \times (F_{0,  T} - F_{t,  T}) \times e^{-r_{\text{USD}} \times (T - t)}$$
This equation reflects the current value of the [long forward](.md) position: If $F_{0,  T} > F_{t,  T}$,   the value is positive,   indicating that the [spot rate](../../../International%20Finance/The%20Foreign%20Exchange%20Market%20Annotations.md) has moved favorably since the contract was initiated. Conversely,   if $F_{0,  T} < F_{t,  T}$,   the value is negative,   reflecting an unfavorable move in the [spot rate](../../../International%20Finance/The%20Foreign%20Exchange%20Market%20Annotations.md). As you mentioned,   since it costs $f_{t,  T}$ to close the position (buy back the [forward contract](../../../Clippings/Forward%20Points%20in%20Currency.md)),   this must also be the value of the original [forward contract](../../../Clippings/Forward%20Points%20in%20Currency.md) from the perspective of the long (buy) side.

To summarize our findings:
- The Forward (Delivery) Price - The price determined at time 0 to buy or sell the foreign [currency](../Teaching%20Note%201-%20Forward%20Rates%20Agreement/Forwards%20and%20Futures%20Notes.md) (Euros in this case) in the future is given by: $$F_{0,  T} = S_0 \times e^{(r_{\text{USD}} - r_{\text{EUR}})T}$$
- The Value of an Existing [Long Forward](.md) Contract - The value of a [forward contract](../../../Clippings/Forward%20Points%20in%20Currency.md) agreed upon in the past at a preset price for the future delivery of the foreign [currency](../Teaching%20Note%201-%20Forward%20Rates%20Agreement/Forwards%20and%20Futures%20Notes.md) is equal to the cost or profit of closing the contract,   which,   if taken at time ( t ),   can be expressed as: $f_{t,  T} = (K - F_{t,  T}) \times e^{-r_{\text{USD}}(T-t)} \times N$ where $K$ is the delivery price set at contract initiation and $N$ is the notional amount of the foreign [currency](../Teaching%20Note%201-%20Forward%20Rates%20Agreement/Forwards%20and%20Futures%20Notes.md).

- So,   to find the value of a [forward contract](../../../Clippings/Forward%20Points%20in%20Currency.md) to buy (a [long forward](.md) contract),   if it is between the start and the maturity date,   you use the last equation with $K = F_{0,  T}$,   which represents the agreed [forward rate](../../../Clippings/Forward%20Points%20in%20Currency.md) at initiation: $$f_{t,  T} = (F_{0,  T} - F_{t,  T}) \times e^{-r_{\text{USD}}(T-t)} \times N$$
- This is the present value of the profit or loss from a [forward contract](../../../Clippings/Forward%20Points%20in%20Currency.md) from the perspective of the holder of a [long position](../../../Financial%20Engineering/Derivatives/Part%20I%20-%20Forwards%20and%20Futures/Chapter%204%20-%20Futures:%20Hedging%20and%20Speculation.md) in that contract. 
- It accounts for how much the holder stands to gain or lose from the contract's current value compared to what was initially locked in at $t=0$.

---
##  EXAMPLE 1: THE FORWARD PRICE OF A STOCK WITH KNOWN DIVIDEND PAYMENT
- Consider a stock with price $S_0$ which pays a known dividend at time $T_1 < T$.
- The [pricing](../../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%207/Arbitrage%20Pricing%20of%20Derivatives.md) formula $F_{0,  T} = (S_0 - PV(D)) e^{rT}$.
- **[Arbitrage](../../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%207/Arbitrage%20Pricing%20of%20Derivatives.md) argument**: What if $F_{0,  T} > (S_0 - PV(D)) e^{rT}$
## ARBITRAGEUR:
- At time 0:
  1. [Short forward](.md) $F_{0,  T}$;
  2. Borrow $(S_0 - PV(D))$ with maturity $T$ and $PV(D)$ with maturity $T_1$;
  3. Use total $S_0$ to buy stock.
- At time $T_1$
  * Receive dividend $D$ from stock. Use it to repay $PV(D)$ loan at $T_1$.
- At time $T$:
  1. Receive $F_{0,  T}$ from sale of stock (which is covered,   because of (c) above);
  2. Repay the loan $(S_0 - PV(D))e^{rT}$
**Payoff at $T$**: $$F_{0,  T} - (S_0 - PV(D))e^{rT} > 0$$
---

## EXAMPLE 2: THE FORWARD PRICE OF A STOCK WITH CONSTANT DIVIDEND YIELD
- **Dividend Yield** = Stock’s payoff per unit of [stock price](../../../Financial%20Engineering/Derivatives/Part%20IV%20-%20Options/Chapter%2016%20-%20Black–Scholes%20Model.md) = $D/S_t$
- Continuously compounded dividend yield $q$
  - $\Rightarrow$ Total dividend in a small interval $[t,   t + dt]$ is $D_t = q \times S_t \times dt$
- [Forward price](../../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%2011/Forward%20Contracts%20and%20Forward%20Prices.md): $F_{0,  T} = S_0 \times e^{-(r-q)T}$
- **What if** $F_{0,  T} > S_0 \times e^{-(r-q)T}$?
  1. [Short Forward](.md) at $F_{0,  T}$
  2. Borrow $S_0 \times e^{-rT}$ and buy $N_0 = e^{-qT} < 1$ shares.
  3. For every $t$ reinvest the dividends in the stock.
     - Change in number of shares in a small interval $dt$: $$(N_{t+dt} - N_t) = N_t \times \frac{D_t}{S_t}$$,   $N_t \times q \times dt$
     - Total number of shares between 0 and $T$: $$N_T = N_0 \times e^{qT} = e^{-qT} \times e^{qT} = 1$$
- The arbitrageur has exactly the right amount of shares to cover the [short forward](.md) position.
**Payoff at $T$**: $$F_{0,  T} - S_0 \times e^{-(r-q)T} > 0$$

---

### COVERED INTEREST RATE PARITY VIOLATION DURING THE 2007 - 2009 FINANCIAL CRISIS
- Sometimes,   arbitrageurs fail to keep markets together.
- The 2007 - 2009 provides a simple example.
- Define the discrepancy between forward and the “theoretical” [forward rate](../../../Clippings/Forward%20Points%20in%20Currency.md) as:
**Basis** = Traded [Forward Rate](../../../Clippings/Forward%20Points%20in%20Currency.md) – Theoretical [Forward Rate](../../../Clippings/Forward%20Points%20in%20Currency.md) $$= \frac{F_{traded} - F_{L,  t+m}}{F_{L,  t+m}}$$
where $m$ = maturity (e.g.,   3 months,   6 months etc.),   and recall $$F_{L,  t+m} = S_t e^{(r_s-r_e)m}$$
- The latter relation is also called "[Covered Interest Rate Parity](../../Financial%20Instruments%20PSET%20Solutions.md)" (CIP)
- If Basis above is not close to zero,   we say that there is a violation of the [covered interest rate parity](../../Financial%20Instruments%20PSET%20Solutions.md).

---
### WHY DID COVERED INTEREST RATE PARITY FAIL DURING THE 2007-2009 CRISIS?
- Holding [US Treasuries](../../../Credit%20Markets/Credit%20Market%20PSETS/Credit%20Market%20Homework%201.md) has its own “convenience yield” when everyone needs cash collateral.
- During the crisis,   from the graph,   we had the basis being positive. That is: $$F_{data,  L,  t+m} > F_{L,  t+m} = M_t e^{(r_s-r_e)m}$$
- Recall that in this case,   an [arbitrage trade](../../Assignments/Solutions/PSET%201%20Solution-Financial%20Instruments.md) requires the following:
  1. [Short forward](.md);
  2. Borrow dollars (or sell [US Treasuries](../../../Credit%20Markets/Credit%20Market%20PSETS/Credit%20Market%20Homework%201.md));
  3. Change them into Euro;
  4. Invest in Euro (or buy Euro bonds)
- But point (b) failed during the crisis,   as:
  1. Increase in [credit risk](../../../Course%20Notes/Quantitative%20Trading%20Strategies%20Lecture%20Notes.md) concerns impaired the ability of [financial institutions](../../../Financial%20Markets%20and%20Institutions/Financial%20Markets%20and%20Institutions%20Lecture%20Notes.md) to borrow;
  2. Holding safe dollars ([US Treasuries](../../../Credit%20Markets/Credit%20Market%20PSETS/Credit%20Market%20Homework%201.md)) is valuable during a [financial crisis](../../../Financial%20Markets%20and%20Institutions/III.%20Liquidity%20of%20Assets/Class%209-%20Bailouts%20and%20Bank%20Failures/Squam%20Lake%20Group%20Letter.md) for [Liquidity](Class%20Note%2010%20[[Class%20Note%2010%20Liquidity%20and%20Class%20Note%2010%20Liquidity%20and%20Liquidity%20Managementliquidity%20management) and [Liquidity Management](../../../Financial%20Markets%20and%20Institutions/III.%20Liquidity%20of%20Assets/Class%207-%20CP,%20Repo,%20and%20the%20Crisis/Class%20Slides%20Effects%20of%20MMF%20Regulations%20in%20the%20United%20States.md)|[liquidity management](../../../Financial%20Markets%20and%20Institutions/III.%20Liquidity%20of%20Assets/Class%207-%20CP,%20Repo,%20and%20the%20Crisis/Class%20Slides%20Effects%20of%20MMF%20Regulations%20in%20the%20United%20States.md)]]
     - [US Treasuries](../../../Credit%20Markets/Credit%20Market%20PSETS/Credit%20Market%20Homework%201.md) are the only collateral accepted for short-term lending transactions.
     - It is very valuable to hold on to them for future cash management

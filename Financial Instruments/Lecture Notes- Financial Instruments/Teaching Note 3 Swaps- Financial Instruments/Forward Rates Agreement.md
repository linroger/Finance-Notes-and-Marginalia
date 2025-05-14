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

[Deriving [[A Primer on Currency Derivatives|Forward Exchange Rate]] Numerical Example 1](Deriving%20Forward%20Exchange%20Rate%20Numerical%20Example%201.md)

[Foreign Exchange Quoting Conventions](Foreign%20Exchange%20Quoting%20Conventions.md)

[[[Interest Rate Quotations|Interest Rates]],  Carry Trades,  and Exchange Rate Movements](Asset%20Classes/[[Chapter 9 Arbitrage and Hedging With Options|Derivatives]]/Forward%20and%20Futures/Forward%20Exchange%20Rate%20Contracts/Foreign%20Exchange%20Notes/Interest%20Rates,  %20Carry%20Trades,  %20and%20Exchange%20Rate%20Movements.md)

[Forward Contracts on Exchange Rates](Forward%20Contracts%20on%20Exchange%20Rates.md)

**[[Teaching Note 3 SwapsFinancial Instruments]]**
	- [[Forward Rates Agreement]]
	- [[Overnight Index Swaps (OIS)]]
	- [[Swaps Types]]
	- [[Teaching Note 3 SwapsFinancial Instruments]]
	- [[The Value of the [[Currency Swaps|Swap Contract]] after Initiation]]
### NO ARBITRAGE PRINCIPLE
- An [[Arbitrage Pricing of Derivatives|Arbitrage]] Opportunity is a trading strategy that either
	1. Costs nothing today and yields a positive profit in the future; or
	1. Yields a positive profit today,  and zero cash in the future.
- In well functioning markets,  no [[Class Note 13 The LTCM Meltdown|arbitrage opportunities]] may arise.
	- If there were,  arbitrageurs would take massive positions to profit from them,  equilibrating the market.
- The value of [[Financial Mathematics Course|derivative securities]],  including [[Forwards and Futures|forwards]],  [[Futures Not Subject to Cash-And-Carry|futures]],  swaps and options,  are determined by assuming that no [[Class Note 13 The LTCM Meltdown|arbitrage opportunities]] exist.

---
### THE LAW OF ONE PRICE

Securities with identical payoffs must have the same price.

- Otherwise,  an [[Class Note 13 The LTCM Meltdown|arbitrage opportunities]] arises
	- Buy Cheap / Sell Dear
- Buy the low-priced security and sell the high-priced one.
- At maturity the arbitrageur is hedged,  since the cash flows are the same.

## FORWARD CONTRACTS
- A [[Forward Points in Currency|Forward contract]] is an agreement between two counterparties to buy or sell a prespecified amount of goods or securities at a prespecified future date$T$at a prespecified price$F$
 - It does not cost anything to enter into a [[Forward Points in Currency|forward contract]] at time 0
	 - The contract is about exchanging goods (or securities) for money in the future,  and not today.
 - The prespecified price$F$moves to ensure that the value of the [[Forward Points in Currency|forward contract]] is zero for both counterparties at the inception of the contract.
- Let$N$be the size of the contract and${} S_t$the price of the good or security at$t$.

-The Profit/Loss at$T$are$$\text{P/L counterpary long the forward} =N\times(S_T-F)$$$$\text{P/L counterpary short the forward} =N\times(F-S_T)$$

- For instance,  the party long the forward agrees to buy at$T$a security for$F$when its value is$S_T$
	- If$S_T> F$,  it makes a profit (it pays only$F$instead of$S_T)$
	- If$S_T< F$,  it makes a loss (it pays$F$instead of the cheaper${} S_T)$
- On the other hand,  the party short the forward agrees to sell at$T$a security for$F$when its value is${} S_T$
	 - If$S_T< F$,  it makes a profit (they receive higher price$F$above prevailing market price of$S_T)$
	 - If$S_T> F$,  it makes a loss (they receive a price$F$below the market price${} S_T)$

[[Forward Rates Agreement|Long forward]] exchange rate: At maturity,  purchase foreign [[Forwards and Futures Notes|currency]] and pay with home [[Forwards and Futures Notes|currency]]

[[Forward Contracts on Exchange Rates|Short forward contract]]: At maturity,  purchase home [[Forwards and Futures Notes|currency]] and pay with foreign [[Forwards and Futures Notes|currency]]

***[[Forward Points in Currency|Forward contract]] to exchange foreign [[Forwards and Futures Notes|currency]] for home [[Forwards and Futures Notes|currency]]
- [[Forward Points in Currency|Forward contract]] to exchange EUR for USD
- [[Arbitrage Opportunity Accounting|Spot Exchange Rate]]:$S_{0} \frac{USD}{EUR}$
- [[Forward Points in Currency|Forward Rate]]:$F_{0,  T} \frac{USD}{EUR}$
- US Interest Rate:$r_{USD}$
- EUR Interest Rate:$r_{EUR}$

***[[Arbitrage Pricing of Derivatives|Pricing]] of [[A Primer on Currency Derivatives|Forward Exchange Rate]] Contracts
- Consider a US Investor with USD N to invest for 1 year. The Investor has 2 options to invest.
1. **Strategy A**
	1. Deposit N at at$r_{USD}$yielding at maturity T:$$\text{Payoff}_{A}=Ne^{(r_{USD})*T}$$
1. **Strategy B**
	1. Exchange USD N into EUR$\frac{N}{S_{0}}$
	1. Invest EUR$\frac{N}{S_{0}}$at$r_{EUR}$yielding at maturity T:$$\text{Payoff}_{B}= \left(\frac{N}{S_{0}}\right)e^{(r_{EUR})*T}$$
	1. Enter into a [[Forward Points in Currency|forward contract]] to buy dollars,  paying euros at [[Forward Points in Currency|forward rate]]$F_{0,  T}$([[Forward Rates Agreement|Short forward]]).$$\text{Dollars recieved }= F_{0,  T}* \left(\frac{N}{S_{0}}\right)e^{(r_{EUR})*T}$$
1. Under no [[Arbitrage Pricing of Derivatives|arbitrage]],  the payoffs to the two strategies must be equal.$$F_{0,  T}* \left(\frac{N}{S_{0}}\right)e^{(r_{EUR})*T} = Ne^{(r_{USD})*T}$$
1. Solving for$F_{0,  T}$,  $$F_{0,  T}=S_{0}e^{(r_{USD}-r_{EUR})*T}$$

---

#### ARBITRAGE STRATEGY WHEN $F_{0,  T} > S_0 \times e^{(R_S-R_E) \times T}$

ie. quoted [[Forward Points in Currency|forward contract]] is overvalued.

Short [[Forwards and Futures|forwards]] contract by paying euros and accepting dollars

1. **Enter a [[Forward Points in Currency|forward contract]] to sell$N$euros at the [[Forward Points in Currency|forward rate]]$F_{0,  T}$:**
	   Commit to sell euros in the future at the currently quoted [[Forward Points in Currency|forward rate]].
	   This is equivalent to [[Short Selling|shorting]] the forward.
1. **Borrow$N \times e^{-r_e \times T} \times M_0$dollars and use it to buy$N \times e^{-r_e \times T}$euros:**
	   Take a loan in dollars now,  which will be repaid by the proceeds of selling euros at the [[Forward Points in Currency|forward rate]].
	   Convert the borrowed dollars to euros at the current [[The Foreign Exchange Market Annotations|spot rate]].
1. **Invest$N \times e^{-r_e \times T}$euros at the euro interest rate$r_e$until$T$:**
	   Invest the euros at the Euro [[A Guide to the Front End and [[Basis Swaps|Basis Swap]] Markets#[[Short-Term Rates and the Transition from LIBOR|London Interbank Offered Rate]] (LIBOR)|LIBOR]] rate,  expecting them to grow back to$N$euros over time$T$.
### AT MATURITY $T$
- **Receive$\$F_{0,  T} \times N$from the forward sale of euros:**
   - This is the dollar amount you get from selling$N$euros at the [[Forward Points in Currency|forward rate]].
- **Pay back the dollar loan of$\$(N \times e^{-r_e \times T} \times M_0) \times e^{r_s \times T}$:**
   - Repay the dollar loan which has grown to this amount with the US interest rate over time$T$.

- **The dollar profit at$T$is:**$$N \times (F_{0,  T} - M_0 \times e^{(r_s-r_e) \times T})$$

  1. [[Forward Contracts on Exchange Rates|Short forward contract]] (sell euros,  buy dollars)
  1. Borrow dollars
  1. Buy euro
  1. Invest in euro deposits
At maturity,
1. Collect [[Assets|returns]] from euro deposits
1. Deliver euros and receive dollars
1. Pay back loan obligation

### ARBITRAGE STRATEGY WHEN $F_{0,  T} < M_0 \times E^{(R_S-R_E) \times T}$
1. **Enter into a [[Forward Points in Currency|forward contract]] to buy$N$euros at [[Forward Points in Currency|forward rate]]$F_{0,  T}$:**
	- This step locks in the price at which you will buy euros in the future.

1. **Borrow$N \times e^{-r_e \times T}$euros:**
	- Borrow euros now at the current Euro [[A Guide to the Front End and [[Basis Swaps|Basis Swap]] Markets#[[Short-Term Rates and the Transition from LIBOR|London Interbank Offered Rate]] (LIBOR)|LIBOR]] rate,  and you will need to pay back the borrowed amount multiplied by the exponential of the negative Euro interest rate times the [[Hedging Strategies with Forwards|time to maturity]]$T$.

1. **Exchange them to$N \times e^{-r_e \times T} \times M_0$dollars:**
	- Convert the borrowed euros to dollars at the current [[The Foreign Exchange Market Annotations|spot rate]].

1. **Invest$N \times e^{-r_e \times T} \times M_0$dollars at the dollar interest rate$r_s$:**
	- Invest the dollar amount at the current US [[A Guide to the Front End and [[Basis Swaps|Basis Swap]] Markets#[[Short-Term Rates and the Transition from LIBOR|London Interbank Offered Rate]] (LIBOR)|LIBOR]] rate,  and the [[An Asset Allocation Primer|investment]] will grow according to the dollar interest rate over the [[Hedging Strategies with Forwards|time to maturity]]$T$.

1. **At maturity$T$,  the arbitrageur:**
	- Receives$N$euros from the [[Forward Points in Currency|forward contract]] and pays$F_{0,  T} \times N$dollars for them.
	- Pays back the euro loan of$N \times e^{-r_e \times T}$euros,  which has grown to$N$euros by$T$.
	- Receives proceeds from the dollar [[An Asset Allocation Primer|investment]],  which is the invested amount multiplied by the exponential of the dollar interest rate times$T$.

1. **Dollar Profit at$T$:**
	- The profit is calculated as the proceeds from the dollar [[An Asset Allocation Primer|investment]] minus the cost of buying euros in the [[Forward Points in Currency|forward contract]].

1. [[Forward Rates Agreement|Long forward]] (buy euros,  pay dollars)
1. Borrow euros
1. Convert to dollars
1. invest in dollars deposits
At maturity,
1. Collect [[Assets|returns]] from dollar deposits
1. Pay dollars to forward counterparty
1. Collect euros
1. Use euros to pay back euro loan
---

### TABLE 1: OVERVALUED FORWARD RATE
- In this scenario,  the arbitrageur believes that the [[Forward Points in Currency|forward rate]] for buying euros is overvalued,  meaning that the market's [[Forward Points in Currency|forward rate]] is higher than what it should be based on [[What Really Is the Cross-Currency Basis|interest rate differentials]].

| Trade | Payoff |
| --- | --- |
| Enter a [[Forward Points in Currency|forward contract]] to sell euros at the overvalued [[Forward Points in Currency|forward rate]] $F_{0,  T}$ | 0 |
| Borrow euros at the current [[The Foreign Exchange Market Annotations|spot rate]] $M_0$ | $-N \times e^{-r_e \times T}$ |
| Convert borrowed euros to dollars at [[The Foreign Exchange Market Annotations|spot rate]] $M_0$ | $N \times e^{-r_e \times T} \times M_0$ |
| Invest the dollar amount at the US interest rate $r_s$ | $N \times e^{-r_e \times T} \times M_0 \times e^{r_s \times T}$ |
| At maturity $T$,   fulfill the [[Forward Points in Currency|forward contract]] | $-N \times F_{0,  T}$ |
| Pay back the euro loan | $N$ |
| **Net Profit/Loss at $T$** | $N \times (e^{-r_e \times T} \times M_0 \times e^{r_s \times T} - F_{0,  T})$ |

### TABLE 2: UNDERVALUED FORWARD RATE
- In this scenario,  the arbitrageur believes that the [[Forward Points in Currency|forward rate]] for buying euros is undervalued,  meaning that the market's [[Forward Points in Currency|forward rate]] is lower than what it should be based on [[What Really Is the Cross-Currency Basis|interest rate differentials]].

| Trade | Payoff |
| --- | --- |
| Enter a [[Forward Points in Currency|forward contract]] to buy euros at the undervalued [[Forward Points in Currency|forward rate]] $F_{0,  T}$ | 0 |
| Borrow dollars at the current [[The Foreign Exchange Market Annotations|spot rate]] $M_0$ | $-N \times e^{-r_s \times T} \times M_0$ |
| Convert borrowed dollars to euros at [[The Foreign Exchange Market Annotations|spot rate]]$M_0$|$N \times e^{-r_s \times T}$|
| Invest the euro amount at the Euro interest rate$r_e$|$N \times e^{-r_s \times T} \times e^{r_e \times T}$|
| At maturity$T$,   fulfill the [[Forward Points in Currency|forward contract]] |$N \times F_{0,  T}$|
| Pay back the dollar loan |$N \times e^{-r_s \times T} \times M_0 \times e^{r_s \times T}$|
| **Net Profit/Loss at$T$** |$N \times (F_{0,  T} - e^{-r_s \times T} \times M_0 \times e^{r_s \times T})$|

---

# Forward Rates Agreement

- The earlier derivation was obtained for [[Forward Contracts on Exchange Rates|currency forwards]].
- Similar derivations hold for other securities,  such as stocks,  bonds,  and [[Futures Not Subject to Cash-And-Carry|commodities]].
- Here is a list of "formulas". A good exercise is to go over the steps again.

| Security | [[Forward Contracts and Forward Prices|Forward Price]] |
|----------|---------------|

| [[Forwards and Futures Notes|Currency]] (e.g. dollar vs euro) |$$F_{0,  T} = M_0 \times e^{(r_s-r_e)T}$$|

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

- In all cases,  the value of a [[Forward Points in Currency|forward contract]] at time$t > 0$(after initiation) is:
$$f_{t,  T} = e^{-r(T-t)}[F_{0,  T} - F_{t,  T}]$$

1. Assume that at time t months the Euro appreciated from$S_{0}$to$S_{t}$,  with$S_0<S_t$
1. If the US firm wants to cancel the contract with the bank,  how much does it have to pay?

	- The US firm can enter into the reverse [[Forward Points in Currency|forward contract]] with the bank,  with payoff$$\text{Dollar payoff at$T$of reverse forward contract} = N × (S_{T} − F_{t,   T})$$Now:$$F_{t,  T} = S_t × e^{(r_{USD}−r_{EUR})×(T −t)}$$
	- The reverse contract neutralizes the former one.
- Payoff at$T$from forward + reverse forward$$= N\times (F_{0,  T}-S_T)+N \times(M_T-F_{t,  T})$$$$= N\times(F_{0,  T}- F_{t,   T})$$
- The US firm will have to pay the bank$N\times(F_{0,  T}- F_{t,   T})$at$T$
	- The Present Value of$N\times(F_{0,  T}- F_{t,   T})$is the value of the original [[Forward Points in Currency|forward contract]] to the US firm
$$
f_{t,  T}=e^{-r_{\$}\times(T-t)}\times(F_{0,  T}-F_{t,  T})\times N
$$

- Since it costs$e^{-r_{\$}\times(T-t)}\times(F_{0,  T}-F_{t,  T})\times N$to close the position,  the value of the [[Forward Points in Currency|forward contract]] to the firm must equal this amount.
	- Vice-versa,  the value to the bank must be$e^{-r_{\$}\times(T-t)}\times(F_{0,  T}-F_{t,  T})\times N$

> [!note]
> The above formula is general: The value of a [[Forward Points in Currency|forward contract]] to $sell$ euros at a prespecifled
>
> price $K$ is always given by $$f_{t,  T}=e^{-r_{\$}\times(T-t)}\times(K-F_{t,  T})$$

To summarize,  we found:

1. The Forward (Delivery) Price - the price decided at time 0 to buy / sell goods (Euros) in the future is given by$$
\begin{aligned}F_{0,  T}=S_0\times e^{(r_{\$}-r_e)T}\end{aligned}

$$
2. The value of an $existing$ [[Forward Points in Currency|forward contract]] to deliver goods (Euros) at preset price $K$ (determined some time in the past) is equal to the cost / profit of closing the contract: $$ f_{t,  T}=[K-F_{t,  T}]\times e^{-r_{\$}(T-t)}$$
- This is the value of [[Forward Points in Currency|forward contract]] to $sell$. 

- What is the value of a [[Forward Points in Currency|forward contract]] to buy (i.e. a [[Forward Rates Agreement|long forward]] contract?)

**Valuation of a [[Forward Rates Agreement|Long Forward]] Contract at Time $t$
Set Up the Current Value Notation
- Let $F_{0,  T}$ be the [[Forward Points in Currency|forward rate]] agreed upon at initiation for exchange at future time $T$.
- Let $F_{t,  T}$ be the [[Forward Points in Currency|forward rate]] at the intermediate time $t$ for the same exchange at time $T$.
- Let $S_t$ be the [[The Foreign Exchange Market Annotations|spot rate]] at the intermediate time $t$.
- Let $r$ be the domestic [[Exercises|risk-free interest rate]]; $r_{\text{USD}}$.
- Let $N$ be the notional amount of foreign [[Forwards and Futures Notes|currency]] (Euros in this context) to be exchanged.

**Determine the Payoff of the Original [[Forward Points in Currency|Forward Contract]]
- At maturity $T$,   the payoff to the [[Chapter 4 - Futures: Hedging and Speculation|long position]] in the original [[Forward Points in Currency|forward contract]] is $$N \times (S_T - F_{0,  T})$$
***Calculate the Reverse [[Forward Points in Currency|Forward Contract]]
- To exit the forward position,   the firm enters into a reverse [[Forward Points in Currency|forward contract]],   agreeing at time $t$ to sell Euros at the new [[Forward Points in Currency|forward rate]] $F_{t,  T}$.
- The payoff of the reverse contract at maturity $T$ is $N \times (F_{t,  T} - S_T)$.

***Combine Forward and Reverse Forward Payoffs
- The two payoffs $N \times (S_T - F_{0,  T})$ and $N \times (F_{t,  T} - S_T)$ offset each other.
- The net payoff from both contracts at $T$ is $N \times (F_{0,  T} - F_{t,  T})$.

***Calculate the Present Value at Time $t$
- The present value of the net payoff is the value of the original [[Forward Points in Currency|forward contract]] to the [[Chapter 4 - Futures: Hedging and Speculation|long position]]. 
- That value,   discounted back from $T$ to $t$,   is calculated as: $$f_{t,  T} = N \times (F_{0,  T} - F_{t,  T}) \times e^{-r \times (T - t)}$$
***Final Value of a [[Forward Rates Agreement|Long Forward]] Contract at Time $t$
- The value of the [[Forward Rates Agreement|long forward]] contract at time $t$ is therefore: $$f_{t,  T} = N \times (F_{0,  T} - F_{t,  T}) \times e^{-r_{\text{USD}} \times (T - t)}$$
This equation reflects the current value of the [[Forward Rates Agreement|long forward]] position: If $F_{0,  T} > F_{t,  T}$,   the value is positive,   indicating that the [[The Foreign Exchange Market Annotations|spot rate]] has moved favorably since the contract was initiated. Conversely,   if $F_{0,  T} < F_{t,  T}$,   the value is negative,   reflecting an unfavorable move in the [[The Foreign Exchange Market Annotations|spot rate]]. As you mentioned,   since it costs $f_{t,  T}$ to close the position (buy back the [[Forward Points in Currency|forward contract]]),   this must also be the value of the original [[Forward Points in Currency|forward contract]] from the perspective of the long (buy) side.

To summarize our findings:
- The Forward (Delivery) Price - The price determined at time 0 to buy or sell the foreign [[Forwards and Futures Notes|currency]] (Euros in this case) in the future is given by: $$F_{0,  T} = S_0 \times e^{(r_{\text{USD}} - r_{\text{EUR}})T}$$
- The Value of an Existing [[Forward Rates Agreement|Long Forward]] Contract - The value of a [[Forward Points in Currency|forward contract]] agreed upon in the past at a preset price for the future delivery of the foreign [[Forwards and Futures Notes|currency]] is equal to the cost or profit of closing the contract,   which,   if taken at time ( t ),   can be expressed as: $f_{t,  T} = (K - F_{t,  T}) \times e^{-r_{\text{USD}}(T-t)} \times N$ where $K$ is the delivery price set at contract initiation and $N$ is the notional amount of the foreign [[Forwards and Futures Notes|currency]].

- So,   to find the value of a [[Forward Points in Currency|forward contract]] to buy (a [[Forward Rates Agreement|long forward]] contract),   if it is between the start and the maturity date,   you use the last equation with $K = F_{0,  T}$,   which represents the agreed [[Forward Points in Currency|forward rate]] at initiation: $$f_{t,  T} = (F_{0,  T} - F_{t,  T}) \times e^{-r_{\text{USD}}(T-t)} \times N$$
- This is the present value of the profit or loss from a [[Forward Points in Currency|forward contract]] from the perspective of the holder of a [[Chapter 4 - Futures: Hedging and Speculation|long position]] in that contract. 
- It accounts for how much the holder stands to gain or lose from the contract's current value compared to what was initially locked in at $t=0$.

---
##  EXAMPLE 1: THE FORWARD PRICE OF A STOCK WITH KNOWN DIVIDEND PAYMENT
- Consider a stock with price $S_0$ which pays a known dividend at time $T_1 < T$.
- The [[Arbitrage Pricing of Derivatives|pricing]] formula $F_{0,  T} = (S_0 - PV(D)) e^{rT}$.
- **[[Arbitrage Pricing of Derivatives|Arbitrage]] argument**: What if $F_{0,  T} > (S_0 - PV(D)) e^{rT}$
## ARBITRAGEUR:
- At time 0:
  1. [[Forward Rates Agreement|Short forward]] $F_{0,  T}$;
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
- **Dividend Yield** = Stock’s payoff per unit of [[Chapter 16 - Black–Scholes Model|stock price]] = $D/S_t$
- Continuously compounded dividend yield $q$
  - $\Rightarrow$ Total dividend in a small interval $[t,   t + dt]$ is $D_t = q \times S_t \times dt$
- [[Forward Contracts and Forward Prices|Forward price]]: $F_{0,  T} = S_0 \times e^{-(r-q)T}$
- **What if** $F_{0,  T} > S_0 \times e^{-(r-q)T}$?
  1. [[Forward Rates Agreement|Short Forward]] at $F_{0,  T}$
  2. Borrow $S_0 \times e^{-rT}$ and buy $N_0 = e^{-qT} < 1$ shares.
  3. For every $t$ reinvest the dividends in the stock.
     - Change in number of shares in a small interval $dt$: $$(N_{t+dt} - N_t) = N_t \times \frac{D_t}{S_t}$$,   $N_t \times q \times dt$
     - Total number of shares between 0 and $T$: $$N_T = N_0 \times e^{qT} = e^{-qT} \times e^{qT} = 1$$
- The arbitrageur has exactly the right amount of shares to cover the [[Forward Rates Agreement|short forward]] position.
**Payoff at $T$**: $$F_{0,  T} - S_0 \times e^{-(r-q)T} > 0$$

---

### COVERED INTEREST RATE PARITY VIOLATION DURING THE 2007 - 2009 FINANCIAL CRISIS
- Sometimes,   arbitrageurs fail to keep markets together.
- The 2007 - 2009 provides a simple example.
- Define the discrepancy between forward and the “theoretical” [[Forward Points in Currency|forward rate]] as:
**Basis** = Traded [[Forward Points in Currency|Forward Rate]] – Theoretical [[Forward Points in Currency|Forward Rate]] $$= \frac{F_{traded} - F_{L,  t+m}}{F_{L,  t+m}}$$
where $m$ = maturity (e.g.,   3 months,   6 months etc.),   and recall $$F_{L,  t+m} = S_t e^{(r_s-r_e)m}$$
- The latter relation is also called "[[Financial Instruments PSET Solutions|Covered Interest Rate Parity]]" (CIP)
- If Basis above is not close to zero,   we say that there is a violation of the [[Financial Instruments PSET Solutions|covered interest rate parity]].

---
### WHY DID COVERED INTEREST RATE PARITY FAIL DURING THE 2007-2009 CRISIS?
- Holding [[Credit Market Homework 1|US Treasuries]] has its own “convenience yield” when everyone needs cash collateral.
- During the crisis,   from the graph,   we had the basis being positive. That is: $$F_{data,  L,  t+m} > F_{L,  t+m} = M_t e^{(r_s-r_e)m}$$
- Recall that in this case,   an [[PSET 1 Solution-Financial Instruments|arbitrage trade]] requires the following:
  1. [[Forward Rates Agreement|Short forward]];
  2. Borrow dollars (or sell [[Credit Market Homework 1|US Treasuries]]);
  3. Change them into Euro;
  4. Invest in Euro (or buy Euro bonds)
- But point (b) failed during the crisis,   as:
  1. Increase in [[Quantitative Trading Strategies Lecture Notes|credit risk]] concerns impaired the ability of [[Financial Markets and Institutions Lecture Notes|financial institutions]] to borrow;
  2. Holding safe dollars ([[Credit Market Homework 1|US Treasuries]]) is valuable during a [[Squam Lake Group Letter|financial crisis]] for [[Class Note 10 [[Class Note 10 Liquidity and Class Note 10 Liquidity and Liquidity Managementliquidity management|Liquidity]] and [[Class Slides Effects of MMF Regulations in the United States|Liquidity Management]]|[[Class Slides Effects of MMF Regulations in the United States|liquidity management]]]]
     - [[Credit Market Homework 1|US Treasuries]] are the only collateral accepted for short-term lending transactions.
     - It is very valuable to hold on to them for future cash management

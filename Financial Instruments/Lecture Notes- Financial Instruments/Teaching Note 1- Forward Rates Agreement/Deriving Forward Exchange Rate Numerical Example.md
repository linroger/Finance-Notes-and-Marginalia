---
title: Deriving Forward Exchange Rate Numerical Example
tags:
  - currency_depreciation
  - forward_exchange_rate
  - futures_contracts
  - hedging_strategy
  - mark_to_market
aliases:
  - FX Forward Example
  - Forward Rate Derivation
key_concepts:
  - European bank hedging
  - Forward exchange rate
  - Futures contract payoff
  - Hedging currency risk
  - Mark to market
---

# Deriving Forward Exchange Rate Numerical Example

Carry Trade](Carry%20Trade.md)
Currency Forward](Currency%20Forward.md)

- Introduction to Derivative Markets]]
- Hedging%20[Key%20Rates%20O1s%20Durations%20and%20Hedging) Strategies with [Forwards]]
- Forward Exchange Rate Numerical Example]]
- Secondary Commodities]]
- Foreign Exchange Quoting Conventions
- Forward Contracts on Exchange Rates
- Forwards and Futures Notes]]
- Hedging Strategies with Forwards]]
- Financial Instruments/Lecture Notes/Teaching Note 1- Forward Rates Agreement/Interest Rates,  Carry Trades,  and Exchange Rate Movements]]
- Teaching Note 1 Forward Rates Agreement

 | Exchange Rate | USD/EUR | 
 | ---- | ---- | 
 | Current Exchange Rate | $M_{0}=1.2673$ | 
 | Forward Exchange Rate | $F=1.28$ | 
 | US interest rate | $r_{USD} = 0.05$ | 
 | EUR interest rate | $r_{EUR}=0.03$ | 

[^1]: A US firm has sold a piece of equipment to a German client. German firm will pay EUR 5 million in T = 6 months
	- US Firm wants to hedge this receivable against EUR depreciation,  which will lessen the dollar amount of the receivable it is due to collect.
	- US firm can implement a hedge to pay EUR and receive USD at maturity,  at a forward exchange rate determined today.
		- Hedging Strategy
			- US Firm will pay EUR 5 million and receive
			- EUR 5 million and receive$$\text{EUR } 5, 000, 000 * 1.28=  \$6, 400, 000$$
		- Total Payoff to US Firm$$5, 000, 000*M_{T}+5, 000, 000(F-M_{T})$$
$$(5, 000, 000*1.2673)+[5, 000, 000(1.28-1.2673)]= \$6, 400, 000  ⚡$$

[^1]: European Bank hedges its commitment to receive EUR in exchange for USD
[^1]: Borrow PV of EUR 5 million at$r_{e}=0.03$$$\text{EUR }5000000e^{\left(-0.03\times 0.5\right)}= \text{EUR }4925559.698$$
[^1]: Exchange EUR 4925559.698 into USD today at spot exchange rate$$\text{EUR }4925559.698 * 1.2673 \frac{\text{USD}}{\text{EUR}}= \text{USD } 6242161.81$$
[^1]: Invest this amount in dollar deposits at$r_{USD}=0.05$$$\text{USD } 6242161.81e^{0.05*\frac{1}{2}}=6400182.88$$
[^1]: Today,  the bank nets 0
[^1]: At time T,  the bank:
[^1]: Receives 5 mil euros from the US firm (from fwd contract).
[^1]: Uses this money to close the 5 mil euro loan.
[^1]: Cashes in the dollar investment:$$\text{USD } 6242161.81e^{0.05*\frac{1}{2}}=6400182.88$$
[^1]: Gives this money to the client

		- Effective exchange rate:$$F=\frac{\text{USD 6400182.88}}{\text{EUR } 5000000}= 1.28004$$

[^1]: Assume that at time t = 3 months the Euro appreciated from$M_{0}$= 1.2673 to$M_{t}$= 1.29
	- If the US firm wants to cancel the contract with the bank,  how much does it have to pay?
	- The US firm can enter into the reverse forward contract with the bank,  with payoff$$\text{Dollar payoff at$T$of reverse forward contract} = 5, 000, 000 × (M_{T} − F_{t,  T})$$Now:$$F_{t, T} = M_t × e^{(r_USD−r_EUR)×(T −t)} = 1.29 × e^{(0.05−0.03)×0.25} = 1.296 \$/EUR$$
	- The reverse contract neutralizes the former one.
- Payoff at$T$from forward + reverse forward$$= 5000000\times (F_{0, T}-S_T)+5000000 \times(M_T-F_{t, T})$$$$=$5000000\times(F_{0, T}- F_{t,  T})$$$$=$5000000$\times (1.281.296) = - \$80, 000$$
- The US firm will have to pay the bank$80, 000 at$T$
	- The Present Value of$-\$80, 000$is the value of the original forward contract to the US firm
$$
f_{t, T}=e^{-r_{\$}\times(T-t)}\times(F_{0, T}-F_{t, T})\times5\text{ mil}=-\$79, 006.2
$$

- Since it costs$\$79, 006.2$to close the position,  the value of the forward contract to the firm must equal this amount.
	- Vice-versa,  the value to the bank must be \$79, 006.20

> [!note]
> The above formula is general: The value of a forward contract to $sell$ euros at a prespecifled
>
> price $K$ is always given by $$f_{t, T}=e^{-r_{\$}\times(T-t)}\times(K-F_{t, T})$$

To summarize,  we found:

[^1]: The Forward (Delivery) Price - the price decided at time 0 to buy / sell goods (Euros) in the future is given by$$
\begin{aligned}F_{0, T}=M_0\times e^{(r_{\$}-r_e)T}\end{aligned}

$$
[^2]: The value of an $existing$ forward contract to deliver goods (Euros) at preset price $K$ (determined some time in the past) is equal to the cost / profit of closing the contract: $$ f_{t, T}=[K-F_{t, T}]\times e^{-r_{\$}(T-t)}$$
- This is the value of forward contract to $sell$. 

- What is the value of a forward contract to buy (i.e. a long forward contract?)

· Important Note: The value of a forward contract at inception $t=0$ is zero.
- The Forward delivery price $K=F_{0, T}$,  which makes $f_{0, T}=0.$
* When two counterparties enter into a forward contract,  they do not exchange any money 
* In fact, they agree to exchange money only in the future,  depending on $M_T$

· Finally,  an equivalent formula is obtained by substituting $F_{t, T}$$$

f_{t, T}=Ke^{-r_{\$}(T-t)}-M_te^{-r_{e}(T-t)}

$$

· The earlier derivation was obtained for currency forwards. · Similar derivations hold for other securities,  such as stocks,  bonds,  and commodities.

# EXAMPLE: HEDGING WITH FUTURES

Consider earlier example: The US firm could hedge with futures contracts instead of forwards.
- CME Euro FX Futures have size of 125, 000 Euro and expire on Mar,  Jun,  Sep,  and Dec.
- Suppose that $T =$ Mar 2007 and $F_{0, T} = 1.28$.
- US firm can short 5 mil/125, 000 $\approx$ 40 futures contracts.
- Every day $t$,  $$P/L_t = k \times 125, 000 \times (F_{1, T} - F_{t, T}) =5, 000, 000\times (F_{1, T} - F_{t, T})$$
- At maturity $T$: Payoff at $T = (P/L)_t + (P/L)_2 + ... + (P/L)_T$
  - $=5, 000, 000\times (F_{0, T} - F_{T, T})$
  - $=5, 000, 000\times (F_{0, T} - M_T)$
  - $=$ Payoff of Forward Contract at $T$ if  $F_{0, T} = F_{T, T}$

**Caveat**: The total payoff from using a constant number of contracts $k$ every period is actually not exactly equivalent to the one of a forward contract.
- Because of mark to market,  trading profits and losses accrue **over time** to the hedger.
- The correct statement of the payoff at $T$ is in fact:
  - Payoff at $T$ = $$(P/L)_1 \times e^{-r(T-t)} + (P/L)_2 \times e^{-r(T-t2)} + ... + (P/L)_T \times e^{-r(T-T)}$$
  - where $dt = 1/365 = 1$ day (in annual units)

To obtain the forward contract's payoff,  we must **tail the hedge** and choose the number of contracts $k$ per period as $$k = 40 \times e^{-r(T-t1)}$,  
$k = 40 \times e^{-r(T-t2)}$,  ...,  $k = 40 \times e^{-r(T-t_{T-1})}$,  $k_{T-1} = 40$$
- which yields the payoff sequence at $T =5, 000, 000\times (F_{0, T} - F_{1, T}) \times e^{r(T-t1)} + 5, 000, 000\times (F_{1, T} - F_{2, T}) \times e^{r(T-t2)} + ... + 5, 000, 000\times (F_{T-1, T} - F_{T, T}) \times e^{r(T-T)}$
  - $=5, 000, 000\times (F_{0, T} - M_T)$

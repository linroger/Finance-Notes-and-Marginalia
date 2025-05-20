---
linter-yaml-title-alias: HEDGING WITH CURRENCY SWAPS
title: Teaching Note 3 SwapsFinancial Instruments
tags:
  - financial_instruments
  - forward_rates
  - fx_swap
  - interest_rate_swaps
  - no_arbitrage
aliases:
  - FX Swap
  - Forward Contracts
  - Swap Rate
  - Swaps
  - Teaching Note 3
key_concepts:
  - 'FX swap: currency exchange'
  - 'Forward rates: cash flow'
  - Interest rate swaps
  - No arbitrage condition
  - 'Swap rate: zero value'
---

Teaching Note 2-Futures Contracts
**Teaching Note 1Forward Rates Agreement**
 Teaching Note 2-Futures Contracts
 **Teaching Note 3 SwapsFinancial Instruments**
 **Teaching Note 4-Multiperiod Binomial Trees**
 Teaching Note 5Black Scholes Formula
 Teaching Note 6-Implied Volatility
 Teaching Note 7- Exotic Options  And Derivative Pricing By Monte Carlo Simulation]]
 Teaching Note 8 American Options
 Teaching Notes 9Corporate Securities And Credit Derivatives
 Teaching Notes 9ACredit Default Swaps
 Teaching Notes 10Interest Rate Derivatives

PSET 3 Financial Instruments

Swaps-Financial Instruments
Overnight Index Swaps (OIS).md)

%% Begin Waypoint %%
- **Teaching Note 3 Swaps- Financial Instruments**
	- Forward Rates Agreement
	- Overnight Index Swaps (OIS).md)
	- Swaps Types
	- Teaching Note 3 Swaps- Financial Instruments
	- The Value of the Swap Contract after Initiation

%% End Waypoint %%

# Teaching Note 3 Swaps- Financial Instruments
## OVERVIEW
- Back to the example,  assume the US firm is due to receive the 5 mil euros in 5 equal installments,  every 6 months.
- The US company can enter into five forward (or futures) contracts,  and hedge each single installment as a stand-alone cash flow.$$S_0 = 1.2673,  \ r_{USD} = 5\%,  \ r_{EUR} = 3\%$$

imply the following forward rates

### FORWARD RATES

 | Maturity$T$ | Forward Rate$F_{0, T}$ | 
 | --- | --- | 
 | 0.5 | 1.28 | 
 | 1 | 1.2929 | 
 | 1.5 | 1.3059 | 
 | 2 | 1.3190 | 
 | 2.5 | 1.3323 | 

- For each cash flow,  same arguments as above hold.
Alternatively,  the US firm can also enter into a FX swap:
- A FX swap is a contractual agreement between two counterparties to exchange prespecified amounts of moneys denominated in different currencies.

## FX SWAP CONTRACT DETAILS
- For instance,  the swap contract between the US firm and a bank may be specified as follows:
  1. US firm pays Bank 1 mil euros on every date$T =0.\1,  1,  …,  2.5$;
  2. Bank pays US firm 1 mil$\times K$,  say 1.306 mil,  dollar on the same dates.

### CASH FLOW IN SWAPS
- What is the net cash flow from the swap at any payment date?
  - We need to express cash flows in the same currency.

  - Every$T$,  the firm receives 1 mil$\times K$dollars,  and must pay 1 mil$\times S_T$dollars.$$\text{Net } \$CF \text{ at } T = 1 \ mil \times (K - S_T)$$

Alternatively,  the US firm can also enter into a FX swap:

- A FX swap is a contractual agreement between two counterparties to exchange prespecified amounts of moneys denominated in different currencies.
- For instance,  the swap contract between the US firm and a bank may be specified as follows:
  1. US firm pays Bank 1, 000, 000 euros on every date$T =0.\1,  1,  …,  2.5$;
  1. Bank pays US firm 1, 000, 000 x$K$,  say 1.306 million dollars on the same dates.

What is the net cash flow for the firm from the swap at any payment date?

- We need to express cash flows in the same currency.
- Every$T$,  the firm receives 1, 000, 000 x$K$dollars and must pay 1, 000, 000 x$M_T$dollars.
  - Net$\text{CF}$at$T = 1$million x$(K - M_T)$
## DETERMINING THE SWAP RATE

### HOW IS THE SWAP RATE $K = 1.306$ DETERMINED?
- The **Swap Rate$K$** is chosen at time 0 so that the **Value of the swap is equal to zero**. 
	- $\Rightarrow$no exchange of money at inception but only in the future.
### VALUING A SWAP
- How can we determine the value of a swap?
  - Let’s use the same methodology we used to value forwards,  that is,  let’s find how much would the firm pay to get out of the position.
#### NO ARBITRAGE CONDITION
- No arbitrage condition: Suppose the firm wants to close the swap exposure by using a sequence of forwards.
#### SWAP PAYOFF

- The payoff for every$T = 0.5,  …,  2.5$is$$\text{Payoff at } T \text{ of swap + reverse forward } = 1 \ mil \times (K - S_T) + 1 \ mil \times (S_T - F_{0, T})$$
- The Present Value of these sequence of net payments is$$PV \text{ of swap + reverse forward cash flows } = e^{-r_{USD} \times 0.5} \times 1 \ mil \times (K - F_{0, 0.5}) + e^{r_{USD} \times 1} \times 1 \ mil \times (K - F_{0, 1}) + … + e^{-r_{USD} \times 2.5} \times 1 \ mil \times (K - F_{0, 2.5})$$
- No arbitrage$\Rightarrow$At time 0,  the PV of swap + reverse forwards cash flows = 0
  - Why?$K$and$F_{0, T}$are chosen so that it costs nothing to enter into a swap or forward.
  - If PV of these cash flows$\neq 0$,  infinite profits are available.
#### SOLVING FOR$K$
- We obtain one equation in one unknown$K$$$0 = e^{-r_{USD} \times 0.5} \times 1 \ mil \times (K - F_{0, 0.5}) + e^{r_{USD} \times 1} \times 1 \ mil \times (K - F_{0, 1}) + … + e^{-r_{USD} \times 2.5} \times 1 \ mil \times (K - F_{0, 2.5})$$
- The solution to the equation is a weighted average of forward prices:$$\text{Currency Swap Rate} = K = w_{0.5}F_{0.5} + w_{1}F_{0, 1} + … + w_{2.5}F_{0, 2.5}$$
- The weights$w_T$are given by the relative time value of money across maturities$$w_T = \frac{e^{-r_{USD} \times T}}{e^{-r_{USD} \times 0.5} + e^{-r_{USD} \times 1} + … + e^{-r_{USD} \times 2.5}}$$
- We obtain an alternative (equivalent) formulation by substituting the forward prices$F_{0, T} = S_0(e^{-r_{EUR} \times T})$: $$\text{Currency Swap Rate} = K = \frac{S_0(e^{-r_{EUR} \times 0.5} + e^{-r_{EUR} \times 1} + … + e^{-r_{EUR} \times 2.5})}{e^{-r_{USD} \times 0.5} + e^{-r_{USD} \times 1} + … + e^{-r_{USD} \times 2.5}}$$

  - The FX Swap rate equals the current exchange rate multiplied by the ratio of the relative borrowing costs in the two currencies.

---

# HEDGING WITH SWAPS VERSUS FORWARDS

The payoff profile from the sequence of forwards and one swap is different:

[^1]: The sequence of forwards imply the US firms gets less money early on,  and more later on (from$1.28 mil to$1.3323 mil).
[^1]: The swap implies the firm gets a constant amount$1.306 mil every six months.
[^1]: !500
[^1]: Both strategies perfectly hedge the exposure,  as the exchange rate risk is eliminated and both payoff profiles are known at 0.

### OTHER TYPES OF SWAPS

The number of swaps that exist in the market is very large. • The most common are:

[^1]: Interest rate swaps
[^1]: One party pays a fixed coupon and the other party pays a floating rate.
[^1]: Plain vanilla IR swaps have floating rate given by LIBOR
[^1]: Energy swaps
[^1]: One party pays a fixed amount and the other party pays a floating amount linked to some energy index,  such as oil prices,  gas prices,  etc.
[^1]: Basis swaps
[^1]: Both parties make floating payments,  but linked to different indices,  such as [](../../../Fixed%20Income%20Asset%20Pricing/Fixed%20Income%20Lecture%20Notes/A%20Guide%20to%20the%20Front%20End%20and%20Basis%20Swap%20Markets.md#London%20Interbank%20Offered%20Rate%20(LIBOR) | LIBOR) versus Treasuries
[^1]: Total return swaps
[^1]: Both parties make floating payments,  linked to the total return of different securities.
[^1]: E.g. one party may pay the total return of Apple stock and the other the total return of Microsoft stock.
-----------------------------------------------------------------------------------

# THE VALUE OF THE SWAP CONTRACT AFTER INITIATION
## DETERMINING THE VALUE POST-INITIATION
- What is the value of a swap contract *after* initiation?
  - Let today be$t$, $K$be the swap rate of the existing swap,  and$T_1,  T_2,  …,  T_n$be the remaining payment periods.
  - Use the same logic as for forward and ask: What would the firm have to pay to get out of the position?
  - As before,  using a sequence of forwards to get out of the position gives

$$V^{swap}_t = PV \text{ of swap + reverse forward cash flows } = e^{-r_s(T_{1}-t)} \times (K - F_{1, T_1}) + e^{-r_s(T_{2}-t)} \times (K - F_{1, T_2}) + … + e^{-r_s(T_{n}-t)} \times (K - F_{1, T_n})$$

### OBTAINING THE SWAP VALUE FORMULA

- The swap value formula can be expressed as:$$V^{swap}_t = \sum_{i=1}^n e^{-r_s(T_{i}-t)} \times (K - F_{1, T_i})$$
  - By substituting the value of$F_{1, T_i}$with$S_t$times the discounted cash flow,  we get the equivalent formula:$$V^{swap}_t = K \times \left(\sum_{i=1}^n e^{-r_s(T_{i}-t)} \right) - S_t \times \left(\sum_{i=1}^n e^{-r_e(T_{i}-t)} \right)$$

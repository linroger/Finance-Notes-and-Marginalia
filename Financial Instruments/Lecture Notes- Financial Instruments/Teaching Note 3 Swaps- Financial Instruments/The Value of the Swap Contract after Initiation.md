---
tags:
- currency_swap
- derivatives-pricing
- eurodollar_futures
- fx-derivatives
- fx_swap
- interest-rate-derivatives
- interest_rate_risk
- markets
- risk-management
- swap_contract
aliases:
- Currency Swap
- Eurodollar Futures
- FX Swap
- Hedging Strategy
- Swap Value
key_concepts:
- Borrowing in foreign currency
- Delta hedging and Greeks calculation
- Eurodollar futures hedging
- Expected Shortfall (ES) and coherent risk measures
- Heath-Jarrow-Morton (HJM) framework
- Hedging principal amount
- Interest rate swaps and swap pricing
- Plain vanilla FX swaps
- Swap value formula
---


**Teaching Note 3 SwapsFinancial Instruments**
	- Forward Rates Agreement
	- Overnight Index Swaps (OIS).md)
	- Swaps Types
	- Teaching Note 3 SwapsFinancial Instruments
	- Swap Contract after Initiation]]

PSET 3 Financial Instruments

## DETERMINING THE VALUE POST-INITIATION
+ What is the value of a swap contract *after* initiation?
  + Let today be$t$,$K$be the swap rate of the existing swap, and$T_1, T_2, …, T_n$be the remaining payment periods.
  + Use the same logic as for forward and ask: What would the firm have to pay to get out of the position?
  + As before, using a sequence of forwards to get out of the position gives
$$V^{swap}_t = PV \text{ of swap + reverse forward cash flows } = e^{-r_s(T_{1}-t)} \times (K - F_{1,T_1}) + e^{-r_s(T_{2}-t)} \times (K - F_{1,T_2}) + … + e^{-r_s(T_{n}-t)} \times (K - F_{1,T_n})$$

### OBTAINING THE SWAP VALUE FORMULA

+ The swap value formula can be expressed as:$$V^{swap}_t = \sum_{i=1}^n e^{-r_s(T_{i}-t)} \times (K - F_{1,T_i})$$
  + By substituting the value of$F_{1,T_i}$with$S_t$$$V^{swap}*t = K \times \left(\sum*{i=1}^n e^{-r_s(T_{i}-t)} \right) - S_t \times \left(\sum_{i=1}^n e^{-r_e(T_{i}-t)} \right)$$

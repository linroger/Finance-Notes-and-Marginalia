---
title: Currency Swaps
tags:
  - currency_swaps
  - exchange_rate_risk
  - government_bonds
  - hedging
  - swap_contract
aliases:
  - FX swap
  - currency swap
key_concepts:
  - bond value
  - currency swap rates
  - exchange rate risk
  - government bonds
  - swap contract
---

# Currency Swaps

[Swaps-[[A Practical Guide for Actuaries and other Business Professionals.|Financial Instruments]]](Swaps-Financial%20Instruments)
[Lecture Note 3 Swaps- [[A Practical Guide for Actuaries and other Business Professionals.|Financial Instruments]]](Lecture%20Note%203%20Swaps-%20Financial%20Instruments.md)

## 1. DETERMINING CURRENCY SWAP RATES

### 1.1. PREAMBLE

1. Governments often issue bonds in foreign currencies (e.g.,  the Greek government issues Greek bonds denominated in USD rather than in EUR,  the home [[Forwards and Futures Notes|currency]]).
1. In issuing bonds in a foreign [[Forwards and Futures Notes|currency]],  a government exposes itself to [[PSET 3 Financial Instruments|exchange rate risk]]. If the foreign [[Forwards and Futures Notes|currency]] appreciates relative to the home [[Forwards and Futures Notes|currency]],  then more units of the home [[Forwards and Futures Notes|currency]] are required to pay the [[Notes on Currency Swaps|interest and principal]] in the foreign [[Forwards and Futures Notes|currency]].
1. [[Financial Instruments PSET Solutions|Currency swaps]] serve as a hedge against such [[PSET 3 Financial Instruments|exchange rate risk]].

### 1.2. CURRENCY SWAP

1. Consider two countries: Home H and Foreign F.
1. At inception$t = 0$,  Home issues government bonds with value$X$in [[Forwards and Futures Notes|currency]] F.
1. The bond pays a coupon (interest) semi-annually at the [[Continuously Compounding Interest|annual interest rate]]$c$.
1. To hedge against [[PSET 3 Financial Instruments|exchange rate risk]],  Home enters in a [[Currency Swaps|swap contract]].
1. Let$M_0$denote the exchange rate for F/H currencies at inception$t = 0$.
1. At inception$t = 0$,  the [[Currency Swaps|swap contract]] requires:
		a. Home pays$N_F = X$in F [[Forwards and Futures Notes|currency]].
		b. Home receives$N_H = X \cdot \frac{1}{M_0}$in H [[Forwards and Futures Notes|currency]].
1. At maturity$t = T$,  the [[Currency Swaps|swap contract]] requires:
		a. Home receives$N_F = X$in F [[Forwards and Futures Notes|currency]].
		b. Home pays$N_H = X \cdot \frac{1}{M_0}$in H [[Forwards and Futures Notes|currency]].

### 1.3. VALUE OF BONDS

1. Time$t = 0$value of the bond denominated in F [[Forwards and Futures Notes|currency]].$$B_0^F = \sum_{t=1}^T \frac{c}{2} \cdot N_F \cdot Z_F(0,  t)\text{ Interest PV} + N_F \cdot Z_F(0,  T)\text{ Principal PV}$$
1. Time$t = 0$value of the bond denominated in H [[Forwards and Futures Notes|currency]].$$B_0^H(K) = \sum_{t=1}^T \frac{K}{2} \cdot N_H \cdot Z_{H(0,  t)}\text{ Interest PV} + N_H \cdot Z_H(0,  T)\text{ Principal PV}$$

		-$K$denotes the "[[Teaching Note 4 Interest Rate Derivatives|swap rate]], " i.e. the annualized coupon rate for semi-annual payments of coupons in the H [[Forwards and Futures Notes|currency]].  
		- The bond value$B_0^H(K)$is a function of the [[Teaching Note 4 Interest Rate Derivatives|swap rate]]$K$.

### 1.4. SWAP RATE UNDER SPOT EXCHANGE OF PRINCIPAL

1. Time$t = 0$value of the swap in F [[Forwards and Futures Notes|currency]] is equal to the value of the [[Chapter 4 - Futures: Hedging and Speculation|long position]] in the bond denominated in the F [[Forwards and Futures Notes|currency]] minus the value of the short position in the bond denominated in the H [[Forwards and Futures Notes|currency]],  converted into the F [[Forwards and Futures Notes|currency]] using the time$t = 0$exchange rate$M_0$.$$V_{0, }^{\text{Swap,  }F}(K)=B_{0}^{F}-M_{0}\cdot B_{0}^{H}(K)+V_{0}^{\text{FX, }F}(\overline{M}_{0})$$
1. Value of exchange of principal.$$V_0^{\mathrm{FX, }F}(\bar{M}_0)=\left(\frac{M_0}{\overline{M}_0}-1\right)\cdot N^F$$
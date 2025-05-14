---
linter-yaml-title-alias: COVERED INTEREST RATE PARITY
title: COVERED INTEREST RATE PARITY
tags:
  - covered_interest_rate_parity
  - currency_security
  - exchange_rate
  - forward_rate
  - model_parameters
aliases:
  - CIRP
key_concepts:
  - Currency exchange
  - Exchange rate units
  - Forward rate
  - Home interest rate
  - Maturity time
---

[Teaching Note 1 Forward Rates Agreement](Teaching%20Note%201%20Forward%20Rates%20Agreement)
[Teaching Note 2-[[Mathematics of the Financial Markets|Futures Contracts]]](Teaching%20Note%202-[[Futures Not Subject to Cash-And-Carry|Futures]]%20Contracts.md)

[PSET 1-[[A Practical Guide for Actuaries and other Business Professionals.|Financial Instruments]]](PSET%201-Financial%20Instruments.md)
[1. Exploiting an Apparent [[Arbitrage Pricing of Derivatives|Arbitrage]] Opportunity](1.%20Exploiting%20an%20Apparent%20Arbitrage%20Opportunity.md)

# COVERED INTEREST RATE PARITY
## 1. MODEL PARAMETERS

There are four model parameters that collectively determine the [[Forward Points in Currency|forward rate]] for a [[Forwards and Futures Notes|currency]] security.

1. Home/[Foreign Exchange](Foreign%20Exchange%20Quoting%20Conventions.md) rate: $M$
2. Interest rate in home country: $r_\$$
3. Interest rate in foreign country: $r_\text{€}$
4. Maturity: $T$

The [[Interest Rate Quotations|interest rates]] $(r_\$, r_\text{€})$ are continuously compounded. The exchange rate $M$ denotes the number of units of the Home currency required to purchase one unit of the Foreign currency. For example, if $M = 1.2$, then 1.2 units of the Home [[Forwards and Futures Notes|currency]] (e.g., USD) are required to purchase one unit of the Foreign [[Forwards and Futures Notes|currency]] (e.g., EUR).

## 2. FORWARD RATE UNDER NO-AARBITRAGE

Determining the [[Forward Points in Currency|forward rate]] of a [[Forwards and Futures Notes|currency]] security requires appealing to a no-[[Arbitrage Pricing of Derivatives|arbitrage]] argument. Consider an investor in the home country, endowed with capital $N$ (measured in the home [[Forwards and Futures Notes|currency]]) to invest. This investor can pursue one of two strategies.

First, the investor can invest the home capital at the [[Covered Interest Rate Parity|home interest rate]] until maturity. Let $\Pi_\$(r_\$, T, N)$ denote the payoff function from this [[An Asset Allocation Primer|investment]] strategy.
$$\Pi_\$(r_\$, T, N) = e^{(r_\text{€} \cdot T)} \cdot N$$

Second, the investor can convert the home capital into foreign capital, invest the foreign capital at the foreign interest rate, and convert the proceeds on the foreign capital back into the home [[Forwards and Futures Notes|currency]] at the [[Forward Points in Currency|forward rate]] $F$.
$$\Pi_\text{€}(F; r_\text{€}, T, N, M) = e^{(r_\text{€} \cdot T)} \cdot \frac{N}{M} \cdot F$$

Note that both payoff functions, $\Pi_\$(\\cdot)$ and $\Pi_\text{€}(\\cdot)$, are measured in the home [[Forwards and Futures Notes|currency]] (e.g., USD).

The [[Forward Points in Currency|forward rate]] $F$ adjusts so as equate the payoffs from the two [[An Asset Allocation Primer|investment]] strategies.
$$\Pi_\$(r_\$, T, N) = \Pi_\text{€}(F; r_\text{€}, T, M, N)$$

This equation is a "no-[[Arbitrage Pricing of Derivatives|arbitrage]]" condition. Solving the no-[[Arbitrage Pricing of Derivatives|arbitrage]] condition for the endogenous variable $F$ yields the covered interest-rate parity formula for the [[Forward Points in Currency|forward rate]].
$$F = e^{(r_\$ - r_\text{€}) \cdot T]} \cdot M$$

Note that the [[Forward Points in Currency|forward rate]] $F$ inherits the units of the exchange rate $M$. Since the units of the exchange rate $M$ is Home/Foreign (e.g., USD/EUR), it follows that the units of the [[Forward Points in Currency|forward rate]] $F$ is also Home/Foreign.

## 3. INTERPRETATION

The [[Forward Points in Currency|forward rate]] $F$ is the exchange rate at which Home and Foreign currencies are exchanged upon maturity at time $T$ from inception. The [[Forward Points in Currency|forward rate]] $F$ is agreed upon at inception (i.e., at time 0).
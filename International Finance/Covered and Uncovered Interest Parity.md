---
cssclasses: academia
title: Covered and Uncovered Interest Parity
tags:
  - covered_interest_parity
  - exchange_rates
  - interest_rates
  - international_finance
  - uncovered_interest_parity
aliases:
  - CIP
  - FX Parity
  - Interest Parity
  - UIP
key_concepts:
  - Arbitrage in FX markets
  - 'CIP: interest rate parity'
  - Forward exchange contracts
  - Risk premium deviations
  - 'UIP: exchange rate expectations'
---

# Covered and Uncovered Interest Parity

[[Interest Rates, Carry Trades, and Exchange Rate Movements|Covered Interest Parity]] (CIP) and Uncovered [[Covered and Uncovered Interest Parity|Interest Parity]] (UIP) are two fundamental theories in [[International Trade Banking and Capital Markets Lecture Notes|international finance]] that describe the relationship between [[Interest Rate Quotations|interest rates]] and exchange rates between two countries. Let’s delve into each of these concepts,  their mechanisms,  and their real-world validity.

### CONCEPT

CIP states that the difference in [[Interest Rate Quotations|interest rates]] between two countries is equal to the difference between the [[A Primer on Currency Derivatives|forward exchange rate]] and the [[Arbitrage Opportunity Accounting|spot exchange rate]]. The relationship ensures that there is no [[Arbitrage Pricing of Derivatives|arbitrage]] opportunity when engaging in foreign exchange transactions covered by a [[Forward Points in Currency|forward contract]].

### FORMULA

The CIP condition can be expressed as:
$$
(1 + i_d) = (1 + i_f) \left(\frac{F}{S}\right)
$$

Where:

- $i_d$ is the domestic interest rate.
- $i_f$ is the foreign interest rate.
- $F$ is the [[A Primer on Currency Derivatives|forward exchange rate]].
- $S$ is the [[Arbitrage Opportunity Accounting|spot exchange rate]].

Alternatively,  rearranged:
$$
F = S \left(\frac{1 + i_d}{1 + i_f}\right)
$$

### MECHANISM
1. **[[Arbitrage Pricing of Derivatives|Arbitrage]]**: Suppose there is a discrepancy between the [[Interest Rate Quotations|interest rates]] and the [[Forward Points in Currency|forward rate]]. Traders would exploit this by borrowing in the country with a lower interest rate,  converting to the foreign [[Forwards and Futures Notes|currency]],  and entering a [[Forward Points in Currency|forward contract]] to convert back to the domestic [[Forwards and Futures Notes|currency]] after a certain period. The [[Class Note 13 The LTCM Meltdown|arbitrage opportunities]] would eventually drive the [[Forward Points in Currency|forward rate]] to a level where CIP holds.
1. **Forward Contracts**: Forward contracts are agreements to [[Currency Swap Basics|exchange currencies]] at a future date at a predetermined rate. They are used to hedge against exchange rate fluctuations.

### REAL-WORLD VALIDITY
- **Generally Holds**: CIP is considered one of the strongest empirical regularities in finance,  primarily due to the relatively low transaction costs and high [[Class Note 10 Liquidity and Class Note 10 Liquidity and Liquidity Managementliquidity management|liquidity]] in major [[Forwards and Futures Notes|currency]] markets.
- **Deviations**: Temporary deviations can occur due to factors such as capital controls,  transaction costs,  and differing levels of risk in different markets,  but [[Arbitrage Pricing of Derivatives|arbitrage]] typically brings the relationship back into equilibrium.

## UNCOVERED INTEREST PARITY (UIP)

### CONCEPT

UIP suggests that the difference in [[Interest Rate Quotations|interest rates]] between two countries is equal to the expected change in exchange rates between these two countries. Unlike CIP,  UIP does not involve the use of forward contracts,  making it "uncovered."

### FORMULA

The UIP condition can be expressed as:
$$
(1 + i_d) = (1 + i_f) E\left(\frac{S_{t+1}}{S_t}\right)
$$

Where:

- $i_d$ is the domestic interest rate.
- $i_f$ is the foreign interest rate.
- $E(S_{t+1})$ is the expected future [[Arbitrage Opportunity Accounting|spot exchange rate]].
- $S_t$ is the current [[Arbitrage Opportunity Accounting|spot exchange rate]].

Alternatively,  in logarithmic form:
$$
i_d - i_f = E(\Delta s)
$$

Where $\Delta s$ represents the expected change in the logarithm of the exchange rate.

### MECHANISM
1. **[[FORWARD RATES AND TERM STRUCTURE|Expectations]]**: UIP relies on [[Forward Rate|market expectations]] about future exchange rates. Investors will be indifferent between domestic and foreign investments if the [[Lecture 1- Probability Distributions of Returns|expected return]],  adjusted for exchange [[Profit and Loss Attribution with an OAS|rate changes]],  is equal.
1. **Risk**: The risk premium can cause deviations from UIP. If investors require additional compensation for holding riskier foreign assets,  this can lead to differences between actual and expected [[Assets|returns]].

### REAL-WORLD VALIDITY
- **Less Reliable**: UIP is less robust empirically compared to CIP. Studies often find that exchange rates do not always move in the manner predicted by UIP.
- **Reasons for Deviation**: Factors like risk premiums,  exchange rate volatility,  behavioral [[Week 2 Fundamentals Of Forecasting|biases]],  and deviations from rational [[FORWARD RATES AND TERM STRUCTURE|expectations]] contribute to the failure of UIP in the real world.

## IMPLEMENTATION AND REAL-WORLD OBSERVATIONS

### CIP IMPLEMENTATION
- **[[Arbitrage Pricing of Derivatives|Arbitrage]] Activity**: [[Financial Markets and Institutions Lecture Notes|Financial institutions]] continuously monitor [[What Really Is the Cross-Currency Basis|interest rate differentials]] and forward rates,  engaging in [[Arbitrage Pricing of Derivatives|arbitrage]] when opportunities arise.
- **[[Key Rates O1s Durations and Hedging|Hedging]]**: Corporations use forward contracts to hedge against [[Forwards and Futures Notes|currency]] risk,  ensuring the certainty of [[Advanced Derivatives Pricing Methodology|future cash flows]].

### UIP IMPLEMENTATION
- **[[An Asset Allocation Primer|Investment]] Decisions**: Investors consider [[What Really Is the Cross-Currency Basis|interest rate differentials]] and expected exchange rate movements when making [[An Asset Allocation Primer|investment]] decisions across borders.
- **[[Week 2 Fundamentals Of Forecasting|Forecasting]] Models**: Economists and financial analysts use UIP as a basis for [[Week 2 Fundamentals Of Forecasting|forecasting]] exchange rates,  though with caution given its empirical limitations.

### OBSERVATIONS
- **CIP Deviations**: Instances such as the [[8. Credit Modeling and Credit Derivatives|Global Financial Crisis]] of 2008 showed significant CIP deviations due to heightened counterparty risk and [[Class Note 10 Liquidity and Class Note 10 Liquidity and Liquidity Managementliquidity management|liquidity]] constraints.
- **UIP Failures**: Studies have shown that high-interest rate currencies tend to depreciate less than predicted by UIP,  a phenomenon known as the "forward premium puzzle."

In conclusion,  while CIP generally holds due to the ease of [[Arbitrage Pricing of Derivatives|arbitrage]] and the efficiency of the [[Tba and Specified Pools Markets|forward market]],  UIP is more contentious and often fails to predict future exchange rate movements accurately due to the complexities of [[Forward Rate|market expectations]] and [[HomeMax Case Study Solution|risk considerations]].
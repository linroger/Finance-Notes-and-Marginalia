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

[Covered Interest Parity](../Financial%20Instruments/Lecture%20Notes-%20Financial%20Instruments/Teaching%20Note%201-%20Forward%20Rates%20Agreement/Interest%20Rates,%20Carry%20Trades,%20and%20Exchange%20Rate%20Movements.md) (CIP) and Uncovered [Interest Parity](.md) (UIP) are two fundamental theories in [international finance](../Course%20Notes/International%20Trade%20Banking%20and%20Capital%20Markets%20Lecture%20Notes.md) that describe the relationship between [interest rates](../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%202/Interest%20Rate%20Quotations.md) and exchange rates between two countries. Let’s delve into each of these concepts,  their mechanisms,  and their real-world validity.

### CONCEPT

CIP states that the difference in [interest rates](../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%202/Interest%20Rate%20Quotations.md) between two countries is equal to the difference between the [forward exchange rate](../Financial%20Engineering/A%20Primer%20on%20Currency%20Derivatives.md) and the [spot exchange rate](../Financial%20Instruments/Review%20Session%20Notes/Arbitrage%20Opportunity%20Accounting.md). The relationship ensures that there is no [arbitrage](../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%207/Arbitrage%20Pricing%20of%20Derivatives.md) opportunity when engaging in foreign exchange transactions covered by a [forward contract](../Clippings/Forward%20Points%20in%20Currency.md).

### FORMULA

The CIP condition can be expressed as:
$$
(1 + i_d) = (1 + i_f) \left(\frac{F}{S}\right)
$$

Where:

- $i_d$ is the domestic interest rate.
- $i_f$ is the foreign interest rate.
- $F$ is the [forward exchange rate](../Financial%20Engineering/A%20Primer%20on%20Currency%20Derivatives.md).
- $S$ is the [spot exchange rate](../Financial%20Instruments/Review%20Session%20Notes/Arbitrage%20Opportunity%20Accounting.md).

Alternatively,  rearranged:
$$
F = S \left(\frac{1 + i_d}{1 + i_f}\right)
$$

### MECHANISM
1. **[Arbitrage](../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%207/Arbitrage%20Pricing%20of%20Derivatives.md)**: Suppose there is a discrepancy between the [interest rates](../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%202/Interest%20Rate%20Quotations.md) and the [forward rate](../Clippings/Forward%20Points%20in%20Currency.md). Traders would exploit this by borrowing in the country with a lower interest rate,  converting to the foreign [currency](../Financial%20Instruments/Lecture%20Notes-%20Financial%20Instruments/Teaching%20Note%201-%20Forward%20Rates%20Agreement/Forwards%20and%20Futures%20Notes.md),  and entering a [forward contract](../Clippings/Forward%20Points%20in%20Currency.md) to convert back to the domestic [currency](../Financial%20Instruments/Lecture%20Notes-%20Financial%20Instruments/Teaching%20Note%201-%20Forward%20Rates%20Agreement/Forwards%20and%20Futures%20Notes.md) after a certain period. The [arbitrage opportunities](../Financial%20Markets%20and%20Institutions/III.%20Liquidity%20of%20Assets/Class%208-%20Markets,%20Meltdowns,%20and%20Arbitrage/Class%20Note%2013%20The%20LTCM%20Meltdown.md) would eventually drive the [forward rate](../Clippings/Forward%20Points%20in%20Currency.md) to a level where CIP holds.
1. **Forward Contracts**: Forward contracts are agreements to [exchange currencies](../Clippings/Currency%20Swap%20Basics.md) at a future date at a predetermined rate. They are used to hedge against exchange rate fluctuations.

### REAL-WORLD VALIDITY
- **Generally Holds**: CIP is considered one of the strongest empirical regularities in finance,  primarily due to the relatively low transaction costs and high [liquidity](../Financial%20Markets%20and%20Institutions/III.%20Liquidity%20of%20Assets/Class%205-%20Private%20Information,%20Liquidity,%20and%20Securitization/Class%20Note%2010%20Liquidity%20and%20Class%20Note%2010%20Liquidity%20and%20Liquidity%20Managementliquidity%20management.md) in major [currency](../Financial%20Instruments/Lecture%20Notes-%20Financial%20Instruments/Teaching%20Note%201-%20Forward%20Rates%20Agreement/Forwards%20and%20Futures%20Notes.md) markets.
- **Deviations**: Temporary deviations can occur due to factors such as capital controls,  transaction costs,  and differing levels of risk in different markets,  but [arbitrage](../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%207/Arbitrage%20Pricing%20of%20Derivatives.md) typically brings the relationship back into equilibrium.

## UNCOVERED INTEREST PARITY (UIP)

### CONCEPT

UIP suggests that the difference in [interest rates](../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%202/Interest%20Rate%20Quotations.md) between two countries is equal to the expected change in exchange rates between these two countries. Unlike CIP,  UIP does not involve the use of forward contracts,  making it "uncovered."

### FORMULA

The UIP condition can be expressed as:
$$
(1 + i_d) = (1 + i_f) E\left(\frac{S_{t+1}}{S_t}\right)
$$

Where:

- $i_d$ is the domestic interest rate.
- $i_f$ is the foreign interest rate.
- $E(S_{t+1})$ is the expected future [spot exchange rate](../Financial%20Instruments/Review%20Session%20Notes/Arbitrage%20Opportunity%20Accounting.md).
- $S_t$ is the current [spot exchange rate](../Financial%20Instruments/Review%20Session%20Notes/Arbitrage%20Opportunity%20Accounting.md).

Alternatively,  in logarithmic form:
$$
i_d - i_f = E(\Delta s)
$$

Where $\Delta s$ represents the expected change in the logarithm of the exchange rate.

### MECHANISM
1. **[Expectations](../Fixed%20Income%20Asset%20Pricing/Fixed%20Income%20Lecture%20Notes/FORWARD%20RATES%20AND%20TERM%20STRUCTURE.md)**: UIP relies on [market expectations](../Clippings/Forward%20Rate.md) about future exchange rates. Investors will be indifferent between domestic and foreign investments if the [expected return](../Advanced%20Investments/Lecture%201-%20Probability%20Distributions%20of%20Returns.md),  adjusted for exchange [rate changes](../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%207/Profit%20and%20Loss%20Attribution%20with%20an%20OAS.md),  is equal.
1. **Risk**: The risk premium can cause deviations from UIP. If investors require additional compensation for holding riskier foreign assets,  this can lead to differences between actual and expected [returns](../Financial%20Markets/Financial%20Asset%20Pricing%20Theory%20Overview/Chapter%203%20-%20%20Assets,%20Portfolios,%20and%20Arbitrage/Assets.md).

### REAL-WORLD VALIDITY
- **Less Reliable**: UIP is less robust empirically compared to CIP. Studies often find that exchange rates do not always move in the manner predicted by UIP.
- **Reasons for Deviation**: Factors like risk premiums,  exchange rate volatility,  behavioral [biases](../Advanced%20Financial%20Analysis%20and%20Valuation/Lecture%20Notes%20Advanced%20Financial%20Analysis%20and%20Valuation/Week%202/Week%202%20Fundamentals%20Of%20Forecasting.md),  and deviations from rational [expectations](../Fixed%20Income%20Asset%20Pricing/Fixed%20Income%20Lecture%20Notes/FORWARD%20RATES%20AND%20TERM%20STRUCTURE.md) contribute to the failure of UIP in the real world.

## IMPLEMENTATION AND REAL-WORLD OBSERVATIONS

### CIP IMPLEMENTATION
- **[Arbitrage](../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%207/Arbitrage%20Pricing%20of%20Derivatives.md) Activity**: [Financial institutions](../Financial%20Markets%20and%20Institutions/Financial%20Markets%20and%20Institutions%20Lecture%20Notes.md) continuously monitor [interest rate differentials](../Financial%20Markets/Random%20Walks%20in%20Fixed%20Income%20and%20Foreign%20Exchange/Chapter%201/What%20Really%20Is%20the%20Cross-Currency%20Basis.md) and forward rates,  engaging in [arbitrage](../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%207/Arbitrage%20Pricing%20of%20Derivatives.md) when opportunities arise.
- **[Hedging](../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%205/Key%20Rates%20O1s%20Durations%20and%20Hedging.md)**: Corporations use forward contracts to hedge against [currency](../Financial%20Instruments/Lecture%20Notes-%20Financial%20Instruments/Teaching%20Note%201-%20Forward%20Rates%20Agreement/Forwards%20and%20Futures%20Notes.md) risk,  ensuring the certainty of [future cash flows](../Financial%20Engineering/Advanced%20Derivatives%20Pricing%20Methodology.md).

### UIP IMPLEMENTATION
- **[Investment](../Advanced%20Investments/An%20Asset%20Allocation%20Primer.md) Decisions**: Investors consider [interest rate differentials](../Financial%20Markets/Random%20Walks%20in%20Fixed%20Income%20and%20Foreign%20Exchange/Chapter%201/What%20Really%20Is%20the%20Cross-Currency%20Basis.md) and expected exchange rate movements when making [investment](../Advanced%20Investments/An%20Asset%20Allocation%20Primer.md) decisions across borders.
- **[Forecasting](../Advanced%20Financial%20Analysis%20and%20Valuation/Lecture%20Notes%20Advanced%20Financial%20Analysis%20and%20Valuation/Week%202/Week%202%20Fundamentals%20Of%20Forecasting.md) Models**: Economists and financial analysts use UIP as a basis for [forecasting](../Advanced%20Financial%20Analysis%20and%20Valuation/Lecture%20Notes%20Advanced%20Financial%20Analysis%20and%20Valuation/Week%202/Week%202%20Fundamentals%20Of%20Forecasting.md) exchange rates,  though with caution given its empirical limitations.

### OBSERVATIONS
- **CIP Deviations**: Instances such as the [Global Financial Crisis](../Financial%20Engineering/8.%20Credit%20Modeling%20and%20Credit%20Derivatives.md) of 2008 showed significant CIP deviations due to heightened counterparty risk and [liquidity](../Financial%20Markets%20and%20Institutions/III.%20Liquidity%20of%20Assets/Class%205-%20Private%20Information,%20Liquidity,%20and%20Securitization/Class%20Note%2010%20Liquidity%20and%20Class%20Note%2010%20Liquidity%20and%20Liquidity%20Managementliquidity%20management.md) constraints.
- **UIP Failures**: Studies have shown that high-interest rate currencies tend to depreciate less than predicted by UIP,  a phenomenon known as the "forward premium puzzle."

In conclusion,  while CIP generally holds due to the ease of [arbitrage](../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%207/Arbitrage%20Pricing%20of%20Derivatives.md) and the efficiency of the [forward market](../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%2015/Tba%20and%20Specified%20Pools%20Markets.md),  UIP is more contentious and often fails to predict future exchange rate movements accurately due to the complexities of [market expectations](../Clippings/Forward%20Rate.md) and [risk considerations](../Financial%20Markets%20and%20Institutions/II.%20The%20Roles%20of%20Banks%20and%20Derivative%20Markets%20in%20Resolving%20Problems%20Inherent%20in%20Debt%20Contracts/HomeMax%20Case%20Study%20Solution.md).
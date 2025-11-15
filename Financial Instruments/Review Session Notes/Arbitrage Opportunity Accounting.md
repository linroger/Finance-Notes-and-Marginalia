---
title: Arbitrage Opportunity Accounting
aliases:
- Currency Swap Accounting
- FX Risk Management
- Foreign Currency Bonds
key_concepts:
- Basis swap mechanics
- Bond valuation in foreign currencies
- Cross-currency basis
- Currency swap contracts
- Currency swap structure
- Derivative securities
- Exchange rate risk hedging
- Financial risk management
- Fixed vs floating leg
- Foreign currency bonds issuance
- Interest rate swap pricing
- Portfolio optimization
- Present value of swaps
- Quantitative financial analysis
- Risk assessment and mitigation
- Spot exchange rate mechanics
- Swap curve construction
- Swap rate determination
- Swaption valuation
tags:
- arbitrage-opportunity
- bond
- bond-valuation
- cost-of-debt
- currency
- currency-swaps
- exam-prep
- exchange-rate
- exchange-rate-risk
- government-bonds
- hedging-strategies
- review-session
- swap
---

# Arbitrage Opportunity Accounting

## Key Concepts

### Overview
Governments often issue bonds in foreign currencies to access broader capital markets or meet investor demand. However, this creates **exchange rate risk** - if the foreign currency appreciates relative to the home currency, the cost of debt service increases.

**Currency swaps** serve as an effective hedge against this exchange rate risk by allowing the government to exchange foreign currency cash flows for domestic currency cash flows.

### Currency Swap Mechanics

A currency swap is a contractual agreement between two parties to exchange:
- **Principal amounts** in different currencies at inception and maturity
- **Interest payments** in each currency over the life of the swap

## Formulas/Math

### Bond Valuation in Foreign Currency

The value of a bond denominated in foreign currency F at time $t = 0$:

$$B_0^F = \sum_{t=1}^T \frac{c}{2} \cdot N_F \cdot Z_F(0, t) + N_F \cdot Z_F(0, T)$$

Where:
- $c$ = annual coupon rate (semi-annual payments)
- $N_F$ = principal amount in foreign currency
- $Z_F(0, t)$ = discount factor for foreign currency
- First term = present value of interest payments
- Second term = present value of principal

### Bond Valuation in Home Currency

The value of a bond denominated in home currency H at time $t = 0$:

$$B_0^H(K) = \sum_{t=1}^T \frac{K}{2} \cdot N_H \cdot Z_H(0, t) + N_H \cdot Z_H(0, T)$$

Where $K$ is the **swap rate** (annualized coupon rate for semi-annual payments in H currency).

### Currency Swap Setup

**At Inception ($t = 0$):**
- Home pays: $N_F = X$ in foreign currency F
- Home receives: $N_H = X \cdot \frac{1}{M_0}$ in home currency H
- $M_0$ = spot exchange rate (units of H per unit of F)

**At Maturity ($t = T$):**
- Home receives: $N_F = X$ in foreign currency F
- Home pays: $N_H = X \cdot \frac{1}{M_0}$ in home currency H

### Swap Value Calculation

Time $t = 0$ value of the swap in foreign currency F:

$$V_{0}^{\text{Swap, }F}(K) = B_{0}^{F} - M_{0} \cdot B_{0}^{H}(K) + V_{0}^{\text{FX, }F}(\bar{M}_{0})$$

**Value of Exchange of Principal:**

$$V_0^{\mathrm{FX, }F}(\bar{M}_0) = \left(\frac{M_0}{\bar{M}_0} - 1\right) \cdot N^F$$

### No-Arbitrage Condition

The swap rate $K$ is determined such that the swap has **zero value** at inception:

$$V_{0}^{\text{Swap, }F}(K) = 0$$

## Examples

### Example 1: Government Bond Issuance with Currency Swap

**Scenario:**
- Country H (Home) issues government bonds worth $X = 100$ million USD
- H's home currency is EUR
- Spot exchange rate: $M_0 = 1.2$ USD/EUR
- Annual coupon rate: $c = 5\%$
- Maturity: $T = 5$ years

**Setup:**
1. **At Inception:**
   - H issues $100$ million USD bonds
   - H enters swap: Pays $100$ million USD, Receives $100 / 1.2 = 83.33$ million EUR

2. **Swap Cash Flows:**
   - Semi-annual interest payments exchanged
   - Principal amounts exchanged at maturity

**Key Insight:**
The swap effectively converts the USD-denominated debt into EUR-denominated debt, eliminating exchange rate risk on both interest and principal payments.

### Example 2: Swap Rate Calculation

**Given:**
- Foreign bond value: $B_0^F = 95$ million USD
- Exchange rate: $M_0 = 1.2$ USD/EUR
- Home discount factors: $Z_H(0, t) = e^{-r_H \cdot t}$ where $r_H = 3\%$

**Find the swap rate $K$ such that:**

$$B_0^F - M_0 \cdot B_0^H(K) + V_0^{\mathrm{FX, }F}(\bar{M}_0) = 0$$

**Solution Approach:**
1. Calculate home currency bond value $B_0^H(K)$
2. Solve for $K$ that sets swap value to zero
3. This $K$ represents the coupon rate that makes the swap fair

## Study Points

**Key Formulas to Remember:**
- Foreign bond valuation: $B_0^F = \text{PV(interest)} + \text{PV(principal)}$
- Currency swap setup: Principal exchange at inception and maturity
- Swap value: $V_{0}^{\text{Swap}} = B_{0}^{\text{Foreign}} - M_{0} \cdot B_{0}^{\text{Home}} + V_{0}^{\text{FX}}$
- No-arbitrage: Swap value = 0 at inception

**Common Exam Questions:**
- Calculate swap rate given bond values
- Determine optimal hedge ratio
- Evaluate exchange rate risk exposure
- Price currency swap contracts

---
title: Currency Swaps
aliases:
- FX swap
- Currency Swap
- Cross-Currency Swap
key_concepts:
- Basis swap mechanics
- Bond valuation in foreign currencies
- Cross-currency basis
- Currency swap rates determination
- Currency swap structure
- Derivative securities
- Exchange rate risk hedging
- Financial risk management
- Fixed vs floating leg
- Government bond issuance
- Interest rate differentials
- Interest rate swap pricing
- Portfolio optimization
- Present value of swaps
- Principal exchange mechanics
- Quantitative financial analysis
- Risk assessment and mitigation
- Semi-annual coupon payments
- Swap contract mechanics
- Swap curve construction
- Swaption valuation
tags:
- bond
- cross-currency-swaps
- currency
- currency-swaps
- exam-prep
- exchange-rate
- exchange-rate-risk
- fixed-income
- forward
- government-bonds
- hedging
- interest-rate
- international-finance
- review-session
- swap
- swap-contract
---

# Currency Swaps

## Key Concepts

### Overview
Currency swaps are financial contracts that allow parties to exchange **principal and interest payments** in different currencies. They are commonly used by governments and corporations to hedge **exchange rate risk** when issuing debt in foreign currencies.

**Key Benefits:**
- Hedge against currency fluctuations
- Access to foreign capital markets
- Manage interest rate exposure
- Reduce funding costs

### Currency Swap Mechanics

A currency swap involves two main exchanges:

1. **Principal Exchange** at inception and maturity
2. **Interest Payment Exchange** throughout the life of the swap

**Currency swap parties:**
- **Home (H)**: Issues bonds in foreign currency F
- **Foreign (F)**: Provides the foreign currency funding
- **Swap counterparty**: Facilitates the exchange

## Formulas/Math

### Bond Valuation in Foreign Currency

**Value of bond denominated in foreign currency F at $t = 0$:**

$$B_0^F = \sum_{t=1}^T \frac{c}{2} \cdot N_F \cdot Z_F(0, t) + N_F \cdot Z_F(0, T)$$

**Components:**
- **Interest PV:** $\sum_{t=1}^T \frac{c}{2} \cdot N_F \cdot Z_F(0, t)$
- **Principal PV:** $N_F \cdot Z_F(0, T)$
- $c$ = annual coupon rate (semi-annual payments)
- $N_F$ = principal amount in foreign currency
- $Z_F(0, t)$ = discount factor for foreign currency

### Bond Valuation in Home Currency

**Value of bond denominated in home currency H at $t = 0$:**

$$B_0^H(K) = \sum_{t=1}^T \frac{K}{2} \cdot N_H \cdot Z_H(0, t) + N_H \cdot Z_H(0, T)$$

Where:
- $K$ = **swap rate** (annualized coupon rate for semi-annual payments in H currency)
- $N_H$ = principal amount in home currency
- $Z_H(0, t)$ = discount factor for home currency

### Currency Swap Setup

**At Inception ($t = 0$):**
- Home **pays**: $N_F = X$ in foreign currency F
- Home **receives**: $N_H = X \cdot \frac{1}{M_0}$ in home currency H
- $M_0$ = spot exchange rate (units of H per unit of F)

**At Maturity ($t = T$):**
- Home **receives**: $N_F = X$ in foreign currency F  
- Home **pays**: $N_H = X \cdot \frac{1}{M_0}$ in home currency H

### Swap Value Calculation

**Time $t = 0$ value of swap in foreign currency F:**

$$V_{0}^{\text{Swap, }F}(K) = B_{0}^{F} - M_{0} \cdot B_{0}^{H}(K) + V_{0}^{\text{FX, }F}(\bar{M}_{0})$$

**Value of Exchange of Principal:**

$$V_0^{\mathrm{FX, }F}(\bar{M}_0) = \left(\frac{M_0}{\bar{M}_0} - 1\right) \cdot N^F$$

### No-Arbitrage Condition

The swap rate $K$ is set such that the **swap has zero value** at inception:

$$V_{0}^{\text{Swap, }F}(K) = 0$$

This ensures a **fair swap** with no initial cost to either party.

## Examples

### Example 1: Government Currency Swap Hedging

**Scenario:**
- Country H wants to issue $200$ million USD bonds
- H's home currency is EUR
- USD coupon: $c = 4.5\%$ annually
- Spot rate: $M_0 = 1.10$ USD/EUR
- Maturity: $T = 7$ years

**Step 1: Principal Exchange Calculation**
- USD principal: $N_{USD} = 200$ million
- EUR principal: $N_{EUR} = 200 / 1.10 = 181.82$ million

**Step 2: Swap Cash Flows**

**At Inception:**
- H pays 200 million USD to counterparty
- H receives 181.82 million EUR from counterparty

**During Swap (Semi-annually for 7 years):**
- H pays: $(4.5\% / 2) \times 200 = 4.5$ million USD in interest
- H receives: $(K / 2) \times 181.82$ million EUR in interest

**At Maturity:**
- H receives 200 million USD from counterparty
- H pays 181.82 million EUR to counterparty

**Benefit:** H has effectively converted USD debt into EUR debt, eliminating exchange rate risk on both interest and principal.

### Example 2: Determining Swap Rate

**Given:**
- Foreign bond value: $B_0^F = 185$ million USD
- Exchange rate: $M_0 = 1.15$ USD/EUR
- Home discount factors: $Z_H(0, t) = e^{-0.03t}$ (3% continuously compounded)
- Principal: $N_F = 200$ million USD → $N_H = 173.91$ million EUR

**Find $K$ such that swap value = 0**

**Equation:**
$$185 - 1.15 \cdot B_0^H(K) + \left(\frac{1.15}{1.15} - 1\right) \cdot 200 = 0$$

$$185 - 1.15 \cdot B_0^H(K) = 0$$

$$B_0^H(K) = 185 / 1.15 = 160.87 \text{ million USD}$$

**Solution approach:**
1. Calculate present value of EUR interest payments
2. Find coupon rate $K$ that makes $B_0^H(K) = 160.87$
3. This $K$ is the **fair swap rate** for EUR payments

### Example 3: Swap Value Evaluation

**Given:**
- $B_0^F = 95$ million USD
- $B_0^H(K) = 80$ million EUR
- $M_0 = 1.25$ USD/EUR
- $N_F = 100$ million USD

**Calculate swap value:**
$$V_{0}^{\text{Swap}} = 95 - 1.25 \cdot 80 + 0 = 95 - 100 = -5$$

**Interpretation:**
- Swap has **negative value** of -5 million USD for Home
- Counterparty has **positive value** of +5 million USD
- This suggests $K$ is too high for Home (Home paying too much in EUR interest)

## Study Points

### Key Formulas to Remember

1. **Foreign bond value:** $B_0^F = \text{PV(interest)} + \text{PV(principal)}$
2. **Home bond value:** $B_0^H(K) = f(K)$ (linear in swap rate $K$)
3. **Swap setup:** Principal exchange at inception and maturity
4. **Swap value:** $V_{0}^{\text{Swap}} = B_{0}^{F} - M_{0} \cdot B_{0}^{H}(K) + V_{0}^{\text{FX}}$
5. **No-arbitrage:** Set $V_{0}^{\text{Swap}} = 0$ to solve for fair $K$

### Swap Rate Determination Process

1. **Identify bond values** in both currencies
2. **Convert home bond value** to foreign currency using spot rate
3. **Set swap value to zero** (no-arbitrage condition)
4. **Solve for swap rate** $K$ that balances the equation
5. **Verify** the solution makes economic sense

### Common Exam Questions

- Calculate swap rate given bond market values
- Determine optimal hedge ratio for currency exposure
- Evaluate whether to hedge using swaps vs. forwards
- Analyze swap value changes given exchange rate movements
- Compare fixed-for-fixed vs. other swap structures

### Key Insights

- **Swap rate $K$** is determined by market forces, not arbitrarily set
- **Zero initial value** makes swaps attractive (no upfront payment)
- **Principal exchange** at both ends ensures full currency hedge
- **Semi-annual payments** match common bond coupon frequencies
- **Market value** of swap can become positive or negative over time

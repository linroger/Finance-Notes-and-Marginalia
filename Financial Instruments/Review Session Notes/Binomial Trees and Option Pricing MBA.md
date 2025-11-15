---
title: Binomial Trees and Option Pricing MBA
aliases:
- BOPM
- Binomial Option Pricing
- Option Valuation
- Single-Period Option Model
key_concepts:
- ATM option valuation
- American options valuation
- Backward induction algorithm
- Beta calculation
- Binomial option pricing model
- Binomial tree parameters
- CAPM formula
- Capital Asset Pricing Model
- Convergence to Black-Scholes
- Cost of equity estimation
- Cox-Ross-Rubinstein framework
- Delta risk management
- Derivative securities
- Dynamic hedging strategies
- Dynamic replication strategies
- Financial risk management
- Gamma effects on options
- Lattice methods for derivatives
- Market efficiency implications
- Market portfolio
- Multi-period binomial tree
- Options Greeks measurement
- Portfolio optimization
- Portfolio risk hedging
- Quantitative financial analysis
- Rho interest rate sensitivity
- Risk assessment and mitigation
- Risk neutral probability
- Risk-neutral methodology
- Risk-neutral probability
- Risk-return tradeoff
- Security Market Line
- Single-period option pricing
- Stock price at maturity
- Systematic vs idiosyncratic risk
- Theta time decay
- Vega volatility sensitivity
tags:
- binomial
- binomial-tree
- bond
- call
- capm
- comparative-statics
- dynamic-replication
- exam-prep
- greeks
- interest-rate
- market-risk
- market-risk-premium
- option
- option-pricing
- review-session
- risk-free-rate
- risk-neutral
- stock
- stock-valuation
---

# Binomial Trees and Option Pricing MBA

## Key Concepts

### Binomial Model Overview
The Binomial Option Pricing Model (BOPM) is a discrete-time approach to option valuation that models stock price movements using a **binomial tree**. At each period, the stock price can either move **up** or **down** by specified factors.

### Key Parameters
- **Stock price at inception**: $S_0$
- **Up factor**: $u$ (stock price increases to $S_u = u \cdot S_0$)
- **Down factor**: $d$ (stock price decreases to $S_d = d \cdot S_0$)
- **Risk-free rate**: $r_f$ (continuously compounded)
- **Systematic risk**: $\beta_i$ (for stock $i$)

### CAPM Relationship
The Capital Asset Pricing Model (CAPM) relates expected return to systematic risk:
$$E[R_i] = \bar{r}_f + \beta_i \cdot [E[R_m] - r_f]$$

Where:
- $E[R_i]$ = expected return on stock $i$
- $\bar{r}_f$ = risk-free rate (annually compounded)
- $E[R_m] - r_f$ = market risk premium

### Two Pricing Approaches

1. **Dynamic Replication**: Construct a hedging portfolio that replicates option payoff
2. **Risk-Neutral Valuation**: Use risk-neutral probabilities to price the option

## Formulas/Math

### Stock Price Evolution

**At maturity $t = T$:**
$$S_{T, i} \in \{S_d, S_u\}$$

**Expected stock price at $t = T$ under analyst probability $q$:**
$$E_q[S_{T, i}] = q \cdot S_u + (1 - q) \cdot S_d$$

**Present value at $t = 0$:**
$$(1 + E[R_i]) \cdot S_{0, i} = E[S_{T, i}]$$

### Dynamic Replication for ATM Options

An **at-the-money (ATM)** option has strike price $K_i = S_{0, i}$.

**Option payoff at maturity:**
$$c(S_{T, i}) = \begin{cases} 
\max\{S_d - K_i, 0\} & \text{if } S_{T, i} = S_d \\
\max\{S_u - K_i, 0\} & \text{if } S_{T, i} = S_u
\end{cases}$$

**Position in stocks (delta):**
$$\Delta_{i, 0} = \frac{\max\{S_u - K_i, 0\} - \max\{S_d - K_i, 0\}}{S_u - S_d}$$

**Position in bonds:**
$$B_0 = e^{(-r_f)} \cdot [\max\{S_u - K_i, 0\} - \Delta_{i, 0} \cdot S_u]$$

**Option value:**
$$V_0^{\text{ATM}} = \Delta_{i, 0} \cdot S_{0, i} + B_0$$

**Replication portfolio payoff at $t = T$:**
$$V_{T, i}^{DR}(S_{T, i}) = \begin{cases} 
\Delta_{i, 0} \cdot S_d + e^{r_f} \cdot B_0 & \text{if } S_{T, i} = S_d \\
\Delta_{i, 0} \cdot S_u + e^{r_f} \cdot B_0 & \text{if } S_{T, i} = S_u
\end{cases}$$

### Risk-Neutral Methodology

**Risk-neutral probability $q^*$:** Equates expected stock return to risk-free return
$$q^* \cdot \frac{S_u}{S_0} + (1 - q^*) \cdot \frac{S_d}{S_0} = e^{r_f}$$

**Expected stock price under risk-neutral probability:**
$$E_{q^*}[S_{T, i}] = q^* \cdot S_u + (1 - q^*) \cdot S_d$$

**Option value under risk-neutral pricing:**
$$V_0^{\text{ATM}} = e^{-r_f} \cdot [q^* \cdot \max\{S_u - K_i, 0\} + (1 - q^*) \cdot \max\{S_d - K_i, 0\}]$$

### Interest Rate Conversions

**Continuous to annual:**
$$1 + \bar{r}_f = \exp(r_f)$$

**Annual to continuous:**
$$1 + \bar{r}_f = \exp(-r_f)$$

## Examples

### Example 1: ATM Call Option Pricing

**Given:**
- $S_0 = 100$, $K = 100$ (ATM)
- Up factor: $u = 1.10$ (stock rises 10%)
- Down factor: $d = 0.90$ (stock falls 10%)
- Risk-free rate: $r_f = 5\%$ (continuous)
- Analyst probability of up: $q = 0.60$

**Step 1: Calculate option payoffs**
- If up: $\max\{110 - 100, 0\} = 10$
- If down: $\max\{90 - 100, 0\} = 0$

**Step 2: Dynamic Replication**
$$\Delta_0 = \frac{10 - 0}{110 - 90} = 0.5$$

$$B_0 = e^{-0.05} \cdot [10 - 0.5 \cdot 110] = 0.9512 \cdot [-45] = -42.80$$

$$V_0 = 0.5 \cdot 100 + (-42.80) = 50 - 42.80 = 7.20$$

**Result:** Option value = **$7.20**

**Step 3: Risk-Neutral Method**

First, solve for $q^*$:
$$q^* \cdot \frac{110}{100} + (1 - q^*) \cdot \frac{90}{100} = e^{0.05}$$

$$q^* \cdot 1.10 + (1 - q^*) \cdot 0.90 = 1.0513$$

$$1.10q^* + 0.90 - 0.90q^* = 1.0513$$

$$0.20q^* = 0.1513$$

$$q^* = 0.7565$$

**Option value:**
$$V_0 = e^{-0.05} \cdot [0.7565 \cdot 10 + (1 - 0.7565) \cdot 0]$$

$$V_0 = 0.9512 \cdot 7.565 = 7.20$$

**Consistency Check:** Both methods give the same result!

### Example 2: CAPM and Stock Valuation

**Given:**
- $S_0 = 50$
- $\beta_i = 1.5$
- $r_f = 3\%$ (continuous) → $\bar{r}_f = 3.045\%$
- $E[R_m] - r_f = 8\%$
- $q = 0.55$, $u = 1.20$, $d = 0.80$

**Step 1: Calculate expected return using CAPM**
$$E[R_i] = 0.03045 + 1.5 \cdot 0.08 = 0.15045 = 15.045\%$$

**Step 2: Calculate expected stock price at T**
$$E[S_T] = 0.55 \cdot 60 + 0.45 \cdot 40 = 33 + 18 = 51$$

**Step 3: Verify present value**
$$(1 + 0.15045) \cdot 50 = 57.52 \neq 51$$

**Analysis:** The expected return implies a different present value than current price, suggesting either:
- Market inefficiency
- Risk premium adjustment needed
- Probability estimates need revision

## Study Points

### Key Formulas Summary

**Dynamic Replication:**
- $\Delta = \frac{c_u - c_d}{S_u - S_d}$
- $B = e^{-rT} \cdot (c_u - \Delta \cdot S_u)$
- $V_0 = \Delta \cdot S_0 + B$

**Risk-Neutral Pricing:**
- Solve $q^*$ from: $q^* \cdot u + (1 - q^*) \cdot d = e^{r_f}$
- $V_0 = e^{-r_f} \cdot [q^* \cdot c_u + (1 - q^*) \cdot c_d]$

**CAPM:**
- $E[R_i] = \bar{r}_f + \beta_i \cdot (E[R_m] - r_f)$

### Comparative Statics

**Change in Analyst Probabilities ($q$):**
- Affects $E[S_T]$ and $S_0$
- Changes risk-neutral probability $q^*$
- Impacts option valuation indirectly

**Change in Market Exposure ($\beta_i$):**
- Affects expected return $E[R_i]$
- Changes present value of stock
- Influences risk-neutral pricing

### Exam Strategies

1. **Identify pricing method** - Dynamic replication or risk-neutral
2. **Calculate $\Delta$** - Number of shares to hold
3. **Compute bond position** - Amount to borrow/lend
4. **Verify consistency** - Check both methods give same result
5. **Interpret results** - Understand economic meaning

### Common Pitfalls

- Confusing analyst probability $q$ with risk-neutral probability $q^*$
- Forgetting to discount bond position
- Using annual vs. continuous compounding incorrectly
- Not recognizing ATM vs. ITM/OTM options

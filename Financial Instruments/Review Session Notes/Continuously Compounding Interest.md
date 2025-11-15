---
title: Continuously Compounding Interest
aliases:
- Compound Interest
- Continuously Compounding
- Interest Rate Conversion
key_concepts:
- Annual interest rate
- Continuously compounding interest rate
- Derivative securities
- Discrete compounding frequency
- Exponential compounding
- Financial risk management
- Gross rate of return
- Interest rate conversion formulas
- LIBOR rate conversion
- Maturity horizon T
- Portfolio optimization
- Quantitative financial analysis
- Risk assessment and mitigation
tags:
- compounding-interest
- continuous-compounding
- discrete-compounding
- exam-prep
- financial-mathematics
- fixed-income
- gross-return
- interest-rate
- libor
- review-session
---

# Continuously Compounding Interest

## Key Concepts

### Overview
The LIBOR annual interest rate $r_d$ compounds at a **discrete frequency** (e.g., annually, semi-annually, monthly). In contrast, **continuously compounding** interest represents the limiting case as the compounding frequency approaches infinity.

**Key Insight:** The conversion between discrete and continuous compounding rates is **independent of the time horizon** $T$. This is a crucial property that simplifies many financial calculations.

### Discrete Compounding
- Interest is added at specific intervals
- Common frequencies: annual ($n=1$), semi-annual ($n=2$), quarterly ($n=4$), monthly ($n=12$)
- Formula: $(1 + \frac{r_d}{n})^{n \cdot T}$

### Continuous Compounding
- Interest is compounded continuously
- Mathematical limit as $n \to \infty$
- Formula: $e^{r_c \cdot T}$
- Where $e \approx 2.71828$ is the base of natural logarithm

## Formulas/Math

### Gross Rate of Return

**Discrete Compounding:**
$$\text{Gross Return} = \left(1 + \frac{r_d}{n}\right)^{n \cdot T}$$

Where:
- $r_d$ = discrete compounding interest rate
- $n$ = compounding frequency per year
- $T$ = time to maturity (in years)

**Continuous Compounding:**
$$\text{Gross Return} = e^{(r_c \cdot T)}$$

Where $r_c$ = continuously compounding interest rate

### Interest Rate Conversion Formula

To equate the two gross returns:

$$e^{(r_c \cdot T)} = \left(1 + \frac{r_d}{n}\right)^{n \cdot T}$$

**Solving for $r_c$:**

$$r_c = n \cdot \ln\left(1 + \frac{r_d}{n}\right)$$

**Critical Property:** The maturity $T$ **does not appear** in the conversion formula. This means:
- The relationship between $r_c$ and $r_d$ is **time-independent**
- The same conversion applies regardless of investment horizon
- You can convert rates without knowing the specific time period

## Examples

### Example 1: Converting Semi-Annual to Continuous

**Given:**
- Semi-annual rate: $r_d = 5\%$ (compounds twice per year)
- $n = 2$

**Calculation:**

$$r_c = 2 \cdot \ln\left(1 + \frac{0.05}{2}\right)$$

$$r_c = 2 \cdot \ln(1.025)$$

$$r_c = 2 \cdot 0.02469 = 0.04938 = 4.94\%$$

**Verification:**
- After 1 year, discrete: $(1.025)^2 = 1.050625$
- After 1 year, continuous: $e^{0.04938} = 1.050625$

**Result:** 5% semi-annually ≈ **4.94% continuously**

### Example 2: Converting Monthly to Continuous

**Given:**
- Monthly rate: $r_d = 6\%$ (compounds 12 times per year)
- $n = 12$

**Calculation:**

$$r_c = 12 \cdot \ln\left(1 + \frac{0.06}{12}\right)$$

$$r_c = 12 \cdot \ln(1.005)$$

$$r_c = 12 \cdot 0.0049875 = 0.05985 = 5.99\%$$

**Result:** 6% monthly ≈ **5.99% continuously**

### Example 3: Finding Discrete Rate from Continuous Rate

**Given:**
- Continuous rate: $r_c = 5\%$
- Compounding frequency: quarterly ($n = 4$)

**Rearrange the conversion formula:**

$$1 + \frac{r_d}{n} = e^{r_c / n}$$

$$\frac{r_d}{n} = e^{r_c / n} - 1$$

$$r_d = n \cdot (e^{r_c / n} - 1)$$

**Calculation:**

$$r_d = 4 \cdot (e^{0.05 / 4} - 1)$$

$$r_d = 4 \cdot (e^{0.0125} - 1)$$

$$r_d = 4 \cdot (1.012578 - 1) = 0.05031 = 5.03\%$$

**Result:** 5% continuously ≈ **5.03% quarterly**

## Study Points

### Key Formulas to Memorize

1. **Discrete to Continuous:**
   $$r_c = n \cdot \ln\left(1 + \frac{r_d}{n}\right)$$

2. **Continuous to Discrete:**
   $$r_d = n \cdot (e^{r_c / n} - 1)$$

3. **Time-Independent Property:**
   - Conversion formulas **do not depend on T**
   - Same conversion applies to any time period

### Common Compounding Frequencies

| Frequency | $n$ | Formula |
|-----------|-----|---------|
| Annual | 1 | $r_c = \ln(1 + r_d)$ |
| Semi-Annual | 2 | $r_c = 2 \cdot \ln(1 + r_d/2)$ |
| Quarterly | 4 | $r_c = 4 \cdot \ln(1 + r_d/4)$ |
| Monthly | 12 | $r_c = 12 \cdot \ln(1 + r_d/12)$ |
| Daily | 365 | $r_c = 365 \cdot \ln(1 + r_d/365)$ |

### Exam Tips

1. **Remember the time-independence** - Don't try to plug in T values
2. **Use natural log (ln)** - Not base-10 log
3. **Verify reasonableness** - Continuous rate should be **lower** than discrete rate
4. **Check for rounding** - Small differences due to calculator precision are normal

### Common Mistakes to Avoid

- Forgetting that T cancels out in the conversion
- Using log base 10 instead of natural log
- Confusing which rate is discrete vs. continuous
- Incorrectly solving for the wrong variable

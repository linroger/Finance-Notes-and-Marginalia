---
tags:
  - cpi
  - derivative_pricing
  - fixed_income
  - inflation_swap
  - risk_management
  - inflation_expectations
  - swap_valuation
aliases:
  - CPI
  - Consumer Price Index
  - IS
  - Inflation Swap
  - Inflation-linked derivatives
key_concepts:
  - CPI index
  - Fixed side payment
  - Floating side payout
  - Inflation swap contract
  - Swap valuation
  - Present value calculation
  - Discount factors
  - Inflation rate calculation
cssclasses: academia
---

# Pricing an Inflation Swap

## Summary

An inflation swap is a contract between two counterparties where at maturity, sides exchange a pre-specified payment determined by the inflation rate at inception for a payment determined by the simple rate of return of the Consumer Price Index (CPI) from inception to maturity.

## 1. Mathematical Formulation

At inception, counterparties of an inflation swap agree to exchange payments at maturity. The fixed side pays the contract notional amount:

$$\begin{array}{rl}
\mathcal{P}_{fixed}\left(t_{0}, T; r_{CPI}(t_{0}, T)\right) &= N\left\{ \left[1 + r_{CPI}(t_{0})\right]^{(T - t_{0})} - 1 \right\}\;,
\end{array}$$

Where:

$$\begin{array}{lll}
t_{0} & \cdot & \text{effective date,} \\
T & \cdot & \text{swap maturity (in years),} \\
r_{CPI}(t_{0}) & \cdot & \text{contract inflation rate from } t_{0} \text{ to } T \text{ specific at inception,} \\
\mathcal{P}_{fixed}\left(t, T; r_{CPI}(t_{0}, T)\right) & \cdot & \text{contract notional}.
\end{array}$$

The floating side pays the actual realized simple inflation rate adjustment based on the realized CPI at maturity:

$$P_{floating}(t_{0}, T) = N\left[ \frac{I(T)}{I(t_{0})} - 1 \right]\;,$$

Where:
- $I(t_{0})$ - CPI index at inception,
- $I(T)$ - CPI index at maturity,
- $P_{floating}(t, T)$ - floating side payout at $T$.

At inception, the inflation swap (IS) should value at par, i.e., the net value of both sides is zero. At time $t > t_{0}$, however, the value of the IS changes as the new expected inflation rate diverges from the contract rate and as the maturity of the swap approaches. If we were to enter (at par) a new IS at time $t$ with the same maturity $T$ as the original IS, the fixed side payout would be:

$$\begin{array}{rl}
\mathcal{P}_{fixed}\left(t, T; r_{CPI}(t, T)\right) &= N\left\{ \left[1 + r_{CPI}(t)\right]^{(T - t)} - 1 \right\}\;,
\end{array}$$

Using the same notation as in (1.1). Since the contract at $t$ is worth zero, the expectation at $t$ of the floating side payout at $T$ equals that of the fixed payout. From (1.2), we get:

$$I(T) = I(t) \left[ 1 + r_{CPI}(t, T) \right]^{(T - t)}\;.$$

This, in turn, allows us to compute the expected floating payout from (1.2) and (1.3) and substituting $t$ for $t_{0}$:

$$P_{floating}(t, T) = N\left\{ \frac{I(t)}{I(t_{0})} \left[ 1 + r_{CPI}(t, T) \right]^{(T - t)} - 1 \right\}\;.$$

The total value of the IS at $t$ is the difference between the floating and fixed sides present valued from $T$ back to $t$:

$$\begin{array}{rcl}
V(t, T) &=& \left[ P_{floating}(t, T) - P_{fixed}\left(t_{0}, T; r_{CPI}(t_{0}, T)\right) \right] \\
&\times& df(t, T) \delta_{pay\;fixed} \;,
\end{array}$$

Where:

$$\begin{array}{rll}
V(t, T) & \cdot & \text{value of IS at } t, \\
df(t, T) & \cdot & \text{discount factor associated with } T \text{ as seen at } t, \\
\delta_{pay\;fixed} &=& 
\begin{cases}
1, & \text{IS is pay-fixed}, \\
-1, & \text{otherwise}.
\end{cases}
\end{array}$$

If the counterparty to the IS is considered risk-free, discount factor $df(t, T)$ above is calculated using the usual swap discount curve. In the opposite case, an adjustment to the discount curve can be made by shocking the discount curve by its spread to a bond issued by this counterparty and maturing at (approximately) the same time as the IS.

## 2. Example

We consider a pay-fixed inflation swap effective 3/4/2008 and maturing on 3/4/2010. The swap was priced 3/7/2008 settling on 3/11/2007. The CPI for 12/31/2007 and 1/31/2008 were 210.036 and 211.08 respectively. Quoted IS rates for 3/7/2008 are presented in Table 1. The results are presented in Table 2.

### Table 1: IS Rate Quotes
!Table 1: IS Rate Quotes

!Table 1: IS Rate Quotes (continued).jpg)

### Table 2: LIBOR Quotes
!Table 2: LIBOR Quotes

### Table 3: Future Quotes
!Table 3: Future Quotes

### Table 4: Swap Quotes
!Table 4: Swap Quotes

### Table 5: ATM Implied Swaption Volatilities
!Table 5: ATM Implied Swaption Volatilities

For the corresponding interest rate volatilities, we have:

$$\sigma_{t+\tau, t+T}^{2} = \alpha^{2} \sigma_{t, T_{\text{short}}}^{2} + \beta^{2} \sigma_{t, T_{\text{long}}}^{2} + 2 \alpha \beta \sigma_{t, T_{\text{short}}} \sigma_{t, T_{\text{long}}} \rho_{t; \tau, T}\;,$$

Where $\sigma_{t_{1}+\delta t, t_{2}}$ is the implied forward swaption volatility at time $t_{1}$ of forward interest rate effective between $t_{1}+\delta t$ and $t_{2}$. The respective correlation coefficient is:

$$\rho_{t; \tau, T} = \frac{\sigma_{t+\tau, t+T}^{2} - \alpha^{2} \sigma_{t, T_{\text{short}}}^{2} - \beta^{2} \sigma_{t, T_{\text{long}}}^{2}}{2 \alpha \beta \sigma_{t, T_{\text{short}}} \sigma_{t, T_{\text{long}}}}\;.$$

## Appendix A: Calculation of Option Price and $\Delta$ in Example 1

The Black-Scholes equation for the call price yields:

$$\begin{array}{rcl}
c &=& S N(d_{1}) - K e^{-r T} N(d_{2})\;, \\
d_{1} &=& \displaystyle\frac{\ln\left(\frac{S}{K}\right) + \left(r + \frac{\sigma^{2}}{2}\right) T}{\sigma \sqrt{T}}\;, \\
d_{2} &=& d_{1} - \sigma \sqrt{T}\;, \\
N(x) &=& \displaystyle\frac{1}{\sqrt{2\pi}} \int_{-\infty}^{x} e^{-\frac{y^{2}}{2}} dy\;.
\end{array}$$

Where:
- $c$ - call price,
- $S$ - spot price of the underlying stock = $75,
- $N$ - cumulative distribution function of the standard normal distribution,
- $K$ - call strike = $80,
- $r$ - simple 3-month risk-free rate = 0.1% = 0.001,
- $T$ - time to option expiry in years = 0.25,
- $\sigma$ - volatility of the price of the underlying stock = 20% = 0.2.

Differentiating (A.1) - (A.4) with respect to $S$, we obtain:

$$\frac{\partial c}{\partial S} = \Delta = N(d_{1}).$$

Substituting the numbers from Example 1 into (A.1) - (A.4), we obtain $c = 1.22$ and $\Delta = 0.28$.

## References

[^1]: FINCAD Financial Corporation. Support and Reference, 2007. http://fincad.com/default.asp?id=17300&s=Support&n=References.
[^2]: P. Miron and P. Swannell. *Pricing and Hedging Swaps*. Euromoney Books, 1991.

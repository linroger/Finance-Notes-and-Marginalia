---
tags:
- arbitrage
- black-scholes-model
- black_scholes
- equity-derivatives
- european_call
- financial_mathematics
- geometric_brownian_motion
- interest-rate-derivatives
- ito-calculus
- markets
- mathematics
- option-greeks
- options
- options-pricing
- options_pricing
- pde
- quantitative-pricing
- risk-management
- risk_neutral_pricing
- stochastic
aliases:
- BS equation
- Black-Scholes model
- Option pricing derivation
- Black-Scholes-Merton model
key_concepts:
- Black-Scholes PDE
- Black-Scholes option pricing model
- Brownian motion and Wiener processes
- Delta hedging
- Delta hedging and Greeks calculation
- European call option
- Expected Shortfall (ES) and coherent risk measures
- Geometric Brownian motion
- Interest rate models and term structure
- Ito's Lemma and stochastic calculus
- Ito's lemma
- No-arbitrage principle
- Numerical methods for PDEs
- Portfolio optimization and mean-variance theory
- Risk-free rate
- Risk-neutral portfolio
- Risk-neutral valuation and martingale measures
- Underlying asset price
- Value at Risk (VaR) and risk metrics
cssclasses: academia
---


# Black-Scholes Derivation

To derive the Black-Scholes partial differential equation (PDE) from first principles, we start by considering a financial market where the price of an underlying asset follows a geometric Brownian motion. The goal is to determine the fair value of a European call option, which gives the holder the right to buy the asset at a specified strike price on a specific expiration date.

## Step 1: Define Variables and Assumptions

- **Underlying Asset Price ($S$):** The price of the asset at time $t$.
- **Option Price ($C$):** The price of a European call option at time $t$ when the underlying asset is priced at $S$.
- **Strike Price ($K$):** The price at which the holder of the option can buy the asset.
- **Expiration Time ($T$):** The time at which the option expires.
- **Risk-Free Rate ($r$):** The continuously compounded risk-free interest rate.
- **Volatility ($\sigma$):** The volatility of the underlying asset's returns, which measures the degree of randomness in the asset price.
- **Drift Rate ($\mu$):** The expected rate of return of the underlying asset.

## Step 2: Model the Underlying Asset Price

Assume that the price of the underlying asset follows a geometric Brownian motion:

$$dS = \mu S dt + \sigma S dW$$

Where:
- $dS$ is the change in the asset price over a small time interval $dt$.
- $dW$ is a Wiener process, representing the random component of the asset price movement.

## Step 3: Formulate a Risk-Neutral Portfolio

To eliminate risk, we construct a portfolio consisting of one call option and $\Delta$ shares of the underlying asset. The value of this portfolio is:

$$\Pi = C - \Delta S$$

The goal is to choose $\Delta$ such that the portfolio is risk-neutral, meaning it has no exposure to random price movements of the underlying asset.

## Step 4: Calculate the Change in Portfolio Value

Using a Taylor series expansion, we approximate the change in the call option price $C$ over a small time interval $dt$:

$$dC = \frac{\partial C}{\partial S} dS + \frac{\partial C}{\partial t} dt + \frac{1}{2}\frac{\partial[^2] C}{\partial S[^2]}(dS)[^2]$$

Substituting the expression for $dS$ and noting that $(dS)[^2] = \sigma[^2] S[^2] dt$ (using Ito's lemma):

$$dC = \frac{\partial C}{\partial S} (\mu S dt + \sigma S dW) + \frac{\partial C}{\partial t} dt + \frac{1}{2}\frac{\partial[^2] C}{\partial S[^2]}\sigma[^2] S[^2] dt$$

The change in the portfolio value $d\Pi$ is:

$$d\Pi = dC - \Delta dS$$

Substituting $dC$ and $dS$:

$$d\Pi = \left(\frac{\partial C}{\partial S} (\mu S dt + \sigma S dW) + \frac{\partial C}{\partial t} dt + \frac{1}{2}\frac{\partial[^2] C}{\partial S[^2]}\sigma[^2] S[^2] dt\right) - \Delta (\mu S dt + \sigma S dW)$$

## Step 5: Eliminate Random Component

To make the portfolio risk-neutral, we set $\Delta = \frac{\partial C}{\partial S}$. This eliminates the random component $dW$:

$$d\Pi = \left(\frac{\partial C}{\partial S} (\mu S dt) + \frac{\partial C}{\partial t} dt + \frac{1}{2}\frac{\partial[^2] C}{\partial S[^2]}\sigma[^2] S[^2] dt\right) - \frac{\partial C}{\partial S} (\mu S dt)$$

Simplifying:

$$d\Pi = \frac{\partial C}{\partial t} dt + \frac{1}{2}\frac{\partial[^2] C}{\partial S[^2]}\sigma[^2] S[^2] dt$$

## Step 6: Equate Portfolio Return to Risk-Free Rate

In a risk-neutral world, the return on the portfolio should equal the risk-free rate:

$$d\Pi = r \Pi dt$$

Substituting $\Pi = C - \Delta S$ and $\Delta = \frac{\partial C}{\partial S}$:

$$\frac{\partial C}{\partial t} dt + \frac{1}{2}\frac{\partial[^2] C}{\partial S[^2]}\sigma[^2] S[^2] dt = r \left(C - \frac{\partial C}{\partial S}S\right) dt$$

Dividing both sides by $dt$:

$$\frac{\partial C}{\partial t} + \frac{1}{2}\frac{\partial[^2] C}{\partial S[^2]}\sigma[^2] S[^2] = r \left(C - \frac{\partial C}{\partial S}S\right)$$

## Step 7: Finalize the Black-Scholes PDE

Rearranging the terms, we arrive at the Black-Scholes partial differential equation:

$$\frac{\partial C}{\partial t} + \frac{1}{2} \sigma[^2] S[^2] \frac{\partial[^2] C}{\partial S[^2]} + rS \frac{\partial C}{\partial S} - rC = 0$$

This PDE describes how the price of a European call option changes with respect to time and the underlying asset price, considering the effects of volatility, risk-free rate, and time decay.

## Step 8: Solving the Black-Scholes PDE

To solve the PDE, we use a transformation to simplify it. Define:

$$\tau = T - t$$
$$x = \ln\left(\frac{S}{K}\right)$$

With appropriate boundary conditions:
- At expiration $t = T$, the option price is $C(S, T) = \max(S - K, 0)$.
- As $S \to 0$, the option price $C(S, t) \to 0$.
- As $S \to \infty$, the option price $C(S, t) \sim S - Ke^{-r(T-t)}$.

The solution to the Black-Scholes PDE is:

$$C(S, t) = SN(d_1) - Ke^{-r(T-t)}N(d_2)$$

Where:
- $d_1 = \frac{\ln\left(\frac{S}{K}\right) + \left(r + \frac{1}{2}\sigma[^2]\right)(T-t)}{\sigma\sqrt{T-t}}$
- $d_2 = d_1 - \sigma\sqrt{T-t}$
- $N(\cdot)$ is the cumulative distribution function of the standard normal distribution.

## Summary

By constructing a risk-neutral portfolio and ensuring its return matches the risk-free rate, we derived the Black-Scholes PDE. This equation is fundamental in options pricing and forms the basis for the Black-Scholes-Merton model, which revolutionized financial derivatives pricing.

The Black-Scholes formula provides the fair value of a European call option under the assumptions of constant volatility, no dividends, and continuous trading without transaction costs.

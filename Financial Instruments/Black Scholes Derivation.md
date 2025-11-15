---
academic_level: graduate
aliases:
- BS equation
- Black-Scholes model
- Option pricing derivation
- Black-Scholes-Merton model
cssclasses: academia
enhanced: true
enhancement_date: '2025-11-06'
enhancement_id: batch09-000133
key_concepts:
- Black-Scholes option pricing model and continuous-time finance
- Options Greeks and sensitivity analysis for risk management
- Delta hedging and dynamic replication strategies
- Risk-neutral measures and martingale pricing
- Ito's lemma and stochastic calculus applications
- Wiener process and Brownian motion modeling
- Martingale theory and change of measure
- Duration analysis and interest rate risk management
- Convexity adjustments and yield curve sensitivity
- Capital Asset Pricing Model (CAPM) and expected returns
- Credit default swaps (CDS) and credit risk modeling
- Value at Risk (VaR) and tail risk measurement
- Expected shortfall and coherent risk measures
- Collateralized debt obligations (CDO) and tranche structure
- Arbitrage opportunities and no-arbitrage pricing
- Factor models and multi-factor pricing
- Volatility modeling and estimation techniques
- Risk preference theory and utility functions
- Sensitivity analysis and Greeks calculation
- Ito's Lemma and Lognormal Asset Price Dynamics
- Risk-Neutral Valuation in Option Pricing
- Value at Risk and Expected Shortfall
- Vasicek Interest Rate Model and Mean Reversion
- Short Rate Models and Term Structure Dynamics
- Credit Risk Management and Default Probability
- Expected Loss and Loss Given Default Models
- 'Greeks: Delta, Gamma, Theta, and Vega Hedging'
- Ornstein-Uhlenbeck Process in Finance
- Black-Scholes Option Pricing Model and Its Applications
- Options Trading Strategies and Risk Management
- Stress Testing and Extreme Value Analysis
- Fama-French Factors and Style Analysis
- Risk Measurement and VaR Backtesting
- Contango, Backwardation, and Roll Yield
- Futures and Forward Contracts in Financial Markets
- Hedge Strategies and Basis Risk Management
- Option Valuation and Exercise Strategies
- Credit Spreads and Rating Migration Analysis
- Factor Models and Asset Pricing
- Arbitrage Pricing Theory and Multi-Factor Models
professional_application: theoreti
status: active
tags:
- arbitrage-opportunity
- arbitrage-pricing
- asset-allocation
- binomial-model
- black-scholes-model
- brownian-motion
- capital-asset-pricing
- caplet
- cds
- coherent-risk-measure
- collateralized-debt-obligation
- conditional-var
- continuous-time-pricing
- convexity-adjustment
- counterparty-risk
- hull-white
- call-options
- cir-model
- butterfly-spreads
- expected-shortfall
- straddles
- extreme-value-theory
- book-to-market
- partial-differential-equation
- risk-neutral-valuation
- backwardation
- volatility-analysis
- style-analysis
- option-strategies
- unexpected-loss
- clearinghouse
- arbitrage-pricing-theory
- hedge-ratio
- market-price-of-risk
- volatility-surface
- loss-given-default
- value-factor
- vasicek-model
- monte-carlo-var
- options-trading
- forward-contracts
- fama-french
- bsm-model
- recovery-rate
- black-scholes-formula
- parametric-var
- lognormal-models
- var-methodologies
- historical-var
- mean-reversion
- contango
- expected-loss
- quantitative-finance
- protective-puts
- probabilty-of-default
- roll-yield
- risk-premium
- put-options
- affine-term-structure
- momentum
- basis-risk
- covered-calls
- ' exposure-at-default'
- stress-testing
- mathematical-finance
- ornstein-uhlenbeck
- rating-migration
- investment-analysis
- portfolio-optimization
- value-at-risk
- factor-models
- risk-management
- convergence
- var-backtesting
- european-options
- strangles
- short-rate-models
- credit-migration
- default-probability
- marking-to-market
- credit-spreads
- multi-factor-models
- ito-calculus
- iron-condors
- option-pricing
- financial-markets
- size-effect
- lognormal-distribution
- futures-contracts
- apt
type: note
---
--



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

$$dC = \frac{\partial C}{\partial S} dS + \frac{\partial C}{\partial t} dt + \frac{1}{2}\frac{\partial^2 C}{\partial S^2}(dS)^2$$

Substituting the expression for $dS$ and noting that $(dS)^2 = \sigma^2 S^2 dt$ (using Ito's lemma):

$$dC = \frac{\partial C}{\partial S} (\mu S dt + \sigma S dW) + \frac{\partial C}{\partial t} dt + \frac{1}{2}\frac{\partial^2 C}{\partial S^2}\sigma^2 S^2 dt$$

The change in the portfolio value $d\Pi$ is:

$$d\Pi = dC - \Delta dS$$

Substituting $dC$ and $dS$:

$$d\Pi = \left(\frac{\partial C}{\partial S} (\mu S dt + \sigma S dW) + \frac{\partial C}{\partial t} dt + \frac{1}{2}\frac{\partial^2 C}{\partial S^2}\sigma^2 S^2 dt\right) - \Delta (\mu S dt + \sigma S dW)$$

## Step 5: Eliminate Random Component

To make the portfolio risk-neutral, we set $\Delta = \frac{\partial C}{\partial S}$. This eliminates the random component $dW$:

$$d\Pi = \left(\frac{\partial C}{\partial S} (\mu S dt) + \frac{\partial C}{\partial t} dt + \frac{1}{2}\frac{\partial^2 C}{\partial S^2}\sigma^2 S^2 dt\right) - \frac{\partial C}{\partial S} (\mu S dt)$$

Simplifying:

$$d\Pi = \frac{\partial C}{\partial t} dt + \frac{1}{2}\frac{\partial^2 C}{\partial S^2}\sigma^2 S^2 dt$$

## Step 6: Equate Portfolio Return to Risk-Free Rate

In a risk-neutral world, the return on the portfolio should equal the risk-free rate:

$$d\Pi = r \Pi dt$$

Substituting $\Pi = C - \Delta S$ and $\Delta = \frac{\partial C}{\partial S}$:

$$\frac{\partial C}{\partial t} dt + \frac{1}{2}\frac{\partial^2 C}{\partial S^2}\sigma^2 S^2 dt = r \left(C - \frac{\partial C}{\partial S}S\right) dt$$

Dividing both sides by $dt$:

$$\frac{\partial C}{\partial t} + \frac{1}{2}\frac{\partial^2 C}{\partial S^2}\sigma^2 S^2 = r \left(C - \frac{\partial C}{\partial S}S\right)$$

## Step 7: Finalize the Black-Scholes PDE

Rearranging the terms, we arrive at the Black-Scholes partial differential equation:

$$\frac{\partial C}{\partial t} + \frac{1}{2} \sigma^2 S^2 \frac{\partial^2 C}{\partial S^2} + rS \frac{\partial C}{\partial S} - rC = 0$$

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

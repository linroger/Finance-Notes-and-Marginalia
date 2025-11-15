---
academic_level: graduate
aliases:
- Arithmetic Mean vs Geometric Mean
- Continuously Compounded Return
- Arithmetic vs Geometric Return
cssclasses: academia
enhanced: true
enhancement_date: '2025-11-06'
enhancement_id: batch09-000078
key_concepts:
- Black-Scholes option pricing model and continuous-time finance
- Binomial option pricing model and lattice methods
- Options Greeks and sensitivity analysis for risk management
- Ito's lemma and stochastic calculus applications
- Wiener process and Brownian motion modeling
- Duration analysis and interest rate risk management
- Convexity adjustments and yield curve sensitivity
- Value at Risk (VaR) and tail risk measurement
- Expected shortfall and coherent risk measures
- Arbitrage opportunities and no-arbitrage pricing
- Volatility modeling and estimation techniques
- Risk preference theory and utility functions
- Sensitivity analysis and Greeks calculation
- Value at Risk and Expected Shortfall
- Vasicek Interest Rate Model and Mean Reversion
- Short Rate Models and Term Structure Dynamics
- Variance Reduction Techniques in Monte Carlo Methods
- Credit Risk Management and Default Probability
- Expected Loss and Loss Given Default Models
- Swap Market Mechanisms and Pricing
- 'Greeks: Delta, Gamma, Theta, and Vega Hedging'
- Ornstein-Uhlenbeck Process in Finance
- Stochastic Integration and Path-Dependent Options
- Options Trading Strategies and Risk Management
- Stress Testing and Extreme Value Analysis
- Lattice Methods and Recombining Trees in Derivatives Pricing
- Credit Default Swaps and Credit Risk Transfer
- Fama-French Factors and Style Analysis
- Risk Measurement and VaR Backtesting
- Contango, Backwardation, and Roll Yield
- Futures and Forward Contracts in Financial Markets
- Factor Models and Asset Pricing
- Binomial Option Pricing Model for Discrete Time Valuation
- Hedge Strategies and Basis Risk Management
- American Option Pricing and Early Exercise Premium
- Interest Rate Swaps and Currency Swap Structures
- Option Valuation and Exercise Strategies
- Credit Spreads and Rating Migration Analysis
- Monte Carlo Simulation Methods for Derivative Pricing
- Arbitrage Pricing Theory and Multi-Factor Models
professional_application: theoreti
status: active
tags:
- arbitrage-opportunity
- binomial-model
- black-scholes-model
- brownian-motion
- coherent-risk-measure
- collateral-rates
- conditional-var
- continuous-time-pricing
- convexity-adjustment
- credit-rating
- delta-hedging
- derivatives
- discrete-time-pricing
- duration-analysis
- dynamic-hedging
- control-variates
- exotic-options
- hull-white
- call-options
- cir-model
- butterfly-spreads
- expected-shortfall
- binomial-tree
- straddles
- extreme-value-theory
- american-options
- book-to-market
- backwardation
- volatility-analysis
- style-analysis
- option-strategies
- unexpected-loss
- clearinghouse
- overnight-indexed-swaps
- arbitrage-pricing-theory
- monte-carlo-simulation
- hedge-ratio
- market-price-of-risk
- loss-given-default
- value-factor
- vasicek-model
- monte-carlo-var
- options-trading
- forward-contracts
- fama-french
- recovery-rate
- parametric-var
- lognormal-models
- var-methodologies
- historical-var
- mean-reversion
- contango
- random-walks
- expected-loss
- quantitative-finance
- currency-swaps
- crr-model
- protective-puts
- probabilty-of-default
- roll-yield
- risk-premium
- put-options
- affine-term-structure
- multi-period-binomial
- momentum
- basis-risk
- antithetic-variates
- covered-calls
- swap-rate
- sofr
- ' exposure-at-default'
- stress-testing
- mathematical-finance
- ornstein-uhlenbeck
- rating-migration
- path-dependency
- value-at-risk
- factor-models
- risk-management
- convergence
- var-backtesting
- stochastic-integration
- variance-reduction
- lattice-models
- strangles
- cox-ross-rubinstein
- short-rate-models
- least-squares-mc
- swap-spread
- optional-exercise
- credit-migration
- default-probability
- marking-to-market
- binomial-option-pricing
- total-return-swaps
- libor
- credit-spreads
- multi-factor-models
- iron-condors
- size-effect
- basis-swaps
- interest-rate-swaps
- ' recombining-trees'
- futures-contracts
- quasi-monte-carlo
- apt
- credit-default-swaps
title: Arithmetic and Geometric Rates of Return
type: note
---
--



# Arithmetic and Geometric Rates of Return

We now consider $\mu$ and $\nu$ again. Suppose we have an asset worth 100 and for two successive periods it increases by $20\%$. Then the value at the end of the first period is 120 and the value at the end of the second period is 144.

Now suppose that instead the asset increases in the first period by $30\%$ and in the second period by $10\%$. The average or arithmetic mean of the return is $20\%$. However, the value of the asset is 130 at the end of the first period and 143 at the end of the second period. The variability of the return has meant that the asset is worth less after two periods even though the average return is the same. We can calculate the equivalent per period return that would give the same value of 143 after two periods if there were no variance in the returns. That is the value $\nu$ that satisfies
$$143=100 (1+\nu)[^2].$$

This value is known as the geometric mean. It is another measure of the average return over the two periods. Solving this equation gives the geometric mean as $\nu=0.195826$ or $19.58\%$ per period which is less than the arithmetic rate of return per period.

There is a simple relationship between the arithmetic mean return, the geometric mean return, and the variance of the return. Let $\mu_{1}=\mu+\sigma$ be the rate of return in the first period and let $\mu_{2}=\mu-\sigma$ be the rate of return in the second period. Here the average rate of return is $\frac{1}{2}(\mu_{1}+\mu_{2})=\mu$ and the variance of the two rates is $\sigma^{2}$. The geometric rate of return $\nu$ satisfies $(1+\nu)^{2}=(1+\mu_{1})(1+\mu_{2})$. Substituting and expanding this gives:
$$1+2\nu+\nu[^2]=(1+\mu+\sigma)(1+\mu-\sigma)=(1+\mu)[^2]-\sigma[^2]=1+2\mu+\mu[^2]-\sigma[^2]$$

Or
$$\nu=\mu-\frac{1}{2}\sigma^{2}+\frac{1}{2}(\mu^{2}-\nu^{2}).$$

Since rates of return are typically less than one, the square of the return is even smaller and hence the difference between two squared percentage terms is smaller still. Hence we have the approximation $\nu\approx\mu-\frac{1}{2}\sigma^{2}$ or:
$$\mathrm{geometric~mean}\approx\mathrm{arithmetic~mean}-\frac{1}{2}\mathrm{variance}.$$

This approximation will be better the smaller the interest rates and the smaller the variance. In the example, $\mu=0.2$ and $\sigma=0.1$, so $\frac{1}{2}\sigma^{2}=0.005$ and $\mu-\frac{1}{2}\sigma^{2}=0.1950$, which is close to the actual geometric mean of 0.1958. Thus, the difference between $\mu$ and $\nu$ is that $\nu$ is the geometric rate of return, and $\mu$ is the arithmetic rate of return. It is quite usual to use the arithmetic rate and therefore to write that the expected value of the logarithm of the stock price satisfies:
$$\operatorname{E}[\ln S_T]=\ln S_0+\left (\mu-\frac{1}{2}\sigma[^2]\right) T$$

And
$$\mathrm{Var}[\ln S_T]=\sigma[^2] T.$$

### Continuously Compounded Rate of Return

The value $\nu$ is the continuously compounded rate of return. It is given by:
$$\nu=\frac{1}{T}[\ln S_{T}-\ln S_{0}].$$

Hence, taking expectations, we can calculate:
$$\mathrm{E}[\nu]=\frac{1}{T}\mathrm{E}[\ln S_{T}-\ln S_{0}]=\frac{1}{T}\left (\mathrm{E}[\ln S_{T}]-\ln S_{0}\right)=\mu-\frac{\sigma^{2}}{2}.$$

Similarly, the variance satisfies:
$$\mathrm{Var}[\nu]=\frac{1}{T^{2}}\mathrm{Var}[\ln S_{T}-\ln S_{0}]=\frac{1}{T^{2}}\mathrm{Var}[\ln S_{T}]=\frac{\sigma^{2}T}{T^{2}}=\frac{\sigma^{2}}{T}.$$

Hence, the standard deviation of $\nu$ is simply $\sigma/{\sqrt{T}}$.

### A Wiener Process

We will now consider the stochastic process in more detail and see how to take limits as the length of the time interval goes to zero. This will produce a continuous-time stochastic process.

Consider a variable $z$ which takes on values at discrete points in time $t=0, 1, \ldots, T$ and suppose that $z$ evolves according to the following rule:
$$z_{t+1}=z_{t}+\epsilon;\quad z_{0}\quad\mathrm{fixed}$$

Where $\epsilon$ is a random drawing from a standardized normal distribution, that is, with mean of zero and variance of one. The draws are assumed to be independently distributed. This represents a random walk where on average $z$ remains unchanged each period but where the standard deviation of the realized value is one each period. At date $t=0$, we have $E[z_{T}]=z_{0}$ and the variance $Var[z_{T}]=T$ as the draws are independent.

Now divide the periods into $T/\Delta t$ subperiods, each of length $\Delta t$. To keep the process equivalent, the variance in the shock must also be reduced so that the standard deviation is $\sqrt{\Delta t}$. The resulting process is known as a Wiener process. The Wiener process has two important properties:

Property 1: The change in $z$ over a small interval of time satisfies:
$$z_{t+\Delta t}=z_{t}+\epsilon\sqrt{\Delta t}.$$

Then, as of time $t=0$, it is still the case that $E[z_{T}] = z_{0}$ and the variance $Var[z_{T}]=T$. This relation may be written:
$$\Delta z(t+\Delta t)=\epsilon\sqrt{\Delta t}$$

Where $\Delta z(t+\Delta t)=z_{t+\Delta t}-z_{t}$. This has an expected value of zero and standard deviation of $\sqrt{\Delta t}$.

Property 2: The values of $\Delta z$ for any two different short intervals of time are independent.

It follows from this that:
$$z(T) - z(0)=\sum_{i=1}^N\epsilon_i\sqrt{\Delta t}$$

Where $N=T/\Delta t$ is the number of time intervals between 0 and $T$. Hence, we have:
$$\mathrm{E}[z(T)]=z(0)$$

And
$$\mathrm{Var}[z(T)]=N\Delta t=T$$

Or the standard deviation of $z(T)$ is $\sqrt{T}$.

Now consider what happens in the limit as $\Delta t\to 0$, that is, as the length of the interval becomes an infinitesimal $dt$. We replace $\Delta z(t+\Delta t)$ by $dz(t)$, which has a mean of zero and standard deviation of $\sqrt{dt}$. This continuous time stochastic process is also known as Brownian Motion after its use in physics to describe the motion of particles subject to a large number of small molecular shocks.

This process is easily generalized to allow for a non-zero mean and arbitrary standard deviation. A generalized Wiener process for a variable $x$ is defined in terms of $dz(t)$ as follows:
$$dx = adt + bdz$$

where $a$ and $b$ are constants. This formula for the change in the value of $x$ consists of two components:
1. A deterministic component $adt$
2. A stochastic component $bdz(t)$

The deterministic component is $dx = adt$ or $\frac{dx}{dt} = a$ which shows that $x = x_0 + at$ so that $a$ is simply the trend term for $x$. Thus the expected increase in the value of $x$ over one time period is $a$. 

The stochastic component $bdz(t)$ adds noise or variability to the path for $x$. The amount of variability added is $b$ times the Wiener process. Since the Wiener process has a standard deviation of one, the generalized process has a standard deviation of $b$.

### The Asset Price Process

Remember that we have:
$$\ln S_{t+1}-\ln S_t=\omega_t$$

Where $\omega_t$ are independent random variables with mean $\nu$ and standard deviation of $\sigma$. The continuous time version of this equation is therefore:
$$d\ln S(t)=\nu\,dt+\sigma\,dz$$

Where $z$ is a standard Wiener process. The right-hand-side of the equation is just a random variable that is evolving through time. The term $\nu$ is called the drift parameter and the standard deviation of the continuously compounded rate of return is $\sqrt{\mathrm{Var}[r(t)]}=\sigma\sqrt{\Delta t}$. The term $\sigma$ is referred to as the volatility of the asset return.

### Ito Calculus

We have written the process in terms of $\ln S(t)$ rather than $S(t)$ itself. This is convenient and shows the connection to the binomial model. However, it is usual to think in terms of $S(t)$ itself too. In ordinary calculus, we know that:
$$d\ln S(t)=\frac{dS(t)}{S(t)}.$$

Thus, we might think that $\frac{dS(t)}{S(t)} = \nu\,dt + \sigma\,dz$. But this would be WRONG. The correct version is:
$$\frac{dS(t)}{S(t)}=\left(\nu+\frac{1}{2}\sigma[^2]\right)\,dt+\sigma\,dz.$$

This is a special case of Ito's lemma. Ito's lemma shows that for any process of the form
$$dx=a (x,    t) dt+b (x,    t) dz$$

Then the function $G (x,    t)$ follows the process
$$dG=\left (\frac{\partial G}{\partial x}a (x,    t)+\frac{\partial G}{\partial t}+\frac{1}{2}\frac{\partial[^2] G}{\partial x[^2]}b[^2] (x,    t)\right) dt+\frac{\partial G}{\partial x}b (x,    t) dz.$$

We'll see how to use Ito's lemma. We have
$$d\:\ln S (t)=\nu\:dt+\sigma\: dz.$$

Then let $\ln S (t)=x (t)$ s 0 $s (T)=G (x,    t)=e^{x}$ . Then upon differentiating
$$\frac{\partial G}{\partial x}=e^x=S,    \quad\frac{\partial[^2] G}{\partial S[^2]}=e^x=S,    \quad\frac{\partial G}{\partial t}=0.$$

Hence,  using Ito's lemma
$$dS (t)=(\nu S (t)+0+\frac{1}{2}\sigma^{2}S (t)) dt+\sigma S (t)\:dz$$

Or
$$d\: S (t)=(\nu+\frac 12\sigma[^2]) S (t)\:dt+\sigma S (t)\:dz$$

Since $\mu=\nu+\frac{1}{2}\sigma^{2}$ we can write this as
$$d\: S (t)=\mu S (t)\:dt+\sigma S (t)\: dz.$$

This process is known as geometric Brownian motion as it is the rate of change which is Brownian motion. Thus sometimes the above equation is written as
$$\begin{aligned}\frac{d\: S (t)}{S (t)}=\mu\:dt+\sigma\: dz.\end{aligned}$$

We can also do the same calculation the other way around. Suppose that we start from the process
$$ds (t)=\mu S (t)\:dt+\sigma S (t)\: dz.$$

Now consider the function $G (S)=\ln S$ . Differentiating we have
$$\frac{\partial G}{\partial S}=1,    \quad\frac{\partial[^2] G}{\partial S[^2]}=-\frac{1}{S[^2]},    \quad\frac{\partial G}{\partial t}=0.$$

Hence substituting into Ito's lemma we get.
$$dG=d\ln S (t)=\left (\mu-\frac{1}{2}\sigma[^2]\right)\:dt+\sigma\: dz.$$

### The forward price

As we have seen before the forward price just depends on the current price of the underlying,  the interest rate,  and the time to expiration. With continuous compounding we can write the forward price equation as
$$F (S (t),    t)=S (t) e^{r (T-t)}.$$

This shows the forward price is a stochastic process%20Process.md) which depends on the price of the underlying asset which itself is a stochastic process%20Process.md). Since we have

That the forward price is a function of a stochastic process%20Process.md) we can use Ito's lemma. Upon differentiation we have
$$\frac{\partial F}{\partial S}=e^{r (T-t)};\quad\frac{\partial F}{\partial t}=-rS (t) e^{r (T-t)};\quad\frac{\partial[^2] F}{\partial S[^2]}=0.$$

Hence substituting into Ito's lemma
$$\begin{aligned}dF&=\left (e^{r (T-t)}\mu S (t)-rS (t) e^{r (T-t)}\right) dt+\sigma S (t) e^{r (T-t)}dz\\&=(\mu-r) S (t) e^{r (T-t)}\sigma S (t) e^{r (T-t)}dz\\&=(\mu-r) F (t) dt+\sigma F (t) dz.\end{aligned}$$

This shows that the forward price also follows a geometric Brownian motion process with expected return given by the risk premium on the underlying $\mu-r$ and volatility 0 (the same as the underlying asset).

## Summary

We have shown how returns are continuously compounded and introduced the geometric Brownian motion process for stock prices. We have shown how Ito's lemma can be used. The next thing to do will be to show how to use the assumption of geometric Brownian motion to price an option or derivative using Ito's lemma.

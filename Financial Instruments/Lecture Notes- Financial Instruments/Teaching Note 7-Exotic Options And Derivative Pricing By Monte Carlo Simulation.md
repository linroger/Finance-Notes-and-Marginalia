---
academic_level: graduate
aliases:
- John Heaton
- Monte Carlo
- Risk Neutral
- Teaching Note 7
enhanced: true
enhancement_date: '2025-11-06'
enhancement_id: batch09-000139
key_concepts:
- Black-Scholes option pricing model and continuous-time finance
- Monte Carlo simulation for derivatives pricing and risk management
- Options Greeks and sensitivity analysis for risk management
- Risk-neutral measures and martingale pricing
- Martingale theory and change of measure
- Duration analysis and interest rate risk management
- Convexity adjustments and yield curve sensitivity
- Value at Risk (VaR) and tail risk measurement
- Expected shortfall and coherent risk measures
- Arbitrage opportunities and no-arbitrage pricing
- Volatility modeling and estimation techniques
- Risk preference theory and utility functions
- Sensitivity analysis and Greeks calculation
- 'Valuation Methods: DCF, Comps, and Precedents'
- Auto-Callable Notes and Barrier Options
- Ito's Lemma and Lognormal Asset Price Dynamics
- Risk-Neutral Valuation in Option Pricing
- Value at Risk and Expected Shortfall
- Vasicek Interest Rate Model and Mean Reversion
- Short Rate Models and Term Structure Dynamics
- Company Valuation and Multiple Analysis
- Variance Reduction Techniques in Monte Carlo Methods
- Credit Risk Management and Default Probability
- Expected Loss and Loss Given Default Models
- Equity-Linked Notes and Market-Linked Securities
- Comparable Company Analysis and Trading Multiples
- 'Greeks: Delta, Gamma, Theta, and Vega Hedging'
- Ornstein-Uhlenbeck Process in Finance
- Price Discovery and Market Efficiency
- Stochastic Integration and Path-Dependent Options
- Black-Scholes Option Pricing Model and Its Applications
- Structured Products and Principal Protection
- Options Trading Strategies and Risk Management
- Stress Testing and Extreme Value Analysis
- Lattice Methods and Recombining Trees in Derivatives Pricing
- Fama-French Factors and Style Analysis
- Risk Measurement and VaR Backtesting
- Bid-Ask Spreads and Market Impact
- Factor Models and Asset Pricing
- Binomial Option Pricing Model for Discrete Time Valuation
- American Option Pricing and Early Exercise Premium
- Option Valuation and Exercise Strategies
- Market Microstructure and Liquidity Analysis
- Credit Spreads and Rating Migration Analysis
- Monte Carlo Simulation Methods for Derivative Pricing
- Arbitrage Pricing Theory and Multi-Factor Models
linter-yaml-title-alias: Teaching Note 7  Exotic Options  and Derivative Pricing by
  Monte Carlo Simulation
professional_application: theoreti
status: active
tags:
- arbitrage-opportunity
- asian-derivatives
- average-price-options
- barrier-derivatives
- barrier-options
- binomial-model
- black-scholes-model
- caplet
- coherent-risk-measure
- conditional-var
- continuous-time-pricing
- convexity-adjustment
- credit-rating
- delta-hedging
- derivatives
- control-variates
- leveraged-buyout
- exotic-options
- hull-white
- call-options
- cir-model
- butterfly-spreads
- dcf-analysis
- expected-shortfall
- binomial-tree
- straddles
- extreme-value-theory
- american-options
- partial-differential-equation
- book-to-market
- arbitrage
- risk-neutral-valuation
- volatility-analysis
- style-analysis
- option-strategies
- unexpected-loss
- arbitrage-pricing-theory
- monte-carlo-simulation
- market-price-of-risk
- volatility-surface
- price-discovery
- loss-given-default
- value-factor
- vasicek-model
- monte-carlo-var
- options-trading
- market-impact
- fama-french
- price-to-earnings
- bsm-model
- recovery-rate
- black-scholes-formula
- parametric-var
- lognormal-models
- var-methodologies
- historical-var
- mean-reversion
- random-walks
- expected-loss
- market-efficiency
- quantitative-finance
- order-flow
- market-linked-notes
- bid-ask-spread
- crr-model
- protective-puts
- probabilty-of-default
- liquidity
- reverse-convertibles
- risk-premium
- put-options
- affine-term-structure
- multi-period-binomial
- algorithmic-trading
- momentum
- discrete-time-pricing
- antithetic-variates
- covered-calls
- ' exposure-at-default'
- stress-testing
- mathematical-finance
- ornstein-uhlenbeck
- rating-migration
- comparable-analysis
- investment-analysis
- economic-value-added
- path-dependency
- value-at-risk
- factor-models
- risk-management
- var-backtesting
- variance-reduction
- stochastic-integration
- sum-of-parts
- european-options
- high-frequency-trading
- principal-protected-notes
- lattice-models
- strangles
- equity-linked-notes
- cox-ross-rubinstein
- short-rate-models
- least-squares-mc
- optional-exercise
- credit-migration
- default-probability
- binomial-option-pricing
- auto-callables
- credit-spreads
- multi-factor-models
- ito-calculus
- trading-multiples
- structured-notes
- iron-condors
- option-pricing
- financial-markets
- size-effect
- precedent-transactions
- knock-out-options
- lognormal-distribution
- ipo-valuation
- market-multiple
- ' recombining-trees'
- quasi-monte-carlo
- apt
title: Teaching Note 7- Exotic Options  And Derivative Pricing By Monte Carlo Simulation
type: course-note
---
--



# Teaching Note 7- Exotic Options  And Derivative Pricing By Monte Carlo Simulation

John Heaton
The University of Chicago
Booth School of Business

### 1. Risk Neutral Trees and Monte Carlo Simulations
1.1 One Step tree
1.2 Multi-Step Tree
1.3 Why Monte Carlo Simulations?

### 2. Monte Carlo Simulations without Trees
2.1 Lognormal Model
2.2 Multi Factors
2.3 Delta Calculation

## Risk Neutral Trees

- Consider again a one-step tree (to begin with).
- Assume $S_{0}=100$,  $K=100$,  $I^{\prime}=1$,  $r=2\%$,  $\sigma=30\%$
- Given that $u=e^{\sigma\sqrt T}=1.34986$,  the price of any derivative security with payoff $V(S_{1})$ can be computed as:$$V_0=E^*\left[e^{-rT}V(S_1)\right]=e^{-rT}\left[q^*V(S_{1,          u})+(1-q^*)V(S_{1,          d})\right]$$

- For instance,  a call option has price given by
!Image

### Monte Carlo Simulations on the Risk Neutral Trees
- An alternative way of computing the expected future payoff is to simulate up and down movements using a computer.
- For instance,  in Excel the function `RAND()` simulates a uniform between $\left[0,  1\right]`.
  - Thus,  $RAND()>q^{*}$ occurs with probability $(1-q^{*})$,  and vice versa (e.g $q^{*}=1$ implies that $(1-q^{*})=0$,  and indeed $RAND () ` can never be above $q^*$).
- We can simulate `RAND()` many times,  say $N `.
  - Whenever the realization `RAND()>q^{*}` we say that we went down the tree.
  - Whenever `RAND()<q^{*}`,  we say we went up the tree.
- Compute the value of the stock price at time $T=1$,  $S_{1,          u}$ or $S_{1,          d}$ for each simulation.
  - Let $S_{1}^{i}$ denote the realization of $S_{1}$ in simulation run $i `.
  - Compute the payoff of the security at time $T=1$ for each simulation run,  e.g. $V(S_{1}^{i})=\max(S_{1}^{i}-K,          0)$.
- The value of the security is the average of the realizations:$$\left\{e^{-rT}V(S_{1}^{1}),           e^{-rT}V(S_{1}^{2}),           e^{-rT}V(S_{1}^{3}),           \dots,           e^{-rT}V(S_{1}^{N})\right\}=\frac{1}{N}$$

## Monte Carlo Simulations on the Risk Neutral Trees
- For instance,  given $q^{*}=0.4587$,  we obtain the following table:
```latex
\begin{document}
\begin{tabular}{ | c | c | c | c | c | }
\hline
RAND & Move Tree On & Price at T & Payoff & Discounted \\
\hline
0.457335 & up & 134.986 & 34.986 & 34.293 \\
\hline
0.393937 & up & 134.986 & 34.986 & 34.293 \\
\hline
0.090053 & up & 134.986 & 34.986 & 34.293 \\
\hline
0.878148 & down & 74.082 & 0 & 0 \\
\hline
0.658659 & down & 74.082 & 0 & 0 \\
\hline
0.759579 & down & 74.082 & 0 & 0 \\
\hline
0.798027 & down & 74.082 & 0 & 0 \\
\hline
0.061689 & up & 134.986 & 34.986 & 34.293 \\
\hline
0.969222 & down & 74.082 & 0 & 0 \\
\hline
0.39267 & up & 134.986 & 34.986 & 34.293 \\
\hline
 &  & Average & 17.147 & \\
\hline
 &  & st. error & 5.715 & \\
\hline
\end{tabular}
\end{document}
```

- With only $N=10$ simulation,  it is no surprise that the value of the security ${\tilde{V}}_{0}=17.147$ comes rather different from the value from the tree ($V_{0}=15.731$).
- As $N$ increases,  the value gets more and more precise.

## Monte Carlo Simulations on the Risk Neutral Trees
- How many simulations?
  - The number of simulations $N$ should be large enough to obtain a reasonable “standard error",  that is,  standard deviation of our estimate itself.
  - This is computed as the standard deviation of our discounted payoff,  divided by $\sqrt{N}$.
$$\mathrm{error~}=\frac{\mathrm{Standard~Deviation~of~}\{e^{-rT}V(S_{1}^{1}),          e^{-rT}V(S_{1}^{2}),          e^{-rT}\}}{\sqrt{N}}$$

- In the previous example,  the standard error was $s.e.=5.715$
  - This implies that with 95% probability,  the true value of the security is between
$$\mathrm{Confidence~Interval}=[\widehat{V}_{0}-2\times s.e.,          \widehat{V}_{0}+2\times s.e.]=[5.715,           28.577]$$

- Given the number of simulations,  we give $95\%$ probability that the true value is between 5.715 and 28.577,  a rather large interval.
- Increasing the number of simulations to $N=1000$,  we obtain ${\tilde{V}}_{0}=15.725$ with $s.e.=0.54$.
  - The confidence interval is [14.644,  16.806],  much tighter than before.

## Monte Carlo Simulations on the Multi-Step Risk Neutral Trees
- The same logic applies to multi-step trees.
- Consider a two-step tree,  with the same parameters.
!Image
- Again,  the value of any derivative security with payoff $V(S_{2})$ is given by:$$V(S)=E^*[e^{-rT}V(S_2)]$$

## Monte Carlo Simulations on the Multi-Step Risk Neutral Trees

- For instance,  with $N=10$ simulations,  we may obtain something as follows:
```latex
\begin{document}
\begin{tabular}{ | c | c | c | c | c | c | c | }
\hline
RAND 1 & Move Tree On & RAND 2 & Move Tree On & Price at T & Payoff & Discounted \\
\hline
0.535163 & down & 0.621716 & down & 65.425 & 0.000 & 0 \\
\hline
0.501443 & down & 0.542492 & down & 65.425 & 0.000 & 0 \\
\hline
0.079387 & up & 0.021237 & up & 152.847 & 52.847 & 51.80 \\
\hline
0.194357 & up & 0.964902 & down & 100.000 & 0.000 & 0 \\
\hline
0.329731 & up & 0.487593 & down & 100.000 & 0.000 & 0 \\
\hline
0.581736 & down & 0.841805 & down & 65.425 & 0.000 & 0 \\
\hline
0.450822 & up & 0.308040 & up & 152.847 & 52.847 & 51.80 \\
\hline
0.017819 & up & 0.978316 & down & 100.000 & 0.000 & 0 \\
\hline
\end{tabular}
\end{document}
```

- 6.90 st. Error
- With $N=1000$ simulations,  the price is ${\tilde{V}}_{0}=10.453$ with $s.e.=0.657$.
- The value from the risk-neutral tree is instead 11.476.

## Monte Carlo Simulations on the Multi-Step Risk Neutral Trees
- A 10-step tree is as follows:
!Image

## Monte Carlo Simulations on the Multi-Step Risk Neutral Trees
- 10 simulated paths are given by (the price in the table refers to $N=1000$ though).
!Image

## Monte Carlo Simulations on the Multi-Step Risk Neutral Trees
- The simulation paths are (they look like a tree,  with missing branches).
!Image

## Why Monte Carlo Simulations?
- Why do we need Monte Carlo Simulations on the tree when we have the tree itself?
  - Monte Carlo Simulations may be useful to price derivative securities with path-dependent payoff.
  - That is,  the value at maturity depends on the path taken by the stock during the life of the security.
- For instance,  Asian options have payoff given by:$$\mathrm{Asian~Call~Option}=\max\left(\{\mathrm{Average~of~}S_{t}\mathrm{~from~}0\mathrm{~to~T}\}-1\right)$$$$\mathrm{Asian~Put~Option}=\max\left(K-\{\mathrm{Average~of~}S_{t}\mathrm{~from~}0\mathrm{~to~T}\right)$$

- These options are very hard to price on a tree without simulations.
- Consider a two-step tree.

!Image

- Even if $S_{2,          ud}=S_{2,          du}=100$,  the payoff when the final price is 100 depends on the path of $S$,  namely,  whether $S_{1}=S_{1,          u}=123.631$ or $S_{1}=S_{1,          d}=80.886$.
- In this case,  we can compute the value of the security on the tree $V_{0}=\Sigma_{j=1}^{4}Q_{j}^{*}V_{2,          j}=7.45$.
- 1000 Monte Carlo simulations yield $\widehat V_{0}=7.560$ with $s.e.=0.316$.

## Why Monte Carlo Simulations?

- When we move to multi-period trees,  path-dependent options become much more difficult to price without Monte Carlo Simulations.
- The following picture shows the averages ${\overline{S}}_{t}$ over 10 paths.
  - While the original paths look like the recombining tree we started out with,  the averages look like paths on a non-recombining tree.
  - Non-recombining trees are much harder to evaluate numerically for a large number of time steps.

!Image

## Why Monte Carlo Simulations?
- The number of path-dependent options is very large.
- Besides the Asian option discussed,  some other popular examples are:
  - **Barrier Options**:
	- The option expires if stock hits an upper (up and out) or a lower (down and out) barrier.
	- The option comes into existence if the stock hits an upper (up and in) or a lower (down and in) barrier.
  - **Lookback Options**:
	- The final payoff depends on the maximum or minimum value achieved by the stock before maturity. For instance:$$g_T=\max(S_0,          \dots,          S_T)-S_T$$

  - **Asian Strike Options**:
	- The strike price is equal to the average stock price. E.g.$$g_T=\max(S_T-\text{Average}(S_0,          \dots,          S_T),          0)$$

## Monte Carlo Simulations without Trees
- There is no reason to limit MC simulations to trees.
  - The main motivation behind pricing by MC simulations is risk-neutral pricing.
	- That is,  dynamic replication can be achieved.
	- These no-arbitrage conditions are naturally satisfied on trees,  as we have seen.
- However,  once we decide we can use risk-neutral pricing,  we can simulate out of any distribution.
  - In particular,  we can use the lognormal model,  as in Black and Scholes.
  - Risk-neutral pricing implies that over a small period:$$E^*\left(\frac{S_{t+h}}{S_t}\right)=e^{rh}$$

## Monte Carlo Simulations under Log Normality
- One way to simulate is then to use the following algorithm:$$S_{t+h}=S_t\times e^{(r-\frac{\sigma[^2]}{2})h+\sigma\sqrt{h}\epsilon_t}$$
- Where:$$\epsilon_t\sim N(0,          1)$$
- The rules of the log-normal distribution imply:$$E^*\left(\frac{S_{t+h}}{S_t}\right)=e^{(r-\frac{\sigma[^2]}{2})h+\left\{E^*[\sigma\sqrt{h}\times\epsilon_t]+1/2Var[\sigma\sqrt{h}\times\epsilon_t]\right\}}=e^{rh}$$
- Moreover,  $\sigma^{2}$ converges to the (annualized) variance of log returns $Var[\log(S_{t+h}/S_{t})]$.

## Monte Carlo Simulations under Log Normality
- For instance,  a few 10-period paths are plotted in the next figure.
!Image

## Monte Carlo Simulations under Log Normality
- MC price of put and calls under Black and Scholes assumptions (1000 simulations).
!Image

## Monte Carlo Simulations with Many "Factors"
- The Monte Carlo Simulation method to price options can be extended to price derivative securities that depend on multiple factors. For instance:
  - Time varying interest rates.
  - Time varying volatility.
  - Payoffs on the relative value of different stocks,  exchange rates,  etc.
- The methodology is the same:
  1. Simulate risk-neutral factors.
  1. Compute the cash flows of the security.
  1. Compute the present value,  discounting at the risk-free rate.
  1. Average all of the simulated paths.

- One difficulty is with obtaining risk-neutral dynamics for factors:
  - Traded factors are simple: the expected return on such factors must be the risk-free rate.
  - It is harder for non-traded factors (e.g.,  interest rates,  volatility). We attack this problem later on.

## Monte Carlo Simulations with Many "Factors"
- Consider an option that pays the maximum between the stock return on IBM and Apple within a pre-specified period.
  - That is,  if $S_{0}$ and $N_{0}$ are the current prices of the two stocks,  the payoff at maturity of the option is:$$\text{Payoff at}T=\max\left(\frac{S_T}{S_0},          \frac{N_T}{N_0}\right)$$
- How much would you pay for this security?
  - We can use Monte Carlo Simulations to find out.
  - The risk-neutral processes of $S_{t}$ and $N_{t}$ are the same as before,  so we simulate:$$S_{t+h}=S_{t}\times e^{(r-\frac{\sigma_{S}^{2}}{2})h+\sigma_{S}\sqrt{h}\epsilon_{1,          t}}$$$$N_{t+h}=N_{t}\times e^{(r-\frac{\sigma_{N}^{2}}{2})h+\sigma_{N}\sqrt{h}\epsilon_{2,          t}}$$
- If IBM and Apple are correlated stocks (as they are),  we need a methodology to simulate correlated shocks $\epsilon_{1,          t}$ and $\epsilon_{2,          t}$.
  - Let $\hat{\epsilon}_t$ and $\hat{\epsilon}_{t}$ be standard normal,  uncorrelated with $\epsilon_{1,          t}$. Then define:$$\epsilon_{2,          t}=\rho\epsilon_{1,          t}+\sqrt{1-\rho^{2}}\widehat{\epsilon}_{t}$$
  - Claim: $\epsilon_{2,          t}$ has zero mean,  variance 1,  and correlation $\rho$ with $\epsilon_{1,          t}$ (check!).

## Monte Carlo Simulations with Many "Factors"
- For each simulation run $i$,  compute the discounted payoff:$$V^i=e^{-rT}\max\left(\frac{S_T^i}{S_0},          \frac{N_T^i}{N_0}\right)$$
- The price of the security is then:$$\widehat{V}_0=\frac{1}{n}\sum\limits_{i=1}^nV^i$$

- Assuming $\sigma_{S}=\sigma_{N}=0.3$,  $r=0.02$,  and $\rho=0.7$,  the value of this option is $\widehat{V}_{0}=1.134$.
- As a second example,  consider an option with the payoff:$$\text{Payoff at}T=\max\left(\frac{S_T}{S_0}-\frac{N_T}{N_0},          0\right)$$
  - That is,  it pays only when the first stock (say IBM) does better than the second (say Apple).
  - The same simulations show that the fair value of this option is $\widehat V_{0}=0.1$.
- Note that the difference between one option and another is simply the final payoff. The methodology is identical.

!Image

!Image

SIMULATION OF RISK NEUTRAL PRICE PROCESS
```latex
\begin{document}
\begin{tabular}{ | c | c | c | c | c | c | c | c | }
\hline
 & 0.000 & 0.004 & 0.008 & 0.012 & 0.016 & 0.020 & 0.024 \\
\hline
0n & 0.000 & 1.000 & 2.000 & 3.000 & 4.000 & 5.000 & 6.000 \\
\hline
1.000 & 100.000 & 98.498 & 97.697 & 100.548 & 102.477 & 104.831 & 101.270 \\
\hline
2.000 & 100.000 & 100.697 & 100.882 & 103.319 & 101.228 & 104.745 & 107.374 \\
\hline
3.000 & 100.000 & 104.143 & 102.590 & 101.671 & 101.579 & 102.504 & 103.337 \\
\hline
4.000 & 100.000 & 100.266 & 98.972 & 99.121 & 99.309 & 99.744 & 99.729 \\
\hline
5.000 & 100.000 & 101.133 & 98.477 & 96.643 & 98.565 & 96.410 & 96.365 \\
\hline
6.000 & 100.000 & 101.824 & 103.298 & 101.684 & 98.772 & 97.923 & 100.191 \\
\hline
7.000 & 100.000 & 97.859 & 101.048 & 101.048 & 95.698 & 95.496 & 96.103 \\
\hline
8.000 & 100.000 & 100.923 & 99.002 & 96.070 & 98.452 & 97.768 & 96.828 \\
\hline
9.000 & 100.000 & 101.021 & 99.586 & 98.328 & 98.466 & 99.917 & 103.322 \\
\hline
10.000 & 100.000 & 94.981 & 93.695 & 92.245 & 92.556 & 91.834 & 92.319 \\
\hline
\end{tabular}
\end{document}
```

## How can we Compute $\Delta$ with Monte Carlo Simulations?

- Once we have computed the value of the security,  we may want to know what is its sensitivity to changes in the stock.
- Computing $\Delta$ is not hard,  and we use Monte Carlo simulations again:$$\Delta=\frac{dV(S)}{dS}\approx\frac{V(S+h)-V(S)}{h}$$

- Thus,  compute $V(S)$ and $V(S+h)$ using MC simulations.
- Apply the above formula.
- For instance,  we obtained earlier the price of a call equal to $c(100)=13.359$. Using $S=101$,  we obtain:$$c(101)=13.979 \Longrightarrow \Delta=(13.979-13.359)/1=0.62$$
- Black and Scholes Delta is $\Delta=N(d_1)=0.58$. As $N$ increases,  the simulated $\Delta$ converges to the true one.

## Conclusion

- The Monte Carlo Simulations Method is one of the main tools used by practitioners to price complex securities under fairly general assumptions about the underlying stochastic processes.
- Just three steps:
  1. Simulate many paths of underlying stochastic variables under the risk-neutral probabilities.
  1. For each path,  compute the discounted simulated payoff of the security.
  1. Compute the average.
- MCS are especially useful to value path-dependent securities,  or securities that depend on the value of multiple underlying variables:
  - Barrier options,  Asian options,  Lookback options.
  - Options on maximum,  options on relative returns across securities.
- MCS are also very useful to value securities under general processes for underlying stochastic variables,  such as:
  - Stochastic volatility.
  - Stochastic interest rates.
  - Jumps.
- The ever-increasing gains in computer speed make MCS methodology increasingly attractive.

---
academic_level: graduate
aliases:
- BSM
- IV
- The Smirk
cssclasses: academia
enhanced: true
enhancement_date: '2025-11-06'
enhancement_id: batch09-000136
key_concepts:
- Black-Scholes option pricing model and continuous-time finance
- Binomial option pricing model and lattice methods
- Implied volatility calculation and volatility surface analysis
- Volatility smile and skew in options markets
- Options Greeks and sensitivity analysis for risk management
- Risk-neutral measures and martingale pricing
- Martingale theory and change of measure
- Duration analysis and interest rate risk management
- Convexity adjustments and yield curve sensitivity
- Capital Asset Pricing Model (CAPM) and expected returns
- Value at Risk (VaR) and tail risk measurement
- Expected shortfall and coherent risk measures
- Arbitrage opportunities and no-arbitrage pricing
- Alpha generation and active portfolio management
- Factor models and multi-factor pricing
- Volatility modeling and estimation techniques
- Alpha generation and active return measurement
- Risk preference theory and utility functions
- Sensitivity analysis and Greeks calculation
- Ito's Lemma and Lognormal Asset Price Dynamics
- Risk-Neutral Valuation in Option Pricing
- Value at Risk and Expected Shortfall
- Vasicek Interest Rate Model and Mean Reversion
- Short Rate Models and Term Structure Dynamics
- Capital Asset Pricing Model and Beta Analysis
- Credit Risk Management and Default Probability
- Expected Loss and Loss Given Default Models
- Swap Market Mechanisms and Pricing
- Delta, Gamma, and Vega Hedging Techniques
- 'Greeks: Delta, Gamma, Theta, and Vega Hedging'
- Ornstein-Uhlenbeck Process in Finance
- Price Discovery and Market Efficiency
- Cost of Equity and Expected Returns
- Black-Scholes Option Pricing Model and Its Applications
- Security Market Line and Risk-Return Tradeoff
- Options Trading Strategies and Risk Management
- Stress Testing and Extreme Value Analysis
- Lattice Methods and Recombining Trees in Derivatives Pricing
- Time Series Analysis in Financial Markets
- Credit Default Swaps and Credit Risk Transfer
- Fama-French Factors and Style Analysis
- Risk Measurement and VaR Backtesting
- Bid-Ask Spreads and Market Impact
- Contango, Backwardation, and Roll Yield
- Futures and Forward Contracts in Financial Markets
- Binomial Option Pricing Model for Discrete Time Valuation
- Hedge Strategies and Basis Risk Management
- Dynamic vs Static Hedging in Practice
- American Option Pricing and Early Exercise Premium
- Interest Rate Swaps and Currency Swap Structures
- Cointegration and Statistical Arbitrage
- Option Valuation and Exercise Strategies
- Market Microstructure and Liquidity Analysis
- Credit Spreads and Rating Migration Analysis
- GARCH Models and Volatility Forecasting
- Hedging Strategies and Risk Mitigation
- Factor Models and Asset Pricing
- Arbitrage Pricing Theory and Multi-Factor Models
linter-yaml-title-alias: LECTURE NOTE 7-EXOTIC OPTIONS AND DERIVATIVE PRICING BY MONTE
  CARLO SIMULATION
professional_application: theoreti
status: active
tags:
- arbitrage-opportunity
- arbitrage-pricing
- asset-allocation
- barrier-options
- binomial-model
- black-scholes-model
- capital-asset-pricing
- caplet
- coherent-risk-measure
- conditional-var
- continuous-time-pricing
- convexity-adjustment
- credit-rating
- delta-hedging
- derivatives
- hull-white
- call-options
- cir-model
- butterfly-spreads
- expected-shortfall
- binomial-tree
- straddles
- extreme-value-theory
- american-options
- partial-differential-equation
- book-to-market
- arbitrage
- risk-neutral-valuation
- backwardation
- volatility-analysis
- style-analysis
- option-strategies
- unexpected-loss
- capital-asset-pricing-model
- clearinghouse
- overnight-indexed-swaps
- arbitrage-pricing-theory
- hedge-ratio
- market-price-of-risk
- volatility-surface
- price-discovery
- loss-given-default
- value-factor
- vasicek-model
- sharpe-ratio
- dynamic-hedging
- monte-carlo-var
- options-trading
- market-impact
- forward-contracts
- stationarity
- fama-french
- bsm-model
- recovery-rate
- black-scholes-formula
- garch
- parametric-var
- lognormal-models
- var-methodologies
- historical-var
- mean-reversion
- contango
- vega-hedging
- unit-roots
- expected-loss
- market-efficiency
- quantitative-finance
- order-flow
- currency-swaps
- bid-ask-spread
- crr-model
- systematic-risk
- protective-puts
- alpha
- security-market-line
- probabilty-of-default
- liquidity
- gamma-hedging
- hedge-effectiveness
- idiosyncratic-risk
- roll-yield
- beta
- risk-premium
- put-options
- affine-term-structure
- multi-period-binomial
- capm
- algorithmic-trading
- momentum
- basis-risk
- market-risk-premium
- volatility-modeling
- discrete-time-pricing
- hedge-strategies
- regime-switching
- covered-calls
- swap-rate
- sofr
- ' exposure-at-default'
- stress-testing
- roll-over-risk
- mathematical-finance
- ornstein-uhlenbeck
- rating-migration
- investment-analysis
- portfolio-optimization
- value-at-risk
- kalman-filter
- factor-models
- risk-management
- convergence
- var-backtesting
- arima-models
- state-space-models
- cross-hedging
- european-options
- high-frequency-trading
- lattice-models
- strangles
- cointegration
- cox-ross-rubinstein
- short-rate-models
- swap-spread
- optional-exercise
- efficient-frontier
- credit-migration
- default-probability
- marking-to-market
- binomial-option-pricing
- total-return-swaps
- libor
- credit-spreads
- granger-causality
- multi-factor-models
- ito-calculus
- iron-condors
- option-pricing
- financial-markets
- static-hedging
- size-effect
- basis-swaps
- interest-rate-swaps
- lognormal-distribution
- ' recombining-trees'
- futures-contracts
- apt
- credit-default-swaps
title: Lecture Note 6-Implied Volatility
type: course-note
---
--



# Lecture Note 6-Implied Volatility
- **Title**: Implied Volatility
- **Author**: John Heaton
- **Institution**: The University of Chicago Booth School of Business

#### 1. Black and Scholes Option Pricing Model: Does it work?
- **1.1 Fat Tails**
- **1.2 Stochastic Volatility**
- **1.3 Jumps**

#### 2. Implied Volatility
- **2.1 The Smirk**
- **2.2 Implied Volatility and Empirical Volatility**
- **2.3 Implied Volatility Surface**

#### 3. Improvements on Black and Scholes Model
- **3.1 Deterministic and Stochastic Volatility Models**
- **3.2 Jump Model**
- **3.3 Implied Tree Models**

## Black and Scholes Model: Does it Work?
- Does the Black and Scholes model yield option prices similar to the market price of traded options?
  - On October 31:
	- The S&P 500 index was $S = 3871.98$.
	- The one-month risk-free rate was $r = 3.75\%$ (c.c).
	- The dividend yield on the S&P 500 is about $q = 1.69\%$.
	- Observed options prices with maturity end of November $T = 1/12$.

!Observed Options Prices

#### Moneyness
- Moneyness is defined as the ratio of the strike price to the current stock price $K/S$:
  - $K/S < 1$:
	- $K < S$: **Puts are OTM,  calls are ITM**.
  - $K/S > 1$:
	- $K > S$: **Puts are ITM,  calls are OTM**.

!Moneyness Diagram

#### Comparison to Black-Scholes Using Historical Volatility
- Historical volatility used: $22.2\%$.

!BSM vs Observed Prices

### BSM Using Historical Volatility Relative to Observed Prices

!Historical Volatility Comparison

### BSM Using Historical Volatility Relative to Observed Prices

!BSM Comparison

#### BSM Put Prices Relative to Observed Prices
- **Implied volatility** was set to match the "ATM" put option with strike of $3870$. This implied volatility was $23.1\%$.

!BSM Put Prices

## Black and Scholes: What is Wrong?
- **Assumption**: Black-Scholes assumes log-normal returns.
  - That is:
	$$r_{S} = \log\left(\frac{S_{t+h} + \text{dividends}}{S_{t}}\right)$$
  - $S_{t}$ is normally distributed.
  - **Issue**: Fat tails in empirical distribution indicate extreme observations are more likely than implied by the normal distribution.
- **Figure 1**: Empirical distribution of monthly returns versus the normal distribution.
  !Fat Tails

- **Assumption**: The Black-Scholes model assumes that volatility of stock returns is constant.
  - **Issue**: Volatility is stochastic—it moves unpredictably over time.
  !Stochastic Volatility](https://storage.simpletex.cn/view/fGysIz0gqllwhIFfks5Ye3qmc5TnMsgGa)

- **Assumption**: Black-Scholes assumes continuous trading and no jumps.
  - **Issue**: Prices sometimes jump discretely.
  !Price Jumps

## Black and Scholes Implied Volatility
- **Definition**: Implied Volatility is the level of volatility $\sigma$ that,  when used in the Black-Scholes formula,  matches the value of a traded option.
  - For instance,  given:
	$$put^{mkt}(3870,     1/12) = 98.50$$
	- The implied volatility for this option was $23.1\%$.
- **Note**: Every option has a potentially different implied volatility $\sigma_{\text{Imp}}$.

#### Implied Volatility Smile (Smirk)

!Implied Volatility Smile](https://storage.simpletex.cn/view/fezEoUykvROU4GsR96sxSe0XYhlAepbAv)

### Uses of Implied Volatility
- **Gauge Market Uncertainty**: Higher uncertainty leads to higher implied volatility.
  - Implied volatility augments return volatility as it is forward-looking.
- **Relative Pricing of Options**:
  - Options with different strike prices and maturities can be compared using implied volatility.

!Option Prices Across Strikes and Maturities

#### VIX
- The **VIX** uses the concept of "Volatility Swaps,  " where a portfolio of options is created that is hedged against index-level moves,  exposing only volatility changes.
  - **Note**: Technically,  it is not the same as "implied volatility" in the BSM model.

#### Implied Volatility Surface
- Represents implied volatilities across different strikes and maturities.
  !Implied Volatility Surface](https://storage.simpletex.cn/view/fyBmkHCKoTHgnXQsLMBY0WzvXAEsVUkg3)

## Black and Scholes Model: Shall We Throw It Away?
- **No**: Black-Scholes is still a useful benchmark.
- It works reasonably well for **hedging against changes** in stock prices.
- New models address BSM's shortcomings:
  - **Deterministic and Stochastic Volatility Models**: Account for time-varying volatility.
  - **Models with Price Jumps**: Account for discrete jumps in prices.
  - **Implied Tree Models**: Find trees that actually price options.
- These models often imply that put prices are overpriced due to investors paying a premium for downside protection.

### Deterministic Volatility Models
- **Assumption**: Volatility depends on the stock price itself.
  - E.g.,  **Constant Elasticity of Variance Model**:
	$$\sigma(S) = \Sigma \times S^{\alpha}$$
	$$\log\left(\frac{S_{t,    t+h}}{S_t}\right) = \mu \times h + S_t^{\alpha} \times \Sigma \times \epsilon_t$$
  - If $\alpha < 0$,  lower $S_{t}$ implies higher volatility,  leading to an implied volatility smirk.

!Deterministic Volatility

#### Stochastic Volatility Models
- **Assumption**: Volatility $\sigma_{t}$ changes over time.
  - E.g.,  let $\sigma_{t} = \sqrt{v_{t}}$:
	$$R_{t,    t+h} = \mu \times h + \sqrt{v_t} \times \epsilon_{1,    t}$$
	$$(v_{t+h} - v_t) = k \times (\overline{v} - v_t) \times h + \Sigma \times \sqrt{v_t} \times \epsilon_{2,    t}$$
Result: if volatility is negatively correlated with stock returns,  OTM put options become relatively more expensive.
- **Intuition**: A decline in price $\Rightarrow$ higher volatility $\Rightarrow$ higher probability of even larger declines $\Rightarrow$ higher price of insurance against downturns.
  - If volatility is negatively correlated with stock returns,  OTM put options become relatively more expensive.

#### Jump Models

Assume that sometimes big changes in stock prices occur (e.g.,  October 1987).
$$R_{t,    t+h} = \mu \times h + \sigma \times \epsilon_t + \omega \times Q_t$$

- Where $Q_{t} = 0$ most of the time,  but sometimes $Q_{t} = 1$ (with small probability).
- $\omega$ can be a random variable (e.g.,  normal) or a constant.
Result: If $\omega < 0$,  then OTM put options are relatively more expensive.
- Investors are willing to pay a higher premium to insure against negative outcomes.
**Pricing with jumps is particularly complicated**.
- The pricing formulas are not as "nice" as the Black-Scholes formula.
  - Result: If $\omega < 0$,  OTM put options are more expensive.
- The idea is reasonably simple.
- In Teaching Note 4,  we learnt how to go from a tree to option prices
- The “implied tree” methodology does the opposite: Uses (some) option prices to obtain a tree
- For instance,  consider the binomial tree model in Teaching Note 4.
- Given $S_0=1502.39,    \sigma=12.36\%,    r=4.713\%,    \delta=1.91\%$ and $T=0.\1$,  we fnd $u=$ $exp(\sigma\sqrt T)=1.043746137$ and $d=1/u=0.958087378.$ Thus,  the risk neutral probability$$q^*=\frac{e^{(r-\delta)T}-d}{u-d}=0.528631113$$
- The price of the $K=1500$ put option come out to be $p_0=\$28.394$,     higher than the tradeci$\bar{\text{market price }p^{mkt}(1500,  0.\1)}=\bar{\$20.35}.$
```latex
\usepackage{tikz}
\usetikzlibrary{positioning}

\begin{document}
\begin{tikzpicture}[
    box/.style = {draw,     rounded corners,     minimum width=4cm,     minimum height=2cm,     align=left},    
    node distance=3cm
]

% Level i = 0
\node[box] (i0) {
    $S_0 = 1502.39$\\
    $q^*_0 = 0.528631113$\\
    $p_0 = e^{-r \times 0.12} \times (1 - q^*_0) \times p_{1,    d} = 28.394$
};

% Level i = 1,     upper branch
\node[box,     right=of i0,     yshift=1.5cm] (i1u) {
    $S_{1,    u} = 1568.114$\\
    $p_{1,    u} = 0$
};

% Level i = 1,     lower branch
\node[box,     right=of i0,     yshift=-1.5cm] (i1d) {
    $S_{1,    d} = 1439.421$\\
    $p_{1,    d} = 60.579$
};

% Connect nodes
\draw[->] (i0.east) -- ++(0.5,    0) | - (i1u.west);
\draw[->] (i0.east) -- ++(0.5,    0) | - (i1d.west);

% Labels for time levels
\node[above left=0.5cm of i0] {$i = 0$};
\node[above left=0.5cm of i1u] {$i = 1$};

\end{tikzpicture}
\end{document}

```		
!Implied Tree Logic

An implied tree has the same logic as implied volatility: Since the model is not working using the correct inputs,  we look for an alternative specification that makes it work.

- In the above example,  we can **choose $S_{1,    u}$** to price the option correctly.
- To avoid too many parameters,  define $u = S_{1,    u}/S_{0}$ and define $S_{1,    d} = S_{0}/u$.

We obtain the following:
```latex
\usepackage{tikz}
\usetikzlibrary{positioning}

\begin{document}
\begin{tikzpicture}[
    box/.style = {draw,     rounded corners,     minimum width=4cm,     minimum height=2cm,     align=left},    
    node distance=3cm
]

% Level i = 0
\node[box] (i0) {
    $S_0 = 1502.39$\\
    $q^*_0 = 0.528631113$\\
    $p_0 = e^{-r \times 0.12} \times (1 - q^*_0) \times p_{1,    d} = 28.394$
};

% Level i = 1,     upper branch
\node[box,     right=of i0,     yshift=1.5cm] (i1u) {
    $S_{1,    u} = 1568.114$\\
    $p_{1,    u} = 0$
};

% Level i = 1,     lower branch
\node[box,     right=of i0,     yshift=-1.5cm] (i1d) {
    $S_{1,    d} = 1439.421$\\
    $p_{1,    d} = 60.579$
};

% Connect nodes
\draw[->] (i0.east) -- ++(0.5,    0) | - (i1u.west);
\draw[->] (i0.east) -- ++(0.5,    0) | - (i1d.west);

% Labels for time levels
\node[above left=0.5cm of i0] {$i = 0$};
\node[above left=0.5cm of i1u] {$i = 1$};

\end{tikzpicture}
\end{document}

```		

### Implied Tree Models
- **Idea**: Use some option prices to obtain a pricing tree.
  - Example: Binomial Tree Model.
- What do we use an implied tree for?
	- To price other options. For instance,  if $K=1490$,  the put price from the binomial tree $\bar{\text{is }\$15.82184291,  \text{ closer to the market value of }p^{mkt}(1490,  0.\1)}=\$17.05$,     compared to the original case (which would be $23.707)
	- With more elaborated trees,  one can also price more elaborated derivatives,  which have path dependencies,  or American features.
	- Given:
	  $$S_{0} = 1502.39,     \sigma = 12.36\%,     r = 4.713\%,     \delta = 1.91\%,     T = 0.12$$
	  - $u = \exp(\sigma\sqrt{T}) = 1.043746137$,  $d = 1/u = 0.958087378$
	  - Risk-neutral probability:
		$$q^* = \frac{e^{(r-\delta)T} - d}{u - d} = 0.528631113$$
	  - Price of $K = 1500$ put option is $p_{0} = 28.394$,  higher than the market price $p^{mkt}(1500,     0.12) = 20.35$.
- **Two-Step Implied Tree**: After solving the first step,  extend to a two-step tree to fit additional market options.
- Once we solved for the first step,  we can proceed to obtain a two step tree
	- We need to keep the frst step fixed though
- What do we choose?$$-\:S_{2,    uu},    \:S_{2,    ud}=S_{2,    du}\mathrm{~and~}\:S_{2,    dd}.$$
- It is desirable to keep the tree somewhat balanced around the starting value $S_0.$$$-\Longrightarrow\text{choose }S_{2,    ud}=S_{2,    du}=S_0$$
- Since we have two price levels to choose,  we need two options.
,  The following example has $p^mkt(1450,    0.\1)=\$14.65$ and $p^{mkt}(1550,  0.\1)=\$50.2$
```latex
\usepackage{tikz}
\usetikzlibrary{positioning}

\begin{document}
\begin{tikzpicture}[
    box/.style = {draw,     rounded corners,     minimum width=5cm,     minimum height=2cm,     align=left},    
    node distance=4cm
]

% Level i = 0
\node[box] (i0) {
    $S_0 = 1502.39$\\
    $q^*_0 = 0.5446$\\
    $p_0[^1] = 50.2 = p^{mkt}(1550,     0.21)$\\
    $p_0[^2] = 14.65 = p^{mkt}(1450,     0.21)$
};

% Level i = 1,     upper branch
\node[box,     right=of i0,     yshift=3cm] (i1u) {
    $S_{1,    u} = 1551.26$\\
    $q^*_{1,    u} = 0.7144$\\
    $p[^1]_{1,    u} = 13.5413$\\
    $p[^2]_{1,    u} = 0$
};

% Level i = 1,     lower branch
\node[box,     right=of i0,     yshift=-3cm] (i1d) {
    $S_{1,    d} = 1455.059$\\
    $q^*_{1,    d} = 0.7373$\\
    $p[^1]_{1,    d} = 94.67$\\
    $p[^2]_{1,    d} = 32.36$
};

% Level i = 2,     upper-upper branch
\node[box,     right=of i1u,     yshift=3cm] (i2uu) {
    $S_{2,    uu} = 1567.0713$\\
    $p[^1]_{2,    uu} = 0$\\
    $p[^2]_{2,    uu} = 0$
};

% Level i = 2,     middle branch
\node[box,     right=of i1u,     yshift=-3cm] (i2ud) {
    $S_{2,    ud} = S_{2,    du} = 1502.39$\\
    $p[^1]_{2,    ud} = 47.61$\\
    $p[^2]_{2,    ud} = 0$
};

% Level i = 2,     lower-lower branch
\node[box,     right=of i1d,     yshift=-3cm] (i2dd) {
    $S_{2,    dd} = 1336.2316$\\
    $p[^1]_{2,    dd} = 213.7684$\\
    $p[^2]_{2,    dd} = 113.7684$
};

% Connect nodes
\draw[->] (i0.east) -- ++(0.5,    0) | - (i1u.west);
\draw[->] (i0.east) -- ++(0.5,    0) | - (i1d.west);
\draw[->] (i1u.east) -- ++(0.5,    0) | - (i2uu.west);
\draw[->] (i1u.east) -- ++(0.5,    0) | - (i2ud.west);
\draw[->] (i1d.east) -- ++(0.5,    0) | - (i2ud.west);
\draw[->] (i1d.east) -- ++(0.5,    0) | - (i2dd.west);

% Labels for time levels
\node[above left=0.5cm of i0] {$i = 0$};
\node[above left=0.5cm of i1u] {$i = 1$};
\node[above left=0.5cm of i2uu] {$i = 2$};

\end{tikzpicture}
\end{document}

```

### Conclusions
- The **Black-Scholes formula** does not price options consistently,  either in cross-section (different strike prices) or over time.
  - Issues:
  - **Stochastic Volatility**,
  - **Jumps**,
  - **Fat Tails**.
- Despite these issues,  BSM is still a useful benchmark,  especially for first-order pricing and hedging.
- **More Complicated Models** fit the data better and can be used for arbitrage strategies,  but gains are often limited.
- Black-Scholes has become the industry standard for quoting options.
  - **Implied Volatility Surfaces** provide a convenient way to gauge the relative value of options.

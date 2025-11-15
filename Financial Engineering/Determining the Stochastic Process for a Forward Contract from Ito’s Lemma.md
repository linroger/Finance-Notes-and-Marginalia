---
academic_level: graduate
aliases:
- Forward Price Dynamics
- Ito's Lemma
enhanced: true
enhancement_date: '2025-11-06'
enhancement_id: batch09-000433
key_concepts:
- Black-Scholes option pricing model and continuous-time finance
- Options Greeks and sensitivity analysis for risk management
- Ito's lemma and stochastic calculus applications
- Convexity adjustments and yield curve sensitivity
- Arbitrage opportunities and no-arbitrage pricing
- Sensitivity analysis and Greeks calculation
- Financial modeling and quantitative analysis
- Risk management and portfolio optimization
- Derivatives pricing and hedging strategies
- Market risk measurement and control
- Risk Measurement and VaR Backtesting
- Bid-Ask Spreads and Market Impact
- Contango, Backwardation, and Roll Yield
- 'Greeks: Delta, Gamma, Theta, and Vega Hedging'
- Futures and Forward Contracts in Financial Markets
- Option Valuation and Exercise Strategies
- Value at Risk and Expected Shortfall
- Factor Models and Asset Pricing
- Hedge Strategies and Basis Risk Management
- Market Microstructure and Liquidity Analysis
- Price Discovery and Market Efficiency
- Options Trading Strategies and Risk Management
- Stress Testing and Extreme Value Analysis
- Fama-French Factors and Style Analysis
- Arbitrage Pricing Theory and Multi-Factor Models
professional_application: theoreti
status: active
tags:
- arbitrage-opportunity
- asset-allocation
- binomial-model
- black-scholes-model
- caplet
- continuous-time-pricing
- convexity
- convexity-adjustment
- credit-rating
- delta-hedging
- derivatives
- discrete-time-pricing
- dividend-policy
- dividend-stability
- dynamic-hedging
- put-options
- call-options
- high-frequency-trading
- butterfly-spreads
- momentum
- strangles
- algorithmic-trading
- expected-shortfall
- straddles
- basis-risk
- parametric-var
- conditional-var
- extreme-value-theory
- var-methodologies
- historical-var
- book-to-market
- arbitrage
- contango
- backwardation
- volatility-analysis
- covered-calls
- style-analysis
- option-strategies
- stress-testing
- clearinghouse
- market-efficiency
- marking-to-market
- value-at-risk
- order-flow
- arbitrage-pricing-theory
- multi-factor-models
- hedge-ratio
- bid-ask-spread
- iron-condors
- protective-puts
- price-discovery
- size-effect
- factor-models
- liquidity
- value-factor
- monte-carlo-var
- risk-management
- convergence
- options-trading
- var-backtesting
- futures-contracts
- roll-yield
- market-impact
- apt
- forward-contracts
- fama-french
type: note
---
--



# Determining the Stochastic Process for a Forward Contract from Ito’s Lemma 

Let $F=F(S,t)$ . Note that $F$ is once differentiable in $t$ and twice differentiable in $S$ . Ito's Lemma justifies the use of the following Taylor-series-like expansion for the instantaneous change in $F$ : 
$$ d F=\frac{\partial F}{\partial t}d t+\frac{\partial F}{\partial S}d S+\frac{1}{2}\frac{\partial^{2}F}{\partial S^{2}}d S^{2}. $$ 

Since $d S^{2}=S^{2}\sigma^{2}d t$ , substituting $S^{2}\sigma^{2}d t$ in place of $d S^{2}$ in the Ito's Lemma equation yields equation (2): 
$$ \frac{\partial F}{\partial t}d t+\frac{\partial F}{\partial S}d S+\frac{1}{2}\sigma^{2}S^{2}\frac{\partial^{2}F}{\partial S^{2}}d t $$ 

Since the instantaneous change in $S$ evolves according to the geometric Brownian motion (GBM) equation $d S=\mu S d t+\sigma S d z$ , substituting $\mu S d t+\sigma S d z$ in place of $d S$ in equation (2) yields: 
$$ d F=\left({\frac{\partial F}{\partial t}}+{\frac{\partial F}{\partial S}}\mu S+{\frac{1}{2}}\sigma^{2}S^{2}{\frac{\partial^{2}F}{\partial S^{2}}}\right)d t+{\frac{\partial F}{\partial S}}\sigma S d z $$ 

In equation (3), we refer to $\frac{\partial F}{\partial t}$ as “theta”, $\frac{∂F}{∂S}$ as “delta”, and $\frac{\partial^{2}{\cal F}}{\partial S^{2}}$ as “gamma”. Theta measures the effect that the passage of time has on $F$ , delta measures the sensitivity of $F$ with respect to changes in $S$ , and gamma captures the sensitivity of delta with respect to changes in $S$ . 

Next, consider a forward contract on a non-dividend paying stock; its date $t$ “arbitrage-free” price is $F=S e^{r(T-t)}$ . Since $\mathrm{theta}={\frac{\partial F}{\partial t}}=-r S e^{r(T-t)}$ , ${\mathrm{delta}}={\frac{\partial F}{\partial S}}=e^{r(T-t)}$ , and $\mathrm{{gamma}=}$ $\frac{\partial^{2}F}{\partial S^{2}}=0$ , we are now able to infer the stochastic process%20Process.md) for the price of the forward contract by substituting the values for theta, delta and gamma into equation (3): 
$$ d F=[e^{r(T-t)}\mu S-r S e^{r(T-t)}]d t+e^{r(T-t)}\sigma S d z. $$ 

Substituting $F$ in place of $S e^{r(T-t)}$ in equation (4), we obtain 
$$ d F=(\mu-r)F d t+\sigma F d z. $$ 

Note the difference in the drift rate for the forward contract vis-a-vis the drift rate for the underlying asset. Specifically, over infinitesimal units of time, the price of the forward contract grows at the rate of $(\mu-r)d t$ , whereas the underlying asset grows at the rate of µdt. Intuitively this is not a surprising result, particularly in view of the fact that the “arbitrage-free” price $F=S e^{r(T-t)}$ represents the future (date $T$ ) value of the date $t$ value of the underlying asset, compounded forward at the riskless rate of interest.

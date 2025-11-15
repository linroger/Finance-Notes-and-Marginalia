---
academic_level: graduate
aliases:
- Option Hedging
- Static Hedge
- Uncertain Volatility
enhanced: true
enhancement_date: '2025-11-06'
enhancement_id: batch09-000356
key_concepts:
- Black-Scholes option pricing model and continuous-time finance
- Options Greeks and sensitivity analysis for risk management
- Delta hedging and dynamic replication strategies
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
- Credit Risk Management and Default Probability
- Expected Loss and Loss Given Default Models
- Risk Measurement and VaR Backtesting
- Delta, Gamma, and Vega Hedging Techniques
- 'Greeks: Delta, Gamma, Theta, and Vega Hedging'
- Option Valuation and Exercise Strategies
- Value at Risk and Expected Shortfall
- Credit Spreads and Rating Migration Analysis
- Factor Models and Asset Pricing
- GARCH Models and Volatility Forecasting
- Cointegration and Statistical Arbitrage
- Hedging Strategies and Risk Mitigation
- Options Trading Strategies and Risk Management
- Dynamic vs Static Hedging in Practice
- Stress Testing and Extreme Value Analysis
- Time Series Analysis in Financial Markets
- Fama-French Factors and Style Analysis
- Arbitrage Pricing Theory and Multi-Factor Models
professional_application: theoreti
status: active
tags:
- arbitrage-opportunity
- arbitrage-pricing
- asset-allocation
- binomial-model
- black-scholes-model
- capital-asset-pricing
- caplet
- cds
- coherent-risk-measure
- collateralized-debt-obligation
- conditional-var
- continuous-time-pricing
- convexity
- convexity-adjustment
- counterparty-risk
- put-options
- state-space-models
- recovery-rate
- cross-hedging
- call-options
- butterfly-spreads
- momentum
- strangles
- expected-shortfall
- straddles
- parametric-var
- extreme-value-theory
- basis-risk
- var-methodologies
- historical-var
- hedge-strategies
- book-to-market
- volatility-modeling
- vega-hedging
- volatility-analysis
- regime-switching
- covered-calls
- ' exposure-at-default'
- style-analysis
- cointegration
- unit-roots
- option-strategies
- stress-testing
- roll-over-risk
- unexpected-loss
- mathematical-finance
- garch
- rating-migration
- expected-loss
- investment-analysis
- portfolio-optimization
- delta-hedging
- credit-migration
- default-probability
- quantitative-finance
- value-at-risk
- credit-spreads
- granger-causality
- arbitrage-pricing-theory
- multi-factor-models
- iron-condors
- protective-puts
- kalman-filter
- financial-markets
- probabilty-of-default
- static-hedging
- loss-given-default
- size-effect
- factor-models
- value-factor
- gamma-hedging
- dynamic-hedging
- hedge-effectiveness
- monte-carlo-var
- risk-management
- var-backtesting
- options-trading
- arima-models
- apt
- stationarity
- fama-french
type: note
---
--



# Uncertain Volatility with Static Hedge

We begin with the Black-Scholes equation for pricing a vanilla option contract which is a  parabolic PDE with two variables,  $S$   and  $t$   and with constant parameters such as  $r,D$  , and sigma  (volatility).  Instead of pricing the option with constant volatility, this assumption can be relaxed  and we can assume volatility to be parameter that lies within certain range.

Assume that volatility lies within the band
$$
\sigma^{-}<\sigma<\sigma^{+}
$$

Construct a portfolio consisting of the value of a long call option   $V(S,t)$  ,  and hedge it by shorting  -  $\cdot\Delta$   of the underlying asset. The value of the portfolio becomes
$$
\Pi=V-\Delta S\quad\mathrm{and}\qquad d s=u s d t+\sigma S d X
$$

The change in the value of the portfolio is
$$
\begin{array}{r}{d\Pi=\left(\frac{\partial V}{\partial t}+0.5\sigma^{2}\frac{\partial^{2}V}{\partial^{2}S}\right)d t+\left(\frac{\partial V}{\partial S}-\Delta\right)d s,\qquad d\Pi=\left(\frac{\partial V}{\partial t}+0.5\sigma^{2}\frac{\partial^{2}V}{\partial^{2}S}\right)d t}\end{array}
$$

Since volatility is unknown, we now assume long vanilla positions to take the lowest value of  the volatility range while short position takes the highest volatility value. The return of the  portfolio is set equal to the risk-free rate.
$$
\operatorname*{min}_{\sigma^{-}<\sigma<\sigma^{+}}(\mathrm{d}\Pi)=\mathrm{r}\Pi\mathrm{d}\mathrm{t}
$$

We set
$$
\begin{array}{r}{\underset{\sigma^{-}<\sigma<\sigma^{+}}{\operatorname*{min}}\left(\frac{\partial V}{\partial t}+0.5\sigma^{2}\frac{\partial^{2}V}{\partial^{2}S}\right)d t=\left(V-S\frac{\partial V}{\partial S}\right)d t}\end{array}
$$

The value that the volatility takes depends sign of Gamma  (Γ)  and the worst-case value  satisfies 1
$$
\begin{array}{r}{\frac{\partial V^{-}}{\partial t}+0.5\sigma\left(\Gamma\right)^{2}\frac{\partial^{2}V^{-}}{\partial^{2}S}+r S\frac{\partial V^{-}}{\partial S}-r V^{-}=0}\end{array}
$$

Where
$$
\Gamma=\frac{\partial^{2}V^{-}}{\partial^{2}S}
$$

and
$$
\sigma(\Gamma)=\sigma^{+}\,i f\,\,\,\Gamma<0
$$$$
\sigma(\Gamma)=\sigma^{-}\,i f\,\,\,\Gamma>0
$$

The worst-case scenario for a delta hedged long vanilla option is if volatility is low while the  opposite is true for a delta hedged short vanilla option.

The best option value, and hence the range of possible values can be found by solving
$$
\begin{array}{r}{\frac{\partial V^{-}}{\partial t}+0.5\sigma\left(\Gamma\right)^{2}\frac{\partial^{2}V^{-}}{\partial^{2}S}+r S\frac{\partial V^{-}}{\partial S}-r V^{-}=0}\end{array}
$$

Where
$$
\begin{array}{r}{\Gamma=\frac{\partial^{2}V^{-}}{\partial^{2}S}}\end{array}
$$

and
$$
\begin{array}{c}{{\sigma(\Gamma)=\sigma^{+}\,i f\,\,\,\Gamma<0}}\\ {{{}}}\\ {{\sigma(\Gamma)=\sigma^{-}\,i f\,\,\,\Gamma>0}}\end{array}
$$

# Static Hedging

Unlike delta hedging, static hedging does not require dynamic rebalancing of the hedged  portfolio. For example, suppose we have long position of a digital option which we would like  to hedge. To hedge the position, we can use call spread and discrete hedge the position from  time to time., However, instead of continues rebalancing, we can set up a one time hedge with  the same instrument as above (call spread) but with an optimum number of call spread to use  for the static hedge.

Consider the following example; suppose we want to buy a call option with strike price  $K_{1}$  with  the following payoff:
$$
P=M a x(S-K_{1},0)
$$

To hedge the above call position, we short another call with strike   $K_{2}$   and a  payoff    $P_{2}=M a x(S-K_{2},0)$  . The difference in the payoffs is then
$$
D i f f=M a x(S-K_{1})-\lambda M a x(S-K_{2},0)
$$

Were  $\lambda$   is the number of short positions we need to hedge the long call position. This portfolio  is said to be statically hedged and it has smaller payoff then the unhedged call.

To value the residual payoff (Diff) in the uncertain parameter framework, one needs to solve
$$
\begin{array}{r}{\frac{\partial V^{-}}{\partial t}+0.5\sigma\left(\Gamma\right)^{2}\frac{\partial^{2}V^{-}}{\partial^{2}S}+r S\frac{\partial V^{-}}{\partial S}-r V^{-}=0}\end{array}
$$

With the final condition
$$
V(S,T)=M a x(S-K_{1})-\lambda M a x(S-K_{2},0)
$$
To find the optimum hedge, we solve for the optimum number of calls to short. So, given  market price for the original call, the statically hedged portfolio with the final condition and  with the optimum hedge should produce more tighter spread using the volatility scenario under  the static hedge and uncertain parameter framework.

We initially price up the digital call option and produce its payoff chart at expiry. To hedge the  digital call option we use a portfolio of long and short call options. As stated above, we price  up these options individually and show their payoff at expiry.

 !500
Figure 2.1 Digital Call

To hedge the digital call option with strike price of 100, we use initially a short call option with  a quantity of 0.05 and long call position with quantity of 0.05. Assume the calls have market  prices as given in table below

 !500
The cost of setting up the hedge is

Hedging Cost  $=$      $-0.05\mathrm{~x~}14.42+0.05\mathrm{~x~}4.22\ \ =-0.51$  -0.05 x 14.42 + 0.05 x 4.22   = -0.51

We solve
$$
\frac{\partial V^{-}}{\partial t}+0.5\sigma\left(\Gamma\right)^{2}\frac{\partial^{2}V^{-}}{\partial^{2}S}+r S\frac{\partial V^{-}}{\partial S}-r V^{-}=0
$$

With the final condition
$$
V(S,T)=M a x(S-K_{1})-\lambda M a x(S-K_{2},0)
$$
We deduct the result from the cost of setting up the hedge.

We repeat this process but this time we use the opposite scenario for the volatility and we  deduct the result from the cost of setting up the hedge.

The difference from both results should produce tighter price spread then what would have  been quoted for the original unhedged digital call option. To find the optimum number of calls  to sell and buy, we can use solver in excel.

 !500
Figure 2.2

Technical Problem.

Due to the copy office package currently running on my PC, the solver is NOT available and  downloading this add-in is also still causing some technical problems. See screen grab below.

 !500
# References

M. Avellaneda, A. Levy, A. Paras,  “Pricing and hedging derivative securities in markets with uncertain  vol at ili ties” , Journal of   Applied Finance, Vol 1, 1995

Paul Wilmott,  P.Wilmott on Quantitative Finance”,  $2^{n d}$   Edition, Volume 3, Wiley.     CQF  Lecture 2010/2011 – Heath, Jarrow and Morton Model     CQF Lecture 2010/ 2011 - Advanced Volatility Modelling in Complete Markets     P. Wilmott, A. Oztukel, “

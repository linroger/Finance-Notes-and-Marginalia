---
academic_level: graduate
aliases:
- BS formula
- Black-Scholes formula
cssclasses: academia
enhanced: true
enhancement_date: '2025-11-06'
enhancement_id: batch09-000097
key_concepts:
- Black-Scholes option pricing model and continuous-time finance
- Binomial option pricing model and lattice methods
- Options Greeks and sensitivity analysis for risk management
- Delta hedging and dynamic replication strategies
- Risk-neutral measures and martingale pricing
- Ito's lemma and stochastic calculus applications
- Martingale theory and change of measure
- Duration analysis and interest rate risk management
- Convexity adjustments and yield curve sensitivity
- Discounted cash flow (DCF) valuation methodology
- Capital Asset Pricing Model (CAPM) and expected returns
- Weighted Average Cost of Capital (WACC) and firm valuation
- Value at Risk (VaR) and tail risk measurement
- Expected shortfall and coherent risk measures
- Arbitrage opportunities and no-arbitrage pricing
- Factor models and multi-factor pricing
- Volatility modeling and estimation techniques
- Risk preference theory and utility functions
- Sensitivity analysis and Greeks calculation
- 'Valuation Methods: DCF, Comps, and Precedents'
- Ito's Lemma and Lognormal Asset Price Dynamics
- Risk-Neutral Valuation in Option Pricing
- Value at Risk and Expected Shortfall
- Vasicek Interest Rate Model and Mean Reversion
- Short Rate Models and Term Structure Dynamics
- Company Valuation and Multiple Analysis
- Capital Asset Pricing Model and Beta Analysis
- Credit Risk Management and Default Probability
- Expected Loss and Loss Given Default Models
- Delta, Gamma, and Vega Hedging Techniques
- Comparable Company Analysis and Trading Multiples
- 'Greeks: Delta, Gamma, Theta, and Vega Hedging'
- Ornstein-Uhlenbeck Process in Finance
- Price Discovery and Market Efficiency
- Cost of Equity and Expected Returns
- Black-Scholes Option Pricing Model and Its Applications
- Security Market Line and Risk-Return Tradeoff
- Options Trading Strategies and Risk Management
- Stress Testing and Extreme Value Analysis
- Lattice Methods and Recombining Trees in Derivatives Pricing
- Fama-French Factors and Style Analysis
- Risk Measurement and VaR Backtesting
- Bid-Ask Spreads and Market Impact
- Contango, Backwardation, and Roll Yield
- Futures and Forward Contracts in Financial Markets
- Binomial Option Pricing Model for Discrete Time Valuation
- Hedge Strategies and Basis Risk Management
- Dynamic vs Static Hedging in Practice
- American Option Pricing and Early Exercise Premium
- Option Valuation and Exercise Strategies
- Market Microstructure and Liquidity Analysis
- Credit Spreads and Rating Migration Analysis
- Hedging Strategies and Risk Mitigation
- Factor Models and Asset Pricing
- Arbitrage Pricing Theory and Multi-Factor Models
professional_application: theoreti
status: active
tags:
- all-or-nothing
- arbitrage-opportunity
- arbitrage-pricing
- asset-allocation
- binary-derivatives
- binomial-model
- black-scholes-model
- capital-asset-pricing
- capital-structure
- caplet
- cash-flow-modeling
- coherent-risk-measure
- conditional-var
- continuous-time-pricing
- convexity-adjustment
- leveraged-buyout
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
- backwardation
- volatility-analysis
- style-analysis
- option-strategies
- unexpected-loss
- capital-asset-pricing-model
- clearinghouse
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
- contango
- vega-hedging
- expected-loss
- market-efficiency
- delta-hedging
- quantitative-finance
- order-flow
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
- discrete-time-pricing
- hedge-strategies
- covered-calls
- ' exposure-at-default'
- stress-testing
- roll-over-risk
- mathematical-finance
- ornstein-uhlenbeck
- rating-migration
- comparable-analysis
- investment-analysis
- economic-value-added
- portfolio-optimization
- value-at-risk
- factor-models
- risk-management
- convergence
- var-backtesting
- cross-hedging
- sum-of-parts
- european-options
- high-frequency-trading
- lattice-models
- strangles
- cox-ross-rubinstein
- short-rate-models
- optional-exercise
- efficient-frontier
- credit-migration
- default-probability
- marking-to-market
- binomial-option-pricing
- credit-spreads
- multi-factor-models
- ito-calculus
- trading-multiples
- iron-condors
- option-pricing
- financial-markets
- static-hedging
- size-effect
- precedent-transactions
- lognormal-distribution
- ipo-valuation
- market-multiple
- ' recombining-trees'
- futures-contracts
- apt
title: Black Scholes Formula
type: note
---
--



# Black Scholes Formula

These notes examine the Black-Scholes formula for European options. The Black-Scholes formula is complex as it is based on the geometric Brownian motion assumption for the underlying asset price. Nevertheless, it can be interpreted and is easy to use once understood. We start off by examining digital or binary options, which are easy and intuitive to price. We shall show how the Black-Scholes formula can be derived and derive and justify the Black-Scholes-Merton partial differential equation.

Keywords: Black-Scholes formula, Black-Scholes-Merton partial differential equation, replication, self-financing portfolio, martingale pricing, boundary conditions, PDE.

## Digital Options

To help understand the Black-Scholes formula for call and put options, we start by looking at digital options. Digital options are very simple. A digital call with a strike price $K$ and maturity date $T$ pays out one unit if $S(T)>K$ and nothing otherwise. Likewise, a digital put with a strike price $K$ and maturity date $T$ pays out one unit if $S(T)<K$ and nothing otherwise.

Thus, for a digital call option, the payoff at maturity is:
$$c^b(T)=\begin{cases}0 & \text{if } S(T)\leq K \\ 1 & \text{if } S(T)>K \end{cases}$$

And the payoff at maturity to a digital put option is:
$$p^b(T)=\begin{cases}1 & \text{if } S(T)\leq K \\ 0 & \text{if } S(T)>K \end{cases}$$

We now show how to value the digital call option. The end price $S_T$ is a random variable. We have by assumption that $\ln S(T)$ is normally distributed with
$$\operatorname{E}[\ln S(T)]=\ln S(0)+\left(\mu - \frac{1}{2}\sigma[^2]\right)T$$

And
$$\mathrm{Var}[\ln S(T)]=\sigma[^2] T.$$

Thus
$$\frac{\ln S(T) - \ln S(0) - \left(\mu - \frac{1}{2}\sigma[^2]\right)T}{\sigma\sqrt{T}}$$

Is a standard normal variable with expected value of zero and standard deviation of one. We want to know the probability that the call option is exercised. The call option is exercised if $S_T>K$ or equivalently if $\ln S(T)>\ln K$. Thus, the probability of exercise is given by $1 - N(x^*)$ where
$$x^*=\frac{\ln K - \ln S(0) - \left(\mu - \frac{1}{2}\sigma[^2]\right)T}{\sigma\sqrt{T}}$$

As we have seen, options can be evaluated using risk-neutral pricing, that is, as if all assets earn the same rate of return as the riskless asset. Thus, we replace $\mu$ by $r$ in the above equation to get
$$x=\frac{\ln K-\ln S(0)-\left(r-\frac{1}{2}\sigma[^2]\right)T}{\sigma\sqrt{T}}.$$

Thus, the probability of exercise in a risk-neutral world is $1-N(x)=N(-x)$. The call option pays out one unit if it is exercised but only after $T$ periods. Thus, the expected discounted value of the digital call option is
$$c^b(0)=e^{-rT}N(-x).$$

There is a simple condition for put-call parity for digital options. This is given by
$$c^b(0)+p^b(0)=e^{-rT}$$

Since if one buys a digital call and a digital put with the same strike price and maturity date, one is sure to have one unit at time $T$ no matter what the price of the underlying asset. Hence, the put price satisfies
$$p^b(0)=e^{-rT}-c^b(0)=e^{-rT}-e^{-rT}N(-x)=e^{-rT}(1-N(-x))=e^{-rT}N(x).$$

Equivalently, we can see that the risk-neutral probability that $S_{T}<K$ is given by $N(x)$ and hence the value of the binary or digital put is $e^{-rT}N(x)$ where $x$ is given above.

## The Black-Scholes Formula

Plain options have slightly more complex payoffs than digital options, but the principles for calculating the option value are the same.

The payoff to a European call option with strike price $K$ at the maturity date $T$ is
$$c(T)=\max[S(T)-K, 0]$$

Where $S(T)$ is the price of the underlying asset at the maturity date. At maturity, if $S(T)>K$, the option to buy the underlying at $K$ can be exercised, and the underlying asset immediately sold for $S(T)$ to give a net payoff of $S(T) - K$. Since the option gives only the right and not the obligation to buy the underlying asset, the option to buy the underlying will not be exercised if doing so would lead to a loss, $S(T) - K<0$. The Black-Scholes formula for the price of the call option at date $t=0$ prior to maturity is given by
$$c(0)=S(0)N(d_1) - e^{-rT}KN(d_2)$$

Where $N(d)$ is the cumulative probability distribution for a variable that has a standard normal distribution with a mean of zero and a standard deviation of one. It is the area under the standard normal density function from $-\infty$ to $d$ and therefore gives the probability that a random draw from the standard normal distribution will have a value less than or equal to $d$. We have therefore that $0 \leq N(d) \leq 1$ with $N(-\infty)=0$, $N(0)=\frac{1}{2}$, and $N(+\infty)=1$. The term $r$ is the continuously compounded risk-free rate of interest, and $d_1$ and $d_2$ satisfy
$$\begin{array}{rcl}
d_1 &=& \frac{\ln(\frac{S(0)}{K})+(r+\frac{1}{2}\sigma[^2])T}{\sigma\sqrt{T}} \\\\
d_2 &=& d_1-\sigma\sqrt{T}=\frac{\ln(\frac{S(0)}{K})+(r-\frac{1}{2}\sigma[^2])T}{\sigma\sqrt{T}}
\end{array}$$

Here $\sigma^{2}$ is the variance of the continuously compounded rate of return on the underlying asset.

Likewise, the payoff to a European put option with strike price $K$ at the maturity date $T$ is
$$p(T)=\max[K-S(T), 0]$$

As the put option gives the right to sell the underlying asset at the strike price of $K$. The Black-Scholes formula for the price of the put option at date $t=0$ prior to maturity is given by
$$p(0)=c(0)+e^{-rT}K-S(0)=e^{-rT}K(1-N(d_2))-S(0)(1-N(d_1))$$

Where $d_{1}$ and $d_{2}$ are defined above. By the symmetry of the standard normal distribution $N(-d)=(1-N(d))$, the formula for the put option is usually written as
$$p(0)=e^{-rT}KN(-d_2)-S(0)N(-d_1).$$

### Interpretation of the Formula

Rewrite the Black-Scholes formula as
$$c(0)=e^{-rT}\begin{pmatrix}S(0)e^{rT}N(d_1)-KN(d_2)\end{pmatrix}.$$

The formula can be interpreted as follows. If the call option is exercised at the maturity date, then the holder gets the stock worth $S(T)$ but has to pay the strike price $K$. But this exchange takes place only if the call finishes in the money. Thus $S(0)e^{rT}N(d_{1})$ represents the future value of the underlying asset conditional on the end stock value $S(T)$ being greater than the strike price $K$. The second term in the brackets $KN(d_{2})$ is the value of the known payment $K$ times the probability that the strike price will be paid $N(d_{2})$. The terms inside the brackets are discounted by the risk-free rate $r$ to bring the payments into present value terms. Thus the evaluation inside the brackets is made using the risk-neutral or martingale probabilities. The term $N(d_{2})$ represents the probability that the call finishes in the money where $d_{2}$ is also evaluated using the risk-free rate.

Remember that in a risk-neutral world all assets earn the risk-free rate. We are assuming the logarithm of the stock price is normally distributed. Thus the expected continuously compounded rate of return in a risk-neutral world is equal to $r-\frac{1}{2}\sigma^{2}$ where the variance is deducted to calculate the certainty equivalent rate of return. Therefore at time $T$, $\ln S(T)$ is normally distributed with a mean value of $\ln S(0)+(r-\frac{1}{2}\sigma^{2})T$ and a standard deviation of $\sigma\sqrt{T}$. Thus
$$\frac{\ln S(T)-(\ln S(0)+(r-\frac{1}{2}\sigma[^2])T)}{\sigma\sqrt{T}}$$

is a standard normal variable. The probability that $S(T)<K$ is therefore given by $N(-d_{2})$ and the probability that $S(T)>K$ is given by $1-N(-d_{2})=N(d_{2})$.

It is more complicated to show that $S(0)e^{rT}N(d_{1})$ is the future value of the underlying asset in a risk-neutral world conditional on $S(T)>K$ but a proof can be found in more advanced textbooks.

The formula also has another useful interpretation. From our analysis of the binomial model we know that the value of the call is
$$c(0)=S(0)\Delta - B$$

Where $\Delta$ is the amount of the underlying asset bought and $B$ is the amount of money borrowed needed to synthesize the call option. From the formula, therefore, $N(d_{1})$ is the hedge parameter indicating the number of shares bought and $e^{-rT}KN(d_{2})$ indicates the amount of cash borrowed to part finance the share purchase. Since $0 \leq N(d) \leq 1$, the formula shows that the replicating portfolio consists of a fraction of the underlying asset and a positive amount of cash borrowed. The $\Delta$ of this formula is also found by partially differentiating the call price formula
$$\frac{\partial c(0)}{\partial S(0)}=\Delta.$$

It is the slope of the curve relating the option price with the price of the underlying asset. The cost of buying $\Delta$ units of the stock and writing one call option is $S(0)\Delta - c(0)$. This portfolio is said to be delta neutral as a small change in the stock price will not affect the value of the portfolio.

### Boundary Conditions

We shall consider the boundary conditions for the call option. Consider first the boundary condition for the call at expiration when $T=0$. To do this, consider the formula for the call option as $T \longrightarrow 0$, that is, as the time until maturity goes to zero. At maturity, $c(T)=\operatorname*{max}[S(T)-K, 0]$ so we need to show that as $T \longrightarrow 0$ the formula converges to $c(0) = \operatorname*{max}[S(0)-K, 0]$. If $S(0)>K$ then $\ln(\frac{S(0)}{K})>0$ so that as $T \longrightarrow 0$, $d_{1}$ and $d_{2} \to +\infty$. Thus $N(d_{1})$ and $N(d_{2}) \to 1$. Since $e^{-rT} \to 1$ as $T \longrightarrow 0$ we have that $c(0) \longrightarrow S(0)-K$ if $S(0)>K$. Alternatively, if $S(0)<K$ then $\ln(\frac{S(0)}{K})<0$ so that as $T \longrightarrow 0$ $d_{1}$ and $d_{2} \rightarrow -\infty$ and hence $N(d_{1})$ and $N(d_{2}) \to 0$. Thus $c(0) \longrightarrow 0$ if $S(0)<K$. This is precisely as expected. If the option is in the money at maturity, $S(0)>K$, it is exercised for a profit of $S(0)-K$ and if it is out of the money, $S(0)<K$, the option expires unexercised and valueless.

As another example, consider what happens as $\sigma \rightarrow 0$. In this case, the underlying asset becomes riskless and grows at the constant rate of $r$. Thus, the future value of the stock is $S(T)=e^{rT}S(0)$ and the payoff to the call option at maturity is $\operatorname*{max}[e^{rT}S(0)-K, 0]$. Thus, the value of the call at date $t=0$ is $\operatorname*{max}[S(0)-e^{-rT}K, 0]$. To see this from the formula, first consider the case where $S(0)-e^{-rT}K>0$ or $\ln(\frac{S(0)}{K})+rT>0$. Then, as $\sigma \longrightarrow 0$, $d_{1}$ and $d_{2} \to +\infty$ and hence $N(d_{1})$ and $N(d_{2}) \to 1$. Thus, $c(0) \to S(0)-e^{-rT}K$. Likewise, when $S(0)-e^{-rT}K<0$ or $\ln(\frac{S(0)}{K})+rT<0$, then $d_{1}$ and $d_{2} \to -\infty$ as $\sigma \rightarrow 0$. Hence, $N(d_{1})$ and $N(d_{2}) \to 0$ and so $c(0) \to 0$. Thus, combining both conditions, $c(0) \longrightarrow \operatorname*{max}[S(0)-e^{-rT}K, 0]$ as $\sigma \rightarrow 0$.

## At-the-money Options

Consider an option that is currently at-the-money, $S(0)=K$. Then, the formula for the call option becomes
$$c(0)=S(0)\begin{pmatrix}N(d_1)-e^{-rT}N(d_2)\end{pmatrix}$$

Where
$$d_1=\frac{(r+\frac{1}{2}\sigma[^2])T}{\sigma\sqrt{T}}; \quad d_2=d_1-\sigma\sqrt{T}.$$

Thus, the price of an at-the-money call option is simply a fraction of the price of the underlying.

There is an even more convenient approximation if we take $K=S(0)e^{rT}$ that is where the strike price is the forward price of the underlying asset. Then
$$c(0)=S(0)(N(d_1)-N(d_2))$$

And
$$d_1=\frac{\ln(\frac{S(0)}{K})+(r+\frac{1}{2}\sigma[^2])T}{\sigma\sqrt{T}}=\frac{\frac{1}{2}\sigma[^2]T}{\sigma\sqrt{T}}=\frac{1}{2}\sigma\sqrt{T}$$

And $d_{2}=-\frac{1}{2}\sigma\sqrt{T}$. By Taylor's theorem, expanding $N(x)$ about $x=0$ gives
$$N(x) \approx N(0)+xN'(0)+\frac{1}{2}x^{2}N''(0).$$

Thus we have
$$\begin{aligned}
N(d_1)-N(d_2) &\approx \left(N(0)+d_1N'(0)+\frac{1}{2}d_1[^2]N''(0)\right)\\
&-\left(N(0)+d_2N'(0)+\frac{1}{2}d_2[^2]N''(0)\right)
\end{aligned}$$

Hence since $d_{1}^{2}=d_{2}^{2}$ and $d_{1}=-d_{2}=\frac{1}{2}\sigma\sqrt{T}$ we have
$$c(0) \approx S(0)(N'(0)\sigma\sqrt{T})$$

And since $N'(0)=\frac{1}{\sqrt{2\pi}}$ we have
$$c(0) \approx \frac{S(0)\sigma\sqrt{T}}{\sqrt{2\pi}} \approx 0.4S(0)\sigma\sqrt{T}.$$

This can be used as a rough and ready method for calculating the implied volatility if the price is known. Note this formula applies equally to puts as well as calls.

## The Black-Scholes-Merton Partial Differential Equation

We wish to price a call on an underlying stock. Assume that the time to maturity is $T$ and the strike price is $K$ the volatility of the underlying asset is $\sigma$. We assume that the underlying asset follows a geometric Brownian motion process
$$dS(t)=\mu S(t)dt+\sigma S(t)dz(t)$$

where $dz$ is a Wiener process, i.e. has zero mean and unit variance, and increments are independent. We assume there is a risk-free asset that has a constant continuously compounded rate of return of $r$, so that a money market account follows the process
$$dB(t)=rB(t)dt.$$

The latter is equivalent to $B(t)=B(0)e^{rt}$. The excess return on the stock is $\mu-r$, and the ratio $\lambda=(\mu-r)/\sigma$ is known as the market price of risk. The call option changes value over time as the stock price and the time to maturity change, and therefore we can write the call price $c(S(t), t)$

The objective is to show that $c(S(t), t)$ is well defined (there is a unique price) and describe how the call price depends on $S(t)$ and $t$

Since $c(S(t), t)$ is just a function, we can apply Ito's lemma to derive
$$dc=\left(\frac{\partial c}{\partial t}+\mu S\frac{\partial c}{\partial S}+\frac{1}{2}\sigma[^2]S[^2]\frac{\partial[^2]c}{\partial S[^2]}\right)dt+\sigma S\frac{\partial c}{\partial S}dz.$$

We now consider a portfolio of one option and $\Delta$ units of the underlying itself. The process for this portfolio is
$$d(c+\Delta S)=\left(\frac{\partial c}{\partial t}+\mu S\frac{\partial c}{\partial S}+\frac{1}{2}\sigma[^2]S[^2]\frac{\partial[^2]c}{\partial S[^2]}+\Delta\mu S\right)dt+\left(\frac{\partial c}{\partial S}+\Delta\right)\sigma Sdz.$$

Now setting $\Delta=-\partial c/\partial S$ eliminates the random $dz$ term to give
$$d(c+\Delta S)=\left(\frac{\partial c}{\partial t}+\frac{1}{2}\sigma[^2]S[^2]\frac{\partial[^2]c}{\partial S[^2]}\right)dt.$$

This is our $\Delta$-hedged portfolio which has eliminated all risk. Since this portfolio is riskless, it must satisfy exactly the same equation as the money-market account, i.e.
$$d(c+\Delta S)=r(c+\Delta S)dt$$

And hence we have by equating these two terms that
$$\left(\frac{\partial c}{\partial t}+\frac{1}{2}\sigma[^2]S[^2]\frac{\partial[^2]c}{\partial S[^2]}\right)=r\left(c-\frac{\partial c}{\partial S}S\right)$$

Where we've replaced $\Delta$ by $-\partial c/\partial S$. Rewriting, we have
$$\frac{\partial c}{\partial t}+rS\frac{\partial c}{\partial S}+\frac{1}{2}\sigma[^2]S[^2]\frac{\partial[^2]c}{\partial S[^2]}-rc=0.$$

This is a second-order partial differential equation (PDE). It is known as the Black-Scholes-Merton Partial Differential Equation. Indeed, since we did not yet specify anything about the nature of the option, this equation will apply to any derivative security. What determines how the equation applies to a particular derivative is given by the boundary condition. For the call option, we have the boundary condition that at maturity
$$c(S(T), T)=\max\{S(T)-K, 0\}.$$

Solving this second-order differential equation together with the boundary condition gives the Black-Scholes formula we have seen before
$$c(0)=S(0)N(d_1)-e^{-rT}KN(d_2)$$

Where $d_{1}$ and $d_{2}$ satisfy
$$\begin{array}{rcl}
d_1 &=& \frac{\ln(\frac{S(0)}{K})+(r+\frac{1}{2}\sigma[^2])T}{\sigma\sqrt{T}} \\\\
d_2 &=& d_1-\sigma\sqrt{T}=\frac{\ln(\frac{S(0)}{K})+(r-\frac{1}{2}\sigma[^2])T}{\sigma\sqrt{T}}.
\end{array}$$

## A Replication Argument

We consider a portfolio that invests $\alpha$ in the underlying asset and $\beta$ in the risk-free asset.

The value of this portfolio at the initial date is
$$P(0)=\alpha S(0)+\beta B(0).$$

We shall require that this strategy is both replicating and self-financing. A portfolio is self-financing if it involves no injection or extraction of cash at any time and thus the change in the value of the portfolio depends on how the stock price and value of the risk-free asset change. Thus the portfolio is self-financing if and only if
$$dP=\alpha dS+\beta dB.$$

To satisfy this equation, $\alpha$ and $\beta$ will in general be changing over time and as $S(t)$ varies. However, it is also clear that once $\alpha(S(t), t)$ is specified, $\beta(S(t), t)$ is determined as well by the fact that the portfolio is self-financing and thus has to satisfy the above equation. We shall follow what we did in the previous section and suppose that $\alpha=\partial c/\partial S$. Here, we are taking a long position in the stock as we are trying to replicate the portfolio (whereas in the previous section, we were taking a short position to hedge out the risk of the option itself). We want to show that the value of the portfolio equals the value of the call at every instant. That is, we want to show that $P(S(t), t)=c(S(t), t)$. Therefore, we consider the difference
$$\begin{aligned}
d(P(S(t), t)-c(S(t), t)) &= dP-dc \\
&= \alpha(S, t)dS+\beta(S, t)dB \\
&- \left(\frac{\partial c}{\partial t}+\mu S\frac{\partial c}{\partial S}+\frac{1}{2}\sigma^{2}S^{2}\frac{\partial^{2}c}{\partial S^{2}}\right)dt-\sigma S\frac{\partial c}{\partial S}dz.
\end{aligned}$$

Then substituting for $dS$, $dB$, and $\alpha(S, t)$ gives
$$d(P(S(t), t)-c(S(t), t))=\left(\beta(S, t)rB-\frac{\partial c}{\partial t}-\frac{1}{2}\sigma[^2]S[^2]\frac{\partial[^2]c}{\partial S[^2]}\right)dt.$$

Again, the risk has been eliminated from this equation. Then, using the Black-Scholes equation gives
$$d(P(S(t), t)-c(S(t), t))=\left(\beta(S, t)rB-r\left(c-S\frac{\partial c}{\partial S}\right)\right)dt$$

And since $\beta(S, t)B=P(S, t)-\alpha(S, t)S$, this gives
$$\begin{aligned}
d(P(S(t), t)-c(S(t), t)) &= r\left(P(S, t)-\alpha(S, t)S\right)dt-r\left(c-S\frac{\partial c}{\partial S}\right)dt \\
&= r\left(P(S, t)-c(S, t)\right)dt.
\end{aligned}$$

Let $D(S, t)=P(S, t)-c(S, t)$. By construction, we want the portfolio to be replicating, so $P(S(0), 0)=c(S(0), 0)$ and hence $D(S, 0)=0$. But we have from the above equation that $dD=rD(S, t)dt$ and so $D(S, t)=D(S, 0)e^{rt}=0$. Thus, the portfolio, because it is self-financing and all risk has been hedged away, replicates the call value at every instant. Moreover, unlike the previous argument which assumed a call value function $c(S, t)$ and differentiated, the present approach proves the existence of this value and shows that it is well-defined.

## Martingale Pricing

We now consider the ratio $\varrho(t)=S(t)/B(t)$. In the binomial case, we have seen that this is a martingale, so that the ratio $\varrho(t)$ satisfies the property $\mathrm{E}_{*}[x(t+1)]=x(t)$, where the expectation is taken using the risk-neutral probabilities. Equivalently, we have $\mathrm{E}_{*}[x(t+1)-x(t)]=0$ or, in the limit, $\mathrm{E}_{*}[dx(t)]=0$.

Using the equations above for $S(t)$ and $B(t)$, we have, upon differentiation, that
$$d\varrho(t)=\frac{dS(t)}{B(t)}+S(t)d(B(t)^{-1}).$$

We have $d(B(t)^{-1})=-rB(t)^{-1}dt$, so that
$$\begin{aligned}
d\varrho(t) &= \frac{1}{B(t)}(\mu S(t)dt+\sigma S(t)dz)-\frac{1}{B(t)}rSdt \\
&= (\mu-r)\varrho(t)dt+\sigma\varrho(t)dz.
\end{aligned}$$

This does not satisfy the martingale property because the drift rate is not equal to $r$. We remember, however, that in the binomial model, we never had to specify the true probabilities but could derive risk-neutral probabilities.

We can do something similar here by changing the probabilities or measure of the distribution. It turns out that if we specify a process $\tilde{z}=z-\eta t$ where $z$ is a Wiener process, then so too is $\tilde{z}$. Thus
$$d\varrho(t)=(\mu-r)\varrho(t)dt+\sigma\varrho(t)d\tilde{z}+\sigma\varrho(t)\eta dt.$$

If we choose $\eta$ to be equal to the market price of risk, $\lambda=(\mu-r)/\sigma$, then the drift terms cancel out and $\varrho(t)$ is a martingale, that is, $d\varrho(t)=\sigma\varrho(t)d\tilde{z}$. Hence, since $dB(t)=rB(t)dt$, we get
$$d\varrho(t)=\frac{dS(t)}{B(t)}-\frac{rS(t)}{B(t)}dt=\sigma\frac{S(t)}{B(t)}d\tilde{z}$$

Or, after cancelling out the $B(t)$ term and rewriting,
$$dS(t)=rS(t)dt+\sigma S(t)d\tilde{z}$$

So that $S(t)$ is a geometric Brownian motion process using the new variable $\tilde{z}$. Here, the drift with the new variable is just the risk-free rate. It is as if we are in a risk-neutral world and all assets are growing at the same expected rate equal to the risk-free rate.

We can then proceed as before to show that
$$\frac{\ln S(T)-\ln S(0)-(r-\frac{1}{2}\sigma[^2])T}{\sigma\sqrt{T}}$$

Is a standard normal variable with mean zero and unit variance. The value of a call option can be calculated as the discounted value of the expected intrinsic value using the risk-neutral expectation. That is,
$$c(0)=e^{-rT}\mathrm{E}_*[\max\{S(T)-K, 0\}].$$

Thus, we need to calculate the expected value of $S(T)-K$ conditional on the option ending in the money, $S(T)>K$. The value of the option consists of two parts: the future value of the underlying asset conditional on $S(T)>K$ and the strike price paid times the probability the option is exercised. The probability the option is exercised is the probability $S(T)>K$. This will be given by $1-N(x)$ where
$$x=\frac{\ln K-\ln S(0)-(r-\frac{1}{2}\sigma[^2])T}{\sigma\sqrt{T}}.$$

Since $1-N(x)=N(-x)$ the probability of exercise is $N(d_{2})$ where
$$-x=d_2=\frac{\ln(S(0)/K)+(r-\frac{1}{2}\sigma[^2])T}{\sigma\sqrt{T}}.$$

It can also be shown by integration that the expected future value of the underlying asset conditional on $S(T)>K$ is $S(0)e^{rT}N(d_{1})$ where $d_{1}=d_{2}+\sigma\sqrt{T}$. Hence
$$c(0)=e^{-rT}(S(0)e^{rT}N(d_1)-KN(d_2))$$

Which is the Black-Scholes formula.

## Summary

We have considered three ways in which the Black-Scholes formula may be derived. The first is to develop a second-order partial differential equation by creating a riskless portfolio by dynamically $\Delta$-hedging. The second is to synthesize the option by using the underlying and the risk-free asset. This second method is more satisfactory as it does not assume the existence of a well-defined option price but derives it from the assumption that all arbitrage opportunities are eliminated in the market. The third method considers replacing actual probabilities by fictitious risk-neutral probabilities so that all assets satisfy a martingale property. This then allows one to replace the actual return on the underlying asset with the risk-free rate. This allows a straightforward derivation of the formula.

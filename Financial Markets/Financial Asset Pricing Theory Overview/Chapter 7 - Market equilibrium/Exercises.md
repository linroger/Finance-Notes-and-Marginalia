---
tags:
- aggregate_consumption
- artificial-intelligence
- banking
- beta
- brownian_motion
- consumption
- defi
- discrete_time_economy
- interest-rate-derivatives
- ma
- market_completeness
- markets
- mpt
- option-greeks
- options
- options-pricing
- risk-management
- risk_aversion
- sharpe-ratio
- state_price
- state_price_deflator
- stochastic
- utility_function
aliases:
- exercise 7.1
- exercise 7.2
- exercise 7.3
- exercise 7.4
- exercise 7.5
- exercise 7.6
- exercise 7.7
key_concepts:
- Agricultural futures and seasonality
- Alternative investments and hedge fund strategies
- American vs European options and early exercise features
- Asset swaps and spread-lock strategies
- Bank asset-liability management (ALM) strategies
- Bank capital adequacy and Basel III compliance
- Bank stress testing and CCAR requirements
- Barrier options and knock-in/knock-out structures
- Basis swaps and cross-currency basis adjustments
- Basis swaps and floating rate correlations
- Behavioral finance and market anomalies
- Best execution and regulatory requirements
- Bid-ask spreads and market making profitability
- Binomial option pricing model with multi-period trees
- Black-Litterman model and portfolio optimization
- Black-Scholes option pricing model and its applications
- Bond portfolio immunization strategies
- Brownian motion and Wiener processes
- Brownian motion
- CDO structuring and tranche allocation methodologies
- CDO-squared structures and correlation trading
- CDS spread curves and hazard rate modeling
- Calendar spreads and roll strategies
- Capital Asset Pricing Model (CAPM)
- Capital Asset Pricing Model (CAPM) and beta estimation
- Central bank digital currencies (CBDCs)
- Central clearing and CCP risk management
- Commodity futures and convenience yields
- Commodity swaps and energy derivatives
- Complete markets and replication
- Constant maturity swaps and roll-over features
- Crack spreads in energy markets
- Credit risk assessment and loan pricing
- Cryptocurrency valuation and blockchain technology
- Currency swaps and cross-currency basis
- Dark pools and alternative trading venues
- DeFi protocols and decentralized finance
- Delta hedging and Greeks calculation
- Delta hedging strategies in options markets
- Deposit insurance and systemic risk
- Dividend discount model (DDM) applications
- Duration and convexity for bond price sensitivity
- ESG investing and sustainability metrics
- Enterprise value and equity value relationships
- Equity swaps and total return swaps
- European call options
- Exotic derivatives and path-dependent options
- Expected Shortfall (ES) and coherent risk measures
- Extreme value theory and tail risk modeling
- FX futures and currency hedging
- Fama-French three-factor and five-factor models
- Fintech disruption and digital banking
- GARCH models for volatility forecasting
- Gamma trading and convexity adjustments
- Green bonds and climate risk assessment
- HJM and forward rate model frameworks
- Historical simulation and parametric VaR approaches
- Hull-White and Black-Karasinski short rate models
- IPO pricing and underpricing analysis
- Implied volatility and volatility surface modeling
- Inflation-linked swaps and CPI adjustments
- Interest rate derivatives and forward rate agreements
- Interest rate models and term structure
- Interest rate swaps and swap spread decomposition
- Key rate duration and curve risk decomposition
- Liquidity coverage ratio and funding strategies
- Liquidity-adjusted VaR and liquidity horizons
- Margin requirements and collateral optimization
- Market impact and transaction cost analysis
- Mean reversion in interest rate processes
- Mergers and acquisitions due diligence
- Metal futures and industrial commodities
- Model backtesting and validation procedures
- Modern portfolio theory and efficient frontier
- Momentum and reversal investment strategies
- Mortgage-backed securities and prepayment modeling
- Multi-factor interest rate models
- Negative interest rates and floor/cap structures
- Net interest margin and banking profitability
- Netting agreements and close-out procedures
- Non-deliverable forwards and emerging market instruments
- OIS discounting and collateralized interest rate derivatives
- Option-adjusted spread (OAS) analysis
- Options on futures and forward-starting options
- Payment systems and settlement risk
- Portfolio optimization and mean-variance theory
- Prime brokerage and securities lending
- Private credit and direct lending
- Project finance and syndicated lending
- Real estate investment trusts (REITs)
- Recovery rate modeling and loss given default
- Repo markets and securities lending
- Risk factor decomposition and sensitivity analysis
- Risk parity and risk budgeting strategies
- Shadow banking and non-bank intermediation
- Smart beta and alternative indexing approaches
- Stochastic volatility in interest rate markets
- Stress testing and scenario analysis frameworks
- Swaptions and interest rate option pricing
- Swaptions and option volatility surfaces
- Synthetic CDOs and credit-linked note structures
- Terminal value modeling and exit multiples
- 'The Greeks: Delta, Gamma, Vega, Theta, and Rho sensitivity analysis'
- Too-big-to-fail policies and resolution regimes
- Treasury futures and bond basis
- Treasury securities and government bond markets
- VIX futures and volatility trading
- Value at Risk (VaR) and expected shortfall methodologies
- Value vs growth investing frameworks
- Vasicek and CIR interest rate models
- Volatility smile and skew patterns in option markets
- Weighted average cost of capital (WACC) calculations
- Working capital and cash conversion cycle
- Wrong-way risk and correlation adjustments
- aggregate consumption dynamics
- extended log-utility
- market price of risk
- negative exponential utility
- risk-free rate
- state-contingent dividends
- state-price deflator
- time-additive expected utility
- utility of individuals
enhanced: true
enhancement_date: '2025-11-06'
enhancement_id: batch04-971197
---




# 7.5 Exercises  

EXERCISE 7.1 Suppose $\eta_{1}$ and $\eta_{2}$ are strictly positive numbers and that $u_{1}(c)=u_{2}(c)=$ $c^{1-\gamma}/(1-\gamma)$ for any non-negative real number $c$ . Define the function $u_{\eta}:\mathbb{R}_{+}\to\mathbb{R}$ by  
$$
u_{\eta}(x)=\operatorname*{sup}\left\{\eta_{1}u_{1}(y_{1})+\eta_{2}u_{2}(y_{2}) | y_{1}+y_{2}\leq x;y_{1},y_{2}\geq0\right\}.
$$  

Show that $u_{\eta}(x)=k x^{1-\gamma}/(1-\gamma)$ for some constant $k$ . What is the implication for the utility of representative individuals?  

EXERCISE 7.2 Show Theorem 7.7 for the case of extended log-utility and the case of negative exponential utility.  

EXERCISE 7.3 Suppose that aggregate time 1 consumption can only take on the values. $1,2,\ldots,K$ for some finite integer $K$ . Assume that European call options on aggregate consumption are traded for any exercise price $0,1,2,\ldots,K$ . Consider a portfolio with one unit of the option with exercise price $k-1$ , one unit of the option with exercise price $k+1$ , and minus two units of the option with exercise price $k$ . What is the payoff of this portfolio? Discuss the consequences of your findings for the (effective) completeness of the market. Could you do just as well with put options?  

EXERCISE 7.4 Assume a discrete-time economy with $L$ agents. Each agent $l$ maximizes timeadditive expected utility $\mathrm{E}\left[\sum_{t=0}^{T}\beta_{l}^{t}u_{l}(c_{l t})\right]$ where $u_{l}$ is strictly increasing and concave. Show that  
$$
\frac{\zeta_{t+1}}{\zeta_{t}}=\frac{\sum_{l=1}^{L}\beta_{l}u_{l}^{\prime}(c_{l,t+1})}{\sum_{l=1}^{L}u_{l}^{\prime}(c_{l t})}
$$  

is a valid one-period state-price deflator, i.e. that it is strictly positive and satisfies $\mathrm{E}_{t}[(\zeta_{t+1}/\zeta_{t})R_{t+1}]=$ 1 for any gross return $R_{t+1}$ over the period $[t,t+1]$  

EXERCISE 7.5  George and John live in a continuous-time economy in which the relevant uncertainty is generated by a one-dimensional standard Brownian motion. $z=(z_{t})_{t\in[0,T]}$ .Both have time-additive utility of their consumption process: George maximizes.  
$$
U_{G}(c)=\mathrm{E}\left[\int_{0}^{T}e^{-0.02t}\ln c_{t}d t\right],
$$  

while John maximizes  
$$
U_{J}(c)=\operatorname{E}\left[\int_{0}^{T}e^{-0.02t}\left(-{\frac{1}{c_{t}}}\right)d t\right].
$$  

George's optimal consumption process $c_{G}=\left(c_{G t}\right)$ has a constant expected growth rate of 4% and a constant volatility of $5\%$ , i.e.  
$$
d c_{G t}=c_{G t}\left[0.04d t+0.05d z_{t}\right].
$$  

Two assets are traded in the economy. One asset is an instantaneously risk-free bank account with continuously compounded rate of return $r_{t}$ .The other asset is a risky asset with price process $P=\left(P_{t}\right)$ satisfying  
$$
d P_{t}=P_{t}\left[\mu_{P t}d t+0.4d z_{t}\right]
$$  

for some drift. $\mu_{P t}$ . The market is complete.  

(a) What are the relative risk aversions of George and John, respectively?   
(b) Using the fact that a state price deflator can be derived from George's consumption process, determine the risk-free rate $r_{t}$ and the market price of risk $\lambda_{t}$ . What can you conclude about the price processes of the two assets?  

(c) Find the drift and volatility of John's optimal consumption process, $c_{J}=\left(c_{J t}\right)$  

(d) Suppose George and John are the only two individuals in the economy. What can you say about the dynamics of aggregate consumption? Can the representative agent have constant relative risk aversion?  

EXERCISE 7.6 Consider a discrete-time economy with $L$ individuals with identical preferences so that agent $l=1,\ldots,L$ at time 0 wants to maximize  
$$
\operatorname{E}\left[\sum_{t=0}^{T}\beta^{t}{\frac{1}{1-\gamma}}c_{l,t}^{1-\gamma}\right]
$$  

where $c_{l,t}$ denotes the consumption rate of individual $l$ at time $t$ . Let $c_{l,t}^{*}$ be the optimal consumption rate of individual. $l$ at time $t$  

(a) Argue why  
$$
\frac{\zeta_{t+1}}{\zeta_{t}}=\frac{\beta}{L}\sum_{l=1}^{L}\left(\frac{c_{l,t+1}^{*}}{c_{l,t}^{*}}\right)^{-\gamma}
$$  

is a state-price deflator between time $t$ and time $t+1$  

(b) If the market is complete, explain why the next-period state-price deflator in $(^{*})$ can be written as  
$$
\frac{\zeta_{t+1}}{\zeta_{t}}=\beta\left(\frac{\sum_{l=1}^{L}c_{l,t+1}^{\ast}}{\sum_{l=1}^{L}c_{l,t}^{\ast}}\right)^{-\gamma}.
$$  

EXERCISE 7.7 (Use spreadsheet or similar computational tool.) Consider a one-period economy with 5 possible states and 5 assets traded. The state-contingent dividends and prices of the assets and the state probabilities are as follows:.  

<html><body><table><tr><td></td><td>state 1</td><td>state 2</td><td>state 3</td><td>state 4</td><td>state 5</td><td>price</td></tr><tr><td>Asset 1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>0.9</td></tr><tr><td>Asset 2</td><td>0</td><td>2</td><td>4</td><td>6</td><td>8</td><td>1.7</td></tr><tr><td>Asset 3</td><td>4</td><td>0</td><td>2</td><td>4</td><td>2</td><td>2.3</td></tr><tr><td>Asset 4</td><td>10</td><td>0</td><td>0</td><td>2</td><td>2</td><td>4.3</td></tr><tr><td>Asset 5</td><td>4</td><td>4</td><td>0</td><td>4</td><td>4</td><td>2.8</td></tr><tr><td>probability</td><td>0.25</td><td>0.25</td><td>0.2</td><td>0.2</td><td>0.1</td><td></td></tr></table></body></html>  

(a) Verify that the market is complete and find the unique state-price deflator.  

Consider an individual investor, Alex, with access to the above financial market with the given prices. Suppose Alex has time-additive expected utility with a time preference rate of $\delta=0.03$ and a constant relative risk aversion of. $\gamma=2$ . Suppose his optimal consumption at time. $0$ is 5 and that he will receive an income of 5 at time 1 no matter which state is realized..  

(b) What is Alex' optimal time 1 consumption? What does it cost him to finance that consumption? What is the optimal portfolio for Alex?  

Suppose now that there is only one other individual, Bob, in the economy. Bob also has timeadditive expected utility with a time preference rate of 0.03 but a relative risk aversion of 5. Bob's. optimal time 0 consumption is also 5..  

(c) What is Bob's optimal time 1 consumption?   
(d) What is the aggregate time 0 consumption and the state-dependent aggregate time 1 consumption?   
(e) What is Bob's time 0 endowment and state-dependent time 1 endowment? What is Bob's optimal portfolio?   
(f) Verify that the markets clear.  

EXERCISE 7.8  Bruce lives in a continuous-time complete market economy. He has timeadditive logarithmic utility, $u_{B}(c)=\ln{c}$ , with a time preference rate of $\delta_{B}=0.02$ , and his optimal consumption process $c_{B}=\left(c_{B t}\right)$ has dynamics  
$$
d c_{B t}=c_{B t}\left[0.03d t+0.1d z_{t}\right],
$$  

where $z=\left(z_{t}\right)$ is a standard Brownian motion.  

(a) Characterize the state-price deflator induced by Bruce's optimal consumption process? Identify the continuously compounded short-term risk-free interest rate and the instantaneous. Sharpe ratio of any risky asset.  

Patti lives in the same economy as Bruce. She has time-additive expected utility with a HARA utility function $\begin{array}{r}{u_{P}(c)=\frac{1}{1-\gamma}(c-\bar{c})^{1-\gamma}}\end{array}$ and a time preference rate identical to Bruce's, i.e. $\delta_{P}=0.02$  

(b) Explain why Patti's optimal consumption strategy $c_{P}=\left(c_{P t}\right)$ must satisfy  
$$
c_{P t}=\bar{c}+\left(\frac{c_{B t}}{c_{B0}}\right)^{1/\gamma}\left(c_{P0}-\bar{c}\right).
$$  

Find the dynamics of Patti's optimal consumption process.

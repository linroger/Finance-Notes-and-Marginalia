---
tags:
- artificial-intelligence
- asset_pricing
- consumption
- continuous_time
- defi
- expected_utility
- fixed-income
- interest-rate-swap
- irs
- ma
- market_completeness
- mpt
- option-greeks
- risk-management
- state_price
- value-at-risk
- var
aliases:
- Continuous Time Framework
- Continuous-time Model
key_concepts:
- Agricultural futures and seasonality
- Alternative investments and hedge fund strategies
- Asset swaps and spread-lock strategies
- Barrier options and knock-in/knock-out structures
- Basis swaps and cross-currency basis adjustments
- Basis swaps and floating rate correlations
- Behavioral finance and market anomalies
- Best execution and regulatory requirements
- Bid-ask spreads and market making profitability
- Black-Litterman model and portfolio optimization
- CDO structuring and tranche allocation methodologies
- CDO-squared structures and correlation trading
- Calendar spreads and roll strategies
- Capital Asset Pricing Model (CAPM) and beta estimation
- Central clearing and CCP risk management
- Commodity futures and convenience yields
- Commodity swaps and energy derivatives
- Continuous-time setting
- Crack spreads in energy markets
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
- Interest rate swaps and swap spread decomposition
- Key rate duration and curve risk decomposition
- Liquidity-adjusted VaR and liquidity horizons
- Margin requirements and collateral optimization
- Market completeness
- Market impact and transaction cost analysis
- Mean reversion in interest rate processes
- Mergers and acquisitions due diligence
- Metal futures and industrial commodities
- Model backtesting and validation procedures
- Momentum and reversal investment strategies
- Mortgage-backed securities and prepayment modeling
- Multi-factor interest rate models
- Negative interest rates and floor/cap structures
- Netting agreements and close-out procedures
- Non-deliverable forwards and emerging market instruments
- OIS discounting and collateralized interest rate derivatives
- Optimal consumption process
- Options on futures and forward-starting options
- Payment systems and settlement risk
- Prime brokerage and securities lending
- Private credit and direct lending
- Project finance and syndicated lending
- Real estate investment trusts (REITs)
- Recovery rate modeling and loss given default
- Repo markets and securities lending
- Risk parity and risk budgeting strategies
- Shadow banking and non-bank intermediation
- Smart beta and alternative indexing approaches
- State-price deflator
- Stochastic volatility in interest rate markets
- Stress testing and scenario analysis frameworks
- Swaptions and interest rate option pricing
- Swaptions and option volatility surfaces
- Synthetic CDOs and credit-linked note structures
- Terminal value modeling and exit multiples
- 'The Greeks: Delta, Gamma, Vega, Theta, and Rho sensitivity analysis'
- Time-additive utility
- Too-big-to-fail policies and resolution regimes
- Treasury futures and bond basis
- Treasury securities and government bond markets
- VIX futures and volatility trading
- Value at Risk (VaR) and expected shortfall methodologies
- Value at Risk (VaR) and risk metrics
- Value vs growth investing frameworks
- Vasicek and CIR interest rate models
- Volatility smile and skew patterns in option markets
- Weighted average cost of capital (WACC) calculations
- Working capital and cash conversion cycle
- Wrong-way risk and correlation adjustments
- Yield curve construction and term structure modeling
enhanced: true
enhancement_date: '2025-11-06'
enhancement_id: batch04-733064
---




# 6.4 The continuous-time framework  

In a continuous-time setting an individual consumes according to a non-negative continuous-time process $c=\left(c_{t}\right)$ . Suppose that her preferences are described by time-additive expected utility so that the objective is to maximize $\begin{array}{r}{\operatorname{E}[\int_{0}^{T}e^{-\delta t}u(c_{t})d t]}\end{array}$  

We will again go through a variational argument giving a link between the optimal consumption process and asset prices. For simplicity assume that assets pay no intermediate dividends. Suppose $c=\left(c_{t}\right)$ is the optimal consumption process for some agent and consider the following deviation from this strategy: at time 0 increase the investment in asset $i$ by $\varepsilon$ units. The extra costs of $\varepsilon P_{i0}$ implies a reduced consumption now. Let us suppose that the individual finances this extra investment by cutting down the consumption rate in the time interval $[0,\Delta t]$ for some small positive $\Delta t$ by $\varepsilon P_{i0}/\Delta t$ . The extra $\varepsilon$ units of asset $i$ is resold at time $t<T$ , yielding a revenue of $\varepsilon P_{i t}$ . This finances an increase in the consumption rate over $[t,t+\Delta t]$ by $\varepsilon P_{i t}/\Delta t$ . The consumption rates outside the intervals $[0,\Delta t]$ and $[t,t+\Delta t]$ will be unaffected. Given the optimality of $c=\left(c_{t}\right)$ , we must have that  
$$
\operatorname{E}\left[\int_{0}^{\Delta t}e^{-\delta s}\left(u\left(c_{s}-{\frac{\varepsilon P_{i0}}{\Delta t}}\right)-u(c_{s})\right)d s+\int_{t}^{t+\Delta t}e^{-\delta s}\left(u\left(c_{s}+{\frac{\varepsilon P_{i t}}{\Delta t}}\right)-u(c_{s})\right)d s\right]\leq0.
$$  

Dividing by $\varepsilon$ and letting $\varepsilon\rightarrow0$ , we obtain  
$$
\operatorname{E}\left[-\frac{P_{i0}}{\Delta t}\int_{0}^{\Delta t}e^{-\delta s}u^{\prime}(c_{s})d s+\frac{P_{i t}}{\Delta t}\int_{t}^{t+\Delta t}e^{-\delta s}u^{\prime}(c_{s})d s\right]\leq0.
$$  

Letting $\Delta t\to0$ , we arrive at  
$$
\mathrm{E}\left[-P_{i0}u^{\prime}(c_{0})+P_{i t}e^{-\delta t}u^{\prime}(c_{t})\right]\leq0,
$$  

or, equivalently,  
$$
P_{i0}u^{\prime}(c_{0})\geq\mathrm{E}\left[e^{-\delta t}P_{i t}u^{\prime}(c_{t})\right].
$$  

The reverse inequality can be shown similarly so that we have that $P_{i0}u^{\prime}(c_{0})=\mathrm{E}[e^{-\partial t}P_{t}u^{\prime}(c_{t})]$ or more generally  
$$
P_{i t}=\mathrm{E}_{t}\left[e^{-\delta(t^{\prime}-t)}\frac{u^{\prime}(c_{t^{\prime}})}{u^{\prime}(c_{t})}P_{i t^{\prime}}\right],\quad t\leq t^{\prime}\leq T.
$$  

With intermediate dividends this relation is slightly more complicated:  
$$
P_{i t}=\mathrm{E}_{t}\left[\int_{t}^{t^{\prime}}\delta_{i s}P_{i s}e^{-\delta(s-t)}\frac{u^{\prime}(c_{s})}{u^{\prime}(c_{t})}d s+e^{-\delta(t^{\prime}-t)}\frac{u^{\prime}(c_{t^{\prime}})}{u^{\prime}(c_{t})}P_{i t^{\prime}}\right].
$$  

We see that  
$$
\zeta_{t}=e^{-\delta t}\frac{u^{\prime}(c_{t})}{u^{\prime}(c_{0})}
$$  

defines a state-price deflator, exactly as in the discrete-time case.  

If the market is complete, we can easily reach (6.44) solving step one of the two-step procedure suggested in Section 6.2.4. The problem is  
$$
\operatorname*{max}_{c=(c_{t})}\operatorname{E}\left[\int_{0}^{T}e^{-\delta t}u(c_{t})d t\right]\qquad\mathrm{s.t.}\mathrm{E}\left[\int_{0}^{T}\zeta_{t}c_{t}d t\right]\leq e_{0}+\mathrm{E}\left[\int_{0}^{T}\zeta_{t}e_{t}d t\right],
$$  

where $\zeta=\left(\zeta_{t}\right)$ is the unique state-price deflator. The left-hand side of the constraint is the present value of the consumption process, the right-hand side is the sum of the initial wealth $e_{0}$ and the present value of the income process. The Lagrangian for this problem is  
$$
\begin{array}{r l}&{\mathcal{L}=\mathrm{E}\left[\displaystyle\int_{0}^{T}e^{-\delta t}u(c_{t})d t\right]+\alpha\left(e_{0}+\mathrm{E}\left[\displaystyle\int_{0}^{T}\zeta_{t}e_{t}d t\right]-\mathrm{E}\left[\displaystyle\int_{0}^{T}\zeta_{t}c_{t}\right]\right)}\ &{\quad=\alpha\left(e_{0}+\mathrm{E}\left[\displaystyle\int_{0}^{T}\zeta_{t}e_{t}d t\right]\right)+\mathrm{E}\left[\displaystyle\int_{0}^{T}\left(e^{-\delta t}u(c_{t})-\alpha\zeta_{t}c_{t}\right)d t\right].}\end{array}
$$  

If we for each $t$ and each state maximize the integrand in the last integral above, we will surely maximize the Lagrangian. The first-order condition is $e^{-\delta t}u^{\prime}(c_{t})=\alpha\zeta_{t}$ and since $\zeta_{0}=1$ , we must have (6.44).  

Exercise 6.10 considers an individual with habit formation in a continuous-time setting.

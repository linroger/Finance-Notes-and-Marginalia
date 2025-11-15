---
aliases:
- Appendix 5.C
- Forward vs. Futures
- Stochastic Interest Rates
cssclasses:
- academia
enhanced: true
enhancement_date: '2025-11-06'
enhancement_id: batch03-a4c7c5
key_concepts:
- Apt
- Carry trades and momentum in FX markets
- coupon-bearing bond analysis
- Extensions to multi-factor CAPM models
- Sensitivity analysis in DCF models
- Duration and convexity analysis for bond portfolio management
- Active portfolio management and performance attribution
- Option Greeks and portfolio risk management
- Common pitfalls in DCF valuation
- Capital Asset Pricing Model and beta estimation
- Risk budgeting and portfolio construction techniques
- Discounted Cash Flow valuation methodology
- Solution
- Capital Asset Pricing Model and expected returns
- Replicating fully funded contracts
- Vega and volatility risk management
- Portfolio immunization strategies
- forward commitments and hedging
- Mathematical Finance
- Money-market account
- Key rate duration and curve risk
- Course Material
- Security Market Line and beta measurement
- Currency risk management and hedging
- Forward rates and interest rate parity
- Theta and time decay modeling
- Exchange rate determination and PPP theory
- Forward price formula
- ESG integration in portfolio management
- present value and discounting methods
- zero-coupon bond pricing and yields
- Continuous time formula
- Delta hedging strategies in options portfolio management
- Futures price derivation
- Free cash flow to equity and firm valuation
- Terminal value estimation and perpetuity growth
- Quantitative Implementation
- Gamma and convexity adjustments
- Credit risk modeling and portfolio correlation analysis
- Credit risk assessment and loan portfolio management
- Delta hedging and the replication argument
- Exotic Options
- Duration and convexity measures for bond portfolios
- Currency hedging strategies for global portfolios
- Price sensitivity to interest rate changes
- Modified duration vs. Macaulay duration
- Market portfolio and risk-free rate assumptions
- Currency markets and foreign exchange trading
tags:
- financial-analysis
- stochastic-calculus
- mathematical-finance
- course-material
- capm
- financial-modeling
- apt
- greeks
- money-market-account
- exchange-rates
- credit-risk
- quantitative-implementation
- duration-convexity
- solution
- exotic-options
- forward-prices
- quantitative-finance
- futures-prices
- dcf-valuation
- interest-rates
title: Appendix 5.C Forward And Futures Prices When Interest Rates Are Random
---

# Appendix 5.C Forward And Futures Prices When Interest Rates Are Random

This appendix formalizes the difference between forward and futures prices and shows the relationship between them when interest rates are stochastic. We will use the following notation:

$$\begin{aligned}
&F_{t,T} = \text{Forward price} \\
&f_{t,T} = \text{Futures price} \\
&S_t = \text{Time } t \text{ price of the underlying asset} \\
&P_{t,T} = \text{Time } t \text{ price of a zero-coupon bond maturing at time } T \\
&R_t = \text{Time } t \text{ interest rate from time } t \text{ to time } t+h \\
&h = \text{Length of a period}; h=T/n 
\end{aligned}$$

We will refer to an instrument that pays the short-term interest rate as a money-market account.

The strategy in these derivations, which follow Cox et al. (1981), is to find a strategy that replicates fully funded contracts.

### Forward Prices

The forward price is:

$$F_{t,T}=\text{PV}\left(\frac{S_T}{P_{t,T}}\right)=\frac{S_t}{P_{t,T}}$$

In the chapter, we wrote this formula as $F_{t,T}=S_t e^{r(T-t)}$. This is the same as equation (5.23), where $r$ is the continuously compounded yield on the bond: $r=\ln(1/P_{t,T})/(T-t)$.

To prove equation (5.23), buy $F_{t,T}$ bonds paying $\$1$ at maturity (this pre-funds the forward price) and go long $1/P_{t,T}$ forward contracts. The payoff is:

$$\frac{F_{t,T}}{P_{t,T}}+\frac{1}{P_{t,T}}\left[F_{T,T}-F_{t,T}\right]=\frac{F_{t,T}}{P_{t,T}}=\frac{S_T}{P_{t,T}}$$

This demonstrates that a portfolio costing the forward price at time $t$ pays $S_T/P_{t,T}$. Thus the forward price is the present value of $S_T/P_{t,T}$, or $S_t/P_{t,T}$.

## Futures Price

We will show that the futures price is:

$$f_{t,T}=\text{PV}\left[S_T\prod_{i=t}^T(1+R_i)\right]$$

Note that if the interest rate is known, $\prod_{i=t}^{T}(1+R_i)=1/P_{t,T}$ (the bond can be replicated with the money-market fund), and the forward price equals the futures price. To prove equation (5.24), invest the amount $f_{t,T}$ at the short-term interest rate, reinvesting the proceeds each period. Also, at each time $t_i \equiv t+ih, i=1, \ldots, n$, invest in $\prod_{j=t}^{t_i}(1+R_j)$ futures contracts. At time $t_{i+1}$, liquidate position and invest the proceeds in the money-market account. The net cash flow at time $T$ will be:

$$\begin{gathered}
f_{t,T}\prod_{i=t}^{T}(1+R_i) +\sum_{i=t}^{T-h}\left(\prod_{j=t}^{i}(1+R_j)(f_{j,T}-f_{j-h,T})\prod_{j=i+h}^{T-h}(1+R_j)\right) \\
=f_{T,T}\prod_{i=t}^{T-h}(1+R_i)=S_T\prod_{i=t}^{T-h}(1+R_i) 
\end{gathered}$$

For future reference, note that in continuous time, equation (5.24) becomes:

$$f_{t,T}=\text{PV}\left[S_T e^{\int_t^T r(s)ds}\right]$$

where $r(s)$ is the instantaneous continuously compounded short-term interest rate.

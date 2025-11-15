---
tags:
- abs
- aggregate_consumption
- apt
- artificial-intelligence
- bond-pricing
- consumption_dynamics
- defi
- derivatives-pricing
- fixed-income
- fixed-income-derivatives
- interest-rate-derivatives
- interest-rate-swap
- irs
- ma
- markets
- mpt
- option-greeks
- real_interest_rates
- risk-management
- stochastic
- time_preference
- value-at-risk
- var
- yield-curve
- yield_curve
aliases:
- Consumption and Interest Rates
- Real Rates and Consumption
key_concepts:
- Agricultural futures and seasonality
- Alternative investments and hedge fund strategies
- Arbitrage pricing theory (APT)
- Asset swaps and spread-lock strategies
- Barrier options and knock-in/knock-out structures
- Basis swaps and cross-currency basis adjustments
- Basis swaps and floating rate correlations
- Behavioral finance and market anomalies
- Best execution and regulatory requirements
- Bid-ask spreads and market making profitability
- Black-Litterman model and portfolio optimization
- Bond portfolio immunization strategies
- Brownian motion and Wiener processes
- CDO structuring and tranche allocation methodologies
- CDO-squared structures and correlation trading
- Calendar spreads and roll strategies
- Central clearing and CCP risk management
- Commodity futures and convenience yields
- Commodity swaps and energy derivatives
- Complete markets and replication
- Constant maturity swaps and roll-over features
- Corporate bond pricing and credit spread decomposition
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
- Equilibrium interest rate
- Equity swaps and total return swaps
- Exotic derivatives and path-dependent options
- Expected Shortfall (ES) and coherent risk measures
- FX futures and currency hedging
- Fama-French three-factor and five-factor models
- Fintech disruption and digital banking
- GARCH models for volatility forecasting
- Gamma trading and convexity adjustments
- Green bonds and climate risk assessment
- HJM and forward rate model frameworks
- High frequency trading and algorithmic strategies
- Historical simulation and parametric VaR approaches
- Hull-White and Black-Karasinski short rate models
- IPO pricing and underpricing analysis
- Implied volatility and volatility surface modeling
- Inflation-linked swaps and CPI adjustments
- Interest rate derivatives and forward rate agreements
- Interest rate models and term structure
- Interest rate swaps and swap spread decomposition
- Interest rates and consumption
- Key rate duration and curve risk decomposition
- Liquidity-adjusted VaR and liquidity horizons
- Margin requirements and collateral optimization
- Market impact and transaction cost analysis
- Mean reversion in interest rate processes
- Mergers and acquisitions due diligence
- Metal futures and industrial commodities
- Model backtesting and validation procedures
- Momentum and reversal investment strategies
- Mortgage-backed securities and prepayment modeling
- Multi-factor interest rate models
- Negative interest rates and floor/cap structures
- Net interest margin and banking profitability
- Netting agreements and close-out procedures
- Non-deliverable forwards and emerging market instruments
- OIS discounting and collateralized interest rate derivatives
- Option Greeks and sensitivity analysis
- Options on futures and forward-starting options
- Payment systems and settlement risk
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
- Spot rates, forward rates, and discount factor curves
- State-price deflator
- Stochastic process
- Stochastic volatility in interest rate markets
- Stress testing and scenario analysis frameworks
- Swaptions and interest rate option pricing
- Swaptions and option volatility surfaces
- Synthetic CDOs and credit-linked note structures
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
- Working capital and cash conversion cycle
- Wrong-way risk and correlation adjustments
- Yield curve construction and term structure modeling
- Zero-coupon bond pricing and bootstrapping
enhanced: true
enhancement_date: '2025-11-06'
enhancement_id: batch04-707327
---




# 10.3 Real interest rates and aggregate consumption  

In order to study the link between interest rates and aggregate consumption, we assume the existence of a representative individual maximizing the expected time-additive utility F $[\int_{0}^{T}e^{-\delta t}u(c_{t})d t]$ As discussed in Chapter 7, a representative individual will exist in a complete market. The parameter $\delta$ is the subjective time preference rate with higher $\delta$ representing a more impatient individual. $c_{t}$ is the consumption rate of the individual, which is then also the aggregate consumption level in the economy. In terms of the utility and time preference of the representative individual the state-price deflator is therefore characterized by  
$$
\zeta_{t}=e^{-\delta t}\frac{u^{\prime}(c_{t})}{u^{\prime}(c_{0})}.
$$  

Let us take a continuous-time framework and assume that $c=\left(c_{t}\right)$ follows a stochastic process%20Process.md) of the form  
$$
d c_{t}=c_{t}\left[\mu_{c t}\:d t+\pmb{\sigma}_{c t}^{\top}\:d z_{t}\right],
$$  

where $z=\left(z_{t}\right)$ is a (possibly multi-dimensional) standard Brownian motion. Then Theorem 8.1 states that the equilibrium continuously compounded short-term interest rate is given by  
$$
r_{t}=\delta+\gamma(c_{t})\mu_{c t}-\frac{1}{2}\eta(c_{t})\ | \pmb{\sigma}_{c t}\ | ^{2},
$$  

and that  
$$
\lambda_{t}=\gamma(c_{t})\sigma_{c t}
$$  

defines a market price of risk process. Here $\gamma(c_{t})\equiv-c_{t}u^{\prime\prime}(c_{t})/u^{\prime}(c_{t})$ is the relative risk aversion and $\eta(c_{t})\equiv c_{t}^{2}u^{\prime\prime\prime}(c_{t})/u^{\prime}(c_{t})$ , which is positive under the very plausible assumption of decreasing absolute risk aversion. For notational simplicity we leave out the $f$ superscript on the short-term interest rate in this chapter. The short rate in (10.14) was already interpreted in Section 8.3.  

In the special case of constant relative risk aversion, $u(c)=c^{1-\gamma}/(1-\gamma)$ , Equation (10.14) simplifies to  
$$
r_{t}=\delta+\gamma\mu_{c t}-\frac{1}{2}\gamma(1+\gamma)\ | \pmb{\sigma}_{c t}\ | ^{2}.
$$  

In particular, we see that if the drift and variance rates of aggregate consumption are constant, i.e. aggregate consumption follows a geometric Brownian motion, then the short-term interest rate will be constant over time. In that case the time $t$ price of the zero-coupon bond maturing at time $s$ iS  
$$
B_{t}^{s}=\operatorname{E}_{t}\left[{\frac{\zeta_{s}}{\zeta_{t}}}\right]=\operatorname{E}_{t}\left[\exp\left\{-r(s-t)-{\frac{1}{2}}\ | \lambda\ | ^{2}(s-t)-\lambda^{\top}(z_{s}-z_{t})\right\}\right]=e^{-r(s-t)}
$$  

and the corresponding continuous compounded yield is $y_{t}^{s}=r$ . Consequently, the yield curve will be flat and constant over time. This is clearly an unrealistic case. To obtain interesting models we must either allow for variations in the expectation and the variance of aggregate consumption growth or allow for non-constant relative risk aversion (or both).  

What can we say about the relation between the equilibrium yield curve and the expectations and uncertainty about future aggregate consumption? Given the consumption dynamics in (10.13), we have  
$$
\frac{c_{T}}{c_{t}}=\exp\left\{\int_{t}^{T}\left(\mu_{c s}-\frac{1}{2}\ | \pmb{\sigma}_{c s}\ | ^{2}\right)d s+\int_{t}^{T}\pmb{\sigma}_{c s}^{\top}d z_{s}\right\}.
$$  

Assuming that the consumption sensitivity $\sigma_{c s}$ is constant and that the drift rate is so that $\begin{array}{r}{\int_{t}^{T}\mu_{c s}d s}\end{array}$ is normally distributed, we see that $c_{T}/c_{t}$ is lognormally distributed. Assuming timeadditive power utility, the state-price deflator $\zeta_{T}/\zeta_{t}=e^{-\delta(T-t)}(c_{T}/c_{t})^{-\gamma}$ will then also be lognormally distributed. Consequently, the price of the zero-coupon bond maturing at time $T$ is given by  
$$
\begin{array}{r l}&{\boldsymbol{B}_{t}^{T}=\mathrm{E}_{t}\left[\frac{\zeta_{T}}{\zeta_{t}}\right]=e^{-\delta(T-t)}\mathrm{E}_{t}\left[e^{-\gamma\ln(c_{T}/c_{t})}\right]}\ &{\qquad=\exp\left\{-\delta(T-t)-\gamma\mathrm{E}_{t}\left[\ln\left(\frac{c_{T}}{c_{t}}\right)\right]+\frac{1}{2}\gamma^{2}\mathrm{Var}_{t}\left[\ln\left(\frac{c_{T}}{c_{t}}\right)\right]\right\},}\end{array}
$$  

where we have applied Theorem B.2 in Appendix B. Combining the above expression with (10.7). the continuously compounded zero-coupon rate or yield. $y_{t}^{T}$ for maturity $T$ is  
$$
y_{t}^{T}=\delta+\gamma\frac{\mathrm{E}_{t}[\ln(c_{T}/c_{t})]}{T-t}-\frac{1}{2}\gamma^{2}\frac{\mathrm{Var}_{t}[\ln(c_{T}/c_{t})]}{T-t}.
$$  

Since  
$$
\ln\mathrm{E}_{t}\left[\frac{c_{T}}{c_{t}}\right]=\mathrm{E}_{t}\left[\ln\left(\frac{c_{T}}{c_{t}}\right)\right]+\frac{1}{2}\mathrm{Var}_{T}\left[\ln\left(\frac{c_{T}}{c_{t}}\right)\right],
$$  

the zero-coupon rate can be rewritten as  
$$
y_{t}^{T}=\delta+\gamma\frac{\ln\mathrm{E}_{t}[c_{T}/c_{t}]}{T-t}-\frac{1}{2}\gamma(1+\gamma)\frac{\mathrm{Var}_{t}[\ln(c_{T}/c_{t})]}{T-t},
$$  

which is very similar to the short-rate equation (10.16). The yield is increasing in the subjective rate of time preference. The equilibrium yield for the period $[t,T]$ is positively related to the expected growth rate of aggregate consumption over the period and negatively related to the uncertainty about the growth rate of consumption over the period. The intuition for these results is the same as for short-term interest rate discussed above. We see that the shape of the equilibrium time. $t$ yield curve $T\mapsto y_{t}^{T}$ is determined by how expectations and variances of consumption growth rates. depend on the length of the forecast period. For example, if the economy is expected to enter a short period of high growth rates, real short-term interest rates tend to be high and the yield curve downward-sloping.  

Equation (10.18) is based on a lognormal future consumption and power utility. We will discuss such a setting in more detail in Section 10.5.1. It appears impossible to obtain an exact relation of the same structure as (10.18) for a more general model, where future consumption is not necessarily lognormal and preferences are different from power utility. However, following Breeden (1986), we can derive an approximate relation of a similar form. The equilibrium time $t$ price of a zero-coupon bond paying one consumption unit at time $T\geq t$ is given by  
$$
B_{t}^{T}=\mathrm{E}_{t}\left[\frac{\zeta_{T}}{\zeta_{t}}\right]=e^{-\delta(T-t)}\frac{\mathrm{E}_{t}\left[u^{\prime}(c_{T})\right]}{u^{\prime}(c_{t})},
$$  

where $c_{T}$ is the uncertain future aggregate consumption level. We can write the left-hand side of the equation above in terms of the yield $y_{t}^{T}$ of the bond as  
$$
B_{t}^{T}=e^{-y_{t}^{T}(T-t)}\approx1-y_{t}^{T}(T-t);
$$  

using a first order Taylor expansion. Turning to the right-hand side of the equation, we will use a second-order Taylor expansion of $u^{\prime}(c_{T})$ around $c_{t}$  
$$
u^{\prime}(c_{T})\approx u^{\prime}(c_{t})+u^{\prime\prime}(c_{t})(c_{T}-c_{t})+{\frac{1}{2}}u^{\prime\prime\prime}(c_{t})(c_{T}-c_{t})^{2}.
$$  

This approximation is reasonable when. $c_{T}$ stays relatively close to $c_{t}$ , which is the case for fairly low and smooth consumption growth and fairly short time horizons. Applying the approximation, the right-hand side of (10.19) becomes  
$$
\begin{array}{r l r}{\lefteqn{e^{-\delta(T-t)}\frac{\mathrm{E}_{t}\left[u^{\prime}(c_{T})\right]}{u^{\prime}(c_{t})}\approx e^{-\delta(T-t)}\left(1+\frac{u^{\prime\prime}(c_{t})}{u^{\prime}(c_{t})}\mathrm{E}_{t}[c_{T}-c_{t}]+\frac{1}{2}\frac{u^{\prime\prime\prime}(c_{t})}{u^{\prime}(c_{t})}\mathrm{E}_{t}\left[(c_{T}-c_{t})^{2}\right]\right)}}\ &{}&{\approx1-\delta(T-t)+e^{-\delta(T-t)}\frac{c_{t}u^{\prime\prime}(c_{t})}{u^{\prime}(c_{t})}\mathrm{E}_{t}\left[\frac{c_{T}}{c_{t}}-1\right]}\ &{}&{+\frac{1}{2}e^{-\delta(T-t)}c_{t}^{2}\frac{u^{\prime\prime\prime}(c_{t})}{u^{\prime}(c_{t})}\mathrm{E}_{t}\left[\left(\frac{c_{T}}{c_{t}}-1\right)^{2}\right],}\end{array}
$$  

where we have used the approximation $e^{-\delta(T-t)}\approx1-\delta(T-t)$ . Substituting the approximations of both sides into (10.19) and rearranging, we find the following approximate expression for the zero-coupon yield:  
$$
y_{t}^{T}\approx\delta+e^{-\delta(T-t)}\left(\frac{-c_{t}u^{\prime\prime}(c_{t})}{u^{\prime}(c_{t})}\right)\frac{\operatorname{E}_{t}\left[c_{T}/c_{t}-1\right]}{T-t}-\frac{1}{2}e^{-\delta(T-t)}c_{t}^{2}\frac{u^{\prime\prime\prime}(c_{t})}{u^{\prime}(c_{t})}\frac{\operatorname{E}_{t}\left[\left(\frac{c_{T}}{c_{t}}-1\right)^{2}\right]}{T-t}.
$$  

We can replace $\mathrm{E}_{t}\left[\left(c_{T}/c_{t}-1\right)^{2}\right]$ by $\mathrm{Var}_{t}\left[c_{T}/c_{t}\right]+\left(\mathrm{E}_{t}\left[c_{T}/c_{t}-1\right]\right)^{2}$ and consider the effect of a shift in variance for a fixed expected consumption growth. Again assuming $u^{\prime}>0$ $u^{\prime\prime}<0$ , and $u^{\prime\prime\prime}>0$ , we see that the yield of a given maturity is positively related to the expected growth rate of consumption up to the maturity date and negatively related to the variance of the consumption growth rate up to maturity.

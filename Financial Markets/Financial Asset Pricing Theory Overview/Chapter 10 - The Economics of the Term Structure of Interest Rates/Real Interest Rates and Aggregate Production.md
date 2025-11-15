---
tags:
- aggregate_production
- artificial-intelligence
- brownian_motion
- clearing
- defi
- equity-derivatives
- general_equilibrium
- hedging-strategies
- hjb-equation
- interest-rate-derivatives
- interest-rate-swap
- investment
- irs
- ma
- markets
- mpt
- option-greeks
- options
- options-pricing
- real_interest_rates
- risk-management
- stochastic
- value-at-risk
- var
aliases:
- CIR model
- Interest Rates and Production
key_concepts:
- Aggregate production
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
- Brownian motion
- Brownian motion and Wiener processes
- CDO structuring and tranche allocation methodologies
- CDO-squared structures and correlation trading
- Calendar spreads and roll strategies
- Capital Asset Pricing Model (CAPM) and beta estimation
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
- Exotic derivatives and path-dependent options
- Expected Shortfall (ES) and coherent risk measures
- Extreme value theory and tail risk modeling
- FX futures and currency hedging
- Fama-French three-factor and five-factor models
- Fintech disruption and digital banking
- GARCH models for volatility forecasting
- Gamma trading and convexity adjustments
- General equilibrium model
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
- Investment in production
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
- Real interest rates
- Recovery rate modeling and loss given default
- Repo markets and securities lending
- Risk factor decomposition and sensitivity analysis
- Risk parity and risk budgeting strategies
- Shadow banking and non-bank intermediation
- Smart beta and alternative indexing approaches
- Spot rates, forward rates, and discount factor curves
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
- Value at Risk (VaR) and risk metrics
- Value vs growth investing frameworks
- Vasicek and CIR interest rate models
- Vasicek and Cox-Ingersoll-Ross models
- Volatility smile and skew patterns in option markets
- Working capital and cash conversion cycle
- Wrong-way risk and correlation adjustments
enhanced: true
enhancement_date: '2025-11-06'
enhancement_id: batch04-867405
---




# 10.4 Real interest rates and aggregate production  

In order to study the relation between interest rates and production, we will look at a slightly simplified version of the general equilibrium model of Cox, Ingersoll, and Ross (1985a).  

Consider an economy with a single physical good that can be used either for consumption or. investment. All values are expressed in units of this good. The instantaneous rate of return on an investment in the production of the good is.  
$$
\frac{d\eta_{t}}{\eta_{t}}=g(x_{t})d t+\xi(x_{t})d z_{1t},
$$  

where $z_{1}$ is a standard one-dimensional Brownian motion and $g$ and $\xi$ are well-behaved real-valued functions (given by Mother Nature) of some state variable $x_{t}$ . We assume that $\xi(x)$ is non-negative for all values of $x$ . The above dynamics means that $\eta_{0}$ goods invested in the production process at time 0 will grow to $\eta_{t}$ goods at time $t$ if the output of the production process is continuously reinvested in this period. We can interpret $g$ as the expected real growth rate of production in the economy and the volatility $\xi$ (assumed positive for all $x$ ) as a measure of the uncertainty about the growth rate of production in the economy. The production process has constant returns to scale in the sense that the distribution of the rate of return is independent of the scale of the investment. There is free entry to the production process. We can think of individuals investing in production directly by forming their own firm or indirectly by investing in stocks of production firms. For simplicity we take the first interpretation. All producers, individuals and firms, act competitively so that firms have zero profits and just passes production returns on to their owners. All individuals and firms act as price takers.  

We assume that the state variable is a one-dimensional diffusion with dynamics  
$$
d x_{t}=m(x_{t})d t+v_{1}(x_{t})d z_{1t}+v_{2}(x_{t})d z_{2t},
$$  

where $z_{2}$ is another standard one-dimensional Brownian motion independent of $z_{1}$ , and $m$ $v_{1}$ , and $v_{2}$ are well-behaved real-valued functions. The instantaneous variance rate of the state variable is $v_{1}(x)^{2}+v_{2}(x)^{2}$ , the covariance rate of the state variable and the real growth rate is $\xi(x)v_{1}(x)$ so that the correlation between the state and the growth rate is $v_{1}(x)/\sqrt{v_{1}(x)^{2}+v_{2}(x)^{2}}$ . Unless $v_{2}~\equiv~0$ , the state variable is imperfectly correlated with the real production returns. If $v_{1}$ is positive [negative], then the state variable is positively [negatively] correlated with the growth rate of production in the economy. Since the state determines the expected returns and the variance of returns on real investments, we may think of. $x_{t}$ as a productivity or technology variable..  

In addition to the investment in the production process, we assume that the individuals have access to a financial asset with a price. $P_{t}$ with dynamics of the form.  
$$
\frac{d P_{t}}{P_{t}}=\mu_{t}d t+\sigma_{1t}d z_{1t}+\sigma_{2t}d z_{2t}.
$$  

As a part of the equilibrium we will determine the relation between the expected return $\mu_{t}$ and the sensitivity coefficients $\sigma_{1t}$ and $\sigma_{2t}$ . Finally, the individuals can borrow and lend funds at an instantaneously risk-free interest rate $r_{t}$ , which is also determined in equilibrium. The market is therefore complete. Other financial assets affected by $z_{1}$ and $z_{2}$ may be traded, but they will be redundant. We will get the same equilibrium relation between expected returns and sensitivity coefficients for these other assets as for the one modeled explicitly. For simplicity we stick to the case with a single financial asset..  

If an individual at each time $t$ consumes at a rate of $c_{t}\geq0$ , invests a fraction $\alpha_{t}$ of his wealth in the production process, invests a fraction. $\pi_{t}$ of wealth in the financial asset, and invests the remaining fraction $1-\alpha_{t}-\pi_{t}$ of wealth in the risk-free asset, his wealth $W_{t}$ will evolve as  
$$
\begin{array}{r}{d W_{t}=\left\{r_{t}W_{t}+W_{t}\alpha_{t}\left(g(x_{t})-r_{t}\right)+W_{t}\pi_{t}\left(\mu_{t}-r_{t}\right)-c_{t}\right\}d t}\ {+W_{t}\alpha_{t}\xi(x_{t})d z_{1t}+W_{t}\pi_{t}\sigma_{1t}d z_{1t}+W_{t}\pi_{t}\sigma_{2t}d z_{2t}.}\end{array}
$$  

Since a negative real investment is physically impossible, we should restrict $\alpha_{t}$ to the non-negative numbers. However, we will assume that this constraint is not binding.  

Let us look at an individual maximizing expected utility of future consumption. The indirect utility function is defined as  
$$
J(W,x,t)=\operatorname*{sup}_{\substack{(\alpha_{s},\pi_{s},c_{s})_{s\in[t,T]}}}\mathrm{E}_{t}\left[\int_{t}^{T}e^{-\delta(s-t)}u(c_{s})d s\right],
$$  

i.e. the maximal expected utility the individual can obtain given his current wealth and the current value of the state variable. The dynamic programming technique of Section 6.5.2 lead to the Hamilton-Jacobi-Bellman equation  
$$
\begin{array}{l}{{\delta J=\displaystyle\operatorname*{sup}_{\alpha,\pi,c}\Big\{u(c)+\frac{\partial J}{\partial t}+J_{W}\left(r W+\alpha W(g-r)+\pi W(\mu-r)-c\right)+J_{x}m}}\ {{\qquad+\displaystyle\frac{1}{2}J_{W W}W^{2}\left([\alpha\xi+\pi\sigma_{1}]^{2}+\pi^{2}\sigma_{2}^{2}\right)+\displaystyle\frac{1}{2}J_{x x}(v_{1}^{2}+v_{2}^{2})+J_{W x}W v_{1}(\alpha\xi+\pi\sigma_{1})\Big\}}}\end{array}
$$  

The first-order conditions for $\alpha$ and $\pi$ imply that  
$$
\begin{array}{l}{\displaystyle{\alpha^{*}=\frac{-J_{W}}{W J_{W W}}\left[(g-r)\frac{\sigma_{1}^{2}+\sigma_{2}^{2}}{\xi^{2}\sigma_{2}^{2}}-(\mu-r)\frac{\sigma_{1}}{\xi\sigma_{2}^{2}}\right]+\frac{-J_{W x}}{W J_{W W}}\frac{\sigma_{2}v_{1}-\sigma_{1}v_{2}}{\xi\sigma_{2}},}}\ {\displaystyle{\pi^{*}=\frac{-J_{W}}{W J_{W W}}\left[-\frac{\sigma_{1}}{\xi\sigma_{2}^{2}}(g-r)+\frac{1}{\sigma_{2}^{2}}(\mu-r)\right]+\frac{-J_{W x}}{W J_{W W}}\frac{v_{2}}{\sigma_{2}}.}}\end{array}
$$  

In equilibrium, prices and interest rates are such that (a) all individuals act optimally and (b). all markets clear. In particular, summing up the positions of all individuals in the financial asset we should get zero, and the total amount borrowed by individuals on a short-term basis should equal the total amount lend by individuals. Since the available production apparatus is to be held by some investors, summing the optimal $\alpha$ 's over investors we should get 1. Since we have assumed. a complete market, we can construct a representative individual, i.e. an individual with a given utility function so that the equilibrium interest rates and price processes are the same in the single individual economy as in the larger multi-individual economy. (Alternatively, we may think of the case where all individuals in the economy are identical so that they will have the same indirect utility function and always make the same consumption and investment choice.).  

In an equilibrium, we have. $\pi^{*}=0$ for a representative individual, and hence (10.26) implies that  
$$
\mu-r=\frac{\sigma_{1}}{\xi}(g-r)-\frac{\left(\frac{-J_{W x}}{W J_{W W}}\right)}{\left(\frac{-J_{W}}{W J_{W W}}\right)}\sigma_{2}v_{2}.
$$  

Substituting this into the expression for $\alpha^{*}$ and using the fact that. ${\boldsymbol{\alpha}}^{*}=1$ in equilibrium, we get. that  
$$
\begin{array}{l}{{1=\left(\displaystyle{\frac{-J_{W}}{W J_{W W}}}\right)\left[(g-r)\frac{\sigma_{1}^{2}+\sigma_{2}^{2}}{\xi^{2}\sigma_{2}^{2}}-\frac{\sigma_{1}}{\xi}\frac{\sigma_{1}}{\xi\sigma_{2}^{2}}(g-r)+\frac{\left(\displaystyle{\frac{-J_{W x}}{W J_{W W}}}\right)}{\left(\displaystyle{\frac{-J_{W x}}{W J_{W W}}}\right)}\sigma_{2}v_{2}\frac{\sigma_{1}}{\xi\sigma_{2}^{2}}\right]}}\ {{+\left(\displaystyle{\frac{-J_{W x}}{W J_{W W}}}\right)\frac{\sigma_{2}v_{1}-\sigma_{1}v_{2}}{\xi\sigma_{2}}}}\ {{=\left(\displaystyle{\frac{-J_{W}}{W J_{W W}}}\right)\frac{g-r}{\xi^{2}}+\left(\displaystyle{\frac{-J_{W x}}{W J_{W W}}}\right)\frac{v_{1}}{\xi}.}}\end{array}
$$  

Consequently, the equilibrium short-term interest rate can be written as  
$$
r=g-\left({\frac{-W J_{W W}}{J_{W}}}\right)\xi^{2}+{\frac{J_{W x}}{J_{W}}}\xi v_{1}.
$$  

This equation ties the equilibrium real short-term interest rate to the production side of the economy. Let us address each of the three right-hand side terms:.  

. The equilibrium real interest rate. $r$ is positively related to the expected real growth rate. $g$ of the economy. The intuition is that for higher expected growth rates, the productive. investments are more attractive relative to the risk-free investment, so to maintain market. clearing the interest rate has to be higher as well..   
. The term $-W J_{W W}/J_{W}$ is the relative risk aversion of the representative individual's indirect utility. This is assumed to be positive. Hence, we see that the equilibrium real interest rate $r$ is negatively related to the uncertainty about the growth rate of the economy, represented by the instantaneous variance $\xi^{2}$ . For a higher uncertainty, the safe returns of a risk-free. investment is relatively more attractive, so to establish market clearing the interest rate has to decrease.   
: The last term in (10.28) is due to the presence of the state variable. The covariance rate of the state variable and the real growth rate of the economy is equal to. $\xi v_{1}$ . Suppose that high values of the state variable represent good states of the economy, where the wealth of the individual is high. Then the marginal utility. $J_{W}$ will be decreasing in $x$ , i.e. $J_{W x}<$ O. If instantaneous changes in the state variable and the growth rate of the economy are. positively correlated, we see from (10.25) that the hedge demand of the productive investment. is decreasing, and hence the demand for depositing money at the short rate increasing, in the magnitude of the correlation (both $J_{W x}$ and $J_{W W}$ are negative). To maintain market clearing, the interest rate must be decreasing in the magnitude of the correlation as reflected by (10.28).  

We see from (10.27) that the market prices of risk are given by  
$$
\lambda_{1}=\frac{g-r}{\xi},\quad\lambda_{2}=-\frac{\bigg(\frac{-J_{W x}}{W J_{W W}}\bigg)}{\bigg(\frac{-J_{W}}{W J_{W W}}\bigg)}v_{2}=-\frac{J_{W x}}{J_{W}}v_{2}.
$$  

Applying the relation  
$$
g-r=\left(\frac{-W J_{W W}}{J_{W}}\right)\xi^{2}-\frac{J_{W x}}{J_{W}}\xi v_{1},
$$  

we can rewrite $\lambda_{1}$ as  
$$
\lambda_{1}=\left(\frac{-W J_{W W}}{J_{W}}\right)\xi-\frac{J_{W x}}{J_{W}}v_{1}.
$$

---
tags:
- apt
- artificial-intelligence
- beta
- capm
- consumption_based_model
- factor-models
- factor_models
- fixed-income
- interest-rate-derivatives
- interest-rate-swap
- intertemporal_capm
- irs
- ito-calculus
- ma
- market_portfolio
- markets
- mpt
- option-greeks
- options
- options-pricing
- risk-management
- stochastic
- theoretical_factors
- value-at-risk
- var
aliases:
- Intertemporal CAPM
- Theoretical Factors
key_concepts:
- Agricultural futures and seasonality
- Alternative investments and hedge fund strategies
- Arbitrage Pricing Theory (APT) and factor models
- Arbitrage pricing theory (APT)
- Asset swaps and spread-lock strategies
- Bank capital adequacy and Basel III compliance
- Barrier options and knock-in/knock-out structures
- Basel III capital requirements and risk metrics
- Basis swaps and cross-currency basis adjustments
- Basis swaps and floating rate correlations
- Behavioral finance and market anomalies
- Best execution and regulatory requirements
- Bid-ask spreads and market making profitability
- Binomial option pricing model with multi-period trees
- Black-Litterman model and portfolio optimization
- Black-Scholes option pricing model and its applications
- Bond portfolio immunization strategies
- CDO structuring and tranche allocation methodologies
- CDO-squared structures and correlation trading
- Calendar spreads and roll strategies
- Capital Asset Pricing Model (CAPM)
- Capital Asset Pricing Model (CAPM) and beta estimation
- Capital expenditure planning and depreciation
- Central clearing and CCP risk management
- Commodity futures and convenience yields
- Commodity swaps and energy derivatives
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
- Equity swaps and total return swaps
- Exotic derivatives and path-dependent options
- Expected Shortfall (ES) and coherent risk measures
- Expected excess return
- Extreme value theory and tail risk modeling
- FX futures and currency hedging
- Fama-French three-factor and five-factor models
- Fintech disruption and digital banking
- Forward contract pricing and cost of carry
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
- Ito's Lemma and stochastic calculus
- Key rate duration and curve risk decomposition
- Liquidity-adjusted VaR and liquidity horizons
- Margin requirements and collateral optimization
- Market impact and transaction cost analysis
- Market price of risk
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
- Optimal consumption plan
- Options on futures and forward-starting options
- Payment systems and settlement risk
- Portfolio optimization and mean-variance theory
- Prime brokerage and securities lending
- Private credit and direct lending
- Project finance and syndicated lending
- Real estate investment trusts (REITs)
- Recovery rate modeling and loss given default
- Repo markets and securities lending
- Representative individual wealth
- Risk factor decomposition and sensitivity analysis
- Risk parity and risk budgeting strategies
- Shadow banking and non-bank intermediation
- Smart beta and alternative indexing approaches
- State-price deflator dynamics
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
- Volatility smile and skew patterns in option markets
- Working capital and cash conversion cycle
- Wrong-way risk and correlation adjustments
- Yield curve construction and term structure modeling
- Zero-coupon bond pricing and bootstrapping
enhanced: true
enhancement_date: '2025-11-06'
enhancement_id: batch04-214260
---




# 9.7 Theoretical factors  

Factor models can be obtained through the general consumption-based asset pricing model by relating optimal consumption to various factors. As discussed in Section 6.5 the optimal consumption plan of an individual with time-additive expected utility must satisfy the so-called envelope condition  
$$
u^{\prime}(c_{t})=J_{W}(W_{t},x_{t},t).
$$  

Here $J$ is the indirect utility function of the individual, i.e. the maximum obtainable expected utility of future consumption. $W_{t}$ is the financial wealth of the investor at time $t$ $x_{t}$ is the time $t$ value of a variable that captures the variations in investment opportunities (captured by the riskfree interest rate, expected returns and volatilities on risky assets, and correlations between risky assets) and investor-specific variables (e.g. labor income). For notational simplicity, $x$ is assumed to be one-dimensional, but this could be generalized.  

In a continuous-time framework write the dynamics of wealth compactly as  
$$
d W_{t}=W_{t}\left[\mu_{W t}d t+\pmb{\sigma}_{W t}^{\top}d z_{t}\right]
$$  

and assume that the state variable $x$ follows a diffusion process.  
$$
d x_{t}=\mu_{x t}d t+\sigma_{x t}^{\top}d z_{t},\qquad\mu_{x t}=\mu_{x}(x_{t},t),\quad\sigma_{x t}=\sigma_{x}(x_{t},t).
$$  

From (8.16) it follows that the state-price deflator derived from this individual can be written as  
$$
\zeta_{t}=e^{-\delta t}\frac{J_{W}(W_{t},x_{t},t)}{J_{W}(W_{0},x_{0},0)}.
$$  

An application of Ito's Lemma yields a new expression for the dynamics of $\zeta$ , which again can be compared with (4.41). It follows from this comparison that.  
$$
\lambda_{t}=\left(\frac{-W_{t}J_{W W}(W_{t},x_{t},t)}{J_{W}(W_{t},x_{t},t)}\right)\sigma_{W t}+\left(\frac{-J_{W x}(W_{t},x_{t},t)}{J_{W}(W_{t},x_{t},t)}\right)\sigma_{x t},
$$  

is a market price of risk. Consequently, the expected excess rate of return on asset $i$ can be written  
$$
\mu_{i t}+\delta_{i t}-r_{t}^{f}=\left(\frac{-W_{t}J_{W W}(W_{t},x_{t},t)}{J_{W}(W_{t},x_{t},t)}\right)\sigma_{i t}^{\top}\sigma_{W t}+\left(\frac{-J_{W x}(W_{t},x_{t},t)}{J_{W}(W_{t},x_{t},t)}\right)\sigma_{i t}^{\top}\sigma_{x t},
$$  

which can be rewritten as  
$$
\mu_{i t}+\delta_{i t}-r_{t}^{f}=\beta_{i W t}\eta_{W t}+\beta_{i x t}\eta_{x t},
$$  

where  
$$
\begin{array}{r}{\beta_{i W t}=\frac{\sigma_{i t}^{\top}\sigma_{W t}}{\ | \sigma_{W t}\ | ^{2}},\quad\beta_{i x t}=\frac{\sigma_{i t}^{\top}\sigma_{x t}}{\ | \sigma_{x t}\ | ^{2}},\quad}\ {\eta_{W t}=\ | \sigma_{W t}\ | ^{2}\left(\frac{-W_{t}J_{W W}\left(W_{t},x_{t},t\right)}{J_{W}\left(W_{t},x_{t},t\right)}\right),\quad\eta_{x t}=\ | \sigma_{x t}\ | ^{2}\left(\frac{-J_{W x}\left(W_{t},x_{t},t\right)}{J_{W}\left(W_{t},x_{t},t\right)}\right).}\end{array}
$$  

We now have a continuous-time version of (9.35) with the wealth of the individual and the state variable as the factors.If it takes. $m$ state variables to describe the variations in investment. opportunities, labor income, etc., we get an. $(m+1)$ -factor model.  

If the individual is taken to be a representative individual, her wealth will be identical to the. aggregate value of all assets in the economy, including all traded financial assets and non-traded. asset such as human capital. This is like the market portfolio in the traditional static CAPM. The first term on the right-hand side of (9.42) is then the product of the relative risk aversion of the representative individual (derived from her indirect utility) and the covariance between the rate of return on asset $i$ and the rate of return on the market portfolio. In the special case where the. indirect utility is a function of wealth and time only, the last term on the right-hand side will be zero, and we get the well-known relation.  
$$
\mu_{i t}+\delta_{i t}-r_{t}^{f}=\beta_{i W t}\left(\mu_{W t}+\delta_{W t}-r_{t}^{f}\right),
$$  

where $\beta_{i W t}$ is the "market-beta' of asset. $i$ . This is a continuous-time version of the traditional. static CAPM. This is only true under the strong assumption that individuals do not care about. variations in investment opportunities, income, etc. In general we have to add factors describing the future investment opportunities, future labor income, etc. This extension of the CAPM is called the Intertemporal CAPM and was first derived by Merton (1973b)..  

Only few empirical studies of factor models refer to Merton's Intertemporal CAPM when motivating the choice of factors. Brennan, Wang, and Xia (2004) set up a simple model with the short-term real interest rate and the slope of the capital market line as the factors since these variables capture the investment opportunities. In an empirical test, this model performs as well as the Fama-French model, which is encouraging for the development of theoretically well-founded and empirically viable factor models.

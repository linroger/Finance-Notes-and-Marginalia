---
tags:
- apt
- artificial-intelligence
- asset_allocation
- asset_pricing
- banking
- beta
- capital_budgeting
- capital_structure
- capm
- credit
- credit-derivatives
- equity-derivatives
- financial_markets
- interest-rate-derivatives
- ito-calculus
- ma
- markets
- mpt
- options
- options-pricing
- resolution
- risk-management
- sifi
- stochastic
- value-at-risk
- var
aliases:
- CAPM
- Modern Asset Pricing
key_concepts:
- Agricultural futures and seasonality
- Alternative investments and hedge fund strategies
- American vs European options and early exercise features
- Arbitrage Pricing Theory (APT) and factor models
- Arbitrage pricing theory (APT)
- Asset swaps and spread-lock strategies
- Bank asset-liability management (ALM) strategies
- Bank capital adequacy and Basel III compliance
- Bank stress testing and CCAR requirements
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
- Central bank digital currencies (CBDCs)
- Central clearing and CCP risk management
- Commodity futures and convenience yields
- Commodity swaps and energy derivatives
- Corporate bond pricing and credit spread decomposition
- Crack spreads in energy markets
- Credit default swaps and credit protection mechanisms
- Credit risk assessment and loan pricing
- Credit valuation adjustment (CVA) and counterparty risk
- Cryptocurrency valuation and blockchain technology
- Currency swaps and cross-currency basis
- Dark pools and alternative trading venues
- DeFi protocols and decentralized finance
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
- Forward contract pricing and cost of carry
- Futures vs forwards and delivery options
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
- Ito's Lemma and stochastic calculus
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
- Value at Risk (VaR) and risk metrics
- Value vs growth investing frameworks
- Vasicek and CIR interest rate models
- Volatility smile and skew patterns in option markets
- Weighted average cost of capital (WACC) calculations
- Working capital and cash conversion cycle
- Wrong-way risk and correlation adjustments
- Zero-coupon bond pricing and bootstrapping
- asset allocation
- capital budgeting decisions
- financial risk management
- pricing financial assets
- shareholders vs creditors
enhanced: true
enhancement_date: '2025-11-06'
enhancement_id: batch04-353396
---




# 1.1 What is modern asset pricing?  

Asset pricing models are models for the pricing of financial assets. It is interesting in itself to be able to model and understand the pricing mechanisms in the seemingly complex financial markets, but it is also important for a number of financial problems faced by individuals and corporations such as  

asset allocation: how individual and institutional investors combine various financial assets into portfolios;   
the measurement and management of financial risks, e.g. in banks and other financial insti-. tutions;   
capital budgeting decision in firms;   
capital structure decisions in firms;   
. the identification and possible resolution of potential conflicts of interest between the stakeholders of a firm, e.g. shareholders vs. creditors, shareholders vs. managers.  

To the extent that central banks and governments want to control or at least influence financial markets, e.g. setting interest rates or limiting stock market volatility, they also need a deep. understanding of the asset pricing mechanisms and the link between financial markets and macro-. economics. Finally, there is a trend in accounting regulation towards more market-oriented valuation of assets and liabilities instead of the traditional valuation at historical costs..  

Undoubtedly, the Capital Asset Pricing Model (CAPM) developed by Sharpe (1964), Lintner (1965), and Mossin (1966) is the best known asset pricing model. The key message of the model is that the expected excess return on a risky financial asset is given by the product of the market-beta of the asset and the expected excess return on the market portfolio. In symbols, the relation can be written as  
$$
\operatorname{E}[R_{i}]-R^{f}=\beta_{i}\left(\operatorname{E}[R_{M}]-R^{f}\right).
$$  

Here the "excess return' of an asset or a portfolio is the return $R_{i}$ less the risk-free return $R^{f}$ and the "market-beta' of an asset is the covariance between the return on this asset and the return on the market portfolio, divided by the variance of the return on the market portfolio, i.e. $\beta_{i}=\mathrm{Cov}[R_{i},R_{M}]/\mathrm{Var}[R_{M}]$ . Only the risk correlated with the market will give a risk premium in terms of a higher expected return (assuming the market-beta is positive). The remaining risk can be diversified away and is therefore not priced in equilibrium. In principle, the market portfolio includes all assets, not only traded financial assets but also non-traded assets like the human capital (value of labor income) of all individuals. However, the market portfolio is typically approximated by a broad stock index, although this approximation is not necessarily very precise.  

The CAPM has been very successful as a pedagogical tool for presenting and quantifying the. tradeoff between risk and (expected) return, and it has also been widely used in practical applications. It captures some important characteristics of the pricing in financial markets in a rather simple way. However, the CAPM is insufficient in many aspects and it is based on a number of. unrealistic assumptions. Here is a partial list of problems with the CAPM:.  

[^1]: The original CAPM is formulated and derived in a one-period world where assets and investors are only modeled over one common period. In applications, it is implicitly assumed that the CAPM repeats itself period by period which intuitively demands some sort of independence between the pricing mechanisms in different periods, which again requires the unrealistic assumption that the demand and supply of agents living for several periods are. the same in all periods..
[^2]: The CAPM is not designed for capturing variations in asset prices over time and cannot do SO.
[^3]: Typical derivations of the CAPM assume that all asset returns over the fixed period are. normally distributed. For assets with limited liability you cannot loose more than you have invested so the rate of return cannot be lower than. $-100\%$ , which is inconsistent with the normal distribution that associates a positive probability to any return between. $-\infty$ and $+\infty$ . Empirical studies show that for many assets the normal distribution is not even a good approximation of the return distribution..
[^4]: The true market portfolio contains many unobservable assets so how should you find the expected return and variance on the market portfolio and its covariances with all individual assets?
[^5]: The CAPM is really quite unsuccessful in explaining empirical asset returns. Differences in market-betas cannot explain observed differences in average returns of stocks..
[^6]: The CAPM is not a full asset pricing model in the sense that it does not say anything. about what the return on the risk-free asset or the expected return on the market portfolio should be. And it does not offer any insight into the links between financial markets and macroeconomic variables like consumption, production, and inflation/War%20Economies%20and%20Hyperinflation.md)..

The purpose of this book is to develop a deeper understanding of asset pricing than the CAPM can offer.  

When an investor purchases a given asset, she obtains the right to receive the future payments of the asset. For many assets the size of these future payments is uncertain at the time of purchase since it may depend on the overall state of the economy and/or the state of the issuer of the asset at the payment dates. Risk-averse investors will value a payment of a given size more highly if they receive it in a "bad' state than in a "good" state. This is captured by the term "state price" introduced by Arrow (1953). A state price for a given state at a given future point in time indicates how much investors are willing to sacrifice today in return for an extra payment of one unit in that future state. Presumably investors will value a given payment in a given state the same no matter. which asset the payment comes from. Therefore state prices are valid for all assets. The value of any specific asset is determined by the general state prices in the market and the state-contingent future payments of the asset. Modern asset pricing theory is based on models of the possible states and the associated state prices.  

The well-being of individuals will depend on their consumption of goods throughout their lives. By trading financial assets they can move consumption opportunities from one point in time to another and from one state of the world to another. The preferences for consumption of individuals determine their demand for various assets and thereby the equilibrium prices of these assets. Hence, the state price for any given state must be closely related to the individuals' (marginal) utility of consumption in that state. Many modern asset pricing theories and models are based on this link between asset prices and consumption.

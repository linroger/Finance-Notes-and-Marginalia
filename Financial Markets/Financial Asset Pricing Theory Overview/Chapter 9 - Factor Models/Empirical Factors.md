---
tags:
- artificial-intelligence
- beta
- book-value
- empirical_factors
- equity-derivatives
- factor-models
- factor_models
- fama_french_model
- ma
- market-value
- market_data
- options
- risk-management
- risk_premia
- size-effect
- value-at-risk
- var
aliases:
- Empirical Factor
- Fama and French
key_concepts:
- Agricultural futures and seasonality
- Alternative investments and hedge fund strategies
- Arbitrage Pricing Theory (APT) and factor models
- Arbitrage pricing theory (APT)
- Asset swaps and spread-lock strategies
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
- CDO structuring and tranche allocation methodologies
- CDO-squared structures and correlation trading
- Calendar spreads and roll strategies
- Capital Asset Pricing Model (CAPM)
- Capital Asset Pricing Model (CAPM) and beta estimation
- Central clearing and CCP risk management
- Commodity futures and convenience yields
- Commodity swaps and energy derivatives
- Corporate bond pricing and credit spread decomposition
- Crack spreads in energy markets
- Credit risk assessment and loan pricing
- Cryptocurrency valuation and blockchain technology
- Currency swaps and cross-currency basis
- Dark pools and alternative trading venues
- Data snooping biases
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
- Factor models and betas
- Fama-French three factors
- Fama-French three-factor and five-factor models
- Fintech disruption and digital banking
- Forward contract pricing and cost of carry
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
- Interest rate swaps and swap spread decomposition
- Liquidity coverage ratio and funding strategies
- Liquidity-adjusted VaR and liquidity horizons
- Margin requirements and collateral optimization
- Market data performance
- Market impact and transaction cost analysis
- Mean reversion in interest rate processes
- Measurement of beta
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
- Working capital and cash conversion cycle
- Wrong-way risk and correlation adjustments
- Zero-coupon bond pricing and bootstrapping
enhanced: true
enhancement_date: '2025-11-06'
enhancement_id: batch04-350289
---




# 9.6 Empirical factors  

A large part of the literature on factor models is based on empirical studies which for a given. data set identifies a number of priced factors so that most of the differences between the returns on different financial assets- -typically only various portfolios of stocks-can be explained by their different factor betas. The best known studies of this kind were carried out by Fama and French, who find support for a model with three factors:.  

[^1]: the return on a broad stock market index;
[^2]: the return on a portfolio of stocks in small companies (according to the market value of all stocks issued by the firm) minus the return on a portfolio of stocks in large companies;
[^3]: the return on a portfolio of stocks issued by firms with a high book-to-market value (the ratio between the book value of the assets of the firm to the market value of all the assets) minus the return on a portfolio of stocks in firms with a low book-to-market value.

According to Fama and French (1996) such a model gives a good fit of U.S. stock market data over. the period 1963-1993. However, the empirical analysis does not explain why this three-factor model does well and what the underlying pricing mechanisms might be. Also note that while a given. factor model does well in a given market over a given period it may perform very badly in other. markets and/or other periods (and risk premia may be different for other data sets). Some recent studies indicate that the second of the three factors (the "size effect"') seems to have disappeared. Another critique is that over the last 30 years empirical researchers have tried so many factors that it is hardly surprising that they have found some statistically significant factors. In fact, we know that in any given sample of historical returns it is possible to find a portfolio so that a factor model with the return on this portfolio as the only factor will perfectly explain all returns in the sample! Also note that the Fama-French model is a partial pricing model since the factors themselves are derived from prices of financial assets. For these reasons the purely empirically based "models" do not contribute much to the understanding of the pricing mechanisms of financial markets. However, some interesting recent studies explore whether the Fama-French factors can be seen as proxies for macro-economic variables that can logically be linked to asset prices.  

Linking Fama-French factors to risk and variations in investment opportunities: Liew and Vassalou (2000), Lettau and Ludvigson (2001), Vassalou (2003), Petkova (2006).  

Data snooping/biases explanations of the success of FF: Lo and MacKinlay (1990), Kothari, Shanken, and Sloan (1995).  

Problems in measurement of beta: Berk, Green, and Naik (1999), Gomes, Kogan, and Zhang (2003).

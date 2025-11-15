---
tags:
- apt
- arbitrage
- artificial-intelligence
- asset_pricing
- bond-pricing
- book_organization
- capm
- defi
- equity-derivatives
- factor-models
- financial_assets
- fixed-income
- fixed-income-derivatives
- interest-rate-derivatives
- ma
- markets
- mpt
- options
- options-pricing
- state_price_deflator
- stochastic
- stochastic_processes
- term-structure
aliases:
- Book Structure
key_concepts:
- Agricultural futures and seasonality
- Alternative investments and hedge fund strategies
- Arbitrage Pricing Theory (APT) and factor models
- Arbitrage and market completeness
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
- Bond prices and term structure
- CDO structuring and tranche allocation methodologies
- CDO-squared structures and correlation trading
- Calendar spreads and roll strategies
- Capital Asset Pricing Model (CAPM)
- Capital Asset Pricing Model (CAPM) and beta estimation
- Capital expenditure planning and depreciation
- Central clearing and CCP risk management
- Commodity futures and convenience yields
- Commodity swaps and energy derivatives
- Consumption and investment decisions
- Consumption-based CAPM (CCAPM)
- Corporate bond pricing and credit spread decomposition
- Crack spreads in energy markets
- Credit risk assessment and loan pricing
- Cryptocurrency valuation and blockchain technology
- Currency swaps and cross-currency basis
- Dark pools and alternative trading venues
- DeFi protocols and decentralized finance
- Delta hedging strategies in options markets
- Deposit insurance and systemic risk
- Derivative securities discussion
- Discounted cash flow (DCF) valuation methodologies
- Dividend discount model (DDM) applications
- Duration and convexity for bond price sensitivity
- ESG investing and sustainability metrics
- Enterprise value and equity value relationships
- Equity swaps and total return swaps
- Exotic derivatives and path-dependent options
- Expected Shortfall (ES) and coherent risk measures
- Extreme value theory and tail risk modeling
- FX futures and currency hedging
- Factor models of asset pricing
- Fama-French three-factor and five-factor models
- Financial asset modeling
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
- Interest rate models and term structure
- Interest rate swaps and swap spread decomposition
- Investor preferences representation
- Key rate duration and curve risk decomposition
- Liquidity-adjusted VaR and liquidity horizons
- Margin requirements and collateral optimization
- Market equilibrium analysis
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
- Risk-adjusted probability measure
- Risk-neutral valuation and martingale measures
- Shadow banking and non-bank intermediation
- Smart beta and alternative indexing approaches
- State-price deflator definition
- Stochastic processes introduction
- Stochastic volatility in interest rate markets
- Stress testing and scenario analysis frameworks
- Swaptions and interest rate option pricing
- Swaptions and option volatility surfaces
- Synthetic CDOs and credit-linked note structures
- 'The Greeks: Delta, Gamma, Vega, Theta, and Rho sensitivity analysis'
- Too-big-to-fail policies and resolution regimes
- Treasury futures and bond basis
- Treasury securities and government bond markets
- Uncertainty and information flow
- VIX futures and volatility trading
- Value at Risk (VaR) and expected shortfall methodologies
- Vasicek and CIR interest rate models
- Volatility smile and skew patterns in option markets
- Working capital and cash conversion cycle
- Wrong-way risk and correlation adjustments
- Zero-coupon bond pricing and bootstrapping
enhanced: true
enhancement_date: '2025-11-06'
enhancement_id: batch04-359448
---




# 1.4 The organization of this book  

The remainder of this book is organized as follows. Chapter 2 discusses how to represent uncertainty and information flow in asset pricing models. It also introduces stochastic processes and some key results on how to deal with stochastic processes, which we will use in later chapters.  

Chapter 3 shows how we can model financial assets and their dividends as well as how we can represent portfolios and trading strategies. It also defines the important concepts of arbitrage, redundant assets, and market completeness.  

Chapter 4 defines the key concept of a state-price deflator both in one-period models, in discretetime multi-period models, and in continuous-time models. A state-price deflator is one way to represent the general pricing mechanism of a financial market. We can price any asset given the state-price deflator and the dividend process of that asset. Conditions for the existence and uniqueness of a state-price deflator are derived as well as a number of useful properties of stateprice deflators. We will also briefly discuss alternative ways of representing the general market pricing mechanism, e.g. through a set of risk-neutral probabilities.  

The state-price deflator and therefore asset prices are ultimately determined by the supply and demand of investors. Chapter 5 studies how we can represent the preferences for investors. We discuss when preferences can be represented by expected utility, how we can measure the risk aversion of an individual, and introduce some frequently used utility functions. In Chapter 6 we investigate how individual investors will make decisions on consumption and investments. We set up the utility maximization problem for the individual and characterize the solution for different relevant specifications of preferences. The solution gives an important link between state-price deflators (and, thus, the prices of financial assets) and the optimal decisions at the individual level. Chapter 7 deals with the market equilibrium. We will discuss when market equilibria are Paretoefficient and when we can think of the economy as having only one, representative individual instead of many individuals.  

Chapter 8 further explores the link between individual consumption choice and asset prices. The very general Consumption-based Capital Asset Pricing Model (CCAPM) is derived. A simple version of the CCAPM is confronted with data and a number of extensions are discussed.  

Chapter 9 studies the so-called factor models of asset pricing where one or multiple factors. govern the state-price deflators and thus asset prices and returns. Some empirically successful. factor models are described. It is also shown how pricing factors can be identified theoretically as a special case of the general CCAPM.  

While Chapters 8 and 9 mostly focus on explaining the expected excess return of risky assets, most prominently stocks, Chapter 10 explores the implications of general asset pricing theory for bond prices and the term structure of interest rates. It also critically reviews some traditional hypotheses on the term structure of interest rates.  

Chapter 11 shows how the information in a state-price deflator equivalently can be represented by the price of one specific asset and an appropriately risk-adjusted probability measure. This turns out to be very useful when dealing with derivative securities, which is the topic of Chapter 12.  

Each chapter ends with a number of exercises, which either illustrate the concepts and conclusions of the chapter or provide additional related results.

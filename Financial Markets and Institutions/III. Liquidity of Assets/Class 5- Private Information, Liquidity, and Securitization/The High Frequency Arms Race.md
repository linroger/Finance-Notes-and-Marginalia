---
linter-yaml-title-alias: 'The HFT Arms Race: Example'
title: The High Frequency Arms Race
tags:
- artificial-intelligence
- cme_nyse
- derivatives-pricing
- duration
- equity-derivatives
- fixed-income
- high_frequency_trading
- limit_order_book
- ma
- market_correlation
- market_design
- resolution
aliases:
- Frequent Batch Auctions
- HFT Arms Race
key_concepts:
- Agricultural futures and seasonality
- Alternative investments and hedge fund strategies
- American vs European options and early exercise features
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
- CDS spread curves and hazard rate modeling
- CME and NYSE data
- Calendar spreads and roll strategies
- Central clearing and CCP risk management
- Commodity futures and convenience yields
- Commodity swaps and energy derivatives
- Crack spreads in energy markets
- Cryptocurrency valuation and blockchain technology
- Currency swaps and cross-currency basis
- Dark pools and alternative trading venues
- DeFi protocols and decentralized finance
- Deposit insurance and systemic risk
- Duration and convexity for bond price sensitivity
- ES vs SPY
- ESG investing and sustainability metrics
- Enterprise value and equity value relationships
- Equity swaps and total return swaps
- Exotic derivatives and path-dependent options
- Expected Shortfall (ES) and coherent risk measures
- FX futures and currency hedging
- Fama-French three-factor and five-factor models
- Fintech disruption and digital banking
- Futures vs forwards and delivery options
- GARCH models for volatility forecasting
- Gamma trading and convexity adjustments
- Green bonds and climate risk assessment
- HJM and forward rate model frameworks
- High frequency trading and algorithmic strategies
- High-frequency trading
- Historical simulation and parametric VaR approaches
- Hull-White and Black-Karasinski short rate models
- IPO pricing and underpricing analysis
- Implied volatility and volatility surface modeling
- Inflation-linked swaps and CPI adjustments
- Key rate duration and curve risk decomposition
- Limit order book
- Liquidity coverage ratio and funding strategies
- Liquidity-adjusted VaR and liquidity horizons
- Margin requirements and collateral optimization
- Market correlations breakdown
- Market impact and transaction cost analysis
- Mean reversion in interest rate processes
- Mergers and acquisitions due diligence
- Metal futures and industrial commodities
- Model backtesting and validation procedures
- Momentum and reversal investment strategies
- Mortgage-backed securities and prepayment modeling
- Net interest margin and banking profitability
- Netting agreements and close-out procedures
- Non-deliverable forwards and emerging market instruments
- OIS discounting and collateralized interest rate derivatives
- Option-adjusted spread (OAS) analysis
- Options on futures and forward-starting options
- Payment systems and settlement risk
- Prime brokerage and securities lending
- Private credit and direct lending
- Project finance and syndicated lending
- Real estate investment trusts (REITs)
- Repo markets and securities lending
- Risk parity and risk budgeting strategies
- Shadow banking and non-bank intermediation
- Smart beta and alternative indexing approaches
- Stochastic volatility in interest rate markets
- Stress testing and scenario analysis frameworks
- Swaptions and interest rate option pricing
- Swaptions and option volatility surfaces
- Synthetic CDOs and credit-linked note structures
- 'The Greeks: Delta, Gamma, Vega, Theta, and Rho sensitivity analysis'
- Too-big-to-fail policies and resolution regimes
- Treasury futures and bond basis
- Treasury securities and government bond markets
- VIX futures and volatility trading
- Value at Risk (VaR) and expected shortfall methodologies
- Value vs growth investing frameworks
- Vasicek and CIR interest rate models
- Volatility smile and skew patterns in option markets
- Working capital and cash conversion cycle
- Wrong-way risk and correlation adjustments
enhanced: true
enhancement_date: '2025-11-06'
enhancement_id: batch04-244356
---




A few slides taken from: The High-Frequency Trading Arms Race: Frequent Batch Auctions as a Market Design Response Eric Budish,  Peter Cramton and John Shim Forthcoming,  Quarterly Journal of Economics Seminar Slides,  Sept 2015

# The High Frequency Arms Race

!1_Image_0.Png

- In 2010,  Spread Networks invests $300mm to dig a high-speed ber optic cable from NYC to Chicago.
- Shaves round-trip data transmission time … from 16ms to 13ms.
- Industry observers: 3ms is an eternity. Anybody pinging both markets has to be on this line,  or they're dead.
- Joke at the time: next innovation will be to dig a tunnel,  avoiding the planet's pesky curvature.
- Joke isn't that funny … Spread's cable is already obsolete!
- Not tunnels,  but microwaves (rst 10ms,  then 9ms,  now 8ms).
- Analogous races occurring throughout the financial system,  sometimes measured as minutely as microseconds or nanoseconds

# Brief Description Of The Continuous Limit Order Book

- Basic building block: limit order
- Species a price,  quantity,  and buy/sell (bid/ask)
- Buy 100 shares of XYZ at $100.00
- Traders may submit limit orders to the market at any time during the trading day
- Also may cancel or modify outstanding limit orders at any time
- Orders and cancellations are processed by the exchange one-at-a-time in order of receipt (serial process)
- Set of outstanding orders is known as the limit order book
- Trade occurs whenever a new limit order is submitted that is either (i) bid ≥ lowest ask; (ii) ask ≤ highest bid
- New limit order is interpreted as accepting (fully or partially) one or more outstanding orders
- Direct feed data from Chicago Mercantile Exchange (CME) and New York Stock Exchange (NYSE)
- Gives play by play of limit order book
- Millisecond resolution time stamps
- These are the data HFT rms subscribe to and parse in real time
- Focus primarily on a pair of instruments that track the S&$P$ 500 index
- ES: E-MinS&P 500 Future,  traded on CME
- SPY: SPDR S&P 500 Exchange Traded Fund,  traded on NYSE (and other equities exchanges)
- Time period: 2005-2011 Market Correlations Break Down at High Frequency ES vs. SPY: 1 Day

!4_image_0.png

Market Correlations Break Down at High Frequency ES vs. SPY: 1 hour

!5_image_0.png

Market Correlations Break Down at High Frequency ES vs. SPY: 1 minute

!6_image_0.png

Market Correlations Break Down at High Frequency ES vs. SPY: 250 milliseconds

!7_image_0.png

# Arb Durations Over Time: 2005-2011

Median over time Distribution by year

!8_image_0.png

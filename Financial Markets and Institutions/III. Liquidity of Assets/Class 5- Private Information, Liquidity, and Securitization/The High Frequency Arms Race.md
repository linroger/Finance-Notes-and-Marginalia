---
aliases:
- Frequent Batch Auctions
- HFT Arms Race
- Market structure and trading
- Order types and execution
- Market making and liquidity provision
- Market liquidity and measurement
- Bid-ask spreads and transaction costs
- Market impact and execution
- Financial econometrics and regression
- Time series analysis in finance
- Volatility modeling (GARCH)
- Bond pricing and yield curves
- Duration and convexity hedging
- Credit spreads and bond valuation
- The High Frequency Arms Race and financial analysis
- The High Frequency Arms Race in modern finance
- Applications of The High Frequency Arms Race
- 'Case study: The High Frequency Arms Race'
linter-yaml-title-alias: 'The HFT Arms Race: Example'
- high-frequency
- spread
- correlation
- bonds
- regression
- liquidity
- duration
- trading
title: The High Frequency Arms Race
tags:
- bid-ask
- bond
- case-study
- commercial-paper
- crisis-analysis
- derivatives
- duration
- empirical-analysis
- equity
- financial-institutions
- financial-markets
- graduate-level
- hedging
- high-frequency
- institutional-analysis
- institutional-quality
- learning-from-crisis
- liquidity
- liquidity-management
- market-liquidity
- market-making
- market-structure
- mathematical-finance
- mbs
- money-markets
- professional-standard
- provision
- quantitative-methods
- real-world-example
- repo-markets
- securitization
- short-term-funding
- spread
- volatility
- yield-curve

key_concepts:
- Banking and Financial Intermediation
- Case Study Methodology
- Central Bank Liquidity Facilities
- Commercial Paper Markets
- Crisis Case Study Design
- Empirical Analysis of Financial Events
- Empirical Finance Research
- Financial Crisis Case Studies
- Financial Intermediation and Banking
- Financial Markets and Institutions
- Historical Financial Analysis
- Institutional Analysis of Financial Systems
- Institutional-Quality Financial Education
- Learning from Financial Crises
- Liquidity Crisis and Management
- Liquidity Risk and Management
- Market Structure and Microstructure
- Money Market Fund Dynamics
- Money Market Instruments
- Quantitative Methods in Finance
- Real-World Financial Examples
- Regulatory Framework in Financial Markets
- Repurchase Agreement Markets
- Risk Management and Hedging Strategies
- Short-Term Funding Markets

enhanced: true
enhancement_date: 2025-11-06
enhancement_id: batch06-af

type: note
created: 2025-11-06
modified: 2025-11-06
status: active
academic_level: graduate
professional_application: industry-standard
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

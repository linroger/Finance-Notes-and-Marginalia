---
tags:
- apt
- arbitrage
- artificial-intelligence
- banking
- bond-pricing
- credit
- credit-derivatives
- credit-spread
- defi
- duration
- e-mini
- equity-derivatives
- equity-value
- financial_markets
- fixed-income
- fixed-income-derivatives
- forward-contracts
- forward_transactions
- futures-contracts
- hedging-strategies
- interest-rate-derivatives
- interest-rate-swap
- irs
- libor
- ma
- markets
- mpt
- nim
- options
- options-pricing
- risk-management
- risk_transfer
- rwa
- settlement
- spot_markets
- transactional_structure
- value-at-risk
- var
aliases:
- Financial Markets Structure
- Transactional Finance
key_concepts:
- Agricultural futures and seasonality
- Alternative investments and hedge fund strategies
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
- CDS spread curves and hazard rate modeling
- Calendar spreads and roll strategies
- Capital Asset Pricing Model (CAPM) and beta estimation
- Capital expenditure planning and depreciation
- Central bank digital currencies (CBDCs)
- Central clearing and CCP risk management
- Commodity futures and convenience yields
- Commodity swaps and energy derivatives
- Constant maturity swaps and roll-over features
- Corporate bond pricing and credit spread decomposition
- Crack spreads in energy markets
- Credit default swaps and credit protection mechanisms
- Credit risk and default probability
- Credit risk assessment and loan pricing
- Credit valuation adjustment (CVA) and counterparty risk
- Cryptocurrency valuation and blockchain technology
- Currency swaps and cross-currency basis
- Dark pools and alternative trading venues
- DeFi protocols and decentralized finance
- Deposit insurance and systemic risk
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
- Fama-French three-factor and five-factor models
- Financial market bazaar
- Fintech disruption and digital banking
- Forward buy transaction
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
- Key rate duration and curve risk decomposition
- Liquidity coverage ratio and funding strategies
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
- Option-adjusted spread (OAS) analysis
- Options on futures and forward-starting options
- Payment systems and settlement risk
- Prime brokerage and securities lending
- Private credit and direct lending
- Project finance and syndicated lending
- Recovery rate modeling and loss given default
- Repo markets and securities lending
- Risk factor decomposition and sensitivity analysis
- Risk parity and risk budgeting strategies
- Risk transfer mechanism
- Shadow banking and non-bank intermediation
- Smart beta and alternative indexing approaches
- Spot market transactions
- Spot rates, forward rates, and discount factor curves
- Stochastic volatility in interest rate markets
- Stress testing and scenario analysis frameworks
- Subprime mortgage crisis and structured finance risks
- Swaptions and interest rate option pricing
- Swaptions and option volatility surfaces
- Synthetic CDOs and credit-linked note structures
- Terminal value modeling and exit multiples
- 'The Greeks: Delta, Gamma, Vega, Theta, and Rho sensitivity analysis'
- Time of delivery
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
- Zero-coupon bond pricing and bootstrapping
enhanced: true
enhancement_date: '2025-11-06'
enhancement_id: batch04-732376
---




# 1.3 TRANSACTIONAL STRUCTURE OF FINANCIAL MARKETS  

Most people think of financial markets as a giant bazaar with individuals buying and selling stuff to each other for money. The "stuff"' they trade is paper claims on future earnings, coupon interest, or insurance payouts. If you buy good claims and their value goes up, you can sell them for more; if you buy bad ones and their value goes down, you lose money.  

Finance and economics professionals usually offer a seemingly more complete descrip-. tion of this process, adding detail about who buys and sells what and why in each market.. They may educate us that businesses and governments need funds. They issue stock, lease-. and asset-backed bonds, unsecured debentures, sell short-term commercial paper, or rely on. bank loans. These issuers get their required capital and, in exchange, promise to pay inter-. est payments or dividends in the future. The legal claims on business assets are purchased by investors, both individual and institutional, who spend cash today to get more cash to-. morrow, i.e. they invest. Investors can leverage themselves by borrowing cash to buy more securities, and through that they themselves become issuers or users of broker margin or. bank loans.  

While this bazaar description of the financial transactions appears to be very comprehensive, it is actually an incomplete one-dimensional portrait of a multidimensional object. The missing dimension is the time of delivery.  

The standard view focuses exclusively on spot markets where investors purchase securities and pay for them at the time of the purchase. To manage risk they diversify or hedge by holding shorts against longs. Most are investors (read: speculators) hoping to buy low and sell high. This misses the point of the risk-sharing discussion that many participants enter financial markets not to speculate/invest, but to transfer risk - and spot transactions may not be the best way to accomplish that.  

Let us introduce the time of delivery into the picture. Let us relax the assumption that all trades of securities for cash are immediate. An equity investor may agree today to buy a stock for a certain price, but to deliver cash and receive the stock 1 year from today. The investor. is entering into a forward buy transaction. His risk profile is drastically different from that of a spot buyer. He is exposed to the value of the stock, but his exposure does not start until. 1 year from now. He does not care if the stock drops in value as long as it recovers by his. delivery date. He also does not benefit from a temporary appreciation of the stock compared to the spot buyer who could sell the stock immediately. In our time-state risk rectangle with time and stock price on the axes, the forward buy looks like a spot buy, but with a subplane demarcated by today and 1 year from today taken out. Ignoring the time value of money, in Figure 1.1 the area above the forward price line corresponds to a gain, and the area below it. to a loss. A forward sell would cover the same subplane, but the "good"' and the "bad"' areas. would be reversed.  

In the bazaar of finance, agents buy and sell spot, and they buy and sell forward. The forward is an important speculative and risk transfer.md) tool. For our discussion, it does not matter if, at the future delivery time, an actual exchange of securities for cash takes place, or just a. marked-to-market settlement in cash (see Chapter 3). If the stock is trading at. $\in75$ in the spot market, it is economically irrelevant whether the parties to a. $\yen60$ forward transaction exchange cash $(\overleftarrow{\overleftarrow{\mathrm{~60}}})$ for stock (share worth $\in75$ ) or simply settle the difference of $\notin15$ . Also, for most purposes, futures contracts can be treated as identical to forwards, even though they involve a daily settlement through a margin account. Forwards and futures attract speculators and hedgers. They first use their information to bet on the direction of the price in order to profit or risk share; the latter use their skill to arbitrage the mispricing between spot and forward transactions in the same asset.  

Let us now further complicate the view of the markets by introducing the concept of contingent delivery time. An exchange of a security for cash, agreed upon today, is not only delayed into the future but is also made contingent upon a future event or condition. The simplest example is an insurance contract. The payment on a. $\$1,000,000$ life insurance policy takes place only upon the death of the insured person. The benefit is agreed upon and fixed up front between the policyholder and the issuing company. Hazard insurance (fire, auto, flood) is different from life in that the amount of the benefit depends on the "size"' of the future event. The greater the damage, the greater the payment. An option contract is similar to a hazard insurance policy. The option payout depends on the value of the underlying financial variable in the future (see Chapters 5 and 6). A put option on the S&P 100 stock index pays the difference between the selected strike price and the value of the index at some future date times $\$100$ , but only if the index goes down below that strike price level. The buyer insures against the index going down; the more the index goes down the more benefit he obtains from the put. A cap on an interest rate index provides the holder with a periodic payment every time the underlying interest rate goes above a certain level. A borrower may use a cap to protect against interest rate hikes.  

Options involve risk sharing, not only when buying protection, but also when selling protection. A borrower relying on revolving credit with a floating interest rate defined as spread over 3-month LIBOR can sell a floor to offset the cost of the borrowing. When the index rate goes down, he makes payments to the floor buyer. He willingly accepts that risk. because when rates go down and he makes the floor payments, the interest he pays on the revolving loan also declines. In effect, the floor fixes the minimum borrowing rate in exchange. for an up-front premium.  

Options are not the only forms of contingent claims traded in today's markets. In fact, the contingent delivery feature, often referred to as "optionality, is quite common. Buyers of. convertible bonds exchange their bonds for shares when interest rates and/or stock prices are high, making the post-conversion equity value higher than the present value of the remaining interest on the unconverted bond. Issuers call outstanding callable bonds when interest rates decline below a level at which the value of those bonds is higher than the call price. Adjustable mortgages typically contain periodic caps which prevent the interest rate, and thus the monthly payment charged to the homeowner, from changing too rapidly between periods. Many bonds have credit covenants that require the issuing company to maintain certain financial ratios;. non-compliance triggers automatic repayment or default. Car lease agreements give the lessees the right to purchase the automobile at the end of the lease for a prespecified residual value, and lessees exercise those rights when the residual value is sufficiently lower than the market price of the vehicle. In many countries, including the USA, the homeowners with fixed-rate mortgages can prepay their loans partially or fully at any time without penalty. This feature allows the homeowners to refinance their loans with new ones when interest rates drop by a significant enough margin. The cash flows from the original fixed-rate loans are thus contingent upon interest rates staying high. Other examples abound..  

The key to understanding complex securities is to break them down into simpler components:. spot, forward, and contingent delivery. The components may trade separately in the wholesale markets, but are more likely to be bundled together for retail customers or original (primary. market) acquirers. Not uncommonly, they are unbundled and rebundled several times during their lives.  

All financial market evolve to have three structural components: the market for spot. securities, the market for forwards and futures, and the contingent securities market which includes options and other derivatives..  

Most of the activity of the last two forms is reserved for institutions, which is why most people are unaware of them. Yet their dynamic risk-sharing functions are necessary for the. smooth operation of the spot markets. They constantly signal the changing price of risk to. the "bundled" value of the spot securities. In some respects, the spot securities are the most complicated types from the informational content perspective. Their value reflects all available. information about the financial prospects of the broad market and the entity that issued them, and is equal to the sum of the values of all state-contingent claims that can be viewed as. informational units. The value of forwards and option-like contracts is tied to more narrow information subsets. These contracts have expiry dates that are short relative to the underlying. security and are tailored to specific dimensions of risk. They allow the unbundling of the information contained in the spot security. This function is extremely desirable to holders of cash assets as it offers them a way to sell off undesirable risks and acquire desirable ones at. various points in time. If you own a bond issued by a tobacco company, you may be worried. that legal proceedings against the company may adversely affect the credit spread of the bond you hold. You could sell the bond spot and repurchase it forward with the contract date set far into the future. You could purchase an option on the yield spread or a put option on the bond, or sell calls on the bond. All of these activities would allow you to share the risks of the bond with another party and tailor the duration of the risk sharing to your needs..

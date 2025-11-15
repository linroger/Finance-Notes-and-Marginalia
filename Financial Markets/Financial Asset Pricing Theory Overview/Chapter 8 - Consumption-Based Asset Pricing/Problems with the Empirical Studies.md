---
tags:
- apt
- artificial-intelligence
- asset_pricing
- bond-pricing
- consumption_based_model
- credit
- credit-derivatives
- empirical_studies
- equity-derivatives
- factor-models
- fixed-income
- fixed-income-derivatives
- interest-rate-swap
- irs
- ma
- mpt
- options
- repo
- repurchase-agreements
- risk-management
- sifi
- stock_returns
- survivorship_bias
- transaction-costs
- value-at-risk
- var
aliases:
- Empirical Study Issues
- Problems in Empirical Research
key_concepts:
- Agricultural futures and seasonality
- Alternative investments and hedge fund strategies
- Arbitrage Pricing Theory (APT) and factor models
- Arbitrage pricing theory (APT)
- Asset swaps and spread-lock strategies
- Bank stress testing and CCAR requirements
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
- Capital Asset Pricing Model (CAPM) and beta estimation
- Central clearing and CCP risk management
- Commodity futures and convenience yields
- Commodity swaps and energy derivatives
- Corporate bond pricing and credit spread decomposition
- Crack spreads in energy markets
- Credit default swaps and credit protection mechanisms
- Credit risk assessment and loan pricing
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
- Ex-ante expectations vs realized
- Excess stock return estimate
- Exotic derivatives and path-dependent options
- Expected Shortfall (ES) and coherent risk measures
- Extreme value theory and tail risk modeling
- FX futures and currency hedging
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
- Key rate duration and curve risk decomposition
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
- Poor quality consumption data
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
- Stationarity assumption issues
- Stochastic volatility in interest rate markets
- Stress testing and scenario analysis frameworks
- Survivorship bias in returns
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
enhanced: true
enhancement_date: '2025-11-06'
enhancement_id: batch04-381695
---




# 8.6 Problems with the empirical studies  

A number of issues should be taken into account when the conclusions of the empirical studies of the consumption-based model are evaluated. In the following we discuss some selected issues.  

Firstly, the 8% estimate of the average excess stock return is relatively imprecise. With 50 observations (one per year) and a standard deviation of 20%, the standard error equals $20\%/\sqrt{50}\approx$ 2.8% so that a $95\%$ confidence interval is roughly [2.5 $\%$ , 13.5%]. With a mean return of $2.5\%$ instead of $8.0\%$ , the required value of the relative risk aversion drops to 31.25, which is certainly still very high but nevertheless considerably smaller than the original value of 100.  

Secondly, the consumption data used in the tests is of a poor quality as pointed out by e.g.  

Breeden, Gibbons, and Litzenberger (1989). The available data on aggregate consumption measures the expenses for purchases of consumption goods over a given period (usually a quarter or a month). This is problematic for several reasons. Many, especially very expensive, consumption. goods are durable goods offering consumption "services" beyond the period of purchase. The model addresses the rate of consumption at a given point in time rather than the sum of consumption rates over some time interval; see Grossman, Melino, and Shiller (1987). The consumption data. is reported infrequently relative to financial data. Moreover, the aggregate consumption numbers are undoubtedly subject to various sampling and measurement errors; see Wilcox (1992). These problems motivate the development of asset pricing models that do not depend on consumption at all. This is for example the case of the so-called factor models discussed in Chapter 9.  

Thirdly, also data for stock returns has to be selected and applied with caution. Most tests of the asset pricing models are based on data from the U.S. or other economies that have experienced relatively high growth at least throughout the last 50 years. Probably investors in these countries were not so sure 50 years ago that the economy would avoid major financial and political crises and outperform other countries. Brown, Goetzmann, and Ross (1995) point out that due to this survivorship bias the realized stock returns overstate the ex-ante expected rate of returns significantly by maybe as much as 2-4 percentage points. Note however that in many crises in which stocks do badly, also bonds and deposits tend to provide low returns so it is not clear how big the effect on the expected excess stock return is.  

Fourthly, the pricing relations of the model involve the ex-ante expectations of individuals, while the tests of the model are based on a single realized sequence of market prices and consumption. Estimating and testing a model involving ex-ante expectations and other moments requires stationarity in data in the sense that it must be assumed that each of the annual observations is drawn from the same probability distribution. For example, the average of the observed annual. stock market returns is only a reasonable estimate of the ex-ante expected annual stock market return if the stock market return in each of the 50 years is drawn from the same probability distribution. Some important changes in the investment environment over the past years invalidate the stationarity assumption. For example, Mehra and Prescott (2003) note two significant changes in the U.S. tax system in the period between 1960 and 2000, a period included in most tests of the consumption-based model:  

: The marginal tax rate for stock dividends has dropped from 43% to 17%. Stock returns in most pension savings accounts are now tax-exempt, which was not so in the 1960s. Bond returns in savings accounts have been tax-exempt throughout the period..  

Both changes have led to increased demands for stocks with stock price increases as a result. These changes in the tax rules were hardly predicted by investors and, hence, they can partly explain why the model has problems explaining the high realized stock returns. Similarly, it can be argued that the reductions in direct and indirect transaction costs and the liberalizations of international financial markets experienced over the last decades have increased the demands for stocks and driven up stock returns above what could be expected ex-ante. The high transaction costs and restrictions on particularly international investments in the past may have made it impossible or at least very expensive for investors to obtain the optimal diversification of their investments so that even unsystematic risks may have been priced with higher required returns as a consequence.1  

One can also argue theoretically that the returns of a given stock cannot be stationary. Here is the argument: in each period there is a probability that the issuing firm defaults and the stock stops to exist. Then it no longer makes sense to talk about the return probability distribution of that stock. More generally, the probability distribution of the return in one period may very well depend on the returns in previous periods.  

Fifthly, as emphasized by Bossaerts (2002), standard tests assume that ex-ante expectations of individuals are correct in the sense that they are confirmed by realizations. The general asset pricing theory does allow individuals to have systematically over-optimistic or over-pessimistic expectations. The usual tests implicitly assume that market data can be seen as realizations of the ex-ante expectations of individuals. Bossaerts (2002) describes studies which indicate that this assumption is not necessarily valid.

---
academic_level: graduate
aliases:
- Leverage Impact
- Leverage Risk
- Risk Measure
- Risk-Based Leverage
cssclasses: academia
enhanced: true
enhancement_date: '2025-11-06'
enhancement_id: batch09-000101
key_concepts:
- Black-Scholes option pricing model and continuous-time finance
- Implied volatility calculation and volatility surface analysis
- Options Greeks and sensitivity analysis for risk management
- Duration analysis and interest rate risk management
- Convexity adjustments and yield curve sensitivity
- Capital Asset Pricing Model (CAPM) and expected returns
- Value at Risk (VaR) and tail risk measurement
- Basel accords and banking regulation framework
- Arbitrage opportunities and no-arbitrage pricing
- Alpha generation and active portfolio management
- Beta estimation and systematic risk measurement
- Factor models and multi-factor pricing
- Volatility modeling and estimation techniques
- Correlation analysis and dependency structures
- Beta estimation and systematic risk measurement
- Alpha generation and active return measurement
- Risk preference theory and utility functions
- Sensitivity analysis and Greeks calculation
- Duration and Convexity in Fixed Income Risk Management
- Auto-Callable Notes and Barrier Options
- Yield Curve Analysis and Bond Valuation
- Value at Risk and Expected Shortfall
- Vasicek Interest Rate Model and Mean Reversion
- Short Rate Models and Term Structure Dynamics
- Variance Reduction Techniques in Monte Carlo Methods
- Capital Asset Pricing Model and Beta Analysis
- Distressed Debt Strategies and Recovery Analysis
- Credit Risk Management and Default Probability
- Expected Loss and Loss Given Default Models
- Forward Rates and Curve Construction Methods
- Swap Market Mechanisms and Pricing
- Equity-Linked Notes and Market-Linked Securities
- Delta, Gamma, and Vega Hedging Techniques
- 'Greeks: Delta, Gamma, Theta, and Vega Hedging'
- Ornstein-Uhlenbeck Process in Finance
- Distressed Investing and Debt Restructuring
- Cost of Equity and Expected Returns
- Stochastic Integration and Path-Dependent Options
- Forward Curves and Roll Strategies
- Chapter 11 Bankruptcy and Creditor Negotiations
- Security Market Line and Risk-Return Tradeoff
- Options Trading Strategies and Risk Management
- Structured Products and Principal Protection
- Stress Testing and Extreme Value Analysis
- Credit Default Swaps and Credit Risk Transfer
- Fama-French Factors and Style Analysis
- Risk Measurement and VaR Backtesting
- Contango, Backwardation, and Roll Yield
- Futures and Forward Contracts in Financial Markets
- Bond Pricing and Yield to Maturity Analysis
- Fixed Income Securities and Credit Quality
- Factor Models and Asset Pricing
- Hedge Strategies and Basis Risk Management
- Bond Portfolio Immunization Strategies
- Dynamic vs Static Hedging in Practice
- Interest Rate Swaps and Currency Swap Structures
- Term Structure of Interest Rates and Yield Curves
- Seasonality and Convenience Yield
- Commodity Markets and Energy Derivatives
- Option Valuation and Exercise Strategies
- Credit Spreads and Rating Migration Analysis
- Interest Rate Risk and DV01 Calculations
- Hedging Strategies and Risk Mitigation
- Monte Carlo Simulation Methods for Derivative Pricing
- Government and Corporate Bond Markets
- Arbitrage Pricing Theory and Multi-Factor Models
professional_application: theoreti
status: active
tags:
- arbitrage-opportunity
- arbitrage-pricing
- asset-allocation
- banking-regulation
- basel-accord
- basis-point-value
- beta-estimation
- binomial-model
- black-scholes-model
- capital-adequacy
- capital-asset-pricing
- capital-budgeting
- caplet
- continuous-time-pricing
- convexity-adjustment
- control-variates
- exotic-options
- hull-white
- call-options
- cir-model
- butterfly-spreads
- expected-shortfall
- straddles
- extreme-value-theory
- book-to-market
- exchange-offers
- backwardation
- volatility-analysis
- energy-derivatives
- style-analysis
- bond-pricing
- option-strategies
- cramdown
- corporate-bonds
- yield-curve
- unexpected-loss
- capital-asset-pricing-model
- clearinghouse
- debt-restructuring
- interpolation
- overnight-indexed-swaps
- interest-rate-risk
- arbitrage-pricing-theory
- monte-carlo-simulation
- hedge-ratio
- market-price-of-risk
- loss-given-default
- roll-strategies
- value-factor
- vasicek-model
- sharpe-ratio
- dirty-price
- forward-curves
- distressed-investing
- dynamic-hedging
- monte-carlo-var
- options-trading
- coupon-bonds
- commodity-trading
- forward-contracts
- yield-to-maturity
- forward-rates
- fama-french
- recovery-rate
- zero-coupon-bonds
- parametric-var
- lognormal-models
- var-methodologies
- historical-var
- mean-reversion
- contango
- vega-hedging
- random-walks
- modified-duration
- expected-loss
- delta-hedging
- quantitative-finance
- forward-curve
- currency-swaps
- market-linked-notes
- systematic-risk
- protective-puts
- government-bonds
- alpha
- security-market-line
- probabilty-of-default
- curve-steepening
- reverse-convertibles
- curve-fitting
- credit-default-swaps
- gamma-hedging
- hedge-effectiveness
- idiosyncratic-risk
- storage-costs
- roll-yield
- beta
- risk-premium
- spot-rates
- put-options
- affine-term-structure
- capm
- momentum
- curve-flattening
- basis-risk
- market-risk-premium
- convexity
- hedge-strategies
- antithetic-variates
- term-structure
- covered-calls
- swap-rate
- sofr
- ' exposure-at-default'
- chapter-11-bankruptcy
- stress-testing
- roll-over-risk
- mathematical-finance
- ornstein-uhlenbeck
- rating-migration
- par-yield
- investment-analysis
- portfolio-optimization
- duration-analysis
- path-dependency
- value-at-risk
- metals-trading
- blocker-strategy
- factor-models
- convenience-yield
- creditor-committees
- agricultural-commodities
- barbell-strategy
- risk-management
- convergence
- var-backtesting
- variance-reduction
- stochastic-integration
- barrier-options
- tender-offers
- cross-hedging
- seasonality
- ' DIP-financing'
- clean-price
- yield-curve-shocks
- principal-protected-notes
- strangles
- conditional-var
- equity-linked-notes
- fixed-income
- dv01
- short-rate-models
- least-squares-mc
- swap-spread
- efficient-frontier
- price-yield-relationship
- credit-migration
- default-probability
- marking-to-market
- auto-callables
- total-return-swaps
- libor
- credit-spreads
- multi-factor-models
- structured-notes
- iron-condors
- financial-markets
- macaulay-duration
- static-hedging
- size-effect
- basis-swaps
- knock-out-options
- interest-rate-swaps
- futures-contracts
- quasi-monte-carlo
- apt
- bootstrap-method
- current-yield
title: Leverage as a Measure of Risk
type: note
---
--



# Leverage as a Measure of Risk

## Summary

Leverage is treated as a measure of risk factor sensitivity. It can be computed using the "equivalent security" approach to determine "bucketized risk".

## 1. Justification

The unfolding financial crisis has brought the issue of leverage into the limelight. "Over leveraging" is often blamed for the demise of structured finance yet the issue is often viewed from the traditional, purely accounting standpoint. This technical note expands the concept of leverage to derivative products and provides a tool for assessing its impact when the "traditional" approach does not work. The intended audience is non-technical practitioners interested in controlling portfolio risks associated with leverage.

## 2. Accounting and Risk-Based Leverage

Accounting leverage can be defined as:
$$
\begin{array}{r c l}
L &=& \frac{\text{assets}}{\operatorname*{max}\left\{\text{equity}, 0\right\}} = \frac{\text{assets}}{\operatorname*{max}\left\{\text{assets} - \text{liabilities}, 0\right\}}\;.
\end{array}
$$

It follows from Eq. (1) that as the value of liabilities approaches that of assets, the leverage of the portfolio grows infinitely. This is not an unduly restrictive assumption for traditional portfolios since in this case the liquidation of the portfolio (e.g., due to bankruptcy) is a rational consequence.

Let us illustrate this with an example.

### Example 1

Suppose that you bought a house last year for $500,000 with $50,000 as a down payment. Considering this house as a self-contained real estate portfolio, its assets last year were $500,000, its equity portion (total assets less liabilities) was $50,000, so its accounting leverage was:
$$
\frac{\$500,000}{\$50,000} = 10.
$$

If the value of your house this year grows by 10% to $550,000, your equity increases by 100% to $100,000. If your house value drops to $450,000, your equity decreases by 100% (disappears).

In this example, a 10% return on assets (ROA):
$$
\text{ROA} = \frac{\$50,000}{\$500,000} = 10\%
$$

Results in a 100% return on equity (ROE), and a -10% ROA:
$$
\text{ROA} = \frac{-\$50,000}{\$500,000} = -10\%
$$

Yields a -100% ROE. From (1),
$$
L(t_{0}) = \frac{\text{assets}(t_{0})}{\text{equity}(t_{0})} = \frac{\frac{\text{P\&L}(t_{0}, t_{1})}{\text{equity}(t_{0})}}{\frac{\text{P\&L}(t_{0}, t_{1})}{\text{assets}(t_{0})}} = \frac{\frac{\text{change in equity}(t_{0}, t_{1})}{\text{equity}(t_{0})}}{\frac{\text{change in assets}(t_{0}, t_{1})}{\text{assets}(t_{0})}} = \frac{\text{ROE}}{\text{ROA}}\;,
$$

which gives us an alternative definition of leverage. Note here that this definition only makes sense under the **going concern** assumptions, i.e., in situations where the portfolio has sufficient equity to prevent liquidation. In fact, if your house value increases to $550,000 (and your debt doesn't change), your leverage falls to:
$$
\frac{\$550,000}{\$550,000 - \$450,000} = 5.5.
$$

If your house value decreases to $450,000 (or less) — under the same assumptions, your leverage becomes infinite:
$$
\frac{\$450,000}{\$450,000 - \$450,000} = \infty,
$$

And (2) becomes meaningless.

### Example 2

Suppose you bought a $\mathcal{B}$-month European call option struck at $80 on a stock currently trading at $75. Here the underlying stock plays the role of an asset and the call itself plays the role of equity. Assuming:

- (annualized) implied volatility of 20%,
- Simple 3-month risk-free rate at 0.1%,

The price of this call is $1.22 and its delta is $\Delta = 0.28$.

Accounting leverage as defined by (1) is equal to 1, since you bought the option with your own money. Risk-based leverage defined by (2), however, is:
$$
L(t_{0}) = \frac{\text{change in equity}(t_{0}, t_{1})}{\text{equity}} = \frac{\text{change in assets}(t_{0}, t_{1})}{\text{assets}} = \Delta \frac{\text{assets}}{\text{equity}} = 0.28 \times \frac{75}{1.22} = 17\;,
$$

Which makes sense: a 
$$
\frac{\$2}{\$75} = 2.7\%
$$

Change in the (underlying) asset price leads to a 
$$
\frac{\$0.55}{\$1.22} = 45\%
$$

Change in equity, and the ratio of the second to the first is 17. Clearly, any reference to "borrowed money" is irrelevant in this case.

**Summarizing:**

- Accounting leverage is irrelevant to derivative securities as a measure of risk;
- Risk-based leverage captures risk better than accounting leverage;
- Risk-based leverage yields the same result as accounting leverage for "traditional" assets;
- Risk-based leverage is a dynamic measure, i.e., it requires that asset and equity P&L be known, whereas accounting leverage is a static measure not requiring such knowledge.

## 3. Application of Risk-Based Leverage to Portfolio Management

As follows from Section 2, risk-based leverage, and not accounting leverage, is an appropriate measure for a portfolio that includes derivative products (futures, swaps, options, and other exotics). In this case, "equity" is the current portfolio net asset value (NAV). It is unclear, however, how "assets" can be defined in the case of a complex portfolio. A case can be made for the following algorithm:

- **Select an easy-to-analyze "equivalent (non-derivative) security"** from some intuitive considerations, e.g., a bond with the same duration as the portfolio or a 10-year Treasury note;

- **Calculate DV01 of the equivalent security per $1 notional:**
  $$
  DV01_{\text{equiv. sec.}} = \frac{PV_{\$1}(\text{curve}_{\text{up}_{10\text{b.p.}}}) - PV_{\$1}(\text{curve}_{\text{down}_{10\text{b.p.}}})}{20}
  $$

- **Find a "perfect hedge" for the portfolio in terms of the equivalent security**, i.e., find the notional amount of this security that has the same DV01 as our portfolio, i.e.,
  $$
  N_{\text{equiv. sec}} = \frac{DV01_{\text{port}}}{DV01_{\text{equiv. sec.}}}
  $$

- **The amount of assets required for (2)** is equal to the notional amount found above.

### Example 3

Suppose that portfolio DV01 is 
$$
DV01_{\text{port}} = \$50,000
$$

which is calculated by moving the interest rate curve (assuming that we are only concerned with one currency) up and down by 10 b.p. Suppose further that DV01 of a 10-year Treasury note is 
$$
DV01_{TY(\$1)} = \$0.001
$$

Per $1 notional. Then the equivalent assets will be:
$$
\frac{DV01_{\text{port}}}{DV01_{TY(\$1)}} = \frac{50,000}{0.001} = \$50,000,000.
$$

If the current value of the portfolio is $50,000,000, then equivalent risk-based leverage is:
$$
\frac{\$50,000,000}{\$50,000,000} = 1.
$$

Clearly, any number of equivalent assets can be used to calculate portfolio leverage in the general case. One could expand the definition in (2) to include leverage with respect to a collection of "base assets", e.g., 2, 3, 5, 10, and 30-year (on-the-run) Treasury notes. If it is possible to construct a unique portfolio decomposition as presented by 4–5, one can perform "sensitivity analysis" with respect to each equivalent security separately. Such analysis would capture "bucketized risk", i.e., exposure to different parts of the interest rate curve. Using an equivalent asset approach yields a more comprehensive picture of the overall portfolio risk compared to the one painted by accounting leverage.

## Appendix A: Calculation of Option Price and $\Delta$ in Example 1

The Black-Scholes equation for the call price yields:
$$
\begin{array}{r c l}
c &=& S N(d_{1}) - K e^{-r T} N(d_{2})\;, \\
d_{1} &=& \displaystyle\frac{\ln\left(\frac{S}{K}\right) + \left(r + \frac{\sigma^{2}}{2}\right) T}{\sigma \sqrt{T}}\;, \\
d_{2} &=& d_{1} - \sigma \sqrt{T}\;, \\
N(x) &=& \displaystyle\frac{1}{\sqrt{2\pi}} \int_{-\infty}^{x} e^{-\frac{y^{2}}{2}} dy\;.
\end{array}
$$

### Where

- $c$ - call price,
- $S$ - spot price of the underlying stock = $75,
- $N$ - cumulative distribution function of the standard normal distribution,
- $K$ - call strike = $80,
- $r$ - simple 3-month risk-free rate = 0.1% = 0.001,
- $T$ - time to option expiry in years = 0.25,
- $\sigma$ - volatility of the price of the underlying stock = 20% = 0.2.

Differentiating (A.1) - (A.4) with respect to $S$, we obtain:
$$
\frac{\partial c}{\partial S} = \Delta = N(d_{1}).
$$

Substituting the numbers from Example 1 into (A.1) - (A.4), we obtain $c = 1.22$ and $\Delta = 0.28$.

## Appendix B: Derivation of the Implied Correlation Coefficient

Consider two par swap rates effective at time $t$: $r (t, t+\tau)$ and $r (t, t+T)$, where $\tau$ and $T$ are time intervals such that $0 < \tau \leq T$. The present values of the fixed legs of the respective swaps with unit notionals are:
$$
\begin{array}{r c l}
S(t, t+\tau) &=& r(t, t+\tau) \Delta t \displaystyle\sum_{i=1}^{m} d F(t_{i}) = \alpha^{*} r(t, t+\tau)\;, \\
S(t, t+T) &=& r(t, t+T) \Delta t \displaystyle\sum_{i=1}^{n} d F(t_{i}) = \beta^{*} r(t, t+T)\;, \\
m &=& \displaystyle\frac{\tau}{\Delta t}\;, \\
n &=& \displaystyle\frac{T}{\Delta t}\;, \\
\alpha^{*} &=& \Delta t \displaystyle\sum_{i=1}^{m} d F(t, t_{i})\;, \\
\beta^{*} &=& \Delta t \displaystyle\sum_{i=1}^{n} d F(t, t_{i})\;.
\end{array}
$$

### Table 2: LIBOR Quotes
!Table 2: LIBOR Quotes

### Table 3: Future Quotes
!Table 3: Future Quotes

### Table 4: Swap Quotes
!Table 4: Swap Quotes

From (B.1) - (B.6), the PV of a forward swap effective between $t+\tau$ and $t+T$ as seen at $t$ is:
$$
\begin{array}{r c l}
S(t+\tau, t+T) &=& r(t+\tau, t+T) \Delta t \displaystyle\sum_{i=m+1}^{n} d F(t, t_{i}) = \gamma^{*} r(t+\tau, t+T) \\
&=& S(t, t+T) - S(t, t+\tau)\;, \\
\gamma^{*} &=& \Delta t \displaystyle\sum_{i=m+1}^{n} d F(t, t_{i}) = \beta^{*} - \alpha^{*}\;.
\end{array}
$$

The implied forward rate defined by (B.1) and (B.2) satisfies:
$$
r(t+\tau, t+T) = \alpha r(t, t+T) + \beta r(t, t+\tau)\;,
$$

Where:
$$
\alpha = \frac{\beta^{*}}{\gamma^{*}}\;, \quad \beta = \frac{-\alpha^{*}}{\gamma^{*}} = 1 - \alpha\;.
$$

For the corresponding interest rate volatilities, we have:
$$
\sigma_{t+\tau, t+T}^{2} = \alpha^{2} \sigma_{t, T_{\text{short}}}^{2} + \beta^{2} \sigma_{t, T_{\text{long}}}^{2} + 2 \alpha \beta \sigma_{t, T_{\text{short}}} \sigma_{t, T_{\text{long}}} \rho_{t; \tau, T}\;,
$$

Where $\sigma_{t_{1}+\delta t, t_{2}}$ is the implied forward swaption volatility at time $t_{1}$ of forward interest rate effective between $t_{1}+\delta t$ and $t_{2}$. The respective correlation coefficient is:
$$
\rho_{t; \tau, T} = \frac{\sigma_{t+\tau, t+T}^{2} - \alpha^{2} \sigma_{t, T_{\text{short}}}^{2} - \beta^{2} \sigma_{t, T_{\text{long}}}^{2}}{2 \alpha \beta \sigma_{t, T_{\text{short}}} \sigma_{t, T_{\text{long}}}}\;.
$$

### Table 5: ATM Implied Swaption Volatilities
!Table 5: ATM Implied Swaption Volatilities

## References

[^1]: D. Goldman. *Seeing is not believing: Fund of funds and hedge fund risk assessment and transparency, survival and leverage*. Working paper, Measurisk TM, 2003.
[^2]: J. Hull. *Options, Futures and Other Derivatives*. Prentice Hall, 6th edition, 2006.
[^3]: F. Fabozzi. *The Handbook of Fixed Income Securities*. McGraw-Hill, 7th edition, 2005.
[^4]: W. Feller. *An Introduction to Probability Theory and Its Applications*, Volume 1. John Wiley & Sons, 3rd edition, 1968.
[^5]: P. Glasserman. *Monte Carlo Methods in Financial Engineering* (Stochastic Modelling and Applied Probability). Springer-Verlag, New York, 2004.
[^6]: M. Matsumoto and T. Nishimura. *Mersenne Twister: A 623-dimensionally equidistributed uniform pseudorandom number generator*. *ACM Transactions on Modeling and Computer Simulation*, 8 (1):3–30, January 1998. http://www.math.sci.hiroshima-u.ac.jp/~m-mat/MT/ARTICLES/mt.pdf.
[^7]: P. Miron and P. Swannell. *Pricing and Hedging Swaps*. Euromoney Books, 1991.

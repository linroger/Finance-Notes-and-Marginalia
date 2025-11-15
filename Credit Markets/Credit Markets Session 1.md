---
title: Credit Markets Session 1
tags:
- black-scholes
- bond
- bond_pricing
- call
- capital-structure
- cds
- convexity
- corporate-bond
- credit-derivatives
- credit-risk
- credit-spread
- credit_instruments
- credit_markets
- credit_trading
- currency
- default_risk
- duration
- dv01
- equity
- equity-value
- etf
- fixed-income
- fixed_income
- future
- g-spread
- greeks
- hedge-fund
- index
- interest-rate
- limit-order
- liquidity
- option
- order-book
- put
- sofr
- swap
- treasury
- yield-curve
- z-spread
aliases:
- Credit Default Risk
- Credit Markets
- Credit Trading
- Credit Instruments
key_concepts:
- ' tranche valuation'
- Basis swap mechanics
- CDO squared structures
- CDS curve construction
- CDS spread calibration
- Convexity adjustment
- Credit Default Swaps
- Credit index products
- Cross-currency basis
- Currency swap structure
- DV01 calculation
- Default correlation
- Delta risk management
- Derivative securities
- Duration measurement
- Dynamic hedging strategies
- Financial risk management
- Fixed vs floating leg
- Gamma effects on options
- Hedging with bonds
- Interest rate sensitivity
- Interest rate swap pricing
- Modified duration calculation
- Options Greeks measurement
- Portfolio immunization
- Portfolio optimization
- Portfolio risk hedging
- Present value of swaps
- Price-yield relationship
- Quantitative financial analysis
- Rho interest rate sensitivity
- Risk assessment and mitigation
- Swap curve construction
- Swaption valuation
- Synthetic CDO pricing
- Theta time decay
- Vega volatility sensitivity
- bond cash flows
- credit default swaps
- credit market segments
- credit spreads
- default risk valuation
- duration and convexity
- instrument types
- seniority ranks
- yield calculations
---

# Credit Markets Session 1
- Course objective: introduce basic concepts on pricing, trading and portfolio risk management for credit instruments. Discuss credit market segments, seniority ranks, instrument types & specs, quoting conventions, execution venues and trading protocols
- Understand the valuation of an instrument with default risk
- Focus on:
   - Corporate Bonds and loans
   - Foreign sovereign bonds
   - Fixed income ETFs
   - Credit Default Swaps (CDS) and
   - CDS Indices
- Good insight into the daily activity of a credit trading desk
# What is Credit Default Risk?
!500

# When Does a Company Default?
- Issuer default triggered by non-payment of contractual obligation!
- Usually, caused by missed coupon or principal payment
- In default, coupon payments are stopped and all liabilities becomes due
- Assets are liquidated and used to pay the debt holders, based on seniority rank in the capital structure
- Technical/Non-financial default: can lead to accelerated debt repayment and financial default
- See appendix on "structural" vs "reduced form" credit risk modeling approaches
# Credit Market Segments
- Investment Grade
   - low risk of default
- Speculative Grade / High Yield
   - higher risk of default
- Role of credit rating agencies in assessing issuer default risk
!500

# Instrument Types & Contractual Specs: Corporate Bonds
- Issuer name
- Issue currency, price and amount
- Issue maturity
- Seniority rank in capital structure
- Coupon payment type: fixed rate, floating rate (+ reset index), variable rate, etc
- Coupon frequency & day count convention: semi-annual, 30/360, etc
- Call/Put schedules / embedded optionality: right to exercise call/put options $\$a_t$$ pre-specified prices
- Covenants (positive vs negative, mostly high yield)
!500

# Instrument Types & Contractual Specs Fixed Rate IG Bond Example: Oracle
!500

# Fixed Rate Bond Cash-Flows
!500

# Floating Rate Bond (SOFR Ref Index): Morgan Stanley
!500

# Floating Rate Bond Cash-Flows
!500

## Fixed Rate HY Bond Example: AMC
!500

## Foreign Sovereign Bond Example: Mexico
!500

# Floating Rate Loan Example (First Lien): United Airlines
!500

# Floating Rate Loan Cash-Flows
!500

# Preferred Perpetual Example: Morgan Stanley
!500

# Market Participants: Mostly Institutional Players
- Commercial and investment banks
- Pension funds
- Insurance companies
- Mutual funds
- Various asset managers / ETF issuers
- Hedge funds
- Sovereign funds
- Retail Clients: mostly via ETFs
# Quoting Conventions
- Yield: for Investment Grade bonds with maturity < 1 year
- Spread (to Treasury Benchmark Yield): for Investment Grade bonds with maturity > 1 year
- Clean price: for High Yield bonds
- Bonds are fungible and uniquely identified via ISIN/CUSIP codes (market convention), SEDOL codes, FIGI codes, etc.
# Size of the US Corporate Bond Market
- USD denominated Corporate Bonds
- ~100K bonds total ~10K liquid
- Outstanding notional value: ~ 10T USD
- Average daily volume: ~ 40B USD
- Trades sizes smaller than $100,000 are viewed as "odd lots".$
# SIFMA: Fixed Income Outstanding and New Issues (2023) IG Bonds Liquidity
!500

# Hedging and Related Instruments
- US treasuries
- US treasury futures
- Credit Default Swaps
- CDX credit indices
- Fixed income ETFs
!500

# Trading
- ~70% over-the-counter (with broker-dealers)
- ~30% on electronic trading venues
- Trading volume moving gradually from OTC to electronic venues
- US Bond trades reported to FINRA TRACE facility (up to 15 mins delayed)
# Transition from OTC to Electronic Trading Venues
## Market Structure: OTC/Bilateral with Broker-Dealers (70%)
- Brokers provide markets to clients, e.g. via MSG1 (principal market maker)
- Brokers also act as agents between buyers and sellers
- Negotiation over the Phone / IB Chat
- Bloomberg VCON confirmation
- Electronic connectivity to broker via API
- Bloomberg FIT, TSOX and BOLT screens
- Single bonds vs Portfolio trading
## Market Structure: Electronic Venues (30%) Order Execution Protocols (via FIX)
- RFQ: "Request For Quote" (auction based) vs LOB: "Limit Order Book" (live trading)
- RFQ venues: MarketAxess (80% of electronic volume), TradeWeb, TrueMid, etc
- LOB venues: ICEBondPoint, TradeWebDirect, TheMuniCenter, MTSBondPro, TrueMid, etc
- Anonymous vs Bilateral trading
- GUI click-trading vs API trading
# Bond Cash-Flow, Prices and Yields
- Fixed-rate bond cash-flows for maturity $T=T_n$:
$\$\{c_i, T_i\}_{i=1..n}, \quad 0\leq t<T_1<...<T_n \tag{1}$$

- Quoting bonds: price to "continuously componded" yield conversion
$\$B_t=B(t, y):=\sum_{i=1}^n c_i\cdot e^{(t-T_i)\cdot y} \tag{2}$$

- Cash-flow weights:
$\$w_i=w_i(t, y):=\frac{c_i\cdot e^{(t-T_i)\cdot y}}{B_t}>0 \tag{3}$$

# Bond Cash-Flow, Prices and Yields Bond Valuation Formulas (0 Accrued, T+0 Settle)
- Bullet fixed-rate bond with semi-annual coupon pct. $c$ and $T$ years to maturity:
$\$B_0=B(0, c, T, y)=\sum_{k=1}^{2T}\frac{c}{2}\cdot e^{-k\cdot\frac{y}{2}}+e^{-T\cdot y} \tag{4}$$

- Simple bond price (using geometric series formula):
$\$\mathcal{B}_{0}=1+\frac{\frac{c}{2}-\left(e^{\frac{y}{2}}-1\right)}{e^{\frac{y}{2}}-1}\cdot\left(1-e^{-T\cdot y}\right) \tag{5}$$

- Bullet fixed-rate bond with semi-annual coupon pct. $c$ and $T$ years to maturity:
$\$B_{0}=B(0, c, T, y)=\sum_{k=1}^{2T}\frac{c}{2}\cdot e^{-k\cdot\frac{y}{2}}+e^{-T\cdot y} \tag{4}$$

- Using "semi-annual yield": $y_{\text{sa}}=2\cdot\left(e^{\frac{y}{2}}-1\right)$
$\$B_0=1+\frac{c-y_{sa}}{y_{sa}}\cdot\left[1-\left(1+\frac{y_{sa}}{2}\right)^{-2T}\right] \tag{6}$$

# Bond Valuation Surface (0 Accrued, T+0 Settle)
!500

!500

# Comments
Bond trading $\$a_t$$ 100% "par" price:
$\$B_{0}=1 \iff c=y_{sa} \iff \left(1+\frac{c}{2}\right)$$

New issue pricing (primary market): pricing "$\$a_t$$ par" ⇐⇒ "semi-annual coupon" = "semi-annual yield"

- When yield > coupon, bond trades below par
- When yield < coupon, bond trades above par
- Bond price is increasing in coupon, decreasing in yield
## Time Sensitivity: Theta/Carry = "Yield"
$\$\frac{\partial B}{\partial t}\left(t, y\right)=\frac{\partial}{\partial t}\left[\sum_{i=1}^{n}c_{i}\cdot e^{\left(t-T_{i}\right)\cdot y}\right]=\sum_{i=1}^{n}c_{i}\cdot\frac{\partial}{\partial t}\left[e^{\left(t-T_{i}\right)\cdot y}\right] \tag{8}$$

$\$=\sum_{i=1}^{n}c_{i}\cdot y\cdot e^{\left(t-T_{i}\right)\cdot y}=y\cdot\left[\sum_{i=1}^{n}c_{i}\cdot e^{\left(t-T_{i}\right)\cdot y}\right]=y\cdot B_{t}$$

$\$B\left(t+\\Delta t, y\right)-B\left(t, y\right) \approx B_{t}\cdot y\cdot\\Delta t \tag{9}$$

## Yield Sensitivity: Duration/D = "Weighted Sum of TTMs"
$\$\frac{\partial B}{\partial y}=\frac{\partial}{\partial y}\left[\sum_{i=1}^{n}c_{i}\cdot e^{(t-T_{i})\cdot y}\right]=\sum_{i=1}^{n}c_{i}\cdot\frac{\partial}{\partial y}\left[e^{(t-T_{i})\cdot y}\right] \tag{10}$$

$\$=\sum_{i=1}^{n}c_{i}\cdot(t-T_{i})\cdot e^{(t-T_{i})\cdot y}=-B_{t}\cdot\sum_{i=1}^{n}(T_{i}-t)\cdot w_{i}=-B_{t}\cdot D$$

$\$B\left(t, y+\\Delta y\right)-B\left(t, y\right) \approx -B_{t}\cdot D\cdot\\Delta y \tag{11}$$

## Yield Convexity: Gamma/Γ = "Weighted Sum of Squared TTMs"
$$\begin{aligned}
\frac{\partial[^2]B}{\partial y[^2]}&=\frac{\partial[^2]}{\partial y[^2]}\left[\sum_{i=1}^n c_i\cdot e^{(t-T_i)\cdot y}\right]=\sum_{i=1}^n c_i\cdot\frac{\partial[^2]}{\partial y[^2]}\left[e^{(t-T_i)\cdot y}\right] \tag{12}\\
&=\sum_{i=1}^n c_i\cdot(T_i-t)[^2]\cdot e^{(t-T_i)\cdot y}=B_t\cdot\sum_{i=1}^n (T_i-t)[^2]\cdot w_i=B_t\cdot\Gamma\\
&B\left(t, y+\Delta y\right)-B\left(t, y\right) \approx B_t\cdot\left[-D\cdot\Delta y+\frac{1}{2}\cdot\Gamma\cdot(\Delta y)[^2]\right] \tag{13}
\end{aligned}$$

## Summary of Sensitivities (Yield Parametrization)
Theta/Carry
$\$\mbox{\Theta}=\frac{\partial B}{\partial t}=y\cdot B_{t} \tag{14}$$

"DV01" (-1bp change in yield) and Duration
$\$DV01=-\frac{\partial B}{\partial y}=B_{t}\cdot D, \quad D=\sum_{i=1}^{n}(T_{i}-t)\cdot w_{i}>0 \tag{15}$$

Convexity (-1bp change in yield) and Gamma
$\$\frac{\partial^{2}B}{\partial y^{2}}=B_{t}\cdot\\Gamma, \quad\\Gamma=\sum_{i=1}^{n}(T_{i}-t)^{2}\cdot w_{i}>0 \tag{16}$$

Simple bond price dynamics
$$\begin{align}
dB_t &= dB(t, $y_t$) = \frac{\partial B}{\partial t} \cdot $\$d_t$$ + \frac{\partial B}{\partial y} \cdot dy_t + \frac{1}{2} \frac{\partial[^2] B}{\partial y[^2]} \cdot \sigma_y[^2] \cdot $$d_t$$ \tag{17} \\
&= y \cdot B_t \cdot $\$d_t$$ - B_t \cdot D \cdot dy_t + \frac{1}{2} \cdot B_t \cdot \\Gamma \cdot \sigma_y[^2] \cdot $$d_t$$ \\
\frac{dB_t}{B_t} &= \left( $y_t$ + \frac{1}{2} \cdot \Gamma \cdot \sigma_y[^2] \right) \cdot $\$d_t$$ - D_t \cdot dy_t \tag{18}
\end{align}$$

## Bond Price Dynamics and Drift Components
Bond Drift Components

$\$\mathbb{E}\left[\frac{dB_t}{B_t}\right]/$$d_t$$ = $y_t$ - D \cdot \mathbb{E}\left[\frac{dy_t}{$$d_t$$}\right] + \frac{1}{2} \cdot \\Gamma \cdot \sigma_y[^2] \tag{19}$$

$\$\text{"yield"} + \text{"yield curve roll down"} + \text{"yield convexity"}$$

!500

# Credit Spreads and Treasury Benchmarks
- "Treasury benchmark" = US treasury bond with same/similar maturity as the corporate bond
- "Spread to benchmark" = corporate bond yield - treasury benchmark yield
- "G-Spread" = corporate bond yield - interpolated treasury yield
- Credit spreads quantify the risk of credit issuer defaulting to bond maturity
- Spread to benchmark = market convention for quoting IG bonds
!500

## Z-Spread Parametrization
- Interest rate curve bootstrapping & risk-free bond valuation
$\$G_t = G(t, r) \coloneqq \sum_{i=1}^{n} c_i \cdot e^{(t-T_i)\cdot r_i} \tag{20}$$

- Bond price to z-spread conversion
$\$B_t = B(t, r, s) \coloneqq \sum_{i=1}^{n} c_i \cdot e^{(t-T_i) \cdot (r_i+s)} \tag{21}$$

- Cash-flow spread weights:
$\$\widetilde{\\omega}_i = \widetilde{\\omega}_i(t, r, s) \coloneqq \frac{c_i \cdot e^{(t-T_i) \cdot (r_i+s)}}{B_t} > 0 \tag{22}$$

## Summary of Bond Sensitivities (Spread Parametrization)
- Theta/Carry
$\$\\Theta = \frac{\partial B}{\partial t} = B_t \cdot \sum_{i=1}^{n} (r_i + s) \cdot \omega_i \approx B_t \cdot y \tag{23}$$

- "CS01" (-1bp change in spread) and Spread Duration $D$
$\$CS01 = -\frac{\partial B}{\partial s} = B_t \cdot D, \quad D = \sum_{i=1}^{n} (T_i - t) \cdot \omega_i > 0 \tag{24}$$

- Spread Convexity (-1bp change in spread) and Gamma $\\Gamma$
$\$\frac{\partial[^2] B}{\partial s[^2]} = B_t \cdot \\Gamma, \quad \\Gamma = \sum_{i=1}^{n} (T_i - t)[^2] \cdot \omega_i > 0 \tag{25}$$

## IR-Hedged Bond Price Dynamics
$\$\frac{dB_t}{B_t} = \left($s_t$ + \frac{1}{2} \cdot \\Gamma \cdot \sigma_s[^2]\right) \cdot $$d_t$$ - D \cdot ds_t \tag{26}$$

$\$\mathbb{E}\left[\frac{dB_t}{B_t}\right]/$$d_t$$ = $s_t$ - D \cdot \mathbb{E}\left[\frac{ds_t}{$$d_t$$}\right] + \frac{1}{2} \cdot \\Gamma \cdot \sigma_s[^2] \tag{27}$$

$\$\text{spread} + \text{spread curve roll down} + \text{spread convexity}$$

!500

!500

# Summary
- Capital structure and credit default events
- Credit ratings
- Credit instruments & contractual spec
- Market participants
- Trading details
- Corporate Bonds: valuation and risk
- Corporate credit spreads
- Interest rate hedging
# Appendix: Modelling Approaches: Structural vs. Reduced Form Credit Risk Models
## Structural Credit Risk Models
- Introduced by Robert C. Merton (1974), refined by Black-Cox (1976) and others
- Equity value represented as call option on company Assets, using Liabilities as strike
- Issuer default triggered by Assets falling below Liabilities (predictable default time)
- Structural credit risk quantified by solving a Black-Scholes-Merton-type equation
- Moody's KMV implementation widely used by credit analysts
## Reduced Form Credit Risk Models
- Introduced by Jarrow & Turnbull (1995), Duffie & Singleton (1999) and others
- Default driven by exogenous Default Intensity (Hazard Rate) process
- Default occurs without warning (non-predictable default time)
- Dynamics of exogenous default intensity process calibrated to market prices
- No direct connection to company's capital structure
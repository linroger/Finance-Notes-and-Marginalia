---
title: Credit Market Session 2
tags:
  - cds
  - cdx_index
  - credit_market
  - etfs
  - sovereign_bonds
  - fixed_income
  - hazard_rate
aliases:
  - CDS
  - CDX
  - Fixed Income ETFs
  - Sovereign Bonds
  - Credit Default Swap
key_concepts:
  - cdx index trading
  - credit default swap
  - currency devaluation risk
  - etf basis arbitrage
  - fixed income etfs
  - hazard rate model
  - sovereign bonds
  - sovereign debt issuers
  - floating rate bonds
  - reference interest rates
---

# Credit Market Session 2

## Sovereign Bonds, ETFs, CDS and CDX

[^1]: Sovereign Bonds
   - Sovereign bonds
[^2]: ETFs
   - Fixed Income ETFs
   - Sovereign Bond ETFs
   - Aggregated Cash-Flows method
[^3]: Floating rate bonds
   - Floating rate cash-flows
   - Financed floating rate bonds
[^4]: CDS and Hazard Rates
   - Credit Default Swap specs and cash-flows
   - CDS quoting and trading
   - Hazard Rate Model
[^5]: CDX Index
   - CDX IG, HY and EM indexes
   - Pairs trading using CDX indexes
[^6]: Q&A

## What Is Special About Sovereigns?

- Think of a sovereign as a "corporation" with monopoly on managing resources of an entire state/country
- Ability to issue "common stock" at will ("printing press" in local currency)
- Legal power to enforce local economic activity & taxation be conducted in local currency (it's own "common stock")
- Central Banks manage supply and value of "common stock" of via interest rates, QE, QT, swaps with other CBs, etc

## Why Do Governments Issue Bonds in Foreign Currencies?

- When sovereigns need money to fund operations, they usually issue debt in their own currencies
- If they struggle to pay off the bonds, they print more money (diluting the value of the "common stock")
- This can cause inflation, eroding investors earnings potential
- A sovereign may issue debt in a foreign currency to calm investor fears of currency devaluation
- Issuing debt in a foreign currency exposes a nation to exchange rate risk
  - If the local currency drops in value, paying down international debt becomes costlier

## Valuation and Risks of Sovereign Bonds

- Sovereign Debt Issuers Are Considered
  - Risk-free in local currency (they own the "printing press")
  - Risky for USD and other foreign currencies (cannot print foreign currencies)
- Risk factors: a country's debt-to-GDP ratios, economic growth prospects, political risks, etc
- In default, sovereigns suspend payment of contractual cash-flows
- There is no bankruptcy/liquidation procedure for sovereign entities
- Defaulted bonds trade at distressed levels, based on likelihood of recovering the funds sometime in the future
- Sovereign bond investors can try to recover assets abroad, but it can be tricky

### Sovereign Bond Example: Brazil 8.5 2034

!500

### Sovereign Bond Example: Turkey 8 2034

!500

### Sovereign Yield/Spread Curves: US vs Brazil vs Turkey

!500

### Sovereign Bond Example: Sri Lanka 6.85 2024 (Defaulted)

!500

### Sovereign Bond Example: Sri Lanka 6.85 2024 (Historical Prices)

!500

## Fixed Income ETFs: 'Credit' Trading as 'Equity'

- Basket of bonds packaged into ETF shares
- ETF basket weights and NAVs published daily
- Major ETF issuers: BlackRock, StateStreet, Vanguard, etc
- Primary Market: enables "in-kind" creation/redemption of ETF shares
- Secondary Market: electronic trading on equity exchanges (NYSE Arca, NYSE, NASDAQ, BATS, EDGE)
- Efficient way for investors to gain macro exposure to credit markets

### Fixed Income ETF Example: LQD (Most Liquid IG Credit ETF)

!500

### LQD Basket Composition

!500

### Historical Prices, Yields and Credit Spreads for LQD

!500

### Total Return Analysis for LQD (Price Dynamics + Dividends)

!500

### ETF Basis (Market vs Intrinsic NAV): LQD

!500

### ETF Creations/Redemptions & Basis Arbitrage

!500

## Sovereign Bond ETFs

- ETFs that track a sovereign bond index (monthly re-balancing)
- Coupon payments accumulated over time and paid as monthly dividends
- Principal payments re-invested according to target index weights
- Sovereign bond exposure can be hedged with "CDX EM"

### Examples

- EMB: tracking JPM USD Emerging Market Bond index
- EMHY: tracking JPM USD Emerging Market HY Bond index

### Sovereign Bond ETF Example: EMB ("Emerging Market Bonds")

!500

### EMB Composition: ~600 Fixed Rate Sovereign Bonds

!500

### Coupon Cash-Flows Distributed as Monthly Dividends

!500

### Computing ETF Yield and Spread Using ACF Method

- Model ETF as "synthetic bond" by aggregating weighted constituent cash-flows
- Discount aggregated cash-flows using flat yield to match the ETF market price (ignoring yield dispersion of individual sovereign issuers)
- Use weighted average "time to maturity" of cash-flows to determine treasury benchmark
- Compute spread to benchmark (to interpolated treasury yield for g-spread)

### ACF Cash-Flow Aggregation Example

!500

### Yield and Spread/YAS Calculation for EMB ETF

!500

## Why Do Corporations (Specifically Banks) Issue Floating Rate Bonds?

- Commercial/other corporate loans are floating rate contracts
- Banks provide commercial loans to corporations and issue floating rate bonds to match the risk exposure
- Banks can swap their fixed rate vs floating rate exposure via interest rate swaps

### Examples

- Floating rate High Yield senior loans (monthly coupon frequency)
- Floating rate Corporate Bonds issued by banks/financials (quarterly coupon frequency)

## Reference Interest Rates (April 8 2024)

- Federal Funds Target Rate - Lower Bound (currently 5.25%)
- Federal Funds Target Rate - Upper Bound (currently 5.5%)
- Federal Funds Effective Rate (currently 5.33%)
- SOFR - Secured Overnight Financing Rate (currently 5.32%)
- 3M Term SOFR Rate (currently 5.28%)
- 3M US Treasury Rate (currently 5.35%)

### Reference Interest Rates: Fed Funds (E/U/L) and SOFR

!500

### Historical 3M Term Interest Rates: SOFR vs US Treasuries

!500

### Interest Rates Curves: SOFR vs Active Treasury (April 8 2024)

!500

## Composition of Floating Rate Cash-Flows

- Floating rate cash-flow payments are composed of two parts:
  - Reference Index Rate part: usually indexed to SOFR, FedFunds, LIBOR, etc
  - Contractual Spread part: "floating" on the top of the Reference Index rate
- Reference Index Rate gets "fixed"/reset on the coupon frequency schedule
- Coupons determined "on-the-fly", known on payment date

### Floating Rate Bond (SOFR Ref Index): Morgan Stanley

!500

## Investing at Risk-Free Reference Rates (FedFunds, SOFR, LIBOR)

!500

## Risky Bond Cash-Flows Indexed to Reference Rate

!500

### Floating Rate Bond Financed at Reference Index Rate

!500

## Financed Risky Floating Rate Bond

- Long position: floating rate bond
- Short position: finance the cash costs via Reference Index Rate contracts (FedFunds, SOFR)
- Enables investor to "extract" the company specific credit risk
- Eliminates (most) exposure to interest rates
- Investor receives spread premium payments to maturity (or default time)
- Investor pays loss in case of default (100% - bond recovery value)

### Credit Default Swap Cash-Flows

!500

## What Is A CDS Contract?

- Synthetic swap contract "mimicking" cash-flows of financed floating rate bond
- "Insurance" contract linked to an issuer credit default event
- Mainly used for hedging long corporate bond positions against credit default risk
- Fixed/Premium Leg details: seller of protection receives spread premiums until maturity (or default)
- Default/Loss Leg details: seller of protection pays the loss in case of default before maturity

## CDS Accounting Convention

- Seller Of CDS Contract: Investor sells credit default protection
  - Corresponds to "long risk" position in (financed floating rate) bond
  - It is a bet on no default occurring before maturity
- Buyer Of CDS Contract: Investor buys credit default protection
  - Corresponds to "short risk" position in (financed floating rate) bond
  - It is a bet on default occurring before maturity

## International Swaps and Derivatives Association (ISDA)

- CDS market regulated by International Swaps and Derivatives Association
- ISDA agreement with PB is needed to enter into CDS contracts
- Provides Standard Model for CDS pricing and risk ("hazard rate model")
- Role of ISDA Committee
  - Declare when default event occurs for an issuer
  - Run defaulted bond recovery rate auction / publish CDS recovery rate
  - Coordinate default settlement of existing CDS contracts

## Credit Default Swap Specs and Cash-Flows

### CDS Contract Specs

- Credit issuer entity
- Rank/seniority: usually Senior Unsecured/SNRFOR
- Currency
- Coupon premium: 100bps for IG, 500bps for HY issuers
- Maturity date: quarterly payments (on IMM dates) to maturity
- ISDA docs: SNAC 2014 XR SR USD
- Reference proxy bond (if available)

## CDS Quoting and Trading Conventions

- Quotation in spread for IG issuers
- Quotation in "points upfront" for HY issuers
- Quotes converted into "points upfront" for trade settlement (via ISDA Standard Model)
- ISDA Standard Model also provides risk and accrued calcs

### CDSW Screen: IBM 5Y CDS (ISDA STD Model)

!500

### CDSW Screen: Ford Motor Credit 5Y CDS (ISDA STD Model)

!500

### CDS Par Spread Curves: Ford Motor Credit (5Y Most Liquid)

!500

### Ford Motor Credit: CDS Spreads vs Cash Equity (INV)

!500

## ISDA CDS Standard Model

!500

### Hazard Rate Model Inputs

- Contractual cash-flows to maturity
- Calibrated discount factors curve for given Reference Interest Rate (SOFR)
- Expected recover rates given default (by seniority rank)
- "Market implied" survival probability curve ... calibrated to standard CDS maturities: 6M, 1Y, 2Y, 3Y, 5Y, 7Y and 10Y
- Hazard rates: local probabilities of default, can be "computed" from survival probability curves

### Shape of Survival Probability Curves

!500

### Simple Valuation Formulas (Flat Hazard Rate Model)

$$PV_{CDS}\left(c, r, h, R, T\right)=\left[\frac{c-(1-R)\cdot h}{r+h}\right]\cdot\left[1-e^{-T\cdot(r+h)}\right]. \tag{1}$$

$$PV_{Bond}\left(c, r, h, R, T\right)=1+\left[\frac{c-r-(1-R)\cdot h}{r+h}\right]\cdot\left[1-e^{-T\cdot(r+h)}\right] \tag{2}$$

See next session for details on the Hazard Rate Model

### CDS PV Surface (5% Flat Interest Rates, 5% Coupon)

!500

## CDX Contract Specs

- CDX is an equally weighted index of CDS contracts
- Reference issuers portfolios
  - CDX IG: top 125 North American Investment Grade CDS issuers (100bps coupon)
  - CDX HY: top 100 North American High Yield CDS issuers (500bps coupon)
  - CDX EM: 20 sovereign CDS issuers (100bps coupon)
- Financials are excluded (banks not allowed to trade their own CDS)

### CDX Contract Details

- IHS Markit provides the index composition
- Electronically trading on SEF, ICE cleared
- CDX indexes roll every 6 months (March and September IMM dates)
- Individual CDS defaults settled in cash after recovery rate auctions
- ISDA docs: SNAC 2014 XR SR USD

### CDX Example: IG 5Y Series 42

!500

### CDX IG Series 42 Composition: 125 Equally Weighted Issuers

!500

### CDX HY 42 Composition: 100 Equally Weighted Issuers

!500

### CDX EM 41 Composition: 20 Emerging Market Sovereign Issuers

!500

## What Do CDX Index Spreads Represent?

- Level of credit default risk in US Markets (by credit market segment: IG vs HY)
- Level of credit default risk in Emerging Markets (CDX EM)
- CDX is most liquid macro trading/hedging instruments for credit risk!
- High leverage, with funding advantage (synthetic swap contract)
- Very similar in nature to Options Volatility Index VIX!

### CDX IG 5Y & 10Y Spreads vs VIX Index

!500

### CDX HY 5Y vs JNK and HYG Spreads

!500

### CDX EM 5Y vs EMB Spreads: What Could Cause the Level Diffs?

!500

## Summary and Q&A

- Sovereign bonds
- Credit ETFs
- Corporate Sovereign
- Floating rate bonds
- CDS
- CDX Index IG HY EM
- Pairs trading

---
academic_level: graduate
aliases:
- Currency Swap Accounting
- FX Risk Management
- Foreign Currency Bonds
cssclasses:
- academia
enhanced: true
enhancement_date: '2025-11-06'
enhancement_id: batch09-000170
key_concepts:
- Black-Scholes option pricing model and continuous-time finance
- Options Greeks and sensitivity analysis for risk management
- Duration analysis and interest rate risk management
- Convexity adjustments and yield curve sensitivity
- Credit default swaps (CDS) and credit risk modeling
- Currency swaps and foreign exchange risk management
- Collateralized debt obligations (CDO) and tranche structure
- Arbitrage opportunities and no-arbitrage pricing
- Swap Market Mechanisms and Pricing
- Risk Measurement and VaR Backtesting
- Bid-Ask Spreads and Market Impact
- Delta, Gamma, and Vega Hedging Techniques
- Price Discovery and Market Efficiency
- Bond Pricing and Yield to Maturity Analysis
- Fixed Income Securities and Credit Quality
- Value at Risk and Expected Shortfall
- Factor Models and Asset Pricing
- Market Microstructure and Liquidity Analysis
- Fama-French Factors and Style Analysis
- Hedging Strategies and Risk Mitigation
- Dynamic vs Static Hedging in Practice
- Government and Corporate Bond Markets
- Interest Rate Swaps and Currency Swap Structures
- Stress Testing and Extreme Value Analysis
- Credit Default Swaps and Credit Risk Transfer
- Arbitrage Pricing Theory and Multi-Factor Models
linter-yaml-title-alias: Arbitrage Opportunity Accounting
professional_application: theoreti
status: active
tags:
- arbitrage-opportunity
- binomial-model
- black-scholes-model
- cds
- collateralized-debt-obligation
- continuous-time-pricing
- convexity-adjustment
- counterparty-risk
- credit-default-swap
- credit-derivatives
- credit-modeling
- credit-rating
- cross-currency-swap
- currency-hedging
- currency-markets
- cross-hedging
- zero-coupon-bonds
- clean-price
- high-frequency-trading
- algorithmic-trading
- momentum
- expected-shortfall
- parametric-var
- conditional-var
- extreme-value-theory
- basis-risk
- book-to-market
- fixed-income
- var-methodologies
- historical-var
- hedge-strategies
- vega-hedging
- volatility-analysis
- sofr
- swap-rate
- style-analysis
- bond-pricing
- swap-spread
- corporate-bonds
- stress-testing
- roll-over-risk
- arbitrage
- market-efficiency
- delta-hedging
- value-at-risk
- order-flow
- total-return-swaps
- libor
- currency-swaps
- overnight-indexed-swaps
- arbitrage-pricing-theory
- multi-factor-models
- bid-ask-spread
- government-bonds
- static-hedging
- price-discovery
- size-effect
- factor-models
- basis-swaps
- liquidity
- value-factor
- interest-rate-swaps
- dirty-price
- credit-default-swaps
- gamma-hedging
- dynamic-hedging
- monte-carlo-var
- hedge-effectiveness
- risk-management
- var-backtesting
- coupon-bonds
- market-impact
- apt
- current-yield
- yield-to-maturity
- fama-french
title: Arbitrage Opportunity Accounting
type: note
---
--



# Arbitrage Opportunity Accounting
## 1. DETERMINING CURRENCY SWAP RATES

### 1.1. PREAMBLE

[^1]: Governments often issue bonds in foreign currencies (e.g., the Greek government issues Greek bonds denominated in USD rather than in EUR, the home currency).
[^2]: In issuing bonds in a foreign currency, a government exposes itself to exchange rate risk. If the foreign currency appreciates relative to the home currency, then more units of the home currency are required to pay the interest and principal in the foreign currency.
[^3]: Currency swaps serve as a hedge against such exchange rate risk.

### 1.2. CURRENCY SWAP

[^1]: Consider two countries: Home H and Foreign F.
[^2]: At inception $t = 0$, Home issues government bonds with value $X$ in currency F.
[^3]: The bond pays a coupon (interest) semi-annually at the annual interest rate $c$.
[^4]: To hedge against exchange rate risk, Home enters in a swap contract.
[^5]: Let $M_0$ denote the exchange rate for F/H currencies at inception $t = 0$.
[^6]: At inception $t = 0$, the swap contract requires:
   a. Home pays $N_F = X$ in F currency.
   b. Home receives $N_H = X \cdot \frac{1}{M_0}$ in H currency.
[^7]: At maturity $t = T$, the swap contract requires:
   a. Home receives $N_F = X$ in F currency.
   b. Home pays $N_H = X \cdot \frac{1}{M_0}$ in H currency.

### 1.3. VALUE OF BONDS

[^1]: Time $t = 0$ value of the bond denominated in F currency:
   $$B_0^F = \sum_{t=1}^T \frac{c}{2} \cdot N_F \cdot Z_F(0, t)\text{ Interest PV} + N_F \cdot Z_F(0, T)\text{ Principal PV}$$

[^2]: Time $t = 0$ value of the bond denominated in H currency:
   $$B_0^H(K) = \sum_{t=1}^T \frac{K}{2} \cdot N_H \cdot Z_H(0, t)\text{ Interest PV} + N_H \cdot Z_H(0, T)\text{ Principal PV}$$

   - $K$ denotes the "swap rate," i.e. the annualized coupon rate for semi-annual payments of coupons in the H currency.
   - The bond value $B_0^H(K)$ is a function of the swap rate $K$.

### 1.4. SWAP RATE UNDER SPOT EXCHANGE OF PRINCIPAL

[^1]: Time $t = 0$ value of the swap in F currency is equal to the value of the long position in the bond denominated in the F currency minus the value of the short position in the bond denominated in the H currency, converted into the F currency using the time $t = 0$ exchange rate $M_0$:
   $$V_{0}^{\text{Swap, }F}(K)=B_{0}^{F}-M_{0}\cdot B_{0}^{H}(K)+V_{0}^{\text{FX,}F}(\overline{M}_{0})$$

[^2]: Value of exchange of principal:
   $$V_0^{\mathrm{FX,}F}(\bar{M}_0)=\left(\frac{M_0}{\overline{M}_0}-1\right)\cdot N^F$$

---
tags:
- basis-swap
- basis_swap
- bps
- cross_currency_swap
- currency
- currency_hedging
- defi
- discounted_cashflows
- exchange-rate
- fixed_income
- forward
- interest-rate
- interest_rate_parity
- libor
- ltfx_contract
- swap
- swap_pricing
aliases:
- Citi Guide
- Forward Foreign Exchange
- LTFX
- POS
- Swap Pricing
- Cross Currency Swaps
key_concepts:
- Basis swap definition
- Basis swap mechanics
- Common swap structures
- Cross currency swap pricing
- Cross-currency basis
- Currency swap structure
- Derivative securities
- Discounted cashflow methodology
- Financial risk management
- Fixed vs floating leg
- Foreign exchange hedging
- Interest rate parity application
- Interest rate swap pricing
- Long-Dated Foreign Exchange (LTFX)
- Portfolio optimization
- Present value of swaps
- Principal-Only Swap (POS)
- Quantitative financial analysis
- Risk assessment and mitigation
- Swap curve construction
- Swap pricing
- Swaption valuation
cssclasses: academia
---

# Citi: Guide to Swaps

## Swap Pricing: Discounted Cashflows

!500

## Common Swap Structures

- **Basis swap** (i.e., floating/floating) is one of the basic building blocks in fixed/fixed and fixed/floating Cross Currency Swaps (CCS).
- A basis swap in this context is defined as the exchange of LIBORs in two different currencies with both initial and final exchange of principal.
- Cost of a basis swap is quoted against USD LIBOR flat (e.g., USD LIBOR vs YEN LIBOR 17 bps) and is driven by demand and supply.
- Example: ABC company has 3-year funding in JPY and is required to hedge exchange rate exposure created by this foreign currency debt.

!500

## Fixed/Fixed Cross Currency Swap

!500

!500

## Principal-Only Swap (POS)

- Compared to a full cross currency swap, a Principal-Only Swap (POS) costs less because a POS does not provide a hedge against exchange rate risks on coupon payments.
- Consider a 3-year USD/JPY swap:
  - At maturity, company receives JPY principal and pays USD principal at current spot rate (in fact can be any agreed exchange rate).
  - Same as a long-dated forward contract of the company buying JPY and selling USD at current spot rate.
  - Due to the interest rate differential between JPY and USD, forward USD/JPY exchange rate is lower than spot rate (i.e., JPY at premium).
  - The contract to buy JPY/sell USD forward at current spot rate has a positive value to the Company.
  - As a compensation to Citibank (i.e., to make NPV = 0), the Company will need to pay a periodic coupon (either in USD or JPY) to Citibank.

!500

!500

## Coupon-Only Swap

- Consider a 3-year USD/JPY swap with only coupon exchanges.
- There are no principal exchanges. If the USD fixed rate is known, we can solve for the JPY fixed rate.

!500

## Long-Dated Foreign Exchange (LTFX)

- A Long-Dated Foreign Exchange (LTFX) contract is a Zero Coupon Currency & Interest Rate Swap
- Instead of exchanging coupons, at the time of dealing, the Principal amount on one set of cashflows is set so that the NPV = 0.

!500

## Using Interest Rate Parity - Pricing Forward Foreign Exchange

!500

!500

!500

!500

Rather than using zero coupon rates, each currency's discount factors may be used:

**Short Cut:** Forward Rate = Spot × dfUSD/dfJPY = 105 × 0.9420 / 0.9975

!500

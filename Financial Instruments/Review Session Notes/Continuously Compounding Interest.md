---
linter-yaml-title-alias: CONTINUOUSLY COMPOUNDING INTEREST
title: CONTINUOUSLY COMPOUNDING INTEREST
tags:
  - compounding_interest
  - continuous_compounding
  - discrete_compounding
  - gross_return
  - interest_rate
aliases:
  - Compound Interest
  - Continuously Compounding
key_concepts:
  - Annual interest rate
  - Continuously compounding interest rate
  - Discrete compounding frequency
  - Gross rate of return
  - Maturity horizon T
---

# CONTINUOUSLY COMPOUNDING INTEREST

#TA_Session

The [[A Guide to the Front End and [[Basis Swaps|Basis Swap]] Markets#[[Short-Term Rates and the Transition from LIBOR|London Interbank Offered Rate]] (LIBOR)|LIBOR]] [[Continuously Compounding Interest|annual interest rate]] 𝑟𝑑 compounds at a discrete frequency. For example, interest may compound on an annual basis, a semi-annual basis, a monthly basis, and so on.
Let 𝑛 denote the discrete frequency with which interest compounds in a year. For example, if interest compounds on an annual basis, then 𝑛 = 1. If interest compounds on a semi-annual basis, then 𝑛 = 2. If interest compounds on a monthly basis, then 𝑛 = 12.

 For a given maturity 𝑇 and [[Continuously Compounding Interest|discrete compounding frequency]] 𝑛, the gross rate of return is$$\left(1+\frac{r_d}n\right)^{n\cdot T}$$

By contrast, under [[Continuously Compounding Interest|continuously compounding]] interest, the gross rate of return is  $$e^{(r_c\cdot T)}$$

The appropriate [[Continuously Compounding Interest|continuously compounding interest rate]] 𝑟𝑐 that aligns with the discrete compounding interest rate 𝑟𝑑 is that which equates the two gross rates of return.$$e^{(r_c\cdot T)}=\left(1+\frac{r_d}n\right)^{n\cdot T}$$

Solving the equation above for the endogenous variable 𝑟𝑐 yields the formula for the [[Continuously Compounding Interest|continuously compounding interest rate]] as a function of the discrete compounding interest rate.$$r_c=n\cdot\ln\left[1+\frac{r_d}n\right]$$

Note that the maturity horizon 𝑇 does not affect the conversion between a discrete compounding interest rate and a [[Continuously Compounding Interest|continuously compounding interest rate]].
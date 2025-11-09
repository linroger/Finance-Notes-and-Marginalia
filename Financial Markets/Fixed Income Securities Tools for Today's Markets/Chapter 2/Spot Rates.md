---
tags:
  - discount_factors
  - semiannual_compounding
  - sofr_swap_rates
  - spot_loan
  - spot_rates
aliases:
  - Spot Rate
  - Spot Rates Definition
key_concepts:
  - Discount factors and spot rates
  - Forward vs spot transactions
  - SOFR swap rates
  - Semiannual compounded spot rate
  - Spot rate definition
---

# 2.4 SPOT RATES  

The word spot in finance typically refers to transactions for immediate or imminent settlement, as opposed to forward transactions, which settle further in the future. Consistent with this usage, a [spot rate](../../../International%20Finance/The%20Foreign%20Exchange%20Market%20Annotations.md) is the rate on a. spot loan, an agreement in which a lender gives money to the borrower at or around the time of the agreement and, furthermore, expects repay-. ment at some single, specified time in the future. For example, along the lines of Equation (2.7), a two-year [investment](../../../Advanced%20Investments/An%20Asset%20Allocation%20Primer.md) of 100, at a semiannually compounded [spot rate](../../../International%20Finance/The%20Foreign%20Exchange%20Market%20Annotations.md) of $0.1136\%$ , grows over those two years or four. semiannual periods to a final payment of,.  
$$
100{\left(1+\frac{0.1136\%}{2}\right)}^{2\times2}=100.2274
$$  

More generally, denote the semiannually compounded $t$ -year [spot rate](../../../International%20Finance/The%20Foreign%20Exchange%20Market%20Annotations.md) by $\hat{\boldsymbol{r}}(t)$ . With semiannual compounding and an [investment](../../../Advanced%20Investments/An%20Asset%20Allocation%20Primer.md) period of $t$ years, or $2t$ semiannual periods, investing one unit of [currency](../../../Financial%20Instruments/Lecture%20Notes-%20Financial%20Instruments/Teaching%20Note%201-%20Forward%20Rates%20Agreement/Forwards%20and%20Futures%20Notes.md) from now to year $t$ generates final proceeds of,  
$$
\left(1+{\frac{{\hat{r}}(t)}{2}}\right)^{2t}
$$  

To link spot rates and discount factors, note that if one unit of [currency](../../../Financial%20Instruments/Lecture%20Notes-%20Financial%20Instruments/Teaching%20Note%201-%20Forward%20Rates%20Agreement/Forwards%20and%20Futures%20Notes.md). grows to the quantity in (2.17) in. $t$ years, then the present value of that. quantity, by definition, is one. Using discount factors to compute that present value,  
$$
\left(1+\frac{\hat{r}(t)}{2}\right)^{2t}d(t)=1
$$  

or, solving for $d(t)$  
$$
d(t)=\frac{1}{\left(1+\frac{\hat{r}(t)}{2}\right)^{2t}}
$$  

Either of these two equations can be used to solve for a [spot rate](../../../International%20Finance/The%20Foreign%20Exchange%20Market%20Annotations.md) of term. $t$ given the [discount factor](../Chapter%201/Discount%20Factors.md) of that term. To illustrate, consider the discount factors implied by [SOFR swap rates](.md) in Table 2.1. The two-year [discount factor](../Chapter%201/Discount%20Factors.md) is 0.997732, which, by either (2.18) or (2.19), implies that the two-year [spot rate](../../../International%20Finance/The%20Foreign%20Exchange%20Market%20Annotations.md) is $0.1136\%$ . Along the same lines, Table 2.1 computes spot rates. of terms 0.5 to 2.0 years from the respective discount factors..  
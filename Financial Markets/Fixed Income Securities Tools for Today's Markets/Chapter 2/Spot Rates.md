---
tags:
- spot_loan
- discount
- discount_factors
- implied
- sofr
- call
- currency
- put
- semiannual_compounding
- spot-rate
- sofr_swap_rates
- forward
- spot_rates
- future
- swap
aliases:
- Spot Rate
- Spot Rates Definition
key_concepts:
- Cross-currency swaps and FX risk management
- Swap market mechanisms and pricing
- Financial markets and securities trading
- Capital market instruments and their characteristics
- Modern portfolio theory and asset pricing
- Financial engineering and structured products
- Investment analysis and decision-making
- Financial regulation and market oversight
- SOFR implementation and overnight rate markets
- Spot Rate in financial markets
- Financial markets and instrument analysis
- Quantitative finance and mathematical modeling
- Risk management and hedging strategies
- Investment analysis and portfolio theory
- Capital markets and trading strategies
- Financial engineering and product innovation
- Regulatory frameworks and compliance
- Market dynamics and behavioral finance
enhanced: true
enhancement_date: '2025-11-06'
enhancement_id: batch08-000216
batch: BATCH_AH
processing_agent: Enhancement Agent 8
---



# 2.4 SPOT RATES  

The word spot in finance typically refers to transactions for immediate or imminent settlement, as opposed to forward transactions, which settle further in the future. Consistent with this usage, a spot rate is the rate on a. spot loan, an agreement in which a lender gives money to the borrower at or around the time of the agreement and, furthermore, expects repay-. ment at some single, specified time in the future. For example, along the lines of Equation (2.7), a two-year investment of 100, at a semiannually compounded spot rate of $0.1136\%$ , grows over those two years or four. semiannual periods to a final payment of,.  
$$
100{\left(1+\frac{0.1136\%}{2}\right)}^{2\times2}=100.2274
$$  

More generally, denote the semiannually compounded $t$ -year spot rate by $\hat{\boldsymbol{r}}(t)$ . With semiannual compounding and an investment period of $t$ years, or $2t$ semiannual periods, investing one unit of currency from now to year $t$ generates final proceeds of,  
$$
\left(1+{\frac{{\hat{r}}(t)}{2}}\right)^{2t}
$$  

To link spot rates and discount factors, note that if one unit of currency. grows to the quantity in (2.17) in. $t$ years, then the present value of that. quantity, by definition, is one. Using discount factors to compute that present value,  
$$
\left(1+\frac{\hat{r}(t)}{2}\right)^{2t}d(t)=1
$$  

or, solving for $d(t)$  
$$
d(t)=\frac{1}{\left(1+\frac{\hat{r}(t)}{2}\right)^{2t}}
$$  

Either of these two equations can be used to solve for a spot rate of term. $t$ given the discount factor of that term. To illustrate, consider the discount factors implied by SOFR swap rates in Table 2.1. The two-year discount factor is 0.997732, which, by either (2.18) or (2.19), implies that the two-year spot rate is $0.1136\%$ . Along the same lines, Table 2.1 computes spot rates. of terms 0.5 to 2.0 years from the respective discount factors..

---
cssclasses:
  - academia
title: PSET 1-Financial Instruments
tags:
  - arbitrage
  - financial_instruments
  - forward_rates
  - linear_compounding
  - interest_rates
  - currency_markets
  - exchange_rates
aliases:
  - PSET 1-FINANCIAL INSTRUMENTS
  - Problem Set 1
key_concepts:
  - Compute Forward Exchange Rate
  - Forward Exchange Rate
  - Forward pricing formula
  - Linear compounding rates
  - Natural logarithm function
  - Arbitrage opportunity identification
  - Covered interest rate parity
  - Interest rate conversion
  - No-arbitrage relationship
---
# PSET 1-Financial Instruments

Bus 35100
John Heaton - Homework 1

Due at the beginning of class week 2.

## 1. ARBITRAGE AND FORWARD RATES

### Exchange Rate Data

| Date | $/EURO SPOT | $/EURO FORWARD 1M | $/EURO FORWARD 3M | $/EURO FORWARD 6M | $/EURO FORWARD 1Y |
| ---- | ----------- | ----------------- | ----------------- | ----------------- | ----------------- |
| Monday, October 3, 2005 | 1.19235 | 1.19425 | 1.19812 | 1.20462 | 1.21789 |
| Monday, October 2, 2006 | 1.27385 | 1.27619 | 1.28007 | 1.28505 | 1.29298 |
| Monday, October 1, 2007 | 1.42325 | 1.42448 | 1.42562 | 1.42667 | 1.42805 |
| Wednesday, October 1, 2008 | 1.4021 | 1.40422 | 1.4047 | 1.40302 | 1.39603 |
| Thursday, October 1, 2009 | 1.4533 | 1.45341 | 1.45325 | 1.45307 | 1.45302 |

### Interest Rate Data

#### US LIBOR 

| Date | 1M | 3M | 6M | 1Y |
| ---- | -- | -- | -- | -- |
| October 3, 2005 | 3.88 | 4.08 | 4.27 | 4.48 |
| October 2, 2006 | 5.32 | 5.37 | 5.38 | 5.32 |
| October 1, 2007 | 5.12 | 5.23 | 5.15 | 4.94 |
| October 1, 2008 | 4.00 | 4.15 | 4.04 | 4.04 |
| October 1, 2009 | 0.25 | 0.28 | 0.62 | 1.24 |

#### EURO LIBOR

| Date | 1M | 3M | 6M | 1Y |
| ---- | -- | -- | -- | -- |
| October 3, 2005 | 2.12 | 2.18 | 2.21 | 2.33 |
| October 2, 2006 | 3.29 | 3.42 | 3.58 | 3.74 |
| October 1, 2007 | 4.39 | 4.79 | 4.76 | 4.72 |
| October 1, 2008 | 5.07 | 5.29 | 5.39 | 5.50 |
| October 1, 2009 | 0.39 | 0.70 | 1.00 | 1.23 |

#### US LIBOR (continuously compounded rates)

| Date | 1M | 3M | 6M | 1Y |
| ---- | -- | -- | -- | -- |
| October 3, 2005 | 3.87 | 4.06 | 4.22 | 4.39 |
| October 2, 2006 | 5.31 | 5.33 | 5.31 | 5.18 |
| October 1, 2007 | 5.11 | 5.20 | 5.08 | 4.82 |
| October 1, 2008 | 4.00 | 4.13 | 4.00 | 3.96 |
| October 1, 2009 | 0.25 | 0.28 | 0.62 | 1.23 |

#### EURO LIBOR (continuously compounded rates)

| Date | 1M | 3M | 6M | 1Y |
| ---- | -- | -- | -- | -- |
| October 3, 2005 | 2.12 | 2.17 | 2.20 | 2.31 |
| October 2, 2006 | 3.29 | 3.41 | 3.55 | 3.68 |
| October 1, 2007 | 4.38 | 4.76 | 4.70 | 4.61 |
| October 1, 2008 | 5.06 | 5.25 | 5.32 | 5.35 |
| October 1, 2009 | 0.39 | 0.70 | 1.00 | 1.22 |

Consider a one-year forward contract for converting between dollars and Euros. The current exchange rate is $1.20 for each Euro. The one-year risk-free rate in dollars is 5% in continuously compounded units while the one-year risk-free rate in Euros is 4.5%.

(1) According to the principle of no-arbitrage, what should be the one-year forward rate?

$$F_{0,T}=S_{0}e^{(r_{USD}-r_{EUR})T}$$

$$F_{0,T}=1.20 \times e^{(0.05-0.045) \times 1}= \$1.20602 \text{ per euro}$$

> [!ANSWER] According to no-arbitrage, the Forward Exchange rate is given by
> $$M_{0}\cdot e^{(r_{H}-r_{F})\cdot T}\tag{1}$$
>
> where $M_0$ is the spot exchange rate (number of units of the Home currency to buy 1 unit of the Foreign currency), $r_H$ is the annualized continuously-compounded interest rate in the Home country, $r_F$ is the annualized continuously-compounded interest rate in the Foreign country and $T$ is the maturity we are interested in.
> 
> Here the home country is the US so that:
> - $r_H = r_{USD} = 5\%$ and
> - $r_F = r_{EUR} = 4.5\%$
> 
> Further, $M_0 = 1.2$ and $T = 1$. The forward rate should be:
> 
> $$F_{0,1}=M_{0}\cdot e^{(r_{USD}-r_{EUR})\cdot T}=1.2\cdot e^{5\%-4.5\%}=1.2060$$
(2) Suppose that the one-year forward contract is currently trading at $1.15 per Euro. Is there an arbitrage opportunity? If so, explain in detail the trading you would like to do to exploit this arbitrage opportunity.

### Forward Rates Implied by No Arbitrage

| Date | 1M (0.0833 years) | 3M (0.25 years) | 6M (0.5 years) | 1Y (1 year) |
| ---- | ----------------- | --------------- | -------------- | ----------- |
| Monday, October 3, 2005 | 1.1941 | 1.1980 | 1.2045 | 1.2174 |
| Monday, October 2, 2006 | 1.2760 | 1.2800 | 1.2851 | 1.2932 |
| Monday, October 1, 2007 | 1.4241 | 1.4248 | 1.4260 | 1.4262 |
| Wednesday, October 1, 2008 | 1.4009 | 1.3982 | 1.3929 | 1.3827 |
| Thursday, October 1, 2009 | 1.4531 | 1.4518 | 1.4505 | 1.4535 |

### Difference Between Quoted and No-Arbitrage Forward Rates

| Date | 1M | 3M | 6M | 1Y |
| ---- | -- | -- | -- | -- |
| Monday, October 3, 2005 | 0.0002 | 0.0001 | 0.0002 | 0.0005 |
| Monday, October 2, 2006 | 0.0002 | 0.0001 | 0.0000 | -0.0002 |
| Monday, October 1, 2007 | 0.0004 | 0.0008 | 0.0007 | 0.0018 |
| Wednesday, October 1, 2008 | 0.0034 | 0.0065 | 0.0102 | 0.0134 |
| Thursday, October 1, 2009 | 0.0003 | 0.0015 | 0.0025 | -0.0004 |

> [!ANSWER]
> The traded value of the forward is $1.15, which is below the no-arbitrage value of $1.2060, so there is an arbitrage opportunity to be exploited. We would like to "buy low" and "sell high." In other words, we would like to enter into the forward contract to buy Euros at $1.15 and *synthetically* sell them forward using the bond markets in the countries and the current exchange rate.
> 
> Let's suppose we want to do this at the level of 100 million Euros. Here are the trades:
> 
> 1. Buy 100 million Euros forward, which creates an obligation of $100M × $1.15 = $115 million at time 1 (one year).
> 2. We need to trade today so that we have (at least) the $115 million to deliver at time 1. To do this:
>    - Borrow 100M × e^(-0.045) = 95.5887 million Euros today.
>    - Convert the 95.5887 million Euros today to dollars: 95.5887M × $1.20 = $114.7197 million today
>    - Invest $114.7197 million at the rate of 5% in continuously compounded units.
> 
> Notice that the trades in the bond markets and foreign exchange market create the following cash flows at time 1:
> 
> - Euros owed at time 1: $95.5887M \cdot e^{0.045} = 100M$ Euros, which is covered by our receipt of 100 million Euros at time 1 under the forward contract.
> - Dollars received at time 1: $114.7197M \cdot e^{0.05} = 120.6015$ million dollars, which more than covers our obligation of $115 million under the forward contract.
> 
> The profit at time 1 is: $120.6015M - $115M = $5.6015 million.
> 
> Note: Since there is an arbitrage opportunity, there are several ways to numerically set up the trade to generate extra cash in either Euros or dollars at time 0 or time 1. The trade described here mimics the "no cash today" outcome of the forward contract.
## 2. FORWARD RATES AND COVERED INTEREST RATE PARITY

The Excel file DataHW1 2024.xls contains data on the $/Euro exchange rate on the first business day of October of the years 2005 to 2009. In addition, it contains Forward Rate quotes, as well as US and EURO LIBOR rates.

Please, do the following:

(1) For each date, use the Forward Rate formula discussed in Teaching Note 2 to compute the Forward Exchange Rate. Please do so for all of the given maturities (1 month, 3 months, 6 months, 1 year).

- **Tip #1**: Note that LIBOR rates use linear compounding, while the formula in the teaching notes use continuous compounding. You will need the transformation like the one on page 14 of Teaching Note 2 to use the forward pricing formula we developed.
- **Tip #2**: The log function in the notes on page 14 is the *natural logarithm*. To implement this in Excel you use the function LN NOT the function *LOG*.

### US and EURO LIBOR Continuously Compounded Rates

|          | US LIBOR                          |        |        |        | EURO LIBOR                       |        |        |        |
|----------|-----------------------------------|--------|--------|--------|----------------------------------|--------|--------|--------|
| Date     | 1M                                | 3M     | 6M     | 1Y     | 1M                               | 3M     | 6M     | 1Y     |
|----------|-----------------------------------|--------|--------|--------|----------------------------------|--------|--------|--------|
| 03-Oct-05| 3.87%                             | 4.06%  | 4.22%  | 4.39%  | 2.12%                            | 2.17%  | 2.20%  | 2.31%  |
| 02-Oct-06| 5.31%                             | 5.33%  | 5.31%  | 5.18%  | 3.29%                            | 3.41%  | 3.55%  | 3.68%  |
| 01-Oct-07| 5.11%                             | 5.20%  | 5.08%  | 4.82%  | 4.38%                            | 4.76%  | 4.70%  | 4.61%  |
| 01-Oct-08| 4.00%                             | 4.13%  | 4.00%  | 3.96%  | 5.06%                            | 5.25%  | 5.32%  | 5.35%  |
| 01-Oct-09| 0.25%                             | 0.28%  | 0.62%  | 1.23%  | 0.39%                            | 0.70%  | 1.00%  | 1.22%  |

### Computed Forward Exchange Rates

| Date       | 1M     | 3M     | 6M     | 1Y     |
|------------|--------|--------|--------|--------|
| 03-Oct-05  | 1.1941 | 1.1980 | 1.2045 | 1.2174 |
| 02-Oct-06  | 1.2760 | 1.2800 | 1.2851 | 1.2932 |
| 01-Oct-07  | 1.4241 | 1.4248 | 1.4260 | 1.4262 |
| 01-Oct-08  | 1.4009 | 1.3982 | 1.3929 | 1.3827 |
| 01-Oct-09  | 1.4531 | 1.4518 | 1.4505 | 1.4535 |
> [!ANSWER]
> As above, according to no-arbitrage, the Forward Exchange rate is given by:
> 
> $$M_{0}\cdot e^{(r_{H}-r_{F})\cdot T}\tag{2}$$
> 
> where $M_0$ is the spot exchange rate (number of units of the Home currency to buy 1 unit of the Foreign currency), $r_H$ is the annualized continuously-compounded interest rate in the Home country, $r_F$ is the annualized continuously-compounded interest rate in the Foreign country, and $T$ is the maturity we are interested in.
> 
> Before applying formula 2, we need to compute the continuously compounded LIBOR rates:
> 
> - LIBOR rates use linear compounding, meaning that the x-months LIBOR is compounded 12/x times in a year.
> - The 1-month LIBOR has a $\frac{1}{12}$ = monthly compounding frequency
> - The 3-month LIBOR has a $\frac{3}{12} = \frac{1}{4}$ = quarterly compounding frequency, and so on.
> 
> If we define $m$ to be the number of times interest is compounded in a year (according to what was just said, $m = \frac{12}{x}$), to compute the equivalent continuously-compounded rate we use the equivalence:
> 
> $$e^{r\cdot T}=\left(1+\frac{r_{m}}{m}\right)^{m\cdot T}\tag{3}$$
> 
> where $r_m$ denotes an annualized interest rate compounded $m$ times in 1 year (e.g., $r_{12}$ is the annualized monthly compounded rate, $r_4$ is the annualized quarterly compounded rate, and so on).
> 
> To get a formula for the continuously compounded rate, we take natural logarithms in equation 3:
> 
> $$\ln\left(e^{r\cdot T}\right)=\ln\left[\left(1+\frac{r_{m}}{m}\right)^{m\cdot T}\right]$$
> 
> Then, knowing that $\ln(e^{x})=x$ and that $\ln(a^{x})=x\cdot \ln(a)$:
> 
> $$r\cdot T=m\cdot T\cdot \ln\left(1+\frac{r_{m}}{m}\right)$$
> 
> Dividing both sides by $T$, we finally get:
> 
> $$r=m\cdot \ln\left(1+\frac{r_{m}}{m}\right)\tag{4}$$
> 
> Applying formula 4, we can compute the continuously compounded US and EURO LIBOR rates. The results are shown in the table above. Using these rates, we apply formula 2 to compute Forward Exchange rates.
(2) Do your forward exchange rates match (approximately) the quoted ones?
<<<<<<< HEAD
=======

> [!ANSWER]
> We compute the difference between the quoted and the computed Forward Exchange rates, which are reported in the table below.
> 
> If we exclude October 1st 2008, the difference is smaller than 0.001 in most of the cases.
> 
> For October 1st 2008 (15 days after Lehman failure), the difference is larger. To understand why this is so, think about how we determined formula 2 for the Forward Exchange rate:
> 
> - Our assumption was that we could set up a strategy which perfectly matches the cash flows of a short forward position in euros for dollars.
> - The strategy requires borrowing in euros, exchanging euros into dollars and investing the money at the dollar interest rate.
> - If market participants are worried about third party solvency, borrowing may be much more difficult, especially for longer maturities.
> - If borrowing is more difficult, then arbitrageurs may have a hard time correcting market inefficiencies, and the result is quoted prices misaligned with the theoretical ones.
> 
> **Table: Difference between quoted and computed Forward Exchange rates**
> 
> | Date       | 1M     | 3M     | 6M     | 1Y     |
> |------------|--------|--------|--------|--------|
> | 03-Oct-05  | 0.0002 | 0.0001 | 0.0002 | 0.0005 |
> | 02-Oct-06  | 0.0002 | 0.0001 | 0.0000 | -0.0002|
> | 01-Oct-07  | 0.0004 | 0.0008 | 0.0007 | 0.0018 |
> | 01-Oct-08  | 0.0034 | 0.0065 | 0.0102 | 0.0134 |
> | 01-Oct-09  | 0.0003 | 0.0015 | 0.0025 | -0.0004|
>>>>>>> d83d5c06204d625fbecfdb77e4d3f37c9c80e27b

> [!ANSWER]
> We compute the difference between the quoted and the computed Forward Exchange rates, which are reported in the table below.
> 
> If we exclude October 1st 2008, the difference is smaller than 0.001 in most of the cases.
> 
> For October 1st 2008 (15 days after Lehman failure), the difference is larger. To understand why this is so, think about how we determined formula 2 for the Forward Exchange rate:
> 
> - Our assumption was that we could set up a strategy which perfectly matches the cash flows of a short forward position in euros for dollars.
> - The strategy requires borrowing in euros, exchanging euros into dollars and investing the money at the dollar interest rate.
> - If market participants are worried about third party solvency, borrowing may be much more difficult, especially for longer maturities.
> - If borrowing is more difficult, then arbitrageurs may have a hard time correcting market inefficiencies, and the result is quoted prices misaligned with the theoretical ones.
> 
> **Table: Difference between quoted and computed Forward Exchange rates**
> 
> | Date       | 1M     | 3M     | 6M     | 1Y     |
> |------------|--------|--------|--------|--------|
> | 03-Oct-05  | 0.0002 | 0.0001 | 0.0002 | 0.0005 |
> | 02-Oct-06  | 0.0002 | 0.0001 | 0.0000 | -0.0002|
> | 01-Oct-07  | 0.0004 | 0.0008 | 0.0007 | 0.0018 |
> | 01-Oct-08  | 0.0034 | 0.0065 | 0.0102 | 0.0134 |
> | 01-Oct-09  | 0.0003 | 0.0015 | 0.0025 | -0.0004|

(3) If not,  pick one particular date in which the parity is violated,  and describe the [arbitrage](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%207/Arbitrage%20Pricing%20of%20Derivatives.md) strategy you would undertake.

> [!ANSWER]
> 1. As we have seen that the biggest discrepancy occurs for October 1 st 2008.
> Let's focus on that date and consider the 1 year [Forward Exchange rate](../../Financial%20Engineering/A%20Primer%20on%20Currency%20Derivatives.md). As mentioned above the difference $F^{quoted} − F^{computed}>0$,  that is equivalent to $F^{quoted} > F^{computed}$.
> - The rule of thumb for [arbitrage](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%207/Arbitrage%20Pricing%20of%20Derivatives.md) is to buy cheap and sell dear.
> 	- This means "buy computed" and "sell quoted."
> - The computed [Forward Exchange rate](../../Financial%20Engineering/A%20Primer%20on%20Currency%20Derivatives.md) is a *synthetic* price that we pay if we set-up a strategy that replicates the payoff of a [forward contract](../../Clippings/Forward%20Points%20in%20Currency.md),  while the quoted [Forward Exchange rate](../../Financial%20Engineering/A%20Primer%20on%20Currency%20Derivatives.md) is what we obtain when entering into a forward position (just sign a contract,  much easier than setting up a replicating strategy).
> - We already know that we enter into a [short forward contract](../Lecture%20Notes-%20Financial%20Instruments/Teaching%20Note%201-%20Forward%20Rates%20Agreement/Forward%20Contracts%20on%20Exchange%20Rates.md) to sell 1 euro for dollars (this is the "sell quoted" - we are selling euros and buying dollars; remember that with exchange rates we are long / short the Foreign [currency](../Lecture%20Notes-%20Financial%20Instruments/Teaching%20Note%201-%20Forward%20Rates%20Agreement/Forwards%20and%20Futures%20Notes.md)).
> - On the other side we have to set up a strategy that replicates the payoff of a [long forward](../Lecture%20Notes-%20Financial%20Instruments/Teaching%20Note%203%20Swaps-%20Financial%20Instruments/Forward%20Rates%20Agreement.md) position to buy 1 euro for dollars.
> Let's start by matching the payoffs at maturity.
> 	- A [long forward](../Lecture%20Notes-%20Financial%20Instruments/Teaching%20Note%203%20Swaps-%20Financial%20Instruments/Forward%20Rates%20Agreement.md) contract,  at maturity,  entails:
> 		- An outflow (we pay) of dollars
> 		- An inflow (we receive) of euros To pay dollars tomorrow we simply borrow something in US.
> - To receive euros tomorrow we have to invest something in Europe today. How much? Here we have to remember our goal.
> 	- We are matching the cash flows of a [forward contract](../../Clippings/Forward%20Points%20in%20Currency.md),  and a [forward contract](../../Clippings/Forward%20Points%20in%20Currency.md) does not require any [cash flow](../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%201%20-%20Purpose%20and%20Structure%20of%20Financial%20Markets/Preview%20of%20the%20Book.md) when we enter into it.
> 	- As our strategy so far requires borrowing in dollars and investing in euros today,  to get a [cash flow](../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%201%20-%20Purpose%20and%20Structure%20of%20Financial%20Markets/Preview%20of%20the%20Book.md) equal to 0 we have to match the amount we borrow with the amount we invest,  or in other words we have to invest in Europe the full amount borrowed in US.
> 		- To do this we just need to exchange the dollars for euros today.
> 	- The last thing we need to understand is how much to borrow in dollars today. As the [forward exchange rate](../../Financial%20Engineering/A%20Primer%20on%20Currency%20Derivatives.md) tells us "how many dollar we have to pay in exchange for 1 euro at maturity",  following our logic of matching the cash flows of a [forward contract](../../Clippings/Forward%20Points%20in%20Currency.md) we want to borrow today (in dollars) a sum that will give us 1 euro tomorrow: that's the very definition of present value.
> [!ANSWER]
> - Summing up,  the "buy computed" strategy requires (please note that the amounts in the first and third rows are in different currencies so they cannot be summed):
> - Table 4: Summary of the synthetic [long forward](../Lecture%20Notes-%20Financial%20Instruments/Teaching%20Note%203%20Swaps-%20Financial%20Instruments/Forward%20Rates%20Agreement.md) position$$
> \begin{array}{lccc}
> \hline
> \text{Today } t = 0 & & \text{In formulas} \\
> \hline
> \text{Borrow in dollars the PV or 1 euro} & & +e^{-r_e} \cdot M_0 \\
> \text{Exchange the amount borrowed into euros} & & \\
> \text{Invest the present value of 1 euro today} & & -e^{-r_e} \\
> \hline
> \text{At maturity } t = T & & \text{In formulas} \\
> \hline
> \text{Pay dollars} & & -M_0 \cdot e^{(r_{US}-r_e) \cdot T} \\
> \text{Exchange the euros received into dollars} & & \\
> \text{Receive 1 euro} & & +1 \\
> \hline
> \end{array}
> $$
> - Finally we can consider the cash flows from both the short position (again,     short since we are selling euros) and the synthetic long (again,     long since we are buying euros) forward position,     which are reported in Table 5. Please note that the amount$M_T$is simply the value,     in dollars,     of 1 euro at time$T$.
> $$
> \begin{array}{lccc}
> \hline
> \text{Amounts in USD} & t = 0 & & t = T \\
> \hline
> \text{Short forward position} & 0 & & F_{\text{quoted}} - M_T \\
> \text{Synthetic long forward position} & 0 & & M_T - F_{\text{computed}} \\
> \text{TOTAL} & 0 & & F_{\text{quoted}} - F_{\text{compute}} > 0 \\
> \hline
> \end{array}
> $$
> - Applying the above formulas to our case the strategy becomes:
> 	- Short a [forward contract](../../Clippings/Forward%20Points%20in%20Currency.md) to sell 1 euro for 1.3960 dollars in one year
> 	- Borrow$e^{−0.0535} · 1.4021 = 0.9479 · 1.4021 = 1.3290$dollars today (October 1st 2008)
> 	- Exchange 1.3290 dollars for euros obtaining 0.9479 euros
> 	- Invest 0.9479 euros at$r_{EUR} = 5.35$%
> - At maturity we will have
> 	- Pay 1 euro (from [short forward](../Lecture%20Notes-%20Financial%20Instruments/Teaching%20Note%203%20Swaps-%20Financial%20Instruments/Forward%20Rates%20Agreement.md) position)
> 	- Receive 1.3960 dollars
> 	- Receive 1 euro (from long synthetic forward position)
> 	- Pay $1.3290 · e^{0.0396} = 1.3827$ dollars
> - The net [cash flow](../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%201%20-%20Purpose%20and%20Structure%20of%20Financial%20Markets/Preview%20of%20the%20Book.md) will be a positive amount equal $1.396 − 1.3827 = 0.0134$
> dollars per euro traded. If we apply the same strategy on$100 m,     the arbitrage is supposed to generate a positive cash flow at maturity equal to $1.337 m.
---
title: Financial Instruments Example Midterm Solutions
cssclasses: academia
tags:
- arbitrage
- binomial-model
- binomial_trees
- black-scholes-model
- bond_valuation
- credit
- credit-derivatives
- equity-derivatives
- european_call_option
- european_put_option
- fixed-income
- fixed-income-derivatives
- fx-derivatives
- hedging-strategies
- interest-rate-derivatives
- markets
- no_arbitrage_price
- option-greeks
- options
- options-pricing
- quantitative-pricing
- risk-management
aliases:
- financial instruments midterm solutions
- option pricing exam
- option valuation
key_concepts:
- Arbitrage pricing theory (APT)
- Binary option price
- Binomial tree models for option pricing
- Binomial tree pricing
- Black-Scholes option pricing model
- Bond valuation example
- Complete markets and replication
- Delta hedging and Greeks calculation
- European call option
- European put option
- Expected Shortfall (ES) and coherent risk measures
- Forward contract pricing
- Heath-Jarrow-Morton (HJM) framework
- Hedging strategies
- Interest rate models and term structure
- Interest rate swaps and swap pricing
- No-arbitrage pricing
- Option Greeks and sensitivity analysis
- Option delta calculation
- Portfolio optimization and mean-variance theory
- Risk-neutral valuation
- Risk-neutral valuation and martingale measures
- Value at Risk (VaR) and risk metrics
---


# Financial Instruments Example Midterm Solutions

## Problem 1 (20 Points)
True-False Questions (There Are 4 Of Them). Grade Depends On Completeness Of Answer.

### (a) (5 points) 
Let's suppose you write a European call option on a stock. To hedge your exposure to the stock you could buy an equivalent number of shares of the stock.

> [!ANSWER]
> Solution: False. You need to match the Delta of the option.

### (b) (5 points)
XYZ airlines is committed to buying one million barrels of jet fuel next quarter. XYZ can hedge this position by going long futures contracts for one million barrels of oil.

> [!ANSWER]
> Solution: False in general. The hedge ratio depends on the relationship between the futures price and the price of jet fuel. This should be checked empirically.

### (c) (5 points)
Some options contracts may increase in value as they approach maturity.

> [!ANSWER]
> Solution: True. A call option with a large dividend yield and a put option that is significantly out of the money both increase in value as they approach maturity.

### (d) (5 points)
The current price of a security is given by the expected future price of that security discounted using the risk-adjusted required rate of return. A forward contract to buy that same security locks in the price to buy the security at maturity. Since risk is eliminated, the forward price should reflect discounting using the risk-free return. The forward price must therefore be lower than the expected future price of the security.

> [!ANSWER]
> Solution: False in general. This depends on the sign of the risk-premium.

## Problem 2 (20 Points) Binomial Trees

Suppose that stock JCH, whose current price is $100, can either increase by u = 1.05 or decrease by d = 1/(1.05) per year for the next 2 years.
The continuously-compounded interest rate is 2% per year.

### (a) (15 points) 
Suppose you are *long* a call option that gives you the option to buy, in two years, *100* shares of JCH stock at a strike price of $95 per share. How would you hedge your exposure to the price of JCH stock over the life of the option? What is the current price of your option position?

> [!ANSWER]
> Solution: The stock price dynamics are given by:
> ! | 500
> 
> To do the hedging and pricing we need all of the Delta's and bond positions. These are:
> 
> $$\Delta_{u}=\frac{15.25-5}{110.25-100}=1$$
> 
> $$B_{u}=e^{-0.02}\times(15.25-1\times110.25)=-93.12$$
>
> so that $c_{u}=1\times105-93.12=11.88$
>
> $$\Delta_{d}=\frac{5-0}{100-90.70}=0.54$$
>
> $$B_{u}=e^{-0.02}\times(5-0.54\times100)=-47.81$$
>
> so that $c_{d}=0.54\times95.24-47.81=3.40$.
>
> $$\Delta=\frac{11.88-3.4}{105-95.24}=0.87$$
>
> $$B=e^{-0.02}\times(11.88-0.87\times105)=-77.72$$
>
> so that c = 0.87 × 100 − 77.72 = 9.11.
>
> The current price of the option is 9.11 and the positions in the stock and bond are given by the Delta's and "B's" above.

### (b) (5 points) 
Consider a *binary* option on JCH stock. Under this option contract the holder of the option receives one share of JCH stock if in two years (the maturity of the option) the stock is trading between $85 and $95. According to your assumptions, what is an appropriate price for this option? (Hint: notice that I only asked you to price the option. No hedging required!)

> [!ANSWER]
> Solution: The payoffs and values of the option are given by:
>
> $$\begin{array}{ccccc}&&V_{uu}=0\\ &&\nearrow&&\\ &&V_u&&\\ &&\nearrow&&\searrow&&\\ V&&&&&V_{ud}=0\\ &&\searrow&&\nearrow&&\\ &&V_d&&\\ &&\searrow&&\\ &&V_{dd}=90.70\end{array}$$
>
> The risk neutral probability of an "up" move is:
>
> $$q^{*}={\frac{e^{0.02}-d}{u-d}}=0.69$$
>
> The price of the option is therefore:
>
> $$V=e^{-0.02\times2}\times(1-0.69)^{2}\times90.70=8.38$$

## Problem 3 (30 Points)

A few years ago your company issued a bond denominated in Euros. The bond has a face value of 1 million Euros and pays semi-annual coupons at an annual rate of 6%. You just made a coupon payment and the bond has one year left to maturity. In other words you owe a coupon payment in 6 months, and payments of coupon and principal in 1 year.

The current exchange rate is 1.3 dollars per Euro (USD/EUR). The current LIBOR rates (in continuously compounded units) are:

 | Maturity | USD | Euro | 
 | ------------ | ------- | -------- | 
 | 6 months | 2% | 2% | 
 | 1 year | 2.5% | 3% | 

### (a) (10 points) 
You would like to hedge your exposure to the Euro using forward contracts. How many and what maturities of forward contracts would you use? What would be the forward prices of these contracts?

> [!ANSWER]
> Solution: The forward prices are:
>
> $$F_{0, 0.5}=1.3\times e^{(0.02-0.02)\times0.5}=1.3$$
>
> and
>
> $$F_{0, 1}=1.3\times e^{(0.025-0.03)\times1}=1.29$$
>
> Hedge: buy 6%/2 × 1 milllion = 30,000 Euros forward at the 6 month rate of 1.3 and buy 1,030,000 Euros forward at the 1 year rate of 1.29.

### (b) (10 points) 
Suppose the day after you signed your forward contract in part (a) above, the spot exchange rate between dollars and Euros is 1.29 dollars per Euro (USD/EUR). Yields (c.c.) in the LIBOR market are now:

 | Maturity | USD | Euro | 
 | ----------------------- | ------- | -------- | 
 | 6 months (less a day) | 2% | 2% | 
 | 1 year (less a day) | 2.5% | 3.1% | 

What would be the market values of the forward contracts you signed in part (a)? (Assume that there are 360 days in a year.)

> [!ANSWER]
> Solution:
> The new forward rates for the maturities from part (a) are now:
>
> $$F_{1/360, 0.5}=1.29$$
>
> and
>
> $${F}_{{{1}\text{/}{360}},{1}}={1.29}\times{e}^{{{\left({0.025}-{0.031}\right)}\times{359}\text{/}{360}}}={1.28}$$
>
> The value of the forward contracts from part(a) are now:
>
> $${V}_{{{1}\text{/}{360}, {0.5}}}={e}^{{-{0.02}\times{179}\text{/}{360}}}\times{30},{000}\times{\left({1.29}\text{-}{1.30}\right)}=\text{-}{297.03}$$
>
> and
>
> $$V_{1/360, 1} = e^{−0.025×359/360} × 1,030,000 × (1.28 − 1.29) = -11,263.69$$

### (c) (10 points) 
Let's return to the setting of part (a) where you owe a coupon payment in six months, and coupon and principal payments in one year. An investment bank offers you a contract where they will pay the Euros under your bond obligation. In return, you will owe the bank US dollar denominated payments on a bond with one year to maturity, face value of $1.29 million, and semiannual coupon payments at an annual rate of 6%. Would you enter into this contract to hedge your exposure to the Euro? Why or why not?

> [!ANSWER]
> Solution: The present value of what you currently owe is (in US Dollars):
>
> $$V_{Euro Bond} = 1.3 × (e^{−0.02×0.5} × 30,000 + e^{−0.03} × 1,030,000) = 1,338,038.51$$
>
> The semiannual coupon from the offer is: $1,290,000 × 0.03 = 38,700$
>
> The present value of the offer is:
>
> $$V_{Offer} = e^{−0.02×0.5} × 38,700 + e^{−0.025} × [1,290,000 + 38,700] = 1,327,745.91$$
>
> Since I would owe the bank less than what I would receive, I would enter the agreement.

## Problem 4 (20 Points)

Through your investment in an index fund you are currently long 1,000 units of the S&P500. In addition, you are long a put option on the S&P500. The terms of this put option are:
- Underlying index: S&P500.
- Current value of the S&P500: $1,200.
- Number of units of the underlying index: 750.
- Strike price of the put option (per unit of underlying): $1,000.
- Maturity of the put option: 2 years.

### (a) (5 points) 
Why might you be holding the put option contract along with the S&P 500 index?

> [!ANSWER]
> Solution: You would like to participate in the upside of the S&P500 but would like some down-side protection.

### (b) (15 points) 
Make the following additional assumptions:
- Risk-free rate: 1% continuously compounded.
- Dividend yield for the S&P500: 0%.
- Volatility of the S&P500: 30%. This will be constant over the life of the option.

Under these assumptions, what should be the value of your portfolio? What is the delta of your portfolio with respect to the S&P500?

> [!ANSWER]
> Solution: Black-Scholes quantities:
>
> $$d_1=\frac{\ln(1200/1000)+(0.01+0.3[^2]/2)\times2}{0.3\times\sqrt{2}}=0.69$$
>
> $$d_2=0.69-0.3\times\sqrt{2}=0.26$$
>
> $$N(-d_1)=0.25$$
>
> $$N(-d_2)=0.4$$
>
> The value of a put option on one unit of the index:
>
> $$p=1,000\times e^{-0.01\times2}\times0.4-1,200\times0.25=93.28$$
>
> Hence the value of your portfolio is:
>
> $$1,000\times1,200+750\times93.28=1,269,959.22$$
>
> The delta of your portfolio is:
>
> $$1,000-750\times0.25=815.94$$

# Financial Instruments Midterm Solutions 2022

## Problem 1 (15 Points) 
True-False Questions (There Are 3 Of Them). Grade Depends On Completeness Of Answer.

### (a) (5 points) 
In a Foreign Exchange forward contract, the value of the forward contract is always positive.

> [!ANSWER]
> False: the value of a forward exchange contract is given by
>
> $$f_{t, T}=M(t)\cdot e^{-r_{e}\cdot(T-t)}-F_{0, T}\cdot e^{-r_{\mathrm{g}}\cdot(T-t)}=e^{-r_{\mathrm{g}}\cdot(T-t)}\cdot[F_{t, T}-F_{0, T}]$$
>
> where $M(t)$ is the spot rate (e.g. USD / EUR exchange rate, that is the price in USD of 1 euro) at time $t$, $r^e$ is the continuously compounded EUR risk free rate and $r_\text{usd}$ is the continuously compounded USD risk free rate. As we know, at inception, $f_{0, T} = 0$, since $F_{0, T} = M_0 \cdot e^{(r−r_e)·T}$. At any time $t$ such that $0 < t < T$ the value of the contract can actually be either positive or negative. If, for example, the dollar appreciates, that is if $M_t$ falls significantly, then the value of the contract can become negative.
>
> An intuitive way of thinking about it is that as at time $t = 0$ we have signed a contract to buy 1 EUR in $T$ years, at a given price $F_{0, T}$, but now the market conditions are much more favorable (as $F_{t, T} < F_{0, T}$) therefore under the initial contract we have agreed to pay "too much" for a EUR. This means that the value of our position is negative.

### (b) (5 points) 
IT IS POSSIBLE TO CALCULATE THE SWAP RATE $S$ OF A SWAP ON ANY UNDERLYING FACTOR $X_T$ (E.G. EXCHANGE RATES, GOLDS, OIL) WITH SPOT RATE $X_T$ AND NET CASH FLOWS $X_T - S$ FROM THE CURRENT FORWARD RATES $F_{T, T}$ ON THE FACTOR ITSELF

> [!ANSWER]
> True: One example we know well is a Foreign Exchange swap. The swap requires an exchange of cash flows in two different currencies.
> At each time period, the total cash flow can be considered as a purchase of some units of foreign currency in exchange for some known quantity of home currency. In other words each cash flow represents a forward position (purchase or sale, depending on the swap) on the foreign currency. In order to prevent arbitrage opportunities therefore the swap rate has to be such that the sum of the values of the various forward positions is equal to the value of the swap. Given this it is therefore possible to compute the swap rate $K$ from the current forward curve. 
>
> [The following example was not required to get full credit]. Consider a simple 3 years swap that requires to pay $c = 8$ USD and to receive $K$ EUR at the end of each year (we don't consider the exchange of principal for simplicity).
> The cash flows will be
>
> $$\begin{array}{llr}\text{Maturity}&\text{USD}&\text{BPD}\\1\text{year}&2\%&3\%\\2\text{years}&3\%&3\%\end{array}$$
>
> The two streams of payments (two columns) are two annuities in two different currencies.
> One way to compute the value of $K$ is to find a number such that the value of the two annuities (in the same currency) matches. To do this we need the zeros in both currencies and the spot exchange rate. An alternative way is to consider Table (1) row by row. Each row represents the purchase of $K$ EUR for 8 USD, or in other words the purchase of 1 EUR for $\frac{8}{K}$ dollars. Therefore each row represents a long forward position in EUR, with a delivery price equal to $\frac{8}{K}$. Let's set $K^\text{fwd} = \frac{8}{K}$. Given the current forward curve we can compute the value of each forward position in Table (1) using
>
> $$f_{0, T}=e^{-r_{5}\cdot T}\cdot\left(F_{0, T}-K^\text{fwd}\right)$$
>
> We will then obtain $f_{0, 1}$, $f_{0, 2}$ and $f_{0, 3}$. Now since the swap is a sum of three forward positions, its value has to be equal to the sum of the values of each forward contract. In addition, at inception the swap rate is such that the value of the SWAP is 0. Therefore by setting
>
> $$f_{0, 1}+f_{0, 2}+f_{0, 3}=0$$
>
> We have an equation in 1 unknown ($K$), that we can easily solve. We can apply the same reasoning to any kind of swap (commodity, equity, etc.).

### (c) (5 points)
THE CURRENT EXCHANGE RATE BETWEEN THE UNITED STATES AND CANADA IS 1.02 US DOLLARS per Canadian dollar. The one-year forward exchange rate is 1.03 US dollars per Canadian dollar. The market must be expecting that over the next year the US dollar will depreciate relative to the Canadian dollar.

! | 500

> [!ANSWER]
> False: The forward exchange rate is determined by the current exchange rate and the interest rate differential between the US and Canada. Further the forward rate reflects both expectations and risk premia.

## Problem 2 (25 Points) Binomial Trees

SUPPOSE THAT STOCK XYZ, WHOSE CURRENT PRICE IS $50, CAN EITHER INCREASE BY $U = 1.1$ OR DECREASE BY ${} D = \frac{1}{1.1} {}$ EACH YEAR OVER THE NEXT 2 YEARS. THE CONTINUOUSLY-COMPOUNDED INTEREST RATE IS 1% PER YEAR

! | 500

### (a) (10 points) 
WHAT IS THE NO-ARBITRAGE PRICE OF A EUROPEAN PUT OPTION WITH STRIKE PRICE OF $48 AND MATURITY OF 2 YEARS

> [!ANSWER]
> Solution: Dynamics for the stock price and option payoff:
> 
> - The risk-neutral probability of an "up" move is:
>   - $q' = \frac{e^{r\delta t} - d}{u - d} = \frac{e^{1\%} - 1/1.1}{1.1 - 1/1.1} = 0.5288$
>
> - The price of the option at time zero is therefore:
>   - $p_0 = e^{-0.01\times2}(1 - 0.5288) \times 6.78 = 1.43$
>
> - Consider now an 2-year *look-back* call option on the stock with a strike price of $50.
>   - With this option, at maturity the buyer as the option to pay the strike price and receive the *maximum* value the stock achieves during the life of the option.
>   - The maximum stock price, $S_{max}$ across paths and value of the option are:
>
> - Since we need to replicate the option to answer the question below, let's price the option with replication. The delta and bond positions at each node are given by:
>   - $\Delta_{1, u} = \frac{V_{2, uu} - V_{2, ud}}{S_{2, uu} - S_{2, ud}} = \frac{10.5 - 5}{60.5 - 50} = 0.5238$
>   - $B_{1, u} = e^{-r\delta t}(V_{2, uu} - \Delta_{1, u}S_{2, uu}) = e^{0.01}(10.5 - 0.5238 \times 60.5) = -20.98$
>   - $V_{1, u} = \Delta_{1, u} \times S_{1, u} + B_{1, u} = 0.5238 \times 55 - 20.98 = 7.8299$
>   - $\Delta_0 = \frac{V_{1, u} - V_{1, d}}{S_{1, u} - S_{1, d}} = \frac{7.8299 - 0}{55 - 45.45} = 0.8203$
>   - $B_0 = e^{-r\delta t}(V_{1, u} - \Delta_0S_{1, u}) = e^{-0.01}(7.8299 - 0.8203 \times 55) = -36.9142$
>   - $V_0 = \Delta_0 \times 50 + B_0 = 0.8203 \times 50 - 36.9142 = 4.0995$
>
> For each Capital Protected Note hold 1.1347 1-year options.
> To hedge this note we would hold the short data option in the proportion:
> For each Capital Protected Note hold 1.1347 1-year options.

### (d) (5 points)
IF IMMEDIATELY AFTER YOU ENTER INTO THE HEDGING POSITIONS OF PART (B), THE S&P500 INCREASES IN PRICE. DESCRIBE $IN$ $WORDS$ THE DIRECTIONS IN WHICH YOU WOULD HAVE TO CHANGE YOUR POSITIONS AND WHY. (INTUITION ONLY, NO CALCULATIONS HERE)

> [!ANSWER]
> Solution: Yes because the Delta of each position increases but not by the same amount.

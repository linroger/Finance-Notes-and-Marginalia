---
title: '# Lecture Notes 4-Mechanics of Futures Trading and Fixed Income Derivatives'
cssclasses: academia
tags:
  - derivatives
  - fixed_income
  - futures_trading
  - limit_orders
  - market_orders
  - stop_orders
aliases:
  - Futures and Derivatives
  - Lecture 4
  - Trading Mechanics
key_concepts:
  - Exchange-traded futures options
  - Futures trading mechanics
  - Long and short positions
  - Managing interest rate risk
  - Types of futures orders
---

# # Lecture Notes 4-Mechanics of Futures Trading and Fixed Income Derivatives

## 1. Introduction to Futures Trading and Fixed Income Derivatives

- [[6. A Brief Introduction to Stochastic Calculus|Fixed income derivatives]],  including [[Futures Not Subject to Cash-And-Carry|futures]] and options,  are essential tools for [[Key Rates O1s Durations and Hedging|hedging]],  speculation,  and [[Lecture Notes 4-Mechanics of Futures Trading and Fixed Income Derivatives|managing interest rate risk]].
- This lecture focuses on the mechanics of [[Futures Mechanics|futures trading]],  the types of orders used,  the role of clearing corporations,  [[Lecture 6-[[Lecture 6-Leverage, Tail Risk, Volatility Products|Leverage]], Tail Risk, Volatility Products#6.1.3 [[Case Study Mf Globals Repo-To-Maturity Trades|Margin requirements]]|[[Case Study Mf Globals Repo-To-Maturity Trades|margin requirements]]]],  and the structure of the over-the-counter (OTC) market for [[6. A Brief Introduction to Stochastic Calculus|fixed income derivatives]].
- We will also explore exchange-traded [[Futures Not Subject to Cash-And-Carry|futures]] options,  including options on Treasury bond [[Futures Not Subject to Cash-And-Carry|futures]] and [[Convexity-Adjusted Models for LIBOR Forwards Qu|Eurodollar futures]],  and their applications in managing financial risks.

## 2. Mechanics of Futures Trading

### 2.1 Types of Orders in Futures Trading

- When a trader wants to buy or sell a [[Futures Not Subject to Cash-And-Carry|futures]] contract,  they must specify the price and conditions under which the order is to be executed. These conditions are communicated to a [[Futures Not Subject to Cash-And-Carry|futures]] broker.
- There are several types of orders,  each with unique characteristics,  advantages,  and risks:

#### 2.1.1 Market Orders
- A **market order** is executed at the best available price as soon as it reaches the trading pit.
  - *Advantages*: Immediate execution.
  - *Risks*: Adverse price movements may occur between the time the order is placed and executed.

#### 2.1.2 Limit Orders
- A **limit order** specifies a price limit for the transaction.
  - A **buy limit order** allows the purchase of a [[Futures Not Subject to Cash-And-Carry|futures]] contract only at the designated price or lower.
  - A **sell limit order** allows the sale of a [[Futures Not Subject to Cash-And-Carry|futures]] contract only at the designated price or higher.
  - *Advantages*: Provides price control.
  - *Risks*: The order may not be executed if the market does not reach the specified price.

#### 2.1.3 Stop Orders
- A **stop order** becomes a market order once the market reaches a designated price.
  - A **buy stop order** is triggered when the market rises to or above the designated price.
  - A **sell stop order** is triggered when the market falls to or below the designated price.
  - *Advantages*: Useful for preserving profits or minimizing losses.
  - *Risks*: Abrupt price changes may lead to premature execution,  and the execution price is uncertain.

#### 2.1.4 Stop-Limit Orders
- A **stop-limit order** is a hybrid of a stop order and a limit order.
  - Once the stop price is reached,  the order becomes a limit order rather than a market order.
  - *Advantages*: Limits the execution price after the stop is triggered.
  - *Risks*: The order may not be executed if the limit price is not reached.

#### 2.1.5 Market-if-Touched Orders
- A **market-if-touched order** becomes a market order if a designated price is reached.
  - A **buy market-if-touched order** is triggered when the market falls to a given price.
  - A **sell market-if-touched order** is triggered when the market rises to a given price.
  - *Purpose*: Designed to enter a position at an acceptable price.

#### 2.1.6 Other Specialized Orders
- **Opening Orders**: Executed only during the opening range of the trading day.
- **Closing Orders**: Executed only during the closing range of the trading day.
- **Discretionary Orders**: Gives the broker discretion to achieve a better price within a specified range.
- **Not Held Orders**: Grants the broker full discretion over whether to fill the order.
- **Fill-or-Kill Orders**: Must be executed immediately or canceled.
- **One-Cancels-Other Orders**: A pair of orders where the execution of one cancels the other.

### 2.2 Taking and Liquidating a Position

- A trader can take a position in the [[Futures Not Subject to Cash-And-Carry|futures]] market by:
  - **Buying a [[Futures Not Subject to Cash-And-Carry|futures]] contract**: This creates a **[[Chapter 4 - Futures: Hedging and Speculation|long position]]**.
  - **Selling a [[Futures Not Subject to Cash-And-Carry|futures]] contract**: This creates a **short position**.
- Positions can be liquidated in two ways:
  1. **Offsetting the position**: Taking an opposite position in the same contract (e.g.,  selling a [[Chapter 4 - Futures: Hedging and Speculation|long position]] or buying a short position).
  1. **Waiting until the delivery date**: Accepting or delivering the underlying instrument at the agreed-upon price.

- For contracts that do not involve physical delivery (e.g.,  [[Convexity-Adjusted Models for LIBOR Forwards Qu|Eurodollar futures]]),  settlement is in cash at the settlement price on the delivery date.

### 2.3 The Role of the Clearing Corporation

- The clearing corporation acts as an intermediary between buyers and sellers in the [[Futures Not Subject to Cash-And-Carry|futures]] market.
  - It becomes the buyer for every seller and the seller for every buyer.
  - This eliminates counterparty risk and allows traders to liquidate positions without involving the original counterparty.
- However,  traders remain exposed to the risk of default by their [[Futures Not Subject to Cash-And-Carry|futures]] broker. It is crucial to ensure that the broker has adequate capital to mitigate this risk.

### 2.4 Margin Requirements

- **Initial Margin**: A minimum deposit required to open a position,  specified by the exchange.
  - This serves as a good faith deposit and can be in the form of Treasury bills.
- **Maintenance Margin**: The minimum equity level required to maintain a position.
  - If the equity falls below this level due to adverse price movements,  additional margin ([[Repurchase Agreements|variation margin]]) must be deposited.
- **[[Repurchase Agreements|Variation Margin]]**: The amount required to restore equity to the initial margin level.
  - Must be deposited in cash.
- [[Lecture 6-[[Lecture 6-Leverage, Tail Risk, Volatility Products|Leverage]], Tail Risk, Volatility Products#6.1.3 [[Case Study Mf Globals Repo-To-Maturity Trades|Margin requirements]]|[[Case Study Mf Globals Repo-To-Maturity Trades|margin requirements]]]] vary based on:
  - The type of position (e.g.,  outright long/short vs. spread).
  - The purpose of the trade (e.g.,  speculative vs. [[Key Rates O1s Durations and Hedging|hedging]]).
  - The perceived risk of the contract.

## 3. Exchange-Traded Futures Options

### 3.1 Overview of Futures Options

- [[Futures Not Subject to Cash-And-Carry|Futures]] options are similar to traditional options but differ in that the underlying instrument is a [[Futures Not Subject to Cash-And-Carry|futures]] contract rather than a spot security.
- Types of [[Futures Not Subject to Cash-And-Carry|futures]] options:
  - **Call Options**: Grant the right to buy the underlying [[Futures Not Subject to Cash-And-Carry|futures]] contract at a specific price.
  - **Put Options**: Grant the right to sell the underlying [[Futures Not Subject to Cash-And-Carry|futures]] contract at a specific price.
- When exercised:
  - A call option results in a long [[Futures Not Subject to Cash-And-Carry|futures]] position for the buyer and a short [[Futures Not Subject to Cash-And-Carry|futures]] position for the seller.
  - A put option results in a short [[Futures Not Subject to Cash-And-Carry|futures]] position for the buyer and a long [[Futures Not Subject to Cash-And-Carry|futures]] position for the seller.
- The resulting [[Futures Not Subject to Cash-And-Carry|futures]] positions are subject to daily marking to market.

### 3.2 Options on Treasury Bond Futures

- Options on Treasury bond [[Futures Not Subject to Cash-And-Carry|futures]] are based on the price of a fictitious 20-year,  6% Treasury bond.
- The nominal size of the contract is $100,  000.
- Premiums are quoted in points and 64ths of a point.
  - Example: A premium of 1-10 implies a price of $1.15625% of face value,    or $1,  156.25.
- Flexible Treasury [[Futures Not Subject to Cash-And-Carry|futures]] options allow customization of strike prices,  expiration dates,  and exercise types (American or European).

### 3.3 Options on Eurodollar Futures

- These options are based on the quoted [[Convexity-Adjusted Models for LIBOR Forwards Qu|Eurodollar futures]] price (100 minus the annualized yield).
- Contract size: $1 million.
- Premiums are quoted in basis points.
  - Example: A premium of 20 (0.20) implies a price of $500.
- Applications:
  - **[[Key Rates O1s Durations and Hedging|Hedging]] floating-rate liabilities**: Institutions can buy puts to cap interest rate expenses.
  - **[[Key Rates O1s Durations and Hedging|Hedging]] floating-rate assets**: Investors can buy calls to offset lower interest income when rates fall.

## 4. OTC Fixed Income Derivatives

### 4.1 Structure of the OTC Market

- The OTC market lacks a central marketplace; transactions occur directly between buyers and sellers.
- Market participants include:
  - **Market-Makers**: Large [[An Asset Allocation Primer|investment]] and commercial banks that provide [[Class Note 10 Liquidity and Class Note 10 Liquidity and Liquidity Managementliquidity management|liquidity]].
  - **Brokers**: Facilitate transactions by connecting buyers and sellers.
- Key differences from exchange-traded markets:
  - No clearinghouse,  so counterparty [[Quantitative Trading Strategies Lecture Notes|credit risk]] is significant.
  - Greater flexibility in contract terms,  sizes,  and expiration dates.

### 4.2 Advantages and Disadvantages of OTC Markets

- **Advantages**:
  - Customization of contracts to meet specific needs.
  - Ability to trade a wide range of instruments,  including options on LIBOR,  [[Class Note 12 - Commercial Paper#Class Note 12 – Commercial Paper|Commercial Paper]],  and mortgage securities.
- **Disadvantages**:
  - [[Hedge Fund Replication and Strategy Indexes|Lack of transparency]] and price visibility.
  - Counterparty [[Quantitative Trading Strategies Lecture Notes|credit risk]].

## 5. Summary and Key Takeaways

- [[Futures Mechanics|Futures trading]] involves various types of orders,  each with unique risks and benefits.
- The clearing corporation plays a critical role in mitigating counterparty risk in exchange-traded markets.
- [[Lecture 6-[[Lecture 6-Leverage, Tail Risk, Volatility Products|Leverage]], Tail Risk, Volatility Products#6.1.3 [[Case Study Mf Globals Repo-To-Maturity Trades|Margin requirements]]|[[Case Study Mf Globals Repo-To-Maturity Trades|margin requirements]]]] ensure that traders maintain sufficient equity to cover potential losses.
- [[Futures Not Subject to Cash-And-Carry|Futures]] options provide flexibility for [[Key Rates O1s Durations and Hedging|hedging]] and speculation,  with applications in [[Lecture Notes 4-Mechanics of Futures Trading and Fixed Income Derivatives|managing interest rate risk]].
- The OTC market offers customization but comes with significant counterparty risk and reduced transparency.

By understanding these mechanics and instruments,  traders and institutions can effectively manage risk and optimize their financial strategies.

# Lecture Notes: OTC Derivatives,  Caps,  Floors,  and Futures Pricing

## 1. Introduction to OTC Derivatives and Interest Rate Risk Management

- Over-the-counter (OTC) [[Chapter 9 Arbitrage and Hedging With Options|derivatives]] are [[A Practical Guide for Actuaries and other Business Professionals.|financial instruments]] traded directly between two parties,  without the involvement of an exchange.
- These instruments,  including [[A Guide to the Front End and [[Basis Swaps|Basis Swap]] Markets#[[EURIBOR Forward Rate Agreements and Futures|Forward Rate Agreements]] (FRAs) [[Overview of Financial Markets|Overview]]|[[EURIBOR Forward Rate Agreements and Futures|Forward Rate Agreements]]]] (FRAs),  caps,  and [[Caps and Floors|floors]],  are widely used for [[Lecture Notes 4-Mechanics of Futures Trading and Fixed Income Derivatives|managing interest rate risk]].
- Unlike exchange-traded [[Chapter 9 Arbitrage and Hedging With Options|derivatives]],  OTC [[Chapter 9 Arbitrage and Hedging With Options|derivatives]] are customizable but come with counterparty risk and [[Class Note 10 Liquidity and Class Note 10 Liquidity and Liquidity Managementliquidity management|liquidity]] constraints.
- This lecture will cover:
  - The mechanics and applications of [[Interest Rate Derivatives-An Introduction to the  Pricing of Caps and Floors|caps and floors]] on LIBOR.
  - The structure and [[Arbitrage Pricing of Derivatives|pricing]] of [[A Guide to the Front End and [[Basis Swaps|Basis Swap]] Markets#[[EURIBOR Forward Rate Agreements and Futures|Forward Rate Agreements]] (FRAs) [[Overview of Financial Markets|Overview]]|[[EURIBOR Forward Rate Agreements and Futures|Forward Rate Agreements]]]] (FRAs).
  - The [[Arbitrage Pricing of Derivatives|pricing]] of [[Mathematics of the Financial Markets|futures contracts]] and their [[An Asset Allocation Primer|portfolio]] applications.

## 2. Mechanics of OTC Derivatives

### 2.1 Counterparty Risk in OTC Markets

- Counterparty risk is a significant concern in [[A Survey of the Micro structure of Fixed-Income Markets|OTC markets]],  as there is no central clearinghouse to guarantee transactions.
- Institutions mitigate counterparty risk in several ways:
  - **Creditworthiness Requirements**: Some institutions only transact with major entities that have sound credit ratings.
  - **Collateral Posting**: Counterparties may be required to post collateral immediately after the transaction,  similar to initial margin in [[Contango And Backwardation In Arbitrage-Free Futures-Markets|futures markets]].
  - **[[Repurchase Agreements|Variation Margin]]**: Institutions reserve the right to call for additional collateral if the market moves against the counterparty.
- While these measures do not eliminate counterparty risk entirely,  they are sufficient for a large number of institutions to participate in the OTC market.

### 2.2 Liquidity Constraints in OTC Markets

- [[Class Note 10 Liquidity and Class Note 10 Liquidity and Liquidity Managementliquidity management|Liquidity]] in [[A Survey of the Micro structure of Fixed-Income Markets|OTC markets]] can be constrained due to the non-assignable nature of most transactions.
  - For example,  an option seller cannot transfer the contingent liability to a third party without the buyer's permission.
  - To offset a short option position,  the seller may need to buy a similar option from a third party,  which introduces risks if the offsetting option is not identical or if the counterparty's credit is questionable.
- Non-standardization of contracts contributes to these [[Class Note 10 Liquidity and Class Note 10 Liquidity and Liquidity Managementliquidity management|liquidity]] issues but also provides flexibility in structuring agreements.

## 3. Caps and Floors on LIBOR

### 3.1 Overview of Caps and Floors

- [[Interest Rate Derivatives-An Introduction to the  Pricing of Caps and Floors|Caps and floors]] are OTC options designed to manage [[Analysis of Fixed Income Securities|interest rate risk]] on the short end of the yield curve.
  - A **cap** on [[A Guide to the Front End and [[Basis Swaps|Basis Swap]] Markets#[[Short-Term Rates and the Transition from LIBOR|London Interbank Offered Rate]] (LIBOR)|LIBOR]] is essentially a series of put options on LIBOR-based debt.
  - A **floor** on [[A Guide to the Front End and [[Basis Swaps|Basis Swap]] Markets#[[Short-Term Rates and the Transition from LIBOR|London Interbank Offered Rate]] (LIBOR)|LIBOR]] is essentially a series of call options on LIBOR-based debt.
- The buyer of a cap or floor pays an upfront premium and holds most of the rights in the contract,  while the seller receives the premium and is obligated to perform under the contract terms.

### 3.2 Mechanics of Caps

- A cap consists of multiple reset dates,  typically aligned with the interest accrual periods of the underlying LIBOR-based debt.

> [!NOTE]
> - **Example**: A five-year,  $100 million cap on three-month [[A Guide to the Front End and [[Basis Swaps|Basis Swap]] Markets#[[Short-Term Rates and the Transition from LIBOR|London Interbank Offered Rate]] (LIBOR)|LIBOR]] struck at 2%.
>   - The contract specifies 20 reset dates (one every three months).
>   - On each reset date,  the three-month [[A Guide to the Front End and [[Basis Swaps|Basis Swap]] Markets#[[Short-Term Rates and the Transition from LIBOR|London Interbank Offered Rate]] (LIBOR)|LIBOR]] rate is compared to the 2% strike rate:
> 	- If [[A Guide to the Front End and [[Basis Swaps|Basis Swap]] Markets#[[Short-Term Rates and the Transition from LIBOR|London Interbank Offered Rate]] (LIBOR)|LIBOR]] ≤ 2%,  no payment is made.
> 	- If [[A Guide to the Front End and [[Basis Swaps|Basis Swap]] Markets#[[Short-Term Rates and the Transition from LIBOR|London Interbank Offered Rate]] (LIBOR)|LIBOR]] > 2%,  the cap seller pays the buyer the monetary value of the excess LIBOR.
>
> - **Payoff Calculation**:
>   - For a 90-day interest accrual period,  the value of each basis point is:
> $$0.0001 \times 100,   000,   000 \times \frac{90}{360} = 2,   500 \,    \text{USD}$$
>   - If [[A Guide to the Front End and [[Basis Swaps|Basis Swap]] Markets#[[Short-Term Rates and the Transition from LIBOR|London Interbank Offered Rate]] (LIBOR)|LIBOR]] = 2.50%,  the payoff is:
> $$\text{Payoff} = (2.50\% - 2.00\%) \times 100 \,    \text{basis points} \times 2,   500 = 125,   000 \,    \text{USD}$$
>   - If [[A Guide to the Front End and [[Basis Swaps|Basis Swap]] Markets#[[Short-Term Rates and the Transition from LIBOR|London Interbank Offered Rate]] (LIBOR)|LIBOR]] = 4.00%,  the payoff is:
> $$\text{Payoff} = (4.00\% - 2.00\%) \times 100 \,    \text{basis points} \times 2,   500 = 500,   000 \,    \text{USD}$$
>
> - Payments are typically made at the end of the interest accrual period.
>

### 3.3 Mechanics of Floors

- [[Caps and Floors|Floors]] operate similarly to caps but provide protection against falling [[Interest Rate Quotations|interest rates]].

> [!NOTE]
> - **Example**: A $25 million,  seven-year floor on six-month [[A Guide to the Front End and [[Basis Swaps|Basis Swap]] Markets#[[Short-Term Rates and the Transition from LIBOR|London Interbank Offered Rate]] (LIBOR)|LIBOR]] struck at 3%.
>   - The contract specifies 14 reset dates (one every six months).
>   - On each reset date,  the six-month [[A Guide to the Front End and [[Basis Swaps|Basis Swap]] Markets#[[Short-Term Rates and the Transition from LIBOR|London Interbank Offered Rate]] (LIBOR)|LIBOR]] rate is compared to the 3% strike rate:
> 	- If [[A Guide to the Front End and [[Basis Swaps|Basis Swap]] Markets#[[Short-Term Rates and the Transition from LIBOR|London Interbank Offered Rate]] (LIBOR)|LIBOR]] ≥ 3%,  no payment is made.
> 	- If [[A Guide to the Front End and [[Basis Swaps|Basis Swap]] Markets#[[Short-Term Rates and the Transition from LIBOR|London Interbank Offered Rate]] (LIBOR)|LIBOR]] < 3%,  the floor seller pays the buyer the monetary value of the shortfall.
>
> - **Payoff Calculation**:
>   - For a 180-day interest accrual period,  the value of each basis point is:
> $$0.0001 \times 25,   000,   000 \times \frac{180}{360} = 1,   250 \,    \text{USD}$$
>   - If [[A Guide to the Front End and [[Basis Swaps|Basis Swap]] Markets#[[Short-Term Rates and the Transition from LIBOR|London Interbank Offered Rate]] (LIBOR)|LIBOR]] = 2.50%,  the payoff is:
> $$\text{Payoff} = (3.00\% - 2.50\%) \times 100 \,    \text{basis points} \times 1,   250 = 62,   500 \,    \text{USD}$$
>

### 3.4 Market Participants

- **Market-Makers**: Large [[An Asset Allocation Primer|investment]] and commercial banks dominate the cap and floor market,  providing [[Class Note 10 Liquidity and Class Note 10 Liquidity and Liquidity Managementliquidity management|liquidity]] and [[Arbitrage Pricing of Derivatives|pricing]].
- **End-Users**:
  - Buyers of caps: Institutions exposed to rising [[Volatility and Convexity|short-term rates]] (e.g.,  banks funding short and lending long).
  - Buyers of [[Caps and Floors|floors]]: Institutions exposed to falling rates (e.g.,  borrowers with [[Uses of Interest Rate Swaps|floating-rate debt]] that has a built-in floor).
- **Sellers**:
  - Some sell caps or [[Caps and Floors|floors]] outright for premium income.
  - Others use [[Interest Rate Derivatives-An Introduction to the  Pricing of Caps and Floors|caps and floors]] to hedge or smooth cash flows on other [[Lecture 7-Risk and Return of Bonds|fixed-income instruments]].

## 4. [[A Guide to the Front End and Basis Swap Markets#Forward Rate Agreements (FRAs) Overview|Forward Rate Agreements]] (FRAs)

### 4.1 Overview of FRAs

- FRAs are OTC [[Chapter 9 Arbitrage and Hedging With Options|derivatives]] that function as forward-starting loans without the exchange of principal.
- The cash exchanged at settlement depends only on the difference between the agreed-upon [[A Guide to the Front End and [[Basis Swaps|Basis Swap]] Markets#[[EURIBOR Forward Rate Agreements and Futures|Forward Rate Agreements]] (FRAs) [[Overview of Financial Markets|Overview]]|FRA]] rate and the reference rate (e.g.,  LIBOR).

### 4.2 [[A Guide to the Front End and Basis Swap Markets#Forward Rate Agreements (FRAs) Overview|FRA]] Market Structure

- The [[A Guide to the Front End and [[Basis Swaps|Basis Swap]] Markets#[[EURIBOR Forward Rate Agreements and Futures|Forward Rate Agreements]] (FRAs) [[Overview of Financial Markets|Overview]]|FRA]] market is highly liquid for threeand six-month LIBOR,  with contracts available for settlement starting one month forward and extending up to six months forward.
- Contracts are denoted by the start and end of the interest period they cover (e.g.,  a 1×4 [[A Guide to the Front End and [[Basis Swaps|Basis Swap]] Markets#[[EURIBOR Forward Rate Agreements and Futures|Forward Rate Agreements]] (FRAs) [[Overview of Financial Markets|Overview]]|FRA]] covers the period from one month to four months forward).

### 4.3 [[A Guide to the Front End and Basis Swap Markets#Forward Rate Agreements (FRAs) Overview|FRA]] Settlement

- No money changes hands until the settlement date.
- On the settlement date,  the [[Preview of the Book|cash flow]] is calculated as the present value of the interest differential:
 $\text{Cash Flow} = \text{Notional Amount} \times \frac{\text{(Reference Rate - [[A Guide to the Front End and Basis Swap Markets#Forward Rate Agreements (FRAs) Overview|FRA]] Rate)} \times \text{Days}}{360} \times \frac{1}{(1 + \text{Reference Rate} \times \frac{\text{Days}}{360})}$$

### 4.4 [[A Guide to the Front End and Basis Swap Markets#Forward Rate Agreements (FRAs) Overview|FRA]] vs. Futures

- Unlike [[Futures Not Subject to Cash-And-Carry|futures]],  FRAs are not marked to market daily,  and the profit/loss is a convex function of the underlying rate due to present valuing.
- Buyers of FRAs benefit from rising rates,  while sellers benefit from falling rates.

## 5. Pricing Futures Contracts

### 5.1 Arbitrage and the Law of One Price

- [[Futures Not Subject to Cash-And-Carry|Futures]] prices are determined by [[Arbitrage Pricing of Derivatives|arbitrage]],  ensuring that no [[Arbitrage|risk-free profit]] opportunities exist.
- The [[Pricing Forwards, Futures, Bonds, Swaps, Swaptions, Caps and Floors under No-Arbitrage and Risk-Neutral Pricing|law of one price]] states that identical cash flows must have the same price,  regardless of how they are created.

### 5.2 Cash-and-Carry Arbitrage

> [!NOTE]
> - **Example**: A 20-year,  $100 par value bond with a 12% coupon is selling at par. The three-month interest rate is 8% per year.
>   - If the [[Futures Price and the Quality Option Before E|futures price]] is 107:
> 	- Sell the [[Futures Not Subject to Cash-And-Carry|futures]] contract at 107.
> 	- Borrow $100 for three months at 8%.
> 	- Buy the bond for $100.
> 	- At settlement,  deliver the bond and repay the loan:
> 	  - Receive $107 from the [[Futures Not Subject to Cash-And-Carry|futures]] contract.
> 	  - Pay $102 (loan principal + interest).
> 	  - Profit = $107 - $102 = $5.

- [[Arbitrage Pricing of Derivatives|Arbitrage]] forces the [[Futures Price and the Quality Option Before E|futures price]] to converge to its fair value.

### 5.3 Reverse Cash-and-Carry Arbitrage

> [!NOTE]
>
> - If the [[Futures Price and the Quality Option Before E|futures price]] is 92:
>   - Buy the [[Futures Not Subject to Cash-And-Carry|futures]] contract at 92.
>   - Short the bond for $100.
>   - Invest $100 for three months at 8%.
>   - At settlement,  buy the bond to cover the short position:
> 	- Pay $95 (bond price + [[Intra-Year Compounding and Day-Count|accrued interest]]).
> 	- Receive $102 ([[An Asset Allocation Primer|investment]] principal + interest).
> 	- Profit = $102 - $95 = $7.
>

- Again,  [[Arbitrage Pricing of Derivatives|arbitrage]] eliminates the profit opportunity.

### 5.4 Equilibrium Futures Price

- The equilibrium [[Futures Price and the Quality Option Before E|futures price]] eliminates [[Class Note 13 The LTCM Meltdown|arbitrage opportunities]]:
 $\text{Futures Price} = \text{Spot Price} \times (1 + \text{Risk-Free Rate} \times \text{Time to Maturity})$$

## 6. Summary and Key Takeaways

- OTC [[Chapter 9 Arbitrage and Hedging With Options|derivatives]] like caps,  [[Caps and Floors|floors]],  and FRAs provide flexibility in [[Lecture Notes 4-Mechanics of Futures Trading and Fixed Income Derivatives|managing interest rate risk]] but come with counterparty risk and [[Class Note 10 Liquidity and Class Note 10 Liquidity and Liquidity Managementliquidity management|liquidity]] constraints.
- [[Interest Rate Derivatives-An Introduction to the  Pricing of Caps and Floors|Caps and floors]] are essential tools for institutions exposed to [[Fixed Income Versus Equity Derivatives|interest rate volatility]].
- FRAs are forward-starting loans that allow participants to hedge or speculate on future [[Interest Rate Quotations|interest rates]].
- [[Futures Not Subject to Cash-And-Carry|Futures]] prices are determined by [[Arbitrage Pricing of Derivatives|arbitrage]],  ensuring that they reflect fair value based on the [[Pricing Forwards, Futures, Bonds, Swaps, Swaptions, Caps and Floors under No-Arbitrage and Risk-Neutral Pricing|law of one price]].

By understanding these instruments and their [[Chinese Financial System|pricing mechanisms]],  market participants can effectively manage risk and exploit [[Class Note 13 The LTCM Meltdown|arbitrage opportunities]].

# Lecture Notes: Controlling Interest-Rate Risk with Futures and Options

## 1. Introduction to Interest-Rate Risk Management

- Interest-rate risk is a critical concern for [[An Asset Allocation Primer|portfolio]] managers,  as changes in [[Interest Rate Quotations|interest rates]] can significantly impact the value of fixed-income securities.
- Derivative instruments,  such as [[Futures Not Subject to Cash-And-Carry|futures]] and options,  provide powerful tools for managing this risk.
- This lecture focuses on:
  - The theoretical [[Arbitrage Pricing of Derivatives|pricing]] of [[Mathematics of the Financial Markets|futures contracts]].
  - The concept of carry and its role in [[Chapter 3 - Forward and Futures Prices|futures pricing]].
  - Applications of [[Mathematics of the Financial Markets|futures contracts]] in [[The Impact of Option Strategies in Financial  Portfolios Performance|portfolio management]],  including [[Key Rates O1s Durations and Hedging|duration]] control,  [[Key Rates O1s Durations and Hedging|hedging]],  [[Lecture 2- [[Lecture 2- Asset Allocation with Multiple Risky Assets|Asset Allocation]] with [[Lecture 2- Asset Allocation with Multiple Risky Assets|Multiple Risky Assets]]|[[Lecture 2- Asset Allocation with Multiple Risky Assets|asset allocation]]]],  and [[Hedge Funds Alpha Beta and Strategy Indexes 287|portable alpha]] strategies.

## 2. Theoretical Futures Pricing and the Concept of Carry

### 2.1 Deriving the Theoretical Futures Price
- The theoretical [[Futures Price and the Quality Option Before E|futures price]] is derived using [[Forward Contracts and Forward Prices|arbitrage arguments]],  assuming no transaction costs and no interim cash flows.
- Key variables:
	  - $P$: Cash market price of the bond.
	  - $c$: Current yield,  calculated as the coupon rate divided by the cash market price.
	  - $r$: Financing rate (borrowing/lending rate).
	  - $t$: Time to the [[Futures Not Subject to Cash-And-Carry|futures]] delivery date (in years).
	  - $F$: [[Futures Price and the Quality Option Before E|Futures price]].

#### 2.1.1 Cash-and-Carry Arbitrage

- **Steps**:
  1. Sell the [[Futures Not Subject to Cash-And-Carry|futures]] contract at $F$.
  1. Purchase the bond for $P$.
  1. Borrow $P$ at the financing rate $r$ until the settlement date.

- **Outcome at Settlement**:
  - **Proceeds**:
	- From the [[Futures Not Subject to Cash-And-Carry|futures]] contract: $F$.
	- [[Intra-Year Compounding and Day-Count|Accrued interest]] on the bond: $ctP$.
	- Total proceeds: $$F + ctP$$
  - **Outlay**:
	- Repayment of the loan principal: $P$.
	- Interest on the loan: $rtP$.
	- Total outlay: $P + rtP$.
- **Profit**:
 $$\text{Profit} = F + ctP - (P + rtP)$$

- **Equilibrium Condition**:
  - To eliminate [[Class Note 13 The LTCM Meltdown|arbitrage opportunities]],  profit must equal zero:
   $$0 = F + ctP - (P + rtP)$$
  - Solving for $F$:
   $$F = P + Pt(r - c) = P[1 + t(r - c)]$$

#### 2.1.2 Reverse Cash-and-Carry Arbitrage

- **Steps**:
  1. Buy the [[Futures Not Subject to Cash-And-Carry|futures]] contract at $F$.
  1. Sell (short) the bond for $P$.
  1. Invest $P$ at the financing rate $r$ until the settlement date.

- **Outcome at Settlement**:
  - **Proceeds**:
	- From the loan principal: $P$.
	- Interest earned: $rtP$.
	- Total proceeds: $P + rtP$.
  - **Outlay**:
	- From the [[Futures Not Subject to Cash-And-Carry|futures]] contract: $F$.
	- [[Intra-Year Compounding and Day-Count|Accrued interest]] on the bond: $ctP$.
	- Total outlay: $F + ctP$.
- **Profit**:
 $$\text{Profit} = P + rtP - (F + ctP)$$

- **Equilibrium Condition**:
  - To eliminate [[Class Note 13 The LTCM Meltdown|arbitrage opportunities]],  profit must equal zero:
   $$0 = P + rtP - (F + ctP)$$
  - Solving for $F$ yields the same equation:
   $$F = P[1 + t(r - c)]$$

> [!NOTE]
> ### 2.2 Example: Calculating the Theoretical [[Futures Price and the Quality Option Before E|Futures Price]]
>
> - **Given**:
>   - $r = 0.08$ (financing rate).
>   - $c = 0.12$ (current yield).
>   - $P = 100$ (cash market price).
>   - $t = 0.25$ (time to delivery in years).
> - **Calculation**:
> $F = P[1 + t(r - c)]$
> $F = 100[1 + 0.25(0.08 - 0.12)]$
> $F = 100[1 - 0.01]$
> $F = 99$

- **Interpretation**:
  - The theoretical [[Futures Price and the Quality Option Before E|futures price]] is $99$,  which is at a discount to the cash market price due to negative carry ($r < c$).

### 2.3 The Concept of Carry

- **Definition**:
  - Carry is the net [[Realized Returns|financing cost]],  calculated as the difference between the financing rate ($r$) and the current yield ($c$).
  - $\text{Carry} = r - c$
- **Implications**:
  - **Positive Carry ($c > r$)**:
	- The [[Futures Price and the Quality Option Before E|futures price]] will sell at a discount to the cash price ($F < P$).
  - **Negative Carry ($c < r$)**:
	- The [[Futures Price and the Quality Option Before E|futures price]] will sell at a premium to the cash price ($F > P$).
  - **Zero Carry ($c = r$)**:
	- The [[Futures Price and the Quality Option Before E|futures price]] will equal the cash price ($F = P$).
- **Real-World Factors**:
  - The shape of the yield curve influences carry:
	- **Upward-Sloping Yield Curve**: [[Asset Backed Commercial Paper Understanding the Risks|Short-term financing]] rates are lower than current yields,  resulting in positive carry.
	- **Inverted Yield Curve**: [[Asset Backed Commercial Paper Understanding the Risks|Short-term financing]] rates are higher than current yields,  resulting in negative carry.

## 3. Applications of Futures in Portfolio Management

### 3.1 Interest-Rate Risk Control

- **Objective**:
  - Adjust the [[An Asset Allocation Primer|portfolio]]'s [[Key Rates O1s Durations and Hedging|duration]] to manage exposure to [[How Countries Go Broke-Chapter 12 to Chapter 14|interest rate changes]].
  - Increase [[Key Rates O1s Durations and Hedging|duration]] if rates are expected to fall; decrease [[Key Rates O1s Durations and Hedging|duration]] if rates are expected to rise.
- **Mechanism**:
  - **Buying [[Futures Not Subject to Cash-And-Carry|Futures]]**: Increases [[An Asset Allocation Primer|portfolio]] [[Key Rates O1s Durations and Hedging|duration]],  as [[Futures Not Subject to Cash-And-Carry|futures]] prices rise when rates fall.
  - **Selling [[Futures Not Subject to Cash-And-Carry|Futures]]**: Decreases [[An Asset Allocation Primer|portfolio]] [[Key Rates O1s Durations and Hedging|duration]],  as [[Futures Not Subject to Cash-And-Carry|futures]] prices fall when rates rise.
- **Advantages**:
  - [[Futures Not Subject to Cash-And-Carry|Futures]] provide a quick and cost-effective way to adjust [[Key Rates O1s Durations and Hedging|duration]] compared to cash market instruments.

### 3.2 Hedging

- **Definition**:
  - [[Key Rates O1s Durations and Hedging|Hedging]] involves taking a [[Futures Not Subject to Cash-And-Carry|futures]] position to offset potential losses in the cash market.
- **Types of Hedges**:
  - **[[Chapter 4 - Futures: Hedging and Speculation|Short Hedge]]**:
	- Protects against a decline in the cash price of a fixed-income security.
	- Example: A [[Uses of Interest Rate Swaps|pension fund]] manager sells [[Futures Not Subject to Cash-And-Carry|futures]] to lock in a selling price for bonds that must be liquidated in the future.
  - **Long Hedge**:
	- Protects against an increase in the cash price of a fixed-income security.
	- Example: A manager buys [[Futures Not Subject to Cash-And-Carry|futures]] to lock in a purchase price for bonds expected to be bought in the future.
- **[[Lessons From The Crisis|Basis Risk]]**:
  - The difference between the cash price and the [[Futures Price and the Quality Option Before E|futures price]] is called the basis.
  - [[Lessons From The Crisis|Basis risk]] arises when the cash and [[Futures Not Subject to Cash-And-Carry|futures]] prices do not move perfectly together.
- **Cross-[[Key Rates O1s Durations and Hedging|Hedging]]**:
  - Occurs when the bond to be hedged is not identical to the bond underlying the [[Futures Not Subject to Cash-And-Carry|futures]] contract.
  - Cross-[[Key Rates O1s Durations and Hedging|hedging]] introduces additional [[Lessons From The Crisis|basis risk]].

### 3.3 [[Lecture 2- Asset Allocation with Multiple Risky Assets|asset allocation]]

- **Objective**:
  - Adjust the composition of a [[An Asset Allocation Primer|portfolio]] between asset classes (e.g.,  stocks and bonds).
- **Mechanism**:
  - Use interest-rate [[Futures Not Subject to Cash-And-Carry|futures]] and [[Teaching Note 2-Futures Contracts|stock index futures]] to efficiently shift allocations without transacting in the cash market.

### 3.4 Creating Synthetic Securities for Yield Enhancement

- **Concept**:
  - Combine [[Mathematics of the Financial Markets|futures contracts]] with cash market instruments to create [[Chapter 17 - Option Strategies|synthetic securities]].
- **Example**:
  - An investor holding a 20-year Treasury bond sells Treasury [[Futures Not Subject to Cash-And-Carry|futures]] for delivery in three months.
  - The combined position is equivalent to a three-month riskless security (e.g.,  a Treasury bill).
  - If the synthetic security's yield exceeds the yield on a cash market Treasury bill,  the investor can enhance [[An Asset Allocation Primer|portfolio]] [[Assets|returns]].

### 3.5 Portable Alpha Strategies

- **Definition**:
  - [[Hedge Funds Alpha Beta and Strategy Indexes 287|Portable alpha]] strategies separate market [[Assets|returns]] (beta) from [[Assets|returns]] generated by selection skill (alpha).
- **Implementation**:
  - Use [[Chapter 9 Arbitrage and Hedging With Options|derivatives]] (e.g.,  [[Futures Not Subject to Cash-And-Carry|futures]] and swaps) to maintain market exposure while pursuing alpha-generating strategies.
- **Advantages**:
  - Flexibility to add [[Assets|returns]] without increasing risk.
  - Applicable across asset classes,  including equities and [[Lecture Notes Bonds,  Preferred Stock,  and Structured Products|fixed income]].

## 4. Key Takeaways

- The theoretical [[Futures Price and the Quality Option Before E|futures price]] is determined by the net [[Realized Returns|financing cost]] (carry),  which reflects the relationship between the financing rate and the current yield.
- [[Mathematics of the Financial Markets|Futures contracts]] are versatile tools for managing interest-rate risk,  enabling [[An Asset Allocation Primer|portfolio]] managers to adjust [[Key Rates O1s Durations and Hedging|duration]],  hedge positions,  and alter [[Lecture 2- [[Lecture 2- Asset Allocation with Multiple Risky Assets|Asset Allocation]] with [[Lecture 2- Asset Allocation with Multiple Risky Assets|Multiple Risky Assets]]|[[Lecture 2- Asset Allocation with Multiple Risky Assets|asset allocation]]]]s efficiently.
- [[Chapter 17 - Option Strategies|Synthetic securities]] and [[Hedge Funds Alpha Beta and Strategy Indexes 287|portable alpha]] strategies demonstrate the innovative applications of [[Futures Not Subject to Cash-And-Carry|futures]] in enhancing [[An Asset Allocation Primer|portfolio]] [[Assets|returns]] and achieving [[An Asset Allocation Primer|investment]] objectives.
- [[Lessons From The Crisis|Basis risk]] and cross-[[Key Rates O1s Durations and Hedging|hedging]] are important considerations when using [[Chapter 4 - Futures: Hedging and Speculation|futures for hedging]] purposes,  as they can impact the effectiveness of the hedge.

By mastering these concepts and strategies,  [[An Asset Allocation Primer|portfolio]] managers can effectively navigate interest-rate risk and optimize [[An Asset Allocation Primer|portfolio]] performance.

# Lecture Notes: Controlling Interest-Rate Risk with Futures and Hedging Strategies

## 1. Introduction to Interest-Rate Risk Management with Futures

- Interest-rate risk is a critical concern for [[An Asset Allocation Primer|portfolio]] managers,  as changes in [[Interest Rate Quotations|interest rates]] can significantly impact the value of fixed-income securities.
- [[Mathematics of the Financial Markets|Futures contracts]] on interest-rate instruments provide a cost-effective and flexible way to manage this risk.
- This lecture focuses on:
  - The advantages of using interest-rate [[Futures Not Subject to Cash-And-Carry|futures]] over cash-market instruments.
  - The principles of controlling interest-rate risk using [[Futures Not Subject to Cash-And-Carry|futures]].
  - The mechanics of determining the number of [[Mathematics of the Financial Markets|futures contracts]] required to achieve a target [[A Guide to Duration DV01 and Yield Curve|dollar duration]].
  - [[Key Rates O1s Durations and Hedging|Hedging]] strategies using interest-rate [[Futures Not Subject to Cash-And-Carry|futures]],  including short and long hedges.

## 2. Advantages of Using Interest-Rate Futures

### 2.1 Lower Transaction Costs
- Trading [[Mathematics of the Financial Markets|futures contracts]] incurs significantly lower transaction costs compared to trading long-term [[US Markets|Treasury securities]] in the cash market.
- This cost efficiency makes [[Futures Not Subject to Cash-And-Carry|futures]] an attractive tool for frequent adjustments to [[An Asset Allocation Primer|portfolio]] [[Key Rates O1s Durations and Hedging|duration]] or [[Key Rates O1s Durations and Hedging|hedging]] strategies.

### 2.2 Lower Margin Requirements
- [[Mathematics of the Financial Markets|Futures contracts]] require only an initial margin deposit,  which is a fraction of the contract's notional value.
- This allows [[An Asset Allocation Primer|portfolio]] managers to achieve greater [[Lecture 6-Leverage, Tail Risk, Volatility Products|leverage]] compared to directly trading [[US Markets|Treasury securities]].

### 2.3 Ease of Short Selling
- Selling short in the [[Futures Not Subject to Cash-And-Carry|futures]] market is more straightforward than in the cash market for [[US Markets|Treasury securities]].
- [[Mathematics of the Financial Markets|Futures contracts]] eliminate the need to borrow securities,  making short positions more accessible and cost-effective.

### 2.4 Extending Portfolio Duration
- [[Futures Not Subject to Cash-And-Carry|Futures]] can be used to construct portfolios with longer durations than those available in the cash market.
  - *Example*: A [[Uses of Interest Rate Swaps|pension fund]] manager may need a [[An Asset Allocation Primer|portfolio]] [[Key Rates O1s Durations and Hedging|duration]] of 15 to meet specific [[An Asset Allocation Primer|investment]] objectives. If bonds with such a long [[Key Rates O1s Durations and Hedging|duration]] are unavailable,  the manager can buy interest-rate [[Futures Not Subject to Cash-And-Carry|futures]] to increase the [[An Asset Allocation Primer|portfolio]]'s [[Key Rates O1s Durations and Hedging|duration]] to the target level.

## 3. General Principles of Interest-Rate Risk Control

### 3.1 Combining Dollar Exposures
- The key principle in controlling interest-rate risk with [[Futures Not Subject to Cash-And-Carry|futures]] is to combine the dollar exposure of the current [[An Asset Allocation Primer|portfolio]] with the dollar exposure of a [[Futures Not Subject to Cash-And-Carry|futures]] position to achieve the target dollar exposure.
- The total dollar exposure is given by:
 $\text{Portfolio's Dollar Duration} = \text{Current Dollar Duration} + \text{Dollar Duration of Futures Position}$$

### 3.2 Measures of Interest-Rate Sensitivity
- Two commonly used measures for approximating the sensitivity of a bond or [[An Asset Allocation Primer|portfolio]] to changes in [[Interest Rate Quotations|interest rates]] are:
  - **Price Value of a Basis Point (PVBP)**: The dollar price change resulting from a 1 basis point change in yield.
  - **[[Key Rates O1s Durations and Hedging|Duration]]**: The approximate percentage price change for a 100 basis point change in rates.
	- *Effective [[Key Rates O1s Durations and Hedging|Duration]]*: Used for bonds with embedded options,  as it accounts for changes in cash flows due to interest rate movements.
	- *Effective [[A Guide to Duration DV01 and Yield Curve|Dollar Duration]]*: The dollar price change for a given change in [[Interest Rate Quotations|interest rates]],  calculated using the [[An Asset Allocation Primer|portfolio]]'s valuation model.

### 3.3 Importance of a Valuation Model
- A reliable valuation model is essential for:
  - Estimating the new values of bonds in the [[An Asset Allocation Primer|portfolio]] when [[Interest Rate Quotations|interest rates]] change.
  - Valuing the derivative contracts used to control interest-rate exposure.

## 4. Determining the Target Dollar Duration

### 4.1 Calculating Target Dollar Duration
- The target [[A Guide to Duration DV01 and Yield Curve|dollar duration]] for a [[An Asset Allocation Primer|portfolio]] is determined based on the desired sensitivity to [[How Countries Go Broke-Chapter 12 to Chapter 14|interest rate changes]].
- For a 50 basis point change in [[Interest Rate Quotations|interest rates]],  the target [[A Guide to Duration DV01 and Yield Curve|dollar duration]] is calculated as:
 $\text{Target Dollar Duration} = \frac{\text{Target Duration} \times \text{Portfolio Value}}{200}$$
- *Example*: A manager of a $500 million [[An Asset Allocation Primer|portfolio]] seeks a target [[Key Rates O1s Durations and Hedging|duration]] of 6.
  - $$\text{Target Dollar Duration} = \frac{6 \times 500,   000,   000}{200} = 15,   000,   000$$

### 4.2 Comparing Target and Current Dollar Duration
- The current [[A Guide to Duration DV01 and Yield Curve|dollar duration]] is calculated similarly:
 $\text{Current Dollar Duration} = \frac{\text{Current Duration} \times \text{Portfolio Value}}{200}$$
- *Example*: If the current [[Key Rates O1s Durations and Hedging|duration]] is 4 for the $500 million [[An Asset Allocation Primer|portfolio]]:
  - $$\text{Current Dollar Duration} = \frac{4 \times 500,   000,   000}{200} = 10,   000,   000$$

### 4.3 Adjusting Dollar Duration with Futures
- The difference between the target and current dollar durations determines the dollar exposure required from the [[Futures Not Subject to Cash-And-Carry|futures]] position:
 $\text{Dollar Exposure from Futures} = \text{Target Dollar Duration} - \text{Current Dollar Duration}$$
- If the difference is positive,  [[Mathematics of the Financial Markets|futures contracts]] must be purchased to increase dollar exposure. If negative,  [[Mathematics of the Financial Markets|futures contracts]] must be sold to decrease dollar exposure.

## 5. Determining the Number of Futures Contracts

### 5.1 Dollar Duration of a Futures Contract
- The [[A Guide to Duration DV01 and Yield Curve|dollar duration]] of a [[Futures Not Subject to Cash-And-Carry|futures]] contract is the sensitivity of its value to changes in [[Interest Rate Quotations|interest rates]].
- It is calculated as:
 $\text{Dollar Duration of Futures Contract} = \text{Dollar Duration of CTD Issue} \times \text{Conversion Factor for CTD Issue}$$
  - **CTD Issue**: The [[Tba and Specified Pools Markets|cheapest-to-deliver]] bond for the [[Futures Not Subject to Cash-And-Carry|futures]] contract.
  - **Conversion Factor**: Adjusts for differences in coupon rates and maturities among deliverable bonds.

### 5.2 Calculating the Number of Futures Contracts
- The number of [[Mathematics of the Financial Markets|futures contracts]] required to achieve the target [[A Guide to Duration DV01 and Yield Curve|dollar duration]] is given by:
 $\text{Number of Futures Contracts} = \frac{\text{Target Dollar Duration} - \text{Current Dollar Duration}}{\text{Dollar Duration per Futures Contract}}$$
- A positive result indicates that [[Mathematics of the Financial Markets|futures contracts]] must be purchased,  while a negative result indicates that [[Mathematics of the Financial Markets|futures contracts]] must be sold.

### 5.3 Example: Determining the Number of Contracts
- *Given*:
  - Target [[A Guide to Duration DV01 and Yield Curve|Dollar Duration]] = $15,   000,   000$
  - Current [[A Guide to Duration DV01 and Yield Curve|Dollar Duration]] = $10,   000,   000$
  - [[A Guide to Duration DV01 and Yield Curve|Dollar Duration]] per [[Futures Not Subject to Cash-And-Carry|Futures]] Contract = $2,   100$
- *Calculation*:
 $\text{Number of Futures Contracts} = \frac{15,  000,  000 - 10,  000,  000}{2,  100} = 2,  381$$
- The manager must purchase 2,  381 [[Mathematics of the Financial Markets|futures contracts]] to achieve the target [[A Guide to Duration DV01 and Yield Curve|dollar duration]].

## 6. Hedging with Interest-Rate Futures

### 6.1 Short Hedge
- A [[Chapter 4 - Futures: Hedging and Speculation|short hedge]] is used to protect against a decline in the cash price of a bond.
- [[Mathematics of the Financial Markets|Futures contracts]] are sold to lock in a selling price.
- *Example*: A [[Uses of Interest Rate Swaps|pension fund]] manager expects to liquidate bonds in 40 days to make a $5 million payment. Selling [[Mathematics of the Financial Markets|futures contracts]] protects against rising [[Interest Rate Quotations|interest rates]],  which would lower bond prices.

### 6.2 Long Hedge
- A long hedge is used to protect against an increase in the cash price of a bond.
- [[Mathematics of the Financial Markets|Futures contracts]] are purchased to lock in a buying price.
- *Example*: A manager expects substantial cash contributions and anticipates falling [[Interest Rate Quotations|interest rates]]. Buying [[Mathematics of the Financial Markets|futures contracts]] protects against rising bond prices.

### 6.3 Cross-Hedging
- Cross-[[Key Rates O1s Durations and Hedging|hedging]] occurs when the bond or [[An Asset Allocation Primer|portfolio]] to be hedged is not identical to the bond underlying the [[Futures Not Subject to Cash-And-Carry|futures]] contract.
- This introduces [[Lessons From The Crisis|basis risk]],  as the cash and [[Futures Not Subject to Cash-And-Carry|futures]] prices may not move perfectly together.

## 7. Monitoring and Evaluating the Hedge

### 7.1 Steps in the Hedging Process
1. **Determine the Appropriate [[Key Rates O1s Durations and Hedging|Hedging]] Instrument**:
   - Choose a [[Futures Not Subject to Cash-And-Carry|futures]] contract with a high correlation to the [[Analysis of Fixed Income Securities|interest rate risk]] being hedged.
   - Consider [[Class Note 10 Liquidity and Class Note 10 Liquidity and Liquidity Managementliquidity management|liquidity]] and [[One-Month SOFR Futures|delivery month]].
1. **Determine the Target for the Hedge**:
   - Establish the target rate or price to be locked in by the hedge.
1. **Determine the Position to Be Taken**:
   - Calculate the number of [[Mathematics of the Financial Markets|futures contracts]] required to achieve the target [[A Guide to Duration DV01 and Yield Curve|dollar duration]].
1. **Monitor and Evaluate the Hedge**:
   - Adjust the [[Futures Not Subject to Cash-And-Carry|futures]] position as needed to maintain the target [[A Guide to Duration DV01 and Yield Curve|dollar duration]] over time.

### 7.2 Risk and Expected Return in a Hedge
- The effectiveness of a hedge depends on the correlation between cash and [[Futures Not Subject to Cash-And-Carry|futures]] prices.
- The manager's objective is to "lock in" a rate or price,  but the actual outcome may vary due to [[Lessons From The Crisis|basis risk]] and delivery options.

## 8. Summary and Key Takeaways

- Interest-rate [[Futures Not Subject to Cash-And-Carry|futures]] provide a cost-effective and flexible tool for managing interest-rate risk.
- The key to controlling interest-rate risk is to align the [[An Asset Allocation Primer|portfolio]]'s [[A Guide to Duration DV01 and Yield Curve|dollar duration]] with the target [[A Guide to Duration DV01 and Yield Curve|dollar duration]] using [[Mathematics of the Financial Markets|futures contracts]].
- The number of [[Mathematics of the Financial Markets|futures contracts]] required is determined by the difference between the target and current dollar durations,  divided by the [[A Guide to Duration DV01 and Yield Curve|dollar duration]] per [[Futures Not Subject to Cash-And-Carry|futures]] contract.
- [[Key Rates O1s Durations and Hedging|Hedging]] strategies,  including short and long hedges,  allow managers to protect against adverse interest rate movements.
- Monitoring and adjusting the hedge over time ensures that the [[An Asset Allocation Primer|portfolio]] remains aligned with its [[An Asset Allocation Primer|investment]] objectives.

By mastering these principles and techniques,  [[An Asset Allocation Primer|portfolio]] managers can effectively manage interest-rate risk and optimize [[An Asset Allocation Primer|portfolio]] performance.

# Lecture Notes: Hedging with Treasury Bond Futures and Basis Risk

## 1. Introduction to Hedging with Treasury Bond Futures

- Treasury bond [[Futures Not Subject to Cash-And-Carry|futures]] are widely used by [[An Asset Allocation Primer|portfolio]] managers to hedge [[Analysis of Fixed Income Securities|interest rate risk]] and lock in effective sale or purchase prices for fixed-income securities.
- This lecture focuses on:
  - The mechanics of [[Key Rates O1s Durations and Hedging|hedging]] with Treasury bond [[Futures Not Subject to Cash-And-Carry|futures]].
  - The calculation of effective sale prices.
  - The role of [[Lessons From The Crisis|basis risk]] in [[Key Rates O1s Durations and Hedging|hedging]].
  - The determination of the number of [[Mathematics of the Financial Markets|futures contracts]] required for a hedge.
  - A detailed example of cross-[[Key Rates O1s Durations and Hedging|hedging]] a non-deliverable bond using Treasury bond [[Futures Not Subject to Cash-And-Carry|futures]].

## 2. Mechanics of Hedging with Treasury Bond Futures

### 2.1 Effective Sale Price of Treasury Bonds

- The effective sale price of a Treasury bond is determined by combining the actual sale price of the bond with the gain or loss on the [[Futures Not Subject to Cash-And-Carry|futures]] position.
- **Formula**:
 $\text{Effective Sale Price} = \text{Actual Sale Price of Treasury Bond} + \text{Gain or Loss on Futures Position}$$

- **Example**:
  - Actual sale price of Treasury bond: \$140,  000,  000.
  - Gain on [[Futures Not Subject to Cash-And-Carry|futures]] position: \$4,  979,  000.
  - Effective sale price:
	$$\text{Effective Sale Price} = 140,   000,   000 + 4,   979,   000 = 144,   979,   000$$

- The effective sale price reflects the target price dictated by the [[Futures Not Subject to Cash-And-Carry|futures]] rate when the hedge is set.

### 2.2 Convergence at Delivery Date

- If a hedge is held until the delivery date of the [[Futures Not Subject to Cash-And-Carry|futures]] contract,  the spot price of the bond and the [[Futures Price and the Quality Option Before E|futures price]] converge.
- This ensures that the effective sale price is locked in at the [[Futures Not Subject to Cash-And-Carry|futures]] rate set when the hedge was established.

### 2.3 Short-Term Hedges

- For hedges lifted prior to the delivery date,  the effective rate or price is more likely to approximate the current [[The Foreign Exchange Market Annotations|spot rate]] rather than the [[Futures Not Subject to Cash-And-Carry|futures]] rate.
- The shorter the hedge [[Key Rates O1s Durations and Hedging|duration]],  the less likely convergence will occur,  and the effective rate will reflect the one-day [[Forward Points in Currency|forward rate]],  which is nearly equal to the [[The Foreign Exchange Market Annotations|spot rate]].

## 3. Basis and Basis Risk in Hedging

### 3.1 Definition of Basis

- The **basis** is the difference between the spot price of a security and its [[Futures Price and the Quality Option Before E|futures price]].
- **Price Basis**:
 $\text{Price Basis} = \text{Spot Price} - \text{Futures Delivery Price}$$
- **Rate Basis**:
 $\text{Rate Basis} = \text{Spot Rate} - \text{Futures Rate}$$

### 3.2 Target Basis and Basis Risk

- The **target basis** is the expected basis on the day the hedge is lifted.
- **Hedge to Delivery Date**:
  - The target basis is zero due to convergence.
  - The target rate equals the [[Futures Not Subject to Cash-And-Carry|futures]] rate.
- **Hedge Lifted Before Delivery**:
  - The target basis is the current basis,  which introduces uncertainty.
  - The target rate equals the [[Futures Not Subject to Cash-And-Carry|futures]] rate plus the target rate basis.
- **[[Lessons From The Crisis|Basis Risk]]**:
  - [[Lessons From The Crisis|Basis risk]] refers to the uncertainty surrounding the target basis on the day the hedge is lifted.
  - It arises from unpredictable changes in the relationship between cash and [[Futures Not Subject to Cash-And-Carry|futures]] prices.

## 4. Determining the Number of Futures Contracts

### 4.1 Hedge Ratio

- The [[Chapter 27 - Delta Hedging|hedge ratio]] determines the number of [[Mathematics of the Financial Markets|futures contracts]] required to offset the risk of the position being hedged.
- **Formula**:
 $\text{Number of Futures Contracts} = \frac{\text{Current Dollar Duration Without Futures}}{\text{Dollar Duration per Futures Contract}}$$

### 4.2 Cross-Hedging

- Cross-[[Key Rates O1s Durations and Hedging|hedging]] occurs when the security to be hedged is not deliverable on the [[Futures Not Subject to Cash-And-Carry|futures]] contract used in the hedge.
- The number of [[Mathematics of the Financial Markets|futures contracts]] for a cross-hedge is determined by the relative dollar durations of the bond to be hedged and the [[Tba and Specified Pools Markets|cheapest-to-deliver]] (CTD) issue.
- **Formula**:
 $\text{Number of Futures Contracts} = \frac{\text{Current Dollar Duration Without Futures}}{\text{Dollar Duration of CTD Issue}} \times \text{Conversion Factor for CTD Issue}$$

## 5. Example: Cross-Hedging a Non-Deliverable Bond

### 5.1 Problem Setup

- **Bond to be Hedged**:
  - \$10 million par value of a 6.25% FNMA bond maturing on 5/15/2029.
  - Current price: 88.39.
  - Current yield: 7.20%.
- **[[Futures Not Subject to Cash-And-Carry|Futures]] Contract**:
  - September 1999 Treasury bond [[Futures Not Subject to Cash-And-Carry|futures]].
  - [[Futures Price and the Quality Option Before E|Futures price]]: 113.
  - CTD issue: 11.25% Treasury bond maturing on 2/15/2015.
  - CTD price: 146.19.
  - CTD yield: 6.50%.
  - Conversion factor for CTD issue: 1.283.
- **Assumptions**:
  - Yield spread between FNMA bond and CTD issue remains constant at 70 basis points.
  - Anticipated sale date: Last business day of September 1999.

### 5.2 Target Levels

- **Target Yield for CTD Issue**:
  - [[Futures Price and the Quality Option Before E|Futures price]] × Conversion factor = Target price for CTD issue.
  - $$\text{Target Price for CTD Issue} = 113 \times 1.283 = 144.979$$
  - Yield corresponding to target price: 6.56%.
- **Target Yield for FNMA Bond**:
  - $$\text{Target Yield for FNMA Bond} = 6.56\% + 0.70\% = 7.26\%$$
  - Price corresponding to target yield: 87.76.

### 5.3 Dollar Durations

- **[[A Guide to Duration DV01 and Yield Curve|Dollar Duration]] of FNMA Bond**:
  - [[A Guide to Duration DV01 and Yield Curve|Dollar duration]] per \$100 par value: \$5.453.
  - Total [[A Guide to Duration DV01 and Yield Curve|dollar duration]]:
	$$\text{Dollar Duration of FNMA Bond} = \frac{\$10,   000,   000}{100} \times 5.453 = 545,   300$$

- **[[A Guide to Duration DV01 and Yield Curve|Dollar Duration]] of CTD Issue**:
  - [[A Guide to Duration DV01 and Yield Curve|Dollar duration]] per \$100 par value: \$6.255.
  - [[A Guide to Duration DV01 and Yield Curve|Dollar duration]] per [[Futures Not Subject to Cash-And-Carry|futures]] contract:
	$$\text{Dollar Duration per Futures Contract} = \frac{\$100,   000}{100} \times 6.255 = 6,   255$$

### 5.4 Number of Futures Contracts

- **Formula**:
 $\text{Number of Futures Contracts} = \frac{\text{Dollar Duration of FNMA Bond}}{\text{Dollar Duration of CTD Issue}} \times \text{Conversion Factor for CTD Issue}$$

- **Calculation**:
 $\text{Number of Futures Contracts} = \frac{545,  300}{6,  255} \times 1.283 = 112$$

- **Result**:
  - To hedge the FNMA bond position,  112 Treasury bond [[Mathematics of the Financial Markets|futures contracts]] must be shorted.

### 5.5 Scenario Analysis

- Exhibit 63-2 provides a [[Week 4 Valuing Young and High‐Growth Companies|scenario analysis]] of the hedge outcome based on different sale prices for the FNMA bond at the delivery date of the [[Futures Not Subject to Cash-And-Carry|futures]] contract.

#### Key Observations
1. The effective sale price for the FNMA bond remains close to the target price of \$8,  776,  000 across various scenarios.
1. Gains or losses on the [[Futures Not Subject to Cash-And-Carry|futures]] position offset changes in the actual sale price of the FNMA bond,  stabilizing the effective sale price.

## 6. Summary and Key Takeaways

- Treasury bond [[Futures Not Subject to Cash-And-Carry|futures]] are effective tools for [[Multi-Factor Exposures and Portfolio Volatility|hedging interest rate risk]] and locking in target sale or purchase prices.
- The effective sale price of a bond is determined by combining the actual sale price with the gain or loss on the [[Futures Not Subject to Cash-And-Carry|futures]] position.
- [[Lessons From The Crisis|Basis risk]] arises from uncertainty about the target basis on the day the hedge is lifted and is a key consideration in [[Key Rates O1s Durations and Hedging|hedging]] strategies.
- The number of [[Mathematics of the Financial Markets|futures contracts]] required for a hedge depends on the relative dollar durations of the bond to be hedged and the CTD issue.
- Cross-[[Key Rates O1s Durations and Hedging|hedging]] introduces additional complexity but can be effectively managed by carefully calculating the [[Chapter 27 - Delta Hedging|hedge ratio]] and monitoring [[Lessons From The Crisis|basis risk]].

By understanding these principles and applying them rigorously,  [[An Asset Allocation Primer|portfolio]] managers can effectively manage [[Analysis of Fixed Income Securities|interest rate risk]] and achieve their [[An Asset Allocation Primer|investment]] objectives.

# Lecture Notes: Hedging with Futures and Options in Fixed Income Markets

## 1. Introduction to Hedging with Futures and Options

- [[Key Rates O1s Durations and Hedging|Hedging]] is a critical [[Financial Mathematics Course|risk management]] strategy in [[A Practical Guide to Bonds and Swaps|fixed income markets]],  allowing [[An Asset Allocation Primer|portfolio]] managers to mitigate the impact of adverse interest rate movements on bond portfolios.
- This lecture focuses on:
  - [[Key Rates O1s Durations and Hedging|Hedging]] with Treasury bond [[Futures Not Subject to Cash-And-Carry|futures]],  including the mechanics,  [[Lessons From The Crisis|basis risk]],  and the calculation of effective sale prices.
  - Advanced refinements in [[Key Rates O1s Durations and Hedging|hedging]] strategies,  such as adjusting for changing yield spreads and incorporating yield beta.
  - [[Key Rates O1s Durations and Hedging|Hedging]] with options,  including [[Chapter 29 - Portfolio Insurance|protective put]]-buying,  [[Chapter 18 - Stock Options and Stock Index Options|covered call]]-writing,  and collar strategies.
  - A detailed comparison of [[Futures Not Subject to Cash-And-Carry|futures]] and options [[Key Rates O1s Durations and Hedging|hedging]] strategies,  including their respective advantages and limitations.

## 2. Hedging with Treasury Bond Futures

### 2.1 Mechanics of Hedging with Futures

#### 2.1.1 Effective Sale Price
- The **effective sale price** of a bond is determined by combining the actual sale price with the gain or loss on the [[Futures Not Subject to Cash-And-Carry|futures]] position.
- **Formula**:
 $\text{Effective Sale Price} = \text{Actual Sale Price of Bond} + \text{Gain or Loss on Futures Position}$$
- Example:
  - Actual sale price of FNMA bond: \$8,  000,  000.
  - Gain on [[Futures Not Subject to Cash-And-Carry|futures]] position: \$800,  150.
  - Effective sale price:
	$$\text{Effective Sale Price} = 8,   000,   000 + 800,   150 = 8,   800,   150$$

#### 2.1.2 Convergence at Delivery Date
- By the delivery date of the [[Futures Not Subject to Cash-And-Carry|futures]] contract,  the [[Futures Price and the Quality Option Before E|futures price]] converges with the price of the [[Tba and Specified Pools Markets|cheapest-to-deliver]] (CTD) issue divided by its conversion factor.
- This ensures that the effective sale price is locked in at the [[Futures Not Subject to Cash-And-Carry|futures]] rate set at the inception of the hedge.

#### 2.1.3 Value of Futures Position
- The value of the [[Futures Not Subject to Cash-And-Carry|futures]] position is calculated as:
 $\text{Value of Futures Position} = \left(\frac{\text{Futures Price}}{100}\right) \times 100,  000 \times \text{Number of Futures Contracts}$$
- Example:
  - Final [[Futures Price and the Quality Option Before E|futures price]]: 105.85581.
  - Number of [[Mathematics of the Financial Markets|futures contracts]]: 112.
  - Value of [[Futures Not Subject to Cash-And-Carry|futures]] position:
	$$\text{Value of Futures Position} = \left(\frac{105.85581}{100}\right) \times 100,   000 \times 112 = 11,   855,   850$$

#### 2.1.4 Gain or Loss on Futures Position
- The gain or loss on the [[Futures Not Subject to Cash-And-Carry|futures]] position is calculated as:
 $\text{Gain or Loss} = \left(\frac{\text{Initial Futures Price} - \text{Final Futures Price}}{100}\right) \times 100,  000 \times \text{Number of Futures Contracts}$$
- Example:
  - Initial [[Futures Price and the Quality Option Before E|futures price]]: 113.
  - Final [[Futures Price and the Quality Option Before E|futures price]]: 105.85581.
  - Number of [[Mathematics of the Financial Markets|futures contracts]]: 112.
  - Gain:
	$$\text{Gain} = \left(\frac{113 - 105.85581}{100}\right) \times 100,   000 \times 112 = 800,   150$$

### 2.2 Basis and Basis Risk

#### 2.2.1 Definition of Basis
- The **basis** is the difference between the spot price of a bond and its [[Futures Price and the Quality Option Before E|futures price]].
- **Price Basis**:
 $\text{Price Basis} = \text{Spot Price} - \text{Futures Delivery Price}$$
- **Rate Basis**:
 $\text{Rate Basis} = \text{Spot Rate} - \text{Futures Rate}$$

#### 2.2.2 Basis Risk
- **[[Lessons From The Crisis|Basis risk]]** arises from uncertainty about the target basis on the day the hedge is lifted.
- If the hedge is lifted before the delivery date,  the target basis is the current basis,  introducing uncertainty into the effective sale price.

### 2.3 Refining the Hedge for Changing Yield Spreads

#### 2.3.1 Yield Beta
- Yield beta ($b$) measures the relative yield change between the bond to be hedged and the CTD issue.
- **Regression Equation**:
 $\text{Yield on Bond to Be Hedged} = a + b \times \text{Yield on CTD Issue} + \text{Error}$$
- Example:
  - If $b = 1.05$,  the yield on the FNMA bond is expected to move 5% more than the yield on the CTD issue.

#### 2.3.2 Adjusting the Number of Futures Contracts
- The number of [[Mathematics of the Financial Markets|futures contracts]] is adjusted to account for yield beta:
 $\text{Number of Futures Contracts} = \frac{\text{Current Dollar Duration Without Futures}}{\text{Dollar Duration of CTD Issue}} \times \text{Conversion Factor for CTD Issue} \times \text{Yield Beta}$$
- Example:
  - Original number of contracts: 112.
  - Yield beta: 1.05.
  - Adjusted number of contracts:
	$$\text{Adjusted Number of Contracts} = 112 \times 1.05 = 118$$

## 3. Hedging with Options

### 3.1 Protective Put-Buying Strategy

#### 3.1.1 Overview
- A **[[Chapter 29 - Portfolio Insurance|protective put]]-buying strategy** involves purchasing put options to hedge against rising [[Interest Rate Quotations|interest rates]].
- This strategy combines a [[Chapter 4 - Futures: Hedging and Speculation|long position]] in a bond with a [[Chapter 4 - Futures: Hedging and Speculation|long position]] in a put option,  providing [[Equity Linked Note|downside protection]] while retaining upside potential.

#### 3.1.2 Mechanics
- If [[Interest Rate Quotations|interest rates]] rise,  the value of the put option increases,  offsetting losses on the bond.
- If [[Interest Rate Quotations|interest rates]] fall,  the bond appreciates,  but the cost of the put option reduces the net gain.

#### 3.1.3 Example
- A manager holds \$10 million par value of a 6.25% FNMA bond and wants to establish a minimum price of 84.453.
- The equivalent [[Call and Put Payoffs at Expiry|strike price]] for a Treasury bond [[Futures Not Subject to Cash-And-Carry|futures]] put option is calculated using:
  - The price-yield relationship for the FNMA bond.
  - The yield spread between the FNMA bond and the CTD issue.
  - The conversion factor for the CTD issue.

### 3.2 Covered Call-Writing Strategy

#### 3.2.1 Overview
- A **[[Chapter 18 - Stock Options and Stock Index Options|covered call]]-writing strategy** involves selling call options against a bond [[An Asset Allocation Primer|portfolio]] to generate premium income.
- This strategy reduces downside risk but limits upside potential.

#### 3.2.2 Mechanics
- If [[Interest Rate Quotations|interest rates]] rise,  the premium received cushions the loss on the bond [[An Asset Allocation Primer|portfolio]].
- If [[Interest Rate Quotations|interest rates]] fall,  the call option becomes a liability,  capping the [[An Asset Allocation Primer|portfolio]]'s gains.

### 3.3 Collar Strategy

#### 3.3.1 Overview
- A **collar strategy** combines a [[Chapter 29 - Portfolio Insurance|protective put]]-buying strategy with a [[Chapter 18 - Stock Options and Stock Index Options|covered call]]-writing strategy.
- This involves purchasing a put option and selling a call option,  both out-of-the-money,  to create a range of protection.

#### 3.3.2 Mechanics
- The collar limits downside risk while capping upside potential.
- Within the range defined by the strike prices,  the [[An Asset Allocation Primer|portfolio]]'s value varies with [[Interest Rate Quotations|interest rates]].

## 4. Comparing Futures and Options Hedging Strategies

### 4.1 Futures Hedging
- **Advantages**:
  - Simple to implement.
  - Locks in a target price or rate.
  - Low transaction costs.
- **Disadvantages**:
  - No flexibility to benefit from favorable rate movements.
  - Subject to [[Lessons From The Crisis|basis risk]].

### 4.2 Options Hedging
- **Advantages**:
  - Provides flexibility to benefit from favorable rate movements.
  - Limits downside risk.
- **Disadvantages**:
  - Higher cost due to option premiums.
  - Requires careful selection of strike prices and contracts.

## 5. Steps in Options Hedging

### 5.1 Determine the Best Hedging Vehicle
- Consider factors such as option price,  [[Class Note 10 Liquidity and Class Note 10 Liquidity and Liquidity Managementliquidity management|liquidity]],  and correlation with the bond to be hedged.

### 5.2 Find the Appropriate Strike Price
- Convert the [[Call and Put Payoffs at Expiry|strike price]] of the option into an equivalent [[Call and Put Payoffs at Expiry|strike price]] for the bond being hedged.

### 5.3 Determine the Number of Contracts
- Calculate the [[Chapter 27 - Delta Hedging|hedge ratio]] to determine the number of options to buy or sell.

## 6. Summary and Key Takeaways

- [[Financial Instruments PSET Solutions|Hedging with futures]] and options provides [[An Asset Allocation Primer|portfolio]] managers with powerful tools to manage [[Analysis of Fixed Income Securities|interest rate risk]].
- [[Chapter 4 - Futures: Hedging and Speculation|Futures hedging]] is straightforward and cost-effective but lacks flexibility and is subject to [[Lessons From The Crisis|basis risk]].
- Options [[Key Rates O1s Durations and Hedging|hedging]] offers flexibility and [[Equity Linked Note|downside protection]] but is more complex and costly.
- The choice of [[The Value of the Swap Contract after Initiation|hedging strategy]] depends on the manager's market outlook and risk tolerance.
- Refinements such as adjusting for yield beta and monitoring yield spreads enhance the effectiveness of [[Key Rates O1s Durations and Hedging|hedging]] strategies.

By mastering these techniques,  [[An Asset Allocation Primer|portfolio]] managers can effectively mitigate [[Analysis of Fixed Income Securities|interest rate risk]] and optimize [[An Asset Allocation Primer|portfolio]] performance.

# Lecture Notes: Hedging with Futures Options – Protective Put and Covered Call Strategies

## 1. Introduction to Hedging with Futures Options

- [[Futures Not Subject to Cash-And-Carry|Futures]] options provide a flexible and effective way to hedge [[Analysis of Fixed Income Securities|interest rate risk]] in fixed-income portfolios.
- Two common strategies are:
  - **[[Chapter 29 - Portfolio Insurance|Protective Put]]-Buying Strategy**: Protects against rising [[Interest Rate Quotations|interest rates]] while allowing for upside potential if rates fall.
  - **[[Chapter 18 - Stock Options and Stock Index Options|Covered Call]]-Writing Strategy**: Generates premium income while limiting upside potential in exchange for partial [[Equity Linked Note|downside protection]].
- This lecture will cover:
  - The mechanics of calculating the number of options contracts required for a hedge.
  - [[Week 4 Valuing Young and High‐Growth Companies|Scenario analysis]] for [[Chapter 29 - Portfolio Insurance|protective put]] and [[Chapter 18 - Stock Options and Stock Index Options|covered call]] strategies.
  - A comparison of the two strategies and their implications for [[The Impact of Option Strategies in Financial  Portfolios Performance|portfolio management]].

## 2. Protective Put-Buying Strategy

### 2.1 Mechanics of Protective Put Hedging

#### 2.1.1 Calculating the Number of Options Contracts
- The [[Chapter 27 - Delta Hedging|hedge ratio]] for options is determined using the following formula:
 $\text{Number of Options Contracts} = \frac{\text{Current Dollar Duration Without Options}}{\text{Dollar Duration of the CTD Issue}} \times \text{Conversion Factor for CTD Issue}$$
- **Inputs**:
  - Current [[A Guide to Duration DV01 and Yield Curve|dollar duration]] without options: $$\$512,   320$$
  - [[A Guide to Duration DV01 and Yield Curve|Dollar duration]] of the CTD issue: $$\$6.021$$
  - Conversion factor for the CTD issue: $$1.283$$
- **Calculation**:
 $\text{Number of Options Contracts} = \frac{\$512,  320}{\$6.021} \times 1.283 = 109 \,  \text{put options}$$
- **Interpretation**:
  - To hedge the FNMA bond position,  109 put options on Treasury bond [[Futures Not Subject to Cash-And-Carry|futures]] must be purchased.

#### 2.1.2 Cost of the Hedge
- Suppose the price of the put option with a [[Call and Put Payoffs at Expiry|strike price]] of 110 is $$\$500$$ per contract.
- Total cost of the hedge:
 $\text{Cost of Hedge} = 109 \times \$500 = \$54,  500$$
- This cost is equivalent to $$0.545$$ per $$\$100$$ par value hedged.

### 2.2 Outcome of the Hedge

#### 2.2.1 Value of the Put Option Position
- The value of the put option position at expiration depends on whether the [[Futures Price and the Quality Option Before E|futures price]] is below the [[Call and Put Payoffs at Expiry|strike price]] of 110:
  - If the [[Futures Price and the Quality Option Before E|futures price]] is **greater than or equal to 110**,  the options expire worthless,  and the value of the put option position is zero.
  - If the [[Futures Price and the Quality Option Before E|futures price]] is **below 110**,  the options expire in the money,  and the value of the put option position is calculated as:
	$$\text{Value of Put Option Position} = \left(\frac{110}{100} - \frac{\text{Futures Price}}{100}\right) \times 100,   000 \times \text{Number of Put Options}$$

#### 2.2.2 Example Calculation
- **Scenario**:
  - Actual sale price of FNMA bond: $$\$8,   000,   000$$
  - [[Futures Price and the Quality Option Before E|Futures price]]: $$105.85581$$
  - Number of put options: $$109$$
- **Value of Put Option Position**:
 $\text{Value of Put Option Position} = \left(\frac{110}{100} - \frac{105.85581}{100}\right) \times 100,   000 \times 109 = \$45,  717$$
- **Effective Sale Price**:
 $\text{Effective Sale Price} = \text{Actual Sale Price} + \text{Value of Put Option Position} - \text{Cost of Hedge}$$
 $\text{Effective Sale Price} = 8,  000,  000 + 45,  717 - 54,  500 = 8,  397,  217$$

#### 2.2.3 Minimum Effective Sale Price
- The minimum effective sale price can be calculated before initiating the hedge:
 $\text{Minimum Effective Sale Price} = \text{Price of FNMA Bonds Equivalent to Futures Strike Price} - \text{Cost of Hedge}$$
  - Price of FNMA bonds equivalent to [[Futures Not Subject to Cash-And-Carry|futures]] [[Call and Put Payoffs at Expiry|strike price]]: $$84.453$$
  - Cost of hedge: $$0.545$$ per $$\$100$$ par value.
 $\text{Minimum Effective Sale Price} = 84.453 - 0.545 = 83.908$$
- **Interpretation**:
  - The effective sale price will never fall below $$83.908$$,  providing [[Equity Linked Note|downside protection]].

#### 2.2.4 Scenario Analysis
- Exhibit 63-8 provides a detailed [[Week 4 Valuing Young and High‐Growth Companies|scenario analysis]] for the [[Chapter 29 - Portfolio Insurance|protective put]] hedge,  showing the effective sale price under various [[Futures Price and the Quality Option Before E|futures price]] scenarios.

## 3. Covered Call-Writing Strategy

### 3.1 Mechanics of Covered Call Writing

#### 3.1.1 Selling Call Options
- In a [[Chapter 18 - Stock Options and Stock Index Options|covered call]]-writing strategy,  the [[An Asset Allocation Primer|portfolio]] manager sells out-of-the-money call options against an existing bond [[An Asset Allocation Primer|portfolio]].
- **Assumptions**:
  - [[Futures Price and the Quality Option Before E|Futures price]] at hedge initiation: $$113$$
  - [[Call and Put Payoffs at Expiry|Strike price]] of call options: $$117$$
  - Price of call options: $$\$500$$ per contract
  - Number of call options sold: $$109$$
- **Proceeds from Sale of Call Options**:
 $\text{Proceeds} = 109 \times \$500 = \$54,  500$$

#### 3.1.2 Liability of Call Option Position
- The liability from the call option position depends on whether the [[Futures Price and the Quality Option Before E|futures price]] exceeds the [[Call and Put Payoffs at Expiry|strike price]] of 117:
  - If the [[Futures Price and the Quality Option Before E|futures price]] is **less than or equal to 117**,  the liability is zero.
  - If the [[Futures Price and the Quality Option Before E|futures price]] is **greater than 117**,  the liability is calculated as:
	$$\text{Liability} = \left(\frac{\text{Futures Price}}{100} - \frac{117}{100}\right) \times 100,   000 \times \text{Number of Call Options}$$

#### 3.1.3 Example Calculation
- **Scenario**:
  - Actual sale price of FNMA bond: $$\$9,   500,   000$$
  - [[Futures Price and the Quality Option Before E|Futures price]]: $$119.31255$$
  - Number of call options: $$109$$
- **Liability**:
 $\text{Liability} = \left(\frac{119.31255}{100} - \frac{117}{100}\right) \times 100,   000 \times 109 = \$252,  068$$
- **Effective Sale Price**:
 $\text{Effective Sale Price} = \text{Actual Sale Price} + \text{Proceeds from Sale of Call Options} - \text{Liability}$$
 $\text{Effective Sale Price} = 9,  500,  000 + 54,  500 - 252,  068 = 9,  302,  432$$

### 3.2 Maximum Effective Sale Price
- The maximum effective sale price can be calculated before initiating the hedge:
 $\text{Maximum Effective Sale Price} = \text{Price of Hedged Bond Corresponding to Strike Price} + \text{Premium Received}$$
  - Price of hedged bond corresponding to [[Call and Put Payoffs at Expiry|strike price]]: $$92.858$$
  - Premium received: $$0.545$$ per $$\$100$$ par value.
 $\text{Maximum Effective Sale Price} = 92.858 + 0.545 = 93.403$$
- **Interpretation**:
  - The effective sale price will never exceed $$93.403$$,  limiting upside potential.

#### 3.2.1 Scenario Analysis
- Exhibit 63-9 provides a detailed [[Week 4 Valuing Young and High‐Growth Companies|scenario analysis]] for the [[Chapter 18 - Stock Options and Stock Index Options|covered call]]-writing strategy,  showing the effective sale price under various [[Futures Price and the Quality Option Before E|futures price]] scenarios.

## 4. Comparison of Protective Put and Covered Call Strategies

### 4.1 Protective Put Strategy
- **Advantages**:
  - Provides full [[Equity Linked Note|downside protection]] if rates rise.
  - Allows for unlimited upside potential if rates fall.
- **Disadvantages**:
  - Requires an upfront cost (option premium).
  - Minimum effective sale price is reduced by the cost of the hedge.

### 4.2 Covered Call Strategy
- **Advantages**:
  - Generates premium income,  providing partial [[Equity Linked Note|downside protection]].
  - No upfront cost; instead,  the strategy generates cash inflow.
- **Disadvantages**:
  - Limits upside potential if rates fall.
  - Maximum effective sale price is capped by the [[Call and Put Payoffs at Expiry|strike price]] of the call options.

## 5. Summary and Key Takeaways

- **[[Options Strategies Construction|Protective Put Strategy]]**:
  - Best suited for investors seeking [[Equity Linked Note|downside protection]] while retaining upside potential.
  - The cost of the hedge reduces the minimum effective sale price.
- **[[Chapter 18 - Stock Options and Stock Index Options|Covered Call]] Strategy**:
  - Best suited for investors expecting stable [[Interest Rate Quotations|interest rates]] and seeking to generate additional income.
  - Limits upside potential in exchange for premium income.
- **[[Week 4 Valuing Young and High‐Growth Companies|Scenario Analysis]]**:
  - Both strategies provide predictable outcomes under various interest rate scenarios,  allowing investors to align their [[Key Rates O1s Durations and Hedging|hedging]] approach with their market outlook and risk tolerance.

By understanding the mechanics and implications of these strategies,  [[An Asset Allocation Primer|portfolio]] managers can effectively manage [[Analysis of Fixed Income Securities|interest rate risk]] and optimize [[An Asset Allocation Primer|portfolio]] performance.

# Lecture Notes: Hedging Strategies and Interest Rate Swaps

## 1. Introduction to Hedging Strategies and Interest Rate Swaps

- [[Key Rates O1s Durations and Hedging|Hedging]] strategies are essential tools for [[Lecture Notes 4-Mechanics of Futures Trading and Fixed Income Derivatives|managing interest rate risk]] in fixed-income portfolios. These strategies allow [[An Asset Allocation Primer|portfolio]] managers to mitigate the impact of adverse interest rate movements on bond portfolios.
- Interest rate swaps,  a type of derivative,  are widely used by [[Financial Markets and Institutions Lecture Notes|financial institutions]] to synthetically manage [[Duration Gap Management|interest rate exposure]],  especially when direct restructuring of assets and liabilities is not feasible.
- This lecture focuses on:
  - Comparing alternative [[Key Rates O1s Durations and Hedging|hedging]] strategies,  including [[Futures Not Subject to Cash-And-Carry|futures]],  protective puts,  and covered calls.
  - The mechanics and features of interest rate swaps.
  - The interpretation of swap positions as packages of forward contracts or cash market instruments.

## 2. Comparing Hedging Strategies: Futures,  Protective Puts,  and Covered Calls

### 2.1 Overview of Hedging Strategies

- **[[Financial Instruments PSET Solutions|Hedging with Futures]]**:
  - [[Mathematics of the Financial Markets|Futures contracts]] are used to lock in a target price or rate for a bond [[An Asset Allocation Primer|portfolio]].
  - This strategy substitutes [[Lessons From The Crisis|basis risk]] for price risk,  as the [[Futures Price and the Quality Option Before E|futures price]] may not perfectly track the cash price of the bond being hedged.
- **[[Chapter 29 - Portfolio Insurance|Protective Put]]-Buying Strategy**:
  - Involves purchasing put options to hedge against rising [[Interest Rate Quotations|interest rates]].
  - Provides [[Equity Linked Note|downside protection]] while retaining upside potential.
- **[[Chapter 18 - Stock Options and Stock Index Options|Covered Call]]-Writing Strategy**:
  - Involves selling call options against a bond [[An Asset Allocation Primer|portfolio]] to generate premium income.
  - Limits upside potential in exchange for partial [[Equity Linked Note|downside protection]].

### 2.2 Exhibit 63-10: Comparison of Alternative Strategies

#### Key Observations from Exhibit 63-10

- **Effective Sale Price with [[Futures Not Subject to Cash-And-Carry|Futures]] Hedge**:
  - Provides a relatively stable effective sale price across a range of actual sale prices.
  - Example: For an actual sale price of $8,   000,   000,    the effective sale price is $8,  800,  150.
- **Effective Sale Price with Protective Puts**:
  - Offers [[Equity Linked Note|downside protection]] but results in a lower effective sale price compared to [[Chapter 4 - Futures: Hedging and Speculation|futures hedging]].
  - Example: For an actual sale price of $8,   000,   000,    the effective sale price is $8,  397,  217.
- **Effective Sale Price with Covered Calls**:
  - Generates premium income but caps the upside potential.
  - Example: For an actual sale price of $8,   000,   000,    the effective sale price is $8,  054,  500.

#### Implications
- No single strategy is superior across all scenarios. Each strategy has its advantages and disadvantages,  depending on the manager's market outlook and risk tolerance.
- Managers must choose among [[Lecture 1- [[Exercises|Probability Distributions]] of [[Assets|Returns]]|probability distribution]]s of outcomes rather than specific outcomes.

### 2.3 Key Takeaways on Hedging Strategies

- **[[Chapter 4 - Futures: Hedging and Speculation|Futures Hedging]]**:
  - Best suited for locking in a target price or rate.
  - Subject to [[Lessons From The Crisis|basis risk]] and delivery options embedded in [[Mathematics of the Financial Markets|futures contracts]].
- **[[Options Strategies Construction|Protective Put Strategy]]**:
  - Provides full [[Equity Linked Note|downside protection]] but requires an upfront cost (option premium).
  - Retains upside potential.
- **[[Chapter 18 - Stock Options and Stock Index Options|Covered Call]] Strategy**:
  - Generates premium income but limits upside potential.
  - Entails more downside risk than protective puts.
- **Collar Strategy**:
  - Combines protective puts and covered calls to create a range of protection.
  - Eliminates part of the [[An Asset Allocation Primer|portfolio]]'s downside risk by giving up part of its upside potential.

## 3. Interest Rate Swaps: Mechanics and Features

### 3.1 Definition and Purpose

- An **[[Primer on Interest Rate Swaps|interest rate swap]]** is an agreement between two parties (counterparties) to exchange periodic interest payments based on a [[Fundamentals of Swaps|notional principal]] amount.
- The [[Fundamentals of Swaps|notional principal]] amount is not exchanged; it serves as the basis for calculating the interest payments.
- Swaps are used to:
  - Manage [[Analysis of Fixed Income Securities|interest rate risk]].
  - Align the [[Key Rates O1s Durations and Hedging|duration]] of assets and liabilities.
  - Hedge against changes in [[Interest Rate Quotations|interest rates]].

### 3.2 Features of a Generic Swap

- **Fixed-Rate Payer and Floating-Rate Payer**:
  - One party agrees to pay a [[Chapter 36 - Currency Swaps|fixed interest rate]] (fixed-rate payer) and receive a floating interest rate.
  - The other party agrees to pay a floating interest rate (floating-rate payer) and receive a [[Chapter 36 - Currency Swaps|fixed interest rate]].
- **[[Fundamentals of Swaps|Notional Principal]] Amount**:
  - The dollar amount used to calculate interest payments.
  - Example: For a $50 million notional amount,    the fixed-rate payer pays $1.25 million every six months (5% × $50 million ÷ 2).
- **Floating Rate**:
  - Commonly based on benchmarks such as LIBOR,  Treasury bills,  or the [[Topics in Fiscal and Monetary Policies and Stabilization- Empirical Issues|federal funds rate]].
  - Resets periodically (e.g.,  daily,  monthly,  or semiannually).
- **Settlement**:
  - Payments are exchanged at designated intervals (e.g.,  semiannually).
  - Only the net difference between the fixed and floating payments is exchanged.

### 3.3 Example: Fixed-Rate Payer and Floating-Rate Payer

- **Assumptions**:
  - Notional amount: $50 million.
  - Fixed rate: 5%.
  - Floating rate: Six-month LIBOR.
  - Settlement frequency: Semiannual.
- **Cash Flows**:
  - Fixed-rate payer pays $1.25 million every six months.
  - Floating-rate payer pays [[A Guide to the Front End and [[Basis Swaps|Basis Swap]] Markets#[[Short-Term Rates and the Transition from LIBOR|London Interbank Offered Rate]] (LIBOR)|LIBOR]] × $50 million ÷ 2.
  - Example: If [[A Guide to the Front End and [[Basis Swaps|Basis Swap]] Markets#[[Short-Term Rates and the Transition from LIBOR|London Interbank Offered Rate]] (LIBOR)|LIBOR]] = 3%,  the floating-rate payer pays $750,  000.

### 3.4 Swap Market Structure

- **Over-the-Counter (OTC) Market**:
  - Swaps are typically traded OTC between counterparties.
  - The [[Note on The [[Credit Derivative Indexes|Dodd-Frank Act]] and Its Impact|[[Note on The Dodd-Frank Act and Its Impact|Dodd-Frank]]]] Act introduced Swap Execution Facilities (SEFs) to centralize clearing for standardized swaps.
- **Customization**:
  - Swaps can be tailored to meet specific needs,  including unusual terms or indices.

## 4. Interpreting a Swap Position

### 4.1 Swap as a Package of Forward Contracts

- An [[Primer on Interest Rate Swaps|interest rate swap]] can be viewed as a package of [[A Guide to the Front End and [[Basis Swaps|Basis Swap]] Markets#[[EURIBOR Forward Rate Agreements and Futures|Forward Rate Agreements]] (FRAs) [[Overview of Financial Markets|Overview]]|[[EURIBOR Forward Rate Agreements and Futures|Forward Rate Agreements]]]] (FRAs).
- **Advantages**:
  - Longer maturities: Swaps can extend beyond the maturities of typical forward contracts.
  - Transactional efficiency: A single [[Currency Swaps|swap contract]] replaces multiple forward contracts.

### 4.2 Swap as a Package of Cash Market Instruments

- A swap can also be interpreted as a combination of cash market instruments.
- **Example**:
  - Buy a $50 million floating-rate bond (pays [[A Guide to the Front End and [[Basis Swaps|Basis Swap]] Markets#[[Short-Term Rates and the Transition from LIBOR|London Interbank Offered Rate]] (LIBOR)|LIBOR]] every six months).
  - Finance the purchase by borrowing $50 million at a fixed rate (5% annual interest).
  - **Net [[Preview of the Book|Cash Flow]]**:
	- Inflows: [[A Guide to the Front End and [[Basis Swaps|Basis Swap]] Markets#[[Short-Term Rates and the Transition from LIBOR|London Interbank Offered Rate]] (LIBOR)|LIBOR]] × $50 million ÷ 2.
	- Outflows: $1.25 million.
	- Net position: [[A Guide to the Front End and [[Basis Swaps|Basis Swap]] Markets#[[Short-Term Rates and the Transition from LIBOR|London Interbank Offered Rate]] (LIBOR)|LIBOR]] × $50 million ÷ 2 - $1.25 million.
  - This is equivalent to the cash flows of a fixed-rate payer/floating-rate receiver.

### 4.3 Exhibit 64-1: Cash Flow Analysis

#### Cash Flow for a Five-Year Floating-Rate Bond Financed by Fixed-Rate Borrowing

| Six-Month Period | Floating-Rate Bond | Borrowing Cost | Net [[Preview of the Book|Cash Flow]] |

| 0 | -$50 million      | +$50 million | $0 |

| 1 | [[A Guide to the Front End and [[Basis Swaps|Basis Swap]] Markets#[[Short-Term Rates and the Transition from LIBOR|London Interbank Offered Rate]] (LIBOR)|LIBOR]] × $50 ÷ 2 | -$1.25 million | [[A Guide to the Front End and [[Basis Swaps|Basis Swap]] Markets#[[Short-Term Rates and the Transition from LIBOR|London Interbank Offered Rate]] (LIBOR)|LIBOR]] × $50 ÷ 2 - $1.25 million |

| 2 | [[A Guide to the Front End and [[Basis Swaps|Basis Swap]] Markets#[[Short-Term Rates and the Transition from LIBOR|London Interbank Offered Rate]] (LIBOR)|LIBOR]] × $50 ÷ 2 | -$1.25 million | [[A Guide to the Front End and [[Basis Swaps|Basis Swap]] Markets#[[Short-Term Rates and the Transition from LIBOR|London Interbank Offered Rate]] (LIBOR)|LIBOR]] × $50 ÷ 2 - $1.25 million |

| … | … | … | … |

| 10 | [[A Guide to the Front End and [[Basis Swaps|Basis Swap]] Markets#[[Short-Term Rates and the Transition from LIBOR|London Interbank Offered Rate]] (LIBOR)|LIBOR]] × $50 ÷ 2 + $50 million | -$51.25 million | [[A Guide to the Front End and Basis Swap Markets#London Interbank Offered Rate (LIBOR)|LIBOR]] × $50 ÷ 2 - $1.25 million |

#### Key Insight
- The net cash flows replicate the position of a fixed-rate payer/floating-rate receiver in a swap.

## 5. Summary and Key Takeaways

### 5.1 Hedging Strategies

- [[Futures Not Subject to Cash-And-Carry|Futures]],  protective puts,  and covered calls each offer unique advantages and disadvantages.
- The choice of strategy depends on the manager's market outlook and risk tolerance.
- [[Chapter 4 - Futures: Hedging and Speculation|Futures hedging]] locks in a target price or rate but introduces [[Lessons From The Crisis|basis risk]].
- Protective puts provide [[Equity Linked Note|downside protection]] but require an upfront cost.
- Covered calls generate premium income but limit upside potential.

### 5.2 Interest Rate Swaps

- Swaps are versatile tools for [[Lecture Notes 4-Mechanics of Futures Trading and Fixed Income Derivatives|managing interest rate risk]] and aligning the [[Key Rates O1s Durations and Hedging|duration]] of assets and liabilities.
- They can be interpreted as packages of forward contracts or cash market instruments.
- The [[Fundamentals of Swaps|notional principal]] amount is used to calculate interest payments but is not exchanged.
- Swaps are typically traded OTC,  with standardized contracts cleared through SEFs.

### 5.3 Practical Applications

- [[Partial O1s and PV01|Hedging with swaps]] allows institutions to synthetically manage [[Duration Gap Management|interest rate exposure]] without restructuring their asset and liability mix.
- Swaps provide flexibility in terms of maturity,  structure,  and indices,  making them suitable for a wide range of financial strategies.

By mastering these concepts,  [[An Asset Allocation Primer|portfolio]] managers can effectively manage [[Analysis of Fixed Income Securities|interest rate risk]] and optimize [[An Asset Allocation Primer|portfolio]] performance.

# Lecture Notes: Interest Rate Swaps and Applications in Asset/Liability Management

## 1. Introduction to Interest Rate Swaps

- Interest rate swaps are [[Financial Instruments PSET Solutions|financial derivatives]] that allow counterparties to [[Fundamentals of Swaps|exchange cash flows]] based on a [[Fundamentals of Swaps|notional principal]] amount.
- These instruments are widely used in asset/liability management to manage [[Analysis of Fixed Income Securities|interest rate risk]],  synthetically convert liabilities or assets,  and fine-tune the [[Key Rates O1s Durations and Hedging|duration]] of portfolios.
- This lecture will cover:
  - The mechanics of interest rate swaps.
  - The interpretation of swap positions as combinations of cash market instruments.
  - Applications of swaps in converting [[Uses of Interest Rate Swaps|floating-rate debt]] to fixed-rate debt and vice versa.
  - Innovations in swap markets,  including basis swaps and other advanced instruments.

## 2. Mechanics of Interest Rate Swaps

### 2.1 Key Terminology

- **Trade Date**: The date on which the counterparties commit to the swap.
- **Effective Date**: The date the swap begins accruing interest.
- **Maturity Date**: The date the swap stops accruing interest.
- **Settlement Date**: The date on which cash flows are exchanged.

### 2.2 Structure of a Generic Swap

- **Fixed-Rate Payer**:
  - Pays a [[Chapter 36 - Currency Swaps|fixed interest rate]].
  - Receives a floating interest rate (e.g.,  LIBOR).
  - This position is equivalent to being **short the bond market** because it benefits from rising [[Interest Rate Quotations|interest rates]].
- **Floating-Rate Payer**:
  - Pays a floating interest rate (e.g.,  LIBOR).
  - Receives a [[Chapter 36 - Currency Swaps|fixed interest rate]].
  - This position is equivalent to being **long the bond market** because it benefits from falling [[Interest Rate Quotations|interest rates]].

### 2.3 Cash Flow Mechanics

- **Fixed-Rate Payer Example**:
  - [[Fundamentals of Swaps|Notional principal]]: $50 million.
  - Fixed rate: 5%.
  - Floating rate: 6-month LIBOR.
  - Semiannual payments:
	- Fixed payment: $$\frac{5\%}{2} \times 50,   000,   000 = 1,   250,   000$$
	- Floating payment: $$\text{LIBOR} \times \frac{50,   000,   000}{2}$$
	- Net payment: Difference between fixed and floating payments.

## 3. Interpretation of Swap Positions

### 3.1 Fixed-Rate Payer

- A fixed-rate payer's position can be interpreted as:
  - **Long a floating-rate bond**: Receives floating-rate cash flows.
  - **Short a fixed-rate bond**: Pays fixed-rate cash flows.
- This position benefits from rising [[Interest Rate Quotations|interest rates]] because the fixed-rate liability is locked in at a lower rate.

### 3.2 Floating-Rate Payer

- A floating-rate payer's position can be interpreted as:
  - **Long a fixed-rate bond**: Receives fixed-rate cash flows.
  - **Short a floating-rate bond**: Pays floating-rate cash flows.
- This position benefits from falling [[Interest Rate Quotations|interest rates]] because the floating-rate liability adjusts downward.

## 4. Applications of Interest Rate Swaps

### 4.1 Converting Floating-Rate Debt to Fixed-Rate Debt

- **Objective**: Lock in a fixed liability cost to mitigate the risk of rising [[Interest Rate Quotations|interest rates]].
- **Mechanism**:
  - Enter into a fixed-rate payer/floating-rate receiver swap.
  - The floating-rate liability is offset by the floating-rate inflow from the swap.
  - The net funding cost becomes the fixed rate of the swap.
- **Example**:
  - Floating-rate liability: 3-month [[A Guide to the Front End and [[Basis Swaps|Basis Swap]] Markets#[[Short-Term Rates and the Transition from LIBOR|London Interbank Offered Rate]] (LIBOR)|LIBOR]] + 10 bps (3.10%).
  - Swap terms: Pay fixed at 3.40%,  receive floating at 3-month [[A Guide to the Front End and [[Basis Swaps|Basis Swap]] Markets#[[Short-Term Rates and the Transition from LIBOR|London Interbank Offered Rate]] (LIBOR)|LIBOR]] (3.00%).
  - Net funding cost:
	$$\text{Net Funding Cost} = \text{Floating Liability Cost} + \text{Fixed Rate of Swap} - \text{Floating Rate of Swap}$$
	$$\text{Net Funding Cost} = 3.10\% + 3.40\% - 3.00\% = 3.50\%$$
- **Exhibit 64-2**: Funding costs remain constant at 3.50% across various interest rate scenarios,  demonstrating the effectiveness of the swap.

### 4.2 Converting Fixed-Rate Debt to Floating-Rate Debt

- **Objective**: Align liability costs with floating-rate assets to better match durations.
- **Mechanism**:
  - Enter into a floating-rate payer/fixed-rate receiver swap.
  - The fixed-rate liability is offset by the fixed-rate inflow from the swap.
  - The net funding cost becomes the floating rate of the swap.
- **Example**:
  - Fixed-rate liability: 3.85%.
  - Swap terms: Pay floating at 3-month LIBOR,  receive fixed at 3.70%.
  - Net funding cost:
	$$\text{Net Funding Cost} = \text{Fixed Liability Cost} - \text{Fixed Rate of Swap} + \text{Floating Rate of Swap}$$
	$$\text{Net Funding Cost} = 3.85\% - 3.70\% + \text{LIBOR}$$
	$$\text{Net Funding Cost} = \text{LIBOR} + 0.15\%$$
- **Exhibit 64-3**: Funding costs vary with [[A Guide to the Front End and [[Basis Swaps|Basis Swap]] Markets#[[Short-Term Rates and the Transition from LIBOR|London Interbank Offered Rate]] (LIBOR)|LIBOR]] but maintain a consistent spread of 15 bps over LIBOR.

### 4.3 Basis Swaps

- **Objective**: Manage [[Lessons From The Crisis|basis risk]] when [[Some Stylized Empirical Facts About Asset Retur|asset returns]] and liability costs are based on different benchmarks.
- **Mechanism**:
  - Enter into a floating-to-floating [[Basis Swaps|basis swap]].
  - Example: Receive prime - 150 bps (reset semiannually),  pay 1-month [[A Guide to the Front End and [[Basis Swaps|Basis Swap]] Markets#[[Short-Term Rates and the Transition from LIBOR|London Interbank Offered Rate]] (LIBOR)|LIBOR]] (reset monthly).
- **Exhibit 64-5**: Basis swaps lock in a consistent spread over funding costs,  mitigating the impact of imperfect correlation between benchmarks.

## 5. Swap Pricing and Market Quotes

### 5.1 Quoting Conventions

- Dealers quote swaps by setting the floating rate equal to the index (e.g.,  LIBOR) and quoting the fixed rate.
- **Example**:
  - Fixed-rate payer: Pay 3.85%,  receive LIBOR.
  - Floating-rate payer: Pay LIBOR,  receive 3.75%.
  - Bid/offer spread: 10 bps.

### 5.2 Swap Spread

- The fixed rate is quoted as a spread over the Treasury yield curve.
- **Example**:
  - 10-year Treasury yield: 3.35%.
  - Fixed-rate payer: Pay 3.85% (50 bps over Treasury).
  - Floating-rate payer: Receive 3.75% (40 bps over Treasury).
- Swap spreads are influenced by:
  - Supply and demand dynamics.
  - [[Quantitative Trading Strategies Lecture Notes|Credit risk]] considerations.
  - Market conditions (e.g.,  post-2008 [[Squam Lake Group Letter|financial crisis]]).

## 6. Dollar Duration of a Swap

### 6.1 Definition

- The [[A Guide to Duration DV01 and Yield Curve|dollar duration]] of a swap measures the sensitivity of its value to changes in [[Interest Rate Quotations|interest rates]].
- **Formula**:
 $\text{Dollar Duration of Swap} = \text{Dollar Duration of Fixed-Rate Bond} - \text{Dollar Duration of Floating-Rate Bond}$$

### 6.2 Key Insights

- The [[A Guide to Duration DV01 and Yield Curve|dollar duration]] of the fixed-rate bond dominates because the floating-rate bond's [[Key Rates O1s Durations and Hedging|duration]] is small (less than the time to the next reset date).
- As the reset date approaches,  the floating-rate bond's [[Key Rates O1s Durations and Hedging|duration]] decreases further,  reducing the overall sensitivity of the swap.

## 7. Innovations in Swap Markets

### 7.1 Basis Swaps

- Address [[Lessons From The Crisis|basis risk]] by aligning cash flows indexed to different benchmarks.
- Example: Swap prime-based liabilities for LIBOR-based liabilities.

### 7.2 Yield-Curve Swaps

- Allow counterparties to [[Fundamentals of Swaps|exchange cash flows]] based on different points on the yield curve.
- Example: Pay 2-year Treasury yield,  receive 10-year Treasury yield.

### 7.3 Asset Swaps

- Combine a bond purchase with a swap to convert fixed-rate bond cash flows into floating-rate cash flows or vice versa.

### 7.4 Swaptions

- Options on swaps that provide the right,  but not the obligation,  to enter into a swap at a future date.
- Example: A callable liability can be created by combining a fixed-rate liability with a [[Chapter 39 - Swaptions, Forward Swaps, and MBS|payer swaption]].

## 8. Summary and Key Takeaways

- Interest rate swaps are versatile tools for [[Lecture Notes 4-Mechanics of Futures Trading and Fixed Income Derivatives|managing interest rate risk]] and aligning asset/liability durations.
- Fixed-rate payers are effectively short the bond market,  while floating-rate payers are long the bond market.
- Swaps can synthetically convert [[Uses of Interest Rate Swaps|floating-rate debt]] to fixed-rate debt and vice versa,  providing flexibility in managing funding costs.
- Basis swaps and other innovations address specific risks,  such as [[Lessons From The Crisis|basis risk]] and yield curve mismatches.
- [[Citi-Guide to Swaps|Swap pricing]] is influenced by Treasury yields,  [[Quantitative Trading Strategies Lecture Notes|credit risk]],  and market conditions,  with bid/offer spreads reflecting dealer costs and market dynamics.

By mastering these concepts,  [[Financial Markets and Institutions Lecture Notes|financial institutions]] can effectively use swaps to optimize their balance sheets and manage [[Duration Gap Management|interest rate exposure]].

# Lecture Notes: Advanced Interest Rate Swaps and Swaptions

## 1. Introduction to Advanced Interest Rate Swaps and Swaptions

- Interest rate swaps and swaptions are critical tools in modern [[Financial Markets and Institutions Lecture Notes|financial markets]],  offering flexibility in [[Lecture Notes 4-Mechanics of Futures Trading and Fixed Income Derivatives|managing interest rate risk]] and customizing cash flows.
- This lecture focuses on:
  - Advanced swap structures,  including yield-curve swaps,  amortizing and accreting swaps,  forward swaps,  and equity swaps.
  - The mechanics and applications of swaptions.
  - The valuation of swaps and swaptions using traditional and lattice-based approaches.
  - Practical applications in asset/liability management and [[Key Rates O1s Durations and Hedging|hedging]] strategies.

## 2. Advanced Swap Structures

### 2.1 Yield-Curve Swaps

- **Definition**: A yield-curve swap is a floating-for-floating rate swap where payments are based on [[Interest Rate Quotations|interest rates]] at two different points on the yield curve.
- **Mechanics**:
  - Party A agrees to receive the six-month Treasury bill rate and pay Party B the 10-year Treasury yield minus 200 basis points.
  - Both rates reset every six months.
- **Example**:
  - At a reset date:
	- Six-month T-bill rate = 2.5%.
	- 10-year Treasury yield = 4%.
	- Party A receives 2.5% and pays 2% (4% - 200 bps).
  - If the yield curve flattens:
	- Six-month T-bill rate = 3%.
	- 10-year Treasury yield = 3.5%.
	- Party A receives 3% and pays 1.5% (3.5% - 200 bps).
- **Applications**:
  - Used to hedge or speculate on changes in the shape of the yield curve.
  - Common in managing [[Key Rates O1s Durations and Hedging|duration]] mismatches in portfolios.

### 2.2 Amortizing and Accreting Swaps

#### 2.2.1 Amortizing Swaps
- **Definition**: A swap where the [[Fundamentals of Swaps|notional principal]] decreases over time,  aligning with the amortization of an [[Risk Neutral Pricing of Options|underlying asset]] (e.g.,  mortgage loans).
- **Purpose**:
  - Matches the declining principal balance of amortizing assets,  such as [[Fremont Financial Corp. (b)|mortgage-backed securities]] (MBS) or [[Other MBS|collateralized mortgage obligations]] (CMOs).
  - Reduces the risk of being overhedged or underhedged due to changes in asset [[Mortgage Pools|prepayment rates]].
- **Mechanics**:
  - The notional amount decreases according to a predefined schedule.
  - [[Chapter 34 - Pricing Interest Rate Swaps|Swap cash flows]] adjust based on the reduced notional amount.
- **Example**:
  - Initial notional = $100 million.
  - Year 1: Notional = $80 million.
  - Year 2: Notional = $60 million.
- **Challenges**:
  - [[Risk Factors and Hedging Agency MBS|Prepayment risk]] can lead to mismatches if the actual amortization differs from the predefined schedule.
  - Balance-guaranteed swaps address this by tying the notional amount to the actual outstanding balance of a reference asset pool.

#### 2.2.2 Accreting Swaps
- **Definition**: A swap where the [[Fundamentals of Swaps|notional principal]] increases over time,  often used to hedge liabilities that grow incrementally.
- **Applications**:
  - Common in the construction industry to hedge floating-rate drawdown facilities.
  - Aligns with increasing liability schedules.

### 2.3 Forward Swaps

- **Definition**: A [[Chapter 39 - Swaptions, Forward Swaps, and MBS|forward swap]] is a swap agreement with a delayed start date.
- **Purpose**:
  - Hedge future funding requirements or anticipated debt issuance.
  - Lock in current [[Interest Rate Quotations|interest rates]] for future periods.
- **Example**:
  - A firm has $200 million of fixed-rate debt maturing in three years.
  - To lock in funding costs for the subsequent five years,  the firm enters into a [[Chapter 39 - Swaptions, Forward Swaps, and MBS|forward swap]] to pay fixed and receive floating starting three years from now.
  - If rates rise,  the firm issues [[Uses of Interest Rate Swaps|floating-rate debt]] and converts it to fixed-rate liability using the swap.

### 2.4 Equity Swaps

- **Definition**: An [[Equity Commodity and Exotic Swaps|equity swap]] involves exchanging cash flows based on the total return of a [[Hedge Fund Strategies|stock market]] index and an interest rate (fixed or floating).
- **Mechanics**:
  - One party receives the total return on an equity index (e.g.,  S&P 500,  DAX) and pays an interest rate (e.g.,  LIBOR).
  - Payments can be denominated in different currencies.
- **Example**:
  - A money manager enters a two-year quarterly reset [[Equity Commodity and Exotic Swaps|equity swap]]:
	- Receives the German DAX index return in euros.
	- Pays [[A Guide to the Front End and [[Basis Swaps|Basis Swap]] Markets#[[Short-Term Rates and the Transition from LIBOR|London Interbank Offered Rate]] (LIBOR)|LIBOR]] in euros.
- **Applications**:
  - Used to gain synthetic exposure to [[An Introduction to Equity Markets|equity markets]] without directly holding the underlying assets.
  - Facilitates cross-border investments and [[Foreign Exchange Reserves|currency diversification]].

## 3. Swaptions: Mechanics and Applications

### 3.1 Definition and Types

- **Definition**: A swaption is an option to enter into a swap at a future date.
- **Types**:
  - **[[Chapter 39 - Swaptions, Forward Swaps, and MBS|Payer Swaption]]**: The right to pay fixed and receive floating.
  - **Receiver Swaption**: The right to receive fixed and pay floating.
  - **Cancellation Swaption**: The right to cancel an existing swap.

### 3.2 Exercise Styles

- **European Swaption**: Exercisable only on a specific date.
- **American Swaption**: Exercisable at any time up to and including the [[Risk Neutral Pricing of Options|expiration date]].
- **Example**:
  - A seven-year swaption allows the holder to pay fixed at 4% at any time before maturity.
  - If exercised after one year,  the holder pays 4% and receives [[A Guide to the Front End and [[Basis Swaps|Basis Swap]] Markets#[[Short-Term Rates and the Transition from LIBOR|London Interbank Offered Rate]] (LIBOR)|LIBOR]] for the remaining six years.

### 3.3 Applications

#### 3.3.1 Liability Management
- **[[Key Rates O1s Durations and Hedging|Hedging]] Uncertain Funding Requirements**:
  - Lock in current rates without committing to future borrowing.
  - Example: A firm purchases a [[Chapter 39 - Swaptions, Forward Swaps, and MBS|payer swaption]] to hedge against rising rates for anticipated debt issuance.
- **Issuing Callable Debt**:
  - Corporations issue callable bonds and strip off the embedded call option by writing a swaption,  reducing the all-in cost of debt.

#### 3.3.2 Asset Management
- **[[Key Rates O1s Durations and Hedging|Hedging]] Prepayable Assets**:
  - Investors holding prepayable assets (e.g.,  MBS) can use swaptions to hedge against [[Risk Factors and Hedging Agency MBS|prepayment risk]].
  - Example: Purchase a receiver swaption to offset the impact of declining [[Interest Rate Quotations|interest rates]] on prepayment-sensitive assets.

#### 3.3.3 Arbitrage Opportunities
- Exploit [[Arbitrage Pricing of Derivatives|pricing]] inefficiencies between the swaption and callable bond markets.
- Example: Issue callable debt and write a swaption to strip off the embedded call option.

### 3.4 Comparison with Caps and Floors

- **Caps**:
  - Provide protection against rising rates by capping the maximum interest rate.
  - More expensive than swaptions because they consist of a strip of options.
- **Swaptions**:
  - Offer flexibility to enter into a swap at a future date.
  - Less expensive than caps but expose the holder to rate movements after exercise.

## 4. Valuation of Swaps and Swaptions

### 4.1 Traditional Valuation Approach

- **Method**:
  - Discount [[Advanced Derivatives Pricing Methodology|future cash flows]] using [[Forwards and Futures Notes|implied forward rates]] derived from [[Convexity-Adjusted Models for LIBOR Forwards Qu|Eurodollar futures]].
  - Compute the swap fixed rate (SFR) as the rate that equates the present value of fixed and floating cash flows.
- **Limitations**:
  - Cannot handle cash flows that depend on [[Forward Rate|future interest rate]] movements.

### 4.2 Lattice-Based Valuation Approach

- **[[Overview of Financial Markets|Overview]]**:
  - Incorporates [[Fixed Income Versus Equity Derivatives|interest rate volatility]] to model [[Forward Rate|future rate]] movements.
  - Constructs an interest-rate lattice to represent possible rate paths.
- **Steps**:
  1. Build the interest-rate lattice using a [[Profit and Loss Attribution with an OAS|one-factor model]] (e.g.,  Kalotay-Williams-Fabozzi model).
  1. Compute [[Chapter 34 - Pricing Interest Rate Swaps|swap cash flows]] at each node on the lattice.
  1. Discount cash flows backward through the lattice to determine present value.
- **Advantages**:
  - Handles [[Exotic Interest Rate Options|exotic]] instruments with option-like features.
  - Incorporates no-[[Arbitrage Pricing of Derivatives|arbitrage]] conditions and [[Fixed Income Versus Equity Derivatives|interest rate volatility]].

### 4.3 Example: Swaption Valuation

- **Inputs**:
  - [[Fundamentals of Swaps|Notional principal]]: $100 million.
  - Strike rate: 5%.
  - [[Chapter 16 - Black–Scholes Model|Time to expiration]]: 2 years.
  - Volatility: 20%.
- **Process**:
  - Construct a [[A Real-Life Option Pricing Exercise|binomial]] interest-rate lattice.
  - Calculate [[Chapter 34 - Pricing Interest Rate Swaps|swap cash flows]] at each node.
  - Discount cash flows to determine the swaption's present value.
- **Impact of Volatility**:
  - Higher volatility increases the value of the swaption due to greater potential rate movements.

## 5. Termination of Interest Rate Swaps

### 5.1 Reverse Swap

- **Definition**: Entering into an offsetting swap to neutralize the original swap's cash flows.
- **Example**:
  - Original swap: Pay fixed at 5.4%,  receive LIBOR.
  - Reverse swap: Receive fixed at 6.4%,  pay LIBOR.
  - Profit: 1% of the notional amount annually for the remaining term.

### 5.2 Swap Sale

- **Definition**: Selling the swap in the [[Primary Issuance and Secondary Resale Markets|secondary market]] for a profit or loss.
- **Valuation**:
  - Termination value = Present value of the annuity (difference between old and new fixed rates) discounted at the current [[Teaching Note 4 Interest Rate Derivatives|swap rate]].

## 6. Summary and Key Takeaways

- Advanced swap structures,  such as yield-curve swaps,  amortizing swaps,  and forward swaps,  provide tailored solutions for [[Lecture Notes 4-Mechanics of Futures Trading and Fixed Income Derivatives|managing interest rate risk]].
- Swaptions offer flexibility in [[Key Rates O1s Durations and Hedging|hedging]] and liability management,  bridging the gap between swaps and [[Black Models for Bond Price Options Capsfloors|caps/floors]].
- The lattice-based valuation approach incorporates [[Fixed Income Versus Equity Derivatives|interest rate volatility]],  enabling the [[Arbitrage Pricing of Derivatives|pricing]] of complex instruments.
- Termination strategies,  including reverse swaps and swap sales,  allow firms to manage or exit swap positions efficiently.

By mastering these advanced concepts,  financial professionals can effectively navigate the complexities of interest rate [[Chapter 9 Arbitrage and Hedging With Options|derivatives]] and optimize their [[Banks' Bonds Playing Role as I|risk management strategies]].

# Lecture Notes: Valuation of Interest Rate Swaps and Forward Start Swaps Using a Binomial Lattice

## 1. Introduction to Interest Rate Swaps and Forward Start Swaps

- Interest rate swaps are derivative instruments that allow counterparties to exchange fixed and floating interest rate payments based on a [[Fundamentals of Swaps|notional principal]] amount.
- Forward start swaps are a variation of interest rate swaps that begin at a specified future date and are used to hedge or lock in [[Interest Rate Quotations|interest rates]] for future periods.
- This lecture focuses on:
  - The valuation of a five-year plain vanilla [[Primer on Interest Rate Swaps|interest rate swap]] using a [[A Real-Life Option Pricing Exercise|binomial]] [[Chapter 41 - Pricing Fixed Income Derivatives: BOPM|interest rate lattice]].
  - The valuation of a forward start swap using the same lattice framework.
  - The mechanics of calculating cash flows,  cumulative swap valuation,  and probabilities in the lattice.

## 2. Valuation of a Five-Year Plain Vanilla Interest Rate Swap

### 2.1 Overview of the Swap

- **Swap Details**:
  - [[Fundamentals of Swaps|Notional Principal]] (NP): $100
  - Swap Fixed Rate (SFR): 3%
  - Tenor: 5 years
  - Settlement Frequency: Semiannual
  - [[An Overview of the Vasicek Short Rate Model|Interest Rate Model]]: One-factor [[6. A Brief Introduction to Stochastic Calculus|binomial lattice]] with 10 semiannual time steps.
- **Key Assumptions**:
  - Semiannual cash flows with a fraction of the year equal to 0.5.
  - Cash flows are determined at the start of each period but paid in arrears at the end of the period.

### 2.2 Cash Flow Calculation

- **Fixed-Rate Payment**:
 $\text{Fixed-Rate Payment} = \text{SFR} \times \text{NP} \times \left(\frac{\text{Days in Period}}{360}\right)$$
 $\text{Fixed-Rate Payment} = 3\% \times 100 \times 0.5 = 1.5$$

- **Floating-Rate Payment**:
 $\text{Floating-Rate Payment} = \text{Floating Rate} \times \text{NP} \times \left(\frac{\text{Days in Period}}{360}\right)$$

- **Net [[Preview of the Book|Cash Flow]]**:
 $\text{Net Cash Flow} = (\text{Floating Rate} - \text{SFR}) \times \text{NP} \times \left(\frac{\text{Days in Period}}{360}\right)$$

- **Example**:
  - At $t=4.5$ years,  the [[An Overview of the Vasicek Short Rate Model|short rate]] is 9.1446%.
  - Net [[Preview of the Book|Cash Flow]]:
	$$\text{Net Cash Flow} = (9.1446\% - 3.0\%) \times 100 \times 0.5 = 3.0723$$

### 2.3 Cumulative Swap Valuation Lattice

- **Purpose**:
  - The cumulative swap valuation lattice calculates the present value of all [[Advanced Derivatives Pricing Methodology|future cash flows]] at each node,  discounted using the rates in the [[6. A Brief Introduction to Stochastic Calculus|binomial lattice]].
- **Discounting Cash Flows**:
 $\text{Present Value} = \frac{\text{Cash Flow}}{1 + \text{Short Rate}/2}$$

- **Example**:
  - At $t=4.5$ years,  the [[Preview of the Book|cash flow]] at $t=5$ years is $3.0723$.
  - Discounted Value:
	$$\text{PV} = \frac{3.0723}{1 + 9.1446\%/2} = 2.9380$$

- **Backward Induction**:
  - At each node,  the cumulative value is the sum of:
	1. The discounted values of the two possible future nodes (weighted equally).
	1. The [[Preview of the Book|cash flow]] at the current node.

- **Example**:
  - At $t=4$,  the cumulative value is:
	$$\text{Cumulative Value} = \frac{0.5 \times 2.9380 + 0.5 \times 2.3750 + 2.3104}{1 + 7.6208\%/2} = 4.7846$$

### 2.4 Swap Valuation at $t=0$

- **Final Value**:
  - The present value of the swap at $t=0$ is the cumulative value at the root of the lattice.
  - For the given swap:
	$$\text{Swap Value} = 1.5892$$

- **Interpretation**:
  - The negative value indicates that the fixed-rate payer is at a disadvantage because the present value of fixed payments exceeds the present value of floating payments.
  - This occurs because [[Interest Rate Quotations|interest rates]] have declined since the swap was initiated.

## 3. Valuation of a Forward Start Swap

### 3.1 Overview of the Forward Start Swap

- **Swap Details**:
  - [[Fundamentals of Swaps|Notional Principal]] (NP): $100
  - [[Chapter 39 - Swaptions, Forward Swaps, and MBS|Forward Swap]] Fixed Rate (SFR): 3.250%
  - Start Date: 3 years from today
  - Maturity Date: 5 years from today
  - Settlement Frequency: Semiannual
- **Key Assumptions**:
  - The forward start swap begins at $t=3$ years,  so cash flows are calculated for the period $t=3$ to $t=5$.
  - The valuation process uses the same [[6. A Brief Introduction to Stochastic Calculus|binomial lattice]] as the plain vanilla swap.

### 3.2 Cumulative Swap Valuation Lattice

- **Steps**:
  1. Calculate the cash flows at each node for the period $t=3$ to $t=5$.
  1. Construct the cumulative valuation lattice for the forward start swap,  starting at $t=5$ and working backward to $t=3$.

- **Example**:
  - At $t=4.5$,  the [[An Overview of the Vasicek Short Rate Model|short rate]] is 9.1446%.
  - Net [[Preview of the Book|Cash Flow]]:
	$$\text{Net Cash Flow} = (9.1446\% - 3.250\%) \times 100 \times 0.5 = 2.9473$$
  - Discounted Value:
	$$\text{PV} = \frac{2.9473}{1 + 9.1446\%/2} = 2.8160$$

### 3.3 Probability of Reaching Each Node

- **Formula**:
 $\text{Number of Paths} = \frac{n!}{j!(n-j)!}$$
  - $n$: Total number of time steps.
  - $j$: Number of down movements.
- **Example**:
  - At $t=3$,  the total number of paths is $2^6 = 64$.
  - For the second node from the top:
	$$\text{Number of Paths} = \frac{6!}{1!(5!)} = 6$$
  - Probability:
	$$\text{Probability} = \frac{\text{Number of Paths}}{\text{Total Paths}} = \frac{6}{64} = 0.09375$$

### 3.4 Forward Start Swap Valuation at $t=3$

- **Weighted Value**:
  - The value of the forward start swap is the probability-weighted sum of the cumulative values at $t=3$.
  - Example:
	- Node 1: Cumulative Value = $2.8160$,  Probability = $0.09375$.
	- Node 2: Cumulative Value = $2.3750$,  Probability = $0.1875$.
	- Total Value:
	 $\text{Forward Start Swap Value} = \sum (\text{Cumulative Value} \times \text{Probability}) = 1.87089$$

- **Interpretation**:
  - The positive value indicates that the floating-rate payments are expected to exceed the fixed-rate payments.

## 4. Summary and Key Takeaways

### 4.1 Plain Vanilla Swap

- The valuation of a plain vanilla swap involves:
  - Calculating cash flows at each node based on the [[Chapter 41 - Pricing Fixed Income Derivatives: BOPM|interest rate lattice]].
  - Constructing a cumulative valuation lattice using backward induction.
  - Discounting [[Advanced Derivatives Pricing Methodology|future cash flows]] to determine the present value of the swap.
- The swap value reflects the difference between the present value of fixed and floating payments.

### 4.2 Forward Start Swap

- The valuation of a forward start swap involves:
  - Calculating cash flows for the forward period.
  - Constructing a cumulative valuation lattice starting at the forward start date.
  - Weighting cumulative values by the probability of reaching each node.
- The forward start swap value reflects the expected difference between fixed and floating payments during the forward period.

### 4.3 Practical Applications

- **Plain Vanilla Swaps**:
  - Used to hedge [[Analysis of Fixed Income Securities|interest rate risk]] or align asset and liability durations.
- **Forward Start Swaps**:
  - Used to lock in [[Interest Rate Quotations|interest rates]] for future funding requirements or anticipated liabilities.

By mastering these valuation techniques,  financial professionals can effectively manage [[Analysis of Fixed Income Securities|interest rate risk]] and optimize their derivative strategies.

# Lecture Notes: Advanced Valuation of Swaps,  Swaptions,  and Basis Swaps

## 1. Introduction to Advanced Swap Valuation

- This lecture focuses on the valuation of advanced swap structures,  including forward start swaps,  swaptions,  and basis swaps.
- We will explore:
  - The probability-weighted valuation of forward start swaps using a [[6. A Brief Introduction to Stochastic Calculus|binomial lattice]].
  - The valuation of swaptions,  including pay-fixed and receive-fixed swaptions.
  - The mechanics of basis swaps,  including the valuation of pay [[A Guide to the Front End and [[Basis Swaps|Basis Swap]] Markets#[[Short-Term Rates and the Transition from LIBOR|London Interbank Offered Rate]] (LIBOR)|LIBOR]] TED swaps.
- The lattice approach is emphasized for its flexibility in handling complex swap structures and varying [[Preview of the Book|cash flow]] assumptions.

## 2. Valuation of Forward Start Swaps (FSS)

### 2.1 Overview of Forward Start Swaps

- A forward start swap (FSS) is a swap that begins at a specified future date.
- **Key Features**:
  - The fixed-rate (SFR) is determined at the time of valuation.
  - The FSS allows counterparties to lock in [[Interest Rate Quotations|interest rates]] for future periods.
- **Example**:
  - [[Fundamentals of Swaps|Notional Principal]]: $100
  - Swap Fixed Rate (SFR): 3.250%
  - Start Date: 3 years from today
  - Maturity Date: 5 years from today
  - Settlement Frequency: Semiannual

### 2.2 Probability-Weighted Valuation of FSS

#### 2.2.1 Cumulative Swap Valuation at Year 3

- The cumulative swap valuation at year 3 is calculated using the [[6. A Brief Introduction to Stochastic Calculus|binomial lattice]] approach.
- **Exhibit 6S-6** provides the cumulative valuation for each node at year 3,  along with the probability of arriving at each node.

| **Node** | **Cumulative Swap Valuation** | **Number of Paths** | **Probability** | **Probability-Weighted Value** |

| 1 | 5.8014 | 1 | 1.56% | 0.09065 |

| 2 | 4.2874 | 6 | 9.38% | 0.40194 |

| 3 | 2.9476 | 15 | 23.44% | 0.69085 |

| 4 | 1.7650 | 20 | 31.25% | 0.55156 |

| 5 | 0.7233 | 15 | 23.44% | 0.16952 |

| 6 | -0.1926 | 6 | 9.38% | -0.01805 |

| 7 | -0.9964 | 1 | 1.56% | -0.01557 |

| **Total**| **14.3356** | **64** | **100.00%** | **1.87089** |

#### 2.2.2 Interpretation of Results

- The total probability-weighted value of the FSS at year 3 is **1.87089**.
- This value represents the present value of the [[Week 6 Assignment Review|expected cash flows]] for the fixed-rate payer.
- The value for the floating-rate payer is the negative of this amount: **-1.87089**.

#### 2.2.3 Swap Fixed Rate (SFR) for Zero Value

- The SFR that would produce a zero value for the FSS is **4.233%**.
- This is computed iteratively,  similar to the process for valuing a plain vanilla swap.

## 3. Valuation of Swaptions

### 3.1 Overview of Swaptions

- A **swaption** is an option contract on an [[Primer on Interest Rate Swaps|interest rate swap]].
- **Key Features**:
  - The swaption specifies the tenor of the swap and the swap fixed rate (strike rate).
  - The owner has the right,  but not the obligation,  to enter into the swap.
  - Swaptions can be **European-style** (exercisable only at expiration) or **American-style** (exercisable at any time up to expiration).

#### 3.1.1 Types of Swaptions
- **[[Chapter 39 - Swaptions, Forward Swaps, and MBS|Payer Swaption]]**: The right to pay fixed and receive floating.
- **Receiver Swaption**: The right to receive fixed and pay floating.

### 3.2 Example: Valuation of a Pay-Fixed Swaption

#### 3.2.1 Swaption Details

- **Strike Rate**: 3.650%
- **Option Expiration**: 2 years
- **Swap Tenor**: 3 years
- **[[Fundamentals of Swaps|Notional Principal]]**: $100

#### 3.2.2 Cash Flow Lattice for Plain Vanilla Swap

- The [[Preview of the Book|cash flow]] lattice is constructed for a plain vanilla swap with a strike rate of 3.650%.
- **Formula**:
 $\text{Cash Flow}*{i,  j} = (\text{Floating Rate}*{i,  j-1} - \text{SFR}) \times \text{NP} \times 0.5$$
- **Example**:
  - At $t=5$,  the floating rate at $t=4.5$ is 9.1446%.
  - [[Preview of the Book|Cash Flow]]:
	$$\text{Cash Flow}_{1,   5} = (9.1446\% - 3.650\%) \times 100 \times 0.5 = 2.7473$$

#### 3.2.3 Cumulative Swap Valuation Lattice

- The cumulative swap valuation lattice is constructed using backward induction.
- **Example**:
  - At $t=2.5$,  the top value is computed as:
	$$0.5 \times (5.058457 + 3.537322) / (1 + 4.4031\% / 2) = 4.205307$$

#### 3.2.4 Swaption Valuation at Expiration

- At expiration ($t=3$),  the swaption value is the maximum of zero or the cumulative swap valuation.
- **Example**:
  - At the bottom node ($t=3$),  the cumulative valuation is 0.7711.
  - Swaption Value:
	$$\text{Value} = \max(0,    0.7711) = 0.7711$$

#### 3.2.5 Final Swaption Value

- Using backward induction,  the value of the (3,  2) pay-fixed swaption is **1.170195** per $100 of [[Fundamentals of Swaps|notional principal]].

## 4. Valuation of Basis Swaps

### 4.1 Overview of Basis Swaps

- A **[[Basis Swaps|basis swap]]** involves the exchange of floating-rate payments based on different benchmarks.
- **Example**:
  - A [[A Guide to the Front End and [[Basis Swaps|Basis Swap]] Markets#[[Short-Term Rates and the Transition from LIBOR|London Interbank Offered Rate]] (LIBOR)|LIBOR]] TED swap exchanges payments based on [[A Guide to the Front End and [[Basis Swaps|Basis Swap]] Markets#[[Short-Term Rates and the Transition from LIBOR|London Interbank Offered Rate]] (LIBOR)|LIBOR]] and the 90-day Treasury bill rate plus a spread.

### 4.2 Example: Valuation of a Pay [[A Guide to the Front End and Basis Swap Markets#London Interbank Offered Rate (LIBOR)|LIBOR]] TED Swap

#### 4.2.1 Swap Details

- **Spread**: 0.376%
- **[[Fundamentals of Swaps|Notional Principal]]**: $100
- **Tenor**: 1 year
- **Payment Frequency**: Quarterly

#### 4.2.2 Interest Rate Lattices

- Separate lattices are constructed for [[A Guide to the Front End and [[Basis Swaps|Basis Swap]] Markets#[[Short-Term Rates and the Transition from LIBOR|London Interbank Offered Rate]] (LIBOR)|LIBOR]] and the Treasury bill rate.
- **Example**:
  - At the highest node ($t=1$),   [[A Guide to the Front End and [[Basis Swaps|Basis Swap]] Markets#[[Short-Term Rates and the Transition from LIBOR|London Interbank Offered Rate]] (LIBOR)|LIBOR]] = 1.01%,  Treasury bill rate = 0.29%.

#### 4.2.3 Cash Flow Calculation

- **Formula**:
 $\text{CF}*{i,  j} = (\text{T-Bill}*{i,  j-1} + \text{Spread} - \text{LIBOR}_{i,  j-1}) \times 0.25 \times \text{NP}$$
- **Example**:
  - At the highest node ($t=1$):
	$$\text{CF}_{i,   j} = (0.29\% + 0.376\% - 1.01\%) \times 0.25 \times 100 = -0.085$$

#### 4.2.4 Cumulative Value Lattice

- The cumulative value lattice is constructed using backward induction.
- The spread of 0.376% ensures that the present value of the two payment streams is equal,  resulting in a zero value for the swap.

## 5. Summary and Key Takeaways

### 5.1 Forward Start Swaps

- Forward start swaps allow counterparties to lock in [[Interest Rate Quotations|interest rates]] for future periods.
- The valuation involves constructing a cumulative swap valuation lattice and calculating probability-weighted values.

### 5.2 Swaptions

- Swaptions provide the right,  but not the obligation,  to enter into a swap.
- The lattice approach is flexible and can handle variations such as amortizing or accreting notional principals.

### 5.3 Basis Swaps

- Basis swaps involve the exchange of floating-rate payments based on different benchmarks.
- The spread is adjusted to ensure that the present value of the two legs is equal.

By mastering these valuation techniques,  financial professionals can effectively manage complex interest rate risks and optimize their derivative strategies.

# Lecture Notes: Advanced Valuation of Swaps,  Swaptions,  and Interest-Rate Options

## 1. Introduction to Swaps,  Swaptions,  and Interest-Rate Options

- Swaps,  swaptions,  and interest-rate options are critical tools in fixed-income markets,  enabling investors to manage interest-rate risk,  hedge liabilities,  and speculate on rate movements.
- This lecture focuses on:
  - The valuation of swaps and swaptions using the lattice approach.
  - The sensitivity of swaption values to key factors such as volatility and strike rate.
  - The basics of interest-rate options,  including their [[Arbitrage Pricing of Derivatives|pricing]],  risk/return profiles,  and [[Key Rates O1s Durations and Hedging|hedging]] strategies.
- We will also explore the foundational concepts of option [[Arbitrage Pricing of Derivatives|pricing]],  including intrinsic value,  time value,  and the impact of volatility.

## 2. Factors Affecting Swaption Valuation

### 2.1 Overview of Swaption Valuation

- Swaptions are option contracts that provide the right,  but not the obligation,  to enter into a swap agreement in the future.
- The value of a swaption is influenced by:
  - **Market Inputs**: [[6. A Brief Introduction to Stochastic Calculus|Term structure of interest rates]] and interest-rate volatility.
  - **Contract Specifications**: Tenor,  strike rate,  and [[Risk Neutral Pricing of Options|expiration date]].
- The lattice approach is a flexible framework for valuing swaptions,  as it can handle variations in [[Exotic Interest Rate Options|exotic]] swaps and changing market conditions.

### 2.2 Sensitivity to Interest-Rate Volatility

- **Key Insight**: Holding all else constant,  an increase in interest-rate volatility increases the value of a swaption.
- **Mechanism**:
  - Higher volatility increases the probability of the underlying swap moving in-the-money,  thereby increasing the swaption's time value.
- **Example**:
  - Exhibit 65-14 illustrates the effect of volatility on pay-fixed swaptions with a strike rate of 3.5%.
  - As volatility increases,  the value of the swaption rises,  regardless of the [[Risk Neutral Pricing of Options|expiration date]].

### 2.3 Sensitivity to Strike Rate

- **Pay-Fixed Swaptions**:
  - As the strike rate increases,  the value of the pay-fixed swaption decreases.
  - This occurs because higher strike rates reduce the likelihood of the fixed-rate payments being advantageous relative to the floating-rate payments.
- **Receive-Fixed Swaptions**:
  - As the strike rate increases,  the value of the receive-fixed swaption increases.
  - This is because higher strike rates make the fixed-rate payments more attractive relative to the floating-rate payments.
- **Example**:
  - Exhibit 65-15 shows the joint effect of strike rate and volatility on the value of a (2,  3) pay-fixed swaption.
  - Exhibit 65-16 demonstrates the opposite relationship for a (2,  3) receive-fixed swaption.

### 2.4 Combined Effects of Volatility and Strike Rate

- **Surface Plots**:
  - Exhibit 65-15 (Pay-Fixed Swaption): Value increases with volatility and decreases with strike rate.
  - Exhibit 65-16 (Receive-Fixed Swaption): Value increases with both volatility and strike rate.
- **Key Takeaway**:
  - Volatility has a positive impact on both pay-fixed and receive-fixed swaptions.
  - Strike rate has opposite effects on the two types of swaptions.

## 3. Basics of Interest-Rate Options

### 3.1 Definition and Types

- An **option** is the right,  but not the obligation,  to buy or sell a security at a fixed price ([[Call and Put Payoffs at Expiry|strike price]]) before or at expiration.
- **Types**:
  - **Call Option**: The right to buy the underlying security.
  - **Put Option**: The right to sell the underlying security.
- **Exercise Styles**:
  - **American Options**: Exercisable at any time up to expiration.
  - **European Options**: Exercisable only at expiration.

### 3.2 Profit/Loss Profiles

- **Call Option**:
  - Profit increases as the price of the underlying security rises above the [[Call and Put Payoffs at Expiry|strike price]].
  - Break-even price = [[Call and Put Payoffs at Expiry|Strike price]] + Premium paid.
  - Example: Exhibit 66-1 shows the profit/loss graph for a call struck at par with a 1-point premium.
- **Put Option**:
  - Profit increases as the price of the underlying security falls below the [[Call and Put Payoffs at Expiry|strike price]].
  - Break-even price = [[Call and Put Payoffs at Expiry|Strike price]] - Premium paid.
  - Example: Exhibit 66-2 shows the profit/loss graph for a put struck at par with a 1-point premium.

### 3.3 Put-Call Parity

- **Definition**: [[7. Black Scholes Model|Put-call parity]] is a fundamental relationship in options [[Arbitrage Pricing of Derivatives|pricing]] that links the prices of calls,  puts,  and the underlying security.
- **Formula**:
 $\text{Long Security} = \text{Long Call} + \text{Short Put}$$
- **Implications**:
  - A call can be created from a put by buying the underlying security.
  - A put can be created from a call by selling the underlying security.
- **Exhibits**:
  - Exhibit 66-3: Long Security = Long Call + Short Put.
  - Exhibit 66-4: Long Call = Long Security + Long Put.
  - Exhibit 66-5: Long Put = Short Security + Long Call.

## 4. Valuing an Option

### 4.1 Determinants of Option Value

- **Key Factors**:
  - **Price of the Underlying**: Higher prices increase call values and decrease put values.
  - **[[Call and Put Payoffs at Expiry|Strike Price]]**: Higher strike prices decrease call values and increase put values.
  - **[[Chapter 16 - Black–Scholes Model|Time to Expiration]]**: Longer time increases the option's time value.
  - **Volatility**: Higher volatility increases the option's time value.
  - **Carry**: Positive carry decreases call values and increases put values.
- **Exhibit 66-10** summarizes the effects of these factors on [[Notes on Basic Options Properties|call and put]] values.

### 4.2 Intrinsic Value and Time Value

- **Intrinsic Value**:
  - The value of the option if exercised immediately.
  - For calls: $$\text{Intrinsic Value} = \max(0,    \text{Underlying Price} - \text{Strike Price})$$
  - For puts: $$\text{Intrinsic Value} = \max(0,    \text{Strike Price} - \text{Underlying Price})$$
- **Time Value**:
  - The additional value due to the time remaining until expiration.
  - Time value decreases as expiration approaches (Exhibit 66-6).

### 4.3 Impact of Volatility

- **Definition**: Volatility measures the variability of the underlying security's price.
- **Effect on Option Value**:
  - Higher volatility increases the probability of the option expiring in-the-money.
  - At-the-money options are most sensitive to changes in volatility.
- **Exhibit 66-8**: Call option value increases with volatility for at-the-money,  in-the-money,  and out-of-the-money options.

### 4.4 Impact of Carry

- **Definition**: Carry is the difference between the [[Realized Returns|coupon payments]] on a security and the cost of financing its purchase.
- **Effect on Option Value**:
  - Positive carry decreases call values and increases put values.
  - Negative carry (e.g.,  inverted yield curve) has the opposite effect.
- **Exhibit 66-9**: Compares the cost of at-the-money calls and puts across different financing rates.

## 5. Delta,  Gamma,  and Theta: Hedging an Option Position

### 5.1 Delta

- **Definition**: Delta measures the sensitivity of an option's value to changes in the price of the underlying security.
- **Formula**:
 $\Delta = \frac{\Delta \text{Option Value}}{\Delta \text{Underlying Price}}$$
- **Key Insights**:
  - At-the-money calls have a delta of approximately 0.5.
  - Deeply in-the-money calls have a delta close to 1.
  - Deeply out-of-the-money calls have a delta close to 0.
- **[[Financial Instruments|Delta Hedging]]**:
  - A delta-neutral position is created by offsetting the delta of the option with an opposing position in the underlying security.

### 5.2 Gamma

- **Definition**: Gamma measures the rate of change of delta with respect to changes in the underlying price.
- **Key Insights**:
  - High gamma indicates greater sensitivity of delta to price changes.
  - Gamma is highest for at-the-money options near expiration.

### 5.3 Theta

- **Definition**: Theta measures the rate of change of an option's value with respect to time.
- **Key Insights**:
  - Theta is negative for long options positions,  as time decay reduces the option's value.
  - Time decay accelerates as expiration approaches.

## 6. Summary and Key Takeaways

### 6.1 Swaps and Swaptions

- Swaptions are valued using the lattice approach,  which accounts for interest-rate volatility and strike rate.
- Volatility increases swaption values,  while the strike rate has opposite effects on pay-fixed and receive-fixed swaptions.

### 6.2 Interest-Rate Options

- Option value is determined by intrinsic value,  time value,  volatility,  and carry.
- [[7. Black Scholes Model|Put-call parity]] links the prices of calls,  puts,  and the underlying security.
- Delta,  gamma,  and theta are essential metrics for managing option positions.

By mastering these concepts,  financial professionals can effectively use swaps,  swaptions,  and options to manage risk and optimize [[An Asset Allocation Primer|portfolio]] performance.

complex than calculating empirical volatility. [[A Real-Life Option Pricing Exercise|Implied volatility]] is derived by solving the option [[Arbitrage Pricing of Derivatives|pricing]] model (e.g.,  [[Mathematical Modeling of Derivative Pricing|Black-Scholes]] or [[A Real-Life Option Pricing Exercise|binomial]] models) for the volatility input that equates the theoretical price of the option to its observed market price. This process requires iterative numerical methods,  as the relationship between volatility and option price is nonlinear.

## 1. Introduction to Volatility in Fixed Income Markets

- Volatility is a critical input in the valuation of options and the design of option strategies. It measures the uncertainty or risk associated with changes in the price or yield of a security.
- In [[A Practical Guide to Bonds and Swaps|fixed income markets]],  volatility is expressed in terms of either price or yield,  and it can be measured on an absolute or percentage basis.
- There are two primary types of volatility:
  - **Empirical Volatility**: Historical volatility based on observed market data.
  - **[[A Real-Life Option Pricing Exercise|Implied Volatility]]**: Forward-looking volatility derived from the market prices of options.

## 2. Empirical Volatility

### 2.1 Definition and Calculation

- Empirical volatility is the historical measure of how much a security's price or yield has fluctuated over a specific time period.
- It is calculated as the standard deviation of a time series of daily price or yield changes,  annualized to reflect yearly volatility.

#### 2.1.1 Absolute Volatility
- Absolute volatility is the annualized standard deviation of daily price or yield changes,  assuming a normal distribution.
- **Formula**:
 $\text{Absolute Volatility} = \sqrt{\frac{\sum_{i=1}^{n} (\Delta P_i - \bar{\Delta P})^2}{n-1}} \times \sqrt{252}$$
  - Where:
	- $$\Delta P_i$$: Daily price change.
	- $$\bar{\Delta P}$$: Average daily price change.
	- $$n$$: Number of observations.
	- $$252$$: Number of trading days in a year.

#### 2.1.2 Percentage Volatility
- Percentage volatility is the annualized standard deviation of the daily logarithmic changes in price or yield,  assuming a lognormal distribution.
- **Formula**:
 $\text{Percentage Volatility} = \sqrt{\frac{\sum_{i=1}^{n} (\ln(P_i / P_{i-1}) - \bar{\ln(P_i / P_{i-1})})^2}{n-1}} \times \sqrt{252}$$
  - Where:
	- $$P_i$$: Price on day $$i$$.
	- $$P_{i-1}$$: Price on the previous day.

### 2.2 Time Periods for Empirical Volatility

- Empirical volatility can be calculated over different time periods,  such as 10 days,  30 days,  or 360 days.
- **Shorter Time Periods**:
  - Reflect current market conditions more accurately.
  - Are more sensitive to recent deviations,  making them less stable.
- **Longer Time Periods**:
  - Provide a smoother measure of volatility.
  - Introduce a lag,  making them less responsive to recent market changes.

#### 2.2.1 Matching Volatility to Option Contracts
- The time period used to calculate empirical volatility should align with the length of the option contract.
- This ensures that the historical volatility reflects the time horizon relevant to the option's expiration.

### 2.3 Converting Between Price and Yield Volatility

- The [[A Guide to Duration DV01 and Yield Curve|modified duration]] of a security provides the link between price and yield volatilities.
- **Formula**:
 $\text{Price Volatility} = \text{Yield Volatility} \times \text{Modified Duration}$$
  - Where:
	- **[[Black Models for Bond Price Options Capsfloors|Price Volatility]]**: Percentage change in price.
	- **Yield Volatility**: Absolute change in yield.
	- **[[A Guide to Duration DV01 and Yield Curve|Modified Duration]]**: Sensitivity of price to yield changes.

#### 2.3.1 Example Conversion
- **Given**:
  - Yield Volatility: 0.50% (annualized).
  - [[A Guide to Duration DV01 and Yield Curve|Modified Duration]]: 5.
- **Calculation**:
 $\text{Price Volatility} = 0.50\% \times 5 = 2.5\%$$

## 3. Implied Volatility

### 3.1 Definition and Importance

- [[A Real-Life Option Pricing Exercise|Implied volatility]] represents the market's expectation of future volatility over the life of an option.
- It is derived from the observed market price of an option by solving the option [[Arbitrage Pricing of Derivatives|pricing]] model for the volatility input.

### 3.2 Calculation of Implied Volatility

- [[A Real-Life Option Pricing Exercise|Implied volatility]] is calculated using iterative numerical methods,  as there is no closed-form solution.
- The process involves:
  1. Inputting the observed market price of the option into an option [[Arbitrage Pricing of Derivatives|pricing]] model (e.g.,  [[Mathematical Modeling of Derivative Pricing|Black-Scholes]]).
  1. Adjusting the volatility input until the theoretical price matches the observed price.

#### 3.2.1 Example
- **Given**:
  - Observed Call Price: $2.50.
  - [[Call and Put Payoffs at Expiry|Strike Price]]: $100.
  - Underlying Price: $102.
  - [[Chapter 16 - Black–Scholes Model|Time to Expiration]]: 90 days.
  - [[Black Scholes Derivation|Risk-Free Rate]]: 2%.
- **Process**:
  - Use the [[Black Scholes Derivation|Black-Scholes model]] to iteratively solve for the [[A Real-Life Option Pricing Exercise|implied volatility]] that equates the theoretical price to $2.50.

### 3.3 Applications of Implied Volatility

- **Market Sentiment**:
  - [[A Real-Life Option Pricing Exercise|Implied volatility]] reflects the market's [[FORWARD RATES AND TERM STRUCTURE|expectations]] of future uncertainty.
  - High [[A Real-Life Option Pricing Exercise|implied volatility]] indicates greater expected price fluctuations.
- **Option [[Arbitrage Pricing of Derivatives|Pricing]]**:
  - [[A Real-Life Option Pricing Exercise|Implied volatility]] is a critical input for [[Arbitrage Pricing of Derivatives|pricing]] options and structuring option strategies.
- **Volatility [[Arbitrage Pricing of Derivatives|Arbitrage]]**:
  - Traders exploit discrepancies between implied and empirical volatility to generate profits.

## 4. Comparing Empirical and Implied Volatility

| **Aspect** | **Empirical Volatility** | **[[A Real-Life Option Pricing Exercise|Implied Volatility]]** |

| **Definition** | Historical measure of past price/yield changes. | Market's expectation of future volatility. |

| **Calculation** | Based on standard deviation of historical data. | Derived from observed option prices. |

| **Time Horizon** | Retrospective (past volatility). | Prospective (future volatility). |

| **Use Case** | Evaluating historical risk. | [[Arbitrage Pricing of Derivatives|Pricing]] options and assessing market sentiment. |

## 5. Practical Applications of Volatility in Fixed Income Markets

### 5.1 Option Pricing and Strategy Design

- Volatility is a key input in option [[Arbitrage Pricing of Derivatives|pricing]] models,  influencing the premium of calls and puts.
- Traders and [[An Asset Allocation Primer|portfolio]] managers use volatility to design strategies that align with their market outlook and risk tolerance.

### 5.2 Risk Management

- Understanding volatility helps investors assess the risk of their portfolios and implement appropriate [[Key Rates O1s Durations and Hedging|hedging]] strategies.
- For example,  high volatility may prompt the use of protective puts to limit downside risk.

### 5.3 Volatility Arbitrage

- Traders exploit differences between implied and empirical volatility to identify mispriced options.
- **Example**:
  - If [[A Real-Life Option Pricing Exercise|implied volatility]] is higher than empirical volatility,  traders may sell options to capture the premium.

## 6. Summary and Key Takeaways

- Volatility is a measure of uncertainty in the price or yield of a security and plays a central role in option [[Arbitrage Pricing of Derivatives|pricing]] and strategy design.
- Empirical volatility is based on historical data,  while [[A Real-Life Option Pricing Exercise|implied volatility]] reflects [[Forward Rate|market expectations]] of future uncertainty.
- The choice of volatility measure depends on the specific application,  such as [[Arbitrage Pricing of Derivatives|pricing]] options,  managing risk,  or designing [[Quantitative Trading Strategies Lecture Notes|trading strategies]].
- Converting between price and yield volatility requires an understanding of [[A Guide to Duration DV01 and Yield Curve|modified duration]],  which links the two measures.

By mastering the concepts of empirical and [[A Real-Life Option Pricing Exercise|implied volatility]],  investors can make informed decisions in the [[Lecture Notes Bonds,  Preferred Stock,  and Structured Products|fixed income]] and options markets,  optimizing their strategies to align with market conditions and their [[An Asset Allocation Primer|investment]] objectives.

# Lecture Notes: Interest-Rate Caps,  Floors,  and Participating Structures

## 1. Introduction to Interest-Rate Caps and Floors

- Interest-rate [[Interest Rate Derivatives-An Introduction to the  Pricing of Caps and Floors|caps and floors]] are derivative instruments that provide asymmetric interest-rate [[Financial Mathematics Course|risk management]] capabilities,  similar to options.
- **Caps**: Protect against rising [[Interest Rate Quotations|interest rates]] by capping the maximum rate on floating-rate liabilities.
- **[[Caps and Floors|Floors]]**: Protect against falling [[Interest Rate Quotations|interest rates]] by establishing a minimum rate of return on floating-rate assets.
- These instruments are highly customizable,  allowing users to tailor protection to specific needs by selecting parameters such as the underlying index,  strike rate,  term,  settlement frequency,  and notional amount.

## 2. Features of Interest-Rate Caps and Floors

### 2.1 Underlying Index
- The underlying index determines the reference rate for the cap or floor.
- Common indexes include:
  - [[A Guide to the Front End and [[Basis Swaps|Basis Swap]] Markets#[[Short-Term Rates and the Transition from LIBOR|London Interbank Offered Rate]] (LIBOR)|LIBOR]] (e.g.,  3-month LIBOR).
  - Treasury bills.
  - [[Class Note 12 - Commercial Paper#Class Note 12 – Commercial Paper|Commercial Paper]].
  - Certificates of deposit.
- The maturity of the index (e.g.,  1-month,  3-month,  or 6-month LIBOR) is an additional variable.

### 2.2 Strike Rate
- The strike rate is the threshold rate at which cash flows are exchanged between the purchaser and seller.
- **Caps**:
  - Higher strike rates result in lower premiums because the likelihood of the cap being "in the money" decreases.
- **[[Caps and Floors|Floors]]**:
  - Higher strike rates result in higher premiums because the likelihood of the floor being "in the money" increases.

### 2.3 Term of Protection
- The term of the cap or floor can range from several months to 30 years.
- [[Class Note 10 Liquidity and Class Note 10 Liquidity and Liquidity Managementliquidity management|Liquidity]] decreases for longer-dated [[Interest Rate Derivatives-An Introduction to the  Pricing of Caps and Floors|caps and floors]],  potentially increasing premiums.

### 2.4 Settlement Frequency
- Settlement frequency determines how often the strike rate is compared to the underlying index.
- Common frequencies include:
  - Monthly.
  - Quarterly.
  - Semiannually.
- Cash flows can be based on:
  - The average daily rate during the settlement period.
  - The [[The Foreign Exchange Market Annotations|spot rate]] on the settlement date.

### 2.5 Notional Amount
- The notional amount is the principal on which cash flows are calculated.
- [[Interest Rate Derivatives-An Introduction to the  Pricing of Caps and Floors|Caps and floors]] can include amortization features to align with the declining balance of an [[Risk Neutral Pricing of Options|underlying asset]] (e.g.,  [[Fremont Financial Corp. (b)|mortgage-backed securities]]).

## 3. Pricing of Caps and Floors

### 3.1 Upfront Premium
- The upfront premium is the fee paid by the purchaser to the seller at the inception of the contract.
- Factors influencing the premium:
  - Strike rate.
  - Current level of the reference rate.
  - Volatility of the underlying index.
  - Length of the agreement.
  - Notional amount.
  - Special features (e.g.,  amortization,  termination options).

### 3.2 Option Pricing Theory
- [[Interest Rate Derivatives-An Introduction to the  Pricing of Caps and Floors|Caps and floors]] are priced using option [[Arbitrage Pricing of Derivatives|pricing]] models,  as they share characteristics with options.
- **Volatility**:
  - Higher volatility increases the premium for both [[Interest Rate Derivatives-An Introduction to the  Pricing of Caps and Floors|caps and floors]].
- **Strike Rate**:
  - Caps: Higher strike rates reduce the premium.
  - [[Caps and Floors|Floors]]: Higher strike rates increase the premium.
- **Term**:
  - Longer terms result in higher premiums due to the increased probability of a positive payoff.
- **Settlement Frequency**:
  - Shorter settlement frequencies result in higher premiums because there are more opportunities for payoffs.

## 4. Example: Interest-Rate Cap

### 4.1 Cap Details
- **Notional Amount**: $10,  000,  000.
- **Underlying Index**: 3-month LIBOR.
- **Maturity**: 3 years.
- **Strike Rate**: 6%.
- **Premium**: 145 basis points (1.45% of $10,   000,   000 = $145,  000).
- **Settlement Frequency**: Quarterly.
- **Day Count**: Actual/360.

### 4.2 Annualized Premium
- The upfront premium can be converted to an annual basis-point equivalent.
- **Assumptions**:
  - Premium funded at 5%.
  - 12 reset periods (quarterly over 3 years).
- **Calculation**:
  - Treat $145,  000 as the present value of a stream of equal quarterly payments.
  - Annualized premium = 52 basis points.

### 4.3 Cap Payments
- Payments are made when the reference rate exceeds the strike rate.
- **Formula**:
 $\text{Payment} = (\text{Index Rate} - \text{Strike Rate}) \times \frac{\text{Days in Settlement Period}}{360} \times \text{Notional Amount}$$
- **Example**:
  - 3-month [[A Guide to the Front End and [[Basis Swaps|Basis Swap]] Markets#[[Short-Term Rates and the Transition from LIBOR|London Interbank Offered Rate]] (LIBOR)|LIBOR]] = 7%.
  - Strike Rate = 6%.
  - Days in Settlement Period = 90.
  - Payment:
	$$\text{Payment} = (7\% - 6\%) \times \frac{90}{360} \times 10,   000,   000 = 25,   000$$

### 4.4 Effective Interest Expense
- The effective interest expense includes the amortized premium.
- **Maximum Rate**:
  - Strike Rate + Annualized Premium = 6% + 0.52% = 6.52%.
- **Exhibit 67-1**: Illustrates the capped liability's effective interest expense under various [[A Guide to the Front End and [[Basis Swaps|Basis Swap]] Markets#[[Short-Term Rates and the Transition from LIBOR|London Interbank Offered Rate]] (LIBOR)|LIBOR]] scenarios.

## 5. Participating Caps

### 5.1 Definition
- A participating cap provides full protection against rising rates but requires the buyer to share a percentage of the benefit when rates fall below the strike rate.

### 5.2 Example: Participating Cap
- **Details**:
  - Strike Rate: 7%.
  - Participation Rate: 60%.
- **Scenario**:
  - [[A Guide to the Front End and [[Basis Swaps|Basis Swap]] Markets#[[Short-Term Rates and the Transition from LIBOR|London Interbank Offered Rate]] (LIBOR)|LIBOR]] = 5%.
  - Difference = 7% - 5% = 2%.
  - Participation = 60% × 2% = 1.2%.
  - Effective Interest Expense = [[A Guide to the Front End and [[Basis Swaps|Basis Swap]] Markets#[[Short-Term Rates and the Transition from LIBOR|London Interbank Offered Rate]] (LIBOR)|LIBOR]] + Participation = 5% + 1.2% = 6.2%.

### 5.3 Comparison with Non-Participating Cap
- **Bearish Scenarios**:
  - Non-participating caps have higher effective costs due to the amortized premium.
- **Bullish Scenarios**:
  - Participating caps have higher effective costs due to the participation feature.
- **Exhibit 67-3**: Compares effective interest expenses for participating and non-participating caps.

## 6. Participating Cap Structures

### 6.1 Definition
- Participating cap structures combine caps and swaps to hedge floating-rate liabilities.
- Caps are purchased without an upfront fee,  funded by executing an off-market swap at a higher fixed rate.

### 6.2 Example: Participating Cap Structure
- **Details**:
  - Floating Rate: [[A Guide to the Front End and [[Basis Swaps|Basis Swap]] Markets#[[Short-Term Rates and the Transition from LIBOR|London Interbank Offered Rate]] (LIBOR)|LIBOR]] + 10 bps.
  - Cap Strike Rate: 7%.
  - Swap Fixed Rate: 5% (off-market).
  - Cap Premium: 200 bps (2% of notional).
  - Present Value of Annuity: 2.76% (based on 0.6% spread over 5 years at 4.4% [[PSET 7- Kohler|discount rate]]).
- **Allocation**:
  - Caps: 58%.
  - Swaps: 42%.
- **Exhibit 67-4**: Illustrates effective interest expenses under various [[A Guide to the Front End and [[Basis Swaps|Basis Swap]] Markets#[[Short-Term Rates and the Transition from LIBOR|London Interbank Offered Rate]] (LIBOR)|LIBOR]] scenarios.

## 7. Interest-Rate Floors

### 7.1 Definition
- [[Caps and Floors|Floors]] protect the rate of return on floating-rate assets by establishing a minimum rate.
- **Example**:
  - Notional Amount: $10,  000,  000.
  - Underlying Index: 3-month Treasury bill.
  - Maturity: 3 years.
  - Strike Rate: 2%.
  - Premium: 85 basis points (0.85% of $10,   000,   000 = $85,  000).
  - Settlement Frequency: Quarterly.
  - Day Count: Actual/360.

### 7.2 Floor Payments
- Payments are made when the reference rate falls below the strike rate.
- **Formula**:
 $\text{Payment} = (\text{Strike Rate} - \text{Index Rate}) \times \frac{\text{Days in Settlement Period}}{360} \times \text{Notional Amount}$$

## 8. Summary and Key Takeaways

### 8.1 Caps
- Caps provide protection against rising rates while allowing the buyer to benefit from falling rates.
- The effective interest expense includes the amortized premium,  which increases the cost in low-rate scenarios.

### 8.2 Floors
- [[Caps and Floors|Floors]] protect the rate of return on floating-rate assets in falling-rate scenarios.
- The premium is influenced by the strike rate,  volatility,  and term.

### 8.3 Participating Structures
- Participating caps and swaps offer flexible [[Key Rates O1s Durations and Hedging|hedging]] solutions by combining caps and swaps.
- These structures allow buyers to tailor their liability costs to specific rate scenarios.

By understanding the mechanics and [[Arbitrage Pricing of Derivatives|pricing]] of caps,  [[Caps and Floors|floors]],  and participating structures,  financial professionals can effectively manage interest-rate risk and optimize funding strategies.

out the [[Quantitative Trading Strategies Lecture Notes|credit risk]] of a corporate bond while retaining exposure to [[Analysis of Fixed Income Securities|interest rate risk]] or other factors. This decomposition allows investors to isolate and manage specific risks more effectively.

## 7. Summary and Key Takeaways

### 7.1 Interest-Rate Floors and Caps
- **Interest-Rate [[Caps and Floors|Floors]]**: Provide protection against falling [[Interest Rate Quotations|interest rates]],  ensuring a minimum return on floating-rate assets. They are beneficial in bullish interest-rate scenarios where [[Some Stylized Empirical Facts About Asset Retur|asset returns]] are subject to erosion.
- **Interest-Rate Caps**: Protect against rising [[Interest Rate Quotations|interest rates]] by capping the maximum rate on floating-rate liabilities. They are analogous to buying a strip of put options on [[Interest Rate Quotations|interest rates]].
- **Cap/Floor Parity**: Similar to put/call parity in options,  cap/floor parity establishes the relationship between caps,  [[Caps and Floors|floors]],  and interest-rate swaps. The cost of a cap should equal the cost of a floor struck at the same rate on an identical index,  ensuring no [[Class Note 13 The LTCM Meltdown|arbitrage opportunities]].

### 7.2 Interest-Rate Collars and Corridors
- **Interest-Rate Collars**: Combine the purchase of a cap and the sale of a floor to hedge floating-rate liabilities. This strategy limits the liability rate between the floor and cap strike rates,  reducing the cost of protection but sacrificing benefits from market rallies below the floor strike rate.
- **Interest-Rate Corridors**: Involve buying a cap at a lower strike rate and selling a cap at a higher strike rate. This strategy reduces the cost of the lower strike cap while maintaining the benefit of falling [[Interest Rate Quotations|interest rates]]. However,  it introduces risk if rates exceed the higher strike cap.

### 7.3 Credit Derivatives
- **Credit Default Swaps (CDS)**: Allow the transfer of [[Quantitative Trading Strategies Lecture Notes|credit risk]] from one party to another,  providing a tool for [[Key Rates O1s Durations and Hedging|hedging]] or assuming credit exposure. They are widely used by banks,  insurance companies,  [[Basis Trade Explainer|hedge funds]],  and other market participants.
- **CDS Indices**: Offer a diversified exposure to a [[An Asset Allocation Primer|portfolio]] of credits,  simplifying the process of managing macro-level [[Quantitative Trading Strategies Lecture Notes|credit risk]].
- **Market Evolution**: The [[Credit Derivative Indexes|CDS market]] has evolved significantly since its inception,  with standardization efforts by ISDA and regulatory changes improving transparency and reducing systemic risk.

### 7.4 Applications of Credit Derivatives
- **[[Key Rates O1s Durations and Hedging|Hedging]] [[Quantitative Trading Strategies Lecture Notes|Credit Risk]]**: CDS provide an efficient way to hedge [[Quantitative Trading Strategies Lecture Notes|credit risk]],  replacing the need to short [[Class Notes 2 – Corporate Bond Contracts|Corporate Bonds]].
- **Customization**: The bilateral OTC nature of CDS allows for tailored contracts to meet specific needs.
- **[[Lecture 6-Leverage, Tail Risk, Volatility Products|Leverage]] and Yield Enhancement**: CDS require minimal upfront payments,  enabling leveraged exposure to [[Quantitative Trading Strategies Lecture Notes|credit risk]].
- **Risk Decomposition**: CDS can isolate [[Quantitative Trading Strategies Lecture Notes|credit risk]] from other risks,  such as [[Analysis of Fixed Income Securities|interest rate risk]],  allowing for more precise [[Financial Mathematics Course|risk management]].

## 8. Practical Considerations

### 8.1 Risk Management
- Interest-rate [[Chapter 9 Arbitrage and Hedging With Options|derivatives]] and [[RISK NEUTRAL VALUATION FRAMEWORK FOR CREDIT DEFAULT SWAPS|credit derivatives]] are powerful tools for managing risk but require careful consideration of market conditions,  counterparty risk,  and [[Class Note 10 Liquidity and Class Note 10 Liquidity and Liquidity Managementliquidity management|liquidity]].
- Strategies such as collars and corridors can reduce costs but may introduce additional risks,  particularly in extreme market scenarios.

### 8.2 Regulatory and Market Changes
- The [[Squam Lake Group Introduction|introduction]] of centralized clearing and standardized contracts has improved the transparency and efficiency of the [[Chapter 9 Arbitrage and Hedging With Options|derivatives]] market.
- Market participants must stay informed about regulatory developments to ensure compliance and optimize their use of [[Chapter 9 Arbitrage and Hedging With Options|derivatives]].

### 8.3 Strategic Use of Derivatives
- Combining interest-rate and [[RISK NEUTRAL VALUATION FRAMEWORK FOR CREDIT DEFAULT SWAPS|credit derivatives]] can create sophisticated [[Key Rates O1s Durations and Hedging|hedging]] strategies that address multiple risks simultaneously.
- Understanding the interplay between different instruments,  such as caps,  [[Caps and Floors|floors]],  swaps,  and CDS,  is essential for effective [[The Impact of Option Strategies in Financial  Portfolios Performance|portfolio management]].

By mastering the mechanics,  [[Arbitrage Pricing of Derivatives|pricing]],  and applications of interest-rate and [[RISK NEUTRAL VALUATION FRAMEWORK FOR CREDIT DEFAULT SWAPS|credit derivatives]],  financial professionals can enhance their ability to manage risk,  optimize [[Assets|returns]],  and navigate complex market environments.

# Lecture Notes: Credit Default Swaps (CDS) – Mechanics,  Pricing,  and Settlement

## 1. Introduction to Credit Default Swaps (CDS)

- A **[[Credit Market Session 2|Credit Default Swap]] (CDS)** is a financial derivative that allows the transfer of [[Quantitative Trading Strategies Lecture Notes|credit risk]] from one party to another. It functions similarly to an insurance contract but is traded in [[Financial Markets and Institutions Lecture Notes|financial markets]] and can be valued at any time.
- **Key Participants**:
  - **[[Credit Default Swaps|Protection Buyer]]**: Pays a premium to transfer the [[Quantitative Trading Strategies Lecture Notes|credit risk]] of a [[Lecture Notes 9A- Credit Default Swaps|reference entity]] to the [[Credit Default Swaps|protection seller]].
  - **[[Credit Default Swaps|Protection Seller]]**: Receives the premium and assumes the [[Quantitative Trading Strategies Lecture Notes|credit risk]] of the [[Lecture Notes 9A- Credit Default Swaps|reference entity]].
- **Purpose**:
  - [[Key Rates O1s Durations and Hedging|Hedging]] [[Quantitative Trading Strategies Lecture Notes|credit risk]].
  - Speculating on creditworthiness.
  - Structuring tailored credit investments.
  - Managing regulatory capital.

## 2. Mechanics of a CDS Contract

### 2.1 Structure of a CDS

- A CDS is a bilateral contract between a [[Credit Default Swaps|protection buyer]] and a [[Credit Default Swaps|protection seller]].
- **Key Components**:
  - **[[Lecture Notes 9A- Credit Default Swaps|Reference Entity]]**: The corporate or sovereign issuer whose [[Quantitative Trading Strategies Lecture Notes|credit risk]] is being transferred.
  - **Deliverable Obligations**: Bonds or loans of the [[Lecture Notes 9A- Credit Default Swaps|reference entity]] that are covered by the CDS.
  - **Credit Events**: Specific events (e.g.,  bankruptcy,  failure to pay) that trigger the CDS.
  - **Notional Amount**: The face value of the debt being protected.
  - **Premium Leg**: Regular payments made by the [[Credit Default Swaps|protection buyer]] to the [[Credit Default Swaps|protection seller]].
  - **Protection Leg**: Contingent payment made by the [[Credit Default Swaps|protection seller]] if a [[Valuation of Credit Default Swaps|credit event]] occurs.

### 2.2 Premium Leg

- The **premium leg** consists of periodic fixed payments made by the [[Credit Default Swaps|protection buyer]] to the [[Credit Default Swaps|protection seller]].
- **Calculation**:
 $\text{Premium Payment} = \text{Fixed Coupon} \times \text{Notional Amount} \times \text{Year Fraction (Actual/360)}$$
- **Key Features**:
  - Payments terminate after a [[Valuation of Credit Default Swaps|credit event]].
  - Fixed coupons are standardized (e.g.,  100 bps or 500 bps) and do not reflect the [[Quantitative Trading Strategies Lecture Notes|credit risk]] of the [[Lecture Notes 9A- Credit Default Swaps|reference entity]]. Instead,  the upfront payment adjusts for [[Quantitative Trading Strategies Lecture Notes|credit risk]].

### 2.3 Protection Leg

- The **protection leg** is a contingent payment made by the [[Credit Default Swaps|protection seller]] to the [[Credit Default Swaps|protection buyer]] if a [[Valuation of Credit Default Swaps|credit event]] occurs.
- **Payment Amount**:
 $\text{Protection Payment} = \text{Notional Amount} \times (1 - \text{Recovery Rate})$$
  - **[[Credit Markets Session 3|Recovery Rate]]**: The market-determined value of the deliverable obligations after a [[Valuation of Credit Default Swaps|credit event]].
- **Settlement Methods**:
  - **[[Swaptions|Cash Settlement]]**: [[Credit Default Swaps|Protection seller]] pays the difference between par and the recovery price.
  - **[[Fundamentals of Futures and Forwards|Physical Settlement]]**: [[Credit Default Swaps|Protection buyer]] delivers the impaired obligations to the [[Credit Default Swaps|protection seller]] in exchange for the notional amount.

### 2.4 Upfront Payment

- The **upfront payment** adjusts for the difference between the fixed coupon and the market-implied [[Cds-Equivalent Bond Spread|credit spread]] of the [[Lecture Notes 9A- Credit Default Swaps|reference entity]].
- **Key Factors**:
  - If the fixed coupon is lower than the market-implied spread,  the [[Credit Default Swaps|protection buyer]] makes an upfront payment to the [[Credit Default Swaps|protection seller]].
  - If the fixed coupon is higher than the market-implied spread,  the [[Credit Default Swaps|protection seller]] makes an upfront payment to the [[Credit Default Swaps|protection buyer]].

## 3. Credit Events in CDS Contracts

### 3.1 Definition of Credit Events

- A **[[Valuation of Credit Default Swaps|credit event]]** is a predefined event that triggers the protection leg of a CDS contract.
- **Types of Credit Events**:
  - **Hard Credit Events**: Cause all pari passu debt obligations to trade at the same price.
	- Bankruptcy.
	- Failure to pay.
	- Obligation acceleration.
	- Obligation default.
	- Repudiation/moratorium.
  - **Soft Credit Events**: Do not cause all pari passu debt obligations to trade at the same price.
	- Restructuring.

### 3.2 Restructuring Credit Event

- **Restructuring** refers to a consensual agreement between a [[Lecture Notes 9A- Credit Default Swaps|reference entity]] and its creditors to modify debt terms in a way that negatively impacts creditors.
- **Challenges**:
  - Restructuring creates a "delivery option" for the [[Credit Default Swaps|protection buyer]],  who can choose the [[Tba and Specified Pools Markets|cheapest-to-deliver]] obligation.
  - This can lead to windfall gains for the [[Credit Default Swaps|protection buyer]] and larger losses for the [[Credit Default Swaps|protection seller]].
- **Mitigation**:
  - [[Squam Lake Group Introduction|Introduction]] of restructuring clauses:
	- **Old-Restructuring (Old-Re)**: 30-year maturity limit on deliverables.
	- **Modified-Restructuring (Mod-Re)**: Limits deliverables to those maturing within the greater of the CDS termination date or 30 months after the restructuring date.
	- **Modified-Modified Restructuring (Mod-Mod Re)**: Similar to Mod-Re but with a 60-month limit for restructured obligations and a 30-month limit for non-restructured obligations.
	- **No-Restructuring (No-Re)**: Excludes restructuring as a [[Valuation of Credit Default Swaps|credit event]].

## 4. Settlement of CDS Contracts

### 4.1 Auction Process

- The settlement of a CDS contract after a [[Valuation of Credit Default Swaps|credit event]] involves determining the recovery price of the deliverable obligations through a market-wide auction.
- **Objectives**:
  1. Prevent short squeezes by ensuring sufficient deliverable obligations.
  1. Establish a common recovery price across the [[Credit Derivative Indexes|CDS market]].
  1. Handle soft restructuring credit events.
- **Mechanics**:
  - Dealers submit bids and offers for the deliverable obligations.
  - The final recovery price is determined based on the auction results.

### 4.2 Settlement Timeline

- **[[Valuation of Credit Default Swaps|Credit Event]] Determination**:
  - Before 2009: Bilateral decision based on publicly available information.
  - After 2009: Determined by a centralized determinations committee.
- **Key Dates**:
  - **Effective Date**: Protection begins 60 days before the [[Valuation of Credit Default Swaps|credit event]] determination request.
  - **Scheduled Termination Date**: Standardized to March 20,  June 20,  September 20,  or December 20 of the specified year.

## 5. Pricing and Valuation of CDS Contracts

### 5.1 Quoted Spread and Fixed Coupon

- The **quoted spread** reflects the market-implied [[Quantitative Trading Strategies Lecture Notes|credit risk]] of the [[Lecture Notes 9A- Credit Default Swaps|reference entity]].
- The **fixed coupon** is standardized (e.g.,  100 bps or 500 bps) and does not vary with [[Quantitative Trading Strategies Lecture Notes|credit risk]].
- **Upfront Payment**:
  - Adjusts for the difference between the fixed coupon and the quoted spread.
  - **Example**:
	- Fixed Coupon: 100 bps.
	- Quoted Spread: 160 bps.
	- Upfront Payment: [[Credit Default Swaps|Protection buyer]] pays the [[Credit Default Swaps|protection seller]] to compensate for the lower fixed coupon.

### 5.2 Mark-to-Market Valuation

- The value of a CDS contract changes over time due to:
  - Changes in the quoted spread.
  - Changes in [[Interest Rate Quotations|interest rates]].
- **Key Insight**:
  - A long protection position (buying CDS protection) gains value when the quoted spread widens,  as the cost of protection increases.
  - A short protection position (selling CDS protection) gains value when the quoted spread tightens,  as the cost of protection decreases.

## 6. Applications of CDS

### 6.1 Hedging Credit Risk

- CDS provide an efficient way to hedge [[Quantitative Trading Strategies Lecture Notes|credit risk]] without selling the underlying bonds or loans.
- **Example**:
  - A bank holding [[Class Notes 2 – Corporate Bond Contracts|Corporate Bonds]] can buy CDS protection to hedge against [[Default Risk and Credit Derivatives 183|default risk]].

### 6.2 Speculation

- CDS enable market participants to express views on the creditworthiness of a [[Lecture Notes 9A- Credit Default Swaps|reference entity]].
- **Example**:
  - Buying CDS protection is equivalent to [[Short Selling|shorting]] the [[Quantitative Trading Strategies Lecture Notes|credit risk]] of the [[Lecture Notes 9A- Credit Default Swaps|reference entity]].
  - Selling CDS protection is equivalent to going long on the [[Quantitative Trading Strategies Lecture Notes|credit risk]] of the [[Lecture Notes 9A- Credit Default Swaps|reference entity]].

### 6.3 Structured Credit Investments

- CDS can be used as building blocks for [[A Survey of the Micro structure of Fixed-Income Markets|structured credit products]],  such as [[Credit Markets Session 5|collateralized debt obligations]] (CDOs).
- These products provide tailored risk-return profiles for specific investor needs.

### 6.4 Regulatory Capital Management

- Banks can use CDS to hedge credits with high regulatory capital charges,  provided the hedge is recognized as economically effective by regulators.

## 7. Summary and Key Takeaways

### 7.1 Mechanics of CDS

- A CDS is a bilateral contract that transfers [[Quantitative Trading Strategies Lecture Notes|credit risk]] from the [[Credit Default Swaps|protection buyer]] to the [[Credit Default Swaps|protection seller]].
- The premium leg consists of fixed periodic payments,  while the protection leg is contingent on a [[Valuation of Credit Default Swaps|credit event]].

### 7.2 Credit Events and Settlement

- Credit events trigger the protection leg of a CDS and include bankruptcy,  failure to pay,  and restructuring.
- Settlement involves determining the recovery price through an [[Chapter 2 Securities Markets|auction process]].

### 7.3 Pricing and Applications

- The upfront payment adjusts for the difference between the fixed coupon and the quoted spread.
- CDS are versatile tools for [[Key Rates O1s Durations and Hedging|hedging]],  speculation,  structured credit investments,  and regulatory capital management.

By understanding the mechanics,  [[Arbitrage Pricing of Derivatives|pricing]],  and applications of CDS,  financial professionals can effectively manage [[Quantitative Trading Strategies Lecture Notes|credit risk]] and optimize their [[An Asset Allocation Primer|investment]] strategies.

of a [[An Asset Allocation Primer|portfolio]] of CDS contracts,  where the premium payments are adjusted for the surviving notional of the reference [[An Asset Allocation Primer|portfolio]].

## 1. Introduction to Credit Default Swaps (CDS) and Indices

- Credit Default Swaps (CDS) and CDS indices are essential tools in the [[RISK NEUTRAL VALUATION FRAMEWORK FOR CREDIT DEFAULT SWAPS|credit derivatives]] market,  providing investors with mechanisms to hedge [[Quantitative Trading Strategies Lecture Notes|credit risk]],  speculate on creditworthiness,  and gain diversified exposure to [[Credit Markets Session 1|credit markets]].
- This lecture focuses on:
  - The mechanics of CDS contracts and indices.
  - The innovations introduced by the 2009 Big Bang Protocol,  including the Determinations Committee (DC) and auction-based settlement.
  - The compression cycle and its role in reducing systemic risk.
  - The structure,  [[Arbitrage Pricing of Derivatives|pricing]],  and applications of CDS indices.

## 2. The 2009 Big Bang Protocol and Determinations Committee

### 2.1 Introduction of the Determinations Committee (DC)

- The **2009 Big Bang Protocol** introduced a centralized mechanism for determining credit events,  replacing the bilateral process that existed previously.
- **Key Features**:
  - Five regional DCs: Americas,  Asia (excluding Japan),  Japan,  Australia-New Zealand,  and EMEA (Europe,  Middle East,  and Africa).
  - Membership includes both buy-side and sell-side representatives to ensure impartiality.
  - Decisions require an **80% supermajority** for approval.

### 2.2 Credit Event Determination Process

- **Process**:
  1. A market participant submits a request to the DC secretary to investigate a potential [[Valuation of Credit Default Swaps|credit event]].
  1. The request must include publicly available information supporting the claim.
  1. The DC has **two business days** to meet,  investigate,  and vote on whether a [[Valuation of Credit Default Swaps|credit event]] has occurred.
  1. If more time is needed,  the DC can vote to extend the investigation period.

- **Outcomes**:
  - For **hard credit events** (e.g.,  bankruptcy,  failure to pay),  CDS contracts are automatically triggered.
  - For **restructuring credit events**,  the [[Credit Default Swaps|protection buyer]] or seller must choose to trigger the contract.

### 2.3 Restructuring Credit Events

- Restructuring is not an automatic trigger because it is not a [[Course Notes/HBR Notes/A Strategic Perspective on Bankruptcy|bankruptcy]] event and may be a precursor to one.
- **Triggering Rules**:
  - If the [[Credit Default Swaps|protection buyer]] triggers,  the basket of deliverable obligations corresponds to the CDS contract's scheduled termination date.
  - If the [[Credit Default Swaps|protection seller]] triggers,  the basket corresponds to the longest maturity (30-year) bucket.
- **Implications**:
  - Both parties prefer the other to trigger due to the differing value of deliverable obligations.
  - The "use it or lose it" rule requires careful timing to avoid missing the triggering deadline.

## 3. The Compression Cycle

### 3.1 Purpose and Mechanics

- The **compression cycle** is a process designed to cancel out mutually offsetting CDS positions,  reducing the number of outstanding contracts and systemic risk.
- **Key Features**:
  - Conducted quarterly across the [[RISK NEUTRAL VALUATION FRAMEWORK FOR CREDIT DEFAULT SWAPS|credit derivatives]] market.
  - Focuses on contracts held by dealers who choose to participate.
  - Reduces the number of contracts participating in subsequent auctions,  minimizing the need for physical assets.

### 3.2 Role of TriOptima

- TriOptima is the primary provider of compression services.
- **Process**:
  - Dealers submit their positions to TriOptima,  which uses an algorithm to identify offsetting transactions.
  - The algorithm calculates the optimal set of transactions to minimize outstanding contracts.
  - Dealers can choose whether to execute the proposed transactions.
- **Impact**:
  - Between 2008 and 2010,  the compression process eliminated approximately **$14.5 trillion** of credit derivative contracts.

## 4. Settlement of CDS Contracts

### 4.1 Auction Process

- The [[Chapter 2 Securities Markets|auction process]] determines the recovery price of deliverable obligations after a [[Valuation of Credit Default Swaps|credit event]].
- **Stages**:
  - **Stage One**: Determines the indicative recovery price (Internal Market Midpoint Price,  IMMP) and net open interest.
  - **Stage Two**: Matches net open interest with market participants to establish the final auction price.

### 4.2 Stage One: Indicative Recovery Price

- **Process**:
  - Dealers submit bid/offer prices and [[CDS Settlement Auctions|physical settlement requests]].
  - An algorithm calculates the IMMP by rejecting outliers and averaging the remaining bid/offer spreads.
  - The IMMP is rounded to the nearest 1/8th of a point.
- **Net Open Interest**:
  - Represents the [[Macroeconomic Models of Business Cycles|aggregate demand]] for [[Fundamentals of Futures and Forwards|physical settlement]].
  - Determines the size and direction of the demand for deliverable obligations.

### 4.3 Stage Two: Final Auction Price

- **Process**:
  - Participants submit limit orders to buy or sell deliverable obligations.
  - An order-matching algorithm fills the net open interest,  starting with the most competitive prices.
  - The final auction price is constrained to be within a specified range (cap amount) of the IMMP.
- **Settlement**:
  - The final auction price is used to settle all CDS contracts,  including both cash and physical settlements.

## 5. CDS Indices

### 5.1 Overview

- CDS indices provide diversified exposure to [[Credit Markets Session 1|credit markets]] and are widely used for [[Key Rates O1s Durations and Hedging|hedging]] and speculative purposes.
- **Key Features**:
  - Equally weighted at issuance for simplicity and diversification.
  - Issued semiannually with multiple maturities (e.g.,  1,  3,  5,  7,  and 10 years).
  - Most liquid series is the "on-the-run" index.

### 5.2 Standard CDS Indices

| **Name** | **Domicile and Type of Credits** | **Number of Credits** |

| **[[Credit Default Swaps|CDX.NA.IG]]** | North American [[An Asset Allocation Primer|investment]]-grade | 125 |

| **CDX.NA.HY** | North American high-yield | 100 |

| **CDX.NA.XO** | North American crossover | 35 |

| **CDX.EM** | Emerging market sovereign | 15 |

| **CDX.EM.Diversified** | Emerging market sovereign/corporate | 40 |

| **[[Credit Derivative Indexes|iTraxx]] Europe** | European [[An Asset Allocation Primer|investment]]-grade | 125 |

| **[[Credit Derivative Indexes|iTraxx]] Europe XO** | European crossover | 40 |

| **[[Credit Derivative Indexes|iTraxx]] Japan** | Japanese [[An Asset Allocation Primer|investment]]-grade | 50 |

| **[[Credit Derivative Indexes|iTraxx]] Asia ex-Japan**| Asian non-Japanese [[An Asset Allocation Primer|investment]]-grade | 50 |

| **[[Credit Derivative Indexes|iTraxx]] Australia** | Australian [[An Asset Allocation Primer|investment]]-grade | 25 |

### 5.3 Mechanics of CDS Indices

- **Premium Leg**:
  - The buyer pays a fixed coupon based on the surviving notional of the reference [[An Asset Allocation Primer|portfolio]].
  - The surviving notional decreases as credits in the [[An Asset Allocation Primer|portfolio]] experience credit events.
- **Protection Leg**:
  - The seller compensates the buyer for losses due to credit events,  based on the [[Credit Markets Session 3|recovery rate]] of defaulted credits.

## 6. Applications of CDS and CDS Indices

### 6.1 Hedging Credit Risk

- CDS and CDS indices provide efficient tools for [[Key Rates O1s Durations and Hedging|hedging]] [[Quantitative Trading Strategies Lecture Notes|credit risk]] in individual credits or broad portfolios.
- **Example**:
  - A bank can hedge its exposure to a [[An Asset Allocation Primer|portfolio]] of [[Class Notes 2 – Corporate Bond Contracts|Corporate Bonds]] by buying protection on a CDS index.

### 6.2 Speculation and Arbitrage

- CDS indices allow investors to express views on [[Credit Markets Session 1|credit markets]] or exploit mispricings.
- **Example**:
  - Selling protection on a CDS index is equivalent to taking a [[Chapter 4 - Futures: Hedging and Speculation|long position]] on the creditworthiness of the reference [[An Asset Allocation Primer|portfolio]].

### 6.3 Regulatory Capital Management

- Banks use CDS to reduce [[Case Study of Northern Rock|regulatory capital requirements]] by transferring [[Quantitative Trading Strategies Lecture Notes|credit risk]] to third parties.

## 7. Summary and Key Takeaways

### 7.1 Innovations in the CDS Market

- The 2009 Big Bang Protocol introduced centralized [[Valuation of Credit Default Swaps|credit event]] determination and auction-based settlement,  improving transparency and efficiency.
- The compression cycle has significantly reduced systemic risk by eliminating redundant contracts.

### 7.2 CDS Indices

- CDS indices provide diversified credit exposure and are widely used for [[Key Rates O1s Durations and Hedging|hedging]] and speculative purposes.
- The mechanics of CDS indices mirror those of individual CDS contracts,  with adjustments for the surviving notional of the reference [[An Asset Allocation Primer|portfolio]].

By understanding the mechanics,  [[Arbitrage Pricing of Derivatives|pricing]],  and applications of CDS and CDS indices,  financial professionals can effectively manage [[Quantitative Trading Strategies Lecture Notes|credit risk]] and optimize their [[An Asset Allocation Primer|investment]] strategies.

# Lecture Notes: Credit Default Swaps (CDS) and CDS Indices – Mechanics,  Valuation,  and Risk Management

## 1. Introduction to Credit Default Swaps (CDS) and CDS Indices

- Credit Default Swaps (CDS) are [[Financial Instruments PSET Solutions|financial derivatives]] that allow the transfer of [[Quantitative Trading Strategies Lecture Notes|credit risk]] from one party to another. They are widely used for [[Key Rates O1s Durations and Hedging|hedging]],  speculation,  and structured credit investments.
- CDS indices are portfolios of CDS contracts that provide diversified exposure to [[Credit Markets Session 1|credit markets]],  enabling investors to hedge or speculate on macro-level [[Quantitative Trading Strategies Lecture Notes|credit risk]] efficiently.
- This lecture focuses on:
  - The mechanics of CDS and CDS indices.
  - Valuation methodologies for CDS contracts.
  - The relationship between CDS and bond markets.
  - [[Financial Mathematics Course|Risk management]] and [[Quantitative Trading Strategies Lecture Notes|trading strategies]] involving CDS and CDS indices.

## 2. Mechanics of CDS Contracts

### 2.1 Key Features of CDS Contracts

- **[[Credit Default Swaps|Protection Buyer]]**: Pays a regular premium (fixed coupon) to the [[Credit Default Swaps|protection seller]] in exchange for protection against credit events.
- **[[Credit Default Swaps|Protection Seller]]**: Receives the premium and compensates the buyer if a [[Valuation of Credit Default Swaps|credit event]] occurs.
- **[[Lecture Notes 9A- Credit Default Swaps|Reference Entity]]**: The corporate or sovereign issuer whose [[Quantitative Trading Strategies Lecture Notes|credit risk]] is being transferred.
- **Credit Events**: Events that trigger the protection leg,  such as bankruptcy,  failure to pay,  obligation acceleration,  repudiation/moratorium,  and restructuring.
- **Notional Amount**: The face value of the debt being protected.

### 2.2 Premium Leg

- The premium leg consists of regular fixed payments made by the [[Credit Default Swaps|protection buyer]] to the [[Credit Default Swaps|protection seller]].
- **Formula**:
 $\text{Premium Payment} = \text{Fixed Coupon} \times \text{Notional Amount} \times \text{Year Fraction (Actual/360)}$$
- Payments continue until the contract matures or a [[Valuation of Credit Default Swaps|credit event]] occurs.
- If a [[Valuation of Credit Default Swaps|credit event]] occurs between two payment dates,  the accrued portion of the premium is paid by the [[Credit Default Swaps|protection buyer]].

### 2.3 Protection Leg

- The protection leg is a contingent payment made by the [[Credit Default Swaps|protection seller]] to the [[Credit Default Swaps|protection buyer]] if a [[Valuation of Credit Default Swaps|credit event]] occurs.
- **Formula**:
 $\text{Protection Payment} = \text{Notional Amount} \times (1 - \text{Recovery Rate})$$
  - **[[Credit Markets Session 3|Recovery Rate]]**: The market-determined value of the deliverable obligations after a [[Valuation of Credit Default Swaps|credit event]].
- Settlement can be:
  - **[[Swaptions|Cash Settlement]]**: The seller pays the difference between par and the recovery price.
  - **[[Fundamentals of Futures and Forwards|Physical Settlement]]**: The buyer delivers the impaired obligations to the seller in exchange for the notional amount.

### 2.4 Upfront Payment

- The upfront payment adjusts for the difference between the fixed coupon and the market-implied [[Cds-Equivalent Bond Spread|credit spread]] of the [[Lecture Notes 9A- Credit Default Swaps|reference entity]].
- **Key Insights**:
  - If the fixed coupon is lower than the market-implied spread,  the [[Credit Default Swaps|protection buyer]] makes an upfront payment to the seller.
  - If the fixed coupon is higher than the market-implied spread,  the seller makes an upfront payment to the buyer.

## 3. Mechanics of CDS Indices

### 3.1 Premium Leg of CDS Indices

- The premium leg of a CDS index is equivalent to a [[An Asset Allocation Primer|portfolio]] of CDS premium legs linked to each reference credit in the index.
- All reference credits pay a fixed coupon equal to the index coupon.
- Payments continue until the contract matures or all credits in the index experience credit events (an unlikely scenario).

### 3.2 Protection Leg of CDS Indices

- The protection leg of a CDS index mirrors that of an equally weighted [[An Asset Allocation Primer|portfolio]] of CDS protection legs on the reference credits.
- **Process for Credit Events**:
  1. The affected credit is removed from the index across all maturities.
  1. The index is assigned a new version number to distinguish it from earlier versions.
  1. The removed credit becomes a standalone CDS position with a notional corresponding to its size in the index.
	 - Example: If the index notional is $10 million and there are 125 credits,    the standalone CDS notional is $80,  000.
  1. The standalone CDS participates in the standard [[Chapter 2 Securities Markets|auction process]] to determine the [[Credit Markets Session 3|recovery rate]].

### 3.3 Restructuring Credit Events in CDS Indices

- If the [[Valuation of Credit Default Swaps|credit event]] is a restructuring:
  - The index buyer and seller can choose to trigger the standalone CDS contract.
  - If neither party triggers,  the standalone CDS remains on their books until maturity or a subsequent [[Valuation of Credit Default Swaps|credit event]].
  - Restructuring is excluded as a [[Valuation of Credit Default Swaps|credit event]] in North American indices but included in European and Asian indices.

## 4. Valuation of CDS Contracts

### 4.1 Expected Present Value of Cash Flows

- The value of a CDS contract is the expected present value of [[Advanced Derivatives Pricing Methodology|future cash flows]],  calculated under the [[Verifying Martingale Property with Q|risk-neutral measure]].
- **Premium Leg Value**:
  - The expected present value of fixed [[Realized Returns|coupon payments]] until maturity or a [[Valuation of Credit Default Swaps|credit event]].
  - Falls if the [[Wellman Inc the Importance of Loan Covenants|credit quality]] deteriorates,  as fewer coupons are expected to be received.
- **Protection Leg Value**:
  - The expected present value of the contingent payment (par minus [[Credit Markets Session 3|recovery rate]]) in the event of default.
  - Increases if the [[Wellman Inc the Importance of Loan Covenants|credit quality]] deteriorates,  as the likelihood of default rises.

### 4.2 No-Arbitrage Relationship Between CDS and Bonds

- There is a fundamental no-[[Arbitrage Pricing of Derivatives|arbitrage]] relationship between the upfront cost of a CDS and the price of a floating-rate bond issued by the same [[Lecture Notes 9A- Credit Default Swaps|reference entity]].
- **Key Insight**:
  - The upfront cost of a CDS equals the difference between par and the bond price,  adjusted for [[Intra-Year Compounding and Day-Count|accrued interest]] and recovery assumptions.
- **Simplifying Assumptions**:
  1. The bond is funded at [[A Guide to the Front End and [[Basis Swaps|Basis Swap]] Markets#[[Short-Term Rates and the Transition from LIBOR|London Interbank Offered Rate]] (LIBOR)|LIBOR]] flat.
  1. The bond pays a floating rate coupon equal to [[A Guide to the Front End and [[Basis Swaps|Basis Swap]] Markets#[[Short-Term Rates and the Transition from LIBOR|London Interbank Offered Rate]] (LIBOR)|LIBOR]] plus the CDS fixed spread.
  1. The [[Valuation of Credit Default Swaps|credit event]] occurs on a coupon payment date.

### 4.3 The CDS Basis

- The CDS basis is the difference between the CDS par spread and the bond [[A Guide to the Front End and [[Basis Swaps|Basis Swap]] Markets#[[Short-Term Rates and the Transition from LIBOR|London Interbank Offered Rate]] (LIBOR)|LIBOR]] spread.
- **Formula**:
 $\text{CDS Basis} = \text{CDS Par Spread} - \text{Bond [[A Guide to the Front End and Basis Swap Markets#London Interbank Offered Rate (LIBOR)|LIBOR]] Spread}$$
- **Applications**:
  - Basis trading involves exploiting discrepancies between CDS spreads and bond spreads.
  - A "[[Cds-Bond Basis|negative basis trade]]" involves buying the bond and buying CDS protection,  earning the bond spread while paying the [[Cds-Equivalent Bond Spread|CDS spread]].

## 5. Risk Management and Trading Strategies

### 5.1 Hedging Credit Risk

- CDS contracts provide an efficient way to hedge [[Quantitative Trading Strategies Lecture Notes|credit risk]] without selling the underlying bonds or loans.
- **Example**:
  - A bank holding [[Class Notes 2 – Corporate Bond Contracts|Corporate Bonds]] can buy CDS protection to hedge against [[Default Risk and Credit Derivatives 183|default risk]].

### 5.2 Speculation and Arbitrage

- CDS contracts enable investors to express views on the creditworthiness of a [[Lecture Notes 9A- Credit Default Swaps|reference entity]].
- **Example**:
  - Buying CDS protection is equivalent to [[Short Selling|shorting]] the [[Quantitative Trading Strategies Lecture Notes|credit risk]] of the [[Lecture Notes 9A- Credit Default Swaps|reference entity]].
  - Selling CDS protection is equivalent to going long on the [[Quantitative Trading Strategies Lecture Notes|credit risk]] of the [[Lecture Notes 9A- Credit Default Swaps|reference entity]].

### 5.3 Valuation of Existing CDS Contracts

- The mark-to-market value of a CDS contract is the difference between the expected present value of the premium leg and the protection leg.
- **Formula**:
 $U(t) = V_{\text{Premium}}(t,  T) - V_{\text{Protection}}(t,  T)$$
  - Where:
	- $$U(t)$$: Mark-to-market value at time $$t$$.
	- $$V_{\text{Premium}}(t,    T)$$: Value of the premium leg.
	- $$V_{\text{Protection}}(t,    T)$$: Value of the protection leg.

## 6. Importance of the CDS Market

### 6.1 Post-2008 Reforms

- The [[Credit Derivative Indexes|CDS market]] underwent significant reforms after the 2008 [[Squam Lake Group Letter|financial crisis]] to improve transparency,  reduce systemic risk,  and ensure market-wide settlement mechanisms.
- **Key Changes**:
  - [[Squam Lake Group Introduction|Introduction]] of centralized counterparties (CCPs) to reduce counterparty risk.
  - Standardized auction processes for [[Valuation of Credit Default Swaps|credit event]] settlement.
  - Increased transparency through data publication by the DTCC.

### 6.2 Applications of CDS and CDS Indices

- **[[Key Rates O1s Durations and Hedging|Hedging]]**: Protect against credit losses on individual credits or portfolios.
- **Speculation**: Express views on creditworthiness or market-wide [[Quantitative Trading Strategies Lecture Notes|credit risk]].
- **Yield Enhancement**: Earn premiums by selling protection.
- **Regulatory Capital Management**: Reduce capital requirements by transferring [[Quantitative Trading Strategies Lecture Notes|credit risk]].

## 7. Summary and Key Takeaways

### 7.1 CDS Contracts

- CDS contracts [[Credit Default Swaps|transfer credit risk]] from the [[Credit Default Swaps|protection buyer]] to the [[Credit Default Swaps|protection seller]].
- The value of a CDS contract depends on the expected present value of the premium and protection legs.

### 7.2 CDS Indices

- CDS indices provide diversified exposure to [[Credit Markets Session 1|credit markets]] and are widely used for [[Key Rates O1s Durations and Hedging|hedging]] and speculative purposes.
- The mechanics of CDS indices mirror those of individual CDS contracts,  with adjustments for the surviving notional of the reference [[An Asset Allocation Primer|portfolio]].

### 7.3 Risk Management

- CDS contracts and indices are versatile tools for managing [[Quantitative Trading Strategies Lecture Notes|credit risk]],  enabling investors to hedge,  speculate,  and optimize their portfolios.
- Basis trading and other strategies exploit discrepancies between CDS and bond markets.

By mastering the mechanics,  valuation,  and applications of CDS and CDS indices,  financial professionals can effectively manage [[Quantitative Trading Strategies Lecture Notes|credit risk]] and enhance [[An Asset Allocation Primer|portfolio]] performance.

# Lecture Notes: Credit Default Swaps (CDS) – Par Spreads,  Flat Quoted Spreads,  and Valuation

## 1. Introduction to Par Spreads and Flat Quoted Spreads

- **Par Spread ($S(t,    T)$)**: The par spread is the coupon rate on a CDS contract that results in no upfront cost at inception. It is the spread that equates the present value of the premium leg to the present value of the protection leg.
- **Flat Quoted Spread ($\bar{\mathcal{S}}(t,    T)$)**: The flat quoted spread is the level of a flat CDS par spread curve that matches the model-implied upfront value to the market-quoted upfront value. It assumes a flat [[The Vasicek Model|term structure]] of spreads and is analogous to the bond yield-to-maturity.

### 1.1 Key Differences Between Par Spreads and Flat Quoted Spreads

- **Par Spread**:
  - Requires knowledge of the full [[The Vasicek Model|term structure]] of par spreads for accurate valuation.
  - Cannot be used to imply a [[The Vasicek Model|term structure]] of spreads from a single upfront value.
  - Was the market standard until 2010.
- **Flat Quoted Spread**:
  - Assumes a flat spread curve,  simplifying the valuation process.
  - Provides a one-to-one mapping between the quoted flat spread and the upfront cost of a CDS contract.
  - Has become the market standard since 2010 due to its simplicity and ease of use.

### 1.2 Relationship Between Par Spreads and Flat Quoted Spreads

- If the [[The Vasicek Model|term structure]] of par spreads is flat,  the par spread and flat quoted spread are equal for all maturities.
- If the [[The Vasicek Model|term structure]] is not flat,  the flat quoted spread provides an approximation that ignores the shape of the [[The Vasicek Model|term structure]].

## 2. Valuation Model for CDS Contracts

### 2.1 Requirements for the Model

The valuation model for CDS contracts must satisfy the following:

1. Capture credit events as single events that can occur at any future time.
1. Account for the timing of defaults and allow for a [[The Vasicek Model|term structure]] of [[Credit Markets Session 3|default probabilities]].
1. Incorporate the payment of par minus the [[Credit Markets Session 3|recovery rate]] following a [[Valuation of Credit Default Swaps|credit event]].
1. Reprice the [[The Vasicek Model|term structure]] of market prices exactly.
1. Be fast to calibrate and compute.

### 2.2 Survival Probability ($Q(T)$)

- **Definition**: The [[A Poisson Model of Single Issuer Default|survival probability]] $Q(T)$ is the probability that the [[Lecture Notes 9A- Credit Default Swaps|reference entity]] survives without experiencing a [[Valuation of Credit Default Swaps|credit event]] from today (time 0) to time $T$.
- **Properties**:
  - $Q(T)$ is a constant or decreasing function of $T$.
  - $Q(T)$ lies between 0 and 1.

## 3. Valuation of the Premium Leg

### 3.1 Premium Leg Formula

The premium leg represents the expected present value of the fixed [[Realized Returns|coupon payments]] made by the [[Credit Default Swaps|protection buyer]]. It is given by:
$$
V_{\text{Premium}} = C(T) \sum_{i=1}^N \Delta(t_{i-1},    t_i) Z(t_i) Q(t_i)
$$

Where:

- $C(T)$: Fixed coupon (par spread or quoted spread).
- $\Delta(t_{i-1},    t_i)$: Year fraction between coupon payment dates.
- $Z(t_i)$: [[Discount Factors|Discount factor]] at time $t_i$.
- $Q(t_i)$: [[A Poisson Model of Single Issuer Default|Survival probability]] at time $t_i$.

### 3.2 Accrued Coupon Adjustment

- If a [[Valuation of Credit Default Swaps|credit event]] occurs between coupon payment dates,  the accrued coupon must be accounted for.
- **Accrued Coupon Contribution**:
 $
  \frac{C(T)}{2} \sum_{i=1}^N \Delta(t_{i-1},    t_i) Z(t_i) (Q(t_{i-1}) - Q(t_i))
 $

### 3.3 Total Premium Leg Value

Combining the regular [[Realized Returns|coupon payments]] and the accrued coupon adjustment,  the total premium leg value is:
$$
V_{\text{Premium}} = \frac{C(T)}{2} \sum_{i=1}^N \Delta(t_{i-1},    t_i) Z(t_i) (Q(t_i) + Q(t_{i-1}))
$$

This can be rewritten as:
$$
V_{\text{Premium}} = C(T) A(T)
$$

Where:

- $A(T)$: Risky annuity,  representing the expected present value of the premium leg assuming an annualized coupon of $C(T)$.

## 4. Valuation of the Protection Leg

### 4.1 Protection Leg Formula

The protection leg represents the expected present value of the contingent payment made by the [[Credit Default Swaps|protection seller]] in the event of a [[Valuation of Credit Default Swaps|credit event]]. It is given by:
$$
V_{\text{Protection}} = (1 - R) \sum_{n=1}^M Z(t_n) (Q(t_{n-1}) - Q(t_n))
$$

Where:

- $R$: [[Credit Markets Session 3|Recovery rate]] (assumed to be 40% for senior [[HBR Case Study- Oaktree|unsecured debt]]).
- $Q(t_{n-1}) - Q(t_n)$: Probability of default between $t_{n-1}$ and $t_n$.

## 5. Upfront Cost of a CDS Contract

### 5.1 Definition

The upfront cost $U(0)$ is the cost paid by the [[Credit Default Swaps|protection buyer]] to enter into a CDS contract. It is the difference between the protection leg value and the premium leg value:
$$
U(0) = V_{\text{Protection}} - V_{\text{Premium}}
$$

Substituting the expressions for $V_{\text{Protection}}$ and $V_{\text{Premium}}$:
$$
U(0) = (1 - R) \sum_{n=1}^M Z(t_n) (Q(t_{n-1}) - Q(t_n)) - C(T) A(T)
$$

### 5.2 Relationship Between Upfront Cost and Par Spread

The par spread $S(T)$ is the coupon rate that makes the upfront cost zero:
$$
S(T) A(T) = V_{\text{Protection}}
$$

For a CDS contract with a fixed coupon $C(T)$,  the upfront cost is:
$$
U(0) = (S(T) - C(T)) A(T)
$$

### 5.3 Relationship Between Upfront Cost and Flat Quoted Spread

For a flat quoted spread $\bar{\mathcal{S}}(T)$,  the upfront cost is:
$$
U(0) = (\bar{\mathcal{S}}(T) - C(T)) \bar{A}(T)
$$

Where $\bar{A}(T)$ is the risky annuity calculated using the flat quoted spread.

## 6. Calibration of the Survival Curve

### 6.1 Forward Default Rate ($h(t)$)

- The [[A Poisson Model of Single Issuer Default|survival probability]] $Q(T)$ is expressed in terms of the continuously compounded forward default rate $h(t)$:
$$
Q(T) = \exp\left(-\int_0^T h(t) dt\right)
$$

- A piecewise flat [[The Vasicek Model|term structure]] of $h(t)$ is commonly used for [[Credit Markets Session 4|calibration]].

### 6.2 Bootstrap Calibration

The [[Credit Markets Session 4|calibration]] process involves determining the values of $h(t)$ that match the model-implied upfront values to the market-quoted upfront values for CDS contracts of different maturities.

1. Start with the shortest maturity (e.g.,  6 months) and solve for $h(0.5)$.
1. Use $h(0.5)$ to solve for $h(1.0)$ using the 1-year [[CDS Upfront Amounts|CDS upfront]] value.
1. Repeat for longer maturities.

## 7. Risk Management: Spread DV01

### 7.1 Definition

The Spread DV01 measures the sensitivity of the upfront value of a CDS contract to a 1 basis point parallel shift in the [[Cds-Equivalent Bond Spread|CDS spread]] curve:
$$
\text{Spread DV01} = U(t,    S + 1 \text{bp}) - U(t,    S)
$$

### 7.2 Components of Spread DV01

1. **Primary Term**:
   - Change in the upfront value due to the change in spread:
  $ -A(T,  S + 1 \text{bp}) \cdot 1 \text{bp} $$

1. **Secondary Term**:
   - Change in the risky annuity due to the change in spread:
  $ (S - C) \cdot (A(T,  S) - A(T,  S + 1 \text{bp})) $$

### 7.3 Applications

- Spread DV01 is used to hedge CDS positions against parallel shifts in the spread curve.
- Effective for contracts with similar maturities,  as it assumes parallel shifts in the spread curve.

## 8. Summary and Key Takeaways

### 8.1 Par Spreads and Flat Quoted Spreads

- Par spreads require knowledge of the full [[The Vasicek Model|term structure]] of spreads,  while flat quoted spreads assume a flat curve and simplify valuation.

### 8.2 Valuation of CDS Contracts

- The premium leg and protection leg are valued using survival probabilities,  discount factors,  and recovery rates.
- The upfront cost is the difference between the protection leg value and the premium leg value.

### 8.3 Risk Management

- Spread DV01 measures the sensitivity of a CDS contract to changes in the spread curve and is a key tool for [[Key Rates O1s Durations and Hedging|hedging]] [[Quantitative Trading Strategies Lecture Notes|credit risk]].

By understanding the mechanics,  valuation,  and [[Financial Mathematics Course|risk management]] of CDS contracts,  financial professionals can effectively manage [[Quantitative Trading Strategies Lecture Notes|credit risk]] and optimize their portfolios.

# Lecture Notes: Interest Rate Duration of a CDS and CDS Index Valuation

## 1. Introduction to Interest Rate Sensitivity of a CDS

- The **[[Forward Bond Yield|interest rate sensitivity]]** of a CDS contract is measured by its **IR DV01** (Interest Rate Dollar Value of 01). This metric quantifies the change in the upfront value of the CDS for a 1 basis point (bp) parallel upward shift in the [[A Guide to the Front End and [[Basis Swaps|Basis Swap]] Markets#[[Short-Term Rates and the Transition from LIBOR|London Interbank Offered Rate]] (LIBOR)|LIBOR]] curve,  while keeping the par spread curve fixed.
- The IR DV01 is derived from the dependency of the CDS valuation on the **risky annuity**,  which is the present value of future premium payments.

### 1.1 Formula for IR DV01

The IR DV01 is given by:
$$
\text{IR DV01} = (C - S) \cdot \left(A^*(T) - A(T)\right)
$$

Where:

- \(C\): Deal spread (fixed coupon of the CDS).
- \(S\): Quoted spread (flat spread reflecting the [[Quantitative Trading Strategies Lecture Notes|credit risk]] of the [[Lecture Notes 9A- Credit Default Swaps|reference entity]]).
- \(A(T)\): Risky annuity calculated using the original interest rate curve.
- \(A^*(T)\): Risky annuity calculated using the bumped interest rate curve.

### 1.2 Key Observations

1. **Sign of IR DV01**:
   - If \(C = S\),  the IR DV01 is zero because the CDS is priced at par.
   - If \(C > S\),  the IR DV01 is positive because the CDS buyer is overpaying for protection,  and the value of the risky annuity decreases with higher rates.
   - If \(C < S\),  the IR DV01 is negative because the CDS buyer is underpaying for protection,  and the value of the risky annuity decreases with higher rates.

1. **Magnitude of IR DV01**:
   - The [[Forward Bond Yield|interest rate sensitivity]] of a CDS is generally low compared to a fixed-rate corporate bond with the same maturity. This is because:
	 - A CDS is effectively a credit-risky annuity with annualized [[Realized Returns|coupon payments]] of \((C - S)\).
	 - Unlike a bond,  a CDS does not involve a par payment at maturity.

1. **Comparison to Floating-Rate Notes**:
   - The [[Forward Bond Yield|interest rate sensitivity]] of a CDS closely resembles that of a par floating-rate note issued by the [[Lecture Notes 9A- Credit Default Swaps|reference entity]],  as both instruments are primarily driven by credit spreads rather than [[Interest Rate Quotations|interest rates]].

## 2. Example: IR DV01 of a CDS Contract

### 2.1 CDS Contract Details (Exhibit 69-5)

| **Parameter** | **Value** |

| Notional | $10,  000,  000 |

| Trade Date | February 3,  2011 |

| Maturity | March 20,  2016 |

| Deal Spread (\(C\)) | 100 bp |

| Quoted Spread (\(S\)) | 34.32 bp |

| [[Credit Markets Session 3|Recovery Rate]] | 40% |

| IR DV01 | $84.26 |

### 2.2 Explanation of Valuation Outputs

1. **Price**:
   - The "clean" price of the CDS excludes [[Intra-Year Compounding and Day-Count|accrued interest]] and represents the value of the contract for a [[Credit Default Swaps|protection seller]] who buys the CDS along with a par [[A Guide to the Front End and [[Basis Swaps|Basis Swap]] Markets#[[Short-Term Rates and the Transition from LIBOR|London Interbank Offered Rate]] (LIBOR)|LIBOR]] floating-rate note.

1. **Principal**:
   - The clean value of the contract,  excluding [[Intra-Year Compounding and Day-Count|accrued interest]]. For this CDS,  the principal value is \(-\$322,  035\).

1. **[[Intra-Year Compounding and Day-Count|Accrued Interest]]**:
   - The accrued coupon since the last payment date (December 20,  2010) is \(-\$12,  778\),  reflecting 46 days of a 100 bp coupon.

1. **Cash Amount**:
   - The actual upfront payment required to enter the contract is \(-\$334,  813\). This reflects the compensation to the [[Credit Default Swaps|protection buyer]] for paying a deal spread (\(C = 100\) bp) higher than the quoted spread (\(S = 34.32\) bp).

1. **Spread DV01**:
   - The spread sensitivity of the CDS is \$5,  036.41,  meaning a 1 bp increase in the quoted spread curve increases the value of the CDS by this amount.

1. **IR DV01**:
   - The [[Forward Bond Yield|interest rate sensitivity]] of the CDS is \$84.26,  which is much smaller than the spread DV01,  highlighting that the CDS is primarily a credit-spread product.

## 3. Risky Annuity and Approximation for CDS Valuation

### 3.1 Risky Annuity Formula

The risky annuity \(A(T)\) is the present value of future premium payments,  adjusted for survival probabilities and discount factors. For a simplified approximation:
$$
A(\bar{S},    T) = \frac{1 - \exp\left(-\left(W + \frac{\bar{S}}{1 - R}\right)T\right)}{W + \frac{\bar{S}}{1 - R}} \cdot \frac{365}{360}
$$

Where:

- \(W\): [[Teaching Note 4 Interest Rate Derivatives|Swap rate]] to the contract maturity.
- \(\bar{S}\): Quoted spread.
- \(R\): [[Credit Markets Session 3|Recovery rate]].
- \(T\): [[Hedging Strategies with Forwards|Time to maturity]].

### 3.2 Example Calculation

Using the CDS details from Exhibit 69-5:

- Quoted spread (\(\bar{S}\)): 34.32 bp.
- [[Hedging Strategies with Forwards|Time to maturity]] (\(T\)): 5.122 years.
- [[Teaching Note 4 Interest Rate Derivatives|Swap rate]] (\(W\)): 2.4%.
- [[Credit Markets Session 3|Recovery rate]] (\(R\)): 40%.

The risky annuity is:
$$
A(\bar{S},    T) = \frac{1 - \exp\left(-\left(0.024 + \frac{0.003432}{1 - 0.4}\right) \cdot 5.122\right)}{0.024 + \frac{0.003432}{1 - 0.4}} \cdot \frac{365}{360} = 4.81764
$$

### 3.3 Upfront Value Calculation

The upfront value of the CDS is:
$$
U(t) = \left(\bar{S} - C\right) \cdot A(\bar{S},    T) - \text{Accrued Coupon}
$$

Substituting the values:

- \(\bar{S} = 34.32\) bp,  \(C = 100\) bp,  \(A(\bar{S},  T) = 4.81764\),  and accrued coupon = \(-\$12,  778\):
$$
U(t) = 10,   000,   000 \cdot \frac{(34.32 - 100)}{10,   000} \cdot 4.81764 - 12,   778 = -\$329,   992
$$

This is within 1.5% of the Bloomberg-calculated cash amount (\(-\$334,  813\)).

## 4. CDS Index Valuation

### 4.1 Mechanics of a CDS Index

- A CDS index is equivalent to a [[An Asset Allocation Primer|portfolio]] of CDS contracts on multiple reference credits,  each paying the same index coupon (\(C_I(T)\)).
- Credit events result in the removal of affected credits from the index,  with loss payments made as they occur.

### 4.2 Valuation Formula

The value of a CDS index for a [[Credit Default Swaps|protection seller]] is:
$$
V^{\text{Index}} = \frac{1}{P} \sum_{p=1}^P \left(C_I(T) - S_p(T)\right) A_p(T)
$$

Where:

- \(P\): Number of reference credits in the index.
- \(C_I(T)\): Index coupon.
- \(S_p(T)\): Par spread of reference credit \(p\).
- \(A_p(T)\): Risky annuity of reference credit \(p\).

### 4.3 Simplified Valuation Using Quoted Spread

For practical purposes,  the CDS index is treated as a single CDS contract with a flat quoted spread (\(\bar{S}_I(T)\)):
$$
V^{\text{Index}} = \left(C_I(T) - \bar{S}_I(T)\right) \bar{A}_I(T)
$$

Where:

- \(\bar{A}_I(T)\): Risky annuity of the index.

### 4.4 Risk Management

- The price sensitivities of a CDS index are identical to those of a [[Lecture Notes 9A- Credit Default Swaps|single-name CDS]] with the same [[The Vasicek Model|term structure]] of spreads,  [[Credit Markets Session 3|recovery rate]],  and maturity.
- The **CDS Index Basis** measures the difference between the index spread and the weighted average spread of its constituents. Deviations may arise due to market technical factors or restructuring clauses.

## 5. Summary and Key Takeaways

### 5.1 Interest Rate Sensitivity of a CDS

- The IR DV01 measures the sensitivity of a CDS to changes in [[Interest Rate Quotations|interest rates]] and is generally low compared to its spread sensitivity (Spread DV01).
- The IR DV01 is positive if \(C > S\),  negative if \(C < S\),  and zero if \(C = S\).

### 5.2 CDS Valuation

- The upfront value of a CDS depends on the quoted spread,  deal spread,  risky annuity,  and accrued coupon.
- Simplified approximations can provide valuations within 1.5% of Bloomberg-calculated results.

### 5.3 CDS Index Valuation

- A CDS index is valued as though it were a single CDS contract,  simplifying [[Financial Mathematics Course|risk management]] and [[Arbitrage Pricing of Derivatives|pricing]].
- The CDS Index Basis reflects deviations between the index spread and the weighted average spread of its constituents.

By understanding the mechanics,  valuation,  and [[Financial Mathematics Course|risk management]] of CDS and CDS indices,  financial professionals can effectively manage [[Quantitative Trading Strategies Lecture Notes|credit risk]] and optimize their portfolios.

# Lecture Notes: Credit Default Swaps (CDS) and Performance Attribution

## 1. Introduction to Credit Default Swaps (CDS)

- Credit Default Swaps (CDS) are [[Financial Instruments PSET Solutions|financial derivatives]] that allow the transfer of [[Quantitative Trading Strategies Lecture Notes|credit risk]] from one party to another. They are widely used for [[Key Rates O1s Durations and Hedging|hedging]],  speculation,  and structured credit investments.
- Since the [[Squam Lake Group Introduction|introduction]] of fixed coupons for CDS contracts in 2009,  entering into a CDS contract almost always involves an upfront cash payment,  which can be positive or negative depending on the relationship between the fixed coupon and the market-implied [[Cds-Equivalent Bond Spread|credit spread]].

### 1.1 Key Features of CDS Contracts

- **[[Credit Default Swaps|Protection Buyer]]**: Pays a regular premium (fixed coupon) to the [[Credit Default Swaps|protection seller]] in exchange for protection against credit events.
- **[[Credit Default Swaps|Protection Seller]]**: Receives the premium and compensates the buyer if a [[Valuation of Credit Default Swaps|credit event]] occurs.
- **Upfront Payment**: The size and sign of the upfront payment depend on whether the fixed coupon sufficiently compensates the [[Credit Default Swaps|protection seller]] for the market-perceived risk of a [[Valuation of Credit Default Swaps|credit event]].
  - If the fixed coupon is low,  the [[Credit Default Swaps|protection seller]] may receive cash at trade initiation.
  - If the fixed coupon is high,  the [[Credit Default Swaps|protection seller]] may have to pay cash at trade initiation.
  - The situation is reversed for the [[Credit Default Swaps|protection buyer]].

### 1.2 Purpose of CDS Valuation

- The primary goal of CDS valuation is to calculate the upfront cash payment required to enter the contract.
- This requires a model that:
  - Accounts for the probability and timing of a [[Valuation of Credit Default Swaps|credit event]].
  - Values the premium leg,  considering the risk that not all coupons will be paid.
  - Values the protection leg,  which involves the unknown payment of par minus recovery at the time of a [[Valuation of Credit Default Swaps|credit event]].
  - Flexibly reprices the [[The Vasicek Model|term structure]] of quoted market spreads.

### 1.3 Market Quotes: Par Spread and Flat Quoted Spread

- **CDS Par Spread**:
  - The par spread is the coupon rate that results in a zero upfront value for the CDS contract on the trade date.
  - The value of a CDS is a function of the [[The Vasicek Model|term structure]] of CDS par spreads.
- **Flat Quoted Spread**:
  - Introduced in 2011,  the flat quoted spread assumes a flat [[The Vasicek Model|term structure]] of par spreads that reprices the market-quoted upfront value.
  - Only one quoted spread is needed to value a CDS contract,  simplifying the valuation process.

### 1.4 Forward-Looking Nature of CDS Spreads

- The probability of a CDS experiencing a [[Valuation of Credit Default Swaps|credit event]],  as implied by market spreads,  usually exceeds the historical default probability for credits with the same initial rating.
- This is because CDS spreads are forward-looking and embed a risk premium.

### 1.5 Sensitivity Analysis

- CDS valuation models allow holders to calculate the sensitivity of the contract's value to changes in the quoted spread.
- This enables [[Key Rates O1s Durations and Hedging|hedging]] with other CDS contracts or instruments.

### 1.6 CDS Indices

- For valuation purposes,  a CDS index can be treated as a [[Lecture Notes 9A- Credit Default Swaps|single-name CDS]] and valued using the same model.
- CDS indices provide diversified exposure to [[Credit Markets Session 1|credit markets]] and are widely used for [[Key Rates O1s Durations and Hedging|hedging]] and speculative purposes.

## 2. Principles of Performance Attribution

- Performance attribution is a mathematical framework that splits the total outperformance of a [[An Asset Allocation Primer|portfolio]] versus a benchmark into contributions from individual decisions and actions.
- It helps quantify the contributions of decision-makers,  identify structural issues,  and clarify sources of [[An Asset Allocation Primer|portfolio]] risk and performance.

### 2.1 Key Requirements of Performance Attribution

1. **Additivity**: The contribution of two or more agents combined equals the sum of their individual contributions.
1. **Completeness**: The sum of all contributions equals the total [[An Asset Allocation Primer|portfolio]] outperformance.
1. **Fairness**: The allocation of outperformance to different agents is perceived as fair.

### 2.2 Multi-Period Attribution and Compounding

- Performance attribution over multiple periods must account for dynamic [[The Impact of Option Strategies in Financial  Portfolios Performance|portfolio management]] and compounding effects.
- **Time-Weighted vs. Money-Weighted [[Assets|Returns]]**:
  - Time-weighted [[Assets|returns]] ignore [[An Asset Allocation Primer|portfolio]] size and are appropriate for managers without control over cash flows.
  - Money-weighted [[Assets|returns]] account for cash flows and are suitable for managers responsible for timing cash flows.
- **Example**:
  - A [[An Asset Allocation Primer|portfolio]] with a seed [[An Asset Allocation Primer|investment]] of $1,   000,   000 doubles in value in the first half of the year but loses 10% in the second half after attracting $100,  000,  000 in new investments.
  - Time-weighted return: 80%.
  - Money-weighted return: -17.24%.

### 2.3 Attribution Frequency

- The frequency of the attribution system should match the frequency of [[The Impact of Option Strategies in Financial  Portfolios Performance|portfolio management]] decisions.
- [[Lecture Notes Bonds,  Preferred Stock,  and Structured Products|Fixed income]] portfolios often require daily-frequency attribution models due to their dynamic interest-rate exposures.

### 2.4 Flexibility of Attribution Models

- A practical attribution system must:
  - Measure [[PSET 6- Financial Instruments|risk factors]] corresponding to [[An Asset Allocation Primer|portfolio]] manager decisions.
  - Independently measure contributions of each factor.
  - Align with published [[Assets|returns]] of the fund and its benchmark.
  - Be timely and adaptable to short and long time periods.

## 3. Sector-Based Attribution

- Sector-based attribution decomposes [[An Asset Allocation Primer|portfolio]] outperformance into:
  1. **[[Lecture 2- [[Lecture 2- Asset Allocation with Multiple Risky Assets|Asset Allocation]] with [[Lecture 2- Asset Allocation with Multiple Risky Assets|Multiple Risky Assets]]|[[Lecture 2- Asset Allocation with Multiple Risky Assets|asset allocation]]]]**: Outperformance due to differences in sector weights between the [[An Asset Allocation Primer|portfolio]] and benchmark.
  1. **Security Selection**: Outperformance due to differences in [[Assets|returns]] within each sector.
  1. **Interaction Effect**: Joint effect of [[Lecture 2- [[Lecture 2- Asset Allocation with Multiple Risky Assets|Asset Allocation]] with [[Lecture 2- Asset Allocation with Multiple Risky Assets|Multiple Risky Assets]]|[[Lecture 2- Asset Allocation with Multiple Risky Assets|asset allocation]]]] and security selection.

### 3.1 Mathematical Framework

- [[An Asset Allocation Primer|Portfolio]] return:
 $R^P = \sum_s w_s^P R_s^P$$
- Benchmark return:
 $R^B = \sum_s w_s^B R_s^B$$
- Total outperformance:
 $R^P - R^B = \text{Asset Allocation} + \text{Security Selection} + \text{Interaction}$$
- [[Lecture 2- [[Lecture 2- Asset Allocation with Multiple Risky Assets|Asset Allocation]] with [[Lecture 2- Asset Allocation with Multiple Risky Assets|Multiple Risky Assets]]|[[Lecture 2- Asset Allocation with Multiple Risky Assets|asset allocation]]]]:
 $\sum_s (w_s^P - w_s^B) \cdot R_s^B$$
- Security Selection:
 $\sum_s w_s^B \cdot (R_s^P - R_s^B)$$
- Interaction:
 $\sum_s (w_s^P - w_s^B) \cdot (R_s^P - R_s^B)$$

### 3.2 Recursive Allocation

- Large portfolios often involve multiple layers of management,  requiring recursive application of the attribution framework.
- Each sector can be treated as a smaller [[An Asset Allocation Primer|portfolio]],  with its performance further decomposed into [[Lecture 2- [[Lecture 2- Asset Allocation with Multiple Risky Assets|Asset Allocation]] with [[Lecture 2- Asset Allocation with Multiple Risky Assets|Multiple Risky Assets]]|[[Lecture 2- Asset Allocation with Multiple Risky Assets|asset allocation]]]] and security selection.

## 4. Factor-Based Attribution

- Factor-based attribution decomposes [[An Asset Allocation Primer|portfolio]] [[Assets|returns]] into contributions from common [[PSET 6- Financial Instruments|risk factors]] (e.g.,  [[Interest Rate Quotations|interest rates]],  spreads,  volatility) and a residual.
- **Mathematical Framework**:
 $R^P = \sum_k \alpha_k^P f_k^P + \varepsilon^P$$
 $R^P - R^B = \sum_k (\alpha_k^P - \alpha_k^B) \cdot f_k^P + (\varepsilon^P - \varepsilon^B)$$
- **Advantages**:
  - Explains systematic [[Assets|returns]] using [[PSET 6- Financial Instruments|risk factors]].
  - Residual [[Assets|returns]] are idiosyncratic and small for well-diversified portfolios.
- **Disadvantages**:
  - Limited flexibility in defining [[PSET 6- Financial Instruments|risk factors]].
  - Does not attribute idiosyncratic [[Assets|returns]] to security selection.

## 5. Hybrid Performance Attribution

- The hybrid model combines sector-based and factor-based attribution,  offering flexibility to account for complex management structures.
- **Steps**:
  1. **Return Splitting**: Decompose total [[Assets|returns]] into factor contributions.
  1. **Factor [[Pl Attribution|Return Attribution]]**: Attribute outperformance to individual factors.
  1. **Recursive Application**: Apply the framework recursively to different management layers.

## 6. Summary and Key Takeaways

### 6.1 Credit Default Swaps (CDS)

- CDS contracts involve upfront payments that depend on the relationship between the fixed coupon and market-implied credit spreads.
- Valuation models calculate the expected present value of the premium and protection legs,  accounting for [[Valuation of Credit Default Swaps|credit event]] probabilities and timing.

### 6.2 Performance Attribution

- Performance attribution splits [[An Asset Allocation Primer|portfolio]] outperformance into contributions from [[Lecture 2- [[Lecture 2- Asset Allocation with Multiple Risky Assets|Asset Allocation]] with [[Lecture 2- Asset Allocation with Multiple Risky Assets|Multiple Risky Assets]]|[[Lecture 2- Asset Allocation with Multiple Risky Assets|asset allocation]]]],  security selection,  and [[PSET 6- Financial Instruments|risk factors]].
- Sector-based and factor-based attribution frameworks can be combined into a hybrid model to address the complexity of modern [[The Impact of Option Strategies in Financial  Portfolios Performance|portfolio management]].

By mastering CDS valuation and performance attribution principles,  financial professionals can effectively manage [[Quantitative Trading Strategies Lecture Notes|credit risk]] and optimize [[An Asset Allocation Primer|portfolio]] performance.

# Lecture Notes: Advanced Performance Attribution in Fixed Income Portfolio Management

## 1. Introduction to Performance Attribution

- Performance attribution is a systematic framework used to decompose [[An Asset Allocation Primer|portfolio]] outperformance into contributions from various factors,  decisions,  and exposures.
- It provides insights into the sources of [[Lecture 7-Risk and Return of Bonds|risk and return]],  linking ex-post performance to ex-ante management decisions.
- This lecture focuses on:
  - Factor [[Pl Attribution|return attribution]].
  - Recursive decomposition of outperformance.
  - Applications of performance attribution as a [[The Impact of Option Strategies in Financial  Portfolios Performance|portfolio management]] tool.
  - A detailed example of hybrid performance attribution using a fixed-income [[An Asset Allocation Primer|portfolio]].

## 2. Factor Return Attribution

### 2.1 Common and Allocated Factors

- Factors are categorized into **common factors** and **allocated factors**:
  - **Common Factors**: Shared across the [[An Asset Allocation Primer|portfolio]] and benchmark,  such as yield curve exposure or [[Key Rates O1s Durations and Hedging|duration]].
  - **Allocated Factors**: Specific to individual securities or sectors,  such as credit spreads or security selection.
- The total [[An Asset Allocation Primer|portfolio]] outperformance is expressed as:
$$
R^{P} - R^{B} = \left(\sum_{k \in C} \alpha_{k}^{P} f_{k}^{P} - \sum_{k \in C} \alpha_{k}^{B} f_{k}^{B}\right) + \left(\sum_{k \in A} \alpha_{k}^{P} f_{k}^{P} - \sum_{k \in A} \alpha_{k}^{B} f_{k}^{B}\right)
$$

Where:

- \(R^{P}\): [[An Asset Allocation Primer|Portfolio]] return.
- \(R^{B}\): Benchmark return.
- \(\alpha_{k}^{P}\): [[An Asset Allocation Primer|Portfolio]] exposure to factor \(k\).
- \(\alpha_{k}^{B}\): Benchmark exposure to factor \(k\).
- \(f_{k}^{P}\): [[An Asset Allocation Primer|Portfolio]] factor return.
- \(f_{k}^{B}\): Benchmark factor return.

### 2.2 Decomposition of Factor Outperformance

- For each factor,  the outperformance is decomposed across sectors:
$$
\alpha_{k}^{P} f_{k}^{P} - \alpha_{k}^{B} f_{k}^{B} = \sum_{s} \alpha_{k,   s}^{P} f_{k,   s}^{P} - \sum_{s} \alpha_{k,   s}^{B} f_{k,   s}^{B}
$$

- **Common Factors**:
  - If the factor return is identical for the [[An Asset Allocation Primer|portfolio]] and benchmark (\(f_{k,  s}^{P} = f_{k,  s}^{B}\)),  the contribution simplifies to:
	$$\sum_{s} \left(\alpha_{k,   s}^{P} - \alpha_{k,   s}^{B}\right) \cdot f_{k,   s}$$
  - Example: Yield curve exposure managed at the [[An Asset Allocation Primer|portfolio]] level.
- **Allocated Factors**:
  - Allocated factors may have different realizations for different securities or sectors.
  - Example: Credit spreads,  which vary across securities within a sector.

### 2.3 Allocation Methods

#### Absolute Allocation
- Total [[An Asset Allocation Primer|portfolio]] exposure to a factor is determined by the net sector exposures.
- Decomposition:
  - **[[Lecture 2- [[Lecture 2- Asset Allocation with Multiple Risky Assets|Asset Allocation]] with [[Lecture 2- Asset Allocation with Multiple Risky Assets|Multiple Risky Assets]]|[[Lecture 2- Asset Allocation with Multiple Risky Assets|asset allocation]]]]**:
	$$\sum_{s} \left(\alpha_{k,   s}^{P} - \alpha_{k,   s}^{B}\right) \cdot f_{k,   s}^{B}$$
  - **Sector Management**:
	$$\sum_{s} \alpha_{k,   s}^{P} \cdot \left(f_{k,   s}^{P} - f_{k,   s}^{B}\right)$$

#### Relative Allocation
- Total [[An Asset Allocation Primer|portfolio]] exposure to a factor is determined at the [[An Asset Allocation Primer|portfolio]] level,  with sector exposures constrained by the [[An Asset Allocation Primer|portfolio]] exposure.
- Decomposition:
  - **[[Lecture 2- [[Lecture 2- Asset Allocation with Multiple Risky Assets|Asset Allocation]] with [[Lecture 2- Asset Allocation with Multiple Risky Assets|Multiple Risky Assets]]|[[Lecture 2- Asset Allocation with Multiple Risky Assets|asset allocation]]]]**:
	$$\alpha_{k}^{P} \cdot \sum_{s} \left(\frac{\alpha_{k,   s}^{P}}{\alpha_{k}^{P}} - \frac{\alpha_{k,   s}^{B}}{\alpha_{k}^{B}}\right) \cdot \left(f_{k,   s}^{B} - f_{k}^{H}\right)$$
  - **Sector Management**:
	$$\sum_{s} \alpha_{k,   s}^{P} \cdot \left(f_{k,   s}^{P} - f_{k,   s}^{B}\right)$$
  - **Top-Level Exposure**:
	$$\left(\alpha_{k}^{P} - \alpha_{k}^{B}\right) \cdot f_{k}^{H}$$

Where \(f_{k}^{H}\) is the hurdle rate for the factor.

## 3. Recursive Application of Attribution

- The sector management terms (\(f_{k,  s}^{P} - f_{k,  s}^{B}\)) can be recursively decomposed into subsectors or individual securities.
- At the final stage,  the sector management term becomes **security selection**.
- Example:
  - Top-level [[Key Rates O1s Durations and Hedging|duration]] exposure is decomposed into sector-level [[Key Rates O1s Durations and Hedging|duration]] exposures.
  - Sector-level exposures are further decomposed into individual security contributions.

## 4. Example: Hybrid Performance Attribution

### 4.1 Portfolio Overview

- **Mandate**: Track the Barclays Capital Global Aggregate G4 Index with a tracking error volatility (TEV) limit of 40 bps per month.
- **Manager Views**:
  - Bullish on the Japanese yen.
  - Bearish on the euro.
  - Neutral on the U.S. dollar and British pound.
  - Positive on U.S. corporates,  negative on U.S. securitized sector.
- **[[An Asset Allocation Primer|Portfolio]] Characteristics**:
  - 5% overweight in yen,  5% underweight in euro.
  - 5% overweight in U.S. corporates,  5% underweight in U.S. securitized.
  - [[An Asset Allocation Primer|Portfolio]] [[Key Rates O1s Durations and Hedging|duration]] is 1 year longer than the benchmark.

### 4.2 Performance Attribution Results

#### Total Outperformance
- [[An Asset Allocation Primer|Portfolio]] return: +188.7 bps.
- Benchmark return: +150.0 bps.
- Total outperformance: +38.7 bps.

#### Global Outperformance Summary (Exhibit 70-2)
- **FX Allocation and [[Key Rates O1s Durations and Hedging|Hedging]]**: +28.3 bps.
- **Local Market Allocation**: -8.7 bps.
- **Local Market Management**: +19.1 bps.

#### Local Market Management Details (Exhibit 70-3)
- **Yield-Curve Exposures**: +20.6 bps.
- **[[Lecture 2- Asset Allocation with Multiple Risky Assets|Asset Allocation]]**: +0.2 bps.
- **Security Selection**: -1.7 bps.

### 4.3 FX Outperformance Breakdown (Exhibit 70-4)

- **Yen**:
  - Rally vs. USD: +319.4 bps.
  - [[An Asset Allocation Primer|Portfolio]] overweight: +5%.
  - Contribution: \(5\% \times 319.4 = +16.0\) bps.
- **Euro**:
  - Decline vs. USD: -244.1 bps.
  - [[An Asset Allocation Primer|Portfolio]] underweight: -5%.
  - Contribution: \(-5\% \times -244.1 = +12.0\) bps.
- **British Pound**:
  - Decline vs. USD: -183.5 bps.
  - [[An Asset Allocation Primer|Portfolio]] exposure: 0%.
  - Contribution: 0 bps.
- **Total FX Contribution**: +28.3 bps.

### 4.4 Local Market Allocation (Exhibit 70-5)

- **Yen Local Market**:
  - [[An Asset Allocation Primer|Portfolio]] overweight: +5%.
  - Underperformance: \( (64.2 - 164.1) \times 5\% = -5.0 \) bps.
- **Euro Local Market**:
  - [[An Asset Allocation Primer|Portfolio]] underweight: -5%.
  - Underperformance: \( (239.2 - 164.1) \times -5\% = -3.8 \) bps.
- **Total Local Market Allocation Contribution**: -8.7 bps.

## 5. Applications of Performance Attribution

### 5.1 Linking Ex-Post and Ex-Ante Decisions

- Performance attribution links realized outperformance to the manager's initial views and decisions.
- Example:
  - The manager's bullish yen view contributed +16.1 bps,  validating the decision.
  - The underweight in the euro local market resulted in -3.1 bps,  highlighting an area for improvement.

### 5.2 Identifying Unanticipated Risks

- Attribution exposes unanticipated sources of [[Lecture 7-Risk and Return of Bonds|risk and return]].
- Example:
  - The yen local market underperformance (-5.0 bps) was incidental to the FX overweight and could be addressed in future allocations.

### 5.3 Data Validation

- Recursive decomposition facilitates the discovery of data errors in large financial systems.
- Example:
  - Discrepancies in sector weights or [[Assets|returns]] can be traced back to individual securities.

## 6. Summary and Key Takeaways

### 6.1 Factor Return Attribution

- Common factors (e.g.,  yield curve) are managed at the [[An Asset Allocation Primer|portfolio]] level,  while allocated factors (e.g.,  credit spreads) vary across sectors and securities.
- Absolute and relative allocation frameworks provide flexibility in decomposing outperformance.

### 6.2 Hybrid Attribution

- Hybrid models combine sector-based and factor-based attribution,  enabling detailed analysis of [[An Asset Allocation Primer|portfolio]] performance.
- Recursive decomposition links top-level decisions to individual security contributions.

### 6.3 Portfolio Management Applications

- Performance attribution enhances [[The Impact of Option Strategies in Financial  Portfolios Performance|portfolio management]] by:
  - Validating ex-ante views.
  - Identifying unanticipated risks.
  - Improving decision-making processes.

By mastering advanced performance attribution techniques,  [[An Asset Allocation Primer|portfolio]] managers can systematically evaluate their strategies,  optimize risk-adjusted [[Assets|returns]],  and enhance their decision-making frameworks.

### Lecture Notes: Performance Attribution in Fixed Income Portfolio Management – Local Market and Yield-Curve Analysis

## 1. Introduction to Local Market and Yield-Curve Attribution

- Performance attribution in [[Lecture Notes Bonds,  Preferred Stock,  and Structured Products|fixed income]] [[The Impact of Option Strategies in Financial  Portfolios Performance|portfolio management]] involves analyzing the sources of [[An Asset Allocation Primer|portfolio]] outperformance relative to a benchmark.
- This lecture focuses on:
  - Local market management and its contribution to [[An Asset Allocation Primer|portfolio]] outperformance.
  - Yield-curve exposure and its impact on performance across different currencies.
  - Detailed breakdowns of yield-curve outperformance for the U.S. dollar,  euro,  Japanese yen,  and British pound markets.

## 2. Local Market Management and Outperformance

### 2.1 Breakdown of Local Market Contributions (Exhibit 70-6)

| **Metric** | **U.S. Dollar** | **Euro** | **Japanese Yen** | **British Pound** | **Total** |

| **[[An Asset Allocation Primer|Portfolio]] Weight (%)** | 45.5 | 23.2 | 25.6 | 5.8 | 100.0 |

| **Local Management (bp)**| 14.6 | 6.3 | 2.4 | -4.2 | 19.1 |

| **Yield-Curve (bp)** | 11.2 | 17.9 | 3.0 | -11.5 | 20.6 |

| **[[Lecture 2- Asset Allocation with Multiple Risky Assets|Asset Allocation]] (bp)**| -2.5 | 1.5 | -0.1 | 1.3 | 0.2 |

| **Security Selection (bp)**| 5.9 | -13.3 | -0.5 | 6.2 | -1.7 |

### 2.2 Key Observations

1. **Local Management**:
   - The total contribution from local market management is **+19.1 bp**.
   - Positive contributions came from the U.S. dollar (**+14.6 bp**) and euro (**+6.3 bp**) markets,  while the British pound market detracted **-4.2 bp**.

1. **Yield-Curve Exposure**:
   - Yield-curve exposure contributed **+20.6 bp**,  driven primarily by the U.S. dollar (**+11.2 bp**) and euro (**+17.9 bp**) markets.
   - The British pound market detracted **-11.5 bp** due to unfavorable curve positioning.

1. **Security Selection**:
   - Security selection had a small net impact of **-1.7 bp**.
   - Positive contributions from the U.S. dollar (**+5.9 bp**) and British pound (**+6.2 bp**) markets were offset by a significant negative contribution from the euro market (**-13.3 bp**).

1. **[[Lecture 2- [[Lecture 2- Asset Allocation with Multiple Risky Assets|Asset Allocation]] with [[Lecture 2- Asset Allocation with Multiple Risky Assets|Multiple Risky Assets]]|[[Lecture 2- Asset Allocation with Multiple Risky Assets|asset allocation]]]]**:
   - [[Lecture 2- [[Lecture 2- Asset Allocation with Multiple Risky Assets|Asset Allocation]] with [[Lecture 2- Asset Allocation with Multiple Risky Assets|Multiple Risky Assets]]|[[Lecture 2- Asset Allocation with Multiple Risky Assets|asset allocation]]]] had a negligible impact,  contributing only **+0.2 bp**.

## 3. Yield-Curve Outperformance Analysis

### 3.1 U.S. Dollar Yield-Curve Breakdown (Exhibit 70-7)

| **Metric** | **[[An Asset Allocation Primer|Portfolio]]** | **Benchmark** | **Difference** | **Outperformance (bp)** |

| **Average Yield (%)** | 1.311 | 1.245 | -31.6 bp | |

| **Average [[Key Rates O1s Durations and Hedging|Duration]] (yrs)**| 4.66 | 4.18 | +0.48 yrs | |

| **Parallel Shift (bp)** | | | | +14.6 |

| **Curve Reshaping (bp)** | | | | +10.3 |

| **Total Yield-Curve (bp)**| | | | +24.6 |

#### Key Insights
1. **Parallel Shift**:
   - The [[An Asset Allocation Primer|portfolio]]'s [[Key Rates O1s Durations and Hedging|duration]] overweight of **+0.48 years** contributed **+14.6 bp** of outperformance due to falling yields (bull-flattening of the U.S. Treasury curve).

1. **Curve Reshaping**:
   - A butterfly position,  with an overweight at the 20-year point and underweights at the 5-,  10-,  and 30-year points,  contributed an additional **+10.3 bp**.
   - The 20-year point experienced the largest yield drop (**-48.7 bp**),  driving most of the reshaping outperformance.

1. **Total Contribution**:
   - The total yield-curve outperformance for the U.S. dollar market was **+24.6 bp**.

### 3.2 Euro Yield-Curve Breakdown (Exhibit 70-8)

| **Metric** | **[[An Asset Allocation Primer|Portfolio]]** | **Benchmark** | **Difference** | **Outperformance (bp)** |

| **Average Yield (%)** | 2.030 | 1.698 | -50.2 bp | |

| **Average [[Key Rates O1s Durations and Hedging|Duration]] (yrs)**| 6.68 | 5.62 | +1.05 yrs | |

| **Parallel Shift (bp)** | | | | +54.2 |

| **Curve Reshaping (bp)** | | | | +23.2 |

| **Total Yield-Curve (bp)**| | | | +77.4 |

#### Key Insights
1. **Parallel Shift**:
   - The [[An Asset Allocation Primer|portfolio]]'s [[Key Rates O1s Durations and Hedging|duration]] overweight of **+1.05 years** contributed **+54.2 bp** of outperformance due to falling yields (bull-flattening of the euro curve).

1. **Curve Reshaping**:
   - A butterfly position,  with an overweight at the 10-year point and underweights at the 5and 30-year points,  contributed an additional **+23.2 bp**.

1. **Total Contribution**:
   - The total yield-curve outperformance for the euro market was **+77.4 bp**,  translating to **+17.9 bp** when scaled by the [[An Asset Allocation Primer|portfolio]] weight of **23.2%**.

### 3.3 Japanese Yen Yield-Curve Breakdown (Exhibit 70-8)

| **Metric** | **[[An Asset Allocation Primer|Portfolio]]** | **Benchmark** | **Difference** | **Outperformance (bp)** |

| **Average Yield (%)** | 0.534 | 0.534 | -7.0 bp | |

| **Average [[Key Rates O1s Durations and Hedging|Duration]] (yrs)**| 7.12 | 4.42 | +2.70 yrs | |

| **Parallel Shift (bp)** | | | | +3.0 |

| **Curve Reshaping (bp)** | | | | +0.0 |

| **Total Yield-Curve (bp)**| | | | +3.0 |

#### Key Insights
1. **Parallel Shift**:
   - The [[An Asset Allocation Primer|portfolio]]'s [[Key Rates O1s Durations and Hedging|duration]] overweight of **+2.70 years** contributed **+3.0 bp** of outperformance due to modest yield declines.

1. **Curve Reshaping**:
   - Curve reshaping had no significant impact on performance.

1. **Total Contribution**:
   - The total yield-curve outperformance for the yen market was **+3.0 bp**,  translating to **+0.8 bp** when scaled by the [[An Asset Allocation Primer|portfolio]] weight of **25.6%**.

### 3.4 British Pound Yield-Curve Breakdown (Exhibit 70-8)

| **Metric** | **[[An Asset Allocation Primer|Portfolio]]** | **Benchmark** | **Difference** | **Outperformance (bp)** |

| **Average Yield (%)** | 3.195 | 3.195 | -48.7 bp | |

| **Average [[Key Rates O1s Durations and Hedging|Duration]] (yrs)**| 4.66 | 4.18 | +0.48 yrs | |

| **Parallel Shift (bp)** | | | | -11.5 |

| **Curve Reshaping (bp)** | | | | +0.0 |

| **Total Yield-Curve (bp)**| | | | -11.5 |

#### Key Insights
1. **Parallel Shift**:
   - The [[An Asset Allocation Primer|portfolio]]'s [[Key Rates O1s Durations and Hedging|duration]] overweight contributed **-11.5 bp** of underperformance due to unfavorable yield movements.

1. **Curve Reshaping**:
   - Curve reshaping had no significant impact on performance.

1. **Total Contribution**:
   - The total yield-curve outperformance for the British pound market was **-11.5 bp**,  translating to **-0.7 bp** when scaled by the [[An Asset Allocation Primer|portfolio]] weight of **5.8%**.

## 4. Managerial Implications

### 4.1 Key Takeaways from Yield-Curve Analysis

1. **U.S. Dollar and Euro Markets**:
   - The [[An Asset Allocation Primer|portfolio]]'s [[Key Rates O1s Durations and Hedging|duration]] overweights and curve reshaping positions were well-aligned with market movements,  resulting in significant outperformance.

1. **Japanese Yen Market**:
   - The [[An Asset Allocation Primer|portfolio]]'s [[Key Rates O1s Durations and Hedging|duration]] overweight contributed modestly to outperformance,  but the lack of significant curve reshaping limited the total contribution.

1. **British Pound Market**:
   - The [[An Asset Allocation Primer|portfolio]]'s [[Key Rates O1s Durations and Hedging|duration]] overweight detracted from performance due to unfavorable yield movements.

### 4.2 Recommendations for Future Management

1. **Control Curve Reshaping**:
   - The manager should carefully monitor and control exposure to specific curve points to avoid inadvertent positions.

1. **Diversify Contributions**:
   - Relying heavily on a single market (e.g.,  U.S. dollar) for outperformance increases risk. Diversifying contributions across markets can improve risk-adjusted [[Assets|returns]].

1. **Refine [[Key Rates O1s Durations and Hedging|Duration]] Overweights**:
   - While [[Key Rates O1s Durations and Hedging|duration]] overweights contributed positively in most markets,  the British pound market highlights the need for more precise implementation.

## 5. Summary and Key Takeaways

- Local market management contributed **+19.1 bp** to total [[An Asset Allocation Primer|portfolio]] outperformance,  driven by the U.S. dollar and euro markets.
- Yield-curve exposure was the dominant driver of outperformance,  contributing **+20.6 bp**,  with significant contributions from the U.S. dollar and euro markets.
- The manager should focus on controlling curve reshaping positions and diversifying contributions across markets to enhance future performance.

By understanding the sources of outperformance and refining [[The Impact of Option Strategies in Financial  Portfolios Performance|portfolio management]] strategies,  [[Lecture Notes Bonds,  Preferred Stock,  and Structured Products|fixed income]] managers can optimize risk-adjusted [[Assets|returns]] and achieve their [[An Asset Allocation Primer|investment]] objectives.

### Lecture Notes: Yield-Curve Outperformance Breakdown for Euro,  Japanese Yen,  and British Pound

## 1. Introduction to Yield-Curve Outperformance Analysis

- Yield-curve outperformance analysis is a critical component of fixed-income [[The Impact of Option Strategies in Financial  Portfolios Performance|portfolio management]],  as it quantifies the impact of [[An Asset Allocation Primer|portfolio]] positioning relative to benchmark yield-curve movements.
- This lecture focuses on:
  - Detailed yield-curve outperformance for the **Euro**,  **Japanese Yen**,  and **British Pound** markets.
  - The importance of managing yield-curve exposures across currencies.
  - Implications for [[The Impact of Option Strategies in Financial  Portfolios Performance|portfolio management]] and attribution methodologies.

## 2. Yield-Curve Outperformance Breakdown

### 2.1 Japanese Yen (JPY) Yield-Curve Analysis

#### Key Metrics
- **[[An Asset Allocation Primer|Portfolio]] [[Key Rates O1s Durations and Hedging|Duration]] Overweight**: +2.69 years.
- **Yield-Curve Movement**: Modest bull-flattening,  with a parallel shift of -7.0 bp.
- **Unscaled Outperformance**: +11.8 bp.
- **Scaled Contribution**: +3.0 bp ([[An Asset Allocation Primer|portfolio]] weight: 25.6%).

#### Observations
1. **[[Key Rates O1s Durations and Hedging|Duration]] Overweight**:
   - The [[An Asset Allocation Primer|portfolio]]'s significant [[Key Rates O1s Durations and Hedging|duration]] overweight of +2.69 years was well-positioned to benefit from the modest bull-flattening of the yen yield curve.
   - However,  the magnitude of the yield-curve movement was insufficient to generate substantial outperformance.

1. **[[Key Rates O1s Durations and Hedging|Key Rate]] Contributions**:
   - The 20-year point contributed positively (+3.9 bp unscaled) due to its overweight and a yield drop of -8.1 bp.
   - The 5-year and 7-year points detracted (-4.0 bp and -5.1 bp unscaled,  respectively) due to underperformance relative to their weights.

1. **Implications**:
   - The yen market's contribution to total [[An Asset Allocation Primer|portfolio]] outperformance was modest,  highlighting the need for more pronounced yield-curve movements to capitalize on [[Key Rates O1s Durations and Hedging|duration]] overweights.

### 2.2 British Pound (GBP) Yield-Curve Analysis

#### Key Metrics
- **[[An Asset Allocation Primer|Portfolio]] [[Key Rates O1s Durations and Hedging|Duration]] Underweight**: -3.81 years.
- **Yield-Curve Movement**: Strong bull-flattening,  with a parallel shift of -44.9 bp.
- **Unscaled Underperformance**: -199.2 bp.
- **Scaled Contribution**: -11.5 bp ([[An Asset Allocation Primer|portfolio]] weight: 5.8%).

#### Observations
1. **[[Key Rates O1s Durations and Hedging|Duration]] Underweight**:
   - The [[An Asset Allocation Primer|portfolio]]'s significant [[Key Rates O1s Durations and Hedging|duration]] underweight of -3.81 years was poorly positioned for the strong bull-flattening of the British pound yield curve.
   - The long end of the curve (20-year and 30-year points) experienced substantial yield drops (-49.5 bp and -44.9 bp,  respectively),  exacerbating the underperformance.

1. **[[Key Rates O1s Durations and Hedging|Key Rate]] Contributions**:
   - The 10-year point contributed positively (+2.7 bp unscaled) due to its overweight and a yield drop of -46.7 bp.
   - The 20-year and 30-year points detracted significantly (-11.2 bp and -0.5 bp unscaled,  respectively) due to their underweights and large yield drops.

1. **Implications**:
   - The British pound market's underperformance highlights the risks of significant [[Key Rates O1s Durations and Hedging|duration]] underweights in markets experiencing strong yield-curve movements.
   - Despite the small [[An Asset Allocation Primer|portfolio]] weight (5.8%),  the GBP market's contribution to total [[An Asset Allocation Primer|portfolio]] underperformance was substantial.

### 2.3 Euro (EUR) Yield-Curve Analysis

#### Key Metrics
- **[[An Asset Allocation Primer|Portfolio]] [[Key Rates O1s Durations and Hedging|Duration]] Overweight**: +1.05 years.
- **Yield-Curve Movement**: Bull-flattening,  with a parallel shift of -50.2 bp.
- **Unscaled Outperformance**: +77.4 bp.
- **Scaled Contribution**: +17.9 bp ([[An Asset Allocation Primer|portfolio]] weight: 23.2%).

#### Observations
1. **[[Key Rates O1s Durations and Hedging|Duration]] Overweight**:
   - The [[An Asset Allocation Primer|portfolio]]'s [[Key Rates O1s Durations and Hedging|duration]] overweight of +1.05 years was well-positioned to benefit from the significant bull-flattening of the euro yield curve.
   - The 10-year point experienced the largest yield drop (-46.7 bp),  driving much of the outperformance.

1. **[[Key Rates O1s Durations and Hedging|Key Rate]] Contributions**:
   - The 10-year point contributed positively (+2.7 bp unscaled) due to its overweight and a yield drop of -46.7 bp.
   - The 5-year point contributed modestly (+1.2 bp unscaled),  while the 20-year point detracted slightly (-11.2 bp unscaled).

1. **Implications**:
   - The euro market's contribution to total [[An Asset Allocation Primer|portfolio]] outperformance was significant,  demonstrating the benefits of well-aligned [[Key Rates O1s Durations and Hedging|duration]] overweights in markets with pronounced yield-curve movements.

## 3. Implications for Portfolio Management

### 3.1 Importance of Yield-Curve Management

- The analysis underscores the critical role of yield-curve management in fixed-income [[An Asset Allocation Primer|portfolio]] performance.
- **Key Takeaways**:
  - [[Key Rates O1s Durations and Hedging|Duration]] overweights and underweights must be carefully aligned with expected yield-curve movements.
  - Significant underweights in markets with strong yield-curve movements (e.g.,  GBP) can lead to substantial underperformance,  even with small [[An Asset Allocation Primer|portfolio]] weights.

### 3.2 Global vs. Local Curve Management

- The [[An Asset Allocation Primer|portfolio]] manager may decide to prioritize **global yield-curve management** over local market allocation and management decisions.
- **Rationale**:
  - Yield-curve movements often dominate other sources of outperformance or underperformance.
  - A global approach ensures consistent alignment of [[Key Rates O1s Durations and Hedging|duration]] exposures across currencies.

### 3.3 Attribution Methodology Adjustments

- If global yield-curve management is prioritized,  the attribution methodology should exclude yield-curve outperformance from the **Local Market Allocation** and **Local Management** components.
- **Alternative Attribution Framework**:
  - Yield-curve outperformance is attributed to a separate **Global Curve Management** component.
  - Local market allocation and management focus solely on sector and security selection.

## 4. [[Lecture 2- Asset Allocation with Multiple Risky Assets|asset allocation]] and Security Selection

### 4.1 U.S. Dollar [[Lecture 2- Asset Allocation with Multiple Risky Assets|asset allocation]] (Exhibit 70-9)

#### Key Metrics
- **[[An Asset Allocation Primer|Portfolio]] Weight**: 45.5%.
- **Corporate Bond Overweight**: +5.0%.
- **Unscaled Underperformance**: -5.5 bp.
- **Scaled Contribution**: -2.5 bp.

#### Observations
1. **[[Class Notes 2 – Corporate Bond Contracts|Corporate Bonds]]**:
   - The [[An Asset Allocation Primer|portfolio]]'s overweight to U.S. [[Class Notes 2 – Corporate Bond Contracts|Corporate Bonds]] contributed -5.2 bp to unscaled underperformance.
   - This was driven by the significant underperformance of the corporate sector in the benchmark (-70.2 bp) relative to the benchmark itself (-22.0 bp).

1. **Treasury and Government-Related Sectors**:
   - These sectors had no contribution to [[Lecture 2- [[Lecture 2- Asset Allocation with Multiple Risky Assets|Asset Allocation]] with [[Lecture 2- Asset Allocation with Multiple Risky Assets|Multiple Risky Assets]]|[[Lecture 2- Asset Allocation with Multiple Risky Assets|asset allocation]]]],  as their weights were matched exactly between the [[An Asset Allocation Primer|portfolio]] and benchmark.

1. **Securitized Sector**:
   - The securitized sector had minimal contribution to [[Lecture 2- [[Lecture 2- Asset Allocation with Multiple Risky Assets|Asset Allocation]] with [[Lecture 2- Asset Allocation with Multiple Risky Assets|Multiple Risky Assets]]|[[Lecture 2- Asset Allocation with Multiple Risky Assets|asset allocation]]]],  as its performance (-19.0 bp) was close to that of the benchmark (-22.0 bp).

### 4.2 Implications for [[Lecture 2- Asset Allocation with Multiple Risky Assets|asset allocation]]

- The manager's overweight to U.S. [[Class Notes 2 – Corporate Bond Contracts|Corporate Bonds]] was a key source of underperformance,  highlighting the risks of sector overweights in underperforming markets.
- **Recommendations**:
  - Reassess sector overweights in light of benchmark performance trends.
  - Consider diversifying sector exposures to mitigate the impact of underperformance in specific sectors.

## 5. Summary and Key Takeaways

### 5.1 Yield-Curve Outperformance

- The **Euro** market contributed significantly to total [[An Asset Allocation Primer|portfolio]] outperformance (+17.9 bp),  driven by well-aligned [[Key Rates O1s Durations and Hedging|duration]] overweights and strong bull-flattening.
- The **Japanese Yen** market contributed modestly (+3.0 bp),  as the yield-curve movement was insufficiently pronounced.
- The **British Pound** market detracted significantly (-11.5 bp),  highlighting the risks of [[Key Rates O1s Durations and Hedging|duration]] underweights in markets with strong yield-curve movements.

### 5.2 Portfolio Management Implications

- Yield-curve management is a critical driver of fixed-income [[An Asset Allocation Primer|portfolio]] performance and should be prioritized in the [[Exercises|portfolio construction]] process.
- The manager should consider adopting a global yield-curve management framework to ensure consistent alignment of [[Key Rates O1s Durations and Hedging|duration]] exposures across currencies.

### 5.3 [[Lecture 2- Asset Allocation with Multiple Risky Assets|asset allocation]] and Security Selection

- The U.S. dollar market's [[Lecture 2- [[Lecture 2- Asset Allocation with Multiple Risky Assets|Asset Allocation]] with [[Lecture 2- Asset Allocation with Multiple Risky Assets|Multiple Risky Assets]]|[[Lecture 2- Asset Allocation with Multiple Risky Assets|asset allocation]]]] contributed -2.5 bp to total [[An Asset Allocation Primer|portfolio]] underperformance,  driven by the overweight to [[Class Notes 2 – Corporate Bond Contracts|Corporate Bonds]].
- The manager should reassess sector overweights and consider diversifying exposures to mitigate the impact of sector underperformance.

By understanding the sources of yield-curve outperformance and refining [[The Impact of Option Strategies in Financial  Portfolios Performance|portfolio management]] strategies,  fixed-income managers can optimize risk-adjusted [[Assets|returns]] and achieve their [[An Asset Allocation Primer|investment]] objectives.

## Lecture Notes: U.S. and Euro Security Selection Breakdown and Performance Attribution

### 1. Introduction to Security Selection and Performance Attribution

- Security selection is a critical component of fixed-income [[The Impact of Option Strategies in Financial  Portfolios Performance|portfolio management]],  as it directly impacts [[An Asset Allocation Primer|portfolio]] outperformance relative to the benchmark.
- This lecture focuses on:
  - The U.S. security selection breakdown and its contribution to [[An Asset Allocation Primer|portfolio]] outperformance.
  - The Euro security selection breakdown and its significant underperformance.
  - Key takeaways and recommendations for improving security selection and managing risks.

### 2. U.S. Security Selection Breakdown (Exhibit 70-10)

#### 2.1 Overview of U.S. Security Selection

| **Sector** | **[[An Asset Allocation Primer|Portfolio]] Weight (%)** | **Benchmark Weight (%)** | **Excess Return ([[An Asset Allocation Primer|Portfolio]],  bp)** | **Excess Return (Benchmark,  bp)** | **Security Selection (bp)** |

| **Total** | 100.0 | 100.0 | -14.6 | -22.0 | +13.0 |

| **Treasury** | 31.7 | 31.7 | -4.7 | -2.2 | -0.8 |

| **Govt-Related** | 14.3 | 14.3 | +17.6 | -7.7 | +3.7 |

| **Corporate** | 30.7 | 19.8 | -33.5 | -70.2 | +11.1 |

| **Securitized** | 22.8 | 33.4 | -23.3 | -19.0 | -1.0 |

| **Cash** | 0.5 | 0.8 | 0.0 | 0.0 | 0.0 |

#### 2.2 Key Observations

1. **Corporate Sector**:
   - The corporate sector contributed **+11.1 bp** to security selection outperformance,  making it the dominant contributor.
   - Positive contributions came from securities such as **[[Lessons From The Crisis|Morgan Stanley]] (+3.9 bp)**,  **Rabobank (+3.7 bp)**,  and **[[The Fall of Bear Stearns|JP Morgan]] (+3.4 bp)**.
   - However,  the **Comcast 6.45% 2037 bond** detracted **-6.3 bp**,  highlighting the importance of scrutinizing individual names.

1. **Government-Related Sector**:
   - The government-related sector contributed **+3.7 bp**,  driven by strong performance from securities such as **Israel State of (+1.5 bp)** and **Federal National Mortgage Association (FNMA) bonds (+2.0 bp)**.

1. **Treasury Sector**:
   - The Treasury sector detracted **-0.8 bp**,  with underperformance concentrated in specific securities such as **US Treasury Bonds (912810FP,  -1.1 bp)**.

1. **Securitized Sector**:
   - The securitized sector detracted **-1.0 bp**,  with notable underperformance from securities such as **GNMAI Single Family 15yr (-2.2 bp)**.

#### 2.3 Comcast Bond Analysis

- The **Comcast 6.45% 2037 bond** had an **excess return of -280.0 bp**,  significantly underperforming the benchmark (-70.2 bp).
- Contribution to U.S. corporate security selection:
 $\text{Contribution} = 30.7\% \times 10.1\% \times (-280.0 + 70.2) = -6.4 \,  \text{bp}$$
- Contribution to global outperformance:
 $\text{Global Contribution} = 45.5\% \times -6.4 \,  \text{bp} = -2.9 \,  \text{bp}$$
- **Implication**: The Comcast bond's significant underperformance highlights the importance of name selection in a concentrated [[An Asset Allocation Primer|portfolio]].

### 3. Euro Security Selection Breakdown (Exhibit 70-11)

#### 3.1 Overview of Euro Security Selection

| **Sector** | **[[An Asset Allocation Primer|Portfolio]] Weight (%)** | **Benchmark Weight (%)** | **Excess Return ([[An Asset Allocation Primer|Portfolio]],  bp)** | **Excess Return (Benchmark,  bp)** | **Security Selection (bp)** |

| **Total** | 100.0 | 100.0 | -121.0 | -69.7 | -57.4 |

| **Treasury** | 44.0 | 55.4 | -275.8 | -122.4 | -66.6 |

| **Govt-Related** | 7.5 | 15.3 | -119.4 | -6.3 | -8.2 |

| **Corporate** | 43.8 | 17.6 | +18.4 | -23.0 | +18.2 |

#### 3.2 Key Observations

1. **Treasury Sector**:
   - The Treasury sector detracted **-66.6 bp**,  driven by significant underperformance of **Italian government bonds**.
   - Notable detractors include:
	 - **Italy (IT0004009673,  -20.7 bp)**.
	 - **Italy (IT0004356843,  -21.6 bp)**.

1. **Government-Related Sector**:
   - The government-related sector detracted **-8.2 bp**,  with underperformance concentrated in **Poland (Republic of,  -8.1 bp)**.

1. **Corporate Sector**:
   - The corporate sector contributed **+18.2 bp**,  driven by strong performance from securities such as **GE Capital (+8.0 bp)** and **Royal Bank of Scotland (+3.5 bp)**.

#### 3.3 Italian Government Bond Analysis

- Italian government bonds were the main culprits for the euro market's underperformance,  contributing significantly to the **-66.6 bp** Treasury sector security selection.
- **Implication**: The manager should take control of country exposure within the euro sector to mitigate sovereign [[Quantitative Trading Strategies Lecture Notes|credit risk]].

### 4. Key Takeaways and Recommendations

#### 4.1 U.S. Security Selection

1. **Corporate Sector**:
   - The corporate sector was the dominant contributor to U.S. security selection outperformance (**+11.1 bp**).
   - However,  the **Comcast bond's underperformance (-6.3 bp)** highlights the importance of scrutinizing individual names.

1. **Government-Related Sector**:
   - Strong performance from government-related securities (**+3.7 bp**) underscores the value of diversifying across high-quality issuers.

1. **Recommendations**:
   - Enhance name selection processes to avoid significant detractors like Comcast.
   - Continue leveraging strong performers in the corporate and government-related sectors.

#### 4.2 Euro Security Selection

1. **Treasury Sector**:
   - The Treasury sector's significant underperformance (**-66.6 bp**) was driven by Italian government bonds.
   - The manager should actively manage country exposure within the euro sector to mitigate sovereign [[Quantitative Trading Strategies Lecture Notes|credit risk]].

1. **Corporate Sector**:
   - The corporate sector contributed positively (**+18.2 bp**),  driven by strong performers like GE Capital and Royal Bank of Scotland.

1. **Recommendations**:
   - Reduce exposure to high-risk sovereigns like Italy.
   - Focus on high-quality corporate issuers to drive outperformance.

### 5. Summary and Key Takeaways

1. **U.S. Security Selection**:
   - The U.S. corporate sector was the dominant contributor to security selection outperformance,  but individual detractors like Comcast highlight the importance of name selection.

1. **Euro Security Selection**:
   - The euro market's significant underperformance was driven by Italian government bonds,  underscoring the need for active [[How Countries Go Broke-Chapter 15 & Chapter 16|country risk]] management.

1. **Recommendations**:
   - Enhance name selection processes to avoid significant detractors.
   - Actively manage country exposure within the euro sector to mitigate sovereign [[Quantitative Trading Strategies Lecture Notes|credit risk]].
   - [[Lecture 6-Leverage, Tail Risk, Volatility Products|Leverage]] strong performers in the corporate and government-related sectors to drive outperformance.

By addressing these areas,  [[An Asset Allocation Primer|portfolio]] managers can optimize security selection and improve overall [[An Asset Allocation Primer|portfolio]] performance.

### Lecture Notes: Advanced Performance Attribution in Fixed Income Portfolio Management – Euro Security Selection and Analytical Models

## 1. Introduction to Euro Security Selection and Analytical Models

- Performance attribution in [[Lecture Notes Bonds,  Preferred Stock,  and Structured Products|fixed income]] portfolios involves decomposing [[Assets|returns]] into contributions from various factors,  such as yield-curve movements,  credit spreads,  and security selection.
- This lecture focuses on:
  - The detailed breakdown of Euro security selection and its impact on [[An Asset Allocation Primer|portfolio]] performance.
  - The role of fully analytical models in identifying residuals and improving data quality.
  - The importance of scenario-based return decomposition and analytics-based attribution in [[Lecture Notes Bonds,  Preferred Stock,  and Structured Products|fixed income]] portfolios.

## 2. Euro Security Selection Breakdown

### 2.1 Overview of Euro Security Selection (Exhibit 70-11)

| **Bucket/Issue** | **Issuer** | **$MV(\%)$ Portf** | **Excess to Curve [[Assets|Returns]] (bp)** | **Security Selection (bp)** |

| **IBESM** | IBERDROLA | 22.7 | 1.1 | 2.2 |

| **$BAC$** | MERRILL LYNCH & CO INC | 13.2 | 5.5 | 2.0 |

| **IMTLN** | IMPERIAL TOBACCO FIN PLC | 16.7 | 0.9 | 1.6 |

| **$C$** | CITIGROUP INC | 4.8 | -181.4 | -2.7 |

| **Bmark Securities** | Not in [[An Asset Allocation Primer|Portfolio]] | 90.5 | -22.8 | -0.1 |

| **Securitized** | | 4.4 | 11.3 | -0.7 |

| **ES0312298237** | AYT CEDULAS CAJAS GLOBAL | 100.0 | 11.3 | -0.7 |

| **Cash** | | 0.3 | 0.0 | 0.0 |

#### Key Observations
1. **Positive Contributors**:
   - **IBERDROLA** contributed **+2.2 bp** due to strong excess [[Assets|returns]] of **1.1 bp**.
   - **MERRILL LYNCH & CO INC** contributed **+2.0 bp**,  driven by excess [[Assets|returns]] of **5.5 bp**.
   - **IMPERIAL TOBACCO FIN PLC** added **+1.6 bp**,  with excess [[Assets|returns]] of **0.9 bp**.

1. **Negative Contributors**:
   - **CITIGROUP INC** detracted **-2.7 bp**,  with significant underperformance of **-181.4 bp** relative to the curve.
   - **Securitized** securities detracted **-0.7 bp**,  despite positive excess [[Assets|returns]] of **11.3 bp**,  due to their small [[An Asset Allocation Primer|portfolio]] weight.

1. **Benchmark Securities**:
   - Securities not in the [[An Asset Allocation Primer|portfolio]] contributed **-0.1 bp**,  reflecting missed opportunities in the benchmark.

### 2.2 Residual Analysis and Data Quality Issues (Exhibit 70-13)

| **Bucket/Issue** | **Issuer** | **$MV(\%)$ Portf** | **Spread Carry (bp)** | **[[Profit and Loss Attribution with an OAS|Spread Change]] (bp)** | **Residual (bp)** | **Total (bp)** |

| **IT0004513641** | $ITALY$ | 18.3 | 0.6 | -22.3 | +17.4 | -3.7 |

| **IT0004356843** | $ITALY$ | 17.1 | 0.5 | -16.8 | -0.1 | -16.4 |

| **IT0004009673** | $ITALY$ | 15.8 | 0.3 | -17.1 | -0.1 | -16.9 |

#### Key Observations
1. **Residual Contribution**:
   - The bond **IT0004513641** contributed **+17.4 bp** of residual to the Euro [[An Asset Allocation Primer|portfolio]],  accounting for **+4.0 bp** of the total [[An Asset Allocation Primer|portfolio]]-level residual.
   - This residual was traced to a **data quality issue**,  where a coupon payment of **2.50%** was recorded twice.

1. **Impact of Data Correction**:
   - After correcting the double entry,  the [[An Asset Allocation Primer|portfolio]] return decreased by **4.2 bp**,  and the residual term was reduced from **+4.4 bp** to **+0.2 bp**.

1. **Implications**:
   - Residuals can indicate data quality problems,  such as incorrect prices,  transaction errors,  or model deficiencies.
   - A robust performance attribution system can help identify and correct such issues promptly.

## 3. Fully Analytical Models and Scenario-Based Decomposition

### 3.1 Fully Analytical Models

- Fully analytical models decompose [[Assets|returns]] into detailed components,  providing greater clarity into the sources of outperformance.
- **Key Features**:
  - Incorporates terms such as **[[A Real-Life Option Pricing Exercise|Implied Volatility]]** and **Mortgage Contributions**.
  - Identifies residuals and their potential causes,  such as data errors or model deficiencies.

### 3.2 Scenario-Based Return Decomposition (Exhibit 71-1)

| **Return Component** | **Description** |

| **Surprise Return** | Difference between actual cash flows and model predictions. |

| **Time Return** | Effect of elapsing time. |

| **Yield-Curve Change Return** | Effect of changes in the yield curve. |

| **[[A Real-Life Option Pricing Exercise|Implied Volatility]] Change** | Effect of changes in the [[Modeling Volatility Smile and Heston Model Calibration Using QuantLib Python|implied volatility surface]]. |

| **Other Market Return** | Effect of changes in other market parameters. |

| **[[Profit and Loss Attribution with an OAS|Spread Change]] Return** | Effect of changes in the option-adjusted spread (OAS). |

#### Key Insights
1. **Surprise Return**:
   - Relevant for securities with non-[[1. DeterministicCashFlows|deterministic cash flows]],  such as [[Fremont Financial Corp. (b)|mortgage-backed securities]] or [[War Economies and Hyperinflation|inflation]]-linked bonds.
   - Captures deviations between realized and projected parameters.

1. **Residual**:
   - Represents unexplained differences between actual and modeled [[Assets|returns]].
   - Can result from unaccounted model inputs,  higher-order terms,  or data errors.

## 4. Implications for Portfolio Management

### 4.1 Importance of Data Quality

- Data quality issues,  such as incorrect prices or duplicate entries,  can significantly impact performance measurement and attribution.
- **Example**:
  - The double entry of a coupon payment for **IT0004513641** inflated the residual by **+17.4 bp**,  masking the true sources of outperformance.

### 4.2 Managing Spread Duration Exposure

- The Euro [[An Asset Allocation Primer|portfolio]]'s concentration in Italian government bonds,  particularly long-maturity issues,  resulted in significant [[Spread Duration and Dvo1|spread duration]] exposure.
- **Recommendation**:
  - [[Spread Duration and Dvo1|Spread duration]] exposure in sectors with [[Quantitative Trading Strategies Lecture Notes|credit risk]] should be carefully controlled to avoid excessive sensitivity to spread changes.

### 4.3 Enhancing Attribution Models

- Fully analytical models provide a more detailed breakdown of [[Assets|returns]],  allowing managers to identify and address specific sources of outperformance or underperformance.
- **Benefits**:
  - Greater transparency into residuals and their causes.
  - Improved alignment between attribution results and [[The Impact of Option Strategies in Financial  Portfolios Performance|portfolio management]] decisions.

## 5. Summary and Key Takeaways

### 5.1 Euro Security Selection

- Positive contributors included **IBERDROLA** and **MERRILL LYNCH & CO INC**,  while **CITIGROUP INC** and Italian government bonds detracted significantly.
- Data quality issues,  such as the double entry for **IT0004513641**,  can inflate residuals and distort performance attribution.

### 5.2 Fully Analytical Models

- Fully analytical models decompose [[Assets|returns]] into detailed components,  such as [[A Real-Life Option Pricing Exercise|implied volatility]] and spread changes,  providing greater clarity into the sources of outperformance.
- Scenario-based decomposition helps identify residuals and their potential causes,  such as data errors or model deficiencies.

### 5.3 Recommendations for Portfolio Management

1. **Improve Data Quality**:
   - Regularly audit data to identify and correct errors,  such as duplicate entries or incorrect prices.

1. **Control [[Spread Duration and Dvo1|Spread Duration]] Exposure**:
   - Avoid excessive concentration in sectors with high [[Quantitative Trading Strategies Lecture Notes|credit risk]],  such as long-maturity Italian government bonds.

1. **Adopt Fully Analytical Models**:
   - Use detailed attribution models to gain deeper insights into the sources of [[An Asset Allocation Primer|portfolio]] performance and residuals.

By addressing these areas,  [[An Asset Allocation Primer|portfolio]] managers can enhance performance attribution,  improve decision-making,  and optimize risk-adjusted [[Assets|returns]].

### Lecture Notes: Advanced Performance Attribution in Fixed Income Portfolio Management – Prepayment,  Inflation,  and Yield-Curve Returns

## 1. Introduction to Advanced Attribution Components

- [[Lecture Notes Bonds,  Preferred Stock,  and Structured Products|Fixed income]] [[An Asset Allocation Primer|portfolio]] performance attribution involves decomposing [[Assets|returns]] into various components,  such as prepayment surprises,  [[War Economies and Hyperinflation|inflation]] surprises,  time [[Assets|returns]],  yield-curve changes,  and spread changes.
- This lecture focuses on:
  - **Prepayment Surprise Return**: The impact of deviations in actual prepayments from model [[FORWARD RATES AND TERM STRUCTURE|expectations]].
  - **[[War Economies and Hyperinflation|Inflation]] Surprise Return**: The effect of unexpected [[War Economies and Hyperinflation|inflation]] announcements on [[War Economies and Hyperinflation|inflation]]-linked securities.
  - **Time Return**: The deterministic return component driven by yield-curve carry,  spread carry,  and volatility decay.
  - **Yield-Curve Change Return**: The impact of interest rate movements on [[An Asset Allocation Primer|portfolio]] [[Assets|returns]],  including [[An Analytical Decomposition of Forward Rates|duration and convexity]] effects.

## 2. Prepayment Surprise Return

### 2.1 Definition and Example

- **Prepayment Surprise Return** measures the difference between actual prepayments and model-projected prepayments for [[Fremont Financial Corp. (b)|mortgage-backed securities]] (MBS).
- **Example**:
  - **Security Price**: 105 (zero accrued).
  - **Model-Projected Prepayment**: 2.4% (25% CPR),  predicting a return of **+11.4 bp**.
  - **Actual Prepayment**: 1.3% (15% CPR),  resulting in a return of **-6.2 bp**.
  - **Prepayment Surprise Return**:
	$$\text{Surprise Return} = -6.2 \,    \text{bp} - 11.4 \,    \text{bp} = +5.2 \,    \text{bp}$$
- **Key Insight**:
  - The model-[[Lecture 1- Probability Distributions of Returns|expected return]] (**+11.4 bp**) is part of the **time return** component,  while the deviation (**+5.2 bp**) is attributed to prepayment surprise.

## 3. Inflation Surprise Return

### 3.1 Definition and Example

- **[[War Economies and Hyperinflation|Inflation]] Surprise Return** captures the impact of unexpected [[War Economies and Hyperinflation|inflation]] announcements on [[War Economies and Hyperinflation|inflation]]-linked securities.
- **Example**:
  - **Projected [[War Economies and Hyperinflation|Inflation]]**: 3.0%.
  - **Actual [[War Economies and Hyperinflation|Inflation]]**: 3.5%.
  - **[[War Economies and Hyperinflation|Inflation]] Surprise Return**: **+4.2 bp** due to higher-than-expected [[War Economies and Hyperinflation|inflation]] accretion.
- **Key Insight**:
  - This return is separate from any changes in future [[War Economies and Hyperinflation|inflation]] [[FORWARD RATES AND TERM STRUCTURE|expectations]],  which are captured under **[[War Economies and Hyperinflation|inflation]] [[Profit and Loss Attribution with an OAS|spread change]]**.

## 4. Time Return

### 4.1 Components of Time Return

- **Time Return** is the deterministic component of return,  assuming no changes in market parameters.
- **Components**:
  - **Yield-Curve Carry**: Return from rolling down the yield curve.
  - **Spread Carry**: Return from holding securities with positive spreads.
  - **Volatility Decay**: Return from the passage of time reducing the value of optionality.
  - **[[War Economies and Hyperinflation|Inflation]] Accretion**: Return from [[War Economies and Hyperinflation|inflation]]-linked securities due to projected [[War Economies and Hyperinflation|inflation]].
  - **[[War Economies and Hyperinflation|Inflation]] Spread Carry**: Return from holding [[War Economies and Hyperinflation|inflation]]-linked securities with positive spreads.

## 5. Yield-Curve Change Return

### 5.1 Definition and Sensitivities

- **Yield-Curve Change Return** measures the impact of interest rate movements on [[An Asset Allocation Primer|portfolio]] [[Assets|returns]].
- **Sensitivities**:
  - **Option-Adjusted [[Key Rates O1s Durations and Hedging|Duration]] (OAD)**: Sensitivity to parallel shifts in the yield curve.
  - **Key-Rate Durations (KRDs)**: Sensitivity to movements at specific points on the yield curve.
  - **Option-Adjusted [[PSET II Fixed Income Asset Pricing 1|Convexity]] (OAC)**: Second-order sensitivity to yield-curve changes.

### 5.2 Duration and Convexity Example

- **[[An Asset Allocation Primer|Portfolio]] Characteristics**:
  - **OAD**: 5.
  - **OAC**: -2.
- **Scenario**:
  - [[Interest Rate Quotations|Interest rates]] fall by **10 bp per day** over 10 business days,  for a total change of **-100 bp**.
- **Formula**:
 $R^{\Delta YC} = -OAD \cdot \Delta r + \frac{1}{2} \cdot \frac{OAC}{100} \cdot \Delta r^2$$
- **Calculation**:
  - **[[Key Rates O1s Durations and Hedging|Duration]] Return**:
	$$-5 \cdot (-100) = +500 \,    \text{bp}$$
  - **[[PSET II Fixed Income Asset Pricing 1|Convexity]] Return**:
	$$0.5 \cdot \frac{-2}{100} \cdot (-100)^2 = -100 \,    \text{bp}$$
  - **Total Return**:
	$$+500 \,    \text{bp} - 100 \,    \text{bp} = +400 \,    \text{bp}$$

### 5.3 Daily Attribution Adjustments

- **Daily Adjustments**:
  - [[Key Rates O1s Durations and Hedging|Duration]] drift due to falling [[Interest Rate Quotations|interest rates]] reduces the [[An Asset Allocation Primer|portfolio]]'s [[Key Rates O1s Durations and Hedging|duration]] by approximately 2 years over 10 days.
  - [[Assets|Returns]] must be compounded daily.
- **Adjusted [[Assets|Returns]]**:
  - **[[Key Rates O1s Durations and Hedging|Duration]] Return**: **+408 bp**.
  - **[[PSET II Fixed Income Asset Pricing 1|Convexity]] Return**: **-10 bp**.
  - **Total Return**: **+398 bp**.
- **Key Insight**:
  - Daily attribution models typically show smaller [[PSET II Fixed Income Asset Pricing 1|convexity]] contributions compared to [[Key Rates O1s Durations and Hedging|duration]] contributions.

### 5.4 Key-Rate Duration Attribution

- **Key-Rate Durations (KRDs)**:
  - Capture the contribution of yield-curve changes at specific points (e.g.,  2-year,  5-year,  10-year).
  - Any unexplained yield-curve change return is attributed to movements between key-rate points or higher-order terms.

## 6. Implied Volatility Change Return

### 6.1 Definition and Sensitivities

- **[[A Real-Life Option Pricing Exercise|Implied Volatility]] Change Return** measures the impact of changes in [[A Real-Life Option Pricing Exercise|implied volatility]] on securities with optionality.
- **Sensitivity**:
  - **Vega**: Price change for a 1% parallel shift in the [[Modeling Volatility Smile and Heston Model Calibration Using QuantLib Python|implied volatility surface]].
- **Advanced Models**:
  - Generate partial Vegas for multiple points on the [[7. Black Scholes Model|volatility surface]].
  - Decompose [[A Real-Life Option Pricing Exercise|implied volatility]] change return into parallel and non-parallel components.

### 6.2 Example

- **Scenario**:
  - Vega: 0.5.
  - Parallel Volatility Shift: +2%.
  - **Parallel Component**:
	$$\text{Return} = 0.5 \cdot 2 = +1.0 \,    \text{bp}$$
  - **Non-Parallel Component**:
	- Captures the effects of reshaping the [[7. Black Scholes Model|volatility surface]] and interactions with other model parameters.

## 7. Spread Change Return

### 7.1 Definition and Sensitivities

- **[[Profit and Loss Attribution with an OAS|Spread Change]] Return** measures the impact of changes in option-adjusted spreads (OAS) on [[An Asset Allocation Primer|portfolio]] [[Assets|returns]].
- **Sensitivities**:
  - **[[Spread Duration and Dvo1|Spread Duration]] (OASD)**: First-order sensitivity to spread changes.
  - **Spread [[PSET II Fixed Income Asset Pricing 1|Convexity]] (OASC)**: Second-order sensitivity to spread changes.

### 7.2 Example

- **Scenario**:
  - OASD: 4.
  - OASC: -1.
  - Spread widens by **50 bp**.
- **Formula**:
 $R^{\Delta \text{Spread}} = -OASD \cdot \Delta \text{Spread} + \frac{1}{2} \cdot OASC \cdot (\Delta \text{Spread})^2$$
- **Calculation**:
  - **[[Key Rates O1s Durations and Hedging|Duration]] Return**:
	$$-4 \cdot 50 = -200 \,    \text{bp}$$
  - **[[PSET II Fixed Income Asset Pricing 1|Convexity]] Return**:
	$$0.5 \cdot (-1) \cdot (50)^2 = -125 \,    \text{bp}$$
  - **Total Return**:
	$$-200 \,    \text{bp} - 125 \,    \text{bp} = -325 \,    \text{bp}$$

## 8. Other Market Return

### 8.1 Definition

- **Other Market Return** captures the impact of changes in external factors not directly related to yield-curve or [[A Real-Life Option Pricing Exercise|implied volatility]] changes.
- **Examples**:
  - [[Fremont Financial Corp. (b)|Mortgage-backed securities]]: [[Mortgage Pools|Prepayment rates]],  home price appreciation [[FORWARD RATES AND TERM STRUCTURE|expectations]].
  - [[War Economies and Hyperinflation|Inflation]]-linked securities: Changes in [[War Economies and Hyperinflation|inflation]] [[FORWARD RATES AND TERM STRUCTURE|expectations]].

## 9. Summary and Key Takeaways

### 9.1 Prepayment and Inflation Surprises

- **Prepayment Surprise Return**: Captures deviations in actual prepayments from model [[FORWARD RATES AND TERM STRUCTURE|expectations]].
- **[[War Economies and Hyperinflation|Inflation]] Surprise Return**: Measures the impact of unexpected [[War Economies and Hyperinflation|inflation]] announcements on [[War Economies and Hyperinflation|inflation]]-linked securities.

### 9.2 Yield-Curve and Spread Changes

- **Yield-Curve Change Return**: Driven by [[An Analytical Decomposition of Forward Rates|duration and convexity]] effects,  with key-rate durations capturing specific curve movements.
- **[[Profit and Loss Attribution with an OAS|Spread Change]] Return**: Captures the impact of OAS changes,  with [[PSET II Fixed Income Asset Pricing 1|convexity]] effects becoming significant during large spread moves.

### 9.3 Advanced Attribution Models

- Fully analytical models provide detailed decompositions of [[Assets|returns]],  enabling [[An Asset Allocation Primer|portfolio]] managers to identify and address specific sources of outperformance or underperformance.
- Scenario-based decomposition is essential for securities with complex cash flows or optionality.

By mastering these advanced attribution components,  [[Lecture Notes Bonds,  Preferred Stock,  and Structured Products|fixed income]] [[An Asset Allocation Primer|portfolio]] managers can optimize risk-adjusted [[Assets|returns]] and enhance decision-making processes.

# Lecture Notes: Advanced Performance Attribution in Fixed Income Portfolio Management – Two-Level [[Lecture 2- Asset Allocation with Multiple Risky Assets|asset allocation]],  Yield-Curve Exposure,  and Excess Return Model

## 1. Introduction to Two-Level [[Lecture 2- Asset Allocation with Multiple Risky Assets|asset allocation]] and Performance Attribution

- Performance attribution in [[Lecture Notes Bonds,  Preferred Stock,  and Structured Products|fixed income]] portfolios involves decomposing [[Assets|returns]] into contributions from [[Lecture 2- [[Lecture 2- Asset Allocation with Multiple Risky Assets|Asset Allocation]] with [[Lecture 2- Asset Allocation with Multiple Risky Assets|Multiple Risky Assets]]|[[Lecture 2- Asset Allocation with Multiple Risky Assets|asset allocation]]]],  security selection,  and exposure to common factors such as yield-curve movements and [[A Real-Life Option Pricing Exercise|implied volatility]].
- This lecture focuses on:
  - Two-level [[Lecture 2- [[Lecture 2- Asset Allocation with Multiple Risky Assets|Asset Allocation]] with [[Lecture 2- Asset Allocation with Multiple Risky Assets|Multiple Risky Assets]]|[[Lecture 2- Asset Allocation with Multiple Risky Assets|asset allocation]]]] and its impact on performance attribution.
  - Yield-curve exposure and its contribution to outperformance.
  - The Excess Return Model and its application in separating yield-curve and excess return contributions.

## 2. Two-Level Asset Allocation Using the Total Return Model

### 2.1 Overview of Two-Level Asset Allocation

- Two-level [[Lecture 2- [[Lecture 2- Asset Allocation with Multiple Risky Assets|Asset Allocation]] with [[Lecture 2- Asset Allocation with Multiple Risky Assets|Multiple Risky Assets]]|[[Lecture 2- Asset Allocation with Multiple Risky Assets|asset allocation]]]] introduces a finer partition of asset classes into subsectors,  providing a more detailed breakdown of outperformance.
- **Key Insight**:
  - The finer the partition,  the more emphasis is placed on [[Lecture 2- [[Lecture 2- Asset Allocation with Multiple Risky Assets|Asset Allocation]] with [[Lecture 2- Asset Allocation with Multiple Risky Assets|Multiple Risky Assets]]|[[Lecture 2- Asset Allocation with Multiple Risky Assets|asset allocation]]]] decisions versus security selection decisions.
  - Conversely,  broader partitions attribute more outperformance to security selection.

### 2.2 Level 1 Asset Allocation Breakdown (Exhibit 71-6)

| **Partition Bucket** | **Market Weight (%)** | **Return ex Common Factors** | **Outperformance (bps)** |

| **Total** | 100.0 | [[An Asset Allocation Primer|Portfolio]]: 161.6,  Benchmark: 129.8 | [[Lecture 2- Asset Allocation with Multiple Risky Assets|Asset Allocation]]: +18.9,  Further Allocation: -16.0,  Security Selection: +29.2 |

| **Treasury** | 31.7 | [[An Asset Allocation Primer|Portfolio]]: 315.4,  Benchmark: 201.1 | [[Lecture 2- Asset Allocation with Multiple Risky Assets|Asset Allocation]]: 0.0,  Security Selection: +36.3 |

| **Government-Related** | 14.3 | [[An Asset Allocation Primer|Portfolio]]: 123.9,  Benchmark: 129.5 | [[Lecture 2- Asset Allocation with Multiple Risky Assets|Asset Allocation]]: 0.0,  Further Allocation: -4.7,  Security Selection: +3.9 |

| **Corporate** | 30.7 | [[An Asset Allocation Primer|Portfolio]]: 107.9,  Benchmark: 196.1 | [[Lecture 2- Asset Allocation with Multiple Risky Assets|Asset Allocation]]: +7.4,  Further Allocation: -8.6,  Security Selection: -18.7 |

| **Securitized** | 22.8 | [[An Asset Allocation Primer|Portfolio]]: 49.1,  Benchmark: 27.1 | [[Lecture 2- Asset Allocation with Multiple Risky Assets|Asset Allocation]]: +11.0,  Further Allocation: -2.6,  Security Selection: +7.6 |

| **Cash** | 0.5 | [[An Asset Allocation Primer|Portfolio]]: 0.0,  Benchmark: 0.0 | [[Lecture 2- Asset Allocation with Multiple Risky Assets|Asset Allocation]]: +0.5,  Security Selection: 0.0 |

#### Key Observations
1. **Treasury Sector**:
   - Security selection contributed **+36.3 bp**,  driven by strong performance relative to the benchmark.
1. **Corporate Sector**:
   - Further allocation detracted **-8.6 bp**,  primarily due to an overweight in [[Financial Markets and Institutions Lecture Notes|financial institutions]],  which underperformed the corporate benchmark.
1. **Securitized Sector**:
   - Security selection contributed **+7.6 bp**,  driven by strong performance in RMBS securities.

### 2.3 Level 2 Asset Allocation Breakdown (Exhibit 71-7)

#### Government-Related Sector

| **Partition Bucket** | **Market Weight (%)** | **Return ex Common Factors** | **Outperformance (bps)** |

| **Agency** | [[An Asset Allocation Primer|Portfolio]]: 98.3,  Benchmark: 70.5 | [[An Asset Allocation Primer|Portfolio]]: 121.7,  Benchmark: 94.3 | [[Lecture 2- Asset Allocation with Multiple Risky Assets|Asset Allocation]]: -1.4,  Security Selection: +3.9 |

| **Local Authority** | [[An Asset Allocation Primer|Portfolio]]: 0.0,  Benchmark: 6.8 | [[An Asset Allocation Primer|Portfolio]]: N/A,  Benchmark: 330.7 | [[Lecture 2- Asset Allocation with Multiple Risky Assets|Asset Allocation]]: -2.0,  Security Selection: 0.0 |

| **Sovereign** | [[An Asset Allocation Primer|Portfolio]]: 1.7,  Benchmark: 12.6 | [[An Asset Allocation Primer|Portfolio]]: 253.4,  Benchmark: 232.7 | [[Lecture 2- Asset Allocation with Multiple Risky Assets|Asset Allocation]]: -1.6,  Security Selection: 0.0 |

| **Supranational** | [[An Asset Allocation Primer|Portfolio]]: 0.0,  Benchmark: 10.0 | [[An Asset Allocation Primer|Portfolio]]: N/A,  Benchmark: 113.5 | [[Lecture 2- Asset Allocation with Multiple Risky Assets|Asset Allocation]]: +0.2,  Security Selection: 0.0 |

#### Corporate Sector

| **Partition Bucket** | **Market Weight (%)** | **Return ex Common Factors** | **Outperformance (bps)** |

| **Industrial** | [[An Asset Allocation Primer|Portfolio]]: 19.6,  Benchmark: 51.1 | [[An Asset Allocation Primer|Portfolio]]: 171.3,  Benchmark: 214.6 | [[Lecture 2- Asset Allocation with Multiple Risky Assets|Asset Allocation]]: -1.8,  Security Selection: -2.6 |

| **Utility** | [[An Asset Allocation Primer|Portfolio]]: 0.0,  Benchmark: 10.4 | [[An Asset Allocation Primer|Portfolio]]: N/A,  Benchmark: 251.2 | [[Lecture 2- Asset Allocation with Multiple Risky Assets|Asset Allocation]]: -1.8,  Security Selection: 0.0 |

| **[[Financial Markets and Institutions Lecture Notes|Financial Institutions]]** | [[An Asset Allocation Primer|Portfolio]]: 80.4,  Benchmark: 38.5 | [[An Asset Allocation Primer|Portfolio]]: 92.4,  Benchmark: 157.0 | [[Lecture 2- Asset Allocation with Multiple Risky Assets|Asset Allocation]]: -5.1,  Security Selection: -16.1 |

## 3. Yield-Curve Exposure and Outperformance

### 3.1 Yield-Curve Contribution to Outperformance

- Yield-curve exposure includes:
  - **Yield-Curve Change**: Impact of [[How Countries Go Broke-Chapter 12 to Chapter 14|interest rate changes]].
  - **Yield-Curve Carry**: Impact of rolling down the yield curve.
- **Key Insight**:
  - The total yield-curve effect is the sum of yield-curve change and carry,  regardless of the methodology used.

### 3.2 Methodology I: Rolling on Forwards

- A yield-curve is deemed unchanged if rates realize the values implied by forward rates.
- **Example**:
  - One-month forward one-year rate is used as the reference for the one-year rate one month into the future.
- **Implications**:
  - Carry accrues at the [[An Overview of the Vasicek Short Rate Model|short rate]].
  - Yield-curve change is calculated relative to forward rates.

### 3.3 Methodology II: Static Yield-Curve

- A yield-curve is deemed unchanged if rates remain constant over time.
- **Implications**:
  - Carry accrues at the long rate.
  - Yield-curve change is calculated relative to the static curve.

## 4. Excess Return Model

### 4.1 Overview of the Excess Return Model

- The Excess Return Model separates outperformance into:
  - **Yield-Curve Contribution**: Exposure to [[How Countries Go Broke-Chapter 12 to Chapter 14|interest rate changes]] and carry.
  - **Excess Return**: Outperformance relative to the yield curve,  including [[Lecture 2- Asset Allocation with Multiple Risky Assets|asset allocation]] and security selection.

### 4.2 Excess Return Model Breakdown (Exhibit 71-8)

| **Component** | **Yield-Curve Only (bps)** | **Yield-Curve + [[A Real-Life Option Pricing Exercise|Implied Volatility]] (bps)** |

| **Yield-Curve** | +24.6 | +24.6 |

| **[[A Real-Life Option Pricing Exercise|Implied Volatility]]** | N/A | +1.9 |

| **[[Lecture 2- Asset Allocation with Multiple Risky Assets|Asset Allocation]]** | -2.2 | -4.0 |

| **Security Selection** | +9.7 | +9.6 |

#### Key Observations
1. **Yield-Curve Contribution**:
   - Yield-curve exposure contributed **+24.6 bp** to outperformance.
1. **[[A Real-Life Option Pricing Exercise|Implied Volatility]] Contribution**:
   - Adding [[A Real-Life Option Pricing Exercise|implied volatility]] as a common factor contributed an additional **+1.9 bp**.
1. **[[Lecture 2- [[Lecture 2- Asset Allocation with Multiple Risky Assets|Asset Allocation]] with [[Lecture 2- Asset Allocation with Multiple Risky Assets|Multiple Risky Assets]]|[[Lecture 2- Asset Allocation with Multiple Risky Assets|asset allocation]]]]**:
   - [[Lecture 2- Asset Allocation with Multiple Risky Assets|Asset allocation]] detracted **-2.2 bp** when only yield-curve exposure was considered,  and **-4.0 bp** when [[A Real-Life Option Pricing Exercise|implied volatility]] was included.
1. **Security Selection**:
   - Security selection contributed **+9.7 bp** with yield-curve exposure and **+9.6 bp** with [[A Real-Life Option Pricing Exercise|implied volatility]].

## 5. Implications for Portfolio Management

### 5.1 Importance of Two-Level [[Lecture 2- Asset Allocation with Multiple Risky Assets|asset allocation]]

- Two-level [[Lecture 2- [[Lecture 2- Asset Allocation with Multiple Risky Assets|Asset Allocation]] with [[Lecture 2- Asset Allocation with Multiple Risky Assets|Multiple Risky Assets]]|[[Lecture 2- Asset Allocation with Multiple Risky Assets|asset allocation]]]] provides a more granular view of [[An Asset Allocation Primer|portfolio]] decisions,  highlighting the impact of subsector allocations.
- **Recommendation**:
  - Use two-level attribution to identify underperforming subsectors and refine allocation decisions.

### 5.2 Managing Yield-Curve Exposure

- Yield-curve exposure is a significant driver of [[Lecture Notes Bonds,  Preferred Stock,  and Structured Products|fixed income]] outperformance.
- **Recommendation**:
  - Align [[Key Rates O1s Durations and Hedging|duration]] and key-rate exposures with expected yield-curve movements to maximize carry and minimize adverse [[Profit and Loss Attribution with an OAS|rate changes]].

### 5.3 Incorporating Implied Volatility

- [[A Real-Life Option Pricing Exercise|Implied volatility]] is an important factor for securities with optionality.
- **Recommendation**:
  - Include [[A Real-Life Option Pricing Exercise|implied volatility]] in attribution models to capture its contribution to outperformance.

## 6. Summary and Key Takeaways

### 6.1 Two-Level [[Lecture 2- Asset Allocation with Multiple Risky Assets|asset allocation]]

- Two-level [[Lecture 2- [[Lecture 2- Asset Allocation with Multiple Risky Assets|Asset Allocation]] with [[Lecture 2- Asset Allocation with Multiple Risky Assets|Multiple Risky Assets]]|[[Lecture 2- Asset Allocation with Multiple Risky Assets|asset allocation]]]] provides a detailed breakdown of outperformance,  highlighting the impact of subsector allocations.
- [[Lecture 2- Asset Allocation with Multiple Risky Assets|Asset allocation]] contributed **+2.9 bp**,  while security selection contributed **+29.2 bp** in the two-level model.

### 6.2 Yield-Curve Exposure

- Yield-curve exposure contributed **+24.6 bp** to outperformance,  driven by both yield-curve change and carry.
- Methodologies for defining yield-curve changes (rolling on [[Forwards and Futures|forwards]] vs. static yield-curve) affect the breakdown but not the total contribution.

### 6.3 Excess Return Model

- The Excess Return Model separates yield-curve and excess return contributions,  providing a clearer view of [[An Asset Allocation Primer|portfolio]] performance.
- Adding [[A Real-Life Option Pricing Exercise|implied volatility]] as a common factor enhances the model's explanatory power.

By adopting advanced attribution techniques,  [[Lecture Notes Bonds,  Preferred Stock,  and Structured Products|fixed income]] [[An Asset Allocation Primer|portfolio]] managers can optimize risk-adjusted [[Assets|returns]],  refine allocation decisions,  and enhance their understanding of performance drivers.

### Lecture Notes: Advanced Yield-Curve and Implied Volatility Attribution in Fixed Income Portfolio Management

## 1. Introduction to Yield-Curve and Implied Volatility Attribution

- Yield-curve and [[A Real-Life Option Pricing Exercise|implied volatility]] changes are critical drivers of fixed-income [[An Asset Allocation Primer|portfolio]] performance. Proper attribution of these components provides insights into the sources of outperformance or underperformance relative to a benchmark.
- This lecture focuses on:
  - **Yield-Curve Carry and Change**: Decomposing yield-curve contributions into carry and reshaping effects.
  - **[[A Real-Life Option Pricing Exercise|Implied Volatility]] Attribution**: Breaking down volatility contributions into decay,  parallel shifts,  and surface reshaping.
  - Practical examples using the Barclays HPA model to illustrate these concepts.

## 2. Yield-Curve Attribution

### 2.1 Yield-Curve Carry Attribution

#### 2.1.1 Overview of Yield-Curve Carry
- **Definition**: Yield-curve carry measures the return from holding a security as it rolls down the yield curve,  assuming no changes in [[Interest Rate Quotations|interest rates]].
- **Key Components**:
  - **Average Carry**: The difference in average yields between the [[An Asset Allocation Primer|portfolio]] and the benchmark.
  - **Key-Rate Contributions**: The excess carry at specific key-rate points relative to the average carry.

#### 2.1.2 Curve Matching Portfolio (CMP) Method
- **Purpose**: Simplifies yield-curve carry calculations by constructing a [[An Asset Allocation Primer|portfolio]] of reference bonds (par or zero-coupon) that matches the cash-flow profile of the security.
- **Steps**:
  1. Match the key-rate durations of the [[An Asset Allocation Primer|portfolio]] and benchmark using reference bonds.
  1. Adjust for cash to ensure the present value of the matching [[An Asset Allocation Primer|portfolio]] equals the security's price.
  1. Calculate carry contributions using the yields of the reference bonds.

#### 2.1.3 Example: Yield-Curve Carry Attribution
- **[[An Asset Allocation Primer|Portfolio]] Average Yield**: 2.030%.
- **Benchmark Average Yield**: 1.698%.
- **Elapsed Time**: 1 month.
- **Average Carry Contribution**:
 $(2.030\% - 1.698\%) \times \frac{1}{12} = +2.8 \,  \text{bp}$$
- **Key-Rate Contributions**:
  - **2-Year Point**:
	$$[39.5\% \times (0.771\% - 2.030\%) + 37.4\% \times (0.771\% - 1.698\%)] \times \frac{1}{12} = -1.3 \,    \text{bp}$$
  - **10-Year Point**:
	$$[40.1\% \times (2.708\% - 2.030\%) + 18.5\% \times (2.708\% - 1.698\%)] \times \frac{1}{12} = +14.1 \,    \text{bp}$$

#### 2.1.4 Total Yield-Curve Carry Contribution
- **Average Carry**: +2.9 bp.
- **Key-Rate Contributions**: Sum of individual key-rate contributions.
- **Total Carry**: +2.9 bp (average) + key-rate contributions.

### 2.2 Yield-Curve Change Attribution

#### 2.2.1 Overview of Yield-Curve Change
- **Definition**: Yield-curve change measures the impact of interest rate movements on [[An Asset Allocation Primer|portfolio]] [[Assets|returns]],  including parallel shifts,  reshaping,  and [[PSET II Fixed Income Asset Pricing 1|convexity]] effects.
- **Key Components**:
  - **Parallel Shift**: The average change in yields across the curve.
  - **Reshaping**: Changes in the relative levels of key-rate points.
  - **[[PSET II Fixed Income Asset Pricing 1|Convexity]] and Higher-Order Terms**: Residual effects not captured by key-rate durations.

#### 2.2.2 Example: Yield-Curve Change Attribution
- **[[An Asset Allocation Primer|Portfolio]] OAD**: 6.7 years.
- **Benchmark OAD**: 5.6 years.
- **Parallel Shift**: -50.2 bp.
- **Parallel Shift Contribution**:
 $(6.7 - 5.6) \times (-50.2) = +54.2 \,  \text{bp}$$
- **Reshaping Contribution**:
 $-\sum_{j} \left(KRD_{j}^{P} - KRD_{j}^{B}\right) \cdot \left(\Delta y_{j} - \Delta y_{\text{avg}}\right)$$
  - **10-Year Point**:
	$$[3.6 - 1.7] \times (-57.3 - (-50.2)) = +14.1 \,    \text{bp}$$
  - **30-Year Point**:
	$$[0.0 - 0.6] \times (-69.6 - (-50.2)) = -11.5 \,    \text{bp}$$

#### 2.2.3 Total Yield-Curve Change Contribution
- **Parallel Shift**: +54.2 bp.
- **Reshaping**: Sum of key-rate contributions.
- **[[PSET II Fixed Income Asset Pricing 1|Convexity]] and Residual**: +8.3 bp.
- **Total Change**: +74.4 bp.

## 3. Implied Volatility Attribution

### 3.1 Components of Implied Volatility Attribution

#### 3.1.1 Volatility Decay
- **Definition**: Measures the change in option value due to the passage of time,  assuming no changes in [[A Real-Life Option Pricing Exercise|implied volatility]].
- **Calculation**:
  - Subtract all other components of the total time return (e.g.,  yield-curve carry,  spread carry).
  - **Example**:
	$$\text{Volatility Decay Return} = \text{Total Time Return} - (\text{Yield-Curve Carry} + \text{Spread Carry})$$

#### 3.1.2 Parallel Shift of Implied Volatility Surface
- **Definition**: Measures the impact of a uniform change in [[A Real-Life Option Pricing Exercise|implied volatility]] across all maturities and strikes.
- **Calculation**:
 $\text{Parallel Shift Return} = \text{Vega} \times \Delta \text{Volatility}$$
  - **Example**:
	- Vega: 0.5.
	- Parallel Shift: +2%.
	- Return: $$0.5 \times 2 = +1.0 \,    \text{bp}$$

#### 3.1.3 Surface Reshaping
- **Definition**: Measures the impact of non-parallel changes in the [[Modeling Volatility Smile and Heston Model Calibration Using QuantLib Python|implied volatility surface]].
- **Calculation**:
 $\text{Reshaping Return} = \text{Total Volatility Return} - \text{Parallel Shift Return}$$

### 3.2 Example: Implied Volatility Attribution (Exhibit 71-11)

| **Component** | **Decay (bp)** | **Parallel (bp)** | **Reshaping (bp)** | **Total (bp)** |

| **Total** | -0.5 | +6.2 | -3.8 | +1.9 |

| **Treasury** | 0.0 | 0.0 | 0.0 | 0.0 |

| **Government-Related**| 0.0 | +0.2 | -0.2 | 0.0 |

| **Corporate** | +0.1 | -0.6 | +0.9 | +0.3 |

| **Securitized** | -0.6 | +6.6 | -4.5 | +1.5 |

#### Key Observations
1. **Total Volatility Contribution**: +1.9 bp.
1. **Corporate Sector**: Contributed +0.3 bp,  driven by reshaping effects.
1. **Securitized Sector**: Contributed +1.5 bp,  driven by parallel shifts.

## 4. Practical Implications for Portfolio Management

### 4.1 Yield-Curve Management
- **Key Takeaways**:
  - Align [[Key Rates O1s Durations and Hedging|duration]] and key-rate exposures with expected yield-curve movements to maximize carry and minimize adverse [[Profit and Loss Attribution with an OAS|rate changes]].
  - Use the CMP method to simplify carry calculations and improve attribution accuracy.

### 4.2 Implied Volatility Management
- **Key Takeaways**:
  - Monitor Vega exposures to manage sensitivity to parallel shifts in [[A Real-Life Option Pricing Exercise|implied volatility]].
  - Analyze surface reshaping effects to identify opportunities for outperformance in securities with optionality.

### 4.3 Enhancing Attribution Models
- **Recommendations**:
  - Incorporate [[A Real-Life Option Pricing Exercise|implied volatility]] into attribution models to capture its contribution to outperformance.
  - Use scenario-based and analytics-based methods to decompose [[Assets|returns]] into detailed components.

## 5. Summary and Key Takeaways

### 5.1 Yield-Curve Attribution
- Yield-curve carry and change are significant drivers of fixed-income [[An Asset Allocation Primer|portfolio]] performance.
- The CMP method simplifies carry calculations,  while key-rate durations provide a detailed breakdown of yield-curve change contributions.

### 5.2 Implied Volatility Attribution
- [[A Real-Life Option Pricing Exercise|Implied volatility]] contributions include decay,  parallel shifts,  and surface reshaping.
- Proper attribution of volatility effects enhances the understanding of performance drivers in securities with optionality.

### 5.3 Practical Applications
- Advanced attribution techniques provide deeper insights into [[An Asset Allocation Primer|portfolio]] performance,  enabling managers to optimize risk-adjusted [[Assets|returns]] and refine [[An Asset Allocation Primer|investment]] strategies.

By mastering these advanced attribution methodologies,  fixed-income [[An Asset Allocation Primer|portfolio]] managers can enhance their decision-making processes and achieve superior performance outcomes.

# Lecture Notes: Advanced Performance Attribution in Fixed Income Portfolio Management – Implied Volatility,  Spread,  and Mortgage Factors

## 1. Introduction to Advanced Attribution Components

- Advanced performance attribution in [[Lecture Notes Bonds,  Preferred Stock,  and Structured Products|fixed income]] portfolios involves decomposing [[Assets|returns]] into contributions from [[A Real-Life Option Pricing Exercise|implied volatility]],  spread changes,  and mortgage-specific factors.
- This lecture focuses on:
  - **[[A Real-Life Option Pricing Exercise|Implied Volatility]] Attribution**: Contributions from parallel shifts,  surface reshaping,  and volatility decay.
  - **Spread Attribution**: Top-level and sector-level models for spread carry,  [[Spread Duration and Dvo1|spread duration]],  and spread [[PSET II Fixed Income Asset Pricing 1|convexity]].
  - **Mortgage Factors**: Prepayment surprises,  mortgage spread changes,  and other mortgage-specific factors.

## 2. Implied Volatility Attribution

### 2.1 Overview of Implied Volatility Attribution

- **[[A Real-Life Option Pricing Exercise|Implied Volatility]] Exposure**:
  - Bonds with embedded options,  such as callable [[Class Notes 2 – Corporate Bond Contracts|Corporate Bonds]] and [[Fremont Financial Corp. (b)|mortgage-backed securities]] (MBS),  have exposure to [[A Real-Life Option Pricing Exercise|implied volatility]].
  - Issuers of such bonds are long volatility,  while holders are short volatility,  as indicated by negative exposure numbers.
- **[[An Asset Allocation Primer|Portfolio]] Positioning**:
  - The [[An Asset Allocation Primer|portfolio]] is **long volatility** overall,  with a larger exposure to the securitized sector compared to the corporate and government-related sectors.
  - During the attribution period,  implied volatilities increased by **5.71%**,  leading to:
	- **Corporate Sector**: Negative contribution of **-0.6 bp** due to underweight [[JP Morgan-Variance Swaps|volatility exposure]].
	- **Securitized Sector**: Positive contribution of **+6.6 bp** due to overweight [[JP Morgan-Variance Swaps|volatility exposure]].
- **Total Contribution**:
  - Parallel volatility change contributed **+6.2 bp**.
  - Surface reshaping contributed **-3.8 bp**.
  - Volatility decay contributed **-0.5 bp**.
  - **Net Contribution**: **+1.9 bp**.

### 2.2 Key Components of Implied Volatility Attribution

#### 2.2.1 Parallel Volatility Shift
- **Definition**: Measures the impact of a uniform change in [[A Real-Life Option Pricing Exercise|implied volatility]] across all maturities and strikes.
- **Example**:
  - Corporate sector: **-0.6 bp**.
  - Securitized sector: **+6.6 bp**.
  - **Total Contribution**: **+6.2 bp**.

#### 2.2.2 Surface Reshaping
- **Definition**: Measures the impact of non-parallel changes in the [[Modeling Volatility Smile and Heston Model Calibration Using QuantLib Python|implied volatility surface]].
- **Contribution**: **-3.8 bp**.

#### 2.2.3 Volatility Decay
- **Definition**: Measures the loss of return due to the passage of time,  which reduces the value of optionality.
- **Contribution**: **-0.5 bp**.

### 2.3 Implications for Portfolio Management

- **Volatility Positioning**:
  - The [[An Asset Allocation Primer|portfolio]]'s overweight in the securitized sector resulted in a net long volatility position,  which benefited from rising implied volatilities.
  - Managers should monitor sector-level volatility exposures to optimize contributions from parallel shifts and surface reshaping.

## 3. Spread Attribution

### 3.1 Overview of Spread Attribution

- Spread attribution decomposes outperformance into:
  - **Spread Carry**: Return from holding securities with positive spreads.
  - **[[Spread Duration and Dvo1|Spread Duration]]**: Return from [[Pl Attribution|changes in spreads]],  weighted by [[Spread Duration and Dvo1|spread duration]].
  - **Spread [[PSET II Fixed Income Asset Pricing 1|Convexity]]**: Second-order sensitivity to spread changes.

### 3.2 Top-Level Spread Model

- **Assumptions**:
  - [[Spread Duration and Dvo1|Spread duration]] decisions are made at the [[An Asset Allocation Primer|portfolio]] level.
  - Subsequent sector allocations are relative to the [[An Asset Allocation Primer|portfolio]] [[Spread Duration and Dvo1|spread duration]].

#### 3.2.1 Key Formulas
- **[[Lecture 2- [[Lecture 2- Asset Allocation with Multiple Risky Assets|Asset Allocation]] with [[Lecture 2- Asset Allocation with Multiple Risky Assets|Multiple Risky Assets]]|[[Lecture 2- Asset Allocation with Multiple Risky Assets|asset allocation]]]]**:
 $\text{Asset Allocation} = -OASD^{P} \cdot \sum_{s} \left(\frac{w_{s}^{P} OASD_{s}^{P}}{OASD^{P}} - \frac{w_{s}^{B} OASD_{s}^{B}}{OASD^{B}}\right) \cdot \left(\Delta OAS_{s}^{B} - \Delta OAS^{B}\right)$$
- **Security Selection**:
 $\text{Security Selection} = -\sum_{s} w_{s}^{P} OASD_{s}^{P} \cdot \left(\Delta OAS_{s}^{P} - \Delta OAS_{s}^{B}\right)$$
- **[[Spread Duration and Dvo1|Spread Duration]] Mismatch**:
 $\text{Spread Duration Mismatch} = -(OASD^{P} - OASD^{B}) \cdot \Delta OAS^{B}$$

#### 3.2.2 Example
- **[[Spread Duration and Dvo1|Spread Duration]] Mismatch**:
  - [[An Asset Allocation Primer|Portfolio]] [[Spread Duration and Dvo1|spread duration]]: **4.7 years**.
  - Benchmark [[Spread Duration and Dvo1|spread duration]]: **4.5 years**.
  - Benchmark [[Profit and Loss Attribution with an OAS|spread change]]: **+8.3 bp**.
  - Contribution:
	$$+0.2 \cdot (-8.3) = -1.7 \,    \text{bp}$$

### 3.3 Sector-Level Spread Model

- **Assumptions**:
  - [[Spread Duration and Dvo1|Spread duration]] decisions are made independently for each sector.
  - Absolute allocation weights are used,  and the hurdle rate is set to zero.

#### 3.3.1 Key Formulas
- **[[Lecture 2- [[Lecture 2- Asset Allocation with Multiple Risky Assets|Asset Allocation]] with [[Lecture 2- Asset Allocation with Multiple Risky Assets|Multiple Risky Assets]]|[[Lecture 2- Asset Allocation with Multiple Risky Assets|asset allocation]]]]**:
 $\text{Asset Allocation} = -\sum_{s} \left(w_{s}^{P} OASD_{s}^{P} - w_{s}^{B} OASD_{s}^{B}\right) \cdot \Delta OAS_{s}^{B}$$
- **Security Selection**:
 $\text{Security Selection} = -\sum_{s} w_{s}^{P} OASD_{s}^{P} \cdot \left(\Delta OAS_{s}^{P} - \Delta OAS_{s}^{B}\right)$$

#### 3.3.2 Example
- **Securitized Sector**:
  - [[Spread Duration and Dvo1|Spread duration]] underweight: **-0.3 years**.
  - Benchmark [[Profit and Loss Attribution with an OAS|spread change]]: **+15.9 bp**.
  - Contribution:
	$$-0.3 \cdot (-15.9) = +4.8 \,    \text{bp}$$

### 3.4 Comparison of Models

| **Component** | **Top-Level Model (bp)** | **Sector-Level Model (bp)** |

| **[[Lecture 2- Asset Allocation with Multiple Risky Assets|Asset Allocation]]** | **+5.0** | **+3.2** |

| **Security Selection** | **+9.3** | **+9.3** |

| **[[Spread Duration and Dvo1|Spread Duration]] Mismatch** | **-1.8** | N/A |

## 4. Mortgage Factors

### 4.1 Prepayment Surprise

- **Definition**: Measures the difference between actual and model-predicted [[Mortgage Pools|prepayment rates]].
- **Example**:
  - Predicted prepayment rate: **25% CPR**.
  - Actual prepayment rate: **15% CPR**.
  - Contribution: **+5.2 bp**.

### 4.2 Mortgage Spread Change

- **Definition**: Measures the impact of changes in the difference between model-implied and market-observed mortgage rates.
- **Formula**:
 $\text{Mortgage Spread Change Return} = \text{MtgRtDur} \cdot \Delta \text{MtgSpread}$$

### 4.3 Other Mortgage Factors

- **Definition**: Captures [[Assets|returns]] from factors not explicitly modeled,  such as home price appreciation projections and swap spreads.
- **Example**:
  - Residual contribution: **+1.4 bp**.

### 4.4 Example: Securitized Sector Attribution (Exhibit 71-14)

| **Component** | **Spread Carry (bp)** | **[[Profit and Loss Attribution with an OAS|Spread Change]] (bp)** | **Prepayments (bp)** | **Mortgage Spread (bp)** | **Residual (bp)** | **Total (bp)** |

| **Securitized** | **+0.3** | **+3.7** | **-1.2** | **-7.0** | **+1.4** | **-2.7** |

## 5. Summary and Key Takeaways

### 5.1 Implied Volatility Attribution
- Parallel shifts contributed **+6.2 bp**,  while surface reshaping and volatility decay detracted **-3.8 bp** and **-0.5 bp**,  respectively.
- Net contribution: **+1.9 bp**.

### 5.2 Spread Attribution
- The top-level model separates [[Spread Duration and Dvo1|spread duration]] mismatch (**-1.8 bp**) from [[Lecture 2- [[Lecture 2- Asset Allocation with Multiple Risky Assets|Asset Allocation]] with [[Lecture 2- Asset Allocation with Multiple Risky Assets|Multiple Risky Assets]]|[[Lecture 2- Asset Allocation with Multiple Risky Assets|asset allocation]]]] (**+5.0 bp**),  while the sector-level model combines these terms into [[Lecture 2- [[Lecture 2- Asset Allocation with Multiple Risky Assets|Asset Allocation]] with [[Lecture 2- Asset Allocation with Multiple Risky Assets|Multiple Risky Assets]]|[[Lecture 2- Asset Allocation with Multiple Risky Assets|asset allocation]]]] (**+3.2 bp**).

### 5.3 Mortgage Factors
- Prepayment surprises and mortgage spread changes are significant drivers of performance in the securitized sector.
- Residuals indicate areas where additional analytics may be required.

By mastering these advanced attribution techniques,  [[Lecture Notes Bonds,  Preferred Stock,  and Structured Products|fixed income]] [[An Asset Allocation Primer|portfolio]] managers can optimize risk-adjusted [[Assets|returns]] and enhance their understanding of performance drivers.

# Lecture Notes: Advanced Attribution for Inflation-Linked Securities and Model Selection

## 1. Introduction to Inflation-Linked Securities Attribution

- [[War Economies and Hyperinflation|Inflation]]-linked securities,  such as U.S. Treasury [[War Economies and Hyperinflation|Inflation]]-Protected Securities (TIPS),  require specialized attribution models to account for their unique return components.
- This lecture focuses on:
  - The decomposition of [[Assets|returns]] for [[War Economies and Hyperinflation|inflation]]-linked securities into nominal [[Duration Gap Management|interest rate exposure]],  [[War Economies and Hyperinflation|inflation]]-related components,  and residuals.
  - The importance of [[War Economies and Hyperinflation|inflation]] spread,  [[War Economies and Hyperinflation|inflation]] accretion,  and [[War Economies and Hyperinflation|inflation]] surprise in explaining [[Assets|returns]].
  - A comparison of attribution models for fixed-income portfolios,  highlighting the Fully Analytical model.

## 2. Return Decomposition for Inflation-Linked Securities

### 2.1 Key Components of Inflation-Linked Returns

1. **Nominal [[Duration Gap Management|Interest Rate Exposure]]**:
   - **Yield-Curve Carry**: Return from rolling down the nominal yield curve.
   - **Yield-Curve Change**: Return from changes in [[Real and Nominal Interest Rates and Term Struc|nominal interest rates]].

1. **[[War Economies and Hyperinflation|Inflation]]-Related Components**:
   - **[[War Economies and Hyperinflation|Inflation]] Accretion**: Return from realized [[War Economies and Hyperinflation|inflation]],  reflecting the adjustment of principal or [[Realized Returns|coupon payments]].
   - **[[War Economies and Hyperinflation|Inflation]] Spread Carry**: Return from the difference between nominal rates and [[War Economies and Hyperinflation|inflation]] [[FORWARD RATES AND TERM STRUCTURE|expectations]].
   - **[[War Economies and Hyperinflation|Inflation]] Surprise**: Return from differences between realized and projected [[War Economies and Hyperinflation|inflation]].
   - **[[War Economies and Hyperinflation|Inflation]] [[Profit and Loss Attribution with an OAS|Spread Change]]**: Return from changes in [[War Economies and Hyperinflation|inflation]] [[FORWARD RATES AND TERM STRUCTURE|expectations]].

1. **Residual**:
   - Captures unexplained differences between actual and modeled [[Assets|returns]].

### 2.2 Example: Barclays Inflation-Linked U.S. TIPS Index (July 16,  2010 – August 13,  2010)

- **Total Return**: +169.9 bp.
- **Nominal [[Duration Gap Management|Interest Rate Exposure]]**:
  - Yield-Curve Carry: +27.7 bp.
  - Yield-Curve Change: +184.6 bp.
- **[[War Economies and Hyperinflation|Inflation]]-Related Components**:
  - [[War Economies and Hyperinflation|Inflation]] Accretion: -3.0 bp.
  - [[War Economies and Hyperinflation|Inflation]] Spread Carry: -13.1 bp.
  - [[War Economies and Hyperinflation|Inflation]] Surprise: +5.3 bp.
  - [[War Economies and Hyperinflation|Inflation]] [[Profit and Loss Attribution with an OAS|Spread Change]]: -29.7 bp.
- **Residual**: -1.9 bp.

#### Observations
1. **Nominal [[Duration Gap Management|Interest Rate Exposure]]**:
   - The majority of the return came from nominal [[Duration Gap Management|interest rate exposure]],  with yield-curve change contributing +184.6 bp.
1. **[[War Economies and Hyperinflation|Inflation]]-Related Components**:
   - [[War Economies and Hyperinflation|Inflation]]-related [[Assets|returns]] were negative overall (-40.6 bp),  driven by falling [[War Economies and Hyperinflation|inflation]] [[FORWARD RATES AND TERM STRUCTURE|expectations]] (-29.7 bp).
   - [[War Economies and Hyperinflation|Inflation]] accretion (-3.0 bp) reflected [[Forward Rate|market expectations]] of slight deflation at the beginning of the month.
   - [[War Economies and Hyperinflation|Inflation]] surprise (+5.3 bp) indicated that realized [[War Economies and Hyperinflation|inflation]] was slightly positive,  contrary to [[FORWARD RATES AND TERM STRUCTURE|expectations]].

### 2.3 Inflation Spread and Term Structure

- [[War Economies and Hyperinflation|Inflation]] [[FORWARD RATES AND TERM STRUCTURE|expectations]] did not fall uniformly across maturities:
  - **Short Bonds**: Positive [[War Economies and Hyperinflation|inflation]] spread return,  indicating rising short-term [[War Economies and Hyperinflation|inflation]] [[FORWARD RATES AND TERM STRUCTURE|expectations]].
  - **Long Bonds (30-Year)**: Positive [[War Economies and Hyperinflation|inflation]] spread return,  indicating rising long-term [[War Economies and Hyperinflation|inflation]] [[FORWARD RATES AND TERM STRUCTURE|expectations]].
  - **Intermediate Bonds (3.5–20 Years)**: Negative [[War Economies and Hyperinflation|inflation]] spread return,  indicating falling [[War Economies and Hyperinflation|inflation]] [[FORWARD RATES AND TERM STRUCTURE|expectations]].

#### Implications
- [[War Economies and Hyperinflation|Inflation]] [[An Asset Allocation Primer|portfolio]] managers must carefully monitor the [[The Vasicek Model|term structure]] of [[War Economies and Hyperinflation|inflation]] [[FORWARD RATES AND TERM STRUCTURE|expectations]] and use detailed analytics to manage partial sensitivities to [[War Economies and Hyperinflation|inflation]].

## 3. Security-Level Return Splits for Inflation-Linked Securities

### 3.1 Example: Security-Level Attribution (Exhibit 71-15)

| **Bucket/Issue** | **Maturity** | **Yield-Curve Carry (bp)** | **Yield-Curve Change (bp)** | **[[War Economies and Hyperinflation|Inflation]] Accretion (bp)** | **[[War Economies and Hyperinflation|Inflation]] Spread Carry (bp)** | **[[War Economies and Hyperinflation|Inflation]] Surprise (bp)** | **[[War Economies and Hyperinflation|Inflation]] [[Profit and Loss Attribution with an OAS|Spread Change]] (bp)** | **Residual (bp)** | **Total Return (bp)** |

| **Total** | | 27.7 | 184.6 | -3.0 | -13.1 | 5.3 | -29.7 | -1.9 | 169.9 |

| **912828GN** | 4/15/2012 | 7.1 | 8.9 | -3.0 | -6.1 | 5.2 | 31.5 | -0.6 | 43.0 |

| **912828CP** | 7/15/2014 | 19.0 | 77.3 | -3.0 | -9.6 | 5.2 | -0.2 | 2.8 | 91.5 |

| **912810FR** | 1/15/2025 | 39.9 | 337.0 | -3.0 | -17.4 | 5.4 | -66.1 | -8.1 | 287.7 |

#### Observations
1. **Short-Term Bonds (e.g.,  912828GN)**:
   - Positive [[War Economies and Hyperinflation|inflation]] [[Profit and Loss Attribution with an OAS|spread change]] (+31.5 bp) contributed significantly to total return (+43.0 bp).
1. **Intermediate Bonds (e.g.,  912828CP)**:
   - [[War Economies and Hyperinflation|Inflation]] [[Profit and Loss Attribution with an OAS|spread change]] (-0.2 bp) was negligible,  with most of the return driven by yield-curve change (+77.3 bp).
1. **Long-Term Bonds (e.g.,  912810FR)**:
   - Negative [[War Economies and Hyperinflation|inflation]] [[Profit and Loss Attribution with an OAS|spread change]] (-66.1 bp) detracted significantly from total return (+287.7 bp).

## 4. Selecting an Appropriate Attribution Model

### 4.1 Comparison of Attribution Models (Exhibit 71-16)

| **Component** | **Total Return (bp)** | **Excess of Yield-Curve (bp)** | **Excess of Yield-Curve and Vol (bp)** | **Fully Analytical (Sector-Level,  bp)** | **Fully Analytical (Top-Level,  bp)** |

| **Total** | 32.1 | 32.1 | 32.1 | 32.1 | 32.1 |

| **Yield-Curves** | | 24.6 | 24.6 | 24.6 | 24.6 |

| **[[A Real-Life Option Pricing Exercise|Implied Volatility]]**| | | 1.9 | 1.9 | 1.9 |

| **[[Spread Duration and Dvo1|Spread Duration]] Mismatch** | | | | | -1.8 |

| **[[Lecture 2- Asset Allocation with Multiple Risky Assets|Asset Allocation]]** | 2.9 | -2.2 | -4.0 | 3.2 | 5.0 |

| **Security Selection**| 29.2 | 9.7 | 9.6 | 9.3 | 9.3 |

| **Mortgage** | | | | -8.2 | -8.2 |

| **Residual** | | | | 1.3 | 1.3 |

#### Observations
1. **Yield-Curve Contribution**:
   - Yield-curve exposure contributed +24.6 bp across all models.
1. **[[A Real-Life Option Pricing Exercise|Implied Volatility]] Contribution**:
   - Adding [[A Real-Life Option Pricing Exercise|implied volatility]] as a common factor contributed an additional +1.9 bp.
1. **[[Lecture 2- [[Lecture 2- Asset Allocation with Multiple Risky Assets|Asset Allocation]] with [[Lecture 2- Asset Allocation with Multiple Risky Assets|Multiple Risky Assets]]|[[Lecture 2- Asset Allocation with Multiple Risky Assets|asset allocation]]]]**:
   - [[Lecture 2- [[Lecture 2- Asset Allocation with Multiple Risky Assets|Asset Allocation]] with [[Lecture 2- Asset Allocation with Multiple Risky Assets|Multiple Risky Assets]]|[[Lecture 2- Asset Allocation with Multiple Risky Assets|asset allocation]]]] contributions varied significantly across models,  ranging from -4.0 bp to +5.0 bp.
1. **Security Selection**:
   - Security selection contributed consistently across models,  with a range of +9.3 bp to +9.7 bp.

### 4.2 Fully Analytical Model

- The Fully Analytical model provides the most detailed breakdown of [[Assets|returns]],  incorporating:
  - Sector-level allocation of spread exposure.
  - Mortgage-specific factors (e.g.,  prepayment surprises).
  - Residuals to capture unexplained [[Assets|returns]].

## 5. Implications for Portfolio Management

### 5.1 Inflation-Linked Securities
- **Key Takeaways**:
  - [[War Economies and Hyperinflation|Inflation]] spread changes and [[War Economies and Hyperinflation|inflation]] surprises are critical drivers of [[Assets|returns]] for [[War Economies and Hyperinflation|inflation]]-linked securities.
  - Managers should monitor the [[The Vasicek Model|term structure]] of [[War Economies and Hyperinflation|inflation]] [[FORWARD RATES AND TERM STRUCTURE|expectations]] and use detailed analytics to manage partial sensitivities.

### 5.2 Model Selection
- **Key Takeaways**:
  - The choice of attribution model should align with the [[An Asset Allocation Primer|portfolio]]'s decision structure.
  - The Fully Analytical model is ideal for portfolios with complex exposures,  such as [[War Economies and Hyperinflation|inflation]]-linked securities and [[Fremont Financial Corp. (b)|mortgage-backed securities]].

### 5.3 Practical Recommendations
- Use sector-level attribution to identify underperforming subsectors and refine allocation decisions.
- Incorporate [[A Real-Life Option Pricing Exercise|implied volatility]] and [[War Economies and Hyperinflation|inflation]]-related components into attribution models to capture their contributions to performance.

## 6. Summary and Key Takeaways

### 6.1 Inflation-Linked Securities
- [[War Economies and Hyperinflation|Inflation]]-linked securities require specialized attribution models to account for nominal [[Duration Gap Management|interest rate exposure]],  [[War Economies and Hyperinflation|inflation]]-related components,  and residuals.
- [[War Economies and Hyperinflation|Inflation]] spread changes and [[War Economies and Hyperinflation|inflation]] surprises are critical drivers of [[Assets|returns]].

### 6.2 Attribution Models
- The Fully Analytical model provides the most detailed breakdown of [[Assets|returns]],  making it suitable for portfolios with complex exposures.
- Model selection should align with the [[An Asset Allocation Primer|portfolio]]'s decision structure and management objectives.

By adopting advanced attribution techniques,  [[An Asset Allocation Primer|portfolio]] managers can optimize risk-adjusted [[Assets|returns]],  enhance decision-making,  and achieve superior performance outcomes.

# Lecture Notes: Advanced Topics in Performance Attribution for Fixed Income Portfolios

## 1. Introduction to Advanced Performance Attribution

- Performance attribution in [[Lecture Notes Bonds,  Preferred Stock,  and Structured Products|fixed income]] portfolios involves decomposing [[Assets|returns]] into contributions from various factors,  such as yield-curve movements,  [[A Real-Life Option Pricing Exercise|implied volatility]],  spreads,  [[War Economies and Hyperinflation|inflation]],  and foreign exchange (FX) exposures.
- This lecture focuses on:
  - **Multicurrency Attribution**: Decomposing global [[An Asset Allocation Primer|portfolio]] [[Assets|returns]] into FX allocation,  [[Fx Hedging of Fixed Income - What Is the|FX hedging]],  and local market contributions.
  - **[[Fx Hedging of Fixed Income - What Is the|FX Hedging]] Effects**: Accounting for unintended exposures to local [[Interest Rate Quotations|interest rates]] and cash balances.
  - **Local Market Allocation**: Separating global [[Key Rates O1s Durations and Hedging|duration]] positioning from local curve advantages and excess [[Assets|returns]].
  - **Curve Allocation to Local Markets**: Using curve-matching portfolios (CMPs) to analyze global interest rate positioning.

## 2. Multicurrency Attribution

### 2.1 FX Return Splitting

- **Base [[Forwards and Futures Notes|Currency]] Total Return**:
  The total return of a security denominated in a non-base [[Forwards and Futures Notes|currency]] can be expressed as:
 $ {}^{b}R_{i} = F_{i} + R_{i}F_{i} + R_{i} $$
  Where:
  - \( {}^{b}R_{i} \): Base [[Forwards and Futures Notes|currency]] total return of security \(i\).
  - \( F_{i} \): FX return (change in exchange rate).
  - \( R_{i} \): Local [[Forwards and Futures Notes|currency]] return.
- **Cross-Term**:
  - The cross-term \( R_{i}F_{i} \) represents the interaction between FX and local [[Assets|returns]].
  - While typically small for [[Bond Equivalent Yield (BEY) - Definition, Formula, and Example|fixed income securities]],  it can become significant when FX and local [[Assets|returns]] have opposite signs and similar magnitudes.
- **Adjusted FX Return**:
  To separate FX performance from local management,  include the cash deposit return of each [[Forwards and Futures Notes|currency]]:
 $ {}^{b}R_{i} = \left(F_{i} + R_{i}^{depo}\right) + R_{i}F_{i} + \left(R_{i} - R_{i}^{depo}\right) $$
  Where:
  - \( R_{i}^{depo} \): Local cash deposit return.

### 2.2 FX Hedging

- **Purpose**:
  [[Fx Hedging of Fixed Income - What Is the|FX hedging]] overlays are used to manage FX exposures without affecting local market exposures. Common instruments include [[Financial Instruments PSET Solutions|FX forwards]] and swaps.

#### 2.2.1 Exposure to Local Interest Rates
- [[Fx Hedging of Fixed Income - What Is the|FX hedging]] instruments often have unintended exposure to the short end of local [[__temp__Chapter 10 - The Economics of the Term Structure of Interest Rates|interest rate curves]],  especially during market crises.
- This exposure is considered part of the [[Key Rates O1s Durations and Hedging|hedging]] return and not part of local market strategy decisions.

#### 2.2.2 Cash Balance Effect
- As FX rates fluctuate,  the mark-to-market value of [[Financial Instruments PSET Solutions|FX forwards]] becomes nonzero,  creating a cash balance (positive or negative).
- Unless reinvested regularly,  this cash balance represents an unintended allocation to cash or [[Lecture 6-Leverage, Tail Risk, Volatility Products|leverage]].
- **Solution**:
  - Capture this effect as the difference between the actual [[An Asset Allocation Primer|portfolio]] return and the hypothetical return if the FX hedge cash balance were reinvested daily.

### 2.3 FX Outperformance

- **Pure FX Outperformance**:
 $ {}^{FX}R^{P} - {}^{FX}R^{B} = \sum_{c} {}^{b}h_{c}^{P} \cdot \left(F_{c} + R_{c}^{depo}\right) - \sum_{c} {}^{b}h_{c}^{B} \cdot \left(F_{c} + R_{c}^{depo}\right) $$
  Where:
  - \( {}^{b}h_{c}^{P} \): Effective [[An Asset Allocation Primer|portfolio]] exposure to FX rate \(c\) after [[Key Rates O1s Durations and Hedging|hedging]].
  - \( {}^{b}h_{c}^{B} \): Benchmark exposure to FX rate \(c\).
- **FX Allocation**:
 $ \sum_{c} \left({}^{b}h_{c}^{P} - {}^{b}h_{c}^{B}\right) \cdot \left(F_{c} + R_{c}^{depo} - R_{b}^{depo}\right) $$

- **FX/Local Cross-Term**:
 $ \sum_{c} \left({}^{b}w_{c}^{P}R_{c}^{P} - {}^{b}w_{c}^{B}R_{c}^{B}\right) \cdot F_{c}^{B} + \left(\left({}^{b}w_{c}^{P} - {}^{b}h_{c}^{P}\right) - \left({}^{b}w_{c}^{B} - {}^{b}h_{c}^{B}\right)\right) \cdot R_{c}^{depo} \cdot F_{c}^{B} $$

## 3. Local Market Allocation

### 3.1 Local Market Outperformance

- After accounting for FX exposures and [[Key Rates O1s Durations and Hedging|hedging]],  the remaining outperformance is given by:
 $ {}^{L}R^{P} - {}^{L}R^{B} = \sum_{m} {}^{b}w_{m}^{P} \cdot \left(R_{m}^{P} - R_{m}^{depo,  P}\right) - \sum_{m} {}^{b}w_{m}^{B} \cdot \left(R_{m}^{B} - R_{m}^{depo,  B}\right) $$

- **Local Market Allocation**:
 $ \sum_{m} \left({}^{b}w_{m}^{P} - {}^{b}w_{m}^{B}\right) \cdot \left(\left(R_{m}^{B} - R_{m}^{depo,  B}\right) - \left(R^{B} - R^{depo,  B}\right)\right) $$

- **Local Market Management**:
 $ \sum_{m} {}^{b}w_{m}^{P} \cdot \left(\left(R_{m}^{P} - R_{m}^{depo,  P}\right) - \left(R_{m}^{B} - R_{m}^{depo,  B}\right)\right) $$

### 3.2 Factor-Based Local Market Allocation

- Local market allocation can be decomposed into contributions from [[PSET 6- Financial Instruments|risk factors]] such as yield-curve,  [[A Real-Life Option Pricing Exercise|implied volatility]],  and spreads:
 $ {}^{L}R^{P} - {}^{L}R^{B} = \sum_{k} \sum_{m_{k}} {}^{b}w_{m_{k}}^{P} \alpha_{k,  m_{k}}^{P} f_{k,  m_{k}}^{P} - \sum_{k} \sum_{m_{k}} {}^{b}w_{m_{k}}^{B} \alpha_{k,  m_{k}}^{B} f_{k,  m_{k}}^{B} $$

- **Allocation**:
 $ \sum_{k} \left(\sum_{m_{k}} \left({}^{b}w_{m_{k}}^{P} \alpha_{k,  m_{k}}^{P} - {}^{b}w_{m_{k}}^{B} \alpha_{k,  m_{k}}^{B}\right) \cdot \left(f_{k,  m_{k}}^{B} - f_{k}^{H}\right)\right) $$

- **Management**:
 $ \sum_{k} \left(\sum_{m_{k}} {}^{b}w_{m_{k}}^{P} \alpha_{k,  m_{k}}^{P} \cdot \left(f_{k,  m_{k}}^{P} - f_{k,  m_{k}}^{B}\right)\right) $$

## 4. Curve Allocation to Local Markets

### 4.1 Global Interest Rate Positioning

- Global interest rate positioning can be separated into:
  - **Global [[Week 6 Assignment Review|Duration Mismatch]]**: Contribution of the [[An Asset Allocation Primer|portfolio]]'s overall [[Key Rates O1s Durations and Hedging|duration]] position.
  - **Local Curve Advantage**: Contribution of [[Duration Gap Management|interest rate exposure]] outside the reference [[Forwards and Futures Notes|currency]].
  - **Excess of Curve Allocation**: Contribution of other risk exposures in each [[Forwards and Futures Notes|currency]].

### 4.2 Curve Carry Attribution

- **Curve Carry Return**:
 $ R_{c,  j}^{carry} = y_{c,  j} \Delta t $$
  Where:
  - \( y_{c,  j} \): Yield at key-rate point \(j\) on curve \(c\).
  - \( \Delta t \): Time elapsed.
- **Local Curve Carry Allocation**:
 $ \sum_{c} \sum_{j} \left({}^{b}w_{c}^{P} \omega_{c,  j}^{P} - {}^{b}w_{c}^{B} \omega_{c,  j}^{B}\right) \cdot \left(\left(R_{c,  j}^{carry} - R_{c}^{depo}\right) - \left(R_{ref,  j}^{carry} - R_{ref}^{depo}\right)\right) $$

## 5. Practical Implications for Portfolio Management

### 5.1 FX Management
- **Key Takeaways**:
  - [[Fx Hedging of Fixed Income - What Is the|FX hedging]] introduces unintended exposures to local [[Interest Rate Quotations|interest rates]] and cash balances,  which must be accounted for in attribution.
  - Explicitly separating FX and local [[Assets|returns]] provides a clearer view of [[An Asset Allocation Primer|portfolio]] performance.

### 5.2 Local Market Allocation
- **Key Takeaways**:
  - Factor-based allocation provides a more granular view of local market exposures,  enabling better [[Financial Mathematics Course|risk management]].
  - Decomposing local [[Assets|returns]] into allocation,  management,  and [[Lecture 6-Leverage, Tail Risk, Volatility Products|leverage]] components helps identify sources of outperformance.

### 5.3 Curve Allocation
- **Key Takeaways**:
  - Using curve-matching portfolios (CMPs) simplifies the analysis of global interest rate positioning.
  - Separating global [[Week 6 Assignment Review|duration mismatch]] from local curve advantages provides insights into the effectiveness of interest rate strategies.

## 6. Summary and Key Takeaways

### 6.1 Multicurrency Attribution
- Multicurrency portfolios require separating FX [[Assets|returns]],  [[Fx Hedging of Fixed Income - What Is the|FX hedging]] effects,  and local market contributions.
- FX/local cross-terms,  while typically small,  can accumulate over time and significantly impact total [[Assets|returns]].

### 6.2 Local Market Allocation
- Local market outperformance can be decomposed into allocation,  management,  and [[Lecture 6-Leverage, Tail Risk, Volatility Products|leverage]] components.
- Factor-based allocation provides a detailed view of exposures to yield-curve,  volatility,  and spread risks.

### 6.3 Curve Allocation
- Curve carry and curve change [[Assets|returns]] are critical drivers of [[Lecture Notes Bonds,  Preferred Stock,  and Structured Products|fixed income]] performance.
- Using CMPs simplifies the analysis of curve carry and provides consistent attribution results.

By mastering these advanced attribution techniques,  [[An Asset Allocation Primer|portfolio]] managers can optimize risk-adjusted [[Assets|returns]],  enhance decision-making,  and achieve superior performance outcomes.

### Lecture Notes: Advanced Attribution for Global Yield-Curve Allocation and FX Positioning

## 1. Introduction to Global Yield-Curve Allocation and FX Positioning

- Global fixed-income portfolios often involve exposure to multiple currencies and yield curves. Proper attribution of performance requires decomposing [[Assets|returns]] into contributions from FX positioning,  yield-curve carry,  and yield-curve changes.
- This lecture focuses on:
  - **Global Curve Carry and Change Attribution**: Breaking down outperformance into carry and yield-curve change components.
  - **FX Allocation and [[Key Rates O1s Durations and Hedging|Hedging]]**: Understanding the impact of FX positioning and [[Key Rates O1s Durations and Hedging|hedging]] on [[An Asset Allocation Primer|portfolio]] [[Assets|returns]].
  - **Practical Example**: Analyzing the performance of a U.S. dollar-denominated [[An Asset Allocation Primer|portfolio]] managed against the Barclays Global G4 Treasury Index.

## 2. Global Curve Carry Attribution

### 2.1 Curve Carry Management

- **Key Insight**: Curve carry management is zero by construction because the carry return at each key-rate point and the deposit rate return are uniform across all securities in the [[An Asset Allocation Primer|portfolio]] and benchmark.
- **Formula**:
 $\sum_{c}\sum_{j}^{b}w_{c}^{P}\omega_{c,  j}^{P}\cdot\left(\left(R_{c,  j}^{carry}-R_{c}^{depo}\right)-\left(R_{c,  j}^{carry}-R_{c}^{depo}\right)\right)=0$$

### 2.2 Global Curve Carry Over Deposit

- **Definition**: Measures the outperformance due to differences in [[An Asset Allocation Primer|portfolio]] and benchmark weights across curves and key-rate points.
- **Formula**:
 $\sum_{c}\sum_{j}\Big(^{b}w_{c}^{P}\omega_{c,  j}^{P}-^{b}w_{c}^{B}\omega_{c,  j}^{B}\Big)\cdot\Big(R_{ref,  j}^{carry}-R_{ref}^{depo}\Big)$$
- **Key Insight**: If no reference curve is used,  the global curve carry term becomes zero,  and the outperformance is broken down per curve and key-rate point:
 $\sum_{c}\sum_{j}\Big(^{b}w_{c}^{P}\omega_{c,  j}^{P}-^{b}w_{c}^{B}\omega_{c,  j}^{B}\Big)\cdot\Big(R_{c,  j}^{carry}-R_{c}^{depo}\Big)$$

### 2.3 Example: Euro Curve Carry Attribution

- **Average Yield**: 3.1%.
- **Carry Over Deposit Return**: 23.4 bp.
- **Market Value Overweight**: \(34.4\% - 29.8\% = 4.6\%\).
- **Contribution**:
 $(34.4\% - 29.8\%) \times 23.4 \,  \text{bp} = +1.1 \,  \text{bp}$$

## 3. Global Curve Change Attribution

### 3.1 Curve Change Management

- **Key Insight**: Curve change management is zero by construction because [[How Countries Go Broke-Chapter 12 to Chapter 14|interest rate changes]] are uniform across all securities in the [[An Asset Allocation Primer|portfolio]] and benchmark.
- **Formula**:
 $-\sum_{c}\sum_{j}^{b}w_{c}^{P}KRD_{c,  j}^{P}\cdot\left(\Delta y_{c,  j}-\Delta y_{c,  j}\right)=0$$

### 3.2 Global Duration Mismatch

- **Definition**: Measures the outperformance due to differences in [[An Asset Allocation Primer|portfolio]] and benchmark key-rate durations relative to a reference curve.
- **Formula**:
 $-\sum_{c}\sum_{j}\Big(^{b}w_{c}^{P}KRD_{c,  j}^{P}-^{b}w_{c}^{B}KRD_{c,  j}^{B}\Big)\cdot\Delta y_{ref,  j}$$
- **Key Insight**: If no reference curve is used,  the global [[Week 6 Assignment Review|duration mismatch]] becomes zero,  and the outperformance is broken down per curve and key-rate point:
 $-\sum_{c}\sum_{j}\Big(^{b}w_{c}^{P}KRD_{c,  j}^{P}-^{b}w_{c}^{B}KRD_{c,  j}^{B}\Big)\cdot\Delta y_{c,  j}$$

### 3.3 Example: Euro Curve Change Attribution

- **[[Key Rates O1s Durations and Hedging|Duration]] Overweight**: \(2.33 - 1.88 = 0.45\).
- **Average Yield Change**: -28 bp.
- **Contribution**:
 $(2.33 - 1.88) \times (-28 \,  \text{bp}) = -12.6 \,  \text{bp}$$

## 4. FX Allocation and Hedging

### 4.1 FX Allocation Outperformance

- **Definition**: Measures the outperformance due to deviations in [[An Asset Allocation Primer|portfolio]] and benchmark FX exposures.
- **Formula**:
 $\sum_{c} \left({}^{b}h_{c}^{P} - {}^{b}h_{c}^{B}\right) \cdot \left(F_{c} + R_{c}^{depo} - R_{b}^{depo}\right)$$

### 4.2 FX Hedging Effects

- **Definition**: Measures the impact of [[Fx Hedging of Fixed Income - What Is the|FX hedging]] instruments on [[An Asset Allocation Primer|portfolio]] [[Assets|returns]],  including exposure to local [[Interest Rate Quotations|interest rates]] and cash balance effects.
- **Key Insight**: [[Fx Hedging of Fixed Income - What Is the|FX hedging]] effects are captured as the difference between the actual [[An Asset Allocation Primer|portfolio]] return and the hypothetical return if the FX hedge cash balance were reinvested daily.

### 4.3 Example: Euro FX Allocation Outperformance

- **Excess FX Return**: 306.1 bp.
- **Market Value Overweight**: \(34.4\% - 29.8\% = 4.6\%\).
- **Contribution**:
 $(34.4\% - 29.8\%) \times 306.1 \,  \text{bp} = +14.1 \,  \text{bp}$$
- **Reported Contribution**: +14.8 bp (difference due to daily compounding).

## 5. Practical Example: Portfolio vs. Barclays Global G4 Treasury Index

### 5.1 Portfolio Characteristics (Exhibit 72-1)

| **[[Forwards and Futures Notes|Currency]]** | **[[An Asset Allocation Primer|Portfolio]] Weight (%)** | **Benchmark Weight (%)** | **Net Weight (%)** | **[[An Asset Allocation Primer|Portfolio]] OAD** | **Benchmark OAD** | **Net OAD** |

| **Total** | 100.0 | 100.0 | 0.0 | 6.46 | 6.47 | -0.01 |

| **U.S. Dollar** | 24.1 | 28.6 | -4.5 | 1.05 | 1.50 | -0.45 |

| **Euro** | 34.4 | 29.8 | 4.6 | 2.33 | 1.88 | 0.45 |

| **Japanese Yen** | 34.5 | 34.5 | 0.0 | 2.45 | 2.46 | -0.01 |

| **British Pound** | 7.0 | 7.1 | -0.1 | 0.63 | 0.63 | 0.00 |

### 5.2 Total Outperformance Breakdown (Exhibit 72-2)

| **Component** | **Total (bp)** | **U.S. Dollar (bp)** | **Euro (bp)** | **Japanese Yen (bp)** | **British Pound (bp)** |

| **Outperformance** | 10.5 | 15.5 | -5.1 | 0.5 | -0.4 |

| **FX Allocation & [[Key Rates O1s Durations and Hedging|Hedging]]** | 14.3 | 0.0 | 14.4 | 0.0 | -0.1 |

| **Local Market Allocation** | 6.5 | 16.5 | -9.7 | -0.3 | 0.0 |

| **Local Yield-Curves** | 3.1 | 14.9 | -12.0 | 0.2 | 0.0 |

| **Local Management** | -10.3 | -1.0 | -9.8 | 0.8 | -0.3 |

### 5.3 Global Yield-Curve Allocation Outperformance (Exhibit 72-4)

| **[[Forwards and Futures Notes|Currency]]** | **Carry (bp)** | **Change (bp)** | **Total (bp)** |

| **U.S. Dollar** | -1.4 | 16.3 | 14.9 |

| **Euro** | 1.1 | -13.1 | -12.0 |

| **Japanese Yen** | 0.2 | 0.0 | 0.2 |

| **British Pound** | 0.0 | 0.0 | 0.0 |

| **Total** | -0.1 | 3.2 | 3.1 |

## 6. Summary and Key Takeaways

### 6.1 Global Yield-Curve Allocation
- Curve carry management is zero by construction,  while global curve carry and change contributions depend on [[An Asset Allocation Primer|portfolio]] and benchmark deviations.
- [[Key Rates O1s Durations and Hedging|Duration]] positioning in the U.S. dollar and euro markets drove most of the yield-curve outperformance.

### 6.2 FX Allocation and Hedging
- FX allocation contributed significantly to outperformance,  particularly from the euro's strengthening against the U.S. dollar.
- [[Fx Hedging of Fixed Income - What Is the|FX hedging]] effects were minimal,  reflecting effective implementation of the manager's strategy.

### 6.3 Practical Applications
- Advanced attribution techniques provide deeper insights into [[An Asset Allocation Primer|portfolio]] performance,  enabling managers to optimize risk-adjusted [[Assets|returns]] and refine [[An Asset Allocation Primer|investment]] strategies.

By mastering these concepts,  fixed-income [[An Asset Allocation Primer|portfolio]] managers can enhance their decision-making processes and achieve superior performance outcomes.

given by:
$$\sum_{s}\left(\beta^{P}w_{s}^{P}-\beta^{B}w_{s}^{B}\right)\cdot R_{s}^{B}$$

And the sector management term becomes:
$$\sum_{s}\beta^{P}w_{s}^{P}\cdot\left(R_{s}^{P}-R_{s}^{B}\right)$$

This approach shifts the responsibility for [[Lecture 6-Leverage, Tail Risk, Volatility Products|leverage]] decisions to the asset allocator,  who determines the total exposure to each sector. The sector managers are then evaluated based on their ability to generate excess [[Assets|returns]] relative to the benchmark within their allocated exposure.

## 7. Practical Implications for Portfolio Management

### 7.1 Handling Leverage in Attribution Models

- **Key Takeaways**:
  - [[Lecture 6-Leverage, Tail Risk, Volatility Products|Leverage]] introduces additional complexity into performance attribution,  as it affects both the weights and [[Assets|returns]] of [[An Asset Allocation Primer|portfolio]] components.
  - Properly accounting for [[Lecture 6-Leverage, Tail Risk, Volatility Products|leverage]] ensures that the contributions of [[Lecture 2- [[Lecture 2- Asset Allocation with Multiple Risky Assets|Asset Allocation]] with [[Lecture 2- Asset Allocation with Multiple Risky Assets|Multiple Risky Assets]]|[[Lecture 2- Asset Allocation with Multiple Risky Assets|asset allocation]]]] and sector management are accurately measured.
  - The choice of whether to embed [[Lecture 6-Leverage, Tail Risk, Volatility Products|leverage]] decisions in the [[Lecture 2- [[Lecture 2- Asset Allocation with Multiple Risky Assets|Asset Allocation]] with [[Lecture 2- Asset Allocation with Multiple Risky Assets|Multiple Risky Assets]]|[[Lecture 2- Asset Allocation with Multiple Risky Assets|asset allocation]]]] or sector management term depends on the [[An Asset Allocation Primer|portfolio]]'s decision-making structure.

### 7.2 Managing Derivative Exposures

- **Key Takeaways**:
  - [[Chapter 9 Arbitrage and Hedging With Options|Derivatives]] can significantly alter the [[Risk Management Lessons From Long Term Capital Management|leverage and risk]] profile of a [[An Asset Allocation Primer|portfolio]],  even when their market value is small or zero.
  - Attribution models must account for the implicit [[Lecture 6-Leverage, Tail Risk, Volatility Products|leverage]] introduced by [[Chapter 9 Arbitrage and Hedging With Options|derivatives]] to avoid misattributing performance.
  - Reporting [[Lecture 6-Leverage, Tail Risk, Volatility Products|leverage]] as a separate line item provides transparency and helps identify the sources of outperformance or underperformance.

### 7.3 Aligning Attribution with Decision-Making

- **Key Takeaways**:
  - Attribution models should align with the [[An Asset Allocation Primer|portfolio]]'s decision-making structure,  whether [[Lecture 6-Leverage, Tail Risk, Volatility Products|leverage]] decisions are made at the [[Lecture 2- [[Lecture 2- Asset Allocation with Multiple Risky Assets|Asset Allocation]] with [[Lecture 2- Asset Allocation with Multiple Risky Assets|Multiple Risky Assets]]|[[Lecture 2- Asset Allocation with Multiple Risky Assets|asset allocation]]]] or sector management level.
  - Clear separation of responsibilities between asset allocators and sector managers ensures that performance is attributed to the appropriate decision-makers.

## 8. Summary and Key Takeaways

### 8.1 Leverage and Derivatives in Attribution

- [[Lecture 6-Leverage, Tail Risk, Volatility Products|Leverage]] complicates performance attribution by altering the weights and [[Assets|returns]] of [[An Asset Allocation Primer|portfolio]] components.
- Properly accounting for [[Lecture 6-Leverage, Tail Risk, Volatility Products|leverage]] ensures that the contributions of [[Lecture 2- [[Lecture 2- Asset Allocation with Multiple Risky Assets|Asset Allocation]] with [[Lecture 2- Asset Allocation with Multiple Risky Assets|Multiple Risky Assets]]|[[Lecture 2- Asset Allocation with Multiple Risky Assets|asset allocation]]]] and sector management are accurately measured.
- [[Chapter 9 Arbitrage and Hedging With Options|Derivatives]] introduce implicit [[Lecture 6-Leverage, Tail Risk, Volatility Products|leverage]],  which must be accounted for in attribution models to avoid misattributing performance.

### 8.2 Practical Recommendations

1. **Report [[Lecture 6-Leverage, Tail Risk, Volatility Products|Leverage]] Separately**:
   - Include [[Lecture 6-Leverage, Tail Risk, Volatility Products|leverage]] as a separate line item in [[Pl Attribution|attribution reports]] to provide transparency and identify its impact on performance.

1. **Align Attribution with Decision-Making**:
   - Ensure that attribution models reflect the [[An Asset Allocation Primer|portfolio]]'s decision-making structure,  whether [[Lecture 6-Leverage, Tail Risk, Volatility Products|leverage]] decisions are made at the [[Lecture 2- [[Lecture 2- Asset Allocation with Multiple Risky Assets|Asset Allocation]] with [[Lecture 2- Asset Allocation with Multiple Risky Assets|Multiple Risky Assets]]|[[Lecture 2- Asset Allocation with Multiple Risky Assets|asset allocation]]]] or sector management level.

1. **Use Appropriate Return Bases**:
   - Define a consistent return basis for [[Chapter 9 Arbitrage and Hedging With Options|derivatives]] to avoid non-intuitive results and ensure meaningful comparisons.

1. **Monitor Derivative Exposures**:
   - Regularly review derivative exposures to understand their impact on [[An Asset Allocation Primer|portfolio]] [[Risk Management Lessons From Long Term Capital Management|leverage and risk]].

By adopting these advanced attribution techniques,  [[An Asset Allocation Primer|portfolio]] managers can optimize risk-adjusted [[Assets|returns]],  enhance decision-making,  and achieve superior performance outcomes.

### Lecture Notes: Advanced Performance Attribution in Fixed Income Portfolio Management – Leverage,  Derivatives,  and Multi-Currency Portfolios

## 1. Introduction to Advanced Attribution Techniques

- [[Lecture Notes Bonds,  Preferred Stock,  and Structured Products|Fixed income]] [[The Impact of Option Strategies in Financial  Portfolios Performance|portfolio management]] often involves complex instruments such as [[Chapter 9 Arbitrage and Hedging With Options|derivatives]],  multi-[[Forwards and Futures Notes|currency]] exposures,  and [[Lecture 6-Leverage, Tail Risk, Volatility Products|leverage]]. Proper attribution of performance requires decomposing [[Assets|returns]] into contributions from [[Lecture 2- [[Lecture 2- Asset Allocation with Multiple Risky Assets|Asset Allocation]] with [[Lecture 2- Asset Allocation with Multiple Risky Assets|Multiple Risky Assets]]|[[Lecture 2- Asset Allocation with Multiple Risky Assets|asset allocation]]]],  security selection,  FX positioning,  and derivative overlays.
- This lecture focuses on:
  - **[[Lecture 6-Leverage, Tail Risk, Volatility Products|Leverage]] Attribution**: Handling [[Lecture 6-Leverage, Tail Risk, Volatility Products|leverage]] at both the [[An Asset Allocation Primer|portfolio]] and sector levels.
  - **Derivative Attribution**: Special treatment of [[Forwards and Futures Notes|currency]],  interest rate,  and [[RISK NEUTRAL VALUATION FRAMEWORK FOR CREDIT DEFAULT SWAPS|credit derivatives]].
  - **Multi-[[Forwards and Futures Notes|Currency]] Attribution**: Decomposing global [[An Asset Allocation Primer|portfolio]] [[Assets|returns]] into FX and local market contributions.
  - **Practical Challenges**: Handling intra-period transactions,  unsettled positions,  and missing or inconsistent data.

## 2. Leverage Attribution

### 2.1 Leverage at Portfolio and Sector Levels

- **Key Insight**: [[Lecture 6-Leverage, Tail Risk, Volatility Products|Leverage]] decisions can be made at both the [[An Asset Allocation Primer|portfolio]] and sector levels. Proper attribution requires separating the contributions of top-level [[Lecture 6-Leverage, Tail Risk, Volatility Products|leverage]] from sector-level exposures.

#### 2.1.1 Asset Allocation with Leverage
- **Formula**:
 $\beta^P\sum_s\left(\frac{w_s^P\beta_s^P}{\beta^P}-\frac{w_s^B\beta_s^B}{\beta^B}\right)\cdot\left(R_s^B-R^H\right)$$
  - \( \beta^P \): [[An Asset Allocation Primer|Portfolio]] [[Lecture 6-Leverage, Tail Risk, Volatility Products|leverage]].
  - \( \beta^B \): Benchmark [[Lecture 6-Leverage, Tail Risk, Volatility Products|leverage]].
  - \( w_s^P \): [[An Asset Allocation Primer|Portfolio]] weight in sector \(s\).
  - \( w_s^B \): Benchmark weight in sector \(s\).
  - \( R_s^B \): Benchmark return for sector \(s\).
  - \( R^H \): Hurdle return.

#### 2.1.2 Sector Management with Leverage
- **Formula**:
 $\sum_{s}w_{s}^{P}\beta_{s}^{P}\cdot\left(R_{s}^{P}-R_{s}^{B}\right)$$
  - \( \beta_s^P \): Sector [[Lecture 6-Leverage, Tail Risk, Volatility Products|leverage]] in the [[An Asset Allocation Primer|portfolio]].
  - \( R_s^P \): [[An Asset Allocation Primer|Portfolio]] return for sector \(s\).

#### 2.1.3 Diversification Term
- **Formula**:
 $\left(\sum_{s}w_{s}^{P}\beta_{s}^{P}-\beta^{P}\frac{\sum_{s}w_{s}^{B}\beta_{s}^{B}}{\beta^{B}}\right)\cdot R^{H}$$
  - Captures the effect of non-linear aggregation of [[Lecture 6-Leverage, Tail Risk, Volatility Products|leverage]] across sectors.
  - If [[Lecture 6-Leverage, Tail Risk, Volatility Products|leverage]] aggregates linearly (\( \beta^P = \sum_s w_s^P \beta_s^P \)),  this term vanishes.

### 2.2 Practical Implications of Leverage Attribution

1. **Linear vs. Non-Linear Aggregation**:
   - If [[Lecture 6-Leverage, Tail Risk, Volatility Products|leverage]] aggregates non-linearly (e.g.,  due to risk diversification),  the diversification term becomes significant.
   - Positive [[The Modern Portfolio Theory and the Capm|diversification effects]] occur when the [[An Asset Allocation Primer|portfolio]] benefits from uncorrelated sector exposures.

1. **Hurdle Return**:
   - The hurdle return (\( R^H \)) represents the minimum return required to justify [[Lecture 6-Leverage, Tail Risk, Volatility Products|leverage]]. Positive \( R^H \) amplifies the diversification effect.

1. **Reporting [[Lecture 6-Leverage, Tail Risk, Volatility Products|Leverage]]**:
   - [[Lecture 6-Leverage, Tail Risk, Volatility Products|Leverage]] should be reported separately to provide transparency and identify its impact on performance.

## 3. Derivative Attribution

### 3.1 Currency Derivatives

- **Purpose**: [[Financial Instruments PSET Solutions|FX forwards]] and swaps are typically used for [[Forward Rate|hedging currency risk]].
- **Attribution Treatment**:
  - Remove FX hedges from local market attribution to isolate FX effects.
  - Account for:
	1. **Non-FX Return**: Return from FX hedges unrelated to [[Forwards and Futures Notes|currency]] movements.
	1. **[[Fx Hedging of Fixed Income - What Is the|FX Hedging]] Cash Balance Effect**: Implicit allocation to cash or [[Lecture 6-Leverage, Tail Risk, Volatility Products|leverage]] due to the mark-to-market value of FX hedges.

### 3.2 Interest Rate Derivatives

- **Purpose**: Interest rate [[Chapter 9 Arbitrage and Hedging With Options|derivatives]],  such as government bond [[Futures Not Subject to Cash-And-Carry|futures]] and swaps,  are used to manage yield-curve exposures.
- **Attribution Treatment**:
  - Include [[Chapter 9 Arbitrage and Hedging With Options|derivatives]] in yield-curve attribution but exclude them from [[Lecture 2- [[Lecture 2- Asset Allocation with Multiple Risky Assets|Asset Allocation]] with [[Lecture 2- Asset Allocation with Multiple Risky Assets|Multiple Risky Assets]]|[[Lecture 2- Asset Allocation with Multiple Risky Assets|asset allocation]]]] and security selection.
  - Account for:
	1. **Curve Outperformance**: Contribution to yield-curve [[Assets|returns]].
	1. **Cash Balance Effect**: Implicit allocation to cash or [[Lecture 6-Leverage, Tail Risk, Volatility Products|leverage]] due to the market value of [[Chapter 9 Arbitrage and Hedging With Options|derivatives]].
	1. **Spread Effects**: Changes in the spread between [[Futures Not Subject to Cash-And-Carry|futures]] prices and theoretical fair values.

### 3.3 Credit Derivatives

- **Purpose**: [[RISK NEUTRAL VALUATION FRAMEWORK FOR CREDIT DEFAULT SWAPS|Credit derivatives]],  such as CDS and CDX,  are used to manage credit exposures.
- **Attribution Treatment**:
  - Include [[RISK NEUTRAL VALUATION FRAMEWORK FOR CREDIT DEFAULT SWAPS|credit derivatives]] in [[Lecture 2- [[Lecture 2- Asset Allocation with Multiple Risky Assets|Asset Allocation]] with [[Lecture 2- Asset Allocation with Multiple Risky Assets|Multiple Risky Assets]]|[[Lecture 2- Asset Allocation with Multiple Risky Assets|asset allocation]]]] and security selection.
  - Explode credit indices (e.g.,  CDX) into single-issuer constituents for detailed attribution.
  - Account for:
	1. **[[Cds-Equivalent Bond Spread|Credit Spread]] Changes**: Contribution to excess [[Assets|returns]] over the yield curve.
	1. **Bucket [[Lecture 6-Leverage, Tail Risk, Volatility Products|Leverage]]**: Implicit [[Lecture 6-Leverage, Tail Risk, Volatility Products|leverage]] due to the basis of [[Assets|returns]] for [[RISK NEUTRAL VALUATION FRAMEWORK FOR CREDIT DEFAULT SWAPS|credit derivatives]].

## 4. Multi-Currency Attribution

### 4.1 FX Return Splitting

- **Formula**:
 $ {}^{b}R_{i} = F_{i} + R_{i}F_{i} + R_{i} $$
  - \( {}^{b}R_{i} \): Base [[Forwards and Futures Notes|currency]] total return.
  - \( F_{i} \): FX return.
  - \( R_{i} \): Local [[Forwards and Futures Notes|currency]] return.
  - \( R_{i}F_{i} \): Cross-term.

### 4.2 FX Allocation and Hedging

- **FX Allocation**:
 $ \sum_{c} \left({}^{b}h_{c}^{P} - {}^{b}h_{c}^{B}\right) \cdot \left(F_{c} + R_{c}^{depo} - R_{b}^{depo}\right) $$
  - \( {}^{b}h_{c}^{P} \): [[An Asset Allocation Primer|Portfolio]] FX exposure.
  - \( {}^{b}h_{c}^{B} \): Benchmark FX exposure.
- **[[Fx Hedging of Fixed Income - What Is the|FX Hedging]] Effects**:
  - Account for unintended exposures to local [[Interest Rate Quotations|interest rates]] and cash balances due to FX hedges.

### 4.3 Local Market Allocation

- **Formula**:
 $ {}^{L}R^{P} - {}^{L}R^{B} = \sum_{m} {}^{b}w_{m}^{P} \cdot \left(R_{m}^{P} - R_{m}^{depo,  P}\right) - \sum_{m} {}^{b}w_{m}^{B} \cdot \left(R_{m}^{B} - R_{m}^{depo,  B}\right) $$
  - Decomposes local market outperformance into allocation and management components.

## 5. Practical Challenges in Attribution

### 5.1 Intra-Period Transactions

- **Issue**: Transactions that settle on a forward basis create intra-period [[Assets|returns]] and unsettled positions.
- **Solution**:
  - Report intra-period [[Assets|returns]] separately.
  - Distinguish between settled and unsettled positions,  as only settled positions earn carry.

### 5.2 Unsettled Positions

- **Issue**: Unsettled positions earn cash [[Assets|returns]] instead of security yields.
- **Solution**:
  - Account for the return difference (\( r^{cash} - r^{yield} \)) as carry outperformance.

### 5.3 Missing or Inconsistent Data

- **Issue**: Missing prices or discrepancies between [[An Asset Allocation Primer|portfolio]] and benchmark prices can distort attribution.
- **Solution**:
  - Use implied prices based on market changes to fill gaps.
  - Report [[Arbitrage Pricing of Derivatives|pricing]] differences as a separate source of outperformance.

## 6. Summary and Key Takeaways

### 6.1 Leverage Attribution
- Properly account for [[Lecture 6-Leverage, Tail Risk, Volatility Products|leverage]] at both the [[An Asset Allocation Primer|portfolio]] and sector levels.
- Report [[The Modern Portfolio Theory and the Capm|diversification effects]] separately to capture non-linear aggregation of [[Lecture 6-Leverage, Tail Risk, Volatility Products|leverage]].

### 6.2 Derivative Attribution
- Treat [[Forwards and Futures Notes|currency]] and interest rate [[Chapter 9 Arbitrage and Hedging With Options|derivatives]] as overlays,  excluding them from [[Lecture 2- [[Lecture 2- Asset Allocation with Multiple Risky Assets|Asset Allocation]] with [[Lecture 2- Asset Allocation with Multiple Risky Assets|Multiple Risky Assets]]|[[Lecture 2- Asset Allocation with Multiple Risky Assets|asset allocation]]]] and security selection.
- Include [[RISK NEUTRAL VALUATION FRAMEWORK FOR CREDIT DEFAULT SWAPS|credit derivatives]] in regular attribution models,  exploding indices into single-issuer constituents.

### 6.3 Multi-Currency Attribution
- Decompose global [[Assets|returns]] into FX and local market contributions.
- Account for [[Fx Hedging of Fixed Income - What Is the|FX hedging]] effects,  including unintended exposures to local [[Interest Rate Quotations|interest rates]] and cash balances.

### 6.4 Practical Recommendations
1. **Report [[Lecture 6-Leverage, Tail Risk, Volatility Products|Leverage]] and [[Chapter 9 Arbitrage and Hedging With Options|Derivatives]] Separately**:
   - Provide transparency into their contributions to performance.
1. **Handle Intra-Period Transactions**:
   - Capture intra-period [[Assets|returns]] and unsettled positions accurately.
1. **Address Missing Data**:
   - Use implied prices and report [[Arbitrage Pricing of Derivatives|pricing]] differences separately.

By adopting these advanced attribution techniques,  [[An Asset Allocation Primer|portfolio]] managers can optimize risk-adjusted [[Assets|returns]],  enhance decision-making,  and achieve superior performance outcomes.
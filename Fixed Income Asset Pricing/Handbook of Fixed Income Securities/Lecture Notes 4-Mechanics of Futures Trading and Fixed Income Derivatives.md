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

- [Fixed income derivatives](../../Financial%20Engineering/6.%20A%20Brief%20Introduction%20to%20Stochastic%20Calculus.md),  including [futures](../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%203%20-%20Futures%20Markets/Futures%20Not%20Subject%20to%20Cash-And-Carry.md) and options,  are essential tools for [hedging](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%205/Key%20Rates%20O1s%20Durations%20and%20Hedging.md),  speculation,  and [managing interest rate risk](.md).
- This lecture focuses on the mechanics of [futures trading](../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%203%20-%20Futures%20Markets/Futures%20Mechanics.md),  the types of orders used,  the role of clearing corporations,  [Leverage](Lecture%206-[[Lecture%206-Leverage,%20Tail%20Risk,%20Volatility%20Products), Tail Risk, Volatility Products#6.1.3 [Margin requirements](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%2010/Case%20Study%20Mf%20Globals%20Repo-To-Maturity%20Trades.md)|[margin requirements](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%2010/Case%20Study%20Mf%20Globals%20Repo-To-Maturity%20Trades.md)]],  and the structure of the over-the-counter (OTC) market for [fixed income derivatives](../../Financial%20Engineering/6.%20A%20Brief%20Introduction%20to%20Stochastic%20Calculus.md).
- We will also explore exchange-traded [futures](../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%203%20-%20Futures%20Markets/Futures%20Not%20Subject%20to%20Cash-And-Carry.md) options,  including options on Treasury bond [futures](../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%203%20-%20Futures%20Markets/Futures%20Not%20Subject%20to%20Cash-And-Carry.md) and [Eurodollar futures](../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%206%20Options%20on%20Non-Price%20Variables/Convexity-Adjusted%20Models%20for%20LIBOR%20Forwards%20Qu.md),  and their applications in managing financial risks.

## 2. Mechanics of Futures Trading

### 2.1 Types of Orders in Futures Trading

- When a trader wants to buy or sell a [futures](../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%203%20-%20Futures%20Markets/Futures%20Not%20Subject%20to%20Cash-And-Carry.md) contract,  they must specify the price and conditions under which the order is to be executed. These conditions are communicated to a [futures](../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%203%20-%20Futures%20Markets/Futures%20Not%20Subject%20to%20Cash-And-Carry.md) broker.
- There are several types of orders,  each with unique characteristics,  advantages,  and risks:

#### 2.1.1 Market Orders
- A **market order** is executed at the best available price as soon as it reaches the trading pit.
  - *Advantages*: Immediate execution.
  - *Risks*: Adverse price movements may occur between the time the order is placed and executed.

#### 2.1.2 Limit Orders
- A **limit order** specifies a price limit for the transaction.
  - A **buy limit order** allows the purchase of a [futures](../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%203%20-%20Futures%20Markets/Futures%20Not%20Subject%20to%20Cash-And-Carry.md) contract only at the designated price or lower.
  - A **sell limit order** allows the sale of a [futures](../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%203%20-%20Futures%20Markets/Futures%20Not%20Subject%20to%20Cash-And-Carry.md) contract only at the designated price or higher.
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

- A trader can take a position in the [futures](../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%203%20-%20Futures%20Markets/Futures%20Not%20Subject%20to%20Cash-And-Carry.md) market by:
  - **Buying a [futures](../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%203%20-%20Futures%20Markets/Futures%20Not%20Subject%20to%20Cash-And-Carry.md) contract**: This creates a **[long position](../../Financial%20Engineering/Derivatives/Part%20I%20-%20Forwards%20and%20Futures/Chapter%204%20-%20Futures:%20Hedging%20and%20Speculation.md)**.
  - **Selling a [futures](../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%203%20-%20Futures%20Markets/Futures%20Not%20Subject%20to%20Cash-And-Carry.md) contract**: This creates a **short position**.
- Positions can be liquidated in two ways:
  1. **Offsetting the position**: Taking an opposite position in the same contract (e.g.,  selling a [long position](../../Financial%20Engineering/Derivatives/Part%20I%20-%20Forwards%20and%20Futures/Chapter%204%20-%20Futures:%20Hedging%20and%20Speculation.md) or buying a short position).
  1. **Waiting until the delivery date**: Accepting or delivering the underlying instrument at the agreed-upon price.

- For contracts that do not involve physical delivery (e.g.,  [Eurodollar futures](../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%206%20Options%20on%20Non-Price%20Variables/Convexity-Adjusted%20Models%20for%20LIBOR%20Forwards%20Qu.md)),  settlement is in cash at the settlement price on the delivery date.

### 2.3 The Role of the Clearing Corporation

- The clearing corporation acts as an intermediary between buyers and sellers in the [futures](../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%203%20-%20Futures%20Markets/Futures%20Not%20Subject%20to%20Cash-And-Carry.md) market.
  - It becomes the buyer for every seller and the seller for every buyer.
  - This eliminates counterparty risk and allows traders to liquidate positions without involving the original counterparty.
- However,  traders remain exposed to the risk of default by their [futures](../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%203%20-%20Futures%20Markets/Futures%20Not%20Subject%20to%20Cash-And-Carry.md) broker. It is crucial to ensure that the broker has adequate capital to mitigate this risk.

### 2.4 Margin Requirements

- **Initial Margin**: A minimum deposit required to open a position,  specified by the exchange.
  - This serves as a good faith deposit and can be in the form of Treasury bills.
- **Maintenance Margin**: The minimum equity level required to maintain a position.
  - If the equity falls below this level due to adverse price movements,  additional margin ([variation margin](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%2010/Repurchase%20Agreements.md)) must be deposited.
- **[Variation Margin](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%2010/Repurchase%20Agreements.md)**: The amount required to restore equity to the initial margin level.
  - Must be deposited in cash.
- [Leverage](Lecture%206-[[Lecture%206-Leverage,%20Tail%20Risk,%20Volatility%20Products), Tail Risk, Volatility Products#6.1.3 [Margin requirements](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%2010/Case%20Study%20Mf%20Globals%20Repo-To-Maturity%20Trades.md)|[margin requirements](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%2010/Case%20Study%20Mf%20Globals%20Repo-To-Maturity%20Trades.md)]] vary based on:
  - The type of position (e.g.,  outright long/short vs. spread).
  - The purpose of the trade (e.g.,  speculative vs. [hedging](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%205/Key%20Rates%20O1s%20Durations%20and%20Hedging.md)).
  - The perceived risk of the contract.

## 3. Exchange-Traded Futures Options

### 3.1 Overview of Futures Options

- [Futures](../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%203%20-%20Futures%20Markets/Futures%20Not%20Subject%20to%20Cash-And-Carry.md) options are similar to traditional options but differ in that the underlying instrument is a [futures](../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%203%20-%20Futures%20Markets/Futures%20Not%20Subject%20to%20Cash-And-Carry.md) contract rather than a spot security.
- Types of [futures](../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%203%20-%20Futures%20Markets/Futures%20Not%20Subject%20to%20Cash-And-Carry.md) options:
  - **Call Options**: Grant the right to buy the underlying [futures](../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%203%20-%20Futures%20Markets/Futures%20Not%20Subject%20to%20Cash-And-Carry.md) contract at a specific price.
  - **Put Options**: Grant the right to sell the underlying [futures](../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%203%20-%20Futures%20Markets/Futures%20Not%20Subject%20to%20Cash-And-Carry.md) contract at a specific price.
- When exercised:
  - A call option results in a long [futures](../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%203%20-%20Futures%20Markets/Futures%20Not%20Subject%20to%20Cash-And-Carry.md) position for the buyer and a short [futures](../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%203%20-%20Futures%20Markets/Futures%20Not%20Subject%20to%20Cash-And-Carry.md) position for the seller.
  - A put option results in a short [futures](../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%203%20-%20Futures%20Markets/Futures%20Not%20Subject%20to%20Cash-And-Carry.md) position for the buyer and a long [futures](../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%203%20-%20Futures%20Markets/Futures%20Not%20Subject%20to%20Cash-And-Carry.md) position for the seller.
- The resulting [futures](../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%203%20-%20Futures%20Markets/Futures%20Not%20Subject%20to%20Cash-And-Carry.md) positions are subject to daily marking to market.

### 3.2 Options on Treasury Bond Futures

- Options on Treasury bond [futures](../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%203%20-%20Futures%20Markets/Futures%20Not%20Subject%20to%20Cash-And-Carry.md) are based on the price of a fictitious 20-year,  6% Treasury bond.
- The nominal size of the contract is $100,  000.
- Premiums are quoted in points and 64ths of a point.
  - Example: A premium of 1-10 implies a price of $1.15625% of face value,    or $1,  156.25.
- Flexible Treasury [futures](../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%203%20-%20Futures%20Markets/Futures%20Not%20Subject%20to%20Cash-And-Carry.md) options allow customization of strike prices,  expiration dates,  and exercise types (American or European).

### 3.3 Options on Eurodollar Futures

- These options are based on the quoted [Eurodollar futures](../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%206%20Options%20on%20Non-Price%20Variables/Convexity-Adjusted%20Models%20for%20LIBOR%20Forwards%20Qu.md) price (100 minus the annualized yield).
- Contract size: $1 million.
- Premiums are quoted in basis points.
  - Example: A premium of 20 (0.20) implies a price of $500.
- Applications:
  - **[Hedging](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%205/Key%20Rates%20O1s%20Durations%20and%20Hedging.md) floating-rate liabilities**: Institutions can buy puts to cap interest rate expenses.
  - **[Hedging](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%205/Key%20Rates%20O1s%20Durations%20and%20Hedging.md) floating-rate assets**: Investors can buy calls to offset lower interest income when rates fall.

## 4. OTC Fixed Income Derivatives

### 4.1 Structure of the OTC Market

- The OTC market lacks a central marketplace; transactions occur directly between buyers and sellers.
- Market participants include:
  - **Market-Makers**: Large [investment](../../Advanced%20Investments/An%20Asset%20Allocation%20Primer.md) and commercial banks that provide [liquidity](../../Financial%20Markets%20and%20Institutions/III.%20Liquidity%20of%20Assets/Class%205-%20Private%20Information,%20Liquidity,%20and%20Securitization/Class%20Note%2010%20Liquidity%20and%20Class%20Note%2010%20Liquidity%20and%20Liquidity%20Managementliquidity%20management.md).
  - **Brokers**: Facilitate transactions by connecting buyers and sellers.
- Key differences from exchange-traded markets:
  - No clearinghouse,  so counterparty [credit risk](../../Course%20Notes/Quantitative%20Trading%20Strategies%20Lecture%20Notes.md) is significant.
  - Greater flexibility in contract terms,  sizes,  and expiration dates.

### 4.2 Advantages and Disadvantages of OTC Markets

- **Advantages**:
  - Customization of contracts to meet specific needs.
  - Ability to trade a wide range of instruments,  including options on LIBOR,  [](../../Financial%20Markets%20and%20Institutions/III.%20Liquidity%20of%20Assets/Class%207-%20CP,%20Repo,%20and%20the%20Crisis/Class%20Note%2012%20-%20Commercial%20Paper.md#Class%20Note%2012%20–%20Commercial%20Paper|Commercial%20Paper),  and mortgage securities.
- **Disadvantages**:
  - [Lack of transparency](../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20III%20THE%20PLAYERS/Chapter%2012%20-%20Hedge%20Fund%20Strategies/Hedge%20Fund%20Replication%20and%20Strategy%20Indexes.md) and price visibility.
  - Counterparty [credit risk](../../Course%20Notes/Quantitative%20Trading%20Strategies%20Lecture%20Notes.md).

## 5. Summary and Key Takeaways

- [Futures trading](../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%203%20-%20Futures%20Markets/Futures%20Mechanics.md) involves various types of orders,  each with unique risks and benefits.
- The clearing corporation plays a critical role in mitigating counterparty risk in exchange-traded markets.
- [Leverage](Lecture%206-[[Lecture%206-Leverage,%20Tail%20Risk,%20Volatility%20Products), Tail Risk, Volatility Products#6.1.3 [Margin requirements](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%2010/Case%20Study%20Mf%20Globals%20Repo-To-Maturity%20Trades.md)|[margin requirements](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%2010/Case%20Study%20Mf%20Globals%20Repo-To-Maturity%20Trades.md)]] ensure that traders maintain sufficient equity to cover potential losses.
- [Futures](../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%203%20-%20Futures%20Markets/Futures%20Not%20Subject%20to%20Cash-And-Carry.md) options provide flexibility for [hedging](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%205/Key%20Rates%20O1s%20Durations%20and%20Hedging.md) and speculation,  with applications in [managing interest rate risk](.md).
- The OTC market offers customization but comes with significant counterparty risk and reduced transparency.

By understanding these mechanics and instruments,  traders and institutions can effectively manage risk and optimize their financial strategies.

# Lecture Notes: OTC Derivatives,  Caps,  Floors,  and Futures Pricing

## 1. Introduction to OTC Derivatives and Interest Rate Risk Management

- Over-the-counter (OTC) [derivatives](../../Financial%20Markets/Financial%20Trading%20and%20Markets/Chapter%209%20Arbitrage%20and%20Hedging%20With%20Options.md) are [financial instruments](../../Financial%20Instruments/A%20Practical%20Guide%20for%20Actuaries%20and%20other%20Business%20Professionals..md) traded directly between two parties,  without the involvement of an exchange.
- These instruments,  including [Basis Swap](A%20Guide%20to%20the%20Front%20End%20and%20[[Basis%20Swaps) Markets#[Forward Rate Agreements](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%2012/EURIBOR%20Forward%20Rate%20Agreements%20and%20Futures.md) (FRAs) [Overview](../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%201%20-%20Purpose%20and%20Structure%20of%20Financial%20Markets/Overview%20of%20Financial%20Markets.md)|[Forward Rate Agreements](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%2012/EURIBOR%20Forward%20Rate%20Agreements%20and%20Futures.md)]] (FRAs),  caps,  and [floors](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%2016/Caps%20and%20Floors.md),  are widely used for [managing interest rate risk](.md).
- Unlike exchange-traded [derivatives](../../Financial%20Markets/Financial%20Trading%20and%20Markets/Chapter%209%20Arbitrage%20and%20Hedging%20With%20Options.md),  OTC [derivatives](../../Financial%20Markets/Financial%20Trading%20and%20Markets/Chapter%209%20Arbitrage%20and%20Hedging%20With%20Options.md) are customizable but come with counterparty risk and [liquidity](../../Financial%20Markets%20and%20Institutions/III.%20Liquidity%20of%20Assets/Class%205-%20Private%20Information,%20Liquidity,%20and%20Securitization/Class%20Note%2010%20Liquidity%20and%20Class%20Note%2010%20Liquidity%20and%20Liquidity%20Managementliquidity%20management.md) constraints.
- This lecture will cover:
  - The mechanics and applications of [caps and floors](../../Financial%20Engineering/Fixed%20Income%20Derivatives/Interest%20Rate%20Derivatives-An%20Introduction%20to%20the%20%20Pricing%20of%20Caps%20and%20Floors.md) on LIBOR.
  - The structure and [pricing](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%207/Arbitrage%20Pricing%20of%20Derivatives.md) of [Basis Swap](A%20Guide%20to%20the%20Front%20End%20and%20[[Basis%20Swaps) Markets#[Forward Rate Agreements](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%2012/EURIBOR%20Forward%20Rate%20Agreements%20and%20Futures.md) (FRAs) [Overview](../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%201%20-%20Purpose%20and%20Structure%20of%20Financial%20Markets/Overview%20of%20Financial%20Markets.md)|[Forward Rate Agreements](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%2012/EURIBOR%20Forward%20Rate%20Agreements%20and%20Futures.md)]] (FRAs).
  - The [pricing](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%207/Arbitrage%20Pricing%20of%20Derivatives.md) of [futures contracts](../../Financial%20Engineering/Mathematics%20of%20the%20Financial%20Markets.md) and their [portfolio](../../Advanced%20Investments/An%20Asset%20Allocation%20Primer.md) applications.

## 2. Mechanics of OTC Derivatives

### 2.1 Counterparty Risk in OTC Markets

- Counterparty risk is a significant concern in [OTC markets](../A%20Survey%20of%20the%20Micro%20structure%20of%20Fixed-Income%20Markets.md),  as there is no central clearinghouse to guarantee transactions.
- Institutions mitigate counterparty risk in several ways:
  - **Creditworthiness Requirements**: Some institutions only transact with major entities that have sound credit ratings.
  - **Collateral Posting**: Counterparties may be required to post collateral immediately after the transaction,  similar to initial margin in [futures markets](../../Financial%20Instruments/Lecture%20Notes-%20Financial%20Instruments/Teaching%20Note%201-%20Forward%20Rates%20Agreement/Contango%20And%20Backwardation%20In%20Arbitrage-Free%20Futures-Markets.md).
  - **[Variation Margin](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%2010/Repurchase%20Agreements.md)**: Institutions reserve the right to call for additional collateral if the market moves against the counterparty.
- While these measures do not eliminate counterparty risk entirely,  they are sufficient for a large number of institutions to participate in the OTC market.

### 2.2 Liquidity Constraints in OTC Markets

- [Liquidity](../../Financial%20Markets%20and%20Institutions/III.%20Liquidity%20of%20Assets/Class%205-%20Private%20Information,%20Liquidity,%20and%20Securitization/Class%20Note%2010%20Liquidity%20and%20Class%20Note%2010%20Liquidity%20and%20Liquidity%20Managementliquidity%20management.md) in [OTC markets](../A%20Survey%20of%20the%20Micro%20structure%20of%20Fixed-Income%20Markets.md) can be constrained due to the non-assignable nature of most transactions.
  - For example,  an option seller cannot transfer the contingent liability to a third party without the buyer's permission.
  - To offset a short option position,  the seller may need to buy a similar option from a third party,  which introduces risks if the offsetting option is not identical or if the counterparty's credit is questionable.
- Non-standardization of contracts contributes to these [liquidity](../../Financial%20Markets%20and%20Institutions/III.%20Liquidity%20of%20Assets/Class%205-%20Private%20Information,%20Liquidity,%20and%20Securitization/Class%20Note%2010%20Liquidity%20and%20Class%20Note%2010%20Liquidity%20and%20Liquidity%20Managementliquidity%20management.md) issues but also provides flexibility in structuring agreements.

## 3. Caps and Floors on LIBOR

### 3.1 Overview of Caps and Floors

- [Caps and floors](../../Financial%20Engineering/Fixed%20Income%20Derivatives/Interest%20Rate%20Derivatives-An%20Introduction%20to%20the%20%20Pricing%20of%20Caps%20and%20Floors.md) are OTC options designed to manage [interest rate risk](../Analysis%20of%20Fixed%20Income%20Securities.md) on the short end of the yield curve.
  - A **cap** on [Basis Swap](A%20Guide%20to%20the%20Front%20End%20and%20[[Basis%20Swaps) Markets#[London Interbank Offered Rate](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%2012/Short-Term%20Rates%20and%20the%20Transition%20from%20LIBOR.md) (LIBOR)|LIBOR]] is essentially a series of put options on LIBOR-based debt.
  - A **floor** on [Basis Swap](A%20Guide%20to%20the%20Front%20End%20and%20[[Basis%20Swaps) Markets#[London Interbank Offered Rate](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%2012/Short-Term%20Rates%20and%20the%20Transition%20from%20LIBOR.md) (LIBOR)|LIBOR]] is essentially a series of call options on LIBOR-based debt.
- The buyer of a cap or floor pays an upfront premium and holds most of the rights in the contract,  while the seller receives the premium and is obligated to perform under the contract terms.

### 3.2 Mechanics of Caps

- A cap consists of multiple reset dates,  typically aligned with the interest accrual periods of the underlying LIBOR-based debt.

> [!NOTE]
> - **Example**: A five-year,  $100 million cap on three-month [Basis Swap](A%20Guide%20to%20the%20Front%20End%20and%20[[Basis%20Swaps) Markets#[London Interbank Offered Rate](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%2012/Short-Term%20Rates%20and%20the%20Transition%20from%20LIBOR.md) (LIBOR)|LIBOR]] struck at 2%.
>   - The contract specifies 20 reset dates (one every three months).
>   - On each reset date,  the three-month [Basis Swap](A%20Guide%20to%20the%20Front%20End%20and%20[[Basis%20Swaps) Markets#[London Interbank Offered Rate](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%2012/Short-Term%20Rates%20and%20the%20Transition%20from%20LIBOR.md) (LIBOR)|LIBOR]] rate is compared to the 2% strike rate:
> 	- If [Basis Swap](A%20Guide%20to%20the%20Front%20End%20and%20[[Basis%20Swaps) Markets#[London Interbank Offered Rate](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%2012/Short-Term%20Rates%20and%20the%20Transition%20from%20LIBOR.md) (LIBOR)|LIBOR]] ≤ 2%,  no payment is made.
> 	- If [Basis Swap](A%20Guide%20to%20the%20Front%20End%20and%20[[Basis%20Swaps) Markets#[London Interbank Offered Rate](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%2012/Short-Term%20Rates%20and%20the%20Transition%20from%20LIBOR.md) (LIBOR)|LIBOR]] > 2%,  the cap seller pays the buyer the monetary value of the excess LIBOR.
>
> - **Payoff Calculation**:
>   - For a 90-day interest accrual period,  the value of each basis point is:
> $$0.0001 \times 100,   000,   000 \times \frac{90}{360} = 2,   500 \,    \text{USD}$$
>   - If [Basis Swap](A%20Guide%20to%20the%20Front%20End%20and%20[[Basis%20Swaps) Markets#[London Interbank Offered Rate](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%2012/Short-Term%20Rates%20and%20the%20Transition%20from%20LIBOR.md) (LIBOR)|LIBOR]] = 2.50%,  the payoff is:
> $$\text{Payoff} = (2.50\% - 2.00\%) \times 100 \,    \text{basis points} \times 2,   500 = 125,   000 \,    \text{USD}$$
>   - If [Basis Swap](A%20Guide%20to%20the%20Front%20End%20and%20[[Basis%20Swaps) Markets#[London Interbank Offered Rate](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%2012/Short-Term%20Rates%20and%20the%20Transition%20from%20LIBOR.md) (LIBOR)|LIBOR]] = 4.00%,  the payoff is:
> $$\text{Payoff} = (4.00\% - 2.00\%) \times 100 \,    \text{basis points} \times 2,   500 = 500,   000 \,    \text{USD}$$
>
> - Payments are typically made at the end of the interest accrual period.
>

### 3.3 Mechanics of Floors

- [Floors](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%2016/Caps%20and%20Floors.md) operate similarly to caps but provide protection against falling [interest rates](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%202/Interest%20Rate%20Quotations.md).

> [!NOTE]
> - **Example**: A $25 million,  seven-year floor on six-month [Basis Swap](A%20Guide%20to%20the%20Front%20End%20and%20[[Basis%20Swaps) Markets#[London Interbank Offered Rate](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%2012/Short-Term%20Rates%20and%20the%20Transition%20from%20LIBOR.md) (LIBOR)|LIBOR]] struck at 3%.
>   - The contract specifies 14 reset dates (one every six months).
>   - On each reset date,  the six-month [Basis Swap](A%20Guide%20to%20the%20Front%20End%20and%20[[Basis%20Swaps) Markets#[London Interbank Offered Rate](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%2012/Short-Term%20Rates%20and%20the%20Transition%20from%20LIBOR.md) (LIBOR)|LIBOR]] rate is compared to the 3% strike rate:
> 	- If [Basis Swap](A%20Guide%20to%20the%20Front%20End%20and%20[[Basis%20Swaps) Markets#[London Interbank Offered Rate](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%2012/Short-Term%20Rates%20and%20the%20Transition%20from%20LIBOR.md) (LIBOR)|LIBOR]] ≥ 3%,  no payment is made.
> 	- If [Basis Swap](A%20Guide%20to%20the%20Front%20End%20and%20[[Basis%20Swaps) Markets#[London Interbank Offered Rate](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%2012/Short-Term%20Rates%20and%20the%20Transition%20from%20LIBOR.md) (LIBOR)|LIBOR]] < 3%,  the floor seller pays the buyer the monetary value of the shortfall.
>
> - **Payoff Calculation**:
>   - For a 180-day interest accrual period,  the value of each basis point is:
> $$0.0001 \times 25,   000,   000 \times \frac{180}{360} = 1,   250 \,    \text{USD}$$
>   - If [Basis Swap](A%20Guide%20to%20the%20Front%20End%20and%20[[Basis%20Swaps) Markets#[London Interbank Offered Rate](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%2012/Short-Term%20Rates%20and%20the%20Transition%20from%20LIBOR.md) (LIBOR)|LIBOR]] = 2.50%,  the payoff is:
> $$\text{Payoff} = (3.00\% - 2.50\%) \times 100 \,    \text{basis points} \times 1,   250 = 62,   500 \,    \text{USD}$$
>

### 3.4 Market Participants

- **Market-Makers**: Large [investment](../../Advanced%20Investments/An%20Asset%20Allocation%20Primer.md) and commercial banks dominate the cap and floor market,  providing [liquidity](../../Financial%20Markets%20and%20Institutions/III.%20Liquidity%20of%20Assets/Class%205-%20Private%20Information,%20Liquidity,%20and%20Securitization/Class%20Note%2010%20Liquidity%20and%20Class%20Note%2010%20Liquidity%20and%20Liquidity%20Managementliquidity%20management.md) and [pricing](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%207/Arbitrage%20Pricing%20of%20Derivatives.md).
- **End-Users**:
  - Buyers of caps: Institutions exposed to rising [short-term rates](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%208/Volatility%20and%20Convexity.md) (e.g.,  banks funding short and lending long).
  - Buyers of [floors](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%2016/Caps%20and%20Floors.md): Institutions exposed to falling rates (e.g.,  borrowers with [floating-rate debt](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%2013/Uses%20of%20Interest%20Rate%20Swaps.md) that has a built-in floor).
- **Sellers**:
  - Some sell caps or [floors](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%2016/Caps%20and%20Floors.md) outright for premium income.
  - Others use [caps and floors](../../Financial%20Engineering/Fixed%20Income%20Derivatives/Interest%20Rate%20Derivatives-An%20Introduction%20to%20the%20%20Pricing%20of%20Caps%20and%20Floors.md) to hedge or smooth cash flows on other [fixed-income instruments](../../Advanced%20Investments/Lecture%207-Risk%20and%20Return%20of%20Bonds.md).

## 4. [](../Fixed%20Income%20Lecture%20Notes/A%20Guide%20to%20the%20Front%20End%20and%20Basis%20Swap%20Markets.md#Forward%20Rate%20Agreements%20(FRAs)%20Overview|Forward%20Rate%20Agreements) (FRAs)

### 4.1 Overview of FRAs

- FRAs are OTC [derivatives](../../Financial%20Markets/Financial%20Trading%20and%20Markets/Chapter%209%20Arbitrage%20and%20Hedging%20With%20Options.md) that function as forward-starting loans without the exchange of principal.
- The cash exchanged at settlement depends only on the difference between the agreed-upon [Basis Swap](A%20Guide%20to%20the%20Front%20End%20and%20[[Basis%20Swaps) Markets#[Forward Rate Agreements](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%2012/EURIBOR%20Forward%20Rate%20Agreements%20and%20Futures.md) (FRAs) [Overview](../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%201%20-%20Purpose%20and%20Structure%20of%20Financial%20Markets/Overview%20of%20Financial%20Markets.md)|FRA]] rate and the reference rate (e.g.,  LIBOR).

### 4.2 [](../Fixed%20Income%20Lecture%20Notes/A%20Guide%20to%20the%20Front%20End%20and%20Basis%20Swap%20Markets.md#Forward%20Rate%20Agreements%20(FRAs)%20Overview|FRA) Market Structure

- The [Basis Swap](A%20Guide%20to%20the%20Front%20End%20and%20[[Basis%20Swaps) Markets#[Forward Rate Agreements](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%2012/EURIBOR%20Forward%20Rate%20Agreements%20and%20Futures.md) (FRAs) [Overview](../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%201%20-%20Purpose%20and%20Structure%20of%20Financial%20Markets/Overview%20of%20Financial%20Markets.md)|FRA]] market is highly liquid for threeand six-month LIBOR,  with contracts available for settlement starting one month forward and extending up to six months forward.
- Contracts are denoted by the start and end of the interest period they cover (e.g.,  a 1×4 [Basis Swap](A%20Guide%20to%20the%20Front%20End%20and%20[[Basis%20Swaps) Markets#[Forward Rate Agreements](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%2012/EURIBOR%20Forward%20Rate%20Agreements%20and%20Futures.md) (FRAs) [Overview](../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%201%20-%20Purpose%20and%20Structure%20of%20Financial%20Markets/Overview%20of%20Financial%20Markets.md)|FRA]] covers the period from one month to four months forward).

### 4.3 [](../Fixed%20Income%20Lecture%20Notes/A%20Guide%20to%20the%20Front%20End%20and%20Basis%20Swap%20Markets.md#Forward%20Rate%20Agreements%20(FRAs)%20Overview|FRA) Settlement

- No money changes hands until the settlement date.
- On the settlement date,  the [cash flow](../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%201%20-%20Purpose%20and%20Structure%20of%20Financial%20Markets/Preview%20of%20the%20Book.md) is calculated as the present value of the interest differential:
 $\text{Cash Flow} = \text{Notional Amount} \times \frac{\text{(Reference Rate - [](../Fixed%20Income%20Lecture%20Notes/A%20Guide%20to%20the%20Front%20End%20and%20Basis%20Swap%20Markets.md#Forward%20Rate%20Agreements%20(FRAs)%20Overview|FRA) Rate)} \times \text{Days}}{360} \times \frac{1}{(1 + \text{Reference Rate} \times \frac{\text{Days}}{360})}$$

### 4.4 [](../Fixed%20Income%20Lecture%20Notes/A%20Guide%20to%20the%20Front%20End%20and%20Basis%20Swap%20Markets.md#Forward%20Rate%20Agreements%20(FRAs)%20Overview|FRA) vs. Futures

- Unlike [futures](../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%203%20-%20Futures%20Markets/Futures%20Not%20Subject%20to%20Cash-And-Carry.md),  FRAs are not marked to market daily,  and the profit/loss is a convex function of the underlying rate due to present valuing.
- Buyers of FRAs benefit from rising rates,  while sellers benefit from falling rates.

## 5. Pricing Futures Contracts

### 5.1 Arbitrage and the Law of One Price

- [Futures](../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%203%20-%20Futures%20Markets/Futures%20Not%20Subject%20to%20Cash-And-Carry.md) prices are determined by [arbitrage](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%207/Arbitrage%20Pricing%20of%20Derivatives.md),  ensuring that no [risk-free profit](../../Financial%20Markets/Financial%20Asset%20Pricing%20Theory%20Overview/Chapter%203%20-%20%20Assets,%20Portfolios,%20and%20Arbitrage/Arbitrage.md) opportunities exist.
- The [law of one price](../../Pricing%20Forwards,%20Futures,%20Bonds,%20Swaps,%20Swaptions,%20Caps%20and%20Floors%20under%20No-Arbitrage%20and%20Risk-Neutral%20Pricing.md) states that identical cash flows must have the same price,  regardless of how they are created.

### 5.2 Cash-and-Carry Arbitrage

> [!NOTE]
> - **Example**: A 20-year,  $100 par value bond with a 12% coupon is selling at par. The three-month interest rate is 8% per year.
>   - If the [futures price](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%2011/Futures%20Price%20and%20the%20Quality%20Option%20Before%20E.md) is 107:
> 	- Sell the [futures](../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%203%20-%20Futures%20Markets/Futures%20Not%20Subject%20to%20Cash-And-Carry.md) contract at 107.
> 	- Borrow $100 for three months at 8%.
> 	- Buy the bond for $100.
> 	- At settlement,  deliver the bond and repay the loan:
> 	  - Receive $107 from the [futures](../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%203%20-%20Futures%20Markets/Futures%20Not%20Subject%20to%20Cash-And-Carry.md) contract.
> 	  - Pay $102 (loan principal + interest).
> 	  - Profit = $107 - $102 = $5.

- [Arbitrage](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%207/Arbitrage%20Pricing%20of%20Derivatives.md) forces the [futures price](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%2011/Futures%20Price%20and%20the%20Quality%20Option%20Before%20E.md) to converge to its fair value.

### 5.3 Reverse Cash-and-Carry Arbitrage

> [!NOTE]
>
> - If the [futures price](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%2011/Futures%20Price%20and%20the%20Quality%20Option%20Before%20E.md) is 92:
>   - Buy the [futures](../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%203%20-%20Futures%20Markets/Futures%20Not%20Subject%20to%20Cash-And-Carry.md) contract at 92.
>   - Short the bond for $100.
>   - Invest $100 for three months at 8%.
>   - At settlement,  buy the bond to cover the short position:
> 	- Pay $95 (bond price + [accrued interest](../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%202%20-%20Spot%20Markets/Intra-Year%20Compounding%20and%20Day-Count.md)).
> 	- Receive $102 ([investment](../../Advanced%20Investments/An%20Asset%20Allocation%20Primer.md) principal + interest).
> 	- Profit = $102 - $95 = $7.
>

- Again,  [arbitrage](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%207/Arbitrage%20Pricing%20of%20Derivatives.md) eliminates the profit opportunity.

### 5.4 Equilibrium Futures Price

- The equilibrium [futures price](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%2011/Futures%20Price%20and%20the%20Quality%20Option%20Before%20E.md) eliminates [arbitrage opportunities](../../Financial%20Markets%20and%20Institutions/III.%20Liquidity%20of%20Assets/Class%208-%20Markets,%20Meltdowns,%20and%20Arbitrage/Class%20Note%2013%20The%20LTCM%20Meltdown.md):
 $\text{Futures Price} = \text{Spot Price} \times (1 + \text{Risk-Free Rate} \times \text{Time to Maturity})$$

## 6. Summary and Key Takeaways

- OTC [derivatives](../../Financial%20Markets/Financial%20Trading%20and%20Markets/Chapter%209%20Arbitrage%20and%20Hedging%20With%20Options.md) like caps,  [floors](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%2016/Caps%20and%20Floors.md),  and FRAs provide flexibility in [managing interest rate risk](.md) but come with counterparty risk and [liquidity](../../Financial%20Markets%20and%20Institutions/III.%20Liquidity%20of%20Assets/Class%205-%20Private%20Information,%20Liquidity,%20and%20Securitization/Class%20Note%2010%20Liquidity%20and%20Class%20Note%2010%20Liquidity%20and%20Liquidity%20Managementliquidity%20management.md) constraints.
- [Caps and floors](../../Financial%20Engineering/Fixed%20Income%20Derivatives/Interest%20Rate%20Derivatives-An%20Introduction%20to%20the%20%20Pricing%20of%20Caps%20and%20Floors.md) are essential tools for institutions exposed to [interest rate volatility](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%207/Fixed%20Income%20Versus%20Equity%20Derivatives.md).
- FRAs are forward-starting loans that allow participants to hedge or speculate on future [interest rates](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%202/Interest%20Rate%20Quotations.md).
- [Futures](../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%203%20-%20Futures%20Markets/Futures%20Not%20Subject%20to%20Cash-And-Carry.md) prices are determined by [arbitrage](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%207/Arbitrage%20Pricing%20of%20Derivatives.md),  ensuring that they reflect fair value based on the [law of one price](../../Pricing%20Forwards,%20Futures,%20Bonds,%20Swaps,%20Swaptions,%20Caps%20and%20Floors%20under%20No-Arbitrage%20and%20Risk-Neutral%20Pricing.md).

By understanding these instruments and their [pricing mechanisms](../../Chinese%20Financial%20System.md),  market participants can effectively manage risk and exploit [arbitrage opportunities](../../Financial%20Markets%20and%20Institutions/III.%20Liquidity%20of%20Assets/Class%208-%20Markets,%20Meltdowns,%20and%20Arbitrage/Class%20Note%2013%20The%20LTCM%20Meltdown.md).

# Lecture Notes: Controlling Interest-Rate Risk with Futures and Options

## 1. Introduction to Interest-Rate Risk Management

- Interest-rate risk is a critical concern for [portfolio](../../Advanced%20Investments/An%20Asset%20Allocation%20Primer.md) managers,  as changes in [interest rates](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%202/Interest%20Rate%20Quotations.md) can significantly impact the value of fixed-income securities.
- Derivative instruments,  such as [futures](../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%203%20-%20Futures%20Markets/Futures%20Not%20Subject%20to%20Cash-And-Carry.md) and options,  provide powerful tools for managing this risk.
- This lecture focuses on:
  - The theoretical [pricing](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%207/Arbitrage%20Pricing%20of%20Derivatives.md) of [futures contracts](../../Financial%20Engineering/Mathematics%20of%20the%20Financial%20Markets.md).
  - The concept of carry and its role in [futures pricing](../../Financial%20Engineering/Derivatives/Part%20I%20-%20Forwards%20and%20Futures/Chapter%203%20-%20Forward%20and%20Futures%20Prices.md).
  - Applications of [futures contracts](../../Financial%20Engineering/Mathematics%20of%20the%20Financial%20Markets.md) in [portfolio management](../../Financial%20Engineering/Fixed%20Income%20Derivatives/The%20Impact%20of%20Option%20Strategies%20in%20Financial%20%20Portfolios%20Performance.md),  including [duration](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%205/Key%20Rates%20O1s%20Durations%20and%20Hedging.md) control,  [hedging](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%205/Key%20Rates%20O1s%20Durations%20and%20Hedging.md),  [Asset Allocation](Lecture%202-%20[[Lecture%202-%20Asset%20Allocation%20with%20Multiple%20Risky%20Assets) with [Multiple Risky Assets](../../Advanced%20Investments/Lecture%202-%20Asset%20Allocation%20with%20Multiple%20Risky%20Assets.md)|[asset allocation](../../Advanced%20Investments/Lecture%202-%20Asset%20Allocation%20with%20Multiple%20Risky%20Assets.md)]],  and [portable alpha](../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%202%20-%20Spot%20Markets/Hedge%20Funds%20Alpha%20Beta%20and%20Strategy%20Indexes%20287.md) strategies.

## 2. Theoretical Futures Pricing and the Concept of Carry

### 2.1 Deriving the Theoretical Futures Price
- The theoretical [futures price](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%2011/Futures%20Price%20and%20the%20Quality%20Option%20Before%20E.md) is derived using [arbitrage arguments](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%2011/Forward%20Contracts%20and%20Forward%20Prices.md),  assuming no transaction costs and no interim cash flows.
- Key variables:
	  - $P$: Cash market price of the bond.
	  - $c$: Current yield,  calculated as the coupon rate divided by the cash market price.
	  - $r$: Financing rate (borrowing/lending rate).
	  - $t$: Time to the [futures](../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%203%20-%20Futures%20Markets/Futures%20Not%20Subject%20to%20Cash-And-Carry.md) delivery date (in years).
	  - $F$: [Futures price](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%2011/Futures%20Price%20and%20the%20Quality%20Option%20Before%20E.md).

#### 2.1.1 Cash-and-Carry Arbitrage

- **Steps**:
  1. Sell the [futures](../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%203%20-%20Futures%20Markets/Futures%20Not%20Subject%20to%20Cash-And-Carry.md) contract at $F$.
  1. Purchase the bond for $P$.
  1. Borrow $P$ at the financing rate $r$ until the settlement date.

- **Outcome at Settlement**:
  - **Proceeds**:
	- From the [futures](../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%203%20-%20Futures%20Markets/Futures%20Not%20Subject%20to%20Cash-And-Carry.md) contract: $F$.
	- [Accrued interest](../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%202%20-%20Spot%20Markets/Intra-Year%20Compounding%20and%20Day-Count.md) on the bond: $ctP$.
	- Total proceeds: $$F + ctP$$
  - **Outlay**:
	- Repayment of the loan principal: $P$.
	- Interest on the loan: $rtP$.
	- Total outlay: $P + rtP$.
- **Profit**:
 $$\text{Profit} = F + ctP - (P + rtP)$$

- **Equilibrium Condition**:
  - To eliminate [arbitrage opportunities](../../Financial%20Markets%20and%20Institutions/III.%20Liquidity%20of%20Assets/Class%208-%20Markets,%20Meltdowns,%20and%20Arbitrage/Class%20Note%2013%20The%20LTCM%20Meltdown.md),  profit must equal zero:
   $$0 = F + ctP - (P + rtP)$$
  - Solving for $F$:
   $$F = P + Pt(r - c) = P[1 + t(r - c)]$$

#### 2.1.2 Reverse Cash-and-Carry Arbitrage

- **Steps**:
  1. Buy the [futures](../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%203%20-%20Futures%20Markets/Futures%20Not%20Subject%20to%20Cash-And-Carry.md) contract at $F$.
  1. Sell (short) the bond for $P$.
  1. Invest $P$ at the financing rate $r$ until the settlement date.

- **Outcome at Settlement**:
  - **Proceeds**:
	- From the loan principal: $P$.
	- Interest earned: $rtP$.
	- Total proceeds: $P + rtP$.
  - **Outlay**:
	- From the [futures](../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%203%20-%20Futures%20Markets/Futures%20Not%20Subject%20to%20Cash-And-Carry.md) contract: $F$.
	- [Accrued interest](../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%202%20-%20Spot%20Markets/Intra-Year%20Compounding%20and%20Day-Count.md) on the bond: $ctP$.
	- Total outlay: $F + ctP$.
- **Profit**:
 $$\text{Profit} = P + rtP - (F + ctP)$$

- **Equilibrium Condition**:
  - To eliminate [arbitrage opportunities](../../Financial%20Markets%20and%20Institutions/III.%20Liquidity%20of%20Assets/Class%208-%20Markets,%20Meltdowns,%20and%20Arbitrage/Class%20Note%2013%20The%20LTCM%20Meltdown.md),  profit must equal zero:
   $$0 = P + rtP - (F + ctP)$$
  - Solving for $F$ yields the same equation:
   $$F = P[1 + t(r - c)]$$

> [!NOTE]
> ### 2.2 Example: Calculating the Theoretical [Futures Price](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%2011/Futures%20Price%20and%20the%20Quality%20Option%20Before%20E.md)
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
  - The theoretical [futures price](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%2011/Futures%20Price%20and%20the%20Quality%20Option%20Before%20E.md) is $99$,  which is at a discount to the cash market price due to negative carry ($r < c$).

### 2.3 The Concept of Carry

- **Definition**:
  - Carry is the net [financing cost](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%203/Realized%20Returns.md),  calculated as the difference between the financing rate ($r$) and the current yield ($c$).
  - $\text{Carry} = r - c$
- **Implications**:
  - **Positive Carry ($c > r$)**:
	- The [futures price](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%2011/Futures%20Price%20and%20the%20Quality%20Option%20Before%20E.md) will sell at a discount to the cash price ($F < P$).
  - **Negative Carry ($c < r$)**:
	- The [futures price](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%2011/Futures%20Price%20and%20the%20Quality%20Option%20Before%20E.md) will sell at a premium to the cash price ($F > P$).
  - **Zero Carry ($c = r$)**:
	- The [futures price](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%2011/Futures%20Price%20and%20the%20Quality%20Option%20Before%20E.md) will equal the cash price ($F = P$).
- **Real-World Factors**:
  - The shape of the yield curve influences carry:
	- **Upward-Sloping Yield Curve**: [Short-term financing](../../Financial%20Markets%20and%20Institutions/III.%20Liquidity%20of%20Assets/Class%207-%20CP,%20Repo,%20and%20the%20Crisis/Asset%20Backed%20Commercial%20Paper%20Understanding%20the%20Risks.md) rates are lower than current yields,  resulting in positive carry.
	- **Inverted Yield Curve**: [Short-term financing](../../Financial%20Markets%20and%20Institutions/III.%20Liquidity%20of%20Assets/Class%207-%20CP,%20Repo,%20and%20the%20Crisis/Asset%20Backed%20Commercial%20Paper%20Understanding%20the%20Risks.md) rates are higher than current yields,  resulting in negative carry.

## 3. Applications of Futures in Portfolio Management

### 3.1 Interest-Rate Risk Control

- **Objective**:
  - Adjust the [portfolio](../../Advanced%20Investments/An%20Asset%20Allocation%20Primer.md)'s [duration](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%205/Key%20Rates%20O1s%20Durations%20and%20Hedging.md) to manage exposure to [interest rate changes](../../International%20Finance/Bridgewater/How%20Countries%20Go%20Broke/How%20Countries%20Go%20Broke-Chapter%2012%20to%20Chapter%2014.md).
  - Increase [duration](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%205/Key%20Rates%20O1s%20Durations%20and%20Hedging.md) if rates are expected to fall; decrease [duration](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%205/Key%20Rates%20O1s%20Durations%20and%20Hedging.md) if rates are expected to rise.
- **Mechanism**:
  - **Buying [Futures](../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%203%20-%20Futures%20Markets/Futures%20Not%20Subject%20to%20Cash-And-Carry.md)**: Increases [portfolio](../../Advanced%20Investments/An%20Asset%20Allocation%20Primer.md) [duration](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%205/Key%20Rates%20O1s%20Durations%20and%20Hedging.md),  as [futures](../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%203%20-%20Futures%20Markets/Futures%20Not%20Subject%20to%20Cash-And-Carry.md) prices rise when rates fall.
  - **Selling [Futures](../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%203%20-%20Futures%20Markets/Futures%20Not%20Subject%20to%20Cash-And-Carry.md)**: Decreases [portfolio](../../Advanced%20Investments/An%20Asset%20Allocation%20Primer.md) [duration](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%205/Key%20Rates%20O1s%20Durations%20and%20Hedging.md),  as [futures](../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%203%20-%20Futures%20Markets/Futures%20Not%20Subject%20to%20Cash-And-Carry.md) prices fall when rates rise.
- **Advantages**:
  - [Futures](../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%203%20-%20Futures%20Markets/Futures%20Not%20Subject%20to%20Cash-And-Carry.md) provide a quick and cost-effective way to adjust [duration](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%205/Key%20Rates%20O1s%20Durations%20and%20Hedging.md) compared to cash market instruments.

### 3.2 Hedging

- **Definition**:
  - [Hedging](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%205/Key%20Rates%20O1s%20Durations%20and%20Hedging.md) involves taking a [futures](../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%203%20-%20Futures%20Markets/Futures%20Not%20Subject%20to%20Cash-And-Carry.md) position to offset potential losses in the cash market.
- **Types of Hedges**:
  - **[Short Hedge](../../Financial%20Engineering/Derivatives/Part%20I%20-%20Forwards%20and%20Futures/Chapter%204%20-%20Futures:%20Hedging%20and%20Speculation.md)**:
	- Protects against a decline in the cash price of a fixed-income security.
	- Example: A [pension fund](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%2013/Uses%20of%20Interest%20Rate%20Swaps.md) manager sells [futures](../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%203%20-%20Futures%20Markets/Futures%20Not%20Subject%20to%20Cash-And-Carry.md) to lock in a selling price for bonds that must be liquidated in the future.
  - **Long Hedge**:
	- Protects against an increase in the cash price of a fixed-income security.
	- Example: A manager buys [futures](../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%203%20-%20Futures%20Markets/Futures%20Not%20Subject%20to%20Cash-And-Carry.md) to lock in a purchase price for bonds expected to be bought in the future.
- **[Basis Risk](../../Financial%20Markets%20and%20Institutions/III.%20Liquidity%20of%20Assets/Class%208-%20Markets,%20Meltdowns,%20and%20Arbitrage/Lessons%20From%20The%20Crisis.md)**:
  - The difference between the cash price and the [futures price](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%2011/Futures%20Price%20and%20the%20Quality%20Option%20Before%20E.md) is called the basis.
  - [Basis risk](../../Financial%20Markets%20and%20Institutions/III.%20Liquidity%20of%20Assets/Class%208-%20Markets,%20Meltdowns,%20and%20Arbitrage/Lessons%20From%20The%20Crisis.md) arises when the cash and [futures](../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%203%20-%20Futures%20Markets/Futures%20Not%20Subject%20to%20Cash-And-Carry.md) prices do not move perfectly together.
- **Cross-[Hedging](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%205/Key%20Rates%20O1s%20Durations%20and%20Hedging.md)**:
  - Occurs when the bond to be hedged is not identical to the bond underlying the [futures](../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%203%20-%20Futures%20Markets/Futures%20Not%20Subject%20to%20Cash-And-Carry.md) contract.
  - Cross-[hedging](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%205/Key%20Rates%20O1s%20Durations%20and%20Hedging.md) introduces additional [basis risk](../../Financial%20Markets%20and%20Institutions/III.%20Liquidity%20of%20Assets/Class%208-%20Markets,%20Meltdowns,%20and%20Arbitrage/Lessons%20From%20The%20Crisis.md).

### 3.3 [asset allocation](../../Advanced%20Investments/Lecture%202-%20Asset%20Allocation%20with%20Multiple%20Risky%20Assets.md)

- **Objective**:
  - Adjust the composition of a [portfolio](../../Advanced%20Investments/An%20Asset%20Allocation%20Primer.md) between asset classes (e.g.,  stocks and bonds).
- **Mechanism**:
  - Use interest-rate [futures](../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%203%20-%20Futures%20Markets/Futures%20Not%20Subject%20to%20Cash-And-Carry.md) and [stock index futures](../../Financial%20Instruments/Lecture%20Notes-%20Financial%20Instruments/Teaching%20Note%202-Futures%20Contracts.md) to efficiently shift allocations without transacting in the cash market.

### 3.4 Creating Synthetic Securities for Yield Enhancement

- **Concept**:
  - Combine [futures contracts](../../Financial%20Engineering/Mathematics%20of%20the%20Financial%20Markets.md) with cash market instruments to create [synthetic securities](../../Financial%20Engineering/Derivatives/Part%20IV%20-%20Options/Chapter%2017%20-%20Option%20Strategies.md).
- **Example**:
  - An investor holding a 20-year Treasury bond sells Treasury [futures](../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%203%20-%20Futures%20Markets/Futures%20Not%20Subject%20to%20Cash-And-Carry.md) for delivery in three months.
  - The combined position is equivalent to a three-month riskless security (e.g.,  a Treasury bill).
  - If the synthetic security's yield exceeds the yield on a cash market Treasury bill,  the investor can enhance [portfolio](../../Advanced%20Investments/An%20Asset%20Allocation%20Primer.md) [returns](../../Financial%20Markets/Financial%20Asset%20Pricing%20Theory%20Overview/Chapter%203%20-%20%20Assets,%20Portfolios,%20and%20Arbitrage/Assets.md).

### 3.5 Portable Alpha Strategies

- **Definition**:
  - [Portable alpha](../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%202%20-%20Spot%20Markets/Hedge%20Funds%20Alpha%20Beta%20and%20Strategy%20Indexes%20287.md) strategies separate market [returns](../../Financial%20Markets/Financial%20Asset%20Pricing%20Theory%20Overview/Chapter%203%20-%20%20Assets,%20Portfolios,%20and%20Arbitrage/Assets.md) (beta) from [returns](../../Financial%20Markets/Financial%20Asset%20Pricing%20Theory%20Overview/Chapter%203%20-%20%20Assets,%20Portfolios,%20and%20Arbitrage/Assets.md) generated by selection skill (alpha).
- **Implementation**:
  - Use [derivatives](../../Financial%20Markets/Financial%20Trading%20and%20Markets/Chapter%209%20Arbitrage%20and%20Hedging%20With%20Options.md) (e.g.,  [futures](../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%203%20-%20Futures%20Markets/Futures%20Not%20Subject%20to%20Cash-And-Carry.md) and swaps) to maintain market exposure while pursuing alpha-generating strategies.
- **Advantages**:
  - Flexibility to add [returns](../../Financial%20Markets/Financial%20Asset%20Pricing%20Theory%20Overview/Chapter%203%20-%20%20Assets,%20Portfolios,%20and%20Arbitrage/Assets.md) without increasing risk.
  - Applicable across asset classes,  including equities and [fixed income](../Lecture%20Notes%20Bonds,%20%20Preferred%20Stock,%20%20and%20Structured%20Products.md).

## 4. Key Takeaways

- The theoretical [futures price](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%2011/Futures%20Price%20and%20the%20Quality%20Option%20Before%20E.md) is determined by the net [financing cost](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%203/Realized%20Returns.md) (carry),  which reflects the relationship between the financing rate and the current yield.
- [Futures contracts](../../Financial%20Engineering/Mathematics%20of%20the%20Financial%20Markets.md) are versatile tools for managing interest-rate risk,  enabling [portfolio](../../Advanced%20Investments/An%20Asset%20Allocation%20Primer.md) managers to adjust [duration](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%205/Key%20Rates%20O1s%20Durations%20and%20Hedging.md),  hedge positions,  and alter [Asset Allocation](Lecture%202-%20[[Lecture%202-%20Asset%20Allocation%20with%20Multiple%20Risky%20Assets) with [Multiple Risky Assets](../../Advanced%20Investments/Lecture%202-%20Asset%20Allocation%20with%20Multiple%20Risky%20Assets.md)|[asset allocation](../../Advanced%20Investments/Lecture%202-%20Asset%20Allocation%20with%20Multiple%20Risky%20Assets.md)]]s efficiently.
- [Synthetic securities](../../Financial%20Engineering/Derivatives/Part%20IV%20-%20Options/Chapter%2017%20-%20Option%20Strategies.md) and [portable alpha](../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%202%20-%20Spot%20Markets/Hedge%20Funds%20Alpha%20Beta%20and%20Strategy%20Indexes%20287.md) strategies demonstrate the innovative applications of [futures](../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%203%20-%20Futures%20Markets/Futures%20Not%20Subject%20to%20Cash-And-Carry.md) in enhancing [portfolio](../../Advanced%20Investments/An%20Asset%20Allocation%20Primer.md) [returns](../../Financial%20Markets/Financial%20Asset%20Pricing%20Theory%20Overview/Chapter%203%20-%20%20Assets,%20Portfolios,%20and%20Arbitrage/Assets.md) and achieving [investment](../../Advanced%20Investments/An%20Asset%20Allocation%20Primer.md) objectives.
- [Basis risk](../../Financial%20Markets%20and%20Institutions/III.%20Liquidity%20of%20Assets/Class%208-%20Markets,%20Meltdowns,%20and%20Arbitrage/Lessons%20From%20The%20Crisis.md) and cross-[hedging](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%205/Key%20Rates%20O1s%20Durations%20and%20Hedging.md) are important considerations when using [futures for hedging](../../Financial%20Engineering/Derivatives/Part%20I%20-%20Forwards%20and%20Futures/Chapter%204%20-%20Futures:%20Hedging%20and%20Speculation.md) purposes,  as they can impact the effectiveness of the hedge.

By mastering these concepts and strategies,  [portfolio](../../Advanced%20Investments/An%20Asset%20Allocation%20Primer.md) managers can effectively navigate interest-rate risk and optimize [portfolio](../../Advanced%20Investments/An%20Asset%20Allocation%20Primer.md) performance.

# Lecture Notes: Controlling Interest-Rate Risk with Futures and Hedging Strategies

## 1. Introduction to Interest-Rate Risk Management with Futures

- Interest-rate risk is a critical concern for [portfolio](../../Advanced%20Investments/An%20Asset%20Allocation%20Primer.md) managers,  as changes in [interest rates](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%202/Interest%20Rate%20Quotations.md) can significantly impact the value of fixed-income securities.
- [Futures contracts](../../Financial%20Engineering/Mathematics%20of%20the%20Financial%20Markets.md) on interest-rate instruments provide a cost-effective and flexible way to manage this risk.
- This lecture focuses on:
  - The advantages of using interest-rate [futures](../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%203%20-%20Futures%20Markets/Futures%20Not%20Subject%20to%20Cash-And-Carry.md) over cash-market instruments.
  - The principles of controlling interest-rate risk using [futures](../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%203%20-%20Futures%20Markets/Futures%20Not%20Subject%20to%20Cash-And-Carry.md).
  - The mechanics of determining the number of [futures contracts](../../Financial%20Engineering/Mathematics%20of%20the%20Financial%20Markets.md) required to achieve a target [dollar duration](../../Financial%20Engineering/A%20Guide%20to%20Duration%20DV01%20and%20Yield%20Curve.md).
  - [Hedging](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%205/Key%20Rates%20O1s%20Durations%20and%20Hedging.md) strategies using interest-rate [futures](../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%203%20-%20Futures%20Markets/Futures%20Not%20Subject%20to%20Cash-And-Carry.md),  including short and long hedges.

## 2. Advantages of Using Interest-Rate Futures

### 2.1 Lower Transaction Costs
- Trading [futures contracts](../../Financial%20Engineering/Mathematics%20of%20the%20Financial%20Markets.md) incurs significantly lower transaction costs compared to trading long-term [Treasury securities](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Front%20Matter/US%20Markets.md) in the cash market.
- This cost efficiency makes [futures](../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%203%20-%20Futures%20Markets/Futures%20Not%20Subject%20to%20Cash-And-Carry.md) an attractive tool for frequent adjustments to [portfolio](../../Advanced%20Investments/An%20Asset%20Allocation%20Primer.md) [duration](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%205/Key%20Rates%20O1s%20Durations%20and%20Hedging.md) or [hedging](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%205/Key%20Rates%20O1s%20Durations%20and%20Hedging.md) strategies.

### 2.2 Lower Margin Requirements
- [Futures contracts](../../Financial%20Engineering/Mathematics%20of%20the%20Financial%20Markets.md) require only an initial margin deposit,  which is a fraction of the contract's notional value.
- This allows [portfolio](../../Advanced%20Investments/An%20Asset%20Allocation%20Primer.md) managers to achieve greater [leverage](../../Advanced%20Investments/Lecture%206-Leverage,%20Tail%20Risk,%20Volatility%20Products.md) compared to directly trading [Treasury securities](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Front%20Matter/US%20Markets.md).

### 2.3 Ease of Short Selling
- Selling short in the [futures](../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%203%20-%20Futures%20Markets/Futures%20Not%20Subject%20to%20Cash-And-Carry.md) market is more straightforward than in the cash market for [Treasury securities](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Front%20Matter/US%20Markets.md).
- [Futures contracts](../../Financial%20Engineering/Mathematics%20of%20the%20Financial%20Markets.md) eliminate the need to borrow securities,  making short positions more accessible and cost-effective.

### 2.4 Extending Portfolio Duration
- [Futures](../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%203%20-%20Futures%20Markets/Futures%20Not%20Subject%20to%20Cash-And-Carry.md) can be used to construct portfolios with longer durations than those available in the cash market.
  - *Example*: A [pension fund](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%2013/Uses%20of%20Interest%20Rate%20Swaps.md) manager may need a [portfolio](../../Advanced%20Investments/An%20Asset%20Allocation%20Primer.md) [duration](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%205/Key%20Rates%20O1s%20Durations%20and%20Hedging.md) of 15 to meet specific [investment](../../Advanced%20Investments/An%20Asset%20Allocation%20Primer.md) objectives. If bonds with such a long [duration](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%205/Key%20Rates%20O1s%20Durations%20and%20Hedging.md) are unavailable,  the manager can buy interest-rate [futures](../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%203%20-%20Futures%20Markets/Futures%20Not%20Subject%20to%20Cash-And-Carry.md) to increase the [portfolio](../../Advanced%20Investments/An%20Asset%20Allocation%20Primer.md)'s [duration](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%205/Key%20Rates%20O1s%20Durations%20and%20Hedging.md) to the target level.

## 3. General Principles of Interest-Rate Risk Control

### 3.1 Combining Dollar Exposures
- The key principle in controlling interest-rate risk with [futures](../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%203%20-%20Futures%20Markets/Futures%20Not%20Subject%20to%20Cash-And-Carry.md) is to combine the dollar exposure of the current [portfolio](../../Advanced%20Investments/An%20Asset%20Allocation%20Primer.md) with the dollar exposure of a [futures](../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%203%20-%20Futures%20Markets/Futures%20Not%20Subject%20to%20Cash-And-Carry.md) position to achieve the target dollar exposure.
- The total dollar exposure is given by:
 $\text{Portfolio's Dollar Duration} = \text{Current Dollar Duration} + \text{Dollar Duration of Futures Position}$$

### 3.2 Measures of Interest-Rate Sensitivity
- Two commonly used measures for approximating the sensitivity of a bond or [portfolio](../../Advanced%20Investments/An%20Asset%20Allocation%20Primer.md) to changes in [interest rates](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%202/Interest%20Rate%20Quotations.md) are:
  - **Price Value of a Basis Point (PVBP)**: The dollar price change resulting from a 1 basis point change in yield.
  - **[Duration](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%205/Key%20Rates%20O1s%20Durations%20and%20Hedging.md)**: The approximate percentage price change for a 100 basis point change in rates.
	- *Effective [Duration](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%205/Key%20Rates%20O1s%20Durations%20and%20Hedging.md)*: Used for bonds with embedded options,  as it accounts for changes in cash flows due to interest rate movements.
	- *Effective [Dollar Duration](../../Financial%20Engineering/A%20Guide%20to%20Duration%20DV01%20and%20Yield%20Curve.md)*: The dollar price change for a given change in [interest rates](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%202/Interest%20Rate%20Quotations.md),  calculated using the [portfolio](../../Advanced%20Investments/An%20Asset%20Allocation%20Primer.md)'s valuation model.

### 3.3 Importance of a Valuation Model
- A reliable valuation model is essential for:
  - Estimating the new values of bonds in the [portfolio](../../Advanced%20Investments/An%20Asset%20Allocation%20Primer.md) when [interest rates](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%202/Interest%20Rate%20Quotations.md) change.
  - Valuing the derivative contracts used to control interest-rate exposure.

## 4. Determining the Target Dollar Duration

### 4.1 Calculating Target Dollar Duration
- The target [dollar duration](../../Financial%20Engineering/A%20Guide%20to%20Duration%20DV01%20and%20Yield%20Curve.md) for a [portfolio](../../Advanced%20Investments/An%20Asset%20Allocation%20Primer.md) is determined based on the desired sensitivity to [interest rate changes](../../International%20Finance/Bridgewater/How%20Countries%20Go%20Broke/How%20Countries%20Go%20Broke-Chapter%2012%20to%20Chapter%2014.md).
- For a 50 basis point change in [interest rates](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%202/Interest%20Rate%20Quotations.md),  the target [dollar duration](../../Financial%20Engineering/A%20Guide%20to%20Duration%20DV01%20and%20Yield%20Curve.md) is calculated as:
 $\text{Target Dollar Duration} = \frac{\text{Target Duration} \times \text{Portfolio Value}}{200}$$
- *Example*: A manager of a $500 million [portfolio](../../Advanced%20Investments/An%20Asset%20Allocation%20Primer.md) seeks a target [duration](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%205/Key%20Rates%20O1s%20Durations%20and%20Hedging.md) of 6.
  - $$\text{Target Dollar Duration} = \frac{6 \times 500,   000,   000}{200} = 15,   000,   000$$

### 4.2 Comparing Target and Current Dollar Duration
- The current [dollar duration](../../Financial%20Engineering/A%20Guide%20to%20Duration%20DV01%20and%20Yield%20Curve.md) is calculated similarly:
 $\text{Current Dollar Duration} = \frac{\text{Current Duration} \times \text{Portfolio Value}}{200}$$
- *Example*: If the current [duration](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%205/Key%20Rates%20O1s%20Durations%20and%20Hedging.md) is 4 for the $500 million [portfolio](../../Advanced%20Investments/An%20Asset%20Allocation%20Primer.md):
  - $$\text{Current Dollar Duration} = \frac{4 \times 500,   000,   000}{200} = 10,   000,   000$$

### 4.3 Adjusting Dollar Duration with Futures
- The difference between the target and current dollar durations determines the dollar exposure required from the [futures](../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%203%20-%20Futures%20Markets/Futures%20Not%20Subject%20to%20Cash-And-Carry.md) position:
 $\text{Dollar Exposure from Futures} = \text{Target Dollar Duration} - \text{Current Dollar Duration}$$
- If the difference is positive,  [futures contracts](../../Financial%20Engineering/Mathematics%20of%20the%20Financial%20Markets.md) must be purchased to increase dollar exposure. If negative,  [futures contracts](../../Financial%20Engineering/Mathematics%20of%20the%20Financial%20Markets.md) must be sold to decrease dollar exposure.

## 5. Determining the Number of Futures Contracts

### 5.1 Dollar Duration of a Futures Contract
- The [dollar duration](../../Financial%20Engineering/A%20Guide%20to%20Duration%20DV01%20and%20Yield%20Curve.md) of a [futures](../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%203%20-%20Futures%20Markets/Futures%20Not%20Subject%20to%20Cash-And-Carry.md) contract is the sensitivity of its value to changes in [interest rates](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%202/Interest%20Rate%20Quotations.md).
- It is calculated as:
 $\text{Dollar Duration of Futures Contract} = \text{Dollar Duration of CTD Issue} \times \text{Conversion Factor for CTD Issue}$$
  - **CTD Issue**: The [cheapest-to-deliver](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%2015/Tba%20and%20Specified%20Pools%20Markets.md) bond for the [futures](../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%203%20-%20Futures%20Markets/Futures%20Not%20Subject%20to%20Cash-And-Carry.md) contract.
  - **Conversion Factor**: Adjusts for differences in coupon rates and maturities among deliverable bonds.

### 5.2 Calculating the Number of Futures Contracts
- The number of [futures contracts](../../Financial%20Engineering/Mathematics%20of%20the%20Financial%20Markets.md) required to achieve the target [dollar duration](../../Financial%20Engineering/A%20Guide%20to%20Duration%20DV01%20and%20Yield%20Curve.md) is given by:
 $\text{Number of Futures Contracts} = \frac{\text{Target Dollar Duration} - \text{Current Dollar Duration}}{\text{Dollar Duration per Futures Contract}}$$
- A positive result indicates that [futures contracts](../../Financial%20Engineering/Mathematics%20of%20the%20Financial%20Markets.md) must be purchased,  while a negative result indicates that [futures contracts](../../Financial%20Engineering/Mathematics%20of%20the%20Financial%20Markets.md) must be sold.

### 5.3 Example: Determining the Number of Contracts
- *Given*:
  - Target [Dollar Duration](../../Financial%20Engineering/A%20Guide%20to%20Duration%20DV01%20and%20Yield%20Curve.md) = $15,   000,   000$
  - Current [Dollar Duration](../../Financial%20Engineering/A%20Guide%20to%20Duration%20DV01%20and%20Yield%20Curve.md) = $10,   000,   000$
  - [Dollar Duration](../../Financial%20Engineering/A%20Guide%20to%20Duration%20DV01%20and%20Yield%20Curve.md) per [Futures](../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%203%20-%20Futures%20Markets/Futures%20Not%20Subject%20to%20Cash-And-Carry.md) Contract = $2,   100$
- *Calculation*:
 $\text{Number of Futures Contracts} = \frac{15,  000,  000 - 10,  000,  000}{2,  100} = 2,  381$$
- The manager must purchase 2,  381 [futures contracts](../../Financial%20Engineering/Mathematics%20of%20the%20Financial%20Markets.md) to achieve the target [dollar duration](../../Financial%20Engineering/A%20Guide%20to%20Duration%20DV01%20and%20Yield%20Curve.md).

## 6. Hedging with Interest-Rate Futures

### 6.1 Short Hedge
- A [short hedge](../../Financial%20Engineering/Derivatives/Part%20I%20-%20Forwards%20and%20Futures/Chapter%204%20-%20Futures:%20Hedging%20and%20Speculation.md) is used to protect against a decline in the cash price of a bond.
- [Futures contracts](../../Financial%20Engineering/Mathematics%20of%20the%20Financial%20Markets.md) are sold to lock in a selling price.
- *Example*: A [pension fund](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%2013/Uses%20of%20Interest%20Rate%20Swaps.md) manager expects to liquidate bonds in 40 days to make a $5 million payment. Selling [futures contracts](../../Financial%20Engineering/Mathematics%20of%20the%20Financial%20Markets.md) protects against rising [interest rates](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%202/Interest%20Rate%20Quotations.md),  which would lower bond prices.

### 6.2 Long Hedge
- A long hedge is used to protect against an increase in the cash price of a bond.
- [Futures contracts](../../Financial%20Engineering/Mathematics%20of%20the%20Financial%20Markets.md) are purchased to lock in a buying price.
- *Example*: A manager expects substantial cash contributions and anticipates falling [interest rates](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%202/Interest%20Rate%20Quotations.md). Buying [futures contracts](../../Financial%20Engineering/Mathematics%20of%20the%20Financial%20Markets.md) protects against rising bond prices.

### 6.3 Cross-Hedging
- Cross-[hedging](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%205/Key%20Rates%20O1s%20Durations%20and%20Hedging.md) occurs when the bond or [portfolio](../../Advanced%20Investments/An%20Asset%20Allocation%20Primer.md) to be hedged is not identical to the bond underlying the [futures](../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%203%20-%20Futures%20Markets/Futures%20Not%20Subject%20to%20Cash-And-Carry.md) contract.
- This introduces [basis risk](../../Financial%20Markets%20and%20Institutions/III.%20Liquidity%20of%20Assets/Class%208-%20Markets,%20Meltdowns,%20and%20Arbitrage/Lessons%20From%20The%20Crisis.md),  as the cash and [futures](../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%203%20-%20Futures%20Markets/Futures%20Not%20Subject%20to%20Cash-And-Carry.md) prices may not move perfectly together.

## 7. Monitoring and Evaluating the Hedge

### 7.1 Steps in the Hedging Process
1. **Determine the Appropriate [Hedging](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%205/Key%20Rates%20O1s%20Durations%20and%20Hedging.md) Instrument**:
   - Choose a [futures](../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%203%20-%20Futures%20Markets/Futures%20Not%20Subject%20to%20Cash-And-Carry.md) contract with a high correlation to the [interest rate risk](../Analysis%20of%20Fixed%20Income%20Securities.md) being hedged.
   - Consider [liquidity](../../Financial%20Markets%20and%20Institutions/III.%20Liquidity%20of%20Assets/Class%205-%20Private%20Information,%20Liquidity,%20and%20Securitization/Class%20Note%2010%20Liquidity%20and%20Class%20Note%2010%20Liquidity%20and%20Liquidity%20Managementliquidity%20management.md) and [delivery month](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%2012/One-Month%20SOFR%20Futures.md).
1. **Determine the Target for the Hedge**:
   - Establish the target rate or price to be locked in by the hedge.
1. **Determine the Position to Be Taken**:
   - Calculate the number of [futures contracts](../../Financial%20Engineering/Mathematics%20of%20the%20Financial%20Markets.md) required to achieve the target [dollar duration](../../Financial%20Engineering/A%20Guide%20to%20Duration%20DV01%20and%20Yield%20Curve.md).
1. **Monitor and Evaluate the Hedge**:
   - Adjust the [futures](../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%203%20-%20Futures%20Markets/Futures%20Not%20Subject%20to%20Cash-And-Carry.md) position as needed to maintain the target [dollar duration](../../Financial%20Engineering/A%20Guide%20to%20Duration%20DV01%20and%20Yield%20Curve.md) over time.

### 7.2 Risk and Expected Return in a Hedge
- The effectiveness of a hedge depends on the correlation between cash and [futures](../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%203%20-%20Futures%20Markets/Futures%20Not%20Subject%20to%20Cash-And-Carry.md) prices.
- The manager's objective is to "lock in" a rate or price,  but the actual outcome may vary due to [basis risk](../../Financial%20Markets%20and%20Institutions/III.%20Liquidity%20of%20Assets/Class%208-%20Markets,%20Meltdowns,%20and%20Arbitrage/Lessons%20From%20The%20Crisis.md) and delivery options.

## 8. Summary and Key Takeaways

- Interest-rate [futures](../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%203%20-%20Futures%20Markets/Futures%20Not%20Subject%20to%20Cash-And-Carry.md) provide a cost-effective and flexible tool for managing interest-rate risk.
- The key to controlling interest-rate risk is to align the [portfolio](../../Advanced%20Investments/An%20Asset%20Allocation%20Primer.md)'s [dollar duration](../../Financial%20Engineering/A%20Guide%20to%20Duration%20DV01%20and%20Yield%20Curve.md) with the target [dollar duration](../../Financial%20Engineering/A%20Guide%20to%20Duration%20DV01%20and%20Yield%20Curve.md) using [futures contracts](../../Financial%20Engineering/Mathematics%20of%20the%20Financial%20Markets.md).
- The number of [futures contracts](../../Financial%20Engineering/Mathematics%20of%20the%20Financial%20Markets.md) required is determined by the difference between the target and current dollar durations,  divided by the [dollar duration](../../Financial%20Engineering/A%20Guide%20to%20Duration%20DV01%20and%20Yield%20Curve.md) per [futures](../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%203%20-%20Futures%20Markets/Futures%20Not%20Subject%20to%20Cash-And-Carry.md) contract.
- [Hedging](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%205/Key%20Rates%20O1s%20Durations%20and%20Hedging.md) strategies,  including short and long hedges,  allow managers to protect against adverse interest rate movements.
- Monitoring and adjusting the hedge over time ensures that the [portfolio](../../Advanced%20Investments/An%20Asset%20Allocation%20Primer.md) remains aligned with its [investment](../../Advanced%20Investments/An%20Asset%20Allocation%20Primer.md) objectives.

By mastering these principles and techniques,  [portfolio](../../Advanced%20Investments/An%20Asset%20Allocation%20Primer.md) managers can effectively manage interest-rate risk and optimize [portfolio](../../Advanced%20Investments/An%20Asset%20Allocation%20Primer.md) performance.

# Lecture Notes: Hedging with Treasury Bond Futures and Basis Risk

## 1. Introduction to Hedging with Treasury Bond Futures

- Treasury bond [futures](../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%203%20-%20Futures%20Markets/Futures%20Not%20Subject%20to%20Cash-And-Carry.md) are widely used by [portfolio](../../Advanced%20Investments/An%20Asset%20Allocation%20Primer.md) managers to hedge [interest rate risk](../Analysis%20of%20Fixed%20Income%20Securities.md) and lock in effective sale or purchase prices for fixed-income securities.
- This lecture focuses on:
  - The mechanics of [hedging](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%205/Key%20Rates%20O1s%20Durations%20and%20Hedging.md) with Treasury bond [futures](../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%203%20-%20Futures%20Markets/Futures%20Not%20Subject%20to%20Cash-And-Carry.md).
  - The calculation of effective sale prices.
  - The role of [basis risk](../../Financial%20Markets%20and%20Institutions/III.%20Liquidity%20of%20Assets/Class%208-%20Markets,%20Meltdowns,%20and%20Arbitrage/Lessons%20From%20The%20Crisis.md) in [hedging](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%205/Key%20Rates%20O1s%20Durations%20and%20Hedging.md).
  - The determination of the number of [futures contracts](../../Financial%20Engineering/Mathematics%20of%20the%20Financial%20Markets.md) required for a hedge.
  - A detailed example of cross-[hedging](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%205/Key%20Rates%20O1s%20Durations%20and%20Hedging.md) a non-deliverable bond using Treasury bond [futures](../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%203%20-%20Futures%20Markets/Futures%20Not%20Subject%20to%20Cash-And-Carry.md).

## 2. Mechanics of Hedging with Treasury Bond Futures

### 2.1 Effective Sale Price of Treasury Bonds

- The effective sale price of a Treasury bond is determined by combining the actual sale price of the bond with the gain or loss on the [futures](../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%203%20-%20Futures%20Markets/Futures%20Not%20Subject%20to%20Cash-And-Carry.md) position.
- **Formula**:
 $\text{Effective Sale Price} = \text{Actual Sale Price of Treasury Bond} + \text{Gain or Loss on Futures Position}$$

- **Example**:
  - Actual sale price of Treasury bond: \$140,  000,  000.
  - Gain on [futures](../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%203%20-%20Futures%20Markets/Futures%20Not%20Subject%20to%20Cash-And-Carry.md) position: \$4,  979,  000.
  - Effective sale price:
	$$\text{Effective Sale Price} = 140,   000,   000 + 4,   979,   000 = 144,   979,   000$$

- The effective sale price reflects the target price dictated by the [futures](../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%203%20-%20Futures%20Markets/Futures%20Not%20Subject%20to%20Cash-And-Carry.md) rate when the hedge is set.

### 2.2 Convergence at Delivery Date

- If a hedge is held until the delivery date of the [futures](../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%203%20-%20Futures%20Markets/Futures%20Not%20Subject%20to%20Cash-And-Carry.md) contract,  the spot price of the bond and the [futures price](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%2011/Futures%20Price%20and%20the%20Quality%20Option%20Before%20E.md) converge.
- This ensures that the effective sale price is locked in at the [futures](../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%203%20-%20Futures%20Markets/Futures%20Not%20Subject%20to%20Cash-And-Carry.md) rate set when the hedge was established.

### 2.3 Short-Term Hedges

- For hedges lifted prior to the delivery date,  the effective rate or price is more likely to approximate the current [spot rate](../../International%20Finance/The%20Foreign%20Exchange%20Market%20Annotations.md) rather than the [futures](../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%203%20-%20Futures%20Markets/Futures%20Not%20Subject%20to%20Cash-And-Carry.md) rate.
- The shorter the hedge [duration](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%205/Key%20Rates%20O1s%20Durations%20and%20Hedging.md),  the less likely convergence will occur,  and the effective rate will reflect the one-day [forward rate](../../Clippings/Forward%20Points%20in%20Currency.md),  which is nearly equal to the [spot rate](../../International%20Finance/The%20Foreign%20Exchange%20Market%20Annotations.md).

## 3. Basis and Basis Risk in Hedging

### 3.1 Definition of Basis

- The **basis** is the difference between the spot price of a security and its [futures price](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%2011/Futures%20Price%20and%20the%20Quality%20Option%20Before%20E.md).
- **Price Basis**:
 $\text{Price Basis} = \text{Spot Price} - \text{Futures Delivery Price}$$
- **Rate Basis**:
 $\text{Rate Basis} = \text{Spot Rate} - \text{Futures Rate}$$

### 3.2 Target Basis and Basis Risk

- The **target basis** is the expected basis on the day the hedge is lifted.
- **Hedge to Delivery Date**:
  - The target basis is zero due to convergence.
  - The target rate equals the [futures](../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%203%20-%20Futures%20Markets/Futures%20Not%20Subject%20to%20Cash-And-Carry.md) rate.
- **Hedge Lifted Before Delivery**:
  - The target basis is the current basis,  which introduces uncertainty.
  - The target rate equals the [futures](../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%203%20-%20Futures%20Markets/Futures%20Not%20Subject%20to%20Cash-And-Carry.md) rate plus the target rate basis.
- **[Basis Risk](../../Financial%20Markets%20and%20Institutions/III.%20Liquidity%20of%20Assets/Class%208-%20Markets,%20Meltdowns,%20and%20Arbitrage/Lessons%20From%20The%20Crisis.md)**:
  - [Basis risk](../../Financial%20Markets%20and%20Institutions/III.%20Liquidity%20of%20Assets/Class%208-%20Markets,%20Meltdowns,%20and%20Arbitrage/Lessons%20From%20The%20Crisis.md) refers to the uncertainty surrounding the target basis on the day the hedge is lifted.
  - It arises from unpredictable changes in the relationship between cash and [futures](../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%203%20-%20Futures%20Markets/Futures%20Not%20Subject%20to%20Cash-And-Carry.md) prices.

## 4. Determining the Number of Futures Contracts

### 4.1 Hedge Ratio

- The [hedge ratio](../../Financial%20Engineering/Derivatives/Part%20VI%20-%20The%20Greeks/Chapter%2027%20-%20Delta%20Hedging.md) determines the number of [futures contracts](../../Financial%20Engineering/Mathematics%20of%20the%20Financial%20Markets.md) required to offset the risk of the position being hedged.
- **Formula**:
 $\text{Number of Futures Contracts} = \frac{\text{Current Dollar Duration Without Futures}}{\text{Dollar Duration per Futures Contract}}$$

### 4.2 Cross-Hedging

- Cross-[hedging](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%205/Key%20Rates%20O1s%20Durations%20and%20Hedging.md) occurs when the security to be hedged is not deliverable on the [futures](../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%203%20-%20Futures%20Markets/Futures%20Not%20Subject%20to%20Cash-And-Carry.md) contract used in the hedge.
- The number of [futures contracts](../../Financial%20Engineering/Mathematics%20of%20the%20Financial%20Markets.md) for a cross-hedge is determined by the relative dollar durations of the bond to be hedged and the [cheapest-to-deliver](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%2015/Tba%20and%20Specified%20Pools%20Markets.md) (CTD) issue.
- **Formula**:
 $\text{Number of Futures Contracts} = \frac{\text{Current Dollar Duration Without Futures}}{\text{Dollar Duration of CTD Issue}} \times \text{Conversion Factor for CTD Issue}$$

## 5. Example: Cross-Hedging a Non-Deliverable Bond

### 5.1 Problem Setup

- **Bond to be Hedged**:
  - \$10 million par value of a 6.25% FNMA bond maturing on 5/15/2029.
  - Current price: 88.39.
  - Current yield: 7.20%.
- **[Futures](../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%203%20-%20Futures%20Markets/Futures%20Not%20Subject%20to%20Cash-And-Carry.md) Contract**:
  - September 1999 Treasury bond [futures](../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%203%20-%20Futures%20Markets/Futures%20Not%20Subject%20to%20Cash-And-Carry.md).
  - [Futures price](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%2011/Futures%20Price%20and%20the%20Quality%20Option%20Before%20E.md): 113.
  - CTD issue: 11.25% Treasury bond maturing on 2/15/2015.
  - CTD price: 146.19.
  - CTD yield: 6.50%.
  - Conversion factor for CTD issue: 1.283.
- **Assumptions**:
  - Yield spread between FNMA bond and CTD issue remains constant at 70 basis points.
  - Anticipated sale date: Last business day of September 1999.

### 5.2 Target Levels

- **Target Yield for CTD Issue**:
  - [Futures price](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%2011/Futures%20Price%20and%20the%20Quality%20Option%20Before%20E.md) × Conversion factor = Target price for CTD issue.
  - $$\text{Target Price for CTD Issue} = 113 \times 1.283 = 144.979$$
  - Yield corresponding to target price: 6.56%.
- **Target Yield for FNMA Bond**:
  - $$\text{Target Yield for FNMA Bond} = 6.56\% + 0.70\% = 7.26\%$$
  - Price corresponding to target yield: 87.76.

### 5.3 Dollar Durations

- **[Dollar Duration](../../Financial%20Engineering/A%20Guide%20to%20Duration%20DV01%20and%20Yield%20Curve.md) of FNMA Bond**:
  - [Dollar duration](../../Financial%20Engineering/A%20Guide%20to%20Duration%20DV01%20and%20Yield%20Curve.md) per \$100 par value: \$5.453.
  - Total [dollar duration](../../Financial%20Engineering/A%20Guide%20to%20Duration%20DV01%20and%20Yield%20Curve.md):
	$$\text{Dollar Duration of FNMA Bond} = \frac{\$10,   000,   000}{100} \times 5.453 = 545,   300$$

- **[Dollar Duration](../../Financial%20Engineering/A%20Guide%20to%20Duration%20DV01%20and%20Yield%20Curve.md) of CTD Issue**:
  - [Dollar duration](../../Financial%20Engineering/A%20Guide%20to%20Duration%20DV01%20and%20Yield%20Curve.md) per \$100 par value: \$6.255.
  - [Dollar duration](../../Financial%20Engineering/A%20Guide%20to%20Duration%20DV01%20and%20Yield%20Curve.md) per [futures](../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%203%20-%20Futures%20Markets/Futures%20Not%20Subject%20to%20Cash-And-Carry.md) contract:
	$$\text{Dollar Duration per Futures Contract} = \frac{\$100,   000}{100} \times 6.255 = 6,   255$$

### 5.4 Number of Futures Contracts

- **Formula**:
 $\text{Number of Futures Contracts} = \frac{\text{Dollar Duration of FNMA Bond}}{\text{Dollar Duration of CTD Issue}} \times \text{Conversion Factor for CTD Issue}$$

- **Calculation**:
 $\text{Number of Futures Contracts} = \frac{545,  300}{6,  255} \times 1.283 = 112$$

- **Result**:
  - To hedge the FNMA bond position,  112 Treasury bond [futures contracts](../../Financial%20Engineering/Mathematics%20of%20the%20Financial%20Markets.md) must be shorted.

### 5.5 Scenario Analysis

- Exhibit 63-2 provides a [scenario analysis](../../Advanced%20Financial%20Analysis%20and%20Valuation/Lecture%20Notes%20Advanced%20Financial%20Analysis%20and%20Valuation/Week%204%20Advanced%20Financial%20Analysis%20and%20Valuation/Week%204%20Valuing%20Young%20and%20High‐Growth%20Companies.md) of the hedge outcome based on different sale prices for the FNMA bond at the delivery date of the [futures](../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%203%20-%20Futures%20Markets/Futures%20Not%20Subject%20to%20Cash-And-Carry.md) contract.

#### Key Observations
1. The effective sale price for the FNMA bond remains close to the target price of \$8,  776,  000 across various scenarios.
1. Gains or losses on the [futures](../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%203%20-%20Futures%20Markets/Futures%20Not%20Subject%20to%20Cash-And-Carry.md) position offset changes in the actual sale price of the FNMA bond,  stabilizing the effective sale price.

## 6. Summary and Key Takeaways

- Treasury bond [futures](../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%203%20-%20Futures%20Markets/Futures%20Not%20Subject%20to%20Cash-And-Carry.md) are effective tools for [hedging interest rate risk](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%205/Multi-Factor%20Exposures%20and%20Portfolio%20Volatility.md) and locking in target sale or purchase prices.
- The effective sale price of a bond is determined by combining the actual sale price with the gain or loss on the [futures](../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%203%20-%20Futures%20Markets/Futures%20Not%20Subject%20to%20Cash-And-Carry.md) position.
- [Basis risk](../../Financial%20Markets%20and%20Institutions/III.%20Liquidity%20of%20Assets/Class%208-%20Markets,%20Meltdowns,%20and%20Arbitrage/Lessons%20From%20The%20Crisis.md) arises from uncertainty about the target basis on the day the hedge is lifted and is a key consideration in [hedging](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%205/Key%20Rates%20O1s%20Durations%20and%20Hedging.md) strategies.
- The number of [futures contracts](../../Financial%20Engineering/Mathematics%20of%20the%20Financial%20Markets.md) required for a hedge depends on the relative dollar durations of the bond to be hedged and the CTD issue.
- Cross-[hedging](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%205/Key%20Rates%20O1s%20Durations%20and%20Hedging.md) introduces additional complexity but can be effectively managed by carefully calculating the [hedge ratio](../../Financial%20Engineering/Derivatives/Part%20VI%20-%20The%20Greeks/Chapter%2027%20-%20Delta%20Hedging.md) and monitoring [basis risk](../../Financial%20Markets%20and%20Institutions/III.%20Liquidity%20of%20Assets/Class%208-%20Markets,%20Meltdowns,%20and%20Arbitrage/Lessons%20From%20The%20Crisis.md).

By understanding these principles and applying them rigorously,  [portfolio](../../Advanced%20Investments/An%20Asset%20Allocation%20Primer.md) managers can effectively manage [interest rate risk](../Analysis%20of%20Fixed%20Income%20Securities.md) and achieve their [investment](../../Advanced%20Investments/An%20Asset%20Allocation%20Primer.md) objectives.

# Lecture Notes: Hedging with Futures and Options in Fixed Income Markets

## 1. Introduction to Hedging with Futures and Options

- [Hedging](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%205/Key%20Rates%20O1s%20Durations%20and%20Hedging.md) is a critical [risk management](../../Financial%20Engineering/Financial%20Mathematics%20Course.md) strategy in [fixed income markets](../../Financial%20Engineering/A%20Practical%20Guide%20to%20Bonds%20and%20Swaps.md),  allowing [portfolio](../../Advanced%20Investments/An%20Asset%20Allocation%20Primer.md) managers to mitigate the impact of adverse interest rate movements on bond portfolios.
- This lecture focuses on:
  - [Hedging](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%205/Key%20Rates%20O1s%20Durations%20and%20Hedging.md) with Treasury bond [futures](../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%203%20-%20Futures%20Markets/Futures%20Not%20Subject%20to%20Cash-And-Carry.md),  including the mechanics,  [basis risk](../../Financial%20Markets%20and%20Institutions/III.%20Liquidity%20of%20Assets/Class%208-%20Markets,%20Meltdowns,%20and%20Arbitrage/Lessons%20From%20The%20Crisis.md),  and the calculation of effective sale prices.
  - Advanced refinements in [hedging](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%205/Key%20Rates%20O1s%20Durations%20and%20Hedging.md) strategies,  such as adjusting for changing yield spreads and incorporating yield beta.
  - [Hedging](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%205/Key%20Rates%20O1s%20Durations%20and%20Hedging.md) with options,  including [protective put](../../Financial%20Engineering/Derivatives/Part%20VI%20-%20The%20Greeks/Chapter%2029%20-%20Portfolio%20Insurance.md)-buying,  [covered call](../../Financial%20Engineering/Derivatives/Part%20IV%20-%20Options/Chapter%2018%20-%20Stock%20Options%20and%20Stock%20Index%20Options.md)-writing,  and collar strategies.
  - A detailed comparison of [futures](../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%203%20-%20Futures%20Markets/Futures%20Not%20Subject%20to%20Cash-And-Carry.md) and options [hedging](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%205/Key%20Rates%20O1s%20Durations%20and%20Hedging.md) strategies,  including their respective advantages and limitations.

## 2. Hedging with Treasury Bond Futures

### 2.1 Mechanics of Hedging with Futures

#### 2.1.1 Effective Sale Price
- The **effective sale price** of a bond is determined by combining the actual sale price with the gain or loss on the [futures](../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%203%20-%20Futures%20Markets/Futures%20Not%20Subject%20to%20Cash-And-Carry.md) position.
- **Formula**:
 $\text{Effective Sale Price} = \text{Actual Sale Price of Bond} + \text{Gain or Loss on Futures Position}$$
- Example:
  - Actual sale price of FNMA bond: \$8,  000,  000.
  - Gain on [futures](../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%203%20-%20Futures%20Markets/Futures%20Not%20Subject%20to%20Cash-And-Carry.md) position: \$800,  150.
  - Effective sale price:
	$$\text{Effective Sale Price} = 8,   000,   000 + 800,   150 = 8,   800,   150$$

#### 2.1.2 Convergence at Delivery Date
- By the delivery date of the [futures](../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%203%20-%20Futures%20Markets/Futures%20Not%20Subject%20to%20Cash-And-Carry.md) contract,  the [futures price](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%2011/Futures%20Price%20and%20the%20Quality%20Option%20Before%20E.md) converges with the price of the [cheapest-to-deliver](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%2015/Tba%20and%20Specified%20Pools%20Markets.md) (CTD) issue divided by its conversion factor.
- This ensures that the effective sale price is locked in at the [futures](../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%203%20-%20Futures%20Markets/Futures%20Not%20Subject%20to%20Cash-And-Carry.md) rate set at the inception of the hedge.

#### 2.1.3 Value of Futures Position
- The value of the [futures](../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%203%20-%20Futures%20Markets/Futures%20Not%20Subject%20to%20Cash-And-Carry.md) position is calculated as:
 $\text{Value of Futures Position} = \left(\frac{\text{Futures Price}}{100}\right) \times 100,  000 \times \text{Number of Futures Contracts}$$
- Example:
  - Final [futures price](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%2011/Futures%20Price%20and%20the%20Quality%20Option%20Before%20E.md): 105.85581.
  - Number of [futures contracts](../../Financial%20Engineering/Mathematics%20of%20the%20Financial%20Markets.md): 112.
  - Value of [futures](../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%203%20-%20Futures%20Markets/Futures%20Not%20Subject%20to%20Cash-And-Carry.md) position:
	$$\text{Value of Futures Position} = \left(\frac{105.85581}{100}\right) \times 100,   000 \times 112 = 11,   855,   850$$

#### 2.1.4 Gain or Loss on Futures Position
- The gain or loss on the [futures](../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%203%20-%20Futures%20Markets/Futures%20Not%20Subject%20to%20Cash-And-Carry.md) position is calculated as:
 $\text{Gain or Loss} = \left(\frac{\text{Initial Futures Price} - \text{Final Futures Price}}{100}\right) \times 100,  000 \times \text{Number of Futures Contracts}$$
- Example:
  - Initial [futures price](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%2011/Futures%20Price%20and%20the%20Quality%20Option%20Before%20E.md): 113.
  - Final [futures price](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%2011/Futures%20Price%20and%20the%20Quality%20Option%20Before%20E.md): 105.85581.
  - Number of [futures contracts](../../Financial%20Engineering/Mathematics%20of%20the%20Financial%20Markets.md): 112.
  - Gain:
	$$\text{Gain} = \left(\frac{113 - 105.85581}{100}\right) \times 100,   000 \times 112 = 800,   150$$

### 2.2 Basis and Basis Risk

#### 2.2.1 Definition of Basis
- The **basis** is the difference between the spot price of a bond and its [futures price](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%2011/Futures%20Price%20and%20the%20Quality%20Option%20Before%20E.md).
- **Price Basis**:
 $\text{Price Basis} = \text{Spot Price} - \text{Futures Delivery Price}$$
- **Rate Basis**:
 $\text{Rate Basis} = \text{Spot Rate} - \text{Futures Rate}$$

#### 2.2.2 Basis Risk
- **[Basis risk](../../Financial%20Markets%20and%20Institutions/III.%20Liquidity%20of%20Assets/Class%208-%20Markets,%20Meltdowns,%20and%20Arbitrage/Lessons%20From%20The%20Crisis.md)** arises from uncertainty about the target basis on the day the hedge is lifted.
- If the hedge is lifted before the delivery date,  the target basis is the current basis,  introducing uncertainty into the effective sale price.

### 2.3 Refining the Hedge for Changing Yield Spreads

#### 2.3.1 Yield Beta
- Yield beta ($b$) measures the relative yield change between the bond to be hedged and the CTD issue.
- **Regression Equation**:
 $\text{Yield on Bond to Be Hedged} = a + b \times \text{Yield on CTD Issue} + \text{Error}$$
- Example:
  - If $b = 1.05$,  the yield on the FNMA bond is expected to move 5% more than the yield on the CTD issue.

#### 2.3.2 Adjusting the Number of Futures Contracts
- The number of [futures contracts](../../Financial%20Engineering/Mathematics%20of%20the%20Financial%20Markets.md) is adjusted to account for yield beta:
 $\text{Number of Futures Contracts} = \frac{\text{Current Dollar Duration Without Futures}}{\text{Dollar Duration of CTD Issue}} \times \text{Conversion Factor for CTD Issue} \times \text{Yield Beta}$$
- Example:
  - Original number of contracts: 112.
  - Yield beta: 1.05.
  - Adjusted number of contracts:
	$$\text{Adjusted Number of Contracts} = 112 \times 1.05 = 118$$

## 3. Hedging with Options

### 3.1 Protective Put-Buying Strategy

#### 3.1.1 Overview
- A **[protective put](../../Financial%20Engineering/Derivatives/Part%20VI%20-%20The%20Greeks/Chapter%2029%20-%20Portfolio%20Insurance.md)-buying strategy** involves purchasing put options to hedge against rising [interest rates](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%202/Interest%20Rate%20Quotations.md).
- This strategy combines a [long position](../../Financial%20Engineering/Derivatives/Part%20I%20-%20Forwards%20and%20Futures/Chapter%204%20-%20Futures:%20Hedging%20and%20Speculation.md) in a bond with a [long position](../../Financial%20Engineering/Derivatives/Part%20I%20-%20Forwards%20and%20Futures/Chapter%204%20-%20Futures:%20Hedging%20and%20Speculation.md) in a put option,  providing [downside protection](../../Financial%20Engineering/Fixed%20Income%20Derivatives/Equity%20Linked%20Note.md) while retaining upside potential.

#### 3.1.2 Mechanics
- If [interest rates](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%202/Interest%20Rate%20Quotations.md) rise,  the value of the put option increases,  offsetting losses on the bond.
- If [interest rates](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%202/Interest%20Rate%20Quotations.md) fall,  the bond appreciates,  but the cost of the put option reduces the net gain.

#### 3.1.3 Example
- A manager holds \$10 million par value of a 6.25% FNMA bond and wants to establish a minimum price of 84.453.
- The equivalent [strike price](../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%205%20Options%20on%20Prices%20and%20Hedge-Based%20Valuation/Call%20and%20Put%20Payoffs%20at%20Expiry.md) for a Treasury bond [futures](../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%203%20-%20Futures%20Markets/Futures%20Not%20Subject%20to%20Cash-And-Carry.md) put option is calculated using:
  - The price-yield relationship for the FNMA bond.
  - The yield spread between the FNMA bond and the CTD issue.
  - The conversion factor for the CTD issue.

### 3.2 Covered Call-Writing Strategy

#### 3.2.1 Overview
- A **[covered call](../../Financial%20Engineering/Derivatives/Part%20IV%20-%20Options/Chapter%2018%20-%20Stock%20Options%20and%20Stock%20Index%20Options.md)-writing strategy** involves selling call options against a bond [portfolio](../../Advanced%20Investments/An%20Asset%20Allocation%20Primer.md) to generate premium income.
- This strategy reduces downside risk but limits upside potential.

#### 3.2.2 Mechanics
- If [interest rates](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%202/Interest%20Rate%20Quotations.md) rise,  the premium received cushions the loss on the bond [portfolio](../../Advanced%20Investments/An%20Asset%20Allocation%20Primer.md).
- If [interest rates](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%202/Interest%20Rate%20Quotations.md) fall,  the call option becomes a liability,  capping the [portfolio](../../Advanced%20Investments/An%20Asset%20Allocation%20Primer.md)'s gains.

### 3.3 Collar Strategy

#### 3.3.1 Overview
- A **collar strategy** combines a [protective put](../../Financial%20Engineering/Derivatives/Part%20VI%20-%20The%20Greeks/Chapter%2029%20-%20Portfolio%20Insurance.md)-buying strategy with a [covered call](../../Financial%20Engineering/Derivatives/Part%20IV%20-%20Options/Chapter%2018%20-%20Stock%20Options%20and%20Stock%20Index%20Options.md)-writing strategy.
- This involves purchasing a put option and selling a call option,  both out-of-the-money,  to create a range of protection.

#### 3.3.2 Mechanics
- The collar limits downside risk while capping upside potential.
- Within the range defined by the strike prices,  the [portfolio](../../Advanced%20Investments/An%20Asset%20Allocation%20Primer.md)'s value varies with [interest rates](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%202/Interest%20Rate%20Quotations.md).

## 4. Comparing Futures and Options Hedging Strategies

### 4.1 Futures Hedging
- **Advantages**:
  - Simple to implement.
  - Locks in a target price or rate.
  - Low transaction costs.
- **Disadvantages**:
  - No flexibility to benefit from favorable rate movements.
  - Subject to [basis risk](../../Financial%20Markets%20and%20Institutions/III.%20Liquidity%20of%20Assets/Class%208-%20Markets,%20Meltdowns,%20and%20Arbitrage/Lessons%20From%20The%20Crisis.md).

### 4.2 Options Hedging
- **Advantages**:
  - Provides flexibility to benefit from favorable rate movements.
  - Limits downside risk.
- **Disadvantages**:
  - Higher cost due to option premiums.
  - Requires careful selection of strike prices and contracts.

## 5. Steps in Options Hedging

### 5.1 Determine the Best Hedging Vehicle
- Consider factors such as option price,  [liquidity](../../Financial%20Markets%20and%20Institutions/III.%20Liquidity%20of%20Assets/Class%205-%20Private%20Information,%20Liquidity,%20and%20Securitization/Class%20Note%2010%20Liquidity%20and%20Class%20Note%2010%20Liquidity%20and%20Liquidity%20Managementliquidity%20management.md),  and correlation with the bond to be hedged.

### 5.2 Find the Appropriate Strike Price
- Convert the [strike price](../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%205%20Options%20on%20Prices%20and%20Hedge-Based%20Valuation/Call%20and%20Put%20Payoffs%20at%20Expiry.md) of the option into an equivalent [strike price](../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%205%20Options%20on%20Prices%20and%20Hedge-Based%20Valuation/Call%20and%20Put%20Payoffs%20at%20Expiry.md) for the bond being hedged.

### 5.3 Determine the Number of Contracts
- Calculate the [hedge ratio](../../Financial%20Engineering/Derivatives/Part%20VI%20-%20The%20Greeks/Chapter%2027%20-%20Delta%20Hedging.md) to determine the number of options to buy or sell.

## 6. Summary and Key Takeaways

- [Hedging with futures](../../Financial%20Instruments/Financial%20Instruments%20PSET%20Solutions.md) and options provides [portfolio](../../Advanced%20Investments/An%20Asset%20Allocation%20Primer.md) managers with powerful tools to manage [interest rate risk](../Analysis%20of%20Fixed%20Income%20Securities.md).
- [Futures hedging](../../Financial%20Engineering/Derivatives/Part%20I%20-%20Forwards%20and%20Futures/Chapter%204%20-%20Futures:%20Hedging%20and%20Speculation.md) is straightforward and cost-effective but lacks flexibility and is subject to [basis risk](../../Financial%20Markets%20and%20Institutions/III.%20Liquidity%20of%20Assets/Class%208-%20Markets,%20Meltdowns,%20and%20Arbitrage/Lessons%20From%20The%20Crisis.md).
- Options [hedging](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%205/Key%20Rates%20O1s%20Durations%20and%20Hedging.md) offers flexibility and [downside protection](../../Financial%20Engineering/Fixed%20Income%20Derivatives/Equity%20Linked%20Note.md) but is more complex and costly.
- The choice of [hedging strategy](../../Financial%20Instruments/Lecture%20Notes-%20Financial%20Instruments/Teaching%20Note%203%20Swaps-%20Financial%20Instruments/The%20Value%20of%20the%20Swap%20Contract%20after%20Initiation.md) depends on the manager's market outlook and risk tolerance.
- Refinements such as adjusting for yield beta and monitoring yield spreads enhance the effectiveness of [hedging](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%205/Key%20Rates%20O1s%20Durations%20and%20Hedging.md) strategies.

By mastering these techniques,  [portfolio](../../Advanced%20Investments/An%20Asset%20Allocation%20Primer.md) managers can effectively mitigate [interest rate risk](../Analysis%20of%20Fixed%20Income%20Securities.md) and optimize [portfolio](../../Advanced%20Investments/An%20Asset%20Allocation%20Primer.md) performance.

# Lecture Notes: Hedging with Futures Options – Protective Put and Covered Call Strategies

## 1. Introduction to Hedging with Futures Options

- [Futures](../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%203%20-%20Futures%20Markets/Futures%20Not%20Subject%20to%20Cash-And-Carry.md) options provide a flexible and effective way to hedge [interest rate risk](../Analysis%20of%20Fixed%20Income%20Securities.md) in fixed-income portfolios.
- Two common strategies are:
  - **[Protective Put](../../Financial%20Engineering/Derivatives/Part%20VI%20-%20The%20Greeks/Chapter%2029%20-%20Portfolio%20Insurance.md)-Buying Strategy**: Protects against rising [interest rates](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%202/Interest%20Rate%20Quotations.md) while allowing for upside potential if rates fall.
  - **[Covered Call](../../Financial%20Engineering/Derivatives/Part%20IV%20-%20Options/Chapter%2018%20-%20Stock%20Options%20and%20Stock%20Index%20Options.md)-Writing Strategy**: Generates premium income while limiting upside potential in exchange for partial [downside protection](../../Financial%20Engineering/Fixed%20Income%20Derivatives/Equity%20Linked%20Note.md).
- This lecture will cover:
  - The mechanics of calculating the number of options contracts required for a hedge.
  - [Scenario analysis](../../Advanced%20Financial%20Analysis%20and%20Valuation/Lecture%20Notes%20Advanced%20Financial%20Analysis%20and%20Valuation/Week%204%20Advanced%20Financial%20Analysis%20and%20Valuation/Week%204%20Valuing%20Young%20and%20High‐Growth%20Companies.md) for [protective put](../../Financial%20Engineering/Derivatives/Part%20VI%20-%20The%20Greeks/Chapter%2029%20-%20Portfolio%20Insurance.md) and [covered call](../../Financial%20Engineering/Derivatives/Part%20IV%20-%20Options/Chapter%2018%20-%20Stock%20Options%20and%20Stock%20Index%20Options.md) strategies.
  - A comparison of the two strategies and their implications for [portfolio management](../../Financial%20Engineering/Fixed%20Income%20Derivatives/The%20Impact%20of%20Option%20Strategies%20in%20Financial%20%20Portfolios%20Performance.md).

## 2. Protective Put-Buying Strategy

### 2.1 Mechanics of Protective Put Hedging

#### 2.1.1 Calculating the Number of Options Contracts
- The [hedge ratio](../../Financial%20Engineering/Derivatives/Part%20VI%20-%20The%20Greeks/Chapter%2027%20-%20Delta%20Hedging.md) for options is determined using the following formula:
 $\text{Number of Options Contracts} = \frac{\text{Current Dollar Duration Without Options}}{\text{Dollar Duration of the CTD Issue}} \times \text{Conversion Factor for CTD Issue}$$
- **Inputs**:
  - Current [dollar duration](../../Financial%20Engineering/A%20Guide%20to%20Duration%20DV01%20and%20Yield%20Curve.md) without options: $$\$512,   320$$
  - [Dollar duration](../../Financial%20Engineering/A%20Guide%20to%20Duration%20DV01%20and%20Yield%20Curve.md) of the CTD issue: $$\$6.021$$
  - Conversion factor for the CTD issue: $$1.283$$
- **Calculation**:
 $\text{Number of Options Contracts} = \frac{\$512,  320}{\$6.021} \times 1.283 = 109 \,  \text{put options}$$
- **Interpretation**:
  - To hedge the FNMA bond position,  109 put options on Treasury bond [futures](../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%203%20-%20Futures%20Markets/Futures%20Not%20Subject%20to%20Cash-And-Carry.md) must be purchased.

#### 2.1.2 Cost of the Hedge
- Suppose the price of the put option with a [strike price](../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%205%20Options%20on%20Prices%20and%20Hedge-Based%20Valuation/Call%20and%20Put%20Payoffs%20at%20Expiry.md) of 110 is $$\$500$$ per contract.
- Total cost of the hedge:
 $\text{Cost of Hedge} = 109 \times \$500 = \$54,  500$$
- This cost is equivalent to $$0.545$$ per $$\$100$$ par value hedged.

### 2.2 Outcome of the Hedge

#### 2.2.1 Value of the Put Option Position
- The value of the put option position at expiration depends on whether the [futures price](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%2011/Futures%20Price%20and%20the%20Quality%20Option%20Before%20E.md) is below the [strike price](../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%205%20Options%20on%20Prices%20and%20Hedge-Based%20Valuation/Call%20and%20Put%20Payoffs%20at%20Expiry.md) of 110:
  - If the [futures price](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%2011/Futures%20Price%20and%20the%20Quality%20Option%20Before%20E.md) is **greater than or equal to 110**,  the options expire worthless,  and the value of the put option position is zero.
  - If the [futures price](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%2011/Futures%20Price%20and%20the%20Quality%20Option%20Before%20E.md) is **below 110**,  the options expire in the money,  and the value of the put option position is calculated as:
	$$\text{Value of Put Option Position} = \left(\frac{110}{100} - \frac{\text{Futures Price}}{100}\right) \times 100,   000 \times \text{Number of Put Options}$$

#### 2.2.2 Example Calculation
- **Scenario**:
  - Actual sale price of FNMA bond: $$\$8,   000,   000$$
  - [Futures price](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%2011/Futures%20Price%20and%20the%20Quality%20Option%20Before%20E.md): $$105.85581$$
  - Number of put options: $$109$$
- **Value of Put Option Position**:
 $\text{Value of Put Option Position} = \left(\frac{110}{100} - \frac{105.85581}{100}\right) \times 100,   000 \times 109 = \$45,  717$$
- **Effective Sale Price**:
 $\text{Effective Sale Price} = \text{Actual Sale Price} + \text{Value of Put Option Position} - \text{Cost of Hedge}$$
 $\text{Effective Sale Price} = 8,  000,  000 + 45,  717 - 54,  500 = 8,  397,  217$$

#### 2.2.3 Minimum Effective Sale Price
- The minimum effective sale price can be calculated before initiating the hedge:
 $\text{Minimum Effective Sale Price} = \text{Price of FNMA Bonds Equivalent to Futures Strike Price} - \text{Cost of Hedge}$$
  - Price of FNMA bonds equivalent to [futures](../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%203%20-%20Futures%20Markets/Futures%20Not%20Subject%20to%20Cash-And-Carry.md) [strike price](../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%205%20Options%20on%20Prices%20and%20Hedge-Based%20Valuation/Call%20and%20Put%20Payoffs%20at%20Expiry.md): $$84.453$$
  - Cost of hedge: $$0.545$$ per $$\$100$$ par value.
 $\text{Minimum Effective Sale Price} = 84.453 - 0.545 = 83.908$$
- **Interpretation**:
  - The effective sale price will never fall below $$83.908$$,  providing [downside protection](../../Financial%20Engineering/Fixed%20Income%20Derivatives/Equity%20Linked%20Note.md).

#### 2.2.4 Scenario Analysis
- Exhibit 63-8 provides a detailed [scenario analysis](../../Advanced%20Financial%20Analysis%20and%20Valuation/Lecture%20Notes%20Advanced%20Financial%20Analysis%20and%20Valuation/Week%204%20Advanced%20Financial%20Analysis%20and%20Valuation/Week%204%20Valuing%20Young%20and%20High‐Growth%20Companies.md) for the [protective put](../../Financial%20Engineering/Derivatives/Part%20VI%20-%20The%20Greeks/Chapter%2029%20-%20Portfolio%20Insurance.md) hedge,  showing the effective sale price under various [futures price](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%2011/Futures%20Price%20and%20the%20Quality%20Option%20Before%20E.md) scenarios.

## 3. Covered Call-Writing Strategy

### 3.1 Mechanics of Covered Call Writing

#### 3.1.1 Selling Call Options
- In a [covered call](../../Financial%20Engineering/Derivatives/Part%20IV%20-%20Options/Chapter%2018%20-%20Stock%20Options%20and%20Stock%20Index%20Options.md)-writing strategy,  the [portfolio](../../Advanced%20Investments/An%20Asset%20Allocation%20Primer.md) manager sells out-of-the-money call options against an existing bond [portfolio](../../Advanced%20Investments/An%20Asset%20Allocation%20Primer.md).
- **Assumptions**:
  - [Futures price](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%2011/Futures%20Price%20and%20the%20Quality%20Option%20Before%20E.md) at hedge initiation: $$113$$
  - [Strike price](../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%205%20Options%20on%20Prices%20and%20Hedge-Based%20Valuation/Call%20and%20Put%20Payoffs%20at%20Expiry.md) of call options: $$117$$
  - Price of call options: $$\$500$$ per contract
  - Number of call options sold: $$109$$
- **Proceeds from Sale of Call Options**:
 $\text{Proceeds} = 109 \times \$500 = \$54,  500$$

#### 3.1.2 Liability of Call Option Position
- The liability from the call option position depends on whether the [futures price](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%2011/Futures%20Price%20and%20the%20Quality%20Option%20Before%20E.md) exceeds the [strike price](../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%205%20Options%20on%20Prices%20and%20Hedge-Based%20Valuation/Call%20and%20Put%20Payoffs%20at%20Expiry.md) of 117:
  - If the [futures price](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%2011/Futures%20Price%20and%20the%20Quality%20Option%20Before%20E.md) is **less than or equal to 117**,  the liability is zero.
  - If the [futures price](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%2011/Futures%20Price%20and%20the%20Quality%20Option%20Before%20E.md) is **greater than 117**,  the liability is calculated as:
	$$\text{Liability} = \left(\frac{\text{Futures Price}}{100} - \frac{117}{100}\right) \times 100,   000 \times \text{Number of Call Options}$$

#### 3.1.3 Example Calculation
- **Scenario**:
  - Actual sale price of FNMA bond: $$\$9,   500,   000$$
  - [Futures price](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%2011/Futures%20Price%20and%20the%20Quality%20Option%20Before%20E.md): $$119.31255$$
  - Number of call options: $$109$$
- **Liability**:
 $\text{Liability} = \left(\frac{119.31255}{100} - \frac{117}{100}\right) \times 100,   000 \times 109 = \$252,  068$$
- **Effective Sale Price**:
 $\text{Effective Sale Price} = \text{Actual Sale Price} + \text{Proceeds from Sale of Call Options} - \text{Liability}$$
 $\text{Effective Sale Price} = 9,  500,  000 + 54,  500 - 252,  068 = 9,  302,  432$$

### 3.2 Maximum Effective Sale Price
- The maximum effective sale price can be calculated before initiating the hedge:
 $\text{Maximum Effective Sale Price} = \text{Price of Hedged Bond Corresponding to Strike Price} + \text{Premium Received}$$
  - Price of hedged bond corresponding to [strike price](../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%205%20Options%20on%20Prices%20and%20Hedge-Based%20Valuation/Call%20and%20Put%20Payoffs%20at%20Expiry.md): $$92.858$$
  - Premium received: $$0.545$$ per $$\$100$$ par value.
 $\text{Maximum Effective Sale Price} = 92.858 + 0.545 = 93.403$$
- **Interpretation**:
  - The effective sale price will never exceed $$93.403$$,  limiting upside potential.

#### 3.2.1 Scenario Analysis
- Exhibit 63-9 provides a detailed [scenario analysis](../../Advanced%20Financial%20Analysis%20and%20Valuation/Lecture%20Notes%20Advanced%20Financial%20Analysis%20and%20Valuation/Week%204%20Advanced%20Financial%20Analysis%20and%20Valuation/Week%204%20Valuing%20Young%20and%20High‐Growth%20Companies.md) for the [covered call](../../Financial%20Engineering/Derivatives/Part%20IV%20-%20Options/Chapter%2018%20-%20Stock%20Options%20and%20Stock%20Index%20Options.md)-writing strategy,  showing the effective sale price under various [futures price](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%2011/Futures%20Price%20and%20the%20Quality%20Option%20Before%20E.md) scenarios.

## 4. Comparison of Protective Put and Covered Call Strategies

### 4.1 Protective Put Strategy
- **Advantages**:
  - Provides full [downside protection](../../Financial%20Engineering/Fixed%20Income%20Derivatives/Equity%20Linked%20Note.md) if rates rise.
  - Allows for unlimited upside potential if rates fall.
- **Disadvantages**:
  - Requires an upfront cost (option premium).
  - Minimum effective sale price is reduced by the cost of the hedge.

### 4.2 Covered Call Strategy
- **Advantages**:
  - Generates premium income,  providing partial [downside protection](../../Financial%20Engineering/Fixed%20Income%20Derivatives/Equity%20Linked%20Note.md).
  - No upfront cost; instead,  the strategy generates cash inflow.
- **Disadvantages**:
  - Limits upside potential if rates fall.
  - Maximum effective sale price is capped by the [strike price](../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%205%20Options%20on%20Prices%20and%20Hedge-Based%20Valuation/Call%20and%20Put%20Payoffs%20at%20Expiry.md) of the call options.

## 5. Summary and Key Takeaways

- **[Protective Put Strategy](../../Financial%20Instruments/Lecture%20Notes-%20Financial%20Instruments/Teaching%20Note%204-Multiperiod%20Binomial%20Trees/Options%20Strategies%20Construction.md)**:
  - Best suited for investors seeking [downside protection](../../Financial%20Engineering/Fixed%20Income%20Derivatives/Equity%20Linked%20Note.md) while retaining upside potential.
  - The cost of the hedge reduces the minimum effective sale price.
- **[Covered Call](../../Financial%20Engineering/Derivatives/Part%20IV%20-%20Options/Chapter%2018%20-%20Stock%20Options%20and%20Stock%20Index%20Options.md) Strategy**:
  - Best suited for investors expecting stable [interest rates](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%202/Interest%20Rate%20Quotations.md) and seeking to generate additional income.
  - Limits upside potential in exchange for premium income.
- **[Scenario Analysis](../../Advanced%20Financial%20Analysis%20and%20Valuation/Lecture%20Notes%20Advanced%20Financial%20Analysis%20and%20Valuation/Week%204%20Advanced%20Financial%20Analysis%20and%20Valuation/Week%204%20Valuing%20Young%20and%20High‐Growth%20Companies.md)**:
  - Both strategies provide predictable outcomes under various interest rate scenarios,  allowing investors to align their [hedging](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%205/Key%20Rates%20O1s%20Durations%20and%20Hedging.md) approach with their market outlook and risk tolerance.

By understanding the mechanics and implications of these strategies,  [portfolio](../../Advanced%20Investments/An%20Asset%20Allocation%20Primer.md) managers can effectively manage [interest rate risk](../Analysis%20of%20Fixed%20Income%20Securities.md) and optimize [portfolio](../../Advanced%20Investments/An%20Asset%20Allocation%20Primer.md) performance.

# Lecture Notes: Hedging Strategies and Interest Rate Swaps

## 1. Introduction to Hedging Strategies and Interest Rate Swaps

- [Hedging](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%205/Key%20Rates%20O1s%20Durations%20and%20Hedging.md) strategies are essential tools for [managing interest rate risk](.md) in fixed-income portfolios. These strategies allow [portfolio](../../Advanced%20Investments/An%20Asset%20Allocation%20Primer.md) managers to mitigate the impact of adverse interest rate movements on bond portfolios.
- Interest rate swaps,  a type of derivative,  are widely used by [financial institutions](../../Financial%20Markets%20and%20Institutions/Financial%20Markets%20and%20Institutions%20Lecture%20Notes.md) to synthetically manage [interest rate exposure](../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20III%20THE%20PLAYERS/Chapter%2013%20-%20Banks%20Asset-Liability%20Management/Duration%20Gap%20Management.md),  especially when direct restructuring of assets and liabilities is not feasible.
- This lecture focuses on:
  - Comparing alternative [hedging](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%205/Key%20Rates%20O1s%20Durations%20and%20Hedging.md) strategies,  including [futures](../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%203%20-%20Futures%20Markets/Futures%20Not%20Subject%20to%20Cash-And-Carry.md),  protective puts,  and covered calls.
  - The mechanics and features of interest rate swaps.
  - The interpretation of swap positions as packages of forward contracts or cash market instruments.

## 2. Comparing Hedging Strategies: Futures,  Protective Puts,  and Covered Calls

### 2.1 Overview of Hedging Strategies

- **[Hedging with Futures](../../Financial%20Instruments/Financial%20Instruments%20PSET%20Solutions.md)**:
  - [Futures contracts](../../Financial%20Engineering/Mathematics%20of%20the%20Financial%20Markets.md) are used to lock in a target price or rate for a bond [portfolio](../../Advanced%20Investments/An%20Asset%20Allocation%20Primer.md).
  - This strategy substitutes [basis risk](../../Financial%20Markets%20and%20Institutions/III.%20Liquidity%20of%20Assets/Class%208-%20Markets,%20Meltdowns,%20and%20Arbitrage/Lessons%20From%20The%20Crisis.md) for price risk,  as the [futures price](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%2011/Futures%20Price%20and%20the%20Quality%20Option%20Before%20E.md) may not perfectly track the cash price of the bond being hedged.
- **[Protective Put](../../Financial%20Engineering/Derivatives/Part%20VI%20-%20The%20Greeks/Chapter%2029%20-%20Portfolio%20Insurance.md)-Buying Strategy**:
  - Involves purchasing put options to hedge against rising [interest rates](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%202/Interest%20Rate%20Quotations.md).
  - Provides [downside protection](../../Financial%20Engineering/Fixed%20Income%20Derivatives/Equity%20Linked%20Note.md) while retaining upside potential.
- **[Covered Call](../../Financial%20Engineering/Derivatives/Part%20IV%20-%20Options/Chapter%2018%20-%20Stock%20Options%20and%20Stock%20Index%20Options.md)-Writing Strategy**:
  - Involves selling call options against a bond [portfolio](../../Advanced%20Investments/An%20Asset%20Allocation%20Primer.md) to generate premium income.
  - Limits upside potential in exchange for partial [downside protection](../../Financial%20Engineering/Fixed%20Income%20Derivatives/Equity%20Linked%20Note.md).

### 2.2 Exhibit 63-10: Comparison of Alternative Strategies

#### Key Observations from Exhibit 63-10

- **Effective Sale Price with [Futures](../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%203%20-%20Futures%20Markets/Futures%20Not%20Subject%20to%20Cash-And-Carry.md) Hedge**:
  - Provides a relatively stable effective sale price across a range of actual sale prices.
  - Example: For an actual sale price of $8,   000,   000,    the effective sale price is $8,  800,  150.
- **Effective Sale Price with Protective Puts**:
  - Offers [downside protection](../../Financial%20Engineering/Fixed%20Income%20Derivatives/Equity%20Linked%20Note.md) but results in a lower effective sale price compared to [futures hedging](../../Financial%20Engineering/Derivatives/Part%20I%20-%20Forwards%20and%20Futures/Chapter%204%20-%20Futures:%20Hedging%20and%20Speculation.md).
  - Example: For an actual sale price of $8,   000,   000,    the effective sale price is $8,  397,  217.
- **Effective Sale Price with Covered Calls**:
  - Generates premium income but caps the upside potential.
  - Example: For an actual sale price of $8,   000,   000,    the effective sale price is $8,  054,  500.

#### Implications
- No single strategy is superior across all scenarios. Each strategy has its advantages and disadvantages,  depending on the manager's market outlook and risk tolerance.
- Managers must choose among [Probability Distributions](Lecture%201-%20[[Exercises) of [Returns](../../Financial%20Markets/Financial%20Asset%20Pricing%20Theory%20Overview/Chapter%203%20-%20%20Assets,%20Portfolios,%20and%20Arbitrage/Assets.md)|probability distribution]]s of outcomes rather than specific outcomes.

### 2.3 Key Takeaways on Hedging Strategies

- **[Futures Hedging](../../Financial%20Engineering/Derivatives/Part%20I%20-%20Forwards%20and%20Futures/Chapter%204%20-%20Futures:%20Hedging%20and%20Speculation.md)**:
  - Best suited for locking in a target price or rate.
  - Subject to [basis risk](../../Financial%20Markets%20and%20Institutions/III.%20Liquidity%20of%20Assets/Class%208-%20Markets,%20Meltdowns,%20and%20Arbitrage/Lessons%20From%20The%20Crisis.md) and delivery options embedded in [futures contracts](../../Financial%20Engineering/Mathematics%20of%20the%20Financial%20Markets.md).
- **[Protective Put Strategy](../../Financial%20Instruments/Lecture%20Notes-%20Financial%20Instruments/Teaching%20Note%204-Multiperiod%20Binomial%20Trees/Options%20Strategies%20Construction.md)**:
  - Provides full [downside protection](../../Financial%20Engineering/Fixed%20Income%20Derivatives/Equity%20Linked%20Note.md) but requires an upfront cost (option premium).
  - Retains upside potential.
- **[Covered Call](../../Financial%20Engineering/Derivatives/Part%20IV%20-%20Options/Chapter%2018%20-%20Stock%20Options%20and%20Stock%20Index%20Options.md) Strategy**:
  - Generates premium income but limits upside potential.
  - Entails more downside risk than protective puts.
- **Collar Strategy**:
  - Combines protective puts and covered calls to create a range of protection.
  - Eliminates part of the [portfolio](../../Advanced%20Investments/An%20Asset%20Allocation%20Primer.md)'s downside risk by giving up part of its upside potential.

## 3. Interest Rate Swaps: Mechanics and Features

### 3.1 Definition and Purpose

- An **[interest rate swap](../../Financial%20Engineering/Primer%20on%20Interest%20Rate%20Swaps.md)** is an agreement between two parties (counterparties) to exchange periodic interest payments based on a [notional principal](../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%204%20-%20Swap%20Markets/Fundamentals%20of%20Swaps.md) amount.
- The [notional principal](../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%204%20-%20Swap%20Markets/Fundamentals%20of%20Swaps.md) amount is not exchanged; it serves as the basis for calculating the interest payments.
- Swaps are used to:
  - Manage [interest rate risk](../Analysis%20of%20Fixed%20Income%20Securities.md).
  - Align the [duration](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%205/Key%20Rates%20O1s%20Durations%20and%20Hedging.md) of assets and liabilities.
  - Hedge against changes in [interest rates](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%202/Interest%20Rate%20Quotations.md).

### 3.2 Features of a Generic Swap

- **Fixed-Rate Payer and Floating-Rate Payer**:
  - One party agrees to pay a [fixed interest rate](../../Financial%20Engineering/Derivatives/Part%20VIII%20-%20Swaps/Chapter%2036%20-%20Currency%20Swaps.md) (fixed-rate payer) and receive a floating interest rate.
  - The other party agrees to pay a floating interest rate (floating-rate payer) and receive a [fixed interest rate](../../Financial%20Engineering/Derivatives/Part%20VIII%20-%20Swaps/Chapter%2036%20-%20Currency%20Swaps.md).
- **[Notional Principal](../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%204%20-%20Swap%20Markets/Fundamentals%20of%20Swaps.md) Amount**:
  - The dollar amount used to calculate interest payments.
  - Example: For a $50 million notional amount,    the fixed-rate payer pays $1.25 million every six months (5% × $50 million ÷ 2).
- **Floating Rate**:
  - Commonly based on benchmarks such as LIBOR,  Treasury bills,  or the [federal funds rate](../../International%20Finance/Economic%20Stabilization%20Notes/Topics%20in%20Fiscal%20and%20Monetary%20Policies%20and%20Stabilization-%20Empirical%20Issues.md).
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
  - Floating-rate payer pays [Basis Swap](A%20Guide%20to%20the%20Front%20End%20and%20[[Basis%20Swaps) Markets#[London Interbank Offered Rate](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%2012/Short-Term%20Rates%20and%20the%20Transition%20from%20LIBOR.md) (LIBOR)|LIBOR]] × $50 million ÷ 2.
  - Example: If [Basis Swap](A%20Guide%20to%20the%20Front%20End%20and%20[[Basis%20Swaps) Markets#[London Interbank Offered Rate](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%2012/Short-Term%20Rates%20and%20the%20Transition%20from%20LIBOR.md) (LIBOR)|LIBOR]] = 3%,  the floating-rate payer pays $750,  000.

### 3.4 Swap Market Structure

- **Over-the-Counter (OTC) Market**:
  - Swaps are typically traded OTC between counterparties.
  - The [Dodd-Frank Act](Note%20on%20The%20[[Credit%20Derivative%20Indexes) and Its Impact|[Dodd-Frank](../../Course%20Notes/HBR%20Notes/Note%20on%20The%20Dodd-Frank%20Act%20and%20Its%20Impact.md)]] Act introduced Swap Execution Facilities (SEFs) to centralize clearing for standardized swaps.
- **Customization**:
  - Swaps can be tailored to meet specific needs,  including unusual terms or indices.

## 4. Interpreting a Swap Position

### 4.1 Swap as a Package of Forward Contracts

- An [interest rate swap](../../Financial%20Engineering/Primer%20on%20Interest%20Rate%20Swaps.md) can be viewed as a package of [Basis Swap](A%20Guide%20to%20the%20Front%20End%20and%20[[Basis%20Swaps) Markets#[Forward Rate Agreements](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%2012/EURIBOR%20Forward%20Rate%20Agreements%20and%20Futures.md) (FRAs) [Overview](../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%201%20-%20Purpose%20and%20Structure%20of%20Financial%20Markets/Overview%20of%20Financial%20Markets.md)|[Forward Rate Agreements](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%2012/EURIBOR%20Forward%20Rate%20Agreements%20and%20Futures.md)]] (FRAs).
- **Advantages**:
  - Longer maturities: Swaps can extend beyond the maturities of typical forward contracts.
  - Transactional efficiency: A single [swap contract](../../Financial%20Instruments/Review%20Session%20Notes/Currency%20Swaps.md) replaces multiple forward contracts.

### 4.2 Swap as a Package of Cash Market Instruments

- A swap can also be interpreted as a combination of cash market instruments.
- **Example**:
  - Buy a $50 million floating-rate bond (pays [Basis Swap](A%20Guide%20to%20the%20Front%20End%20and%20[[Basis%20Swaps) Markets#[London Interbank Offered Rate](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%2012/Short-Term%20Rates%20and%20the%20Transition%20from%20LIBOR.md) (LIBOR)|LIBOR]] every six months).
  - Finance the purchase by borrowing $50 million at a fixed rate (5% annual interest).
  - **Net [Cash Flow](../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%201%20-%20Purpose%20and%20Structure%20of%20Financial%20Markets/Preview%20of%20the%20Book.md)**:
	- Inflows: [Basis Swap](A%20Guide%20to%20the%20Front%20End%20and%20[[Basis%20Swaps) Markets#[London Interbank Offered Rate](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%2012/Short-Term%20Rates%20and%20the%20Transition%20from%20LIBOR.md) (LIBOR)|LIBOR]] × $50 million ÷ 2.
	- Outflows: $1.25 million.
	- Net position: [Basis Swap](A%20Guide%20to%20the%20Front%20End%20and%20[[Basis%20Swaps) Markets#[London Interbank Offered Rate](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%2012/Short-Term%20Rates%20and%20the%20Transition%20from%20LIBOR.md) (LIBOR)|LIBOR]] × $50 million ÷ 2 - $1.25 million.
  - This is equivalent to the cash flows of a fixed-rate payer/floating-rate receiver.

### 4.3 Exhibit 64-1: Cash Flow Analysis

#### Cash Flow for a Five-Year Floating-Rate Bond Financed by Fixed-Rate Borrowing

| Six-Month Period | Floating-Rate Bond | Borrowing Cost | Net [Cash Flow](../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%201%20-%20Purpose%20and%20Structure%20of%20Financial%20Markets/Preview%20of%20the%20Book.md) |

| 0 | -$50 million      | +$50 million | $0 |

| 1 | [Basis Swap](A%20Guide%20to%20the%20Front%20End%20and%20[[Basis%20Swaps) Markets#[London Interbank Offered Rate](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%2012/Short-Term%20Rates%20and%20the%20Transition%20from%20LIBOR.md) (LIBOR)|LIBOR]] × $50 ÷ 2 | -$1.25 million | [Basis Swap](A%20Guide%20to%20the%20Front%20End%20and%20[[Basis%20Swaps) Markets#[London Interbank Offered Rate](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%2012/Short-Term%20Rates%20and%20the%20Transition%20from%20LIBOR.md) (LIBOR)|LIBOR]] × $50 ÷ 2 - $1.25 million |

| 2 | [Basis Swap](A%20Guide%20to%20the%20Front%20End%20and%20[[Basis%20Swaps) Markets#[London Interbank Offered Rate](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%2012/Short-Term%20Rates%20and%20the%20Transition%20from%20LIBOR.md) (LIBOR)|LIBOR]] × $50 ÷ 2 | -$1.25 million | [Basis Swap](A%20Guide%20to%20the%20Front%20End%20and%20[[Basis%20Swaps) Markets#[London Interbank Offered Rate](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%2012/Short-Term%20Rates%20and%20the%20Transition%20from%20LIBOR.md) (LIBOR)|LIBOR]] × $50 ÷ 2 - $1.25 million |

| … | … | … | … |

| 10 | [Basis Swap](A%20Guide%20to%20the%20Front%20End%20and%20[[Basis%20Swaps) Markets#[London Interbank Offered Rate](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%2012/Short-Term%20Rates%20and%20the%20Transition%20from%20LIBOR.md) (LIBOR)|LIBOR]] × $50 ÷ 2 + $50 million | -$51.25 million | [](../Fixed%20Income%20Lecture%20Notes/A%20Guide%20to%20the%20Front%20End%20and%20Basis%20Swap%20Markets.md#London%20Interbank%20Offered%20Rate%20(LIBOR)|LIBOR) × $50 ÷ 2 - $1.25 million |

#### Key Insight
- The net cash flows replicate the position of a fixed-rate payer/floating-rate receiver in a swap.

## 5. Summary and Key Takeaways

### 5.1 Hedging Strategies

- [Futures](../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%203%20-%20Futures%20Markets/Futures%20Not%20Subject%20to%20Cash-And-Carry.md),  protective puts,  and covered calls each offer unique advantages and disadvantages.
- The choice of strategy depends on the manager's market outlook and risk tolerance.
- [Futures hedging](../../Financial%20Engineering/Derivatives/Part%20I%20-%20Forwards%20and%20Futures/Chapter%204%20-%20Futures:%20Hedging%20and%20Speculation.md) locks in a target price or rate but introduces [basis risk](../../Financial%20Markets%20and%20Institutions/III.%20Liquidity%20of%20Assets/Class%208-%20Markets,%20Meltdowns,%20and%20Arbitrage/Lessons%20From%20The%20Crisis.md).
- Protective puts provide [downside protection](../../Financial%20Engineering/Fixed%20Income%20Derivatives/Equity%20Linked%20Note.md) but require an upfront cost.
- Covered calls generate premium income but limit upside potential.

### 5.2 Interest Rate Swaps

- Swaps are versatile tools for [managing interest rate risk](.md) and aligning the [duration](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%205/Key%20Rates%20O1s%20Durations%20and%20Hedging.md) of assets and liabilities.
- They can be interpreted as packages of forward contracts or cash market instruments.
- The [notional principal](../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%204%20-%20Swap%20Markets/Fundamentals%20of%20Swaps.md) amount is used to calculate interest payments but is not exchanged.
- Swaps are typically traded OTC,  with standardized contracts cleared through SEFs.

### 5.3 Practical Applications

- [Hedging with swaps](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%205/Partial%20O1s%20and%20PV01.md) allows institutions to synthetically manage [interest rate exposure](../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20III%20THE%20PLAYERS/Chapter%2013%20-%20Banks%20Asset-Liability%20Management/Duration%20Gap%20Management.md) without restructuring their asset and liability mix.
- Swaps provide flexibility in terms of maturity,  structure,  and indices,  making them suitable for a wide range of financial strategies.

By mastering these concepts,  [portfolio](../../Advanced%20Investments/An%20Asset%20Allocation%20Primer.md) managers can effectively manage [interest rate risk](../Analysis%20of%20Fixed%20Income%20Securities.md) and optimize [portfolio](../../Advanced%20Investments/An%20Asset%20Allocation%20Primer.md) performance.

# Lecture Notes: Interest Rate Swaps and Applications in Asset/Liability Management

## 1. Introduction to Interest Rate Swaps

- Interest rate swaps are [financial derivatives](../../Financial%20Instruments/Financial%20Instruments%20PSET%20Solutions.md) that allow counterparties to [exchange cash flows](../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%204%20-%20Swap%20Markets/Fundamentals%20of%20Swaps.md) based on a [notional principal](../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%204%20-%20Swap%20Markets/Fundamentals%20of%20Swaps.md) amount.
- These instruments are widely used in asset/liability management to manage [interest rate risk](../Analysis%20of%20Fixed%20Income%20Securities.md),  synthetically convert liabilities or assets,  and fine-tune the [duration](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%205/Key%20Rates%20O1s%20Durations%20and%20Hedging.md) of portfolios.
- This lecture will cover:
  - The mechanics of interest rate swaps.
  - The interpretation of swap positions as combinations of cash market instruments.
  - Applications of swaps in converting [floating-rate debt](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%2013/Uses%20of%20Interest%20Rate%20Swaps.md) to fixed-rate debt and vice versa.
  - Innovations in swap markets,  including basis swaps and other advanced instruments.

## 2. Mechanics of Interest Rate Swaps

### 2.1 Key Terminology

- **Trade Date**: The date on which the counterparties commit to the swap.
- **Effective Date**: The date the swap begins accruing interest.
- **Maturity Date**: The date the swap stops accruing interest.
- **Settlement Date**: The date on which cash flows are exchanged.

### 2.2 Structure of a Generic Swap

- **Fixed-Rate Payer**:
  - Pays a [fixed interest rate](../../Financial%20Engineering/Derivatives/Part%20VIII%20-%20Swaps/Chapter%2036%20-%20Currency%20Swaps.md).
  - Receives a floating interest rate (e.g.,  LIBOR).
  - This position is equivalent to being **short the bond market** because it benefits from rising [interest rates](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%202/Interest%20Rate%20Quotations.md).
- **Floating-Rate Payer**:
  - Pays a floating interest rate (e.g.,  LIBOR).
  - Receives a [fixed interest rate](../../Financial%20Engineering/Derivatives/Part%20VIII%20-%20Swaps/Chapter%2036%20-%20Currency%20Swaps.md).
  - This position is equivalent to being **long the bond market** because it benefits from falling [interest rates](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%202/Interest%20Rate%20Quotations.md).

### 2.3 Cash Flow Mechanics

- **Fixed-Rate Payer Example**:
  - [Notional principal](../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%204%20-%20Swap%20Markets/Fundamentals%20of%20Swaps.md): $50 million.
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
- This position benefits from rising [interest rates](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%202/Interest%20Rate%20Quotations.md) because the fixed-rate liability is locked in at a lower rate.

### 3.2 Floating-Rate Payer

- A floating-rate payer's position can be interpreted as:
  - **Long a fixed-rate bond**: Receives fixed-rate cash flows.
  - **Short a floating-rate bond**: Pays floating-rate cash flows.
- This position benefits from falling [interest rates](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%202/Interest%20Rate%20Quotations.md) because the floating-rate liability adjusts downward.

## 4. Applications of Interest Rate Swaps

### 4.1 Converting Floating-Rate Debt to Fixed-Rate Debt

- **Objective**: Lock in a fixed liability cost to mitigate the risk of rising [interest rates](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%202/Interest%20Rate%20Quotations.md).
- **Mechanism**:
  - Enter into a fixed-rate payer/floating-rate receiver swap.
  - The floating-rate liability is offset by the floating-rate inflow from the swap.
  - The net funding cost becomes the fixed rate of the swap.
- **Example**:
  - Floating-rate liability: 3-month [Basis Swap](A%20Guide%20to%20the%20Front%20End%20and%20[[Basis%20Swaps) Markets#[London Interbank Offered Rate](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%2012/Short-Term%20Rates%20and%20the%20Transition%20from%20LIBOR.md) (LIBOR)|LIBOR]] + 10 bps (3.10%).
  - Swap terms: Pay fixed at 3.40%,  receive floating at 3-month [Basis Swap](A%20Guide%20to%20the%20Front%20End%20and%20[[Basis%20Swaps) Markets#[London Interbank Offered Rate](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%2012/Short-Term%20Rates%20and%20the%20Transition%20from%20LIBOR.md) (LIBOR)|LIBOR]] (3.00%).
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
- **Exhibit 64-3**: Funding costs vary with [Basis Swap](A%20Guide%20to%20the%20Front%20End%20and%20[[Basis%20Swaps) Markets#[London Interbank Offered Rate](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%2012/Short-Term%20Rates%20and%20the%20Transition%20from%20LIBOR.md) (LIBOR)|LIBOR]] but maintain a consistent spread of 15 bps over LIBOR.

### 4.3 Basis Swaps

- **Objective**: Manage [basis risk](../../Financial%20Markets%20and%20Institutions/III.%20Liquidity%20of%20Assets/Class%208-%20Markets,%20Meltdowns,%20and%20Arbitrage/Lessons%20From%20The%20Crisis.md) when [asset returns](../../Financial%20Markets/Financial%20Asset%20Pricing%20Theory%20Overview/Chapter%201%20-%20Introduction%20and%20Overview/Some%20Stylized%20Empirical%20Facts%20About%20Asset%20Retur.md) and liability costs are based on different benchmarks.
- **Mechanism**:
  - Enter into a floating-to-floating [basis swap](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%2013/Basis%20Swaps.md).
  - Example: Receive prime - 150 bps (reset semiannually),  pay 1-month [Basis Swap](A%20Guide%20to%20the%20Front%20End%20and%20[[Basis%20Swaps) Markets#[London Interbank Offered Rate](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%2012/Short-Term%20Rates%20and%20the%20Transition%20from%20LIBOR.md) (LIBOR)|LIBOR]] (reset monthly).
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
  - [Credit risk](../../Course%20Notes/Quantitative%20Trading%20Strategies%20Lecture%20Notes.md) considerations.
  - Market conditions (e.g.,  post-2008 [financial crisis](../../Financial%20Markets%20and%20Institutions/III.%20Liquidity%20of%20Assets/Class%209-%20Bailouts%20and%20Bank%20Failures/Squam%20Lake%20Group%20Letter.md)).

## 6. Dollar Duration of a Swap

### 6.1 Definition

- The [dollar duration](../../Financial%20Engineering/A%20Guide%20to%20Duration%20DV01%20and%20Yield%20Curve.md) of a swap measures the sensitivity of its value to changes in [interest rates](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%202/Interest%20Rate%20Quotations.md).
- **Formula**:
 $\text{Dollar Duration of Swap} = \text{Dollar Duration of Fixed-Rate Bond} - \text{Dollar Duration of Floating-Rate Bond}$$

### 6.2 Key Insights

- The [dollar duration](../../Financial%20Engineering/A%20Guide%20to%20Duration%20DV01%20and%20Yield%20Curve.md) of the fixed-rate bond dominates because the floating-rate bond's [duration](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%205/Key%20Rates%20O1s%20Durations%20and%20Hedging.md) is small (less than the time to the next reset date).
- As the reset date approaches,  the floating-rate bond's [duration](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%205/Key%20Rates%20O1s%20Durations%20and%20Hedging.md) decreases further,  reducing the overall sensitivity of the swap.

## 7. Innovations in Swap Markets

### 7.1 Basis Swaps

- Address [basis risk](../../Financial%20Markets%20and%20Institutions/III.%20Liquidity%20of%20Assets/Class%208-%20Markets,%20Meltdowns,%20and%20Arbitrage/Lessons%20From%20The%20Crisis.md) by aligning cash flows indexed to different benchmarks.
- Example: Swap prime-based liabilities for LIBOR-based liabilities.

### 7.2 Yield-Curve Swaps

- Allow counterparties to [exchange cash flows](../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%204%20-%20Swap%20Markets/Fundamentals%20of%20Swaps.md) based on different points on the yield curve.
- Example: Pay 2-year Treasury yield,  receive 10-year Treasury yield.

### 7.3 Asset Swaps

- Combine a bond purchase with a swap to convert fixed-rate bond cash flows into floating-rate cash flows or vice versa.

### 7.4 Swaptions

- Options on swaps that provide the right,  but not the obligation,  to enter into a swap at a future date.
- Example: A callable liability can be created by combining a fixed-rate liability with a [payer swaption](../../Financial%20Engineering/Derivatives/Part%20IX%20-%20Fixed%20Income%20Derivatives/Chapter%2039%20-%20Swaptions,%20Forward%20Swaps,%20and%20MBS.md).

## 8. Summary and Key Takeaways

- Interest rate swaps are versatile tools for [managing interest rate risk](.md) and aligning asset/liability durations.
- Fixed-rate payers are effectively short the bond market,  while floating-rate payers are long the bond market.
- Swaps can synthetically convert [floating-rate debt](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%2013/Uses%20of%20Interest%20Rate%20Swaps.md) to fixed-rate debt and vice versa,  providing flexibility in managing funding costs.
- Basis swaps and other innovations address specific risks,  such as [basis risk](../../Financial%20Markets%20and%20Institutions/III.%20Liquidity%20of%20Assets/Class%208-%20Markets,%20Meltdowns,%20and%20Arbitrage/Lessons%20From%20The%20Crisis.md) and yield curve mismatches.
- [Swap pricing](../../Financial%20Instruments/Citi-Guide%20to%20Swaps.md) is influenced by Treasury yields,  [credit risk](../../Course%20Notes/Quantitative%20Trading%20Strategies%20Lecture%20Notes.md),  and market conditions,  with bid/offer spreads reflecting dealer costs and market dynamics.

By mastering these concepts,  [financial institutions](../../Financial%20Markets%20and%20Institutions/Financial%20Markets%20and%20Institutions%20Lecture%20Notes.md) can effectively use swaps to optimize their balance sheets and manage [interest rate exposure](../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20III%20THE%20PLAYERS/Chapter%2013%20-%20Banks%20Asset-Liability%20Management/Duration%20Gap%20Management.md).

# Lecture Notes: Advanced Interest Rate Swaps and Swaptions

## 1. Introduction to Advanced Interest Rate Swaps and Swaptions

- Interest rate swaps and swaptions are critical tools in modern [financial markets](../../Financial%20Markets%20and%20Institutions/Financial%20Markets%20and%20Institutions%20Lecture%20Notes.md),  offering flexibility in [managing interest rate risk](.md) and customizing cash flows.
- This lecture focuses on:
  - Advanced swap structures,  including yield-curve swaps,  amortizing and accreting swaps,  forward swaps,  and equity swaps.
  - The mechanics and applications of swaptions.
  - The valuation of swaps and swaptions using traditional and lattice-based approaches.
  - Practical applications in asset/liability management and [hedging](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%205/Key%20Rates%20O1s%20Durations%20and%20Hedging.md) strategies.

## 2. Advanced Swap Structures

### 2.1 Yield-Curve Swaps

- **Definition**: A yield-curve swap is a floating-for-floating rate swap where payments are based on [interest rates](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%202/Interest%20Rate%20Quotations.md) at two different points on the yield curve.
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
  - Common in managing [duration](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%205/Key%20Rates%20O1s%20Durations%20and%20Hedging.md) mismatches in portfolios.

### 2.2 Amortizing and Accreting Swaps

#### 2.2.1 Amortizing Swaps
- **Definition**: A swap where the [notional principal](../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%204%20-%20Swap%20Markets/Fundamentals%20of%20Swaps.md) decreases over time,  aligning with the amortization of an [underlying asset](../../Financial%20Instruments/Financial%20Derivatives%20and%20Quantitative%20Methods/Risk%20Neutral%20Pricing%20of%20Options.md) (e.g.,  mortgage loans).
- **Purpose**:
  - Matches the declining principal balance of amortizing assets,  such as [mortgage-backed securities](../../Financial%20Markets%20and%20Institutions/III.%20Liquidity%20of%20Assets/Class%207-%20CP,%20Repo,%20and%20the%20Crisis/Fremont%20Financial%20Corp.%20(b).md) (MBS) or [collateralized mortgage obligations](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%2015/Other%20MBS.md) (CMOs).
  - Reduces the risk of being overhedged or underhedged due to changes in asset [prepayment rates](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%2015/Mortgage%20Pools.md).
- **Mechanics**:
  - The notional amount decreases according to a predefined schedule.
  - [Swap cash flows](../../Financial%20Engineering/Derivatives/Part%20VIII%20-%20Swaps/Chapter%2034%20-%20Pricing%20Interest%20Rate%20Swaps.md) adjust based on the reduced notional amount.
- **Example**:
  - Initial notional = $100 million.
  - Year 1: Notional = $80 million.
  - Year 2: Notional = $60 million.
- **Challenges**:
  - [Prepayment risk](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%2015/Risk%20Factors%20and%20Hedging%20Agency%20MBS.md) can lead to mismatches if the actual amortization differs from the predefined schedule.
  - Balance-guaranteed swaps address this by tying the notional amount to the actual outstanding balance of a reference asset pool.

#### 2.2.2 Accreting Swaps
- **Definition**: A swap where the [notional principal](../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%204%20-%20Swap%20Markets/Fundamentals%20of%20Swaps.md) increases over time,  often used to hedge liabilities that grow incrementally.
- **Applications**:
  - Common in the construction industry to hedge floating-rate drawdown facilities.
  - Aligns with increasing liability schedules.

### 2.3 Forward Swaps

- **Definition**: A [forward swap](../../Financial%20Engineering/Derivatives/Part%20IX%20-%20Fixed%20Income%20Derivatives/Chapter%2039%20-%20Swaptions,%20Forward%20Swaps,%20and%20MBS.md) is a swap agreement with a delayed start date.
- **Purpose**:
  - Hedge future funding requirements or anticipated debt issuance.
  - Lock in current [interest rates](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%202/Interest%20Rate%20Quotations.md) for future periods.
- **Example**:
  - A firm has $200 million of fixed-rate debt maturing in three years.
  - To lock in funding costs for the subsequent five years,  the firm enters into a [forward swap](../../Financial%20Engineering/Derivatives/Part%20IX%20-%20Fixed%20Income%20Derivatives/Chapter%2039%20-%20Swaptions,%20Forward%20Swaps,%20and%20MBS.md) to pay fixed and receive floating starting three years from now.
  - If rates rise,  the firm issues [floating-rate debt](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%2013/Uses%20of%20Interest%20Rate%20Swaps.md) and converts it to fixed-rate liability using the swap.

### 2.4 Equity Swaps

- **Definition**: An [equity swap](../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%204%20-%20Swap%20Markets/Equity%20Commodity%20and%20Exotic%20Swaps.md) involves exchanging cash flows based on the total return of a [stock market](../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20III%20THE%20PLAYERS/Chapter%2012%20-%20Hedge%20Fund%20Strategies/Hedge%20Fund%20Strategies.md) index and an interest rate (fixed or floating).
- **Mechanics**:
  - One party receives the total return on an equity index (e.g.,  S&P 500,  DAX) and pays an interest rate (e.g.,  LIBOR).
  - Payments can be denominated in different currencies.
- **Example**:
  - A money manager enters a two-year quarterly reset [equity swap](../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%204%20-%20Swap%20Markets/Equity%20Commodity%20and%20Exotic%20Swaps.md):
	- Receives the German DAX index return in euros.
	- Pays [Basis Swap](A%20Guide%20to%20the%20Front%20End%20and%20[[Basis%20Swaps) Markets#[London Interbank Offered Rate](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%2012/Short-Term%20Rates%20and%20the%20Transition%20from%20LIBOR.md) (LIBOR)|LIBOR]] in euros.
- **Applications**:
  - Used to gain synthetic exposure to [equity markets](../../Financial%20Engineering/An%20Introduction%20to%20Equity%20Markets.md) without directly holding the underlying assets.
  - Facilitates cross-border investments and [currency diversification](../../International%20Finance/China%20Foreign%20Exchange%20Reserves/Foreign%20Exchange%20Reserves%20-%20Wikipedia/Foreign%20Exchange%20Reserves.md).

## 3. Swaptions: Mechanics and Applications

### 3.1 Definition and Types

- **Definition**: A swaption is an option to enter into a swap at a future date.
- **Types**:
  - **[Payer Swaption](../../Financial%20Engineering/Derivatives/Part%20IX%20-%20Fixed%20Income%20Derivatives/Chapter%2039%20-%20Swaptions,%20Forward%20Swaps,%20and%20MBS.md)**: The right to pay fixed and receive floating.
  - **Receiver Swaption**: The right to receive fixed and pay floating.
  - **Cancellation Swaption**: The right to cancel an existing swap.

### 3.2 Exercise Styles

- **European Swaption**: Exercisable only on a specific date.
- **American Swaption**: Exercisable at any time up to and including the [expiration date](../../Financial%20Instruments/Financial%20Derivatives%20and%20Quantitative%20Methods/Risk%20Neutral%20Pricing%20of%20Options.md).
- **Example**:
  - A seven-year swaption allows the holder to pay fixed at 4% at any time before maturity.
  - If exercised after one year,  the holder pays 4% and receives [Basis Swap](A%20Guide%20to%20the%20Front%20End%20and%20[[Basis%20Swaps) Markets#[London Interbank Offered Rate](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%2012/Short-Term%20Rates%20and%20the%20Transition%20from%20LIBOR.md) (LIBOR)|LIBOR]] for the remaining six years.

### 3.3 Applications

#### 3.3.1 Liability Management
- **[Hedging](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%205/Key%20Rates%20O1s%20Durations%20and%20Hedging.md) Uncertain Funding Requirements**:
  - Lock in current rates without committing to future borrowing.
  - Example: A firm purchases a [payer swaption](../../Financial%20Engineering/Derivatives/Part%20IX%20-%20Fixed%20Income%20Derivatives/Chapter%2039%20-%20Swaptions,%20Forward%20Swaps,%20and%20MBS.md) to hedge against rising rates for anticipated debt issuance.
- **Issuing Callable Debt**:
  - Corporations issue callable bonds and strip off the embedded call option by writing a swaption,  reducing the all-in cost of debt.

#### 3.3.2 Asset Management
- **[Hedging](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%205/Key%20Rates%20O1s%20Durations%20and%20Hedging.md) Prepayable Assets**:
  - Investors holding prepayable assets (e.g.,  MBS) can use swaptions to hedge against [prepayment risk](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%2015/Risk%20Factors%20and%20Hedging%20Agency%20MBS.md).
  - Example: Purchase a receiver swaption to offset the impact of declining [interest rates](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%202/Interest%20Rate%20Quotations.md) on prepayment-sensitive assets.

#### 3.3.3 Arbitrage Opportunities
- Exploit [pricing](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%207/Arbitrage%20Pricing%20of%20Derivatives.md) inefficiencies between the swaption and callable bond markets.
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
  - Discount [future cash flows](../../Financial%20Engineering/Advanced%20Derivatives%20Pricing%20Methodology.md) using [implied forward rates](../../Financial%20Instruments/Lecture%20Notes-%20Financial%20Instruments/Teaching%20Note%201-%20Forward%20Rates%20Agreement/Forwards%20and%20Futures%20Notes.md) derived from [Eurodollar futures](../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%206%20Options%20on%20Non-Price%20Variables/Convexity-Adjusted%20Models%20for%20LIBOR%20Forwards%20Qu.md).
  - Compute the swap fixed rate (SFR) as the rate that equates the present value of fixed and floating cash flows.
- **Limitations**:
  - Cannot handle cash flows that depend on [future interest rate](../../Clippings/Forward%20Rate.md) movements.

### 4.2 Lattice-Based Valuation Approach

- **[Overview](../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%201%20-%20Purpose%20and%20Structure%20of%20Financial%20Markets/Overview%20of%20Financial%20Markets.md)**:
  - Incorporates [interest rate volatility](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%207/Fixed%20Income%20Versus%20Equity%20Derivatives.md) to model [future rate](../../Clippings/Forward%20Rate.md) movements.
  - Constructs an interest-rate lattice to represent possible rate paths.
- **Steps**:
  1. Build the interest-rate lattice using a [one-factor model](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%207/Profit%20and%20Loss%20Attribution%20with%20an%20OAS.md) (e.g.,  Kalotay-Williams-Fabozzi model).
  1. Compute [swap cash flows](../../Financial%20Engineering/Derivatives/Part%20VIII%20-%20Swaps/Chapter%2034%20-%20Pricing%20Interest%20Rate%20Swaps.md) at each node on the lattice.
  1. Discount cash flows backward through the lattice to determine present value.
- **Advantages**:
  - Handles [exotic](../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%206%20Options%20on%20Non-Price%20Variables/Exotic%20Interest%20Rate%20Options.md) instruments with option-like features.
  - Incorporates no-[arbitrage](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%207/Arbitrage%20Pricing%20of%20Derivatives.md) conditions and [interest rate volatility](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%207/Fixed%20Income%20Versus%20Equity%20Derivatives.md).

### 4.3 Example: Swaption Valuation

- **Inputs**:
  - [Notional principal](../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%204%20-%20Swap%20Markets/Fundamentals%20of%20Swaps.md): $100 million.
  - Strike rate: 5%.
  - [Time to expiration](../../Financial%20Engineering/Derivatives/Part%20IV%20-%20Options/Chapter%2016%20-%20Black–Scholes%20Model.md): 2 years.
  - Volatility: 20%.
- **Process**:
  - Construct a [binomial](../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%205%20Options%20on%20Prices%20and%20Hedge-Based%20Valuation/A%20Real-Life%20Option%20Pricing%20Exercise.md) interest-rate lattice.
  - Calculate [swap cash flows](../../Financial%20Engineering/Derivatives/Part%20VIII%20-%20Swaps/Chapter%2034%20-%20Pricing%20Interest%20Rate%20Swaps.md) at each node.
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

- **Definition**: Selling the swap in the [secondary market](../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%201%20-%20Purpose%20and%20Structure%20of%20Financial%20Markets/Primary%20Issuance%20and%20Secondary%20Resale%20Markets.md) for a profit or loss.
- **Valuation**:
  - Termination value = Present value of the annuity (difference between old and new fixed rates) discounted at the current [swap rate](../Fixed%20Income%20Lecture%20Notes/Teaching%20Note%204%20Interest%20Rate%20Derivatives.md).

## 6. Summary and Key Takeaways

- Advanced swap structures,  such as yield-curve swaps,  amortizing swaps,  and forward swaps,  provide tailored solutions for [managing interest rate risk](.md).
- Swaptions offer flexibility in [hedging](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%205/Key%20Rates%20O1s%20Durations%20and%20Hedging.md) and liability management,  bridging the gap between swaps and [caps/floors](../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%206%20Options%20on%20Non-Price%20Variables/Black%20Models%20for%20Bond%20Price%20Options%20Capsfloors.md).
- The lattice-based valuation approach incorporates [interest rate volatility](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%207/Fixed%20Income%20Versus%20Equity%20Derivatives.md),  enabling the [pricing](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%207/Arbitrage%20Pricing%20of%20Derivatives.md) of complex instruments.
- Termination strategies,  including reverse swaps and swap sales,  allow firms to manage or exit swap positions efficiently.

By mastering these advanced concepts,  financial professionals can effectively navigate the complexities of interest rate [derivatives](../../Financial%20Markets/Financial%20Trading%20and%20Markets/Chapter%209%20Arbitrage%20and%20Hedging%20With%20Options.md) and optimize their [risk management strategies](../../Financial%20Markets%20and%20Institutions/III.%20Liquidity%20of%20Assets/Class%206-%20Bank%20Runs/Banks'%20Bonds%20Playing%20Role%20as%20I.md).

# Lecture Notes: Valuation of Interest Rate Swaps and Forward Start Swaps Using a Binomial Lattice

## 1. Introduction to Interest Rate Swaps and Forward Start Swaps

- Interest rate swaps are derivative instruments that allow counterparties to exchange fixed and floating interest rate payments based on a [notional principal](../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%204%20-%20Swap%20Markets/Fundamentals%20of%20Swaps.md) amount.
- Forward start swaps are a variation of interest rate swaps that begin at a specified future date and are used to hedge or lock in [interest rates](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%202/Interest%20Rate%20Quotations.md) for future periods.
- This lecture focuses on:
  - The valuation of a five-year plain vanilla [interest rate swap](../../Financial%20Engineering/Primer%20on%20Interest%20Rate%20Swaps.md) using a [binomial](../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%205%20Options%20on%20Prices%20and%20Hedge-Based%20Valuation/A%20Real-Life%20Option%20Pricing%20Exercise.md) [interest rate lattice](../../Financial%20Engineering/Derivatives/Part%20IX%20-%20Fixed%20Income%20Derivatives/Chapter%2041%20-%20Pricing%20Fixed%20Income%20Derivatives:%20BOPM.md).
  - The valuation of a forward start swap using the same lattice framework.
  - The mechanics of calculating cash flows,  cumulative swap valuation,  and probabilities in the lattice.

## 2. Valuation of a Five-Year Plain Vanilla Interest Rate Swap

### 2.1 Overview of the Swap

- **Swap Details**:
  - [Notional Principal](../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%204%20-%20Swap%20Markets/Fundamentals%20of%20Swaps.md) (NP): $100
  - Swap Fixed Rate (SFR): 3%
  - Tenor: 5 years
  - Settlement Frequency: Semiannual
  - [Interest Rate Model](../Fixed%20Income%20Lecture%20Notes/An%20Overview%20of%20the%20Vasicek%20Short%20Rate%20Model.md): One-factor [binomial lattice](../../Financial%20Engineering/6.%20A%20Brief%20Introduction%20to%20Stochastic%20Calculus.md) with 10 semiannual time steps.
- **Key Assumptions**:
  - Semiannual cash flows with a fraction of the year equal to 0.5.
  - Cash flows are determined at the start of each period but paid in arrears at the end of the period.

### 2.2 Cash Flow Calculation

- **Fixed-Rate Payment**:
 $\text{Fixed-Rate Payment} = \text{SFR} \times \text{NP} \times \left(\frac{\text{Days in Period}}{360}\right)$$
 $\text{Fixed-Rate Payment} = 3\% \times 100 \times 0.5 = 1.5$$

- **Floating-Rate Payment**:
 $\text{Floating-Rate Payment} = \text{Floating Rate} \times \text{NP} \times \left(\frac{\text{Days in Period}}{360}\right)$$

- **Net [Cash Flow](../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%201%20-%20Purpose%20and%20Structure%20of%20Financial%20Markets/Preview%20of%20the%20Book.md)**:
 $\text{Net Cash Flow} = (\text{Floating Rate} - \text{SFR}) \times \text{NP} \times \left(\frac{\text{Days in Period}}{360}\right)$$

- **Example**:
  - At $t=4.5$ years,  the [short rate](../Fixed%20Income%20Lecture%20Notes/An%20Overview%20of%20the%20Vasicek%20Short%20Rate%20Model.md) is 9.1446%.
  - Net [Cash Flow](../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%201%20-%20Purpose%20and%20Structure%20of%20Financial%20Markets/Preview%20of%20the%20Book.md):
	$$\text{Net Cash Flow} = (9.1446\% - 3.0\%) \times 100 \times 0.5 = 3.0723$$

### 2.3 Cumulative Swap Valuation Lattice

- **Purpose**:
  - The cumulative swap valuation lattice calculates the present value of all [future cash flows](../../Financial%20Engineering/Advanced%20Derivatives%20Pricing%20Methodology.md) at each node,  discounted using the rates in the [binomial lattice](../../Financial%20Engineering/6.%20A%20Brief%20Introduction%20to%20Stochastic%20Calculus.md).
- **Discounting Cash Flows**:
 $\text{Present Value} = \frac{\text{Cash Flow}}{1 + \text{Short Rate}/2}$$

- **Example**:
  - At $t=4.5$ years,  the [cash flow](../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%201%20-%20Purpose%20and%20Structure%20of%20Financial%20Markets/Preview%20of%20the%20Book.md) at $t=5$ years is $3.0723$.
  - Discounted Value:
	$$\text{PV} = \frac{3.0723}{1 + 9.1446\%/2} = 2.9380$$

- **Backward Induction**:
  - At each node,  the cumulative value is the sum of:
	1. The discounted values of the two possible future nodes (weighted equally).
	1. The [cash flow](../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%201%20-%20Purpose%20and%20Structure%20of%20Financial%20Markets/Preview%20of%20the%20Book.md) at the current node.

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
  - This occurs because [interest rates](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%202/Interest%20Rate%20Quotations.md) have declined since the swap was initiated.

## 3. Valuation of a Forward Start Swap

### 3.1 Overview of the Forward Start Swap

- **Swap Details**:
  - [Notional Principal](../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%204%20-%20Swap%20Markets/Fundamentals%20of%20Swaps.md) (NP): $100
  - [Forward Swap](../../Financial%20Engineering/Derivatives/Part%20IX%20-%20Fixed%20Income%20Derivatives/Chapter%2039%20-%20Swaptions,%20Forward%20Swaps,%20and%20MBS.md) Fixed Rate (SFR): 3.250%
  - Start Date: 3 years from today
  - Maturity Date: 5 years from today
  - Settlement Frequency: Semiannual
- **Key Assumptions**:
  - The forward start swap begins at $t=3$ years,  so cash flows are calculated for the period $t=3$ to $t=5$.
  - The valuation process uses the same [binomial lattice](../../Financial%20Engineering/6.%20A%20Brief%20Introduction%20to%20Stochastic%20Calculus.md) as the plain vanilla swap.

### 3.2 Cumulative Swap Valuation Lattice

- **Steps**:
  1. Calculate the cash flows at each node for the period $t=3$ to $t=5$.
  1. Construct the cumulative valuation lattice for the forward start swap,  starting at $t=5$ and working backward to $t=3$.

- **Example**:
  - At $t=4.5$,  the [short rate](../Fixed%20Income%20Lecture%20Notes/An%20Overview%20of%20the%20Vasicek%20Short%20Rate%20Model.md) is 9.1446%.
  - Net [Cash Flow](../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%201%20-%20Purpose%20and%20Structure%20of%20Financial%20Markets/Preview%20of%20the%20Book.md):
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
  - Calculating cash flows at each node based on the [interest rate lattice](../../Financial%20Engineering/Derivatives/Part%20IX%20-%20Fixed%20Income%20Derivatives/Chapter%2041%20-%20Pricing%20Fixed%20Income%20Derivatives:%20BOPM.md).
  - Constructing a cumulative valuation lattice using backward induction.
  - Discounting [future cash flows](../../Financial%20Engineering/Advanced%20Derivatives%20Pricing%20Methodology.md) to determine the present value of the swap.
- The swap value reflects the difference between the present value of fixed and floating payments.

### 4.2 Forward Start Swap

- The valuation of a forward start swap involves:
  - Calculating cash flows for the forward period.
  - Constructing a cumulative valuation lattice starting at the forward start date.
  - Weighting cumulative values by the probability of reaching each node.
- The forward start swap value reflects the expected difference between fixed and floating payments during the forward period.

### 4.3 Practical Applications

- **Plain Vanilla Swaps**:
  - Used to hedge [interest rate risk](../Analysis%20of%20Fixed%20Income%20Securities.md) or align asset and liability durations.
- **Forward Start Swaps**:
  - Used to lock in [interest rates](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%202/Interest%20Rate%20Quotations.md) for future funding requirements or anticipated liabilities.

By mastering these valuation techniques,  financial professionals can effectively manage [interest rate risk](../Analysis%20of%20Fixed%20Income%20Securities.md) and optimize their derivative strategies.

# Lecture Notes: Advanced Valuation of Swaps,  Swaptions,  and Basis Swaps

## 1. Introduction to Advanced Swap Valuation

- This lecture focuses on the valuation of advanced swap structures,  including forward start swaps,  swaptions,  and basis swaps.
- We will explore:
  - The probability-weighted valuation of forward start swaps using a [binomial lattice](../../Financial%20Engineering/6.%20A%20Brief%20Introduction%20to%20Stochastic%20Calculus.md).
  - The valuation of swaptions,  including pay-fixed and receive-fixed swaptions.
  - The mechanics of basis swaps,  including the valuation of pay [Basis Swap](A%20Guide%20to%20the%20Front%20End%20and%20[[Basis%20Swaps) Markets#[London Interbank Offered Rate](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%2012/Short-Term%20Rates%20and%20the%20Transition%20from%20LIBOR.md) (LIBOR)|LIBOR]] TED swaps.
- The lattice approach is emphasized for its flexibility in handling complex swap structures and varying [cash flow](../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%201%20-%20Purpose%20and%20Structure%20of%20Financial%20Markets/Preview%20of%20the%20Book.md) assumptions.

## 2. Valuation of Forward Start Swaps (FSS)

### 2.1 Overview of Forward Start Swaps

- A forward start swap (FSS) is a swap that begins at a specified future date.
- **Key Features**:
  - The fixed-rate (SFR) is determined at the time of valuation.
  - The FSS allows counterparties to lock in [interest rates](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%202/Interest%20Rate%20Quotations.md) for future periods.
- **Example**:
  - [Notional Principal](../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%204%20-%20Swap%20Markets/Fundamentals%20of%20Swaps.md): $100
  - Swap Fixed Rate (SFR): 3.250%
  - Start Date: 3 years from today
  - Maturity Date: 5 years from today
  - Settlement Frequency: Semiannual

### 2.2 Probability-Weighted Valuation of FSS

#### 2.2.1 Cumulative Swap Valuation at Year 3

- The cumulative swap valuation at year 3 is calculated using the [binomial lattice](../../Financial%20Engineering/6.%20A%20Brief%20Introduction%20to%20Stochastic%20Calculus.md) approach.
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
- This value represents the present value of the [expected cash flows](../../Advanced%20Financial%20Analysis%20and%20Valuation/Lecture%20Notes%20Advanced%20Financial%20Analysis%20and%20Valuation/Week%206/Week%206%20Assignment%20Review.md) for the fixed-rate payer.
- The value for the floating-rate payer is the negative of this amount: **-1.87089**.

#### 2.2.3 Swap Fixed Rate (SFR) for Zero Value

- The SFR that would produce a zero value for the FSS is **4.233%**.
- This is computed iteratively,  similar to the process for valuing a plain vanilla swap.

## 3. Valuation of Swaptions

### 3.1 Overview of Swaptions

- A **swaption** is an option contract on an [interest rate swap](../../Financial%20Engineering/Primer%20on%20Interest%20Rate%20Swaps.md).
- **Key Features**:
  - The swaption specifies the tenor of the swap and the swap fixed rate (strike rate).
  - The owner has the right,  but not the obligation,  to enter into the swap.
  - Swaptions can be **European-style** (exercisable only at expiration) or **American-style** (exercisable at any time up to expiration).

#### 3.1.1 Types of Swaptions
- **[Payer Swaption](../../Financial%20Engineering/Derivatives/Part%20IX%20-%20Fixed%20Income%20Derivatives/Chapter%2039%20-%20Swaptions,%20Forward%20Swaps,%20and%20MBS.md)**: The right to pay fixed and receive floating.
- **Receiver Swaption**: The right to receive fixed and pay floating.

### 3.2 Example: Valuation of a Pay-Fixed Swaption

#### 3.2.1 Swaption Details

- **Strike Rate**: 3.650%
- **Option Expiration**: 2 years
- **Swap Tenor**: 3 years
- **[Notional Principal](../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%204%20-%20Swap%20Markets/Fundamentals%20of%20Swaps.md)**: $100

#### 3.2.2 Cash Flow Lattice for Plain Vanilla Swap

- The [cash flow](../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%201%20-%20Purpose%20and%20Structure%20of%20Financial%20Markets/Preview%20of%20the%20Book.md) lattice is constructed for a plain vanilla swap with a strike rate of 3.650%.
- **Formula**:
 $\text{Cash Flow}*{i,  j} = (\text{Floating Rate}*{i,  j-1} - \text{SFR}) \times \text{NP} \times 0.5$$
- **Example**:
  - At $t=5$,  the floating rate at $t=4.5$ is 9.1446%.
  - [Cash Flow](../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%201%20-%20Purpose%20and%20Structure%20of%20Financial%20Markets/Preview%20of%20the%20Book.md):
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

- Using backward induction,  the value of the (3,  2) pay-fixed swaption is **1.170195** per $100 of [notional principal](../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%204%20-%20Swap%20Markets/Fundamentals%20of%20Swaps.md).

## 4. Valuation of Basis Swaps

### 4.1 Overview of Basis Swaps

- A **[basis swap](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%2013/Basis%20Swaps.md)** involves the exchange of floating-rate payments based on different benchmarks.
- **Example**:
  - A [Basis Swap](A%20Guide%20to%20the%20Front%20End%20and%20[[Basis%20Swaps) Markets#[London Interbank Offered Rate](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%2012/Short-Term%20Rates%20and%20the%20Transition%20from%20LIBOR.md) (LIBOR)|LIBOR]] TED swap exchanges payments based on [Basis Swap](A%20Guide%20to%20the%20Front%20End%20and%20[[Basis%20Swaps) Markets#[London Interbank Offered Rate](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%2012/Short-Term%20Rates%20and%20the%20Transition%20from%20LIBOR.md) (LIBOR)|LIBOR]] and the 90-day Treasury bill rate plus a spread.

### 4.2 Example: Valuation of a Pay [](../Fixed%20Income%20Lecture%20Notes/A%20Guide%20to%20the%20Front%20End%20and%20Basis%20Swap%20Markets.md#London%20Interbank%20Offered%20Rate%20(LIBOR)|LIBOR) TED Swap

#### 4.2.1 Swap Details

- **Spread**: 0.376%
- **[Notional Principal](../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%204%20-%20Swap%20Markets/Fundamentals%20of%20Swaps.md)**: $100
- **Tenor**: 1 year
- **Payment Frequency**: Quarterly

#### 4.2.2 Interest Rate Lattices

- Separate lattices are constructed for [Basis Swap](A%20Guide%20to%20the%20Front%20End%20and%20[[Basis%20Swaps) Markets#[London Interbank Offered Rate](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%2012/Short-Term%20Rates%20and%20the%20Transition%20from%20LIBOR.md) (LIBOR)|LIBOR]] and the Treasury bill rate.
- **Example**:
  - At the highest node ($t=1$),   [Basis Swap](A%20Guide%20to%20the%20Front%20End%20and%20[[Basis%20Swaps) Markets#[London Interbank Offered Rate](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%2012/Short-Term%20Rates%20and%20the%20Transition%20from%20LIBOR.md) (LIBOR)|LIBOR]] = 1.01%,  Treasury bill rate = 0.29%.

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

- Forward start swaps allow counterparties to lock in [interest rates](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%202/Interest%20Rate%20Quotations.md) for future periods.
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
  - The basics of interest-rate options,  including their [pricing](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%207/Arbitrage%20Pricing%20of%20Derivatives.md),  risk/return profiles,  and [hedging](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%205/Key%20Rates%20O1s%20Durations%20and%20Hedging.md) strategies.
- We will also explore the foundational concepts of option [pricing](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%207/Arbitrage%20Pricing%20of%20Derivatives.md),  including intrinsic value,  time value,  and the impact of volatility.

## 2. Factors Affecting Swaption Valuation

### 2.1 Overview of Swaption Valuation

- Swaptions are option contracts that provide the right,  but not the obligation,  to enter into a swap agreement in the future.
- The value of a swaption is influenced by:
  - **Market Inputs**: [Term structure of interest rates](../../Financial%20Engineering/6.%20A%20Brief%20Introduction%20to%20Stochastic%20Calculus.md) and interest-rate volatility.
  - **Contract Specifications**: Tenor,  strike rate,  and [expiration date](../../Financial%20Instruments/Financial%20Derivatives%20and%20Quantitative%20Methods/Risk%20Neutral%20Pricing%20of%20Options.md).
- The lattice approach is a flexible framework for valuing swaptions,  as it can handle variations in [exotic](../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%206%20Options%20on%20Non-Price%20Variables/Exotic%20Interest%20Rate%20Options.md) swaps and changing market conditions.

### 2.2 Sensitivity to Interest-Rate Volatility

- **Key Insight**: Holding all else constant,  an increase in interest-rate volatility increases the value of a swaption.
- **Mechanism**:
  - Higher volatility increases the probability of the underlying swap moving in-the-money,  thereby increasing the swaption's time value.
- **Example**:
  - Exhibit 65-14 illustrates the effect of volatility on pay-fixed swaptions with a strike rate of 3.5%.
  - As volatility increases,  the value of the swaption rises,  regardless of the [expiration date](../../Financial%20Instruments/Financial%20Derivatives%20and%20Quantitative%20Methods/Risk%20Neutral%20Pricing%20of%20Options.md).

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

- An **option** is the right,  but not the obligation,  to buy or sell a security at a fixed price ([strike price](../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%205%20Options%20on%20Prices%20and%20Hedge-Based%20Valuation/Call%20and%20Put%20Payoffs%20at%20Expiry.md)) before or at expiration.
- **Types**:
  - **Call Option**: The right to buy the underlying security.
  - **Put Option**: The right to sell the underlying security.
- **Exercise Styles**:
  - **American Options**: Exercisable at any time up to expiration.
  - **European Options**: Exercisable only at expiration.

### 3.2 Profit/Loss Profiles

- **Call Option**:
  - Profit increases as the price of the underlying security rises above the [strike price](../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%205%20Options%20on%20Prices%20and%20Hedge-Based%20Valuation/Call%20and%20Put%20Payoffs%20at%20Expiry.md).
  - Break-even price = [Strike price](../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%205%20Options%20on%20Prices%20and%20Hedge-Based%20Valuation/Call%20and%20Put%20Payoffs%20at%20Expiry.md) + Premium paid.
  - Example: Exhibit 66-1 shows the profit/loss graph for a call struck at par with a 1-point premium.
- **Put Option**:
  - Profit increases as the price of the underlying security falls below the [strike price](../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%205%20Options%20on%20Prices%20and%20Hedge-Based%20Valuation/Call%20and%20Put%20Payoffs%20at%20Expiry.md).
  - Break-even price = [Strike price](../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%205%20Options%20on%20Prices%20and%20Hedge-Based%20Valuation/Call%20and%20Put%20Payoffs%20at%20Expiry.md) - Premium paid.
  - Example: Exhibit 66-2 shows the profit/loss graph for a put struck at par with a 1-point premium.

### 3.3 Put-Call Parity

- **Definition**: [Put-call parity](../../Financial%20Engineering/7.%20Black%20Scholes%20Model.md) is a fundamental relationship in options [pricing](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%207/Arbitrage%20Pricing%20of%20Derivatives.md) that links the prices of calls,  puts,  and the underlying security.
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
  - **[Strike Price](../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%205%20Options%20on%20Prices%20and%20Hedge-Based%20Valuation/Call%20and%20Put%20Payoffs%20at%20Expiry.md)**: Higher strike prices decrease call values and increase put values.
  - **[Time to Expiration](../../Financial%20Engineering/Derivatives/Part%20IV%20-%20Options/Chapter%2016%20-%20Black–Scholes%20Model.md)**: Longer time increases the option's time value.
  - **Volatility**: Higher volatility increases the option's time value.
  - **Carry**: Positive carry decreases call values and increases put values.
- **Exhibit 66-10** summarizes the effects of these factors on [call and put](../../Course%20Notes/HBR%20Notes/Notes%20on%20Basic%20Options%20Properties.md) values.

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

- **Definition**: Carry is the difference between the [coupon payments](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%203/Realized%20Returns.md) on a security and the cost of financing its purchase.
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
- **[Delta Hedging](../../Financial%20Instruments/Financial%20Instruments.md)**:
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
- [Put-call parity](../../Financial%20Engineering/7.%20Black%20Scholes%20Model.md) links the prices of calls,  puts,  and the underlying security.
- Delta,  gamma,  and theta are essential metrics for managing option positions.

By mastering these concepts,  financial professionals can effectively use swaps,  swaptions,  and options to manage risk and optimize [portfolio](../../Advanced%20Investments/An%20Asset%20Allocation%20Primer.md) performance.

complex than calculating empirical volatility. [Implied volatility](../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%205%20Options%20on%20Prices%20and%20Hedge-Based%20Valuation/A%20Real-Life%20Option%20Pricing%20Exercise.md) is derived by solving the option [pricing](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%207/Arbitrage%20Pricing%20of%20Derivatives.md) model (e.g.,  [Black-Scholes](../../Financial%20Engineering/Mathematical%20Modeling%20of%20Derivative%20Pricing.md) or [binomial](../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%205%20Options%20on%20Prices%20and%20Hedge-Based%20Valuation/A%20Real-Life%20Option%20Pricing%20Exercise.md) models) for the volatility input that equates the theoretical price of the option to its observed market price. This process requires iterative numerical methods,  as the relationship between volatility and option price is nonlinear.

## 1. Introduction to Volatility in Fixed Income Markets

- Volatility is a critical input in the valuation of options and the design of option strategies. It measures the uncertainty or risk associated with changes in the price or yield of a security.
- In [fixed income markets](../../Financial%20Engineering/A%20Practical%20Guide%20to%20Bonds%20and%20Swaps.md),  volatility is expressed in terms of either price or yield,  and it can be measured on an absolute or percentage basis.
- There are two primary types of volatility:
  - **Empirical Volatility**: Historical volatility based on observed market data.
  - **[Implied Volatility](../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%205%20Options%20on%20Prices%20and%20Hedge-Based%20Valuation/A%20Real-Life%20Option%20Pricing%20Exercise.md)**: Forward-looking volatility derived from the market prices of options.

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

- The [modified duration](../../Financial%20Engineering/A%20Guide%20to%20Duration%20DV01%20and%20Yield%20Curve.md) of a security provides the link between price and yield volatilities.
- **Formula**:
 $\text{Price Volatility} = \text{Yield Volatility} \times \text{Modified Duration}$$
  - Where:
	- **[Price Volatility](../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%206%20Options%20on%20Non-Price%20Variables/Black%20Models%20for%20Bond%20Price%20Options%20Capsfloors.md)**: Percentage change in price.
	- **Yield Volatility**: Absolute change in yield.
	- **[Modified Duration](../../Financial%20Engineering/A%20Guide%20to%20Duration%20DV01%20and%20Yield%20Curve.md)**: Sensitivity of price to yield changes.

#### 2.3.1 Example Conversion
- **Given**:
  - Yield Volatility: 0.50% (annualized).
  - [Modified Duration](../../Financial%20Engineering/A%20Guide%20to%20Duration%20DV01%20and%20Yield%20Curve.md): 5.
- **Calculation**:
 $\text{Price Volatility} = 0.50\% \times 5 = 2.5\%$$

## 3. Implied Volatility

### 3.1 Definition and Importance

- [Implied volatility](../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%205%20Options%20on%20Prices%20and%20Hedge-Based%20Valuation/A%20Real-Life%20Option%20Pricing%20Exercise.md) represents the market's expectation of future volatility over the life of an option.
- It is derived from the observed market price of an option by solving the option [pricing](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%207/Arbitrage%20Pricing%20of%20Derivatives.md) model for the volatility input.

### 3.2 Calculation of Implied Volatility

- [Implied volatility](../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%205%20Options%20on%20Prices%20and%20Hedge-Based%20Valuation/A%20Real-Life%20Option%20Pricing%20Exercise.md) is calculated using iterative numerical methods,  as there is no closed-form solution.
- The process involves:
  1. Inputting the observed market price of the option into an option [pricing](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%207/Arbitrage%20Pricing%20of%20Derivatives.md) model (e.g.,  [Black-Scholes](../../Financial%20Engineering/Mathematical%20Modeling%20of%20Derivative%20Pricing.md)).
  1. Adjusting the volatility input until the theoretical price matches the observed price.

#### 3.2.1 Example
- **Given**:
  - Observed Call Price: $2.50.
  - [Strike Price](../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%205%20Options%20on%20Prices%20and%20Hedge-Based%20Valuation/Call%20and%20Put%20Payoffs%20at%20Expiry.md): $100.
  - Underlying Price: $102.
  - [Time to Expiration](../../Financial%20Engineering/Derivatives/Part%20IV%20-%20Options/Chapter%2016%20-%20Black–Scholes%20Model.md): 90 days.
  - [Risk-Free Rate](../../Financial%20Instruments/Black%20Scholes%20Derivation.md): 2%.
- **Process**:
  - Use the [Black-Scholes model](../../Financial%20Instruments/Black%20Scholes%20Derivation.md) to iteratively solve for the [implied volatility](../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%205%20Options%20on%20Prices%20and%20Hedge-Based%20Valuation/A%20Real-Life%20Option%20Pricing%20Exercise.md) that equates the theoretical price to $2.50.

### 3.3 Applications of Implied Volatility

- **Market Sentiment**:
  - [Implied volatility](../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%205%20Options%20on%20Prices%20and%20Hedge-Based%20Valuation/A%20Real-Life%20Option%20Pricing%20Exercise.md) reflects the market's [expectations](../Fixed%20Income%20Lecture%20Notes/FORWARD%20RATES%20AND%20TERM%20STRUCTURE.md) of future uncertainty.
  - High [implied volatility](../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%205%20Options%20on%20Prices%20and%20Hedge-Based%20Valuation/A%20Real-Life%20Option%20Pricing%20Exercise.md) indicates greater expected price fluctuations.
- **Option [Pricing](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%207/Arbitrage%20Pricing%20of%20Derivatives.md)**:
  - [Implied volatility](../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%205%20Options%20on%20Prices%20and%20Hedge-Based%20Valuation/A%20Real-Life%20Option%20Pricing%20Exercise.md) is a critical input for [pricing](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%207/Arbitrage%20Pricing%20of%20Derivatives.md) options and structuring option strategies.
- **Volatility [Arbitrage](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%207/Arbitrage%20Pricing%20of%20Derivatives.md)**:
  - Traders exploit discrepancies between implied and empirical volatility to generate profits.

## 4. Comparing Empirical and Implied Volatility

| **Aspect** | **Empirical Volatility** | **[Implied Volatility](../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%205%20Options%20on%20Prices%20and%20Hedge-Based%20Valuation/A%20Real-Life%20Option%20Pricing%20Exercise.md)** |

| **Definition** | Historical measure of past price/yield changes. | Market's expectation of future volatility. |

| **Calculation** | Based on standard deviation of historical data. | Derived from observed option prices. |

| **Time Horizon** | Retrospective (past volatility). | Prospective (future volatility). |

| **Use Case** | Evaluating historical risk. | [Pricing](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%207/Arbitrage%20Pricing%20of%20Derivatives.md) options and assessing market sentiment. |

## 5. Practical Applications of Volatility in Fixed Income Markets

### 5.1 Option Pricing and Strategy Design

- Volatility is a key input in option [pricing](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%207/Arbitrage%20Pricing%20of%20Derivatives.md) models,  influencing the premium of calls and puts.
- Traders and [portfolio](../../Advanced%20Investments/An%20Asset%20Allocation%20Primer.md) managers use volatility to design strategies that align with their market outlook and risk tolerance.

### 5.2 Risk Management

- Understanding volatility helps investors assess the risk of their portfolios and implement appropriate [hedging](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%205/Key%20Rates%20O1s%20Durations%20and%20Hedging.md) strategies.
- For example,  high volatility may prompt the use of protective puts to limit downside risk.

### 5.3 Volatility Arbitrage

- Traders exploit differences between implied and empirical volatility to identify mispriced options.
- **Example**:
  - If [implied volatility](../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%205%20Options%20on%20Prices%20and%20Hedge-Based%20Valuation/A%20Real-Life%20Option%20Pricing%20Exercise.md) is higher than empirical volatility,  traders may sell options to capture the premium.

## 6. Summary and Key Takeaways

- Volatility is a measure of uncertainty in the price or yield of a security and plays a central role in option [pricing](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%207/Arbitrage%20Pricing%20of%20Derivatives.md) and strategy design.
- Empirical volatility is based on historical data,  while [implied volatility](../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%205%20Options%20on%20Prices%20and%20Hedge-Based%20Valuation/A%20Real-Life%20Option%20Pricing%20Exercise.md) reflects [market expectations](../../Clippings/Forward%20Rate.md) of future uncertainty.
- The choice of volatility measure depends on the specific application,  such as [pricing](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%207/Arbitrage%20Pricing%20of%20Derivatives.md) options,  managing risk,  or designing [trading strategies](../../Course%20Notes/Quantitative%20Trading%20Strategies%20Lecture%20Notes.md).
- Converting between price and yield volatility requires an understanding of [modified duration](../../Financial%20Engineering/A%20Guide%20to%20Duration%20DV01%20and%20Yield%20Curve.md),  which links the two measures.

By mastering the concepts of empirical and [implied volatility](../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%205%20Options%20on%20Prices%20and%20Hedge-Based%20Valuation/A%20Real-Life%20Option%20Pricing%20Exercise.md),  investors can make informed decisions in the [fixed income](../Lecture%20Notes%20Bonds,%20%20Preferred%20Stock,%20%20and%20Structured%20Products.md) and options markets,  optimizing their strategies to align with market conditions and their [investment](../../Advanced%20Investments/An%20Asset%20Allocation%20Primer.md) objectives.

# Lecture Notes: Interest-Rate Caps,  Floors,  and Participating Structures

## 1. Introduction to Interest-Rate Caps and Floors

- Interest-rate [caps and floors](../../Financial%20Engineering/Fixed%20Income%20Derivatives/Interest%20Rate%20Derivatives-An%20Introduction%20to%20the%20%20Pricing%20of%20Caps%20and%20Floors.md) are derivative instruments that provide asymmetric interest-rate [risk management](../../Financial%20Engineering/Financial%20Mathematics%20Course.md) capabilities,  similar to options.
- **Caps**: Protect against rising [interest rates](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%202/Interest%20Rate%20Quotations.md) by capping the maximum rate on floating-rate liabilities.
- **[Floors](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%2016/Caps%20and%20Floors.md)**: Protect against falling [interest rates](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%202/Interest%20Rate%20Quotations.md) by establishing a minimum rate of return on floating-rate assets.
- These instruments are highly customizable,  allowing users to tailor protection to specific needs by selecting parameters such as the underlying index,  strike rate,  term,  settlement frequency,  and notional amount.

## 2. Features of Interest-Rate Caps and Floors

### 2.1 Underlying Index
- The underlying index determines the reference rate for the cap or floor.
- Common indexes include:
  - [Basis Swap](A%20Guide%20to%20the%20Front%20End%20and%20[[Basis%20Swaps) Markets#[London Interbank Offered Rate](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%2012/Short-Term%20Rates%20and%20the%20Transition%20from%20LIBOR.md) (LIBOR)|LIBOR]] (e.g.,  3-month LIBOR).
  - Treasury bills.
  - [](../../Financial%20Markets%20and%20Institutions/III.%20Liquidity%20of%20Assets/Class%207-%20CP,%20Repo,%20and%20the%20Crisis/Class%20Note%2012%20-%20Commercial%20Paper.md#Class%20Note%2012%20–%20Commercial%20Paper|Commercial%20Paper).
  - Certificates of deposit.
- The maturity of the index (e.g.,  1-month,  3-month,  or 6-month LIBOR) is an additional variable.

### 2.2 Strike Rate
- The strike rate is the threshold rate at which cash flows are exchanged between the purchaser and seller.
- **Caps**:
  - Higher strike rates result in lower premiums because the likelihood of the cap being "in the money" decreases.
- **[Floors](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%2016/Caps%20and%20Floors.md)**:
  - Higher strike rates result in higher premiums because the likelihood of the floor being "in the money" increases.

### 2.3 Term of Protection
- The term of the cap or floor can range from several months to 30 years.
- [Liquidity](../../Financial%20Markets%20and%20Institutions/III.%20Liquidity%20of%20Assets/Class%205-%20Private%20Information,%20Liquidity,%20and%20Securitization/Class%20Note%2010%20Liquidity%20and%20Class%20Note%2010%20Liquidity%20and%20Liquidity%20Managementliquidity%20management.md) decreases for longer-dated [caps and floors](../../Financial%20Engineering/Fixed%20Income%20Derivatives/Interest%20Rate%20Derivatives-An%20Introduction%20to%20the%20%20Pricing%20of%20Caps%20and%20Floors.md),  potentially increasing premiums.

### 2.4 Settlement Frequency
- Settlement frequency determines how often the strike rate is compared to the underlying index.
- Common frequencies include:
  - Monthly.
  - Quarterly.
  - Semiannually.
- Cash flows can be based on:
  - The average daily rate during the settlement period.
  - The [spot rate](../../International%20Finance/The%20Foreign%20Exchange%20Market%20Annotations.md) on the settlement date.

### 2.5 Notional Amount
- The notional amount is the principal on which cash flows are calculated.
- [Caps and floors](../../Financial%20Engineering/Fixed%20Income%20Derivatives/Interest%20Rate%20Derivatives-An%20Introduction%20to%20the%20%20Pricing%20of%20Caps%20and%20Floors.md) can include amortization features to align with the declining balance of an [underlying asset](../../Financial%20Instruments/Financial%20Derivatives%20and%20Quantitative%20Methods/Risk%20Neutral%20Pricing%20of%20Options.md) (e.g.,  [mortgage-backed securities](../../Financial%20Markets%20and%20Institutions/III.%20Liquidity%20of%20Assets/Class%207-%20CP,%20Repo,%20and%20the%20Crisis/Fremont%20Financial%20Corp.%20(b).md)).

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
- [Caps and floors](../../Financial%20Engineering/Fixed%20Income%20Derivatives/Interest%20Rate%20Derivatives-An%20Introduction%20to%20the%20%20Pricing%20of%20Caps%20and%20Floors.md) are priced using option [pricing](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%207/Arbitrage%20Pricing%20of%20Derivatives.md) models,  as they share characteristics with options.
- **Volatility**:
  - Higher volatility increases the premium for both [caps and floors](../../Financial%20Engineering/Fixed%20Income%20Derivatives/Interest%20Rate%20Derivatives-An%20Introduction%20to%20the%20%20Pricing%20of%20Caps%20and%20Floors.md).
- **Strike Rate**:
  - Caps: Higher strike rates reduce the premium.
  - [Floors](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%2016/Caps%20and%20Floors.md): Higher strike rates increase the premium.
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
  - 3-month [Basis Swap](A%20Guide%20to%20the%20Front%20End%20and%20[[Basis%20Swaps) Markets#[London Interbank Offered Rate](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%2012/Short-Term%20Rates%20and%20the%20Transition%20from%20LIBOR.md) (LIBOR)|LIBOR]] = 7%.
  - Strike Rate = 6%.
  - Days in Settlement Period = 90.
  - Payment:
	$$\text{Payment} = (7\% - 6\%) \times \frac{90}{360} \times 10,   000,   000 = 25,   000$$

### 4.4 Effective Interest Expense
- The effective interest expense includes the amortized premium.
- **Maximum Rate**:
  - Strike Rate + Annualized Premium = 6% + 0.52% = 6.52%.
- **Exhibit 67-1**: Illustrates the capped liability's effective interest expense under various [Basis Swap](A%20Guide%20to%20the%20Front%20End%20and%20[[Basis%20Swaps) Markets#[London Interbank Offered Rate](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%2012/Short-Term%20Rates%20and%20the%20Transition%20from%20LIBOR.md) (LIBOR)|LIBOR]] scenarios.

## 5. Participating Caps

### 5.1 Definition
- A participating cap provides full protection against rising rates but requires the buyer to share a percentage of the benefit when rates fall below the strike rate.

### 5.2 Example: Participating Cap
- **Details**:
  - Strike Rate: 7%.
  - Participation Rate: 60%.
- **Scenario**:
  - [Basis Swap](A%20Guide%20to%20the%20Front%20End%20and%20[[Basis%20Swaps) Markets#[London Interbank Offered Rate](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%2012/Short-Term%20Rates%20and%20the%20Transition%20from%20LIBOR.md) (LIBOR)|LIBOR]] = 5%.
  - Difference = 7% - 5% = 2%.
  - Participation = 60% × 2% = 1.2%.
  - Effective Interest Expense = [Basis Swap](A%20Guide%20to%20the%20Front%20End%20and%20[[Basis%20Swaps) Markets#[London Interbank Offered Rate](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%2012/Short-Term%20Rates%20and%20the%20Transition%20from%20LIBOR.md) (LIBOR)|LIBOR]] + Participation = 5% + 1.2% = 6.2%.

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
  - Floating Rate: [Basis Swap](A%20Guide%20to%20the%20Front%20End%20and%20[[Basis%20Swaps) Markets#[London Interbank Offered Rate](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%2012/Short-Term%20Rates%20and%20the%20Transition%20from%20LIBOR.md) (LIBOR)|LIBOR]] + 10 bps.
  - Cap Strike Rate: 7%.
  - Swap Fixed Rate: 5% (off-market).
  - Cap Premium: 200 bps (2% of notional).
  - Present Value of Annuity: 2.76% (based on 0.6% spread over 5 years at 4.4% [discount rate](../../Advanced%20Financial%20Analysis%20and%20Valuation/Problem%20Sets/PSET%207-%20Kohler.md)).
- **Allocation**:
  - Caps: 58%.
  - Swaps: 42%.
- **Exhibit 67-4**: Illustrates effective interest expenses under various [Basis Swap](A%20Guide%20to%20the%20Front%20End%20and%20[[Basis%20Swaps) Markets#[London Interbank Offered Rate](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%2012/Short-Term%20Rates%20and%20the%20Transition%20from%20LIBOR.md) (LIBOR)|LIBOR]] scenarios.

## 7. Interest-Rate Floors

### 7.1 Definition
- [Floors](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%2016/Caps%20and%20Floors.md) protect the rate of return on floating-rate assets by establishing a minimum rate.
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
- [Floors](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%2016/Caps%20and%20Floors.md) protect the rate of return on floating-rate assets in falling-rate scenarios.
- The premium is influenced by the strike rate,  volatility,  and term.

### 8.3 Participating Structures
- Participating caps and swaps offer flexible [hedging](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%205/Key%20Rates%20O1s%20Durations%20and%20Hedging.md) solutions by combining caps and swaps.
- These structures allow buyers to tailor their liability costs to specific rate scenarios.

By understanding the mechanics and [pricing](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%207/Arbitrage%20Pricing%20of%20Derivatives.md) of caps,  [floors](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%2016/Caps%20and%20Floors.md),  and participating structures,  financial professionals can effectively manage interest-rate risk and optimize funding strategies.

out the [credit risk](../../Course%20Notes/Quantitative%20Trading%20Strategies%20Lecture%20Notes.md) of a corporate bond while retaining exposure to [interest rate risk](../Analysis%20of%20Fixed%20Income%20Securities.md) or other factors. This decomposition allows investors to isolate and manage specific risks more effectively.

## 7. Summary and Key Takeaways

### 7.1 Interest-Rate Floors and Caps
- **Interest-Rate [Floors](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%2016/Caps%20and%20Floors.md)**: Provide protection against falling [interest rates](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%202/Interest%20Rate%20Quotations.md),  ensuring a minimum return on floating-rate assets. They are beneficial in bullish interest-rate scenarios where [asset returns](../../Financial%20Markets/Financial%20Asset%20Pricing%20Theory%20Overview/Chapter%201%20-%20Introduction%20and%20Overview/Some%20Stylized%20Empirical%20Facts%20About%20Asset%20Retur.md) are subject to erosion.
- **Interest-Rate Caps**: Protect against rising [interest rates](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%202/Interest%20Rate%20Quotations.md) by capping the maximum rate on floating-rate liabilities. They are analogous to buying a strip of put options on [interest rates](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%202/Interest%20Rate%20Quotations.md).
- **Cap/Floor Parity**: Similar to put/call parity in options,  cap/floor parity establishes the relationship between caps,  [floors](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%2016/Caps%20and%20Floors.md),  and interest-rate swaps. The cost of a cap should equal the cost of a floor struck at the same rate on an identical index,  ensuring no [arbitrage opportunities](../../Financial%20Markets%20and%20Institutions/III.%20Liquidity%20of%20Assets/Class%208-%20Markets,%20Meltdowns,%20and%20Arbitrage/Class%20Note%2013%20The%20LTCM%20Meltdown.md).

### 7.2 Interest-Rate Collars and Corridors
- **Interest-Rate Collars**: Combine the purchase of a cap and the sale of a floor to hedge floating-rate liabilities. This strategy limits the liability rate between the floor and cap strike rates,  reducing the cost of protection but sacrificing benefits from market rallies below the floor strike rate.
- **Interest-Rate Corridors**: Involve buying a cap at a lower strike rate and selling a cap at a higher strike rate. This strategy reduces the cost of the lower strike cap while maintaining the benefit of falling [interest rates](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%202/Interest%20Rate%20Quotations.md). However,  it introduces risk if rates exceed the higher strike cap.

### 7.3 Credit Derivatives
- **Credit Default Swaps (CDS)**: Allow the transfer of [credit risk](../../Course%20Notes/Quantitative%20Trading%20Strategies%20Lecture%20Notes.md) from one party to another,  providing a tool for [hedging](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%205/Key%20Rates%20O1s%20Durations%20and%20Hedging.md) or assuming credit exposure. They are widely used by banks,  insurance companies,  [hedge funds](../../Financial%20Engineering/Basis%20Trade%20Explainer.md),  and other market participants.
- **CDS Indices**: Offer a diversified exposure to a [portfolio](../../Advanced%20Investments/An%20Asset%20Allocation%20Primer.md) of credits,  simplifying the process of managing macro-level [credit risk](../../Course%20Notes/Quantitative%20Trading%20Strategies%20Lecture%20Notes.md).
- **Market Evolution**: The [CDS market](../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20II%20CASH%20FLOW%20ENGINEERING/Chapter%2010%20-%20Collateralized%20Debt%20Obligations%20and%20Basket%20Credit%20Derivatives/Credit%20Derivative%20Indexes.md) has evolved significantly since its inception,  with standardization efforts by ISDA and regulatory changes improving transparency and reducing systemic risk.

### 7.4 Applications of Credit Derivatives
- **[Hedging](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%205/Key%20Rates%20O1s%20Durations%20and%20Hedging.md) [Credit Risk](../../Course%20Notes/Quantitative%20Trading%20Strategies%20Lecture%20Notes.md)**: CDS provide an efficient way to hedge [credit risk](../../Course%20Notes/Quantitative%20Trading%20Strategies%20Lecture%20Notes.md),  replacing the need to short [Corporate Bonds](../../Financial%20Markets%20and%20Institutions/II.%20The%20Roles%20of%20Banks%20and%20Derivative%20Markets%20in%20Resolving%20Problems%20Inherent%20in%20Debt%20Contracts/Class%202-%20Debt%20Contracts%20due%20to%20Lack%20of%20Information/Class%20Notes%202%20–%20Corporate%20Bond%20Contracts.md).
- **Customization**: The bilateral OTC nature of CDS allows for tailored contracts to meet specific needs.
- **[Leverage](../../Advanced%20Investments/Lecture%206-Leverage,%20Tail%20Risk,%20Volatility%20Products.md) and Yield Enhancement**: CDS require minimal upfront payments,  enabling leveraged exposure to [credit risk](../../Course%20Notes/Quantitative%20Trading%20Strategies%20Lecture%20Notes.md).
- **Risk Decomposition**: CDS can isolate [credit risk](../../Course%20Notes/Quantitative%20Trading%20Strategies%20Lecture%20Notes.md) from other risks,  such as [interest rate risk](../Analysis%20of%20Fixed%20Income%20Securities.md),  allowing for more precise [risk management](../../Financial%20Engineering/Financial%20Mathematics%20Course.md).

## 8. Practical Considerations

### 8.1 Risk Management
- Interest-rate [derivatives](../../Financial%20Markets/Financial%20Trading%20and%20Markets/Chapter%209%20Arbitrage%20and%20Hedging%20With%20Options.md) and [credit derivatives](../../Credit%20Markets/RISK%20NEUTRAL%20VALUATION%20FRAMEWORK%20FOR%20CREDIT%20DEFAULT%20SWAPS.md) are powerful tools for managing risk but require careful consideration of market conditions,  counterparty risk,  and [liquidity](../../Financial%20Markets%20and%20Institutions/III.%20Liquidity%20of%20Assets/Class%205-%20Private%20Information,%20Liquidity,%20and%20Securitization/Class%20Note%2010%20Liquidity%20and%20Class%20Note%2010%20Liquidity%20and%20Liquidity%20Managementliquidity%20management.md).
- Strategies such as collars and corridors can reduce costs but may introduce additional risks,  particularly in extreme market scenarios.

### 8.2 Regulatory and Market Changes
- The [introduction](../../Financial%20Markets%20and%20Institutions/III.%20Liquidity%20of%20Assets/Class%209-%20Bailouts%20and%20Bank%20Failures/Squam%20Lake%20Group%20Introduction.md) of centralized clearing and standardized contracts has improved the transparency and efficiency of the [derivatives](../../Financial%20Markets/Financial%20Trading%20and%20Markets/Chapter%209%20Arbitrage%20and%20Hedging%20With%20Options.md) market.
- Market participants must stay informed about regulatory developments to ensure compliance and optimize their use of [derivatives](../../Financial%20Markets/Financial%20Trading%20and%20Markets/Chapter%209%20Arbitrage%20and%20Hedging%20With%20Options.md).

### 8.3 Strategic Use of Derivatives
- Combining interest-rate and [credit derivatives](../../Credit%20Markets/RISK%20NEUTRAL%20VALUATION%20FRAMEWORK%20FOR%20CREDIT%20DEFAULT%20SWAPS.md) can create sophisticated [hedging](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%205/Key%20Rates%20O1s%20Durations%20and%20Hedging.md) strategies that address multiple risks simultaneously.
- Understanding the interplay between different instruments,  such as caps,  [floors](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%2016/Caps%20and%20Floors.md),  swaps,  and CDS,  is essential for effective [portfolio management](../../Financial%20Engineering/Fixed%20Income%20Derivatives/The%20Impact%20of%20Option%20Strategies%20in%20Financial%20%20Portfolios%20Performance.md).

By mastering the mechanics,  [pricing](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%207/Arbitrage%20Pricing%20of%20Derivatives.md),  and applications of interest-rate and [credit derivatives](../../Credit%20Markets/RISK%20NEUTRAL%20VALUATION%20FRAMEWORK%20FOR%20CREDIT%20DEFAULT%20SWAPS.md),  financial professionals can enhance their ability to manage risk,  optimize [returns](../../Financial%20Markets/Financial%20Asset%20Pricing%20Theory%20Overview/Chapter%203%20-%20%20Assets,%20Portfolios,%20and%20Arbitrage/Assets.md),  and navigate complex market environments.

# Lecture Notes: Credit Default Swaps (CDS) – Mechanics,  Pricing,  and Settlement

## 1. Introduction to Credit Default Swaps (CDS)

- A **[Credit Default Swap](../../Credit%20Markets/Credit%20Market%20Session%202.md) (CDS)** is a financial derivative that allows the transfer of [credit risk](../../Course%20Notes/Quantitative%20Trading%20Strategies%20Lecture%20Notes.md) from one party to another. It functions similarly to an insurance contract but is traded in [financial markets](../../Financial%20Markets%20and%20Institutions/Financial%20Markets%20and%20Institutions%20Lecture%20Notes.md) and can be valued at any time.
- **Key Participants**:
  - **[Protection Buyer](../../Financial%20Instruments/Financial%20Derivatives%20and%20Quantitative%20Methods/Credit%20Default%20Swaps.md)**: Pays a premium to transfer the [credit risk](../../Course%20Notes/Quantitative%20Trading%20Strategies%20Lecture%20Notes.md) of a [reference entity](../../Financial%20Instruments/Lecture%20Notes-%20Financial%20Instruments/Lecture%20Notes%209A-%20Credit%20Default%20Swaps.md) to the [protection seller](../../Financial%20Instruments/Financial%20Derivatives%20and%20Quantitative%20Methods/Credit%20Default%20Swaps.md).
  - **[Protection Seller](../../Financial%20Instruments/Financial%20Derivatives%20and%20Quantitative%20Methods/Credit%20Default%20Swaps.md)**: Receives the premium and assumes the [credit risk](../../Course%20Notes/Quantitative%20Trading%20Strategies%20Lecture%20Notes.md) of the [reference entity](../../Financial%20Instruments/Lecture%20Notes-%20Financial%20Instruments/Lecture%20Notes%209A-%20Credit%20Default%20Swaps.md).
- **Purpose**:
  - [Hedging](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%205/Key%20Rates%20O1s%20Durations%20and%20Hedging.md) [credit risk](../../Course%20Notes/Quantitative%20Trading%20Strategies%20Lecture%20Notes.md).
  - Speculating on creditworthiness.
  - Structuring tailored credit investments.
  - Managing regulatory capital.

## 2. Mechanics of a CDS Contract

### 2.1 Structure of a CDS

- A CDS is a bilateral contract between a [protection buyer](../../Financial%20Instruments/Financial%20Derivatives%20and%20Quantitative%20Methods/Credit%20Default%20Swaps.md) and a [protection seller](../../Financial%20Instruments/Financial%20Derivatives%20and%20Quantitative%20Methods/Credit%20Default%20Swaps.md).
- **Key Components**:
  - **[Reference Entity](../../Financial%20Instruments/Lecture%20Notes-%20Financial%20Instruments/Lecture%20Notes%209A-%20Credit%20Default%20Swaps.md)**: The corporate or sovereign issuer whose [credit risk](../../Course%20Notes/Quantitative%20Trading%20Strategies%20Lecture%20Notes.md) is being transferred.
  - **Deliverable Obligations**: Bonds or loans of the [reference entity](../../Financial%20Instruments/Lecture%20Notes-%20Financial%20Instruments/Lecture%20Notes%209A-%20Credit%20Default%20Swaps.md) that are covered by the CDS.
  - **Credit Events**: Specific events (e.g.,  bankruptcy,  failure to pay) that trigger the CDS.
  - **Notional Amount**: The face value of the debt being protected.
  - **Premium Leg**: Regular payments made by the [protection buyer](../../Financial%20Instruments/Financial%20Derivatives%20and%20Quantitative%20Methods/Credit%20Default%20Swaps.md) to the [protection seller](../../Financial%20Instruments/Financial%20Derivatives%20and%20Quantitative%20Methods/Credit%20Default%20Swaps.md).
  - **Protection Leg**: Contingent payment made by the [protection seller](../../Financial%20Instruments/Financial%20Derivatives%20and%20Quantitative%20Methods/Credit%20Default%20Swaps.md) if a [credit event](../../Financial%20Engineering/Valuation%20of%20Credit%20Default%20Swaps.md) occurs.

### 2.2 Premium Leg

- The **premium leg** consists of periodic fixed payments made by the [protection buyer](../../Financial%20Instruments/Financial%20Derivatives%20and%20Quantitative%20Methods/Credit%20Default%20Swaps.md) to the [protection seller](../../Financial%20Instruments/Financial%20Derivatives%20and%20Quantitative%20Methods/Credit%20Default%20Swaps.md).
- **Calculation**:
 $\text{Premium Payment} = \text{Fixed Coupon} \times \text{Notional Amount} \times \text{Year Fraction (Actual/360)}$$
- **Key Features**:
  - Payments terminate after a [credit event](../../Financial%20Engineering/Valuation%20of%20Credit%20Default%20Swaps.md).
  - Fixed coupons are standardized (e.g.,  100 bps or 500 bps) and do not reflect the [credit risk](../../Course%20Notes/Quantitative%20Trading%20Strategies%20Lecture%20Notes.md) of the [reference entity](../../Financial%20Instruments/Lecture%20Notes-%20Financial%20Instruments/Lecture%20Notes%209A-%20Credit%20Default%20Swaps.md). Instead,  the upfront payment adjusts for [credit risk](../../Course%20Notes/Quantitative%20Trading%20Strategies%20Lecture%20Notes.md).

### 2.3 Protection Leg

- The **protection leg** is a contingent payment made by the [protection seller](../../Financial%20Instruments/Financial%20Derivatives%20and%20Quantitative%20Methods/Credit%20Default%20Swaps.md) to the [protection buyer](../../Financial%20Instruments/Financial%20Derivatives%20and%20Quantitative%20Methods/Credit%20Default%20Swaps.md) if a [credit event](../../Financial%20Engineering/Valuation%20of%20Credit%20Default%20Swaps.md) occurs.
- **Payment Amount**:
 $\text{Protection Payment} = \text{Notional Amount} \times (1 - \text{Recovery Rate})$$
  - **[Recovery Rate](../../Credit%20Markets/Credit%20Markets%20Session%203.md)**: The market-determined value of the deliverable obligations after a [credit event](../../Financial%20Engineering/Valuation%20of%20Credit%20Default%20Swaps.md).
- **Settlement Methods**:
  - **[Cash Settlement](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%2016/Swaptions.md)**: [Protection seller](../../Financial%20Instruments/Financial%20Derivatives%20and%20Quantitative%20Methods/Credit%20Default%20Swaps.md) pays the difference between par and the recovery price.
  - **[Physical Settlement](../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%203%20-%20Futures%20Markets/Fundamentals%20of%20Futures%20and%20Forwards.md)**: [Protection buyer](../../Financial%20Instruments/Financial%20Derivatives%20and%20Quantitative%20Methods/Credit%20Default%20Swaps.md) delivers the impaired obligations to the [protection seller](../../Financial%20Instruments/Financial%20Derivatives%20and%20Quantitative%20Methods/Credit%20Default%20Swaps.md) in exchange for the notional amount.

### 2.4 Upfront Payment

- The **upfront payment** adjusts for the difference between the fixed coupon and the market-implied [credit spread](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%2014/Cds-Equivalent%20Bond%20Spread.md) of the [reference entity](../../Financial%20Instruments/Lecture%20Notes-%20Financial%20Instruments/Lecture%20Notes%209A-%20Credit%20Default%20Swaps.md).
- **Key Factors**:
  - If the fixed coupon is lower than the market-implied spread,  the [protection buyer](../../Financial%20Instruments/Financial%20Derivatives%20and%20Quantitative%20Methods/Credit%20Default%20Swaps.md) makes an upfront payment to the [protection seller](../../Financial%20Instruments/Financial%20Derivatives%20and%20Quantitative%20Methods/Credit%20Default%20Swaps.md).
  - If the fixed coupon is higher than the market-implied spread,  the [protection seller](../../Financial%20Instruments/Financial%20Derivatives%20and%20Quantitative%20Methods/Credit%20Default%20Swaps.md) makes an upfront payment to the [protection buyer](../../Financial%20Instruments/Financial%20Derivatives%20and%20Quantitative%20Methods/Credit%20Default%20Swaps.md).

## 3. Credit Events in CDS Contracts

### 3.1 Definition of Credit Events

- A **[credit event](../../Financial%20Engineering/Valuation%20of%20Credit%20Default%20Swaps.md)** is a predefined event that triggers the protection leg of a CDS contract.
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

- **Restructuring** refers to a consensual agreement between a [reference entity](../../Financial%20Instruments/Lecture%20Notes-%20Financial%20Instruments/Lecture%20Notes%209A-%20Credit%20Default%20Swaps.md) and its creditors to modify debt terms in a way that negatively impacts creditors.
- **Challenges**:
  - Restructuring creates a "delivery option" for the [protection buyer](../../Financial%20Instruments/Financial%20Derivatives%20and%20Quantitative%20Methods/Credit%20Default%20Swaps.md),  who can choose the [cheapest-to-deliver](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%2015/Tba%20and%20Specified%20Pools%20Markets.md) obligation.
  - This can lead to windfall gains for the [protection buyer](../../Financial%20Instruments/Financial%20Derivatives%20and%20Quantitative%20Methods/Credit%20Default%20Swaps.md) and larger losses for the [protection seller](../../Financial%20Instruments/Financial%20Derivatives%20and%20Quantitative%20Methods/Credit%20Default%20Swaps.md).
- **Mitigation**:
  - [Introduction](../../Financial%20Markets%20and%20Institutions/III.%20Liquidity%20of%20Assets/Class%209-%20Bailouts%20and%20Bank%20Failures/Squam%20Lake%20Group%20Introduction.md) of restructuring clauses:
	- **Old-Restructuring (Old-Re)**: 30-year maturity limit on deliverables.
	- **Modified-Restructuring (Mod-Re)**: Limits deliverables to those maturing within the greater of the CDS termination date or 30 months after the restructuring date.
	- **Modified-Modified Restructuring (Mod-Mod Re)**: Similar to Mod-Re but with a 60-month limit for restructured obligations and a 30-month limit for non-restructured obligations.
	- **No-Restructuring (No-Re)**: Excludes restructuring as a [credit event](../../Financial%20Engineering/Valuation%20of%20Credit%20Default%20Swaps.md).

## 4. Settlement of CDS Contracts

### 4.1 Auction Process

- The settlement of a CDS contract after a [credit event](../../Financial%20Engineering/Valuation%20of%20Credit%20Default%20Swaps.md) involves determining the recovery price of the deliverable obligations through a market-wide auction.
- **Objectives**:
  1. Prevent short squeezes by ensuring sufficient deliverable obligations.
  1. Establish a common recovery price across the [CDS market](../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20II%20CASH%20FLOW%20ENGINEERING/Chapter%2010%20-%20Collateralized%20Debt%20Obligations%20and%20Basket%20Credit%20Derivatives/Credit%20Derivative%20Indexes.md).
  1. Handle soft restructuring credit events.
- **Mechanics**:
  - Dealers submit bids and offers for the deliverable obligations.
  - The final recovery price is determined based on the auction results.

### 4.2 Settlement Timeline

- **[Credit Event](../../Financial%20Engineering/Valuation%20of%20Credit%20Default%20Swaps.md) Determination**:
  - Before 2009: Bilateral decision based on publicly available information.
  - After 2009: Determined by a centralized determinations committee.
- **Key Dates**:
  - **Effective Date**: Protection begins 60 days before the [credit event](../../Financial%20Engineering/Valuation%20of%20Credit%20Default%20Swaps.md) determination request.
  - **Scheduled Termination Date**: Standardized to March 20,  June 20,  September 20,  or December 20 of the specified year.

## 5. Pricing and Valuation of CDS Contracts

### 5.1 Quoted Spread and Fixed Coupon

- The **quoted spread** reflects the market-implied [credit risk](../../Course%20Notes/Quantitative%20Trading%20Strategies%20Lecture%20Notes.md) of the [reference entity](../../Financial%20Instruments/Lecture%20Notes-%20Financial%20Instruments/Lecture%20Notes%209A-%20Credit%20Default%20Swaps.md).
- The **fixed coupon** is standardized (e.g.,  100 bps or 500 bps) and does not vary with [credit risk](../../Course%20Notes/Quantitative%20Trading%20Strategies%20Lecture%20Notes.md).
- **Upfront Payment**:
  - Adjusts for the difference between the fixed coupon and the quoted spread.
  - **Example**:
	- Fixed Coupon: 100 bps.
	- Quoted Spread: 160 bps.
	- Upfront Payment: [Protection buyer](../../Financial%20Instruments/Financial%20Derivatives%20and%20Quantitative%20Methods/Credit%20Default%20Swaps.md) pays the [protection seller](../../Financial%20Instruments/Financial%20Derivatives%20and%20Quantitative%20Methods/Credit%20Default%20Swaps.md) to compensate for the lower fixed coupon.

### 5.2 Mark-to-Market Valuation

- The value of a CDS contract changes over time due to:
  - Changes in the quoted spread.
  - Changes in [interest rates](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%202/Interest%20Rate%20Quotations.md).
- **Key Insight**:
  - A long protection position (buying CDS protection) gains value when the quoted spread widens,  as the cost of protection increases.
  - A short protection position (selling CDS protection) gains value when the quoted spread tightens,  as the cost of protection decreases.

## 6. Applications of CDS

### 6.1 Hedging Credit Risk

- CDS provide an efficient way to hedge [credit risk](../../Course%20Notes/Quantitative%20Trading%20Strategies%20Lecture%20Notes.md) without selling the underlying bonds or loans.
- **Example**:
  - A bank holding [Corporate Bonds](../../Financial%20Markets%20and%20Institutions/II.%20The%20Roles%20of%20Banks%20and%20Derivative%20Markets%20in%20Resolving%20Problems%20Inherent%20in%20Debt%20Contracts/Class%202-%20Debt%20Contracts%20due%20to%20Lack%20of%20Information/Class%20Notes%202%20–%20Corporate%20Bond%20Contracts.md) can buy CDS protection to hedge against [default risk](../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%207%20-%20Default%20Risk%20and%20Credit%20Derivatives/Default%20Risk%20and%20Credit%20Derivatives%20183.md).

### 6.2 Speculation

- CDS enable market participants to express views on the creditworthiness of a [reference entity](../../Financial%20Instruments/Lecture%20Notes-%20Financial%20Instruments/Lecture%20Notes%209A-%20Credit%20Default%20Swaps.md).
- **Example**:
  - Buying CDS protection is equivalent to [shorting](../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%202%20-%20Spot%20Markets/Short%20Selling.md) the [credit risk](../../Course%20Notes/Quantitative%20Trading%20Strategies%20Lecture%20Notes.md) of the [reference entity](../../Financial%20Instruments/Lecture%20Notes-%20Financial%20Instruments/Lecture%20Notes%209A-%20Credit%20Default%20Swaps.md).
  - Selling CDS protection is equivalent to going long on the [credit risk](../../Course%20Notes/Quantitative%20Trading%20Strategies%20Lecture%20Notes.md) of the [reference entity](../../Financial%20Instruments/Lecture%20Notes-%20Financial%20Instruments/Lecture%20Notes%209A-%20Credit%20Default%20Swaps.md).

### 6.3 Structured Credit Investments

- CDS can be used as building blocks for [structured credit products](../A%20Survey%20of%20the%20Micro%20structure%20of%20Fixed-Income%20Markets.md),  such as [collateralized debt obligations](../../Credit%20Markets/Credit%20Markets%20Session%205.md) (CDOs).
- These products provide tailored risk-return profiles for specific investor needs.

### 6.4 Regulatory Capital Management

- Banks can use CDS to hedge credits with high regulatory capital charges,  provided the hedge is recognized as economically effective by regulators.

## 7. Summary and Key Takeaways

### 7.1 Mechanics of CDS

- A CDS is a bilateral contract that transfers [credit risk](../../Course%20Notes/Quantitative%20Trading%20Strategies%20Lecture%20Notes.md) from the [protection buyer](../../Financial%20Instruments/Financial%20Derivatives%20and%20Quantitative%20Methods/Credit%20Default%20Swaps.md) to the [protection seller](../../Financial%20Instruments/Financial%20Derivatives%20and%20Quantitative%20Methods/Credit%20Default%20Swaps.md).
- The premium leg consists of fixed periodic payments,  while the protection leg is contingent on a [credit event](../../Financial%20Engineering/Valuation%20of%20Credit%20Default%20Swaps.md).

### 7.2 Credit Events and Settlement

- Credit events trigger the protection leg of a CDS and include bankruptcy,  failure to pay,  and restructuring.
- Settlement involves determining the recovery price through an [auction process](../../Financial%20Markets/Financial%20Trading%20and%20Markets/Chapter%202%20Securities%20Markets.md).

### 7.3 Pricing and Applications

- The upfront payment adjusts for the difference between the fixed coupon and the quoted spread.
- CDS are versatile tools for [hedging](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%205/Key%20Rates%20O1s%20Durations%20and%20Hedging.md),  speculation,  structured credit investments,  and regulatory capital management.

By understanding the mechanics,  [pricing](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%207/Arbitrage%20Pricing%20of%20Derivatives.md),  and applications of CDS,  financial professionals can effectively manage [credit risk](../../Course%20Notes/Quantitative%20Trading%20Strategies%20Lecture%20Notes.md) and optimize their [investment](../../Advanced%20Investments/An%20Asset%20Allocation%20Primer.md) strategies.

of a [portfolio](../../Advanced%20Investments/An%20Asset%20Allocation%20Primer.md) of CDS contracts,  where the premium payments are adjusted for the surviving notional of the reference [portfolio](../../Advanced%20Investments/An%20Asset%20Allocation%20Primer.md).

## 1. Introduction to Credit Default Swaps (CDS) and Indices

- Credit Default Swaps (CDS) and CDS indices are essential tools in the [credit derivatives](../../Credit%20Markets/RISK%20NEUTRAL%20VALUATION%20FRAMEWORK%20FOR%20CREDIT%20DEFAULT%20SWAPS.md) market,  providing investors with mechanisms to hedge [credit risk](../../Course%20Notes/Quantitative%20Trading%20Strategies%20Lecture%20Notes.md),  speculate on creditworthiness,  and gain diversified exposure to [credit markets](../../Credit%20Markets/Credit%20Markets%20Session%201.md).
- This lecture focuses on:
  - The mechanics of CDS contracts and indices.
  - The innovations introduced by the 2009 Big Bang Protocol,  including the Determinations Committee (DC) and auction-based settlement.
  - The compression cycle and its role in reducing systemic risk.
  - The structure,  [pricing](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%207/Arbitrage%20Pricing%20of%20Derivatives.md),  and applications of CDS indices.

## 2. The 2009 Big Bang Protocol and Determinations Committee

### 2.1 Introduction of the Determinations Committee (DC)

- The **2009 Big Bang Protocol** introduced a centralized mechanism for determining credit events,  replacing the bilateral process that existed previously.
- **Key Features**:
  - Five regional DCs: Americas,  Asia (excluding Japan),  Japan,  Australia-New Zealand,  and EMEA (Europe,  Middle East,  and Africa).
  - Membership includes both buy-side and sell-side representatives to ensure impartiality.
  - Decisions require an **80% supermajority** for approval.

### 2.2 Credit Event Determination Process

- **Process**:
  1. A market participant submits a request to the DC secretary to investigate a potential [credit event](../../Financial%20Engineering/Valuation%20of%20Credit%20Default%20Swaps.md).
  1. The request must include publicly available information supporting the claim.
  1. The DC has **two business days** to meet,  investigate,  and vote on whether a [credit event](../../Financial%20Engineering/Valuation%20of%20Credit%20Default%20Swaps.md) has occurred.
  1. If more time is needed,  the DC can vote to extend the investigation period.

- **Outcomes**:
  - For **hard credit events** (e.g.,  bankruptcy,  failure to pay),  CDS contracts are automatically triggered.
  - For **restructuring credit events**,  the [protection buyer](../../Financial%20Instruments/Financial%20Derivatives%20and%20Quantitative%20Methods/Credit%20Default%20Swaps.md) or seller must choose to trigger the contract.

### 2.3 Restructuring Credit Events

- Restructuring is not an automatic trigger because it is not a [bankruptcy](../../Course%20Notes/HBR%20Notes/A%20Strategic%20Perspective%20on%20Bankruptcy.md) event and may be a precursor to one.
- **Triggering Rules**:
  - If the [protection buyer](../../Financial%20Instruments/Financial%20Derivatives%20and%20Quantitative%20Methods/Credit%20Default%20Swaps.md) triggers,  the basket of deliverable obligations corresponds to the CDS contract's scheduled termination date.
  - If the [protection seller](../../Financial%20Instruments/Financial%20Derivatives%20and%20Quantitative%20Methods/Credit%20Default%20Swaps.md) triggers,  the basket corresponds to the longest maturity (30-year) bucket.
- **Implications**:
  - Both parties prefer the other to trigger due to the differing value of deliverable obligations.
  - The "use it or lose it" rule requires careful timing to avoid missing the triggering deadline.

## 3. The Compression Cycle

### 3.1 Purpose and Mechanics

- The **compression cycle** is a process designed to cancel out mutually offsetting CDS positions,  reducing the number of outstanding contracts and systemic risk.
- **Key Features**:
  - Conducted quarterly across the [credit derivatives](../../Credit%20Markets/RISK%20NEUTRAL%20VALUATION%20FRAMEWORK%20FOR%20CREDIT%20DEFAULT%20SWAPS.md) market.
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

- The [auction process](../../Financial%20Markets/Financial%20Trading%20and%20Markets/Chapter%202%20Securities%20Markets.md) determines the recovery price of deliverable obligations after a [credit event](../../Financial%20Engineering/Valuation%20of%20Credit%20Default%20Swaps.md).
- **Stages**:
  - **Stage One**: Determines the indicative recovery price (Internal Market Midpoint Price,  IMMP) and net open interest.
  - **Stage Two**: Matches net open interest with market participants to establish the final auction price.

### 4.2 Stage One: Indicative Recovery Price

- **Process**:
  - Dealers submit bid/offer prices and [physical settlement requests](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%2014/CDS%20Settlement%20Auctions.md).
  - An algorithm calculates the IMMP by rejecting outliers and averaging the remaining bid/offer spreads.
  - The IMMP is rounded to the nearest 1/8th of a point.
- **Net Open Interest**:
  - Represents the [aggregate demand](../../International%20Finance/Economic%20Stabilization%20Notes/Macroeconomic%20Models%20of%20Business%20Cycles.md) for [physical settlement](../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%203%20-%20Futures%20Markets/Fundamentals%20of%20Futures%20and%20Forwards.md).
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

- CDS indices provide diversified exposure to [credit markets](../../Credit%20Markets/Credit%20Markets%20Session%201.md) and are widely used for [hedging](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%205/Key%20Rates%20O1s%20Durations%20and%20Hedging.md) and speculative purposes.
- **Key Features**:
  - Equally weighted at issuance for simplicity and diversification.
  - Issued semiannually with multiple maturities (e.g.,  1,  3,  5,  7,  and 10 years).
  - Most liquid series is the "on-the-run" index.

### 5.2 Standard CDS Indices

| **Name** | **Domicile and Type of Credits** | **Number of Credits** |

| **[CDX.NA.IG](../../Financial%20Instruments/Financial%20Derivatives%20and%20Quantitative%20Methods/Credit%20Default%20Swaps.md)** | North American [investment](../../Advanced%20Investments/An%20Asset%20Allocation%20Primer.md)-grade | 125 |

| **CDX.NA.HY** | North American high-yield | 100 |

| **CDX.NA.XO** | North American crossover | 35 |

| **CDX.EM** | Emerging market sovereign | 15 |

| **CDX.EM.Diversified** | Emerging market sovereign/corporate | 40 |

| **[iTraxx](../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20II%20CASH%20FLOW%20ENGINEERING/Chapter%2010%20-%20Collateralized%20Debt%20Obligations%20and%20Basket%20Credit%20Derivatives/Credit%20Derivative%20Indexes.md) Europe** | European [investment](../../Advanced%20Investments/An%20Asset%20Allocation%20Primer.md)-grade | 125 |

| **[iTraxx](../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20II%20CASH%20FLOW%20ENGINEERING/Chapter%2010%20-%20Collateralized%20Debt%20Obligations%20and%20Basket%20Credit%20Derivatives/Credit%20Derivative%20Indexes.md) Europe XO** | European crossover | 40 |

| **[iTraxx](../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20II%20CASH%20FLOW%20ENGINEERING/Chapter%2010%20-%20Collateralized%20Debt%20Obligations%20and%20Basket%20Credit%20Derivatives/Credit%20Derivative%20Indexes.md) Japan** | Japanese [investment](../../Advanced%20Investments/An%20Asset%20Allocation%20Primer.md)-grade | 50 |

| **[iTraxx](../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20II%20CASH%20FLOW%20ENGINEERING/Chapter%2010%20-%20Collateralized%20Debt%20Obligations%20and%20Basket%20Credit%20Derivatives/Credit%20Derivative%20Indexes.md) Asia ex-Japan**| Asian non-Japanese [investment](../../Advanced%20Investments/An%20Asset%20Allocation%20Primer.md)-grade | 50 |

| **[iTraxx](../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20II%20CASH%20FLOW%20ENGINEERING/Chapter%2010%20-%20Collateralized%20Debt%20Obligations%20and%20Basket%20Credit%20Derivatives/Credit%20Derivative%20Indexes.md) Australia** | Australian [investment](../../Advanced%20Investments/An%20Asset%20Allocation%20Primer.md)-grade | 25 |

### 5.3 Mechanics of CDS Indices

- **Premium Leg**:
  - The buyer pays a fixed coupon based on the surviving notional of the reference [portfolio](../../Advanced%20Investments/An%20Asset%20Allocation%20Primer.md).
  - The surviving notional decreases as credits in the [portfolio](../../Advanced%20Investments/An%20Asset%20Allocation%20Primer.md) experience credit events.
- **Protection Leg**:
  - The seller compensates the buyer for losses due to credit events,  based on the [recovery rate](../../Credit%20Markets/Credit%20Markets%20Session%203.md) of defaulted credits.

## 6. Applications of CDS and CDS Indices

### 6.1 Hedging Credit Risk

- CDS and CDS indices provide efficient tools for [hedging](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%205/Key%20Rates%20O1s%20Durations%20and%20Hedging.md) [credit risk](../../Course%20Notes/Quantitative%20Trading%20Strategies%20Lecture%20Notes.md) in individual credits or broad portfolios.
- **Example**:
  - A bank can hedge its exposure to a [portfolio](../../Advanced%20Investments/An%20Asset%20Allocation%20Primer.md) of [Corporate Bonds](../../Financial%20Markets%20and%20Institutions/II.%20The%20Roles%20of%20Banks%20and%20Derivative%20Markets%20in%20Resolving%20Problems%20Inherent%20in%20Debt%20Contracts/Class%202-%20Debt%20Contracts%20due%20to%20Lack%20of%20Information/Class%20Notes%202%20–%20Corporate%20Bond%20Contracts.md) by buying protection on a CDS index.

### 6.2 Speculation and Arbitrage

- CDS indices allow investors to express views on [credit markets](../../Credit%20Markets/Credit%20Markets%20Session%201.md) or exploit mispricings.
- **Example**:
  - Selling protection on a CDS index is equivalent to taking a [long position](../../Financial%20Engineering/Derivatives/Part%20I%20-%20Forwards%20and%20Futures/Chapter%204%20-%20Futures:%20Hedging%20and%20Speculation.md) on the creditworthiness of the reference [portfolio](../../Advanced%20Investments/An%20Asset%20Allocation%20Primer.md).

### 6.3 Regulatory Capital Management

- Banks use CDS to reduce [regulatory capital requirements](../../Financial%20Markets%20and%20Institutions/III.%20Liquidity%20of%20Assets/Class%207-%20CP,%20Repo,%20and%20the%20Crisis/Case%20Study%20of%20Northern%20Rock.md) by transferring [credit risk](../../Course%20Notes/Quantitative%20Trading%20Strategies%20Lecture%20Notes.md) to third parties.

## 7. Summary and Key Takeaways

### 7.1 Innovations in the CDS Market

- The 2009 Big Bang Protocol introduced centralized [credit event](../../Financial%20Engineering/Valuation%20of%20Credit%20Default%20Swaps.md) determination and auction-based settlement,  improving transparency and efficiency.
- The compression cycle has significantly reduced systemic risk by eliminating redundant contracts.

### 7.2 CDS Indices

- CDS indices provide diversified credit exposure and are widely used for [hedging](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%205/Key%20Rates%20O1s%20Durations%20and%20Hedging.md) and speculative purposes.
- The mechanics of CDS indices mirror those of individual CDS contracts,  with adjustments for the surviving notional of the reference [portfolio](../../Advanced%20Investments/An%20Asset%20Allocation%20Primer.md).

By understanding the mechanics,  [pricing](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%207/Arbitrage%20Pricing%20of%20Derivatives.md),  and applications of CDS and CDS indices,  financial professionals can effectively manage [credit risk](../../Course%20Notes/Quantitative%20Trading%20Strategies%20Lecture%20Notes.md) and optimize their [investment](../../Advanced%20Investments/An%20Asset%20Allocation%20Primer.md) strategies.

# Lecture Notes: Credit Default Swaps (CDS) and CDS Indices – Mechanics,  Valuation,  and Risk Management

## 1. Introduction to Credit Default Swaps (CDS) and CDS Indices

- Credit Default Swaps (CDS) are [financial derivatives](../../Financial%20Instruments/Financial%20Instruments%20PSET%20Solutions.md) that allow the transfer of [credit risk](../../Course%20Notes/Quantitative%20Trading%20Strategies%20Lecture%20Notes.md) from one party to another. They are widely used for [hedging](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%205/Key%20Rates%20O1s%20Durations%20and%20Hedging.md),  speculation,  and structured credit investments.
- CDS indices are portfolios of CDS contracts that provide diversified exposure to [credit markets](../../Credit%20Markets/Credit%20Markets%20Session%201.md),  enabling investors to hedge or speculate on macro-level [credit risk](../../Course%20Notes/Quantitative%20Trading%20Strategies%20Lecture%20Notes.md) efficiently.
- This lecture focuses on:
  - The mechanics of CDS and CDS indices.
  - Valuation methodologies for CDS contracts.
  - The relationship between CDS and bond markets.
  - [Risk management](../../Financial%20Engineering/Financial%20Mathematics%20Course.md) and [trading strategies](../../Course%20Notes/Quantitative%20Trading%20Strategies%20Lecture%20Notes.md) involving CDS and CDS indices.

## 2. Mechanics of CDS Contracts

### 2.1 Key Features of CDS Contracts

- **[Protection Buyer](../../Financial%20Instruments/Financial%20Derivatives%20and%20Quantitative%20Methods/Credit%20Default%20Swaps.md)**: Pays a regular premium (fixed coupon) to the [protection seller](../../Financial%20Instruments/Financial%20Derivatives%20and%20Quantitative%20Methods/Credit%20Default%20Swaps.md) in exchange for protection against credit events.
- **[Protection Seller](../../Financial%20Instruments/Financial%20Derivatives%20and%20Quantitative%20Methods/Credit%20Default%20Swaps.md)**: Receives the premium and compensates the buyer if a [credit event](../../Financial%20Engineering/Valuation%20of%20Credit%20Default%20Swaps.md) occurs.
- **[Reference Entity](../../Financial%20Instruments/Lecture%20Notes-%20Financial%20Instruments/Lecture%20Notes%209A-%20Credit%20Default%20Swaps.md)**: The corporate or sovereign issuer whose [credit risk](../../Course%20Notes/Quantitative%20Trading%20Strategies%20Lecture%20Notes.md) is being transferred.
- **Credit Events**: Events that trigger the protection leg,  such as bankruptcy,  failure to pay,  obligation acceleration,  repudiation/moratorium,  and restructuring.
- **Notional Amount**: The face value of the debt being protected.

### 2.2 Premium Leg

- The premium leg consists of regular fixed payments made by the [protection buyer](../../Financial%20Instruments/Financial%20Derivatives%20and%20Quantitative%20Methods/Credit%20Default%20Swaps.md) to the [protection seller](../../Financial%20Instruments/Financial%20Derivatives%20and%20Quantitative%20Methods/Credit%20Default%20Swaps.md).
- **Formula**:
 $\text{Premium Payment} = \text{Fixed Coupon} \times \text{Notional Amount} \times \text{Year Fraction (Actual/360)}$$
- Payments continue until the contract matures or a [credit event](../../Financial%20Engineering/Valuation%20of%20Credit%20Default%20Swaps.md) occurs.
- If a [credit event](../../Financial%20Engineering/Valuation%20of%20Credit%20Default%20Swaps.md) occurs between two payment dates,  the accrued portion of the premium is paid by the [protection buyer](../../Financial%20Instruments/Financial%20Derivatives%20and%20Quantitative%20Methods/Credit%20Default%20Swaps.md).

### 2.3 Protection Leg

- The protection leg is a contingent payment made by the [protection seller](../../Financial%20Instruments/Financial%20Derivatives%20and%20Quantitative%20Methods/Credit%20Default%20Swaps.md) to the [protection buyer](../../Financial%20Instruments/Financial%20Derivatives%20and%20Quantitative%20Methods/Credit%20Default%20Swaps.md) if a [credit event](../../Financial%20Engineering/Valuation%20of%20Credit%20Default%20Swaps.md) occurs.
- **Formula**:
 $\text{Protection Payment} = \text{Notional Amount} \times (1 - \text{Recovery Rate})$$
  - **[Recovery Rate](../../Credit%20Markets/Credit%20Markets%20Session%203.md)**: The market-determined value of the deliverable obligations after a [credit event](../../Financial%20Engineering/Valuation%20of%20Credit%20Default%20Swaps.md).
- Settlement can be:
  - **[Cash Settlement](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%2016/Swaptions.md)**: The seller pays the difference between par and the recovery price.
  - **[Physical Settlement](../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%203%20-%20Futures%20Markets/Fundamentals%20of%20Futures%20and%20Forwards.md)**: The buyer delivers the impaired obligations to the seller in exchange for the notional amount.

### 2.4 Upfront Payment

- The upfront payment adjusts for the difference between the fixed coupon and the market-implied [credit spread](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%2014/Cds-Equivalent%20Bond%20Spread.md) of the [reference entity](../../Financial%20Instruments/Lecture%20Notes-%20Financial%20Instruments/Lecture%20Notes%209A-%20Credit%20Default%20Swaps.md).
- **Key Insights**:
  - If the fixed coupon is lower than the market-implied spread,  the [protection buyer](../../Financial%20Instruments/Financial%20Derivatives%20and%20Quantitative%20Methods/Credit%20Default%20Swaps.md) makes an upfront payment to the seller.
  - If the fixed coupon is higher than the market-implied spread,  the seller makes an upfront payment to the buyer.

## 3. Mechanics of CDS Indices

### 3.1 Premium Leg of CDS Indices

- The premium leg of a CDS index is equivalent to a [portfolio](../../Advanced%20Investments/An%20Asset%20Allocation%20Primer.md) of CDS premium legs linked to each reference credit in the index.
- All reference credits pay a fixed coupon equal to the index coupon.
- Payments continue until the contract matures or all credits in the index experience credit events (an unlikely scenario).

### 3.2 Protection Leg of CDS Indices

- The protection leg of a CDS index mirrors that of an equally weighted [portfolio](../../Advanced%20Investments/An%20Asset%20Allocation%20Primer.md) of CDS protection legs on the reference credits.
- **Process for Credit Events**:
  1. The affected credit is removed from the index across all maturities.
  1. The index is assigned a new version number to distinguish it from earlier versions.
  1. The removed credit becomes a standalone CDS position with a notional corresponding to its size in the index.
	 - Example: If the index notional is $10 million and there are 125 credits,    the standalone CDS notional is $80,  000.
  1. The standalone CDS participates in the standard [auction process](../../Financial%20Markets/Financial%20Trading%20and%20Markets/Chapter%202%20Securities%20Markets.md) to determine the [recovery rate](../../Credit%20Markets/Credit%20Markets%20Session%203.md).

### 3.3 Restructuring Credit Events in CDS Indices

- If the [credit event](../../Financial%20Engineering/Valuation%20of%20Credit%20Default%20Swaps.md) is a restructuring:
  - The index buyer and seller can choose to trigger the standalone CDS contract.
  - If neither party triggers,  the standalone CDS remains on their books until maturity or a subsequent [credit event](../../Financial%20Engineering/Valuation%20of%20Credit%20Default%20Swaps.md).
  - Restructuring is excluded as a [credit event](../../Financial%20Engineering/Valuation%20of%20Credit%20Default%20Swaps.md) in North American indices but included in European and Asian indices.

## 4. Valuation of CDS Contracts

### 4.1 Expected Present Value of Cash Flows

- The value of a CDS contract is the expected present value of [future cash flows](../../Financial%20Engineering/Advanced%20Derivatives%20Pricing%20Methodology.md),  calculated under the [risk-neutral measure](../../Financial%20Engineering/Verifying%20Martingale%20Property%20with%20Q.md).
- **Premium Leg Value**:
  - The expected present value of fixed [coupon payments](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%203/Realized%20Returns.md) until maturity or a [credit event](../../Financial%20Engineering/Valuation%20of%20Credit%20Default%20Swaps.md).
  - Falls if the [credit quality](../../Financial%20Markets%20and%20Institutions/II.%20The%20Roles%20of%20Banks%20and%20Derivative%20Markets%20in%20Resolving%20Problems%20Inherent%20in%20Debt%20Contracts/Class%202-%20Debt%20Contracts%20due%20to%20Lack%20of%20Information/Wellman%20Inc%20the%20Importance%20of%20Loan%20Covenants.md) deteriorates,  as fewer coupons are expected to be received.
- **Protection Leg Value**:
  - The expected present value of the contingent payment (par minus [recovery rate](../../Credit%20Markets/Credit%20Markets%20Session%203.md)) in the event of default.
  - Increases if the [credit quality](../../Financial%20Markets%20and%20Institutions/II.%20The%20Roles%20of%20Banks%20and%20Derivative%20Markets%20in%20Resolving%20Problems%20Inherent%20in%20Debt%20Contracts/Class%202-%20Debt%20Contracts%20due%20to%20Lack%20of%20Information/Wellman%20Inc%20the%20Importance%20of%20Loan%20Covenants.md) deteriorates,  as the likelihood of default rises.

### 4.2 No-Arbitrage Relationship Between CDS and Bonds

- There is a fundamental no-[arbitrage](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%207/Arbitrage%20Pricing%20of%20Derivatives.md) relationship between the upfront cost of a CDS and the price of a floating-rate bond issued by the same [reference entity](../../Financial%20Instruments/Lecture%20Notes-%20Financial%20Instruments/Lecture%20Notes%209A-%20Credit%20Default%20Swaps.md).
- **Key Insight**:
  - The upfront cost of a CDS equals the difference between par and the bond price,  adjusted for [accrued interest](../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%202%20-%20Spot%20Markets/Intra-Year%20Compounding%20and%20Day-Count.md) and recovery assumptions.
- **Simplifying Assumptions**:
  1. The bond is funded at [Basis Swap](A%20Guide%20to%20the%20Front%20End%20and%20[[Basis%20Swaps) Markets#[London Interbank Offered Rate](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%2012/Short-Term%20Rates%20and%20the%20Transition%20from%20LIBOR.md) (LIBOR)|LIBOR]] flat.
  1. The bond pays a floating rate coupon equal to [Basis Swap](A%20Guide%20to%20the%20Front%20End%20and%20[[Basis%20Swaps) Markets#[London Interbank Offered Rate](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%2012/Short-Term%20Rates%20and%20the%20Transition%20from%20LIBOR.md) (LIBOR)|LIBOR]] plus the CDS fixed spread.
  1. The [credit event](../../Financial%20Engineering/Valuation%20of%20Credit%20Default%20Swaps.md) occurs on a coupon payment date.

### 4.3 The CDS Basis

- The CDS basis is the difference between the CDS par spread and the bond [Basis Swap](A%20Guide%20to%20the%20Front%20End%20and%20[[Basis%20Swaps) Markets#[London Interbank Offered Rate](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%2012/Short-Term%20Rates%20and%20the%20Transition%20from%20LIBOR.md) (LIBOR)|LIBOR]] spread.
- **Formula**:
 $\text{CDS Basis} = \text{CDS Par Spread} - \text{Bond [](../Fixed%20Income%20Lecture%20Notes/A%20Guide%20to%20the%20Front%20End%20and%20Basis%20Swap%20Markets.md#London%20Interbank%20Offered%20Rate%20(LIBOR)|LIBOR) Spread}$$
- **Applications**:
  - Basis trading involves exploiting discrepancies between CDS spreads and bond spreads.
  - A "[negative basis trade](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%2014/Cds-Bond%20Basis.md)" involves buying the bond and buying CDS protection,  earning the bond spread while paying the [CDS spread](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%2014/Cds-Equivalent%20Bond%20Spread.md).

## 5. Risk Management and Trading Strategies

### 5.1 Hedging Credit Risk

- CDS contracts provide an efficient way to hedge [credit risk](../../Course%20Notes/Quantitative%20Trading%20Strategies%20Lecture%20Notes.md) without selling the underlying bonds or loans.
- **Example**:
  - A bank holding [Corporate Bonds](../../Financial%20Markets%20and%20Institutions/II.%20The%20Roles%20of%20Banks%20and%20Derivative%20Markets%20in%20Resolving%20Problems%20Inherent%20in%20Debt%20Contracts/Class%202-%20Debt%20Contracts%20due%20to%20Lack%20of%20Information/Class%20Notes%202%20–%20Corporate%20Bond%20Contracts.md) can buy CDS protection to hedge against [default risk](../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%207%20-%20Default%20Risk%20and%20Credit%20Derivatives/Default%20Risk%20and%20Credit%20Derivatives%20183.md).

### 5.2 Speculation and Arbitrage

- CDS contracts enable investors to express views on the creditworthiness of a [reference entity](../../Financial%20Instruments/Lecture%20Notes-%20Financial%20Instruments/Lecture%20Notes%209A-%20Credit%20Default%20Swaps.md).
- **Example**:
  - Buying CDS protection is equivalent to [shorting](../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%202%20-%20Spot%20Markets/Short%20Selling.md) the [credit risk](../../Course%20Notes/Quantitative%20Trading%20Strategies%20Lecture%20Notes.md) of the [reference entity](../../Financial%20Instruments/Lecture%20Notes-%20Financial%20Instruments/Lecture%20Notes%209A-%20Credit%20Default%20Swaps.md).
  - Selling CDS protection is equivalent to going long on the [credit risk](../../Course%20Notes/Quantitative%20Trading%20Strategies%20Lecture%20Notes.md) of the [reference entity](../../Financial%20Instruments/Lecture%20Notes-%20Financial%20Instruments/Lecture%20Notes%209A-%20Credit%20Default%20Swaps.md).

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

- The [CDS market](../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20II%20CASH%20FLOW%20ENGINEERING/Chapter%2010%20-%20Collateralized%20Debt%20Obligations%20and%20Basket%20Credit%20Derivatives/Credit%20Derivative%20Indexes.md) underwent significant reforms after the 2008 [financial crisis](../../Financial%20Markets%20and%20Institutions/III.%20Liquidity%20of%20Assets/Class%209-%20Bailouts%20and%20Bank%20Failures/Squam%20Lake%20Group%20Letter.md) to improve transparency,  reduce systemic risk,  and ensure market-wide settlement mechanisms.
- **Key Changes**:
  - [Introduction](../../Financial%20Markets%20and%20Institutions/III.%20Liquidity%20of%20Assets/Class%209-%20Bailouts%20and%20Bank%20Failures/Squam%20Lake%20Group%20Introduction.md) of centralized counterparties (CCPs) to reduce counterparty risk.
  - Standardized auction processes for [credit event](../../Financial%20Engineering/Valuation%20of%20Credit%20Default%20Swaps.md) settlement.
  - Increased transparency through data publication by the DTCC.

### 6.2 Applications of CDS and CDS Indices

- **[Hedging](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%205/Key%20Rates%20O1s%20Durations%20and%20Hedging.md)**: Protect against credit losses on individual credits or portfolios.
- **Speculation**: Express views on creditworthiness or market-wide [credit risk](../../Course%20Notes/Quantitative%20Trading%20Strategies%20Lecture%20Notes.md).
- **Yield Enhancement**: Earn premiums by selling protection.
- **Regulatory Capital Management**: Reduce capital requirements by transferring [credit risk](../../Course%20Notes/Quantitative%20Trading%20Strategies%20Lecture%20Notes.md).

## 7. Summary and Key Takeaways

### 7.1 CDS Contracts

- CDS contracts [transfer credit risk](../../Financial%20Instruments/Financial%20Derivatives%20and%20Quantitative%20Methods/Credit%20Default%20Swaps.md) from the [protection buyer](../../Financial%20Instruments/Financial%20Derivatives%20and%20Quantitative%20Methods/Credit%20Default%20Swaps.md) to the [protection seller](../../Financial%20Instruments/Financial%20Derivatives%20and%20Quantitative%20Methods/Credit%20Default%20Swaps.md).
- The value of a CDS contract depends on the expected present value of the premium and protection legs.

### 7.2 CDS Indices

- CDS indices provide diversified exposure to [credit markets](../../Credit%20Markets/Credit%20Markets%20Session%201.md) and are widely used for [hedging](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%205/Key%20Rates%20O1s%20Durations%20and%20Hedging.md) and speculative purposes.
- The mechanics of CDS indices mirror those of individual CDS contracts,  with adjustments for the surviving notional of the reference [portfolio](../../Advanced%20Investments/An%20Asset%20Allocation%20Primer.md).

### 7.3 Risk Management

- CDS contracts and indices are versatile tools for managing [credit risk](../../Course%20Notes/Quantitative%20Trading%20Strategies%20Lecture%20Notes.md),  enabling investors to hedge,  speculate,  and optimize their portfolios.
- Basis trading and other strategies exploit discrepancies between CDS and bond markets.

By mastering the mechanics,  valuation,  and applications of CDS and CDS indices,  financial professionals can effectively manage [credit risk](../../Course%20Notes/Quantitative%20Trading%20Strategies%20Lecture%20Notes.md) and enhance [portfolio](../../Advanced%20Investments/An%20Asset%20Allocation%20Primer.md) performance.

# Lecture Notes: Credit Default Swaps (CDS) – Par Spreads,  Flat Quoted Spreads,  and Valuation

## 1. Introduction to Par Spreads and Flat Quoted Spreads

- **Par Spread ($S(t,    T)$)**: The par spread is the coupon rate on a CDS contract that results in no upfront cost at inception. It is the spread that equates the present value of the premium leg to the present value of the protection leg.
- **Flat Quoted Spread ($\bar{\mathcal{S}}(t,    T)$)**: The flat quoted spread is the level of a flat CDS par spread curve that matches the model-implied upfront value to the market-quoted upfront value. It assumes a flat [term structure](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%209/The%20Vasicek%20Model.md) of spreads and is analogous to the bond yield-to-maturity.

### 1.1 Key Differences Between Par Spreads and Flat Quoted Spreads

- **Par Spread**:
  - Requires knowledge of the full [term structure](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%209/The%20Vasicek%20Model.md) of par spreads for accurate valuation.
  - Cannot be used to imply a [term structure](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%209/The%20Vasicek%20Model.md) of spreads from a single upfront value.
  - Was the market standard until 2010.
- **Flat Quoted Spread**:
  - Assumes a flat spread curve,  simplifying the valuation process.
  - Provides a one-to-one mapping between the quoted flat spread and the upfront cost of a CDS contract.
  - Has become the market standard since 2010 due to its simplicity and ease of use.

### 1.2 Relationship Between Par Spreads and Flat Quoted Spreads

- If the [term structure](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%209/The%20Vasicek%20Model.md) of par spreads is flat,  the par spread and flat quoted spread are equal for all maturities.
- If the [term structure](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%209/The%20Vasicek%20Model.md) is not flat,  the flat quoted spread provides an approximation that ignores the shape of the [term structure](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%209/The%20Vasicek%20Model.md).

## 2. Valuation Model for CDS Contracts

### 2.1 Requirements for the Model

The valuation model for CDS contracts must satisfy the following:

1. Capture credit events as single events that can occur at any future time.
1. Account for the timing of defaults and allow for a [term structure](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%209/The%20Vasicek%20Model.md) of [default probabilities](../../Credit%20Markets/Credit%20Markets%20Session%203.md).
1. Incorporate the payment of par minus the [recovery rate](../../Credit%20Markets/Credit%20Markets%20Session%203.md) following a [credit event](../../Financial%20Engineering/Valuation%20of%20Credit%20Default%20Swaps.md).
1. Reprice the [term structure](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%209/The%20Vasicek%20Model.md) of market prices exactly.
1. Be fast to calibrate and compute.

### 2.2 Survival Probability ($Q(T)$)

- **Definition**: The [survival probability](../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%207%20-%20Default%20Risk%20and%20Credit%20Derivatives/A%20Poisson%20Model%20of%20Single%20Issuer%20Default.md) $Q(T)$ is the probability that the [reference entity](../../Financial%20Instruments/Lecture%20Notes-%20Financial%20Instruments/Lecture%20Notes%209A-%20Credit%20Default%20Swaps.md) survives without experiencing a [credit event](../../Financial%20Engineering/Valuation%20of%20Credit%20Default%20Swaps.md) from today (time 0) to time $T$.
- **Properties**:
  - $Q(T)$ is a constant or decreasing function of $T$.
  - $Q(T)$ lies between 0 and 1.

## 3. Valuation of the Premium Leg

### 3.1 Premium Leg Formula

The premium leg represents the expected present value of the fixed [coupon payments](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%203/Realized%20Returns.md) made by the [protection buyer](../../Financial%20Instruments/Financial%20Derivatives%20and%20Quantitative%20Methods/Credit%20Default%20Swaps.md). It is given by:
$$
V_{\text{Premium}} = C(T) \sum_{i=1}^N \Delta(t_{i-1},    t_i) Z(t_i) Q(t_i)
$$

Where:

- $C(T)$: Fixed coupon (par spread or quoted spread).
- $\Delta(t_{i-1},    t_i)$: Year fraction between coupon payment dates.
- $Z(t_i)$: [Discount factor](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%201/Discount%20Factors.md) at time $t_i$.
- $Q(t_i)$: [Survival probability](../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%207%20-%20Default%20Risk%20and%20Credit%20Derivatives/A%20Poisson%20Model%20of%20Single%20Issuer%20Default.md) at time $t_i$.

### 3.2 Accrued Coupon Adjustment

- If a [credit event](../../Financial%20Engineering/Valuation%20of%20Credit%20Default%20Swaps.md) occurs between coupon payment dates,  the accrued coupon must be accounted for.
- **Accrued Coupon Contribution**:
 $
  \frac{C(T)}{2} \sum_{i=1}^N \Delta(t_{i-1},    t_i) Z(t_i) (Q(t_{i-1}) - Q(t_i))
 $

### 3.3 Total Premium Leg Value

Combining the regular [coupon payments](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%203/Realized%20Returns.md) and the accrued coupon adjustment,  the total premium leg value is:
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

The protection leg represents the expected present value of the contingent payment made by the [protection seller](../../Financial%20Instruments/Financial%20Derivatives%20and%20Quantitative%20Methods/Credit%20Default%20Swaps.md) in the event of a [credit event](../../Financial%20Engineering/Valuation%20of%20Credit%20Default%20Swaps.md). It is given by:
$$
V_{\text{Protection}} = (1 - R) \sum_{n=1}^M Z(t_n) (Q(t_{n-1}) - Q(t_n))
$$

Where:

- $R$: [Recovery rate](../../Credit%20Markets/Credit%20Markets%20Session%203.md) (assumed to be 40% for senior [unsecured debt](../../Course%20Notes/HBR%20Notes/HBR%20Case%20Study-%20Oaktree.md)).
- $Q(t_{n-1}) - Q(t_n)$: Probability of default between $t_{n-1}$ and $t_n$.

## 5. Upfront Cost of a CDS Contract

### 5.1 Definition

The upfront cost $U(0)$ is the cost paid by the [protection buyer](../../Financial%20Instruments/Financial%20Derivatives%20and%20Quantitative%20Methods/Credit%20Default%20Swaps.md) to enter into a CDS contract. It is the difference between the protection leg value and the premium leg value:
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

- The [survival probability](../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%207%20-%20Default%20Risk%20and%20Credit%20Derivatives/A%20Poisson%20Model%20of%20Single%20Issuer%20Default.md) $Q(T)$ is expressed in terms of the continuously compounded forward default rate $h(t)$:
$$
Q(T) = \exp\left(-\int_0^T h(t) dt\right)
$$

- A piecewise flat [term structure](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%209/The%20Vasicek%20Model.md) of $h(t)$ is commonly used for [calibration](../../Credit%20Markets/Credit%20Markets%20Session%204.md).

### 6.2 Bootstrap Calibration

The [calibration](../../Credit%20Markets/Credit%20Markets%20Session%204.md) process involves determining the values of $h(t)$ that match the model-implied upfront values to the market-quoted upfront values for CDS contracts of different maturities.

1. Start with the shortest maturity (e.g.,  6 months) and solve for $h(0.5)$.
1. Use $h(0.5)$ to solve for $h(1.0)$ using the 1-year [CDS upfront](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%2014/CDS%20Upfront%20Amounts.md) value.
1. Repeat for longer maturities.

## 7. Risk Management: Spread DV01

### 7.1 Definition

The Spread DV01 measures the sensitivity of the upfront value of a CDS contract to a 1 basis point parallel shift in the [CDS spread](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%2014/Cds-Equivalent%20Bond%20Spread.md) curve:
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

- Par spreads require knowledge of the full [term structure](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%209/The%20Vasicek%20Model.md) of spreads,  while flat quoted spreads assume a flat curve and simplify valuation.

### 8.2 Valuation of CDS Contracts

- The premium leg and protection leg are valued using survival probabilities,  discount factors,  and recovery rates.
- The upfront cost is the difference between the protection leg value and the premium leg value.

### 8.3 Risk Management

- Spread DV01 measures the sensitivity of a CDS contract to changes in the spread curve and is a key tool for [hedging](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%205/Key%20Rates%20O1s%20Durations%20and%20Hedging.md) [credit risk](../../Course%20Notes/Quantitative%20Trading%20Strategies%20Lecture%20Notes.md).

By understanding the mechanics,  valuation,  and [risk management](../../Financial%20Engineering/Financial%20Mathematics%20Course.md) of CDS contracts,  financial professionals can effectively manage [credit risk](../../Course%20Notes/Quantitative%20Trading%20Strategies%20Lecture%20Notes.md) and optimize their portfolios.

# Lecture Notes: Interest Rate Duration of a CDS and CDS Index Valuation

## 1. Introduction to Interest Rate Sensitivity of a CDS

- The **[interest rate sensitivity](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%2011/Forward%20Bond%20Yield.md)** of a CDS contract is measured by its **IR DV01** (Interest Rate Dollar Value of 01). This metric quantifies the change in the upfront value of the CDS for a 1 basis point (bp) parallel upward shift in the [Basis Swap](A%20Guide%20to%20the%20Front%20End%20and%20[[Basis%20Swaps) Markets#[London Interbank Offered Rate](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%2012/Short-Term%20Rates%20and%20the%20Transition%20from%20LIBOR.md) (LIBOR)|LIBOR]] curve,  while keeping the par spread curve fixed.
- The IR DV01 is derived from the dependency of the CDS valuation on the **risky annuity**,  which is the present value of future premium payments.

### 1.1 Formula for IR DV01

The IR DV01 is given by:
$$
\text{IR DV01} = (C - S) \cdot \left(A^*(T) - A(T)\right)
$$

Where:

- \(C\): Deal spread (fixed coupon of the CDS).
- \(S\): Quoted spread (flat spread reflecting the [credit risk](../../Course%20Notes/Quantitative%20Trading%20Strategies%20Lecture%20Notes.md) of the [reference entity](../../Financial%20Instruments/Lecture%20Notes-%20Financial%20Instruments/Lecture%20Notes%209A-%20Credit%20Default%20Swaps.md)).
- \(A(T)\): Risky annuity calculated using the original interest rate curve.
- \(A^*(T)\): Risky annuity calculated using the bumped interest rate curve.

### 1.2 Key Observations

1. **Sign of IR DV01**:
   - If \(C = S\),  the IR DV01 is zero because the CDS is priced at par.
   - If \(C > S\),  the IR DV01 is positive because the CDS buyer is overpaying for protection,  and the value of the risky annuity decreases with higher rates.
   - If \(C < S\),  the IR DV01 is negative because the CDS buyer is underpaying for protection,  and the value of the risky annuity decreases with higher rates.

1. **Magnitude of IR DV01**:
   - The [interest rate sensitivity](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%2011/Forward%20Bond%20Yield.md) of a CDS is generally low compared to a fixed-rate corporate bond with the same maturity. This is because:
	 - A CDS is effectively a credit-risky annuity with annualized [coupon payments](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%203/Realized%20Returns.md) of \((C - S)\).
	 - Unlike a bond,  a CDS does not involve a par payment at maturity.

1. **Comparison to Floating-Rate Notes**:
   - The [interest rate sensitivity](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%2011/Forward%20Bond%20Yield.md) of a CDS closely resembles that of a par floating-rate note issued by the [reference entity](../../Financial%20Instruments/Lecture%20Notes-%20Financial%20Instruments/Lecture%20Notes%209A-%20Credit%20Default%20Swaps.md),  as both instruments are primarily driven by credit spreads rather than [interest rates](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%202/Interest%20Rate%20Quotations.md).

## 2. Example: IR DV01 of a CDS Contract

### 2.1 CDS Contract Details (Exhibit 69-5)

| **Parameter** | **Value** |

| Notional | $10,  000,  000 |

| Trade Date | February 3,  2011 |

| Maturity | March 20,  2016 |

| Deal Spread (\(C\)) | 100 bp |

| Quoted Spread (\(S\)) | 34.32 bp |

| [Recovery Rate](../../Credit%20Markets/Credit%20Markets%20Session%203.md) | 40% |

| IR DV01 | $84.26 |

### 2.2 Explanation of Valuation Outputs

1. **Price**:
   - The "clean" price of the CDS excludes [accrued interest](../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%202%20-%20Spot%20Markets/Intra-Year%20Compounding%20and%20Day-Count.md) and represents the value of the contract for a [protection seller](../../Financial%20Instruments/Financial%20Derivatives%20and%20Quantitative%20Methods/Credit%20Default%20Swaps.md) who buys the CDS along with a par [Basis Swap](A%20Guide%20to%20the%20Front%20End%20and%20[[Basis%20Swaps) Markets#[London Interbank Offered Rate](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%2012/Short-Term%20Rates%20and%20the%20Transition%20from%20LIBOR.md) (LIBOR)|LIBOR]] floating-rate note.

1. **Principal**:
   - The clean value of the contract,  excluding [accrued interest](../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%202%20-%20Spot%20Markets/Intra-Year%20Compounding%20and%20Day-Count.md). For this CDS,  the principal value is \(-\$322,  035\).

1. **[Accrued Interest](../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%202%20-%20Spot%20Markets/Intra-Year%20Compounding%20and%20Day-Count.md)**:
   - The accrued coupon since the last payment date (December 20,  2010) is \(-\$12,  778\),  reflecting 46 days of a 100 bp coupon.

1. **Cash Amount**:
   - The actual upfront payment required to enter the contract is \(-\$334,  813\). This reflects the compensation to the [protection buyer](../../Financial%20Instruments/Financial%20Derivatives%20and%20Quantitative%20Methods/Credit%20Default%20Swaps.md) for paying a deal spread (\(C = 100\) bp) higher than the quoted spread (\(S = 34.32\) bp).

1. **Spread DV01**:
   - The spread sensitivity of the CDS is \$5,  036.41,  meaning a 1 bp increase in the quoted spread curve increases the value of the CDS by this amount.

1. **IR DV01**:
   - The [interest rate sensitivity](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%2011/Forward%20Bond%20Yield.md) of the CDS is \$84.26,  which is much smaller than the spread DV01,  highlighting that the CDS is primarily a credit-spread product.

## 3. Risky Annuity and Approximation for CDS Valuation

### 3.1 Risky Annuity Formula

The risky annuity \(A(T)\) is the present value of future premium payments,  adjusted for survival probabilities and discount factors. For a simplified approximation:
$$
A(\bar{S},    T) = \frac{1 - \exp\left(-\left(W + \frac{\bar{S}}{1 - R}\right)T\right)}{W + \frac{\bar{S}}{1 - R}} \cdot \frac{365}{360}
$$

Where:

- \(W\): [Swap rate](../Fixed%20Income%20Lecture%20Notes/Teaching%20Note%204%20Interest%20Rate%20Derivatives.md) to the contract maturity.
- \(\bar{S}\): Quoted spread.
- \(R\): [Recovery rate](../../Credit%20Markets/Credit%20Markets%20Session%203.md).
- \(T\): [Time to maturity](../../Financial%20Instruments/Lecture%20Notes-%20Financial%20Instruments/Teaching%20Note%201-%20Forward%20Rates%20Agreement/Hedging%20Strategies%20with%20Forwards.md).

### 3.2 Example Calculation

Using the CDS details from Exhibit 69-5:

- Quoted spread (\(\bar{S}\)): 34.32 bp.
- [Time to maturity](../../Financial%20Instruments/Lecture%20Notes-%20Financial%20Instruments/Teaching%20Note%201-%20Forward%20Rates%20Agreement/Hedging%20Strategies%20with%20Forwards.md) (\(T\)): 5.122 years.
- [Swap rate](../Fixed%20Income%20Lecture%20Notes/Teaching%20Note%204%20Interest%20Rate%20Derivatives.md) (\(W\)): 2.4%.
- [Recovery rate](../../Credit%20Markets/Credit%20Markets%20Session%203.md) (\(R\)): 40%.

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

- A CDS index is equivalent to a [portfolio](../../Advanced%20Investments/An%20Asset%20Allocation%20Primer.md) of CDS contracts on multiple reference credits,  each paying the same index coupon (\(C_I(T)\)).
- Credit events result in the removal of affected credits from the index,  with loss payments made as they occur.

### 4.2 Valuation Formula

The value of a CDS index for a [protection seller](../../Financial%20Instruments/Financial%20Derivatives%20and%20Quantitative%20Methods/Credit%20Default%20Swaps.md) is:
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

- The price sensitivities of a CDS index are identical to those of a [single-name CDS](../../Financial%20Instruments/Lecture%20Notes-%20Financial%20Instruments/Lecture%20Notes%209A-%20Credit%20Default%20Swaps.md) with the same [term structure](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%209/The%20Vasicek%20Model.md) of spreads,  [recovery rate](../../Credit%20Markets/Credit%20Markets%20Session%203.md),  and maturity.
- The **CDS Index Basis** measures the difference between the index spread and the weighted average spread of its constituents. Deviations may arise due to market technical factors or restructuring clauses.

## 5. Summary and Key Takeaways

### 5.1 Interest Rate Sensitivity of a CDS

- The IR DV01 measures the sensitivity of a CDS to changes in [interest rates](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%202/Interest%20Rate%20Quotations.md) and is generally low compared to its spread sensitivity (Spread DV01).
- The IR DV01 is positive if \(C > S\),  negative if \(C < S\),  and zero if \(C = S\).

### 5.2 CDS Valuation

- The upfront value of a CDS depends on the quoted spread,  deal spread,  risky annuity,  and accrued coupon.
- Simplified approximations can provide valuations within 1.5% of Bloomberg-calculated results.

### 5.3 CDS Index Valuation

- A CDS index is valued as though it were a single CDS contract,  simplifying [risk management](../../Financial%20Engineering/Financial%20Mathematics%20Course.md) and [pricing](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%207/Arbitrage%20Pricing%20of%20Derivatives.md).
- The CDS Index Basis reflects deviations between the index spread and the weighted average spread of its constituents.

By understanding the mechanics,  valuation,  and [risk management](../../Financial%20Engineering/Financial%20Mathematics%20Course.md) of CDS and CDS indices,  financial professionals can effectively manage [credit risk](../../Course%20Notes/Quantitative%20Trading%20Strategies%20Lecture%20Notes.md) and optimize their portfolios.

# Lecture Notes: Credit Default Swaps (CDS) and Performance Attribution

## 1. Introduction to Credit Default Swaps (CDS)

- Credit Default Swaps (CDS) are [financial derivatives](../../Financial%20Instruments/Financial%20Instruments%20PSET%20Solutions.md) that allow the transfer of [credit risk](../../Course%20Notes/Quantitative%20Trading%20Strategies%20Lecture%20Notes.md) from one party to another. They are widely used for [hedging](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%205/Key%20Rates%20O1s%20Durations%20and%20Hedging.md),  speculation,  and structured credit investments.
- Since the [introduction](../../Financial%20Markets%20and%20Institutions/III.%20Liquidity%20of%20Assets/Class%209-%20Bailouts%20and%20Bank%20Failures/Squam%20Lake%20Group%20Introduction.md) of fixed coupons for CDS contracts in 2009,  entering into a CDS contract almost always involves an upfront cash payment,  which can be positive or negative depending on the relationship between the fixed coupon and the market-implied [credit spread](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%2014/Cds-Equivalent%20Bond%20Spread.md).

### 1.1 Key Features of CDS Contracts

- **[Protection Buyer](../../Financial%20Instruments/Financial%20Derivatives%20and%20Quantitative%20Methods/Credit%20Default%20Swaps.md)**: Pays a regular premium (fixed coupon) to the [protection seller](../../Financial%20Instruments/Financial%20Derivatives%20and%20Quantitative%20Methods/Credit%20Default%20Swaps.md) in exchange for protection against credit events.
- **[Protection Seller](../../Financial%20Instruments/Financial%20Derivatives%20and%20Quantitative%20Methods/Credit%20Default%20Swaps.md)**: Receives the premium and compensates the buyer if a [credit event](../../Financial%20Engineering/Valuation%20of%20Credit%20Default%20Swaps.md) occurs.
- **Upfront Payment**: The size and sign of the upfront payment depend on whether the fixed coupon sufficiently compensates the [protection seller](../../Financial%20Instruments/Financial%20Derivatives%20and%20Quantitative%20Methods/Credit%20Default%20Swaps.md) for the market-perceived risk of a [credit event](../../Financial%20Engineering/Valuation%20of%20Credit%20Default%20Swaps.md).
  - If the fixed coupon is low,  the [protection seller](../../Financial%20Instruments/Financial%20Derivatives%20and%20Quantitative%20Methods/Credit%20Default%20Swaps.md) may receive cash at trade initiation.
  - If the fixed coupon is high,  the [protection seller](../../Financial%20Instruments/Financial%20Derivatives%20and%20Quantitative%20Methods/Credit%20Default%20Swaps.md) may have to pay cash at trade initiation.
  - The situation is reversed for the [protection buyer](../../Financial%20Instruments/Financial%20Derivatives%20and%20Quantitative%20Methods/Credit%20Default%20Swaps.md).

### 1.2 Purpose of CDS Valuation

- The primary goal of CDS valuation is to calculate the upfront cash payment required to enter the contract.
- This requires a model that:
  - Accounts for the probability and timing of a [credit event](../../Financial%20Engineering/Valuation%20of%20Credit%20Default%20Swaps.md).
  - Values the premium leg,  considering the risk that not all coupons will be paid.
  - Values the protection leg,  which involves the unknown payment of par minus recovery at the time of a [credit event](../../Financial%20Engineering/Valuation%20of%20Credit%20Default%20Swaps.md).
  - Flexibly reprices the [term structure](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%209/The%20Vasicek%20Model.md) of quoted market spreads.

### 1.3 Market Quotes: Par Spread and Flat Quoted Spread

- **CDS Par Spread**:
  - The par spread is the coupon rate that results in a zero upfront value for the CDS contract on the trade date.
  - The value of a CDS is a function of the [term structure](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%209/The%20Vasicek%20Model.md) of CDS par spreads.
- **Flat Quoted Spread**:
  - Introduced in 2011,  the flat quoted spread assumes a flat [term structure](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%209/The%20Vasicek%20Model.md) of par spreads that reprices the market-quoted upfront value.
  - Only one quoted spread is needed to value a CDS contract,  simplifying the valuation process.

### 1.4 Forward-Looking Nature of CDS Spreads

- The probability of a CDS experiencing a [credit event](../../Financial%20Engineering/Valuation%20of%20Credit%20Default%20Swaps.md),  as implied by market spreads,  usually exceeds the historical default probability for credits with the same initial rating.
- This is because CDS spreads are forward-looking and embed a risk premium.

### 1.5 Sensitivity Analysis

- CDS valuation models allow holders to calculate the sensitivity of the contract's value to changes in the quoted spread.
- This enables [hedging](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%205/Key%20Rates%20O1s%20Durations%20and%20Hedging.md) with other CDS contracts or instruments.

### 1.6 CDS Indices

- For valuation purposes,  a CDS index can be treated as a [single-name CDS](../../Financial%20Instruments/Lecture%20Notes-%20Financial%20Instruments/Lecture%20Notes%209A-%20Credit%20Default%20Swaps.md) and valued using the same model.
- CDS indices provide diversified exposure to [credit markets](../../Credit%20Markets/Credit%20Markets%20Session%201.md) and are widely used for [hedging](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%205/Key%20Rates%20O1s%20Durations%20and%20Hedging.md) and speculative purposes.

## 2. Principles of Performance Attribution

- Performance attribution is a mathematical framework that splits the total outperformance of a [portfolio](../../Advanced%20Investments/An%20Asset%20Allocation%20Primer.md) versus a benchmark into contributions from individual decisions and actions.
- It helps quantify the contributions of decision-makers,  identify structural issues,  and clarify sources of [portfolio](../../Advanced%20Investments/An%20Asset%20Allocation%20Primer.md) risk and performance.

### 2.1 Key Requirements of Performance Attribution

1. **Additivity**: The contribution of two or more agents combined equals the sum of their individual contributions.
1. **Completeness**: The sum of all contributions equals the total [portfolio](../../Advanced%20Investments/An%20Asset%20Allocation%20Primer.md) outperformance.
1. **Fairness**: The allocation of outperformance to different agents is perceived as fair.

### 2.2 Multi-Period Attribution and Compounding

- Performance attribution over multiple periods must account for dynamic [portfolio management](../../Financial%20Engineering/Fixed%20Income%20Derivatives/The%20Impact%20of%20Option%20Strategies%20in%20Financial%20%20Portfolios%20Performance.md) and compounding effects.
- **Time-Weighted vs. Money-Weighted [Returns](../../Financial%20Markets/Financial%20Asset%20Pricing%20Theory%20Overview/Chapter%203%20-%20%20Assets,%20Portfolios,%20and%20Arbitrage/Assets.md)**:
  - Time-weighted [returns](../../Financial%20Markets/Financial%20Asset%20Pricing%20Theory%20Overview/Chapter%203%20-%20%20Assets,%20Portfolios,%20and%20Arbitrage/Assets.md) ignore [portfolio](../../Advanced%20Investments/An%20Asset%20Allocation%20Primer.md) size and are appropriate for managers without control over cash flows.
  - Money-weighted [returns](../../Financial%20Markets/Financial%20Asset%20Pricing%20Theory%20Overview/Chapter%203%20-%20%20Assets,%20Portfolios,%20and%20Arbitrage/Assets.md) account for cash flows and are suitable for managers responsible for timing cash flows.
- **Example**:
  - A [portfolio](../../Advanced%20Investments/An%20Asset%20Allocation%20Primer.md) with a seed [investment](../../Advanced%20Investments/An%20Asset%20Allocation%20Primer.md) of $1,   000,   000 doubles in value in the first half of the year but loses 10% in the second half after attracting $100,  000,  000 in new investments.
  - Time-weighted return: 80%.
  - Money-weighted return: -17.24%.

### 2.3 Attribution Frequency

- The frequency of the attribution system should match the frequency of [portfolio management](../../Financial%20Engineering/Fixed%20Income%20Derivatives/The%20Impact%20of%20Option%20Strategies%20in%20Financial%20%20Portfolios%20Performance.md) decisions.
- [Fixed income](../Lecture%20Notes%20Bonds,%20%20Preferred%20Stock,%20%20and%20Structured%20Products.md) portfolios often require daily-frequency attribution models due to their dynamic interest-rate exposures.

### 2.4 Flexibility of Attribution Models

- A practical attribution system must:
  - Measure [risk factors](../../Financial%20Instruments/Assignments/PSET%206-%20Financial%20Instruments.md) corresponding to [portfolio](../../Advanced%20Investments/An%20Asset%20Allocation%20Primer.md) manager decisions.
  - Independently measure contributions of each factor.
  - Align with published [returns](../../Financial%20Markets/Financial%20Asset%20Pricing%20Theory%20Overview/Chapter%203%20-%20%20Assets,%20Portfolios,%20and%20Arbitrage/Assets.md) of the fund and its benchmark.
  - Be timely and adaptable to short and long time periods.

## 3. Sector-Based Attribution

- Sector-based attribution decomposes [portfolio](../../Advanced%20Investments/An%20Asset%20Allocation%20Primer.md) outperformance into:
  1. **[Asset Allocation](Lecture%202-%20[[Lecture%202-%20Asset%20Allocation%20with%20Multiple%20Risky%20Assets) with [Multiple Risky Assets](../../Advanced%20Investments/Lecture%202-%20Asset%20Allocation%20with%20Multiple%20Risky%20Assets.md)|[asset allocation](../../Advanced%20Investments/Lecture%202-%20Asset%20Allocation%20with%20Multiple%20Risky%20Assets.md)]]**: Outperformance due to differences in sector weights between the [portfolio](../../Advanced%20Investments/An%20Asset%20Allocation%20Primer.md) and benchmark.
  1. **Security Selection**: Outperformance due to differences in [returns](../../Financial%20Markets/Financial%20Asset%20Pricing%20Theory%20Overview/Chapter%203%20-%20%20Assets,%20Portfolios,%20and%20Arbitrage/Assets.md) within each sector.
  1. **Interaction Effect**: Joint effect of [Asset Allocation](Lecture%202-%20[[Lecture%202-%20Asset%20Allocation%20with%20Multiple%20Risky%20Assets) with [Multiple Risky Assets](../../Advanced%20Investments/Lecture%202-%20Asset%20Allocation%20with%20Multiple%20Risky%20Assets.md)|[asset allocation](../../Advanced%20Investments/Lecture%202-%20Asset%20Allocation%20with%20Multiple%20Risky%20Assets.md)]] and security selection.

### 3.1 Mathematical Framework

- [Portfolio](../../Advanced%20Investments/An%20Asset%20Allocation%20Primer.md) return:
 $R^P = \sum_s w_s^P R_s^P$$
- Benchmark return:
 $R^B = \sum_s w_s^B R_s^B$$
- Total outperformance:
 $R^P - R^B = \text{Asset Allocation} + \text{Security Selection} + \text{Interaction}$$
- [Asset Allocation](Lecture%202-%20[[Lecture%202-%20Asset%20Allocation%20with%20Multiple%20Risky%20Assets) with [Multiple Risky Assets](../../Advanced%20Investments/Lecture%202-%20Asset%20Allocation%20with%20Multiple%20Risky%20Assets.md)|[asset allocation](../../Advanced%20Investments/Lecture%202-%20Asset%20Allocation%20with%20Multiple%20Risky%20Assets.md)]]:
 $\sum_s (w_s^P - w_s^B) \cdot R_s^B$$
- Security Selection:
 $\sum_s w_s^B \cdot (R_s^P - R_s^B)$$
- Interaction:
 $\sum_s (w_s^P - w_s^B) \cdot (R_s^P - R_s^B)$$

### 3.2 Recursive Allocation

- Large portfolios often involve multiple layers of management,  requiring recursive application of the attribution framework.
- Each sector can be treated as a smaller [portfolio](../../Advanced%20Investments/An%20Asset%20Allocation%20Primer.md),  with its performance further decomposed into [Asset Allocation](Lecture%202-%20[[Lecture%202-%20Asset%20Allocation%20with%20Multiple%20Risky%20Assets) with [Multiple Risky Assets](../../Advanced%20Investments/Lecture%202-%20Asset%20Allocation%20with%20Multiple%20Risky%20Assets.md)|[asset allocation](../../Advanced%20Investments/Lecture%202-%20Asset%20Allocation%20with%20Multiple%20Risky%20Assets.md)]] and security selection.

## 4. Factor-Based Attribution

- Factor-based attribution decomposes [portfolio](../../Advanced%20Investments/An%20Asset%20Allocation%20Primer.md) [returns](../../Financial%20Markets/Financial%20Asset%20Pricing%20Theory%20Overview/Chapter%203%20-%20%20Assets,%20Portfolios,%20and%20Arbitrage/Assets.md) into contributions from common [risk factors](../../Financial%20Instruments/Assignments/PSET%206-%20Financial%20Instruments.md) (e.g.,  [interest rates](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%202/Interest%20Rate%20Quotations.md),  spreads,  volatility) and a residual.
- **Mathematical Framework**:
 $R^P = \sum_k \alpha_k^P f_k^P + \varepsilon^P$$
 $R^P - R^B = \sum_k (\alpha_k^P - \alpha_k^B) \cdot f_k^P + (\varepsilon^P - \varepsilon^B)$$
- **Advantages**:
  - Explains systematic [returns](../../Financial%20Markets/Financial%20Asset%20Pricing%20Theory%20Overview/Chapter%203%20-%20%20Assets,%20Portfolios,%20and%20Arbitrage/Assets.md) using [risk factors](../../Financial%20Instruments/Assignments/PSET%206-%20Financial%20Instruments.md).
  - Residual [returns](../../Financial%20Markets/Financial%20Asset%20Pricing%20Theory%20Overview/Chapter%203%20-%20%20Assets,%20Portfolios,%20and%20Arbitrage/Assets.md) are idiosyncratic and small for well-diversified portfolios.
- **Disadvantages**:
  - Limited flexibility in defining [risk factors](../../Financial%20Instruments/Assignments/PSET%206-%20Financial%20Instruments.md).
  - Does not attribute idiosyncratic [returns](../../Financial%20Markets/Financial%20Asset%20Pricing%20Theory%20Overview/Chapter%203%20-%20%20Assets,%20Portfolios,%20and%20Arbitrage/Assets.md) to security selection.

## 5. Hybrid Performance Attribution

- The hybrid model combines sector-based and factor-based attribution,  offering flexibility to account for complex management structures.
- **Steps**:
  1. **Return Splitting**: Decompose total [returns](../../Financial%20Markets/Financial%20Asset%20Pricing%20Theory%20Overview/Chapter%203%20-%20%20Assets,%20Portfolios,%20and%20Arbitrage/Assets.md) into factor contributions.
  1. **Factor [Return Attribution](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%203/Pl%20Attribution.md)**: Attribute outperformance to individual factors.
  1. **Recursive Application**: Apply the framework recursively to different management layers.

## 6. Summary and Key Takeaways

### 6.1 Credit Default Swaps (CDS)

- CDS contracts involve upfront payments that depend on the relationship between the fixed coupon and market-implied credit spreads.
- Valuation models calculate the expected present value of the premium and protection legs,  accounting for [credit event](../../Financial%20Engineering/Valuation%20of%20Credit%20Default%20Swaps.md) probabilities and timing.

### 6.2 Performance Attribution

- Performance attribution splits [portfolio](../../Advanced%20Investments/An%20Asset%20Allocation%20Primer.md) outperformance into contributions from [Asset Allocation](Lecture%202-%20[[Lecture%202-%20Asset%20Allocation%20with%20Multiple%20Risky%20Assets) with [Multiple Risky Assets](../../Advanced%20Investments/Lecture%202-%20Asset%20Allocation%20with%20Multiple%20Risky%20Assets.md)|[asset allocation](../../Advanced%20Investments/Lecture%202-%20Asset%20Allocation%20with%20Multiple%20Risky%20Assets.md)]],  security selection,  and [risk factors](../../Financial%20Instruments/Assignments/PSET%206-%20Financial%20Instruments.md).
- Sector-based and factor-based attribution frameworks can be combined into a hybrid model to address the complexity of modern [portfolio management](../../Financial%20Engineering/Fixed%20Income%20Derivatives/The%20Impact%20of%20Option%20Strategies%20in%20Financial%20%20Portfolios%20Performance.md).

By mastering CDS valuation and performance attribution principles,  financial professionals can effectively manage [credit risk](../../Course%20Notes/Quantitative%20Trading%20Strategies%20Lecture%20Notes.md) and optimize [portfolio](../../Advanced%20Investments/An%20Asset%20Allocation%20Primer.md) performance.

# Lecture Notes: Advanced Performance Attribution in Fixed Income Portfolio Management

## 1. Introduction to Performance Attribution

- Performance attribution is a systematic framework used to decompose [portfolio](../../Advanced%20Investments/An%20Asset%20Allocation%20Primer.md) outperformance into contributions from various factors,  decisions,  and exposures.
- It provides insights into the sources of [risk and return](../../Advanced%20Investments/Lecture%207-Risk%20and%20Return%20of%20Bonds.md),  linking ex-post performance to ex-ante management decisions.
- This lecture focuses on:
  - Factor [return attribution](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%203/Pl%20Attribution.md).
  - Recursive decomposition of outperformance.
  - Applications of performance attribution as a [portfolio management](../../Financial%20Engineering/Fixed%20Income%20Derivatives/The%20Impact%20of%20Option%20Strategies%20in%20Financial%20%20Portfolios%20Performance.md) tool.
  - A detailed example of hybrid performance attribution using a fixed-income [portfolio](../../Advanced%20Investments/An%20Asset%20Allocation%20Primer.md).

## 2. Factor Return Attribution

### 2.1 Common and Allocated Factors

- Factors are categorized into **common factors** and **allocated factors**:
  - **Common Factors**: Shared across the [portfolio](../../Advanced%20Investments/An%20Asset%20Allocation%20Primer.md) and benchmark,  such as yield curve exposure or [duration](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%205/Key%20Rates%20O1s%20Durations%20and%20Hedging.md).
  - **Allocated Factors**: Specific to individual securities or sectors,  such as credit spreads or security selection.
- The total [portfolio](../../Advanced%20Investments/An%20Asset%20Allocation%20Primer.md) outperformance is expressed as:
$$
R^{P} - R^{B} = \left(\sum_{k \in C} \alpha_{k}^{P} f_{k}^{P} - \sum_{k \in C} \alpha_{k}^{B} f_{k}^{B}\right) + \left(\sum_{k \in A} \alpha_{k}^{P} f_{k}^{P} - \sum_{k \in A} \alpha_{k}^{B} f_{k}^{B}\right)
$$

Where:

- \(R^{P}\): [Portfolio](../../Advanced%20Investments/An%20Asset%20Allocation%20Primer.md) return.
- \(R^{B}\): Benchmark return.
- \(\alpha_{k}^{P}\): [Portfolio](../../Advanced%20Investments/An%20Asset%20Allocation%20Primer.md) exposure to factor \(k\).
- \(\alpha_{k}^{B}\): Benchmark exposure to factor \(k\).
- \(f_{k}^{P}\): [Portfolio](../../Advanced%20Investments/An%20Asset%20Allocation%20Primer.md) factor return.
- \(f_{k}^{B}\): Benchmark factor return.

### 2.2 Decomposition of Factor Outperformance

- For each factor,  the outperformance is decomposed across sectors:
$$
\alpha_{k}^{P} f_{k}^{P} - \alpha_{k}^{B} f_{k}^{B} = \sum_{s} \alpha_{k,   s}^{P} f_{k,   s}^{P} - \sum_{s} \alpha_{k,   s}^{B} f_{k,   s}^{B}
$$

- **Common Factors**:
  - If the factor return is identical for the [portfolio](../../Advanced%20Investments/An%20Asset%20Allocation%20Primer.md) and benchmark (\(f_{k,  s}^{P} = f_{k,  s}^{B}\)),  the contribution simplifies to:
	$$\sum_{s} \left(\alpha_{k,   s}^{P} - \alpha_{k,   s}^{B}\right) \cdot f_{k,   s}$$
  - Example: Yield curve exposure managed at the [portfolio](../../Advanced%20Investments/An%20Asset%20Allocation%20Primer.md) level.
- **Allocated Factors**:
  - Allocated factors may have different realizations for different securities or sectors.
  - Example: Credit spreads,  which vary across securities within a sector.

### 2.3 Allocation Methods

#### Absolute Allocation
- Total [portfolio](../../Advanced%20Investments/An%20Asset%20Allocation%20Primer.md) exposure to a factor is determined by the net sector exposures.
- Decomposition:
  - **[Asset Allocation](Lecture%202-%20[[Lecture%202-%20Asset%20Allocation%20with%20Multiple%20Risky%20Assets) with [Multiple Risky Assets](../../Advanced%20Investments/Lecture%202-%20Asset%20Allocation%20with%20Multiple%20Risky%20Assets.md)|[asset allocation](../../Advanced%20Investments/Lecture%202-%20Asset%20Allocation%20with%20Multiple%20Risky%20Assets.md)]]**:
	$$\sum_{s} \left(\alpha_{k,   s}^{P} - \alpha_{k,   s}^{B}\right) \cdot f_{k,   s}^{B}$$
  - **Sector Management**:
	$$\sum_{s} \alpha_{k,   s}^{P} \cdot \left(f_{k,   s}^{P} - f_{k,   s}^{B}\right)$$

#### Relative Allocation
- Total [portfolio](../../Advanced%20Investments/An%20Asset%20Allocation%20Primer.md) exposure to a factor is determined at the [portfolio](../../Advanced%20Investments/An%20Asset%20Allocation%20Primer.md) level,  with sector exposures constrained by the [portfolio](../../Advanced%20Investments/An%20Asset%20Allocation%20Primer.md) exposure.
- Decomposition:
  - **[Asset Allocation](Lecture%202-%20[[Lecture%202-%20Asset%20Allocation%20with%20Multiple%20Risky%20Assets) with [Multiple Risky Assets](../../Advanced%20Investments/Lecture%202-%20Asset%20Allocation%20with%20Multiple%20Risky%20Assets.md)|[asset allocation](../../Advanced%20Investments/Lecture%202-%20Asset%20Allocation%20with%20Multiple%20Risky%20Assets.md)]]**:
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
  - Top-level [duration](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%205/Key%20Rates%20O1s%20Durations%20and%20Hedging.md) exposure is decomposed into sector-level [duration](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%205/Key%20Rates%20O1s%20Durations%20and%20Hedging.md) exposures.
  - Sector-level exposures are further decomposed into individual security contributions.

## 4. Example: Hybrid Performance Attribution

### 4.1 Portfolio Overview

- **Mandate**: Track the Barclays Capital Global Aggregate G4 Index with a tracking error volatility (TEV) limit of 40 bps per month.
- **Manager Views**:
  - Bullish on the Japanese yen.
  - Bearish on the euro.
  - Neutral on the U.S. dollar and British pound.
  - Positive on U.S. corporates,  negative on U.S. securitized sector.
- **[Portfolio](../../Advanced%20Investments/An%20Asset%20Allocation%20Primer.md) Characteristics**:
  - 5% overweight in yen,  5% underweight in euro.
  - 5% overweight in U.S. corporates,  5% underweight in U.S. securitized.
  - [Portfolio](../../Advanced%20Investments/An%20Asset%20Allocation%20Primer.md) [duration](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%205/Key%20Rates%20O1s%20Durations%20and%20Hedging.md) is 1 year longer than the benchmark.

### 4.2 Performance Attribution Results

#### Total Outperformance
- [Portfolio](../../Advanced%20Investments/An%20Asset%20Allocation%20Primer.md) return: +188.7 bps.
- Benchmark return: +150.0 bps.
- Total outperformance: +38.7 bps.

#### Global Outperformance Summary (Exhibit 70-2)
- **FX Allocation and [Hedging](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%205/Key%20Rates%20O1s%20Durations%20and%20Hedging.md)**: +28.3 bps.
- **Local Market Allocation**: -8.7 bps.
- **Local Market Management**: +19.1 bps.

#### Local Market Management Details (Exhibit 70-3)
- **Yield-Curve Exposures**: +20.6 bps.
- **[Asset Allocation](../../Advanced%20Investments/Lecture%202-%20Asset%20Allocation%20with%20Multiple%20Risky%20Assets.md)**: +0.2 bps.
- **Security Selection**: -1.7 bps.

### 4.3 FX Outperformance Breakdown (Exhibit 70-4)

- **Yen**:
  - Rally vs. USD: +319.4 bps.
  - [Portfolio](../../Advanced%20Investments/An%20Asset%20Allocation%20Primer.md) overweight: +5%.
  - Contribution: \(5\% \times 319.4 = +16.0\) bps.
- **Euro**:
  - Decline vs. USD: -244.1 bps.
  - [Portfolio](../../Advanced%20Investments/An%20Asset%20Allocation%20Primer.md) underweight: -5%.
  - Contribution: \(-5\% \times -244.1 = +12.0\) bps.
- **British Pound**:
  - Decline vs. USD: -183.5 bps.
  - [Portfolio](../../Advanced%20Investments/An%20Asset%20Allocation%20Primer.md) exposure: 0%.
  - Contribution: 0 bps.
- **Total FX Contribution**: +28.3 bps.

### 4.4 Local Market Allocation (Exhibit 70-5)

- **Yen Local Market**:
  - [Portfolio](../../Advanced%20Investments/An%20Asset%20Allocation%20Primer.md) overweight: +5%.
  - Underperformance: \( (64.2 - 164.1) \times 5\% = -5.0 \) bps.
- **Euro Local Market**:
  - [Portfolio](../../Advanced%20Investments/An%20Asset%20Allocation%20Primer.md) underweight: -5%.
  - Underperformance: \( (239.2 - 164.1) \times -5\% = -3.8 \) bps.
- **Total Local Market Allocation Contribution**: -8.7 bps.

## 5. Applications of Performance Attribution

### 5.1 Linking Ex-Post and Ex-Ante Decisions

- Performance attribution links realized outperformance to the manager's initial views and decisions.
- Example:
  - The manager's bullish yen view contributed +16.1 bps,  validating the decision.
  - The underweight in the euro local market resulted in -3.1 bps,  highlighting an area for improvement.

### 5.2 Identifying Unanticipated Risks

- Attribution exposes unanticipated sources of [risk and return](../../Advanced%20Investments/Lecture%207-Risk%20and%20Return%20of%20Bonds.md).
- Example:
  - The yen local market underperformance (-5.0 bps) was incidental to the FX overweight and could be addressed in future allocations.

### 5.3 Data Validation

- Recursive decomposition facilitates the discovery of data errors in large financial systems.
- Example:
  - Discrepancies in sector weights or [returns](../../Financial%20Markets/Financial%20Asset%20Pricing%20Theory%20Overview/Chapter%203%20-%20%20Assets,%20Portfolios,%20and%20Arbitrage/Assets.md) can be traced back to individual securities.

## 6. Summary and Key Takeaways

### 6.1 Factor Return Attribution

- Common factors (e.g.,  yield curve) are managed at the [portfolio](../../Advanced%20Investments/An%20Asset%20Allocation%20Primer.md) level,  while allocated factors (e.g.,  credit spreads) vary across sectors and securities.
- Absolute and relative allocation frameworks provide flexibility in decomposing outperformance.

### 6.2 Hybrid Attribution

- Hybrid models combine sector-based and factor-based attribution,  enabling detailed analysis of [portfolio](../../Advanced%20Investments/An%20Asset%20Allocation%20Primer.md) performance.
- Recursive decomposition links top-level decisions to individual security contributions.

### 6.3 Portfolio Management Applications

- Performance attribution enhances [portfolio management](../../Financial%20Engineering/Fixed%20Income%20Derivatives/The%20Impact%20of%20Option%20Strategies%20in%20Financial%20%20Portfolios%20Performance.md) by:
  - Validating ex-ante views.
  - Identifying unanticipated risks.
  - Improving decision-making processes.

By mastering advanced performance attribution techniques,  [portfolio](../../Advanced%20Investments/An%20Asset%20Allocation%20Primer.md) managers can systematically evaluate their strategies,  optimize risk-adjusted [returns](../../Financial%20Markets/Financial%20Asset%20Pricing%20Theory%20Overview/Chapter%203%20-%20%20Assets,%20Portfolios,%20and%20Arbitrage/Assets.md),  and enhance their decision-making frameworks.

### Lecture Notes: Performance Attribution in Fixed Income Portfolio Management – Local Market and Yield-Curve Analysis

## 1. Introduction to Local Market and Yield-Curve Attribution

- Performance attribution in [fixed income](../Lecture%20Notes%20Bonds,%20%20Preferred%20Stock,%20%20and%20Structured%20Products.md) [portfolio management](../../Financial%20Engineering/Fixed%20Income%20Derivatives/The%20Impact%20of%20Option%20Strategies%20in%20Financial%20%20Portfolios%20Performance.md) involves analyzing the sources of [portfolio](../../Advanced%20Investments/An%20Asset%20Allocation%20Primer.md) outperformance relative to a benchmark.
- This lecture focuses on:
  - Local market management and its contribution to [portfolio](../../Advanced%20Investments/An%20Asset%20Allocation%20Primer.md) outperformance.
  - Yield-curve exposure and its impact on performance across different currencies.
  - Detailed breakdowns of yield-curve outperformance for the U.S. dollar,  euro,  Japanese yen,  and British pound markets.

## 2. Local Market Management and Outperformance

### 2.1 Breakdown of Local Market Contributions (Exhibit 70-6)

| **Metric** | **U.S. Dollar** | **Euro** | **Japanese Yen** | **British Pound** | **Total** |

| **[Portfolio](../../Advanced%20Investments/An%20Asset%20Allocation%20Primer.md) Weight (%)** | 45.5 | 23.2 | 25.6 | 5.8 | 100.0 |

| **Local Management (bp)**| 14.6 | 6.3 | 2.4 | -4.2 | 19.1 |

| **Yield-Curve (bp)** | 11.2 | 17.9 | 3.0 | -11.5 | 20.6 |

| **[Asset Allocation](../../Advanced%20Investments/Lecture%202-%20Asset%20Allocation%20with%20Multiple%20Risky%20Assets.md) (bp)**| -2.5 | 1.5 | -0.1 | 1.3 | 0.2 |

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

1. **[Asset Allocation](Lecture%202-%20[[Lecture%202-%20Asset%20Allocation%20with%20Multiple%20Risky%20Assets) with [Multiple Risky Assets](../../Advanced%20Investments/Lecture%202-%20Asset%20Allocation%20with%20Multiple%20Risky%20Assets.md)|[asset allocation](../../Advanced%20Investments/Lecture%202-%20Asset%20Allocation%20with%20Multiple%20Risky%20Assets.md)]]**:
   - [Asset Allocation](Lecture%202-%20[[Lecture%202-%20Asset%20Allocation%20with%20Multiple%20Risky%20Assets) with [Multiple Risky Assets](../../Advanced%20Investments/Lecture%202-%20Asset%20Allocation%20with%20Multiple%20Risky%20Assets.md)|[asset allocation](../../Advanced%20Investments/Lecture%202-%20Asset%20Allocation%20with%20Multiple%20Risky%20Assets.md)]] had a negligible impact,  contributing only **+0.2 bp**.

## 3. Yield-Curve Outperformance Analysis

### 3.1 U.S. Dollar Yield-Curve Breakdown (Exhibit 70-7)

| **Metric** | **[Portfolio](../../Advanced%20Investments/An%20Asset%20Allocation%20Primer.md)** | **Benchmark** | **Difference** | **Outperformance (bp)** |

| **Average Yield (%)** | 1.311 | 1.245 | -31.6 bp | |

| **Average [Duration](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%205/Key%20Rates%20O1s%20Durations%20and%20Hedging.md) (yrs)**| 4.66 | 4.18 | +0.48 yrs | |

| **Parallel Shift (bp)** | | | | +14.6 |

| **Curve Reshaping (bp)** | | | | +10.3 |

| **Total Yield-Curve (bp)**| | | | +24.6 |

#### Key Insights
1. **Parallel Shift**:
   - The [portfolio](../../Advanced%20Investments/An%20Asset%20Allocation%20Primer.md)'s [duration](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%205/Key%20Rates%20O1s%20Durations%20and%20Hedging.md) overweight of **+0.48 years** contributed **+14.6 bp** of outperformance due to falling yields (bull-flattening of the U.S. Treasury curve).

1. **Curve Reshaping**:
   - A butterfly position,  with an overweight at the 20-year point and underweights at the 5-,  10-,  and 30-year points,  contributed an additional **+10.3 bp**.
   - The 20-year point experienced the largest yield drop (**-48.7 bp**),  driving most of the reshaping outperformance.

1. **Total Contribution**:
   - The total yield-curve outperformance for the U.S. dollar market was **+24.6 bp**.

### 3.2 Euro Yield-Curve Breakdown (Exhibit 70-8)

| **Metric** | **[Portfolio](../../Advanced%20Investments/An%20Asset%20Allocation%20Primer.md)** | **Benchmark** | **Difference** | **Outperformance (bp)** |

| **Average Yield (%)** | 2.030 | 1.698 | -50.2 bp | |

| **Average [Duration](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%205/Key%20Rates%20O1s%20Durations%20and%20Hedging.md) (yrs)**| 6.68 | 5.62 | +1.05 yrs | |

| **Parallel Shift (bp)** | | | | +54.2 |

| **Curve Reshaping (bp)** | | | | +23.2 |

| **Total Yield-Curve (bp)**| | | | +77.4 |

#### Key Insights
1. **Parallel Shift**:
   - The [portfolio](../../Advanced%20Investments/An%20Asset%20Allocation%20Primer.md)'s [duration](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%205/Key%20Rates%20O1s%20Durations%20and%20Hedging.md) overweight of **+1.05 years** contributed **+54.2 bp** of outperformance due to falling yields (bull-flattening of the euro curve).

1. **Curve Reshaping**:
   - A butterfly position,  with an overweight at the 10-year point and underweights at the 5and 30-year points,  contributed an additional **+23.2 bp**.

1. **Total Contribution**:
   - The total yield-curve outperformance for the euro market was **+77.4 bp**,  translating to **+17.9 bp** when scaled by the [portfolio](../../Advanced%20Investments/An%20Asset%20Allocation%20Primer.md) weight of **23.2%**.

### 3.3 Japanese Yen Yield-Curve Breakdown (Exhibit 70-8)

| **Metric** | **[Portfolio](../../Advanced%20Investments/An%20Asset%20Allocation%20Primer.md)** | **Benchmark** | **Difference** | **Outperformance (bp)** |

| **Average Yield (%)** | 0.534 | 0.534 | -7.0 bp | |

| **Average [Duration](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%205/Key%20Rates%20O1s%20Durations%20and%20Hedging.md) (yrs)**| 7.12 | 4.42 | +2.70 yrs | |

| **Parallel Shift (bp)** | | | | +3.0 |

| **Curve Reshaping (bp)** | | | | +0.0 |

| **Total Yield-Curve (bp)**| | | | +3.0 |

#### Key Insights
1. **Parallel Shift**:
   - The [portfolio](../../Advanced%20Investments/An%20Asset%20Allocation%20Primer.md)'s [duration](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%205/Key%20Rates%20O1s%20Durations%20and%20Hedging.md) overweight of **+2.70 years** contributed **+3.0 bp** of outperformance due to modest yield declines.

1. **Curve Reshaping**:
   - Curve reshaping had no significant impact on performance.

1. **Total Contribution**:
   - The total yield-curve outperformance for the yen market was **+3.0 bp**,  translating to **+0.8 bp** when scaled by the [portfolio](../../Advanced%20Investments/An%20Asset%20Allocation%20Primer.md) weight of **25.6%**.

### 3.4 British Pound Yield-Curve Breakdown (Exhibit 70-8)

| **Metric** | **[Portfolio](../../Advanced%20Investments/An%20Asset%20Allocation%20Primer.md)** | **Benchmark** | **Difference** | **Outperformance (bp)** |

| **Average Yield (%)** | 3.195 | 3.195 | -48.7 bp | |

| **Average [Duration](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%205/Key%20Rates%20O1s%20Durations%20and%20Hedging.md) (yrs)**| 4.66 | 4.18 | +0.48 yrs | |

| **Parallel Shift (bp)** | | | | -11.5 |

| **Curve Reshaping (bp)** | | | | +0.0 |

| **Total Yield-Curve (bp)**| | | | -11.5 |

#### Key Insights
1. **Parallel Shift**:
   - The [portfolio](../../Advanced%20Investments/An%20Asset%20Allocation%20Primer.md)'s [duration](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%205/Key%20Rates%20O1s%20Durations%20and%20Hedging.md) overweight contributed **-11.5 bp** of underperformance due to unfavorable yield movements.

1. **Curve Reshaping**:
   - Curve reshaping had no significant impact on performance.

1. **Total Contribution**:
   - The total yield-curve outperformance for the British pound market was **-11.5 bp**,  translating to **-0.7 bp** when scaled by the [portfolio](../../Advanced%20Investments/An%20Asset%20Allocation%20Primer.md) weight of **5.8%**.

## 4. Managerial Implications

### 4.1 Key Takeaways from Yield-Curve Analysis

1. **U.S. Dollar and Euro Markets**:
   - The [portfolio](../../Advanced%20Investments/An%20Asset%20Allocation%20Primer.md)'s [duration](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%205/Key%20Rates%20O1s%20Durations%20and%20Hedging.md) overweights and curve reshaping positions were well-aligned with market movements,  resulting in significant outperformance.

1. **Japanese Yen Market**:
   - The [portfolio](../../Advanced%20Investments/An%20Asset%20Allocation%20Primer.md)'s [duration](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%205/Key%20Rates%20O1s%20Durations%20and%20Hedging.md) overweight contributed modestly to outperformance,  but the lack of significant curve reshaping limited the total contribution.

1. **British Pound Market**:
   - The [portfolio](../../Advanced%20Investments/An%20Asset%20Allocation%20Primer.md)'s [duration](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%205/Key%20Rates%20O1s%20Durations%20and%20Hedging.md) overweight detracted from performance due to unfavorable yield movements.

### 4.2 Recommendations for Future Management

1. **Control Curve Reshaping**:
   - The manager should carefully monitor and control exposure to specific curve points to avoid inadvertent positions.

1. **Diversify Contributions**:
   - Relying heavily on a single market (e.g.,  U.S. dollar) for outperformance increases risk. Diversifying contributions across markets can improve risk-adjusted [returns](../../Financial%20Markets/Financial%20Asset%20Pricing%20Theory%20Overview/Chapter%203%20-%20%20Assets,%20Portfolios,%20and%20Arbitrage/Assets.md).

1. **Refine [Duration](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%205/Key%20Rates%20O1s%20Durations%20and%20Hedging.md) Overweights**:
   - While [duration](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%205/Key%20Rates%20O1s%20Durations%20and%20Hedging.md) overweights contributed positively in most markets,  the British pound market highlights the need for more precise implementation.

## 5. Summary and Key Takeaways

- Local market management contributed **+19.1 bp** to total [portfolio](../../Advanced%20Investments/An%20Asset%20Allocation%20Primer.md) outperformance,  driven by the U.S. dollar and euro markets.
- Yield-curve exposure was the dominant driver of outperformance,  contributing **+20.6 bp**,  with significant contributions from the U.S. dollar and euro markets.
- The manager should focus on controlling curve reshaping positions and diversifying contributions across markets to enhance future performance.

By understanding the sources of outperformance and refining [portfolio management](../../Financial%20Engineering/Fixed%20Income%20Derivatives/The%20Impact%20of%20Option%20Strategies%20in%20Financial%20%20Portfolios%20Performance.md) strategies,  [fixed income](../Lecture%20Notes%20Bonds,%20%20Preferred%20Stock,%20%20and%20Structured%20Products.md) managers can optimize risk-adjusted [returns](../../Financial%20Markets/Financial%20Asset%20Pricing%20Theory%20Overview/Chapter%203%20-%20%20Assets,%20Portfolios,%20and%20Arbitrage/Assets.md) and achieve their [investment](../../Advanced%20Investments/An%20Asset%20Allocation%20Primer.md) objectives.

### Lecture Notes: Yield-Curve Outperformance Breakdown for Euro,  Japanese Yen,  and British Pound

## 1. Introduction to Yield-Curve Outperformance Analysis

- Yield-curve outperformance analysis is a critical component of fixed-income [portfolio management](../../Financial%20Engineering/Fixed%20Income%20Derivatives/The%20Impact%20of%20Option%20Strategies%20in%20Financial%20%20Portfolios%20Performance.md),  as it quantifies the impact of [portfolio](../../Advanced%20Investments/An%20Asset%20Allocation%20Primer.md) positioning relative to benchmark yield-curve movements.
- This lecture focuses on:
  - Detailed yield-curve outperformance for the **Euro**,  **Japanese Yen**,  and **British Pound** markets.
  - The importance of managing yield-curve exposures across currencies.
  - Implications for [portfolio management](../../Financial%20Engineering/Fixed%20Income%20Derivatives/The%20Impact%20of%20Option%20Strategies%20in%20Financial%20%20Portfolios%20Performance.md) and attribution methodologies.

## 2. Yield-Curve Outperformance Breakdown

### 2.1 Japanese Yen (JPY) Yield-Curve Analysis

#### Key Metrics
- **[Portfolio](../../Advanced%20Investments/An%20Asset%20Allocation%20Primer.md) [Duration](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%205/Key%20Rates%20O1s%20Durations%20and%20Hedging.md) Overweight**: +2.69 years.
- **Yield-Curve Movement**: Modest bull-flattening,  with a parallel shift of -7.0 bp.
- **Unscaled Outperformance**: +11.8 bp.
- **Scaled Contribution**: +3.0 bp ([portfolio](../../Advanced%20Investments/An%20Asset%20Allocation%20Primer.md) weight: 25.6%).

#### Observations
1. **[Duration](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%205/Key%20Rates%20O1s%20Durations%20and%20Hedging.md) Overweight**:
   - The [portfolio](../../Advanced%20Investments/An%20Asset%20Allocation%20Primer.md)'s significant [duration](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%205/Key%20Rates%20O1s%20Durations%20and%20Hedging.md) overweight of +2.69 years was well-positioned to benefit from the modest bull-flattening of the yen yield curve.
   - However,  the magnitude of the yield-curve movement was insufficient to generate substantial outperformance.

1. **[Key Rate](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%205/Key%20Rates%20O1s%20Durations%20and%20Hedging.md) Contributions**:
   - The 20-year point contributed positively (+3.9 bp unscaled) due to its overweight and a yield drop of -8.1 bp.
   - The 5-year and 7-year points detracted (-4.0 bp and -5.1 bp unscaled,  respectively) due to underperformance relative to their weights.

1. **Implications**:
   - The yen market's contribution to total [portfolio](../../Advanced%20Investments/An%20Asset%20Allocation%20Primer.md) outperformance was modest,  highlighting the need for more pronounced yield-curve movements to capitalize on [duration](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%205/Key%20Rates%20O1s%20Durations%20and%20Hedging.md) overweights.

### 2.2 British Pound (GBP) Yield-Curve Analysis

#### Key Metrics
- **[Portfolio](../../Advanced%20Investments/An%20Asset%20Allocation%20Primer.md) [Duration](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%205/Key%20Rates%20O1s%20Durations%20and%20Hedging.md) Underweight**: -3.81 years.
- **Yield-Curve Movement**: Strong bull-flattening,  with a parallel shift of -44.9 bp.
- **Unscaled Underperformance**: -199.2 bp.
- **Scaled Contribution**: -11.5 bp ([portfolio](../../Advanced%20Investments/An%20Asset%20Allocation%20Primer.md) weight: 5.8%).

#### Observations
1. **[Duration](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%205/Key%20Rates%20O1s%20Durations%20and%20Hedging.md) Underweight**:
   - The [portfolio](../../Advanced%20Investments/An%20Asset%20Allocation%20Primer.md)'s significant [duration](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%205/Key%20Rates%20O1s%20Durations%20and%20Hedging.md) underweight of -3.81 years was poorly positioned for the strong bull-flattening of the British pound yield curve.
   - The long end of the curve (20-year and 30-year points) experienced substantial yield drops (-49.5 bp and -44.9 bp,  respectively),  exacerbating the underperformance.

1. **[Key Rate](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%205/Key%20Rates%20O1s%20Durations%20and%20Hedging.md) Contributions**:
   - The 10-year point contributed positively (+2.7 bp unscaled) due to its overweight and a yield drop of -46.7 bp.
   - The 20-year and 30-year points detracted significantly (-11.2 bp and -0.5 bp unscaled,  respectively) due to their underweights and large yield drops.

1. **Implications**:
   - The British pound market's underperformance highlights the risks of significant [duration](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%205/Key%20Rates%20O1s%20Durations%20and%20Hedging.md) underweights in markets experiencing strong yield-curve movements.
   - Despite the small [portfolio](../../Advanced%20Investments/An%20Asset%20Allocation%20Primer.md) weight (5.8%),  the GBP market's contribution to total [portfolio](../../Advanced%20Investments/An%20Asset%20Allocation%20Primer.md) underperformance was substantial.

### 2.3 Euro (EUR) Yield-Curve Analysis

#### Key Metrics
- **[Portfolio](../../Advanced%20Investments/An%20Asset%20Allocation%20Primer.md) [Duration](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%205/Key%20Rates%20O1s%20Durations%20and%20Hedging.md) Overweight**: +1.05 years.
- **Yield-Curve Movement**: Bull-flattening,  with a parallel shift of -50.2 bp.
- **Unscaled Outperformance**: +77.4 bp.
- **Scaled Contribution**: +17.9 bp ([portfolio](../../Advanced%20Investments/An%20Asset%20Allocation%20Primer.md) weight: 23.2%).

#### Observations
1. **[Duration](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%205/Key%20Rates%20O1s%20Durations%20and%20Hedging.md) Overweight**:
   - The [portfolio](../../Advanced%20Investments/An%20Asset%20Allocation%20Primer.md)'s [duration](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%205/Key%20Rates%20O1s%20Durations%20and%20Hedging.md) overweight of +1.05 years was well-positioned to benefit from the significant bull-flattening of the euro yield curve.
   - The 10-year point experienced the largest yield drop (-46.7 bp),  driving much of the outperformance.

1. **[Key Rate](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%205/Key%20Rates%20O1s%20Durations%20and%20Hedging.md) Contributions**:
   - The 10-year point contributed positively (+2.7 bp unscaled) due to its overweight and a yield drop of -46.7 bp.
   - The 5-year point contributed modestly (+1.2 bp unscaled),  while the 20-year point detracted slightly (-11.2 bp unscaled).

1. **Implications**:
   - The euro market's contribution to total [portfolio](../../Advanced%20Investments/An%20Asset%20Allocation%20Primer.md) outperformance was significant,  demonstrating the benefits of well-aligned [duration](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%205/Key%20Rates%20O1s%20Durations%20and%20Hedging.md) overweights in markets with pronounced yield-curve movements.

## 3. Implications for Portfolio Management

### 3.1 Importance of Yield-Curve Management

- The analysis underscores the critical role of yield-curve management in fixed-income [portfolio](../../Advanced%20Investments/An%20Asset%20Allocation%20Primer.md) performance.
- **Key Takeaways**:
  - [Duration](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%205/Key%20Rates%20O1s%20Durations%20and%20Hedging.md) overweights and underweights must be carefully aligned with expected yield-curve movements.
  - Significant underweights in markets with strong yield-curve movements (e.g.,  GBP) can lead to substantial underperformance,  even with small [portfolio](../../Advanced%20Investments/An%20Asset%20Allocation%20Primer.md) weights.

### 3.2 Global vs. Local Curve Management

- The [portfolio](../../Advanced%20Investments/An%20Asset%20Allocation%20Primer.md) manager may decide to prioritize **global yield-curve management** over local market allocation and management decisions.
- **Rationale**:
  - Yield-curve movements often dominate other sources of outperformance or underperformance.
  - A global approach ensures consistent alignment of [duration](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%205/Key%20Rates%20O1s%20Durations%20and%20Hedging.md) exposures across currencies.

### 3.3 Attribution Methodology Adjustments

- If global yield-curve management is prioritized,  the attribution methodology should exclude yield-curve outperformance from the **Local Market Allocation** and **Local Management** components.
- **Alternative Attribution Framework**:
  - Yield-curve outperformance is attributed to a separate **Global Curve Management** component.
  - Local market allocation and management focus solely on sector and security selection.

## 4. [asset allocation](../../Advanced%20Investments/Lecture%202-%20Asset%20Allocation%20with%20Multiple%20Risky%20Assets.md) and Security Selection

### 4.1 U.S. Dollar [asset allocation](../../Advanced%20Investments/Lecture%202-%20Asset%20Allocation%20with%20Multiple%20Risky%20Assets.md) (Exhibit 70-9)

#### Key Metrics
- **[Portfolio](../../Advanced%20Investments/An%20Asset%20Allocation%20Primer.md) Weight**: 45.5%.
- **Corporate Bond Overweight**: +5.0%.
- **Unscaled Underperformance**: -5.5 bp.
- **Scaled Contribution**: -2.5 bp.

#### Observations
1. **[Corporate Bonds](../../Financial%20Markets%20and%20Institutions/II.%20The%20Roles%20of%20Banks%20and%20Derivative%20Markets%20in%20Resolving%20Problems%20Inherent%20in%20Debt%20Contracts/Class%202-%20Debt%20Contracts%20due%20to%20Lack%20of%20Information/Class%20Notes%202%20–%20Corporate%20Bond%20Contracts.md)**:
   - The [portfolio](../../Advanced%20Investments/An%20Asset%20Allocation%20Primer.md)'s overweight to U.S. [Corporate Bonds](../../Financial%20Markets%20and%20Institutions/II.%20The%20Roles%20of%20Banks%20and%20Derivative%20Markets%20in%20Resolving%20Problems%20Inherent%20in%20Debt%20Contracts/Class%202-%20Debt%20Contracts%20due%20to%20Lack%20of%20Information/Class%20Notes%202%20–%20Corporate%20Bond%20Contracts.md) contributed -5.2 bp to unscaled underperformance.
   - This was driven by the significant underperformance of the corporate sector in the benchmark (-70.2 bp) relative to the benchmark itself (-22.0 bp).

1. **Treasury and Government-Related Sectors**:
   - These sectors had no contribution to [Asset Allocation](Lecture%202-%20[[Lecture%202-%20Asset%20Allocation%20with%20Multiple%20Risky%20Assets) with [Multiple Risky Assets](../../Advanced%20Investments/Lecture%202-%20Asset%20Allocation%20with%20Multiple%20Risky%20Assets.md)|[asset allocation](../../Advanced%20Investments/Lecture%202-%20Asset%20Allocation%20with%20Multiple%20Risky%20Assets.md)]],  as their weights were matched exactly between the [portfolio](../../Advanced%20Investments/An%20Asset%20Allocation%20Primer.md) and benchmark.

1. **Securitized Sector**:
   - The securitized sector had minimal contribution to [Asset Allocation](Lecture%202-%20[[Lecture%202-%20Asset%20Allocation%20with%20Multiple%20Risky%20Assets) with [Multiple Risky Assets](../../Advanced%20Investments/Lecture%202-%20Asset%20Allocation%20with%20Multiple%20Risky%20Assets.md)|[asset allocation](../../Advanced%20Investments/Lecture%202-%20Asset%20Allocation%20with%20Multiple%20Risky%20Assets.md)]],  as its performance (-19.0 bp) was close to that of the benchmark (-22.0 bp).

### 4.2 Implications for [asset allocation](../../Advanced%20Investments/Lecture%202-%20Asset%20Allocation%20with%20Multiple%20Risky%20Assets.md)

- The manager's overweight to U.S. [Corporate Bonds](../../Financial%20Markets%20and%20Institutions/II.%20The%20Roles%20of%20Banks%20and%20Derivative%20Markets%20in%20Resolving%20Problems%20Inherent%20in%20Debt%20Contracts/Class%202-%20Debt%20Contracts%20due%20to%20Lack%20of%20Information/Class%20Notes%202%20–%20Corporate%20Bond%20Contracts.md) was a key source of underperformance,  highlighting the risks of sector overweights in underperforming markets.
- **Recommendations**:
  - Reassess sector overweights in light of benchmark performance trends.
  - Consider diversifying sector exposures to mitigate the impact of underperformance in specific sectors.

## 5. Summary and Key Takeaways

### 5.1 Yield-Curve Outperformance

- The **Euro** market contributed significantly to total [portfolio](../../Advanced%20Investments/An%20Asset%20Allocation%20Primer.md) outperformance (+17.9 bp),  driven by well-aligned [duration](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%205/Key%20Rates%20O1s%20Durations%20and%20Hedging.md) overweights and strong bull-flattening.
- The **Japanese Yen** market contributed modestly (+3.0 bp),  as the yield-curve movement was insufficiently pronounced.
- The **British Pound** market detracted significantly (-11.5 bp),  highlighting the risks of [duration](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%205/Key%20Rates%20O1s%20Durations%20and%20Hedging.md) underweights in markets with strong yield-curve movements.

### 5.2 Portfolio Management Implications

- Yield-curve management is a critical driver of fixed-income [portfolio](../../Advanced%20Investments/An%20Asset%20Allocation%20Primer.md) performance and should be prioritized in the [portfolio construction](../../Financial%20Markets/Financial%20Asset%20Pricing%20Theory%20Overview/Chapter%2012%20-%20Derivatives/Exercises.md) process.
- The manager should consider adopting a global yield-curve management framework to ensure consistent alignment of [duration](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%205/Key%20Rates%20O1s%20Durations%20and%20Hedging.md) exposures across currencies.

### 5.3 [asset allocation](../../Advanced%20Investments/Lecture%202-%20Asset%20Allocation%20with%20Multiple%20Risky%20Assets.md) and Security Selection

- The U.S. dollar market's [Asset Allocation](Lecture%202-%20[[Lecture%202-%20Asset%20Allocation%20with%20Multiple%20Risky%20Assets) with [Multiple Risky Assets](../../Advanced%20Investments/Lecture%202-%20Asset%20Allocation%20with%20Multiple%20Risky%20Assets.md)|[asset allocation](../../Advanced%20Investments/Lecture%202-%20Asset%20Allocation%20with%20Multiple%20Risky%20Assets.md)]] contributed -2.5 bp to total [portfolio](../../Advanced%20Investments/An%20Asset%20Allocation%20Primer.md) underperformance,  driven by the overweight to [Corporate Bonds](../../Financial%20Markets%20and%20Institutions/II.%20The%20Roles%20of%20Banks%20and%20Derivative%20Markets%20in%20Resolving%20Problems%20Inherent%20in%20Debt%20Contracts/Class%202-%20Debt%20Contracts%20due%20to%20Lack%20of%20Information/Class%20Notes%202%20–%20Corporate%20Bond%20Contracts.md).
- The manager should reassess sector overweights and consider diversifying exposures to mitigate the impact of sector underperformance.

By understanding the sources of yield-curve outperformance and refining [portfolio management](../../Financial%20Engineering/Fixed%20Income%20Derivatives/The%20Impact%20of%20Option%20Strategies%20in%20Financial%20%20Portfolios%20Performance.md) strategies,  fixed-income managers can optimize risk-adjusted [returns](../../Financial%20Markets/Financial%20Asset%20Pricing%20Theory%20Overview/Chapter%203%20-%20%20Assets,%20Portfolios,%20and%20Arbitrage/Assets.md) and achieve their [investment](../../Advanced%20Investments/An%20Asset%20Allocation%20Primer.md) objectives.

## Lecture Notes: U.S. and Euro Security Selection Breakdown and Performance Attribution

### 1. Introduction to Security Selection and Performance Attribution

- Security selection is a critical component of fixed-income [portfolio management](../../Financial%20Engineering/Fixed%20Income%20Derivatives/The%20Impact%20of%20Option%20Strategies%20in%20Financial%20%20Portfolios%20Performance.md),  as it directly impacts [portfolio](../../Advanced%20Investments/An%20Asset%20Allocation%20Primer.md) outperformance relative to the benchmark.
- This lecture focuses on:
  - The U.S. security selection breakdown and its contribution to [portfolio](../../Advanced%20Investments/An%20Asset%20Allocation%20Primer.md) outperformance.
  - The Euro security selection breakdown and its significant underperformance.
  - Key takeaways and recommendations for improving security selection and managing risks.

### 2. U.S. Security Selection Breakdown (Exhibit 70-10)

#### 2.1 Overview of U.S. Security Selection

| **Sector** | **[Portfolio](../../Advanced%20Investments/An%20Asset%20Allocation%20Primer.md) Weight (%)** | **Benchmark Weight (%)** | **Excess Return ([Portfolio](../../Advanced%20Investments/An%20Asset%20Allocation%20Primer.md),  bp)** | **Excess Return (Benchmark,  bp)** | **Security Selection (bp)** |

| **Total** | 100.0 | 100.0 | -14.6 | -22.0 | +13.0 |

| **Treasury** | 31.7 | 31.7 | -4.7 | -2.2 | -0.8 |

| **Govt-Related** | 14.3 | 14.3 | +17.6 | -7.7 | +3.7 |

| **Corporate** | 30.7 | 19.8 | -33.5 | -70.2 | +11.1 |

| **Securitized** | 22.8 | 33.4 | -23.3 | -19.0 | -1.0 |

| **Cash** | 0.5 | 0.8 | 0.0 | 0.0 | 0.0 |

#### 2.2 Key Observations

1. **Corporate Sector**:
   - The corporate sector contributed **+11.1 bp** to security selection outperformance,  making it the dominant contributor.
   - Positive contributions came from securities such as **[Morgan Stanley](../../Financial%20Markets%20and%20Institutions/III.%20Liquidity%20of%20Assets/Class%208-%20Markets,%20Meltdowns,%20and%20Arbitrage/Lessons%20From%20The%20Crisis.md) (+3.9 bp)**,  **Rabobank (+3.7 bp)**,  and **[JP Morgan](../../Financial%20Markets%20and%20Institutions/III.%20Liquidity%20of%20Assets/Class%209-%20Bailouts%20and%20Bank%20Failures/The%20Fall%20of%20Bear%20Stearns.md) (+3.4 bp)**.
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
- **Implication**: The Comcast bond's significant underperformance highlights the importance of name selection in a concentrated [portfolio](../../Advanced%20Investments/An%20Asset%20Allocation%20Primer.md).

### 3. Euro Security Selection Breakdown (Exhibit 70-11)

#### 3.1 Overview of Euro Security Selection

| **Sector** | **[Portfolio](../../Advanced%20Investments/An%20Asset%20Allocation%20Primer.md) Weight (%)** | **Benchmark Weight (%)** | **Excess Return ([Portfolio](../../Advanced%20Investments/An%20Asset%20Allocation%20Primer.md),  bp)** | **Excess Return (Benchmark,  bp)** | **Security Selection (bp)** |

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
- **Implication**: The manager should take control of country exposure within the euro sector to mitigate sovereign [credit risk](../../Course%20Notes/Quantitative%20Trading%20Strategies%20Lecture%20Notes.md).

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
   - The manager should actively manage country exposure within the euro sector to mitigate sovereign [credit risk](../../Course%20Notes/Quantitative%20Trading%20Strategies%20Lecture%20Notes.md).

1. **Corporate Sector**:
   - The corporate sector contributed positively (**+18.2 bp**),  driven by strong performers like GE Capital and Royal Bank of Scotland.

1. **Recommendations**:
   - Reduce exposure to high-risk sovereigns like Italy.
   - Focus on high-quality corporate issuers to drive outperformance.

### 5. Summary and Key Takeaways

1. **U.S. Security Selection**:
   - The U.S. corporate sector was the dominant contributor to security selection outperformance,  but individual detractors like Comcast highlight the importance of name selection.

1. **Euro Security Selection**:
   - The euro market's significant underperformance was driven by Italian government bonds,  underscoring the need for active [country risk](../../International%20Finance/Bridgewater/How%20Countries%20Go%20Broke/How%20Countries%20Go%20Broke-Chapter%2015%20&%20Chapter%2016.md) management.

1. **Recommendations**:
   - Enhance name selection processes to avoid significant detractors.
   - Actively manage country exposure within the euro sector to mitigate sovereign [credit risk](../../Course%20Notes/Quantitative%20Trading%20Strategies%20Lecture%20Notes.md).
   - [Leverage](../../Advanced%20Investments/Lecture%206-Leverage,%20Tail%20Risk,%20Volatility%20Products.md) strong performers in the corporate and government-related sectors to drive outperformance.

By addressing these areas,  [portfolio](../../Advanced%20Investments/An%20Asset%20Allocation%20Primer.md) managers can optimize security selection and improve overall [portfolio](../../Advanced%20Investments/An%20Asset%20Allocation%20Primer.md) performance.

### Lecture Notes: Advanced Performance Attribution in Fixed Income Portfolio Management – Euro Security Selection and Analytical Models

## 1. Introduction to Euro Security Selection and Analytical Models

- Performance attribution in [fixed income](../Lecture%20Notes%20Bonds,%20%20Preferred%20Stock,%20%20and%20Structured%20Products.md) portfolios involves decomposing [returns](../../Financial%20Markets/Financial%20Asset%20Pricing%20Theory%20Overview/Chapter%203%20-%20%20Assets,%20Portfolios,%20and%20Arbitrage/Assets.md) into contributions from various factors,  such as yield-curve movements,  credit spreads,  and security selection.
- This lecture focuses on:
  - The detailed breakdown of Euro security selection and its impact on [portfolio](../../Advanced%20Investments/An%20Asset%20Allocation%20Primer.md) performance.
  - The role of fully analytical models in identifying residuals and improving data quality.
  - The importance of scenario-based return decomposition and analytics-based attribution in [fixed income](../Lecture%20Notes%20Bonds,%20%20Preferred%20Stock,%20%20and%20Structured%20Products.md) portfolios.

## 2. Euro Security Selection Breakdown

### 2.1 Overview of Euro Security Selection (Exhibit 70-11)

| **Bucket/Issue** | **Issuer** | **$MV(\%)$ Portf** | **Excess to Curve [Returns](../../Financial%20Markets/Financial%20Asset%20Pricing%20Theory%20Overview/Chapter%203%20-%20%20Assets,%20Portfolios,%20and%20Arbitrage/Assets.md) (bp)** | **Security Selection (bp)** |

| **IBESM** | IBERDROLA | 22.7 | 1.1 | 2.2 |

| **$BAC$** | MERRILL LYNCH & CO INC | 13.2 | 5.5 | 2.0 |

| **IMTLN** | IMPERIAL TOBACCO FIN PLC | 16.7 | 0.9 | 1.6 |

| **$C$** | CITIGROUP INC | 4.8 | -181.4 | -2.7 |

| **Bmark Securities** | Not in [Portfolio](../../Advanced%20Investments/An%20Asset%20Allocation%20Primer.md) | 90.5 | -22.8 | -0.1 |

| **Securitized** | | 4.4 | 11.3 | -0.7 |

| **ES0312298237** | AYT CEDULAS CAJAS GLOBAL | 100.0 | 11.3 | -0.7 |

| **Cash** | | 0.3 | 0.0 | 0.0 |

#### Key Observations
1. **Positive Contributors**:
   - **IBERDROLA** contributed **+2.2 bp** due to strong excess [returns](../../Financial%20Markets/Financial%20Asset%20Pricing%20Theory%20Overview/Chapter%203%20-%20%20Assets,%20Portfolios,%20and%20Arbitrage/Assets.md) of **1.1 bp**.
   - **MERRILL LYNCH & CO INC** contributed **+2.0 bp**,  driven by excess [returns](../../Financial%20Markets/Financial%20Asset%20Pricing%20Theory%20Overview/Chapter%203%20-%20%20Assets,%20Portfolios,%20and%20Arbitrage/Assets.md) of **5.5 bp**.
   - **IMPERIAL TOBACCO FIN PLC** added **+1.6 bp**,  with excess [returns](../../Financial%20Markets/Financial%20Asset%20Pricing%20Theory%20Overview/Chapter%203%20-%20%20Assets,%20Portfolios,%20and%20Arbitrage/Assets.md) of **0.9 bp**.

1. **Negative Contributors**:
   - **CITIGROUP INC** detracted **-2.7 bp**,  with significant underperformance of **-181.4 bp** relative to the curve.
   - **Securitized** securities detracted **-0.7 bp**,  despite positive excess [returns](../../Financial%20Markets/Financial%20Asset%20Pricing%20Theory%20Overview/Chapter%203%20-%20%20Assets,%20Portfolios,%20and%20Arbitrage/Assets.md) of **11.3 bp**,  due to their small [portfolio](../../Advanced%20Investments/An%20Asset%20Allocation%20Primer.md) weight.

1. **Benchmark Securities**:
   - Securities not in the [portfolio](../../Advanced%20Investments/An%20Asset%20Allocation%20Primer.md) contributed **-0.1 bp**,  reflecting missed opportunities in the benchmark.

### 2.2 Residual Analysis and Data Quality Issues (Exhibit 70-13)

| **Bucket/Issue** | **Issuer** | **$MV(\%)$ Portf** | **Spread Carry (bp)** | **[Spread Change](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%207/Profit%20and%20Loss%20Attribution%20with%20an%20OAS.md) (bp)** | **Residual (bp)** | **Total (bp)** |

| **IT0004513641** | $ITALY$ | 18.3 | 0.6 | -22.3 | +17.4 | -3.7 |

| **IT0004356843** | $ITALY$ | 17.1 | 0.5 | -16.8 | -0.1 | -16.4 |

| **IT0004009673** | $ITALY$ | 15.8 | 0.3 | -17.1 | -0.1 | -16.9 |

#### Key Observations
1. **Residual Contribution**:
   - The bond **IT0004513641** contributed **+17.4 bp** of residual to the Euro [portfolio](../../Advanced%20Investments/An%20Asset%20Allocation%20Primer.md),  accounting for **+4.0 bp** of the total [portfolio](../../Advanced%20Investments/An%20Asset%20Allocation%20Primer.md)-level residual.
   - This residual was traced to a **data quality issue**,  where a coupon payment of **2.50%** was recorded twice.

1. **Impact of Data Correction**:
   - After correcting the double entry,  the [portfolio](../../Advanced%20Investments/An%20Asset%20Allocation%20Primer.md) return decreased by **4.2 bp**,  and the residual term was reduced from **+4.4 bp** to **+0.2 bp**.

1. **Implications**:
   - Residuals can indicate data quality problems,  such as incorrect prices,  transaction errors,  or model deficiencies.
   - A robust performance attribution system can help identify and correct such issues promptly.

## 3. Fully Analytical Models and Scenario-Based Decomposition

### 3.1 Fully Analytical Models

- Fully analytical models decompose [returns](../../Financial%20Markets/Financial%20Asset%20Pricing%20Theory%20Overview/Chapter%203%20-%20%20Assets,%20Portfolios,%20and%20Arbitrage/Assets.md) into detailed components,  providing greater clarity into the sources of outperformance.
- **Key Features**:
  - Incorporates terms such as **[Implied Volatility](../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%205%20Options%20on%20Prices%20and%20Hedge-Based%20Valuation/A%20Real-Life%20Option%20Pricing%20Exercise.md)** and **Mortgage Contributions**.
  - Identifies residuals and their potential causes,  such as data errors or model deficiencies.

### 3.2 Scenario-Based Return Decomposition (Exhibit 71-1)

| **Return Component** | **Description** |

| **Surprise Return** | Difference between actual cash flows and model predictions. |

| **Time Return** | Effect of elapsing time. |

| **Yield-Curve Change Return** | Effect of changes in the yield curve. |

| **[Implied Volatility](../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%205%20Options%20on%20Prices%20and%20Hedge-Based%20Valuation/A%20Real-Life%20Option%20Pricing%20Exercise.md) Change** | Effect of changes in the [implied volatility surface](../../Course%20Notes/Python/QuantLib-Python/Modeling%20Volatility%20Smile%20and%20Heston%20Model%20Calibration%20Using%20QuantLib%20Python.md). |

| **Other Market Return** | Effect of changes in other market parameters. |

| **[Spread Change](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%207/Profit%20and%20Loss%20Attribution%20with%20an%20OAS.md) Return** | Effect of changes in the option-adjusted spread (OAS). |

#### Key Insights
1. **Surprise Return**:
   - Relevant for securities with non-[deterministic cash flows](../../Financial%20Engineering/1.%20DeterministicCashFlows.md),  such as [mortgage-backed securities](../../Financial%20Markets%20and%20Institutions/III.%20Liquidity%20of%20Assets/Class%207-%20CP,%20Repo,%20and%20the%20Crisis/Fremont%20Financial%20Corp.%20(b).md) or [inflation](../../International%20Finance/Bridgewater/Principles%20For%20Navigating%20Big%20Debt%20Cycles/Part%20II%20Detailed%20Case%20Studies/German%20Debt%20Crisis%20andHyperinflation%20(1918–1924)/War%20Economies%20and%20Hyperinflation.md)-linked bonds.
   - Captures deviations between realized and projected parameters.

1. **Residual**:
   - Represents unexplained differences between actual and modeled [returns](../../Financial%20Markets/Financial%20Asset%20Pricing%20Theory%20Overview/Chapter%203%20-%20%20Assets,%20Portfolios,%20and%20Arbitrage/Assets.md).
   - Can result from unaccounted model inputs,  higher-order terms,  or data errors.

## 4. Implications for Portfolio Management

### 4.1 Importance of Data Quality

- Data quality issues,  such as incorrect prices or duplicate entries,  can significantly impact performance measurement and attribution.
- **Example**:
  - The double entry of a coupon payment for **IT0004513641** inflated the residual by **+17.4 bp**,  masking the true sources of outperformance.

### 4.2 Managing Spread Duration Exposure

- The Euro [portfolio](../../Advanced%20Investments/An%20Asset%20Allocation%20Primer.md)'s concentration in Italian government bonds,  particularly long-maturity issues,  resulted in significant [spread duration](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%2014/Spread%20Duration%20and%20Dvo1.md) exposure.
- **Recommendation**:
  - [Spread duration](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%2014/Spread%20Duration%20and%20Dvo1.md) exposure in sectors with [credit risk](../../Course%20Notes/Quantitative%20Trading%20Strategies%20Lecture%20Notes.md) should be carefully controlled to avoid excessive sensitivity to spread changes.

### 4.3 Enhancing Attribution Models

- Fully analytical models provide a more detailed breakdown of [returns](../../Financial%20Markets/Financial%20Asset%20Pricing%20Theory%20Overview/Chapter%203%20-%20%20Assets,%20Portfolios,%20and%20Arbitrage/Assets.md),  allowing managers to identify and address specific sources of outperformance or underperformance.
- **Benefits**:
  - Greater transparency into residuals and their causes.
  - Improved alignment between attribution results and [portfolio management](../../Financial%20Engineering/Fixed%20Income%20Derivatives/The%20Impact%20of%20Option%20Strategies%20in%20Financial%20%20Portfolios%20Performance.md) decisions.

## 5. Summary and Key Takeaways

### 5.1 Euro Security Selection

- Positive contributors included **IBERDROLA** and **MERRILL LYNCH & CO INC**,  while **CITIGROUP INC** and Italian government bonds detracted significantly.
- Data quality issues,  such as the double entry for **IT0004513641**,  can inflate residuals and distort performance attribution.

### 5.2 Fully Analytical Models

- Fully analytical models decompose [returns](../../Financial%20Markets/Financial%20Asset%20Pricing%20Theory%20Overview/Chapter%203%20-%20%20Assets,%20Portfolios,%20and%20Arbitrage/Assets.md) into detailed components,  such as [implied volatility](../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%205%20Options%20on%20Prices%20and%20Hedge-Based%20Valuation/A%20Real-Life%20Option%20Pricing%20Exercise.md) and spread changes,  providing greater clarity into the sources of outperformance.
- Scenario-based decomposition helps identify residuals and their potential causes,  such as data errors or model deficiencies.

### 5.3 Recommendations for Portfolio Management

1. **Improve Data Quality**:
   - Regularly audit data to identify and correct errors,  such as duplicate entries or incorrect prices.

1. **Control [Spread Duration](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%2014/Spread%20Duration%20and%20Dvo1.md) Exposure**:
   - Avoid excessive concentration in sectors with high [credit risk](../../Course%20Notes/Quantitative%20Trading%20Strategies%20Lecture%20Notes.md),  such as long-maturity Italian government bonds.

1. **Adopt Fully Analytical Models**:
   - Use detailed attribution models to gain deeper insights into the sources of [portfolio](../../Advanced%20Investments/An%20Asset%20Allocation%20Primer.md) performance and residuals.

By addressing these areas,  [portfolio](../../Advanced%20Investments/An%20Asset%20Allocation%20Primer.md) managers can enhance performance attribution,  improve decision-making,  and optimize risk-adjusted [returns](../../Financial%20Markets/Financial%20Asset%20Pricing%20Theory%20Overview/Chapter%203%20-%20%20Assets,%20Portfolios,%20and%20Arbitrage/Assets.md).

### Lecture Notes: Advanced Performance Attribution in Fixed Income Portfolio Management – Prepayment,  Inflation,  and Yield-Curve Returns

## 1. Introduction to Advanced Attribution Components

- [Fixed income](../Lecture%20Notes%20Bonds,%20%20Preferred%20Stock,%20%20and%20Structured%20Products.md) [portfolio](../../Advanced%20Investments/An%20Asset%20Allocation%20Primer.md) performance attribution involves decomposing [returns](../../Financial%20Markets/Financial%20Asset%20Pricing%20Theory%20Overview/Chapter%203%20-%20%20Assets,%20Portfolios,%20and%20Arbitrage/Assets.md) into various components,  such as prepayment surprises,  [inflation](../../International%20Finance/Bridgewater/Principles%20For%20Navigating%20Big%20Debt%20Cycles/Part%20II%20Detailed%20Case%20Studies/German%20Debt%20Crisis%20andHyperinflation%20(1918–1924)/War%20Economies%20and%20Hyperinflation.md) surprises,  time [returns](../../Financial%20Markets/Financial%20Asset%20Pricing%20Theory%20Overview/Chapter%203%20-%20%20Assets,%20Portfolios,%20and%20Arbitrage/Assets.md),  yield-curve changes,  and spread changes.
- This lecture focuses on:
  - **Prepayment Surprise Return**: The impact of deviations in actual prepayments from model [expectations](../Fixed%20Income%20Lecture%20Notes/FORWARD%20RATES%20AND%20TERM%20STRUCTURE.md).
  - **[Inflation](../../International%20Finance/Bridgewater/Principles%20For%20Navigating%20Big%20Debt%20Cycles/Part%20II%20Detailed%20Case%20Studies/German%20Debt%20Crisis%20andHyperinflation%20(1918–1924)/War%20Economies%20and%20Hyperinflation.md) Surprise Return**: The effect of unexpected [inflation](../../International%20Finance/Bridgewater/Principles%20For%20Navigating%20Big%20Debt%20Cycles/Part%20II%20Detailed%20Case%20Studies/German%20Debt%20Crisis%20andHyperinflation%20(1918–1924)/War%20Economies%20and%20Hyperinflation.md) announcements on [inflation](../../International%20Finance/Bridgewater/Principles%20For%20Navigating%20Big%20Debt%20Cycles/Part%20II%20Detailed%20Case%20Studies/German%20Debt%20Crisis%20andHyperinflation%20(1918–1924)/War%20Economies%20and%20Hyperinflation.md)-linked securities.
  - **Time Return**: The deterministic return component driven by yield-curve carry,  spread carry,  and volatility decay.
  - **Yield-Curve Change Return**: The impact of interest rate movements on [portfolio](../../Advanced%20Investments/An%20Asset%20Allocation%20Primer.md) [returns](../../Financial%20Markets/Financial%20Asset%20Pricing%20Theory%20Overview/Chapter%203%20-%20%20Assets,%20Portfolios,%20and%20Arbitrage/Assets.md),  including [duration and convexity](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%208/An%20Analytical%20Decomposition%20of%20Forward%20Rates.md) effects.

## 2. Prepayment Surprise Return

### 2.1 Definition and Example

- **Prepayment Surprise Return** measures the difference between actual prepayments and model-projected prepayments for [mortgage-backed securities](../../Financial%20Markets%20and%20Institutions/III.%20Liquidity%20of%20Assets/Class%207-%20CP,%20Repo,%20and%20the%20Crisis/Fremont%20Financial%20Corp.%20(b).md) (MBS).
- **Example**:
  - **Security Price**: 105 (zero accrued).
  - **Model-Projected Prepayment**: 2.4% (25% CPR),  predicting a return of **+11.4 bp**.
  - **Actual Prepayment**: 1.3% (15% CPR),  resulting in a return of **-6.2 bp**.
  - **Prepayment Surprise Return**:
	$$\text{Surprise Return} = -6.2 \,    \text{bp} - 11.4 \,    \text{bp} = +5.2 \,    \text{bp}$$
- **Key Insight**:
  - The model-[expected return](../../Advanced%20Investments/Lecture%201-%20Probability%20Distributions%20of%20Returns.md) (**+11.4 bp**) is part of the **time return** component,  while the deviation (**+5.2 bp**) is attributed to prepayment surprise.

## 3. Inflation Surprise Return

### 3.1 Definition and Example

- **[Inflation](../../International%20Finance/Bridgewater/Principles%20For%20Navigating%20Big%20Debt%20Cycles/Part%20II%20Detailed%20Case%20Studies/German%20Debt%20Crisis%20andHyperinflation%20(1918–1924)/War%20Economies%20and%20Hyperinflation.md) Surprise Return** captures the impact of unexpected [inflation](../../International%20Finance/Bridgewater/Principles%20For%20Navigating%20Big%20Debt%20Cycles/Part%20II%20Detailed%20Case%20Studies/German%20Debt%20Crisis%20andHyperinflation%20(1918–1924)/War%20Economies%20and%20Hyperinflation.md) announcements on [inflation](../../International%20Finance/Bridgewater/Principles%20For%20Navigating%20Big%20Debt%20Cycles/Part%20II%20Detailed%20Case%20Studies/German%20Debt%20Crisis%20andHyperinflation%20(1918–1924)/War%20Economies%20and%20Hyperinflation.md)-linked securities.
- **Example**:
  - **Projected [Inflation](../../International%20Finance/Bridgewater/Principles%20For%20Navigating%20Big%20Debt%20Cycles/Part%20II%20Detailed%20Case%20Studies/German%20Debt%20Crisis%20andHyperinflation%20(1918–1924)/War%20Economies%20and%20Hyperinflation.md)**: 3.0%.
  - **Actual [Inflation](../../International%20Finance/Bridgewater/Principles%20For%20Navigating%20Big%20Debt%20Cycles/Part%20II%20Detailed%20Case%20Studies/German%20Debt%20Crisis%20andHyperinflation%20(1918–1924)/War%20Economies%20and%20Hyperinflation.md)**: 3.5%.
  - **[Inflation](../../International%20Finance/Bridgewater/Principles%20For%20Navigating%20Big%20Debt%20Cycles/Part%20II%20Detailed%20Case%20Studies/German%20Debt%20Crisis%20andHyperinflation%20(1918–1924)/War%20Economies%20and%20Hyperinflation.md) Surprise Return**: **+4.2 bp** due to higher-than-expected [inflation](../../International%20Finance/Bridgewater/Principles%20For%20Navigating%20Big%20Debt%20Cycles/Part%20II%20Detailed%20Case%20Studies/German%20Debt%20Crisis%20andHyperinflation%20(1918–1924)/War%20Economies%20and%20Hyperinflation.md) accretion.
- **Key Insight**:
  - This return is separate from any changes in future [inflation](../../International%20Finance/Bridgewater/Principles%20For%20Navigating%20Big%20Debt%20Cycles/Part%20II%20Detailed%20Case%20Studies/German%20Debt%20Crisis%20andHyperinflation%20(1918–1924)/War%20Economies%20and%20Hyperinflation.md) [expectations](../Fixed%20Income%20Lecture%20Notes/FORWARD%20RATES%20AND%20TERM%20STRUCTURE.md),  which are captured under **[inflation](../../International%20Finance/Bridgewater/Principles%20For%20Navigating%20Big%20Debt%20Cycles/Part%20II%20Detailed%20Case%20Studies/German%20Debt%20Crisis%20andHyperinflation%20(1918–1924)/War%20Economies%20and%20Hyperinflation.md) [spread change](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%207/Profit%20and%20Loss%20Attribution%20with%20an%20OAS.md)**.

## 4. Time Return

### 4.1 Components of Time Return

- **Time Return** is the deterministic component of return,  assuming no changes in market parameters.
- **Components**:
  - **Yield-Curve Carry**: Return from rolling down the yield curve.
  - **Spread Carry**: Return from holding securities with positive spreads.
  - **Volatility Decay**: Return from the passage of time reducing the value of optionality.
  - **[Inflation](../../International%20Finance/Bridgewater/Principles%20For%20Navigating%20Big%20Debt%20Cycles/Part%20II%20Detailed%20Case%20Studies/German%20Debt%20Crisis%20andHyperinflation%20(1918–1924)/War%20Economies%20and%20Hyperinflation.md) Accretion**: Return from [inflation](../../International%20Finance/Bridgewater/Principles%20For%20Navigating%20Big%20Debt%20Cycles/Part%20II%20Detailed%20Case%20Studies/German%20Debt%20Crisis%20andHyperinflation%20(1918–1924)/War%20Economies%20and%20Hyperinflation.md)-linked securities due to projected [inflation](../../International%20Finance/Bridgewater/Principles%20For%20Navigating%20Big%20Debt%20Cycles/Part%20II%20Detailed%20Case%20Studies/German%20Debt%20Crisis%20andHyperinflation%20(1918–1924)/War%20Economies%20and%20Hyperinflation.md).
  - **[Inflation](../../International%20Finance/Bridgewater/Principles%20For%20Navigating%20Big%20Debt%20Cycles/Part%20II%20Detailed%20Case%20Studies/German%20Debt%20Crisis%20andHyperinflation%20(1918–1924)/War%20Economies%20and%20Hyperinflation.md) Spread Carry**: Return from holding [inflation](../../International%20Finance/Bridgewater/Principles%20For%20Navigating%20Big%20Debt%20Cycles/Part%20II%20Detailed%20Case%20Studies/German%20Debt%20Crisis%20andHyperinflation%20(1918–1924)/War%20Economies%20and%20Hyperinflation.md)-linked securities with positive spreads.

## 5. Yield-Curve Change Return

### 5.1 Definition and Sensitivities

- **Yield-Curve Change Return** measures the impact of interest rate movements on [portfolio](../../Advanced%20Investments/An%20Asset%20Allocation%20Primer.md) [returns](../../Financial%20Markets/Financial%20Asset%20Pricing%20Theory%20Overview/Chapter%203%20-%20%20Assets,%20Portfolios,%20and%20Arbitrage/Assets.md).
- **Sensitivities**:
  - **Option-Adjusted [Duration](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%205/Key%20Rates%20O1s%20Durations%20and%20Hedging.md) (OAD)**: Sensitivity to parallel shifts in the yield curve.
  - **Key-Rate Durations (KRDs)**: Sensitivity to movements at specific points on the yield curve.
  - **Option-Adjusted [Convexity](../Problem%20Sets/PSET%20II%20Fixed%20Income%20Asset%20Pricing%201.md) (OAC)**: Second-order sensitivity to yield-curve changes.

### 5.2 Duration and Convexity Example

- **[Portfolio](../../Advanced%20Investments/An%20Asset%20Allocation%20Primer.md) Characteristics**:
  - **OAD**: 5.
  - **OAC**: -2.
- **Scenario**:
  - [Interest rates](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%202/Interest%20Rate%20Quotations.md) fall by **10 bp per day** over 10 business days,  for a total change of **-100 bp**.
- **Formula**:
 $R^{\Delta YC} = -OAD \cdot \Delta r + \frac{1}{2} \cdot \frac{OAC}{100} \cdot \Delta r^2$$
- **Calculation**:
  - **[Duration](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%205/Key%20Rates%20O1s%20Durations%20and%20Hedging.md) Return**:
	$$-5 \cdot (-100) = +500 \,    \text{bp}$$
  - **[Convexity](../Problem%20Sets/PSET%20II%20Fixed%20Income%20Asset%20Pricing%201.md) Return**:
	$$0.5 \cdot \frac{-2}{100} \cdot (-100)^2 = -100 \,    \text{bp}$$
  - **Total Return**:
	$$+500 \,    \text{bp} - 100 \,    \text{bp} = +400 \,    \text{bp}$$

### 5.3 Daily Attribution Adjustments

- **Daily Adjustments**:
  - [Duration](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%205/Key%20Rates%20O1s%20Durations%20and%20Hedging.md) drift due to falling [interest rates](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%202/Interest%20Rate%20Quotations.md) reduces the [portfolio](../../Advanced%20Investments/An%20Asset%20Allocation%20Primer.md)'s [duration](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%205/Key%20Rates%20O1s%20Durations%20and%20Hedging.md) by approximately 2 years over 10 days.
  - [Returns](../../Financial%20Markets/Financial%20Asset%20Pricing%20Theory%20Overview/Chapter%203%20-%20%20Assets,%20Portfolios,%20and%20Arbitrage/Assets.md) must be compounded daily.
- **Adjusted [Returns](../../Financial%20Markets/Financial%20Asset%20Pricing%20Theory%20Overview/Chapter%203%20-%20%20Assets,%20Portfolios,%20and%20Arbitrage/Assets.md)**:
  - **[Duration](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%205/Key%20Rates%20O1s%20Durations%20and%20Hedging.md) Return**: **+408 bp**.
  - **[Convexity](../Problem%20Sets/PSET%20II%20Fixed%20Income%20Asset%20Pricing%201.md) Return**: **-10 bp**.
  - **Total Return**: **+398 bp**.
- **Key Insight**:
  - Daily attribution models typically show smaller [convexity](../Problem%20Sets/PSET%20II%20Fixed%20Income%20Asset%20Pricing%201.md) contributions compared to [duration](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%205/Key%20Rates%20O1s%20Durations%20and%20Hedging.md) contributions.

### 5.4 Key-Rate Duration Attribution

- **Key-Rate Durations (KRDs)**:
  - Capture the contribution of yield-curve changes at specific points (e.g.,  2-year,  5-year,  10-year).
  - Any unexplained yield-curve change return is attributed to movements between key-rate points or higher-order terms.

## 6. Implied Volatility Change Return

### 6.1 Definition and Sensitivities

- **[Implied Volatility](../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%205%20Options%20on%20Prices%20and%20Hedge-Based%20Valuation/A%20Real-Life%20Option%20Pricing%20Exercise.md) Change Return** measures the impact of changes in [implied volatility](../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%205%20Options%20on%20Prices%20and%20Hedge-Based%20Valuation/A%20Real-Life%20Option%20Pricing%20Exercise.md) on securities with optionality.
- **Sensitivity**:
  - **Vega**: Price change for a 1% parallel shift in the [implied volatility surface](../../Course%20Notes/Python/QuantLib-Python/Modeling%20Volatility%20Smile%20and%20Heston%20Model%20Calibration%20Using%20QuantLib%20Python.md).
- **Advanced Models**:
  - Generate partial Vegas for multiple points on the [volatility surface](../../Financial%20Engineering/7.%20Black%20Scholes%20Model.md).
  - Decompose [implied volatility](../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%205%20Options%20on%20Prices%20and%20Hedge-Based%20Valuation/A%20Real-Life%20Option%20Pricing%20Exercise.md) change return into parallel and non-parallel components.

### 6.2 Example

- **Scenario**:
  - Vega: 0.5.
  - Parallel Volatility Shift: +2%.
  - **Parallel Component**:
	$$\text{Return} = 0.5 \cdot 2 = +1.0 \,    \text{bp}$$
  - **Non-Parallel Component**:
	- Captures the effects of reshaping the [volatility surface](../../Financial%20Engineering/7.%20Black%20Scholes%20Model.md) and interactions with other model parameters.

## 7. Spread Change Return

### 7.1 Definition and Sensitivities

- **[Spread Change](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%207/Profit%20and%20Loss%20Attribution%20with%20an%20OAS.md) Return** measures the impact of changes in option-adjusted spreads (OAS) on [portfolio](../../Advanced%20Investments/An%20Asset%20Allocation%20Primer.md) [returns](../../Financial%20Markets/Financial%20Asset%20Pricing%20Theory%20Overview/Chapter%203%20-%20%20Assets,%20Portfolios,%20and%20Arbitrage/Assets.md).
- **Sensitivities**:
  - **[Spread Duration](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%2014/Spread%20Duration%20and%20Dvo1.md) (OASD)**: First-order sensitivity to spread changes.
  - **Spread [Convexity](../Problem%20Sets/PSET%20II%20Fixed%20Income%20Asset%20Pricing%201.md) (OASC)**: Second-order sensitivity to spread changes.

### 7.2 Example

- **Scenario**:
  - OASD: 4.
  - OASC: -1.
  - Spread widens by **50 bp**.
- **Formula**:
 $R^{\Delta \text{Spread}} = -OASD \cdot \Delta \text{Spread} + \frac{1}{2} \cdot OASC \cdot (\Delta \text{Spread})^2$$
- **Calculation**:
  - **[Duration](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%205/Key%20Rates%20O1s%20Durations%20and%20Hedging.md) Return**:
	$$-4 \cdot 50 = -200 \,    \text{bp}$$
  - **[Convexity](../Problem%20Sets/PSET%20II%20Fixed%20Income%20Asset%20Pricing%201.md) Return**:
	$$0.5 \cdot (-1) \cdot (50)^2 = -125 \,    \text{bp}$$
  - **Total Return**:
	$$-200 \,    \text{bp} - 125 \,    \text{bp} = -325 \,    \text{bp}$$

## 8. Other Market Return

### 8.1 Definition

- **Other Market Return** captures the impact of changes in external factors not directly related to yield-curve or [implied volatility](../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%205%20Options%20on%20Prices%20and%20Hedge-Based%20Valuation/A%20Real-Life%20Option%20Pricing%20Exercise.md) changes.
- **Examples**:
  - [Mortgage-backed securities](../../Financial%20Markets%20and%20Institutions/III.%20Liquidity%20of%20Assets/Class%207-%20CP,%20Repo,%20and%20the%20Crisis/Fremont%20Financial%20Corp.%20(b).md): [Prepayment rates](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%2015/Mortgage%20Pools.md),  home price appreciation [expectations](../Fixed%20Income%20Lecture%20Notes/FORWARD%20RATES%20AND%20TERM%20STRUCTURE.md).
  - [Inflation](../../International%20Finance/Bridgewater/Principles%20For%20Navigating%20Big%20Debt%20Cycles/Part%20II%20Detailed%20Case%20Studies/German%20Debt%20Crisis%20andHyperinflation%20(1918–1924)/War%20Economies%20and%20Hyperinflation.md)-linked securities: Changes in [inflation](../../International%20Finance/Bridgewater/Principles%20For%20Navigating%20Big%20Debt%20Cycles/Part%20II%20Detailed%20Case%20Studies/German%20Debt%20Crisis%20andHyperinflation%20(1918–1924)/War%20Economies%20and%20Hyperinflation.md) [expectations](../Fixed%20Income%20Lecture%20Notes/FORWARD%20RATES%20AND%20TERM%20STRUCTURE.md).

## 9. Summary and Key Takeaways

### 9.1 Prepayment and Inflation Surprises

- **Prepayment Surprise Return**: Captures deviations in actual prepayments from model [expectations](../Fixed%20Income%20Lecture%20Notes/FORWARD%20RATES%20AND%20TERM%20STRUCTURE.md).
- **[Inflation](../../International%20Finance/Bridgewater/Principles%20For%20Navigating%20Big%20Debt%20Cycles/Part%20II%20Detailed%20Case%20Studies/German%20Debt%20Crisis%20andHyperinflation%20(1918–1924)/War%20Economies%20and%20Hyperinflation.md) Surprise Return**: Measures the impact of unexpected [inflation](../../International%20Finance/Bridgewater/Principles%20For%20Navigating%20Big%20Debt%20Cycles/Part%20II%20Detailed%20Case%20Studies/German%20Debt%20Crisis%20andHyperinflation%20(1918–1924)/War%20Economies%20and%20Hyperinflation.md) announcements on [inflation](../../International%20Finance/Bridgewater/Principles%20For%20Navigating%20Big%20Debt%20Cycles/Part%20II%20Detailed%20Case%20Studies/German%20Debt%20Crisis%20andHyperinflation%20(1918–1924)/War%20Economies%20and%20Hyperinflation.md)-linked securities.

### 9.2 Yield-Curve and Spread Changes

- **Yield-Curve Change Return**: Driven by [duration and convexity](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%208/An%20Analytical%20Decomposition%20of%20Forward%20Rates.md) effects,  with key-rate durations capturing specific curve movements.
- **[Spread Change](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%207/Profit%20and%20Loss%20Attribution%20with%20an%20OAS.md) Return**: Captures the impact of OAS changes,  with [convexity](../Problem%20Sets/PSET%20II%20Fixed%20Income%20Asset%20Pricing%201.md) effects becoming significant during large spread moves.

### 9.3 Advanced Attribution Models

- Fully analytical models provide detailed decompositions of [returns](../../Financial%20Markets/Financial%20Asset%20Pricing%20Theory%20Overview/Chapter%203%20-%20%20Assets,%20Portfolios,%20and%20Arbitrage/Assets.md),  enabling [portfolio](../../Advanced%20Investments/An%20Asset%20Allocation%20Primer.md) managers to identify and address specific sources of outperformance or underperformance.
- Scenario-based decomposition is essential for securities with complex cash flows or optionality.

By mastering these advanced attribution components,  [fixed income](../Lecture%20Notes%20Bonds,%20%20Preferred%20Stock,%20%20and%20Structured%20Products.md) [portfolio](../../Advanced%20Investments/An%20Asset%20Allocation%20Primer.md) managers can optimize risk-adjusted [returns](../../Financial%20Markets/Financial%20Asset%20Pricing%20Theory%20Overview/Chapter%203%20-%20%20Assets,%20Portfolios,%20and%20Arbitrage/Assets.md) and enhance decision-making processes.

# Lecture Notes: Advanced Performance Attribution in Fixed Income Portfolio Management – Two-Level [asset allocation](../../Advanced%20Investments/Lecture%202-%20Asset%20Allocation%20with%20Multiple%20Risky%20Assets.md),  Yield-Curve Exposure,  and Excess Return Model

## 1. Introduction to Two-Level [asset allocation](../../Advanced%20Investments/Lecture%202-%20Asset%20Allocation%20with%20Multiple%20Risky%20Assets.md) and Performance Attribution

- Performance attribution in [fixed income](../Lecture%20Notes%20Bonds,%20%20Preferred%20Stock,%20%20and%20Structured%20Products.md) portfolios involves decomposing [returns](../../Financial%20Markets/Financial%20Asset%20Pricing%20Theory%20Overview/Chapter%203%20-%20%20Assets,%20Portfolios,%20and%20Arbitrage/Assets.md) into contributions from [Asset Allocation](Lecture%202-%20[[Lecture%202-%20Asset%20Allocation%20with%20Multiple%20Risky%20Assets) with [Multiple Risky Assets](../../Advanced%20Investments/Lecture%202-%20Asset%20Allocation%20with%20Multiple%20Risky%20Assets.md)|[asset allocation](../../Advanced%20Investments/Lecture%202-%20Asset%20Allocation%20with%20Multiple%20Risky%20Assets.md)]],  security selection,  and exposure to common factors such as yield-curve movements and [implied volatility](../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%205%20Options%20on%20Prices%20and%20Hedge-Based%20Valuation/A%20Real-Life%20Option%20Pricing%20Exercise.md).
- This lecture focuses on:
  - Two-level [Asset Allocation](Lecture%202-%20[[Lecture%202-%20Asset%20Allocation%20with%20Multiple%20Risky%20Assets) with [Multiple Risky Assets](../../Advanced%20Investments/Lecture%202-%20Asset%20Allocation%20with%20Multiple%20Risky%20Assets.md)|[asset allocation](../../Advanced%20Investments/Lecture%202-%20Asset%20Allocation%20with%20Multiple%20Risky%20Assets.md)]] and its impact on performance attribution.
  - Yield-curve exposure and its contribution to outperformance.
  - The Excess Return Model and its application in separating yield-curve and excess return contributions.

## 2. Two-Level Asset Allocation Using the Total Return Model

### 2.1 Overview of Two-Level Asset Allocation

- Two-level [Asset Allocation](Lecture%202-%20[[Lecture%202-%20Asset%20Allocation%20with%20Multiple%20Risky%20Assets) with [Multiple Risky Assets](../../Advanced%20Investments/Lecture%202-%20Asset%20Allocation%20with%20Multiple%20Risky%20Assets.md)|[asset allocation](../../Advanced%20Investments/Lecture%202-%20Asset%20Allocation%20with%20Multiple%20Risky%20Assets.md)]] introduces a finer partition of asset classes into subsectors,  providing a more detailed breakdown of outperformance.
- **Key Insight**:
  - The finer the partition,  the more emphasis is placed on [Asset Allocation](Lecture%202-%20[[Lecture%202-%20Asset%20Allocation%20with%20Multiple%20Risky%20Assets) with [Multiple Risky Assets](../../Advanced%20Investments/Lecture%202-%20Asset%20Allocation%20with%20Multiple%20Risky%20Assets.md)|[asset allocation](../../Advanced%20Investments/Lecture%202-%20Asset%20Allocation%20with%20Multiple%20Risky%20Assets.md)]] decisions versus security selection decisions.
  - Conversely,  broader partitions attribute more outperformance to security selection.

### 2.2 Level 1 Asset Allocation Breakdown (Exhibit 71-6)

| **Partition Bucket** | **Market Weight (%)** | **Return ex Common Factors** | **Outperformance (bps)** |

| **Total** | 100.0 | [Portfolio](../../Advanced%20Investments/An%20Asset%20Allocation%20Primer.md): 161.6,  Benchmark: 129.8 | [Asset Allocation](../../Advanced%20Investments/Lecture%202-%20Asset%20Allocation%20with%20Multiple%20Risky%20Assets.md): +18.9,  Further Allocation: -16.0,  Security Selection: +29.2 |

| **Treasury** | 31.7 | [Portfolio](../../Advanced%20Investments/An%20Asset%20Allocation%20Primer.md): 315.4,  Benchmark: 201.1 | [Asset Allocation](../../Advanced%20Investments/Lecture%202-%20Asset%20Allocation%20with%20Multiple%20Risky%20Assets.md): 0.0,  Security Selection: +36.3 |

| **Government-Related** | 14.3 | [Portfolio](../../Advanced%20Investments/An%20Asset%20Allocation%20Primer.md): 123.9,  Benchmark: 129.5 | [Asset Allocation](../../Advanced%20Investments/Lecture%202-%20Asset%20Allocation%20with%20Multiple%20Risky%20Assets.md): 0.0,  Further Allocation: -4.7,  Security Selection: +3.9 |

| **Corporate** | 30.7 | [Portfolio](../../Advanced%20Investments/An%20Asset%20Allocation%20Primer.md): 107.9,  Benchmark: 196.1 | [Asset Allocation](../../Advanced%20Investments/Lecture%202-%20Asset%20Allocation%20with%20Multiple%20Risky%20Assets.md): +7.4,  Further Allocation: -8.6,  Security Selection: -18.7 |

| **Securitized** | 22.8 | [Portfolio](../../Advanced%20Investments/An%20Asset%20Allocation%20Primer.md): 49.1,  Benchmark: 27.1 | [Asset Allocation](../../Advanced%20Investments/Lecture%202-%20Asset%20Allocation%20with%20Multiple%20Risky%20Assets.md): +11.0,  Further Allocation: -2.6,  Security Selection: +7.6 |

| **Cash** | 0.5 | [Portfolio](../../Advanced%20Investments/An%20Asset%20Allocation%20Primer.md): 0.0,  Benchmark: 0.0 | [Asset Allocation](../../Advanced%20Investments/Lecture%202-%20Asset%20Allocation%20with%20Multiple%20Risky%20Assets.md): +0.5,  Security Selection: 0.0 |

#### Key Observations
1. **Treasury Sector**:
   - Security selection contributed **+36.3 bp**,  driven by strong performance relative to the benchmark.
1. **Corporate Sector**:
   - Further allocation detracted **-8.6 bp**,  primarily due to an overweight in [financial institutions](../../Financial%20Markets%20and%20Institutions/Financial%20Markets%20and%20Institutions%20Lecture%20Notes.md),  which underperformed the corporate benchmark.
1. **Securitized Sector**:
   - Security selection contributed **+7.6 bp**,  driven by strong performance in RMBS securities.

### 2.3 Level 2 Asset Allocation Breakdown (Exhibit 71-7)

#### Government-Related Sector

| **Partition Bucket** | **Market Weight (%)** | **Return ex Common Factors** | **Outperformance (bps)** |

| **Agency** | [Portfolio](../../Advanced%20Investments/An%20Asset%20Allocation%20Primer.md): 98.3,  Benchmark: 70.5 | [Portfolio](../../Advanced%20Investments/An%20Asset%20Allocation%20Primer.md): 121.7,  Benchmark: 94.3 | [Asset Allocation](../../Advanced%20Investments/Lecture%202-%20Asset%20Allocation%20with%20Multiple%20Risky%20Assets.md): -1.4,  Security Selection: +3.9 |

| **Local Authority** | [Portfolio](../../Advanced%20Investments/An%20Asset%20Allocation%20Primer.md): 0.0,  Benchmark: 6.8 | [Portfolio](../../Advanced%20Investments/An%20Asset%20Allocation%20Primer.md): N/A,  Benchmark: 330.7 | [Asset Allocation](../../Advanced%20Investments/Lecture%202-%20Asset%20Allocation%20with%20Multiple%20Risky%20Assets.md): -2.0,  Security Selection: 0.0 |

| **Sovereign** | [Portfolio](../../Advanced%20Investments/An%20Asset%20Allocation%20Primer.md): 1.7,  Benchmark: 12.6 | [Portfolio](../../Advanced%20Investments/An%20Asset%20Allocation%20Primer.md): 253.4,  Benchmark: 232.7 | [Asset Allocation](../../Advanced%20Investments/Lecture%202-%20Asset%20Allocation%20with%20Multiple%20Risky%20Assets.md): -1.6,  Security Selection: 0.0 |

| **Supranational** | [Portfolio](../../Advanced%20Investments/An%20Asset%20Allocation%20Primer.md): 0.0,  Benchmark: 10.0 | [Portfolio](../../Advanced%20Investments/An%20Asset%20Allocation%20Primer.md): N/A,  Benchmark: 113.5 | [Asset Allocation](../../Advanced%20Investments/Lecture%202-%20Asset%20Allocation%20with%20Multiple%20Risky%20Assets.md): +0.2,  Security Selection: 0.0 |

#### Corporate Sector

| **Partition Bucket** | **Market Weight (%)** | **Return ex Common Factors** | **Outperformance (bps)** |

| **Industrial** | [Portfolio](../../Advanced%20Investments/An%20Asset%20Allocation%20Primer.md): 19.6,  Benchmark: 51.1 | [Portfolio](../../Advanced%20Investments/An%20Asset%20Allocation%20Primer.md): 171.3,  Benchmark: 214.6 | [Asset Allocation](../../Advanced%20Investments/Lecture%202-%20Asset%20Allocation%20with%20Multiple%20Risky%20Assets.md): -1.8,  Security Selection: -2.6 |

| **Utility** | [Portfolio](../../Advanced%20Investments/An%20Asset%20Allocation%20Primer.md): 0.0,  Benchmark: 10.4 | [Portfolio](../../Advanced%20Investments/An%20Asset%20Allocation%20Primer.md): N/A,  Benchmark: 251.2 | [Asset Allocation](../../Advanced%20Investments/Lecture%202-%20Asset%20Allocation%20with%20Multiple%20Risky%20Assets.md): -1.8,  Security Selection: 0.0 |

| **[Financial Institutions](../../Financial%20Markets%20and%20Institutions/Financial%20Markets%20and%20Institutions%20Lecture%20Notes.md)** | [Portfolio](../../Advanced%20Investments/An%20Asset%20Allocation%20Primer.md): 80.4,  Benchmark: 38.5 | [Portfolio](../../Advanced%20Investments/An%20Asset%20Allocation%20Primer.md): 92.4,  Benchmark: 157.0 | [Asset Allocation](../../Advanced%20Investments/Lecture%202-%20Asset%20Allocation%20with%20Multiple%20Risky%20Assets.md): -5.1,  Security Selection: -16.1 |

## 3. Yield-Curve Exposure and Outperformance

### 3.1 Yield-Curve Contribution to Outperformance

- Yield-curve exposure includes:
  - **Yield-Curve Change**: Impact of [interest rate changes](../../International%20Finance/Bridgewater/How%20Countries%20Go%20Broke/How%20Countries%20Go%20Broke-Chapter%2012%20to%20Chapter%2014.md).
  - **Yield-Curve Carry**: Impact of rolling down the yield curve.
- **Key Insight**:
  - The total yield-curve effect is the sum of yield-curve change and carry,  regardless of the methodology used.

### 3.2 Methodology I: Rolling on Forwards

- A yield-curve is deemed unchanged if rates realize the values implied by forward rates.
- **Example**:
  - One-month forward one-year rate is used as the reference for the one-year rate one month into the future.
- **Implications**:
  - Carry accrues at the [short rate](../Fixed%20Income%20Lecture%20Notes/An%20Overview%20of%20the%20Vasicek%20Short%20Rate%20Model.md).
  - Yield-curve change is calculated relative to forward rates.

### 3.3 Methodology II: Static Yield-Curve

- A yield-curve is deemed unchanged if rates remain constant over time.
- **Implications**:
  - Carry accrues at the long rate.
  - Yield-curve change is calculated relative to the static curve.

## 4. Excess Return Model

### 4.1 Overview of the Excess Return Model

- The Excess Return Model separates outperformance into:
  - **Yield-Curve Contribution**: Exposure to [interest rate changes](../../International%20Finance/Bridgewater/How%20Countries%20Go%20Broke/How%20Countries%20Go%20Broke-Chapter%2012%20to%20Chapter%2014.md) and carry.
  - **Excess Return**: Outperformance relative to the yield curve,  including [asset allocation](../../Advanced%20Investments/Lecture%202-%20Asset%20Allocation%20with%20Multiple%20Risky%20Assets.md) and security selection.

### 4.2 Excess Return Model Breakdown (Exhibit 71-8)

| **Component** | **Yield-Curve Only (bps)** | **Yield-Curve + [Implied Volatility](../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%205%20Options%20on%20Prices%20and%20Hedge-Based%20Valuation/A%20Real-Life%20Option%20Pricing%20Exercise.md) (bps)** |

| **Yield-Curve** | +24.6 | +24.6 |

| **[Implied Volatility](../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%205%20Options%20on%20Prices%20and%20Hedge-Based%20Valuation/A%20Real-Life%20Option%20Pricing%20Exercise.md)** | N/A | +1.9 |

| **[Asset Allocation](../../Advanced%20Investments/Lecture%202-%20Asset%20Allocation%20with%20Multiple%20Risky%20Assets.md)** | -2.2 | -4.0 |

| **Security Selection** | +9.7 | +9.6 |

#### Key Observations
1. **Yield-Curve Contribution**:
   - Yield-curve exposure contributed **+24.6 bp** to outperformance.
1. **[Implied Volatility](../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%205%20Options%20on%20Prices%20and%20Hedge-Based%20Valuation/A%20Real-Life%20Option%20Pricing%20Exercise.md) Contribution**:
   - Adding [implied volatility](../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%205%20Options%20on%20Prices%20and%20Hedge-Based%20Valuation/A%20Real-Life%20Option%20Pricing%20Exercise.md) as a common factor contributed an additional **+1.9 bp**.
1. **[Asset Allocation](Lecture%202-%20[[Lecture%202-%20Asset%20Allocation%20with%20Multiple%20Risky%20Assets) with [Multiple Risky Assets](../../Advanced%20Investments/Lecture%202-%20Asset%20Allocation%20with%20Multiple%20Risky%20Assets.md)|[asset allocation](../../Advanced%20Investments/Lecture%202-%20Asset%20Allocation%20with%20Multiple%20Risky%20Assets.md)]]**:
   - [Asset allocation](../../Advanced%20Investments/Lecture%202-%20Asset%20Allocation%20with%20Multiple%20Risky%20Assets.md) detracted **-2.2 bp** when only yield-curve exposure was considered,  and **-4.0 bp** when [implied volatility](../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%205%20Options%20on%20Prices%20and%20Hedge-Based%20Valuation/A%20Real-Life%20Option%20Pricing%20Exercise.md) was included.
1. **Security Selection**:
   - Security selection contributed **+9.7 bp** with yield-curve exposure and **+9.6 bp** with [implied volatility](../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%205%20Options%20on%20Prices%20and%20Hedge-Based%20Valuation/A%20Real-Life%20Option%20Pricing%20Exercise.md).

## 5. Implications for Portfolio Management

### 5.1 Importance of Two-Level [asset allocation](../../Advanced%20Investments/Lecture%202-%20Asset%20Allocation%20with%20Multiple%20Risky%20Assets.md)

- Two-level [Asset Allocation](Lecture%202-%20[[Lecture%202-%20Asset%20Allocation%20with%20Multiple%20Risky%20Assets) with [Multiple Risky Assets](../../Advanced%20Investments/Lecture%202-%20Asset%20Allocation%20with%20Multiple%20Risky%20Assets.md)|[asset allocation](../../Advanced%20Investments/Lecture%202-%20Asset%20Allocation%20with%20Multiple%20Risky%20Assets.md)]] provides a more granular view of [portfolio](../../Advanced%20Investments/An%20Asset%20Allocation%20Primer.md) decisions,  highlighting the impact of subsector allocations.
- **Recommendation**:
  - Use two-level attribution to identify underperforming subsectors and refine allocation decisions.

### 5.2 Managing Yield-Curve Exposure

- Yield-curve exposure is a significant driver of [fixed income](../Lecture%20Notes%20Bonds,%20%20Preferred%20Stock,%20%20and%20Structured%20Products.md) outperformance.
- **Recommendation**:
  - Align [duration](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%205/Key%20Rates%20O1s%20Durations%20and%20Hedging.md) and key-rate exposures with expected yield-curve movements to maximize carry and minimize adverse [rate changes](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%207/Profit%20and%20Loss%20Attribution%20with%20an%20OAS.md).

### 5.3 Incorporating Implied Volatility

- [Implied volatility](../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%205%20Options%20on%20Prices%20and%20Hedge-Based%20Valuation/A%20Real-Life%20Option%20Pricing%20Exercise.md) is an important factor for securities with optionality.
- **Recommendation**:
  - Include [implied volatility](../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%205%20Options%20on%20Prices%20and%20Hedge-Based%20Valuation/A%20Real-Life%20Option%20Pricing%20Exercise.md) in attribution models to capture its contribution to outperformance.

## 6. Summary and Key Takeaways

### 6.1 Two-Level [asset allocation](../../Advanced%20Investments/Lecture%202-%20Asset%20Allocation%20with%20Multiple%20Risky%20Assets.md)

- Two-level [Asset Allocation](Lecture%202-%20[[Lecture%202-%20Asset%20Allocation%20with%20Multiple%20Risky%20Assets) with [Multiple Risky Assets](../../Advanced%20Investments/Lecture%202-%20Asset%20Allocation%20with%20Multiple%20Risky%20Assets.md)|[asset allocation](../../Advanced%20Investments/Lecture%202-%20Asset%20Allocation%20with%20Multiple%20Risky%20Assets.md)]] provides a detailed breakdown of outperformance,  highlighting the impact of subsector allocations.
- [Asset allocation](../../Advanced%20Investments/Lecture%202-%20Asset%20Allocation%20with%20Multiple%20Risky%20Assets.md) contributed **+2.9 bp**,  while security selection contributed **+29.2 bp** in the two-level model.

### 6.2 Yield-Curve Exposure

- Yield-curve exposure contributed **+24.6 bp** to outperformance,  driven by both yield-curve change and carry.
- Methodologies for defining yield-curve changes (rolling on [forwards](../../Financial%20Markets/Financial%20Asset%20Pricing%20Theory%20Overview/Chapter%2012%20-%20Derivatives/Forwards%20and%20Futures.md) vs. static yield-curve) affect the breakdown but not the total contribution.

### 6.3 Excess Return Model

- The Excess Return Model separates yield-curve and excess return contributions,  providing a clearer view of [portfolio](../../Advanced%20Investments/An%20Asset%20Allocation%20Primer.md) performance.
- Adding [implied volatility](../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%205%20Options%20on%20Prices%20and%20Hedge-Based%20Valuation/A%20Real-Life%20Option%20Pricing%20Exercise.md) as a common factor enhances the model's explanatory power.

By adopting advanced attribution techniques,  [fixed income](../Lecture%20Notes%20Bonds,%20%20Preferred%20Stock,%20%20and%20Structured%20Products.md) [portfolio](../../Advanced%20Investments/An%20Asset%20Allocation%20Primer.md) managers can optimize risk-adjusted [returns](../../Financial%20Markets/Financial%20Asset%20Pricing%20Theory%20Overview/Chapter%203%20-%20%20Assets,%20Portfolios,%20and%20Arbitrage/Assets.md),  refine allocation decisions,  and enhance their understanding of performance drivers.

### Lecture Notes: Advanced Yield-Curve and Implied Volatility Attribution in Fixed Income Portfolio Management

## 1. Introduction to Yield-Curve and Implied Volatility Attribution

- Yield-curve and [implied volatility](../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%205%20Options%20on%20Prices%20and%20Hedge-Based%20Valuation/A%20Real-Life%20Option%20Pricing%20Exercise.md) changes are critical drivers of fixed-income [portfolio](../../Advanced%20Investments/An%20Asset%20Allocation%20Primer.md) performance. Proper attribution of these components provides insights into the sources of outperformance or underperformance relative to a benchmark.
- This lecture focuses on:
  - **Yield-Curve Carry and Change**: Decomposing yield-curve contributions into carry and reshaping effects.
  - **[Implied Volatility](../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%205%20Options%20on%20Prices%20and%20Hedge-Based%20Valuation/A%20Real-Life%20Option%20Pricing%20Exercise.md) Attribution**: Breaking down volatility contributions into decay,  parallel shifts,  and surface reshaping.
  - Practical examples using the Barclays HPA model to illustrate these concepts.

## 2. Yield-Curve Attribution

### 2.1 Yield-Curve Carry Attribution

#### 2.1.1 Overview of Yield-Curve Carry
- **Definition**: Yield-curve carry measures the return from holding a security as it rolls down the yield curve,  assuming no changes in [interest rates](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%202/Interest%20Rate%20Quotations.md).
- **Key Components**:
  - **Average Carry**: The difference in average yields between the [portfolio](../../Advanced%20Investments/An%20Asset%20Allocation%20Primer.md) and the benchmark.
  - **Key-Rate Contributions**: The excess carry at specific key-rate points relative to the average carry.

#### 2.1.2 Curve Matching Portfolio (CMP) Method
- **Purpose**: Simplifies yield-curve carry calculations by constructing a [portfolio](../../Advanced%20Investments/An%20Asset%20Allocation%20Primer.md) of reference bonds (par or zero-coupon) that matches the cash-flow profile of the security.
- **Steps**:
  1. Match the key-rate durations of the [portfolio](../../Advanced%20Investments/An%20Asset%20Allocation%20Primer.md) and benchmark using reference bonds.
  1. Adjust for cash to ensure the present value of the matching [portfolio](../../Advanced%20Investments/An%20Asset%20Allocation%20Primer.md) equals the security's price.
  1. Calculate carry contributions using the yields of the reference bonds.

#### 2.1.3 Example: Yield-Curve Carry Attribution
- **[Portfolio](../../Advanced%20Investments/An%20Asset%20Allocation%20Primer.md) Average Yield**: 2.030%.
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
- **Definition**: Yield-curve change measures the impact of interest rate movements on [portfolio](../../Advanced%20Investments/An%20Asset%20Allocation%20Primer.md) [returns](../../Financial%20Markets/Financial%20Asset%20Pricing%20Theory%20Overview/Chapter%203%20-%20%20Assets,%20Portfolios,%20and%20Arbitrage/Assets.md),  including parallel shifts,  reshaping,  and [convexity](../Problem%20Sets/PSET%20II%20Fixed%20Income%20Asset%20Pricing%201.md) effects.
- **Key Components**:
  - **Parallel Shift**: The average change in yields across the curve.
  - **Reshaping**: Changes in the relative levels of key-rate points.
  - **[Convexity](../Problem%20Sets/PSET%20II%20Fixed%20Income%20Asset%20Pricing%201.md) and Higher-Order Terms**: Residual effects not captured by key-rate durations.

#### 2.2.2 Example: Yield-Curve Change Attribution
- **[Portfolio](../../Advanced%20Investments/An%20Asset%20Allocation%20Primer.md) OAD**: 6.7 years.
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
- **[Convexity](../Problem%20Sets/PSET%20II%20Fixed%20Income%20Asset%20Pricing%201.md) and Residual**: +8.3 bp.
- **Total Change**: +74.4 bp.

## 3. Implied Volatility Attribution

### 3.1 Components of Implied Volatility Attribution

#### 3.1.1 Volatility Decay
- **Definition**: Measures the change in option value due to the passage of time,  assuming no changes in [implied volatility](../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%205%20Options%20on%20Prices%20and%20Hedge-Based%20Valuation/A%20Real-Life%20Option%20Pricing%20Exercise.md).
- **Calculation**:
  - Subtract all other components of the total time return (e.g.,  yield-curve carry,  spread carry).
  - **Example**:
	$$\text{Volatility Decay Return} = \text{Total Time Return} - (\text{Yield-Curve Carry} + \text{Spread Carry})$$

#### 3.1.2 Parallel Shift of Implied Volatility Surface
- **Definition**: Measures the impact of a uniform change in [implied volatility](../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%205%20Options%20on%20Prices%20and%20Hedge-Based%20Valuation/A%20Real-Life%20Option%20Pricing%20Exercise.md) across all maturities and strikes.
- **Calculation**:
 $\text{Parallel Shift Return} = \text{Vega} \times \Delta \text{Volatility}$$
  - **Example**:
	- Vega: 0.5.
	- Parallel Shift: +2%.
	- Return: $$0.5 \times 2 = +1.0 \,    \text{bp}$$

#### 3.1.3 Surface Reshaping
- **Definition**: Measures the impact of non-parallel changes in the [implied volatility surface](../../Course%20Notes/Python/QuantLib-Python/Modeling%20Volatility%20Smile%20and%20Heston%20Model%20Calibration%20Using%20QuantLib%20Python.md).
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
  - Align [duration](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%205/Key%20Rates%20O1s%20Durations%20and%20Hedging.md) and key-rate exposures with expected yield-curve movements to maximize carry and minimize adverse [rate changes](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%207/Profit%20and%20Loss%20Attribution%20with%20an%20OAS.md).
  - Use the CMP method to simplify carry calculations and improve attribution accuracy.

### 4.2 Implied Volatility Management
- **Key Takeaways**:
  - Monitor Vega exposures to manage sensitivity to parallel shifts in [implied volatility](../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%205%20Options%20on%20Prices%20and%20Hedge-Based%20Valuation/A%20Real-Life%20Option%20Pricing%20Exercise.md).
  - Analyze surface reshaping effects to identify opportunities for outperformance in securities with optionality.

### 4.3 Enhancing Attribution Models
- **Recommendations**:
  - Incorporate [implied volatility](../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%205%20Options%20on%20Prices%20and%20Hedge-Based%20Valuation/A%20Real-Life%20Option%20Pricing%20Exercise.md) into attribution models to capture its contribution to outperformance.
  - Use scenario-based and analytics-based methods to decompose [returns](../../Financial%20Markets/Financial%20Asset%20Pricing%20Theory%20Overview/Chapter%203%20-%20%20Assets,%20Portfolios,%20and%20Arbitrage/Assets.md) into detailed components.

## 5. Summary and Key Takeaways

### 5.1 Yield-Curve Attribution
- Yield-curve carry and change are significant drivers of fixed-income [portfolio](../../Advanced%20Investments/An%20Asset%20Allocation%20Primer.md) performance.
- The CMP method simplifies carry calculations,  while key-rate durations provide a detailed breakdown of yield-curve change contributions.

### 5.2 Implied Volatility Attribution
- [Implied volatility](../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%205%20Options%20on%20Prices%20and%20Hedge-Based%20Valuation/A%20Real-Life%20Option%20Pricing%20Exercise.md) contributions include decay,  parallel shifts,  and surface reshaping.
- Proper attribution of volatility effects enhances the understanding of performance drivers in securities with optionality.

### 5.3 Practical Applications
- Advanced attribution techniques provide deeper insights into [portfolio](../../Advanced%20Investments/An%20Asset%20Allocation%20Primer.md) performance,  enabling managers to optimize risk-adjusted [returns](../../Financial%20Markets/Financial%20Asset%20Pricing%20Theory%20Overview/Chapter%203%20-%20%20Assets,%20Portfolios,%20and%20Arbitrage/Assets.md) and refine [investment](../../Advanced%20Investments/An%20Asset%20Allocation%20Primer.md) strategies.

By mastering these advanced attribution methodologies,  fixed-income [portfolio](../../Advanced%20Investments/An%20Asset%20Allocation%20Primer.md) managers can enhance their decision-making processes and achieve superior performance outcomes.

# Lecture Notes: Advanced Performance Attribution in Fixed Income Portfolio Management – Implied Volatility,  Spread,  and Mortgage Factors

## 1. Introduction to Advanced Attribution Components

- Advanced performance attribution in [fixed income](../Lecture%20Notes%20Bonds,%20%20Preferred%20Stock,%20%20and%20Structured%20Products.md) portfolios involves decomposing [returns](../../Financial%20Markets/Financial%20Asset%20Pricing%20Theory%20Overview/Chapter%203%20-%20%20Assets,%20Portfolios,%20and%20Arbitrage/Assets.md) into contributions from [implied volatility](../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%205%20Options%20on%20Prices%20and%20Hedge-Based%20Valuation/A%20Real-Life%20Option%20Pricing%20Exercise.md),  spread changes,  and mortgage-specific factors.
- This lecture focuses on:
  - **[Implied Volatility](../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%205%20Options%20on%20Prices%20and%20Hedge-Based%20Valuation/A%20Real-Life%20Option%20Pricing%20Exercise.md) Attribution**: Contributions from parallel shifts,  surface reshaping,  and volatility decay.
  - **Spread Attribution**: Top-level and sector-level models for spread carry,  [spread duration](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%2014/Spread%20Duration%20and%20Dvo1.md),  and spread [convexity](../Problem%20Sets/PSET%20II%20Fixed%20Income%20Asset%20Pricing%201.md).
  - **Mortgage Factors**: Prepayment surprises,  mortgage spread changes,  and other mortgage-specific factors.

## 2. Implied Volatility Attribution

### 2.1 Overview of Implied Volatility Attribution

- **[Implied Volatility](../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%205%20Options%20on%20Prices%20and%20Hedge-Based%20Valuation/A%20Real-Life%20Option%20Pricing%20Exercise.md) Exposure**:
  - Bonds with embedded options,  such as callable [Corporate Bonds](../../Financial%20Markets%20and%20Institutions/II.%20The%20Roles%20of%20Banks%20and%20Derivative%20Markets%20in%20Resolving%20Problems%20Inherent%20in%20Debt%20Contracts/Class%202-%20Debt%20Contracts%20due%20to%20Lack%20of%20Information/Class%20Notes%202%20–%20Corporate%20Bond%20Contracts.md) and [mortgage-backed securities](../../Financial%20Markets%20and%20Institutions/III.%20Liquidity%20of%20Assets/Class%207-%20CP,%20Repo,%20and%20the%20Crisis/Fremont%20Financial%20Corp.%20(b).md) (MBS),  have exposure to [implied volatility](../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%205%20Options%20on%20Prices%20and%20Hedge-Based%20Valuation/A%20Real-Life%20Option%20Pricing%20Exercise.md).
  - Issuers of such bonds are long volatility,  while holders are short volatility,  as indicated by negative exposure numbers.
- **[Portfolio](../../Advanced%20Investments/An%20Asset%20Allocation%20Primer.md) Positioning**:
  - The [portfolio](../../Advanced%20Investments/An%20Asset%20Allocation%20Primer.md) is **long volatility** overall,  with a larger exposure to the securitized sector compared to the corporate and government-related sectors.
  - During the attribution period,  implied volatilities increased by **5.71%**,  leading to:
	- **Corporate Sector**: Negative contribution of **-0.6 bp** due to underweight [volatility exposure](../../Financial%20Instruments/Financial%20Derivatives%20and%20Quantitative%20Methods/JP%20Morgan-Variance%20Swaps.md).
	- **Securitized Sector**: Positive contribution of **+6.6 bp** due to overweight [volatility exposure](../../Financial%20Instruments/Financial%20Derivatives%20and%20Quantitative%20Methods/JP%20Morgan-Variance%20Swaps.md).
- **Total Contribution**:
  - Parallel volatility change contributed **+6.2 bp**.
  - Surface reshaping contributed **-3.8 bp**.
  - Volatility decay contributed **-0.5 bp**.
  - **Net Contribution**: **+1.9 bp**.

### 2.2 Key Components of Implied Volatility Attribution

#### 2.2.1 Parallel Volatility Shift
- **Definition**: Measures the impact of a uniform change in [implied volatility](../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%205%20Options%20on%20Prices%20and%20Hedge-Based%20Valuation/A%20Real-Life%20Option%20Pricing%20Exercise.md) across all maturities and strikes.
- **Example**:
  - Corporate sector: **-0.6 bp**.
  - Securitized sector: **+6.6 bp**.
  - **Total Contribution**: **+6.2 bp**.

#### 2.2.2 Surface Reshaping
- **Definition**: Measures the impact of non-parallel changes in the [implied volatility surface](../../Course%20Notes/Python/QuantLib-Python/Modeling%20Volatility%20Smile%20and%20Heston%20Model%20Calibration%20Using%20QuantLib%20Python.md).
- **Contribution**: **-3.8 bp**.

#### 2.2.3 Volatility Decay
- **Definition**: Measures the loss of return due to the passage of time,  which reduces the value of optionality.
- **Contribution**: **-0.5 bp**.

### 2.3 Implications for Portfolio Management

- **Volatility Positioning**:
  - The [portfolio](../../Advanced%20Investments/An%20Asset%20Allocation%20Primer.md)'s overweight in the securitized sector resulted in a net long volatility position,  which benefited from rising implied volatilities.
  - Managers should monitor sector-level volatility exposures to optimize contributions from parallel shifts and surface reshaping.

## 3. Spread Attribution

### 3.1 Overview of Spread Attribution

- Spread attribution decomposes outperformance into:
  - **Spread Carry**: Return from holding securities with positive spreads.
  - **[Spread Duration](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%2014/Spread%20Duration%20and%20Dvo1.md)**: Return from [changes in spreads](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%203/Pl%20Attribution.md),  weighted by [spread duration](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%2014/Spread%20Duration%20and%20Dvo1.md).
  - **Spread [Convexity](../Problem%20Sets/PSET%20II%20Fixed%20Income%20Asset%20Pricing%201.md)**: Second-order sensitivity to spread changes.

### 3.2 Top-Level Spread Model

- **Assumptions**:
  - [Spread duration](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%2014/Spread%20Duration%20and%20Dvo1.md) decisions are made at the [portfolio](../../Advanced%20Investments/An%20Asset%20Allocation%20Primer.md) level.
  - Subsequent sector allocations are relative to the [portfolio](../../Advanced%20Investments/An%20Asset%20Allocation%20Primer.md) [spread duration](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%2014/Spread%20Duration%20and%20Dvo1.md).

#### 3.2.1 Key Formulas
- **[Asset Allocation](Lecture%202-%20[[Lecture%202-%20Asset%20Allocation%20with%20Multiple%20Risky%20Assets) with [Multiple Risky Assets](../../Advanced%20Investments/Lecture%202-%20Asset%20Allocation%20with%20Multiple%20Risky%20Assets.md)|[asset allocation](../../Advanced%20Investments/Lecture%202-%20Asset%20Allocation%20with%20Multiple%20Risky%20Assets.md)]]**:
 $\text{Asset Allocation} = -OASD^{P} \cdot \sum_{s} \left(\frac{w_{s}^{P} OASD_{s}^{P}}{OASD^{P}} - \frac{w_{s}^{B} OASD_{s}^{B}}{OASD^{B}}\right) \cdot \left(\Delta OAS_{s}^{B} - \Delta OAS^{B}\right)$$
- **Security Selection**:
 $\text{Security Selection} = -\sum_{s} w_{s}^{P} OASD_{s}^{P} \cdot \left(\Delta OAS_{s}^{P} - \Delta OAS_{s}^{B}\right)$$
- **[Spread Duration](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%2014/Spread%20Duration%20and%20Dvo1.md) Mismatch**:
 $\text{Spread Duration Mismatch} = -(OASD^{P} - OASD^{B}) \cdot \Delta OAS^{B}$$

#### 3.2.2 Example
- **[Spread Duration](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%2014/Spread%20Duration%20and%20Dvo1.md) Mismatch**:
  - [Portfolio](../../Advanced%20Investments/An%20Asset%20Allocation%20Primer.md) [spread duration](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%2014/Spread%20Duration%20and%20Dvo1.md): **4.7 years**.
  - Benchmark [spread duration](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%2014/Spread%20Duration%20and%20Dvo1.md): **4.5 years**.
  - Benchmark [spread change](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%207/Profit%20and%20Loss%20Attribution%20with%20an%20OAS.md): **+8.3 bp**.
  - Contribution:
	$$+0.2 \cdot (-8.3) = -1.7 \,    \text{bp}$$

### 3.3 Sector-Level Spread Model

- **Assumptions**:
  - [Spread duration](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%2014/Spread%20Duration%20and%20Dvo1.md) decisions are made independently for each sector.
  - Absolute allocation weights are used,  and the hurdle rate is set to zero.

#### 3.3.1 Key Formulas
- **[Asset Allocation](Lecture%202-%20[[Lecture%202-%20Asset%20Allocation%20with%20Multiple%20Risky%20Assets) with [Multiple Risky Assets](../../Advanced%20Investments/Lecture%202-%20Asset%20Allocation%20with%20Multiple%20Risky%20Assets.md)|[asset allocation](../../Advanced%20Investments/Lecture%202-%20Asset%20Allocation%20with%20Multiple%20Risky%20Assets.md)]]**:
 $\text{Asset Allocation} = -\sum_{s} \left(w_{s}^{P} OASD_{s}^{P} - w_{s}^{B} OASD_{s}^{B}\right) \cdot \Delta OAS_{s}^{B}$$
- **Security Selection**:
 $\text{Security Selection} = -\sum_{s} w_{s}^{P} OASD_{s}^{P} \cdot \left(\Delta OAS_{s}^{P} - \Delta OAS_{s}^{B}\right)$$

#### 3.3.2 Example
- **Securitized Sector**:
  - [Spread duration](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%2014/Spread%20Duration%20and%20Dvo1.md) underweight: **-0.3 years**.
  - Benchmark [spread change](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%207/Profit%20and%20Loss%20Attribution%20with%20an%20OAS.md): **+15.9 bp**.
  - Contribution:
	$$-0.3 \cdot (-15.9) = +4.8 \,    \text{bp}$$

### 3.4 Comparison of Models

| **Component** | **Top-Level Model (bp)** | **Sector-Level Model (bp)** |

| **[Asset Allocation](../../Advanced%20Investments/Lecture%202-%20Asset%20Allocation%20with%20Multiple%20Risky%20Assets.md)** | **+5.0** | **+3.2** |

| **Security Selection** | **+9.3** | **+9.3** |

| **[Spread Duration](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%2014/Spread%20Duration%20and%20Dvo1.md) Mismatch** | **-1.8** | N/A |

## 4. Mortgage Factors

### 4.1 Prepayment Surprise

- **Definition**: Measures the difference between actual and model-predicted [prepayment rates](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%2015/Mortgage%20Pools.md).
- **Example**:
  - Predicted prepayment rate: **25% CPR**.
  - Actual prepayment rate: **15% CPR**.
  - Contribution: **+5.2 bp**.

### 4.2 Mortgage Spread Change

- **Definition**: Measures the impact of changes in the difference between model-implied and market-observed mortgage rates.
- **Formula**:
 $\text{Mortgage Spread Change Return} = \text{MtgRtDur} \cdot \Delta \text{MtgSpread}$$

### 4.3 Other Mortgage Factors

- **Definition**: Captures [returns](../../Financial%20Markets/Financial%20Asset%20Pricing%20Theory%20Overview/Chapter%203%20-%20%20Assets,%20Portfolios,%20and%20Arbitrage/Assets.md) from factors not explicitly modeled,  such as home price appreciation projections and swap spreads.
- **Example**:
  - Residual contribution: **+1.4 bp**.

### 4.4 Example: Securitized Sector Attribution (Exhibit 71-14)

| **Component** | **Spread Carry (bp)** | **[Spread Change](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%207/Profit%20and%20Loss%20Attribution%20with%20an%20OAS.md) (bp)** | **Prepayments (bp)** | **Mortgage Spread (bp)** | **Residual (bp)** | **Total (bp)** |

| **Securitized** | **+0.3** | **+3.7** | **-1.2** | **-7.0** | **+1.4** | **-2.7** |

## 5. Summary and Key Takeaways

### 5.1 Implied Volatility Attribution
- Parallel shifts contributed **+6.2 bp**,  while surface reshaping and volatility decay detracted **-3.8 bp** and **-0.5 bp**,  respectively.
- Net contribution: **+1.9 bp**.

### 5.2 Spread Attribution
- The top-level model separates [spread duration](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%2014/Spread%20Duration%20and%20Dvo1.md) mismatch (**-1.8 bp**) from [Asset Allocation](Lecture%202-%20[[Lecture%202-%20Asset%20Allocation%20with%20Multiple%20Risky%20Assets) with [Multiple Risky Assets](../../Advanced%20Investments/Lecture%202-%20Asset%20Allocation%20with%20Multiple%20Risky%20Assets.md)|[asset allocation](../../Advanced%20Investments/Lecture%202-%20Asset%20Allocation%20with%20Multiple%20Risky%20Assets.md)]] (**+5.0 bp**),  while the sector-level model combines these terms into [Asset Allocation](Lecture%202-%20[[Lecture%202-%20Asset%20Allocation%20with%20Multiple%20Risky%20Assets) with [Multiple Risky Assets](../../Advanced%20Investments/Lecture%202-%20Asset%20Allocation%20with%20Multiple%20Risky%20Assets.md)|[asset allocation](../../Advanced%20Investments/Lecture%202-%20Asset%20Allocation%20with%20Multiple%20Risky%20Assets.md)]] (**+3.2 bp**).

### 5.3 Mortgage Factors
- Prepayment surprises and mortgage spread changes are significant drivers of performance in the securitized sector.
- Residuals indicate areas where additional analytics may be required.

By mastering these advanced attribution techniques,  [fixed income](../Lecture%20Notes%20Bonds,%20%20Preferred%20Stock,%20%20and%20Structured%20Products.md) [portfolio](../../Advanced%20Investments/An%20Asset%20Allocation%20Primer.md) managers can optimize risk-adjusted [returns](../../Financial%20Markets/Financial%20Asset%20Pricing%20Theory%20Overview/Chapter%203%20-%20%20Assets,%20Portfolios,%20and%20Arbitrage/Assets.md) and enhance their understanding of performance drivers.

# Lecture Notes: Advanced Attribution for Inflation-Linked Securities and Model Selection

## 1. Introduction to Inflation-Linked Securities Attribution

- [Inflation](../../International%20Finance/Bridgewater/Principles%20For%20Navigating%20Big%20Debt%20Cycles/Part%20II%20Detailed%20Case%20Studies/German%20Debt%20Crisis%20andHyperinflation%20(1918–1924)/War%20Economies%20and%20Hyperinflation.md)-linked securities,  such as U.S. Treasury [Inflation](../../International%20Finance/Bridgewater/Principles%20For%20Navigating%20Big%20Debt%20Cycles/Part%20II%20Detailed%20Case%20Studies/German%20Debt%20Crisis%20andHyperinflation%20(1918–1924)/War%20Economies%20and%20Hyperinflation.md)-Protected Securities (TIPS),  require specialized attribution models to account for their unique return components.
- This lecture focuses on:
  - The decomposition of [returns](../../Financial%20Markets/Financial%20Asset%20Pricing%20Theory%20Overview/Chapter%203%20-%20%20Assets,%20Portfolios,%20and%20Arbitrage/Assets.md) for [inflation](../../International%20Finance/Bridgewater/Principles%20For%20Navigating%20Big%20Debt%20Cycles/Part%20II%20Detailed%20Case%20Studies/German%20Debt%20Crisis%20andHyperinflation%20(1918–1924)/War%20Economies%20and%20Hyperinflation.md)-linked securities into nominal [interest rate exposure](../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20III%20THE%20PLAYERS/Chapter%2013%20-%20Banks%20Asset-Liability%20Management/Duration%20Gap%20Management.md),  [inflation](../../International%20Finance/Bridgewater/Principles%20For%20Navigating%20Big%20Debt%20Cycles/Part%20II%20Detailed%20Case%20Studies/German%20Debt%20Crisis%20andHyperinflation%20(1918–1924)/War%20Economies%20and%20Hyperinflation.md)-related components,  and residuals.
  - The importance of [inflation](../../International%20Finance/Bridgewater/Principles%20For%20Navigating%20Big%20Debt%20Cycles/Part%20II%20Detailed%20Case%20Studies/German%20Debt%20Crisis%20andHyperinflation%20(1918–1924)/War%20Economies%20and%20Hyperinflation.md) spread,  [inflation](../../International%20Finance/Bridgewater/Principles%20For%20Navigating%20Big%20Debt%20Cycles/Part%20II%20Detailed%20Case%20Studies/German%20Debt%20Crisis%20andHyperinflation%20(1918–1924)/War%20Economies%20and%20Hyperinflation.md) accretion,  and [inflation](../../International%20Finance/Bridgewater/Principles%20For%20Navigating%20Big%20Debt%20Cycles/Part%20II%20Detailed%20Case%20Studies/German%20Debt%20Crisis%20andHyperinflation%20(1918–1924)/War%20Economies%20and%20Hyperinflation.md) surprise in explaining [returns](../../Financial%20Markets/Financial%20Asset%20Pricing%20Theory%20Overview/Chapter%203%20-%20%20Assets,%20Portfolios,%20and%20Arbitrage/Assets.md).
  - A comparison of attribution models for fixed-income portfolios,  highlighting the Fully Analytical model.

## 2. Return Decomposition for Inflation-Linked Securities

### 2.1 Key Components of Inflation-Linked Returns

1. **Nominal [Interest Rate Exposure](../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20III%20THE%20PLAYERS/Chapter%2013%20-%20Banks%20Asset-Liability%20Management/Duration%20Gap%20Management.md)**:
   - **Yield-Curve Carry**: Return from rolling down the nominal yield curve.
   - **Yield-Curve Change**: Return from changes in [nominal interest rates](../../Financial%20Markets/Financial%20Asset%20Pricing%20Theory%20Overview/Chapter%2010%20-%20The%20Economics%20of%20the%20Term%20Structure%20of%20Interest%20Rates/Real%20and%20Nominal%20Interest%20Rates%20and%20Term%20Struc.md).

1. **[Inflation](../../International%20Finance/Bridgewater/Principles%20For%20Navigating%20Big%20Debt%20Cycles/Part%20II%20Detailed%20Case%20Studies/German%20Debt%20Crisis%20andHyperinflation%20(1918–1924)/War%20Economies%20and%20Hyperinflation.md)-Related Components**:
   - **[Inflation](../../International%20Finance/Bridgewater/Principles%20For%20Navigating%20Big%20Debt%20Cycles/Part%20II%20Detailed%20Case%20Studies/German%20Debt%20Crisis%20andHyperinflation%20(1918–1924)/War%20Economies%20and%20Hyperinflation.md) Accretion**: Return from realized [inflation](../../International%20Finance/Bridgewater/Principles%20For%20Navigating%20Big%20Debt%20Cycles/Part%20II%20Detailed%20Case%20Studies/German%20Debt%20Crisis%20andHyperinflation%20(1918–1924)/War%20Economies%20and%20Hyperinflation.md),  reflecting the adjustment of principal or [coupon payments](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%203/Realized%20Returns.md).
   - **[Inflation](../../International%20Finance/Bridgewater/Principles%20For%20Navigating%20Big%20Debt%20Cycles/Part%20II%20Detailed%20Case%20Studies/German%20Debt%20Crisis%20andHyperinflation%20(1918–1924)/War%20Economies%20and%20Hyperinflation.md) Spread Carry**: Return from the difference between nominal rates and [inflation](../../International%20Finance/Bridgewater/Principles%20For%20Navigating%20Big%20Debt%20Cycles/Part%20II%20Detailed%20Case%20Studies/German%20Debt%20Crisis%20andHyperinflation%20(1918–1924)/War%20Economies%20and%20Hyperinflation.md) [expectations](../Fixed%20Income%20Lecture%20Notes/FORWARD%20RATES%20AND%20TERM%20STRUCTURE.md).
   - **[Inflation](../../International%20Finance/Bridgewater/Principles%20For%20Navigating%20Big%20Debt%20Cycles/Part%20II%20Detailed%20Case%20Studies/German%20Debt%20Crisis%20andHyperinflation%20(1918–1924)/War%20Economies%20and%20Hyperinflation.md) Surprise**: Return from differences between realized and projected [inflation](../../International%20Finance/Bridgewater/Principles%20For%20Navigating%20Big%20Debt%20Cycles/Part%20II%20Detailed%20Case%20Studies/German%20Debt%20Crisis%20andHyperinflation%20(1918–1924)/War%20Economies%20and%20Hyperinflation.md).
   - **[Inflation](../../International%20Finance/Bridgewater/Principles%20For%20Navigating%20Big%20Debt%20Cycles/Part%20II%20Detailed%20Case%20Studies/German%20Debt%20Crisis%20andHyperinflation%20(1918–1924)/War%20Economies%20and%20Hyperinflation.md) [Spread Change](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%207/Profit%20and%20Loss%20Attribution%20with%20an%20OAS.md)**: Return from changes in [inflation](../../International%20Finance/Bridgewater/Principles%20For%20Navigating%20Big%20Debt%20Cycles/Part%20II%20Detailed%20Case%20Studies/German%20Debt%20Crisis%20andHyperinflation%20(1918–1924)/War%20Economies%20and%20Hyperinflation.md) [expectations](../Fixed%20Income%20Lecture%20Notes/FORWARD%20RATES%20AND%20TERM%20STRUCTURE.md).

1. **Residual**:
   - Captures unexplained differences between actual and modeled [returns](../../Financial%20Markets/Financial%20Asset%20Pricing%20Theory%20Overview/Chapter%203%20-%20%20Assets,%20Portfolios,%20and%20Arbitrage/Assets.md).

### 2.2 Example: Barclays Inflation-Linked U.S. TIPS Index (July 16,  2010 – August 13,  2010)

- **Total Return**: +169.9 bp.
- **Nominal [Interest Rate Exposure](../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20III%20THE%20PLAYERS/Chapter%2013%20-%20Banks%20Asset-Liability%20Management/Duration%20Gap%20Management.md)**:
  - Yield-Curve Carry: +27.7 bp.
  - Yield-Curve Change: +184.6 bp.
- **[Inflation](../../International%20Finance/Bridgewater/Principles%20For%20Navigating%20Big%20Debt%20Cycles/Part%20II%20Detailed%20Case%20Studies/German%20Debt%20Crisis%20andHyperinflation%20(1918–1924)/War%20Economies%20and%20Hyperinflation.md)-Related Components**:
  - [Inflation](../../International%20Finance/Bridgewater/Principles%20For%20Navigating%20Big%20Debt%20Cycles/Part%20II%20Detailed%20Case%20Studies/German%20Debt%20Crisis%20andHyperinflation%20(1918–1924)/War%20Economies%20and%20Hyperinflation.md) Accretion: -3.0 bp.
  - [Inflation](../../International%20Finance/Bridgewater/Principles%20For%20Navigating%20Big%20Debt%20Cycles/Part%20II%20Detailed%20Case%20Studies/German%20Debt%20Crisis%20andHyperinflation%20(1918–1924)/War%20Economies%20and%20Hyperinflation.md) Spread Carry: -13.1 bp.
  - [Inflation](../../International%20Finance/Bridgewater/Principles%20For%20Navigating%20Big%20Debt%20Cycles/Part%20II%20Detailed%20Case%20Studies/German%20Debt%20Crisis%20andHyperinflation%20(1918–1924)/War%20Economies%20and%20Hyperinflation.md) Surprise: +5.3 bp.
  - [Inflation](../../International%20Finance/Bridgewater/Principles%20For%20Navigating%20Big%20Debt%20Cycles/Part%20II%20Detailed%20Case%20Studies/German%20Debt%20Crisis%20andHyperinflation%20(1918–1924)/War%20Economies%20and%20Hyperinflation.md) [Spread Change](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%207/Profit%20and%20Loss%20Attribution%20with%20an%20OAS.md): -29.7 bp.
- **Residual**: -1.9 bp.

#### Observations
1. **Nominal [Interest Rate Exposure](../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20III%20THE%20PLAYERS/Chapter%2013%20-%20Banks%20Asset-Liability%20Management/Duration%20Gap%20Management.md)**:
   - The majority of the return came from nominal [interest rate exposure](../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20III%20THE%20PLAYERS/Chapter%2013%20-%20Banks%20Asset-Liability%20Management/Duration%20Gap%20Management.md),  with yield-curve change contributing +184.6 bp.
1. **[Inflation](../../International%20Finance/Bridgewater/Principles%20For%20Navigating%20Big%20Debt%20Cycles/Part%20II%20Detailed%20Case%20Studies/German%20Debt%20Crisis%20andHyperinflation%20(1918–1924)/War%20Economies%20and%20Hyperinflation.md)-Related Components**:
   - [Inflation](../../International%20Finance/Bridgewater/Principles%20For%20Navigating%20Big%20Debt%20Cycles/Part%20II%20Detailed%20Case%20Studies/German%20Debt%20Crisis%20andHyperinflation%20(1918–1924)/War%20Economies%20and%20Hyperinflation.md)-related [returns](../../Financial%20Markets/Financial%20Asset%20Pricing%20Theory%20Overview/Chapter%203%20-%20%20Assets,%20Portfolios,%20and%20Arbitrage/Assets.md) were negative overall (-40.6 bp),  driven by falling [inflation](../../International%20Finance/Bridgewater/Principles%20For%20Navigating%20Big%20Debt%20Cycles/Part%20II%20Detailed%20Case%20Studies/German%20Debt%20Crisis%20andHyperinflation%20(1918–1924)/War%20Economies%20and%20Hyperinflation.md) [expectations](../Fixed%20Income%20Lecture%20Notes/FORWARD%20RATES%20AND%20TERM%20STRUCTURE.md) (-29.7 bp).
   - [Inflation](../../International%20Finance/Bridgewater/Principles%20For%20Navigating%20Big%20Debt%20Cycles/Part%20II%20Detailed%20Case%20Studies/German%20Debt%20Crisis%20andHyperinflation%20(1918–1924)/War%20Economies%20and%20Hyperinflation.md) accretion (-3.0 bp) reflected [market expectations](../../Clippings/Forward%20Rate.md) of slight deflation at the beginning of the month.
   - [Inflation](../../International%20Finance/Bridgewater/Principles%20For%20Navigating%20Big%20Debt%20Cycles/Part%20II%20Detailed%20Case%20Studies/German%20Debt%20Crisis%20andHyperinflation%20(1918–1924)/War%20Economies%20and%20Hyperinflation.md) surprise (+5.3 bp) indicated that realized [inflation](../../International%20Finance/Bridgewater/Principles%20For%20Navigating%20Big%20Debt%20Cycles/Part%20II%20Detailed%20Case%20Studies/German%20Debt%20Crisis%20andHyperinflation%20(1918–1924)/War%20Economies%20and%20Hyperinflation.md) was slightly positive,  contrary to [expectations](../Fixed%20Income%20Lecture%20Notes/FORWARD%20RATES%20AND%20TERM%20STRUCTURE.md).

### 2.3 Inflation Spread and Term Structure

- [Inflation](../../International%20Finance/Bridgewater/Principles%20For%20Navigating%20Big%20Debt%20Cycles/Part%20II%20Detailed%20Case%20Studies/German%20Debt%20Crisis%20andHyperinflation%20(1918–1924)/War%20Economies%20and%20Hyperinflation.md) [expectations](../Fixed%20Income%20Lecture%20Notes/FORWARD%20RATES%20AND%20TERM%20STRUCTURE.md) did not fall uniformly across maturities:
  - **Short Bonds**: Positive [inflation](../../International%20Finance/Bridgewater/Principles%20For%20Navigating%20Big%20Debt%20Cycles/Part%20II%20Detailed%20Case%20Studies/German%20Debt%20Crisis%20andHyperinflation%20(1918–1924)/War%20Economies%20and%20Hyperinflation.md) spread return,  indicating rising short-term [inflation](../../International%20Finance/Bridgewater/Principles%20For%20Navigating%20Big%20Debt%20Cycles/Part%20II%20Detailed%20Case%20Studies/German%20Debt%20Crisis%20andHyperinflation%20(1918–1924)/War%20Economies%20and%20Hyperinflation.md) [expectations](../Fixed%20Income%20Lecture%20Notes/FORWARD%20RATES%20AND%20TERM%20STRUCTURE.md).
  - **Long Bonds (30-Year)**: Positive [inflation](../../International%20Finance/Bridgewater/Principles%20For%20Navigating%20Big%20Debt%20Cycles/Part%20II%20Detailed%20Case%20Studies/German%20Debt%20Crisis%20andHyperinflation%20(1918–1924)/War%20Economies%20and%20Hyperinflation.md) spread return,  indicating rising long-term [inflation](../../International%20Finance/Bridgewater/Principles%20For%20Navigating%20Big%20Debt%20Cycles/Part%20II%20Detailed%20Case%20Studies/German%20Debt%20Crisis%20andHyperinflation%20(1918–1924)/War%20Economies%20and%20Hyperinflation.md) [expectations](../Fixed%20Income%20Lecture%20Notes/FORWARD%20RATES%20AND%20TERM%20STRUCTURE.md).
  - **Intermediate Bonds (3.5–20 Years)**: Negative [inflation](../../International%20Finance/Bridgewater/Principles%20For%20Navigating%20Big%20Debt%20Cycles/Part%20II%20Detailed%20Case%20Studies/German%20Debt%20Crisis%20andHyperinflation%20(1918–1924)/War%20Economies%20and%20Hyperinflation.md) spread return,  indicating falling [inflation](../../International%20Finance/Bridgewater/Principles%20For%20Navigating%20Big%20Debt%20Cycles/Part%20II%20Detailed%20Case%20Studies/German%20Debt%20Crisis%20andHyperinflation%20(1918–1924)/War%20Economies%20and%20Hyperinflation.md) [expectations](../Fixed%20Income%20Lecture%20Notes/FORWARD%20RATES%20AND%20TERM%20STRUCTURE.md).

#### Implications
- [Inflation](../../International%20Finance/Bridgewater/Principles%20For%20Navigating%20Big%20Debt%20Cycles/Part%20II%20Detailed%20Case%20Studies/German%20Debt%20Crisis%20andHyperinflation%20(1918–1924)/War%20Economies%20and%20Hyperinflation.md) [portfolio](../../Advanced%20Investments/An%20Asset%20Allocation%20Primer.md) managers must carefully monitor the [term structure](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%209/The%20Vasicek%20Model.md) of [inflation](../../International%20Finance/Bridgewater/Principles%20For%20Navigating%20Big%20Debt%20Cycles/Part%20II%20Detailed%20Case%20Studies/German%20Debt%20Crisis%20andHyperinflation%20(1918–1924)/War%20Economies%20and%20Hyperinflation.md) [expectations](../Fixed%20Income%20Lecture%20Notes/FORWARD%20RATES%20AND%20TERM%20STRUCTURE.md) and use detailed analytics to manage partial sensitivities to [inflation](../../International%20Finance/Bridgewater/Principles%20For%20Navigating%20Big%20Debt%20Cycles/Part%20II%20Detailed%20Case%20Studies/German%20Debt%20Crisis%20andHyperinflation%20(1918–1924)/War%20Economies%20and%20Hyperinflation.md).

## 3. Security-Level Return Splits for Inflation-Linked Securities

### 3.1 Example: Security-Level Attribution (Exhibit 71-15)

| **Bucket/Issue** | **Maturity** | **Yield-Curve Carry (bp)** | **Yield-Curve Change (bp)** | **[Inflation](../../International%20Finance/Bridgewater/Principles%20For%20Navigating%20Big%20Debt%20Cycles/Part%20II%20Detailed%20Case%20Studies/German%20Debt%20Crisis%20andHyperinflation%20(1918–1924)/War%20Economies%20and%20Hyperinflation.md) Accretion (bp)** | **[Inflation](../../International%20Finance/Bridgewater/Principles%20For%20Navigating%20Big%20Debt%20Cycles/Part%20II%20Detailed%20Case%20Studies/German%20Debt%20Crisis%20andHyperinflation%20(1918–1924)/War%20Economies%20and%20Hyperinflation.md) Spread Carry (bp)** | **[Inflation](../../International%20Finance/Bridgewater/Principles%20For%20Navigating%20Big%20Debt%20Cycles/Part%20II%20Detailed%20Case%20Studies/German%20Debt%20Crisis%20andHyperinflation%20(1918–1924)/War%20Economies%20and%20Hyperinflation.md) Surprise (bp)** | **[Inflation](../../International%20Finance/Bridgewater/Principles%20For%20Navigating%20Big%20Debt%20Cycles/Part%20II%20Detailed%20Case%20Studies/German%20Debt%20Crisis%20andHyperinflation%20(1918–1924)/War%20Economies%20and%20Hyperinflation.md) [Spread Change](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%207/Profit%20and%20Loss%20Attribution%20with%20an%20OAS.md) (bp)** | **Residual (bp)** | **Total Return (bp)** |

| **Total** | | 27.7 | 184.6 | -3.0 | -13.1 | 5.3 | -29.7 | -1.9 | 169.9 |

| **912828GN** | 4/15/2012 | 7.1 | 8.9 | -3.0 | -6.1 | 5.2 | 31.5 | -0.6 | 43.0 |

| **912828CP** | 7/15/2014 | 19.0 | 77.3 | -3.0 | -9.6 | 5.2 | -0.2 | 2.8 | 91.5 |

| **912810FR** | 1/15/2025 | 39.9 | 337.0 | -3.0 | -17.4 | 5.4 | -66.1 | -8.1 | 287.7 |

#### Observations
1. **Short-Term Bonds (e.g.,  912828GN)**:
   - Positive [inflation](../../International%20Finance/Bridgewater/Principles%20For%20Navigating%20Big%20Debt%20Cycles/Part%20II%20Detailed%20Case%20Studies/German%20Debt%20Crisis%20andHyperinflation%20(1918–1924)/War%20Economies%20and%20Hyperinflation.md) [spread change](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%207/Profit%20and%20Loss%20Attribution%20with%20an%20OAS.md) (+31.5 bp) contributed significantly to total return (+43.0 bp).
1. **Intermediate Bonds (e.g.,  912828CP)**:
   - [Inflation](../../International%20Finance/Bridgewater/Principles%20For%20Navigating%20Big%20Debt%20Cycles/Part%20II%20Detailed%20Case%20Studies/German%20Debt%20Crisis%20andHyperinflation%20(1918–1924)/War%20Economies%20and%20Hyperinflation.md) [spread change](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%207/Profit%20and%20Loss%20Attribution%20with%20an%20OAS.md) (-0.2 bp) was negligible,  with most of the return driven by yield-curve change (+77.3 bp).
1. **Long-Term Bonds (e.g.,  912810FR)**:
   - Negative [inflation](../../International%20Finance/Bridgewater/Principles%20For%20Navigating%20Big%20Debt%20Cycles/Part%20II%20Detailed%20Case%20Studies/German%20Debt%20Crisis%20andHyperinflation%20(1918–1924)/War%20Economies%20and%20Hyperinflation.md) [spread change](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%207/Profit%20and%20Loss%20Attribution%20with%20an%20OAS.md) (-66.1 bp) detracted significantly from total return (+287.7 bp).

## 4. Selecting an Appropriate Attribution Model

### 4.1 Comparison of Attribution Models (Exhibit 71-16)

| **Component** | **Total Return (bp)** | **Excess of Yield-Curve (bp)** | **Excess of Yield-Curve and Vol (bp)** | **Fully Analytical (Sector-Level,  bp)** | **Fully Analytical (Top-Level,  bp)** |

| **Total** | 32.1 | 32.1 | 32.1 | 32.1 | 32.1 |

| **Yield-Curves** | | 24.6 | 24.6 | 24.6 | 24.6 |

| **[Implied Volatility](../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%205%20Options%20on%20Prices%20and%20Hedge-Based%20Valuation/A%20Real-Life%20Option%20Pricing%20Exercise.md)**| | | 1.9 | 1.9 | 1.9 |

| **[Spread Duration](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%2014/Spread%20Duration%20and%20Dvo1.md) Mismatch** | | | | | -1.8 |

| **[Asset Allocation](../../Advanced%20Investments/Lecture%202-%20Asset%20Allocation%20with%20Multiple%20Risky%20Assets.md)** | 2.9 | -2.2 | -4.0 | 3.2 | 5.0 |

| **Security Selection**| 29.2 | 9.7 | 9.6 | 9.3 | 9.3 |

| **Mortgage** | | | | -8.2 | -8.2 |

| **Residual** | | | | 1.3 | 1.3 |

#### Observations
1. **Yield-Curve Contribution**:
   - Yield-curve exposure contributed +24.6 bp across all models.
1. **[Implied Volatility](../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%205%20Options%20on%20Prices%20and%20Hedge-Based%20Valuation/A%20Real-Life%20Option%20Pricing%20Exercise.md) Contribution**:
   - Adding [implied volatility](../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%205%20Options%20on%20Prices%20and%20Hedge-Based%20Valuation/A%20Real-Life%20Option%20Pricing%20Exercise.md) as a common factor contributed an additional +1.9 bp.
1. **[Asset Allocation](Lecture%202-%20[[Lecture%202-%20Asset%20Allocation%20with%20Multiple%20Risky%20Assets) with [Multiple Risky Assets](../../Advanced%20Investments/Lecture%202-%20Asset%20Allocation%20with%20Multiple%20Risky%20Assets.md)|[asset allocation](../../Advanced%20Investments/Lecture%202-%20Asset%20Allocation%20with%20Multiple%20Risky%20Assets.md)]]**:
   - [Asset Allocation](Lecture%202-%20[[Lecture%202-%20Asset%20Allocation%20with%20Multiple%20Risky%20Assets) with [Multiple Risky Assets](../../Advanced%20Investments/Lecture%202-%20Asset%20Allocation%20with%20Multiple%20Risky%20Assets.md)|[asset allocation](../../Advanced%20Investments/Lecture%202-%20Asset%20Allocation%20with%20Multiple%20Risky%20Assets.md)]] contributions varied significantly across models,  ranging from -4.0 bp to +5.0 bp.
1. **Security Selection**:
   - Security selection contributed consistently across models,  with a range of +9.3 bp to +9.7 bp.

### 4.2 Fully Analytical Model

- The Fully Analytical model provides the most detailed breakdown of [returns](../../Financial%20Markets/Financial%20Asset%20Pricing%20Theory%20Overview/Chapter%203%20-%20%20Assets,%20Portfolios,%20and%20Arbitrage/Assets.md),  incorporating:
  - Sector-level allocation of spread exposure.
  - Mortgage-specific factors (e.g.,  prepayment surprises).
  - Residuals to capture unexplained [returns](../../Financial%20Markets/Financial%20Asset%20Pricing%20Theory%20Overview/Chapter%203%20-%20%20Assets,%20Portfolios,%20and%20Arbitrage/Assets.md).

## 5. Implications for Portfolio Management

### 5.1 Inflation-Linked Securities
- **Key Takeaways**:
  - [Inflation](../../International%20Finance/Bridgewater/Principles%20For%20Navigating%20Big%20Debt%20Cycles/Part%20II%20Detailed%20Case%20Studies/German%20Debt%20Crisis%20andHyperinflation%20(1918–1924)/War%20Economies%20and%20Hyperinflation.md) spread changes and [inflation](../../International%20Finance/Bridgewater/Principles%20For%20Navigating%20Big%20Debt%20Cycles/Part%20II%20Detailed%20Case%20Studies/German%20Debt%20Crisis%20andHyperinflation%20(1918–1924)/War%20Economies%20and%20Hyperinflation.md) surprises are critical drivers of [returns](../../Financial%20Markets/Financial%20Asset%20Pricing%20Theory%20Overview/Chapter%203%20-%20%20Assets,%20Portfolios,%20and%20Arbitrage/Assets.md) for [inflation](../../International%20Finance/Bridgewater/Principles%20For%20Navigating%20Big%20Debt%20Cycles/Part%20II%20Detailed%20Case%20Studies/German%20Debt%20Crisis%20andHyperinflation%20(1918–1924)/War%20Economies%20and%20Hyperinflation.md)-linked securities.
  - Managers should monitor the [term structure](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%209/The%20Vasicek%20Model.md) of [inflation](../../International%20Finance/Bridgewater/Principles%20For%20Navigating%20Big%20Debt%20Cycles/Part%20II%20Detailed%20Case%20Studies/German%20Debt%20Crisis%20andHyperinflation%20(1918–1924)/War%20Economies%20and%20Hyperinflation.md) [expectations](../Fixed%20Income%20Lecture%20Notes/FORWARD%20RATES%20AND%20TERM%20STRUCTURE.md) and use detailed analytics to manage partial sensitivities.

### 5.2 Model Selection
- **Key Takeaways**:
  - The choice of attribution model should align with the [portfolio](../../Advanced%20Investments/An%20Asset%20Allocation%20Primer.md)'s decision structure.
  - The Fully Analytical model is ideal for portfolios with complex exposures,  such as [inflation](../../International%20Finance/Bridgewater/Principles%20For%20Navigating%20Big%20Debt%20Cycles/Part%20II%20Detailed%20Case%20Studies/German%20Debt%20Crisis%20andHyperinflation%20(1918–1924)/War%20Economies%20and%20Hyperinflation.md)-linked securities and [mortgage-backed securities](../../Financial%20Markets%20and%20Institutions/III.%20Liquidity%20of%20Assets/Class%207-%20CP,%20Repo,%20and%20the%20Crisis/Fremont%20Financial%20Corp.%20(b).md).

### 5.3 Practical Recommendations
- Use sector-level attribution to identify underperforming subsectors and refine allocation decisions.
- Incorporate [implied volatility](../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%205%20Options%20on%20Prices%20and%20Hedge-Based%20Valuation/A%20Real-Life%20Option%20Pricing%20Exercise.md) and [inflation](../../International%20Finance/Bridgewater/Principles%20For%20Navigating%20Big%20Debt%20Cycles/Part%20II%20Detailed%20Case%20Studies/German%20Debt%20Crisis%20andHyperinflation%20(1918–1924)/War%20Economies%20and%20Hyperinflation.md)-related components into attribution models to capture their contributions to performance.

## 6. Summary and Key Takeaways

### 6.1 Inflation-Linked Securities
- [Inflation](../../International%20Finance/Bridgewater/Principles%20For%20Navigating%20Big%20Debt%20Cycles/Part%20II%20Detailed%20Case%20Studies/German%20Debt%20Crisis%20andHyperinflation%20(1918–1924)/War%20Economies%20and%20Hyperinflation.md)-linked securities require specialized attribution models to account for nominal [interest rate exposure](../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20III%20THE%20PLAYERS/Chapter%2013%20-%20Banks%20Asset-Liability%20Management/Duration%20Gap%20Management.md),  [inflation](../../International%20Finance/Bridgewater/Principles%20For%20Navigating%20Big%20Debt%20Cycles/Part%20II%20Detailed%20Case%20Studies/German%20Debt%20Crisis%20andHyperinflation%20(1918–1924)/War%20Economies%20and%20Hyperinflation.md)-related components,  and residuals.
- [Inflation](../../International%20Finance/Bridgewater/Principles%20For%20Navigating%20Big%20Debt%20Cycles/Part%20II%20Detailed%20Case%20Studies/German%20Debt%20Crisis%20andHyperinflation%20(1918–1924)/War%20Economies%20and%20Hyperinflation.md) spread changes and [inflation](../../International%20Finance/Bridgewater/Principles%20For%20Navigating%20Big%20Debt%20Cycles/Part%20II%20Detailed%20Case%20Studies/German%20Debt%20Crisis%20andHyperinflation%20(1918–1924)/War%20Economies%20and%20Hyperinflation.md) surprises are critical drivers of [returns](../../Financial%20Markets/Financial%20Asset%20Pricing%20Theory%20Overview/Chapter%203%20-%20%20Assets,%20Portfolios,%20and%20Arbitrage/Assets.md).

### 6.2 Attribution Models
- The Fully Analytical model provides the most detailed breakdown of [returns](../../Financial%20Markets/Financial%20Asset%20Pricing%20Theory%20Overview/Chapter%203%20-%20%20Assets,%20Portfolios,%20and%20Arbitrage/Assets.md),  making it suitable for portfolios with complex exposures.
- Model selection should align with the [portfolio](../../Advanced%20Investments/An%20Asset%20Allocation%20Primer.md)'s decision structure and management objectives.

By adopting advanced attribution techniques,  [portfolio](../../Advanced%20Investments/An%20Asset%20Allocation%20Primer.md) managers can optimize risk-adjusted [returns](../../Financial%20Markets/Financial%20Asset%20Pricing%20Theory%20Overview/Chapter%203%20-%20%20Assets,%20Portfolios,%20and%20Arbitrage/Assets.md),  enhance decision-making,  and achieve superior performance outcomes.

# Lecture Notes: Advanced Topics in Performance Attribution for Fixed Income Portfolios

## 1. Introduction to Advanced Performance Attribution

- Performance attribution in [fixed income](../Lecture%20Notes%20Bonds,%20%20Preferred%20Stock,%20%20and%20Structured%20Products.md) portfolios involves decomposing [returns](../../Financial%20Markets/Financial%20Asset%20Pricing%20Theory%20Overview/Chapter%203%20-%20%20Assets,%20Portfolios,%20and%20Arbitrage/Assets.md) into contributions from various factors,  such as yield-curve movements,  [implied volatility](../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%205%20Options%20on%20Prices%20and%20Hedge-Based%20Valuation/A%20Real-Life%20Option%20Pricing%20Exercise.md),  spreads,  [inflation](../../International%20Finance/Bridgewater/Principles%20For%20Navigating%20Big%20Debt%20Cycles/Part%20II%20Detailed%20Case%20Studies/German%20Debt%20Crisis%20andHyperinflation%20(1918–1924)/War%20Economies%20and%20Hyperinflation.md),  and foreign exchange (FX) exposures.
- This lecture focuses on:
  - **Multicurrency Attribution**: Decomposing global [portfolio](../../Advanced%20Investments/An%20Asset%20Allocation%20Primer.md) [returns](../../Financial%20Markets/Financial%20Asset%20Pricing%20Theory%20Overview/Chapter%203%20-%20%20Assets,%20Portfolios,%20and%20Arbitrage/Assets.md) into FX allocation,  [FX hedging](../../Financial%20Markets/Random%20Walks%20in%20Fixed%20Income%20and%20Foreign%20Exchange/Chapter%204/Fx%20Hedging%20of%20Fixed%20Income%20-%20What%20Is%20the.md),  and local market contributions.
  - **[FX Hedging](../../Financial%20Markets/Random%20Walks%20in%20Fixed%20Income%20and%20Foreign%20Exchange/Chapter%204/Fx%20Hedging%20of%20Fixed%20Income%20-%20What%20Is%20the.md) Effects**: Accounting for unintended exposures to local [interest rates](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%202/Interest%20Rate%20Quotations.md) and cash balances.
  - **Local Market Allocation**: Separating global [duration](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%205/Key%20Rates%20O1s%20Durations%20and%20Hedging.md) positioning from local curve advantages and excess [returns](../../Financial%20Markets/Financial%20Asset%20Pricing%20Theory%20Overview/Chapter%203%20-%20%20Assets,%20Portfolios,%20and%20Arbitrage/Assets.md).
  - **Curve Allocation to Local Markets**: Using curve-matching portfolios (CMPs) to analyze global interest rate positioning.

## 2. Multicurrency Attribution

### 2.1 FX Return Splitting

- **Base [Currency](../../Financial%20Instruments/Lecture%20Notes-%20Financial%20Instruments/Teaching%20Note%201-%20Forward%20Rates%20Agreement/Forwards%20and%20Futures%20Notes.md) Total Return**:
  The total return of a security denominated in a non-base [currency](../../Financial%20Instruments/Lecture%20Notes-%20Financial%20Instruments/Teaching%20Note%201-%20Forward%20Rates%20Agreement/Forwards%20and%20Futures%20Notes.md) can be expressed as:
 $ {}^{b}R_{i} = F_{i} + R_{i}F_{i} + R_{i} $$
  Where:
  - \( {}^{b}R_{i} \): Base [currency](../../Financial%20Instruments/Lecture%20Notes-%20Financial%20Instruments/Teaching%20Note%201-%20Forward%20Rates%20Agreement/Forwards%20and%20Futures%20Notes.md) total return of security \(i\).
  - \( F_{i} \): FX return (change in exchange rate).
  - \( R_{i} \): Local [currency](../../Financial%20Instruments/Lecture%20Notes-%20Financial%20Instruments/Teaching%20Note%201-%20Forward%20Rates%20Agreement/Forwards%20and%20Futures%20Notes.md) return.
- **Cross-Term**:
  - The cross-term \( R_{i}F_{i} \) represents the interaction between FX and local [returns](../../Financial%20Markets/Financial%20Asset%20Pricing%20Theory%20Overview/Chapter%203%20-%20%20Assets,%20Portfolios,%20and%20Arbitrage/Assets.md).
  - While typically small for [fixed income securities](../../Clippings/Bond%20Equivalent%20Yield%20(BEY)%20-%20Definition,%20Formula,%20and%20Example.md),  it can become significant when FX and local [returns](../../Financial%20Markets/Financial%20Asset%20Pricing%20Theory%20Overview/Chapter%203%20-%20%20Assets,%20Portfolios,%20and%20Arbitrage/Assets.md) have opposite signs and similar magnitudes.
- **Adjusted FX Return**:
  To separate FX performance from local management,  include the cash deposit return of each [currency](../../Financial%20Instruments/Lecture%20Notes-%20Financial%20Instruments/Teaching%20Note%201-%20Forward%20Rates%20Agreement/Forwards%20and%20Futures%20Notes.md):
 $ {}^{b}R_{i} = \left(F_{i} + R_{i}^{depo}\right) + R_{i}F_{i} + \left(R_{i} - R_{i}^{depo}\right) $$
  Where:
  - \( R_{i}^{depo} \): Local cash deposit return.

### 2.2 FX Hedging

- **Purpose**:
  [FX hedging](../../Financial%20Markets/Random%20Walks%20in%20Fixed%20Income%20and%20Foreign%20Exchange/Chapter%204/Fx%20Hedging%20of%20Fixed%20Income%20-%20What%20Is%20the.md) overlays are used to manage FX exposures without affecting local market exposures. Common instruments include [FX forwards](../../Financial%20Instruments/Financial%20Instruments%20PSET%20Solutions.md) and swaps.

#### 2.2.1 Exposure to Local Interest Rates
- [FX hedging](../../Financial%20Markets/Random%20Walks%20in%20Fixed%20Income%20and%20Foreign%20Exchange/Chapter%204/Fx%20Hedging%20of%20Fixed%20Income%20-%20What%20Is%20the.md) instruments often have unintended exposure to the short end of local [interest rate curves](../../Financial%20Markets/Financial%20Asset%20Pricing%20Theory%20Overview/Chapter%2010%20-%20The%20Economics%20of%20the%20Term%20Structure%20of%20Interest%20Rates/__temp__Chapter%2010%20-%20The%20Economics%20of%20the%20Term%20Structure%20of%20Interest%20Rates.md),  especially during market crises.
- This exposure is considered part of the [hedging](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%205/Key%20Rates%20O1s%20Durations%20and%20Hedging.md) return and not part of local market strategy decisions.

#### 2.2.2 Cash Balance Effect
- As FX rates fluctuate,  the mark-to-market value of [FX forwards](../../Financial%20Instruments/Financial%20Instruments%20PSET%20Solutions.md) becomes nonzero,  creating a cash balance (positive or negative).
- Unless reinvested regularly,  this cash balance represents an unintended allocation to cash or [leverage](../../Advanced%20Investments/Lecture%206-Leverage,%20Tail%20Risk,%20Volatility%20Products.md).
- **Solution**:
  - Capture this effect as the difference between the actual [portfolio](../../Advanced%20Investments/An%20Asset%20Allocation%20Primer.md) return and the hypothetical return if the FX hedge cash balance were reinvested daily.

### 2.3 FX Outperformance

- **Pure FX Outperformance**:
 $ {}^{FX}R^{P} - {}^{FX}R^{B} = \sum_{c} {}^{b}h_{c}^{P} \cdot \left(F_{c} + R_{c}^{depo}\right) - \sum_{c} {}^{b}h_{c}^{B} \cdot \left(F_{c} + R_{c}^{depo}\right) $$
  Where:
  - \( {}^{b}h_{c}^{P} \): Effective [portfolio](../../Advanced%20Investments/An%20Asset%20Allocation%20Primer.md) exposure to FX rate \(c\) after [hedging](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%205/Key%20Rates%20O1s%20Durations%20and%20Hedging.md).
  - \( {}^{b}h_{c}^{B} \): Benchmark exposure to FX rate \(c\).
- **FX Allocation**:
 $ \sum_{c} \left({}^{b}h_{c}^{P} - {}^{b}h_{c}^{B}\right) \cdot \left(F_{c} + R_{c}^{depo} - R_{b}^{depo}\right) $$

- **FX/Local Cross-Term**:
 $ \sum_{c} \left({}^{b}w_{c}^{P}R_{c}^{P} - {}^{b}w_{c}^{B}R_{c}^{B}\right) \cdot F_{c}^{B} + \left(\left({}^{b}w_{c}^{P} - {}^{b}h_{c}^{P}\right) - \left({}^{b}w_{c}^{B} - {}^{b}h_{c}^{B}\right)\right) \cdot R_{c}^{depo} \cdot F_{c}^{B} $$

## 3. Local Market Allocation

### 3.1 Local Market Outperformance

- After accounting for FX exposures and [hedging](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%205/Key%20Rates%20O1s%20Durations%20and%20Hedging.md),  the remaining outperformance is given by:
 $ {}^{L}R^{P} - {}^{L}R^{B} = \sum_{m} {}^{b}w_{m}^{P} \cdot \left(R_{m}^{P} - R_{m}^{depo,  P}\right) - \sum_{m} {}^{b}w_{m}^{B} \cdot \left(R_{m}^{B} - R_{m}^{depo,  B}\right) $$

- **Local Market Allocation**:
 $ \sum_{m} \left({}^{b}w_{m}^{P} - {}^{b}w_{m}^{B}\right) \cdot \left(\left(R_{m}^{B} - R_{m}^{depo,  B}\right) - \left(R^{B} - R^{depo,  B}\right)\right) $$

- **Local Market Management**:
 $ \sum_{m} {}^{b}w_{m}^{P} \cdot \left(\left(R_{m}^{P} - R_{m}^{depo,  P}\right) - \left(R_{m}^{B} - R_{m}^{depo,  B}\right)\right) $$

### 3.2 Factor-Based Local Market Allocation

- Local market allocation can be decomposed into contributions from [risk factors](../../Financial%20Instruments/Assignments/PSET%206-%20Financial%20Instruments.md) such as yield-curve,  [implied volatility](../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%205%20Options%20on%20Prices%20and%20Hedge-Based%20Valuation/A%20Real-Life%20Option%20Pricing%20Exercise.md),  and spreads:
 $ {}^{L}R^{P} - {}^{L}R^{B} = \sum_{k} \sum_{m_{k}} {}^{b}w_{m_{k}}^{P} \alpha_{k,  m_{k}}^{P} f_{k,  m_{k}}^{P} - \sum_{k} \sum_{m_{k}} {}^{b}w_{m_{k}}^{B} \alpha_{k,  m_{k}}^{B} f_{k,  m_{k}}^{B} $$

- **Allocation**:
 $ \sum_{k} \left(\sum_{m_{k}} \left({}^{b}w_{m_{k}}^{P} \alpha_{k,  m_{k}}^{P} - {}^{b}w_{m_{k}}^{B} \alpha_{k,  m_{k}}^{B}\right) \cdot \left(f_{k,  m_{k}}^{B} - f_{k}^{H}\right)\right) $$

- **Management**:
 $ \sum_{k} \left(\sum_{m_{k}} {}^{b}w_{m_{k}}^{P} \alpha_{k,  m_{k}}^{P} \cdot \left(f_{k,  m_{k}}^{P} - f_{k,  m_{k}}^{B}\right)\right) $$

## 4. Curve Allocation to Local Markets

### 4.1 Global Interest Rate Positioning

- Global interest rate positioning can be separated into:
  - **Global [Duration Mismatch](../../Advanced%20Financial%20Analysis%20and%20Valuation/Lecture%20Notes%20Advanced%20Financial%20Analysis%20and%20Valuation/Week%206/Week%206%20Assignment%20Review.md)**: Contribution of the [portfolio](../../Advanced%20Investments/An%20Asset%20Allocation%20Primer.md)'s overall [duration](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%205/Key%20Rates%20O1s%20Durations%20and%20Hedging.md) position.
  - **Local Curve Advantage**: Contribution of [interest rate exposure](../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20III%20THE%20PLAYERS/Chapter%2013%20-%20Banks%20Asset-Liability%20Management/Duration%20Gap%20Management.md) outside the reference [currency](../../Financial%20Instruments/Lecture%20Notes-%20Financial%20Instruments/Teaching%20Note%201-%20Forward%20Rates%20Agreement/Forwards%20and%20Futures%20Notes.md).
  - **Excess of Curve Allocation**: Contribution of other risk exposures in each [currency](../../Financial%20Instruments/Lecture%20Notes-%20Financial%20Instruments/Teaching%20Note%201-%20Forward%20Rates%20Agreement/Forwards%20and%20Futures%20Notes.md).

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
  - [FX hedging](../../Financial%20Markets/Random%20Walks%20in%20Fixed%20Income%20and%20Foreign%20Exchange/Chapter%204/Fx%20Hedging%20of%20Fixed%20Income%20-%20What%20Is%20the.md) introduces unintended exposures to local [interest rates](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%202/Interest%20Rate%20Quotations.md) and cash balances,  which must be accounted for in attribution.
  - Explicitly separating FX and local [returns](../../Financial%20Markets/Financial%20Asset%20Pricing%20Theory%20Overview/Chapter%203%20-%20%20Assets,%20Portfolios,%20and%20Arbitrage/Assets.md) provides a clearer view of [portfolio](../../Advanced%20Investments/An%20Asset%20Allocation%20Primer.md) performance.

### 5.2 Local Market Allocation
- **Key Takeaways**:
  - Factor-based allocation provides a more granular view of local market exposures,  enabling better [risk management](../../Financial%20Engineering/Financial%20Mathematics%20Course.md).
  - Decomposing local [returns](../../Financial%20Markets/Financial%20Asset%20Pricing%20Theory%20Overview/Chapter%203%20-%20%20Assets,%20Portfolios,%20and%20Arbitrage/Assets.md) into allocation,  management,  and [leverage](../../Advanced%20Investments/Lecture%206-Leverage,%20Tail%20Risk,%20Volatility%20Products.md) components helps identify sources of outperformance.

### 5.3 Curve Allocation
- **Key Takeaways**:
  - Using curve-matching portfolios (CMPs) simplifies the analysis of global interest rate positioning.
  - Separating global [duration mismatch](../../Advanced%20Financial%20Analysis%20and%20Valuation/Lecture%20Notes%20Advanced%20Financial%20Analysis%20and%20Valuation/Week%206/Week%206%20Assignment%20Review.md) from local curve advantages provides insights into the effectiveness of interest rate strategies.

## 6. Summary and Key Takeaways

### 6.1 Multicurrency Attribution
- Multicurrency portfolios require separating FX [returns](../../Financial%20Markets/Financial%20Asset%20Pricing%20Theory%20Overview/Chapter%203%20-%20%20Assets,%20Portfolios,%20and%20Arbitrage/Assets.md),  [FX hedging](../../Financial%20Markets/Random%20Walks%20in%20Fixed%20Income%20and%20Foreign%20Exchange/Chapter%204/Fx%20Hedging%20of%20Fixed%20Income%20-%20What%20Is%20the.md) effects,  and local market contributions.
- FX/local cross-terms,  while typically small,  can accumulate over time and significantly impact total [returns](../../Financial%20Markets/Financial%20Asset%20Pricing%20Theory%20Overview/Chapter%203%20-%20%20Assets,%20Portfolios,%20and%20Arbitrage/Assets.md).

### 6.2 Local Market Allocation
- Local market outperformance can be decomposed into allocation,  management,  and [leverage](../../Advanced%20Investments/Lecture%206-Leverage,%20Tail%20Risk,%20Volatility%20Products.md) components.
- Factor-based allocation provides a detailed view of exposures to yield-curve,  volatility,  and spread risks.

### 6.3 Curve Allocation
- Curve carry and curve change [returns](../../Financial%20Markets/Financial%20Asset%20Pricing%20Theory%20Overview/Chapter%203%20-%20%20Assets,%20Portfolios,%20and%20Arbitrage/Assets.md) are critical drivers of [fixed income](../Lecture%20Notes%20Bonds,%20%20Preferred%20Stock,%20%20and%20Structured%20Products.md) performance.
- Using CMPs simplifies the analysis of curve carry and provides consistent attribution results.

By mastering these advanced attribution techniques,  [portfolio](../../Advanced%20Investments/An%20Asset%20Allocation%20Primer.md) managers can optimize risk-adjusted [returns](../../Financial%20Markets/Financial%20Asset%20Pricing%20Theory%20Overview/Chapter%203%20-%20%20Assets,%20Portfolios,%20and%20Arbitrage/Assets.md),  enhance decision-making,  and achieve superior performance outcomes.

### Lecture Notes: Advanced Attribution for Global Yield-Curve Allocation and FX Positioning

## 1. Introduction to Global Yield-Curve Allocation and FX Positioning

- Global fixed-income portfolios often involve exposure to multiple currencies and yield curves. Proper attribution of performance requires decomposing [returns](../../Financial%20Markets/Financial%20Asset%20Pricing%20Theory%20Overview/Chapter%203%20-%20%20Assets,%20Portfolios,%20and%20Arbitrage/Assets.md) into contributions from FX positioning,  yield-curve carry,  and yield-curve changes.
- This lecture focuses on:
  - **Global Curve Carry and Change Attribution**: Breaking down outperformance into carry and yield-curve change components.
  - **FX Allocation and [Hedging](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%205/Key%20Rates%20O1s%20Durations%20and%20Hedging.md)**: Understanding the impact of FX positioning and [hedging](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%205/Key%20Rates%20O1s%20Durations%20and%20Hedging.md) on [portfolio](../../Advanced%20Investments/An%20Asset%20Allocation%20Primer.md) [returns](../../Financial%20Markets/Financial%20Asset%20Pricing%20Theory%20Overview/Chapter%203%20-%20%20Assets,%20Portfolios,%20and%20Arbitrage/Assets.md).
  - **Practical Example**: Analyzing the performance of a U.S. dollar-denominated [portfolio](../../Advanced%20Investments/An%20Asset%20Allocation%20Primer.md) managed against the Barclays Global G4 Treasury Index.

## 2. Global Curve Carry Attribution

### 2.1 Curve Carry Management

- **Key Insight**: Curve carry management is zero by construction because the carry return at each key-rate point and the deposit rate return are uniform across all securities in the [portfolio](../../Advanced%20Investments/An%20Asset%20Allocation%20Primer.md) and benchmark.
- **Formula**:
 $\sum_{c}\sum_{j}^{b}w_{c}^{P}\omega_{c,  j}^{P}\cdot\left(\left(R_{c,  j}^{carry}-R_{c}^{depo}\right)-\left(R_{c,  j}^{carry}-R_{c}^{depo}\right)\right)=0$$

### 2.2 Global Curve Carry Over Deposit

- **Definition**: Measures the outperformance due to differences in [portfolio](../../Advanced%20Investments/An%20Asset%20Allocation%20Primer.md) and benchmark weights across curves and key-rate points.
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

- **Key Insight**: Curve change management is zero by construction because [interest rate changes](../../International%20Finance/Bridgewater/How%20Countries%20Go%20Broke/How%20Countries%20Go%20Broke-Chapter%2012%20to%20Chapter%2014.md) are uniform across all securities in the [portfolio](../../Advanced%20Investments/An%20Asset%20Allocation%20Primer.md) and benchmark.
- **Formula**:
 $-\sum_{c}\sum_{j}^{b}w_{c}^{P}KRD_{c,  j}^{P}\cdot\left(\Delta y_{c,  j}-\Delta y_{c,  j}\right)=0$$

### 3.2 Global Duration Mismatch

- **Definition**: Measures the outperformance due to differences in [portfolio](../../Advanced%20Investments/An%20Asset%20Allocation%20Primer.md) and benchmark key-rate durations relative to a reference curve.
- **Formula**:
 $-\sum_{c}\sum_{j}\Big(^{b}w_{c}^{P}KRD_{c,  j}^{P}-^{b}w_{c}^{B}KRD_{c,  j}^{B}\Big)\cdot\Delta y_{ref,  j}$$
- **Key Insight**: If no reference curve is used,  the global [duration mismatch](../../Advanced%20Financial%20Analysis%20and%20Valuation/Lecture%20Notes%20Advanced%20Financial%20Analysis%20and%20Valuation/Week%206/Week%206%20Assignment%20Review.md) becomes zero,  and the outperformance is broken down per curve and key-rate point:
 $-\sum_{c}\sum_{j}\Big(^{b}w_{c}^{P}KRD_{c,  j}^{P}-^{b}w_{c}^{B}KRD_{c,  j}^{B}\Big)\cdot\Delta y_{c,  j}$$

### 3.3 Example: Euro Curve Change Attribution

- **[Duration](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%205/Key%20Rates%20O1s%20Durations%20and%20Hedging.md) Overweight**: \(2.33 - 1.88 = 0.45\).
- **Average Yield Change**: -28 bp.
- **Contribution**:
 $(2.33 - 1.88) \times (-28 \,  \text{bp}) = -12.6 \,  \text{bp}$$

## 4. FX Allocation and Hedging

### 4.1 FX Allocation Outperformance

- **Definition**: Measures the outperformance due to deviations in [portfolio](../../Advanced%20Investments/An%20Asset%20Allocation%20Primer.md) and benchmark FX exposures.
- **Formula**:
 $\sum_{c} \left({}^{b}h_{c}^{P} - {}^{b}h_{c}^{B}\right) \cdot \left(F_{c} + R_{c}^{depo} - R_{b}^{depo}\right)$$

### 4.2 FX Hedging Effects

- **Definition**: Measures the impact of [FX hedging](../../Financial%20Markets/Random%20Walks%20in%20Fixed%20Income%20and%20Foreign%20Exchange/Chapter%204/Fx%20Hedging%20of%20Fixed%20Income%20-%20What%20Is%20the.md) instruments on [portfolio](../../Advanced%20Investments/An%20Asset%20Allocation%20Primer.md) [returns](../../Financial%20Markets/Financial%20Asset%20Pricing%20Theory%20Overview/Chapter%203%20-%20%20Assets,%20Portfolios,%20and%20Arbitrage/Assets.md),  including exposure to local [interest rates](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%202/Interest%20Rate%20Quotations.md) and cash balance effects.
- **Key Insight**: [FX hedging](../../Financial%20Markets/Random%20Walks%20in%20Fixed%20Income%20and%20Foreign%20Exchange/Chapter%204/Fx%20Hedging%20of%20Fixed%20Income%20-%20What%20Is%20the.md) effects are captured as the difference between the actual [portfolio](../../Advanced%20Investments/An%20Asset%20Allocation%20Primer.md) return and the hypothetical return if the FX hedge cash balance were reinvested daily.

### 4.3 Example: Euro FX Allocation Outperformance

- **Excess FX Return**: 306.1 bp.
- **Market Value Overweight**: \(34.4\% - 29.8\% = 4.6\%\).
- **Contribution**:
 $(34.4\% - 29.8\%) \times 306.1 \,  \text{bp} = +14.1 \,  \text{bp}$$
- **Reported Contribution**: +14.8 bp (difference due to daily compounding).

## 5. Practical Example: Portfolio vs. Barclays Global G4 Treasury Index

### 5.1 Portfolio Characteristics (Exhibit 72-1)

| **[Currency](../../Financial%20Instruments/Lecture%20Notes-%20Financial%20Instruments/Teaching%20Note%201-%20Forward%20Rates%20Agreement/Forwards%20and%20Futures%20Notes.md)** | **[Portfolio](../../Advanced%20Investments/An%20Asset%20Allocation%20Primer.md) Weight (%)** | **Benchmark Weight (%)** | **Net Weight (%)** | **[Portfolio](../../Advanced%20Investments/An%20Asset%20Allocation%20Primer.md) OAD** | **Benchmark OAD** | **Net OAD** |

| **Total** | 100.0 | 100.0 | 0.0 | 6.46 | 6.47 | -0.01 |

| **U.S. Dollar** | 24.1 | 28.6 | -4.5 | 1.05 | 1.50 | -0.45 |

| **Euro** | 34.4 | 29.8 | 4.6 | 2.33 | 1.88 | 0.45 |

| **Japanese Yen** | 34.5 | 34.5 | 0.0 | 2.45 | 2.46 | -0.01 |

| **British Pound** | 7.0 | 7.1 | -0.1 | 0.63 | 0.63 | 0.00 |

### 5.2 Total Outperformance Breakdown (Exhibit 72-2)

| **Component** | **Total (bp)** | **U.S. Dollar (bp)** | **Euro (bp)** | **Japanese Yen (bp)** | **British Pound (bp)** |

| **Outperformance** | 10.5 | 15.5 | -5.1 | 0.5 | -0.4 |

| **FX Allocation & [Hedging](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%205/Key%20Rates%20O1s%20Durations%20and%20Hedging.md)** | 14.3 | 0.0 | 14.4 | 0.0 | -0.1 |

| **Local Market Allocation** | 6.5 | 16.5 | -9.7 | -0.3 | 0.0 |

| **Local Yield-Curves** | 3.1 | 14.9 | -12.0 | 0.2 | 0.0 |

| **Local Management** | -10.3 | -1.0 | -9.8 | 0.8 | -0.3 |

### 5.3 Global Yield-Curve Allocation Outperformance (Exhibit 72-4)

| **[Currency](../../Financial%20Instruments/Lecture%20Notes-%20Financial%20Instruments/Teaching%20Note%201-%20Forward%20Rates%20Agreement/Forwards%20and%20Futures%20Notes.md)** | **Carry (bp)** | **Change (bp)** | **Total (bp)** |

| **U.S. Dollar** | -1.4 | 16.3 | 14.9 |

| **Euro** | 1.1 | -13.1 | -12.0 |

| **Japanese Yen** | 0.2 | 0.0 | 0.2 |

| **British Pound** | 0.0 | 0.0 | 0.0 |

| **Total** | -0.1 | 3.2 | 3.1 |

## 6. Summary and Key Takeaways

### 6.1 Global Yield-Curve Allocation
- Curve carry management is zero by construction,  while global curve carry and change contributions depend on [portfolio](../../Advanced%20Investments/An%20Asset%20Allocation%20Primer.md) and benchmark deviations.
- [Duration](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%205/Key%20Rates%20O1s%20Durations%20and%20Hedging.md) positioning in the U.S. dollar and euro markets drove most of the yield-curve outperformance.

### 6.2 FX Allocation and Hedging
- FX allocation contributed significantly to outperformance,  particularly from the euro's strengthening against the U.S. dollar.
- [FX hedging](../../Financial%20Markets/Random%20Walks%20in%20Fixed%20Income%20and%20Foreign%20Exchange/Chapter%204/Fx%20Hedging%20of%20Fixed%20Income%20-%20What%20Is%20the.md) effects were minimal,  reflecting effective implementation of the manager's strategy.

### 6.3 Practical Applications
- Advanced attribution techniques provide deeper insights into [portfolio](../../Advanced%20Investments/An%20Asset%20Allocation%20Primer.md) performance,  enabling managers to optimize risk-adjusted [returns](../../Financial%20Markets/Financial%20Asset%20Pricing%20Theory%20Overview/Chapter%203%20-%20%20Assets,%20Portfolios,%20and%20Arbitrage/Assets.md) and refine [investment](../../Advanced%20Investments/An%20Asset%20Allocation%20Primer.md) strategies.

By mastering these concepts,  fixed-income [portfolio](../../Advanced%20Investments/An%20Asset%20Allocation%20Primer.md) managers can enhance their decision-making processes and achieve superior performance outcomes.

given by:
$$\sum_{s}\left(\beta^{P}w_{s}^{P}-\beta^{B}w_{s}^{B}\right)\cdot R_{s}^{B}$$

And the sector management term becomes:
$$\sum_{s}\beta^{P}w_{s}^{P}\cdot\left(R_{s}^{P}-R_{s}^{B}\right)$$

This approach shifts the responsibility for [leverage](../../Advanced%20Investments/Lecture%206-Leverage,%20Tail%20Risk,%20Volatility%20Products.md) decisions to the asset allocator,  who determines the total exposure to each sector. The sector managers are then evaluated based on their ability to generate excess [returns](../../Financial%20Markets/Financial%20Asset%20Pricing%20Theory%20Overview/Chapter%203%20-%20%20Assets,%20Portfolios,%20and%20Arbitrage/Assets.md) relative to the benchmark within their allocated exposure.

## 7. Practical Implications for Portfolio Management

### 7.1 Handling Leverage in Attribution Models

- **Key Takeaways**:
  - [Leverage](../../Advanced%20Investments/Lecture%206-Leverage,%20Tail%20Risk,%20Volatility%20Products.md) introduces additional complexity into performance attribution,  as it affects both the weights and [returns](../../Financial%20Markets/Financial%20Asset%20Pricing%20Theory%20Overview/Chapter%203%20-%20%20Assets,%20Portfolios,%20and%20Arbitrage/Assets.md) of [portfolio](../../Advanced%20Investments/An%20Asset%20Allocation%20Primer.md) components.
  - Properly accounting for [leverage](../../Advanced%20Investments/Lecture%206-Leverage,%20Tail%20Risk,%20Volatility%20Products.md) ensures that the contributions of [Asset Allocation](Lecture%202-%20[[Lecture%202-%20Asset%20Allocation%20with%20Multiple%20Risky%20Assets) with [Multiple Risky Assets](../../Advanced%20Investments/Lecture%202-%20Asset%20Allocation%20with%20Multiple%20Risky%20Assets.md)|[asset allocation](../../Advanced%20Investments/Lecture%202-%20Asset%20Allocation%20with%20Multiple%20Risky%20Assets.md)]] and sector management are accurately measured.
  - The choice of whether to embed [leverage](../../Advanced%20Investments/Lecture%206-Leverage,%20Tail%20Risk,%20Volatility%20Products.md) decisions in the [Asset Allocation](Lecture%202-%20[[Lecture%202-%20Asset%20Allocation%20with%20Multiple%20Risky%20Assets) with [Multiple Risky Assets](../../Advanced%20Investments/Lecture%202-%20Asset%20Allocation%20with%20Multiple%20Risky%20Assets.md)|[asset allocation](../../Advanced%20Investments/Lecture%202-%20Asset%20Allocation%20with%20Multiple%20Risky%20Assets.md)]] or sector management term depends on the [portfolio](../../Advanced%20Investments/An%20Asset%20Allocation%20Primer.md)'s decision-making structure.

### 7.2 Managing Derivative Exposures

- **Key Takeaways**:
  - [Derivatives](../../Financial%20Markets/Financial%20Trading%20and%20Markets/Chapter%209%20Arbitrage%20and%20Hedging%20With%20Options.md) can significantly alter the [leverage and risk](../../Financial%20Markets%20and%20Institutions/III.%20Liquidity%20of%20Assets/Class%209-%20Bailouts%20and%20Bank%20Failures/Risk%20Management%20Lessons%20From%20Long%20Term%20Capital%20Management.md) profile of a [portfolio](../../Advanced%20Investments/An%20Asset%20Allocation%20Primer.md),  even when their market value is small or zero.
  - Attribution models must account for the implicit [leverage](../../Advanced%20Investments/Lecture%206-Leverage,%20Tail%20Risk,%20Volatility%20Products.md) introduced by [derivatives](../../Financial%20Markets/Financial%20Trading%20and%20Markets/Chapter%209%20Arbitrage%20and%20Hedging%20With%20Options.md) to avoid misattributing performance.
  - Reporting [leverage](../../Advanced%20Investments/Lecture%206-Leverage,%20Tail%20Risk,%20Volatility%20Products.md) as a separate line item provides transparency and helps identify the sources of outperformance or underperformance.

### 7.3 Aligning Attribution with Decision-Making

- **Key Takeaways**:
  - Attribution models should align with the [portfolio](../../Advanced%20Investments/An%20Asset%20Allocation%20Primer.md)'s decision-making structure,  whether [leverage](../../Advanced%20Investments/Lecture%206-Leverage,%20Tail%20Risk,%20Volatility%20Products.md) decisions are made at the [Asset Allocation](Lecture%202-%20[[Lecture%202-%20Asset%20Allocation%20with%20Multiple%20Risky%20Assets) with [Multiple Risky Assets](../../Advanced%20Investments/Lecture%202-%20Asset%20Allocation%20with%20Multiple%20Risky%20Assets.md)|[asset allocation](../../Advanced%20Investments/Lecture%202-%20Asset%20Allocation%20with%20Multiple%20Risky%20Assets.md)]] or sector management level.
  - Clear separation of responsibilities between asset allocators and sector managers ensures that performance is attributed to the appropriate decision-makers.

## 8. Summary and Key Takeaways

### 8.1 Leverage and Derivatives in Attribution

- [Leverage](../../Advanced%20Investments/Lecture%206-Leverage,%20Tail%20Risk,%20Volatility%20Products.md) complicates performance attribution by altering the weights and [returns](../../Financial%20Markets/Financial%20Asset%20Pricing%20Theory%20Overview/Chapter%203%20-%20%20Assets,%20Portfolios,%20and%20Arbitrage/Assets.md) of [portfolio](../../Advanced%20Investments/An%20Asset%20Allocation%20Primer.md) components.
- Properly accounting for [leverage](../../Advanced%20Investments/Lecture%206-Leverage,%20Tail%20Risk,%20Volatility%20Products.md) ensures that the contributions of [Asset Allocation](Lecture%202-%20[[Lecture%202-%20Asset%20Allocation%20with%20Multiple%20Risky%20Assets) with [Multiple Risky Assets](../../Advanced%20Investments/Lecture%202-%20Asset%20Allocation%20with%20Multiple%20Risky%20Assets.md)|[asset allocation](../../Advanced%20Investments/Lecture%202-%20Asset%20Allocation%20with%20Multiple%20Risky%20Assets.md)]] and sector management are accurately measured.
- [Derivatives](../../Financial%20Markets/Financial%20Trading%20and%20Markets/Chapter%209%20Arbitrage%20and%20Hedging%20With%20Options.md) introduce implicit [leverage](../../Advanced%20Investments/Lecture%206-Leverage,%20Tail%20Risk,%20Volatility%20Products.md),  which must be accounted for in attribution models to avoid misattributing performance.

### 8.2 Practical Recommendations

1. **Report [Leverage](../../Advanced%20Investments/Lecture%206-Leverage,%20Tail%20Risk,%20Volatility%20Products.md) Separately**:
   - Include [leverage](../../Advanced%20Investments/Lecture%206-Leverage,%20Tail%20Risk,%20Volatility%20Products.md) as a separate line item in [attribution reports](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%203/Pl%20Attribution.md) to provide transparency and identify its impact on performance.

1. **Align Attribution with Decision-Making**:
   - Ensure that attribution models reflect the [portfolio](../../Advanced%20Investments/An%20Asset%20Allocation%20Primer.md)'s decision-making structure,  whether [leverage](../../Advanced%20Investments/Lecture%206-Leverage,%20Tail%20Risk,%20Volatility%20Products.md) decisions are made at the [Asset Allocation](Lecture%202-%20[[Lecture%202-%20Asset%20Allocation%20with%20Multiple%20Risky%20Assets) with [Multiple Risky Assets](../../Advanced%20Investments/Lecture%202-%20Asset%20Allocation%20with%20Multiple%20Risky%20Assets.md)|[asset allocation](../../Advanced%20Investments/Lecture%202-%20Asset%20Allocation%20with%20Multiple%20Risky%20Assets.md)]] or sector management level.

1. **Use Appropriate Return Bases**:
   - Define a consistent return basis for [derivatives](../../Financial%20Markets/Financial%20Trading%20and%20Markets/Chapter%209%20Arbitrage%20and%20Hedging%20With%20Options.md) to avoid non-intuitive results and ensure meaningful comparisons.

1. **Monitor Derivative Exposures**:
   - Regularly review derivative exposures to understand their impact on [portfolio](../../Advanced%20Investments/An%20Asset%20Allocation%20Primer.md) [leverage and risk](../../Financial%20Markets%20and%20Institutions/III.%20Liquidity%20of%20Assets/Class%209-%20Bailouts%20and%20Bank%20Failures/Risk%20Management%20Lessons%20From%20Long%20Term%20Capital%20Management.md).

By adopting these advanced attribution techniques,  [portfolio](../../Advanced%20Investments/An%20Asset%20Allocation%20Primer.md) managers can optimize risk-adjusted [returns](../../Financial%20Markets/Financial%20Asset%20Pricing%20Theory%20Overview/Chapter%203%20-%20%20Assets,%20Portfolios,%20and%20Arbitrage/Assets.md),  enhance decision-making,  and achieve superior performance outcomes.

### Lecture Notes: Advanced Performance Attribution in Fixed Income Portfolio Management – Leverage,  Derivatives,  and Multi-Currency Portfolios

## 1. Introduction to Advanced Attribution Techniques

- [Fixed income](../Lecture%20Notes%20Bonds,%20%20Preferred%20Stock,%20%20and%20Structured%20Products.md) [portfolio management](../../Financial%20Engineering/Fixed%20Income%20Derivatives/The%20Impact%20of%20Option%20Strategies%20in%20Financial%20%20Portfolios%20Performance.md) often involves complex instruments such as [derivatives](../../Financial%20Markets/Financial%20Trading%20and%20Markets/Chapter%209%20Arbitrage%20and%20Hedging%20With%20Options.md),  multi-[currency](../../Financial%20Instruments/Lecture%20Notes-%20Financial%20Instruments/Teaching%20Note%201-%20Forward%20Rates%20Agreement/Forwards%20and%20Futures%20Notes.md) exposures,  and [leverage](../../Advanced%20Investments/Lecture%206-Leverage,%20Tail%20Risk,%20Volatility%20Products.md). Proper attribution of performance requires decomposing [returns](../../Financial%20Markets/Financial%20Asset%20Pricing%20Theory%20Overview/Chapter%203%20-%20%20Assets,%20Portfolios,%20and%20Arbitrage/Assets.md) into contributions from [Asset Allocation](Lecture%202-%20[[Lecture%202-%20Asset%20Allocation%20with%20Multiple%20Risky%20Assets) with [Multiple Risky Assets](../../Advanced%20Investments/Lecture%202-%20Asset%20Allocation%20with%20Multiple%20Risky%20Assets.md)|[asset allocation](../../Advanced%20Investments/Lecture%202-%20Asset%20Allocation%20with%20Multiple%20Risky%20Assets.md)]],  security selection,  FX positioning,  and derivative overlays.
- This lecture focuses on:
  - **[Leverage](../../Advanced%20Investments/Lecture%206-Leverage,%20Tail%20Risk,%20Volatility%20Products.md) Attribution**: Handling [leverage](../../Advanced%20Investments/Lecture%206-Leverage,%20Tail%20Risk,%20Volatility%20Products.md) at both the [portfolio](../../Advanced%20Investments/An%20Asset%20Allocation%20Primer.md) and sector levels.
  - **Derivative Attribution**: Special treatment of [currency](../../Financial%20Instruments/Lecture%20Notes-%20Financial%20Instruments/Teaching%20Note%201-%20Forward%20Rates%20Agreement/Forwards%20and%20Futures%20Notes.md),  interest rate,  and [credit derivatives](../../Credit%20Markets/RISK%20NEUTRAL%20VALUATION%20FRAMEWORK%20FOR%20CREDIT%20DEFAULT%20SWAPS.md).
  - **Multi-[Currency](../../Financial%20Instruments/Lecture%20Notes-%20Financial%20Instruments/Teaching%20Note%201-%20Forward%20Rates%20Agreement/Forwards%20and%20Futures%20Notes.md) Attribution**: Decomposing global [portfolio](../../Advanced%20Investments/An%20Asset%20Allocation%20Primer.md) [returns](../../Financial%20Markets/Financial%20Asset%20Pricing%20Theory%20Overview/Chapter%203%20-%20%20Assets,%20Portfolios,%20and%20Arbitrage/Assets.md) into FX and local market contributions.
  - **Practical Challenges**: Handling intra-period transactions,  unsettled positions,  and missing or inconsistent data.

## 2. Leverage Attribution

### 2.1 Leverage at Portfolio and Sector Levels

- **Key Insight**: [Leverage](../../Advanced%20Investments/Lecture%206-Leverage,%20Tail%20Risk,%20Volatility%20Products.md) decisions can be made at both the [portfolio](../../Advanced%20Investments/An%20Asset%20Allocation%20Primer.md) and sector levels. Proper attribution requires separating the contributions of top-level [leverage](../../Advanced%20Investments/Lecture%206-Leverage,%20Tail%20Risk,%20Volatility%20Products.md) from sector-level exposures.

#### 2.1.1 Asset Allocation with Leverage
- **Formula**:
 $\beta^P\sum_s\left(\frac{w_s^P\beta_s^P}{\beta^P}-\frac{w_s^B\beta_s^B}{\beta^B}\right)\cdot\left(R_s^B-R^H\right)$$
  - \( \beta^P \): [Portfolio](../../Advanced%20Investments/An%20Asset%20Allocation%20Primer.md) [leverage](../../Advanced%20Investments/Lecture%206-Leverage,%20Tail%20Risk,%20Volatility%20Products.md).
  - \( \beta^B \): Benchmark [leverage](../../Advanced%20Investments/Lecture%206-Leverage,%20Tail%20Risk,%20Volatility%20Products.md).
  - \( w_s^P \): [Portfolio](../../Advanced%20Investments/An%20Asset%20Allocation%20Primer.md) weight in sector \(s\).
  - \( w_s^B \): Benchmark weight in sector \(s\).
  - \( R_s^B \): Benchmark return for sector \(s\).
  - \( R^H \): Hurdle return.

#### 2.1.2 Sector Management with Leverage
- **Formula**:
 $\sum_{s}w_{s}^{P}\beta_{s}^{P}\cdot\left(R_{s}^{P}-R_{s}^{B}\right)$$
  - \( \beta_s^P \): Sector [leverage](../../Advanced%20Investments/Lecture%206-Leverage,%20Tail%20Risk,%20Volatility%20Products.md) in the [portfolio](../../Advanced%20Investments/An%20Asset%20Allocation%20Primer.md).
  - \( R_s^P \): [Portfolio](../../Advanced%20Investments/An%20Asset%20Allocation%20Primer.md) return for sector \(s\).

#### 2.1.3 Diversification Term
- **Formula**:
 $\left(\sum_{s}w_{s}^{P}\beta_{s}^{P}-\beta^{P}\frac{\sum_{s}w_{s}^{B}\beta_{s}^{B}}{\beta^{B}}\right)\cdot R^{H}$$
  - Captures the effect of non-linear aggregation of [leverage](../../Advanced%20Investments/Lecture%206-Leverage,%20Tail%20Risk,%20Volatility%20Products.md) across sectors.
  - If [leverage](../../Advanced%20Investments/Lecture%206-Leverage,%20Tail%20Risk,%20Volatility%20Products.md) aggregates linearly (\( \beta^P = \sum_s w_s^P \beta_s^P \)),  this term vanishes.

### 2.2 Practical Implications of Leverage Attribution

1. **Linear vs. Non-Linear Aggregation**:
   - If [leverage](../../Advanced%20Investments/Lecture%206-Leverage,%20Tail%20Risk,%20Volatility%20Products.md) aggregates non-linearly (e.g.,  due to risk diversification),  the diversification term becomes significant.
   - Positive [diversification effects](../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20III%20THE%20PLAYERS/Chapter%2011%20-%20Individual%20Investors-A%20Survey%20of%20Modern%20Investment%20Theory/The%20Modern%20Portfolio%20Theory%20and%20the%20Capm.md) occur when the [portfolio](../../Advanced%20Investments/An%20Asset%20Allocation%20Primer.md) benefits from uncorrelated sector exposures.

1. **Hurdle Return**:
   - The hurdle return (\( R^H \)) represents the minimum return required to justify [leverage](../../Advanced%20Investments/Lecture%206-Leverage,%20Tail%20Risk,%20Volatility%20Products.md). Positive \( R^H \) amplifies the diversification effect.

1. **Reporting [Leverage](../../Advanced%20Investments/Lecture%206-Leverage,%20Tail%20Risk,%20Volatility%20Products.md)**:
   - [Leverage](../../Advanced%20Investments/Lecture%206-Leverage,%20Tail%20Risk,%20Volatility%20Products.md) should be reported separately to provide transparency and identify its impact on performance.

## 3. Derivative Attribution

### 3.1 Currency Derivatives

- **Purpose**: [FX forwards](../../Financial%20Instruments/Financial%20Instruments%20PSET%20Solutions.md) and swaps are typically used for [hedging currency risk](../../Clippings/Forward%20Rate.md).
- **Attribution Treatment**:
  - Remove FX hedges from local market attribution to isolate FX effects.
  - Account for:
	1. **Non-FX Return**: Return from FX hedges unrelated to [currency](../../Financial%20Instruments/Lecture%20Notes-%20Financial%20Instruments/Teaching%20Note%201-%20Forward%20Rates%20Agreement/Forwards%20and%20Futures%20Notes.md) movements.
	1. **[FX Hedging](../../Financial%20Markets/Random%20Walks%20in%20Fixed%20Income%20and%20Foreign%20Exchange/Chapter%204/Fx%20Hedging%20of%20Fixed%20Income%20-%20What%20Is%20the.md) Cash Balance Effect**: Implicit allocation to cash or [leverage](../../Advanced%20Investments/Lecture%206-Leverage,%20Tail%20Risk,%20Volatility%20Products.md) due to the mark-to-market value of FX hedges.

### 3.2 Interest Rate Derivatives

- **Purpose**: Interest rate [derivatives](../../Financial%20Markets/Financial%20Trading%20and%20Markets/Chapter%209%20Arbitrage%20and%20Hedging%20With%20Options.md),  such as government bond [futures](../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%203%20-%20Futures%20Markets/Futures%20Not%20Subject%20to%20Cash-And-Carry.md) and swaps,  are used to manage yield-curve exposures.
- **Attribution Treatment**:
  - Include [derivatives](../../Financial%20Markets/Financial%20Trading%20and%20Markets/Chapter%209%20Arbitrage%20and%20Hedging%20With%20Options.md) in yield-curve attribution but exclude them from [Asset Allocation](Lecture%202-%20[[Lecture%202-%20Asset%20Allocation%20with%20Multiple%20Risky%20Assets) with [Multiple Risky Assets](../../Advanced%20Investments/Lecture%202-%20Asset%20Allocation%20with%20Multiple%20Risky%20Assets.md)|[asset allocation](../../Advanced%20Investments/Lecture%202-%20Asset%20Allocation%20with%20Multiple%20Risky%20Assets.md)]] and security selection.
  - Account for:
	1. **Curve Outperformance**: Contribution to yield-curve [returns](../../Financial%20Markets/Financial%20Asset%20Pricing%20Theory%20Overview/Chapter%203%20-%20%20Assets,%20Portfolios,%20and%20Arbitrage/Assets.md).
	1. **Cash Balance Effect**: Implicit allocation to cash or [leverage](../../Advanced%20Investments/Lecture%206-Leverage,%20Tail%20Risk,%20Volatility%20Products.md) due to the market value of [derivatives](../../Financial%20Markets/Financial%20Trading%20and%20Markets/Chapter%209%20Arbitrage%20and%20Hedging%20With%20Options.md).
	1. **Spread Effects**: Changes in the spread between [futures](../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%203%20-%20Futures%20Markets/Futures%20Not%20Subject%20to%20Cash-And-Carry.md) prices and theoretical fair values.

### 3.3 Credit Derivatives

- **Purpose**: [Credit derivatives](../../Credit%20Markets/RISK%20NEUTRAL%20VALUATION%20FRAMEWORK%20FOR%20CREDIT%20DEFAULT%20SWAPS.md),  such as CDS and CDX,  are used to manage credit exposures.
- **Attribution Treatment**:
  - Include [credit derivatives](../../Credit%20Markets/RISK%20NEUTRAL%20VALUATION%20FRAMEWORK%20FOR%20CREDIT%20DEFAULT%20SWAPS.md) in [Asset Allocation](Lecture%202-%20[[Lecture%202-%20Asset%20Allocation%20with%20Multiple%20Risky%20Assets) with [Multiple Risky Assets](../../Advanced%20Investments/Lecture%202-%20Asset%20Allocation%20with%20Multiple%20Risky%20Assets.md)|[asset allocation](../../Advanced%20Investments/Lecture%202-%20Asset%20Allocation%20with%20Multiple%20Risky%20Assets.md)]] and security selection.
  - Explode credit indices (e.g.,  CDX) into single-issuer constituents for detailed attribution.
  - Account for:
	1. **[Credit Spread](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%2014/Cds-Equivalent%20Bond%20Spread.md) Changes**: Contribution to excess [returns](../../Financial%20Markets/Financial%20Asset%20Pricing%20Theory%20Overview/Chapter%203%20-%20%20Assets,%20Portfolios,%20and%20Arbitrage/Assets.md) over the yield curve.
	1. **Bucket [Leverage](../../Advanced%20Investments/Lecture%206-Leverage,%20Tail%20Risk,%20Volatility%20Products.md)**: Implicit [leverage](../../Advanced%20Investments/Lecture%206-Leverage,%20Tail%20Risk,%20Volatility%20Products.md) due to the basis of [returns](../../Financial%20Markets/Financial%20Asset%20Pricing%20Theory%20Overview/Chapter%203%20-%20%20Assets,%20Portfolios,%20and%20Arbitrage/Assets.md) for [credit derivatives](../../Credit%20Markets/RISK%20NEUTRAL%20VALUATION%20FRAMEWORK%20FOR%20CREDIT%20DEFAULT%20SWAPS.md).

## 4. Multi-Currency Attribution

### 4.1 FX Return Splitting

- **Formula**:
 $ {}^{b}R_{i} = F_{i} + R_{i}F_{i} + R_{i} $$
  - \( {}^{b}R_{i} \): Base [currency](../../Financial%20Instruments/Lecture%20Notes-%20Financial%20Instruments/Teaching%20Note%201-%20Forward%20Rates%20Agreement/Forwards%20and%20Futures%20Notes.md) total return.
  - \( F_{i} \): FX return.
  - \( R_{i} \): Local [currency](../../Financial%20Instruments/Lecture%20Notes-%20Financial%20Instruments/Teaching%20Note%201-%20Forward%20Rates%20Agreement/Forwards%20and%20Futures%20Notes.md) return.
  - \( R_{i}F_{i} \): Cross-term.

### 4.2 FX Allocation and Hedging

- **FX Allocation**:
 $ \sum_{c} \left({}^{b}h_{c}^{P} - {}^{b}h_{c}^{B}\right) \cdot \left(F_{c} + R_{c}^{depo} - R_{b}^{depo}\right) $$
  - \( {}^{b}h_{c}^{P} \): [Portfolio](../../Advanced%20Investments/An%20Asset%20Allocation%20Primer.md) FX exposure.
  - \( {}^{b}h_{c}^{B} \): Benchmark FX exposure.
- **[FX Hedging](../../Financial%20Markets/Random%20Walks%20in%20Fixed%20Income%20and%20Foreign%20Exchange/Chapter%204/Fx%20Hedging%20of%20Fixed%20Income%20-%20What%20Is%20the.md) Effects**:
  - Account for unintended exposures to local [interest rates](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%202/Interest%20Rate%20Quotations.md) and cash balances due to FX hedges.

### 4.3 Local Market Allocation

- **Formula**:
 $ {}^{L}R^{P} - {}^{L}R^{B} = \sum_{m} {}^{b}w_{m}^{P} \cdot \left(R_{m}^{P} - R_{m}^{depo,  P}\right) - \sum_{m} {}^{b}w_{m}^{B} \cdot \left(R_{m}^{B} - R_{m}^{depo,  B}\right) $$
  - Decomposes local market outperformance into allocation and management components.

## 5. Practical Challenges in Attribution

### 5.1 Intra-Period Transactions

- **Issue**: Transactions that settle on a forward basis create intra-period [returns](../../Financial%20Markets/Financial%20Asset%20Pricing%20Theory%20Overview/Chapter%203%20-%20%20Assets,%20Portfolios,%20and%20Arbitrage/Assets.md) and unsettled positions.
- **Solution**:
  - Report intra-period [returns](../../Financial%20Markets/Financial%20Asset%20Pricing%20Theory%20Overview/Chapter%203%20-%20%20Assets,%20Portfolios,%20and%20Arbitrage/Assets.md) separately.
  - Distinguish between settled and unsettled positions,  as only settled positions earn carry.

### 5.2 Unsettled Positions

- **Issue**: Unsettled positions earn cash [returns](../../Financial%20Markets/Financial%20Asset%20Pricing%20Theory%20Overview/Chapter%203%20-%20%20Assets,%20Portfolios,%20and%20Arbitrage/Assets.md) instead of security yields.
- **Solution**:
  - Account for the return difference (\( r^{cash} - r^{yield} \)) as carry outperformance.

### 5.3 Missing or Inconsistent Data

- **Issue**: Missing prices or discrepancies between [portfolio](../../Advanced%20Investments/An%20Asset%20Allocation%20Primer.md) and benchmark prices can distort attribution.
- **Solution**:
  - Use implied prices based on market changes to fill gaps.
  - Report [pricing](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%207/Arbitrage%20Pricing%20of%20Derivatives.md) differences as a separate source of outperformance.

## 6. Summary and Key Takeaways

### 6.1 Leverage Attribution
- Properly account for [leverage](../../Advanced%20Investments/Lecture%206-Leverage,%20Tail%20Risk,%20Volatility%20Products.md) at both the [portfolio](../../Advanced%20Investments/An%20Asset%20Allocation%20Primer.md) and sector levels.
- Report [diversification effects](../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20III%20THE%20PLAYERS/Chapter%2011%20-%20Individual%20Investors-A%20Survey%20of%20Modern%20Investment%20Theory/The%20Modern%20Portfolio%20Theory%20and%20the%20Capm.md) separately to capture non-linear aggregation of [leverage](../../Advanced%20Investments/Lecture%206-Leverage,%20Tail%20Risk,%20Volatility%20Products.md).

### 6.2 Derivative Attribution
- Treat [currency](../../Financial%20Instruments/Lecture%20Notes-%20Financial%20Instruments/Teaching%20Note%201-%20Forward%20Rates%20Agreement/Forwards%20and%20Futures%20Notes.md) and interest rate [derivatives](../../Financial%20Markets/Financial%20Trading%20and%20Markets/Chapter%209%20Arbitrage%20and%20Hedging%20With%20Options.md) as overlays,  excluding them from [Asset Allocation](Lecture%202-%20[[Lecture%202-%20Asset%20Allocation%20with%20Multiple%20Risky%20Assets) with [Multiple Risky Assets](../../Advanced%20Investments/Lecture%202-%20Asset%20Allocation%20with%20Multiple%20Risky%20Assets.md)|[asset allocation](../../Advanced%20Investments/Lecture%202-%20Asset%20Allocation%20with%20Multiple%20Risky%20Assets.md)]] and security selection.
- Include [credit derivatives](../../Credit%20Markets/RISK%20NEUTRAL%20VALUATION%20FRAMEWORK%20FOR%20CREDIT%20DEFAULT%20SWAPS.md) in regular attribution models,  exploding indices into single-issuer constituents.

### 6.3 Multi-Currency Attribution
- Decompose global [returns](../../Financial%20Markets/Financial%20Asset%20Pricing%20Theory%20Overview/Chapter%203%20-%20%20Assets,%20Portfolios,%20and%20Arbitrage/Assets.md) into FX and local market contributions.
- Account for [FX hedging](../../Financial%20Markets/Random%20Walks%20in%20Fixed%20Income%20and%20Foreign%20Exchange/Chapter%204/Fx%20Hedging%20of%20Fixed%20Income%20-%20What%20Is%20the.md) effects,  including unintended exposures to local [interest rates](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%202/Interest%20Rate%20Quotations.md) and cash balances.

### 6.4 Practical Recommendations
1. **Report [Leverage](../../Advanced%20Investments/Lecture%206-Leverage,%20Tail%20Risk,%20Volatility%20Products.md) and [Derivatives](../../Financial%20Markets/Financial%20Trading%20and%20Markets/Chapter%209%20Arbitrage%20and%20Hedging%20With%20Options.md) Separately**:
   - Provide transparency into their contributions to performance.
1. **Handle Intra-Period Transactions**:
   - Capture intra-period [returns](../../Financial%20Markets/Financial%20Asset%20Pricing%20Theory%20Overview/Chapter%203%20-%20%20Assets,%20Portfolios,%20and%20Arbitrage/Assets.md) and unsettled positions accurately.
1. **Address Missing Data**:
   - Use implied prices and report [pricing](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%207/Arbitrage%20Pricing%20of%20Derivatives.md) differences separately.

By adopting these advanced attribution techniques,  [portfolio](../../Advanced%20Investments/An%20Asset%20Allocation%20Primer.md) managers can optimize risk-adjusted [returns](../../Financial%20Markets/Financial%20Asset%20Pricing%20Theory%20Overview/Chapter%203%20-%20%20Assets,%20Portfolios,%20and%20Arbitrage/Assets.md),  enhance decision-making,  and achieve superior performance outcomes.
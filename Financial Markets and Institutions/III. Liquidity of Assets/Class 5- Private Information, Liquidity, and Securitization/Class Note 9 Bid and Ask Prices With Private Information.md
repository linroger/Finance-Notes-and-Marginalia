---
cssclasses:
  - academia
title: Class Note 9 Bid and Ask Prices With Private Information
tags:
  - adverse_selection
  - bid_ask_spread
  - liquidity_traders
  - market_makers
  - private_information
aliases:
  - Adverse Selection
  - Bid and Ask
  - Glosten-Milgrom
  - Market Maker
key_concepts:
  - Bid-Ask Spread
  - Informed vs. Liquidity Traders
  - Market Maker Profits
  - Private Information Impact
  - Risk Neutrality Assumption
---

# Class Note 9 Bid and Ask Prices With Private Information

**[[Class Note 9 Bid and Ask Prices With Private Information|Bid and Ask]] Prices with [[Class Note 9 Bid and Ask Prices With Private Information|Adverse Selection]]/Private Information**
Based on *The Only Game in Town* by [[Class Note 9 Bid and Ask Prices With Private Information|Glosten-Milgrom]].

### I. **The Setup**

1. **Two types of trader: informed and [[Class Note 10 Liquidity and Class Note 10 Liquidity and Liquidity Managementliquidity management|liquidity]]**
   (can lump the "misinformed" of *The Only Game in Town* together with the uninformed).
   All traders and market makers are [[Teaching Note 7-Exotic Options And Derivative Pricing By Monte Carlo Simulation|risk neutral]],  so there is no risk premium.

   a. **Simple private information**:

   [[Bid-Ask Prices with Adverse SelectionPrivate Information|Informed traders]] know exactly what the firm will be worth on some fixed date in the future.

   - $V$ is the unknown value. Everyone knows $V$ will be either 0 or 1,  and the informed know which of the values will occur.
   - The uninformed [[Bid-Ask Prices with Adverse SelectionPrivate Information|liquidity traders]] start out believing that the probability that $V = 1$ is $\frac{1}{2}$ (and the same for $V = 0$).

   b. Each instant,  at most one trade comes in,  and we assume all trades are the same size

   (abstracts from block trading). This means at each instant,  at most one trader either gets private information about $V$ (and then has a reason to speculate) or finds out about his (or her) need for [[Class Note 10 Liquidity and Class Note 10 Liquidity and Liquidity Managementliquidity management|liquidity]] (implying a non-speculative reason to buy or sell).

	c. **[[Bid-Ask Prices with Adverse SelectionPrivate Information|Informed traders]] buy when stock is underpriced at the ask,  sell when overpriced at the bid** (and do nothing if value is between the bid and the ask).

   - [[Bid-Ask Prices with Adverse SelectionPrivate Information|Liquidity traders]] buy when they have excess [[Class Note 10 Liquidity and Class Note 10 Liquidity and Liquidity Managementliquidity management|liquidity]] (money to invest) and sell when they need [[Class Note 10 Liquidity and Class Note 10 Liquidity and Liquidity Managementliquidity management|liquidity]].
   The need for [[Class Note 10 Liquidity and Class Note 10 Liquidity and Liquidity Managementliquidity management|liquidity]] is not related to the value of the stock or the private information that they do not have.
   Half of all [[Bid-Ask Prices with Adverse SelectionPrivate Information|liquidity traders]] buy,  and the other half sell. Any given [[Class Note 10 Liquidity and Class Note 10 Liquidity and Liquidity Managementliquidity management|liquidity]] trader buys with probability $\frac{1}{2}$.

   - A trader buys one share if he buys and sells one if he sells.
   We abstract from block trading and note that introducing risk aversion would result in a limit to the size of trades made by even very well-[[Bid-Ask Prices with Adverse SelectionPrivate Information|informed traders]].

   d. **The [[Chapter 3-Comparative Advantage, Competitiveness, and the Terms of Trade|competitive]] market makers earn zero monopoly profits and break even on average across trades**.

   - Market makers do not observe the private information of the [[Bid-Ask Prices with Adverse SelectionPrivate Information|informed traders]].
   As a result,  market makers lose money when trading with the informed.

   - The [[Class Note 9 Bid and Ask Prices With Private Information|market maker]] sets prices first,  then traders can choose the type of trade they want at the fixed price.
   To break even,  market makers set a [[Bid Ask and Transaction Prices in a Specialist Market With Heterogeneously Informed Traders|bid-ask spread]]. This implies that they make money from trades with [[Bid-Ask Prices with Adverse SelectionPrivate Information|liquidity traders]].
   The competitive break-even condition implies that the average loss to [[Bid-Ask Prices with Adverse SelectionPrivate Information|informed traders]] is equal to the average profit from [[Class Note 10 Liquidity and Class Note 10 Liquidity and Liquidity Managementliquidity management|liquidity]]-motivated trades.

   - **The [[Class Note 9 Bid and Ask Prices With Private Information|market maker]] cannot distinguish between [[Class Note 10 Liquidity and Class Note 10 Liquidity and Liquidity Managementliquidity management|liquidity]] trades and information trades**
   and must quote a single [[Class Note 9 Bid and Ask Prices With Private Information|bid and ask]] price pair. Break-even on average implies that:

	  1. The bid is the expected value of the stock given public information and the fact that a sell order arrives this instant.
	  1. The ask is the expected value of the stock given all public information and the fact that a buy order arrives this instant.

	  For example,  if there are no [[Bid-Ask Prices with Adverse SelectionPrivate Information|informed traders]],  the [[Class Note 9 [[Class Note 9 Bid and Ask Prices With Private Information|Bid and Ask]] Prices With Private Information|[[Bid Ask and Transaction Prices in a Specialist Market With Heterogeneously Informed Traders|bid-ask spread]]]] is zero.

	  If there are only [[Bid-Ask Prices with Adverse SelectionPrivate Information|informed traders]],  there is no [[Class Note 9 [[Class Note 9 Bid and Ask Prices With Private Information|Bid and Ask]] Prices With Private Information|[[Bid Ask and Transaction Prices in a Specialist Market With Heterogeneously Informed Traders|bid-ask spread]]]] that allows the [[Class Note 9 Bid and Ask Prices With Private Information|market maker]] to break even,  because he loses on all trades to [[Bid-Ask Prices with Adverse SelectionPrivate Information|informed traders]].

---

### II. **One Period Example**

1. Absent a trade,  the price of the stock would be $\frac{1}{2}$
   because there is a 50-50 chance of being worth 1 or 0.
   If no [[Bid-Ask Prices with Adverse SelectionPrivate Information|informed traders]] existed,  this would be the price,  with no spread.
   This represents the "grand mean" average value of the stock.

1. $\frac{1}{2}$ of all traders are informed (more than in reality),  $\frac{1}{2}$ are uninformed.
   This means that when an order comes in,  the probability it is an informed trade is $\frac{1}{2}$.

1. **Ask price determination**
   If a buy order comes in,  and it is from an informed trader,  it must be that the private information is that the stock is worth 1 (otherwise the informed trader would sell),  and the [[Class Note 9 Bid and Ask Prices With Private Information|market maker]] will make a "profit" of:
   $$ \text{ask} - 1 = \text{loss of } 1 - \text{ask}. $$

   If the buy is from a [[Class Note 10 Liquidity and Class Note 10 Liquidity and Liquidity Managementliquidity management|liquidity]] trader,  the stock is equally likely to be worth 0 as 1,  so the average profit from the trade is:

   $$ \text{ask} - \left(\frac{1}{2} \times 1 + \frac{1}{2} \times 0\right) = \text{ask} - \frac{1}{2}. $$

   The average profit is the average of these two "profits,  " so break-even is when:

   $$ \frac{1}{2} \times (\text{ask} - 1) + \frac{1}{2} \times (\text{ask} - \frac{1}{2}) = 0,             $$

   or $\text{ask} = \frac{3}{4}$.

   (Equivalently,  $\frac{3}{4}$ is the expected value of the stock given a buy order).

1. **Bid price determination**
   If a sell order comes in,  and it is from an informed trader,  it must be that the private information is that the stock is worth 0 (otherwise the informed trader would buy),  and the [[Class Note 9 Bid and Ask Prices With Private Information|market maker]] will make a "profit" of:
   $$ 0 - \text{bid} = \text{loss of bid} - 0. $$

   If the sell is from a [[Class Note 10 Liquidity and Class Note 10 Liquidity and Liquidity Managementliquidity management|liquidity]] trader,  the stock is equally likely to be worth 0 as 1,  so the average profit from the trade is:

   $$ \left(\frac{1}{2} \times 1 + \frac{1}{2} \times 0\right) - \text{bid} = \frac{1}{2} - \text{bid}. $$

   A similar calculation to that for the ask price,  but for the bid price solves:

   $$ \frac{1}{2} \times (0 - \text{bid}) + \frac{1}{2} \times \left(\frac{1}{2} - \text{bid}\right) = 0,             $$

   or $\text{bid} = \frac{1}{4}$.

   (Equivalently,  $\frac{1}{4}$ is the expected value of the stock given a sell order).

1. A positive [[Class Note 9 [[Class Note 9 Bid and Ask Prices With Private Information|Bid and Ask]] Prices With Private Information|[[Bid Ask and Transaction Prices in a Specialist Market With Heterogeneously Informed Traders|bid-ask spread]]]] is due to the losses to informed trading.
   It also makes the price reveal and reflect some of the private information of [[Bid-Ask Prices with Adverse SelectionPrivate Information|informed traders]].
   If the first trade were a buy (at the ask of $\frac{3}{4}$),  then $\frac{3}{4}$ would be the transaction price,  and would be the "baseline" for the next transaction.
   The new ask would be above $\frac{3}{4}$,  and the new bid above $\frac{1}{4}$.
   Trade by [[Bid-Ask Prices with Adverse SelectionPrivate Information|informed traders]] makes the price adjust toward the value that is not yet known to the public.

---

### III. **Results**

- **Private information reduces [[Class Note 10 Liquidity and Class Note 10 Liquidity and Liquidity Managementliquidity management|liquidity]]**.
   The larger the fraction of [[Bid-Ask Prices with Adverse SelectionPrivate Information|informed traders]],  the larger the [[Bid Ask and Transaction Prices in a Specialist Market With Heterogeneously Informed Traders|bid-ask spread]],  but the quicker the price reflects the private information.

- **Private information implies that buying or selling a security will move the price**,
   even if you have no information and the market is competitive.

- **[[Chapter 12 Market Efficiency|Market efficiency]]** is consistent with the ability to make money by trading if you have private information (but it is often difficult to tell if you have information that is really private!).
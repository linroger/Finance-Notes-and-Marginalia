---
linter-yaml-title-alias: GOVERNMENT OF CANADA BOND FUTURES
title: Carry Trade
tags:
  - arbitrage
  - carry_trade
  - futures_market
  - market_neutral
  - spot_market
aliases:
  - Cash-and-Carry
  - Reverse Carry Trade
key_concepts:
  - Arbitrage strategy
  - Contango and backwardation
  - Futures vs spot prices
  - Market neutral strategy
  - Profit from price spread
---

[Lecture Note 1- Forward Rates Agreement](Lecture%20Note%201-%20Forward%20Rates%20Agreement.md)
[Teaching Note 2-[Futures Contracts](../../../Financial%20Engineering/Mathematics%20of%20the%20Financial%20Markets.md)](Teaching%20Note%202-[Futures](../../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%203%20-%20Futures%20Markets/Futures%20Not%20Subject%20to%20Cash-And-Carry.md)%20Contracts.md)
[Currency]([Forwards%20and%20Futures%20Notes) Forward]([Currency](Forwards%20and%20Futures%20Notes.md)%20Forward.md)

[Carry Trade]([[Currency%20Carry%20Trade)]]
	- [Introduction](Ch1%20[[Squam%20Lake%20Group%20Introduction) to Derivative Markets]]
	- [Hedging](Chapter%206%20(Hull)%20[[Key%20Rates%20O1s%20Durations%20and%20Hedging) Strategies with [Forwards](../../../Financial%20Markets/Financial%20Asset%20Pricing%20Theory%20Overview/Chapter%2012%20-%20Derivatives/Forwards%20and%20Futures.md)]]
	- [Forward Exchange Rate](Deriving%20[[A%20Primer%20on%20Currency%20Derivatives) Numerical Example]]
	- [Secondary Commodities](Primary%20vs.%20[[Primary%20vs.%20Secondary%20Commodities)]]
	- [Foreign Exchange Quoting Conventions](Foreign%20Exchange%20Quoting%20Conventions.md)
	- [Forward Contracts on Exchange Rates](Forward%20Contracts%20on%20Exchange%20Rates.md)
	- [Forwards and Futures]([[Forward%20and%20Futures%20Contracts) Notes]]
	- [Hedging]([[Key%20Rates%20O1s%20Durations%20and%20Hedging) Strategies with [Forwards](../../../Financial%20Markets/Financial%20Asset%20Pricing%20Theory%20Overview/Chapter%2012%20-%20Derivatives/Forwards%20and%20Futures.md)]]
	- [Financial Instruments]([[A%20Practical%20Guide%20for%20Actuaries%20and%20other%20Business%20Professionals.)/Lecture Notes/Teaching Note 1- Forward Rates Agreement/[Interest Rates](../../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%202/Interest%20Rate%20Quotations.md),     Carry Trades,     and Exchange Rate Movements]]
	- [Teaching Note 1 Forward Rates Agreement](Teaching%20Note%201%20Forward%20Rates%20Agreement)

## WHAT IS A CARRY TRADE?

A [Interest Rates]([Interest%20Rate%20Quotations),  Carry Trades,  and Exchange Rate Movements](Asset%20Classes/[Derivatives](../../../Financial%20Markets/Financial%20Trading%20and%20Markets/Chapter%209%20Arbitrage%20and%20Hedging%20With%20Options.md)/Forward%20and%20Futures/Forward%20Exchange%20Rate%20Contracts/Foreign%20Exchange%20Notes/Interest%20Rates,  %20Carry%20Trades,  %20and%20Exchange%20Rate%20Movements.md) is a form of [arbitrage](../../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%207/Arbitrage%20Pricing%20of%20Derivatives.md) that takes advantage of price discrepancies between [futures](../../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%203%20-%20Futures%20Markets/Futures%20Not%20Subject%20to%20Cash-And-Carry.md) and [spot prices](Contango%20And%20Backwardation%20In%20Arbitrage-Free%20Futures-Markets.md). When performing a [Interest Rates]([Interest%20Rate%20Quotations),  Carry Trades,  and Exchange Rate Movements](Asset%20Classes/[Derivatives](../../../Financial%20Markets/Financial%20Trading%20and%20Markets/Chapter%209%20Arbitrage%20and%20Hedging%20With%20Options.md)/Forward%20and%20Futures/Forward%20Exchange%20Rate%20Contracts/Foreign%20Exchange%20Notes/Interest%20Rates,  %20Carry%20Trades,  %20and%20Exchange%20Rate%20Movements.md),  the trader will take a position in the spot market and simultaneously take the opposite position in the [futures](../../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%203%20-%20Futures%20Markets/Futures%20Not%20Subject%20to%20Cash-And-Carry.md) market. Since one leg makes money as the other loses money,  the strategy is referred to as “market neutral.” When trading a market-neutral strategy,  the trader doesn’t care which direction the [underlying asset](../../Financial%20Derivatives%20and%20Quantitative%20Methods/Risk%20Neutral%20Pricing%20of%20Options.md)’s price moves. 

The strategy’s profitability relies on the fact that [futures contracts](../../../Financial%20Engineering/Mathematics%20of%20the%20Financial%20Markets.md) are often priced above or below the spot price. A [futures](../../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%203%20-%20Futures%20Markets/Futures%20Not%20Subject%20to%20Cash-And-Carry.md) contract’s price represents a market’s perception of where its [underlying asset](../../Financial%20Derivatives%20and%20Quantitative%20Methods/Risk%20Neutral%20Pricing%20of%20Options.md) is heading by its settlement date. Therefore,  [futures](../../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%203%20-%20Futures%20Markets/Futures%20Not%20Subject%20to%20Cash-And-Carry.md) prices often drift from the current spot price,  presenting an opportunity to profit with relatively little risk. 

When the spot price is below the [futures price](../../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%2011/Futures%20Price%20and%20the%20Quality%20Option%20Before%20E.md),  the market is said to be in _contango_,  and a [Interest Rates]([Interest%20Rate%20Quotations),  Carry Trades,  and Exchange Rate Movements](Asset%20Classes/[Derivatives](../../../Financial%20Markets/Financial%20Trading%20and%20Markets/Chapter%209%20Arbitrage%20and%20Hedging%20With%20Options.md)/Forward%20and%20Futures/Forward%20Exchange%20Rate%20Contracts/Foreign%20Exchange%20Notes/Interest%20Rates,  %20Carry%20Trades,  %20and%20Exchange%20Rate%20Movements.md) will often result in profits. When the opposite is true,  the market is said to be in _backwardation_,  and a reverse [Interest Rates]([Interest%20Rate%20Quotations),  Carry Trades,  and Exchange Rate Movements](Asset%20Classes/[Derivatives](../../../Financial%20Markets/Financial%20Trading%20and%20Markets/Chapter%209%20Arbitrage%20and%20Hedging%20With%20Options.md)/Forward%20and%20Futures/Forward%20Exchange%20Rate%20Contracts/Foreign%20Exchange%20Notes/Interest%20Rates,  %20Carry%20Trades,  %20and%20Exchange%20Rate%20Movements.md) (i.e.,  [shorting](../../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%202%20-%20Spot%20Markets/Short%20Selling.md) in the spot market and longing the [futures](../../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%203%20-%20Futures%20Markets/Futures%20Not%20Subject%20to%20Cash-And-Carry.md) contract) will be a more favorable strategy. 

When performing a [Interest Rates]([Interest%20Rate%20Quotations),  Carry Trades,  and Exchange Rate Movements](Asset%20Classes/[Derivatives](../../../Financial%20Markets/Financial%20Trading%20and%20Markets/Chapter%209%20Arbitrage%20and%20Hedging%20With%20Options.md)/Forward%20and%20Futures/Forward%20Exchange%20Rate%20Contracts/Foreign%20Exchange%20Notes/Interest%20Rates,  %20Carry%20Trades,  %20and%20Exchange%20Rate%20Movements.md),  a trader will look for as wide a spread as possible between the spot price and [futures price](../../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%2011/Futures%20Price%20and%20the%20Quality%20Option%20Before%20E.md). As settlement approaches,  this spread will naturally narrow because the time in which the spot price can increase or decrease reduces. By settlement,  the two prices will have converged. The trader can close both positions for a profit whenever the spread is narrower than it was at entry. 

Alternatively,  a trader who settles the [futures](../../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%203%20-%20Futures%20Markets/Futures%20Not%20Subject%20to%20Cash-And-Carry.md) leg of a [Interest Rates]([Interest%20Rate%20Quotations),  Carry Trades,  and Exchange Rate Movements](Asset%20Classes/[Derivatives](../../../Financial%20Markets/Financial%20Trading%20and%20Markets/Chapter%209%20Arbitrage%20and%20Hedging%20With%20Options.md)/Forward%20and%20Futures/Forward%20Exchange%20Rate%20Contracts/Foreign%20Exchange%20Notes/Interest%20Rates,  %20Carry%20Trades,  %20and%20Exchange%20Rate%20Movements.md) can opt to “roll over” their trade to a later-dated [futures](../../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%203%20-%20Futures%20Markets/Futures%20Not%20Subject%20to%20Cash-And-Carry.md) contract. If there is a wide spread between the spot price and a longer-term contract when closing the first [futures](../../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%203%20-%20Futures%20Markets/Futures%20Not%20Subject%20to%20Cash-And-Carry.md) position,  simply [shorting](../../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%202%20-%20Spot%20Markets/Short%20Selling.md) the further out contract and continuing to hold the spot position will create a new [Interest Rates]([Interest%20Rate%20Quotations),  Carry Trades,  and Exchange Rate Movements](Asset%20Classes/[Derivatives](../../../Financial%20Markets/Financial%20Trading%20and%20Markets/Chapter%209%20Arbitrage%20and%20Hedging%20With%20Options.md)/Forward%20and%20Futures/Forward%20Exchange%20Rate%20Contracts/Foreign%20Exchange%20Notes/Interest%20Rates,  %20Carry%20Trades,  %20and%20Exchange%20Rate%20Movements.md) with a new settlement date.

---
#### REVERSE CASH-AND-CARRY ARBITRAGE

A reverse [cash-and-carry arbitrage](../../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%2015/Dollar%20Rolls.md) is the exact opposite to a cash-and –carry transaction. Instead of buying the underlying security because it is underpriced,  you sell it short (because it is overpriced),  take the proceeds and go long a [futures](../../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%203%20-%20Futures%20Markets/Futures%20Not%20Subject%20to%20Cash-And-Carry.md) position on the underlying security. Before the [futures](../../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%203%20-%20Futures%20Markets/Futures%20Not%20Subject%20to%20Cash-And-Carry.md) position expires you close out the position by taking delivery and returning the borrowed shares you were short.

---
# Carry Trade

## MONTRÉAL EXCHANGE: CASH-AND-CARRY TRADE

A bond trader notes that the price relationship between the CTD Can 2% December 1,  2051 bond and the LGB contract is out-of-line.

The trader’s observation is supported by:

1. An actual repo rate (0.20%) that is lower than the repo rate (1.85%) implied by the price of the LGB contract—a condition that provides a trader an [arbitrage](../../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%207/Arbitrage%20Pricing%20of%20Derivatives.md) profit by initiating a [cash-and-carry](.md) trade (whereby the trader sells bond [futures](../../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%203%20-%20Futures%20Markets/Futures%20Not%20Subject%20to%20Cash-And-Carry.md) and finances the purchase of the cash bond at a rate below the rate implied by the [futures price](../../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%2011/Futures%20Price%20and%20the%20Quality%20Option%20Before%20E.md)). The bond is then held until it is delivered to fulfill the obligation of the sale of the [futures](../../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%203%20-%20Futures%20Markets/Futures%20Not%20Subject%20to%20Cash-And-Carry.md) contract; and
1. A net basis (basis after carry) reflecting that the actual LGB contract is overpriced relative to its theoretical fair value.

| Specification | Value |
| ---- | ---- |
| Last Delivery Day | 2022-03-31 |
| Price of LGB Contract | 220.72 |
| Valuation Date | 2021-11-18 |
| Coupon | 2% |
| Maturity | December 2051 |
| Bond Price | 98.964 |
| Conversion Factor | 0.4481 |
| [Implied Repo](../../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%2011/Implied%20Repo%20Rates.md) | 1.85% |
| Actual Repo | 0.20% |
| Net Basis | -0.595 |
|  |  |

| Setting                                           | Value      |
|---------------------------------------------------|------------|
| Price of the CTD Can 2% December 1,     2051 bond     | 98.964     |
| [Accrued interest](../../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%202%20-%20Spot%20Markets/Intra-Year%20Compounding%20and%20Day-Count.md): (170/365) x 2                   | 0.932      |
| (170 days = June 1 to November 18 settlement date)|            |
| Financing rate (actual repo rate)                 | 0.20%      |
| Conversion factor                                 | 0.4481     |
| Price of the LGB contract                         | 220.72     |
| Days from settlement to [futures](../../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%203%20-%20Futures%20Markets/Futures%20Not%20Subject%20to%20Cash-And-Carry.md) delivery          | 133        |
| (November 18 to March 31)                        |            |
| Days from next coupon to [futures](../../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%203%20-%20Futures%20Markets/Futures%20Not%20Subject%20to%20Cash-And-Carry.md) delivery         | 120        |
| (December 1 to March 31)                          |            |

### LGB MARCH 2022

- **Last Delivery Day:** 2022-03-31
- **Price of LGB Contract:** 220.72
- **Valuation Date:** 2021-11-18

#### COUPON MATURITY BOND PRICE
- **Conversion Factor:** 0.4481
- **[Implied Repo](../../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%2011/Implied%20Repo%20Rates.md):** 1.85%
- **Actual Repo:** 0.20%
- **Net Basis:** -0.595

#### SETTING

- **Price of the CTD Can 2% December 1,  2051 bond:** 98.964
- **[Accrued interest](../../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%202%20-%20Spot%20Markets/Intra-Year%20Compounding%20and%20Day-Count.md):** (170/365) x 2 (170 days = June 1 to November 18 settlement date)
- **Financing rate (actual repo rate):** 0.20%
- **Conversion factor:** 0.4481
- **Price of the LGB contract:** 220.72
- **Days from settlement to [futures](../../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%203%20-%20Futures%20Markets/Futures%20Not%20Subject%20to%20Cash-And-Carry.md) delivery (November 18 to March 31):** 133
- **Days from next coupon to [futures](../../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%203%20-%20Futures%20Markets/Futures%20Not%20Subject%20to%20Cash-And-Carry.md) delivery (December 1 to March 31):** 120

The trader initiates a [cash-and-carry](.md) trade that involves the following steps:

1. Pay for the purchase of the CTD bond (bond price + [accrued interest](../../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%202%20-%20Spot%20Markets/Intra-Year%20Compounding%20and%20Day-Count.md)).
1. Finance the bond purchase at the current [short-term financing](../../../Financial%20Markets%20and%20Institutions/III.%20Liquidity%20of%20Assets/Class%207-%20CP,%20Repo,%20and%20the%20Crisis/Asset%20Backed%20Commercial%20Paper%20Understanding%20the%20Risks.md) rate (actual repo rate).
1. Receive any intervening coupon plus reinvestment income during the life of the [futures](../../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%203%20-%20Futures%20Markets/Futures%20Not%20Subject%20to%20Cash-And-Carry.md) contract.
1. Receive the [futures](../../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%203%20-%20Futures%20Markets/Futures%20Not%20Subject%20to%20Cash-And-Carry.md) [invoice price](../../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%201/Accrued%20Interest.md) + intervening coupon [accrued interest](../../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%202%20-%20Spot%20Markets/Intra-Year%20Compounding%20and%20Day-Count.md) from delivering the bond (i.e.,  collect the anticipated receipt from delivering bond to the buyer).
1. Repay the cash amount borrowed to purchase the CTD bond + interest.
1. Calculate [arbitrage](../../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%207/Arbitrage%20Pricing%20of%20Derivatives.md) profit.

### CASH-AND-CARRY TRANSACTION AMOUNT

(per$100,  000.00 notional amount)

- **Purchase the CTD bond:**$98,    964 +$932 =$99,  896 (Price of bond + [Accrued interest](../../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%202%20-%20Spot%20Markets/Intra-Year%20Compounding%20and%20Day-Count.md))
- **Financing costs until LGB delivery:**$99,    896 x 0.0020 x 133/365 =$73 (Amount borrowed to buy bond × [Short-term financing](../../../Financial%20Markets%20and%20Institutions/III.%20Liquidity%20of%20Assets/Class%207-%20CP,%20Repo,%20and%20the%20Crisis/Asset%20Backed%20Commercial%20Paper%20Understanding%20the%20Risks.md) rate × Number of days/365)
- **Income during the life of the LGB contract:**$1,    000 + ($1,  000 x 0.0020 x 120/365) = C$1,  001 ([Coupon income](../../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%203/Pl%20Attribution.md) + ([Coupon income](../../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%203/Pl%20Attribution.md) × [Short-term financing](../../../Financial%20Markets%20and%20Institutions/III.%20Liquidity%20of%20Assets/Class%207-%20CP,%20Repo,%20and%20the%20Crisis/Asset%20Backed%20Commercial%20Paper%20Understanding%20the%20Risks.md) rate × Number of days/365))
- **Total costs of the bond position:**$99,    896 +$73 -$1,    001 = C$98,  968 ([Investment](../../../Advanced%20Investments/An%20Asset%20Allocation%20Primer.md) + Financing - Income)

### DELIVERY PRICE OF THE DELIVERABLE BOND AT LGB FUTURES DELIVERY

($220,    720 x 0.4481) +$658* =$99,    563 (*$100,  000 x 2% coupon x 30/365)

- [Futures](../../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%203%20-%20Futures%20Markets/Futures%20Not%20Subject%20to%20Cash-And-Carry.md) [invoice price](../../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%201/Accrued%20Interest.md) × Conversion factor + [Accrued interest](../../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%202%20-%20Spot%20Markets/Intra-Year%20Compounding%20and%20Day-Count.md) received by the seller from the bond buyer

### ARBITRAGE PROFIT (PER LGB FUTURES)
$99,    563 -$98,  968 =$595 (Delivery price of the deliverable bond - Total costs of the bond position)

In the present strategy the [cash-and-carry](.md) transaction results in a profit of$595 per contract.

# CASH-AND-CARRY TRANSACTION

(per$100,  000.00 notional amount)

| Item                                   | AMOUNT                                      | COMMENTS                                                        |
|----------------------------------------|---------------------------------------------|-----------------------------------------------------------------|
| Purchase the CTD bond                  |$98,    964 +$932 =$99,    896                    | Price of bond + [Accrued interest](../../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%202%20-%20Spot%20Markets/Intra-Year%20Compounding%20and%20Day-Count.md)                                |
| Financing costs until LGB delivery     |$99,    896 x 0.0020 x 133/365 =$73            | Amount borrowed to buy bond × [Short-term financing](../../../Financial%20Markets%20and%20Institutions/III.%20Liquidity%20of%20Assets/Class%207-%20CP,%20Repo,%20and%20the%20Crisis/Asset%20Backed%20Commercial%20Paper%20Understanding%20the%20Risks.md) rate × Number of days/365 |
| Income during the life of the LGB contract (credit and reinvestment of the coupon: December 1 to March 31) |$1000 + ($1000 x 0.0020 x 120/365) = C$1001 | [Coupon income](../../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%203/Pl%20Attribution.md) + ([Coupon income](../../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%203/Pl%20Attribution.md) × [Short-term financing](../../../Financial%20Markets%20and%20Institutions/III.%20Liquidity%20of%20Assets/Class%207-%20CP,%20Repo,%20and%20the%20Crisis/Asset%20Backed%20Commercial%20Paper%20Understanding%20the%20Risks.md) rate × Number of days/365) |
| Total costs of the bond position       |$99,    896 +$73 -$1001 = C$98,    968            | [Investment](../../../Advanced%20Investments/An%20Asset%20Allocation%20Primer.md) + Financing - Income                                 |
| Delivery price of the deliverable bond at LGB [futures](../../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%203%20-%20Futures%20Markets/Futures%20Not%20Subject%20to%20Cash-And-Carry.md) delivery | ($220,    720 x 0.4481) +$658* =$99,    563       | [Futures](../../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%203%20-%20Futures%20Markets/Futures%20Not%20Subject%20to%20Cash-And-Carry.md) [invoice price](../../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%201/Accrued%20Interest.md) × Conversion factor + [Accrued interest](../../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%202%20-%20Spot%20Markets/Intra-Year%20Compounding%20and%20Day-Count.md) received by the seller from the bond buyer |
| [Arbitrage](../../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%207/Arbitrage%20Pricing%20of%20Derivatives.md) profit (per LGB [futures](../../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%203%20-%20Futures%20Markets/Futures%20Not%20Subject%20to%20Cash-And-Carry.md))     |$99,    563 -$98,    968 =$595                    | Delivery price of the deliverable bond - Total costs of the bond position |

- $100,  000 x 2% coupon x 30/365
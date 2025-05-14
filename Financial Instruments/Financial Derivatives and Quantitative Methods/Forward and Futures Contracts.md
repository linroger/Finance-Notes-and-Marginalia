---
title: Forward and Futures Contracts
tags:
  - arbitrage
  - derivative_pricing
  - forward_contracts
  - futures_contracts
  - hedging
aliases:
  - Derivatives
  - Forwards and Futures
  - Hull Chapters 1, 2, 5
key_concepts:
  - Arbitrage
  - Forward contracts
  - Futures contracts
  - Hedging
  - Replication
---

# Forward and Futures Contracts

These notes explore forward and [[Mathematics of the Financial Markets|futures contracts]],  what they are and how they are used. We will learn how to price forward contracts by using [[Arbitrage Pricing of Derivatives|arbitrage]] and [[Forward and Futures Contracts|replication]] arguments that are fundamental to derivative [[Arbitrage Pricing of Derivatives|pricing]]. We shall also learn about the similarities and differences between forward and [[Contango And Backwardation In Arbitrage-Free Futures-Markets|futures markets]] and the differences between forward and [[Contango And Backwardation In Arbitrage-Free Futures-Markets|futures markets]] and prices. We shall also consider how forward and future prices are related to spot market prices.

Keywords: [[Arbitrage Pricing of Derivatives|Arbitrage]],  [[Forward and Futures Contracts|Replication]],  [[Key Rates O1s Durations and Hedging|Hedging]],  Synthetic,  Speculator,  Forward Value,  Maintainable Margin,  Limit Order,  Market Order,  Stop Order,  Backwardation,  Contango,  Underlying,  Derivative.

Reading: You should read Hull chapters 1 (which covers option payoffs as well) and chapters 2 and 5.

## 1 Background

From the 1970 s [[Financial Markets and Institutions Lecture Notes|financial markets]] became riskier with larger swings in [[Interest Rate Quotations|interest rates]] and equity and [[Primary vs. Secondary Commodities|commodity prices]]. In response to this increase in risk,  [[Financial Markets and Institutions Lecture Notes|financial institutions]] looked for new ways to reduce the risks they faced. The way found was the development of exchange traded [[Financial Mathematics Course|derivative securities]] [[Financial Mathematics Course|Derivative securities]] are assets linked to the payments on some underlying security or index of securities. Many [[Financial Mathematics Course|derivative securities]] had been traded over the counter for a long time but it was from this time that volume of trading activity in [[Chapter 9 Arbitrage and Hedging With Options|derivatives]] grew most rapidly

The most important types of [[Chapter 9 Arbitrage and Hedging With Options|derivatives]] are [[Futures Not Subject to Cash-And-Carry|futures]],  options and swaps. An option gives the holder the right to buy or sell the [[Risk Neutral Pricing of Options|underlying asset]] at a specified date for a pre-specified price. A future gives the holder the

Obligation to buy or sell the [[Risk Neutral Pricing of Options|underlying asset]] at a specified date for a prespecified price. Swaps allow investors to exchange cash fows and can be regarded as a [[An Asset Allocation Primer|portfolio]] of [[Mathematics of the Financial Markets|futures contracts]]

Options and [[Futures Not Subject to Cash-And-Carry|futures]] are written on a range of major stocks,  [[Hedge Fund Strategies|stock market]] indices,  major currencies,  government bonds and [[Interest Rate Quotations|interest rates]]. Most options and [[Futures Not Subject to Cash-And-Carry|futures]] in the UK are traded on the London [[Lecture Notes on International Finance|International Financial]] [[Futures Not Subject to Cash-And-Carry|Futures]] Exchange ( http://www.liffe.com/ ) and most options and [[Futures Not Subject to Cash-And-Carry|futures]] in the US are traded on the Chicago Board of Trade ( http://www.cbot.com/ ) It is also possible to trade [[Mathematics of the Financial Markets|futures contracts]] on a range of different individual stocks from across the world at Euronext ( http://www.universalstockfutures.com/ ). Such exchange traded [[Chapter 9 Arbitrage and Hedging With Options|derivatives]] might be described as off-the-peg or generic as the details of the derivative are specified by the Exchange House. Other [[Chapter 9 Arbitrage and Hedging With Options|derivatives]] are traded over the counter. They are tailor-made and designed specifically to meet the needs of individual traders the party and counter party.

[[Chapter 9 Arbitrage and Hedging With Options|Derivatives]] allow investors a great deal of fexibility and choice in determining their cash fows and thus are ideal instruments for [[Key Rates O1s Durations and Hedging|hedging]] of existing risk or speculating on the price movements of the [[Risk Neutral Pricing of Options|underlying asset]]. Thus for example it is possible to offset the risk that a stock will fall in price by buying a put option on the stock. It is possible to gain if a large change in the price of the [[Risk Neutral Pricing of Options|underlying asset]] is anticipated even if the direction of change is unknown. It is also possible by using an appropriate [[An Asset Allocation Primer|portfolio]] of options to guarantee that you buy at the lowest price and sell at the highest price — a trader's dream made reality

## 2 Forward Contracts

[[Forward and Futures Contracts|Forwards and futures]] contracts are a special type of derivative contract. Forward contracts were initially developed in agricultural markets. For exampl an orange grower faces considerable price risk because they do not know at what price their crops will sell. This may be a consequence of weather condi

Tions (frost) that will affect aggregate supply. The farmer can insure or hedge against this price risk by selling the crop forward on the forward orange concentrate market. This obligates the grower to deliver a specific quantity of orange concentrate at a specific date for a specified price. The delivery and the payment occur only at the forward date and no money changes hands initially. Farmers can,  in this way,  eliminate the price risk and be sure of the price they will get for their crop. An investor might also engage in such a [[Forward Points in Currency|forward contract]]. For an example an investor might sell orange concentrate forward for delivery in March at 120. If the price turns out to be 100,  the investor buys at 100 and delivers at 120 making a profit of 20. If the weather was bad and the price in March is 150,  the investor must buy at 150 to fulfill her obligation to supply at 120,  making a loss of 30 on each unit sold. The farmer is said to be a hedger as selling the orange concentrate forward reduces the farmer's risk. The investor on the other hand is taking a position in anticipation of his beliefs about the weather and is said to be a speculator. This terminology is standard but can be misleading. The farmer who does not hedge their price risk is really taking a speculative position and it is difficult to make a hard and fast distinction between the two types of traders.

## Why trade forward?

For an investor the [[Tba and Specified Pools Markets|forward market]] has both pros and cons. The advantage is that there is no initial [[An Asset Allocation Primer|investment]]. That is it costs nothing now to buy or sell forward. The disadvantage is that there is a change of suffering a large loss.

## The price of a forward contract

Let's consider a [[Forward Points in Currency|forward contract]] for a particular [[Risk Neutral Pricing of Options|underlying asset]],  e.g. IBM stock,  with a maturity date of $T$ .The price of such a [[Forward Points in Currency|forward contract]] is easy to determine. In the absence of any transactions or storage cost the price of the [[Forward Points in Currency|forward contract]] is the future value of the current spot price.

<table>
	<tbody>
		<tr>
			<th> </th>
			<th>$\mathbf{P}_{\mathrm{osition}}$</th>
			<th>Cost Now</th>
			<th>Payoff at Maturity</th>
		</tr>
		<tr>
			<td>$\left (\frac{1}{2}\right)$ $f$ $1^{\prime}$ 1 1 1 11</td>
			<td>Long Underlying</td>
			<td>$S_0$</td>
			<td>$S_T$</td>
		</tr>
		<tr>
			<td>$^{'}2$ 1 1</td>
			<td>[[Forward Rates Agreement|Long Forward]]</td>
			<td>0</td>
			<td>$(S_{T}-F)$</td>
		</tr>
		<tr>
			<td>3 1</td>
			<td>[[Forward Rates Agreement|Short Forward]]</td>
			<td>0</td>
			<td>$(F-S_{T})$</td>
		</tr>
		<tr>
			<td>(4) $f$ 1. </td>
			<td>Long Discount Bond</td>
			<td>$F$ $\overline{\left (1+r\right.}$</td>
			<td>$F$</td>
		</tr>
	</tbody>
</table>

Table 1: [[Forward Contracts and Forward Prices|Forward Price]]

Let $F$ be the [[Forward Contracts and Forward Prices|forward price]] and $S_{0}$ be the current spot price and let $r_{0}^{T}$ be the [[Black Scholes Derivation|risk-free rate]] of interest from now until the maturity date $T$ then
$$F=(1+r_0^T) S_0.$$

To simplify the notation denote $r_{0}^{T}$ simply by 7 .Then $F=(1+r) S_{0}$ .To see that this formula is correct,  let's consider the payoff and cost of the positions that can be taken on the stock,  the [[Forward Points in Currency|forward contract]] and a risk-free discount bond with a face value of $F$ and a maturity date of $T$ .If we take a [[Chapter 4 - Futures: Hedging and Speculation|long position]] in the stock,  the cost now is $S_{0}$ and the payoff at the maturity date is $S_{T}$ .We don’t know what $S_{T}$ will be since the payoff to the asset is uncertain. If we take a [[Chapter 4 - Futures: Hedging and Speculation|long position]] in the [[Forward Points in Currency|forward contract]],  the cost now is zero and the payoff at maturity is $S_{T}-F$ .That is we are obligated to buy at $F$ and the [[Risk Neutral Pricing of Options|underlying asset]] can be sold for $S_{T}$ .If $S_{T}>F$ ,  then we buy at $F$ and can immediately sell at $S_{T}$ for a profit of $S_{T}-F$ .If on the other hand $S_{T}<F$ then we must buy at $F$ but can only sell at $S_{T}$ so we have a loss since $S_{T}-F<0$ .In addition suppose we buy the discount bond. It costs $F/(1+r)$ now and pays out the face value $F$ at maturity. We can summarise all this information in Table 1.

Now consider the following trading strategy: go long in the [[Forward Points in Currency|forward contract]] and buy the discount bond. The payoff to the [[Forward Points in Currency|forward contract]] is $(S_{T}-F)$ ,  you are committed to buy at $F$ but can sell for $S_{T}$ ,  and the payoff to the bond is simply $F$ ,  so the total payoff is $S_{T}$ .Thus this trading strategy replicates the payoff to the [[Risk Neutral Pricing of Options|underlying asset]]. We then invoke the [[Arbitrage Pricing of Derivatives|arbitrage]] principle that since this trading strategy has the same payoff at maturity as the underling asset,  it must cost exactly the same as buying the [[Risk Neutral Pricing of Options|underlying asset]] itself. The strategy costs $F/(1+r)$ as the [[Forward Points in Currency|forward contract]] involves no

<table>
	<tbody>
		<tr>
			<th>Position</th>
			<th>Cost Now</th>
			<th>Payoff at Maturity</th>
		</tr>
		<tr>
			<td>(1) - (3)= + (4) T</td>
			<td>$S_0$</td>
			<td>$F$</td>
		</tr>
		<tr>
			<td> </td>
			<td>$F$</td>
			<td> </td>
		</tr>
		<tr>
			<td>(2) + (4) = (1)</td>
			<td>$F$ $\overline{(1+r)}$</td>
			<td>$S_T$</td>
		</tr>
		<tr>
			<td> </td>
			<td>$(1+r)$</td>
			<td>$\nu_{1}^{\prime}T$</td>
		</tr>
	</tbody>
</table>

Table 2:Forward

Initial outlay,  therefore it must be the case that $F/(1+r)=S_{0}$ or
$$F=(1+r) S_0.$$

That is,  the [[Forward Contracts and Forward Prices|forward price]] is simply the future value of the stock. The [[Chapter 4 - Futures: Hedging and Speculation|long position]] in the stock (1) is equivalent to a [[An Asset Allocation Primer|portfolio]] of a [[Chapter 4 - Futures: Hedging and Speculation|long position]] in the forward and a [[Chapter 4 - Futures: Hedging and Speculation|long position]] in the discount bond (2) + (4).

As an alternative suppose you go long in the stock and short on the [[Forward Points in Currency|forward contract]],  that is a [[An Asset Allocation Primer|portfolio]] of (1) and (3). The overall payoff at maturity is $S_{T}+(F-S_{T})=F$ .The cost of this strategy is $S_{0}$ but has the same payoff as a risk-free bond with face value of $F$ and is thus equivalent to position (4). Thus as before $F/(1+r)=S_{0}$ . This is summarised by Table 2.

As yet another possibility consider buying the underlying stock and [[Short Selling|going short]] on the discount bond with face value of $F$ (that is borrow an amount $F/(1+r)$ 0. At maturity one has an asset worth $S_{T}$ but and obligation to repay $F$ and thus a net worth of $S_{T}-F$ .This is exactly the same as the [[Forward Rates Agreement|long forward]] contract. Since the payoffs are the same we are said to have synthesized or replicated the [[Forward Points in Currency|forward contract]]. The cost of this synthetic [[Forward Points in Currency|forward contract]] is the cost of the stock now $S_{0}$ less what we borrowed,  $F/(1+r)$ ,  so that the net cost is
$$S_0-\frac{F}{(1+r)}.$$

The payoff is the same as the [[Forward Points in Currency|forward contract]]. Yet the [[Forward Points in Currency|forward contract]] involves no exchange of money upfront. So the cost of the synthetic forward must be zero too:$$S_0-\frac{F}{(1+r)}=0$$

Which again the delivers the same conclusion that $F=(1+r) S_{0}$

### Exercises

Exercise 1: If $F>(1+r) S_{0}$ identify a [[Arbitrage Pricing of Derivatives|arbitrage]] opportunity. Put togethe. A [[An Asset Allocation Primer|portfolio]] which givesyou money now and only offsetting obligations at the maturity date

Exercise 2: If $F<(1+r) S_{0}$ identify a [[Arbitrage Pricing of Derivatives|arbitrage]] opportunity. Put together a [[An Asset Allocation Primer|portfolio]] which gives you money now and only offsetting obligations at the maturity date.

Exercise 3: If the stock pays out a dividend $D$ at the maturity date 7 S 0 the total payoff to holding the stock is $S_{T}+D$，calculate the [[Forward Contracts and Forward Prices|forward price]] if the interest rate is $T$

### Forward Value

The [[Forward Points in Currency|forward contract]] is initially negotiated so that there is no initial outlay That is the delivery price on the [[Forward Points in Currency|forward contract]] is chosen so that the value of the contract is zero. However,  as maturity approaches the price of the [[Risk Neutral Pricing of Options|underlying asset]] changes but the delivery price does not. Thus as time progresses the [[Forward Points in Currency|forward contract]] may have a positive or negative value. Let $K$ be the delivery price and let $S_{t}$ denote the price of the [[Risk Neutral Pricing of Options|underlying asset]] at time $t$ with time $T-t$ left to maturity. The [[Forward Contracts and Forward Prices|forward price]] is $F_{t}=S_{t}(1+r_{t}^{T})$ where $r_{t}^{T}$ is the [[Exercises|risk-free interest rate]] from $t$ until $T$

The same argument can be used above can now be used to find how the value of the [[Forward Points in Currency|forward contract]] changes as the time moves to maturity. Let this value be $v_{t}$ .Consider the [[An Asset Allocation Primer|portfolio]] of one [[Forward Rates Agreement|long forward]] contract and the purchase of a discount bond with face value of $K$ and maturity date of $T$ The payoff to the [[Forward Points in Currency|forward contract]] is $(S_{T}-K)$ but the payoff to the bond is $K$ leaving a net payoff of $S_{T}$ . The cost of this [[An Asset Allocation Primer|portfolio]] is $v_{t}+\frac{K}{(1+r_{t}^{T})}$ .Since it replicates exactly the underlying (which has a price of $S_{t}$ ) wehave
$$v_t=S_t-\frac{K}{(1+r_t^T)}=\frac{(F_t-K)}{(1+r_t^T)}$$

Where the last part follows since $S_{t}=F_{t}/(1+r_{t}^{T^{\prime}})$ .To check that this makes sense first consider what happens at $t=0$ .At $t=0$ the delivery price is chosen so $v_{t}=0$，that is $K$ = $S_{0}( 1$ + $r_{0}^{T})$ = $F_{0}$ and the [[Forward Contracts and Forward Prices|forward price]] is equal to the delivery price. Next consider $t=T$ .Then $r_{t}^{T}=0$ andwe get $v_{T}=S_{T}-K$ which is just the payoff to the [[Forward Points in Currency|forward contract]] at maturity

To presage what we will do subsequent,  the value of the [[Forward Points in Currency|forward contract]] can also be calculated by using the [[Definitions and Immediate Consequences|stochastic discount factor]] $k$ 1 A [[Forward Points in Currency|forward contract]] with a delivery price of $K$ has a payoff at maturity of $S_{T}-K$ .Thus the value of this payoff is
$$v_t=\operatorname{E}[k\cdot (S_T-K)]=\operatorname{E}[k\cdot S_T]-K\operatorname{E}[k]=S_t-\frac{K}{(1+r_t^T)}$$

Where the last part of the equation follows since $\operatorname{E}[k]$ measure the appropri ately discounted payoff of one unit of payoff for sure and thus is equal to the [[Discount Factors|discount factor]] $1/(1+r_{t}^{T})$

## 3 Futures Contracts

So far we have used the terms forward and [[Futures Not Subject to Cash-And-Carry|futures]] interchangeably and they are equivalent if there is no [[Exercises|interest rate uncertainty]]. There are however. Some differences between forward and [[Mathematics of the Financial Markets|futures contracts]]

Forward contracts are normally traded over the counter and [[Mathematics of the Financial Markets|futures contracts]] are generally exchange traded with [[Futures Not Subject to Cash-And-Carry|futures]] prices reported in the financial press. With a [[Futures Not Subject to Cash-And-Carry|futures]] contract therefore the exchange provides a standardised contract with a range of specified delivery periods. Thus a wheat [[Futures Not Subject to Cash-And-Carry|futures]] contract will be specify the delivery of so many bushels of wheat for delivery in a particular month. The quality and delivery place will also be specified. The exact day of delivery within the month is usually left to the discretion of the writer of the contract

The key difference between forward and [[Mathematics of the Financial Markets|futures contracts]] is that [[Forwards and Futures|forwards]] are settled at maturity,  whereas [[Mathematics of the Financial Markets|futures contracts]] are settled daily. This [[Pricing and Hedging Implications of Daily Sett|daily settlement]] is done by requiring the investor to hold a margin account with the exchange. Thus although the contract costs nothing initially,  the investon is required to deposit a certain amount of funds,  the initial margin with the exchange. This margin account is marked to market to reflect the daily gains or losses on the contract. Thus for example if you buy a [[Futures Not Subject to Cash-And-Carry|futures]] contract on Wednesday for 250 and the following day the [[Futures Price and the Quality Option Before E|futures price]] has fallen to 240 you will have suffered a loss of 10 and this amount will be deducted from your margin account. In effect the [[Futures Not Subject to Cash-And-Carry|futures]] contract is closed out and rewritten every day. The exchange will also specify a maintenance margin which is the amount which must be maintained in the margin account,  usually about $75\%$ of the initial margin. If the margin account does fall below the maintenance margin the investor will be required to deposit extra funds,  the [[Repurchase Agreements|variation margin]],  with the exchange. Most [[Mathematics of the Financial Markets|futures contracts]] are closed out prior to maturity and don’t actually result in delivery of the underlying. Thus an investor will settle the [[Futures Not Subject to Cash-And-Carry|futures]] contract and withdraw the amount in the margin account on that day.

Traders on [[Futures Not Subject to Cash-And-Carry|futures]] (and other types of exchange markets) can place conditional trade as well as trade orders. There are three main types of order that can be executed. (i) A “Market”order will trade immediately at the current market price once the order is made there is no turning back! (ii) “Limit" orders are used to set a price at which the trader is prepared to trade. For example if the prices are currently high,  the trader can input a price a bit lower than the current offer,  and place a conditional order to buy. The order will now move into a working orders account and will be executed $if$ the offer price falls to the limit level specified. (ii) “Stop" orders enable the trader to limit losses in his/her [[An Asset Allocation Primer|portfolio]]. This involves setting a conditional price at which to sell the asset if the market moves too much in the wrong direction The trader specifies a price and volume at which to sell. The order will again be placed in the working orders account and will be executed if the price falls to thelevel specified.

<table>
	<tbody>
		<tr>
			<th>Day</th>
			<th colspan="2">$\mathbf{P}_{\mathrm{osition}}$</th>
			<th>$\mathbf{Futures}$ Price</th>
			<th>$\mathrm{Gain}_{\mathrm{I}}$ $1/\log$</th>
			<th>Gain $/\log$</th>
			<th rowspan="2">$\mathbf{Future}$ Value</th>
		</tr>
		<tr>
			<th>0</th>
			<th>Long</th>
			<th>1 $(1-r) T=1$</th>
			<th>$G_0$</th>
			<th> </th>
			<th> </th>
		</tr>
		<tr>
			<td>1</td>
			<td>Long</td>
			<td>1 $(1+r)^{T}$ -2 1 1 1</td>
			<td>$G_1$</td>
			<td>$G_{1}-G_{0}$ $(1+r)^{T-1}$</td>
			<td>$G_{1}-G_{0}$ $(1+r)^{T-1}$</td>
			<td>$G_{1}-G_{0}$</td>
		</tr>
		<tr>
			<td>2</td>
			<td>Long</td>
			<td>1 -3 $(1+r^{\cdot}$</td>
			<td>$G_{2}$</td>
			<td>$G_{1}-G_{0}$ 11. +7 -7 1 T</td>
			<td>$G_{1}-G_{0}$ 1 + 2</td>
			<td>$G_{2}-G_{1}$</td>
		</tr>
		<tr>
			<td>2</td>
			<td>$\operatorname{Long}$</td>
			<td>$\overline{(1+r)^{T-3}}$</td>
			<td>$.\dot{J}2$</td>
			<td>$(1+r)^{\prime}.$ -7 1.</td>
			<td>$(1+r)^T$ -7</td>
			<td>$(\dot{\boldsymbol{\tau}}2$ $2-(\dot{\boldsymbol{r}}1$</td>
		</tr>
		<tr>
			<td>$T$ 2 -</td>
			<td>Long</td>
			<td>1 $\overline{(1+r)}$</td>
			<td>$G_{T-2}$</td>
			<td>$G_{T-2}-G_{T-3}$ $(1+r)^{2}$</td>
			<td>$G_{T-2}-G_{T-3}$ $(1+r)^{2}$</td>
			<td>$G_{T-2}-$ $G_{T-3}$</td>
		</tr>
		<tr>
			<td>$T$ 1 -</td>
			<td>Long</td>
			<td>1</td>
			<td>$G_{T-1}$</td>
			<td>$G_{T-1}-G_{T-2}$ 11</td>
			<td>$G_{T-1}-G_{T-2}$ $(1+r^{-1})$ 1</td>
			<td>$G_{T-1}$ $-G_{T-2}$</td>
		</tr>
		<tr>
			<td>$T$</td>
			<td>0</td>
			<td> </td>
			<td>$G_{T}$</td>
			<td>$r-G_{T-1}$ $G_{T}$</td>
			<td>$G_{T}-G_{T-1}$</td>
			<td>$G_{T}-G_{T-1}$</td>
		</tr>
	</tbody>
</table>

Table 3: Equivalence of [[Futures Not Subject to Cash-And-Carry|Futures]] and Forward Prices

Although [[Futures Not Subject to Cash-And-Carry|futures]] are settled daily we now show that the [[Forward Contracts and Forward Prices|forward price]] and the [[Futures Price and the Quality Option Before E|futures price]] are the same if [[Interest Rate Quotations|interest rates]] are known even if the [[Forward Points in Currency|forward contract]] cannot be traded. For simplicity suppose that the interest rate is constant and let 7 denote the daily interest rate and suppose that the [[Futures Not Subject to Cash-And-Carry|futures]] contract matures on date and let $G_{0},     G_{1},     G_{2},    \ldots,     G_{T-1},     G_{T}$ denote the [[Futures Price and the Quality Option Before E|futures price]] on each of the trading days. Suppose that we have a position of $\frac 1{(1+r)^{T-t-1}}$ on day $t$ . Thus initially our position is $\frac 1{(1+r)^{T-1}}$ and we increment our position on a daily basis. The change in the value of our position on day 1 is$$\frac{G_1-G_0}{(1+r)^{T-1}}.$$

To calculate the future value of this gain or loss compounded to date we multiply by $(1+r)^{T-1}$ as there are $T-1$ days to go. Thus the future value is simply $G_{1}-G_{0}$ .The positions and future value on each day is summarised in Table 3.

Overall the future value from this [[An Asset Allocation Primer|portfolio]] is $G_{T}-G_{0}$ .Since the [[Futures Price and the Quality Option Before E|futures price]] at maturity must equal the spot price,  $G_T=S_{T}$，the future value is $S_{T}-G_{0}$ .If we combine this [[An Asset Allocation Primer|portfolio]] with a the purchase of a [[2. Forwards, Swaps, Futures, and Options|risk-free asset]] at time zero with a face value of $G_{0}$ the [[An Asset Allocation Primer|portfolio]] has a payoff of $S_T$ .Since the [[Mathematics of the Financial Markets|futures contracts]] cost nothing to purchase the overall cost of the [[An Asset Allocation Primer|portfolio]] is the cost of the [[2. Forwards, Swaps, Futures, and Options|risk-free asset]],  $\frac{1}{(1+r)^T}$ .Suppose that the [[Forward Points in Currency|forward contract]] has a delivery price of $F_{0}$ .Since wehave already seen that the [[Forward Points in Currency|forward contract]] combined with a [[2. Forwards, Swaps, Futures, and Options|risk-free asset]] with face value of $F_{0}$ gives at time
$T$ a [[An Asset Allocation Primer|portfolio]] worth $S_{T}$ ,  these two portfolios must cost the same. Hence
$$\begin{aligned}\frac{G_0}{(1+r)^T}=\frac{F_0}{(1+r)^T}\end{aligned}$$

Or $G_{0}=F_{0}$ and hence for any $t$，$G_{t}=F_{t}$ .Thus the forward and [[Futures Not Subject to Cash-And-Carry|futures]] prices are equivalent.

This argument can be replicated if the [[How Countries Go Broke-Chapter 12 to Chapter 14|interest rate changes]] in a known way,  simply by choosing the appropriate positions so that the future value of the gain or loss on the [[Futures Not Subject to Cash-And-Carry|futures]] contract is $G_{t}-G_{t-1}$ ondate $t$

There is however,  a difference between [[Futures Not Subject to Cash-And-Carry|futures]] and forward prices if the interest rate is uncertain. Suppose that there is a positive covariance between the interest rate and the price of the [[Risk Neutral Pricing of Options|underlying asset]]. Then if the price of the asset rises the gains on the [[Futures Not Subject to Cash-And-Carry|futures]] contract will tend to be valued at a high interest rate and similarly losses on the [[Futures Not Subject to Cash-And-Carry|futures]] contract will be valued at a low interest rate. An investor holding a [[Forward Points in Currency|forward contract]] is not affected by changes in the interest rate if they cannot trade the forward. Hence if the covariance between the interest rate and the underlying is positive,  the [[Futures Price and the Quality Option Before E|futures price]] will tend to be higher than the [[Forward Contracts and Forward Prices|forward price]]. In practice even this difference is likely to be small for as most [[Mathematics of the Financial Markets|futures contracts]] are held for relatively short durations. Thus for most practical purposes there is little difference between the forward and the [[Futures Price and the Quality Option Before E|futures price]].

It is tobe remembered too that although we've talked about the market price there are really two prices,  the bid price and the offer price. 2 The offer price is the price one can buy at (the market offers the contract at this price) and the bid price is the price one can sell at (how much the market is prepared to pay for the asset). It must be the case that offer price $\geq$ bid price otherwise you could buy at the offer price and sell at the bid price and make an immediate [[Arbitrage Pricing of Derivatives|arbitrage]] profit. The difference between the bid and offer prices is know as the bid-offer spread and the cost of buying at the offer price as selling at the bid price is known as the roundtrip cost.

## Backwardation and Contango

We have shown that the [[Forward Contracts and Forward Prices|forward price]] is just the future value of the underlying,  $F$ = $( 1+ r_{0}^{T}) S_{0}$ .Perhaps surprisingly the expected value of the [[Risk Neutral Pricing of Options|underlying asset]] at time 7，$\operatorname{E}[S_{T}]$ does not affect the [[Forward Contracts and Forward Prices|forward price]] at all. Yet it is also clear that the [[Forward Contracts and Forward Prices|forward price]] tends to the current spot price as the contracts tends to maturity. To see this suppose that we are very close to the delivery period. If the [[Forward Contracts and Forward Prices|forward price]] were below the current spot price,  then it would be possible buy the [[Forward Points in Currency|forward contract]],  wait for delivery and sell almost surely at the higher spot price. This will tend to drive the [[Forward Contracts and Forward Prices|forward price]] up toward the spot price. Similarly if the [[Forward Contracts and Forward Prices|forward price]] were above the spot price one could sell the [[Forward Points in Currency|forward contract]],  buy at the lower spot price and make the delivery generating an almost sure profit. With everyone doing this the [[Forward Contracts and Forward Prices|forward price]] will fall toward the spot price.

A situation where the [[Forward Contracts and Forward Prices|forward price]] is below the expected spot price,  $F<\operatorname{E}[S_{T}]$ ,  is called backwardation. A reverse situation where the [[Forward Contracts and Forward Prices|forward price]] is above the expected spot price is called contango. An interesting question,  and one that exercised Hicks and Keynes in the 1930 s,  is whether forward prices normally exhibit backwardation or contango and why.

To consider the relationship between the [[Forward Contracts and Forward Prices|forward price]] and the expected [[Hedging Strategies with Forwards|future spot price]] it is necessary to consider the risk involved in holding a forward or [[Futures Not Subject to Cash-And-Carry|futures]] position. Consider an investor or speculator who holds a [[Chapter 4 - Futures: Hedging and Speculation|long position]] in a [[Forward Points in Currency|forward contract]]. This obligates the investor to pay out $F$ the [[Forward Contracts and Forward Prices|forward price]] at maturity in return for an asset that will be worth the unknown amount $S_{T}$ .For simplicity suppose the investor $F/(1+r)$ in a risk-free [[An Asset Allocation Primer|investment]] now which will deliver $F$ at time $T$ to offset his/her obligations. The cash-fow is thus a certain $F/(1+r)$ now and an uncertain amount $S_{T}$ at time $T$

The question that remains is how to value the risky future payoff $S_{T}$ As in [[Corporate Finance Lecture Notes|corporate finance]] we could evaluate this payoff using a CAPM so that the

<table>
	<tbody>
		<tr>
			<th>Position</th>
			<th>Cost Now</th>
			<th>Payoff at Maturity</th>
		</tr>
		<tr>
			<td>Long Underlying</td>
			<td>$S_{0}=$E$[S_T]/(1$ +</td>
			<td>$S_T$</td>
		</tr>
	</tbody>
</table>

Table 4: [[Arbitrage Pricing of Derivatives|Arbitrage]] Possibility

Since the current stock value reflects the appropriately stochastically discounted value of possible future values,  $S_{0}=$ E $[k\cdot S_{T}]$ .Since $F=S_{0}(1+r)$ we have that $F=(1+r)$ E $[k\cdot S_T]$ .Using the covariance rule
$$\begin{aligned}
F=(1+r)\mathrm{E}[k\cdot S_{T}]& =(1+r)\mathrm{E}[k]\mathrm{E}[S_T]+(1+r) Cov (k,     S_T) \\
&=\mathrm{E}[S_T]+(1+r) Cov (k,     S_T)
\end{aligned}$$

Since $\operatorname{E}[k]=1/(1+r)$ . It can be seen from the above equation that whether there is backwardation or contango depends on the sign of $cov (k,     S_{T})$ . Typi cally,     because individuals are risk averse,     the demand will be for assets that offer insurance and the price of [[Assets|returns]] in low payoff states will be high. Thus for most assets the covariance will be negative. Typically then $F<\operatorname{E}[S_{T}]$ and the forward will exhibit backwardation.
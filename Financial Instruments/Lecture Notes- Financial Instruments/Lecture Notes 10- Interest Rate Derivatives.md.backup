---
linter-yaml-title-alias: LECTURE NOTES 10 INTEREST RATE DERIVATIVES
title: LECTURE NOTES 10 INTEREST RATE DERIVATIVES
tags:
  - black_model
  - callable_bonds
  - financial_instruments
  - floating_rate_debt
  - forward_rate_agreement
  - interest_rate_derivatives
  - interest_rate_swaps
  - risk_neutral_pricing
  - swap_contract
  - treasury_bills
aliases:
  - FRA
  - IR Derivatives
  - Interest Rate Trees
  - Lecture 10
  - Swaps
key_concepts:
  - Callable bonds
  - Floating rate debt
  - Forward rate agreement
  - Hedging problem solution
  - Ho Lee Model
  - Interest rate derivatives
  - Interest rate swaps
  - Risk neutral pricing
  - Swap rate calculation
  - Zero coupon bonds
---

# Lecture Notes 10- Interest Rate Derivatives

[Lecture Notes 9Corporate Securities And [Credit Derivatives](../../Credit%20Markets/RISK%20NEUTRAL%20VALUATION%20FRAMEWORK%20FOR%20CREDIT%20DEFAULT%20SWAPS.md)](Lecture%20Notes%209-%20Corporate%20Securities%20And%20Credit%20Derivatives.md)
[Lecture Notes 9ACredit Default Swaps](Lecture%20Notes%209A-%20Credit%20Default%20Swaps.md)

## FINANCIAL INSTRUMENTS

Interest Rate [Derivatives](../../Financial%20Markets/Financial%20Trading%20and%20Markets/Chapter%209%20Arbitrage%20and%20Hedging%20With%20Options.md)
[John Heaton](../Assignments/PSET%205%20Financial%20Instruments.md)
The University of Chicago Booth School of Business

1. Interest rate [Basis Swap](A%20Guide%20to%20the%20Front%20End%20and%20[[Basis%20Swaps) Markets#[Forward Rate Agreements](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%2012/EURIBOR%20Forward%20Rate%20Agreements%20and%20Futures.md) (FRAs) [Overview](../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%201%20-%20Purpose%20and%20Structure%20of%20Financial%20Markets/Overview%20of%20Financial%20Markets.md)|FRA]] and Swaps
1. [Black's model](../../Financial%20Engineering/Derivatives/Part%20IX%20-%20Fixed%20Income%20Derivatives/Chapter%2040%20-%20Pricing%20Fixed%20Income%20Options:%20Black’s%20Model%20and%20MCS.md) for interest rate [derivatives](../../Financial%20Markets/Financial%20Trading%20and%20Markets/Chapter%209%20Arbitrage%20and%20Hedging%20With%20Options.md)
1. [Interest Rate Trees](.md)
	1. 3.1 [Interest Rate Trees](.md) versus Stock Trees
	1. 3.2 [Risk Neutral Pricing](.md) on Trees
	1. 3.3 A 3-Period Bond
1. The [Ho Lee Model](.md)
	1. 4.1 [Risk Neutral Trees](Teaching%20Note%207-Exotic%20Options%20And%20Derivative%20Pricing%20By%20Monte%20Carlo%20Simulation.md)
	1. 4.2 [Calibration](../../Credit%20Markets/Credit%20Markets%20Session%204.md) of [Ho Lee Model](.md)
1. Using [Risk Neutral Trees](Teaching%20Note%207-Exotic%20Options%20And%20Derivative%20Pricing%20By%20Monte%20Carlo%20Simulation.md)
	1. 5.1 Callable Bonds

## THE GROWTH IN INTEREST RATE DERIVATIVES

The Notional Amount Of Over-The-Counter [Derivatives](../../Financial%20Markets/Financial%20Trading%20and%20Markets/Chapter%209%20Arbitrage%20and%20Hedging%20With%20Options.md) Panel
 ![500](cb7ba51a67fc85b5327fb7d1d8e90f58.png)

## [](../../Fixed%20Income%20Asset%20Pricing/Fixed%20Income%20Lecture%20Notes/A%20Guide%20to%20the%20Front%20End%20and%20Basis%20Swap%20Markets.md#Forward%20Rate%20Agreements%20(FRAs)%20Overview|Forward%20Rate%20Agreements)

- A [Basis Swap](A%20Guide%20to%20the%20Front%20End%20and%20[[Basis%20Swaps) Markets#[Forward Rate Agreements](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%2012/EURIBOR%20Forward%20Rate%20Agreements%20and%20Futures.md) (FRAs) [Overview](../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%201%20-%20Purpose%20and%20Structure%20of%20Financial%20Markets/Overview%20of%20Financial%20Markets.md)|[Forward Rate](../../Clippings/Forward%20Points%20in%20Currency.md) Agreement]](FRA) is an agreement between two counterparties A and B according to which at maturity T
- Counterparty A makes a payment to B equal to$N × F × ∆$,  where$N$is the notional, $∆$the [compounding frequency](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%202/Interest%20Rate%20Quotations.md),  and$F$is a fixed rate decided at time$0$;
- Counterparty B makes a payment to A equal to$N × R(T_{0},  T) × ∆$,  where$T_{0}  = T − ∆$.
- The reference floating rate R is typically the [Basis Swap](A%20Guide%20to%20the%20Front%20End%20and%20[[Basis%20Swaps) Markets#[London Interbank Offered Rate](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%2012/Short-Term%20Rates%20and%20the%20Transition%20from%20LIBOR.md) (LIBOR)|LIBOR]] rate. The *[forward rate](../../Clippings/Forward%20Points%20in%20Currency.md)* F is determined at time 0 so that the value of the [Basis Swap](A%20Guide%20to%20the%20Front%20End%20and%20[[Basis%20Swaps) Markets#[Forward Rate Agreements](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%2012/EURIBOR%20Forward%20Rate%20Agreements%20and%20Futures.md) (FRAs) [Overview](../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%201%20-%20Purpose%20and%20Structure%20of%20Financial%20Markets/Overview%20of%20Financial%20Markets.md)|FRA]] is zero.
- What is the value of this net [cash flow](../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%201%20-%20Purpose%20and%20Structure%20of%20Financial%20Markets/Preview%20of%20the%20Book.md) at time 0 for given F?
- Assume we have available the values of zero coupon bonds$Z(0,   T_{0})\text{ and }Z(0,  T)$.
- The Net [Cash flow](../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%201%20-%20Purpose%20and%20Structure%20of%20Financial%20Markets/Preview%20of%20the%20Book.md) to counterparty A is Net [Cash Flow](../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%201%20-%20Purpose%20and%20Structure%20of%20Financial%20Markets/Preview%20of%20the%20Book.md) at$T\ =\ N\times\Delta\times(F-R(T_{0}, T))$$$=\ N\times(1+F\times\Delta)$$([Fixed Leg](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%202/Pricing%20Interest%20Rate%20Swaps.md))$$-N\times(1+R(T_{0}, T)\times\Delta)$$([Floating Leg](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%202/Pricing%20Interest%20Rate%20Swaps.md))
- We compute the value of the [Basis Swap](A%20Guide%20to%20the%20Front%20End%20and%20[[Basis%20Swaps) Markets#[Forward Rate Agreements](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%2012/EURIBOR%20Forward%20Rate%20Agreements%20and%20Futures.md) (FRAs) [Overview](../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%201%20-%20Purpose%20and%20Structure%20of%20Financial%20Markets/Overview%20of%20Financial%20Markets.md)|FRA]] by computing the value of each leg.

## [](../../Fixed%20Income%20Asset%20Pricing/Fixed%20Income%20Lecture%20Notes/A%20Guide%20to%20the%20Front%20End%20and%20Basis%20Swap%20Markets.md#Forward%20Rate%20Agreements%20(FRAs)%20Overview|Forward%20Rate%20Agreements)
- Present value of [fixed leg](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%202/Pricing%20Interest%20Rate%20Swaps.md). This can be computed immediately:$$\mathrm{Value~of~Fixed~Leg}=Z(0, T)\times N\times(1+F\times\Delta)$$
- Present value of [floating leg](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%202/Pricing%20Interest%20Rate%20Swaps.md). This must be computed in two steps
- 1. Compute the value of [cash flow](../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%201%20-%20Purpose%20and%20Structure%20of%20Financial%20Markets/Preview%20of%20the%20Book.md)$N × R(T_0,  T)$as of time$T_0$. Note that at that time we will know the rate$R(T_0,  T)$
	- Value of [Floating Leg](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%202/Pricing%20Interest%20Rate%20Swaps.md) at$$T_{0}=\dfrac{\text{Cash Flow at } T}{1\text{ period discount}}=N\times\dfrac{(1+R(T_{0}, T)\times\Delta)}{(1+R(T_{0}, T)\times\Delta)}=N$$
1. Obtain the value of [Floating Leg](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%202/Pricing%20Interest%20Rate%20Swaps.md) at 0
- Therefore,  the value of the [Basis Swap](A%20Guide%20to%20the%20Front%20End%20and%20[[Basis%20Swaps) Markets#[Forward Rate Agreements](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%2012/EURIBOR%20Forward%20Rate%20Agreements%20and%20Futures.md) (FRAs) [Overview](../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%201%20-%20Purpose%20and%20Structure%20of%20Financial%20Markets/Overview%20of%20Financial%20Markets.md)|FRA]] is$$V=N\times[Z(0, T)\times(1+F\times\Delta)-Z(0, T_{0})]=N\times Z(0, T)\times\left[(1+F\times\Delta)-\frac{Z(0, T_{0})}{Z(0, T)}\right]$$
- The [forward rate](../../Clippings/Forward%20Points%20in%20Currency.md)$F$makes this quantity equal to zero$$1+F\times\Delta=\frac{Z(0, T_{0})}{Z(0, T)}\Longrightarrow F=\frac{1}{\Delta}\left(\frac{Z(0, T_{0})}{Z(0, T)}-1\right)$$

## FORWARD RATE AGREEMENT: EXAMPLE
- It is November 1,  2022. A firm has a receivable of \$100 million in six months$(T_1 = 0.5)$,  and wishes to park this money for an additional six months (until$T_2 = 1$),  when it will need to use it for some capital expenditure.
- The firm is worried that the six month rate will decline at$T_{1}$and thus wants to lock-in a six-month rate *today*.
- To hedge,  the firm can enter into a six-month [Basis Swap](A%20Guide%20to%20the%20Front%20End%20and%20[[Basis%20Swaps) Markets#[Forward Rate Agreements](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%2012/EURIBOR%20Forward%20Rate%20Agreements%20and%20Futures.md) (FRAs) [Overview](../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%201%20-%20Purpose%20and%20Structure%20of%20Financial%20Markets/Overview%20of%20Financial%20Markets.md)|FRA]] with a bank for the period$T_1$to$T_2$,  and notional N =$100 million.
- Today the bank agrees to pay in one year ($T_2 = 1$) the amount$\frac{N}{2} × F(0.5,  1)$;
- The firm agrees to pay on the same day the amount$\frac{N}{2} × R(0.5,  1)$.
- That is,  they exchange the payment at$T_2 = 1$
	- Net payment of the firm at$T_{2}=\frac{N}{2}\times[F(0, )-R(0.5, 1)]\tag{1}$
- What is the [forward rate](../../Clippings/Forward%20Points%20in%20Currency.md)?
- On November 1,  2022,  the value of 6-months Treasury bills is$Z(0,  0.5) = 97.728$and the value of 1-year Treasury bills is$Z(0,  1) = 95.713$. Thus:$$F(0, 0.5, 1)=2\times\left(\frac{Z(0, 0.5)}{Z(0, 1)}-1\right)=4.21\%.$$

## FORWARD RATE AGREEMENT: EXAMPLE
- Why does the [Basis Swap](A%20Guide%20to%20the%20Front%20End%20and%20[[Basis%20Swaps) Markets#[Forward Rate Agreements](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%2012/EURIBOR%20Forward%20Rate%20Agreements%20and%20Futures.md) (FRAs) [Overview](../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%201%20-%20Purpose%20and%20Structure%20of%20Financial%20Markets/Overview%20of%20Financial%20Markets.md)|FRA]] solves the [hedging](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%205/Key%20Rates%20O1s%20Durations%20and%20Hedging.md) problem of the firm?
- Because at$T_1 = 0.5$,  when the firm receives its \$100 million receivable,  it can simply invest it at the market rate$R(0.5,  1)$
- Then,  at$T_2 = 1$,  the firm receives the payoff from the [investment](../../Advanced%20Investments/An%20Asset%20Allocation%20Primer.md),  plus the net payment from the FRA. In total:
Total amount at$T_{2}$$$=\ \left\{\$100\ \text{million}\ \times\left[1+\frac{R(0.5, 1)}{2}\right]\right\}\quad\text{(Return on investment)}$$$$+\left\{\frac{N}{2}\times[F(0.5, 1)-R(0.5, 1)]\right\}\quad\text{(FRA payment)}$$$$=\ \$100\ \text{million}\ \times\left[1+\frac{F(0, 5, 1)}{2}\right]$$$$=\ \$102.105\ \text{million}$$
- That is,  the firm locked in the [forward rate](../../Clippings/Forward%20Points%20in%20Currency.md)$F(0.5,  1) = 4.21\%$

## INTEREST RATE SWAPS
- An [interest rate swap](../../Financial%20Engineering/Primer%20on%20Interest%20Rate%20Swaps.md) is an agreement between two counterparties,  according to which at dates$T_{1}$, $T_{2}$,  …$T_n$,  with$T_{i}$=$T_{i-1} + ∆$,  the counterparties exchange the net cash flows$${\mathrm{Swap~Net~Cash~Flow~at}}T_{i}=N\times\Delta\times(K-R(T_{i-1}, T_{i}))$$
- The [swap rate](../../Fixed%20Income%20Asset%20Pricing/Fixed%20Income%20Lecture%20Notes/Teaching%20Note%204%20Interest%20Rate%20Derivatives.md) K is chosen to make the value of the swap equal to zero at time 0.
- What is the value of the swap at 0?
- Clearly,  this specific [cash flow](../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%201%20-%20Purpose%20and%20Structure%20of%20Financial%20Markets/Preview%20of%20the%20Book.md) is the same we had earlier for a FRA,  and therefore
PV of [Cash Flow](../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%201%20-%20Purpose%20and%20Structure%20of%20Financial%20Markets/Preview%20of%20the%20Book.md) at$T_{i}\ =\ N\times Z(0, T_{i})\times\left[(1+K\times\Delta)-\frac{Z(0, T_{i-1})}{Z(0, T_{i})}\right]$
$$=\ N\times Z(0, T_{i})\times\left[(1+K\times\Delta)-(1+F(0, T_{i-1}, T_{i})\Delta)\right]$$
$$=\ N\times\Delta\times Z(0, T_{i})\left[K-F(0, T_{i-1}, T_{i})\right]$$

- where we denote$F(0,   T_{i-1},   T_{i}$) the [forward rate](../../Clippings/Forward%20Points%20in%20Currency.md) at time 0 for a [Basis Swap](A%20Guide%20to%20the%20Front%20End%20and%20[[Basis%20Swaps) Markets#[Forward Rate Agreements](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%2012/EURIBOR%20Forward%20Rate%20Agreements%20and%20Futures.md) (FRAs) [Overview](../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%201%20-%20Purpose%20and%20Structure%20of%20Financial%20Markets/Overview%20of%20Financial%20Markets.md)|FRA]] between$T_{i-1}$and$T_{i}$.
- It follows that for given K,  the value of the swap is the sum of these values$${\mathrm{Value~of~Swap}}=N\times\Delta\times\sum\limits_{i=1}^{n}Z(0, T_{i})\times[K-F(0, T_{i-1}, T_{i})]$$
- The [swap rate](../../Fixed%20Income%20Asset%20Pricing/Fixed%20Income%20Lecture%20Notes/Teaching%20Note%204%20Interest%20Rate%20Derivatives.md) is then the K that makes the value of the swap equal to zero$$\sum\limits_{i=1}^{n}Z(0, T_{i})\times[K-F(0, T_{i-1}, T_{i})]=0\Longrightarrow K=\sum\limits_{i=1}^{n}w_{i}\times F(0, T_{i-1}, T_{i})$$
	- where$$w_{i}=\frac{Z(0, T_{i})}{\Sigma_{i=1}^{n}Z(0, T_{i})}$$
- The [swap rate](../../Fixed%20Income%20Asset%20Pricing/Fixed%20Income%20Lecture%20Notes/Teaching%20Note%204%20Interest%20Rate%20Derivatives.md) is a weighted average of forward rates. - This is very similar to our findings in Teaching Notes 2.

## INTEREST RATE SWAP EXAMPLE
- Today is November 1,  2022. A firm has receivables of$5.5 millions every six months for the next 5 years.
- The firm has also a 5-year,  semi-annual, $200 m [floating rate debt](.md) outstanding,  with floating rate [Basis Swap](A%20Guide%20to%20the%20Front%20End%20and%20[[Basis%20Swaps) Markets#[London Interbank Offered Rate](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%2012/Short-Term%20Rates%20and%20the%20Transition%20from%20LIBOR.md) (LIBOR)|LIBOR]] + 4 bps.
- How can the firm use the receivables to service the coupons on the debt?
- A solution is to enter into a [fixed-for-floating swap](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%2016/Swaptions.md) with an [investment](../../Advanced%20Investments/An%20Asset%20Allocation%20Primer.md) bank.
	- On November 1,  2022,  the [swap rate](../../Fixed%20Income%20Asset%20Pricing/Fixed%20Income%20Lecture%20Notes/Teaching%20Note%204%20Interest%20Rate%20Derivatives.md) for a 5-year [fixed-for-floating swap](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%2016/Swaptions.md) was quoted at K = 5.46%.
- So,  the *net* [cash flow](../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%201%20-%20Purpose%20and%20Structure%20of%20Financial%20Markets/Preview%20of%20the%20Book.md) to the firm from the [swap contract](../Review%20Session%20Notes/Currency%20Swaps.md) is
Net [cash flow](../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%201%20-%20Purpose%20and%20Structure%20of%20Financial%20Markets/Preview%20of%20the%20Book.md) to the firm at$$T_{i}  = 200 \text{ million } × 0.5 × [R(T_{i} −1,   T_{i}) − 5.46\%]$$
- Why does this swap resolve the problem? ![500](ddf363508a33988350b1bc3466b5578e.png)
- One of the main reasons for the massive increase in the size of the swap market is its flexibility for [cash flow](../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%201%20-%20Purpose%20and%20Structure%20of%20Financial%20Markets/Preview%20of%20the%20Book.md) management and [risk management](../../Financial%20Engineering/Financial%20Mathematics%20Course.md).

## ISSUES WITH LIBOR
- Until January 31,  2014: British Bankers Association (BBA) LIBOR
	- Survey of a panel of banks
	- Banks could underestimate their [borrowing costs](../../Financial%20Engineering/Notes%20on%20Currency%20Swaps.md)
	- Conflict within the bank: impact of [Basis Swap](A%20Guide%20to%20the%20Front%20End%20and%20[[Basis%20Swaps) Markets#[London Interbank Offered Rate](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%2012/Short-Term%20Rates%20and%20the%20Transition%20from%20LIBOR.md) (LIBOR)|LIBOR]] setting on [derivatives](../../Financial%20Markets/Financial%20Trading%20and%20Markets/Chapter%209%20Arbitrage%20and%20Hedging%20With%20Options.md) trading.
- Now ICE LIBOR
	- ICE now the benchmark administrator
	- Regulator in UK: Financial Conduct Authority (FCA)
	- Rules for fall-back rates if there are issues

## ALTERNATIVES
- SOFR: "[Secured Overnight Financing Rate](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%2010/SOFR.md)"
- ARRC: Alternative Reference Rates Committee.
- Others:
	- SONIA (Sterling Over Night Indexed Average)
	- EONIA (Euro Overnight Index Average)
	- TONAR (Tokyo Overnight Average Rate)
	- SARON (Swiss Average Rate Over-Night)
- Measure of overnight *secured* borrowing.
- Collateralized [US Treasuries](../../Credit%20Markets/Credit%20Market%20PSETS/Credit%20Market%20Homework%201.md) in the repo market.
- Very liquid and likely resilient markets:$1 trillion in daily volume
- Contrast: USD [Basis Swap](A%20Guide%20to%20the%20Front%20End%20and%20[[Basis%20Swaps) Markets#[London Interbank Offered Rate](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%2012/Short-Term%20Rates%20and%20the%20Transition%20from%20LIBOR.md) (LIBOR)|LIBOR]] three-month tenor: about$1 billion
- Published by New York Fed. Along with 30-day,  90-day and 180-day averages

## TRANSITION
- [Basis Swap](A%20Guide%20to%20the%20Front%20End%20and%20[[Basis%20Swaps) Markets#[London Interbank Offered Rate](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%2012/Short-Term%20Rates%20and%20the%20Transition%20from%20LIBOR.md) (LIBOR)|LIBOR]] market:$200+ trillion of financial transactions contracts reference LIBOR
- Transition was set for end of 2021,  but now 18 month extension
- [Basis Swap](A%20Guide%20to%20the%20Front%20End%20and%20[[Basis%20Swaps) Markets#[London Interbank Offered Rate](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%2012/Short-Term%20Rates%20and%20the%20Transition%20from%20LIBOR.md) (LIBOR)|LIBOR]] permeates many contracts for in [securities markets](../../Financial%20Markets/Financial%20Trading%20and%20Markets/Chapter%201%20Introduction%20to%20Securities%20Trading%20and%20Markets.md) and the corporate world: leases,  debt,  ….
- [Derivatives](../../Financial%20Markets/Financial%20Trading%20and%20Markets/Chapter%209%20Arbitrage%20and%20Hedging%20With%20Options.md) market with Central Clearing Partners (e.g. CME …).
	- Cleared US Dollar [interest rate swap](../../Financial%20Engineering/Primer%20on%20Interest%20Rate%20Swaps.md) contracts at CME: move to SOFR discounting.
	- Intercontinental Exchange (ICE) Benchmark Administration: USD [Basis Swap](A%20Guide%20to%20the%20Front%20End%20and%20[[Basis%20Swaps) Markets#[London Interbank Offered Rate](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%2012/Short-Term%20Rates%20and%20the%20Transition%20from%20LIBOR.md) (LIBOR)|LIBOR]] benchmarks will stop June 30,  2023
- Fannie and Freddie: have moved bo SOFR contracts
- New York Fed: conducts repo and reverse repo through tri-party repo.
- OTC [SOFR swaps](../../Credit%20Markets/Credit%20Market%20PSETS/Advanced%20Usage%20of%20QuantLib%20analytics%20library.md)
- SOFR caps products have developed since September 2020

## SOFR DERIVATIVES

As an example: at the CME

- [Futures](../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%203%20-%20Futures%20Markets/Futures%20Not%20Subject%20to%20Cash-And-Carry.md): 3-month and 1-month. Using compounding or simple averages.
- Term SOFR Reference rates based on [futures contracts](../../Financial%20Engineering/Mathematics%20of%20the%20Financial%20Markets.md).
## SOME HISTORY

 ![500](096f82336d662be8e12414cdea9f13c4.png)

## OVERNIGHT INDEX SWAPS (IS)
- In a Is,  the two counterparties agree to exchange [fixed for floating payments](Teaching%20Note%203%20Swaps-%20Financial%20Instruments/Overnight%20Index%20Swaps%20(OIS).md),  where the floating payment is tied to the cumulative return from an overnight rate
- [Federal funds rate](../../International%20Finance/Economic%20Stabilization%20Notes/Topics%20in%20Fiscal%20and%20Monetary%20Policies%20and%20Stabilization-%20Empirical%20Issues.md),  SOFR in US. Europe: short-term rate (eSTR),  (formerly Euro OverNight Index Average (EONIA) rate).
- Given a notional N,  the [floating rate payment](Teaching%20Note%203%20Swaps-%20Financial%20Instruments/Overnight%20Index%20Swaps%20(OIS).md) at time$T_{i}$is$$CF\left(T_{i}\right)=N\left(\prod\limits_{j=1}^{n_{j}}\left(1+r_{t_{j}}\delta\right)-1\right)\tag{2}$$
- where δ is the daily interval, $r_t$is the reference (annualized) overnight rate,  and$n_j$is the number of days between reset periods.
- The day count convention is normally Actual/360.
- In the continuous time limit ($\delta\to0$),  we have that$$CF\left(T_{i}\right)=N\left(e^{\int_{t-1}^{T_{i}}r\left(n\right)\mathrm{d}n}-1\right)\tag{3}$$
- Is with maturity less than 1 year have only one payment at the maturity.
- Is with longer maturities have normally quarterly payments.

## WHAT IS THE VALUE OF IS?
- The value of Is is the difference between the [floating leg](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%202/Pricing%20Interest%20Rate%20Swaps.md) and the [fixed leg](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%202/Pricing%20Interest%20Rate%20Swaps.md):$$V_{t}^{OIS}=V_{t}^{Floating}-V_{t}^{Fixed}\tag{4}$$
- **[Floating Leg](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%202/Pricing%20Interest%20Rate%20Swaps.md)**: At reset dates,  and assuming the payment of a principal at maturity of the swap,  the value of the [floating leg](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%202/Pricing%20Interest%20Rate%20Swaps.md) is par.
- Indeed,  investing the notional N in the overnight index daily gives at$T_{i}$$$N\prod_{j=1}^{n_{j}}\left(1+r_{t_{j}}\Delta\right)=C F\left(T_{i}\right)+N$$
	- ⇒ we can replicate the floating payments,  plus a residual of notional at maturity$T_{i}$,  with an [investment](../../Advanced%20Investments/An%20Asset%20Allocation%20Primer.md) N at time 0.
- It follows$$V_0^{Floating}=N$$
- **[Fixed leg](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%202/Pricing%20Interest%20Rate%20Swaps.md):** Given a proper [discount function](../../Financial%20Markets/Financial%20Asset%20Pricing%20Theory%20Overview/Chapter%2010%20-%20The%20Economics%20of%20the%20Term%20Structure%20of%20Interest%20Rates/Basic%20Interest%20Rate%20Concepts%20and%20Relations.md)$Z_{OIS} (0,  T_{i}$),  we obtain$$V_{0}^{Fixed}=N\ c\ \Delta\ \sum\limits_{i=1}^{n}Z^{OIS}\left(0, T_{i}\right)+N\ Z^{OIS}\left(0, T_{n}\right)\tag{5}$$
- The value of the contract at inception is zero, $V^{OIS}_0= 0$.
- It follows from (4) then that$$V_{0}^{O I S}=V_{0}^{F l o a t i n g}-V_{0}^{F i x e d}=0\tag{6}$$
- This equation implies that the [swap rate](../../Fixed%20Income%20Asset%20Pricing/Fixed%20Income%20Lecture%20Notes/Teaching%20Note%204%20Interest%20Rate%20Derivatives.md) c can be computed from$$1=c\, \Delta\, \, \sum\limits_{i=1}^{n}Z^{OIS}\left(0, T_{i}\right)+Z^{OIS}\left(0, T_{n}\right)\tag{7}$$
	- which gives$$c(T_{n})=\frac{1}{\Delta}\frac{1-Z^{OLS}(0, T_{n})}{\Sigma_{i=1}^{n}Z^{OLS}\left(0, T_{i}\right)}\tag{8}$$
	- where we now emphasize that the coupon rate$c$is for a swap with maturity$T_{n}$,  and thus write$c(T_{n})$.

## IS DISCOUNT CURVE
- Given the Is coupon rates$c(T_{i}$) for every maturity$T_{i}$,  we can bootstrap the Is zero-coupon curve from (6).
- We obtain the relation:$$Z^{OIS}\left(0, T_{i}\right)=\frac{1-c\left(T_{i}\right)\, \Delta\, \, \Sigma_{j=1}^{i-1}\, Z^{OIS}\left(0, T_{j}\right)}{1+c\left(T_{i}\right)\Delta}\tag{9}$$
- recalling,  however,  that Is with maturity less than or equal to 1 year generally have only one payment.
- Next Figure shows an example of bootstrapping from Is quotes,  on January 2,  2009. Panel A reports the original Is quotes from Bloomberg. Panel B uses the quotes from Panel A along with bootstrap methodology (9) and defines the Is [discount function](../../Financial%20Markets/Financial%20Asset%20Pricing%20Theory%20Overview/Chapter%2010%20-%20The%20Economics%20of%20the%20Term%20Structure%20of%20Interest%20Rates/Basic%20Interest%20Rate%20Concepts%20and%20Relations.md)$Z^{OIS}(0,  T)$.
## IS AND [](../../Fixed%20Income%20Asset%20Pricing/Fixed%20Income%20Lecture%20Notes/A%20Guide%20to%20the%20Front%20End%20and%20Basis%20Swap%20Markets.md#London%20Interbank%20Offered%20Rate%20(LIBOR)|LIBOR) DISCOUNT CURVE ON JANUARY 2ND,  2009

 ![500](f56f77987685bc6c5d58d6cc34f039cb.png)

## IS AND [](../../Fixed%20Income%20Asset%20Pricing/Fixed%20Income%20Lecture%20Notes/A%20Guide%20to%20the%20Front%20End%20and%20Basis%20Swap%20Markets.md#London%20Interbank%20Offered%20Rate%20(LIBOR)|LIBOR) DISCOUNT CURVE ON JANUARY 2ND,  2007

 ![500](b687c872a37a38a4405d3.png)

- However,  if we try after the crisis,  we obtain the following figure:

## IS AND [](../../Fixed%20Income%20Asset%20Pricing/Fixed%20Income%20Lecture%20Notes/A%20Guide%20to%20the%20Front%20End%20and%20Basis%20Swap%20Markets.md#London%20Interbank%20Offered%20Rate%20(LIBOR)|LIBOR) DISCOUNT CURVE ON JANUARY 2ND,  2009

 ![500](a5c5dde2f41af7900fa5833565f8581f.png)

- which are quite different.
## INTEREST RATE OPTIONS
- The market for plain vanilla interest rate options is very large.
- These include
	- Treasury bond options: Options to purchase a Treasury bond
	- Swaptions: Options to enter into a swap at a given strike (swap) rate.
		- Receiver Swaptions: Options to enter into a swap and receive the strike [swap rate](../../Fixed%20Income%20Asset%20Pricing/Fixed%20Income%20Lecture%20Notes/Teaching%20Note%204%20Interest%20Rate%20Derivatives.md);
		- Payer Swaptions: Options to enter into a swap and pay the strike [swap rate](../../Fixed%20Income%20Asset%20Pricing/Fixed%20Income%20Lecture%20Notes/Teaching%20Note%204%20Interest%20Rate%20Derivatives.md).
	- [Caps and Floors](../../Financial%20Engineering/Fixed%20Income%20Derivatives/Interest%20Rate%20Derivatives-An%20Introduction%20to%20the%20%20Pricing%20of%20Caps%20and%20Floors.md): Securities that pay when rates go up (Caps) or down ([Floors](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%2016/Caps%20and%20Floors.md)). Their cash flows are given by$$\begin{array}{r c l}{{}}&{{}}&{{\mathrm{Cap~CF~at~}T_{i}~=~N\times\Delta\times\operatorname*{max}\left(R(T_{i-1}, T_{i})-K\right);}}\\ {{}}&{{}}&{{}}\\ {{}}&{{}}&{{\mathrm{Floor~CF~at~}T_{i}~=~N\times\Delta\times\operatorname*{max}\left(K-R(T_{i-1}, T_{i})\right)}}\end{array}$$
	- Popular derivative instruments to insure agains increases or decreases in [interest rates](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%202/Interest%20Rate%20Quotations.md) ∗ For instance,  caps typically accompany floating rate bond issuance.
- Caption and Floortion: Options to enter into a cap or a floor.

## THE BLACK’S FORMULA FOR INTEREST RATE OPTIONS
- The assumptions of Black and Scholes do not apply to interest rate options
	- 1. The [Black-Scholes model](../Black%20Scholes%20Derivation.md) assumes a constant interest rate,  while we are trying to price risk on [interest rates](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%202/Interest%20Rate%20Quotations.md);
	- 2. The [Black-Scholes model](../Black%20Scholes%20Derivation.md) assumes constant volatility,  but if the underlying is e.g. a T-Bond,
the volatility depends on [duration](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%205/Key%20Rates%20O1s%20Durations%20and%20Hedging.md) and thus it is declining with time.
- Even so,  practitioners use the [Black-Scholes formula](../../Credit%20Markets/Credit%20Markets%20Session%205.md) to price a number of interest rate [derivatives](../../Financial%20Markets/Financial%20Trading%20and%20Markets/Chapter%209%20Arbitrage%20and%20Hedging%20With%20Options.md)
- For long this has been thought to be at best an approximation of no [arbitrage](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%207/Arbitrage%20Pricing%20of%20Derivatives.md) models,  because of the violations to [Black-Scholes formula](../../Credit%20Markets/Credit%20Markets%20Session%205.md)'s assumption described earlier
- In recent times,  it has been shown that the [Black and Scholes formula](Lecture%20Note%205-%20Black%20Scholes%20Formula.md) can be derived by no-[arbitrage](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%207/Arbitrage%20Pricing%20of%20Derivatives.md) principles under some assumptions.
- In what follow,  we only look at one simple example.

## EXAMPLE: THE BLACK'S FORMULA TO PRICE CAPS
- The Cap pays the sequence of cash flows$$\mathrm{Cap~CF~at~}T_{i}=N\times\Delta\times\operatorname*{max}\left(R(T_{i-1}, T_{i})-K\right);$$
- where ∆ =$T_{i}$−$T_{i}$−1. Each payment is called a caplet.
- The original Black's formula uses as underlying the [futures price](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%2011/Futures%20Price%20and%20the%20Quality%20Option%20Before%20E.md),  which equals the [forward price](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%2011/Forward%20Contracts%20and%20Forward%20Prices.md)
when [interest rates](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%202/Interest%20Rate%20Quotations.md) are constant.
- In the case of caplets,  we use the [forward rate](../../Clippings/Forward%20Points%20in%20Currency.md) directly,  which is given by$$F(0, T_{i-1}, T_{i})=\frac{1}{\Delta}\left(\frac{Z(0, T_{i-1})}{Z(0, T_{i})}-1\right)$$
- The model assumes that under the proper risk-adjusted probabilities,  at time$T_{i}$, $$R(T_{i-1}, T_{i})=F(T_{i-1}, T_{i-1}, T_{i})\sim LogNormal$$
- with Variance$[R(T_{i} −1,   T_{i})] = σ^2_FT_{i-1}.$
- Then,  the Black formula (see Teaching Notes 5) has$$C a p l e t(T_{i})=Z(0, T_{i})\times[F(0, T_{i-1}, T_{i})\times N(d_{1})-K\times N(d_{2})]$$
- where$$d_{1}=\frac{\log\left(\frac{F(0, T_{i-1}, T_{i})}{K}\right)+\frac{1}{2}\sigma_{F}^{2}T_{i-1}}{\sigma_{F}\sqrt{T_{i-1}}};\quad d_{2}=d_{1}-\sigma_{F}\sqrt{T_{i-1}}$$

## EXAMPLE: THE BLACK'S FORMULA TO PRICE CAPS
- Indeed,  market participants quote [caps and floors](../../Financial%20Engineering/Fixed%20Income%20Derivatives/Interest%20Rate%20Derivatives-An%20Introduction%20to%20the%20%20Pricing%20of%20Caps%20and%20Floors.md) directly in terms of [implied volatility](../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%205%20Options%20on%20Prices%20and%20Hedge-Based%20Valuation/A%20Real-Life%20Option%20Pricing%20Exercise.md). For instance,  from Bloomberg we have
 ![500](f155e82004596b82979fdd6b86ae8c94.png)
- Each entry is a volatility quote for an "at-the-money" instrument,  meaning that its strike rate(equal for all the caplets) is the [swap rate](../../Fixed%20Income%20Asset%20Pricing/Fixed%20Income%20Lecture%20Notes/Teaching%20Note%204%20Interest%20Rate%20Derivatives.md) with the same maturity of the cap.
- The payment frequency of the underlying [caps and floors](../../Financial%20Engineering/Fixed%20Income%20Derivatives/Interest%20Rate%20Derivatives-An%20Introduction%20to%20the%20%20Pricing%20of%20Caps%20and%20Floors.md) is 3 months.
- Since the first payment at horizon 3 months is known at time 0,  it is practice to set this caplet equal to zero.

## EXAMPLE: THE BLACK'S FORMULA TO PRICE CAPS

- Example: Consider a 1-year,  quarterly cap with strike rate$r_K = 2.555\%$,  quoted at volatility$σ_F = 23.5\%$.
- The current [Basis Swap](A%20Guide%20to%20the%20Front%20End%20and%20[[Basis%20Swaps) Markets#[London Interbank Offered Rate](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%2012/Short-Term%20Rates%20and%20the%20Transition%20from%20LIBOR.md) (LIBOR)|LIBOR]] [discount curve](../../Credit%20Markets/Credit%20Market%20PSETS/Advanced%20Usage%20of%20QuantLib%20analytics%20library.md) is as follows$$Z(0,  0.25) = 99.4580; Z(0,  0.5) = 99.8510; Z(0,  0.75) = 99.1899; Z(0,  1) = 97.4834$$
- From the [Basis Swap](A%20Guide%20to%20the%20Front%20End%20and%20[[Basis%20Swaps) Markets#[London Interbank Offered Rate](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%2012/Short-Term%20Rates%20and%20the%20Transition%20from%20LIBOR.md) (LIBOR)|LIBOR]] curve,  we can compute the quarterly compounded forward rates:$$F(0,  0.25,  0.5) = 2.4562\%; F(0,  0.5,  0.75) = 2.6932\%; F(0,  0.75,  1) = 2.8987\%$$
- Finally,  from the quoted volatility$\sigma_{F}=23.5\%$,  we obtain the three relevant volatilities:$$\sigma_{F}\times[\sqrt{T_{1}}, \sqrt{T_{2}}, \sqrt{T_{3}}]\ =\ 23.5\%\times[\sqrt{0.25}, \sqrt{0.5}, \sqrt{0.75}]=[11.75\%\%\%].$$
- Using the formula for$d_1$and$d_2$we obtain$$d_{1}(0.50)=-0.02770;\, d_{2}(0.50)=-0.03945\Longrightarrow\mbox{Caplet}(0.50)=0.0184$$$$d_{1}(0.75)=0.4000;\, d_{2}(0.75)=0.02328\Longrightarrow\mbox{Caplet}(0.75)=0.0617$$$$d_{1}(1)=0.7218;\, d_{2}(1)=0.5183\Longrightarrow\mbox{Caplet}(1)=0.1057$$
- obtaining$$Cap(1Y)=0.0184+0.0617+0.1057=0.1859$$
## THE TIME SERIES OF [IMPLIED VOLATILITY](Lecture%20Note%206-Implied%20Volatility%20)
- The quoted volatility of caps is strongly time varying,  denoting time variation in uncertainty
about changes in future [interest rates](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%202/Interest%20Rate%20Quotations.md).
 ![500](54163984c3287d601b791751fa174d1a.png)

## INTEREST RATE TREES
- We now develop the same arguments we used in TN 4,  but for [interest rates](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%202/Interest%20Rate%20Quotations.md).
- Let$r_t =$be the six-month,  continuously compounded [risk-free rate](../Black%20Scholes%20Derivation.md).
- Let$q = 1/2$be the (true) probability to move up or down on the tree.
	- The movement of the [short-term interest rate](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%209/The%20Gauss%20Model.md) is exogenous to investors.
	- E.g. the Federal Reserve sets [the Fed](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Front%20Matter/Monetary%20Policy%20with%20Abundantreserves.md) Fund rate because of [Risk and Return](Lecture%207-[[Lecture%207-Risk%20and%20Return%20of%20Bonds) of Bonds#7.6 [Asset price](../../Financial%20Markets/Financial%20Asset%20Pricing%20Theory%20Overview/Chapter%204%20-%20State%20Prices/A%20Preview%20of%20Alternative%20Formulations.md) reactions to [monetary policy](../../Financial%20Markets%20and%20Institutions/III.%20Liquidity%20of%20Assets/Class%209-%20Bailouts%20and%20Bank%20Failures/Articles/The%20Economist%20Regime%20Change.md) surprises|[monetary policy](../../Financial%20Markets%20and%20Institutions/III.%20Liquidity%20of%20Assets/Class%209-%20Bailouts%20and%20Bank%20Failures/Articles/The%20Economist%20Regime%20Change.md)]] issues.
-  ![500](cbd186d3c7001e949e521ca66dc13413.png)
- We now develop the same arguments we used in TN 4,  but for [interest rates](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%202/Interest%20Rate%20Quotations.md).
- Let$r_t$be the six-month,  continuously compounded [risk-free rate](../Black%20Scholes%20Derivation.md).
- Let$q = 1/2$be the (true) probability to move up or down on the tree.
- The movement of the [short-term interest rate](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%209/The%20Gauss%20Model.md) is exogenous to investors.
- E.g. the Federal Reserve sets [the Fed](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Front%20Matter/Monetary%20Policy%20with%20Abundantreserves.md) Fund rate because of [Risk and Return](Lecture%207-[[Lecture%207-Risk%20and%20Return%20of%20Bonds) of Bonds#7.6 [Asset price](../../Financial%20Markets/Financial%20Asset%20Pricing%20Theory%20Overview/Chapter%204%20-%20State%20Prices/A%20Preview%20of%20Alternative%20Formulations.md) reactions to [monetary policy](../../Financial%20Markets%20and%20Institutions/III.%20Liquidity%20of%20Assets/Class%209-%20Bailouts%20and%20Bank%20Failures/Articles/The%20Economist%20Regime%20Change.md) surprises|[monetary policy](../../Financial%20Markets%20and%20Institutions/III.%20Liquidity%20of%20Assets/Class%209-%20Bailouts%20and%20Bank%20Failures/Articles/The%20Economist%20Regime%20Change.md)]] issues.
 ![500](3a25798bbd6afb00995ba9571401c706.png)

## INTEREST RATE TREES
- The expected rate in six and twelve months are$$\begin{array}{l l l}{{E\left[r_{1}\right]}}&{{=}}&{{\frac{1}{2}r_{1, u}+\frac{1}{2}r_{1, d}=0.02305}}\\ {{}}&{{}}&{{1}}\\ {{E\left[r_{2}\right]}}&{{=}}&{{\frac{1}{4}r_{2, u u}+\frac{1}{2}r_{2, u d}+\frac{1}{4}r_{2, d d}=}}\end{array}$$
- This tree naturally translates into a tree of one period (six months) zero coupon bonds.
	- Let$$Z_{i, j}\left(k\right)$$
- be the value of a zero coupon bond at index time$i$(e.g.$i = 1$),  at node j (e.g.$j = u,  d…$) and with maturity at index$k$(e.g.$k = 2$).
- For instance
	- $Z_0 (1)$=Zero at time 0 that matures at time 1
	- $Z_{1, u} (2) =$Zero at time 1 in node up that matures at time 2
## INTEREST RATE TREES
- Recall that since steps are every 6 months:$$Z_{i, j}\left(i+1\right)=e^{-r_{i, j}{\frac{1}{2}}}$$
- We obtain
 ![500](9fc00b2f962cde641682ec21c1466826.png)Important: Note that there is a key distinction between this zero-coupon tree,  and the trees for stocks in TN 4.

## INTEREST RATE TREES VS STOCK TREES
- For instance,  suppose you assume that the stock process is given by ($q = 1/2$to move up)
 ![500](46c3bd2d4d70178950654f69122c75a5.png)
- It is always the same security whose price is quoted along the tree.
- This is important,  as if you buy the stock at time 0 for 50,  and wait one period,  you can sell it at 70 or 40 depending on the realization along the tree.

## INTEREST RATE TREES VS STOCK TREES
- This is not the case in the zero coupon tree we saw above.
	- The price along the tree is the price of a different security at each node: it is always the one period ahead zero coupon bond.
	- So,  if I buy at time$t = 0$for 0.94,  at time$t = 1$I will get 1 for sure,  and not 0.962 or 0.993.

## HOW CAN WE MODEL A PROPER TREE,  TO USE IN DERIVATIVE PRICING?
- We need more information.
- For instance,  assume that today$t=0$,  a zero coupon with maturity$T=1$(i.e.$i=2$) trades at$$Z_{0}(2)=0.9781$$
- Combining this price with the previous tree,  we obtain a tree for the bond maturing at i = 2
 ![500](75f560b25c4f945b3ba5a43b8901a783.png)
- This is a proper [asset pricing](../../Fixed%20Income%20Asset%20Pricing/Fixed%20Income%20Asset%20Pricing.md) tree,  in the sense that the security along the tree is always the same,  namely,  the bond expiring at time$i = 2$.
- Since the last payoff of any bond is always 1,  we typically do not report it.

## RISK NEUTRAL PRICING ON TREES

- At this point,  [risk neutral pricing](.md) allows us to price [derivative securities](../../Financial%20Engineering/Financial%20Mathematics%20Course.md) on the interest [rate tree](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%207/Rate%20and%20Price%20Trees.md). - As before,  we first compute the [risk neutral probability](../Review%20Session%20Notes/Binomial%20Trees%20and%20Option%20Pricing%20MBA.md) to move up the tree q∗
- The expected [risk neutral](Teaching%20Note%207-Exotic%20Options%20And%20Derivative%20Pricing%20By%20Monte%20Carlo%20Simulation.md) return to invest in the i = 2 bond is$$E^{*}\left[\frac{Z_{1}\left(2\right)}{Z_{0}\left(2\right)}\right]=q_{0}^{*}\;\frac{Z_{1, u}\left(2\right)}{Z_{0}\left(2\right)}+\left(1-q_{0}^{*}\right)\;\frac{Z_{1, d}\left(2\right)}{Z_{0}\left(2\right)}$$
- [Risk neutral pricing](.md) implies that this [expected return](../../Advanced%20Investments/Lecture%201-%20Probability%20Distributions%20of%20Returns.md) must equal the safe return of an [investment](../../Advanced%20Investments/An%20Asset%20Allocation%20Primer.md) in a zero that matures at time$i = 1$$$\underbrace{\frac{q_{0}^{*}}{Z_{0}\left(2\right)}+\left(1-q_{0}^{*}\right)}_{\mathrm{Expected~Return~on~2-period~bond}}\ =\ \frac{1}{\frac{Z_{0}\left(1\right)}{\mathrm{Return~on~1-period~Bond}}}$$
- yielding$$q_{0}^{*}=\frac{{Z_{0}\left(2\right)/Z_{0}\left(1\right)-Z_{1, d}\left(2\right)}}{{Z_{1, u}\left(2\right)-Z_{1, d}\left(2\right)}}$$
- Note that this is the same equation we found in TN4.

## RISK NEUTRAL PRICING ON TREES
- Given the [risk neutral probability](../Review%20Session%20Notes/Binomial%20Trees%20and%20Option%20Pricing%20MBA.md),  the value Vi of every traded security must satisfy$$V_{0}=Z_{0}\left(1\right)E^{*}\left[V_{1}\right]$$
- For instance,  in the example we have$$q_{0}^{*}=\frac{Z_{0}\left(2\right)/Z_{0}\left(1\right)-Z_{1, d}\left(2\right)}{Z_{1, u}\left(2\right)-Z_{1, d}\left(2\right)}=\frac{0.9781/0.9916-0.9963}{0.9808-0.9963}=0.6435$$

##### **OPTION ON INTEREST RATE**
- Suppose we want to price an option on the interest rate,  with strike r = 0.0168
- The payoffs are:$$\mathrm{pay}_{1, u}=100\times\max(r_{1, u}-\overline{r})=21.9\text{ and }\mathrm{pay}_{1, d}=100\times\max(r_{1, d}-\overline{r})=0$$$$\mathrm{Option}_{0}=Z_{0}\left(1\right)\times E^{*}\left[\mathrm{pay}_{1}\right]$$$$=0.9916\times\left(0.6435\times21.9+0.35645\times0\right)$$$$=13.97$$
##### QUESTION
- Under the [risk neutral](Teaching%20Note%207-Exotic%20Options%20And%20Derivative%20Pricing%20By%20Monte%20Carlo%20Simulation.md) probabilities,  the expected interest rate is$$E^{*}\left[r_{1}\right]=q_{0}^{*}\times r_{1, u}+(1-q_{0}^{*})\times r_{1, d}=0.0275$$
- If your boss asks you what is your forecast of the interest rate in six months,  would you tell him 2.75%?
- In the real world,  the expected interest rate was$$E\left[r_{1}\right]=2.305\%<2.75\%=E^{*}\left[r_{1}\right]$$
- Passing from the real to the [risk neutral](Teaching%20Note%207-Exotic%20Options%20And%20Derivative%20Pricing%20By%20Monte%20Carlo%20Simulation.md) world implies increasing the *expected* interest rate.

## A PROBLEM IN FINDING THE TREE FOR A BOND EXPIRING AT I = 3
- **What is then a tree for a bond expiring at** i = 3?
- Let$Z_0 (3) = 0.9615$be the current market price of a bond maturing at$T = 1.5$,  i.e.$i = 3$.
-  ![500](7abb1e6ab21ca9902f0cc70db2d7be0a.png)
- While from the interest [rate tree](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%207/Rate%20and%20Price%20Trees.md) we find Z2, j(3),  there is not an obvious way to compute Z1, j(3).
- We need **no [arbitrage](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%207/Arbitrage%20Pricing%20of%20Derivatives.md)** restrictions.
- The first no [arbitrage](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%207/Arbitrage%20Pricing%20of%20Derivatives.md) restriction is provided by the [risk neutral probability](../Review%20Session%20Notes/Binomial%20Trees%20and%20Option%20Pricing%20MBA.md)$q^∗_0$,  which implies$$Z_{0}(3)=Z_{0}(1)E^{*}\left[Z_{1}(3)\right]=Z_{0}(1)\left[q_{0}^{*}\ Z_{1, u}(3)+(1-q_{0}^{*})\ Z_{1, d}(3)\right]$$
- How can we compute$Z_{1, u}(3) \text{ and }Z_{1, d}(3)$?
- We can use the "implied tree" methodology,  discussed in TN 5.
- Let$q^∗_{1, u} \text{ and }q^∗_{1, d}$be the [risk neutral](Teaching%20Note%207-Exotic%20Options%20And%20Derivative%20Pricing%20By%20Monte%20Carlo%20Simulation.md) probabilities to move up or down the tree at time$i = 1$.
- Since the same formula as earlier applies,  we have$$\begin{aligned}q_{1, u}^{*}&=\frac{Z_{1, u}\left(3\right)/Z_{1, u}\left(2\right)-Z_{2, ud}\left(3\right)}{Z_{2, uu}\left(3\right)-Z_{2, ud}\left(3\right)}\\q_{2, d}^{*}&=\frac{Z_{1, d}\left(3\right)/Z_{1, d}\left(2\right)-Z_{2, dd}\left(3\right)}{Z_{2, du}\left(3\right)-Z_{2, dd}\left(3\right)}\end{aligned}$$
	- Choose$Z_{1, u}(3)\text{ and }Z_{1, d}(3)$so that the *current* price of the bond$Z_0(3) = 0.9615$
- Problem: We have one equation (the value of the bond) and two unknowns$Z_{1, u}(3)\text{ and }Z_{1, d}(3)$
- We need one more equation. Use for instance$q^∗_{1, u} = q^∗_{1, d} = q^∗_1$
- Practically,  then,  for every$q^∗_1$we obtain the two values of$Z_{1, u}(3)\text{ and }Z_{1, d}(3)$from the equations above,  and thus the tree
- We can find numerically (e.g. using Solver) the value$q^∗_1$such that the price of the traded security$Z_0 (3) = 0.9615$equals the "model price"$$\begin{array}{l l l}{{\widehat{Z}_{0}\left(3\right)\;=\;Z_{0}\left(1\right)\left\{q_{0}^{*}\;Z_{1, u}\left(3\right)+\left(1-q_{0}^{*}\right)\;Z_{1, d}\left(3\right)\right\}}}\\{ \mathrm{ where }}\\ {{Z_{1, u}\left(3\right)\;=\;Z_{1, u}\left(2\right)\left\{q_{1}^{*}\;Z_{2, u u}\left(3\right)+\left(1-q_{1}^{*}\right)\;Z_{2, u d}\left(3\right)\right\}}}\\ {{Z_{1, d}\left(3\right)\;=\;Z_{1, d}\left(2\right)\left\{q_{1}^{*}\;Z_{2, d u}\left(3\right)+\left(1-q_{1}^{*}\right)\;Z_{2, d d}\left(3\right)\right\}}}\end{array}$$
- We find$q_1^*=0.5912$which implies$Z_{1, u}(3)=0.959\text{ and }Z_{1, d}\left(3\right)=0.988$.
 ![500](eb7a0965b0f0a49e8b31b24a3d8d0549.png)
- In summary,  building trees to price [fixed income securities](../../Clippings/Bond%20Equivalent%20Yield%20(BEY)%20-%20Definition,%20Formula,%20and%20Example.md) is not straightforward.
- The task is made complicated from the fact that no-[arbitrage](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%207/Arbitrage%20Pricing%20of%20Derivatives.md) restrictions exist between bonds of different maturities.

## THE HO LEE MODEL
- Moving from risk natural to [risk neutral trees](Teaching%20Note%207-Exotic%20Options%20And%20Derivative%20Pricing%20By%20Monte%20Carlo%20Simulation.md) is complicated.
- The current main methodology is to build directly a [risk neutral](Teaching%20Note%207-Exotic%20Options%20And%20Derivative%20Pricing%20By%20Monte%20Carlo%20Simulation.md) tree. - A famous model is the [Ho Lee model](.md).$$r_{i+1}=r_{i}+\theta(i)\Delta\pm\sigma\sqrt{\Delta}$$
∆ occur with 1/2 ([risk neutral](Teaching%20Note%207-Exotic%20Options%20And%20Derivative%20Pricing%20By%20Monte%20Carlo%20Simulation.md)) probability.
- where$\Delta$is the time step, $\theta(i)$is a function of time chosen to match current prices,  and$\pm\sqrt{\Delta}$occur with$\frac{1}{2}$([risk neutral](Teaching%20Note%207-Exotic%20Options%20And%20Derivative%20Pricing%20By%20Monte%20Carlo%20Simulation.md)) probability.
- This process generates a recombining tree,  independently of$\theta(i)$. Starting from$r_{0}$$$r_{1, u}=r_{0}+\theta(0)\Delta+\sigma\sqrt{\Delta}$$$$r_{1, d}=r_{0}+\theta(0)\Delta-\sigma\sqrt{\Delta}$$
$$r_{2, uu}=r_{1, u}+\theta(1)\Delta+\sigma\sqrt{\Delta}$$$$r_{2, ud}=r_{1, u}+\theta(1)\Delta-\sigma\sqrt{\Delta}$$$$r_{2, du}=r_{1, d}+\theta(1)\Delta+\sigma\sqrt{\Delta}$$$$r_{2, dd}=r_{1, d}+\theta(1)\Delta-\sigma\sqrt{\Delta}$$

- It is easy to see that$r_{2, ud}=r_{2, du}=r_0+(\theta(0)+\theta(1))\Delta$

## THE HO LEE MODEL
- The tree is "implied" as follows:
- **Inputs:** (a) Time series of [short term interest rates](../Assignments/PSETS.md); (b) Current bond prices.
1. From historical [interest rates](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%202/Interest%20Rate%20Quotations.md),  obtain an estimate of$σ = st.dev(∆r_i)$
1. Then,  compute$θ(i)$recursively,  as follows
	- Use bond maturing at time$i=2$to obtain$\theta(0)$
	- Use bond maturing at time$i=3$to obtain$\theta(1)$
	- Use bond maturing at time$i=n$to obtain$\theta(n-2)$
- In order to perform this,  we must first see how to use "[risk neutral](Teaching%20Note%207-Exotic%20Options%20And%20Derivative%20Pricing%20By%20Monte%20Carlo%20Simulation.md)" trees to price bonds.

## USING RISK NEUTRAL TREES
- Assume that we built the [risk neutral](Teaching%20Note%207-Exotic%20Options%20And%20Derivative%20Pricing%20By%20Monte%20Carlo%20Simulation.md) tree already,  and we simply use it.
- Let$r_{i, j}$be the 6 month,  [continuously compounded interest](../Assignments/Solutions/PSET%207%20Solutions-Financial%20Instruments.md) rate.
- At every time (1 period = ∆ = 6 months),  there is equal [risk neutral probability](../Review%20Session%20Notes/Binomial%20Trees%20and%20Option%20Pricing%20MBA.md) ($q^∗ = 1/2$) to move up or down.
 ![500](c12efd1a89750d0a5a2d5.png)

## USING RISK NEUTRAL TREES
- From the tree, $Z_0 (1) = e^{−r_0∆} × 1 = 0.9916$
- What is the value of bond paying \$1 in one year ($i = 2$)?
- As usual,  it can be obtained by proceeding backward on the tree:
 ![500](248db1d0173d726b5947c0b764edca6d.png)

- Similarly,  a bond paying \$1 in 1.5 years ($i = 3$):
 ![500](1c77a7b826dc7915f4f19f7bd70b9d76.png)

## RISK NEUTRAL TREES

- In addition,  computers can be programmed rather easily to carry out the backward computation.
 ![500](6ca6b0c00ce70e2530e1ebf581f0ef15.png)

## CALIBRATION OF HO LEE MODEL

- Given data on [interest rates](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%202/Interest%20Rate%20Quotations.md),  I estimated a volatility$σ =0.022$
- Given data from *current* zero coupon bonds (STRIPS) as of May 25 2007,  we can compute iteratively θ(i) so that [model prices](../../Credit%20Markets/Credit%20Markets%20Session%204.md) equal actual prices for every i.
- In the example below,  I am only showing the model price for T = 5 bond.
 ![500](ee690048ac68710cb1544510ad1acd5c.png)

## INTERMEDIATE CASH FLOWS

- Notice that given a tree,  we can insert any type of known [cash flow](../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%201%20-%20Purpose%20and%20Structure%20of%20Financial%20Markets/Preview%20of%20the%20Book.md). - Specifically,  at any time-node (*i,  j*),  we just must add the CF$$P_{i, j}=e^{-r_{i, j}\Delta}\left(\frac{1}{2}P_{i+1, j}+\frac{1}{2}P_{i+1, j+1}+C F_{i+1}\right)$$
- So,  for example,  a 1.5 year,  4% coupon bond is just given by
 ![500](3cc18b0dcddbeff077a5896cc1c8a280.png)
- This tree gives "ex-coupon" prices.
## EXAMPLE: CALLABLE BONDS
- Trees turn out to be very useful tools (not only pedagogically).
- One of the most important features of them is the ability to deal with "American options."
- As a consequence,  a very simple application of the "tree" methodology is the computation of prices of callable bonds.
- Consider the 1.5 year,  4% coupon bond we discussed earlier,  but assume it is callable at par
- That is,  at any point in time before maturity,  the issuer (Treasury) may "call it back" in exchange of 100.
- In general,  bonds become callable after some period of time.
- For example,  the Nov 2012 Treasury bond is callable at par starting on Nov 2007.
- If the issuer calls the bond between coupon days,  it has to pay the [accrued interest](../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%202%20-%20Spot%20Markets/Intra-Year%20Compounding%20and%20Day-Count.md) to the bond holder.

## EXAMPLE: CALLABLE BONDS - HOW DO WE COMPUTE THE PRICE OF THE IMPLICIT AMERICAN OPTION?

- At any node (*i,  j*) the issuer can decide whether to "exercise" option or wait.
- If [exercises](../../Financial%20Markets/Financial%20Asset%20Pricing%20Theory%20Overview/Chapter%2012%20-%20Derivatives/Exercises.md),  the payoff (= value of the option) is$$C a l l_{i, j}^{\mathrm{Ex}}=P_{i, j}-100$$
- If waits,  the value of the option$$C a l l_{i, j}^{\mathrm{Wait}}~=~e^{-r_{i, j}\Delta}E^{*}\left[C a l_{i+1}\right]=e^{-r_{i, j}\Delta}\left(\frac{1}{2}C a l_{i+1, j}+\frac{1}{2}C a l_{i+1, j+1}\right)$$
- Therefore,  the value at node *i,  j* is$$Call_{i, j}=\max\left(Call_{i, j}^{\rm Wait}, Call_{i, j}^{\rm Ex}\right)$$$$=\max\left(e^{-r_{i, j}\times\Delta}E^{*}\left[Call_{i+1}\right], P_{i, j}-100\right)$$

-  At maturity $I=T/\Delta$ we have $$Call_{I, j}=0\mbox{ for all }j$$
 ![500](028f1eeb379ef6236ccfc204a15cd928.png)

## EXAMPLE: CALLABLE BONDS
##### WHAT IS THEN THE PRICE OF THE CALLABLE BOND?
- The buyer of a callable bond is: (1) buying a non-callable bond; + (2) Selling a call to the issuer.
- Hence,$$\begin{array}{l l l}{{P_{0}^{\mathbf{Call}}\left(3\right)}}&{{=}}&{{P_{0}^{\mathbf{NoCall}}\left(3\right)-C_{0}\left(3\right)}}\\ {{}}&{{=}}&{{101.93-1.16}}\\ {{}}&{{=}}&{{100.77}}\end{array}$$
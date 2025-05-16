---
tags:
  - american_option
  - call_option
  - european_option
  - option_payoff
  - put_option
aliases:
  - Call and Put Payoffs
  - Option Payoffs at Expiry
key_concepts:
  - American options
  - Call option payoff
  - European options
  - Put option payoff
  - Strike price
---

# 5.1 CALL AND PUT PAYOFFS AT EXPIRY  

Tickets sold by national lotteries around the world are bets on sets of numbers. The payoff is a. fixed monetary amount if the ticket buyer guesses the right combination. Such bets are called. binary or digital. It does not matter how "close" he is to the right combination, all that matters is whether he is right or wrong in guessing five or six numbers..  

Most options sold in [financial markets](../../../../Financial%20Markets%20and%20Institutions/Financial%20Markets%20and%20Institutions%20Lecture%20Notes.md) work a little differently. There is also the right and the wrong guess, but, the person who bets is right, the "more right' he is the more he gets.  

![](48ebe88890837c0b94bd80ec563315212655a0e8b07c49f4e092820fad5adb30.jpg)  
Figure 5.1 Payoff on a call and a put at expiry. $K=\mathrm{S}$ trike price; $S={\mathrm{Spot}}$ price at expiry  

A call option on a price of an asset (e.g. stock) pays on the expiry date the greater of zero and the difference between the asset's price and a prespecified [strike price](.md) (bet level). If we think that the price of ABC will go over $\$60$ per share, we buy a call struck at 60. If the price on the expiry date is 67, we get $\$7$ ; if the price is 74, we get $\$14$ . If the price ends up below 60, whether at 40 or 50, we get nothing. A put option on a price of an asset pays on the expiry date the greater of zero and the difference between a prespecified strike price and that asset's price. If we want to bet that the price of ABC will go under $\$60$ per share, we buy a put struck at 60. If the price on the expiry date is 47, we get $\$13$ ; if the price is 54, we get $\$6$ If the price is above 60, whether at 65 or 80, we get nothing. We graph the payoff that the buyer of the option (bet) gets as a function of the [underlying asset](../../../../Financial%20Instruments/Financial%20Derivatives%20and%20Quantitative%20Methods/Risk%20Neutral%20Pricing%20of%20Options.md)'s price in the following payoff diagrams in Figure 5.1.  

Options that pay only at expiry are called European. Those that pay prior to and on the expiry date are called American. Neither notion has any connection to a location.  

At any given time, there may be options trading on the same [underlying asset price](../../../../Financial%20Instruments/Black%20Scholes%20Derivation.md) (event), but with different strikes and expiry dates. On the exchanges, options follow a certain schedule. of dates and strikes. Over the counter, they can be arranged for any payoff date and strike (bet level). The intrinsic value of an option is defined as the payoff the option would have if it were immediately exercisable at today's price of the [underlying asset](../../../../Financial%20Instruments/Financial%20Derivatives%20and%20Quantitative%20Methods/Risk%20Neutral%20Pricing%20of%20Options.md). Options with a positive intrinsic value are called in-the-money; options with no intrinsic value are called out-of-themoney; options whose [strike price](.md) is equal to the [asset price](../../../Financial%20Asset%20Pricing%20Theory%20Overview/Chapter%204%20-%20State%20Prices/A%20Preview%20of%20Alternative%20Formulations.md) are called at-the-money. Note that options cannot have a negative intrinsic value. If the better is wrong he simply does not exercise his option and gets no payoff..  

Most individual stock options and many others have a [physical settlement](../Chapter%203%20-%20Futures%20Markets/Fundamentals%20of%20Futures%20and%20Forwards.md) provision; that is they are not pure bets, but give the holders (option buyers) the right to buy (call) or sell (put) the asset to the option writer (option seller) at the [strike price](.md) on (or prior to) the expiry date. This is tantamount to receiving the payoffs as described above. For example, a 60 call, when the price is 67, gives the holder the right to buy the stock from the writer for 60 ([exercise price](../../../Financial%20Asset%20Pricing%20Theory%20Overview/Chapter%2012%20-%20Derivatives/Options.md)). Once bought, the holder can sell the stock immediately for 67 in the spot market (open market), realizing a profit of 7. A 60 put, when the price is 47, gives the holder the right to sell the stock to the writer for 60 ([exercise price](../../../Financial%20Asset%20Pricing%20Theory%20Overview/Chapter%2012%20-%20Derivatives/Options.md)). To deliver, the holder can buy the stock immediately for 47 in the spot market (open market), realizing a profit of 13. Many options written on non-price financial variables (stock indices, [interest rates](../../../Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%202/Interest%20Rate%20Quotations.md), etc.) are settled in cash. The settlement of options is in general similar to that of [futures](../Chapter%203%20-%20Futures%20Markets/Futures%20Not%20Subject%20to%20Cash-And-Carry.md), cash or physical. One always needs to check contract provisions for both, as they may not follow the same rules.  
---
cssclasses:
  - academia
Owner: RRoger Lin
title: Notes on Basic Options Properties
tags:
  - call_options
  - option_bounds
  - option_parameters
  - option_payoffs
  - option_pricing
  - options_basics
  - put_options
  - underlying_security
aliases:
  - Basic Options
  - Call and Put
  - Option Fundamentals
  - Option Properties
key_concepts:
  - 'Call: Right to buy'
  - Option buyer/holder
  - Option payoff schemes
  - Option price bounds
  - Option seller/writer
  - Option value parameters
  - 'Options: Right to buy/sell'
  - 'Put: Right to sell'
  - Underlying security
---

# Notes on Basic Options Properties

   [Options](../../Financial%20Markets/Financial%20Asset%20Pricing%20Theory%20Overview/Chapter%2012%20-%20Derivatives/Options.md)

[Financial Instruments]([A%20Practical%20Guide%20for%20Actuaries%20and%20other%20Business%20Professionals.)](Financial%20Instruments.md)

[Basic Options Properties](.md)

# NOTE ON BASIC OPTION PROPERTIES

   Options are contracts that give the right,  but not the obligation,  to either buy or sell a specific underlying security for a specified price on or before a specific date.

   This note takes its cue from this fundamental option definition to explain the basics of options. It will cover [fundamentals](../../Advanced%20Financial%20Analysis%20and%20Valuation/Lecture%20Notes%20Advanced%20Financial%20Analysis%20and%20Valuation/Week%202/Week%202%20Fundamentals%20Of%20Forecasting.md) such as the payoff schemes of options,  parameters that influence their value,  the parity between put and call options,  and also the upper and lower bounds of options prices. Before we jump into all that,  however,  let's start with a basic example that shows how options work.

   Say that you are interested in owning stock in Acme,  Inc. Currently,  Acme's shares trade at$100,    which you think is low. You believe the stock should be valued more highly and that its price soon will rise. If you bought now and sold it later,    you would therefore make money. However,    you are not completely sure,    so rather than outright buying the stock,    you buy an option from someone who does own Acme stock. The option contract gives you the right to buy the stock at$100,  no matter what the actual [stock price](../../Financial%20Engineering/Derivatives/Part%20IV%20-%20Options/Chapter%2016%20-%20Black–Scholes%20Model.md) is,  before a certain end date specified in the contract. Of course,  you have to pay an up-front fee to the person who owns the stocks and who might have to part with them. Note that you actually do not own the underlying stock just because you purchased an option. The option derives its value (which is why we call it a derivative instrument) from the stock,  but it is not the stock itself. The party who sold you the option contract still holds the stock; what you have is a promise to own the stock later should the share price rise above the level you picked. Your contract also specifies an ending time,  after which the option is no longer valid.

   In theory,  options can be written on almost any type of underlying security. Equity (stock) is the most common,  but there are also several types of non-equity options,  based on securities such as bonds,  foreign [currency](../../Financial%20Instruments/Lecture%20Notes-%20Financial%20Instruments/Teaching%20Note%201-%20Forward%20Rates%20Agreement/Forwards%20and%20Futures%20Notes.md),  financial indices,  or physical goods such as gold or coffee. This note will primarily deal with equity options.

   People normally trade in options to speculate in the change in value of the underlying security. For instance,  the person who sold you the option on Acme's stock is probably speculating that the [stock price](../../Financial%20Engineering/Derivatives/Part%20IV%20-%20Options/Chapter%2016%20-%20Black–Scholes%20Model.md) will not rise above$100. If the price is below$100 by the end of your contract,  the seller can then simply pocket the up-front fee—or premium—that you paid. You,  on the other hand,  speculate that it will rise.

   The person who buys an option is normally called the "buyer" or "holder." Conversely,  the seller is known as the "seller" or "writer." Stock option contracts generally represent 100 shares of the underlying stock. Options do not have to be purchased directly from the person or company that either owns the security or wrote the initial options contract—they also trade extensively in the [secondary market](../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%201%20-%20Purpose%20and%20Structure%20of%20Financial%20Markets/Primary%20Issuance%20and%20Secondary%20Resale%20Markets.md). Options are traded both in public markets,  on organized exchanges such as the Chicago Board Options Exchange and Deutsche Börse's EUREX,  and in the so-called Over-theCounter (OTC) market,  where financial actors such as [investment](../../Advanced%20Investments/An%20Asset%20Allocation%20Primer.md) banks,  corporate treasurers,  and fund managers trade directly with one another over the phone or via interconnected computer systems. The public markets primarily trade standardized equity options. The OTC market trades all other types of options,  plus equity options of large sizes or with unusual characteristics.

## CALL AND PUT OPTIONS

   The Acme option you just bought gave you the right to purchase stock. In the options industry,  this is known as a call option. Conversely,  if you owned stocks,  you could buy the right to sell them at a certain price,  known as a put option. Let's describe each of these two option types in more detail.

### CALL OPTIONS

   A call option is the right (but not the obligation) to buy the underlying security at a specific price (known as the exercise or [strike price](../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%205%20Options%20on%20Prices%20and%20Hedge-Based%20Valuation/Call%20and%20Put%20Payoffs%20at%20Expiry.md)) before a certain date (the expiration or exercise date). If you have the right to exercise the option before the exercise date,  it is known as an "American" option; if you can exercise only on the [expiration date](../../Financial%20Instruments/Financial%20Derivatives%20and%20Quantitative%20Methods/Risk%20Neutral%20Pricing%20of%20Options.md) itself,  it is a "European" option. If the call option is on equity,  one option normally gives you the right to purchase 100 shares of the underlying stock.

   Investors who believe that the value of the underlying will increase before the [expiration date](../../Financial%20Instruments/Financial%20Derivatives%20and%20Quantitative%20Methods/Risk%20Neutral%20Pricing%20of%20Options.md) usually buy call options. It gives them the possibility of buying stock below future market prices. For instance,  let's assume that the Acme option you bought was an "Acme April 100 call option." It gives you the right to buy 100 shares of Acme at any time before the April [expiration date](../../Financial%20Instruments/Financial%20Derivatives%20and%20Quantitative%20Methods/Risk%20Neutral%20Pricing%20of%20Options.md). If the price of Acme shares rose to$110 before the expiration date,    you could exercise your option and buy the stock. If you then immediately sold the stock,    you would realize a profit of$10 per share.

### PUT OPTIONS

   A put option is the call option's opposite. A put option gives the right,  but not the obligation,  to sell the underlying security at a specific price on or before the [expiration date](../../Financial%20Instruments/Financial%20Derivatives%20and%20Quantitative%20Methods/Risk%20Neutral%20Pricing%20of%20Options.md). A put becomes more valuable if the price of the underlying falls. For example,  assume you own 100 Acme shares and that you buy an "Acme April 100 put option." This gives you the right to sell your 100 shares of Acme at a [strike price](../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%205%20Options%20on%20Prices%20and%20Hedge-Based%20Valuation/Call%20and%20Put%20Payoffs%20at%20Expiry.md) of$100 on or before the April expiration. Say that the Acme shares drop to$80 during the option term. You can then realize a profit of$20 per share by exercising the option,    since it guarantees you a price of$100. Just as a call option allows you to speculate in rising stock prices,  a put option lets you speculate in falling stock prices.

   Note that in this example you speculated against stock that you already owned,  known as a "covered option." You can actually trade options for stock that you do not own,  known as a "naked option." If you exercised the put option and had to deliver the actual stock,  you would have to purchase the stock in a separate transaction.

### OPTION PAYOFFS: AT THE MONEY,  IN THE MONEY,  OR OUT OF THE MONEY

   The payoff patterns for [call and put](.md) options naturally differ—simply said,  they are each other's opposites. Figure A shows a typical payoff pattern for a call option. Based on our Acme example,  the call option does not start to pay off unless the [stock price](../../Financial%20Engineering/Derivatives/Part%20IV%20-%20Options/Chapter%2016%20-%20Black–Scholes%20Model.md) goes above the [strike price](../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%205%20Options%20on%20Prices%20and%20Hedge-Based%20Valuation/Call%20and%20Put%20Payoffs%20at%20Expiry.md) of$100.

   Figure A Payoff

![image3](Attachments/image3.jpg)

   > Source: Casewriters.

   The reverse payoff relationship is true for a put option,  as shown in Figure B. The option has a positive payoff as long as the [stock price](../../Financial%20Engineering/Derivatives/Part%20IV%20-%20Options/Chapter%2016%20-%20Black–Scholes%20Model.md) is below$100. If it hits$100 or more,  though,  the option becomes valueless to the holder,  who will choose not to exercise it since it has zero payoff.

![image4](Attachments/image4.png)

   Figure B Payoff for a Put Option

   Note that the payoff schemes above are for when you buy options: in trader jargon,  holding or going long the options. If you instead short the options (same as writing or selling an option),  you have the exact same payoff multiplied by a negative one; for instance,  the payoff for a short call is negative 10 if the [stock price](../../Financial%20Engineering/Derivatives/Part%20IV%20-%20Options/Chapter%2016%20-%20Black–Scholes%20Model.md) is 110,  while the payoff to the holder of the option is plus 10.

   When traders talk about the payoffs of options,  they often discuss whether an option is at the money,  in the money,  or out of the money. At the money is the easiest concept to understand: it occurs when the price of the underlying security is equal to the [strike price](../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%205%20Options%20on%20Prices%20and%20Hedge-Based%20Valuation/Call%20and%20Put%20Payoffs%20at%20Expiry.md). For both figures above,  the at-the-money level is$100.

   When an option is in the money,  the option holders gain a profit if they exercise the option. For a call option,  in the money is when the [strike price](../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%205%20Options%20on%20Prices%20and%20Hedge-Based%20Valuation/Call%20and%20Put%20Payoffs%20at%20Expiry.md) is less than the market price of the underlying security. In Figure A this happens to the right of the$100 level. Conversely,    the put option is in the money if the strike price is greater than the market price of the underlying security. In Figure B this is the area to the left of the$100 level.

   Being out of the money is when the option holder would not gain a profit if the option was exercised. A holder of an option that reaches expiration and is out of the money simply does not exercise the option. There is no loss associated with not exercising,  except the loss of the fee that the holder paid to own the option. Out of the money is the opposite of in the money for both option types; a call option is out of the money if the [strike price](../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%205%20Options%20on%20Prices%20and%20Hedge-Based%20Valuation/Call%20and%20Put%20Payoffs%20at%20Expiry.md) is greater than the market price of the underlying security,  and a put option is out of the money if the [strike price](../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%205%20Options%20on%20Prices%20and%20Hedge-Based%20Valuation/Call%20and%20Put%20Payoffs%20at%20Expiry.md) is less than the market price of the underlying security.

### OPTION TERMINOLOGY

   Since options convey the right but not the obligation to sell or buy,  you always have the choice of not exercising your options. Also,  instead of exercising an option,  you can choose to sell it in the options market,  a move normally referred to as "closing a position."

   Other terminology you hear in the market is "going long" or "[going short](../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%202%20-%20Spot%20Markets/Short%20Selling.md)" an option. In its most basic form it simply means owning (going long or taking a [long position](../../Financial%20Engineering/Derivatives/Part%20I%20-%20Forwards%20and%20Futures/Chapter%204%20-%20Futures:%20Hedging%20and%20Speculation.md)) or selling ([going short](../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%202%20-%20Spot%20Markets/Short%20Selling.md) or [shorting](../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%202%20-%20Spot%20Markets/Short%20Selling.md)) the option. A "short call" means a sale of a call option; a "long call" means a purchase of a call option. Note that you can actually take a short-like position by buying a put option on stocks that you do not own. You then potentially make a profit by later buying the stocks at a lower price than you are about to sell them for. The term "short selling,  " then,  generally refers to sales of a security that the seller does not own,  or any sale that is completed by the delivery of a security borrowed by the seller. The opposite of "selling short" is "going long."

   In general,  combining [long and short positions](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%2013/Market%20Size%20and%20Participants.md) in various stocks and options is the basis for common [trading strategies](../Quantitative%20Trading%20Strategies%20Lecture%20Notes.md).

   > Other common options terms (some of which we have already encountered) are:

   - Underlying interest or security: The security (such as stock,  commodity,  or index) on which an option is written and traded.
   - Expiry,  expiration,  or maturity date: The date that the option expires and the option seller ceases to have an obligation to honor the options contract. (A related expression is expiry cycle,  which refers to the month or week that the option expires.)
   - Exercise or [strike price](../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%205%20Options%20on%20Prices%20and%20Hedge-Based%20Valuation/Call%20and%20Put%20Payoffs%20at%20Expiry.md): The price at which the underlying security can be bought or sold.
   - Exercise style (American and European options): We know that an option holder has the right to exercise the option—but it differs between options exactly when the holder has the right to do so. If the option only can be exercised on the [expiration date](../../Financial%20Instruments/Financial%20Derivatives%20and%20Quantitative%20Methods/Risk%20Neutral%20Pricing%20of%20Options.md) itself,  it is known as a European-style option. If it can be exercised anytime leading up to the expiry date,  it is called an American-style option. Most options in developed markets are of the American type.
   - Trading hours: The days and hours that options are bought and sold. Related is the term "last trading day,  " which is the last day that your option can be bought or sold.

   > Option premium: Another word for the price of the option. It is paid by the buyer to the writer,  or seller,  of the option. The writer keeps the premium whether or not the option is exercised. You can look at it like this: Since writers lose whenever option buyers find it to their advantage to exercise an option,  the writer wants an up-front payment to be compensated for this possible future exposure.

## OPTION VALUE SENSITIVITIES

   It is common to say that the value of an option,  as it is being issued and also as it trades in the [secondary market](../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%201%20-%20Purpose%20and%20Structure%20of%20Financial%20Markets/Primary%20Issuance%20and%20Secondary%20Resale%20Markets.md),  depends on six important parameters. Since an option is a derivative security—it derives its value from an [underlying asset](../../Financial%20Instruments/Financial%20Derivatives%20and%20Quantitative%20Methods/Risk%20Neutral%20Pricing%20of%20Options.md)—the price of the [underlying asset](../../Financial%20Instruments/Financial%20Derivatives%20and%20Quantitative%20Methods/Risk%20Neutral%20Pricing%20of%20Options.md) is naturally a very important influence on the value of the option,  but it is not the only one.

   [Stock price](../../Financial%20Engineering/Derivatives/Part%20IV%20-%20Options/Chapter%2016%20-%20Black–Scholes%20Model.md) For an equity option,  the price of the underlying stock is naturally the most important influence on its value. The relationship is easy to understand and is,  as always,  the opposite for [call and put](.md) options. We said earlier that call options are in the money if the [stock price](../../Financial%20Engineering/Derivatives/Part%20IV%20-%20Options/Chapter%2016%20-%20Black–Scholes%20Model.md) exceeds the [strike price](../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%205%20Options%20on%20Prices%20and%20Hedge-Based%20Valuation/Call%20and%20Put%20Payoffs%20at%20Expiry.md). Call options therefore become more valuable as the underlying stock's price increases. Put options,  by contrast,  become more valuable as the underlying [stock price](../../Financial%20Engineering/Derivatives/Part%20IV%20-%20Options/Chapter%2016%20-%20Black–Scholes%20Model.md) decreases.

   [Strike price](../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%205%20Options%20on%20Prices%20and%20Hedge-Based%20Valuation/Call%20and%20Put%20Payoffs%20at%20Expiry.md) The [strike price](../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%205%20Options%20on%20Prices%20and%20Hedge-Based%20Valuation/Call%20and%20Put%20Payoffs%20at%20Expiry.md) also influences the option value. Referring to Figure A,  assume that the [stock price](../../Financial%20Engineering/Derivatives/Part%20IV%20-%20Options/Chapter%2016%20-%20Black–Scholes%20Model.md) of a call option did not move—but that its [strike price](../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%205%20Options%20on%20Prices%20and%20Hedge-Based%20Valuation/Call%20and%20Put%20Payoffs%20at%20Expiry.md) did. If the [strike price](../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%205%20Options%20on%20Prices%20and%20Hedge-Based%20Valuation/Call%20and%20Put%20Payoffs%20at%20Expiry.md) increased,  it would require an increasingly higher [stock price](../../Financial%20Engineering/Derivatives/Part%20IV%20-%20Options/Chapter%2016%20-%20Black–Scholes%20Model.md) for the option to move into the money. In other words,  the value of the call option decreases as the [strike price](../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%205%20Options%20on%20Prices%20and%20Hedge-Based%20Valuation/Call%20and%20Put%20Payoffs%20at%20Expiry.md) increases. As always,  the opposite holds for the put option: as the [strike price](../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%205%20Options%20on%20Prices%20and%20Hedge-Based%20Valuation/Call%20and%20Put%20Payoffs%20at%20Expiry.md) increases in value,  the put option value increases.

   Volatility Volatility measures how much the value of the underlying is expected to fluctuate (rise and/or fall) over time. Exactly how to calculate volatility is beyond the scope of this note,  but in broad terms there are two ways to estimate volatility in the market: historical volatility (based on past price activity) and [implied volatility](../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%205%20Options%20on%20Prices%20and%20Hedge-Based%20Valuation/A%20Real-Life%20Option%20Pricing%20Exercise.md) (starts with the option price as a given and works backwards given a [pricing](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%207/Arbitrage%20Pricing%20of%20Derivatives.md) model to deduct the volatility). The more volatile the future is assumed to be,  the higher the value for both [call and put](.md) options. The magnitude and direction of the underlying price movement,  however,  has differential value impacts for calls and puts. For a call option,  large increases in stock prices translate into higher value,  whereas large decreases in stock prices only result in a small limited loss (the price of the option itself). For a put option,  the opposite is true: large decreases in stock prices result in increased value,  whereas large increases only lead to a limited loss.

   [Time to maturity](../../Financial%20Instruments/Lecture%20Notes-%20Financial%20Instruments/Teaching%20Note%201-%20Forward%20Rates%20Agreement/Hedging%20Strategies%20with%20Forwards.md) Also known as [time to expiration](../../Financial%20Engineering/Derivatives/Part%20IV%20-%20Options/Chapter%2016%20-%20Black–Scholes%20Model.md),  this is the only parameter of the six that is different for Europeanand American-style options. Consider first the American option,  which can be exercised at any point up to its [expiration date](../../Financial%20Instruments/Financial%20Derivatives%20and%20Quantitative%20Methods/Risk%20Neutral%20Pricing%20of%20Options.md). Its value—both for [call and put](.md) options—increases as the [time to expiration](../../Financial%20Engineering/Derivatives/Part%20IV%20-%20Options/Chapter%2016%20-%20Black–Scholes%20Model.md) increases. The reason is intuitive: an option with a longer [time to maturity](../../Financial%20Instruments/Lecture%20Notes-%20Financial%20Instruments/Teaching%20Note%201-%20Forward%20Rates%20Agreement/Hedging%20Strategies%20with%20Forwards.md) than an otherwise identical option must have at least the same value—and then a little more.

   The European-style options behave for the most part in the same way as the American,  but they have one complication. Take two European call options written on the same underlying stock,  one with a two-month [time to maturity](../../Financial%20Instruments/Lecture%20Notes-%20Financial%20Instruments/Teaching%20Note%201-%20Forward%20Rates%20Agreement/Hedging%20Strategies%20with%20Forwards.md) and the other with four months to expiration. Assume now that a large dividend is due in three months. According to normal market behavior,  the [stock price](../../Financial%20Engineering/Derivatives/Part%20IV%20-%20Options/Chapter%2016%20-%20Black–Scholes%20Model.md) will decline on the ex-dividend date,  which as we know means that a call option becomes less valuable. However,  this is only true for the longer-term option. The option with a two-month [time to maturity](../../Financial%20Instruments/Lecture%20Notes-%20Financial%20Instruments/Teaching%20Note%201-%20Forward%20Rates%20Agreement/Hedging%20Strategies%20with%20Forwards.md) will not be affected by the dividend,  so its value is therefore not affected. Consequently,  there is no way to generalize the time-to-maturity parameter's impact on European-style options.

   [Interest rate Changes](../../International%20Finance/Bridgewater/How%20Countries%20Go%20Broke/How%20Countries%20Go%20Broke-Chapter%2012%20to%20Chapter%2014.md) in the risk-free interest ratel affect the option value in a rather complicated way. If the interest rate increases independently of the other parameters,  including [stock price](../../Financial%20Engineering/Derivatives/Part%20IV%20-%20Options/Chapter%2016%20-%20Black–Scholes%20Model.md),  the preset value of a call option (put option) will increase (decrease). However,  in practice,  when [interest rates](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%202/Interest%20Rate%20Quotations.md) go up they usually have a negative impact on stock prices. The combined effect is therefore not clear from one time to another.

   Dividends As mentioned for the time-to-maturity parameter,  a stock that pays a dividend will drop in value on the ex-dividend date. This means that the dividends expected during the life of the option will make call options lose in value and put options increase in value.

   Table A below summarizes the description of the six factors. It shows what happens to the value of an American-style option (one that can be exercised at any point up to its expiry) when each factor increases. Note that the table assumes that one factor changes while the others remain fixed; as we discussed for the interest rate factor,  the connection can be more complicated at times. Furthermore,  remember that a European-style option will behave almost the same way as an American option. The one exception is that for European-type options there is no certain relationship with [time to maturity](../../Financial%20Instruments/Lecture%20Notes-%20Financial%20Instruments/Teaching%20Note%201-%20Forward%20Rates%20Agreement/Hedging%20Strategies%20with%20Forwards.md). For example,  if the maturity date is pushed forward,  the extended [time to maturity](../../Financial%20Instruments/Lecture%20Notes-%20Financial%20Instruments/Teaching%20Note%201-%20Forward%20Rates%20Agreement/Hedging%20Strategies%20with%20Forwards.md) might include an extra dividend payment,  which would negatively affect a call option.

   Table A Impact on Option Prices (American-Style Option)

![image5](Attachments/image5.jpg)

## PAYOFFS FOR STOCKS AND BONDS

   Above we showed the payoff for [call and put](.md) options. For completeness,  let's compare these with the payoff for stocks (equity) and risk-free bonds (debt). Figure C shows the profit potential that comes from owning stock in a company. As the [stock price](../../Financial%20Engineering/Derivatives/Part%20IV%20-%20Options/Chapter%2016%20-%20Black–Scholes%20Model.md) increases,  the payoff increases just as much; if the stock goes up by$50,    the profit also increases by$50. The slope of the payoff line is,  in other words,  one.

   The payoff for a risk-free bond is different. Figure D shows the profit potential of a zero-coupon bond (one that makes no interest payments to the bondholder). As the line shows,  no matter how the [stock price](../../Financial%20Engineering/Derivatives/Part%20IV%20-%20Options/Chapter%2016%20-%20Black–Scholes%20Model.md) changes,  the bondholder only receives the principal value of the bond when the bond matures (in the figure,  the assumed [principal amount](../../Financial%20Instruments/Financial%20Derivatives%20and%20Quantitative%20Methods/HSBC-Auto%20callable%20Barrier%20Notes%20with%20Step-up%20Premium.md) is$60). Since the [stock price](../../Financial%20Engineering/Derivatives/Part%20IV%20-%20Options/Chapter%2016%20-%20Black–Scholes%20Model.md) has no impact on the bond value,  the line is flat.

![image7](Attachments/image7.jpg)

## PUT-CALL PARITY

   We have now looked at the payoff schemes for options,  stocks,  and bonds,  and we have also covered how the value of an option is affected by parameters such as stock and [strike price](../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%205%20Options%20on%20Prices%20and%20Hedge-Based%20Valuation/Call%20and%20Put%20Payoffs%20at%20Expiry.md). Combining these schemes will help illustrate an important option concept known as [put-call parity](../../Financial%20Engineering/7.%20Black%20Scholes%20Model.md). As the word "parity" conveys,  there exists a type of equivalence between put and call options; it specifies the relationship between the prices of European call options and European put options of the same class (that is,  with the same underlying security,  [strike price](../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%205%20Options%20on%20Prices%20and%20Hedge-Based%20Valuation/Call%20and%20Put%20Payoffs%20at%20Expiry.md),  and [expiration date](../../Financial%20Instruments/Financial%20Derivatives%20and%20Quantitative%20Methods/Risk%20Neutral%20Pricing%20of%20Options.md)). Note that the parity relationship only holds for European options and not for American (which can be exercised before their maturity date).

   The parity relationship states that the value of a European call with a certain [strike price and maturity](../../Financial%20Instruments/Payoffs%20to%20Plain%20Vanilla%20Options.md) can be deduced from the value of a European-style put option with the same [strike price and maturity](../../Financial%20Instruments/Payoffs%20to%20Plain%20Vanilla%20Options.md) (and vice versa.). A common way of explaining [put-call parity](../../Financial%20Engineering/7.%20Black%20Scholes%20Model.md) is to compare two portfolios. The first [portfolio](../../Advanced%20Investments/An%20Asset%20Allocation%20Primer.md) consists of a stock. The second [portfolio](../../Advanced%20Investments/An%20Asset%20Allocation%20Primer.md) consists of a long call option,  a short put option,  1 and a zero-coupon bond. The call and the put have the same [strike price and maturity](../../Financial%20Instruments/Payoffs%20to%20Plain%20Vanilla%20Options.md),  while the bond's maturity matches those of the options and its [principal amount](../../Financial%20Instruments/Financial%20Derivatives%20and%20Quantitative%20Methods/HSBC-Auto%20callable%20Barrier%20Notes%20with%20Step-up%20Premium.md) equals their [strike price](../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%205%20Options%20on%20Prices%20and%20Hedge-Based%20Valuation/Call%20and%20Put%20Payoffs%20at%20Expiry.md). The key observation is that the two portfolios have exactly the same payoff at the maturity of the options/bond. Because they have the same value at maturity no matter what the [stock price](../../Financial%20Engineering/Derivatives/Part%20IV%20-%20Options/Chapter%2016%20-%20Black–Scholes%20Model.md) is at that time,  their present values must then also be the same. This is the [put-call parity](../../Financial%20Engineering/7.%20Black%20Scholes%20Model.md).

   As an alternative way of explaining [put-call parity](../../Financial%20Engineering/7.%20Black%20Scholes%20Model.md),  Figure E shows the [portfolio](../../Advanced%20Investments/An%20Asset%20Allocation%20Primer.md) [replication](../../Financial%20Instruments/Financial%20Derivatives%20and%20Quantitative%20Methods/Forward%20and%20Futures%20Contracts.md) argument graphically. It combines the payoffs of a long call option,  a short put option,  and a bond to form the stock payoff. In the graphs,  the line crosses the X-axis at the [strike price](../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%205%20Options%20on%20Prices%20and%20Hedge-Based%20Valuation/Call%20and%20Put%20Payoffs%20at%20Expiry.md),  K. First,  combining a call option and a short put option gives the straight line of the stock payoff chart. However,  relative to the stock payoff,  its payoff is everywhere lower by a value of K. If we add the bond payoff,  this then brings the whole line back up by K,  making the net payoff intersect the X and Y axes at the origin (the 0/0 intersection of the two axes).

![image8](Attachments/image8.jpg)

   Figure E [Put-Call Parity](../../Financial%20Engineering/7.%20Black%20Scholes%20Model.md)

   As the figure shows,  combinations of options can create positions that are the same as holding the stock itself—this is the core of financial engineering. By using a call,  a put,  and a bond,  we are able to synthetically construct a stock,  or put differently,  assemble a [portfolio](../../Advanced%20Investments/An%20Asset%20Allocation%20Primer.md) that replicates the payoff of the stock in the future. Therefore,  for no arbitrage2 opportunities to exist,  the [portfolio](../../Advanced%20Investments/An%20Asset%20Allocation%20Primer.md)'s present value must equal the stock's present value. So,  the value of the call minus the value of the put plus the value of the bond must equal the value of the stock. This can be expressed as follows:

   S = C(K) - P(K) + PV (K) [1]

   > where:

   - S = stock
   - C = call option
   - P = put option
   - PV = present (or discounted) value of the bond (whose payoff at maturity is K) K = [strike price](../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%205%20Options%20on%20Prices%20and%20Hedge-Based%20Valuation/Call%20and%20Put%20Payoffs%20at%20Expiry.md)

   	 ![image9.jpg](image9.jpg)

   In other words,  if you know the value of three of the parameters,  you can deduce the value of the fourth. Suppose you want to know the value of a call option,  and you know the value of an equivalent put option,  the [risk-free interest rate](../../Financial%20Markets/Financial%20Asset%20Pricing%20Theory%20Overview/Chapter%2012%20-%20Derivatives/Exercises.md),  and the [stock price](../../Financial%20Engineering/Derivatives/Part%20IV%20-%20Options/Chapter%2016%20-%20Black–Scholes%20Model.md). Plug the values into the formula,  and you receive the value of the call option.

### PUT-CALI PARITY IN USE

   What [put-call parity](../../Financial%20Engineering/7.%20Black%20Scholes%20Model.md) helps us do is to price,  for instance,  a put option as long as we know the price of a call option on the same underlying and with the same [strike price](../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%205%20Options%20on%20Prices%20and%20Hedge-Based%20Valuation/Call%20and%20Put%20Payoffs%20at%20Expiry.md) and [expiration date](../../Financial%20Instruments/Financial%20Derivatives%20and%20Quantitative%20Methods/Risk%20Neutral%20Pricing%20of%20Options.md). Let's exemplify using the formula above. Suppose that the [stock price](../../Financial%20Engineering/Derivatives/Part%20IV%20-%20Options/Chapter%2016%20-%20Black–Scholes%20Model.md) is$20,    the strike price is$20,  the price of a European call option is$5,  the [risk-free interest rate](../../Financial%20Markets/Financial%20Asset%20Pricing%20Theory%20Overview/Chapter%2012%20-%20Derivatives/Exercises.md) is 5%,  and you wanted to know the value of a European put option. Plugging those numbers into [1] gives us:

   $20 =$5 – P($20) + PV ($20)

   Present value,  PV,  for$20,    assuming a one-year horizon and given the 5% interest rate,    is$19.05. Now solving for P gives us the value of the put option—if no [arbitrage](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%207/Arbitrage%20Pricing%20of%20Derivatives.md) possibility exists—at$4.05.

   However,  what would happen if the parity did not hold? What if the put actually traded at$3.50 and not at$4.05? An [arbitrage](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%207/Arbitrage%20Pricing%20of%20Derivatives.md) opportunity would present itself,  since we know that the payoff of the put should be the same as the call minus the stock plus the present value of the zero-coupon bond. However,  despite that their payoff is the same,  the price is not. The put is underpriced relative to the combination of the other instruments with the identical net payoff.

   The most standard [arbitrage](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%207/Arbitrage%20Pricing%20of%20Derivatives.md) strategy is to buy the cheaper instrument and sell the more expensive. In this case,  this means buying the traded put at$3.50 and selling the "synthetic put,   " or the combination of the other instruments. (Using vocabulary from earlier,    you go long the put and short the synthetic put.) This trade results in an up-front payoff of$0.55. There are no further payoff implications,  since you are both short and long a put at the same time.

## UPPER AND LOWER BOUNDS FOR OPTION PRICES

   An important feature of option prices is that their value cannot exceed or go below a particular price,  given the option's characteristic. For instance,  the upper bound is the maximum possible price for a call option or a put option at any point in time. These upper and lower bounds of an option set price limits that are consistent with no [arbitrage opportunities](../../Financial%20Markets%20and%20Institutions/III.%20Liquidity%20of%20Assets/Class%208-%20Markets,%20Meltdowns,%20and%20Arbitrage/Class%20Note%2013%20The%20LTCM%20Meltdown.md). (If option prices go above the upper bound or below the lower bound,  investors have an [arbitrage](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%207/Arbitrage%20Pricing%20of%20Derivatives.md) opportunity.) As always,  calls and puts differ in their definition of upper bounds. To simplify our description,  we'll use European-style options based on a non-dividend-paying stock.

### CALL OPTION: UPPER AND LOWER BOUNDS FOR EUROPEAN CALLS ON NON-DIVIDEND-PAYING STOCK

   As we know,  a call option gives the holder the right to buy stock. It follows then that the option cannot in any circumstance be worth more than [stock price](../../Financial%20Engineering/Derivatives/Part%20IV%20-%20Options/Chapter%2016%20-%20Black–Scholes%20Model.md),  S. This becomes the upper bound of the European-style call option with no [dividend payments](../../Financial%20Markets/Financial%20Asset%20Pricing%20Theory%20Overview/Chapter%2012%20-%20Derivatives/Exercises.md),  C. Its value should be lower or equal to the [stock price](../../Financial%20Engineering/Derivatives/Part%20IV%20-%20Options/Chapter%2016%20-%20Black–Scholes%20Model.md),  expressed as: C ≤ S

   Conversely,  a lower bound for a European call is the [stock price](../../Financial%20Engineering/Derivatives/Part%20IV%20-%20Options/Chapter%2016%20-%20Black–Scholes%20Model.md) minus the present value of the [strike price](../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%205%20Options%20on%20Prices%20and%20Hedge-Based%20Valuation/Call%20and%20Put%20Payoffs%20at%20Expiry.md). It can be expressed as:

   S – PV(K)≤ C

   Combine these two bounds and you get the full range for the call option C: S – PV (K) ≤ C ≤ S

   To exemplify,  let's pick a situation when one of these bounds actually does not hold. Assume you have a stock at$20,    a strike price at$15,  and a [risk-free interest rate](../../Financial%20Markets/Financial%20Asset%20Pricing%20Theory%20Overview/Chapter%2012%20-%20Derivatives/Exercises.md) at 5%. The price of the call should therefore be greater than or equal to$5.71 (the result of the left-hand side of equation [5]).

   But suppose that the call was actually trading at$5.00—which violates this lower bound. The call is,  in other words,  underpriced,  and an [arbitrage](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%207/Arbitrage%20Pricing%20of%20Derivatives.md) opportunity presents itself,  where we want to sell (go short) the left-hand side of the equation and buy the call. How this [arbitrage trade](../../Financial%20Instruments/Assignments/Solutions/PSET%201%20Solution-Financial%20Instruments.md) plays out can be described in tabular form,  as done in the table below.

   Table B [Arbitrage Trade](../../Financial%20Instruments/Assignments/Solutions/PSET%201%20Solution-Financial%20Instruments.md) When Lower Bound Does Not Hold

   Reading column by column,  we first look at the value of our trade today. The net up-front gain is$0.71 (we buy a call option at$5.00,  short-sell the stock for$20.00,    and then buy a bond,    whose present value,    given a one-year time horizon,    is$14.29). This is still not an [arbitrage](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%207/Arbitrage%20Pricing%20of%20Derivatives.md)—this is what we make today,  but we do not know yet what might happen in the future.

   In fact,  there are two things that could happen in the future: the stock value could be above the [strike price](../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%205%20Options%20on%20Prices%20and%20Hedge-Based%20Valuation/Call%20and%20Put%20Payoffs%20at%20Expiry.md) of$15,    or it could be below. These two states are represented in the table by one column each. To start with,    if the stock price goes above$15,  then the call will be in the money and worth S

   ![image11.jpg](image11.jpg)

   1. Short-selling the stock results just in the (negative) stock value itself,  and the bond at maturity is worth$15. All in all,  we neither make nor lose money in this state.

   However,  if the [stock price](../../Financial%20Engineering/Derivatives/Part%20IV%20-%20Options/Chapter%2016%20-%20Black–Scholes%20Model.md) never reaches$15,    we do make money. The long call expires worthless,    the short stock position has a value of —S,    and the bond pays off$15. However,  since the [stock price](../../Financial%20Engineering/Derivatives/Part%20IV%20-%20Options/Chapter%2016%20-%20Black–Scholes%20Model.md) is below$15,    our payoff ends up being the difference between$15 and the [stock price](../../Financial%20Engineering/Derivatives/Part%20IV%20-%20Options/Chapter%2016%20-%20Black–Scholes%20Model.md). Put differently,  15 — S must be positive.

   So,  in the future,  we have no chance of losing money and,  in fact,  have a chance of making money. Since we make money today and have no possible future liability,  this is an [arbitrage](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%207/Arbitrage%20Pricing%20of%20Derivatives.md).

### PUT OPTIONS: UPPER AND LOWER BOUND FOR NON-DIVIDEND-PAYING EUROPEAN PUTS

   The upper bound for a European put option is established from the fact that a put gives its holder the right to sell a stock. Given this,  no matter how low the [stock price](../../Financial%20Engineering/Derivatives/Part%20IV%20-%20Options/Chapter%2016%20-%20Black–Scholes%20Model.md) becomes,  the put option,  P,  can never be worth more than the [strike price](../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%205%20Options%20on%20Prices%20and%20Hedge-Based%20Valuation/Call%20and%20Put%20Payoffs%20at%20Expiry.md),  K,  at maturity. Thus,  the upper bound is simply the option's [strike price](../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%205%20Options%20on%20Prices%20and%20Hedge-Based%20Valuation/Call%20and%20Put%20Payoffs%20at%20Expiry.md),  K,  discounted back to today using the [risk-free rate](../../Financial%20Instruments/Black%20Scholes%20Derivation.md). The value of a put will be lower than or at most equal to the present value of the option [strike price](../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%205%20Options%20on%20Prices%20and%20Hedge-Based%20Valuation/Call%20and%20Put%20Payoffs%20at%20Expiry.md),  which can be expressed as:

   P ≤PV(K) [61

   Conversely,  a lower bound for a European put is the [strike price](../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%205%20Options%20on%20Prices%20and%20Hedge-Based%20Valuation/Call%20and%20Put%20Payoffs%20at%20Expiry.md) (discounted using the [risk-free interest rate](../../Financial%20Markets/Financial%20Asset%20Pricing%20Theory%20Overview/Chapter%2012%20-%20Derivatives/Exercises.md),  r) minus the [stock price](../../Financial%20Engineering/Derivatives/Part%20IV%20-%20Options/Chapter%2016%20-%20Black–Scholes%20Model.md),  or:

   > PV(K) - S≤P
   >
   > Combine these two bounds and you get the full range for the put option P:

   PV(K) - S ≤ P ≤PV(K)

   Just as we did for the bounds for call options,  we can show that the bounds for put options also have to hold so that there are no [arbitrage opportunities](../../Financial%20Markets%20and%20Institutions/III.%20Liquidity%20of%20Assets/Class%208-%20Markets,%20Meltdowns,%20and%20Arbitrage/Class%20Note%2013%20The%20LTCM%20Meltdown.md).

### EFFECT OF DIVIDENDS ON PUT-CALL PARITY AND ON BOUNDS OF CALL AND PUT OPTIONS

   So far,  we have only established bounds for European options that pay no dividend. Let's see now what happens when the stock on which these European options are based do hand out dividends. Assume that the present value of dividends,  D,  during the lifetime of an option can be estimated with reasonable certainty. We then,  in the formulas above,  will have to substitute stock,  S,  whenever it appears,  with stock minus dividend,  S — D. For the [put-call parity formula](../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%205%20Options%20on%20Prices%20and%20Hedge-Based%20Valuation/Options%20and%20Forwards%20Risk%20Sharing%20and%20Put-Call.md) used above,  this translates into:

   $S - PV (D) = C(K) - P(K) + PV (K)$

   For the call option,  this means:

   $S - PV(D) - PV (K) < C S - PV(D)$

   |   |   |
   |---|---|
   |S - PV (D) = C(K) - P(K) + PV (K) For the call option,    this means:  <br>S - PV(D) - PV (K) < C S - PV(D)|[9]  <br>[10]|

   > And for the put option,  the bounds become:

   $PV(K) – S + PV(D) ≤ P ≤ PV(K)$

## PROBLEM SET

   We have now covered the basic properties of options. To conclude,  here are some [exercises](../../Financial%20Markets/Financial%20Asset%20Pricing%20Theory%20Overview/Chapter%2012%20-%20Derivatives/Exercises.md) to practice what you have just read. For the problems below refer to the following set of information. As of July 26,  the following European options,  which expire on August 20,  were written on XYZ Corporation. Their prices are shown in Table C.

### TABLE C

   |   |   |   |
   |---|---|---|
   |[Exercise Price](../../Financial%20Markets/Financial%20Asset%20Pricing%20Theory%20Overview/Chapter%2012%20-%20Derivatives/Options.md)|Calls|Puts|
   |$35  <br>$40  <br>$45|$4 1/8  <br>$1 5/16  <br>$3/8|$1 3/16  <br>Not traded  <br>Not traded|

   > Source: Casewriters.

   XYZ pays no cash dividends to its shareholders. A Treasury bill maturing on August 20 that pays$35 at maturity costs$34.94 on July 26.

   Problem 1 Could an American call option on a stock ever be worth less than a European call? How does an increase in [time to maturity](../../Financial%20Instruments/Lecture%20Notes-%20Financial%20Instruments/Teaching%20Note%201-%20Forward%20Rates%20Agreement/Hedging%20Strategies%20with%20Forwards.md) affect the value of European calls? American calls?

   Problem 2 Suppose the stock on a company is at$150,    and the company pays no dividends. Your friend has an American option on the stock with an exercise price of$100,  but it is still a few months to expiration. He has decided to lock in his profit and exercise the option. Can you think of a way of arbitraging this situation?

   Problem 3 Suppose that XYZ's [stock price](../../Financial%20Engineering/Derivatives/Part%20IV%20-%20Options/Chapter%2016%20-%20Black–Scholes%20Model.md) on July 26 was$50. On that date,    what is the very least a$35 call could be worth? The most? What trade would you do if the call was$15?

   Problem 4 What price would you expect the$45 put on XYZ above to trade at if the stock were at$37.50? If it traded above this price,  what [arbitrage](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%207/Arbitrage%20Pricing%20of%20Derivatives.md) opportunity would exist?

   Problem 5 Suppose a stock,  which pays no dividends,  sells for$10 today. Next period,    it will either move to$7 or$14. You do not know the probabilities of these two outcomes. Riskless zerocoupon bonds,    paying$1.10 in one period,  cost$1.00 today.

   1. What price would an at-the-money call sell for today?
   1. If you wished to synthetically manufacture the at-the-money call option,  how many bonds would you buy? How many shares of stock?
   1. If the call sold for$3.00,  how would you capture [arbitrage](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%207/Arbitrage%20Pricing%20of%20Derivatives.md) profits?
   1. Now,  consider what the stock might do in the second period. If it moves to$14 in the first period,    it can either move up to$18 or down to$11 in the second period. If it moves to$7 in the first period,  it can either move up to$11 or down to$4 in the second period. Assuming that riskless zero-coupon bonds,  paying$1.10 in the second period,    cost$1.00 at the end of the first period,  what price would an at-the-money call sell for today?

   ---

   1. Remember,  a "long call" means buying a call option,  and a "short put" means selling a put option.
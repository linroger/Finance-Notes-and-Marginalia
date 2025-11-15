---
cssclasses: academia
title: Payoffs to Plain Vanilla Options
tags:
- american
- american_options
- bond
- call
- derivatives_trading
- equity
- european
- european_options
- financial_derivatives
- forward
- future
- interest-rate
- option
- option_payoffs
- option_pricing
- plain_vanilla_options
- put
- stock
aliases:
- Options Payoffs
- Vanilla Options
- Option Trading Strategies
key_concepts:
- Bull and bear spreads
- Butterfly spreads
- Call and put options
- Covered calls and protective puts
- Derivative securities
- European and American options
- Financial risk management
- Option arbitrage bounds
- Option holder and writer
- Option trading properties
- Portfolio optimization
- Quantitative financial analysis
- Risk assessment and mitigation
- Strike price and maturity
- Time and intrinsic value
---

# Payoffs to Plain Vanilla Options

## 1. Options

These notes describe the payoffs to European and American put and call options—the so-called plain vanilla options. We consider the payoffs to these options for holders and writers and describe both the time value and intrinsic value of an option. We explain why options are traded and examine some of the properties of put and call option prices. We shall show that longer dated options typically have higher prices and that call prices are higher when the strike price is lower and that put prices are higher when the strike price is higher.

Keywords: Put, call, strike price, maturity date, in-the-money, time value intrinsic value, parity value, American option, European option, early exercise, bull spread, bear spread, butterfly spread.

### 1.1 Options Fundamentals

Options are derivative assets. That is their payoffs are derived from the payoff on some other underlying asset. The underlying asset may be an equity, an index, a bond or indeed any other type of asset. Options themselves are classified by their type, class and their series. The most important distinction of types is between put options and call options. A put option gives the owner the right to sell the underlying asset at specified dates at a specified price. A call option gives the owner the right to buy at specified dates at a specified price. Options are different from forward/futures contracts as a put (call) option gives the owner right to sell (buy) the underlying asset but not an obligation. The right to buy or sell need not be exercised. There is also a last date on which the right may be exercised and this is known as the expiration date or maturity date. The specified price is called the strike price or exercise price.

The most commonly traded option is the American type which may be exercised at any trading date prior to or at the expiration date. There are also options of the European type which may only be exercised at the expiration date. Thus an American put and a European put are different types of option. Another type is the Bermudan option which is half way between the European and American option as it can only be exercised on a limited number of pre-specified days prior to maturity. We shall focus mainly on European options as there is an important parity condition between the prices of European put and call options and we shall explain how the prices of American options differ from their European counterparts.

The owner or buyer of an option is often called the holder and the seller of an option is termed the writer. Thus at date of sale the holder pays the writer the price of the option. For a call option there may be a subsequent transaction at the expiration date where the writer provides the underlying asset to the holder in exchange for the agreed strike price. This subsequent transaction is made at the instigation of the holder and will only be undertaken if it is in the holder's interest. The holder's right to buy the stock at or prior to the expiration date need not be exercised. For a put option, the subsequent transaction is that the holder provides the underlying asset in return for the agreed strike price from the writer.

The difference between American and European options is simply what choices the holder has prior to the expiration date. The holder of the European option has, at any point prior to the expiration date, the choice either to sell the option for the prevailing market price or to retain it. The holder of an American option has, at any point prior to the expiration date, three choices: either to sell the option for the prevailing market price, to retain it or to exercise it. The later case is said to involve early exercise. This terminology is not meant to imply that there is anything sub-optimal about exercising before the expiration date. Indeed we will give below examples where the American option will be exercised early.

A class of option is all options of a particular type on the same underlying asset. Thus all American put options on IBM stock form one class. European call options on the FTSE 100 index form another class. A class will involve a variety of different strike prices and maturity dates. Most options are exchange traded and the exchange will specify a range of maturity dates, usually every two months, and a range of strike prices, usually centered around the prevailing market price. An option series is simply the options of a given class with the same strike price and maturity date.

### 1.2 Payoff at Maturity

Let $X$ be the exercise price and $S_{T}$ the price of the underlying stock at the maturity date. Then the payoff to a put option is
$$p_T=\left\{\begin{array}{ll}X-S_T&\text{if }S_T\leq X\\0&\text{if }S_T>X.\end{array}\right.$$

or more simply $p_{T}=\max[X-S_{T}, 0]$. If $S_{T}<X$, then the put is said to finish in-the-money and the option will be exercised. The holder of this option will buy the underlying stock at a price of $S_{T}$ and exercise their right to sell it to the writer at the strike price of $X$, to make a profit of $X-S_{T}$. If $S_{T}>X$, the option is said to finish out-of-the-money and exercising the right to sell the underlying asset would result in a loss. So the right to sell won't be exercised. The payoff will be zero in this case. Hence with an option the payoff is never negative. Assets with non-negative payoffs are know as limited liability assets.

Suppose that you hold a put option on a stock $PDQ$. The exercise price is 1000 and the expiration date is in four weeks. The current stock price of $PDQ$ is 1109. If the stock is still at 1109 in four weeks time, you we let the option expire without exercising your right to sell at 1000. If you exercised your right to sell you would have to deliver the stock, which would cost you 1109, and you would receive only 1000 in return. Clearly exercising the option to sell would result in a loss. You will not exercise and your payoff is $\max[X-S_{T}, 0]=\max[1000-1109, 0]=0$. However, if $PDQ$ does badly and the stock price falls to 900 after four weeks, you as holder of the put option will do well. In that case you can exercise your right to sell, buying the stock at the reduced price of 900 and selling it to the holder at 1000. The payoff at maturity is $\max[X-S_{T}, 0]=\max[1000-900, 0]=100$ per unit.

Equally the payoff to the holder of a call option is
$$c_T=\left\{\begin{array}{ll}0&\text{if }S_T\leq X\\S_T-X&\text{if }S_T>X.\end{array}\right.$$

or more simply $c_{T}=\max[0, S_{T}-X]$. In this case the call finishes in the money if $S_{T}>X$ as the option holder can exercise the right to buy the underlying asset at a price of $X$ when it is worth the greater amount $S_{T}$. If $S_{T}\leq X$, the call option finishes out of the money and the right to buy will go unexercised.

The writer of the call option has exactly the reverse of the payoff to the holder. The writer of the call has a payoff of $-c_{T} = -\max[0, S_{T}-X] = \min[0, X-S_{T}]$. When the option is exercised the writer will have to deliver a stock worth $S_{T}$ and receives a payment of $X$ from the holder. Since $S_{T}>X$ the writer makes a loss of $X-S_{T}$. Likewise the payoff at maturity to the writer of a put option is $-p_{T}=-\max[X-S_{T}, 0]=\min[S_{T}-X, 0]$.

The intrinsic value or parity value of an option at time $t$ is the payoff to the option if the current date were the maturity date. Thus the intrinsic value of the call option at time $t$ is $\max[0, S_{t}-X]$ where $S_{t}$ is the current price of the underlying asset and the intrinsic value of a put option is $\max[X-S_{t}, 0]$.

An American option will always trade at a price at or above its intrinsic value, since with an American option it is always possible to exercise the option now and realise the intrinsic value. The difference between the price of an option an its intrinsic value is known as the premium or time value of the option. Thus the price of an option is the sum of its intrinsic value plus its premium:
$$\text{price of option}=\text{intrinsic value}+\text{time value}.$$

If an option is initially set up at date 0 when the stock price is $S_{0}$ and with the strike price set such that $X=S_{0}$ then the intrinsic value of the option is 0 and the premium and price are equivalent. Many options were historically set up with the strike price equal to the prevailing price of the underlying asset (or at-the-money as it is called) and this accounts for why the option price is sometimes referred to as the option premium. We will use the term time value rather than premium to avoid confusion.

### 1.3 Why Trade Options?

It is easy to see why it might be desirable to trade options. Suppose you buy a call option with an exercise price equal to the current stock price. If the stock goes up in value, you can still buy at the low current price and sell at the new higher price. And if you are unlucky and the price falls, then you simply don't exercise the option. All you lose is the price you paid for the option in the first place. You only buy the stock when the price has gone up. You get all the upside benefits and eliminate the downside risk. You don't have to risk buying the stock in that hope that the price will rise. You simply buy the option which costs a fraction of the price of the stock itself.

Because you only pay for the stock at maturity, buying a call option is equivalent to borrowing most of the money to buy the stock and repaying only if the bet goes well. Thus a call option is a highly levered or geared position in the stock and thus with a return that is higher but also highly risky.

To see this consider the following simple example. The current price of the stock is 100 and a call option on the stock with a strike price of 100 costs 30. Suppose that the stock price at maturity has risen to 175. The rate of return on the stock is a handsome $75\%$. However the return on the call option is greater still. If the stock price rises to 175 the call option can be exercised to make a profit of 175-10=75. Since the call costs 30 the rate of return is $\frac{75}{30}-1=1.5$ or $150\%$. The high leverage makes possible a high rate of return on the relatively small investment. On the other hand suppose the stock finishes out of the money at 75. Owning the stock results in a rate of return of $-25\%$. The call option however, expires valueless, so the rate of return on the investment in the call option is $-100\%$. Not such a good prospect.

Suppose these are the only two possible values for the stock at maturity and suppose that $\pi$ is the probability the stock price rises and $(1-\pi)$ is the probability it falls. Suppose that the interest rate over the period is $25\%$. The risk premium on the stock is
$$rp_S=75\pi+(-25)(1-\pi)-25=100\pi-50$$

And the risk premium on the call option is
$$rp_C=150\pi+(-100)(1-\pi)-25=250\pi-100.$$

It is clear that the risk premium on the call is 2.5 times the risk premium for the stock irrespective of the value of $\pi$. This ratio is known as the option elasticity and it can be shown that for a call option it is always greater than one. Thus the call option is always riskier than the underlying stock. The high risk means that options are good and cheap ways to hedge risk as we shall see later on.

<table>
    <tbody>
        <tr>
            <th> </th>
            <th> </th>
            <th> </th>
            <th>Calls</th>
            <th> </th>
            <th> </th>
            <th>Puts</th>
            <th> </th>
        </tr>
        <tr>
            <th>Option</th>
            <th> </th>
            <th>May</th>
            <th>Calls Aug</th>
            <th>Nov</th>
            <th>May</th>
            <th>Puts Aug</th>
            <th>Nov</th>
        </tr>
        <tr>
            <th>Option</th>
            <th> </th>
            <th>May</th>
            <th>Aug</th>
            <th>Nov</th>
            <th>May</th>
            <th>Aug</th>
            <th>Nov</th>
        </tr>
        <tr>
            <td>Tesco</td>
            <td>160</td>
            <td>1 22</td>
            <td>27</td>
            <td>31</td>
            <td>7</td>
            <td>10 1/2</td>
            <td>14 1/2</td>
        </tr>
        <tr>
            <td>(*176)</td>
            <td>180</td>
            <td>111</td>
            <td>17</td>
            <td>23</td>
            <td>16</td>
            <td>19</td>
            <td>25</td>
        </tr>
        <tr>
            <td>Rolls Royce</td>
            <td>180</td>
            <td>22</td>
            <td>27</td>
            <td>30 1/2</td>
            <td>8</td>
            <td>12 1/2</td>
            <td>16</td>
        </tr>
        <tr>
            <td>(*194 1/2)</td>
            <td>200</td>
            <td>11</td>
            <td>17 1/2</td>
            <td>21 1/2</td>
            <td>18</td>
            <td>23</td>
            <td>26 1/2</td>
        </tr>
    </tbody>
</table>

Table 1: Call and Put Prices

## 2. Properties of Puts and Calls

Table 1 gives the prices of options on two stocks, Tesco and Rolls Royce given in the Financial Times on Tuesday March 6th 2000. The starred number in the left column gives the closing stock price on the previous day and the paper reports the prices for puts and calls of three maturities, May, August and November, for strike prices on either side of the closing price.

Three things are immediately obvious from this table. First the option prices increase with the maturity date for any given strike price. Second the price of calls falls with the strike price for any given maturity date and third the price of puts rises with the strike price with any given maturity date.

For a given strike price, the table shows that the price of calls increases with the date to maturity. That is $C_{t}(T_{2})\geq C_{t}(T_{1})$ for $T_{2}>T_{1}$ where $C_{t}(T_{1})$ is the price of an American call option at date $t$ that matures at date $T_{1}$ and $C_{t}(T_{2})$ is the an option of the same type and class and with the same strike price but with a longer maturity. From the table we can see that August calls on Tesco stock with a strike price of 160 trade at 27 but the longer maturity November calls trade at 31. There would be a simple arbitrage opportunity if $C_{t}(T_{1})>C_{t}(T_{2})$ for $T_{2}>T_{1}$. Suppose that the prices were reversed and the November call on Tesco trades at 27 and the August call trades at 31. Then buying the lower priced November call and writing the August call yields a net infow of 4 today. Either the August call expires or is exercised prior to maturity. In either case its value is $\max[0, S_{t^{\prime}}-X]$ where $t^{\prime}$ is the maturity date in August or some time prior to the maturity date when the call is exercised. The value of the position is $C_{t^{\prime}}(Nov)-\max[0, S_{t^{\prime}}-X]$. If this is positive then sell the November call at date $t^{\prime}$ to make a profit. Otherwise exercise the November call. Exercising the call yields the same value of $\max[0, S_{t^{\prime}}-X]$ no matter what the maturity date. So there is a completely offsetting gain from the bought November call and the written August call. In either case an arbitrage profit has been made. Note that this does not say anything about how the call value changes over time until maturity. It only compares prices at a particular date of options with different expiration dates. Neither does the argument work for European options which cannot be exercised early. However as a empirical matter European options do demonstrate the same pattern of prices rising with date to maturity.

Equally clear is that a call with a lower strike price must command a higher price. Thus $C_{t}(X_{1})\geq C_{t}(X_{2})$ if $X_{2}>X_{1}$. This can be seen from Table 1. For example, May calls on Rolls-Royce with a strike price of 200 are worth 11 but the May calls with the lower strike price of 180 are worth 22. This is simply because the call gives the holder the option to buy and the lower the exercise price at which the stock can be bought the more valuable is the option. If this were not true and $C_{t}(X_{1}) < C_{t}(X_{2})$ for $X_{2}>X_{1}$ then there is an arbitrage opportunity and the appropriate response is a bull spread. The payoffs can be seen in Table 2. This strategy buys the call with the lower strike price of $X_{1}$ and writes the call with the higher strike price of $X_{2}$ leading to cash inflow now of $C_{t}(X_{2})-C_{t}(X_{1})>0$. In each case the payoff at maturity is non-negative. Thus for European options $c_{t}(X_{1})\geq c_{t}(X_{2})$ for $X_{2}>X_{1}$. Equally suppose the options are of the American type, then if the written option is exercised early, the holder of that option will pay us $X_{2}$ for the stock. If we exercise the bought option immediately, the stock can be bought for $X_{1}$ and then sold for $X_{2}$ leading to a profit of $X_{2}-X_{1}$. Hence we have for American options $C_{t}(X_{1})\geq C_{t}(X_{2})$ for $X_{2}>X_{1}$.

<table>
    <tbody>
        <tr>
            <th>Position</th>
            <th>$S_{T}<X_{1}<X_{2}$</th>
            <th>$X_{1}<S_{T}<X_{2}$</th>
            <th>$X_{1}<X_{2}<S_{T}$</th>
        </tr>
        <tr>
            <td>Long Call</td>
            <td>0</td>
            <td>$S_{T}-X_{1}$</td>
            <td>$S_{T}-X_{1}$</td>
        </tr>
        <tr>
            <td>Short Call</td>
            <td>0</td>
            <td>0</td>
            <td>$X_2-S_T$</td>
        </tr>
        <tr>
            <td>Overall</td>
            <td>0</td>
            <td>$S_{T}-X_{1}>0$</td>
            <td>$X_{2}-X_{1}>0$</td>
        </tr>
    </tbody>
</table>

Table 2: Bull Spread

Another property that we can see from the table is that the differences in the call or put option prices for a given stock and maturity date is less than the difference between the strike prices. For example the difference in the option prices for November calls on Tesco stock is 31-23=8 which is less than the difference in strike prices, which is 180-160=20. Thus for call options we have $C_{t}(X_{1})-C_{t}(X_{2})\leq X_{2}-X_{1}$ for $X_{2}>X_{1}$. Indeed if this were not the case and $C_{t}(X_{1})-C_{t}(X_{2})>X_{2}-X_{1}$ there would again be an arbitrage opportunity. The strategy to exploit the arbitrage opportunity would be a bear spread where the the option with the higher strike price is purchased and the lower strike price option sold, together saving the difference in the strike prices, that is buying $(X_{2}-X_{1})$ risk free bonds with maturity at date $T$ and an interest rate of $r$ between the current date $t$ and the maturity date. The payoffs from this strategy are given in Table 3 and the payoff is always positive at maturity and so the value of the portfolio $V_{t}$ must itself be positive. Thus for European options $V_{t}=c_{t}(X_{2})-c_{t}(X_{1})+(X_{2}-X_{1})>0$. If the options are American the value of the portfolio is $V_{t} = C_{t}(X_{2}) - C_{t}(X_{1})+(X_{2}-X_{1})>0$ but we need to decide what to do if the written call is exercised prior to maturity. Suppose it is exercised at time $t^{\prime}$ when the stock price is $S_{t^{\prime}}$. To meet our obligations on the written call we must buy the stock at $S_{t^{\prime}}$ and sell it at $X_{1}$. The purchased call is worth $C_{t^{\prime}}(X_{2})$ at time $t^{\prime}$. If $C_{t^{\prime}}(X_{2})>S_{t^{\prime}}-X_{2}$, then we simply sell our call to cover our obligation and make a net profit and in addition have our risk-free bonds. If $C_{t^{\prime}}(X_{2})<S_{t^{\prime}}-X_{2}$, then we exercise the call, buying the stock at $X_{2}$ and selling it at $X_{1}<X_{2}$. The loss on this transaction is covered by closing out our bond position, so we retain the accumulated interest $r^{\prime}(X_{2}-X_{1})$ where $r^{\prime}$ is the interest rate from $t$ to $t^\prime$.

<table>
    <tbody>
        <tr>
            <th>Position</th>
            <th>Value</th>
            <th>$S_{T}<X_{1}<X_{2}$</th>
            <th>$X_{1}<S_{T}<X_{2}$</th>
            <th>$X_{1}<X_{2}<S_{T}$</th>
        </tr>
        <tr>
            <td>Long Call</td>
            <td>$C_t (X_2)$</td>
            <td>0</td>
            <td>0</td>
            <td>$S_{T}-X_{2}$</td>
        </tr>
        <tr>
            <td>Short Call</td>
            <td>$-C_{t}(X_{1})$</td>
            <td>0</td>
            <td>$X_{1}-S_{T}$</td>
            <td>$X_{1}-S_{T}$</td>
        </tr>
        <tr>
            <td>Buy Bonds</td>
            <td>$(X_{2}-X_{1})$</td>
            <td>$(X_{2}-X_{1})(1+r)$</td>
            <td>$(X_{2}-X_{1})(1+r)$</td>
            <td>$(X_{2}-X_{1})(1+r)$</td>
        </tr>
        <tr>
            <td>Overall</td>
            <td>$V_{t}$</td>
            <td>$(X_{2}-X_{1})(1+r)$</td>
            <td>$(X_{2}-S_{T})+r(X_{2}-X_{1})>0$</td>
            <td>$r(X_{2}-X_{1})>0$</td>
        </tr>
    </tbody>
</table>

Table 3: Bear Spread plus Savings

One property not apparent from the table is the relationship between options with more than two strike prices. Suppose that May puts on Rolls-Royce with a strike price of 190 are traded. It is to be expected that they trade at a price somewhere between the 8 and 18. Suppose that all the puts are European, then it is simple to show that the May European put with a strike of 190 cannot trade at a price above 13 which is the mid-way point between 8 and 18. To establish this claim consider another popular trading strategy the butterfly spread. This spread consists of a portfolio of buying one put with a strike price of 180, buying another put with a strike price of 200 and selling two puts with a strike price of 190. The payoffs at maturity to this strategy are given in Table 4. In each case the payoffs at maturity are positive so we can be assured that the value of the portfolio is non-negative. Hence $26-2p_{t}(190)\geq 0$ or $p_{t}(190)\leq 13$. This argument again applies to American as well as European options. If the written puts are exercised early, then either exercise both puts immediately to cash-out the position or one or both of the puts can be sold if this yields a higher profit.

Using butterfly spreads in this way establishes that for puts with strike prices $X_{1}$ and $X_{3}$, the price of the put with the mid-way strike price of $\frac{1}{2}X_{1}+\frac{1}{2}X_{3}$ satisfies
$$P_{t}(\frac12X_{1}+\frac12X_{3})\leq\frac12P_{t}(X_{1})+\frac12P_{t}(X_{3}).$$

<table>
    <tbody>
        <tr>
            <th>Position</th>
            <th>Value</th>
            <th>$S_T < 180$</th>
            <th>$180<S_{T}<190$</th>
            <th>$190<S_T<200$</th>
            <th>$S_{T} > 200$</th>
        </tr>
        <tr>
            <td>1st Long Put</td>
            <td>8</td>
            <td>$180-S_T$</td>
            <td>0</td>
            <td>0</td>
            <td>0</td>
        </tr>
        <tr>
            <td>Short Puts</td>
            <td>$-2p_{t}(190)$</td>
            <td>$2(S_T-190)$</td>
            <td>$2(S_{T}-190)$</td>
            <td>0</td>
            <td>0</td>
        </tr>
        <tr>
            <td>2nd Long Put</td>
            <td>18</td>
            <td>$200-S_{T}$</td>
            <td>$200-S_{T}$</td>
            <td>$200-S_{T}$</td>
            <td>0</td>
        </tr>
        <tr>
            <td>Overall</td>
            <td>$26-2p_{t}(190)$</td>
            <td>0</td>
            <td>$S_{T}-180$</td>
            <td>$200-S_{T}$</td>
            <td>0</td>
        </tr>
    </tbody>
</table>

Table 4: Butterfly Spread with Puts

A slightly more general interpretation would be to buy a fraction $\lambda$ units of the put with strike price of $X_{1}$ and buy a fraction $(1-\lambda)$ units of the put with strike price $X_{3}>X_{1}$ and write one put with a strike price of $X_{2}=\lambda X_{1}+(1-\lambda)X_{3}$. With this portfolio it can be found that
$$P_{t}(\lambda X_{1}+(1-\lambda)X_{2})\leq\lambda P_{t}(X_{1})+(1-\lambda)P_{t}(X_{2}).$$

It therefore follows from arbitrage principles that the put price is a convex function of the strike price. Equally constructing a butterfly spread for calls also shows that the call price is a convex function of the strike price.

## 3. Summary

We have seen how the payoffs to put and call options depend on the underlying assets and how the prices of puts and calls depend on the length of time to maturity and strike price. We shall explore other properties of option prices and ultimately derive an expression for how option prices depend on the strike price, time to maturity, interest rate, volatility and current price of the underlying asset. Indeed we shall see how any derivative asset can be priced.

## 4. Option Trading Strategies

These notes consider the way put and call options and the underlying can be combined to create hedges, spreads and combinations. We will consider the parity condition that applies for put and call option and consider arbitrage bounds that apply to the prices of puts and calls.

Keywords: American option, European option, early exercise, put-call parity, hedge, spread, combination, bull spread, bear spread, strap, arbitrage bounds, covered call, protective put.

### 4.1 Option Trading Strategies

There are basically three varieties of trading strategies. A hedge combines an option with an underlying stock to protect either the option or the stock against loss. A spread combines options of the same class but different series, where some are bought and others written. A combination combines options of different types, both bought or both written, on the same underlying stock.

#### A hedge

Suppose that you write a call option. The payoff to a call option at maturity is $\max[0, S_{T}-X]$ where $X$ is the strike price and $S_{T}$ is the price of the underlying at maturity. Your payoff at maturity having written the call is therefore $\min[0, X-S_{T}]$. If the price of the underlying rises above the strike price you will make a loss. Moreover, these losses are potentially unlimited.

If the price rises far above the strike price you are in a very exposed position. You may want to hedge or cover this risk. The obvious way to do so is to buy the stock which you will be obliged to deliver if the call is exercised. Taking a long position in the stock to hedge a written call is known as writing a covered call.

The payoff at maturity to writing a covered call is $\min[S_{T}, X]$. This is far less risky than the naked short position in the call itself as now the worst that can happen is that you sell the underlying at a price below its market value. Of course the hedged position is costly, it costs $S_{t}-c_{t}$, whereas the naked position has a positive initial inflow of cash of $c_t$ the price of the call option.

Likewise if you buy a put option there will loss if the price of the underlying rises equal to the cost of the put option $p_{t}$. The payoff at maturity will be $\max[0, X-S_{T}]$. However, you will have to buy the stock if you wish to exercise the right to sell at the strike price $X$. Thus you may wish to buy the stock in advance at the cost of $S_{t}$. In this case the payoff at maturity is $\max[S_{T}, X]$ and the initial cost is $S_{t}+p_{t}$. Going long in the put and the stock is known as a protective put strategy.

#### A spread

There are many examples of spreads. Vertical spreads use options of the same maturity but different strike prices; horizontal spreads use options with the same strike prices but different maturities and diagonal spreads use option with both different strike prices and maturities.

One popular type of vertical spread is the bull spread which is a position taken by an investor who thinks that the price of the underlying will rise.

<table>
    <tbody>
        <tr>
            <th>Position</th>
            <th>$S_{T}<X_{1}<X_{2}$</th>
            <th>$X_{1}<S_{T}<X_{2}$</th>
            <th>$X_{1}<X_{2}<S_{T}$</th>
        </tr>
        <tr>
            <td>Long Call</td>
            <td>0</td>
            <td>$S_{T}-X_{1}$</td>
            <td>$S_{T}-X_{1}$</td>
        </tr>
        <tr>
            <td>Short Call</td>
            <td>0</td>
            <td>0</td>
            <td>$X_2-S_T$</td>
        </tr>
        <tr>
            <td>Overall</td>
            <td>0</td>
            <td>$S_{T}-X_{1}>0$</td>
            <td>$X_{2}-X_{1}>0$</td>
        </tr>
    </tbody>
</table>

Table 1: Bull Spread

A bull spread can be created by buying a call with a low strike price and writing a call with a higher strike price. Suppose that the written call has a strike price of $X_{2}$ and the long call has a strike price of $X_{1}<X_{2}$. The payoffs at maturity are given in the Table 1. The value of the spread is $c^{1}-c^{2}$ where $c^{1}$ is the price of the call option with a strike price of $X_{1}$ and $c^{2}$ is the price of the call option with a strike price of $X_{2}$. Since the bull spread always yields a non-negative payoff at maturity (it is a limited liability asset) it follows that $c^{1}>c^{2}$.

Another type of spread is a bear spread. A bear spread can be created by holding a put with a higher strike price and writing a put with a lower strike price. In this case the investor benefits if the markets is falling. This is in contrast to a bull spread where the investor gains when the market rises.

Exercise: An investor buys a March put on Reed Elsevier with a strike price of 649 for a price of 55.5 and writes a March put on Reed Elsevier with a strike price of 609 for a price of 34. Calculate the payoff now and the possible payoffs in March when the puts expire. Draw a table and a diagram to illustrate the payoffs.

#### A combination

A combination involves taking a position in both puts and calls on the same underlying asset. One particular combination is a strap. A strap consists of a long position in two calls and one put with the same strike price and expiration date. This position will benefit if the price of the underlying moves sharply in either direction but especially if it rises.

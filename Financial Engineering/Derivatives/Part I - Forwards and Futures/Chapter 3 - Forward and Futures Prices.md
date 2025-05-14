---
tags:
  - arbitrage
  - cash_and_carry
  - forward_contracts
  - futures_prices
  - risk_free_rate
aliases:
  - Forward Pricing
  - Futures Pricing
  - No-Arbitrage Pricing
key_concepts:
  - Cash-and-carry arbitrage
  - Fair forward price
  - Forward contract replication
  - Implied repo rate
  - Income stream impact
---
# Forward and Futures Prices  

# Aims  

• To construct a synthetic or [[Chapter 22 - BOPM: Implementation|replication portfolio]] whose cash fows mimic the cash fows in an actual [[Forward Points in Currency|forward contract]].   
• To show how [[Dollar Rolls|cash-and-carry arbitrage]] can be used to determine the correct (no-[[Arbitrage Pricing of Derivatives|arbitrage]]) ‘fair’ price for a [[Forward Points in Currency|forward contract]] on a (non-dividend paying) stock.   
• To interpret [[Dollar Rolls|cash-and-carry arbitrage]] in terms of the [[The Futures Bond Basis: government bond futures and basis  trading|implied repo rate]] and the actual repo rate.   
• To extend our [[Arbitrage Pricing of Derivatives|arbitrage]] approach to determine the [[Chapter 3 - Forward and Futures Prices|fair forward price]] when the [[Risk Neutral Pricing of Options|underlying asset]] pays an income stream (e.g. dividends on a stock) or has [[Primary vs. Secondary Commodities|storage costs]] (e.g. oil, wheat) or can be used as an input to the production process (e.g. the convenience yield of owning oil).   
• To distinguish between the price of a [[Forward Points in Currency|forward contract]] at inception and the value of a [[Forward Points in Currency|forward contract]] that has been in existence for some time.  

# 3.1 PRICING FORWARD CONTRACTS  

In this section we analyse how forward and future prices are determined as functions of known variables such as the current market price of the [[Risk Neutral Pricing of Options|underlying asset]] and the [[Exercises|risk-free interest rate]]. Forward contracts are easier to analyse than [[Mathematics of the Financial Markets|futures contracts]], since the latter have the added complication of [[Pricing and Hedging Implications of Daily Sett|daily settlement]] (i.e. marking-to-market) whereas for the [[Forward Points in Currency|forward contract]] there is one payment at the maturity date. However, it can be shown that the [[Futures Price and the Quality Option Before E|futures price]] closely follows that of the [[Forward Contracts and Forward Prices|forward price]] (for contracts with the same maturity date). Therefore, for the most part the reader can consider the analysis of ‘forward’ and ‘[[Futures Not Subject to Cash-And-Carry|futures]]’ prices as being interchangeable. In general we assume:  

zero transactions costs   
• zero tax rates   
• agents can borrow or lend unlimited amounts at the [[Black Scholes Derivation|risk-free rate]] of interest   
• short-selling of the [[Risk Neutral Pricing of Options|underlying asset]] is possible   
• risk-free [[Class Note 13 The LTCM Meltdown|arbitrage opportunities]] are instantaneously eliminated.  

For the most part we use (risk-free) [[Arbitrage Pricing of Derivatives|arbitrage]] to price [[Mathematics of the Financial Markets|futures contracts]] and this method is also referred to as the cost of carry method.  

# 3.1.1 Non-income Paying Security  

Consider the [[Futures Price and the Quality Option Before E|futures price]] on a stock (which pays no dividends). The [[Futures Not Subject to Cash-And-Carry|futures]] contract is for the delivery of a single stock in 3 months’ time (Figure 3.1). We set up a situation where initially it is possible to make a risk-free [[Arbitrage Pricing of Derivatives|arbitrage]] proft because the quoted [[Futures Price and the Quality Option Before E|futures price]] is incorrect. Consider the following ‘prices’:  
$F_{q}=\$102$ is the quoted futures price in Chicago 25 June $\mathit{\check{t}}=0\mathit{\check{\Psi}}$ with maturity date of 25 September $T=1/4$ is the time to maturity of futures contract in years or fraction of year $S=\$100$ is the spot cash market price of the stock the NYSE 25 June $r=0.04$ is the [[Exercises|risk-free interest rate]] $(=4\%$ [[Interest Rate Quotations|simple interest]]  

FIGURE 3.1 Risk-free [[Arbitrage Pricing of Derivatives|arbitrage]]   


<html><body><table><tr><td>[[Chapter 16 - Black–Scholes Model|Stock price]]</td><td>S = $100</td></tr><tr><td>Risk-free rate</td><td>r = 4% p.a.</td></tr><tr><td>Quoted future price</td><td>F= $102</td></tr><tr><td>Strategy today (25 June)</td><td>Sell (short) [[Futures Not Subject to Cash-And-Carry|futures]] contract at $1o2 (receive no cash today)</td></tr><tr><td></td><td>Borrow $1oo from bank and buy the stock (= synthetic</td></tr><tr><td>future)</td><td></td></tr><tr><td>Use no ‘own funds'</td><td></td></tr><tr><td></td><td>3 months' time : 25 September (T = 1/4)</td></tr><tr><td></td><td>Bank loan outstanding = $100(1 + 0.04/4) = $101</td></tr><tr><td></td><td>Deliver stock,receipt from [[Futures Not Subject to Cash-And-Carry|futures]] contract = $102</td></tr><tr><td>Riskless profit</td><td>= $1</td></tr></table></body></html>  

# 3.1.2 Overpriced Futures Contract  

Below, we see that the correct (‘no-[[Arbitrage Pricing of Derivatives|arbitrage]]’ or ‘fair’) [[Futures Price and the Quality Option Before E|futures price]] is $F=\$101$ , which with a quoted price $F_{q}=\$102$ implies the [[Futures Not Subject to Cash-And-Carry|futures]] contract is overpriced and it is possible to earn a risk-free ([[Arbitrage Pricing of Derivatives|arbitrage]]) proft. Here’s how. The arbitrageur Ms Arb on 25 June (at 11 a.m.) borrows $\$100$ from bank-A and purchases stock-ABC on the NYSE. She therefore knows for certain that she can deliver the stock in 3 months on 25 September (since it is ‘in her pocket’ and will stay there – she ‘carries’ the stock). This strategy involves no ‘own capital’ by Ms Arb, since the money is borrowed.  

Ms Arb on 25 June (at 11 a.m.) also sells a [[Futures Not Subject to Cash-And-Carry|futures]] contract (on stock-ABC) in Chicago at $F_{q}=\$102$ (to another trader in Chicago, who may be a hedger or a speculator – we don’t care – we only care about our own trades). Note that Ms Arb’s ‘sell order’ is noted by the futures clearing house in Chicago and Ms Arb does not pay any money today (we ignore margin payments). By selling the September-futures contract on 25 June and holding it to maturity, Ms Arb is legally obliged to deliver one stock on 25 September in Chicago, when she will receive today’s quoted futures price, $F_{q}=\$102$ .  

What is the cost between 25 June and 25 September to Ms Arb of ‘carrying’ and then ‘delivering’ stock-ABC in Chicago to fulfl the conditions of her short [[Futures Not Subject to Cash-And-Carry|futures]] position? On 25 September, Ms Arb owes the bank the initial loan of $\$100$ plus interest, which equals $\$101$ $[=\S100(1+0.04/4)=S(1+r T)]$ . By purchasing stock-ABC in the cash-market in June with borrowed money, Ms Arb can (with certainty) deliver it in 3 months’ time in Chicago on 25 September – she has created a ‘synthetic’ or ‘[[Forward and Futures Contracts|replication]]’ [[Futures Not Subject to Cash-And-Carry|futures]] contract at a cost of $S(1+r T)=\$101$ (which accrues on 25 September).  

At maturity of Ms Arb’s (short) [[Futures Not Subject to Cash-And-Carry|futures]] contract on 25 September, she delivers one stock and receives $F_{q}=\$102$ in Chicago. The cost of having the stock ‘in her pocket’ ready for delivery in September is $\$101$ – therefore Ms Arb makes a proft of $(102-101)=\S1$ on 25 September. This strategy is risk-free since Ms Arb knows for certain what the outcome will be on 25 September, when she makes her trades on 25 June. The reason there is a ‘[[Carry Trade|cash-and-carry]]’ [[Arbitrage Pricing of Derivatives|arbitrage]] opportunity is because the quoted [[Futures Price and the Quality Option Before E|futures price]] $F_{q}$ is greater than the correct (‘fair’) price of the [[Futures Not Subject to Cash-And-Carry|futures]] contract $F=S(1+r T)$ that is:  
$$
F_{q}>F=S(1+r T)
$$  

Many arbitrageurs will take advantage of this risk-free proft opportunity by ‘buying low’ and ‘selling high’. Buying stock-ABC in the cash market (NYSE) and borrowing money on 25 June tends to increase $s$ and $r$ , while selling [[Mathematics of the Financial Markets|futures contracts]] in Chicago on 25 June will tend to depress the quoted [[Futures Price and the Quality Option Before E|futures price]] $F_{q}$ – this is just supply and demand and will tend to quickly move the quoted [[Futures Price and the Quality Option Before E|futures price]] to equal the fair [[Futures Price and the Quality Option Before E|futures price]]: $F_{q}=F=S(1+r T)$ . So the ‘correct’, ‘no [[Arbitrage Pricing of Derivatives|arbitrage]]’ or ‘fair’ [[Futures Price and the Quality Option Before E|futures price]] is:  
$$
F=S(1+r T)
$$  

If the quoted [[Futures Price and the Quality Option Before E|futures price]] on 25 June had been $F=\$101$ , then there would be no risk-free arbitrage opportunities available. Above, we have implicitly assumed that all futures traders are quoting a price $F_{q}=\$102$ which makes the [[Dollar Rolls|cash-and-carry arbitrage]] possible for all traders like Ms Arb. However, there is another way all traders will quickly move their quoted [[Futures Not Subject to Cash-And-Carry|futures]] prices to equal the [[Part II-Basis Trading and the Implied Repo Rate|no-arbitrage futures price]], $F=S(1+r T)$ .  

If trader-A is quoting $F_{A}=\$102$ and another trader-B is quoting the no-arbitrage price $F_{B}=\$101$ (for the September contract) then Ms Arb on 25 June will buy a September-[[Futures Not Subject to Cash-And-Carry|futures]] from trader-B and sell a September-[[Futures Not Subject to Cash-And-Carry|futures]] to trader-A. She has a long-short position in September-[[Futures Not Subject to Cash-And-Carry|futures]]. On 25 September, at maturity, she takes delivery from trader-B and pays $F_{B}=\$101$ and immediately delivers the stock in Chicago to futures trader-A and receives $F_{A}=\$102$ – making a risk-free [[Arbitrage Pricing of Derivatives|arbitrage]] proft of $\$1$ . It is the fact that the futures contracts mandate delivery on 25 September that makes this long-short position risk-free. In practice, when lots of Ms Arbs sell futures contracts at $F_{A}=\$102$ , supply and demand ensures that the [[Futures Price and the Quality Option Before E|futures price]] on 25 June will quickly fall to its no-[[Arbitrage Pricing of Derivatives|arbitrage]] correct value of $F=S(1+r T)=\mathbb{\S}101\$ .  

We can write Equation (3.2) as:  

“Fair” [[Futures Price and the Quality Option Before E|Futures Price]] $\c=$ Spot Price $^+$ Dollar Cost of Carry \$100 \$1  
$$
F=S+D C C
$$  

where the dollar cost of carry $D C C=S r T=\S1.$ . Equivalently we have:  

“Fair” [[Futures Price and the Quality Option Before E|Futures Price]] $\c=$ Spot Price $^{1+}$ Percent Cost of Carry  
$$
F=S(1+P C C)
$$  

where the percent (proportionate) cost of carry $\begin{array}{r}{P C C=r.T=1\%}\end{array}$ . Determining the [[Futures Price and the Quality Option Before E|futures price]] using Equation (3.2) involves [[Dollar Rolls|cash-and-carry arbitrage]].  

The spot price of the stock on the NYSE will change continuously but the actions of arbitrageurs means that $F=S(1+r T)$ at all times. It is immediately apparent from Equation (3.2) that the [[Futures Price and the Quality Option Before E|futures price]] and the [[Chapter 16 - Black–Scholes Model|stock price]] will move closely together (if $r$ stays constant). In our case $F=(1.01)S$ and hence over a short time horizon, the change in the [[Futures Price and the Quality Option Before E|futures price]] is approximately equal to the change in the spot price: $F_{1}-F_{0}=1.01(S_{1}-S_{0})$ .  

Arbitrageurs ensure that the spot price (in New York) and the [[Futures Price and the Quality Option Before E|futures price]] (in Chicago) move together (over a short time period), almost dollar-for-dollar  

However, from Equation (3.2), if [[Interest Rate Quotations|interest rates]] change, then $F$ and $s$ will change by slightly diferent amounts – this is a source of [[Lessons From The Crisis|basis risk]] when [[Financial Instruments PSET Solutions|hedging with futures]] contracts.1 If the [[Futures Not Subject to Cash-And-Carry|futures]] contract is correctly priced (i.e. $F=\$101$ ) then it must equal the cost of creating the ‘synthetic (replication) futures’ $S(1+r T)$ – at any other quoted [[Futures Price and the Quality Option Before E|futures price]], traders could make a risk-free ([[Arbitrage Pricing of Derivatives|arbitrage]]) proft. This ‘mispricing’ cannot persist in transparent well-functioning markets with many traders looking to exploit any ‘risk-free’ [[Quantitative Trading Strategies Lecture Notes|trading strategies]].  

Another way of looking at the no-[[Arbitrage Pricing of Derivatives|arbitrage]] approach to determining the fair [[Futures Price and the Quality Option Before E|futures price]] is to note that the actual [[Futures Not Subject to Cash-And-Carry|futures]] contract and the ‘synthetic ([[Forward and Futures Contracts|replication]]) [[Futures Not Subject to Cash-And-Carry|futures]]’ both have the same outcome at $T_{\mathbf{\delta}}$ . Hence to prevent [[Class Note 13 The LTCM Meltdown|arbitrage opportunities]], they must have the same value today. To take a [[Chapter 4 - Futures: Hedging and Speculation|long position]] in the actual [[Futures Not Subject to Cash-And-Carry|futures]] contract, no ‘own funds’ are required at $t=0$ (we ignore margin payments). At maturity of the actual [[Futures Not Subject to Cash-And-Carry|futures]], you pay out $F=\$101$ and take delivery of one stock. To create the ‘synthetic future’ you borrow $\$100$ $@4\%$ p.a.) and purchase the stock today – hence you also use no ‘own funds’. Also, this ‘synthetic [[An Asset Allocation Primer|portfolio]]’ replicates the outcome in the actual [[Futures Not Subject to Cash-And-Carry|futures]] contract since at $T$ , you owe the bank $\$101$ and you own (hold) one stock. The synthetic futures replicates the outcome at $T$ , for the actual futures contract. Hence to prevent arbitrage opportunities both must have the same value today, so the ‘no-arbitrage’ quoted futures price $F=S(1+r T)$ .  

# 3.1.3 Underpriced Futures Contract  

Above we showed that if $F_{q}>S(1+r T)$ this gives rise to ‘[[Carry Trade|cash-and-carry]]’ [[Arbitrage Pricing of Derivatives|arbitrage]] profts. Alternatively, when this inequality is reversed, $F_{q}<S(1+r T)$ , risk-free profts can be made by ‘reverse [[Dollar Rolls|cash-and-carry arbitrage]]’. Suppose (as above) on 25 June, $S=\$100$ , $r=4\%$ p.a., $T=3$ months so the correct (‘fair’ or ‘no-arbitrage’) futures price is $F=\$101$ but the quoted [[Futures Price and the Quality Option Before E|futures price]] $F_{q}=\$99$ . Hence on 25 June the actual futures contract is underpriced, $F_{q}<S(1+r T)$ . Thus, [[Arbitrage Pricing of Derivatives|arbitrage]] profts can be made by ‘selling high, buying low’.  

On 25 June, Ms Arb borrows stock-ABC from her prime broker and sells it on the NYSE – she also buys the September (3-month) [[Futures Not Subject to Cash-And-Carry|futures]] contract. The proceeds from the short-sale of stock-ABC2 are placed in a (risk-free, 3-month term) deposit at bank-A at an interest rate r. On 25 September, cash in the deposit account has accrued to $\$101=S(1+r T)$ . Ms Arb takes delivery of stock-ABC (in Chicago) from her short futures position and pays $F_{q}=\$99$ , giving her an [[Arbitrage Pricing of Derivatives|arbitrage]] proft of $\$2$ . The stock delivered in the (short) [[Futures Not Subject to Cash-And-Carry|futures]] contract is then returned to Ms Arb’s broker.  

Hence, if the quoted [[Futures Price and the Quality Option Before E|futures price]] $F_{q}$ is either slightly above or slightly below the ‘fair’ (no-[[Arbitrage Pricing of Derivatives|arbitrage]]) [[Futures Price and the Quality Option Before E|futures price]] $F=S(1+r{\dot{T}})$ , arbitrageurs will initiate simultaneous trades in the cash market (NYSE) and the [[Futures Not Subject to Cash-And-Carry|futures]] market (Chicago), which will quickly move quoted prices on these two exchanges so that $F_{q}=S(1+r T)$ at almost every instant of time. But it is possible for (3.2) not to hold at absolutely every instant of time and providing lots of ‘Ms Arbs’ act quickly enough, they may make a small [[Arbitrage Pricing of Derivatives|arbitrage]] proft – but such opportunities are likely to be very short lived and the ‘no-[[Arbitrage Pricing of Derivatives|arbitrage]]’ [[Definitions and Immediate Consequences|pricing equation]] $F_{q}=S(1+r T)$ will be quickly restored.  

The above formulas assume $r$ is measured as a [[1. DeterministicCashFlows|simple interest rate]]. If we use a discrete compound rate or a [[Arithmetic and Geometric Rates of Return|continuously compounded rate]], then the ‘fair’ [[Futures Price and the Quality Option Before E|futures price]] is given by the following formulas:  
$$
\begin{array}{l}{F=S(1+r)^{T}\mathrm{~(here~}r=\mathrm{compound~interest~rate)}}\\ {F=S e^{r T}\mathrm{(here~}r=\mathrm{continuously~compounded~rate)}}\end{array}
$$  

# 3.1.4 Futures Price at Maturity  

The ‘September-[[Futures Not Subject to Cash-And-Carry|futures]]’ matures on 25 September and will be continuously traded from 25 June (when it was initiated) and the [[Futures Price and the Quality Option Before E|futures price]] (in Chicago) changes from day-to-day (as the [[Chapter 16 - Black–Scholes Model|stock price]] on the NYSE changes). On 25 September $(=T)$ the maturity date of the [[Futures Not Subject to Cash-And-Carry|futures]] contract, the quoted [[Futures Price and the Quality Option Before E|futures price]] $F_{T}$ in Chicago must equal the quoted [[Chapter 16 - Black–Scholes Model|stock price]] on the NYSE, $S_{T}$ – otherwise risk-free [[Arbitrage Pricing of Derivatives|arbitrage]] profts can be made.  

For example, suppose the [[Futures Price and the Quality Option Before E|futures price]] in Chicago on 25 September for the ‘September [[Futures Not Subject to Cash-And-Carry|futures]] contract’ on stock-ABC is quoted as $F_{T}=\$98$ and the stock price on the NYSE is ${{S}_{T}}=$ $\$98.3$ . An [[Arbitrage Pricing of Derivatives|arbitrage]] proft can be made. Ms Arb buys the [[Futures Not Subject to Cash-And-Carry|futures]] at $F_{T}=\$98$ on 25 September and takes immediate delivery in Chicago of one stock and pays $F_{T}=\$98$ . Ms Arb can then sell stock-ABC in the cash market (NYSE) for $S_{T}=\$98.3$ making an instantaneous risk-free proft of $\$0.3$ .  

On the maturity date of the September-[[Futures Not Subject to Cash-And-Carry|futures]] (i.e. 25 September) unless the quoted [[Futures Price and the Quality Option Before E|futures price]] equals the [[Chapter 16 - Black–Scholes Model|stock price]] $(F_{T}=S_{T})$ , then risk-free [[Arbitrage Pricing of Derivatives|arbitrage]] profts are possible. The actions of Ms Arb will tend to lead to a fall in stock-ABCs price on the NYSE and rise the [[Futures Price and the Quality Option Before E|futures price]] in Chicago – this is supply and demand again. Arbitrageurs will trade [[Futures Not Subject to Cash-And-Carry|futures]] and stocks until $F_{T}=S_{T}$ , which will happen almost instantaneously on 25 September, in well-functioning liquid markets like the NYSE and the Chicago [[Futures Not Subject to Cash-And-Carry|futures]] exchange.  

# 3.1.5 Impediments to Arbitrage  

To establish the ‘fair’ or ‘no-[[Arbitrage Pricing of Derivatives|arbitrage]]’ [[Futures Price and the Quality Option Before E|futures price]] $F=S(1+r T)$ we have assumed that (a) buying and selling prices for spot market assets (e.g. stocks) are equal, and similarly for [[Mathematics of the Financial Markets|futures contracts]] (b) [[Swaps Types|borrowing and lending]] rates (from the bank) are the same, (c) there are zero transactions costs (e.g. commission fees), and (d) short-selling of the [[Risk Neutral Pricing of Options|underlying asset]] in the [[Futures Not Subject to Cash-And-Carry|futures]] contract is always possible.  

We now relax some of the above assumptions. In practice, ‘[[Dollar Rolls|cash-and-carry arbitrage]]’ involves borrowing funds at $r_{b}$ and buying the stock at the ask-price $S_{a s k}$ . If at $T$ , the total dollar transaction costs3 by Ms Arb of borrowing funds, buying the stock (at $t=0\mathrm{\dot{\Omega}}$ ) and selling the [[Futures Not Subject to Cash-And-Carry|futures]] (at $T$ ) is $T C_{T}$ , then [[Arbitrage Pricing of Derivatives|arbitrage]] is proftable if the quoted [[Futures Not Subject to Cash-And-Carry|futures]] bid-price $F_{q}>S_{a s k}(1+r_{b}T)+T C_{T}$ . The upper bound for the [[Part II-Basis Trading and the Implied Repo Rate|no-arbitrage futures price]] is therefore $F_{q}\le S_{a s k}(1+r_{b}T)+T C_{T}$ .  

For ‘reverse [[Dollar Rolls|cash-and-carry arbitrage]]’ Ms Arb buys the [[Futures Not Subject to Cash-And-Carry|futures]] (at the ask-price) and short-sells the stock at the bid-price $S_{b i d}$ . If the broker takes a ‘haircut’ of $(1-z)$ then Ms Arb will place a proportion $z\left(=0.99\right)$ of the proceeds of the short-sale $(z S_{b i d})$ in a bank deposit, earning interest $r_{d}$ . At $T$ , Ms Arb has cash of $z S_{b i d}(1+r_{d}T)-T C_{T}^{*}$ , where $\boldsymbol{T}\boldsymbol{C}_{\boldsymbol{T}}^{*}$ is the (dollar) transaction costs at $T$ of placing funds on deposit, short-selling the stock and buying the [[Futures Not Subject to Cash-And-Carry|futures]] contract. At $T_{:}$ , Ms Arb pays the quoted [[Futures Not Subject to Cash-And-Carry|futures]] ask-price $F_{q}$ and if $F_{q}<z S_{b i d}(1+r_{d}T)-T C_{T}^{*}$ there are [[Arbitrage Pricing of Derivatives|arbitrage]] profts to be made. The lower bound for the [[Part II-Basis Trading and the Implied Repo Rate|no-arbitrage futures price]] is therefore $F_{q}\ge z S_{b i d}(1+r_{d}T)-T C_{T}^{*}$ . Hence, when we take into account these ‘real world’ factors there is no longer a single correct [[Forward Contracts and Forward Prices|forward price]] but the [[Appendix 5.A Taxes and the Forward Price|no-arbitrage forward price]] will lie between an upper and lower bound.  

For ‘professional traders’ operating in highly liquid markets for ‘[[An Asset Allocation Primer|investment]] assets’ such as stocks, bonds, foreign exchange and even [[Futures Not Subject to Cash-And-Carry|commodities]] like gold and silver, the upper and lower bounds for the [[Futures Price and the Quality Option Before E|futures price]] will be ‘close to’ each other. Also, for these [[An Asset Allocation Primer|investment]] assets, short-selling the cash market asset is usually not a problem (e.g. gold or silver held as [[An Asset Allocation Primer|investment]] assets by traders, can be ‘borrowed’ by short-sellers). Also, there are always many traders who hold spot/cash market assets like gold and silver who are willing to sell from their own inventory and execute reverse [[Dollar Rolls|cash-and-carry arbitrage]]. (Note that if you own gold or silver and are selling from inventory the ‘haircut’ $z=0$ , so the upper bound for the [[Futures Price and the Quality Option Before E|futures price]] is diferent to that for a genuine short-seller who has to borrow the [[Risk Neutral Pricing of Options|underlying asset]] from her broker.) In contrast, certain spot market assets (e.g. crude oil, gas, agricultural produce) are used in the production process and for these ‘consumption assets the ease with which short-selling can be undertaken is more questionable – we deal with this below.  

# 3.1.6 Implied Repo Rate  

There is another way we can describe the [[Class Note 13 The LTCM Meltdown|arbitrage opportunities]] discussed above. Suppose on 25 June, the quoted [[Futures Price and the Quality Option Before E|futures price]] is $F_{q}=102\$ and $S=100$ , $r=4\%$ and $T=1/4$ year. The ‘fair’ [[Futures Price and the Quality Option Before E|futures price]] is $F=S(1+r T)=101\ \mathrm{\dot{~-}~}\mathrm{so}$ the quoted [[Futures Price and the Quality Option Before E|futures price]] is too high and [[Arbitrage Pricing of Derivatives|arbitrage]] profts can be made.  

Suppose on 25 June Ms Arb sells the September [[Futures Not Subject to Cash-And-Carry|futures]] contract at $F_{q}=102\$ and simultaneously buys stock-ABC at $S=100$ using her own funds. At maturity of the [[Futures Not Subject to Cash-And-Carry|futures]] $T$ , Ms Arb holds stock-ABC to deliver against her short [[Futures Not Subject to Cash-And-Carry|futures]] position and she receives $F_{q}=102$ in Chicago. The return per annum she earns (on her initial outlay of ‘own funds’ of $\$100$ ) is known as the [[The Futures Bond Basis: government bond futures and basis  trading|implied repo rate]]:  
$$
\widehat{r}=(1/T)[(F_{q}/S)-1]=0.08\:(8\%\mathrm{p.a.})
$$  

Alternatively, if Ms Arb executes the [[Arbitrage Pricing of Derivatives|arbitrage]] strategy by borrowing the $\$100$ (at $t=0$ ) in (what is called) the ‘repo market’, then the actual cost of borrowing is known as the repo rate.4 Suppose the repo cost of 3-month borrowing is $r=4\%$ p.a. then:  

If the ‘[[The Futures Bond Basis: government bond futures and basis  trading|implied repo rate]]’ $\widehat{r}$ is greater or less than the ‘quoted repo rate’ (i.e. cost of borrowing funds, r) then a (risk-free) [[PSET 1 Solution-Financial Instruments|arbitrage trade]] is possible.  

If the [[The Futures Bond Basis: government bond futures and basis  trading|implied repo rate]] $\widehat{\boldsymbol{r}}$ and actual repo rate $r$ are equal then there are no [[Class Note 13 The LTCM Meltdown|arbitrage opportunities]]:  
$$
\widehat{r}=(1/T)[(F_{q}/S)-1]=r,\mathrm{~which\implies\}F_{q}=S(1+r T)
$$  

So comparing the [[The Futures Bond Basis: government bond futures and basis  trading|implied repo rate]] with the actual repo rate is just a diferent way of seeing whether the quoted [[Futures Price and the Quality Option Before E|futures price]] $F_{q}$ is higher or lower than the fair [[Futures Price and the Quality Option Before E|futures price]] $F=S(1+r T)$ and if so, then proftable [[Class Note 13 The LTCM Meltdown|arbitrage opportunities]] are possible.  

# 3.2 DIVIDENDS, STORAGE COSTS, AND CONVENIENCE YIELD  

In practice, many [[Mathematics of the Financial Markets|futures contracts]] are not as straightforward as the one described above. For example, a stock might pay dividends (over the life of the [[Futures Not Subject to Cash-And-Carry|futures]] contract). We frst consider the case of discrete [[Exercises|dividend payments]]. Suppose (again) on 25 June, $S=100$ , $r=4\%$ p.a., and the September-[[Futures Not Subject to Cash-And-Carry|futures]] contract has a maturity of $T=1/4$ year (3 months) but is written on a dividend paying stock-ABC, which pays $a$ known dividend of $D_{1}=\$1$ in one month’s time, on 25 July (Figure 3.2). We also assume (for simplicity of exposition) that the yield curve is fat, so that $r=4\%$ p.a. for borrowing or lending money at any horizon (e.g. over 1 month, 2 months, etc.).  

Consider implementing [[Dollar Rolls|cash-and-carry arbitrage]]. For example, on 25 June, Ms Arb borrows cash, buys stock-ABC and holds the stock for 3 months. This is the ‘synthetic future’. The actual [[Accrued Interest|quoted price]] for the September-[[Futures Not Subject to Cash-And-Carry|futures]] must equal the cost of creating this ‘synthetic future’ (on stock-ABC) – if there are to be no [[Arbitrage Pricing of Derivatives|arbitrage]] profts possible. We repeat our initial example (see above) but in this case Ms Arb borrows funds from the bank over two diferent time horizons: using 1-month and 3-month [[Interest Rate Quotations|interest rates]] (which are both $4\%$ p.a.).  

![](27fb3bc8c28ac28db5bcc9ebb4f95d39224e5eaf88e8bdb350619c506c53e8b6.jpg)  
FIGURE 3.2 [[Futures Price and the Quality Option Before E|Futures price]] on dividend paying stock  

There is a single known dividend payment after 1 month (1/12th year) of $D_{1}=\$1$ , on 25 July. We have a fat yield curve with $r=4\%$ p.a. so the present value of this future dividend payment is $P V(D_{1})=\S1/\left[\left(1+0.04(1/12)\right]=\S0.9967.$ Hence Ms Arb can borrow $\$0.9967$ on 25 June from bank-A at the one-month interest rate and know that she can pay back the $\$1$ (owed to bank-A) from the (known) dividend payment on stock-ABC, on 25 July. For Ms Arb there are zero net cash fows on 25 July – the dividend received on the stock will be used to pay of the bank loan outstanding of $\$1$ .  

Therefore in order to purchase the stock at a price of $S=\$100$ , Ms Arb only needs to borrow an additional $S-P V(D_{1})=\S99.0033$ on 25 June from bank-A. For this second loan she borrows at the 3-month rate, so that repayment of this loan coincides with the maturity date of the futures contract. In 3 months’ time (on 25 September) Ms Arb will owe bank-A, $\$99.9933,[=\S99.0033(1+0.04/4)]$ . But 25 September is also the maturity date of the actual [[Futures Not Subject to Cash-And-Carry|futures]] contract and from our earlier discussion we know that the correct (‘fair’, ‘no-[[Arbitrage Pricing of Derivatives|arbitrage]]’) [[Futures Price and the Quality Option Before E|futures price]] $F$ must equal the cost of creating the synthetic [[Futures Not Subject to Cash-And-Carry|futures]] hence:  
$$
F=[S-P V(D_{1})](1+r T)=\S99.9933
$$  

Notice that all the borrowed funds, $\$0.9967+\S99.0033$ are used to purchase the stock for $\$100$ , in order to execute the [[Arbitrage Pricing of Derivatives|arbitrage]] strategy. The ‘frst’ $\$0.9967$ Ms Arb borrows means she owes $\$1$ after $^{1}$ month – but this debt is paid of with the $\$1$ dividend payout on 25 July from stock-ABC that Ms Arb holds. The net cost of the cash-and-carry arbitrage is the $\$99.9933$ owed to the bank after 3 months – and this is the correct (no-[[Arbitrage Pricing of Derivatives|arbitrage]]) price for the September-[[Futures Not Subject to Cash-And-Carry|futures]] contract, quoted on 25 June.  

# 3.2.1 Several Discrete Dividend Payments  

Suppose there are $N$ [[Exercises|dividend payments]] of diferent dollar amounts $D_{i}$ on the stock, between today and the maturity date of the [[Futures Not Subject to Cash-And-Carry|futures]] contract, that are payable at discrete times $t_{i}$ (from  

today). Then the correct (no-[[Arbitrage Pricing of Derivatives|arbitrage]]) [[Futures Price and the Quality Option Before E|futures price]] is:  
$$
F=[S-P V(D)](1+r T)
$$  

where $\begin{array}{r}{P V(D)=\sum_{i=1}^{N}D_{i}/(1+r_{i}t_{i})}\end{array}$ , $r_{i}=$ spot [[Interest Rate Quotations|interest rates]] (simple rate) between today and $t_{i}$ and $r=$ interest rate with maturity $T$ (when the [[Futures Not Subject to Cash-And-Carry|futures]] contract matures).  

# 3.2.2 Bond Futures  

In principle, the above formula can also be applied to [[Arbitrage Pricing of Derivatives|pricing]] a [[Futures Not Subject to Cash-And-Carry|futures]] contract on a coupon paying T-bond. The [[Futures Price and the Quality Option Before E|futures price]] is $F=[S-P V(\mathbf{C})](1+r T)$ where $s$ is the current cash-market price of the underlying (deliverable) bond, $P V(\mathrm{C})$ is the present value of the [[Realized Returns|coupon payments]] on the underlying bond over the life of the [[Futures Not Subject to Cash-And-Carry|futures]] contract, $T$ is the maturity of the [[Futures Not Subject to Cash-And-Carry|futures]] and $r$ is the [[Black Scholes Derivation|risk-free rate]] for maturity $T$ . This formula ignores several ‘real world’ complications (e.g. [[Intra-Year Compounding and Day-Count|accrued interest]]) which are discussed in Chapter 13.  

# 3.2.3 Continuous Dividend Payments  

Suppose stocks pay out dividends (evenly) at a rate of $\delta=2\%$ p.a. Then in the above [[Arbitrage Pricing of Derivatives|arbitrage]] example, when Ms Arb buys the stock for $\$100$ , some of the borrowed money can be paid back from the receipts of future dividends – this reduces the ‘cost of carry’. If the rate at which dividends are paid is $\delta=2\%$ p.a. then over 3 months Ms Arb receives $\$0.5$ in dividends $(=\S100\times0.02\times\:^{1}/_{4}=S\delta T)$ which reduces the overall cost of carry. So the correct (no-[[Arbitrage Pricing of Derivatives|arbitrage]]) [[Futures Price and the Quality Option Before E|futures price]] is:  
$$
F=S\ \left[1+(r-\delta)T\right]
$$  

When using compound and [[PSET 7 Solutions-Financial Instruments|continuously compounded interest]] rates the formulas are:  
$$
\begin{array}{r l}&{\boldsymbol{F}=S(1+r-\delta)^{T}\mathrm{\ensuremath{\mathrm{\(compoundrates)}}}}\\ &{\boldsymbol{F}=S e^{(r-\delta)T}\mathrm{\ensuremath{\mathrm{\(continuouslycompoundedrates)}}}}\end{array}
$$  

Using Equations (3.6a)–(3.6c), the quoted [[Futures Price and the Quality Option Before E|futures price]] (in Chicago) on 25 June (say) will be above the quoted [[Chapter 16 - Black–Scholes Model|stock price]] (on the NYSE), if $r>\delta$ and below the quoted [[Chapter 16 - Black–Scholes Model|stock price]] if $r<\delta$ . These two cases are referred to as:  

Often backwardation is also referred to as an inverted market. [[Contango And Backwardation In Arbitrage-Free Futures-Markets|Contango and backwardation]] are also used in a slightly diferent way, to describe a whole series of [[Futures Not Subject to Cash-And-Carry|futures]] prices for contracts with diferent maturity dates (but on the same [[Risk Neutral Pricing of Options|underlying asset]]). This is the [[The Vasicek Model|term structure]] of [[Futures Not Subject to Cash-And-Carry|futures]] prices – which can be represented graphically. For example, the [[Futures Not Subject to Cash-And-Carry|futures]] market is said to be in contango (on 25 June, say) if the quoted [[Futures Not Subject to Cash-And-Carry|futures]] prices increase with the maturity dates of the contracts – $(F^{T=5}>F^{T=4}>F^{T=3}>F^{T=1}>S)$ , so prices of ‘far dated’ [[Mathematics of the Financial Markets|futures contracts]] are higher than those of ‘near dated’ contracts.  

# 3.3 COMMODITY FUTURES  

Let’s consider the determination of the correct (no-[[Arbitrage Pricing of Derivatives|arbitrage]]) future prices on [[Futures Not Subject to Cash-And-Carry|commodities]] such as grains and oilseed (e.g. wheat, soybeans, sunfower oil), or food (e.g. cocoa, orange juice), or metals and petroleum (e.g. gold, silver, platinum, heating oil), or livestock and meat (hogs, live cattle, pork bellies), which are actively traded on various exchanges around the world – for example, New York Cotton Exchange (NYCE), Kansas City Board of Trade (KCBT), Mid America Commodity Exchange (MCE), New York Mercantile Exchange (NYMEX) and London Metals Exchange (LME).  

When discussing [[Futures Not Subject to Cash-And-Carry|futures]] prices we split [[Futures Not Subject to Cash-And-Carry|commodities]] into two main types. [[An Asset Allocation Primer|Investment]] [[Futures Not Subject to Cash-And-Carry|commodities]] include precious metals such as gold, silver, platinum and copper which are widely held as [[An Asset Allocation Primer|investment]] assets (as well as being used in the production of other goods). Production [[Futures Not Subject to Cash-And-Carry|commodities]] are primarily held as inputs to the production process to provide consumer goods (e.g. agricultural and energy [[Futures Not Subject to Cash-And-Carry|commodities]]) and are not usually held for [[An Asset Allocation Primer|investment]] purposes.  

# 3.3.1 Investment Commodities  

[[An Asset Allocation Primer|Investment]] [[Futures Not Subject to Cash-And-Carry|commodities]] can be priced using ‘[[Carry Trade|cash-and-carry]]’ [[Arbitrage Pricing of Derivatives|arbitrage]], if we take account of [[Primary vs. Secondary Commodities|storage costs]]. If to undertake [[Dollar Rolls|cash-and-carry arbitrage]] you purchase gold in the cash market (using borrowed money), then you have to store and insure the gold until the maturity date of the [[Futures Not Subject to Cash-And-Carry|futures]] contract. You have [[Primary vs. Secondary Commodities|storage costs]] on top of the existing interest cost on your borrowed money, so the [[Futures Price and the Quality Option Before E|futures price]] for gold is given by5:  
$$
F=S[1+(r+s)T]
$$  

where $s=$ storage cost of gold (per annum). This equation will hold at all points in time since [[Purpose and Structure of Financial Markets 1|arbitrage strategies]] including those which require short-selling the spot asset (gold, silver) will always be possible, because many holders of such [[An Asset Allocation Primer|investment]] assets do not have an alternative use for them (e.g. they are not jewellery manufacturers). [[Arbitrage Pricing of Derivatives|Arbitrage]] involving purchases of these spot [[An Asset Allocation Primer|investment]] assets clearly poses no problems in liquid markets. Equation (3.7) indicates that at any time, the current quoted [[Futures Price and the Quality Option Before E|futures price]] $F$ for gold (in Chicago) will always be above the spot price $s$ for gold (quoted in New York, say).  

# 3.3.2 Production Commodities  

One might think that a [[Futures Not Subject to Cash-And-Carry|futures]] contract on a ‘production commodity’ like oil would be determined by Equation (3.7), which implies the oil [[Futures Price and the Quality Option Before E|futures price]] (in Chicago in USD) would always be above the spot price for oil (quoted in USD in Texas, say). But for many production [[Futures Not Subject to Cash-And-Carry|commodities]] such as oil, at certain times it is observed that the quoted [[Futures Price and the Quality Option Before E|futures price]] is actually below the spot price, (i.e. $F<S$ ) – we then say that oil [[Futures Not Subject to Cash-And-Carry|futures]] are in backwardation. This outcome is rationalised by adapting Equation (3.7) and introducing a concept known as the convenience yield $y$ , for oil. How does this come about?  

The convenience yield arises because the holder (Exxon) of a spot commodity (e.g. barrels of crude oil) has the added advantage that they can supply his local customers (in Texas) if the oil goes into short supply (e.g. during abnormally cold winter months) and hence retain customer loyalty. This ‘convenient’ state of afairs has an intrinsic value for the holder of oil, which is referred to as the convenience yield.  

The presence of a convenience yield might therefore prevent [[Dollar Rolls|cash-and-carry arbitrage]] operating and this invalidates Equation (3.7). For example, suppose the current spot price of oil (quoted in Texas) is high – an indication that oil is currently in short supply (i.e. low levels of oil stored on-shore in Texas). Ms Arb wants to undertake an [[Arbitrage Pricing of Derivatives|arbitrage]] strategy which requires her to short-sell spot oil at $s$ ( $\mathfrak{P}$ per barrel) and simultaneously buy [[Mathematics of the Financial Markets|futures contracts]] on oil at $F$ ( $\mathfrak{P}$ per barrel). Short-selling means Ms Arb has to borrow oil from a holder of oil (Exxon) – which is being stored in onshore oil containers (or maybe sitting in the hold of a tanker in the middle of the ocean). Short-selling may not be possible in practice if Exxon is unwilling to ‘loan out’ their oil inventory.  

To make a risk-free proft Ms Arb has to borrow barrels of oil today and quickly sell them in the spot market (in Texas) and immediately invest the proceeds in a risk-free deposit account. When her long [[Futures Not Subject to Cash-And-Carry|futures]] contract matures she pays F and takes delivery of oil in the [[Futures Not Subject to Cash-And-Carry|futures]] contract and ‘[[Assets|returns]]’ the ‘borrowed oil’ to Exxon. But if holders of spot oil (Exxon) will not provide spot oil to Ms Arb (at the required geographical destination) then [[Arbitrage Pricing of Derivatives|arbitrage]] involving short-selling of oil becomes impossible.  

Hence at these times Equation (3.7) will not hold for quoted [[Futures Not Subject to Cash-And-Carry|futures]] prices on oil and $F\neq S$ $[1+(r+s)T]$ based on historical data. But (daily) historical data on $F,S,r,s$ and $T$ are available. We therefore introduce an ‘unknown variable’, the convenience yield $y$ , to force an equality, so that:  
$$
F=S[1+(r+s-y)T]
$$  

We do this by taking quoted (daily) prices from the historical data, on $F,S,r,s$ and $T$ we derive (‘back out’) the historical ‘convenience yield’ (p.a.) which is given by:  
$$
y=r+s-{\frac{1}{T}}\left({\frac{F-S}{S}}\right)
$$  

Using calculated daily values for $y$ using (3.8b) it must be the case that for the historical data the equality in (3.8a) holds. The right-hand side of Equation (3.8a) now provides the determinants of the historical oil [[Futures Price and the Quality Option Before E|futures price]], $F$ . This provides a way of trying to determine what will happen to the [[Futures Price and the Quality Option Before E|futures price]] for oil over the coming days and months. If today, we know what the convenience yield $y$ of holding a spot barrel of oil (over say the next 3 months) is likely to be, then we could use (3.8a) to price a 3-month [[Futures Not Subject to Cash-And-Carry|futures]] contract. The historical time series for $y$ can be used to try and forecast what $y$ might be over the next 3 months. But clearly this is a forecast and could be very inaccurate. However, the market will today set a [[Futures Price and the Quality Option Before E|futures price]], which will embody traders’ best estimate of the future convenience yield.  

If the convenience yield remains constant then changes in the oil [[Futures Price and the Quality Option Before E|futures price]] (over the next 3 months) will be closely linked to changes in the spot price of oil. But the convenience yield of oil could itself change dramatically over the next 3 months, as supply and demand for oil in the production process and by consumers, as well as inventories of spot oil, change. Hence there is therefore not such a close link between changes in spot and [[Futures Not Subject to Cash-And-Carry|futures]] prices for ‘production [[Futures Not Subject to Cash-And-Carry|commodities]]’ as there is for [[Mathematics of the Financial Markets|futures contracts]] on other ‘[[An Asset Allocation Primer|investment]]’ assets (e.g. stocks, stock indices, currencies, bonds, gold) – so $F$ and $s$ may not move approximately dollar-for-dollar because of changes in y. This makes [[Key Rates O1s Durations and Hedging|hedging]] ‘production [[Futures Not Subject to Cash-And-Carry|commodities]]’ more di\$cult – the technical way of saying this is that ‘[[Lessons From The Crisis|basis risk]]’ is high for [[Financial Instruments PSET Solutions|commodity futures]] where the [[Risk Neutral Pricing of Options|underlying asset]] is a ‘production commodity’. We will consider these issues further in the chapter on energy [[Chapter 9 Arbitrage and Hedging With Options|derivatives]].  

# 3.3.3 Continuous and Discrete Compounded Rates  

The above formulas for [[Futures Not Subject to Cash-And-Carry|futures]] prices using simple rates, compounded rates, and [[PSET 7 Solutions-Financial Instruments|continuously compounded interest]] rates, look slightly diferent. However, they all give exactly the same value for F. This is easily verifed by recalling the relationship between the various defnitions. Let $r_{s}=$ simple rate, $r=$ discrete compound rate and $r_{c}=$ [[Arithmetic and Geometric Rates of Return|continuously compounded rate]] – all expressed ‘per annum’ (decimal). If $\$1$ is invested today, we require that this will result in the same amount at the end of, say, 3 months (i.e. $T={\sqrt[1]{4}}.$ ), regardless of which interest rate convention is used. Therefore the interest rate conventions are defned so that:  
$$
1+r_{s}T=(1+r)^{T}=e^{r_{c}.T}
$$  

For a [[Futures Not Subject to Cash-And-Carry|futures]] contract on (a non-dividend paying) stock we have $F=S(1+r_{s}T)$ – but using (3.9) this is equivalent to $F=S(1+r)^{T}$ and $\bar{\boldsymbol{F}}=\bar{S e}^{r_{c}T}$ – hence the alternative formulas give the same value for $F$ . It is also true that all three formulas would give approximately the same answer for $F$ even if we used the ‘incorrect’ interest rate in each formula. This is because for ‘small’ values of $r$ , the following approximations are quite accurate:  
$$
e^{r.T}\approx1+r T\quad\mathrm{and}\quad(1+r)^{T}\approx1+r T
$$  

Finally note that if:  
$$
\begin{array}{r}{F=S e^{r_{c}T}\quad\mathrm{then}\quad S=F e^{-r_{c}T}}\end{array}
$$  

# 3.3.4 Non-storable Commodities  

How can we price a forward/[[Futures Not Subject to Cash-And-Carry|futures]] contract on a non-storable commodity like electricity and what about any seasonality in the [[Contango And Backwardation In Arbitrage-Free Futures-Markets|spot prices]] of [[Futures Not Subject to Cash-And-Carry|commodities]] such as an agricultural product like wheat? The spot price of wheat tends to rise just before the harvest, usually around August and then falls as the wheat supply comes onto the (spot/cash) market. Seasonality in the spot price will be refected in seasonality in the [[Futures Price and the Quality Option Before E|futures price]] because [[Arbitrage Pricing of Derivatives|arbitrage]] is possible within the year, using inventories of wheat. The convenience yield of wheat just before the harvest is likely to be high and just after the harvest, when inventories of wheat are large, the convenience yield is likely to be low. We can use Equation (3.8a) to determine the [[Futures Price and the Quality Option Before E|futures price]] providing we can obtain an estimate of the market’s view of the future availability of the commodity, which infuences the convenience yield. We can ‘back out’ the historical time series of the convenience yield using (3.8b) and then use statistical [[Week 2 Fundamentals Of Forecasting|forecasting]] methods, to forecast the convenience yield (over the life of the [[Futures Not Subject to Cash-And-Carry|futures]] contract).  

Instead of trying to estimate the convenience yield, a diferent approach to determine today’s [[Futures Price and the Quality Option Before E|futures price]] involves trying to forecast the [[Hedging Strategies with Forwards|future spot price]] of a commodity. Suppose it is 1 May and we wish to determine today’s [[Futures Price and the Quality Option Before E|futures price]] $F_{0}$ for delivery of wheat in 6 months’ time on 1 November $\left\langle T={}^{1}/_{2}\right.$ year). Suppose the expected spot price of wheat (per bushel) for November is $E S_{T}$ and the [[Risk Preferences|riskiness]] of wheat prices means that investors require a (simple) return of $R$ p.a. to speculate on the [[Hedging Strategies with Forwards|future spot price]] of wheat. If the [[Futures Price and the Quality Option Before E|futures price]] quoted today for delivery and payment of wheat in 6 months is $F_{0}$ , then a speculator could borrow cash equal to $F_{0}/(1+r T)$ and take a [[Chapter 4 - Futures: Hedging and Speculation|long position]] in the [[Futures Not Subject to Cash-And-Carry|futures]] contract. Hence, at $T$ the speculator has funds available to take delivery of wheat in the [[Futures Not Subject to Cash-And-Carry|futures]] contract. Suppose the speculator believes that the expected price of wheat in 6 months’ time is $E S_{T}$ which has a present value of $E S_{T}/(1+R.T)$ . If we equate the present value of payment for the wheat delivered in the [[Futures Not Subject to Cash-And-Carry|futures]] contract with the present value of supplying spot-wheat in 6 months’ time, we have:  
$$
F_{0}/(1+r T)=E S_{T}/(1+R.T)
$$  

and  
$$
F_{0}=E S_{T}[(1+r T)/(1+R.T)]
$$  

So today’s [[Futures Not Subject to Cash-And-Carry|futures]] quote depends on the expected spot price of wheat, which itself is infuenced by forecasts of supply and demand for wheat in 6 months’ time – this can lead to seasonality in spot and [[Futures Not Subject to Cash-And-Carry|futures]] prices. Where possibilities for [[Arbitrage Pricing of Derivatives|arbitrage]] are limited then the close link between spot and [[Futures Not Subject to Cash-And-Carry|futures]] prices is broken and successful [[Key Rates O1s Durations and Hedging|hedging]] becomes more di\$cult. Note also that the above approach implies that the forward price is not an unbiased forecast of the expected future spot price – unless the required return on the underlying asset $R$ , equals the [[Black Scholes Derivation|risk-free rate]], r. (This can be shown to be the case using the [[2. Forwards, Swaps, Futures, and Options|Capital Asset Pricing Model]] [CAPM], when the [[Risk Neutral Pricing of Options|underlying asset]] and the ‘market return’ are uncorrelated and hence the asset-beta is zero.)  

# 3.4 VALUE OF A FORWARD CONTRACT  

In this section we explicitly deal with forward contracts rather than [[Mathematics of the Financial Markets|futures contracts]]. Because a [[Futures Not Subject to Cash-And-Carry|futures]] contract is marked-to-market daily and cash is credited or debited to the margin account, a [[Futures Not Subject to Cash-And-Carry|futures]] contract has a value of zero at the end of each trading day.  

But when dealing with forward contracts it is important to distinguish between price and value. Suppose that on 25 January $(t=0)$ ) you initiate (go long) a 6-month [[Forward Points in Currency|forward contract]] 1 $\left\langle T={}^{1}/_{2}\right.$ year) on a stock, at a [[Forward Contracts and Forward Prices|forward price]] $F_{0}=\$90$ . At $t=0$ no cash changes hands. The maturity date of the contract is 25 July. On 25 January you have agreed to exchange the underlying assets (stocks) in exchange for a cash payment of $F_{0}=\$90$ on 25 July.  

At any future date (e.g. $t=\mathrm{April})$ during the life of the [[Forward Points in Currency|forward contract]], you can enter into a ‘new’ [[Forward Points in Currency|forward contract]] with the same delivery date, 25 July, as the initial [[Forward Points in Currency|forward contract]]. The [[Forward Contracts and Forward Prices|forward price]] $F_{t}$ for a ‘new’ [[Forward Points in Currency|forward contract]] entered into on 25 April (with delivery date, 25 July) will be diferent from the price of the ‘old’ [[Forward Points in Currency|forward contract]] $F_{0}=\$90$ initiated on 25 January (because of changes in the [[Chapter 16 - Black–Scholes Model|stock price]] between 25 January and 25 April). The question we wish to answer is: what determines the value of the ‘old’ [[Forward Points in Currency|forward contract]] (initiated on 25 January) each day, as this contract approaches its maturity date of 25 July?  

# 3.4.1 Value When Initiated  

Suppose at the initiation of the [[Forward Points in Currency|forward contract]] on 25 January the [[Forward Contracts and Forward Prices|forward price]] is $F_{0}=$ $S_{0}(1+r T)=\S90$ . However, the value of the [[Forward Rates Agreement|long forward]] contract is zero, since no [[Class Note 13 The LTCM Meltdown|arbitrage opportunities]] exist and no cash changes hands.  

At the initiation of a [[Forward Points in Currency|forward contract]], the value of the contract is zero.  

# 3.4.2 Value at Maturity  

Clearly the price of a [[Forward Points in Currency|forward contract]] on its maturity date must equal the spot price: $F_{T}=S_{T}$ . If $F_{T}\neq S_{T}$ it would be possible to make [[Arbitrage Pricing of Derivatives|arbitrage]] profts. For example, if $F_{T}=\$90$ and ${{S}_{T}}=$ $\$100$ you could buy a [[Forward Rates Agreement|long forward]] contract, take delivery of the underlying (stock) immediately and pay $\$90$ . You could then immediately sell the underlying (stock) in the spot market (NYSE) for $\$100$ and pocket the diference of $\$10$ . The deal is virtually risk-free. Hence arbitrage will ensure that $F_{T}=S_{T}$ on the maturity date of the [[Forward Points in Currency|forward contract]].  

Now consider the value of a [[Chapter 4 - Futures: Hedging and Speculation|long position]] in $a$ [[Forward Points in Currency|forward contract]] at maturity. If the [[Forward Points in Currency|forward contract]] was initially entered into on 25 January at a price $F_{0}=\$90$ , then at maturity $T$ (25 July), the value of this ‘old’ (maturing) forward contract is the proft you could make at $T$ , hence:  

VT Value of [[Chapter 4 - Futures: Hedging and Speculation|long position]] in ‘ ’ [[Forward Points in Currency|forward contract]] maturit $\mathrm{\Omega}^{\prime}=S_{T}-F_{0}$  

If you are long the ‘old’ [[Forward Points in Currency|forward contract]] at an initial [[Forward Contracts and Forward Prices|forward price]] (agreed on 25 January) of $F_{0}=\$90$ , then at $T$ (on 25 September) you can take delivery of the underlying stock in the forward contract, pay $F_{0}=\$90$ and immediately sell the underlying for $S_{T}$ in the cash market. If $S_{T}>F_{0}$ the [[Chapter 4 - Futures: Hedging and Speculation|long position]] in the [[Forward Points in Currency|forward contract]] has a positive value (and vice versa).  

# 3.4.3 Value of Forward Contract Prior to Expiration  

Suppose on 25 January $(t=0)$ a 6-month [[Forward Points in Currency|forward contract]] (on a non-dividend paying stock) with maturity on 25 July is purchased at a [[Forward Contracts and Forward Prices|forward price]] $F_{0}=\$90$ . Sometime later on 25 April, the forward price $F_{t}$ for a ‘new’ forward contract (with the same maturity date, 25 July) has only 3 months to maturity $(T-t=0.25)$ (see Figure 3.3) and if $S_{t}=\S100$ and $r=0.05$ (continuously compounded), then the price of this ‘new’ [[Forward Points in Currency|forward contract]] on 25 April is:  
$$
F_{t}=S_{t}e^{r(T-t)}=\mathbb{\S}100\mathrm{e}^{0.05(0.25)}=\mathbb{\S}101.2578
$$  

The question we wish to answer is: what is the value $V_{t}$ on 25 April, of the original ‘old’ [[Forward Points in Currency|forward contract]]?  

On 25 January, an investor Ms Player initiated her [[Chapter 4 - Futures: Hedging and Speculation|long position]] in the ‘old’ contract at a [[Forward Contracts and Forward Prices|forward price]] of $F_{0}=\$90$ . On 25 April, Ms Player could short the ‘new’ contract (with the same maturity date of 25 July) at a forward price $F_{t}=\$101.2578$ . Then at maturity of both contracts on 25 July Ms Player can (a) take delivery of the stock from her [[Chapter 4 - Futures: Hedging and Speculation|long position]] in the ‘old’ [[Forward Points in Currency|forward contract]] by paying $F_{0}=\$90$ , and (b) then deliver this stock to fulfl her obligations in the ‘new’ short forward contract and receive $F_{t}=\$101.2578$ in cash on 25 July. This cash proft at time $T(25\mathrm{{July})}$ is $F_{t}-F_{0}$ and is risk-free, because at $t=25$ April she knows what this proft will be. The value of the old contract at time $t=25$ April must therefore equal the present value of $F_{t}-F_{0}$ over the remaining period $T-t$ :  
$$
\begin{array}{r}{V_{t}(\mathrm{`Old'forwardcontract})=P V[\mathrm{`New'forwardprice\at\}t-\mathrm{`Old}}\\ {=[F_{t}-F_{0}]e^{-r(T-t)}=S_{t}-F_{0}e^{-r(T-t)}}\end{array}
$$  

![](fcad115f828448b0b0dd7387bab3d6c2aa227f2372d29d2ccb845b6f04a0085e.jpg)  
FIGURE 3.3 Value of [[Forward Points in Currency|forward contract]]  

where we have used $F_{t}=S_{t}e^{r(T-t)}$ . The above expression for the value of the ‘old’ contract follows from [[Forward Contracts and Forward Prices|arbitrage arguments]].  

Ms Player purchased the ‘old’ July-[[Forward Points in Currency|forward contract]] on 25 January at a [[Forward Contracts and Forward Prices|forward price]] $F_{0}=\$90$ and on 25 April she shorts a new July-forward contract at $F_{1}=\$101.2578$ . [[Short Selling|Shorting]] the ‘new’ contract on 25 April will yield receipts of $F_{1}=\$101.2578$ on 25 July and the ‘old’ contract requires a payment of $F_{0}=\$90$ on 25 July. Hence the proft on 25 July is $\$11.2578[=\S101.2578-\S90]$ . Since this strategy is risk-free, another investor would be prepared to pay Ms Player $V_{t}={\tt811.118}[={\tt811.2578}\mathrm{e}^{-0.05(0.25)}]$ on 25 April, for the ‘old’ [[Forward Points in Currency|forward contract]] (which was initially negotiated on 25 January). Otherwise, [[Arbitrage Pricing of Derivatives|arbitrage]] profts can be made.6  

Value of an ‘old’ [[Forward Points in Currency|forward contract]] at any time prior to maturity  
$$
V_{t}=\left[F_{t}-F_{0}\right]e^{-r(T-t)}=S_{t}-F_{0}e^{-r(T-t)}
$$  

The ‘mark-to-market’ value of the [[Forward Rates Agreement|long forward]] contract on 25 April is $V_{t}=\mathbb{\$11.118}$ . If JPMorgan had initially sold this contract it would have to pay the person holding the long position $\$11.118$ on 25 April, to nullify the contract.  

# 3.4.4 Replication Portfolio  

The value of the ‘old’ [[Forward Points in Currency|forward contract]] can also be determined by creating a ‘[[Chapter 22 - BOPM: Implementation|replication portfolio]]’ at $t=25$ April. Suppose on 25 April you purchase the stock for $S_{t}$ and also borrow a cash amount of $F_{0}e^{-r(T-t)}$ from the bank at interest rate, $r-$ this is the [[Chapter 22 - BOPM: Implementation|replication portfolio]] which will mimic the outcome of the ‘old’ [[Forward Points in Currency|forward contract]] at maturity, $T_{\mathbf{\delta}}$ .  

The amount you owe the bank on 25 July is $F_{0}$ . The net cost (i.e. ‘own funds’) to initiate this [[Forward and Futures Contracts|replication]] strategy at $t=25$ April is $S_{t}-F_{0}e^{-r(T-t)}$ . At $T$ you have one stock worth $S_{T}$ and you owe the bank $F_{0}$ . But the latter outcome from the [[Chapter 22 - BOPM: Implementation|replication portfolio]] at $T$ is exactly the same as if you were long a [[Forward Points in Currency|forward contract]] (which matures at $T$ ) with [[Forward Contracts and Forward Prices|forward price]] of $F_{0}$ . We have therefore ‘replicated’ the outcome at $T$ , for a [[Forward Points in Currency|forward contract]] with a [[Forward Contracts and Forward Prices|forward price]] of $F_{0}$ . The cost of setting up this ‘[[Chapter 22 - BOPM: Implementation|replication portfolio]]’ at $t=25$ April is $S_{t}-F_{0}e^{-r(T-t)}$ . At $t$ , the value of the ‘old’ [[Forward Points in Currency|forward contract]] must equal the cost of setting up the [[Chapter 22 - BOPM: Implementation|replication portfolio]] (otherwise [[Arbitrage Pricing of Derivatives|arbitrage]] profts can be made) hence, $V_{t}=S_{t}-F_{0}e^{-r\bar{(T-t)}}$ .  

Note that if we use [[Continuously Compounding Interest|compound interest]] rates or [[Interest Rate Quotations|simple interest]] (rather than continuously compounded rates), the value of a [[Forward Points in Currency|forward contract]] (if the [[Risk Neutral Pricing of Options|underlying asset]] has no cash fows) is:  
$$
V_{t}={\frac{F_{t}-F_{0}}{(1+r)^{T-t}}}=S_{t}-{\frac{F_{0}}{(1+r)^{T-t}}}
$$  

or  
$$
V_{t}={\frac{F_{t}-F_{o}}{[1+r(T-t)]}}=S_{t}-{\frac{F_{o}}{[1+r(T-t)]}}\quad({\mathrm{simple~rates}})
$$  

# 3.4.5 Underlying Asset Has a Cash Inflow  

For a [[Forward Points in Currency|forward contract]] on a dividend paying stock, which matures on 25 July, the ‘new’ [[Forward Points in Currency|forward contract]] (initiated on 25 April) has a [[Forward Contracts and Forward Prices|forward price]]:  
$$
F_{t}=S_{t}e^{(r-\delta)(T-t)}
$$  

where $\delta$ is the (continuously compounded) dividend yield. On 25 April, the value of an ‘old’ [[Forward Points in Currency|forward contract]] (initiated on 25 January, with maturity date 25 July) which pays dividends on the underlying stock is:  
$$
V_{t}=\left[F_{1}-F_{0}\right]e^{-r(T-t)}=S_{t}e^{-\delta(T-t)}-F_{0}e^{-r(T-t)}
$$  

At inception, a [[Forward Points in Currency|forward contract]] has a value of zero which is consistent with the above equation – set $t=0$ and note that at inception $F_{0}=S_{0}e^{(r-\delta)T}$ so we obtain $V_{0}=0$ . At maturity $t=T$ and (3.15) implies $V_{T}=S_{T}-F_{0}$ , which is consistent with the value of the [[Forward Points in Currency|forward contract]] at maturity, as we found earlier. Note that at $t>0$ the value of the [[Forward Points in Currency|forward contract]] $V_{t}$ can be either positive or negative.7  

Note also that $\delta$ could represent any (continuous) cash infows from the [[Risk Neutral Pricing of Options|underlying asset]]. For a [[Forward Points in Currency|forward contract]] on a commodity (e.g. oil), $\delta=$ convenience yield less the storage cost $(=y-s)$ . For a [[Forward Points in Currency|forward contract]] on foreign [[Forwards and Futures Notes|currency]], $\delta=$ [[Exercises|risk-free interest rate]] on foreign bank deposits and $r=\mathrm{risk}$ -free rate on domestic deposits.  

If the net cash infows on the [[Risk Neutral Pricing of Options|underlying asset]] are discrete then the value of the ‘old’ [[Forward Points in Currency|forward contract]] at $t$ is  
$$
V_{t}=S_{t}-P V\left(n e t c a s h i n f l o w s\right)-F_{0}e^{-r(T-t)}
$$  

where $P V$ is the present value of any (dollar) net cash infows between today $t$ and the maturity date of the [[Forward Points in Currency|forward contract]], $T.$ . The net cash infows could be ‘dollar dividends’ on a stock, or receipts of coupons on a bond, or for [[Futures Not Subject to Cash-And-Carry|commodities]] the ‘dollar’ convenience yield less [[Primary vs. Secondary Commodities|storage costs]].  

# 3.5 SUMMARY  

• Risk-free [[Arbitrage Pricing of Derivatives|arbitrage]] ensures that the correct/[[Chapter 3 - Forward and Futures Prices|fair forward price]] is determined by the cost of a synthetic or [[Chapter 22 - BOPM: Implementation|replication portfolio]] which produces the same outcomes as the [[Forward Points in Currency|forward contract]] itself – this is [[Dollar Rolls|cash-and-carry arbitrage]]. For the simplest [[Forward Points in Currency|forward contract]] on an [[Risk Neutral Pricing of Options|underlying asset]] $s$ (which pays no cash fows) we have: $F=S(1+r T)$ .   
• We assume that [[Futures Not Subject to Cash-And-Carry|futures]] prices are determined by [[Arbitrage Pricing of Derivatives|arbitrage]] in the same way as forward prices – this is usually a good working assumption because margin payments on [[Mathematics of the Financial Markets|futures contracts]] do not have a major impact on the above relationship.   
• If the quoted [[Futures Price and the Quality Option Before E|futures price]] does not equal the ‘correct’ (no-[[Arbitrage Pricing of Derivatives|arbitrage]]) [[Futures Price and the Quality Option Before E|futures price]] determined by the cost-of-carry model, then risk-free [[Arbitrage Pricing of Derivatives|arbitrage]] profts can be made.   
• [[Dollar Rolls|Cash-and-carry arbitrage]] ensures that the [[Futures Price and the Quality Option Before E|futures price]] on a stock (traded in Chicago) moves almost dollar-for-dollar with the spot (cash-market) price of the stock (on the NYSE), over small time intervals.   
• [[Dollar Rolls|Cash-and-carry arbitrage]] can be used to determine the correct (no-[[Arbitrage Pricing of Derivatives|arbitrage]]) [[Futures Price and the Quality Option Before E|futures price]] where the underlying assets involve intermediate cash fows (e.g. [[Futures Not Subject to Cash-And-Carry|futures]] contract on [[Chapter 25 - Pricing European Options|dividend paying stocks]] and stock indices) and that involve [[Primary vs. Secondary Commodities|storage costs]] (e.g. silver, gold).   
• [[Mathematics of the Financial Markets|Futures contracts]] on [[Futures Not Subject to Cash-And-Carry|commodities]] that are also used in the production of consumer goods (e.g. oil, gas, wheat, live cattle) are more di\$cult to price by cash-and-carry arbitrage because the futures price depends on the ‘convenience yield’ which is di\$cult to forecast.   
• The [[Futures Price and the Quality Option Before E|futures price]] may not move exactly in line with the (underlying) spot price if [[Interest Rate Quotations|interest rates]], dividends, [[Primary vs. Secondary Commodities|storage costs]] or the convenience yield change in unpredictable ways – and the convenience yield is the most unpredictable element.   
• The [[Forward Contracts and Forward Prices|forward price]] (on a non-dividend paying stock) with maturity in $T$ years is $F_{0}=S_{0}e^{r T}$ determined today $(t~=~0)$ . After initiation, the value of this [[Forward Points in Currency|forward contract]] changes over time and at time $t>0$ the value of the [[Forward Points in Currency|forward contract]] is: $V_{t}=\left[F_{t}-F_{0}\right]\bar{e}^{-r(T-t)}=S_{t}-F_{0}e^{-r(T-t)}$ . Hence $V_{t}$ varies with the spot price $S_{t}$ , interest rate and [[Hedging Strategies with Forwards|time to maturity]].   
• On the other hand, the value of $a$ [[Futures Not Subject to Cash-And-Carry|futures]] contract at the end of each day is zero, since the contract is marked-to-market and the margin account is credited or debited daily.  

# EXERCISES  

# Question 1  

How do [[Mathematics of the Financial Markets|futures contracts]] provide ‘[[Lecture 6-Leverage, Tail Risk, Volatility Products|leverage]]’?  

# Question 2  

For a [[Futures Not Subject to Cash-And-Carry|futures]] contract on a (non-dividend paying) stock, carefully explain how you can make an [[Arbitrage Pricing of Derivatives|arbitrage]] proft if the quoted [[Futures Price and the Quality Option Before E|futures price]] $F_{q}$ is less than the ‘fair’ (or ‘synthetic’) [[Futures Price and the Quality Option Before E|futures price]].  

# Question 3  

For a [[Futures Not Subject to Cash-And-Carry|futures]] contract on a dividend paying stock, with a single dividend payment $D$ before maturity of the [[Futures Not Subject to Cash-And-Carry|futures]], carefully explain how you can make an [[Arbitrage Pricing of Derivatives|arbitrage]] proft if the quoted [[Futures Price and the Quality Option Before E|futures price]] $F_{q}$ is above the ‘fair’ (or ‘no-[[Arbitrage Pricing of Derivatives|arbitrage]]’ or ‘synthetic’) [[Futures Price and the Quality Option Before E|futures price]].  

# Question 4  

What is the ‘convenience yield’ and how does it complicate [[Arbitrage Pricing of Derivatives|arbitrage]] between the spot and [[Contango And Backwardation In Arbitrage-Free Futures-Markets|futures markets]]?  

# Question 5  

The [[Chapter 16 - Black–Scholes Model|stock price]] is currently at $S=400$ , and the quoted [[Futures Price and the Quality Option Before E|futures price]] on a $T=4$ -month contract is $F_{q}=405$ , $r=10\%$ p.a. and the dividend yield is $4\%$ p.a. (both continuously compounded). How could you make an [[Arbitrage Pricing of Derivatives|arbitrage]] proft?  

# Question 6  

The spot price of an asset is $S_{0}$ , the [[Futures Price and the Quality Option Before E|futures price]] today for delivery or settlement at period $T$ in the future is $F_{0}$ , the [[Black Scholes Derivation|risk-free rate]] over the period from $t=0$ to $t=T$ is $r$ (simple rate). Explain the relationship that must hold between $S_{0},F_{0}$ , and $r$ .  

Now suppose the asset pays a known income stream $c$ over the period, the present value of which is $P V(C)$ . Explain the relationship that must hold between $S_{0},F_{0},P V(C)$ and $r$ .  
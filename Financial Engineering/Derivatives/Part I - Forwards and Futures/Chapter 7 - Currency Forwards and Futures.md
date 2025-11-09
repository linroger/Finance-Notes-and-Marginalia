---
tags:
  - covered_interest_arbitrage
  - currency_futures
  - fx_forwards
  - fx_hedging
  - spot_exchange_rate
aliases:
  - Currency Forwards
  - Currency Futures
  - FX Futures
  - FX-forward
key_concepts:
  - Covered interest arbitrage
  - Currency speculation
  - FX futures contracts
  - Hedging future payments
  - Spot exchange rate
---
# Currency Forwards and Futures  

# Aims  

• To outline contract specifcations, [settlement procedures](Chapter%205%20-%20Index%20Futures.md) and [price quotes](../Part%20III%20-%20Fixed%20Income%20Futures%20Contracts/Chapter%2011%20-%20Interest%20Rate%20Futures.md) for selected foreign exchange (FX) [futures contracts](../../Mathematics%20of%20the%20Financial%20Markets.md) – also called ‘[currency futures](.md)’. • To price a [FX-forward](.md) contract by creating a [replication portfolio](../Part%20V%20-%20Options%20Pricing/Chapter%2022%20-%20BOPM:%20Implementation.md) using two money market [interest rates](../../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%202/Interest%20Rate%20Quotations.md) and the [spot exchange rate](../../../Financial%20Instruments/Review%20Session%20Notes/Arbitrage%20Opportunity%20Accounting.md). This is ‘[covered interest arbitrage](../../../Financial%20Instruments/Lecture%20Notes-%20Financial%20Instruments/Teaching%20Note%201-%20Forward%20Rates%20Agreement/Forwards%20and%20Futures%20Notes.md)’. • To show how FX-[futures](../../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%203%20-%20Futures%20Markets/Futures%20Not%20Subject%20to%20Cash-And-Carry.md) can be used to hedge future payments and receipts in foreign [currency](../../../Financial%20Instruments/Lecture%20Notes-%20Financial%20Instruments/Teaching%20Note%201-%20Forward%20Rates%20Agreement/Forwards%20and%20Futures%20Notes.md). • To demonstrate how both FX-[forwards and futures](../../../Financial%20Instruments/Financial%20Derivatives%20and%20Quantitative%20Methods/Forward%20and%20Futures%20Contracts.md) can be used for speculation. • To compare the [pricing](../../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%207/Arbitrage%20Pricing%20of%20Derivatives.md) of [currency futures](.md) with those for forward contracts.  

Two major types of ‘deal’ on the foreign exchange (FX) market involve the spot-rate and the forward-rate. We assume, the [spot rate](../../../International%20Finance/The%20Foreign%20Exchange%20Market%20Annotations.md) is the exchange rate quoted for immediate delivery of the [currency](../../../Financial%20Instruments/Lecture%20Notes-%20Financial%20Instruments/Teaching%20Note%201-%20Forward%20Rates%20Agreement/Forwards%20and%20Futures%20Notes.md) to the buyer (actually, delivery is 2 working days later). The second type of deal involves the [forward rate](../../../Clippings/Forward%20Points%20in%20Currency.md), which is the price agreed today, at which the buyer will take delivery of the [currency](../../../Financial%20Instruments/Lecture%20Notes-%20Financial%20Instruments/Teaching%20Note%201-%20Forward%20Rates%20Agreement/Forwards%20and%20Futures%20Notes.md) at some future date. [Currency forwards](../../../Financial%20Instruments/Lecture%20Notes-%20Financial%20Instruments/Teaching%20Note%201-%20Forward%20Rates%20Agreement/Forward%20Contracts%20on%20Exchange%20Rates.md) and [futures](../../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%203%20-%20Futures%20Markets/Futures%20Not%20Subject%20to%20Cash-And-Carry.md) are very similar analytically, even though in practice the contractual arrangements difer.  

Both, an [FX-forward](.md) and an FX-[futures](../../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%203%20-%20Futures%20Markets/Futures%20Not%20Subject%20to%20Cash-And-Carry.md) contract is an obligation to trade one [currency](../../../Financial%20Instruments/Lecture%20Notes-%20Financial%20Instruments/Teaching%20Note%201-%20Forward%20Rates%20Agreement/Forwards%20and%20Futures%20Notes.md) for another at a pre-specifed exchange rate on a specifc future (delivery) date. The dealing costs in both type of contract are very small. Why then do we need both types of contract? The reasons are slight diferences between the two types of contract.  

A [currency](../../../Financial%20Instruments/Lecture%20Notes-%20Financial%20Instruments/Teaching%20Note%201-%20Forward%20Rates%20Agreement/Forwards%20and%20Futures%20Notes.md) forward can be designed to exactly ft the client’s requirements as to the principal (e.g. sterling) amount in the trade, the exact delivery date and which currencies are involved. It is an over the counter (OTC) transaction. Most forward deals, on a wide range of currencies, are channelled through London, New York and Tokyo with Hong Kong, Singapore and increasingly Shanghai being infuential in the Far East. This OTC market is very e\$cient with low transactions cost.  

Deals are negotiated between large multinational banks (e.g. Barclays, HSBC, Citigroup, [Morgan Stanley](../../../Financial%20Markets%20and%20Institutions/III.%20Liquidity%20of%20Assets/Class%208-%20Markets,%20Meltdowns,%20and%20Arbitrage/Lessons%20From%20The%20Crisis.md), [JPMorgan](../../Basis%20Trade%20Explainer.md)-Chase, Goldman Sachs) for delivery of one [currency](../../../Financial%20Instruments/Lecture%20Notes-%20Financial%20Instruments/Teaching%20Note%201-%20Forward%20Rates%20Agreement/Forwards%20and%20Futures%20Notes.md) (e.g. Swiss francs) usually against the US dollar (the vehicle [currency](../../../Financial%20Instruments/Lecture%20Notes-%20Financial%20Instruments/Teaching%20Note%201-%20Forward%20Rates%20Agreement/Forwards%20and%20Futures%20Notes.md)), at a specifc date in the future. It is also possible to negotiate so-called forward cross-rate deals (which do not involve the US dollar), for example, receipt of Swiss francs and payment of euros. For most major currencies, the most actively traded contracts are for maturities between 1 to 6 months and in exceptional circumstances, 3 to 5 years ahead. Use of the [forward market](../../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%2015/Tba%20and%20Specified%20Pools%20Markets.md) eliminates any exchange risk from future changes in spot-FX rates – assuming no [credit default risk](../../../Credit%20Markets/Credit%20Markets%20Session%205.md) from the counterparties in the OTC forward trade. This is because the [forward rate](../../../Clippings/Forward%20Points%20in%20Currency.md) is agreed today, even though the cash transaction takes place in (say) 1 year’s time.  

In contrast, a [currency futures](.md) contract is an exchange traded instrument on a limited number of currencies. The contract sizes are fxed (e.g. delivery of SFr 125,000) as are the set of delivery dates. With a [forward contract](../../../Clippings/Forward%20Points%20in%20Currency.md), delivery usually takes place, whereas with a [futures](../../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%203%20-%20Futures%20Markets/Futures%20Not%20Subject%20to%20Cash-And-Carry.md) contract you do not necessarily have to take delivery of the [currency](../../../Financial%20Instruments/Lecture%20Notes-%20Financial%20Instruments/Teaching%20Note%201-%20Forward%20Rates%20Agreement/Forwards%20and%20Futures%20Notes.md) because you can easily close out your position before maturity. If you are long a [currency futures](.md) and you decide not to take delivery, then you can close out your position by selling the [futures](../../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%203%20-%20Futures%20Markets/Futures%20Not%20Subject%20to%20Cash-And-Carry.md) (on the same [currency](../../../Financial%20Instruments/Lecture%20Notes-%20Financial%20Instruments/Teaching%20Note%201-%20Forward%20Rates%20Agreement/Forwards%20and%20Futures%20Notes.md) and with the same maturity date). The FX-[futures](../../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%203%20-%20Futures%20Markets/Futures%20Not%20Subject%20to%20Cash-And-Carry.md) contract is marked-to-market daily (which involves margin payments) and therefore has virtually zero [credit risk](../../../Course%20Notes/Quantitative%20Trading%20Strategies%20Lecture%20Notes.md), whereas the [forward contract](../../../Clippings/Forward%20Points%20in%20Currency.md) involves counterparty [credit risk](../../../Course%20Notes/Quantitative%20Trading%20Strategies%20Lecture%20Notes.md).  

[Currency forwards](../../../Financial%20Instruments/Lecture%20Notes-%20Financial%20Instruments/Teaching%20Note%201-%20Forward%20Rates%20Agreement/Forward%20Contracts%20on%20Exchange%20Rates.md) and [futures](../../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%203%20-%20Futures%20Markets/Futures%20Not%20Subject%20to%20Cash-And-Carry.md) are used to hedge future cash fows in foreign [currency](../../../Financial%20Instruments/Lecture%20Notes-%20Financial%20Instruments/Teaching%20Note%201-%20Forward%20Rates%20Agreement/Forwards%20and%20Futures%20Notes.md) – for example, by exporters and importers. Similarly, they are used to hedge future cash fows from purchases or sales of capital assets such as foreign bonds and stocks as well as future interest cash fows from foreign bank deposits or loans. They also provide [leverage](../../../Advanced%20Investments/Lecture%206-Leverage,%20Tail%20Risk,%20Volatility%20Products.md) in speculative FX-transactions, which are gambles on the future path of exchange rates.  

# 7.1 FX-FUTURES CONTRACTS  

# 7.1.1 Contract Specification  

There are a large number of [currency futures](.md) traded on diferent exchanges, the major one being the [International Money Market](../../../International%20Finance/Characteristics%20of%20the%20Eurodollar%20Market.md) (IMM) division of the Chicago Mercantile Exchange (CME). For example, on CME the following currencies are traded against the US dollar: pound sterling, euro, yen, Swiss franc, Canadian dollar, Australian dollar, Mexican peso as well as other currencies. Other notable centres trading FX-[futures](../../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%203%20-%20Futures%20Markets/Futures%20Not%20Subject%20to%20Cash-And-Carry.md) are the Singapore International Money Exchange (SIMEX) and the Sydney [Futures](../../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%203%20-%20Futures%20Markets/Futures%20Not%20Subject%20to%20Cash-And-Carry.md) Exchange (SFE). On CME there are also [futures](../../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%203%20-%20Futures%20Markets/Futures%20Not%20Subject%20to%20Cash-And-Carry.md) on the major cross rates.  

The most actively traded [futures contracts](../../Mathematics%20of%20the%20Financial%20Markets.md) traded on the CME are in the euro, Canadian dollar, Japanese yen, Swiss franc and sterling. Details of some of these contracts are given in Table 7.1. On the CME there is 24-hour electronic [futures trading](../../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%203%20-%20Futures%20Markets/Futures%20Mechanics.md) using the Globex system and  

TABLE 7.1 Contract specifcations IMM [currency futures](.md) (CME)   


<html><body><table><tr><td>[Currency](../../../Financial%20Instruments/Lecture%20Notes-%20Financial%20Instruments/Teaching%20Note%201-%20Forward%20Rates%20Agreement/Forwards%20and%20Futures%20Notes.md)</td><td>Contract size</td><td>Tick size [value]</td></tr><tr><td>Pound sterling</td><td>62,500</td><td>0.02 cent per [$12.50]</td></tr><tr><td>Swiss franc</td><td>SFr125,000</td><td>cent per SFr [$125]</td></tr><tr><td>Japaneseyen</td><td>￥12,500,000</td><td>cent per 100 ? [$12.50]</td></tr><tr><td>Canadian dollar</td><td>C$100,000</td><td>cent per C$ [$100]</td></tr><tr><td>Euro</td><td>125,000</td><td>cent per [$12.50]</td></tr></table></body></html>  

Note: The delivery months for all contracts is January, March, April, June, July, September, October and December and the delivery date is the 3rd Wednesday of the contract months. Last trading day is the second business day before delivery. Initial and maintenance margin are sometimes altered by the exchange. Margins are smaller if the transaction involves either a speculative spread trade or for a hedges position. There are no daily price limits.  

Euro [futures](../../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%203%20-%20Futures%20Markets/Futures%20Not%20Subject%20to%20Cash-And-Carry.md) can be traded at any time if one is willing to trade on diferent exchanges. Take, for example, the Euro [futures](../../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%203%20-%20Futures%20Markets/Futures%20Not%20Subject%20to%20Cash-And-Carry.md) contract on the CME (see Table 7.1). If you are long one contract then the convention is:  

Long Euro [FX Futures](.md) $\Rightarrow$ Receive € and pay out deliver US dollars  

Suppose Ms USA on 1 March wants to receive %125,000 in September. Today she purchases one Euro September-[futures](../../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%203%20-%20Futures%20Markets/Futures%20Not%20Subject%20to%20Cash-And-Carry.md) contract at $F_{0}=1.0400(\S/\epsilon)$ . At maturity (in September) she receives %125,000 from the [futures](../../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%203%20-%20Futures%20Markets/Futures%20Not%20Subject%20to%20Cash-And-Carry.md) contract and pays out $\$130,000$ . Also, the contract is marked-to-market, daily. So for example, on 2 March, if $F_{1}=1.0450(\Phi/\mathrm{\epsilon})$ then Ms USA has gained, since (forward) euros have appreciated and her margin account will be credited with $\$625$ (i.e. $50\mathrm{ticks}\times\$12.50$ per tick).  

# 7.1.2 Settlement  

Although most contracts are closed out before maturity, it is useful to consider what happens on the maturity date of the September-[futures](../../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%203%20-%20Futures%20Markets/Futures%20Not%20Subject%20to%20Cash-And-Carry.md). Assume the September [spot rate](../../../International%20Finance/The%20Foreign%20Exchange%20Market%20Annotations.md) ${{S}_{T}}=$ $1.05(\S/\upepsilon)$ – [arbitrage](../../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%207/Arbitrage%20Pricing%20of%20Derivatives.md) ensures this will also be the quoted [futures price](../../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%2011/Futures%20Price%20and%20the%20Quality%20Option%20Before%20E.md) $F_{T}=1.05(\Phi/\Theta)$ .  

TABLE 7.2 Settlement of sterling [currency futures](.md)  

1. Contract requirements: September settlement Initial September-[futures price](../../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%2011/Futures%20Price%20and%20the%20Quality%20Option%20Before%20E.md) $F_{0}=1.04(\Phi/\epsilon)$ Ms USA notionally receives €125,000 and pays out $\$130,000$  

# 2. Settlement convention at maturity  

Currencies are delivered at the [spot rate](../../../International%20Finance/The%20Foreign%20Exchange%20Market%20Annotations.md) $S_{\tau}=1.05(\mathbb{\S}/\in)$ , prevailing on the last trading day, at maturity of the [futures](../../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%203%20-%20Futures%20Markets/Futures%20Not%20Subject%20to%20Cash-And-Carry.md) contract.   
Ms USA’s margin account has been credited by:  

# Gain on futures:  
$$
\$1250=100
$$  

Net cost to Ms USA $\mathbf{\tau}=\mathbf{\tau}$ -Spot market payment–Gain [futures](../../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%203%20-%20Futures%20Markets/Futures%20Not%20Subject%20to%20Cash-And-Carry.md) $=[S_{\tau}-(F_{\tau}-F_{0})]\in125,000=F_{0}\in125,000=\S130,000$  

Ms USA acquires %125,000 in the spot-[FX market](../../../International%20Finance/Foreign%20Exchange%20Markets%20and%20Exchange%20Rate%20Determination.md) and pays out $\$131,250$ based on $S_{\mathrm{T}}=$ $1.05(\S/\epsilon)$ (Table 7.2). However, this is ofset by profts from her (futures) margin account of $\$1,250$ . The net efect of purchasing euros in the spot-[FX market](../../../International%20Finance/Foreign%20Exchange%20Markets%20and%20Exchange%20Rate%20Determination.md) and the proft from closing out the long [futures](../../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%203%20-%20Futures%20Markets/Futures%20Not%20Subject%20to%20Cash-And-Carry.md) contract is $\$130,000$ . This implies that she has locked in a rate of $F_{0}=1.04(\S/\mathsf{\epsilon})=(\S130,000/\mathsf{\epsilon}125,000)$ . (This calculation ignores any interest earned on the margin account over the life of the contract).  

# 7.1.3 Quotes  

[Currency futures](.md) are quoted as ‘USD per unit of foreign [currency](../../../Financial%20Instruments/Lecture%20Notes-%20Financial%20Instruments/Teaching%20Note%201-%20Forward%20Rates%20Agreement/Forwards%20and%20Futures%20Notes.md)’. For example on 27 July suppose the September-Euro [futures](../../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%203%20-%20Futures%20Markets/Futures%20Not%20Subject%20to%20Cash-And-Carry.md) is quoted at $F_{0}^{S e p t}=0.9416(\bar{\Phi/}\bar{\epsilon})$ and the December [futures](../../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%203%20-%20Futures%20Markets/Futures%20Not%20Subject%20to%20Cash-And-Carry.md) quote is $F_{0}^{D e c}=0.9498(\S/\epsilon)$ . Given a current [spot rate](../../../International%20Finance/The%20Foreign%20Exchange%20Market%20Annotations.md) of $S_{0}=0.9420(\S/\epsilon)$ then with $F_{0}^{S e p t}=$ $0.9416(\mathbb{S}/\epsilon)$ this implies that you will receive 4 points/ticks less US dollars per euro in September than from the spot-FX rate on 27 July. Hence September-Euro [futures](../../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%203%20-%20Futures%20Markets/Futures%20Not%20Subject%20to%20Cash-And-Carry.md) are ‘at a discount’:  

September Euro [FX Futures](.md) at a discount $\Rightarrow$ less US dollars per euro in the [futures](../../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%203%20-%20Futures%20Markets/Futures%20Not%20Subject%20to%20Cash-And-Carry.md) market than in the spot market $F_{0}^{S e p t}<S_{0}$  

In contrast, if the quoted [futures price](../../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%2011/Futures%20Price%20and%20the%20Quality%20Option%20Before%20E.md) $F_{0}^{S e p t}>S_{0}$ then euros are selling at a forward premium relative to the current [spot rate](../../../International%20Finance/The%20Foreign%20Exchange%20Market%20Annotations.md):  

September Euro [FX Futures](.md) at a premium $\Rightarrow$ more US dollars per euro in the [futures](../../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%203%20-%20Futures%20Markets/Futures%20Not%20Subject%20to%20Cash-And-Carry.md) market than in the spot market $F_{0}^{S e p t}>S_{0}$  

# 7.2 PRICING FX-FORWARD CONTRACTS  

[Pricing](../../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%207/Arbitrage%20Pricing%20of%20Derivatives.md) an [FX-forward](.md) contract involves a relationship between the [forward rate](../../../Clippings/Forward%20Points%20in%20Currency.md) $F$ and three other variables, the spot FX-rate and the money market [interest rates](../../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%202/Interest%20Rate%20Quotations.md) in the two countries – it is known as [covered interest parity](../../../Financial%20Instruments/Lecture%20Notes-%20Financial%20Instruments/Teaching%20Note%201-%20Forward%20Rates%20Agreement/Interest%20Rates,%20Carry%20Trades,%20and%20Exchange%20Rate%20Movements.md) (CIP). The no-[arbitrage](../../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%207/Arbitrage%20Pricing%20of%20Derivatives.md) [forward rate](../../../Clippings/Forward%20Points%20in%20Currency.md) (using [simple interest](../../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%202/Interest%20Rate%20Quotations.md)) is:  
$$
F=S\frac{(1+r_{d}T)}{(1+r_{f}T)}
$$  
$s$ and $F$ are measured as ‘domestic per unit of foreign [currency](../../../Financial%20Instruments/Lecture%20Notes-%20Financial%20Instruments/Teaching%20Note%201-%20Forward%20Rates%20Agreement/Forwards%20and%20Futures%20Notes.md)’, $r_{d}=$ domestic interest rate, $r_{f}=$ foreign interest rate, $T=$ [time to maturity](../../../Financial%20Instruments/Lecture%20Notes-%20Financial%20Instruments/Teaching%20Note%201-%20Forward%20Rates%20Agreement/Hedging%20Strategies%20with%20Forwards.md) (expressed in years or fraction of a year) and we assume the [day-count](../../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%202%20-%20Spot%20Markets/Intra-Year%20Compounding%20and%20Day-Count.md) convention is the same in both countries. The quoted [forward rate](../../../Clippings/Forward%20Points%20in%20Currency.md) given by CIP ensures that no risk-free [arbitrage](../../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%207/Arbitrage%20Pricing%20of%20Derivatives.md) profts can be made by transacting between the spot [currency](../../../Financial%20Instruments/Lecture%20Notes-%20Financial%20Instruments/Teaching%20Note%201-%20Forward%20Rates%20Agreement/Forwards%20and%20Futures%20Notes.md), the two money markets and the [forward market](../../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%2015/Tba%20and%20Specified%20Pools%20Markets.md).  

The CIP equation is derived as follows. Assume that a UK frm BritArb has $£ A=£100$ which it can invest in the UK or the USA for 1 year. Assume transactions have no credit/[default risk](../../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%207%20-%20Default%20Risk%20and%20Credit%20Derivatives/Default%20Risk%20and%20Credit%20Derivatives%20183.md). For BritArb to be indiferent as to where the money is invested, the [risk-free return](../../../Financial%20Markets/Financial%20Asset%20Pricing%20Theory%20Overview/Chapter%204%20-%20State%20Prices/A%20Preview%20of%20Alternative%20Formulations.md) from investing in the UK must equal the [risk-free return](../../../Financial%20Markets/Financial%20Asset%20Pricing%20Theory%20Overview/Chapter%204%20-%20State%20Prices/A%20Preview%20of%20Alternative%20Formulations.md) in sterling from investing in the USA. Assume the quoted [interest rates](../../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%202/Interest%20Rate%20Quotations.md) in the ‘domestic’ (sterling) money market, the ‘foreign’ (US) money market and the exchange rates are:  
$$
\begin{array}{r l}{r_{d}=0.11\left(11\%\right)}&{\mathrm{(simple~rate)}}\\ {r_{f}=0.10\left(10\%\right)}&{\mathrm{(simple~rate)}}\\ {S=0.6667\left(£/\mathfrak{S}\right)}&{\mathrm{(equivalent~to~1.5~\mathfrak{S/E})}}\\ {F=0.6727\left(£/\mathfrak{S}\right)}&{\mathrm{(equivalent~to~1.4865~\mathfrak{S/E})}}\\ {T=1\mathrm{,investment~horizon}}&{\mathrm{(years~or~fraction~of~a~\in~\mathfrak{S}_{\varepsilon}~})}\end{array}
$$  

Note that the [forward rate](../../../Clippings/Forward%20Points%20in%20Currency.md) $F$ and the [spot rate](../../../International%20Finance/The%20Foreign%20Exchange%20Market%20Annotations.md) $s$ are measured as ‘domestic per unit of foreign [currency](../../../Financial%20Instruments/Lecture%20Notes-%20Financial%20Instruments/Teaching%20Note%201-%20Forward%20Rates%20Agreement/Forwards%20and%20Futures%20Notes.md)’, here £s per $\$1$ (GBP per USD). We show that the above fgures give equal returns to investing in either the UK or the US – so $F=0.6727$ GBP/USD is the ‘correct’ no-[arbitrage](../../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%207/Arbitrage%20Pricing%20of%20Derivatives.md) [forward rate](../../../Clippings/Forward%20Points%20in%20Currency.md).  

# Strategy-1: BritArb invests in UK  

In 1 year receive (terminal value): $T V_{U K}=£ A(1+r_{d}T)=£100(1.11)=£111$  

# Strategy-2: BritArb invests in US  

(a) Today convert £100 to $\$150($ at spot-FX rate and invest in US deposit account (b) Dollar receipts at end-year are: $\S150(1.10)=(A/S)(1+r_{f}T)=\S165$  

(c) Enter into a [forward contract](../../../Clippings/Forward%20Points%20in%20Currency.md) today at $F=0.6727\left(\mathrm{{f/\mathfrak{s}}}\right)$ to sell $\$165$ for delivery of sterling in 1 year’s time. Sterling receipts in one year are:  
$$
T V_{U S}=\S165F=£[(A/S)(1+r_{f}T)]F=£111
$$  

All of the above transactions (a)–(c) are undertaken at known ‘prices’, hence there is no price risk. Since both [investment](../../../Advanced%20Investments/An%20Asset%20Allocation%20Primer.md) strategies are risk-free, [arbitrage](../../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%207/Arbitrage%20Pricing%20of%20Derivatives.md) will ensure that they give the same terminal value, $T V_{U K}=T V_{U S}$ , hence:  
$$
A(1+r_{d}T)=[(A/S)(1+r_{f}T)]F
$$  

Rearranging, the ‘fair’, ‘correct’ or ‘no-[arbitrage](../../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%207/Arbitrage%20Pricing%20of%20Derivatives.md)’ [forward rate](../../../Clippings/Forward%20Points%20in%20Currency.md) is:  
$$
F=S(1+r_{d}T)/(1+r_{f}T)
$$  

or,  
$$
(F-S)/S=(r_{d}-r_{f})T/(1+r_{f}T)
$$  

The above CIP formulas are exact, but if $r_{f}T<<1$ then $(1+r_{f}T)\approx1$ , hence:  

Forward premium/discount $\approx$ interest rate diferential1  
$$
(F-S)/S\approx(r_{d}-r_{f})T
$$  

# 7.2.1 Forward Points  

In the FX-market, outright forward rates are not quoted, but instead the convention is that the diference between the [forward rate](../../../Clippings/Forward%20Points%20in%20Currency.md) and [spot rate](../../../International%20Finance/The%20Foreign%20Exchange%20Market%20Annotations.md) $F-S$ , or the forward points or forward margins are quoted, where:  
$$
=0.6727-6667=0.0060\:(+60\:\mathrm{points})
$$  

Given forward points of $+60$ on a dealer’s screen, she would quote:  
$$
=0.6667+0.0060=0.6727\left(\mathrm{{\p}}\right/\mathrm{{\Phi}}\right)
$$  

1Note that if [interest rates](../../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%202/Interest%20Rate%20Quotations.md) are continuously compounded then the equivalent to Equation (7.1) is $F=S e^{(r_{d}-r_{f})T}$ or $\ln{\cal F}=\ln S+(r_{d}-r_{f})T$ , respectively.  

The forward points would usually be quoted on FX-screens for 1, 2, 3, 6, and 12 months and the value dates for the forward contracts would coincide with maturity dates for [Eurocurrency](../../../International%20Finance/The%20Eurocurrency%20and%20Eurobond%20Markets%20Annotations.md) deposits and loans. Given that CIP holds, the quoted forward points $F-S$ (approximately) equals the interest diferential (multiplied by the [spot rate](../../../International%20Finance/The%20Foreign%20Exchange%20Market%20Annotations.md)). For example, for $r_{d}=11\%$ and $r_{f}=10\%$ , then if you transfer cash from the foreign to the domestic [investment](../../../Advanced%20Investments/An%20Asset%20Allocation%20Primer.md) you will earn $1\%$ more interest. The only way you do not earn a risk-free proft is if the forward domestic [currency](../../../Financial%20Instruments/Lecture%20Notes-%20Financial%20Instruments/Teaching%20Note%201-%20Forward%20Rates%20Agreement/Forwards%20and%20Futures%20Notes.md) you receive after 1 year is $1\%$ less than the spot domestic [currency](../../../Financial%20Instruments/Lecture%20Notes-%20Financial%20Instruments/Teaching%20Note%201-%20Forward%20Rates%20Agreement/Forwards%20and%20Futures%20Notes.md) you gave up at $t=0$ , that is, if $(F-S)/S$ equals $-1\%$ .  

As CIP holds at all times, then the ‘forward points’ could be positive or negative, depending on whether $r_{d}$ is greater or less than $r_{f}$ . A further practical complication is that the [forward rate](../../../Clippings/Forward%20Points%20in%20Currency.md) calculated from the money market rates will have a bid–ask spread depending on which [currency](../../../Financial%20Instruments/Lecture%20Notes-%20Financial%20Instruments/Teaching%20Note%201-%20Forward%20Rates%20Agreement/Forwards%20and%20Futures%20Notes.md) is being borrowed or placed on deposit in the money markets – we ignore this problem here. Two other rearrangements of the CIP condition are worth mentioning, which are:  
$$
\begin{array}{l}{F=S(1+\mathrm{CC})\mathrm{~where~}\mathrm{CC}=(r_{d}-r_{f})/(1+r_{f})}\\ {F=S+\chi\mathrm{~where~}\chi=S(r_{d}-r_{f})/(1+r_{f})}\end{array}
$$  

CC is known as the percentage cost of forward cover and $\chi$ is the dollar cost of forward cover. The cost of forward cover depends on the interest diferential between the two countries. It is easy to check that our data are consistent with the (exact) algebraic CIP condition:  
$$
\begin{array}{r l}&{\mathrm{Interest\:differential}=(r_{d}-r_{f})/(1+r_{f})=0.0091(0.91\%)}\\ &{\mathrm{Forward\:Discount}=(F-S)/S=0.0091(0.91\%)}\end{array}
$$  

One further ‘trick’ to note is that the CIP formula looks slightly diferent if $s$ and $F$ are measured as ‘foreign per unit of domestic [currency](../../../Financial%20Instruments/Lecture%20Notes-%20Financial%20Instruments/Teaching%20Note%201-%20Forward%20Rates%20Agreement/Forwards%20and%20Futures%20Notes.md)’. However, the following ‘rule of thumb’ always holds:  

If S and $F$ are measured as ‘[currency](../../../Financial%20Instruments/Lecture%20Notes-%20Financial%20Instruments/Teaching%20Note%201-%20Forward%20Rates%20Agreement/Forwards%20and%20Futures%20Notes.md) $X$ per unit of [currency](../../../Financial%20Instruments/Lecture%20Notes-%20Financial%20Instruments/Teaching%20Note%201-%20Forward%20Rates%20Agreement/Forwards%20and%20Futures%20Notes.md) $\boldsymbol{Y}$ then in the [forward rate](../../../Clippings/Forward%20Points%20in%20Currency.md) equation, [interest rates](../../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%202/Interest%20Rate%20Quotations.md) are $r_{X}$ in the numerator and $r_{Y}$ in the denominator  

For example, if $s$ and $F$ are measured as Swiss francs (SFr) per USD then the CIP condition is:  
$$
F/S=(1+r_{S F}T)/(1+r_{U S}T)
$$  

where $r_{S F}$ and $r_{U S}$ are the Swiss franc and US dollar [interest rates](../../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%202/Interest%20Rate%20Quotations.md), respectively. In practice, CIP must refect the [day-count conventions](../../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%201/Day-Count%20Conventions.md) used for domestic and foreign [interest rates](../../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%202/Interest%20Rate%20Quotations.md). For example, if the forward [currency](../../../Financial%20Instruments/Lecture%20Notes-%20Financial%20Instruments/Teaching%20Note%201-%20Forward%20Rates%20Agreement/Forwards%20and%20Futures%20Notes.md) is for delivery in 90 days and the Swiss interest rate convention is ‘actual/ $365^{\prime}$ and the US convention is ‘actual/ $360^{\circ}$ then the 3-month [forward rate](../../../Clippings/Forward%20Points%20in%20Currency.md) (SFr per USD) would be calculated as:  
$$
F/S=[1+r_{S F}(90/365)]/\left[(1+r_{U S}(90/360))\right]
$$  

# 7.2.2 Arbitrage Profits  

To show how [arbitrage](../../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%207/Arbitrage%20Pricing%20of%20Derivatives.md) profts can be made if the actual forward quote $F_{q}$ by bank-M does not equal the fair (no-[arbitrage](../../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%207/Arbitrage%20Pricing%20of%20Derivatives.md)) [futures price](../../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%2011/Futures%20Price%20and%20the%20Quality%20Option%20Before%20E.md) given by the CIP equation (7.1), suppose an investor BritArb is faced with the following data.  

• One-year forward quote (from bank M): $F_{q}=1.4$ (USD/GBP) • $r_{U K}=11\%$ p.a., $r_{U S}=10\%$ p.a., $S_{0}=1.5136$ (USD∕GBP) • [Fair forward price](Chapter%203%20-%20Forward%20and%20Futures%20Prices.md) $F_{0}=S_{0}(1+r_{U S}T)/(1+r_{U K}T)=1.5$ (USD/GBP)  

BritArb, can receive sterling in 1 year from bank-M at the [forward rate](../../../Clippings/Forward%20Points%20in%20Currency.md) $F_{q}$ and will have to pay out $\$1.40$ per £1 in 1 year’s time. Since $F_{0}>F_{q}$ then by using the spot rate and the money markets in the two countries, BritArb can borrow £1 today, buy $\$1$ at a rate $S_{0}$ , invest in the US money market and will receive $\$1.50$ per £1. The details are as follows.  

# Arbitrage strategy for BritArb:  

• Enter a [forward contract](../../../Clippings/Forward%20Points%20in%20Currency.md) at $F_{q}$ to receive £100 at $t=1$ and pay out $\$140$ to bank-M   
• Borrow £90.09 in the UK money market at $t=0$ (i.e. owe £100 at $t=1$ )   
• Convert £90.09 at $S_{0}=1.5136(\S/£)$ and lend $\$136.36$ in the US money market   
• At $t=1$ , BritArb receives $\$136.36\left(1.10\right)=\$150$   
• Risk-free proft for BritArb $=\$150–8140=\$10$  

Given this risk-free proft opportunity, many arbitrageurs implement this strategy, but this would result in:  

• Borrowing in the sterling money market which raises $r_{U K}$ while lending dollars causes downward pressure on $r_{U S}$   
• Buying dollars spot so the dollar appreciates (i.e. $s$ falls)   
• The above implies that $S_{0}(1+r_{U S}T)/(1+r_{U K}T)$ falls   
• Selling dollars forward and buying sterling forward (with bank-M) puts upward pressure on the quoted [forward rate](../../../Clippings/Forward%20Points%20in%20Currency.md) so $F_{q}$ increases).  

The above scenario tends to raise $F_{q}$ and lower $S_{0}(1+r_{U S}T)/(1+r_{U K}T)$ , hence bringing the quoted [forward price](../../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%2011/Forward%20Contracts%20and%20Forward%20Prices.md) into line with the fair [futures price](../../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%2011/Futures%20Price%20and%20the%20Quality%20Option%20Before%20E.md) $F=S(1+r_{U S}T)/(1+r_{U K}T)$ . This happens very quickly because [arbitrage](../../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%207/Arbitrage%20Pricing%20of%20Derivatives.md) transactions are risk-free, so CIP will hold at all times.  

# 7.3 PRICING FX-FUTURES CONTRACTS  

We can price FX-[futures contracts](../../Mathematics%20of%20the%20Financial%20Markets.md) using the same formulas we derived for [pricing](../../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%207/Arbitrage%20Pricing%20of%20Derivatives.md) FX forward contracts. Hence, the no [arbitrage](../../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%207/Arbitrage%20Pricing%20of%20Derivatives.md) FX-[futures price](../../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%2011/Futures%20Price%20and%20the%20Quality%20Option%20Before%20E.md) $F$ (domestic per unit of foreign [currency](../../../Financial%20Instruments/Lecture%20Notes-%20Financial%20Instruments/Teaching%20Note%201-%20Forward%20Rates%20Agreement/Forwards%20and%20Futures%20Notes.md))  

quoted today for delivery in $T$ years (or fraction of a year), using [simple interest](../../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%202/Interest%20Rate%20Quotations.md) $r^{s}$ , compound rates $r$ and continuously compounded rates $r^{c}$ are:  
$$
\begin{array}{c}{F=S\displaystyle\frac{(1+r_{d}^{s}T)}{(1+r_{f}^{s}T)},}\\ {F=S\displaystyle\frac{(1+r_{d})^{T}}{(1+r_{f})^{T}},}\end{array}
$$  
$$
F=S e^{(r_{d}^{c}-r_{f}^{c})T}
$$  

where we have assumed both countries have the same [day-count conventions](../../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%201/Day-Count%20Conventions.md) $T=$ days 360 . All three formulas give the same value for $F$ . In terms of the cost-of-carry approach to [futures pricing](Chapter%203%20-%20Forward%20and%20Futures%20Prices.md), the domestic interest rate $r_{d}$ is the borrowing cost (in GBP) and the income received is the [investment](../../../Advanced%20Investments/An%20Asset%20Allocation%20Primer.md) in the foreign interest rate $r_{f}$ . Brokerage fees mean that the above formula needs to take account of bid–ask spreads but the latter are very small for [currency futures](.md) (and [forwards](../../../Financial%20Markets/Financial%20Asset%20Pricing%20Theory%20Overview/Chapter%2012%20-%20Derivatives/Forwards%20and%20Futures.md)).  

# 7.3.1 Futures Prices  

A [forward contract](../../../Clippings/Forward%20Points%20in%20Currency.md) involves no funds changing hands until the maturity (delivery) date and hence the [forward rate](../../../Clippings/Forward%20Points%20in%20Currency.md) is ‘locked in’ at the outset of the contract. But, there is a subtle difference between the forward and the [futures](../../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%203%20-%20Futures%20Markets/Futures%20Not%20Subject%20to%20Cash-And-Carry.md) contract even when both are held to maturity. The [futures](../../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%203%20-%20Futures%20Markets/Futures%20Not%20Subject%20to%20Cash-And-Carry.md) contract is ‘marked-to-market’ each day so that payments will be made into the margin account (of the long) if $F$ increases and extra [margin calls](../../../Financial%20Markets%20and%20Institutions/III.%20Liquidity%20of%20Assets/Class%208-%20Markets,%20Meltdowns,%20and%20Arbitrage/Class%20Note%2013%20The%20LTCM%20Meltdown.md) may be made if $F$ falls. The interest rate applicable to these changes in margin payments is not known at the outset of the [futures](../../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%203%20-%20Futures%20Markets/Futures%20Not%20Subject%20to%20Cash-And-Carry.md) contract. However, for all practical purposes the interest cash fows from the margin account are not large enough to warrant analysing [currency futures](.md) prices any diferently from [currency forwards](../../../Financial%20Instruments/Lecture%20Notes-%20Financial%20Instruments/Teaching%20Note%201-%20Forward%20Rates%20Agreement/Forward%20Contracts%20on%20Exchange%20Rates.md).  
$F$ will be perfectly correlated with $s$ , providing the interest rate diferential $r_{d}-r_{f}$ remains constant over the hedge period. Hence the outcome from a hedged position will be more uncertain the greater the change in the interest diferential over the hedge period.  

# 7.4 HEDGING AND SPECULATION: FORWARDS  

# 7.4.1 Long Hedge  

Suppose a US importer, UncleSam, on 1 April knows that it will have to pay SFr 500,000 for imports from Switzerland, in 6 months’ time on 25 October. (UncleSam has a liability in Swiss francs and hence is ‘short’ Swiss francs.) UncleSam fears a strengthening of the Swiss franc against the US dollar. If the Swiss franc spot-FX rate appreciates (i.e. the dollar depreciates) over the next 6 months, UncleSam will have to pay out more dollars (than at the current [spot rate](../../../International%20Finance/The%20Foreign%20Exchange%20Market%20Annotations.md)).  

To hedge this position UncleSam takes a [long position](Chapter%204%20-%20Futures:%20Hedging%20and%20Speculation.md) in a Swiss franc [forward contract](../../../Clippings/Forward%20Points%20in%20Currency.md). If the quoted [forward rate](../../../Clippings/Forward%20Points%20in%20Currency.md) on 1 April for delivery on 25 October is $F_{0}=0.6620(\mathbb{S}/\mathrm{SFr})$ then he knows today that he will have to pay $\$331,000$ in 6 months’ time. UncleSam has removed uncertainty over the number of US dollars he will receive.  

The same principle would apply to a US investor who had Swiss franc liabilities (e.g. had issued bonds denominated in Swiss francs or who had a bank loan denominated in Swiss francs) and was facing future coupon (or bank interest) payments or redemption of the bonds (bank loan) in the future. If the Swiss franc appreciates, the US investor with liabilities in Swiss francs would have to pay out more US dollars. She could hedge by buying Swiss franc [forwards](../../../Financial%20Markets/Financial%20Asset%20Pricing%20Theory%20Overview/Chapter%2012%20-%20Derivatives/Forwards%20and%20Futures.md).  

Ex-post, whether it was better to hedge or not depends on the out-turn for the [spot rate](../../../International%20Finance/The%20Foreign%20Exchange%20Market%20Annotations.md) on 25 October relative to the quoted [forward rate](../../../Clippings/Forward%20Points%20in%20Currency.md) $F_{0}=0.6620(\mathbb{S}/\mathrm{SFr})$ . Suppose the Swiss franc depreciates (i.e. USD appreciates) so the [spot rate](../../../International%20Finance/The%20Foreign%20Exchange%20Market%20Annotations.md) in October is $S_{T}=0.6600(\mathbb{\mathbb{S}}/\mathrm{SFr})$ . With hindsight, UncleSam will wish that on 1 April he had not hedged using the [forward market](../../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%2015/Tba%20and%20Specified%20Pools%20Markets.md), since he can obtain SFr 500,000 by paying $\$330,400$ – rather than paying $\$331,000$ in the [forward market](../../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%2015/Tba%20and%20Specified%20Pools%20Markets.md). But the crucial point here is that the [FX spot rate](../../../Financial%20Instruments/Lecture%20Notes-%20Financial%20Instruments/Teaching%20Note%201-%20Forward%20Rates%20Agreement/Foreign%20Exchange%20Quoting%20Conventions.md) for October is not known in April. If you choose to hedge then you remove risk, so you also forego any potential gains (as well as losses) which might accrue ex-post, when you reach 25 October.  

# 7.4.2 Short Hedge  

Suppose on 1 April a US multinational ExportUS expects to receive Swiss franc payments on 25 October, either from sales of goods in Switzerland or from Swiss investments. Hence, ExportUS is ‘long’ Swiss francs in the cash market and may fear a fall in the Swiss franc, thus receiving fewer US dollars in the future. ExportUS would hedge by selling Swiss francs in the [forward market](../../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%2015/Tba%20and%20Specified%20Pools%20Markets.md) on 1 April for delivery on 25 October.  

# 7.4.3 Speculation  

Now consider speculation using the US dollar–pound sterling exchange rate (USD-GBP). Suppose the current (1 April) quoted [forward rate](../../../Clippings/Forward%20Points%20in%20Currency.md) is $F_{0}=1.50(\Phi/\mathrm{f})$ for delivery on 25 October. Suppose on 1 April a UK speculator, BritSpec, forecasts the [spot rate](../../../International%20Finance/The%20Foreign%20Exchange%20Market%20Annotations.md) on 25 October to be $S_{T}=1.52(\Phi/£)$ . Hence, BritSpec believes sterling will be worth more in the spot market in October than indicated by the current [forward rate](../../../Clippings/Forward%20Points%20in%20Currency.md). BritSpec therefore buys sterling in the [forward market](../../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%2015/Tba%20and%20Specified%20Pools%20Markets.md) today and sells sterling in the spot market in October $(S_{T}>F_{0})$ . If BritSpec’s informed guess about $S_{T}$ turns out to be correct then it will make a speculative proft in October.  

# Today 1 April (Spot GBP to rise, go long forward contract)  

• Agree to pay $F_{0}=1.50$ and receive £1 forward on 25 October then:  

# Maturity 25 October  

• Receive $S_{T}=1.52$ USDs (and pay £1) in the spot [FX market](../../../International%20Finance/Foreign%20Exchange%20Markets%20and%20Exchange%20Rate%20Determination.md) • Pay $F_{0}=1.50$ USDs (and receive £1) from the forward deal • Proft $=S_{T}-F_{0}=\S1.52–\S1.50=\S0.02$ £1 .  

If the [principal amount](../../../Financial%20Instruments/Financial%20Derivatives%20and%20Quantitative%20Methods/HSBC-Auto%20callable%20Barrier%20Notes%20with%20Step-up%20Premium.md) in the transaction is $Q=£100,000$ then:  
$$
\mathrm{Total~\mathbb{S}-p r o f i t}=\mathbb{S}(S_{T}\mathrm{-}F_{0})Q=\S2{,}000
$$  

Note that this is a highly risky transaction since if the [spot rate](../../../International%20Finance/The%20Foreign%20Exchange%20Market%20Annotations.md) on 25 October is below $1.50(\S/£)$ then BritSpec will make a loss (which could be very large). This is also a levered transaction since BritSpec uses none of its own funds on 1 April.  

# 7.5 HEDGING AND SPECULATION: FUTURES  

We see below that [hedging](../../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%205/Key%20Rates%20O1s%20Durations%20and%20Hedging.md) and speculation with [futures contracts](../../Mathematics%20of%20the%20Financial%20Markets.md) gives a result which is very close to that when using [forwards](../../../Financial%20Markets/Financial%20Asset%20Pricing%20Theory%20Overview/Chapter%2012%20-%20Derivatives/Forwards%20and%20Futures.md), the main diference being that the [futures](../../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%203%20-%20Futures%20Markets/Futures%20Not%20Subject%20to%20Cash-And-Carry.md) are often closed out before maturity and [futures](../../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%203%20-%20Futures%20Markets/Futures%20Not%20Subject%20to%20Cash-And-Carry.md) involves margin payments.  

# 7.5.1 Speculation Using FX-Futures  

Suppose BritSpec buys sterling [currency futures](.md) at $F_{0}=1.04(\Phi/\Theta)$ , which is for delivery of %125,000. If some time later, $F_{1}=1.05(\mathbb{\S}/\epsilon)$ then BritSpec makes a mark-to-market proft of $\$1,250$ which is credited to its margin account. Alternatively if $F_{1}=1.03(\Phi/\Theta)$ then BritSpec has $\$1,250$ deducted from her margin account.  

If at expiry $F_{T}=1.05(\Phi/\Theta)=S_{T}$ , then the proft would difer slightly from $\$1,250$ because of the interest earned (lost) on BritSpec’s additional margin receipts (payments) over the life of the contract. But ignoring interest on margin payments:  
$$
{\mathfrak{G}}{\mathrm{-}}{\mathrm{Profit~}}({\mathrm{close-out}})={\mathfrak{G}}(F_{1}-F_{0})\in125{,}000
$$  

# 7.5.2 Hedging Using FX-Futures  

International investors and multinational corporations are vulnerable to transactions exposure, namely [exchange rate risk](../../../Financial%20Instruments/Assignments/PSET%203%20Financial%20Instruments.md) of future cash receipts or payments in a foreign [currency](../../../Financial%20Instruments/Lecture%20Notes-%20Financial%20Instruments/Teaching%20Note%201-%20Forward%20Rates%20Agreement/Forwards%20and%20Futures%20Notes.md). [Currency futures](.md) can be used to hedge this exposure because the correlation between spot and [futures](../../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%203%20-%20Futures%20Markets/Futures%20Not%20Subject%20to%20Cash-And-Carry.md) prices is high.  

# 7.5.3 Long Hedge (US Importer)  

Suppose a US importer, UncleSam (on 1 April) has to pay SFr 500,000 in 6 months’ time (on 25 October), for imports from Switzerland. If the spot-FX rate for SFr appreciates (i.e. the dollar depreciates) over the next 6 months then UncleSam will have to pay out more dollars (than at the current [spot rate](../../../International%20Finance/The%20Foreign%20Exchange%20Market%20Annotations.md)). To hedge this position UncleSam takes a [long position](Chapter%204%20-%20Futures:%20Hedging%20and%20Speculation.md) in Swiss franc [futures](../../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%203%20-%20Futures%20Markets/Futures%20Not%20Subject%20to%20Cash-And-Carry.md) (where the maturity date of the [futures](../../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%203%20-%20Futures%20Markets/Futures%20Not%20Subject%20to%20Cash-And-Carry.md) is after 25 October – so for example, UncleSam could use the December [futures](../../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%203%20-%20Futures%20Markets/Futures%20Not%20Subject%20to%20Cash-And-Carry.md)). What UncleSam loses in the spot market it hopes to be ofset with cash gains in the [futures](../../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%203%20-%20Futures%20Markets/Futures%20Not%20Subject%20to%20Cash-And-Carry.md) market (and vice versa), when it closes out the [futures](../../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%203%20-%20Futures%20Markets/Futures%20Not%20Subject%20to%20Cash-And-Carry.md). Hence:  

Need to hedge a payment of SFr in 6 months $\Rightarrow$ Buy SFr [Futures](../../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%203%20-%20Futures%20Markets/Futures%20Not%20Subject%20to%20Cash-And-Carry.md) today  

Suppose UncleSam is currently faced with the following rates:  
$$
\begin{array}{r l}&{S_{0}=\mathrm{spot}\mathrm{rate}=0.6700(\mathbb{\S}/\mathrm{SFr})}\\ &{F_{0}=\mathrm{futures}\mathrm{price}(\mathrm{December}\mathrm{delivery})=0.6738(\mathbb{\S}/\mathrm{SFr})}\end{array}
$$  

Contract size $z=\mathrm{SFr}125,000$  
$$
\mathrm{Tick\size}=0.0001\ (\S/\mathrm{SFr})\quad(\mathrm{Tick\value}=\S12.50)
$$  
$$
V_{s}=\mathrm{value~of~spot~exposure~in~Swiss~Francs~(=SFr~56^{~}~)}
$$  

We can use two methods to calculate the number of [futures contracts](../../Mathematics%20of%20the%20Financial%20Markets.md) required to hedge the upcoming foreign [currency](../../../Financial%20Instruments/Lecture%20Notes-%20Financial%20Instruments/Teaching%20Note%201-%20Forward%20Rates%20Agreement/Forwards%20and%20Futures%20Notes.md) payments. This can be done using either the Swiss franc or the US dollar as the ‘common [currency](../../../Financial%20Instruments/Lecture%20Notes-%20Financial%20Instruments/Teaching%20Note%201-%20Forward%20Rates%20Agreement/Forwards%20and%20Futures%20Notes.md)’ when calculating $N_{F}$ – but the two methods usually give similar answers. (Which is more useful depends in part on whether we expect the absolute change in $F$ and $s$ or their proportionate changes to be most closely correlated – see Appendix 7.)  

# Hedge ratio (1 April, $\pmb{t=0}$ ):  

The simplest method is to use the SFr amount $V_{s}=\mathrm{SFr}500,000$ and divide by the contract size, $z=\mathrm{SFr}125,000$ . This is usually accurate enough and we will concentrate on this method in our example.  
$$
N_{F}=\frac{C a s h m a r k e t p o s i t i o n i n S F r}{C o n t r a c t s i z e i n S F r}=\frac{V_{s}}{\mathrm{SFr}~125,000}=4\:0
$$  

A slightly more complex method is to convert both the cash market position and the size of the [futures](../../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%203%20-%20Futures%20Markets/Futures%20Not%20Subject%20to%20Cash-And-Carry.md) contract into US dollars, the [currency](../../../Financial%20Instruments/Lecture%20Notes-%20Financial%20Instruments/Teaching%20Note%201-%20Forward%20Rates%20Agreement/Forwards%20and%20Futures%20Notes.md) of the US importer, then:  
$$
N_{F}=\frac{\S V_{s}}{\S V_{F}}=\frac{V_{s}S_{0}}{z F_{0}}=\frac{500,000(0.6700)}{125,000(0.6738)}=\frac{\S335,500}{\S84,225}=3.98(4\mathrm{{contra}}
$$  

where $\$1$ is the total value of spot exposure in US dollars and $\$1$ is the value in US dollars of one Swiss franc [futures](../../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%203%20-%20Futures%20Markets/Futures%20Not%20Subject%20to%20Cash-And-Carry.md) contract $(=z F_{0})$ .  

Both methods give $N_{F}=4$ long contracts. We can analyse [hedging](../../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%205/Key%20Rates%20O1s%20Durations%20and%20Hedging.md) by the US importer either in terms of ‘the change in the cash market position less the change in the [futures](../../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%203%20-%20Futures%20Markets/Futures%20Not%20Subject%20to%20Cash-And-Carry.md) position’ or, in terms of ‘the dollar value of the fnal outcome’ for the US importer. We discuss each in turn.  

In Table 7.3 we show the position on 25 October $t=1\AA$ after the Swiss Franc has appreciated from $S_{0}=0.67$ \$ to $S_{1}=0.72\left(\mathbb{S}/\mathrm{SFr}\right)$ , that is by 500 ticks. The increase in cost to the US importer in the spot market is $V_{s}(S_{1}-S_{0})=\mathbb{\{25,000}}$ . However, as the Swiss franc spot-rate appreciates, so does the futures price from $F_{0}=0.6738\left(\mathbb{S}/\mathrm{SFr}\right)$ to $F_{1}=0.7204$ $({\mathbb S}/{\operatorname{SFr}})$ that is, an increase of 466 ticks. The gain on the long futures position is $\$23,300\mathrm{~[=~466~}$ ticks $\times$ $\$12.50\times4$ contracts which nearly ofsets the increased dollar cost in the spot market. A key feature of the success of the hedge is that $\Delta S\approx\Delta F$ so the change in the basis $b_{1}-b_{0}=+34$ ticks, is small.  

Consider the fnal net dollar cost to the US importer in October:  
$$
\begin{array}{r l}{\mathrm{}}&{{}=\S360,000-\S23,300=\S336,700}\\ {\mathrm{}}&{{}=V_{s}S_{1}-N_{F}z(F_{1}-F_{0})=V_{s}(b_{1}+F_{0})}\end{array}
$$  

We have used $N_{F}z=V_{s}$ and (7.12) makes clear that the hedge ‘locks in’ the [futures price](../../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%2011/Futures%20Price%20and%20the%20Quality%20Option%20Before%20E.md) $F_{0}$ , as long as the fnal basis $b_{1}=S_{1}-F_{1}$ is ‘small’. Efectively, UncleSam pays out $\$336,700$ to  

TABLE 7.3 Long hedge (Swiss franc [futures](../../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%203%20-%20Futures%20Markets/Futures%20Not%20Subject%20to%20Cash-And-Carry.md))   


<html><body><table><tr><td>1 April</td><td>Sg= 0.6700 ($/SFr) Nf = 4 contracts</td></tr><tr><td>25 October</td><td>Initial basis = bg = (Sg-F) = -0.0038 ($/SFr) (38 ticks) S = 0.7200 ($/SFr) (Swiss franc has appreciated, dollar has depreciated)</td></tr><tr><td></td><td>F = 0.7204 ($/SFr)</td></tr><tr><td></td><td></td></tr><tr><td></td><td>US importer pays spot:</td></tr><tr><td></td><td>$V = VsS = SFr 500,000(0.7200)= $360,000</td></tr><tr><td></td><td>Increase in $-payments = $V1 - $V = Vs(S - S) = $25,000</td></tr><tr><td></td><td>Gain on [futures](../../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%203%20-%20Futures%20Markets/Futures%20Not%20Subject%20to%20Cash-And-Carry.md) = Nfz(F - Fo) = 4(SFr 125,000)(0.7204-0.6738) = 4($12.50)(466 ticks) = $23,000</td></tr><tr><td></td><td>Final basis: b = S -F = -0.0004 (4 ticks)</td></tr><tr><td></td><td>Change in basis: △S - △F = b - bg= -4 -(-38)= +34 ticks</td></tr></table></body></html>  

receive SFr 500,000 which implies an efective rate at $t=1$ of:  
$$
\frac{N e t U S D c o s t}{V_{s}}=\frac{\S336,700}{\mathrm{SFr}500,000}=\left(b_{1}+F_{0}\right)=0.6734\:(\mathrm{\Phi}\mathrm{\S}\mathrm{Fr})
$$  

which is very close to the initial [futures price](../../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%2011/Futures%20Price%20and%20the%20Quality%20Option%20Before%20E.md) of $F_{0}=0.6738\left(\mathbb{\Phi}/\mathrm{SFr}\right).$ – the diference being the fnal basis $b_{1}=-4$ ticks.  

# 7.5.4 Short Hedge (US Exporter)  

Suppose on 1 April a US multinational, ExpUS, expects to receive sterling payments on 25 October, either from exports of goods to the UK or from sterling investments (i.e. dividends, capital gains or interest). ExpUS is ‘long sterling’ in the cash market and fears a fall in sterling. Hence today it would hedge by [shorting](../../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%202%20-%20Spot%20Markets/Short%20Selling.md) sterling [futures contracts](../../Mathematics%20of%20the%20Financial%20Markets.md):  

ExpUS will receive sterling in months $\Rightarrow$ Sell Sterling [FX Futures](.md) today  

If spot sterling depreciates between April and October then ExpUS obtains less USD in the spot market. However, it will gain by closing out the short-sterling [futures](../../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%203%20-%20Futures%20Markets/Futures%20Not%20Subject%20to%20Cash-And-Carry.md) position at a proft. Of course, these [hedging](../../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%205/Key%20Rates%20O1s%20Durations%20and%20Hedging.md) strategies involve [basis risk](../../../Financial%20Markets%20and%20Institutions/III.%20Liquidity%20of%20Assets/Class%208-%20Markets,%20Meltdowns,%20and%20Arbitrage/Lessons%20From%20The%20Crisis.md): if there are sharp changes in either US [interest rates](../../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%202/Interest%20Rate%20Quotations.md) or foreign [interest rates](../../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%202/Interest%20Rate%20Quotations.md) then $F$ and $s$ will not move closely together and the hedge may perform much worse than expected.  

# 7.6 SUMMARY  

• [Currency forwards](../../../Financial%20Instruments/Lecture%20Notes-%20Financial%20Instruments/Teaching%20Note%201-%20Forward%20Rates%20Agreement/Forward%20Contracts%20on%20Exchange%20Rates.md) are OTC contracts which can be designed to exactly ft clients’ requirements as to amount, delivery dates and currencies. [Forward FX contracts](../../../Financial%20Instruments/Lecture%20Notes-%20Financial%20Instruments/Teaching%20Note%201-%20Forward%20Rates%20Agreement/Forward%20Contracts%20on%20Exchange%20Rates.md) have credit (default) risk. • The cash fows from an actual [forward contract](../../../Clippings/Forward%20Points%20in%20Currency.md) can be ‘replicated’ by using the spot FX-rate and two money market [interest rates](../../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%202/Interest%20Rate%20Quotations.md) – this is the ‘synthetic forward’. Risk-free [arbitrage](../../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%207/Arbitrage%20Pricing%20of%20Derivatives.md) then ensures that the quoted [forward rate](../../../Clippings/Forward%20Points%20in%20Currency.md) equals the synthetic (‘correct’, ‘fair’, ‘no-[arbitrage](../../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%207/Arbitrage%20Pricing%20of%20Derivatives.md)’) [forward rate](../../../Clippings/Forward%20Points%20in%20Currency.md). This is the [covered interest parity](../../../Financial%20Instruments/Lecture%20Notes-%20Financial%20Instruments/Teaching%20Note%201-%20Forward%20Rates%20Agreement/Interest%20Rates,%20Carry%20Trades,%20and%20Exchange%20Rate%20Movements.md) , CIP, condition:  
$$
F=S(1+r_{d}T)/(1+r_{f}T)
$$  

• [Currency forwards](../../../Financial%20Instruments/Lecture%20Notes-%20Financial%20Instruments/Teaching%20Note%201-%20Forward%20Rates%20Agreement/Forward%20Contracts%20on%20Exchange%20Rates.md) can be [used for hedging and speculation](../../../Clippings/Options%20Contract%20-%20Types%20of%20Contracts.md). The payof at maturity for a [long position](Chapter%204%20-%20Futures:%20Hedging%20and%20Speculation.md) in a [forward contract](../../../Clippings/Forward%20Points%20in%20Currency.md) on a foreign [currency](../../../Financial%20Instruments/Lecture%20Notes-%20Financial%20Instruments/Teaching%20Note%201-%20Forward%20Rates%20Agreement/Forwards%20and%20Futures%20Notes.md) is, $S_{T}-F_{0}$ . • [Currency futures](.md) are similar to [currency forwards](../../../Financial%20Instruments/Lecture%20Notes-%20Financial%20Instruments/Teaching%20Note%201-%20Forward%20Rates%20Agreement/Forward%20Contracts%20on%20Exchange%20Rates.md) – the main diferences being that [futures contracts](../../Mathematics%20of%20the%20Financial%20Markets.md) can be easily closed out prior to the maturity (delivery) date and [futures contracts](../../Mathematics%20of%20the%20Financial%20Markets.md) require margin payments.  

• [Currency futures](.md) provide a low cost method of [hedging](../../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%205/Key%20Rates%20O1s%20Durations%20and%20Hedging.md) known future foreign [currency](../../../Financial%20Instruments/Lecture%20Notes-%20Financial%20Instruments/Teaching%20Note%201-%20Forward%20Rates%20Agreement/Forwards%20and%20Futures%20Notes.md) receipts or payments (e.g. transactions exposure from imports and exports and repatriating profts or, receipts or payments on foreign assets, such as dividends, capital gains, and interest). There is virtually zero [credit risk](../../../Course%20Notes/Quantitative%20Trading%20Strategies%20Lecture%20Notes.md) when using [futures](../../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%203%20-%20Futures%20Markets/Futures%20Not%20Subject%20to%20Cash-And-Carry.md), because of [margin requirements](../../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%2010/Case%20Study%20Mf%20Globals%20Repo-To-Maturity%20Trades.md).   
• [Basis risk](../../../Financial%20Markets%20and%20Institutions/III.%20Liquidity%20of%20Assets/Class%208-%20Markets,%20Meltdowns,%20and%20Arbitrage/Lessons%20From%20The%20Crisis.md) in a hedge arises with [futures contracts](../../Mathematics%20of%20the%20Financial%20Markets.md) which are closed out prior to maturity – this is caused by changes in domestic or foreign [interest rates](../../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%202/Interest%20Rate%20Quotations.md) over the hedge period. Also there are risks due to the fact that the interest rate applicable to [margin calls](../../../Financial%20Markets%20and%20Institutions/III.%20Liquidity%20of%20Assets/Class%208-%20Markets,%20Meltdowns,%20and%20Arbitrage/Class%20Note%2013%20The%20LTCM%20Meltdown.md) is unknown at the outset of the hedge.   
• [Futures](../../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%203%20-%20Futures%20Markets/Futures%20Not%20Subject%20to%20Cash-And-Carry.md) prices can be determined using the cost of carry approach which is equivalent to the [covered interest parity](../../../Financial%20Instruments/Lecture%20Notes-%20Financial%20Instruments/Teaching%20Note%201-%20Forward%20Rates%20Agreement/Interest%20Rates,%20Carry%20Trades,%20and%20Exchange%20Rate%20Movements.md) (CIP) condition. In practice there is little diference between quoted FX forward and [futures](../../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%203%20-%20Futures%20Markets/Futures%20Not%20Subject%20to%20Cash-And-Carry.md) prices.   
• Speculation using [currency futures](.md) often allows greater [leverage](../../../Advanced%20Investments/Lecture%206-Leverage,%20Tail%20Risk,%20Volatility%20Products.md) than speculation in the spot [FX market](../../../International%20Finance/Foreign%20Exchange%20Markets%20and%20Exchange%20Rate%20Determination.md) as only the initial margin payment is required to take an open position in an [FX futures](.md) contract.  

# APPENDIX 7: HEDGING USING FX-FUTURES  

This appendix puts the [hedging](../../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%205/Key%20Rates%20O1s%20Durations%20and%20Hedging.md) examples in the text into algebraic form. Consider a US importer UncleSam, with Swiss franc payments of SFr 500,000 in the future. We use the following notation:  

Vs value in foreign [currency](../../../Financial%20Instruments/Lecture%20Notes-%20Financial%20Instruments/Teaching%20Note%201-%20Forward%20Rates%20Agreement/Forwards%20and%20Futures%20Notes.md) of cash market position $\mathbf{\bar{\rho}}=\mathbf{\bar{\rho}}$ 500 000 $S_{0}={\mathrm{spot}}{\mathrm{rate}},\S/{\mathrm{SFr}}$ $\$123,456$ initial value of cash market position $z={\mathrm{Contract~size}}\left(={\mathrm{SFr~}}125,000\right)$ $\$1$ the amount of dollars paid the of the hedge  

Case A: Using ‘Foreign [Currency](../../../Financial%20Instruments/Lecture%20Notes-%20Financial%20Instruments/Teaching%20Note%201-%20Forward%20Rates%20Agreement/Forwards%20and%20Futures%20Notes.md)’ to Calculate $N_{F}$  
$$
N_{F}=V_{s}/z
$$  

Efective Dollar $C o s t=\delta C o s t$ in cash market $\$8$ Gain short [futures](../../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%203%20-%20Futures%20Markets/Futures%20Not%20Subject%20to%20Cash-And-Carry.md) position  
$$
\S V_{1}=V_{s}S_{1}-N_{F}z(F_{1}-F_{0})
$$  

Using $V_{s}=N_{F}z$ , we have:  
$$
\S V_{1}=V_{s}[S_{1}-F_{1}+F_{0}]=b_{1}+F_{0}
$$  

Hence, the hedge locks in the [futures price](../../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%2011/Futures%20Price%20and%20the%20Quality%20Option%20Before%20E.md) $F_{0}$ if the fnal basis $b_{1}=(S_{1}-F_{1})$ is small. This is an unambiguous way of interpreting the hedge. Using $S_{1}=S_{0}+d S$ in Equation (7.A.3) and subtracting the initial USD cost, $\$123,456$ , the increase in USD cost is:  
$$
\mathfrak{H}_{1}-\mathfrak{H}_{0}=V_{s}(d S-d F)
$$  

If equals $d F$ (on average), then the ‘beta’ of the regression of $d S$ on $d F$ would be unity. Under these circumstances, the hedge scenario would involve no change in the USD cost of the imports. But this scenario would be unlikely to occur exactly, in practice.  

Case B: Using Domestic [Currency](../../../Financial%20Instruments/Lecture%20Notes-%20Financial%20Instruments/Teaching%20Note%201-%20Forward%20Rates%20Agreement/Forwards%20and%20Futures%20Notes.md) (USD) to Calculate $N_{F}^{*}$  
$$
N_{F}^{*}=\frac{\mathfrak{F}V_{0}}{\mathfrak{F}V_{F}}=\frac{V_{s}S_{0}}{z F_{0}}
$$  

Here the efective US dollar cost of the imports is:  
$$
\S V_{1}=\S{\mathrm{-Cost~of~imports-}}\S\Phi{\mathrm{-gain~on~futures}}=V_{s}S_{1}-N_{F}^{*}d F z
$$  

Substituting for $N_{F}^{*}$ and using $S_{1}=S_{0}+d S$ :  
$$
\mathfrak{H}V_{1}=\mathfrak{H}V_{0}+\mathfrak{H}V_{0}(d S/S_{0}-d F/F_{0})
$$  

Hence, the fnal USD cost when using this [hedge ratio](../Part%20VI%20-%20The%20Greeks/Chapter%2027%20-%20Delta%20Hedging.md), will be close to the initial USD cost if $s$ and $F$ move together proportionately. Turning now to the increase in cost we have:  
$$
\mathfrak{H}V_{1}-\mathfrak{H}V_{0}=\mathfrak{H}V_{0}(d S/S_{0}-d F/F_{0})
$$  

There is no increase in the cost of the hedge position (in US dollars) if the proportionate change in $F$ and $s$ are equal. Clearly, if $S_{0}\approx F_{0}$ then the two hedge ratios give very similar results. Given [covered interest parity](../../../Financial%20Instruments/Lecture%20Notes-%20Financial%20Instruments/Teaching%20Note%201-%20Forward%20Rates%20Agreement/Interest%20Rates,%20Carry%20Trades,%20and%20Exchange%20Rate%20Movements.md), $F=\overline{{S e}}^{(r_{\mathrm{d}}^{\mathrm{c}}-r_{\mathrm{f}}^{\mathrm{c}})T}$ (using continuously compounded rates) then for small changes we have:  
$$
d F/F_{0}=d S/S_{0}+(d r_{\mathrm{d}}^{\mathrm{c}}-d r_{\mathrm{f}}^{\mathrm{c}})T+(r_{\mathrm{d}}^{\mathrm{c}}-r_{\mathrm{f}}^{\mathrm{c}})d T.
$$  

Hence given the fact that the volatility in $s$ is much greater than the volatility of [interest rates](../../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%202/Interest%20Rate%20Quotations.md), then the proportionate change in $F$ and $s$ will be almost equal if the hedge is over a relatively short time period. Also, if $F_{0}\approx S_{0}$ , which will be the case if the initial domestic and foreign [interest rates](../../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%202/Interest%20Rate%20Quotations.md) are not too diferent (or the [time to maturity](../../../Financial%20Instruments/Lecture%20Notes-%20Financial%20Instruments/Teaching%20Note%201-%20Forward%20Rates%20Agreement/Hedging%20Strategies%20with%20Forwards.md) is short) and remain constant, then from (7.A.9) $d F\approx d S$ . Hence, under these circumstances it may make little diference in practice whether we use $N_{F}$ or $N_{F}^{*}$ .  

# EXERCISES  

# Question 1  

You are a US investor and you forecast that the euro will appreciate against the US dollar over the next week. How can the spot [FX market](../../../International%20Finance/Foreign%20Exchange%20Markets%20and%20Exchange%20Rate%20Determination.md) be used for speculation?  

# Question 2  

How can you use the spot [FX market](../../../International%20Finance/Foreign%20Exchange%20Markets%20and%20Exchange%20Rate%20Determination.md) and the 1-year forward [FX market](../../../International%20Finance/Foreign%20Exchange%20Markets%20and%20Exchange%20Rate%20Determination.md) for speculation? Assume the quoted one-year [forward rate](../../../Clippings/Forward%20Points%20in%20Currency.md) is $F=1.0020$ USD per euro and you forecast the [spot rate](../../../International%20Finance/The%20Foreign%20Exchange%20Market%20Annotations.md) in 1 year’s time is $S_{T}=1.00$ USD per euro. You speculate using %100 today.  

# Question 3  

What does [covered interest parity](../../../Financial%20Instruments/Lecture%20Notes-%20Financial%20Instruments/Teaching%20Note%201-%20Forward%20Rates%20Agreement/Interest%20Rates,%20Carry%20Trades,%20and%20Exchange%20Rate%20Movements.md) (CIP) mean? What determines whether CIP holds at any point in time?  

# Question 4  

The [spot rate](../../../International%20Finance/The%20Foreign%20Exchange%20Market%20Annotations.md) for US dollar (USD) against the pound sterling (GBP) is 1.65 (USD/GBP).   
Three-month UK [interest rates](../../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%202/Interest%20Rate%20Quotations.md) are at $7.5\%$ p.a. ([simple interest](../../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%202/Interest%20Rate%20Quotations.md), actual/365 [day-count](../../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%202%20-%20Spot%20Markets/Intra-Year%20Compounding%20and%20Day-Count.md) basis).   
Three-month US [interest rates](../../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%202/Interest%20Rate%20Quotations.md) are $6\%$ p.a. ([simple interest](../../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%202/Interest%20Rate%20Quotations.md), actual/365 [day-count](../../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%202%20-%20Spot%20Markets/Intra-Year%20Compounding%20and%20Day-Count.md) basis).   
Assume there are 30 days in each month. Calculate the 30-day [forward rate](../../../Clippings/Forward%20Points%20in%20Currency.md) and the forward margin.  

# Question 5  

You are a US investor. Current [interest rates](../../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%202/Interest%20Rate%20Quotations.md) are $r_{U K}=2\%$ , $r_{U S}=1\%$ (continuously compounded) and the spot FX rate is $S=1.3$ (USD/GBP).  

(a) Calculate the no-[arbitrage](../../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%207/Arbitrage%20Pricing%20of%20Derivatives.md) (fair) [forward FX rate](../../../Financial%20Markets/Random%20Walks%20in%20Fixed%20Income%20and%20Foreign%20Exchange/Chapter%201/What%20Really%20Is%20the%20Cross-Currency%20Basis.md), for a maturity of 6 months ( $T=1/2$ year .   
(b) If the current quoted [forward rate](../../../Clippings/Forward%20Points%20in%20Currency.md) is $F_{q}=1.25$ (USD/GBP), show how a £1,000 [investment](../../../Advanced%20Investments/An%20Asset%20Allocation%20Primer.md) by a US arbitrageur can result in risk-free [arbitrage](../../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%207/Arbitrage%20Pricing%20of%20Derivatives.md) proft.  

# Question 6  

The spot price of the Swiss franc (SFr) or ‘Swissy’ is $S=0.65$ (USD per SFr) and the quoted [futures price](../../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%2011/Futures%20Price%20and%20the%20Quality%20Option%20Before%20E.md) on a 2-month [forward contract](../../../Clippings/Forward%20Points%20in%20Currency.md) is $F_{q}=0.66$ (USD/SFr). [Interest rates](../../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%202/Interest%20Rate%20Quotations.md) in Switzerland are $2\%$ p.a. and in the USA $8\%$ p.a. (continuously compounded).  

(a) What is the no-[arbitrage](../../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%207/Arbitrage%20Pricing%20of%20Derivatives.md) (fair) [futures price](../../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%2011/Futures%20Price%20and%20the%20Quality%20Option%20Before%20E.md)? (b) What [arbitrage opportunities](../../../Financial%20Markets%20and%20Institutions/III.%20Liquidity%20of%20Assets/Class%208-%20Markets,%20Meltdowns,%20and%20Arbitrage/Class%20Note%2013%20The%20LTCM%20Meltdown.md) exist for a US resident?  

# Question 7  

A UK frm knows it will receive $\$100$ in 1 year’s time (from the sale of goods in the USA). Current interest rates are $r_{U K}=10\%$ , $r_{U S}=12\%$ (simple rates) and the spot rate $S=$ 1.6 (USD/GBP).   
Calculate the [forward rate](../../../Clippings/Forward%20Points%20in%20Currency.md) (USD per GBP).   
Explain how the UK could hedge this infow of $\$100$ in 1 year’s time by using the money markets and the spot [FX market](../../../International%20Finance/Foreign%20Exchange%20Markets%20and%20Exchange%20Rate%20Determination.md) (i.e. not using the [forward market](../../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%2015/Tba%20and%20Specified%20Pools%20Markets.md) directly).   
Briefy comment on these results.  

# Question 8  

How would a US frm importing goods from Switzerland in 6 months’ time hedge its position by using the (FX) [futures](../../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%203%20-%20Futures%20Markets/Futures%20Not%20Subject%20to%20Cash-And-Carry.md) market?  

# Question 9  

The UK treasurer of Suits plc expects to receive payment for exports of tailored men’s suits to a customer in Munich in 3 months’ time $T=1/4$ year . Her marketing department has sold 1,000 suits at a delivery price of %250 each. In the Financial Times on 10 June, she observes the following:  

Spot FX rate 0.850 (%/£) 3-month [forward FX rate](../../../Financial%20Markets/Random%20Walks%20in%20Fixed%20Income%20and%20Foreign%20Exchange/Chapter%201/What%20Really%20Is%20the%20Cross-Currency%20Basis.md) 0.853 (%/£)  

Sterling 3-month (simple) interest rate (annualised) $r=5.5625\%$  

Euro 3-month (simple) interest rate (annualised) $r^{*}=7.6250\%$  

(a) Explain using the above data, how the treasurer can hedge her receipts in euros by: (i) taking forward cover (ii) taking money-market cover.   
(b) What would be the amount of sterling received if the treasurer took an uncovered (open) position and the [spot rate](../../../International%20Finance/The%20Foreign%20Exchange%20Market%20Annotations.md) $S_{T}$ in 3 months’ time is: (i) 0.653 (%/£) (ii) 0.658 (%/£) (iii) 0.640 (%/£) In each case, compare the hedged outcome with the uncovered outcome.  

(c) Are the set of interest and exchange rates prevailing on 15 June consistent with [covered interest parity](../../../Financial%20Instruments/Lecture%20Notes-%20Financial%20Instruments/Teaching%20Note%201-%20Forward%20Rates%20Agreement/Interest%20Rates,%20Carry%20Trades,%20and%20Exchange%20Rate%20Movements.md)? If not, explain how equilibrium will be established in the relevant markets.  
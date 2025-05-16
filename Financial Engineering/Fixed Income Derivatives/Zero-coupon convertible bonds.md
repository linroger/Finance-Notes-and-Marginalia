---
tags:
  - convertible_bonds
  - equity_play
  - ocns
  - quanto_note
  - volatility
  - zero_coupon_bonds
aliases:
  - Convertible Quanto Note
  - OCNs
  - Optional Convertible Notes
key_concepts:
  - Downside market protection
  - Equity play with protection
  - Exposure to company equity
  - High upside potential
  - Implicit yield and trade
  - No foreign exchange risk
  - Zero-coupon convertible bonds
---

# [](../1.%20DeterministicCashFlows.md#2%20Fixed%20Income%20Securities|Zero-coupon) [convertible bonds](../7.%20Black%20Scholes%20Model.md)
Zero-coupon convertible bonds or “optional convertible notes” (OCNs) are wellestablished in the market. When they are issued at a discount to par, they exhibit an  implicit yield and trade essentially as coupon convertibles. Similarly, if they are  issued at par but redeemed at a stated price above par, an implicit coupon is paid and  so again these bonds trade in similar fashion to coupon convertibles. A zero-coupon  bond issued at par and redeemed at par is a slightly different instrument for investors  to consider. With these products, the buyer is making more of an equity play than he  is with conventional OCNs, but with an element of capital protection retained.

A buyer of a par-priced zero-coupon OCN will have a view that the underlying equity  has [high upside potential](.md). However the stock will have high volatility, so the OCN  route is still lower risk than the pure equity route; the investor pays an opportunity  cost in terms of interest foregone in order to retain the greater safety compared to pure  equity. The softcall option is often built-in so that the issuer can force conversion if  the equity has performed as expected, which caps the investor’s upside.

In many cases, zero-coupon OCNs are issued in one [currency](../../Financial%20Instruments/Lecture%20Notes-%20Financial%20Instruments/Teaching%20Note%201-%20Forward%20Rates%20Agreement/Forwards%20and%20Futures%20Notes.md) but reference shares  denominated in another (less liquid) [currency](../../Financial%20Instruments/Lecture%20Notes-%20Financial%20Instruments/Teaching%20Note%201-%20Forward%20Rates%20Agreement/Forwards%20and%20Futures%20Notes.md), so that investors can have exposure to  an equity without having to hold assets in the less liquid [currency](../../Financial%20Instruments/Lecture%20Notes-%20Financial%20Instruments/Teaching%20Note%201-%20Forward%20Rates%20Agreement/Forwards%20and%20Futures%20Notes.md).

These products are for sophisticated investors only. Buyers often are taking a view on  [price volatility](../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%206%20Options%20on%20Non-Price%20Variables/Black%20Models%20for%20Bond%20Price%20Options%20Capsfloors.md), rather than price  per se , and the value of the note will increase if  volatility increases. In other cases, the volatility trade is put on as an [arbitrage](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%207/Arbitrage%20Pricing%20of%20Derivatives.md), that is,  a simultaneous position in which the trader is:
  long the OCN bond, and
  short the underlying equity.

In such a trade the investor benefits if volatility increases. For Issuers, the advantage  of zero-coupon par priced OCNs is even greater than that afforded by conventional  OCNs: they receive no-cost funding compared to a normal bond or loan. In return  they are selling (for them) a cheap route to their equity should the share price  perform.
 ![500](https://cdn-mineru.openxlab.org.cn/model-mineru/prod/8b2c13e0966685155f86d53734ab46fd0f32301a1a19ebdc44e8157a45fc85c1.jpg)

# Example of zero-coupon par-priced OCN

We describe now a zero-coupon OCN, issued at par and redeemed at par in the event  it is not converted. It is termed a convertible “quanto” note.

# Convertible Quanto Note

The Index-linked Quanto Note is aimed at investors who wish to gain exposure to a  company’s equity, but do not wish to invest in assets denominated in the [currency](../../Financial%20Instruments/Lecture%20Notes-%20Financial%20Instruments/Teaching%20Note%201-%20Forward%20Rates%20Agreement/Forwards%20and%20Futures%20Notes.md) of  that equity. An example would be investors who wish to gain exposure to a Japanese  company share but do not wish to hold Yen-denominated assets.

The Note enables investors to gain from upside performance of the selected equity but  with no associated foreign exchange risk. For added comfort, investors are protected  against any downside performance of the underlying equity by means of the Note  structure, which sets a “bond floor” of a minimum stated return.  This is similar to the  bond floor in a convertible bond. Purchasing the Note is equivalent to purchasing  [market volatility](../../Financial%20Markets%20and%20Institutions/III.%20Liquidity%20of%20Assets/Class%209-%20Bailouts%20and%20Bank%20Failures/Class%20Slides%20On%20Terrausd%20Runs%202.md), in the expectation of higher volatility leading to higher equity  prices, whilst retaining an element of [downside market protection](.md).

Figure 2 below illustrates the concept behind the Note.

 ![500](https://cdn-mineru.openxlab.org.cn/model-mineru/prod/03fd450f4e779f4a228aabf96984d00c555316a00b28a23926b255827a23efdb.jpg)
Figure 2

Investors are in effect holding a [long position](../Derivatives/Part%20I%20-%20Forwards%20and%20Futures/Chapter%204%20-%20Futures:%20Hedging%20and%20Speculation.md) in an option and hence will be exposed  to volatility. However the bond floor protects the Investor from downside risk,  irrespective of volatility.

# Example: Japanese equity Note

This Note is a USD-denominated bond, issued at par, that pays investors a return, in  USD, connected to the share-price performance of a Japanese corporate entity  (denominated in JPY). If the underlying equity rises in price (above a specified level,  the “strike” price), the proportionate increase in the share price is paid out on maturity  to the Note investor, as a percentage of par. At any time during its life, the price of the  Note will reflect (among other things) this increase in underlying share price.

The value of the Note is comprised of two components, the intrinsic value and the  option value. On first issue, an equity “strike” price is set on the Note. This may be at  the current underlying share price, or above it. As the underlying share price rises  above the “strike” price, the Note intrinsic value will increase proportionally with that  of the equity. The option value is an additional value (the “premium”) above the  intrinsic value, and is composed of volatility, time value and the level of USD interest  rates. These are standard option [pricing](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%207/Arbitrage%20Pricing%20of%20Derivatives.md) parameters.
If the underlying equity falls in price, the investor is protected by the minimum value  of the Note, known as the “bond floor”. This is the minimum price of the Note at any  one time, hence if the equity price falls below the level at which the bond floor kicks  in, there is no further downside price risk for the investor.

We can illustrate this with an example. Consider the following terms for a USD  Quanto note:

Underlying            Nippon Corp equity (JPY)  Strike                     Y1,200  Spot                       Y1,150  Note Offer               $100.00\%$    Parity                      $95.83\%$    Premium                 $4.35\%$    Life                        3 years  US 3 year rates       $3.68\%$    Bond Floor              $88.36\%$    Delta                       0.50  Maturity price  100.00

The Note is issued at par with a “strike” of Y1,200.

Consider the following scenarios based on both upside and downside performance of  the underlying equity.

If the shares rise to Y1700, a rise of   $47.8\%$  , the parity, or intrinsic value would be   $(1700/1200^{*}100)$   or   $141.66\%$  . This is the minimum value of the Note. Hence a  $47.8\%$  gain in the shares has resulted in a minimum  $41.66\%$   gain in the Note.

Should the underlying equity price fall below the “strike” price, the note is protected  because it carries a bond floor, currently at   $88.36\%$  , accreting to par at maturity. This  represents the [downside protection](Equity%20Linked%20Note.md) for the investor. The option premium above this  floor will still reflect the three option components, and because time value is always  positive, the total value of the Note will be above this bond floor up to maturity.

If the shares fell to Y800, the parity would be  $66.66\%$  , however the minimum value of  the Note would still be the bond floor of   $88.36\%$  . Therefore in this instance a fall of   $30.4\%$   in the shares has resulted in a maximum  $11.6\%$   decline in the Note. However  although the investor’s capital is protected, he has foregone interest on it for the  period of the [investment](../../Advanced%20Investments/An%20Asset%20Allocation%20Primer.md).

Investors are not exposed to any foreign exchange (FX) risk because they pay USD  for the note, and receive return in USD. However one of the option value parameters  is the level of [interest rates](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%202/Interest%20Rate%20Quotations.md), hence investors are exposed to USD [interest rates](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%202/Interest%20Rate%20Quotations.md). A call  option written on an equity will rise in value if (all other parameters held constant)  there is a rise in [interest rates](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%202/Interest%20Rate%20Quotations.md), because the cost-of-carry associated with the equity  also rises. This sensitivity is carried over in the value of the Note, because the  [secondary market](../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%201%20-%20Purpose%20and%20Structure%20of%20Financial%20Markets/Primary%20Issuance%20and%20Secondary%20Resale%20Markets.md) price of the Note is related to the over-the-counter (OTC) options  market.
A partial measure of the change in the price of an option with respect to a change in  the price of the underlying equity is given by the  delta  of the option, which is

For convertible bonds, delta is defined in terms of the sensitivity of the bond’s price  to changes in its parity. The parity is given from the value of the underlying equity  price. The value of this delta can be gauged from Figure 3, which illustrates an  hypothetical bond’s parity and bond floor. The delta is seen from the relationship of  the parity and Note price.

In our example the delta is given as 0.5. So if the Note theoretical price moved from  100 to 100.5 while its parity changed from 95 to 96, the delta would be 0.5.

 ![500](https://cdn-mineru.openxlab.org.cn/model-mineru/prod/f1ef4587fdd3a7414579485c646e97f0646d9f077e5b51a261fe1818ebf29efe.jpg)
 Figure 3

# Examples of zero-coupon OCNs

Figure 1 is a selection of par-priced zero-coupon OCNs issued in January and  February 2006.

The notes issued by Ranbaxy Labs, STM, AMS Life Sciences and Bajaj Hindustan  can be viewed in a similar way to conventional convertible bonds. The investor is  guaranteed a positive return (ignore credit-[risk considerations](../../Financial%20Markets%20and%20Institutions/II.%20The%20Roles%20of%20Banks%20and%20Derivative%20Markets%20in%20Resolving%20Problems%20Inherent%20in%20Debt%20Contracts/HomeMax%20Case%20Study%20Solution.md) of the Issuer) because  the payment on maturity of the notes is above par. The Ranbaxy bond is an example  of a note issued in one [currency](../../Financial%20Instruments/Lecture%20Notes-%20Financial%20Instruments/Teaching%20Note%201-%20Forward%20Rates%20Agreement/Forwards%20and%20Futures%20Notes.md) (USD) that references shares in another [currency](../../Financial%20Instruments/Lecture%20Notes-%20Financial%20Instruments/Teaching%20Note%201-%20Forward%20Rates%20Agreement/Forwards%20and%20Futures%20Notes.md)  (INR). This enables non-domestic investors, who may not desire the operational and  settlement issues associated with holding INR assets, to have exposure to the equity.   The bonds issued by Unipres, Tata Motors, Taiho Kogyo, Aichi Steel and Daifuku are  examples of par-priced zero-coupon OCNs that redeem on maturity at par (or in one  case below par). These securities pay a negative yield, and this is the interest foregone  by the investor on the notes. If the share price performs as desired, the notes will be  converted and the investor will gain; if they do not, there is still the safety of the  capital repayment on maturity (credit-[risk considerations](../../Financial%20Markets%20and%20Institutions/II.%20The%20Roles%20of%20Banks%20and%20Derivative%20Markets%20in%20Resolving%20Problems%20Inherent%20in%20Debt%20Contracts/HomeMax%20Case%20Study%20Solution.md) of the Issuer ignored again).  In some cases we can see that the premium on the bond is greater than it was on issue,  indicating that the share price has dropped since the bond was issued.
These bonds represent an opportunity for investors to take a view on equity without  having to buy the equity, so that an element of capital protection is retained. For the  Issuer, they represent very low-cost funding, and also diversified funding from nondomestic investors.

The critical point to bear in mind regarding these notes is that they are instruments  that focus on the Issuer’s  equity . It is the equity price, and/or equity [price volatility](../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%206%20Options%20on%20Non-Price%20Variables/Black%20Models%20for%20Bond%20Price%20Options%20Capsfloors.md),  that is being targeted via these notes. Without a tradeable equity and a transparent  equity price, the basic  raison d’etre  behind the notes would disappear.

# Market pricing of par-priced zero-coupon OCN issued by subsidiary company to  parent

Banks price OCNs using option [pricing](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%207/Arbitrage%20Pricing%20of%20Derivatives.md) models such as [Black-Scholes](../Mathematical%20Modeling%20of%20Derivative%20Pricing.md), and tree-based  models such as the [binomial](../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%205%20Options%20on%20Prices%20and%20Hedge-Based%20Valuation/A%20Real-Life%20Option%20Pricing%20Exercise.md) or trinomial model. These make certain assumptions with  regard to the behaviour of equity prices, and also use an assumed volatility level.  They also require the underlying share price as one of their inputs. In other words, we  require a traded equity for the option component to be valued.

In the absence of a traded equity, the market would fall back on the dividend  valuation model used in earlier times. This would make assumptions on the equity  valuation, and would be based on the financial data supplied by the subsidiary  company. It has the advantage of assuming zero volatility, which is unsatisfactory in  the “proper” convertible market but would be suitable when there is no traded equity.

In practice, the option element would have no value, because the equity of the  subsidiary is   $100\%$   owned by the parent company in any case. An option to purchase  more of this equity by the same parent would have no economic rationale to it. The  shares do not trade so there is also no time value to the option. The value of the note  would then be composed of the debt component only, however this pays   $0\%$   coupon  and redeems at par. The note carries “negative value” to the holder, which is the face  value of the note discounted by the parent’s WACC or other suitable [discount rate](../../Advanced%20Financial%20Analysis%20and%20Valuation/Problem%20Sets/PSET%207-%20Kohler.md).
Therefore this would be the price of the note if it was sold to an external third party.  A side impact of this is that the sale would result in a realised mark-to-market loss for  the parent, which purchased the note at 100.

If the parent gives notice to the market that it intends to divest the subsidiary  company from the group, then the option element will acquire value. In the absence of  a tradeable share, an implied share price will be calculated using the Issuer’s financial  reports as input data, via standard [corporate finance](../../Course%20Notes/Corporate%20Finance%20Lecture%20Notes.md) valuation techniques. This then  implies a value of the OCN option element based on the conversion terms of the note.  This value is highly speculative but may still be of interest to sophisticated investors  if they have a view on the subsidiary company as a stand-alone entity.

Note that this valuation approach ignores operational issues associated with any selloff the subsidiary company, such as new ownership details, tax structure, and so on,  which would also be considered by potential investors.

The views, thoughts and opinions expressed in this paper represent those of Moorad Choudhry in his  individual private capacity, and should not be taken to be the views of any employing or affiliated  institution, or the views of Moorad Choudhry as an employee or affiliate of any named or unnamed  institution.

\*Moorad Choudhry  is a Visiting Professor at the Department of Economics, London Metropolitan  University, a Visiting Research Fellow at the ICMA Centre, University of Reading, a Senior Fellow at  the Centre for Mathematical Trading and Finance, Cass Business School and a Fellow of the Securities  and [Investment](../../Advanced%20Investments/An%20Asset%20Allocation%20Primer.md) Institute. He is a managing partner in the [fixed income](../../Fixed%20Income%20Asset%20Pricing/Lecture%20Notes%20Bonds,%20%20Preferred%20Stock,%20%20and%20Structured%20Products.md) research e-Journal  www.yieldcurve.com
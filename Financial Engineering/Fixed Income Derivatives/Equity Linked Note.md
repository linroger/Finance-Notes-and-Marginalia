---
tags:
  - call_option
  - equity_exposure
  - equity_linked_notes
  - principal_guaranteed
  - zero_coupon_bond
aliases:
  - ELN
  - Equity-linked note
  - Principal Guaranteed Structures
key_concepts:
  - Bond with call option
  - Downside protection
  - Equity market participation
  - Investment instrument
  - Redemption amount calculation
---

# Equity Linked Note
# Equity Linked Note :  An Introduction to Principal  Guaranteed Structures

# Introduction

In this article we provide a succinct description of a commonly used [investment instrument](.md)  in the capital markets, the [equity-linked note](.md). These are instruments that allows investors  to secure [downside protection](.md) for their initial [investment](../../Advanced%20Investments/An%20Asset%20Allocation%20Primer.md), while still retaining a  participation in any upside gain in the equity market. The equity side of the instrument is  linked to the performance of an equity index, individual stocks, or a [portfolio](../../Advanced%20Investments/An%20Asset%20Allocation%20Primer.md) of indices  and equities.

The basic instrument consists of a bond with no periodic income payments (zero coupon  bond) plus a long call option on either a basket of indices or equities, single equity index,  or stock. Alternative structures may include interest rate call or put options with lower  [coupon payments](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%203/Realized%20Returns.md). At maturity, the holder of each note will receive the par amount of the  note plus a supplemental redemption amount based on the percentage increase of the  equity exposure. As an example, figure 1 below is the description of a medium term note  issued by [Morgan Stanley](../../Financial%20Markets%20and%20Institutions/III.%20Liquidity%20of%20Assets/Class%208-%20Markets,%20Meltdowns,%20and%20Arbitrage/Lessons%20From%20The%20Crisis.md) Dean Witter which has similar characteristics in terms of its  guaranteed income and return profile. This is the “DES” page as featured on the  Bloomberg analytics system.

 ![500](Attachments/500-467.jpg)
Figure 1
The bond described in figure 1 makes no periodic [coupon payments](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%203/Realized%20Returns.md) and matures on 29  Sept 2003. The redemption of the bond is defined in accordance with the following  formula:
$$
\mathbf{FV}+(\mathbf{\;FV\x\101.65\%})\mathbf{\x\ [\St\-St-1]/\St-1}
$$

where

FV is the face value of the bond or the par amount, adjusted by a gearing or participation  level of 1.0165;

St is the closing level of the index, which the bond's payoff is linked to the ( S&P 500  index ) on  a date close to the bond maturity date;

St1  is the index start level which (in this case) is set at 925.31.

Note that Bloomberg users can select  DES  $\tt<g o>$   and then   ${\bf7}\times{\bf\underline{{g}}o}^{>}$   to see the redemption  formula as it is defined in the prospectus.

From the view point of the holder of the above instrument, the transaction operates as  follows:

  the investor is guaranteed the return of his initial [investment](../../Advanced%20Investments/An%20Asset%20Allocation%20Primer.md). That is  $\mathbb{S}1000$   per note, so  the investor receives at least  $\S1000$  ;

  the investor's final cash receipt, that is, the redemption amount, is linked to the  performance of the S&P 500 index. If the index appreciates over the stated level of  925.31 and stays at this level upon maturity of the bond, then the investor receives a  redemption amount which is calculated as the face value amount multiplied by the  percentage increase of the index adjusted by the participation level. For example, if the  index doubles over the life of the bond, the investor simply doubles the original  [investment](../../Advanced%20Investments/An%20Asset%20Allocation%20Primer.md). If however the index declines below the index start level, the investor will  receive the original [investment](../../Advanced%20Investments/An%20Asset%20Allocation%20Primer.md).

The payoff of the instrument can be compared to a plain vanilla European call option on  the S&P 500 with a strike set at the index start level and an expiry of the option on 15  September 2003. The option value is also modified with the rescaling factor. The option  payoff is defined as:

# Max (St - Et, 0).

At expiry, the option payoff is either the difference between the value at expiry and the  strike level or zero. This implies that the note is worth the greater of the value of the  original [investment](../../Advanced%20Investments/An%20Asset%20Allocation%20Primer.md) (floor or guaranteed part) or the original [investment](../../Advanced%20Investments/An%20Asset%20Allocation%20Primer.md) plus the value of  the call option depending on where the index finishes of at expiry relative to the strike. The  payoff and the structure of this instrument can also be viewed similarly to the structure of a  1 plain vanilla convertible bond . It is interesting to note that the investor is effectively
paying the forgone income from the bond to purchase the call option. To put it differently,  the effective cost of the call is the income forgone on the funds invested. This income  forgone can be stated as the interest income  on the equivalent bullet bond issued by the  same issuer, which has a similar credit rating and maturity.

Figure 2 sets out the essential structural design of the principal protected note in a general  framework.

 ![500](Attachments/500-466.jpg)

# Figure 2

The decision by the issuer to market such a product is motivated by the opportunity of  raising funds at a lower rate via the structured product than issuing a traditional bullet  bond.  However, the issuer assumes a final redemption risk as it has an exposure to the  level of the S&P 500 index at maturity. This risk can simply be hedged through the  purchase of a European style call option with the same terms as the embedded option.   From the issuer’s point of view, the economic basis of the issue/note is the differential  value placed on the equity index call option by the investor (the purchaser of the option or  2 the bond holder) and the writer of the call option .

# Variable Participation Structures

The level of participation relative to the face value of the bond can also vary. In the  standard structure the participation level is set at a   $100\%$   of the index increase, but can also  be below   $100\%$  , above  $100\%$  , or can be capped to a certain level. The level of participation  will depend on whether the forgone income is sufficient to engineer the degree of exposure  to the underlying index. In addition, the guaranteed principal may also be less than  $100\%$  .  In this case, the investor may be prepared to utilise a portion of the principal to purchase  the required option. Below we note an example of how the cost of the option premium can  be engineered to produce a lower premium if the forgone income from the bond is  insufficient to finance the option.

Capped participation level  This is where the note principal is   $100\%$   guaranteed and where the participation level is   $100\%$  . In cases where the coupon available is insufficient to meet the amount of option  premium required, one method for reducing the option premium is through the use of an  option spread. This entails the purchase of a call option at a strike level set at-the-money
and the sale of a call option at a strike level that is out of the money. The premium received  for the second option effectively lowers the option cost that allows the net premium to be  funded from the available coupon.

Figure 3 sets out the return profile of a principal protected capped return equity index  linked note.

 ![500](Attachments/500-465.jpg)

# Figure 3

The issuer may also introduce a note that does not pay or guarantee   $100\%$   of the principal  but allows the investor to get1  $00\%$   return on the index appreciation. This is another  method of engineering sufficient funds to finance the [call premium](../Derivatives/Part%20IV%20-%20Options/Chapter%2017%20-%20Option%20Strategies.md).

Investors have also purchased structures with embedded [exotic](../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%206%20Options%20on%20Non-Price%20Variables/Exotic%20Interest%20Rate%20Options.md) options. For example, a  security may incorporate a payoff linked not just to the single closing value of the index on  a particular date, but also to the average closing values of the index on a series of dates.  This type of option is known as an  Asian  option. To see an example of a security with such  a payoff feature, type:   $\mathbf{EC4143078<}\mathbf{COR}\mathbf{P}\mathrm{>}\mathbf{D}\mathbf{E}\mathbf{S}\mathrm{<}\mathbf{G}\mathbf{O}\mathrm{>}$    on the Bloomberg system   to  pull out a equity linked zero coupon bond that matures on 27 June 2008 and has been  issued by the First Union National Bank. Users should then type,   ${\bf5}\!<\!{\bf g0}^{>}$    from the DES  page to see the redemption formula. Note that the payoff of the security payoff is only  $80\%$    of any increase in the index (in this case the Nasdaq 100 index). The final valuation dates  are given on the next page. The value of the option on maturity is given by the average  closing values on specified dates.

The redemption formula is shown at figure 4, the Bloomberg page DES for this security.
 ![500](Attachments/500-468.jpg)

# Figure 4

Other [exotic](../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%206%20Options%20on%20Non-Price%20Variables/Exotic%20Interest%20Rate%20Options.md) embedded options such as  quanto  options are also issued. With these, the  investor receives a return linked to the performance of an equity index denominated in a  different [currency](../../Financial%20Instruments/Lecture%20Notes-%20Financial%20Instruments/Teaching%20Note%201-%20Forward%20Rates%20Agreement/Forwards%20and%20Futures%20Notes.md) to that of the [currency](../../Financial%20Instruments/Lecture%20Notes-%20Financial%20Instruments/Teaching%20Note%201-%20Forward%20Rates%20Agreement/Forwards%20and%20Futures%20Notes.md) of the bond. For example, this might be a note  denominated in US dollars which is linked to the performance of the Nikkei 225 index.  The investor's principal is guaranteed and the return is asymmetric. The structure is made  up of a combination of a fixed interest security and the quanto call option. The major  feature of this type of option is that is designed to primarily to have a [principal amount](../../Financial%20Instruments/Financial%20Derivatives%20and%20Quantitative%20Methods/HSBC-Auto%20callable%20Barrier%20Notes%20with%20Step-up%20Premium.md) or  face value that is linked to a market variable. In this case, the call option on the Nikkei  option is quantoed to enable any positive return on the option (resulting from the  appreciation of the index) to be converted at a pre-agreed USD/YEN exchange rate. This  quantity adjusting feature of the option allows the yen denominated increases in the  underlying index to be captured in USD terms.  To examine a security which has such a  payoff on the Bloomberg, type:   EC2243102  $\Leftarrow$  CORP> DES <GO>.

Users of the Bloomberg can value a [fixed income](../../Fixed%20Income%20Asset%20Pricing/Lecture%20Notes%20Bonds,%20%20Preferred%20Stock,%20%20and%20Structured%20Products.md) security with any embedded option type  as an integrated product, by means of the OVX function. This allows users to determine  the theoretical value of an equity linked note by valuing both the [fixed income](../../Fixed%20Income%20Asset%20Pricing/Lecture%20Notes%20Bonds,%20%20Preferred%20Stock,%20%20and%20Structured%20Products.md)/guaranteed  and the option component separately on a single screen.

For example, consider one of the securities introduced above by selecting on the  Bloomberg system the following:

# EC2243102 <CORP  $>$   DES <GO>.

Type again  OV  $\mathbf{X}\!<\!\!\mathbf{G}\mathbf{O}\!>$     to determine the theoretical value of the bond. This page is  shown as figure 5.
 
 ![](Attachments/85e6d38da927ee4f6d764f0ecc6f1cc2afc0f9f7f433f9171cc0157ad5dda34c.jpg)
 
![[https://cdn-mineru.openxlab.org.cn/model-mineru/prod/85e6d38da927ee4f6d764f0ecc6f1cc2afc0f9f7f433f9171cc0157ad5dda34c.jpg]]

# Figure 5

The screen defaults to calculate the total value/premium of the bond but also calculates  each component separately. Users can therefore see the [fixed income](../../Fixed%20Income%20Asset%20Pricing/Lecture%20Notes%20Bonds,%20%20Preferred%20Stock,%20%20and%20Structured%20Products.md) bond value and the  option premium. Given that there is a market price available for the bond, one can observe  how far the theoretical value is from the market price. The option components can be seen  by typing   $1\mathrm{<}\mathrm{go>}$  . To see all the input parameters that is fed into the model such as the  volatility level and dividend yield, type  $4\!<\!\mathrm{geo}^{>}$  . Inputs are user-determined and can be  altered as required. For example, one can change the participation level or change the  structure of the equity exposure such that the security is linked a basked of indices instead  of a single index.

Equity-linked notes are commonly used by commercial banks and retail finance houses to  attract private sector funds that increasingly seek greater risk/return profiles but with an  element of guarantee built in. The issuers invariably hedge their exposure to the stock or  index that the note is linked, using [exotic](../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%206%20Options%20on%20Non-Price%20Variables/Exotic%20Interest%20Rate%20Options.md) options bought from [investment](../../Advanced%20Investments/An%20Asset%20Allocation%20Primer.md) banks.
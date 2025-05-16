---
tags:
  - black_model
  - caps_and_floors
  - interest_rate_derivatives
  - option_pricing
  - risk_neutral
aliases:
  - Black-Scholes Approach
  - Caps and Floors Pricing
  - Interest Rate Derivatives
key_concepts:
  - Black-Scholes model
  - Caps and floors
  - Floating rate borrowers
  - Interest rate derivatives
  - Option payoff structure
  - Over-the-counter market
  - Risk neutral representation
---

# Interest Rate Derivatives-An Introduction to the  Pricing of Caps and Floors
# Abstract

This article introduces the basic structure and engineering of [interest rate derivative](../../Clippings/Interest%20Rate%20Derivatives.md)  instruments, which are products whose payoffs depend in some way on the level of  [interest rates](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%202/Interest%20Rate%20Quotations.md). These [financial instruments](../../Financial%20Instruments/A%20Practical%20Guide%20for%20Actuaries%20and%20other%20Business%20Professionals..md) include caps, [floors](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%2016/Caps%20and%20Floors.md), swaptions and options  on coupon-paying bonds. The most common way to price interest rate [derivatives](../../Financial%20Markets/Financial%20Trading%20and%20Markets/Chapter%209%20Arbitrage%20and%20Hedging%20With%20Options.md)  such as [caps and floors](.md), is to adopt the [Black-Scholes approach](.md) and to implement the  Black (1976) [pricing](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%207/Arbitrage%20Pricing%20of%20Derivatives.md) model. Following an [introduction](../../Financial%20Markets%20and%20Institutions/III.%20Liquidity%20of%20Assets/Class%209-%20Bailouts%20and%20Bank%20Failures/Squam%20Lake%20Group%20Introduction.md) to the structure of interest rate  [derivatives](../../Financial%20Markets/Financial%20Trading%20and%20Markets/Chapter%209%20Arbitrage%20and%20Hedging%20With%20Options.md), we also present the underlying [risk neutral representation](.md) of the Black  model in order to derive the existing closed form solution. In fact, the model is very  intuitive and easy to implement for a single cap/floor. When [pricing](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%207/Arbitrage%20Pricing%20of%20Derivatives.md) a [portfolio](../../Advanced%20Investments/An%20Asset%20Allocation%20Primer.md) of  caplets/floorlets however, with multiple expiry dates, one may need to use  sophisticated analytics written in higher programming languages for computational  speed and efficiency.

# Interest-rate caps and floors

Interest rate options are widely used to either speculate on the future course of interest  rates or to hedge the interest payments or receipts on an underlying position. The  advantage of these instruments over other types of [derivatives](../../Financial%20Markets/Financial%20Trading%20and%20Markets/Chapter%209%20Arbitrage%20and%20Hedging%20With%20Options.md) such as swaps and  [interest rate futures](../Derivatives/Part%20III%20-%20Fixed%20Income%20Futures%20Contracts/Chapter%2012%20-%20Hedging%20with%20Interest%20Rate%20Futures.md) is that interest options allow an investor to benefit from changes  in [interest rates](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%202/Interest%20Rate%20Quotations.md) while also limiting any downside losses. Hence, like all options they  provide insurance.

The [over-the-counter market](.md) trades options on a number of [interest rates](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%202/Interest%20Rate%20Quotations.md) relating to  short-term [financial instruments](../../Financial%20Instruments/A%20Practical%20Guide%20for%20Actuaries%20and%20other%20Business%20Professionals..md), such as bank deposits, certificates of deposit,  commercial paper, and T-bills. The most liquid options traded of all these are caps,  [floors](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%2016/Caps%20and%20Floors.md), and collars. Caps are interest rate option structures with a payout if interest  rates rise (this may also depend on the option style or exercise). Consequently, they  are used by [floating rate borrowers](.md) or issuers to ensure against a rise in [interest rates](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%202/Interest%20Rate%20Quotations.md).  [Floors](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%2016/Caps%20and%20Floors.md), on the hand, have a payoff for the user if [interest rates](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%202/Interest%20Rate%20Quotations.md) fall and, consequently,  are used by depositors/investors to insure against [interest rates](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%202/Interest%20Rate%20Quotations.md) falling. A collar is a  combination of the two while a [zero cost collar](../Derivatives/Part%20VII%20-%20Advanced%20Options/Chapter%2030%20-%20Other%20Options.md) can be constructed by taking opposite  position of the two options types, such that the strike prices are chosen so that the net  premium for the user is zero.

Consider the following example where a corporation has issued a floating-rate note or  a loan, paying interest semi-annually at six-month Libor  $+\ 0.50\%$  , with residual term  to maturity of 5 years and 3 months. You can effectively lock in the maximum level  of your future borrowing rate by buying a cap that consists of 10 half-year caplets,  starting in 3 month's time.

Generic representation of the payoff to a cap is given in Figure 1.1. The long option  position is a call if the underlying is an interest rate or an FRA; it is a put if the  underlying instrument is a future. The long-option position combined with the  unexpected effects of [interest rate changes](../../International%20Finance/Bridgewater/How%20Countries%20Go%20Broke/How%20Countries%20Go%20Broke-Chapter%2012%20to%20Chapter%2014.md) gives a payoff that resembles a long put  position on the interest rate – i.e. if [interest rates](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%202/Interest%20Rate%20Quotations.md) fall the borrower benefits from the  fall less the option premium, but if rates rise the interest rate payable on is capped.  The effective rate of interest on the capped loan will be the [exercise price](../../Financial%20Markets/Financial%20Asset%20Pricing%20Theory%20Overview/Chapter%2012%20-%20Derivatives/Options.md) of the  option plus the option premium and plus (minus) any reset margin above (below)  Libor. It is in fact very intuitive to see the payoff to the cap from the graph. The solid  thin line represents the [interest rate exposure](../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20III%20THE%20PLAYERS/Chapter%2013%20-%20Banks%20Asset-Liability%20Management/Duration%20Gap%20Management.md) to the issuer or a borrower of a floating  rate loan. The thin dotted line represents the long call option for [hedging](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%205/Key%20Rates%20O1s%20Durations%20and%20Hedging.md) the loan. The  payoff of the combined position is represented by the solid fat line, which shows the  offsetting effect of the positions for various interest rate scenarios.
 ![500](https://cdn-mineru.openxlab.org.cn/model-mineru/prod/44785c5e549601a118e900929a3ce157d1295a924a25ff41e14ad0d5de9c67b5.jpg)
Figure 1.1 Profit and Loss using a Long Call on FRA

# Caps and Floors payoffs

The pay off of the options can simply be described algebraically using the following  notation. Let  $K_{c}$    and  $K_{p}$   be the strike levels for the call and the put respectively while  $T$    is the [expiration date](../../Financial%20Instruments/Financial%20Derivatives%20and%20Quantitative%20Methods/Risk%20Neutral%20Pricing%20of%20Options.md) of the contract.

Caplet (pay off at maturity)    $\begin{array}{l}{{\displaystyle Q\{\mathrm{max},(0,L i b o r_{T}-K_{c})\frac{d a y s}{360}\}}}\\ {{\displaystyle Q\{\mathrm{max},(0,K_{P}-l i b o r_{T})\frac{d a y s}{360}\}}}\end{array}$  Floorlet (pay off at maturity)

The implication from the above algebrical representation of the payoffs at settlement  requires knowledge of the future course of the underlying rates, i.e. LIBOR. Since we  cannot realistically forecast the future course of an interest rate, it is natural to model  1 it as a random variable. Now, following the [Black-Scholes](../Mathematical%20Modeling%20of%20Derivative%20Pricing.md)  framework, the basic  assumption underlying option [pricing](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%207/Arbitrage%20Pricing%20of%20Derivatives.md) theory is the nonexistent of [arbitrage](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%207/Arbitrage%20Pricing%20of%20Derivatives.md), were the  word "[arbitrage](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%207/Arbitrage%20Pricing%20of%20Derivatives.md)" essentially addresses the opportunity to make a [risk-free profit](../../Financial%20Markets/Financial%20Asset%20Pricing%20Theory%20Overview/Chapter%203%20-%20%20Assets,%20Portfolios,%20and%20Arbitrage/Arbitrage.md). In  other words, the common saying that "there is no free lunch" is the fundamental  principal underlying the theory of finance. To make the ideas presented above more  concrete, we now begin a formal treatment of the [stochastic process](../../The%20Ornstein-Uhlenbeck%20(OU)%20Process.md) of interest rate.

Let us suppose that the interest rate   $r$    follows [Brownian Motion](../../Financial%20Markets/Financial%20Asset%20Pricing%20Theory%20Overview/Chapter%202%20-%20Uncertainty,%20Information,%20and%20Stochastic%20Processes/Continuous-Time%20Stochastic%20Processes.md) described by a  [stochastic differential equation](Implementing%20Heath,%20Jarrow%20&%20Merton%20(HJM)%20Model.md) of the form$$
d r_{t}=u(t,r_{t})d t+\sigma(t,r_{t})d W_{t}
$$

where   $u(t,r_{t})$  and   $\sigma(t,r_{t})$    the expected value and the standard deviation of the  instantaneous interest rate variation, respectively. The price at date  $t$    of a zero-coupon  bond maturing at date   $T>t$    is a function of the short term interest rate
$$
B(t,T)=B(t,T,r)\,.
$$
  .

Finally, the prices of zero-coupon bonds are derived by using an approach based on a  parabolic partial differential equation (PDE). From the PDE approach and applying  2 [Ito's lemma](../Determining%20the%20Stochastic%20Process%20for%20a%20Forward%20Contract%20from%20Ito’s%20Lemma.md)  to equation (2) and using
$$
d r_{t}=u(t,r_{t})d t+\sigma(t,r_{t})d W_{t}
$$

one gets
$$
d B=[\frac{\delta B}{\delta t}+\frac{\delta B}{\delta r}u+{\scriptstyle\frac{1}{2}}\sigma^{2}\,\frac{\delta^{2}B}{{\delta r}^{2}}]d t+\frac{\delta B}{\delta r}\sigma d W_{t}
$$
$$
=u_{_B}B d t+\sigma B d W_{_t}\,.
$$

We now set up a riskless [portfolio](../../Advanced%20Investments/An%20Asset%20Allocation%20Primer.md):   $P=B_{1}+\Phi B_{2}$    involving two zero-coupon bonds,  described as
$$
\begin{array}{l}{B_{1}=B(t,T_{1},r)}\\ {B_{2}=B(t,T_{2},r)\,.}\end{array}
$$
 .

Selecting the position   $\Phi$     in the second bond which renders the [portfolio](../../Advanced%20Investments/An%20Asset%20Allocation%20Primer.md) to be riskless,  we find the following condition:
$$
\frac{\delta B_{1}}{\delta r}+\Phi\,\frac{\delta B_{2}}{\delta r}=0\,.
$$

The net effect of the change of the [portfolio](../../Advanced%20Investments/An%20Asset%20Allocation%20Primer.md) is equal to zero. We can determine the  appropriate value of the position in the second bond by simply rearranging the  equation (7), from which we get
$$
\Phi=-\frac{\delta B_{1}}{\delta r}\nearrow\frac{\delta B_{2}}{\delta r}\,.
$$
 .

3 This can also be interpreted as the ratio of the sensitivities to the risk variable . We  can now express the change of the [portfolio](../../Advanced%20Investments/An%20Asset%20Allocation%20Primer.md) in a time  dt  as$$
d\Pi=[{\frac{\delta B_{1}}{\delta t}}+{\frac{\delta B_{1}}{\delta r}}u+{\frac{\i}{2}}\sigma^{2}\,{\frac{\delta^{2}B_{1}}{\delta r^{2}}}]d t+\Phi[{\frac{\delta B_{2}}{\delta t}}+{\frac{\delta B_{2}}{\delta r}}u+{\frac{\i}{2}}\sigma^{2}\,{\frac{\delta^{2}B_{2}}{\delta r^{2}}}]d t
$$

Now, since the [portfolio](../../Advanced%20Investments/An%20Asset%20Allocation%20Primer.md) is riskless, it should have a return equal to the [risk-free rate](../../Financial%20Instruments/Black%20Scholes%20Derivation.md).
$$
\frac{d\Pi}{\Pi}=r d t
$$

4 or equivalently
$$
d\Pi=[{\frac{\delta B_{1}}{\delta t}}+{\frac{\delta B_{1}}{\delta r}}u+{\frac{_{1}}{2}}\sigma^{2}\,{\frac{\delta^{2}B_{1}}{\delta r^{2}}}]d t+\Phi[{\frac{\delta B_{2}}{\delta t}}+{\frac{\delta B_{2}}{\delta r}}u+{\frac{_{1}}{2}}\sigma^{2}\,{\frac{\delta^{2}B_{2}}{\delta r^{2}}}]d t=r(B_{1}+\Phi B_{2})
$$

The randomness in  d Π   will vanish since it makes the coefficient of   $d r$    zero. If we  assume the non existence of [arbitrage](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%207/Arbitrage%20Pricing%20of%20Derivatives.md), the [portfolio](../../Advanced%20Investments/An%20Asset%20Allocation%20Primer.md) must have a rate of return equal to  the [short rate](../../Fixed%20Income%20Asset%20Pricing/Fixed%20Income%20Lecture%20Notes/An%20Overview%20of%20the%20Vasicek%20Short%20Rate%20Model.md) of interest. Finally, using equation (8) and rearranging the above  equation, we have
$$
\frac{\displaystyle\frac{\partial B_{1}}{\partial t}+\frac{\partial B_{1}}{\partial r}u+\frac{1}{2}\sigma^{2}\,\frac{\delta^{2}B_{1}}{\delta r^{2}}-r B_{1}}{\displaystyle\frac{\partial B_{1}}{\partial r}}=\frac{\displaystyle\frac{\partial B_{2}}{\partial t}+\frac{\partial B_{2}}{\partial r}u+\frac{1}{2}\sigma^{2}\,\frac{\delta^{2}B_{2}}{\delta r^{2}}-r B_{2}}{\displaystyle\frac{\delta B_{2}}{\delta r}}
$$

Hence the quantity (the same as the above equation except that we have divided by   $\sigma$  )
$$
\lambda=\lambda(t,r_{t})=\frac{\displaystyle{\frac{\delta B}{\delta t}+\frac{\delta B}{\delta r}u+{\scriptstyle{\frac{1}{2}}}\sigma^{2}\,\frac{\delta^{2}B}{\delta r^{2}}-r B}}{\displaystyle{\frac{\delta B}{\delta r}\sigma}}
$$

is a constant across all obligations at a given date. That is to say, the price of risk is  constant. Dividing the numerator and denominator by  $B$    in equation (11), we get
$$
\lambda=\frac{u_{\scriptscriptstyle B}-r}{\displaystyle\frac{1}{B}\frac{\delta B}{\delta r}\sigma}
$$

or equivalently
$$
u_{B}-r=\lambda\sigma_{B}
$$

Equation (12) can be interpreted as the access return (the return on a bond above the  [risk-free rate](../../Financial%20Instruments/Black%20Scholes%20Derivation.md)) is equal to   $\lambda$    times a factor measuring the risk (volatility) of the bond.  Hence,   $\lambda$    can be interpreted naturally as the market price (interest rate) of risk.
It follows that the values of any securities that are sensitive to the change of the  interest rate  $r$    satisfies the partial-differential equation:
$$
\frac{\delta B}{\delta t}+\frac{\delta B}{\delta r}\,u+{\scriptstyle\frac{1}{2}}\sigma^{2}\,\frac{\delta^{2}B}{\delta r^{2}}-r B=\frac{\delta B}{\delta r}\sigma\lambda
$$

or
$$
\frac{\delta B}{\delta t}+\frac{\delta B}{\delta r}(u-\lambda\sigma)+{\scriptstyle{\frac{1}{2}}}\sigma^{2}\,\frac{\delta^{2}B}{\delta r^{2}}-r B=0
$$

The stochastic model for the [spot rate](../../International%20Finance/The%20Foreign%20Exchange%20Market%20Annotations.md) presented above allows us to value contingent  claims such as bond options. In our analysis we can price caps and floor by solving  equation (14) with the boundary condition   $B(T,T,r)=1$  .

The result from equation (14) is a modified version of the original [Black-Scholes](../Mathematical%20Modeling%20of%20Derivative%20Pricing.md)  solution for [pricing derivatives](../../Pricing%20Forwards,%20Futures,%20Bonds,%20Swaps,%20Swaptions,%20Caps%20and%20Floors%20under%20No-Arbitrage%20and%20Risk-Neutral%20Pricing.md) via [risk neutral](../../Financial%20Instruments/Lecture%20Notes-%20Financial%20Instruments/Teaching%20Note%207-Exotic%20Options%20And%20Derivative%20Pricing%20By%20Monte%20Carlo%20Simulation.md) technique. This solution is the most  elegant result for [pricing derivatives](../../Pricing%20Forwards,%20Futures,%20Bonds,%20Swaps,%20Swaptions,%20Caps%20and%20Floors%20under%20No-Arbitrage%20and%20Risk-Neutral%20Pricing.md) as it provides neat and incredible mathematical  solution to a complicated issue that incorporates investor risk. In fact one of the  crucial aspect of the model is based on its assumption on [complete markets](../Financial%20Mathematics%20Course.md). This  implies that that all [derivatives](../../Financial%20Markets/Financial%20Trading%20and%20Markets/Chapter%209%20Arbitrage%20and%20Hedging%20With%20Options.md) can be priced via [replication](../../Financial%20Instruments/Financial%20Derivatives%20and%20Quantitative%20Methods/Forward%20and%20Futures%20Contracts.md) strategy and it further  assumes that the appropriate securities to create the replicate position always exist.  Under this scenario, the return from the hedged or the replicated position should yield  the risk free rate and the risk premium required by investors is solved via the above  partial-differential equation. In fact, you can see this by rearranging the equation and  taking the   $-r B$   to the right hand side and equate this to the change of the [portfolio](../../Advanced%20Investments/An%20Asset%20Allocation%20Primer.md).

Having derived the general bond [pricing](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%207/Arbitrage%20Pricing%20of%20Derivatives.md) and risk-neutral framework, one can solve  equation (14) while using the [boundary conditions](../Appendices/Appendix%2021.C%20Solutions%20for%20Black-Scholes%20PDE.md) to arrive the Black-76 closed-from  5 solution to price interest options such caps/floor, and bond option . For caps and  [floors](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%2016/Caps%20and%20Floors.md), we will use the implied [forward rate](../../Clippings/Forward%20Points%20in%20Currency.md)   $F,$  ,  at each caplet maturity as the  [underlying asset](../../Financial%20Instruments/Financial%20Derivatives%20and%20Quantitative%20Methods/Risk%20Neutral%20Pricing%20of%20Options.md). We assume also that underlying forward rates follow lognormal  process. The price of the cap is simply the sum of the price of the caplets that make up  the cap. Similarly, the value of a floor is the sum of the sequence of individual put  options, these are often called floorlets.
$$
C a p=\sum_{i=1}^{n}C a p l e t_{i}\qquad\qquad\qquad\qquad F l o o r=\sum_{i=1}^{n}F l o o r l e t_{i}
$$

where
$$
C a p l e t=\frac{N o t i o n a l\cfrac{d}{B a s i s}}{(1+F\cfrac{d}{B a s i s})}e^{-r(T-t)}[F N(d_{1})-X N(d_{2})]
$$$$
F l o o r l e t=\frac{N o t i o n a l\displaystyle\frac{d}{B a s i s}}{(1+F\displaystyle\frac{d}{B a s i s})}e^{-r(T-t)}[X N(-d_{2})-F N(-d_{1})]
$$

and
$$
d_{1}={\frac{\ln(F/X)+(\sigma^{2}/2(T-t)}{\sigma{\sqrt{T-t}}}}\qquad\quad d_{2}=d_{1}-\sigma{\sqrt{T-t}}
$$

The term   $d$    is the number of days in the forward period .  Basis  is the number of days  in the year used in the market, and the term  $N(.)$   is the cumulative normal distribution.  Note that the [risk-free interest rate](../../Financial%20Markets/Financial%20Asset%20Pricing%20Theory%20Overview/Chapter%2012%20-%20Derivatives/Exercises.md) does not enter the equation for   $d_{\scriptscriptstyle1}$   and   $d_{2}$    because  the influence of the [risk-free rate](../../Financial%20Instruments/Black%20Scholes%20Derivation.md) on the future values of the [underlying asset](../../Financial%20Instruments/Financial%20Derivatives%20and%20Quantitative%20Methods/Risk%20Neutral%20Pricing%20of%20Options.md) in a riskneutral world is already accounted for in the [forward price](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%2011/Forward%20Contracts%20and%20Forward%20Prices.md). Now, you can easily  implement this model by simply plugging in the input parameters such as, a value for  the [underlying asset](../../Financial%20Instruments/Financial%20Derivatives%20and%20Quantitative%20Methods/Risk%20Neutral%20Pricing%20of%20Options.md), strike level, number of days in the forward period and year. Most  importantly, you will need to assume a value for the volatility parameter. Once these  values are entered, the value of a cap or floor can easily be determined.

To implement the model described above and generate a numerical values, we will  use the Bloomberg Professional Analytics as our [pricing](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%207/Arbitrage%20Pricing%20of%20Derivatives.md) tool of choice. The  Bloomberg cap/floor/collar [pricing](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%207/Arbitrage%20Pricing%20of%20Derivatives.md) capabilities has become market standard among  various market players such as derivative traders, sales, and risk managers. Use of  these analytics creates transparency and helps market practitioners assess risk and  execute trades very easily. To continue our discussion, we analyse 5 year cap on a 3  month LIBOR. Figure 1.2. displays the value of the caplets expressed as a percentage  of face amount as well as the market value in nominal terms.

We illustrate the form for [pricing](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%207/Arbitrage%20Pricing%20of%20Derivatives.md) the caplet on the Bloomberg system. This is done by  selecting the function BCCF   $<\!\mathrm{go}^{>}$   and then entering the following parameters:  settlement date, start date and [expiration date](../../Financial%20Instruments/Financial%20Derivatives%20and%20Quantitative%20Methods/Risk%20Neutral%20Pricing%20of%20Options.md) and the face amount of the contract.  Volatility and strike(s) are crucial parameters to the model and will have tremendous  effect on the cost of the option depending on whether you wish to price the option on  a flat or varying strike and volatility levels. Enter a single volatility and strike for all  maturities or simply page forward to the second page and enter unique strike and  volatility levels for each caplet components. Once you have entered the strike(s), you  will immediately see the intrinsic value of the option visually from the graph on the  first page. The red horizontal line and the white steep curve display the strike level  6 and the implied forward  rate respectively.
 ![500](https://cdn-mineru.openxlab.org.cn/model-mineru/prod/29a9d228cf43837cf0fa03358db9dcbb6856374f2a1c2c6048818dc440b2de9f.jpg)

# Figure 1.2.  Bloomberg Cap/Floor/Collar Valuation Screen: BCCF <go>

The selected flat option strike level of 3.501 is in fact higher then the implied forward  rate until approximately 12/27/04 but it is lower after this date until the expiry of the  last option. So, from the point of view of intrinsic value, the option is out-of-the  money until December 2004 and in-the-money from March 2005 until the last  [expiration date](../../Financial%20Instruments/Financial%20Derivatives%20and%20Quantitative%20Methods/Risk%20Neutral%20Pricing%20of%20Options.md).  We use the models default cap/floor implied vol at ili ties and get an  option premium of:
$$
C a p=\sum_{i=1}^{n}C a p l e t_{i}=5.0781\%
$$

and corresponding market value of
$$
(\frac{5.0781}{100})x1,\!000,\!000=50781.00
$$

To see the impact of the cost of the option by simply changing a single parameter  input such as the strike level, increase the strike by for example one percentage point  and you will price the option cheaper. To demonstrate the computational speed of the  model, change the calculator option to solve for the [implied volatility](../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%205%20Options%20on%20Prices%20and%20Hedge-Based%20Valuation/A%20Real-Life%20Option%20Pricing%20Exercise.md) by entering  specific premium level. Through iterative process the model will work out the correct  immediately [implied volatility](../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%205%20Options%20on%20Prices%20and%20Hedge-Based%20Valuation/A%20Real-Life%20Option%20Pricing%20Exercise.md) given an option premium.
Page three of the Bloomberg Cap/Floor/Collar [pricing](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%207/Arbitrage%20Pricing%20of%20Derivatives.md) screen BCCF provides detailed  information such as each expiry dates of the option components, vol at ili ties, implied  forward rates, deltas, and the option component values. This is shown at figure 1.3.

 ![500](https://cdn-mineru.openxlab.org.cn/model-mineru/prod/3ea86aea34e696ff176d11274d3604c4c8d28412cf3e5ce53e5cfaaa2fac0109.jpg)

# Figure 1.3.  Bloomberg Cap/Floor/Collar Valuation Screen: BCCF <go>

Now, once the premium is computed, it must also be discounted back to time zero  using the [forward rate](../../Clippings/Forward%20Points%20in%20Currency.md) consistent to the expiry of the contract. Bloomberg's  cap/floor/collar analytics is a powerful tool to price these contracts and requires  minimum model required inputs as it will also compute the [implied forward rates](../../Financial%20Instruments/Lecture%20Notes-%20Financial%20Instruments/Teaching%20Note%201-%20Forward%20Rates%20Agreement/Forwards%20and%20Futures%20Notes.md)  applicable for different expiry dates for the option.

# Estimating volatility

The estimation of volatility is of course central to the [pricing](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%207/Arbitrage%20Pricing%20of%20Derivatives.md) options.  Specifically,  the volatility of [returns](../../Financial%20Markets/Financial%20Asset%20Pricing%20Theory%20Overview/Chapter%203%20-%20%20Assets,%20Portfolios,%20and%20Arbitrage/Assets.md) from today until the maturity of the option is required. The  [black model](../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%206%20Options%20on%20Non-Price%20Variables/Black%20Models%20for%20Bond%20Price%20Options%20Capsfloors.md) assumes constant volatility over this period, unlike the stochastic  volatility and some of the numerical models. The most common approaches in  estimating vol at ili ties is to adopt either of the following techniques:

  To assume volatility is stationary, and to calculate historical volatility
  To model volatility based upon historic information to provide a forecast using  7 models such as ARCH (Auto regressive Conditional Heteros ke d asti city)

   To imply volatility from other options already trading in the market place

The latter approach suggests a circular argument, namely deriving the volatility from  existing options. It can however act as an extremely useful check on where other  participants see volatility, but must be interpreted carefully.

This is precisely what is referred to in most academic literatures as the market  expectation of [future rate](../../Clippings/Forward%20Rate.md) changes. Many option markets that are highly liquid, for  example at-the-money USD and GBP cap markets, will quote vol at ili ties rather than  option prices. This is because all the [pricing](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%207/Arbitrage%20Pricing%20of%20Derivatives.md) parameters required for the [black model](../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%206%20Options%20on%20Non-Price%20Variables/Black%20Models%20for%20Bond%20Price%20Options%20Capsfloors.md)  are available elsewhere such as in the swap market. Therefore volatility is the only  unknown parameter.

 ![500](https://cdn-mineru.openxlab.org.cn/model-mineru/prod/135dfa776ce8d474df7fb081484b0dcc4a76239a8e1dcc79faf2c165417f305a.jpg)

# Figure 1.4.  Bloomberg Cap/Floor Implied volatility surface

An excellent knowledge of [implied volatility](../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%205%20Options%20on%20Prices%20and%20Hedge-Based%20Valuation/A%20Real-Life%20Option%20Pricing%20Exercise.md) in terms of future [expectations](../../Fixed%20Income%20Asset%20Pricing/Fixed%20Income%20Lecture%20Notes/FORWARD%20RATES%20AND%20TERM%20STRUCTURE.md) for future  price or rate variability allows one a better way to assess his/her exposure to market  risk. Knowing how changing volatility affect [hedging](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%205/Key%20Rates%20O1s%20Durations%20and%20Hedging.md) and [pricing](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%207/Arbitrage%20Pricing%20of%20Derivatives.md) will be crucial for  the development of a cost-effective hedges and weigh up the timing risks coupled  with a particular strategy.

It is also a common practise to use volatility surfaces, i.e. a matrix of (strike vs.  forward start date), when [pricing](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%207/Arbitrage%20Pricing%20of%20Derivatives.md) and [valuing caps and floors](../../Course%20Notes/Python/QuantLib-Python/Valuing%20Interest%20Rate%20Caps%20and%20Floors%20Using%20QuantLib%20Python.md). This allows the smile  effect to be incorporated. The data used in figure 1.4 can be accessed or easily  downloaded from the Bloomberg in order to generate three dimensional volatility  surfaces and smiles to help one identify miss-priced options.
# Appendix: Itô’s Lemma

In finance, when using continues-time models, it is common to assume that the price  of an asset is an Ito's process. Therefore, to derive the price of a financial derivative,  one needs to use Ito's calculus. In this section, we briefly review [Ito's lemma](../Determining%20the%20Stochastic%20Process%20for%20a%20Forward%20Contract%20from%20Ito’s%20Lemma.md) by  treating it as a natural extension of the differentiation in calculus. [Ito's lemma](../Determining%20the%20Stochastic%20Process%20for%20a%20Forward%20Contract%20from%20Ito’s%20Lemma.md) is the  basis of [stochastic calculus](../6.%20A%20Brief%20Introduction%20to%20Stochastic%20Calculus.md).

# Review of Differentiation

Let   $G(x)$    be differentiable function of  $x$  .  Using Taylor expansion, we have
$$
\Delta G\equiv G(x+\Delta x)-G(x)=\frac{\delta G}{\delta x}\Delta x+\frac{1}{2}\frac{\delta^{2}G}{\delta x^{2}}(\Delta x)^{2}+\frac{1}{6}\frac{\delta^{3}G}{\delta x^{3}}(\Delta x)^{3}+.......\,.
$$

Taking the limit as   $\Delta x\rightarrow0$   and ignoring the higher order terms of ,  we have
$$
d G={\frac{\delta G}{\delta x}}d x.
$$

When  $G$    is a function of  $x$    and  $y.$  ,  we have
$$
\Delta G=\frac{\delta G}{\delta x}\Delta x+\frac{\delta G}{\delta y}\Delta y+\frac{1}{2}\frac{\delta^{2}G}{\delta x^{2}}(\Delta x)^{2}+\frac{\delta^{2}G}{\delta x\delta y}\Delta x\Delta y+\frac{1}{2}\frac{\delta^{2}G}{\delta y^{2}}(\Delta y)^{2}+.......
$$

Taking the limit as   $\Delta x\rightarrow0$    and as   $\Delta y\to0$  ,  we have
$$
d G=\frac{\delta G}{\delta x}d x+\frac{\delta G}{\delta y}d y.
$$

To turn in the case in which  $\mathrm{G}$   is a differentiable function of   $x_{t}$  and  $t,$  ,  and   $x_{t}$  is an Ito's  process. The Taylor expansion becomes
$$
\Delta G=\frac{\delta G}{\delta x}\Delta x+\frac{\delta G}{\delta t}\Delta t+\frac{1}{2}\frac{\delta^{2}G}{\delta x^{2}}(\Delta x)^{2}+\frac{\delta^{2}G}{\delta x\delta t}\Delta x\Delta t+\frac{1}{2}\frac{\delta^{2}G}{\delta t^{2}}(\Delta t)^{2}+.......
$$

# Selected Bibliography and References

Abken, Peter A. "[Interest Rate Caps](../Derivatives/Part%20IX%20-%20Fixed%20Income%20Derivatives/Chapter%2038%20-%20T-Bond%20Option,%20Caps,%20Floors%20and%20Collar.md), Collars and [Floors](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%2016/Caps%20and%20Floors.md)."  Economic Review ,  Federal Reserve Bank of Atlanta 74 (November-December, 1989), pp.2-25  Black, F & Scholes, M 1973 “The [pricing](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%207/Arbitrage%20Pricing%20of%20Derivatives.md) of options and corporate liabilities”  Journal of Political Economy

#  www.YieldCurve.com 2003
Yaksick, Rudy. "Swaps, [Caps and Floors](.md): Some Parity and Price Identities."  The Journal of Financial Engineering  1 (June, 1992), pp.105-115.  Bjork, Tomas,  [Arbitrage Theory](../Financial%20Mathematics%20Course.md) in Continuous Time . Oxford: Oxford  University Press 1998  Clewlow, Les and Chris Strickland.  Implementing [Derivatives](../../Financial%20Markets/Financial%20Trading%20and%20Markets/Chapter%209%20Arbitrage%20and%20Hedging%20With%20Options.md) Models ,  Chichester, U.K.: John Wiley 1998  Haug, Espen Gaarder.  The Complete Guide to Option [Pricing](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%207/Arbitrage%20Pricing%20of%20Derivatives.md) Formulas . New  York: McGraw-Hill 1997  Hull, John C.  Options, [Futures](../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%203%20-%20Futures%20Markets/Futures%20Not%20Subject%20to%20Cash-And-Carry.md) and other [Derivatives](../../Financial%20Markets/Financial%20Trading%20and%20Markets/Chapter%209%20Arbitrage%20and%20Hedging%20With%20Options.md) , 4th. ed. Inglewood  Cliffs, New Jersey: Prentice-Hall 2000   Jarrow, Robert A.  Modelling [Fixed Income Securities](../../Clippings/Bond%20Equivalent%20Yield%20(BEY)%20-%20Definition,%20Formula,%20and%20Example.md) and Interest Rate  Options . New York: McGraw-Hill 1996  Pliska, Stanley R.  [Introduction](../../Financial%20Markets%20and%20Institutions/III.%20Liquidity%20of%20Assets/Class%209-%20Bailouts%20and%20Bank%20Failures/Squam%20Lake%20Group%20Introduction.md) to Mathematical Finance: Discrete Time  Models.  Malden, Mass.: Blackwell 1997  Prisman, Eliezer Z.   [Pricing](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%207/Arbitrage%20Pricing%20of%20Derivatives.md) [Derivative Securities](../Financial%20Mathematics%20Course.md) .  San Diego: Academic  Press 2000  Wilmott, Paul.  [Derivatives](../../Financial%20Markets/Financial%20Trading%20and%20Markets/Chapter%209%20Arbitrage%20and%20Hedging%20With%20Options.md): The Theory and Practice of Financial  Engineering . New York: Wiley 1999  Wilmott, Paul, Sam Howison and Jeff DeWynne.  The Mathematics of  [Financial Derivatives](../../Financial%20Instruments/Financial%20Instruments%20PSET%20Solutions.md): A Student [Introduction](../../Financial%20Markets%20and%20Institutions/III.%20Liquidity%20of%20Assets/Class%209-%20Bailouts%20and%20Bank%20Failures/Squam%20Lake%20Group%20Introduction.md) . Cambridge: Cambridge  University Press 1995  Tsay, Ruey S.   Analysis of Financial Time Series . Wiley, 2002
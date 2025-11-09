---
tags:
  - bond_pricing
  - convexity
  - duration
  - forward_rates
  - risk_premium
aliases:
  - Bond Return Decomposition
  - Forward Rate Decomposition
key_concepts:
  - Bond price and rate
  - Duration and convexity
  - Expected bond returns
  - Forward rate decomposition
  - Risk-neutral investors
---

# 8.3 AN ANALYTICAL DECOMPOSITION OF FORWARD RATES  

This section derives a general decomposition of forward rates in terms of. [expectations](../../../Fixed%20Income%20Asset%20Pricing/Fixed%20Income%20Lecture%20Notes/FORWARD%20RATES%20AND%20TERM%20STRUCTURE.md), [convexity](../../../Fixed%20Income%20Asset%20Pricing/Problem%20Sets/PSET%20II%20Fixed%20Income%20Asset%20Pricing%201.md), and risk premium. The level of mathematics here is higher than used in most of the book, but the discussion still aims at intuition.  

Assume that all bond prices are determined by the instantaneous rate, $r$ which takes on the value of. $r_{t}$ at time $t$ . Let $P_{t}(r_{t},T)$ be the price of a $T$ year zero coupon bond at time. $t$ . By [Ito's lemma](../../../Financial%20Engineering/Determining%20the%20Stochastic%20Process%20for%20a%20Forward%20Contract%20from%20Ito’s%20Lemma.md), a discussion of which is beyond. the scope of this book,  
$$
d P={\frac{\partial P}{\partial r}}d r+{\frac{\partial P}{\partial t}}d t+{\frac{1}{2}}{\frac{\partial^{2}P}{\partial r^{2}}}\sigma^{2}d t
$$  

where $d P,d r$ and $d t$ are the changes in price, rate, and time over the next instant, respectively, and $\sigma$ is the volatility of changes in $r$ . The two first-order. partial [derivatives](../../Financial%20Trading%20and%20Markets/Chapter%209%20Arbitrage%20and%20Hedging%20With%20Options.md) in Equation (8.9) denote the instantaneous change in the bond price for a unit change in the rate (with time unchanged) and for a unit change in time (with rate unchanged), respectively. Finally, the second order partial derivative in the equation gives the instantaneous change in $\partial P/\partial r$ (with time unchanged). Dividing both sides of (8.9) by price,  
$$
{\frac{d P}{P}}={\frac{1}{P}}{\frac{\partial P}{\partial r}}d r+{\frac{1}{P}}{\frac{\partial P}{\partial t}}d t+{\frac{1}{2}}{\frac{1}{P}}{\frac{\partial^{2}P}{\partial r^{2}}}\sigma^{2}d t
$$  

Equation (8.10) breaks down the instantaneous return on the zero. coupon bond into three components, but this decomposition can be written more intuitively by invoking several ideas from earlier chapters..  

First, in terms of instantaneous compounded forward rates, $f(t)$ , the price of a $T$ -year zero coupon bond is (from Section A2.1),  
$$
P=e^{-\int_{0}^{T}f(s)d s}
$$  

Then, differentiating both sides of (8.11) with respect to $t$ , recognizing that increasing $t$ decreases $T$ one-for-one,  
$$
{\frac{\partial P}{\partial t}}=-{\frac{\partial P}{\partial T}}=f(T)P
$$  

Second, by the definitions of [duration](../Chapter%205/Key%20Rates%20O1s%20Durations%20and%20Hedging.md), $D$ , and [convexity](../../../Fixed%20Income%20Asset%20Pricing/Problem%20Sets/PSET%20II%20Fixed%20Income%20Asset%20Pricing%201.md), C,  
$$
\begin{array}{l}{{\displaystyle{\cal D}\equiv-\frac{1}{{\cal P}}\frac{\partial{\cal P}}{\partial r}}~}\ {{\displaystyle~C\equiv\frac{1}{{\cal P}}\frac{\partial^{2}{\cal P}}{\partial r^{2}}}}\end{array}
$$  

Now, substituting Equations (8.12) through (8.14) into the return decomposition (8.10),  
$$
\frac{\partial P}{P}=f(T)d t-D d r+\frac{1}{2}C\sigma^{2}d t
$$  

Equation (8.15) gives the return decomposition in terms of the following three components. The first is the return due to the passage of time, which, in this case, is the [forward rate](../../../Clippings/Forward%20Points%20in%20Currency.md), $f(T)$ .1 The second and third components are [returns](../../Financial%20Asset%20Pricing%20Theory%20Overview/Chapter%203%20-%20%20Assets,%20Portfolios,%20and%20Arbitrage/Assets.md) due to changes in the rate. The second term says that increases in rate. reduce bond return in proportion to [duration](../Chapter%205/Key%20Rates%20O1s%20Durations%20and%20Hedging.md). The third term says that the volatility of rates - movement of rates either up or down - increases return in proportion to [convexity](../../../Fixed%20Income%20Asset%20Pricing/Problem%20Sets/PSET%20II%20Fixed%20Income%20Asset%20Pricing%201.md). To appreciate this term, recall from Chapter 4 that,. across portfolios with the same [duration](../Chapter%205/Key%20Rates%20O1s%20Durations%20and%20Hedging.md), more convex portfolios increase. more in value as rates change (at a fixed moment in time), whether rates rise. or fall.  

To draw conclusions about expected [returns](../../Financial%20Asset%20Pricing%20Theory%20Overview/Chapter%203%20-%20%20Assets,%20Portfolios,%20and%20Arbitrage/Assets.md), take the expectation of both sides of (8.15),  
$$
E\left[\frac{\partial P}{P}\right]=f(T)d t-D E[d r]+\frac{1}{2}C\sigma^{2}d t
$$  

The intuition of this decomposition is the same as for Equation (8.15), but with the [duration](../Chapter%205/Key%20Rates%20O1s%20Durations%20and%20Hedging.md) component depending not on the change in rate but on the expected change in rate.  

The next step in the analysis introduces the concept of a risk premium. [Risk-neutral investors](.md), who do not require a risk premium, demand that each bond offer an [expected return](../../../Advanced%20Investments/Lecture%201-%20Probability%20Distributions%20of%20Returns.md) equal to the short-term rate of interest. Mathematically,  
$$
E\left[{\frac{d P}{P}}\right]=r_{0}d t
$$  

Risk averse investors, however, demand higher expected [returns](../../Financial%20Asset%20Pricing%20Theory%20Overview/Chapter%203%20-%20%20Assets,%20Portfolios,%20and%20Arbitrage/Assets.md) for bonds with greater [interest rate risk](../../../Fixed%20Income%20Asset%20Pricing/Analysis%20of%20Fixed%20Income%20Securities.md). The appendix to this chapter shows that the [interest rate risk](../../../Fixed%20Income%20Asset%20Pricing/Analysis%20of%20Fixed%20Income%20Securities.md) of a bond over the next instant may be measured by its [duration](../Chapter%205/Key%20Rates%20O1s%20Durations%20and%20Hedging.md) with respect to the interest rate factor, and that risk-averse investors demand a risk premium proportional to [duration](../Chapter%205/Key%20Rates%20O1s%20Durations%20and%20Hedging.md). This risk premium may depend on time and on the level of rates, but not on the characteristics of any individual bond. The discussion proceeds here, however, as if the risk premium were constant and denoted by $\lambda$ . In that case, the [expected return](../../../Advanced%20Investments/Lecture%201-%20Probability%20Distributions%20of%20Returns.md) equation for risk-averse investors is,  
$$
E\left[{\frac{d P}{P}}\right]=r_{0}d t+\lambda D d t
$$  

Say, for example, that the short-term rate is $1\%$ , that the [duration](../Chapter%205/Key%20Rates%20O1s%20Durations%20and%20Hedging.md) of a bond is five, and that the risk premium is 10 basis points per year of [duration](../Chapter%205/Key%20Rates%20O1s%20Durations%20and%20Hedging.md) risk. Then, according to Equation (8.18), the bond's [expected return](../../../Advanced%20Investments/Lecture%201-%20Probability%20Distributions%20of%20Returns.md) is $1\%+$ $5\times0.1\%=1.5\%$ per year.  

Another useful way to think of the risk premium is in terms of the Sharpe ratio (SR) of a security, defined as its [expected excess return](../../Financial%20Asset%20Pricing%20Theory%20Overview/Chapter%209%20-%20Factor%20Models/Theoretical%20Factors.md) (over the short-term rate) divided by the standard deviation of its return. Because the random part of a bond's return comes from its [duration](../Chapter%205/Key%20Rates%20O1s%20Durations%20and%20Hedging.md) times the change in rate, as in Equation (8.15), the standard deviation of the return equals the [duration](../Chapter%205/Key%20Rates%20O1s%20Durations%20and%20Hedging.md) times the standard deviation of rates. Therefore, the SR of a bond may be written as,  
$$
S R={\frac{E[d P/P]-r_{0}d t}{\sigma D d t}}={\frac{\lambda}{\sigma}}
$$  

where the second equality follows from Equation (8.18). For example, if the risk premium is 10 basis points per year, and if the standard deviation of. rates is 100 basis points per year, then the Sharpe ratio of bond investments is $10\%$  

The decomposition of [returns](../../Financial%20Asset%20Pricing%20Theory%20Overview/Chapter%203%20-%20%20Assets,%20Portfolios,%20and%20Arbitrage/Assets.md) can now be combined with the economics. of the risk premium to draw conclusions about the shape of the [term structure](../Chapter%209/The%20Vasicek%20Model.md) of forward rates. Equating the expressions for expected [returns](../../Financial%20Asset%20Pricing%20Theory%20Overview/Chapter%203%20-%20%20Assets,%20Portfolios,%20and%20Arbitrage/Assets.md) in the right-hand sides of Equations (8.16) and (8.18),.  
$$
f(T)=\left\{r_{0}+E\left[\frac{d r}{d t}\right]D\right\}+\lambda D-\frac{1}{2}C\sigma^{2}
$$  

Equation (8.20) mathematically describes the determinants of forward rates. The three terms represent the impacts of [expectations](../../../Fixed%20Income%20Asset%20Pricing/Fixed%20Income%20Lecture%20Notes/FORWARD%20RATES%20AND%20TERM%20STRUCTURE.md), risk premium,. and [convexity](../../../Fixed%20Income%20Asset%20Pricing/Problem%20Sets/PSET%20II%20Fixed%20Income%20Asset%20Pricing%201.md), respectively. The first term says that the [forward rate](../../../Clippings/Forward%20Points%20in%20Currency.md) is composed of the instantaneous interest rate plus the expected change in that rate times the [duration](../Chapter%205/Key%20Rates%20O1s%20Durations%20and%20Hedging.md) of the zero coupon bond corresponding to the term of the [forward rate](../../../Clippings/Forward%20Points%20in%20Currency.md). In other words, the higher the instantaneous rate, the higher the [forward rate](../../../Clippings/Forward%20Points%20in%20Currency.md); the more rates are expected to increase, the higher the [forward rate](../../../Clippings/Forward%20Points%20in%20Currency.md); and the greater the corresponding [duration](../Chapter%205/Key%20Rates%20O1s%20Durations%20and%20Hedging.md), the greater the effect of expected [rate changes](../Chapter%207/Profit%20and%20Loss%20Attribution%20with%20an%20OAS.md) on the [forward rate](../../../Clippings/Forward%20Points%20in%20Currency.md)..  

The second term on the right-hand side of (8.20) says that the forward. rate increases with the risk premium in proportion to the corresponding [duration](../Chapter%205/Key%20Rates%20O1s%20Durations%20and%20Hedging.md). In other words, the greater the corresponding [interest rate risk](../../../Fixed%20Income%20Asset%20Pricing/Analysis%20of%20Fixed%20Income%20Securities.md) and the greater the risk premium, the greater the [forward rate](../../../Clippings/Forward%20Points%20in%20Currency.md).  

Chapter 7 noted that a drift in the short-term rate of a certain number. of basis points has the same effect on bond [pricing](../Chapter%207/Arbitrage%20Pricing%20of%20Derivatives.md) as a risk premium of that number of basis points per year of [duration](../Chapter%205/Key%20Rates%20O1s%20Durations%20and%20Hedging.md) risk. Equation (8.20) formal-. izes this statement. Increasing the risk premium or increasing the expected short-term rate by the same amount are indistinguishable from the observation of forward rates. This means that the [term structure of interest rates](../../../Financial%20Engineering/6.%20A%20Brief%20Introduction%20to%20Stochastic%20Calculus.md). cannot, on its own, be used to separate [expectations](../../../Fixed%20Income%20Asset%20Pricing/Fixed%20Income%20Lecture%20Notes/FORWARD%20RATES%20AND%20TERM%20STRUCTURE.md) of [rate changes](../Chapter%207/Profit%20and%20Loss%20Attribution%20with%20an%20OAS.md) from risk premium. From a modeling perspective, this means that only the [risk-neutral process](../Chapter%207/Profit%20and%20Loss%20Attribution%20with%20an%20OAS.md) is relevant for [pricing](../Chapter%207/Arbitrage%20Pricing%20of%20Derivatives.md). Dividing the risk-neutral drift into expecta-. tions and risk premium might be very useful for economic perspectives and. for [macro-style trading](../Chapter%209/Relative%20Value%20and%20Macro-Style%20Trading%20with%20the.md) (see Chapter 9), but this division is not observable from a cross section of bond prices alone..  

The first two terms of Equation (8.20) can also be cast in terms of theories of the [term structure of interest rates](../../../Financial%20Engineering/6.%20A%20Brief%20Introduction%20to%20Stochastic%20Calculus.md). (Put aside the [convexity](../../../Fixed%20Income%20Asset%20Pricing/Problem%20Sets/PSET%20II%20Fixed%20Income%20Asset%20Pricing%201.md) term for the moment.) Under the pure [expectations hypothesis](../../Financial%20Asset%20Pricing%20Theory%20Overview/Chapter%2010%20-%20The%20Economics%20of%20the%20Term%20Structure%20of%20Interest%20Rates/The%20Expectation%20Hypothesis.md), the risk premium, $\lambda$ , is zero, and the [term structure](../Chapter%209/The%20Vasicek%20Model.md) of forward rates is determined by [expectations](../../../Fixed%20Income%20Asset%20Pricing/Fixed%20Income%20Lecture%20Notes/FORWARD%20RATES%20AND%20TERM%20STRUCTURE.md), $E[d r/d t]$ . In this view of the world, the most natural "no-change" scenario,. in the terms of Chapter 3, is that [short-term rates](Volatility%20and%20Convexity.md) evolve as expected and that forward rates are realized. At the opposite extreme, under the pure risk premium hypothesis, the market has no [expectations](../../../Fixed%20Income%20Asset%20Pricing/Fixed%20Income%20Lecture%20Notes/FORWARD%20RATES%20AND%20TERM%20STRUCTURE.md) about rates, that is, $E[d r/d t]=0$ , and the [term structure](../Chapter%209/The%20Vasicek%20Model.md) of forward rates is determined by the risk premium. In this view of the world, the most natural "no-change" scenario is that [short-term rates](Volatility%20and%20Convexity.md) stay the same, as expected, which, in terms of Chapter 3 is an unchanged [term structure](../Chapter%209/The%20Vasicek%20Model.md). The reality, of course, can be between the two extremes, such the the [term structure](../Chapter%209/The%20Vasicek%20Model.md) is determined by a mix of [expectations](../../../Fixed%20Income%20Asset%20Pricing/Fixed%20Income%20Lecture%20Notes/FORWARD%20RATES%20AND%20TERM%20STRUCTURE.md) and risk premium..  

To conclude the discussion of Equation (8.20), the third term shows that the [forward rate](../../../Clippings/Forward%20Points%20in%20Currency.md) is reduced because of volatility and the [convexity](../../../Fixed%20Income%20Asset%20Pricing/Problem%20Sets/PSET%20II%20Fixed%20Income%20Asset%20Pricing%201.md) of. the zero corresponding to the term of the [forward rate](../../../Clippings/Forward%20Points%20in%20Currency.md) by. $0.5C\sigma^{2}$ . Using this to reinterpret Equation (8.16), the indirect reduction in return through the [forward rate](../../../Clippings/Forward%20Points%20in%20Currency.md), because of [convexity](../../../Fixed%20Income%20Asset%20Pricing/Problem%20Sets/PSET%20II%20Fixed%20Income%20Asset%20Pricing%201.md), is exactly offset by the direct increase in return, because of [convexity](../../../Fixed%20Income%20Asset%20Pricing/Problem%20Sets/PSET%20II%20Fixed%20Income%20Asset%20Pricing%201.md). Put another way, the [expected return](../../../Advanced%20Investments/Lecture%201-%20Probability%20Distributions%20of%20Returns.md) condition of Equation (8.18) ensures that there is no net advantage of [convexity](../../../Fixed%20Income%20Asset%20Pricing/Problem%20Sets/PSET%20II%20Fixed%20Income%20Asset%20Pricing%201.md). The significance of this reasoning for [investment](../../../Advanced%20Investments/An%20Asset%20Allocation%20Primer.md) and [hedging](../Chapter%205/Key%20Rates%20O1s%20Durations%20and%20Hedging.md) decisions is intro-. duced in Chapter 4 in the context of establishing long- and short-[convexity](../../../Fixed%20Income%20Asset%20Pricing/Problem%20Sets/PSET%20II%20Fixed%20Income%20Asset%20Pricing%201.md). positions.  

# The Vasicek and Gauss+ Models  

well-known [Vasicek](../Chapter%209/The%20Vasicek%20Model.md) and Gauss+ models. The [Vasicek model](../../../Fixed%20Income%20Asset%20Pricing/Fixed%20Income%20Lecture%20Notes/Vasicek%20Short%20Rate%20Model.md) started the literature on short-term rate models;' remains an extremely good starting point for learning about these models; and can still be used in some applied contexts. The $\mathrm{Gauss+}$ model has proven very popular for proprietary trading, for both relative value and [macro-style trading](../Chapter%209/Relative%20Value%20and%20Macro-Style%20Trading%20with%20the.md). The presentation of this model here is directed toward determined readers who would like to implement a [term structure](../Chapter%209/The%20Vasicek%20Model.md) model for their own trading purposes.  
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

This section derives a general decomposition of forward rates in terms of. [[FORWARD RATES AND TERM STRUCTURE|expectations]], [[PSET II Fixed Income Asset Pricing 1|convexity]], and risk premium. The level of mathematics here is higher than used in most of the book, but the discussion still aims at intuition.  

Assume that all bond prices are determined by the instantaneous rate, $r$ which takes on the value of. $r_{t}$ at time $t$ . Let $P_{t}(r_{t},T)$ be the price of a $T$ year zero coupon bond at time. $t$ . By [[Determining the Stochastic Process for a Forward Contract from Ito’s Lemma|Ito's lemma]], a discussion of which is beyond. the scope of this book,  
$$
d P={\frac{\partial P}{\partial r}}d r+{\frac{\partial P}{\partial t}}d t+{\frac{1}{2}}{\frac{\partial^{2}P}{\partial r^{2}}}\sigma^{2}d t
$$  

where $d P,d r$ and $d t$ are the changes in price, rate, and time over the next instant, respectively, and $\sigma$ is the volatility of changes in $r$ . The two first-order. partial [[Chapter 9 Arbitrage and Hedging With Options|derivatives]] in Equation (8.9) denote the instantaneous change in the bond price for a unit change in the rate (with time unchanged) and for a unit change in time (with rate unchanged), respectively. Finally, the second order partial derivative in the equation gives the instantaneous change in $\partial P/\partial r$ (with time unchanged). Dividing both sides of (8.9) by price,  
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

Second, by the definitions of [[Key Rates O1s Durations and Hedging|duration]], $D$ , and [[PSET II Fixed Income Asset Pricing 1|convexity]], C,  
$$
\begin{array}{l}{{\displaystyle{\cal D}\equiv-\frac{1}{{\cal P}}\frac{\partial{\cal P}}{\partial r}}~}\ {{\displaystyle~C\equiv\frac{1}{{\cal P}}\frac{\partial^{2}{\cal P}}{\partial r^{2}}}}\end{array}
$$  

Now, substituting Equations (8.12) through (8.14) into the return decomposition (8.10),  
$$
\frac{\partial P}{P}=f(T)d t-D d r+\frac{1}{2}C\sigma^{2}d t
$$  

Equation (8.15) gives the return decomposition in terms of the following three components. The first is the return due to the passage of time, which, in this case, is the [[Forward Points in Currency|forward rate]], $f(T)$ .1 The second and third components are [[Assets|returns]] due to changes in the rate. The second term says that increases in rate. reduce bond return in proportion to [[Key Rates O1s Durations and Hedging|duration]]. The third term says that the volatility of rates - movement of rates either up or down - increases return in proportion to [[PSET II Fixed Income Asset Pricing 1|convexity]]. To appreciate this term, recall from Chapter 4 that,. across portfolios with the same [[Key Rates O1s Durations and Hedging|duration]], more convex portfolios increase. more in value as rates change (at a fixed moment in time), whether rates rise. or fall.  

To draw conclusions about expected [[Assets|returns]], take the expectation of both sides of (8.15),  
$$
E\left[\frac{\partial P}{P}\right]=f(T)d t-D E[d r]+\frac{1}{2}C\sigma^{2}d t
$$  

The intuition of this decomposition is the same as for Equation (8.15), but with the [[Key Rates O1s Durations and Hedging|duration]] component depending not on the change in rate but on the expected change in rate.  

The next step in the analysis introduces the concept of a risk premium. [[An Analytical Decomposition of Forward Rates|Risk-neutral investors]], who do not require a risk premium, demand that each bond offer an [[Lecture 1- Probability Distributions of Returns|expected return]] equal to the short-term rate of interest. Mathematically,  
$$
E\left[{\frac{d P}{P}}\right]=r_{0}d t
$$  

Risk averse investors, however, demand higher expected [[Assets|returns]] for bonds with greater [[Analysis of Fixed Income Securities|interest rate risk]]. The appendix to this chapter shows that the [[Analysis of Fixed Income Securities|interest rate risk]] of a bond over the next instant may be measured by its [[Key Rates O1s Durations and Hedging|duration]] with respect to the interest rate factor, and that risk-averse investors demand a risk premium proportional to [[Key Rates O1s Durations and Hedging|duration]]. This risk premium may depend on time and on the level of rates, but not on the characteristics of any individual bond. The discussion proceeds here, however, as if the risk premium were constant and denoted by $\lambda$ . In that case, the [[Lecture 1- Probability Distributions of Returns|expected return]] equation for risk-averse investors is,  
$$
E\left[{\frac{d P}{P}}\right]=r_{0}d t+\lambda D d t
$$  

Say, for example, that the short-term rate is $1\%$ , that the [[Key Rates O1s Durations and Hedging|duration]] of a bond is five, and that the risk premium is 10 basis points per year of [[Key Rates O1s Durations and Hedging|duration]] risk. Then, according to Equation (8.18), the bond's [[Lecture 1- Probability Distributions of Returns|expected return]] is $1\%+$ $5\times0.1\%=1.5\%$ per year.  

Another useful way to think of the risk premium is in terms of the Sharpe ratio (SR) of a security, defined as its [[Theoretical Factors|expected excess return]] (over the short-term rate) divided by the standard deviation of its return. Because the random part of a bond's return comes from its [[Key Rates O1s Durations and Hedging|duration]] times the change in rate, as in Equation (8.15), the standard deviation of the return equals the [[Key Rates O1s Durations and Hedging|duration]] times the standard deviation of rates. Therefore, the SR of a bond may be written as,  
$$
S R={\frac{E[d P/P]-r_{0}d t}{\sigma D d t}}={\frac{\lambda}{\sigma}}
$$  

where the second equality follows from Equation (8.18). For example, if the risk premium is 10 basis points per year, and if the standard deviation of. rates is 100 basis points per year, then the Sharpe ratio of bond investments is $10\%$  

The decomposition of [[Assets|returns]] can now be combined with the economics. of the risk premium to draw conclusions about the shape of the [[The Vasicek Model|term structure]] of forward rates. Equating the expressions for expected [[Assets|returns]] in the right-hand sides of Equations (8.16) and (8.18),.  
$$
f(T)=\left\{r_{0}+E\left[\frac{d r}{d t}\right]D\right\}+\lambda D-\frac{1}{2}C\sigma^{2}
$$  

Equation (8.20) mathematically describes the determinants of forward rates. The three terms represent the impacts of [[FORWARD RATES AND TERM STRUCTURE|expectations]], risk premium,. and [[PSET II Fixed Income Asset Pricing 1|convexity]], respectively. The first term says that the [[Forward Points in Currency|forward rate]] is composed of the instantaneous interest rate plus the expected change in that rate times the [[Key Rates O1s Durations and Hedging|duration]] of the zero coupon bond corresponding to the term of the [[Forward Points in Currency|forward rate]]. In other words, the higher the instantaneous rate, the higher the [[Forward Points in Currency|forward rate]]; the more rates are expected to increase, the higher the [[Forward Points in Currency|forward rate]]; and the greater the corresponding [[Key Rates O1s Durations and Hedging|duration]], the greater the effect of expected [[Profit and Loss Attribution with an OAS|rate changes]] on the [[Forward Points in Currency|forward rate]]..  

The second term on the right-hand side of (8.20) says that the forward. rate increases with the risk premium in proportion to the corresponding [[Key Rates O1s Durations and Hedging|duration]]. In other words, the greater the corresponding [[Analysis of Fixed Income Securities|interest rate risk]] and the greater the risk premium, the greater the [[Forward Points in Currency|forward rate]].  

Chapter 7 noted that a drift in the short-term rate of a certain number. of basis points has the same effect on bond [[Arbitrage Pricing of Derivatives|pricing]] as a risk premium of that number of basis points per year of [[Key Rates O1s Durations and Hedging|duration]] risk. Equation (8.20) formal-. izes this statement. Increasing the risk premium or increasing the expected short-term rate by the same amount are indistinguishable from the observation of forward rates. This means that the [[6. A Brief Introduction to Stochastic Calculus|term structure of interest rates]]. cannot, on its own, be used to separate [[FORWARD RATES AND TERM STRUCTURE|expectations]] of [[Profit and Loss Attribution with an OAS|rate changes]] from risk premium. From a modeling perspective, this means that only the [[Profit and Loss Attribution with an OAS|risk-neutral process]] is relevant for [[Arbitrage Pricing of Derivatives|pricing]]. Dividing the risk-neutral drift into expecta-. tions and risk premium might be very useful for economic perspectives and. for [[Relative Value and Macro-Style Trading with the|macro-style trading]] (see Chapter 9), but this division is not observable from a cross section of bond prices alone..  

The first two terms of Equation (8.20) can also be cast in terms of theories of the [[6. A Brief Introduction to Stochastic Calculus|term structure of interest rates]]. (Put aside the [[PSET II Fixed Income Asset Pricing 1|convexity]] term for the moment.) Under the pure [[The Expectation Hypothesis|expectations hypothesis]], the risk premium, $\lambda$ , is zero, and the [[The Vasicek Model|term structure]] of forward rates is determined by [[FORWARD RATES AND TERM STRUCTURE|expectations]], $E[d r/d t]$ . In this view of the world, the most natural "no-change" scenario,. in the terms of Chapter 3, is that [[Volatility and Convexity|short-term rates]] evolve as expected and that forward rates are realized. At the opposite extreme, under the pure risk premium hypothesis, the market has no [[FORWARD RATES AND TERM STRUCTURE|expectations]] about rates, that is, $E[d r/d t]=0$ , and the [[The Vasicek Model|term structure]] of forward rates is determined by the risk premium. In this view of the world, the most natural "no-change" scenario is that [[Volatility and Convexity|short-term rates]] stay the same, as expected, which, in terms of Chapter 3 is an unchanged [[The Vasicek Model|term structure]]. The reality, of course, can be between the two extremes, such the the [[The Vasicek Model|term structure]] is determined by a mix of [[FORWARD RATES AND TERM STRUCTURE|expectations]] and risk premium..  

To conclude the discussion of Equation (8.20), the third term shows that the [[Forward Points in Currency|forward rate]] is reduced because of volatility and the [[PSET II Fixed Income Asset Pricing 1|convexity]] of. the zero corresponding to the term of the [[Forward Points in Currency|forward rate]] by. $0.5C\sigma^{2}$ . Using this to reinterpret Equation (8.16), the indirect reduction in return through the [[Forward Points in Currency|forward rate]], because of [[PSET II Fixed Income Asset Pricing 1|convexity]], is exactly offset by the direct increase in return, because of [[PSET II Fixed Income Asset Pricing 1|convexity]]. Put another way, the [[Lecture 1- Probability Distributions of Returns|expected return]] condition of Equation (8.18) ensures that there is no net advantage of [[PSET II Fixed Income Asset Pricing 1|convexity]]. The significance of this reasoning for [[An Asset Allocation Primer|investment]] and [[Key Rates O1s Durations and Hedging|hedging]] decisions is intro-. duced in Chapter 4 in the context of establishing long- and short-[[PSET II Fixed Income Asset Pricing 1|convexity]]. positions.  

# The Vasicek and Gauss+ Models  

well-known [[The Vasicek Model|Vasicek]] and Gauss+ models. The [[Vasicek Short Rate Model|Vasicek model]] started the literature on short-term rate models;' remains an extremely good starting point for learning about these models; and can still be used in some applied contexts. The $\mathrm{Gauss+}$ model has proven very popular for proprietary trading, for both relative value and [[Relative Value and Macro-Style Trading with the|macro-style trading]]. The presentation of this model here is directed toward determined readers who would like to implement a [[The Vasicek Model|term structure]] model for their own trading purposes.  
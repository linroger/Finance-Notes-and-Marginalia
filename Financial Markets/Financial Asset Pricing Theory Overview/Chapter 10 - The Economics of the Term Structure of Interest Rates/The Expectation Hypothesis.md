---
tags:
  - bond_markets
  - expectation_hypothesis
  - interest_rates
  - term_structure
  - yield_curve
aliases:
  - Expectations Hypothesis
  - Pure Expectation Hypothesis
key_concepts:
  - Continuously compounded returns
  - Expected future interest rates
  - Gross return trading strategies
  - Long-term vs short-term bonds
  - Risk-neutral investors
---

# 10.7 The expectation hypothesis  

The expectation hypothesis relates the current [interest rates](../../Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%202/Interest%20Rate%20Quotations.md) and yields to expected future inter-. est rates or [returns](../Chapter%203%20-%20%20Assets,%20Portfolios,%20and%20Arbitrage/Assets.md). This basic issue was discussed already by Fisher (1896) and further developed and concretized by Hicks (1939) and Lutz (1940). The original motivation of the hypothesis is that when lenders (bond investors) and borrowers (bond issuers) decide between long-term or shortterm bonds, they will compare the price or yield of a long-term bond to the expected price or return on a roll-over strategy in short-term bonds. Hence, long-term rates and expected future [short-term rates](../../Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%208/Volatility%20and%20Convexity.md) will be linked. Of course, a cornerstone of modern finance theory is that, when comparing different strategies, investors will also take the risks into account. So even before going. into the specifics of the hypothesis you should really be quite skeptical, at least when it comes to very strict interpretations of the expectation hypothesis..  

The vague idea that current yields and [interest rates](../../Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%202/Interest%20Rate%20Quotations.md) are linked to expected future rates and. [returns](../Chapter%203%20-%20%20Assets,%20Portfolios,%20and%20Arbitrage/Assets.md) can be concretized in a number of ways. Below we will present and evaluate a number of versions. This analysis follows Cox, Ingersoll, and Ross (1981a) quite closely. We find that. some versions are equivalent, some versions inconsistent. We end up concluding that none of the variants of the [expectations hypothesis](.md) are consistent with any realistic behavior of [interest rates](../../Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%202/Interest%20Rate%20Quotations.md). Hence, the analysis of the shape of the yield curve and models of [term structure dynamics](../../Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%209/The%20Gauss%20Model.md) should not be based on this hypothesis. Hence, it is surprising, maybe even disappointing, that empirical tests of the expectation hypothesis have generated such a huge literature in the past and that the hypothesis still seems to be widely accepted among economists..  

# 10.7.1 Versions of the pure expectation hypothesis  

The first version of the [pure expectation hypothesis](.md) that we will discuss says that prices in the. bond markets are set so that the expected gross [returns](../Chapter%203%20-%20%20Assets,%20Portfolios,%20and%20Arbitrage/Assets.md) on all self-financing [trading strategies](../../../Course%20Notes/Quantitative%20Trading%20Strategies%20Lecture%20Notes.md) over a given period are identical. In particular, the expected gross return from buying at time $t$ a zero-coupon bond maturing at time $T$ and reselling it at time $t^{\prime}\leq T$ , which is given by $\mathrm{E}_{t}[B_{t^{\prime}}^{T}/B_{t}^{T}]$ will be independent of the maturity date $T$ of the bond (but generally not independent of $t^{\prime}$ ). Let us refer to this as the gross return [pure expectation hypothesis](.md).  

This version of the hypothesis is consistent with [pricing](../../Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%207/Arbitrage%20Pricing%20of%20Derivatives.md) in a world of [risk-neutral investors](../../Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%208/An%20Analytical%20Decomposition%20of%20Forward%20Rates.md). If. we have a [representative individual](../Chapter%208%20-%20Consumption-Based%20Asset%20Pricing/The%20Simple%20Multi-Period%20Ccapm.md) with [time-additive expected utility](../Chapter%208%20-%20Consumption-Based%20Asset%20Pricing/General%20Multi-Period%20Link%20Between%20Consumption%20a.md), we know that zero-coupon bond prices satisfy  
$$
B_{t}^{T}=\mathrm{E}_{t}\left[e^{-\delta(t^{\prime}-t)}\frac{u^{\prime}(c_{t^{\prime}})}{u^{\prime}(c_{t})}B_{t^{\prime}}^{T}\right],
$$  

where $u$ is the instantaneous utility function, $\delta$ is the time [preference](../Chapter%205%20-%20Modeling%20the%20Preferences%20of%20Individuals/Utility%20Indices.md) rate, and $C$ denotes [aggregate consumption](../Chapter%207%20-%20Market%20equilibrium/Pareto-Optimality%20in%20Some%20Incomplete%20Markets.md). If the [representative individual](../Chapter%208%20-%20Consumption-Based%20Asset%20Pricing/The%20Simple%20Multi-Period%20Ccapm.md) is risk-neutral, his marginal utility is constant, which implies that  
$$
\mathrm{E}_{t}\left[\frac{B_{t^{\prime}}^{T}}{B_{t}^{T}}\right]=e^{\delta(t^{\prime}-t)},
$$  

which is clearly independent of. $T$ . Clearly, the assumption of risk-neutrality is not very attractive.. There is also another serious problem with this hypothesis. As is to be shown in Exercise 10.4, it cannot hold when [interest rates](../../Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%202/Interest%20Rate%20Quotations.md) are uncertain..  

A slight variation of the above is to align all expected [continuously compounded returns](.md), i.e. $\begin{array}{r}{\frac{1}{t^{\prime}-t}\operatorname{E}_{t}[\ln\left(B_{t^{\prime}}^{T}/B_{t}^{T}\right)]}\end{array}$ for all $T$ . In particular with $T=t^{\prime}$ , the expected [continuously compounded rate](../../../Financial%20Instruments/Financial%20Derivatives%20and%20Quantitative%20Methods/Arithmetic%20and%20Geometric%20Rates%20of%20Return.md) of return is known to be equal to the zero-coupon yield for maturity. $t^{\prime}$ , which we denote by $\begin{array}{r}{y_{t}^{t^{\prime}}=-\frac{1}{t^{\prime}-t}\ln B_{t}^{t^{\prime}}}\end{array}$ . We can therefore formulate the hypothesis as.  
$$
{\frac{1}{t^{\prime}-t}}\operatorname{E}_{t}\left[\ln\left({\frac{B_{t^{\prime}}^{T}}{B_{t}^{T}}}\right)\right]=y_{t}^{t^{\prime}},{\mathrm{~all~}}T\geq t^{\prime}.
$$  

Let us refer to this as the rate of return [pure expectation hypothesis](.md). For $t^{\prime}\to t$ , the right-hand side approaches the current [short rate](../../../Fixed%20Income%20Asset%20Pricing/Fixed%20Income%20Lecture%20Notes/An%20Overview%20of%20the%20Vasicek%20Short%20Rate%20Model.md). $r_{t}$ , while the left-hand side approaches the absolute drift. rate of $\ln B_{t}^{T}$  

An alternative specification of the [pure expectation hypothesis](.md) claims that the [expected return](../../../Advanced%20Investments/Lecture%201-%20Probability%20Distributions%20of%20Returns.md) over the next time period is the same for all investments in bonds and deposits. In other words there is no difference between expected [returns](../Chapter%203%20-%20%20Assets,%20Portfolios,%20and%20Arbitrage/Assets.md) on long-maturity and short-maturity bonds. In the continuous-time limit we consider [returns](../Chapter%203%20-%20%20Assets,%20Portfolios,%20and%20Arbitrage/Assets.md) over the next instant. The [risk-free return](../Chapter%204%20-%20State%20Prices/A%20Preview%20of%20Alternative%20Formulations.md) over $[t,t+d t]$ is $r_{t}d t$ , so for any zero-coupon bond, the hypothesis claims that  
$$
\operatorname{E}_{t}\left[{\frac{d B_{t}^{T}}{B_{t}^{T}}}\right]=r_{t}d t,\quad{\mathrm{~for~all~}}T>t,
$$  

or, using Theorem 2.7, that  
$$
B_{t}^{T}=\operatorname{E}_{t}\left[e^{-\int_{t}^{T}r_{s}d s}\right],\quad{\mathrm{~for~all~}}T>t.
$$  

This is the local pure [expectations hypothesis](.md).  

Another interpretation says that the return from holding a zero-coupon bond to maturity should equal the [expected return](../../../Advanced%20Investments/Lecture%201-%20Probability%20Distributions%20of%20Returns.md) from rolling over short-term bonds over the same time period, i.e.  

or, equivalently,  
$$
{\frac{1}{B_{t}^{T}}}=\mathrm{E}_{t}\left[e^{\int_{t}^{T}r_{s}d s}\right],\quad{\mathrm{~for~all~}}T>t
$$  
$$
B_{t}^{T}=\left(\operatorname{E}_{t}\left[e^{\int_{t}^{T}r_{s}d s}\right]\right)^{-1},\quad{\mathrm{~for~all~}}T>t.
$$  

This is the return-to-maturity [pure expectation hypothesis](.md).  

A related claim is that the yield on any zero-coupon bond should equal the "expected yield" on a roll-over strategy in short bonds. Since an [investment](../../../Advanced%20Investments/An%20Asset%20Allocation%20Primer.md) of one at time. $t$ in the bank account generates $e^{\int_{t}^{T}r_{s}d s}$ at time $T$ , the ex-post realized yield is $\begin{array}{r}{\frac{1}{T-t}\int_{t}^{T}r_{s}d s}\end{array}$ . Hence, this yield-to-maturity [pure expectation hypothesis](.md) says that  

or, equivalently,  
$$
y_{t}^{T}=-\frac{1}{T-t}\ln B_{t}^{T}=\mathrm{E}_{t}\left[\frac{1}{T-t}\int_{t}^{T}r_{s}d s\right],
$$  
$$
B_{t}^{T}=e^{-\operatorname{E}_{t}\left[\int_{t}^{T}r_{s}d s\right]},\quad{\mathrm{~for~all~}}T>t.
$$  

Finally, the unbiased [pure expectation hypothesis](.md) states that the [forward rate](../../../Clippings/Forward%20Points%20in%20Currency.md) for time $T$ prevailing at time $t<T$ is equal to the time. $t$ expectation of the [short rate](../../../Fixed%20Income%20Asset%20Pricing/Fixed%20Income%20Lecture%20Notes/An%20Overview%20of%20the%20Vasicek%20Short%20Rate%20Model.md) at time. $T$ , i.e. that forward. rates are unbiased estimates of future spot rates. In symbols,  
$$
f_{t}^{T}=\mathrm{E}_{t}[r_{T}],\quad\mathrm{~for~all~}T>t.
$$  

This implies that  
$$
-\ln B_{t}^{T}=\int_{t}^{T}f_{t}^{s}d s=\int_{t}^{T}\operatorname{E}_{t}[r_{s}]d s=\operatorname{E}_{t}\left[\int_{t}^{T}r_{s}d s\right],
$$  

from which we see that the unbiased version of the [pure expectation hypothesis](.md) is indistinguishable from the yield-to-maturity version.  

We will first show that the different versions are inconsistent when future rates are uncertain. This follows from an application of [Jensen's inequality](../../Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%208/Volatility%20and%20Convexity.md) which states that if $X$ is a random variable and $f$ is a convex function, i.e. $f^{\prime\prime}>0$ , then $\operatorname{E}[f(X)]>f(\operatorname{E}[X])$ . Since $f(x)=e^{x}$ is a convex function, we have $\operatorname{E}[e^{X}]>e^{\operatorname{E}[X]}$ for any random variable $X$ . In particular for $\begin{array}{r}{X=\int_{t}^{T}r_{s}d s}\end{array}$ , we get  
$$
\begin{array}{r}{\operatorname{E}_{t}\left[e^{\int_{t}^{T}r_{s}d s}\right]>e^{\operatorname{E}_{t}\left[\int_{t}^{T}r_{s}d s\right]}\quad\Rightarrow\quad e^{-\operatorname{E}_{t}\left[\int_{t}^{T}r_{s}d s\right]}>\left(\operatorname{E}_{t}\left[e^{\int_{t}^{T}r_{s}d s}\right]\right)^{-1}.}\end{array}
$$  

This shows that the bond price according to the yield-to-maturity version is strictly greater than the bond price according to the return-to-maturity version. For $\begin{array}{r}{X=-\int_{t}^{T}r_{s}d s}\end{array}$ , we get  
$$
\begin{array}{r}{\mathrm{E}_{t}\left[e^{-\int_{t}^{T}r_{s}d s}\right]>e^{\mathrm{E}_{t}\left[-\int_{t}^{T}r_{s}d s\right]}=e^{-\mathrm{E}_{t}\left[\int_{t}^{T}r_{s}d s\right]},}\end{array}
$$  

hence the bond price according to the local version of the hypothesis is strictly greater than the bond price according to the yield-to-maturity version. We can conclude that at most one of the versions of the local, return-to-maturity, and yield-to-maturity pure [expectations hypothesis](.md) can hold.  

# 10.7.2 The pure expectation hypothesis and equilibrium  

Next, let us see whether the different versions can be consistent with any equilibrium. Assume that [interest rates](../../Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%202/Interest%20Rate%20Quotations.md) and bond prices are generated by a $d$ -dimensional standard [Brownian motion](../Chapter%202%20-%20Uncertainty,%20Information,%20and%20Stochastic%20Processes/Continuous-Time%20Stochastic%20Processes.md). $_{z}$ . Assuming [absence of arbitrage](Exercises.md) there exists a [market price of risk](Exercises.md) process. $\lambda$ so that for any maturity. $T$ the zero-coupon bond [price dynamics](../../../Financial%20Engineering/Derivatives/Part%20XII%20-%20Price%20Dynamics/Chapter%2047%20-%20Asset%20Price%20Dynamics.md) is of the form  
$$
d B_{t}^{T}=B_{t}^{T}\left[\left(r_{t}+\left({\pmb\sigma}_{t}^{T}\right)^{\top}\pmb\lambda_{t}\right)~d t+\left({\pmb\sigma}_{t}^{T}\right)^{\top}~d z_{t}\right],
$$  

where $\pmb{\sigma}_{t}^{T}$ denotes the $d$ -dimensional sensitivity vector of the bond price. Recall that the same $\lambda_{t}$ applies to all zero-coupon bonds so that $\lambda_{t}$ is independent of the maturity of the bond. Comparing with (10.75), we see that the local expectation hypothesis will hold if and only if $\left(\pmb{\sigma}_{t}^{T}\right)^{\top}\pmb{\lambda}_{t}=0$ for all $T$ . This is true if either investors are risk-neutral or [interest rate risk](../../../Fixed%20Income%20Asset%20Pricing/Analysis%20of%20Fixed%20Income%20Securities.md) is uncorrelated with [aggregate consumption](../Chapter%207%20-%20Market%20equilibrium/Pareto-Optimality%20in%20Some%20Incomplete%20Markets.md). Neither of these conditions hold in real life.  

To evaluate the return-to-maturity version, first note that an application of [Ito's Lemma](../../../Financial%20Engineering/Determining%20the%20Stochastic%20Process%20for%20a%20Forward%20Contract%20from%20Ito’s%20Lemma.md) on (10.78) show that  
$$
d\left(\frac{1}{B_{t}^{T}}\right)=\frac{1}{B_{t}^{T}}\left[\left(-r_{t}-\left(\pmb{\sigma}_{t}^{T}\right)^{\top}\lambda_{t}+\|\pmb{\sigma}_{t}^{T}\|^{2}\right)d t-\left(\pmb{\sigma}_{t}^{T}\right)^{\top}d z_{t}\right].
$$  

On the other hand, according to the hypothesis (10.76) the relative drift of $1/B_{t}^{T}$ equals $-\boldsymbol{r}_{t}$ cf. Theorem 2.7. To match the two expressions for the drift, we must have  
$$
\left(\pmb{\sigma}_{t}^{T}\right)^{\top}\pmb{\lambda}_{t}=\|\pmb{\sigma}_{t}^{T}\|^{2},\quad\mathrm{~for~all~}T.
$$  

Is this possible? Cox, Ingersoll, and Ross (1981a) conclude that it is impossible. If the exogenous. shock $_{z}$ and therefore $\pmb{\sigma}_{t}^{T}$ and $\lambda_{t}$ are one-dimensional, they are right, since $\lambda_{t}$ must then equal $\pmb{\sigma}_{t}^{T}$ and this must hold for all $T$ . Since $\lambda_{t}$ is independent of $T$ and the volatility $\pmb{\sigma}_{t}^{T}$ approaches zero for $T\to t$ , this can only hold if $\lambda_{t}\equiv0$ ([risk-neutral investors](../../Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%208/An%20Analytical%20Decomposition%20of%20Forward%20Rates.md)) or $\sigma_{t}^{\prime}\equiv0$ ([deterministic interest rates](../../../Credit%20Markets/RISK%20NEUTRAL%20VALUATION%20FRAMEWORK%20FOR%20CREDIT%20DEFAULT%20SWAPS.md)). However, as pointed out by McCulloch (1993) and Fisher and Gilles (1998), in multi-. dimensional cases the key condition (10.79) may indeed hold, at least in very special cases. Let. $\varphi$ be a $d$ -dimensional function with the property that $\|\varphi(\tau)\|^{2}$ is independent of $\tau$ . Define $\lambda_{t}=2\varphi(0)$ and $\pmb{\sigma}_{t}^{T}=\varphi(0)-\varphi(T-t)$ . Then (10.79) is indeed satisfied. However, all such functions. $\varphi$ seem to generate very strange bond [price dynamics](../../../Financial%20Engineering/Derivatives/Part%20XII%20-%20Price%20Dynamics/Chapter%2047%20-%20Asset%20Price%20Dynamics.md). The examples given in the two papers mentioned above are  
$$
\varphi(\tau)=k\left(\begin{array}{c c c c}{{\sqrt{2e^{-\tau}-e^{-2\tau}}}}\ {{1-e^{-\tau}}}\end{array}\right),\qquad\varphi(\tau)=k_{1}\left(\begin{array}{c c c c}{{\cos(k_{2}\tau)}}\ {{\sin(k_{2}\tau)}}\end{array}\right),
$$  

where $k,k_{1},k_{2}$ are constants.  

As discussed above, the rate of return version implies that the absolute drift rate of the log-bond price equals the [short rate](../../../Fixed%20Income%20Asset%20Pricing/Fixed%20Income%20Lecture%20Notes/An%20Overview%20of%20the%20Vasicek%20Short%20Rate%20Model.md). We can see from (10.77) that the same is true for the yield-to-maturity version and hence the unbiased version.3 On the other hand [Ito's Lemma](../../../Financial%20Engineering/Determining%20the%20Stochastic%20Process%20for%20a%20Forward%20Contract%20from%20Ito’s%20Lemma.md) and (10.78) imply that  
$$
d\left(\ln B_{t}^{T}\right)=\left(r_{t}+(\pmb{\sigma}_{t}^{T})^{\top}\pmb{\lambda}_{t}-\frac{1}{2}\|\pmb{\sigma}_{t}^{T}\|^{2}\right)d t+\left(\pmb{\sigma}_{t}^{T}\right)^{\top}d z_{t}.
$$  

Hence, these versions of the hypothesis will hold if and only if  
$$
({\pmb\sigma}_{t}^{T})^{\top}{\pmb\lambda}_{t}=\frac{1}{2}\|{\pmb\sigma}_{t}^{T}\|^{2},\quad\mathrm{~for~all~}T.
$$  

Again, it is possible that the condition holds. Just let. $\varphi$ and $\pmb{\sigma}_{t}^{T}$ be as for the return-to-maturity hypothesis and let $\lambda_{t}=\varphi(0)$ . But such specifications are not likely to represent real life term structures.  

The conclusion to be drawn from this analysis is that neither of the different versions of the [pure expectation hypothesis](.md) seem to be consistent with any reasonable description of the [term structure of interest rates](../../../Financial%20Engineering/6.%20A%20Brief%20Introduction%20to%20Stochastic%20Calculus.md).  
$$
\frac{1}{\Delta t}\operatorname{E}_{t}\left[\ln B_{t+\Delta t}^{T}-\ln B_{t}^{T}\right]=\frac{1}{\Delta t}\operatorname{E}_{t}\left[-\operatorname{E}_{t+\Delta t}\left[\int_{t+\Delta t}^{T}r_{s}d s\right]+\operatorname{E}_{t}\left[\int_{t}^{T}r_{s}d s\right]\right]=\frac{1}{\Delta t}\operatorname{E}_{t}\left[\int_{t}^{t+\Delta t}r_{s}d s\right],
$$  

# 10.7.3 The weak expectation hypothesis  

Above we looked at versions of the [pure expectation hypothesis](.md) that all aligns an [expected return](../../../Advanced%20Investments/Lecture%201-%20Probability%20Distributions%20of%20Returns.md) or yield with a current interest rate or yield. However, as pointed out by Campbell (1986), there is also a weak expectation hypothesis that allows for a difference between the relevant [expected return](../../../Advanced%20Investments/Lecture%201-%20Probability%20Distributions%20of%20Returns.md)/yield and the current rate/yield, but restricts this difference to be constant over time.  

The local weak expectation hypothesis says that  
$$
\mathrm{E}_{t}\left[{\frac{d B_{t}^{T}}{B_{t}^{T}}}\right]=(r_{t}+g(T-t))d t
$$  

for some deterministic function. $g$ . In the pure version. $g$ is identically zero. For a given time-to-.   
maturity there is a constant "instantaneous holding [term premium](../../../Contemporary%20Financial%20Intermediation%20Notes/Table%20of%20Contents.md)'. Comparing with (10.78), we see that this hypothesis will hold when the [market price of risk](Exercises.md). $\lambda_{t}$ is constant and the bond price.   
sensitivity vector $\pmb{\sigma}_{t}^{T}$ is a deterministic function of time-to-maturity. These conditions are satisfied.   
in the [Vasicek](../../Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%209/The%20Vasicek%20Model.md) (1977) model and in other models of the Gaussian class.  

Similarly, the weak yield-to-maturity expectation hypothesis says that  
$$
f_{t}^{T}=\mathrm{E}_{t}[r_{T}]+h(T-t)
$$  

for some deterministic function $h$ with $h(0)=0$ , i.e. that there is a constant "instantaneous forward [term premium](../../../Contemporary%20Financial%20Intermediation%20Notes/Table%20of%20Contents.md)". The pure version requires. $h$ to be identically equal to zero. It can be shown that this condition implies that the drift of. $\ln B_{t}^{T}$ equals $r_{t}+h(T-t)$ .4 Comparing with (10.80), we see that also this hypothesis will hold when. $\lambda_{t}$ is constant and $\sigma_{t}^{T}$ is a deterministic function of $T-t$ as is the case in the [Gaussian models](../../../Financial%20Engineering/SOFR%20Derivative%20Pricing%20Using%20a%20Short%20Rate%20Model.md)..  

The class of [Gaussian models](../../../Financial%20Engineering/SOFR%20Derivative%20Pricing%20Using%20a%20Short%20Rate%20Model.md) have several unrealistic properties. For example, such models. allow [negative interest rates](../../Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Front%20Matter/Negative%20Rates%20and%20Qe%20in%20Europe%20and%20Japan.md) and requires bond and interest rate volatilities to be independent of the level of [interest rates](../../Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%202/Interest%20Rate%20Quotations.md). So far, the validity of even weak versions of the expectation hypothesis. has not been shown in more realistic [term structure models](../../../Financial%20Engineering/Financial%20Mathematics%20Course.md)..  
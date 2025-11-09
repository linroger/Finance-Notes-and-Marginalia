---
tags:
  - call_option
  - european_option
  - option_pricing
  - put_call_parity
  - put_option
aliases:
  - Call Option
  - European Options
  - Option Pricing
  - Put Option
key_concepts:
  - European call option
  - European put option
  - Exercise price
  - Forward martingale measure
  - Non-dividend paying asset
  - Option price formula
  - Put-call parity
---

# 12.3 Options  

In this section, we focus on European options. Some aspects of American options are discussed in Section 12.5.  

# 12.3.1 General pricing results for European options  

A European call option with an [exercise price](.md) of $K$ and expiration at time $T$ gives a dividend at. $T$ of  
$$
C_{T}=\operatorname*{max}(P_{T}-K,0);
$$  

where $P_{T}$ is the value at time. $T$ of the underlying variable of the option. For an option on a traded. asset, $P_{T}$ is the price of the [underlying asset](../../../Financial%20Instruments/Financial%20Derivatives%20and%20Quantitative%20Methods/Risk%20Neutral%20Pricing%20of%20Options.md) at the expiry date. For an option on a given interest rate, $P_{T}$ denotes the value of this interest rate at the expiry date. With a call option you can speculate in high values of $P_{T}$ . A call option on an asset offers protection to an investor who wants. to purchase the [underlying asset](../../../Financial%20Instruments/Financial%20Derivatives%20and%20Quantitative%20Methods/Risk%20Neutral%20Pricing%20of%20Options.md) at time. $T$ . The call option ensures that the investor effectively. pays at most. $K$ for the [underlying asset](../../../Financial%20Instruments/Financial%20Derivatives%20and%20Quantitative%20Methods/Risk%20Neutral%20Pricing%20of%20Options.md). The call option price is the price of that protection.  

Similarly, a European put option with an [exercise price](.md) of $K$ and expiration at time $T$ gives a dividend at $T$ of  
$$
\pi_{T}=\operatorname*{max}(K-P_{T},0).
$$  

With a put option you can speculate in low values of $P_{T}$ . A put option offers protection to an investor who wants to sell the [underlying asset](../../../Financial%20Instruments/Financial%20Derivatives%20and%20Quantitative%20Methods/Risk%20Neutral%20Pricing%20of%20Options.md) at time $T$ . The put option ensures that the effective selling price is at least $K$  

Prices of European [call and put](../../../Course%20Notes/HBR%20Notes/Notes%20on%20Basic%20Options%20Properties.md) options on the same underlying variable are closely related. Since $C_{T}+K=\pi_{t}+P_{T}$ , it is clear that  
$$
\boldsymbol{C}_{t}+K\boldsymbol{B}_{t}^{T}=\boldsymbol{\pi}_{T}+\boldsymbol{B}_{t}^{T}\boldsymbol{\mathrm{E}}_{t}^{\boldsymbol{\mathbb{Q}}^{T}}\left[\boldsymbol{P}_{T}\right],
$$  

where $\mathbb{Q}^{T}$ is the $T$ [forward martingale measure](.md). In particular, if the underlying variable is the price of a [non-dividend paying asset](.md), we have $P_{t}=B_{t}^{T}\operatorname{E}_{t}^{\mathbb{Q}^{T}}[P_{T}]$ and thus the following result:  

Theorem 12.3 ([Put-call parity](../../../Financial%20Engineering/7.%20Black%20Scholes%20Model.md)) The prices of a European call option and a European put option on a [non-dividend paying asset](.md) are related through the equation.  
$$
C_{t}+K B_{t}^{T}=\pi_{t}+P_{t}.
$$  

A [portfolio](../../../Advanced%20Investments/An%20Asset%20Allocation%20Primer.md) of a call option and. $K$ zero-coupon bonds maturing at time $T$ gives exactly the same dividend as a [portfolio](../../../Advanced%20Investments/An%20Asset%20Allocation%20Primer.md) of a put option and the [underlying asset](../../../Financial%20Instruments/Financial%20Derivatives%20and%20Quantitative%20Methods/Risk%20Neutral%20Pricing%20of%20Options.md). The [put-call parity](../../../Financial%20Engineering/7.%20Black%20Scholes%20Model.md) (12.9) follows  

by [absence of arbitrage](Exercises.md). A consequence of the [put-call parity](../../../Financial%20Engineering/7.%20Black%20Scholes%20Model.md) is that we can focus on the [pricing](../../Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%207/Arbitrage%20Pricing%20of%20Derivatives.md) of European call options. The prices of European put options will then follow immediately..  

Now let us focus on the call option. In terms of the forward measure $\mathbb{Q}^{T}$ for maturity $T$ , the time $t$ price of the option is  
$$
C_{t}=B_{t}^{T}\operatorname{E}_{t}^{\mathbb{Q}^{T}}\left[\operatorname*{max}(P_{T}-K,0)\right].
$$  

We can rewrite the payoff as  
$$
C_{T}=\left(P_{T}-K\right)\mathbf{1}_{\left\{P_{T}>K\right\}},
$$  

where $\mathbf{1}_{\{P_{T}>K\}}$ is the indicator for the event $P_{T}>K$ . This indicator is a random variable whose value will be. $^{1}$ if the realized value of $P_{T}$ turns out to be larger than $K$ and the value is. $0$ otherwise.. Hence, the option price can be rewritten as1  
$$
\begin{array}{r l}&{C_{t}=B_{t}^{T}\mathrm{E}_{t}^{\mathbb{Q}^{T}}\left[\left(P_{T}-K\right)\mathbf{1}_{\{P_{T}>K\}}\right]}\ &{\quad=B_{t}^{T}\left(\mathrm{E}_{t}^{\mathbb{Q}^{T}}\left[P_{T}\mathbf{1}_{\{P_{T}>K\}}\right]-K\mathrm{E}_{t}^{\mathbb{Q}^{T}}\left[\mathbf{1}_{\{P_{T}>K\}}\right]\right)}\ &{\quad=B_{t}^{T}\left(\mathrm{E}_{t}^{\mathbb{Q}^{T}}\left[P_{T}\mathbf{1}_{\{P_{T}>K\}}\right]-K\mathbb{Q}_{t}^{T}(P_{T}>K)\right)}\ &{\quad=B_{t}^{T}\mathrm{E}_{t}^{\mathbb{Q}^{T}}\left[P_{T}\mathbf{1}_{\{P_{T}>K\}}\right]-K B_{t}^{T}\mathbb{Q}_{t}^{T}(P_{T}>K).}\end{array}
$$  

Here $\mathbb{Q}_{t}^{T}(P_{T}>K)$ denotes the probability (using the probability measure $\mathbb{Q}^{T}$ ) of $P_{T}>K$ given the information known at time. $t$ , i.e. the forward risk-adjusted probability of the option finishing in-the-money.  

The term $B_{t}^{T}\operatorname{E}_{t}^{\mathbb{Q}^{T}}[P_{T}\mathbf{1}_{\{P_{T}>K\}}]$ is the value at time $t$ Of a dividend of ${\cal P}_{T}{\bf1}_{\{{\cal P}_{T}>K\}}$ at time $T$ . For an option on a traded asset with a strictly positive price we can value the same payment using that [underlying asset](../../../Financial%20Instruments/Financial%20Derivatives%20and%20Quantitative%20Methods/Risk%20Neutral%20Pricing%20of%20Options.md) as the numeraire. In terms of the associated risk-adjusted measure. $\mathbb{Q}^{P}$ , the time. $t$ value of getting a dividend of $D_{T}$ at time $T$ .5 $P_{t}\operatorname{E}_{t}^{\mathbb{Q}^{P}}[D_{T}/P_{T}]$ . Using this with ${\cal D}_{T}=P_{T}{\bf1}_{\{P_{T}>K\}}$ we conclude that  
$$
B_{t}^{T}\operatorname{E}_{t}^{\mathbb{Q}^{T}}\left[P_{T}\mathbf{1}_{\{P_{T}>K\}}\right]=P_{t}\operatorname{E}_{t}^{\mathbb{Q}^{P}}\left[\mathbf{1}_{\{P_{T}>K\}}\right]=P_{t}\mathbb{Q}_{t}^{P}(P_{T}>K).
$$  

Now the call price formula in the following theorem is clear. The put price can be derived analogously or from the [put-call parity](../../../Financial%20Engineering/7.%20Black%20Scholes%20Model.md).  

Theorem 12.4 The price of a European call option on a [non-dividend paying asset](.md) is given by  
$$
C_{t}=P_{t}\mathbb{Q}_{t}^{P}(P_{T}>K)-K B_{t}^{T}\mathbb{Q}_{t}^{T}(P_{T}>K).
$$  

1In the computation we use the fact that the expected value of the indicator of an event is equal to the probability of that event. This follows from the general definition of an expected value, $\begin{array}{r}{\operatorname{E}[g(\omega)]=\int_{\omega\in\Omega}g(\omega)f(\omega)d\omega}\end{array}$ , where $f(\omega)$ is the probability density function of the state $\omega$ and the integration is over all possible states. The set of possible states can be divided into two sets, namely the set of states $\omega$ for which $P_{T}>K$ and the set of $\omega$ for which $P_{T}\leq K$ . Consequently,  
$$
\begin{array}{r l}&{\displaystyle\mathbb{E}[{\bf1}_{\{P_{T}>K\}}]=\int_{\omega\in\Omega}{\bf1}_{\{P_{T}>K\}}f(\omega)d\omega}\ &{\quad\quad\quad=\displaystyle\int_{\omega\colon P_{T}>K}1\cdot f(\omega)d\omega+\int_{\omega\colon P_{T}\le K}0\cdot f(\omega)d\omega}\ &{\quad\quad=\displaystyle\int_{\omega\colon P_{T}>K}f(\omega)d\omega,}\end{array}
$$  

which is exactly the probability of the event $P_{T}>K$  

The price. $\pi_{t}$ of a put option is given as  
$$
\pi_{t}=K B_{t}^{T}\mathbb{Q}_{t}^{T}(P_{T}\leq K)-P_{t}\mathbb{Q}_{t}^{P}(P_{T}\leq K).
$$  

Both probabilities in (12.12) show the probability of the option finishing in-the-money, but under two different probability measures. To compute the price of the European call option in a concrete model we "just"' have to compute these probabilities. In some cases, however, it is easier to work directly on (12.10) or (12.11).  

# 12.3.2 European option prices when the underlying is lognormal  

If we assume that the value of the underlying variable at the maturity of the option is lognormally distributed under the forward measure for maturity $T$ , a more explicit option [pricing](../../Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%207/Arbitrage%20Pricing%20of%20Derivatives.md) formula can be derived without too much work. For this reason many specific option [pricing](../../Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%207/Arbitrage%20Pricing%20of%20Derivatives.md) models build on assumptions leading to $P_{T}$ being lognormal under the measure $\mathbb{Q}^{T}$  

If $\ln P_{T}\sim N(m,v^{2})$ under the $\mathbb{Q}^{T}$ -measure conditional on the information at time $t<T$ , it follows that.  
$$
\begin{array}{r}{\mathbb{Q}_{t}^{T}(P_{T}>K)=\mathbb{Q}_{t}^{T}(\ln P_{T}>\ln K)=\mathbb{Q}_{t}^{T}\left(\frac{\ln P_{T}-m}{v}>\frac{\ln K-m}{v}\right)}\ {=\mathbb{Q}_{t}^{T}\left(\frac{\ln P_{T}-m}{v}<-\frac{\ln K-m}{v}\right)=N\left(\frac{m-\ln K}{v}\right),}\end{array}
$$  

where $N(\cdot)$ is the cumulative probability [distribution function](../../../Financial%20Engineering/Verification%20of%20Central%20Limit%20Theorem.md) of a normally distributed random variable with mean zero and variance one. The last equality follows since. $(\ln P_{T}-m)/v\sim N(0,1)$ Moreover, it follows from Theorem B.3 in Appendix B that.  
$$
\operatorname{E}_{t}^{\mathbb{Q}^{T}}\left[P_{T}\mathbf{1}_{\{P_{T}>K\}}\right]=\operatorname{E}_{t}^{\mathbb{Q}^{T}}[P_{T}]N\left(\frac{m-\ln K}{v}+v\right)=\operatorname{E}_{t}^{\mathbb{Q}^{T}}[P_{T}]N\left(\frac{\ln\left(\operatorname{E}_{t}^{\mathbb{Q}^{T}}[P_{T}]/K\right)+\frac{1}{2}v^{2}}{v}\right).
$$  

Substituting these results into (12.11), we get  
$$
C_{t}=B_{t}^{T}\operatorname{E}_{t}^{\operatorname{Q}^{T}}[P_{T}]N\left({\frac{\ln\left(\operatorname{E}_{t}^{\operatorname{Q}^{T}}[P_{T}]/K\right)+{\frac{1}{2}}v^{2}}{v}}\right)-K B_{t}^{T}N\left({\frac{\ln\left(\operatorname{E}_{t}^{\operatorname{Q}^{T}}[P_{T}]/K\right)-{\frac{1}{2}}v^{2}}{v}}\right)
$$  

In the typical case where. $P$ is the price of a [non-dividend paying asset](.md), we know that. $P_{t}={}$ $B_{t}^{T}\operatorname{E}_{t}^{\mathbb{Q}^{T}}[P_{T}]$ . Let us identify the relevant $v^{2}$ . By convention the [forward price](../../Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%2011/Forward%20Contracts%20and%20Forward%20Prices.md) of the underlying at time $T$ for immediate delivery is $F_{T}^{T}=P_{T}$ so we can focus on the dynamics of the forward. price $F_{t}^{T}=P_{t}/B_{t}^{T}$ . This is easier since we know that the [forward price](../../Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%2011/Forward%20Contracts%20and%20Forward%20Prices.md) is a martingale under the. measure $\mathbb{Q}^{T}$ so that the drift is zero. By [Ito's Lemma](../../../Financial%20Engineering/Determining%20the%20Stochastic%20Process%20for%20a%20Forward%20Contract%20from%20Ito’s%20Lemma.md) the sensitivity of the [forward price](../../Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%2011/Forward%20Contracts%20and%20Forward%20Prices.md) is given. by the sensitivity of the underlying and the sensitivity of the zero-coupon bond price so for this purpose we can ignore the drift terms in $P_{t}$ and $B_{t}^{T}$ . If we write their. $\mathbb{Q}^{T}$ -dynamics as  
$$
\begin{array}{r l}&{{d{P}_{t}}={P}_{t}\left[...d t+\sigma(t)d z_{1t}^{T}\right],}\ &{d B_{t}^{T}=B_{t}^{T}\left[...d t+\sigma_{B}(T-t)\rho d z_{1t}^{T}+\sigma_{B}(T-t)\sqrt{1-\rho^{2}}d z_{2t}^{T}\right],}\end{array}
$$  

where $(z_{1}^{T},z_{2}^{T})$ is a two-dimensional standard [Brownian motion](../Chapter%202%20-%20Uncertainty,%20Information,%20and%20Stochastic%20Processes/Continuous-Time%20Stochastic%20Processes.md) under $\mathbb{Q}^{T}$ , then $\sigma(t)$ is the volatility of the [underlying asset](../../../Financial%20Instruments/Financial%20Derivatives%20and%20Quantitative%20Methods/Risk%20Neutral%20Pricing%20of%20Options.md),. $\sigma_{B}(T-t)$ is the volatility of the zero-coupon bond price, and $\rho$ is the correlation between shocks to those two prices. We have assumed that $\rho$ is a constant, that. the volatility of the [underlying asset](../../../Financial%20Instruments/Financial%20Derivatives%20and%20Quantitative%20Methods/Risk%20Neutral%20Pricing%20of%20Options.md) $\sigma(t)$ is a deterministic function of time, and that $\sigma_{B}(\cdot)$ is a deterministic function of the time-to-maturity of the bond since these are the only reasonable assumptions that will lead to. $P_{T}$ being lognormal under $\mathbb{Q}^{T}$ . Now the [forward price dynamics](../../../Financial%20Engineering/Determining%20the%20Stochastic%20Process%20for%20a%20Forward%20Contract%20from%20Ito’s%20Lemma.md) will be  
$$
\begin{array}{l}{{\displaystyle d F_{t}^{T}=\frac{1}{B_{t}^{T}}\sigma(t)S_{t}d z_{1t}^{T}-\frac{S_{t}}{(B_{t}^{T})^{2}}B_{t}^{T}\left(\sigma_{B}(T-t)\rho d z_{1t}^{T}+\sigma_{B}(T-t)\sqrt{1-\rho^{2}}d z_{2t}^{T}\right)}}\ {{\mathrm{}~=F_{t}^{T}\left[\left(\sigma(t)-\rho\sigma_{B}(T-t)\right)d z_{1t}^{T}-\sqrt{1-\rho^{2}}\sigma_{B}(T-t)d z_{2t}^{T}\right],}}\end{array}
$$  

which implies that  
$$
\mathfrak{a}P_{T}=\ln F_{T}^{T}=\ln F_{t}^{T}-\frac{1}{2}v_{F}(T,t)^{2}+\int_{t}^{T}\left(\sigma(u)-\rho\sigma_{B}(T-u)\right)d z_{1u}^{T}-\int_{t}^{T}\sqrt{1-\rho^{2}}\sigma_{B}(T-u)d z_{2u}^{T},
$$  

where  
$$
v_{F}(t,T)=\left(\int_{t}^{T}\left(\sigma(u)^{2}+\sigma_{B}(T-u)^{2}-2\rho\sigma(u)\sigma_{B}(T-u)\right)d u\right)^{1/2}
$$  

is the volatility of the [forward price](../../Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%2011/Forward%20Contracts%20and%20Forward%20Prices.md). Now we see that $\ln P_{T}\sim N(\ln F_{t}^{T}-{\textstyle\frac{1}{2}}v_{F}(t,T)^{2},v_{F}(t,T)^{2})$ under $\mathbb{Q}^{T}$  

We summarize the above results in the following theorem:  

Theorem 12.5 If $\ln{P_{T}}$ conditional on time t information is normally distributed with variance $v^{2}$ under the forward measure $\mathbb{Q}^{T}$ , the price of a European option maturing at time $T$ is given by  
$$
C_{t}=B_{t}^{T}\operatorname{E}_{t}^{\boldsymbol{\mathbb{Q}}^{T}}[P_{T}]N(d)-K B_{t}^{T}N(d-v),
$$  

where  
$$
d=\frac{\ln\left(\mathrm{E}_{t}^{\mathbb{Q}^{T}}[P_{T}]/K\right)+\frac{1}{2}v^{2}}{v}.
$$  

In particular, if $P$ is the price of a [non-dividend paying asset](.md) and $\ln{P_{T}}$ is normally distributed under $\mathbb{Q}^{T}$ , the call price is  
$$
\boldsymbol{C_{t}}=\boldsymbol{P_{t}}\boldsymbol{N}\left(\boldsymbol{d}(\boldsymbol{F_{t}^{T}},t)\right)-\boldsymbol{K}\boldsymbol{B_{t}^{T}}\boldsymbol{N}\left(\boldsymbol{d}(\boldsymbol{F_{t}^{T}},t)-\boldsymbol{v_{F}}(t,T)\right),
$$  

where $F_{t}^{T}=P_{t}/B_{t}^{T}$  
$$
d(F_{t}^{T},t)=\frac{\ln\left(F_{t}^{T}/K\right)+\frac{1}{2}v_{F}(t,T)^{2}}{v_{F}(t,T)}
$$  

and $v_{F}(t,T)$ is given by (12.15).  

# 12.3.3 The Black-Scholes-Merton model for stock option pricing  

While option [pricing](../../Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%207/Arbitrage%20Pricing%20of%20Derivatives.md) models date back at least to Bachelier (1900), the most famous model is the [Black-Scholes](../../../Financial%20Engineering/Mathematical%20Modeling%20of%20Derivative%20Pricing.md)-[Merton model](../../../Credit%20Markets/Credit%20Markets%20Session%205.md) developed by Black and Scholes (1973) and [Merton](../../../Credit%20Markets/Credit%20Markets%20Session%205.md) (1973c) for the [pricing](../../Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%207/Arbitrage%20Pricing%20of%20Derivatives.md) of a European option on a stock. The model is formulated in continuous time and assumes. that the [risk-free interest rate](Exercises.md). $r$ (continuously compounded) is constant over time and that the. price $S_{t}$ of the underlying stock follows a continuous [stochastic process](../../../The%20Ornstein-Uhlenbeck%20(OU)%20Process.md) with a constant relative. volatility, i.e.  
$$
d S_{t}=\mu_{t}S_{t}d t+\sigma S_{t}d z_{t},
$$  

where $\sigma$ is a constant and $\mu$ is a "nice" process. Furthermore, we assume that the underlying stock pays no dividends in the life of the option.  

With constant [interest rates](../../Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%202/Interest%20Rate%20Quotations.md), $B_{t}^{T}=e^{-r(T-t)}$ and the [risk-neutral measure](../../../Financial%20Engineering/Verifying%20Martingale%20Property%20with%20Q.md) is identical to the forward measure, $\mathbb{Q}=\mathbb{Q}^{T}$ . Since the risk-neutral expected rate of return of any asset is equal to the [risk-free rate of return](../../../Financial%20Instruments/Financial%20Instruments.md), the [risk-neutral dynamics](../../Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%209/The%20Vasicek%20Model.md) of the [stock price](../../../Financial%20Engineering/Derivatives/Part%20IV%20-%20Options/Chapter%2016%20-%20Black–Scholes%20Model.md) is  
$$
d S_{t}=S_{t}\left[r d t+\sigma d z_{t}^{\mathbb{Q}}\right],
$$  

where $z^{\mathbb{Q}}=(z_{t}^{\mathbb{Q}})$ is a standard [Brownian motion](../Chapter%202%20-%20Uncertainty,%20Information,%20and%20Stochastic%20Processes/Continuous-Time%20Stochastic%20Processes.md) under. $\mathbb{Q}$ . It follows that the [stock price](../../../Financial%20Engineering/Derivatives/Part%20IV%20-%20Options/Chapter%2016%20-%20Black–Scholes%20Model.md) is a. [geometric Brownian motion](../../../Financial%20Instruments/Black%20Scholes%20Derivation.md) under. $\mathbb{Q}=\mathbb{Q}^{T}$ and, in particular, we know from Section 2.6.7 that  
$$
\ln S_{T}=\ln S_{t}+\left(r-\frac{1}{2}\sigma^{2}\right)(T-t)+\sigma(z_{T}^{\mathbb{Q}}-z_{t}^{\mathbb{Q}}).
$$  

Hence $S_{T}$ is lognormal and $\mathrm{Var}_{t}^{\mathbb{Q}}[\ln S_{T}]=\sigma^{2}(T-t)$ .We can apply Theorem 12.5 and since $\sigma_{B}(T-t)=0$ with constant [interest rates](../../Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%202/Interest%20Rate%20Quotations.md), $v_{F}=\sigma\sqrt{T-t}$ . The [forward price](../../Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%2011/Forward%20Contracts%20and%20Forward%20Prices.md) of the stock is $F_{t}^{T}=S_{t}e^{r(T-t)}$ . We summarize in the following theorem:  

Theorem 12.6 ([Black-Scholes](../../../Financial%20Engineering/Mathematical%20Modeling%20of%20Derivative%20Pricing.md)-[Merton](../../../Credit%20Markets/Credit%20Markets%20Session%205.md)) Assume that the stock pays no dividend, the [stock price dynamics](../../../Financial%20Engineering/Verifying%20Martingale%20Property%20with%20Q.md) is of the form (12.18) and the short-term [risk-free rate](../../../Financial%20Instruments/Black%20Scholes%20Derivation.md) is constant. Then the. price of a European call option on the stock is given by.  
$$
C_{t}=S_{t}N\left(d(S_{t},t)\right)-K e^{-r(T-t)}N\left(d(S_{t},t)-\sigma\sqrt{T-t}\right),
$$  

where  
$$
d(S_{t},t)=\frac{\ln(S_{t}/K)+\left(r+\frac{1}{2}\sigma^{2}\right)(T-t)}{\sigma\sqrt{T-t}}.
$$  

Equation (12.20) is the famous [Black-Scholes-Merton equation](Exercises.md).  

Alternatively, we can derive the above result using (12.12) which implies that the price of a European call option on a stock is given by.  
$$
C_{t}=S_{t}\mathbb{Q}_{t}^{S}(S_{T}>K)-K B_{t}^{T}\mathbb{Q}_{t}(S_{T}>K),
$$  

where $\mathbb{Q}^{S}$ is the risk-adjusted measure associated with the underlying stock. With the [risk-neutral dynamics](../../Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%209/The%20Vasicek%20Model.md) (12.19), we have  
$$
\begin{array}{r l}&{\mathbb{Q}_{t}(S_{T}>K)=\mathbb{Q}_{t}(\ln S_{T}>\ln K)}\ &{\qquad=\mathbb{Q}_{t}\left(\ln S_{t}+\left(r-\frac{1}{2}\sigma^{2}\right)(T-t)+\sigma(z_{T}^{0}-z_{t}^{0})>\ln K\right)}\ &{\qquad=\mathbb{Q}_{t}\left(\frac{z_{T}^{0}-z_{t}^{0}}{\sqrt{T}-t}>-\frac{\ln(S_{t}/K)+\left(r-\frac{1}{2}\sigma^{2}\right)(T-t)}{\sigma\sqrt{T}-t}\right)}\ &{\qquad=\mathbb{Q}_{t}\left(\frac{z_{T}^{0}-z_{t}^{0}}{\sqrt{T}-t}<\frac{\ln(S_{t}/K)+\left(r-\frac{1}{2}\sigma^{2}\right)(T-t)}{\sigma\sqrt{T}-t}\right)}\ &{\qquad=N\left(\frac{\ln(S_{t}/K)+\left(r-\frac{1}{2}\sigma^{2}\right)(T-t)}{\sigma\sqrt{T}-t}\right).}\end{array}
$$  

According to (11.32), the dynamics of the [stock price](../../../Financial%20Engineering/Derivatives/Part%20IV%20-%20Options/Chapter%2016%20-%20Black–Scholes%20Model.md) under the measure $\mathbb{Q}^{S}$ is  
$$
d S_{t}=S_{t}\left[\left(r+\sigma^{2}\right)d t+\sigma d z_{t}^{S}\right]
$$  

so that $S$ is also a [geometric Brownian motion](../../../Financial%20Instruments/Black%20Scholes%20Derivation.md) under the measure $\mathbb{Q}^{S}$ . Analogously to the above.   
equations it can be shown that.  
$$
\mathbb{Q}_{t}^{S}(S_{T}>K)=N\left(\frac{\ln(S_{t}/K)+\left(r+\frac{1}{2}\sigma^{2}\right)(T-t)}{\sigma\sqrt{T-t}}\right).
$$  

Now the option price in (12.20) follows.  

The [Black-Scholes-Merton equation](Exercises.md) states the call option price in terms of five quantities:  

(1) the price of the underlying stock,   
(2) the price of the zero-coupon bond maturing at expiry of the option (or, equivalently, the [risk-free interest rate](Exercises.md)),   
(3) the time-to-expiration of the option,   
(4) the [exercise price](.md) (or, equivalently, the moneyness $S_{t}/K$ of the option),   
(5) the volatility of the underlying stock.  

It can be shown (you are asked to do that in Exercise 12.2) by straightforward differentiation that  
$$
\frac{\partial C_{t}}{\partial S_{t}}=N\left(d(S_{t},t)\right),\quad\frac{\partial^{2}C_{t}}{\partial S_{t}^{2}}=\frac{n\left(d(S_{t},t)\right)}{S_{t}\sigma\sqrt{T-t}},
$$  

where $n(\cdot)=N^{\prime}(\cdot)$ is the probability density function of an $N(0,1)$ random variable, and.  
$$
\frac{\partial C_{t}}{\partial t}=-\frac{-S_{t}\sigma n\left(d(S_{t},t)\right)}{2\sqrt{T-t}}-r K B_{t}^{T}N\left(d(S_{t},t)-\sigma\sqrt{T-t}\right),
$$  

using that $B_{t}^{T}=\exp\{-r(T-t)\}$ . In particular, the call option price is an increasing, convex. function of the price of the underlying stock. The call price is increasing in the volatility $\sigma$ (obviously) decreasing in the [exercise price](.md) $K$ , and increasing in the zero-coupon bond price (and, hence, decreasing in the [risk-free rate](../../../Financial%20Instruments/Black%20Scholes%20Derivation.md) $r$  

Note that the [Black-Scholes](../../../Financial%20Engineering/Mathematical%20Modeling%20of%20Derivative%20Pricing.md)-[Merton](../../../Credit%20Markets/Credit%20Markets%20Session%205.md) price of the call option does not involve any [preference](../Chapter%205%20-%20Modeling%20the%20Preferences%20of%20Individuals/Utility%20Indices.md) parameters or a [market price of risk](Exercises.md) associated with the shock $z$ to the underlying [stock price](../../../Financial%20Engineering/Derivatives/Part%20IV%20-%20Options/Chapter%2016%20-%20Black–Scholes%20Model.md). On the other hand, it involves the price of the underlying stock. In the [Black-Scholes](../../../Financial%20Engineering/Mathematical%20Modeling%20of%20Derivative%20Pricing.md)-[Merton model](../../../Credit%20Markets/Credit%20Markets%20Session%205.md) the option is a redundant asset. There is only one source of risk and with the stock and the [risk-free asset](../../../Financial%20Engineering/2.%20Forwards,%20Swaps,%20Futures,%20and%20Options.md), the market is already complete. Any additional asset affected only by the same shock will be redundant.  

The option can be perfectly replicated by a trading strategy in the stock and the [risk-free asset](../../../Financial%20Engineering/2.%20Forwards,%20Swaps,%20Futures,%20and%20Options.md). At any time $t<T$ , the [portfolio](../../../Advanced%20Investments/An%20Asset%20Allocation%20Primer.md) consists of $\theta_{t}^{S}=N\left(d(S_{t},t)\right)\in\mathbf{\Gamma}(0,1)$ units of the stock and $\theta_{t}^{B}=-K N\left(d(S_{t},t)-\sigma\sqrt{T-t}\right)\in(-K,0)$ units of the zero-coupon bond maturing at time $T$ Clearly, the value of this [portfolio](../../../Advanced%20Investments/An%20Asset%20Allocation%20Primer.md) is identical to the value of the call option, $\theta_{t}^{S}S_{t}+\theta_{t}^{B}B_{t}^{\prime I^{\prime}}=C_{t}$ Since $\boldsymbol{C}_{t}=\boldsymbol{C}(\boldsymbol{S}_{t},t)$ , it follows from [Ito's Lemma](../../../Financial%20Engineering/Determining%20the%20Stochastic%20Process%20for%20a%20Forward%20Contract%20from%20Ito’s%20Lemma.md) and the [derivatives](../../Financial%20Trading%20and%20Markets/Chapter%209%20Arbitrage%20and%20Hedging%20With%20Options.md) of $C$ computed above that the dynamics of the call price is  
$$
{\begin{array}{r l}&{d C_{t}={\cfrac{\partial C_{t}}{\partial t}}~d t+{\cfrac{\partial C_{t}}{\partial S_{t}}}~d S_{t}+{\cfrac{1}{2}}~{\cfrac{\partial^{2}C_{t}}{\partial S_{t}^{2}}}(d S_{t})^{2}}\ &{\qquad=\left(N\left(d(S_{t},t)\right)\mu(S_{t},t)-r K B_{t}^{T}N\left(d(S_{t},t)-\sigma{\sqrt{T-t}}\right)\right)~d t+N\left(d(S_{t},t)\right)\sigma S_{t}~d z_{t}.}\end{array}}
$$  

The dynamics of the trading strategy is  
$$
\begin{array}{r l}&{\overset{S}{t}d S_{t}+\theta_{t}^{B}d B_{t}^{T}=N\left(d(S_{t},t)\right)d S_{t}-K N\left(d(S_{t},t)-\sigma\sqrt{T-t}\right)d B_{t}^{T}}\ &{\qquad=\left(N\left(d(S_{t},t)\right)\mu(S_{t},t)-r K B_{t}^{T}N\left(d(S_{t},t)-\sigma\sqrt{T-t}\right)\right)d t+N\left(d(S_{t},t)\right)\sigma S_{t}d z_{t},}\end{array}
$$  

which is identical to $d C_{t}$ . The trading strategy is therefore replicating the option  

Applying the [put-call parity](../../../Financial%20Engineering/7.%20Black%20Scholes%20Model.md) (12.9), we obtain a European put option price of  
$$
\pi(S_{t},t)=K B_{t}^{T}N\left(-[d(S_{t},t)-\sigma\sqrt{T-t}]\right)-S_{t}N\left(-d(S_{t},t)\right).
$$  

In the above model, [interest rates](../../Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%202/Interest%20Rate%20Quotations.md) and hence bond price were assumed to be constant. However, we can easily generalize to the case where bond prices vary stochastically with a deterministic volatility and a constant correlation with the [stock price](../../../Financial%20Engineering/Derivatives/Part%20IV%20-%20Options/Chapter%2016%20-%20Black–Scholes%20Model.md). Assuming that the dynamics of the [stock price](../../../Financial%20Engineering/Derivatives/Part%20IV%20-%20Options/Chapter%2016%20-%20Black–Scholes%20Model.md) and the price of the zero-coupon bond maturing at time $T$ are given by  
$$
\begin{array}{r l}&{\quad d S_{t}=S_{t}\left[\ldots d t+\sigma d z_{1t}\right],}\ &{\quad d B_{t}^{T}=B_{t}^{T}\left[\ldots d t+\sigma_{B}(T-t)\rho d z_{1t}+\sigma_{B}(T-t)\sqrt{1-\rho^{2}}d z_{2t}\right],}\end{array}
$$  

we are still in the setting of Section 12.3.2 and can apply Theorem 12.5.  

Theorem 12.7 Suppose the stock pays no dividend, has a constant volatility $\sigma$ , and a constant correlation $\rho$ with the price of the zero-coupon bond maturing at time $T$ , and suppose that this bond. has a deterministic volatility. $\sigma_{B}(T-t)$ . Then the price of a European call option on the stock is given by  
$$
C_{t}=S_{t}N\left(\boldsymbol{d}(\boldsymbol{F}_{t}^{T},t)\right)-K\boldsymbol{B}_{t}^{T}N\left(\boldsymbol{d}(\boldsymbol{F}_{t}^{T},t)-\boldsymbol{v}_{F}(t,T)\right),
$$  

where $F_{t}^{T}=S_{t}/B_{t}^{T}$  
$$
\begin{array}{r l}&{{d(F_{t}^{T},t)}=\cfrac{\ln(F_{t}^{T}/K)+\frac{1}{2}v_{F}(t,T)^{2}}{v_{F}(t,T)},}\ &{{v_{F}(t,T)}=\left(\displaystyle\int_{t}^{T}\left(\sigma^{2}+\sigma_{B}(T-u)^{2}-2\rho\sigma\sigma_{B}(T-u)\right)d u\right)^{1/2}.}\end{array}
$$  

In practice $\sigma_{B}(T-t)$ is typically much smaller than $\sigma$ and the approximation.  
$$
v_{F}(t,T)\approx{\sqrt{\int_{t}^{T}\sigma^{2}d u}}=\sigma{\sqrt{T-t}}
$$  

is not too bad. With that approximation you will get the same call price using (12.27) as by using. the [Black-Scholes-Merton equation](Exercises.md) (12.20) with the zero-coupon yield. $y_{t}^{T}=-(\ln B_{t}^{T})/(T-t)$ replacing $r$ . In this sense the above theorem supports the use of the [Black-Scholes-Merton equation](Exercises.md) even when [interest rates](../../Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%202/Interest%20Rate%20Quotations.md) are stochastic. Note, however, that the above theorem requires the bond [price volatility](../../Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%206%20Options%20on%20Non-Price%20Variables/Black%20Models%20for%20Bond%20Price%20Options%20Capsfloors.md) to be a deterministic function of the time-to-maturity of the bond. This will only. be satisfied if the short-term [risk-free interest rate](Exercises.md). $r_{t}$ follows a Gaussian process, e.g. an Ornstein-. Uhlenbeck process as assumed in the [Vasicek model](../../../Fixed%20Income%20Asset%20Pricing/Fixed%20Income%20Lecture%20Notes/Vasicek%20Short%20Rate%20Model.md) introduced in Section 10.5.1. While such models are very nice to work with, they are not terribly realistic. On the other hand, for short maturities and relatively stable [interest rates](../../Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%202/Interest%20Rate%20Quotations.md), it is probably reasonable to approximate the bond [price volatility](../../Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%206%20Options%20on%20Non-Price%20Variables/Black%20Models%20for%20Bond%20Price%20Options%20Capsfloors.md) with a deterministic function or even approximate it with zero as the Black-ScholesMerton model implicitly does.  

The assumption of a constant [stock price volatility](../../Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%205%20Options%20on%20Prices%20and%20Hedge-Based%20Valuation/Black-Scholes%20Model%20and%20Extensions.md) is important for the derivations of the BlackScholes-[Merton](../../../Credit%20Markets/Credit%20Markets%20Session%205.md) option [pricing](../../Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%207/Arbitrage%20Pricing%20of%20Derivatives.md) formula. Alas, it is not realistic. The volatility of a stock can be estimated from historical variations in the [stock price](../../../Financial%20Engineering/Derivatives/Part%20IV%20-%20Options/Chapter%2016%20-%20Black–Scholes%20Model.md) and the estimate varies with the time period used in the estimation-both over short periods and long periods. Another measure of the volatility of a stock is its [implied volatility](../../Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%205%20Options%20on%20Prices%20and%20Hedge-Based%20Valuation/A%20Real-Life%20Option%20Pricing%20Exercise.md). Given the current [stock price](../../../Financial%20Engineering/Derivatives/Part%20IV%20-%20Options/Chapter%2016%20-%20Black–Scholes%20Model.md) $S_{t}$ and interest rate $r$ , we can define an [implied volatility](../../Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%205%20Options%20on%20Prices%20and%20Hedge-Based%20Valuation/A%20Real-Life%20Option%20Pricing%20Exercise.md) of the stock for any option traded upon that stock (i.e.. for any [exercise price](.md) $K$ and any maturity $T$ ) as the value of $\sigma$ you need to plug into the Black-. Scholes-[Merton](../../../Credit%20Markets/Credit%20Markets%20Session%205.md) formula to get a match with the observed market price of the option. Since the [Black-Scholes](../../../Financial%20Engineering/Mathematical%20Modeling%20of%20Derivative%20Pricing.md)-[Merton](../../../Credit%20Markets/Credit%20Markets%20Session%205.md) option price is an increasing function of the volatility, there will be a unique value of $\sigma$ that does the job. Looking at simultaneous prices of different options on the same stock, the [implied volatility](../../Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%205%20Options%20on%20Prices%20and%20Hedge-Based%20Valuation/A%20Real-Life%20Option%20Pricing%20Exercise.md) is found to vary with the [exercise price](.md) and the maturity of the option. If the [Black-Scholes](../../../Financial%20Engineering/Mathematical%20Modeling%20of%20Derivative%20Pricing.md)-[Merton](../../../Credit%20Markets/Credit%20Markets%20Session%205.md) assumptions were correct, you would find the same [implied volatility](../../Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%205%20Options%20on%20Prices%20and%20Hedge-Based%20Valuation/A%20Real-Life%20Option%20Pricing%20Exercise.md) for all options on the same underlying..  

Various alternatives to the constant [volatility assumption](../../Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%205%20Options%20on%20Prices%20and%20Hedge-Based%20Valuation/Residual%20Risk%20of%20Options%20Gamma%20Vega%20and%20Volatil.md) have been proposed. Black and Cox (1976) replace the constant $\sigma$ by $\sigma S_{t}^{\alpha}$ for some power $\alpha$ . Here the volatility is a function of the. [stock price](../../../Financial%20Engineering/Derivatives/Part%20IV%20-%20Options/Chapter%2016%20-%20Black–Scholes%20Model.md) and therefore perfectly correlated with the [stock price](../../../Financial%20Engineering/Derivatives/Part%20IV%20-%20Options/Chapter%2016%20-%20Black–Scholes%20Model.md). This extension does not seem sufficient. The [stochastic volatility](../../../Course%20Notes/Python/QuantLib-Python/Valuing%20European%20Option%20Using%20the%20Heston%20Model%20in%20QuantLib%20Python.md) models of Hull and White (1987) and [Heston](../../../Financial%20Engineering/Mathematical%20Modeling%20of%20Derivative%20Pricing.md) (1993) allow the volatility to be affected by another exogenous shock than the shock to the [stock price](../../../Financial%20Engineering/Derivatives/Part%20IV%20-%20Options/Chapter%2016%20-%20Black–Scholes%20Model.md) itself. With these extensions it is possible to match the option prices in the model with observed option prices. In the [stochastic volatility](../../../Course%20Notes/Python/QuantLib-Python/Valuing%20European%20Option%20Using%20the%20Heston%20Model%20in%20QuantLib%20Python.md) models, the market is no longer complete, and the option prices will depend on the market price of volatility risk, which then has to be specified and estimated.  

Occasionally stock prices change a lot over a very short period of time, for example in the so-called [stock market](../../Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20III%20THE%20PLAYERS/Chapter%2012%20-%20Hedge%20Fund%20Strategies/Hedge%20Fund%20Strategies.md) crashes. Such dramatic variations are probably better modeled by jump. processes than by pure diffusion models like those discussed in this book. Several papers study. the [pricing](../../Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%207/Arbitrage%20Pricing%20of%20Derivatives.md) of options on stocks, when the [stock price](../../../Financial%20Engineering/Derivatives/Part%20IV%20-%20Options/Chapter%2016%20-%20Black–Scholes%20Model.md) can jump. Some prominent examples are. [Merton](../../../Credit%20Markets/Credit%20Markets%20Session%205.md) (1976) and Madan, Carr, and Chang (1998).  

# 12.3.4 Options on bonds  

Consider a European call option on a zero-coupon bond. Let. $T$ be the maturity of the option and. $T^{*}>T$ the maturity of the bond. $K$ is the [exercise price](.md). Let $C_{t}^{K,T,T^{*}}$ denote the price at time $t$ of a European call option on this zero-coupon bond. The dividend of the option at time $T$ is  
$$
C_{T}^{K,T,T^{*}}=\operatorname*{max}\left(B_{T}^{T^{*}}-K,0\right).
$$  

The option price is generally characterized by  
$$
C_{t}^{K,T,T^{*}}={B_{t}^{T}}^{*}\mathbb{Q}_{t}^{T^{*}}\left({B_{T}^{T^{*}}>K}\right)-K{B_{t}^{T}}\mathbb{Q}_{t}^{T}\left({B_{T}^{T^{*}}>K}\right),
$$  

where $\mathbb{Q}^{T^{*}}$ and $\mathbb{Q}^{T}$ are the forward measures for maturities $T^{*}$ and $T$ , respectively.  

If $B_{T}^{T^{*}}$ is lognormally distributed under the forward measure for maturity. $T$ , we know from Theorem 12.5 that we can find a nice closed-form solution. This is for example the case in the  

[Vasicek model](../../../Fixed%20Income%20Asset%20Pricing/Fixed%20Income%20Lecture%20Notes/Vasicek%20Short%20Rate%20Model.md) introduced in Section 10.5.1. Given the [Ornstein-Uhlenbeck process](../Chapter%2010%20-%20The%20Economics%20of%20the%20Term%20Structure%20of%20Interest%20Rates/Equilibrium%20Interest%20Rate%20Models.md) for the shortterm [risk-free rate](../../../Financial%20Instruments/Black%20Scholes%20Derivation.md),  
$$
d r_{t}=\kappa\left(\bar{r}-r_{t}\right)d t+\sigma_{r}d z_{t},
$$  

and a constant market price of [interest rate risk](../../../Fixed%20Income%20Asset%20Pricing/Analysis%20of%20Fixed%20Income%20Securities.md) $\lambda$ , the price of a zero-coupon bond price maturing at time $s$ is  
$$
B_{t}^{s}=e^{-a(s-t)-b(s-t)r_{t}},
$$  

cf. (10.37), where $a(\cdot)$ and $b(\cdot)$ are defined in (10.38) and (10.36), respectively. The change to the forward measure requires identification of the bond [price sensitivity](../../Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%204/Duration.md). An application of [Ito's Lemma](../../../Financial%20Engineering/Determining%20the%20Stochastic%20Process%20for%20a%20Forward%20Contract%20from%20Ito’s%20Lemma.md) gives the bond [price dynamics](../../../Financial%20Engineering/Derivatives/Part%20XII%20-%20Price%20Dynamics/Chapter%2047%20-%20Asset%20Price%20Dynamics.md).  
$$
d B_{t}^{s}=B_{t}^{s}\left[...d t-\sigma_{r}b(s-t)d z_{t}\right]
$$  

so that the bond [price sensitivity](../../Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%204/Duration.md) is $\sigma_{B}(s-t)=-\sigma_{r}b(s-t)$ .(Since this is negative, the bond [price volatility](../../Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%206%20Options%20on%20Non-Price%20Variables/Black%20Models%20for%20Bond%20Price%20Options%20Capsfloors.md) is $-\sigma_{B}(s-t)=\sigma_{r}b(s-t)$ .) It now follows from (11.28) that the $\mathbb{Q}^{T}$ -dynamics of the [short-term interest rate](../../Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%209/The%20Gauss%20Model.md) is  
$$
\begin{array}{r l}&{d r_{t}=\left(\kappa[\bar{r}-r_{t}]-\sigma_{r}[\lambda-\sigma_{B}(T-t)]\right)d t+\sigma_{r}d z_{t}^{T}}\ &{\qquad=\kappa\left(\tilde{r}(T-t)-r_{t}\right)d t+\sigma_{r}d z_{t}^{T},}\end{array}
$$  

where $\tilde{r}(\tau)=\bar{r}-\sigma_{r}\lambda/\kappa-\sigma_{r}^{2}b(\tau)/\kappa$ and $z^{T}=(z_{t}^{T})$ is a standard [Brownian motion](../Chapter%202%20-%20Uncertainty,%20Information,%20and%20Stochastic%20Processes/Continuous-Time%20Stochastic%20Processes.md) under. $\mathbb{Q}^{T}$ Under the $\mathbb{Q}^{T}$ -measure, the [short rate](../../../Fixed%20Income%20Asset%20Pricing/Fixed%20Income%20Lecture%20Notes/An%20Overview%20of%20the%20Vasicek%20Short%20Rate%20Model.md) behaves as an [Ornstein-Uhlenbeck process](../Chapter%2010%20-%20The%20Economics%20of%20the%20Term%20Structure%20of%20Interest%20Rates/Equilibrium%20Interest%20Rate%20Models.md) but with a deterministically changing mean-reversion level $\tilde{r}(T-t)$ .Hence, $r_{T}$ will be normally distributed. under $\mathbb{Q}^{T}$ and, consequently, the price of the underlying zero-coupon bond at the maturity of the. option, $B_{T}^{T^{*}}=\exp\{-a(T^{*}-T)-b(T^{*}-T)r_{T}\}$ , will be lognormally distributed under. $\mathbb{Q}^{T}$ . We can therefore apply Theorem 12.5 and conclude that the price of the option is.  
$$
C_{t}^{K,T,T^{*}}=B_{t}^{T^{*}}N(d)-K B_{t}^{T}N\left(d-v_{F}(t,T,T^{*})\right),
$$  

where  
$$
d=\frac{\ln{\left(\frac{B_{t}^{T^{*}}}{K B_{t}^{T}}\right)}+\frac{1}{2}v_{F}(t,T,T^{*})^{2}}{v_{F}(t,T,T^{*})}
$$  

and, using the fact that the underlying zero-coupon bond price is perfectly correlated with the price of the zero-coupon bond maturing at $T$  
$$
\begin{array}{c}{{v_{F}(t,T,T^{*})^{2}=\displaystyle\int_{t}^{T}\left(\sigma_{B}(T^{*}-u)-\sigma_{B}(T-u)\right)^{2}d u}}\ {{{}}}\ {{{}=\displaystyle\sigma_{r}^{2}\displaystyle\int_{t}^{T}\left(b(T^{*}-u)-b(T-u)\right)^{2}d u}}\ {{{}=\displaystyle\frac{\sigma_{r}^{2}}{\kappa^{2}}\displaystyle\int_{t}^{T}\left(e^{-\kappa(T-u)}-e^{-\kappa(T^{*}-u)}\right)^{2}d u}}\ {{{}=\displaystyle\frac{\sigma_{r}^{2}}{\kappa^{3}}\left(1-e^{-\kappa(T^{*}-T)}\right)^{2}\left(1-e^{-2\kappa(T-t)}\right).}}\end{array}
$$  

In many other models of [interest rates](../../Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%202/Interest%20Rate%20Quotations.md) and bond prices, an option [pricing](../../Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%207/Arbitrage%20Pricing%20of%20Derivatives.md) formula very similar to (12.29) can be derived. For example, in the Cox-Ingersoll-Ross model introduced in Section 10.5.2, the price of a European call option on a zero-coupon bond is of the form.  
$$
C_{t}^{K,T,T^{*}}=B_{t}^{T^{*}}\chi^{2}(h_{1};f,g_{1})-K B_{t}^{T}\chi^{2}(h_{2};f,g_{2}).
$$  

where $\chi^{2}(\cdot;f,g)$ is the cumulative probability [distribution function](../../../Financial%20Engineering/Verification%20of%20Central%20Limit%20Theorem.md) of a non-centrally $\chi^{2}$ -distributed random variable with $f$ degrees of freedom and non-centrally parameter $g$ . For details see, e.g., Munk (2005, Ch. 7).  

The options considered above are options on zero-coupon bonds. Traded bond options usually have a coupon bond as the underlying. Fortunately, the [pricing](../../Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%207/Arbitrage%20Pricing%20of%20Derivatives.md) formulas for options on zerocoupon bonds can, under some assumptions, be used in the [pricing](../../Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%207/Arbitrage%20Pricing%20of%20Derivatives.md) of options on coupon bonds. First some notation. The underlying coupon bond is assumed to pay $Y_{i}$ at time $T_{i}$ $i=1,2,\dots,n$ where $T_{1}<T_{2}<\cdots<T_{n}$ , so that the price of the bond is  
$$
B_{t}=\sum_{T_{i}>t}Y_{i}B_{t}^{T_{i}},
$$  

where we sum over all the future payment dates. Let $C_{t}^{K,T,\mathrm{cpn}}$ denote the price at time $t$ of a European call option on the coupon bond, where. $K$ is the [exercise price](.md) and $T$ is the [expiration date](../../../Financial%20Instruments/Financial%20Derivatives%20and%20Quantitative%20Methods/Risk%20Neutral%20Pricing%20of%20Options.md) of the option. In reasonable one-factor models, the price of a given zero-coupon bond will be a decreasing function of the [short-term interest rate](../../Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%209/The%20Gauss%20Model.md). In both the [Vasicek model](../../../Fixed%20Income%20Asset%20Pricing/Fixed%20Income%20Lecture%20Notes/Vasicek%20Short%20Rate%20Model.md) and the CoxIngersoll-Ross model the zero-coupon bond price is of the form. $B_{t}^{T}=\exp\{-a(T-t)-b(T-t)r_{t}\}$ and since the $b$ -function is positive in both models, the bond price is indeed decreasing in maturity.. Then the following result, first derived by Jamshidian (1989), applies:.  

Theorem 12.8 Suppose that the zero-coupon bond prices are of the form $B_{t}^{T}=B^{T}(r_{t},t)$ and $B^{T}$ is decreasing in. $r_{t}$ . Then the price of a European call on a coupon bond is.  
$$
C_{t}^{K,T,c p n}=\sum_{T_{i}>T}Y_{i}C_{t}^{K_{i},T,T_{i}},
$$  

where $K_{i}=B^{T_{i}}(r^{*},T)$ , and $r^{*}$ is defined as the solution to the equation  
$$
B(r^{*},T)\equiv\sum_{T_{i}>T}Y_{i}B^{T_{i}}(r^{*},T)=K.
$$  

Proof: The payoff of the option on the coupon bond is  
$$
\operatorname*{max}(B(r_{T},T)-K,0)=\operatorname*{max}\left(\sum_{T_{i}>T}Y_{i}B^{T_{i}}(r_{T},T)-K,0\right).
$$  

Since the zero-coupon bond price $B^{T_{i}}(r_{T},T)$ is a monotonically decreasing function of the interest rate $r_{T}$ , the whole sum $\begin{array}{r}{\sum_{T_{i}>T}Y_{i}B^{T_{i}}(r_{T},T)}\end{array}$ is monotonically decreasing in $r_{T}$ . Therefore, exactly one value $r^{*}$ of $r_{T}$ will make the option finish at the money so that (12.31) holds. Letting $K_{i}=$ $B^{T_{i}}(r^{*},T)$ , we have that $\begin{array}{r}{\sum_{T_{i}>T}Y_{i}K_{i}=K}\end{array}$  

For $r_{T}<r^{*}$  
$$
\sum_{T_{i}>T}Y_{i}B^{T_{i}}(r_{T},T)>\sum_{T_{i}>T}Y_{i}B^{T_{i}}(r^{*},T)=K,\quad B^{T_{i}}(r_{T},T)>B^{T_{i}}(r^{*},T)=K_{i},
$$  

so that  
$$
\begin{array}{r l r}{\lefteqn{\operatorname*{max}\left(\sum_{T_{i}>T}Y_{i}B^{T_{i}}(r_{T},T)-K,0\right)=\sum_{T_{i}>T}Y_{i}B^{T_{i}}(r_{T},T)-K}}\ &{}&{=\displaystyle\sum_{T_{i}>T}Y_{i}\left(B^{T_{i}}(r_{T},T)-K_{i}\right)}\ &{}&{=\displaystyle\sum_{T_{i}>T}Y_{i}\operatorname*{max}\left(B^{T_{i}}(r_{T},T)-K_{i},0\right).}\end{array}
$$  

For $r_{T}\geq r^{*}$  
$$
\sum_{T_{i}>T}Y_{i}B^{T_{i}}(r_{T},T)\le\sum_{T_{i}>T}Y_{i}B^{T_{i}}(r^{*},T)=K,\quad B^{T_{i}}(r_{T},T)\le B^{T_{i}}(r^{*},T)=K_{i},
$$  

so that  
$$
\operatorname*{max}\left(\sum_{T_{i}>T}Y_{i}B^{T_{i}}(r_{T},T)-K,0\right)=0=\sum_{T_{i}>T}Y_{i}\operatorname*{max}\left(B^{T_{i}}(r_{T},T)-K_{i},0\right).
$$  

Hence, for all possible values of $r_{T}$ we may conclude that  
$$
\operatorname*{max}\left(\sum_{T_{i}>T}Y_{i}B^{T_{i}}(r_{T},T)-K,0\right)=\sum_{T_{i}>T}Y_{i}\operatorname*{max}\left(B^{T_{i}}(r_{T},T)-K_{i},0\right).
$$  

The payoff of the option on the coupon bond is thus identical to the payoff of a [portfolio](../../../Advanced%20Investments/An%20Asset%20Allocation%20Primer.md) of options on zero-coupon bonds, namely a [portfolio](../../../Advanced%20Investments/An%20Asset%20Allocation%20Primer.md) consisting (for each $i$ with $T_{i}>T$ ) of $Y_{i}$ options on a. zero-coupon bond maturing at time $T_{i}$ and an [exercise price](.md) of. $K_{i}$ . Consequently, the value of. the option on the coupon bond at time $t\leq T$ equals the value of that [portfolio](../../../Advanced%20Investments/An%20Asset%20Allocation%20Primer.md) of options on zero-coupon bonds. A formal derivation goes as follows:  
$$
\begin{array}{r l}{{\displaystyle C_{t}^{K,T,\mathrm{cpn}}=\mathrm{E}_{r,t}^{\mathbb{Q}}\left[e^{-\int_{t}^{T}r_{u}d u}\operatorname*{max}\left(B(r_{T},T)-K,0\right)\right]}}&{{}}\ {{\displaystyle=\mathrm{E}_{r,t}^{\mathbb{Q}}\left[e^{-\int_{t}^{T}r_{u}d u}\sum_{T_{i}>T}Y_{i}\operatorname*{max}\left(B^{T_{i}}(r_{T},T)-K_{i},0\right)\right]}}&{{}}\ {{\displaystyle=\sum_{T_{i}>T}Y_{i}\mathrm{E}_{r,t}^{\mathbb{Q}}\left[e^{-\int_{t}^{T}r_{u}d u}\operatorname*{max}\left(B^{T_{i}}(r_{T},T)-K_{i},0\right)\right]}}&{{}}\ {{\displaystyle=\sum_{T_{i}>T}Y_{i}C_{t}^{K_{i},T,T_{i}}},}&{{}}\end{array}
$$  

which completes the proof.  

To compute the price of a European call option on a coupon bond we must numerically solve one equation in one unknown (to find. $r^{*}$ ) and calculate $n^{\prime}$ prices of European call options on. zero-coupon bonds, where. $n^{\prime}$ is the number of payment dates of the coupon bond after expiration. of the option. For example, in the [Vasicek model](../../../Fixed%20Income%20Asset%20Pricing/Fixed%20Income%20Lecture%20Notes/Vasicek%20Short%20Rate%20Model.md) we can use (12.29).  

Practitioners often use [Black-Scholes](../../../Financial%20Engineering/Mathematical%20Modeling%20of%20Derivative%20Pricing.md)-[Merton](../../../Credit%20Markets/Credit%20Markets%20Session%205.md) type formulas for pretty much all types of options, including options on bonds. The formulas are based on the Black (1976) variant of the BlackScholes-[Merton model](../../../Credit%20Markets/Credit%20Markets%20Session%205.md) developed for stock option [pricing](../../Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%207/Arbitrage%20Pricing%20of%20Derivatives.md), originally developed for options on [futures](../../Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%203%20-%20Futures%20Markets/Futures%20Not%20Subject%20to%20Cash-And-Carry.md) on an asset with a lognormally distributed value. Black's formula for a European call option on a bond is  
$$
\begin{array}{r l}&{C_{t}^{K,T,\mathrm{cpn}}=B_{t}^{T}\left[F_{t}^{T,\mathrm{cpn}}N\left(d(F_{t}^{T,\mathrm{cpn}},t)\right)-K N\left(d(F_{t}^{T,\mathrm{cpn}},t)-\sigma_{B}\sqrt{T-t}\right)\right],}\ &{\qquad=\tilde{B}_{t}N\left(d(F_{t}^{T,\mathrm{cpn}},t)\right)-K B_{t}^{T}N\left(d(F_{t}^{T,\mathrm{cpn}},t)-\sigma_{B}\sqrt{T-t}\right),}\end{array}
$$  

where $\sigma_{B}$ is the volatility of the bond, $F_{t}^{T,\mathrm{cpn}}=\tilde{B}_{t}/B_{t}^{T}$ is the [forward price](../../Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%2011/Forward%20Contracts%20and%20Forward%20Prices.md) of the bond, $\tilde{B}_{t}=$ $\begin{array}{r}{B_{t}-\sum_{t<T_{i}<T}Y_{i}B_{t}^{T_{i}}}\end{array}$ is the present value of the bond payments after maturity of the option, and  
$$
d(F_{t}^{T,\mathrm{cpn}},t)=\frac{\ln(F_{t}^{T,\mathrm{cpn}}/K)}{\sigma\sqrt{T-t}}+\frac{1}{2}\sigma_{B}\sqrt{T-t}.
$$  

The use of Black's formula for bond options is not theoretically supported and may lead to prices allowing [arbitrage](../../Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%207/Arbitrage%20Pricing%20of%20Derivatives.md). At best, it is a reasonable approximation to the correct price..  

# 12.3.5 Interest rate options: caps and floors  

An (interest rate) cap is designed to protect an investor who has borrowed funds on a floating interest rate basis against the risk of paying very high [interest rates](../../Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%202/Interest%20Rate%20Quotations.md). Suppose the loan has a face value of $H$ and payment dates. $T_{1}<T_{2}<\cdots<T_{n}$ , where $T_{i+1}-T_{i}=\delta$ for all $\imath$ 2 The interest rate to be paid at time $T_{i}$ is determined by the $\delta$ -period money market interest rate prevailing at. time $T_{i-1}=T_{i}-\delta$ , i.e. the payment at time. $T_{i}$ is equal to $H\delta l_{T_{i}-\delta}^{T_{i}^{\prime}}$ , cf. the notation for interest. rates introduced in Section 10.2. Note that the interest rate is set at the beginning of the period, but paid at the end. Define $T_{0}=T_{1}-\delta$ . The dates $T_{0},T_{1},\ldots,T_{n-1}$ where the rate for the coming period is determined are called the reset dates of the loan..  

A cap with a face value of. $H$ , payment dates $T_{i}$ $i=1,\ldots,n$ ) as above, and a so-called cap rate $K$ yields a time $T_{i}$ payoff of $H\delta\operatorname*{max}(l_{T_{i}-\delta}^{T_{i}}-K,0)$ , for $i=1,2,\dots,n$ . If a borrower buys such a cap, the net payment at time. $T_{i}$ cannot exceed $H\delta K$ . The period length. $\delta$ is often referred to as. the frequency or the tenor of the cap.3 In practice, the frequency is typically either 3, 6, or 12 months. Note that the time distance between payment dates coincides with the "maturity" of the foating interest rate. Also note that while a cap is tailored for interest rate [hedging](../../Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%205/Key%20Rates%20O1s%20Durations%20and%20Hedging.md), it can also be used for interest rate speculation.  

A cap can be seen as a [portfolio](../../../Advanced%20Investments/An%20Asset%20Allocation%20Primer.md) of. $n$ caplets, namely one for each payment date of the cap. The $i$ 'th caplet yields a payoff at time. $T_{i}$ of  
$$
\mathcal{C}_{T_{i}}^{i}=H\delta\operatorname*{max}\left(l_{T_{i}-\delta}^{T_{i}}-K,0\right)
$$  

and no other payments. A caplet is a call option on the zero-coupon yield prevailing at time $T_{i}-\delta$ for a period of length $\delta$ , but where the payment takes place at time $T_{i}$ although it is already fixed at time $T_{i}-\delta$  

In the following we will find the value of the $i$ 'th caplet before time. $T_{i}$ . Since the payoff becomes known at time. $T_{i}-\delta$ , we can obtain its value in the interval between $T_{i}-\delta$ and $T_{i}$ by a simple discounting of the payoff, i.e.  
$$
\begin{array}{r}{\mathcal{C}_{t}^{i}=B_{t}^{T_{i}}H\delta\operatorname*{max}\left(l_{T_{i}-\delta}^{T_{i}}-K,0\right),\quad T_{i}-\delta\leq t\leq T_{i}.}\end{array}
$$  

In particular,  
$$
\begin{array}{r}{\mathcal{C}_{T_{i}-\delta}^{i}=B_{T_{i}-\delta}^{T_{i}}H\delta\operatorname*{max}\left(l_{T_{i}-\delta}^{T_{i}}-K,0\right).}\end{array}
$$  

To find the value before the fixing of the payoff, i.e. for $t<T_{i}-\delta$ , we shall use two strategies. The first is simply to take relevant [expectations](../../../Fixed%20Income%20Asset%20Pricing/Fixed%20Income%20Lecture%20Notes/FORWARD%20RATES%20AND%20TERM%20STRUCTURE.md) of the payoff. Since the payoff comes at. $T_{i}$ , we know from Section 11.4 that the value of the payoff can be found as the product of the expected payoff computed under the $T_{i}$ -[forward martingale measure](.md) and the current [discount factor](../../Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%201/Discount%20Factors.md) for time. $T_{i}$ payments, i.e.  
$$
\mathcal{C}_{t}^{i}=H\delta B_{t}^{T_{i}}\mathrm{E}_{t}^{\mathbb{Q}^{T_{i}}}\left[\operatorname*{max}\left(l_{T_{i}-\delta}^{T_{i}}-K,0\right)\right],\quad t<T_{i}-\delta.
$$  

The price of a cap can therefore be determined as  
$$
\boldsymbol{\mathfrak{C}}_{t}=H\delta\sum_{i=1}^{n}B_{t}^{T_{i}}\mathrm{E}_{t}^{\mathbb{Q}^{T_{i}}}\left[\operatorname*{max}\left(l_{T_{i}-\delta}^{T_{i}}-K,0\right)\right],\quad t<T_{0}.
$$  

If each LIBOR rate $l_{T_{i}-\delta}^{T-i}$ is lognormally distributed under the $\mathbb{Q}^{T_{i}}$ -forward measure, we can obtain a nice closed-form [pricing](../../Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%207/Arbitrage%20Pricing%20of%20Derivatives.md) formula. This is satisfied in the so-called LIBOR market model introduced by Miltersen, Sandmann, and Sondermann (1997) and Brace, Gatarek, and Musiela (1997). See Munk (2005, Ch. 11) for a review. In fact, the resulting [pricing](../../Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%207/Arbitrage%20Pricing%20of%20Derivatives.md) formula is the Black formula often applied in practice:  
$$
\mathfrak{C}_{t}^{i}=H\delta B_{t}^{T_{i}}\left[L_{t}^{T_{i}-\delta,T_{i}}N\left(d^{i}(L_{t}^{T_{i}-\delta,T_{i}},t)\right)-K N\left(d^{i}(L_{t}^{T_{i}-\delta,T_{i}},t)-\sigma_{i}\sqrt{T_{i}-\delta-t}\right)\right],\quad t<T_{i}-\delta,
$$  

where $\sigma_{i}$ is the (relative) volatility of the forward LIBOR rate $L_{t}^{T_{i}-\delta,T_{i}}$ , and $d^{i}$ is given by  
$$
d^{i}(L_{t}^{T_{i}-\delta,T_{i}},t)=\frac{\ln(L_{t}^{T_{i}-\delta,T_{i}}/K)}{\sigma_{i}\sqrt{T_{i}-\delta-t}}+\frac{1}{2}\sigma_{i}\sqrt{T_{i}-\delta-t}.
$$  

The second [pricing](../../Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%207/Arbitrage%20Pricing%20of%20Derivatives.md) strategy links caps to bond options. Applying (10.5) on page 246, we can rewrite (12.34) as  
$$
\begin{array}{l}{{\displaystyle\mathcal{C}_{T_{i}-\delta}^{i}=B_{T_{i}-\delta}^{T_{i}}H\operatorname*{max}\left(1+\delta l_{T_{i}-\delta}^{T_{i}}-[1+\delta K],0\right)}}\ {{\displaystyle\qquad=B_{T_{i}-\delta}^{T_{i}}H\operatorname*{max}\left(\frac{1}{B_{T_{i}-\delta}^{T_{i}}}-[1+\delta K],0\right)}}\ {{\displaystyle\qquad=H(1+\delta K)\operatorname*{max}\left(\frac{1}{1+\delta K}-B_{T_{i}-\delta}^{T_{i}},0\right).}}\end{array}
$$  

We can now see that the value at time $T_{i}-\delta$ is identical to the payoff of a European put option expiring at time $T_{i}-\delta$ that has an [exercise price](.md) of $1/(1+\delta K)$ and is written on a zero-coupon bond maturing at time $T_{i}$ .Accordingly, the value of the $\imath$ th caplet at an earlier point in time $t\leq T_{i}-\delta$ must equal the value of that put option, i.e.  
$$
\begin{array}{r}{\mathcal{\ C}_{t}^{i}=H(1+\delta K)\pi_{t}^{(1+\delta K)^{-1},T_{i}-\delta,T_{i}}.}\end{array}
$$  

To find the value of the entire cap contract we simply have to add up the values of all the caplets corresponding to the remaining payment dates of the cap. Before the first reset date, $T_{0}$ , none of the cap payments are known, so the value of the cap is given by.  
$$
\displaystyle\mathcal{C}_{t}=\sum_{i=1}^{n}\mathcal{C}_{t}^{i}=H(1+\delta K)\sum_{i=1}^{n}\pi_{t}^{(1+\delta K)^{-1},T_{i}-\delta,T_{i}},\quad t<T_{0}.
$$  

At all dates after the first reset date, the next payment of the cap will already be known. If we use the notation. $T_{i(t)}$ for the nearest following payment date after time. $t$ , the value of the cap at. any time $t$ in $[T_{0},T_{n}]$ (exclusive of any payment received exactly at time $t$ ) can be written as.  
$$
\begin{array}{r l}&{\boldsymbol{\mathcal{C}}_{t}=H B_{t}^{T_{i(t)}}\delta\operatorname*{max}\left(\boldsymbol{l}_{T_{i(t)}-\delta}^{T_{i(t)}}-\boldsymbol{K},0\right)}\ &{\qquad+\left(1+\delta\boldsymbol{K}\right)H\displaystyle\sum_{i=i(t)+1}^{n}\pi_{t}^{(1+\delta\boldsymbol{K})^{-1},T_{i}-\delta,T_{i}},\quad T_{0}\le t\le T_{n}.}\end{array}
$$  

If $T_{n-1}<t<T_{n}$ , we have $i(t)=n$ , and there will be no terms in the sum, which is then considered to be equal to zero. In various models of interest rate dynamics, nice [pricing](../../Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%207/Arbitrage%20Pricing%20of%20Derivatives.md) formulas for European options on zero-coupon bonds can be derived. This is for example the case in the [Vasicek model](../../../Fixed%20Income%20Asset%20Pricing/Fixed%20Income%20Lecture%20Notes/Vasicek%20Short%20Rate%20Model.md) studied above. Cap prices will then follow from prices of European puts on zero-coupon bonds.  

Note that the [interest rates](../../Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%202/Interest%20Rate%20Quotations.md) and the discount factors appearing in the expressions above are taken. from the money market, not from the government bond market. Also note that since caps and most other contracts related to money market rates trade OTC, one should take the [default risk](../../Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%207%20-%20Default%20Risk%20and%20Credit%20Derivatives/Default%20Risk%20and%20Credit%20Derivatives%20183.md) of the two parties into account when valuing the cap. Here, default simply means that the party. cannot pay the amounts promised in the contract. Official money market rates and the associated [discount function](../Chapter%2010%20-%20The%20Economics%20of%20the%20Term%20Structure%20of%20Interest%20Rates/Basic%20Interest%20Rate%20Concepts%20and%20Relations.md) apply to loan and deposit arrangements between large [financial institutions](../../../Financial%20Markets%20and%20Institutions/Financial%20Markets%20and%20Institutions%20Lecture%20Notes.md), and. thus they reflect the [default risk](../../Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%207%20-%20Default%20Risk%20and%20Credit%20Derivatives/Default%20Risk%20and%20Credit%20Derivatives%20183.md) of these corporations. If the parties in an OTC transaction have a [default risk](../../Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%207%20-%20Default%20Risk%20and%20Credit%20Derivatives/Default%20Risk%20and%20Credit%20Derivatives%20183.md) significantly different from that, the discount rates in the formulas should be adjusted accordingly. However, it is quite complicated to do that in a theoretically correct manner, so we will not discuss this issue any further at this point..  

An (interest rate) floor is designed to protect an investor who has lent funds on a floating rate basis against receiving very [low interest rates](../../../Financial%20Markets%20and%20Institutions/III.%20Liquidity%20of%20Assets/Class%209-%20Bailouts%20and%20Bank%20Failures/Articles/The%20Economist%20Time%20Is%20Cheap.md). The contract is constructed just as a cap except. that the payoff at time $T_{i}$ $i=1,\ldots,n$ ) is given by  
$$
\mathcal{F}_{T_{i}}^{i}=H\delta\operatorname*{max}\left(K-l_{T_{i}-\delta}^{T_{i}},0\right),
$$  

where $K$ is called the floor rate. Buying an appropriate floor, an investor who has provided another investor with a floating rate loan will in total at least receive the floor rate. Of course, an investor can also speculate in low future [interest rates](../../Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%202/Interest%20Rate%20Quotations.md) by buying a floor. The (hypothetical) contracts that only yield one of the payments in (12.41) are called floorlets. Obviously, we can think of a floorlet as a European put on the floating interest rate with delayed payment of the payoff.  

Analogously to the analysis for caps, we can price the floor directly as  
$$
\mathcal{F}_{t}=H\delta\sum_{i=1}^{n}B_{t}^{T_{i}}\operatorname{E}_{t}^{\mathbb{Q}^{T_{i}}}\left[\operatorname*{max}\left(K-L_{T_{i}-\delta}^{T_{i}-\delta,T_{i}},0\right)\right],\quad t<T_{0}.
$$  

Again a [pricing](../../Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%207/Arbitrage%20Pricing%20of%20Derivatives.md) formula consistent with the Black formula is obtained assuming lognormally distributed forward LIBOR rates. Alternatively, we can express the floorlet as a European call on a zero-coupon bond, and hence a floor is equivalent to a [portfolio](../../../Advanced%20Investments/An%20Asset%20Allocation%20Primer.md) of European calls on zero-coupon bonds. More precisely, the value of the $i$ 'th floorlet at time $T_{i}-\delta$ is  
$$
\mathcal{F}_{T_{i}-\delta}^{i}=H(1+\delta K)\operatorname*{max}{\left(B_{T_{i}-\delta}^{T_{i}}-\frac{1}{1+\delta K},0\right)}.
$$  

The total value of the floor contract at any time $t<T_{0}$ is therefore given by.  
$$
\mathcal{F}_{t}=H(1+\delta K)\sum_{i=1}^{n}C_{t}^{(1+\delta K)^{-1},T_{i}-\delta,T_{i}},\quad t<T_{0},
$$  

and later the value is  
$$
\begin{array}{r l}&{\mathcal{F}_{t}=H B_{t}^{T_{i(t)}}\delta\operatorname*{max}\Big(K-l_{T_{i(t)}-\delta}^{T_{i(t)}},0\Big)}\ &{\qquad+(1+\delta K)H\underset{i=i(t)+1}{\overset{n}{\sum}}C_{t}^{(1+\delta K)^{-1},T_{i}-\delta,T_{i}},\quad T_{0}\leq t\leq T_{n}.}\end{array}
$$  
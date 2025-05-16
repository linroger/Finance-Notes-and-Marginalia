---
tags:
  - continuous_time
  - discrete_time
  - one_period_economy
  - risk_free_return
  - risk_neutral_probabilities
aliases:
  - Risk-Neutral Expectation
  - Risk-Neutral Measure
key_concepts:
  - Continuous-time economy
  - Discrete-time economy
  - One-period economy
  - Risk-free return
  - Risk-neutral probability measure
---

# 11.3 Risk-neutral probabilities  

# 11.3.1 Definition  

A [risk-neutral probability measure](Pricing%20Forwards,%20Futures,%20Bonds,%20Swaps,%20Swaptions,%20Caps%20and%20Floors%20under%20No-Arbitrage%20and%20Risk-Neutral%20Pricing.md) for a given financial market can only be defined if the investors at any point in time considered in the model and for any state can trade in an asset which provides a [risk-free return](../Chapter%204%20-%20State%20Prices/A%20Preview%20of%20Alternative%20Formulations.md) until the next point in time where the investors can rebalance their portfolios. In a [one-period economy](Exercises.md), this is simply a one-period [risk-free asset](../../../Financial%20Engineering/2.%20Forwards,%20Swaps,%20Futures,%20and%20Options.md). As before, $R^{f}$ denotes the gross return on that asset. In a [discrete-time economy](Exercises.md) with trading at. $t=0,1,2,\ldots,T-1$ , the assumptions is that investors can roll over in one-period risk-free investments. Investing one unit in a one-period risk-free [investment](../../../Advanced%20Investments/An%20Asset%20Allocation%20Primer.md) at time. $t$ will give you $R_{t}^{f}$ at time $t+1$ . Reinvesting that in a risk-fre manner over the next period will give you $R_{t,t+2}^{f}=R_{t}^{f}R_{t+1}^{f}$ at time $t+2$ . Continuing that procedure, you end up with.  
$$
R_{t,t+n}^{f}=R_{t}^{f}R_{t+1}^{f}R_{t+2}^{f}\cdot\cdot\cdot R_{t+n-1}^{f}=\prod_{m=0}^{n-1}R_{t+m}^{f}
$$  

at time $t+n$ . Note that, in general, this return is not known before time $t+n-1$ and in particular not at time. $t$ where the [investment](../../../Advanced%20Investments/An%20Asset%20Allocation%20Primer.md) strategy is initiated. An [investment](../../../Advanced%20Investments/An%20Asset%20Allocation%20Primer.md) with a truly [risk-free return](../Chapter%204%20-%20State%20Prices/A%20Preview%20of%20Alternative%20Formulations.md) between time $t$ and $t+n$ is a zero-coupon bond maturing at time $t+n$ . If $B_{t}^{t+n}$ denotes the price of this bond at time $t$ and the face value of the bond is normalized at 1, the gross [risk-free return](../Chapter%204%20-%20State%20Prices/A%20Preview%20of%20Alternative%20Formulations.md) between $t$ and $t+n$ is $1/B_{t}^{t+n}$  

In a [continuous-time economy](.md) we can think of the limit of the above roll-over strategy. If $\boldsymbol{r}_{t}^{f}$ denotes the continuously compounded risk-free [net rate of return](../Chapter%203%20-%20%20Assets,%20Portfolios,%20and%20Arbitrage/Assets.md) at time $t$ (the interest rate over the instant following time $t$ ), an [investment](../../../Advanced%20Investments/An%20Asset%20Allocation%20Primer.md) of $^{1}$ in this roll-over strategy at time $\mathrm{\Delta t}$ will give you  
$$
R_{t,t^{\prime}}^{f}=\exp\left\{\int_{t}^{t^{\prime}}r_{u}^{f}d u\right\}
$$  

at time $t^{\prime}$  

Whether the model is formulated in discrete or in continuous time we refer to the roll-over strategy in short risk-free investments as the bank account and refer to $R_{t,s}^{f}$ as the gross return on the bank account between time $t$ and time $s>t$ . In the [one-period model](Exercises.md), the bank account is simply a one-period [risk-free asset](../../../Financial%20Engineering/2.%20Forwards,%20Swaps,%20Futures,%20and%20Options.md).  

We can now give a unified definition of a [risk-neutral probability measure](Pricing%20Forwards,%20Futures,%20Bonds,%20Swaps,%20Swaptions,%20Caps%20and%20Floors%20under%20No-Arbitrage%20and%20Risk-Neutral%20Pricing.md). A probability measure $\mathbb{Q}$ is called a [risk-neutral probability measure](Pricing%20Forwards,%20Futures,%20Bonds,%20Swaps,%20Swaptions,%20Caps%20and%20Floors%20under%20No-Arbitrage%20and%20Risk-Neutral%20Pricing.md) for a given financial market in which a bank account is traded if the following conditions are satisfied:  

(i) $\mathbb{P}$ and $\mathbb{Q}$ are equivalent;   
(ii) the [Radon-Nikodym derivative](../Chapter%204%20-%20State%20Prices/A%20Preview%20of%20Alternative%20Formulations.md) $\textstyle{\frac{d\mathbb{Q}}{d\mathbb{P}}}$ has finite variance;   
(iii) the price of a future dividend equals the $\mathbb{Q}$ -expectation of the ratio of the dividend to the. gross return on the bank account between the [pricing](../../Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%207/Arbitrage%20Pricing%20of%20Derivatives.md) date and the dividend payment date.  

When $\mathbb{Q}$ is a [risk-neutral probability measure](Pricing%20Forwards,%20Futures,%20Bonds,%20Swaps,%20Swaptions,%20Caps%20and%20Floors%20under%20No-Arbitrage%20and%20Risk-Neutral%20Pricing.md), we will refer to the $\mathbb{Q}$ -expectation as the [risk-neutral expectation](.md).  

The [pricing](../../Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%207/Arbitrage%20Pricing%20of%20Derivatives.md) condition (ii) is a bit vague at this point. In a [one-period framework](../Chapter%204%20-%20State%20Prices/Properties%20of%20State-Price%20Deflators.md), it means that  
$$
\begin{array}{r}{{P}_{i}=\mathrm{E}^{\mathbb{Q}}\left[(R^{f})^{-1}D_{i}\right]=(R^{f})^{-1}\mathrm{E}^{\mathbb{Q}}\left[D_{i}\right],}\end{array}
$$  

and, consequently, $\operatorname{E}[R_{i}]=R^{f}$ . In a discrete-time model, the [pricing](../../Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%207/Arbitrage%20Pricing%20of%20Derivatives.md) condition (iii) is  
$$
P_{i t}=\mathrm{E}_{t}^{\mathbb{Q}}\left[\sum_{s=t+1}^{T}\frac{D_{i s}}{R_{t,s}^{f}}\right],
$$  

which is equivalent to  
$$
P_{i t}=\mathrm{E}_{t}^{\mathbb{Q}}\left[\frac{P_{i t^{\prime}}}{R_{t,t^{\prime}}^{f}}+\sum_{s=t+1}^{t^{\prime}}\frac{D_{i s}}{R_{t,s}^{f}}\right],\quad t<t^{\prime}\leq T,
$$  

cf. Exercise 11.1. In particular, for $t^{\prime}=t+1$ this reduces to.  
$$
P_{i t}=\frac{1}{R_{t}^{f}}\operatorname{E}_{t}^{\mathbb{Q}}\left[P_{i,t+1}+D_{i,t+1}\right]
$$  

so that $\mathrm{E}_{t}[R_{i,t+1}]=R_{t}^{f}$ . In the [continuous-time framework](Exercises.md), the [pricing](../../Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%207/Arbitrage%20Pricing%20of%20Derivatives.md) condition (ili) is interpreted as  
$$
\begin{array}{r l}&{P_{i t}=\mathrm{E}_{t}^{\mathbb{Q}}\left[\int_{t}^{T}(R_{t,s}^{f})^{-1}\delta_{i s}P_{i s}d s+(R_{t,T}^{f})^{-1}D_{i T}\right]}\ &{\quad=\mathrm{E}_{t}^{\mathbb{Q}}\left[(R_{t,T}^{f})^{-1}e^{\int_{t}^{T}\delta_{i s}d s}D_{i T}\right]=\mathrm{E}_{t}^{\mathbb{Q}}\left[e^{-\int_{t}^{T}(r_{s}^{f}-\delta_{i s})d s}D_{i T}\right],}\end{array}
$$  

from which the relation  
$$
P_{i t}=\mathrm{E}_{t}^{\mathrm{Q}}\left[\int_{t}^{t^{\prime}}(R_{t,s}^{f})^{-1}\delta_{i s}P_{i s}d s+(R_{t,t^{\prime}}^{f})^{-1}P_{i,t^{\prime}}\right]=\mathrm{E}_{t}^{\mathrm{Q}}\left[e^{-\int_{t}^{t^{\prime}}(r_{s}^{f}-\delta_{i s})d s}P_{i,t^{\prime}}\right]
$$  

follows. This implies that  
$$
d P_{i t}=P_{i t}\left[\left(r_{t}^{f}-\delta_{i t}\right)d t+\pm\sigma_{i t}^{\top}d z_{t}^{\mathbb{Q}}\right]
$$  

so that the total instantaneous rate of return has a [risk-neutral expectation](.md) equal to the [risk-free rate](../../../Financial%20Instruments/Black%20Scholes%20Derivation.md). Therefore, in all of the modeling frameworks, the risk-neutral [expected return](../../../Advanced%20Investments/Lecture%201-%20Probability%20Distributions%20of%20Returns.md) on any asset. over the next period equals the [risk-free return](../Chapter%204%20-%20State%20Prices/A%20Preview%20of%20Alternative%20Formulations.md) over that period. The above considerations also hold for all [trading strategies](../../../Course%20Notes/Quantitative%20Trading%20Strategies%20Lecture%20Notes.md) (as always, in the [continuous-time framework](Exercises.md) some "wild' trading. strategies must be ruled out).  

We can see from the above equations that given the [stochastic process](../../../The%20Ornstein-Uhlenbeck%20(OU)%20Process.md) for the [risk-free return](../Chapter%204%20-%20State%20Prices/A%20Preview%20of%20Alternative%20Formulations.md) and a [risk-neutral probability measure](Pricing%20Forwards,%20Futures,%20Bonds,%20Swaps,%20Swaptions,%20Caps%20and%20Floors%20under%20No-Arbitrage%20and%20Risk-Neutral%20Pricing.md), we can price any dividend process. Therefore the riskfree return process and a [risk-neutral probability measure](Pricing%20Forwards,%20Futures,%20Bonds,%20Swaps,%20Swaptions,%20Caps%20and%20Floors%20under%20No-Arbitrage%20and%20Risk-Neutral%20Pricing.md) jointly capture the market-wide [pricing](../../Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%207/Arbitrage%20Pricing%20of%20Derivatives.md) mechanism of the financial market.  

A [risk-neutral probability measure](Pricing%20Forwards,%20Futures,%20Bonds,%20Swaps,%20Swaptions,%20Caps%20and%20Floors%20under%20No-Arbitrage%20and%20Risk-Neutral%20Pricing.md) is sometimes called an equivalent martingale measure. Of course, the word equivalent refers to the equivalence of the [risk-neutral probability measure](Pricing%20Forwards,%20Futures,%20Bonds,%20Swaps,%20Swaptions,%20Caps%20and%20Floors%20under%20No-Arbitrage%20and%20Risk-Neutral%20Pricing.md) and the real-world probability measure. The word martingale is used here since the risk-free discounted gains process of any asset will be a. $\mathbb{Q}$ -martingale. The risk-free discounted gains process of asset. $i$ is denoted by $G_{i}=(G_{i t})_{t\in\mathcal{T}}$ . In the discrete-time setting, it is defined as.  
$$
\bar{G}_{i t}=\frac{P_{i t}}{R_{0,t}^{f}}+\sum_{s=1}^{t}\frac{D_{i s}}{R_{0,s}^{f}}
$$  

Since $R_{0,s}^{f}=R_{0,t}^{f}R_{t,s}^{f}$ for all $t<s$ , the [pricing](../../Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%207/Arbitrage%20Pricing%20of%20Derivatives.md) condition (11.9) can be rewritten as  
$$
\frac{P_{i t}}{R_{0,t}^{f}}=\mathrm{E}_{t}^{\mathbb{Q}}\left[\frac{P_{i t^{\prime}}}{R_{0,t^{\prime}}^{f}}+\sum_{s=t+1}^{t^{\prime}}\frac{D_{i s}}{R_{0,s}^{f}}\right],\quad t<t^{\prime}\leq T,
$$  

which is equivalent to  
$$
\frac{P_{i t}}{R_{0,t}^{f}}+\sum_{s=1}^{t}\frac{D_{i s}}{R_{0,s}^{f}}=\mathrm{E}_{t}^{\mathbb{Q}}\left[\frac{P_{i t^{\prime}}}{R_{0,t^{\prime}}^{f}}+\sum_{s=1}^{t^{\prime}}\frac{D_{i s}}{R_{0,s}^{f}}\right],\quad t<t^{\prime}\le T,
$$  

i.e. $\bar{G}_{i t}=\mathrm{E}_{t}^{\mathbb{Q}}[\bar{G}_{i,t^{\prime}}]$ so that ${\bar{G}}_{i}$ indeed is a $\mathbb{Q}$ martingale. In the [continuous-time setting](../Chapter%206%20-%20Individual%20optimality/The%20Continuous-Time%20Framework.md), the discounted gains process of asset. $i$ is defined as.  
$$
\bar{G}_{i t}=\frac{P_{i t}}{R_{0,t}^{f}}+\int_{0}^{t}\frac{\delta_{i s}P_{i s}}{R_{0,s}^{f}}d s,
$$  

and again it can be shown that the [pricing](../../Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%207/Arbitrage%20Pricing%20of%20Derivatives.md) condition (11.12) is equivalent to $G_{i}$ being a $\mathbb{Q}$ martingale.  

# 11.3.2 Relation to state-price deflators  

Since we can represent the general [pricing](../../Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%207/Arbitrage%20Pricing%20of%20Derivatives.md) mechanism of a financial market either by a [state-price deflator](Exercises.md) or by a [risk-neutral probability measure](Pricing%20Forwards,%20Futures,%20Bonds,%20Swaps,%20Swaptions,%20Caps%20and%20Floors%20under%20No-Arbitrage%20and%20Risk-Neutral%20Pricing.md) and the [risk-free return](../Chapter%204%20-%20State%20Prices/A%20Preview%20of%20Alternative%20Formulations.md) process, it should come as no surprise that there is a close relation between these quantities..  

First, consider a [one-period economy](Exercises.md) with a [risk-free asset](../../../Financial%20Engineering/2.%20Forwards,%20Swaps,%20Futures,%20and%20Options.md). Given a [state-price deflator](Exercises.md) $\zeta$ , the [risk-free rate](../../../Financial%20Instruments/Black%20Scholes%20Derivation.md) is $R^{f}=1/\operatorname{E}[\zeta]$ and we can define the random variable  
$$
\frac{d\mathbb{Q}}{d\mathbb{P}}=R^{f}\zeta,
$$  

which is a strictly positive random variable with  
$$
\operatorname{E}\left[{\frac{d\mathbb{Q}}{d\mathbb{P}}}\right]=R^{f}\operatorname{E}[\zeta]=1.
$$  

Therefore, $\textstyle{\frac{d\mathbb{Q}}{d\mathbb{P}}}$ defines a probability measure $\mathbb{Q}$ , which is equivalent to $\mathbb{P}$ . Since a [state-price deflator](Exercises.md) has finite variance and $R^{f}$ is a constant, $\textstyle{\frac{d\mathbb{Q}}{d\mathbb{P}}}$ has finite variance. Furthermore, from (11.1) we get  
$$
\operatorname{E}^{\mathbb{Q}}\left[{\frac{D_{i}}{R^{f}}}\right]=\operatorname{E}\left[{\frac{d\mathbb{Q}}{d\mathbb{P}}}{\frac{D_{i}}{R^{f}}}\right]=\operatorname{E}[\zeta D_{i}]=P_{i}.
$$  

Hence $\mathbb{Q}$ is indeed a [risk-neutral probability measure](Pricing%20Forwards,%20Futures,%20Bonds,%20Swaps,%20Swaptions,%20Caps%20and%20Floors%20under%20No-Arbitrage%20and%20Risk-Neutral%20Pricing.md). Conversely, if $\mathbb{Q}$ is a [risk-neutral probability measure](Pricing%20Forwards,%20Futures,%20Bonds,%20Swaps,%20Swaptions,%20Caps%20and%20Floors%20under%20No-Arbitrage%20and%20Risk-Neutral%20Pricing.md), a [state-price deflator](Exercises.md) can be defined by  
$$
\zeta=(R^{f})^{-1}\frac{d\mathbb{Q}}{d\mathbb{P}}.
$$  

Changing the probability measure is a reallocation of probability mass over the states. We can see that the [risk-neutral measure](../../../Financial%20Engineering/Verifying%20Martingale%20Property%20with%20Q.md) allocates a higher probability to states. $\omega$ for which $\zeta_{\omega}>(R^{f})^{-1}=$ $\operatorname{E}[\zeta]$ , i.e. if the value of the [state-price deflator](Exercises.md) for state. $\omega$ is higher than average..  

Example 11.1 Consider the same [one-period economy](Exercises.md) as in the Examples 3.1 and 4.2. The realworld probabilities of the three states are. $p_{1}=0.5$ $p_{2}=p_{3}=0.25$ , respectively. The [state-price deflator](Exercises.md) is given by. $\zeta_{1}=0.6$ $\zeta_{2}=0.8$ , and $\zeta_{3}=1.2$ . Since  
$$
\operatorname{E}[\zeta]=0.5\cdot0.6+0.25\cdot0.8+0.25\cdot1.2=0.8,
$$  

the gross [risk-free return](../Chapter%204%20-%20State%20Prices/A%20Preview%20of%20Alternative%20Formulations.md) is $R^{f}=1/\operatorname{E}[\zeta]=1.25$ corresponding to a $25\%$ risk-free [net rate of return](../Chapter%203%20-%20%20Assets,%20Portfolios,%20and%20Arbitrage/Assets.md). It follows that the [risk-neutral probabilities](../../../Financial%20Instruments/Financial%20Instruments.md) are  
$$
\begin{array}{r}{75,\quad q_{2}=R^{f}\zeta_{2}p_{2}=0.25,\quad q_{3}=R^{f}\zeta_{3}p_{3}=0.375}\end{array}
$$  

The [risk-neutral measure](../../../Financial%20Engineering/Verifying%20Martingale%20Property%20with%20Q.md) allocates a larger probability to state 3, the same probability to state 2, and a lower probability to state 1 than the real-world measure..  

In a [multi-period model](../Chapter%202%20-%20Uncertainty,%20Information,%20and%20Stochastic%20Processes/Information.md) where all uncertainty is resolved at time $T$ , the relation linking the. [state-price deflator](Exercises.md) $\zeta=(\zeta_{t})_{t\in\mathcal{T}}$ and the [risk-neutral probability measure](Pricing%20Forwards,%20Futures,%20Bonds,%20Swaps,%20Swaptions,%20Caps%20and%20Floors%20under%20No-Arbitrage%20and%20Risk-Neutral%20Pricing.md) is.  
$$
\zeta_{t}=\frac{1}{R_{0,t}^{f}}\operatorname{E}_{t}\left[\frac{d\mathbb{Q}}{d\mathbb{P}}\right]=\frac{\xi_{t}}{R_{0,t}^{f}},
$$  

where $\begin{array}{r}{\xi_{t}=\mathrm{E}_{t}^{\mathbb{P}}[\frac{d\mathbb{Q}}{d\mathbb{P}}]}\end{array}$ as before. Given a [risk-neutral probability measure](Pricing%20Forwards,%20Futures,%20Bonds,%20Swaps,%20Swaptions,%20Caps%20and%20Floors%20under%20No-Arbitrage%20and%20Risk-Neutral%20Pricing.md) $\mathbb{Q}$ and the risk-fee return process $(R_{0,t}^{f})_{t\in\mathcal{T}}$ , this equation defines the [state-price deflator](Exercises.md). Conversely, given a [state-price deflator](Exercises.md) $\zeta$ , the [risk-free return](../Chapter%204%20-%20State%20Prices/A%20Preview%20of%20Alternative%20Formulations.md) process is  
$$
R_{0,t}^{f}=R_{0}^{f}R_{1}^{f}\cdot\cdot\cdot R_{t-1}^{f}=\left(\operatorname{E}\left[\frac{\zeta_{1}}{\zeta_{0}}\right]\operatorname{E}_{1}\left[\frac{\zeta_{2}}{\zeta_{1}}\right]\ldots\operatorname{E}_{t}\left[\frac{\zeta_{t}}{\zeta_{t-1}}\right]\right)^{-1}
$$  

and  
$$
\frac{d\mathbb{Q}}{d\mathbb{P}}=R_{0,T}^{f}\zeta_{T}
$$  

defines a [risk-neutral probability measure](Pricing%20Forwards,%20Futures,%20Bonds,%20Swaps,%20Swaptions,%20Caps%20and%20Floors%20under%20No-Arbitrage%20and%20Risk-Neutral%20Pricing.md) $\mathbb{Q}$  

Let us consider a [discrete-time framework](../Chapter%204%20-%20State%20Prices/Multi-Period%20Valuation%20Models.md) and verify that the [pricing](../../Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%207/Arbitrage%20Pricing%20of%20Derivatives.md) condition (11.9) in the definition of a [risk-neutral probability measure](Pricing%20Forwards,%20Futures,%20Bonds,%20Swaps,%20Swaptions,%20Caps%20and%20Floors%20under%20No-Arbitrage%20and%20Risk-Neutral%20Pricing.md) is satisfied when $\zeta$ is a [state-price deflator](Exercises.md) and $\mathbb{Q}$ is defined through the [Radon-Nikodym derivative](../Chapter%204%20-%20State%20Prices/A%20Preview%20of%20Alternative%20Formulations.md) (11.15). First note that when $\zeta$ is a [state-price deflator](Exercises.md),  
$$
1=\mathrm{E}_{t}\left[\frac{\zeta_{T}}{\zeta_{t}}R_{t,T}^{f}\right]
$$  

and hence  
$$
\xi_{t}=\operatorname{E}_{t}\left[{\frac{d\mathbb{Q}}{d\mathbb{P}}}\right]=\operatorname{E}_{t}\left[\zeta_{T}R_{0,T}^{f}\right]=\zeta_{t}R_{0,t}^{f}\operatorname{E}_{t}\left[{\frac{\zeta_{T}}{\zeta_{t}}}R_{t,T}^{f}\right]=\zeta_{t}R_{0,t}^{f},
$$  

so that  
$$
\xi_{t}=\zeta_{t}R_{0,t}^{f},\quad t=0,1,\ldots,T,
$$  

and, thus,  
$$
\frac{\xi_{s}}{\xi_{t}}=\frac{\zeta_{s}}{\zeta_{t}}R_{t,s}^{f},\quad t<s\leq T.
$$  

We now have that  
$$
\begin{array}{r l}{\mathbb{E}_{t}^{\mathrm{Q}}\left[\frac{P_{t^{\prime}}}{R_{t^{\prime}}^{\prime}}+\displaystyle\sum_{s=t+1}^{t^{\prime}}\frac{D_{i s}}{R_{t,s}^{\prime}}\right]=\mathbb{E}_{t}^{\mathrm{Q}}\left[\frac{P_{t^{\prime}}}{R_{t^{\prime}}^{\prime}}\right]+\displaystyle\sum_{s=t+1}^{t^{\prime}}\mathbb{E}_{t}^{\mathrm{Q}}\left[\frac{D_{i s}}{R_{t,s}^{\prime}}\right]}&{}\ {=\mathbb{E}_{t}\left[\frac{\xi_{t^{\prime}}}{\xi_{t}}\frac{P_{t^{\prime}}}{R_{t,s}^{\prime}}\right]+\displaystyle\sum_{s=t+1}^{t^{\prime}}\mathbb{E}_{t}\left[\frac{\xi_{s}}{\xi_{t}}\frac{D_{i s}}{R_{t,s}^{\prime}}\right]}&{}\ {=\mathbb{E}_{t}\left[\frac{\xi_{t^{\prime}}}{\xi_{t}}\frac{P_{t^{\prime}}}{R_{t,t^{\prime}}^{\prime}}+\displaystyle\sum_{s=t+1}^{t^{\prime}}\frac{\xi_{s}}{\xi_{t}}\frac{D_{i s}}{R_{t,s}^{\prime}}\right]}&{}\ {=\mathbb{E}_{t}\left[\frac{\xi_{t^{\prime}}}{\xi_{t}}\frac{P_{t^{\prime}}}{R_{t^{\prime}}^{\prime}}+\displaystyle\sum_{s=t+1}^{t^{\prime}}\frac{\xi_{s}}{\xi_{t}}\frac{D_{i s}}{R_{t,s}^{\prime}}\right]}&{}\ {=\mathbb{E}_{t}\left[\frac{\xi_{t^{\prime}}}{\xi_{t}}P_{t^{\prime}}+\displaystyle\sum_{s=t+1}^{t^{\prime}}\frac{\xi_{s}}{\xi_{t}}D_{i s}\right]}&{}\ {=P_{t},}\end{array}
$$  

as was to be shown. Here the second equality is due to the relation (11.2), the fourth equality comes from inserting (11.16), and the final equality holds since $\zeta$ is a [state-price deflator](Exercises.md). Taking the above steps in the reverse order will show that if the [pricing](../../Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%207/Arbitrage%20Pricing%20of%20Derivatives.md) condition in the definition of a [risk-neutral probability measure](Pricing%20Forwards,%20Futures,%20Bonds,%20Swaps,%20Swaptions,%20Caps%20and%20Floors%20under%20No-Arbitrage%20and%20Risk-Neutral%20Pricing.md) is satisfied, then the [pricing](../../Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%207/Arbitrage%20Pricing%20of%20Derivatives.md) condition in the definition of a [state-price deflator](Exercises.md) is satisfied when $\zeta$ is defined as in (11.14). An analogous procedure works in the [continuous-time setting](../Chapter%206%20-%20Individual%20optimality/The%20Continuous-Time%20Framework.md).  

Combining the relation between risk-neutral measures and state-price deflators with the results on the existence and uniqueness of state-price defators derived in Section 4.3, we can make the following conclusions:  

Theorem 11.2 Assume that a bank account is traded. Prices admit no [arbitrage](../../Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%207/Arbitrage%20Pricing%20of%20Derivatives.md) if and only if a [risk-neutral probability measure](Pricing%20Forwards,%20Futures,%20Bonds,%20Swaps,%20Swaptions,%20Caps%20and%20Floors%20under%20No-Arbitrage%20and%20Risk-Neutral%20Pricing.md) exists. An [arbitrage-free market](Exercises.md) is complete if and only if there is a unique [risk-neutral probability measure](Pricing%20Forwards,%20Futures,%20Bonds,%20Swaps,%20Swaptions,%20Caps%20and%20Floors%20under%20No-Arbitrage%20and%20Risk-Neutral%20Pricing.md).  

In the [continuous-time framework](Exercises.md) some technical conditions have to be added or the definition of [arbitrage](../../Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%207/Arbitrage%20Pricing%20of%20Derivatives.md) must be slightly adjusted. In that framework, we know from Chapter 4 that a [state-price deflator](Exercises.md) is of the form  
$$
\zeta_{t}=\exp\left\{-\int_{0}^{t}r_{s}^{f}d s-\frac12\int_{0}^{t}\|\lambda_{s}\|^{2}d s-\int_{0}^{t}\lambda_{s}^{\top}d z_{s}\right\},
$$  

where $\lambda=\left(\lambda_{t}\right)$ is a [market price of risk](Exercises.md) process so that  
$$
\mu_{t}+\delta_{t}-r_{t}^{f}{\bf1}=\underline{{\underline{{\sigma}}}}{}_{t}\lambda_{t}.
$$  

The corresponding [risk-neutral probability measure](Pricing%20Forwards,%20Futures,%20Bonds,%20Swaps,%20Swaptions,%20Caps%20and%20Floors%20under%20No-Arbitrage%20and%20Risk-Neutral%20Pricing.md) is defined by  
$$
{\frac{d\mathbb{Q}}{d\mathbb{P}}}=R_{0,T}^{f}\zeta_{T}=e^{\int_{0}^{T}r_{s}^{f}d s}\zeta_{T}=\exp\left\{-{\frac{1}{2}}\int_{0}^{T}\|\lambda_{s}\|^{2}d s-\int_{0}^{T}(\lambda_{s})^{\top}d z_{s}\right\}
$$  

and  
$$
\xi_{t}=\operatorname{E}_{t}\left[{\frac{d{\mathbb{Q}}}{d{\mathbb{P}}}}\right]=\exp\left\{-{\frac{1}{2}}\int_{0}^{t}\|\mathbf{\lambda}_{s}\|^{2}d s-\int_{0}^{t}(\mathbf{\lambda}_{s})^{\top}d z_{s}\right\}.
$$  

It follows by the Girsanov Theorem 11.1 that the process $z^{\mathbb{Q}}=(z^{\mathbb{Q}})_{t\in[0,T]}$ defined by $z_{0}^{\mathbb{Q}}=\mathbf{0}$ and  
$$
d z_{t}^{\mathbb{Q}}=d z_{t}+\lambda_{t}d t
$$  

is a standard [Brownian motion](../Chapter%202%20-%20Uncertainty,%20Information,%20and%20Stochastic%20Processes/Continuous-Time%20Stochastic%20Processes.md) under the [risk-neutral probability measure](Pricing%20Forwards,%20Futures,%20Bonds,%20Swaps,%20Swaptions,%20Caps%20and%20Floors%20under%20No-Arbitrage%20and%20Risk-Neutral%20Pricing.md). We can then transform the dynamics of any process $X=(X_{t})_{t\in[0,T]}$ as follows:  
$$
{\begin{array}{r l}&{d X_{t}=\mu_{X t}d t+\sigma_{X t}^{\top}d z_{t}}\ &{\qquad=\mu_{X t}d t+\sigma_{X t}^{\top}\left(d z_{t}^{\mathbb{Q}}-\lambda_{t}d t\right)}\ &{\qquad=\left(\mu_{X t}-\sigma_{X t}^{\top}\lambda_{t}\right)d t+\sigma_{X t}^{\top}d z_{t}^{\mathbb{Q}}.}\end{array}}
$$  

The instantaneous sensitivity is unchanged, but the product of the sensitivity vector and the [market price of risk](Exercises.md) is subtracted from the drift. In particular, for a price process we get  
$$
\begin{array}{r l}&{d P_{i t}=P_{i t}\left[\mu_{i t}d t+\pmb{\sigma}_{i t}^{\top}d z_{t}\right]}\ &{\quad\quad=P_{i t}\left[\left(\mu_{i t}-\pmb{\sigma}_{i t}^{\top}\pmb{\lambda}_{t}\right)d t+\pmb{\sigma}_{i t}^{\top}d z_{t}^{\mathbb{Q}}\right]}\ &{\quad\quad=P_{i t}\left[\left(r_{t}^{f}-\delta_{i t}\right)d t+\pmb{\sigma}_{i t}^{\top}d z_{t}^{\mathbb{Q}}\right],}\end{array}
$$  

where the last equality follows from the definition of a [market price of risk](Exercises.md). Again we see that the [risk-neutral expectation](.md) of the total instantaneous rate of return is identical to the risk-free. interest rate.  

# 11.3.3 Valuation with risk-neutral probabilities  

From the [pricing](../../Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%207/Arbitrage%20Pricing%20of%20Derivatives.md) condition in the definition of a [risk-neutral probability measure](Pricing%20Forwards,%20Futures,%20Bonds,%20Swaps,%20Swaptions,%20Caps%20and%20Floors%20under%20No-Arbitrage%20and%20Risk-Neutral%20Pricing.md), it is clear that the valuation of an asset requires knowledge of the joint risk-neutral probability distribution of the risk-free [discount factor](../../Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%201/Discount%20Factors.md) $(R_{t,s}^{f})^{-1}$ and the asset dividend $D_{i,s}$ . More precisely, we have to know the. covariance under the [risk-neutral probability measure](Pricing%20Forwards,%20Futures,%20Bonds,%20Swaps,%20Swaptions,%20Caps%20and%20Floors%20under%20No-Arbitrage%20and%20Risk-Neutral%20Pricing.md) of the two variables. For example, in the discrete-time setting, (11.8) implies that  
$$
P_{i t}=\sum_{s=t+1}^{T}\left(\mathrm{E}_{t}^{\mathbb{Q}}\left[\left(R_{t,s}^{f}\right)^{-1}\right]\mathrm{E}_{t}^{\mathbb{Q}}\left[D_{i s}\right]+\mathrm{Cov}_{t}^{\mathbb{Q}}\left[\left(R_{t,s}^{f}\right)^{-1},D_{i s}\right]\right).
$$  

Note that $\begin{array}{r}{\mathrm{E}_{t}^{\mathbb{Q}}\left[\left(R_{t,s}^{f}\right)^{-1}\right]=B_{t}^{s}}\end{array}$ , the time $t$ price of a zero-coupon bond maturing with a unit payment at time $s$ . Therefore, we can rewrite the above equation as.  
$$
P_{i t}=\sum_{s=t+1}^{T}B_{t}^{s}\left(\mathrm{E}_{t}^{\mathbb{Q}}\left[D_{i s}\right]+\frac{\mathrm{Cov}_{t}^{\mathbb{Q}}\left[\left(R_{t,s}^{f}\right)^{-1},D_{i s}\right]}{B_{t}^{s}}\right).
$$  

Example 11.2 Consider the two-period economy illustrated in Figures 2.1 and 2.2 and also studied in Exercise 4.8. There are six states. The real-world state probabilities and the assumed values of the [state-price deflator](Exercises.md) at time 1 and time 2 are listed in left-most columns of Table 11.1. Figure 11.1 illustrates the economy as a two-period tree. Each state corresponds to a path through the tree. Two numbers are written along each branch. The left-most number is the value of the. next-period deflator along that branch ( $\zeta_{1}$ over the first period and $\zeta_{2}/\zeta_{1}$ over the second period).  

Table 11.1: P, $\mathbb{Q}$ $R^{f}$ , and $\zeta$ in Example 11.2.   


<html><body><table><tr><td>W</td><td>p</td><td>S1</td><td>S2/S1</td><td>S2</td><td>Rf</td><td>Ro.2</td><td>dQ dIP</td><td>q</td></tr><tr><td>1</td><td>0.24</td><td>1.2</td><td>1</td><td>1.2</td><td>1.0714</td><td>1.1398</td><td>1.3678</td><td>0.3283</td></tr><tr><td>2</td><td>0.06</td><td>1.2</td><td>0.6667</td><td>0.8</td><td>1.0714</td><td>1.1398</td><td>0.9119</td><td>0.0547</td></tr><tr><td>3</td><td>0.04</td><td>1</td><td>1</td><td>1</td><td>1.0989</td><td>1.1690</td><td>1.1690</td><td>0.0468</td></tr><tr><td>4</td><td>0.16</td><td>1</td><td>0.9</td><td>0.9</td><td>1.0989</td><td>1.1690</td><td>1.0521</td><td>0.1683</td></tr><tr><td>5</td><td>0.2</td><td>1</td><td>0.9</td><td>0.9</td><td>1.0989</td><td>1.1690</td><td>1.0521</td><td>0.2104</td></tr><tr><td>6</td><td>0.3</td><td>0.6</td><td>0.9</td><td>0.54</td><td>1.1111</td><td>1.1820</td><td>0.6383</td><td>0.1915</td></tr></table></body></html>  

The right-most number is the conditional real-world probability of that branch. The [conditional probabilities](../../Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%207%20-%20Default%20Risk%20and%20Credit%20Derivatives/A%20Deterministic%20Credit%20Migration%20Model.md) can be computed from the state probabilities, e.g. the conditional probability for the upward branch leaving the upper node at time 1 is the probability that state 1 is realized given that it is known that the true state is either 1 or 2, i.e. $0.24/(0.24+0.06)=0.8$  

Before the [risk-neutral probabilities](../../../Financial%20Instruments/Financial%20Instruments.md) can be computed, we have to find the gross return $R_{0,2}^{f}=$ $R_{0}^{f}R_{1}^{f}$ on the bank account. We can identify this from the [state-price deflator](Exercises.md) and the [real-world probabilities](Change%20of%20Probability%20Measure.md). Over the first period the [risk-free gross return](../Chapter%208%20-%20Consumption-Based%20Asset%20Pricing/General%20Multi-Period%20Link%20Between%20Consumption%20a.md) is.  
$$
R_{0}^{f}={\frac{1}{\operatorname{E}[\zeta_{1}]}}={\frac{1}{0.3\cdot1.2+0.4\cdot1+0.3\cdot0.6}}={\frac{1}{0.94}}\approx1.0638.
$$  

Over the second period the [risk-free gross return](../Chapter%208%20-%20Consumption-Based%20Asset%20Pricing/General%20Multi-Period%20Link%20Between%20Consumption%20a.md) depends on the information at time $^{1}$ .In the upper node at time 1 the one-period gross [risk-free return](../Chapter%204%20-%20State%20Prices/A%20Preview%20of%20Alternative%20Formulations.md) is.  
$$
R_{1}^{f}={\frac{1}{\mathrm{E}_{1}[\zeta_{2}/\zeta_{1}]}}={\frac{1}{0.8\cdot1+0.2\cdot0.6667}}={\frac{1}{0.9333}}\approx1.0714.
$$  

Similarly, $R_{1}^{f}\approx1.0989$ in the middle node and $R_{1}^{f}\approx1.1111$ in the lower node at time 1. Now the.   
[risk-neutral probabilities](../../../Financial%20Instruments/Financial%20Instruments.md) can be computed as shown in the right-most part of Table 11.1.  

Given the [risk-neutral probabilities](../../../Financial%20Instruments/Financial%20Instruments.md) of each state, we can compute the conditional risk-neutral. probabilities of transitions from one point in time to the next, exactly as for the real-world prob-. abilities. Together with the one-period risk-free [returns](../Chapter%203%20-%20%20Assets,%20Portfolios,%20and%20Arbitrage/Assets.md), the conditional [risk-neutral probabilities](../../../Financial%20Instruments/Financial%20Instruments.md) contain all the necessary information to price a given dividend process by backwards recursions through the tree. This information is illustrated in Figure 11.2. The conditional [risk-neutral probabilities](../../../Financial%20Instruments/Financial%20Instruments.md) can also be computed directly from the conditional [real-world probabilities](Change%20of%20Probability%20Measure.md) and the [risk-free return](../Chapter%204%20-%20State%20Prices/A%20Preview%20of%20Alternative%20Formulations.md) and the state-price defator for that transition. For example, the conditional risk-neutral probability of the upper branch leaving the upper node at time 1 equals. $1.0714\cdot1\cdot0.8\approx0.8571$  

Let us compute the price process of an asset with the dividends written in the circles in Figure 11.3 (this is asset 2 from Exercise 4.8). The ex-dividend price in the upper node at time. $^{1}$ is simply  
$$
P_{1}^{u}=\frac{1}{1.0714}\left(0.8571\cdot2+0.1429\cdot1\right)\approx1.7333.
$$  

Similarly, the time 1 prices in the middle and lower node are $P_{1}^{r n}=2.27$ and $P_{1}^{l}=2.7$ , respectively. The time 0 price is then computed as  
$$
P_{0}={\frac{1}{1.0638}}\left(0.3830\cdot[1.7333+2]+0.4255\cdot[2.27+3]+0.1915\cdot[2.7+4]\right)=4.658.
$$  

![](a2f52a9a4d6ae2ad5b0760089f702b9af89feead1fe5c4b8462876d702fb8e07.jpg)  
Figure 11.1: [Real-world probabilities](Change%20of%20Probability%20Measure.md) and the [state-price deflator](Exercises.md) in Example 11.2.  

![](5fbaa82e401a43e247d8c3a1121114d2eca1c065c5f0810d8f69cc4bf9a0d33f.jpg)  
Figure 11.2: [Risk-neutral probabilities](../../../Financial%20Instruments/Financial%20Instruments.md) and one-period risk-free [returns](../Chapter%203%20-%20%20Assets,%20Portfolios,%20and%20Arbitrage/Assets.md) in Example 11.2.  

![](6afb5642b9dfd827a091414f89df09ac8edfff8274d41fb12d73ba13f2a87f8c.jpg)  
Figure 11.3: Risk-neutral valuation of a dividend process in Example 11.2.  
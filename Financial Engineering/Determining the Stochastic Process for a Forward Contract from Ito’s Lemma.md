---
tags:
  - arbitrage_free_pricing
  - forward_contract
  - geometric_brownian_motion
  - ito_lemma
  - stochastic_process
aliases:
  - Forward Price Dynamics
  - Ito's Lemma
key_concepts:
  - Arbitrage-free price
  - Drift rate comparison
  - Forward contract price
  - Geometric Brownian Motion (GBM)
  - Ito's Lemma expansion
---

# Determining the Stochastic Process for a Forward Contract from Ito’s Lemma 

Let $F=F(S,t)$ . Note that $F$ is once differentiable in $t$ and twice differentiable in $S$ . [Ito's Lemma](.md) justifies the use of the following Taylor-series-like expansion for the instantaneous change in $F$ : 
$$ d F=\frac{\partial F}{\partial t}d t+\frac{\partial F}{\partial S}d S+\frac{1}{2}\frac{\partial^{2}F}{\partial S^{2}}d S^{2}. $$ 

Since $d S^{2}=S^{2}\sigma^{2}d t$ , substituting $S^{2}\sigma^{2}d t$ in place of $d S^{2}$ in the [Ito's Lemma](.md) equation yields equation (2): 
$$ \frac{\partial F}{\partial t}d t+\frac{\partial F}{\partial S}d S+\frac{1}{2}\sigma^{2}S^{2}\frac{\partial^{2}F}{\partial S^{2}}d t $$ 

Since the instantaneous change in $S$ evolves according to the [geometric Brownian motion](../Financial%20Instruments/Black%20Scholes%20Derivation.md) (GBM) equation $d S=\mu S d t+\sigma S d z$ , substituting $\mu S d t+\sigma S d z$ in place of $d S$ in equation (2) yields: 
$$ d F=\left({\frac{\partial F}{\partial t}}+{\frac{\partial F}{\partial S}}\mu S+{\frac{1}{2}}\sigma^{2}S^{2}{\frac{\partial^{2}F}{\partial S^{2}}}\right)d t+{\frac{\partial F}{\partial S}}\sigma S d z $$ 

In equation (3), we refer to $\frac{\partial F}{\partial t}$ as “theta”, $\frac{∂F}{∂S}$ as “delta”, and $\frac{\partial^{2}{\cal F}}{\partial S^{2}}$ as “gamma”. Theta measures the effect that the passage of time has on $F$ , delta measures the sensitivity of $F$ with respect to changes in $S$ , and gamma captures the sensitivity of delta with respect to changes in $S$ . 

Next, consider a [forward contract](../Clippings/Forward%20Points%20in%20Currency.md) on a non-dividend paying stock; its date $t$ “[arbitrage](../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%207/Arbitrage%20Pricing%20of%20Derivatives.md)-free” price is $F=S e^{r(T-t)}$ . Since $\mathrm{theta}={\frac{\partial F}{\partial t}}=-r S e^{r(T-t)}$ , ${\mathrm{delta}}={\frac{\partial F}{\partial S}}=e^{r(T-t)}$ , and $\mathrm{{gamma}=}$ $\frac{\partial^{2}F}{\partial S^{2}}=0$ , we are now able to infer the [stochastic process](../The%20Ornstein-Uhlenbeck%20(OU)%20Process.md) for the price of the [forward contract](../Clippings/Forward%20Points%20in%20Currency.md) by substituting the values for theta, delta and gamma into equation (3): 
$$ d F=[e^{r(T-t)}\mu S-r S e^{r(T-t)}]d t+e^{r(T-t)}\sigma S d z. $$ 

Substituting $F$ in place of $S e^{r(T-t)}$ in equation (4), we obtain 
$$ d F=(\mu-r)F d t+\sigma F d z. $$ 

Note the difference in the drift rate for the [forward contract](../Clippings/Forward%20Points%20in%20Currency.md) vis-a-vis the drift rate for the [underlying asset](../Financial%20Instruments/Financial%20Derivatives%20and%20Quantitative%20Methods/Risk%20Neutral%20Pricing%20of%20Options.md). Specifically, over infinitesimal units of time, the price of the [forward contract](../Clippings/Forward%20Points%20in%20Currency.md) grows at the rate of $(\mu-r)d t$ , whereas the [underlying asset](../Financial%20Instruments/Financial%20Derivatives%20and%20Quantitative%20Methods/Risk%20Neutral%20Pricing%20of%20Options.md) grows at the rate of µdt. Intuitively this is not a surprising result, particularly in view of the fact that the “[arbitrage](../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%207/Arbitrage%20Pricing%20of%20Derivatives.md)-free” price $F=S e^{r(T-t)}$ represents the future (date $T$ ) value of the date $t$ value of the [underlying asset](../Financial%20Instruments/Financial%20Derivatives%20and%20Quantitative%20Methods/Risk%20Neutral%20Pricing%20of%20Options.md), compounded forward at the riskless rate of interest.
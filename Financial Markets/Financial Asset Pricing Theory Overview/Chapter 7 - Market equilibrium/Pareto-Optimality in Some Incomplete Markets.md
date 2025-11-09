---
tags:
  - arrow_debreu_asset
  - hara_utility
  - incomplete_markets
  - market_completeness
  - pareto_optimality
aliases:
  - Incomplete Markets
  - Pareto Optimality
key_concepts:
  - Arrow-Debreu style asset
  - HARA utility functions
  - Pareto-optimal consumption allocation
  - aggregate consumption
  - effectively complete markets
---

# 7.4 Pareto-optimality in some incomplete markets  

In the previous section we saw that complete market equilibria are Pareto-optimal. However, as discussed earlier, real-life [financial markets](../../../Financial%20Markets%20and%20Institutions/Financial%20Markets%20and%20Institutions%20Lecture%20Notes.md) are probably not complete. Equilibrium consumption allocations in [incomplete markets](../../../International%20Finance/Lecture%20Notes%20on%20International%20Finance.md) will generally not be Pareto-optimal since the individuals cannot necessarily implement the trades needed to align their marginal rates of substitution. On the other hand, individuals do not have to be able to implement any possible consumption plan so we do not need markets to be complete in the strict sense. If every [Pareto-optimal consumption allocation](.md) can be obtained by trading in the available assets, the market is said to be effectively complete. If the market is effectively complete, we can use the [representative individual](../Chapter%208%20-%20Consumption-Based%20Asset%20Pricing/The%20Simple%20Multi-Period%20Ccapm.md) approach to [asset pricing](../../../Fixed%20Income%20Asset%20Pricing/Fixed%20Income%20Asset%20Pricing.md). In this section we will discuss some examples of [effectively complete markets](.md).  

For any [Pareto-optimal consumption allocation](.md) we know from Theorem 7.2 that the consumption of any individual is an increasing function of [aggregate consumption](.md). Individual consumption is measurable with respect to [aggregate consumption](.md). As in the discussion below Theorem 7.2, suppose that the possible values of [aggregate consumption](.md) are. $x_{1},\ldots,x_{K}$ and let $\Omega_{k}~=~\{\omega~\in$ $\Omega|C_{\omega}=x_{k}\}$ be the set of states in which [aggregate consumption](.md) equals. $x_{k}$ . If it is possible for each $k$ to form a [portfolio](../../../Advanced%20Investments/An%20Asset%20Allocation%20Primer.md) that provides a payment of 1 if the state is in. $\Omega_{k}$ and a zero payment otherwise --an [Arrow-Debreu style asset](.md) for [aggregate consumption](.md)--then the market is effectively complete. (See also Exercise 7.3.) The individuals are indifferent between states within a given subset $\Omega_{k}$ . Risk beyond [aggregate consumption](.md) risk does not carry any premium. Assuming strictly increasing utility functions, aggregate time 1 consumption will equal aggregate time 1 endowment. If we think of the aggregate endowment as the total value of the market, [aggregate consumption](.md) will equal the value of the market [portfolio](../../../Advanced%20Investments/An%20Asset%20Allocation%20Primer.md) and we can partition the state space according to the value or return of the market [portfolio](../../../Advanced%20Investments/An%20Asset%20Allocation%20Primer.md). Risk beyond [market risk](../../../Financial%20Engineering/Derivatives/Part%20I%20-%20Forwards%20and%20Futures/Chapter%205%20-%20Index%20Futures.md) is diversified away and does not carry any premium.  

If there is a full set of Arrow-Debreu style assets for [aggregate consumption](.md), markets will be. effectively complete for all strictly increasing and concave utility functions. The next theorem,. which is due to Rubinstein (1974), shows that markets are effectively complete under weaker assumptions on the available assets if individuals have utility functions of the HARA class with identical risk cautiousness. Before stating the precise result, let us review a few facts about the HARA utility functions which were defined in Section 5.6. A utility function. $u$ is of the HARA class, if the absolute risk tolerance is affine, i.e..  
$$
\operatorname{ART}(c)\equiv-{\frac{u^{\prime}(c)}{u^{\prime\prime}(c)}}=\alpha c+\beta.
$$  

The risk cautiousness is A. $\mathrm{RT}^{\prime}(c)=\alpha$ . Ignoring insignificant constants, the marginal utility must be either  
$$
u^{\prime}(c)=e^{-c/\beta},
$$  

for the case $\alpha=0$ (corresponding to [negative exponential utility](../Chapter%205%20-%20Modeling%20the%20Preferences%20of%20Individuals/Utility%20Functions%20in%20Models%20and%20in%20Reality.md)), or  
$$
u^{\prime}(c)=\left(\alpha c+\beta\right)^{-1/\alpha},
$$  

for the case $\alpha\neq0$ (which encompasses extended log-utility, [satiation HARA utility](../Chapter%205%20-%20Modeling%20the%20Preferences%20of%20Individuals/Utility%20Functions%20in%20Models%20and%20in%20Reality.md), and subsistence HARA utility).  

Theorem 7.6 Suppose that  

(i) all individuals have time-additive HARA utility functions with identical risk cautiousness;  

(ii) a [risk-free asset](../../../Financial%20Engineering/2.%20Forwards,%20Swaps,%20Futures,%20and%20Options.md) is traded;  

(ii) the time 1 endowment of all individuals are spanned by traded assets, i.e. $e^{l}\in\mathcal{M}$ $l=1,\ldots,L$  

Then the equilibrium is Pareto-optimal and the economy has a [representative individual](../Chapter%208%20-%20Consumption-Based%20Asset%20Pricing/The%20Simple%20Multi-Period%20Ccapm.md). The [optimal consumption](../Chapter%206%20-%20Individual%20optimality/Dynamic%20Programming.md) for any individual is a strictly increasing affine function of [aggregate consumption](.md).  

Proof: Suppose first that the market is complete. Then we know that the equilibrium [consumption allocation](Pareto-Optimality%20in%20Complete%20Markets.md) will be Pareto-optimal and we can find a weighting vector $\pmb{\eta}=(\eta_{1},\dots,\eta_{L})^{\top}$ so that  
$$
\eta_{k}e^{-\delta_{k}}u_{k}^{\prime}(c_{\omega}^{k})=\eta_{l}e^{-\delta_{l}}u_{l}^{\prime}(c_{\omega}^{l})
$$  

for any two individuals $k$ and $\textit{l}$ and any $\omega$ . Assume that the common risk cautiousness $\alpha$ is different from zero so that  
$$
u_{l}^{\prime}(c)=(\alpha c+\beta_{l})^{-1/\alpha},\quad l=1,\ldots,L.
$$  

(The proof for the case. $\alpha=0$ is similar.) Substituting this into the previous equation, we obtain  
$$
\eta_{k}e^{-\delta_{k}}\left(\alpha c_{\omega}^{k}+\beta_{k}\right)^{-1/\alpha}=\eta_{l}e^{-\delta_{l}}\left(\alpha c_{\omega}^{l}+\beta_{l}\right)^{-1/\alpha},
$$  

which implies that  
$$
\left(\eta_{k}e^{-\delta_{k}}\right)^{-\alpha}\left(\alpha c_{\omega}^{k}+\beta_{k}\right)\left(\eta_{l}e^{-\delta_{l}}\right)^{\alpha}=\alpha c_{\omega}^{l}+\beta_{l}.
$$  

Summing up over $l=1,\ldots,L$ , we get  
$$
\left(\eta_{k}e^{-\delta_{k}}\right)^{-\alpha}\left(\alpha c_{\omega}^{k}+\beta_{k}\right)\sum_{l=1}^{L}\left(\eta_{l}e^{-\delta_{l}}\right)^{\alpha}=\alpha\sum_{l=1}^{L}c_{\omega}^{l}+\sum_{l=1}^{L}\beta_{l}=\alpha C_{\omega}+\sum_{l=1}^{L}\beta_{l},
$$  

where $C_{\omega}$ is [aggregate consumption](.md) (or endowment) in state $\omega$ . Solving for $c_{\omega}^{k}$ , we find that.  
$$
c_{\omega}^{k}=\frac{\alpha C_{\omega}+\sum_{l=1}^{L}\beta_{l}}{\alpha\left(\eta_{k}e^{-\delta_{k}}\right)^{-\alpha}\sum_{l=1}^{L}\left(\eta_{l}e^{-\delta_{l}}\right)^{\alpha}}-\frac{\beta_{k}}{\alpha}\equiv A_{k}C_{\omega}+B_{k},
$$  

which is strictly increasing and affine in $C_{\omega}$  

The same [consumption allocation](Pareto-Optimality%20in%20Complete%20Markets.md) can be obtained in a market where a [risk-free asset](../../../Financial%20Engineering/2.%20Forwards,%20Swaps,%20Futures,%20and%20Options.md) exists and the time 1 endowments of all individuals are spanned by traded assets..  

Under the additional assumption that the time [preference](../Chapter%205%20-%20Modeling%20the%20Preferences%20of%20Individuals/Utility%20Indices.md) rates of individuals are identical, $\delta_{l}=\delta$ for all $l=1,\ldots,L$ , we can show a bit more:  

Theorem 7.7 If the assumptions of Theorem 7.6 are satisfied and individuals have identical. time [preference](../Chapter%205%20-%20Modeling%20the%20Preferences%20of%20Individuals/Utility%20Indices.md) rates, then the relative weights which the [representative individual](../Chapter%208%20-%20Consumption-Based%20Asset%20Pricing/The%20Simple%20Multi-Period%20Ccapm.md) associates to. individuals-and therefore equilibrium asset prices-will be independent of the initial distribution of aggregate endowment across individuals.  

Proof: In order to verify this, we will compute the utility function of the [representative individual](../Chapter%208%20-%20Consumption-Based%20Asset%20Pricing/The%20Simple%20Multi-Period%20Ccapm.md). Since we are assuming [time-additive utility](../Chapter%208%20-%20Consumption-Based%20Asset%20Pricing/The%20One-Period%20Ccapm.md), we will derive. $u_{\eta,0}$ and $u_{\eta,1}$ defined in (7.19) and (7.20) for any given weighting vector $\pmb{\eta}$ . We will focus on the case where the common risk cautiousness. $\alpha$ is non-zero and different from $^{1}$ so that  
$$
u_{l}(c)=\frac{1}{1-1/\alpha}\left(\alpha c+\beta_{l}\right)^{1-1/\alpha},\quad u_{l}^{\prime}(c)=\left(\alpha c+\beta_{l}\right)^{-1/\alpha},\quad l=1,\ldots,L.
$$  

(In Exercise 7.2 you are asked to do the same for the cases of extended log-utility ( $\alpha=1$ ) and [negative exponential utility](../Chapter%205%20-%20Modeling%20the%20Preferences%20of%20Individuals/Utility%20Functions%20in%20Models%20and%20in%20Reality.md) ( $\alpha=0$ ).) The first-order condition for the maximization in the definition of $u_{\eta,0}$ implies that  
$$
\eta_{l}\left(\alpha c+\beta_{l}\right)^{-1/\alpha}=\nu,
$$  

where $\nu$ is the Lagrange multiplier. Rearranging, we get  
$$
\alpha c_{0}^{l}+\beta_{l}=\nu^{-\alpha}\eta_{l}^{\alpha}.
$$  

Summing up over $\textit{l}$ gives  
$$
\alpha c_{0}+\sum_{l=1}^{L}\beta_{l}=\nu^{-\alpha}\sum_{l=1}^{L}\eta_{l}^{\alpha},
$$  

so that the Lagrange multiplier is  
$$
\nu=\left(\alpha c_{0}+\sum_{l=1}^{L}\beta_{l}\right)^{-1/\alpha}\left(\sum_{l=1}^{L}\eta_{l}^{\alpha}\right)^{1/\alpha}.
$$  

Substituting this back into (7.22), we see that the solution to the maximization problem is such that  
$$
\eta_{l}\left(\alpha c+\beta_{l}\right)^{-1/\alpha}=\left(\alpha c_{0}+\sum_{l=1}^{L}\beta_{l}\right)^{-1/\alpha}\left(\sum_{l=1}^{L}\eta_{l}^{\alpha}\right)^{1/\alpha},
$$  

which implies that  
$$
\begin{array}{l}{{\displaystyle u_{\eta,0}(c_{0})=\sum_{l=1}^{L}\eta_{l}\frac{1}{1-1/\alpha}\left(\alpha c_{0}^{l}+\beta_{l}\right)^{1-1/\alpha}}}\ {{\displaystyle\quad=\frac{1}{1-1/\alpha}\sum_{l=1}^{L}\left(\alpha c_{0}^{l}+\beta_{l}\right)\eta_{l}\left(\alpha c_{0}^{l}+\beta_{l}\right)^{-1/\alpha}}}\ {{\displaystyle\quad\quad=\frac{1}{1-1/\alpha}\left(\alpha c_{0}+\sum_{l=1}^{L}\beta_{l}\right)^{-1/\alpha}\left(\sum_{l=1}^{L}\eta_{l}^{\alpha}\right)^{1/\alpha}\sum_{l=1}^{L}\left(\alpha c_{0}^{l}+\beta_{l}\right)}}\ {{\displaystyle\quad\quad=\frac{1}{1-1/\alpha}\left(\sum_{l=1}^{L}\eta_{l}^{\alpha}\right)^{1/\alpha}\left(\alpha c_{0}+\sum_{l=1}^{L}\beta_{l}\right)^{1-1/\alpha}.}}\end{array}
$$  

Almost identical computations lead to  
$$
u_{\eta,1}(c)=e^{-\delta}\frac{1}{1-1/\alpha}\left(\sum_{l=1}^{L}\eta_{l}^{\alpha}\right)^{1/\alpha}\left(\alpha c+\sum_{l=1}^{L}\beta_{l}\right)^{1-1/\alpha}
$$  

The utility function of the [representative individual](../Chapter%208%20-%20Consumption-Based%20Asset%20Pricing/The%20Simple%20Multi-Period%20Ccapm.md) is therefore of the same class as the individual utility functions,  
$$
\begin{array}{r}{\mathcal{U}_{\eta}(c_{0},c)=u_{\eta,0}(c_{0})+\mathrm{E}\left[u_{\eta,1}(c)\right]=u_{\eta}(c_{0})+e^{-\delta}\mathrm{E}[u_{\eta}(c)],}\end{array}
$$  

where  
$$
u_{\eta}(c)=\frac{1}{1-1/\alpha}\left(\sum_{l=1}^{L}\eta_{l}^{\alpha}\right)^{1/\alpha}\left(\alpha c+\sum_{l=1}^{L}\beta_{l}\right)^{1-1/\alpha}.
$$  

More importantly, the [state-price deflator](Exercises.md) is  
$$
\begin{array}{c}{{\zeta=e^{-\delta}\displaystyle\frac{u_{\eta}^{\prime}(c)}{u_{\eta}^{\prime}(c_{0})}=e^{-\delta}\displaystyle\frac{\left(\sum_{l=1}^{L}\eta_{l}^{\alpha}\right)^{1/\alpha}\left(\alpha c+\sum_{l=1}^{L}\beta_{l}\right)^{-1/\alpha}}{\left(\sum_{l=1}^{L}\eta_{l}^{\alpha}\right)^{1/\alpha}\left(\alpha c_{0}+\sum_{l=1}^{L}\beta_{l}\right)^{-1/\alpha}}}}\ {{=e^{-\delta}\displaystyle\frac{\left(\alpha c+\sum_{l=1}^{L}\beta_{l}\right)^{-1/\alpha}}{\left(\alpha c_{0}+\sum_{l=1}^{L}\beta_{l}\right)^{-1/\alpha}},}}\end{array}
$$  

which is independent of the weighting vector $\pmb{\eta}$ . The [state-price deflator](Exercises.md) and, hence, the asset prices are independent of the distribution of endowment across individuals.  
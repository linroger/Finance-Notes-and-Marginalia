---
tags:
  - asset_returns
  - consumption_growth
  - continuous_time
  - multi_period_model
  - risk_free_rate
aliases:
  - Consumption and Returns
  - Multi-Period Analysis
key_concepts:
  - Consumption-beta equation
  - Excess expected return
  - Relative consumption growth
  - Risk-free gross return
  - State-price deflator
  - Time-additive expected utility
---

# 8.3 General multi-period link between consumption and asset returns  

Now take the analysis to multi-period settings. Assuming [time-additive expected utility](.md) we can define a [state-price deflator](Exercises.md) from the [optimal consumption plan](../Chapter%209%20-%20Factor%20Models/Theoretical%20Factors.md) of any individual as  
$$
\zeta_{t}=e^{-\delta t}\frac{u^{\prime}(c_{t})}{u^{\prime}(c_{0})}.
$$  

This is true both in the discrete-time and in the [continuous-time setting](../Chapter%206%20-%20Individual%20optimality/The%20Continuous-Time%20Framework.md). If a [representative individual](The%20Simple%20Multi-Period%20Ccapm.md) exists, the equation holds for [aggregate consumption](../Chapter%207%20-%20Market%20equilibrium/Pareto-Optimality%20in%20Some%20Incomplete%20Markets.md)..  

Not surprisingly, the multi-period discrete-time setting leads to equations very similar to those derived in the [one-period framework](../Chapter%204%20-%20State%20Prices/Properties%20of%20State-Price%20Deflators.md) in the previous section. Since.  
$$
\frac{\zeta_{t+1}}{\zeta_{t}}=e^{-\delta}\frac{u^{\prime}(c_{t+1})}{u^{\prime}(c_{t})},
$$  

we get from (4.25) and (4.26) that the [risk-free gross return](.md) is  
$$
R_{t}^{f}=e^{\delta}\left(\mathrm{E}_{t}\left[\frac{u^{\prime}(c_{t+1})}{u^{\prime}(c_{t})}\right]\right)^{-1}
$$  

and that the excess expected gross return on a risky asset is  
$$
\begin{array}{r l}&{\mathrm{E}_{t}[R_{i,t+1}]-R_{t}^{f}=-\frac{\mathrm{Cov}_{t}[u^{\prime}(c_{t+1})/u^{\prime}(c_{t}),R_{i,t+1}]}{\mathrm{E}_{t}[u^{\prime}(c_{t+1})/u^{\prime}(c_{t})]}}\ &{\qquad=\rho_{t}\left[R_{i,t+1},\frac{u^{\prime}(c_{t+1})}{u^{\prime}(c_{t})}\right]\sigma_{t}[R_{i,t+1}]\left(-\frac{\sigma_{t}[u^{\prime}(c_{t+1})/u^{\prime}(c_{t})]}{\mathrm{E}_{t}[u^{\prime}(c_{t+1})/u^{\prime}(c_{t})]}\right).}\end{array}
$$  

These equations are the multi-period equivalents of the Equations (8.1) and (8.2) for the one-period. model. As in the one-period case, we can obtain an approximate relation between expected [returns](../Chapter%203%20-%20%20Assets,%20Portfolios,%20and%20Arbitrage/Assets.md) and [relative consumption growth](.md), $g_{t+1}=c_{t+1}/c_{t}-1$ , over the next period,  
$$
\begin{array}{r}{\mathrm{E}_{t}[R_{i,t+1}]-R_{t}^{f}\approx\gamma(c_{t})\mathrm{Cov}_{t}[g_{t+1},R_{i,t+1}],}\end{array}
$$  

and also an approximate [consumption-beta equation](.md)  
$$
\begin{array}{r}{\mathrm{E}_{t}[R_{i,t+1}]-R_{t}^{f}\approx\beta_{t}[R_{i,t+1},R_{t+1}^{c}]\left(\mathrm{E}_{t}[R_{t+1}^{c}]-R_{t}^{f}\right),}\end{array}
$$  

where $\beta_{t}[R_{i,t+1},R_{t+1}^{c}]=\operatorname{Cov}_{t}[R_{i,t+1},R_{t+1}^{c}]/\operatorname{Var}_{t}[R_{t+1}^{c}]$ and $R_{t+1}^{c}$ is the gross return on a [portfolio](../../../Advanced%20Investments/An%20Asset%20Allocation%20Primer.md) perfectly correlated with [consumption growth](Long-Run%20Risks%20and%20Epstein-Zin%20Utility.md) over this period.  

Now let us turn to the [continuous-time setting](../Chapter%206%20-%20Individual%20optimality/The%20Continuous-Time%20Framework.md). Suppose that the dynamics of consumption can be written as  
$$
d c_{t}=c_{t}\left[\mu_{c t}\:d t+\pmb{\sigma}_{c t}^{\top}\:d z_{t}\right],
$$  

where $\mu_{c t}$ is the expected relative growth rate of consumption and. $\sigma_{c t}$ is the vector of sensitivities. of [consumption growth](Long-Run%20Risks%20and%20Epstein-Zin%20Utility.md) to the [exogenous shocks](../Chapter%202%20-%20Uncertainty,%20Information,%20and%20Stochastic%20Processes/Some%20Discrete-Time%20Stochastic%20Processes.md) to the economy. In particular, the variance of [relative consumption growth](.md) is given by $\|\sigma_{c t}\|^{2}$ .Given the dynamics of consumption and the. relation (8.16) we can obtain the dynamics of $\zeta_{t}$ by an application of [Ito's Lemma](../../../Financial%20Engineering/Determining%20the%20Stochastic%20Process%20for%20a%20Forward%20Contract%20from%20Ito’s%20Lemma.md) on the function. $g(t,c)=e^{-\partial t}u^{\prime}(c)/u^{\prime}(c_{0})$ . The relevant [derivatives](../../Financial%20Trading%20and%20Markets/Chapter%209%20Arbitrage%20and%20Hedging%20With%20Options.md) are  
$$
\frac{\partial g}{\partial t}(t,c)=-\delta e^{-\delta t}\frac{u^{\prime}(c)}{u^{\prime}(c_{0})},\quad\frac{\partial g}{\partial c}(t,c)=e^{-\delta t}\frac{u^{\prime\prime}(c)}{u^{\prime}(c_{0})},\quad\frac{\partial^{2}g}{\partial c^{2}}(t,c)=e^{-\delta t}\frac{u^{\prime\prime\prime}(c)}{u^{\prime}(c_{0})},
$$  

implying that  
$$
\begin{array}{l}{\displaystyle\frac{\partial g}{\partial t}(t,c_{t})=-\delta e^{-\delta t}\frac{u^{\prime}(c_{t})}{u^{\prime}(c_{0})}=-\delta\zeta_{t},}\ {\displaystyle\frac{\partial g}{\partial c}(t,c_{t})=e^{-\delta t}\frac{u^{\prime\prime}(c_{t})}{u^{\prime}(c_{0})}=\frac{u^{\prime\prime}(c_{t})}{u^{\prime}(c_{t})}\zeta_{t}=-\gamma(c_{t})c_{t}^{-1}\zeta_{t},}\ {\displaystyle\frac{\partial^{2}g}{\partial c^{2}}(t,c_{t})=e^{-\delta t}\frac{u^{\prime\prime\prime}(c_{t})}{u^{\prime}(c_{0})}=\frac{u^{\prime\prime\prime}(c_{t})}{u^{\prime}(c_{t})}\zeta_{t}=\eta(c_{t})c_{t}^{-2}\zeta_{t},}\end{array}
$$  

where $\gamma(c_{t})\equiv-c_{t}u^{\prime\prime}(c_{t})/u^{\prime}(c_{t})$ is the [relative risk aversion](CCAPM%20with%20Alternative%20Preferences.md) of the individual, and where $\eta(c_{t})\equiv$ $c_{t}^{2}u^{\prime\prime\prime}(c_{t})/u^{\prime}(c_{t})$ is positive under the very plausible assumption that the [absolute risk aversion](../Chapter%205%20-%20Modeling%20the%20Preferences%20of%20Individuals/Utility%20Functions%20in%20Models%20and%20in%20Reality.md) of the individual is decreasing in the level of consumption. Consequently, the dynamics of the [state-price deflator](Exercises.md) can be expressed as  
$$
d\zeta_{t}=-\zeta_{t}\left[\Big(\delta+\gamma(c_{t})\mu_{c t}-\frac{1}{2}\eta(c_{t})\|\sigma_{c t}\|^{2}\Big)d t+\gamma(c_{t})\sigma_{c t}^{\top}d z_{t}\right],
$$  

Comparing the above equation with (4.41), we can draw the conclusions summarized in the following theorem:  

Theorem 8.1 In a [continuous-time economy](../Chapter%2011%20-%20Risk-adjusted%20probabilities/Risk-Neutral%20Probabilities.md) where the [optimal consumption process](../Chapter%206%20-%20Individual%20optimality/The%20Continuous-Time%20Framework.md) of an in-. dividual with [time-additive expected utility](.md) satisfies (8.21), the continuously compounded risk-free [short-term interest rate](../../Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%209/The%20Gauss%20Model.md) satisfies  
$$
r_{t}^{f}=\delta+\gamma(c_{t})\mu_{c t}-\frac{1}{2}\eta(c_{t})\|\pmb{\sigma}_{c t}\|^{2}
$$  

and  
$$
\lambda_{t}=\gamma(c_{t})\sigma_{c t}
$$  

defines a [market price of risk](Exercises.md) process. Here $\gamma(c_{t})=-c_{t}u^{\prime\prime}(c_{t})/u^{\prime}(c_{t})$ and $\eta(c_{t})=c_{t}^{2}u^{\prime\prime\prime}(c_{t})/u^{\prime}(c_{t})$  

Equation (8.23) gives the interest rate at which the market for [short-term borrowing and lending](../../../International%20Finance/Characteristics%20of%20the%20Eurodollar%20Market.md). will clear. The equation relates the equilibrium [short-term interest rate](../../Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%209/The%20Gauss%20Model.md) to the time [preference](../Chapter%205%20-%20Modeling%20the%20Preferences%20of%20Individuals/Utility%20Indices.md) rate and the expected growth rate $\mu_{c t}$ and the variance rate $\|\sigma_{c t}\|^{2}$ of [aggregate consumption growth](Exercises.md) over the next instant. We can observe the following relations:.  

: There is a positive relation between the time [preference](../Chapter%205%20-%20Modeling%20the%20Preferences%20of%20Individuals/Utility%20Indices.md) rate and the [equilibrium interest rate](../Chapter%2010%20-%20The%20Economics%20of%20the%20Term%20Structure%20of%20Interest%20Rates/Real%20Interest%20Rates%20and%20Aggregate%20Consumption.md). The intuition behind this is that when the individuals of the economy are impatient and has a high demand for current consumption, the [equilibrium interest rate](../Chapter%2010%20-%20The%20Economics%20of%20the%20Term%20Structure%20of%20Interest%20Rates/Real%20Interest%20Rates%20and%20Aggregate%20Consumption.md) must be high in order to encourage the individuals to save now and postpone consumption..   
. The multiplier of $\mu_{c t}$ in (8.23) is the [relative risk aversion](CCAPM%20with%20Alternative%20Preferences.md) of the [representative individual](The%20Simple%20Multi-Period%20Ccapm.md), which is positive. Hence, there is a positive relation between the expected growth in [aggregate consumption](../Chapter%207%20-%20Market%20equilibrium/Pareto-Optimality%20in%20Some%20Incomplete%20Markets.md) and the [equilibrium interest rate](../Chapter%2010%20-%20The%20Economics%20of%20the%20Term%20Structure%20of%20Interest%20Rates/Real%20Interest%20Rates%20and%20Aggregate%20Consumption.md). This can be explained as follows: We expect. higher future consumption and hence lower future marginal utility, so postponed payments due to saving have lower value. Consequently, a higher return on saving is needed to maintain market clearing.   
If $u^{\prime\prime\prime}$ is positive, there will be a negative relation between the variance of aggregate con-. sumption and the [equilibrium interest rate](../Chapter%2010%20-%20The%20Economics%20of%20the%20Term%20Structure%20of%20Interest%20Rates/Real%20Interest%20Rates%20and%20Aggregate%20Consumption.md). If the [representative individual](The%20Simple%20Multi-Period%20Ccapm.md) has decreasing [absolute risk aversion](../Chapter%205%20-%20Modeling%20the%20Preferences%20of%20Individuals/Utility%20Functions%20in%20Models%20and%20in%20Reality.md), which is certainly a reasonable assumption,. $u^{\prime\prime\prime}$ has to be positive. The intuition is that the greater the uncertainty about future consumption, the more will the individuals appreciate the sure payments from the [risk-free asset](../../../Financial%20Engineering/2.%20Forwards,%20Swaps,%20Futures,%20and%20Options.md) and hence the lower a return is necessary to clear the market for [borrowing and lending](../../../Financial%20Instruments/Lecture%20Notes-%20Financial%20Instruments/Teaching%20Note%203%20Swaps-%20Financial%20Instruments/Swaps%20Types.md).  

If we substitute (8.24) into (4.39) we see that the excess expected rate of return on asset $i$ OVer the instant following time $t$ can be written as  
$$
\mu_{i t}+\delta_{i t}-r_{t}^{f}=\gamma(c_{t})\pmb{\sigma}_{i t}^{\top}\pmb{\sigma}_{c t}=\gamma(c_{t})\rho_{i c t}\left\|\pmb{\sigma}_{i t}\right\|\left\|\pmb{\sigma}_{c t}\right\|.
$$  

Here $\sigma_{i t}^{\top}\sigma_{c t}$ and $\rho_{i c t}$ are the covariance and correlation between the rate of return on asset $i$ and the [consumption growth rate](Exercises.md), respectively, and. $\lVert\pmb{\sigma}_{i t}\rVert$ and $\|\sigma_{c t}\|$ are standard deviations (volatilities) of the rate of return on asset. $i$ and the [consumption growth rate](Exercises.md), respectively. Equation (8.25) is the continuous-time version of (8.19). Note that the continuous-time relation is exact. Again, if we can find a trading strategy "mimicking" the consumption process (same volatility, perfect correlation) we get the "consumption-beta" relation  
$$
\mu_{i t}+\delta_{i t}-r_{t}^{f}=\beta_{i t}^{c}\left(\mu_{t}^{*}+\delta_{t}^{*}-r_{t}^{f}\right),
$$  

where $\beta_{i t}^{c}=\pmb{\sigma}_{i t}^{\top}\pmb{\sigma}_{c t}/\lVert\pmb{\sigma}_{c t}\rVert^{2}$  

If the market is effectively complete, the above equations are valid for [aggregate consumption](../Chapter%207%20-%20Market%20equilibrium/Pareto-Optimality%20in%20Some%20Incomplete%20Markets.md). if we apply the utility function and time [preference](../Chapter%205%20-%20Modeling%20the%20Preferences%20of%20Individuals/Utility%20Indices.md) rate of the [representative individual](The%20Simple%20Multi-Period%20Ccapm.md). The [representative individual](The%20Simple%20Multi-Period%20Ccapm.md) version of Equation (8.25) says that risky assets are priced so that the [expected excess return](../Chapter%209%20-%20Factor%20Models/Theoretical%20Factors.md) on an asset is given by the product of the [relative risk aversion](CCAPM%20with%20Alternative%20Preferences.md) of the [representative individual](The%20Simple%20Multi-Period%20Ccapm.md) and the covariance between the asset return and the growth rate of [aggregate consumption](../Chapter%207%20-%20Market%20equilibrium/Pareto-Optimality%20in%20Some%20Incomplete%20Markets.md). This is the key result in the [Consumption-based CAPM](../Chapter%2012%20-%20Derivatives/Concluding%20Remarks.md) (or just CCAPM) developed by Breeden (1979).  

As already indicated in the [one-period framework](../Chapter%204%20-%20State%20Prices/Properties%20of%20State-Price%20Deflators.md), we can obtain a relation between expected [returns](../Chapter%203%20-%20%20Assets,%20Portfolios,%20and%20Arbitrage/Assets.md) and [aggregate consumption](../Chapter%207%20-%20Market%20equilibrium/Pareto-Optimality%20in%20Some%20Incomplete%20Markets.md) also if the market is incomplete and no [representative individual](The%20Simple%20Multi-Period%20Ccapm.md) exists. Let us stick to the [continuous-time setting](../Chapter%206%20-%20Individual%20optimality/The%20Continuous-Time%20Framework.md). Let $c_{l}=\left(c_{l t}\right)$ denote the [optimal consumption process](../Chapter%206%20-%20Individual%20optimality/The%20Continuous-Time%20Framework.md) of individual number $\textit{l}$ in the economy and assume that  
$$
d c_{l t}=c_{l t}\left[\mu_{c l t}d t+\sigma_{c l t}^{\top}d z_{t}\right].
$$  

If there are $L$ individuals in the economy, [aggregate consumption](../Chapter%207%20-%20Market%20equilibrium/Pareto-Optimality%20in%20Some%20Incomplete%20Markets.md) is $\begin{array}{r}{C_{t}=\sum_{l=1}^{L}c_{l t}}\end{array}$ and we have that  
$$
\begin{array}{l}{\displaystyle{d C_{t}=\sum_{l=1}^{L}d c_{l t}=\left(\sum_{l=1}^{L}c_{l t}\mu_{c l t}\right)d t+\left(\sum_{l=1}^{L}c_{l t}\sigma_{c l t}\right)^{\top}d z_{t}}}\ {\displaystyle{~\equiv C_{t}\left[\mu_{C t}d t+\pmb{\sigma}_{C t}^{\top}d z_{t}\right],}}\end{array}
$$  

where $\begin{array}{r}{\mu_{C t}\equiv\left(\sum_{l=1}^{L}c_{l t}\mu_{c l t}\right)/C_{t}}\end{array}$ and $\begin{array}{r}{\pmb{\sigma}_{C t}=\left(\sum_{l=1}^{L}c_{l t}\pmb{\sigma}_{c l t}\right)/C_{t}}\end{array}$ . We know from (8.25) that  
$$
\mu_{i t}+\delta_{i t}-r_{t}^{f}=A_{l}(c_{l t})c_{l t}\pmb{\sigma}_{i t}^{\top}\pmb{\sigma}_{c l t},\quad l=1,\ldots,L,
$$  

where $A_{l}(c_{l t})\equiv-u_{l}^{\prime\prime}(c_{l t})/u_{l}^{\prime}(c_{l t})$ is the [absolute risk aversion](../Chapter%205%20-%20Modeling%20the%20Preferences%20of%20Individuals/Utility%20Functions%20in%20Models%20and%20in%20Reality.md) of individual $\textit{l}$ . Consequently,  
$$
\left(\mu_{i t}+\delta_{i t}-r_{t}^{f}\right)\frac{1}{A_{l}(c_{l t})}=c_{l t}\pmb{\sigma}_{i t}^{\top}\pmb{\sigma}_{c l t},\quad l=1,\ldots,L,
$$  

and summing up over $l$ , we get  
$$
\left(\mu_{i t}+\delta_{i t}-r_{t}^{f}\right)\sum_{l=1}^{L}\left(\frac{1}{A_{l}(c_{l t})}\right)=\sigma_{i t}^{\top}\left(\sum_{l=1}^{L}c_{l t}\sigma_{c l t}\right)=\sigma_{i t}^{\top}\left(C_{t}\sigma_{C t}\right).
$$  

Therefore, we have the following relation between excess expected [returns](../Chapter%203%20-%20%20Assets,%20Portfolios,%20and%20Arbitrage/Assets.md) and [aggregate consumption](../Chapter%207%20-%20Market%20equilibrium/Pareto-Optimality%20in%20Some%20Incomplete%20Markets.md):  
$$
\mu_{i t}+\delta_{i t}-r_{t}^{f}=\frac{C_{t}}{\sum_{l=1}^{L}\left(\frac{1}{A_{l}\left(c_{l t}\right)}\right)}\pmb{\sigma}_{i t}^{\top}\pmb{\sigma}_{C t}.
$$  

Relative to the [complete markets](../../../Financial%20Engineering/Financial%20Mathematics%20Course.md) version (8.25), the only difference is that the [relative risk aversion](CCAPM%20with%20Alternative%20Preferences.md) of the [representative individual](The%20Simple%20Multi-Period%20Ccapm.md) is replaced by some complicated average of the risk aversions of the individuals. Note that if all individuals have [CRRA utility](The%20Simple%20Multi-Period%20Ccapm.md) with identical relative risk aversions, then $A_{l}(c_{l t})=\gamma/c_{l t}$ and the multilier $\begin{array}{r}{C_{t}/\sum_{l=1}^{L}\left(\frac{1}{A_{l}\left(c_{l t}\right)}\right)}\end{array}$ in the above equation reduces to $\gamma$  

The [Consumption-based CAPM](../Chapter%2012%20-%20Derivatives/Concluding%20Remarks.md) is a very general [asset pricing](../../../Fixed%20Income%20Asset%20Pricing/Fixed%20Income%20Asset%20Pricing.md) result. Basically any [asset pricing](../../../Fixed%20Income%20Asset%20Pricing/Fixed%20Income%20Asset%20Pricing.md). model can be seen as a special case of the [Consumption-based CAPM](../Chapter%2012%20-%20Derivatives/Concluding%20Remarks.md). On the other hand, the general [Consumption-based CAPM](../Chapter%2012%20-%20Derivatives/Concluding%20Remarks.md) is not very useful for applications without further assumptions. Therefore we turn now to more specific consumption-based models..  
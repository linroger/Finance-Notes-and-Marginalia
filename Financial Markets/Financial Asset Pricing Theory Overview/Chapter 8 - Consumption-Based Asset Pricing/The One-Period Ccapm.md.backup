---
tags:
  - asset_pricing
  - ccapm
  - consumption_based_model
  - consumption_growth
  - risk_aversion
aliases:
  - One-Period CCAPM
  - Simple CCAPM
key_concepts:
  - Expected excess returns
  - Marginal rate of substitution
  - Risk-free return
  - State-price deflator
  - Time-additive utility
---

# 8.2 The one-period CCAPM  

For simplicity let us first investigate the link between asset prices and consumption in the oneperiod framework.  

As discussed several times the [marginal rate of substitution](.md) of any individual defines a stateprice deflator. If we assume [time-additive expected utility](General%20Multi-Period%20Link%20Between%20Consumption%20a.md) with time [preference](../Chapter%205%20-%20Modeling%20the%20Preferences%20of%20Individuals/Utility%20Indices.md) rate. $\delta$ and utility function $u$ , this [state-price deflator](Exercises.md) is.  
$$
\zeta=e^{-\delta}\frac{u^{\prime}(c)}{u^{\prime}(c_{0})},
$$  

where $c_{0}$ is optimal time $0$ consumption and $c$ is the state-dependent optimal time 1 consumption. If the economy can be modeled by a [representative individual](The%20Simple%20Multi-Period%20Ccapm.md), the equation holds for [aggregate consumption](../Chapter%207%20-%20Market%20equilibrium/Pareto-Optimality%20in%20Some%20Incomplete%20Markets.md).  

Assuming that a [risk-free asset](../../../Financial%20Engineering/2.%20Forwards,%20Swaps,%20Futures,%20and%20Options.md) is traded, we know from Section 4.2.1 that the gross risk-free  

return is  
$$
R^{f}={\frac{1}{\operatorname{E}[\zeta]}}=e^{\delta}{\frac{1}{\operatorname{E}[u^{\prime}(c)/u^{\prime}(c_{0})]}}
$$  

and the expected gross return on any asset $i$ is  
$$
\begin{array}{r l}&{\mathrm{E}[R_{i}]=\frac{1}{\mathrm{E}[\boldsymbol{\zeta}]}-\frac{\mathrm{Cov}[R_{i},\boldsymbol{\zeta}]}{\mathrm{E}[\boldsymbol{\zeta}]}}\ &{\quad\quad=R^{f}-\frac{\mathrm{Cov}[u^{\prime}(\boldsymbol{c})/u^{\prime}(\boldsymbol{c}_{0}),R_{i}]}{\mathrm{E}[u^{\prime}(\boldsymbol{c})/u^{\prime}(\boldsymbol{c}_{0})]}}\ &{\quad\quad=R^{f}-\frac{\sigma[u^{\prime}(\boldsymbol{c})/u^{\prime}(\boldsymbol{c}_{0})]}{\mathrm{E}[u^{\prime}(\boldsymbol{c})/u^{\prime}(\boldsymbol{c}_{0})]}\sigma[R_{i}]\rho[R_{i},u^{\prime}(\boldsymbol{c})/u^{\prime}(\boldsymbol{c}_{0})],}\end{array}
$$  

where $\sigma[x]$ denotes the standard deviation of the random variable $x$ , while $\rho[x,y]$ is the correlation between the random variables $x$ and $y$ . An asset with a return which is positively correlated with. the [marginal utility of consumption](../../../Financial%20Engineering/Appendices/Appendix%2022.C%20Risk-Neutral%20Pricing%20and%20Marginal%20Utility%20in%20the%20Binomial%20Model.md) (and hence negatively correlated with the level of consumption) is attractive, has a high equilibrium price, and thus a low [expected return](../../../Advanced%20Investments/Lecture%201-%20Probability%20Distributions%20of%20Returns.md)..  

In order to obtain a relation between expected [returns](../Chapter%203%20-%20%20Assets,%20Portfolios,%20and%20Arbitrage/Assets.md) and consumption itself (rather than [marginal utility of consumption](../../../Financial%20Engineering/Appendices/Appendix%2022.C%20Risk-Neutral%20Pricing%20and%20Marginal%20Utility%20in%20the%20Binomial%20Model.md)) we need to make further assumptions or approximations. Below we develop three versions.  

# 8.2.1 The simple one-period CCAPM: version 1  

A first-order [Taylor approximation](../../Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%207/Profit%20and%20Loss%20Attribution%20with%20an%20OAS.md) of $u^{\prime}(c)$ around $c_{0}$ gives that  
$$
\frac{u^{\prime}(c)}{u^{\prime}(c_{0})}\approx\frac{u^{\prime}(c_{0})+u^{\prime\prime}(c_{0})(c-c_{0})}{u^{\prime}(c_{0})}=1-\gamma(c_{0})g,
$$  

where $\gamma(c_{0})=-c_{0}u^{\prime\prime}(c_{0})/u^{\prime}(c_{0})$ is the [relative risk aversion](CCAPM%20with%20Alternative%20Preferences.md) of the individual evaluated at the time 0 consumption level, and $g=c/c_{0}-1$ is the (state-dependent) relative growth rate of consumption over the period. If we further assume that $\operatorname{E}[u^{\prime}(c)/u^{\prime}(c_{0})]\approx1$ , we get that  
$$
\operatorname{E}[R_{i}]-R^{f}\approx\gamma(c_{0})\operatorname{Cov}[g,R_{i}]=\gamma(c_{0})\rho[g,R_{i}]\sigma[g]\sigma[R_{i}],
$$  

where $\rho[g,R_{i}]$ is the correlation between [consumption growth](Long-Run%20Risks%20and%20Epstein-Zin%20Utility.md) and the return and. $\sigma[g]$ and $\sigma[R_{i}]$ are the standard deviations of [consumption growth](Long-Run%20Risks%20and%20Epstein-Zin%20Utility.md) and return, respectively. The above equation links expected excess [returns](../Chapter%203%20-%20%20Assets,%20Portfolios,%20and%20Arbitrage/Assets.md) to covariance with [consumption growth](Long-Run%20Risks%20and%20Epstein-Zin%20Utility.md). We can rewrite the equation as  
$$
\begin{array}{r}{\operatorname{E}[R_{i}]\approx R^{f}+\beta[R_{i},g]\eta,}\end{array}
$$  

where $\beta[R_{i},g]=\mathrm{Cov}[g,R_{i}]/\mathrm{Var}[g]$ and $\eta=\gamma(c_{0})\operatorname{Var}[g]$ . If we ignore the approximative character of the equation, it shows that the growth rate of the individual's [optimal consumption](../Chapter%206%20-%20Individual%20optimality/Dynamic%20Programming.md) is a [pricing factor](../Chapter%209%20-%20Factor%20Models/Pricing%20Factors%20in%20a%20One-Period%20Framework.md).  

If the economy has a [representative individual](The%20Simple%20Multi-Period%20Ccapm.md) we can use the above relations with [aggregate consumption](../Chapter%207%20-%20Market%20equilibrium/Pareto-Optimality%20in%20Some%20Incomplete%20Markets.md) instead of individual consumption. The factor risk premium $\eta$ should then reflect the [relative risk aversion](CCAPM%20with%20Alternative%20Preferences.md) of the [representative individual](The%20Simple%20Multi-Period%20Ccapm.md)..  

What if the economy does not have a [representative individual](The%20Simple%20Multi-Period%20Ccapm.md)? Eq. (8.3) will still hold for any individual $\textit{l}$ , i.e.  
$$
\mathrm{E}[R_{i}]-R^{f}\approx\gamma_{l}(c_{0}^{l})\mathrm{Cov}[c^{l}/c_{0}^{l},R_{i}]=\mathrm{ARA}_{l}(c_{0}^{l})\mathrm{Cov}[c^{l},R_{i}],
$$  

where y and $\mathrm{ARA}_{l}$ are the relative and [absolute risk aversion](../Chapter%205%20-%20Modeling%20the%20Preferences%20of%20Individuals/Utility%20Functions%20in%20Models%20and%20in%20Reality.md) of individual $\textit{l}$ , so that  
$$
\left(\operatorname{E}[R_{i}]-R^{f}\right){\frac{1}{\operatorname{ARA}_{l}(c_{0}^{l})}}\approx\operatorname{Cov}[c^{l},R_{i}],\quad l=1,2,\ldots,L.
$$  

Summing up over all individuals, we get  
$$
\left(\operatorname{E}[R_{i}]-R^{f}\right)\sum_{l=1}^{L}{\frac{1}{\operatorname{ARA}_{l}(c_{0}^{l})}}\approx\sum_{l=1}^{L}\operatorname{Cov}[c^{l},R_{i}]=\operatorname{Cov}\left[\sum_{l=1}^{L}c^{l},R_{i}\right]=\operatorname{Cov}[C,R_{i}],
$$  

where $C$ is aggregate time 1 consumption. If we let $C_{0}$ denote aggregate time $0$ consumption, we obtain  
$$
\operatorname{E}[R_{i}]-R^{f}\approx\left(\sum_{l=1}^{L}{\frac{1}{\mathrm{ARA}_{l}(c_{0}^{l})}}\right)^{-1}C_{0}\operatorname{Cov}[C/C_{0},R_{i}].
$$  

Again ignoring the approximation, this equation shows that [aggregate consumption growth](Exercises.md) is a [pricing factor](../Chapter%209%20-%20Factor%20Models/Pricing%20Factors%20in%20a%20One-Period%20Framework.md) even if there is no [representative individual](The%20Simple%20Multi-Period%20Ccapm.md). We just need to replace the [relative risk aversion](CCAPM%20with%20Alternative%20Preferences.md) of the [representative individual](The%20Simple%20Multi-Period%20Ccapm.md) by some complex average of individual risk aversions. The absolute risk tolerance of individual $l$ is exactly $1/\mathrm{ARA}_{l}(c_{0}^{l})$ so the first term on the right-hand side of the above equation can be interpreted as the inverse of the aggregate absolute risk tolerance in the economy. The higher the aggregate absolute risk tolerance, the lower the equilibrium risk premium on risky assets.  

Of course, we prefer exact [asset pricing](../../../Fixed%20Income%20Asset%20Pricing/Fixed%20Income%20Asset%20Pricing.md) results to approximate. In a later section, we will show that in [continuous-time models](../../../Financial%20Engineering/Financial%20Mathematics%20Course.md) the analogues to the above relations will hold as exact equalities under appropriate assumptions.  

# 8.2.2 The simple one-period CCAPM: version 2  

Suppose that  

(i) the individual has constant [relative risk aversion](CCAPM%20with%20Alternative%20Preferences.md), $u(c)=c^{1-\gamma}/(1-\gamma)$  

(ii) [consumption growth](Long-Run%20Risks%20and%20Epstein-Zin%20Utility.md) is lognormally distributed,  
$$
\ln(1+g)\equiv\ln\left(\frac{c}{c_{0}}\right)\sim N(\bar{g},\sigma_{g}^{2}).
$$  

Then  
$$
\frac{u^{\prime}(c)}{u^{\prime}(c_{0})}=\left(\frac{c}{c_{0}}\right)^{-\gamma}=\exp\left\{-\gamma\ln\left(\frac{c}{c_{0}}\right)\right\}.
$$  

For a random variable $x\sim N(m,s^{2})$ , it can be shown (see Appendix B) that  
$$
\operatorname{E}[e^{-k x}]=e^{-k m+{\frac{1}{2}}k^{2}s^{2}}
$$  

for any constant $k$ . In particular,  
$$
\mathrm{E}[e^{-\gamma x}]=e^{-\gamma m+\frac{1}{2}\gamma^{2}s^{2}}
$$  

and  
$$
{\begin{array}{r l}&{\operatorname{Var}[e^{-\gamma x}]=\operatorname{E}[(e^{-\gamma x})^{2}]-\left(\operatorname{E}[e^{-\gamma x}]\right)^{2}=\operatorname{E}[e^{-2\gamma x}]-\left(e^{-\gamma m+{\frac{1}{2}}\gamma^{2}s^{2}}\right)^{2}}\ &{\qquad=e^{-2\gamma m+2\gamma^{2}s^{2}}-\left(e^{-\gamma m+{\frac{1}{2}}\gamma^{2}s^{2}}\right)^{2}=\left(e^{-\gamma m+{\frac{1}{2}}\gamma^{2}s^{2}}\right)^{2}\left[e^{\gamma^{2}s^{2}}-1\right].}\end{array}}
$$  

In our case, we get  
$$
\operatorname{E}\left[{\frac{u^{\prime}(c)}{u^{\prime}(c_{0})}}\right]=\operatorname{E}\left[\exp\left\{-\gamma\ln\left({\frac{c}{c_{0}}}\right)\right\}\right]=\exp\left\{-\gamma{\bar{g}}+{\frac{1}{2}}\gamma^{2}\sigma_{g}^{2}\right\}
$$  

and  
$$
\frac{\sigma\left[u^{\prime}(c)/u^{\prime}(c_{0})\right]}{\operatorname{E}\left[u^{\prime}(c)/u^{\prime}(c_{0})\right]}=\sqrt{e^{\gamma^{2}\sigma_{g}^{2}}-1}\approx\gamma\sigma_{g},
$$  

where the approximation is based on $e^{x}\approx1+x$ for $x\approx0$ . The gross [risk-free rate of return](../../../Financial%20Instruments/Financial%20Instruments.md) is then given by.  
$$
R^{f}=e^{\delta}\left(\operatorname{E}\left[(c/c_{0})^{-\gamma}\right]\right)^{-1}=\exp\left\{\delta+\gamma{\bar{g}}-{\frac{1}{2}}\gamma^{2}\sigma_{g}^{2}\right\}
$$  

so that the continuously compounded [risk-free rate of return](../../../Financial%20Instruments/Financial%20Instruments.md) becomes  
$$
\ln R^{f}=\delta+\gamma\bar{g}-\frac{1}{2}\gamma^{2}\sigma_{g}^{2}.
$$  

From (8.2) and (8.7) we conclude that in the simple model the excess expected rate of return on a risky asset is  
$$
\begin{array}{r}{\mathrm{E}[R_{i}]-R^{f}\approx-\gamma\sigma_{g}\rho\left[R_{i},(c/c_{0})^{-\gamma}\right]\sigma[R_{i}].}\end{array}
$$  

A first-order [Taylor approximation](../../Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%207/Profit%20and%20Loss%20Attribution%20with%20an%20OAS.md) of the function $f(x)=x^{-\gamma}$ around $^{1}$ gives $f(x)\approx f(1)+$ $f^{\prime}(1)(x-1)=1-\gamma(x-1)$ and with $x=c/c_{0}$ we get  
$$
\left(\frac{c}{c_{0}}\right)^{-\gamma}\approx1-\gamma\left(\frac{c}{c_{0}}-1\right)
$$  

and, consequently,  
$$
\begin{array}{r l}&{\rho\left[R_{i},\left(\frac{c}{c_{0}}\right)^{-\gamma}\right]\approx\rho\left[R_{i},1-\gamma\left(\frac{c}{c_{0}}-1\right)\right]=\frac{\operatorname{Cov}\left[R_{i},1-\gamma\left(\frac{c}{c_{0}}-1\right)\right]}{\sigma\left[R_{i}\right]\sigma\left[1-\gamma\left(\frac{c}{c_{0}}-1\right)\right]}}\ &{\qquad=\frac{-\gamma\operatorname{Cov}\left[R_{i},c/c_{0}\right]}{\sigma\left[R_{i}\right]\gamma\sigma\left[c/c_{0}\right]}=-\rho[R_{i},c/c_{0}].}\end{array}
$$  

Therefore,  
$$
\begin{array}{r}{\mathrm{E}[R_{i}]-R^{f}\approx\gamma\sigma_{g}\rho[R_{i},c/c_{0}]\sigma[R_{i}],}\end{array}
$$  

as in (8.3).  

# 8.2.3 The simple one-period CCAPM: version 3  

Assume that the individual has constant [relative risk aversion](CCAPM%20with%20Alternative%20Preferences.md) and that the gross asset return $R_{i}$ and the [consumption growth](Long-Run%20Risks%20and%20Epstein-Zin%20Utility.md) $c/c_{0}$ are jointly lognormally distributed (a stronger condition than in version 2). Then the [state-price deflator](Exercises.md) $\zeta=e^{-\delta}(c/c_{0})^{-\gamma}$ is also lognormally distributed. It now follows from the analysis in Section 4.2.1 that the continuously compounded [risk-free rate of return](../../../Financial%20Instruments/Financial%20Instruments.md) is  
${\mathrm{\Delta}}^{,}=\ln{R}^{f}=-\operatorname{E}[\ln\zeta]-{\frac{1}{2}}\operatorname{Var}[\ln\zeta]=\delta+\gamma\operatorname{E}\left[\ln\left({\frac{c}{c_{0}}}\right)\right]-{\frac{1}{2}}\gamma^{2}\operatorname{Var}\left[\ln\left({\frac{c}{c_{0}}}\right)\right]=\delta+\gamma\bar{g}-{\frac{1}{2}}\gamma^{2}\sigma_{g}^{2},$ as in version 2 above. The expectation of the [continuously compounded rate](../../../Financial%20Instruments/Financial%20Derivatives%20and%20Quantitative%20Methods/Arithmetic%20and%20Geometric%20Rates%20of%20Return.md) of return $r_{i}=\ln R_{i}$ of asset $i$ satisfies  
$$
\begin{array}{l}{{\displaystyle\mathrm{E}[r_{i}]-r^{f}=-\mathrm{Cov}[\ln\zeta,r_{i}]-\frac{1}{2}\mathrm{Var}[r_{i}]}}\ {~}\ {{\displaystyle~=\gamma\mathrm{Cov}\left[r_{i},\ln\left(\frac{c}{c_{0}}\right)\right]=\gamma\sigma_{g}\rho[r_{i},\ln(c/c_{0})]\sigma[r_{i}]}.}\end{array}
$$  

This relation is exact but holds only under the more restrictive assumption of joint lognormality of [consumption and returns](General%20Multi-Period%20Link%20Between%20Consumption%20a.md).  

# 8.2.4 The consumption-mimicking portfolio  

In both versions 1 and 2 above, expected excess [returns](../Chapter%203%20-%20%20Assets,%20Portfolios,%20and%20Arbitrage/Assets.md) are determined by the beta of the asset with the growth rate of consumption via the equation $\begin{array}{r}{\mathrm{E}[R_{i}]\approx R^{f}+\beta[R_{i},g]\eta}\end{array}$ , cf. (8.4).We will now show that we can replace the [consumption growth](Long-Run%20Risks%20and%20Epstein-Zin%20Utility.md) by the return $R^{c}$ on a [portfolio](../../../Advanced%20Investments/An%20Asset%20Allocation%20Primer.md) $\pi^{c}$ mimicking the [consumption growth](Long-Run%20Risks%20and%20Epstein-Zin%20Utility.md) in the sense that $\pi^{c}$ is the [portfolio](../../../Advanced%20Investments/An%20Asset%20Allocation%20Primer.md) minimizing the variance of the difference between the [portfolio](../../../Advanced%20Investments/An%20Asset%20Allocation%20Primer.md) return and the [consumption growth](Long-Run%20Risks%20and%20Epstein-Zin%20Utility.md). A [portfolio](../../../Advanced%20Investments/An%20Asset%20Allocation%20Primer.md) characterized by the [portfolio weight vector](../Chapter%203%20-%20%20Assets,%20Portfolios,%20and%20Arbitrage/Portfolios%20and%20Trading%20Strategies.md) $\pi$ has a return of $R^{\pi}=\pi^{\top}R$ , where $\kappa$ is the vector of [returns](../Chapter%203%20-%20%20Assets,%20Portfolios,%20and%20Arbitrage/Assets.md) of the individual assets. The variance we seek to minimize is  
$$
\mathrm{Var}\left[R^{\pi}-g\right]=\pi^{\top}\mathrm{Var}[R]\pi+\mathrm{Var}[g]-2\pi^{\top}\mathrm{Cov}[R,g].
$$  

Here $\mathrm{Var}[R]$ is the variance-covariance matrix of the [returns](../Chapter%203%20-%20%20Assets,%20Portfolios,%20and%20Arbitrage/Assets.md) and. $\operatorname{Cov}[R,g]$ is the vector of the covariances of each assets return with [consumption growth](Long-Run%20Risks%20and%20Epstein-Zin%20Utility.md). The first-order condition determining the [consumption growth](Long-Run%20Risks%20and%20Epstein-Zin%20Utility.md) mimicking [portfolio](../../../Advanced%20Investments/An%20Asset%20Allocation%20Primer.md). $\pi=\pi^{c}$ is  
$$
2\operatorname{Var}[R]\pi^{c}-2\operatorname{Cov}[R,g]=0\quad\Leftrightarrow\quad\pi^{c}=\left(\operatorname{Var}[R]\right)^{-1}\operatorname{Cov}[R,g],
$$  

so that the return on that [portfolio](../../../Advanced%20Investments/An%20Asset%20Allocation%20Primer.md) is  
$$
R^{c}=(\pi^{c})^{\top}R=(\operatorname{Cov}[R,g])^{\top}(\operatorname{Var}[R])^{-1}R.
$$  

The variance of the return is  
$$
\mathrm{Var}[R^{c}]=\left(\mathrm{Cov}[R,g]\right)^{\top}\left(\mathrm{Var}[R]\right)^{-1}\mathrm{Cov}[R,g],
$$  

which implies that  
$$
\operatorname{Cov}[R^{c},g]=(\operatorname{Cov}[\pmb{R},g])^{\top}\left(\operatorname{Var}[\pmb{R}]\right)^{-1}\operatorname{Cov}[\pmb{R},g]=\operatorname{Var}[R^{c}].
$$  

Also observe that  
$$
\mathrm{Cov}[R,R^{c}]=\mathrm{Cov}[R,g].
$$  

The equation (8.4) holds for all assets and portfolios. In particular, it must hold for the consumption-mimicking [portfolio](../../../Advanced%20Investments/An%20Asset%20Allocation%20Primer.md) so that  
$$
\operatorname{E}[R^{c}]-R^{f}\approx\beta[R^{c},g]\eta={\frac{\operatorname{Cov}[R^{c},g]}{\operatorname{Var}[g]}}\eta={\frac{\operatorname{Var}[R^{c}]}{\operatorname{Var}[g]}}\eta,
$$  

where the last equality follows from (8.13). Solving for $\eta$ in the above equation, we find.  
$$
\eta\approx{\frac{\operatorname{Var}[g]}{\operatorname{Var}[R^{c}]}}\left(\operatorname{E}[R^{c}]-R^{f}\right).
$$  

Hence the [expected excess return](../Chapter%209%20-%20Factor%20Models/Theoretical%20Factors.md) on any risky asset $i$ can be rewritten as  
$$
\operatorname{E}[R_{i}]-R^{f}\approx{\frac{\operatorname{Cov}[R_{i},g]}{\operatorname{Var}[g]}}{\frac{\operatorname{Var}[g]}{\operatorname{Var}[R^{c}]}}\left(\operatorname{E}[R^{c}]-R^{f}\right)={\frac{\operatorname{Cov}[R_{i},g]}{\operatorname{Var}[R^{c}]}}\left(\operatorname{E}[R^{c}]-R^{f}\right).
$$  

Applying (8.14), we conclude that  
$$
\begin{array}{r}{\operatorname{E}[R_{i}]-R^{f}\approx\beta[R_{i},R^{c}]\left(\operatorname{E}[R^{c}]-R^{f}\right),}\end{array}
$$  

where $\beta[R_{i},R^{c}]=\operatorname{Cov}[R_{i},R^{c}]/\operatorname{Var}[R^{c}]$ . Equation (8.15) is exactly as the classic CAPM but with.   
the return on a consumption-mimicking [portfolio](../../../Advanced%20Investments/An%20Asset%20Allocation%20Primer.md) instead of the return on the market [portfolio](../../../Advanced%20Investments/An%20Asset%20Allocation%20Primer.md).  

The consumption-mimicking [portfolio](../../../Advanced%20Investments/An%20Asset%20Allocation%20Primer.md) has the property that its return has the highest absolute correlation with [consumption growth](Long-Run%20Risks%20and%20Epstein-Zin%20Utility.md). In order to see this, note that  
$$
\left(\operatorname{Corr}[R^{\pi},g]\right)^{2}={\frac{\left(\operatorname{Cov}[R^{\pi},g]\right)^{2}}{\operatorname{Var}[R^{\pi}]\operatorname{Var}[g]}}={\frac{\left(\pi^{\top}\operatorname{Cov}[R,g]\right)^{2}}{\pi^{\top}\operatorname{Var}[R]\pi\operatorname{Var}[g]}}.
$$  

The first-order condition for the minimization implies that  
$$
2\pi^{\top}\operatorname{Cov}[R,g]\operatorname{Cov}[R,g]\left(\pi^{\top}\operatorname{Var}[R]\pi\operatorname{Var}[g]\right)-\left(\pi^{\top}\operatorname{Cov}[R,g]\right)^{2}2\operatorname{Var}[R]\pi\operatorname{Var}[g]=0.
$$  

Simplification leads to  
$$
\operatorname{Cov}[R,g]\pi^{\top}\operatorname{Var}[R]\pi=\pi^{\top}\operatorname{Cov}[R,g]\operatorname{Var}[R]\pi.
$$  

We know from (8.12) that the consumption-mimicking [portfolio](../../../Advanced%20Investments/An%20Asset%20Allocation%20Primer.md) satisfies. $\operatorname{Var}[R]\pi=\operatorname{Cov}[R,g]$ and substituting that into the above equation, we see that the consumption-mimicking [portfolio](../../../Advanced%20Investments/An%20Asset%20Allocation%20Primer.md) also satisfies the first-order condition for the correlation maximization problem..  
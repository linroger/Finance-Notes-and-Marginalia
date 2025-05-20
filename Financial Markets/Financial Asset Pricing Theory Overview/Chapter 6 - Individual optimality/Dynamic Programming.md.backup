---
tags:
  - asset_pricing
  - consumption
  - dynamic_programming
  - state_prices
  - utility_maximization
aliases:
  - DP
  - Indirect Utility
  - Optimal Consumption
key_concepts:
  - Consumption-based asset pricing
  - Discrete-time framework
  - Envelope condition
  - Indirect utility function
  - Optimal consumption plan
---

# 6.5 Dynamic programming  

Above we have linked the [optimal consumption plan](../Chapter%209%20-%20Factor%20Models/Theoretical%20Factors.md) of an individual to asset prices. In Chapter 8 we will see how this leads to [consumption-based asset pricing](../Chapter%209%20-%20Factor%20Models/The%20Classical%20One-Period%20Capm.md) models. While this link is quite intuitive and theoretically elegant, empirical tests and practical applications of the model suffer from the fact that available data on individual or [aggregate consumption](../Chapter%207%20-%20Market%20equilibrium/Pareto-Optimality%20in%20Some%20Incomplete%20Markets.md) are of poor quality. For that purpose it is tempting to link asset prices to other variables for which better data are available. One way to provide such a link is to explain [optimal consumption](.md) in terms of other variables. If $c_{t}$ is a function of some variable, say. $x_{t}$ , then the equations in this chapter proves a link between. asset prices and $x$ . To figure out what explains the consumption choice of an individual we have. to dig deeper into the [utility maximization problem](../Chapter%204%20-%20State%20Prices/Properties%20of%20State-Price%20Deflators.md)..  

We will consider both a discrete-time and a [continuous-time framework](Exercises.md). In both cases we will for. simplicity assume [time-additive expected utility](../Chapter%208%20-%20Consumption-Based%20Asset%20Pricing/General%20Multi-Period%20Link%20Between%20Consumption%20a.md). A central element of the analysis is the [indirect utility function](.md) of the individual, which is defined as the maximum expected utility of current and future consumption. In the discrete-time case the [indirect utility](Epstein-Zin%20Recursive%20Utility.md) at time. $t$ is defined as  
$$
J_{t}=\operatorname*{sup}_{(c_{s},\theta_{s})_{s=t}^{T}}\mathrm{E}_{t}\left[\sum_{s=t}^{T}e^{-\delta(s-t)}u(c_{s})\right].
$$  

There is no [portfolio](../../../Advanced%20Investments/An%20Asset%20Allocation%20Primer.md) chosen at the final date so it is understood that $\pmb{\theta}_{T}=\mathbf{0}$ . Consumption at the final date is equal to the time. $T$ value of the [portfolio](../../../Advanced%20Investments/An%20Asset%20Allocation%20Primer.md) purchased at. $T-1$ . In continuous time the. corresponding definition is  
$$
J_{t}=\operatorname*{sup}_{(c_{s},\theta_{s})_{s\in[t,T]}}\operatorname{E}_{t}\left[\int_{t}^{T}e^{-\delta(s-t)}u(c_{s})d s\right].
$$  

For tractability it is necessary to assume that the [indirect utility](Epstein-Zin%20Recursive%20Utility.md) is a function of a limited number of variables. Surely the [indirect utility](Epstein-Zin%20Recursive%20Utility.md) of a finitely-lived individual will depend on the length of the remaining life and therefore on calender time $t$ .The [indirect utility](Epstein-Zin%20Recursive%20Utility.md) at a given time. $t$ will also depend on the wealth. $W_{t}$ of the individual at that point in time. Other variables containing. information about current or future [investment](../../../Advanced%20Investments/An%20Asset%20Allocation%20Primer.md) opportunities or current or future income may have. to be added. Suppose that that extra information can be captured by a single variable. $x_{t}$ . In that case the [indirect utility](Epstein-Zin%20Recursive%20Utility.md) is of the form.  
$$
J_{t}=J(W_{t},x_{t},t)
$$  

for some function $J$  

We will show below that both in discrete and in continuous time the [optimal consumption](.md) strategy will satisfy the so-called [envelope condition](.md):.  
$$
u^{\prime}(c_{t})=J_{W}(W_{t},x_{t},t),
$$  

where $J_{W}$ is the partial derivative of $J$ with respect to $W$ . This is an intuitive optimality condition.. The left-hand side is the marginal utility of an extra unit of consumption at time $t$ . The right-hand side is the marginal utility from investing an extra unit at time. $t$ in the optimal way. In an optimum. these marginal utilities have to be equal. If that was not the case the allocation of wealth between consumption and [investment](../../../Advanced%20Investments/An%20Asset%20Allocation%20Primer.md) should be reconsidered. For example, if. $u^{\prime}(c_{t})>J_{W}(W_{t},x_{t},t)$ , the consumption $c_{t}$ should be increased and the amount invested should be decreased. Using the [envelope condition](.md), the [state-price deflator](Exercises.md) derived from the individual's optimization problem can be rewritten as  
$$
\zeta_{t}=e^{-\delta t}\frac{u^{\prime}(c_{t})}{u^{\prime}(c_{0})}=e^{-\delta t}\frac{J_{W}(W_{t},x_{t},t)}{J_{W}(W_{0},x_{0},0)},
$$  

which links state prices to the optimally invested wealth of the individual and the variable $x_{t}$ .This will be useful in constructing factor models in Chapter 9.  

We will derive (6.47) using the dynamic programming technique. Along the way we will also find. interesting conclusions on the optimal trading strategy of the individual. We do not make specific assumptions on utility functions or the dynamics of asset prices but stick to a general setting.. More details and a lot of specific models are discussed in Munk (2008). The basic references for the [discrete-time models](../../../Financial%20Engineering/Financial%20Mathematics%20Course.md) are Samuelson (1969), Hakansson (1970), Fama (1970, 1976), and. Ingersoll (1987, Ch. 11). The basic references for the [continuous-time models](../../../Financial%20Engineering/Financial%20Mathematics%20Course.md) are [Merton](../../../Credit%20Markets/Credit%20Markets%20Session%205.md) (1969, 1971, 1973b).  

# 6.5.1 The discrete-time framework  

Assume that a risk-free and $d$ risky assets are traded. Let $\pmb{\theta}_{t}$ denote the $d$ -vector of units invested. in the risky assets at time. $t$ and let $\theta_{0t}$ denote the units of the [risk-free asset](../../../Financial%20Engineering/2.%20Forwards,%20Swaps,%20Futures,%20and%20Options.md). Assume for simplicity  

that the assets do not pay intermediate dividends. Similar to (3.10) the change in the wealth of the individual between time $t$ and time $t+1$  
$$
W_{t+1}-W_{t}=\sum_{i=0}^{d}\theta_{i t}\left(P_{i,t+1}-P_{i t}\right)+y_{t}-c_{t},
$$  

where $y_{t}$ denotes the income received at time $t$ . After receiving income and consuming at time $t$ the funds invested will be $W_{t}+y_{t}-c_{t}$ . Assuming this is non-negative, we can represent the [portfolio](../../../Advanced%20Investments/An%20Asset%20Allocation%20Primer.md) in terms of the fractions of this total [investment](../../../Advanced%20Investments/An%20Asset%20Allocation%20Primer.md) invested in the different assets, i.e.  
$$
\pi_{i t}=\frac{\theta_{i t}P_{i t}}{W_{t}+y_{t}-c_{t}},\quad i=0,1,\ldots,d.
$$  

Define the [portfolio weight vector](../Chapter%203%20-%20%20Assets,%20Portfolios,%20and%20Arbitrage/Portfolios%20and%20Trading%20Strategies.md) of the risky assets by. $\pi_{t}=\left(\pi_{1t},\ldots,\pi_{d t}\right)^{\top}$ . By construction the fraction invested in the risk-fre asset is then given byd $\begin{array}{r}{\pi_{0t}=1-\sum_{i=1}^{d}\pi_{i t}=1-\pi_{t}^{\top}{\bf1}}\end{array}$ . The wealth at the end of the period can then be restated as  
$$
\boldsymbol{W}_{t+1}=(\boldsymbol{W}_{t}+\boldsymbol{y}_{t}-\boldsymbol{c}_{t})\boldsymbol{R}_{t+1}^{W},
$$  

where  
$$
R_{t+1}^{W}=1+r_{t}^{f}+\pi_{t}^{\top}\left[r_{t+1}-r_{t}^{f}{\bf1}\right]
$$  

is the gross rate of return on the [portfolio](../../../Advanced%20Investments/An%20Asset%20Allocation%20Primer.md), $\boldsymbol{r}_{t}^{f}$ is the risk-free [net rate of return](../Chapter%203%20-%20%20Assets,%20Portfolios,%20and%20Arbitrage/Assets.md), and $r_{t+1}$ is the $d$ -vector of the net rates of return of the risky assets over the period. Note that the only random variable (seen from time $t$ ) on the right-hand side of the above expressions is the return vector It+1:  

In the definition of [indirect utility](Epstein-Zin%20Recursive%20Utility.md) in (6.45) the maximization is over both the current and all. future consumption rates and portfolios. This is clearly a quite complicated maximization problem. We will now show that we can alternatively perform a sequence of simpler maximization problems. This result is based on the following manipulations:.  
$$
\begin{array}{r l}{J_{t}=}&{\underset{(c,e,n,s)_{\mathrm{ret}}^{\prime}}{\operatorname*{sup}}\mathbb{E}_{t}\left[\displaystyle\sum_{s=t}^{T}e^{-\delta(s-t)}u(c_{s})\right]}\ {=}&{\underset{(c,e,s)_{\mathrm{ret}}^{\prime}}{\operatorname*{sup}}\mathbb{E}_{t}\left[u(c_{t})+\displaystyle\sum_{s=t+1}^{T}e^{-\delta(s-t)}u(c_{s})\right]}\ &{=\underset{(c,e,s)_{\mathrm{ret}}^{\prime}}{\operatorname*{sup}}\mathbb{E}_{t}\left[u(c_{t})+\mathbb{E}_{t+1}\left[\displaystyle\sum_{s=t+1}^{T}e^{-\delta(s-t)}u(c_{s})\right]\right]}\ &{=\underset{(c,e,s)_{\mathrm{ret}}^{\prime}}{\operatorname*{sup}}\mathbb{E}_{t}\left[u(c_{t})+e^{-\delta}\mathbb{E}_{t+1}\left[\displaystyle\sum_{s=t+1}^{T}e^{-\delta(s-t)}u(c_{s})\right]\right]}\ &{=\underset{(c,e,s)_{\mathrm{ret}}^{\prime}}{\operatorname*{sup}}\mathbb{E}_{t}\left[u(c_{t})+e^{-\delta}\mathbb{E}_{t+1}\left[\displaystyle\sum_{s=t+1}^{T}e^{-\delta(s-(t+1))}u(c_{s})\right]\right]}\ &{=\underset{c,e,n}{\operatorname*{sup}}\mathbb{E}_{t}\left[u(c_{t})+e^{-\delta}\underbrace{\operatorname*{sup}}_{(c,e,n,\xi_{\mathrm{ret}}^{\prime})}+E_{t+1}\left[\displaystyle\sum_{s=t+1}^{T}e^{-\delta(s-(t+1))}u(c_{s})\right]\right]}\ &{=\underset{c,e,n}{\operatorname*{sup}}\mathbb{E}_{t}\left[u(c_{t})+e^{-\delta}\underbrace{\operatorname*{sup}}_{(c,e,n,\xi_{\mathrm{ret}}^{\prime})}+1\right].}\end{array}
$$  

Here, the first equality is simply due to the definition of [indirect utility](Epstein-Zin%20Recursive%20Utility.md), the second equality comes from separating out the first term of the sum, the third equality is valid according to the [law of iterated expectations](../Chapter%2011%20-%20Risk-adjusted%20probabilities/General%20Risk-Adjusted%20Probability%20Measures.md), the fourth equality comes from separating out the discount term $e^{-\delta}$ , and the final equality is due to the fact the only the inner expectation depends on future consumption rates and portfolios. Noting that the inner supremum is by definition the [indirect utility](Epstein-Zin%20Recursive%20Utility.md) at time $t+1$ we arrive at  
$$
J_{t}=\operatorname*{sup}_{c_{t},\pi_{t}}\mathrm{E}_{t}\left[u(c_{t})+e^{-\delta}J_{t+1}\right]=\operatorname*{sup}_{c_{t},\pi_{t}}\left\{u(c_{t})+e^{-\delta}\mathrm{E}_{t}\left[J_{t+1}\right]\right\}.
$$  

This equation is called the Bellman equation, and the [indirect utility](Epstein-Zin%20Recursive%20Utility.md) $J$ is said to have the dynamic programming property. The decision to be taken at time $t$ is split up in two: (1) the consumption and [portfolio](../../../Advanced%20Investments/An%20Asset%20Allocation%20Primer.md) decision for the current period and (2) the consumption and [portfolio](../../../Advanced%20Investments/An%20Asset%20Allocation%20Primer.md) decisions for all future periods. We take the decision for the current period assuming that we will make optimal decisions in all future periods. Note that this does not imply that the decision for the current period is taken independently from future decisions. We take into account the effect that our current decision has on the maximum expected utility we can get from all future periods. The expectation $\operatorname{E}_{t}\left[J_{t+1}\right]$ will depend on our choice of $c_{t}$ and $\pi_{t}$ 2.  

The dynamic programming property is the basis for a backward iterative solution procedi First, note that $J_{T}=u(c_{T})=u(W_{T})$ , and $c_{T-1}$ and $\pi_{T-1}$ are chosen to maximize  
$$
u(c_{T-1})+e^{-\delta}\operatorname{E}_{T-1}\left[u(W_{T})\right],
$$  

where  
$$
W_{T}=\left(W_{T-1}+y_{T-1}-c_{T-1}\right)R_{T}^{W},\quad R_{T}^{W}=1+r_{T-1}^{f}+\pi_{T-1}^{\top}\left[r_{T}-r_{T-1}^{f}{\bf1}\right].
$$  

This is done for each possible scenario at time $T-1$ and gives us ${\mathcal{I}}_{T-1}$ . Then $c_{T-2}$ and $\pi_{T-2}$ are chosen to maximize  
$$
u\left(c_{T-2}\right)+e^{-\delta}\operatorname{E}_{T-2}\left[J_{T-1}\right],
$$  

and so on until time zero is reached. Since we have to perform a maximization for each scenario of the world at every point in time, we have to make assumptions on the possible scenarios at. each point in time before we can implement the recursive procedure. The optimal decisions at any. time are expected to depend on the wealth level of the agent at that date, but also on the value of. other time-varying state variables that affect future [returns](../Chapter%203%20-%20%20Assets,%20Portfolios,%20and%20Arbitrage/Assets.md) on [investment](../../../Advanced%20Investments/An%20Asset%20Allocation%20Primer.md) (e.g. the interest rate level) and future income levels. To be practically implementable only a few state variables can be incorporated. Also, these state variables must follow Markov processes so only the current values of the variables are relevant for the maximization at a given point in time..  

Suppose that the relevant information is captured by a one-dimensional [Markov process](../../Financial%20Trading%20and%20Markets/Chapter%207%20Random%20Walks%20Risk%20and%20Arbitrage.md) $x=\left(x_{t}\right)$ so that the [indirect utility](Epstein-Zin%20Recursive%20Utility.md) at any time. $t=0,1,\dots,T$ can be written as $J_{t}=J(W_{t},x_{t},t)$ .Then the dynamic programming equation (6.52) becomes  
$$
J(W_{t},x_{t},t)=\operatorname*{sup}_{c_{t},\pi_{t}}\left\{u(c_{t})+e^{-\delta}\mathrm{E}_{t}\left[J(W_{t+1},x_{t+1},t+1)\right]\right\}
$$  

with terminal condition $J(W_{T},x_{T},T)=u(W_{T})$ . Doing the maximization we have to remember that $W_{t+1}$ will be affected by the choice of. $c_{t}$ and $\pi_{t}$ , cf. Equation (6.50). In particular, we see that  
$$
\frac{\partial W_{t+1}}{\partial c_{t}}=-R_{t+1}^{W},\qquad\frac{\partial W_{t+1}}{\partial\pi_{t}}=\left(W_{t}+y_{t}-c_{t}\right)\left(r_{t+1}-r_{t}^{f}{\bf1}\right).
$$  

The first-order condition for the maximization with respect to $c_{t}$ is  

which implies that  
$$
u^{\prime}(c_{t})+e^{-\delta}\operatorname{E}_{t}\bigg[J_{W}(W_{t+1},x_{t+1},t+1)\frac{\partial W_{t+1}}{\partial c_{t}}\bigg]=0,
$$  
$$
u^{\prime}(c_{t})=e^{-\delta}\operatorname{E}_{t}\left[J_{W}(W_{t+1},x_{t+1},t+1)R_{t+1}^{W}\right].
$$  

The first-order condition for the maximization with respect to $\pi_{t}$ is  

which implies that  
$$
\mathrm{E}_{t}\left[J_{W}(W_{t+1},x_{t+1},t+1)\frac{\partial W_{t+1}}{\partial\pmb{\pi}_{t}}\right]=0,
$$  
$$
\operatorname{E}_{t}\left[J_{W}(W_{t+1},x_{t+1},t+1)\left(r_{t+1}-r_{t}^{f}1\right)\right]=0.
$$  

While we cannot generally solve for the optimal decisions, we can show that the [envelope condition](.md) (6.47) holds. First note that for the optimal choice $\hat{c}_{t},\hat{\pi}_{t}$ we have that  
$$
\begin{array}{r}{J(W_{t},x_{t},t)=u(\hat{c}_{t})+e^{-\delta}\mathrm{E}_{t}\left[J(\hat{W}_{t+1},x_{t+1},t+1)\right],}\end{array}
$$  

where $\hat{W}_{t+1}$ is next period's wealth using $\hat{c}_{t},\hat{\pi}_{t}$ . Taking [derivatives](../../Financial%20Trading%20and%20Markets/Chapter%209%20Arbitrage%20and%20Hedging%20With%20Options.md) with respect to $W_{t}$ in this equation, and acknowledging that $\hat{c}_{t}$ and $\hat{\pi}_{t}$ will in general depend on $W_{t}$ , we get  

where  
$$
J_{W}(W_{t},x_{t},t)=u^{\prime}(\hat{c}_{t})\frac{\partial\hat{c}_{t}}{\partial W_{t}}+e^{-\delta}\mathrm{E}_{t}\left[J_{W}(\hat{W}_{t+1},x_{t+1},t+1)\frac{\partial\hat{W}_{t+1}}{\partial W_{t}}\right],
$$  
$$
\frac{\partial\hat{W}_{t+1}}{\partial W_{t}}=R_{t+1}^{W}\left(1-\frac{\partial\hat{c}_{t}}{\partial W_{t}}\right)+\left(W_{t}+y_{t}-c_{t}\right)\left(\frac{\partial\hat{\pi}_{t}}{\partial W_{t}}\right)^{\top}\left(r_{t+1}-r_{t}^{f}\mathbf{1}\right).
$$  

Inserting this and rearranging terms, we get  
$$
\begin{array}{r l}&{J_{W}(W_{t},x_{t},t)=e^{-\delta}\mathrm{E}_{t}\left[J_{W}(\hat{W}_{t+1},x_{t+1},t+1)R_{t+1}^{W}\right]}\ &{\qquad+\left(u^{\prime}(\hat{c}_{t})-e^{-\delta}\mathrm{E}_{t}\left[J_{W}(\hat{W}_{t+1},x_{t+1},t+1)R_{t+1}^{W}\right]\right)\frac{\partial\hat{c}_{t}}{\partial W_{t}}}\ &{\qquad+\left(W_{t}+y_{t}-c_{t}\right)e^{-\delta}\left(\frac{\partial\hat{\pi}_{t}}{\partial W_{t}}\right)^{\top}\mathrm{E}_{t}\left[J_{W}(\hat{W}_{t+1},x_{t+1},t+1)\left(r_{t+1}-r_{t}^{f}\mathbf{1}\right)\right].}\end{array}
$$  

On the right-hand side the last two terms are zero due to the first-order conditions and only the leading term remains, i.e.  
$$
\begin{array}{r}{J_{W}(W_{t},x_{t},t)=e^{-\delta}\mathrm{E}_{t}\left[J(\hat{W}_{t+1},x_{t+1},t+1)R_{t+1}^{W}\right].}\end{array}
$$  

Combining this with (6.55) we obtain the [envelope condition](.md) (6.47).  

# 6.5.2 The continuous-time framework  

As in the discrete-time setting above assume that an instantaneously [risk-free asset](../../../Financial%20Engineering/2.%20Forwards,%20Swaps,%20Futures,%20and%20Options.md) with a continuously compounded [risk-free rate](../../../Financial%20Instruments/Black%20Scholes%20Derivation.md) of. $\boldsymbol{r}_{t}^{f}$ and $d$ risky assets are traded. We assume for simplicity. that the assets pay no intermediate dividends and write their [price dynamics](../../../Financial%20Engineering/Derivatives/Part%20XII%20-%20Price%20Dynamics/Chapter%2047%20-%20Asset%20Price%20Dynamics.md) as.  
$$
d P_{t}=\operatorname{diag}(P_{t})\left[\mu_{t}\c{d t}+\underline{{\underline{{\sigma}}}}{}_{t}\:d z_{t}\right],
$$  

where $\boldsymbol{z}=(z_{1},\dots,z_{d})^{\top}$ is a $d$ -dimensional standard [Brownian motion](../Chapter%202%20-%20Uncertainty,%20Information,%20and%20Stochastic%20Processes/Continuous-Time%20Stochastic%20Processes.md). We can write this componentwise as  
$$
d P_{i t}=P_{i t}\left[\mu_{i t}d t+\sum_{j=1}^{d}\sigma_{i j t}d z_{j t}\right],\quad i=1,\dots,d.
$$  

The instantaneous rate of return on asset $i$ is given by $d P_{i t}/P_{i t}$ . The $d$ vector $\pmb{\mu}_{t}=(\mu_{1t},\dots,\mu_{d t})^{\top}$ contains the expected rates of return and the $(d\times d)$ matrix $\underline{{\underline{{\sigma}}}}_{t}=(\sigma_{i j t})_{i,j=1}^{d}$ measures the sensitivities of the risky asset prices with respect to [exogenous shocks](../Chapter%202%20-%20Uncertainty,%20Information,%20and%20Stochastic%20Processes/Some%20Discrete-Time%20Stochastic%20Processes.md) so that the $(d\times d)$ matrix $\underline{{\Sigma}}_{t}=\underline{{\underline{{\sigma}}}}_{t}\underline{{\underline{{\sigma}}}}_{t}^{\top}$ contains the variance and covariance rates of instantaneous rates of return. We assume that $\underline{{\underline{{\sigma}}}}t$ is non-singular and, hence, we can define the [market price of risk](Exercises.md) associated with $_{z}$ as  
$$
\lambda_{t}=\underline{{\underline{{\sigma}}}}_{t}^{-1}(\pmb{\mu}_{t}-r_{t}^{f}\mathbf{1}),
$$  

so that  
$$
\begin{array}{r}{\pmb{\mu}_{t}=r_{t}\mathbf{1}+\underline{{\underline{{\sigma}}}}_{t}\pmb{\lambda}_{t},}\end{array}
$$  

i.e. $\begin{array}{r}{\mu_{i t}=r_{t}+\sum_{j=1}^{d}\sigma_{i j t}\lambda_{j t}}\end{array}$ . We can now rewrite the [price dynamics](../../../Financial%20Engineering/Derivatives/Part%20XII%20-%20Price%20Dynamics/Chapter%2047%20-%20Asset%20Price%20Dynamics.md) as  
$$
d P_{t}=\operatorname{diag}(P_{t})\left[\left(r_{t}\mathbf{1}+\underline{{\underline{{\sigma}}}}_{t}\lambda_{t}\right)\mathbf{\delta}d t+\underline{{\underline{{\sigma}}}}_{t}\mathbf{\delta}d z_{t}\right].
$$  

We represent the trading strategy by the [portfolio](../../../Advanced%20Investments/An%20Asset%20Allocation%20Primer.md) weight process $\pi=\left(\pi_{t}\right)$ , where $\pi_{t}$ is the. $d$ -vector of fractions of wealth invested in the $d$ risky assets at time $t$ .Again the weight of the [risk-free asset](../../../Financial%20Engineering/2.%20Forwards,%20Swaps,%20Futures,%20and%20Options.md) is $\begin{array}{r}{\pi_{0t}=1-\pi_{t}^{\top}{\bf1}=1-\sum_{i=1}^{d}\pi_{i t}}\end{array}$ . Analogous to (3.14), the [wealth dynamics](Epstein-Zin%20Recursive%20Utility.md) can be written as.  
$$
d W_{t}=W_{t}\left[r_{t}^{f}+\pi_{t}^{\top}\underline{{\sigma}}_{t}\lambda_{t}\right]d t+\left[y_{t}-c_{t}\right]d t+W_{t}\pi_{t}^{\top}\underline{{\sigma}}_{t}d z_{t}.
$$  

For simplicity we assume in the following that the agent receives no labor income, i.e. $y_{t}\equiv0$ .We also assume that a single variable $x_{t}$ captures the time $t$ information about [investment](../../../Advanced%20Investments/An%20Asset%20Allocation%20Primer.md) opportunities so that, in particular,  
$$
r_{t}^{f}=r^{f}(x_{t}),\quad\mu_{t}=\mu(x_{t},t),\quad\underline{{\underline{{\sigma}}}}_{t}=\underline{{\underline{{\sigma}}}}(x_{t},t),
$$  

where $r^{f}$ , and now (also) denote sufficiently well-behaved functions. The [market price of risk](Exercises.md) $\pmb{\mu}$ $\underline{{\underline{{\sigma}}}}$   
is also given by the state variable:.  
$$
\boldsymbol{\lambda}(\boldsymbol{x}_{t})=\underline{{\underline{{\sigma}}}}(\boldsymbol{x}_{t},t)^{-1}\left(\boldsymbol{\mu}(\boldsymbol{x}_{t},t)-\boldsymbol{r}^{f}(\boldsymbol{x}_{t})\mathbf{1}\right).
$$  

Note that we have assumed that the [short-term interest rate](../../Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%209/The%20Gauss%20Model.md) $\boldsymbol{r}_{t}^{f}$ and the [market price of risk](Exercises.md) vector $\lambda_{t}$ do not depend on calendar time directly. The fluctuations in $\boldsymbol{r}_{t}^{f}$ and $\lambda_{t}$ over time are presumably not due to the mere passage of time, but rather due to variations in some more fundamental economic variables. In contrast, the expected rates of [returns](../Chapter%203%20-%20%20Assets,%20Portfolios,%20and%20Arbitrage/Assets.md) and the price sensitivities of some assets will depend directly on time, e.g. the volatility and the expected rate of return on a bond. will depend on the time-to-maturity of the bond and therefore on calendar time.  

Now the [wealth dynamics](Epstein-Zin%20Recursive%20Utility.md) for a given [portfolio](../../../Advanced%20Investments/An%20Asset%20Allocation%20Primer.md) and consumption strategy is  
$$
d W_{t}=W_{t}\left[r^{f}(x_{t})+\pi_{t}^{\top}\underline{{\sigma}}(x_{t},t)\lambda(x_{t})\right]d t-c_{t}d t+W_{t}\pi_{t}^{\top}\underline{{\sigma}}(x_{t},t)d z_{t}.
$$  

The state variable $x$ is assumed to follow a one-dimensional diffusion process  
$$
d x_{t}=m(x_{t})d t+{\pmb v}(x_{t})^{\top}d z_{t}+{\hat{v}}(x_{t})d{\hat{z}}_{t},
$$  

where $\hat{z}=(\hat{z}_{t})$ is a one-dimensional standard [Brownian motion](../Chapter%202%20-%20Uncertainty,%20Information,%20and%20Stochastic%20Processes/Continuous-Time%20Stochastic%20Processes.md) independent of $z=(z_{t})$ . Hence, if $\hat{\boldsymbol v}(\boldsymbol x_{t})\neq0$ , there is an exogenous shock to the state variable that cannot be hedged by investments in the financial market. In other words, the financial market is incomplete. Conversely, if $\hat{v}(x_{t})$ is identically equal to zero, the financial market is complete. We shall consider examples of both cases later. The $d$ -vector $\pmb{v}(x_{t})$ represents the sensitivity of the state variable with respect to the [exogenous shocks](../Chapter%202%20-%20Uncertainty,%20Information,%20and%20Stochastic%20Processes/Some%20Discrete-Time%20Stochastic%20Processes.md) to market prices. Note that the. $d$ vector $\underline{{\underline{{\sigma}}}}(x,t){\pmb{v}}(x)$ is the vector of instanta-. neous covariance rates between the [returns](../Chapter%203%20-%20%20Assets,%20Portfolios,%20and%20Arbitrage/Assets.md) on the risky assets and the state variable. Under the assumptions made above the [indirect utility](Epstein-Zin%20Recursive%20Utility.md) at time $t$ is $J_{t}=J(W_{t},x_{t},t)$  

How do we implement the dynamic programming principle in continuous time? First consider a discrete-time approximation with time set $\{0,\Delta t,2\Delta t,\ldots,T=N\Delta t\}$ . The Bellman equation corresponding to this discrete-time [utility maximization problem](../Chapter%204%20-%20State%20Prices/Properties%20of%20State-Price%20Deflators.md) is  
$$
J(W,x,t)=\operatorname*{sup}_{c_{t}\geq0,\pi_{t}\in\mathbb{R}^{d}}\left\{u(c_{t})\Delta t+e^{-\delta\Delta t}\operatorname{E}_{t}\left[J(W_{t+\Delta t},x_{t+\Delta t},t+\Delta t)\right]\right\},
$$  

cf. (6.52). Here $c_{t}$ and $\pi_{t}$ are held fixed over the interval $[t,t+\Delta t)$ . If we multiply by $e^{\delta\Delta t}$ , subtract $J(W,x,t)$ , and then divide by. $\Delta t$ , we get  
$$
\frac{e^{\delta\Delta t}-1}{\Delta t}J(W,x,t)=\operatorname*{sup}_{c_{t}\geq0,\pi_{t}\in\mathbb{R}^{d}}\left\{e^{\delta\Delta t}u(c_{t})+\frac{1}{\Delta t}{\ensuremath{\mathrm{E}}}_{t}\left[J(W_{t+\Delta t},x_{t+\Delta t},t+\Delta t)-J(W,x,t)\right]\right\}.
$$  

When we let. $\Delta t\rightarrow0$ , we have that (by l'Hospital's rule)  
$$
\frac{e^{\delta\Delta t}-1}{\Delta t}\rightarrow\delta,
$$  

and that (by definition of the drift of a process)  
$$
\frac{1}{\Delta t}\operatorname{E}_{t}\left[J(W_{t+\Delta t},x_{t+\Delta t},t+\Delta t)-J(W,x,t)\right]
$$  

will approach the drift of $J$ at time $t$ , which according to [Ito's Lemma](../../../Financial%20Engineering/Determining%20the%20Stochastic%20Process%20for%20a%20Forward%20Contract%20from%20Ito’s%20Lemma.md) is given by  
$$
\begin{array}{l}{\displaystyle\frac{\partial J}{\partial t}(W,x,t)+J_{W}(W,x,t)\left(W\left[r(x)+\pi_{t}^{\top}\underline{{\sigma}}(x,t)\lambda(x)\right]-c_{t}\right)}\ {\displaystyle+\frac{1}{2}J_{W W}(W,x,t)W^{2}\pi_{t}^{\top}\underline{{\sigma}}(x,t)\underline{{\sigma}}(x,t)^{\top}\pi_{t}+J_{x}(W,x,t)m(x)}\ {\displaystyle+\frac{1}{2}J_{x x}(W,x,t)(v(x)^{\top}v(x)+\hat{v}(x)^{2})+J_{W x}(W,x,t)W\pi_{t}^{\top}\underline{{\sigma}}(x,t)v(x).}\end{array}
$$  

The limit of (6.61) is therefore  
$$
\begin{array}{r l}&{\delta J(W,x,t)=\underset{c\geq0,\pi\in\mathbb{R}^{d}}{\operatorname*{sup}}\bigg\{u(c)+\frac{\partial J}{\partial t}(W,x,t)+J_{W}(W,x,t)\left(W\left[r(x)+\pi^{\top}\underline{{\sigma}}(x,t)\lambda(x)\right]-c\right)}\ &{\qquad+\frac{1}{2}J_{W W}(W,x,t)W^{2}\pi^{\top}\underline{{\sigma}}(x,t)\underline{{\sigma}}(x,t)^{\top}\pi+J_{x}(W,x,t)m(x)}\ &{\qquad+\frac{1}{2}J_{x x}(W,x,t)(v(x)^{\top}v(x)+\hat{v}(x)^{2})}\ &{\qquad+J_{W x}(W,x,t)W\pi^{\top}\underline{{\sigma}}(x,t)v(x)\bigg\}.}\end{array}
$$  

This is called the Hamilton-Jacobi-Bellman (HJB) equation corresponding to the dynamic optimization problem. Subscripts on. $J$ denote partial [derivatives](../../Financial%20Trading%20and%20Markets/Chapter%209%20Arbitrage%20and%20Hedging%20With%20Options.md), however we will write the partial. derivative with respect to time as. $\partial J/\partial t$ to distinguish it from the value. $J_{t}$ of the [indirect utility](Epstein-Zin%20Recursive%20Utility.md).  

process. The HJB equation involves the supremum over the feasible time. $t$ consumption rates and portfolios (not the supremum over the entire processes!) and is therefore a highly non-linear second-order partial differential equation..  

From the analysis above we will expect that the [indirect utility function](.md). $J(W,x,t)$ solves the HJB equation for all possible values of $W$ and $x$ and all $t\in[0,T)$ and that it satisfies the terminal condition $J(W,x,T)=0$ . (We could allow for some utility of terminal consumption or wealth, e.g. representing the utility of leaving money for your heirs. Then the terminal condition should be of the form $J(W,x,T)=\Bar{u}(W)$ .) This can be supported formally by the so-called verification theorem. The solution procedure is therefore as follows: (1) solve the maximization problem embedded in the HJB-equation giving a candidate for the optimal strategies expressed in terms of the yet unknown. [indirect utility function](.md) and its [derivatives](../../Financial%20Trading%20and%20Markets/Chapter%209%20Arbitrage%20and%20Hedging%20With%20Options.md). (2) substitute the candidate for the optimal strategies into the HJB-equation, ignore the sup-operator, and solve the resulting partial differential equation for $J(W,x,t)$ . Such a solution will then also give the candidate optimal strategies in terms of. $W$ x, and t.3  

Let us find the first-order conditions of the maximization in (6.63). The first-order condition with respect to $c$ gives us immediately the [envelope condition](.md) (6.47), which we were really looking. for. Nevertheless, let us also look at the first-order condition with respect to. $\pi$ , i.e.  
$$
J_{W}(W,x,t)W_{\underline{{\sigma}}}(x,t)\lambda(x)+J_{W W}(W,x,t)W^{2}\underline{{\sigma}}(x,t)\underline{{\sigma}}(x,t)^{\top}\pi+J_{W x}(W,x,t)W\underline{{\sigma}}(x,t)v(x)=0
$$  

so that the optimal [portfolio](../../../Advanced%20Investments/An%20Asset%20Allocation%20Primer.md) is  
$$
\pi_{t}=-\frac{J_{W}(W_{t},x_{t},t)}{W_{t}J_{W W}(W_{t},x_{t},t)}\left(\underline{{\underline{{\sigma}}}}(x_{t},t)^{\top}\right)^{-1}\lambda(x_{t})-\frac{J_{W x}(W_{t},x_{t},t)}{W_{t}J_{W W}(W_{t},x_{t},t)}\left(\underline{{\underline{{\sigma}}}}(x_{t},t)^{\top}\right)^{-1}v(x_{t}).
$$  

As the horizon shrinks, the [indirect utility function](.md) $J(W,x,t)$ approaches the terminal utility which is independent of the state $x$ . Consequently, the derivative $J_{W x}(W,x,t)$ and hence the last term of the [portfolio](../../../Advanced%20Investments/An%20Asset%20Allocation%20Primer.md) will approach zero as $t\to T$ . Short-sighted investors pick a [portfolio](../../../Advanced%20Investments/An%20Asset%20Allocation%20Primer.md) given by the first term on the right-hand side. We can interpret the second term as an intertemporal hedge term since it shows how a long-term investor will deviate from the short-term investor. The last term will also disappear for "non-instantaneous' investors in three special cases:  

(1) there is no $x$ : [investment](../../../Advanced%20Investments/An%20Asset%20Allocation%20Primer.md) opportunities are constant; there is nothing to hedge..   
(2) $J_{W x}(W,x,t)\equiv0$ : The state variable does not affect the marginal utility of the investor.. This turns out to be the case for investors with [logarithmic utility](Exercises.md). Such an investor is not interested in [hedging](../../Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%205/Key%20Rates%20O1s%20Durations%20and%20Hedging.md) changes in the state variable..   
(3) $v(x)\equiv0$ : The state variable is uncorrelated with instantaneous [returns](../Chapter%203%20-%20%20Assets,%20Portfolios,%20and%20Arbitrage/Assets.md) on the traded assets. In this case the investor is not able to hedge changes in the state variable.  

In all other cases the state variable induces an additional term to the optimal [portfolio](../../../Advanced%20Investments/An%20Asset%20Allocation%20Primer.md) relative to the case of constant [investment](../../../Advanced%20Investments/An%20Asset%20Allocation%20Primer.md) opportunities.  

In general, we have three-fund separation in the sense that all investors will combine the [risk-free asset](../../../Financial%20Engineering/2.%20Forwards,%20Swaps,%20Futures,%20and%20Options.md), the "tangency [portfolio](../../../Advanced%20Investments/An%20Asset%20Allocation%20Primer.md)' of risky assets given by the [portfolio](../../../Advanced%20Investments/An%20Asset%20Allocation%20Primer.md) weights  
$$
\pi_{t}^{\mathrm{tan}}=\frac{1}{\mathbf{1}^{\top}\left(\underline{{\underline{{\sigma}}}}(x_{t},t)^{\top}\right)^{-1}\mathbf{\lambda}\mathbf{\lambda}\mathbf{\lambda}\mathbf{\lambda}(x_{t})}\left(\underline{{\underline{{\sigma}}}}(x_{t},t)^{\top}\right)^{-1}\mathbf{\lambda}\mathbf{\lambda}\mathbf{\lambda}\mathbf{\lambda}\mathbf{\lambda}\mathbf{\lambda}\mathbf{\lambda}\mathbf{\lambda}\mathbf{\lambda}.
$$  

and the "hedge [portfolio](../../../Advanced%20Investments/An%20Asset%20Allocation%20Primer.md)" given by the weights  
$$
\boldsymbol{\pi}_{t}^{\mathrm{hdg}}=\frac{1}{\mathbf{1}^{\top}\left(\underline{{\underline{{\sigma}}}}(x_{t},t)^{\top}\right)^{-1}\pmb{v}(x_{t})}\left(\underline{{\underline{{\sigma}}}}(x_{t},t)^{\top}\right)^{-1}\pmb{v}(x_{t}).
$$  

Inserting the definition of. $\lambda$ we can rewrite the expression for the tangency [portfolio](../../../Advanced%20Investments/An%20Asset%20Allocation%20Primer.md) as  
$$
\boldsymbol{\pi}_{t}^{\mathrm{tan}}=\frac{1}{\mathbf{1}^{\top}\underline{{\Sigma}}(x_{t},t)^{-1}(\boldsymbol{\mu}(x_{t},t)-\boldsymbol{r}^{f}(x_{t})\mathbf{1})}\underline{{\Sigma}}(x_{t},t)^{-1}\left(\boldsymbol{\mu}(x_{t},t)-\boldsymbol{r}^{f}(x_{t})\mathbf{1}\right),
$$  

which is analogous to the tangency [portfolio](../../../Advanced%20Investments/An%20Asset%20Allocation%20Primer.md) in the one-period [mean-variance analysis](../../../Financial%20Engineering/2.%20Forwards,%20Swaps,%20Futures,%20and%20Options.md), cf. (6.33).  

Substituting the candidate optimal values of. $c$ and $\pi$ back into the HJB equation and gathering. terms, we get the second order PDE  
$$
\begin{array}{l}{{\displaystyle{\left[{\cal M},{\scriptstyle x,t}}\right]=u\left(I_{u}(J_{W}(W,x,t))\right)-J_{W}(W,x,t)I_{u}(J_{W}(W,x,t))+\frac{\partial J}{\partial t}(W,x,t)+r(x)W J_{W}(W,x,t)}}\ {{\displaystyle~-\frac{1}{2}\frac{J_{W}(W,x,t)^{2}}{J_{W W}(W,x,t)}\|{\lambda(x)}\|^{2}+J_{x}(W,x,t)m(x)+\frac{1}{2}J_{x x}(W,x,t)\left(\|v(x)\|^{2}+\hat{v}(x)^{2}\right)}}\ {{\displaystyle~-\frac{1}{2}\frac{J_{W x}(W,x,t)^{2}}{J_{W W}(W,x,t)}\|v(x)\|^{2}-\frac{J_{W}(W,x,t)J_{W x}(W,x,t)}{J_{W W}(W,x,t)}\lambda(x)^{\top}v(x)}.}\end{array}
$$  

Although the PDE (6.65) looks very complicated, [closed-form solutions](../../../Financial%20Engineering/Derivatives/Part%20IX%20-%20Fixed%20Income%20Derivatives/Chapter%2040%20-%20Pricing%20Fixed%20Income%20Options:%20Black’s%20Model%20and%20MCS.md) can be found for a number of interesting model specifications. See, e.g., Munk (2008).  

If more than one, say. $k$ , variables are necessary to capture the information about [investment](../../../Advanced%20Investments/An%20Asset%20Allocation%20Primer.md) opportunities, the optimal [portfolio](../../../Advanced%20Investments/An%20Asset%20Allocation%20Primer.md) will involve. $k$ hedge portfolios beside the tangency [portfolio](../../../Advanced%20Investments/An%20Asset%20Allocation%20Primer.md). and the [risk-free asset](../../../Financial%20Engineering/2.%20Forwards,%20Swaps,%20Futures,%20and%20Options.md) so that. $(k+2)$ -fund separation holds.  

Nielsen and Vassalou (2006) have shown that the only characteristics of [investment](../../../Advanced%20Investments/An%20Asset%20Allocation%20Primer.md) opportunities. that will induce intertemporal [hedging](../../Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%205/Key%20Rates%20O1s%20Durations%20and%20Hedging.md) is the short-term [risk-free interest rate](Exercises.md) $\boldsymbol{r}_{t}^{f}$ and $\|\lambda_{t}\|$ , which is the maximum Sharpe ratio obtainable at the financial market. Since $\boldsymbol{r}_{t}^{f}$ is the intercept and $\|\lambda_{t}\|$ the slope of the instantaneous [mean-variance frontier](Exercises.md) this result makes good sense. Long-term. investors are concerned about the variations in the investments that are good in the short run.  
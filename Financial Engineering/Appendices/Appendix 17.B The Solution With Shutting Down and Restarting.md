---
aliases:
- Appendix 17B
- Investment
- Restarting
- Shutting Down
cssclasses: academia
key_concepts:
- Option pricing theory and Black-Scholes model
- Options Greeks and risk management
- Call and put option strategies
- Interest rate swaps and valuation
- Currency and cross-currency swaps
- Swap spreads and basis trading
- Appendix 17.B The Solution With Shutting Down and Restarting and financial analysis
- Appendix 17.B The Solution With Shutting Down and Restarting in modern finance
- Applications of Appendix 17.B The Solution With Shutting Down and Restarting
- 'Case study: Appendix 17.B The Solution With Shutting Down and Restarting'
tags:
- swaps
- options
- put
- call
- delta
- irs
title: Appendix 17.B The Solution With Shutting Down and Restarting
---

# Appendix 17.B The Solution With Shutting Down and Restarting  

In this appendix we explain the solution of two problems: investing and operating (1) when it is possible to shut down once and restart once, permanently, and (2) when it is possible to shut down and restart an infinite number of times. The solutions here can be implemented numerically.  

First, we develop some notation. Let $V_U(S,m,n;*)$ represent the value of an undeveloped reserve and $V_O(S,m,n;*)$ and $V_C(S,m,n;*)$ the value of developed operating and developed closed reserves, where it is possible to shut down $m$ times and restart $n$ times. The $*$ denotes a dependence on the prices at which shutting and restarting is optimal. We will be using the formulas given by equations (12.22) and (12.23) for the value of $\$1$ when $S$ reaches a barrier.  

# Single Shutdown and Restart  

Prior to the final permanent restart at $S^*$, we have:

$$
V_C(S,0,1;S^*)=\left(\frac{S^*}{\delta}-\frac{c}{r}-k_r\right)\left(\frac{S}{S^*}\right)^{h_1}
$$  

We choose $S^*$ to maximize this expression.  

While operating, prior to the shutdown at $S_* < S$, we have:

$$
V_O(S,1,1;S_*,S^*)=\frac{S}{\delta}-\frac{c}{r}+\left[\frac{c}{r}-k_s-\frac{S_*}{\delta}+V_C(S_*,0,1;S^*)\right]\left(\frac{S}{S_*}\right)^{h_2}
$$  

We choose $S_*$ to maximize this expression, taking $S^*$ as determined by equation (17.15).  

Finally, prior to the original investment decision, which occurs at $\bar{S} > S$, the value of the well is:

$$
V_U(S, 1, 1; S_*, S^*)=\left[V_O(\bar{S}, 1, 1; S_*, S^*)-I\right]\left(\frac{S}{\bar{S}}\right)^{h_1}
$$  

We find the $\bar{S}$ that maximizes this equation, taking $S_*$ and $S^*$ as given, determined by maximizing equations (17.15) and (17.16).  

# Infinite Shutdown and Restart  

The solution here is conceptually like that in the single shutdown and restart case, except that when we restart, we receive the option to shut down. Thus, when the well is shut, we have:

$$
V_C(S,\infty,\infty;S_*,S^*)=\left[-k_r+V_O(S^*,\infty,\infty;S_*,S^*)\right]\left(\frac{S}{S^*}\right)^{h_1}
$$  

While operating, prior to the shutdown at $S > S_*$, we have:

$$
\begin{aligned}
V_O(S,\infty,\infty;S_*,S^*) &= \frac{S}{\delta}-\frac{c}{r}\\
&+ \left[\frac{c}{r}-k_s-\frac{S_*}{\delta}+V_C(S_*,\infty,\infty;S_*,S^*)\right]\left(\frac{S}{S_*}\right)^{h_2}
\end{aligned}
$$  

Note that $V_C$ and $V_O$ are defined in terms of each other. We can substitute equation (17.17) into equation (17.18) and set $S = S_*$. This gives:

$$
V_O(S^*,\infty,\infty;S_*,S^*)=\frac{S^*/\delta-c/r-k_r(S_*/S^*)^{h_1}+(c/r-S_*/\delta-k_s)\times(S^*/S_*)^{h_2}}{1-(S_*/S^*)^{h_1}\times(S^*/S_*)^{h_2}}
$$  

Given starting values of $S^*$ and $S_*$, we can evaluate equation (17.19), substituting the answer into equation (17.17) to obtain an estimate of $V_C(S,\infty,\infty;S_*,S^*)$. Then we can maximize equation (17.17) with respect to $S^*$ and equation (17.18) with respect to $S_*$. This gives us new estimates of $V_C(S_*)$ and $V_O(S^*)$. Iterate until convergence.  

Once we have computed $S^*$, $S_*$, and $V_C(S_*)$, the value of the well is:

$$
V_U(S,\infty,\infty;S_*,S^*)=\left[\frac{\bar{S}}{\delta}-\frac{c}{r}-I+V_C(S_*,\infty,\infty;S_*,S^*)\left(\frac{\bar{S}}{S_*}\right)^{h_2}\right]\left(\frac{S}{\bar{S}}\right)^{h_1}
$$  

We maximize this with respect to $\bar{S}$ to find the investment trigger and value of the well.

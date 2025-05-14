---
tags:
  - discount_function
  - interest_rate
  - ornstein_uhlenbeck
  - term_premium
  - zero_coupon_bond
aliases:
  - Chapter 10 Exercises
  - Exercises
key_concepts:
  - Arbitrage and short rate
  - Interest rate uncertainty
  - Nominal term structure
  - SAINTS model
  - Term premium and deflator
---

# 10.10 Exercises  

EXERCISE 10.1 Show that if there is no [[Arbitrage Pricing of Derivatives|arbitrage]] and the [[An Overview of the Vasicek Short Rate Model|short rate]] can never go negative,.   
then the [[Basic Interest Rate Concepts and Relations|discount function]] is non-increasing and all forward rates are non-negative.  

EXERCISE 10.2 Show Equation (10.51).  

EXERCISE 10.3 The [[Table of Contents|term premium]] at time $t$ for the future period $[t^{\prime},T]$ is the current [[Forward Points in Currency|forward rate]] for that period minus the expected [[The Foreign Exchange Market Annotations|spot rate]], i.e. $f_{t}^{t^{\prime},T}-\mathrm{E}_{t}[y_{t^{\prime}}^{T}]$ . This exercise will give a link between the [[Table of Contents|term premium]] and a [[Exercises|state-price deflator]] $\zeta=\left(\zeta_{t}\right)$  

(a) Show that  
$$
B_{t}^{T}=B_{t}^{t^{\prime}}\operatorname{E}_{t}\left[B_{t^{\prime}}^{T}\right]+\operatorname{Cov}_{t}\left[\frac{\zeta_{t^{\prime}}}{\zeta_{t}},\frac{\zeta_{T}}{\zeta_{t^{\prime}}}\right]
$$  

for any $t\leq t^{\prime}\leq T$  

(b) Using the above result, show that  
$$
\operatorname{E}_{t}\left[e^{-y_{t^{\prime}}^{T}(T-t^{\prime})}\right]-e^{-f_{t}^{t^{\prime},T}(T-t^{\prime})}=-{\frac{1}{B_{t}^{t^{\prime}}}}\operatorname{Cov}_{t}\left[{\frac{\zeta_{t^{\prime}}}{\zeta_{t}}},{\frac{\zeta_{T}}{\zeta_{t^{\prime}}}}\right].
$$  

Using the previous result and the approximation $e^{x}\approx1+x$ , show that  
$$
f_{t}^{t^{\prime},T}-\mathrm{E}_{t}[y_{t^{\prime}}^{T}]\approx-\frac{1}{(T-t^{\prime})B_{t}^{t^{\prime}}}\mathrm{Cov}_{t}\left[\frac{\zeta_{t^{\prime}}}{\zeta_{t}},\frac{\zeta_{T}}{\zeta_{t^{\prime}}}\right].
$$  

EXERCISE 10.4 The purpose of this exercise is to show that the claim of the gross return pure. expectation hypothesis is inconsistent with [[Exercises|interest rate uncertainty]]. In the following we consider time points $t_{0}<t_{1}<t_{2}$  

(a) Show that if the hypothesis holds, then  
$$
\frac{1}{B_{t_{0}}^{t_{1}}}=\frac{1}{B_{t_{0}}^{t_{2}}}\operatorname{E}_{t_{0}}\left[B_{t_{1}}^{t_{2}}\right].
$$  

Hint: Compare two [[An Asset Allocation Primer|investment]] strategies over the period $[t_{0},t_{1}]$ .The first strategy is to buy.   
at time $t_{0}$ zero-coupon bonds maturing at time. $t_{1}$ .The second strategy is to buy at time. $t_{0}$   
zero-coupon bonds maturing at time $t_{2}$ and to sell them again at time. $t_{1}$  

(b) Show that if the hypothesis holds, then  
$$
\frac{1}{B_{t_{0}}^{t_{2}}}=\frac{1}{B_{t_{0}}^{t_{1}}}\operatorname{E}_{t_{0}}\left[\frac{1}{B_{t_{1}}^{t_{2}}}\right].
$$  

(c) Show from the two previous questions that the hypothesis implies that  
$$
\mathrm{E}_{t_{0}}\left[{\frac{1}{B_{t_{1}}^{t_{2}}}}\right]={\frac{1}{\mathrm{E}_{t_{0}}\left[B_{t_{1}}^{t_{2}}\right]}}.
$$  

(d) Show that ( $^*$ ) can only hold under full certainty. Hint: Use [[Volatility and Convexity|Jensen's inequality]].  

EXERCISE 10.5 Show (10.63) and (10.64).  

EXERCISE 10.6 Go through the derivations in the subsection with the heading "An example" in Section 10.6.3.  

EXERCISE 10.7 Constantinides (1992) develops the so-called [[Exercises|SAINTS model]] of the [[Exercises|nominal term structure]] of [[Interest Rate Quotations|interest rates]] by specifying exogenously the [[Real and Nominal Interest Rates and Term Struc|nominal state-price deflator]]. $\ddot{\zeta}$ . In a  

slightly simplified version, his assumption is that  
$$
\tilde{\zeta}_{t}=k e^{-g t+(X_{t}-\alpha)^{2}},
$$  

where $k$ $g$ , and $\alpha$ are constants, and $X=\left(X_{t}\right)$ follows the [[Equilibrium Interest Rate Models|Ornstein-Uhlenbeck process]]  
$$
d X_{t}=-\kappa X_{t}d t+\sigma d z_{t},
$$  

where $\kappa$ and $\sigma$ are positive constants with $\sigma^{2}<\kappa$ and $z=\left(z_{t}\right)$ is a standard one-dimensional [[Continuous-Time Stochastic Processes|Brownian motion]]..  

(a) Derive the dynamics of the [[Real and Nominal Interest Rates and Term Struc|nominal state-price deflator]]. Express the nominal [[The Gauss Model|short-term interest rate]], $\tilde{r}_{t}$ , and the nominal [[Exercises|market price of risk]], $\ddot{\lambda}_{t}$ , in terms of the variable $X_{t}$   
(b) Find the dynamics of the nominal [[An Overview of the Vasicek Short Rate Model|short rate]].   
(c) Find parameter constraints that ensure that the [[An Overview of the Vasicek Short Rate Model|short rate]] stays positive? Hint: The [[An Overview of the Vasicek Short Rate Model|short rate]] is a quadratic function of $X$ . Find the minimum value of this function.   
(d) What is the distribution of $X_{T}$ given $X_{t}$ \~.   
(e) Let $Y$ be a normally distributed random variable with mean $\mu$ and variance $v^{2}$ . Show that  
$$
\operatorname{E}\left[e^{-\gamma Y^{2}}\right]=(1+2\gamma v^{2})^{-1/2}\exp\left\{-{\frac{\gamma\mu^{2}}{1+2\gamma v^{2}}}\right\}.
$$  

(f) Use the results of the two previous questions to derive the time $t$ price of a nominal zero-. coupon bond with maturity. $T$ , i.e. $\tilde{B}_{t}^{T}$ . It will be an exponential-quadratic function of $X_{t}$ What is the yield on this bond?.  

(g) Find the percentage volatility. $\sigma_{t}^{T}$ of the price of the zero-coupon bond maturing at $T$  

(h) The instantaneous expected excess rate of return on the zero-coupon bond maturing at $T$ is often called the [[Table of Contents|term premium]] for maturity. $T$ . Explain why the [[Table of Contents|term premium]] is given by. $\sigma_{t}^{T}\ddot{\lambda}_{t}$ and show that the [[Table of Contents|term premium]] can be written as.  
$$
4\sigma^{2}\alpha^{2}\left(1-F(T-t)\right)\left(\frac{X_{t}}{\alpha}-1\right)\left(\frac{X_{t}}{\alpha}-\frac{1-F(T-t)e^{\kappa(T-t)}}{1-F(T-t)}\right),
$$  

where  
$$
F(\tau)=\frac{1}{\frac{\sigma^{2}}{\kappa}+\left(1-\frac{\sigma^{2}}{\kappa}\right)e^{2\kappa\tau}}.
$$  

For which values of $X_{t}$ will the [[Table of Contents|term premium]] for maturity $T$ be positive/negative? For a given state $X_{t}$ , is it possible that the the [[Table of Contents|term premium]] is positive for some maturities and negative for others?  

EXERCISE 10.8 Assume a [[Risk-Neutral Probabilities|continuous-time economy]] where the [[Exercises|state-price deflator]] $\zeta=\left(\zeta_{t}\right)$ has dynamics  
$$
d\zeta_{t}=-\zeta_{t}\left[r_{t}d t+\lambda d z_{1t}\right],
$$  

where $z_{1}=\left(z_{1t}\right)$ is a (one-dimensional) standard [[Continuous-Time Stochastic Processes|Brownian motion]], $\lambda$ is a constant, and $\boldsymbol r=(r_{t})$ follows the [[Equilibrium Interest Rate Models|Ornstein-Uhlenbeck process]]  
$$
d r_{t}=\kappa[\bar{r}-r_{t}]d t+\sigma_{r}d z_{1t}.
$$  

This is the [[Vasicek Short Rate Model|Vasicek model]] so we know that the prices of zero-coupon bonds are given by (10.37) and the corresponding yields are given by (10.39).  

Suppose you want to value a real uncertain [[Preview of the Book|cash flow]] of $F_{T}$ coming at time $T$ . Let $x_{t}=\operatorname{E}_{t}[F_{T}]$ and assume that  
$$
d x_{t}=x_{t}\left[\mu_{x}d t+\sigma_{x}\rho d z_{1t}+\sigma_{x}\sqrt{1-\rho^{2}}d z_{2t}\right],
$$  

where $\mu_{x}$ $\sigma_{x}$ , and $\rho$ are constants, and where. $z_{2}~=~(z_{2t})$ is another (one-dimensional) standard [[Continuous-Time Stochastic Processes|Brownian motion]] independent of $z_{1}$  

(a) Argue that $x=\left(x_{t}\right)$ must be a martingale and hence that $\mu_{x}=0$  

(b) Show that the time $t$ value of the claim to the [[Preview of the Book|cash flow]] $F_{T}$ is given by  
$$
V_{t}\equiv V(t,r_{t},x_{t})=x_{t}e^{-A(T-t)-B(T-t)r_{t}},
$$  

where $B(\tau)=b(\tau)$ and  
$$
A(\tau)=a(\tau)+\rho\lambda\sigma_{x}\tau+\frac{\rho\sigma_{x}\sigma_{r}}{\kappa}\left(\tau-b(\tau)\right).
$$  

(c) Write the dynamics of $V=\left(V_{t}\right)$ as $d V_{t}=V_{t}[\mu_{t}^{V}d t+\sigma_{1t}^{V}d z_{1t}+\sigma_{2t}^{V}d z_{2t}]$ . Use $(^{*})$ to identify $\mu_{t}^{V}$ $\sigma_{1t}^{V}$ , and $\sigma_{2t}^{V}$ . Verify that $\mu_{t}^{V}=r_{t}+\left(\pmb{\sigma}_{t}^{V}\right)^{\top}\lambda_{t}$ , where ${\pmb\sigma}^{V}=(\sigma_{1}^{V},\sigma_{2}^{V})^{\top}$ and $\lambda$ is the [[Exercises|market price of risk]] vector (the [[Exercises|market price of risk]] associated with $z_{2}$ is zero! Why?).  

(d) Define the risk-adjusted [[PSET 7- Kohler|discount rate]]. $R_{t}$ for the [[Preview of the Book|cash flow]] by the relation $V_{t}=\mathrm{E}_{t}[F_{T}]e^{-R_{t}[T-t]}$ What is the difference between $R_{t}$ and $y_{t}^{T}$ ? How does this difference depend on the [[Preview of the Book|cash flow]] payment date $T$  

EXERCISE 10.9 Consider an economy with complete [[Financial Markets and Institutions Lecture Notes|financial markets]] and a representative agent with [[The Simple Multi-Period Ccapm|CRRA utility]], u(C) = q'-z, , where $\gamma>0$ , and a time [[Utility Indices|preference]] rate of $\delta$ .The [[Pareto-Optimality in Some Incomplete Markets|aggregate consumption]] level $C$ is assumed to follow the [[The Ornstein-Uhlenbeck (OU) Process|stochastic process]]  
$$
d c_{t}=c_{t}\left[\left(a_{1}X_{t}^{2}+a_{2}X_{t}+a_{3}\right)d t+\sigma_{c}d z_{t}\right],
$$  

where $z~=~\left(z_{t}\right)$ is a standard one-dimensional [[Continuous-Time Stochastic Processes|Brownian motion]] under the real-life probability measure $\mathbb{P}$ and where. $a_{1},a_{2},a_{3},\sigma_{c}$ are constants with $\sigma_{c}~>~0$ .Furthermore, $X~=~\left(X_{t}\right)$ is a [[The Ornstein-Uhlenbeck (OU) Process|stochastic process]] with dynamics  
$$
d X_{t}=-\kappa X_{t}d t+d z_{t}.
$$  

where $\kappa$ is a positive constant.  

(a) Show that the [[The Gauss Model|short-term interest rate]] is of the form $r_{t}=d_{1}X_{t}^{2}+d_{2}X_{t}+d_{3}$ and determine the constants $d_{1},d_{2},d_{3}$  

(b) Find a parameter condition under which the [[The Gauss Model|short-term interest rate]] is always non-negative.  

(c) Write up the dynamics of $r_{t}$ (d) What is the [[Exercises|market price of risk]] in this economy?  

Suppose that the above applies to the real economy and that money has no effects on the real economy. The [[Pricing an Inflation Swap|consumer price index]] $F_{t}$ is supposed to have dynamics  
$$
d F_{t}=F_{t}\left[\mu_{\varphi t}d t+\rho_{C F}\sigma_{\varphi t}d z_{t}+\sqrt{1-\rho_{C F}^{2}}\sigma_{\varphi t}d\hat{z}_{t}\right],
$$  

where $\rho_{C F}$ is a constant correlation coefficient and $\hat{z}=(\hat{z}_{t})$ is another standard [[Continuous-Time Stochastic Processes|Brownian motion]] independent of $z$ . Assume that $\mu_{\varphi t}$ and $\sigma_{\varphi t}$ are on the form  
$$
\mu_{\varphi t}=b_{1}X_{t}^{2}+b_{2}X_{t}+b_{3},\qquad\sigma_{\varphi t}=k X_{t}.
$$  

(e) Write up an expression for the nominal [[The Gauss Model|short-term interest rate]], $\tilde{r}_{t}$  

Assume in the rest of the problem that $\gamma a_{1}+b_{1}=k^{2}$  

(f) Show that the nominal [[An Overview of the Vasicek Short Rate Model|short rate]] $\ddot{r}_{t}$ is affine in $X_{t}$ and express $X_{t}$ as an affine function of $\tilde{r}_{t}$   
(g) Compute the nominal [[Exercises|market price of risk]] $\tilde{\lambda}_{t}$   
(h) Determine the dynamics of the nominal [[An Overview of the Vasicek Short Rate Model|short rate]]. The [[Black-Scholes Model|drift and volatility]] should be expressed in terms of $\ddot{r}_{t}$ , not $X_{t}$  
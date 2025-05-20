---
cssclasses:
  - academia
title: Black-Scholes Model
tags:
  - black_scholes_model
  - geometric_brownian_motion
  - kospi_200
  - stock_price_process
  - volatility
  - option_pricing
  - risk_neutral_valuation
aliases:
  - BSM
  - Black Scholes
  - Black-Scholes Formula
key_concepts:
  - Drift and volatility
  - Geometric Brownian motion
  - KOSPI 200 index data
  - Normal distribution histograms
  - Stock price process
  - Risk-neutral valuation
  - Black-Scholes PDE
  - Option pricing
---

# Black-Scholes Model

## Modeling the Stock Price Process

One of the basic building blocks of the Black-Scholes model is the stock price process. In particular, in the Black-Scholes world, the stock price process, denoted by $S_t$, is modeled as a geometric Brownian motion satisfying the following stochastic differential equation:

$$dS_t=S_t(\mu dt+\sigma dW_t),$$

where $\mu$ and $\sigma$ are constants called the drift and volatility, respectively. Also, $\sigma$ is always assumed to be a positive constant.

In order to see if such model is "reasonable," let us look at the price data of KOSPI 200 index. In particular Figure 5.1 depicts the KOSPI 200 index from January 2, 2001 till May 18, 2011. If it is reasonable to model it as a geometric Brownian motion, we must have

$$\frac{\Delta S_t}{S_t}\approx\mu\Delta t+\sigma\Delta W_t.$$

In particular if we let $\Delta t=h$ (so that $\Delta S_t=S_{t+h}-S_t$ and $\Delta W_t=W_{t+h}-W_t$), the above approximate equality becomes

$$\frac{S_{t+h}-S_t}{S_t}\approx\mu h+\sigma(W_{t+h}-W_t).$$

Since $\sigma(W_{t+h}-W_t)\sim N(0, \sigma^2h)$, the histogram of $(S_{t+h}-S_t)/S_t$ should resemble a normal distribution with standard deviation $\sigma\sqrt{h}$ (It is called the $h$-day volatility.) To see it is indeed the case we have plotted the histograms for $h=1, 2, 3, 5, 7$ (days) in Figures 5.2 up to

![500](Attachments/500-101.png)

Figure 5.1: KOSPI 200 from 2001. 1. 2 to 2011. 5. 18.

5.7. In there, we have also computed the normal distributions that are closest to the given histograms. Such normal distributions are overlaid together in Figure 5.8. In there, we can see the standard deviations ($h$-day volatility) for each time interval $h$ increases as shown in Table 5.1.

Let us now see if the $h$-day volatility increases in proportion to $\sqrt{h}$. The last column of Table 5.1 shows the $h$-day volatilities divided by $\sqrt{h}$. There, we can see that they remain roughly constant. In Figure 5.9 are plotted $h$-day volatilities and a graph $y=0.016436\sqrt{h}$ that best fits the data. In either case, we can see that the $h$-day volatilities scales roughly in proportion to $\sqrt{h}$.

<table>
<tbody>
<tr>
<th>$\mathrm{day}(h)$</th>
<th>$h$-day volatility</th>
<th>$(h$-day volatility$)/\sqrt{h}$</th>
</tr>
<tr>
<td>1</td>
<td>0.016858</td>
<td>0.016858</td>
</tr>
<tr>
<td>2</td>
<td>0.023430</td>
<td>0.016568</td>
</tr>
<tr>
<td>3</td>
<td>0.029624</td>
<td>0.017103</td>
</tr>
<tr>
<td>5</td>
<td>0.036611</td>
<td>0.016373</td>
</tr>
<tr>
<td>7</td>
<td>0.040421</td>
<td>0.015278</td>
</tr>
</tbody>
</table>

Table 5.1: Standard Deviations (volatility) for the Normal Distributions.

Next, if $S_t$ were to be modeled as satisfying

$$\frac{\Delta S_t}{S_t}\approx\mu\Delta t+\sigma \Delta W_t,$$

using the increment Brownian motion $W_t$, it is not enough to check that the standard deviation of $\Delta S_t/S_t$ scales like $\sqrt{h}$. We also need to check the independence of increment. In order to do that, let us go back to the stochastic differential equation for $S_t$ and rewrite $d\log S_t$ using the Ito formula as:

$$d\log S_t=(\mu-\frac{1}{2}\sigma^2)dt+\sigma dW_t.$$

Therefore we can write

$$\Delta\log S_t\approx\left(\mu-\frac{1}{2}\sigma^2\right)\Delta t+\sigma\Delta W_t.$$

On the other hand

$$\log S_t=\log S_0+\left(\mu-\frac{1}{2}\sigma^2\right)t+\sigma W_t.$$

Therefore from (5.1) and (5.2), $\log S_t$ and $\Delta\log S_t$ should exhibit "independent" behavior. For that purpose, the following lemma comes in handy.

Lemma 5.1. Let $X$ and $Y$ be both Gaussian random variables. Then $X$ and $Y$ are independent if and only if $Cor(X, Y) = 0$, where $Cor(X, Y)$ is the correlation given by

$$Cor(X, Y)=E\left[\left(\frac{X-m_X}{\sigma_X}\right)\left(\frac{Y-m_Y}{\sigma_Y}\right)\right],$$

where $m_X=E[X]$ and $\sigma_X^2 = E[(X - m_X)^2]$ and $m_Y$ and $\sigma_Y$ are defined similarly.

From the data we can compute $Cor(\log S_t, \Delta\log S_t)$, which turns out to be -0.023749. This correlation between $\log S_t$ and $\Delta\log S_t$ is quite small; therefore it is reasonable to presume it to be zero, which then implies by Lemma 5.1 that $\log S_t$ and $\Delta\log S_t$ are independent.

The $h$-day volatility scaling and the independence expounded above indicate that it is "reasonable" to model $S_t$ as a geometric Brownian motion.

It should be noted that we can use $\Delta S_t/S_t$ and $\Delta\log S_t$ interchangeably. The reason is as follows. First

$$\Delta\log S_t=\log S_{t+h}-\log S_t=\log\frac{S_{t+h}}{S_t},$$

But

$$\log\frac{S_{t+h}}{S_t}=\log\left(1+\frac{S_{t+h}-S_t}{S_t}\right).$$

By the Taylor expansion, $\log(1+x)=x+O(x^2)$. Therefore

$$\log\frac{S_{t+h}}{S_t}\approx\frac{S_{t+h}-S_t}{S_t}.$$

In other words, it is reasonable to say that $\Delta\log S_t\approx\Delta S_t/S_t$.

A remark on the drift term is in order. The $h$-day drift terms are listed as Table 5.2

<table>
<tbody>
<tr>
<th>$\mathrm{day}(h)$</th>
<th>$h$-day mean</th>
</tr>
<tr>
<td>1</td>
<td>0.0007</td>
</tr>
<tr>
<td>2</td>
<td>0.0014</td>
</tr>
<tr>
<td>3</td>
<td>0.0021</td>
</tr>
<tr>
<td>5</td>
<td>0.0035</td>
</tr>
<tr>
<td>7</td>
<td>0.0046</td>
</tr>
</tbody>
</table>

Table 5.2: $h$-day mean ($h$-day drift terms).

It confirms the expected pattern that $h$-day mean is supposed to be proportional to $h$. However, it is a happy accident of data. In many cases, $h$-day mean will change quite a bit so that they generally do not exhibit such pattern. Estimating the drift term is not a statistically robust process. So any estimate of the drift is not a reliable data. However, as we shall see below, the drift term plays no role in the Black-Scholes model. So it really does not matter how one sets it.

## Black-Scholes Market

Black-Scholes model is the simplest yet most widely used continuous model in finance. Even with its many shortcomings, its importance can not be too emphasized. Anyone who is interested in gaining deeper understanding of mathematical finance must be thoroughly familiar with it. Let us now spell out the details of this model.

### Time

The interval is $[0, T]$, where $t=0$ denotes the present.

### Probability space

The underlying probability space is denoted by $(\Omega, \mathcal{F}, P)$.

### Information Structure

The information structure is given by a filtration $(\mathcal{F}_t)_{t\geq0}$ of sub-fields of $F$ such that:

(i) $\mathcal{F}_0$ is the trivial field $\{\emptyset, \Omega\}$

(ii) $\mathcal{F}_{t_1}\subset\mathcal{F}_{t_2}$ if $t_1\leq t_2$

For any $t\in[0, T]$, we define $\mathcal{F}_{t-}$ to be the field generated by all $\mathcal{F}_s$, ($s<t$) and $\mathcal{F}_{t+}$ the field that is the intersection of $\mathcal{F}_s$ for all $s>t$. We then assume that

$$\mathcal{F}_{t-}=\mathcal{F}_t=\mathcal{F}_{t+}.$$

### Brownian motion

The Brownian motion with respect to the measure $P$ is denoted by $W_t$. It is assumed that

$$W_t\in\mathcal{F}_t.$$

### Bank account (riskless bond) process

The bank account (riskless bond) process $B_t$ is assumed to satisfy the following ordinary differential equation:

$$\begin{array}{rcl}
dB_t&=&rB_tdt\\
B_0&=&1
\end{array}$$

For a fixed positive constant $r$ which is usually called the riskless (instantaneous) interest rate. It is trivial to see that

$$B_t=e^{rt},$$

Which is the result of the continuous compounding with interest rate $r$.

### Time scale

It is customary to use the time scale in such a way that one year is given duration (time span) 1. Since we only count the trading days, one year is considered to have roughly 250 trading days, which means that one trading day is given 1/250 (year). By the same token, the interest rate is always quoted as the annualized interest rate. However, in reality, banks do not compound continuously; and if the compounding is to be done daily, banks do compound even for holidays. So reconciling the differences between the theory (continuous compounding) and the practice (daily, monthly or quarterly compounding) is a subtle matter.

### Stock price process

We assume there is only one risky asset, which we call the stock. Its price process is denoted by $S_t$. Following the motivation given in Section 5.1, it is assumed to satisfy the following stochastic differential equation:

$$dS_t=S_t(\mu dt+\sigma dW_t),$$

where $\mu$ is a constant while we always assume $\sigma$ is a positive constant. Thus $S_t$ is the so-called geometric Brownian motion studied in Example 4.25 of Chapter 4. In particular, we know that

$$S_t=S_0\exp\left[\left(\mu-\frac{1}{2}\sigma^2\right)t+\sigma W_t\right].$$

### Discounted stock price process

Define the discounted stock price process $S_t^*$ by

$$S_t^*=\frac{S_t}{B_t}=e^{-rt}S_t.$$

Then it is easily seen that

$$dS_t^*=S_t^*\left[(\mu-r)dt+\sigma dW_t\right].$$

The standard procedure of the martingale approach in finance is to find a new measure $Q$, called the martingale measure or risk neutral measure, with respect to which $S_t^*$ becomes a martingale. Utilizing the standard procedure in Girsanov theorem, define the exponential martingale $M_t$ by

$$\begin{array}{rcl}
dM_t&=&-\gamma M_tdW_t\\
M_0&=&1
\end{array}$$

for some constant $\gamma$ to be determined later. First, define the measure $Q_t$ on $\mathcal{F}_t$ by

$$dQ_t=M_tdP.$$

Then let $Q=Q_T$. We learned that

$$Q_t=Q|_{\mathcal{F}_t}.$$

The Girsanov theorem says that the new stochastic process $\widetilde{W}_t$ defined by

$$d\widetilde{W}_t=dW_t+\gamma dt$$

is a Brownian motion with respect to $Q(=Q_T)$. Now

$$\begin{array}{rcl}
dS_t^*&=&S_t^*\left[(\mu-r)dt+\sigma dW_t\right]\\
&=&S_t^*\left[(\mu-r-\sigma\gamma)dt+\sigma d\widetilde{W}_t\right].
\end{array}$$

If we define $\gamma$ by

$$\gamma=\frac{\mu-r}{\sigma},$$

$S_t^*$ now satisfies

$$dS_t^*=\sigma S_t^*d\widetilde{W}_t.$$

Namely, $S_t^*$ is a $Q$-martingale. The constant $\gamma$ defined in (5.3) is called the "market price of risk." Although a misnomer, it nonetheless plays a very important role in finance. It is also useful to notice that (5.4) is equivalent to

$$dS_t=S_t(rdt+\sigma d\widetilde{W}_t).$$

In finance jargon, (5.5) is to be interpreted as saying that in the risk neutral (martingale) world, the mean instantaneous return of any risky asset should be exactly the same as that of riskless asset.

## Risk-Neutral Valuation Principle in the Black-Scholes Model

In Chapter 2, we have established the risk-neutral valuation principle for the discrete model. The same risk neutral valuation principle holds for continuous model. In this section, we establish it for the Black-Scholes model. However any alert reader will notice that this derivation works without any significant modification for any continuous market model with stochastic volatility.

Definition 5.2. A European option or a European contingent claim with expiry (time) at $t=T$ is an $\mathcal{F}_T$-random variable.

Let us now suppose $X$ is a European option with expiry $t=T$. The risk-neutral valuation principle we are trying to derive here has the same form as the one given for discrete case.

### Construction of Portfolio

Let $Q$ be the martingale measure obtained in section 5.2. Define $V_t$ by

$$V_t=B_tE_Q\left[\frac{X}{B_T}\mid\mathcal{F}_t\right]$$

And

$$V_t^*=\frac{V_t}{B_t}.$$

Thus $V_t^*$ is obviously a $Q$-martingale. Then by the Martingale Representation theorem, there exists $\alpha_t\in\mathcal{F}_t$ such that

$$dV_t^*=\alpha_td\widetilde{W}_t.$$

Combining this with (5.4), and setting

$$\zeta_t=\frac{\alpha_t}{\sigma S_t^*},$$

It is easy to see that

$$dV_t^*=\zeta_tdS_t^*.$$

It should be noted that the denominator in (5.6) never vanishes as $\sigma>0$ and $S_t^*>0$. Define $\xi_t$ by

$$\xi_t=V_t^*-\zeta_tS_t^*.$$

Thus we have

$$V_t=\xi_tB_t+\zeta_tS_t.$$

Namely, if one construct a portfolio of $\xi_t$ units of riskless bond and $\zeta_t$ shares of stock at each time $t$, then $V_t$ must be the one that represents the value of this portfolio. We will show below that this portfolio is self-financing.

### Continuous Trading and Self-Financing

In the Black-Scholes model, we assume the portfolio is continuously changed, i.e. traded (rebalanced, to use finance jargon). This continuous trading assumption is not of course realistic but can be envisioned as a "limit" of frequent trading.

Definition 5.3. A portfolio $(\xi_t, \zeta_t)$ that consists of $\xi_t$ units of riskless bond and $\zeta_t$ shares of stocks is called self-financing, if

$$dV_t=\xi_tdB_t+\zeta_tdS_t,$$

where $V_t$ is the values of the portfolio at time $t$ given by

$$V_t=\xi_tB_t+\zeta_tS_t.$$

This definition comes as a "limit" of the discrete counterpart. (See especially Definition 2.39.)

Theorem 5.4. The portfolio $(\xi_t, \zeta_t)$ is self-financing if and only if

$$dV_t^*=\zeta_tdS_t^*.$$

Proof. First note that

$$\begin{array}{rcl}
dV_t&=&d(B_tV_t^*)\\
&=&V_t^*dB_t+B_tdV_t^*
\end{array}$$

By Ito's formula. On the other hand, using (5.9), we have

$$\begin{aligned}
\xi_tdB_t+\zeta_tdS_t &= (V_t^*-\zeta_tS_t^*)dB_t+\zeta_tdS_t \\
&= V_t^*dB_t+\zeta_tB_t\left[-B_t^{-2}S_tdB_t+B_t^{-1}dS_t\right] \\
&= V_t^*dB_t+\zeta_tB_td(B_t^{-1}S_t) \\
&= V_t^*dB_t+\zeta_tB_tdS_t^*.
\end{aligned}$$

Note that the self-financing condition is equivalent to the LHS of (5.10) being equal to the LHS of (5.11), which in turn is equivalent to $dV_t^*=\zeta_tdS_t^*$ by looking at the right hand sides of (5.10) and (5.11).

Remark 5.5. Theorem 5.4 is the continuous counter-part of Proposition 2.40. It also proves that the portfolio constructed in "Constructing Portfolio" subsection is self-financing.

### Replicating Portfolio

Definition 5.6. A portfolio consisting of $\xi_t$ units of riskless bond and $\zeta_t$ shares of stock is said to replicate a European option $X\in\mathcal{F}_T$ if

$$\xi_TB_T+\zeta_TS_T=X$$

As random variables.

### Risk-Neutral Valuation Principle

We are now ready to state and prove the risk-neutral valuation principle in the Black-Scholes model setting. Suppose $(\xi_t, \zeta_t)$ is a portfolio constructed above using the martingale representation theorem as in "Construction of Portfolio" subsection above. Then, in particular, the discounted portfolio value $V_t^*$ satisfies

$$dV_t^*=\zeta_tdS_t^*,$$

which then implies that this portfolio is self-financing by Theorem 5.4. Now note that since $X$ and $B_T\in\mathcal{F}_T$

$$\begin{array}{rcl}
V_T&=&B_TE_Q\left[\frac{X}{B_T}\mid\mathcal{F}_T\right]\\
&=&X
\end{array}$$

which means that this portfolio replicates $X$. Therefore the price of $X$ at time $t$ must be

$$V_t=B_tE_Q\left[\frac{X}{B_T}\mid\mathcal{F}_t\right].$$

For, otherwise, there must exist an arbitrage at time $t$ involving the portfolio $(\xi_t, \zeta_t)$ and the option itself $X$. We summarize our result as follows:

Theorem 5.7. (Risk-Neutral Valuation Principle) The price $V_t$ at time $t$ of the European option $X\in\mathcal{F}_T$ is

$$V_t=B_tE_Q\left[\frac{X}{B_T}\mid\mathcal{F}_t\right].$$

## The Black-Scholes Formula

The above risk-neutral valuation principle gives a method of computing the price of any European option. However, in practice, it is not easy to carry out actual closed-form computation. In this section, we derive the celebrated formula called the Black-Scholes formula for pricing the European call or put options. A European call option is a contract to pay at expiry, say at time $T$, the amount that is the difference between the preset value, say $K$, called the strike price and the stock price $S_T$ as long as $S_T$ is greater than $K$; and zero otherwise. (In this chapter all options are European.) Thus the call option can be succinctly expressed as

$$X=(S_T-K)^+,$$

where $a^+$ means $\max(a, 0)$.

Let us now find the formula for the price of $X$ at time 0 i.e. we are seeking a closed-form formula for $V_0$:

$$\begin{aligned}
V_0 &= e^{-rT}E_Q\left[(S_T-K)^+\right] \\
&= e^{-rT}E_Q\left[(S_T-K)\cdot\mathbf{1}_{\{S_T>K\}}\right] \\
&= e^{-rT}E_Q\left[S_T\cdot\mathbf{1}_{\{S_T>K\}}\right]-Ke^{-rT}E_Q\left[\mathbf{1}_{\{S_T>K\}}\right] \\
&= I_1-I_2
\end{aligned}$$

where $\mathbf{1}_{\{S_T>K\}}$ is the indicator (characteristic) function of the set $\{S_T>K\}$.

Compute $I_2$: First, note that

$$S_T=S_0\exp\left[\left(r-\frac{1}{2}\sigma^2\right)T+\sigma\widetilde{W}_T\right]>K$$

Is equivalent to

$$\log(S_0/K)+\left(r-\frac{1}{2}\sigma^2\right)T>-\sigma\widetilde{W}_T\stackrel{\mathcal{L}}{=}-\sigma\sqrt{T}\widetilde{W}_1,$$

where the symbol $\mathcal{L}$ above the equal sign denotes the equality in law, or equivalently in distribution. Then

$$Prob(S_T>K)=Prob\left(-\widetilde{W}_1<\frac{\log(S_0/K)+(r-\frac{1}{2}\sigma^2)T}{\sigma\sqrt{T}}\right).$$

Thus, since the distribution of $-\widetilde{W}_1$ is the standard normal distribution $N(0, 1)$ of mean 0 and variance 1,

$$E_Q[\mathbf{1}_{\{S_T>K\}}]=Prob\left(Z<\frac{\log(S_0/K)+(r-\frac{1}{2}\sigma^2)T}{\sigma\sqrt{T}}\right),$$

where $Z$ is a standard Gaussian random variable with mean 0 and variance 1. Therefore

$$E_Q[\mathbf{1}_{\{S_T>K\}}]=N(d_2),$$

Where

$$N(d)=\frac{1}{\sqrt{2\pi}}\int_{-\infty}^{d}e^{-x^2/2}dx$$

And

$$d_2=\frac{\log(S_0/K)+(r-\frac{1}{2}\sigma^2)T}{\sigma\sqrt{T}}.$$

Thus

$$I_2=Ke^{-rT}N(d_2).$$

Compute $I_1$:

$$\begin{aligned}
I_1 &= E_Q\left[\frac{S_T}{B_T}\cdot\mathbf{1}_{\{S_T>K\}}\right]\\
&= E_Q\left[S_T^*\cdot\mathbf{1}_{\{S_T>K\}}\right]\\
&= \int_{\{S_T>K\}}S_T^*dQ.
\end{aligned}$$

Recall

$$dS_t^*=\sigma S_t^*d\widetilde{W}_t.$$

Thus $S_t^*$ is an exponential martingale, and so is $\frac{S_t^*}{S_0}$. In view of the facts that $\frac{S_t^*}{S_0}$ is an exponential martingale and $\left.\frac{S_t^*}{S_0}\right|_{t=0}=1$, define a new measure $\widetilde{\widetilde{P}}$ by first defining $\widetilde{\widetilde{P}}_t$ by

$$d\widetilde{\widetilde{P}}_t=\frac{S_t^*}{S_0}dQ$$

and then setting $\widetilde{\widetilde{P}}=\widetilde{\widetilde{P}}_T$. Thus by the machinery of Girsanov theorem, there exists $\widetilde{\widetilde{W}}_t$, which is a $\widetilde{\widetilde{P}}$-Brownian motion such that

$$d\widetilde{\widetilde{W}}_t=d\widetilde{W}_t-\sigma dt.$$

Thus

$$\widetilde{\widetilde{W}}_t=\widetilde{W}_t-\sigma t.$$

Now from the fact that

$$dS_t=S_t(rdt+\sigma d\widetilde{W}_t),$$

We have

$$\begin{aligned}
S_T &= S_0\exp\left[\left(r-\frac{1}{2}\sigma^2\right)T+\sigma\widetilde{W}_T\right]\\
&= S_0\exp\left[\left(r+\frac{1}{2}\sigma^2\right)T+\sigma\widetilde{\widetilde{W}}_T\right]
\end{aligned}$$

by (5.13). Hence $S_T>K$ if and only if

$$d_1=\frac{\log(S_0/K)+\left(r+\frac{1}{2}\sigma^2\right)T}{\sigma\sqrt{T}}>-\frac{\widetilde{\widetilde{W}}_T}{\sqrt{T}}=Z,$$

where $Z$ is a standard Gaussian random variable of mean 0 and variance 1. Therefore

$$\begin{aligned}
&E_Q\left[\frac{S_T}{B_T}\cdot\mathbf{1}_{\{S_T>K\}}\right]\\
&= E_Q\left[S_T^*\cdot\mathbf{1}_{\{S_T>K\}}\right]\\
&= S_0E_Q\left[\frac{S_T^*}{S_0}\cdot\mathbf{1}_{\{S_T>K\}}\right]\\
&= S_0\int_{\{S_T>K\}}\frac{S_T^*}{S_0}dQ\\
&= S_0\int_{\{S_T>K\}}d\widetilde{\widetilde{P}}\\
&= S_0\int_{\{Z<d_1\}}d\widetilde{\widetilde{P}}\\
&= S_0N(d_1).
\end{aligned}$$

Therefore we have

$$V_0=S_0N(d_1)-Ke^{-rT}N(d_2).$$

In general, by shifting time and conditioning everything at time $t$ one can obtain the following:

Theorem 5.8. The price $V_t$ at time $t$ of the European call option $X=(S_T-K)^+$ is given by

$$V_t=S_tN(d_1)-Ke^{-r(T-t)}N(d_2),$$

Where

$$\begin{aligned}
N(d) &= \frac{1}{\sqrt{2\pi}}\int_{-\infty}^{d}e^{-x^2/2}dx,\\
d_1 &= \frac{\log(S_t/K)+(r+\frac{1}{2}\sigma^2)(T-t)}{\sigma\sqrt{T-t}},\\
d_2 &= \frac{\log(S_t/K)+(r-\frac{1}{2}\sigma^2)(T-t)}{\sigma\sqrt{T-t}}.
\end{aligned}$$

Note also that Theorem 5.8 provides a valuable information on the replicating portfolio. Namely,

$$\begin{array}{rcl}
\xi_t &=& -Ke^{-rT}N(d_2),\\
\zeta_t &=& N(d_1).
\end{array}$$

The negative sign of $\xi_t$ indicates the short position of the riskless bond; the positive sign of $\zeta_t$ indicates the long position of the stock.

## The Black-Scholes Partial Differential Equation

The original derivation of the Black-Scholes formula Black and Scholes gave was via the so-called Black-Scholes partial differential equation. In this section, we present two derivations of the celebrated Black-Scholes PDE. The first one is via the martingale framework and the second without it.

### First Derivation of the Black-Scholes PDE

We use the notations and facts from the previous sections. Recall that in the risk-neutral world, i.e., with respect to the martingale measure, the discounted stock price process satisfies.

$$dS_t^*=\sigma S_t^*d\widetilde{W}_t,$$

Which is equivalent to

$$dS_t=S_t(rdt+\sigma d\widetilde{W}_t).$$

Let $(\xi_t, \zeta_t)$ be the self-financing portfolio consisting of $\xi_t$ units of riskless bond and $\zeta_t$ shares of stock that replicates the call option

$$X=(S_T-K)^+$$

with the expiry $T$ and the strick price $K$. The existence of such portfolio was already verified in section 5.3, and the discounted value $V_t^*$ of this portfolio is seen to satisfy

$$\begin{array}{rcl}
dV_t^* &=& \zeta_tdS_t^*\\
&=& \sigma\zeta_tS_t^*d\widetilde{W}_t.
\end{array}$$

Let us now assume that $V_t$ can be expressed as

$$V_t=C(t, S_t)$$

for some smooth deterministic function $C(t, S)$ of two variables $t$ and $S$. At this juncture, we do not yet know such function exists. But we will later show that such function indeed exists. Define $C^* = C^*(t, S_t)=C(t, S_t)/B_t=e^{-rt}C$. Then

$$\begin{aligned}
dC^* &= d(e^{-rt}C)\\
&= e^{-rt}dC-re^{-rt}Cdt\\
&= e^{-rt}\left[\frac{\partial C}{\partial t}dt+\frac{\partial C}{\partial S}dS_t+\frac{1}{2}\frac{\partial^2C}{\partial S^2}(dS_t)^2\right]-re^{-rt}Cdt.
\end{aligned}$$

The last equality is due to Ito's formula. It is to be noted that $\frac{\partial C}{\partial S}(t, S)$ is $\frac{\partial C}{\partial S}=\frac{\partial C}{\partial S}(t, S_t)$ and $C(t, S)$ is $C(t, S_t)$. The same applies to the $\frac{\partial C}{\partial t}$ and $\frac{\partial^2C}{\partial S^2}$. Collecting terms and using (5.14), we have

$$\begin{aligned}
dC^* &= e^{-rt}\left[\frac{\partial C}{\partial t}+rS_t\frac{\partial C}{\partial S}+\frac{1}{2}\sigma^2S_t^2\frac{\partial^2C}{\partial S^2}-rC\right]dt\\
&+ \sigma e^{-rt}S_t\frac{\partial C}{\partial S}d\widetilde{W}_t.
\end{aligned}$$

Thus utilizing (5.14) the necessary and sufficient condition for $C(t, S_t)$ to be equal to $V_t$ is that

$$\left.\frac{\partial C}{\partial t}+rS\frac{\partial C}{\partial S}+\frac{1}{2}\sigma^2S^2\frac{\partial^2C}{\partial S^2}-rC\right|_{t=t, S=S_t}=0$$

And

$$\sigma e^{-rt}S_t\frac{\partial C}{\partial S}=\sigma\zeta_tS_t^*.$$

Therefore by (5.17), we must have

$$\zeta_t=\frac{\partial C}{\partial S}=\frac{\partial C}{\partial S}(t, S_t)$$

and (5.16) says that the deterministic function $C(t, S)$ of two variables $t$ and S must satisfies the following partial differential equation

$$\frac{\partial C}{\partial t}+rS\frac{\partial C}{\partial S}+\frac{1}{2}\sigma^2S^2\frac{\partial^2C}{\partial S^2}-rC=0.$$

The reason for the validity of this partial differential equation is that $S_t$ can take any positive value therefore (5.19) must hold for any $t\geq0$ and $S$. (In fact it suffices to assume $S>0$. But it is a moot point here.) Now it is easy to see that the replication condition is

$$C(T, S)=(S-K)^+.$$

(5.18) is also very useful in that it gives a method or formula to calculate the number of shares of stock the replication portfolio is to have.

The promised proof of the existence of $C(t, S)$ satisfying (5.15) can now be seen very easily. Namely, suppose $C(t, S)$ is a deterministic function of two variables satisfying (5.19) and (5.20). Then by backtracking the arguments presented above, (5.15) can be easily seen to be satisfied by such $C(t, S)$. Thus the proof boils down to the existence of the solution of (5.19) and (5.20), which will be shown in the subsequent sections.

### Second Derivation of the Black-Scholes PDE

The derivation given above is the most succinct and conceptually cleanest derivation of the Black-Scholes PDE. The reader is advised to get familiar with this type of argument. However, it presupposes some knowledge of the risk-neutral valuation theory utilizing the martingale methodology. There is a way, however, to derive it directly without resorting to the martingale measure $Q$ and $Q$ Brownian motion $\widetilde{W}_t$. This also is the way Black and Scholes originally derived it. Let us present it here.

As before, the stock price process is assumed to satisfy

$$dS_t=S_t(\mu dt+\sigma dW_t),$$

where $W_t$ is a Brownian motion with respect to some Wiener measure $P$, usually called the underlying (physical) measure.

Let $X=(S_T-K)^+$ be a European call option, and let $(\xi_t, \zeta_t)$ be a self-financing portfolio consisting of $\xi_t$ units of riskless bond and $\zeta_t$ shares of stock that replicates $X$. Of course, it is far from trivial that such portfolio exists. The existence of such portfolio is part of the derivation process of the Black-Scholes PDE given in this subsection.

Let us for now assume such portfolio exists, and let

$$V_t=\xi_tB_t+\zeta_tS_t$$

be the value at time $t$ of such portfolio. Then the self-financing condition implies that $dV_t=\xi_tdB_t+\zeta_tdS_t$. Therefore,

$$\begin{aligned}
dV_t &= \xi_tdB_t+\zeta_tdS_t \\
&= re^{rt}\xi_tdt+\zeta_tS_t\left[\mu dt+\sigma dW_t\right] \\
&= \left[re^{rt}\xi_t+\mu\zeta_tS_t\right]dt+\sigma\zeta_tS_tdW_t.
\end{aligned}$$

As before, let us assume that $V_t$ can be expressed as

$$V_t=C(t, S_t)$$

for some smooth function $C(t, S)$ of two variables $t$ and $S$. Then by Ito's formula

$$\begin{aligned}
dC &= \frac{\partial C}{\partial t}dt+\frac{\partial C}{\partial S}dS_t+\frac{1}{2}\frac{\partial^2C}{\partial S^2}(dS_t)^2\\
&= \left[\frac{\partial C}{\partial t}+\mu S_t\frac{\partial C}{\partial S}+\frac{1}{2}\sigma^2S_t^2\frac{\partial^2C}{\partial S^2}\right]dt\\
&+ \sigma S_t\frac{\partial C}{\partial S}dW_t.
\end{aligned}$$

Equating (5.22) and (5.23) and collecting the coefficients of $dW_t$, we have

$$\zeta_t=\frac{\partial C}{\partial S}(t, S_t)$$

And

$$re^{rt}\xi_t+\mu\zeta_tS_t=\frac{\partial C}{\partial t}+\mu S_t\frac{\partial C}{\partial S}+\frac{1}{2}\sigma^2S_t^2\frac{\partial^2C}{\partial S^2}.$$

Since

$$V_t=C, \quad V_t=e^{rt}\xi_t+\zeta_tS_t\quad\mathrm{and}\quad\zeta_t=\frac{\partial C}{\partial S},$$

Plugging them into (5.21), we have

$$\xi_t=e^{-rt}\left[C(t, S_t)-S_t\frac{\partial C}{\partial S}(t, S_t)\right].$$

Plugging (5.24) and (5.26) into (5.25) and simplifying, we have

$$\left.\frac{\partial C}{\partial t}+rS\frac{\partial C}{\partial S}+\frac{1}{2}\sigma^2S^2\frac{\partial^2C}{\partial S^2}-rC\right|_{t=t, S=S_t}=0,$$

Which is exactly what we have derived before. Therefore the Black Scholes PDE (5.19) must also hold.

Note that in the Black-Scholes PDE, the drift coefficient $\mu$ disappears and in its stead the riskless interest rate $r$ appears. By the same token, the physical measure $P$ plays no role but the martingale measure $Q$ is what matters.

Let us now give an argument for the promised existence of the self-financing portfolio. Let $C$ be the solution of the Black-Scholes PDE (5.19) satisfying the condition

$$C(T, S)=(S-K)^+.$$

As suggested by (5.24), define $\zeta_t$ by

$$\zeta_t=\frac{\partial C}{\partial S}(t, S_t),$$

and $\xi_t$, as in (5.26), by

$$\xi_t=e^{-rt}\left[C(t, S_t)-S_t\frac{\partial C}{\partial S}(t, S_t)\right].$$

Construct a portfolio consisting of $\xi_t$ units of riskless bond and $\zeta_t$ shares of stock. Then it is trivial to see that

$$\begin{array}{rcl}
V_t &=& e^{rt}\xi_t+\zeta_tS_t\\
&=& C\\
&=& C(t, S_t).
\end{array}$$

Let us now prove the self-financing property of this portfolio. Rewriting the Black-Scholes PDE by

$$\frac{\partial C}{\partial t}+\mu S_t\frac{\partial C}{\partial S}+\frac{1}{2}\sigma^2S_t^2\frac{\partial^2C}{\partial S^2}=(\mu-r)S_t\frac{\partial C}{\partial S}+rC$$

And plugging this into (5.23), we have

$$\begin{array}{rcl}
dV_t &=& dC(t, S_t)\\
&=& \left[(\mu-r)S_t\frac{\partial C}{\partial S}+rC\right]dt+\sigma S_t\frac{\partial C}{\partial S}dW_t.
\end{array}$$

Using $\zeta_t=\frac{\partial C}{\partial S}$ and plugging (5.31) into the above equation, we then have

$$\begin{aligned}
dV_t &= dC \\
&= \left[(\mu-r)\zeta_tS_t+r(\xi_te^{rt}+\zeta_tS_t)\right]dt+\sigma\zeta_tS_tdW_t \\
&= r\xi_te^{rt}dt+\zeta_tS_t\left[\mu dt+\sigma dW_t\right] \\
&= \xi_tdB_t+\zeta_tdS_t
\end{aligned}$$

Which is the self-financing condition we were after. The replicating condition is trivially satisfied by (5.28).

## Solution of the Black-Scholes PDE

Now solve the Black-Scholes PDE (5.19) subject to the condition (5.20). Let $S_0$ be the constant that represents the known stock price at time $t=0$. Define $z=\log\left(S/S_0\right)$ and $\widetilde{C}(t, z)=C(t, S)$. Then:

$$\begin{array}{rcl}
\frac{\partial\widetilde{C}}{\partial z} &=& S\frac{\partial C}{\partial S},\\
\frac{\partial^2\widetilde{C}}{\partial z^2} &=& S^2\frac{\partial^2C}{\partial S^2}+S\frac{\partial C}{\partial S}.
\end{array}$$

Therefore, Black-Scholes equation becomes

$$\frac{\partial\widetilde{C}}{\partial t}+\left(r-\frac{1}{2}\sigma^2\right)\frac{\partial\widetilde{C}}{\partial z}+\frac{1}{2}\sigma^2\frac{\partial^2\widetilde{C}}{\partial z^2}-r\widetilde{C}=0.$$

Now let $x=Az+Bt$, where $A$ and $B$ are constant to be determined. Let

$$v(t, x)=\widetilde{C}(t, z)=C(t, S).$$

Then

$$\begin{aligned}
\frac{\partial\widetilde{C}}{\partial t} &= \frac{\partial v}{\partial t}+\frac{\partial v}{\partial x}\frac{\partial x}{\partial t}=\frac{\partial v}{\partial t}+B\frac{\partial v}{\partial x},\\
\frac{\partial\widetilde{C}}{\partial z} &= \frac{\partial v}{\partial t}\frac{\partial t}{\partial z}+\frac{\partial v}{\partial x}\frac{\partial x}{\partial z}=A\frac{\partial v}{\partial x},\\
\frac{\partial^2\widetilde{C}}{\partial z^2} &= A^2\frac{\partial^2v}{\partial x^2}.
\end{aligned}$$

Therefore (5.32) becomes

$$\frac{\partial v}{\partial t}+\left(B+\left(r-\frac{1}{2}\sigma^2\right)A\right)\frac{\partial v}{\partial x}+\frac{1}{2}\sigma^2A^2\frac{\partial^2v}{\partial x^2}-rv=0.$$

Let us choose $A$ and $B$ so that

$$B+\left(r-\frac{1}{2}\sigma^2\right)A=0\quad\mathrm{and}\quad\sigma A=1,$$

i.e.,

$$A=\frac{1}{\sigma}\quad\text{and}\quad B=-\frac{1}{\sigma}\left(r-\frac{1}{2}\sigma^2\right).$$

Then (5.33) becomes

$$\frac{\partial v}{\partial t}+\frac{1}{2}\frac{\partial^2v}{\partial x^2}-rv=0.$$

Define

$$u(t, x)=e^{-rt}v(t, x),$$

Then (5.35) becomes

$$\frac{\partial u}{\partial t}+\frac{1}{2}\frac{\partial^2u}{\partial x^2}=0.$$

If we replace $A$ and $B$ in (5.34) then:

$$x=\frac{1}{\sigma}z-\frac{1}{\sigma}\left(r-\frac{1}{2}\sigma^2\right)t,$$

And so

$$z=\left(r-\frac{1}{2}\sigma^2\right)t+\sigma x.$$

Back to the first change of variable, we have

$$\begin{array}{rcl}
S &=& S_0e^z\\
&=& S_0\exp\left(\left(r-\frac{1}{2}\sigma^2\right)t+\sigma x\right).
\end{array}$$

In conclusion, if $u$ is defined by

$$u(t, x)=e^{-rt}v(t, x)=e^{-rt}C(t, S),$$

$u$ satisfies the following heat equation initial boundary problem:

$$\left\{\begin{array}{l}
\frac{\partial u}{\partial t}+\frac{1}{2}\frac{\partial^2u}{\partial x^2}=0\\\\
u(T, x)=e^{-rT}C(T, S)
\end{array}\right.$$

where $x$ and $S$ are related by

$$S=S_0\exp\left(\left(r-\frac{1}{2}\sigma^2\right)t+\sigma x\right).$$

The equation in (5.38) is the so-called heat equation, but with the time seemingly flowing backward. However, if we make one more substitution $\tau = T-t$ for time, (5.38) becomes an equation for $u(\tau, x)$ satisfying

$$\left\{\begin{array}{l}
\frac{\partial u}{\partial\tau}=\frac{1}{2}\frac{\partial^2u}{\partial x^2}\\\\
u(0, x)=e^{-rT}C(T, S).
\end{array}\right.$$

This is the usual form of the initial value problem of the heat equation. In other words, (5.38) is the correct, well-posed heat equation because the initial condition $u(T, x)=e^{-rT}C(T, S)$ is posed at a future time while we are interested in the solution at times before that fixed future time. Incidentally, in finance literature, (5.38) is called the boundary value problem. It is a well known fact from the theory of parabolic (heat) equations that the solution $u(t, x)$ of (5.38) can be written as

$$u(t, x)=\int_{-\infty}^{\infty}\frac{1}{\sqrt{2\pi(T-t)}}e^{-\frac{(x-y)^2}{2(T-t)}}u(T, y)dy.$$

Here the function

$$\frac{1}{\sqrt{2\pi(T-t)}}e^{-\frac{(x-y)^2}{2(T-t)}}$$

is called the heat kernel (for (5.38)) and its probabilistic meaning is that it represents the probability density function for a Brownian particle (motion) to move from $y$ to $x$ in time $T-t$.

Let us now derive the value of the European call option. Since the stock price at time $t=0$ is $S_0$, it must be $C(0, S_0)$. It is easily seen from (5.37) that this case corresponds to the case in which $t=0$ and $x=0$. Namely, by (5.40) the option's value at time $t=0$ is nothing but

$$u(0, 0)=\int_{-\infty}^{\infty}\frac{1}{\sqrt{2\pi T}}e^{-\frac{x^2}{2T}}u(T, x)dx.$$

We now derive the Black-Scholes formula for the call option. Note that

$$u(T, x)=e^{-rT}(S_T-K)^+.$$

By (5.41),

$$u(0, 0)=\int_{-\infty}^{\infty}\frac{1}{\sqrt{2\pi T}}e^{-\frac{x^2}{2T}}e^{-rT}(S_T-K)^+dx,$$

where at $T$, $S_T$ and $x$ are related by

$$S_T=S_0\exp\left(\left(r-\frac{1}{2}\sigma^2\right)T+\sigma x\right).$$

One can compute $u(0, 0)$ as follows:

$$\begin{aligned}
u(0, 0) &= e^{-rT}\int_{D}\frac{1}{\sqrt{2\pi T}}e^{-\frac{x^2}{2T}}\left(S_0\exp\left(\left(r-\frac{1}{2}\sigma^2\right)T+\sigma x\right)-K\right)dx \\
&= e^{-rT}\int_{D}\frac{1}{\sqrt{2\pi T}}e^{-\frac{x^2}{2T}}S_0\exp\left(\left(r-\frac{1}{2}\sigma^2\right)T+\sigma x\right)dx \\
&- Ke^{-rT}\int_{D}\frac{1}{\sqrt{2\pi T}}e^{-\frac{x^2}{2T}}dx \\
&= I_1-Ke^{-rT}I_2
\end{aligned}$$

Where

$$\begin{aligned}
D &= \left\{x:S_0\exp\left(\left(r-\frac{1}{2}\sigma^2\right)T+\sigma x\right)>K\right\},\\
I_1 &= e^{-rT}\int_{D}\frac{1}{\sqrt{2\pi T}}e^{-\frac{x^2}{2T}}S_0\exp\left(\left(r-\frac{1}{2}\sigma^2\right)T+\sigma x\right)dx,\\
I_2 &= \int_{D}\frac{1}{\sqrt{2\pi T}}e^{-\frac{x^2}{2T}}dx.
\end{aligned}$$

### Compute $I_2$

Put $y=\frac{x}{\sqrt{T}}$ then

$$\begin{aligned}
D &= \left\{x:S_0\exp\left(\left(r-\frac{1}{2}\sigma^2\right)T+\sigma x\right)>K\right\}\\
&= \left\{y:y>-\frac{\log(S_0/K)+(r-\frac{1}{2}\sigma^2)T}{\sigma\sqrt{T}}\right\}
\end{aligned}$$

And

$$\begin{aligned}
I_2 &= \int_{D}\frac{1}{\sqrt{2\pi}}e^{-\frac{y^2}{2}}dy \\
&= \int_{-\frac{\log(S_0/K)+(r-\frac{1}{2}\sigma^2)T}{\sigma\sqrt{T}}}^{\infty}\frac{1}{\sqrt{2\pi}}e^{-\frac{y^2}{2}}dy \\
&= \int_{-\infty}^{\frac{\log(S_0/K)+(r-\frac{1}{2}\sigma^2)T}{\sigma\sqrt{T}}}\frac{1}{\sqrt{2\pi}}e^{-\frac{y^2}{2}}dy \\
&= N\left(\frac{\log(S_0/K)+(r-\frac{1}{2}\sigma^2)T}{\sigma\sqrt{T}}\right).
\end{aligned}$$

### Compute $I_1$

Put $y=\frac{x-\sigma T}{\sqrt{T}}$ then

$$\begin{aligned}
D &= \left\{x:S_0\exp\left(\left(r-\frac{1}{2}\sigma^2\right)T+\sigma x\right)>K\right\}\\
&= \left\{y:y>-\frac{\log(S_0/K)+(r+\frac{1}{2}\sigma^2)T}{\sigma\sqrt{T}}\right\}
\end{aligned}$$

And

$$\begin{gathered}
I_1 = S_0\int_{D}\frac{1}{\sqrt{2\pi T}}\exp\left(-\frac{1}{2}\left(\frac{x-\sigma T}{\sqrt{T}}\right)^2\right)dx \\
= S_0\int_{-\frac{\log(S_0/K)+(r+\frac{1}{2}\sigma^2)T}{\sigma\sqrt{T}}}^{\infty}\frac{1}{\sqrt{2\pi}}e^{-\frac{y^2}{2}}dy \\
= S_0\int_{-\infty}^{\frac{\log(S_0/K)+(r+\frac{1}{2}\sigma^2)T}{\sigma\sqrt{T}}}\frac{1}{\sqrt{2\pi}}e^{-\frac{y^2}{2}}dy \\
= S_0N\left(\frac{\log(S_0/K)+(r+\frac{1}{2}\sigma^2)T}{\sigma\sqrt{T}}\right).
\end{gathered}$$

Therefore, we can obtain the following:

$$C(0, S_0)=S_0N(d_1)-e^{-rT}KN(d_2),$$

Where

$$\begin{gathered}
d_1 = \frac{\log(S_0/K)+(r+\frac{1}{2}\sigma^2)T}{\sigma\sqrt{T}},\\
d_2 = \frac{\log(S_0/K)+(r-\frac{1}{2}\sigma^2)T}{\sigma\sqrt{T}}.
\end{gathered}$$

In general, if we know the value $S_t$ at time $t$, then we can apply the same formula to get

$$C(t, S_t)=S_tN(d_1)-e^{-r(T-t)}KN(d_2),$$

where $T-t$ is the time to expiry from time $t$ and

$$\begin{aligned}
d_1 &= \frac{\log(S_t/K)+(r+\frac{1}{2}\sigma^2)(T-t)}{\sigma\sqrt{T-t}},\\
d_2 &= \frac{\log(S_t/K)+(r-\frac{1}{2}\sigma^2)(T-t)}{\sigma\sqrt{T-t}}.
\end{aligned}$$

Note also that (5.43) provides a valuable information on the replicating portfolio. Namely,

$$\left\{\begin{array}{ll}
\xi_t = -Ke^{-rT}N(d_2),\\
\zeta_t = N(d_1).
\end{array}\right.$$

The negative sign of $\xi_t$ indicates the short position of the riskless bond; the positive sign of $\zeta_t$ indicates the long position of the stock.

## Put-Call Parity

Let $X$ be the European call option with the expiry $T$ and the strike price $K$, i.e.,

$$X=(S_T-K)^+$$

as $\mathcal{F}_T$ measurable random variables. Let $C_t$ be its value at time $t$. Then the risk-neutral valuation principle, Theorem 5.7, says that

$$C_t=B_tE_Q\left[\frac{X}{B_T}\mid\mathcal{F}_t\right],$$

where $Q$ is the martingale measure. Let $Y$ be the European put option with the same expiry $T$ and the same strike price $K$. Namely, $Y = (K - S_T)^+$. Then these call and put options are intricately linked via a principle called the "put-call parity." Let $P_t$ be the value of $Y$ at time $t$, then Theorem 5.7 says that

$$P_t=B_tE_Q\left[\frac{Y}{B_T}\mid\mathcal{F}_t\right].$$

Note now that

$$C_T-P_T=X-Y=S_T-K.$$

Therefore, upon applying the risk-neutral valuation principle, Theorem 5.7, to the above, we have

$$\begin{aligned}
C_t-P_t &= B_tE_Q\left[\frac{X-Y}{B_T}\mid\mathcal{F}_t\right] \\
&= B_tE_Q\left[\frac{S_T}{B_T}\mid\mathcal{F}_t\right]-B_tE_Q\left[\frac{K}{B_T}\mid\mathcal{F}_t\right] \\
&= S_t-Ke^{-r(T-t)}.
\end{aligned}$$

![500](Attachments/500-98.png)

Figure 5.10: Payoff of $C_T$

![500](Attachments/500-97.png)

Figure 5.11: Payoff of $P_T$

![500](Attachments/500-99.png)

Figure 5.12: Payoff of $C_T-P_T$

The last equality is the consequence of the fact that $S_t^*=S_t/B_t$ is a $Q$-martingale and that $B_t=e^{rt}$. (5.45) combined with the Black-Scholes formula (5.43) gives the Black-Scholes formula for put option. From (5.45), we have

$$\begin{aligned}
P_t &= C_t-S_t+Ke^{-r(T-t)}\\
&= -S_t\left(1-N(d_1)\right)+Ke^{-r(T-t)}\left(1-N(d_2)\right)\\
&= -S_tN(-d_1)+Ke^{-r(T-t)}N(-d_2)
\end{aligned}$$

Where

$$\begin{aligned}
d_1 &= \frac{\log(S_t/K)+(r+\frac{1}{2}\sigma^2)(T-t)}{\sigma\sqrt{T-t}},\\
d_2 &= \frac{\log(S_t/K)+(r-\frac{1}{2}\sigma^2)(T-t)}{\sigma\sqrt{T-t}}.
\end{aligned}$$

Here we used the fact that

$$1-N(d)=N(-d)$$

for the cumulative normal distribution $N(d)$.

This Black-Scholes formula also gives the replicating portfolio $(\xi_t, \zeta_t)$ for the put option that consists of $\xi_t$ units of riskless bond and $\zeta_t$ shares of stock by

$$\left\{\begin{array}{ll}
\xi_t = Ke^{-rT}N(-d_2),\\
\zeta_t = -N(-d_1).
\end{array}\right.$$

## Appendix

![500](Attachments/500-102.png)

Figure 5.2: 1-day percentage changes of KOSPI 200.

![500](Attachments/500-103.png)

Figure 5.3: 1-day percentage changes of KOSPI 200 with Normal Distribution Approximation.

![500](Attachments/500-107.png)

Figure 5.4: 2-day percentage changes of KOSPI 200 with Normal Distribution Approximation

![500](Attachments/500-105.png)

Figure 5.5: 3-day percentage changes of KOSPI 200 with Normal Distribution Approximation

![500](Attachments/500-108.png)

Figure 5.6: 5-day percentage changes of KOSPI 200 with Normal Distribution Approximation

![500](Attachments/500-104.png)

Figure 5.7: 7-day percentage changes of KOSPI 200 with Normal Distribution Approximation.

![500](Attachments/500-106.png)

Figure 5.8: Overlaid normal distributions.

![500](Attachments/500-100.png)

Figure 5.9: Change of the $h$-day Volatilities
---
title: Some Applications of the Fundamental Theorem
chapter: 13
subject: Financial Engineering
category: Principles of Financial Engineering
tags:
- american
- asian
- barrier
- bid-ask
- binomial
- black-scholes
- bond
- brownian
- call
- cap
- counterparty
- credit-risk
- currency
- defi
- digital
- dividend-yield
- european
- exchange-rate
- exotic
- factor-model
- forward
- future
- gbm
- greeks
- interest-rate
- ito
- libor
- liquidity
- monte-carlo
- multiple
- option
- pde
- put
- regression
- risk-free-rate
- sde
- stochastic
- stock
- transaction-cost
- var
- yield-curve
key_concepts:
- American options valuation
- Backtesting VaR models
- Backward induction algorithm
- Binomial option pricing model
- Convergence to Black-Scholes
- Cox-Ross-Rubinstein framework
- Delta risk management
- Derivative securities
- Dynamic hedging strategies
- Expected Shortfall calculation
- Financial risk management
- Gamma effects on options
- Historical simulation VaR
- Lattice methods for derivatives
- Monte Carlo VaR
- Multi-period binomial tree
- Options Greeks measurement
- Parametric VaR models
- Portfolio optimization
- Portfolio risk hedging
- Quantitative financial analysis
- Regulatory VaR requirements
- Rho interest rate sensitivity
- Risk assessment and mitigation
- Risk-neutral probability
- Theta time decay
- VaR model validation
- Value $\$a_t$$ Risk (VaR) methodology
- Vega volatility sensitivity
---

# SOME APPLICATIONS OF THE FUNDAMENTAL THEOREM
# CHAPTER OUTLINE
[^13]: 1 Introduction . 428
[^13]: 2 Application 1: The Monte Carlo Approach. 429
[^13]: 2.1 Pricing with Monte Carlo . 430
[^13]: 2.1.1 Pricing a call with constant spot rate . 431
[^13]: 2.2 Pricing Binary FX Options. 433
[^13]: 2.2.1 Obtaining the risk-neutral dynamics . 433
[^13]: 2.2.2 Monte Carlo process. 435
[^13]: 2.3 Path Dependency . 436
[^13]: 2.4 Discretization Bias and Closed Forms. 438
[^13]: 2.5 Real-Life Complications . 438
[^13]: 3 Application 2: Calibration . 438
[^13]: 3.1 Calibrating a Tree . 439
[^13]: 3.2 Extracting a LIBOR Tree. 439
[^13]: 3.2.1 Pricing functions . 439
[^13]: 3.3 Obtaining the BDT Tree. 441
[^13]: 3.3.1 Specifying the dynamics . 441
[^13]: 3.3.2 The variance of Li . 441
[^13]: 3.4 Calibrating the Tree . 443
[^13]: 3.5 Uses of the Tree 445
[^13]: 3.5.1 Application: pricing a cap . 445
[^13]: 3.5.2 Some assumptions of the model . 447
[^13]: 3.5.3 Remarks . 447
[^13]: 3.6 Real-World Complications . 448
[^13]: 4 Application 3: Quantos . 448
[^13]: 4.1 Pricing Quantos. 448
[^13]: 4.2 The PDE Approach . 451
[^13]: 4.2.1 A PDE for quantos. 452
[^13]: 4.3 Quanto Forward. 453
[^13]: 4.4 Quanto Option. 453
[^13]: 4.4.1 Black-Scholes and dividends. 454
[^13]: 4.5 How to Hedge Quantos. 454
[^13]: 4.6 Real-Life Considerations . 454
[^13]: 5 Conclusions. 455
Suggested Reading . 455
Exercises . 455
EXCEL Exercises . 456
MATLAB Exercises. 457

# 13.1 INTRODUCTION
The theorem discussed in the previous chapter establishes important no-arbitrage conditions that permit pricing and risk management using Martingale methods. According to these conditions, given unique arbitrage-free state prices, we can obtain a synthetic probability measure, $\tilde{P}$, under which all asset prices normalized by a particular $Z_{t}$ become Martingales. Letting $C(S_{t}, t)$ represent a security whose price depends on an underlying risk $S_{t}$, we can write,
$$
\frac{C(S_{t}, t)}{Z_{t}} = E_{t}^{\tilde{P}}\left[\frac{C(S_{T}, T)}{Z_{T}}\right]
$$

As long as positive state prices exist, many such probabilities can be found and each will be associated with a particular normalization. The choice of the right working probability then becomes a matter of convenience and data availability.

The equality in Eq. (13.1) can be evaluated numerically using various methods. The arbitrage-free price $S_{t}$ can be calculated by evaluating the expectation and then multiplying by $Z_{t}$. But to evaluate the expectation, we would need the probability $\tilde{P}$, hence, this must be obtained first. A further desirable characteristic is that the future value, $Z_{T}$, be constant, as it would be in the case of a default-free bond that matures $\$a_t$$ time $T$. Hence, $T$ maturity bonds are good candidates for normalization.

In this chapter, we show three applications of the fundamental theorem. The first application is the Monte Carlo procedure which can be interpreted as a general method to calculate the expectation in Eq. (13.1). This method can be applied straightforwardly when instruments under consideration are of European type. The procedure uses the tools supplied by the fundamental theorem together with the law of large numbers.

The second application of the fundamental theorem involves calibration. Calibration is the selection of model parameters using observed arbitrage-free prices from liquid markets. The chapter discusses simple examples of how to calibrate stochastic differential equations and tree models to market data using the fundamental theorem. This is done within the context of the Black Derman Toy (BDT) model.

The third application of the fundamental theorem introduced in Chapter 12 is more conceptual in nature. We use quanto assets to show how the theorem can be exploited in modeling. Quanto assets provide an excellent vehicle for this, since their pricing involves switches between domestic and foreign risk-neutral measures. Techniques for switching between measures are an integral part of financial engineering and will be discussed further in the next chapter. The application to quantos provides the first step.

Before we discuss these issues, a note of caution is in order. The discussion in this chapter should be regarded as an overview that presents examples for when to use the fundamental theorem, instead of being a source of how to implement such numerical techniques. Calculations using Monte Carlo or calibration are complex numerical procedures, and a straightforward application may not give satisfactory results. Interested readers can consult the sources provided $\$a_t$$ the end of the chapter.

# 13.2 APPLICATION 1: THE MONTE CARLO APPROACH
Consider again the expectation involving a function $C(S_{t}, t)$ of the underlying risk $S_{t}$ under a working Martingale measure, $\tilde{P}$:
$$
\frac{C(S_{t}, t)}{Z_{t}} = E_{t}^{\tilde{P}}\left[\frac{C(S_{T}, T)}{Z_{T}}\right]
$$

where $S_{t}$ and $Z_{t}$ are two arbitrage-free asset prices $\$a_t$$ time $t$. $Z_{t}$ is used as the normalizing asset and is instrumental in defining $\tilde{P}$. $C(S_{t}, t)$ may represent a European option premium or any other derivative that depends on $S_{t}$ with expiration $T$.

This equation can be used as a vehicle to calculate a numerical value for $C(S_{t}, t)$, if we are given the probability measure $\tilde{P}$ and if we know $Z_{t}$. There are two ways of doing this. First, we can try to solve analytically for the expectation and obtain the resulting $C(S_{t}, t)$ as a closed-form formula. When the current value of the normalizing asset, $Z_{t}$, is known, this would amount to taking the integral:
$$
C(S_{t}, t) = Z_{t}\left[\int_{-\infty}^{\infty}\int_{-\infty}^{\infty}\frac{C(S_{T}, T)}{Z_{T}}\tilde{f}(S_{T}, Z_{T})\mathrm{d}S_{T}\mathrm{d}Z_{T}\right]
$$

where $\tilde{f}(.)$ is the joint conditional probability density function of $S_{T}, Z_{T}$ in terms of the $\tilde{P}$ probability. $Z_{T}$ on the right-hand side is considered to be random and possibly correlated with $S_{T}$. As a result, the probability $\tilde{P}$ would apply to both random variables, $S_{T}$ and $Z_{T}$.

With judicious choices of $Z_{t}$, we can however make $Z_{T}$ a constant. For example, if we choose $Z_{t}$ as the default-free discount bond that matures $\$a_t$$ time $T$,
$$
Z_{T} = 1
$$

It is clear that such normalization greatly simplifies the pricing exercise, since $\tilde{f}(.)$ is then a univariate conditional density.

But, even with this there is a problem with the analytical method. Often, there are no closed-form solutions for the integrals, and a nice formula tying $S_{t}$ to $Z_{t}$ and other parameters of the distribution function $\tilde{P}$ may not exist. The value of the integral can still be calculated, although not through a closed-form formula. It has to be evaluated numerically.

One way of doing this is the Monte Carlo method. This section briefly summarizes the procedure. We begin with a simple example. Suppose a random variable, $X$, with a known normal distribution denoted by $P$, is given:
$$
X \sim N(\mu, \sigma)
$$

Suppose we have a known function $g(X)$ of $X$. How would we calculate the expectation $E^{P}[g(X)]$, knowing that $E^{P}[g(X)] < \infty$? One way, of course, is by using the analytical approach mentioned earlier. Take the integral
$$
E^{P}[g(X)] = \int_{-\infty}^{\infty}g(x)\left(\frac{1}{\sqrt{2\pi\sigma^{2}}}e^{-(1/2\sigma^{2})(x-\mu)^{2}}\right)\mathrm{d}x
$$

if a closed-form solution exists.

But there is a second, easier way. We can invoke the law of large numbers and realize that given a large sample of realizations of $X$, denoted by $x_{i}$, the sample mean of any function of the $x_{i}$, say $g(x_{i})$, will be close to the true expected value $E^{P}[g(X)]$. So, the task of calculating an arbitrarily good approximation of $E^{P}[g(X)]$ reduces to drawing a very large sample of $x_{i}$ from the right distribution. Using random number generators, and the known distribution function of $X$, we can obtain $N$ replicas of $x_{i}$. These would be generated independently, and the law of large numbers would apply:

$$
\lim_{N \to \infty} \frac{1}{N}\sum_{i=1}^{N}g(x_{i}) = E^{P}[g(X)]
$$

a.s. (almost surely).

This means that for finite $N$,
$$
\overline{g(x)} = \frac{1}{N}\sum_{i=1}^{N}g(x_{i})
$$

would be an approximation to the true expectation. In fact, one can calculate the (finite sample) moments of $\overline{g(x)}$ and determine the error bounds. Thus, with a properly selected probability (e.g., risk-neutral measure) and with a judiciously chosen normalizing asset, the expectation in Eq. (13.2) can be calculated using the same approach.

The term "Monte Carlo" comes from the fact that the procedure generates random paths that are similar to games of chance in gambling. This suggests that the Monte Carlo method is a viable technique for calculating expectations when the latter do not permit closed-form solutions, especially when only an approximation is sought. The method is general and can be applied to calculating any expectation under all types of probability distributions. But still, to apply this general framework to asset pricing, a knowledge of the probability $\tilde{P}$ is necessary. At various steps of the Monte Carlo procedure used in practice, utilization of the probability measure $\tilde{P}$ introduced by the fundamental theorem is often implicit.

We have seen the fundamental theorem tells us that the $\tilde{P}$ exists and has some desirable properties. However, the theorem does not pin down a unique $\tilde{P}$, depending on the chosen normalization. Also, depending on the asset under consideration, there may actually be several convenient probabilities that can be used. Thus, the application of Monte Carlo to pricing requires a good understanding of the fundamental theorem, risk-neutral measures, and the relation of $\tilde{P}$ to observed data.

# 13.2.1 PRICING WITH MONTE CARLO
Now, consider the general case of pricing financial assets. According to the fundamental theorem of asset pricing, we can write
$$
\frac{C(S_{t}, t)}{B(t, T)} = E_{t}^{\tilde{P}}\left[C(S_{T}, T)\right]
$$

Here, $B(t, T)$ is the value $\$a_t$$ time $t$ of a risk-free discount bond that matures $$a_t$$ time $T$. Thus, we have
$$
Z_{t} = B(t, T)
$$
$$
Z_{T} = 1
$$

$S_{t}$ is the price of the underlying instrument and $C(S_{t}, t)$ is any derivative written on it. For example, $C(S_{t}, t)$ can be a plain vanilla call, in which case,
$$
C(S_{T}, T) = \max[S_{T} - K, 0]
$$

But the method is much more general. We can value various types of exotic options as well. The only restriction is that the option should not have any early exercise clauses. Such American-style options need to be priced using backward induction methods since $\$a_t$$ any point in time, there is a need to check whether it is optimal to exercise the option or not. With Monte Carlo, we generate future paths for the underlying risk, and this can be done only in a "forward" fashion. During this process, there is no way to check if early exercise is optimal. But the Monte Carlo approach can be used with exotic options that have a path-dependent structure, if they are of European type. Finally, once an expectation is to be calculated, the method is general; the underlying probability can be continuous or discrete, univariate or multivariate.

We will discuss the use of Monte Carlo with a simple example.

# 13.2.1.1 Pricing a call with constant spot rate
We consider a plain vanilla European call option $C(S_{t}, t)$, written on the stock $S_{t}$. The call has strike $K$ and expiration $T$. At expiration, the value of the call will be
$$
C(S_{T}, T) = \max[S_{T} - K, 0]
$$

and, according to the fundamental theorem
$$
C(S_{t}, t) = B(t, T)E_{t}^{\tilde{P}}[\max[S_{T} - K, 0]]
$$

To calculate the current value of the call $C(S_{t}, t)$, we need to evaluate the expectation on the right-hand side. We need to do the following:

[^1]: Display the arbitrage-free dynamics of $S_{t}$ under the probability $\tilde{P}$.
[^2]: Using the dynamics from step 1, obtain as many future paths for $S_{t}$ as needed. Since the call has European-style exercise, only the values $\$a_t$$ expiration date, $S_{T}$, are relevant and need to be calculated.
[^3]: Calculate the $\max[S^{i}_{T} - K, 0]$ for each simulated path $i$ and then take the average.

The last step will involve the approximation formula
$$
E_{t}^{\tilde{P}}[\max[S_{T} - K, 0]] \cong \frac{1}{n}\sum_{i=1}^{n}\max[S^{i}_{T} - K, 0]
$$

We now provide details for each of these steps.

Step 1 requires displaying $S_{t}$ dynamics under the risk-neutral probability $\tilde{P}$.

When we discussed the fundamental theorem, we saw that when we normalize asset prices with a $T$-maturity pure discount bond price, the asset prices become martingales under $\tilde{P}$. In a sense, the $\tilde{P}$ selected this way is a risk-neutral probability.

We have from the fundamental theorem
$$
\frac{S_{t}}{B(t, T)} = E_{t}^{\tilde{P}}\left[\frac{S_{u}}{B(u, T)}\right]
$$

where $t < u$. But the price of bond $B(t, T)$ is given by
$$
B(t, T) = e^{-r(T-t)}
$$

where $r$ is the constant spot rate. Then we get from Eq. (13.13)
$$
S_{t} = e^{-r(u-t)}E_{t}^{\tilde{P}}[S_{u}]
$$

This can be rewritten, after rearranging, as
$$
E_{t}^{\tilde{P}}[S_{u}] = S_{t}e^{r(u-t)}
$$

The last equation says that the expected return on the stock equals the risk-free rate under the probability $\tilde{P}$. With the normalization by a default-free bond, the risk-neutral probability makes the expected returns of all assets equal to the risk-free rate.

But, this still does not provide the dynamics of $S_{t}$. We need this to generate Monte Carlo paths. Arbitrage-free dynamics are given by the stochastic differential equation (SDE):
$$
\mathrm{d}S_{t} = rS_{t}\mathrm{d}t + \sigma S_{t}\mathrm{d}W^{\tilde{P}}_{t}
$$

where $\mathrm{d}W^{\tilde{P}}_{t}$ is an infinitesimal increment in a Wiener process defined using the probability measure $\tilde{P}$.

We now have access to the arbitrage-free dynamics of the underlying defined with the probability $\tilde{P}$. In step 2, we generate the paths of $S_{t}$ using the risk-neutral dynamics. The equation
$$
\mathrm{d}S_{t} = rS_{t}\mathrm{d}t + \sigma S_{t}\mathrm{d}W^{\tilde{P}}_{t}
$$

can be written
$$
\frac{\mathrm{d}S_{t}}{S_{t}} = r\mathrm{d}t + \sigma\mathrm{d}W^{\tilde{P}}_{t}
$$

To generate paths, we need to discretize this SDE. In discrete time, over finite intervals $\\Delta$, we obtain the approximation
$$
\Delta S_{t_{i}} = rS_{t_{i-1}}\Delta + \sigma S_{t_{i-1}}\sqrt{\Delta}z_{i}
$$

where $z_{i}$ is a random variable drawn from a standard normal distribution with mean zero and variance one. Hence $z_{i}$ has the same distribution as a normally distributed $\frac{\\Delta W_{t}}{\sqrt{\\Delta}}$. Also, by discretizing the SDE we always incur some level of error. This error is known as discretization bias or error. Finally, the Monte Carlo approach involves statistical error as well, although this can be decreased by increasing the number of simulated trajectories.

Further, if volatility is a function of time or of the value of $S$, these can be approximated by replacing $\\sigma$ by $\\sigma(t_{i}, S_{t_{i}})$. However, note that in such a case, where the volatility parameter becomes a function of the underlying itself, the discretization bias is much greater.

According to Eq. (13.20), once we draw a series of normally distributed random numbers $\{z_{j}\}$, we can obtain "paths" for $S_{t_j}$ for times $t_{j} = t + j\\Delta$, where $j = 1, \ldots, n$. In particular,
$$
S_{t_{j+1}} = S_{t_{j}} + rS_{t_{j}}\Delta + \sigma S_{t_{j}}\sqrt{\Delta}z_{j+1}
$$

At the initial point $t_{0} = t$, the value $S_{t}$ is known. Using random number generators, we can draw a random value for $z_{1}$ and then use Eq. (13.21) to calculate $S_{t_{1}}$. Using $S_{t_{1}}$ and a new random number $z_{2}$, we can obtain $S_{t_{2}}$ from the same equation. Continuing this way until time $T$, we get a path $S_{t_{j}}$, $j = 1, \ldots, n$. Note that to value the particular European call, only the value of $S_{T}$ is needed, since early exercise is not allowed.

Repeating this procedure many times, we obtain paths, $\{S^{i}_{t_{j}}, i = 1, \ldots, M\}$ as shown in Figure 13.1. Given the $M$ values $\$a_t$$ maturity $S^{i}_{T}$, we can obtain the Monte Carlo approximation to the expectation in Eq. (13.9),
$$
E_{t}^{\tilde{P}}[\max[S_{T} - K, 0]] \approx \frac{1}{M}\sum_{i=1}^{M}\max[S^{i}_{T} - K, 0]
$$

Multiplying with the current value of the bond, we get
$$
C(S_{t}, t) \approx B(t, T)\frac{1}{M}\sum_{i=1}^{M}\max[S^{i}_{T} - K, 0]
$$

As $M$ increases, the approximation error goes to zero.

![](5e6c7d8e9f0a1b2c3d4e5f6789abcdef0123456789abcdef0123456789abcdef.jpg)

# FIGURE 13.1
Simulated paths.

# 13.2.2 PRICING BINARY FX OPTIONS
Suppose now the security whose price we want to calculate is a binary or digital foreign currency option written on $e_{t}$, the USD/EUR exchange rate. The current date is $t$ and the expiry is $T$. Suppose the European binary call option has payoff

$$
C(e_{T}, T) = \begin{cases}
$100 & \text{if } e_{T} > K \\$
$0 & \text{otherwise}$
\end{cases}
$$

The strike is $K$ and the payoff is in USD. According to the fundamental theorem, we can express the current value of the binary call option as
$$
C(e_{t}, t) = E_{t}^{\tilde{P}}\left[\frac{C(e_{T}, T)}{Z_{T}/Z_{t}}\right]
$$

where $\tilde{P}$ is a martingale measure that corresponds to a normalization by $Z_{t}$.

# 13.2.2.1 Obtaining the risk-neutral dynamics
In this particular case, we need a probability associated with USD-denominated risk because the payoff is in USD. Hence, let $Z_{t}$ be the price of a USD-denominated risk-free discount bond
$$
Z_{t} = B_{d}(t, T) = e^{-r^{d}(T-t)}
$$

where $r^{d}$ is the (constant) domestic spot rate. This means $Z_{T} = 1$, and the equation becomes
$$
C(e_{t}, t) = B_{d}(t, T)E_{t}^{\tilde{P}}[C(e_{T}, T)]
$$

where $\tilde{P}$ is the probability measure that makes USD-denominated assets have an expected return equal to the domestic risk-free rate. Determining the risk-adjusted dynamics for the exchange rate $e_{t}$ is more complex than obtaining those for the simple stock price $S_{t}$. There are $\$a_t$$ least two ways we can proceed. First, we can use the risk-neutral dynamics immediately. We can conjecture, in analogy with Eq. (13.19), that the exchange rate should have the risk-neutral dynamics given by the SDE:
$$
\mathrm{d}e_{t} = re_{t}\mathrm{d}t + \sigma e_{t}\mathrm{d}W^{\tilde{P}}_{t}
$$

But this is only a conjecture, and we need to check if it is consistent with no-arbitrage conditions. To see this, we note that the foreign savings account dynamics are given by
$$
\mathrm{d}A^{f}_{t} = r^{f}A^{f}_{t}\mathrm{d}t
$$

Normalize this with the $B_{d}(t, T)$. The fundamental theorem says
$$
\frac{e_{t}A^{f}_{t}}{B_{d}(t, T)} = E_{t}^{\tilde{P}}\left[\frac{e_{T}A^{f}_{T}}{1}\right]
$$

With constant interest rates this leads to
$$
e_{t}A^{f}_{t}e^{r^{d}(T-t)} = E_{t}^{\tilde{P}}[e_{T}A^{f}_{T}]
$$

Now divide both sides by $A^{f}_{t}$ and rearrange to get
$$
e_{t}e^{(r^{d}-r^{f})(T-t)} = E_{t}^{\tilde{P}}[e_{T}]
$$

since $A^{f}_{T}/A^{f}_{t} = e^{r^{f}(T-t)}$. This gives
$$
E_{t}^{\tilde{P}}[e_{T}] = e_{t}e^{(r^{d}-r^{f})(T-t)}
$$

This last equation is important. It tells us that if we select normalizing USD-denominated bonds, then the expected rate of appreciation of the USD/EUR exchange rate, calculated with the $\tilde{P}$, will equal the interest rate differential.

This will not be satisfied by the conjectured SDE in Eq. (13.28). Using the dynamics in this equation, the conditional expectation of $e_{T}$ will be
$$
E_{t}^{\tilde{P}}[e_{T}] = e_{t}e^{r^{d}(T-t)}
$$

which is not the same as Eq. (13.33) when $r^{f} \neq 0$.

What is the problem? The normalization by $B_{d}(t, T)$ led to a probability under which all USD-denominated assets will have an expected return equal to the US risk-free rate. But, the exchange rate is not USD-denominated. It is the ratio of USD over EUR and does not have a "dimension."

What is the solution? Convert the exchange rate $e_{t}$ artificially into a USD-denominated asset. In fact, the entity
$$
\hat{e}_{t} = e_{t}A^{f}_{t}
$$

is the value in USD of one EUR invested in the foreign (EUR) savings account, and is measured in USD. Under the $\tilde{P}$, the expected return of this asset should equal $r^{d}$. Now, we have
$$
E_{t}^{\tilde{P}}[\hat{e}_{u}] = \hat{e}_{t}e^{r^{d}(u-t)}
$$

But the relationship between $\hat{e}_{t}$ and $e_{t}$ can be used to get
$$
E_{t}^{\tilde{P}}[e_{u}] = e_{t}\frac{A^{f}_{u}}{A^{f}_{t}}e^{r^{d}(u-t)}
$$

With constant EUR interest rates, we get Eq. (13.33) again.

The SDE for $\hat{e}_{t}$ is given by
$$
\mathrm{d}\hat{e}_{t} = r^{d}\hat{e}_{t}\mathrm{d}t + \sigma \hat{e}_{t}\mathrm{d}W^{\tilde{P}}_{t}
$$

where we assume that the volatility of $\hat{e}_{t}$ is the same as the volatility of $e_{t}$. We now apply Ito's Lemma. In particular, $\hat{e}_{t} = e_{t}A^{f}_{t}$ represents
$$
\hat{e}_{t} = f(e_{t}, A^{f}_{t})
$$

Using Ito's Lemma, we get
$$
\mathrm{d}\hat{e}_{t} = e_{t}\mathrm{d}A^{f}_{t} + A^{f}_{t}\mathrm{d}e_{t}
$$

Substituting the dynamics of $A^{f}_{t}$ and the unknown dynamics of $e_{t}$:
$$
\mathrm{d}e_{t} = \mu e_{t}\mathrm{d}t + \sigma e_{t}\mathrm{d}W^{\tilde{P}}_{t}
$$

where the unknown drift is denoted by $\\mu$. Substituting and using the fact that $\hat{e}_{t} = e_{t}A^{f}_{t}$:
$$
\mathrm{d}\hat{e}_{t} = (r^{f} + \mu)\hat{e}_{t}\mathrm{d}t + \sigma \hat{e}_{t}\mathrm{d}W^{\tilde{P}}_{t}
$$

But we know that $\hat{e}_{t}$ should have the expected return $r^{d}$ under $\tilde{P}$. Comparing with Eq. (13.38):
$$
r^{f} + \mu = r^{d}
$$

which gives
$$
\mu = r^{d} - r^{f}
$$

Therefore, the risk-neutral dynamics of $e_{t}$ are
$$
\mathrm{d}e_{t} = (r^{d} - r^{f})e_{t}\mathrm{d}t + \sigma e_{t}\mathrm{d}W^{\tilde{P}}_{t}
$$

This is the result we need for the Monte Carlo approach applied to foreign exchange options.

# 13.2.2.2 Monte Carlo process
Given the dynamics in Eq. (13.45), we can use Monte Carlo simulations to price the binary option. The discretized dynamics are
$$
\Delta e_{t_{i}} = (r^{d} - r^{f})e_{t_{i-1}}\Delta + \sigma e_{t_{i-1}}\sqrt{\Delta}z_{i}
$$

where $z_{i}$ are independent draws from a standard normal distribution.

The steps are:
[^1]: Generate $M$ paths of $e_{t}$ from time $t$ to $T$ using Eq. (13.46).
[^2]: For each path $i$, calculate the payoff:
   $$
   C^{i}(e_{T}, T) = \begin{cases}
   \$100 & \text{if } e^{i}_{T} > K \\$
   \$0 & \text{otherwise}$
   \end{cases}
   $$
[^3]: Calculate the average payoff:
   $$
   \overline{C} = \frac{1}{M}\sum_{i=1}^{M}C^{i}(e_{T}, T)
   $$
[^4]: Discount back to get the option price:
   $$
   C(e_{t}, t) = B_{d}(t, T)\overline{C} = e^{-r^{d}(T-t)}\overline{C}
   $$

This completes the Monte Carlo pricing of the binary FX option.

# 13.2.3 PATH DEPENDENCY
One of the main advantages of Monte Carlo methods is their ability to handle path-dependent options. Unlike the binomial tree or closed-form solutions, Monte Carlo can easily accommodate complex payoff structures that depend on the entire path of the underlying asset.

Consider an Asian option whose payoff depends on the average exchange rate over the option's life:
$$
C(e_{T}, T) = \max\left[\frac{1}{n}\sum_{i=1}^{n}e_{t_{i}} - K, 0\right]
$$

where $t_{i}$, $i = 1, \ldots, n$ are the averaging dates.

To price this option using Monte Carlo:
[^1]: Generate paths for $e_{t}$ from time $t$ to $T$.
[^2]: For each path, calculate the average rate $\$a_t$$ the specified dates.
[^3]: Calculate the payoff based on this average.
[^4]: Average across all paths and discount.

The Monte Carlo approach naturally handles this complexity, while analytical solutions for such options are rare or involve complex approximations.

Another example is a barrier option, where the payoff depends on whether the underlying crosses a certain level during the option's life:
$$
C(e_{T}, T) = \begin{cases}
\max[e_{T} - K, 0] & \text{if } e_{u} < H \text{ for all } t \leq u \leq T \\
[^0]: & \text{otherwise}
\end{cases}
$$

where $H$ is the barrier level.

For barrier options, the Monte Carlo simulation must check $\$a_t$$ each time step whether the barrier has been breached. With continuous barriers, care must be taken about the discretization, as the discrete approximation might miss barrier crossings that would occur in continuous time.

# 13.2.4 DISCRETIZATION BIAS AND CLOSED FORMS
When implementing Monte Carlo methods, discretization of the continuous-time stochastic process introduces bias. The size of this bias depends on:
[^1]: The time step $\\Delta$
[^2]: The functional form of the drift and volatility
[^3]: The particular discretization scheme used

For geometric Brownian motion with constant parameters, the exact solution is known:
$$
S_{T} = S_{t}\exp\left[\left(r - \frac{\sigma^{2}}{2}\right)(T-t) + \sigma\sqrt{T-t}z\right]
$$

where $z \sim N(0,1)$. When such closed-form solutions exist, they should be used instead of discretization to eliminate bias.

For more complex processes, higher-order discretization schemes (such as the Milstein scheme) can reduce bias compared to the simple Euler scheme we've been using.

# 13.2.5 REAL-LIFE COMPLICATIONS
In practice, several complications arise when implementing Monte Carlo methods:

[^1]: **Variance reduction**: Basic Monte Carlo can require many simulations for accurate results. Techniques like antithetic variates, control variates, and importance sampling can significantly reduce the variance of estimates.

[^2]: **Quasi-random sequences**: Instead of pseudo-random numbers, quasi-random (low-discrepancy) sequences can provide better convergence properties.

[^3]: **American options**: Standard Monte Carlo cannot handle early exercise directly. Methods like the Longstaff-Schwartz algorithm use regression techniques to approximate the optimal exercise boundary.

[^4]: **Multi-factor models**: With multiple sources of randomness, careful attention must be paid to correlation structures and the choice of random number generation.

[^5]: **Computational efficiency**: For complex models or large portfolios, computational time becomes a significant constraint. Parallel computing and GPU acceleration are often employed.

# 13.3 APPLICATION 2: CALIBRATION
Calibration is the process of determining model parameters such that the model prices match observed market prices for liquid instruments. This is a crucial step in derivatives pricing and risk management, as it ensures the model is consistent with current market conditions.

The fundamental theorem provides the theoretical foundation for calibration. Since market prices should be arbitrage-free, they can be expressed as expectations under some risk-neutral measure. The calibration process finds the parameters of this measure that best match observed prices.

# 13.3.1 CALIBRATING A TREE
Tree models provide a discrete approximation to continuous processes and are particularly useful for American options and other path-dependent derivatives. The Black-Derman-Toy (BDT) model is a popular example that we'll use to illustrate calibration.

The BDT model specifies the evolution of short rates in a binomial tree where:
- Interest rates are lognormally distributed
- The model is calibrated to match the initial term structure
- Volatility can be time-dependent
# 13.3.2 EXTRACTING A LIBOR TREE
Consider calibrating a tree to match observed LIBOR rates and caplet prices. The goal is to construct a tree such that:
[^1]: The model prices of zero-coupon bonds match market prices
[^2]: The model prices of caplets match market prices

# 13.3.2.1 Pricing functions
Let $P(t, T)$ denote the price $\$a_t$$ time $t$ of a zero-coupon bond maturing $$a_t$$ time $T$. In a tree model:
$$
P(t, T) = E_{t}^{Q}\left[\exp\left(-\int_{t}^{T}r_{s}\mathrm{d}s\right)\right]
$$

where $r_{s}$ is the short rate and $Q$ is the risk-neutral measure.

For a caplet with strike $K$ and maturity $T$:
$$
\text{Caplet}(t, T) = P(t, T+\tau)E_{t}^{Q_{T+\tau}}[\tau(L_{T} - K)^{+}]
$$

where $L_{T}$ is the LIBOR rate, $\\tau$ is the tenor, and $Q_{T+\\tau}$ is the $(T+\\tau)$-forward measure.

# 13.3.3 OBTAINING THE BDT TREE
The BDT model assumes that the short rate follows a lognormal process in the risk-neutral measure:
$$
\mathrm{d}\ln r_{t} = \theta(t)\mathrm{d}t + \sigma(t)\mathrm{d}W_{t}
$$

where $\\theta(t)$ is chosen to match the initial term structure and $\\sigma(t)$ is the volatility function.

# 13.3.3.1 Specifying the dynamics
In the binomial tree, $\$a_t$$ each node the short rate can move up or down:
$$
r_{u} = r_{m}u
$$
$$
r_{d} = r_{m}d
$$

where $u$ and $d$ are the up and down factors, and $r_{m}$ is the median rate $\$a_t$$ that time step.

# 13.3.3.2 The variance of $L_i$
The variance of the LIBOR rate $\$a_t$$ each node is related to the volatility of the short rate through:
$$
\text{Var}[\ln L_{i}] = \int_{t_{i}}^{t_{i+1}}\sigma^{2}(s)\mathrm{d}s
$$

This relationship allows us to calibrate the volatility function $\\sigma(t)$ to match market caplet prices.

# 13.3.4 CALIBRATING THE TREE
The calibration process involves:

[^1]: **Building the tree structure**: Start with an initial guess for the median rates and volatilities $\$a_t$$ each time step.

[^2]: **Matching zero-coupon bond prices**: Adjust the median rates so that the tree prices of zero-coupon bonds match market prices. This is done iteratively, starting from the shortest maturity.

[^3]: **Matching caplet prices**: Adjust the volatilities $\$a_t$$ each time step so that the tree prices of caplets match market prices.

[^4]: **Iteration**: The process may require several iterations as adjustments to volatilities can affect bond prices and vice versa.

The calibration algorithm:
```
For each time step i:
[^1]: Choose initial median rate r_m(i)
[^2]: Calculate bond prices using the tree
[^3]: Adjust r_m(i) until model bond price matches market
[^4]: Choose initial volatility σ(i)
[^5]: Calculate caplet prices using the tree
[^6]: Adjust σ(i) until model caplet price matches market
[^7]: Check convergence, iterate if necessary
```

# 13.3.5 USES OF THE TREE
Once calibrated, the BDT tree can be used to price various interest rate derivatives:

# 13.3.5.1 Application: pricing a cap
A cap is a series of caplets. To price a cap using the calibrated tree:

[^1]: Start $\$a_t$$ the final nodes of the tree
[^2]: Calculate the payoff $\$a_t$$ each node: $\max(\tau(L - K), 0)$
[^3]: Work backward through the tree, calculating expected values
[^4]: At each node: $V = e^{-r\\Delta t}[pV_{u} + (1-p)V_{d}]$

where $p$ is the risk-neutral probability, $V_{u}$ and $V_{d}$ are the values $\$a_t$$ the up and down nodes, and $\Delta t$ is the time step.

# 13.3.5.2 Some assumptions of the model
The BDT model makes several assumptions:
- Lognormal distribution of rates (rates cannot go negative)
- Time-homogeneous volatility structure
- Perfect correlation between different maturity rates
- No jumps in interest rates
These assumptions may not hold in practice, leading to model risk.

# 13.3.5.3 Remarks
Calibration quality depends on:
- The number of calibration instruments
- The accuracy of market prices
- The numerical methods used
- The model's ability to capture market dynamics
Over-calibration can lead to unstable models that perform poorly for out-of-sample pricing.

# 13.3.6 REAL-WORLD COMPLICATIONS
In practice, calibration faces several challenges:

[^1]: **Illiquid instruments**: Market prices may not be available for all maturities
[^2]: **Bid-ask spreads**: Which price to use for calibration?
[^3]: **Arbitrage violations**: Market quotes may contain arbitrage opportunities
[^4]: **Model limitations**: The model may not be flexible enough to match all prices
[^5]: **Stability**: Small changes in inputs can lead to large changes in calibrated parameters
[^6]: **Cross-sectional consistency**: Calibrating to different instrument types simultaneously

# 13.4 APPLICATION 3: QUANTOS
Quantos (quantity-adjusted options) are derivatives where the payoff is in a different currency than the underlying asset, but without foreign exchange risk. They provide an excellent example of how to switch between different risk-neutral measures.

# 13.4.1 PRICING QUANTOS
Consider a quanto call option on a foreign stock $S^{f}_{t}$ with the following features:
- The underlying stock price is in foreign currency (e.g., EUR)
- The strike price $K$ is in foreign currency
- The payoff is in domestic currency (e.g., USD) $\$a_t$$ a fixed exchange rate
The payoff $\$a_t$$ maturity is:
$$
C_{T} = \max(S^{f}_{T} - K, 0) \text{ USD}
$$

Note that the payoff is the foreign currency amount converted $\$a_t$$ a rate of 1:1, not $$a_t$$ the prevailing exchange rate.

To price this option, we need to find the appropriate risk-neutral measure. The challenge is that the underlying is denominated in EUR, but the payoff is in USD.

Using the fundamental theorem:
$$
C_{t} = B_{d}(t,T)E_{t}^{Q^{d}}[\max(S^{f}_{T} - K, 0)]
$$

where $Q^{d}$ is the domestic risk-neutral measure.

However, $S^{f}_{t}$ follows its natural dynamics under the foreign risk-neutral measure $Q^{f}$, not under $Q^{d}$. We need to change measures.

The Radon-Nikodym derivative for changing from $Q^{f}$ to $Q^{d}$ is:
$$
\frac{\mathrm{d}Q^{d}}{\mathrm{d}Q^{f}} = \frac{e_{T}B_{f}(0,T)}{e_{0}B_{d}(0,T)}
$$

where $e_{t}$ is the exchange rate (domestic per foreign).

Under $Q^{f}$, the stock follows:
$$
\mathrm{d}S^{f}_{t} = r^{f}S^{f}_{t}\mathrm{d}t + \sigma^{f}S^{f}_{t}\mathrm{d}W^{f}_{t}
$$

After the measure change to $Q^{d}$:
$$
\mathrm{d}S^{f}_{t} = (r^{f} - \rho\sigma^{f}\sigma_{e})S^{f}_{t}\mathrm{d}t + \sigma^{f}S^{f}_{t}\mathrm{d}W^{d}_{t}
$$

where $\\rho$ is the correlation between the stock and exchange rate, and $\sigma_{e}$ is the exchange rate volatility.

# 13.4.2 THE PDE APPROACH
An alternative approach uses partial differential equations. Consider a quanto derivative with value $V(S^{f}, e, t)$ depending on both the foreign stock price and the exchange rate.

The hedging portfolio consists of:
- The quanto derivative
- $\Delta_{S}$ units of the foreign stock
- $\Delta_{e}$ units of foreign currency
The no-arbitrage condition leads to the PDE:
$$
\frac{\partial V}{\partial t} + r^{f}S^{f}\frac{\partial V}{\partial S^{f}} + (r^{d} - r^{f})e\frac{\partial V}{\partial e} + \frac{1}{2}\sigma_{S}^{2}(S^{f})^{2}\frac{\partial^{2}V}{\partial (S^{f})^{2}} + \frac{1}{2}\sigma_{e}^{2}e^{2}\frac{\partial^{2}V}{\partial e^{2}} + \rho\sigma_{S}\sigma_{e}S^{f}e\frac{\partial^{2}V}{\partial S^{f}\partial e} = r^{d}V
$$

# 13.4.2.1 A PDE for quantos
For a quanto option where the payoff doesn't depend on the exchange rate, we can simplify. Let $V = V(S^{f}, t)$. The PDE becomes:
$$
\frac{\partial V}{\partial t} + (r^{d} - \rho\sigma_{S}\sigma_{e})S^{f}\frac{\partial V}{\partial S^{f}} + \frac{1}{2}\sigma_{S}^{2}(S^{f})^{2}\frac{\partial^{2}V}{\partial (S^{f})^{2}} = r^{d}V
$$

This is the Black-Scholes PDE with:
- Risk-free rate: $r^{d}$
- Dividend yield: $q = r^{f} - r^{d} + \\rho\sigma_{S}\sigma_{e}$
# 13.4.3 QUANTO FORWARD
The quanto forward price is:
$$
F_{t,T} = S^{f}_{t}\exp[(r^{d} - r^{f} + \rho\sigma_{S}\sigma_{e})(T-t)]
$$

This differs from the standard forward price by the correlation term $\\rho\sigma_{S}\sigma_{e}$.

# 13.4.4 QUANTO OPTION
Using the modified Black-Scholes formula, the quanto call option price is:
$$
C_{t} = e^{-r^{d}(T-t)}[F_{t,T}N(d_{1}) - KN(d_{2})]
$$

where:
$$
d_{1} = \frac{\ln(F_{t,T}/K) + \frac{1}{2}\sigma_{S}^{2}(T-t)}{\sigma_{S}\sqrt{T-t}}
$$
$$
d_{2} = d_{1} - \sigma_{S}\sqrt{T-t}
$$

# 13.4.4.1 Black-Scholes and dividends
If the foreign stock pays dividends $\$a_t$$ rate $q^{f}$, the quanto forward price becomes:
$$
F_{t,T} = S^{f}_{t}\exp[(r^{d} - r^{f} - q^{f} + \rho\sigma_{S}\sigma_{e})(T-t)]
$$

The option pricing formula remains the same with this adjusted forward price.

# 13.4.5 HOW TO HEDGE QUANTOS
Hedging quanto options requires positions in:
[^1]: The foreign stock (delta hedge)
[^2]: Foreign currency (to hedge correlation risk)
[^3]: Options on the exchange rate (vega hedge for correlation)

The delta with respect to the stock is:
$$
\Delta_{S} = e^{-r^{d}(T-t)}N(d_{1})
$$

The sensitivity to correlation (cross-gamma) is:
$$
\frac{\partial^{2}C}{\partial S^{f}\partial e} = e^{-r^{d}(T-t)}\sigma_{e}(T-t)N(d_{1})
$$

This cross-risk makes quanto options more complex to hedge than standard options.

# 13.4.6 REAL-LIFE CONSIDERATIONS
In practice, quanto pricing and hedging involve:

[^1]: **Correlation estimation**: Historical correlation may not predict future correlation
[^2]: **Liquidity**: Foreign stocks may have different liquidity than domestic markets
[^3]: **Transaction costs**: Cross-border transactions may have higher costs
[^4]: **Regulatory issues**: Capital controls or taxes may affect hedging
[^5]: **Model risk**: The assumption of constant correlation is often violated
[^6]: **Credit risk**: Quanto structures may involve counterparty risk

Quanto products are popular because they allow investors to:
- Take views on foreign assets without currency risk
- Access foreign markets with domestic currency settlement
- Create structured products with simplified currency exposure
# 13.5 CONCLUSIONS
This chapter has demonstrated three important applications of the fundamental theorem of asset pricing:

[^1]: **Monte Carlo methods**: A general numerical technique for calculating risk-neutral expectations, particularly useful for path-dependent and exotic options.

[^2]: **Calibration**: The process of fitting model parameters to match market prices, ensuring consistency with observed arbitrage-free prices.

[^3]: **Quanto pricing**: An example of changing between risk-neutral measures, showing how the fundamental theorem applies to multi-currency derivatives.

These applications highlight the practical importance of the fundamental theorem in modern financial engineering. The theorem not only provides theoretical insight but also guides the development of numerical methods, model calibration procedures, and pricing frameworks for complex derivatives.

Key takeaways include:
- The choice of numeraire affects the risk-neutral dynamics
- Measure changes are essential for multi-currency products
- Calibration ensures models are consistent with market prices
- Numerical methods like Monte Carlo make the theory practical
Understanding these applications is crucial for financial engineers working with derivatives pricing, risk management, and product development.

# SUGGESTED READING
For Monte Carlo methods:
• Glasserman, P. (2004). *Monte Carlo Methods in Financial Engineering*. Springer. - Comprehensive treatment of Monte Carlo techniques in finance

• Jäckel, P. (2002). *Monte Carlo Methods in Finance*. Wiley. - Practical guide to implementing Monte Carlo simulations

For calibration:
• Brigo, D., & Mercurio, F. (2006). *Interest Rate Models - Theory and Practice*. Springer. - Detailed coverage of interest rate model calibration

• Rebonato, R. (2004). *Volatility and Correlation*. Wiley. - Advanced treatment of model calibration in practice

For quanto products:
• Wystup, U. (2006). *FX Options and Structured Products*. Wiley. - Comprehensive guide to FX derivatives including quantos

• Hull, J. (2018). *Options, Futures, and Other Derivatives*. Pearson. - Standard reference with sections on quanto products

# EXERCISES
[^1]: Implement a Monte Carlo pricer for a European call option on a stock. Compare your results with the Black-Scholes formula for various parameter values.

[^2]: Price an Asian call option using Monte Carlo simulation. How does the price compare to a European call with the same strike and maturity?

[^3]: Calibrate a two-period binomial tree to match:
   a) Two zero-coupon bond prices
   b) One $\$a_t$$-the-money caplet price
   Document your calibration procedure.

[^4]: Derive the PDE for a quanto put option. What boundary conditions would you use?

[^5]: Calculate the price of a quanto forward when the correlation between the foreign stock and exchange rate is:
   a) +0.5
   b) 0
   c) -0.5
   Explain the economic intuition for the differences.

[^6]: Implement a Monte Carlo pricer for a barrier option. How does discretization affect the accuracy of your price?

[^7]: Show that under the domestic risk-neutral measure, the expected return on a foreign stock is $r^{d} - r^{f} + \\rho\sigma_{S}\sigma_{e}$.

[^8]: Design a hedging strategy for a quanto option. What instruments would you use and why?

[^9]: Explain why American quanto options are more difficult to price than European quanto options.

[^10]: Consider a "composite" option where the payoff is $\max(e_{T}S^{f}_{T} - K, 0)$ in domestic currency. How would you price this option?

# EXCEL EXERCISES
[^1]: Build a Monte Carlo simulation in Excel for:
   a) Geometric Brownian motion
   b) European option pricing
   c) Confidence intervals for the price estimate

[^2]: Create a spreadsheet that calibrates a binomial tree to:
   a) An initial yield curve
   b) At-the-money caplet volatilities
   Use Solver for the optimization.

[^3]: Implement a quanto option pricer that:
   a) Takes correlation as an input
   b) Calculates option Greeks
   c) Shows sensitivity to correlation

[^4]: Build a tool that compares Monte Carlo prices with:
   a) Different numbers of paths
   b) Different time steps
   c) Variance reduction techniques

# MATLAB EXERCISES
[^1]: Implement an efficient Monte Carlo engine that:
   a) Uses vectorization for speed
   b) Implements antithetic variates
   c) Calculates standard errors

[^2]: Program the BDT model calibration:
   a) Use Newton-Raphson for root finding
   b) Implement smoothness constraints
   c) Visualize the resulting tree

[^3]: Create a quanto pricing library that:
   a) Handles multiple underlying assets
   b) Allows time-varying correlation
   c) Computes hedge ratios

[^4]: Develop a convergence study for Monte Carlo:
   a) Plot price vs. number of paths
   b) Analyze discretization error
   c) Compare different random number generators

[^5]: Implement a PDE solver for quanto options:
   a) Use finite differences
   b) Handle American exercise
   c) Compare with Monte Carlo results
---
title: Lecture 2 - Asset Allocation with Multiple Risky Assets
cssclasses:
  - academia
  - finance
tags:
  - asset_allocation
  - covariance_matrix
  - multiple_assets
  - portfolio_theory
  - risk_return
  - portfolio_optimization
  - modern_portfolio_theory
  - efficient_frontier
  - diversification
  - risk_management
aliases:
  - Asset Allocation
  - Multiple Risky Assets
  - Lecture 2
  - Portfolio Optimization
  - Tangency Portfolio
key_concepts:
  - CRRA preferences
  - Mean-standard deviation frontier
  - Optimal portfolio framework
  - Portfolio return variance
  - Tangency portfolio formulas
  - Efficient frontier construction
  - Diversification benefits
  - Correlation effects
  - Capital allocation line
  - Matrix algebra in portfolio theory
  - Constrained optimization
  - Global minimum variance portfolio
---

# Lecture 2: Asset Allocation with Multiple Risky Assets
<<<<<<< HEAD
We now extend our optimal [portfolio](An%20Asset%20Allocation%20Primer.md) choice framework to allow for multiple risky assets. This gets us close to the type of models that are used by asset managers of large portfolios to decide how much to allocate to different asset classes.
=======
We now extend our optimal [[An Asset Allocation Primer|portfolio]] choice framework to allow for multiple risky assets. This gets us close to the type of models that are used by asset managers of large portfolios to decide how much to allocate to different asset classes.
>>>>>>> d83d5c06204d625fbecfdb77e4d3f37c9c80e27b

We still stick to the IID [returns](../Financial%20Markets/Financial%20Asset%20Pricing%20Theory%20Overview/Chapter%203%20-%20%20Assets,%20Portfolios,%20and%20Arbitrage/Assets.md) assumption for now.

<<<<<<< HEAD
In your intro investments course, you saw the graphical representation of the solution for the optimal [portfolio](An%20Asset%20Allocation%20Primer.md). Recall the hyperbolic shape of the mean-standard deviation frontier, the tangency [portfolio](An%20Asset%20Allocation%20Primer.md), and the capital market line that depicts all possible combinations of the [risk-free asset](../Financial%20Engineering/2.%20Forwards,%20Swaps,%20Futures,%20and%20Options.md) with the tangency [portfolio](An%20Asset%20Allocation%20Primer.md). Here we are going to use matrix algebra to get explicit formulas for the tangency [portfolio](An%20Asset%20Allocation%20Primer.md) and its risk-return properties.
=======
In your intro investments course, you saw the graphical representation of the solution for the optimal [[An Asset Allocation Primer|portfolio]]. Recall the hyperbolic shape of the mean-standard deviation frontier, the tangency [[An Asset Allocation Primer|portfolio]], and the capital market line that depicts all possible combinations of the [[2. Forwards, Swaps, Futures, and Options|risk-free asset]] with the tangency [[An Asset Allocation Primer|portfolio]]. Here we are going to use matrix algebra to get explicit formulas for the tangency [[An Asset Allocation Primer|portfolio]] and its risk-return properties.
>>>>>>> d83d5c06204d625fbecfdb77e4d3f37c9c80e27b

I use bold lowercase letters for vectors and bold uppercase letters for matrices. I use $\boldsymbol{\iota}$ to denote a column vector with all elements equal to one and $\boldsymbol{I}$ for the [identity matrix](../Financial%20Markets/Financial%20Asset%20Pricing%20Theory%20Overview/Chapter%201%20-%20Introduction%20and%20Overview/Prerequisites.md) (which has ones on its diagonals and zeros everywhere else). Letters or symbols that are not in boldface are scalars.

## 2.1 Risk and Return at the Portfolio Level

Consider $N$ risky assets with an $N \times 1$ vector of [returns](../Financial%20Markets/Financial%20Asset%20Pricing%20Theory%20Overview/Chapter%203%20-%20%20Assets,%20Portfolios,%20and%20Arbitrage/Assets.md) $\boldsymbol{r}$ and expected [returns](../Financial%20Markets/Financial%20Asset%20Pricing%20Theory%20Overview/Chapter%203%20-%20%20Assets,%20Portfolios,%20and%20Arbitrage/Assets.md) $\mathbb{E}[\boldsymbol{r}]$. We will often look at excess [returns](../Financial%20Markets/Financial%20Asset%20Pricing%20Theory%20Overview/Chapter%203%20-%20%20Assets,%20Portfolios,%20and%20Arbitrage/Assets.md)
$$

\begin{equation*}

\boldsymbol{z}=\boldsymbol{r}-\boldsymbol{\iota} R_{f},         \quad \boldsymbol{\mu}=\mathbb{E}[\boldsymbol{z}] \tag{2.1}

\end{equation*}

$$

<<<<<<< HEAD
Very important for our [portfolio](An%20Asset%20Allocation%20Primer.md) choice analysis is the $N \times N$ covariance matrix of [returns](../Financial%20Markets/Financial%20Asset%20Pricing%20Theory%20Overview/Chapter%203%20-%20%20Assets,%20Portfolios,%20and%20Arbitrage/Assets.md)
=======
Very important for our [[An Asset Allocation Primer|portfolio]] choice analysis is the $N \times N$ covariance matrix of [[Assets|returns]]
>>>>>>> d83d5c06204d625fbecfdb77e4d3f37c9c80e27b
$$

\begin{equation*}

\boldsymbol{\Sigma}=\mathbb{E}\left[(\boldsymbol{z}-\boldsymbol{\mu})(\boldsymbol{z}-\boldsymbol{\mu})^{\prime}\right] \tag{2.2}

\end{equation*}

$$

For analyzing [portfolio](An%20Asset%20Allocation%20Primer.md) [risk and return](Lecture%207-Risk%20and%20Return%20of%20Bonds.md),  we need to know a few rules on how the moments of [portfolio](An%20Asset%20Allocation%20Primer.md) [returns](../Financial%20Markets/Financial%20Asset%20Pricing%20Theory%20Overview/Chapter%203%20-%20%20Assets,%20Portfolios,%20and%20Arbitrage/Assets.md),  e.g.,  mean and variance,  depend on moments of individual [asset returns](../Financial%20Markets/Financial%20Asset%20Pricing%20Theory%20Overview/Chapter%201%20-%20Introduction%20and%20Overview/Some%20Stylized%20Empirical%20Facts%20About%20Asset%20Retur.md). Suppose we have a [portfolio](An%20Asset%20Allocation%20Primer.md) with $N$ assets and the weight of every asset (in terms of the proportion of the [portfolio](An%20Asset%20Allocation%20Primer.md)'s market value accounted for by each asset) is collected in the $N \times 1$ [portfolio weight vector](../Financial%20Markets/Financial%20Asset%20Pricing%20Theory%20Overview/Chapter%203%20-%20%20Assets,%20Portfolios,%20and%20Arbitrage/Portfolios%20and%20Trading%20Strategies.md) $\boldsymbol{\omega}=\left(\omega_{1},         \omega_{2},         \ldots,         \omega_{N}\right)^{\prime}$. Then the [portfolio](An%20Asset%20Allocation%20Primer.md) return is
$$

\begin{equation*}

R_{p}=\boldsymbol{\omega}^{\prime} \boldsymbol{r} \tag{2.3}

\end{equation*}

$$

and the expected [portfolio](An%20Asset%20Allocation%20Primer.md) return
$$

\begin{equation*}

\mathbb{E}\left[R_{p}\right]=\boldsymbol{\omega}^{\prime} \mathbb{E}[\boldsymbol{r}] \tag{2.4}

\end{equation*}

$$

We can calculate the variance from the $N \times N$ covariance matrix of individual [asset returns](../Financial%20Markets/Financial%20Asset%20Pricing%20Theory%20Overview/Chapter%201%20-%20Introduction%20and%20Overview/Some%20Stylized%20Empirical%20Facts%20About%20Asset%20Retur.md) as
$$

\begin{equation*}

\operatorname{var}\left(R_{p}\right)=\boldsymbol{\omega}^{\prime} \boldsymbol{\Sigma} \boldsymbol{\omega} . \tag{2.5}

\end{equation*}

$$

<<<<<<< HEAD
This last formula shows that all $N \times N$ elements of the covariance matrix play a role in determining the portfolio return variance. This is important. The [portfolio](An%20Asset%20Allocation%20Primer.md) variance depends not only on how volatile individual [asset returns](../Financial%20Markets/Financial%20Asset%20Pricing%20Theory%20Overview/Chapter%201%20-%20Introduction%20and%20Overview/Some%20Stylized%20Empirical%20Facts%20About%20Asset%20Retur.md) are,  but also on how strongly they covary,  i.e.,  whether they tend to move together or not. Here is how this looks like in the $N=2$ case,  where $\rho$ denotes the correlation of the two [asset returns](../Financial%20Markets/Financial%20Asset%20Pricing%20Theory%20Overview/Chapter%201%20-%20Introduction%20and%20Overview/Some%20Stylized%20Empirical%20Facts%20About%20Asset%20Retur.md) and $\rho \sigma_{1} \sigma_{2}$ their covariance:
=======
This last formula shows that all $N \times N$ elements of the covariance matrix play a role in determining the portfolio return variance. This is important. The [[An Asset Allocation Primer|portfolio]] variance depends not only on how volatile individual [[Some Stylized Empirical Facts About Asset Retur|asset returns]] are,  but also on how strongly they covary,  i.e.,  whether they tend to move together or not. Here is how this looks like in the $N=2$ case,  where $\rho$ denotes the correlation of the two [[Some Stylized Empirical Facts About Asset Retur|asset returns]] and $\rho \sigma_{1} \sigma_{2}$ their covariance:
>>>>>>> d83d5c06204d625fbecfdb77e4d3f37c9c80e27b
$$

\begin{align*}

\operatorname{var}\left(R_{p}\right) & =\binom{\omega_{1}}{\omega_{2}}^{\prime}\left(\begin{array}{cc}

\sigma_{1}^{2} & \rho \sigma_{1} \sigma_{2} \\

\rho \sigma_{1} \sigma_{2} & \sigma_{2}^{2}

\end{array}\right)\binom{\omega_{1}}{\omega_{2}}  \tag{2.6}\\

& =\omega_{1}^{2} \sigma_{1}^{2}+2 \omega_{1} \omega_{2} \rho \sigma_{1} \sigma_{2}+\omega_{2}^{2} \sigma_{2}^{2} \tag{2.7}

\end{align*}

$$

<<<<<<< HEAD
So if the [portfolio](An%20Asset%20Allocation%20Primer.md) has positive weight on both assets, $\omega_{1}>0$ and $\omega_{2}>0$, then, due to the middle term in this expression, the higher the correlation of the two [asset returns](../Financial%20Markets/Financial%20Asset%20Pricing%20Theory%20Overview/Chapter%201%20-%20Introduction%20and%20Overview/Some%20Stylized%20Empirical%20Facts%20About%20Asset%20Retur.md), the higher the portfolio return variance.
=======
So if the [[An Asset Allocation Primer|portfolio]] has positive weight on both assets, $\omega_{1}>0$ and $\omega_{2}>0$, then, due to the middle term in this expression, the higher the correlation of the two [[Some Stylized Empirical Facts About Asset Retur|asset returns]], the higher the portfolio return variance.
>>>>>>> d83d5c06204d625fbecfdb77e4d3f37c9c80e27b

Sometimes we are interested in the covariances of [returns](../Financial%20Markets/Financial%20Asset%20Pricing%20Theory%20Overview/Chapter%203%20-%20%20Assets,%20Portfolios,%20and%20Arbitrage/Assets.md) of the individual assets that are in the [portfolio](An%20Asset%20Allocation%20Primer.md) with the return of the overall [portfolio](An%20Asset%20Allocation%20Primer.md). We can get this vector of covariances by post-multiplying the covariance matrix with the [portfolio weight vector](../Financial%20Markets/Financial%20Asset%20Pricing%20Theory%20Overview/Chapter%203%20-%20%20Assets,%20Portfolios,%20and%20Arbitrage/Portfolios%20and%20Trading%20Strategies.md),
$$

\left(\begin{array}{c}

\operatorname{cov}\left(R_{1},         R_{p}\right)  \tag{2.8}\\

\operatorname{cov}\left(R_{2},         R_{p}\right) \\

\ldots \\

\operatorname{cov}\left(R_{N},         R_{N}\right)

\end{array}\right)=\boldsymbol{\Sigma} \boldsymbol{\omega} .

$$

## 2.2 Optimal Portfolio Choice with Multiple Risky Assets

<<<<<<< HEAD
Let's now turn to finding the optimal [portfolio](An%20Asset%20Allocation%20Primer.md) weight when we have multiple risky assets. As in the last lecture, we assume the investor has CRRA preferences and we'll use a [first-order approximation](../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%204/Convexity.md) of marginal utility to simplify the problem. The following analysis is pretty much analogous to our analysis in the single risky asset case in the last lecture,  but with some [vectors and matrices](../Financial%20Markets/Financial%20Asset%20Pricing%20Theory%20Overview/Chapter%201%20-%20Introduction%20and%20Overview/Prerequisites.md) replacing some scalars to account for the fact that we have [multiple risky assets](.md).
=======
Let's now turn to finding the optimal [[An Asset Allocation Primer|portfolio]] weight when we have multiple risky assets. As in the last lecture, we assume the investor has CRRA preferences and we'll use a [[Convexity|first-order approximation]] of marginal utility to simplify the problem. The following analysis is pretty much analogous to our analysis in the single risky asset case in the last lecture,  but with some [[Prerequisites|vectors and matrices]] replacing some scalars to account for the fact that we have [[Lecture 2- Asset Allocation with Multiple Risky Assets|multiple risky assets]].
>>>>>>> d83d5c06204d625fbecfdb77e4d3f37c9c80e27b

If the investor starts with wealth $W_{0}$ at the beginning of a period and invests proportions $\boldsymbol{\omega}$ of this [initial wealth](../Financial%20Markets/Financial%20Asset%20Pricing%20Theory%20Overview/Chapter%206%20-%20Individual%20optimality/The%20One-Period%20Framework.md) into the $N$ risky assets and the rest in the [risk-free asset](../Financial%20Engineering/2.%20Forwards,%20Swaps,%20Futures,%20and%20Options.md),  then the total [investment](An%20Asset%20Allocation%20Primer.md) in risky assets accounts for a proportion $\boldsymbol{\iota}^{\prime} \boldsymbol{\omega}=\sum_{i}^{N} \omega_{i}$ of [initial wealth](../Financial%20Markets/Financial%20Asset%20Pricing%20Theory%20Overview/Chapter%206%20-%20Individual%20optimality/The%20One-Period%20Framework.md) and the rest,  $1-\boldsymbol{\iota}^{\prime} \boldsymbol{\omega}$ is allocated to the [risk-free asset](../Financial%20Engineering/2.%20Forwards,%20Swaps,%20Futures,%20and%20Options.md). Hence the return on the investor's wealth [portfolio](An%20Asset%20Allocation%20Primer.md) is
$$

\begin{equation*}

R_{w}=\left(1-\boldsymbol{\iota}^{\prime} \boldsymbol{\omega}\right) R_{f}+\boldsymbol{r}^{\prime} \boldsymbol{\omega} \tag{2.9}

\end{equation*}

$$

or,  equivalently,
$$

\begin{equation*}

R_{w}=R_{f}+\boldsymbol{z}^{\prime} \boldsymbol{\omega} \tag{2.10}

\end{equation*}

$$

The investor's wealth at the end of the period is $W=W_{0}\left(1+R_{w}\right)$.

The investors' objective is the same as in the single risky asset case in the previous lecture
$$

\begin{equation*}

\max _{\boldsymbol{\omega}} \mathbb{E}[U(W)] \quad \text { s.t. } W=W_{0}\left(1+R_{w}\right),         \tag{2.11}

\end{equation*}

$$

but $R_{w}$ now depends on a vector of [portfolio](An%20Asset%20Allocation%20Primer.md) weights $\boldsymbol{\omega}$,  not just a single risky [asset portfolio](../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%204/The%20Barbell%20Versus%20the%20Bullet.md) weight,  that the investor is trying to optimize. The first-order condition of this problem is analogous to the single risky asset case,  but now we have $N$ first order conditions instead of just one.
$$

\begin{equation*}

\mathbb{E}\left[z \frac{U^{\prime}(W)}{U^{\prime}(\mathbb{E}[W])}\right]=0 \tag{2.12}

\end{equation*}

$$

In this vector of first-order conditions,  there is one first-order condition for each element of $\boldsymbol{z}$.

Approximating $\frac{U^{\prime}(W)}{U^{\prime}(\mathbb{E}[W])}$ linearly,  we get,  analogous to last lecture,
$$

\begin{equation*}

\frac{U^{\prime}(W)}{U^{\prime}(\mathbb{E}[W])} \approx 1-\gamma(\boldsymbol{r}-\mathbb{E}[\boldsymbol{r}])^{\prime} \boldsymbol{\omega} \tag{2.13}

\end{equation*}

$$

just now with a vector of [returns](../Financial%20Markets/Financial%20Asset%20Pricing%20Theory%20Overview/Chapter%203%20-%20%20Assets,%20Portfolios,%20and%20Arbitrage/Assets.md) and,  correspondingly,  a vector of [portfolio](An%20Asset%20Allocation%20Primer.md) weights $\boldsymbol{\omega}$. Substituting this approximation into the first-order condition (2.12),  we get
$$

\begin{equation*}

\mathbb{E}\left[\boldsymbol{z}\left\{1-\gamma(\boldsymbol{r}-\mathbb{E}[\boldsymbol{r}])^{\prime} \boldsymbol{\omega}\right\}\right]=0 \tag{2.14}

\end{equation*}

$$

With $E[\boldsymbol{z}]=\boldsymbol{\mu}$ and $\mathbb{E}\left[\boldsymbol{z}(\boldsymbol{r}-\mathbb{E}[\boldsymbol{r}])^{\prime}\right]=\boldsymbol{\Sigma}$,  we get
$$

\begin{equation*}

\boldsymbol{\mu}-\gamma \boldsymbol{\Sigma} \boldsymbol{\omega}=0 \tag{2.15}

\end{equation*}

$$

where the covariance matrix $\boldsymbol{\Sigma}$ has taken the place of the variance of risky asset return in the single risky asset case. We can solve this expression for the optimal risky asset share
$$

\begin{equation*}

\boldsymbol{\omega}=\frac{1}{\gamma} \boldsymbol{\Sigma}^{-1} \boldsymbol{\mu} \tag{2.16}

\end{equation*}

$$

So instead of division by the variance of the asset return in the single risky asset case we now have the inverse of the covariance matrix. Taking the inverse of a matrix is sort of like dividing. The proportion of wealth invested in the [risk-free asset](../Financial%20Engineering/2.%20Forwards,%20Swaps,%20Futures,%20and%20Options.md) is
$$

\begin{equation*}

\omega_{f}=1-\boldsymbol{\iota}^{\prime} \boldsymbol{\omega}=1-\frac{1}{\gamma} \boldsymbol{\iota}^{\prime} \boldsymbol{\Sigma}^{-1} \boldsymbol{\mu} \tag{2.17}

\end{equation*}

$$

Let's look at some properties of this solution. Note that we can can further rescale the weights $\boldsymbol{\omega}$ so that they sum up to unity. This yields the weights within the risky [asset portfolio](../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%204/The%20Barbell%20Versus%20the%20Bullet.md):
$$

\begin{equation*}

\boldsymbol{\omega}^{*}=\frac{1}{\boldsymbol{\iota}^{\prime} \boldsymbol{\omega}} \boldsymbol{\omega}=\frac{1}{\boldsymbol{\iota}^{\prime} \boldsymbol{\Sigma}^{-1} \boldsymbol{\mu}} \boldsymbol{\Sigma}^{-1} \boldsymbol{\mu} \tag{2.18}

\end{equation*}

$$

This tells us something important and very useful: The solution for $\boldsymbol{\omega}^{*}$ does not depend on the level of risk aversion! All investors,  irrespective of their degree of risk aversion should therefore hold a risky [asset portfolio](../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%204/The%20Barbell%20Versus%20the%20Bullet.md) with the same composition (as long as they have the same beliefs about $\boldsymbol{\Sigma}$ and $\boldsymbol{\mu}$ ). Risk preferences should only matter for how much of their wealth they allocate to the risky [asset portfolio](../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%204/The%20Barbell%20Versus%20the%20Bullet.md) overall and to the [risk-free asset](../Financial%20Engineering/2.%20Forwards,%20Swaps,%20Futures,%20and%20Options.md). By scaling up or down the risky asset portion of their wealth,  investors can adjust the [riskiness](../Financial%20Instruments/Financial%20Derivatives%20and%20Quantitative%20Methods/Risk%20Preferences.md) of their wealth [portfolio](An%20Asset%20Allocation%20Primer.md). This is sufficient for getting a [portfolio](An%20Asset%20Allocation%20Primer.md) consistent with their risk preferences.

Thus,  the decision on how to structure a [portfolio](An%20Asset%20Allocation%20Primer.md) can be separated into two independent steps. First,  how to split the risky [asset portfolio](../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%204/The%20Barbell%20Versus%20the%20Bullet.md) among the different risky assets; second,  how to allocate between this risky [asset portfolio](../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%204/The%20Barbell%20Versus%20the%20Bullet.md) and the [risk-free asset](../Financial%20Engineering/2.%20Forwards,%20Swaps,%20Futures,%20and%20Options.md). This result is called the two-fund separation theorem.

The risky [asset portfolio](../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%204/The%20Barbell%20Versus%20the%20Bullet.md) with weights $\boldsymbol{\omega}^{*}$ is the tangency [portfolio](An%20Asset%20Allocation%20Primer.md) that you already encountered in your introductory investments course. Let's denote with $R^{*}$ and $Z^{*}$ the [returns](../Financial%20Markets/Financial%20Asset%20Pricing%20Theory%20Overview/Chapter%203%20-%20%20Assets,%20Portfolios,%20and%20Arbitrage/Assets.md) and excess [returns](../Financial%20Markets/Financial%20Asset%20Pricing%20Theory%20Overview/Chapter%203%20-%20%20Assets,%20Portfolios,%20and%20Arbitrage/Assets.md) of this tangency [portfolio](An%20Asset%20Allocation%20Primer.md),  respectively.

To get some intuition for what the optimal [portfolio](An%20Asset%20Allocation%20Primer.md) solution does and how it depends on expected [returns](../Financial%20Markets/Financial%20Asset%20Pricing%20Theory%20Overview/Chapter%203%20-%20%20Assets,%20Portfolios,%20and%20Arbitrage/Assets.md) and correlations,  suppose we have $N=2$ and
$$

\boldsymbol{\mu}=\binom{\mu_{1}}{\mu_{2}},         \quad \boldsymbol{\Sigma}=\sigma^{2}\left(\begin{array}{ll}

1 & \rho  \tag{2.19}\\

\rho & 1

\end{array}\right)

$$

Then
$$

\boldsymbol{\Sigma}^{-1}=\frac{1}{\sigma^{2}\left(1-\rho^{2}\right)}\left(\begin{array}{cc}

1 & -\rho  \tag{2.20}\\

-\rho & 1

\end{array}\right)

$$

Plugging into (2.18) we get
$$

\begin{equation*}

\boldsymbol{\omega}^{*}=a\binom{\mu_{1}-\rho \mu_{2}}{\mu_{2}-\rho \mu_{1}} \tag{2.21}

\end{equation*}

$$

for some constant $a$ that collects all the scalar factors.

Now let's think about some special cases. If the two assets' [returns](../Financial%20Markets/Financial%20Asset%20Pricing%20Theory%20Overview/Chapter%203%20-%20%20Assets,%20Portfolios,%20and%20Arbitrage/Assets.md) are uncorrelated,  $\rho=0$,  then optimal [portfolio](An%20Asset%20Allocation%20Primer.md) weights are proportional to their expected [returns](../Financial%20Markets/Financial%20Asset%20Pricing%20Theory%20Overview/Chapter%203%20-%20%20Assets,%20Portfolios,%20and%20Arbitrage/Assets.md). Suppose $\mu_{1}>\mu_{2}$. Then the investor puts a higher share into asset 1 than into asset 2 . This should be intuitive. It makes sense to invest more in the higher-earning asset when the two assets are otherwise identical. But why not put everything into asset 1 (or even short asset 2 and invest more than $100/% of the risky [asset portfolio](../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%204/The%20Barbell%20Versus%20the%20Bullet.md) into asset 1)? [Diversification benefits](../Advanced%20Financial%20Analysis%20and%20Valuation/Lecture%20Notes%20Advanced%20Financial%20Analysis%20and%20Valuation/Week%208/Week%208%20Opportunities%20And%20Risks%20Of%20Investing%20Internationally.md)! Having some of asset 2 in the [portfolio](An%20Asset%20Allocation%20Primer.md),  but not too much,  can still be useful because it lowers the risk of the [portfolio](An%20Asset%20Allocation%20Primer.md).

Now consider a case where $\rho$ is very close to 1 and again $\mu_{1}>\mu_{2}$. In this case,  the assets are,  in terms of risk,  almost perfect substitutes. As a consequence,  a long-short position,  going long in asset 1 ,  short in asset 2 ,  is optimal: it earns a positive expected [returns](../Financial%20Markets/Financial%20Asset%20Pricing%20Theory%20Overview/Chapter%203%20-%20%20Assets,%20Portfolios,%20and%20Arbitrage/Assets.md) $\mu_{1}-\mu_{2}>0$,  but it has almost no risk because the [returns](../Financial%20Markets/Financial%20Asset%20Pricing%20Theory%20Overview/Chapter%203%20-%20%20Assets,%20Portfolios,%20and%20Arbitrage/Assets.md) of the two assets are almost perfectly correlated.

### 2.3 Systematic risk

How does a [mean-variance](../Financial%20Markets/Financial%20Asset%20Pricing%20Theory%20Overview/Chapter%2012%20-%20Derivatives/Exercises.md) optimizing investor think about a new asset that could be added to the existing [portfolio](An%20Asset%20Allocation%20Primer.md)? When is it attractive in terms of [risk and return](Lecture%207-Risk%20and%20Return%20of%20Bonds.md)? When does it make sense to alter the [portfolio](An%20Asset%20Allocation%20Primer.md) to include more or less of this asset? As we will see now,  the [mean-variance](../Financial%20Markets/Financial%20Asset%20Pricing%20Theory%20Overview/Chapter%2012%20-%20Derivatives/Exercises.md) optimal [portfolio](An%20Asset%20Allocation%20Primer.md) strikes a perfect balance between the [expected return](Lecture%201-%20Probability%20Distributions%20of%20Returns.md) that an asset contributes to the [portfolio](An%20Asset%20Allocation%20Primer.md) and the risk that it contributes. This contribution to [portfolio](An%20Asset%20Allocation%20Primer.md) risk is what we call systematic risk.

We can see the risk contribution of assets to the overall [portfolio](An%20Asset%20Allocation%20Primer.md) by examining the [portfolio](An%20Asset%20Allocation%20Primer.md) variance in equation (2.5). Note from (2.8) that the expression $\boldsymbol{\Sigma} \boldsymbol{\omega}$ in
$\operatorname{var}\left(R_{p}\right)=\boldsymbol{\omega}^{\prime} \boldsymbol{\Sigma} \boldsymbol{\omega}$ is a vector of covariances,  so the pre-multiplication by $\boldsymbol{\omega}^{\prime}$ forms a weighted sum of these covariances,  i.e.,$$\operatorname{var}\left(R_{p}\right) = \omega_{1} 
\underbrace{\operatorname{cov}\left(R_{1},   R_{p}\right)}_{
\begin{array}{c}
\text{Risk} \\
\text{contribution} \\
\text{of asset 1}
\end{array}
} 
+ \omega_{2} \operatorname{cov}\left(R_{2},   R_{p}\right) + \ldots + \omega_{N} \operatorname{cov}\left(R_{N},   R_{p}\right)$$

We have now decomposed the overall [portfolio](An%20Asset%20Allocation%20Primer.md) variance in the pieces that come from each asset. How much risk each asset brings to the [portfolio](An%20Asset%20Allocation%20Primer.md) is determined by how much of this asset is in the [portfolio](An%20Asset%20Allocation%20Primer.md),    i.e.,    its [portfolio](An%20Asset%20Allocation%20Primer.md) weight,    times the risk contribution measured by the covariance $\operatorname{cov}\left(R_{i},         R_{p}\right)$. For the same weight,    an asset that has a higher covariance with the [portfolio](An%20Asset%20Allocation%20Primer.md) return adds more risk to the [portfolio](An%20Asset%20Allocation%20Primer.md).

Dividing by $\operatorname{var}\left(R_{p}\right)$ on both sides,    we can express the risk contributions as shares of total [portfolio](An%20Asset%20Allocation%20Primer.md) risk. We get
$$

\begin{equation*}

1=\omega_{1} \beta_{1}+\omega_{2} \beta_{2}+\ldots+\omega_{N} \beta_{N} \tag{2.23}

\end{equation*}

$$

The systematic risk of asset $i$ is measured by
$$

\begin{equation*}

\beta_{i}=\frac{\operatorname{cov}\left(R_{i},  R_{p}\right)}{\operatorname{var}\left(R_{p}\right)} . \tag{2.24}

\end{equation*}

$$

One important take-away at this point is that systematic risk is investor specific. How much an asset contributes in terms of risk to an existing [portfolio](An%20Asset%20Allocation%20Primer.md) depends on what else is in the [portfolio](An%20Asset%20Allocation%20Primer.md),    which will typically differ across investors. If asset $i$ has a high return covariance with the other assets in the [portfolio](An%20Asset%20Allocation%20Primer.md),    then $\beta_{i}$ will be high. If the other assets' [returns](../Financial%20Markets/Financial%20Asset%20Pricing%20Theory%20Overview/Chapter%203%20-%20%20Assets,%20Portfolios,%20and%20Arbitrage/Assets.md) don't covary much with asset $i$ 's [returns](../Financial%20Markets/Financial%20Asset%20Pricing%20Theory%20Overview/Chapter%203%20-%20%20Assets,%20Portfolios,%20and%20Arbitrage/Assets.md),    then $\beta_{i}$ will be low.

Now let's assume the investor's [portfolio](An%20Asset%20Allocation%20Primer.md) is [mean-variance](../Financial%20Markets/Financial%20Asset%20Pricing%20Theory%20Overview/Chapter%2012%20-%20Derivatives/Exercises.md) optimal,    i.e.,    it has weights $\boldsymbol{\omega}^{*}=\boldsymbol{\Sigma}^{-1} \boldsymbol{\mu}$ as in (2.18),    with the modification that I dropped the scalar constant that rescales the [portfolio](An%20Asset%20Allocation%20Primer.md) in (2.18) to have weights that add up to $100/%. Whether we scale the portfolio weights by some constant factor does not matter for any of the calculations that follow in this section,    so I just drop the scaling factor to make the expression for $\omega^{*}$ less messy.

With these optimal [portfolio](An%20Asset%20Allocation%20Primer.md) weights,    following (2.8),    individual assets have a vector of covariances
$$

\begin{equation*}

\boldsymbol{\Sigma} \boldsymbol{\omega}^{*}=\boldsymbol{\Sigma} \boldsymbol{\Sigma}^{-1} \boldsymbol{\mu}=\boldsymbol{\mu} \tag{2.25}

\end{equation*}

$$

and,    following (2.5),    we have the [portfolio](An%20Asset%20Allocation%20Primer.md) variance
$$

\begin{equation*}

\operatorname{var}\left(R^{*}\right)=\boldsymbol{\omega}^{* /} \boldsymbol{\Sigma} \boldsymbol{\omega}^{*}=\boldsymbol{\omega}^{* \prime} \boldsymbol{\mu}=\mu^{*} \tag{2.26}

\end{equation*}

$$

where $\mu^{*}=\mathbb{E}\left[Z^{*}\right]$ is the [expected excess return](../Financial%20Markets/Financial%20Asset%20Pricing%20Theory%20Overview/Chapter%209%20-%20Factor%20Models/Theoretical%20Factors.md) of the [mean-variance](../Financial%20Markets/Financial%20Asset%20Pricing%20Theory%20Overview/Chapter%2012%20-%20Derivatives/Exercises.md) optimal [portfolio](An%20Asset%20Allocation%20Primer.md). Dividing the vector covariances in (2.25) by the [portfolio](An%20Asset%20Allocation%20Primer.md) variance in (2.26),    we then get a vector of betas:
$$

\begin{equation*}

\boldsymbol{\beta}^{*}=\frac{1}{\operatorname{var}\left(R^{*}\right)} \boldsymbol{\Sigma} \boldsymbol{\omega}^{*}=\frac{1}{\mu^{*}} \boldsymbol{\mu} . \tag{2.27}

\end{equation*}

$$

Rearranging,    we see that expected [returns](../Financial%20Markets/Financial%20Asset%20Pricing%20Theory%20Overview/Chapter%203%20-%20%20Assets,%20Portfolios,%20and%20Arbitrage/Assets.md) of individual are tightly linked to their systematic risk with respect to the [mean-variance](../Financial%20Markets/Financial%20Asset%20Pricing%20Theory%20Overview/Chapter%2012%20-%20Derivatives/Exercises.md) optimal [portfolio](An%20Asset%20Allocation%20Primer.md)
$$

\begin{equation*}

\boldsymbol{\mu}=\boldsymbol{\beta}^{*} \mu^{*} \tag{2.28}

\end{equation*}

$$

For an asset $i$,    therefore,  
$$

\begin{equation*}

\mathbb{E}\left[Z_{i}\right]=\beta_{i}^{*} \mathbb{E}\left[Z^{*}\right] \tag{2.29}

\end{equation*}

$$

which looks exactly like the relationship predicted by the [Capital Asset Pricing Model](../Financial%20Engineering/2.%20Forwards,%20Swaps,%20Futures,%20and%20Options.md) (CAPM) that you encountered in your introductory investments course - just with one very important difference: in the CAPM,    $\beta_{i}^{*}$ would be the beta with respect to the [market portfolio return](../Financial%20Markets/Financial%20Asset%20Pricing%20Theory%20Overview/Chapter%209%20-%20Factor%20Models/The%20Classical%20One-Period%20Capm.md) and $\mathbb{E}\left[Z^{*}\right]$ would be the [expected excess return](../Financial%20Markets/Financial%20Asset%20Pricing%20Theory%20Overview/Chapter%209%20-%20Factor%20Models/Theoretical%20Factors.md) on the market [portfolio](An%20Asset%20Allocation%20Primer.md). Here they are just the beta with respect to an investor's optimal [portfolio](An%20Asset%20Allocation%20Primer.md),    which need not be the same as the market [portfolio](An%20Asset%20Allocation%20Primer.md),    and $\mathbb{E}\left[Z^{*}\right]$ is the [expected excess return](../Financial%20Markets/Financial%20Asset%20Pricing%20Theory%20Overview/Chapter%209%20-%20Factor%20Models/Theoretical%20Factors.md) on the investor's [portfolio](An%20Asset%20Allocation%20Primer.md),    not the market [portfolio](An%20Asset%20Allocation%20Primer.md).

The condition (2.29) tells us that when the existing [portfolio](An%20Asset%20Allocation%20Primer.md) is [mean-variance](../Financial%20Markets/Financial%20Asset%20Pricing%20Theory%20Overview/Chapter%2012%20-%20Derivatives/Exercises.md) optimal,    then expected [returns](../Financial%20Markets/Financial%20Asset%20Pricing%20Theory%20Overview/Chapter%203%20-%20%20Assets,%20Portfolios,%20and%20Arbitrage/Assets.md) of all assets must have expected excess [returns](../Financial%20Markets/Financial%20Asset%20Pricing%20Theory%20Overview/Chapter%203%20-%20%20Assets,%20Portfolios,%20and%20Arbitrage/Assets.md) exactly proportional to their betas with respect to the [portfolio](An%20Asset%20Allocation%20Primer.md) return $R^{*}$. The beta of asset $i$ tells us how much risk we would add to the [portfolio](An%20Asset%20Allocation%20Primer.md) if we added more of this asset to the [portfolio](An%20Asset%20Allocation%20Primer.md). This is what we call systematic risk. This systematic risk originates from covariance,    i.e.,    the degree to which the return of asset $i$ and the [portfolio](An%20Asset%20Allocation%20Primer.md) $R^{*}$ move together in the same direction.

Furthermore,    equation (2.29) tells us that if the [portfolio](An%20Asset%20Allocation%20Primer.md) with return $R^{*}$ is already optimal,    then there cannot be any asset out there that offers an [expected return](Lecture%201-%20Probability%20Distributions%20of%20Returns.md) that is lower or higher than what equation (2.29) prescribes. Each asset's [expected return](Lecture%201-%20Probability%20Distributions%20of%20Returns.md) must be exactly commensurate with the systematic risk $\beta_{i}^{*}$ that this asset brings to the [portfolio](An%20Asset%20Allocation%20Primer.md) so that no asset looks attractive enough to add more of it to the [portfolio](An%20Asset%20Allocation%20Primer.md),    or unattractive enough to reduce its position.

Otherwise,    if we could find such an asset $i$ that violates condition (2.29),    we could improve our [portfolio](An%20Asset%20Allocation%20Primer.md)'s Sharpe ratio by adding more of asset $i$ to the [portfolio](An%20Asset%20Allocation%20Primer.md) (if the [expected return](Lecture%201-%20Probability%20Distributions%20of%20Returns.md) is higher than required) or taking some of it out,    and possibly [shorting](../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%202%20-%20Spot%20Markets/Short%20Selling.md) it (if the [expected return](Lecture%201-%20Probability%20Distributions%20of%20Returns.md) is lower than required). For example,    if an asset $i$ has $\mathbb{E}\left[Z_{i}\right]>\beta_{i}^{*} \mathbb{E}\left[Z^{*}\right]$,    it would make sense for the investor to take more of asset $i$ into the [portfolio](An%20Asset%20Allocation%20Primer.md),    because this would contribute to a relatively small amount of [portfolio](An%20Asset%20Allocation%20Primer.md) risk,    but a relatively big [expected excess return](../Financial%20Markets/Financial%20Asset%20Pricing%20Theory%20Overview/Chapter%209%20-%20Factor%20Models/Theoretical%20Factors.md).

We can decompose the total risk of an asset into systematic and idiosyncratic components. Note that $\beta_{i}^{*}=\operatorname{cov}\left(R_{i},         R^{*}\right) / \operatorname{var}\left(R^{*}\right)$ is an ordinary least squares (OLS) regression slope coefficient in a regression of $R_{i}$ on $R^{*}$. This means we can decompose $R_{i}$ as follows
$$

\begin{equation*}

R_{i}=a_{i}+\beta_{i}^{*} R^{*}+\varepsilon_{i} \tag{2.30}

\end{equation*}

$$

where $\operatorname{cov}\left(R^{*},         \varepsilon_{i}\right)=0$. This decomposition shows that movements in $R_{i}$ are partly due to movements perfectly aligned with $R^{*}$ (systematic) and partly due to movements uncorrelated with $R^{*}$ (idiosyncratic). Taking the variance of the leftand right-hand sides,  
$$

\begin{equation*}

\operatorname{var}\left(R_{i}\right)=\left(\beta_{i}^{*}\right)^{2} \operatorname{var}\left(R^{*}\right)+\operatorname{var}\left(\varepsilon_{i}\right),  \tag{2.31}

\end{equation*}

$$

we have now broken the total risk of asset $i,         \operatorname{var}\left(R_{i}\right)$,    into two components: Systematic risk,    $\left(\beta_{i}^{*}\right)^{2} \operatorname{var}\left(R^{*}\right)$,    and idiosyncratic risk,    $\operatorname{var}\left(\varepsilon_{i}\right)$.

Since systematic risk determines an assets (un)attractiveness,    not the idiosyncratic risk,    Sharpe Ratios are not good measures of the reward to risk ratio for individual assets,    because the Sharpe Ratio uses total volatility as a [risk measure](../Financial%20Instruments/Leverage%20as%20a%20Measure%20of%20Risk.md),    not just the systematic risk component.

Of course,    this reasoning based on (2.29) applies only to small changes to the [portfolio](An%20Asset%20Allocation%20Primer.md) at the margin. The change in [portfolio](An%20Asset%20Allocation%20Primer.md) risk from a small addition of asset $i$ to the [portfolio](An%20Asset%20Allocation%20Primer.md) depends approximately only on the asset's systematic risk because the idiosyncratic risk diversifies away in the [portfolio](An%20Asset%20Allocation%20Primer.md). Yet,    if the investor were to add a lot of asset $i$ to the [portfolio](An%20Asset%20Allocation%20Primer.md),    [portfolio return variance](.md) and the covariance of [portfolio](An%20Asset%20Allocation%20Primer.md) return and asset $i$ 's return changes. Moreover,    some of the risk that was idiosyncratic now becomes systematic: The higher the allocation to asset $i$,    the higher becomes the correlation of $R_{i}$ and $R_{w}$. In the extreme case,    where there is so much of asset $i$ in the [portfolio](An%20Asset%20Allocation%20Primer.md) that $R^{*} \approx R_{i}$,    the $\varepsilon_{i}$ component vanishes.

This illustrates that what an investor considers as systematic or idiosyncratic risk depends on her existing [portfolio](An%20Asset%20Allocation%20Primer.md). Since $\beta_{i}^{*}$ depends on what's in the investor's existing [portfolio](An%20Asset%20Allocation%20Primer.md),    $\beta_{i}^{*}$ will typically be different for different investors. Hence,    how investors perceive systematic risk of assets will also differ.

### 2.4 Maximum Sharpe ratio

We can also show that when the condition (2.29) holds,    and hence $R^{*}$ is truly the return on an optimal [portfolio](An%20Asset%20Allocation%20Primer.md) that cannot be improved any further,    then this optimal [portfolio](An%20Asset%20Allocation%20Primer.md) achieves the highest possible Sharpe Ratio of any [portfolio](An%20Asset%20Allocation%20Primer.md) that can be constructed from the available assets.

To see this,    start from (2.29),  
$$

\begin{equation*}

\mathbb{E}\left[Z_{i}\right]=\frac{\operatorname{cov}\left(Z_{i},  R^{*}\right)}{\operatorname{var}\left(R^{*}\right)} \mathbb{E}\left[Z^{*}\right] \tag{2.32}

\end{equation*}

$$

and let $\sigma_{i}=\operatorname{var}\left(Z_{i}\right)^{1 / 2},         \sigma=\operatorname{var}\left(R^{*}\right)^{1 / 2}$ and let $\rho_{i}$ denote the correlation of $Z_{i}$ and $R^{*}$. Since $\left|\rho_{i}\right| \leq 1$,    it is true that
$$

\begin{equation*}

\left|\operatorname{cov}\left(Z_{i},  R^{*}\right)\right|=\left|\rho_{i}\right| \sigma_{i} \sigma \leq \sigma_{i} \sigma \tag{2.33}

\end{equation*}

$$

Substituting this inequality into (2.32) and rearranging,    we get
$$

\begin{equation*}

\frac{\left|\mathbb{E}\left[Z_{i}\right]\right|}{\sigma_{i}} \leq \frac{\mathbb{E}\left[Z^{*}\right]}{\sigma} \tag{2.34}

\end{equation*}

$$

This tells us that the Sharpe ratio of any asset $i$ (or any combination of assets) cannot exceed the Sharpe ratio of the optimal [portfolio](An%20Asset%20Allocation%20Primer.md). In other words,    the [portfolio](An%20Asset%20Allocation%20Primer.md) with weights $\boldsymbol{\omega}^{*}$ that we constructed in (2.18) has the highest possible Sharpe ratio of any [portfolio](An%20Asset%20Allocation%20Primer.md) combining the same assets.

### 2.5 Market equilibrium

As we did in the previous lecture for a single risky asset,    we can again ask how the [Portfolio](Lecture%205-%20Dynamic%20[[An%20Asset%20Allocation%20Primer) Choice|[portfolio](An%20Asset%20Allocation%20Primer.md) choice]] of an individual investor fits together with the choices of other investors in equilibrium where supply equals demand. Our [market equilibrium analysis](../Financial%20Markets/Financial%20Asset%20Pricing%20Theory%20Overview/Chapter%201%20-%20Introduction%20and%20Overview/The%20Organization%20of%20This%20Book.md) in the previous lecture can be interpreted as dealing with the [demand and supply](../International%20Finance/China%20Foreign%20Exchange%20Reserves/Currency%20Appreciation%20and%20Depreciation.md) of risky assets as a whole class. Here we are now asking about the composition of risky asset portfolios: what sort of composition investors would like to have,    and how the market gets these desired [portfolio](An%20Asset%20Allocation%20Primer.md) weights in line with the supply of securities actually available. Because we are interested in this compositional question,    we now focus on the relative quantities of risky assets,    expressed as a proportion of the total [market capitalization](../Advanced%20Financial%20Analysis%20and%20Valuation/Financial%20Ratios/Price-to-Sales%20Ratios%20in%20Stock%20Valuation.md) of risky assets that investors demand or that is available as supply.

Supply is then given by the weights of the market [portfolio](An%20Asset%20Allocation%20Primer.md) of risky assets. This is the [portfolio](An%20Asset%20Allocation%20Primer.md) in which the weight of each asset is equal to ratio of the asset's [market capitalization](../Advanced%20Financial%20Analysis%20and%20Valuation/Financial%20Ratios/Price-to-Sales%20Ratios%20in%20Stock%20Valuation.md) (price times shares outstanding),    mcap $_{i}$,    to the aggregate [market capitalization](../Advanced%20Financial%20Analysis%20and%20Valuation/Financial%20Ratios/Price-to-Sales%20Ratios%20in%20Stock%20Valuation.md) of all risky assets:
$$

\begin{equation*}

\omega_{m,  i}=\frac{m_{c a p}}{\sum_{j=1}^{N} m_{c a p}^{j}} \tag{2.35}

\end{equation*}

$$

To see how equilibrium plays out,    in a first simple thought experiment,    suppose all investors want to hold the same [portfolio](An%20Asset%20Allocation%20Primer.md),    i.e,    they all want to have the same proportions

of risky assets in their portfolios. In this case it is very easy to see which [portfolio](An%20Asset%20Allocation%20Primer.md) they must necessarily end up with in equilibrium: the market [portfolio](An%20Asset%20Allocation%20Primer.md). Holding the market [portfolio](An%20Asset%20Allocation%20Primer.md) is the only way in which all investors can hold the same [portfolio](An%20Asset%20Allocation%20Primer.md). Then the weight of each asset in the market overall,    aggregated across all investors is the same as the weight the asset has in each investor's [portfolio](An%20Asset%20Allocation%20Primer.md). For example,    suppose each investor wants to hold $3/% of their portfolio,    in terms of market value,    in Apple stock. The only way this is possible is if the aggregate market capitalization of Apple is $3/% of the aggregate [market capitalization](../Advanced%20Financial%20Analysis%20and%20Valuation/Financial%20Ratios/Price-to-Sales%20Ratios%20in%20Stock%20Valuation.md) of all risky assets.

How would the market get to such an equilibrium in which the market clears? Prices need to adjust so that investors' desired [portfolio](An%20Asset%20Allocation%20Primer.md) weights end up being identical to market [portfolio](An%20Asset%20Allocation%20Primer.md) weights. Suppose for example that the market for Apple stock does not clear (yet): there is excess demand,    i.e. investors want to hold more shares of Apple than there are outstanding shares of Apple. This means that investors will bid up the price. This has two effects. First,    a rise in the price (with [expectations](../Fixed%20Income%20Asset%20Pricing/Fixed%20Income%20Lecture%20Notes/FORWARD%20RATES%20AND%20TERM%20STRUCTURE.md) of future [fundamentals](../Advanced%20Financial%20Analysis%20and%20Valuation/Lecture%20Notes%20Advanced%20Financial%20Analysis%20and%20Valuation/Week%202/Week%202%20Fundamentals%20Of%20Forecasting.md) unchanged) lowers the [expected return](Lecture%201-%20Probability%20Distributions%20of%20Returns.md) of Apple. This makes Apple stock less attractive. Hence investors' desired [portfolio](An%20Asset%20Allocation%20Primer.md) share of Apple,    and hence demand,    goes down. At the same time,    the rise in the price raises Apple's weight in the market [portfolio](An%20Asset%20Allocation%20Primer.md) and in each investor's [portfolio](An%20Asset%20Allocation%20Primer.md). So both of these effects of the price change work to get investors' desired [portfolio](An%20Asset%20Allocation%20Primer.md) weights closer to market [portfolio](An%20Asset%20Allocation%20Primer.md) weights. If the price rise is big enough,    desired [portfolio](An%20Asset%20Allocation%20Primer.md) weights and market [portfolio](An%20Asset%20Allocation%20Primer.md) become equal,    supply equals demand,    and the market therefore clears.

Now let's analyze what happens when investors not only want to hold identical portfolios,    but their demands come from [mean-variance](../Financial%20Markets/Financial%20Asset%20Pricing%20Theory%20Overview/Chapter%2012%20-%20Derivatives/Exercises.md) optimization: they all want to hold portfolios with weights according to our optimal risky [asset portfolio](../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%204/The%20Barbell%20Versus%20the%20Bullet.md) formula (2.18) and they have the same beliefs about expected [returns](../Financial%20Markets/Financial%20Asset%20Pricing%20Theory%20Overview/Chapter%203%20-%20%20Assets,%20Portfolios,%20and%20Arbitrage/Assets.md),    variances,    and covariances. Then prices of risky assets must adjust such that the optimal [portfolio](An%20Asset%20Allocation%20Primer.md) ends up being equal to the market [portfolio](An%20Asset%20Allocation%20Primer.md). And the return $R^{*}$ is then equal to the [market portfolio return](../Financial%20Markets/Financial%20Asset%20Pricing%20Theory%20Overview/Chapter%209%20-%20Factor%20Models/The%20Classical%20One-Period%20Capm.md) $R_{m}$. This means that the relationship in (2.29) now becomes
$$

\begin{equation*}

\mathbb{E}\left[Z_{i}\right]=\frac{\operatorname{cov}\left(Z_{i},  R_{m}\right)}{\operatorname{var}\left(R_{m}\right)} \mathbb{E}\left[Z_{m}\right]=\beta_{i} \mathbb{E}\left[Z_{m}\right] \tag{2.36}

\end{equation*}

$$

which is the [Capital Asset Pricing Model](../Financial%20Engineering/2.%20Forwards,%20Swaps,%20Futures,%20and%20Options.md) (CAPM)! So the CAPM results from combining the assumption that investors have identical beliefs about [risk and return](Lecture%207-Risk%20and%20Return%20of%20Bonds.md) and seek to hold [mean-variance](../Financial%20Markets/Financial%20Asset%20Pricing%20Theory%20Overview/Chapter%2012%20-%20Derivatives/Exercises.md) optimal portfolios with the market equilibrium condition that demand equals supply.

For the applications we focus on in this course,    the assumption that all investors want the same [portfolio](An%20Asset%20Allocation%20Primer.md) is not realistic. But,    still,    the market [portfolio](An%20Asset%20Allocation%20Primer.md) is an important reference point.

If we take a position different from the market [portfolio](An%20Asset%20Allocation%20Primer.md),    there must be,    for the market to clear,    someone willing to take the other side in the sense of also deviating from market [portfolio](An%20Asset%20Allocation%20Primer.md) weights,    but in the opposite direction. If we overweight an asset in our [portfolio](An%20Asset%20Allocation%20Primer.md),    then,    collectively,    the rest of the investors in the market have to underweight this asset. Therefore,    if we are entertaining such a deviation,    it is always important to ask: Why would anyone be willing to take the other side? Can we have confidence that we are right and the party taking the other side is not,    or that we have special circumstances (e.g.,    a better ability to bear certain types of risk than others) that make an asset more attractive to us than it is to others?

The market [portfolio](An%20Asset%20Allocation%20Primer.md) is a very special [portfolio](An%20Asset%20Allocation%20Primer.md). Aside from new issues of stocks,    delistings,    and needs to reinvest dividends,    holding the market [portfolio](An%20Asset%20Allocation%20Primer.md) does not require any trading. For example,    if we hold the market [portfolio](An%20Asset%20Allocation%20Primer.md) and the price of asset $i$ goes up from yesterday to today more than the market overall,    its weight in our [portfolio](An%20Asset%20Allocation%20Primer.md) goes up. However,    its weight goes up exactly the same in the market [portfolio](An%20Asset%20Allocation%20Primer.md). Hence,    we don't have to trade to keep holding the market [portfolio](An%20Asset%20Allocation%20Primer.md). This is why index funds typically follow value-weighted indices where asset weights depend on stocks' [market capitalization](../Advanced%20Financial%20Analysis%20and%20Valuation/Financial%20Ratios/Price-to-Sales%20Ratios%20in%20Stock%20Valuation.md) relative to the aggregate [market capitalization](../Advanced%20Financial%20Analysis%20and%20Valuation/Financial%20Ratios/Price-to-Sales%20Ratios%20in%20Stock%20Valuation.md) of all stocks in the index,    just like in the market [portfolio](An%20Asset%20Allocation%20Primer.md).

 ![500](CleanShot%202024-10-24%20-003106@2x.png)

Figure 2.1: Turnover rate of Vanguard Total [Stock Market](../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20III%20THE%20PLAYERS/Chapter%2012%20-%20Hedge%20Fund%20Strategies/Hedge%20Fund%20Strategies.md) Index Fund (VITNX)

Because trading needs are so minimal,    holding the market [portfolio](An%20Asset%20Allocation%20Primer.md),    or more generally a value-weighted [portfolio](An%20Asset%20Allocation%20Primer.md),    is very cheap in terms of trading cost. As an example,    Figure (2.1) shows some [portfolio](An%20Asset%20Allocation%20Primer.md) statistics for the Vanguard Total [Stock Market](../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20III%20THE%20PLAYERS/Chapter%2012%20-%20Hedge%20Fund%20Strategies/Hedge%20Fund%20Strategies.md) Index Fund. This is a fund that aims to replicate the performance of the entire market [portfolio](An%20Asset%20Allocation%20Primer.md) of U.S. stocks as represented by the CRSP value-weighted index. As the figure shows,    the turnover rate of this fund is less than $5/% per year. This means that only $5/% of the [portfolio](An%20Asset%20Allocation%20Primer.md)'s total value is traded each year. Most of this is accounted for by dividends,    proceeds from mergers that must be reinvested,    and [investment](An%20Asset%20Allocation%20Primer.md) in initial or seasoned public offerings that come to the market. But other than this,    there is basically no need to trade.

> [!Figure 2.2: From Pershing Square Capital Management Annual Letter 2015]
> popular indexes are market-cap weighted. This means that the larger the market cap of the company,    the larger its representation in the index. In other words,    as the [stock price](../Financial%20Engineering/Derivatives/Part%20IV%20-%20Options/Chapter%2016%20-%20Black–Scholes%20Model.md) rises,    its weighting in the index increases,    and the index fund is required to buy more of the company. While value investors typically buy more as stock prices decline (assuming intrinsic value has also not declined),    market-cap weighted index funds do the opposite. They are inherently momentum investors,    forced to buy more as stock prices rise,    magnifying the risk of overvaluation of the index components.
There is also a lot of misconception out there about the mechanics of running a market-capitalization weighted [portfolio](An%20Asset%20Allocation%20Primer.md) like the Vanguard Total [Stock Market](../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20III%20THE%20PLAYERS/Chapter%2012%20-%20Hedge%20Fund%20Strategies/Hedge%20Fund%20Strategies.md) Index Fund or any other market-capitalization weighted fund. One popular misconception is that market-cap weighting implies that the fund has to purchase more shares when prices go up. This fuels the concern that the presence of market-cap weighted funds in the market may lead to [asset price](../Financial%20Markets/Financial%20Asset%20Pricing%20Theory%20Overview/Chapter%204%20-%20State%20Prices/A%20Preview%20of%20Alternative%20Formulations.md) bubbles where price increases cause further mechanical buying,    which leads to further price increases not justified by [fundamentals](../Advanced%20Financial%20Analysis%20and%20Valuation/Lecture%20Notes%20Advanced%20Financial%20Analysis%20and%20Valuation/Week%202/Week%202%20Fundamentals%20Of%20Forecasting.md),    etc. Figure 2.2 shows an example from Bill Ackman's (Pershing Square Capital Management) 2015 letter to shareholders. This sort of argument is mistaken,    however. If the price of an asset in a market-cap weighted [portfolio](An%20Asset%20Allocation%20Primer.md) rises by $x/%,    then,    everything else equal,    the weight of the asset in a market-capitalization weighted index rises by $x/%. At the same time,    the weight of the asset in a market-capitalization weighted [portfolio](An%20Asset%20Allocation%20Primer.md) also rises by $x/%-without any trading. Therefore,    after this price change,    the asset's weight in the [portfolio](An%20Asset%20Allocation%20Primer.md) is still exactly equal to the share that a market-capitalization weighted index fund wants it to be. There is zero need to trade.

### 2.6 Estimation of return moments in the multiple risky asset case

Last lecture we discussed empirical estimation of mean and variance of [returns](../Financial%20Markets/Financial%20Asset%20Pricing%20Theory%20Overview/Chapter%203%20-%20%20Assets,%20Portfolios,%20and%20Arbitrage/Assets.md). To implement the optimal [portfolio](An%20Asset%20Allocation%20Primer.md) according to our formula (2.18),    we now also need an estimate of the covariance matrix $\boldsymbol{\Sigma}$. We can estimate it from historical [returns](../Financial%20Markets/Financial%20Asset%20Pricing%20Theory%20Overview/Chapter%203%20-%20%20Assets,%20Portfolios,%20and%20Arbitrage/Assets.md) as
$$

\begin{equation*}

\widehat{\boldsymbol{\Sigma}}=\frac{1}{T-1} \sum_{t=1}^{T}\left(\boldsymbol{R}*{t}-\hat{\boldsymbol{\mu}}\right)\left(\boldsymbol{R}*{t}-\hat{\boldsymbol{\mu}}\right)^{\prime} \tag{2.37}

\end{equation*}

$$

where
$$

\begin{equation*}

\hat{\boldsymbol{\mu}}=\frac{1}{T} \sum_{t=1}^{T} \boldsymbol{R}_{t} \tag{2.38}

\end{equation*}

$$

Table 2.1: Annualized mean,    standard deviations,    and correlations for various asset classes 1980-2022

 ![500](CleanShot%202024-10-24%20-003108@2x.png)
Table 2.1 shows an example from the same data of several asset classes that we already looked at last lecture. I broke the covariances into standard deviations (shown in the second row) and correlations (matrix below the second row). The underlying data are monthly [returns](../Financial%20Markets/Financial%20Asset%20Pricing%20Theory%20Overview/Chapter%203%20-%20%20Assets,%20Portfolios,%20and%20Arbitrage/Assets.md),    but I annualized the mean [returns](../Financial%20Markets/Financial%20Asset%20Pricing%20Theory%20Overview/Chapter%203%20-%20%20Assets,%20Portfolios,%20and%20Arbitrage/Assets.md) and standard deviations by multiplying with 12 and $\sqrt{12}$,    respectively.

Note that we are now considering Treasury bonds,    and also the other bond asset classes,    as risky assets. In Lecture 1,    we did a crude calculation of the average investor's risky asset share where we lumped Treasury bonds and other bonds into a broad riskfree asset class. Here we are now taking a more refined approach where only short-term Treasury bills are viewed as risk-free while bonds with maturities beyond one year are viewed as risky. And,    indeed,    the table above shows that the return standard deviations of the bond asset classes are substantial.

For the estimates of mean [returns](../Financial%20Markets/Financial%20Asset%20Pricing%20Theory%20Overview/Chapter%203%20-%20%20Assets,%20Portfolios,%20and%20Arbitrage/Assets.md),    we discussed in the last lecture how to estimate standard errors that give us an idea about the statistical uncertainty we have about expected [returns](../Financial%20Markets/Financial%20Asset%20Pricing%20Theory%20Overview/Chapter%203%20-%20%20Assets,%20Portfolios,%20and%20Arbitrage/Assets.md).

It would be useful to also get a sense for the statistical uncertainty about covariances. However,    the covariance matrix is a high-dimensional object. For our purposes it's not necessary to now write down and study the formula for the standard error of the whole covariance matrix estimate. But to get a sense of the magnitudes,    let's focus on the

standard error of the variance estimates (i.e.,    the entries on the diagonal of the covariance matrix). In the special case of normally distributed [returns](../Financial%20Markets/Financial%20Asset%20Pricing%20Theory%20Overview/Chapter%203%20-%20%20Assets,%20Portfolios,%20and%20Arbitrage/Assets.md),    the estimate of the variance of asset $i$ on the diagonal of the covariance matrix has standard error
$$

\begin{equation*}

\text { s.e. }\left(\hat{\sigma}*{i}^{2}\right)=\frac{\sqrt{2}}{\sqrt{T}} \sigma*{i}^{2} \tag{2.39}

\end{equation*}

$$

A back-of-the-envelope calculation: Let's say we estimate the variance of an aggregate [stock market](../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20III%20THE%20PLAYERS/Chapter%2012%20-%20Hedge%20Fund%20Strategies/Hedge%20Fund%20Strategies.md) index. Suppose the estimated standard deviation of annual [returns](../Financial%20Markets/Financial%20Asset%20Pricing%20Theory%20Overview/Chapter%203%20-%20%20Assets,%20Portfolios,%20and%20Arbitrage/Assets.md) on the aggregate [stock market](../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20III%20THE%20PLAYERS/Chapter%2012%20-%20Hedge%20Fund%20Strategies/Hedge%20Fund%20Strategies.md) index is roughly $20/% and so the variance is about $4/%. Then with 10 years of data,    s.e. $\left(\hat{\sigma}^{2}\right) \approx 0.018$. So,    using again a Bayesian interpretation,    as when we looked at the standard error of the mean last lecture,    we would conclude that with $95/% probability,    the true variance is in the interval $0.04 \pm 2 \times 0.018$. This is quite wide,    but not quite as wide as in the case of the estimate of $\mu$. With 100 years s.e. $\left(\hat{\sigma}^{2}\right) \approx 0.006$,    which is quite precise. Of course,    one can ask the same question about variance estimation that one can ask about estimation of the [expected return](Lecture%201-%20Probability%20Distributions%20of%20Returns.md): Is data from so long ago relevant for assessing the likely values of variance going forward?

However,    as we will see shortly,    there may be an opportunity to get much more precise estimates of variances and covariances by measuring [returns](../Financial%20Markets/Financial%20Asset%20Pricing%20Theory%20Overview/Chapter%203%20-%20%20Assets,%20Portfolios,%20and%20Arbitrage/Assets.md) over higher frequencies. Unfortunately,    the same trick is not going to work for getting more precise estimates of expected [returns](../Financial%20Markets/Financial%20Asset%20Pricing%20Theory%20Overview/Chapter%203%20-%20%20Assets,%20Portfolios,%20and%20Arbitrage/Assets.md).

### 2.6.1 Effect of measurement frequency on statistical precision

Since we can often choose the frequency at which we measure [returns](../Financial%20Markets/Financial%20Asset%20Pricing%20Theory%20Overview/Chapter%203%20-%20%20Assets,%20Portfolios,%20and%20Arbitrage/Assets.md),    we may wonder what is the best frequency? One way in which we might evaluate what's "best" is to focus on the effects on our statistical uncertainty about the true values of expected [returns](../Financial%20Markets/Financial%20Asset%20Pricing%20Theory%20Overview/Chapter%203%20-%20%20Assets,%20Portfolios,%20and%20Arbitrage/Assets.md) and variances. Having less statistical uncertainty is better. As it turns out,    there is a drastic difference in how the standard error of estimates of [expected return](Lecture%201-%20Probability%20Distributions%20of%20Returns.md) relates to measurement frequency and how the standard error of variances (and covariances) relates to measurement frequency.

Consider first the [expected return](Lecture%201-%20Probability%20Distributions%20of%20Returns.md). Suppose we have [returns](../Financial%20Markets/Financial%20Asset%20Pricing%20Theory%20Overview/Chapter%203%20-%20%20Assets,%20Portfolios,%20and%20Arbitrage/Assets.md) measured over $T$ periods,    say,    annual. The average return over these $T$ periods gives us the [expected return](Lecture%201-%20Probability%20Distributions%20of%20Returns.md) estimate $\hat{\mu}$. As we noted last lecture,    the standard error is
$$

\begin{equation*}

\text { s.e. }(\hat{\mu})=\frac{1}{\sqrt{T}} \sigma \text {. } \tag{2.40}

\end{equation*}

$$

But now we wonder whether we should perhaps chop each of these periods into $n$ smaller subperiods and measure [returns](../Financial%20Markets/Financial%20Asset%20Pricing%20Theory%20Overview/Chapter%203%20-%20%20Assets,%20Portfolios,%20and%20Arbitrage/Assets.md) at this higher frequency. We then have a total number

of periods of $T \times n$. Based on our annualization formulas from last lecture,    the expected [returns](../Financial%20Markets/Financial%20Asset%20Pricing%20Theory%20Overview/Chapter%203%20-%20%20Assets,%20Portfolios,%20and%20Arbitrage/Assets.md) at this higher measurement frequency would be approximately $1 / n$ times the annual average return,    i.e.,    $\mu / n$. The standard deviation would be $1 / \sqrt{n}$ times the standard deviation of annual [returns](../Financial%20Markets/Financial%20Asset%20Pricing%20Theory%20Overview/Chapter%203%20-%20%20Assets,%20Portfolios,%20and%20Arbitrage/Assets.md),    i.e.,    $\sigma / \sqrt{n}$. Therefore,    the standard error of the higher-frequency estimate $\hat{\mu}(n)$ would be
$$

\begin{equation*}

\text { s.e. }(\hat{\mu}(n))=\frac{1}{\sqrt{n T}} \frac{\sigma}{\sqrt{n}}=\frac{1}{\sqrt{T} n} \sigma \tag{2.41}

\end{equation*}

$$

This is $1 / n$ times the standard error of annual [returns](../Financial%20Markets/Financial%20Asset%20Pricing%20Theory%20Overview/Chapter%203%20-%20%20Assets,%20Portfolios,%20and%20Arbitrage/Assets.md). However,    as we discussed,    the magnitude of expected [returns](../Financial%20Markets/Financial%20Asset%20Pricing%20Theory%20Overview/Chapter%203%20-%20%20Assets,%20Portfolios,%20and%20Arbitrage/Assets.md) is also smaller by factor $1 / n$. Hence,    the ratio of true [expected return](Lecture%201-%20Probability%20Distributions%20of%20Returns.md) to standard error remains unchanged. It is invariant to the measurement frequency! So chopping the return measurement intervals into smaller pieces is not going to help us at all to get more precise estimates of expected [returns](../Financial%20Markets/Financial%20Asset%20Pricing%20Theory%20Overview/Chapter%203%20-%20%20Assets,%20Portfolios,%20and%20Arbitrage/Assets.md). If we make the measurement intervals smaller,    the signal (true [expected return](Lecture%201-%20Probability%20Distributions%20of%20Returns.md)) shrinks at the same rate as the standard error.

As a consequence,    if we annualize the higher-frequency estimate in order to get an apples-to-applies comparison,    i.e.,    we look at $n \hat{\mu}(n)$,    then the standard error for this annualized estimate is simply $n \times$ s.e. $(\hat{\mu}(n))=\frac{1}{\sqrt{T}} \sigma$,    i.e.,    exactly the same as the standard error when we use annual [returns](../Financial%20Markets/Financial%20Asset%20Pricing%20Theory%20Overview/Chapter%203%20-%20%20Assets,%20Portfolios,%20and%20Arbitrage/Assets.md)!

This is a very important lesson. If we are trying to improve the precision of our [expected return](Lecture%201-%20Probability%20Distributions%20of%20Returns.md) estimates,    it's of no use to go to higher return measurement frequency! Say we have 30 years of data at most on an asset and we use the average return as an estimate of the [expected return](Lecture%201-%20Probability%20Distributions%20of%20Returns.md). Then the total length of this sample period,    30 years,    effectively pins down the standard error of the [expected return](Lecture%201-%20Probability%20Distributions%20of%20Returns.md) estimates. It does not matter for the statistical precision of our estimate whether we measure the [returns](../Financial%20Markets/Financial%20Asset%20Pricing%20Theory%20Overview/Chapter%203%20-%20%20Assets,%20Portfolios,%20and%20Arbitrage/Assets.md) annually,    monthly,    daily,    or at some other frequency.

Now,    interestingly,    the situation is very different for variances and covariances. Recall that for the variance estimate,    the standard error is
$$

\begin{equation*}

\text { s.e. }\left(\hat{\sigma}^{2}\right)=\frac{\sqrt{2}}{\sqrt{T}} \sigma^{2} \tag{2.42}

\end{equation*}

$$

The key is that this standard error depends on the variance,    while the standard error of the mean in (2.40) depends on the standard deviation. If we divide the return measurement periods into $n$ subperiods,    then this variance falls by a factor of $1 / n$. The standard error of the higher-frequency estimate $\hat{\sigma}(n)^{2}$ becomes
$$

\begin{equation*}

\text { s.e. }\left(\hat{\sigma}(n)^{2}\right)=\frac{\sqrt{2}}{\sqrt{n T}} \frac{\sigma^{2}}{n}=\frac{1}{n^{3 / 2}} \frac{\sqrt{2}}{\sqrt{T}} \sigma^{2} \tag{2.43}

\end{equation*}

$$

If we look at the ratio of the true variance,    which falls by factor of $1 / n$ and the standard error,    which falls by a factor of $\frac{1}{n^{3 / 2}}$,    we see that the ratio rises by $(1 / n) / n^{3 / 2}=\sqrt{n}$. In other words,    the standard error falls relative to the true variance. This means we gain in precision!

If we annualize the higher-frequency variance estimate,    i.e.,    we look at $n \hat{\sigma}(n)^{2}$,    then the standard error for this annualized estimate is
$$

\begin{equation*}

n \text { s.e. }\left(\hat{\sigma}(n)^{2}\right)=\frac{1}{\sqrt{n}} \frac{\sqrt{2}}{\sqrt{T}} \sigma^{2} \tag{2.44}

\end{equation*}

$$

which is smaller,    by factor $1 / \sqrt{n}$,    than the standard error when we use annual [returns](../Financial%20Markets/Financial%20Asset%20Pricing%20Theory%20Overview/Chapter%203%20-%20%20Assets,%20Portfolios,%20and%20Arbitrage/Assets.md). The same factor applies to covariances as well,    but we are not going to show this explicitly.

 ![500](Attachments/500-997.jpg)

Figure 2.3: Distribution of annualized mean estimates when [returns](../Financial%20Markets/Financial%20Asset%20Pricing%20Theory%20Overview/Chapter%203%20-%20%20Assets,%20Portfolios,%20and%20Arbitrage/Assets.md) are measured at different measurement frequencies

Figures 2.3 and 2.4 illustrate this with simulations. I simulate $T=10,        000$ daily [returns](../Financial%20Markets/Financial%20Asset%20Pricing%20Theory%20Overview/Chapter%203%20-%20%20Assets,%20Portfolios,%20and%20Arbitrage/Assets.md) by drawing from a normal distribution such that the annualized [returns](../Financial%20Markets/Financial%20Asset%20Pricing%20Theory%20Overview/Chapter%203%20-%20%20Assets,%20Portfolios,%20and%20Arbitrage/Assets.md) (assuming 250 trading days per year) have mean 0.05 and standard deviation 0.20 . I calculate the mean and standard deviation of these daily [returns](../Financial%20Markets/Financial%20Asset%20Pricing%20Theory%20Overview/Chapter%203%20-%20%20Assets,%20Portfolios,%20and%20Arbitrage/Assets.md). Then I aggregate the [returns](../Financial%20Markets/Financial%20Asset%20Pricing%20Theory%20Overview/Chapter%203%20-%20%20Assets,%20Portfolios,%20and%20Arbitrage/Assets.md) to annual [returns](../Financial%20Markets/Financial%20Asset%20Pricing%20Theory%20Overview/Chapter%203%20-%20%20Assets,%20Portfolios,%20and%20Arbitrage/Assets.md) by summing the daily [returns](../Financial%20Markets/Financial%20Asset%20Pricing%20Theory%20Overview/Chapter%203%20-%20%20Assets,%20Portfolios,%20and%20Arbitrage/Assets.md) within 250 -day windows (if I do it by

 ![500](Attachments/500-998.jpg)

Figure 2.4: Distribution of annualized standard deviation estimates when [returns](../Financial%20Markets/Financial%20Asset%20Pricing%20Theory%20Overview/Chapter%203%20-%20%20Assets,%20Portfolios,%20and%20Arbitrage/Assets.md) are measured at different measurement frequencies

properly compounding the daily [returns](../Financial%20Markets/Financial%20Asset%20Pricing%20Theory%20Overview/Chapter%203%20-%20%20Assets,%20Portfolios,%20and%20Arbitrage/Assets.md),    the results are very similar). I calculate the mean and standard deviation of these annual [returns](../Financial%20Markets/Financial%20Asset%20Pricing%20Theory%20Overview/Chapter%203%20-%20%20Assets,%20Portfolios,%20and%20Arbitrage/Assets.md). Then I repeat this 1,    000 times each with a new random draw of a daily return series of length $T=10,        000$.

Figures 2.3 shows that the distribution of the mean of annual [returns](../Financial%20Markets/Financial%20Asset%20Pricing%20Theory%20Overview/Chapter%203%20-%20%20Assets,%20Portfolios,%20and%20Arbitrage/Assets.md) and distribution of the annualized mean estimated from daily [returns](../Financial%20Markets/Financial%20Asset%20Pricing%20Theory%20Overview/Chapter%203%20-%20%20Assets,%20Portfolios,%20and%20Arbitrage/Assets.md) (i.e.g,    daily return mean times 250) is basically identical,    as expected based on our earlier standard error calculations. In contrast,    Figure 2.4 shows that the distribution of annualized standard deviations estimated from daily [returns](../Financial%20Markets/Financial%20Asset%20Pricing%20Theory%20Overview/Chapter%203%20-%20%20Assets,%20Portfolios,%20and%20Arbitrage/Assets.md) (i.e.,    daily return standard deviation times $\sqrt{250}$ ) is far smaller than the standard deviation of annual [returns](../Financial%20Markets/Financial%20Asset%20Pricing%20Theory%20Overview/Chapter%203%20-%20%20Assets,%20Portfolios,%20and%20Arbitrage/Assets.md). The annualized standard deviations estimated from daily [returns](../Financial%20Markets/Financial%20Asset%20Pricing%20Theory%20Overview/Chapter%203%20-%20%20Assets,%20Portfolios,%20and%20Arbitrage/Assets.md) are much closer to the true standard deviation of 0.20. In other words,    these estimates are much more precise.

This is potentially extremely useful. The covariance matrix $\boldsymbol{\Sigma}$ is an important input into the [mean-variance](../Financial%20Markets/Financial%20Asset%20Pricing%20Theory%20Overview/Chapter%2012%20-%20Derivatives/Exercises.md) optimal [portfolio](An%20Asset%20Allocation%20Primer.md) formula. If it is estimated with too much error,    the error may render the estimated [portfolio](An%20Asset%20Allocation%20Primer.md) weights useless. This is,    in fact,    one of the major problems that practical applications of [portfolio optimization](../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20III%20THE%20PLAYERS/Chapter%2011%20-%20Individual%20Investors-A%20Survey%20of%20Modern%20Investment%20Theory/The%20Modern%20Portfolio%20Theory%20and%20the%20Capm.md) struggle with and where clever improvements can make a difference. One first step is to do what our analysis above suggests: Make the estimate of $\boldsymbol{\Sigma}$ more precise by using higher-frequency

data (say,    daily or weekly rather than annual data). In Table 2.1 I have used monthly data,    which is not as good as daily or weekly,    but better than annual.

That said,    while higher-frequency data is useful for covariance matrix estimation,    we also need to keep in mind some limitations.

First,    by going to higher measurement frequencies,    we can only get more precise estimates of variances if random shocks to [returns](../Financial%20Markets/Financial%20Asset%20Pricing%20Theory%20Overview/Chapter%203%20-%20%20Assets,%20Portfolios,%20and%20Arbitrage/Assets.md) over longer periods are always composed of smaller random shocks over shorter subperiods. This means that,    for example,    for variances of daily [returns](../Financial%20Markets/Financial%20Asset%20Pricing%20Theory%20Overview/Chapter%203%20-%20%20Assets,%20Portfolios,%20and%20Arbitrage/Assets.md) to give us more precise estimates than variances of monthly [returns](../Financial%20Markets/Financial%20Asset%20Pricing%20Theory%20Overview/Chapter%203%20-%20%20Assets,%20Portfolios,%20and%20Arbitrage/Assets.md),    the monthly [returns](../Financial%20Markets/Financial%20Asset%20Pricing%20Theory%20Overview/Chapter%203%20-%20%20Assets,%20Portfolios,%20and%20Arbitrage/Assets.md) should be composed of a steady series of random shocks,    as opposed to just occasional jumps in prices on a few days with little price movement inbetween these infrequent jumps. ${ }^{1}$ To illustrate: Suppose once every ten years,    the [stock market](../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20III%20THE%20PLAYERS/Chapter%2012%20-%20Hedge%20Fund%20Strategies/Hedge%20Fund%20Strategies.md) experiences a day in which the market crashes with a huge negative return on a single day (say,    $-20/% ). Let's also stick to the notion that [returns](../Financial%20Markets/Financial%20Asset%20Pricing%20Theory%20Overview/Chapter%203%20-%20%20Assets,%20Portfolios,%20and%20Arbitrage/Assets.md) are serially independent. Hence a crash is not followed by a predictable reversal of stock prices afterwards. If we have data that spans ten years and includes one of those crashes,    the variance estimate will capture the existence of such crashes. While variance as a [risk measure](../Financial%20Instruments/Leverage%20as%20a%20Measure%20of%20Risk.md) might not do enough to properly characterize the severity of the crash,    if the data includes the crash,    the variance estimate will be substantially increased by the crash data point. However,    dividing return measurement intervals into shorter periods is not going to help us to get a more precise estimate of the frequency and magnitude of such crashes because most return measurement periods do not include a crash.

[Market microstructure](../Financial%20Markets%20and%20Institutions/III.%20Liquidity%20of%20Assets/Class%205-%20Private%20Information,%20Liquidity,%20and%20Securitization/Bid%20Ask%20and%20Transaction%20Prices%20in%20a%20Specialist%20Market%20With%20Heterogeneously%20Informed%20Traders.md) can also interfere if we try to measure [returns](../Financial%20Markets/Financial%20Asset%20Pricing%20Theory%20Overview/Chapter%203%20-%20%20Assets,%20Portfolios,%20and%20Arbitrage/Assets.md) from [transaction prices](../Financial%20Markets%20and%20Institutions/III.%20Liquidity%20of%20Assets/Class%205-%20Private%20Information,%20Liquidity,%20and%20Securitization/Bid%20Ask%20and%20Transaction%20Prices%20in%20a%20Specialist%20Market%20With%20Heterogeneously%20Informed%20Traders.md) at very high frequency,    especially for assets that are relatively illiquid. At high time resolution,    [returns](../Financial%20Markets/Financial%20Asset%20Pricing%20Theory%20Overview/Chapter%203%20-%20%20Assets,%20Portfolios,%20and%20Arbitrage/Assets.md) can be distorted by the [bid-ask spread](../Financial%20Markets%20and%20Institutions/III.%20Liquidity%20of%20Assets/Class%205-%20Private%20Information,%20Liquidity,%20and%20Securitization/Bid%20Ask%20and%20Transaction%20Prices%20in%20a%20Specialist%20Market%20With%20Heterogeneously%20Informed%20Traders.md),    for example. If a buy order comes in,    it gets executed at the (high) ask price,    if a sell order comes in,    it gets executed at the (low) bid price. As a flow of orders comes in,    randomly switching between buys and sells,    the prices at which transactions occur tends to bounce around between the lower bid and higher ask prices. If we measure [returns](../Financial%20Markets/Financial%20Asset%20Pricing%20Theory%20Overview/Chapter%203%20-%20%20Assets,%20Portfolios,%20and%20Arbitrage/Assets.md) at such high frequency that we capture a lot of this bouncing around between [bid and ask](../Financial%20Markets%20and%20Institutions/III.%20Liquidity%20of%20Assets/Class%205-%20Private%20Information,%20Liquidity,%20and%20Securitization/Class%20Note%209%20Bid%20and%20Ask%20Prices%20With%20Private%20Information.md),    but this bouncing between [bid and ask](../Financial%20Markets%20and%20Institutions/III.%20Liquidity%20of%20Assets/Class%205-%20Private%20Information,%20Liquidity,%20and%20Securitization/Class%20Note%209%20Bid%20and%20Ask%20Prices%20With%20Private%20Information.md) is not really reflecting any variation in the value of the asset. This means a variance estimate based on very high-frequency return data may overstate the true variance because it contains the [bid-ask](../Financial%20Markets%20and%20Institutions/III.%20Liquidity%20of%20Assets/Class%205-%20Private%20Information,%20Liquidity,%20and%20Securitization/Bid-Ask%20Prices%20with%20Adverse%20SelectionPrivate%20Information.md) bounce effects in addition to variance in the value of the asset.

[^6]Non-synchronicity effects are another microstructure phenomenon that will distort covariance estimates constructed from [transaction prices](../Financial%20Markets%20and%20Institutions/III.%20Liquidity%20of%20Assets/Class%205-%20Private%20Information,%20Liquidity,%20and%20Securitization/Bid%20Ask%20and%20Transaction%20Prices%20in%20a%20Specialist%20Market%20With%20Heterogeneously%20Informed%20Traders.md) at very high frequency. Suppose you have two assets: Asset $A$ which is very liquid and usually trades every microsecond,    and asset $B$ which is very illiquid and trades only about once per hour. If we go to very high frequency - say,    5 minute [returns](../Financial%20Markets/Financial%20Asset%20Pricing%20Theory%20Overview/Chapter%203%20-%20%20Assets,%20Portfolios,%20and%20Arbitrage/Assets.md) - to estimate covariances,    it will happen very often that there is a piece of news that affects the true value of both assets,    but only the price of liquid asset $A$ responds immediately,    while it may often take another hour or so until the price of asset $B$ adjusts. But this stale price of asset $B$ that is recorded in a [returns](../Financial%20Markets/Financial%20Asset%20Pricing%20Theory%20Overview/Chapter%203%20-%20%20Assets,%20Portfolios,%20and%20Arbitrage/Assets.md) data file is not a true price. If someone actually tried to trade,    the price would adjust. It just didn't because it happened to be the case that nobody wanted to trade. With such non-synchronicity of prices,    it may seem,    based on 5 minute return data that the covariance of the [returns](../Financial%20Markets/Financial%20Asset%20Pricing%20Theory%20Overview/Chapter%203%20-%20%20Assets,%20Portfolios,%20and%20Arbitrage/Assets.md) of asset $A$ and $B$ is really low,    when in fact it is much higher. In contrast,    covariances estimated from daily [returns](../Financial%20Markets/Financial%20Asset%20Pricing%20Theory%20Overview/Chapter%203%20-%20%20Assets,%20Portfolios,%20and%20Arbitrage/Assets.md) in this example would have virtually no distortion from non-synchronicity and would reveal a higher covariance.

Similar problems can appear when assets are traded in different time zones. A [returns](../Financial%20Markets/Financial%20Asset%20Pricing%20Theory%20Overview/Chapter%203%20-%20%20Assets,%20Portfolios,%20and%20Arbitrage/Assets.md) data set may record daily prices for assets on the same day,    but if one asset traded in Tokyo and the other in New York,    they are clearly not measured at the same point in time. Hence,    a covariance estimate based on these daily [returns](../Financial%20Markets/Financial%20Asset%20Pricing%20Theory%20Overview/Chapter%203%20-%20%20Assets,%20Portfolios,%20and%20Arbitrage/Assets.md) would underestimate the true covariance.

An extreme form of this latter problem shows up with highly [illiquid assets](../Financial%20Markets%20and%20Institutions/III.%20Liquidity%20of%20Assets/Class%205-%20Private%20Information,%20Liquidity,%20and%20Securitization/Class%20Note%2010%20Liquidity%20and%20Class%20Note%2010%20Liquidity%20and%20Liquidity%20Managementliquidity%20management.md) like [private equity](../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20III%20THE%20PLAYERS/Chapter%2014%20-%20Private%20Equity,%20Pension,%20and%20Sovereign%20Funds/Private%20Equity.md),    private-market [debt securities](../Fixed%20Income%20Asset%20Pricing/Analysis%20of%20Fixed%20Income%20Securities.md),    and infrastructure assets. These assets rarely trade. And if we don't observe market prices regularly,    it's difficult to estimate covariances,    and,    as a consequence,    it's difficult to figure out how much risk such assets bring to a [portfolio](An%20Asset%20Allocation%20Primer.md). More on this in lecture 9.

### 2.7 Optimal portfolio weights based on empirical estimates of return moments

Now let's use the estimates of means and covariances in Table 2.1 to construct the [mean-variance](../Financial%20Markets/Financial%20Asset%20Pricing%20Theory%20Overview/Chapter%2012%20-%20Derivatives/Exercises.md) optimal risky [asset portfolio](../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%204/The%20Barbell%20Versus%20the%20Bullet.md) according to our formula (2.18) which I repeat here:
$$

\begin{equation*}

\boldsymbol{\omega}^{*}=\frac{1}{\boldsymbol{\iota}^{\prime} \boldsymbol{\Sigma}^{-1} \boldsymbol{\mu}} \boldsymbol{\Sigma}^{-1} \boldsymbol{\mu} \tag{2.45}

\end{equation*}

$$

I now use a plug-in approach where we simply replace the vector $\boldsymbol{\mu}$ with the mean excess [returns](../Financial%20Markets/Financial%20Asset%20Pricing%20Theory%20Overview/Chapter%203%20-%20%20Assets,%20Portfolios,%20and%20Arbitrage/Assets.md) estimates from Table 2.1,    which I label $\overline{\boldsymbol{z}}$,    and the covariance matrix $\boldsymbol{\Sigma}$ with the

estimated covariance matrix from Table 2.1 (recall that a covariance is the product of the two standard deviations of the pair of [asset returns](../Financial%20Markets/Financial%20Asset%20Pricing%20Theory%20Overview/Chapter%201%20-%20Introduction%20and%20Overview/Some%20Stylized%20Empirical%20Facts%20About%20Asset%20Retur.md) and their correlation),    which I label $\widehat{\boldsymbol{\Sigma}}$. I then calculate
$$

\begin{equation*}

\hat{\omega}^{*}=\frac{1}{\iota^{\prime} \widehat{\boldsymbol{\Sigma}}^{-1} \overline{\boldsymbol{z}}} \widehat{\boldsymbol{\Sigma}}^{-1} \overline{\boldsymbol{z}} \tag{2.46}

\end{equation*}

$$

 ![500](https://cdn.mathpix.com/cropped/2024_10_19_48a1c4654e845915c45cg-052.jpg?height=1012&width=1201&top_left_y=594&top_left_x=424)

Figure 2.5: Optimal allocation of risky [asset portfolio](../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%204/The%20Barbell%20Versus%20the%20Bullet.md) based on estimated return moments

Figure 2.5 presents the result. The bars in this figure show the elements of the [portfolio weight vector](../Financial%20Markets/Financial%20Asset%20Pricing%20Theory%20Overview/Chapter%203%20-%20%20Assets,%20Portfolios,%20and%20Arbitrage/Portfolios%20and%20Trading%20Strategies.md) $\hat{\boldsymbol{\omega}}^{*}$. This result may be somewhat surprising. The [portfolio](An%20Asset%20Allocation%20Primer.md) is mostly a combination of long positions in government bonds (U.S. Treasury and international) and domestic value stocks,    as well as a short position in international stocks. Other asset classes only play a minor role.

These results are quite sensitive to the inputs,    though. So our work is not done yet.

A first step to understand a bit better the potential fragility of the plug-in solution to the optimal [portfolio](An%20Asset%20Allocation%20Primer.md) problem is to conduct a [sensitivity analysis](../Advanced%20Financial%20Analysis%20and%20Valuation/DCF%20Breakdown.md). In general,    it's quite difficult to predict how changes in a small number of inputs affects the optimal [portfolio](An%20Asset%20Allocation%20Primer.md) weights. The covariance matrix is a big object. It's difficult to tease out simple

relationships between inputs to the formula and the optimal weights that are the outputs when the formula involves an inverse of a relatively big covariance matrix. All of the elements of the covariance matrix and the mean return vector can interact in ways that are difficult to isolate. But we can sometimes get a rough idea by seeing what happens when we change some of the input numbers.

The perhaps most striking fact of the [portfolio](An%20Asset%20Allocation%20Primer.md) in Figure 2.5 is the high allocation to bonds. One may be concerned that,    at least in part,    this is a consequence of the fact that bond [returns](../Financial%20Markets/Financial%20Asset%20Pricing%20Theory%20Overview/Chapter%203%20-%20%20Assets,%20Portfolios,%20and%20Arbitrage/Assets.md) have been fantastic during the past 40 years that our data covers in this exercise. At the beginning of this four-decade period,    [interest rates](../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%202/Interest%20Rate%20Quotations.md) were very high and they have trended down throughout these four decades. This long downward trend was certainly not fully anticipated in the early 1980s when [interest rates](../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%202/Interest%20Rate%20Quotations.md) were high. As a consequence,    part of the high [returns](../Financial%20Markets/Financial%20Asset%20Pricing%20Theory%20Overview/Chapter%203%20-%20%20Assets,%20Portfolios,%20and%20Arbitrage/Assets.md) that bonds realized over the past 40 years was an unexpected positive surprise. So our estimates of expected excess [returns](../Financial%20Markets/Financial%20Asset%20Pricing%20Theory%20Overview/Chapter%203%20-%20%20Assets,%20Portfolios,%20and%20Arbitrage/Assets.md) based on historical [returns](../Financial%20Markets/Financial%20Asset%20Pricing%20Theory%20Overview/Chapter%203%20-%20%20Assets,%20Portfolios,%20and%20Arbitrage/Assets.md) from the past four decades may overstate the [returns](../Financial%20Markets/Financial%20Asset%20Pricing%20Theory%20Overview/Chapter%203%20-%20%20Assets,%20Portfolios,%20and%20Arbitrage/Assets.md) that can be expected going forward. We will look into all this in much greater detail when we discuss bonds and [interest rates](../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%202/Interest%20Rate%20Quotations.md) in a future session. But for now let's just do a simple sensitivity check: How do the results change if we reduce our estimate of the expected excess [returns](../Financial%20Markets/Financial%20Asset%20Pricing%20Theory%20Overview/Chapter%203%20-%20%20Assets,%20Portfolios,%20and%20Arbitrage/Assets.md) of the three bond categories by one (annualized) percentage point?

One percentage point is not much. Recall that in the last lecture we estimated the standard error of the mean [returns](../Financial%20Markets/Financial%20Asset%20Pricing%20Theory%20Overview/Chapter%203%20-%20%20Assets,%20Portfolios,%20and%20Arbitrage/Assets.md) in the three bond categories and the standard error was roughly one percent for each of them. So in this sensitivity check we are just considering a relatively mild deviation of one standard error.

Subtracting one percentage point from the mean [returns](../Financial%20Markets/Financial%20Asset%20Pricing%20Theory%20Overview/Chapter%203%20-%20%20Assets,%20Portfolios,%20and%20Arbitrage/Assets.md) of the three bond categories and then recalculating the optimal [portfolio](An%20Asset%20Allocation%20Primer.md) yields weights of shown in Figure 2.6a. Comparing with the weights before this modification,    we see a reduction in the allocation to international and [Corporate Bonds](../Financial%20Markets%20and%20Institutions/II.%20The%20Roles%20of%20Banks%20and%20Derivative%20Markets%20in%20Resolving%20Problems%20Inherent%20in%20Debt%20Contracts/Class%202-%20Debt%20Contracts%20due%20to%20Lack%20of%20Information/Class%20Notes%202%20–%20Corporate%20Bond%20Contracts.md),    but,    surprisingly,    an increase in the U.S. Treasury bond allocation. This illustrates how difficult it is to anticipate the change in the optimal [portfolio](An%20Asset%20Allocation%20Primer.md) weights that results from changing some of the inputs of the [portfolio](An%20Asset%20Allocation%20Primer.md) formula. The overall allocation to bonds of all three categories combined does not seem very sensitive to the potentially too optimistic bond return [expectations](../Fixed%20Income%20Asset%20Pricing/Fixed%20Income%20Lecture%20Notes/FORWARD%20RATES%20AND%20TERM%20STRUCTURE.md).

Another useful sensitivity check can help us understand the conditions that lead to short positions in international stocks in the optimized [portfolio](An%20Asset%20Allocation%20Primer.md). Looking back at Table 2.1 and focusing on the stock asset classes,    we see that the three stocks asset classes - domestic,    international,    and value stocks-have high correlations above 0.60. At the same time,    the mean excess [returns](../Financial%20Markets/Financial%20Asset%20Pricing%20Theory%20Overview/Chapter%203%20-%20%20Assets,%20Portfolios,%20and%20Arbitrage/Assets.md) are quite different,    with value stocks having about four percentage points higher mean excess [returns](../Financial%20Markets/Financial%20Asset%20Pricing%20Theory%20Overview/Chapter%203%20-%20%20Assets,%20Portfolios,%20and%20Arbitrage/Assets.md) than international stocks,    and domestic stocks somewhere inbetween. From a [portfolio optimization](../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20III%20THE%20PLAYERS/Chapter%2011%20-%20Individual%20Investors-A%20Survey%20of%20Modern%20Investment%20Theory/The%20Modern%20Portfolio%20Theory%20and%20the%20Capm.md) viewpoint,    this looks like an opportunity to construct a position that earns high [expected return](Lecture%201-%20Probability%20Distributions%20of%20Returns.md) with

 ![500](https://cdn.mathpix.com/cropped/2024_10_19_48a1c4654e845915c45cg-054.jpg?height=1410&width=966&top_left_y=290&top_left_x=536)

(b) Mean excess return of international stocks raised to be the same as domestic stocks

Figure 2.6: [Sensitivity analysis](../Advanced%20Financial%20Analysis%20and%20Valuation/DCF%20Breakdown.md)

little risk: go long value stocks and short international stocks. This position earns the spread in mean [returns](../Financial%20Markets/Financial%20Asset%20Pricing%20Theory%20Overview/Chapter%203%20-%20%20Assets,%20Portfolios,%20and%20Arbitrage/Assets.md) between the two asset classes. At the same time,    due to the high correlation,    much of the unexpected movements in [returns](../Financial%20Markets/Financial%20Asset%20Pricing%20Theory%20Overview/Chapter%203%20-%20%20Assets,%20Portfolios,%20and%20Arbitrage/Assets.md) cancel out. High correlation means that the [returns](../Financial%20Markets/Financial%20Asset%20Pricing%20Theory%20Overview/Chapter%203%20-%20%20Assets,%20Portfolios,%20and%20Arbitrage/Assets.md) tend to move together in the same direction; so then going long in one asset and short the other means that the [returns](../Financial%20Markets/Financial%20Asset%20Pricing%20Theory%20Overview/Chapter%203%20-%20%20Assets,%20Portfolios,%20and%20Arbitrage/Assets.md) offset to a large extent,    leaving very little [residual risk](../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%205%20Options%20on%20Prices%20and%20Hedge-Based%20Valuation/Residual%20Risk%20of%20Options%20Gamma%20Vega%20and%20Volatil.md) relative to the size of the spread in mean [returns](../Financial%20Markets/Financial%20Asset%20Pricing%20Theory%20Overview/Chapter%203%20-%20%20Assets,%20Portfolios,%20and%20Arbitrage/Assets.md) that the position earns.

We can see this mechanism at work when we change the mean return inputs. I set the mean excess return of international stocks to be the same as domestic stocks,    i.e.,    1.9 percentage points higher relative to the estimate from historical data. Recalculating the optimal [portfolio](An%20Asset%20Allocation%20Primer.md) weights we get the allocations shown in Figure 2.6b. Now the short position in international stocks is gone. But bond allocations change,    too,    even though we made no change to bond [expected return](Lecture%201-%20Probability%20Distributions%20of%20Returns.md) or covariance estimates,    which illustrates again how difficult it is to predict what happens to optimal allocations when one changes a few of the inputs.

Another way of checking sensitivity is to examine how the optimal weights change if we use inputs from different time periods. For this exercise,    I estimate mean excess [returns](../Financial%20Markets/Financial%20Asset%20Pricing%20Theory%20Overview/Chapter%203%20-%20%20Assets,%20Portfolios,%20and%20Arbitrage/Assets.md) and the covariance matrix over 10-year periods. I start at the beginning of 1990 and use data from 1980 to 1989 to calculate the optimal weights. Then I move the data window forward by one month and recalculate the weights; then I repeat until the end 10 -year data window reaches the end of the data set at the end of 2022.

 ![500](https://cdn.mathpix.com/cropped/2024_10_19_48a1c4654e845915c45cg-055.jpg?height=941&width=1185&top_left_y=1058&top_left_x=486)

Figure 2.7: Weights of estimated [mean-variance](../Financial%20Markets/Financial%20Asset%20Pricing%20Theory%20Overview/Chapter%2012%20-%20Derivatives/Exercises.md) efficient [portfolio](An%20Asset%20Allocation%20Primer.md) without shrinkage (10 years of data to estimate means and covariances)

Figure 2.7 shows the results. In the latest decade,    the weights are somewhat stable and not too extreme. But in the first decade,    they take extreme values: In the early years we see weights of more than $400/% in [Corporate Bonds](../Financial%20Markets%20and%20Institutions/II.%20The%20Roles%20of%20Banks%20and%20Derivative%20Markets%20in%20Resolving%20Problems%20Inherent%20in%20Debt%20Contracts/Class%202-%20Debt%20Contracts%20due%20to%20Lack%20of%20Information/Class%20Notes%202%20–%20Corporate%20Bond%20Contracts.md) and a roughly similarly sized

short position in Treasury bonds. This is effectively an extremely highly levered bet on corporate credit. Based on 10-year lagged data on [returns](../Financial%20Markets/Financial%20Asset%20Pricing%20Theory%20Overview/Chapter%203%20-%20%20Assets,%20Portfolios,%20and%20Arbitrage/Assets.md),    and taking these data as the true expected excess [returns](../Financial%20Markets/Financial%20Asset%20Pricing%20Theory%20Overview/Chapter%203%20-%20%20Assets,%20Portfolios,%20and%20Arbitrage/Assets.md) and covariances,    this looked like an attractive position back then.

But we should be skeptical about such extreme weights coming out of a [portfolio optimization](../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20III%20THE%20PLAYERS/Chapter%2011%20-%20Individual%20Investors-A%20Survey%20of%20Modern%20Investment%20Theory/The%20Modern%20Portfolio%20Theory%20and%20the%20Capm.md) formula. After all,    if such an extreme long-short bet was so attractive in the 1990s,    how come other investors didn't exploit it? If they had tried to exploit it,    prices of corporate and treasury bonds would have adjusted to make the trade less attractive.

And there is good statistical reason to be skeptical. With 10-year data windows,    the estimates of mean excess [returns](../Financial%20Markets/Financial%20Asset%20Pricing%20Theory%20Overview/Chapter%203%20-%20%20Assets,%20Portfolios,%20and%20Arbitrage/Assets.md) are very imprecise. With 10-years of data,    the standard error of the mean is about $2/% for Treasury and corporate bond [returns](../Financial%20Markets/Financial%20Asset%20Pricing%20Theory%20Overview/Chapter%203%20-%20%20Assets,%20Portfolios,%20and%20Arbitrage/Assets.md),    which is substantial relative to the estimated mean excess [returns](../Financial%20Markets/Financial%20Asset%20Pricing%20Theory%20Overview/Chapter%203%20-%20%20Assets,%20Portfolios,%20and%20Arbitrage/Assets.md) for these two asset classes. Therefore,    it is quite likely that the extreme long corporate,    short Treasury bond position that the optimal [portfolio](An%20Asset%20Allocation%20Primer.md) formula recommends is just an artifact of estimation error in the mean excess [returns](../Financial%20Markets/Financial%20Asset%20Pricing%20Theory%20Overview/Chapter%203%20-%20%20Assets,%20Portfolios,%20and%20Arbitrage/Assets.md) (which would also explain why it disappeared subsequently in Figure 2.7).

That such extreme weights can occur as output of the [portfolio optimization](../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20III%20THE%20PLAYERS/Chapter%2011%20-%20Individual%20Investors-A%20Survey%20of%20Modern%20Investment%20Theory/The%20Modern%20Portfolio%20Theory%20and%20the%20Capm.md) formula is quite typical for plug-in implementations of the [mean-variance](../Financial%20Markets/Financial%20Asset%20Pricing%20Theory%20Overview/Chapter%2012%20-%20Derivatives/Exercises.md) efficient [portfolio](An%20Asset%20Allocation%20Primer.md) weights. Especially if one feeds in estimates of mean excess [returns](../Financial%20Markets/Financial%20Asset%20Pricing%20Theory%20Overview/Chapter%203%20-%20%20Assets,%20Portfolios,%20and%20Arbitrage/Assets.md) that were obtained from a relatively short time window of only a decade or two.

Now there are good reasons why sometimes we may want to use data windows that are relatively short. We may be worried that markets and the [global economy](../Financial%20Markets%20and%20Institutions/III.%20Liquidity%20of%20Assets/Class%209-%20Bailouts%20and%20Bank%20Failures/Articles/The%20Economist%20Fewer%20Or%20Even%20None.md) have changed so much over time that data from several decades ago may no longer be very relevant for [forecasting](../Advanced%20Financial%20Analysis%20and%20Valuation/Lecture%20Notes%20Advanced%20Financial%20Analysis%20and%20Valuation/Week%202/Week%202%20Fundamentals%20Of%20Forecasting.md) [returns](../Financial%20Markets/Financial%20Asset%20Pricing%20Theory%20Overview/Chapter%203%20-%20%20Assets,%20Portfolios,%20and%20Arbitrage/Assets.md) and covariances in the future. For this reason,    we now look at statistical methods that can help us increase the precision of the inputs to our [portfolio optimization](../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20III%20THE%20PLAYERS/Chapter%2011%20-%20Individual%20Investors-A%20Survey%20of%20Modern%20Investment%20Theory/The%20Modern%20Portfolio%20Theory%20and%20the%20Capm.md) formula.

### 2.8 Shrinkage estimation

The estimation approach we have discussed so far starts from a viewpoint of complete ignorance about $\boldsymbol{\mu}$ and $\boldsymbol{\Sigma}$. We proceeded as if,    before looking at historical data,    we basically have no idea whatsoever what the values of expected [returns](../Financial%20Markets/Financial%20Asset%20Pricing%20Theory%20Overview/Chapter%203%20-%20%20Assets,%20Portfolios,%20and%20Arbitrage/Assets.md),    variances,    and covariances are likely to be. And then we just set $\boldsymbol{\mu}$ and $\boldsymbol{\Sigma}$ to whatever the data tells us the estimates are.

This doesn't seem quite right. Surely we would think that an [expected excess return](../Financial%20Markets/Financial%20Asset%20Pricing%20Theory%20Overview/Chapter%209%20-%20Factor%20Models/Theoretical%20Factors.md) of,    say,    the domestic [stock market](../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20III%20THE%20PLAYERS/Chapter%2012%20-%20Hedge%20Fund%20Strategies/Hedge%20Fund%20Strategies.md) in the vicinity of,    say,    $5/% annually in excess of the risk-free rate is more likely than the expected return exceeding $100/% ? It would not make economic sense that expected [returns](../Financial%20Markets/Financial%20Asset%20Pricing%20Theory%20Overview/Chapter%203%20-%20%20Assets,%20Portfolios,%20and%20Arbitrage/Assets.md) are so high,    as people would have to have crazily high levels of risk aversion for stocks to offer such high rates of [expected return](Lecture%201-%20Probability%20Distributions%20of%20Returns.md). Based on a priori considerations,    before looking at any data,    we would say that such high expected [returns](../Financial%20Markets/Financial%20Asset%20Pricing%20Theory%20Overview/Chapter%203%20-%20%20Assets,%20Portfolios,%20and%20Arbitrage/Assets.md) are totally implausible. Yet,    if we take the sample average return as the only piece of information about the [expected return](Lecture%201-%20Probability%20Distributions%20of%20Returns.md),    we are not making any use of such prior knowledge that we may have. This prior knowledge may be vague,    but as we will see,    it can still be useful to obtain better estimates of return moments.

The Bayesian branch of statistics offers tools that allow use to describe mathematically how prior knowledge expressed as a [Probability Distributions](Lecture%201-%20[[Exercises) of [Returns](../Financial%20Markets/Financial%20Asset%20Pricing%20Theory%20Overview/Chapter%203%20-%20%20Assets,%20Portfolios,%20and%20Arbitrage/Assets.md)|probability distribution]],    the prior distribution,    can be combined with evidence from data to obtain a posterior distribution that reflects the combined information from the prior and the data. For our purposes here,    we don't have to work through all that math required for working with the full prior and posterior [Probability Distributions](Lecture%201-%20[[Exercises) of [Returns](../Financial%20Markets/Financial%20Asset%20Pricing%20Theory%20Overview/Chapter%203%20-%20%20Assets,%20Portfolios,%20and%20Arbitrage/Assets.md)|probability distribution]]s. For practical purposes,    we can get quite far by just using a heuristic approach that captures the essence of the Bayesian method for the purpose of choosing portfolios.

Let's start with the prior beliefs. Suppose we think,    a priori,    that a reasonable number for expected excess [returns](../Financial%20Markets/Financial%20Asset%20Pricing%20Theory%20Overview/Chapter%203%20-%20%20Assets,%20Portfolios,%20and%20Arbitrage/Assets.md) of the risky assets under consideration is $5/%. Then,    our prior mean vector (the mean of the prior [probability distribution](Lecture%201-%20Probability%20Distributions%20of%20Returns.md)) $\boldsymbol{\mu}_{0}$ is a vector in which all elements are equal to 0.05 . This does not mean at all that we are certain about this number,    but we see it as a reasonable starting point. Bayesian statistics (under the assumption that both the prior distribution and the deviations of realized excess returns from $\boldsymbol{\mu}$ are normally distributed) then tells us that our posterior mean is
$$

\begin{equation*}

\hat{\boldsymbol{\mu}}=\phi \overline{\boldsymbol{z}}+(1-\phi) \boldsymbol{\mu}_{0} \tag{2.47}

\end{equation*}

$$

i.e.,    it's a weighted average of sample average excess [returns](../Financial%20Markets/Financial%20Asset%20Pricing%20Theory%20Overview/Chapter%203%20-%20%20Assets,%20Portfolios,%20and%20Arbitrage/Assets.md) of the assets and the prior mean. How much weight $\phi$ we would optimally put on the information coming from the observed data,    $\overline{\boldsymbol{z}}$ vs. the weight $1-\phi$ on the prior mean depends on: (i) how informative the data is (higher $\phi$ if the sample is larger and [returns](../Financial%20Markets/Financial%20Asset%20Pricing%20Theory%20Overview/Chapter%203%20-%20%20Assets,%20Portfolios,%20and%20Arbitrage/Assets.md) are less volatile); (ii) the precision of our prior beliefs that $\boldsymbol{\mu}$ is in the vicinity of $\boldsymbol{\mu}_{0}$ (lower $\phi$ if our prior beliefs are more precise).

But how do we come up with $\boldsymbol{\mu}_{0}$ ? We could put in a number that seems reasonable. But is there perhaps a better approach,    one in which we could still let data influence our view?

We can exploit that we have [multiple risky assets](.md). It is not only implausible that expected excess [returns](../Financial%20Markets/Financial%20Asset%20Pricing%20Theory%20Overview/Chapter%203%20-%20%20Assets,%20Portfolios,%20and%20Arbitrage/Assets.md) on any individual asset class are extremely large,    it is also

implausible that they differ from each other by huge amounts. So if it happens to be the case that the sample averages of [returns](../Financial%20Markets/Financial%20Asset%20Pricing%20Theory%20Overview/Chapter%203%20-%20%20Assets,%20Portfolios,%20and%20Arbitrage/Assets.md) of asset classes differ a lot,    it's likely at least partly due to estimation error. To express this view that expected excess [returns](../Financial%20Markets/Financial%20Asset%20Pricing%20Theory%20Overview/Chapter%203%20-%20%20Assets,%20Portfolios,%20and%20Arbitrage/Assets.md) can't be too different in a prior belief we could say that the $N$ elements of $\boldsymbol{\mu}$ are drawn from a distribution that is centered around the same mean $\mu_{0}$ for all $N$ assets,    with some variance around this mean. In other words,    we can write the prior mean vector as $\boldsymbol{\mu}_{0}=\boldsymbol{\iota} \mu_{0}$.

Our posterior mean now becomes
$$

\begin{equation*}

\hat{\boldsymbol{\mu}}=\phi \overline{\boldsymbol{z}}+(1-\phi) \boldsymbol{\iota} \mu_{0} \tag{2.48}

\end{equation*}

$$

The posterior mean of the [asset returns](../Financial%20Markets/Financial%20Asset%20Pricing%20Theory%20Overview/Chapter%201%20-%20Introduction%20and%20Overview/Some%20Stylized%20Empirical%20Facts%20About%20Asset%20Retur.md) is now pulled towards the common prior mean $\mu_{0}$. We call this shrinking towards $\mu_{0}$ and $\hat{\boldsymbol{\mu}}$ is a shrinkage estimator.

Now to the final step: What would be a good way to find a plausible value for this common mean? Rather than specifying $\mu_{0}$ purely based on a priori reasoning,    as a truly Bayesian approach demands,    we will use an approach that backs it out from observable data. This approach is known as an empirical Bayes approach.

Given that all assets share the same prior mean,    and realizations of [returns](../Financial%20Markets/Financial%20Asset%20Pricing%20Theory%20Overview/Chapter%203%20-%20%20Assets,%20Portfolios,%20and%20Arbitrage/Assets.md) are basically all random deviations from this prior mean (with two components,    first,    the deviation of individual $\mu_{i}$ from $\mu_{0}$ and then deviations of realized excess [returns](../Financial%20Markets/Financial%20Asset%20Pricing%20Theory%20Overview/Chapter%203%20-%20%20Assets,%20Portfolios,%20and%20Arbitrage/Assets.md) from the individual asset specific mean $\mu_{i}$ ),    a natural approach is to simply average,    across assets,    the time series averages of [returns](../Financial%20Markets/Financial%20Asset%20Pricing%20Theory%20Overview/Chapter%203%20-%20%20Assets,%20Portfolios,%20and%20Arbitrage/Assets.md),    i.e.,    use
$$

\begin{equation*}

\overline{\bar{z}}=\frac{1}{N} \iota^{\prime} \overline{\boldsymbol{z}} \tag{2.49}

\end{equation*}

$$

as an estimator of $\mu_{0}$. And then we plug it into the posterior mean equation in place of $\mu_{0}$ :
$$

\begin{equation*}

\hat{\boldsymbol{\mu}}=\phi \overline{\boldsymbol{z}}+(1-\phi) \boldsymbol{\iota} \overline{\bar{z}} \tag{2.50}

\end{equation*}

$$

Now the posterior mean is pulling the estimates away from the individual-asset timeseries averages in $\overline{\boldsymbol{z}}$ toward the the cross-asset average of these time-series averages,    $\overline{\bar{z}}$.

Now let's refine this a little. For many assets,    it might not be all that plausible that the true elements of $\boldsymbol{\mu}$ are drawn from distributions with a common mean $\mu_{0}$ because the assets differ substantially in their levels of risk. For example,    think of a [portfolio](An%20Asset%20Allocation%20Primer.md) of long-term U.S. Treasury bonds and a broad [stock market](../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20III%20THE%20PLAYERS/Chapter%2012%20-%20Hedge%20Fund%20Strategies/Hedge%20Fund%20Strategies.md) [portfolio](An%20Asset%20Allocation%20Primer.md). It does not seem plausible,    a priori,    that the lower-risk Treasury bond [portfolio](An%20Asset%20Allocation%20Primer.md) would earn the same [expected return](Lecture%201-%20Probability%20Distributions%20of%20Returns.md) as a broad stock [portfolio](An%20Asset%20Allocation%20Primer.md). For this reason,    it may be better to work with [risk-adjusted measures](../Financial%20Markets/Financial%20Asset%20Pricing%20Theory%20Overview/Chapter%2011%20-%20Risk-adjusted%20probabilities/General%20Risk-Adjusted%20Probability%20Measures.md) of expected [returns](../Financial%20Markets/Financial%20Asset%20Pricing%20Theory%20Overview/Chapter%203%20-%20%20Assets,%20Portfolios,%20and%20Arbitrage/Assets.md),    such as the Sharpe Ratio

For the kind of application we have in mind in this course,    where we are trying to form a [portfolio](An%20Asset%20Allocation%20Primer.md) that invests in a number of broad asset classes,    a reasonable prior view,    before seeing data on this,    might be that each of these asset classes have a tendency to deliver similar Sharpe ratios,    i.e.,    that the true ratios
$$

\begin{equation*}

s_{i}=\frac{\mu_{i}}{\sigma_{i}} \tag{2.51}

\end{equation*}

$$

can't stray too far from each other. In other words,    they are drawn from a distribution that is centered around the same mean $s_{0}$ for all $N$ assets,    with some random variation around $s_{0}$ for each asset. Following this view,    we then shrink estimated asset class Sharpe ratios $\bar{z}_{i} / \hat{\sigma}_{i}$ toward their common mean rather than shrinking the mean [returns](../Financial%20Markets/Financial%20Asset%20Pricing%20Theory%20Overview/Chapter%203%20-%20%20Assets,%20Portfolios,%20and%20Arbitrage/Assets.md). If we have a value for this $s_{0}$,    we can then get posterior Sharpe Ratios for the individual assets as
$$

\begin{equation*}

\hat{s}*{i}=\phi \frac{\bar{z}*{i}}{\hat{\sigma}*{i}}+(1-\phi) \boldsymbol{\iota} s*{0} \tag{2.52}

\end{equation*}

$$

And as we discussed above for shrinking means,    we can use an empirical Bayes approach by replacing $s_{0}$ with the cross-sectional mean of the assets' estimated Sharpe ratios,    $\overline{\bar{s}}$ :
$$

\begin{equation*}

\hat{s}*{i}=\phi \frac{\bar{z}*{i}}{\hat{\sigma}_{i}}+(1-\phi) \iota \overline{\bar{s}} \tag{2.53}

\end{equation*}

$$

Based on this posterior Sharpe ratio,    we can then calculate the implied posterior mean as
$$

\begin{equation*}

\hat{\mu}*{i}=\hat{s}*{i} \hat{\sigma}_{i} \tag{2.54}

\end{equation*}

$$

which we can plug into the optimal [Portfolio](Lecture%205-%20Dynamic%20[[An%20Asset%20Allocation%20Primer) Choice|[portfolio](An%20Asset%20Allocation%20Primer.md) choice]] formula.

So far so good,    but how can all this be useful if we don't know $\phi$ ? We could be pick some value for $\phi$ and hope that it is somewhat plausible. We would want shrinkage to be weak enough to allow Sharpe ratios to vary across asset classes in [ranges](../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%206%20Options%20on%20Non-Price%20Variables/Exotic%20Interest%20Rate%20Options.md) that seem plausible,    but strong enough to make it very unlikely that we get $\hat{s}_{i}$ that take extreme values like,    say,    $\hat{s}_{i}>5$. We will get to this soon.

But before we get there,    let's first look at covariance matrix estimation. We can employ similar shrinkage ideas in covariance matrix estimation. If we are trying to find an optimal [portfolio](An%20Asset%20Allocation%20Primer.md) with many assets,    it is crucial to bring in prior information to discipline the covariance matrix. With $N$ assets,    the covariance matrix has $N \times N$ elements. The covariance matrix is symmetric,    where each covariance shows up twice above and below the diagonal,    but this still leaves $N(N+1) / 2$ parameters to estimate. For example,    with just 10 assets,    we already have $10 \times(10+1) / 2=55$ parameters to estimate. The more parameters there are in the covariance matrix,    the more likely it is that estimation error generates problems.

The fact that we have to invert the covariance matrix in the optimal [portfolio](An%20Asset%20Allocation%20Primer.md) formula can hugely magnify estimation errors. We can get an idea of where the problem comes from by looking first at the case of only one asset. Here $\widehat{\boldsymbol{\Sigma}}$ is just the estimated variance of a single asset return $\sigma^{2}$. If estimation error pushes $\hat{\sigma}^{2}$ close to zero,    the inverse,    which is here just $1 / \hat{\sigma}^{2}$,    explodes toward infinity. Non-invertibility of a covariance matrix is sort of like this. The difference to the single asset case is that with multiple assets,    the existence of any [portfolio](An%20Asset%20Allocation%20Primer.md) of assets (which is a linear combination of individual [asset returns](../Financial%20Markets/Financial%20Asset%20Pricing%20Theory%20Overview/Chapter%201%20-%20Introduction%20and%20Overview/Some%20Stylized%20Empirical%20Facts%20About%20Asset%20Retur.md)) with close to zero variance makes the covariance matrix blow up. The more assets there are,    the easier it is to find such portfolios where,    by chance,    a combination of estimation errors results in a [portfolio](An%20Asset%20Allocation%20Primer.md) that seemingly has close to zero variance in the sample that we are using to estimate the covariance matrix.

If the covariance matrix is not invertible,    statistical software packages will tell us. But sometimes it may just be close to non-invertible,    even though technically it is still invertible. It's useful to know how this sort of problem then manifests in the optimal [portfolio](An%20Asset%20Allocation%20Primer.md) weight output of the optimal [portfolio](An%20Asset%20Allocation%20Primer.md) formula: A typical symptom of this problem is that the optimal [portfolio](An%20Asset%20Allocation%20Primer.md) weights imply some huge [long and short positions](../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%2013/Market%20Size%20and%20Participants.md),    i.e.,    some weights are huge and positive,    others are huge and negative.

Intuitively,    when estimation errors in covariances make it look like as if some combination of assets delivers close to zero risk,    but earns a substantial spread in excess [returns](../Financial%20Markets/Financial%20Asset%20Pricing%20Theory%20Overview/Chapter%203%20-%20%20Assets,%20Portfolios,%20and%20Arbitrage/Assets.md),    this looks like a great [investment](An%20Asset%20Allocation%20Primer.md) opportunity to the [portfolio optimization](../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20III%20THE%20PLAYERS/Chapter%2011%20-%20Individual%20Investors-A%20Survey%20of%20Modern%20Investment%20Theory/The%20Modern%20Portfolio%20Theory%20and%20the%20Capm.md) formula. For example,    suppose two assets happen to have different [expected return](Lecture%201-%20Probability%20Distributions%20of%20Returns.md) estimates and similar variance estimates,    and their estimated correlation is far too high (relative to their true correlation) because [returns](../Financial%20Markets/Financial%20Asset%20Pricing%20Theory%20Overview/Chapter%203%20-%20%20Assets,%20Portfolios,%20and%20Arbitrage/Assets.md) of these two assets in our sample just happened to be highly positively correlated by chance even though they are not truly highly correlated. This looks like an opportunity to go long in the high [expected return](Lecture%201-%20Probability%20Distributions%20of%20Returns.md) asset and short in the low [expected return](Lecture%201-%20Probability%20Distributions%20of%20Returns.md) asset. This position earns the spread in expected [returns](../Financial%20Markets/Financial%20Asset%20Pricing%20Theory%20Overview/Chapter%203%20-%20%20Assets,%20Portfolios,%20and%20Arbitrage/Assets.md) with very little risk. The optimal [portfolio](An%20Asset%20Allocation%20Primer.md) formula will tell us to take a huge long-short bet. But of course taking this position would very likely lead to a big disappointment out-of-sample because the assets aren't truly highly correlated. Estimation error just made it look like they were.

A large number of assets magnifies this problem because the more assets there are,    the more likely it is that,    just by chance,    some linear combination of assets seemingly has zero risk.

If high-frequency data is available for covariance matrix estimation,    this can help avoid these problems because it reduces the magnitude of estimation errors in covariances,    along the lines we discussed earlier. But shrinkage can be useful,    too.

Heuristically,    we can again give this a Bayesian interpretation where we combine

information in the sample covariance matrix obtained from [returns](../Financial%20Markets/Financial%20Asset%20Pricing%20Theory%20Overview/Chapter%203%20-%20%20Assets,%20Portfolios,%20and%20Arbitrage/Assets.md) data with prior knowledge about the likely values of variances and covariances.

We can decompose the covariance matrix into standard deviations and correlations:
$$

\boldsymbol{\Sigma}=\left(\begin{array}{cccc}

\sigma_{1} & 0 & \ldots & 0  \tag{2.55}\\

0 & \sigma_{2} & \ldots & 0 \\

& \ldots & & \\

0 & 0 & \ldots & \sigma_{N}

\end{array}\right)\left(\begin{array}{cccc}

1 & \rho_{12} & \ldots & \rho_{1 N} \\

\rho_{21} & 1 & \ldots & \rho_{2 N} \\

& \ldots & & \\

\rho_{N 1} & \rho_{N 2} & \ldots & 1

\end{array}\right)\left(\begin{array}{cccc}

\sigma_{1} & 0 & \ldots & 0 \\

0 & \sigma_{2} & \ldots & 0 \\

& \ldots & & \\

0 & 0 & \ldots & \sigma_{N}

\end{array}\right)

$$

where $\rho_{i j}$ denotes the correlation between [returns](../Financial%20Markets/Financial%20Asset%20Pricing%20Theory%20Overview/Chapter%203%20-%20%20Assets,%20Portfolios,%20and%20Arbitrage/Assets.md) of asset $i$ and $j$.

Let's denote the diagonal matrix with standard deviations on the diagonal with $\boldsymbol{S}$ and the correlation matrix with $\boldsymbol{C}$. Then we can write $\boldsymbol{\Sigma}$ as
$$

\begin{equation*}

\Sigma=\boldsymbol{S C S} \tag{2.56}

\end{equation*}

$$

Imprecisely estimated correlations are often the source of trouble in [portfolio optimization](../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20III%20THE%20PLAYERS/Chapter%2011%20-%20Individual%20Investors-A%20Survey%20of%20Modern%20Investment%20Theory/The%20Modern%20Portfolio%20Theory%20and%20the%20Capm.md). To see why,    recall the two-asset example we just discussed earlier where two assets have different estimated expected [returns](../Financial%20Markets/Financial%20Asset%20Pricing%20Theory%20Overview/Chapter%203%20-%20%20Assets,%20Portfolios,%20and%20Arbitrage/Assets.md) and the estimate of their correlation is close to one,    even though their true correlation is far from one. If the estimated high correlation is indeed just a statistical fluke,    then the [portfolio](An%20Asset%20Allocation%20Primer.md) takes an extreme position in a strategy that in reality does not deliver a great ratio of reward to risk. It just looked like it might based on erroneous estimates. This can mess up the performance of the whole [portfolio](An%20Asset%20Allocation%20Primer.md). And if we have many assets,    we need to estimate many correlations (e.g.,    if we have 10 assets,    we must estimate $(10 \times 10-10) / 2=45$ correlations). Among so many estimates,    it's likely that a few will be way off from the true correlation due to estimation error. Hence,    it's generally a well-known problem that with a large number of assets,    just plugging the sample covariance matrix (and hence,    implicitly,    all these sample estimates of correlations) into a [portfolio](An%20Asset%20Allocation%20Primer.md) optimizer yields poor results.

For this reason,    we may want to express that we know that correlations are probably all positive (risky assets generally tend to move together),    but teasing out from the data which ones are higher and which ones are lower may be difficult. We express this prior belief by shrinking our correlation estimates towards an equicorrelation matrix
$$

\boldsymbol{C}*{0}=\left(\begin{array}{cccc}*

*1 & \rho*{0} & \ldots & \rho_{0}  \tag{2.57}\\

\rho_{0} & 1 & \ldots & \rho_{0} \\

\rho_{0} & \rho_{0} & \ldots & 1

\end{array}\right)

$$

where all the correlations take the same value $\rho_{0}$. Using $\overline{\boldsymbol{C}}$ to denote the matrix of correlations estimated from the data,    our posterior estimate of the correlation matrix becomes
$$

\begin{equation*}

\widehat{\boldsymbol{C}}=\phi \overline{\boldsymbol{C}}+(1-\phi) \boldsymbol{C}_{0} \tag{2.58}

\end{equation*}

$$

Then our estimate of the covariance matrix becomes
$$

\begin{equation*}

\widehat{\boldsymbol{\Sigma}}=\widehat{\boldsymbol{S}} \widehat{\boldsymbol{C}} \widehat{\boldsymbol{S}} \tag{2.59}

\end{equation*}

$$

where $\widehat{\boldsymbol{S}}$ is the estimated version of $\boldsymbol{S}$,    i.e.,    with estimated standard deviations on its diagonal.

How can we come up with a number for $\rho_{0}$ ? In the same empirical Bayes spirit as above when we looked at expected [returns](../Financial%20Markets/Financial%20Asset%20Pricing%20Theory%20Overview/Chapter%203%20-%20%20Assets,%20Portfolios,%20and%20Arbitrage/Assets.md) and Sharpe Ratios,    we can plug in an estimate of the average pairwise correlation of all assets. This means that we use the observed [returns](../Financial%20Markets/Financial%20Asset%20Pricing%20Theory%20Overview/Chapter%203%20-%20%20Assets,%20Portfolios,%20and%20Arbitrage/Assets.md) data,    we form all possible pairs of asset return series $i$ and $i$ where $i \neq j$,    and we estimate their correlation $\hat{\rho}_{i j}$. Then we construct their average,  
$$

\begin{equation*}

\bar{\rho}=\frac{1}{N(N-1)} \sum_{i=1}^{N} \sum_{j \neq i} \hat{\rho}_{i j} \tag{2.60}

\end{equation*}

$$

We then replace $\rho_{0}$ in the prior correlation matrix $\boldsymbol{C}_{0}$ with this estimate $\bar{\rho}$.

Now we have to tackle the remaining problem of how to estimate $\phi$. We can use an approach known as cross-validation. Cross-validation is a powerful idea that appears in lots of places in applied statistics and data science,    including many machine learning applications. The idea is that we can use historical data on [returns](../Financial%20Markets/Financial%20Asset%20Pricing%20Theory%20Overview/Chapter%203%20-%20%20Assets,%20Portfolios,%20and%20Arbitrage/Assets.md) to evaluate which value of $\phi$ would have led us to construct the best portfolios in the past,    where with "best" we mean that this value leads to the best out-of-sample [portfolio](An%20Asset%20Allocation%20Primer.md) performance. In this approach,    we basically imagine that we had constructed Sharpe Ratio estimates as in (2.53),    and portfolios based on these estimates,    in the past and we look for the value of $\phi$ that would have given us the best out-of-sample performance in the past.

To implement this cross-validation approach,    I use [returns](../Financial%20Markets/Financial%20Asset%20Pricing%20Theory%20Overview/Chapter%203%20-%20%20Assets,%20Portfolios,%20and%20Arbitrage/Assets.md) data for our nine asset classes from the beginning of 1980 to the end of 2022. I then pick an estimation window size,    e.g.,    240 months,    or 20 years. Then I implement the following steps:

Estimate $\hat{\boldsymbol{\mu}}$ as in (2.54) and $\widehat{\boldsymbol{\Sigma}}$ as in (2.59) using data from beginning of 1980 to end of 1999 and for different values from $\phi=0$ (total shrinkage) to $\phi=1$ (no shrinkage).

For each of these $\hat{\boldsymbol{\mu}}$ and $\widehat{\boldsymbol{\Sigma}}$ combinations for a value of $\phi$,    I calculate the optimal risky [asset portfolio](../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%204/The%20Barbell%20Versus%20the%20Bullet.md) weights as in (2.18).

I then apply these weights to [returns](../Financial%20Markets/Financial%20Asset%20Pricing%20Theory%20Overview/Chapter%203%20-%20%20Assets,%20Portfolios,%20and%20Arbitrage/Assets.md) on the nine asset classes in January 2000 to calculate the out-of-sample [portfolio](An%20Asset%20Allocation%20Primer.md) return in January 2000,    i.e.,    in the month following the end of the estimation window. Again I do this for every value of $\phi$.

Then I move the estimation window in step 1 forward by one month to beginning of February 1980 to end of January 2000. Then I repeat steps 1 to 3 and I get an out-of-sample [portfolio](An%20Asset%20Allocation%20Primer.md) return in February 2020 for each value of $\phi$. I keep repeating until I have reached the [portfolio](An%20Asset%20Allocation%20Primer.md) return in December 2022.

Now I have several time-series of [portfolio](An%20Asset%20Allocation%20Primer.md) excess [returns](../Financial%20Markets/Financial%20Asset%20Pricing%20Theory%20Overview/Chapter%203%20-%20%20Assets,%20Portfolios,%20and%20Arbitrage/Assets.md),    one for each $\phi$. I calculate the Sharpe ratio from these [portfolio](An%20Asset%20Allocation%20Primer.md) excess [returns](../Financial%20Markets/Financial%20Asset%20Pricing%20Theory%20Overview/Chapter%203%20-%20%20Assets,%20Portfolios,%20and%20Arbitrage/Assets.md).

 ![500](Attachments/500-999.jpg)

Figure 2.8: Out-of-sample Sharpe Ratios for different values of the shrinkage parameter $\phi$ and different lengths of the backward-looking estimation window

I then redo the whole procedure with a different estimation window sizes of 10 years and 5 years in addition to the 20-year window. Figure 2.8 shows the results. For each of the estimation window lengths,    it shows how the Sharpe ratio of the [portfolio](An%20Asset%20Allocation%20Primer.md) changes with $\phi$. There are a few things to note.

First,    when we use 20 years of data,    shrinkage doesn't have much of an effect. The Sharpe ratio is more or less insensitive to the value of $\phi$. Shrinkage is apparently not really needed to get better estimates,    but imposing lots of shrinkage also doesn't hurt. (Just to be clear,    this is obviously not a general conclusion that is always valid everywhere. It could well be the case that with a different set of asset classes,    or with estimates from different time periods,    there is substantial sensitivity of the out-of-sample Sharpe ratio to $\phi$ with 20-year estimation windows).

Second,    if we wish to use shorter estimation windows (perhaps because we think that expected [returns](../Financial%20Markets/Financial%20Asset%20Pricing%20Theory%20Overview/Chapter%203%20-%20%20Assets,%20Portfolios,%20and%20Arbitrage/Assets.md) and covariances may have changed too much over long periods of time),    shrinkage is important. With 5 -year estimation windows and no shrinkage at all (i.e.,    $\phi=1$ at the right-hand side of the plot) the Sharpe ratio is around zero. In other words,    the [portfolio optimization](../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20III%20THE%20PLAYERS/Chapter%2011%20-%20Individual%20Investors-A%20Survey%20of%20Modern%20Investment%20Theory/The%20Modern%20Portfolio%20Theory%20and%20the%20Capm.md) has become useless. In contrast,    with $\phi=0$,    and hence extreme shrinkage,    the 5-year estimation window approach produces Sharpe ratios that are close to the highest possible Sharpe ratios for the 10-year and 20-year estimation windows.

As it turns out,    this extreme shrinkage approach with $\phi=0$ actually leads to an [Asset Allocation](Lecture%202-%20[[Lecture%202-%20Asset%20Allocation%20with%20Multiple%20Risky%20Assets) with [Multiple Risky Assets](.md)|[asset allocation](.md)]] strategy that has become quite popular in the past decade or two.

### 2.9 Extreme forms of shrinkage: Risk parity and $1 / \mathrm{N}$

Let's examine in more detail the extreme shrinkage [portfolio](An%20Asset%20Allocation%20Primer.md) that results when we set $\phi=0$ in estimating $\hat{\boldsymbol{\mu}}$ as in (2.54),    i.e.,    with shrinkage towards a equal Sharpe ratios,    and $\widehat{\boldsymbol{\Sigma}}$ as in (2.59).

In this case,    the covariance matrix estimate uses the empirically estimated standard deviations,    while the correlations are all shrunk completely to the equicorrelation matrix $C_{0}$ :
$$

\begin{equation*}

\widehat{\Sigma}=\widehat{\boldsymbol{S}} C_{0} \widehat{\boldsymbol{S}} \tag{2.61}

\end{equation*}

$$

Before we plug this into the optimal [portfolio](An%20Asset%20Allocation%20Primer.md) formula,    it's useful to note that $\widehat{\boldsymbol{\Sigma}}^{-1}=$ $\widehat{\boldsymbol{S}}^{-1} \boldsymbol{C}_{0}^{-1} \widehat{\boldsymbol{S}}^{-1}$.

With $\phi=0$,    the Sharpe ratios of all asset classes are completely shrunk to their common mean $\overline{\bar{s}}$ and so the [expected excess return](../Financial%20Markets/Financial%20Asset%20Pricing%20Theory%20Overview/Chapter%209%20-%20Factor%20Models/Theoretical%20Factors.md) estimates implied by these identical Sharpe ratios are
$$

\begin{equation*}

\hat{\boldsymbol{\mu}}=\widehat{\boldsymbol{S}} \boldsymbol{\iota} \bar{s} \tag{2.62}

\end{equation*}

$$

The optimal [portfolio](An%20Asset%20Allocation%20Primer.md) weight formula (2.18) tells us that [portfolio](An%20Asset%20Allocation%20Primer.md) weights are proportional to $\widehat{\boldsymbol{\Sigma}}^{-1} \hat{\boldsymbol{\mu}}$. In this case here,  
$$

\begin{align*}

\widehat{\boldsymbol{\Sigma}}^{-1} \hat{\boldsymbol{\mu}} & =\widehat{\boldsymbol{S}}^{-1} \boldsymbol{C}*{0}^{-1} \widehat{\boldsymbol{S}}^{-1} \widehat{\boldsymbol{S}} \boldsymbol{\iota} \bar{s} \\*

*& =\widehat{\boldsymbol{S}}^{-1} \boldsymbol{C}*{0}^{-1} \iota \bar{s} \\

& \propto \widehat{\boldsymbol{S}}^{-1} \boldsymbol{\iota} \tag{2.63}

\end{align*}

$$

(The last equality holds because the inverse of the equicorrelation matrix has the property,    just like the equicorrelation matrix does,    that the sum of the elements in each row or column is the same. This means that when we multiply $\boldsymbol{C}_{0}^{-1}$ with $\boldsymbol{\iota}$ we get,    as a result,    a vector with equal elements that is proportional to $\boldsymbol{\iota}$.) So,    optimal [portfolio](An%20Asset%20Allocation%20Primer.md) weights will be proportional to $\widehat{\boldsymbol{S}}^{-1} \boldsymbol{\iota}$. And since $\boldsymbol{S}^{-1}$ is diagonal,    we get
$$

\hat{\boldsymbol{\omega}}^{*} \propto\left(\begin{array}{c}

\frac{1}{\hat{\sigma}*{1}}  \tag{2.64}\\*

*\frac{1}{\hat{\sigma}*{2}} \\

\ldots \\

\frac{1}{\hat{\sigma}_{N}}

\end{array}\right)

$$

Let's examine the weights in (2.64). They only depend on individual asset class risk as measured by standard deviations. Estimates of mean [returns](../Financial%20Markets/Financial%20Asset%20Pricing%20Theory%20Overview/Chapter%203%20-%20%20Assets,%20Portfolios,%20and%20Arbitrage/Assets.md) or correlations have completely disappeared from the optimal [portfolio](An%20Asset%20Allocation%20Primer.md) weight formula. This is a consequence of the extreme shrinkage we have imposed. These are the weights underlying the portfolios at the very left side of Figure 2.8 for $\phi=0$. Basically,    this strategy expresses extreme distrust in empirical estimates of correlations and mean [returns](../Financial%20Markets/Financial%20Asset%20Pricing%20Theory%20Overview/Chapter%203%20-%20%20Assets,%20Portfolios,%20and%20Arbitrage/Assets.md),    but considers standard deviation estimates as reliable.

Among [investment](An%20Asset%20Allocation%20Primer.md) practitioners,    the approach to [portfolio](An%20Asset%20Allocation%20Primer.md) allocation embodied in the weights in (2.64) is known as [risk parity](Lecture%206-Leverage,%20Tail%20Risk,%20Volatility%20Products.md). It was pioneered by the hedge fund firm Bridgewater Associates in their All Weather Fund in the mid-1990s. The high Sharpe ratios for $\phi=0$ in Figure 2.8 tells us that this approach has done well in the past few decades,    which may explain why it became popular.

The motivation [investment](An%20Asset%20Allocation%20Primer.md) practitioners give for this approach is typically a bit different from the way we arrived at it here. [Risk parity](Lecture%206-Leverage,%20Tail%20Risk,%20Volatility%20Products.md) is often presented as the idea that each asset class should be held with a weight that has each asset class make the same risk contribution to the [portfolio](An%20Asset%20Allocation%20Primer.md),    or,    in other words,    it gets the same "risk budget." Recall our decomposition of the [portfolio](An%20Asset%20Allocation%20Primer.md) variance in (2.22):
$$

\operatorname{var}\left(R_{p}\right)=\omega_{1} \underbrace{\operatorname{cov}\left(R_{1},  R_{p}\right)}*{\begin{array}{c}*

*\text { Risk }  \tag{2.65}\\*

*\text { contribution } \\*

*\text { of asset } 1*

*\end{array}}+\omega*{2} \operatorname{cov}\left(R_{2},  R_{p}\right)+\ldots+\omega_{N} \operatorname{cov}\left(R_{N},  R_{p}\right)

$$

The risk contributions of each asset class per unit of weight are represented by the covariances $\operatorname{cov}\left(R_{i},         R_{p}\right)$,    and their total risk contribution to the [portfolio](An%20Asset%20Allocation%20Primer.md) by this covariance times the [portfolio](An%20Asset%20Allocation%20Primer.md) weight. With risk-parity weights proportional to $1 / \sigma_{i}$ and the assumption that the correlation matrix of the asset classes is an equicorrelation matrix,    one can show that $\omega_{i} \operatorname{cov}\left(R_{i},         R_{p}\right)$ is then the same for each asset class-i.e.,    each asset

class accounts for the same share of total [portfolio](An%20Asset%20Allocation%20Primer.md) risk. ${ }^{2}$ This is what people mean when they say that a [risk parity](Lecture%206-Leverage,%20Tail%20Risk,%20Volatility%20Products.md) strategy then gives each asset class an equal risk budget for its contribution to [portfolio](An%20Asset%20Allocation%20Primer.md) risk (and keep in mind that this statement is true only if the equicorrelation assumption holds).

Now,    conceptually,    it's not clear why equal risk budgets for each asset class would be desirable. In contrast,    our shrinkage approach gives a clear motivation: if we strongly distrust mean return and correlation estimates due to estimation error,    then meanvariance optimization implies a [risk parity](Lecture%206-Leverage,%20Tail%20Risk,%20Volatility%20Products.md) strategy.

 ![500](https://cdn.mathpix.com/cropped/2024_10_19_48a1c4654e845915c45cg-066.jpg?height=926&width=1201&top_left_y=762&top_left_x=424)

Figure 2.9: Weights of [risk parity portfolio](Lecture%206-Leverage,%20Tail%20Risk,%20Volatility%20Products.md) (10 years of data to estimate standard deviations)

Figure 2.9 shows how [risk parity portfolio](Lecture%206-Leverage,%20Tail%20Risk,%20Volatility%20Products.md) weights looked like if we implemented this approach in the past few decades,    using 10 years of backward looking data to estimate the

[^7]asset class return standard deviations. Notice the different scale of the y-axis compared with Figure 2.7.

Also,    note that I am plotting the risky [portfolio](An%20Asset%20Allocation%20Primer.md) weights in (2.18) that are scaled to sum up to one. We will leave aside for now the question of how to allocate between short-term risk-free assets (proxied for by T-bills) and the risky [asset portfolio](../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%204/The%20Barbell%20Versus%20the%20Bullet.md).

In several ways,    these [portfolio](An%20Asset%20Allocation%20Primer.md) weights have desirable attributes. There are no huge outliers asking for huge amounts of [leverage](Lecture%206-Leverage,%20Tail%20Risk,%20Volatility%20Products.md) ([portfolio](An%20Asset%20Allocation%20Primer.md) weights in excess of 1.0) or short positions ([portfolio](An%20Asset%20Allocation%20Primer.md) weights $<0$ ) that [portfolio](An%20Asset%20Allocation%20Primer.md) managers are often reluctant to take. As we saw in Figure 2.7,    this can be very different for optimal weights without shrinkage when a relatively short estimation window of 10 years is used to estimate the inputs for the optimal [portfolio](An%20Asset%20Allocation%20Primer.md) weight formula (that make the calculation of the optimal weights far more cumbersome). One way to fix this problem (for a manager who is reluctant to take on [leverage](Lecture%206-Leverage,%20Tail%20Risk,%20Volatility%20Products.md) and short positions) is to impose additional constraints on the meanvariance optimization problem. But the [risk parity](Lecture%206-Leverage,%20Tail%20Risk,%20Volatility%20Products.md) strategy delivers moderate weights without having to impose such constraints.

Figure 2.9 also highlights one property that has generated criticism of the [risk parity](Lecture%206-Leverage,%20Tail%20Risk,%20Volatility%20Products.md) approach: its heavy loading on bonds. As the figure shows,    the three bond asset classes,    U.S. Treasury bonds,    international bonds,    and [Corporate Bonds](../Financial%20Markets%20and%20Institutions/II.%20The%20Roles%20of%20Banks%20and%20Derivative%20Markets%20in%20Resolving%20Problems%20Inherent%20in%20Debt%20Contracts/Class%202-%20Debt%20Contracts%20due%20to%20Lack%20of%20Information/Class%20Notes%202%20–%20Corporate%20Bond%20Contracts.md) account for a large share of the total [portfolio](An%20Asset%20Allocation%20Primer.md). The concern is that the strategy has benefitted from the secular decline in [interest rates](../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%202/Interest%20Rate%20Quotations.md) (which lead to high [returns](../Financial%20Markets/Financial%20Asset%20Pricing%20Theory%20Overview/Chapter%203%20-%20%20Assets,%20Portfolios,%20and%20Arbitrage/Assets.md) for holders of long-term bonds) that took place during the past decades. The performance of a strategy with a high bond exposure in the future may look much less appealing.

Another problem that is useful to keep in mind concerns the initial menu of asset classes. The [mean-variance](../Financial%20Markets/Financial%20Asset%20Pricing%20Theory%20Overview/Chapter%2012%20-%20Derivatives/Exercises.md) optimization approach that takes into account correlations is not as sensitive to the selection of the asset class menu than the risky parity approach. For example,    if we add another asset class to the menu that is very similar in terms of mean return and highly correlated with an asset class that we already have in the menu,    the [mean-variance](../Financial%20Markets/Financial%20Asset%20Pricing%20Theory%20Overview/Chapter%2012%20-%20Derivatives/Exercises.md) optimal [portfolio](An%20Asset%20Allocation%20Primer.md) will tend to reduce the share of the one we already have in the menu and give some of this share to the new asset class,    leaving other asset classes largely unaffected.

In contrast,    the [risk parity](Lecture%206-Leverage,%20Tail%20Risk,%20Volatility%20Products.md) approach reduces the weight on all other asset classes equally when we bring in a new asset class,    even if the new asset class is very similar to one we already have in the menu,    and not to the others.

The [bottom line](../Advanced%20Financial%20Analysis%20and%20Valuation/Financial%20Ratios/Operating%20Income%20vs.%20Net%20Income%20What's%20the%20Difference.md) from this is that the equicorrelation prior should be somewhat plausible for the selected menu of asset classes for the risky parity approach to make sense. Having two asset classes in there that are clearly much more highly correlated than others could lead to excessive weight for these two asset classes.

Now consider an even more extreme form of distrust in the data. Suppose we don't believe that historical data on standard deviations are useful for [forecasting](../Advanced%20Financial%20Analysis%20and%20Valuation/Lecture%20Notes%20Advanced%20Financial%20Analysis%20and%20Valuation/Week%202/Week%202%20Fundamentals%20Of%20Forecasting.md) future volatility. We therefore feel that we can't distinguish between asset risk levels and we impose extreme shrinkage not only on mean [returns](../Financial%20Markets/Financial%20Asset%20Pricing%20Theory%20Overview/Chapter%203%20-%20%20Assets,%20Portfolios,%20and%20Arbitrage/Assets.md) and correlations,    but also standard deviations: we assume they are the same $\sigma_{1}=\sigma_{2}=\ldots=\sigma_{N}$. Then the [portfolio](An%20Asset%20Allocation%20Primer.md) weights for all asset classes are exactly equal and the risky [asset portfolio](../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%204/The%20Barbell%20Versus%20the%20Bullet.md) weights are
$$

\hat{\boldsymbol{\omega}}^{*}=\left(\begin{array}{c}

\frac{1}{N}  \tag{2.66}\\

\frac{1}{N} \\

\ldots \\

\frac{1}{N}

\end{array}\right)

$$

where $N$ is the number of asset classes. This [portfolio](An%20Asset%20Allocation%20Primer.md) formation strategy is called,    sensibly,    a $1 / N$ strategy. It uses no inputs about expected [returns](../Financial%20Markets/Financial%20Asset%20Pricing%20Theory%20Overview/Chapter%203%20-%20%20Assets,%20Portfolios,%20and%20Arbitrage/Assets.md) and risks whatsoever.

 ![500](https://cdn.mathpix.com/cropped/2024_10_19_48a1c4654e845915c45cg-068.jpg?height=955&width=1201&top_left_y=1035&top_left_x=424)

Figure 2.10: Out-of-sample Sharpe Ratios of different [portfolio strategies](../Fixed%20Income%20Asset%20Pricing/Lecture%20Notes%20Bonds,%20%20Preferred%20Stock,%20%20and%20Structured%20Products.md) (10 years of data to estimate return moments)

This may seem like an extremely unsophisticated [Asset Allocation](Lecture%202-%20[[Lecture%202-%20Asset%20Allocation%20with%20Multiple%20Risky%20Assets) with [Multiple Risky Assets](.md)|[asset allocation](.md)]] strategy. And in some sense it is. But look at Figure 2.10! The Figure shows the out-of-sample Sharpe ratios of four strategies: (i) no shrinkage at all - this is the [portfolio](An%20Asset%20Allocation%20Primer.md) of the 10-year line

for $\phi=1$ in Figure 2.8; (ii) optimal shrinkage of $\phi=0.05$ based on the maximum of the line for 10-year estimation windows in Figure 2.8; (iii) [risk parity](Lecture%206-Leverage,%20Tail%20Risk,%20Volatility%20Products.md); (iv) $1 / N$.

Surprisingly,    $1 / N$ does quite well! Not as good as optimal shrinkage and [risk parity](Lecture%206-Leverage,%20Tail%20Risk,%20Volatility%20Products.md),    but still much better than in the no-shrinkage case. There is actually a fairly large body of research at this point showing that the $1 / N$ strategy of forming a [diversified portfolio](../Financial%20Engineering/Derivatives/Part%20I%20-%20Forwards%20and%20Futures/Chapter%205%20-%20Index%20Futures.md) does quite well in a number of settings.

As for the [risk parity](Lecture%206-Leverage,%20Tail%20Risk,%20Volatility%20Products.md) approach,    the selection of the menu of assets is very important. By adding lots of very similar,    highly correlated asset classes,    a $1 / N$ [portfolio](An%20Asset%20Allocation%20Primer.md) would become poorly diversified and its Sharpe ratio would suffer. Part of the success of $1 / N$ in our analysis here comes from the fact that we started with a good selection of asset classes that span a lot of different types of risks.

But one conclusion that we can tentatively draw from the success of $1 / N$ in this exercise is that our inputs to the optimal [portfolio](An%20Asset%20Allocation%20Primer.md) weight formula are perhaps not good enough yet. For example,    just plugging in historical estimates of mean excess [returns](../Financial%20Markets/Financial%20Asset%20Pricing%20Theory%20Overview/Chapter%203%20-%20%20Assets,%20Portfolios,%20and%20Arbitrage/Assets.md) from the past 10 years may be a poor way of [forecasting](../Advanced%20Financial%20Analysis%20and%20Valuation/Lecture%20Notes%20Advanced%20Financial%20Analysis%20and%20Valuation/Week%202/Week%202%20Fundamentals%20Of%20Forecasting.md) future excess [returns](../Financial%20Markets/Financial%20Asset%20Pricing%20Theory%20Overview/Chapter%203%20-%20%20Assets,%20Portfolios,%20and%20Arbitrage/Assets.md).

Much of the rest of the course will be devoted to getting a better understanding of how to forecast [risk and return](Lecture%207-Risk%20and%20Return%20of%20Bonds.md).
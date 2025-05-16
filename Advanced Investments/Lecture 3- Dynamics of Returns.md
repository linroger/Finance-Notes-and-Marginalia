---
title: Lecture 3 - Dynamics of Returns
cssclasses:
  - academia
  - finance
tags:
  - conditional_returns
  - lecture_notes
  - market_timing
  - stock_returns
  - volatility
  - return_predictability
  - time_series_analysis
  - market_efficiency
  - dynamic_portfolio_management
  - financial_econometrics
aliases:
  - Dynamics of Returns
  - Lecture 3
  - Lecture 3 Notes
  - Return Dynamics
  - Time-Varying Returns
key_concepts:
  - Conditional distribution of returns
  - Optimal allocation formula
  - Statistical model of returns
  - Time-varying expected returns
  - Unconditional distribution of returns
  - Market timing strategies
  - Return predictability evidence
  - Volatility forecasting methods
  - Dynamic allocation techniques
  - Autoregressive processes
  - Business cycle predictability
  - Conditional variances
---


# Lecture 3: Dynamics of Returns

We now focus on return dynamics over time. Recall from lecture 1 the formula for the optimal risky asset share in the single risky asset case:
$$

\begin{equation*}

\omega=\frac{\mathbb{E}[R]-R_{f}}{\gamma \operatorname{var}(R)} \tag{3.1}

\end{equation*}

$$

<<<<<<< HEAD
The inputs of this optimal allocation formula could potentially vary over time. Perhaps there are times when expected excess [returns](../Financial%20Markets/Financial%20Asset%20Pricing%20Theory%20Overview/Chapter%203%20-%20%20Assets,%20Portfolios,%20and%20Arbitrage/Assets.md) are high and times when they are low? Perhaps there are times when volatility is high and other times when volatility is low? If such time-variation in expected [returns](../Financial%20Markets/Financial%20Asset%20Pricing%20Theory%20Overview/Chapter%203%20-%20%20Assets,%20Portfolios,%20and%20Arbitrage/Assets.md) or risk exists,  can it be exploited in a markettiming strategy? Later, in lecture 5, we will look more detail into optimal [asset allocation](Lecture%202-%20Asset%20Allocation%20with%20Multiple%20Risky%20Assets.md) in a multi-period setting when risk and expected return are time-varying. But for now,  let's just think about potentially applying this formula period-by-period,  with a oneperiod [investment](An%20Asset%20Allocation%20Primer.md) horizon. To do this,  we need to a statistical model that gives us [expectations](../Fixed%20Income%20Asset%20Pricing/Fixed%20Income%20Lecture%20Notes/FORWARD%20RATES%20AND%20TERM%20STRUCTURE.md) of next-period [returns](../Financial%20Markets/Financial%20Asset%20Pricing%20Theory%20Overview/Chapter%203%20-%20%20Assets,%20Portfolios,%20and%20Arbitrage/Assets.md) and/or forecasts of next-period volatility.
=======
The inputs of this optimal allocation formula could potentially vary over time. Perhaps there are times when expected excess [[Assets|returns]] are high and times when they are low? Perhaps there are times when volatility is high and other times when volatility is low? If such time-variation in expected [[Assets|returns]] or risk exists,  can it be exploited in a markettiming strategy? Later, in lecture 5, we will look more detail into optimal [[Lecture 2- Asset Allocation with Multiple Risky Assets|asset allocation]] in a multi-period setting when risk and expected return are time-varying. But for now,  let's just think about potentially applying this formula period-by-period,  with a oneperiod [[An Asset Allocation Primer|investment]] horizon. To do this,  we need to a statistical model that gives us [[FORWARD RATES AND TERM STRUCTURE|expectations]] of next-period [[Assets|returns]] and/or forecasts of next-period volatility.
>>>>>>> d83d5c06204d625fbecfdb77e4d3f37c9c80e27b

With this motivation in mind,  we will now look the data to answer questions such as: Are [stock market](../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20III%20THE%20PLAYERS/Chapter%2012%20-%20Hedge%20Fund%20Strategies/Hedge%20Fund%20Strategies.md) index [returns](../Financial%20Markets/Financial%20Asset%20Pricing%20Theory%20Overview/Chapter%203%20-%20%20Assets,%20Portfolios,%20and%20Arbitrage/Assets.md) predictable? If yes,  does such predictability allow market timing? What sort of variables can be useful predictors of [returns](../Financial%20Markets/Financial%20Asset%20Pricing%20Theory%20Overview/Chapter%203%20-%20%20Assets,%20Portfolios,%20and%20Arbitrage/Assets.md)? Is volatility predictable?

## 3.1 Conditional Probability Distributions

Questions about the asset allocation,  predictability,  and market timing all have to do with the conditional probability distribution of returns.

In the past two lectures we focused on the unconditional probability distribution of returns. The unconditional distribution describes how likely various outcomes are

in general,  without picking a subset of specific situations. For example,  we discussed how to estimate the unconditional mean of stock [returns](../Financial%20Markets/Financial%20Asset%20Pricing%20Theory%20Overview/Chapter%203%20-%20%20Assets,%20Portfolios,%20and%20Arbitrage/Assets.md) by taking a simple average of [returns](../Financial%20Markets/Financial%20Asset%20Pricing%20Theory%20Overview/Chapter%203%20-%20%20Assets,%20Portfolios,%20and%20Arbitrage/Assets.md).

In contrast,  the conditional distribution describes how likely various outcomes for returns are conditional on a subset of specific situations. For example,  suppose we come to the conclusion that the distribution of next period returns,  $R_{t+1}$ is different depending on whether returns in the current period,  $R_{t}$ are negative or positive. In this case,  the current period return $R_{t}$ is the conditioning information and the distribution of returns conditional on whether $R_{t}<0$ or $R_{t} \geq 0$ is the conditional distribution of returns.

Now,  the conditional distribution differs from the unconditional distribution only if the conditioning information (lagged returns in our example) actually has some useful information about the shape and location of probability distribution of future returns. To describe how the shape and location of this probability distribution changes with conditioning information,  we need a statistical model.

For example,  a crude statistical model of the conditional distribution of stock market returns would be to assert that that future returns may be drawn from two different distributions: one that applies when the market went up in the previous month,  the other one when it fell.

Figure 3.1 plots histograms of the two distributions: one depicts the distribution of stock market returns following a gain in the previous month; the other one depicts the distribution of stock market returns following a loss in the previous month. Interestingly,  the distributions do seem to be different! Note how the distribution following a loss is more spread out and less concentrated in the middle. This means that when the stock market has fallen in the previous month then,  historically,  it was followed by a more volatile month in which returns were likely to be either very high or very low.

Just as we can characterize unconditional probability distributions in terms of unconditional moments,  we can describe conditional distributions in terms of conditional moments. If $x_{t}$ is a variable that represents our conditioning information (in Figure $3.1 x_{t}$ would be an indicator for whether $R_{t}<0$ or $R_{t} \geq 0$ ),  then we can describe the distribution of $R_{t+1}$ conditional on $x_{t}$ with its conditional moments such as,  e.g.,  the conditional expected return,  $\mathbb{E}\left[R_{t+1} \mid x_{t}\right]$,  and the conditional variance $\operatorname{var}\left(R_{t+1} \mid x_{t}\right)$.

To make these conditional moments useful in applications,  we need a statistical model to describe them. Here is an example: Suppose there was momentum in returns,  by which we mean that high returns in month $t$ are followed,  on average,  by predictably high returns in month $t+1$. We could capture this with a model for conditional expected returns such as
$$

\mathbb{E}\left[R_{t+1} \mid R_{t}\right]=a+b R_{t}

$$

 ![500](https://cdn.mathpix.com/cropped/2024_10_19_48a1c4654e845915c45cg-073.jpg?height=790&width=969&top_left_y=353&top_left_x=600)

Figure 3.1: Distribution of monthly stock market returns 1927-2021 conditional on gain or loss in previous month

for some constants $a,      b>0$. If we had instead $b<0$,  this would be a model for reversals where high past returns predict low future returns. We can use regressions to estimate such models of conditional expected returns.

We often omit stating the conditioning information explicitly and just write $\mathbb{E}_{t}[\cdot]$,  e.g. $E_{t}\left[R_{t+1}\right]$. This is imprecise because this notation is not explicit about the type of information we are conditioning on,  but reduces clutter in our notation. Typically this notation means that we think of the expectations conditioned on whatever is observable to an investor at time $t$.

If returns are independently and identically (IID) distributed,  then conditional and unconditional distributions are the same. Or,  put differently,  in this case conditioning information about the current state of the economy etc. does not contain information about the distribution of future returns. Our crude analysis of the returns conditional on previous month's gain/loss in Figure 3.1 already suggests that returns are not IID,  as the two conditional distributions shown in this figure differ substantially (although we haven't yet done a formal statistical test to see whether the difference is really statistically significant).

## 3.2 Logarithmic returns

In this lecture and the coming ones,  we will pay more attention to the return dynamics over time. This means that we will have to take into account the compounding of returns.

Unfortunately,  working with compound [returns](../Financial%20Markets/Financial%20Asset%20Pricing%20Theory%20Overview/Chapter%203%20-%20%20Assets,%20Portfolios,%20and%20Arbitrage/Assets.md) is messy,  because compounding is multiplicative. Consider an asset that earns a sequence of [returns](../Financial%20Markets/Financial%20Asset%20Pricing%20Theory%20Overview/Chapter%203%20-%20%20Assets,%20Portfolios,%20and%20Arbitrage/Assets.md) over time: $R_{t+1},      R_{t+2},      \ldots,      R_{T}$. Calculation of the long-run return on this asset from time $t$ to $t+T$ involves compounding of [returns](../Financial%20Markets/Financial%20Asset%20Pricing%20Theory%20Overview/Chapter%203%20-%20%20Assets,%20Portfolios,%20and%20Arbitrage/Assets.md) over multiple periods:
$$

\begin{equation*}

R_{t: t+T}=\left(1+R_{t+1}\right) \times\left(1+R_{t+2}\right) \times \ldots \times\left(1+R_{t+T}\right)-1 \tag{3.2}

\end{equation*}

$$

This compound return involves products of random single period [returns](../Financial%20Markets/Financial%20Asset%20Pricing%20Theory%20Overview/Chapter%203%20-%20%20Assets,%20Portfolios,%20and%20Arbitrage/Assets.md). Products of random variables are statistically difficult to analyze. Things quickly become intractable.

When we analyze such long-run [returns](../Financial%20Markets/Financial%20Asset%20Pricing%20Theory%20Overview/Chapter%203%20-%20%20Assets,%20Portfolios,%20and%20Arbitrage/Assets.md),  it is often convenient to work with the natural logarithm of [returns](../Financial%20Markets/Financial%20Asset%20Pricing%20Theory%20Overview/Chapter%203%20-%20%20Assets,%20Portfolios,%20and%20Arbitrage/Assets.md),  or short just log [returns](../Financial%20Markets/Financial%20Asset%20Pricing%20Theory%20Overview/Chapter%203%20-%20%20Assets,%20Portfolios,%20and%20Arbitrage/Assets.md). ${ }^{1}$ We use lower-case letters to denote $\log$ [returns](../Financial%20Markets/Financial%20Asset%20Pricing%20Theory%20Overview/Chapter%203%20-%20%20Assets,%20Portfolios,%20and%20Arbitrage/Assets.md)
$$

\begin{equation*}

r_{t}=\log \left(1+R_{t}\right) \tag{3.3}

\end{equation*}

$$

The nice property of the log transformation is that the log of a product becomes the sum of the log of the factors of the product. Hence,  for the long-run return we get,  after taking the log,
$$

\begin{equation*}

r_{t: t+T}=\log \left(1+R_{t: t+T}\right)=r_{t+1}+r_{t+2}+\ldots+r_{t+T} \tag{3.4}

\end{equation*}

$$

i.e.,  the long-run log return is a simple sum of the individual period log [returns](../Financial%20Markets/Financial%20Asset%20Pricing%20Theory%20Overview/Chapter%203%20-%20%20Assets,%20Portfolios,%20and%20Arbitrage/Assets.md). Sums are much easier to analyze statistically than products of random variables.

Taking the exponential function of the log return gets us back to simple [returns](../Financial%20Markets/Financial%20Asset%20Pricing%20Theory%20Overview/Chapter%203%20-%20%20Assets,%20Portfolios,%20and%20Arbitrage/Assets.md)
$$

\begin{equation*}

R_{t: t+T}=\exp \left(r_{t+1}+r_{t+2}+\ldots+r_{t+T}\right)-1 \tag{3.5}

\end{equation*}

$$

When we use log [returns](../Financial%20Markets/Financial%20Asset%20Pricing%20Theory%20Overview/Chapter%203%20-%20%20Assets,%20Portfolios,%20and%20Arbitrage/Assets.md),  we always need to keep in mind that the log return is not the same as the simple return. For example,  as we will see in more detail in the next lecture,  looking for a [portfolio](An%20Asset%20Allocation%20Primer.md) that maximizes the expected log return of the [portfolio](An%20Asset%20Allocation%20Primer.md) is not the same as one that maximizes the expected simple return. For now,  let's just note two things that we should keep in mind.

First,  the expected log return is not the same as the log of one plus the [expected return](Lecture%201-%20Probability%20Distributions%20of%20Returns.md). The following relations hold:
$$

\begin{equation*}

\mathbb{E}\left[R_{t}\right] \geq \log \mathbb{E}\left[1+R_{t}\right] \geq \mathbb{E}\left[r_{t}\right] \tag{3.6}

\end{equation*}

$$

[^8]The first inequality on the left just reflects that $\log (1+x) \leq x$ for any real $x$. The second inequality on the right is a special case of a mathematical law called [Jensen's inequality](../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%208/Volatility%20and%20Convexity.md). For risky [returns](../Financial%20Markets/Financial%20Asset%20Pricing%20Theory%20Overview/Chapter%203%20-%20%20Assets,%20Portfolios,%20and%20Arbitrage/Assets.md) with non-zero variance,  both inequalities are strict. We get a more precise statement about the relation between these two [expectations](../Fixed%20Income%20Asset%20Pricing/Fixed%20Income%20Lecture%20Notes/FORWARD%20RATES%20AND%20TERM%20STRUCTURE.md) if we impose an assumption about the statistical distribution of [returns](../Financial%20Markets/Financial%20Asset%20Pricing%20Theory%20Overview/Chapter%203%20-%20%20Assets,%20Portfolios,%20and%20Arbitrage/Assets.md). More on this below.

Second,  the log of weighted average of simple [returns](../Financial%20Markets/Financial%20Asset%20Pricing%20Theory%20Overview/Chapter%203%20-%20%20Assets,%20Portfolios,%20and%20Arbitrage/Assets.md) (i.e.,  the log of a [portfolio](An%20Asset%20Allocation%20Primer.md) return) is not equal to the weighted average of the log [returns](../Financial%20Markets/Financial%20Asset%20Pricing%20Theory%20Overview/Chapter%203%20-%20%20Assets,%20Portfolios,%20and%20Arbitrage/Assets.md) of the individual assets. Suppose we have $N$ assets and we collect their [returns](../Financial%20Markets/Financial%20Asset%20Pricing%20Theory%20Overview/Chapter%203%20-%20%20Assets,%20Portfolios,%20and%20Arbitrage/Assets.md) $R_{1},      R_{2},      \ldots,      R_{N}$ in the vector $\boldsymbol{r}$. For a [portfolio](An%20Asset%20Allocation%20Primer.md) with weights $\boldsymbol{\omega}$,  the (simple) return on a [portfolio](An%20Asset%20Allocation%20Primer.md) is simply the weighted average of individual asset (simple) [returns](../Financial%20Markets/Financial%20Asset%20Pricing%20Theory%20Overview/Chapter%203%20-%20%20Assets,%20Portfolios,%20and%20Arbitrage/Assets.md):
$$

\begin{equation*}

R_{p}=\boldsymbol{\omega}^{\prime} \boldsymbol{r} \tag{3.7}

\end{equation*}

$$

The same is not true for log [returns](../Financial%20Markets/Financial%20Asset%20Pricing%20Theory%20Overview/Chapter%203%20-%20%20Assets,%20Portfolios,%20and%20Arbitrage/Assets.md). A weighted average of log [returns](../Financial%20Markets/Financial%20Asset%20Pricing%20Theory%20Overview/Chapter%203%20-%20%20Assets,%20Portfolios,%20and%20Arbitrage/Assets.md) is not equal to the $\log$ return on the [portfolio](An%20Asset%20Allocation%20Primer.md),  $r_{p}=\log \left(\boldsymbol{\omega}^{\prime} \boldsymbol{r}\right)$.

Now that we have log [returns](../Financial%20Markets/Financial%20Asset%20Pricing%20Theory%20Overview/Chapter%203%20-%20%20Assets,%20Portfolios,%20and%20Arbitrage/Assets.md) in our toolbox,  we can also get a more realistic in our assumptions about the distribution of [returns](../Financial%20Markets/Financial%20Asset%20Pricing%20Theory%20Overview/Chapter%203%20-%20%20Assets,%20Portfolios,%20and%20Arbitrage/Assets.md). In the past two lectures,  we assumed in some analyses and simulations that simple [returns](../Financial%20Markets/Financial%20Asset%20Pricing%20Theory%20Overview/Chapter%203%20-%20%20Assets,%20Portfolios,%20and%20Arbitrage/Assets.md) are normally distributed. Strictly speaking,  this assumption did not really make economic sense. The support of the normal distribution is unbounded in both tails. This means that assuming normally distributed [returns](../Financial%20Markets/Financial%20Asset%20Pricing%20Theory%20Overview/Chapter%203%20-%20%20Assets,%20Portfolios,%20and%20Arbitrage/Assets.md) implies positive probability on the event that [returns](../Financial%20Markets/Financial%20Asset%20Pricing%20Theory%20Overview/Chapter%203%20-%20%20Assets,%20Portfolios,%20and%20Arbitrage/Assets.md) are less than $-100/%,  which is impossible for assets like equity where investors are protected by limited liability and hence can lose at most their initial [investment](An%20Asset%20Allocation%20Primer.md).

At short horizons,  this issue is negligible because typical return magnitudes are so small. But it matters more over longer horizons. This is why now that we are paying more attention to long-run dynamics,  we need to address this issue.

Figure 3.2 illustrates this. It shows the [empirical distribution](Lecture%201-%20Probability%20Distributions%20of%20Returns.md) of [stock market](../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20III%20THE%20PLAYERS/Chapter%2012%20-%20Hedge%20Fund%20Strategies/Hedge%20Fund%20Strategies.md) [returns](../Financial%20Markets/Financial%20Asset%20Pricing%20Theory%20Overview/Chapter%203%20-%20%20Assets,%20Portfolios,%20and%20Arbitrage/Assets.md) from 1927-2022. The top panel shows the distribution of monthly [returns](../Financial%20Markets/Financial%20Asset%20Pricing%20Theory%20Overview/Chapter%203%20-%20%20Assets,%20Portfolios,%20and%20Arbitrage/Assets.md),  the middle panel annual [returns](../Financial%20Markets/Financial%20Asset%20Pricing%20Theory%20Overview/Chapter%203%20-%20%20Assets,%20Portfolios,%20and%20Arbitrage/Assets.md),  and the bottom panel 10-year [returns](../Financial%20Markets/Financial%20Asset%20Pricing%20Theory%20Overview/Chapter%203%20-%20%20Assets,%20Portfolios,%20and%20Arbitrage/Assets.md). We see that for monthly [returns](../Financial%20Markets/Financial%20Asset%20Pricing%20Theory%20Overview/Chapter%203%20-%20%20Assets,%20Portfolios,%20and%20Arbitrage/Assets.md) the fact that [returns](../Financial%20Markets/Financial%20Asset%20Pricing%20Theory%20Overview/Chapter%203%20-%20%20Assets,%20Portfolios,%20and%20Arbitrage/Assets.md) are bounded below at $-100/% does not really matter. It's just extremely unlikely that a monthly return would ever get even close to a loss of this magnitude. As a consequence,  the distribution of monthly [returns](../Financial%20Markets/Financial%20Asset%20Pricing%20Theory%20Overview/Chapter%203%20-%20%20Assets,%20Portfolios,%20and%20Arbitrage/Assets.md) looks quite symmetric. The magnitudes of upside moves tend to be similar to the magnitudes of downside moves.

In contrast,  for 10-year [returns](../Financial%20Markets/Financial%20Asset%20Pricing%20Theory%20Overview/Chapter%203%20-%20%20Assets,%20Portfolios,%20and%20Arbitrage/Assets.md),  the picture is different. Looking at the upside in the bottom panel of Figure 3.2,  we can see 10-year periods with realized [returns](../Financial%20Markets/Financial%20Asset%20Pricing%20Theory%20Overview/Chapter%203%20-%20%20Assets,%20Portfolios,%20and%20Arbitrage/Assets.md) of 400/% or more. On the downside,  of course,  there are no downside moves of similar magnitude. The biggest losses over 10-year periods in this data set are [returns](../Financial%20Markets/Financial%20Asset%20Pricing%20Theory%20Overview/Chapter%203%20-%20%20Assets,%20Portfolios,%20and%20Arbitrage/Assets.md) of around -50/%. As a consequence,  the [empirical distribution](Lecture%201-%20Probability%20Distributions%20of%20Returns.md) of 10 -year [returns](../Financial%20Markets/Financial%20Asset%20Pricing%20Theory%20Overview/Chapter%203%20-%20%20Assets,%20Portfolios,%20and%20Arbitrage/Assets.md) is strongly asymmetric. It basically has to be as the upside is unbounded but the downside is limited to -100 %.

 ![500](https://cdn.mathpix.com/cropped/2024_10_19_48a1c4654e845915c45cg-076.jpg?height=1060&width=1330&top_left_y=359&top_left_x=346)

Figure 3.2: Empirical [stock market](../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20III%20THE%20PLAYERS/Chapter%2012%20-%20Hedge%20Fund%20Strategies/Hedge%20Fund%20Strategies.md) return distributions when [returns](../Financial%20Markets/Financial%20Asset%20Pricing%20Theory%20Overview/Chapter%203%20-%20%20Assets,%20Portfolios,%20and%20Arbitrage/Assets.md) are measured over different horizons,  1927-2022

In contrast,  it is an economically sensible approximation for many types of assets,  although of course not always literally true,  that $\log$ [returns](../Financial%20Markets/Financial%20Asset%20Pricing%20Theory%20Overview/Chapter%203%20-%20%20Assets,%20Portfolios,%20and%20Arbitrage/Assets.md),  $r=\log (1+R)$,  are normally distributed.

If log [returns](../Financial%20Markets/Financial%20Asset%20Pricing%20Theory%20Overview/Chapter%203%20-%20%20Assets,%20Portfolios,%20and%20Arbitrage/Assets.md) are normally distributed,  this means that simple [returns](../Financial%20Markets/Financial%20Asset%20Pricing%20Theory%20Overview/Chapter%203%20-%20%20Assets,%20Portfolios,%20and%20Arbitrage/Assets.md) plus one,  $1+R=\exp (r)$,  are log-normally distributed. Since $\exp (r)-1$ is bounded below by -1 when $r$ is normally distributed,  the log-normal distribution is consistent exactly with the theoretical lower bound on stock [returns](../Financial%20Markets/Financial%20Asset%20Pricing%20Theory%20Overview/Chapter%203%20-%20%20Assets,%20Portfolios,%20and%20Arbitrage/Assets.md) of $-100/%. So,    using the log-normal distribution for $1+R$,  we can have a distribution of one plus simple [returns](../Financial%20Markets/Financial%20Asset%20Pricing%20Theory%20Overview/Chapter%203%20-%20%20Assets,%20Portfolios,%20and%20Arbitrage/Assets.md) that is realistically right-skewed and bounded below at zero,  but is still fully described by mean

 ![500](https://cdn.mathpix.com/cropped/2024_10_19_48a1c4654e845915c45cg-077.jpg?height=955&width=1199&top_left_y=284&top_left_x=474)

Figure 3.3: Probability distribution of $R$ when $r=\log (1+R)$ is normally distributed

and variance.

Figure 3.3 presents an example where $r$ is normally distributed and hence $1+R$ has a log-normal distribution (the plot shows the distribution of $R$,  not $1+R$ ). Note the lower bound at -1 and also the right-skewness (greater upside) of $R$ compared with $r$.

Going in the reverse direction,  if log-normality is approximately a good description of the return distribution,  then,  if we apply the $\log$ transformation,  $r=\log (1+R)$,  to empirically observed [returns](../Financial%20Markets/Financial%20Asset%20Pricing%20Theory%20Overview/Chapter%203%20-%20%20Assets,%20Portfolios,%20and%20Arbitrage/Assets.md) $R$,  we should be getting a distribution that looks closer to a normal distribution than the distribution of $R$ does.

We can see the effect of the log transformation if we redo the bottom plot from Figure 3.2 for 10-year [returns](../Financial%20Markets/Financial%20Asset%20Pricing%20Theory%20Overview/Chapter%203%20-%20%20Assets,%20Portfolios,%20and%20Arbitrage/Assets.md),  but now with $\log$ [returns](../Financial%20Markets/Financial%20Asset%20Pricing%20Theory%20Overview/Chapter%203%20-%20%20Assets,%20Portfolios,%20and%20Arbitrage/Assets.md). See Figure 3.4. While the distribution is not quite normal,  it is now much closer to being symmetric. The log transformation has shrunk the long upper tail and hence removed the positive skewness. Instead,  the distribution is now somewhat negatively skewed.

At short horizons,  though,  normal distribution can often be a good approximation to the log-normal distribution. The reason is that for small variance,  the log-normal distribution becomes close to symmetric. One way to see this is to note that $\exp (x) \approx$

 ![500](https://cdn.mathpix.com/cropped/2024_10_19_48a1c4654e845915c45cg-078.jpg?height=779&width=971&top_left_y=353&top_left_x=531)

Figure 3.4: [Empirical distribution](Lecture%201-%20Probability%20Distributions%20of%20Returns.md) of 10-year log [returns](../Financial%20Markets/Financial%20Asset%20Pricing%20Theory%20Overview/Chapter%203%20-%20%20Assets,%20Portfolios,%20and%20Arbitrage/Assets.md) on a [stock market](../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20III%20THE%20PLAYERS/Chapter%2012%20-%20Hedge%20Fund%20Strategies/Hedge%20Fund%20Strategies.md) index,  19272022
$1+x$ for very small $x$.

Empirically,  we also see that the distribution of historical [returns](../Financial%20Markets/Financial%20Asset%20Pricing%20Theory%20Overview/Chapter%203%20-%20%20Assets,%20Portfolios,%20and%20Arbitrage/Assets.md) is closer to normal when they are measured over shorter time frames. Check out,  for instance,  the top panel of Figure 3.2. Like a normal distribution,  monthly [returns](../Financial%20Markets/Financial%20Asset%20Pricing%20Theory%20Overview/Chapter%203%20-%20%20Assets,%20Portfolios,%20and%20Arbitrage/Assets.md) are close to symmetric,  unlike the longer horizon [returns](../Financial%20Markets/Financial%20Asset%20Pricing%20Theory%20Overview/Chapter%203%20-%20%20Assets,%20Portfolios,%20and%20Arbitrage/Assets.md) in the bottom panel.

But there are some important exceptions from log-normality: Occasionally the [stock market](../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20III%20THE%20PLAYERS/Chapter%2012%20-%20Hedge%20Fund%20Strategies/Hedge%20Fund%20Strategies.md) experiences violent crashes. This makes the left tail of the distribution much fatter than in a normal distribution. Occasionally,  there are also huge upward movements in a single month. This generates the fat right tail of the distribution in the top panel of Figure 3.2.

The log-normal distribution has a number of properties that we will use in the coming

weeks. If $r_{t} \sim \mathcal{N}\left(\mu,      \sigma^{2}\right)$ and $1+R_{t}=\exp \left(r_{t}\right)$,  then
$$

\begin{align*}

\log \mathbb{E}\left[1+R_{t}\right] & =\mathbb{E}\left[\log \left(1+R_{t}\right)\right]+\frac{1}{2} \operatorname{var}\left[\log \left(1+R_{t}\right)\right] \\

& =\mathbb{E}\left[r_{t}\right]+\frac{1}{2} \operatorname{var}\left(r_{t}\right) \\

& =\mu+\frac{1}{2} \sigma^{2} \tag{3.8}

\end{align*}

$$

and hence
$$

\begin{equation*}

1+\mathbb{E}\left[R_{t}\right]=\exp \left(\mu+\frac{1}{2} \sigma^{2}\right) \tag{3.9}

\end{equation*}

$$

Approximately then,  at least for relatively short return measurement intervals such as monthly [returns](../Financial%20Markets/Financial%20Asset%20Pricing%20Theory%20Overview/Chapter%203%20-%20%20Assets,%20Portfolios,%20and%20Arbitrage/Assets.md) where the return magnitudes are typically not so big that the transformation by the exponential function matters much,
$$

\begin{equation*}

\mathbb{E}\left[R_{t}\right] \approx \mu+\frac{1}{2} \sigma^{2} \tag{3.10}

\end{equation*}

$$

This approximation is a useful rule of thumb to keep in mind. If you see someone presenting average log [returns](../Financial%20Markets/Financial%20Asset%20Pricing%20Theory%20Overview/Chapter%203%20-%20%20Assets,%20Portfolios,%20and%20Arbitrage/Assets.md) from some [investment](An%20Asset%20Allocation%20Primer.md) and the variance of log [returns](../Financial%20Markets/Financial%20Asset%20Pricing%20Theory%20Overview/Chapter%203%20-%20%20Assets,%20Portfolios,%20and%20Arbitrage/Assets.md),  you can easily get an estimate of the implied average simple [returns](../Financial%20Markets/Financial%20Asset%20Pricing%20Theory%20Overview/Chapter%203%20-%20%20Assets,%20Portfolios,%20and%20Arbitrage/Assets.md) using this formula.

## 3.3 Stock market valuation models

With log transformations in our toolkit,  we now turn our attention to valuation models that allow us to analyze how investor [expectations](../Fixed%20Income%20Asset%20Pricing/Fixed%20Income%20Lecture%20Notes/FORWARD%20RATES%20AND%20TERM%20STRUCTURE.md) and [Investor Sentiment](Lecture%204-%20[[Lecture%204-%20Investor%20Sentiment)|[investor sentiment](Lecture%204-%20Investor%20Sentiment.md)]] may affect [pricing](../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%207/Arbitrage%20Pricing%20of%20Derivatives.md) in the [stock market](../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20III%20THE%20PLAYERS/Chapter%2012%20-%20Hedge%20Fund%20Strategies/Hedge%20Fund%20Strategies.md) (and other risky [asset markets](../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%201%20-%20Purpose%20and%20Structure%20of%20Financial%20Markets/Primary%20Issuance%20and%20Secondary%20Resale%20Markets.md)). This in turn provides insights about observable variables that may be useful for predicting [stock market](../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20III%20THE%20PLAYERS/Chapter%2012%20-%20Hedge%20Fund%20Strategies/Hedge%20Fund%20Strategies.md) [returns](../Financial%20Markets/Financial%20Asset%20Pricing%20Theory%20Overview/Chapter%203%20-%20%20Assets,%20Portfolios,%20and%20Arbitrage/Assets.md).

For now,  we use [Investor Sentiment](Lecture%204-%20[[Lecture%204-%20Investor%20Sentiment)|[investor sentiment](Lecture%204-%20Investor%20Sentiment.md)]] as a catch-all label to describe forces that affect stock prices and that do not reflect rational [expectations](../Fixed%20Income%20Asset%20Pricing/Fixed%20Income%20Lecture%20Notes/FORWARD%20RATES%20AND%20TERM%20STRUCTURE.md) of [future cash flows](../Financial%20Engineering/Advanced%20Derivatives%20Pricing%20Methodology.md) of firms. This includes,  for example,  the effects of irrational investor optimism or pessimism about [future cash flows](../Financial%20Engineering/Advanced%20Derivatives%20Pricing%20Methodology.md). It also includes the [stock price](../Financial%20Engineering/Derivatives/Part%20IV%20-%20Options/Chapter%2016%20-%20Black–Scholes%20Model.md) effects of time-varying risk aversion that investors may have. In the next lecture,  we'll take a more detailed look at what could explain [Investor Sentiment](Lecture%204-%20[[Lecture%204-%20Investor%20Sentiment)|[investor sentiment](Lecture%204-%20Investor%20Sentiment.md)]] changes over time.

The [discounted cash flow](../Financial%20Instruments/Lehman%20Brothers%20Option%20Adjusted%20Spread.md) (DCF) valuation models that you are familiar with from your introductory finance classes look somewhat like this
$$

\begin{equation*}

P_{t}=\frac{\mathbb{E}_{t}\left[D_{t+1}\right]}{1+R}+\frac{\mathbb{E}_{t}\left[D_{t+2}\right]}{(1+R)^{2}}+\frac{\mathbb{E}_{t}\left[D_{t+3}\right]}{(1+R)^{3}}+\ldots \tag{3.11}

\end{equation*}

$$

where $P_{t}$ is present value of cash flows,  $D_{t+1},      D_{t+2},      \ldots$ are [future cash flows](../Financial%20Engineering/Advanced%20Derivatives%20Pricing%20Methodology.md),  and $R$ is a (risk-adjusted) [discount rate](../Advanced%20Financial%20Analysis%20and%20Valuation/Problem%20Sets/PSET%207-%20Kohler.md). Here we are interested in the valuation of the [stock market](../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20III%20THE%20PLAYERS/Chapter%2012%20-%20Hedge%20Fund%20Strategies/Hedge%20Fund%20Strategies.md) in aggregate,  so $D$ would represent the aggregate dividends of all stocks. More precisely,  $D_{t}$ would comprise aggregate dividends plus aggregate share repurchases,  i.e.,  the entire flow of cash to investors. To keep it short,  I'll just refer to $D_{t}$ as dividends.

You may also recall that if the [expected cash flows](../Advanced%20Financial%20Analysis%20and%20Valuation/Lecture%20Notes%20Advanced%20Financial%20Analysis%20and%20Valuation/Week%206/Week%206%20Assignment%20Review.md) are growing at constant rate $G$,  so that $\mathbb{E}_{t}\left[D_{t+1}\right]=(1+G) D_{t},      \mathbb{E}_{t}\left[D_{t+2}\right]=(1+G)^{2} D_{t}$,  then we get the so-called Gordon growth model
$$

\begin{equation*}

P_{t}=D_{t} \frac{1+G}{R-G} \tag{3.12}

\end{equation*}

$$

or
$$

\begin{equation*}

\frac{P_{t}}{D_{t}}=\frac{1+G}{R-G} \tag{3.13}

\end{equation*}

$$

The trouble with these sorts of valuation models is that they are mixes of summations and multiplicative relationships. For our purposes,  we want something even simpler,  only with additive terms,  not ratios and powers of stuff. We're looking for such a simple valuation framework so that we can easily think through the consequences of timevarying [Investor Sentiment](Lecture%204-%20[[Lecture%204-%20Investor%20Sentiment)|[investor sentiment](Lecture%204-%20Investor%20Sentiment.md)]] on aggregate [stock market](../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20III%20THE%20PLAYERS/Chapter%2012%20-%20Hedge%20Fund%20Strategies/Hedge%20Fund%20Strategies.md) prices,  and the implications for market-timing strategies.

As it turns out,  logs and some approximations can help us here.

Consider first the case in which we are at time $t$ and an asset has just one more terminal dividend payment left at $t+1$ (after it just paid out $D_{t}$ at $t$ ). After this terminal payment,  the asset ceases to exist. The return over this last period is
$$

\begin{equation*}

1+R_{t+1}=\frac{D_{t+1}}{P_{t}} \tag{3.14}

\end{equation*}

$$

We can rewrite the right-hand side as
$$

\begin{equation*}

\frac{D_{t+1}}{P_{t}}=\frac{D_{t+1}}{D_{t}} \frac{D_{t}}{P_{t}} \tag{3.15}

\end{equation*}

$$

Taking logs of both sides of this equation,  rearranging,  and using the definitions $v_{t}=$ $\log \left(P_{t} / D_{t}\right)$ and $\Delta d_{t+1}=\log \left(D_{t+1} / D_{t}\right)$,  we get
$$

\begin{equation*}

v_{t}=\Delta d_{t+1}-r_{t+1} \tag{3.16}

\end{equation*}

$$

The left-hand side of this equation is the log [price-dividend ratio](Lecture%204-%20Investor%20Sentiment.md). Even though this is an extremely simple relationship,  it already tells us something important: If we see a high [price-dividend ratio](Lecture%204-%20Investor%20Sentiment.md) today,  then it must either be the case that future dividends will be

high or [returns](../Financial%20Markets/Financial%20Asset%20Pricing%20Theory%20Overview/Chapter%203%20-%20%20Assets,%20Portfolios,%20and%20Arbitrage/Assets.md) in the future will be low,  or a combination of both. Taking logs helped us get a valuation model,  in terms of the log [price-dividend ratio](Lecture%204-%20Investor%20Sentiment.md),  that nicely involves only additive terms.

When there is more than one period left we calculate [returns](../Financial%20Markets/Financial%20Asset%20Pricing%20Theory%20Overview/Chapter%203%20-%20%20Assets,%20Portfolios,%20and%20Arbitrage/Assets.md) as
$$

\begin{equation*}

1+R_{t+1}=\frac{P_{t+1}+D_{t+1}}{P_{t}} \tag{3.17}

\end{equation*}

$$

Taking logs in this case does not immediately lead to a simple additive expression. However,  one can find a quite accurate linear approximation. We won't go into the details of how to do this,  but the end result makes intuitive sense in comparison with the single-period version $(3.16):^{2}$ The result of the approximation is
$$

\begin{equation*}

v_{t}=c+\Delta d_{t+1}-r_{t+1}+\rho v_{t+1} \tag{3.18}

\end{equation*}

$$

where $\rho$ is a number very close to one,  something like 0.96 if [returns](../Financial%20Markets/Financial%20Asset%20Pricing%20Theory%20Overview/Chapter%203%20-%20%20Assets,%20Portfolios,%20and%20Arbitrage/Assets.md) are measured annually,  or 0.99 if [returns](../Financial%20Markets/Financial%20Asset%20Pricing%20Theory%20Overview/Chapter%203%20-%20%20Assets,%20Portfolios,%20and%20Arbitrage/Assets.md) are measured quarterly. The constant $c$ doesn't matter much for what we will discuss so I did not write out explicitly what determines this constant.
${ }^{2}$ For those who are interested in seeing the steps to get there: Rewrite (3.17) as
$$

\begin{aligned}

1+R_{t+1} & =\frac{D_{t+1}}{D_{t}} \frac{\frac{P_{t+1}}{D_{t+1}}+1}{\frac{P_{t}}{D_{t}}} \\

& =\frac{D_{t+1}}{D_{t}} \frac{\frac{P_{t+1}}{D_{t+1}}}{\frac{P_{t}}{D_{t}}}\left(1+\frac{D_{t+1}}{P_{t+1}}\right)

\end{aligned}

$$

and take logs and let $v_{t}=\log \left(P_{t} / D_{t}\right)$,
$$

r_{t+1}=\Delta d_{t+1}+v_{t+1}-v_{t}+\log \left(1+\exp \left(-v_{t+1}\right)\right)

$$

Use a first-order Taylor expansion to approximate the last term linearly as a function of $v_{t+1}$ around $\bar{v}$
$$

\log \left(1+\exp \left(-v_{t+1}\right)\right) \approx c-(1-\rho) v_{t+1}

$$

where the derivative in this Taylor expansion is $-(1-\rho)=-[1 /(1+\exp (-\bar{v}))] \exp (\bar{v})$ which means $\rho=1 /(1+\exp (-\bar{v})$; the constant is $c=-\log \rho-(1-\rho) \log (1 / \rho-1)$. We can see that $\rho$ is a constant very close to one for any reasonable value of $v$. If we take $\bar{v}$ to be the long-term historical average of the [price-dividend ratio](Lecture%204-%20Investor%20Sentiment.md) with annual data,  which is around 3.2 ,  we have something in the ballpark of $\rho=1 /(1+\exp (-3)) \approx 0.96$ for annual data (and $0.96^{\frac{1}{4}} \approx 0.99$ for quarterly data). Plugging the approximation in (2) into (2),  we get
$$

r_{t+1} \approx c+\Delta d_{t+1}+v_{t+1}-v_{t}-(1-\rho) v_{t+1}

$$

which we can solve for $v_{t}$ to get (3.18). This approximation was first proposed by Campbell,  J.Y. and Shiller,  R.J.,  1988. The dividend-price ratio and [expectations](../Fixed%20Income%20Asset%20Pricing/Fixed%20Income%20Lecture%20Notes/FORWARD%20RATES%20AND%20TERM%20STRUCTURE.md) of future dividends and discount factors. The Review of Financial Studies,  1(3),  pp0.\1-228.

The equation (3.18) looks very similar to (3.16) - just with the addition of $\rho v_{t+1}$ (and the constant $c$,  but again that constant won't matter much for anything). So when $v_{t}$ is high,  there could now be three different ways in which the future plays out: high [dividend growth](../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%202%20-%20Spot%20Markets/Equity%20Commodity%20and%20Currency%20Math.md),  low [returns](../Financial%20Markets/Financial%20Asset%20Pricing%20Theory%20Overview/Chapter%203%20-%20%20Assets,%20Portfolios,%20and%20Arbitrage/Assets.md),  or high future [price-dividend ratio](Lecture%204-%20Investor%20Sentiment.md).

We can also take [expectations](../Fixed%20Income%20Asset%20Pricing/Fixed%20Income%20Lecture%20Notes/FORWARD%20RATES%20AND%20TERM%20STRUCTURE.md) of (3.18). We get
$$

\begin{equation*}

v_{t}=c+\mathbb{E}_{t}\left[\Delta d_{t+1}\right]-\mathbb{E}_{t}\left[r_{t+1}\right]+\rho \mathbb{E}_{t}\left[v_{t+1}\right] \tag{3.19}

\end{equation*}

$$

which we can solve for
$$

\begin{equation*}

\mathbb{E}_{t}\left[r_{t+1}\right]=c+\mathbb{E}_{t}\left[\Delta d_{t+1}\right]+\rho \mathbb{E}_{t}\left[v_{t+1}\right]-v_{t} \tag{3.20}

\end{equation*}

$$

So,  if we expect a high return today,  we must either expect high dividends next period,  or a high [price-dividend ratio](Lecture%204-%20Investor%20Sentiment.md) next period,  or a combination of the two.

We can take this further and iterate on (3.18). Substituting $v_{t+1}=c+\Delta d_{t+2}-r_{t+2}+$ $\rho v_{t+2}$ into (3.18),  we get
$$

\begin{equation*}

v_{t}=c+\rho c+\Delta d_{t+1}+\rho \Delta d_{t+2}-r_{t+1}-\rho r_{t+2}+\rho^{2} v_{t+2} \tag{3.21}

\end{equation*}

$$

Doing this $T$ times,  we get
$$

\begin{equation*}

v_{t}=\frac{c}{1-\rho}\left(1-\rho^{T+1}\right)+\sum_{j=1}^{T+1} \rho^{j-1}\left(\Delta d_{t+j}-r_{t+j}\right)+\rho^{T+1} v_{T+1} \tag{3.22}

\end{equation*}

$$

Now consider taking $T$ to infinity. The first term and the summation term are straightforward. The key question is what happens to $\rho^{T+1} v_{T+1}$. Recall that $\rho$ is a number close to but smaller than one. So $\rho^{T+1}$ goes to zero when $T$ goes to infinity. Then $\rho^{T+1} v_{T+1}$ also goes to zero,  unless the [price-dividend ratio](Lecture%204-%20Investor%20Sentiment.md) is on an explosive path on which it grows without upper bound in the long-run and it grows faster than $\rho^{T+1}$ shrinks. But such an exploding dividend-price ratio doesn't really make economic sense. Therefore,  we assume that
$$

\begin{equation*}

\lim _{T \rightarrow \infty} \rho^{T+1} v_{T+1}=0 \tag{3.23}

\end{equation*}

$$

This seems like a reasonable assumption (it's known as a transversality condition). Prices should not be wandering away arbitrarily far from dividends. Temporarily,  price levels might vary a lot relative to dividends,  but it would be rather weird if stock prices could diverge on a path towards an infinitely high [price-dividend ratio](Lecture%204-%20Investor%20Sentiment.md) in the long run. We will come back to think more about this assumption in the next lecture,  but for now we will assume that the condition (3.23) holds. With this assumption,  letting $T$ go to infinity yields
$$

\begin{equation*}

v_{t}=\frac{c}{1-\rho}+\sum_{j=1}^{\infty} \rho^{j-1}\left(\Delta d_{t+j}-r_{t+j}\right) \tag{3.24}

\end{equation*}

$$

which we refer to as present-value identity.

So now we have to possibilities left,  as earlier in (3.16),  but with many future periods: High [price-dividend ratio](Lecture%204-%20Investor%20Sentiment.md) today means that either future dividends will be high,  or [returns](../Financial%20Markets/Financial%20Asset%20Pricing%20Theory%20Overview/Chapter%203%20-%20%20Assets,%20Portfolios,%20and%20Arbitrage/Assets.md) in the future will be low. This should make intuitive sense. If you pay a high price for an asset today then either you'll be lucky enough that the cash flows you receive from this asset are also high,  or otherwise you will have to suffer from earning low [returns](../Financial%20Markets/Financial%20Asset%20Pricing%20Theory%20Overview/Chapter%203%20-%20%20Assets,%20Portfolios,%20and%20Arbitrage/Assets.md).

At this point,  (3.24) is just a tautological identity. The relationship between pricedividend ratio and future [dividend growth](../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%202%20-%20Spot%20Markets/Equity%20Commodity%20and%20Currency%20Math.md) and [returns](../Financial%20Markets/Financial%20Asset%20Pricing%20Theory%20Overview/Chapter%203%20-%20%20Assets,%20Portfolios,%20and%20Arbitrage/Assets.md) that we described must hold mechanically,  always. It does not depend on whether markets are efficient,  investors' risk aversion is constant or not,  or anything else. It's just mechanical. So the insights coming from it are also naturally limited. But we can use the identity to do useful things with it.

If we introduce [expectations](../Fixed%20Income%20Asset%20Pricing/Fixed%20Income%20Lecture%20Notes/FORWARD%20RATES%20AND%20TERM%20STRUCTURE.md) of dividends and [returns](../Financial%20Markets/Financial%20Asset%20Pricing%20Theory%20Overview/Chapter%203%20-%20%20Assets,%20Portfolios,%20and%20Arbitrage/Assets.md) we can turn the identity into a valuation model. We do this by taking expected values of the rightand left-hand side of (3.24) conditional on time- $t$ information. Since $v_{t}$ is observable at time $t$,  its expectation is just $v_{t}$. But on the right-hand side we have [expectations](../Fixed%20Income%20Asset%20Pricing/Fixed%20Income%20Lecture%20Notes/FORWARD%20RATES%20AND%20TERM%20STRUCTURE.md) of dividends and [returns](../Financial%20Markets/Financial%20Asset%20Pricing%20Theory%20Overview/Chapter%203%20-%20%20Assets,%20Portfolios,%20and%20Arbitrage/Assets.md) in the future:
$$

\begin{equation*}

v_{t}=\frac{c}{1-\rho}+\sum_{j=1}^{\infty} \rho^{j-1} \mathbb{E}_{t}\left[\Delta d_{t+j}\right]-\sum_{j=1}^{\infty} \rho^{j-1} \mathbb{E}_{t}\left[r_{t+j}\right] \tag{3.25}

\end{equation*}

$$

So the [price-dividend ratio](Lecture%204-%20Investor%20Sentiment.md) reflects [expectations](../Fixed%20Income%20Asset%20Pricing/Fixed%20Income%20Lecture%20Notes/FORWARD%20RATES%20AND%20TERM%20STRUCTURE.md) of future dividend and future [returns](../Financial%20Markets/Financial%20Asset%20Pricing%20Theory%20Overview/Chapter%203%20-%20%20Assets,%20Portfolios,%20and%20Arbitrage/Assets.md).

The model in (3.25) could now be used for fundamental valuation. We would have to build a [forecasting](../Advanced%20Financial%20Analysis%20and%20Valuation/Lecture%20Notes%20Advanced%20Financial%20Analysis%20and%20Valuation/Week%202/Week%202%20Fundamentals%20Of%20Forecasting.md) model for future [dividend growth](../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%202%20-%20Spot%20Markets/Equity%20Commodity%20and%20Currency%20Math.md). This would give us the [expectations](../Fixed%20Income%20Asset%20Pricing/Fixed%20Income%20Lecture%20Notes/FORWARD%20RATES%20AND%20TERM%20STRUCTURE.md) of future [dividend growth](../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%202%20-%20Spot%20Markets/Equity%20Commodity%20and%20Currency%20Math.md),  $\mathbb{E}_{t}\left[\Delta d_{t+j}\right]$. We could then also plug the required rate of return for $\mathbb{E}_{t}\left[r_{t+j}\right]$ that we would require from a [stock market](../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20III%20THE%20PLAYERS/Chapter%2012%20-%20Hedge%20Fund%20Strategies/Hedge%20Fund%20Strategies.md) [investment](An%20Asset%20Allocation%20Primer.md). This would then give us a model implied log [price-dividend ratio](Lecture%204-%20Investor%20Sentiment.md) $v_{t}$ that we could compare to the current actual $v_{t}$ to estimate current over/undervaluation of [stock market](../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20III%20THE%20PLAYERS/Chapter%2012%20-%20Hedge%20Fund%20Strategies/Hedge%20Fund%20Strategies.md). For example,  if the model implied $v_{t}$ is higher than the actual current $v_{t}$,  we would conclude that the [stock market](../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20III%20THE%20PLAYERS/Chapter%2012%20-%20Hedge%20Fund%20Strategies/Hedge%20Fund%20Strategies.md) is currently overvalued and hence currently not an attractive [investment](An%20Asset%20Allocation%20Primer.md) (and possibly even an opportunity to take a short position).

In the special case that expected log [dividend growth](../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%202%20-%20Spot%20Markets/Equity%20Commodity%20and%20Currency%20Math.md) is constant,  $\mathbb{E}_{t}\left[\Delta d_{t+j}\right]=g$ and investors price the [stock market](../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20III%20THE%20PLAYERS/Chapter%2012%20-%20Hedge%20Fund%20Strategies/Hedge%20Fund%20Strategies.md) with a constant required rate of expected (log) return of $\mathbb{E}_{t}\left[r_{t+j}\right]=\theta$,  the expression in (3.25) simplifies drastically to
$$

\begin{equation*}

v_{t}=\frac{1}{1-\rho}(c+g-\theta) . \tag{3.26}

\end{equation*}

$$

Compare this to the Gordon growth model in (3.13). It's very similar,  showing that it's the difference between expected growth and the required rate of [expected return](Lecture%201-%20Probability%20Distributions%20of%20Returns.md) that determines the level of the [price-dividend ratio](Lecture%204-%20Investor%20Sentiment.md).

Substituting in this result for $v_{t}$ and $v_{t+1}$ from (3.26) into (3.20),  and solving for expected log [returns](../Financial%20Markets/Financial%20Asset%20Pricing%20Theory%20Overview/Chapter%203%20-%20%20Assets,%20Portfolios,%20and%20Arbitrage/Assets.md),  we obtain
$$

\begin{equation*}

\mathbb{E}_{t}\left[r_{t+1}\right]=\theta \tag{3.27}

\end{equation*}

$$

which is exactly what it should be: The log return investors can expect to earn is the required rate of expected log return that they priced into the [stock market](../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20III%20THE%20PLAYERS/Chapter%2012%20-%20Hedge%20Fund%20Strategies/Hedge%20Fund%20Strategies.md) valuation.

<<<<<<< HEAD
## 3.4 A valuation model with [investor sentiment](Lecture%204-%20Investor%20Sentiment.md)
=======
## 3.4 A valuation model with [[Lecture 4- Investor Sentiment|investor sentiment]]
>>>>>>> d83d5c06204d625fbecfdb77e4d3f37c9c80e27b

Let's use this framework to understand how time-varying [Investor Sentiment](Lecture%204-%20[[Lecture%204-%20Investor%20Sentiment)|[investor sentiment](Lecture%204-%20Investor%20Sentiment.md)]] could affect prices,  how we could measure sentiment,  and how we could potentially exploit it in our [Asset Allocation](Lecture%202-%20[[Lecture%202-%20Asset%20Allocation%20with%20Multiple%20Risky%20Assets) with [Multiple Risky Assets](Lecture%202-%20Asset%20Allocation%20with%20Multiple%20Risky%20Assets.md)|[asset allocation](Lecture%202-%20Asset%20Allocation%20with%20Multiple%20Risky%20Assets.md)]] strategy. For the purpose of this exercise,  suppose that equation (3.26) represents how rational investors - who are not subject to sentiment fluctuationswould value the aggregate [stock market](../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20III%20THE%20PLAYERS/Chapter%2012%20-%20Hedge%20Fund%20Strategies/Hedge%20Fund%20Strategies.md). This means that these rational investors expect constant growth of dividends $g$ and they would require an [expected return](Lecture%201-%20Probability%20Distributions%20of%20Returns.md) of $\theta$ to hold the outstanding value of all stocks. Let's call the $v_{t}$ in (3.26) the (log) fundamental value.

In contrast,  suppose that actual investors are subject to influence of [Investor Sentiment](Lecture%204-%20[[Lecture%204-%20Investor%20Sentiment)|[investor sentiment](Lecture%204-%20Investor%20Sentiment.md)]]. For example,  they are sometimes more optimistic about [dividend growth](../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%202%20-%20Spot%20Markets/Equity%20Commodity%20and%20Currency%20Math.md) and sometimes more pessimistic. Their valuation of the aggregate [stock market](../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20III%20THE%20PLAYERS/Chapter%2012%20-%20Hedge%20Fund%20Strategies/Hedge%20Fund%20Strategies.md) is
$$

\begin{equation*}

v_{t}=\frac{1}{1-\rho}(c+g-\theta)+s_{t} \tag{3.28}

\end{equation*}

$$

where $s_{t}$ is the level of sentiment,  with $s_{t}>0$ reflecting excessive optimism and $s_{t}<0$ excessive pessimism.

Now imagine a rational investor looking at this market,  seeing $v_{t}$,  as determined by (3.28),  and wondering what rate of return to expect given that stock prices are subject to the influence of [Investor Sentiment](Lecture%204-%20[[Lecture%204-%20Investor%20Sentiment)|[investor sentiment](Lecture%204-%20Investor%20Sentiment.md)]]. We can answer this question by substituting $v_{t}$ and $v_{t+1}$ from (3.28) into (3.20). Lots of terms cancel,  and we are left with
$$

\begin{equation*}

\mathbb{E}_{t}\left[r_{t+1}\right]=\theta+\rho \mathbb{E}_{t}\left[s_{t+1}\right]-s_{t} \tag{3.29}

\end{equation*}

$$

Naturally,  if there was no sentiment effect on prices,  as in (3.27),  a rational investor could expect to earn $\theta$,  the rate of return that rational investors would price the market to earn

according to our assumption. But with sentiment,  there is an additional component that reflects that current high sentiment $\left(s_{t}\right)$ makes the market overpriced,  which is bad for next period [returns](../Financial%20Markets/Financial%20Asset%20Pricing%20Theory%20Overview/Chapter%203%20-%20%20Assets,%20Portfolios,%20and%20Arbitrage/Assets.md),  while high future sentiment ( $\rho \mathbb{E}_{t}\left[s_{t+1}\right]$ ) makes the market overpriced in the future,  which is good for next period [returns](../Financial%20Markets/Financial%20Asset%20Pricing%20Theory%20Overview/Chapter%203%20-%20%20Assets,%20Portfolios,%20and%20Arbitrage/Assets.md).

Also note that if sentiment and hence mispricing is constant,  $s_{t}=s$,  then this mispricing component becomes $\rho \mathbb{E}_{t}[s]-s$,  which is not zero,  so it still affects [returns](../Financial%20Markets/Financial%20Asset%20Pricing%20Theory%20Overview/Chapter%203%20-%20%20Assets,%20Portfolios,%20and%20Arbitrage/Assets.md) the rational investor can expect. For example,  with constant overpricing,  $s>0$,  we have $\mathbb{E}_{t}[s]-s<0$. This reflects the fact that with a constant level of overvaluation,  even though an investor does not have to suffer from collapses of overpricing in this case,  the investor is paying more for stocks than they are really worth,  given their [expected dividends](../Financial%20Markets/Financial%20Asset%20Pricing%20Theory%20Overview/Chapter%2012%20-%20Derivatives/Exercises.md),  which hurts [returns](../Financial%20Markets/Financial%20Asset%20Pricing%20Theory%20Overview/Chapter%203%20-%20%20Assets,%20Portfolios,%20and%20Arbitrage/Assets.md).

The relationship in (3.29) also tells us that if we could forecast $s_{t+1}$,  we could calculate expected [returns](../Financial%20Markets/Financial%20Asset%20Pricing%20Theory%20Overview/Chapter%203%20-%20%20Assets,%20Portfolios,%20and%20Arbitrage/Assets.md) and therefore forecast [returns](../Financial%20Markets/Financial%20Asset%20Pricing%20Theory%20Overview/Chapter%203%20-%20%20Assets,%20Portfolios,%20and%20Arbitrage/Assets.md). This means that to forecast [returns](../Financial%20Markets/Financial%20Asset%20Pricing%20Theory%20Overview/Chapter%203%20-%20%20Assets,%20Portfolios,%20and%20Arbitrage/Assets.md),  we need to have a model of the dynamics of [Investor Sentiment](Lecture%204-%20[[Lecture%204-%20Investor%20Sentiment)|[investor sentiment](Lecture%204-%20Investor%20Sentiment.md)]].

A reasonable starting point for such a model of sentiment could be that sentiment is positively correlated over time (so when sentiment is,  e.g.,  above average today,  it will tend to be above average next quarter) and mean-reverting (so when sentiment is,  e.g.,  above average today,  we expect it to be closer to the average level next quarter). This would mean that sentiment slowly cycles through periods of optimism and pessimism. We can capture these properties with a first-order [autoregressive process](../Financial%20Markets/Financial%20Asset%20Pricing%20Theory%20Overview/Chapter%202%20-%20Uncertainty,%20Information,%20and%20Stochastic%20Processes/Some%20Discrete-Time%20Stochastic%20Processes.md),  or $\operatorname{AR}(1)$ process:
$$

\begin{equation*}

s_{t+1}=\phi s_{t}+\eta_{t+1},      \quad \eta_{t+1} \sim \mathcal{N}\left(0,      \sigma_{s}^{2}\right) \tag{3.30}

\end{equation*}

$$

where $0<\phi<1$,  which makes sentiment mean-reverting. Thus,  every period,  sentiment is subject to an unpredictable shock $\eta_{t+1}$. In addition,  some of the previous period's sentiment carries over to the next period through the $\phi s_{t}$ term. In this model,
$$

\begin{equation*}

\mathbb{E}_{t}\left[s_{t+1}\right]=\phi s_{t} \tag{3.31}

\end{equation*}

$$

Therefore,  (3.29) becomes
$$

\begin{equation*}

\mathbb{E}_{t}\left[r_{t+1}\right]=\theta-(1-\rho \phi) s_{t} \tag{3.32}

\end{equation*}

$$

Note that $(1-\rho \phi)>0$. So,  expected [returns](../Financial%20Markets/Financial%20Asset%20Pricing%20Theory%20Overview/Chapter%203%20-%20%20Assets,%20Portfolios,%20and%20Arbitrage/Assets.md) are low when current sentiment is high,  for two reasons. First,  as we discussed earlier,  even constant high sentiment would mean low expected [returns](../Financial%20Markets/Financial%20Asset%20Pricing%20Theory%20Overview/Chapter%203%20-%20%20Assets,%20Portfolios,%20and%20Arbitrage/Assets.md) because price is high relative to the expected stream of dividends. Second,  in addition,  expected [returns](../Financial%20Markets/Financial%20Asset%20Pricing%20Theory%20Overview/Chapter%203%20-%20%20Assets,%20Portfolios,%20and%20Arbitrage/Assets.md) are low because prices are expected to depreciate. Sentiment is mean-reverting $(\phi<1)$,  so if it's high today,  it's likely to be lower next period. So when sentiment is high today,  we can forecast that sentiment will likely go down in the future. Following (3.28),  stock prices will go down along with sentiment.

When we have a relationship between rationally expected [returns](../Financial%20Markets/Financial%20Asset%20Pricing%20Theory%20Overview/Chapter%203%20-%20%20Assets,%20Portfolios,%20and%20Arbitrage/Assets.md) and time-varying variable like $s_{t}$,  we say that there is return predictability.

Yet,  to empirically use (3.32),  we need to measure $s_{t}$. How can we measure it? We'll discuss some empirical proxies for [Investor Sentiment](Lecture%204-%20[[Lecture%204-%20Investor%20Sentiment)|[investor sentiment](Lecture%204-%20Investor%20Sentiment.md)]] in the next lecture. But for now let's look at an indirect way of getting at it. Go back to (3.28) and solve for $s_{t}$ :
$$

\begin{equation*}

s_{t}=v_{t}-\frac{1}{1-\rho}(c+g-\theta) \tag{3.33}

\end{equation*}

$$

Now plug this into (3.32). The result is
$$

\begin{equation*}

\mathbb{E}_{t}\left[r_{t+1}\right]=\text { const. }-(1-\rho \phi) v_{t} \tag{3.34}

\end{equation*}

$$

where I collected all the constants in the first term. So the log [price-dividend ratio](Lecture%204-%20Investor%20Sentiment.md),  which we can directly observe,  should capture the time-variation in expected [returns](../Financial%20Markets/Financial%20Asset%20Pricing%20Theory%20Overview/Chapter%203%20-%20%20Assets,%20Portfolios,%20and%20Arbitrage/Assets.md) induced by [Investor Sentiment](Lecture%204-%20[[Lecture%204-%20Investor%20Sentiment)|[investor sentiment](Lecture%204-%20Investor%20Sentiment.md)]]. If investors were rational,  under the assumptions we made,  the [price-dividend ratio](Lecture%204-%20Investor%20Sentiment.md) would not vary. So to the extent it varies,  it varies with the [Investor Sentiment](Lecture%204-%20[[Lecture%204-%20Investor%20Sentiment)|[investor sentiment](Lecture%204-%20Investor%20Sentiment.md)]] level $s_{t}$. This is why the [price-dividend ratio](Lecture%204-%20Investor%20Sentiment.md) predicts [returns](../Financial%20Markets/Financial%20Asset%20Pricing%20Theory%20Overview/Chapter%203%20-%20%20Assets,%20Portfolios,%20and%20Arbitrage/Assets.md). Times of high price-dividend ratios,  for example,  are times when a rational investor in this model should expect low future [returns](../Financial%20Markets/Financial%20Asset%20Pricing%20Theory%20Overview/Chapter%203%20-%20%20Assets,%20Portfolios,%20and%20Arbitrage/Assets.md).

In practice,  there can be a distortion that can prevent the price-divided ratio from accurately capturing the sentiment level. If rationally expected [dividend growth](../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%202%20-%20Spot%20Markets/Equity%20Commodity%20and%20Currency%20Math.md) rates are not constant but time-varying,  this would introduce rational reasons for why the pricedividend ratio should vary. If so,  then not all variation in $v_{t}$ in our sentiment valuation model (3.28) is due to variation in $s_{t}$. Some of the variation would be due to timevarying $g$. Then the [price-dividend ratio](Lecture%204-%20Investor%20Sentiment.md) may be high not because the market is currently overpriced due to positive sentiment,  but rather because because high rationally expected growth of dividends justifies high a current price relative to current dividends. This makes $v_{t}$ a less reliable predictor of future [returns](../Financial%20Markets/Financial%20Asset%20Pricing%20Theory%20Overview/Chapter%203%20-%20%20Assets,%20Portfolios,%20and%20Arbitrage/Assets.md).

It is also possible that the risk premium that rational investors demand,  and that we have assumed to be constant at $\theta$ in (3.28),  may in fact be time-varying. Then the [price-dividend ratio](Lecture%204-%20Investor%20Sentiment.md) may be high because investors require a low risk premium. Then future [returns](../Financial%20Markets/Financial%20Asset%20Pricing%20Theory%20Overview/Chapter%203%20-%20%20Assets,%20Portfolios,%20and%20Arbitrage/Assets.md) will be low because a [stock market](../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20III%20THE%20PLAYERS/Chapter%2012%20-%20Hedge%20Fund%20Strategies/Hedge%20Fund%20Strategies.md) [investment](An%20Asset%20Allocation%20Primer.md) will earn only this low risk premium. So this is just like the sentiment effect that we discussed in the sense that a high current [price-dividend ratio](Lecture%204-%20Investor%20Sentiment.md) forecasts low future [returns](../Financial%20Markets/Financial%20Asset%20Pricing%20Theory%20Overview/Chapter%203%20-%20%20Assets,%20Portfolios,%20and%20Arbitrage/Assets.md). So for now we just include time-varying risk aversion as one potential manifestation of sentiment. We can just include the time-varying part of $\theta$ in $s_{t}$.

### 3.5 Macro vs. micro market inefficiency

At this point,  it's useful to reflect a bit on the possibility that sentiment of not-sorational investors could have some impact on the [stock market](../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20III%20THE%20PLAYERS/Chapter%2012%20-%20Hedge%20Fund%20Strategies/Hedge%20Fund%20Strategies.md) valuation overall. If such sentiment reflects excessive optimism or pessimism about [future cash flows](../Financial%20Engineering/Advanced%20Derivatives%20Pricing%20Methodology.md) and affects prices,  then there is a [market inefficiency](../Course%20Notes/Quantitative%20Trading%20Strategies%20Lecture%20Notes.md). In an [efficient market](../Financial%20Markets/Financial%20Trading%20and%20Markets/Chapter%2012%20Market%20Efficiency.md),  prices are supposed to reflect a rational assessment of the information available at a point in time,  not sentiment disconnected from [fundamentals](../Advanced%20Financial%20Analysis%20and%20Valuation/Lecture%20Notes%20Advanced%20Financial%20Analysis%20and%20Valuation/Week%202/Week%202%20Fundamentals%20Of%20Forecasting.md).

A common argument in modern finance against existence of such market inefficiencies is that "smart money,  " i.e.,  highly sophisticated professional investors,  would take advantage of such market inefficiencies by trading against them and thereby eliminating them. But how strong is this force against market inefficiencies? This depends on the level of aggregation that we are interested in (e.g.,  individual stock level or at an aggregate level,  say the market [portfolio](An%20Asset%20Allocation%20Primer.md)) and the nature of the [riskiness](../Financial%20Instruments/Financial%20Derivatives%20and%20Quantitative%20Methods/Risk%20Preferences.md) of the assets involved.

Consider first individual stocks. Suppose there are lots of idiosyncratic mispricings. Idiosyncratic here means that whether a stock is overor undervalued is totally random and not systematically related to,  say,  firms' industry,  their size,  or other common attributes that firms may have. In this case,  a hedge fund can run a "pairs trading" strategy,  taking long positions in undervalued stocks and pairing each [long position](../Financial%20Engineering/Derivatives/Part%20I%20-%20Forwards%20and%20Futures/Chapter%204%20-%20Futures:%20Hedging%20and%20Speculation.md) with a short position in an overvalued stock that has highly correlated [returns](../Financial%20Markets/Financial%20Asset%20Pricing%20Theory%20Overview/Chapter%203%20-%20%20Assets,%20Portfolios,%20and%20Arbitrage/Assets.md) because it's in the same industry,  has the same size,  etc. The high correlation ensures that the pair long-short position has relatively little risk because the short position to a large extent hedges the risk of the [long position](../Financial%20Engineering/Derivatives/Part%20I%20-%20Forwards%20and%20Futures/Chapter%204%20-%20Futures:%20Hedging%20and%20Speculation.md). Moreover,  putting lots of such pairs together into a [portfolio](An%20Asset%20Allocation%20Primer.md) results in a lot of the remaining risk being diversified away. As a consequence,  very little risk is left in this [portfolio](An%20Asset%20Allocation%20Primer.md). Hence,  if these kinds of market inefficiencies existed,  it would be an extremely attractive opportunity that [hedge funds](../Financial%20Engineering/Basis%20Trade%20Explainer.md) or other smart-money investors would aggressively exploit and thereby largely eliminate. For exactly that reason,  these sorts of inefficiencies are unlikely to be big.

Now consider the [stock market](../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20III%20THE%20PLAYERS/Chapter%2012%20-%20Hedge%20Fund%20Strategies/Hedge%20Fund%20Strategies.md) as a whole. Suppose,  for instance,  that the [stock market](../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20III%20THE%20PLAYERS/Chapter%2012%20-%20Hedge%20Fund%20Strategies/Hedge%20Fund%20Strategies.md) [portfolio](An%20Asset%20Allocation%20Primer.md) as a whole is overvalued by $50/% and smart-money investors know about this overvaluation (without any uncertainty about the degree of misvaluation). Unfortunately for them,  there is no way to construct a low-risk,  high-return trade that exploits this misvaluation. Unlike in the pairs trading example,  there is no other asset class out there that has a return that is highly correlated with the [stock market](../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20III%20THE%20PLAYERS/Chapter%2012%20-%20Hedge%20Fund%20Strategies/Hedge%20Fund%20Strategies.md). In other words,  one cannot really hedge the risk of a short position in the overvalued [stock market](../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20III%20THE%20PLAYERS/Chapter%2012%20-%20Hedge%20Fund%20Strategies/Hedge%20Fund%20Strategies.md) with a [long position](../Financial%20Engineering/Derivatives/Part%20I%20-%20Forwards%20and%20Futures/Chapter%204%20-%20Futures:%20Hedging%20and%20Speculation.md) in some other asset class. As a consequence,  taking a bet agains [stock market](../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20III%20THE%20PLAYERS/Chapter%2012%20-%20Hedge%20Fund%20Strategies/Hedge%20Fund%20Strategies.md) overor undervaluation is necessarily risky. Recall that a typical

one-standard deviation move in the [stock market](../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20III%20THE%20PLAYERS/Chapter%2012%20-%20Hedge%20Fund%20Strategies/Hedge%20Fund%20Strategies.md) in a single year is a $20/% return. So if an investor stays out of the market due to concerns about overvaluation,    this investor takes a substantial risk that they could experience a performance shortfall of $20/% or more relative to a broad [stock index](../Financial%20Instruments/Lecture%20Notes-%20Financial%20Instruments/Teaching%20Note%201-%20Forward%20Rates%20Agreement/Hedging%20Strategies%20with%20Forwards.md). For an investor who responded to overvaluation by taking short position in the [stock market](../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20III%20THE%20PLAYERS/Chapter%2012%20-%20Hedge%20Fund%20Strategies/Hedge%20Fund%20Strategies.md),  the performance shortfall in this case would be even bigger.

Moreover,  even if smart-money investors are correct in their judgment that the [stock market](../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20III%20THE%20PLAYERS/Chapter%2012%20-%20Hedge%20Fund%20Strategies/Hedge%20Fund%20Strategies.md) is misvalued,  it could take years until the misvaluation is corrected. And since betting against the entire [stock market](../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20III%20THE%20PLAYERS/Chapter%2012%20-%20Hedge%20Fund%20Strategies/Hedge%20Fund%20Strategies.md) is very risky,  substantial losses can pile up until the position finally pays off. This means smart-money investors may have to write many quarterly letters to their outside investors pleading with them to be patient and arguing that their position will win in the long run. Yet,  outside investors are rarely patient enough to see this through. As [the economist](../Financial%20Markets%20and%20Institutions/III.%20Liquidity%20of%20Assets/Class%209-%20Bailouts%20and%20Bank%20Failures/Articles/The%20Economist%20Fewer%20Or%20Even%20None.md) John Maynard Keynes,  who,  was also an active speculator in markets,  once remarked: "Markets can stay irrational longer than you can stay solvent."

One well-known example is the famous value investor Julian Robertson of Tiger Management during the technology stock bubble during the late 1990s. Tech stock prices were going through the roof in 1999,  before crashing sharply in March 2000. In mid-1999,  tech stocks seemed extremely overvalued. Julian Robertson decided to exit long positions in tech stocks and to bet against further price rises of tech stocks. Unfortunately for him,  prices kept rising at a fast pace. His funds started to suffer outflows. In October 1999,  Tiger Management increased the redemption period for investors from 3 to 6 months in to curb outflows. But nevertheless,  in the last quarter of 1999,  their funds lost about $25/% of its assets through withdrawals. In March 2000,  Robertson threw in the towel and announced the liquidation of his funds,  just a few days before the start of the technology stock crash.

Figure 3.5 shows the monthly flows of the Jaguar fund,  one of the funds managed by Tiger Management,  and compares with the the flows of the Quantum fund,  managed by George Soros. Soros took a very different approach. He tried to "ride the bubble" until the end,  with long positions in tech stocks until March 2000. At the start of the crash,  he quickly reduced these positions. His performance in late 1999 and early 2000 therefore was much better than Julian Robertson's. As the figure shows,  this made a dramatic difference to the timing of flows. The Jaguar fund had strong outflows in the second half of 1999 before being closed down in the first quarter of 2000. The Quantum fund also suffered outflows once its long positions got hit by the crash in March 2000. But due to the prior inflows as well as the large gains it had achieved on its long positions,  the Quantum fund was able to weather those outflows. After the Quantum fund exited tech stock positions quickly in the wake of the crash,  outflows stopped a couple of months

 ![500](https://cdn.mathpix.com/cropped/2024_10_19_48a1c4654e845915c45cg-089.jpg?height=616&width=1109&top_left_y=321&top_left_x=519)

Figure 3.5: Fund flows of Jaguar fund and Quantum fund

Source: Brunnermeier,  M. and Nagel,  S.,  2004. [Hedge funds](../Financial%20Engineering/Basis%20Trade%20Explainer.md) and the technology bubble. Journal of Finance,  59(5),  pp0.\1-2040. The peak of technology stock prices was in mid-March 2000.

later.

The [bottom line](../Advanced%20Financial%20Analysis%20and%20Valuation/Financial%20Ratios/Operating%20Income%20vs.%20Net%20Income%20What's%20the%20Difference.md) of all this is that betting against misvaluation of the entire market,  or large sectors of the market,  is very risky. And it's not even clear that betting early on against misvaluation is necessarily the best strategy for a smart-money investor. Temporarily riding a bubble of inflating misvaluation of the [stock market](../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20III%20THE%20PLAYERS/Chapter%2012%20-%20Hedge%20Fund%20Strategies/Hedge%20Fund%20Strategies.md),  like George Soros seems to have done,  may be preferable. In the short run,  therefore,  smart money investors may even further amplify misvaluation.

Overall,  it's quite implausible that smart money would lean aggressively against misvaluation at the aggregate [stock market](../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20III%20THE%20PLAYERS/Chapter%2012%20-%20Hedge%20Fund%20Strategies/Hedge%20Fund%20Strategies.md) level.

Another argument that is often made is that professional investors manage most of the money invested in the [stock market](../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20III%20THE%20PLAYERS/Chapter%2012%20-%20Hedge%20Fund%20Strategies/Hedge%20Fund%20Strategies.md) and so it must be professionals,  not the likely less sophisticated individual investors that effectively determine [pricing](../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%207/Arbitrage%20Pricing%20of%20Derivatives.md) in the [stock market](../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20III%20THE%20PLAYERS/Chapter%2012%20-%20Hedge%20Fund%20Strategies/Hedge%20Fund%20Strategies.md). However,  according to the U.S. Financial Accounts,  at the end of 2021,  individual investors held about $37/% of total stock market capitalization directly,    and an additional roughly $25/% indirectly through mutual funds,  ETFs,  and direct-contribution retirement products. This means that a substantial share of equity investments is directly or indirectly controlled by individual investors. The [investment](An%20Asset%20Allocation%20Primer.md) products that individual investors purchase in the mutual funds and ETF space are often quite narrowly defined (e.g.,  a stock fund,  a bond fund,  or a stock fund focused on a specific sector,  etc.). By

allocating money to these products,  it is the individual investors who are effectively making the allocation decision at the asset-class level,  not the professional managers running these funds. Professionals,  or the computer algorithms they use,  then decide on how the allocated flows are invested in individual securities within the asset class,  but the asset-class level allocation decision is left to individuals.

In contrast,  at the individual stock level,  most of the funds products that individual investors hold leave it to professional [investment](An%20Asset%20Allocation%20Primer.md) managers to choose the individual securities within asset class buckets. So we should expect individual investors to have much less influence on the relative [pricing](../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%207/Arbitrage%20Pricing%20of%20Derivatives.md) of individual securities within asset classes.

In summary,  at the macro level,  for asset classes,  [investment](An%20Asset%20Allocation%20Primer.md) flows are more likely to be driven by sentiment-prone retail investors than at the individual security level. These asset-class level flows are also more difficult to counteract for smart money investors because doing so is risky. The conclusion from all this is that we should not expect that smart money investors exert a strong influence to keep markets efficient at the macro level. Markets are likely to be quite efficient at the micro level,  but inefficiencies are more likely at the macro level.

Our next step will be to look into getting estimates of the [returns](../Financial%20Markets/Financial%20Asset%20Pricing%20Theory%20Overview/Chapter%203%20-%20%20Assets,%20Portfolios,%20and%20Arbitrage/Assets.md) we can expect from a [stock market](../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20III%20THE%20PLAYERS/Chapter%2012%20-%20Hedge%20Fund%20Strategies/Hedge%20Fund%20Strategies.md) in the presence of misvaluation. We do this first by looking at simulations of the model from above,  then we'll look at actual data.

### 3.6 Return prediction regressions: Simulations

Recall from earlier that our valuation model with sentiment had the following equation for the $\log$ [price-dividend ratio](Lecture%204-%20Investor%20Sentiment.md):
$$

\begin{equation*}

v_{t}=\frac{1}{1-\rho}(c+g-\theta)+s_{t} \tag{3.35}

\end{equation*}

$$

The fundamental value component of the log price-dividend price ratio is obtained as $v_{t}-s_{t}$. We then get the level of the fundamental value,  $F_{t}$,  by adding the log dividend and then exponentiating
$$

\begin{equation*}

F_{t}=\exp \left(v_{t}-s_{t}+d_{t}\right) \tag{3.36}

\end{equation*}

$$

The price level is
$$

\begin{equation*}

P_{t}=\exp \left(v_{t}+d_{t}\right) \tag{3.37}

\end{equation*}

$$

I simulate unexpected changes log dividends as a normal random variables,
$$

\begin{equation*}

d_{t+1}-d_{t}=g+\varepsilon_{t+1},      \quad \varepsilon_{t+1} \sim \mathcal{N}\left(0,      \sigma_{d}^{2}\right) \tag{3.38}

\end{equation*}

$$

and the level of sentiment as in (3.30),
$$

\begin{equation*}

s_{t+1}=\phi s_{t}+\eta_{t+1},      \quad \eta_{t+1} \sim \mathcal{N}\left(0,      \sigma_{s}^{2}\right) \tag{3.39}

\end{equation*}

$$

i.e.,  also with normally distributed shocks. Based on the simulated $d_{t}$ and $s_{t}$ series,  I then calculate series of first $v_{t}$,  and then $F_{t}$ and $P_{t}$ using the above formulas. Finally,  I get a series of realized log [returns](../Financial%20Markets/Financial%20Asset%20Pricing%20Theory%20Overview/Chapter%203%20-%20%20Assets,%20Portfolios,%20and%20Arbitrage/Assets.md) by solving (3.18) for $r_{t+1}$,  which yields
$$

\begin{equation*}

r_{t+1}=c+\Delta d_{t+1}+\rho v_{t+1}-v_{t} \tag{3.40}

\end{equation*}

$$

Plugging the simulated $d_{t},      v_{t}$ series into this formula then yields the simulated log [returns](../Financial%20Markets/Financial%20Asset%20Pricing%20Theory%20Overview/Chapter%203%20-%20%20Assets,%20Portfolios,%20and%20Arbitrage/Assets.md) series.

I pick parameters that make the series have properties close to the actual [stock market](../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20III%20THE%20PLAYERS/Chapter%2012%20-%20Hedge%20Fund%20Strategies/Hedge%20Fund%20Strategies.md) index return and [price-dividend ratio](Lecture%204-%20Investor%20Sentiment.md) series at a quarterly frequency: $\rho=0.99$ (the parameter in the log-linearization that is very close to one),  $g=0.01$ (expected log [dividend growth](../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%202%20-%20Spot%20Markets/Equity%20Commodity%20and%20Currency%20Math.md)); $\theta=0.02$ (unconditional expected log return). I set the volatility of dividend shocks to $\sigma_{d}=0.07$.

A key question we should look into is how the persistence of sentiment affects the nature of mispricing and the return predictability that follows from it. For this reason,  I will show results for several different values of $\phi$ in (3.39). For each value of $\phi$,  I look for a value of the sentiment shocks $\sigma_{s}$ that makes the standard deviation of $s_{t}$ equal to 0.20 . In other words,  I want to see the effects of changing persistence of sentiment without changing the typical magnitudes of sentiment-induced misvaluation.

Figure 3.6 shows simulated price paths of $F_{t}$ and $P_{t}$ for total length of 400 quarters and for two different values of $\phi: \phi=0.15$ in the top panel and $\phi=0.95$ in the bottom panel. In both cases,  there is a substantial degree of misvaluation due to the time-varying [Investor Sentiment](Lecture%204-%20[[Lecture%204-%20Investor%20Sentiment)|[investor sentiment](Lecture%204-%20Investor%20Sentiment.md)]],  often exceeding $+30/% or $-30/% of the fundamental value. But which value of $\phi$ we pick makes a big difference for how fast misvaluation corrects. In the top panel,  if [Investor Sentiment](Lecture%204-%20[[Lecture%204-%20Investor%20Sentiment)|[investor sentiment](Lecture%204-%20Investor%20Sentiment.md)]] is not very persistent,  mispricing corrects very quickly and so we get relatively high-frequency variation of the price around fundamental value. In contrast,  with $\phi=0.95$ in the bottom panel,  [Investor Sentiment](Lecture%204-%20[[Lecture%204-%20Investor%20Sentiment)|[investor sentiment](Lecture%204-%20Investor%20Sentiment.md)]] is highly persistent and we get long-lasting cycles of misvaluation.

Which of the two cases would make it easier for a smart investor to profit from misvaluation? Clearly the first case. In this case,  if the investor recognizes at a certain point in time that there is big misvaluation,  then,  because sentiment has low persistence,  it's very likely that this misvaluation will correct soon. A bet against misvaluation is therefore likely to pay off soon. In contrast,  in the high-persistence case in the bottom panel,  an investor could correctly diagnose that there is,  say,  undervaluation (such as around quarter 245 in the plot) but then it can take another 5 to 10 years until the

 ![500](https://cdn.mathpix.com/cropped/2024_10_19_48a1c4654e845915c45cg-092.jpg?height=1671&width=963&top_left_y=425&top_left_x=538)

Figure 3.6: Simulated paths of prices and fundamental value for different values of $\phi$

misvaluation finally gets corrected and the bet against the mispricing eventually pays off.

We can see this more clearly if we look at the scatter plots of log [returns](../Financial%20Markets/Financial%20Asset%20Pricing%20Theory%20Overview/Chapter%203%20-%20%20Assets,%20Portfolios,%20and%20Arbitrage/Assets.md) in period $t+1$,  i.e.,  $r_{t+1}$,  on $\log$ sentiment in the previous period,  $s_{t}$,  shown in Figure 3.7 for these two 400-quarter simulation runs. These scatter plots show us how informative $s_{t}$ is about the return in the next quarter.

As the top panel shows,  with low persistence,  there is a clearly visible negative relationship between sentiment and next-quarter [returns](../Financial%20Markets/Financial%20Asset%20Pricing%20Theory%20Overview/Chapter%203%20-%20%20Assets,%20Portfolios,%20and%20Arbitrage/Assets.md): high sentiment strongly forecasts low future [returns](../Financial%20Markets/Financial%20Asset%20Pricing%20Theory%20Overview/Chapter%203%20-%20%20Assets,%20Portfolios,%20and%20Arbitrage/Assets.md). This reflects the relatively quick correction of mispricing in the low-persistence case.

In contrast,  the bottom panel shows that when persistence is high,  there is at best a very weak relation between sentiment and next-quarter [returns](../Financial%20Markets/Financial%20Asset%20Pricing%20Theory%20Overview/Chapter%203%20-%20%20Assets,%20Portfolios,%20and%20Arbitrage/Assets.md). So,  even if we perfectly know the level of mispricing at $t$,  it's still very difficult to predict what [returns](../Financial%20Markets/Financial%20Asset%20Pricing%20Theory%20Overview/Chapter%203%20-%20%20Assets,%20Portfolios,%20and%20Arbitrage/Assets.md) will be next quarter! And remember that typical magnitudes of mispricing in the simulations in both panels are the same. The only difference is that mispricing in the top panel is meanreverting quickly,  while it can be very long-lasting in the bottom panel. Long-lasting mispricing is difficult to exploit,  even if it's big!

Let's explore this more through the lens of a statistical model that an investor could then use to get estimates of conditional expected [returns](../Financial%20Markets/Financial%20Asset%20Pricing%20Theory%20Overview/Chapter%203%20-%20%20Assets,%20Portfolios,%20and%20Arbitrage/Assets.md) (which the investor could then fit into a [portfolio optimization](../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20III%20THE%20PLAYERS/Chapter%2011%20-%20Individual%20Investors-A%20Survey%20of%20Modern%20Investment%20Theory/The%20Modern%20Portfolio%20Theory%20and%20the%20Capm.md) model). Let's run a regression of log [returns](../Financial%20Markets/Financial%20Asset%20Pricing%20Theory%20Overview/Chapter%203%20-%20%20Assets,%20Portfolios,%20and%20Arbitrage/Assets.md) on lagged log sentiment:
$$

r_{t+1}=a+b s_{t}+e_{t+1}

$$

Basically,  we are fitting a straight line with slope $b$ and intercept $a$ through the scatter plots we just looked at. Once we have an estimate of the [regression coefficients](../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%209/A%20Practical%20Estimation%20Method.md) $a,      b$-let's label them $\hat{a},      \hat{b}$-we can form an estimate of the conditional expected next-quarter log return as $\hat{a}+\hat{b} s_{t}$.

Table 3.1: Predictive regressions of one-quarter-ahead log [returns](../Financial%20Markets/Financial%20Asset%20Pricing%20Theory%20Overview/Chapter%203%20-%20%20Assets,%20Portfolios,%20and%20Arbitrage/Assets.md) on the log sentiment level $s_{t}$
![400](CleanShot%202024-10-24%20-003109@2x.png)

To see what such a regression delivers on average (or said differently,  in expectation),  I now generate 1,  000 simulated series of [returns](../Financial%20Markets/Financial%20Asset%20Pricing%20Theory%20Overview/Chapter%203%20-%20%20Assets,%20Portfolios,%20and%20Arbitrage/Assets.md) and sentiment,  each with length 400 quarters. I run the regression above on each of these simulated 400-quarter series. So for each simulated series,  I get one set of estimates $\hat{a},      \hat{b}$. Table 3.1 shows average $\hat{b}$ across

 ![500](https://cdn.mathpix.com/cropped/2024_10_19_48a1c4654e845915c45cg-094.jpg?height=1681&width=963&top_left_y=420&top_left_x=540)

Figure 3.7: One period ahead $\log$ [returns](../Financial%20Markets/Financial%20Asset%20Pricing%20Theory%20Overview/Chapter%203%20-%20%20Assets,%20Portfolios,%20and%20Arbitrage/Assets.md),  $r_{t+1}$ and $\log$ sentiment,  $s_{t}$

 ![500](https://cdn.mathpix.com/cropped/2024_10_19_48a1c4654e845915c45cg-095.jpg?height=781&width=965&top_left_y=352&top_left_x=599)

Figure 3.8: Distribution of estimated slope coefficient in return-prediction regression (each simulation run has 400 quarters of data)

the 1,  000 simulations. I also calculate the average $R^{2}$,  which shows how much of the variance of $r_{t+1}$ is explained by the predictable component $b s_{t}$.

In line with the intuition from the scatter plots. When $\phi$ is low,  there is a strong negative relationship between $r_{t+1}$ and $s_{t}$ as shown by the large negative average slope coefficient of -0.85 and the high $R^{2}$ of $40/%. The high $R^{2}$ basically says the same thing as our visual impression from the scatter plot for $\phi=0.15$ where we can see the negative relationship just by eyeballing the scatter plot.

In contrast,  when $\phi=0.95$,  the average slope coefficient is much,  much smaller $(-0.07)$ and the $R^{2}$ is much lower $(2 %)$. Again,  this lines up well with what we concluded from the scatter plot: if there is any predictive relationship,  it must be weak,  because we can't really see it in the scatter plot.

In this high persistence case,  $\phi=0.95$,  how difficult is it,  statistically,  to pin down the slope coefficient? We can get an idea by looking at the different estimates $\hat{b}$ we get across the 1,  000 simulation runs. Figure 3.8 presents a histogram. The variation in $\hat{b}$ across the different simulation runs is substantial! It is not all that unlikely that an estimates ends up quite close to zero-which looks like [returns](../Financial%20Markets/Financial%20Asset%20Pricing%20Theory%20Overview/Chapter%203%20-%20%20Assets,%20Portfolios,%20and%20Arbitrage/Assets.md) are only very weakly predictable,  even though the magnitudes of mispricing are substantial.

Moreover,  we get this result that the slope $b$ is difficult to estimate precisely even though we are looking at really long samples here in these simulation runs. In practice,  the sample length of 400 quarters we are using here would be unusually long. And it's not only 400 quarters long here,  but we also know for sure that the underlying process of sentiment and [dividend growth](../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%202%20-%20Spot%20Markets/Equity%20Commodity%20and%20Currency%20Math.md),  and their parameters,  are not changing over time. In practice,  using a 400-quarter sample of data to estimate these sorts of predictive relationship runs into questions whether the predictive relationship we are trying to uncover could really be stable over such a long period of time. So,  in practice we would be even less certain about the predictive relationship between measures of misvaluation and future return.

All this shows how exceedingly difficult market timing can be,  even if the [stock market](../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20III%20THE%20PLAYERS/Chapter%2012%20-%20Hedge%20Fund%20Strategies/Hedge%20Fund%20Strategies.md) goes through cycles of large misvaluations that we can perfectly measure!

And we haven't even gotten to the main difficulty,  which is that a real-world investor must predict out-of-sample. Here we have only examined in-sample regressions. For example,  an investor living in our simulations and trying to make an [investment decision](../Financial%20Markets/Financial%20Trading%20and%20Markets/Chapter%201%20Introduction%20to%20Securities%20Trading%20and%20Markets.md) at,  say,  quarter 200 does not yet have the benefit of knowing the coefficient estimates of a regression run with data all the way until quarter 400. The investor would only be able to use data up to quarter 200 to inform themselves about the predictive relationship. But before we get to this problem of out-of-sample prediction,  let's first look at actual data on [returns](../Financial%20Markets/Financial%20Asset%20Pricing%20Theory%20Overview/Chapter%203%20-%20%20Assets,%20Portfolios,%20and%20Arbitrage/Assets.md) and price-dividend ratios to see whether any of the cases for different $\phi$ that we considered so far could be a good approximation to reality.

### 3.7 Predictive regressions in actual data

Table 4.2,  Panel A,  shows the results from a regression of log [returns](../Financial%20Markets/Financial%20Asset%20Pricing%20Theory%20Overview/Chapter%203%20-%20%20Assets,%20Portfolios,%20and%20Arbitrage/Assets.md) on the lagged log [price-dividend ratio](Lecture%204-%20Investor%20Sentiment.md) $v_{t}$,  i.e.,  the regression
$$

r_{t+1}=a+b v_{t}+\varepsilon_{t+1}

$$

The dependent variable are quarterly log [returns](../Financial%20Markets/Financial%20Asset%20Pricing%20Theory%20Overview/Chapter%203%20-%20%20Assets,%20Portfolios,%20and%20Arbitrage/Assets.md) on the CRSP value-weighted index from 1927Q2 to 2022Q4; the predictor variable is the $\log \mathrm{P} / \mathrm{D}$ ratio of this index from end of quarter 1927Q1 to end of quarter 2022Q3. Each quarter $t$,  I compute the P/D ratio as the total aggregate [market capitalization](../Advanced%20Financial%20Analysis%20and%20Valuation/Financial%20Ratios/Price-to-Sales%20Ratios%20in%20Stock%20Valuation.md) of all stocks in the index dividend by the sum of dividends of all stocks in the index during the quarters $t-3$ to $t$.

As Panel A shows,  the results are quite weak. The sign of the coefficient is as expected from our simulations earlier. A high [price-dividend ratio](Lecture%204-%20Investor%20Sentiment.md) forecasts low future [returns](../Financial%20Markets/Financial%20Asset%20Pricing%20Theory%20Overview/Chapter%203%20-%20%20Assets,%20Portfolios,%20and%20Arbitrage/Assets.md). However,  the $t$-statistic of the slope coefficient of -1.776 does not exceed conventional

Table 3.2: Predictive regressions of one-quarter-ahead [returns](../Financial%20Markets/Financial%20Asset%20Pricing%20Theory%20Overview/Chapter%203%20-%20%20Assets,%20Portfolios,%20and%20Arbitrage/Assets.md) on the lagged log pricedividend ratio,  1927-2022

![300](CleanShot%202024-10-24%20-003110@2x.png)

thresholds for statistical significance at a $5/% confidence level (this threshold is at -1.96). And the $R^{2}$ of $0.6/% tells us that the $\log \mathrm{P} / \mathrm{D}$ ratio explains very little of the variation of future [returns](../Financial%20Markets/Financial%20Asset%20Pricing%20Theory%20Overview/Chapter%203%20-%20%20Assets,%20Portfolios,%20and%20Arbitrage/Assets.md).

While the present-value identity framework based on log-linear approximation that we used in this lecture relates the $\log \mathrm{P} / \mathrm{D}$ ratio to future $\log$ [returns](../Financial%20Markets/Financial%20Asset%20Pricing%20Theory%20Overview/Chapter%203%20-%20%20Assets,%20Portfolios,%20and%20Arbitrage/Assets.md) and future $\log$ [dividend growth](../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%202%20-%20Spot%20Markets/Equity%20Commodity%20and%20Currency%20Math.md),  for the purpose of choosing an [Asset Allocation](Lecture%202-%20[[Lecture%202-%20Asset%20Allocation%20with%20Multiple%20Risky%20Assets) with [Multiple Risky Assets](Lecture%202-%20Asset%20Allocation%20with%20Multiple%20Risky%20Assets.md)|[asset allocation](Lecture%202-%20Asset%20Allocation%20with%20Multiple%20Risky%20Assets.md)]] we are actually not really interested directly in expected log [returns](../Financial%20Markets/Financial%20Asset%20Pricing%20Theory%20Overview/Chapter%203%20-%20%20Assets,%20Portfolios,%20and%20Arbitrage/Assets.md). Instead,  we want to know expected simple [returns](../Financial%20Markets/Financial%20Asset%20Pricing%20Theory%20Overview/Chapter%203%20-%20%20Assets,%20Portfolios,%20and%20Arbitrage/Assets.md). Yet,  a regression with log [returns](../Financial%20Markets/Financial%20Asset%20Pricing%20Theory%20Overview/Chapter%203%20-%20%20Assets,%20Portfolios,%20and%20Arbitrage/Assets.md) as dependent variable gives us forecasts of log [returns](../Financial%20Markets/Financial%20Asset%20Pricing%20Theory%20Overview/Chapter%203%20-%20%20Assets,%20Portfolios,%20and%20Arbitrage/Assets.md),  not forecasts of simple [returns](../Financial%20Markets/Financial%20Asset%20Pricing%20Theory%20Overview/Chapter%203%20-%20%20Assets,%20Portfolios,%20and%20Arbitrage/Assets.md). To illustrate what difference this makes,  recall from (3.10) that if [returns](../Financial%20Markets/Financial%20Asset%20Pricing%20Theory%20Overview/Chapter%203%20-%20%20Assets,%20Portfolios,%20and%20Arbitrage/Assets.md) are conditionally log normal,  the conditional expected simple return return relates to the conditional expected log return as follows:
$$

\begin{equation*}

\mathbb{E}_{t} R_{t+1} \approx \mathbb{E}_{t} r_{t+1}+\frac{1}{2} \operatorname{var}_{t}\left(r_{t+1}\right) \tag{3.41}

\end{equation*}

$$

If $\operatorname{var}_{t}\left(r_{t+1}\right)$ was constant,  then the difference between conditional expected simple and log [returns](../Financial%20Markets/Financial%20Asset%20Pricing%20Theory%20Overview/Chapter%203%20-%20%20Assets,%20Portfolios,%20and%20Arbitrage/Assets.md) would be roughly constant most of the difference would be absorbed by the intercept term $a$ in the regression without affecting the slope coefficient $b$. However,  in reality volatility is time-varying and it may also vary with $\log \mathrm{P} / \mathrm{D}$,  which means it can affect the slope coefficient. So,  to get usable inputs for [Asset Allocation](Lecture%202-%20[[Lecture%202-%20Asset%20Allocation%20with%20Multiple%20Risky%20Assets) with [Multiple Risky Assets](Lecture%202-%20Asset%20Allocation%20with%20Multiple%20Risky%20Assets.md)|[asset allocation](Lecture%202-%20Asset%20Allocation%20with%20Multiple%20Risky%20Assets.md)]] optimization,  it makes sense for us to use simple,  not log [returns](../Financial%20Markets/Financial%20Asset%20Pricing%20Theory%20Overview/Chapter%203%20-%20%20Assets,%20Portfolios,%20and%20Arbitrage/Assets.md) as the dependent variable in the regression.

Panel B of Table 4.2 shows the result: The slope coefficient is much bigger than in Panel A,  the $t$-statistic is now -2.428 ,  which is statistically significantly different from zero at a $5/% level,    and the $R^{2}$ is now $1.3/%.

 ![500](https://cdn.mathpix.com/cropped/2024_10_19_48a1c4654e845915c45cg-098.jpg?height=911&width=1201&top_left_y=298&top_left_x=424)

Figure 3.9: Conventional and repurchase-adjusted log [price-dividend ratio](Lecture%204-%20Investor%20Sentiment.md)

Finally,  we may want to separate variation in [returns](../Financial%20Markets/Financial%20Asset%20Pricing%20Theory%20Overview/Chapter%203%20-%20%20Assets,%20Portfolios,%20and%20Arbitrage/Assets.md) that comes from variation over time in the [risk-free rate](../Financial%20Instruments/Black%20Scholes%20Derivation.md) from variation that comes from variation in the conditional [equity premium](../Financial%20Markets/Financial%20Asset%20Pricing%20Theory%20Overview/Chapter%208%20-%20Consumption-Based%20Asset%20Pricing/Theory%20Meets%20Data%20-%20Asset%20Pricing%20Puzzles.md) that can be earned by an investor. For this reason,  Panel C puts the quarterly simple [stock index](../Financial%20Instruments/Lecture%20Notes-%20Financial%20Instruments/Teaching%20Note%201-%20Forward%20Rates%20Agreement/Hedging%20Strategies%20with%20Forwards.md) return in excess of the return on a U.S. Treasury Bill [investment](An%20Asset%20Allocation%20Primer.md) (one-month T-bill,  rolled over within quarters to get a quarterly return) as the dependent variable of the regression. As it turns out,  this does not make much difference compared with Panel B.

Now,  in this regression we have used data that covers time periods stretching over almost 100 years. Lots of things have changed in the world and in the U.S. economy over this long period. Should we be worried that these relationships between [returns](../Financial%20Markets/Financial%20Asset%20Pricing%20Theory%20Overview/Chapter%203%20-%20%20Assets,%20Portfolios,%20and%20Arbitrage/Assets.md) and $\log \mathrm{P} / \mathrm{D}$ could be unstable?

This is a valid concern and we won't be able in this course to thoroughly investigate this question. But I want to highlight one such source of instability - and offer a way to fix the problem.

To see the problem,  examine Figure 3.9. The red line shows the $\log \mathrm{P} / \mathrm{D}$ ratio we have been using so far. To calculate it,  I accumulate cash dividends of all stocks in the index over moving 12-month windows and divide by the aggregate market value of all

stocks at the end of this window (and then take the log). It's striking that from around 1995 onwards,  the level of the $\log \mathrm{P} / \mathrm{D}$ ratio has been almost always substantially higher than in any period before 1995. It looks as if something had shifted up the log P/D permanently to a higher level.

The reason for this shift is that in the 1980s and 1990s,  many firms switched from paying out dividends to (at least partly) returning cash to shareholders in the form of share repurchases. Repurchases of shares are in some ways equivalent to dividends: cash leaves the company's account and arrives in shareholders' pockets. But repurchases and dividends differ in who gets the payment. With dividends,  every shareholder gets a payment. With repurchases,  the shareholders who sell their shares back to the company get cash.

In the present-value identity model that we worked with in this lecture,  repurchases did not show up explicitly. But since "price" represents the aggregate value of the [stock market](../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20III%20THE%20PLAYERS/Chapter%2012%20-%20Hedge%20Fund%20Strategies/Hedge%20Fund%20Strategies.md) and "dividends" represent the cash flows that go back to all shareholders in aggregate,  we should really include repurchases in the denominator of the [price-dividend ratio](Lecture%204-%20Investor%20Sentiment.md).

The blue line in Figure 3.9 adds repurchases to dividends when computing the log [price-dividend ratio](Lecture%204-%20Investor%20Sentiment.md). As the figure shows,  this completely eliminates the unusual level shift in the $\log \mathrm{P} / \mathrm{D}$ ratio.

Table 3.3: Predictive regressions of one-quarter-ahead [returns](../Financial%20Markets/Financial%20Asset%20Pricing%20Theory%20Overview/Chapter%203%20-%20%20Assets,%20Portfolios,%20and%20Arbitrage/Assets.md) on the lagged repurchaseadjusted $\log$ [price-dividend ratio](Lecture%204-%20Investor%20Sentiment.md),  1927-2022
![300](CleanShot%202024-10-24%20-003111@2x.png)

Table 3.3 shows that the repurchase-adjustment also improves the ability of the log [price-dividend ratio](Lecture%204-%20Investor%20Sentiment.md) to predict [returns](../Financial%20Markets/Financial%20Asset%20Pricing%20Theory%20Overview/Chapter%203%20-%20%20Assets,%20Portfolios,%20and%20Arbitrage/Assets.md): In all three panels for the different types of [returns](../Financial%20Markets/Financial%20Asset%20Pricing%20Theory%20Overview/Chapter%203%20-%20%20Assets,%20Portfolios,%20and%20Arbitrage/Assets.md),  the $t$-statistics are of greater magnitude and the $R^{2}$ are higher than in Table 4.2 .

Interestingly,  the results in Table 3.3,  and,  specifically,  the estimates of the regression slope coefficient and $R^{2}$,  are quite close to what we obtained in the simulations in Table 3.1 in the case $\phi=0.95$. (In these simulations,  $s_{t}$ and $\log \mathrm{P} / \mathrm{D}$ are equal up to a constant,  so the slope coefficient and $R^{2}$ would be the same if we had run the regressions in the simulated data on $\log \mathrm{P} / \mathrm{D}$ instead of $s_{t}$.) Recall that for this value of $\phi$,  sentimentinduced misvaluation was very large and persistent. So our empirical finding of seemingly small $R^{2}$ of around $2/% can be consistent with large,  highly persistent sentiment-driven time-varying misvaluation of the aggregate [stock market](../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20III%20THE%20PLAYERS/Chapter%2012%20-%20Hedge%20Fund%20Strategies/Hedge%20Fund%20Strategies.md).

But this also means,  as in our simulations,  that the return predictability is likely difficult to exploit in an [investment](An%20Asset%20Allocation%20Primer.md) strategy. For example,  as in our simulations,  the uncertainty about the magnitude of the slope coefficient is substantial. For example,  in Panel C the $t$-statistic for the estimate of $b$ is around -3 ,  and one standard error is a little less than 0.02. This means that it's quite likely (again using a Bayesian interpretation of statistical estimates) that the true coefficient could be substantially smaller or bigger than the estimate shown in Panel C. So our prediction of [returns](../Financial%20Markets/Financial%20Asset%20Pricing%20Theory%20Overview/Chapter%203%20-%20%20Assets,%20Portfolios,%20and%20Arbitrage/Assets.md) based on these estimates in Panel C is quite likely to be wrong in a substantial way. And that the $R^{2}$ is only around $2/% tells us that most of the future [returns](../Financial%20Markets/Financial%20Asset%20Pricing%20Theory%20Overview/Chapter%203%20-%20%20Assets,%20Portfolios,%20and%20Arbitrage/Assets.md) will be unpredictable,  even if we happened to stumble on the true slope coefficient in our estimates.

### 3.8 Other valuation measures

[Investment](An%20Asset%20Allocation%20Primer.md) practitioners frequently use a number of alternative measures along with the $\mathrm{P} / \mathrm{D}$ ratio. The common idea underlying all of these measures,  including the $\mathrm{P} / \mathrm{D}$ ratio,  is to compare the aggregate [stock price](../Financial%20Engineering/Derivatives/Part%20IV%20-%20Options/Chapter%2016%20-%20Black–Scholes%20Model.md) level with a variable that should,  at least roughly,  be proportional to the fundamental value of the fundamental value of stocks,  so that the ratio is informative about the degree of sentiment-induced misvaluation.

### 3.8.1 Cyclically adjusted price-earnings ratio

Economics Nobel laureate Robert Shiller at Yale created the cyclically-adjusted priceearnings ratio (CAPE). ${ }^{3}$ It uses aggregate earnings of firms instead of their dividends. The hope is that earnings may be a better proxy for fundamental value than dividends,  which may be distorted as a measure of fundamental value by certain quirks in firms' payout policy,  such as their tendency to smooth dividends over time,  or firms' substitu-

[^9] ![500](https://cdn.mathpix.com/cropped/2024_10_19_48a1c4654e845915c45cg-101.jpg?height=925&width=1202&top_left_y=291&top_left_x=472)

Figure 3.10: Repurchase-adjusted log [price-dividend ratio](Lecture%204-%20Investor%20Sentiment.md) and log price-earnings ratio

tion of stock repurchases for dividends in recent decades (which we tried to address by repurchase-adjusting dividends in our analysis above).

However,  just using current-year earnings as the denominator in a price-earnings ratio does not always work well because annual earnings are notoriously volatile. In particular,  when a recession hits and earnings fall,  firms often like to take big "earnings baths" by taking all sorts of asset write downs. Firms tend to prefer to take such a big earnings bath once in a while rather than having more frequent moderately low earnings. The consequence of this is that annual aggregate earnings fall much more in recessions than the fundamental value of stocks. They often fall so much that the price/earnings ratio with current-year earnings goes $u p$ when the economy hits a recession,  even though stock prices fall substantially.

As Figure 3.10 shows,  this happened during the [Great Recession](../Advanced%20Financial%20Analysis%20and%20Valuation/Problem%20Sets/HKS%20The%20Banking%20Industry.md) in 2008/09 and,  to a lesser extent in the recession in 2001. The figure also shows the repurchase-adjusted $\log P / D$ ratio for comparison. Earnings fell so much that the log price-to-earnings ratio actually went up very sharply in 2008/09,  despite the huge drop in stock prices that took place back then! This very different from how the $\log P / D$ ratio behaved. This upward spike completely destroyed the ability of the $P / E$ ratio to serve as a [Forecasting](Week%203%20Cyclical%20Industries%20(and%20Advanced%20[[Week%202%20Fundamentals%20Of%20Forecasting))|cyclical]] valuation measure around this time.

 ![500](https://cdn.mathpix.com/cropped/2024_10_19_48a1c4654e845915c45cg-102.jpg?height=915&width=1199&top_left_y=296&top_left_x=428)

Figure 3.11: Repurchase-adjusted log [price-dividend ratio](Lecture%204-%20Investor%20Sentiment.md) and log of cyclically adjusted price-earnings ratio

Shiller noticed that using a ten-year moving average of earnings instead of annual earnings gets around this problem. Because this average of earnings over the past ten years smoothes out [business cycle](../International%20Finance/Economic%20Stabilization%20Notes/Business%20Cycles-%20Introduction,%20Characteristics,%20and%20History.md) fluctuations in earnings,  the price/earnings ratio with this ten-year moving average in the denominator is called the cyclically-adjusted price/earnings ratio.

Moreover,  Shiller's calculation uses real (i.e.,  [inflation](../International%20Finance/Bridgewater/Principles%20For%20Navigating%20Big%20Debt%20Cycles/Part%20II%20Detailed%20Case%20Studies/German%20Debt%20Crisis%20andHyperinflation%20(1918–1924)/War%20Economies%20and%20Hyperinflation.md)-adjusted) earnings and prices in this calculation. He divides the real [stock price](../Financial%20Engineering/Derivatives/Part%20IV%20-%20Options/Chapter%2016%20-%20Black–Scholes%20Model.md) by the ten-year moving average of real earnings. This is an important detail especially in times when [inflation](../International%20Finance/Bridgewater/Principles%20For%20Navigating%20Big%20Debt%20Cycles/Part%20II%20Detailed%20Case%20Studies/German%20Debt%20Crisis%20andHyperinflation%20(1918–1924)/War%20Economies%20and%20Hyperinflation.md) is high. If the calculation was instead done with nominal earnings and prices,  then high [inflation](../International%20Finance/Bridgewater/Principles%20For%20Navigating%20Big%20Debt%20Cycles/Part%20II%20Detailed%20Case%20Studies/German%20Debt%20Crisis%20andHyperinflation%20(1918–1924)/War%20Economies%20and%20Hyperinflation.md) would distort the valuation ratio. When [inflation](../International%20Finance/Bridgewater/Principles%20For%20Navigating%20Big%20Debt%20Cycles/Part%20II%20Detailed%20Case%20Studies/German%20Debt%20Crisis%20andHyperinflation%20(1918–1924)/War%20Economies%20and%20Hyperinflation.md) is high,  comparing current nominal [stock price](../Financial%20Engineering/Derivatives/Part%20IV%20-%20Options/Chapter%2016%20-%20Black–Scholes%20Model.md) levels to nominal earnings from several years ago would compare apples and oranges because nominal earnings a few years ago are expressed in units of dollars that had much higher purchasing power than current dollars. Nominal earnings from a few years ago would therefore not be a good measure of future nominal earnings potential.

Figure 3.11 show the time-series of the log of CAPE in comparison with the repurchaseadjusted $\mathrm{P} / \mathrm{D}$ ratio. The two series are quite highly correlated.

### 3.8.2 Fed model

Another popular gauge of the [stock market](../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20III%20THE%20PLAYERS/Chapter%2012%20-%20Hedge%20Fund%20Strategies/Hedge%20Fund%20Strategies.md)'s valuation level is the so-called Fed modelwhich,  despite the name,  has almost nothing to do with the Federal Reserve. ${ }^{4}$ Recall the equation for the $P / D$ ratio in the Gordon growth model (3.13):
$$

\begin{equation*}

\frac{P_{t}}{D_{t}}=\frac{1+G}{R-G} \tag{3.42}

\end{equation*}

$$

The idea behind [the Fed](../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Front%20Matter/Monetary%20Policy%20with%20Abundantreserves.md) model is that the [discount rate](../Advanced%20Financial%20Analysis%20and%20Valuation/Problem%20Sets/PSET%207-%20Kohler.md) on stocks is a long-term bond yield $Y$ plus a fixed risk premium $\theta$,  i.e.,  $R=Y+\theta$. Substituting this into the equation above and solving for $R$,  we get
$$

\begin{equation*}

\theta=(1+G) \frac{D_{t}}{P_{t}}+G-Y \tag{3.43}

\end{equation*}

$$

Then,  the reasoning goes,  with the growth rate $G$ fixed,  whether stocks are attractive in terms of the risk premium $\theta$ that one can expect to earn depends on the relative magnitudes of the dividend-price ratio (calculated with "forward" dividends $(1+G) D_{t}$ ) and the bond yield. If stocks are too "expensive" with low dividend-price ratio compared with the nominal yield $Y$ offered by bonds,  then bonds are a better [investment](An%20Asset%20Allocation%20Primer.md) in expectation.

By the same logic,  higher bond yields should be bad for stocks in equilibrium in the sense that to keep earning the same risk premium $\theta$,  the dividend-price ratio must rise (via a fall in stock prices) when $Y$ rises. Conversely,  lower bond yields would justify higher stock prices relative to dividends.

There is a likely flaw in this argument though. The flaw is in thinking of $G$ as fixed while we consider variation in $Y$. In the past decades,  especially in the 1970s and 1980s,  and again very recently,  a lot of time-variation in nominal long-term bond yields is driven by [inflation](../International%20Finance/Bridgewater/Principles%20For%20Navigating%20Big%20Debt%20Cycles/Part%20II%20Detailed%20Case%20Studies/German%20Debt%20Crisis%20andHyperinflation%20(1918–1924)/War%20Economies%20and%20Hyperinflation.md). We will look at this in much more detail when we discuss bonds and [interest rates](../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%202/Interest%20Rate%20Quotations.md),  but,  broadly,  investors require higher nominal yields when [inflation](../International%20Finance/Bridgewater/Principles%20For%20Navigating%20Big%20Debt%20Cycles/Part%20II%20Detailed%20Case%20Studies/German%20Debt%20Crisis%20andHyperinflation%20(1918–1924)/War%20Economies%20and%20Hyperinflation.md) is higher. And if [inflation](../International%20Finance/Bridgewater/Principles%20For%20Navigating%20Big%20Debt%20Cycles/Part%20II%20Detailed%20Case%20Studies/German%20Debt%20Crisis%20andHyperinflation%20(1918–1924)/War%20Economies%20and%20Hyperinflation.md) is higher,  it's also likely that corporate earnings rise with [inflation](../International%20Finance/Bridgewater/Principles%20For%20Navigating%20Big%20Debt%20Cycles/Part%20II%20Detailed%20Case%20Studies/German%20Debt%20Crisis%20andHyperinflation%20(1918–1924)/War%20Economies%20and%20Hyperinflation.md),  at least in the long run. After all,  [inflation](../International%20Finance/Bridgewater/Principles%20For%20Navigating%20Big%20Debt%20Cycles/Part%20II%20Detailed%20Case%20Studies/German%20Debt%20Crisis%20andHyperinflation%20(1918–1924)/War%20Economies%20and%20Hyperinflation.md) is nothing else than firms charging higher prices for the goods and services they provide. If so,  $G$ should rise with expected [inflation](../International%20Finance/Bridgewater/Principles%20For%20Navigating%20Big%20Debt%20Cycles/Part%20II%20Detailed%20Case%20Studies/German%20Debt%20Crisis%20andHyperinflation%20(1918–1924)/War%20Economies%20and%20Hyperinflation.md). It's not clear that it should rise one-for-one with expected [inflation](../International%20Finance/Bridgewater/Principles%20For%20Navigating%20Big%20Debt%20Cycles/Part%20II%20Detailed%20Case%20Studies/German%20Debt%20Crisis%20andHyperinflation%20(1918–1924)/War%20Economies%20and%20Hyperinflation.md),  but for simplicity suppose that [dividend growth](../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%202%20-%20Spot%20Markets/Equity%20Commodity%20and%20Currency%20Math.md) and bond yields rise one-for-one with [inflation](../International%20Finance/Bridgewater/Principles%20For%20Navigating%20Big%20Debt%20Cycles/Part%20II%20Detailed%20Case%20Studies/German%20Debt%20Crisis%20andHyperinflation%20(1918–1924)/War%20Economies%20and%20Hyperinflation.md)
$$

\begin{equation*}

G=G_{r}+\pi,      \quad Y=Y_{r}+\pi \tag{3.44}

\end{equation*}

$$

[^10] ![500](https://cdn.mathpix.com/cropped/2024_10_19_48a1c4654e845915c45cg-104.jpg?height=904&width=1201&top_left_y=285&top_left_x=424)

Figure 3.12: Fed model: Repurchase-adjusted log [price-dividend ratio](Lecture%204-%20Investor%20Sentiment.md) minus 10-year yield

where $\pi$ is the [inflation](../International%20Finance/Bridgewater/Principles%20For%20Navigating%20Big%20Debt%20Cycles/Part%20II%20Detailed%20Case%20Studies/German%20Debt%20Crisis%20andHyperinflation%20(1918–1924)/War%20Economies%20and%20Hyperinflation.md) rate,  $G_{r}$ is the real growth rate,  and $Y_{r}$ is the real bond yield. Plugging this into (3.43),  we get
$$

\begin{equation*}

\theta=\frac{(1+G) D_{t}}{P_{t}}+G_{r}-Y_{r} \tag{3.45}

\end{equation*}

$$

This suggests that one should compare the forward $D / P$ ratio with the real bond yield $Y_{r}$ to assess the magnitude of the risk premium $\theta$ priced into the [stock market](../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20III%20THE%20PLAYERS/Chapter%2012%20-%20Hedge%20Fund%20Strategies/Hedge%20Fund%20Strategies.md),  not the nominal bond yield $Y$. Basically,  if stocks' payouts grow with [inflation](../International%20Finance/Bridgewater/Principles%20For%20Navigating%20Big%20Debt%20Cycles/Part%20II%20Detailed%20Case%20Studies/German%20Debt%20Crisis%20andHyperinflation%20(1918–1924)/War%20Economies%20and%20Hyperinflation.md),  this means that stocks are a real asset,  and so their dividend yield should be compared with real yields.

### 3.9 Out-of-sample prediction

The predictive regressions we looked at so far are not regressions that an actual investor could have run before they made [investment](An%20Asset%20Allocation%20Primer.md) decisions. We used decades of data all the way until the end of 2022. But an investor making decisions in,  say,  1990 would not have had access to the data after 1990. So perhaps the return predictability that we see

in the full sample regression now with data all the way until 2022 was not apparent to the same extent to an investor in 1990?

For this reason,  we now look at out-of-sample (OOS) regressions. Strictly speaking,  the regressions won't be truly out of sample. To run a true OOS test,  we would have to wait a few years to collect entirely new,  truly out-of-sample data. Instead,  we will look at pseudo-OOS tests where we recreate regressions that investors in the past could have run,  based on the data that was available at the time. As we proceed through time,  and more data becomes available,  the regressions use more observations. But to avoid clutter,  I'll still refer to these sorts of tests simply as OOS tests.

In more detail,  I fix an initial burn-in period of 40 quarters as minimum data requirement before one can run a regression. This means that I run the first regression of excess [returns](../Financial%20Markets/Financial%20Asset%20Pricing%20Theory%20Overview/Chapter%203%20-%20%20Assets,%20Portfolios,%20and%20Arbitrage/Assets.md) on the lagged repurchased-adjusted [price-dividend ratio](Lecture%204-%20Investor%20Sentiment.md) with 40 quarters of data up until the end of 1937Q1. I record the estimated coefficients and compute predicted excess [returns](../Financial%20Markets/Financial%20Asset%20Pricing%20Theory%20Overview/Chapter%203%20-%20%20Assets,%20Portfolios,%20and%20Arbitrage/Assets.md) for quarter 1937Q2. I then use this predicted excess return as [portfolio](An%20Asset%20Allocation%20Primer.md) weight $\omega_{t}$ for the [stock market](../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20III%20THE%20PLAYERS/Chapter%2012%20-%20Hedge%20Fund%20Strategies/Hedge%20Fund%20Strategies.md) index.

Investing weight $\omega$ in the [stock market](../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20III%20THE%20PLAYERS/Chapter%2012%20-%20Hedge%20Fund%20Strategies/Hedge%20Fund%20Strategies.md) and the rest in the [risk-free asset](../Financial%20Engineering/2.%20Forwards,%20Swaps,%20Futures,%20and%20Options.md) means that this market-timing strategy then has a realized excess return (i.e.,  in excess of the [risk-free return](../Financial%20Markets/Financial%20Asset%20Pricing%20Theory%20Overview/Chapter%204%20-%20State%20Prices/A%20Preview%20of%20Alternative%20Formulations.md)) in quarter 1937Q2 of
$$

\begin{equation*}

\omega_{t}\left(R_{t+1}-R_{f,      t}\right) \tag{3.46}

\end{equation*}

$$

Then I move forward one quarter and use all data until the end of quarter 1937Q2 to estimate the regression and calculate a [portfolio](An%20Asset%20Allocation%20Primer.md) return in quarter 1937Q3,  and so on,  until the end of 2021 .

If it happens to be the case that [stock market](../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20III%20THE%20PLAYERS/Chapter%2012%20-%20Hedge%20Fund%20Strategies/Hedge%20Fund%20Strategies.md) excess [returns](../Financial%20Markets/Financial%20Asset%20Pricing%20Theory%20Overview/Chapter%203%20-%20%20Assets,%20Portfolios,%20and%20Arbitrage/Assets.md) are predictable out-ofsample,  then it should be somewhat likely that $\left(R_{t+1}-R_{f,      t}\right)$ will be high in times when the [portfolio](An%20Asset%20Allocation%20Primer.md) weight $\omega_{t}$ is high,  and that $\left(R_{t+1}-R_{f,      t}\right)$ low when $\omega_{t}$ is low. In this case,  the market-timing strategy will be successful and should earn a higher Sharpe ratio than the Sharpe ratio an investor would have earned from holding a constant [portfolio](An%20Asset%20Allocation%20Primer.md) share invested in the [stock market](../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20III%20THE%20PLAYERS/Chapter%2012%20-%20Hedge%20Fund%20Strategies/Hedge%20Fund%20Strategies.md).

The blue line in Figure 3.13 shows the time-series of predicted excess return $\hat{r}_{t}$ that comes out of this exercise. When it's positive,  the pseudo-OOS trading strategy takes a [long position](../Financial%20Engineering/Derivatives/Part%20I%20-%20Forwards%20and%20Futures/Chapter%204%20-%20Futures:%20Hedging%20and%20Speculation.md) in the [stock market](../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20III%20THE%20PLAYERS/Chapter%2012%20-%20Hedge%20Fund%20Strategies/Hedge%20Fund%20Strategies.md) index,  when it's negative,  it takes a short position.

For comparison,  the red line in the figure shows the predicted excess return if one restricts the regression to have just an intercept. In this case,  there is no predictor variable and the predicted excess return at time $t$ is just he historical mean excess return in the data up to time $t$. I label this the "trailing mean." This trailing mean

 ![500](https://cdn.mathpix.com/cropped/2024_10_19_48a1c4654e845915c45cg-106.jpg?height=898&width=1199&top_left_y=288&top_left_x=425)

Figure 3.13: Predicted excess [returns](../Financial%20Markets/Financial%20Asset%20Pricing%20Theory%20Overview/Chapter%203%20-%20%20Assets,%20Portfolios,%20and%20Arbitrage/Assets.md) from recursively expanding window estimation

forecast will be a useful benchmark for evaluating how much OOS-useful information about future excess [returns](../Financial%20Markets/Financial%20Asset%20Pricing%20Theory%20Overview/Chapter%203%20-%20%20Assets,%20Portfolios,%20and%20Arbitrage/Assets.md) there is in the [price-dividend ratio](Lecture%204-%20Investor%20Sentiment.md).

To evaluate the [realized return](../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%203/Realized%20Returns.md) of the market timing strategy in (3.46),  I first standardize these [returns](../Financial%20Markets/Financial%20Asset%20Pricing%20Theory%20Overview/Chapter%203%20-%20%20Assets,%20Portfolios,%20and%20Arbitrage/Assets.md) by dividing them by the full sample standard deviation (which turns the average of these realized [returns](../Financial%20Markets/Financial%20Asset%20Pricing%20Theory%20Overview/Chapter%203%20-%20%20Assets,%20Portfolios,%20and%20Arbitrage/Assets.md) into a "realized Sharpe ratio" because the are then a ratio of mean excess return to standard deviation). I then cumulate these standardized [returns](../Financial%20Markets/Financial%20Asset%20Pricing%20Theory%20Overview/Chapter%203%20-%20%20Assets,%20Portfolios,%20and%20Arbitrage/Assets.md) over time (by simply adding up). The blue line in Figure (3.14) shows the result. Strategies with higher Sharpe ratios will end up at a higher point at the end of the sample period at the right-hand side of the plot.

To interpret this cumulative standardized return,  we need a benchmark for comparison. I use the trading strategy that uses the trailing mean instead of the [price-dividend ratio](Lecture%204-%20Investor%20Sentiment.md) regression prediction as the [portfolio](An%20Asset%20Allocation%20Primer.md) weight. [Returns](../Financial%20Markets/Financial%20Asset%20Pricing%20Theory%20Overview/Chapter%203%20-%20%20Assets,%20Portfolios,%20and%20Arbitrage/Assets.md) are again standardized and cumulated. The solid black line shows the result. The result is striking (and disappointing for anyone hoping to find an easy way to time the [stock market](../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20III%20THE%20PLAYERS/Chapter%2012%20-%20Hedge%20Fund%20Strategies/Hedge%20Fund%20Strategies.md) using the [price-dividend ratio](Lecture%204-%20Investor%20Sentiment.md)): By 2022,  the strategy using the trailing mean as forecast is just as good in terms of its cumulative performance as the strategy that used information from the [price-dividend ratio](Lecture%204-%20Investor%20Sentiment.md) in a predictive regression. Thus,  despite the [forecasting](../Advanced%20Financial%20Analysis%20and%20Valuation/Lecture%20Notes%20Advanced%20Financial%20Analysis%20and%20Valuation/Week%202/Week%202%20Fundamentals%20Of%20Forecasting.md) power that the [price-dividend ratio](Lecture%204-%20Investor%20Sentiment.md) seems to have in in-sample regressions run over the full

 ![500](https://cdn.mathpix.com/cropped/2024_10_19_48a1c4654e845915c45cg-107.jpg?height=911&width=1189&top_left_y=298&top_left_x=487)

Figure 3.14: Cumulative standardized excess [returns](../Financial%20Markets/Financial%20Asset%20Pricing%20Theory%20Overview/Chapter%203%20-%20%20Assets,%20Portfolios,%20and%20Arbitrage/Assets.md) of different out-of-sample [portfolio strategies](../Fixed%20Income%20Asset%20Pricing/Lecture%20Notes%20Bonds,%20%20Preferred%20Stock,%20%20and%20Structured%20Products.md)

sample from 1927 to 2022,  it does not seem to have been of much use for investors who had to make out-of-sample forecasts based only on data that was observable to them.

Another interesting benchmark is a strategy that keeps a constant weight in stocks without any time-variation in this weight. [Returns](../Financial%20Markets/Financial%20Asset%20Pricing%20Theory%20Overview/Chapter%203%20-%20%20Assets,%20Portfolios,%20and%20Arbitrage/Assets.md) are again standardized and cumulated. The black dotted line shows the result. In this case,  the cumulated [returns](../Financial%20Markets/Financial%20Asset%20Pricing%20Theory%20Overview/Chapter%203%20-%20%20Assets,%20Portfolios,%20and%20Arbitrage/Assets.md) at the end in 2022 are even a little higher than the cumulated return of the predictive regression strategy that uses the [price-dividend ratio](Lecture%204-%20Investor%20Sentiment.md).

But perhaps the way we have constructed the excess return forecasts in this pseudoOOS [forecasting](../Advanced%20Financial%20Analysis%20and%20Valuation/Lecture%20Notes%20Advanced%20Financial%20Analysis%20and%20Valuation/Week%202/Week%202%20Fundamentals%20Of%20Forecasting.md) exercise did not use the information in the [price-dividend ratio](Lecture%204-%20Investor%20Sentiment.md) to its full extent. Recall what we discussed in earlier lectures about estimation error and shrinkage. The estimates of the coefficients of the predictive regression come with substantial statistical uncertainty. They could be quite far from their true values due to estimation error. At the same time,  we know that excess return predictability cannot be huge,  otherwise market timing would be too easy. It can't be easy in a world where smart investors are hunting for opportunities to earn profits. These two circumstances together mean that a good forecast should not really use the regression coefficient estimates directly to construct excess return forecasts,  but first shrink them towards zero.

 ![500](https://cdn.mathpix.com/cropped/2024_10_19_48a1c4654e845915c45cg-108.jpg?height=784&width=1012&top_left_y=351&top_left_x=491)

Figure 3.15: Distribution of the difference in cumulative standardized excess [returns](../Financial%20Markets/Financial%20Asset%20Pricing%20Theory%20Overview/Chapter%203%20-%20%20Assets,%20Portfolios,%20and%20Arbitrage/Assets.md) of predictive regression minus trailing mean strategy in sentiment model simulations

I won't try to figure out the optimal degree of shrinkage here. Instead,  I'll try something very simple. I take the predictive regression coefficient estimates every period and I shrink them halfway towards the trailing mean. Put differently,  my forecast now is a weighted average of the predictive regression forecast and the trailing mean with weight $50/%. The red line shows the result. This simple shrinkage strategy does better than all the others!

Even so,  it's quite clear that OOS [forecasting](../Advanced%20Financial%20Analysis%20and%20Valuation/Lecture%20Notes%20Advanced%20Financial%20Analysis%20and%20Valuation/Week%202/Week%202%20Fundamentals%20Of%20Forecasting.md) of excess [returns](../Financial%20Markets/Financial%20Asset%20Pricing%20Theory%20Overview/Chapter%203%20-%20%20Assets,%20Portfolios,%20and%20Arbitrage/Assets.md) on a [stock market](../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20III%20THE%20PLAYERS/Chapter%2012%20-%20Hedge%20Fund%20Strategies/Hedge%20Fund%20Strategies.md) [investment](An%20Asset%20Allocation%20Primer.md) is not easy. Some observers conclude from this that the market must be macro efficient,  i.e.,  that there is little mispricing at the aggregate [stock market](../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20III%20THE%20PLAYERS/Chapter%2012%20-%20Hedge%20Fund%20Strategies/Hedge%20Fund%20Strategies.md) level. While this could be true,  it does not follow necessarily from the fact that [returns](../Financial%20Markets/Financial%20Asset%20Pricing%20Theory%20Overview/Chapter%203%20-%20%20Assets,%20Portfolios,%20and%20Arbitrage/Assets.md) are hard to forecast OOS. [Stock market](../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20III%20THE%20PLAYERS/Chapter%2012%20-%20Hedge%20Fund%20Strategies/Hedge%20Fund%20Strategies.md) excess [returns](../Financial%20Markets/Financial%20Asset%20Pricing%20Theory%20Overview/Chapter%203%20-%20%20Assets,%20Portfolios,%20and%20Arbitrage/Assets.md) would also be difficult to forecast in a world in which there is substantial mispricing,  with large deviations in stock prices from their fundamental values at the aggregate market level,  if this mispricing is very persistent. If mispricing is not followed by quick price corrections,  the mispricing does not represent a great [investment](An%20Asset%20Allocation%20Primer.md) opportunity even for the smartest investors.

Figure 3.15 illustrates this based on simulated data from the sentiment model that we looked at earlier. Each simulation run produces [returns](../Financial%20Markets/Financial%20Asset%20Pricing%20Theory%20Overview/Chapter%203%20-%20%20Assets,%20Portfolios,%20and%20Arbitrage/Assets.md) and [price-dividend ratio](Lecture%204-%20Investor%20Sentiment.md) samples

of similar length as the ones I used in Figure 3.14. I then run the pseudo-OOS [forecasting](../Advanced%20Financial%20Analysis%20and%20Valuation/Lecture%20Notes%20Advanced%20Financial%20Analysis%20and%20Valuation/Week%202/Week%202%20Fundamentals%20Of%20Forecasting.md) exercise from Figure 3.14 on the simulated data and I record the differences between the cumulated standardized excess [returns](../Financial%20Markets/Financial%20Asset%20Pricing%20Theory%20Overview/Chapter%203%20-%20%20Assets,%20Portfolios,%20and%20Arbitrage/Assets.md) of the predictive regression strategy and a trailing mean strategy. The histogram of these differences shows that the predictive regression wins on average,  but there is a huge amount of variation around it. About a third of the time,  the trailing mean forecast wins! And this is in a simulated model where we know for sure that there is big time-varying mispricing in the [stock market](../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20III%20THE%20PLAYERS/Chapter%2012%20-%20Hedge%20Fund%20Strategies/Hedge%20Fund%20Strategies.md).

That [returns](../Financial%20Markets/Financial%20Asset%20Pricing%20Theory%20Overview/Chapter%203%20-%20%20Assets,%20Portfolios,%20and%20Arbitrage/Assets.md) are not easily forecastable prevents smart investors from aggressively trading against and thereby eliminating the mispricing. So the difficulty of OOS [forecasting](../Advanced%20Financial%20Analysis%20and%20Valuation/Lecture%20Notes%20Advanced%20Financial%20Analysis%20and%20Valuation/Week%202/Week%202%20Fundamentals%20Of%20Forecasting.md) even if mispricing is big may be an important part of the story why big deviations of aggregate market values from [fundamentals](../Advanced%20Financial%20Analysis%20and%20Valuation/Lecture%20Notes%20Advanced%20Financial%20Analysis%20and%20Valuation/Week%202/Week%202%20Fundamentals%20Of%20Forecasting.md) are possible in the first place. There is little reason to think that the value of stocks in aggregate should be close to fundamental values if deviations don't represent much of a profit opportunity.

### 3.10 The trouble with market timing

Given the earlier evidence from in-sample predictive regressions that the [price-dividend ratio](Lecture%204-%20Investor%20Sentiment.md) predicts [returns](../Financial%20Markets/Financial%20Asset%20Pricing%20Theory%20Overview/Chapter%203%20-%20%20Assets,%20Portfolios,%20and%20Arbitrage/Assets.md),  why is it so difficult to construct a market-timing strategy that outperforms?

To understand this better,  a first point to note is that our evaluation of performance in Figure 3.14 was based on cumulated standardized excess [returns](../Financial%20Markets/Financial%20Asset%20Pricing%20Theory%20Overview/Chapter%203%20-%20%20Assets,%20Portfolios,%20and%20Arbitrage/Assets.md). Standardizing excess [returns](../Financial%20Markets/Financial%20Asset%20Pricing%20Theory%20Overview/Chapter%203%20-%20%20Assets,%20Portfolios,%20and%20Arbitrage/Assets.md) by their standard deviation over the full sample means we effectively compared the alternative strategies in terms of their Sharpe ratios. So we'll focus here on understanding why market-timing attempts can produce a poor Sharpe ratio even if the [portfolio](An%20Asset%20Allocation%20Primer.md) weights are based on a return-prediction model that actually produces a somewhat informative signal about expected excess [returns](../Financial%20Markets/Financial%20Asset%20Pricing%20Theory%20Overview/Chapter%203%20-%20%20Assets,%20Portfolios,%20and%20Arbitrage/Assets.md).

The root of the problem is that the signal we are getting from a predictive regression is not a perfect signal of expected [returns](../Financial%20Markets/Financial%20Asset%20Pricing%20Theory%20Overview/Chapter%203%20-%20%20Assets,%20Portfolios,%20and%20Arbitrage/Assets.md). It is distorted by noise because the predictive [regression coefficients](../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%209/A%20Practical%20Estimation%20Method.md) we use to construct the predicted [returns](../Financial%20Markets/Financial%20Asset%20Pricing%20Theory%20Overview/Chapter%203%20-%20%20Assets,%20Portfolios,%20and%20Arbitrage/Assets.md) and then the [portfolio](An%20Asset%20Allocation%20Primer.md) weight are subject to estimation error. To examine the consequences of such noise in [portfolio](An%20Asset%20Allocation%20Primer.md) weights,  let's consider the extreme case where expected [returns](../Financial%20Markets/Financial%20Asset%20Pricing%20Theory%20Overview/Chapter%203%20-%20%20Assets,%20Portfolios,%20and%20Arbitrage/Assets.md) are actually constant and the investor's timing strategy is based purely on noise. Is timing based on noise worse,  in terms of Sharpe ratio,  than just being fully invested with $100/% weight in the [stock market](../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20III%20THE%20PLAYERS/Chapter%2012%20-%20Hedge%20Fund%20Strategies/Hedge%20Fund%20Strategies.md) at all times?

Let $R_{f,      t}=0$ for simplicity. [Stock market](../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20III%20THE%20PLAYERS/Chapter%2012%20-%20Hedge%20Fund%20Strategies/Hedge%20Fund%20Strategies.md) [returns](../Financial%20Markets/Financial%20Asset%20Pricing%20Theory%20Overview/Chapter%203%20-%20%20Assets,%20Portfolios,%20and%20Arbitrage/Assets.md) are generated as
$$

\begin{equation*}

R_{t+1}=\mu+\sigma \varepsilon_{t+1},      \quad \varepsilon_{t+1} \sim \mathcal{N}(0,     1) \tag{3.47}

\end{equation*}

$$

so that market timing is not possible. A strategy with constant weight $\omega_{t}=\mu$ would earn [expected return](Lecture%201-%20Probability%20Distributions%20of%20Returns.md) and variance
$$

\begin{equation*}

\mathbb{E}\left[\mu R_{t+1}\right]=\mu^{2},      \quad \operatorname{var}\left(\mu R_{t+1}\right)=\mu^{2} \sigma^{2} . \tag{3.48}

\end{equation*}

$$

But let's say an investor tries to time the market nevertheless. The investor builds a market-timing strategy based on a signal that is a constant plus pure noise. More precisely,  the investor sets the [portfolio](An%20Asset%20Allocation%20Primer.md) weight equal to the unconditional [expected return](Lecture%201-%20Probability%20Distributions%20of%20Returns.md) $\mu$ plus noise:
$$

\begin{equation*}

\omega_{t}=\mu+\sigma_{u} u_{t},      \quad u_{t} \sim \mathcal{N}(0,     1) \tag{3.49}

\end{equation*}

$$

where $u_{t}$ is uncorrelated with $\varepsilon_{t+1}$ (so this is noise that does not predict [returns](../Financial%20Markets/Financial%20Asset%20Pricing%20Theory%20Overview/Chapter%203%20-%20%20Assets,%20Portfolios,%20and%20Arbitrage/Assets.md)). While the timing based on pure noise clearly can't boost performance,  one might hope that it at least does not hurt. But this hope would be misguided. The [expected return](Lecture%201-%20Probability%20Distributions%20of%20Returns.md) is not hurt as
$$

\begin{equation*}

\mathbb{E}\left[\omega_{t} R_{t+1}\right]=\mathbb{E}\left[\left(\mu+\sigma_{u} u_{t}\right)\left(\mu+\sigma \varepsilon_{t+1}\right)\right]=\mu^{2} \tag{3.50}

\end{equation*}

$$

is the same as the [expected return](Lecture%201-%20Probability%20Distributions%20of%20Returns.md) of a constant-weight strategy with weight equal to $\mu$. But the attempt to time the market produces a bigger variance
$$

\begin{align*}

\operatorname{var}\left[\omega_{t} R_{t+1}\right] & =\mathbb{E}\left[\omega_{t}^{2} R_{t+1}^{2}\right]-\mathbb{E}\left[\omega_{t} R_{t+1}\right]^{2} \\

& =\mathbb{E}\left[\left(\mu+\sigma_{u} u_{t}\right)^{2}\left(\mu+\sigma \varepsilon_{t+1}\right)^{2}\right]-\mu^{4} \\

& =\mu^{2} \sigma^{2}+\sigma_{u}^{2}\left(\mu^{2}+\sigma^{2}\right) \tag{3.51}

\end{align*}

$$

So relative to the constant-weight strategy variance in (3.48),  there is the additional $\sigma_{u}^{2}\left(\mu^{2}+\sigma^{2}\right)$ term here. And this term is bigger the bigger the noise variance $\sigma_{u}^{2}$. Timing based on noise induces additional variance,  from two sources:
$\sigma_{u}^{2} \mu^{2}$ : By sometimes taking a high exposure,  sometimes a low exposure to stocks,  the timing strategy generates [time-varying expected returns](.md),  which then shows up as one source of higher variance of realized [returns](../Financial%20Markets/Financial%20Asset%20Pricing%20Theory%20Overview/Chapter%203%20-%20%20Assets,%20Portfolios,%20and%20Arbitrage/Assets.md). (If $\mu$ was zero,  the [expected return](Lecture%201-%20Probability%20Distributions%20of%20Returns.md) would always stay zero,  and this component of variance would not exist.)
$\sigma_{u}^{2} \sigma^{2}$ : This one is a bit more subtle,  but quantitatively much more important. Noise makes the strategy risky in some time periods,  with high return variance when $\omega_{t}$ is high in absolute value and sometimes low return variance when $\omega_{t}$ is low. But averaged across time periods,  this variance averages to a higher value than the variance of a constant weight strategy because the variance depends on the squared [portfolio](An%20Asset%20Allocation%20Primer.md) weight. To see this,  take a simplified case with a binary noisy signal: suppose the [portfolio](An%20Asset%20Allocation%20Primer.md) weight is equal to 0.5 half the time and equal to 1.5 in the remaining time periods and hence 1.0 on average. So then the conditional variance of the resulting [investment](An%20Asset%20Allocation%20Primer.md) strategy return based on this signal is $0.5^{2} \sigma^{2}$ half the time and $1.5^{2} \sigma^{2}$ in the remaining periods. The

average conditional variance then is $\frac{1}{2} 0.5^{2} \sigma^{2}+\frac{1}{2} 1.5^{2} \sigma^{2}=1.25 \sigma^{2}$,  which is bigger than the return variance of a strategy that invests with a constant [portfolio](An%20Asset%20Allocation%20Primer.md) weight of 1.0! So mean-zero noise in [portfolio](An%20Asset%20Allocation%20Primer.md) weights raises the average conditional variance,  because the [portfolio](An%20Asset%20Allocation%20Primer.md) variance depends on the squared [portfolio](An%20Asset%20Allocation%20Primer.md) weight,  which means it is convex in the [portfolio](An%20Asset%20Allocation%20Primer.md) weight. So having [portfolio](An%20Asset%20Allocation%20Primer.md) weights vary over time for no good reason hurts the Sharpe ratio!

### 3.11 Volatility timing

The general idea underlying market timing strategies is that we would like to increase exposure to the [stock market](../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20III%20THE%20PLAYERS/Chapter%2012%20-%20Hedge%20Fund%20Strategies/Hedge%20Fund%20Strategies.md) when the reward-to-risk ratio is high and keep the exposure lower when the reward-to-risk ratio is low. This should then boost the Sharpe ratio of the long-run return of the strategy. Recall the optimal [Asset Allocation](Lecture%202-%20[[Lecture%202-%20Asset%20Allocation%20with%20Multiple%20Risky%20Assets) with [Multiple Risky Assets](Lecture%202-%20Asset%20Allocation%20with%20Multiple%20Risky%20Assets.md)|[asset allocation](Lecture%202-%20Asset%20Allocation%20with%20Multiple%20Risky%20Assets.md)]] formula for the single risky asset case (3.1),  now written with conditional moments:
$$

\begin{equation*}

\omega_{t}=\frac{\mathbb{E}_{t}\left[R_{t+1}\right]-R_{f,      t}}{\gamma \operatorname{var}_{t}\left(R_{t+1}\right)} \tag{3.52}

\end{equation*}

$$

So far we have focused on the numerator,  trying to identity variation in $\mathbb{E}_{t}\left[R_{t+1}\right]-R_{f,      t}$ in the data. But we can also improve our [Asset Allocation](Lecture%202-%20[[Lecture%202-%20Asset%20Allocation%20with%20Multiple%20Risky%20Assets) with [Multiple Risky Assets](Lecture%202-%20Asset%20Allocation%20with%20Multiple%20Risky%20Assets.md)|[asset allocation](Lecture%202-%20Asset%20Allocation%20with%20Multiple%20Risky%20Assets.md)]] if we focus on the denominator and identify variation in $\operatorname{var}_{t}\left(R_{t+1}\right)$ in the data. To identify periods when the reward for taking risk in the [stock market](../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20III%20THE%20PLAYERS/Chapter%2012%20-%20Hedge%20Fund%20Strategies/Hedge%20Fund%20Strategies.md) is high,  we can look for periods in which expected [returns](../Financial%20Markets/Financial%20Asset%20Pricing%20Theory%20Overview/Chapter%203%20-%20%20Assets,%20Portfolios,%20and%20Arbitrage/Assets.md) are higher than average,  or periods in which volatility is lower than average (or a combination of both). We now focus on predicting volatility.

To generate a time-series of volatility,  I take a series of daily [returns](../Financial%20Markets/Financial%20Asset%20Pricing%20Theory%20Overview/Chapter%203%20-%20%20Assets,%20Portfolios,%20and%20Arbitrage/Assets.md) on the CRSP value-weighted [stock market](../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20III%20THE%20PLAYERS/Chapter%2012%20-%20Hedge%20Fund%20Strategies/Hedge%20Fund%20Strategies.md) index. Each quarter I calculate the standard deviation of daily [returns](../Financial%20Markets/Financial%20Asset%20Pricing%20Theory%20Overview/Chapter%203%20-%20%20Assets,%20Portfolios,%20and%20Arbitrage/Assets.md) and I annualize (multiply by $\sqrt{250}$ ). Figure 3.16 displays the time-series of these annualized quarterly standard deviations of daily [returns](../Financial%20Markets/Financial%20Asset%20Pricing%20Theory%20Overview/Chapter%203%20-%20%20Assets,%20Portfolios,%20and%20Arbitrage/Assets.md).

As the figure shows,  there is a lot of variation over time in the level of volatility. Tranquil periods like the early 1990s or the years prior to the [financial crisis](../Financial%20Markets%20and%20Institutions/III.%20Liquidity%20of%20Assets/Class%209-%20Bailouts%20and%20Bank%20Failures/Squam%20Lake%20Group%20Letter.md) in 2008/09 have volatility below $10/%. But in quarters of turmoil,    such as at the onset of the COVID pandemic in the first quarter of 2020,    the height of the financial crisis in the last quarter of 2008,    the last quarter of 1987 (which included the "Black Monday" crash),    and the onset of the Great Depression at the end of 1929 have volatility above $40/% annualized.

The first thing we should check is whether our earlier market-timing strategy based on the $\log P / D$ ratio,  which tried to exploit variation in $\mathbb{E}_{t}\left[R_{t+1}\right]-R_{f,      t}$,  inadvertently also timed volatility,  and perhaps in the wrong direction. We can check this by regressing

 ![500](https://cdn.mathpix.com/cropped/2024_10_19_48a1c4654e845915c45cg-112.jpg?height=922&width=1201&top_left_y=287&top_left_x=424)

Figure 3.16: Annualized quarterly standard deviations of daily [stock market](../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20III%20THE%20PLAYERS/Chapter%2012%20-%20Hedge%20Fund%20Strategies/Hedge%20Fund%20Strategies.md) index [returns](../Financial%20Markets/Financial%20Asset%20Pricing%20Theory%20Overview/Chapter%203%20-%20%20Assets,%20Portfolios,%20and%20Arbitrage/Assets.md)

the quarterly volatility observations on the repurchase-adjusted $\log P / D$ ratio at the end of the previous quarter. Table 3.4 shows the result.

Table 3.4: Predicting standard deviations with the lagged repurchase-adjusted $\log P / D$ ratio,  1927-2022
![300](Microsoft%20Word%202024-10-24%2010.27.39.png)

|               | a         | b          | $R^{2}$ |
| ------------- | --------- | ---------- | ------- |
| Estimates     | 0.305     | -0.051     | 0.032   |
| $t$-statistic | $(2.368)$ | $(-1.324)$ |         |

The negative slope coefficient means that volatility tends to be somewhat higher when $P / D$ is lower. These are the times when our market-timing strategy raised the weight on the [stock market](../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20III%20THE%20PLAYERS/Chapter%2012%20-%20Hedge%20Fund%20Strategies/Hedge%20Fund%20Strategies.md) index. So our market-timing strategy did inadvertently time volatility in the wrong direction. This may have lowered the Sharpe ratio that we achieved with this strategy a little bit,  but probably not by much as the relationship between the repurchase-adjusted $\log P / D$ ratio and future volatility is very weak: as the $t$-statistic shows,  the slope coefficient estimate is not statistically significant at

conventional significance levels.

Now let's turn to predicting volatility with lagged values of volatility. Looking back at Figure 3.16,  one can see just by eyeballing the chart that volatility is much more predictable than [returns](../Financial%20Markets/Financial%20Asset%20Pricing%20Theory%20Overview/Chapter%203%20-%20%20Assets,%20Portfolios,%20and%20Arbitrage/Assets.md). Volatility is strongly positively autocorrelated and hence strongly predictable. When volatility is high in quarter $t$,  it is very likely that volatility is also going to be quite high in quarter $t+1$. The [stock market](../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20III%20THE%20PLAYERS/Chapter%2012%20-%20Hedge%20Fund%20Strategies/Hedge%20Fund%20Strategies.md) history in this figure shows that there have been multiple cycles of high and low volatility that lasted several years. In terms of predictability,  this makes volatility very different from [returns](../Financial%20Markets/Financial%20Asset%20Pricing%20Theory%20Overview/Chapter%203%20-%20%20Assets,%20Portfolios,%20and%20Arbitrage/Assets.md). While [returns](../Financial%20Markets/Financial%20Asset%20Pricing%20Theory%20Overview/Chapter%203%20-%20%20Assets,%20Portfolios,%20and%20Arbitrage/Assets.md) are hard to predict and the $R^{2}$ in any predictive regression for [returns](../Financial%20Markets/Financial%20Asset%20Pricing%20Theory%20Overview/Chapter%203%20-%20%20Assets,%20Portfolios,%20and%20Arbitrage/Assets.md) necessarily has to be low (at best perhaps a few percent in quarterly data for a good prediction model),  volatility can be predicted quite well.

Table 3.5: Predicting excess [returns](../Financial%20Markets/Financial%20Asset%20Pricing%20Theory%20Overview/Chapter%203%20-%20%20Assets,%20Portfolios,%20and%20Arbitrage/Assets.md) and standard deviations with lagged standard deviations,  1927-2022
![300](Microsoft%20Word%202024-10-24%2010.27.48.png)

|                                                      | a         | b          | $R^{2}$ |
| ---------------------------------------------------- | --------- | ---------- | ------- |
| Panel A: Regression of quarterly S.D. on lagged S.D. |           |            |         |
| Estimates                                            | 0.049     | 0.650      | 0.421   |
| $t$-statistic                                        | $(7.750)$ | $(16.686)$ |         |
| Panel B: Regression of quarterly excess              |           |            |         |
| Estimates                                            | 0.003     | 0.127      | 0.006   |
| $t$-statistic                                        | $(0.311)$ | $(1.868)$  |         |

We can see this in the regressions show in Table 3.5. Panel A shows the parameter estimates from regressing the annualized standard deviation of daily [returns](../Financial%20Markets/Financial%20Asset%20Pricing%20Theory%20Overview/Chapter%203%20-%20%20Assets,%20Portfolios,%20and%20Arbitrage/Assets.md) within quarter $t$ on the lagged standard deviation in quarter $t$. In other words,  the $b$ coefficient in this regression is the autocorrelation coefficient of the volatility time series from Figure 3.16. The estimate for this coefficient of 0.650 shows that volatility is strongly positively autocorrelated. And the $R^{2}$ of $42.1/% shows that just with its own lagged value,  we can predict a substantial share of next-quarter variation in volatility. Thus,  volatility is indeed strongly persistent and predictable. This means that when volatility is above its long-run average in the current quarter,  it is also likely to be above the long-run average in the next quarter,  but also,  on average,  somewhat closer to the long-term average than in the current quarter. By the same token,  if volatility is below the long-run average in the current quarter,  it is also likely to be below the long-run average in the next quarter,  but also,  on average,  closer to the to the long-term average than in the current quarter.

Whether volatility timing could improve the Sharpe ratio of an [investment](An%20Asset%20Allocation%20Primer.md) strategy depends on whether conditional expected excess [returns](../Financial%20Markets/Financial%20Asset%20Pricing%20Theory%20Overview/Chapter%203%20-%20%20Assets,%20Portfolios,%20and%20Arbitrage/Assets.md) of the [stock market](../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20III%20THE%20PLAYERS/Chapter%2012%20-%20Hedge%20Fund%20Strategies/Hedge%20Fund%20Strategies.md) index are

positive related to volatility or not. If they are,  then a strategy that scales down the weight of the [stock market](../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20III%20THE%20PLAYERS/Chapter%2012%20-%20Hedge%20Fund%20Strategies/Hedge%20Fund%20Strategies.md) index in favor of the [risk-free asset](../Financial%20Engineering/2.%20Forwards,%20Swaps,%20Futures,%20and%20Options.md) in times of high volatility may stay out of the market in times when expected excess [returns](../Financial%20Markets/Financial%20Asset%20Pricing%20Theory%20Overview/Chapter%203%20-%20%20Assets,%20Portfolios,%20and%20Arbitrage/Assets.md) are also high. If the relationship between conditional expected excess [returns](../Financial%20Markets/Financial%20Asset%20Pricing%20Theory%20Overview/Chapter%203%20-%20%20Assets,%20Portfolios,%20and%20Arbitrage/Assets.md) of the [stock market](../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20III%20THE%20PLAYERS/Chapter%2012%20-%20Hedge%20Fund%20Strategies/Hedge%20Fund%20Strategies.md) index and volatility is sufficiently strongly positive,  then the attempt at volatility timing may actually result in a lower Sharpe ratio. In contrast,  if the conditional [expected excess return](../Financial%20Markets/Financial%20Asset%20Pricing%20Theory%20Overview/Chapter%209%20-%20Factor%20Models/Theoretical%20Factors.md) of the [stock market](../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20III%20THE%20PLAYERS/Chapter%2012%20-%20Hedge%20Fund%20Strategies/Hedge%20Fund%20Strategies.md) index does not vary with the level of volatility,  then the reward-to-risk ratio in the [stock market](../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20III%20THE%20PLAYERS/Chapter%2012%20-%20Hedge%20Fund%20Strategies/Hedge%20Fund%20Strategies.md) is low when volatility is high,  and it may be beneficial to scale back the [stock market](../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20III%20THE%20PLAYERS/Chapter%2012%20-%20Hedge%20Fund%20Strategies/Hedge%20Fund%20Strategies.md) exposure and dial it up in times of low volatility when the reward-to-risk ratio is higher.

To check whether conditional expected excess [returns](../Financial%20Markets/Financial%20Asset%20Pricing%20Theory%20Overview/Chapter%203%20-%20%20Assets,%20Portfolios,%20and%20Arbitrage/Assets.md) are positively related to volatility,  Panel B shows a regression of quarterly excess [returns](../Financial%20Markets/Financial%20Asset%20Pricing%20Theory%20Overview/Chapter%203%20-%20%20Assets,%20Portfolios,%20and%20Arbitrage/Assets.md) on lagged volatility. The estimated slope coefficient on lagged volatility is positive,  so there is a positive empirical relationship. But with a $t$-statistic a little below two,  it is not statistically significant at conventional significance levels,  despite about $90+$ years of data,  and the $R^{2}$ is quite low. So it's not a strong positive relationship. It may be sufficiently weak for a volatilitytiming strategy to still have some beneficial effect on performance.

I will not attempt to derive the optimal utility-maximizing volatility-timing strategy here. Instead,  let's just start with the observation that if the [expected excess return](../Financial%20Markets/Financial%20Asset%20Pricing%20Theory%20Overview/Chapter%209%20-%20Factor%20Models/Theoretical%20Factors.md) conditional on lagged volatility is constant,  $\mathbb{E}\left[R_{t+1} \mid \sigma_{t}\right]-R_{f,      t}=\mu$,  a [mean-variance](../Financial%20Markets/Financial%20Asset%20Pricing%20Theory%20Overview/Chapter%2012%20-%20Derivatives/Exercises.md) optimizing investor who looks one period ahead and uses the formula (3.52) would select a risky asset share of
$$

\begin{equation*}

\omega_{t}=\frac{\mathbb{E}_{t}\left[R_{t+1}\right]-R_{f,      t}}{\gamma \operatorname{var}_{t}\left(R_{t+1}\right)} \tag{3.53}

\end{equation*}

$$

Thus,  this investor's [portfolio](An%20Asset%20Allocation%20Primer.md) share would be proportional to $1 / \sigma_{t}^{2}$. Since multiplying the [portfolio](An%20Asset%20Allocation%20Primer.md) share by a proportionality constant does not affect the Sharpe ratio,  we can work directly with $\omega_{t}=1 / \sigma_{t}^{2}$ as the [portfolio](An%20Asset%20Allocation%20Primer.md) weight to investigate potential gains from volatility timing.

However,  we do not observe conditional volatility directly. Instead,  we are going to work with lagged volatility $\hat{\sigma}_{t}$ that was realized in quarter $t$. Volatility is,  as the regressions above showed,  very persistent,  but lagged volatility translates less than one-for-one into expected next-period volatility. Moreover,  the regressions above showed that conditional expected excess [returns](../Financial%20Markets/Financial%20Asset%20Pricing%20Theory%20Overview/Chapter%203%20-%20%20Assets,%20Portfolios,%20and%20Arbitrage/Assets.md) are actually at least somewhat positively related to lagged volatility,  and not exactly constant. So we should temper the aggressiveness of volatility timing a little bit. I try to address both of these issues with a very simple tweak: Rather than setting the [portfolio](An%20Asset%20Allocation%20Primer.md) weight $\omega_{t}$ equal to the reciprocal of $\hat{\sigma}_{t}^{2}$,  I set it

 ![500](https://cdn.mathpix.com/cropped/2024_10_19_48a1c4654e845915c45cg-115.jpg?height=915&width=1189&top_left_y=296&top_left_x=487)

Figure 3.17: Cumulative standardized excess [returns](../Financial%20Markets/Financial%20Asset%20Pricing%20Theory%20Overview/Chapter%203%20-%20%20Assets,%20Portfolios,%20and%20Arbitrage/Assets.md) of the volatility-timing strategy

equal to the reciprocal of the standard deviation,
$$

\begin{equation*}

\omega_{t}=\frac{1}{\hat{\sigma}_{t}} \tag{3.54}

\end{equation*}

$$

For this simple volatility-timing strategy,  we don't need to estimate any parameters. It is directly out-of-sample implementable. All we need is a measure of lagged volatility.

I calculate the time series of volatility-timing strategy excess [returns](../Financial%20Markets/Financial%20Asset%20Pricing%20Theory%20Overview/Chapter%203%20-%20%20Assets,%20Portfolios,%20and%20Arbitrage/Assets.md) as $\omega_{t}\left(R_{t+1}-\right.$ $R_{f,      t}$ ). I then standardize the [realized return](../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%203/Realized%20Returns.md) by dividing by the full sample standard deviation (recall that this standardization turns the [returns](../Financial%20Markets/Financial%20Asset%20Pricing%20Theory%20Overview/Chapter%203%20-%20%20Assets,%20Portfolios,%20and%20Arbitrage/Assets.md) into a "realized Sharpe ratio"). I then cumulate these standardized [returns](../Financial%20Markets/Financial%20Asset%20Pricing%20Theory%20Overview/Chapter%203%20-%20%20Assets,%20Portfolios,%20and%20Arbitrage/Assets.md) over time. The red line in Figure (3.17) shows the result. For comparison,  I also show the cumulative standardized [returns](../Financial%20Markets/Financial%20Asset%20Pricing%20Theory%20Overview/Chapter%203%20-%20%20Assets,%20Portfolios,%20and%20Arbitrage/Assets.md) of a strategy that is always $100/% invested in the stock market index. The volatility-timing strategy shows some improvement relative to the $100/% [stock market](../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20III%20THE%20PLAYERS/Chapter%2012%20-%20Hedge%20Fund%20Strategies/Hedge%20Fund%20Strategies.md) index strategy. Looking closer,  we can also see that the volatility-timing strategy managed to partly avoid big downturns like in late 2008,  during the [financial crisis](../Financial%20Markets%20and%20Institutions/III.%20Liquidity%20of%20Assets/Class%209-%20Bailouts%20and%20Bank%20Failures/Squam%20Lake%20Group%20Letter.md),  or in the early 1930s,  during the onset of the [Great Depression](../International%20Finance/Bridgewater/Chapters/US%20Debt%20Crisis%20and%20Adjustment%201928-1937.md). The big down-moves in the [stock market](../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20III%20THE%20PLAYERS/Chapter%2012%20-%20Hedge%20Fund%20Strategies/Hedge%20Fund%20Strategies.md) in these episodes were preceded in earlier months by elevated levels of volatility,  which leads the volatility-timing strategy to reduce equity exposure prior to the downturn.
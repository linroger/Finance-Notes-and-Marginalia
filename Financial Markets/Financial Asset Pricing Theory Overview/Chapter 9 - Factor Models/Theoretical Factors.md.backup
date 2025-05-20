---
tags:
  - consumption_based_model
  - factor_models
  - intertemporal_capm
  - market_portfolio
  - theoretical_factors
aliases:
  - Intertemporal CAPM
  - Theoretical Factors
key_concepts:
  - Expected excess return
  - Market price of risk
  - Optimal consumption plan
  - Representative individual wealth
  - State-price deflator dynamics
---

# 9.7 Theoretical factors  

Factor models can be obtained through the general [consumption-based asset pricing](The%20Classical%20One-Period%20Capm.md) model by relating [optimal consumption](../Chapter%206%20-%20Individual%20optimality/Dynamic%20Programming.md) to various factors. As discussed in Section 6.5 the [optimal consumption plan](.md) of an individual with [time-additive expected utility](../Chapter%208%20-%20Consumption-Based%20Asset%20Pricing/General%20Multi-Period%20Link%20Between%20Consumption%20a.md) must satisfy the so-called [envelope condition](../Chapter%206%20-%20Individual%20optimality/Dynamic%20Programming.md)  
$$
u^{\prime}(c_{t})=J_{W}(W_{t},x_{t},t).
$$  

Here $J$ is the [indirect utility function](../Chapter%206%20-%20Individual%20optimality/Dynamic%20Programming.md) of the individual, i.e. the maximum obtainable expected utility of future consumption. $W_{t}$ is the financial wealth of the investor at time $t$ $x_{t}$ is the time $t$ value of a variable that captures the variations in [investment](../../../Advanced%20Investments/An%20Asset%20Allocation%20Primer.md) opportunities (captured by the riskfree interest rate, expected [returns](../Chapter%203%20-%20%20Assets,%20Portfolios,%20and%20Arbitrage/Assets.md) and volatilities on risky assets, and correlations between risky assets) and investor-specific variables (e.g. labor income). For notational simplicity, $x$ is assumed to be one-dimensional, but this could be generalized.  

In a [continuous-time framework](Exercises.md) write the dynamics of wealth compactly as  
$$
d W_{t}=W_{t}\left[\mu_{W t}d t+\pmb{\sigma}_{W t}^{\top}d z_{t}\right]
$$  

and assume that the state variable $x$ follows a diffusion process.  
$$
d x_{t}=\mu_{x t}d t+\sigma_{x t}^{\top}d z_{t},\qquad\mu_{x t}=\mu_{x}(x_{t},t),\quad\sigma_{x t}=\sigma_{x}(x_{t},t).
$$  

From (8.16) it follows that the [state-price deflator](Exercises.md) derived from this individual can be written as  
$$
\zeta_{t}=e^{-\delta t}\frac{J_{W}(W_{t},x_{t},t)}{J_{W}(W_{0},x_{0},0)}.
$$  

An application of [Ito's Lemma](../../../Financial%20Engineering/Determining%20the%20Stochastic%20Process%20for%20a%20Forward%20Contract%20from%20Ito’s%20Lemma.md) yields a new expression for the dynamics of $\zeta$ , which again can be compared with (4.41). It follows from this comparison that.  
$$
\lambda_{t}=\left(\frac{-W_{t}J_{W W}(W_{t},x_{t},t)}{J_{W}(W_{t},x_{t},t)}\right)\sigma_{W t}+\left(\frac{-J_{W x}(W_{t},x_{t},t)}{J_{W}(W_{t},x_{t},t)}\right)\sigma_{x t},
$$  

is a [market price of risk](Exercises.md). Consequently, the expected excess rate of return on asset $i$ can be written  
$$
\mu_{i t}+\delta_{i t}-r_{t}^{f}=\left(\frac{-W_{t}J_{W W}(W_{t},x_{t},t)}{J_{W}(W_{t},x_{t},t)}\right)\sigma_{i t}^{\top}\sigma_{W t}+\left(\frac{-J_{W x}(W_{t},x_{t},t)}{J_{W}(W_{t},x_{t},t)}\right)\sigma_{i t}^{\top}\sigma_{x t},
$$  

which can be rewritten as  
$$
\mu_{i t}+\delta_{i t}-r_{t}^{f}=\beta_{i W t}\eta_{W t}+\beta_{i x t}\eta_{x t},
$$  

where  
$$
\begin{array}{r}{\beta_{i W t}=\frac{\sigma_{i t}^{\top}\sigma_{W t}}{\|\sigma_{W t}\|^{2}},\quad\beta_{i x t}=\frac{\sigma_{i t}^{\top}\sigma_{x t}}{\|\sigma_{x t}\|^{2}},\quad}\ {\eta_{W t}=\|\sigma_{W t}\|^{2}\left(\frac{-W_{t}J_{W W}\left(W_{t},x_{t},t\right)}{J_{W}\left(W_{t},x_{t},t\right)}\right),\quad\eta_{x t}=\|\sigma_{x t}\|^{2}\left(\frac{-J_{W x}\left(W_{t},x_{t},t\right)}{J_{W}\left(W_{t},x_{t},t\right)}\right).}\end{array}
$$  

We now have a continuous-time version of (9.35) with the wealth of the individual and the state variable as the factors.If it takes. $m$ state variables to describe the variations in [investment](../../../Advanced%20Investments/An%20Asset%20Allocation%20Primer.md). opportunities, labor income, etc., we get an. $(m+1)$ -[factor model](Pricing%20Factors%20in%20a%20One-Period%20Framework.md).  

If the individual is taken to be a [representative individual](../Chapter%208%20-%20Consumption-Based%20Asset%20Pricing/The%20Simple%20Multi-Period%20Ccapm.md), her wealth will be identical to the. aggregate value of all assets in the economy, including all traded financial assets and non-traded. asset such as human capital. This is like the market [portfolio](../../../Advanced%20Investments/An%20Asset%20Allocation%20Primer.md) in the traditional static CAPM. The first term on the right-hand side of (9.42) is then the product of the [relative risk aversion](../Chapter%208%20-%20Consumption-Based%20Asset%20Pricing/CCAPM%20with%20Alternative%20Preferences.md) of the [representative individual](../Chapter%208%20-%20Consumption-Based%20Asset%20Pricing/The%20Simple%20Multi-Period%20Ccapm.md) (derived from her [indirect utility](../Chapter%206%20-%20Individual%20optimality/Epstein-Zin%20Recursive%20Utility.md)) and the covariance between the rate of return on asset $i$ and the rate of return on the market [portfolio](../../../Advanced%20Investments/An%20Asset%20Allocation%20Primer.md). In the special case where the. [indirect utility](../Chapter%206%20-%20Individual%20optimality/Epstein-Zin%20Recursive%20Utility.md) is a function of wealth and time only, the last term on the right-hand side will be zero, and we get the well-known relation.  
$$
\mu_{i t}+\delta_{i t}-r_{t}^{f}=\beta_{i W t}\left(\mu_{W t}+\delta_{W t}-r_{t}^{f}\right),
$$  

where $\beta_{i W t}$ is the "market-beta' of asset. $i$ . This is a continuous-time version of the traditional. static CAPM. This is only true under the strong assumption that individuals do not care about. variations in [investment](../../../Advanced%20Investments/An%20Asset%20Allocation%20Primer.md) opportunities, income, etc. In general we have to add factors describing the future [investment](../../../Advanced%20Investments/An%20Asset%20Allocation%20Primer.md) opportunities, future labor income, etc. This extension of the CAPM is called the [Intertemporal CAPM](.md) and was first derived by [Merton](../../../Credit%20Markets/Credit%20Markets%20Session%205.md) (1973b)..  

Only few empirical studies of factor models refer to [Merton](../../../Credit%20Markets/Credit%20Markets%20Session%205.md)'s [Intertemporal CAPM](.md) when motivating the choice of factors. Brennan, Wang, and Xia (2004) set up a simple model with the short-term real interest rate and the slope of the capital market line as the factors since these variables capture the [investment](../../../Advanced%20Investments/An%20Asset%20Allocation%20Primer.md) opportunities. In an empirical test, this model performs as well as the Fama-French model, which is encouraging for the development of theoretically well-founded and empirically viable factor models.  
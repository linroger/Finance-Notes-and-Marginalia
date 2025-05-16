---
title: Credit Markets Session 5
tags:
  - black_scholes_model
  - capital_structure
  - cdos
  - correlated_defaults
  - credit_markets
  - merton_model
  - volatility_smiles
  - structural_credit_models
  - credit_default_risk
  - option_pricing
aliases:
  - BS Model
  - Credit Risk
  - Merton
  - Structural Credit
  - Capital Structure Models
key_concepts:
  - Base correlations
  - Black-Scholes formula
  - CS strategies
  - Capital structure modeling
  - Collateralized debt obligations
  - Credit default risk
  - Fair value bonds
  - Fair value equity
  - Hedging bonds defaults
  - Merton model
  - Synthetic cdo pricing
  - Volatility smiles
  - Structural Credit Models
  - Correlated Defaults
  - Default Barrier
---

# Credit Markets Session 5
1. [Capital Structure](../Advanced%20Financial%20Analysis%20and%20Valuation/Introduction%20to%20Corporate%20Finance.md)
	- [Structural Approach](../Financial%20Engineering/8.%20Credit%20Modeling%20and%20Credit%20Derivatives.md) to [Credit Default Risk](.md)
2. [Black-Scholes Model](../Financial%20Instruments/Black%20Scholes%20Derivation.md)
	- Recap: [Black-Scholes](../Financial%20Engineering/Mathematical%20Modeling%20of%20Derivative%20Pricing.md)
3. [Merton Model](.md)
	- [Structural Credit](.md) Models
	- Fair Value of Equity
	- Fair Value of Risky Bonds
	- [Volatility Smiles](.md)
4. [CS Strategies](.md)
	- [Capital Structure](../Advanced%20Financial%20Analysis%20and%20Valuation/Introduction%20to%20Corporate%20Finance.md) Strategies
	- [Hedging](../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%205/Key%20Rates%20O1s%20Durations%20and%20Hedging.md) bonds against defaults
5. Correlated Defaults
	- Correlated defaults
6. Cdos
	- [Collateralized Debt Obligations](.md)
	- [Synthetic Cdo Pricing](.md) / [Base Correlations](.md)
7. Q&A

## Reminder: E of a Corporation Structural Approach

![500](Z.%20Clippings/Credit%20Markets%20Session%205-20240506035225976.png)

Main idea: model interaction between components of the [capital structure](../Advanced%20Financial%20Analysis%20and%20Valuation/Introduction%20to%20Corporate%20Finance.md) of a corporation

- Assets value of corporation modeled by [stochastic process](../The%20Ornstein-Uhlenbeck%20(OU)%20Process.md) 
$$\left(A_t\right)_{t\geq0}, A_t>0 \tag{1}$$
- Corporate Liabilities are known and denoted by 
$$\left(K_t\right)_{t\geq0}, K_t\geq0 \tag{2}$$

## Book Value of Equity and Leverage
- [Leverage](../Advanced%20Investments/Lecture%206-Leverage,%20Tail%20Risk,%20Volatility%20Products.md) $L$ of the corporate [capital structure](../Advanced%20Financial%20Analysis%20and%20Valuation/Introduction%20to%20Corporate%20Finance.md) defined as
$$L_t=\frac{Liabilities}{Assets}=\frac{K_t}{A_t}\tag{3}$$

- [Leverage](../Advanced%20Investments/Lecture%206-Leverage,%20Tail%20Risk,%20Volatility%20Products.md) can be obtained from corporate balance sheet details
- "Book Value of Equity" defined as "Assets - Liabilities"
$$BVE_t=A_t-K_t=A_t\cdot(1-L_t)\tag{4}$$

- Time horizon for credit default event given by maturity of liabilities

## Reminder: [Black-Scholes](../Financial%20Engineering/Mathematical%20Modeling%20of%20Derivative%20Pricing.md) '73 Option Pricing Formulas

- [Stock price process](Black-Scholes%20Model.md) $S_t$ follows [geometric Brownian motion](../Financial%20Instruments/Black%20Scholes%20Derivation.md) with constant drift $r$ and volatility $\sigma$ (under [risk neutral](../Financial%20Instruments/Lecture%20Notes-%20Financial%20Instruments/Teaching%20Note%207-Exotic%20Options%20And%20Derivative%20Pricing%20By%20Monte%20Carlo%20Simulation.md) measure)
$$\frac{dS_t}{S_t}=r\cdot dt+\sigma\cdot dW_t, S_0>0, \tag{5}$$
$$S_t=S_0\cdot\exp\left[\left(r-\frac12\sigma^2\right)\cdot t+\sigma\cdot W_t\right].\tag{6}$$

- Stock log-price $S_t$ is normally distributed:
$$\log\left(\frac{S_t}{S_0}\right)\sim\mathcal{N}\left[\left(r-\frac12\sigma^2\right)\cdot t, \sigma^2\cdot t\right].\tag{7}$$

# Reminder: Black-Scholes '73 Option Pricing Formulas

## Equation Breakdown
$$\text{Call} (S_0, K, T, \sigma, r) = e^{-rT} \cdot \mathbb{E}[(S_T - K)^+ | \mathcal{F}_0]$$

- **$S_0$**: The initial [stock price](../Financial%20Engineering/Derivatives/Part%20IV%20-%20Options/Chapter%2016%20-%20Black–Scholes%20Model.md) at time $t = 0$.
- **$K$**: The [strike price](../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%205%20Options%20on%20Prices%20and%20Hedge-Based%20Valuation/Call%20and%20Put%20Payoffs%20at%20Expiry.md) of the option, i.e., the price at which the holder of the option can buy the stock at maturity.
- **$T$**: The [time to maturity](../Financial%20Instruments/Lecture%20Notes-%20Financial%20Instruments/Teaching%20Note%201-%20Forward%20Rates%20Agreement/Hedging%20Strategies%20with%20Forwards.md) of the option (in years).
- **$\sigma$**: The volatility of the [stock price](../Financial%20Engineering/Derivatives/Part%20IV%20-%20Options/Chapter%2016%20-%20Black–Scholes%20Model.md), a measure of the amount by which the [stock price](../Financial%20Engineering/Derivatives/Part%20IV%20-%20Options/Chapter%2016%20-%20Black–Scholes%20Model.md) is expected to fluctuate per year.
- **$r$**: The [risk-free interest rate](../Financial%20Markets/Financial%20Asset%20Pricing%20Theory%20Overview/Chapter%2012%20-%20Derivatives/Exercises.md), representing the time value of money.
- **$\mathbb{E}[(S_T - K)^+ | \mathcal{F}_0]$**: The expected value of the payoff of the call option at maturity, conditioned on the filtration $\mathcal{F}_0$, which represents the information available at time $t = 0$.

## Payoff Function

The payoff of a European call option at maturity is given by $(S_T - K)^+$, where $x^+ = \max(x, 0)$. This means that the holder of the option will exercise it and benefit from the payoff if $S_T > K$ ([stock price at maturity](../Financial%20Instruments/Review%20Session%20Notes/Binomial%20Trees%20and%20Option%20Pricing%20MBA.md) exceeds the [strike price](../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%205%20Options%20on%20Prices%20and%20Hedge-Based%20Valuation/Call%20and%20Put%20Payoffs%20at%20Expiry.md)), and will let it expire worthless otherwise.

## Risk-Neutral Valuation

The factor $e^{-rT}$ is used to discount the expected payoff back to present value, under the [risk-neutral measure](../Financial%20Engineering/Verifying%20Martingale%20Property%20with%20Q.md). In a [risk-neutral world](../Financial%20Instruments/Binomial%20Option%20Pricing%20Model.md), all investors are assumed to earn at a rate of return equal to the [risk-free rate](../Financial%20Instruments/Black%20Scholes%20Derivation.md) $r$, regardless of the [investment](../Advanced%20Investments/An%20Asset%20Allocation%20Primer.md)'s risk. Thus, the [expected return](../Advanced%20Investments/Lecture%201-%20Probability%20Distributions%20of%20Returns.md) of holding the stock is also $r$, and the expected growth rate of the stock under this measure is adjusted accordingly.

## Black-Scholes Formula

The expected value $\mathbb{E}[(S_T - K)^+]$ is calculated under the assumption that the [stock price](../Financial%20Engineering/Derivatives/Part%20IV%20-%20Options/Chapter%2016%20-%20Black–Scholes%20Model.md) follows a [geometric Brownian motion](../Financial%20Instruments/Black%20Scholes%20Derivation.md) under the [risk-neutral measure](../Financial%20Engineering/Verifying%20Martingale%20Property%20with%20Q.md). This leads to the [stock price](../Financial%20Engineering/Derivatives/Part%20IV%20-%20Options/Chapter%2016%20-%20Black–Scholes%20Model.md) at time $T$, $S_T$, being log-normally distributed with:
$$S_T = S_0 e^{(r - \frac{1}{2} \sigma^2)T + \sigma \sqrt{T} Z}$$

where $Z$ is a standard normal random variable.

The [Black-Scholes formula](.md) for a European call option can then be expressed as:
$$\text{Call}(S_0, K, T, \sigma, r) = S_0 N(d_1) - e^{-rT} K N(d_2)$$

where:

- **$N(d)$** is the cumulative [distribution function](../Financial%20Engineering/Verification%20of%20Central%20Limit%20Theorem.md) of the [standard normal distribution](../Financial%20Engineering/Verification%20of%20Central%20Limit%20Theorem.md).
- **$d_1 = \frac{\log(S_0/K) + (r + \sigma^2/2)T}{\sigma \sqrt{T}}$**
- **$d_2 = d_1 - \sigma \sqrt{T}$**

This formula results from integrating the payoff function over the probability density function of $S_T$, using the properties of the log-normal distribution and the properties of [stochastic calculus](../Financial%20Engineering/6.%20A%20Brief%20Introduction%20to%20Stochastic%20Calculus.md).

- Fair value price of European Call option with maturity T and strike K given by
$$= S_0 \cdot \Phi (d_+) - e^{-r T} \cdot K \cdot \Phi (d_-), \tag{9}$$
$$d_\pm = \frac{\log (S_0/K) + (r \pm \frac{1}{2}\sigma^2) \cdot T}{\sigma \cdot \sqrt{T}}\tag{10}$$

- Intuition behind option [pricing](../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%207/Arbitrage%20Pricing%20of%20Derivatives.md) formulas
	- use [risk-neutral measure](../Financial%20Engineering/Verifying%20Martingale%20Property%20with%20Q.md) $d\tilde{P}$ and stock-forward measure $d\tilde{P}_* = \frac{S_T}{S_0 e^{rT}} d\tilde{P}$ (via Girsanov transform):

$$\begin{align}
\text{Call} (S_0, K, T, \sigma, r) &= e^{-rT} \cdot \mathbb{E} \left[(S_T - K)^+ \mid \mathcal{F}_0 \right] \tag{11} \\
&= e^{-rT} \cdot \mathbb{E} \left[ (S_T - K) \cdot \mathbb{1}_{\{S_T > K\}} \mid \mathcal{F}_0 \right] \\
&= S_0 \cdot \mathbb{E} \left[\frac{S_T}{S_0 e^{rT}} \cdot \mathbb{1}_{\{S_T > K\}} \mid \mathcal{F}_0 \right] - e^{-rT} \cdot K \cdot \mathbb{E} \left[\mathbb{1}_{\{S_T > K\}} \mid \mathcal{F}_0 \right] \\
&= S_0 \cdot \mathbb{P}(S_T > K \mid \mathcal{F}_0) - K \cdot e^{-rT} \cdot \mathbb{P}(S_T > K \mid \mathcal{F}_0) \tag{12} \\
&= S_0 \cdot \Phi (d_+) - e^{-rT} \cdot K \cdot \Phi (d_-) \tag{13}
\end{align}$$

- It's all about measuring the event $\{S_T > K\}$ under $\mathbb{P}$ and $\mathbb{P}_*$

## Intuition Behind Option Delta Hedging
1. **Definition of Delta**:

   $$\Delta_{\text{Call}} (S_0, K, T, \sigma, r, t)\tag{14}$$

   $$= \frac{\partial}{\partial S_0} \left\{ e^{-rT} \cdot \mathbb{E} \left[(S_T - K)^+ \mid \mathcal{F}_0 \right] \right\}$$

2. **Interchanging Derivative and Expectation**:

   $$= e^{-rT} \cdot \mathbb{E} \left[\frac{\partial}{\partial S_0} (S_T - K)^+ \mid \mathcal{F}_0 \right]$$

3. **Differentiating the Payoff**:

   $$= e^{-rT} \cdot \mathbb{E} \left[\frac{S_T}{S_0} \cdot \mathbb{1}_{\{S_T > K\}} \mid \mathcal{F}_0 \right]$$

	- **Explanation**: This differentiation assumes $S_T$ is functionally dependent on $S_0$, which under the [Black-Scholes model](../Financial%20Instruments/Black%20Scholes%20Derivation.md), it is. Thus, $\frac{\partial S_T}{\partial S_0} = \frac{S_T}{S_0}$.

4. **Simplifying to Risk-Neutral Probability**:
   $$= \mathbb{P}(S_T > K \mid \mathcal{F}_0)\tag{15}$$

5. **Final Delta Expression Using Cumulative Normal Distribution**:
   $$= \Phi(d_+)\tag{16}$$
   $$ d_1 = \frac{\log(S_0/K) + (r + \frac{1}{2}\sigma^2)T}{\sigma\sqrt{T}}$$
	- $\Phi$ represents the cumulative [distribution function](../Financial%20Engineering/Verification%20of%20Central%20Limit%20Theorem.md) of the [standard normal distribution](../Financial%20Engineering/Verification%20of%20Central%20Limit%20Theorem.md).

## Recovering the Market Implied Distribution of $S_T$
- **Implied [Distribution Function](../Financial%20Engineering/Verification%20of%20Central%20Limit%20Theorem.md)**:
	- The statement about the implied distribution refers to the model-independent cumulative [distribution function](../Financial%20Engineering/Verification%20of%20Central%20Limit%20Theorem.md) $\mathbb{P}(S_T \leq K \mid \mathcal{F}_0)$. This function can be derived by evaluating how market prices of options (both calls and puts) across various strike prices $K$ reflect the cumulative probabilities under the [risk-neutral measure](../Financial%20Engineering/Verifying%20Martingale%20Property%20with%20Q.md). This method involves using the Breeden-Litzenberger identity which expresses that the second derivative of option prices with respect to strike prices provides the density function under the [risk-neutral measure](../Financial%20Engineering/Verifying%20Martingale%20Property%20with%20Q.md).

## Recovering the Market Implied Distribution of $S_T$
1. **Intuition behind option [delta hedging](../Financial%20Instruments/Financial%20Instruments.md):**
$$\Delta \text{Call} (S_0, K, T, \sigma, r) = \frac{\partial}{\partial S_0} \left\{ e^{-rT} \mathbb{E}[(S_T - K)^+ \mid \mathcal{F}_0] \right\}$$
$$ = e^{-rT} \mathbb{E} \left[\frac{\partial}{\partial S_0} (S_T - K)^+ \mid \mathcal{F}_0 \right]$$
$$= e^{-rT} \mathbb{E} \left[\frac{S_T}{S_0} \mathbf{1}_{\{S_T > K\}} \mid \mathcal{F}_0 \right] = \mathbb{P}^* [S_T > K \mid \mathcal{F}_0] = \Phi(d_+)$$

2. **Recovering the market implied distribution of $S_T$:**
   $$\text{Call}(S_0, K + \Delta K, \ldots) - \text{Call}(S_0, K, \ldots) \approx \frac{\partial}{\partial K} \text{Call}(S_0, K, \ldots)$$
   $$= \frac{\partial}{\partial K} \left\{ e^{-rT} \mathbb{E}[(S_T - K)^+ \mid \mathcal{F}_0] \right\} = e^{-rT} \mathbb{E}[\mathbf{1}_{\{S_T \leq K\}} \mid \mathcal{F}_0] = e^{-rT} \mathbb{P}[S_T \leq K \mid \mathcal{F}_0]$$

3. **Credit default event:**
   $$\frac{dA_t}{A_t} = r \, dt + \sigma_A \, dW_t, \quad A_0 > 0$$
   $$A_t = A_0 \exp \left(\left(r - \frac{1}{2} \sigma_A^2 \right) t + \sigma_A W_t \right)$$
   $$ \tau = \begin{cases}
   T, & \text{if } A_T \leq K \\
   \infty, & \text{if } A_T > K
   \end{cases}$$

4. **Equity Fair Value:**
$$E_0 = e^{-rT} \mathbb{E}[(A_T - K)^+ \mid \mathcal{F}_0] = \text{Call}(A_0, K, T, \sigma_A, r)$$
$$= A_0 \Phi(d_+) - e^{-rT} K \Phi(d_-), \quad d_{\pm} = \frac{\log(A_0/K) + (r \pm \frac{1}{2} \sigma_A^2) T}{\sigma_A \sqrt{T}}$$

Is the market implied distribution of $S_T$ log-normal with constant volatility σ? Not really...

## Structural Credit Default Model: Merton '74 Extension
- At time horizon $T$, the firm has the [contractual obligation](../Clippings/Forward%20Rate.md) to liquidate the assets and repay the fixed liabilities $K_T = K$
- No refinancing of debt is allowed!
- Credit default triggered if value of assets $A_T$ is below liabilities $K$ (Book Value of Equity < 0) at time horizon $T$
- Equity investors have limited liability, so their payout at T is
	- $$\text{EquityPayout} = (BVE_T)^+ = (A_T - K)^+\tag{18}$$
- Bond investors take over the assets in case of default, their payout at T is
	- $$\text{BondPayout} = \min (K, A_T) = A_T - (A_T - K)^+\tag{19}$$

## Possible Paths of Asset Values Relative to Liabilities

![500](Z.%20Clippings/Credit%20Markets%20Session%205-20240506035320204.png)

## Credit Default Event
- Constant [interest rates](../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%202/Interest%20Rate%20Quotations.md) $r$
- Constant asset volatility $\sigma_A$
- Asset value process $A_t$ follows a [geometric Brownian motion](../Financial%20Instruments/Black%20Scholes%20Derivation.md) with drift (under [risk neutral](../Financial%20Instruments/Lecture%20Notes-%20Financial%20Instruments/Teaching%20Note%207-Exotic%20Options%20And%20Derivative%20Pricing%20By%20Monte%20Carlo%20Simulation.md) measure)
	- $$\frac{dA_t}{A_t} = r \cdot dt + \sigma_A \cdot dW_t, A_0 > 0\tag{20}$$
	- $$A_t = A_0 \cdot \exp \left[\left(r - \frac{1}{2} \sigma_A^2 \right) \cdot t + \sigma_A \cdot W_t \right]\tag{21}$$
- Default time $\tau$ is discrete and given by
	- $$\tau = \begin{cases}
        T, & \text{if } A_T \leq K \\
        \infty, & \text{if } A_T > K
      \end{cases}\tag{22}$$

## Equity Value as a Function of Assets and Liabilities

![500](Z.%20Clippings/Credit%20Markets%20Session%205-20240506035424495.png)

## Equity Fair Value
- Fair Value of equity computed from the equity payout function
- ... via [Black-Scholes](../Financial%20Engineering/Mathematical%20Modeling%20of%20Derivative%20Pricing.md)-[Merton](.md) risk-neutral valuation formula

$$\begin{aligned}
&E_0=e^{-r\cdot T}\cdot\mathbb{E}\left[\left(A_T-K\right)^+\left|\mathcal{F}_0\right]\right. && (23) \\
&=\text{Call}\left(A_0, K, T, \sigma_A, r \right) \\
&=A_0\cdot\Phi\left(d_+\right)-e^{-r\cdot T}\cdot K\cdot\Phi\left(d_-\right), \\
&d_{\pm}=\frac{-\log\left(L_{0}\right)+\left(r\pm\frac{1}{2}\sigma_{A}^{2}\right)\cdot T}{\sigma_{A}\cdot\sqrt{T}}&& \text{(24)}
\end{aligned}$$

![500](Z.%20Clippings/%20Session%205-20240506035532128.png)

# Fair Value of Risky Bond / Risky Liabilities
- Computed from risky bond payoff function:

$$ \begin{aligned}
B_0 &= e^{-r\cdot T}\cdot\mathbb{E}\left[\min\left(K, A_T\right)|\mathcal{F}_0\right] && \text{(25)} \\
&= e^{-r\cdot T}\cdot\mathbb{E}\left[A_T-\left(A_T-K\right)^+|\mathcal{F}_0\right] \\
&= A_0-\left[A_0\cdot\Phi\left(d_+\right)-e^{-r\cdot T}\cdot K\cdot\Phi\left(d_-\right)\right] \\
&= A_0\cdot\Phi\left(-d_+\right)+e^{-r\cdot T}\cdot K\cdot\Phi\left(d_-\right).
\end{aligned}$$

- [Arbitrage](../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%207/Arbitrage%20Pricing%20of%20Derivatives.md) relationship holds ([Modigliani](../Financial%20Markets/Financial%20Asset%20Pricing%20Theory%20Overview/Chapter%2010%20-%20The%20Economics%20of%20the%20Term%20Structure%20of%20Interest%20Rates/Liquidity%20Preference%20Market%20Segmentation%20and%20P.md)-Miller theorem):
	- $$A_0 = B_0 + E_0\tag{26}$$

![500](Z.%20Clippings/Credit%20Markets%20Session%205-20240506035543887.png)

## Survival and Default Probabilities for Time Horizon $T$
- [Survival Probability](../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%207%20-%20Default%20Risk%20and%20Credit%20Derivatives/A%20Poisson%20Model%20of%20Single%20Issuer%20Default.md) computed as 
$$SP(0, T)=\mathbb{P}\left[\tau>T|\mathcal{F}_0\right]\\=\mathbb{P}\left[A_T>K|\mathcal{F}_0\right]\\=\Phi\left(d_-\right).\tag{27}$$
- Default Probability computed as
$$DP(0, T)=1-SP(0, T)=1-\Phi\left(d_-\right)\\=\Phi\left(-d_-\right).\tag{28}$$

## Hazard Rates and "Distance to Default"
- Flat Hazard Rate computed as
$$h=-\frac1T\cdot\log\left(SP(0, T)\right)=-\frac1T\cdot\log\left(\Phi\left(d_-\right)\right)\tag{29}$$

- Using KMV "Distance to Default"/DD notation:

$$\begin{align} 
DD &= d_{-} \tag{30} \\ 
DP(0, T) &= \Phi(-DD) \tag{31} \\ 
SP(0, T) &= \Phi(DD) \tag{32} 
\end{align}$$

## Risky Bond Yield and Credit Spread
- Yield of risky bond is given by
$$y_0=-\frac{\log\left(B_0/K\right)}{T}\tag{33}$$
$$=-\frac1T\cdot\log\left(L_0^{-1}\cdot\Phi\left(-d_+\right)+e^{-r\cdot T}\cdot\Phi\left(d_-\right)\right)$$
- [Credit spread](../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%2014/Cds-Equivalent%20Bond%20Spread.md) of risky bond ("yield-risk free rate")
$$s_0=y_0-r=-\frac1T\cdot\log{(B_0/K)}-r$$
$$=-\frac1T\cdot\log\left(e^{r\cdot T}\cdot L_0^{-1}\cdot\Phi\left(-d_+\right)+\Phi\left(d_-\right)\right)\tag{34}$$

![500](Credit%20Markets%20Session%205-20240508035225840.png)

## Expected Recovery Rate Given Default R

$$\begin{aligned}
&R=\mathbb{E}\left[\frac{A_T}{K}|A_T<K, \mathcal{F}_0\right] \\
&=\frac{\mathbb{E}\left[\frac{A_T}{K}\cdot\mathbb{1}_{\{A_T<K\}}|\mathcal{F}_0\right]}{\mathbb{P}\left[A_T<K|\mathcal{F}_0\right]} \\
&=\frac{A_0}{K}\cdot\frac{\Phi\left(-d_+\right)}{\Phi\left(-d_-\right)}
\end{aligned}\tag{35}$$

![500](Credit%20Markets%20Session%205-20240508035457245.png)

## Expected Recovery on Default Equity vs. Assets Volatilities
- We apply [Ito's lemma](Determining%20the%20Stochastic%20Process%20for%20a%20Forward%20Contract%20from%20Ito's%20Lemma) to the equity price:
$$\frac{dE_t}{E_t}=\frac{1}{E_t}\cdot\frac{\partial E}{\partial A}\left(A_t, K\right)\cdot dA_t+\ldots\tag{36}$$
$$=\frac{A_t}{E_t}\cdot \text{DeltaCall}\left(A_t, K\right)\cdot\sigma_{A}\cdot dW_t+\ldots$$
$$=\frac{A_t}{E_t}\cdot\Phi\left(d_{+}\right)\cdot\sigma_{A}\cdot dW_t+\ldots$$
- Connection between equity vol $\sigma_{E}$ and assets vol $\sigma_{A}$ ($t$ =0):
$$\sigma_{E}=\frac{A_{0}}{E_{0}}\cdot\Phi\left(d_{+}\right)\cdot\sigma_{A}.\tag{37}$$
- Equity volatility $\sigma_E$ is stochastic, and inversely correlated to equity price changes!

![500](Credit%20Markets%20Session%205-20240508035755242.png)

## Equity Volatility Surface Leverage Effect for Equity Volatilities

Intuitive explanation: when asset prices change, equity price and equity volatility move in opposite directions 
$$\frac{\partial E}{\partial A}=\text{DeltaCall}>0\tag{38}$$,
$$\frac{\partial\sigma_{E}}{\partial A}\approx-\frac{L\cdot A}{E^{2}}\cdot \text{DeltaCall}\cdot\sigma_{A}<0\tag{39}$$

Correlation between equity price and equity vol changes is negative and dependent on company [leverage](../Advanced%20Investments/Lecture%206-Leverage,%20Tail%20Risk,%20Volatility%20Products.md) parameter $L$

Zero-correlation case obtain only for un-leveraged companies only (when Assets = Equity)

## Equity Option Valuation

![500](Credit%20Markets%20Session%205-20240508035907209.png)

### Fair Value of Equity Call Option (Strike K and Maturity T < T) Fair Value of Equity
$$E_{t}=\text{EquityValue}(T)=e^{-r\cdot(T-t)}\cdot\mathbb{E}\left[\left(A_{T}-K\right)^{+}\,|\mathcal{F}_{t}\right]\tag{40}$$ 
$$=\text{Call}\left(A_{t}, K, T-t, \sigma_{A}, r\right).$$

Fair Value of Equity Call derived from payoff function:
$$\text{EquityCall}\left(E_{0}, k, t\right)=e^{-r\cdot t}\cdot\mathbb{E}\left[\left(E_{t}-k\right)^{+}\,|\mathcal{F}_{0}\right]\tag{41}$$
$$=e^{-r\cdot t}\cdot\mathbb{E}\left[\left(\text{Call}\left(A_{t}, K, T-t, \sigma_{A}, r\right)-k\right)^{+}\,|\mathcal{F}_{0}\right].$$

Value obtained by 1-dimensional integration of the call function vs the log-normal density of $A_{t}$.

## Implied Volatility Surfaces
- Classic [Black-Scholes model](../Financial%20Instruments/Black%20Scholes%20Derivation.md) assumes constant [stock price volatility](../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%205%20Options%20on%20Prices%20and%20Hedge-Based%20Valuation/Black-Scholes%20Model%20and%20Extensions.md) (flat across strikes and maturities)
- [Implied Volatility](../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%205%20Options%20on%20Prices%20and%20Hedge-Based%20Valuation/A%20Real-Life%20Option%20Pricing%20Exercise.md) Surfaces observed in the market are not flat, they exhibit "vol skew" + "vol smile"
- Equity volatilities in the [Capital Structure](../Advanced%20Financial%20Analysis%20and%20Valuation/Introduction%20to%20Corporate%20Finance.md) model are stochastic and generate implied vol surfaces similar to ones observed in the market
- This is due to:
	- the equity volatility [leverage](../Advanced%20Investments/Lecture%206-Leverage,%20Tail%20Risk,%20Volatility%20Products.md) effect (equity down ⇒ vol up) and
	- the "fat tails" of the equity price distribution (caused by non-zero company [leverage](../Advanced%20Investments/Lecture%206-Leverage,%20Tail%20Risk,%20Volatility%20Products.md))

## Equity Volatility Surface in Structural Credit Model

![500](Credit%20Markets%20Session%205-20240508040030505.png)

## Modern Capital Structure Arbitrage Models

Inputs:
- [Term structure](../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%209/The%20Vasicek%20Model.md) of risk-free [interest rates](../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%202/Interest%20Rate%20Quotations.md)
- Detailed assets and ([term structure](../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%209/The%20Vasicek%20Model.md) of) liabilities information from the balance sheet of a company
- Equity market prices
- Equity [volatility surface](../Financial%20Engineering/7.%20Black%20Scholes%20Model.md)

Outputs:
- Implied Asset value levels and volatilities (via [leverage](../Advanced%20Investments/Lecture%206-Leverage,%20Tail%20Risk,%20Volatility%20Products.md))
- Model implied probabilities of default to various maturities / "Distance to Default" metrics
- Implied prices for CDS and risky [Corporate Bonds](../Financial%20Markets%20and%20Institutions/II.%20The%20Roles%20of%20Banks%20and%20Derivative%20Markets%20in%20Resolving%20Problems%20Inherent%20in%20Debt%20Contracts/Class%202-%20Debt%20Contracts%20due%20to%20Lack%20of%20Information/Class%20Notes%202%20–%20Corporate%20Bond%20Contracts.md) (hazard rate curve)
- Implied prices for convertible bonds

## Inverse Capital Structure Arbitrage Models

Inputs:
- [Term structure](../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%209/The%20Vasicek%20Model.md) of risk-free [interest rates](../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%202/Interest%20Rate%20Quotations.md)
- Detailed assets and ([term structure](../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%209/The%20Vasicek%20Model.md) of) liabilities information from the balance sheet of a company
- Equity market prices
- Market prices for CDS and risky [Corporate Bonds](../Financial%20Markets%20and%20Institutions/II.%20The%20Roles%20of%20Banks%20and%20Derivative%20Markets%20in%20Resolving%20Problems%20Inherent%20in%20Debt%20Contracts/Class%202-%20Debt%20Contracts%20due%20to%20Lack%20of%20Information/Class%20Notes%202%20–%20Corporate%20Bond%20Contracts.md) (hazard rate curve)

Outputs:
- Implied Asset value levels and volatilities (via [leverage](../Advanced%20Investments/Lecture%206-Leverage,%20Tail%20Risk,%20Volatility%20Products.md))
- Credit Implied equity [volatility surface](../Financial%20Engineering/7.%20Black%20Scholes%20Model.md) / model implied prices for all equity options

## Capital Structure Arbitrage Strategy: Main Idea
- Identify dislocations across the [capital structure](../Advanced%20Financial%20Analysis%20and%20Valuation/Introduction%20to%20Corporate%20Finance.md) of a company
- Monetize dislocations via credit vs equity vs options "[Capital Structure](../Advanced%20Financial%20Analysis%20and%20Valuation/Introduction%20to%20Corporate%20Finance.md) [Arbitrage](../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%207/Arbitrage%20Pricing%20of%20Derivatives.md)" trades
- Trade examples
	- Risky bonds & CDS vs equity
	- Risky bond & CDS vs equity options
	- Convertible bonds vs equity & equity options

## How Can We Hedge the AMC 2025 Bond Against Default?

![500](Credit%20Markets%20Session%205-20240508040339873.png)

# AMC 2025 Bond: Implied Volatility Surface

![500](Credit%20Markets%20Session%205-20240508040356751.png)

## AMC 2025 Bond: Recovering from Distressed Levels

![500](Credit%20Markets%20Session%205-20240508040415900.png)

## Capital Structure Arbitrage Strategy Example
- Buy short-dated AMC 2025 bond with maturity T
- Buy AMC out of the money Put option with strike k and maturity t close to T
- Positive/No Default Scenario PnL analysis
	- bond price increases to 100
	- bond coupons collected until T
	- option price decreases to 0
- Negative/Default Scenario PnL analysis
	- bond price drops to recovery value R
	- option price increases to k
- If equity and vol markets are dislocated from [credit markets](Credit%20Markets%20Session%201.md): we can construct an [arbitrage](../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%207/Arbitrage%20Pricing%20of%20Derivatives.md) [portfolio](../Advanced%20Investments/An%20Asset%20Allocation%20Primer.md), with positive PnL outcomes in both scenarios!

## Idiosyncratic vs. Systematic/Market Risks
- Main idea: decompose the Gaussian [risk factors](../Financial%20Instruments/Assignments/PSET%206-%20Financial%20Instruments.md) $W^i$ driving the company assets $A^i$ into
	- idiosyncratic risk $Z_i$ (specific for company $i$) and
	- systematic/[market risk](../Financial%20Engineering/Derivatives/Part%20I%20-%20Forwards%20and%20Futures/Chapter%205%20-%20Index%20Futures.md) $X$ (common to all companies)
- The portion of systematic/market factor risk in $W^i_t$ (and $A^i_t$) controlled via Gaussian correlation coefficient $\rho^i$:
$$\text{Corr}\left(W_{T}^{i}, X\right)=\rho_{i}\in[-1, 1]\tag{42}$$
$$W_{T}^{i}=\sqrt{T}\cdot\left(\sqrt{1-\rho_{i}^2}\cdot Z^{i}+\rho_{i}\cdot X\right)\tag{43}$$
$$X, Z_{i}\sim\mathcal{N}\left(0, 1\right), \ \ X\perp Z_{j}, \ \ Z_{i}\perp Z_{j}, i\neq j\tag{44}$$

### Assets Cross-Correlations: Via Common Market Factor
- Assets become explicitly dependent on the level of the common market factor $X$:
$$A^i_T = A^i_0 \cdot \exp \left(\left(r - \frac{1}{2} \sigma^2_i \right) T + \sigma_i \cdot W^i_T \right)\tag{45}$$
$$= A^i_0 \cdot \exp \left(\left(r - \frac{1}{2} \sigma^2_i \right) T + \sigma_i \cdot \sqrt{T} \cdot (\sqrt{1-\rho_i^2} \cdot Z^i + \rho_i \cdot X) \right)\tag{46}$$
- **Cross-correlations between assets $A^i_T$ and $A^j_T$ given by**
$$\text{Corr}(A^i_T, A^j_T) = \rho_i \cdot \rho_j, \quad i \neq j\tag{47}$$
- $A^i_T$ and $A^j_T$ are independent, conditional on $X$

### Survival Probability Formulas
- **Unconditional survival probabilities $p'$:**
$$p' = \mathbb{P}[\tau_i \geq T] = \mathbb{P}[A^i_T > K_i]\tag{48}$$
$$= \mathbb{P} \left[\frac{W^i_T}{\sqrt{T}} < d'_i \right] = \Phi(d'_i), \tag{49}$$
$$d'_i = \Phi^{-1}(p')\tag{50}$$
- **Conditional survival probabilities $p'_x$:**
$$p'_x:= \mathbb{P}[\tau_i \geq T \mid X = x] = \mathbb{P} \left[\frac{W^i_T}{\sqrt{T}} < d'_i \mid X = x \right]\tag{51}$$
$$= \mathbb{P} \left[\sqrt{1-\rho_i^2} \cdot Z^i + \rho_i \cdot x < d'_i \mid X = x \right]\tag{52}$$
$$= \mathbb{P} \left[Z^i < \frac{d'_i - \rho_i \cdot x}{\sqrt{1-\rho^2_i}} \right] = \Phi \left(\frac{d'_i - \rho_i \cdot x}{\sqrt{1-\rho^2_i}} \right)\tag{53}$$

## Correlated Defaults Measuring Joint Credit Defaults
- Conditional on $X$, default times $\tau_i$ are independent, hence
$$\mathbb{P}\left[\tau_{i}>T, \tau_{j}>T|X=x\right]=p_{x}^{i}\cdot p_{x}^{j}\tag{54}$$
- Joint credit survival/[default probabilities](Credit%20Markets%20Session%203.md) ($\varphi=\Phi^{\prime}$):
$$\mathbb{P}\left[\tau_{i}>T, \tau_{j}>T\right]\tag{55}$$
$$=\int_{-\infty}^{\infty}\mathbb{P}\left[\tau_{i}>T, \tau_{j}>T|X=x\right]\cdot\varphi\left(x\right)dx\tag{56}$$
$$=\int_{-\infty}^{\infty}p_{x}^{i}\cdot p_{x}^{j}\cdot\varphi\left(x\right)dx\tag{57}$$
$$ = \int_{-\infty}^\infty \Phi \left(\frac{d'_i - \rho_i \cdot x}{\sqrt{1-\rho^2_i}} \right) \cdot \Phi \left(\frac{d'_j - \rho_j \cdot x}{\sqrt{1-\rho^2_j}} \right) \cdot \phi(x) \, dx\tag{58}$$

## Pools of Homogeneous Credit Issuers

Simple case: we assume that the underlying pool consists of n homogeneous credit issuers, i.e. with identical:

- notionals $\frac{1}{n}$,
- "distance to default" coefficients $d_-$,
- recovery rates $R$,
- market correlations $\rho$

The total pool loss $L_T$ at time T is given by
$$L_{T}=\frac{(1-R)}{n}\cdot\sum_{i=1}^{n}\mathbb{I}_{\{\tau_{i}\leq T\}}\tag{59}$$

## Conditional Credit Events: "K Out of N" Defaults
- We are interested in counting the number of defaults in the pool, conditional on the market factor X
- Conditional default events are independent and Bernoulli distributed
$$\mathbb{I}_{\{\tau_{i}\leq T\}}|X=x\sim\text{Bernoulli}\left(1-p_{x}\right)\tag{60}$$

Therefore, their sum follows the [Binomial](../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%205%20Options%20on%20Prices%20and%20Hedge-Based%20Valuation/A%20Real-Life%20Option%20Pricing%20Exercise.md) distribution
$$\sum_{i=1}^{n}\mathbb{1}_{\{\tau_{i}\leq T\}}|X=x\sim \text{Binomial}\left(n, 1-p_{x}\right), \tag{61}$$
$$\mathbb{P}\left[\sum_{i=1}^{n}\mathbb{1}_{\{\tau_{i}\leq T\}}=k|X=x\right]=\binom{n}{k}\cdot\left(1-p_{x}\right)^{k}\cdot p_{x}^{n-k}\tag{62}$$

## Joint/Correlated Credit Events: "K Out of N" Defaults
- We are interested in counting the number of defaults in the pool, as well as the distribution of the pool loss $L_T$ at T
$$\mathbb{P}\left[L_{T}=k\cdot\frac{(1-R)}{n}\right]=\mathbb{P}\left[\sum_{i=1}^{n}\mathbb{I}_{\{\tau_{i}\leq T\}}=k\right]\tag{63}$$
$$=\int_{-\infty}^{\infty}\mathbb{P}\left[\sum_{i=1}^{n}\mathbb{I}_{\{\tau_{i}\leq T\}}=k|X=x\right]\cdot\varphi\left(x\right)dx\tag{64}$$
$$=\int_{-\infty}^{\infty}\binom{n}{k}\cdot\left(1-p_{x}\right)^{k}\cdot p_{x}^{n-k}\cdot\varphi\left(x\right)dx\tag{65}$$
- Therefore, in the homogeneous case, the pool loss distribution $L_{T}$ can be computed explicitly... and depends on the Gaussian correlation coefficient $\rho$!

## Loss Distribution $L_T$ for General (Non-Homogeneous) Pools
1. Calibrate "distance to default" coefficients $d^i_{-}$ from market data (from survival probabilities to maturity T)
2. Estimate the level of expected "Recovery Given Default" coefficients $R_i$, on a 1% discretization grid
3. Estimate the correlation levels $\rho_i$ of assets $A_i$ with the systematic/market factor $X$
4. Discretize the distribution of the market factor $X$ on a grid $\{(x_j)\}_{j=1..J}$ (also works for general, non-Gaussian $X$)
5. Compute the conditional distribution of $L_T|x_j$ on a 1% discretization grid, via numerical "convolution"
6. Aggregate the distribution of $L_T$ as a weighted sum of conditional distributions: $\sum_j P [X = x_j] \cdot L_T|x_j$

## What is a Collateralized Debt Obligation/CDO?
- A derivative/"structured" credit product linked to an underlying/collateral pool of risky assets
- Example of underlying pool assets:
	- [Corporate Bonds](../Financial%20Markets%20and%20Institutions/II.%20The%20Roles%20of%20Banks%20and%20Derivative%20Markets%20in%20Resolving%20Problems%20Inherent%20in%20Debt%20Contracts/Class%202-%20Debt%20Contracts%20due%20to%20Lack%20of%20Information/Class%20Notes%202%20–%20Corporate%20Bond%20Contracts.md),
	- Corporate Loans,
	- Mortgage backed securities/MBS,
	- CDS, etc
- Underlying pool notional divided into tranches, corresponding to various level of risk (usually credit rated by rating agencies)
- CDO Tranche cash-flows defined via from underlying pool cash-flows via structural subordination waterfall
- CDO has contractual coupon c and maturity T

## CDX IG Index Tranche Summary (CDX IG 5Y S41)

![500](Credit%20Markets%20Session%205-20240508042703014.png)

## More Details on CDO Tranches
- Each CDO Tranche is characterized by an interval [a, d]:
	- a is the attachment point of the tranche,
	- d is the detachment point of the tranche,
	- a and d are expressed in % of the underlying pool notional
- Cumulative portfolio cash-flows, both coupons and losses, are assigned to tranche cash-flows via "waterfall" logic
- CDO [fixed leg](../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%202/Pricing%20Interest%20Rate%20Swaps.md) pays the contractual coupon c on the outstanding Tranche notional (adjusted for defaults)
- Tranche detachment points are adjusted for realized defaults

## Synthetic CDX IG Index Tranches
- Uses CDX IG Index as underlying pool
- Each tranche "behaves" like a CDS with dynamic face notional!
	- Equity [0%, 3%]: highest level of risk (B), "first pool losses"
	- Mezzanine [3%, 7%], intermediate (BBB) risk
	- Senior [7%, 15%], senior (AA) level of risk
	- Super-Senior [15%, 100%], super-senior (AAA) level of risk
	- Equity + Mezzanine + Senior + Super-Senior = Total Pool

## Credit Risk Details for Underlying Pool Instruments
- Synthetic pool: equally weighted basket of n CDS instruments, e.g. CDX IG index basket
- Total notional of the pool normalized to 1, i.e. each CDS notional is $\frac{1}{n}$
- CDS issuer default times $\tau_i$, $i = 1..n$ 
- CDS issuer expected default recoveries $R_i, i = 1..n$
- Default Loss Given Default payments are
$$L_{i}=\frac{1}{n}\cdot(1-R_{i})\, , i=1..n\tag{66}$$

## CDO Tranches: Structural Subordination "Waterfall" Logic

![500](Credit%20Markets%20Session%205-20240508043040259.png)

## CDO "Waterfall" Logic for Tranche Default Leg
- Cumulative losses in the pool at time $t\in[0, T]$ given by
$$L_{t}=\frac{1}{n}\cdot\sum_{i=1}^{n}\left(1-R_{i}\right)\mathbb{1}_{\{\tau_{i}\leq t\}}, \, L_{0}=0\tag{67}$$
- Cumulative losses in the [a, d] tranche at time $t \in [0, T]$
$$L_{t}^{[a, d]}=\left(L_{t}-a\right)^{+}-\left(L_{t}-d\right)^{+}=L_{t}^{[0, d]}-L_{t}^{[0, a]}\tag{68}$$
- Notice that $L_{t}^{[a, d]}, t \leq T$ is a discrete jump process paying the [portfolio](../Advanced%20Investments/An%20Asset%20Allocation%20Primer.md) losses within the $[a, d]$ tranche until maturity $T$
- Maximum loss on [a, d] tranche is d − a (tranche "wipe-out")

## CDO "Waterfall" Logic for Tranche Premium Leg
- Outstanding/non-defaulted [a, d] tranche notional at time t
$$\mathcal{N}_{t}^{[a, d]}=d-a-L_{t}^{[a, d]}=\mathcal{N}_{t}^{[0, d]}-\mathcal{N}_{t}^{[0, a]}\tag{69}$$
- Premium leg cash-flow payments for the [a, d] tranche occur on (quarterly) cash-flow times $\{T_k\}, k = 1..K$
- ... on the outstanding tranche notional $\mathcal{N}^{[a, d]}_{T_k}$ at time $T_k$: 
$$C_{k}^{[a, d]}=c\cdot\Delta T_{k}\cdot \mathcal{N}_{T_{k}}^{[a, d]}=c\cdot\Delta T_{k}\cdot\left(\mathcal{N}_{T_{k}}^{[0, d]}-\mathcal{N}_{T_{k}}^{[0, a]}\right)\tag{70}$$
- Maximum premium leg payment on $[a, d]$ tranche is $c\cdot\Delta T_{k}\cdot(d-a)$, minimum payment is 0 (tranche "wipe out")

## CDO [a, d] Tranche Pricing: Premium Leg

Present Value Of Premium/[Fixed Leg](../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%202/Pricing%20Interest%20Rate%20Swaps.md) Is Given By
$$PV_{CDO\_PL}(0)=\mathbb{E}\left[\sum_{k=1}^{K}DF(0, T_{k})\cdot c\cdot\Delta T_{k}\cdot \mathcal{N}_{T_{k}}^{[a, d]}\right].\tag{71}$$
$$=c\cdot\sum_{k=1}^{K}DF(0, T_{k})\cdot\Delta T_{k}\cdot\mathbb{E}\left[\mathcal{N}_{T_{k}}^{[a, d]}\right]\tag{72}$$ 
$$=c\cdot\sum_{k=1}^{K}DF(0, T_{k})\cdot\Delta T_{k}\cdot\left(d-a-\mathbb{E}\left[L_{T_{k}}^{[a, d]}\right]\right)\tag{73}$$

## CDO [a, d] Tranche Pricing Present Value and Par Spread of the [a, d] Tranche
$$PV_{CDO}(0)=PV_{CDO\_DL}(0)-PV_{CDO\_PL}(0), \tag{77}$$
$$ParSpread_{CDO}(0)=c\cdot\frac{PV_{CDO\_DL}(0)}{PV_{CDO\_PL}(0)}\tag{78}$$

In practice, we need to compute the "Expected Tranche Loss" at each premium payment time $\{T_{k}\}$, $k=1..K$
$$\mathbb{E}\left[L_{T_{k-1}}^{[a, d]}\right]=\mathbb{E}\left[\left(L_{T_{k}}-a\right)^{+}\right]-\mathbb{E}\left[\left(L_{T_{k}}-d\right)^{+}\right]\tag{79}$$
... which can be computed explicitly from the distribution of the pool loss $L_{T_{k}}$

## Base Correlation Model for Quoting CDO Tranches
- Start with a pool of credit issuer and calibrate the "distance to default" coefficients $d^i_{-}$
- For a given Gaussian correlation coefficient $\rho$, one can consistently price all CDO equity tranches
- Convert the market prices for mezzanine and senior tranches into "equity equivalent" tranches (tranche linearity)
- Calibrate the "base" tranche correlations $\rho_i$ matching the prices of "equity equivalent" tranches
- The calibrated "base" correlations are used as market convention for quoting CDO tranches
- Observation: the "base" correlation model for [pricing](../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%207/Arbitrage%20Pricing%20of%20Derivatives.md) CDOs is not consistent for mezzanine and senior tranches!

## CDOs in the GFC (2008-2009) Financial Crisis
- During the GFC (2008-2009) [financial crisis](../Financial%20Markets%20and%20Institutions/III.%20Liquidity%20of%20Assets/Class%209-%20Bailouts%20and%20Bank%20Failures/Squam%20Lake%20Group%20Letter.md), various pools underlying CDO contracts experienced realized defaults. In particular, pools consisting of mortgage and [asset backed securities](../Financial%20Engineering/Derivatives/Part%20X%20-%20Credit%20Derivatives/Chapter%2043%20-%20Securitisation,%20ABSs%20and%20CDOs.md) were severely impacted in the real estate crisis
- Synthetic CDOs linked to CDX IG and HY (North America) indices also experienced unprecedented [default rates](../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%2014/Default%20Rates%20Recovery%20Rates%20and%20Credit%20Losses.md)
- In many cases, investors in senior (AA) and super-senior (AAA) tranches were partially wiped out!
- Failures of understanding risks were amplified by the market-wide use of an inconsistent, non-realistic CDO model:
	- Gaussian correlation models do not cover properly "fat tail" risks/"clustering" of defaults events!

## Q&A
- Assets/Liabilities of a company
- [Black-Scholes model](../Financial%20Instruments/Black%20Scholes%20Derivation.md)
- [Capital Structure](../Advanced%20Financial%20Analysis%20and%20Valuation/Introduction%20to%20Corporate%20Finance.md) / [Merton model](.md)
- Correlated Defaults
- CDO [Pricing](../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%207/Arbitrage%20Pricing%20of%20Derivatives.md)
- Appendix: First Passage/Black-Cox model

## First Passage Time Credit Model: Black & Cox '76
- Model introduces a "default barrier" parameter D
- Barrier D chosen below the liabilities level K, in order to protect bond investors from excessive losses
- Credit default triggered when assets $A_t$ fall through the liabilities level $K$ and cross the default barrier $D_t$.
- In that case, equity investors get "wiped out" and the bond holders take over the assets of the company.
- Assets still liquidated at time T to repay the bond investors.

## Possible Paths of Asset Values Relative to Liabilities

![500](Credit%20Markets%20Session%205-20240508043846006.png)

## Equity and Bond Investor's Payout
- We denote the running minimum of the asset process $A_{t}$ as
$$A_{t}^{*}=\min\{A_{s}:0<s<t\}\tag{80}$$
- Equity investors payout at $T$ defined as
$$\text{EquityPayout}=\left(A_{T}-K\right)^{+}\cdot\mathbb{1}_{\{A_{T}^{*}\geq D\}}\tag{81}$$
- Bond investors payout at $T$ is
$$\begin{array}{l}\text{BondPayout}=A_{T}-\text{EquityPayout}\\ =K-(K-A_{T})^{+}+(A_{T}-K)^{+}\cdot\mathbb{1}_{\{A_{T}^{*}<D\}}\end{array}\tag{82}$$

## Valuation: Down-and-Out Barrier Options Formulas

### First Passage Time Model: Pricing Formulas
- Fair value of equity priced as an down-and-out Call option on the assets value with strike $K$, barrier $D$ and maturity $T$
$$E_{0}=e^{-r\cdot T}\cdot\mathbb{E}\left[(A_{T}-K)^{+}\cdot\mathbb{I}_{\{A_{T}^{*}\geq D\}}|\mathcal{F}_{0}\right]\tag{83}$$
- Price is known explicitly in the [Black-Scholes](../Financial%20Engineering/Mathematical%20Modeling%20of%20Derivative%20Pricing.md) framework ("down-an-out" barrier option)
- Fair value of risky bond derived from equity price 
- Fair value of a risky bond higher in "first passage time model" vs. "classical structural model", due to additional value from the barrier option
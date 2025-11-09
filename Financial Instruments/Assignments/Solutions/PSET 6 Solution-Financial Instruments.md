---
linter-yaml-title-alias: Solution to Homework 6
title: Solution to Homework 6
tags:
  - black_scholes_merton
  - call_option
  - implied_volatility
  - sp500
  - structured_security
aliases:
  - BMS implied volatility
  - Homework 6 Solution
key_concepts:
  - Black-Scholes model
  - Implied volatility calculation
  - Option pricing
  - PLUS security payoff
  - Structured security valuation
---

# Solution to Homework 6

## 1. Implied Volatility

From the CBOE site I extract options prices with expiration of February 21, 2024 and compute “mid" prices as an average of [bid and ask](../../../Financial%20Markets%20and%20Institutions/III.%20Liquidity%20of%20Assets/Class%205-%20Private%20Information,%20Liquidity,%20and%20Securitization/Class%20Note%209%20Bid%20and%20Ask%20Prices%20With%20Private%20Information.md). To compute the [Black-Scholes](../../../Financial%20Engineering/Mathematical%20Modeling%20of%20Derivative%20Pricing.md)-[Merton](../../../Credit%20Markets/Credit%20Markets%20Session%205.md) (BSM) [implied volatility](../../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%205%20Options%20on%20Prices%20and%20Hedge-Based%20Valuation/A%20Real-Life%20Option%20Pricing%20Exercise.md) I need the maturity,  the continuously compounded risk free rate $7^{\prime}$ and the continuously compounded dividend yield $y$.Let $T=0.35$ (365 days in a year and 129 days to maturity). From the Federal Reserve website the annually compounded 3 months constant maturity rate was $r_{1}(0.25)=5.43\%$ on February 12 (some interpolation could be done here. Any reasonable extraction is fine!). Converting this to [continuous compounding](../../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%202/Interest%20Rate%20Quotations.md) units gives $r(0.25)=ln\left(1+r_{1}(0.25)/4\right)\times4=5.39\%$ From Robert Shiller's dataset,  the January 2021 to June 2023 average dividend yield (annually compounded) was equal to $y_{1}=1.51\%$,  which,  converted into [continuous compounding](../../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%202/Interest%20Rate%20Quotations.md) units,  gives $y=1.50\%$

The BSM [implied volatility](../../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%205%20Options%20on%20Prices%20and%20Hedge-Based%20Valuation/A%20Real-Life%20Option%20Pricing%20Exercise.md) is computed using solver (I use Matlab,  but Excel does exactly the same calculation but takes a bit more time unless you know how to use macros). The results are shown Figure 1 for moneyness from 08 to 1.1
![500](Attachments/500-136.png)

Figure 1: [Implied volatility](../../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%205%20Options%20on%20Prices%20and%20Hedge-Based%20Valuation/A%20Real-Life%20Option%20Pricing%20Exercise.md) for June 21,  2024 S&P500 call and call options

As you can see the volatility is not constant.but it is decreasing with the monevness of the option (as in the Figure from Teaching Note 6).

The [PLUS security](../PSET%206-%20Financial%20Instruments.md) has one-year to maturity with embedded call options so it would be nice to have [implied volatility](../../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%205%20Options%20on%20Prices%20and%20Hedge-Based%20Valuation/A%20Real-Life%20Option%20Pricing%20Exercise.md) for a one-year maturity. I use the February 2025 options (maturity of 12 months) (don't worry if you didn't do this!). [Implied volatility](../../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%205%20Options%20on%20Prices%20and%20Hedge-Based%20Valuation/A%20Real-Life%20Option%20Pricing%20Exercise.md) from the June 2024 and February 2025 call options with $r(1)=4.8\%$ (from the one-year constant maturity yield) are show in Figure 2.
 ![500](Attachments/500-138.png)

Figure 2: [Implied volatility](../../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%205%20Options%20on%20Prices%20and%20Hedge-Based%20Valuation/A%20Real-Life%20Option%20Pricing%20Exercise.md) for June 2024 and February 2025 S&P500 call options

# 2. Valuing and analyzing a structured security

(1). In order to value the PLUS follow these steps:

- (a) Decompose the PLUS payoff into simpler securities.
	- The payoff of thePLUS security at maturity is$$\pi(T)=\left\{\begin{array}{cc}min\left[10+10\times3\times\left(\frac{S_T-S_0}{S_0}\right), 11.9\right]&\quad if\:S_T>S_0\\10\times\frac{S_T}{S_0}&\quad if\:S_T\leq S_0\end{array}\right.$$
Starting with $S_{T}\leq S_{0}$,  this is just a [long position](../../../Financial%20Engineering/Derivatives/Part%20I%20-%20Forwards%20and%20Futures/Chapter%204%20-%20Futures:%20Hedging%20and%20Speculation.md) in $\frac{10}{S_0}$ units of the index. Let $N$ = $\frac {10}{S_{0}}$ be the number of units of the index determined by this part of the payoff. With the S&P500 at 5, 000.57 N = 0.0020

Finding the payoff for the case when $S_{T}>S_{0}$ is simpler than it first appears. The trick is to plot the payoff and to analyze the chart to determine the basic securities. Figure 3 gives the PLUS payoff for different values of $S_{T}$

 ![500](Attachments/500-134.png)

Figure 3: PLUS payoff decomposition
We see that there are two points where the slope changes. The first point is $S_{0}$ while the second is where:
$$10+10\times3\times\frac{S_T-S_0}{S_0}=11.9$$

This is where $S_{T}=5, 317.27$ Call this point $K_{1}$.After $K_{1}$ the slope is zero. Table 1 reports the slopes of the [PLUS security](../PSET%206-%20Financial%20Instruments.md):
```latex
\begin{document}
\begin{tabular}{|c|c|}
\hline

\textbf{Range}         & \textbf{Slope}                          \\ \hline

$S_T \leq S_0$         & $N = \frac{10}{5, 000.57} = 0.0020$      \\ \hline

$S_0 < S_T \leq K_1$  & $3 \times N = 0.0060$                   \\ \hline

$S_T > K_1$            & 0                                       \\ \hline

\end{tabular}
\end{document}
```

Table 1: Slope of the PLUS for different values of $S_{T}$

Alternatively,  let $N$ be the number of units of the [underlying securities](../../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%207/Rate%20and%20Price%20Trees.md) implicitly held in the [PLUS security](../PSET%206-%20Financial%20Instruments.md).

Table 2 reports the resulting slopes for this position:
```latex
\begin{document}
\renewcommand{\arraystretch}{1.5}
\begin{tabular}{|c|c|}
\hline
\textbf{Range}             & \textbf{Slope} \\ \hline
\(S_T \leq S_0\)   & 1     \\ \hline
\(S_0 < S_T \leq K_1\) & 3     \\ \hline
\(S_T > K_1\)      & 0     \\ \hline
\end{tabular}
\end{document}
```

Table 2: Slope when holding $N$ [underlying securities](../../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%207/Rate%20and%20Price%20Trees.md) for different values of $S_{T}$

So.the pavoff of the PLUS can be rewritten as
$$\pi(T)=N\cdot[S_T+2\cdot max(S_T-S_0, 0)-3\cdot max(S_T-K_1, 0)]$$

The [PLUS security](../PSET%206-%20Financial%20Instruments.md) is long $e^{-y}N$ units of the underlying index. $2N$ units of an at the money call option and short $3N$ units of a call option with [strike price](../../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%205%20Options%20on%20Prices%20and%20Hedge-Based%20Valuation/Call%20and%20Put%20Payoffs%20at%20Expiry.md) $K_{1}$

- (b)Use the Black and Scholes model to price the identified simpler securities.
	- Assuming the PLUS was issued on February 18,  2024,  $N=0.0020$ and $K_{1}=5, 317.27$.
	- To price the at the money option I use the [implied volatility](../../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%205%20Options%20on%20Prices%20and%20Hedge-Based%20Valuation/A%20Real-Life%20Option%20Pricing%20Exercise.md) for a February 2025 call option with strike equal to 5000: $\sigma^{ATM}=17.2\%$.
	- For the OTM option I use the [implied volatility](../../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%205%20Options%20on%20Prices%20and%20Hedge-Based%20Valuation/A%20Real-Life%20Option%20Pricing%20Exercise.md) for a February 2025 call option with strike equal to 5300: $\sigma^{OTM}=15.1\%$
	- The prices of the options are
	$$c^{ATM}=418.26\mathrm{~and~}c^{OTM}=235.01$$
	Hence:$$V^{PLUS}=N\cdot\left[e^{-y}S_{0}+2\cdot c^{ATM}-3\cdot c^{OTM}\right]=10.114$$
- (c) Adjust the parameters to obtain a value equal to the issue price. In the prospectus the security is sold for 10 dollars,  but according to the model the value is actually greater than par. In order to increase its value we can change the [strike price](../../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%205%20Options%20on%20Prices%20and%20Hedge-Based%20Valuation/Call%20and%20Put%20Payoffs%20at%20Expiry.md) of the $({\mathit{DTM}}$ option by decreasing the maximum payoff currently set at 11.9.
- Let $C$ be the maximum payoff.
	- Changing this value implicitly changes the [strike price](../../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%205%20Options%20on%20Prices%20and%20Hedge-Based%20Valuation/Call%20and%20Put%20Payoffs%20at%20Expiry.md),  $K_{1}$,  of the OTM option.
	- The value of $C$ that sets the [PLUS security](../PSET%206-%20Financial%20Instruments.md) value to $\$10$ is $C=11.61$ implying a value of $K_{1}^{\prime}=5, 268.42$.
	- By decreasing $C$ the upside potential of the security is decreased as shown in Figure (4).
 ![500](Attachments/500-135.png)
Figure 4: PLUS payoff change with $C=11.61$

(2) The sensitivity of the PLUS to changes in the underlying is given by
$$\begin{aligned}
\frac{\partial V^{PLUS}}{\partial S}& =\:\frac{\partial N\cdot\left\lfloor S+2\cdot c^{ATM}-3\cdot c^{OTM}\right\rfloor}{\partial S}=  \\
&=\quad N\cdot\left[\frac{e^{-y}\partial S}{\partial S}+2\cdot\frac{\partial c^{ATM}}{\partial S}-3\cdot\frac{\partial c^{OTM}}{\partial S}\right]= \\
&\text{=} N\cdot\left[e^{-y}+2\cdot e^{-y}N\left(d_{1}^{ATM}\right)-3\cdot e^{-y}N\left(d_{1}^{OTM}\right)\right]
\end{aligned}$$
remember that $d_{1}$ is a function of S and $K$ is given by
$$d_1(S, K)=\frac{ln\left(\frac{S}{K}\right)+\left(r-y+\frac{\sigma^2}{2}\right)\cdot T}{\sigma\cdot\sqrt{T}}$$
So$$

d_1^{ATM}=d_1(S, S_0)=\frac{ln\left(\frac{S}{S_0}\right)+\left(r-y+\frac{\sigma^2}{2}\right)\cdot T}{\sigma\cdot\sqrt{T}}

$$$$d_1^{OTM}=d_1(S, K_1)=\frac{ln\left(\frac{S}{K_1}\right)+\left(r-y+\frac{\sigma^2}{2}\right)\cdot T}{\sigma\cdot\sqrt{T}}
$$
- for $S=S_{0}$ we get $e^{-y}N\left(d_{1}^{ATM}\right)=0.621$ and $e^{-y}N\left(d_{1}^{OTM}\right)=0.447$.
- Therefore $\frac{\partial V^{PLUS}}{\partial S}=0.00177$. (In this calculation I used the appropriate [implied volatility](../../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%205%20Options%20on%20Prices%20and%20Hedge-Based%20Valuation/A%20Real-Life%20Option%20Pricing%20Exercise.md) fo each option.)
To compute the beta of the PLUS,  use the formula$$\beta^{PLUS}=\frac{\frac{dV^{PLUS}}{V^{PLUS}}}{\frac{dS}{S}}=\frac{dV^{PLUS}}{dS}\cdot\frac{S}{V^{PLUS}}=0.0020\cdot\frac{S}{V^{PLUS}}$$
that results in$$\beta^{PLUS}=0.0020\cdot\frac{5000.57}{10.114}=0.88$$
which is less than 1. At the current level of the S&P500 the security is less risky than the S&P500 itself

Computing the value of beta for different values of S (keeping the same impliec volatilities used to compute option prices)and for different times to maturity(see Figure 5)，we see that as we approach maturity,  the beta of the PLUS increases substantially in the region between $S_{0}$ and $K_{1}$

This happens because between $S_{0}$ and $K_{1}$ the [PLUS security](../PSET%206-%20Financial%20Instruments.md) is a leveraged [investment](../../../Advanced%20Investments/An%20Asset%20Allocation%20Primer.md) (the slope of the payoff increases in that region since the at the money option becomes in the money).In may be helpful to see how the value of the security changes when the value of the underlying changes at different points in time. This is shown in Figure 6.
 ![500](Attachments/500-133.png)

Figure 5: PLUS beta for different values of $S$ and $t$

 ![500](Attachments/500-137.png)

Figure 6:PLUS value for different values of S and $t$
---
title: Appendix 22. C Risk-Neutral Pricing and Marginal Utility in the Binomial Model
tags:
  - binomial_model
  - marginal_utility
  - risk_averse
  - risk_neutral_pricing
  - stochastic_discount_factor
aliases:
  - Binomial Pricing
  - Risk-Neutral Valuation
key_concepts:
  - Marginal utility of consumption
  - Physical probabilities valuation
  - Risk-neutral binomial pricing
  - Risk-neutral probabilities
  - Risky stock and bond
  - Stochastic discount factors
---

# Appendix 22. C Risk-Neutral Pricing and Marginal Utility in the Binomial Model

This appendix links the discussion in this chapter to that in Appendix 11. B We now see how the concepts we have just discussed arise in the [binomial model](../../Financial%20Instruments/Lecture%20Notes-%20Financial%20Instruments/Teaching%20Note%204-Multiperiod%20Binomial%20Trees/Binomial%20Option%20Pricing.md). The discussion in this section builds on Appendix 11. B. There are two assets,  a risky stock and a risk-free bond. Investorsare risk-averse,  there is one period and two [possible outcomes](../../Financial%20Markets/Financial%20Asset%20Pricing%20Theory%20Overview/Chapter%202%20-%20Uncertainty,%20Information,%20and%20Stochastic%20Processes/Probability%20Space.md): a high [stock price](../Derivatives/Part%20IV%20-%20Options/Chapter%2016%20-%20Black–Scholes%20Model.md) (the good state) and a low [stock price](../Derivatives/Part%20IV%20-%20Options/Chapter%2016%20-%20Black–Scholes%20Model.md) (the bad state). The payoff to the risky stock is $S_{\mathrm{l}}^{H}$ in the high state,  which occurs with probability $p^{H}$ ,  and $S_{\mathrm{l}}^{L}$ in the low state,  with probability $p^{L}=1-p^{H}$ The investor receives a [marginal utility of consumption](.md) today of $U_{0}^{\prime}(C_{0})$. In the future,  if the high state occurs then the investor consumes $C_{\mathrm{l}}^{H}$ and obtains a marginal utility of ${} U_{\mathrm{l}}^{\prime}(C_{\mathrm{l}}^{H}) {}$. In the low state,  the investor consumes $C_{\mathrm{l}}^{L}$ and obtains a marginal utility of $U_{\mathrm{l}}^{\prime}(C_{\mathrm{l}}^{L})$. As we have discussed,  these consumption levels are consequences of the decisions the investor makes about how much to consume and how to invest savings. We simply take the outcome of this decision process for granted.
## Valuing the Stock and Bond with Physical Probabilities

We can directly apply the formulas from the preceding sections to value the stock and bond. It simplifies notation to define the marginal utility ratios $\chi^{H}=U_{\mathrm{l}}^{\prime}(C_{\mathrm{l}}^{H})/U_{0}^{\prime}(C_{0})$ and $\chi^{L}=U_{1}^{\prime}(S_{1}^{L})/U_{0}^{\prime}(C_{0})$ The values $\chi^{H}$ and $x^{L}$ are the stochastic discount factors for the high and low state. The value of the stock at time I will be either $S_{\mathrm{l}}^{H}$ or $S_{\mathrm{l}}^{L}$ . Using equation (22.5),  the value of the stock at time 0 is
$$\begin{gathered}
S_{0}=\operatorname{E}_{0}\left[{\frac{U_{1}^{\prime}(C_{1})}{U_{0}^{\prime}(C_{0})}}S_{1}\right] =p^{H}\left[\frac{U_{1}^{\prime}(C_{1}^{H})}{U_{0}^{\prime}(C_{0})}S_{1}^{H}\right]+p^{L}\left[\frac{U_{1}^{\prime}(C_{1}^{L})}{U_{0}^{\prime}(C_{0})}S_{1}^{L}\right] \\
=p^{H}\chi^{H}S_{1}^{H}+p^{L}\chi^{L}S_{1}^{L} 
\end{gathered}$$

The value of the bond at time 0 is
$$\begin{gathered}
B_{0}=\operatorname{E}_{0}\left[{\frac{U_{1}^{\prime}(C_{1})}{U_{0}^{\prime}(C_{0})}}B_{1}\right] =p^{H}\left[\frac{U_{1}^{\prime}(C_{1}^{H})}{U_{0}^{\prime}(C_{0})}B_{1}\right]+p^{L}\left[\frac{U_{1}^{\prime}(C_{1}^{L})}{U_{0}^{\prime}(C_{0})}B_{1}\right] \\
=p^{H}\chi^{H}B_{1}+p^{L}\chi^{L}B_{1} 
\end{gathered}$$

Equations (22.50) and (22.51) present stock and bond valuations using the [stochastic discount factor](../../Financial%20Markets/Financial%20Asset%20Pricing%20Theory%20Overview/Chapter%204%20-%20State%20Prices/Definitions%20and%20Immediate%20Consequences.md) and physical probabilities

### Risk-Neutral Valuation

Using the [change of measure](../../Financial%20Markets/Financial%20Asset%20Pricing%20Theory%20Overview/Chapter%2011%20-%20Risk-adjusted%20probabilities/Change%20of%20Probability%20Measure.md) result from section 22.3,        we can pick the bond as numeraire and define a new [Probability Distributions](Lecture%201-%20[[Exercises) of [Returns](../../Financial%20Markets/Financial%20Asset%20Pricing%20Theory%20Overview/Chapter%203%20-%20%20Assets,%20Portfolios,%20and%20Arbitrage/Assets.md)|probability distribution]]. We accomplish this by multiplying and dividing by the price ratio $B_{1}/B_{0}$ in equation (22.50):
$$\begin{aligned}
S_{0}& =B_{0}\mathrm{E}_{0}\left[\frac{U_{1}^{\prime}(C_{1})B_{1}}{U_{0}^{\prime}(C_{0})B_{0}}\frac{S_{1}}{B_{1}}\right] \\
&=B_{0}\left(\left[p^{H}\chi^{H}\frac{B_{1}}{B_{0}}\right]\frac{S_{1}^{H}}{B_{1}}+\left[p^{L}\chi^{L}\frac{B_{1}}{B_{0}}\right]\frac{S_{1}^{L}}{B_{1}}\right)
\end{aligned}$$

This valuation uses the physical probabilities,        $p^{H}$ and $p^{L}$ ,        and marginal utilities. Now define new probabilities $\hat{p}^{H}$ and $\hat{p}^{L}$
$$\hat{p}^{H}=p^{H}\chi^{H}\frac{B_{1}}{B_{0}}\\\hat{p}^{L}=p^{L}\chi^{L}\frac{B_{1}}{B_{0}}$$

We have to make sure that these are legitimate probabilities.They are nonnegative because physical probabilities,        marginal utilities,        and bond prices are nonnegative. We can also verify that they sum to 1:
$$\begin{aligned}
\hat{p}^{H}+\hat{p}^{L}& =p^{H}\chi^{H}\frac{B_{1}}{B_{0}}+p^{L}\chi^{L}\frac{B_{1}}{B_{0}} \\
&=\frac{1}{B_{0}}\left[p^{H}\chi^{H}B_{1}+p^{L}\chi^{L}B_{1}\right]=1
\end{aligned}$$

The last equality follows from equation (22.51)

We can substitute equations (22.53) and (22.54) into equation (22.52),        and using the fact that $B_{0}/B_{\mathrm{l}}=1/(1+r)$ ,        the result is
$$S_0=\frac{1}{1+r}\left[\hat{p}S_1^H+(1-\hat{p})S_1^L\right]$$

This is [risk-neutral binomial pricing](.md):Compute the expected [stock price](../Derivatives/Part%20IV%20-%20Options/Chapter%2016%20-%20Black–Scholes%20Model.md) using the [risk neutral probability](../../Financial%20Instruments/Review%20Session%20Notes/Binomial%20Trees%20and%20Option%20Pricing%20MBA.md),        and discount the result at the [risk-free rate](../../Financial%20Instruments/Black%20Scholes%20Derivation.md). The [risk-neutral probabilities](../../Financial%20Instruments/Financial%20Instruments.md) are the physical probabilities weighted by marginal utilities.

This example illustrates how [risk-neutral pricing](../Financial%20Mathematics%20Course.md) permits us to sidestep explicit utility calculations while still performing a correct valuation. [Risk-neutral probabilities](../../Financial%20Instruments/Financial%20Instruments.md) have the property that we obtain the correct time-O value of a security when we compute [expected cash flows](../../Advanced%20Financial%20Analysis%20and%20Valuation/Lecture%20Notes%20Advanced%20Financial%20Analysis%20and%20Valuation/Week%206/Week%206%20Assignment%20Review.md) using those probabilities,        without explicit utility adjustments,        and then discount that expectation at the [risk-free rate](../../Financial%20Instruments/Black%20Scholes%20Derivation.md). This is feasible because instead of utility-weighting the cash flows and computing [expectations](../../Fixed%20Income%20Asset%20Pricing/Fixed%20Income%20Lecture%20Notes/FORWARD%20RATES%20AND%20TERM%20STRUCTURE.md),        we utility-weight the probabilities,        creating new "[risk-neutral probabilities](../../Financial%20Instruments/Financial%20Instruments.md),        A final observation about this example. Note that $U_{\mathrm{l}}^{\prime}(C_{\mathrm{l}}^{H})<U_{\mathrm{l}}^{\prime}(C_{\mathrm{l}}^{L})$ (marginal utility

decreases with consumption). Because of this,        $\hat{p}^{H}<p^{H}$ The effect of utility-weighting the physical probabilities in equation (22.14) is to reduce the probability associated with the high state. Assigning a lower weight to the more valuable outcome has the same effect as using a [discount rate](../../Advanced%20Financial%20Analysis%20and%20Valuation/Problem%20Sets/PSET%207-%20Kohler.md) greater than the [risk-free rate](../../Financial%20Instruments/Black%20Scholes%20Derivation.md),        which is what we do in ordinary DCF valuation.

> [!note] 
> ## BOX 22.3: State Prices
> In the example above,        $\hat{p}^{H}/(1+r)$ is the state price for the event that the economy does well,        and $\hat{p}^{L}/(1+r)$ is the state price for the event that the economy does badly.
> Let $Q^H$ be the price at time 0 of a security that pays $1 when the high state occurs,        and $\varrho^{\tilde{L}}$ the price of a security paying $1 when the low state occurs.* Call these the high and low securities. To understand the economics of a state price,        we can think about marginal utility. If the investor buys an additional unit of the high security,        the additional future [cash flow](../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%201%20-%20Purpose%20and%20Structure%20of%20Financial%20Markets/Preview%20of%20the%20Book.md) is $1 received when the high state occurs. In order to pay for this security,        the investor reduces consumption at time 0 by $Q^H$,       which has a utility cost of $U_0^{\prime}(C_0)Q^H$ In exchange,        the investor receives $1 of extra consumption in the high state,        which has a utility value of $U_1^{\prime}(C^H)\times\$1.$ The utility given up must equal the expected utility received,        so we have
> $$U_0^{\prime}(C_0)Q^H=p\times U_1^{\prime}(C_1^H)\times\$1$$
> We can rewrite this as
> $$Q^{H}=p^{H}\times\chi^{H}\tag{22.55}$$
> Similarly,        we can write the price of the low security as
> 
> $$Q^L=p^L\times\chi^L\tag{22.56}$$
> The variables $\chi^H$ and $\chi^L$ are state-specific discount factors: Cash flows in the high state are discounted by $\chi^H$ and in the low state by $\chi^L.$
> We can now value the bond and the stock. The bond pays $1 in each state. Using the state prices,        we have
> $$B_{0}=[p\times\chi^{H}\times\$1]+[(1-p)\times\chi^{L}\times\$1]\\=Q^{H}\times\$1+Q^{L}\times\$1\text{(22.57)}$$
> Similarly,        the value of the stock is
> $$S_{0}=[p\times\chi^{H}\times S_{1}^{H}]+[(1-p)\times\chi^{L}\times S_{1}^{L}]\\=Q^{H}\times S_{1}^{H}+Q^{L}\times S_{1}^{L}\text{(22.58)}$$
> *These are often called“Arrow-Debreu”securities,        named after Nobel prize-winning economists Kenneth Arrow and Gerard Debreu.

Appendix 11. B presents a numerical example corresponding to this discussion
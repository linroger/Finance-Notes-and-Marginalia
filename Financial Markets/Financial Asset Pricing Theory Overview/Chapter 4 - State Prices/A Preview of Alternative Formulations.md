---
tags:
  - pricing_equation
  - radon_nikodym
  - risk_free_return
  - risk_neutral_probability
  - state_price_deflator
aliases:
  - Alternative Representations
  - Risk-Neutral Valuation
key_concepts:
  - Asset price
  - Radon-Nikodym derivative
  - Risk-free return
  - Risk-neutral probability measure
  - State-price deflator
---

# 4.6 A preview of alternative formulations  

The previous sections show that a [state-price deflator](Exercises.md) is a good way to represent the marketwide [pricing](../../Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%207/Arbitrage%20Pricing%20of%20Derivatives.md) mechanism in a financial market. Paired with characteristics of any individual asset, the state-price defator leads to the price of the asset. This section shows that we can capture the same information in other ways. The [alternative representations](.md) can be preferable for some specific purposes and we will return to them in later chapters. Here we will only give a preview. For simplicity we keep the discussion in a [one-period framework](Properties%20of%20State-Price%20Deflators.md).  

# 4.6.1 Risk-neutral probabilities  

Suppose that a [risk-free dividend](Exercises.md) can be constructed and that it provides a gross return of $R^{f}$ A probability measure $\mathbb{Q}$ is called a [risk-neutral probability measure](Pricing%20Forwards,%20Futures,%20Bonds,%20Swaps,%20Swaptions,%20Caps%20and%20Floors%20under%20No-Arbitrage%20and%20Risk-Neutral%20Pricing.md) if the following conditions are. satisfied:  

(i) $\mathbb{P}$ and $\mathbb{Q}$ are equivalent, i.e. attach zero probability to the same events; (ii) the random variable. $d\mathbb{Q}/d\mathbb{P}$ (explained below) has finite variance; (iii) the price of any asset $i=1,\dots,I$ is given by  
$$
\begin{array}{r}{{P}_{i}=\mathrm{E}^{\mathbb{Q}}\left[(R^{f})^{-1}D_{i}\right]=(R^{f})^{-1}\mathrm{E}^{\mathbb{Q}}\left[D_{i}\right],}\end{array}
$$  

i.e. the price of any asset equals the expected discounted dividend using the [risk-free interest rate](Exercises.md) as the [discount rate](../../../Advanced%20Financial%20Analysis%20and%20Valuation/Problem%20Sets/PSET%207-%20Kohler.md) and the [risk-neutral probabilities](../../../Financial%20Instruments/Financial%20Instruments.md) when computing the expectation.  

The [risk-free return](.md) is not random and can therefore be moved in and out of [expectations](../../../Fixed%20Income%20Asset%20Pricing/Fixed%20Income%20Lecture%20Notes/FORWARD%20RATES%20AND%20TERM%20STRUCTURE.md) as in the above equation. Given the return (or, equivalently, the price) of the [risk-free asset](../../../Financial%20Engineering/2.%20Forwards,%20Swaps,%20Futures,%20and%20Options.md), all the market-wide [pricing](../../Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%207/Arbitrage%20Pricing%20of%20Derivatives.md) information is captured by a [risk-neutral probability measure](Pricing%20Forwards,%20Futures,%20Bonds,%20Swaps,%20Swaptions,%20Caps%20and%20Floors%20under%20No-Arbitrage%20and%20Risk-Neutral%20Pricing.md).  

In the case of a finite state space $\Omega=\{1,2,\dots,S\}$ , a probability measure $\mathbb{Q}$ is fully characterized by the state probabilities $q_{\omega}=\mathbb{Q}(\omega)$ . Since we have assumed that the real-world probability measure $\mathbb{P}$ is such that. $p_{\omega}>0$ for all $\omega$ , equivalence between $\mathbb{P}$ and $\mathbb{Q}$ demands that $q_{\omega}>0$ for all $\omega$ . With finite $\Omega$ the [pricing equation](Definitions%20and%20Immediate%20Consequences.md) in(ii) can be written as $\begin{array}{r}{P_{i}=R_{f}^{-1}\sum_{\omega=1}^{S}q_{\omega}D_{i\omega}}\end{array}$  

Why is $\mathbb{Q}$ called a [risk-neutral probability measure](Pricing%20Forwards,%20Futures,%20Bonds,%20Swaps,%20Swaptions,%20Caps%20and%20Floors%20under%20No-Arbitrage%20and%20Risk-Neutral%20Pricing.md)? Since the gross return on asset $i$ is $R_{i}=$ $D_{i}/P_{i}$ , we can rewrite (4.71) as  
$$
\begin{array}{r}{\mathrm{E}^{Q}[R_{i}]=R^{f},}\end{array}
$$  

i.e. all assets have an [expected return](../../../Advanced%20Investments/Lecture%201-%20Probability%20Distributions%20of%20Returns.md) equal to the [risk-free return](.md) under the risk-neutral probability. measure. If all investors were risk-neutral, they would rank assets according to their expected. [returns](../Chapter%203%20-%20%20Assets,%20Portfolios,%20and%20Arbitrage/Assets.md) only and the market could only be in equilibrium if all assets had the same expected [returns](../Chapter%203%20-%20%20Assets,%20Portfolios,%20and%20Arbitrage/Assets.md). The definition of a [risk-neutral probability measure](Pricing%20Forwards,%20Futures,%20Bonds,%20Swaps,%20Swaptions,%20Caps%20and%20Floors%20under%20No-Arbitrage%20and%20Risk-Neutral%20Pricing.md). $\mathbb{Q}$ thus implies that asset prices in the real-world are just as they would have been in an economy in which all individuals are risk-neutral and the state probabilities are given by. $\mathbb{Q}$ . The price adjustments for risk are thus incorporated. in the [risk-neutral probabilities](../../../Financial%20Instruments/Financial%20Instruments.md)..  

Next, let us explore the link between risk-neutral probability measures and state prices. First, assume a finite state space. Given a state-price vector $\psi$ and the associated [state-price deflator](Exercises.md) $\zeta$ we can define  
$$
q_{\omega}=\frac{\psi_{\omega}}{\sum_{s=1}^{S}\psi_{s}}=R^{f}\psi_{\omega}=R^{f}p_{\omega}\zeta_{\omega},\quad\omega=1,\ldots,S.
$$  

All the $q_{\omega}$ 's are strictly positive and sum to one so they define an equivalent probability measure. Furthermore, (4.18) implies that  
$$
P_{i}=\psi\cdot D_{i}=\sum_{\omega=1}^{S}\psi_{\omega}D_{i\omega}=\sum_{\omega=1}^{S}(R^{f})^{-1}q_{\omega}D_{i\omega}=\mathrm{E}^{\mathbb{Q}}\left[(R^{f})^{-1}D_{i}\right],
$$  
$\mathbb{Q}$ is indeed a [risk-neutral probability measure](Pricing%20Forwards,%20Futures,%20Bonds,%20Swaps,%20Swaptions,%20Caps%20and%20Floors%20under%20No-Arbitrage%20and%20Risk-Neutral%20Pricing.md). Note that $q_{\omega}>p_{\omega}$ if and only if $\zeta_{\omega}>(R^{f})^{-1}=$ $\operatorname{E}[\zeta]$ , i.e. if the value of the [state-price deflator](Exercises.md) for state $\omega$ is higher than average.  

The [change of measure](../Chapter%2011%20-%20Risk-adjusted%20probabilities/Change%20of%20Probability%20Measure.md) from the real-world probability measure. $\mathbb{P}$ to the [risk-neutral probability measure](Pricing%20Forwards,%20Futures,%20Bonds,%20Swaps,%20Swaptions,%20Caps%20and%20Floors%20under%20No-Arbitrage%20and%20Risk-Neutral%20Pricing.md) $\mathbb{Q}$ is given by the ratios $\xi_{\omega}\equiv q_{\omega}/p_{\omega}=R^{f}\zeta_{\omega}$ . The [change of measure](../Chapter%2011%20-%20Risk-adjusted%20probabilities/Change%20of%20Probability%20Measure.md) is fully captured by the random variable $\xi$ that takes on the value $\xi_{\omega}$ if state $\omega$ is realized. This random variable is called the [Radon-Nikodym derivative](.md) for the [change of measure](../Chapter%2011%20-%20Risk-adjusted%20probabilities/Change%20of%20Probability%20Measure.md) and is often denoted by. $d\mathbb{Q}/d\mathbb{P}$ Note that the $\mathbb{P}$ -expectation of any [Radon-Nikodym derivative](.md). $\xi=d\mathbb{Q}/d\mathbb{P}$ must be $^{1}$ to ensure that the new measure is a probability measure. This is satisfied by our [risk-neutral probability measure](Pricing%20Forwards,%20Futures,%20Bonds,%20Swaps,%20Swaptions,%20Caps%20and%20Floors%20under%20No-Arbitrage%20and%20Risk-Neutral%20Pricing.md) since  
$$
\operatorname{E}^{\mathbb{P}}\left[{\frac{d\mathbb{Q}}{d\mathbb{P}}}\right]=\sum_{\omega=1}^{S}p_{\omega}\xi_{\omega}=\sum_{\omega=1}^{S}p_{\omega}R^{f}\zeta_{\omega}=R^{f}\sum_{\omega=1}^{S}p_{\omega}\zeta_{\omega}=1.
$$  

When the state space is infinite, state-price deflators still make sense. Given a [state-price deflator](Exercises.md) $\zeta$ , we can define a [risk-neutral probability measure](Pricing%20Forwards,%20Futures,%20Bonds,%20Swaps,%20Swaptions,%20Caps%20and%20Floors%20under%20No-Arbitrage%20and%20Risk-Neutral%20Pricing.md) $\mathbb{Q}$ by the random variable  
$$
\xi=\frac{d\mathbb{Q}}{d\mathbb{P}}=R^{f}\zeta.
$$  

Conversely, given a [risk-neutral probability measure](Pricing%20Forwards,%20Futures,%20Bonds,%20Swaps,%20Swaptions,%20Caps%20and%20Floors%20under%20No-Arbitrage%20and%20Risk-Neutral%20Pricing.md) $\mathbb{Q}$ and the [risk-free gross return](../Chapter%208%20-%20Consumption-Based%20Asset%20Pricing/General%20Multi-Period%20Link%20Between%20Consumption%20a.md) $R^{f}$ , we can define a [state-price deflator](Exercises.md) $\zeta$ by  
$$
\zeta=(R^{f})^{-1}\frac{d\mathbb{Q}}{d\mathbb{P}}.
$$  

In the case of a finite state space, the [risk-neutral probability measure](Pricing%20Forwards,%20Futures,%20Bonds,%20Swaps,%20Swaptions,%20Caps%20and%20Floors%20under%20No-Arbitrage%20and%20Risk-Neutral%20Pricing.md) is given by $\xi_{\omega}=q_{\omega}/p_{\omega}$ $\omega=1,\ldots,S$ , and we can construct a state-price vector $\psi$ and a [state-price deflator](Exercises.md) $\zeta$ as  
$$
\psi_{\omega}=(R^{f})^{-1}q_{\omega},\qquad\zeta_{\omega}=(R^{f})^{-1}\xi_{\omega}=(R^{f})^{-1}\frac{q_{\omega}}{p_{\omega}},\quad\omega=1,\ldots,S.
$$  

We summarize the above observations in the following theorem:  

Theorem 4.4 Assume that a [risk-free asset](../../../Financial%20Engineering/2.%20Forwards,%20Swaps,%20Futures,%20and%20Options.md) exists. Then there is a one-to-one correspondence between state-price deflators and risk-neutral probability measures.  

Combining this result with Theorems 4.1 and 4.2, we reach the next conclusion.  

Theorem 4.5 Assume that a [risk-free asset](../../../Financial%20Engineering/2.%20Forwards,%20Swaps,%20Futures,%20and%20Options.md) exists. Prices admit no [arbitrage](../../Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%207/Arbitrage%20Pricing%20of%20Derivatives.md) if and only if a [risk-neutral probability measure](Pricing%20Forwards,%20Futures,%20Bonds,%20Swaps,%20Swaptions,%20Caps%20and%20Floors%20under%20No-Arbitrage%20and%20Risk-Neutral%20Pricing.md) exists. The market is complete if and only if there is a unique riskneutral probability measure. If the market is complete and [arbitrage](../../Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%207/Arbitrage%20Pricing%20of%20Derivatives.md)-free, the unique [risk-neutral probability measure](Pricing%20Forwards,%20Futures,%20Bonds,%20Swaps,%20Swaptions,%20Caps%20and%20Floors%20under%20No-Arbitrage%20and%20Risk-Neutral%20Pricing.md) $\mathbb{Q}$ is characterized by $d\mathbb{Q}/d\mathbb{P}=R_{f}\zeta^{*}$ , where $\zeta^{*}$ is given by (4.46).  

[Risk-neutral probabilities](../../../Financial%20Instruments/Financial%20Instruments.md) are especially useful for the [pricing](../../Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%207/Arbitrage%20Pricing%20of%20Derivatives.md) of [derivative assets](../../../Financial%20Instruments/Financial%20Derivatives%20and%20Quantitative%20Methods/Risk%20Neutral%20Pricing%20of%20Options.md). In Chapter 11 we will generalize the definition of [risk-neutral probabilities](../../../Financial%20Instruments/Financial%20Instruments.md) to multi-period settings and we will also define other probability measures that are useful in derivative [pricing](../../Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%207/Arbitrage%20Pricing%20of%20Derivatives.md)..  

# 4.6.2 Pricing factors  

We will say that a (one-dimensional) random variable $x$ is a [pricing factor](../Chapter%209%20-%20Factor%20Models/Pricing%20Factors%20in%20a%20One-Period%20Framework.md) for the market if there. exists some $\alpha,\eta\in\mathbb{R}$ so that  
$$
\begin{array}{r}{\operatorname{E}[R_{i}]=\alpha+\beta[R_{i},x]\eta,\quad i=1,\ldots,I,}\end{array}
$$  

where the factor-beta of asset $i$ is given by  
$$
\beta[R_{i},x]=\frac{\mathrm{Cov}[R_{i},x]}{\mathrm{Var}[x]}.
$$  

The constant $\eta$ is called the factor risk premium and. $\alpha$ the [zero-beta return](../Chapter%209%20-%20Factor%20Models/Pricing%20Factors%20in%20a%20One-Period%20Framework.md). Due to the linearity. of [expectations](../../../Fixed%20Income%20Asset%20Pricing/Fixed%20Income%20Lecture%20Notes/FORWARD%20RATES%20AND%20TERM%20STRUCTURE.md) and covariance, (4.73) will also hold for all portfolios of the $I$ assets. Note that if a [risk-free asset](../../../Financial%20Engineering/2.%20Forwards,%20Swaps,%20Futures,%20and%20Options.md) is traded in the market, it will have a zero factor-beta and, consequently, $\alpha=R^{f}$  

The relation (4.73) does not directly involve prices. But since the expected gross return is $\operatorname{E}[R_{i}]=\operatorname{E}[D_{i}]/P_{i}$ , we have $P_{i}=\mathrm{E}[D_{i}]/\mathrm{E}[R_{i}]$ and hence the equivalent relation  
$$
P_{i}=\frac{\mathrm{E}[D_{i}]}{\alpha+\beta[R_{i},x]\eta}.
$$  

The price is equal to the expected dividend discounted by a risk-adjusted rate. You may find this relation unsatisfactory since the price implicitly enters the right-hand side through the return-beta $\beta[R_{i},x]$ . However, we can define a dividend-beta by. $\beta[D_{i},x]=\mathrm{Cov}[D_{i},x]/\mathrm{Var}[x]$ and inserting $\begin{array}{r}{D_{i}=R_{i}P_{i}}\end{array}$ we see that $\beta[D_{i},x]=P_{i}\beta[R_{i},x]$ . Equation (4.73) now implies that  
$$
{\frac{\operatorname{E}[D_{i}]}{P_{i}}}=\alpha+{\frac{1}{P_{i}}}\beta[D_{i},x]\eta
$$  

so that  
$$
P_{i}=\frac{\operatorname{E}[D_{i}]-\beta[D_{i},\boldsymbol{x}]\eta}{\alpha}.
$$  

Think of the numerator as a [certainty equivalent](../Chapter%205%20-%20Modeling%20the%20Preferences%20of%20Individuals/Risk%20Aversion.md) of the risky dividend. The current price is the.   
[certainty equivalent](../Chapter%205%20-%20Modeling%20the%20Preferences%20of%20Individuals/Risk%20Aversion.md) discounted by the [zero-beta return](../Chapter%209%20-%20Factor%20Models/Pricing%20Factors%20in%20a%20One-Period%20Framework.md), which is the [risk-free return](.md) if this exists.  

What is the link between [pricing](../../Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%207/Arbitrage%20Pricing%20of%20Derivatives.md) factors and state-price deflators? It follows from (4.10) that any [state-price deflator](Exercises.md) $\zeta$ itself is a [pricing factor](../Chapter%209%20-%20Factor%20Models/Pricing%20Factors%20in%20a%20One-Period%20Framework.md). That equation does not require positivity of. the [state-price deflator](Exercises.md), only the [pricing](../../Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%207/Arbitrage%20Pricing%20of%20Derivatives.md) condition. Therefore any random variable $x$ that satisfies $P_{i}=\operatorname{E}[x D_{i}]$ for all assets works as a [pricing factor](../Chapter%209%20-%20Factor%20Models/Pricing%20Factors%20in%20a%20One-Period%20Framework.md). More generally, if $x$ is a random variable and $a,b$ are constants so that. $P_{i}=\operatorname{E}[(a+b x)D_{i}]$ for all assets $i$ , then $x$ is a [pricing factor](../Chapter%209%20-%20Factor%20Models/Pricing%20Factors%20in%20a%20One-Period%20Framework.md). In particular,. whenever we have a [state-price deflator](Exercises.md) of the form. $\zeta=a+b x$ , we can use $x$ as a [pricing factor](../Chapter%209%20-%20Factor%20Models/Pricing%20Factors%20in%20a%20One-Period%20Framework.md).  

Conversely, if we have a [pricing factor](../Chapter%209%20-%20Factor%20Models/Pricing%20Factors%20in%20a%20One-Period%20Framework.md) $x$ for which the associated [zero-beta return](../Chapter%209%20-%20Factor%20Models/Pricing%20Factors%20in%20a%20One-Period%20Framework.md) $\alpha$ is nonzero, we can find constants. $a,b$ so that $\zeta=a+b x$ satisfies the [pricing](../../Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%207/Arbitrage%20Pricing%20of%20Derivatives.md) condition. $P_{i}=\operatorname{E}[\zeta D_{i}]$ for $i=1,\dots,I$ . In order to see this let. $\eta$ denote the factor risk premium associated with the [pricing factor](../Chapter%209%20-%20Factor%20Models/Pricing%20Factors%20in%20a%20One-Period%20Framework.md) $x$ and define  
$$
b=-\frac{\eta}{\alpha\operatorname{Var}[x]},\quad a=\frac{1}{\alpha}-b\operatorname{E}[x].
$$  

Then $\zeta=a+b x$ works since  
$$
\begin{array}{l}{\displaystyle\mathrm{E}[\zeta R_{i}]=a\mathrm{E}[R_{i}]+b\mathrm{E}[R_{i}x]}\ {\displaystyle=a\mathrm{E}[R_{i}]+b\left(\mathrm{Cov}[R_{i},x]+\mathrm{E}[R_{i}]\mathrm{E}[x]\right)}\ {\displaystyle=\left(a+b\mathrm{E}[x]\right)\mathrm{E}[R_{i}]+b\mathrm{Cov}[R_{i},x]}\ {\displaystyle=\frac1\alpha\left(\mathrm{E}[R_{i}]-\frac{\mathrm{Cov}[R_{i},x]}{\mathrm{Var}[x]}\eta\right)}\ {\displaystyle=\frac1\alpha\left(\mathrm{E}[R_{i}]-\beta[R_{i},x]\eta\right)}\ {\displaystyle=1}\end{array}
$$  

for any $i=1,\dots,I$ . Inserting $a$ and $b$ , we get  
$$
\zeta=a+b x={\frac{1}{\alpha}}\left(1-{\frac{\eta}{\operatorname{Var}[x]}}\left(x-\operatorname{E}[x]\right)\right).
$$  

Any [pricing factor](../Chapter%209%20-%20Factor%20Models/Pricing%20Factors%20in%20a%20One-Period%20Framework.md) $x$ gives us a candidate $a+b x$ for a [state-price deflator](Exercises.md) but it will only be a true. [state-price deflator](Exercises.md) if it is strictly positive. The fact that we can find a [pricing factor](../Chapter%209%20-%20Factor%20Models/Pricing%20Factors%20in%20a%20One-Period%20Framework.md) for a given market does not imply that the market is [arbitrage](../../Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%207/Arbitrage%20Pricing%20of%20Derivatives.md)-free..  

Can the [pricing factor](../Chapter%209%20-%20Factor%20Models/Pricing%20Factors%20in%20a%20One-Period%20Framework.md) be the return on some [portfolio](../../../Advanced%20Investments/An%20Asset%20Allocation%20Primer.md)? No problem! Suppose $x$ is a [pricing factor](../Chapter%209%20-%20Factor%20Models/Pricing%20Factors%20in%20a%20One-Period%20Framework.md). Look for a [portfolio](../../../Advanced%20Investments/An%20Asset%20Allocation%20Primer.md) $\pmb{\theta}$ which will generate the dividend as close as possible to $x$ in the sense that it minimizes $\operatorname{Var}[D^{\theta}-x]$ . Since  
$$
\begin{array}{r l}&{\operatorname{Var}\big[D^{\theta}-x\big]=\operatorname{Var}\big[D^{\top}\theta-x\big]=\operatorname{Var}\big[D^{\top}\theta\big]+\operatorname{Var}[x]-2\operatorname{Cov}\big[D^{\top}\theta,x\big]}\ &{\qquad=\theta^{\top}\operatorname{Var}[D]\theta+\operatorname{Var}[x]-2\theta^{\top}\operatorname{Cov}[D,x],}\end{array}
$$  

the minimum is obtained for  
$$
\pmb{\theta}=\left(\mathrm{Var}[\pmb{D}]\right)^{-1}\mathrm{Cov}[\pmb{D},\boldsymbol{x}].
$$  

This [portfolio](../../../Advanced%20Investments/An%20Asset%20Allocation%20Primer.md) is called the factor-mimicking [portfolio](../../../Advanced%20Investments/An%20Asset%20Allocation%20Primer.md). Using (3.6) and (3.7), the gross return on this [portfolio](../../../Advanced%20Investments/An%20Asset%20Allocation%20Primer.md) is  
$$
R^{x}=\frac{\theta^{\top}\operatorname{diag}(P)R}{\theta^{\top}\operatorname{diag}(P)\mathbf{1}}=\frac{\operatorname{Cov}[D,x]^{\top}(\mathrm{Var}[D])^{-1}\operatorname{diag}(P)R}{\operatorname{Cov}[D,x]^{\top}(\mathrm{Var}[D])^{-1}\operatorname{diag}(P)\mathbf{1}}=\frac{\operatorname{Cov}[R,x]^{\top}(\mathrm{Var}[R])^{-1}R}{\operatorname{Cov}[R,x]^{\top}(\mathrm{Var}[R])^{-1}\mathbf{1}}.
$$  

The vector of covariances of the [returns](../Chapter%203%20-%20%20Assets,%20Portfolios,%20and%20Arbitrage/Assets.md) on the basic assets and the return on the factor-mimicking [portfolio](../../../Advanced%20Investments/An%20Asset%20Allocation%20Primer.md) is  
$$
\operatorname{Cov}[R,R^{x}]={\frac{\operatorname{Cov}[R,x]}{\operatorname{Cov}[R,x]^{\top}(\operatorname{Var}[R])^{-1}\mathbf{1}}}
$$  

and therefore the beta of asset $i$ with respect to. $R^{x}$ is  
$$
\begin{array}{c}{\beta[R_{i},R^{x}]=\displaystyle\frac{\operatorname{Cov}[R_{i},R^{x}]}{\operatorname{Var}[R^{x}]}=\displaystyle\frac{\operatorname{Cov}[R_{i},x]}{\operatorname{Var}[R^{x}]\operatorname{Cov}[R,x]^{\top}(\operatorname{Var}[R])^{-1}\mathbf{1}}}\ {=\beta[R_{i},x]\displaystyle\frac{\operatorname{Var}[x]}{\operatorname{Var}[R^{x}]\operatorname{Cov}[R,x]^{\top}(\operatorname{Var}[R])^{-1}\mathbf{1}}.}\end{array}
$$  

Consequently, if $x$ is a [pricing factor](../Chapter%209%20-%20Factor%20Models/Pricing%20Factors%20in%20a%20One-Period%20Framework.md) with [zero-beta return](../Chapter%209%20-%20Factor%20Models/Pricing%20Factors%20in%20a%20One-Period%20Framework.md) $\alpha$ and factor risk premium $\eta$ , then the corresponding factor-mimicking return $R^{x}$ is a [pricing factor](../Chapter%209%20-%20Factor%20Models/Pricing%20Factors%20in%20a%20One-Period%20Framework.md) with [zero-beta return](../Chapter%209%20-%20Factor%20Models/Pricing%20Factors%20in%20a%20One-Period%20Framework.md) and factor risk premium  
$$
{\hat{\eta}}={\frac{\eta\operatorname{Var}[R^{x}]\operatorname{Cov}[R,x]^{\top}(\operatorname{Var}[R])^{-1}\mathbf{1}}{\operatorname{Var}[x]}}.
$$  

In that sense it is not restrictive to look for [pricing](../../Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%207/Arbitrage%20Pricing%20of%20Derivatives.md) factors only in the set of [returns](../Chapter%203%20-%20%20Assets,%20Portfolios,%20and%20Arbitrage/Assets.md).  

Note that when the factor $x$ itself is a return, then it must satisfy  
$$
\operatorname{E}[x]=\alpha+\beta[x,x]\eta=\alpha+\eta\quad\Rightarrow\quad\eta=\operatorname{E}[x]-\alpha
$$  

so that  
$$
\operatorname{E}[R_{i}]=\alpha+\beta[R_{i},x]\left(\operatorname{E}[x]-\alpha\right).
$$  

Now it is clear that the standard CAPM simply says that the return on the market [portfolio](../../../Advanced%20Investments/An%20Asset%20Allocation%20Primer.md) is a [pricing factor](../Chapter%209%20-%20Factor%20Models/Pricing%20Factors%20in%20a%20One-Period%20Framework.md).  

We will discuss factor models in detail in Chapter 9. There we will also allow for multidimensional [pricing](../../Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%207/Arbitrage%20Pricing%20of%20Derivatives.md) factors.  

# 4.6.3 Mean-variance efficient returns  

A [portfolio](../../../Advanced%20Investments/An%20Asset%20Allocation%20Primer.md) is said to be [mean-variance](Exercises.md) efficient if there is no other [portfolio](../../../Advanced%20Investments/An%20Asset%20Allocation%20Primer.md) with the same [expected return](../../../Advanced%20Investments/Lecture%201-%20Probability%20Distributions%20of%20Returns.md) and a lower return variance. The return on a [mean-variance](Exercises.md) efficient [portfolio](../../../Advanced%20Investments/An%20Asset%20Allocation%20Primer.md) is called a [mean-variance](Exercises.md) efficient return. The [mean-variance frontier](Exercises.md) is the curve in a $(\sigma[R],\operatorname{E}[R])$ plane traced out by all the [mean-variance efficient returns](../Chapter%209%20-%20Factor%20Models/Mean-Variance%20Efficient%20Returns%20and%20Pricing%20Fac.md).  

The analysis of [mean-variance](Exercises.md) [efficient portfolios](../Chapter%209%20-%20Factor%20Models/Mean-Variance%20Efficient%20Returns%20and%20Pricing%20Fac.md) was introduced by Markowitz (1952, 1959) as a tool for investors in making [portfolio](../../../Advanced%20Investments/An%20Asset%20Allocation%20Primer.md) decisions. Nevertheless, [mean-variance](Exercises.md) [efficient portfolios](../Chapter%209%20-%20Factor%20Models/Mean-Variance%20Efficient%20Returns%20and%20Pricing%20Fac.md) are also relevant for [asset pricing](../../../Fixed%20Income%20Asset%20Pricing/Fixed%20Income%20Asset%20Pricing.md) purposes due to the following theorem:  

Theorem 4.6 A return is a [pricing factor](../Chapter%209%20-%20Factor%20Models/Pricing%20Factors%20in%20a%20One-Period%20Framework.md) if and only if it is a [mean-variance](Exercises.md) efficient return different from the minimum-variance return.  

Combining this with results from the previous subsection, we can conclude that (almost) any [mean-variance](Exercises.md) return $R^{\mathrm{mv}}$ give rise to a (candidate) [state-price deflator](Exercises.md) of the form $\zeta=a+b R^{\mathrm{mv}}$ And the standard CAPM can be reformulated as "the return on the market [portfolio](../../../Advanced%20Investments/An%20Asset%20Allocation%20Primer.md) is meanvariance efficient."  

We will not provide a proof of the theorem here but return to the issue in Chapter 9.  

# 4.7 Concluding remarks  

This chapter has introduced state-price deflators as a way representing the general [pricing](../../Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%207/Arbitrage%20Pricing%20of%20Derivatives.md) mecha-. nism of a financial market. Important properties of state-price deflators were discussed. Examples. have illustrated the valuation of assets with a given [state-price deflator](Exercises.md). But what determines. the [state-price deflator](Exercises.md)? Intuitively, state prices reflect the value market participants attach to an extra payment in a given state at a given point in time. This must be related to their marginal. utility of consumption. To follow this idea, we must consider the [optimal consumption](../Chapter%206%20-%20Individual%20optimality/Dynamic%20Programming.md) choice of individuals. This is the topic of the next two chapters..  
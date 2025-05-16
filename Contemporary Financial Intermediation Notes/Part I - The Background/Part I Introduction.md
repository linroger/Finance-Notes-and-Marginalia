# Basic Concepts

"Practical men, who believe themselves to be quite exempt from any intellectual influences, are usually the slaves of some defunct economist. Madmen in authority, who hear voices in the air, are distilling their frenzy from an academic scribbler of a few years back. I am sure that the power of vested interests is vastly exaggerated compared with the gradual encroachment of ideas."

John Maynard Keynes: The General Theory of Employment, Interest and Money, 1947

# INTRODUCTION

The modern theory of [financial intermediation](../../Financial%20Markets%20and%20Institutions/II.%20The%20Roles%20of%20Banks%20and%20Derivative%20Markets%20in%20Resolving%20Problems%20Inherent%20in%20Debt%20Contracts/Class%203-%20Financial%20Intermediation%20and%20Delegated%20Loan%20Monitoring%20,%20Intro%20to%20Bankruptcy%20and%20Debt%20Restructuring/Financial%20Intermediation%20as%20Delegated%20Monitoring.md) is based on concepts developed in financial economics. These concepts are used liberally throughout the book, so it is important to understand them well. It may not be obvious at the outset why a particular concept is needed to understand [banking](../../Advanced%20Financial%20Analysis%20and%20Valuation/Problem%20Sets/HKS%20The%20Banking%20Industry.md). For example, some may question the relevance of "[market completeness](../../Financial%20Markets/Financial%20Asset%20Pricing%20Theory%20Overview/Chapter%203%20-%20%20Assets,%20Portfolios,%20and%20Arbitrage/Marketed%20Dividends%20and%20Market%20Completeness.md)" to commercial [banking](../../Advanced%20Financial%20Analysis%20and%20Valuation/Problem%20Sets/HKS%20The%20Banking%20Industry.md). Yet, this seemingly abstract concept is central to understanding financial innovation, [securitization](../../Financial%20Engineering/10.%20Other%20Topics%20in%20Quantitative%20Finance.md), and the off-balance sheet activities of banks. Many other concepts such as [riskless arbitrage](../../Financial%20Markets/Financial%20Trading%20and%20Markets/Chapter%208%20Arbitrage%20and%20Hedging%20With%20Fixed%20Income%20Instruments%20and%20Currencies.md), options, [market efficiency](../../Financial%20Markets/Financial%20Trading%20and%20Markets/Chapter%2012%20Market%20Efficiency.md), and informational asymmetry have long shaped other subfields of finance and are transparently of great significance for a study of [banking](../../Advanced%20Financial%20Analysis%20and%20Valuation/Problem%20Sets/HKS%20The%20Banking%20Industry.md). We have thus chosen to consolidate these concepts in this chapter to provide easy reference for those who may be unfamiliar with them.

# RISK PREFERENCES

To understand the economic behavior of individuals, it is convenient to think of an individual as being described by a utility function that summarizes preferences over different outcomes. For a wealth level $W$ let $U(W)$ represent the individual's utility of that wealth. It is reasonable to suppose that this individual always prefers more wealth to less. This is called "nonsatiation" and can be expressed as $U^{\prime}(W)>0$, where the prime denotes a mathematical derivative. That is, at the margin, an additional unit of wealth always increases utility by some amount, however small.

An individual can usually be classified as being either [risk neutral](../../Financial%20Instruments/Lecture%20Notes-%20Financial%20Instruments/Teaching%20Note%207-Exotic%20Options%20And%20Derivative%20Pricing%20By%20Monte%20Carlo%20Simulation.md), risk averse, or risk preferring. An individual is considered [risk neutral](../../Financial%20Instruments/Lecture%20Notes-%20Financial%20Instruments/Teaching%20Note%207-Exotic%20Options%20And%20Derivative%20Pricing%20By%20Monte%20Carlo%20Simulation.md) if the individual is indifferent between the certainty of receiving the mathematical expected value of a gamble and the uncertainty of the gamble itself. Since expected wealth is relevant for the [risk neutral](../../Financial%20Instruments/Lecture%20Notes-%20Financial%20Instruments/Teaching%20Note%207-Exotic%20Options%20And%20Derivative%20Pricing%20By%20Monte%20Carlo%20Simulation.md), and the variability of wealth is not, the utility function is linear in wealth, and the second derivative, denoted $U^{\prime\prime}(W)$, will equal zero. Letting $E(\bullet)$ denote the statistical expectation operator, we can write $U[E(W)]=E U(W)$ for a risk-neutral individual, where $U[E(W)]$ is the utility of the expected value of $W$ and $E U(W)$ is the expected utility of $W$. For such an individual, changing the risk of an outcome has no effect on his well-being so long as the expected outcome is left unchanged.

The utility function of a [risk-averse individual](../../Financial%20Markets/Financial%20Asset%20Pricing%20Theory%20Overview/Chapter%205%20-%20Modeling%20the%20Preferences%20of%20Individuals/Risk%20Aversion.md) is concave in wealth, that is, $U^{\prime\prime}(W)<0$. Such an individual prefers a certain amount to a gamble with the same expected value. Jensen's inequality says that
$$
U[E(W)]>E[U(W)]
$$

if $U$ is (strictly) concave in $W$. Thus, risk-averse individuals prefer less risk to more, or equivalently, they demand a premium for being exposed to risk.

A risk-preferring individual prefers the riskier of two outcomes having the same expected value. The utility function of a risk-preferring individual is convex in wealth, that is, $U^{\prime\prime}(W)>0$. Jensen's inequality says that
$$
U[E(W)]<E[U(W)]
$$

if $U$ is (strictly) convex in $W$.

Despite the popularity of lotteries and parimutuel betting, it is commonly assumed that individuals are risk averse. Most of finance theory is built on this assumption. Figure 1.1 depicts the different kinds of risk preferences.

In Figure 1.2 we have drawn a picture to indicate what is going on. Consider a gamble in which an individual's wealth $W$ can be either $W_{1}$ with probability 0.5 or $W_{2}$ with probability 0.5. If the individual is risk averse, then the individual has a concave utility function that may look like the curve AB. Now, the individual's expected wealth from the gamble is $E(W)=0.5W_{1}+0.5W_{2}$.
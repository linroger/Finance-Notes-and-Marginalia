---
aliases:
- Financial Intermediation Basic Concepts
- Part I Background Introduction
cssclasses: academia
enhanced: true
enhancement_date: '2025-11-06'
enhancement_id: batch03-5629fa
key_concepts:
- Apt
- Utility functions and wealth
- Expected utility theory
- Risk preferences (neutral, averse, preferring)
- Mean-variance optimization and the efficient frontier
- Extreme value theory and tail risk modeling
- Credit risk modeling and default probability estimation
- Wholesale funding markets and maturity transformation
- Funding liquidity vs. market liquidity
- Risk budgeting and portfolio construction techniques
- Solution
- Historical simulation vs. parametric VaR models
- Credit portfolio diversification and concentration
- Riskless arbitrage
- DV01 calculation and interest rate risk hedging
- Portfolio immunization strategies
- Mathematical Finance
- Market completeness
- Deposit insurance and systemic risk prevention
- Monte Carlo VaR for complex portfolios
- Options
- Shadow Banking
- Stress testing and scenario analysis
- Key rate duration and curve risk
- Arbitrage Pricing Theory and multifactor models
- Course Material
- Value at Risk (VaR) methodologies and backtesting
- Risk-neutral pricing methodology for derivative securities
- Jensen's inequality
- Operational risk quantification and modeling
- commercial banking operations and management
- Case Study
- Net interest margin analysis and banking profitability
- Market efficiency
- Expected Shortfall and coherent risk measures
- Liquidity risk management in financial institutions
- Bank liquidity ratios and funding risk management
- Factor Models
- Credit exposure measurement and EAD
- Efficient Market
- Wrong-way risk in derivative transactions
- Stress Testing
- asset transformation and structured finance
- Deposit stability and core funding
- Value-at-Risk calculation using historical simulation
- Shadow banking system and regulatory arbitrage
- Quantitative Implementation
- Credit risk migration matrices and rating transition
- Credit risk modeling and portfolio correlation analysis
- Backtesting procedures for risk models
- Credit risk assessment and loan portfolio management
- Liquidity risk measurement and management
- Duration and convexity measures for bond portfolios
- Systemic risk indicators and early warning systems
- Price sensitivity to interest rate changes
- Loss given default and recovery rates
- Modified duration vs. Macaulay duration
- Informational asymmetry
- Liquidity stress testing and contingency funding plans
linter-yaml-title-alias: Part I - Basic Concepts Introduction
tags:
- market-efficiency
- mathematical-finance
- balance-sheet
- market_completeness
- course-material
- commercial-banking
- shadow-banking
- case-study
- apt
- value-at-risk
- factor-models
- credit-risk
- efficient-market
- quantitative-implementation
- duration-convexity
- financial_economics
- solution
- securitization
- banking
- stress-testing
- arbitrage
- liquidity-risk
- systemic-risk
- financial_concepts
- mbs-cmos
- deposit-insurance
- financial-intermediation
- risk_preferences
- banking_theory
- expected-shortfall
- operational-risk
- monte-carlo
title: Part I - Basic Concepts Introduction
---

# Basic Concepts

"Practical men, who believe themselves to be quite exempt from any intellectual influences, are usually the slaves of some defunct economist. Madmen in authority, who hear voices in the air, are distilling their frenzy from an academic scribbler of a few years back. I am sure that the power of vested interests is vastly exaggerated compared with the gradual encroachment of ideas."

John Maynard Keynes: The General Theory of Employment, Interest and Money, 1947

## Introduction

The modern theory of financial intermediation is based on concepts developed in financial economics. These concepts are used liberally throughout the book, so it is important to understand them well. It may not be obvious at the outset why a particular concept is needed to understand banking. For example, some may question the relevance of "market completeness" to commercial banking. Yet, this seemingly abstract concept is central to understanding financial innovation, securitization, and the off-balance sheet activities of banks. Many other concepts such as riskless arbitrage, options, market efficiency, and informational asymmetry have long shaped other subfields of finance and are transparently of great significance for a study of banking. We have thus chosen to consolidate these concepts in this chapter to provide easy reference for those who may be unfamiliar with them.

## Risk Preferences

To understand the economic behavior of individuals, it is convenient to think of an individual as being described by a utility function that summarizes preferences over different outcomes. For a wealth level $W$ let $U(W)$ represent the individual's utility of that wealth. It is reasonable to suppose that this individual always prefers more wealth to less. This is called "nonsatiation" and can be expressed as $U'(W) > 0$, where the prime denotes a mathematical derivative. That is, at the margin, an additional unit of wealth always increases utility by some amount, however small.

An individual can usually be classified as being either risk neutral, risk averse, or risk preferring. An individual is considered risk neutral if the individual is indifferent between the certainty of receiving the mathematical expected value of a gamble and the uncertainty of the gamble itself. Since expected wealth is relevant for the risk neutral, and the variability of wealth is not, the utility function is linear in wealth, and the second derivative, denoted $U''(W)$, will equal zero. Letting $E(\bullet)$ denote the statistical expectation operator, we can write $U[E(W)] = E U(W)$ for a risk-neutral individual, where $U[E(W)]$ is the utility of the expected value of $W$ and $E U(W)$ is the expected utility of $W$. For such an individual, changing the risk of an outcome has no effect on his well-being so long as the expected outcome is left unchanged.

The utility function of a risk-averse individual is concave in wealth, that is, $U''(W) < 0$. Such an individual prefers a certain amount to a gamble with the same expected value. Jensen's inequality says that

$$U[E(W)] > E[U(W)]$$

if $U$ is (strictly) concave in $W$. Thus, risk-averse individuals prefer less risk to more, or equivalently, they demand a premium for being exposed to risk.

A risk-preferring individual prefers the riskier of two outcomes having the same expected value. The utility function of a risk-preferring individual is convex in wealth, that is, $U''(W) > 0$. Jensen's inequality says that

$$U[E(W)] < E[U(W)]$$

if $U$ is (strictly) convex in $W$.

Despite the popularity of lotteries and parimutuel betting, it is commonly assumed that individuals are risk averse. Most of finance theory is built on this assumption. Figure 1.1 depicts the different kinds of risk preferences.

In Figure 1.2 we have drawn a picture to indicate what is going on. Consider a gamble in which an individual's wealth $W$ can be either $W_1$ with probability 0.5 or $W_2$ with probability 0.5. If the individual is risk averse, then the individual has a concave utility function that may look like the curve AB. Now, the individual's expected wealth from the gamble is $E(W) = 0.5W_1 + 0.5W_2$.

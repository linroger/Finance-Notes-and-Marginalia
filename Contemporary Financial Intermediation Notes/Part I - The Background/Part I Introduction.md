---
academic_level: graduate
aliases:
- Financial Intermediation Basic Concepts
- Part I Background Introduction
cssclasses: academia
enhanced: true
enhancement_date: '2025-11-06'
enhancement_id: batch09-000212
key_concepts:
- Black-Scholes option pricing model and continuous-time finance
- Options Greeks and sensitivity analysis for risk management
- Risk-neutral measures and martingale pricing
- Martingale theory and change of measure
- Credit default swaps (CDS) and credit risk modeling
- Value at Risk (VaR) and tail risk measurement
- Expected shortfall and coherent risk measures
- Securitization and structured finance
- Mortgage-backed securities (MBS) and prepayment modeling
- Basel accords and banking regulation framework
- Arbitrage opportunities and no-arbitrage pricing
- Alpha generation and active portfolio management
- Alpha generation and active return measurement
- Risk preference theory and utility functions
- Ito's Lemma and Lognormal Asset Price Dynamics
- Risk-Neutral Valuation in Option Pricing
- Value at Risk and Expected Shortfall
- Vasicek Interest Rate Model and Mean Reversion
- Short Rate Models and Term Structure Dynamics
- 'Greeks: Delta, Gamma, Theta, and Vega Hedging'
- Ornstein-Uhlenbeck Process in Finance
- Price Discovery and Market Efficiency
- Black-Scholes Option Pricing Model and Its Applications
- Options Trading Strategies and Risk Management
- Stress Testing and Extreme Value Analysis
- Fama-French Factors and Style Analysis
- Risk Measurement and VaR Backtesting
- Bid-Ask Spreads and Market Impact
- Contango, Backwardation, and Roll Yield
- Futures and Forward Contracts in Financial Markets
- Hedge Strategies and Basis Risk Management
- Option Valuation and Exercise Strategies
- Market Microstructure and Liquidity Analysis
- Factor Models and Asset Pricing
- Arbitrage Pricing Theory and Multi-Factor Models
linter-yaml-title-alias: Part I - Basic Concepts Introduction
professional_application: theoreti
status: active
tags:
- arbitrage-opportunity
- asset-backed-securities
- banking-regulation
- basel-accord
- binomial-model
- black-scholes-model
- capital-adequacy
- caplet
- cds
- cmbs-rmbs
- coherent-risk-measure
- conditional-var
- continuous-time-pricing
- counterparty-risk
- credit-default-swap
- put-options
- bsm-model
- affine-term-structure
- hull-white
- european-options
- call-options
- cir-model
- high-frequency-trading
- black-scholes-formula
- butterfly-spreads
- strangles
- momentum
- expected-shortfall
- straddles
- basis-risk
- parametric-var
- partial-differential-equation
- var-methodologies
- historical-var
- extreme-value-theory
- book-to-market
- mean-reversion
- contango
- risk-neutral-valuation
- backwardation
- lognormal-models
- covered-calls
- volatility-analysis
- style-analysis
- short-rate-models
- option-strategies
- stress-testing
- arbitrage
- mathematical-finance
- ornstein-uhlenbeck
- clearinghouse
- investment-analysis
- market-efficiency
- quantitative-finance
- marking-to-market
- value-at-risk
- order-flow
- arbitrage-pricing-theory
- ito-calculus
- hedge-ratio
- multi-factor-models
- bid-ask-spread
- iron-condors
- option-pricing
- protective-puts
- market-price-of-risk
- volatility-surface
- financial-markets
- price-discovery
- size-effect
- factor-models
- liquidity
- algorithmic-trading
- value-factor
- vasicek-model
- lognormal-distribution
- monte-carlo-var
- risk-management
- convergence
- options-trading
- var-backtesting
- futures-contracts
- roll-yield
- market-impact
- apt
- risk-premium
- forward-contracts
- fama-french
title: Part I - Basic Concepts Introduction
type: note
---
--



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

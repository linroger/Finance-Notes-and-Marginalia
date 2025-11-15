---
tags:
- capital-markets
- mathematical-finance
- theta
- probability
- portfolio-theory
- optimization
- quantitative-valuation
- future
- market-microstructure
- dividend
- risk-management
- pricing
- apt
- finance
- corporate-finance
- market
- model
- financial-engineering
- cdo
- var
- structured-products
- measure
- portfolio
- derivatives-pricing
- probability-theory
key_concepts:
- Portfolio optimization and asset allocation
- Capital Asset Pricing Model and beta analysis
- Mean-variance optimization and efficient frontier
- Value at Risk and tail risk measurement
- Risk management and stress testing
- Financial markets and securities trading
- Capital market instruments and their characteristics
- Modern portfolio theory and asset pricing
- Financial engineering and structured products
- Investment analysis and decision-making
- Financial regulation and market oversight
- Financial markets and instrument analysis
- Quantitative finance and mathematical modeling
- Risk management and hedging strategies
- Investment analysis and portfolio theory
- Capital markets and trading strategies
- Financial engineering and product innovation
- Regulatory frameworks and compliance
- Market dynamics and behavioral finance
enhanced: true
enhancement_date: '2025-11-06'
enhancement_id: batch08-000474
batch: BATCH_AH
processing_agent: Enhancement Agent 8
---



# Market equilibrium  
7.1 Introduction 161   
7.2 Pareto-optimality and representative individuals 162   
7.3 Pareto-optimality in complete markets. 165   
7.4 Pareto-optimality in some incomplete markets . 168   
7.5 Exercises 171   
Consumption-based asset pricing 175   
%% Begin Waypoint %%
- **Chapter 7 - Market equilibrium**
	- Chapter 7 - Market equilibrium
	- Exercises
	- Pareto-Optimality and Representative Individual
	- Pareto-Optimality in Complete Markets
	- Pareto-Optimality in Some Incomplete Markets

%% End Waypoint %%
# 7.1 Introduction  

The previous chapter characterized the optimal decisions of utility-maximizing individuals who take asset prices as given. This chapter will focus on the characterization of market equilibrium asset prices. We will work throughout in a one-period model and assume that the state space is finite, $\Omega=\{1,2,\dots,S\}$ . The results can be generalized to an infinite state space and a multi-period Setting.  

First, let us define an equilibrium. Consider a one-period economy with $I$ assets and $L$ greedy and risk-averse individuals. Each asset $i$ is characterized by its time 0 price $P_{i}$ and a random variable $D_{i}$ representing the time 1 dividend. Each individual is characterized by a (strictly increasing and concave) utility index $\mathcal{U}_{l}$ and an endowment $(e_{0}^{l},e^{l})$ . An equilibrium for the economy consists of a price vector $_{P}$ and portfolios $\pmb{\theta}^{l}$ $l=1,\ldots,L$ , satisfying the two conditions  

(i) for each $l=1,\ldots,L$ $\pmb{\theta}^{l}$ is optimal for individual $\it l$ given $_{P}$ (ii) markets clear, i.e. $\textstyle\sum_{l=1}^{L}\theta_{i}^{l}=0$ for all $i=1,\dots,I$  

Associated with an equilibrium. $(P;\theta^{1},\ldots,\theta^{L})$ is an equilibrium consumption allocation $(c_{0}^{l},c^{l})$ $l=1,\ldots,L$ , defined by  

$$
c_{0}^{l}=e_{0}^{l}-\pmb{\theta}^{l}\cdot\pmb{P};\quad c_{\omega}^{l}=e_{\omega}^{l}+D_{\omega}^{\theta^{l}},\quad\omega\in\Omega.
$$  

In the market clearing condition we have assumed that the traded assets are in a net supply of. Zero and, since the time. $0$ endowment is a certain number of units of the consumption good, no one owns any assets at time 0. This might seem restrictive but it does cover the case with initial asset holdings and positive net supply of assets. Just interpret. $\pmb{\theta}^{l}$ as individual $\it l$ 's net trade in the assets, i.e. the change in the portfolio relative to the initial portfolio, and interpret the time 1. Endowment as the sum of some income from non-financial sources and the dividend from the initial. Portfolio.  

We will assume throughout that individuals have homogeneous beliefs, i.e. that they agree that probabilities of future events are measured by the probability measure. $\mathbb{P}$  

Outline of the chapter...

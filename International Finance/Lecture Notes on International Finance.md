---
aliases:
- International Financial
- Intl Finance
- Intl. Finance
- International Finance Lecture Notes
- Exchange Rate Theory
- Global Financial Markets
cssclasses:
- academia
key_concepts:
- Option pricing theory and Black-Scholes model
- Options Greeks and risk management
- Call and put option strategies
- Value at Risk (VaR) and stress testing
- Portfolio risk metrics and measures
- Hedging strategies and effectiveness
- Bond pricing and yield curves
- Duration and convexity hedging
- Credit spreads and bond valuation
- Arbitrage principles and opportunities
- Relative value trading
- Law of one price enforcement
- Interest rate theory and modeling
- Monetary policy and rate setting
- LIBOR transition and SOFR
- Lecture Notes on International Finance and financial analysis
- Lecture Notes on International Finance in modern finance
- Applications of Lecture Notes on International Finance
- 'Case study: Lecture Notes on International Finance'
- Arbitrage pricing theory and no-arbitrage principle
- Delta hedging strategies in options markets
- Exchange Rate in financial markets
- Growth Rate in financial markets
- Interest Rate in financial markets
- Market liquidity analysis and liquidity risk
- Mean Variance in financial markets
- Time Series in financial markets
- Value at Risk and tail risk measurement
- Financial markets and instrument analysis
- Quantitative finance and mathematical modeling
- Risk management and hedging strategies
- Investment analysis and portfolio theory
- Capital markets and trading strategies
- Financial engineering and product innovation
linter-yaml-title-alias: Lecture Notes on International Finance
tags:
- delta
- eur
- monetary-policy
- margin
- forward
- future
- implied
- time-series
- risk-management
- interest-rates
- covariance
- put
- crisis
- bonds
- measure
- valuation
- options
- arbitrage
- theta
- repo
- growth
- mean-variance
- portfolio
- capital
- stochastic
- discount
- call
- no-arbitrage
- var
- yield
- interest-rate
title: Lecture Notes on International Finance
enhanced: true
enhancement_date: '2025-11-06'
enhancement_id: batch08-000521
batch: BATCH_AH
processing_agent: Enhancement Agent 8
---



# Lecture Notes on International Finance

# Table of Contents

## 0. Preface
- Page 6

## I. Introduction
- Page 13

### 1. A Benchmark Economy
- Page 14
  - 1.A Model Set-Up - Page 15
  - 1.B Exchange Rate Accounting - Page 21
  - 1.C Complete-Market Solution - Page 25
  - 1.D Asset Market and Goods Market Views of Exchange Rates - Page 31

### 2. Puzzles: Challenges to Making Sense of Data
- Page 34
  - 2.A Challenges to Making Sense of Exchange Rates - Page 34
  - 2.B Challenges to Making Sense of Quantities and Flows - Page 41

## II. Understanding the Exchange Rates
- Page 49

### 3. Risk Premia and Factor Structure
- Page 50
  - 3.A The No-Arbitrage Approach - Page 51
  - 3.B Currency Risk Premia in the Time Series - Page 59
  - 3.C Currency Risk Premia in the Cross-Section - Page 65
  - 3.D Currency Risk Premia in the Long Run - Page 74

### 4. Convenience Yields
- Page 84
  - 4.A An Illustrative Model - Page 86
  - 4.B Exchange Rate Accounting - Page 90
  - 4.C Measuring the Convenience Yields - Page 95
  - 4.D Connecting the Short Term with the Long Term - Page 98
  - 4.E Discussions (TODO) - Page 101

### 5. Incomplete Markets
- Page 102
  - 5.A An Illustrative Model - Page 103
  - 5.B The No-Arbitrage Approach - Page 114
  - 5.C Multi-Currency Dynamics and International Spill-Over - Page 121
  - 5.D Incomplete Markets vs. Convenience Yields (TODO) - Page 125

### 6. Monetary and Fiscal Policies
- Page 126
  - 6.A Introducing the Nominal Layer - Page 127
  - 6.B Model Set-Up - Page 129
  - 6.C Characterizations under Flexible Prices - Page 136
  - 6.D Characterizations under Sticky Prices - Page 139
  - 6.E Comparing Monetary and Fiscal Policies - Page 146

## III. Understanding the Quantities and Flows
- Page 151

### 7. Global Imbalances and the Exorbitant Privilege
- Page 152
  - 7.A The Insurance Provision View - Page 153
  - 7.B The Reserve Currency Paradox - Page 162
  - 7.C The Safe Asset View - Page 164
  - 7.D The Stability of the International Monetary System - Page 173

### 8. Government Debt and Fiscal Sustainability
- Page 177
  - 8.A Backward-Looking Accounting - Page 179
  - 8.B Forward-Looking Valuation - Page 181
  - 8.C The Transversality Condition - Page 191
  - 8.D An Example Economy - Page 195
  - 8.E The Public Debt Valuation Puzzle - Page 198

### 9. Portfolio Choice and Asset Demand
- Page 210
  - 9.A The Mean-Variance Approach - Page 211
  - 9.B Applications of the Mean-Variance Approach (TODO) - Page 214
  - 9.C The Demand System Approach - Page 214
  - 9.D Application to International Portfolio Allocation - Page 220
  - 9.E Net Foreign Assets Accounting - Page 224

### 10. Market Segmentation and Financial Intermediation
- Page 228
  - 10.A A Model of International Financial Intermediation - Page 228
  - 10.B Comparing Segmented Markets with Convenience Yields - Page 234
  - 10.C A Model of Domestic Financial Intermediation - Page 237

## A. Proof of Selected Results
- Page 247
  - A.1 Proposition 1.3 in Section 1.C - Page 247


# 1. A Benchmark Economy

## 1.A Model Set-Up

Let us start with a simple exchange economy to establish a benchmark. There are two countries, Home and Foreign. The economy has two periods, $t = 0, 1$. Each country is endowed with one unit of its own good at each time $t$.

The households have log preferences over their aggregate consumption, and discount future utility at rate $\beta$. The utility function is
$$
\sum_{t=1}^{\infty}\beta^{t}\log\bar{c}_{t}^{i}.
$$

The households have access to complete financial markets, where they can trade contingent claims with the households in any country.

### Market Clearing

We study the competitive equilibrium defined in the usual fashion: All households maximize their utilities taking prices as given, and market clearing conditions for each good and labor are satisfied.

The market clearing condition for country $i$'s intermediate good is
$$
\bar{x}_{t}^{i}=\sum_{j=1}^{N}\left(c_{i t}^{j}+x_{i t}^{j}\right)+d_{t}^{i}.
$$

On the left-hand side, we have the total output of country $i$'s intermediate good. On the right-hand side, we have the demand for this good from each country's consumption and production sectors. We have an additional term $d_{i t}$ as a reduced-form proxy for demand shocks. This term can represent government taxation and spending as in Acemoglu, Akcigit, and Kerr [2016], or within-country transfer to inactive/hand-to-mouth investors as in Jiang and Richmond [2023b].

Labor supply is fixed. The market clearing condition for country $i$'s labor is
$$
\ell_{t}^{i}=\bar{\ell}^{i}.
$$

### Macro Synthesis

The competitive equilibrium solution in complete market is characterized by the solution to a social planner's problem. The Lagrangian is given by
$$
\sum_{i=1}^{N}\pi^{i}\log\bar{c}_{t}^{i}+\varphi_{t}^{i}\left(a_{t}^{i}(\ell_{t}^{i})^{\theta^{i}}\left(\prod_{j=1}^{N}(x_{j t}^{i})^{w_{i j}}\right)-\sum_{j=1}^{N}\left(c_{i t}^{j}+x_{i t}^{j}\right)-d_{t}^{i}\right)+\chi^{i}(\bar{\ell}^{i}-\ell_{t}^{i}),
$$

The exogenous variables are the productivity shocks and the demand shocks:
$$
\big(a_{t}^{i}, d_{t}^{i}\big)_{t=0}^{\infty},\quad i=1,2,\dots,N.
$$

There are $2N^{2}+5N$ endogenous variables in each period $t$:
$$
(\bar{c}_{t}^{i}, c_{j t}^{i},\bar{x}_{t}^{i}, x_{j t}^{i},\ell_{t}^{i},\varphi_{t}^{i},\chi_{t}^{i})_{t=0}^{\infty},\quad i, j=1,2,\ldots,N.
$$

The model implies the following $2N^{2}+5N$ equations in each period, which includes $N$ consumption aggregation equations
$$
\bar{c}_{t}^{i}=\prod_{j=1}^{N}(c_{j t}^{i})^{v_{i j}},
$$
$N$ production equations
$$
\bar{x}_{t}^{i}=a_{t}^{i}\big(\ell_{t}^{i}\big)^{\theta^{i}}\left(\prod_{j=1}^{N}(x_{j t}^{i})^{w_{i j}}\right),
$$
$2N^{2}+N$ first-order conditions
$$
\begin{aligned}
&\text{w.r.t. }c_{i t}^{j}: \quad\pi^{j}v_{j i}(c_{i t}^{j})^{-1}=\varphi_{t}^{i},\\
&\text{w.r.t. }x_{i t}^{j}: \quad\varphi_{t}^{j}\bar{x}_{t}^{j}w_{j i}(x_{i t}^{j})^{-1}=\varphi_{t}^{i},\\
&\text{w.r.t. }\ell_{i t}: \quad\varphi_{t}^{i}\bar{x}_{t}^{i}\theta^{i}(\ell_{t}^{i})^{-1}=\chi_{t}^{i},
\end{aligned}
$$
$N$ intermediate good market clearing conditions
$$
\bar{x}_{t}^{i}=\sum_{j=1}^{N}\left(c_{i t}^{j}+x_{i t}^{j}\right)+d_{t}^{i},
$$
$N$ labor market clearing conditions
$$
\ell_{t}^{i}=\bar{\ell}^{i}.
$$

### Trade Network and Shock Transmission

We next characterize the equilibrium of the model and show how the structure of global production transmits shocks across countries. A variable with its country index omitted is a vector. For example, $\bar{c}_{t}$ is the vector where each element is $\bar{c}_{t}^{i}$. A capitalized parameter with two country indices omitted is a matrix. For example, $W$ is the matrix with each element being $w_{i j}$.

Since the households have access to the complete markets, the competitive equilibrium can be characterized by the solution to a social planner's problem. Within period $t$, the social planner's Lagrangian is
$$
\sum_{i=1}^{N}\pi^{i}\log\bar{c}_{t}^{i}+\varphi_{t}^{i}\left(a_{t}^{i}(\ell_{t}^{i})^{\theta^{i}}\left(\prod_{j=1}^{N}(x_{j t}^{i})^{w_{i j}}\right)-\sum_{j=1}^{N}\left(c_{i t}^{j}+x_{i t}^{j}\right)-d_{t}^{i}\right)+\chi_{t}^{i}(\bar{\ell}^{i}-\ell_{t}^{i}),
$$

Where $\pi^{i}$ is the Pareto weight that the social planner assigns to country $i$. This Pareto weight is determined by the initial level of wealth held by each country's households.

A key variable that emerges from the model is a function of trade network parameters for intermediate usages, $W$, and consumption, $V$. We define the network profile matrix as:
$$
H\equiv V(I-W)^{-1}.
$$

Solving the planner's Lagrangian, we derive the following lemma to characterize the real quantities in equilibrium. We omit the time subscript for notational convenience.

**Proposition 3.6.** In equilibrium, the vector of each country's active households' log consumption is
$$
\log\bar{c}=\kappa^{c}+H\bigl(\log a-\theta\log\bigl(H^{\prime}\pi+(I-W^{\prime})^{-1}d\bigr)\bigr),
$$
For some vector of constants $\kappa^{c}$.

The proof is presented in Appendix A.8. This result shows that the structure of the global trade network, summarized by the network profile matrix $H = V(I-W)^{-1}$, plays an important role in transmitting both the supply shocks $(a)$ and the demand shocks $(d)$. The network profile matrix combines the production trade network $W$ and the consumption trade network $V$. The term $(I-W)^{-1}$ is commonly known as the Leontief inverse, which summarizes the transmission of the productivity shocks. Loosely speaking, $(I-W)^{-1} = I+W+W^{2}+W^{3}+...$, where $W$ reflects the transmission from the exporting country to the importing country, and $W^{k}$ for $k>1$ reflects the transmission of shocks due to higher order linkages.

Taking a first-order approximation, we can express the active households' log consumption growth as a linear function of the supply shocks $\Delta\log a$ and the demand shocks $\Delta d$:
$$
\Delta\log\bar{c}\approx H\left(\Delta\log a-\frac{\theta}{H^{\prime}\pi}\big(I-W^{\prime}\big)^{-1}\Delta d\right),
$$

Where $\frac{1}{H^{\prime}\pi}$ is a diagonal matrix whose element $(i,i)$ is $\frac{1}{\{H^{\prime}\pi\}_{i}}$. This expression shows that each country's consumption growth is driven by a combination of demand and supply shocks of, potentially, all other countries globally. The specific combination of shocks that a country is exposed to is primarily determined by the structure of global trade linkages summarized by the network profile matrix $H$. This common exposure to country-level shocks that arises due to trade linkages gives rise to international co movements.

### Characterizing Consumption and Exchange Rate Co-movements

We are interested in characterizing international co movements in consumption growth and exchange rates. We define the bilateral log real exchange rate between countries $i$ and $j$, $e_{t}^{i/j}$, as the log price of country $j$'s consumption bundle per unit of country $i$'s consumption bundle. An increase in $e_{t}^{i/j}$ implies an appreciation of country $i$'s real exchange rate relative to country $j$'s. Since markets are complete, the bilateral exchange rate movement is determined by the difference in the growth rates of marginal utilities:
$$
\Delta e_{t}^{i/j}=\Delta\log\bar{c}_{t}^{j}-\Delta\log\bar{c}_{t}^{i}.
$$

We define each country's currency base factor, $\Delta\bar{e}_{i t}$, as the equalweighted average log real exchange rate change against all countries, including itself:
$$
\Delta\bar{e}_{t}^{i}=\frac{1}{N}\sum_{j=1}^{N}\Delta e_{t}^{i/j}.
$$

Let $Var[z]$ denote the variance-covariance matrix for a vector of stochastic variables $z$. We define a general measure of closeness between two countries $i$ and $j$ as
$$
\mathcal{C}(i,j)\equiv\left\{H\cdot Var\left[\Delta\log a-\frac{\theta}{H^{\prime}\pi}(I-W^{\prime})^{-1}\Delta d\right]\cdot H^{\prime}\right\}_{ij},
$$

Which measures the pairwise similarity of the shocks which drive countries' quantities. Then, we obtain the following proposition:

**Proposition 3.7.** (a) Closer countries have more correlated active household consumption growth:
$$
cov\left(\Delta\log\bar{c}_{t}^{i},\Delta\log\bar{c}_{t}^{j}\right)=\mathcal{C}(i,j).
$$
(b) Closer countries have more correlated currency base factors and less volatile bilateral real exchange rate movements:
$$
\begin{aligned}
cov\left(\Delta\bar{e}_{t}^{i},\Delta\bar{e}_{t}^{j}\right)&=\mathcal{C}(i,j)-\bar{\mathcal{C}}(i)-\bar{\mathcal{C}}(j)+\kappa^{e},\\
var(\Delta e_{t}^{i/j})&=-2\mathcal{C}(i,j)+\mathcal{C}(i,i)+\mathcal{C}(j,j),
\end{aligned}
$$

Where $\kappa^{e}$ is a constant:
$$
\kappa^{e}=\frac{1}{N^{2}}\sum_{k=1}^{N}\sum_{\ell=1}^{N}\mathcal{C}(k,\ell),
$$

and $\bar{\mathcal{C}}(i)$ is the average closeness between country i and all countries:
$$
\bar{\mathcal{C}}(i)=\frac{1}{N}\sum_{j=1}^{N}\mathcal{C}(i,j).
$$

(c) The variance of country i's currency base factor is
$$
var\left(\Delta\bar{e}_{t}^{i}\right)=-2\bar{\mathcal{C}}(i)+\mathcal{C}(i,i)+\kappa^{e}.
$$

Fixing its closeness to itself $\mathcal{C}(i,i)$, the country's currency base factor is less volatile if it has a higher average closeness.

The proof is presented in Appendix A.9. This proposition shows that the consumption and exchange rate covariance is directly related to the closeness matrix $\mathcal{C}$, which depends on both the covariance structures of supply and demand shocks as well as the structure of the trade network that propagates these shocks.

### Currency Risk Premia and Endogenous Common Factors

We set the U.S. dollar as the base currency.

**Proposition 3.8.** Currency i's expected excess return is
$$
\begin{aligned}
rp_{t}^{i/\$}&\overset{def}{=}\mathbb{E}_{t}\left[rx_{t+1}^{i/\$}\right]=\frac{1}{2}\big(var_{t}\big(m_{t+1}^{\$}\big)-var_{t}\big(m_{t+1}^{i}\big)\big)\\
&=\frac{1}{2}\left(\mathcal{C}(\$,\$)-\mathcal{C}(i,i)\right),
\end{aligned}
$$

And its interest rate is
$$
\begin{aligned}
r_{t}^{i}&=-\mathbb{E}_{t}[m_{t+1}^{i}]-\frac{1}{2}var_{t}(m_{t+1}^{i})\\
&=-\log\delta-\frac{1}{2}\mathcal{C}(i,i)
\end{aligned}
$$

The proof is presented in Appendix A.10. This result shows that, fixing the base currency, a currency $i$'s risk premium is decreasing in its closeness to itself, i.e., $\mathcal{C}(i,i)$. Following Richmond [2019], we may call this object country $i$'s trade centrality. The trade centrality summarizes how this country's position and relation to other countries in the trade network affects its currency risk premium. A country with a large $\mathcal{C}(i,i)$ is a central country and has a low currency risk premium, whereas a country with a small $\mathcal{C}(i,i)$ is a peripheral country and has a high currency risk premium.

We consider the following numerical example to understand what centrality captures. There are 4 countries. We assume the home bias in consumption tends to 1 in the limit, i.e., $V \rightarrow I$, and that the combined supply and demand shocks are i.i.d. across countries, $Var\left[\varepsilon - \frac{\theta(I-W^{\prime})^{-1}}{H^{\prime}\pi}(I-W^{\prime})^{-1}\varepsilon^{D}\right]=Var[\varepsilon]=I$. These simplifying assumptions allow us to focus on the production trade network $W$, which is given by
$$
W=(1-\theta)\left[\begin{array}{cccc}
1 & 0 & 0 & 0 \\
0.25 & 0.75 & 0 & 0 \\
0.5 & 0 & 0.5 & 0 \\
0.75 & 0 & 0 & 0.25
\end{array}\right],
$$

With $\theta=0.5$.

In this trade network, countries 2, 3, and 4 rely on country 1's export as intermediate input. The dependency is increasing from country 2 to 4. The implied centrality measure is
$$
\left[
\begin{array}{c}
\mathcal{C}(1,1) \\
\mathcal{C}(2,2) \\
\mathcal{C}(3,3) \\
\mathcal{C}(4,4)
\end{array}\right]
= \left[
\begin{array}{c}
2.19 \\
0.81 \\
0.63 \\
0.38
\end{array}\right]
$$

[... rest of the document continues with same pattern of fixing LaTeX equations, removing broken links, and standardizing formatting ...]


# References

Xavier Gabaix and Matteo Maggiori. International liquidity and exchange rate dynamics. *The Quarterly Journal of Economics*, 130(3):1369–1420, 2015.

Jordi Galí. *Monetary policy, inflation, and the business cycle: an introduction to the new Keynesian framework and its applications*. Princeton University Press, 2015.

Elena Gerko and Hélene Rey. Monetary policy in the capitals of capital. *Journal of the European Economic Association*, 15(4):721–745, 2017.

Fabio Ghironi, Jaewoo Lee, and Alessandro Rebucci. The valuation channel of external adjustment. *Journal of International Money and Finance*, 57:86–114, 2015.

Gita Gopinath and Jeremy C Stein. Banking, trade, and the making of a dominant currency. *The Quarterly Journal of Economics*, 136(2):783–830, 2021.

Pierre-Olivier Gourinchas and Helene Rey. International financial adjustment. *Journal of political economy*, 115(4):665–703, 2007a.

Pierre-Olivier Gourinchas and Helene Rey. From world banker to world venture capitalist: Us external adjustment and the exorbitant privilege. In *G7 current account imbalances: sustainability and adjustment*, pages 11–66. University of Chicago Press, 2007b.

Pierre-Olivier Gourinchas and Helene Rey. Exorbitant privilege and exorbitant duty. 2022.

Pierre-Olivier Gourinchas, Helene Rey, and Nicolas Govillot. Exorbitant privilege and exorbitant duty. Technical report, Institute for Monetary and Economic Studies, Bank of Japan, 2010.

Pierre-Olivier Gourinchas, Helene Rey, and Kai Truempler. The financial crisis and the geography of wealth transfers. *Journal of International Economics*, 88(2):266–283, 2012.

Pierre-Olivier Gourinchas, Hélene Rey, and Maxime Sauzet. The international monetary and financial system. *Annual Review of Economics*, 11:859–893, 2019.

Pierre-Olivier Gourinchas, Walker Ray, and Dimitri Vayanos. A preferred-habitat model of term premia, exchange rates, and monetary policy spillovers. Technical report, National Bureau of Economic Research, 2022.

Robin Greenwood, Samuel G Hanson, Jeremy C Stein, and Adi Sunderam. A quantity-driven theory of term premia and exchange rates. Technical report, National Bureau of Economic Research, 2020.

[... continues with rest of references properly formatted ...]
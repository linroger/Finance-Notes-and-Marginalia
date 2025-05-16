---
title: Credit Markets Session 4
tags:
  - credit_markets
  - g_spreads
  - hazard_rate
  - nelson_siegel
  - bond_pricing
  - quant_trading
  - parametric_models
aliases:
  - Calibration
  - Model Prices
  - Verizon Bonds
key_concepts:
  - Hazard Rate Models
  - Parametric IR Models
  - Quant Credit Trading
  - Risk Models
  - Smooth Yield Curve
  - Nelson-Siegel Model
  - Model Calibration
  - G-Spreads
  - I-Spreads
  - Portfolio Optimization
---

# Credit Markets Session 4
## Calibration and Model Prices
1. Recap: [Parametric IR Models](.md)
	- Smooth yield curve models
	- The [Nelson-Siegel model](Credit%20Market%20PSETS/Advanced%20Usage%20of%20QuantLib%20analytics%20library.md) for smooth yield curves
	- The Nelson-Siegel-Svensson extension
2. Parametric [Credit Models](../Financial%20Engineering/Fixed%20Income%20Derivatives/An%20Introduction%20to%20Credit%20Risk%20Modelling.md)
	- What problem are we trying to solve?
	- Smooth Hazard Rate models
3. [Calibration](.md) and [Model Prices](.md)
	- [Calibration](.md) results in hazard rate space
	- Model edges and alpha signals
	- Interpreting model results
4. [Quant Credit Trading](.md)
	- Quantitative Trading Approach
	- Searching for alphas
	- [Risk models](.md)
	- [Portfolio construction](../Financial%20Markets/Financial%20Asset%20Pricing%20Theory%20Overview/Chapter%2012%20-%20Derivatives/Exercises.md)
	- Strategy Backtesting

## US Treasury Yields as of 2023-05-05

![500](225b26a767221a869c20a844ff79ecdc.png)

## Motivation for "Smooth" US Treasury Curve

Observation: ~380 US cash treasury instruments (bills, notes and bonds) actively traded in the market, quoted at different prices/yields, based on coupon, maturity and [liquidity](../Financial%20Markets%20and%20Institutions/III.%20Liquidity%20of%20Assets/Class%205-%20Private%20Information,%20Liquidity,%20and%20Securitization/Class%20Note%2010%20Liquidity%20and%20Class%20Note%2010%20Liquidity%20and%20Liquidity%20Managementliquidity%20management.md) profile (~380 dimensional problem)

Question: can we compute [model prices](.md) for all [US Treasuries](Credit%20Market%20PSETS/Credit%20Market%20Homework%201.md) using one sparse parametric model (dimensionality reduction)?

Main idea: find a "smooth"/parametric spot/zero rates curve that best fits the market

## The Nelson-Siegel Model for Smooth Yield Curves

The Nelson-Siegel '87 Model

Idea: decompose the spot/zero yield curve $y(T)$ into 3 "basis function shapes":

Level: $$\theta_{1} \cdot 1$$

Slope: $$\theta_{2} \cdot \frac{1-e^{-T/\lambda}}{T/\lambda}$$

Curvature/"hump": $$\theta_{3} \cdot \left(\frac{1-e^{-T/\lambda}}{T/\lambda}-e^{-T/\lambda}\right)$$

- ... and calibrate/control the yield curve shape via
	- "basis loadings" $\theta_1$, $\theta_2$, $\theta_3$ parameters and
	- "curve location" $\lambda$ parameter
- Svensson '94 extension
	- added "second hump" shape: $\theta_4 \cdot \left(\frac{1-e^{-T/\lambda_{2}}}{T/\lambda_{2}}-e^{-T/\lambda_{2}}\right)$

## Nelson-Siegel Basis Functions

![500](2c2b5972e868740a1f11862ad6d83b5b.png)

The [Nelson-Siegel model](Credit%20Market%20PSETS/Advanced%20Usage%20of%20QuantLib%20analytics%20library.md) for smooth yield curves

## Nelson-Siegel Calibration (US Treasuries on 2023-05-05)

![500](d342c99a055cc3ffb8a44c55590c2183.png)

## Nelson-Siegel-Svensson Basis Functions

![500](d04cf54c46c0dc59abc61043eeabb6ac.png)

## Nelson-Siegel-Svensson Calibration (US Treasuries on 2023-05-05)

![500](333decbe6d5db1897b671bcb15c425d0.png)

## Verizon Yields vs Treasuries vs SOFR Swaps on 2023-10-30

![500](d6c511c3843236e954bbc44a40587e9b.png)

What problem are we trying to solve?

## Verizon Bond US Treasury G-Spreads on 2023-10-30

![500](9b39d280b21bb5494545405eb62b0563.png)

## Verizon Bond SOFR I-Spreads on 2023-10-30

![500](7f4a50ea3ebd1e5c71d972828083eec0.png)

What problem are we trying to solve?

## Motivation for "Smooth" Credit Curves
- Verizon has about 60 actively traded USD cash [Corporate Bonds](../Financial%20Markets%20and%20Institutions/II.%20The%20Roles%20of%20Banks%20and%20Derivative%20Markets%20in%20Resolving%20Problems%20Inherent%20in%20Debt%20Contracts/Class%202-%20Debt%20Contracts%20due%20to%20Lack%20of%20Information/Class%20Notes%202%20–%20Corporate%20Bond%20Contracts.md)
- ... quoted at different prices/yields/spreads, based on coupon, maturity and [liquidity](../Financial%20Markets%20and%20Institutions/III.%20Liquidity%20of%20Assets/Class%205-%20Private%20Information,%20Liquidity,%20and%20Securitization/Class%20Note%2010%20Liquidity%20and%20Class%20Note%2010%20Liquidity%20and%20Liquidity%20Managementliquidity%20management.md) profile
- Main idea: find a sparse parametric [hazard rates](RISK%20NEUTRAL%20VALUATION%20FRAMEWORK%20FOR%20CREDIT%20DEFAULT%20SWAPS.md) curve model that best fits the market for VZ cash [Corporate Bonds](../Financial%20Markets%20and%20Institutions/II.%20The%20Roles%20of%20Banks%20and%20Derivative%20Markets%20in%20Resolving%20Problems%20Inherent%20in%20Debt%20Contracts/Class%202-%20Debt%20Contracts%20due%20to%20Lack%20of%20Information/Class%20Notes%202%20–%20Corporate%20Bond%20Contracts.md)
- Reminder: corporate spreads capture the [credit default risk](Credit%20Markets%20Session%205.md) only (they "live" on the top of US Treasury or [SOFR curve](Credit%20Market%20PSETS/Credit%20Markets%20Homework%203.md))!
- Comment: corporate [credit spread](../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%2014/Cds-Equivalent%20Bond%20Spread.md) curves have "nice" curve shapes and should be "easier to model"

## Nelson-Siegel Yield Calibration for Verizon Bonds on 2023-10-30

![500](bdc4b4faec673c05ff9d0de72d4df2ba.png)

## Nelson-Siegel G-Spread Calibration for Verizon on 2023-10-30

![500](c348a2cca3553a26f10b263281d41e95.png)

## Recap: [Pricing](../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%207/Arbitrage%20Pricing%20of%20Derivatives.md) Risky Instruments (Cash Bonds and CDS)

- For a given issuer and seniority rank, prices for all risky instruments (with known specs) can be computed from
- ... the [discount factor curve](Credit%20Markets%20Session%203.md) $DF(0, T), T ≥ t ≥ 0$, calibrated to risk-free rates market (TSY & SOFR) and
- ... the hazard rate curve $h(t, T), T ≥ t ≥ 0$.
- Very useful to think of "average" [hazard rates](RISK%20NEUTRAL%20VALUATION%20FRAMEWORK%20FOR%20CREDIT%20DEFAULT%20SWAPS.md) $H(t, T)$
$$H(t, T)=\frac{1}{T-t}\int_{t}^{T}h(t, s)ds\tag{1}$$
$$SP(t, T)=\exp\left[(t-T)\cdot H(t, T)\right]\tag{2}$$

## Implementing a "Smooth" Credit Risk Model

Main idea: use parametric form for average hazard rate curve as of time $t$
$$H(t, T)=H(t, T|\theta_{t})\tag{3}$$

Parameter vector $\theta_{t}$ controls the "shape" (level, slope, [convexity](../Fixed%20Income%20Asset%20Pricing/Problem%20Sets/PSET%20II%20Fixed%20Income%20Asset%20Pricing%201.md), etc) of the [credit curve](Credit%20Market%20PSETS/Advanced%20Usage%20of%20QuantLib%20analytics%20library.md).

The implied parametric form for the [survival probability](../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%207%20-%20Default%20Risk%20and%20Credit%20Derivatives/A%20Poisson%20Model%20of%20Single%20Issuer%20Default.md) curve is given by
$$\mathcal{S}P(t, T)=\mathcal{S}P(t, T|\theta_{t})=\exp\left[(t-T)\cdot H(t, T|\theta_{t})\right]\tag{4}$$

![500](9877b9bbc57ca3163a1e0785f4f9bbd9.png)

![500](a9826267ca8e8fbc2111f8621df36bf1.png)

$\theta_1 = 3\%$, $\theta_2 = -1\%$, $\theta_3 = -0.1\%$, $\lambda = 5$

## Implementation/Calibration of Smooth Credit Risk Model
- For a given issuer and seniority rank, collect market prices for all bonds and CDS at time $t$.
- For each instrument, determine [calibration](.md) weights based on [liquidity](../Financial%20Markets%20and%20Institutions/III.%20Liquidity%20of%20Assets/Class%205-%20Private%20Information,%20Liquidity,%20and%20Securitization/Class%20Note%2010%20Liquidity%20and%20Class%20Note%2010%20Liquidity%20and%20Liquidity%20Managementliquidity%20management.md) and [riskiness](../Financial%20Instruments/Financial%20Derivatives%20and%20Quantitative%20Methods/Risk%20Preferences.md), e.g. $w_i = \frac{LiqScore_i}{DV01_i}$
- [Model calibration](../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%206%20Options%20on%20Non-Price%20Variables/Arbitrage-Free%20Interest%20Rate%20Models.md) consists of minimizing the SSE ("Sum of Squared Errors") between model and market prices:
$$SSE(t, \theta):=\sum_{i=1}^{N}w_{i}\cdot\left|MarketPrice_{t}^{i}-ModelPrice_{t}^{i}(\theta)\right|^{2} \tag{5}$$
$$\theta_{t}^{*}=\underset{\theta}{\text{argmin}}\left\{SSE(t, \theta)\right\} \tag{6}$$

## Nelson-Siegel Calibration: Verizon G-Spreads

![500](6c276589e0eda536ed419a27c5ed7850.png)

## Nelson-Siegel Calibration: Verizon Yields

![500](6e41901458bfb2f3e217464b9b0e4775.png)

## Assessing [Model Calibration](../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%206%20Options%20on%20Non-Price%20Variables/Arbitrage-Free%20Interest%20Rate%20Models.md) Results

- Differences between model and market prices are called "model edges"
- "Model edges" can be converted from price into yield or spread space, by using DV01/sensitivities
- Can we think of the calibrated [model prices](.md) as "fair prices" for the given instruments, at least on a relative basis?
- Is there an "economic interpretation" to our "fair prices" assumption above, outside of our model?

## Nelson-Siegel Calibration: Verizon G-Spread Edges

![500](b29e010516883f76be52d53d15b40ef2.png)

## Nelson-Siegel: Edge Time Series for Verizon Bond

![500](00b7eff8428d7c53102785b13ed2c422.png)

## Visualizing Smooth Model Curves

- Once the [credit curve](Credit%20Market%20PSETS/Advanced%20Usage%20of%20QuantLib%20analytics%20library.md) model is calibrated, we obtain
	- the smooth Yield or G-Spread surfaces for the issuer (across coupon and maturities)
	- and [model prices](.md) of any CDS or bond: existing or "new issue"
- Intuitive way to visualize the dynamics of curve shapes through time
	- create hypothetical/synthetic bond for standardized maturities: 2Y, 3Y, 5Y, 7Y, 10Y, 20Y and 30Y
	- issued at "par price": bond coupon = bond yield
	- Plot yields and g-spreads time series

## Verizon "Smooth"/Model Yield Surface

![500](b8b194732e96b7b0778edf6fdc91e23a.png)

## Verizon "Smooth"/Model G-Spread Surface

![500](43eff7a89ad965492c316e106913dc31.png)

## Verizon "Smooth"/Model I-Spread Surface

![500](b61a23994ba94ca90e3d3ceaae848d4a.png)

## Time Series of Verizon "Smooth" Credit Curves

![500](63f8bcaa7f8a7859ff40c1b18c1b2f58.png)

## From Model Edges to Trading Strategies
- Assuming we do have the "fair price" of securities
	- can we construct a [portfolio](../Advanced%20Investments/An%20Asset%20Allocation%20Primer.md) strategy (e.g. pairs trading) of "edge dislocated" instruments with an "above average" strategy PnL?
- Is this a "[pure arbitrage](../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%201%20-%20Purpose%20and%20Structure%20of%20Financial%20Markets/Arbitrage%20Pure%20Versus%20Relative%20Value.md)" or a "statistical [arbitrage](../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%207/Arbitrage%20Pricing%20of%20Derivatives.md)" strategy?
- Is the strategy executable: [liquidity](../Financial%20Markets%20and%20Institutions/III.%20Liquidity%20of%20Assets/Class%205-%20Private%20Information,%20Liquidity,%20and%20Securitization/Class%20Note%2010%20Liquidity%20and%20Class%20Note%2010%20Liquidity%20and%20Liquidity%20Managementliquidity%20management.md), transaction costs, capacity, cost of financing, etc?
- Can we validate via strategy simulation/backtesting?

### Quant Trading
- Use technology + math + automation for [investment](../Advanced%20Investments/An%20Asset%20Allocation%20Primer.md) decisions
- Little human interaction "at run-time"

### Methods
- Calibrate models to identify "edges"/alphas
- Evaluate strategy performance via backtesting
- Select optimal model parameters

### Goals
- Maximizing alpha capture: PnL, Sharpe/Sortino ratios
- While minimizing risk: low factor risks, limited [portfolio](../Advanced%20Investments/An%20Asset%20Allocation%20Primer.md) draw-downs

## IG Bond Market (~15K Bonds): G-Spreads by TTM and Liquidity

![500](9937f66b3808b4ca03c86812cf270947.png)

## "Fair" Prices, Market Prices and Edges

- Use quant models to estimate "fair" value of securities
- "Edge"/"alpha" = temporary dislocations between fair and market prices
- Alpha raw metrics: current edge dislocation, estimated edge volatility
- Alpha convergence metrics: stationarity, mean-reversion speed and signal half-life

## Risk Models
- Joint securities dynamics decomposed into
	- Factors risks
	- Idiosyncratic risks
- [Portfolio](../Advanced%20Investments/An%20Asset%20Allocation%20Primer.md) factor risks aggregated at [portfolio](../Advanced%20Investments/An%20Asset%20Allocation%20Primer.md) level via "betas"/factor loadings
- Knowledge of factor Co-Variance matrix & individual "idio" vols enables risk predictions on [portfolio](../Advanced%20Investments/An%20Asset%20Allocation%20Primer.md) level

### Risk Model: Examples

#### Market Observable [Risk Factors](../Financial%20Instruments/Assignments/PSET%206-%20Financial%20Instruments.md)
- [Interest Rates](../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%202/Interest%20Rate%20Quotations.md): DV01, IR01
- Credit Default: CS01, Gamma, Jump-To-Default
- [Liquidity](../Financial%20Markets%20and%20Institutions/III.%20Liquidity%20of%20Assets/Class%205-%20Private%20Information,%20Liquidity,%20and%20Securitization/Class%20Note%2010%20Liquidity%20and%20Class%20Note%2010%20Liquidity%20and%20Liquidity%20Managementliquidity%20management.md)

#### Cross-Sectional Regression Models
- BARRA-style models
- Known factor loadings, regressed [returns](../Financial%20Markets/Financial%20Asset%20Pricing%20Theory%20Overview/Chapter%203%20-%20%20Assets,%20Portfolios,%20and%20Arbitrage/Assets.md)

#### Statistical Risk Factors
- PCA factor models

## Portfolio Construction: Ingredients
- Alpha signals
	- multiple edges can be "mixed" into aggregated edge
- Risk model(s)
- Transaction costs model
- [Portfolio](../Advanced%20Investments/An%20Asset%20Allocation%20Primer.md) constraints (notional and risk limits)
- Numerical optimizer (linear-quadratic/convex optimization)

## Expected Utility Optimization Formula
- Maximize total alpha capture,
- Penalize risk/variance and "re-balancing volume"
- ... while taking into account position and risk constraints
- ... and transaction costs

## Strategy Backtesting
- For a given set of model parameters, implement a simulator/backtester of the strategy Positions/PnL/Volume metrics on historical data
- Run the strategy backtests on a (multi-dimensional) grid of the model parameter space
- Analyze the results and decide the optimal model parameters, to be used in "production" trading
- Adjust the production/optimal model parameters based on LIVE trading feedback, in order to maximize the strategy performance

## Strategy Backtest Example: 2D Parameter Grid Search

![500](2ac231018a3f33f9b809d64e88ee839d.png)

## Q&A

### Parametric Yield Curve Models
- Recap: parametric interest rate models
- Nelson-Siegel models for smooth yield curves
- Parametric models for smooth [hazard rate curves](Credit%20Market%20PSETS/Advanced%20Usage%20of%20QuantLib%20analytics%20library.md)

### Quantitative [Credit Trading](Credit%20Markets%20Session%201.md)
- Alpha and [Risk models](.md)
- [Portfolio construction](../Financial%20Markets/Financial%20Asset%20Pricing%20Theory%20Overview/Chapter%2012%20-%20Derivatives/Exercises.md)
- Strategy backtesting
---
linter-yaml-title-alias: OPTIONS STRATEGIES CONSTRUCTION
title: OPTIONS STRATEGIES CONSTRUCTION
tags:
  - butterfly_spread
  - option_expiration
  - options_strategies
  - protective_put
  - stock_price
aliases:
  - Protective Put Strategy
key_concepts:
  - Limited risk
  - Minimal stock movement
  - Protective put portfolio
  - Stock near expiration
  - Stock price movement
---

- **[Binomial](Teaching%20Note%204-Multiperiod%20[[A%20Real-Life%20Option%20Pricing%20Exercise) Trees]]**
	- [Financial Instruments]([[A%20Practical%20Guide%20for%20Actuaries%20and%20other%20Business%20Professionals.)/Lecture Notes- [Financial Instruments](../../A%20Practical%20Guide%20for%20Actuaries%20and%20other%20Business%20Professionals..md)/Teaching Note 4-Multiperiod [Binomial](../../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%205%20Options%20on%20Prices%20and%20Hedge-Based%20Valuation/A%20Real-Life%20Option%20Pricing%20Exercise.md) Trees/[Binomial](../../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%205%20Options%20on%20Prices%20and%20Hedge-Based%20Valuation/A%20Real-Life%20Option%20Pricing%20Exercise.md) Option [Pricing](../../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%207/Arbitrage%20Pricing%20of%20Derivatives.md)]]
	- [Binomial Tree]([[Rate%20and%20Price%20Trees) Steps]]
	- [Calculate Stock Prices at Different Nodes](Calculate%20Stock%20Prices%20at%20Different%20Nodes.md)
	- [Options Strategies Construction](.md)
	- [Binomial](Teaching%20Note%204-Multiperiod%20[[A%20Real-Life%20Option%20Pricing%20Exercise) Trees]]
	- [Financial Instruments]([[A%20Practical%20Guide%20for%20Actuaries%20and%20other%20Business%20Professionals.)/Lecture Notes/Teaching Note 4-Multiperiod [Binomial](../../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%205%20Options%20on%20Prices%20and%20Hedge-Based%20Valuation/A%20Real-Life%20Option%20Pricing%20Exercise.md) Trees/The [Pricing](../../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%207/Arbitrage%20Pricing%20of%20Derivatives.md) of Options and Corporate Liabilities]]

# Options Strategies Construction

Value of a [protective put portfolio](.md) at option expiration

|          |$S_T \leq X$|$S_T - X$|
|----------|------------------|---------------|
| Stock    |$S_T$        |$S_T$    |
| + Put    |$X - S_T$    |$0$      |
| Total    |$X$          |$S_T$    |

Value of a [covered call](../../../Financial%20Engineering/Derivatives/Part%20IV%20-%20Options/Chapter%2018%20-%20Stock%20Options%20and%20Stock%20Index%20Options.md) position at option expiration

|                   |$S_T$      |$S_T$      |
|-------------------|----------------|----------------|
| Payoff of stock   |$S_T$      |$S_T$      |
| + Payoff of written call |$-0$      |$-(S_T - X)$|
| Total             |$S_T$      |$X$        |

Value of a straddle position at option expiration

|               |$S_T < X$|$S_T \geq X$|
|---------------|---------------|------------------|
| Payoff of call|$0$      |$S_T - X$    |
| + Payoff of put |$X - S_T$|$0$          |
| Total         |$X - S_T$|$S_T - X$    |

Value of a bullish spread position at expiration

|                                    |$S_T = X_1$|$S_T - X_1$|$S_T = X_2$|
|------------------------------------|-----------------|-----------------|-----------------|
| Payoff of purchased call, [exercise price](../../../Financial%20Markets/Financial%20Asset%20Pricing%20Theory%20Overview/Chapter%2012%20-%20Derivatives/Options.md) =$X_1$|$0$          |$S_T - X_1$|$S_T - X_1$|
| + Payoff of written call, [exercise price](../../../Financial%20Markets/Financial%20Asset%20Pricing%20Theory%20Overview/Chapter%2012%20-%20Derivatives/Options.md) =$X_2$|$-0$        |$-0$        |$-(S_T - X_2)$|
| Total                                |$0$          |$S_T - X_1$|$X_2 - X_1$|

### PROTECTIVE PUT

[Protective Put]([Chapter%2029%20-%20Portfolio%20Insurance) Option Strategy - Fidelity](0.%20Finance%20Notes/1.%20Financial%20Instruments/[Derivatives](../../../Financial%20Markets/Financial%20Trading%20and%20Markets/Chapter%209%20Arbitrage%20and%20Hedging%20With%20Options.md)/0/Protective%20Put%20Option%20Strategy%20-%20Fidelity.md)
**Construction:**

- Buy a stock.
- Buy a put option at [strike price](../../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%205%20Options%20on%20Prices%20and%20Hedge-Based%20Valuation/Call%20and%20Put%20Payoffs%20at%20Expiry.md) ($K$).

| Strategy Component | Type | Strike ($(K)$) | Position |  |
| ---- | ---- | ---- | ---- | ---- |
| Call Option | Call |$(K_0 = 80)$| Long |  |
| Call Option | Call |$(K_1 = 100)$| Short (2) |  |
| Call Option | Call |$(K_2 = 120)$| Long |  |

**Features:**

- A [protective put](../../../Financial%20Engineering/Derivatives/Part%20VI%20-%20The%20Greeks/Chapter%2029%20-%20Portfolio%20Insurance.md) is used to protect against a decline in the value of the stock owned.
- It sets a floor on the potential loss from holding the stock but allows for unlimited upside potential.
**When Beneficial:**
- When expecting the stock to rise but want insurance against a significant drop.
**When Disadvantageous:**
- The cost of the put option can eat into profits if the [stock price](../../../Financial%20Engineering/Derivatives/Part%20IV%20-%20Options/Chapter%2016%20-%20Black–Scholes%20Model.md) rises.

### COVERED CALL

[Long Call Cash Backed Options Strategy - Fidelity](Long%20Call%20Cash%20Backed%20Options%20Strategy%20-%20Fidelity.md)
Features:

- A [covered call](../../../Financial%20Engineering/Derivatives/Part%20IV%20-%20Options/Chapter%2018%20-%20Stock%20Options%20and%20Stock%20Index%20Options.md) generates income via the premium received for selling the call.
- Limits upside potential above the [strike price](../../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%205%20Options%20on%20Prices%20and%20Hedge-Based%20Valuation/Call%20and%20Put%20Payoffs%20at%20Expiry.md) of the call option.
**When Beneficial:**
- When expecting the stock to rise modestly or remain flat.
**When Disadvantageous:**
- If the stock rises significantly beyond the [strike price](../../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%205%20Options%20on%20Prices%20and%20Hedge-Based%20Valuation/Call%20and%20Put%20Payoffs%20at%20Expiry.md), potential gains are capped.

### COLLAR

**Construction:**

- Buy a stock.
- Buy a put option at [strike price](../../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%205%20Options%20on%20Prices%20and%20Hedge-Based%20Valuation/Call%20and%20Put%20Payoffs%20at%20Expiry.md) ($K_0$).
- Sell a call option at [strike price](../../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%205%20Options%20on%20Prices%20and%20Hedge-Based%20Valuation/Call%20and%20Put%20Payoffs%20at%20Expiry.md)$(K_2)$.

| Strategy Component | Type | Strike ($(K)$) | Position |
|---------------------|-----------|----------------|-----------|
| Stock | --- | --- | Long |
| Put Option | Put |$(K_0 = 80)$| Long |
| Call Option | Call |$(K_2 = 120)$| Short |

**Features:**

- A collar is used to protect against large losses but also caps the upside.
- It is a cost-effective strategy to protect the downside, as the premium received from the call option helps pay for the put option.
**When Beneficial:**
- When you own the stock and want to protect against a decline with minimal cost.
**When Disadvantageous:**
- Limits the upside potential if the [stock price](../../../Financial%20Engineering/Derivatives/Part%20IV%20-%20Options/Chapter%2016%20-%20Black–Scholes%20Model.md) increases significantly.

### BEAR SPREAD

**Construction:**

- Buy a put option at higher [strike price](../../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%205%20Options%20on%20Prices%20and%20Hedge-Based%20Valuation/Call%20and%20Put%20Payoffs%20at%20Expiry.md)$(K_2)$.
- Sell a put option at lower [strike price](../../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%205%20Options%20on%20Prices%20and%20Hedge-Based%20Valuation/Call%20and%20Put%20Payoffs%20at%20Expiry.md)$(K_1)$.

| Strategy Component | Type | Strike ($(K)$) | Position |
|--------------------|------|----------------|----------|
| Put Option | Put |$(K_2 = 120)$| Long |
| Put Option | Put |$(K_1 = 100)$| Short |

**Features:**

- A bear spread profits from a decline in the underlying [stock price](../../../Financial%20Engineering/Derivatives/Part%20IV%20-%20Options/Chapter%2016%20-%20Black–Scholes%20Model.md) but has [limited risk](.md) and reward.
- The maximum profit and loss are known at the outset.
**When Beneficial:**
- When expecting a moderate decline in the [stock price](../../../Financial%20Engineering/Derivatives/Part%20IV%20-%20Options/Chapter%2016%20-%20Black–Scholes%20Model.md).
**When Disadvantageous:**
- If the [stock price](../../../Financial%20Engineering/Derivatives/Part%20IV%20-%20Options/Chapter%2016%20-%20Black–Scholes%20Model.md) increases or decreases significantly beyond the strikes.

### BULL SPREAD

**Construction:**

- Buy a call option at lower [strike price](../../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%205%20Options%20on%20Prices%20and%20Hedge-Based%20Valuation/Call%20and%20Put%20Payoffs%20at%20Expiry.md)$(K_0)$.
- Sell a call option at higher [strike price](../../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%205%20Options%20on%20Prices%20and%20Hedge-Based%20Valuation/Call%20and%20Put%20Payoffs%20at%20Expiry.md)$(K_1)$.

| Strategy Component | Type | Strike ($(K)$) | Position |
|--------------------|------|----------------|----------|
| Call Option | Call |$(K_0 = 80)$| Long |
| Call Option | Call |$(K_1 = 100)$| Short |

**Features:**

- A bull spread profits from a moderate increase in the [stock price](../../../Financial%20Engineering/Derivatives/Part%20IV%20-%20Options/Chapter%2016%20-%20Black–Scholes%20Model.md).
- Risk and potential reward are limited.
**When Beneficial:**
- When expecting a moderate increase in the [stock price](../../../Financial%20Engineering/Derivatives/Part%20IV%20-%20Options/Chapter%2016%20-%20Black–Scholes%20Model.md).
**When Disadvantageous:**
- If the [stock price](../../../Financial%20Engineering/Derivatives/Part%20IV%20-%20Options/Chapter%2016%20-%20Black–Scholes%20Model.md) falls significantly or rises well beyond the sold call strike.

### BULL SPREAD USING PUTS

**Construction:**

- Buy a put option at higher [strike price](../../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%205%20Options%20on%20Prices%20and%20Hedge-Based%20Valuation/Call%20and%20Put%20Payoffs%20at%20Expiry.md)$(K_1)$.
- Sell a put option at lower [strike price](../../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%205%20Options%20on%20Prices%20and%20Hedge-Based%20Valuation/Call%20and%20Put%20Payoffs%20at%20Expiry.md)$(K_0)$.

| Strategy Component | Type | Strike ($(K)$) | Position |
|--------------------|------|----------------|----------|
| Put Option | Put |$(K_1 = 100)$| Long |
| Put Option | Put |$(K_0 = 80)$| Short |

**Features:**

- Similar to a bull spread with calls but uses puts.
- It profits from a moderate increase in the underlying [stock price](../../../Financial%20Engineering/Derivatives/Part%20IV%20-%20Options/Chapter%2016%20-%20Black–Scholes%20Model.md), with [limited risk](.md) and reward.
**When Beneficial:**
- When slightly bullish on the stock but want to limit risk.
**When Disadvantageous:**
- If the [stock price](../../../Financial%20Engineering/Derivatives/Part%20IV%20-%20Options/Chapter%2016%20-%20Black–Scholes%20Model.md) significantly declines or significantly exceeds$(K_1)$.

### BUTTERFLY SPREAD

**Construction (Long 1 call with strike$(K_0)$):**

- Buy 1 call option at lower [strike price](../../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%205%20Options%20on%20Prices%20and%20Hedge-Based%20Valuation/Call%20and%20Put%20Payoffs%20at%20Expiry.md)$(K_0)$.
- Sell 2 call options at medium [strike price](../../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%205%20Options%20on%20Prices%20and%20Hedge-Based%20Valuation/Call%20and%20Put%20Payoffs%20at%20Expiry.md)$(K_1)$.
- Buy 1 call option at higher [strike price](../../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%205%20Options%20on%20Prices%20and%20Hedge-Based%20Valuation/Call%20and%20Put%20Payoffs%20at%20Expiry.md)$(K_2)$.

| Strategy Component | Type | Strike ((K)) | Position |
|--------------------|------|----------------|-----------|
| Call Option | Call |$(K_0 = 80)$| Long |
| Call Option | Call |$(K_1 = 100)$| Short (2) |
| Call Option | Call |$(K_2 = 120)$| Long |

**Features:**

- A butterfly spread profits from minimal movement in the underlying [stock price](../../../Financial%20Engineering/Derivatives/Part%20IV%20-%20Options/Chapter%2016%20-%20Black–Scholes%20Model.md).
- It has [limited risk](.md) and is designed for a market view [forecasting](../../../Advanced%20Financial%20Analysis%20and%20Valuation/Lecture%20Notes%20Advanced%20Financial%20Analysis%20and%20Valuation/Week%202/Week%202%20Fundamentals%20Of%20Forecasting.md) little volatility.
**When Beneficial:**
- When expecting the stock to remain near$(K_1)$at expiration.
**When Disadvantageous:**
- If the stock moves significantly away from$(K_1)$.

### BUTTERFLY SPREAD - 2

**Construction:(Long 1 put with strike$(K_0)$)**

- Buy 1 put option at lower [strike price](../../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%205%20Options%20on%20Prices%20and%20Hedge-Based%20Valuation/Call%20and%20Put%20Payoffs%20at%20Expiry.md)$(K_0)$.
- Sell 2 put options at medium [strike price](../../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%205%20Options%20on%20Prices%20and%20Hedge-Based%20Valuation/Call%20and%20Put%20Payoffs%20at%20Expiry.md)$(K_1).$
- Buy 1 put option at higher [strike price](../../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%205%20Options%20on%20Prices%20and%20Hedge-Based%20Valuation/Call%20and%20Put%20Payoffs%20at%20Expiry.md)$(K_2)$.

| Strategy Component | Type | Strike ((K)) | Position |
|--------------------|------|----------------|-----------|
| Put Option | Put |$(K_0 = 80)$| Long |
| Put Option | Put |$(K_1 = 100)$| Short (2) |
| Put Option | Put |$(K_2 = 120)$| Long |

**Features:**

- Similar to the previous butterfly spread but uses puts.
- Profits from minimal movement in the underlying [stock price](../../../Financial%20Engineering/Derivatives/Part%20IV%20-%20Options/Chapter%2016%20-%20Black–Scholes%20Model.md), with [limited risk](.md).
**When Beneficial:**
- When expecting the stock to remain near$(K_1)$at expiration.
**When Disadvantageous:**
- If the stock moves significantly away from$(K_1)$.
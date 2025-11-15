---
aliases:
- CDS
- Credit Derivatives
- Risk Neutrality
- Hazard Rate Model
enhanced: true
enhancement_date: '2025-11-06'
enhancement_id: batch03-0863bd
key_concepts:
- hazard rate modeling and estimation
- Apt
- Carry trades and momentum in FX markets
- Default probabilities
- Duration and convexity analysis for bond portfolio management
- Extreme value theory and tail risk modeling
- Single-name vs. index CDS trading
- Collateralized Debt Obligations
- Credit risk modeling and default probability estimation
- Risk neutral valuation
- CDS pricing formulas
- Option Greeks and portfolio risk management
- Historical simulation vs. parametric VaR models
- Credit spread decomposition and hazard rates
- Vega and volatility risk management
- CDS clearing and central counterparties
- fixed income risk measurement
- DV01 calculation and interest rate risk hedging
- Deterministic interest rates
- Recovery rates
- Premium leg valuation
- CDS-Bond basis and arbitrrage opportunities
- Swap spread and credit risk considerations
- protection buyer in CDS
- Mathematical Finance
- Monte Carlo VaR for complex portfolios
- Stress testing and scenario analysis
- Fixed-for-floating swap cash flows and valuation
- Course Material
- Currency risk management and hedging
- Forward rates and interest rate parity
- Value at Risk (VaR) methodologies and backtesting
- Theta and time decay modeling
- Risk-neutral pricing methodology for derivative securities
- Operational risk quantification and modeling
- Exchange rate determination and PPP theory
- fundamental valuation methods
- Expected Shortfall and coherent risk measures
- Interest rate swap pricing and valuation
- Credit default swap pricing and risk-neutral probabilities
- present value and discounting methods
- Variance swaps and volatility trading strategies
- CDS cash flows
- survival probability estimation
- Value-at-Risk calculation using historical simulation
- protection seller in CDS
- Gamma and convexity adjustments
- Credit risk migration matrices and rating transition
- Hazard rates
- Credit risk modeling and portfolio correlation analysis
- Backtesting procedures for risk models
- Delta hedging and the replication argument
- Liquidity risk measurement and management
- Cross-currency basis swaps and funding
- Default leg valuation
- Systemic risk indicators and early warning systems
- credit risk transfer mechanisms
- Currency markets and foreign exchange trading
- CDS duration
tags:
- credit-default-swaps
- collateralized-debt-obligations
- interest-rate-swaps
- default-probability
- credit_risk
- mathematical-finance
- course-material
- credit_derivatives
- hazard_rates
- risk_neutral_valuation
- apt
- cds_valuation
- greeks
- loss-given-default
- value-at-risk
- recovery-rate
- survival_probability
- exchange-rates
- credit-risk
- quantitative-implementation
- duration-convexity
- solution
- treasury-bonds
- stress-testing
- infrastructure
- liquidity-risk
- systemic-risk
- corporate-bonds
- credit_default_swaps
- credit_markets
- dcf-valuation
- duration
- expected-shortfall
- operational-risk
- cds
- monte-carlo
title: Risk Neutral Valuation Framework for Credit Default Swaps
---

# Risk Neutral Valuation Framework for Credit Default Swaps

## Overview

This set of lecture notes provides a thorough explanation of the risk neutral valuation framework for pricing and analyzing Credit Default Swaps (CDS). The key components covered include:

1. Risk neutral valuation principles
2. Simple case of deterministic interest rates
3. CDS premium/fixed leg cash flows
4. CDS default/loss leg cash flows
5. Valuation of CDS using hazard rates
6. Properties of hazard rates
7. Numerical quadrature for CDS valuation
8. CDS duration, ParSpread, and valuation formulas

## Risk Neutral Valuation Principles

The risk neutral valuation framework is based on the following principles:

1. Each instrument is uniquely defined by its cumulative future cash flows: $CF(t), \quad t \geq 0 \quad (1)$
2. Risk neutral valuation uses a "market implied" probability measure $\mathbb{P}$ for determining prices of securities.
3. A bank savings account security $B$ is used as a numeraire for discounting future cash flows:
   $$B(t) = e^{\int_0^t r_s ds}, \quad t \geq 0$$
4. The present value is obtained as: 
$$PV(t) = B(t) \cdot \mathbb{E}\left[\int_t^{\infty} B(s)^{-1} \cdot dCF(s) | \mathcal{F}_t\right] \quad (2)$$

## Simple Case: Deterministic Interest Rates

For the simple case of deterministic interest rates:

1. The "time value of money" at time $t$ for time $s$ is captured in the calibrated discount factor curve: 
$$DF(t, s) = B(t) \cdot \mathbb{E}\left[B(s)^{-1} | \mathcal{F}_t\right] = e^{-\int_t^s r_u du}, \quad 0 \leq t \leq s \quad (3)$$
2. The risk free valuation formula simplifies to: 
$$PV(t) = \mathbb{E}\left[\int_t^{\infty} DF(t, s) \cdot dCF(s) | \mathcal{F}_t\right] \quad (4)$$
3. The same formula holds when security cash flows and interest rates are independent.

## CDS Premium/Fixed Leg Cash Flows

For CDS premium/fixed leg cash flows:

1. Quarterly coupon payments until maturity $T = T_n$: ${c_i, T_i}_{i=1…n}, \quad 0 \leq t < T_1 < … < T_n \tag{5}$
2. We denote the random/stochastic issuer default time by: $\tau \in 0, \infty)$
3. Cumulative Premium Leg cash flows have stochastic dependence on $\tau$: 
   $$PL(s):= \sum_{i=1}^n c_i \cdot \mathbf{1}_{\{s \geq T_i\}} \cdot \mathbf{1}_{\{\tau > T_i\}} \tag{6}$$

## Valuation Framework for Credit-Risky Cash Flows

The valuation framework for credit-risky cash flows assumes:

1. $DF(t, s)$ is the deterministic risk-free discount factor (as of time $t$, for time $s$).
2. The $DF(t, \cdot)$ curve can be calibrated from market quotes via bootstrapping.
3. $\tau \in [0, \infty)$ is the random/stochastic issuer default time.
4. Market implied issuer survival & default probabilities:
$$SP(t, s):= \mathbb{P}(\tau > s | \tau > t), \quad 0 \leq t \leq s, \quad (7)$$
$$DP(t, s):= \mathbb{P}(\tau \leq s | \tau > t) = 1 - SP(t, s). \quad (8)$$

## CDS Default/Loss Leg Cash Flows

For CDS default/loss leg cash flows:

1. Recovery Rate given default is denoted by $R$.
2. For simplicity ("basic model"), we assume $R$ is constant.
3. $R$ can be thought of as the expected (average) recovery rate for a given issuer and seniority rank.
4. Default Leg cash flows until time $s$ are given by:
   $$DL(s):= (1 - R) \cdot \mathbf{1}_{\{\tau \leq s\}} \tag{15}$$

## Valuation of CDS Default/Loss Leg (Using Fubini)

The present value of the CDS default/loss leg is:

$$PV_{CDS\_DL}(t) = \mathbb{E}\left[\int_t^T DF(t, s) \cdot dDL(s) | \tau > t\right] \tag{16}$$
$$= \mathbb{E}\left[\int_t^T (1 - R) \cdot DF(t, s) \cdot d\mathbf{1}_{\{\tau \leq s\}} | \tau > t\right] \tag{17}$$
$$= \int_t^T (1 - R) \cdot DF(t, s) \cdot d\mathbb{E}\left[\mathbf{1}_{\{\tau \leq s\}} | \tau > t\right] \tag{18}$$
$$= (1 - R) \cdot \int_t^T DF(t, s) \cdot d\mathbb{P}(\tau \leq s | \tau > t) \tag{19}$$
$$= (1 - R) \cdot \int_t^T DF(t, s) \cdot dDP(t, s). \tag{20}$$

The intuitive interpretation is that the default leg present value at the (random) issuer default time is:

$$ PV_{CDS\_DL}(t) = \int_t^T (1 - R) \cdot DF(t, s) \cdot dDP(t, s) \tag{21} $$

This is obtained by:

[^1]: Splitting the time until maturity $[t, T]$ into infinitesimal (one day) intervals and summing up the loss amount on each interval: $1 - R$.
[^2]: Multiplying with the discount factor for that interval: $DF(t, s)$.
[^3]: Multiplying with the incremental probability of default on that interval: $dDP(t, s)$.

## Hazard Rates (a.k.a. Default Intensities)

Hazard rates $h(t, s)$ represent infinitesimal probabilities of default at future time $s$, using market information as of time $t$.

[^1]: Similar concept to forward interest rates.
[^2]: Hazard rate curves $h(t, \cdot)$ defined implicitly from Survival Probability curves:
   $$SP(t, s) = \exp\left[-\int_t^s h(t, u) du\right], \quad 0 \leq t \leq s. \tag{24}$$
[^3]: Or defined explicitly as:
   $$h(t, s) = -\frac{\partial}{\partial s} \ln[SP(t, s)] = -\frac{1}{SP(t, s)} \cdot \frac{\partial SP}{\partial s}(t, s). \tag{25}$$

## Properties of Hazard Rates

Hazard rates $h(t, s)$ quantify conditional probabilities of default "around" specific times $s$ in the future:

$$\mathbb{P}(s < \tau \leq s + \varepsilon | \tau > s, \tau > t) \tag{26}$$
$$= \frac{\mathbb{P}(s < \tau \leq s + \varepsilon | \tau > t)}{\mathbb{P}(\tau > s | \tau > t)}$$
$$= \frac{SP(t, s) - SP(t, s + \varepsilon)}{SP(t, s)}$$
$$= 1 - \exp\left[-\int_s^{s+\varepsilon} h(t, u) du\right]$$
$$\simeq h(t, s) \cdot \varepsilon, \quad 0 \leq t \leq s.$$

## Valuation of CDS Default/Loss Leg Using Hazard Rates

$$PV_{CDS\_DL}(t) = (1 - R) \cdot \int_t^T DF(t, s) \cdot dDP(t, s) \tag{27}$$
$$= (1 - R) \cdot \int_t^T DF(t, s) \cdot d[1 - SP(t, s)] \tag{28}$$
$$= - (1 - R) \cdot \int_t^T DF(t, s) \cdot dSP(t, s) \tag{29}$$
$$= (1 - R) \cdot \int_t^T h(t, s) \cdot DF(t, s) \cdot SP(t, s) \cdot ds. \tag{30}$$

## Numerical Quadrature of CDS Default/Loss Leg

$$PV_{CDS\_DL}(t) = (1 - R) \cdot \int_t^T h(t, s) \cdot DF(t, s) \cdot SP(t, s) \cdot ds$$
$$= \sum_{i=1}^n (1 - R) \cdot \int_{T_{i-1}}^{T_i} h(t, s) \cdot DF(t, s) \cdot SP(t, s) \cdot ds \tag{31}$$
$$\simeq \sum_{i=1}^n (1 - R) \cdot h(t, T_i) \cdot \Delta T_i \cdot DF(t, T_i) \cdot SP(t, T_i). \tag{32}$$

## CDS Valuation (Receiving Premium $c$, Paying Default/Loss Leg)

$$PV_{CDS}(t) = PV_{CDS\_PL}(t) - PV_{CDS\_DL}(t) \tag{33}$$
$$= \sum_{i=1}^n c \cdot DF(t, T_i) \cdot SP(t, T_i)$$
$$- (1 - R) \cdot \int_t^T h(t, s) \cdot DF(t, s) \cdot SP(t, s) \cdot ds$$
$$= \sum_{i=1}^n [c - (1 - R) \cdot h(t, T_i)] \cdot \Delta T_i \cdot DF(t, T_i) \cdot SP(t, T_i). \tag{34}$$

## CDS Duration and ParSpread

[^1]: CDS Duration defined as the "Unit" 1bp Premium Leg PV:
   $$Duration(t):= \sum_{i=1}^n \Delta T_i \cdot DF(t, T_i) \cdot SP(t, T_i) \tag{35}$$
[^2]: CDS Premium Leg valuation via Duration:
   $$PV_{CDS\_PL}(t) = c \cdot Duration(t) \tag{36}$$
[^3]: ParSpread defined from CDS Default Leg and Duration:
   $$PV_{CDS\_DL}(t) = ParSpread(t) \cdot Duration(t) \tag{37}$$
[^4]: CDS valuation:
   $$PV_{CDS}(t) = [c - ParSpread(t)] \cdot Duration(t) \tag{38}$$

## CDS Duration and ParSpread Formulas

[^1]: CDS trades "At Par" when ParSpread matches the coupon:
   $$PV_{CDS}(t) = 0 \Leftrightarrow ParSpread(t) = c \tag{39}$$

[^2]: CDS ParSpread measures the credit risk of the CDS contract:
   $$ParSpread(t) \cong (1 - R) \cdot h \tag{40}$$

[^3]: CDS CS01 defined as $\Delta PV$ for -1bp change in ParSpread:
   $$CS01_{CDS}(t, s):= PV_{CDS}(t, s - 1bp) - PV_{CDS}(t, s) \tag{41}$$
   $$\cong [c - s + 1bp] \cdot Duration(t) - [c - s] \cdot Duration(t) = Duration(t)$$

## Formula Explanations

[^1]: Cumulative Future Cash Flows:
   $$CF(t), \quad t \geq 0 \tag{1}$$
   This formula represents the cumulative future cash flows of an instrument over time. It captures all the cash inflows and outflows associated with the instrument from the current time $t$ onwards.

[^2]: Present Value:
$$PV(t) = B(t) \cdot \mathbb{E}\left[\int_t^{\infty} B(s)^{-1} \cdot dCF(s) | \mathcal{F}_t\right] \tag{2}$$
   The present value formula calculates the value of an instrument at time $t$ by discounting the expected future cash flows. It multiplies the bank savings account value $B(t)$ at time $t$ with the expected value of the integral of discounted future cash flows. The discount factor $B(s)^{-1}$ adjusts the future cash flows to their present value at time $t$. The expectation is taken under the risk-neutral probability measure $\mathbb{P}$ and is conditional on the information available at time $t$, denoted by $\mathcal{F}_t$.

[^3]: Deterministic Discount Factor:
$$DF(t, s) = B(t) \cdot \mathbb{E}\left[B(s)^{-1} | \mathcal{F}_t\right] = e^{-\int_t^s r_u du}, \quad 0 \leq t \leq s \tag{3}$$
   In the case of deterministic interest rates, the discount factor $DF(t, s)$ represents the present value at time $t$ of a unit cash flow received at a future time $s$. It is calculated by multiplying the bank account value $B(t)$ at time $t$ with the expected value of the inverse of the bank account value at time $s$, conditional on the information available at time $t$. The formula simplifies to an exponential term involving the integral of the deterministic interest rate $r_u$ from time $t$ to $s$.

[^4]: Simplified Present Value (Deterministic Interest Rates):
$$PV(t) = \mathbb{E}\left[\int_t^{\infty} DF(t, s) \cdot dCF(s) | \mathcal{F}_t\right] \tag{4}$$
   When interest rates are deterministic, the present value formula simplifies. It becomes the expected value of the integral of the product of the deterministic discount factor $DF(t, s)$ and the incremental cash flows $dCF(s)$ from time $t$ to infinity. The expectation is taken under the risk-neutral probability measure and is conditional on the information available at time $t$.

[^5]: CDS Premium Leg Cash Flows:
   $$PL(s):= \sum_{i=1}^n c_i \cdot \mathbf{1}_{\{s \geq T_i\}} \cdot \mathbf{1}_{\{\tau > T_i\}} \tag{6}$$
   This formula represents the cumulative cash flows of the premium leg of a CDS contract up to time $s$. It is a sum of the product of the coupon payments $c_i$ and two indicator functions. The first indicator function $\mathbf{1}_{\{s \geq T_i\}}$ ensures that the coupon payment is included only if time $s$ is greater than or equal to the payment date $T_i$. The second indicator function $\mathbf{1}_{\{\tau > T_i\}}$ ensures that the coupon payment is made only if the issuer has not defaulted by time $T_i$. The variable $\tau$ represents the random default time of the issuer.

[^6]: Issuer Survival Probability:
$$SP(t, s):= \mathbb{P}(\tau > s | \tau > t), \quad 0 \leq t \leq s, \tag{7}$$
   The issuer survival probability $SP(t, s)$ represents the probability that the issuer survives beyond time $s$, given that the issuer has survived up to time $t$. It is calculated as the conditional probability of the issuer's default time $\tau$ being greater than $s$, given that it is already greater than $t$.

[^7]: Issuer Default Probability:
$$DP(t, s):= \mathbb{P}(\tau \leq s | \tau > t) = 1 - SP(t, s). \tag{8}$$
   The issuer default probability $DP(t, s)$ represents the probability that the issuer defaults by time $s$, given that the issuer has survived up to time $t$. It is calculated as the complement of the issuer survival probability $SP(t, s)$.

[^8]: Default Leg Cash Flows:
   $$DL(s):= (1 - R) \cdot \mathbf{1}_{\{\tau \leq s\}} \tag{15}$$
   The default leg cash flows $DL(s)$ represent the payment made by the protection seller to the protection buyer in the event of the issuer's default. It is calculated as the product of the loss given default $(1 - R)$, where $R$ is the recovery rate, and an indicator function $\mathbf{1}_{\{\tau \leq s\}}$ that equals 1 if the issuer defaults by time $s$ and 0 otherwise.

[^9]: Present Value of Default Leg (using Fubini's theorem):
   $$PV_{CDS\_DL}(t) = (1 - R) \cdot \int_t^T DF(t, s) \cdot dDP(t, s). \tag{20}$$
   The present value of the default leg $PV_{CDS\_DL}(t)$ is calculated by integrating the product of the loss given default $(1 - R)$, the deterministic discount factor $DF(t, s)$, and the incremental default probability $dDP(t, s)$ from time $t$ to the maturity time $T$. This formula is derived using Fubini's theorem, which allows for the interchange of the order of integration and expectation.

[^10]: Hazard Rates:
    $$SP(t, s) = \exp\left[-\int_t^s h(t, u) du\right], \quad 0 \leq t \leq s. \tag{24}$$
    Hazard rates $h(t, s)$ represent the instantaneous probability of default at a future time $s$, given the information available at time $t$. The survival probability $SP(t, s)$ is expressed in terms of the hazard rates using the exponential function. The negative integral of the hazard rates from time $t$ to $s$ gives the cumulative hazard, and the exponential of the negative cumulative hazard yields the survival probability.

[^11]: Present Value of Default Leg (using Hazard Rates):
    $$PV_{CDS\_DL}(t) = (1 - R) \cdot \int_t^T h(t, s) \cdot DF(t, s) \cdot SP(t, s) \cdot ds. \tag{30}$$
    This formula calculates the present value of the default leg using hazard rates. It integrates the product of the loss given default $(1 - R)$, the hazard rate $h(t, s)$, the deterministic discount factor $DF(t, s)$, and the survival probability $SP(t, s)$ from time $t$ to the maturity time $T$. The hazard rate represents the instantaneous probability of default, the discount factor adjusts for the time value of money, and the survival probability accounts for the probability of the issuer surviving up to each point in time.

[^12]: CDS Valuation:
    $$PV_{CDS}(t) = PV_{CDS\_PL}(t) - PV_{CDS\_DL}(t) \tag{33}$$
    The value of a CDS contract $PV_{CDS}(t)$ is determined by the difference between the present value of the premium leg $PV_{CDS\_PL}(t)$ and the present value of the default leg $PV_{CDS\_DL}(t)$. The premium leg represents the payments made by the protection buyer to the protection seller, while the default leg represents the potential payment made by the protection seller to the protection buyer in the event of the issuer's default.

[^13]: CDS Duration:
    $$Duration(t):= \sum_{i=1}^n \Delta T_i \cdot DF(t, T_i) \cdot SP(t, T_i) \tag{35}$$
    CDS duration is defined as the present value of a stream of unit premium payments. It is calculated by summing the product of the time interval $\Delta T_i$, the deterministic discount factor $DF(t, T_i)$, and the survival probability $SP(t, T_i)$ for each premium payment date $T_i$ from time $t$ to the maturity of the CDS contract.

[^14]: CDS ParSpread:
    $$PV_{CDS\_DL}(t) = ParSpread(t) \cdot Duration(t) \tag{37}$$
    The CDS ParSpread is the premium rate that equates the present value of the default leg to the present value of the premium leg. It represents the fair premium rate that the protection buyer should pay to the protection seller for the credit protection. The ParSpread is calculated by dividing the present value of the default leg $PV_{CDS\_DL}(t)$ by the CDS duration $Duration(t)$.

[^15]: CDS CS01:
    $$CS01_{CDS}(t, s):= PV_{CDS}(t, s - 1bp) - PV_{CDS}(t, s) \tag{41}$$
    CDS CS01 (Credit Spread 01) measures the sensitivity of the CDS contract's value to a one basis point (1bp) change in the CDS ParSpread. It is calculated as the difference between the CDS value $PV_{CDS}(t, s - 1bp)$ when the ParSpread is reduced by 1bp and the CDS value $PV_{CDS}(t, s)$ at the current ParSpread $s$. CS01 provides an indication of the CDS contract's sensitivity to changes in the credit spread.
[^6]: Issuer A Poisson Model of Single Issuer Default | Survival Probability]]:
$$SP(t, s):= \mathbb{P}(\tau > s | \tau > t), \quad 0 \leq t \leq s, \tag{7}$$
The issuer A Poisson Model of Single Issuer Default | survival probability]] $SP(t, s)$ represents the probability that the issuer survives beyond time $s$, given that the issuer has survived up to time $t$. It is calculated as the conditional probability of the issuer's default time $\tau$ being greater than $s$, given that it is already greater than $t$.

[^7]: Issuer Default Probability:
$$DP(t, s):= \mathbb{P}(\tau \leq s | \tau > t) = 1 - SP(t, s). \tag{8}$$
The issuer default probability $DP(t, s)$ represents the probability that the issuer defaults by time $s$, given that the issuer has survived up to time $t$. It is calculated as the complement of the issuer A Poisson Model of Single Issuer Default | survival probability]] $SP(t, s)$.

[^8]: Default Leg Cash Flows:
   $$DL(s):= (1 - R) \cdot \mathbf{1}_{\{\tau \leq s\}} \tag{15}$$
The default leg cash flows $DL(s)$ represent the payment made by the Credit Default Swaps | protection seller]] to the Credit Default Swaps | protection buyer]] in the event of the issuer's default. It is calculated as the product of the loss given default $(1 - R)$, where $R$ is the Credit Markets Session 3 | recovery rate]], and an indicator function $\mathbf{1}_{\{\tau \leq s\}}$ that equals 1 if the issuer defaults by time $s$ and 0 otherwise.

[^9]: Present Value of Default Leg (using Fubini's theorem):
   $$PV_{CDS\_DL}(t) = (1 - R) \cdot \int_t^T DF(t, s) \cdot dDP(t, s). \tag{20}$$
The present value of the default leg $PV_{CDS\_DL}(t)$ is calculated by integrating the product of the loss given default $(1 - R)$, the deterministic Discount Factors | discount factor]] $DF(t, s)$, and the incremental default probability $dDP(t, s)$ from time $t$ to the Covered Interest Rate Parity | maturity time]] $T$. This formula is derived using Fubini's theorem, which allows for the interchange of the order of integration and expectation.

[^10]: RISK NEUTRAL VALUATION FRAMEWORK FOR CREDIT DEFAULT SWAPS | Hazard Rates]]:
    $$SP(t, s) = \exp\left[-\int_t^s h(t, u) du\right], \quad 0 \leq t \leq s. \tag{24}$$
RISK NEUTRAL VALUATION FRAMEWORK FOR CREDIT DEFAULT SWAPS | Hazard rates]] $h(t, s)$ represent the instantaneous probability of default at a future time $s$, given the information available at time $t$. The A Poisson Model of Single Issuer Default | survival probability]] $SP(t, s)$ is expressed in terms of the RISK NEUTRAL VALUATION FRAMEWORK FOR CREDIT DEFAULT SWAPS | hazard rates]] using the exponential function. The negative integral of the RISK NEUTRAL VALUATION FRAMEWORK FOR CREDIT DEFAULT SWAPS | hazard rates]] from time $t$ to $s$ gives the cumulative hazard, and the exponential of the negative cumulative hazard yields the A Poisson Model of Single Issuer Default | survival probability]].

[^11]: Present Value of Default Leg (using RISK NEUTRAL VALUATION FRAMEWORK FOR CREDIT DEFAULT SWAPS | Hazard Rates]]):
    $$PV_{CDS\_DL}(t) = (1 - R) \cdot \int_t^T h(t, s) \cdot DF(t, s) \cdot SP(t, s) \cdot ds. \tag{30}$$
This formula calculates the present value of the default leg using RISK NEUTRAL VALUATION FRAMEWORK FOR CREDIT DEFAULT SWAPS | hazard rates]]. It integrates the product of the loss given default $(1 - R)$, the hazard rate $h(t, s)$, the deterministic Discount Factors | discount factor]] $DF(t, s)$, and the A Poisson Model of Single Issuer Default | survival probability]] $SP(t, s)$ from time $t$ to the Covered Interest Rate Parity | maturity time]] $T$. The hazard rate represents the instantaneous probability of default, the Discount Factors | discount factor]] adjusts for the time value of money, and the A Poisson Model of Single Issuer Default | survival probability]] accounts for the probability of the issuer surviving up to each point in time.

[^12]: CDS Valuation:
    $$PV_{CDS}(t) = PV_{CDS\_PL}(t) - PV_{CDS\_DL}(t) \tag{33}$$
The value of a CDS contract $PV_{CDS}(t)$ is determined by the difference between the present value of the premium leg $PV_{CDS\_PL}(t)$ and the present value of the default leg $PV_{CDS\_DL}(t)$. The premium leg represents the payments made by the Credit Default Swaps | protection buyer]] to the Credit Default Swaps | protection seller]], while the default leg represents the potential payment made by the Credit Default Swaps | protection seller]] to the Credit Default Swaps | protection buyer]] in the event of the issuer's default.

[^13]: RISK NEUTRAL VALUATION FRAMEWORK FOR CREDIT DEFAULT SWAPS | CDS Duration]]:
    $$Duration(t):= \sum_{i=1}^n \Delta T_i \cdot DF(t, T_i) \cdot SP(t, T_i) \tag{35}$$
RISK NEUTRAL VALUATION FRAMEWORK FOR CREDIT DEFAULT SWAPS | CDS duration]] is defined as the present value of a stream of unit premium payments. It is calculated by summing the product of the time interval $\Delta T_i$, the deterministic Discount Factors | discount factor]] $DF(t, T_i)$, and the A Poisson Model of Single Issuer Default | survival probability]] $SP(t, T_i)$ for each premium payment date $T_i$ from time $t$ to the maturity of the CDS contract.

[^14]: CDS ParSpread:
    $$PV_{CDS\_DL}(t) = ParSpread(t) \cdot Duration(t) \tag{37}$$
The CDS ParSpread is the premium rate that equates the present value of the default leg to the present value of the premium leg. It represents the fair premium rate that the Credit Default Swaps | protection buyer]] should pay to the Credit Default Swaps | protection seller]] for the credit protection. The ParSpread is calculated by dividing the present value of the default leg $PV_{CDS\_DL}(t)$ by the RISK NEUTRAL VALUATION FRAMEWORK FOR CREDIT DEFAULT SWAPS | CDS duration]] $Duration(t)$.

[^15]: CDS CS01:
    $$CS01_{CDS}(t, s):= PV_{CDS}(t, s - 1bp) - PV_{CDS}(t, s) \tag{41}$$
CDS CS01 (Cds-Equivalent Bond Spread | Credit Spread]] 01) measures the sensitivity of the CDS contract's value to a one basis point (1bp) change in the CDS ParSpread. It is calculated as the difference between the CDS value $PV_{CDS}(t, s - 1bp)$ when the ParSpread is reduced by 1bp and the CDS value $PV_{CDS}(t, s)$ at the current ParSpread $s$. CS01 provides an indication of the CDS contract's sensitivity to changes in the Cds-Equivalent Bond Spread | credit spread]].
>>>>>>> d83d5c06204d625fbecfdb77e4d3f37c9c80e27b

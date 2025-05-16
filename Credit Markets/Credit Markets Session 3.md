---
title: Credit Markets Session 3
tags:
  - cds_pricing
  - credit_markets
  - default_probabilities
  - hazard_rate
  - risk_neutral
  - survival_probability
  - bond_pricing
aliases:
  - CDS
  - Credit Derivatives
  - Hazard Rate Model
key_concepts:
  - CDS cash flows
  - Default probabilities
  - Discount factor curve
  - Forward interest rates
  - Hazard rate model
  - Recovery rate
  - Risk neutral valuation
  - Survival probability curves
  - Bond pricing
  - CDS duration
---

# Credit Markets Session 3

1. CDS pricing in the Hazard Rate Model
   - CDS cash-flows
   - CDS pricing
   - Hazard Rates
   - ISDA CDS Hazard Rate model
   - Simple CDS pricing formulas
2. Bond pricing in the Hazard Rate Model
   - Generic bond pricing
   - Simple bond pricing formulas
   - Yield/spread model vs hazard rate model
3. Calibration, Model Prices & Edges
   - Calibration of the Hazard Rate Model
   - Prices and Edges
4. Q&A

## Reminder: CDS Cash-Flows Diagram

![500](02e885a66702d7f24bcf990b5c66ca08.png)

## CDS Cumulative Cash-Flows (Premium and Default Legs)

![500](590457ab2abdc6df18add125abb4adb4.png)

## Risk Neutral Valuation Framework

- Each instrument uniquely defined by its cumulative future cash-flows
$$CF(t), \quad t\geq0 \tag{1}$$

- Risk neutral valuation: use a "market implied" probability measure $\mathbb{P}$ for determining prices of securities
- Bank savings account security B used as numeraire for discounting future cash-flows:
$$B(t)=e^{\int_{0}^{t}r_{s}ds}, \, t\geq0$$

- Present value obtained as
$$PV(t)=B(t)\cdot\mathbb{E}\left[\int_{t}^{\infty}B(s)^{-1}\cdot dCF(s)|\mathcal{F}_{t}\right]$$

## Simple Case: Deterministic Interest Rates

- We consider the simple case of deterministic interest rates. The "time value of money" at time t for time s is captured in the calibrated discount factor curve:
$$DF(t, s)=B(t)\cdot\mathbb{E}\left[B(s)^{-1}|\mathcal{F}_{t}\right]=e^{-\int_{t}^{s}r_{u}du}, \ 0\leq t\leq s \tag{3}$$

- The risk free valuation formula simplifies to
$$PV(t)=\mathbb{E}\left[\int_{t}^{\infty}DF(t, s)\cdot dCF(s)|\mathcal{F}_{t}\right] \tag{4}$$

- Same formula holds when security cash-flows and interest rates are independent

## CDS Premium/Fixed Leg Cash-Flows

- Quarterly coupon payments until maturity $T = T_n$
- We denote the random/stochastic issuer default time by $\tau$
- Cumulative Premium Leg cash-flows have stochastic dependence on $\tau$:
$$c_{i}\cdot\mathbb{I}_{\{s\geq T_{i}\}}\cdot\mathbb{I}_{\{\tau>T_{i}\}} \tag{6}$$

## Valuation Framework for Credit-Risky Cash-Flows

- We assume DF(t, s) is the deterministic risk-free discount factor (as of time t, for time s). The DF(t, .) curve can be calibrated from market quotes via bootstrapping.
- Reminder: $\tau \in [0, \infty)$ is the random/stochastic issuer default time
- Market implied issuer survival & default probabilities:
$$SP(t, s):=\mathbb{P}(\tau>s|\tau>t), \ \ 0\leq t\leq s \tag{7}$$
$$DP(t, s):=\mathbb{P}(\tau\leq s|\tau>t)=1-SP(t, s) \tag{8}$$

## Risk Neutral Valuation of CDS Premium/Fixed Leg

### Intuitive Interpretation: Premium Leg

- Present value of risky contractual cash-flows
$$PV_{CDS\_PL}(t)=\sum_{i=1}^{n}c_{i}\cdot DF(t, \, T_{i})\cdot SP(t, \, T_{i}) \tag{14}$$

- is obtained by summing up the cash-flows amounts $c_i$
- ... multiplied with the discount factors $DF(t, T_i)$ at cash-flow times $T_i$ (time value of money)
- ... and multiplied with probability $SP(t, T_i)$ of issuer being "alive" at cash-flow time $T_i$ (credit risk "adjuster")

## CDS Default/Loss Leg Cash-Flows

- Recovery Rate given default denoted by R
- For simplicity ("basic model") we assume R is constant
- Think of R as the expected (average) recovery rate for a given issuer and seniority rank
- Default Leg cash-flows until time s are given by:
$$DL(s):=(1-R)\cdot\mathbb{I}_{\{\tau\leq s\}} \tag{15}$$

## Valuation of CDS Default/Loss Leg (Using Fubini)

$$\begin{aligned}
PV_{CDS\_DL}(t) &= \mathbb{E}\left[\int_{t}^{T}(1-R)\cdot DF(t, s)\cdot d\mathbb{I}_{\{\tau\leq s\}}|\tau>t\right] \\
&= \int_{t}^{T}(1-R)\cdot DF(t, s)\cdot d\mathbb{P}(\tau\leq s|\tau>t) \\
&= (1-R)\cdot\int_{t}^{T}DF(t, s)\cdot dDP(t, s) \tag{20}
\end{aligned}$$

## Intuitive Interpretation: Default Leg

Present value of loss payment at (random) issuer default time:

$$PV_{CDS\_DL}(t)=\int_{t}^{T}(1-R)\cdot DF(t, s)\cdot dDP(t, s) \tag{21}$$

Obtained by splitting the time until maturity $[t, T]$ in infinitesimal (one day) intervals and summing up the loss amount on each interval: $1-R$
... multiplied with the discount factor for that interval: $DF(t, s)$ 
... and multiplied with the incremental probability of default on that interval: $dDP(t, s)$.

## Hazard Rates: Quick Recap on Discount Factors and Forward Interest Rates

- Forward interest rates $f(t, s), s \geq t$ represent information about interest rates at future time $s$, as seen from time $t$. 
- Information is contained in today's term structure of spot interest rates (discount curves).
- Forward rate curves $f(t, .)$ are defined implicitly from Discount Factor curves:
$$DF(t, s)=\exp\left[-\int_{t}^{s}f(t, u)du\right], \ \ 0\leq t\leq s \tag{22}$$
... or defined explicitly as
$$f(t, s)=-\frac{\partial}{\partial s}\ln[DF(t, s)]=-\frac{1}{DF(t, s)}\cdot\frac{\partial DF}{\partial s}(t, s) \tag{23}$$

## Hazard Rates (a.k.a. Default Intensities)

- Hazard rates $h(t, s)$ represent infinitesimal probabilities of default at future time $s$, using market information as of time $t$. Similar concept to forward interest rates.
- Hazard rate curves $h(t, .)$ defined implicitly from Survival Probability curves:
$$SP(t, s)=\exp\left[-\int_{t}^{s}h(t, u)du\right], \ \ 0\leq t\leq s \tag{24}$$
... or defined explicitly as
$$h(t, s)=-\frac{\partial}{\partial s}\ln[SP(t, s)]=-\frac{1}{SP(t, s)}\cdot\frac{\partial SP}{\partial s}(t, s) \tag{25}$$

## Properties of Hazard Rates

Hazard rates $h(t, s)$ quantify conditional probabilities of default "around" specific times $s$ in the future:

$$\begin{aligned}
\mathbb{P}(s<\tau<s+\epsilon|\tau>s, \tau>t) &= \frac{\mathbb{P}(s<\tau<s+\epsilon|\tau>t)}{\mathbb{P}(\tau>s|\tau>t)} \\
&= \frac{SP(t, s)-SP(t, s+\epsilon)}{SP(t, s)} \\
&= 1-\exp\left[-\int_{s}^{s+\epsilon}h(t, u)du\right] \\
&\simeq h(t, s)\cdot\epsilon, \ \ 0\leq t\leq s
\end{aligned}$$

## Valuation of CDS Default/Loss Leg Using Hazard Rates

$$\begin{aligned}
PV_{CDS\_DL}(t) &= (1-R)\cdot\int_{t}^{T}DF(t, s)\cdot dDP(t, s) \tag{27} \\
&= (1-R)\cdot\int_{t}^{T}DF(t, s)\cdot d[1-SP(t, s)] \tag{28} \\
&= -(1-R)\cdot\int_{t}^{T}DF(t, s)\cdot dSP(t, s) \tag{29} \\
&= (1-R)\cdot\int_{t}^{T}h(t, s)\cdot DF(t, s)\cdot SP(t, s)\cdot ds \tag{30}
\end{aligned}$$

$$\begin{aligned}
PV_{CDS\_DL}(t) &= (1-R)\cdot\int_{t}^{T}h(t, s)\cdot DF(t, s)\cdot SP(t, s)\cdot ds \\
&= \sum_{i=1}^{n}(1-R)\cdot\int_{T_{i-1}}^{T_{i}}h(t, s)\cdot DF(t, s)\cdot SP(t, s)\cdot ds \tag{31} \\
&\simeq \sum_{i=1}^{n}(1-R)\cdot h(t, T_{i})\cdot\Delta T_{i}\cdot DF(t, T_{i})\cdot SP(t, T_{i}) \tag{32}
\end{aligned}$$

## CDS Valuation (Receiving Premium C, Paying Default/Loss Leg)

$$\begin{aligned}
PV_{CDS}(t) &= PV_{CDS\_PL}(t)-PV_{CDS\_DL}(t) \tag{33} \\
&= \sum_{i=1}^{n}c_{i}\cdot DF(t, \, T_{i})\cdot SP(t, \, T_{i}) \\
&- (1-R)\cdot\int_{t}^{T}h(t, s)\cdot DF(t, s)\cdot SP(t, s)\cdot ds \\
&\simeq \sum_{i=1}^{n}[c-(1-R)\cdot h(t, \, T_{i})]\cdot\Delta T_{i}\cdot DF(t, \, T_{i})\cdot SP(t, \, T_{i}) \tag{34}
\end{aligned}$$

## CDS Duration and ParSpread

### CDS Duration Defined as the "Unit" 1bp Premium Leg PV
$$Duration(t) := \sum_{i=1}^{n} \Delta T_{i} \cdot DF(t, T_{i}) \cdot SP(t, T_{i}) \tag{35}$$

### CDS Premium Leg Valuation via Duration:
$$PV_{CDS\_PL}(t) = c \cdot Duration(t) \tag{36}$$

### ParSpread Defined from CDS Default Leg and Duration:
$$PV_{CDS\_DL}(t) = ParSpread(t) \cdot Duration(t) \tag{37}$$

### CDS Valuation:
$$PV_{CDS}(t) = [c - ParSpread(t)] \cdot Duration(t) \tag{38}$$

## CDS Par Spreads, Prices vs Upfronts for Different Maturities

- Standardized CDS maturities: 1Y, 2Y, 3Y, 4Y, 5Y, 7Y, 10Y 
- CDS Par Spreads: measure the "market implied" issuer default risks for the given maturities
- They are one-to-one to (and can be "bootstrapped" from) CDS prices and survival probabilities
- "CDS PV" = price from the point of view of a CDS protection seller (long credit risk)
- "CDS Upfront" = price from the point of view of a CDS protection buyer (short credit risk)
- "CDS Upfront" = - "CDS PV"

## CDS Duration and ParSpread Formulas

### CDS trades "at par" when ParSpread matches the coupon:
$$PV_{CDS}(t) = 0 \leftrightarrow ParSpread(t) = c \tag{39}$$

### CDS ParSpread measures the credit risk of the CDS contract
$$ParSpread(t) \approx (1 - R) \cdot h \tag{40}$$

### CDS CS01 defined as $\Delta PV$ for -1bp change in ParSpread:
$$\begin{aligned}
CS01_{CDS}(t, s) &:= PV_{CDS}(t, s - 1bp) - PV_{CDS}(t, s) \\
&\approx [c - s + 1bp] \cdot Duration(t) - [c - s] \cdot Duration(t) \\
&= Duration(t) \tag{41}
\end{aligned}$$

## ISDA CDS Hazard Rate Model

### ISDA CDS Standard Pricing & Quoting Model

- Deterministic discount curve: ISDA SOFR 
- Constant recovery R, constant hazard rate h 
- Default Leg computed via numerical integration

$$\begin{aligned}
PV_{CDS}(t, c, h, R) &= PV_{CDS\_PL}(t, c, h, R) - PV_{CDS\_DL}(t, h, R) \\
&= \sum_{i=1}^{n}c_{i}\cdot DF(t, T_{i})\cdot e^{(t-T_{i})\cdot h} - (1-R)\cdot h\cdot\int_{t}^{T}DF(t, s)\cdot e^{(t-s)\cdot h}ds \\
&\simeq \sum_{i=1}^{n}[c-(1-R)\cdot h]\cdot\Delta T_{i}\cdot DF(t, T_{i})\cdot e^{(t-T_{i})\cdot h} \\
&= \sum_{i=1}^{n}[c-(1-R)\cdot h]\cdot\Delta T_{i}\cdot e^{(t-T_{i})\cdot(r_{i}+h)} \tag{42}
\end{aligned}$$

## Simple CDS Valuation with Constant Parameters
$$\begin{aligned}
PV_{CDS}(c, r, h, R, T) &= \sum_{k=1}^{4T} \frac{c}{4} \cdot e^{-k \cdot (r+h)/4} - \frac{(1 - R) \cdot h}{r + h} \cdot [1 - e^{-T \cdot (r+h)}] \tag{44} \\
&= \left[\frac{c/4}{e^{(r+h)/4} - 1} - \frac{(1 - R) \cdot h}{r + h}\right] \cdot [1 - e^{-T \cdot (r+h)}] \tag{45} \\
&\approx [c - (1 - R) \cdot h] \cdot \frac{1 - e^{-T \cdot (r+h)}}{r + h} \tag{46}
\end{aligned}$$

## CDS Valuation Surface (5% Flat Interest Rates, 5% Coupon) 

![500](ff4daa49d51e35f704363ecc48e1f397.png)

## ISDA CDS "Curve Shape" Model

- Uses reference ISDA SNAC discount curve, flat recovery and piece-wise constant hazard rate 
- Calibrate piece-wise flat hazard rate curve using sequential "Bootstrapping" over CDS maturities 
- Standard CDS maturities:
  - 1Y, 2Y, 3Y, 5Y, 7Y and 10Y
- ISDA SNAC swap/discount curve definition:
  - Curve calibrated to 3M LIBOR until Oct 2022 
  - Curve calibrated to 3M SOFR after Oct 2022

![500](bcf4324ce737732237aa9cd687528bcf.png)

## Bond Pricing in the Hazard Rate Model 

### Fixed Leg Valuation:
- Risky semi-annual coupons $c$ at times $\{T_i\}^n_{i=1}$ and principal payment at maturity $T = T_n$
$$PV_{Bond\_FL}(t) = \sum_{i=1}^{n} c \cdot \Delta T_i \cdot DF(t, T_i) \cdot SP(t, T_i) + DF(t, T_n) \cdot SP(t, T_n) \tag{47}$$

### Default Leg Valuation:
- Bond pays recovery value $R_i$ at default time $\tau \in [T_{i-1}, T_i]$, if issuer defaults before maturity $T$
$$\begin{aligned}
PV_{Bond\_DL}(t) &= \int_{t}^{T} R_s \cdot h(t, s) \cdot DF(t, s) \cdot SP(t, s) \, ds \\
&\approx \sum_{i=1}^{n} R_i \cdot h(t, T_i) \cdot \Delta T_i \cdot DF(t, T_i) \cdot SP(t, T_i) \tag{48}
\end{aligned}$$

### Bond Valuation Formula (Combined Fixed and Default Legs)
$$\begin{aligned}
PV_{Bond}(t) &= PV_{Bond\_FL}(t) + PV_{Bond\_DL}(t) \tag{49} \\
&= \sum_{i=1}^{n} c \cdot \Delta T_i \cdot DF(t, T_i) \cdot SP(t, T_i) + \int_{t}^{T} R_s \cdot h(t, s) \cdot DF(t, s) \cdot SP(t, s) ds \tag{50} \\
&\approx \sum_{i=1}^{n} [c + R_i \cdot h(t, T_i)] \cdot \Delta T_i \cdot DF(t, T_i) \cdot SP(t, T_i) + DF(t, T_n) \cdot SP(t, T_n) \tag{51}
\end{aligned}$$

## Simple Hazard Rate Bond Pricing Formula (Flat Parameters)
$$\begin{aligned}
PV_{Bond}(c, r, h, R) &= \sum_{k=1}^{2T} \frac{c}{2} \cdot e^{-k \cdot (r+h)/2} + e^{-T \cdot (r+h)} + \frac{R \cdot h}{r + h} \cdot [1 - e^{-T \cdot (r+h)}] \tag{53} \\
&= 1 + \left[\frac{c}{2} \cdot \frac{1 - e^{-T \cdot (r+h)}}{1 - e^{-(r+h)/2}} - 1 + \frac{R \cdot h}{r + h}\right] \cdot [1 - e^{-T \cdot (r+h)}] \tag{54} \\
&\approx 1 + \left[\frac{c - r - (1 - R) \cdot h}{r + h}\right] \cdot [1 - e^{-T \cdot (r+h)}] \tag{55}
\end{aligned}$$

## Bond Valuation Surface Using Hazard Rate Model 

![500](b090a10c674e9619ed30797c6a98325e.png)

## Yield/Spread Model vs Hazard Rate Model

### Hazard Rate vs Yield/Spread Models (Flat Parameters)

Bond valuation in flat "yield/spread" model:
$$PV_{Bond}(c, r, s) \simeq 1 + \left[\frac{c-r-s}{r+s}\right] \cdot [1-e^{-T \cdot (r+s)}] \tag{56}$$

Bond valuation in flat "hazard rate" model: 
$$PV_{Bond}(c, r, h, R) \simeq 1 + \left[\frac{c-r-(1-R) \cdot h}{r+h}\right] \cdot [1-e^{-T \cdot (r+h)}] \tag{57}$$

Yield/spread model is "simple" case of hazard rate model for
$$R=0, s=h \tag{58}$$

## Bond Pricing in Yield Model vs Hazard Rate Model

Bond trading at 100% "par" price in hazard rate model:
$$PV=1 \iff c=r+(1-R) \cdot h \tag{59}$$

Bond trading at 100% "par" price in yield/spread model:
$$PV=1 \iff c=y=r+s \tag{60}$$

Model translations:
$$y=c=r+(1-R) \cdot h \tag{61}$$
$$s=(1-R) \cdot h \tag{62}$$

## Summary of Hazard Rate Model

- By construction, recovery rates R are increasing with seniority rank in the capital structure
  - Preferred Equity ~0%
  - Subordinated ~20%
  - Senior Unsecured ~40%
  - Senior Secured ~ 65%
  - Senior Loan (First Lien) ~80%
- When using the hazard rate model, bonds of all seniorities are priced simultaneously 
  - using same survival probability/hazard rate curve (default time is common to all instruments) 
  - ... but different recovery rates.
- Consistent framework for identifying dislocations across maturities and seniority ranks!

## Credit Curve Shapes: VZ vs US Treasury Yields

![500](63cb053f2afd6bf0d66b64295ea9749b.png)

## Calibration of the Hazard Rate Model

- Decide on a functional form for the Hazard Rate curve:
  - piece-wise constant (or linear) curve on pivot maturities grid (e.g. 1Y, 2Y, 3Y, 5Y, 7Y, 10Y, 20Y and 30Y) 
  - or use smooth parametric curve shapes (e.g. Nelson-Siegel)
- Agree on issuer recovery rates by seniority ranks
  - use historical averages: ~40% recovery for CDS and senior unsecured bonds 
  - ... or calibrate recovery rates from market prices
- Select weights for instrument used as calibration inputs
  - usually weights are proportional to liquidity 
  - and inversely proportional to risk/DV01
- Run calibration process: sequential bootstrapping vs numerical minimization of residual errors

## Fair Value Prices and "Model Edges"

- Use jointly calibrated Hazard Rates model to compute model prices for arbitrary credit instruments:
  - for instruments used as calibration inputs: bonds and CDS 
  - ... as well as instruments outside the calibration set: less liquid, off-the-run, new issues bonds, etc 
- One can think of the calibrated model price as the "Fair Value" price for an instrument 
- The difference between market and model/fair value prices (distance to fair value) is called "model edge"

## Example: Bond vs CDS Basis Arbitrage

- For any credit issuer, cash bonds and synthetic CDS are linked to same default event! 
- CDS usually used to hedge the credit default risk of a "long" risky bond position 
- Bond "intrinsic" prices (priced on CDS calibrated curve) and market prices "should be close" 
- Option Adjusted Spread/OAS = "market - intrinsic" bond price 
- OAS "dislocated" from zero => opportunity for bond vs CDS basis arbitrage trade!

## Bond vs CDS Basis Example: VZ Curve 

![500](7152aea3e4bab8153540da4ee622c989.png)

## Q&A

- Hazard rate model formulas 
- CDS pricing 
- Bond pricing
- Yield vs. Hazard Rate pricing models 
- Risks and sensitivities 
- Credit Calibration 
- Model Prices and Edges
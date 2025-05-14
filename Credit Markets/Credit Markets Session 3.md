---
title: Credit Markets Session 3
tags:
  - cds_pricing
  - credit_markets
  - default_probabilities
  - hazard_rate
  - risk_neutral
aliases:
  - CDS
  - Credit Derivatives
key_concepts:
  - CDS cash flows
  - Default probabilities
  - Discount factor curve
  - Forward interest rates
  - Hazard rate model
  - Recovery rate
  - Risk neutral valuation
---

# Credit Markets Session 3
1. [[Copulas and the Modeling of Default Correlatio|CDS pricing]] in the [[Credit Market Session 2|Hazard Rate Model]]
	- CDS cash-flows
	- [[Copulas and the Modeling of Default Correlatio|CDS pricing]]
	- [[RISK NEUTRAL VALUATION FRAMEWORK FOR CREDIT DEFAULT SWAPS|Hazard Rates]]
	- ISDA [[Credit Markets Homework 4|CDS Hazard Rate]] model
	- Simple [[Copulas and the Modeling of Default Correlatio|CDS pricing]] formulas
1. Bond [[Arbitrage Pricing of Derivatives|pricing]] in the [[Credit Market Session 2|Hazard Rate Model]]
	- Generic bond [[Arbitrage Pricing of Derivatives|pricing]]
	- Simple bond [[Arbitrage Pricing of Derivatives|pricing]] formulas
	- Yield/spread model vs [[Credit Market Session 2|hazard rate model]]
1. [[Credit Markets Session 4|Calibration]],  [[Credit Markets Session 4|Model Prices]] & Edges
	- [[Credit Markets Session 4|Calibration]] of the [[Credit Market Session 2|Hazard Rate Model]] Model
	- Prices and Edges
1. Q&A

## REMINDER : CDS CASH-FLOWS DIAGRAM

 ![500](02e885a66702d7f24bcf990b5c66ca08.png)

## CDS CUMULATIVE CASH-FLOWS (PREMIUM AND DEFAULT LEGS)

 ![500](590457ab2abdc6df18add125abb4adb4.png)

## RISK NEUTRAL VALUATION FRAMEWORK
- Each instrument uniquely defined by its cumulative future cash-flows
$$CF(t),     \quad t\geq0\tag{1}$$

- [[Teaching Note 7-Exotic Options And Derivative Pricing By Monte Carlo Simulation|Risk neutral]] valuation: use a "market implied" probability measure $\mathbb{P}$ for determining prices of securities
- Bank savings account security B used as numeraire for discounting future cash-flows:
$$B(t)=e^{\int_{0}^{t}r_{\mathrm{s}}d s},     \,     t\geq0$$

- Present value obtained as
$$P V\left(t\right)=B(t)\cdot\mathbb{E}\left[\int_{t}^{\infty}B(s)^{-1}\cdot d C F(s)|{\mathcal{F}}_{t}\right]$$

## SIMPLE CASE: DETERMINISTIC INTEREST RATES
- We consider the simple case of [[RISK NEUTRAL VALUATION FRAMEWORK FOR CREDIT DEFAULT SWAPS|deterministic interest rates]] The "time value of money" at time t for time s is captured in the calibrated [[Credit Markets Session 3|discount factor curve]]:
$$DF(t,     s)=B(t)\cdot\mathbb{E}\left[B(s)^{-1}|\mathcal{F}_{t}\right]=e^{-\int_{t}^{s}r_{u}du},     \ 0\leq t\leq s\tag{3}$$

- The risk free valuation formula simplifies to
$$PV\left(t\right)=\mathbb{E}\left[\int_{t}^{\infty}DF(t,     s)\cdot dCF(s)|\mathcal{F}_{t}\right]\tag{4}$$

- Same formula holds when security cash-flows and [[Interest Rate Quotations|interest rates]] are independent

## CDS PREMIUM/FIXED LEG CASH-FLOWS
- Quarterly [[Realized Returns|coupon payments]] until maturity $T = T_n$:
- We denote the random/stochastic issuer default time by
- Cumulative Premium Leg cash-flows have stochastic dependence on t:
$$c_{i}\cdot\mathbb{I}_{\{s\geq T_{i}\}}\cdot\mathbb{I}_{\{\tau>T_{i}\}}\qquad\qquad(6)$$

## VALUATION FRAMEWORK FOR CREDIT-RISKY CASH-FLOWS
- We assume DF(t,  s) is the deterministic risk-free [[Discount Factors|discount factor]] (as of time t,  for time s). The DF(t,  .) curve can be calibrated from market quotes via bootstrapping.
- Reminder: $t ∈ [0,     \infty)$ is the random/stochastic issuer default time
- Market implied issuer survival & [[Credit Markets Session 3|default probabilities]]:
$$SP\left(t,     s\right):=\mathbb{P}\left(\tau>s|\tau>t\right),     \ \ 0\leq t\leq s,     \tag{7}$$
$$DP\left(t,     s\right):=\mathbb{P}\left(\tau\leq s|\tau>t\right)=1-SP\left(t,     s\right).\tag{8}$$

## RISK NEUTRAL VALUATION OF CDS PREMIUM/FIXED LEG

INTUITIVE INTERPRETATION: PREMIUM LEG

- Present value of risky contractual cash-flows
$$PV_{\mathit{CDS\_PL}}\left(t\right)=\sum_{i=1}^{n}c_{i}\cdot DF(t,     \,     T_{i})\cdot SP(t,     \,     T_{i})\tag{14}$$

- is obtained by summing up the cash-flows amounts $c_i$
- … multiplied with the discount factors $DF(t,      T_i)$ at cash-flow times $T_i$ (time value of money)
- … and multiplied with probability $SP(t,      T_i)$ of issuer being "alive" at cash-flow time $T_i$ ([[Quantitative Trading Strategies Lecture Notes|credit risk]] "adjuster")

## CDS DEFAULT/LOSS LEG CASH-FLOWS

- [[Credit Markets Session 3|Recovery Rate]] given default denoted by R
- For simplicity ("basic model") we assume R is constant
- Think of R as the expected (average) [[Credit Markets Session 3|recovery rate]] for a given issuer and seniority rank
- Default Leg cash-flows until time s are given by:
$$D L\left(s\right):=\left(1-R\right)\cdot\mathbb{I}_{\left\{\tau\leq s\right\}}\tag{15}$$

## VALUATION OF CDS DEFAULT/LOSS LEG (USING FUBINI)
$$PV_{CDS \_{}DL} (t) ==\mathbb{E}\left[\int_{t}^{T}\left(1-R\right)\cdot DF(t,     s)\cdot d\mathbb{I}_{\left\{\tau\leq s\right\}}|\tau>t\right.$$$$=\int_{t}^{T}\left(1-R\right)\cdot DF(t,     s)\cdot d\mathbb{I}$$$$=\left(1-R\right)\cdot\int_{t}^{T}DF(t,     s)\cdot d\mathbb{P}\left(\tau\leq s|\tau>t\right)\tag{19}$$$$=\left(1-R\right)\cdot\int_{t}^{T}DF(t,     s)\cdot dDP(t,     s).\tag{20}$$$$\left[\mathbf{I}_{\{\tau\leq s\}}|\tau>t\right]$$

## INTUITIVE INTERPRETATION: DEFAULT LEG

Present value of loss payment at (random) issuer default time$$
P V_{C D S_{-}D{\it L}}\left(t\right)=\int_{t}^{T}\left(1-R\right)\cdot D F(t,  s)\cdot d D P(t,  s) \tag{21}

$$
Obtained by splitting the time until maturity $[t,      T]$ in infinitesimal (one day) intervals and summing up the loss amount on each interval: $1 − R$
… multiplied with the [[Discount Factors|discount factor]] for that interval: $DF(t,      s)$ … and multiplied with the incremental probability of default on that interval: $*dDP*(t,      s)$.

## HAZARD RATES QUICK RECAP ON DISCOUNT FACTORS AND FORWARD INTEREST RATES
- Forward [[Interest Rate Quotations|interest rates]] $f (t,      s),      s ≥ t$ represent information about [[Interest Rate Quotations|interest rates]] at future time $s$,      as seen from time $t$. 
- Information is contained in today's [[The Vasicek Model|term structure]] of spot [[Interest Rate Quotations|interest rates]] (discount curves).
- [[Forward Points in Currency|Forward rate]] curves $f (t,     .)$ are defined implicitly from [[Discount Factors|Discount Factor]] curves:$$DF(t,     s)=\exp\left[-\int_{t}^{s}f\left(t,     u\right)du\right],     \ \ 0\leq t\leq s,     \tag{22}$$
… or defined explicitly as
$$f\left(t,     s\right)=-\frac{\partial}{\partial s}\ln\left[D F\left(t,     s\right)\right]=-\frac{1}{D F(t,     s)}\cdot\frac{\partial D F}{\partial s}\left(t,     s\right).\tag{23}$$

## HAZARD RATES HAZARD RATES (A.K.A. DEFAULT INTENSITIES)
- [[RISK NEUTRAL VALUATION FRAMEWORK FOR CREDIT DEFAULT SWAPS|Hazard rates]] $h (t,      s)$ represent infinitesimal probabilities of default at future time $s$,      using market information as of time $t$. Similar concept to forward [[Interest Rate Quotations|interest rates]].
- [[Advanced Usage of QuantLib analytics library|Hazard rate curves]] $h (t,     .)$ defined implicitly from [[A Poisson Model of Single Issuer Default|Survival Probability]] curves:$$SP(t,     s)=\exp\left[-\int_{t}^{s}h\left(t,     u\right)du\right],     \ \ 0\leq t\leq s,     \tag{24}$$
… or defined explicitly as$$h\left(t,     s\right)=-\frac{\partial}{\partial s}\ln\left[SP\left(t,     s\right)\right]=-\frac{1}{SP(t,     s)}\cdot\frac{\partial SP}{\partial s}\left(t,     s\right).\tag{25}$$
## PROPERTIES OF HAZARD RATES
[[RISK NEUTRAL VALUATION FRAMEWORK FOR CREDIT DEFAULT SWAPS|Hazard rates]] $h (t,      s)$ quantify [[A Deterministic Credit Migration Model|conditional probabilities]] of default "around" specific times $s$ in the future$$\mathbb{P}\left(s<\tau<s+\epsilon|\tau>s,     \tau>t\right)\tag{26}$$$$=\frac{\mathbb{P}\left(s<\tau<s+\epsilon|\tau>t\right)}{\mathbb{P}\left(\tau>s|\tau>t\right)}$$$$ =\frac{SP(t,     s)-SP(t,     s+\epsilon)}{SP(t,     s)}$$ $$=1-\exp\left[-\int_{s}^{s+\epsilon}h\left(t,     u\right)du\right]$$$$\simeq h\left(t,     s\right)\cdot\epsilon,     \ \ 0\leq t\leq s.$$

## VALUATION OF CDS DEFAULT/LOSS LEG USING HAZARD RATES
$$PV_{\mathit{CDS\_DL}}\left(t\right)=\left(1-R\right)\cdot\int_{t}^{T}DF(t,     s)\cdot dDP(t,     s)\tag{27}$$

 $$=\left(1-R\right)\cdot\int_{t}^{T}DF(t,     s)\cdot d\left[1-SP(t,     s)\right]\tag{28}$$$$=-\left(1-R\right)\cdot\int_{t}^{T}DF(t,     s)\cdot dSP(t,     s)\tag{29}$$ $$=\left(1-R\right)\cdot\int_{t}^{T}h\left(t,     s\right)\cdot DF(t,     s)\cdot SP(t,     s)\cdot ds.\tag{30}$$$$PV_{\mathit{CDS\_DL}}\left(t\right)=\left(1-R\right)\cdot\int_{t}^{T}h\left(t,     s\right)\cdot DF(t,     s)\cdot SP(t,     s)\cdot ds$$
$$=\sum_{i=1}^{n}\left(1-R\right)\cdot\int_{T_{i-1}}^{T_{i}}h\left(t,     s\right)\cdot DF(t,     s)\cdot SP(t,     s)\cdot ds\tag{31}$$
$$\simeq\sum_{i=1}^{n}\left(1-R\right)\cdot h\left(t,     T_{i}\right)\cdot\Delta T_{i}\cdot DF(t,     T_{i})\cdot SP(t,     T_{i}).\tag{32}$$

## CDS VALUATION (RECEIVING PREMIUM C,      PAYING DEFAULT/LOSS LEG)
$$PV_{CDS}\left(t\right)=PV_{CDS\_PL}\left(t\right)-PV_{CDS\_PL}\left(t\right)\tag{33}$$
$$=\sum_{i=1}^{n}c_{i}\cdot DF(t,     \,     T_{i})\cdot SP(t,     \,     T_{i})$$
$$-\left(1-R\right)\cdot\int_{t}^{T}h\left(t,     s\right)\cdot DF(t,     s)\cdot SP(t,     s)\cdot ds$$
$$\simeq\sum_{i=1}^{n}\left[c-\left(1-R\right)\cdot h\left(t,     \,     T_{i}\right)\right]\cdot\Delta T_{i}\cdot DF(t,     \,     T_{i})\cdot SP(t,     \,     T_{i}).\tag{34}$$

## CDS DURATION AND PARSPREAD
- [[RISK NEUTRAL VALUATION FRAMEWORK FOR CREDIT DEFAULT SWAPS|CDS Duration]] defined as the "Unit" 1bp Premium Leg PV 
- CDS Premium Leg valuation via [[Key Rates O1s Durations and Hedging|Duration]]:
- ParSpread defined from [[The Default Correlation of the Reference Issuer|CDS Default]] Leg and [[Key Rates O1s Durations and Hedging|Duration]]: 
- 
- CDS valuation:
#### CDS DURATION DEFINED AS THE "UNIT" 1BP PREMIUM LEG PV$$ Duration(t) := \sum_{i=1}^{n} \Delta T_{i} \cdot DF(t,      T_{i}) \cdot SP(t,      T_{i}) \tag{35}$$
#### CDS PREMIUM LEG VALUATION VIA DURATION:$$ PV_{CDS\_PL} (t) = c \cdot Duration(t) \tag{36}$$
#### PARSPREAD DEFINED FROM CDS DEFAULT LEG AND DURATION:$$ PV_{CDS\_DL} (t) = ParSpread(t) \cdot Duration(t) \tag{37}$$
#### CDS VALUATION:$$ PV_{CDS} (t) = [c - ParSpread(t)] \cdot Duration(t) \tag{38}$$
## CDS PAR SPREADS,      PRICES VS UPFRONTS FOR DIFFERENT MATURITIES
- Standardized CDS maturities: 1Y,      2Y,      3Y,      4Y,      5Y,      7Y,      10Y 
- CDS Par Spreads: measure the "market implied" issuer default risks for the given maturities. 
- They are one-to-one to (and can be "bootstrapped" from) CDS prices and survival probabilities.
- "CDS PV" = price from the point of view of a CDS [[Credit Default Swaps|protection seller]] (long [[Quantitative Trading Strategies Lecture Notes|credit risk]]) 
- "[[CDS Upfront Amounts|CDS Upfront]]" = price from the point of view of a CDS [[Credit Default Swaps|protection buyer]] (short [[Quantitative Trading Strategies Lecture Notes|credit risk]]) 
- "[[CDS Upfront Amounts|CDS Upfront]]" = - "CDS PV"
## CDS DURATION AND PARSPREAD FORMULAS

## CDS TRADES "AT PAR" WHEN PARSPREAD MATCHES THE COUPON:
- $$ PV_{CDS} (t) = 0 \leftrightarrow ParSpread(t) = c \tag{39}$$

## CDS PARSPREAD MEASURES THE CREDIT RISK OF THE CDS CONTRACT
- $$ ParSpread(t) \approx (1 - R) \cdot h \tag{40}$$
## CDS CS01 DEFINED AS \(\DELTA PV\) FOR -1BP CHANGE IN PARSPREAD:$$ CS01_{CDS} (t,      s) := PV_{CDS} (t,      s - 1bp) - PV_{CDS} (t,      s) $$ $$ \approx [c - s + 1bp] \cdot Duration(t) - [c - s] \cdot Duration(t) $$$$ = Duration(t) \tag{41}$$## ISDA CDS HAZARD RATE MODEL ISDA CDS STANDARD PRICING & QUOTING MODEL

Deterministic [[Advanced Usage of QuantLib analytics library|discount curve]]: ISDA SOFR Constant recovery R,      constant hazard rate h Default Leg computed via numerical integration$$PV_{\mathit{CDS}}\left(t,     c,     h,     R\right)=PV_{\mathit{CDS}\_\mathit{PL}}\left(t,     c,     h,     R\right)-PV_{\mathit{CDS}\_\mathit{PL}}\left(t,     h,     R\right)$$
$$=\sum_{i=1}^{n}c_{i}\cdot DF(t,     T_{i})\cdot e^{\left(t-T_{i}\right)\cdot h}-\left(1-R\right)\cdot h\cdot\int_{t}^{T}DF(t,     s)\cdot e^{\left(t-s\right)\cdot h}ds$$
$$\simeq\sum_{i=1}^{n}\left[c-\left(1-R\right)\cdot h\right]\cdot\Delta T_{i}\cdot DF(t,     T_{i})\cdot e^{\left(t-T_{i}\right)\cdot h}$$$$ \sum_{i=1}^{n}\left[c-(1-R)\cdot h\right]\cdot\Delta T_{i}\cdot e^{(t-T_{i})\cdot(r_{i}+h)}.\tag{42}$$

## SIMPLE CDS VALUATION WITH CONSTANT PARAMETERS$$ PV_{CDS} (c,      r,      h,      R,      T) = \tag{43} $$$$ = \sum_{k=1}^{4T} \frac{c}{4} \cdot e^{-k \cdot (r+h)/4} - \frac{(1 - R) \cdot h}{r + h} \cdot \left[ 1 - e^{-T \cdot (r+h)} \right] \tag{44} $$$$ = \left[ \frac{c/4}{e^{(r+h)/4} - 1} - \frac{(1 - R) \cdot h}{r + h} \right] \cdot \left[ 1 - e^{-T \cdot (r+h)} \right] \tag{45} $$$$ \approx \left[ c - (1 - R) \cdot h \right] \cdot \frac{1 - e^{-T \cdot (r+h)}}{r + h} \tag{46} $$
## CDS VALUATION SURFACE (5% FLAT INTEREST RATES,      5% COUPON) 
 ![500](ff4daa49d51e35f704363ecc48e1f397.png)
ISDA CDS "CURVE SHAPE" MODEL
- Uses reference ISDA SNAC [[Advanced Usage of QuantLib analytics library|discount curve]],      flat recovery and piece-wise constant hazard rate 
- Calibrate piece-wise flat hazard rate curve using sequential "Bootstrapping" over CDS maturities 
- Standard CDS maturities:
	- 1Y,      2Y,      3Y,      5Y,      7Y and 10Y
- ISDA SNAC swap/[[Advanced Usage of QuantLib analytics library|discount curve]] definition:
	- Curve calibrated to 3M [[A Guide to the Front End and [[Basis Swaps|Basis Swap]] Markets#[[Short-Term Rates and the Transition from LIBOR|London Interbank Offered Rate]] (LIBOR)|LIBOR]] until Oct 2022 
	- Curve calibrated to 3M SOFR after Oct 2022
 ![500](bcf4324ce737732237aa9cd687528bcf.png)
##  BOND PRICING IN THE HAZARD RATE MODEL 
#### FIXED LEG VALUATION:
- Risky semi-annual coupons $c$ at times $\{ T_i \}^n_{i=1}$ and principal payment at maturity $T = T_n$$$ PV_{Bond\_FL} (t) = \sum_{i=1}^{n} c \cdot \Delta T_i \cdot DF(t,      T_i) \cdot SP(t,      T_i) + DF(t,      T_n) \cdot SP(t,      T_n) \tag{47} $$
  #### DEFAULT LEG VALUATION:
- Bond pays recovery value $R_i$ at default time $\tau \in [T_{i-1},      T_i]$,      if issuer defaults before maturity $T$$$ PV_{Bond\_DL} (t) = \int_{t}^{T} R_s \cdot h(t,      s) \cdot DF(t,      s) \cdot SP(t,      s) \,      ds $$
$$$ \approx \sum_{i=1}^{n} R_i \cdot h(t,      T_i) \cdot \Delta T_i \cdot DF(t,      T_i) \cdot SP(t,      T_i) \tag{48} $$
#### BOND VALUATION FORMULA (COMBINED FIXED AND DEFAULT LEGS)$$ PV_{Bond} (t) = PV_{Bond\_FL} (t) + PV_{Bond\_DL} (t) \tag{49} $$$$ = \sum_{i=1}^{n} c \cdot \Delta T_i \cdot DF(t,      T_i) \cdot SP(t,      T_i) + \int_{t}^{T} R_s \cdot h(t,      s) \cdot DF(t,      s) \cdot SP(t,      s) ds \tag{50}$$ $$ \approx \sum_{i=1}^{n} [c + R_i \cdot h(t,      T_i)] \cdot \Delta T_i \cdot DF(t,      T_i) \cdot SP(t,      T_i) + DF(t,      T_n) \cdot SP(t,      T_n) \tag{51}$$
## SIMPLE HAZARD RATE BOND PRICING FORMULA (FLAT PARAMETERS)$$ PV_{Bond} (c,      r,      h,      R) = \tag{52} $$$$ = \sum_{k=1}^{2T} \frac{c}{2} \cdot e^{-k \cdot (r+h)/2} + e^{-T \cdot (r+h)} + \frac{R \cdot h}{r + h} \cdot [1 - e^{-T \cdot (r+h)}] \tag{53} $$$$ = 1 + \left[\frac{c}{2} - \frac{(e^{\frac{r+h}{2}} - 1)}{e^{\frac{r+h}{2}} - 1}\right] \cdot \frac{R \cdot h}{r + h} \cdot [1 - e^{-T \cdot (r+h)}] \tag{54} $$$$ \approx 1 + \left[ \frac{c - r - (1 - R) \cdot h}{r + h} \right] \cdot [1 - e^{-T \cdot (r+h)}] \tag{55} $$

## BOND VALUATION SURFACE USING HAZARD RATE MODEL 
 ![500](b090a10c674e9619ed30797c6a98325e.png)

## YIELD/SPREAD MODEL VS HAZARD RATE MODEL HAZARD RATE VS YIELD/SPREAD MODELS (FLAT PARAMETERS)
Bond valuation in flat "yield/spread" model:$$PV_{Bond}\left(c,     r,     s\right)\simeq1+\left[\frac{c-r-s}{r+s}\right]\cdot\left[1-e^{-T\cdot\left(r+s\right)}\right]\,     .\tag{56}$$
Bond valuation in flat "hazard rate" model: $$PV_{Bond}\left(c,     r,     h,     R\right)\simeq1+\left[\frac{c-r-\left(1-R\right)\cdot h}{r+h}\right]\cdot\left[1-e^{-T\cdot\left(r+h\right)}\right]\tag{57}$$
Yield/spread model is "simple" case of [[Credit Market Session 2|hazard rate model]] for$$R=0,      s=h\tag{58}$$

## BOND PRICING IN YIELD MODEL VS HAZARD RATE MODEL
Bond trading at 100% "par" price in [[Credit Market Session 2|hazard rate model]]:$$PV=1\iff c=r+(1-R)\cdot h.\tag{59}$$
Bond trading at 100% "par" price in yield/spread model:
$$PV=1\iff c=y=r+s\tag{60}$$
Model translations:$$y=c=r+(1-R)\cdot h\tag{61}$$$$s=(1-R)\cdot h\tag{62}$$

## YIELD/SPREAD MODEL VS HAZARD RATE MODEL 
SUMMARY OF [[Credit Market Session 2|HAZARD RATE MODEL]]
- By construction,      recovery rates R are increasing with seniority rank in the [[Introduction to Corporate Finance|capital structure]]
	- Preferred Equity ~0%
	- Subordinated ~20%
	- Senior Unsecured ~40%
	- Senior Secured ~ 65%
	- Senior Loan (First Lien) ~80%
- When using the [[Credit Market Session 2|hazard rate model]],      bonds of all seniorities are priced simultaneously 
	- using same [[A Poisson Model of Single Issuer Default|survival probability]]/hazard rate curve (default time is common to all instruments) 
	- … but different recovery rates.
- Consistent framework for identifying dislocations across maturities and [[Credit Markets Session 1|seniority ranks]]!
[[Advanced Usage of QuantLib analytics library|CREDIT CURVE]] SHAPES: VZ VS US TREASURY YIELDS [[Credit Markets Session 4|CALIBRATION]] OF THE [[Credit Market Session 2|HAZARD RATE MODEL]] 
 ![500](63cb053f2afd6bf0d66b64295ea9749b.png)

[[Credit Markets Session 4|CALIBRATION]] OF THE [[Credit Market Session 2|HAZARD RATE MODEL]]
- Decide on a functional form for the Hazard Rate curve:
	- piece-wise constant (or linear) curve on pivot maturities grid (e.g. 1Y,      2Y,      3Y,      5Y,      7Y,      10Y,      20Y and 30Y) 
	- or use smooth parametric curve shapes (e.g. Nelson-Siegel)
- Agree on issuer recovery rates by [[Credit Markets Session 1|seniority ranks]]
	- use historical averages: ~40% recovery for CDS and senior unsecured bonds 
	- … or calibrate recovery rates from market prices
- Select weights for instrument used as [[Credit Markets Session 4|calibration]] inputs
	- usually weights are proportional to [[Class Note 10 Liquidity and Class Note 10 Liquidity and Liquidity Managementliquidity management|liquidity]] 
	- and inversely proportional to risk/DV01
- Run [[Credit Markets Session 4|calibration]] process: sequential bootstrapping vs numerical minimization of residual errors

## FAIR VALUE PRICES AND "MODEL EDGES"
- Use jointly calibrated [[RISK NEUTRAL VALUATION FRAMEWORK FOR CREDIT DEFAULT SWAPS|Hazard Rates]] model to compute [[Credit Markets Session 4|model prices]] for arbitrary credit instruments:
	- for instruments used as [[Credit Markets Session 4|calibration]] inputs: bonds and CDS 
	- … as well as instruments outside the [[Credit Markets Session 4|calibration]] set: less liquid,      off-the-run,      new issues bonds,      etc 
- Once can think of the calibrated model price as the "Fair Value" price for an instrument 
- The difference between market and model/fair value prices (distance to fair value) is called "model edge"

## EXAMPLE: BOND VS CDS BASIS ARBITRAGE
- For any credit issuer,      cash bonds and synthetic CDS are linked to same default event! 
- CDS usually used to hedge the [[Credit Markets Session 5|credit default risk]] of a "long" risky bond position 
- Bond "intrinsic" prices (priced on CDS calibrated curve) and market prices "should be close" 
- Option Adjusted Spread/OAS = "market - intrinsic" bond price 
- OAS "dislocated" from zero =) opportunity for bond vs CDS basis [[PSET 1 Solution-Financial Instruments|arbitrage trade]]!

## BOND VS CDS BASIS EXAMPLE: VZ CURVE 
 ![500](7152aea3e4bab8153540da4ee622c989.png)
## Q &A
- [[Credit Market Session 2|Hazard rate model]] formulas 
- [[Copulas and the Modeling of Default Correlatio|CDS pricing]] Bond [[Arbitrage Pricing of Derivatives|pricing]]
- Yield vs. Hazard Rate [[Arbitrage Pricing of Derivatives|pricing]] models 
- Risks and sensitivities 
- Credit [[Credit Markets Session 4|Calibration]] 
- [[Credit Markets Session 4|Model Prices]] and Edges
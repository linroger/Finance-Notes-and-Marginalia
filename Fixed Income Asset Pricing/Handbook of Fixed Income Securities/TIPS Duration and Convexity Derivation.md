---
title: Untitled
cssclasses: academia
tags:
  - convexity
  - inflation_linked_bonds
  - nominal_bonds
  - real_yield
  - tips_duration
aliases:
  - Inflation-Linked Bonds
  - Nominal Bonds
  - TIPS
key_concepts:
  - Bond pricing formulas
  - Continuous compounding
  - Duration definition
  - Inflation index factor
  - Real vs nominal yield
---

# TIPS Duration and Convexity Derivation
Below is a greatly expanded and highly detailed step-by-step derivation of the key formulas for [pricing](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%207/Arbitrage%20Pricing%20of%20Derivatives.md), [duration](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%205/Key%20Rates%20O1s%20Durations%20and%20Hedging.md), and [convexity](../Problem%20Sets/PSET%20II%20Fixed%20Income%20Asset%20Pricing%201.md) of both nominal and [inflation](../../International%20Finance/Bridgewater/Principles%20For%20Navigating%20Big%20Debt%20Cycles/Part%20II%20Detailed%20Case%20Studies/German%20Debt%20Crisis%20andHyperinflation%20(1918–1924)/War%20Economies%20and%20Hyperinflation.md)-linked (TIPS) bonds, mirroring the style of specificity you requested. We will show how each expression is derived with a focus on “showing all the work.” Where relevant, we will also provide commentary on underlying assumptions (e.g., [continuous compounding](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%202/Interest%20Rate%20Quotations.md), the concept of [real vs. nominal](../../Financial%20Markets/Financial%20Asset%20Pricing%20Theory%20Overview/Chapter%204%20-%20State%20Prices/Nominal%20and%20Real%20State-Price%20Deflators.md) yield, the [inflation index factor](.md)).
Part 1: Preliminaries and Notation
	1.	Action: Introduce notation and define the concept of price, yield, and indexing for both nominal and [inflation](../../International%20Finance/Bridgewater/Principles%20For%20Navigating%20Big%20Debt%20Cycles/Part%20II%20Detailed%20Case%20Studies/German%20Debt%20Crisis%20andHyperinflation%20(1918–1924)/War%20Economies%20and%20Hyperinflation.md)-linked bonds.
	2.	Mathematical Work:
	•	Nominal bond:$$	\begin{align}
P_{\text{nom}}(0) = \text{price of the nominal bond at time } t=0, \\
C_{\text{nom}} = \text{(annual) coupon rate (as a decimal),}\\
F = \text{face value of the bond (par value),}\\
y = \text{the continuously compounded (nominal) yield to maturity,}\\
t_i = \text{the time in years (from now, }t=0\text{) at which coupon } i \text{ is paid, for } i=1,2,\dots,N,\\
N = \text{the total number of future coupon payments until maturity.}\\
\end{align}$$
	•	[Inflation](../../International%20Finance/Bridgewater/Principles%20For%20Navigating%20Big%20Debt%20Cycles/Part%20II%20Detailed%20Case%20Studies/German%20Debt%20Crisis%20andHyperinflation%20(1918–1924)/War%20Economies%20and%20Hyperinflation.md)-linked bond (TIPS):$$
\begin{align}
P_{\text{TIPS}}(0) = \text{price of the TIPS at time } t=0, \\
C_{\text{TIPS}} = \text{(annual) coupon rate on the TIPS, as a decimal,}\\
y_{\text{real}} = \text{the continuously compounded real yield of the TIPS,}\\
I(0) = \text{the inflation index (CPI) at issuance or at the settlement date},\\
I(t_i) = \text{the inflation index at time } t_i,\\
\frac{I(t_i)}{I(0)} = \text{the inflation index ratio, used to scale the principal.}\\
\end{align}$$
	3.	Reasoning: We establish the fundamental building blocks to price the bonds. A nominal bond’s coupons and redemption value do not change with [inflation](../../International%20Finance/Bridgewater/Principles%20For%20Navigating%20Big%20Debt%20Cycles/Part%20II%20Detailed%20Case%20Studies/German%20Debt%20Crisis%20andHyperinflation%20(1918–1924)/War%20Economies%20and%20Hyperinflation.md), whereas a TIPS’s coupons and redemption value do adjust based on the ratio ￼.
Part 2: Price of a Nominal (Coupon) Bond
	1.	Action: Derive the standard formula for the present value (price) of all cash flows from a nominal coupon bond under [continuous compounding](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%202/Interest%20Rate%20Quotations.md).
	2.	Mathematical Work:
	•	A nominal coupon bond pays coupon $\bigl(C_{\text{nom}} \times F\bigr)$ at each coupon date ￼ for ￼, plus the face value ￼ at the final date ￼.
	•	Under [continuous compounding](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%202/Interest%20Rate%20Quotations.md), the [discount factor](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%201/Discount%20Factors.md) for a [cash flow](../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%201%20-%20Purpose%20and%20Structure%20of%20Financial%20Markets/Preview%20of%20the%20Book.md) at time ￼ is ￼.
	•	Hence, the present value of the nominal bond’s [future cash flows](../../Financial%20Engineering/Advanced%20Derivatives%20Pricing%20Methodology.md) is$$
P_{\text{nom}}(0)
= \sum_{i=1}^{N-1} \Bigl( C_{\text{nom}} \, F \Bigr) e^{-y\,t_i}
+ \Bigl( C_{\text{nom}} \, F + F \Bigr)e^{-y\,t_N}.
$$
In a more compact notation (since the final coupon is just coupon plus principal),$$
P_{\text{nom}}(0)
= \sum_{i=1}^{N} \bigl( C_{\text{nom}}\,F \bigr) e^{-y\,t_i} \;+\; F \, e^{-y\,t_N}.
$$
	3.	Reasoning: Each coupon is discounted back to ￼ by multiplying by ￼. The final redemption includes the last coupon plus the face value ￼. This is standard bond-[pricing](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%207/Arbitrage%20Pricing%20of%20Derivatives.md) procedure under [continuous compounding](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%202/Interest%20Rate%20Quotations.md).
Part 3: Price of a TIPS ([Inflation](../../International%20Finance/Bridgewater/Principles%20For%20Navigating%20Big%20Debt%20Cycles/Part%20II%20Detailed%20Case%20Studies/German%20Debt%20Crisis%20andHyperinflation%20(1918–1924)/War%20Economies%20and%20Hyperinflation.md)-Linked Bond)
	1.	Action: Recognize that TIPS principal is adjusted by [inflation](../../International%20Finance/Bridgewater/Principles%20For%20Navigating%20Big%20Debt%20Cycles/Part%20II%20Detailed%20Case%20Studies/German%20Debt%20Crisis%20andHyperinflation%20(1918–1924)/War%20Economies%20and%20Hyperinflation.md). We incorporate the real yield and [inflation](../../International%20Finance/Bridgewater/Principles%20For%20Navigating%20Big%20Debt%20Cycles/Part%20II%20Detailed%20Case%20Studies/German%20Debt%20Crisis%20andHyperinflation%20(1918–1924)/War%20Economies%20and%20Hyperinflation.md) index ratio into the [pricing](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%207/Arbitrage%20Pricing%20of%20Derivatives.md) formula.
	2.	Mathematical Work:
	•	Key difference: the principal at time ￼ is scaled by $\tfrac{I(t_i)}{I(0)}$.
	•	The coupon payment at time ￼ is$$
\Bigl(C_{\text{TIPS}} \times F \times \frac{I(t_i)}{I(0)}\Bigr).
$$
	•	The redemption (principal repayment) at maturity ￼ is
￼
	•	Discounting these real cash flows at the continuously compounded real yield ￼ gives$$
P_{\text{TIPS}}(0)
= \sum_{i=1}^{N} \Bigl( C_{\text{TIPS}} \,F \,\frac{I(t_i)}{I(0)} \Bigr) e^{-\,y_{\text{real}}\,t_i}
\;+\;
\Bigl(F \,\frac{I(t_N)}{I(0)}\Bigr) e^{-\,y_{\text{real}}\,t_N}.
$$
	3.	Reasoning: The TIPS principal “inflates” over time by ￼, and the coupons and principal are discounted at the real yield. Thus, TIPS incorporate expected [inflation](../../International%20Finance/Bridgewater/Principles%20For%20Navigating%20Big%20Debt%20Cycles/Part%20II%20Detailed%20Case%20Studies/German%20Debt%20Crisis%20andHyperinflation%20(1918–1924)/War%20Economies%20and%20Hyperinflation.md) implicitly via these index adjustments.
Part 4: [Duration](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%205/Key%20Rates%20O1s%20Durations%20and%20Hedging.md) – The Formal Definition
	1.	Action: Introduce the concept of [duration](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%205/Key%20Rates%20O1s%20Durations%20and%20Hedging.md) in a way analogous to your example, using [continuous compounding](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%202/Interest%20Rate%20Quotations.md) yields.
	2.	Mathematical Work:
	•	General definition: If ￼ is a bond’s price (or present value of [future cash flows](../../Financial%20Engineering/Advanced%20Derivatives%20Pricing%20Methodology.md)), and ￼ is the continuously compounded yield, we define
￼
	•	Economically, ￼ measures the percentage change in price for a small parallel shift ￼ in the yield curve:
￼
	3.	Reasoning: [Duration](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%205/Key%20Rates%20O1s%20Durations%20and%20Hedging.md) approximates the first-order sensitivity of price to changes in yield. If yields increase slightly by ￼, the price of the bond changes by approximately ￼.
Part 5: [Duration](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%205/Key%20Rates%20O1s%20Durations%20and%20Hedging.md) for a Nominal Coupon Bond (Detailed)
We now apply the definition
￼
Here, ￼ can be the same as ￼ (the continuously compounded nominal yield).
5.1. Express the Bond Price$$
P_{\text{nom}}(0)
= \sum_{i=1}^{N} \Bigl( C_{\text{nom}}\,F \Bigr) e^{-r\,t_i}
	•	F\, e^{-r\,t_N}.
$$
5.2. Take the Derivative w.r.t. ￼
	1.	Action: Differentiate term by term with respect to ￼.
	2.	Mathematical Work (term-by-term differentiation):
	•	For a single coupon [cash flow](../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%201%20-%20Purpose%20and%20Structure%20of%20Financial%20Markets/Preview%20of%20the%20Book.md) $\Bigl(C_{\text{nom}}\,F\Bigr) e^{-r t_i}$:$$
\frac{d}{dr} \Bigl[(C_{\text{nom}}\,F) e^{-r\,t_i}\Bigr]
\;=\;
(C_{\text{nom}}\,F)\,\frac{d}{dr}\bigl(e^{-r\,t_i}\bigr)
\;=\;
(C_{\text{nom}}\,F)\,\bigl(-\,t_i\;e^{-r\,t_i}\bigr).
$$
	•	For the redemption at ￼:$$
\frac{d}{dr}\Bigl[F\,e^{-r\,t_N}\Bigr]
\;=\;
F\,\bigl(-\,t_N\;e^{-r\,t_N}\bigr).
$$
	•	Summing up, we get$$
\frac{d P_{\text{nom}}}{d r}
\;=\;
\sum_{i=1}^{N}
\Bigl( C_{\text{nom}}\,F \Bigr)\bigl(-\,t_i\, e^{-r\,t_i}\bigr)
\;+\;
F\;\bigl(-\,t_N\;e^{-r\,t_N}\bigr).
$$
Factoring out the minus sign:
￼
	3.	Reasoning: Each [cash flow](../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%201%20-%20Purpose%20and%20Structure%20of%20Financial%20Markets/Preview%20of%20the%20Book.md)’s derivative w.r.t. ￼ includes a factor ￼ from the derivative $\frac{d}{dr}\bigl(e^{-r t}\bigr) = -t\,e^{-r t}$.
5.3. Plug Into the [Duration](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%205/Key%20Rates%20O1s%20Durations%20and%20Hedging.md) Formula$$
D_{\text{nom}}
-\,\frac{1}{P_{\text{nom}}}\;\frac{dP_{\text{nom}}}{dr}
-\,\frac{1}{P_{\text{nom}}}
\Bigl[-\sum_{i=1}^{N} t_i\,(C_{\text{nom}}\,F)\,e^{-r\,t_i} - t_N\,F\,e^{-r\,t_N}\Bigr].
$$
Simplify:
￼
5.4. Interpret the Formula
	•	Numerator: Weighted sum of times ￼ where each weight is the present value of the corresponding [cash flow](../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%201%20-%20Purpose%20and%20Structure%20of%20Financial%20Markets/Preview%20of%20the%20Book.md).
	•	Denominator: The total present value of all cash flows (the bond’s price).
Hence,
￼
Part 6: [Duration](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%205/Key%20Rates%20O1s%20Durations%20and%20Hedging.md) for a TIPS (Detailed)
Similarly, we define
￼
But now ￼ is the real yield (continuously compounded). The TIPS price is:$$
P_{\text{TIPS}}(0)
\sum_{i=1}^{N}
\Bigl(C_{\text{TIPS}} \, F\,\frac{I(t_i)}{I(0)}\Bigr)\, e^{-\,r_{\text{real}}\,t_i}
\;+\;
\Bigl(F\,\frac{I(t_N)}{I(0)}\Bigr)\,e^{-\,r_{\text{real}}\,t_N}.
$$
6.1. Take the Derivative w.r.t. ￼
	1.	Action: Differentiate term-by-term.
	2.	Mathematical Work:
	•	Each coupon is $\Bigl(C_{\text{TIPS}} \, F\,\tfrac{I(t_i)}{I(0)}\Bigr)\, e^{-\,r_{\text{real}}\,t_i}$.
	•	Its derivative with respect to ￼ is$$
\frac{d}{dr_{\text{real}}}
\left[
C_{\text{TIPS}} \,F\,\frac{I(t_i)}{I(0)}\,
e^{-\,r_{\text{real}}\,t_i}
\right]
C_{\text{TIPS}}\,F\,\frac{I(t_i)}{I(0)}
\cdot
\bigl(-\,t_i\,e^{-\,r_{\text{real}}\,t_i}\bigr).
$$
	•	For the principal redemption $\bigl(F\,\tfrac{I(t_N)}{I(0)}\bigr)\,e^{-\,r_{\text{real}}\,t_N}$:$$
\frac{d}{dr_{\text{real}}}
\left[
F\,\frac{I(t_N)}{I(0)} \, e^{-\,r_{\text{real}}\,t_N}
\right]
\Bigl(F\,\frac{I(t_N)}{I(0)}\Bigr)
\,\bigl(-\,t_N\,e^{-\,r_{\text{real}}\,t_N}\bigr).
$$
	•	Summing up:$$
\frac{d P_{\text{TIPS}}}{d\,r_{\text{real}}}
-\sum_{i=1}^{N}
t_i\,C_{\text{TIPS}}\,F\,\frac{I(t_i)}{I(0)}\,
e^{-\,r_{\text{real}}\,t_i}
\;-\;
t_N\,\Bigl(F\,\frac{I(t_N)}{I(0)}\Bigr)\,e^{-\,r_{\text{real}}\,t_N}.
$$
6.2. Insert into the [Duration](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%205/Key%20Rates%20O1s%20Durations%20and%20Hedging.md) Formula$$
D_{\text{TIPS}}
-\,\frac{1}{P_{\text{TIPS}}(0)}
\left[
-\sum_{i=1}^{N}
t_i\,C_{\text{TIPS}}\,F\,\frac{I(t_i)}{I(0)}\, e^{-\,r_{\text{real}}\,t_i}
\;-\;
t_N \,\Bigl(F\,\frac{I(t_N)}{I(0)}\Bigr)\,e^{-\,r_{\text{real}}\,t_N}
\right].
$$
Simplify the negatives:$$
D_{\text{TIPS}}
\frac
{
\sum_{i=1}^{N}
t_i\,C_{\text{TIPS}}\,F\,\frac{I(t_i)}{I(0)}\, e^{-\,r_{\text{real}}\,t_i}
+
t_N\,\Bigl(F\,\frac{I(t_N)}{I(0)}\Bigr)\,e^{-\,r_{\text{real}}\,t_N}
}
{ P_{\text{TIPS}}(0) }.
$$
6.3. Interpretation
	•	TIPS [duration](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%205/Key%20Rates%20O1s%20Durations%20and%20Hedging.md) measures sensitivity to changes in the real yield ￼.
	•	In practice, the TIPS price also depends on [inflation](../../International%20Finance/Bridgewater/Principles%20For%20Navigating%20Big%20Debt%20Cycles/Part%20II%20Detailed%20Case%20Studies/German%20Debt%20Crisis%20andHyperinflation%20(1918–1924)/War%20Economies%20and%20Hyperinflation.md) [expectations](../Fixed%20Income%20Lecture%20Notes/FORWARD%20RATES%20AND%20TERM%20STRUCTURE.md) (through the future path of ￼). However, for the standard textbook formula, we treat [inflation](../../International%20Finance/Bridgewater/Principles%20For%20Navigating%20Big%20Debt%20Cycles/Part%20II%20Detailed%20Case%20Studies/German%20Debt%20Crisis%20andHyperinflation%20(1918–1924)/War%20Economies%20and%20Hyperinflation.md) indexation as “projected” and discount by ￼.
Thus,$$
\boxed{
D_{\text{TIPS}}
\frac
{\sum_{i=1}^{N} t_i\,\Bigl(C_{\text{TIPS}}\,F\,\tfrac{I(t_i)}{I(0)}\Bigr)\,e^{-\,r_{\text{real}}\,t_i}
	•	t_N\,\Bigl(F\,\tfrac{I(t_N)}{I(0)}\Bigr)\,e^{-\,r_{\text{real}}\,t_N}}
{ \sum_{i=1}^{N}\Bigl(C_{\text{TIPS}}\,F\,\tfrac{I(t_i)}{I(0)}\Bigr)\,e^{-\,r_{\text{real}}\,t_i}
	•	\Bigl(F\,\tfrac{I(t_N)}{I(0)}\Bigr)\,e^{-\,r_{\text{real}}\,t_N} }
}.
$$
Part 7: [Convexity](../Problem%20Sets/PSET%20II%20Fixed%20Income%20Asset%20Pricing%201.md) – The Formal Definition
Just like [duration](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%205/Key%20Rates%20O1s%20Durations%20and%20Hedging.md) captures the first derivative, [convexity](../Problem%20Sets/PSET%20II%20Fixed%20Income%20Asset%20Pricing%201.md) measures the [second derivative of price](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%204/Convexity.md) w.r.t. yield. Formally:
￼
	•	With [continuous compounding](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%202/Interest%20Rate%20Quotations.md), we again let ￼ be either ￼ (nominal yield) or ￼ (real yield), depending on the bond type.
Part 8: [Convexity](../Problem%20Sets/PSET%20II%20Fixed%20Income%20Asset%20Pricing%201.md) of a Nominal Coupon Bond (Step by Step)
	1.	Action: Recall the nominal bond price:$$
P_{\text{nom}}(0) = \sum_{i=1}^{N} \Bigl(C_{\text{nom}}\,F\Bigr)\,e^{-r\,t_i} + F\,e^{-r\,t_N}.
$$
	2.	First derivative: As derived above,
￼
	3.	Second derivative: Now differentiate again w.r.t. ￼:
	•	For the coupon term ￼, we get:$$
\frac{d}{dr}\bigl[-t_i\,C_{\text{nom}}\,F\,e^{-r\,t_i}\bigr]
\;=\;
-\,t_i\,C_{\text{nom}}\,F\,\frac{d}{dr}\bigl(e^{-r\,t_i}\bigr)
\;=\;
-\,t_i\,C_{\text{nom}}\,F\,\bigl(-t_i\,e^{-r\,t_i}\bigr)
\;=\;
t_i^2 \, (C_{\text{nom}}\,F)\, e^{-\,r\,t_i}.
$$
	•	For the principal redemption term ￼, similarly:$$
\frac{d}{dr}\bigl[-\,t_N\,F\,e^{-r\,t_N}\bigr]
= t_N^2 \,F\,e^{-\,r\,t_N}.
$$
	•	Summing up:
￼
	4.	Plug into the [Convexity](../Problem%20Sets/PSET%20II%20Fixed%20Income%20Asset%20Pricing%201.md) Formula:
￼
Part 9: [Convexity](../Problem%20Sets/PSET%20II%20Fixed%20Income%20Asset%20Pricing%201.md) of a TIPS
By exactly the same procedure (but with ￼ in place of ￼, and scaled cash flows), for TIPS we get:$$
\frac{d^2 P_{\text{TIPS}}}{d r_{\text{real}}^{2}}
\sum_{i=1}^{N}
t_i^{2}\,\Bigl(C_{\text{TIPS}}\,F\,\tfrac{I(t_i)}{I(0)}\Bigr)\, e^{-\,r_{\text{real}}\,t_i}
\;+\;
t_N^{2}\,
\Bigl(F\,\tfrac{I(t_N)}{I(0)}\Bigr)\,e^{-\,r_{\text{real}}\,t_N}.
$$
Therefore, the TIPS [convexity](../Problem%20Sets/PSET%20II%20Fixed%20Income%20Asset%20Pricing%201.md) is:$$
\mathcal{C}_{\text{TIPS}}
\frac{1}{P_{\text{TIPS}}(0)}
\sum_{i=1}^{N}
t_i^{2}\,\Bigl(C_{\text{TIPS}}\,F\,\tfrac{I(t_i)}{I(0)}\Bigr)\, e^{-\,r_{\text{real}}\,t_i}
\;+\;
t_N^{2}\,
\Bigl(F\,\tfrac{I(t_N)}{I(0)}\Bigr)\,e^{-\,r_{\text{real}}\,t_N}.
$$
Part 10: [Hedging](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%205/Key%20Rates%20O1s%20Durations%20and%20Hedging.md) – [Duration and Convexity](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%208/An%20Analytical%20Decomposition%20of%20Forward%20Rates.md)
	1.	[Duration](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%205/Key%20Rates%20O1s%20Durations%20and%20Hedging.md) [Hedging](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%205/Key%20Rates%20O1s%20Durations%20and%20Hedging.md): If you hold a [portfolio](../../Advanced%20Investments/An%20Asset%20Allocation%20Primer.md) with net [duration](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%205/Key%20Rates%20O1s%20Durations%20and%20Hedging.md) zero (to nominal yields), the first-order exposure to yield changes is mitigated. For small parallel shifts ￼,
￼
If ￼ for the [portfolio](../../Advanced%20Investments/An%20Asset%20Allocation%20Primer.md), ￼ to first order.
	2.	[Convexity](../Problem%20Sets/PSET%20II%20Fixed%20Income%20Asset%20Pricing%201.md) [Hedging](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%205/Key%20Rates%20O1s%20Durations%20and%20Hedging.md): If yields move significantly (i.e., ￼ is not tiny), you must also hedge the second-order term:$$
\Delta P
\;\approx\;
-D \,P\,\Delta r
\;+\;
\tfrac{1}{2}\,\mathcal{C}\,P\,(\Delta r)^{2}.
$$
Setting up a hedge that neutralizes both ￼ and ￼ can require multiple instruments (e.g., a combination of short and long maturity bonds to solve the two-equation system).
	3.	TIPS vs. Nominal:
	•	TIPS are sensitive primarily to changes in real yields.
	•	Nominal Treasury bonds are sensitive primarily to changes in nominal yields.
	•	The difference between nominal and real yields is the breakeven [inflation](../../International%20Finance/Bridgewater/Principles%20For%20Navigating%20Big%20Debt%20Cycles/Part%20II%20Detailed%20Case%20Studies/German%20Debt%20Crisis%20andHyperinflation%20(1918–1924)/War%20Economies%20and%20Hyperinflation.md) ￼.
Thus, an investor might use nominal bonds to hedge the [duration](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%205/Key%20Rates%20O1s%20Durations%20and%20Hedging.md) of a TIPS position, understanding that perfect [hedging](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%205/Key%20Rates%20O1s%20Durations%20and%20Hedging.md) is complicated by the possibility that real yields and [inflation](../../International%20Finance/Bridgewater/Principles%20For%20Navigating%20Big%20Debt%20Cycles/Part%20II%20Detailed%20Case%20Studies/German%20Debt%20Crisis%20andHyperinflation%20(1918–1924)/War%20Economies%20and%20Hyperinflation.md) [expectations](../Fixed%20Income%20Lecture%20Notes/FORWARD%20RATES%20AND%20TERM%20STRUCTURE.md) move differently.
Summary of Formulas
	1.	Nominal Bond:$$
\boxed{
\begin{aligned}
P_{\text{nom}}(0)
&= \sum_{i=1}^{N} \bigl(C_{\text{nom}} F\bigr) e^{-r\,t_i} \;+\; F\,e^{-r\,t_N},\\
D_{\text{nom}}
&=
\frac
{\sum_{i=1}^{N} t_i\,(C_{\text{nom}} F)\, e^{-r\,t_i} + t_N\,F\,e^{-r\,t_N}}
{P_{\text{nom}}(0)},\\
\mathcal{C}{\text{nom}}
&=
\frac{1}{P{\text{nom}}(0)}
\left(
\sum_{i=1}^{N} t_i^2\,(C_{\text{nom}}\,F)\, e^{-r\,t_i}
	•	t_N^2\,F\, e^{-r\,t_N}
\right).
\end{aligned}
}
$$
	2.	TIPS:$$
\boxed{
\begin{aligned}
P_{\text{TIPS}}(0)
&= \sum_{i=1}^{N}
\bigl(C_{\text{TIPS}} F \frac{I(t_i)}{I(0)}\bigr)\, e^{-r_{\text{real}}\,t_i}
\;+\;
\bigl(F \frac{I(t_N)}{I(0)}\bigr)\, e^{-r_{\text{real}}\,t_N},\\
D_{\text{TIPS}}
&=
\frac
{\sum_{i=1}^{N}
t_i\,C_{\text{TIPS}}\,F\,\frac{I(t_i)}{I(0)}\, e^{-r_{\text{real}}\,t_i}
	•	t_N\,\Bigl(F\,\frac{I(t_N)}{I(0)}\Bigr)\,e^{-r_{\text{real}}\,t_N}}
{P_{\text{TIPS}}(0)},
\\
\mathcal{C}{\text{TIPS}}
&=
\frac{1}{P{\text{TIPS}}(0)}
\sum_{i=1}^{N}
t_i^{2}\,\bigl(C_{\text{TIPS}}\,F\,\tfrac{I(t_i)}{I(0)}\bigr)\, e^{-\,r_{\text{real}}\,t_i}
\;+\;
t_N^{2}\,
\bigl(F\,\tfrac{I(t_N)}{I(0)}\bigr)\, e^{-\,r_{\text{real}}\,t_N}.
\end{aligned}
}
$$
Key Takeaways
	1.	Same structural formulas for [duration and convexity](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%208/An%20Analytical%20Decomposition%20of%20Forward%20Rates.md) apply to both nominal and TIPS bonds, except that TIPS coupons and redemption amounts are multiplied by the [inflation](../../International%20Finance/Bridgewater/Principles%20For%20Navigating%20Big%20Debt%20Cycles/Part%20II%20Detailed%20Case%20Studies/German%20Debt%20Crisis%20andHyperinflation%20(1918–1924)/War%20Economies%20and%20Hyperinflation.md) index ratio $\tfrac{I(t_i)}{I(0)}$ and discounted at the real yield.
	2.	[Duration](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%205/Key%20Rates%20O1s%20Durations%20and%20Hedging.md) (Macaulay or continuous) is always the weighted average time to cash flows, with weights proportional to present values of those cash flows.
	3.	[Convexity](../Problem%20Sets/PSET%20II%20Fixed%20Income%20Asset%20Pricing%201.md) refines the approximation of the bond’s price response to interest-rate moves, accounting for the curvature (the second derivative).
	4.	[Hedging](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%205/Key%20Rates%20O1s%20Durations%20and%20Hedging.md) with [duration](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%205/Key%20Rates%20O1s%20Durations%20and%20Hedging.md) alone is a linear approximation; large rate moves require considering [convexity](../Problem%20Sets/PSET%20II%20Fixed%20Income%20Asset%20Pricing%201.md). TIPS [hedging](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%205/Key%20Rates%20O1s%20Durations%20and%20Hedging.md) also involves understanding how real yields differ from nominal yields (the breakeven [inflation](../../International%20Finance/Bridgewater/Principles%20For%20Navigating%20Big%20Debt%20Cycles/Part%20II%20Detailed%20Case%20Studies/German%20Debt%20Crisis%20andHyperinflation%20(1918–1924)/War%20Economies%20and%20Hyperinflation.md) concept).
This level of detail—deriving each step, explaining each derivative, and interpreting the final results—mirrors the style of your provided example.
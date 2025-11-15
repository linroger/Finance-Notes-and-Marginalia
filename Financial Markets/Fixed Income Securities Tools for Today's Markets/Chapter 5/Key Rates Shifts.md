---
aliases:
- HQM Curve
- JNJ Bonds
- Key Rate Shifts
- Futures and forwards contract mechanics
- Cash-and-carry arbitrage
- Basis trading and roll strategies
- Bond pricing and yield curves
- Duration and convexity hedging
- Credit spreads and bond valuation
- Option pricing theory and Black-Scholes model
- Options Greeks and risk management
- Call and put option strategies
- Fixed income securities and markets
- Bond valuation and yield calculation
- Credit analysis and spread decomposition
- Yield curve construction and modeling
- Forward rate calculations
- Spot and discount factors
- Key Rates Shifts and financial analysis
- Key Rates Shifts in modern finance
- Applications of Key Rates Shifts
- 'Case study: Key Rates Shifts'
last_enhanced: '2025-11-06 08:42:36'
- bond
- dv01
- put
- fixed-income
- hedging
- bonds
- options
- forward-rates
- portfolio
- basis
- forward
- term-structure
- futures
- duration
tags:
- arbitrage
- basis
- bid-ask
- bond
- case-study
- credit-curve
- crisis-analysis
- derivative-pricing
- derivatives
- duration
- empirical-analysis
- fixed-income
- graduate-level
- hedging
- institutional-quality
- learning-from-crisis
- mathematical-finance
- professional-standard
- provision
- quantitative-methods
- real-world-example
- sec-regulation
- securitization
- spread
- yield-curve

key_concepts:
- Banking and Financial Intermediation
- Case Study Methodology
- Crisis Case Study Design
- Empirical Analysis of Financial Events
- Empirical Finance Research
- Financial Crisis Case Studies
- Financial Markets and Banking
- Financial Markets and Institutions
- Historical Financial Analysis
- Institutional-Quality Financial Education
- Learning from Financial Crises
- Quantitative Methods in Finance
- Real-World Financial Examples
- Risk Management and Hedging Strategies
- Risk Management in Finance

enhanced: true
enhancement_date: 2025-11-06
enhancement_id: batch06-af

type: note
created: 2025-11-06
modified: 2025-11-06
status: active
academic_level: graduate
professional_application: industry-standard
---







# 5.3 KEY RATES: SHIFTS  

The next section applies key-rate metrics and hedging to the problem of the.   
pension fund introduced in Section 4.8. To keep the exposition simple, and to.   
dovetail with the pension fund's long-term liabilities and intention to invest in the Johnson $\&$ Johnson (JNJ) bonds listed in Table 4.6, the analysis here.   
is restricted to four key rates with terms of 10, 20, 30, and 40 years..  

The key-rate framework imposes no restrictions on how any key rate. changes relative to another. But in order to reprice any bond after any shift of key rates, the framework must specify how all par rates move, not just how key rates move. To that end, key-rate analysis makes the following assump-. tions: i) each key-rate shift leaves all other key rates unchanged; ii) each key-rate shift changes only those par rates that are between adjacent key rates; and ii) changes in par rates due to a key-rate shift decline linearly. from the change in that key rate to zero at adjacent key rates. The resulting. shifts, in the current example, are shown in Figure 5.2..  

The 20-year key-rate shift, depicted by the black, dashed line in the figure, equals one basis point at a term of 20 years. That shift has no effect on par rates with terms less than 10 years - the term of the previous key rate - or on par rates with terms greater than 30 years - the term of the next key rate. Between 10 and 30 years, however, the impact of the shift declines linearly from the 20-year term, which, since the adjacent key rates are both 10 years distant, means a decline of 0.1 basis points per year. For example, the shift increases the 19- and 21-year par rates by 0.9 basis points each; the 18- and 22-year rates by 0.8 basis points each; etc., the 11- and 29-year rates by 0.1 basis points each; and the 10- and 30-year par rates, which are the adjacent key rates, by 0.0 basis points each.  

![](e323b7819f8cc02a99bec1e6a6206385c80e5230bd279d728ee337aa827173a5.jpg)  
FIGURE 5.2  Key Rate Shifts with Four Key Rates at Terms of 10, 20, 30, and 40 Years.  

![](47046b21390abda98b945cc5d8b5b8e4635f8cd1194d8b91e82ec86b46bacba0.jpg)  
FIGURE 5.3 The HQM Par Rate Curve, as of May 2021, with and Without a 20- Year Key-Rate Shift.  

When computing the 20-year key-rate Dv01 or key-rate duration of. a bond or portfolio, all prices are recomputed after shifting the existing. par rate curve by the 20-year key-rate shift. Figure 5.3 shows the starting High-Quality Market-Weighted (HQM) corporate par-rate curve as the gray, dotted line, and the 20-year key-rate shift, just described, added to that par-rate curve. The shifted par-rate curve, therefore, is the dotted line out to 10 years, the black line from 10 to 30 years, and the dotted line again from 30 to 60 years. As an aside, while this shifted par-rate curve looks reasonable enough, spot and forward rates implied by this shifted curve may not look as natural or reasonable..  

The 30-year key-rate shift in Figure 5.2 is constructed like the 20-year. shift. The shift equals one basis point at 30 years and declines linearly on. both sides, at 0.1 basis points a year, because the adjacent key rates -- at 20 and 40 years - are each 10 years distant. The 10-year and 40-year shifts are constructed somewhat differently, because there is no key-rate at a term less than 10 years or greater than 40 years. The 10-year shift, therefore, equals. one basis point for all par rates with terms less than 10 years, and the 40-year shift equals one basis point for all par rates with terms greater than 40 years..  

Were all the shifts in Figure 5.2 to occur simultaneously, the result would be a parallel shift of one basis point. This is obvious for par rates of terms less than or equal to 10 years. For terms between 10 and 20 years, which are affected by the 10- and 20-year shifts, note the following. The 10-year shift, which starts at one basis point at 10 years, decreases by 0.1 basis points per year. At the same time, the 20-year shift, which starts at zero at 10 years, increases by 0.1 basis points per year. Hence, the decrease and increase cancel, leaving the shift at one basis point. With similar logic, it is easy to see that simultaneous shifts of all the key rates do result in a parallel shift. This observation explains the sense in which key-rate $^{\circ_{01s}}$ and key-rate durations decompose the Dv01 and duration of Chapter 4: each key-rate exposure is that part of the overall exposure arising from a change in that key rate, holding all other key rates constant.  

This section concludes by emphasizing that the assumptions invoked to compute the shifts of par rates between key rates are for convenience rather than to capture market or empirical realities. Most obviously, there is no reason to think that par rates respond linearly to changes in adjacent key rates. More subtly, the assumption that par rates are affected only by adjacent par rates is restrictive as well. If, for example, the 10-year rate falls, while the 20- and 30-year rates stay the same, the 25-year rate might very well change so that the overall shape of the term structure continues to be reasonable. In any case, despite these objections, the formulation of key-rate shifts described here has been widely accepted as a sensible trade-off between reality and tractability.

---
tags:
  - bond_convexity
  - bond_duration
  - interest_rate_risk
  - macaulay_duration
  - yield_to_maturity
aliases:
  - Bond Risk
  - Duration and Convexity
  - Interest Rate Risk
  - PVBP
key_concepts:
  - Bond cash flows
  - Bond price fluctuations
  - Coupon rate impact
  - Interest rate risk
  - Macaulay duration calculation
---

# 2.4 INTEREST RATE RISK: DURATION AND CONVEXITY  

There are two main risks of owning a bond. The first is the risk that the issuer may default on the bond and the promised cash flows are not paid. The second risk is that the price of the bond may go down when [interest rates](../../../Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%202/Interest%20Rate%20Quotations.md) go up. As [interest rates](../../../Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%202/Interest%20Rate%20Quotations.md) fluctuate over time, they affect the present value of the bond's cash flows through the discounting process. The [price volatility](../Chapter%206%20Options%20on%20Non-Price%20Variables/Black%20Models%20for%20Bond%20Price%20Options%20Capsfloors.md) of the bond as a result of interest rate fluctuations is referred to as the [interest rate risk](../../../../Fixed%20Income%20Asset%20Pricing/Analysis%20of%20Fixed%20Income%20Securities.md) of the bond. The two main measures of the [interest rate risk](../../../../Fixed%20Income%20Asset%20Pricing/Analysis%20of%20Fixed%20Income%20Securities.md) of the bond are the [duration](../../../Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%205/Key%20Rates%20O1s%20Durations%20and%20Hedging.md) of the bond and the price value of a basis point (PVBP). Both are local measures and work well for small changes in yields. For larger changes they are often corrected using the bond's [convexity](../../../../Fixed%20Income%20Asset%20Pricing/Problem%20Sets/PSET%20II%20Fixed%20Income%20Asset%20Pricing%201.md).  

The price of a bond fluctuates as [interest rates](../../../Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%202/Interest%20Rate%20Quotations.md) change. The coupon rate set at the time of. issue does not change, the cash flows it defines do not change, and nor do the dates of the cash flows. But as yields demanded by investors change, so do the discounted values of those cash flows. This phenomenon is normally portrayed as a downward-sloping concave relationship. between the bond's price its yield-to-maturity..  

Consider a 12-year $10\%$ semi-annual coupon bond currently yielding. $10\%$ semi-annually. The face value is $\$100$ . The bond pays $\$5$ every 6 months for the next 12 years and [returns](../../../Financial%20Asset%20Pricing%20Theory%20Overview/Chapter%203%20-%20%20Assets,%20Portfolios,%20and%20Arbitrage/Assets.md) the. principal of. $\$10012$ years from today. The price of the bond today, equal to the discounted value of its cash flows, is equal to:  
$$
P={\frac{5}{(1+0.05)}}+{\frac{5}{(1+0.05)^{2}}}+\cdot\cdot\cdot+{\frac{5}{(1+0.05)^{23}}}+{\frac{105}{(1+0.05)^{24}}}=100
$$  

The bond trades at par given that the yield-to-maturity is equal to the coupon rate.  

Now suppose that the market yield on the 12-year bond changes to $8\%$ semi-annually. The. new price of the $10\%$ coupon bond is:  
$$
P={\frac{5}{(1+0.04)}}+{\frac{5}{(1+0.04)^{2}}}+\cdot\cdot\cdot+{\frac{5}{(1+0.04)^{23}}}+{\frac{105}{(1+0.04)^{24}}}=115.25
$$  

A bond paying a $10\%$ coupon rate while investors demand $8\%$ trades at a premium over par. Conversely, if the market yield on a 12-year bond changes to $12\%$ semi-annually, the price will drop to:  
$$
P={\frac{5}{(1+0.06)}}+{\frac{5}{(1+0.06)^{2}}}+\cdot\cdot\cdot+{\frac{5}{(1+0.06)^{23}}}+{\frac{105}{(1+0.06)^{24}}}=87.45\cdot
$$  

A bond paying a $10\%$ coupon rate while investors demand $12\%$ trades at a discount.  

Plotting the relationship between the price of the bond and its yield, we get the graph shown in Figure 2.15.  

Note that the maximum price for the bond is 220. If the yield drops to zero, then the value of the bond will be equal to the sum of its cash flows, or.  
$$
P={\frac{5}{(1+0.0)}}+{\frac{5}{(1+0.0)^{2}}}+\cdots+{\frac{5}{(1+0.0)^{23}}}+{\frac{105}{(1+0.0)^{24}}}=220.00
$$  

The price for the bond asymptotically approaches zero as the yield goes to infinity. Most. of the time, we are in between. The graph is a convex curve (bowed to below) due to interest compounding. This [convexity](../../../../Fixed%20Income%20Asset%20Pricing/Problem%20Sets/PSET%20II%20Fixed%20Income%20Asset%20Pricing%201.md) implies that price responses are not symmetric. When the yield.  

![](c62058bbf9192530fa522313dfc0a25e2f257fa709a3de8b7985cd98358015d1.jpg)  
Figure 2.15 The Price-Yield Relationship of a 12-Year $10\%$ Coupon Bond  

goes down by $2\%$ , the price goes up by 15.25, but when the yield goes up by $2\%$ , the price goes down by 12.55. The magnitude of bond price responses to yield changes depends on three factors (in the order of importance):  

[Time to maturity](../../../../Financial%20Instruments/Lecture%20Notes-%20Financial%20Instruments/Teaching%20Note%201-%20Forward%20Rates%20Agreement/Hedging%20Strategies%20with%20Forwards.md) - Other thing being equal, the longer the maturity of the bond the larger are the price swings for the same change in [interest rates](../../../Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%202/Interest%20Rate%20Quotations.md). A 16-year. $10\%$ semi-annual coupon bond prices to par at a $10\%$ semi-annual yield, to 117.87 at. $8\%$ , and to 85.92 at $12\%$ . A longer bond's cash flows extend further into the future, making them more sensitive. to discounting. Coupon rate - Other thing being equal, the lower the coupon rate of the bond the larger. are the price swings for the same change in [interest rates](../../../Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%202/Interest%20Rate%20Quotations.md). Low coupon bonds derive more benefits from the principal than from coupon cash flows, and the impact of discounting is greater for later cash flows.. Coupon frequency - Other thing being equal, the more frequently the coupons on the bond are paid the smaller are the price swings for the same change in [interest rates](../../../Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%202/Interest%20Rate%20Quotations.md), as. more frequent coupons bring the cash flows closer to today, making them less sensitive to [discount rate](../../../../Advanced%20Financial%20Analysis%20and%20Valuation/Problem%20Sets/PSET%207-%20Kohler.md) changes.  

Zero-coupon bonds have the greatest [interest rate risk](../../../../Fixed%20Income%20Asset%20Pricing/Analysis%20of%20Fixed%20Income%20Securities.md) of all bonds with the same maturity,. as there is only one [cash flow](../Chapter%201%20-%20Purpose%20and%20Structure%20of%20Financial%20Markets/Preview%20of%20the%20Book.md) at maturity. Floating rate bonds have virtually no interest rate. sensitivity. Their prices return to par after [coupon payments](../../../Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%203/Realized%20Returns.md) and deviate from par on non-. coupon dates only to the extent that the first coupon rate that has already been set is different from the [discount rate](../../../../Advanced%20Financial%20Analysis%20and%20Valuation/Problem%20Sets/PSET%207-%20Kohler.md) for that first coupon..  

The most common interest rate metrics used to compare the [riskiness](../../../../Financial%20Instruments/Financial%20Derivatives%20and%20Quantitative%20Methods/Risk%20Preferences.md) of bonds are [duration](../../../Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%205/Key%20Rates%20O1s%20Durations%20and%20Hedging.md). and [convexity](../../../../Fixed%20Income%20Asset%20Pricing/Problem%20Sets/PSET%20II%20Fixed%20Income%20Asset%20Pricing%201.md). Both are "local' statistics describing the sensitivity of the bond's price to small changes in yields away from the current level. They do not work for large market moves: the [duration](../../../Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%205/Key%20Rates%20O1s%20Durations%20and%20Hedging.md) of the bond when yields are. $8\%$ cannot be extrapolated from the [duration](../../../Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%205/Key%20Rates%20O1s%20Durations%20and%20Hedging.md) of the same bond when yields are $5\%$  

# 2.4.1 Duration  

The universe of bonds, even for the same issuer, can be enormous. On any given day, Jack may be considering the following set of outstanding XYZ Corporation bonds:.  

a 5-year semi-annual $4\%$ coupon bond;   
a $7^{1}/4$ -year annual $3\%$ bond with next coupon due in 3 months;.   
a 6-year zero coupon; or   
a 4-year step-up bond whose coupon starts at $3.5\%$ but increases by $0.75\%$ each year.  

How does Jack choose which bond to invest in or which one to sell out of his [portfolio](../../../../Advanced%20Investments/An%20Asset%20Allocation%20Primer.md)?  

Jack can compare bonds with different characteristics with the help of the notion of [duration](../../../Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%205/Key%20Rates%20O1s%20Durations%20and%20Hedging.md). In its original form, as described by Frederick Macaulay (1938), [duration](../../../Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%205/Key%20Rates%20O1s%20Durations%20and%20Hedging.md) $(D)$ is defined as the present value-weighted average time to the bond's cash flows. [Macaulay duration](../../../../Fixed%20Income%20Asset%20Pricing/Fixed%20Income%20Lecture%20Notes/Teaching%20Note%202-%20Interest%20Rate%20Risk%20Management%20And%20Factors.md) is defined in years of time. A bond has, for example, a [duration](../../../Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%205/Key%20Rates%20O1s%20Durations%20and%20Hedging.md) of 3.45 years, another bond has a [duration](../../../Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%205/Key%20Rates%20O1s%20Durations%20and%20Hedging.md) of 7.29 years, and we can compare bonds based on that number.  

[Duration](../../../Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%205/Key%20Rates%20O1s%20Durations%20and%20Hedging.md) has yet another, most interesting, interpretation. [Modified duration](../../../../Financial%20Engineering/A%20Guide%20to%20Duration%20DV01%20and%20Yield%20Curve.md) is the relative sensitivity of the bond price to a unit yield change. That unit can be $1\%$ , but a preferred unit of yield change is a smaller 1 basis point (bp), or $0.01\%$ . If a bond has a [modified duration](../../../../Financial%20Engineering/A%20Guide%20to%20Duration%20DV01%20and%20Yield%20Curve.md) of 6.94 and the yield to maturity increases by 1 bp, then the price of the bond decreases by. 6.94 bp. [Modified duration](../../../../Financial%20Engineering/A%20Guide%20to%20Duration%20DV01%20and%20Yield%20Curve.md) is defined as the percentage change in price divided by the change in yield, or:  
$$
M o d D=-\frac{\Delta P/P}{\Delta y}
$$  

[Duration](../../../Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%205/Key%20Rates%20O1s%20Durations%20and%20Hedging.md) and [modified duration](../../../../Financial%20Engineering/A%20Guide%20to%20Duration%20DV01%20and%20Yield%20Curve.md) are closely related through the following formula:  
$$
M o d D={\frac{D}{1+{\frac{y}{n}}}}
$$  

where $n$ is the number of compounding periods per year for the yield $y$ . As the denominator is always close to 1, [duration](../../../Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%205/Key%20Rates%20O1s%20Durations%20and%20Hedging.md) and [modified duration](../../../../Financial%20Engineering/A%20Guide%20to%20Duration%20DV01%20and%20Yield%20Curve.md) are roughly the same. Often we speak only of one [duration](../../../Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%205/Key%20Rates%20O1s%20Durations%20and%20Hedging.md), quoting exclusively the [modified duration](../../../../Financial%20Engineering/A%20Guide%20to%20Duration%20DV01%20and%20Yield%20Curve.md) number as it reflects the local [riskiness](../../../../Financial%20Instruments/Financial%20Derivatives%20and%20Quantitative%20Methods/Risk%20Preferences.md) of bonds, but relying on the intuitive understanding of [Macaulay duration](../../../../Fixed%20Income%20Asset%20Pricing/Fixed%20Income%20Lecture%20Notes/Teaching%20Note%202-%20Interest%20Rate%20Risk%20Management%20And%20Factors.md).  

Consider a 6-year $\$100$ face value $7\%$ semi-annual coupon bond yielding $8\%$ . The bond. pays $\$3.50$ every 6 months and [returns](../../../Financial%20Asset%20Pricing%20Theory%20Overview/Chapter%203%20-%20%20Assets,%20Portfolios,%20and%20Arbitrage/Assets.md) the principal of $\$100$ in 6 years. Table 2.2 presents the logic of the Macaulay duration calculation. Columns 1 and 2 contain times and cash flows. Column 3 contains discount factors $\begin{array}{r}{d f=\frac{1}{(1+y_{n}/2)^{n}},n=1,\dots,12}\end{array}$ for each cash flow, based on the yield ofu. $8\%$ (semi). Column 4 has the present value of the cash flows ([cash flow](../Chapter%201%20-%20Purpose%20and%20Structure%20of%20Financial%20Markets/Preview%20of%20the%20Book.md) times the [discount factor](../../../Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%201/Discount%20Factors.md)), with the sum of the present values at the bottom. The main [duration](../../../Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%205/Key%20Rates%20O1s%20Durations%20and%20Hedging.md) computations are in columns 5 and 6. Column 5 has the percentage that the PV of each [cash flow](../Chapter%201%20-%20Purpose%20and%20Structure%20of%20Financial%20Markets/Preview%20of%20the%20Book.md) represents in the total value of the bond. Each percentage is construed as the weight of the [cash flow](../Chapter%201%20-%20Purpose%20and%20Structure%20of%20Financial%20Markets/Preview%20of%20the%20Book.md) in today's value of the bond. Column 6 multiplies those weights by the times of the cash flows to arrive at a weighted-average time to cash flows.  

Graphically, the [duration](../../../Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%205/Key%20Rates%20O1s%20Durations%20and%20Hedging.md) is presented as the center of mass (fulcrum) of a set of blocks in Figure 2.16, each block being the percentage of present value recovered through each cash. flow, the heights of the blocks taken from the rows of column 5 in Table 2.2.  

The weighted average time to the cash flows, using the block heights as the weights, is equal to 4.972. (Imagine a fulcrum placed at $2\times4.972=9.944$ on the horizontal axis in Figure 2.16..  

Table 2.2 [Macaulay duration calculation](.md)   


<html><body><table><tr><td colspan="6">Maturity in years: 6</td></tr><tr><td>Coupon:</td><td></td><td>7.00%</td><td>semi</td><td></td><td></td></tr><tr><td>Yield:</td><td></td><td>8.00%</td><td>semi</td><td></td><td></td></tr><tr><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td><td>6</td></tr><tr><td>t</td><td>CF</td><td>Df</td><td>PV</td><td>%PV</td><td>tx %PV</td></tr><tr><td>0.5</td><td>3.5</td><td>0.961538</td><td>3.365385</td><td>3.53%</td><td>0.0177</td></tr><tr><td>1</td><td>3.5</td><td>0.924556</td><td>3.235947</td><td>3.40%</td><td>0.0340</td></tr><tr><td>1.5</td><td>3.5</td><td>0.888996</td><td>3.111487</td><td>3.26%</td><td>0.0490</td></tr><tr><td>2</td><td>3.5</td><td>0.854804</td><td>2.991815</td><td>3.14%</td><td>0.0628</td></tr><tr><td>2.5</td><td>3.5</td><td>0.821927</td><td>2.876745</td><td>3.02%</td><td>0.0755</td></tr><tr><td>3</td><td>3.5</td><td>0.790315</td><td>2.766101</td><td>2.90%</td><td>0.0871</td></tr><tr><td>3.5</td><td>3.5</td><td>0.759918</td><td>2.659712</td><td>2.79%</td><td>0.0977</td></tr><tr><td>4</td><td>3.5</td><td>0.730690</td><td>2.557416</td><td>2.68%</td><td>0.1073</td></tr><tr><td>4.5</td><td>3.5</td><td>0.702587</td><td>2.459054</td><td>2.58%</td><td>0.1161</td></tr><tr><td>5</td><td>3.5</td><td>0.675564</td><td>2.364475</td><td>2.48%</td><td>0.1240</td></tr><tr><td>5.5</td><td>3.5</td><td>0.649581</td><td>2.273533</td><td>2.39%</td><td>0.1312</td></tr><tr><td>6</td><td>103.5</td><td>0.624597</td><td>64.64579</td><td>67.83%</td><td>4.0697</td></tr><tr><td>Total</td><td></td><td></td><td>95.30746</td><td>100.00%</td><td>4.9720</td></tr></table></body></html>  

![](8a3106518acf5ce41baa4c3850bfa3562d409b3de53c64adc46cd5ff34964919.jpg)  
Figure 2.16 Present values of the coupons as [duration calculation](../../../../Fixed%20Income%20Asset%20Pricing/Problem%20Sets/PSET%20II%20Fixed%20Income%20Asset%20Pricing%201.md) weights  

It would make all the blocks balance.) That number is the approximate percentage change of the price corresponding to a $1\%$ change in yield.  

The [Macaulay duration](../../../../Fixed%20Income%20Asset%20Pricing/Fixed%20Income%20Lecture%20Notes/Teaching%20Note%202-%20Interest%20Rate%20Risk%20Management%20And%20Factors.md) concept is extremely intuitive. With a little experience, one is able to guess bond durations fairly accurately. Here are some heuristics:.  

.The longer the maturity, the longer the [duration](../../../Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%205/Key%20Rates%20O1s%20Durations%20and%20Hedging.md), all other things being equal - the blocks in our graph extend further out and so the weighted time to the repayment is longer. The larger the coupon, the shorter the [duration](../../../Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%205/Key%20Rates%20O1s%20Durations%20and%20Hedging.md)  the higher the coupon blocks, the less weight is assigned to the principal repayment and the smaller the weighted average. The greater the frequency of the coupons, the shorter the [duration](../../../Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%205/Key%20Rates%20O1s%20Durations%20and%20Hedging.md) - as more blocks are closer to today.  

These correspond to the factors affecting the interest rate risks of bonds. Two more observations:  

The [duration](../../../Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%205/Key%20Rates%20O1s%20Durations%20and%20Hedging.md) of a zero-coupon bond is equal to its maturity..   
Floating rate bonds have short durations equal to the next coupon date.  

Let us now examine a more practical meaning of [duration](../../../Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%205/Key%20Rates%20O1s%20Durations%20and%20Hedging.md), that of the [interest rate sensitivity](../../../Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%2011/Forward%20Bond%20Yield.md), applied to our bond. The 6-year $7\%$ semi-annual coupon bond yielding $8\%$ is valued at 95.3075. We computed the [Macaulay duration](../../../../Fixed%20Income%20Asset%20Pricing/Fixed%20Income%20Lecture%20Notes/Teaching%20Note%202-%20Interest%20Rate%20Risk%20Management%20And%20Factors.md) to be 4.9720. The [modified duration](../../../../Financial%20Engineering/A%20Guide%20to%20Duration%20DV01%20and%20Yield%20Curve.md) is  
$$
M o d D=\frac{4.9720}{1+\frac{0.08}{2}}=4.7807
$$  

If the yield on the bond were to increase from $8.00\%$ to $8.15\%$ , that is by $0.15\%$ or $15\mathrm{~bp}$ then the price of the bond should decrease by $0.7171\%$ (4.7807 times 0.15). Based on the starting value of 95.3075, this translates into a change to 94.6240. Mathematically this can be expressed as:  
$$
\begin{array}{r l}&{P_{n e w}=P[1+(-M o d D)\Delta y]}\ &{\qquad=95.3075[1+(-4.7807)(0.15)]=94.6240}\end{array}
$$  

An exact calculation of the value of the bond, assuming an. $8.15\%$ yield, produces the. discounted value of the bond's cash flows equal to 94.6270. For a small change in the yield, [duration](../../../Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%205/Key%20Rates%20O1s%20Durations%20and%20Hedging.md) is a very good approximation to the exact value of the bond. This does not apply,. however, if the yield change is large. In the extreme case of the yield dropping to zero,. i.e. changing by minus. $8\%$ , multiplying 4.7807 by 8.00 produces the predicted change of. $38.2456\%$ of the current value, or. $\$36.4509$ . Duration thus predicts the bond price rise to $\$131.7584$ while the actual price with a zero [discount rate](../../../../Advanced%20Financial%20Analysis%20and%20Valuation/Problem%20Sets/PSET%207-%20Kohler.md) is. $\$142$ , the sum of the cash. flows.  

What can go wrong? As a local measure, [duration](../../../Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%205/Key%20Rates%20O1s%20Durations%20and%20Hedging.md) is the first derivative of the price with respect to the yield. Thus, it is a linear approximation based on a straight line tangent to a polynomial curve, the true price-yield relationship. This is represented in Figure 2.17.  

Later we show how the [duration](../../../Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%205/Key%20Rates%20O1s%20Durations%20and%20Hedging.md)-based linear approximation can be improved with the use of [convexity](../../../../Fixed%20Income%20Asset%20Pricing/Problem%20Sets/PSET%20II%20Fixed%20Income%20Asset%20Pricing%201.md).  

Most computer applications do not compute [duration](../../../Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%205/Key%20Rates%20O1s%20Durations%20and%20Hedging.md) the way we presented it in Table.   
2.2. Rather they revalue the bond using two yields, one set a small number of basis points.   
above and one set a small number of basis points below the current yield-to-maturity, and then.   
dividing the change in the bond's value by the combined size of the yield change "blip.' That.   
is, they compute the numerical sensitivity of price to yield. If we denote the value of the bond  

![](f7178273188402cbadbfa41c3a75de2743e59255969e0658c9e290d4a21db02b.jpg)  
Figure 2.17Bond price vs yield  

with a yield blipped up by $d y$ basis points as $P_{+d y}$ and the value of the bond with a yield blipped down by $d y$ basis points as $P_{-d y}$ , then [duration](../../../Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%205/Key%20Rates%20O1s%20Durations%20and%20Hedging.md) is computed numerically by dividing the percentage price change by the total change in yield:  
$$
M o d D=-\frac{(P_{+d y}-P_{-d y})/P}{2d y}
$$  

The two prices can be easily found by use of a financial calculator or a spreadsheet. Doing so, at the yield of 8.02 we get $P_{+2}=95.21639$ and at the yield of 7.98 we get $P_{-2}=95.39864$ The [duration](../../../Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%205/Key%20Rates%20O1s%20Durations%20and%20Hedging.md) is:  
$$
M o d D=-\frac{(95.21639-95.39864)/95.30746}{2\cdot0.0002}=4.7806
$$  

The estimate is off by 0.0001 due to the large blip of 2 bp. To improve the estimate we can use a smaller blip of 1 bp or $0.5\mathrm{bp}$ , or we can adjust the centering in the numerator..  

This numerical blipping procedure of computing [duration](../../../Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%205/Key%20Rates%20O1s%20Durations%20and%20Hedging.md) is very general and works even for the most complex bonds with embedded options, for which [expected cash flows](../../../../Advanced%20Financial%20Analysis%20and%20Valuation/Lecture%20Notes%20Advanced%20Financial%20Analysis%20and%20Valuation/Week%206/Week%206%20Assignment%20Review.md) change as yields vary.  

# 2.4.2 Portfolio Duration  

[Duration](../../../Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%205/Key%20Rates%20O1s%20Durations%20and%20Hedging.md) is very popular with managers of large bond portfolios. This is due to its one very attractive property: the [duration](../../../Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%205/Key%20Rates%20O1s%20Durations%20and%20Hedging.md) of a [portfolio](../../../../Advanced%20Investments/An%20Asset%20Allocation%20Primer.md) is equal to the weighted average of the durations of individual bonds. The weight for each bond is simply the proportion of the [portfolio](../../../../Advanced%20Investments/An%20Asset%20Allocation%20Primer.md) invested in that bond. This property is a direct result of the fact that durations are [first derivatives](../../../../Fixed%20Income%20Asset%20Pricing/Fixed%20Income%20Lecture%20Notes/Vasicek%20Short%20Rate%20Model.md) of the bond values with respect to yields and that [first derivatives](../../../../Fixed%20Income%20Asset%20Pricing/Fixed%20Income%20Lecture%20Notes/Vasicek%20Short%20Rate%20Model.md) are additive. Let us look at the example in Table 2.3.  

The interpretation of the [portfolio](../../../../Advanced%20Investments/An%20Asset%20Allocation%20Primer.md) [duration](../../../Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%205/Key%20Rates%20O1s%20Durations%20and%20Hedging.md) is the same as that for individual bonds with the qualification that the [duration](../../../Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%205/Key%20Rates%20O1s%20Durations%20and%20Hedging.md) of the [portfolio](../../../../Advanced%20Investments/An%20Asset%20Allocation%20Primer.md) is the sensitivity of the value of the [portfolio](../../../../Advanced%20Investments/An%20Asset%20Allocation%20Primer.md) with respect to a parallel shift in yields-to-maturity. For the [portfolio](../../../../Advanced%20Investments/An%20Asset%20Allocation%20Primer.md) in Table 2.3, this translates into the following statement: If the yield-to-maturity on each bond in the [portfolio](../../../../Advanced%20Investments/An%20Asset%20Allocation%20Primer.md) decreased by 7 basis points, then the value of the [portfolio](../../../../Advanced%20Investments/An%20Asset%20Allocation%20Primer.md) would increase by 6.859. times 7, or $48.013\$ basis points. In dollars, that is equal to an increase of 0.0048013 times. $\$2$ billion, or $\$9,402,600$ . Conveniently, by knowing one statistic about the [portfolio](../../../../Advanced%20Investments/An%20Asset%20Allocation%20Primer.md), its. [duration](../../../Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%205/Key%20Rates%20O1s%20Durations%20and%20Hedging.md), we can predict the value of the entire [portfolio](../../../../Advanced%20Investments/An%20Asset%20Allocation%20Primer.md) very accurately for small changes in yields.  

Table 2.3 The [duration](../../../Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%205/Key%20Rates%20O1s%20Durations%20and%20Hedging.md) of the [portfolio](../../../../Advanced%20Investments/An%20Asset%20Allocation%20Primer.md) of bonds   


<html><body><table><tr><td>Invested</td><td>%Invested</td><td>Coupon</td><td>Maturity</td><td>[Duration](../../../Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%205/Key%20Rates%20O1s%20Durations%20and%20Hedging.md)</td></tr><tr><td>400m</td><td>20</td><td>6.50</td><td>12</td><td>9.54</td></tr><tr><td>900m</td><td>45</td><td>5.75</td><td>10</td><td>7.23</td></tr><tr><td>700m</td><td>35</td><td>5.25</td><td>6</td><td>4.85</td></tr><tr><td>2,000m</td><td>100</td><td></td><td></td><td>6.86</td></tr></table></body></html>

Dur=0.209.54+0.45x7.23+0.354.85=6.859  

Often, bond managers engage in what is called [duration](../../../Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%205/Key%20Rates%20O1s%20Durations%20and%20Hedging.md) matching or [portfolio](../../../../Advanced%20Investments/An%20Asset%20Allocation%20Primer.md) immunization.. These terms refer to a conscious selection of bonds to be added to the [portfolio](../../../../Advanced%20Investments/An%20Asset%20Allocation%20Primer.md) in order to reduce the [duration](../../../Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%205/Key%20Rates%20O1s%20Durations%20and%20Hedging.md) of the [portfolio](../../../../Advanced%20Investments/An%20Asset%20Allocation%20Primer.md) to zero, i.e. to eliminate all [interest rate risk](../../../../Fixed%20Income%20Asset%20Pricing/Analysis%20of%20Fixed%20Income%20Securities.md). This can be done by selecting the right amount of bonds to be shorted or by buying bonds with negative [duration](../../../Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%205/Key%20Rates%20O1s%20Durations%20and%20Hedging.md). Alternatively, managers may attempt to shorten or lengthen the [duration](../../../Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%205/Key%20Rates%20O1s%20Durations%20and%20Hedging.md) of a [portfolio](../../../../Advanced%20Investments/An%20Asset%20Allocation%20Primer.md). by reshuffling the allocations to various bonds in order to decrease or increase the exposure to interest rate movements. Many managers of corporate bond portfolios short government bonds with the same [duration](../../../Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%205/Key%20Rates%20O1s%20Durations%20and%20Hedging.md) to eliminate exposure to [interest rates](../../../Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%202/Interest%20Rate%20Quotations.md), leaving themselves with pure [credit spread](../../../Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%2014/Cds-Equivalent%20Bond%20Spread.md) exposure.  

If, in Table 2.3, the yields-to-maturity do not change in parallel, e.g. some change by 8 bp. while others change by 6 bp, then the estimate based on [portfolio](../../../../Advanced%20Investments/An%20Asset%20Allocation%20Primer.md) [duration](../../../Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%205/Key%20Rates%20O1s%20Durations%20and%20Hedging.md) will be somewhat inaccurate, but an estimate obtained by summing the products of the changes in yields for all bond times their individual durations will be very accurate. This is still much easier than. revaluing all bonds.  

# 2.4.3Convexity  

[Convexity](../../../../Fixed%20Income%20Asset%20Pricing/Problem%20Sets/PSET%20II%20Fixed%20Income%20Asset%20Pricing%201.md) is used to improve the accuracy of the [duration](../../../Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%205/Key%20Rates%20O1s%20Durations%20and%20Hedging.md) approximation to the change in the value of the bond. It is important to include it in the approximation for  

large changes in yields-to-maturity, or.   
. bonds whose price-yield relationship is highly non-linear (bonds with embedded options, some [mortgage-backed securities](../../../../Financial%20Markets%20and%20Institutions/III.%20Liquidity%20of%20Assets/Class%207-%20CP,%20Repo,%20and%20the%20Crisis/Fremont%20Financial%20Corp.%20(b).md), etc.).  

[Convexity](../../../../Fixed%20Income%20Asset%20Pricing/Problem%20Sets/PSET%20II%20Fixed%20Income%20Asset%20Pricing%201.md) is equal to half the second derivative of bond price with respect to the yield and as such it measures the average rate of change in the slope of the tangent [duration](../../../Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%205/Key%20Rates%20O1s%20Durations%20and%20Hedging.md) line. Numerically it can be computed as the following difference formula:  
$$
C=\frac{1}{2}\cdot\frac{(P_{+d y}+P_{-d y}-2P)/P}{(d y)^{2}}
$$  

We already have all the ingredients to compute [convexity](../../../../Fixed%20Income%20Asset%20Pricing/Problem%20Sets/PSET%20II%20Fixed%20Income%20Asset%20Pricing%201.md) for our example bond. Let us plug the numbers into the formula to get:  
$$
C={\frac{1}{2}}\cdot{\frac{(95.21639+95.39864-2\cdot95.30746)/95.30746}{(0.0002)^{2}}}=14.4270
$$  

The [convexity](../../../../Fixed%20Income%20Asset%20Pricing/Problem%20Sets/PSET%20II%20Fixed%20Income%20Asset%20Pricing%201.md) number measures the average change in the [duration](../../../Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%205/Key%20Rates%20O1s%20Durations%20and%20Hedging.md) per. $d y$ basis points.' It tells us the extent to which the true price-yield curve deviates from the linear approximation. What we are mostly interested in is improving that approximation. In order to do that, we need to multiply the [convexity](../../../../Fixed%20Income%20Asset%20Pricing/Problem%20Sets/PSET%20II%20Fixed%20Income%20Asset%20Pricing%201.md) by the relevant yield change. $\Delta y$ to obtain the change in [duration](../../../Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%205/Key%20Rates%20O1s%20Durations%20and%20Hedging.md). over that entire yield change. This may explain the logic behind the following [duration](../../../Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%205/Key%20Rates%20O1s%20Durations%20and%20Hedging.md)-cumconvexity approximation formula for the bond price change:.  
$$
P_{n e w}=P[1+(-M o d D+C\cdot\Delta y)\Delta y]
$$  

The percentage price change in the bond value per unit of yield comes from two sources: the [duration](../../../Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%205/Key%20Rates%20O1s%20Durations%20and%20Hedging.md), which for most bonds will underestimate the magnitude of the change following. a straight line, and the [convexity](../../../../Fixed%20Income%20Asset%20Pricing/Problem%20Sets/PSET%20II%20Fixed%20Income%20Asset%20Pricing%201.md), which will correct for that underestimation by reducing the absolute value of the [duration](../../../Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%205/Key%20Rates%20O1s%20Durations%20and%20Hedging.md). Using the numbers for our example bond, we get:.  
$$
P_{n e w}=95.30746[1+(-4.7806+14.4270\cdot0.0015)\cdot0.0015]=95.6271
$$  

We have improved our estimate considerably and are almost spot on! Recall that the true value of the bond at a yield of $8.15\%$ was 95.6270.  

[Convexity](../../../../Fixed%20Income%20Asset%20Pricing/Problem%20Sets/PSET%20II%20Fixed%20Income%20Asset%20Pricing%201.md) is used as the second summary statistic to describe large bond portfolios. Typically, durations and convexities are computed for several possible yield increments relative to today's level, e.g. $-50$ bp, $-25$ bp, 0 bp, $+25$ bp, $+50$ bp. It is important to remember,. however, that convexities, unlike durations, are not additive and are computed by blipping entire portfolios and revaluing all the bonds in them. Just as with durations, managers engage in immunization strategies with respect to convexities by adding negatively convex bonds or reshuffling [portfolio](../../../../Advanced%20Investments/An%20Asset%20Allocation%20Primer.md) allocations to reduce or increase the [convexity](../../../../Fixed%20Income%20Asset%20Pricing/Problem%20Sets/PSET%20II%20Fixed%20Income%20Asset%20Pricing%201.md) of the overall [portfolio](../../../../Advanced%20Investments/An%20Asset%20Allocation%20Primer.md).  

# 2.4.4Other Risk Measures  

[Duration and convexity](../../../Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%208/An%20Analytical%20Decomposition%20of%20Forward%20Rates.md) calculations assume that the underlying cash flows of the bond do not change - only the yield-to-maturity. Yet the cash flows of bonds with embedded options often change as the yields change (e.g. a 'blip' in the yield on a callable bond may trigger a call provision). In those cases, one can compute alternative measures of effective [duration and convexity](../../../Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%208/An%20Analytical%20Decomposition%20of%20Forward%20Rates.md) where the changed cash flows are explicitly taken into account when computing. the blipped values $P_{+d y}$ and $P_{-d y}$ . One should, however, bear in mind, that those values are. not computed through simple discounting, but, rather, with a use of an option-[pricing](../../../Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%207/Arbitrage%20Pricing%20of%20Derivatives.md) model. As such they take into account other inputs, the most important of which is the volatility of the yield.  

The volatility of the yield also enters into the analysis in a different way. Imagine a [portfolio](../../../../Advanced%20Investments/An%20Asset%20Allocation%20Primer.md). of two corporate bonds both with the same maturity and both trading at par, but one of the bonds. has a much higher coupon reflecting a lower [credit quality](../../../../Financial%20Markets%20and%20Institutions/II.%20The%20Roles%20of%20Banks%20and%20Derivative%20Markets%20in%20Resolving%20Problems%20Inherent%20in%20Debt%20Contracts/Class%202-%20Debt%20Contracts%20due%20to%20Lack%20of%20Information/Wellman%20Inc%20the%20Importance%20of%20Loan%20Covenants.md) of its issuer. Is it realistic to assume that the yields on the bonds will move in parallel, or is it more realistic to assume that the riskier bond's yield will fluctuate proportionately more? The volatility of the yield refers precisely to that concept. Computing [portfolio](../../../../Advanced%20Investments/An%20Asset%20Allocation%20Primer.md) durations may be of little help in this case. Rather, one. may prefer to compute individual durations and scale the assumed yield movements by the respective yield volatilities to arrive at [portfolio](../../../../Advanced%20Investments/An%20Asset%20Allocation%20Primer.md) value change approximations for more realistic yield movements.  

Lastly, let us define the concept of the price value of a basis point which is closely related to the [duration](../../../Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%205/Key%20Rates%20O1s%20Durations%20and%20Hedging.md). Unlike [duration](../../../Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%205/Key%20Rates%20O1s%20Durations%20and%20Hedging.md), which is expressed in relative terms, the price value of a basis point, or PVBP, measures the absolute value of the change in price of a bond per unit of yield change, i.e. it is defined as:  
$$
P V B P=-{\frac{\Delta P}{\Delta y}}
$$  

and can be approximated by:  
$$
P V B P=-\frac{(P_{+d y}-P_{-d y})/10000}{2d y}
$$  

In our bond example, it could be computed as:  
$$
P V B P=-{\frac{(95.21639-95.39864)/10000}{2\cdot0.0002}}=0.0456
$$  

and is defined in dollars. The interpretation of PVBP is that [one basis point change](../../../Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%204/DV01.md) in the yield causes $\$0.0456$ change in the value of the bond with a face value of. $\$100$ . For par bonds, modified durations and PVBPs scaled by 1/100 are identical since percentage changes and absolute value changes are the same if. $P=100~\$ Modified durations or PVBPs can be used in. computing hedge ratios for basis trading or [portfolio](../../../../Advanced%20Investments/An%20Asset%20Allocation%20Primer.md) immunizations.  
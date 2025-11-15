---
linter-yaml-title-alias: FIXED INCOME ASSET PRICING BUS 35130 SPRING 2024 JOHN HEATON
title: PSET VI Fixed Income
tags:
- bdt_model
- bond-convexity
- bond-durability
- bond_pricing
- callable_bond
- convexity
- coupon-bonds
- fixed_income
- forward-contracts
- forward-rates
- ho-lee-model
- ho_lee_model
- interest-rates
- options
- options-greeks
- term-structure
- zero-coupon-bonds
aliases:
- Freddie Mac Bond
- HW6
- Homework 6
- PSET VI
key_concepts:
- Duration and interest rate risk measurement
- Convexity adjustments in fixed income
- Forward rate calculations and forward curve construction
- Term structure of interest rates and yield curves
- Financial valuation and pricing methodologies
- Fixed income securities and bond markets
last_enhanced: '2025-11-06 08:42:40'
---





# PSET VI Fixed Income

## HOMEWORK 6

Due at the beginning of Class 8
Note As with past homeworks there are "guides" for doing the homework in Excel,  Matlab and Python. In each code provides partial solutions to the questions. To make the code run you are required to complete some formulas or to produce some of the results yourself. You are not required to use any of the guides,  but use of one of them is recommended.

## PRICING THE FREDDIE MAC 6% CALLABLE BOND

Attached below you will find the prospectus of Freddie Mac 6%,  20-year callable bond,  issued on June 7,  2007. Your task in this homework is to obtain its fair valuation,  using both the Ho-Lee model and the Simple BDT model. Proceed as follows:

[^1]: (CP) Use the data in *"HW6 Data Bonds.xls"* and extract the discount curve $Z(0,          T)$ from the Treasuries using Nelson-Siegel model.

- Here are the discount curves and forward rates and 6 month Treasury yields plotted against time to maturity.
- !500
- !500
[^1]: (CP) Build the Ho-Lee tree,  given by
$$r_{i+1,         j}=r_{i,         j}+\theta(i)\times\Delta+\sigma\times\sqrt{\Delta}\times\epsilon_{i+1}$$

where $σ$ is the volatility of interest rates,  $θ(i)$ are chosen to fit the term structure of interest rates exactly,  and
$$\epsilon(i)=\left\{\begin{array}{l l}{{+1}}&{{\mathrm{with~probability}}}\\ {{-1}}&{{\mathrm{with~probability}}}\end{array}\right.\;\;1/2$$

Let $r_0$ match the first zero-coupon bond $Z_0(0.5)$ from Nelson Siegel model. The methodology to fit the model to the term structure of interest rates is explained in TN4. Both the matlab file and the guide spreadsheet that are available contain the routine to build it. You need a value of σ. Use the data on six-months rates available in the dataset (HW6 FRB H15*.csv*) to estimate σ (this can be done by taking the standard deviation of first differences in interest rates,  over six-month periods,  which is one time step). Remember to *annualize* the volatility estimates,  as $σ$ in Ho-Lee and BDT are annualized.

- The volatility of interest rates in the Ho-Lee model is given by $$\sigma^{HL}_{r_{t}}=st.dev(r_{t+1}-r_{{t}})$$

	This gives the monthly volatility of interest rates under the Ho-Lee model.

	- To annualize this volatility,  we multiply by $\sqrt{12}$,  such that annual volatility under the Ho-Lee model is $\sigma^{HL}_{r_{t}}\sqrt{12}$ =
	- The volatility of interest rates in the Simple Black Derman Toy model is given by $\sigma^{BDT}_{z_{t}}=st.dev(\ln(r_{{t+1}}-\ln(r_{t})))$
	- To find the annualized rate,  we multiply by $\sigma^{BDT}_{z_{t}} \times \sqrt{ 12 }$ =
[^1]: (CP) After fitting the tree to the data,  please plot the zero-coupon bond yields from the tree and from the original zero-coupon bonds Z(T) obtained from Nelson and Siegel (and used as inputs for the tree). Are they the same? Show also the first 10 time-steps of the interest rate tree (table 10 x 10)
[^1]: The zero coupon bond yields derived from the Ho-Lee tree largely match those produced by the Nelson Siegel interpolation.
[^1]: !500
[^1]: (CP) Use the tree tree
ˆ Obtain the price of the non-callable bond
!500
ˆ Obtain the price of
!500
ˆ Obtain the price of the callable bond as the difference.
!500
## PLEASE,  MAKE SURE TO INCORPORATE THE FACT THAT THE CALLABLE BOND BECOMES CALLABLE ONLY AFTER THE FIRST-CALL-DATE

(Matlab users: please see below for a generic algorithm to compute prices through backward calculation)

[^1]: (CP) Show the first 10 nodes of the non-callable bond,  the option to call,  and the callable security.
[^1]: (CP) Plot the price of the non-callable and of the callable security against interest rates at call time,  as well as 1,  2,  3 semesters before. How does the callable and non-callable bonds compare? Comment and discuss.

!500

!500

!500

!500

[^1]: (CP) Compute the duration and convexity of callable and non-callable bond at time 0. Comment on the difference between the two securities.
[^1]: (CP) **Ho Lee versus Simple BDT.** Redo all of the points above for the Simple BDT model (note: in both the matlab file and the spreadsheet,  this amounts to change BDT Flag from 0 to 1 and re-run the routine to build the tree. Everything else should be automatic,  except for the estimate of σ which now should use log differences in rates). Comment on the difference in price,  if any,  from the two methodologies.
- THe prices derived from the Ho-Lee model and the Black Derman Toy model should be the same,  because both models use the same zero discount curve as the input,  though the BDT model has a larger volatility.
!500!500!500!500!500!500!500!500!500

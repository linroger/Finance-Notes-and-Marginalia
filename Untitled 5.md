

---
title: CFA Level 1 Formula Sheet 2025
key_concepts:
- Quantitative methods formulas
- Financial calculator operations
- Time value of money
- Portfolio mathematics
- Corporate finance formulas
- Equity valuation models
- Fixed income valuation
- Derivatives pricing
- Risk management metrics
tags:
- cfa-level-1
- quantitative-methods
- financial-formulas
- portfolio-theory
- corporate-finance
- equity-valuation
- fixed-income
- derivatives
- risk-management
aliases:
- CFA Formulas 2025
- CFA Level 1 Quant Formulas
cssclasses: academia
---

# CFA Level 1 – Formula Sheet (2025)

# Setting Up the Texas BA II Plus Financial Calculator

Video: https://youtu.be/0MS8d8QQFmc

# Using Texas BA II Plus Financial Calculator

Video: https://youtu.be/LWmTTiZz8BU

Video (Requires Login to Facebook): https://fb.watch/nci5V7Dwtj/

# VOLUME 1: QUANTITATIVE METHODS

Learning Module 1: Rates and Returns

# Determinants of Interest Rates

Interest rate,  $r =$  Real risk-free rate + Inflation premium + Default risk premium

$
+ \text{Liquidity premium} + \text{Maturity premium}
$

(1 + Nominal risk-free rate) = (1 + Real risk-free rate) × (1 + Inflation premium)

Nominal risk-free rate $=$ Real risk-free rate + Inflation premium

Maturity premium = Interest rate on longer-maturity, liquid Treasury debt

- Interest rate on short-term Treasury debt

# Holding Period Return

$$
R = \frac {P _ {1} - P _ {0} + I _ {1}}{P _ {0}}
$$

where:

$P_{0} =$ Price at the beginning of the period

$P_{1} =$ Price at the end of the period

$I_{1} = \text{Income}$

If given holding period returns $R_{1}, R_{2}, \ldots, R_{T}$ over the holding period:

$$
R = (1 + R _ {1}) \times (1 + R _ {2}) \times \ldots \times (1 + R _ {T}) - 1
$$

# Arithmetic Return

$
\bar{R}_{i} = \frac{1}{T} \sum_{t=1}^{T} R_{it} = \frac{1}{T} (R_{i1} + R_{i2} + \dots + R_{iT})
$

# Geometric Mean Return

$
\bar{R}_{Gi} = \sqrt[T]{\prod_{t=1}^{T} (1 + R_{t}) - 1} = \sqrt[T]{(1 + R_{i1}) \times (1 + R_{i2}) \times \ldots \times (1 + R_{iT})} - 1
$

# Harmonic Mean

$
\bar{X}_{Hi} = \frac{n}{\sum_{i=1}^{n} (1 / X_{i})} \qquad \text{for } X_{i} > 0
$

# Relationship between Arithmetic Mean, Geometric Mean, and Harmonic Mean

(Geometric mean)² = Arithmetic mean × Harmonic mean

# Money-Weighted Return (MWR)

$
\sum_{t=0}^{T} \frac{CF_{t}}{(1 + MWR)^{t}} = 0
$

# Time-Weighted Return (TWR)

Given the holding period returns for each sub-period, $R_{1}, R_{2}, \ldots, R_{T}$

If $T > 1$ year, then

$
\text{Annualized TWR} = [ (1 + R_{1}) \times (1 + R_{2}) \times \ldots \times (1 + R_{T}) ]^{1 / T} - 1
$

If $T = 1$ year, then

$
\text{Annualized TWR} = (1 + R_{1}) \times (1 + R_{2}) \times \ldots \times (1 + R_{T}) - 1
$

If $T < 1$ year, then

$
\text{TWR for holding period} = (1 + R_{1}) \times (1 + R_{2}) \times \ldots \times (1 + R_{T}) - 1
$

# Non-Annual Compounding

$
PV = FV_{N} \left(1 + \frac{R_{S}}{m}\right)^{-mN}
$

where:

$m =$ Number of compounding periods per year

$R_{s} =$ Quoted annual interest rate

$N =$ Number of years

# Annualizing Returns

$
\begin{array}{l} 
R_{annual} = \left(1 + R_{weekly}\right)^{52} - 1 \\ 
R_{annual} = \left(1 + R_{monthly}\right)^{12} - 1 \\ 
R_{annual} = \left(1 + R_{daily}\right)^{252} - 1 \quad \text{assuming } 252 \text{ trading days per year} \\ 
R_{weekly} = \left(1 + R_{daily}\right)^{5} - 1 \quad \text{assuming } 5 \text{ trading days per week} \\ 
\end{array}
$

# Continuously Compounded Returns

$
P_{t} = P_{0} e^{r_{0, T}}
$

$
r_{0, T} = \ln \left(\frac{P_{t}}{P_{0}}\right)
$

$
r_{0, T} = r_{0, 1} + r_{1, 2} + \dots + r_{T-2, T-1} + r_{T-1, T}
$

# Real Returns

$(1 + \text{real return}) = (1 + \text{real risk-free rate}) \times (1 + \text{risk premium})$

# Pre-Tax and After-Tax Nominal Return

After-tax nominal return = Pre-tax nominal return $\times$ (1 - Tax rate)

$
\text{After-tax real return} = \frac{[ 1 + \text{Pre-Tax nominal return} \times (1 - \text{Tax rate}) ]}{1 + \text{Inflation premium}} - 1
$

# Leveraged Return

Return on a leveraged portfolio

$
R_{L} = R_{P} + \frac{V_{B}}{V_{E}} (R_{P} - r_{D})
$

where:

$
R_{P} = \text{Return on the investment portfolio (unleveraged)}
$

$
r_{D} = \text{Cost of debt}
$

$
V_{B} = \text{Debt} / \text{borrowed funds}
$

$
V_{E} = \text{Equity of the portfolio}
$

Learning Module 2: Time Value of Money in Finance

$
FV_{t} = PV (1 + r)^{t} \qquad \qquad PV = \frac{FV_{t}}{(1 + r)^{t}}
$

where:

$FV_{t} =$ Future value at time $t$

$PV =$ Present value

$r =$ Discount rate per period

$t =$ Number of compounding periods

As compounding frequency becomes very large (i.e., continuous compounding)

$
FV_{t} = PV e^{rt} \qquad \qquad PV = FV_{t} e^{-rt}
$

# Present Value of Zero-Coupon Bond

$
PV(\text{Discount Bond}) = \frac{FV}{(1 + r)^{t}}
$

where:

$
FV = \text{Principal} (\text{or Face Value})
$

$
r = \text{Market}
$

$
t = \text{Maturity}
$

$
r = \left(\frac{FV_{t}}{PV}\right)^{1/T} - 1
$

# Present Value of Coupon Bond

$
PV(\text{Coupon Bond}) = \frac{PMT}{(1 + r)^{1}} + \frac{PMT}{(1 + r)^{2}} + \dots + \frac{PMT + FV}{(1 + r)^{N}}
$

where:

$
PV = \text{Bond's price}
$

$
PMT = \text{Periodic}
$

$
FV = \text{Face value}
$

$
N = \text{Number of periods}
$

$
r = \text{Market}
$

# Present Value of a Perpetual Bond (Perpetuity)

$
PV(\text{Perpetual Bond}) = \frac{PMT}{r}
$

Annuity Instruments (e.g., Mortgage)

$
A = \frac{rPV}{1 - (1 + r)^{-t}}
$

where:

$A =$ Periodic cash flow

$r =$ Market interest rate per period

$PV =$ Present value or principal amount of loan/bond

$t =$ Number of payment periods

# Price of a Preferred Share

$
PV_{t} = \frac{D_{t}}{r}
$

where:

$D_{t} =$ Fixed periodic dividend

$r =$ Expected rate of return

# Price of a Common Share

# Constant Dividend Growth Rate into Perpetuity

$
PV_{t} = \frac{D_{t} (1 + g)}{r - g} = \frac{D_{t+1}}{r - g} \qquad r > g
$

where:

$D_{t} =$ Common dividend at time $t$

$g =$ Constant growth rate

$r =$ Expected rate of return

$
r = \frac{D_{t+1}}{PV_{t}} + g
$

$
\frac{PV_{t}}{E_{t}} = \frac{\frac{D_{t}}{E_{t}} \times (1 + g)}{r - g}
$

$
\frac{PV_{t}}{E_{t+1}} = \frac{\frac{D_{t+1}}{E_{t+1}}}{r - g}
$

where:

$E_{t} =$ Earnings per share for period $t$

$\frac{PV_t}{E_t} =$ Trailing price-to-earnings ratio

$\frac{PV_{t}}{E_{t + 1}} =$ Forward price-to-earnings ratio

# Two-stage Dividend Discount Model

$
PV_{t} = \sum_{i=1}^{n} \frac{D_{t} (1 + g_{s})^{i}}{(1 + r)^{i}} + \frac{E(S_{t + n})}{(1 + r)^{n}}
$

where:

$g_{s} =$ Higher short-term dividend growth rate

$g_{L} =$ Lower long-term dividend growth rate

$n =$ Initial growth phase

$E(S_{t + n}) =$ Stock value in $n$ periods (Terminal value)

$
= \frac{D_{t + n + 1}}{r - g_{L}}
$

# Forward Rate

$
F_{1,1} = \frac{(1 + r_{2})^{2}}{(1 + r_{1})} - 1
$

where:

$F_{1,1} =$ One-year forward rate one year from now

$r_1 =$ Discount rate on one-year risk-free discount bond

$r_2 =$ Discount rate on two-year risk-free discount bond

Learning Module 3: Statistical Measures of Asset Returns

# Measures of Central Tendency

$
\text{Sample Mean,} \qquad \bar{X} = \frac{1}{n} \sum_{i=1}^{n} X_{i}
$

where:

$
X_{i} = \text{Observation } i (i = 1, 2, 3, \dots , n)
$

# Median

$
\text{Position of median} = \frac{\text{Number of observations} + 1}{2}
$

# Quantiles

$
\text{Interquartile} = Q_{3} - Q_{1}
$

where: $Q_{1} =$ First quartile

$
Q_{3} = \text{Third quartile}
$

Box and Whisker Plot

$
\text{Upper fence} = Q_{3} + 1.5 \times IQR
$

$
\text{Lower fence} = Q_{1} - 1.5 \times IQR
$

# Measures of Dispersion

Range = Maximum value - Minimum value

Mean Absolute Deviation (MAD)

$
MAD = \frac{\sum_{i=1}^{n} |X_{i} - \bar{X}|}{n}
$

Sample Variance

$
s^{2} = \frac{\sum_{i=1}^{n} (X_{i} - \bar{X})^{2}}{n - 1}
$

Sample Standard Deviation

$
s = \sqrt{\frac{\sum_{i=1}^{n} (X_{i} - \bar{X})^{2}}{n - 1}}
$

Sample Target Semideviation

$
s_{Target} = \sqrt{\frac{\sum_{X_{i} \leq B}^{n} (X_{i} - B)^{2}}{n - 1}}
$

where:

$
B = \text{target}
$

$n =$ total number of sample observations

Coefficient of Variation

$
CV = \frac{S}{\bar{X}}
$

Sample Skewness

$
\text{Skewness} \approx \left(\frac{1}{n}\right) \frac{\sum_{i=1}^{n} (X_{i} - \bar{X})^{3}}{s^{3}}
$

Sample Excess Kurtosis

$
K_{E} \approx \left(\frac{1}{n}\right) \frac{\sum_{i=1}^{n} (X_{i} - \bar{X})^{4}}{s^{4}} - 3
$

Sample Covariance

$
s_{XY} = \frac{1}{n - 1} \sum_{i=1}^{n} (X_{i} - \bar{X}) (Y_{i} - \bar{Y})
$

Sample Correlation Coefficient

$
r_{XY} = \frac{s_{XY}}{s_{X} s_{Y}}
$

Learning Module 4: Probability Trees and Conditional Expectations

Expected Value of a Discrete Random Variable

$
E(X) = \sum_{i=1}^{n} P(X_{i}) X_{i}
$

Variance of a Random Variable

$
\begin{array}{l} 
\sigma^{2}(X) = E[X - E(X)]^{2} \\ 
= \sum_{i=1}^{n} P(X_{i})[X - E(X)]^{2} \\ 
\end{array}
$

Conditional Expected Value of a Random Variable

$
E(X | S) = P(X_{1} | S) X_{1} + P(X_{2} | S) X_{2} + \dots + P(X_{n} | S) X_{n}
$

Conditional Variance of a Random Variable

$
\begin{array}{l} 
\sigma^{2}(X | S) = P(X_{1} | S)[X_{1} - E(X_{1} | S)]^{2} + P(X_{2} | S)[X_{2} - E(X_{2} | S)]^{2} + \dots \\ 
+ P(X_{n} | S)[X_{n} - E(X_{n} | S)]^{2} \\ 
\end{array}
$

Total Probability Rule for Expected Value

$
E(X) = E(X | S_{1}) P(S_{1}) + E(X | S_{2}) P(S_{2}) + \dots + E(X | S_{n}) P(S_{n})
$

where: $S_{1}, S_{2}, \ldots, S_{n}$ are mutually exclusive and exhaustive events.

Bayes' Formula

$
P(A | B) = \frac{P(B | A)}{P(B)} \times P(A)
$

$
P(\text{Event} | \text{Information}) = \frac{P(\text{Information} | \text{Event})}{P(\text{Information})} \times P(\text{Event})
$

Video (Bayes' Formula and Total Probability Rule): https://youtu.be/9 h0EzssPZ4

For $n$ assets in a portfolio

Expected return on portfolio

$
E(R_{P}) = w_{1} E(R_{1}) + w_{2} E(R_{2}) + \dots + w_{n} E(R_{n})
$

Variance on portfolio

$
\sigma^{2}(R_{P}) = \sum_{i=1}^{n} \sum_{j=1}^{n} w_{i} w_{j} Cov(R_{i}, R_{j})
$

Requires $n$ variances and $\frac{n(n - 1)}{2}$ distinct covariances to estimate portfolio variance.

# Covariance

$
\begin{array}{l} 
Cov(R_{i}, R_{j}) = E\left[(R_{i} - E(R_{i}))(R_{j} - E(R_{j}))\right] \\ 
= \frac{1}{n - 1} \sum_{t=1}^{n} (R_{i,t} - \bar{R}_{i})(R_{j,t} - \bar{R}_{j}) \\ 
\end{array}
$

For a two-asset $(n = 2)$ portfolio:

$
\sigma^{2}(R_{P}) = w_{1}^{2} \sigma_{1}^{2} + w_{2}^{2} \sigma_{2}^{2} + 2 w_{1} w_{2} Cov(R_{1}, R_{2})
$

where: $Cov(R_1, R_2) = \rho(R_1, R_2) \times \sigma(R_1) \times \sigma(R_2)$

Video: https://youtu.be/luwulZ9ONC0

For a three-asset $(n = 3)$ portfolio:

$
\begin{array}{l} 
\sigma^{2}(R_{P}) = w_{1}^{2} \sigma_{1}^{2} + w_{2}^{2} \sigma_{2}^{2} + w_{3}^{2} \sigma_{3}^{2} + 2 w_{1} w_{2} Cov(R_{1}, R_{2}) \\ 
+ 2 w_{1} w_{3} Cov(R_{1}, R_{3}) + 2 w_{2} w_{3} Cov(R_{2}, R_{3}) \\ 
\end{array}
$

# Covariance Given a Joint Probability Function

$
Cov(R_{A}, R_{B}) = \sum_{i=1} \sum_{j=1} P(R_{A,i}, R_{B,j}) \times [R_{A,i} - E(R_{A})] \times [R_{B,j} - E(R_{B})]
$

If  $X$  and  $Y$  are uncorrelated, then  $E(XY) = E(X)E(Y)$ .

If  $X$  and  $Y$  are independent, then  $P(X,Y) = P(X)P(Y)$ .

# Safety-First Optimal Portfolio

# Safety-First Ratio

$
\text{SFRatio} = \frac{E(R_{P}) - R_{L}}{\sigma_{P}}
$

$
\text{Shortfall} = \Pr[E(R_{P}) < R_{L}] = \text{Normal}(-\text{SFRatio})
$

where:

$
R_{L} = \text{Investor's threshold level}
$

$
E(R_{P}) = \text{Expected}
$

$
\sigma_{P} = \text{Portfolio standard deviation}
$

Video: https://youtu.be/S3x5JrGIOUA

Learning Module 6: Simulation Methods

# Lognormal Distribution

Mean of a lognormal random variable

$
\mu_{L} = \exp(\mu + 0.50 \sigma^{2})
$

Variance of a lognormal random variable

$
\sigma_{L}^{2} = \exp(2\mu + \sigma^{2}) \times [\exp(\sigma^{2}) - 1]
$

where:

$
\mu = \text{Mean of the normal random variable}
$

$
\sigma^{2} = \text{Variance}
$

# Continuously Compounded Rates of Return

$
P_{T} = P_{0} \exp(r_{0, T})
$

where:

$
P_{0} = \text{Current asset price}
$

$
P_{T} = \text{Asset price at time } T
$

$
r_{0, T} = \text{Continuously compounded return from 0 to T}
$

If returns are independently and identically distributed (i.i.d.), then

$
r_{0, T} = r_{0, 1} + r_{1, 2} + \dots + r_{T-2, T-1} + r_{T-1, T}
$

If the one-period continuously compounded returns are i.i.d. random variables with mean $\mu$ and $\sigma^2$, then

$
E(r_{0, T}) = \mu T
$

$
\sigma^{2}(r_{0, T}) = \sigma^{2} T
$

$
\sigma(r_{0, T}) = \sigma \sqrt{T}
$

Learning Module 7: Estimation and Inference

$
\text{Sharpe ratio} = \frac{R_{P} - R_{F}}{\sigma_{P}}
$

where:

$
R_{P} = \text{Portfolio return}
$

$
R_{F} = \text{Risk-free rate}
$

$
\sigma_{P} = \text{Portfolio standard deviation of return}
$

$
\text{Variance of the sampling distribution of the sample means} = \frac{\sigma^{2}}{n}
$

$
\text{Standard error of the sample mean} = \frac{\sigma}{\sqrt{n}}
$

where:

$
\sigma = \text{Population}
$

$
n = \text{Sample size}
$

Note: If  $\sigma$  is not known, use  $s$ , the sample standard deviation.

# Bootstrap Resampling

$
s_{\bar{X}} = \sqrt{\frac{1}{B - 1} \sum_{b=1}^{B} (\hat{\theta}_{b} - \bar{\theta})^{2}}
$

where:

$
s_{\bar{X}} = \text{Estimate}
$

$
B = \text{Number of resamples drawn from the original sample}
$

$
\hat{\theta}_{b} = \text{Mean of a resample}
$

$
\bar{\theta} = \text{Mean across all the resample means}
$

Learning Module 8: Hypothesis Testing

$
\text{Confidence level} = 1 - \alpha
$

$
\text{Power of the test} = 1 - \beta
$

where:

$
\alpha = \text{Significance level} (\text{Probability of Type I error})
$

$
\beta = \text{Probability}
$

# Test of a Single Mean

Test statistic

$
t = \frac{\bar{X} - \mu_{0}}{s / \sqrt{n}}
$

Degrees of freedom $= n - 1$

$
(1 - \alpha)\% \text{ Confidence Interval} = \bar{X} + \text{Critical value} \times \left(\frac{s}{\sqrt{n}}\right)
$

# Test of the Difference in Means

Test statistic

$
t = \frac{(\bar{X}_{d1} - \bar{X}_{d2}) - (\mu_{d1} - \mu_{d2})}{\sqrt{\frac{s_{p}^{2}}{n_{d1}} + \frac{s_{p}^{2}}{n_{d2}}}}
$

Degrees of freedom $= n_{d1} + n_{d2} - 2$

$
s_{p}^{2} = \frac{(n_{d1} - 1) s_{d1}^{2} + (n_{d2} - 1) s_{d2}^{2}}{n_{d1} + n_{d2} - 2}
$

# Test of the Mean of Differences

Test statistic

$
t = \frac{\bar{d} - \mu_{d0}}{s_{\bar{d}}}
$

Degrees of freedom $= n - 1$

# Test of a Single Variance

Test statistic

$
\chi^{2} = \frac{(n - 1) s^{2}}{\sigma_{0}^{2}}
$

Degrees of freedom $= n - 1$

# Test of the Difference in Variances

Test statistic

$
F = \frac{S_{Before}^{2}}{S_{After}^{2}}
$

Degrees of freedom $= n_{1} - 1$, $n_{2} - 1$

# Test of a Correlation

Test statistic

$
t = \frac{r \sqrt{n - 2}}{\sqrt{1 - r^{2}}}
$

Degrees of freedom $= n - 2$

# Test of Independence (Categorical Data)

Test statistic

$
\chi^{2} = \sum_{i=1}^{m} \frac{(O_{ij} - E_{ij})^{2}}{E_{ij}}
$

Degrees of freedom $= (r - 1)(c - 1)$

where:

$
m = \text{Number of cells in the table}
$

$
O_{ij} = \text{Number of observations in each cell of row } i \text{ and column } j
$

$
E_{ij} = \text{Expected number of observations in each cell of row } i \text{ and column } j
$

Learning Module 9: Parametric and Non-Parametric Tests of Independence

# Test of a Correlation

Test statistic

$
t = \frac{r \sqrt{n - 2}}{\sqrt{1 - r^{2}}}
$

Degrees of freedom $= n - 2$

Pearson Correlation (or Bivariate Correlation)

$
r_{XY} = \frac{s_{XY}}{s_{X} s_{Y}}
$

Spearman Rank Correlation Coefficient

$
r_{S} = 1 - \frac{6 \sum_{i=1}^{n} d_{i}^{2}}{n (n^{2} - 1)}
$

where:

$d =$ Difference in ranks

# Test of Independence (Categorical Data)

Test statistic

$
\chi^{2} = \sum_{i=1}^{m} \frac{(O_{ij} - E_{ij})^{2}}{E_{ij}}
$

Degrees of freedom $= (r - 1)(c - 1)$

where:

$m =$ Number of cells in the table

$O_{ij} =$ Number of observations in each cell of row $i$ and column $j$

$E_{ij} =$ Expected number of observations in each cell of row $i$ and column $j$

$
= \frac{(\text{Total row } i) \times (\text{Total column } j)}{\text{Overall total}}
$

Standardized Residual (or Pearson Residual)

$
\text{Standardized Residual} = \frac{O_{ij} - E_{ij}}{\sqrt{E_{ij}}}
$

Learning Module 10: Simple Linear Regression

$
Y_{i} = b_{0} + b_{1} X_{1} + \dots + b_{n} X_{n} + \varepsilon_{i}, i = 1, 2, \ldots , n
$

where:

$Y =$ Dependent variable

$X =$ Independent variable

$b_{0} =$ Intercept

$b_{i} =$ Slope coefficient, $i = 1,2,\dots ,n$

$\varepsilon_{i} =$ Error term

$b_{0}, b_{1}, \ldots, b_{n} =$ Regression coefficients

$
\hat{Y}_{i} = \hat{b}_{0} + \hat{b}_{1} X_{i} + e_{i}
$

where:

$\widehat{Y}_i =$ Estimated value on the regression line for the ith observation

$\widehat{b}_0 = \text{Intercept}$

$\hat{b}_{1} = \text{Slope}$

$e_i =$ Residual for the ith observation

$
\hat{b}_{1} = \frac{\textit{Covariance of X and Y}}{\textit{Variance of X}} = \frac{\sum_{i=1}^{n} (Y_{i} - \bar{Y}) (X_{i} - \bar{X})}{\sum_{i=1}^{n} (X_{i} - \bar{X})^{2}}
$

$
\hat{b}_{0} = \bar{Y} - \hat{b}_{1} \bar{X}
$

Sum of Squares Total, $SST = \sum_{i=1}^{n} (Y_i - \bar{Y})^2 = SSR + SSE$

Sum of Squares Regression, $SSR = \sum_{i=1}^{n} (\hat{Y}_i - \bar{Y})^2$

Sum of Squares Error, $SSE = \sum_{i=1}^{n}(Y_{i} - \hat{Y}_{i})^{2} = \sum_{i=1}^{n}e_{i}^{2}$

Coefficient of Determination

$
R^{2} = \frac{SSR}{SST} = 1 - \frac{SSE}{SST}
$

Correlation coefficient

$
r = \frac{\text{Covariance of X and Y}}{\text{(Standard deviation of X) (Standard deviation of Y)}}
$

Note: (Correlation coefficient)2 = Coefficient of determination

Sample standard deviation of X

$
S_{X} = \sqrt{\frac{\sum_{i=1}^{n} (X_{i} - \bar{X})^{2}}{n - 1}}
$

Sample standard deviation of Y

$
S_{Y} = \sqrt{\frac{\sum_{i=1}^{n} (Y_{i} - \bar{Y})^{2}}{n - 1}}
$

Homoskedasticity

$
E(\varepsilon_{i}^{2}) = \sigma_{\varepsilon}^{2}, i = 1, 2, \dots , n
$

# ANOVA F-Test

Mean square regression (MSR)

$
MSR = \frac{SSR}{k}
$

Mean square error (MSE)

$
MSE = \frac{SSE}{n - k - 1}
$

F-distributed test statistic

$
F = \frac{MSR}{MSE}
$

where:

$
n = \text{Number of observations}
$

$
k = \text{Number of independent variables}
$

Standard error of estimate

$
s_{e} = \sqrt{MSE} = \sqrt{\frac{\sum_{i=1}^{n} (Y_{i} - \hat{Y}_{i})^{2}}{n - k - 1}}
$

Hypothesis Test of the Slope Coefficient

$
t = \frac{\hat{b}_{1} - B_{1}}{S_{\hat{b}_{1}}}
$

Degrees of freedom, $df = n - k - 1$

where:

$B_{1} =$ Hypothesized population slope

$s_{\hat{b}_1} =$ Standard error of the slope coefficient

$
= \frac{s_{e}}{\sqrt{\sum_{i=1}^{n} (X_{i} - \bar{X})^{2}}}
$

Hypothesis Test of the Intercept

$
t_{intercept} = \frac{\widehat{b}_{0} - B_{0}}{s_{\widehat{b}_{0}}}
$

Standard error of the intercept, $S_{\hat{b}_0}$

$
s_{\hat{b}_{0}} = \sqrt{\frac{1}{n} + \frac{\bar{X}^{2}}{\sum_{i=1}^{n} (X_{i} - \bar{X})^{2}}}
$

Prediction Intervals

$
\hat{Y}_{f} \pm t_{\alpha / 2} \times s_{f}
$

where: $\hat{Y}_f = \hat{b}_0 + \hat{b}_1X_f$

Variance of the prediction error of Y, given X

$
s_{f}^{2} = s_{e}^{2} \left[ 1 + \frac{1}{n} + \frac{(X_{f} - \bar{X})^{2}}{(n - 1) s_{X}^{2}} \right]
$

Standard error of the forecast

$
s_{f} = s_{e} \sqrt{1 + \frac{1}{n} + \frac{(X_{f} - \bar{X})^{2}}{(n - 1) s_{X}^{2}}}
$

The Log-Lin Model

$
\ln Y_{i} = b_{0} + b_{1} X_{i}
$

The Lin-Log Model

$
Y_{i} = b_{0} + b_{1} \ln X_{i}
$

The Log-Log Model

$
\ln Y_{i} = b_{0} + b_{1} \ln X_{i}
$

Learning Module 11: Introduction to Big Data Techniques

No formula.

# # VOLUME 2: ECONOMICS

Learning Module 1: The Firm and Market Structures

Total profit = Total revenue - Total cost

Economic profit = Total revenue - Total economic costs

Accounting profit = Total revenue - Total accounting costs

Total revenue $=$ Price $\times$ Quantity $= P \times Q$

Average revenue $=$ $\frac{\text{Total revenue}}{\text{Quantity}}$

Marginal cost $=$ $\frac{\Delta TC}{\Delta Q}$

Average variable cost $=$ $\frac{\text{Total variable cost}}{\text{Quantity}}$

Average fixed cost $=$ $\frac{\text{Total fixed cost}}{\text{Quantity}}$

Total cost = Total fixed cost + Total variable cost

Average total cost = Average fixed cost + Average variable cost

# Concentration Ratio

$
\text{Concentration ratio} = \sum_{i=1}^{n} (\text{Market share})_{i}
$

Herfindahl-Hirschman Index (HHI)

$
HHI = \sum_{i=1}^{n} (\text{Market share})_{i}^{2}
$

Learning Module 2: Understanding Business Cycles

No formula

Learning Module 3: Fiscal Policy

$
\text{Budget surplus/(deficit)} = G - T + B
$

where:

$
G = \text{Government}
$

$
T = \text{Taxes}
$

$
B = \text{Payments of transfer benefits}
$

# Disposable Income

$
YD = Y - NT = (1 - t) Y
$

where:

$
t = \text{Net}
$

$
NT = \text{Net} = \text{Taxes} = \text{Taxes} - \text{Transfers}
$

$
tY = \text{Total}
$

# The Fiscal Multiplier

$
\text{Fiscal multiplier} = \frac{1}{1 - c (1 - t)}
$

where:

$
c = \text{Marginal}
$

$
t = \text{Tax rate}
$

Learning Module 4: Monetary Policy

Neutral rate $=$ Trend growth + Inflation target

Learning Module 5: Introduction to Geopolitics

No formula

Learning Module 6: International Trade

No formula

Learning Module 7: Capital Flows and the FX Market

Real exchange rate ${d}_{d/f} = {S}_{d/f} \times \frac{{P}_{f}}{{P}_{d}}$

$
\begin{array}{l} 
\% \text{Change in real exchange rate} = \left(1 + \% \Delta S_{d/f}\right) \times \frac{\left(1 + \% \Delta P_{f}\right)}{\left(1 + \% \Delta P_{d}\right)} - 1 \\ 
\approx \% \Delta S_{d/f} + \% \Delta P_{f} - \% \Delta P_{d} \\ 
\end{array}
$

Percentage change in base currency $f$ (vs currency $d$)

$
\frac{E(S_{d/f}) - S_{d/f}}{S_{d/f}}
$

where:

$
S_{d/f} = \text{Spot exchange rate}
$

$
P_{f} = \text{General price level of goods indexed in currency } f
$

$
P_{d} = \text{General price level of goods indexed in currency } d
$

Learning Module 8: Exchange Rate Calculations

# Cross-Rate

$
\frac{A}{B} = \frac{A}{C} \times \frac{C}{D}
$

# Forward Rate

$
F_{A/B} = S_{A/B} \times \left[ \frac{1 + r_{A} \times T}{1 + r_{B} \times T} \right]
$

$
\begin{array}{l} 
\text{Forward points} = F_{A/B} - S_{A/B} \  
= S_{A/B} \left(\frac{r_{A} - r_{B}}{1 + r_{B}}\right) T \ 
\end{array}
$

where:

$
\begin{array}{l} 
S_{A/B} = \text{Spot exchange rate} \ 
F_{A/B} = \text{Forward exchange rate} \ 
T = \text{Time} \ 
\end{array}
$

# VOLUME 3: CORPORATE ISSUERS

Learning Module 1: Organizational Forms, Corporate Issuer Features, and Ownership

No formula

Learning Module 2: Investors and Other Stakeholders

No formula

Learning Module 3: Working Capital and Liquidity

$$
\begin{array}{l} \begin{array}{c} \text {C a s h c o n v e r s i o n} \\ \text {c y c l e} \end{array} = \begin{array}{c} \text {D a y s o f i n v e n t o r y} \\ \text {o n h a n d} \end{array} + \begin{array}{c} \text {D a y s s a l e s} \\ \text {o u t s t a n d i n g} \end{array} - \begin{array}{c} \text {D a y s p a y a b l e s} \\ \text {o u t s t a n d i n g} \end{array} \\ \frac{EAR\ of\ Supplier}{Financing} = \Big(1 + \frac{Discount\%}{100\% - Discount\%}\Big)^{\frac{Days\ in\ Year}{Payment\ Period - Discount\ Period}} - 1 \\ \end{array}
$$

Total working capital = Current assets - Current Liabilities

$$
\begin{array}{r l} & {\frac {N e t w o r k i n g}{c a p i t a l} = C u r r e n t a s s e t s (e x c l u d i n g c a s h a n d m a r k e t a b l e s e c u r i t i e s)} \\ & {- C u r r e n t L i a b i l i t i e s (e x c l u d i n g s h o r t - t e r m a n d c u r r e n t d e b t)} \end{array}
$$

Cash flow from operations

$$
\begin{array}{r l} & {= \text {C a s h r e c e i v e d f r o m c u t s o m e r s}} \\ & {\quad + \text {I n t e r s t a n d d i v i d e n d s r e c e i v e d o n f i n a n c i a l i n v e s t m e n t s}} \\ & {\quad - \text {C a s h p a i d t o e m p l e y e e s a n d s u p p l i e r s}} \\ & {\quad - \text {T a x e s p a i d t o g o v e r n m e n t s}} \\ & {\quad - \text {I n t e r s t a n d p a i l e r s}} \end{array}
$$

Free cash flow = Cash flow from operations - Investments in long-term assets

$$
C u r r e n t r a t i o = \frac {C u r r e n t a s s e t s}{C u r r e n t l i a b i l i t i e s}
$$

$$
Q u i c k r a t i o = \frac {C a s h + S h o r t - t e r m m a r k e t a b l e i n s t r u m e n t s + R e c e i v a b l e s}{C u r r e n t l i a b i l i t i e s}
$$

$$
C a s h r a t i o = \frac {C a s h + S h o r t - t e r m m a r k e t a b l e i n s t r u m e n t s}{C u r r e n t l i a b i l i t i e s}
$$

Learning Module 4: Corporate Governance: Conflicts, Mechanisms, Risks, and Benefits

No formula

Learning Module 5: Capital Investments and Capital Allocation

# Net Present Value

$$
N P V = C F _ {0} + \frac {C F _ {1}}{(1 + r) ^ {1}} + \frac {C F _ {2}}{(1 + r) ^ {2}} + \dots + \frac {C F _ {T}}{(1 + r) ^ {T}} = \sum_ {t = 0} ^ {T} \frac {C F _ {t}}{(1 + r) ^ {t}}
$$

where:

$CF_{t} =$  After-tax cash flow at time  $t$

$r =$  Required rate of return

$CF_0 = \text{Initial outlay}$

# Internal Rate of Return

$$
\sum_ {t = 0} ^ {T} \frac {C F _ {t}}{(1 + I R R) ^ {t}} = 0
$$

Video: https://youtu.be/bzck7QLhICw

# Return on Invested Capital

$$
\begin{array}{l} R O I C = \frac {A f t e r - t a x o p e r a t i n g p r o f i t}{A v e r a g e i n v e s t e d c a p i t a l} \\ = \frac {\text {O p e r a t i n g p r o f i t} _ {t} \times (1 - \text {T a x r a t e})}{\text {A v e r a g e t o t a l l o n g - t e r m l i a b i l i t i e s a n d e q u i t y} _ {t - 1 , t}} \\ \end{array}
$$

$$
R O I C = \frac {A f t e r - t a x o p e r a t i n g p r o f i t}{S a l e s} \times \frac {S a l e s}{A v e r a g e i n v e s t e d c a p i t a l}
$$

# Real Options in Capital Budgeting

$$
\begin{array}{c} \text {P r o j e c t N P V} \\ (\text {w i t h o p t i o n}) \end{array} = \begin{array}{c} \text {P r o j e c t N P V} \\ (\text {w i t h o u t o p t i o n}) \end{array} - \text {O p t i o n c o s t} + \text {O p t i o n v a l u e}
$$

# Weighted Average Cost of Capital

$$
W A C C = w _ {d} r _ {d} (1 - t) + w _ {e} r _ {e}
$$

where:

$$
\begin{array}{l} w _ {d} = \text {T a r g e t w e i g h t o f d e b t i n c a p i t a l s t r u c t u r e} = \frac {D}{D + E} \\ w _ {e} = \text {T a r g e t w e i g h t o f c o m m o n s t o c k i n c a p i t a l s t r u c t u r e} = \frac {E}{D + E} \\ \end{array}
$$

$$
\begin{array}{l} r _ {d} = \text {B e f o r e - t a x m a r g i n a l c o s t o f d e b t} \\ t = \text {M a r g i n a l} \\ r _ {d} (1 - t) = \text {A f t e r - t a x m a r g i n a l c o s t o f d e b t} \\ r _ {e} = \text {M a r g i n a l} \\ \end{array}
$$

# Operating Leverage

$$
O p e r a t i n g l e v e r a g e = \frac {F i x e d c o s t s}{T o t a l c o s t s}
$$

# Interest Coverage

$$
I n t e r e s t c o v e r a g e = \frac {P r o f i t b e f o r e i n t e r e s t a n d t a x e s}{I n t e r e s t e x p e n s e}
$$

# Modigliani-Miller Capital Structure Propositions

$$
V _ {L} = V _ {U} + t D
$$

$$
r _ {e} = r _ {0} + (r _ {0} - r _ {d}) (1 - t) \frac {D}{E}
$$

$$
E = \frac {(C F _ {e} - r _ {d} D) (1 - t)}{r _ {e}}
$$

$$
V _ {L} = \frac {C F _ {e} (1 - t)}{r _ {W A C C}}
$$

where:

$$
V _ {L} = \text {V a l u e o f l e v e r e d f i r m}
$$

$$
V _ {U} = \text {V a l u e o f u n l e v e r e d f i r m}
$$

$$
t = \text {M a r g i n a l}
$$

$$
r _ {e} = \text {C o s t o f e q u i t y}
$$

$$
r _ {d} = \text {C o s t o f d e b t}
$$

$$
r_{0} = \text{Cost of capital (for a 100\% equity-financed company)}
$$

$$
D = \text {M a r k e t v a l u e o f d e b t}
$$

$$
E = \text {M a r k e t v a l u e o f e q u i t y}
$$

$$
C F _ {e} = \text {A f t e r - t a x c a s h f l o w s t o s h a r e s h o l d e r s}
$$

$$
r _ {d} D = \text {I n t e r e s t}
$$

# Static Trade-off Theory of Capital Structure

$$
V _ {L} = V _ {U} + t D - P V (C o s t s \text {o f F i n a n c i a l D i s t r e s s})
$$

Learning Module 7: Business Models

No formula

# VOLUME 4: FINANCIAL STATEMENT ANALYSIS

Learning Module 1: Introduction to Financial Statement Analysis

No formula

Learning Module 2: Analyzing Income Statements

Gross profit = Revenue - Cost of Goods Sold

Operating income = Gross margin - Selling, General, and Administrative Expense

Taxable income = Operating income - Interest expense

Net income = Taxable income - Taxes

Ending shareholders' equity = Beginning shareholders' equity + Net income  
+ Other comprehensive income  
- Dividends  
+Net capital contributions from shareholders

Ending retained earnings = Beginning retained earnings + Net income - Dividends

# Return on Equity

$$
R O E = \frac {\text {N e t i n c o m e}}{\text {A v e r a g e s h a r e h o l d e r s} ^ {\prime} \text {e q u i t y}}
$$

# Net Profit Margin

$$
N e t p r o f i t m a r g i n = \frac {N e t i n c o m e}{R e v e n u e}
$$

# Basic EPS

$$
B a s i c E P S = \frac {N e t i n c o m e - P r e f e r r e d d i v i d e n d s}{W e i g h t e d a v e r a g e n u m b e r o f s h a r e s o u t s t a n d i n g}
$$

# Diluted EPS (for convertible preferred stock)

$$
D i l u t e d E P S = \frac {N e t i n c o m e}{\underset {\text {W e i g h t e d a v e r a g e n u m b e r}} {W e i g h t e d a v e r a g e n u m b e r}} + \underset {\text {o f s h a r e s o u t s t a n d i n g}} {N e w c o m m o n s h a r e s t h a t w o u l d}
$$

# Diluted EPS (for convertible debt)

$$
D i l u t e d E P S = \frac {N e t i n c o m e - P r e f e r r e d d i v i d e n d s + ^ {A f t e r t a x i n t e r e s t e x p e n s e} o n c o n v e r t i b l e d e b t}{\text {W e i g h t e d a v e r a g e n u m b e r} + \text {N e w c o m m o n s h a r e s t h a t w o u l d o f s h a r e s o u t s t a n d i n g} \quad \text {h a v e b e e n i s s u e d a t c o n v e r s i o n}}
$$

# Diluted EPS (for options)

$$
D i l u t e d E P S = \frac {N e t i n c o m e - P r e f e r r e d d i v i d e n d s}{\underset {\text {W e i g h t e d a v e r a g e n u m b e r}} {W e i g h t e d a v e r a g e n u m b e r}} + \underset {\text {o f s h a r e s o u t s t a n d i n g}} {A d d i t i o n a l c o m m o n} + \underset {\text {c o n v e r s i o n}} {s h a r e s i s s u e d u p o n}
$$

# Treasury stock method

$$
\begin{array}{c} \text {A d d i t i o n a l c o m m o n} \\ \text {s h a r e s i s s u e d u p o n} = \left( \begin{array}{c c} \text {N e w s h a r e s} & \text {S h a r e s r e p u r c h a s e d} \\ \text {i s s u e d a t} & - \text {w i t h c a s h r e c e i v e d} \\ \text {o p t i o n e x e r c i s e} & \text {f r o m o p t i o n e x e r c i s e d} \end{array} \right) \times \text {d u r i n g w h i c h o p t i o n s} \\ \text {c o n v e r s i o n} \end{array}
$$

Video (Basic & Diluted EPS): https://youtu.be/2C-mwVqO2SQ

Learning Module 3: Analyzing Balance Sheets

Working capital = Current assets - Current liabilities

# Liquidity Ratios

$$
C u r r e n t r a t i o = \frac {C u r r e n t a s s e t s}{C u r r e n t l i a b i l i t i e s}
$$

$$
Q u i c k (a c i d t e s t) r a t i o = \frac {C a s h + M a r k e t a b l e s e c u r i t i e s + R e c e i v a b l e s}{C u r r e n t l i a b i l i t i e s}
$$

$$
C a s h r a t i o = \frac {C a s h + M a r k e t a b l e s e c u r i t i e s}{C u n c r e n t l i a b i l i t i e s}
$$

# Solvency Ratios

$$
L o n g - t e r m d e b t - t o - e q u i t y = \frac {L o n g - t e r m d e b t}{T o t a l e q u i t y}
$$

$$
D e b t - t o - e q u i t y = \frac {T o t a l d e b t}{T o t a l e q u i t y}
$$

$$
T o t a l d e b t = \frac {T o t a l d e b t}{T o t a l a s s e t s}
$$

$$
F i n a n c i a l l e v e r a g e = \frac {T o t a l a s s e t s}{T o t a l e q u i t y}
$$

# Learning Module 4: Analyzing Statements of Cash Flows I

$$
\begin{array}{l} \frac {E n d i n g}{c a s h} = \frac {B e g i n n i n g}{c a s h} + \frac {C a s h f l o w}{f r o m o p e r a t i n g} + \frac {C a s h f l o w}{f r o m i n v e s t i n g} + \frac {C a s h f l o w}{f r o m f i n a n c i n g} \\ \begin{array}{c} E n d i n g a c c o u n t s \\ r e c e i v a b l e \end{array} = \begin{array}{c} B e g i n n i n g a c c o u n t s \\ r e c e i v a b l e \end{array} + R e v e n u e - \begin{array}{c} C a s h c o l l e c t e d \\ f r o m c u s t o m e r s \end{array} \\ \begin{array}{c} E n d i n g \\ i n v e n t o r y \end{array} = \begin{array}{c} B e g i n n i n g \\ i n v e n t o r y \end{array} + P u r c h a s e s - \begin{array}{c} C o s t o f \\ g o o d s s o l d \end{array} \\ \begin{array}{c} E n d i n g a c c o u n t s \\ p a y a b l e \end{array} = \begin{array}{c} B e g i n n i n g a c c o u n t s \\ p a y a b l e \end{array} + P u r c h a s e s - \begin{array}{c} C a s h p a i d \\ t o s u p p l i e r s \end{array} \\ \begin{array}{c} E n d i n g w a g e s \\ p a y a b l e \end{array} = \begin{array}{c} B e g i n n i n g w a g e s \\ p a y a b l e \end{array} + \begin{array}{c} W a g e s \\ e x p e n s e \end{array} - \begin{array}{c} C a s h p a i d \\ t o e m p l o y e e s \end{array} \\ \begin{array}{c} E n d i n g i n t e r e s t \\ p a y a b l e \end{array} = \begin{array}{c} B e g i n n i n g i n t e r e s t \\ p a y a b l e \end{array} + \begin{array}{c} I n t e r e s t \\ e x p e n s e \end{array} - \begin{array}{c} C a s h p a i d \\ f o r i n t e r e s t \end{array} \\ \begin{array}{c} E n d i n g i n c o m e \\ t a x p a y a b l e \end{array} = \begin{array}{c} B e g i n n i n g i n c o m e \\ t a x p a y a b l e \end{array} + \begin{array}{c} I n c o m e t a x \\ e x p e n s e \end{array} - \begin{array}{c} C a s h p a i d \\ f o r i n c o m e t a x e s \end{array} \\ E n d i n g P P \& E = B e g i n n i n g P P \& E + \frac {E q u i p m e n t}{p u r c h a s e d} - \frac {E q u i p m e n t}{s o l d} \\ \frac {E n d i n g a c c u m u l a t e d}{d e p r e c i a t i o n} = \frac {B e g i n n i n g a c c u m u l a t e d}{d e p r e c i a t i o n} + \frac {D e p r e c i a t i o n}{e x p e n s e} - \frac {A c c u m u l a t e d}{d e p r e c i a t i o n o n} \\ \end{array}
$$

# Note:

Gain on sale  $= \frac{\text{Cash received from Book value of}}{\text{sale of equipment}} -$  Book value of of equipment sold

$$
\begin{array}{c} E n d i n g r e t a i n e d \\ e a r n i n g s \end{array} = \begin{array}{c} B e g i n n i n g r e t a i n e d \\ e a r n i n g s \end{array} + \begin{array}{c} N e t \\ i n c o m e \end{array} - D i v i d e n d s
$$

# Free Cash Flow To Firm (FCFF)

$$
\begin{array}{l} F C F F = N I + N C C + I n t (1 - T a x r a t e) - F C I n v - W C I n v \\ = C F O + I n t (1 - T a x r a t e) - F C I n v \\ \end{array}
$$

where:

$$
N I = \text {N e t i n c o m e}
$$

$$
N C C = \text {N o n - c a s h}
$$

$$
I n t = \text {I n t e r s t}
$$

$$
F C I n v = \text {C a p i t a l}
$$

$$
W C I n v = \text {W o r k i n g}
$$

$$
C F O = \text {C a s h f l o w} = N I + N C C - W C I n v
$$

# Free Cash Flow to Equity (FCFE)

$$
F C F E = C F O - F C I n v + N e t B o r r o w i n g
$$

where:

Net Borrowing  $=$  Debt issued - Debt repaid

# Performance Ratios

$$
C a s h f l o w t o r e v e n u e = \frac {C F O}{R e v e n u e}
$$

$$
C a s h r e t u r n o n a s s e t s = \frac {C F O}{A v e r a g e t o t a l a s s e t s}
$$

$$
C a s h r e t u r n o n e q u i t y = \frac {C F O}{A v e r a g e s h a r e h o l d e r s e q u i t y}
$$

$$
C a s h t o i n c o m e = \frac {C F O}{O p e r a t i n g i n c o m e}
$$

$$
C a s h f l o w p e r s h a r e = \frac {C F O - P r e f e r e d d i v i d e n d s}{N u m b e r o f c o m m o n s h a r e s o u t s t a n d i n g}
$$

# Coverage Ratios

$$
D e b t c o v e r a g e r a t i o = \frac {C F O}{T o t a l d e b t}
$$

$$
I n t e r e s t c o v e r a g e r a t i o = \frac {C F O + I n t e r e s t p a i d + T a x e s p a i d}{I n t e r e s t p a i d}
$$

$$
R e i n v e s t m e n t r a t i o = \frac {C F O}{C a s h p a i d f o r l o n g t e r m a s s e t s}
$$

$$
D e b t p a y m e n t r a t i o = \frac {C F O}{C a s h p a i d f o r l o n g t e r m d e b t r e p a y m e n t}
$$

$$
D i v i d e n d p a y m e n t r a t i o = \frac {C F O}{D i v i d e n d s p a i d}
$$

$$
\text {I n v e s t i n g a n d f i n a n c i n g r a t i o} = \frac {C F O}{\text {C a s h f l o w f o r i n v e s t i n g a n d}}
$$

# Learning Module 6: Analysis of Inventories

# IFRS

Inventories  $=$  Lower of Cost and Net Realizable Value (NRV)

$NRV =$  Estimated selling price less estimated costs of completion and costs necessary to complete the sale

# US GAAP

Inventories  $=$  Lower of Cost and NRV

For last-in, first-out (LIFO) method or retail inventory methods

Inventories = Lower of Cost and Market Value

Market value = Current replacement cost (subject to lower and upper limits)

Lower limit  $= N R V - N o r m a l p r o f i t m a r g i n$

Upper limit  $= NRV$

Video: https://youtu.be/V8C31mslBzs

Inventory turnover ratio =  $\frac{\text{Cost of sales}}{\text{Average inventory}}$

Days of inventory on hand =  $\frac{\text{Number of days in period}}{\text{Inventory turnover ratio}}$

Ending inventory (FIFO) = Ending inventory (LIFO) + LIFO reserve

COGS (FIFO) = COGS (LIFO) - Change in LIFO reserve

Learning Module 7: Analysis of Long-Term Assets

Net book value = Historical cost - Accumulated depreciation

Gain on sale of asset  $=$  Sale proceeds-Net book value

$$
\begin{array}{l} \begin{array}{c} E s t i m a t e d \text {t o t a l} \\ \text {u s e f u l l i f e} \end{array} = \begin{array}{c} E s t i m a t e d \text {a g e} \\ \text {o f e q u i p m e n t} \end{array} + \begin{array}{c} E s t i m a t e d \\ \text {r e m a i n i n g l i f e} \end{array} \\ \frac {\text {E s t i m a t e d t o t a l}}{\text {u s e f u l l i f e}} = \frac {\text {G r o s s P P} \& E}{\text {A n n u a l d e p r e c i a t i o n e x p e n s e}} \\ \frac {\text {E s t i m a t e d a g e}}{\text {o f e q u i p m e n t}} = \frac {\text {A c c u m u l a t e d d e p r e c i a t i o n}}{\text {A n n u a l d e p r e c i a t i o n e x p e n s e}} \\ \frac {\text {E s t i m a t e d}}{\text {r e m a i n i n g l i f e}} = \frac {\text {N e t P P} \& E}{\text {A n n u a l d e p r e c i a t i o n e x p e n s e}} \\ \end{array}
$$

# Straight-line Depreciation

$$
A n n u a l d e p r e c i a t i o n e x p e n s e = \frac {H i s t o r i c a l c o s t - S a l v a g e v a l u e}{E s t i m a t e d u s e f u l l i f e}
$$

# Fixed Asset Turnover

$$
F i x e d a s s e t t u r n o v e r = \frac {R e v e n u e}{A v e r a g e n e t P P \& E}
$$

# Impairment of Long-Lived Assets

# IFRS

$$
\text {I m p a i r m e n t} = \text {C a r r y i n g a m o u n t} - \text {R e c o v e r a b l e a m o u n t}
$$

where:

Recoverable amount = max(Fair value less costs to sell, Value in use)

# US GAAP

If asset's carrying amount  $>$  undiscounted expected future cash flows:

Impairment = Carrying amount - Fair value

Learning Module 8: Topics in Long-Term Liabilities and Equity

# Lessee Accounting - Finance Lease (IFRS)

Interest expense on lease  $=$  Implied interest rate  $\times$  Beginning lease liability

Principal repayment  $=$  Lease payment - Interest expense

Ending lease  $= \begin{array}{l}B e g i n n i n g l e a s e \\ l i a b i l i t y\end{array} + I n t e r e s t e x p e n s e - L e a s e p a y m e n t$

If ROU asset is amortized on a straight-line basis:

$$
\frac {\text {A m o r t i z a t i o n}}{\text {e x p e n s e}} = \frac {\text {I n i t i a l R O U a s s e t v a l u e - S a l v a g e v a l u e}}{\text {L e a s e t e r m}}
$$

Ending ROU  $=$  Beginning ROU -Amortization asset asset expense

# Lessee Accounting - Operating Lease (US GAAP)

$$
\underset {e x p e n s e} {A m o r t i z a t i o n} = L e a s e p a y m e n t - I n t e r e s t e x p e n s e
$$

$$
\begin{array}{c} E n d i n g R O U \\ a s s e t \end{array} = \begin{array}{c} B e g i n n i n g R O U \\ a s s e t \end{array} - \begin{array}{c} A m o r t i z a t i o n \\ e x p e n s e \end{array}
$$

$$
\begin{array}{c} E n d i n g \text {l e a s e} \\ \text {l i a b i l i t y} \end{array} = \begin{array}{c} B e g i n n i n g \text {l e a s e} \\ \text {l i a b i l i t y} \end{array} - \begin{array}{c} A m o r t i z a t i o n \\ \text {e x p e n s e} \end{array}
$$

# Stock Options

Compensation expense =  $\frac{\text{Fair value of options granted}}{\text{Vesting period}}$

Learning Module 9: Analysis of Income Taxes

# Deferred Tax Asset/Liability

For Assets:

$$
\frac {D e f e r r e d t a x}{l i a b i l i t y / (a s s e t)} = T a x r a t e \times \left( \begin{array}{c} C a r r y i n g a m o u n t - T a x b a s e \\ o f a s s e t - o f a s s e t \end{array} \right)
$$

For Liabilities:

$$
\frac {D e f e r r e d t a x}{l i a b i l i t y / (a s s e t)} = T a x r a t e \times \left( \begin{array}{c} T a x b a s e \\ o f l i a b i l i t y \end{array} - \begin{array}{c} C a r r y i n g a m o u n t \\ o f l i a b i l i t y \end{array} \right)
$$

Income tax expense = Income tax payable + Changes in deferred tax assets and liabilities

Effective tax rate =  $\frac{\text{Income tax expense}}{\text{Pre-tax income}}$

Cash tax rate =  $\frac{\text{Cash tax}}{\text{Pre-tax income}}$

Learning Module 10: Financial Reporting Quality

# Adjusted EBITDA

$$
\underset {E B I T D A} {A d j u s t e d} = \underset {E B I T} {A d j u s t e d} + \underset {a m o r t i z a t i o n} {\text {S o f t w a r e}} + \underset {a m o r t i z a t i o n} {\text {D e p r e c i a t i o n}} + \underset {a m o r t i z a t i o n} {\text {P o s t - I P O}}
$$

# Straight-line method of depreciation

$$
D e p r e c i a t i o n e x p e n s e = \frac {C o s t - S a l v a g e v a l u e}{U s e f u l l i f e}
$$

# Double-Declining Balance method

$$
D e p r e c i a t o n e x p e n s e = \frac {2}{U s e f u l l i f e} \times (C o s t - A c c u m u l a t e d d e p r e c i a t i o n)
$$

Video: https://youtu.be/6RskYAxdAFk

# Units-of-Production method

$$
D e p r e c i a t i o n \enspace e x p e n s e = \frac {\text {U n i t s p r o d u c e d}}{\text {T o t a l u n i t s o v e r u s e f u l l i f e}} \times (\text {C o s t - S a l v a g e v a l u e})
$$

# Activity Ratios

$$
I n v e n t o r y t u r n o v e r = \frac {C o s t o f s a l e s}{A v e r a g e i n v e n t o r y}
$$

$$
D a y s o f i n v e n t o r y o n h a n d = \frac {N u m b e r o f d a y s i n t h e p e r i o d}{I n v e n t o r y t u r n o v e r}
$$

$$
R e c e i v a b l e s t u r n o v e r = \frac {R e v e n u e}{A v e r a g e r e c e i v a b l e s}
$$

$$
D a y s o f s a l e s o u t s t a n d i n g = \frac {\text {N u m b e r o f d a y s i n t h e p e r i o d}}{\text {R e c e i v a b l e s t u r n o v e r}}
$$

$$
P a y a b l e s t u r n o v e r = \frac {P u r c h a s e s}{A v e r a g e p a y a b l e s}
$$

$$
N u m b e r o f d a y s o f p a y a b l e s = \frac {N u m b e r o f d a y s i n t h e p e r i o d}{P a y a b l e s t u r n o v e r}
$$

$$
\text {W o r k i n g c a p i t a l t u r n o v e r} = \frac {\text {R e v e n u e}}{\text {A v e r a g e w o r k i n g c a p i t a l}}
$$

$$
F i x e d a s s e t t u r n o v e r = \frac {R e v e n u e}{A v e r a g e n e t f i x e d a s s e t s}
$$

$$
T o t a l a s s e t t u r n o v e r = \frac {R e v e n u e}{A v e r a g e t o t a l a s s e t s}
$$

# Liquidity Ratios

$$
C u r r e n t r a t i o = \frac {C u r r e n t a s s e t s}{C u r r e n t l i a b i l i t i e s}
$$

$$
\text {Q u i c k r a t i o} = \frac {\text {C a s h} + \text {S h o r t t e r m m a r k e t a b l e i n v e s t m e n t s} + \text {R e c e i v a b l e s}}{\text {C u r r e n t l i a b i l i t i e s}}
$$

$$
C a s h r a t i o = \frac {C a s h + S h o r t t e r m m a r k e t a b l e i n v e s t m e n t s}{C u r r e n t l i a b i l i t i e s}
$$

$$
\frac {\text {D e f e n s i v e i n t e r v a l}}{\text {r a t i o}} = \frac {\text {C a s h} + \text {S h o r t t e r m m a r k e t a b l e i n v e s t m e n t s} + \text {R e c e i v a b l e s}}{\text {D a i l y c a s h e x p e n d i t u r e s}}
$$

$$
\begin{array}{c} \text {C a s h c o n v e r s i o n} \\ \text {c y c l e} \end{array} = \begin{array}{c} \text {D a y s o f i n v e n t o r y} \\ \text {o n h a n d} \end{array} + \begin{array}{c} \text {D a y s o f s a l e s} \\ \text {o u t s t a n d i n g} \end{array} - \begin{array}{c} \text {N u m b e r o f d a y s} \\ \text {o f p a y a b l e s} \end{array}
$$

Video (Cash Conversion Cycle): https://youtu.be/IFsl9c4wUD4

# Solvency Ratios

$$
\begin{array}{c} D e b t - t o - a s s e t s r a t i o \\ \text {(}" T o t a l d e b t r a t i o ")} \end{array} = \frac {T o t a l d e b t}{T o t a l a s s e t s}
$$

$$
D e b t - t o - c a p i t a l r a t i o = \frac {T o t a l d e b t}{T o t a l d e b t + T o t a l e q u i t y}
$$

$$
D e b t - t o - e q u i t y r a t i o = \frac {T o t a l d e b t}{T o t a l e q u i t y}
$$

$$
F i n a n c i a l \quad l e v e r a g e \quad r a t i o = \frac {A v e r a g e \quad t o t a l \quad a s s e t s}{A v e r a g e \quad t o t a l \quad e q u i t y}
$$

$$
D e b t - t o - E B I T D A r a t i o = \frac {T o t a l o r n e t d e b t}{E B I T D A}
$$

# Coverage Ratios

$$
I n t e r e s t c o v e r a g e r a t i o = \frac {E B I T}{I n t e r e s t p a y m e n t s}
$$

$$
F i x e d c h a r g e c o v e r a g e r a t i o = \frac {E B I T + L e a s e p a y m e n t s}{I n t e r e s t p a y m e n t s + L e a s e p a y m e n t s}
$$

# Profitability Ratios

$$
G r o s s p r o f i t m a r g i n = \frac {G r o s s p r o f i t}{R e v e n u e}
$$

$$
\text {O p e r a t i n g} = \frac {\text {O p e r a t i n g} = \frac {\text {I n c o m e}}{\text {R e v e n u e}}
$$

$$
P r e t a x m a r g i n = \frac {E B T}{R e v e n u e}
$$

$$
N e t p r o f i t m a r g i n = \frac {N e t i n c o m e}{R e v e n u e}
$$

$$
O p e r a t i n g R O A = \frac {O p e r a t i n g i n c o m e}{A v e r a g e t o t a l a s s e t s}
$$

$$
R O A = \frac {N e t i n c o m e}{A v e r a g e t o t a l a s s e t s}
$$

$$
R e t u r n o n i n v e s t e d c a p i t a l = \frac {E B I T \times (1 - E f f e c t i v e t a x r a t e)}{A v e r a g e t o t a l d e b t a n d e q u i t y}
$$

$$
R O E = \frac {N e t i n c o m e}{A v e r a g e t o t a l e q u i t y}
$$

$$
R e t u r n o n c o m m o n e q u i t y = \frac {N e t i n c o m e - P r e f e r r e d d i v i d e n d s}{A v e r a g e c o m m o n e q u i t y}
$$

# DuPont Analysis

$$
R O E = R O A \times F i n a n c i a l L e v e r a g e
$$

$$
R O E = N e t p r o f i t m a r g i n \times T o t a l a s s e t t u r n o v e r \times F i n a n c i a l l e v e r a g e
$$

$$
R O E = \frac {T a x}{b u r d e n} \times \frac {I n t e r e s t}{b u r d e n} \times \frac {E B I T}{m a r g i n} \times \frac {T o t a l a s s e t}{t u r n o v e r} \times \frac {F i n a n c i a l}{l e v e r a g e}
$$

where:

$$
T a x b u r d e n = \frac {N e t i n c o m e}{E B T}
$$

$$
I n t e r e s t b u r d e n = \frac {E B T}{E B I T}
$$

# Business Risk

$$
\frac {\text {C o e f f i c i e n t o f v a r i a t i o n}}{\text {o f o p e r a t i n g i n c o m e}} = \frac {\text {S t a n d a r d d e v i a t i o n o f o p e r a t i n g i n c o m e}}{\text {A v e r a g e o p e r a t i n g i n c o m e}}
$$

$$
\frac {\text {C o e f f i c i e n t o f v a r i a t i o n}}{\text {o f n e t i n c o m e}} = \frac {\text {S t a n d a r d d e v i a t i o n o f n e t i n c o m e}}{\text {A v e r a g e n e t i n c o m e}}
$$

$$
\frac {C o e f f i c i e n t o f v a r i a t i o n}{o f r e v e n u e} = \frac {S t a n d a r d d e v i a t i o n o f r e v e n u e}{A v e r a g e r e v e n u e}
$$

# Financial Sector Ratios

$$
\begin{array}{c} \text {M o n e t a r y r e s e r v e r e q u i r e m e n t} \\ (\text {C a s h r e s e r v e r a t i o}) \end{array} = \frac {\text {R e s e r v e s h e l d a t c e n t r a l b a n k}}{\text {S p e c i f i e d d e p o s i t l i a b i l i t i e s}}
$$

$$
N e t i n t e r e s t m a r g i n = \frac {N e t i n t e r e s t i n c o m e}{T o t a l i n t e r e s t e a r n i n g a s s e t s}
$$

$$
L i q u i d a s s e t r e q u i r e m e n t = \frac {A p p r o v e d r e a d i l y m a r k e t a b l e s e c u r i t i e s}{S p e c i f i e d d e p o s i t l i a b i l i t i e s}
$$

$$
N e t i n t e r e s t m a r g i n = \frac {N e t i n t e r e s t i n c o m e}{T o t a l i n t e r e s t e a r n i n g a s s e t s}
$$

Learning Module 12: Introduction to Financial Statement Modeling

Nothing new.

Learning Module 1: Market Organization and Structure

$$
M a x i m u m l e v e r a g e r a t i o = \frac {1}{\text {M i n i m u m m a r g i n r e q u i r e m e n t}}
$$

Total return on leveraged stock investment:

$$
T o t a l R e t u r n = \frac {\underset {p r o c e e d s} {S a l e s} + D i v i d e n d s - L o a n - \underset {i n t e r e s t} {M a r g i n} - \underset {c o m m i s s i o n} {S a l e s}}{\underset {e q u i t y} {I n i t i a l} + \underset {c o m m i s s i o n} {P u r c h a s e}} - 1
$$

$$
I n i t i a l e q u i t y = \frac {\text {M i n i m u m m a r g i n}}{\text {r e q u i r e m e n t}} \times \text {T o t a l p u r c h a s e p r i c e}
$$

Video (Return on Leveraged Stock Position): https://youtu.be/tZd4Xtvjjll

$$
M a r g i n C a l l P r i c e = \frac {P _ {0} (1 - I n i t i a l M a r g i n)}{(1 - M a i n t e n a n c e M a r g i n)}
$$

Learning Module 2: Security Market Indexes

$$
\text {P r i c e R e t u r n I n d e x}, \quad V _ {P R I} = \frac {\sum_ {i = 1} ^ {N} n _ {i} P _ {i}}{D}
$$

where:  $n_i =$  the number of units of constituent security  $i$  held in the index portfolio

$N =$  the number of constituent securities in the index

$P_{i} =$  the unit price of constituent security  $i$

$D =$  value of the divisor

$$
P r e c e \text {r e t u r n o f a n i n d e x}, \quad P R _ {I} = \frac {V _ {P R I 1} - V _ {P R I 0}}{V _ {P R I 0}}
$$

$$
\text {T o t a l R e t u r n I n d e x}, \quad T R _ {I} = \frac {V _ {P R I 1} - V _ {P R I 0} + I n c _ {I}}{V _ {P R I 0}}
$$

where:

$V_{PRI1} =$  value of the price return index at the end of the period

$V_{PRIO} =$  value of the price return index at the beginning of the period

$Inc_{I} =$  total income (dividends and/or interest) from all securities in the index held over the period

# Weighting Methods

$$
\mathrm {P r i c e w e i g h t i n g}, \qquad w _ {i} ^ {P} = \frac {P _ {i}}{\sum_ {j = 1} ^ {N} P _ {j}}
$$

Video (Recalculating the divisor of a price weighted index): https://youtu.be/eYiZNK-ETrg

$$
\mathrm {E q u a l w e i g h t i n g}, \qquad w _ {i} ^ {E} = \frac {1}{N}
$$

$$
\mathrm {M a r k e t - c a p i t a l i z a t i o n w e i g h t i n g ,} \qquad w _ {i} ^ {M} = \frac {Q _ {i} P _ {i}}{\sum_ {j = 1} ^ {N} Q _ {j} P _ {j}}
$$

$$
\mathrm {F l o a t - a d j u s t e d m a r k e t c a p i t a l i z a t i o n w e i g h t i n g ,} \qquad w _ {i} ^ {M} = \frac {f _ {i} Q _ {i} P _ {i}}{\sum_ {j = 1} ^ {N} f _ {j} Q _ {j} P _ {j}}
$$

where:

$$
f _ {i} = \text {f r a c t i o n o f s h a r e s o u t d a n s t i n g i n t h e m a k e t f l o a t}
$$

$$
Q _ {i} = \text {n u m b e r o f s h a r e s o u t d a n s i n g o f s e c u r i t y} i
$$

$$
P _ {i} = \text {s h a r e p r i c e o f s e c u r i t y} i
$$

$$
N = \text {n u m b e r o f s e c u r i t i e s i n t h e i n d e x}
$$

$$
\mathrm {F u n d a m e n t a l w e i g h t i n g}, \qquad w _ {i} ^ {F} = \frac {F _ {i}}{\sum_ {j = 1} ^ {N} F _ {j}}
$$

where  $F_{i}$  denotes a fundamental size measure of company  $i$

# Learning Module 3: Market Efficiency

# No formula

# Learning Module 4: Overview of Equity Securities

Return on Equity (using average total book value of equity)

$$
R O E _ {t} = \frac {N I _ {t}}{(B V E _ {t} + B V E _ {t - 1}) / 2}
$$

Return on Equity (using beginning book value of equity)

$$
R O E _ {t} = \frac {N I _ {t}}{B V E _ {t - 1}}
$$

where BVE = book value (Assets - Liabilities)

Learning Module 5: Company Analysis: Past and Present

$$
M a r k e t s h a r e = \frac {R e v e n u e}{M a r k e t s i z e}
$$

Sales potential = 100% - Market share%

Net sales  $=$  Average selling price  $\times$  Quantity sold

$$
\text {Take rate} = \frac {\text {Revenue earned from transactions}}{\text {Total transaction volume}} \times 100 \%
$$

Operating income  $= Q \times (P - VC) - FC$

where:

$$
Q = \text {U n i t s}
$$

$$
P = \text {P r i c e p e r u n i t}
$$

$$
V C = \text {V a r i a b l e}
$$

$$
F C = \text {F i x e d}
$$

$$
P - V C = \text {C o n t r i b u t i o n}
$$

Degree of operating leverage (DOL) =  $\frac{\%\Delta\text{Operating income}}{\%\Delta\text{Sales}}$

Degree of financial leverage (DFL) =  $\frac{\% \Delta \text{Net income}}{\% \Delta \text{Operating income}}$

$$
W A C C = \underset {o f d e b t} {W e i g h t} \times \underset {o f d e b t} {G r o s s c o s t} \times (1 - t a x r a t e) + \underset {o f e q u i t y} {W e i g h t} \times \underset {e q u i t y} {C o s t o f}
$$

Learning Module 6: Industry and Company Analysis

Herfindahl-Hirschman Index (HHI)

$$
H H I = \sum_ {i = 1} ^ {\infty} s _ {i} ^ {2}
$$

where:

$s_i =$  Market share of participant  $i$  (stated as a whole number)

Learning Module 7: Company Analysis: Forecasting

$$
\% \text{Variable cost} \approx \frac {\% \Delta (\text {Cost of revenue} + \text {Operating expense})}{\% \Delta \text {Revenue}}
$$

$$
\% \text {Fixed cost} \approx 1 - \% \text {Variable cost}
$$

$$
\begin{array}{c} N u m b e r o f u n i t s s o l d \\ p o s t - c a n n i b a l i z a t i o n \end{array} = \begin{array}{c} N u m b e r o f u n i t s s o l d \\ p r e - c a n n i b a l i z a t i o n \end{array} - \begin{array}{c} E x p e c t e d \\ c a n n i b a l i z a t i o n \end{array}
$$

$$
\begin{array}{c} \text {E x p e c t e d} \\ \text {c a n n i b a l i z a t i o n} \end{array} = \begin{array}{c} \text {N u m b e r o f u n i t s s o l d} \\ \text {p r e - c a n n i b a l i z a t i o n} \end{array} \times \begin{array}{c} \text {C a n n i b a l i z a t i o n} \\ \text {f a c t o r} \end{array}
$$

Learning Module 8: Equity Valuation: Concepts and Basic Tools

# Dividend Discount Model (DDM)

$$
V _ {0} = \sum_ {t = 1} ^ {n} \frac {D _ {t}}{(1 + r) ^ {t}} + \frac {P _ {n}}{(1 + r) ^ {n}}
$$

where:

$$
V _ {0} = \text {I n t r i n s i c v a l u e o f a s h a r e a t} t = 0
$$

$$
D _ {t} = \text {e x p e c t e d}
$$

$$
r = \text {r e q u i r e d}
$$

$$
P _ {n} = \text {e x p e c t e d p r i c e p e r s h a r e a t} t = n (\text {t e r m i n a l v a l u e})
$$

# Free-cash-flow-to-equity (FCFE) Valuation Model

$$
V _ {0} = \sum_ {t = 1} ^ {\infty} \frac {F C F E _ {t}}{(1 + r) ^ {t}}
$$

where:

$$
F C F E = C F O - F C I n v + N e t B o r r o w i n g
$$

$$
F C I n v = \text {F i x e d}
$$

$$
\text {N e t B o r r o w i n g} = \text {B o r r o w i n g s m i n u s r e p a y m e n t s}
$$

Value of preferred stock (non-callable, non-convertible, perpetual)

$$
V _ {0} = \frac {D _ {0}}{r}
$$

Value of preferred stock (non-callable, non-convertible, maturity at time  $n$ )

$$
V _ {0} = \sum_ {t = 1} ^ {n} \frac {D _ {t}}{(1 + r) ^ {t}} + \frac {\text {P a r v a l u e}}{(1 + r) ^ {n}}
$$

# Gordon Growth Model

$$
P _ {0} = \frac {D _ {1}}{r - g} = \frac {D _ {0} (1 + g)}{r - g}
$$

where:

$$
D _ {0} = \text {M o s t r e c e n t a n n u a l d i v i d e n d}
$$

$D_{1} =$  Expected dividend in the next period

$$
g = \text {C o n s t a n t g r o w t h r a t e}
$$

$$
r = \text {R e q u i r e d}
$$

# Sustainable growth rate

$$
g = b \times R O E
$$

where:

$$
b = \text {e a r n i n g s}
$$

$$
R O E = R e t u r n o n e q u i t y
$$

Video: https://youtu.be/MnfRRRhuGpA

# Two-Stage Dividend Discount Model

$$
V _ {0} = \sum_ {t = 1} ^ {n} \frac {D _ {0} (1 + g _ {s}) ^ {t}}{(1 + r) ^ {t}} + \frac {V _ {n}}{(1 + r) ^ {t}}
$$

where:

$$
g _ {L} = \text {L o n g - t e r m s t a b l e g r o w t h r a t e}
$$

$$
g _ {s} = \text {S h o r t - t e r m g r o w t h r a t e}
$$

$$
V _ {n} = \frac {D _ {n + 1}}{r - g _ {L}} = \frac {D _ {0} (1 + g _ {s}) ^ {t} (1 + g _ {L})}{r - g _ {L}}
$$

# Justified forward P/E

$$
\frac {P _ {0}}{E _ {1}} = \frac {\text {D i v i d e n d p a y o u t r a t i o}}{r - g}
$$

# Enterprise Value

$$
E V = \frac {\text {M a r k e t v a l u e}}{\text {o f e q u i t y}} + \frac {\text {M a r k e t v a l u e}}{\text {o f p r e f e r r e d s t o c k}} + \frac {\text {M a r k e t v a l u e}}{\text {o f d e b t}} - \frac {\text {C a s h a n d}}{\text {s h o r t t e r m}}
$$

# Asset-based Valuation

$$
\begin{array}{c} A d j u s t e d \\ b o o k v a l u e \end{array} = \begin{array}{c} M a r k e t v a l u e \\ o f a s s e t s \end{array} - \begin{array}{c} M a r k e t v a l u e \\ o f l i a b i l i t i e s \end{array}
$$

# VOLUME 6: FIXED INCOME

Learning Module 1: Fixed-Income Instrument Features

$$
C u r r e n t y i e l d = \frac {A n n u a l c o u p o n}{B o n d p r i c e}
$$

$$
B o n d p r i c e = \frac {C o u p o n}{(1 + r) ^ {1}} + \frac {C o u p o n}{(1 + r) ^ {2}} + \dots + \frac {C o u p o n + F a c e v a l u e}{(1 + r) ^ {n}}
$$

where:

$$
C o u p o n \text {p e r p e r i o d} = \text {C o u p o n r a t e p e r p e r i o d} \times \text {F a c e v a l u e}
$$

$$
r = \text {Y i e l d t o m a t u r i t y p e r p e r i o d}
$$

$$
n = \text {N u m b e r o f p a y m e n t s}
$$

Floating-rate Note (FRN) coupon rate  $= \text{MRR} + \text{Spread}$

Learning Module 2: Fixed-Income Cash Flows and Types

# Fully Amortizing Loan with Level Payment

$$
A = \frac {r \times P r i n c i p a l}{1 - (1 + r) ^ {- N}}
$$

where:

$$
A = \text {P e r i o d i c}
$$

$$
r = \text {M a r k e t i n t e r e s t r a t e p e r p e r i o d}
$$

$$
N = \text {N u m b e r o f p a y m e n t p e r i o d s}
$$

If the periodic payment is monthly:

Monthly interest payment = Interest rate per month  $\times$  Beginning principal of loan

Monthly principal payment = Total monthly payment - Monthly interest payment

Ending principal of loan = Beginning principal of loan – Monthly principal payment

# Capital-Index Bond (e.g., TIPS)

Inflation-adjusted principal = Principal amount  $\times$  (1 + Inflation adjustment)

Coupon per period  $=$  Coupon rate per period  $\times$  Inflation-adjusted principal

# Deferred Coupon Bond

Video: https://youtu.be/erRbAUOGlyM

# Convertible Bonds

$$
\frac {\text {C o n v e r s i o n}}{\text {r a t i o}} = \frac {\text {C o n v e r t i b l e b o n d p a r v a l u e}}{\text {C o n v e r s i o n p r i c e}}
$$

$$
\begin{array}{c} \text {C o n v e r s i o n} \\ \text {v a l u e} \end{array} = \begin{array}{c} \text {C o n v e r s i o n} \\ \text {r a t i o} \end{array} \times \begin{array}{c} \text {C u r r e n t s h a r e} \\ \text {p r i c e} \end{array}
$$

# Zero-Coupon Bond

Original issue discount  $=$  Bond par value - Issuance price

Learning Module 3: Fixed-Income Issuance and Trading

No formula

Learning Module 4: Fixed-Income Markets for Corporate Issuers

# Repurchase Agreements

$$
R e p u r c h a s e p r i c e = P r i c e o f b o n d \times \left[ 1 + R e p o r a t e \times \frac {R e p o t e r m (i n d a y s)}{N u m b e r o f d a y s i n a y e a r} \right]
$$

$$
I n i t i a l m a r g i n = \frac {S e c u r i t y p r i c e _ {0}}{P u r c h a s e p r i c e _ {0}}
$$

$$
H a i r c u t = \frac {S e c u r i t y p r i c e _ {0} - P u r c h a s e p r i c e _ {0}}{S e c u r i t y p r i c e _ {0}}
$$

$$
V a r i a t i o n \quad m a r g i n = (I n i t i a l \quad m a r g i n \times P u r c h a s e \quad p r i c e _ {t}) - S e c u r i t y \quad p r i c e _ {t}
$$

Learning Module 5: Fixed-Income Markets for Government Issuers

No formula.

Learning Module 6: Fixed-Income Bond Valuation: Prices and Yields

$$
P V = \frac {P M T _ {1}}{(1 + r) ^ {1}} + \frac {P M T _ {2}}{(1 + r) ^ {2}} + \dots + \frac {P M T _ {N} + F V _ {N}}{(1 + r) ^ {N}}
$$

where:

$PMT_{t} =$  Coupon that occurs in  $t$  periods

$r =$  Market discount rate per period

$N =$  Number of periods to maturity

$FV =$  Face value of bond

# Full Price, Flat Price, and Accrued Interest

(Video: https://youtu.be/l7G075JAu5w)

PVFull = PVFlat + Accrued Interest

$$
= P V _ {B O P} \times (1 + r) ^ {t / T}
$$

where:

Accrued Interest  $= \frac{t}{T} \times PMT$

$t =$  number of days from the last coupon payment to the settlement date

$T =$  number of days in the coupon period

$t / T =$  fraction of the coupon period that has gone by since the last payment

$PV_{BOP} = \text{price on the previous coupon date (before the settlement date)}$

# Matrix Pricing

$$
I n t e r p o l a t e d y i e l d = Y i e l d _ {S} + \left(\frac {T e n o r _ {T a r g e t} - T e n o r _ {S}}{T e n o r _ {L} - T e n o r _ {S}}\right) \times (Y i e l d _ {L} - Y i e l d _ {S})
$$

where:

Yield  $s =$  Yield of shorter-term bond

Yield  $L =$  Yield of longer-term bond

Tenor  $S =$  Tenor of shorter-term bond

Tenor $_{L}$  = Tenor of longer-term bond

Tenor  $_{Target} =$  Tenor of the subject bond

Tenor  $S <   T e n o r_{T a r g e t} <   T e n o r_{L}$

Required yield spread = Bond YTM - Government Bond YTM (Similar maturity)

Learning Module 7: Yield and Yield Spread Measures for Fixed Rate Bonds

# Periodicity Conversion

$$
\left(1 + \frac {A P R _ {m}}{m}\right) ^ {m} = \left(1 + \frac {A P R _ {n}}{n}\right) ^ {n}
$$

where:

$$
A P R _ {m} = \text {A n n u a l p e r c a n t e g a r e r a t e f o r m p e r i o d s p e r y e a r}
$$

$$
A P R _ {n} = \text {A n n u a l p e r t a g e r a t e f o r} n \text {p e r i o d s p e r y e a r}
$$

$$
C u r r e n t y i e l d _ {t} = \frac {\text {A n n u a l c o u p o n} _ {t}}{\text {B o n d p r i c e} _ {t}}
$$

$$
G o v e r n m e n t \quad \text {e q u i v a l e n t y i e l d}, \quad Y i e l d _ {A C T / A C T} = \frac {3 6 5}{3 6 0} \times Y i e l d _ {3 0 / 3 6 0}
$$

$$
S i m p l e y i e l d = \frac {C o u p o n + \left(\frac {F V - P V}{N}\right)}{F l a t p r i c e}
$$

# Callable Bonds

$$
P V = \frac {P M T}{(1 + Y T C) ^ {1}} + \frac {P M T}{(1 + Y T C) ^ {2}} + \dots + \frac {P M T + C a l l p r i c e}{(1 + Y T C) ^ {N}}
$$

where:

$$
P V = \text {P r i c e o f t h e c a l l a b e b o n d}
$$

$$
P M T = \text {C o u p o n}
$$

$$
Y T C = Y i e l d \text {t o}
$$

$$
N = \text {N u m b e r o f p e r i o d s t o w h e n t h e b o n d c a n b e c a l e d a t t h e c a l l p r i c e}
$$

$$
\text {O p t i o n - a d j u s t e d p r i c e} = \text {F l a t p r i c e o f b o n d} + \text {V a l u e o f e m b e d d e d c a l l o p t i o n}
$$

$$
\text {V a l u e o f c a l l o p t i o n} = \text {P r i c e o f o p t i o n - f r e e b o n d} - \text {P r i c e o f c a l l a b e b o n d}
$$

$$
G - s p r e a d = B o n d Y T M - I n t e r p o l a t e d s o v e r e i g h n b o u n d Y T M
$$

$$
I - s p r e a d = B o n d Y T M - S w a p r a t e
$$

# Z-Spread

$$
P V = \frac {P M T}{(1 + z _ {1} + Z) ^ {1}} + \frac {P M T}{(1 + z _ {2} + Z) ^ {2}} + \dots + \frac {P M T + F V}{(1 + z _ {N} + Z) ^ {N}}
$$

where:

$$
Z = Z \text {- s p r e a d}
$$

$$
z _ {N} = \text {S p o t r a t e f o r N p e r i o d s}
$$

$$
O A S = Z - s p r e a d - O p t i o n \text {v a l u e} (i n b a s i s p o i n t s p e r y e a r)
$$

Learning Module 8: Yield and Yield Spread Measures for Floating-Rate Instruments

# Value of Floating Rate Note (FRN)

$$
P V = \frac {\left(\frac {M R R + Q M}{m}\right) \times F V}{\left(1 + \frac {M R R + D M}{m}\right) ^ {1}} + \frac {\left(\frac {M R R + Q M}{m}\right) \times F V}{\left(1 + \frac {M R R + D M}{m}\right) ^ {2}} + \dots + \frac {\left(\frac {M R R + Q M}{m}\right) \times F V + F V}{\left(1 + \frac {M R R + D M}{m}\right) ^ {n}}
$$

where:

$$
Q M = \text {Q u o t e d}
$$

$$
D M = \text {D i s c o u n t}
$$

$$
M R R = \text {M a r k e t}
$$

$$
m = \text {P e r i o d i c i t y (i . e . , n u m b e r o f p a y m e n t p e r i o d s p e r y e a r)}
$$

$$
F V = \text {F a c e}
$$

$$
N = \text {N u m b e r o f e v e n l y s p a c e d p e r i o d s t o m a t u r i t y}
$$

Video: https://youtu.be/zqYOtVLkYR8

# Yield Measures for Money Market Instruments

# Discount Rate Basis

$$
P V = F V \times \left(1 - \frac {D a y s}{Y e a r} \times D R\right)
$$

$$
D R = \frac {Y e a r}{D a y s} \times \left(\frac {F V - P V}{F V}\right)
$$

where:

$PV =$  present value of money market instrument

$FV =$  future value paid at maturity

Days = number of days between settlement and maturity

Year = number of days in the year

$DR =$  discount rate (stated as annual percentage rate)

# Add-on Rate Basis

$$
P V = \frac {F V}{\left(1 + \frac {D a y s}{Y e a r} \times A O R\right)}
$$

$$
A O R = \frac {Y e a r}{D a y s} \times \left(\frac {F V - P V}{P V}\right)
$$

$$
B o n d e q u i v a l e n t y i e l d = \frac {3 6 5}{D a y s} \times \left(\frac {F V - P V}{P V}\right)
$$

Learning Module 9: The Term Structure of Interest Rates: Spot, Par, and Forward Curves

# Calculation of Bond Price Using Spot Rates

$$
P V = \frac {P M T}{(1 + Z _ {1}) ^ {1}} + \frac {P M T}{(1 + Z _ {2}) ^ {2}} + \dots + \frac {P M T + F V}{(1 + Z _ {N}) ^ {N}}
$$

where:

$PV =$  Price of bond

${PMT} =$  Bond coupon payment

$Z_{N} =$  Spot rate (or zero-coupon yield or zero rate) for period  $N$

$FV =$  Face value of bond

Given a Par Rate,  $FV = PV$  and  $PMT = Par$  Rate (\%) ×  $FV$

$$
1 0 0 = \frac {P M T}{(1 + Z _ {1}) ^ {1}} + \frac {P M T}{(1 + Z _ {2}) ^ {2}} + \dots + \frac {P M T + 1 0 0}{(1 + Z _ {N}) ^ {N}}
$$

# Forward Rates, IFR

$$
(1 + z _ {A}) ^ {A} \times (1 + I F R _ {A, B - A}) ^ {B - A} = (1 + z _ {B}) ^ {B}
$$

where:

$IFR_{A,B - A} =$  Forward rate for  $(B - A)$  periods that starts in period  $A$

![](images/fe109a281a5d0010dc4ee5bbb5f94dddfc1b54131b5c066922ff9851dd234e36.jpg)

Learning Module 10: Interest Rate Risk and Return

# Duration Gap

Duration gap = Macaulay duration - Investment horizon

# Macaulay Duration

$$
\begin{array}{l} M a c a u l a y d u r a t i o n = \left(1 - \frac {t}{T}\right) \left[ \frac {\frac {P M T}{(1 + r) ^ {1 - t / T}}}{P V ^ {F u l l}} \right] + \left(2 - \frac {t}{T}\right) \left[ \frac {\frac {P M T}{(1 + r) ^ {2 - t / T}}}{P V ^ {F u l l}} \right] + \dots \\ + \left(N - \frac {t}{T}\right) \left[ \frac {\frac {P M T + F V}{(1 + r) ^ {N - t / T}}}{P V ^ {F u l l}} \right] \\ \end{array}
$$

$$
M a c a u l a y d u r a t i o n = \left\{\frac {1 + r}{r} - \frac {1 + r + [ N \times (c - r) ]}{c \times [ (1 + r) ^ {N} - 1 ] + r} \right\} - \frac {t}{T}
$$

where:

$$
r = \text {Y i e l d p e r p e r i o d}
$$

$$
c = \text {C o u p o n r a t e p e r p e r i o d}
$$

$$
N = \text {N u m b e r o f e v e n l y s p a c e d p e r i o d s t o m a t u r i t y a s o f t h e b e g i n n i n g o f t h e c u r r e n t p e r i o d}
$$

$$
t = \text {N u m b e r o f d a y s f r o m t h e l a s t c o u p o n p a y m e n t t o t h e s e t t l e m e n t d a t e}
$$

$$
T = \text {N u m b e r o f d a y s i n t h e c o u p o n p e r i o d}
$$

Video: https://youtu.be/USgjcdCk7Fs

Learning Module 11: Yield-Based Bond Duration Measures and Properties

# Modified Duration

$$
M o d i f i e d D u r a t i o n = \frac {M a c a u l a y D u r a t i o n}{1 + r}
$$

# Approximate Modified Duration

$$
A n n M o d D u r \approx \frac {(P V _ {-}) - (P V _ {+})}{2 \times (\Delta Y i e l d) \times (P V _ {0})}
$$

$$
\% \Delta P V ^ {F u l l} \approx - A n n M o d D u r \times \Delta Y i e l d
$$

# Money Duration

$$
M o n e y d u r a t i o n = A n n M o d D u r \times P V ^ {f u l l}
$$

$$
\Delta P V ^ {F u l l} \approx - M o n e y D u r \times \Delta Y i e l d
$$

# Duration of Zero-Coupon Bond

$$
M a c D u r = T i m e t o m a t u r i t y
$$

$$
M o d D u r = \frac {T i m e t o m a t u r i t y}{1 + r}
$$

# Duration of Perpetual Bond

$$
M a c D u r = \frac {1 + r}{r}
$$

$$
M o d D u r = \frac {1}{r}
$$

# Duration of Floating-Rate Notes

$$
M a c D u r = \frac {T - t}{T} = \frac {F r a c t i o n o f p e r i o d r e m a i n i n g u n t i l}{t h e n e x t r e s e t d a t e}
$$

Learning Module 12: Yield-Based Bond Convexity and Portfolio Properties

# Convexity

$$
C o n v e x i t y = \sum_ {t = 1} ^ {N} \frac {t (t + 1) \times \frac {P V _ {t}}{P V ^ {F u l l}}}{(1 + Y T M) ^ {2}}
$$

# Approximate Annualized Convexity

$$
\text {A p p r o x C o n v} \approx \frac {\left(P V _ {-}\right) + \left(P V _ {+}\right) - 2 \left(P V _ {0}\right)}{\left(\Delta Y i e l d\right) ^ {2} \times \left(P V _ {0}\right)}
$$

$$
\% \Delta P V ^ {F u l l} \approx - A n n M o d D u r \times \Delta Y i e l d + \frac {1}{2} \times A n n C o n v e x i t y \times (\Delta Y i e l d) ^ {2}
$$

# Money Convexity

$$
M o n e y C o n = A n n C o n v e x i t y \times P V ^ {F u l l}
$$

$$
\Delta P V ^ {F u l l} \approx - (M o n e y D u r \times \Delta Y i e l d) + \left[ \frac {1}{2} \times M o n e y C o n \times (\Delta Y i e l d) ^ {2} \right]
$$

# Portfolio Duration and Convexity

$$
\text {P o r t f o l i o M o d i f i e d D u r a t i o n} = \sum_ {i = 1} ^ {N} w _ {i} \times \operatorname {M o d D u r} _ {i}
$$

$$
P o r t f o l i o C o n v e x i t y = \sum_ {i = 1} ^ {N} w _ {i} \times C o n v e x i t y _ {i}
$$

where:

$w_{i} =$  Weight of bond  $i$ , measured in market value

Learning Module 13: Curve-Based and Empirical Fixed-Income Risk Measures

# Effective Duration

$$
E f f D u r = \frac {(P V _ {-}) - (P V _ {+})}{2 \times (\Delta C u r v e) \times P V _ {0}}
$$

# Effective Convexity

$$
E f f C o n = \frac {(P V _ {-}) + (P V _ {+}) - 2 \times P V _ {0}}{(\Delta C u r v e) ^ {2} \times P V _ {0}}
$$

$$
\% \Delta P V ^ {F u l l} \approx - E f f D u r \times \Delta C u r v e + \frac {1}{2} \times E f f C o n \times (\Delta C u r v e) ^ {2}
$$

# Key Rate Duration

$$
K e y R a t e D u r _ {k} = - \frac {1}{P V} \times \frac {\Delta P V}{\Delta r _ {k}}
$$

$$
\% \Delta P V = - K e y R a t e D u r _ {k} \times \Delta r _ {k}
$$

$$
\sum_ {k = 1} ^ {n} \text {K e y R a t e D u r} _ {k} = E f f D u r
$$

where:

$r_k = k$ th key rate

Learning Module 14: Credit Risk

# Expected Loss

$$
E L = L G D \times P O D
$$

$$
L G D = E E \times (1 - R R)
$$

where:

$POD =$  Probability of default

$LGD =$  Loss given default

$EE =$  Expected exposure

$RR =$  Recovery rate

1 - RR = Loss severity

Credit spread  $\approx$  POD  $\times$  LGD

# Decomposing Bond Yields

Yield spread  $=$  Bond YTM - Government bond YTM (Similar maturity)

Liquidity spread  $=$  Bond YTM (Bid) - Bond YTM (Offer)

Credit spread  $=$  Yield spread - Liquidity spread

# Price Impact Given a Change in Yield Spread

$$
\% \Delta P V ^ {F u l l} \approx - A n n M o d D u r \times \Delta S p r e a d + \frac {1}{2} \times A n n C o n v e x i t y \times (\Delta S p r e a d) ^ {2}
$$

where:

$$
A n n M o d D u r \approx \frac {(P V _ {-}) - (P V _ {+})}{2 \times (\Delta Y i e l d) \times (P V _ {0})}
$$

$$
A n n C o n v e x i t y \approx \frac {(P V _ {-}) + (P V _ {+}) - 2 (P V _ {0})}{(\Delta Y i e l d) ^ {2} \times (P V _ {0})}
$$

Learning Module 15: Credit Analysis for Government Issuers

No formula.

Learning Module 16: Credit Analysis for Corporate Issuers

$$
E B I T m a r g i n = \frac {O p e r a t i n g i n c o m e}{R e v e n u e}
$$

$$
E B I T t o i n t e r e s t e x p e n s e = \frac {O p e r a t i n g i n c o m e}{I n t e r e s t e x p e n s e}
$$

$$
D e b t \text {t o} E B I T D A = \frac {D e b t}{E B I T D A}
$$

$$
R C F t o n e t d e b t = \frac {R e t a i n e d c a s h f l o w}{D e b t - C a s h a n d m a r k e t a b l e s e c u r i t i e s}
$$

$$
F F O t o d e b t = \frac {F F O}{D e b t}
$$

where:

[ FFO = \text{Net income from continuing operations} + \text{Depreciation & amortization} + \text{Deferred income taxes} + \text{Other non-cash items} ]

Learning Module 17: Fixed-Income Securitization

No formula.

Learning Module 18: Asset-Backed Security (ABS) Instrument and Market Features

No formula.

Learning Module 19: Mortgage-Backed Security (MBS) Instrument and Market Features

Loan-to-value (LTV) ratio

$$
L T V = \frac {L o a n a m o u n t}{H o u s e p r i c e}
$$

Debt-to-income (DTI) ratio

$$
D T I = \frac {M o n t h l y d e b t p a y m e n t}{M o n t h l y p r e - t a x g r o s s i n c o m e}
$$

# Mortgage Pass-Through Securities

$$
W A C = \sum_ {i = 1} ^ {N} c _ {i} \left(\frac {C B _ {i}}{C B}\right)
$$

$$
W A M = \sum_ {i = 1} ^ {N} M M _ {i} \left(\frac {C B _ {i}}{C B}\right)
$$

where:

$$
W A C = \text {W e i g h t e d a v e r a g e c o u p o n}
$$

$$
W A M = \text {W e i g h t e d a v e a r a g e m a t u r i t y}
$$

$$
c _ {i} = \text {C o u p o n r a t e o n m o r t g a g e} i
$$

$$
M M _ {i} = \text {N u m b e r o f m o n t h s t o m a t u r i t y f o r m o r g a t e} i
$$

$$
N = \text {N u m b e r o f m o r t g a g e s i n M B S}
$$

$$
C B _ {i} = \text {C u r r e n t b a l a n c e o n m o r t g a g e} i
$$

$$
C B = \text {T o t a l c u r r e n t b a l a n c e o f m o r g a g e s i n M B S}
$$

# Commercial Mortgage-Backed Securities (CMBS)

# Debt Service Coverage Ratio (DSCR)

$$
D S C R = \frac {N e t o p e r a t i n g i n c o m e}{D e b t s e r v i c e}
$$

# Net Operating Income (NOI)

NOI = (Rental income - Cash operating expenses) - Replacement reserves

# VOLUME 7: DERIVATIVES

Learning Module 1: Derivative Instrument and Derivatives Market Features

No formula.

Learning Module 2: Forward Commitments and Contingent Claim Features and Instruments

# Forward Contract

$$
\text {B u y e r (L o n g) p a y o f} = S _ {T} - F _ {0} (T)
$$

$$
\text {S e l l e r (S h o r t) p a y o f f} = - \left[ S _ {T} - F _ {0} (T) \right]
$$

where:

$$
S _ {T} = \text {S p o t p r i c e o n c h o n t r a c t}
$$

$$
F _ {0} (T) = \text {F o r w a r d p r i c e w i t h m a t u r i t y o f} T
$$

# Futures Contract

For one futures contract:

$$
\text {L o n g F u t u r e s d a i l y m a r k - t o - m a r k e t} = f _ {t} (T) - f _ {t - 1} (T)
$$

$$
\text {S h o r t F u t u r e s d a l l y m a r k - t o - m a r k e t} = - \left[ f _ {t} (T) - f _ {t - 1} (T) \right]
$$

where:

$$
f _ {t} (T) = \text {C l o s i n g p r i c e o f f u t u r e s c h o r t a c t o n d a y} t
$$

$$
f _ {t - 1} (T) = \text {C l o s i n g p r i c e o f f u t u r e s c h i r c a t o n d a y} t - 1
$$

$$
T = \text {M a t u r i t y o f f u t u r e s c h o n t r a c t}
$$

If margin balance  $<$  maintenance margin:

$$
V a r i a t i o n M a r g i n = I n i t i a l m a r g i n - M a r g i n b a l a n c e
$$

# Options Contract

# LONG Call option

Payoff or Value at expiration,  $c_{T} = \max (0,S_{T} - X)$

Profit at expiration,  $\Pi = \max (0,S_T - X) - c_0$

where:

$$
c _ {0} = \text {C a l l p r e m i u m}
$$

$$
X = \text {E x e r c i s e} / \text {S t r i k e p r i c e}
$$

$$
S _ {T} = \text {S p o t p r i c e a t}
$$

# SHORT Call option

Payoff or Value at expiration,  $c_{T} = -\max (0,S_{T} - X)$

Profit at expiration,  $\Pi = -[\max (0,S_T - X) - c_0]$

# LONG Put option

Payoff or Value at expiration,  $p_T = \max(0, X - S_T)$

Profit at expiration,  $\Pi = \max (0,X - S_T) - p_0$

# SHORT Put option

Payoff or Value at expiration,  $p_T = -\max(0, X - S_T)$

Profit at expiration,  $\Pi = -[\max (0,X - S_T) - p_0]$

# Credit Default Swap (CDS)

CDS MTM Change = ΔCDS Spread × CDS Notional × EffDur<sub>CDS</sub>

In a credit event, payment from CDS seller to CDS buyer  $\approx LGD(\%)\times$  Notional

Learning Module 3: Derivative Benefits, Risks, and Issuer and Investor Uses

No formula.

# Learning Module 4: Arbitrage, Replication, and the Cost of Carry in Pricing Derivatives

If there are no underlying costs or benefits:

$$
F o r w a r d p r i c e, F _ {0} (T) = S _ {0} (1 + r) ^ {T}
$$

If there are underlying costs or benefits in present value terms:

$$
\text {F o r w a r d p r i c e}, F _ {0} (T) = \left[ S _ {0} - P V _ {0} (\text {I n c o m e}) + P V _ {0} (\text {C o s t}) \right] (1 + r) ^ {T}
$$

where:

$$
S _ {0} = \text {C u r r e n t s p o t p r i c e}
$$

$$
r = \text {R i s k - f r e e}
$$

$$
T = \text {T e n o r}
$$

Under continuous compounding,  $F_{0}(T) = S_{0}e^{rT}$

Under continuous compounding, with income  $(i)$  and cost  $(c)$  expressed in  $\%$

$$
F _ {0} (T) = S _ {0} e ^ {(r + c - i) T}
$$

# Foreign Exchange Forward Contract

$$
F _ {0, f / d} (T) = S _ {0, f / d} (T) e ^ {(r _ {f} - r _ {d}) T}
$$

where:

$$
F _ {0, f / d} = \text {F o r w a r d e x c h a n g e r a t e}
$$

$$
S _ {0, f / d} = \text {S p o t e x c h a n g e r a t e}
$$

$$
r _ {f} = \text {C o n t i n u o u s l y c o m p o u n d e d r i s k - f r e e r a t e (f o r p r i c e / q u o t e c u r r e n c y)}
$$

$$
r _ {d} = \text {C o n t i n u o u s l y c o m p o u n d e d r i s k - f r e e r a t e (f o r b a s e c u r r e n c y)}
$$

$$
T = \text {M a t u r i t y o f f o r w a r d c h a r t}
$$

Learning Module 5: Pricing and Valuation of Forward Contracts and for an Underlying with Varying Maturities

# Value of LONG Forward Prior to Expiration

$$
V _ {0} (T) = 0
$$

$$
V _ {t} (T) = S _ {t} - \frac {F _ {0} (T)}{(1 + r) ^ {T - t}} = S _ {t} - F _ {0} (T) \times (1 + r) ^ {- (T - t)}
$$

$$
V _ {T} (T) = S _ {0} - F _ {0} (T)
$$

If the asset incurs cost or generates income from time  $t$  through maturity,

$$
V _ {t} (T) = [ S _ {t} - P V _ {t} (I n c o m e) + P V _ {t} (C o s t) ] - F _ {0} (T) \times (1 + r) ^ {- (T - t)}
$$

For foreign exchange forward contract,

$$
V _ {t} (T) = S _ {t, f / d} - F _ {0, f / d} (T) \times e ^ {- (r _ {f} - r _ {d}) (T - t)}
$$

Value of SHORT Forward Prior to Expiration

$$
V _ {0} (T) = 0
$$

$$
V _ {t} (T) = - \left[ S _ {t} - \frac {F _ {0} (T)}{(1 + r) ^ {T - t}} \right]
$$

$$
V _ {T} (T) = - [ S _ {0} - F _ {0} (T) ]
$$

Interest Rate Forward Contracts (Forward Rate Agreements (FRA))

$$
(1 + z _ {A}) ^ {A} \times (1 + I F R _ {A, B - A}) ^ {B - A} = (1 + z _ {B}) ^ {B}
$$

where:

$z_A =$  Spot rate for  $A$  periods

$z_{B} =$  Spot rate for  $B$  periods

$IFR_{A,B-A} =$  Implied forward rate for  $(B - A)$  periods, starting in  $A$  periods

Payoff for a Long FRA =  $(MRR_{B - A} - IFR_{A,B - A})\times$  Notional principal  $\times$  Period

Payoff for a Short FRA  $= -\left(MRR_{B-A} - IFR_{A,B-A}\right) \times$  Notional principal  $\times$  Period

Learning Module 6: Pricing and Valuation of Futures Contracts

If there are no underlying costs or benefits:

$$
\text {F u t u r e s p r i c e ,} f _ {0} (T) = S _ {0} (1 + r) ^ {T}
$$

If there are underlying costs or benefits in present value terms:

$$
f _ {0} (T) = [ S _ {0} - P V _ {0} (I n c o m e) + P V _ {0} (C o s t) ] (1 + r) ^ {T}
$$

Under continuous compounding,  $f_{0}(T) = S_{0}e^{rT}$

Under continuous compounding, with income  $(i)$  and cost  $(c)$  expressed in  $\%$  ..

$$
f _ {0} (T) = S _ {0} e ^ {(r + c - i) T}
$$

# Foreign Exchange Forward Contract

$$
f _ {0, f / d} (T) = S _ {0, f / d} (T) e ^ {(r _ {f} - r _ {d}) T}
$$

# Interest Rate Futures Contract

$$
f _ {A, B - A} = 1 0 0 - \left(1 0 0 \times M R R _ {A, B - A}\right)
$$

where:

$$
f _ {A, B - A} = \text {F u t u r e s p r i c e f o r a m a r k e t r e f e r e n c e r a t e r e f o r (B - A) p e r i o d s}
$$

Futures contract basis point value,  $BPV =$  Notional principal  $\times 0.01\% \times$  Period

Learning Module 7: Pricing and Valuation of Interest Rates and Other Swaps

For a fixed-rate payer in an interest rate swap:

$$
\text {P e r i o d i c s e t t l e m e n t v a l u e} = \left(M R R - s _ {N}\right) \times \text {S w a p N o t i o n a l} \times \text {P e r i o d}
$$

For a fixed-rate receiver in an interest rate swap:

$$
\text {P e r i o d i c s e t t l e m e n t v a l u e} = \left(s _ {N} - M R R\right) \times \text {S w a p N o t i o n a l} \times \text {P e r i o d}
$$

where:

$$
s _ {N} = \text {F i x e d s w a p r a t e}
$$

$$
M R R = \text {M a r k e t}
$$

# Calculating Par Swap Rate

$$
\sum_ {i = 1} ^ {N} \frac {I F R}{(1 + z _ {i}) ^ {i}} = \sum_ {i = 1} ^ {N} \frac {s _ {N}}{(1 + z _ {i}) ^ {i}}
$$

where:

$$
I F R = \text {I m p l i e d f o r w a r d r a t e s}
$$

$$
S _ {N} = \text {F i x e d s w a p r a t e}
$$

$$
N = \text {T e n o r}
$$

# Valuation of Interest Rate Swap

Value of a pay-fixed interest rate swap on a settlement date after inception

$$
= \underset {v a l u e} {C u r r e n t s e t t l e m e n t} + \Sigma (F l o a t i n g p a y m e n t s) - \Sigma (F i x e d p a y m e n t s)
$$

Value of a receive-fixed interest rate swap on a settlement date after inception

$$
= \underset {v a l u e} {C u r r e n t s e t t l e m e n t} + \Sigma (F i x e d p a y m e n t s) - \Sigma (F l o a t i n g p a y m e n t s)
$$

Learning Module 8: Pricing and Valuation of Options

$$
\text {O p t i o n v a l u e} = \text {E x e c i s e v a l u e} + \text {T i m e v a l u e}
$$

At time  $t$  (prior to option expiration):

$$
C a l l o p t i o n e x e r c i s e v a l u e = M a x \bigl [ 0, S _ {t} - X (1 + r) ^ {- (T - t)} \bigr ]
$$

$$
C a l l o p t i o n t i m e v a l u e = c _ {t} - M a x \bigl [ 0, S _ {t} - X (1 + r) ^ {- (T - t)} \bigr ]
$$

$$
P u t o p t i o n e x e r c i s e v a l u e = M a x \bigl [ 0, X (1 + r) ^ {- (T - t)} - S _ {t} \bigr ]
$$

$$
P u t o p t i o n t i m e v a l u e = p _ {t} - M a x \bigl [ 0, X (1 + r) ^ {- (T - t)} - S _ {t} \bigr ]
$$

$$
\text {L o w e r b o u n d o f c a l l o p t i o n v a l u e} = M a x \left[ 0, S _ {t} - X (1 + r) ^ {- (T - t)} \right]
$$

$$
\text {U p p e r b o u n d o f c a l l o p t i o n v a l u e} = S _ {t}
$$

$$
\text {L o w e r b o u n d o f p u t o p t i o n v a l u e} = M a x \left[ 0, X (1 + r) ^ {- (T - t)} - S _ {t} \right]
$$

$$
\text {U p p e r b o u n d o f p u t o p t i o n v a l u e} = X
$$

where:

$$
S _ {t} = \text {S p o t p r i c e a t t i m e} t
$$

$$
X = \text {E x e r c i s e p r i c e (o r s t r i k e p r i c e)}
$$

$$
T = \text {M a t u r i t y o f}
$$

$$
r = \text {R i s k - f r e e}
$$

Learning Module 9: Option Replication Using Put-Call Parity

# Put-Call Parity

$$
S _ {0} + p _ {0} = c _ {0} + X (1 + r) ^ {- T}
$$

# Put-Call Forward Parity

$$
F _ {0} (T) (1 + r) ^ {- T} + p _ {0} = c _ {0} + X (1 + r) ^ {- T}
$$

# Value of the Firm

$$
V _ {0} = c _ {0} + P V (D e b t) - p _ {0}
$$

Value of debt  $= PV(Debt) - p_{0}$

Value of equity  $= c_{0}$

Learning Module 10: Valuing a Derivative Using a One-Period Binomial Model

Risk-neutral probability of a price increase in underlying

$$
\pi = \frac {1 + r - R ^ {d}}{R ^ {u} - R ^ {d}}
$$

where:

$$
R ^ {u} = U p f a c t o r = \frac {S _ {1} ^ {u}}{S _ {0}} > 1
$$

$$
R ^ {d} = D o w n f a c t o r = \frac {S _ {1} ^ {d}}{S _ {0}} <   1
$$

$$
S _ {0} = \text {C u r r e n t a s s e t p r i c e}
$$

$$
S _ {1} ^ {u} = \text {O n e - p e r i o d a s s e t p r i c e w h e n p r i c e m o v e s u p}
$$

$$
S _ {1} ^ {d} = \text {O n e - p e r i o d a s s e t p r i c e w h e n p r i c e m o v e s d o w n}
$$

Video: https://youtu.be/ymUkgz-rAw

# Hedge ratio

$$
h ^ {*} = \frac {c _ {1} ^ {u} - c _ {1} ^ {d}}{S _ {1} ^ {u} - S _ {1} ^ {d}}
$$

where:

$$
c _ {1} ^ {u} = \max  (0, S _ {1} ^ {u} - X)
$$

$$
c _ {1} ^ {d} = \max  \left(0, S _ {1} ^ {d} - X\right)
$$

Riskless portfolio with a Call:  $h$  of the underlying,  $S$ , and short call position,  $c$

$$
V _ {0} = h S _ {0} - c _ {0}
$$

$$
V _ {1} ^ {u} = h S _ {1} ^ {u} - c _ {1} ^ {u}
$$

$$
V _ {1} ^ {d} = h S _ {1} ^ {d} - c _ {1} ^ {d}
$$

Riskless portfolio with a Put:  $h$  of the underlying,  $S$ , and long put position,  $p$

$$
V _ {0} = h S _ {0} + p _ {0}
$$

$$
V _ {1} ^ {u} = h S _ {1} ^ {u} + p _ {1} ^ {u}
$$

$$
V _ {1} ^ {d} = h S _ {1} ^ {d} + p _ {1} ^ {d}
$$

# Value of a one-period call option

$$
c _ {0} = \frac {\pi c _ {1} ^ {u} + (1 - \pi) c _ {1} ^ {d}}{1 + r}
$$

# Value of a one-period put option

$$
p _ {0} = \frac {\pi p _ {1} ^ {u} + (1 - \pi) p _ {1} ^ {d}}{1 + r}
$$

where:

$$
p _ {1} ^ {u} = \max  (0, X - S _ {1} ^ {u})
$$

$$
p _ {1} ^ {d} = \max  \left(0, X - S _ {1} ^ {d}\right)
$$

Video: https://youtu.be/bXEC-78v_AU

# VOLUME 8: ALTERNATIVE INVESTMENTS

Learning Module 1: Alternative Investment Features, Methods, and Structures

# GP Compensation Structure

Ignoring management fee; no catch-up clause

$$
r _ {G P} = \max [ 0, p (r - r _ {h}) ]
$$

Ignoring management fee; with catch-up clause

$$
r _ {G P} = \max [ 0, r _ {c u} + p (r - r _ {h} - r _ {c u}) ]
$$

where:

$$
r _ {G P} = G P ^ {\prime} s \text {r a t e o f r e t u r n}
$$

$$
p = \text {P e r f o r m a n c e f e e a s a p e r t e n g a t e o f t o t a l r e t u r n}
$$

$$
r = \text {S i n g l e - p e r i o d r a t e o f r e t u r n}
$$

$$
r _ {h} = \text {H a r d h u r d l e r a t e}
$$

$$
r _ {c u} = \text {C a t c h - u p c l a u s e}
$$

Learning Module 2: Alternative Investment Performance and Returns

# Multiple on Invested Capital

$$
M O I C = \frac {\text {R e a l i z e d v a l u e o f i n v e s t m e n t} + \text {U n r e a l i z e d v a l u e o f i n v e s t m e n t}}{\text {T o t a l a m o u n t o f i n v e s t e d c a p i t a l}}
$$

# Leveraged Portfolio Return

$$
r _ {L} = r + \frac {V _ {b}}{V _ {c}} (r - r _ {b})
$$

where:

$$
r = \text {P e r i o d i c}
$$

$$
r _ {b} = \text {P e r i o d i c}
$$

$$
V _ {b} = \text {A m o u n t o f b o r r o w e d f u n d s}
$$

$$
V _ {c} = \text {A m o u n t o f c a s h (i n v e s t o r ' s o w n c a p i t a l)}
$$

# Investor's Return Net of Fees

$$
r _ {i} = \frac {P _ {1} - P _ {0} - R _ {G P}}{P _ {0}}
$$

$$
R _ {G P} = (P _ {1} \times r _ {m}) + \max [ 0, (P _ {1} - P _ {0}) \times p ]
$$

where:

$P_0 =$  Beginning-of-period asset value

$P_{1} =$  End-of-period asset value

$p = \mathrm{GP}$  performance fee

$R_{GP} = \mathbf{GP}'$  s return in current terms

$r_m = \mathsf{GP}'s$  management fees as a percentage of assets under management

# Calculating Hedge Fund Fees and Returns

Management Fee Based on Beginning Market Value

$$
\begin{array}{c} \text {M a n a g e m e n t} \\ F e e \end{array} = \frac {\% M a n a g e m e n t}{F e e} \times \begin{array}{c} \text {B e g i n n i n g M a r k e t} \\ V a l u e \end{array}
$$

Management Fee Based on Ending Market Value

$$
\begin{array}{c} \text {M a n a g e m e n t} \\ F e e \end{array} = \frac {\% M a n a g e m e n t}{F e e} \times \begin{array}{c} E n d i n g M a r k e t \\ V a l u e \end{array}
$$

Incentive Fee Calculated Independent of Management Fee

$$
\begin{array}{c} \text {Incentive} \\ F e e \end{array} = \begin{array}{c} \% \text {Incentive} \\ F e e \end{array} \times G a i n
$$

Incentive Fee Calculated Net of Management Fee

$$
\frac {\text {Incentive}}{\text {Fee}} = \frac {\% \text {Incentive}}{\text {Fee}} \times (\text {Gain} - \text {Management Fee})
$$

Incentive Fee with Hard Hurdle (Independent of Management Fee)

$$
\begin{array}{c} \text {Incentive} \\ F e e \end{array} = \begin{array}{c} \% \text {Incentive} \\ F e e \end{array} \times (G a i n - H u r d l e)
$$

Incentive Fee with Hard Hurdle (Net of Management Fee)

$$
\frac {\text {Incentive}}{\text {Fee}} = \frac {\% \text {Incentive}}{\text {Fee}} \times (\text {Gain} - \text {Management Fee} - \text {Hurdle})
$$

$$
H u r d l e = H u r d l e \quad R a t e \times B e g i n n i n g \quad m a k e t \quad v a l u e
$$

Note: 1) No incentive is paid if hedge fund incurs loss for the year.

2) Gain may be subject to high watermark.

Video: https://youtu.be/0DKmCgsAAdc

Learning Module 3: Investments in Private Capital: Equity and Debt

No formula.

Learning Module 4: Real Estate and Infrastructure

Loan-to-Value (LTV) Ratio

$$
L T V = \frac {M o r t g a g e l i a b i l i t y}{P o r t f o l i o v a l u e}
$$

Required reduction in mortgage liability = Mortgage liability – Required mortgage liability

Learning Module 5: Natural Resources

No formula.

Learning Module 6: Hedge Funds

No formula.

Learning Module 7: Introduction to Digital Assets

No formula.

# VOLUME 9: PORTFOLIO MANAGEMENT

Learning Module 1: Portfolio Risk and Return: Part I

# Expected Return on Asset

$$
1 + E (R) = \left(1 + r _ {r F}\right) \times \left[ 1 + E (\pi) \right] \times \left[ 1 + E (R P) \right]
$$

where:

$$
r _ {r F} = \text {R e a l}
$$

$$
E (\pi) = \text {E x p e c t e d i n f l a t i o n}
$$

$$
E (R P) = \text {E x p e c t e d}
$$

# Utility on Investment

$$
U = E (R) - \frac {1}{2} A \sigma^ {2}
$$

where:

$$
U = \text {U t i l i t y}
$$

$$
E (R) = \text {E x p e c t e d}
$$

$$
A = \text {R i s k a v e r s i o n c o e f f i c i e n t}
$$

$$
\sigma^ {2} = \text {V a r i a n c e o f i n v e s t m e n t (N o t e : S u b s t i t u t e} \sigma \text {i n d e c i m a l s)}
$$

# Capital Allocation Line (CAL)

For a portfolio of risky assets (Weight:  $w_{i}$ ) and risk-free asset:

$$
E \big (R _ {p} \big) = R _ {f} + \left[ \frac {E (R _ {i}) - R _ {f}}{\sigma_ {i}} \right] \sigma_ {p}
$$

where:

$$
R _ {f} = \text {R a t e o f r e t u r n o n r i s k - f r e e a s s e t}
$$

$$
E \left(R _ {i}\right) = \text {E x p e c t e d}
$$

$$
E \left(R _ {p}\right) = \text {E x p e c t e d}
$$

$$
\sigma_ {i} = \text {S t a n d a r d}
$$

$$
\sigma_ {p} = \text {S t a n d a r d} \sigma_ {i}
$$

$$
\frac {E (R _ {i}) - R _ {f}}{\sigma_ {i}} = M a r k e t p r i c e o f r i s k
$$

# Two-asset portfolio

Portfolio expected return,  $E\left( {R}_{p}\right)  = {w}_{1}{R}_{1} + {w}_{2}{R}_{2}$

Portfolio variance,  $\sigma_p^2 = w_1^2\sigma_1^2 +w_2^2\sigma_2^2 +2w_1w_2Cov(R_1,R_2)$

Portfolio standard deviation,  $\sigma_{p} = \sqrt{w_{1}^{2}\sigma_{1}^{2} + w_{2}^{2}\sigma_{2}^{2} + 2w_{1}w_{2}Cov(R_{1},R_{2})}$

Note: 1)  $\text{Cov}(R_1, R_2) = \rho_{12}\sigma_1\sigma_2$  
2)  $n$  securities requires  $n$  variances and  $\frac{n(n - 1)}{2}$  covariances

Video: https://youtu.be/luwulZ9ONCO

# Foreign Asset

Return of a foreign asset in domestic currency

$$
R _ {D} = (1 + R _ {l c}) \times (1 + R _ {F X}) - 1
$$

Standard deviation of return of a foreign asset in domestic currency

$$
\sigma_ {D} = \sqrt {\sigma_ {l c} ^ {2} + \sigma_ {F X} ^ {2} + 2 \times \rho \times \sigma_ {l c} \times \sigma_ {F X}}
$$

where:

$R_{lc} =$  Return of foreign asset (in local currency)

$R_{FX} =$  Change in exchange rate (FX rate quoted as domestic currency/foreign currency)

$\sigma_{lc} =$  Standard deviation of foreign asset's returns

$\sigma_{FX} =$  Standard deviation of the exchange rate (DC/FC)

$\rho =$  Correlation coefficient between returns on foreign asset and exchange rate

# Portfolio of Many Risky Assets

$$
\sigma_ {p} ^ {2} = \frac {\bar {\sigma} ^ {2}}{N} + \frac {N - 1}{N} \overline {{C o v}} = \frac {\bar {\sigma} ^ {2}}{N} + \frac {N - 1}{N} \rho \bar {\sigma} ^ {2}
$$

where:

$N =$  Number of assets in portfolio

$\bar{\sigma}^2 = \text{Average variance}$

$\overline{Cov} =$  Average covariance

# Capital Market Line (CML)

$$
E \big (R _ {p} \big) = w _ {f} R _ {f} + (1 - w _ {f}) E (R _ {m}) = R _ {f} + \left[ \frac {E (R _ {m}) - R _ {f}}{\sigma_ {m}} \right] \sigma_ {p}
$$

$$
\sigma_ {p} = (1 - w _ {f}) \sigma_ {m}
$$

# Return-Generating Models

$$
E (R _ {i}) - R _ {f} = \beta_ {i 1} \big [ E (R _ {m}) - R _ {f} \big ] + \sum_ {j = 2} ^ {k} \beta_ {i j} E \big (F _ {j} \big)
$$

where:

$$
E \left(R _ {i}\right) - R _ {f} = \text {E x p e c t e d}
$$

$$
k = \text {N u m b e r o f f a c t o r s}
$$

$$
\beta_ {i j} = \text {F a c t o r w e i g h t s (a l s o c a l l e d f a c t o r l o a d i n g s)}
$$

$$
E \left(R _ {m}\right) = \text {E x p e c t e d}
$$

# The Single-Index Model

$$
E (R _ {i}) - R _ {f} = \left(\frac {\sigma_ {i}}{\sigma_ {m}}\right) \left[ E (R _ {m}) - R _ {f} \right]
$$

where:

$$
\frac {\sigma_ {i}}{\sigma_ {m}} = F a c t o r l o a d i n g (o r f a c t o r w e i g h t)
$$

# Capital Asset Pricing Model

$$
E (R _ {i}) = R _ {f} + \beta_ {i} \big [ E (R _ {m}) - R _ {f} \big ]
$$

# The Market Model

$$
R _ {i} = \alpha_ {i} + \beta_ {i} R _ {m} + e _ {i}
$$

# Beta of security  $i$

$$
\beta_ {i} = \frac {C o v (R _ {i} , R _ {m})}{\sigma_ {m} ^ {2}} = \frac {\rho_ {i , m} \sigma_ {i}}{\sigma_ {m}}
$$

Portfolio beta,  $\beta_{p} = \sum_{i=1}^{n} w_{i} \beta_{i}$

Total variance  $=$  Systematic variance + Nonsystematic variance

$$
\sigma_ {i} ^ {2} = \beta_ {i} ^ {2} \sigma_ {m} ^ {2} + \sigma_ {e} ^ {2}
$$

Total risk,  $\sigma_{i} = \sqrt{\beta_{i}^{2}\sigma_{m}^{2} + \sigma_{e}^{2}}$

# Arbitrage Pricing Theory (APT) Model

$$
E (R _ {P}) = R _ {F} + \lambda_ {1} \beta_ {P, 1} + \dots + \lambda_ {K} \beta_ {P, K}
$$

where:

$$
E \left(R _ {P}\right) = \text {E x p e c t e d}
$$

$$
R _ {F} = \text {R i s k - f r e e r a t e}
$$

$$
\lambda_ {j} = \text {R i s k p r e m i u m f o r f a c t o r} j
$$

$$
\beta_ {P, 1} = \text {S e n s i t i v i t y o f t h e p o r t f o l i o t o f a c t o r} j
$$

$$
K = \text {N u m b e r o f r i s k f a c t o r s}
$$

# Fama-French Model

$$
E (R _ {i t}) = \alpha_ {i} + \beta_ {i, M K T} M K T _ {t} + \beta_ {i, S M B} S M B _ {t} + \beta_ {i, H M L} H M L _ {t}
$$

# Carhart Model

$$
E (R _ {i t}) = \alpha_ {i} + \beta_ {i, M K T} M K T _ {t} + \beta_ {i, S M B} S M B _ {t} + \beta_ {i, H M L} H M L _ {t} + \beta_ {i, U M D} U M D _ {t}
$$

where:

$$
E \left(R _ {i}\right) = \text {R e t u r n}
$$

$$
M K T = \text {E x c e s s}
$$

$$
\begin{array}{l} S M B = \text {D i f f e r e n c e i n r e t u r n s b e t w e e n s m a l l - c a p i t a l i z a t i o n s t o c k s a n d l a r g e - c a p i t a l i z a t i o n} \\ \text {s t o c k s (S i z e)} \end{array}
$$

$$
H M L = \text {D i f f e r e n c e i n r e t u r n s b e t w e e n h i g h - b o o k - t o - m a r k e t s t o c k s a n d l o w - b o o k - t o - m a r k e t}
$$

$$
U M D = \text {D i f f e r e n c e}
$$

# Portfolio Performance Appraisal Measures

$$
\mathrm {S h a r p e r a t i o} = \frac {R _ {p} - R _ {f}}{\sigma_ {p}}
$$

$$
\mathrm {T r e y n o r r a t i o} = \frac {R _ {p} - R _ {f}}{\beta_ {p}}
$$

$$
M ^ {2} = \left(R _ {p} - R _ {f}\right) \frac {\sigma_ {m}}{\sigma_ {p}} + R _ {f} = S h a r p e r a t i o \times \sigma_ {m} + R _ {f}
$$

$$
M ^ {2} a l p h a = M ^ {2} - R _ {m}
$$

$$
\mathrm {J e n s e n ' s A l p h a}, \alpha_ {p} = R _ {p} - \left[ R _ {f} + \beta_ {p} \big (R _ {m} - R _ {f} \big) \right]
$$

# Security Characteristic Line (SCL)

$$
R _ {i} - R _ {f} = \alpha_ {i} + \beta_ {i} \big (R _ {m} - R _ {f} \big)
$$

Information ratio = αi / σei

Learning Module 3: Portfolio Management: An Overview

No formula.

Learning Module 4: Basics of Portfolio Planning and Construction

No formula.

Learning Module 5: The Behavioral Biases of Individuals

No formula.

Learning Module 6: Introduction to Risk Management

No formula.

![](images/15939805a604fb7f8605144de14b46f212b9c891679915ce8ba4d8fe2aaf5ef5.jpg)

# oesis

# CFA® Program

# Level II

# FORMULA SHEET (2025) Version 1.0

Prepared by: Fabian Moa, CFA, FRM, CTP, FMVA, AFM, FSA Credential

![](images/0ceb270522c1177fe6c794e5ac0b3e1fe2651192dcc5abb3b317aa8c0be9ec7d.jpg)

# FOR REFERENCE ONLY

# (Note: Formula Sheet is not provided in the CFA exam)

Follow us on:

YouTube

LinkedIn

Facebook

Instagram

# NOESIS EXED SDN BHD

Block VO2, Level 5, Unit 8, Lingkaran SV, Sunway Velocity, 55100 Kuala Lumpur, Malaysia

Website: www.noesis.edu.sg

CFA Institute does not endorse, promote, or warrant the accuracy or quality of the products or services offered by Noesis

Exed. CFA Institute, CFA® and Chartered Financial Analyst® are trademarks owned by CFA Institute.

# Contents

Setting Up the Texas BA II Plus Financial Calculator 4  
VOLUME 1: QUANTITATIVE METHODS 4  
Learning Module 1 | Basics of Multiple Regression and Underlying Assumptions. 4  
Learning Module 2 | Evaluating Regression Model Fit and Interpreting Model Results 4  
Learning Module 3 | Model Misspecification. 6  
Learning Module 4 | Extensions of Multiple Regression. 6  
Learning Module 5 | Time-Series Analysis. 7  
Learning Module 6 | Machine Learning. 8  
Learning Module 7 | Big Data Projects 9  
VOLUME 2: ECONOMICS 10  
Learning Module 1 | Currency Exchange Rates: Understanding Equilibrium Value 10  
Learning Module 2 | Economic Growth and the Investment Decision 12  
VOLUME 3: FINANCIAL STATEMENT ANALYSIS. 14  
Learning Module 1 | Intercorporate Investments. 14  
Learning Module 2 | Employee Compensation - Post-Employment and Share-Based 15  
Learning Module 3 | Multinational Operations. 16  
Learning Module 4 | Analysis of Financial Institutions. 17  
Learning Module 5 | Evaluating Quality of Financial Reports 18  
Learning Module 6 | Integration of Financial Statement Analysis Techniques. 18  
VOLUME 4: CORPORATE ISSUERS 19  
Learning Module 1 | Analysis of Dividends and Share Repurchases. 19  
Learning Module 3 | Cost of Capital: Advanced Topics 20  
Learning Module 4 | Corporate Restructuring 23  
VOLUME 5: EQUITY VALUATION 24  
Learning Module 1 | Equity Valuation Applications and Processes 24  
Learning Module 2 | Discounted Dividend Valuation 24  
Learning Module 3 | Free Cash Flow Valuation. 25  
Learning Module 4 | Market-Based Valuation Price and Enterprise Value Multiples. 27  
Learning Module 5 | Residual Income Valuation 29  
Learning Module 6 | Private Company Valuation 30  
VOLUME 6: FIXED INCOME 32  
Learning Module 1 | The Term Structure and Interest Rate Dynamics. 32  
Learning Module 2 | The Arbitrage-Free Valuation Framework 33  
Learning Module 3 | Valuation and Analysis - Bonds with Embedded Options. 34  
Learning Module 4 | Credit Analysis Models. 36

Learning Module 5 | Credit Default Swaps 37

VOLUME 7: DERIVATIVES 38  
Learning Module 1 | Pricing and Valuation of Forward Commitments 38  
Learning Module 2 | Valuation of Contingent Claims 42  
VOLUME 8: ALTERNATIVE INVESTMENTS 46  
Learning Module 1 | Introduction to Commodities and Commodity Derivatives. 46  
Learning Module 2 | Overview of Types of Real Estate Investment 46  
Learning Module 3 | Investments in Real Estate Through Publicly Traded Securities 48  
Learning Module 4 | Hedge Fund Strategies 49  
VOLUME 9: PORTFOLIO MANAGEMENT 50  
Learning Module 1 | Economics and Investment Markets. 50  
Learning Module 2 | Analysis of Active Portfolio Management. 52  
Learning Module 3 | Exchange-Traded Funds: Mechanics and Applications 53  
Learning Module 4 | Using Multifactor Models 54  
Learning Module 5 | Measuring and Managing Market Risk 55  
Learning Module 6 | Backtesting and Simulation. 56

# CFA Level II – Formula Sheet (2025)

# Setting Up the Texas BA II Plus Financial Calculator

Video: https://youtu.be/0MS8d8QOFmc

# VOLUME 1: QUANTITATIVE METHODS

Learning Module 1 | Basics of Multiple Regression and Underlying Assumptions

$$
Y _ {i} = b _ {0} + b _ {1} X _ {1 i} + b _ {2} X _ {2 i} + \dots + b _ {k} X _ {k i} + \varepsilon_ {i} \qquad \qquad i = 1, 2, 3, \ldots , n
$$

where:

$Y =$  dependent variable

$X =$  independent variable

$b_{0} =$  intercept

$b_{1}, b_{2}, \ldots, b_{k} =$  slope coefficients

$\varepsilon =$  error term

$n =$  number of observations

$k =$  number of independent variables

$b_{0}, b_{1}, b_{2}, \ldots, b_{k} =$  regression coefficients

$$
V a r i a t i o n o f Y = \sum_ {i = 1} ^ {n} (Y _ {i} - \bar {Y}) ^ {2}
$$

# Learning Module 2 | Evaluating Regression Model Fit and Interpreting Model Results

Coefficient of determination,  $R^2$

$$
R ^ {2} = \frac {\text {S u m o f S q u a r e s R e g r e s s i o n}}{\text {S u m o f S q u a r e s T o t a l}} = \frac {S S R}{S S T} = 1 - \frac {S S E}{S S T}
$$

Sum of Squares Total,  $SST = \sum_{i=1}^{n} (Y_i - \bar{Y})^2$

Sum of Squares Regression,  $SSR = \sum_{i=1}^{n}\left(\hat{Y}_i - \bar{Y}\right)^2$

Sum of Squares Error,  $SSE = \sum_{i=1}^{n}\left(Y_{i} - \hat{Y}_{i}\right)^{2}$

Adjusted  $R^2$ ,  $\bar{R}^2 = 1 - \left[\frac{SSE / (n - k - 1)}{SST / (n - 1)}\right] = 1 - \left(\frac{n - 1}{n - k - 1}\right)(1 - R^2)$

# Akaike's information criterion (AIC)

$$
A I C = n \ln \left(\frac {S u m o f s q u a r e s e r r o r}{n}\right) + 2 (k + 1)
$$

where:

$$
n = \text {S a m p l e s i z e}
$$

$k =$  Number of independent variables in the model

# Schwarz's Bayesian information criterion (BIC of SBC)

$$
B I C = n \ln \left(\frac {S u m o f s q u a r e s e r r o r}{n}\right) + \ln (n) (k + 1)
$$

# F-distributed test statistic for jointly omitted variables

$$
F = \frac {(S u m o f s q u a r e s e r r o r r e s t r i c t e d m o d e l - S u m o f s q u a r e s u n r e s t r i c t e d) / q}{S u m o f s q u a r e s u n r e s t r i c t e d m o d e l / (n - k - 1)}
$$

where:

$q =$  Number of restrictions (i.e., number of variables omitted in the restricted model compared to the unrestricted model)

$$
H _ {0}: b _ {m} = b _ {m + 1} = \dots = b _ {m + q - 1} = 0
$$

$H_{a}$  : At least one of the  $q$  slopes  $\neq 0$

# F-test for joint test of slope coefficients

<table><tr><td>ANOVA</td><td>df</td><td>SS</td><td>MS</td><td>F</td></tr><tr><td>Regression</td><td>k</td><td>SSR</td><td>SSR/k</td><td>SSR/k/SSE/(n-k-1)</td></tr><tr><td>Residual</td><td>n-k-1</td><td>SSE</td><td>SSE/(n-k-1)</td><td></td></tr><tr><td>Total</td><td>n-1</td><td>SST</td><td></td><td></td></tr></table>

$$
F s t a t i s t i c = \frac {M e a n S q u a r e R e g r e s s i o n}{M e a n S q u a r e E r r o r} = \frac {S S R / k}{S S E / (n - k - 1)}
$$

$$
H _ {0}: b _ {1} = b _ {2} = \dots = b _ {k} = 0
$$

$$
H _ {a}: \text {A t l e a s t o n e} b _ {j} \neq 0
$$

# t-test statistic for slope coefficient

$$
t = \frac {\hat {b} _ {j} - B _ {j}}{s _ {\hat {b} _ {j}}}
$$

where:

$$
\hat {b} _ {j} = \text {R e g r e s s i o n e s t i m a t e o f} b _ {j}
$$

$$
B _ {j} = \text {H y p o t h e s i z e d v a l u e o f c o e f f i c i e n t} j
$$

$$
s _ {\hat {b} _ {j}} = \text {E s t i m a t e d s t a n d a r d e r r o r o f} \hat {b} _ {j}
$$

Video (Simple Linear Regression): https://youtu.be/uR_9im2JP18

Learning Module 3 | Model Misspecification

# Breusch-Pagan Test

$$
T e s t S t a t i s t i c, \chi_ {B P, k} ^ {2} = n R ^ {2}
$$

where:

$R^2 = R$ -squared between squared residuals and independent variables

# Variance Inflation Factor (VIF)

$$
V I F _ {j} = \frac {1}{1 - R _ {j} ^ {2}}
$$

where:

$R_{j}^{2} = \text{Variation in } X_{j}$  explained by the other  $k - 1$  independent variables

Learning Module 4 | Extensions of Multiple Regression

# Detecting Influential Points

Sum of individual leverages for all observations  $= k + 1$

If observation's leverage  $>3\left(\frac{k + 1}{n}\right) \Rightarrow$  Potentially influential observation

# Studentized Deleted Residual,  $t_{l^*}$

$$
t _ {i ^ {*}} = \frac {e _ {i} ^ {*}}{s _ {e ^ {*}}} = \frac {e _ {i}}{\sqrt {M S E _ {(i)} (1 - h _ {i i})}}
$$

where:

$$
e _ {i} ^ {*} = \text {T h e r e s i d u a l w i t h t h e i t h o b s e r v a t i o n d e l t e d}
$$

$$
S _ {e ^ {*}} = \text {T h e}
$$

$$
k = \text {T h e n u m b e r o f i n d e p e n d e n t v a r i a b l e s}
$$

$MSE_{(i)} = \text{Mean squared error of the regression model that deletes the } i \text{th observation}$ $h_{ii} = \text{The leverage value for the } i \text{th observation}$

# Logistic Regression (Logit)

$$
\ln \left(\frac {P}{1 - P}\right) = b _ {0} + b _ {1} X _ {1} + b _ {2} X _ {2} + \dots + b _ {k} X _ {k} + \varepsilon
$$

$$
P = \frac {1}{1 + \exp [ - (b _ {0} + b _ {1} X _ {1} + b _ {2} X _ {2} + \cdots + b _ {k} X _ {k}) ]}
$$

$$
\ln \left(\frac {P}{1 - P}\right) = L o g o d d s
$$

$$
O d d s r a t i o = e ^ {b _ {i}}
$$

# Likelihood ratio (LR) test

$LR = -2$  (Log likelihood restricted model – Log likelihood unrestricted model)

Learning Module 5 | Time-Series Analysis

# Linear Trend Models

$$
Y _ {t} = b _ {0} + b _ {1} t + \varepsilon_ {t} \qquad t = 1, 2, \dots , T
$$

$t =$  time (independent variable)

# Log-Linear Trend Models

$$
Y _ {t} = e ^ {b _ {0} + b _ {1} t} \qquad t = 1, 2, \dots , T
$$

$$
\ln Y _ {t} = b _ {0} + b _ {1} t
$$

Growth rate of  $Y = e^{b_1} - 1$

# $\pmb{p}$  -th order autoregressive model,  $AR(p)$

$$
x _ {t} = b _ {0} + b _ {1} x _ {t - 1} + b _ {2} x _ {t - 2} + \dots + b _ {p} x _ {t - p} + \varepsilon_ {t}
$$

# Test statistic for autocorrelation of residuals

$$
t = \frac {\text {R e s i d u a l a u t o c o r r e l a t i o n} - 0}{\text {S t a n d a r d e r r o r}} = \frac {\text {R e s i d u a l a u t o c o r r e l a t i o n}}{1 / \sqrt {T}}
$$

where:

$\rho_{\varepsilon ,k} = \frac{Cov(\varepsilon_t,\varepsilon_{t - k})}{\sigma_\varepsilon^2} = k^{th}$  order autocorrelation of the residual

Mean reverting level for AR(1) model

$$
x _ {t} = \frac {b _ {0}}{1 - b _ {1}}
$$

Root Mean Squared Error

$$
R M S E = \sqrt {\frac {S q u a r e d e r r o r}{n}}
$$

Dickey and Fuller Unit-Root Test

$$
x _ {t} - x _ {t - 1} = b _ {0} + g _ {1} x _ {t - 1} + \varepsilon_ {t}
$$

where:

$$
g _ {1} = b _ {1} - 1
$$

n-Period Moving Average

$$
M A _ {n} = \frac {x _ {t} + x _ {t - 1} + \cdots + x _ {t - (n - 1)}}{n}
$$

qth-order Moving-Average,  $MA(q)$

$$
x _ {t} = \varepsilon_ {t} + \theta_ {1} \varepsilon_ {t - 1} + \dots + \theta_ {q} \varepsilon_ {t - q}
$$

$$
E (\varepsilon) = 0, \quad E (\varepsilon_ {t} ^ {2}) = \sigma^ {2}, \quad c o v (\varepsilon_ {t}, \varepsilon_ {s}) = E (\varepsilon_ {t} \varepsilon_ {s}) = 0 \quad f o r t \neq s
$$

Autoregressive Moving-Average (ARMA) Model, ARMA  $(p,q)$

$$
x _ {t} = b _ {0} + b _ {1} x _ {t - 1} + b _ {2} x _ {t - 2} + \dots + b _ {p} x _ {t - p} + \varepsilon_ {t} + \theta_ {1} \varepsilon_ {t - 1} + \dots + \theta_ {q} \varepsilon_ {t - q}
$$

$$
E (\varepsilon) = 0, \quad E (\varepsilon_ {t} ^ {2}) = \sigma^ {2}, \quad c o v (\varepsilon_ {t}, \varepsilon_ {s}) = E (\varepsilon_ {t} \varepsilon_ {s}) = 0 \quad f o r t \neq s
$$

Autoregressive Conditional Heteroskedasticity (ARCH) Model

ARCH(1):

$$
\hat {\sigma} _ {t + 1} ^ {2} = a _ {0} + a _ {1} \hat {\epsilon} _ {t} ^ {2}
$$

Learning Module 6 | Machine Learning

Neural Networks

$$
\underset {w e i g h t} {N e w n e t w o r k} = O l d w e i g h t - L e a n n i n g r a t e \times \left( \begin{array}{c} P a r t i a l d e r i v a t i v e o f t h e \\ t o t a l e r r o r w i t h r e s p e c t \\ t o t h e o l d w e i g h t \end{array} \right)
$$

# Learning Module 7 | Big Data Projects

Normalization of variable X

$$
X _ {i \mathrm {(n o r m a l i z e d)}} = \frac {X _ {i} - X _ {m i n}}{X _ {m a x} - X _ {m i n}}
$$

Standardization of variable X

$$
X _ {i \mathrm {(s t a n d a r d i z e d)}} = \frac {X _ {i} - \mu}{\sigma}
$$

$$
P r e c i s i o n, P = \frac {T r u e P o s i t i v e}{T r u e P o s i t i v e + F a l s e P o s i t i v e}
$$

$$
R e c a l l, R = \frac {T r u e P o s i t i v e}{T r u e P o s i t i v e + F a l s e N e g a t i v e}
$$

$$
A c c u r a c y = \frac {T r u e P o s i t i v e + T r u e N e g a t i v e}{T r u e P o s i t i v e + F a l s e P o s i t i v e + T r u e N e g a t i v e + F a l s e N e g a t i v e}
$$

$$
F 1 S c o r e = \frac {2 \times P r e c i s i o n \times R e c a l l}{P r e c i s i o n + R e c a l l}
$$

$$
F a l s e P o s i t i v e R a t e, F P R = \frac {F a l s e P o s i t i v e}{T r u e N e g a t i v e + F a l s e P o s i t i v e}
$$

$$
T r u e P o s i t i v e R a t e, T P R = \frac {T r u e P o s i t i v e}{T r u e P o s i t i v e + F a l s e N e g a t i v e}
$$

$$
\begin{array}{l} {D o c u m e n t F r e q u e n c y, D F = \frac {S e n t e n c e C o u n t w i t h W o r d}{T o t a l N u m b e r o f S e n t e n c e s}} \\ {I n v e r s e D o c u m e n t F r e q u e n c y, I D F = \log \left(\frac {1}{D F}\right)} \end{array}
$$

$$
T F - I D F = T F \times I D F
$$

Learning Module 1 | Currency Exchange Rates: Understanding Equilibrium Value

# Cross Rates

When given  $\frac{A}{C}$  and  $\frac{C}{B}$ , then  $\frac{A}{B} = \frac{A}{C} \times \frac{C}{B}$ .

When given  $\frac{A}{C}$  and  $\frac{B}{C}$ , then  $\frac{A}{B} = \frac{A}{C} \times \frac{1}{\left(\frac{B}{C}\right)}$

<table><tr><td>Currency pair</td><td>Bid</td><td>Bid/Ask</td></tr><tr><td>A/B</td><td>x</td><td>y</td></tr><tr><td>B/A</td><td>1/y</td><td>1/x</td></tr></table>

Video: https://youtu.be/wyDKKPkPhzw

# Arbitrage Opportunities Between Dealers and Interbank

Video: https://youtu.be/Lqo9UZ3yyEA

# Covered Interest Rate Parity

$$
F _ {f / d} = S _ {f / d} \left[ \frac {1 + i _ {f} \left(\frac {A c t u a l}{3 6 0}\right)}{1 + i _ {d} \left(\frac {A c t u a l}{3 6 0}\right)} \right]
$$

$$
\frac {F _ {f / d} - S _ {f / d}}{S _ {f / d}} = \frac {(i _ {f} - i _ {d}) \left(\frac {A c t u a l}{3 6 0}\right)}{1 + i _ {d} \left(\frac {A c t u a l}{3 6 0}\right)}
$$

Video: https://youtu.be/9jOzFA9GuHU

# Mark-to-Market Value of a Forward Contract

Original position: Long base currency  $d$  forward at forward rate  $F_{0,f / d}$  (Offer side)

$$
V a l u e o f L o n g F o r w a r d = \frac {\left(F _ {t , f / d} - F _ {0 , f / d}\right) \times C o n t r a c t S i z e}{1 + i _ {f} \left(\frac {R e m a i n i n g d a y s t o m a t u r i t y}{3 6 0}\right)}
$$

$F_{t,f / d} =$  Forward rate at valuation date, t (Bid side)

Video: https://youtu.be/wLqzRrutAc

# Uncovered Interest Rate Parity

$$
E (S _ {f / d}) = S _ {f / d} \left[ \frac {1 + i _ {f} \left(\frac {A c t u a l}{3 6 0}\right)}{1 + i _ {d} \left(\frac {A c t u a l}{3 6 0}\right)} \right]
$$

$$
\% \Delta S _ {f / d} ^ {e} = \frac {(i _ {f} - i _ {d}) \left(\frac {A c t u a l}{3 6 0}\right)}{1 + i _ {d} \left(\frac {A c t u a l}{3 6 0}\right)} \approx (i _ {f} - i _ {d}) \left(\frac {A c t u a l}{3 6 0}\right)
$$

Video (Carry Trade): https://youtu.be/ 26fG3Zvzyg

# Absolute PPP

$$
S _ {f / d} = \frac {P _ {f}}{P _ {d}}
$$

# Relative PPP

$$
\% \Delta S _ {f / d} = \frac {\left(\pi_ {f} - \pi_ {d}\right) \left(\frac {A c t u a l}{3 6 0}\right)}{1 + \pi_ {d} \left(\frac {A c t u a l}{3 6 0}\right)} \approx \left(\pi_ {f} - \pi_ {d}\right) \left(\frac {A c t u a l}{3 6 0}\right)
$$

# Ex ante PPP

$$
\% \Delta S _ {f / d} ^ {e} \approx (\pi_ {f} ^ {e} - \pi_ {d} ^ {e}) \left(\frac {A c t u a l}{3 6 0}\right)
$$

# International Fisher Effect

$$
i _ {f} - i _ {d} = \pi_ {f} ^ {e} - \pi_ {d} ^ {e}
$$

where:

$$
\pi^ {e} = \text {E x p e c t e d i n f l a t i o n r a t e}
$$

$$
\pi = \text {A c t u a l i n f l a t i o n r a t e}
$$

# Mundell-Fleming Model

Bonus Video: https://youtu.be/xNo3GpWYgKA

Learning Module 2 | Economic Growth and the Investment Decision

# Grinold-Kroner Model

$$
E (R _ {e}) = D Y + \Delta (P / E) + i + g - \Delta S
$$

where:

$E(R_{e}) =$  Expected equity return

$DY =$  Dividend yield

$\Delta(P / E) = \text{Expected repricing}$

$i =$  Expected inflation rate

$g =$  Real economic growth rate

$\Delta S =$  Change in shares outstanding

# Dilution effect

$$
\Delta S = \text {N e t b u y b a c k} + \text {R e l a t i v e d y n a m i s m}
$$

# Cobb-Douglas Production Function

$$
Y = T K ^ {\alpha} L ^ {1 - \alpha} \quad \text {w h e r e a <   1}
$$

where:

Y = Output

$\alpha =$  Share of output allocated to capital  $(K)$

$1 - \alpha =$  share of output allocated to labor  $(L)$

$T =$  total factor productivity (TFP), represents technological progress of the economy

Output per worker  $= \frac{Y}{L} = T\left(\frac{K}{L}\right)^{\alpha}$

$$
\begin{array}{c} \text {P e r c e n t a g e c h a n g e i n} \\ \text {l a b o r p r o d u c t i v i t y} \end{array} = \begin{array}{c} \text {P e r c e n t a g e c h a n g e i n} \\ \text {t o t a l f a c t o r p r o d u c t i v i t y} \end{array} + \begin{array}{c} \text {P e r c e n t a g e c h a n g e i n} \\ \text {c a p i t a l d e e p e n i n g} \end{array}
$$

Marginal product of capital, MPK

$$
M P K = \alpha \left(\frac {Y}{K}\right)
$$

Amount of output that is allocated to providers of capital, a

$$
\alpha = \frac {r K}{Y}
$$

Growth Accounting equation:

$$
\frac {\Delta Y}{Y} = \frac {\Delta T}{T} + \alpha \frac {\Delta K}{K} + (1 - \alpha) \frac {\Delta L}{L}
$$

Growth rate in potential GDP = Long-term growth rate + Long-term growth rate

of labor force

in labor productivity

Labor force participation =  $\frac{\text{Labor force}}{\text{Working age population}}$

Sustainable growth rate of output per capita

$$
g ^ {*} = \frac {\theta}{1 - \alpha}
$$

Sustainable growth rate of output (Steady state growth rate)

$$
G ^ {*} = \frac {\theta}{1 - \alpha} + n
$$

Equilibrium output-to-capital ratio (in steady state):

$$
{\frac {Y}{K}} = {\frac {1}{s}} \Bigl [ {\frac {\theta}{1 - \alpha}} + n + \delta \Bigr ]
$$

where:

$$
\begin{array}{l} \theta = \text {g r o w t h} \\ \alpha = \text {e l e s t i c i t y o f o u t p u t w i t h r e s p e c t t o c a p i t a l} \\ s = \text {f r a c t i o n} (\Upsilon) \text {t h a t i s s a v e d} \\ \delta = \text {r a t e} \\ n = \text {labor supply growth} = \% \Delta L \\ \end{array}
$$

# Endogeneous Growth Model

Production function:

$$
y _ {e} = c k _ {e}
$$

Growth rate of output per capita:

$$
\frac {\Delta y _ {e}}{y _ {e}} = \frac {\Delta k}{k _ {e}} = s c - \delta - n
$$

where:

$$
\begin{array}{l} y _ {e} = \text {o u t p u t p e r w o r k e r} \\ k _ {e} = \text {c a p i t a l p e r w o k e r} \\ c = \text {m a r g i n a l} \\ \end{array}
$$

Learning Module 1 | Intercorporate Investments

# Investments in Associates (Equity Method)

$$
\underset {a s s o c i a t e s} {E n d i n g} \underset {a s s o c i a t e s} {B e g i n n i n g} = \underset {a s s o c i a t e s} {i n v e s t m e n t i n} + \underset {n e t} {\text {S h a r e o f}} - \underset {r e c e i v e d} {\text {S h a r e o f}} - \underset {p u r c h a s e p r i c e} {\text {A m o r t i z a t i o n o f e x c e s s}}
$$

Impact on Investor's Income Statement

$$
= \frac {\text {S h a r e o f}}{\text {n e t i n c o m e}} - \frac {\text {A m o r t i z a t i o n o f e x c e s s}}{\text {p u r c h a s e p r i c e}} - \frac {\text {S h a r e o f U n r e l i z e d p r o f i t f r o m}}{\text {d o w n s t r e a m o r u p s t r e a m s a l e}}
$$

# Business Combinations (Acquisition Method)

Excess purchase price

= Acquisition price – %Ownership × Book value of net identifiable assets

# Partial Goodwill

= Acquisition price - (%Ownership × Fair value of identifiable net assets)  
= Acquisition price - (%Ownership × Book value of identifiable net assets)

- (%Ownership × Excess purchase price attributable to identifiable net assets)

Non controlling interest = %NCI × Fair value of identifiable net assets

# Full Goodwill

= Fair value of entity - Fair value of net identifiable assets

Non controlling interest = %NCI × Fair value of entity

Video: https://youtu.be/RgxmPbx4-0o

# IFRS

$$
\begin{array}{c} I m p a i r m e n t \\ \text {l o s s} \end{array} = \begin{array}{c} C a r r y i n g v a l u e o f \\ c a s h g e n e r a t i n g u n i t \end{array} - \begin{array}{c} R e c o v e r a b l e a m o u n t o f \\ c a s h g e n e r a t i n g u n i t \end{array}
$$

# US GAAP

$$
\begin{array}{c} \text {I m p l i e d} \\ \text {g o o d w i l l} \end{array} = \begin{array}{c} \text {F a i r v a l u e o f} \\ \text {r e p o r t i n g u n i t} \end{array} - \begin{array}{c} \text {F a i r v a l u e o f r e p o r t i n g u n i t ^ {\prime}} \\ \text {i d e n t i f i a b l e n e t a s s e t s} \end{array}
$$

$$
\begin{array}{c} I m p a i r m e n t \\ \text {l o s s} \end{array} = \begin{array}{c} C a r r y i n g v a l u e \\ \text {o f g o o d w i l l} \end{array} - \begin{array}{c} I m p l i e d \\ \text {g o o d w i l l} \end{array}
$$

# Share-Based Compensation Accounting

# Share Award

$$
C o m p e n s a t i o n e x p e n s e = \frac {F a i r v a l u e o f a w a r d o n g r a n t d a t e}{V e s t i n g p e r i o d}
$$

# Stock Options

$$
C o m p e n s a t i o n e x p e n s e = \frac {F a i r v a l u e o f o p t i o n s o n g r a n t d a t e}{V e s t i n g p e r i o d}
$$

# Treasury Stock Method

$$
\begin{array}{c} D i l u t e d \\ s h a r e s \\ o u t s t a n d i n g \end{array} = \begin{array}{c} B a s i c \\ s h a r e s \\ o u t s t a n d i n g \end{array} + \begin{array}{c} S h a r e s i s s u e d f r o m \\ c o n v e r s i o n o r e x e c i s e \\ o f s h a r e b a s e d a w a r d s \end{array} - \frac {\left( \begin{array}{c} P r o c e e d s f r o m \\ c o n v e r s i o n o r e x e c i s e \\ o f s h a r e b a s e d a w a r d s \end{array} \right)}{\text {A v e r a g e s h a r e p r i c e f o r}}
$$

$$
\begin{array}{c} \text {A s s u m e d} \\ \text {p r o c e e d s} \end{array} = \begin{array}{c} \text {C a s h p r o c e e d s} \\ \text {f r o m e x e r c i s e} \end{array} + \begin{array}{c} \text {A v e r a g e u n r e c o n g i z e d} \\ \text {s h a r e - b a s e d} \\ \text {c o m p e n s a t i o n e x p e n s e} \end{array}
$$

where:

$$
C a s h p r o c e e d s f r o m e x e r c i s e = \left\{ \begin{array}{c l} S t r i k e p r i c e \times N u m b e r o f o p t i o n s & F o r o p t i o n s \\ 0 & F o r R S U s \end{array} \right.
$$

$$
\begin{array}{c} U n r e c o g n i s e d s h a r e - b a s e d \\ c o m p e n s a t i o n e x p e n s e \end{array} = \begin{array}{c} U n v e s t e d \\ a w a r d s \end{array} \times \begin{array}{c} F a i r v a l u e o n \\ g r a n t d a t e \end{array}
$$

# Forecasting Shares Outstanding With Share-Based Awards

$$
\begin{array}{l} \begin{array}{c} \text {B a s i c s h a r e s} \\ \text {o u t s t a n d i n g , =} \\ \text {e n d o f p e r i o d} \end{array} \begin{array}{c} \text {B a s i c s h a r e s} \\ \text {o u t s t a n d i n g ,} \\ \text {b e g i n n i n g o f p e r i o d} \end{array} + R S U s v e s t e d + \begin{array}{c} \text {S h a r e o p t i o n s} \\ \text {e x e r c i s e d} \end{array} \\ \begin{array}{c} \text {S h a r e s i s s u e d f r o m} \\ + \text {s e c o n d a r i e s ,} \\ \text {a c q u i s i t i o n s , e t c .} \end{array} - \begin{array}{c} \text {S h a r e} \\ \text {r e p u r c h a s e s} \end{array} \\ \end{array}
$$

# Defined Benefit Pension Plans

$$
F u n d e d \quad s t a t u s = F a i r \quad v a l u e \quad o f \quad p l a n \quad a s s e t s - P e n s i o n \quad o b j o l i g a t i o n
$$

$$
\frac {E n d i n g f a i r v a l u e}{o f p l a n a s s e t s} = \frac {B e g i n n i n g f a i r v a l u e}{o f p l a n a s s e t s} + C o n t r i b u t i o n s + \frac {A c t u a l r e t u r n}{o n p l a n a s s e t s} - \frac {B e n e f i t s}{p a i d}
$$

$$
\begin{array}{c} E n d i n g p e n s i o n \\ o b l i g a t i o n \end{array} = \begin{array}{c} B e g i n n i n g p e n s i o n \\ o b l i g a t i o n \end{array} + \begin{array}{c} S e r v i c e \\ c o s t s \end{array} + \begin{array}{c} I n t e r e s t \\ c o s t \end{array} + \begin{array}{c} A c t u a r i a l \\ l o s s / (g a i n) \end{array} - \begin{array}{c} B e n e f i t s \\ p a i d \end{array}
$$

$$
I n t e r e s t c o s t = \begin{array}{c} B e g i n n i n g p e n s i o n \\ o b l i g a t i o n \end{array} \times \begin{array}{c} Y i e l d o n i n v e s t m e n t g r a d e \\ c o r p o r a t e b o n d \end{array}
$$

# IFRS Only

In income statement,

$$
\text {R e p o r t e d} = \frac {\text {C u r r e n t a n d p a s t}}{\text {s e r v i c e c o s t s}} + \frac {\text {N e t i n t e r e s t}}{\text {c o s t / (i n c o m e)}}
$$

$$
\frac {\text {N e t i n t e r e s t}}{\text {c o s t} / (\text {i n c o m e})} = \binom {\text {B e g i n n i n g p e n s i o n} - \text {B e g i n n i n g f a i r v a l u e}} {\text {o b l i g a t i o n}} \times \frac {\text {Y i e l d o n i n v e s t m e n t}}{\text {g r a d e c o r p o r a t e b o n d}}
$$

# Learning Module 3 | Multinational Operations

Net assets = Total assets - Total liabilities

Net monetary assets = Monetary assets – Monetary liabilities

# Current Rate Method

Currency translation adjustment

= Total assets of foreign subsidiary in parent currency terms

Total liabilities of foreign subsidiary in parent currency terms  
- Shareholder capital of foreign subsidiary in parent currency terms  
- Other equity items of foreign subsidiary in parent currency terms

# Hyperinflationary Environment

# IFRS

$$
\begin{array}{c} R e s t a t e m e n t f a c t o r f o r \\ m o n e t a r y a s s e t s \& l i a b i l i t i e s \end{array} = \frac {E n d o f p e r i o d p r i c e i n d e x}{E n d o f p e r i o d p r i c e i n d e x}
$$

$$
\frac {\text {R e s t a t e m e n t f a c t o r f o r}}{\text {n o n - m o n e t a r y a s s e t s} \& \text {l i a b i l i t i e s}} = \frac {\text {E n d o f p e r i o d p r i c e i n d e x}}{\text {B e g i n n i n g o f p e r i o d p r i c e i n d e x}}
$$

$$
\frac {\text {R e s t a t e m e n t f a c t o r f o r}}{\text {i n c o m e s t a t e m e n t i t e m s}} = \frac {\text {E n d o f p e r i o d p r i c e i n d e x}}{\text {A v e r a g e p r i c e i n d e x f o r t h e p e r i o d}}
$$

$$
\begin{array}{c} T o t a l   T i e r   1 \\ C a p i t a l \end{array} = \begin{array}{c} C o m m o n   E q u i t y \\ T i e r   1   C a p i t a l \end{array} + \begin{array}{c} A d d i t i o n a l \\ T i e r   1   C a p i t a l \end{array}
$$

$$
\begin{array}{c} T o t a l R e g u l a t o r y \\ C a p i t a l \end{array} = \begin{array}{c} T o t a l T i e r 1 \\ C a p i t a l \end{array} + \begin{array}{c} T o t a l T i e r 2 \\ C a p i t a l \end{array}
$$

$$
\frac{\text{Common Equity}}{\text{Tier 1 Ratio}} = \frac{\text{Common Equity Tier 1 Capital}}{\text{Risk Weighted Assets}}\geq 4.5\%
$$

$$
\frac{\text{Tier 1}}{\text{Ratio}} = \frac{\text{Total Tier 1 Capital}}{\text{Risk Weighted Assets}}\geq 6.0\%
$$

$$
\frac {T o t a l C a p i t a l}{R a t i o} = \frac {T o t a l R e g u l a t o r y C a p i t a l}{R i s k W e i g h t e d A s s e t s} \geq 8.0 \%
$$

$$
\frac {\text {L i q u i d i t y C o v e r a g e}}{\text {R a t i o} , L C R} = \frac {\text {H i g h Q u a l i t y L i q u i d A s s e t s}}{\text {E x p e c t e d c a s h o u t f l o w s}}
$$

$$
\begin{array}{c} N u m b e r o f d a y s t h a t b a n k c a n w i t h s t a n d \\ a s t r e s s l e v e l v o l u m e o f c a s h o u t f l o w s \end{array} = L C R \times 3 0
$$

Number of days that bank can withstand a stress level volume of cash outflows for  $(LCR \times 30)$  days.

$$
\frac {\text {N e t S t a b l e F u n d i n g}}{\text {R a t i o} , \text {N S F R}} = \frac {\text {A v a i l a b l e S t a b l e F u n d i n g}}{\text {R e q u i r e d S t a b l e F u n d i n g}}
$$

# Property and Casualty Companies

$$
\frac {\text {L o s s a n d l o s s a d j u s t m e n t}}{\text {e x p e n s e r a t i o}} = \frac {\text {L o s s e x p e n s e} + \text {L o s s a d j u s t m e n t e x p e n s e}}{\text {N e t p r e m i u m s e a r n e d}}
$$

$$
\frac {\text {U n d e r w r i t i n g}}{\text {e x p e n s e r a t i o}} = \frac {\text {U n d e r w r i t i n g e x p e n s e}}{\text {N e t p r e m i u m s w r i t t e n}}
$$

$$
\begin{array}{c} \text {C o m b i n e d} \\ \text {r a t i o} \end{array} = \begin{array}{c} \text {L o s s a n d l o s s a d j u s t m e n t} \\ \text {e x p e n s e r a t i o} \end{array} + \begin{array}{c} \text {U n d e r w r i t i n g} \\ \text {e x p e n s e r a t i o} \end{array}
$$

$$
\frac {\text {D i v i d e n d s t o p o l i c y h o l d e r s}}{\text {(s h a r e h o l d e r s) r a t i o}} = \frac {\text {D i v i d e n d s t o p o l i c y h o l d e r s (s h a r e h o l d e r s)}}{\text {N e t p r e m i u m s e a r n e d}}
$$

$$
\begin{array}{c} \text {C o m b i n e d r a t i o} \\ \text {a f t e r d i v i d e n d s} \end{array} = \begin{array}{c} \text {C o m b i n e d} \\ \text {r a t i o} \end{array} + \begin{array}{c} \text {D i v i d e n d s t o p o l i c y h o l d e r s} \\ \text {(s h a r e h o l d e r s) r a t i o} \end{array}
$$

# Beneish Model

$$
\begin{array}{l} M - s c o r e = - 4. 8 4 + 0. 9 2 0 (D S R) + 0. 5 2 8 (G M I) + 0. 4 0 4 (A Q I) + 0. 8 9 2 (S G I) \\ + 0. 1 1 5 (D E P I) - 0. 1 7 2 (S G A I) + 4. 6 7 0 (A c c r u a l s) - 0. 3 2 7 (L E V I) \\ \end{array}
$$

where:

DSR (day sales receivable index) =  $\frac{\text{Receivables}_t / \text{Sales}_t}{\text{Receivables}_{t-1} / \text{Sales}_{t-1}}$

GMI (gross margin index) =  $\frac{GM_{t-1}}{GM_t}$

AQI (asset quality index) =  $\frac{[1 - (PPE_{t} + CA_{t}) / TA_{t}]}{[1 - (PPE_{t-1} + CA_{t-1}) / TA_{t-1}]$

SGI (sales growth index) =  $\frac{Sales_{t}}{Sales_{t-1}}$

DEPI (depreciation index) =  $\frac{Depreciation_{t-1}}{Depreciation_t}$

SGAI (sales, general, and administrative expenses index) =  $\frac{SGA_{t} / Sales_{t}}{SGA_{t-1} / Sales_{t-1}}$

Accruals =  $\frac{\text{Income before extraordinary items} - \text{Cash from operations}}{\text{Total assets}}$

LEVI (leverage index) =  $\frac{Leverage_t}{Leverage_{t-1}}$

# Earnings Persistence

$$
E a r n i n g s _ {t + 1} = \alpha + \beta (E a r n i n g s _ {t}) + \varepsilon
$$

$$
E a r n i n g s _ {t + 1} = \alpha + \beta_ {1} (C a s h f l o w _ {t}) + \beta_ {2} (A c c r u a l s _ {t}) + \varepsilon
$$

$$
\text {C a s h - f l o w - b a s e d a c c r u a l s} = \mathrm {N I} - (\mathrm {C F O} + \mathrm {C F I})
$$

# Learning Module 6 | Integration of Financial Statement Analysis Techniques

$$
\begin{array}{l} \begin{array}{c} \text {N e t O p e r a t i n g} \\ \text {A s s e t s (N O A)} \end{array} = \begin{array}{c} \text {O p e r a t i n g} \\ \text {A s s e t s} \end{array} - \begin{array}{c} \text {O p e r a t i n g} \\ \text {L i a b i l i t i e s} \end{array} \\ = \left( \begin{array}{c} T o t a l \\ A s s e t s \end{array} - \begin{array}{c} C a s h a n d \\ S h o r t - t e r m I n v e s t m e n t s \end{array} \right) - \left( \begin{array}{c} T o t a l \\ L i a b i l i t i e s \end{array} - \begin{array}{c} T o t a l \\ D e b t \end{array} \right) \\ \end{array}
$$

$$
\frac {\text {B a l a n c e - s h e e t - b a s e d}}{\text {a c c r u a l s r a t i o}} = \frac {N O A _ {t} - N O A _ {t - 1}}{(N O A _ {t} + N O A _ {t - 1}) / 2}
$$

$$
\frac {\text {C a s h - f l o w - b a s e d}}{\text {a c c r u a l s r a t i o}} = \frac {N I _ {t} - (C F O _ {t} + C F I _ {t})}{(N O A _ {t} + N O A _ {t - 1}) / 2}
$$

Learning Module 1 | Analysis of Dividends and Share Repurchases

# Dividend Payout Policies

Target payout adjustment model (Lintner model)

$$
\frac {E x p e c t e d}{d i v i d e n d} = \frac {L a s t}{d i v i d e n d} + \left(\frac {E x p e c t e d}{E a r n i n g s} \times \frac {T a r g e t p a y o u t}{r a t i o} - \frac {L a s t}{d i v i d e n d}\right) \times \frac {A d j u s t m e n t}{f a c t o r}
$$

where:

$$
A d j u s t m e n t f a c t o r = \frac {1}{N u m b e r o f y e a r s f o r a d j u s t m e n t t o t a k e p l a c e}
$$

Constant dividend payout ratio policy

$$
D i v i d e n d = \underset {p a y o u t r a t i o} {\text {D i v i d e n d}} \times \underset {e a r n i n g s} {\text {C u r r e n t}}
$$

Video: https://youtu.be/hhcvNiTpZX4

# EPS and BVPS After Share Repurchase

$$
E P S a f t e r b u y b a c k = \frac {E a r n i n g s b e f o r e b u y b a c k - A f t e r t a x c o s t o f f u n d s}{S h a r e s o u t s t a n d i n g a f t e r b u y b a c k}
$$

Video: https://youtu.be/Pd0-QQF-VhQ

$$
B V P S a f t e r b u y b a c k = \frac {\text {B o o k V a l u e b e f o r e b u y b a c k} - \text {V a l u e o f s h a r e b u y b a c k}}{\text {S h a r e s o u t s t a n d i n g a f t e r b u y b a c k}}
$$

# Analysis of Dividend Safety

$$
D i v i d e n d p a y o u t r a t i o = \frac {D i v i d e n d s}{N e t I n c o m e}
$$

$$
\text {D i v i d e n d c o v e r a g e r a t i o} = \frac {\text {N e t I n c o m e}}{\text {D i v i d e n d s}}
$$

$$
F C F E c o v e r a g e r a t i o = \frac {F C F E}{D i v i d e n d s + S h a r e r e p u r c h a s e s}
$$

Weighted average cost of capital

$$
W A C C = w _ {d} r _ {d} (1 - t) + w _ {p} r _ {p} + w _ {e} r _ {e}
$$

where:

$w_{d} =$  Weight of debt in capital structure

$w_{p} =$  Weight of preferred equity in capital structure

$w_{e} =$  Weight of common equity in capital structure

$r_d = \text{Pre-tax cost of debt}$

$r_p =$  Cost of preferred equity

$r_e =$  Cost of common equity

Cost of debt,  $r_d = r_f + \text{Credit spread}$

Cost of equity,  $r_e = r_f + ERP + IRP$

where:

[ ERP = \text{Equity risk premium} = \frac{\text{Benchmark index}}{\text{return}} - \frac{\text{Risk free rate}}{\text{rate}} ]

IRP = Idiosyncratic risk premium

# Leases

$$
\begin{array}{c} \text {P r e s e n t V a l u e o f} \\ \text {L e a s e P a y m e n t s} \end{array} + \begin{array}{c} \text {P r e s e n t V a l u e o f} \\ \text {R e s i d u a l V a l u e t o} \end{array} = \begin{array}{c} \text {F a i r V a l u e o f} \\ \text {L e a s e d A s s e t} \end{array} + \begin{array}{c} \text {L e s s o r ^ {\prime} s D i r e c t} \\ \text {I n i t i a l C o s t s} \end{array}
$$

# Equity Risk Premium

Historical Approach (Ex-Post)

$$
E R P = \begin{array}{c} A v e r a g e b e n c h m a r k \\ i n d e x r e t u r n \end{array} - \begin{array}{c} A v e r a g e r i s k \\ f r e e r a t e \end{array}
$$

Gordon Growth model

$$
E R P = \frac {D _ {1}}{V _ {0}} + g - r _ {f}
$$

# Grinold-Kroner Model

$$
E R P = [ D Y + \text {E x p e c t e d r e p r i c i n g} + E a r n i n g s g r o w t h p e r s h a r e ] - r _ {f}
$$

$$
E R P = [ D Y + \Delta (P / E) + i + g - \Delta S ] - r _ {f}
$$

$$
E a r n i n g s \quad g r o w t h \quad p e r \quad s h a r e = i + g - \Delta S
$$

where:

$DY =$  Dividend yield of market index

$\Delta(P / E) =$  Expected growth rate in P/E

$$
i = \text {E x p e c t e d i n f l a t i o n} = \frac {1 + Y T M _ {\text {T r e a s u r y b o n d}}}{1 + Y T M _ {\text {T I P S}}} - 1
$$

$g =$  Expected growth rate in real earnings per share

$\Delta S =$  Expected change in shares outstanding ( $\Delta S > 0$  for share issuance;  $\Delta S < 0$  for share buyback)

# Cost of Equity

# Gordon Growth Model

$$
r _ {e} = \frac {D _ {1}}{P _ {0}} + g
$$

# Two-Stage DDM

$$
P _ {0} = \sum_ {i = 1} ^ {n} \frac {D _ {t}}{(1 + r _ {e}) ^ {t}} + \frac {P _ {n}}{(1 + r _ {e}) ^ {n}}
$$

# Bond Yield Plus Risk Premium Approach (BYPRP)

$$
r _ {e} = r _ {d} + \text {R i s k p r e m i u m}
$$

where  $r_d =$  Cost of company's long-term debt

# Capital Asset Pricing Model (CAPM)

$$
r _ {e} = r _ {f} + \beta \times E R P
$$

# Fama-French model

Three-factor model

$$
r _ {e} = r _ {f} + \beta_ {1} E R P + \beta_ {2} S M B + \beta_ {3} H M L
$$

Five-factor model

$$
r _ {e} = r _ {f} + \beta_ {1} E R P + \beta_ {2} S M B + \beta_ {3} H M L + \beta_ {4} R M W + \beta_ {5} C M A
$$

where:

$$
S M B = \text {S i z e p r e m i u m}
$$

$$
H M L = \text {V a l u e p r e m i u m}
$$

$$
R M W = \text {P r o f i t a b i l i t y p r e m i u m}
$$

$$
C M A = \text {I n v e s t m e n t p r e m i u m}
$$

# Expanded CAPM

$$
r _ {e} = r _ {f} + \beta_ {p e e r} (E R P) + S P + S C R P
$$

# Build-Up Approach

$$
r _ {e} = r _ {f} + E R P + S P + S C R P + I P
$$

where:

$$
S P = \text {S i z e p r e m i u m (f o r s m a l l e r , p r i v a t e l y h e l d c o m p a n i e n s)}
$$

$$
I P = \text {I n d u s t r y}
$$

$$
S C R P = \text {C o m p a n y - s p e c i f i c r i s k p r e m i u m}
$$

# Country Spread Model

$$
E R P = \underset {d e v e l o p e d m a r k e t} {E R P f o r a} + \lambda \times C o u n t r y r i s k p r e m i u m
$$

where:

$$
\lambda = \text {L e v e l o f}
$$

$$
C o u n t r y \text {r i s k p r e m i u m} = \text {S o v e r e i g n y i e l d s p r e a d}
$$

$$
\underset {s p r e a d} {S o v e r e i g n y i e l d} = \underset {o f t h e d e v e l o p e d m a r k e t} {Y i e l d o n e m e r g i n g m a r k e t b o n d s} - \underset {g o v e r n m e n t b o n d s} {Y i e l d o n d e v e l o p e d m a r k e t}
$$

# Aswath Damodaran's CRP

$$
C o u n t r y r i s k p r e m i u m = S o v e r e i g n y i e l d s p r e a d \times \frac {\sigma_ {E q u i t y}}{\sigma_ {B o n d}}
$$

where:

$\sigma_{Equity} = \text{Volatility of the local country's equity market}$ $\sigma_{Bond} = \text{Volatility of the local country's bond market}$

# International CAPM

$$
E (r _ {e}) = r _ {f} + \beta_ {G} \big [ E (r _ {g m}) - r _ {f} \big ] + \beta_ {C} \big [ E (r _ {C}) - r _ {f} \big ]
$$

where:

[ E\left(r_{gm}\right) - r_f = \text{Risk premium of a global index} ]
[ r_C = \text{Wealth-weighted foreign currency index return} ]

Learning Module 4 | Corporate Restructuring

# Evaluating Materiality Based on Size

For Acquisition/Divestiture:

Value of transaction Enterprise value of acquiring company

For Cost Restructuring:

Cost savings Sales

# Premium Paid Analysis

$$
T a k e o v e r p r e m i u m, P R M = \frac {D P - S P}{S P}
$$

where:

$$
D P = \text {D e a l p r i c e p e r s h a r e o f t h e t a r g e t c o m p a n y}
$$

$SP =$  Unaffected stock price of the target company (i.e., pre-announcement)

# VOLUME 5: EQUITY VALUATION

Learning Module 1 | Equity Valuation Applications and Processes

$$
V _ {E} - P = (V - P) + (V _ {E} - V)
$$

where:

$$
V _ {E} = \text {E s t i m a t e d i n t r i n s i c v a l u e}
$$

$$
P = \text {M a r k e t p r i c e}
$$

$$
V = \text {I n t r i n s i c v a l u e}
$$

Conglomerate discount = Sum-of-the-parts value - Market value

Learning Module 2 | Discounted Dividend Valuation

# Discounted Dividend Valuation

$$
V _ {0} = \sum_ {t = 1} ^ {n} \frac {C F _ {t}}{(1 + r) ^ {t}}
$$

$$
V _ {0} = \frac {D _ {1}}{(1 + r) ^ {1}} + \frac {D _ {2}}{(1 + r) ^ {2}} + \dots + \frac {D _ {n}}{(1 + r) ^ {n}} + \frac {P _ {n}}{(1 + r) ^ {n}}
$$

# Gordon Growth Model

$$
V _ {0} = \frac {D _ {1}}{r - g} = \frac {D _ {0} (1 + g)}{r - g}
$$

# Fixed-rate perpetual preferred stock

$$
V _ {0} = \frac {D}{r}
$$

Value of stock = Value of a company + Present value of growth

with zero-growth

opportunities (PVGO)

$$
V _ {0} = \frac {E _ {1}}{r} + P V G O
$$

$$
\frac {V _ {0}}{E _ {1}} = \frac {P _ {0}}{E _ {1}} = \frac {1}{r} + \frac {P V G O}{E _ {1}}
$$

If dividend and earnings growth rate is constant,

$$
r = \frac {D _ {1}}{P _ {0}} + g
$$

# Two-Stage Dividend Discount Model

$$
V _ {0} = \sum_ {t = 1} ^ {n} \frac {D _ {0} (1 + g _ {s}) ^ {t}}{(1 + r) ^ {t}} + \frac {D _ {0} (1 + g _ {s}) ^ {n} (1 + g _ {L})}{(1 + r) ^ {n} (r - g _ {L})}
$$

Video: https://youtu.be/7vXWsTKiSPE

# The H-Model

$$
V _ {0} = \frac {D _ {0} (1 + g _ {L}) + D _ {0} H (g _ {S} - g _ {L})}{r - g _ {L}}
$$

where:

$H =$  half-life in years of the high-growth period

$g_{S} =$  Short-term growth-rate

$g_{L} =$  Long-term growth rate

Video: https://youtu.be/IAMFZXSPKOY

# PRAT model

Sustainable growth rate,  $g = b \times ROE$

Video: https://youtu.be/MnfRRRhuGpA

$$
g = \frac {N I - D i v i d e n d s}{N I} \times \frac {N I}{S a l e s} \times \frac {S a l e s}{T A} \times \frac {T A}{T E}
$$

Learning Module 3 | Free Cash Flow Valuation

# Free Cash Flow to the Firm (FCFF) Valuation Approach

$$
F i r m V a l u e = \sum_ {t = 1} ^ {\infty} \frac {F C F F _ {t}}{(1 + W A C C) ^ {t}}
$$

If non-operating assets = 0

Equity Value = Firm Value - Market Value of Debt

# FCFE Valuation Approach

$$
E q u i t y V a l u e = \sum_ {t = 1} ^ {\infty} \frac {F C F E _ {t}}{(1 + r) ^ {t}}
$$

# Single-Stage (Constant Growth) FCFF and FCFE Model

# FCFF Valuation Approach

$$
F i r m V a l u e = \frac {F C F F _ {1}}{W A C C - g} = \frac {F C F F _ {0} (1 + g)}{W A C C - g}
$$

# FCFE Valuation Approach

$$
E q u i t y V a l u e = \frac {F C F E _ {1}}{r - g} = \frac {F C F E _ {0} (1 + g)}{r - g}
$$

# Free cash flow to the Firm, FCFF

$$
\begin{array}{l} F C F F = N I + N C C + I n t (1 - T a x R a t e) - F C I n v - W C I n v \\ = C F O + \operatorname {I n t} (1 - \text {T a x R a t e}) - F C I n v \\ = E B I T (1 - \text {T a x R a t e}) + D e p - F C I n v - W C I n v \\ = E B I T D A (1 - \text {T a x R a t e}) + \text {D e p} (\text {T a x R a t e}) - F C I n v - W C I n v \\ \end{array}
$$

where:

NI = Net income available to common shareholders

NCC = Net noncash charges (e.g. depreciation)

Int  $=$  Interest expense

FCInv = Fixed capital investments = Maintenance Capex + Growth Capex

$$
= \Delta G r o s s P P E = \Delta N e t P P E + D e p r e c i a t i o n
$$

WClInv = Investment in working capital

# Free cash flow to the Equity, FCFE

$$
\begin{array}{l} \mathrm {F C F E} = \mathrm {F C F F} - \operatorname {I n t} (1 - \text {T a x R a t e}) + \text {N e t b o r r o w i n g} \\ = N I + N C C - F C I n v - W C I n v + N e t b o r r o w i n g \\ = C F O - F C I n v + N e t b o r r o w i n g \\ \end{array}
$$

where:

Net borrowing = Debt issued - Debt repaid

# Video: https://youtu.be/rtlvly6F10A

If (FCInv - Dep) and WClnv funded using Debt (based on debt ratio):

$$
\mathrm {F C F E} = \mathrm {N I} + \text {D e p} - \mathrm {F C I n v} - \mathrm {W C I n v} + \text {N e t b o r r o w i n g}
$$

where:

Net borrowing  $=$  DR(FCInv - Dep) + DR(WCInv)

$$
D R = D e b t r a t i o = \frac {D e b t}{A s s e t s}
$$

If company issues preferred shares:

$$
F C F F = C F O + I n t (1 - T a x R a t e) + P r e f e r e d d i v i d e n d s - F C I n v
$$

# Two-Stage Free Cash Flow Models

$$
F i r m v a l u e = \sum_ {t = 1} ^ {n} \frac {F C F F _ {t}}{(1 + W A C C) ^ {t}} + \frac {F C F F _ {n + 1}}{(W A C C - g)} \left[ \frac {1}{(1 + W A C C) ^ {n}} \right]
$$

$$
E q u i t y v a l u e = \sum_ {t = 1} ^ {n} \frac {F C F E _ {t}}{(1 + r) ^ {t}} + \frac {F C F E _ {n + 1}}{(r - g)} \bigg [ \frac {1}{(1 + r) ^ {n}} \bigg ]
$$

Value of Firm = Value of operating assets + Value of nonoperating assets

$$
(P V \text {o f} C F F)
$$

Learning Module 4 | Market-Based Valuation Price and Enterprise Value Multiples

Enterprise value, EV = Market value of common stock

+ Market value of preferred equity  
+ Market value of debt + Minority interest  
Cash and Short-term investments

<table><tr><td></td><td>Actual</td><td>Justified</td></tr><tr><td>Trailing P/E</td><td>Market price per share/EPS over previous 12 months</td><td>(1-b)(1+g)/r-g</td></tr><tr><td>Leading P/E</td><td>Market price per share/Forecasted EPS over next 12 months</td><td>1-b/r-g</td></tr><tr><td>P/B</td><td>Market price per share/Book value per share</td><td>ROE-g/r-g
Video:https://youtu.be/c0vmCUtDpZs</td></tr><tr><td>P/S</td><td>Market price per share/Sales per share</td><td>V0/S0=E0/S0×(1-b)(1+g)/r-g or V1/S1=E1/S1×1-b/r-g</td></tr><tr><td>Trailing D/P</td><td>4 × Most recent quarterly dividendMarket price per share</td><td>r - g/1 + g</td></tr><tr><td>Leading D/P</td><td>Forecast dividends over the next yearMarket price per share</td><td>r - g</td></tr><tr><td>Earnings yield</td><td>EPS/Price per share</td><td>r - g/(1 - b)(1 + g)</td></tr></table>

Underlying Earnings = Net income - non recurring gains + non recurring loss

# Normalized Earnings

Method 1: Average EPS Approach

$$
\text {N o r m a l i z e d E P S} = \frac {1}{n} \sum_ {i = 1} ^ {n} E P S _ {i}
$$

Method 2: Average ROE Approach

$$
\text {N o r m a l i z e d E P S} = \frac {1}{n} \sum_ {i = 1} ^ {n} R O E _ {i} \times C u r r e n t B o o k v a l u e p e r s h a r e
$$

Price-to-Earnings Growth (PEG) Ratio

$$
P E G r a t i o = \frac {P / E r a t i o}{g (i n \%)}
$$

# Momentum Indicators

Earnings surprise = Reported EPS – Expected EPS

Reported EPS - Expected EPS Scaled earnings surprise  $\equiv$ $\sigma$  (Analyst forecast EPS)

Standardized unexpected earnings (SUE) =  $\frac{\text{Earnings Surprise}}{\sigma(\text{Earnings Surprise})}$

# Portfolio P/E

$$
W e i g h t e d h a r m o n i c m e a n = \frac {1}{\sum_ {i = 1} ^ {n} \frac {W _ {i}}{X _ {i}}}
$$

where:

$$
w _ {i} = \text {W e i g h t o f s t o c k} i \text {i n p o r t f o l i o}
$$

$$
X _ {i} = \mathrm {P} / \mathrm {E} \text {o f s t o c k} i
$$

# Economic Value Added (EVA)

$$
E V A _ {t} = E B I T _ {t} (1 - T) - \left(W A C C \times I n v e s t e d C a p i t a l _ {t - 1}\right)
$$

# Market Value Added (MVA)

$$
M V A _ {t} = M a r k e t v a l u e o f F i r m _ {t} - I n v e s t e d C a p i t a l _ {t}
$$

# Residual Income, RI

$$
R I _ {t} = E _ {t} - (r \times B _ {t - 1}) = (R O E - r) \times B _ {t - 1}
$$

# Residual Income Model

$$
V _ {0} = B _ {0} + \left[ \frac {R I _ {1}}{(1 + r) ^ {1}} + \frac {R I _ {2}}{(1 + r) ^ {2}} + \frac {R I _ {3}}{(1 + r) ^ {3}} + \dots \right]
$$

Video: https://youtu.be/O0KTBkEtP9M

# Single-stage residual income valuation model

$$
V _ {0} = B _ {0} + \frac {(R O E - r) \times B _ {0}}{r - g} = B _ {0} + \frac {R I _ {1}}{r - g}
$$

Video: https://youtu.be/82GJu5umrB0

# Tobin's Q

$$
T o b i n ^ {\prime} s Q = \frac {M a r k e t v a l u e o f d e b t + M a r k e t v a l u e o f e q u i t y}{R e p l a c e m e n t c o s t o f t o t a l a s s e t s}
$$

# Continuing Residual Income

$$
V _ {0} = B _ {0} + \sum_ {t = 1} ^ {T - 1} \frac {R I _ {t}}{(1 + r) ^ {t}} + \frac {R I _ {T}}{(1 + r - \omega) (1 + r) ^ {T - 1}} \qquad \qquad 0 \leq \omega \leq 1
$$

$\omega =$  Persistence factor

If Rl declines to Long-run level in mature industry, with premium over book value

$$
V _ {0} = B _ {0} + \sum_ {t = 1} ^ {T} \frac {R I _ {t}}{(1 + r) ^ {t}} + \frac {P _ {T} - B _ {T}}{(1 + r) ^ {T}}
$$

Video: https://youtu.be/vhRW3q70E0w

Clean surplus relationship:

$$
B _ {t} = B _ {t - 1} + E _ {t} - D i v _ {t}
$$

# Capitalized Cash Flow Method (CCM)

$$
F i r m v a l u e = \frac {F C F F _ {1}}{W A C C - g} = \frac {F C F F _ {0} (1 + g)}{W A C C - g} \rightarrow E q u i t y v a l u e = \frac {F i r m v a l u e - M a r k e t v a l u e}{o f D e b t}
$$

$$
F i r m v a l u e = \frac {E B I T _ {1} (1 - t) (1 - R I R)}{W A C C - g}
$$

$$
R e i n v e s t m e n t r a t e, R I R = \frac {g}{W A C C}
$$

$$
E q u i t y v a l u e = \frac {F C F E _ {0} (1 + g)}{r - g}
$$

# Excess Earnings Method (EEM)

$$
\begin{array}{c} \text {E x c e s s} \\ \text {e a r n i n g s} \end{array} = \begin{array}{c} \text {N o r m a l i z e d} \\ \text {e a r n i n g s} \end{array} - \left(\text {W o r k i n g C a p i t a l} \times r _ {W C}\right) - \left(\text {F i x e d A s s e t s} \times r _ {F A}\right)
$$

$$
\begin{array}{c} V a l u e o f t h e i n t a n g i b l e a s s e t s \\ (R e s i d u a l v a l u e) \end{array} = \frac {(E x c e s s E a r n i n g s) _ {0} (1 + g)}{r _ {R I} - g}
$$

Value of the firm = Working capital + Fixed assets + Intangible Assets

where:

$$
g = \text {G r o w t h}
$$

$$
r _ {R I} = \text {R e q u i r e d r e t u r n o n i n t a n g l i b e a s s e t s}
$$

Video: https://youtu.be/137ga1xgAbA

# Discount for Lack of Control and Marketability

Discount for Lack of Control (DLOC)

$$
D L O C = 1 - \frac {1}{1 + C o n t r o l p r e m i u m}
$$

Total discount  $= 1 - (1 - \text{DLOC})(1 - \text{DLOM})$

$$
D L O M = \frac {V a l u e o f A T M o p t i o n}{S h a r e p r i c e}
$$

where Strike price is based on forward price,  $F = S_{0}e^{r_{f}\times T}$

# Levered and Unlevered Beta

Given the beta of a comparable company  $(\beta_{levered})$ , the unlevered beta:

$$
\beta_ {u n l e v e r e d} = \frac {\beta_ {l e v e r e d}}{\left[ 1 + \left(1 - t _ {p l c}\right) \left(\frac {D e b t _ {p l c}}{E q u i t y _ {p l c}}\right) \right]}
$$

The beta of the private company  $(\beta_{levered}^{*})$

$$
\beta_ {l e v e r e d} ^ {*} = \beta_ {u n l e v e r e d} \left[ 1 + \left(1 - t _ {p v t}\right) \left(\frac {D e b t _ {p v t}}{E q u i t y _ {p v t}}\right) \right]
$$

Learning Module 1 | The Term Structure and Interest Rate Dynamics

Forward Pricing Model

$$
D F _ {B} = D F _ {A} \times F _ {A, B - A}
$$

where:

$$
D F _ {B} = \frac {1}{(1 + z _ {B}) ^ {B}}
$$

$$
F _ {A, B - A} = \frac {1}{\left(1 + f _ {A , B - A}\right) ^ {B - A}}
$$

Forward Rate Model

$$
(1 + z _ {B}) ^ {B} = (1 + z _ {A}) ^ {A} \left(1 + f _ {A, B - A}\right) ^ {B - A}
$$

where:

$$
z _ {B} = \text {S p o t r a t e f o r p e r i o d} B
$$

$f_{A,B - A} = (B - A)$  forward rate that starts in period  $A$

Calculating spot rate from one-period forward rates

$$
z _ {T} = \left[ (1 + z _ {1}) \big (1 + f _ {1, 1} \big) \big (1 + f _ {2, 1} \big) \dots \big (1 + f _ {T - 1, 1} \big) \right] ^ {1 / T} - 1
$$

Boostrapping Spot Rates From Par Rates

Video: https://youtu.be/-FnweFO172Q

Fixed swap rate

$$
s _ {T} = \frac {1 - D F _ {T}}{\sum_ {t = 1} ^ {T} D F _ {t}} = \frac {1 - D i s c o u n t F a c t o r o f L a s t P a y m e n t}{S u m o f D i s c o u n t F a c t o r s}
$$

Swap spread = YTM of swap rate - YTM of government bond (same maturity)

TED spread = LIBOR - YTM of T-bill (same maturity)

LIBOR-OIS spread = LIBOR - OIS Fixed rate

For Parallel shifts in yield curve:

$$
\% \Delta P V = - M o d D u r \times \Delta Y T M \quad \Delta P V = - M o d D u r \times \Delta Y T M \times P V _ {0}
$$

$$
\% \Delta P V = - E f f D u r \times \Delta C u r v e \quad \Delta P V = - E f f D u r \times \Delta C u r v e \times P V _ {0}
$$

Non-parallel shifts (i.e. change in slope or curvature):

$$
\% \Delta P V = - K e y R a t e D u r a t i o n \times \Delta K e y R a t e
$$

# Bond Risk Premium

$$
B o n d r i s k p r e m i u m = \begin{array}{c} Y i e l d o f d e f a u l t f r e e \\ l o n g t e r m b o n d \end{array} - \begin{array}{c} Y i e l d o f d e f a u l t f r e e \\ s h o r t t e r m b o n d \end{array}
$$

Learning Module 2 | The Arbitrage-Free Valuation Framework

# Arbitrage-free Value of Bond

$$
V _ {0} = \frac {C}{(1 + z _ {1}) ^ {1}} + \frac {C}{(1 + z _ {2}) ^ {2}} + \dots + \frac {F V + C}{(1 + z _ {n}) ^ {n}}
$$

where:

$z_{n} =$  Spot rate for period  $n$

# Backward Induction Valuation Methodology

$$
B o n d v a l u e a t a n y n o d e = \frac {(0 . 5 \times V _ {H} + 0 . 5 \times V _ {L}) + C}{1 + i}
$$

where:

$V_{H} =$  bond's value if the higher forward rate is realized one year hence

$V_{L} =$  bond's value if the lower forward rate is realized one year hence

$C =$  coupon payment that is not dependent on interest rates

Video (Backward Induction Valuation): https://youtu.be/DhAVQ3hIXIQ

Video (Backward Induction with Financial Calculator): https://youtu.be/FycX2UwJxCM

Video (Pathwise Valuation): https://youtu.be/3oM-220oi7o

# Binomial Interest Rate Tree

$$
i _ {1, H} = i _ {1, L} e ^ {2 \sigma}
$$

$$
i _ {2, H H} = i _ {2, L L} e ^ {4 \sigma} \qquad \qquad i _ {2, H L} = i _ {2, L L} e ^ {2 \sigma}
$$

$$
i _ {3, H H H} = i _ {3, L L L} e ^ {6 \sigma} \qquad \qquad i _ {3, H H L} = i _ {3, L L L} e ^ {4 \sigma} \qquad i _ {3, L L H} = i _ {3, L L L} e ^ {2 \sigma}
$$

# Equilibrium Term Structure Models

# Cox-Ingersoll-Ross (CIR) Model

$$
d r = k (\theta - r _ {t}) d t + \sigma \sqrt {r _ {t}} d z
$$

# Vasicek Model

$$
d r = k (\theta - r _ {t}) d t + \sigma d z
$$

where:

$$
\begin{array}{l} k = \text {S p e e d o f} (> 0) \\ \theta = \text {L o n g - r u n i n t e r e s t r a t e} \\ \sigma = \text {I n t e r s t r a t e v o l a t i l i t y} \\ \end{array}
$$

# Arbitrage Free Models

# Ho-Lee Model

$$
d r _ {t} = \theta_ {t} d t + \sigma d z _ {t}
$$

# Kalotay-Williams-Fabozzi (KWF) Model

$$
d (\ln r _ {t}) = \theta_ {t} d t + \sigma d z _ {t}
$$

where:

$\theta_{t} =$  Time-dependent drift term

Learning Module 3 | Valuation and Analysis - Bonds with Embedded Options

# Callable and Putable Bonds

Value of callable bond = Value of straight bond - Value of issuer call option

Value of putable bond = Value of straight bond + Value of investor put option

Video (Valuing a callable bond): https://youtu.be/lWLSodiqZaM

Video (Valuing a putable bond): https://youtu.be/qmUnAtpXIAg

Effectiveduration  $= \frac{(PV_{-}) - (PV_{+})}{2\times(\Delta Curve)\times PV_{0}}$

Effectivcconvexity  $= \frac{(PV_{-}) + (PV_{+}) - 2\times PV_{0}}{PV_{0}\times(\Delta Curve)^{2}}$

# Capped and Floored Floaters

Value of capped floater = Value of straight floater - Value of cap

Value of floored floater  $=$  Value of straight floater + Value of floor

Video (Valuing a capped floater): https://youtu.be/d4LNMdXV9vU

Video (Valuing a floored floater): https://youtu.be/YJZU0THHBNE

# Convertible Bonds

$$
\begin{array}{c} \text {C o n v e r s i o n} \\ \text {v a l u e} \end{array} = \begin{array}{c} \text {U n d e r l y i n g} \\ \text {s h a r e p r i c e} \end{array} \times \begin{array}{c} \text {C o n v e r s i o n} \\ \text {r a t i o} \end{array}
$$

$$
\begin{array}{c} \text {M i n i m u m v a l u e} \\ \text {o f c o n v e r t i b l e b o n d} \end{array} = \mathbf {M a x} \left[ \begin{array}{c} \text {C o n v e r s i o n , V a l u e o f u n d e r l y i n g} \\ \text {v a l u e , S t r a i g h t b o n d} \end{array} \right]
$$

$$
\frac {\text {M a r k e t c o n v e r s i o n}}{\text {p r i c e}} = \frac {\text {C o n v e r t i b l e b o n d p r i c e}}{\text {C o n v e r s i o n r a t i o}}
$$

$$
\begin{array}{c} M a r k e t c o n v e r s i o n \\ p r e m i u m p e r s h a r e \end{array} = \begin{array}{c} M a r k e t c o n v e r s i o n \\ p r i c e \end{array} - \begin{array}{c} U n d e r l y i n g s h a r e \\ p r i c e \end{array}
$$

$$
\frac {\text {M a r k e t c o n v e r s i o n}}{\text {p r e m i u m r a t i o}} = \frac {\text {M a r k e t c o n v e r s i o n p r e m i u m p e r s h a r e}}{\text {U n d e r l y i n g s h a r e p r i c e}}
$$

$$
\frac {P r e m i u m o v e r}{S t r a i g h t v a l u e} = \frac {C o n v e r t i b l e b o n d p r i c e}{S t r a i g h t v a l u e} - 1
$$

# Convertible Bond (With No Additional Options)

$$
\underset {c o n v e r t i b l e b o n d} {V a l u e o f} = \underset {s t r a i g h t b o n d} {V a l u e o f} + \underset {i s s u e r ^ {\prime} s s t o c k} {V a l u e o f c a l l}
$$

# Callable Convertible Bond

$$
\underset {c o n v e r t i b l e b o n d} {V a l u e o f} = \underset {s t r a i g h t b o n d} {V a l u e o f} + \underset {i s s u e r ^ {\prime} s s t o c k} {V a l u e o f c a l l} - \underset {o p t i o n} {V a l u e o f}
$$

# ifiable Convertible Bond

$$
\underset {c o n v e r t i b l e b o n d} {V a l u e o f} = \underset {s t r a i g h t b o n d} {V a l u e o f} + \underset {i s s u e r ^ {\prime} s s t o c k} {V a l u e o f c a l l} + \underset {o p t i o n} {V a l u e o f}
$$

$G$ -spread  $= YTM$  of Corporate bond - YTM of Government bond

$$
\underset {d e f a u l t} {L o s s g i v e n} = \underset {e x p o s u r e} {E x p e c t e d} \times \left(1 - \underset {r a t e} {R e c o v e r y}\right)
$$

$$
\begin{array}{c} L o s s \\ s e v e r i t y \end{array} = 1 - \frac {R e c o v e r y}{r a t e}
$$

Expected Loss  $=$  Probability of Default  $\times$  Loss Given Default

Fair value of credit risky bond  $= \frac{\text{Fair value of bond}}{\text{assuming no default}} - \frac{\text{Credit Valuation}}{\text{Adjustment}}$

Credit valuation adjustment,  $CVA = \sum_{t=1}^{n} \frac{EL_t}{(1 + rf_t)^t} = \sum_{t=1}^{n} \frac{POD_t \times LGD_t}{(1 + rf_t)^t}$

where:

$EL_{t} =$  Expected loss of bond at time  $t$

$POD_{t} = \text{Probability of default of bond at time } t$

$LGD_{t} =$  Loss given default at time  $t = Expected\,Exposure_{t} - Recovery_{t}$

$rf_{t} =$  Risk-free rate at time  $t$

$n =$  Bond's remaining tenor

PV of expected loss for period  $t = \frac{EL_t}{(1 + rf_t)^t}$

$POD_{t} = (1 - Hazard rate)^{t - 1} \times Hazard rate$

Approximation of credit spread  $\approx$  Annual hazard rate  $\times$  (1 - Recovery rate)

Video (Probability of Default): https://youtu.be/e7K4x48Eg4U

Video (Valuing a Credit Risky Bond – Zero Interest Rate Volatility):

https://youtu.be/2l9bgu-o7al

Video (YTM of Corporate Bonds – Default and Non-Default):

https://youtu.be/K253Y7c2Yto

Expected percentage price change of a corporate bond

$$
\sum \text {Probability of credit migration} \times \% \Delta P
$$

where:

$$
\% \Delta P = -ModDur \times \Delta credit spread
$$

# Structural Model

$$
A _ {t} = D (t, T) + S _ {t}
$$

<table><tr><td>In terms of…</td><td>Call options</td><td>Put options</td></tr><tr><td>Equity</td><td>E(T) = Max[A(T) − K, 0]</td><td>E(T) = A(T) − K + Max[K − A(T), 0]</td></tr><tr><td>Debt</td><td>D(T) = A(T) − Max[A(T) − K, 0]</td><td>D(T) = K − Max[K − A(T), 0]</td></tr></table>

where:

$S_{t} =$  Equity value at time  $t$

$A_{T} =$  Asset value at time  $T$

$K =$  Face value of debt

# Learning Module 5 | Credit Default Swaps

CDS spread  $\approx$  (1 - Recovery Rate)  $\times$  POD

CDS payout amount = Payout ratio × Notional  
$= (1 -$  Recovery rate of CTD bond)  $\times$  Notional

Upfront payment = PV of protection leg - PV of premium leg

Upfront  $= \frac{PV\ of}{Credit\ Spread} - \frac{PV\ of}{Fixed\ Coupon}$  premium

$$
\approx \binom {C r e d i t} {S p r e a d} - \frac {F i x e d}{C o u p o n}) \times C D S D u r a t i o n
$$

Price of CDS per 100 notional  $= 100 -$  Upfront premium

$\%$  Change in  $CDS \, price = \frac{Change \, in}{spread \, in \, bps} \times Duration$

# VOLUME 7: DERIVATIVES

Learning Module 1 | Pricing and Valuation of Forward Commitments

# Forward Contracts

# Forward Pricing:

$$
F _ {0} = S _ {0} (1 + r) ^ {T}
$$

$$
F _ {0} = \left(S _ {0} + C C _ {0} - C B _ {0}\right) (1 + r) ^ {T}
$$

$$
F _ {0} = S _ {0} e ^ {r _ {c} T}
$$

$$
F _ {0} = S _ {0} e ^ {(r _ {c} + C C - C B) T}
$$

where:

$S_0 =$  Current spot price

$F_{0} =$  Forward price (set today)

$r =$  Annually compounded risk-free rate

$r_c =$  Continuously compounded risk-free rate

$CC_0 = \mathrm{PV}$  of Carry cost

$CB_{0} = \mathrm{PV}$  of carry benefits

$CC =$  Continuously compounded cost of carry

$CB =$  Continuously compounded carry benefit

# Forward Valuation (Long Position):

$$
V _ {0} = 0
$$

$$
V _ {t} = \frac {F _ {t} - F _ {0}}{(1 + r) ^ {T - t}} = S _ {t} - \frac {F _ {0}}{(1 + r) ^ {T - t}}
$$

$$
V _ {T} = S _ {T} - F _ {0}
$$

# Forward Rate Agreement (FRA)

$\textbf{Long FRA payoff at expiration of FRA} = \frac{\text { Notional } \times (L_{m} - FRA_{0}) \times t_{m}}{1 + D_{m} t_{m}}$

$$
F R A _ {0} = \left(\frac {1 + L _ {T} t _ {T}}{1 + L _ {h} t _ {h}} - 1\right) \left(\frac {1}{t _ {m}}\right)
$$

Valuation at time  $t = g$  (prior to FRA expiration):

$$
V a l u e o f L o n g F R A a t g = \frac {N o t i o n a l \times (F R A _ {g} - F R A _ {0}) \times t _ {m}}{1 + D _ {T - g} t _ {T - g}}
$$

where:

$D_{m} =$  Discount rate for  $m$  periods at  $t = h$

$h =$  FRA tenor

$m =$  Tenor of the underlying rate

$T = h + m =$  Maturity of underlying instrument

Video (Pricing an FRA): https://youtu.be/uBmAt_z9f3Y

Video (Valuing an FRA): https://youtu.be/AYKRVdaYvxY

# Fixed Income Forwards and Futures

Pricing:

$$
\begin{array}{l} F _ {0} = \begin{array}{c} Q u o t e d f u t u r e s \\ p r i c e \end{array} \times \begin{array}{c} C o n v e r s i o n \\ f a c t o r \end{array} \\ = F V \left(B _ {0} + A I _ {0}\right) - A I _ {T} - F V C I \\ \end{array}
$$

Valuation for fixed income forward contracts:

$V_{t} =$  Present value of difference in forward prices

$$
= P V \left[ F _ {t} - F _ {0} \right]
$$

Valuation for fixed income futures contracts:

$V_{t} =$  Price change since previous day's settlement

where:

$B_{0} =$  Quoted bond price

$AI = \frac{Number\ of\ accrued\ days\ since\ last\ coupon\ payment}{Total\ days\ during\ the\ coupon\ payment\ period}\times \frac{Annual\ coupon}{Coupon\ frequency}$

# Interest Rate Swaps (IRS)

# Fixed Swap Rate

$$
r _ {F I X} = \frac {1 - P V _ {n}}{\sum_ {i = 1} ^ {n} P V _ {i}} \times \frac {1}{A P}
$$

where:

$$
P V _ {i} = \frac {1}{1 + S p o t r a t e _ {i} \left(\frac {D a y s t o M a t u r i t y _ {i}}{3 6 0}\right)}
$$

$AP =$  Accrual period (i.e., payment frequency of swap)

# Fixed Swap Cash Flow

$$
F S = A P \times r _ {F I X}
$$

Pay-fixed, receive-floating IRS

$$
V a l u e o f S w a p = N o t i o n a l \times (F S _ {t} - F S _ {\mathbf {0}}) \sum_ {i = 1} ^ {n} P V _ {i}
$$

Receive-fixed, pay-floating IRS

$$
V a l u e o f S w a p = N o t i o n a l \times (F S _ {0} - F S _ {t}) \sum_ {i = 1} ^ {n} P V _ {i}
$$

Video (Pricing an Interest Rate Swap): https://youtu.be/0QvtKZutr5E

Video (Valuing an Interest Rate Swap): https://youtu.be/ A2a909etvg

# Currency Swap

Pricing for fixed leg of currency swap in currency  $a$  and  $b$

$$
r _ {a} = \frac {1 - P V _ {n , a}}{\sum_ {i = 1} ^ {n} P V _ {i , a}} \times \frac {1}{A P}
$$

$$
r _ {b} = \frac {1 - P V _ {n , b}}{\sum_ {i = 1} ^ {n} P V _ {i , b}} \times \frac {1}{A P}
$$

Fixed Cash Flows

$$
F S _ {a} = A P \times r _ {a}
$$

$$
F S _ {b} = A P \times r _ {b}
$$

Value of a fixed-for-fixed currency swap (Receive currency  $a$ , Pay currency  $b$ )

$$
V _ {C S} (i n c u r r e n c y a) = N o t i o n a l _ {a} \times V _ {a} - S _ {t} \times N o t i o n a l _ {b} \times V _ {b}
$$

$$
V _ {C S} (i n c u r r e n c y b) = \frac {1}{S _ {t}} \times N o t i o n a l _ {a} \times V _ {a} - N o t i o n a l _ {b} \times V _ {b}
$$

Value of a fixed-for-fixed currency swap (Receive currency  $b$ , Pay currency  $a$ )

$$
V _ {C S} (i n c u r r e n c y a) = S _ {t} \times N o t i o n a l _ {b} \times V _ {b} - N o t i o n a l _ {a} \times V _ {a}
$$

$$
V _ {C S} (i n c u r r e n c y b) = N o t i o n a l _ {b} \times V _ {b} - \frac {1}{S _ {t}} \times N o t i o n a l _ {a} \times V _ {a}
$$

where:

$$
V _ {a} = F S _ {a} \sum_ {i = 1} ^ {n} P V _ {i, a} + P V _ {n, a} \times P a r _ {a} = V a l u e o f c u r r e n c y a l e g
$$

$$
V _ {b} = F S _ {b} \sum_ {i = 1} ^ {n} P V _ {i, b} + P V _ {n, b} \times P a r _ {b} = V a l u e o f c u r r e n c y b l e g
$$

$S_{t} =$  Spot exchange rate at time  $t$  (quoted as  $a / b$ )

Video (Pricing a currency swap): https://youtu.be/XZlxcVByc00

Video (Valuing a currency swap): https://youtu.be/3h4mElS48aA

# Equity Swap

Value of equity swap (receive fixed-rate, pay equity return)

$$
V _ {E Q, t} = V _ {F I X} (C _ {0}) - \frac {S _ {t}}{S _ {t - 1}} \times N o t i o n a l - P V _ {t} (P a r - N o t i o n a l)
$$

$$
\text {V a l u e o f E q u i t y L e g} = \frac {S _ {t}}{S _ {t - 1}} \times \text {N o t i o n a l}
$$

Cash flow for equity leg = Notional  $\times$  Periodic equity return

where:

$V_{FIX}(C_0) = \text{Value at time } t$  of a fixed-rate bond initiated with coupon  $C_0$  at Time 0

$S_{t} =$  Current equity index level (on the valuation date)

$S_{t - 1} =$  Equity index level at last reset date

# Hedge Ratio

$$
h _ {c a l l} = \frac {c ^ {+} - c ^ {-}}{S ^ {+} - S ^ {-}} \geq 0
$$

$$
h _ {p u t} = \frac {p ^ {+} - p ^ {-}}{S ^ {+} - S ^ {-}} \leq 0
$$

# No-arbitrage Approach:

$$
c = h _ {c a l l} S + P V (- h _ {c a l l} S ^ {+} + c ^ {+}) = h _ {c a l l} S + P V (- h _ {c a l l} S ^ {-} + c ^ {-})
$$

$$
p = h _ {p u t} S + P V \bigl (- h _ {p u t} S ^ {+} + p ^ {+} \bigr) = h _ {p u t} S + P V \bigl (- h _ {p u t} S ^ {-} + p ^ {-} \bigr)
$$

# Expectations Approach:

$$
\pi = \frac {(1 + r) - d}{u - d}
$$

where:

$$
u = \cup p f a c t o r
$$

$$
d = \text {D o w n f a c t o r}
$$

$$
r = \text {R i s k - f r e e r a t e}
$$

# One-period Binomial Model

$$
c = \frac {\pi c ^ {+} + (1 - \pi) c ^ {-}}{1 + r}
$$

$$
p = \frac {\pi p ^ {+} + (1 - \pi) p ^ {-}}{1 + r}
$$

where:

$\pi =$  Risk-neutral probability of an up-move

Note: For interest rate options,  $\pi = 0.5$  and discount expected option payoff using the 1-period forward rates.

Video (Valuing interest rate options): https://youtu.be/X4R8j_cf8SA

# Two-period Binomial Model:

$$
c = \frac {\pi^ {2} c ^ {+ +} + 2 \pi (1 - \pi) c ^ {+ -} + (1 - \pi) ^ {2} c ^ {- -}}{(1 + r) ^ {2}}
$$

$$
p = \frac {\pi^ {2} p ^ {+ +} + 2 \pi (1 - \pi) p ^ {+ -} + (1 - \pi) ^ {2} p ^ {- -}}{(1 + r) ^ {2}}
$$

For 2-period American-styled call option with dividend in  $t = 1$ :

$$
S ^ {+} = u \times (S - P V o f d i v i d e n d s a t r i s k f r e e r a t e)
$$

$$
S ^ {-} = d \times (S - P V o f d i v i d e n d s a t r i s k f r e e r a t e)
$$

Video: https://youtu.be/U_XklZjJIAU

# Black-Scholes Option Pricing Model

$$
c = S N \left(d _ {1}\right) - X e ^ {- r T} N \left(d _ {2}\right)
$$

$$
p = X e ^ {- r T} N (- d _ {2}) - S N (- d _ {1})
$$

$$
d _ {1} = \frac {\ln \left(\frac {S}{X}\right) + \left(r + \frac {1}{2} \sigma^ {2}\right) T}{\sigma \sqrt {T}}
$$

$$
d _ {2} = d _ {1} - \sigma \sqrt {T}
$$

Put-call parity:  $p + S = c + Xe^{-rT}$

- Hedge ratio for calls  $= N\left( {d}_{1}\right)$  
- Probability that the call option expires in the money  $= N\left( {d}_{2}\right)  = \operatorname{Prob}\left( {{S}_{T} > X}\right)$  
- Hedge ratio for puts  $= N\left( {d}_{1}\right)  - 1 =  - N\left( {-{d}_{1}}\right)$  
- Probability that the put option expires in the money  $= 1 - N\left( {d}_{2}\right)$

$$
\operatorname {P r o b} \left(S _ {T} <   X\right) = N \left(- d _ {2}\right)
$$

# BSM model with carry benefits

$$
c = S e ^ {- \gamma T} N \left(d _ {1}\right) - X e ^ {- r T} N \left(d _ {2}\right)
$$

$$
p = X e ^ {- r T} N (- d _ {2}) - S e ^ {- \gamma T} N (- d _ {1})
$$

$$
d _ {1} = \frac {\ln \left(\frac {S}{X}\right) + \left(r - \gamma + \frac {1}{2} \sigma^ {2}\right) T}{\sigma \sqrt {T}}
$$

$$
d _ {2} = d _ {1} - \sigma \sqrt {T}
$$

Put-call parity:

$$
p + S e ^ {- \gamma T} = c + X e ^ {- r T}
$$

# Black Option Valuation Model

# European Options on Futures

$$
c = e ^ {- r T} \left[ F _ {0} (T) N \left(d _ {1}\right) - X N \left(d _ {2}\right) \right]
$$

$$
c = e ^ {- r T} \left[ X N \left(- d _ {2}\right) - F _ {0} (T) N \left(- d _ {1}\right) \right]
$$

$$
d _ {1} = \frac {\ln \left[ \frac {F _ {0} (T)}{X} \right] + \frac {1}{2} \sigma^ {2} T}{\sigma \sqrt {T}}
$$

$$
d _ {2} = d _ {1} - \sigma \sqrt {T}
$$

Put-call parity:

$$
c = e ^ {- r T} \left[ F _ {0} (T) - X \right] + p
$$

# Interest Rate Options

$$
c = (A P) e ^ {- r \left(t _ {j - 1} + t _ {m}\right)} \left[ F R A \left(0, t _ {j - 1}, t _ {m}\right) N \left(d _ {1}\right) - R _ {X} e ^ {- r T} N \left(d _ {2}\right) \right]
$$

$$
p = (A P) e ^ {- r \left(t _ {j - 1} + t _ {m}\right)} \left[ R _ {X} e ^ {- r T} N (- d _ {2}) - F R A \left(0, t _ {j - 1}, t _ {m}\right) N (- d _ {1}) \right]
$$

$$
d _ {1} = \frac {\ln \left[ \frac {F R A (0 , t _ {j - 1} , t _ {m})}{X} \right] + \left(\frac {1}{2} \sigma^ {2}\right) t _ {j - 1}}{\sigma \sqrt {t _ {j - 1}}}
$$

$$
d _ {2} = d _ {1} - \sigma \sqrt {t _ {j - 1}}
$$

# Payer Swaption

$$
P A Y _ {S W N} = A P \times [ R _ {F I X} N (d _ {1}) - R _ {X} N (d _ {2}) ] \times \sum_ {j = 1} ^ {n} P V _ {j} (1)
$$

# Receiver Swaption

$$
R E C _ {S W N} = A P \times [ R _ {X} N (- d _ {2}) - R _ {F I X} N (- d _ {1}) ] \times \sum_ {j = 1} ^ {n} P V _ {j} (1)
$$

$$
d _ {1} = \frac {\ln \left(\frac {R _ {F I X}}{R _ {X}}\right) + \left(\frac {1}{2} \sigma^ {2}\right) T}{\sigma \sqrt {T}}
$$

$$
d _ {2} = d _ {1} - \sigma \sqrt {T}
$$

Video (Interest Rate Options & Swaptions Equivalences:

https://youtu.be/uZQO50sEzso

Optimal Number of Hedging Units (for Delta Hedging)

$$
N _ {H} = - \frac {\text {P o r t f o l i o d e l t a}}{\text {D e l t a} _ {H}}
$$

Video: https://youtu.be/v8RcvkQKFpw

# Option Greeks

$$
D e l t a _ {c a l l} = e ^ {- \delta T} N (d _ {1})
$$

$$
D e l t a _ {p u t} = - e ^ {- \delta T} N (- d _ {1})
$$

where:

$\delta =$  Continuously compounded dividend yield

$$
G a m m a _ {c a l l} = G a m m a _ {p u t} = \frac {e ^ {- \delta T}}{S \sigma \sqrt {T}} N (d _ {1})
$$

$$
c = c _ {0} + D e l t a _ {c a l l} \times \varDelta S + \frac {1}{2} G a m m a _ {c a l l} \times (\varDelta S) ^ {2}
$$

$$
p = p _ {0} + D e l t a _ {p u t} \times \Delta S + \frac {1}{2} G a m m a _ {p u t} \times (\Delta S) ^ {2}
$$

Learning Module 1 | Introduction to Commodities and Commodity Derivatives

$$
\begin{array}{c} \text {F u t u r e s} \\ \text {p r i c e} \end{array} = \begin{array}{c} \text {S p o t p r i c e o f} \\ \text {p h y s i c a l c o m m o d i t y} \end{array} + \begin{array}{c} \text {S t o r a g e} \\ \text {c o s t s} \end{array} - \begin{array}{c} \text {C o n v e n i e n c e} \\ \text {y i e l d} \end{array}
$$

$$
\underset {s p r e a d} {C a l e n d a r} = \begin{array}{c c} N e a r t e r m & L o n g e r t e r m \\ f u t u r e s c o n t r a c t - f u t u r e s c o n t r a c t & \\ c l o s i n g p r i c e & c l o s i n g p r i c e \end{array}
$$

$$
P r i c e \: r e t u r n = \frac {\text {C u r r e n t p r i c e - P r e v i o u s p r i c e}}{\text {P r e v i o u s p r i c e}}
$$

$$
\text {R o l l r e t u r n} = \frac {\left( \begin{array}{c c} \text {N e a r t e r m} & \text {L o n g e r t e r m} \\ \text {f u t u r e s c o n t r a c t} - \text {f u t u r e s c o n t r a c t} \\ \text {c l o s i n g p r i c e} & \text {c l o s i n g p r i c e} \end{array} \right)}{\text {N e a r t e r m}} \times \frac {\text {P e r c e n t a g e o f t h e p o s i t i o n}}{\text {i n t h e f u t u r e s c o n t r a c t}}
$$

$$
\underset {r e t u r n} {T o t a l} = \underset {r e t u r n} {P r i c e} + \underset {r e t u r n} {R o l l} + \underset {r e t u r n} {C o l l a t e r a l} + \underset {r e t u r n} {R e b a l a n c i n g}
$$

Learning Module 2 | Overview of Types of Real Estate Investment

Net Operating Income

$$
N O I = \begin{array}{c} E f f e c t i v e g r o s s \\ i n c o m e \end{array} - \begin{array}{c} O p e r a t i n g \\ e x p e n s e s \end{array} - \begin{array}{c} P r o p e r t y m a i n t e n a n c e \\ a l l o w a n c e \end{array}
$$

$$
G r o s s \quad r e n t = B a s e \quad r e n t \times R e n t a b l e \quad a r e a
$$

$$
\text {O p e r a t i n g} = \text {R e c o v e r y} \times \text {R e n t a b l e}
$$

Loan-to-value ratio

$$
L T V = \frac {D e b t o u t s t a n d i n g}{P r o p e r t y v a l u e}
$$

Debt service coverage ratio

$$
D S C = \frac {N e t o p e r a t i n g i n c o m e}{D e b t s e r v i c e}
$$

$$
E q u i t y d i v i d e n d r a t e = \frac {P r e t a x c a s h f l o w}{P r o p e r t y p e p u r c h a s e p r i c e - M o r t g a g e l o a n}
$$

Pretax cash flow  $=$  Net operating income - Debt service

After tax cash flow  $=$  Pretax cash flow - Taxes

Where:  $Taxes = t \times (NOI - \text{Interest expense} - \text{Depreciation expense})$

Funds from Operations

$$
F F O = N e t i n c o m e + D e p r e c i a t i o n + A m o r t i z a t i o n - \frac {N e t g a i n s f r o m}{p r o p e r t y s a l e s}
$$

Gross potential rental income

$$
G P R I = M a r k e t \text {r e n t} \times \text {R e n t a b l e s p a c e}
$$

# Income Approach

# Direct Capitalization method

$$
P r o p e r t y v a l u e = \frac {E x p e c t e d N O I}{C a p i t a l i z a t i o n r a t e}
$$

where: Capitalization rate  $= r - g$

$$
r = \text {R e q u i r e d}
$$

$$
g = \text {C o n s t a n t g r o w t h r a t e}
$$

# Discounted Cash Flow (DCF) Methodology

$$
P r o p e r t y v a l u e = \sum_ {t = 1} ^ {n} \frac {N O I _ {t}}{(1 + r) ^ {t}} + \frac {T e r m i n a l v a l u e}{(1 + r) ^ {n}}
$$

$$
T e r m i n a l v a l u e = \frac {N O I _ {n} (1 + g)}{r - g}
$$

# Appraisal-based index

$$
R e t u r n = \frac {N O I - \frac {C a p i t a l}{E x p e n d i t u r e s} + \binom {E n d i n g} {m a r k e t v a l u e} - \frac {B e g i n n i n g}{m a r k e t v a l u e}}{B e g i n n i n g m a r k e t v a l u e}
$$

# Adjustment for Appraisal Lag

$$
R _ {t} = \frac {R _ {t} ^ {*}}{a} + \left(\frac {1 - a}{a}\right) R _ {t - 1} ^ {*}
$$

where:

$$
R _ {t} = \text {A c t u a l i n d e x r e t u r n}
$$

$$
R _ {t} ^ {*} = \text {A p p r a i s a l i n d e x}
$$

$$
R _ {t - 1} ^ {*} = \text {P r i o r p e r i o d ' s a p p r a i s a l i n d e x r e t u r n}
$$

$$
a = \text {S p e e d} a \text {S p e e d} a \text {S p e e d} a \text {S p e e d} a \text {S p e e d} a \text {S p e e d} a \text {S p e e d} a \text {S p e e d} a \text {S p e e d} a \text {S p e e d} a \text {S p e e d}
$$

# Net Asset Value Approach

$$
N A V p e r s h a r e = \frac {\text {V a l u e o f} + \text {V a l u e o f} - \text {T o t a l d e b t}}{\text {N u m b e r o f s h a r e s o u t s t a n d i n g}}
$$

If valuation of operating real estate is not provided:

$$
V a l u e o f o p e r a t i n g e s t a t e = \frac {N O I _ {1}}{C a p r a t e}
$$

Video: https://youtu.be/WncC3BZmfs8

$$
N O I = \frac {\text {G r o s s r e n t a l}}{\text {r e v e n u e}} - \frac {\text {E s t i m a t e d v a c a n c y a n d}}{\text {c o l l e c t i o n s l o s s}} - \frac {\text {O p e r a t i n g}}{\text {e x p e n s e s}}
$$

# Relative Value Approach

# Funds from Operations:

$$
F F O = N e t i n c o m e + D e p r e c i a t i o n + A m o r t i z a t i o n - \begin{array}{c} N e t g a i n s f r o m \\ p r o p e r t y s a l e s \end{array}
$$

# Adjusted Funds from Operations:

$$
A F F O = F F O - \frac {N o n c a s h}{r e n t} - \frac {R e c u r r i n g c a p i t a l}{e x p e n d i t u r e}
$$

# Two-Stage Dividend Discount Model

$$
\text {V a l u e} = P V \text {o f d i v i d e n d s} + P V \text {o f t e r m i n a l v a l u e}
$$

# Equity Market Neutral Pairs Trading

$$
\frac {\text {A m o u n t o f S h o r t P o s i t i o n}}{\text {i n O v e r v a l u e d S t o c k}} = - \frac {\text {B e t a o f u n d e r v a l u e d s t o c k} \times \text {A m o u n t I n v e s t e d}}{\text {B e t a o f o v e r v a l u e d s t o c k}}
$$

# Merger Arbitrage Strategy

For a stock-for-stock deal:

$$
\text {P a y o f f i f m e r g e r i s s u c c e s s f u l} = \left(N _ {A} \times P _ {A}\right) - \left(N _ {T} \times P _ {T}\right)
$$

where:

$$
\begin{array}{l} N _ {A} = \text {N u m b e r o f a c a i r i e r ’ s s h a r e s t o s h o r t s e l l} \\ P _ {A} = \text {S h a r e p r i c e o f a c q u i r e r p o s t a n n o u n c e m e n t} \\ N _ {T} = \text {N u m b e r o f t a r g e t ’ s s h a r e s t o b u y} \\ P _ {T} = \text {S h a r e p r i c e o f t a r g e t p o s t a n n o u c c e m e n t} \\ \end{array}
$$

# Convertible Arbitrage Strategy

$$
C o n v e r s i o n p r i c e = \frac {C o n v e r t i b l e b o n d p r i c e}{C o n v e r s i o n r a t i o}
$$

Conversion value = Share price × Conversion ratio

# Conditional Factor Risk Model

$$
\begin{array}{l} R _ {i, t} = \alpha_ {i} + \beta_ {i, 1} (F a c t o r 1) _ {t} + \beta_ {i, 2} (F a c t o r 2) _ {t} + \dots + \beta_ {i, K} (F a c t o r K) _ {t} + \\ + D _ {t} \beta_ {i, 1} (F a c t o r 1) _ {t} + D _ {t} \beta_ {i, 2} (F a c t o r 2) _ {t} + \dots + D _ {t} \beta_ {i, K} (F a c t o r K) _ {t} + (e r r o r) _ {i, t} \\ \end{array}
$$

where:

$$
\begin{array}{l} R _ {i, t} = \text {R e t u r n o f h e d g e f u n d i n p e r i o d} t \\ \beta_ {i, K} (F a c t o r K) _ {t} = \text {E x p o s u r e t o r i s k f a c t o r K f o r h e d g e f u n d i n p e r i o d t d u r i n g} \\ D _ {t} \beta_ {i, K} (F a c t o r K) _ {t} = I n c r e m e n t a l \text {e x p o s u r e t o r i s k f a c t o r} K \text {f o r h e d g e f u n d} i \text {i n p e r i o d} t \\ D _ {t} = \text {D u m m y v a r i a b l e t h a t e q u a l s 1 d u n i n g f i n a c i a l c r i s i s p e r i o d s (0 o t h e r w i s e)} \\ \alpha_ {i} = \text {I n t e r c e p t f o r h e d g e f u n d} i \\ (e r r o r) _ {i, t} = \text {R a n d o m e r r o r w i t h z e r o m e a n a n d s t a n d a r d d e v i a t i o n} \sigma_ {i} \\ \end{array}
$$

Learning Module 1 | Economics and Investment Markets

One-period real-risk free rate:

$$
l _ {t, 1} = \frac {1}{E _ {t} [ \widetilde {m} _ {t , 1} ]} - 1
$$

where:

$E_{t}\big[\widetilde{m}_{t,1}\big] =$  Inter-temporal rate of substitution

$$
P r i c e o f r i s k y a s s e t = \frac {E \left[ \tilde {P} _ {t + 1 , s - 1} \right]}{1 + l _ {t , 1}} + c o v _ {t} \left[ \tilde {P} _ {t + 1, s - 1}, \tilde {m} _ {t, 1} \right]
$$

where:

$\frac{E[\tilde{P}_{t+1,s-1}]}{1 + l_{t,1}} = \text{risk neutral present value}$

$cov_{t}\big[\widetilde{P}_{t + 1,s - 1},\widetilde{m}_{t,1}\big] =$  covariance between investor's inter-temporal rate of substitution and the random future price the investment at  $t + 1$ , based on the information available to investor today.

$s =$  time to maturity of investment

# Default-free nominal coupon-paying bond

$$
P _ {t} ^ {i} = \sum_ {s = 1} ^ {N} \frac {C F _ {t + s} ^ {i}}{(1 + l _ {t , s} + \theta_ {t , s} + \pi_ {t , s}) ^ {s}}
$$

where:

$l_{t,s} =$  Real-risk free rate

$\theta_{t,s} =$  Expected inflation rate

$\pi_{t,s} =$  Uncertainty in future inflation rate

$\theta_{t,s} + \pi_{t,s} =$  Breakeven rate of inflaton

# Short-dated nominal zero-coupon government bonds (e.g., T-bills)

$$
P _ {t} ^ {i} = \frac {C F _ {t + s} ^ {i}}{(1 + l _ {t , s} + \theta_ {t , s}) ^ {s}}
$$

# Taylor Rule

$$
p r _ {t} = I _ {t} + \pi_ {t} + 0. 5 \left(\pi_ {t} - \pi_ {t} ^ {*}\right) + 0. 5 \left(Y _ {t} - Y _ {t} ^ {*}\right)
$$

where:

$$
p r _ {t} = \text {p o l i c y r a t e}
$$

$I_{t} =$  level of real short-term interest rates that balance long-term savings and borrowing in the economy

$$
\pi_ {t} = \text {r a t e}
$$

$$
\pi_ {t} ^ {*} = \text {t a r g e t}
$$

$$
Y _ {t} = \text {l o g a r i t h m i c l e v e l o f a c t u a l G D P}
$$

$$
Y _ {t} ^ {*} = \text {l o g a r i t h m i c l e v e l o f p o t e n t i a l r e a l G D P}
$$

$$
Y _ {t} - Y _ {t} ^ {*} = \text {o u t p u t}
$$

# Corporate bond

$$
P _ {t} ^ {i} = \sum_ {s = 1} ^ {N} \frac {E _ {t} \big [ \widetilde {C F} _ {t + s} ^ {i} \big ]}{(1 + l _ {t , s} + \theta_ {t , s} + \pi_ {t , s} + \gamma_ {t , s}) ^ {s}}
$$

where:

$$
\gamma_ {t, s} = \text {C r e d i t p r e m i u m}
$$

# Equity

$$
P _ {t} ^ {i} = \sum_ {s = 1} ^ {\infty} \frac {E _ {t} \left[ \widetilde {C F} _ {t + s} ^ {i} \right]}{\left(1 + l _ {t , s} + \theta_ {t , s} + \pi_ {t , s} + \gamma_ {t , s} + \kappa_ {t , s}\right) ^ {s}}
$$

$$
P _ {t} ^ {i} = \sum_ {s = 1} ^ {\infty} \frac {E _ {t} \big [ \widetilde {C F} _ {t + s} ^ {i} \big ]}{(1 + l _ {t , s} + \theta_ {t , s} + \pi_ {t , s} + \lambda_ {t , s}) ^ {s}}
$$

where:

$$
\kappa_ {t, s} = \text {E q u i t y p r e m i u m r e l a t i v e t o r i s k y b o n d s}
$$

$$
\lambda_ {t, s} = \gamma_ {t, s} + \kappa_ {t, s} = \text {E q u i t y r i s k p r e m i u m}
$$

# Commercial Real Estate

$$
P _ {t} ^ {i} = \sum_ {s = 1} ^ {N} \frac {E _ {t} \big [ \widetilde {C F} _ {t + s} ^ {i} \big ]}{(1 + l _ {t , s} + \theta_ {t , s} + \pi_ {t , s} + \gamma_ {t , s} + \kappa_ {t , s} + \phi_ {t , s}) ^ {s}}
$$

where:

$$
\phi_ {t, s} = \text {l i q u i d i t y r i s k p r e m i u m}
$$

Active return,  $R_{A} = R_{P} - R_{B}$

$\text{Alpha}, \alpha_{p} = R_{p} - \beta_{p} R_{B}$

Value added,  $R_{A} = \sum_{j = 1}^{M}\Delta w_{j}R_{B,j} + \sum_{j = 1}^{M}w_{P,j}R_{A,j}$

$$
S R _ {P} ^ {2} = S R _ {B} ^ {2} + I R ^ {2}
$$

$$
\sigma^ {2} (R _ {P}) = \sigma^ {2} (R _ {B}) + \sigma^ {2} (R _ {A})
$$

For optimal Sharpe ratio,

$$
\sigma (R _ {A}) = \frac {I R}{S R _ {B}} \sigma (R _ {B})
$$

Transfer Coefficient,  $TC = Corr\left(\frac{\mu_i}{\sigma_i}, \Delta w_i \sigma_i\right)$

Information Coefficient,  $IC = \text{Corr}\left(\frac{R_{Ai}}{\sigma_i}, \frac{\mu_i}{\sigma_i}\right)$

$IC\approx 2(\text{Probability of right call}) - 1$

Forecasted active return,  $\mu_{i} = IC\times \sigma_{i}\times S_{i}$

where:  $S_{i}$  is set of standardized forecasts of expected returns across securities

Mean-variance optimal weights

$$
\Delta w _ {i} ^ {*} = \frac {\mu_ {i} \sigma_ {A}}{\sigma_ {i} ^ {2} I C \sqrt {B R}}
$$

Full Fundamental Law

$$
E (R _ {A}) = T C \times I C \sqrt {B R} \sigma_ {A}
$$

$$
I R = T C \times I C \sqrt {B R}
$$

$$
\sigma \left(R _ {A}\right) = T C \times \frac {I R ^ {*}}{S R _ {B}} \sigma \left(R _ {B}\right)
$$

$$
S R _ {P} ^ {2} = S R _ {B} ^ {2} + (T C) ^ {2} (I R ^ {*}) ^ {2}
$$

# Performance Measurement

$$
R _ {A} = E (R _ {A} | I C _ {R}) + N o i s e
$$

$TC^2 = \text{Proportion of variation in realized performance attributed to realized information coefficient}$

where:

$IC_{R} =$  realized information coefficient

# Ex-ante measurement of skill

$$
E (R _ {A}) = \frac {I C}{\sigma_ {I C}} \sigma_ {A}
$$

# Independence of Investment Decision

$$
B R = \frac {N}{1 + (N - 1) \rho}
$$

# Learning Module 3 | Exchange-Traded Funds: Mechanics and Applications

End-of-day ETF premium or discount  $(\%)$

$$
\frac {E T F p r i c e - N A V p e r s h a r e}{N A V p e r s h a r e}
$$

Intraday ETF premium or discount  $(\%)$

$$
\frac {E T F p r i c e - I n d i c a t e d N A V p e r s h a r e}{I n d i c a t e d N A V p e r s h a r e}
$$

$$
\text {Holding period cost} (\%) = \text {Round trip trade cost} (\%) + \text {Management fee} (\%)
$$

$$
Round \text {trip trade cost} \% = \text {One way commission} \% \times 2 + \text {Bid ask spread} \%
$$

# Arbitrage Pricing Theory (APT)

$$
E (R _ {p}) = R _ {F} + \lambda_ {1} \beta_ {p, 1} + \dots + \lambda_ {K} \beta_ {p, K}
$$

where:

$$
E \left(R _ {p}\right) = \text {t h e} p
$$

$$
R _ {F} = \text {t h e r i s k - f r e e r a t e}
$$

$$
\beta_ {p, j} = \text {t h e s e n s i t i v i t y o f t h e p o r t f o l i o t o f a c t o r} j
$$

$$
\lambda_ {j} = \text {t h e}
$$

$$
K = \text {t h e n u m b e r o f f a c t o r s}
$$

# Carhart Four-Factor Model

$$
E \left(R _ {p}\right) = R _ {F} + \beta_ {p, 1} R M R F + \beta_ {p, 2} S M B + \beta_ {p, 3} H M L + \beta_ {p, 4} W M L
$$

where:

$R M R F =$  Return on a value-weighted equity index minus one-month T-bill rate

SMB = small minus big; average return on three small-cap portfolios minus the

average return on three large-cap portfolios

HML = high minus low; average return on two high book-to-market portfolios minus

average return on two low book-to-market portfolios

WML = winners minus losers, a momentum factor; return on a portfolio of past year's

winners minus return on a portfolio of past year's losers.

# Macroeconomic Factor Model

$$
R _ {i} = a _ {i} + b _ {i 1} F _ {1} + b _ {i 2} F _ {2} + \dots + b _ {i K} F _ {K} + \varepsilon_ {i}
$$

where:

$$
F _ {k} = \text {t h e s u r p r i s e i n t h e f a c t o r} k
$$

$b_{ik} =$  the sensitivity of the return on asset  $i$  to a surprise in factor  $k, k = 1, 2, \ldots,$

$a_{i} =$  Expected return on the portfolio

# Fundamental Factor Model

$$
b _ {i k} = \frac {\mathrm {V a l u e o f a t t r i b u t e} k \mathrm {f o r a s s e t} i - \mathrm {A v e r a g e v a l u e o f a t t r i b u t e} k}{\sigma (\mathrm {V a l u e s o f a t t r i b u t e} k)}
$$

# Return Attribution

Active return  $= R_P - R_B$

$$
= \sum_ {k = 1} ^ {K} \left[ \binom {\text {P o r t f o l i o}} {\text {s e n s i t i v i t y}} _ {k} - \binom {\text {B e n c h m a r k}} {\text {s e n s i t i v i t y}} _ {k} \right] \times \binom {\text {F a c t o r}} {\text {r e t u r n}} _ {k} + \underset {\text {s e l e c t i o n}} {\text {S e c u r i t y}}
$$

Tracking error,  $TE = s(R_{P} - R_{B})$

Information ratio,  $IR = \frac{\bar{R}_P - \bar{R}_B}{s(R_P - R_B)}$

Active risk squared = Active factor risk + Active specific risk

Learning Module 5 | Measuring and Managing Market Risk

# Parametric VaR (Using Normal Distribution)

$$
V a r e p t o f l o i o V a l u e
$$

where:

$$
\begin{array}{l} E \left(R _ {p}\right) = \text {P o r t f o l i o} \\ \sigma_ {p} = \text {P o r t f o l i o s t a n d a r d d e v i a t i o n} \\ \end{array}
$$

# Two-asset portfolio:

$$
\begin{array}{l} E \left(R _ {p}\right) = w _ {1} E \left(R _ {1}\right) + w _ {2} E \left(R _ {2}\right) \\ \sigma_ {p} ^ {2} = w _ {1} ^ {2} \sigma_ {1} ^ {2} + w _ {2} ^ {2} \sigma_ {2} ^ {2} + 2 w _ {1} w _ {2} \rho_ {1, 2} \sigma_ {1} \sigma_ {2} \\ \end{array}
$$

Scaling from daily returns to annual returns (Assuming 1 year = 250 trading days):

$$
R _ {d a i l y} \times 2 5 0 t r a d i n g d a y s
$$

Scaling from daily standard deviation to annual standard deviaton:

$$
\sigma_ {d a i l y} \times \sqrt {2 5 0}
$$

Incremental VaR (IVaR) = VaR after change - VaR before change

Percentage change in bond price:

$$
{\frac {\Delta \mathrm {B}}{B}} \approx - D u r a t i o n {\frac {\Delta y}{1 + y}} + {\frac {1}{2}} C o n v e x i t y \left({\frac {\Delta y}{1 + y}}\right) ^ {2}
$$

New call price:  $c + \Delta c \approx c + \mathrm{Delta}_c(\Delta S) + \frac{1}{2} \mathrm{Gamma}_c(\Delta S)^2 + Vega_c(\Delta \sigma)$

New put price:  $p + \Delta p \approx p + \mathrm{Delta}_p(\Delta S) + \frac{1}{2} \mathrm{Gamma}_p(\Delta S)^2 + Vega_p(\Delta \sigma)$

Learning Module 6 | Backtesting and Simulation

No formula.

# CFA® Program

# Level III

# PRIVATE MARKETS PATHWAY

# FORMULA SHEET (2025) Version 1.0

Prepared by: Fabian Moa, CFA, FRM, CTP, FMVA, AFM, FSA Credential

![](images/84bcb19c7a8b33a0d4182dddad95e3e7c74524c0a3f0c3e7dffac337f9c1c007.jpg)

# FOR REFERENCE ONLY

# (Note: Formula Sheet is not provided in the CFA exam)

Follow us on:

YouTube

LinkedIn

# NOESIS EXED SDN BHD

Block VO2, Level 5, Unit 8, Lingkaran SV, Sunway Velocity, 55100 Kuala Lumpur, Malaysia

Website: www.noesis.edu.sg

# Table of Contents

Setting Up the Texas BA II Plus Financial Calculator 3

VOLUME 1 - ASSET ALLOCATION. 3

Learning Module 1: Capital Market Expectations, Part 1: Framework and Macro Considerations...3  
Learning Module 2: Capital Market Expectations, Part 2: Forecasting Asset Class Returns 4  
Learning Module 3: Overview of Asset Allocation. 9  
Learning Module 4: Principles of Asset Allocation 9  
Learning Module 5: Asset Allocation with Real-World Constraints. 10

VOLUME 2 - PORTFOLIO CONSTRUCTION. 11

Learning Module 1: Passive Equity Investing. 11  
Learning Module 2: Overview of Fixed Income Portfolio Management 11  
Learning Module 3: Asset Allocation to Alternative Investments 13  
Learning Module 4: Overview of Private Wealth Management. 13  
Learning Module 5: Portfolio Management for Institutional Investors 15  
Learning Module 6: Trading Costs and Electronic Markets 16  
Learning Module 7: Case Study in Portfolio Management: Institutional (SWF) 16

VOLUME 3 - PERFORMANCE MEASUREMENT 17

Learning Module 1: Portfolio Performance Evaluation 17  
Learning Module 2: Investment Manager Selection. 20  
Learning Module 3: Overview of the Global Investment Performance Standards. 21

VOLUME 4 - DERIVATIVES AND RISK MANAGEMENT 23

Learning Module 1: Option Strategies 23  
Learning Module 2: Swaps, Forwards, and Futures Strategies. 25  
Learning Module 3: Currency Management: An Introduction 27

PRIVATE MARKETS PATHWAY 29

Learning Module 1: Private Investments and Structures 29  
Learning Module 2: General Partner and Investor Perspectives and the Investment Process. 30  
Learning Module 3: Private Equity. 30  
Learning Module 4: Private Debt 31  
Learning Module 5: Private Special Situations. 33  
Learning Module 6: Private Real Estate Investments 34  
Learning Module 7: Infrastructure. 36

# CFA Level III – Formula Sheet (2025)

Setting Up the Texas BA II Plus Financial Calculator

Video: https://youtu.be/0MS8d8QOFmc

VOLUME 1 - ASSET ALLOCATION

Learning Module 1: Capital Market Expectations, Part 1: Framework and Macro Considerations

$$
\begin{array}{c} \text {A g g r e g a t e t r e n d} \\ \text {g r o w t h o f e c o n o m y} \end{array} = \begin{array}{c} \text {G r o w t h f r o m} \\ \text {l a b o r i n p u t s} \end{array} + \begin{array}{c} \text {G r o w t h f r o m} \\ \text {l a b o r p r o d u c t i v i t y} \end{array}
$$

where:

$$
\begin{array}{c} G r o w t h f r o m \\ \text {l a b o r i n p u t s} \end{array} = \begin{array}{c} G r o w t h i n p o t e n t i a l \\ \text {l a b o r f o r c e s i z e} \end{array} + \begin{array}{c} G r o w t h i n a c t u a l l a b o r \\ \text {f o r c e p a r t i c i p a t i o n} \end{array}
$$

$$
\begin{array}{c} G r o w t h f r o m \\ \text {l a b o r p r o d u c t i v i t y} \end{array} = \begin{array}{c} G r o w t h f r o m i n c r e a s i n g \\ \text {c a p i t a l i n p u t s} \end{array} + \begin{array}{c} G r o w t h i n t o t a l \\ \text {f a c t o r p r o d u c t i v i t y} \end{array}
$$

Aggregate market value of equity

$$
V _ {t} ^ {e} = G D P _ {t} \times S _ {t} ^ {k} \times P E _ {t}
$$

$$
E q u i t y \quad r e t u r n = C a p i t a l \quad a p p r e c i a t i o n + D i v i d e n d \quad y i e l d
$$

Over a finite horizon:

$$
Equity \text{return} = \% \Delta GDP_{t} + \% \Delta S_{t}^{k} + \% \Delta PE_{t} + \frac{\text{Dividend}}{\text{yield}}
$$

In the long-run:

$$
Equity \text{return} = \% \Delta GDP_{t} + \frac{\text{Dividend}}{\text{yield}}
$$

where:

$$
V _ {t} ^ {e} = \text {A g g r a g e m a t k e t v a l u e o f e q u i t y}
$$

$$
G D P _ {t} = \text {N o m i n a l l e v e l o f G D P}
$$

$$
S _ {t} ^ {k} = \text {S h a r e o f p r o f i t s i n t h e e c o n o m y} = \frac {E P S _ {t}}{G D P _ {t}}
$$

$$
P E _ {t} = P / E \text {r a t i o}
$$

$$
D i v i d e n d y i e l d = \frac {D i v i d e n d p a y o u t r a t i o}{P r o f i t m u l t i p l e}
$$

Taylor Rule (Video: https://youtu.be/Cl_SShKmOwA)

$$
i ^ {*} = r _ {n e u t r a l} + \pi_ {e} + 0. 5 \big (\hat {Y} _ {e} - \hat {Y} _ {t r e n d} \big) + 0. 5 (\pi_ {e} - \pi_ {t a r g e t})
$$

where:

$i^{*} =$  target nominal policy rate

$r_{\text{neutral}} = \text{real neutral policy rate}$

$\pi_{e} =$  expected inflation rate  $\pi_{target} =$  target inflation rate

$\hat{Y}_e =$  expected real GDP growth rates  $\hat{Y}_{trend} =$  trend real GDP growth rates

$i^{*} - \pi_{e} =$  real, inflation-adjusted policy rate

$$
X - M = (S - I) + (T - G)
$$

where:

$$
X - M = \text {N e t}
$$

$$
S = \text {S a v i n g s}
$$

$$
I = \text {I n v e s t m e n t}
$$

$$
T - G = \text {G o v e r n m e n t}
$$

Learning Module 2: Capital Market Expectations, Part 2: Forecasting Asset Class Returns

# Grinold-Kroner model

Expected equity return

$$
E (R _ {e}) \approx \frac {D}{P} + (\% \Delta E - \% \Delta S) + \% \Delta P / E
$$

where:

$\frac{D}{P} =$  Dividend yield

$\% \Delta E =$  Expected  $\%$  change in total earnings

= Expected nominal earnings growth return

$\% \Delta S =$  Expected  $\%$  change in shares outstanding ( $\% \Delta S < 0$ : Net share repurchases)

$\% \Delta P / E =$  Expected  $\%$  change in price-to-earnings ratio

$=$  Expected repricing return

$\% \Delta E - \% \Delta S =$  Growth rate of earnings per share

$\frac{D}{P} - \% \Delta S =$  Expected cash flow ("income") return

$\% \Delta E + \% \Delta P / E =$  Expected capital gains

In the long run,  $\% \Delta E =$  Nominal GDP growth,  $\% \Delta S = 0, \% \Delta P / E = 0$

Video: https://youtu.be/yOmaMz2YC18

# Risk Premium Approaches to Equity Returns

Equity-vs-bills premium = Term premium + Equity-vs-bond premium

Term premium = Return on bonds - Return on bills

# Singer-Terhaar Approach

Risk premium under full integration:

$$
R P _ {i} ^ {G} = \rho_ {i, G M} \sigma_ {i} \left(\frac {R P _ {G M}}{\sigma_ {G M}}\right)
$$

Risk premium under complete segmentation:

$$
R P _ {i} ^ {S} = 1 \times \sigma_ {i} \times \begin{array}{c} S h a r p e r a t i o o f \\ s e g m e n t e d m a r k e t e t \end{array}
$$

Singer-Terhaar risk premium,  $RP_{i} = \phi RP_{i}^{G} + (1 - \phi)RP_{i}^{S}$

Expected return of asset class  $i$ ,  $E(R_{i}) = R_{F} + RP_{i}$

where:

$$
\rho_ {i, G M} = \text {c o r r e l a t i o n b e t w e e n i t h a s s e t a n d g l o b a m a k e t p o r t f o l i o}
$$

$$
\sigma_ {i} = \text {s t a n d a r d}
$$

$$
\frac {R P _ {G M}}{\sigma_ {G M}} = \text {S h a r p e}
$$

$$
\phi = \text {D e g r e e o f i n t e g r a t i o n}
$$

$$
R _ {F} = \text {R i s k - f r e e r a t e}
$$

# Note:

- Add liquidity premium where appropriate  
- If Sharpe ratio of segmented market not given, use Sharpe ratio of global market portfolio

Video: https://youtu.be/RK2WETqIzoQ

# Risk Premium (Building Block) Approach to Fixed Income Returns

<table><tr><td>Bond</td><td>Required Return</td></tr><tr><td>Short-term fixed-rate government bill</td><td>Real risk-free rate + Inflation premium</td></tr><tr><td>Long-term fixed-rate government bond</td><td>Real risk-free rate + Inflation premium + Maturity premium</td></tr><tr><td>Long-term inflation-linked government bond</td><td>Real risk-free rate + Maturity premium</td></tr><tr><td>Long-term fixed-rate corporate bond</td><td>Real risk-free rate + Inflation premium + Maturity premium + Credit premium</td></tr><tr><td>Long-term callable fixed-rate corporate bond</td><td>Real risk-free rate + Inflation premium + Maturity premium + Credit premium + Call risk</td></tr></table>

# Real Estate

Long-run:

$$
E \left(R _ {r e}\right) = C a p r a t e + N O I g r o w t h r a t e
$$

Finite horizon:

$$
E \left(R _ {r e}\right) = C a p r a t e + N O I g r o w t h r a t e - \% \Delta C a p r a t e
$$

# Capital Flows

In the long run

$$
\begin{array}{l} E \left(\% \Delta S _ {d / f}\right) = \left(r ^ {d} - r ^ {f}\right) + \left(T e r m ^ {d} - T e r m ^ {f}\right) + \left(C r e d i t ^ {d} - C r e d i t ^ {f}\right) \\ + (E q u i t y ^ {d} - E q u i t y ^ {f}) + (L i q u i d ^ {d} - L i q u i d ^ {f}) \\ \end{array}
$$

# Currency

For a currency pair,  $d / f$ , if  $f$  changes by  $x\%$  against  $d$ , then  $d$  changes by  $\frac{1}{1 + x} - 1$  against  $f$ .

# VCV Matrix with Sample Statistics

With  $N$  assets, required:

-  $N$  variances  
$\frac{N(N - 1)}{2}$  covariances

# VCV Matrices from Multi-Factor Models

Return on ith asset:

$$
r _ {i} = \alpha_ {i} + \sum_ {k = 1} ^ {K} \beta_ {i K} F _ {K} + \varepsilon_ {i}
$$

Variance of the ith asset:

$$
\sigma_ {i} ^ {2} = \sum_ {m = 1} ^ {K} \sum_ {n = 1} ^ {K} \beta_ {i m} \beta_ {i n} \rho_ {m n} + \nu_ {i} ^ {2}
$$

Covariance between ith and jth asset:

$$
\sigma_ {i j} = \sum_ {m = 1} ^ {K} \sum_ {n = 1} ^ {K} \beta_ {i m} \beta_ {j n} \rho_ {m n}
$$

With  $N$  assets and  $K$  factors, required:

-  $(N \times K)$  factor sensitivities  
$K(K + 1)$  factor covariances

where:

$$
\alpha_ {i} = \text {I n t e r c e p t}
$$

$\beta_{iK} =$  Asset's sensitivity to the kth factor

$$
F _ {K} = k \text {t h c o m m o n f a c t o r r e t u r n}
$$

$$
\varepsilon_ {i} = \text {s t o c h a s t i c t e r m (m e a n = z e r o)}
$$

$$
\rho_ {m n} = \text {c o r r e l a t i o n b e t w e e n m t h a n d n t h f a c t o r s}
$$

$\nu_{i}^{2} =$  variance of unique component of ith asset's return

Video: https://youtu.be/XVpJ8yuTngo

# Smoothed Returns

$$
R _ {t} = (1 - \lambda) r _ {t} + \lambda R _ {t - 1} \quad 0 <   \lambda <   1
$$

$$
v a r (r) = \left(\frac {1 + \lambda}{1 - \lambda}\right) v a r (R)
$$

where:

$$
R _ {t} = \text {C u r r e n t o b s e r v e d r e t u r n} \quad R _ {t - 1} = \text {P r e v i o u s o b s e r v e d r e t u r n}
$$

$$
r _ {t} = \text {C u r r e n t t r u e r e t u r n} \quad v a r (r) = \text {T r u e v a r i a n c e}
$$

# ARCH Model

$$
\begin{array}{l} \sigma_ {t} ^ {2} = \gamma + \alpha \sigma_ {t - 1} ^ {2} + \beta \eta_ {t} ^ {2} \quad \gamma , \alpha , \beta \geq 0, \alpha + \beta <   1 \\ = \gamma + (\alpha + \beta) \sigma_ {t - 1} ^ {2} + \beta \left(\eta_ {t} ^ {2} - \sigma_ {t - 1} ^ {2}\right) \\ \end{array}
$$

where:

$$
\begin{array}{l} \sigma_ {t} ^ {2} = \text {V a r i a n c e} t \\ \eta_ {t} = \text {U n e x p e c t e d} t (\text {m e a n} = 0) \\ \eta_ {t} ^ {2} - \sigma_ {t - 1} ^ {2} = \text {S h o c k t o v a r i a n c e i n p e r i o d} t \\ \end{array}
$$

Unconditional expected value of variance

$$
\frac {\gamma}{1 - \alpha - \beta}
$$

Learning Module 3: Overview of Asset Allocation

Economic Net Worth = Economic Assets - Economic Liabilities

Economic Assets = Financial Assets + Extended Assets

Economic Liabilities = Financial Liabilities + Extended Liabilities

Learning Module 4: Principles of Asset Allocation

# Mean-Variance Optimization

# Utility

$$
U _ {m} = E (R _ {m}) - 0. 0 0 5 \lambda \sigma_ {m} ^ {2}
$$

where:

$U_{m} =$  Investor's utility for asset mix,  $m$

$R_{m} =$  Return for asset mix,  $m$

$\lambda =$  Investor's risk aversion coefficient

$\sigma_{m}^{2} =$  Expected variance of return for asset mix  $m$  (in  $\%$

Surplus  $=$  Market value of assets - Present value of liabilities

Funding ratio =  $\frac{\text{Market value of assets}}{\text{Present value of liabilities}}$

# Surplus Optimization

$$
U _ {m} ^ {L R} = E \big (R _ {s, m} \big) - 0. 0 0 5 \lambda \sigma_ {s, m} ^ {2}
$$

where:

$U_{m}^{LR} =$  Surplus objective function's expected value for asset mix m

[ E\left(R_{s,m}\right) = \text{Expected surplus return for asset mix } m ]  
$= \frac{\text{Change in asset value} - \text{Change in liability value}}{\text{Initial asset value}}$

$\sigma_{s,m} =$  Surplus return volatility for asset mix  $m$

$\lambda =$  Investor's risk aversion

# Goals-based Asset Allocation

Video: https://youtu.be/ufo0cNWmfbo

# Risk Parity

$$
w _ {i} \times C o v (r _ {i}, r _ {p}) = \frac {1}{n} \sigma_ {p} ^ {2}
$$

where:

$$
w _ {i} = \text {W e i g h t o f a s s e t} i
$$

$\text{Cov}\left( {{r}_{i},{r}_{p}}\right)  =$  Covariance of asset  $i$  with portfolio

$$
n = \text {N u m b e r o f a s s e t s}
$$

$$
\sigma_ {p} ^ {2} = \text {V a r i a n c e o f p o r t f o l i o}
$$

# Risk Budgeting

Marginal Contribution to Risk

$$
M C T R = \begin{array}{c} A s s e t b e t a r e l a t i v e \\ t o p o r t f o l i o \end{array} \times \begin{array}{c} P o r t f o l i o s t a n d a r d \\ d e v i a t i o n \end{array}
$$

Actual Contribution to Risk

$$
A C T R = \frac {\text {A s s e t w e i g h t}}{\text {i n p o r t f o l i o}} \times M C T R
$$

Ratio of excess return to MCTR = Expected return - Risk free rate / MCTR

Learning Module 5: Asset Allocation with Real-World Constraints

# After-tax Portfolio Optimization

$$
r _ {a t} = r _ {p t} (1 - t)
$$

$$
\sigma_ {a t} = \sigma_ {p t} (1 - t)
$$

$$
R R _ {a t} = \frac {R R _ {p t}}{1 - t}
$$

where:  $r_{at} =$  Expected after-tax return

$$
\begin{array}{l} r _ {p t} = \text {E x p e c t e d p r e - t a x r e t u r n} \\ t = \text {E x p e c t e d} \\ \end{array}
$$

$\sigma_{at} =$  Expected after-tax standard deviation

$\sigma_{pt} =$  Expected pre-tax standard deviation

$RR_{at} =$  After-tax rebalancing range

$RR_{pt} = \text{Pre-tax rebalancing range}$

Learning Module 1: Passive Equity Investing

Herfindahl Hirschman Index (HHI)

$$
H H I = \sum_ {i = 1} ^ {n} w _ {i} ^ {2}
$$

where:  $w_{i} =$  Weight of stock  $i$  in portfolio

$$
E f f e c t i v e n u m b e r o f s t o c k s = \frac {1}{H H I}
$$

$$
T r a c k i n g e r r o r _ {p} = \sqrt {V a r i a n c e} _ {R _ {p} - R _ {b}}
$$

$$
E x c e s s r e t u r n _ {p} = R _ {p} - R _ {b}
$$

Learning Module 2: Overview of Fixed Income Portfolio Management

Expected fixed-income return

$$
\begin{array}{l} E (R) = \text {Y i e l d i n c o m e} + \text {R o l l d o w n r e t u r n} \\ + E (C h a n g e i n p r i c e b a s e d o n i n v e s t o r ^ {\prime} s v i e w o f b e n c h m a r k y i e l d) \\ + E (C h a n g e i n p r i c e b a s e d o n i n v e s t o r ^ {\prime} s v i e w o f y i e l d s p r e a d s) \\ + E (C h a n g e i n p r i c e b a s e d o n i n v e s t o r ^ {\prime} s v i e w o f c u r r e n c y v a l u e \text {c h a n g e s}) \\ \end{array}
$$

$$
\frac {\text {Y i e l d i n c o m e}}{\text {(o r c u r r e n t y i e l d)}} = \frac {\text {A n n u a l c o u p o n p a y m e n t}}{\text {C u r r e n t b o n d p r i c e}}
$$

$$
\text {R o l l d o w n r e t u r n} = \frac {\text {P r i c e} _ {\text {E n d}} - \text {P r i c e} _ {0}}{\text {P r i c e} _ {0}} \quad (\text {A s s u m e n o c h a n g e i n y i e l d c u r v e})
$$

Rolling yield  $=$  Yield income + Rolldown return

$$
E \left( \begin{array}{c} C h a n g e i n p r i c e b a s e d \\ o n i n v e s t o r ^ {\prime} s v i e w o f \\ b e n c h m a r k y i e l d \end{array} \right) = - M o d D u r \times \Delta Y i e l d + \frac {1}{2} \times C o n v e x i t y \times (\Delta Y i e l d) ^ {2}
$$

$$
\begin{array}{l} E \left( \begin{array}{c} C h a n g e i n p r i c e b a s e d \\ o n i n v e s t o r ^ {\prime} s v i e w o f \\ y i e l d s p r e a d s \end{array} \right) \\ = - S p r e a d D u r \times \Delta S p r e a d + \frac {1}{2} \times S p r e a d C o n v e x i t y \times (\Delta S p r e a d) ^ {2} \\ \end{array}
$$

For foreign fixed income investments:

$$
R _ {D C} = \left(1 + R _ {F C}\right) \left(1 + R _ {F X}\right) - 1
$$

$$
\begin{array}{l} R _ {F C} = \text {Y i e l d i n c o m e} + \text {R o l l d o w n r e t u r n} \\ + E (\text {C h a n g e i n p r i c e b a s e d o n i n v e s t o r} ^ {\prime} \text {s v i e w o f b e n c h m a r k y i e l d}) \\ + E (C h a n g e i n p r i c e b a s e d o n i n v e s t o r ^ {\prime} s v i e w o f y i e l d s p r e a d s) \\ \end{array}
$$

$$
\begin{array}{l} R _ {F X} = \text {P e r c e n t a g e} \\ = \frac {E \left(S _ {D C / F C}\right) - S _ {0 , D C / F C}}{S _ {0 , D C / F C}} \quad (u n h e d g e d) \\ = \frac {F _ {D C / F C} - S _ {0 , D C / F C}}{S _ {0 , D C / F C}} \quad (h e d g e d) \\ \end{array}
$$

# Using Leverage in the Bond Portfolio

Leveraged portfolio return

$$
r _ {P} = r _ {I} + \frac {V _ {B}}{V _ {E}} (r _ {I} - r _ {B})
$$

where:

$$
r _ {I} = \text {r e t u r n o n i n v e s t e d f u n d s}
$$

$$
r _ {B} = \text {c o s t}
$$

$$
V _ {B} = \text {b o r r o w e d f u n d s}
$$

$$
V _ {E} = \text {v a l u e o f p o r t f i l o i o s e q u i t y}
$$

Video: https://youtu.be/NadocNKzDBw

Futures

$$
L e v e r a g e _ {F u t u r e s} = \frac {N o t i o n a l v a l u e - M a r g i n}{M a r g i n}
$$

Repo

$$
D o l l a r i n t e r e s t = P r i n c i p a l \times R e p o r a t e \times \frac {T e r m o f r e p o i n d a y s}{3 6 0}
$$

# Securities Lending

$$
R e b a t e r a t e = C o l l a t e r a l \quad e a n i n g s \quad r a t e - S e c u r i t y \quad l e n d i n g \quad r a t e
$$

# Cash Flow Matching

$$
\begin{array}{c} \text {R e q u i r e d p a r v a l u e} \\ \text {f o r t h e l o n g e s t} \\ \text {m a t u r i t y b o n d} \end{array} = \frac {\text {A m o u n t o f f i n a l l i a b i l i t y d u e}}{1 + \text {C o u p o n r a t e o f t h e l o n g e s t m a t u r i t y b o n d}}
$$

Video: https://youtu.be/fB257bEep59c

$$
C o n v e x i t y = \frac {M a c D u r ^ {2} + M a c D u r + D i s p e r s i o n}{(1 + C a s h f l o w y i e l d) ^ {2}}
$$

Learning Module 3: Asset Allocation to Alternative Investments

# Unsmoothed Returns

$$
r _ {t, u n s m o o t h e d} = \frac {r _ {t , r e p o r t e d} - s \times r _ {t - 1 , r e p o r t e d}}{1 - s}
$$

where:  $s =$  Serial correlation

# Net Asset Value (NAV)

$$
N A V _ {t} = N A V _ {t - 1} \times (1 + G) + C _ {t} - D _ {t}
$$

where:

$$
C _ {t} = R C _ {t} \times \left(C C - P I C _ {t}\right)
$$

$$
D _ {t} = R D _ {t} \times [ N A V _ {t - 1} \times (1 + G) ]
$$

Learning Module 4: Overview of Private Wealth Management

$$
H u m a n C a p i t a l = \sum_ {t = 1} ^ {N} \frac {p (s _ {t}) \times w _ {t - 1} \times (1 + g _ {t})}{\left(1 + r _ {f} + y\right) ^ {t}}
$$

where:

$$
p \left(s _ {t}\right) = \text {P r o b a b i l i t y}
$$

$$
w _ {t - 1} = \text {I n c o m e f r o m e m p l o y m e n t i n p e r i o d} t - 1
$$

$$
g _ {t} = \text {A n n u a l w a g e g r o w t h r a t e}
$$

$$
r _ {f} = \text {N o m i n a l}
$$

$$
y = \text {R i s k p r e m i u m a s s o c i a t e d w i t h o c o u p a t i o n a l i n c o m e v o l a t i l y}
$$

$$
N = \text {L e n g t h o f w o r k i n g l e}
$$

# Taxes on Income

$$
A v e r a g e t a x r a t e = \frac {T a x l i a b i l i t y}{T a x a b l e i n c o m e}
$$

# Accrual Taxes on Investment Returns

After-tax future value of a $1 investment, with returns taxed annually:

$$
F V _ {A T} = [ 1 + R (1 - t _ {x}) ] ^ {T}
$$

where:

PV = Initial investment

$R =$  Pretax return

$t_{x} = \text{Tax rate on investment income}$

$T =$  Investment period (in years)

$$
\begin{array}{l} T a x d r a g = \frac {D i f f e r e n c e i n i n v e s t m e n t g a i n s w i t h a n d w i t h o u t t a x e s}{I n v e s t m e n t g a i n s w i t h o u t t a x e s} \\ = \frac {(1 + R) ^ {T} - [ 1 + R (1 - t _ {x}) ] ^ {T}}{(1 + R) ^ {T} - 1} \\ \end{array}
$$

After-tax inflation-adjusted future value of a $1 investment (accrual taxes):

$$
F V _ {A T, i n f l} = \left[ \frac {1 + R (1 - t _ {x})}{1 + i n f l} \right] ^ {T}
$$

# Deferral of Taxes on Capital Gains

After-tax future value of a \(1 investment, with deferred capital gains taxed at t_{CG} and the cost basis, B, expressed as percentage of the current market value of the investment:

$$
F V _ {C G} = (1 + R) ^ {T} \left(1 - t _ {C G}\right) + t _ {C G} \times B
$$

$$
T a x d r a g = \frac {(1 + R) ^ {T} - [ (1 + R) ^ {T} (1 - t _ {C G}) + t _ {C G} \times B ]}{(1 + R) ^ {T} - 1}
$$

After-tax inflation-adjusted future value of a $1 investment:

$$
F V _ {C G, i n f l} = \frac {(1 + R) ^ {T} (1 - t _ {C G}) + t _ {C G} \times B}{(1 + i n f l) ^ {T}}
$$

# Defined Benefit Pension Plan

$$
F u n d e d r a t i o = \frac {F a i r v a l u e o f p l a n a s s e t s}{P r e s e n t v a l u e o f d e f i n e d b e n e f i t o b l i g a t i o n s}
$$

$$
F u n d e d s t a t u s = \frac {F a i r v a l u e o f}{p l a n a s s e t s} - \frac {P r e s e n t v a l u e o f d e f i n e d}{b e n e f i t o b l i g a t i o n s}
$$

# Spending Policies (Endowment and Foundation)

Constant Growth rule:

$$
S p e n d i n g _ {t + 1} = S p e n d i n g _ {t} \times (1 + I n f l a t i o n R a t e)
$$

Market Value rule:

$$
S p e n d i n g _ {t + 1} = S p e n d i n g r a t e \times A v e r a g e A U M
$$

Hybrid rule:

$$
S p e n d i n g _ {t + 1} = w \times \begin{array}{c} C o n s t a n t G r o w t h \\ r u l e \end{array} + (1 - w) \times \begin{array}{c} M a r k e t v a l u e \\ r u l e \end{array}
$$

# Bank and Insurance

Duration of equity capital,  $D_{E}$

$$
D _ {E} = \left(\frac {A}{E}\right) D _ {A} - \left(\frac {A}{E} - 1\right) D _ {L} \left(\frac {\Delta i}{\Delta y}\right)
$$

$$
\sigma_ {\Delta E / E} ^ {2} = \left(\frac {A}{E}\right) ^ {2} \sigma_ {\Delta A / A} ^ {2} + \left(\frac {A}{E} - 1\right) ^ {2} \sigma_ {\Delta L / L} ^ {2} - 2 \left(\frac {A}{E}\right) \left(\frac {A}{E} - 1\right) \rho \sigma_ {\Delta A / A} \sigma_ {\Delta L / L}
$$

Equity capital ratio  $= \frac{E}{A}$

$$
D _ {A} = \text {D u r a t i o n o f a s s e t s}
$$

$$
D _ {L} = \text {D u r a t i o n o f l i a b i l i t i e s}
$$

$$
i = \text {E f f e c t i v e}
$$

$$
y = \text {E f f e c t i v e}
$$

$$
\sigma_ {\Delta E / E} ^ {2} = \text {V a r i a n c e o f c h a n g e i n v a l u e o f e q u i t y c a p i t a l}
$$

$$
\sigma_ {\Delta A / A} ^ {2} = \text {V a r i a n c e o f c h a n g e i n v a l u e o f a s s e t s}
$$

$$
\sigma_ {\Delta L / L} ^ {2} = \text {V a r i a n c e o f c h a n g e i n v a l u e o f l i a b i l i t i e s}
$$

$$
\rho = \text {C o r r e l a t i o n b e t w e e n p e r t a g e v a l u e c h a n g e s o f a s s e t s a n d l i a b i l i t i e s}
$$

# Learning Module 6: Trading Costs and Electronic Markets

$$
\begin{array}{c} E f f e c t i v e s p r e a d \\ t r a n s a c t i o n c o s t e s t i m a t e \end{array} = T r a d e s i z e \times \left\{ \begin{array}{l l} T r a d e p r i c e - M i d q u o t e p r i c e & f o r b u y o r d e r s \\ M i d q u o t e p r i c e - T r a d e p r i c e & f o r s e l l o r d e r s \end{array} \right.
$$

$$
E f f e c t i v e s p r e a d = \left\{ \begin{array}{l l} 2 \times (T r a d e p r i c e - M i d q u o t e p r i c e) & f o r b u y o r d e r s \\ 2 \times (M i d q u o t e p r i c e - T r a d e s i z e) & f o r s e l l o r d e r s \end{array} \right.
$$

where:

$$
M i d q u o t e p r i c e = \frac {B i d + A s k}{2}
$$

$$
\begin{array}{c} V W A P \text {t r a n s a c t i o n} \\ \text {c o s t e s t i m a t e} \end{array} = \text {T r a d e s i z e} \times \left\{ \begin{array}{l l} \text {T r a d e V W A P - M i d q u o t e p r i c e} & \text {f o r b u y o r d e r s} \\ \text {M i d q u o t e p r i c e - T r a d e V W A P} & \text {f o r s e l l o r d e r s} \end{array} \right.
$$

# Learning Module 7: Case Study in Portfolio Management: Institutional (SWF)

No formula.

Learning Module 1: Portfolio Performance Evaluation

Arithmeticexcessreturn  $= R - B$

Geometric excess return  $= \frac{R - B}{1 + B}$

# Attribution based on Factor Models

Active Return  $=$  Return from factor tilt + Security selection return

$$
R - B = \sum \left(\beta_ {P, i} - \beta_ {B, i}\right) \times F _ {i} + S e c u r i t y s e l e c t i o n r e t u r n
$$

where:

$$
\beta_ {P, i} = \text {S e n s i t i v i t y o f t h e p o r t f i l o o t o t h e g i v e n f a c t o r}
$$

$$
\beta_ {B, i} = \text {S e n s i t i v i t y o f t h e b e n c h m a r k t o t h e g i v e n f a c t o r}
$$

$$
F _ {i} = \text {F a c t o r}
$$

# Micro and Macro Return Attribution

$$
R - B = \sum_ {i = 1} ^ {n} A _ {i} + \sum_ {i = 1} ^ {n} S _ {i} + \sum_ {i = 1} ^ {n} I _ {i}
$$

where:

$$
w _ {i} = \text {W e i g h t o f a s s e t} i \text {i n p o r t f o l i o}
$$

$$
W _ {i} = \text {W e i g h t o f a s s e t} i \text {i n b e n c h m a r k}
$$

$$
R _ {i} = \text {R e t u r n o f a s s e t} i \text {i n p o r t f o l i o}
$$

$$
B _ {i} = \text {R e t u r n o f a s s e t} i \text {i n b e n c h m a r k}
$$

Video: https://youtu.be/yrzTVIfqloM

# Brinson-Fachler Model

Allocation effect:  $A_{i} = (w_{i} - W_{i})(B_{i} - B)$

Selection effect:  $S_{i} = W_{i}(R_{i} - B_{i})$

Interaction effect:  $I_{i} = (w_{i} - W_{i})(R_{i} - B_{i})$

# Brinson-Hood-Beebower Model (BHB)

Allocation effect:  $A_{i} = (w_{i} - W_{i})B_{i}$

Selection effect:  $S_{i} = W_{i}(R_{i} - B_{i})$

Interaction effect:  $I_{i} = (w_{i} - W_{i})(R_{i} - B_{i})$

# Decomposing Portfolio Returns

$$
P = M + S + A
$$

where:

$$
P = \text {P o r t f l o i r o}
$$

$$
M = \text {M a r k e t i n d e x r e t u r n}
$$

$$
B = \text {B e n c h m a r k}
$$

$$
S = B - M = \text {S t y l e}
$$

$$
A = P - B = \text {A c t i v e r e t u r n (T r u e a c t i v e r e t u r n)}
$$

# Performance Appraisal

# Sharpe Ratio

$$
S h a r p e r a t i o = \frac {R _ {p} - r _ {f}}{\sigma_ {p}}
$$

where:

$$
R _ {p} = \text {P o r t f o l i o r e t u r n}
$$

$$
r _ {f} = \text {R i s k - f r e e r a t e}
$$

$$
\sigma_ {p} = \text {P o r t f o l i o s t a n d a r d d e v i a t i o n}
$$

# Treynor Ratio

$$
T r e y n o r r a t i o = \frac {R _ {p} - r _ {f}}{\beta_ {p}}
$$

where:

$$
R _ {p} = \text {P o r t f o l i o r e t u r n}
$$

$$
r _ {f} = \text {R i s k - f r e e r a t e}
$$

$$
\beta_ {p} = \text {P o r t f o l i o b e t a (S y s t e m a t i c r i s k)}
$$

# Information Ratio

$$
I n f o r m a t i o n r a t i o = \frac {R _ {p} - R _ {B}}{\sigma_ {R _ {p} - R _ {B}}}
$$

where:

$$
R _ {p} = \text {P o r t f i l o}
$$

$$
R _ {B} = \text {B e n c h m a r k}
$$

$$
\sigma_ {R _ {p} - R _ {B}} = \text {A c t i v e r i s k (T r a c k i n g r i s k / T r a c k i n g e r r o r)}
$$

# Appraisal Ratio

$$
A p p r a i s a l r a t i o (T r e y n o r B l a c k r a t i o) = \frac {\alpha}{\sigma_ {\varepsilon}}
$$

where:

$$
\begin{array}{l} \sigma_ {\varepsilon} = \text {S t a n d a r d e r r o f r e g r e s s i o n (f r o m f a c t o r m o d e l)} \\ = \sqrt {\sigma_ {P} ^ {2} - \beta_ {i} ^ {2} \sigma_ {M} ^ {2}} \\ \end{array}
$$

$$
\alpha = R _ {i} - \left[ R _ {f} + \beta_ {i} \big (R _ {M} - R _ {f} \big) \right]
$$

# Sortino Ratio

$$
\text {S o r t i n o r a t i o} = \frac {R _ {p} - r _ {T}}{\sigma_ {\text {D o w n s i d e}}}
$$

where:

$$
\begin{array}{l} r _ {T} = \text {I n v e s t o r} ^ {\prime} \text {s m i n i m u m a c c e p t a b l e r e t u r n / t a r g e t r e t u r n} \\ \sigma_ {D o w n s i d e} = \sqrt {\frac {1}{N} \sum_ {t = 1} ^ {N} \min (r _ {t} - r _ {T} , 0) ^ {2}} \\ \end{array}
$$

# Capture Ratio

$$
C a p t u r e \: R a t i o = \frac {U p s i d e \: C a p t u r e}{D o w n s i d e \: C a p t u r e}
$$

$$
U p s i d e C a p t u r e = \frac {R _ {m}}{R _ {B}} \quad R _ {B} \geq 0
$$

$$
D o w n s i d e C a p t u r e = \frac {R _ {m}}{R _ {B}} \quad R _ {B} <   0
$$

where:

$$
\begin{array}{l} R _ {m} = \text {M a n a g e r ' s} \\ R _ {B} = \text {B e n c h m a r k} \\ \end{array}
$$

# Maximum Drawdown

$$
M a x i m u m D r a w d o w n = \min \left(\left[ \frac {V (m , t) - V (m , t ^ {*})}{V (m , t ^ {*})} \right], 0\right)
$$

where:

$$
V (m, t) = \text {p o r t f i l o o v e} m \text {a t} t
$$

$$
V (m, t ^ {*}) = \text {p e a k p o r t f i l o v i e o f m a n a g e r} m
$$

$$
t > t ^ {*}
$$

Video: https://youtu.be/0tRDDT9E9AU

Learning Module 2: Investment Manager Selection

# Performance-Based Fees

If manager is fully exposed to upside and downside:

$$
\text {C o m p u t e d f e e} = \text {B a s e f e e} + \text {S h a r i n g o f p e r f e r m a n c e}
$$

If manager not exposed to downside:

Computed fee = Higher of either [1] Base fee, OR  
[2] Base fee plus sharing of positive performance

If manager is not exposed to downside, and there is a maximum fee.

Computed fee = Higher of either [1] Base fee, OR

[2] Base fee plus sharing of performance, to a maximum fee

# Time-weighted return

$$
r _ {t w r} = \left(1 + r _ {t, 1}\right) \times \left(1 + r _ {t, 2}\right) \times \ldots \times \left(1 + r _ {t, n}\right) - 1
$$

where:

$r_{t,1}$  through  $r_{t,n} = \text{Sub-period returns}$

# Modified Dietz method

$$
r _ {M o d D i e t z} = \frac {V _ {1} - V _ {0} - C F}{V _ {0} + \sum_ {i = 1} ^ {n} (C F _ {i} \times w _ {i})}
$$

Video: https://youtu.be/guZWVXirJLO

# Modified IRR method

$$
V _ {1} = \sum_ {i = 1} ^ {n} [ C F _ {i} \times (1 + M I R R) ^ {w _ {i}} ] + V _ {0} (1 + M I R R)
$$

where:

$w_{i} =$  Proportion of period (in days) that each cash flow has been in the portfolio

$$
= \frac {C D - D _ {i}}{C D}
$$

$CD =$  Total number of calendar days in the period

$D_{i} =$  Number of calendar days from the beginning of the period to the time cash flow  $CF_{i}$  occurs

$$
C F = \sum_ {i = 1} ^ {n} C F _ {i}
$$

# Composite Time-Weighted Return

Asset-weight individual portfolio returns using beginning-of-period values

$$
r _ {C} = \sum_ {p i = 1} ^ {n} r _ {p i} \times \frac {V _ {0 , p i}}{\sum_ {p i = 1} ^ {n} V _ {0 , p i}}
$$

where:

$$
r _ {C} = \text {C o m p o s i t e r e t u r n}
$$

$$
r _ {p i} = \text {R e t u r n o f a n i n d i v i d u a l p o r t f i l o} i
$$

$$
V _ {0, p i} = \text {B e g i n n i n g v a l u e o f p o r t f o l i o} i
$$

$\sum_{pi=1}^{n} V_{0,pi} = \text{Total beginning fair value of all individual portfolios in the composite}$

Use a method that reflects both beginning-of-period values and external cash flows

$$
r _ {C} = \sum_ {p i = 1} ^ {n} r _ {p i} \times \frac {V _ {p i}}{\sum_ {p i = 1} ^ {n} V _ {p i}}
$$

where:

$V_{pi} =$  Beginning value of portfolio  $i +$  Weighted external cash flows

$\sum_{pi=1}^{n} V_{pi} = \text{Total beginning fair value and weighted external cash flows of all individual portfolios in the composite}$

# Aggregate Return Method

$$
r _ {M o d D i e t z} = \frac {V _ {1} - V _ {0} - C F}{V _ {0} + \sum_ {i = 1} ^ {n} (C F _ {i} \times w _ {i})}
$$

where:

$V_{1} =$  Ending value of composite

$V_{0} =$  Beginning value of composite

$$
C F = \underset {c a s h f l o w s i n c o m p o s i t e} {T o t a l o f e x t e r n a l} = \sum_ {i = 1} ^ {n} C F _ {i}
$$

$$
\sum_ {i = 1} ^ {n} \left(C F _ {i} \times w _ {i}\right) = \frac {\text {T o t a l o f w e i g h t e d e x t e r n a l}}{\text {c a s h f l o w s i n c o m p o s i t e}} = \sum_ {p i = 1} ^ {n} V _ {p i}
$$

# Equal-weighted standard deviation

$$
S _ {c} = \sqrt {\frac {\sum_ {i = 1} ^ {n} (r _ {i} - \bar {r} _ {c}) ^ {2}}{n}}
$$

where:

$$
r _ {i} = \text {r e t u r n f o r p o r t f i l o i}
$$

$$
\bar {r} _ {c} = \text {e q u a l - w e i g h t e d m e a n}
$$

$$
n = \text {n u m b e r o f p o r t f o l i o s i n c o m p o s i t e}
$$

# Asset-weighted standard deviation

$$
S _ {c, a w} = \sqrt {\sum_ {i = 1} ^ {n} w _ {i} \times \left(r _ {i} - \bar {r} _ {p r o x y}\right) ^ {2}}
$$

$$
\begin{array}{l} \bar {r} _ {p r o x y} = \text {a s s e t - w e i g h t e d m e a n r e t u r n} \\ = \sum_ {i = 1} ^ {n} w _ {i} \times r _ {i} \\ \end{array}
$$

$$
w _ {i} = \text {w e i g h t o f p o r t f o l i o} i = \frac {V _ {0 , i}}{V _ {0 , T o t a l}}
$$

# Learning Module 1: Option Strategies

Put-call parity

$$
S _ {0} + p _ {0} = c _ {0} + \frac {X}{(1 + r) ^ {T}}
$$

Put-call-forward parity

$$
\frac {F _ {0}}{(1 + r) ^ {T}} + p _ {0} = c _ {0} + \frac {X}{(1 + r) ^ {T}}
$$

Synthetic long forward

$$
c _ {0} - p _ {0} = \frac {F _ {0} - X}{(1 + r) ^ {T}}
$$

Option premium = Time value + Intrinsic value

# Covered Calls

Video: https://youtu.be/2SocH6PghOk

Expiration value  $= S_{T} - \operatorname{Max}(S_{T} - X, 0)$

Profit at Expiration  $= S_{T} - \text{Max}(S_{T} - X, 0) + c_{0} - S_{0}$

Maximum gain  $= X - S_{0} + c_{0}$

Maximum loss  $= S_{0} - c_{0}$

Breachaven price  $= S_{0} - c_{0}$

Position delta = Stock Delta - Call Delta = 1 -  $\Delta_{call}$

Position gamma = Stock Gamma - Call Gamma = -Gamma<0

Position vega = Stock Vega - Call Vega = -Vega call < 0

Position theta = Stock Theta - Call Theta = -Theta<0

# Protective Puts

Video: https://youtu.be/VLK1IXbXtRk

Expiration value  $= S_{T} + \text{Max}(X - S_{T}, 0)$

Profit at Expiration  $= S_{T} + \text{Max}(X - S_{T}, 0) - S_{0} - p_{0}$

Maximum gain  $= \infty$

Maximum loss  $= S_{0} - X + p_{0}$

Breakeven price  $= S_{0} + p_{0}$

Position delta = Stock Delta + Put Delta = 1 +  $\Delta_{put}$

Position gamma = Stock Gamma + Put Gamma = Gamma $_{put}$  > 0

Position Vega = Stock Vega + Put Vega = Vega $_{put}$  > 0

Position theta = Stock Theta + Put Theta = Theta<sub>put</sub> < 0

# Call Bull Spread

Video: https://youtu.be/3NHwelzEU0k

Expiration value  $= \text{Max}(S_T - X_L, 0) - \text{Max}(S_T - X_H, 0)$

Profit at Expiration  $= \text{Max}(S_T - X_L, 0) - \text{Max}(S_T - X_H, 0) - (c_L - c_H)$

Maximum gain  $= X_{H} - X_{L} - (c_{L} - c_{H})$

Maximum loss  $= c_{L} - c_{H}$

Breachaven price  $= X_{L} + c_{L} - c_{H}$

# Put Bull Spread

Video: https://youtu.be/Lf1Fi-zy7w4

Expiration value  $= \text{Max}(X_L - S_T, 0) - \text{Max}(X_H - S_T, 0)$

Profit at Expiration  $= \text{Max}(X_L - S_T, 0) - \text{Max}(X_H - S_T, 0) - (p_L - p_H)$

Maximum gain  $= p_{H} - p_{L}$

Maximum loss  $= X_{H} - X_{L} + p_{L} - p_{H}$

Breakeven price  $= X_{H} + p_{L} - p_{H}$

# Put Bear Spread

Video: https://youtu.be/eTejezNXZbU

Expiration value  $= \text{Max}(X_H - S_T, 0) - \text{Max}(X_L - S_T, 0)$

Profit at Expiration  $= \max(X_H - S_T, 0) - \max(X_L - S_T, 0) - (p_H - p_L)$

Maximum gain  $= X_{H} - X_{L} - (p_{H} - p_{L})$

Maximum loss  $= p_{H} - p_{L}$

Breakeven price  $= X_{H} - p_{H} + p_{L}$

# Call Bear Spread

Expiration value  $= \text{Max}(S_T - X_H, 0) - \text{Max}(S_T - X_L, 0)$

Profit at Expiration  $= \text{Max}(S_T - X_H, 0) - \text{Max}(S_T - X_L, 0) - (c_H - c_L)$

Maximum gain  $= c_{L} - c_{H}$

Maximum loss  $= X_{H} - X_{L} + c_{H} - c_{L}$

Breachaven price  $= X_{L} + c_{L} - c_{H}$

# Straddle

Video: https://youtu.be/oDklmeMTnCg

Expiration value  $= \text{Max}(S_T - X, 0) + \text{Max}(X - S_T, 0)$

Profit at Expiration  $= \text{Max}(S_T - X, 0) + \text{Max}(X - S_T, 0) - c_0 - p_0$

Maximum gain  $= \left\{  \begin{array}{ll} \infty & {S}_{T} > X \\  X - {S}_{T} - {c}_{0} - {p}_{0} & {S}_{T} < X \end{array}\right.$

Maximum loss  $= c_{0} + p_{0}$

Breateiven price  $= X \pm (c_{0} + p_{0})$

# Collar

Video: https://youtu.be/LkS_sxmg2cs

Note:  $X_{L} <   S_{0} <   X_{H}$

Expiration value  $= S_{T} + \text{Max}(X_{L} - S_{T}, 0) - \text{Max}(S_{T} - X_{H}, 0)$

Profit at Expiration  $= S_{T} + \text{Max}(X_{L} - S_{T}, 0) - \text{Max}(S_{T} - X_{H}, 0) - S_{0} - p_{0} + c_{0}$

Maximum gain  $= X_{H} - S_{0} - p_{0} + c_{0}$

Maximum loss  $= -X_{L} + S_{0} + p_{0} - c_{0}$

Breachaven price  $= S_{0} + p_{0} - c_{0}$

For zero-cost collar,  $p_0 = c_0$

# Implied Volatility

For 252 trading days in a year and 21 trading days in a month:

$$
\sigma_ {a n n u a l} = \sigma_ {m o n t h l y} \sqrt {\frac {2 5 2}{2 1}}
$$

# Delta hedging

$$
N _ {p o s i t i o n} \times D e l t a _ {p o s i t i o n} + N _ {h e d g e} \times D e l t a _ {h e d g e} = 0
$$

Video: https://youtu.be/v8RcvkQKFpw

Learning Module 2: Swaps, Forwards, and Futures Strategies

# Managing Interest Rate Risk

# Interest Rate Swaps

$$
N _ {S} = \left(\frac {M D U R _ {T} - M D U R _ {P}}{M D U R _ {S}}\right) M V _ {P}
$$

$N_{S} =$  Swap notional principal

$MDUR_{T} =$  Target modified duration

$MDUR_{P} =$  Modified duration of portfolio

$MDUR_{S} =$  Modified duration of swap

$MV_{P} =$  Market value of portfolio

Note: Modified duration of cash = 0 (unless stated otherwise in case)

# Money Market Instrument

$$
B P V = \text {Face Value} \times \frac {\text {Days}}{360} \times 0.01 \%
$$

# Interest Rate Futures

Eurodollar futures price  $= 100 -$  Annualized yield

# Treasury Futures

$$
\frac {\text {P r i n c i p a l i n v o i c e}}{\text {a m o u n t}} = \frac {\text {F u t u r e s s e t t l e m e n t p r i c e}}{1 0 0} \times \frac {\text {C o n v e r s i o n}}{\text {F a c t o r}} \times \text {C o n t r a c t s i z e}
$$

# Basis Point Value Hedge Ratio (BPVHR)

$$
B P V H R = \left(\frac {B P V _ {T} - B P V _ {P}}{B P V _ {C T D}}\right) \times C o n v e r s i o n F a c t o r
$$

$$
\begin{array}{l} B P V _ {T} = M D U R _ {T} \times 0.01 \% \times M V _ {P} \\ B P V _ {P} = M D U R _ {P} \times 0.01 \% \times M V _ {P} \\ B P V _ {C T D} = M D U R _ {C T D} \times 0.01 \% \times M V _ {C T D} \\ M V _ {C T D} = \frac {C T D p r i c e}{1 0 0} \times F u t u r e s c o n t r a c t s i z e \\ B P V _ {F} = \frac {B P V _ {C T D}}{C F} \\ \end{array}
$$

# Hedging Currency Risk with Futures

$$
N _ {f} = \frac {\text {R e q u i r e d c u r r e n c y h e d g e}}{\text {C o n t r a c t s i z e}}
$$

# Hedging Equity Risk with Futures

$$
N _ {f} = \left(\frac {\beta_ {T} - \beta_ {S}}{\beta_ {f}}\right) \left(\frac {S}{F}\right)
$$

where:

$$
\beta_ {T} = \text {T a r g e t b e t a}
$$

$$
\beta_ {S} = \text {P o r t f o l i o b e t a}
$$

$$
\beta_ {f} = \text {F u t u r e s b e t a}
$$

$$
S = \text {P o r t f i l o m a r k e t v a l u e}
$$

$$
F = \text {F u t u r e s p r i c e}
$$

$$
\text {Effective beta} = \frac {\% \Delta \text {Portfolio value}}{\% \Delta \text {Index value}}
$$

Note: Beta of cash = 0

Video: https://youtu.be/VMVQ2GOrG0Q

# Variance Swap

$$
\begin{array}{l} S e t t l e m e n t a m o u n t _ {T} = V e g a n o t i o n a l \left(\frac {\sigma^ {2} - X ^ {2}}{2 X}\right) \\ = \text {V a r i a n c e n o t i o n a l} (\sigma^ {2} - X ^ {2}) \\ \end{array}
$$

$$
\frac {V a l u e o f l o n g v a r i a n c e}{s w a p a t t i m e t} = \frac {V a r i a n c e n o t i o n a l \times (\sigma_ {t} ^ {2} - X ^ {2})}{1 + r \times \left(\frac {T - t}{T}\right)}
$$

where:

$$
\sigma_ {t} ^ {2} = \frac {t}{T} \times \sigma_ {r e a l i z e d} ^ {2} (0, t) + \frac {T - t}{T} \times \sigma_ {i m p l i e d} ^ {2} (t, T)
$$

Video: https://youtu.be/YVNPCXGTdWk

# Probability of a Change in Federal Funds Rate

$$
\begin{array}{c} \text {P r o b a b i l i t y o f} \\ \text {a c h a n g e i n} \\ \text {f e d e r a l f u n d s r a t e} \end{array} = \frac {\text {I m p l i e d F e d f u n d s r a t e - C u r r e n t f e d f u n d s r a t e}}{\text {T a r g e t r a t e h i k e}}
$$

Current fed funds rate  $=$  Midpoint of current target range

Fed funds futures price  $= 100 -$  Implied Fed funds rate

Learning Module 3: Currency Management: An Introduction

$$
R _ {D C} = \left(1 + R _ {F C}\right) \left(1 + R _ {F X}\right) - 1
$$

$$
R _ {D C} = \text {D o m e s t i c - c u r r e n c y}
$$

$$
R _ {F C} = \text {F o r g i n - c u r r e n c y}
$$

$$
R _ {F X} = \text {P e r t e n a g e} \quad \text {c h a n g e i n f o r g i n c} \quad \text {c u r r e n c y a g a i n s t d o m e s t i c c u r r e n c y} \quad (\text {c u r r e n c y q u o t a d s D C / F C})
$$

Video (Unhedged Returns): https://youtu.be/7Cycb5teSbU

Volatility of foreign asset (in domestic currency terms)

$$
\sigma_ {D C} ^ {2} = \sigma_ {F C} ^ {2} + \sigma_ {F X} ^ {2} + 2 \sigma_ {F C} \sigma_ {F X} \rho_ {F C, F X}
$$

For a foreign-risk free asset:

$$
\sigma_ {D C} = \sigma_ {F X} (1 + R _ {F C})
$$

# Minimum Variance Hedge Ratio

$$
y _ {t} = \alpha + \beta x _ {t} + \varepsilon_ {t}
$$

where:

$$
y _ {t} = \text {c h a n g e i n v a l u e o f a s s e t t o b e h e d g e d (m e a s u r e d i n D C)} = R _ {D C}
$$

$$
x _ {t} = \text {c h a n g e i n v a l u e o f h e d g i n g i n s t r u m e n t (m e a s u r e d i n D C)} = R _ {F X}
$$

$$
M V H R, \beta = \frac {C o v (x , y)}{V a r (x)} = \rho_ {x, y} \left(\frac {\sigma_ {y}}{\sigma_ {x}}\right)
$$

Learning Module 1: Private Investments and Structures

Internal Rate of Return (IRR)

$$
N P V = 0 = \frac {C F _ {1}}{(1 + I R R) ^ {1}} + \frac {C F _ {2}}{(1 + I R R) ^ {2}} + \dots + \frac {C F _ {n}}{(1 + I R R) ^ {n}}
$$

Return on Investment (ROI)

$$
R O I = \frac {\Sigma (C a s h f l o w s r e c e i v e d)}{\Sigma (C a s h f l o w s i n v e s t e d)}
$$

For a single cash outflow at the beginning of the period and a single payoff at the end of the period:

$$
R O I = (1 + I R R) ^ {n}
$$

Public Market Equivalent (PME)

$$
N P V = 0 = \frac {C F _ {1}}{(1 + P M E I R R) ^ {1}} + \frac {C F _ {2}}{(1 + P M E I R R) ^ {2}} + \dots + \frac {P M E T e r m i n a l V a l u e}{(1 + P M E I R R) ^ {n}}
$$

Distributed to paid-in (DPI) multiple

$$
D P I = \frac {C u m u l a t i v e d i s t r i b u t i o n}{T o t a l c a p i t a l i n v e s t e d}
$$

Residual value to paid-in (RVPI) multiple

$$
R V P I = \frac {N e t a s s e t v a l u e}{T o t a l c a p i t a l i n v e s t e d}
$$

Total value to paid-in (TVPI) multiple

$$
T V P I = \frac {C u m u l a t i v e d i s t r i b u t i o n + N e t a s s e t v a l u e}{T o t a l c a p i t a l i n v e s t e d}
$$

$$
T V P I = D P I + R V P I
$$

Note: TVPI is also referred to as multiple on money (MOM), multiple on invested capital (MOIC)

Learning Module 2: General Partner and Investor Perspectives and the Investment Process

# Management Fee

$$
\begin{array}{c} \text {M a n a g e m e n t} \\ F e e \end{array} = \begin{array}{c} \text {M a n a g e m e n t} \\ F e e (\%) \end{array} \times \left( \begin{array}{c} \text {C o m m i t t e d} \\ \text {C a p i t a l} \end{array} - \begin{array}{c} \text {C o s t B a s i s o f E x i t s} \\ \text {a n d W r i t e o f f s} \end{array} \right)
$$

Carried Interest with Hard Hurdle Rate (Excluding Management Fee)

$$
r _ {G P} = \max  [ 0, p (r - r _ {h}) ]
$$

Carried Interest with Soft Hurdle Rate/Catch-up Clause (Excluding Management Fee)

$$
r _ {G P} = \max  \left[ 0, r _ {c u} + p \left(r - r _ {h} - r _ {c u}\right) \right]
$$

$$
r _ {c u} = \frac {r _ {h}}{1 - p}
$$

where:

$$
r _ {G P} = G P ^ {\prime} s \text {p e r f o r m a n c e f e e}
$$

$$
r _ {c u} = \text {C a t c h - u p r e t u r n}
$$

$$
p = \text {P e r f o r m a n c e f e e (a s a \% o f r e t u r n)}
$$

$$
r _ {h} = \text {H u r d l e r a t e}
$$

$$
r = \text {O n e - p e r i o d}
$$

Learning Module 3: Private Equity

# Convertible Preferred Shares

$$
\text {O p t i m a l c o n v e r s i o n p o i n t} = \frac {\text {T o t a l l i q u i d a t i o n p r e f e r e n c e v a l u e}}{\text {C o n v e r s i o n r a t i o} \times \text {N u m b e r o f p r e f e r e r d s h a r e s}}
$$

# Venture Capital (VC) Method

$$
\begin{array}{l} \text {P o s t m o n e y v a l u a t i o n} = \text {P r e m o n e y v a l u a t i o n} + \text {E q u i t y i n v e s t m e n t} \\ = \underset {(o l d a n d n e w)} {T o t a l s h a r e s o u t s t a n d i n g} \times S h a r e p r i c e \\ \end{array}
$$

$$
R O I = \frac {E x i t v a l u e}{P o s t m o n e y v a l u a t i o n}
$$

$$
\begin{array}{l} F r a c t i o n a l o w n e r s h i p = \frac {E q u i t y i n v e s t m e n t}{P o s t m o n e y v a l u a t i o n} \\ = \frac {\text {N e w s h a r e s i s s u e d}}{\text {P o s t m o n e y s h a r e s o u t s t a n d i n g}} \\ \end{array}
$$

# Postfinancing Fractional Ownership

$$
F O _ {p o s t} = \left(F O _ {p r i o r} \times \frac {P r e m o n e y v a l u a t i o n}{P o s t m o n e y v a l u a t i o n}\right) + \frac {N e w i n v e s t o r e q u i t y}{P o s t m o n e y v a l u a t i o n}
$$

# Price Step Up

$$
S t e p u p (m u l t i p l e) = \frac {N e w r o u n d s h a r e p r i c e}{P r i o r r o u n d s h a r e p r i c e}
$$

$$
S t e p u p (p e r c e n t a g e) = \left(\frac {N e w r o u n d s h a r e p r i c e}{P r i o r r o u n d s h a r e p r i c e} -\right) \times 1 0 0
$$

# Learning Module 4: Private Debt

# Floating-Rate Loans

$$
P V = \frac {\frac {(M R R + Q M) \times F V}{m}}{\left(1 + \frac {M R R + D M}{m}\right) ^ {1}} + \frac {\frac {(M R R + Q M) \times F V}{m}}{\left(1 + \frac {M R R + D M}{m}\right) ^ {2}} + \dots + \frac {\frac {(M R R + Q M) \times F V}{m} + F V}{\left(1 + \frac {M R R + D M}{m}\right) ^ {N}}
$$

where:

${QM} =$  Quoted margin

DM = Discount margin

$FV =$  Face value

$N =$  Maturity of loan

$MRR =$  Market reference rate (assumed to be constant)

$m =$  Periodicity (e.g.,  $m = 4$  for quarterly payments)

# Binomial Interest Rate Tree

$$
r _ {1, H} = r _ {1, L} e ^ {2 \sigma}
$$

$$
r _ {1, H} = r _ {0} e ^ {\left(\sigma - 0. 5 \sigma^ {2}\right)}
$$

$$
r _ {1, L} = r _ {0} e ^ {\left(- \sigma - 0. 5 \sigma^ {2}\right)}
$$

$$
r _ {2, H H} = r _ {2, L L} e ^ {4 \sigma}
$$

# Effective Duration

$$
E f f e c t i v e D u r a t i o n = \frac {(P V _ {-}) - (P V _ {+})}{2 \times (\Delta C u r v e) \times P V _ {0}}
$$

# Effective Spread Duration

$$
E f f e c t i v e S p r e a d D u r a t i o n = \frac {(P V _ {-}) - (P V _ {+})}{2 \times (\Delta S p r e a d) \times P V _ {0}}
$$

# Convertible Bond

Convertible bond value  $=$  Value of straight bond + Value of call option on issuer stock

$$
C o n v e r s i o n r a t i o = \frac {C o n v e r t i b l e b o n d p a r v a l u e}{C o n v e r s i o n p r i c e}
$$

$$
C o n v e s s i o n \quad v a l u e = C o n v e s s i o n \quad r a t i o \times C u r r e n t \quad s h a r e \quad p r i c e
$$

# Credit Valuation Adjustment

$$
C r e d i t s p r e a d \approx L G D \times P O D
$$

$$
L G D = 1 - R e c o v e r y R a t e
$$

# Key Financial Ratios

Profitability

$$
E B I T D A m a r g i n = \frac {E B I T D A}{R e v e n u e}
$$

Leverage

$$
D e b t \text {t o} E B I T D A = \frac {\text {T o t a l d e b t}}{E B I T D A}
$$

$$
R C F t o n e t d e b t = \frac {\text {R e t a i n e d c a s h f l o w}}{\text {D e b t} - \text {C a s h a n d m a r k e t a b l e s e c u r i t i e s}}
$$

Coverage

$$
E B I T D A t o i n t e r e s t e x p e n s e = \frac {E B I T D A}{I n t e r e s t e x p e n s e}
$$

$$
E L = L G D \times P O D
$$

$$
L G D = 1 - R e c o v e r y \text {R a t e}
$$

$$
C V A = \Sigma (P V \text {o f} E x p e c t e d L o s s)
$$

# Merger Arbitrage

Arbitrage Spread = Announced acquisition price - Post-announcement market price

# The Merton Model

$$
V _ {0} = c _ {0} + P V (D) - p _ {0}
$$

$V_{0} =$  Firm asset value

$D =$  Risk-free bond's face value

$c_{0} =$  Call option on firm value

$p_0 =$  Put option on firm value

$-p_{0} =$  Sold put option (i.e., Firm's credit spread)

At time  $T$  (i.e., debt matures),

$$
V _ {T} = E _ {T} + D _ {T}
$$

where:

$V_{T} =$  Firm value at time  $T$

$E_{T} = \max [V_{T} - D_{T},0]$  (i.e., Equity value at time  $T$  )

$D_{T} = V_{T} - \max [V_{T} - D_{T},0]$  (i.e., Debt value at time  $T$ )

Based on Black-Scholes-Merton model,

$$
E _ {t} = V _ {t} N \left(d _ {1}\right) - e ^ {- r T} D N \left(d _ {2}\right)
$$

where:

$$
d _ {1} = \frac {\ln \left(\frac {V _ {t}}{D}\right) + \left(r + \frac {1}{2} \sigma^ {2}\right) (T - t)}{\sigma \sqrt {T - t}}
$$

$$
d _ {2} = d _ {1} - \sigma \sqrt {T - t}
$$

$N(x) = \operatorname*{Pr}(Z < x)$  in Standard Normal Distribution

$\sigma =$  Asset volatility

# Credit Spread Implied From Equity Value

$$
\begin{array}{l} R - r = \frac {1}{T - t} \ln \left(\frac {D}{D _ {t}}\right) - r \\ = \frac {1}{T - t} \ln \left(\frac {D}{D - P u t o p t i o n}\right) - r \\ \end{array}
$$

where:

$R - r =$  Credit spread implied from the equity value  $= S_{Equity,Implied}$

$R =$  Yield-to-maturity on issuer's debt

$r =$  Risk-free rate

# Hedge Ratio of Capital Arbitrage Strategy

$$
\frac {d D _ {t}}{d E _ {t}} = \frac {d V _ {t}}{d E _ {t}} - 1 = \frac {1}{N (d _ {1})} - 1
$$

where:

$$
\frac {d E _ {t}}{d V _ {t}} = N (d _ {1})
$$

# Learning Module 6: Private Real Estate Investments

# Net Operating Income

$$
N O I = \begin{array}{c} E f f e c t i v e g r o s s \\ i n c o m e \end{array} - \begin{array}{c} O p e r a t i n g \\ e x p e n s e s \end{array} - \begin{array}{c} P r o p e r t y m a i n t e n a n c e \\ a l l o w a n c e \end{array}
$$

where:

$$
\underset {i n c o m e} {E f f e c t i v e g r o s s} = \underset {r e n t} {G r o s s} + \underset {r e c o v e r y} {O p e r a t i n g} + \underset {i n c o m e} {O t h e r} - V a c a n c i e s - C o n c e s s i o n s
$$

# Project Return

$$
P r o j e c t r e t u r n = \frac {N O I}{P r o j e c t c o s t}
$$

where:

Project cost = Land costs + Land improvements + Construction costs

# Direct Capitalization Approach

$$
P r o p e r t y v a l u e = \frac {E x p e c t e d N O I}{C a p i t a l i z a t i o n r a t e}
$$

# Loan-to-Value (LTV)

$$
L T V = \frac {\text {D e b t o u t s t a n d i n g}}{\text {C u r r e n t p r o p e r t y v a l u e}}
$$

$$
L T V = \frac {D e b t}{D e b t + E q u i t y}
$$

# Debt Service Coverage Ratio (DSCR)

$$
D S C R = \frac {\text {N e t o p e r a t i n g i n c o m e}}{\text {D e b t s e r v i c e}}
$$

# Equity Dividend Rate

$$
E q u i t y d i v i d e n d r a t e = \frac {B e f o r e t a x c a s h f l o w}{P r o p e r t y p e u p r c h a s e p r i c e - D e b t o u t s t a n d i n g}
$$

where:

Before tax cash flow  $=$  NOI - Debt service

# Periodic Payments for a Fully Amortizing Loan

$$
A = \frac {r \times P r i n c i p a l}{1 - (1 + r) ^ {- n}}
$$

where:

$A =$  Periodic payment

$r =$  Interest rate per period

$n =$  Number of periods

If given the annualized interest rate of a loan that is payable monthly:

$$
R _ {m o n t h l y} = (1 + R _ {a n n u a l}) ^ {1 / 1 2} - 1
$$

# Sales Comparison Approach

$$
A d j u s t e d p r i c e p s f = \frac {S a l e p r i c e}{G r o s s s q u a r e f e e t} \times (1 + \% A d j u s t ments)
$$

# Cost Approach

$$
\begin{array}{l} \underset {\text {p r o p e r t y v a l u e}} {\text {E s t i m a t e d}} = \underset {\text {l a n d c o s t}} {\text {C o m p a r a b l e}} + \underset {\text {c o s t}} {\text {C o n s t r u c t i o n}} + \underset {\text {a c c o u n t i n g}} {\text {A r c h i e c t , l e g a l}} + \underset {\text {p a c e r m i t s ,}} {\text {D e v e l o p m e n t}} \\ + \underset {p r o f i t} {C o n t r a c t o r ^ {\prime} s} - \underset {p r o p e r t} {A d j u s t m e n t s f o r} \\ \end{array}
$$

# Discounted Cash Flow Method

$$
P r o p e r t y v a l u e = \sum_ {t = 1} ^ {N} \frac {N O I _ {t}}{(1 + r) ^ {t}} + \frac {T e r m i n a l v a l u e}{(1 + r) ^ {N}}
$$

where:

$$
T e r m i n a l v a l u e = \frac {N O I _ {N} (1 + g)}{C a p r a t e}
$$

$r =$  Required return on equity

# Scenario Analysis

$$
P r o p e r t y v a l u e = \sum_ {i = 1} ^ {n} P r o b a b i l i t y (i) \times P r o p e r t y v a l u e _ {i}
$$

# Timberland

Land Expectation Value (LEV)

$$
L E V = \frac {N F V}{(1 + r) ^ {t} - 1}
$$

where:

$NFV =$  Net future value of a single timber rotation

$$
= \mathrm {P V} \text {o f t i m b e r r o t a t i o n p l a n} \times (1 + r) ^ {t}
$$

$r =$  Required rate of return

$t =$  Length of timber rotation (in years)

Learning Module 7: Infrastructure

# Contract for Difference (CfD)

$$
C f D S e t t l e m e n t = \binom {\text {S t r i k e}} {\text {p r i c e}} - I M R P) \times O u t p u t (M W) \times N u m b e r o f h o u r s
$$

where:

IMRP = Intermittent market reference price (per MWh)

# Electricity Income Based on IMRP

$$
E l e c t r i c i t y \quad i n c o m e = I M R P \times O u t p u t (M W) \times N u m b e r o f h o u r s
$$

# Total income

$$
T o t a l i n c o m e = E \text {E l t r e c i t y} + C f D s e t t l e m e n t
$$

# Loan-to-Value

$$
L T V = \frac {D e b t o u t s t a n d i n g}{C u r r e n t p r o j e c t v a l u e}
$$

# Debt Service Coverage Ratio (DSCR)

$$
D S C R = \frac {N e t c a s h f l o w f r o m o p e r a t i o n s}{D e b t s e r v i c e}
$$

# Equity Dividend Rate

$$
E q u i t y d i v i d e n d r a t e = \frac {B e f o r e t a x n e t c a s h f l o w}{E q u i t y i n v e s t e d}
$$

where:

Before tax cash flow  $=$  Net cash flow from operations - Debt service

# GP's Performance Fee

$$
R _ {G P (N e t w i t h h u r d l e)} = (P _ {1} \times r _ {m}) + \max \{0, [ P _ {1} (1 - r _ {m}) - P _ {0} \times (1 + r _ {h}) ] \times p \}
$$

- Management fee is based on end-of-period assets  
Performance fee is net of management fee and in excess of hurdle rate

where:

$$
P _ {0} = \text {B e g i n n i n g - o f - p e r i o d a s s e t s}
$$

$$
P _ {1} = \text {E n d - o f - p e r i o d a s s e t s}
$$

$$
r_{m} = \text{Management fee, as a}\% \text{of end-of-period AUM}
$$

$$
r _ {h} = \text {H u r d l e r a t e}
$$

$p = \mathrm{GP}$  performance fee as a % of total period return  $(P_{1} - P_{0})$  in excess of a hurdle rate

# Valuation

$$
I n t r i n s i c v a l u e = \sum_ {t = 1} ^ {n} \frac {D _ {t}}{(1 + r _ {t} + \gamma_ {t}) ^ {t}}
$$

where:

$$
D _ {t} = \text {D i v i d e n d s a t t i m e} t
$$

$$
r _ {t} = \text {R i s k - f r e e r a t e} t
$$

$$
\begin{array}{l} \gamma_ {t} = \text {A s s e t - s p e c i f i c r i s k p r e m i u m b a s e d u p o n l e v e r a g e , s i z e , e t c . a t t i m e} t \\ = \text {R i s k f a c t o r} _ {1, t} + \text {R i s k f a c t o r} _ {2, t} + \dots \\ \end{array}
$$

# CFA® Program

# Level III

# PORTFOLIO MANAGEMENT PATHWAY

# FORMULA SHEET (2025) Version 1.0

Prepared by: Fabian Moa, CFA, FRM, CTP, FMVA, AFM, FSA Credential

![](images/d4ebff4c6af515f1a40b2974c58f2a49738f10f5f0ac2ac4be59daacef3280f0.jpg)

# FOR REFERENCE ONLY

# (Note: Formula Sheet is not provided in the CFA exam)

Follow us on:

YouTube

LinkedIn

# NOESIS EXED SDN BHD

Block VO2, Level 5, Unit 8, Lingkaran SV, Sunway Velocity, 55100 Kuala Lumpur, Malaysia

Website: www.noesis.edu.sg

# Table of Contents

Setting Up the Texas BA II Plus Financial Calculator 3  
VOLUME 1 - ASSET ALLOCATION 3  
Learning Module 1: Capital Market Expectations, Part 1: Framework and Macro Considerations...3  
Learning Module 2: Capital Market Expectations, Part 2: Forecasting Asset Class Returns 4  
Learning Module 3: Overview of Asset Allocation. 9  
Learning Module 4: Principles of Asset Allocation 9  
Learning Module 5: Asset Allocation with Real-World Constraints 10  
VOLUME 2 - PORTFOLIO CONSTRUCTION. 11  
Learning Module 1: Passive Equity Investing. 11  
Learning Module 2: Overview of Fixed Income Portfolio Management 11  
Learning Module 3: Asset Allocation to Alternative Investments 13  
Learning Module 4: Overview of Private Wealth Management. 13  
Learning Module 5: Portfolio Management for Institutional Investors 15  
Learning Module 6: Trading Costs and Electronic Markets 16  
Learning Module 7: Case Study in Portfolio Management: Institutional (SWF) 16  
VOLUME 3 - PERFORMANCE MEASUREMENT 17  
Learning Module 1: Portfolio Performance Evaluation 17  
Learning Module 2: Investment Manager Selection. 20  
Learning Module 3: Overview of the Global Investment Performance Standards. 21  
VOLUME 4 - DERIVATIVES AND RISK MANAGEMENT 23  
Learning Module 1: Option Strategies 23  
Learning Module 2: Swaps, Forwards, and Futures Strategies. 25  
Learning Module 3: Currency Management An Introduction 27  
PORTFOLIO MANAGEMENT PATHWAY 29  
Learning Module 1: Index-Based Equity Strategies 29  
Learning Module 2: Active Equity Investing: Strategies 29  
Learning Module 3: Active Equity Investing: Portfolio Construction. 30  
Learning Module 4: Liability-Driven and Index-Based Strategies 32  
Learning Module 5: Yield Curve Strategies 34  
Learning Module 6: Fixed Income Active Management: Credit Strategies 34  
Learning Module 7: Trade Strategy and Execution. 37  
Learning Module 8: Case Study in Portfolio Management: Institutional 38

# CFA Level III – Formula Sheet (2025)

Setting Up the Texas BA II Plus Financial Calculator

Video: https://youtu.be/0MS8d8QOFmc

VOLUME 1 - ASSET ALLOCATION

Learning Module 1: Capital Market Expectations, Part 1: Framework and Macro Considerations

$$
\begin{array}{c} \text {A g g r e g a t e t r e n d} \\ \text {g r o w t h o f e c o n o m y} \end{array} = \begin{array}{c} \text {G r o w t h f r o m} \\ \text {l a b o r i n p u t s} \end{array} + \begin{array}{c} \text {G r o w t h f r o m} \\ \text {l a b o r p r o d u c t i v i t y} \end{array}
$$

where:

$$
\begin{array}{c} G r o w t h f r o m \\ \text {l a b o r i n p u t s} \end{array} = \begin{array}{c} G r o w t h i n p o t e n t i a l \\ \text {l a b o r f o r c e s i z e} \end{array} + \begin{array}{c} G r o w t h i n a c t u a l l a b o r \\ \text {f o r c e p a r t i c a p i t i o n} \end{array}
$$

$$
\begin{array}{c} G r o w t h f r o m \\ \text {l a b o r p r o d u c t i v i t y} \end{array} = \begin{array}{c} G r o w t h f r o m i n c r e a s i n g \\ \text {c a p i t a l i n p u t s} \end{array} + \begin{array}{c} G r o w t h i n t o t a l \\ \text {f a c t o r p r o d u c t i v i t y} \end{array}
$$

Aggregate market value of equity

$$
V _ {t} ^ {e} = G D P _ {t} \times S _ {t} ^ {k} \times P E _ {t}
$$

$$
E q u i t y \quad r e t u r n = C a p i t a l \quad a p p r e c i a t i o n + D i v i d e n d \quad y i e l d
$$

Over a finite horizon:

$$
Equity \text{return} = \% \Delta GDP_{t} + \% \Delta S_{t}^{k} + \% \Delta PE_{t} + \frac{\text{Dividend}}{\text{yield}}
$$

In the long-run:

$$
Equity \text{return} = \% \Delta GDP_{t} + \frac{\text{Dividend}}{\text{yield}}
$$

where:

$$
V _ {t} ^ {e} = \text {A g g r a g e m a t k e t v a l u e o f e q u i t y}
$$

$$
G D P _ {t} = \text {N o m i n a l l e v e l o f G D P}
$$

$$
S _ {t} ^ {k} = \text {S h a r e o f p r o f i t s i n t h e e c o n o m o y} = \frac {E P S _ {t}}{G D P _ {t}}
$$

$$
P E _ {t} = P / E \text {r a t i o}
$$

$$
D i v i d e n d y i e l d = \frac {D i v i d e n d p a y o u t r a t i o}{P r o f i t m u l t i p l e}
$$

Taylor Rule (Video: https://youtu.be/Cl_SShKmOwA)

$$
i ^ {*} = r _ {n e u t r a l} + \pi_ {e} + 0. 5 \big (\hat {Y} _ {e} - \hat {Y} _ {t r e n d} \big) + 0. 5 (\pi_ {e} - \pi_ {t a r g e t})
$$

where:

$i^{*} =$  target nominal policy rate

$r_{\text{neutral}} = \text{real neutral policy rate}$

$\pi_{e} =$  expected inflation rate  $\pi_{target} =$  target inflation rate

$\hat{Y}_e =$  expected real GDP growth rates  $\hat{Y}_{trend} =$  trend real GDP growth rates

$i^{*} - \pi_{e} =$  real, inflation-adjusted policy rate

$$
X - M = (S - I) + (T - G)
$$

where:

$$
X - M = \text {N e t}
$$

$$
S = \text {S a v i n g s}
$$

$$
I = \text {I n v e s t m e n t}
$$

$$
T - G = \text {G o v e r n m e n t}
$$

Learning Module 2: Capital Market Expectations, Part 2: Forecasting Asset Class Returns

# Grinold-Kroner model

Expected equity return

$$
E (R _ {e}) \approx \frac {D}{P} + (\% \Delta E - \% \Delta S) + \% \Delta P / E
$$

where:

$\frac{D}{P} =$  Dividend yield

$\% \Delta E =$  Expected  $\%$  change in total earnings

= Expected nominal earnings growth return

$\% \Delta S =$  Expected  $\%$  change in shares outstanding ( $\% \Delta S < 0$ : Net share repurchases)

$\% \Delta P / E =$  Expected  $\%$  change in price-to-earnings ratio

$=$  Expected repricing return

$\% \Delta E - \% \Delta S =$  Growth rate of earnings per share

$\frac{D}{P} - \% \Delta S =$  Expected cash flow ("income") return

$\% \Delta E + \% \Delta P / E =$  Expected capital gains

In the long run,  $\% \Delta E =$  Nominal GDP growth,  $\% \Delta S = 0, \% \Delta P / E = 0$

Video: https://youtu.be/yOmaMz2YC18

# Risk Premium Approaches to Equity Returns

Equity-vs-bills premium = Term premium + Equity-vs-bond premium

Term premium = Return on bonds - Return on bills

# Singer-Terhaar Approach

Risk premium under full integration:

$$
R P _ {i} ^ {G} = \rho_ {i, G M} \sigma_ {i} \left(\frac {R P _ {G M}}{\sigma_ {G M}}\right)
$$

Risk premium under complete segmentation:

$$
R P _ {i} ^ {S} = 1 \times \sigma_ {i} \times \begin{array}{c} S h a r p e r a t i o o f \\ s e g m e n t e d m a r k e t \end{array}
$$

Singer-Terhaar risk premium,  $RP_{i} = \phi RP_{i}^{G} + (1 - \phi)RP_{i}^{S}$

Expected return of asset class  $i$ ,  $E(R_{i}) = R_{F} + RP_{i}$

where:

$$
\rho_ {i, G M} = \text {c o r r e l a t i o n b e t w e e n i t h a s s e t a n d g l o b a m a k e t p o r t f l o i o}
$$

$$
\sigma_ {i} = \text {s t a n d a r d}
$$

$$
\frac {R P _ {G M}}{\sigma_ {G M}} = \text {S h a r p e}
$$

$$
\phi = \text {D e g r e e o f i n t e g r a t i o n}
$$

$$
R _ {F} = \text {R i s k - f r e e r a t e}
$$

# Note:

- Add liquidity premium where appropriate  
- If Sharpe ratio of segmented market not given, use Sharpe ratio of global market portfolio

Video: https://youtu.be/RK2WETqIzoQ

# Risk Premium (Building Block) Approach to Fixed Income Returns

<table><tr><td>Bond</td><td>Required Return</td></tr><tr><td>Short-term fixed-rate government bill</td><td>Real risk-free rate + Inflation premium</td></tr><tr><td>Long-term fixed-rate government bond</td><td>Real risk-free rate + Inflation premium + Maturity premium</td></tr><tr><td>Long-term inflation-linked government bond</td><td>Real risk-free rate + Maturity premium</td></tr><tr><td>Long-term fixed-rate corporate bond</td><td>Real risk-free rate + Inflation premium + Maturity premium + Credit premium</td></tr><tr><td>Long-term callable fixed-rate corporate bond</td><td>Real risk-free rate + Inflation premium + Maturity premium + Credit premium + Call risk</td></tr></table>

# Real Estate

Long-run:

$$
E \left(R _ {r e}\right) = C a p r a t e + N O I g r o w t h r a t e
$$

Finite horizon:

$$
E \left(R _ {r e}\right) = C a p r a t e + N O I g r o w t h r a t e - \% \Delta C a p r a t e
$$

# Capital Flows

In the long run

$$
\begin{array}{l} E \left(\% \Delta S _ {d / f}\right) = \left(r ^ {d} - r ^ {f}\right) + \left(T e r m ^ {d} - T e r m ^ {f}\right) + \left(C r e d i t ^ {d} - C r e d i t ^ {f}\right) \\ + (E q u i t y ^ {d} - E q u i t y ^ {f}) + (L i q u i d ^ {d} - L i q u i d ^ {f}) \\ \end{array}
$$

# Currency

For a currency pair,  $d / f$ , if  $f$  changes by  $x\%$  against  $d$ , then  $d$  changes by  $\frac{1}{1 + x} - 1$  against  $f$ .

# VCV Matrix with Sample Statistics

With  $N$  assets, required:

-  $N$  variances  
$\frac{N(N - 1)}{2}$  covariances

# VCV Matrices from Multi-Factor Models

Return on ith asset:

$$
r _ {i} = \alpha_ {i} + \sum_ {k = 1} ^ {K} \beta_ {i K} F _ {K} + \varepsilon_ {i}
$$

Variance of the ith asset:

$$
\sigma_ {i} ^ {2} = \sum_ {m = 1} ^ {K} \sum_ {n = 1} ^ {K} \beta_ {i m} \beta_ {i n} \rho_ {m n} + \nu_ {i} ^ {2}
$$

Covariance between ith and jth asset:

$$
\sigma_ {i j} = \sum_ {m = 1} ^ {K} \sum_ {n = 1} ^ {K} \beta_ {i m} \beta_ {j n} \rho_ {m n}
$$

With  $N$  assets and  $K$  factors, required:

-  $(N \times K)$  factor sensitivities  
$K(K + 1)$  factor covariances

where:

$$
\alpha_ {i} = \text {I n t e r c e p t}
$$

$\beta_{iK} =$  Asset's sensitivity to the kth factor

$$
F _ {K} = k \text {t h c o m m o n f a c t o r r e t u r n}
$$

$$
\varepsilon_ {i} = \text {s t o c h a s t i c t e r m (m e a n = z e r o)}
$$

$$
\rho_ {m n} = \text {c o r r e l a t i o n b e t w e e n m t h a n d n t h f a c t o r s}
$$

$\nu_{i}^{2} =$  variance of unique component of ith asset's return

Video: https://youtu.be/XVpJ8yuTngo

# Smoothed Returns

$$
R _ {t} = (1 - \lambda) r _ {t} + \lambda R _ {t - 1} \quad 0 <   \lambda <   1
$$

$$
v a r (r) = \left(\frac {1 + \lambda}{1 - \lambda}\right) v a r (R)
$$

where:

$$
R _ {t} = \text {C u r r e n t o b s e r v e d r e t u r n}
$$

$$
R _ {t - 1} = \text {P r e v i o u s o b s e r v e d r e t u r n}
$$

$$
r _ {t} = \text {C u r r e n t t r u e r e t u r n}
$$

$$
v a r (r) = \text {T r u e}
$$

# ARCH Model

$$
\begin{array}{l} \sigma_ {t} ^ {2} = \gamma + \alpha \sigma_ {t - 1} ^ {2} + \beta \eta_ {t} ^ {2} \quad \gamma , \alpha , \beta \geq 0, \alpha + \beta <   1 \\ = \gamma + (\alpha + \beta) \sigma_ {t - 1} ^ {2} + \beta \left(\eta_ {t} ^ {2} - \sigma_ {t - 1} ^ {2}\right) \\ \end{array}
$$

where:

$$
\begin{array}{l} \sigma_ {t} ^ {2} = \text {V a r i a n c e} t \\ \eta_ {t} = \text {U n e x p e c t e d c o m p o n e n t o f r e t u r n i n p e r i o d} t (\text {m e a n} = 0) \\ \eta_ {t} ^ {2} - \sigma_ {t - 1} ^ {2} = \text {S h o c k t o v a r i a n c e i n p e r i o d} t \\ \end{array}
$$

Unconditional expected value of variance

$$
\frac {\gamma}{1 - \alpha - \beta}
$$

Learning Module 3: Overview of Asset Allocation

Economic Net Worth = Economic Assets - Economic Liabilities

Economic Assets = Financial Assets + Extended Assets

Economic Liabilities = Financial Liabilities + Extended Liabilities

Learning Module 4: Principles of Asset Allocation

# Mean-Variance Optimization

# Utility

$$
U _ {m} = E (R _ {m}) - 0. 0 0 5 \lambda \sigma_ {m} ^ {2}
$$

where:

$U_{m} =$  Investor's utility for asset mix,  $m$

$R_{m} =$  Return for asset mix,  $m$

$\lambda =$  Investor's risk aversion coefficient

$\sigma_{m}^{2} =$  Expected variance of return for asset mix  $m$  (in  $\%$

Surplus  $=$  Market value of assets - Present value of liabilities

Funding ratio =  $\frac{\text{Market value of assets}}{\text{Present value of liabilities}}$

# Surplus Optimization

$$
U _ {m} ^ {L R} = E \big (R _ {s, m} \big) - 0. 0 0 5 \lambda \sigma_ {s, m} ^ {2}
$$

where:

$U_{m}^{LR} =$  Surplus objective function's expected value for asset mix m

[ E\left(R_{s,m}\right) = \text{Expected surplus return for asset mix } m ]  
$= \frac{\text{Change in asset value} - \text{Change in liability value}}{\text{Initial asset value}}$

$\sigma_{s,m} =$  Surplus return volatility for asset mix  $m$

$\lambda =$  Investor's risk aversion

# Goals-based Asset Allocation

Video: https://youtu.be/ufo0cNWmfbo

# Risk Parity

$$
w _ {i} \times C o v (r _ {i}, r _ {p}) = \frac {1}{n} \sigma_ {p} ^ {2}
$$

where:

$$
w _ {i} = \text {W e i g h t o f a s s e t} i
$$

$\text{Cov}\left( {{r}_{i},{r}_{p}}\right)  =$  Covariance of asset  $i$  with portfolio

$$
n = \text {N u m b e r o f a s s e t s}
$$

$$
\sigma_ {p} ^ {2} = \text {V a r i a n c e o f p o r t f o l i o}
$$

# Risk Budgeting

Marginal Contribution to Risk

$$
M C T R = \begin{array}{c} A s s e t b e t a r e l a t i v e \\ t o p o r t f o l i o \end{array} \times \begin{array}{c} P o r t f o l i o s t a n d a r d \\ d e v i a t i o n \end{array}
$$

Actual Contribution to Risk

$$
A C T R = \frac {\text {A s s e t w e i g h t}}{\text {i n p o r t f o l i o}} \times M C T R
$$

Ratio of excess return to MCTR = Expected return - Risk free rate / MCTR

Learning Module 5: Asset Allocation with Real-World Constraints

# After-tax Portfolio Optimization

$$
r _ {a t} = r _ {p t} (1 - t)
$$

$$
\sigma_ {a t} = \sigma_ {p t} (1 - t)
$$

$$
R R _ {a t} = \frac {R R _ {p t}}{1 - t}
$$

where:  $r_{at} =$  Expected after-tax return

$$
\begin{array}{l} r _ {p t} = \text {E x p e c t e d p r e - t a x r e t u r n} \\ t = \text {E x p e c t e d} \\ \end{array}
$$

$\sigma_{at} =$  Expected after-tax standard deviation

$\sigma_{pt} =$  Expected pre-tax standard deviation

$RR_{at} =$  After-tax rebalancing range

$RR_{pt} = \text{Pre-tax rebalancing range}$

Learning Module 1: Passive Equity Investing

Herfindahl Hirschman Index (HHI)

$$
H H I = \sum_ {i = 1} ^ {n} w _ {i} ^ {2}
$$

where:  $w_{i} =$  Weight of stock  $i$  in portfolio

$$
E f f e c t i v e n u m b e r o f s t o c k s = \frac {1}{H H I}
$$

$$
T r a c k i n g e r r o r _ {p} = \sqrt {V a r i a n c e} _ {R _ {p} - R _ {b}}
$$

$$
E x c e s s r e t u r n _ {p} = R _ {p} - R _ {b}
$$

Learning Module 2: Overview of Fixed Income Portfolio Management

Expected fixed-income return

$$
\begin{array}{l} E (R) = \text {Y i e l d i n c o m e} + \text {R o l l d o w n r e t u r n} \\ + E (C h a n g e i n p r i c e b a s e d o n i n v e s t o r ^ {\prime} s v i e w o f b e n c h m a r k y i e l d) \\ + E (C h a n g e i n p r i c e b a s e d o n i n v e s t o r ^ {\prime} s v i e w o f y i e l d s p r e a d s) \\ + E (C h a n g e i n p r i c e b a s e d o n i n v e s t o r ^ {\prime} s v i e w o f c u r r e n c y v a l u e c h a n g e s) \\ \end{array}
$$

$$
\begin{array}{c} Y i e l d i n c o m e \\ (o r c u r r e n t y i e l d) \end{array} = \frac {A n n u a l c o u p o n p a y m e n t}{C u r r e n t b o n d p r i c e}
$$

$$
\text {R o l l d o w n r e t u r n} = \frac {\text {P r i c e} _ {\text {E n d}} - \text {P r i c e} _ {0}}{\text {P r i c e} _ {0}} \quad (\text {A s s u m e n o c h a n g e i n y i e l d c u r v e})
$$

Rolling yield  $=$  Yield income + Rolldown return

$$
E \left( \begin{array}{c} C h a n g e i n p r i c e b a s e d \\ o n i n v e s t o r ^ {\prime} s v i e w o f \\ b e n c h m a r k y i e l d \end{array} \right) = - M o d D u r \times \Delta Y i e l d + \frac {1}{2} \times C o n v e x i t y \times (\Delta Y i e l d) ^ {2}
$$

$$
\begin{array}{l} E \left( \begin{array}{c} C h a n g e i n p r i c e b a s e d \\ o n i n v e s t o r ^ {\prime} s v i e w o f \\ y i e l d s p r e a d s \end{array} \right) \\ = - S p r e a d D u r \times \Delta S p r e a d + \frac {1}{2} \times S p r e a d C o n v e x i t y \times (\Delta S p r e a d) ^ {2} \\ \end{array}
$$

For foreign fixed income investments:

$$
R _ {D C} = \left(1 + R _ {F C}\right) \left(1 + R _ {F X}\right) - 1
$$

$$
\begin{array}{l} R _ {F C} = \text {Y i e l d i n c o m e} + \text {R o l l d o w n r e t u r n} \\ + E (\text {C h a n g e i n p r i c e b a s e d o n i n v e s t o r} ^ {\prime} \text {s v i e w o f b e n c h m a r k y i e l d}) \\ + E (C h a n g e i n p r i c e b a s e d o n i n v e s t o r ^ {\prime} s v i e w o f y i e l d s p r e a d s) \\ \end{array}
$$

$$
\begin{array}{l} R _ {F X} = \text {P e r c e n t a g e} \\ = \frac {E \left(S _ {D C / F C}\right) - S _ {0 , D C / F C}}{S _ {0 , D C / F C}} \quad (u n h e d g e d) \\ = \frac {F _ {D C / F C} - S _ {0 , D C / F C}}{S _ {0 , D C / F C}} \quad (h e d g e d) \\ \end{array}
$$

# Using Leverage in the Bond Portfolio

Leveraged portfolio return

$$
r _ {P} = r _ {I} + \frac {V _ {B}}{V _ {E}} (r _ {I} - r _ {B})
$$

where:

$$
r _ {I} = \text {r e t u r n o n i n v e s t e d f u n d s}
$$

$$
r _ {B} = \text {c o s t}
$$

$$
V _ {B} = \text {b o r r o w e d f u n d s}
$$

$$
V _ {E} = \text {v a l u e o f p o r t f i l o i o s e q u i t y}
$$

Video: https://youtu.be/NadocNKzDBw

Futures

$$
L e v e r a g e _ {F u t u r e s} = \frac {N o t i o n a l v a l u e - M a r g i n}{M a r g i n}
$$

Repo

$$
D o l l a r i n t e r e s t = P r i n c i p a l \times R e p o r a t e \times \frac {T e r m o f r e p o i n d a y s}{3 6 0}
$$

# Securities Lending

$$
R e b a t e r a t e = C o l l a t e r a l \quad e a n i n g s \quad r a t e - S e c u r i t y \quad l e n d i n g \quad r a t e
$$

# Cash Flow Matching

$$
\begin{array}{c} \text {R e q u i r e d p a r v a l u e} \\ \text {f o r t h e l o n g e s t} \\ \text {m a t u r i t y b o n d} \end{array} = \frac {\text {A m o u n t o f f i n a l l i a b i l i t y d u e}}{1 + \text {C o u p o n r a t e o f t h e l o n g e s t m a t u r i t y b o n d}}
$$

Video: https://youtu.be/fB257bEp59c

$$
C o n v e x i t y = \frac {M a c D u r ^ {2} + M a c D u r + D i s p e r s i o n}{(1 + C a s h f l o w y i e l d) ^ {2}}
$$

Learning Module 3: Asset Allocation to Alternative Investments

# Unsmoothed Returns

$$
r _ {t, u n s m o o t h e d} = \frac {r _ {t , r e p o r t e d} - s \times r _ {t - 1 , r e p o r t e d}}{1 - s}
$$

where:  $s =$  Serial correlation

# Net Asset Value (NAV)

$$
N A V _ {t} = N A V _ {t - 1} \times (1 + G) + C _ {t} - D _ {t}
$$

where:

$$
C _ {t} = R C _ {t} \times \left(C C - P I C _ {t}\right)
$$

$$
D _ {t} = R D _ {t} \times [ N A V _ {t - 1} \times (1 + G) ]
$$

Learning Module 4: Overview of Private Wealth Management

$$
H u m a n C a p i t a l = \sum_ {t = 1} ^ {N} \frac {p (s _ {t}) \times w _ {t - 1} \times (1 + g _ {t})}{\left(1 + r _ {f} + y\right) ^ {t}}
$$

where:

$$
p \left(s _ {t}\right) = \text {P r o b a b i l i t y}
$$

$$
w _ {t - 1} = \text {I n c o m e f r o m e m p l o y m e n t i n p e r i o d} t - 1
$$

$$
g _ {t} = \text {A n n u a l w a g e g r o w t h r a t e}
$$

$$
r _ {f} = \text {N o m i n a l}
$$

$$
y = \text {R i s k p r e m i u m a s s o c i a t e d w i t h o c o u p u t a t i o n a l i n c o m e v o l a t i l i t y}
$$

$$
N = \text {L e n g t h o f w o r k i n g l e}
$$

# Taxes on Income

$$
A v e r a g e t a x r a t e = \frac {T a x l i a b i l i t y}{T a x a b l e i n c o m e}
$$

# Accrual Taxes on Investment Returns

After-tax future value of a $1 investment, with returns taxed annually:

$$
F V _ {A T} = [ 1 + R (1 - t _ {x}) ] ^ {T}
$$

where:

PV = Initial investment

$R =$  Pretax return

$t_{x} = \text{Tax rate on investment income}$

$T =$  Investment period (in years)

$$
\begin{array}{l} T a x d r a g = \frac {D i f f e r e n c e i n i n v e s t m e n t g a i n s w i t h a n d w i t h o u t t a x e s}{I n v e s t m e n t g a i n s w i t h o u t t a x e s} \\ = \frac {(1 + R) ^ {T} - [ 1 + R (1 - t _ {x}) ] ^ {T}}{(1 + R) ^ {T} - 1} \\ \end{array}
$$

After-tax inflation-adjusted future value of a $1 investment (accrual taxes):

$$
F V _ {A T, i n f l} = \left[ \frac {1 + R (1 - t _ {x})}{1 + i n f l} \right] ^ {T}
$$

# Deferral of Taxes on Capital Gains

After-tax future value of a \(1 investment, with deferred capital gains taxed at t_{CG} and the cost basis, B, expressed as percentage of the current market value of the investment:

$$
F V _ {C G} = (1 + R) ^ {T} \left(1 - t _ {C G}\right) + t _ {C G} \times B
$$

$$
T a x d r a g = \frac {(1 + R) ^ {T} - [ (1 + R) ^ {T} (1 - t _ {C G}) + t _ {C G} \times B ]}{(1 + R) ^ {T} - 1}
$$

After-tax inflation-adjusted future value of a $1 investment:

$$
F V _ {C G, i n f l} = \frac {(1 + R) ^ {T} (1 - t _ {C G}) + t _ {C G} \times B}{(1 + i n f l) ^ {T}}
$$

# Defined Benefit Pension Plan

$$
F u n d e d r a t i o = \frac {F a i r v a l u e o f p l a n a s s e t s}{P r e s e n t v a l u e o f d e f i n e d b e n e f i t o b l i g a t i o n s}
$$

$$
F u n d e d s t a t u s = \frac {F a i r v a l u e o f}{p l a n a s s e t s} - \frac {P r e s e n t v a l u e o f d e f i n e d}{b e n e f i t o b l i g a t i o n s}
$$

# Spending Policies (Endowment and Foundation)

Constant Growth rule:

$$
S p e n d i n g _ {t + 1} = S p e n d i n g _ {t} \times (1 + I n f l a t i o n R a t e)
$$

Market Value rule:

$$
S p e n d i n g _ {t + 1} = S p e n d i n g r a t e \times A v e r a g e A U M
$$

Hybrid rule:

$$
S p e n d i n g _ {t + 1} = w \times \begin{array}{c} C o n s t a n t G r o w t h \\ r u l e \end{array} + (1 - w) \times \begin{array}{c} M a r k e t v a l u e \\ r u l e \end{array}
$$

# Bank and Insurance

Duration of equity capital,  $D_{E}$

$$
D _ {E} = \left(\frac {A}{E}\right) D _ {A} - \left(\frac {A}{E} - 1\right) D _ {L} \left(\frac {\Delta i}{\Delta y}\right)
$$

$$
\sigma_ {\Delta E / E} ^ {2} = \left(\frac {A}{E}\right) ^ {2} \sigma_ {\Delta A / A} ^ {2} + \left(\frac {A}{E} - 1\right) ^ {2} \sigma_ {\Delta L / L} ^ {2} - 2 \left(\frac {A}{E}\right) \left(\frac {A}{E} - 1\right) \rho \sigma_ {\Delta A / A} \sigma_ {\Delta L / L}
$$

Equity capital ratio  $= \frac{E}{A}$

$$
D _ {A} = \text {D u r a t i o n o f a s s e t s}
$$

$$
D _ {L} = \text {D u r a t i o n o f l i a b i l i t i e s}
$$

$$
i = \text {E f f e c t i v e}
$$

$$
y = \text {E f f e c t i v e}
$$

$$
\sigma_ {\Delta E / E} ^ {2} = \text {V a r i a n c e o f c h a n g e i n v a l u e o f e q u i t y c a p i t a l}
$$

$$
\sigma_ {\Delta A / A} ^ {2} = \text {V a r i a n c e o f c h a n g e i n v a l u e o f a s s e t s}
$$

$$
\sigma_ {\Delta L / L} ^ {2} = \text {V a r i a n c e o f c h a n g e i n v a l u e o f l i a b i l i t i e s}
$$

$$
\rho = \text {C o r r e l a t i o n b e t w e e n p e r t a g e v a l u e c h a n g e s o f a s s e t s a n d l i a b i l i t i e s}
$$

# Learning Module 6: Trading Costs and Electronic Markets

Effectivesspread  $=$  Trade size  $\times$  {Trade price-Midquote price for buy orders  $=$ $M i d q u o t e p r i c e - T r a d e p r i c e$  for sell orders

$$
E f f e c t i v e s p r e a d = \left\{ \begin{array}{l l} 2 \times (T r a d e p r i c e - M i d q u o t e p r i c e) & f o r b u y o r d e r s \\ 2 \times (M i d q u o t e p r i c e - T r a d e s i z e) & f o r s e l l o r d e r s \end{array} \right.
$$

where:

$$
M i d q u o t e p r i c e = \frac {B i d + A s k}{2}
$$

$$
\begin{array}{c} V W A P \text {t r a n s a c t i o n} \\ \text {c o s t e s t i m a t e} \end{array} = \text {T r a d e s i z e} \times \left\{ \begin{array}{l l} \text {T r a d e V W A P - M i d q u o t e p r i c e} & \text {f o r b u y o r d e r s} \\ \text {M i d q u o t e p r i c e - T r a d e V W A P} & \text {f o r s e l l o r d e r s} \end{array} \right.
$$

# Learning Module 7: Case Study in Portfolio Management: Institutional (SWF)

No formula.

Learning Module 1: Portfolio Performance Evaluation

Arithmeticexcessreturn  $= R - B$

Geometric excess return  $= \frac{R - B}{1 + B}$

# Attribution based on Factor Models

Active Return  $=$  Return from factor tilt + Security selection return

$$
R - B = \sum \left(\beta_ {P, i} - \beta_ {B, i}\right) \times F _ {i} + S e c u r i t y s e l e c t i o n r e t u r n
$$

where:

$$
\beta_ {P, i} = \text {S e n s i t i v i t y o f t h e p o r t f i l o o t o t h e g i v e n f a c t o r}
$$

$$
\beta_ {B, i} = \text {S e n s i t i v i t y o f t h e b e n c h m a r k t o t h e g i v e n f a c t o r}
$$

$$
F _ {i} = \text {F a c t o r}
$$

# Micro and Macro Return Attribution

$$
R - B = \sum_ {i = 1} ^ {n} A _ {i} + \sum_ {i = 1} ^ {n} S _ {i} + \sum_ {i = 1} ^ {n} I _ {i}
$$

where:

$$
w _ {i} = \text {W e i g h t o f a s s e t} i \text {i n p o r t f o l i o}
$$

$$
W _ {i} = \text {W e i g h t o f a s s e t} i \text {i n b e n c h m a r k}
$$

$$
R _ {i} = \text {R e t u r n o f a s s e t} i \text {i n p o r t f o l i o}
$$

$$
B _ {i} = \text {R e t u r n o f a s s e t} i \text {i n b e n c h m a r k}
$$

Video: https://youtu.be/yrzTVIfqloM

# Brinson-Fachler Model

Allocation effect:  $A_{i} = (w_{i} - W_{i})(B_{i} - B)$

Selection effect:  $S_{i} = W_{i}(R_{i} - B_{i})$

Interaction effect:  $I_{i} = (w_{i} - W_{i})(R_{i} - B_{i})$

# Brinson-Hood-Beebower Model (BHB)

Allocation effect:  $A_{i} = (w_{i} - W_{i})B_{i}$

Selection effect:  $S_{i} = W_{i}(R_{i} - B_{i})$

Interaction effect:  $I_{i} = (w_{i} - W_{i})(R_{i} - B_{i})$

# Decomposing Portfolio Returns

$$
P = M + S + A
$$

where:

$$
P = \text {P o r t f l o i r o}
$$

$$
M = \text {M a r k e t i n d e x r e t u r n}
$$

$$
B = \text {B e n c h m a r k}
$$

$$
S = B - M = \text {S t y l e}
$$

$$
A = P - B = \text {A c t i v e r e t u r n (T r u e a c t i v e r e t u r n)}
$$

# Performance Appraisal

# Sharpe Ratio

$$
S h a r p e r a t i o = \frac {R _ {p} - r _ {f}}{\sigma_ {p}}
$$

where:

$$
R _ {p} = \text {P o r t f o l i o r e t u r n}
$$

$$
r _ {f} = \text {R i s k - f r e e r a t e}
$$

$$
\sigma_ {p} = \text {P o r t f o l i o s t a n d a r d d e v i a t i o n}
$$

# Treynor Ratio

$$
T r e y n o r r a t i o = \frac {R _ {p} - r _ {f}}{\beta_ {p}}
$$

where:

$$
R _ {p} = \text {P o r t f o l i o r e t u r n}
$$

$$
r _ {f} = \text {R i s k - f r e e r a t e}
$$

$$
\beta_ {p} = \text {P o r t f o l i o b e t a (S y s t e m a t i c r i s k)}
$$

# Information Ratio

$$
I n f o r m a t i o n r a t i o = \frac {R _ {p} - R _ {B}}{\sigma_ {R _ {p} - R _ {B}}}
$$

where:

$$
R _ {p} = \text {P o r t f i l o}
$$

$$
R _ {B} = \text {B e n c h m a r k}
$$

$$
\sigma_ {R _ {p} - R _ {B}} = \text {A c t i v e r i s k (T r a c k i n g r i s k / T r a c k i n g e r r o r)}
$$

# Appraisal Ratio

$$
A p p r a i s a l r a t i o (T r e y n o r B l a c k r a t i o) = \frac {\alpha}{\sigma_ {\varepsilon}}
$$

where:

$$
\begin{array}{l} \sigma_ {\varepsilon} = \text {S t a n d a r d e r r o f r e g r e s s i o n (f r o m f a c t o r m o d e l)} \\ = \sqrt {\sigma_ {P} ^ {2} - \beta_ {i} ^ {2} \sigma_ {M} ^ {2}} \\ \end{array}
$$

$$
\alpha = R _ {i} - \left[ R _ {f} + \beta_ {i} \big (R _ {M} - R _ {f} \big) \right]
$$

# Sortino Ratio

$$
\text {S o r t i n o r a t i o} = \frac {R _ {p} - r _ {T}}{\sigma_ {\text {D o w n s i d e}}}
$$

where:

$$
\begin{array}{l} r _ {T} = \text {I n v e s t o r} ^ {\prime} \text {s m i n i m u m a c c e p t a b l e r e t u r n / t a r g e t r e t u r n} \\ \sigma_ {D o w n s i d e} = \sqrt {\frac {1}{N} \sum_ {t = 1} ^ {N} \min (r _ {t} - r _ {T} , 0) ^ {2}} \\ \end{array}
$$

# Capture Ratio

$$
C a p t u r e \: R a t i o = \frac {U p s i d e \: C a p t u r e}{D o w n s i d e \: C a p t u r e}
$$

$$
U p s i d e C a p t u r e = \frac {R _ {m}}{R _ {B}} \quad R _ {B} \geq 0
$$

$$
D o w n s i d e C a p t u r e = \frac {R _ {m}}{R _ {B}} \quad R _ {B} <   0
$$

where:

$$
\begin{array}{l} R _ {m} = \text {M a n a g e r ' s} \\ R _ {B} = \text {B e n c h m a r k} \\ \end{array}
$$

# Maximum Drawdown

$$
M a x i m u m D r a w d o w n = \min \left(\left[ \frac {V (m , t) - V (m , t ^ {*})}{V (m , t ^ {*})} \right], 0\right)
$$

where:

$$
V (m, t) = \text {p o r t f i l o o v e} m \text {a t} t
$$

$$
V (m, t ^ {*}) = \text {p e a k p o r t f i l o v a l u e o f m a n a g e r} m
$$

$$
t > t ^ {*}
$$

Video: https://youtu.be/0tRDDT9E9AU

Learning Module 2: Investment Manager Selection

# Performance-Based Fees

If manager is fully exposed to upside and downside:

$$
\text {C o m p u t e d f e e} = \text {B a s e f e e} + \text {S h a r i n g o f p e r f e r m a n c e}
$$

If manager not exposed to downside:

Computed fee = Higher of either [1] Base fee, OR  
[2] Base fee plus sharing of positive performance

If manager is not exposed to downside, and there is a maximum fee.

Computed fee = Higher of either [1] Base fee, OR

[2] Base fee plus sharing of performance, to a maximum fee

# Time-weighted return

$$
r _ {t w r} = \left(1 + r _ {t, 1}\right) \times \left(1 + r _ {t, 2}\right) \times \ldots \times \left(1 + r _ {t, n}\right) - 1
$$

$r_{t,1}$  through  $r_{t,n} = \text{Sub-period returns}$

# Modified Dietz method

$$
r _ {M o d D i e t z} = \frac {V _ {1} - V _ {0} - C F}{V _ {0} + \sum_ {i = 1} ^ {n} (C F _ {i} \times w _ {i})}
$$

Video: https://youtu.be/guZWVXirJLO

# Modified IRR method

$$
V _ {1} = \sum_ {i = 1} ^ {n} [ C F _ {i} \times (1 + M I R R) ^ {w _ {i}} ] + V _ {0} (1 + M I R R)
$$

where:

$w_{i} =$  Proportion of period (in days) that each cash flow has been in the portfolio

$$
= \frac {C D - D _ {i}}{C D}
$$

$CD =$  Total number of calendar days in the period

$D_{i} =$  Number of calendar days from the beginning of the period to the time cash flow  $CF_{i}$  occurs

$$
C F = \sum_ {i = 1} ^ {n} C F _ {i}
$$

# Composite Time-Weighted Return

Asset-weight individual portfolio returns using beginning-of-period values

$$
r _ {C} = \sum_ {p i = 1} ^ {n} r _ {p i} \times \frac {V _ {0 , p i}}{\sum_ {p i = 1} ^ {n} V _ {0 , p i}}
$$

where:

$$
r _ {C} = \text {C o m p o s i t e r e t u r n}
$$

$$
r _ {p i} = \text {R e t u r n o f a n i n d i v i d u a l p o r t f i l i o} i
$$

$V_{0,pi} =$  Beginning value of portfolio  $i$

$\sum_{pi=1}^{n} V_{0,pi} = \text{Total beginning fair value of all individual portfolios in the composite}$

Use a method that reflects both beginning-of-period values and external cash flows

$$
r _ {C} = \sum_ {p i = 1} ^ {n} r _ {p i} \times \frac {V _ {p i}}{\sum_ {p i = 1} ^ {n} V _ {p i}}
$$

where:

$V_{pi} =$  Beginning value of portfolio  $i +$  Weighted external cash flows

$\sum_{pi=1}^{n} V_{pi} = \text{Total beginning fair value and weighted external cash flows of all individual portfolios in the composite}$

# Aggregate Return Method

$$
r _ {M o d D i e t z} = \frac {V _ {1} - V _ {0} - C F}{V _ {0} + \sum_ {i = 1} ^ {n} (C F _ {i} \times w _ {i})}
$$

where:

$V_{1} =$  Ending value of composite

$V_{0} =$  Beginning value of composite

$$
C F = \underset {c a s h f l o w s i n c o m p o s i t e} {T o t a l o f e x t e r n a l} = \sum_ {i = 1} ^ {n} C F _ {i}
$$

$$
\sum_ {i = 1} ^ {n} \left(C F _ {i} \times w _ {i}\right) = \frac {\text {T o t a l o f w e i g h t e d e x t e r n a l}}{\text {c a s h f l o w s i n c o m p o s i t e}} = \sum_ {p i = 1} ^ {n} V _ {p i}
$$

# Equal-weighted standard deviation

$$
S _ {c} = \sqrt {\frac {\sum_ {i = 1} ^ {n} (r _ {i} - \bar {r} _ {c}) ^ {2}}{n}}
$$

where:

$$
r _ {i} = \text {r e t u r n f o r p o r t f i l o i}
$$

$$
\bar {r} _ {c} = \text {e q u a l - w e i g h t e d m e a n}
$$

$$
n = \text {n u m b e r o f p o r t f o l i o s i n c o m p o s i t e}
$$

# Asset-weighted standard deviation

$$
S _ {c, a w} = \sqrt {\sum_ {i = 1} ^ {n} w _ {i} \times \left(r _ {i} - \bar {r} _ {p r o x y}\right) ^ {2}}
$$

$$
\begin{array}{l} \bar {r} _ {\text {p r o x y}} = \text {a s s e t - w e i g h t e d m e a n r e t u r n} \\ = \sum_ {i = 1} ^ {n} w _ {i} \times r _ {i} \\ \end{array}
$$

$$
w _ {i} = \text {w e i g h t o f p o r t f o l i o} i = \frac {V _ {0 , i}}{V _ {0 , T o t a l}}
$$

# Learning Module 1: Option Strategies

Put-call parity

$$
S _ {0} + p _ {0} = c _ {0} + \frac {X}{(1 + r) ^ {T}}
$$

Put-call-forward parity

$$
\frac {F _ {0}}{(1 + r) ^ {T}} + p _ {0} = c _ {0} + \frac {X}{(1 + r) ^ {T}}
$$

Synthetic long forward

$$
c _ {0} - p _ {0} = \frac {F _ {0} - X}{(1 + r) ^ {T}}
$$

Option premium = Time value + Intrinsic value

# Covered Calls

Video: https://youtu.be/2SocH6PghOk

Expiration value  $= S_{T} - \operatorname{Max}(S_{T} - X, 0)$

Profit at Expiration  $= S_{T} - \text{Max}(S_{T} - X, 0) + c_{0} - S_{0}$

Maximum gain  $= X - S_{0} + c_{0}$

Maximum loss  $= S_{0} - c_{0}$

Breachaven price  $= S_{0} - c_{0}$

Position delta = Stock Delta - Call Delta = 1 -  $\Delta_{call}$

Position gamma = Stock Gamma - Call Gamma = -Gamma<0

Position vega = Stock Vega - Call Vega = -Vega call < 0

Position theta = Stock Theta - Call Theta = -Theta<0

# Protective Puts

Video: https://youtu.be/VLK1IXbXtRk

Expiration value  $= S_{T} + \text{Max}(X - S_{T}, 0)$

Profit at Expiration  $= S_{T} + \text{Max}(X - S_{T}, 0) - S_{0} - p_{0}$

Maximum gain  $= \infty$

Maximum loss  $= S_{0} - X + p_{0}$

Breakeven price  $= S_{0} + p_{0}$

Position delta = Stock Delta + Put Delta = 1 +  $\Delta_{put}$

Position gamma = Stock Gamma + Put Gamma = Gamma $_{put}$  > 0

Position Vega = Stock Vega + Put Vega = Vega $_{put}$  > 0

Position theta = Stock Theta + Put Theta = Theta<sub>put</sub> < 0

# Call Bull Spread

Video: https://youtu.be/3NHwelzEU0k

Expiration value  $= \text{Max}(S_T - X_L, 0) - \text{Max}(S_T - X_H, 0)$

Profit at Expiration  $= \text{Max}(S_T - X_L, 0) - \text{Max}(S_T - X_H, 0) - (c_L - c_H)$

Maximum gain  $= X_{H} - X_{L} - (c_{L} - c_{H})$

Maximum loss  $= c_{L} - c_{H}$

Breachaven price  $= X_{L} + c_{L} - c_{H}$

# Put Bull Spread

Video: https://youtu.be/Lf1Fi-zy7w4

Expiration value  $= \text{Max}(X_L - S_T, 0) - \text{Max}(X_H - S_T, 0)$

Profit at Expiration  $= \operatorname{Max}(X_L - S_T, 0) - \operatorname{Max}(X_H - S_T, 0) - (p_L - p_H)$

Maximum gain  $= p_{H} - p_{L}$

Maximum loss  $= X_{H} - X_{L} + p_{L} - p_{H}$

Breakeven price  $= X_{H} + p_{L} - p_{H}$

# Put Bear Spread

Video: https://youtu.be/eTejezNXZbU

Expiration value  $= \text{Max}(X_H - S_T, 0) - \text{Max}(X_L - S_T, 0)$

Profit at Expiration  $= \text{Max}(X_H - S_T, 0) - \text{Max}(X_L - S_T, 0) - (p_H - p_L)$

Maximum gain  $= X_{H} - X_{L} - (p_{H} - p_{L})$

Maximum loss  $= p_{H} - p_{L}$

Breakeven price  $= X_{H} - p_{H} + p_{L}$

# Call Bear Spread

Expiration value  $= \text{Max}(S_T - X_H, 0) - \text{Max}(S_T - X_L, 0)$

Profit at Expiration  $= \text{Max}(S_T - X_H, 0) - \text{Max}(S_T - X_L, 0) - (c_H - c_L)$

Maximum gain  $= c_{L} - c_{H}$

Maximum loss  $= X_{H} - X_{L} + c_{H} - c_{L}$

Breachaven price  $= X_{L} + c_{L} - c_{H}$

# Straddle

Video: https://youtu.be/oDklmeMTnCg

Expiration value  $= \text{Max}(S_T - X, 0) + \text{Max}(X - S_T, 0)$

Profit at Expiration  $= \text{Max}(S_T - X, 0) + \text{Max}(X - S_T, 0) - c_0 - p_0$

Maximum gain =  $\begin{cases} \infty & S_T > X \\ X - S_T - c_0 - p_0 & S_T < X \end{cases}$

Maximum loss  $= c_{0} + p_{0}$

Breateiven price  $= X\pm (c_{0} + p_{0})$

# Collar

Video: https://youtu.be/LkS_sxmg2cs

Note:  $X_{L} <   S_{0} <   X_{H}$

Expiration value  $= S_{T} + \text{Max}(X_{L} - S_{T}, 0) - \text{Max}(S_{T} - X_{H}, 0)$

Profit at Expiration  $= S_{T} + \text{Max}(X_{L} - S_{T}, 0) - \text{Max}(S_{T} - X_{H}, 0) - S_{0} - p_{0} + c_{0}$

Maximum gain  $= X_{H} - S_{0} - p_{0} + c_{0}$

Maximum loss  $= -X_{L} + S_{0} + p_{0} - c_{0}$

Breachaven price  $= S_{0} + p_{0} - c_{0}$

For zero-cost collar,  $p_0 = c_0$

# Implied Volatility

For 252 trading days in a year and 21 trading days in a month:

$$
\sigma_ {a n n u a l} = \sigma_ {m o n t h l y} \sqrt {\frac {2 5 2}{2 1}}
$$

# Delta hedging

$$
N _ {p o s i t i o n} \times D e l t a _ {p o s i t i o n} + N _ {h e d g e} \times D e l t a _ {h e d g e} = 0
$$

Video: https://youtu.be/v8RcvkQKFpw

Learning Module 2: Swaps, Forwards, and Futures Strategies

# Managing Interest Rate Risk

# Interest Rate Swaps

$$
N _ {S} = \left(\frac {M D U R _ {T} - M D U R _ {P}}{M D U R _ {S}}\right) M V _ {P}
$$

$N_{S} =$  Swap notional principal

$MDUR_{T} =$  Target modified duration

$MDUR_{P} =$  Modified duration of portfolio

$MDUR_{S} =$  Modified duration of swap

$MV_{P} =$  Market value of portfolio

Note: Modified duration of cash = 0 (unless stated otherwise in case)

# Money Market Instrument

$$
B P V = \text {Face Value} \times \frac {\text {Days}}{360} \times 0.01 \%
$$

# Interest Rate Futures

Eurodollar futures price  $= 100 -$  Annualized yield

# Treasury Futures

$$
\frac {\text {P r i n c i p a l i n v o i c e}}{\text {a m o u n t}} = \frac {\text {F u t u r e s s e t t l e m e n t p r i c e}}{1 0 0} \times \frac {\text {C o n v e r s i o n}}{\text {F a c t o r}} \times \text {C o n t r a c t s i z e}
$$

# Basis Point Value Hedge Ratio (BPVHR)

$$
B P V H R = \left(\frac {B P V _ {T} - B P V _ {P}}{B P V _ {C T D}}\right) \times C o n v e r s i o n F a c t o r
$$

$$
\begin{array}{l} B P V _ {T} = M D U R _ {T} \times 0.01 \% \times M V _ {P} \\ B P V _ {P} = M D U R _ {P} \times 0.01 \% \times M V _ {P} \\ B P V _ {C T D} = M D U R _ {C T D} \times 0.01 \% \times M V _ {C T D} \\ M V _ {C T D} = \frac {C T D p r i c e}{1 0 0} \times F u t u r e s c o n t r a c t s i z e \\ B P V _ {F} = \frac {B P V _ {C T D}}{C F} \\ \end{array}
$$

# Hedging Currency Risk with Futures

$$
N _ {f} = \frac {\text {R e q u i r e d c u r r e n c y h e d g e}}{\text {C o n t r a c t s i z e}}
$$

# Hedging Equity Risk with Futures

$$
N _ {f} = \left(\frac {\beta_ {T} - \beta_ {S}}{\beta_ {f}}\right) \left(\frac {S}{F}\right)
$$

where:

$$
\beta_ {T} = \text {T a r g e t b e t a}
$$

$$
\beta_ {S} = \text {P o r t f o l i o b e t a}
$$

$$
\beta_ {f} = \text {F u t u r e s b e t a}
$$

$$
S = \text {P o r t f l o i o m a r k e t v a l u e}
$$

$$
F = \text {F u t u r e s p r i c e}
$$

$$
\text {Effective beta} = \frac {\% \Delta \text {Portfolio value}}{\% \Delta \text {Index value}}
$$

Note: Beta of cash = 0

Video: https://youtu.be/VMVQ2GOrG0Q

# Variance Swap

$$
\begin{array}{l} S e t t l e m e n t a m o u n t _ {T} = V e g a n o t i o n a l \left(\frac {\sigma^ {2} - X ^ {2}}{2 X}\right) \\ = \text {V a r i a n c e n o t i o n a l} (\sigma^ {2} - X ^ {2}) \\ \end{array}
$$

$$
\frac {V a l u e o f l o n g v a r i a n c e}{s w a p a t t i m e t} = \frac {V a r i a n c e n o t i o n a l \times (\sigma_ {t} ^ {2} - X ^ {2})}{1 + r \times \left(\frac {T - t}{T}\right)}
$$

where:

$$
\sigma_ {t} ^ {2} = \frac {t}{T} \times \sigma_ {r e a l i z e d} ^ {2} (0, t) + \frac {T - t}{T} \times \sigma_ {i m p l i e d} ^ {2} (t, T)
$$

Video: https://youtu.be/YVNPCXGTdWk

# Probability of a Change in Federal Funds Rate

$$
\begin{array}{c} \text {P r o b a b i l i t y o f} \\ \text {a c h a n g e i n} \\ \text {f e d e r a l f u n d s r a t e} \end{array} = \frac {\text {I m p l i e d F e d f u n d s r a t e - C u r r e n t f e d f u n d s r a t e}}{\text {T a r g e t r a t e h i k e}}
$$

Current fed funds rate  $=$  Midpoint of current target range

Fed funds futures price  $= 100 -$  Implied Fed funds rate

Learning Module 3: Currency Management An Introduction

$$
R _ {D C} = \left(1 + R _ {F C}\right) \left(1 + R _ {F X}\right) - 1
$$

$$
R _ {D C} = \text {D o m e s t i c - c u r r e n c y}
$$

$$
R _ {F C} = \text {F o r g i n - c u r r e n c y}
$$

$$
R _ {F X} = \text {P e r t e n a g e} \quad \text {c h a n g e i n f o r g i n c} \quad \text {c u r r e n c y a g a i n s t d o m e s t i c c u r r e n c y} \quad (\text {c u r r e n c y q u o t a d s D C / F C})
$$

Video (Unhedged Returns): https://youtu.be/7Cycb5teSbU

Volatility of foreign asset (in domestic currency terms)

$$
\sigma_ {D C} ^ {2} = \sigma_ {F C} ^ {2} + \sigma_ {F X} ^ {2} + 2 \sigma_ {F C} \sigma_ {F X} \rho_ {F C, F X}
$$

For a foreign-risk free asset:

$$
\sigma_ {D C} = \sigma_ {F X} \left(1 + R _ {F C}\right)
$$

# Minimum Variance Hedge Ratio

$$
y _ {t} = \alpha + \beta x _ {t} + \varepsilon_ {t}
$$

where:

$y _ {t} = \text {c h a n g e i n v a l u e o f a s s e t t o b e h e d g e d (m e a s u r e d i n D C)} = R _ {D C}$

$$
x _ {t} = \text {c h a n g e i n v a l u e o f h e d g i n g i n s t r u m e n t (m e a s u r e d i n D C)} = R _ {F X}
$$

$$
M V H R, \beta = \frac {C o v (x , y)}{V a r (x)} = \rho_ {x, y} \left(\frac {\sigma_ {y}}{\sigma_ {x}}\right)
$$

Learning Module 1: Index-Based Equity Strategies

# Attribution Analysis

$$
\begin{array}{c} \text {C o n t r i b u t i o n o f s e c t o r i} \\ \text {t o p o r t f o l i o r e t u r n} \end{array} = \begin{array}{c} \text {W e i g h t o f s e c t o r i} \\ \text {i n p o r t f o l i o} \end{array} \times \begin{array}{c} \text {R e t u r n o f} \\ \text {s e c t o r i} \end{array}
$$

$$
\begin{array}{c} \text {C o n t r i b u t i o n o f s e c t o r i} \\ \text {t o b e n c h m a r k r e t u r n} \end{array} = \begin{array}{c} \text {W e i g h t o f s e c t o r i} \\ \text {i n b e n c h m a r k} \end{array} \times \begin{array}{c} \text {R e t u r n o f} \\ \text {s e c t o r i} \end{array}
$$

Learning Module 2: Active Equity Investing: Strategies

Growth at a Reasonable Price (GARP)

$$
P E G r a t i o = \frac {P / E}{g (i n \%)}
$$

# Information Coefficient

Pearson IC = Correlation between factor score and subsequent month return

Spearman rank IC = Correlation between rank of factor score and rank of subsequent month return

Returns-based Style Analysis

$$
r _ {t} = \alpha + \sum_ {s = 1} ^ {m} \beta^ {s} R _ {t} ^ {s} + \varepsilon_ {t}
$$

where:

$$
r _ {t} = \text {f u n d r e t u r n w i t h i n p e r i o d e n d i n g a t t i m e} t
$$

$$
R _ {t} ^ {s} = \text {r e t u r n o f s t y l e i n d e x s i n s a m e p e r i o d}
$$

$$
\beta^ {s} = \text {f u n d e x p o s u r e t o s t y l e} s \left(\sum_ {s = 1} ^ {m} \beta^ {s} = 1; \beta^ {s} > 0 \text {f o r l o n g - o n l y}\right)
$$

$$
\alpha = \text {m a n a g e r} ^ {\prime} \text {s v a l u e a d d e d}
$$

$$
\varepsilon_ {t} = \text {r e s i d u a l r e t u r n t h a t c a n n o t b e e x p l a i n e d b y t h e s t y l e s u s e d}
$$

# Active Return

$$
R _ {A} = \sum_ {i = 1} ^ {N} \Delta W _ {i} R _ {i}
$$

where:  $R_{i} =$  return on security  $i$

$$
\Delta W _ {i} = \text {a c t i v e w e i g h t} = W _ {p i} - W _ {B i}
$$

$$
R _ {A} = \sum_ {i = 1} ^ {N} \left(\beta_ {p k} - \beta_ {b k}\right) \times F _ {k} + (\alpha + \varepsilon)
$$

where:

$\beta_{pk} =$  sensitivity of portfolio  $(p)$  to rewarded factor  $(k)$

$\beta_{bk} =$  sensitivity of benchmark  $(b)$  to rewarded factor  $(k)$

$F_{k} =$  return of each rewarded factor

$\alpha =$  active return that can be attributed to manger's specific skill/strategies (security selection, factor timing)

$\varepsilon =$  idiosyncratic return

Portfolio turnover ratio =  $\frac{\text{Min}(\text{Purchases}, \text{Sales})}{\text{Average monthly net assets}}$

# Fundamental Law of Active Management

$$
E (R _ {A}) = I C \times \sqrt {B R} \times \sigma_ {R _ {A}} \times T C
$$

where:

$IC =$  Information coefficient

$BR =$  Breadth (Number of independent decisions made per year)

$TC =$  Transfer coefficient (Unconstrained portfolio  $\rightarrow$  TC  $= 1$

$\sigma_{R_A} =$  Manager's active risk

$$
A c t i v e S h a r e = \frac {1}{2} \sum_ {i = 1} ^ {n} \left| w _ {p, i} - w _ {B, i} \right|
$$

where:  $n =$  number of securities in either portfolio or benchmark

$$
A c t i v e R i s k o r T r a c k i n g E r r o r, \sigma_ {R _ {A}} = \sqrt {\frac {\sum_ {t = 1} ^ {T} (R _ {A t}) ^ {2}}{T - 1}}
$$

$$
\sigma_ {R _ {A}} ^ {2} = \sigma^ {2} \left(\sum_ {i = 1} ^ {N} \left(\beta_ {p k} - \beta_ {b k}\right) \times F _ {k}\right) + \sigma_ {\varepsilon} ^ {2}
$$

$$
\begin{array}{l} \sigma^ {2} \left(\sum_ {i = 1} ^ {N} \left(\beta_ {p k} - \beta_ {b k}\right) \times F _ {k}\right) = V a r i a n c e \text {a t t r i b u t e d t o f a c t o r e x p o s u r e} \\ \sigma_ {\varepsilon} ^ {2} = \text {V a r i a n c e a t t r i b u t e d t o i d i o s y n c r a t i c r i s k} \\ \end{array}
$$

# Absolute Risk Attribution

Video: https://youtu.be/zpk24jsMGDM

$$
V _ {p} = \sum_ {i = 1} ^ {n} \sum_ {j = 1} ^ {n} x _ {i} x _ {j} C _ {i j}
$$

$$
C V _ {i} = \sum_ {j = 1} ^ {n} x _ {i} x _ {j} C _ {i j} = x _ {i} C _ {i p}
$$

where:

$V_{p} =$  Portfolio variance

$CV_{i} =$  Contribution of asset  $i$  to portfolio variance

$x_{i} =$  weight of asset  $i$  in portfolio

$C_{ij} =$  Covariance of returns between asset  $i$  and  $j$

$C_{ip} =$  Covariance of returns between asset  $i$  and portfolio

# Relative Risk Attribution

$$
A V _ {p} = \sum_ {i = 1} ^ {n} \sum_ {j = 1} ^ {n} (x _ {i} - b _ {i}) (x _ {j} - b _ {j}) R C _ {i j}
$$

$$
C A V _ {i} = \sum_ {j = 1} ^ {n} (x _ {i} - b _ {i}) (x _ {j} - b _ {j}) C _ {i j} = (x _ {i} - b _ {i}) R C _ {i p}
$$

where:

$AV_{p} =$  Variance of portfolio's active return

$CAV_{i} =$  Contribution of asset  $i$  to portfolio active variance

$b_{i} =$  benchmark weight in asset  $i$

$RC_{ij} =$  Covariance of relative returns between asset  $i$  and  $j$

$C_{ip} =$  Covariance of returns between asset  $i$  and portfolio

# Compounded Return (Geometric Return)

$$
R _ {g} = k \times R _ {a} - (k - 1) R _ {d} - \frac {1}{2} (k \times \sigma) ^ {2}
$$

$R_{g} =$  Compounded/geometric return

$R_{a} =$  Arithmetic/periodic return

$k =$  Leverage factor  $=$  Asset/Equity

$R_{d} =$  Cost of funding leverage

# Gross and Net Exposure

Gross Exposure = Long positions + |Short positions|

Net Exposure = Long positions - |Short positions|

Learning Module 4: Liability-Driven and Index-Based Strategies

# Macaulay Duration, Dispersion, and Convexity

Macaulay Duration  $= \sum_{i=1}^{N} w_i \times t$

$$
w _ {i} = \frac {P V _ {i}}{P V}
$$

Note: To annualize MacDur, divide by periodicity.

$$
D i s p e r s i o n = \sum_ {t = 1} ^ {N} w _ {i} \times (t - M a c D u r) ^ {2}
$$

$$
C o n v e x i t y = \frac {1}{(1 + C a s h f l o w y i e l d) ^ {2}} \sum_ {t = 1} ^ {N} w _ {i} \times t (t + 1)
$$

Note: To annualize dispersion and convexity, divide by periodicity squared.

$$
C o n v e x i t y = \frac {M a c D u r ^ {2} + M a c D u r + D i s p e r s i o n}{(1 + C a s h f l o w y i e l d) ^ {2}}
$$

Video: https://youtu.be/qeky-p7Hljw

$$
M o d i f i e d D u r a t i o n = \frac {M a c a u l a y D u r a t i o n}{1 + C a s h f l o w y i e l d}
$$

Money Duration = Market value × Modified Duration

$$
B P V = M a r k e t v a l u e \times M o d i f i e d D u r a t i o n \times 0. 0 0 0 1
$$

Note: For zero-coupon bonds, Macaulay duration = Maturity

Number of bond futures contracts required to close the duration gap

$$
N _ {f} = \frac {\text {L i a b i l i t y B P V - A s s e t B P V}}{\text {F u t u r e s B P V}}
$$

where:

$$
F u t u r e s B P V \approx \frac {B P V _ {C T D}}{C F _ {C T D}}
$$

Duration gap  $=$  Asset BPV - Liability BPV

Video (Derivatives overlay with futures): https://youtu.be/3ZlCA1nP8Zc

Video (Contingent immunization): https://youtu.be/bL9P0j5LNJk

Required Swap Notional to close the duration gap

$$
N P = \frac {\text {L i a b i l i t y B P V - A s s e t B P V}}{\text {S w a p B P V / 1 0 0}}
$$

Note: Swap BPV quoted per $100 notional

Video: https://youtu.be/LGsJEXCYH0g

$$
\begin{array}{c} \text {A s s e t} \\ B P V \end{array} \times \begin{array}{c} \Delta A s s e t \\ y i e l d s \end{array} + \begin{array}{c} \text {H e d g e} \\ B P V \end{array} \times \begin{array}{c} \Delta H e d g e \\ y i e l d s \end{array} = \begin{array}{c} \text {L i a b i l i t y} \\ B P V \end{array} \times \begin{array}{c} \Delta L i a b i l i t y \\ y i e l d s \end{array}
$$

Learning Module 5: Yield Curve Strategies

$$
\begin{array}{c} \text {Y i e l d c u r v e} \\ \text {s l o p e} \end{array} = \begin{array}{c} \text {L o n g t e r m} \\ \text {y i e l d} \end{array} - \begin{array}{c} \text {S h o r t t e r m} \\ \text {y i e l d} \end{array}
$$

$$
\begin{array}{c} B u t t e r f l y \\ s p r e a d \end{array} = - \frac {S h o r t t e r m}{y i e l d} + 2 \times \frac {M e d i u m t e r m}{y i e l d} - \frac {L o n g t e r m}{y i e l d}
$$

$$
\begin{array}{l} \% \Delta \mathrm {PV} ^ {F u l l} = - (M o d D u r \times \Delta Y i e l d) + \frac {1}{2} \times C o n v e x i t y \times (\Delta Y i e l d) ^ {2} \\ = \% \Delta \mathrm {PV} ^ {F u l l} \times P V ^ {F u l l} \\ \end{array}
$$

# Repo carry trade

Repo carry return = Coupon income ± Rolldown Return - Financing cost

# Long futures position

Targeted Return = %ΔFutures Price - Margin cost

Video: https://youtu.be/EB9IOJwzmRA

# Receive-fixed interest rate swap

Targeted Return = (Swap rate - MRR) + %ΔSwap mark to market

# Key Rate Duration

$$
K e y R a t e D u r _ {k} = \frac {1}{P V} \times \frac {\Delta P V}{\Delta r _ {k}}
$$

Learning Module 6: Fixed Income Active Management: Credit Strategies

Credit Spread  $= POD \times LGD$

Yield  $= \frac{YTM of}{credit security} - \frac{YTM of}{benchmark bond}$

$$
G - S p r e a d = \frac {Y T M o f}{c r e d i t s e c u r i t y} - \frac {Y T M o f i n t e r p o l a t e d}{g o v e r n m e n t b o n d}
$$

$$
I - S p r e a d = \frac {Y T M o f}{c r e d i t s e c u r i t y} - \frac {S w a p}{r a t e}
$$

Asset swap spread,  $ASW =$  Bond coupon rate - Swap rate

# Discount margin (DM) for floating-rate notes

$$
P V = \frac {\left[ \frac {(M R R + Q M) \times F V}{m} \right]}{\left(1 + \frac {M R R + D M}{m}\right) ^ {1}} + \frac {\left[ \frac {(M R R + Q M) \times F V}{m} \right]}{\left(1 + \frac {M R R + D M}{m}\right) ^ {2}} + \dots + \frac {\left[ \frac {(M R R + Q M) \times F V}{m} \right] + F V}{\left(1 + \frac {M R R + D M}{m}\right) ^ {n}}
$$

$QM =$  Quoted margin

DM = Discount margin

$m =$  Periodicity

$n =$  Tenor of FRN

$MRR =$  Market reference rate (assume constant)

$FV =$  Face value

$$
P o r t f o l i o O A S = \sum_ {i = 1} ^ {N} \frac {M V _ {i}}{M V} \times O A S _ {i} \quad M V = M a r k e t v a l u e o f p o r t f o l i o
$$

Duration Times Squared,  $DTS =$  Spread duration  $\times$  Spread

$$
P o r t f o l i o D T S = \sum_ {i = 1} ^ {N} \frac {M V _ {i}}{M V} \times (S p r e a d D u r a t i o n _ {i} \times S p r e a d _ {i})
$$

Estimated change in portfolio (in bps) = -Portfolio DTS × %DeltaSpread

# Impact of Yield Spreads on Portfolio Return

$$
\% \Delta P V ^ {S p r e a d} \approx - E f f S p r e a d D u r \times \Delta S p r e a d + \frac {1}{2} \times E f f S p r e a d C o n \times (\Delta S p r e a d) ^ {2}
$$

$$
E f f S p r e a d D u r = \frac {(P V _ {-}) - (P V _ {+})}{2 \times (\Delta S p r e a d) \times P V _ {0}}
$$

$$
E f f S p r e a d C o n = \frac {(P V _ {-}) + (P V _ {+}) - 2 (P V _ {0})}{(\Delta S p r e a d) ^ {2} \times P V _ {0}}
$$

# Excess return on credit risky bond

$$
E (E x c e s s S p r e a d) \approx (S p r e a d _ {0} \times t) - (E f f S p r e a d D u r \times \Delta S p r e a d) - (t \times P O D \times L G D)
$$

where:

$Spread_{0} = Initial\ yield\ spread per annum$

$\Delta \text{Spread} =$  Change in spread over holding period

$POD =$  Annualized expected probability of default

$LGD =$  Expected loss severity

$POD \times LGD =$  expected annual credit loss

$t =$  Holding period (in years)

Video: https://youtu.be/U1C5 eNFMBA

# Floating-rate Note (FRN)

Effective rate duration

$$
E f f R a t e D u r _ {F R N} = \frac {(P V _ {-}) - (P V _ {+})}{2 \times (\Delta M R R) \times P V _ {0}}
$$

Effective spread duration

$$
E f f S p r e a d D u r _ {F R N} = \frac {(P V _ {-}) - (P V _ {+})}{2 \times (\Delta D M) \times P V _ {0}}
$$

Expected change in YTM based on a  $C\%$  confidence interval over one month

= Daily interest rate volatility  $\times \sqrt{\frac{Number\ of\ trading}{days\ in\ a\ month}}\times Z$  score

# Credit Default Swap (CDS)

For a $1 notional:

$$
C D S P r i c e \approx 1 + \left[ (F i x e d C o u p o n - C D S S p r e a d) \times E f f S p r e a d D u r _ {C D S} \right]
$$

$$
U p f r o n t p r e m i u m = (F i x e d c o u p o n - C D S s p r e a d) \times E f f S p r e a d D u r _ {C D S}
$$

$$
\% \Delta CDS Price \approx -\Delta (CDS \text {Spread}) \times Eff \text {Spread} Dur_{CDS}
$$

$$
\Delta CDS \text {Price} \approx CDS \text {Notional} \times \% \Delta CDS \text {Price}
$$

# Note:

- Buy protection  $\rightarrow$  CDS Notional  $< 0$  (Short risk position)  
- Sell protection  $\rightarrow$  CDS Notional  $>0$  (Long risk position)

# Implementation Shortfall

$$
I S = \text {P a p e r} - \text {A c t u a l}
$$

Paper return  $= (P_{n} - P_{d})S$

Actual return  $= \left( \sum s_{j} \right) P_{n} - \sum s_{j} p_{j} - \text{Fees}$

Total cost of paper portfolio  $= P_{d} \times S$

$$
I S = E x e c u t i o n \text {c o s t} + O p p o r t u n i t y \text {c o s t} + F e e s
$$

Execution cost =  $\sum s_{j}p_{j} - \left(\sum s_{j}\right)P_{d}$

Opportunity cost  $= \left( {S - \mathop{\sum }\limits_{{j = 1}}^{n}{s}_{j}}\right) \left( {{P}_{n} - {P}_{d}}\right)$

Expanded IS = Delay cost + Trading cost + Opportunity cost + Fees

Delay cost =  $\left(\sum s_{j}\right)P_{0} - \left(\sum s_{j}\right)P_{d}$

\[
\text{Trading cost} = \sum s_{j} p_{j} - \left( \sum s_{j} \right) P_{0}
\]

where:

$P_{n} =$  Current price

$P_{d} =$  Decision price (Benchmark price)

$P_0 =$  Arrival price

$S =$  Total order of shares  $(S > 0$  for buy order;  $S <   0$  for sell order)

$s_j =$  Number of shares executed in  $j$ th trade

$p_j = \text{Transaction price of } j \text{th trade}$

$\sum s_{j} =$  Total number of shares executed

Video (Buy order): https://youtu.be/xScTmNlyIRQ

Video (Sell order): https://youtu.be/ssHM84hU3iw

# Trade Evaluation

$$
S i d e = \left\{ \begin{array}{l l} + 1 & B u y o r d e r \\ - 1 & S e l l o r d e r \end{array} \right. \qquad \bar {P} = A v e r a g e e x e c u t i o n p r i c e
$$

$$
\text {A r r i v a l c o s t (b p s)} = \text {S i d e} \times \frac {\bar {P} - \text {A r r i v a l p r i c e}}{\text {A r r i v a l p r i c e}} \times 1 0, 0 0 0
$$

$$
V W A P c o s t (b p s) = S i d e \times \frac {\bar {P} - V W A P}{V W A P} \times 1 0, 0 0 0
$$

$$
T W A P c o s t (b p s) = S i d e \times \frac {\bar {P} - T W A P}{T W A P} \times 1 0, 0 0 0
$$

$$
C l o s e (b p s) = S i d e \times \frac {\bar {P} - C l o s e}{C l o s e} \times 1 0, 0 0 0
$$

Market adjusted cost (bps) = Arrival cost (bps) -  $\beta \times$  Index cost (bps)

where:

$$
I n d e x c o s t (b p s) = S i d e \times \frac {I n d e x V W A P - I n d e x A r r i v a l P r i c e}{I n d e x A r r i v a l P r i c e} \times 1 0, 0 0 0
$$

Added value (bps) = Arrival cost (bps) - Estimated pre trade cost (bps)

# Learning Module 8: Case Study in Portfolio Management: Institutional

Total levered cost = Unlevered cost + Additional cost of obtaining leverage

$$
\underset {\text {l e v e r a g e f o r E T F}} {\text {A d d i t i o n a l c o s t o f o b t a i n i n g}} = \left(1 - \frac {1}{\text {L e v e r a g e f a c t o r}}\right) \times \text {B o r r o w i n g c o s t}
$$

$$
\underset {\text {l e v e r a g e f o r F u t u r e s}} {\text {A d d i t i o n a l c o s t o f o b t a i n i n g}} = \left(1 - \frac {1}{L e v e r a g e f a c t o r}\right) \times \text {O p p o r t u n i t y c o s t}
$$

$$
\frac {A d d i t i o n a l c o s t o f o b t a i n i n g}{l e v e r a g e f o r S w a p s} = \left(1 - \frac {1}{L e v e r a g e f a c t o r}\right) \times O p p o r t u n i t y c o s t
$$
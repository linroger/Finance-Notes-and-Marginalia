
## **CFA Program Formula Sheet (2025) – Complete & Corrected**

### **CFA Level 1**

#### **VOLUME 1: QUANTITATIVE METHODS**

##### **Learning Module 1: Rates and Returns**

- **1. Determinants of Interest Rates**
  $$r = r_{rf} + IP + DRP + LP + MP$$

  | Variable | Definition |
  | --- | --- |
  | $r$ | Total interest rate |
  | $r_{rf}$ | Real risk-free rate (return on riskless asset with no inflation) |
  | $IP$ | Inflation premium (compensation for expected inflation) |
  | $DRP$ | Default risk premium (compensation for default risk) |
  | $LP$ | Liquidity premium (compensation for illiquidity) |
  | $MP$ | Maturity premium (compensation for longer maturity risk) |
  | *Significance*: Breaks down interest rates into risk/inflation components to explain why different assets have different yields. |  |

- **2. Nominal vs. Real Risk-Free Rate**
  $$(1 + r_{nom}) = (1 + r_{rf}) \times (1 + IP)$$
  Simplified: $$r_{nom} \approx r_{rf} + IP$$

  | Variable | Definition |
  | --- | --- |
  | $r_{nom}$ | Nominal risk-free rate (e.g., T-bill yield) |
  | *Significance*: Links real returns to nominal returns by accounting for inflation—critical for adjusting returns for purchasing power. |  |

- **3. Holding Period Return (HPR)**
  $$R = \frac{P_1 - P_0 + I_1}{P_0}$$

  | Variable | Definition |
  | --- | --- |
  | $P_0$ | Asset price at period start |
  | $P_1$ | Asset price at period end |
  | $I_1$ | Income (dividends/coupons) during the period |
  | *Significance*: Measures total return from an asset over a single holding period (time-agnostic). |  |

- **4. Multi-Period HPR**
  $$R_{total} = \prod_{t=1}^{T} (1 + R_t) - 1$$

  | Variable | Definition |
  | --- | --- |
  | $R_t$ | HPR in period $t$ |
  | $T$ | Number of periods |
  | *Significance*: Compounds single-period returns to calculate total return over multiple periods (accounts for compounding). |  |

- **5. Arithmetic Mean Return**
  $$\overline{R}*A = \frac{1}{T} \sum*{t=1}^{T} R_t$$
  *Significance*: Simple average of returns—used for estimating expected return when periods are independent (but ignores compounding).

- **6. Geometric Mean Return**
  $$\overline{R}*G = \left( \prod*{t=1}^{T} (1 + R_t) \right)^{1/T} - 1$$
  *Significance*: Accounts for compounding—better for measuring **actual historical performance** over multiple periods.

- **7. Harmonic Mean Return**
  $$\overline{X}*H = \frac{T}{\sum*{t=1}^{T} \frac{1}{X_t}} \quad (X_t &gt; 0)$$
  *Significance*: Used for average price per unit (e.g., average cost of shares bought at different prices)—least common in CFA Level 1.

- **8. Relationship Between Means**
  $$(\overline{R}_G)^2 \approx \overline{R}_A \times \overline{X}_H$$
  *Significance*: For positive returns, arithmetic mean &gt; geometric mean &gt; harmonic mean (arithmetic overestimates compound returns).

- **9. Money-Weighted Return (MWR)**
  $$\sum_{t=0}^{T} \frac{CF_t}{(1 + MWR)^t} = 0$$

  | Variable | Definition |
  | --- | --- |
  | $CF_t$ | Cash flow at time $t$ (outflows = negative, inflows = positive) |
  | *Significance*: Equals IRR of the investment—reflects the actual return for the investor (sensitive to cash flow timing). |  |

- **10. Time-Weighted Return (TWR)**

  - $T &gt; 1$ year: $$\text{Annualized TWR} = \left( \prod_{t=1}^{T} (1 + R_t) \right)^{1/T} - 1$$
  - $T = 1$ year: $$\text{TWR} = \prod_{t=1}^{T} (1 + R_t) - 1$$
    *Significance*: Eliminates cash flow timing bias—used to evaluate **manager performance** (focuses on investment skill, not investor behavior).

- **11. Non-Annual Compounding (PV)**
  $$PV = FV_N \times \left(1 + \frac{R_s}{m}\right)^{-mN}$$

  | Variable | Definition |
  | --- | --- |
  | $R_s$ | Quoted annual interest rate |
  | $m$ | Number of compounding periods per year |
  | $N$ | Number of years |
  | *Significance*: Adjusts for compounding frequency (e.g., monthly, quarterly) to calculate present value of future cash flows. |  |

- **12. Annualizing Returns**

  - Weekly → Annual: $$R_{annual} = (1 + R_{weekly})^{52} - 1$$
  - Monthly → Annual: $$R_{annual} = (1 + R_{monthly})^{12} - 1$$
  - Daily → Annual: $$R_{annual} = (1 + R_{daily})^{252} - 1$$ (252 trading days/year)
    *Significance*: Standardizes returns to an annual basis for comparison across assets with different holding periods.

- **13. Continuously Compounded Return**
  $$P_T = P_0 \times e^{r_{0,T}} \implies r_{0,T} = \ln\left( \frac{P_T}{P_0} \right)$$

  | Variable | Definition |
  | --- | --- |
  | $r_{0,T}$ | Continuously compounded return from time 0 to T |
  | $e$ | Euler’s number (\~2.718) |
  | $\ln$ | Natural logarithm |
  | *Significance*: Additive across periods ($r_{0,T} = r_{0,1} + r_{1,2} + ... + r_{T-1,T}$)—used in derivatives pricing. |  |

- **14. After-Tax Nominal Return**
  $$R_{after-tax, nom} = R_{pre-tax, nom} \times (1 - t)$$

  | Variable | Definition |
  | --- | --- |
  | $t$ | Marginal tax rate |
  | *Significance*: Adjusts returns for taxes—critical for individual investors to measure net returns. |  |

- **15. After-Tax Real Return**
  $$R_{after-tax, real} = \frac{1 + R_{pre-tax, nom} \times (1 - t)}{1 + IP} - 1$$
  *Significance*: Adjusts for both taxes and inflation—measures **purchasing power gain** after taxes.

- **16. Leveraged Portfolio Return**
  $$R_L = R_P + \frac{V_B}{V_E} \times (R_P - r_D)$$

  | Variable | Definition |
  | --- | --- |
  | $R_L$ | Leveraged portfolio return |
  | $R_P$ | Unleveraged portfolio return |
  | $V_B$ | Value of borrowed funds |
  | $V_E$ | Investor’s equity (own capital) |
  | $r_D$ | Cost of debt (borrowing rate) |
  | *Significance*: Shows how leverage amplifies returns (positive if $R_P &gt; r_D$, negative if $R_P &lt; r_D$). |  |

##### **Learning Module 2: Time Value of Money (TVM)**

- **1. Single Cash Flow (Discrete Compounding)**
  $$FV_t = PV \times (1 + r)^t \quad ; \quad PV = \frac{FV_t}{(1 + r)^t}$$

  | Variable | Definition |
  | --- | --- |
  | $FV_t$ | Future value at time $t$ |
  | $r$ | Discount rate per period |
  | $t$ | Number of periods |
  | *Significance*: Foundation of TVM—converts between present and future values of a single cash flow. |  |

- **2. Single Cash Flow (Continuous Compounding)**
  $$FV_t = PV \times e^{rt} \quad ; \quad PV = FV_t \times e^{-rt}$$
  *Significance*: Used for assets with continuous compounding (e.g., some derivatives, savings accounts).

- **3. Zero-Coupon Bond Price**
  $$PV_{\text{zero-coupon}} = \frac{FV}{(1 + r)^t}$$

  | Variable | Definition |
  | --- | --- |
  | $FV$ | Bond face value (par value) |
  | $r$ | Market discount rate per period |
  | $t$ | Time to maturity (periods) |
  | *Significance*: Values bonds with no periodic coupons—price equals present value of par value. |  |

- **4. Coupon Bond Price**
  $$PV_{\text{coupon}} = \sum_{t=1}^{N} \frac{PMT}{(1 + r)^t} + \frac{FV}{(1 + r)^N}$$

  | Variable | Definition |
  | --- | --- |
  | $PMT$ | Periodic coupon payment ($= \text{Coupon rate} \times FV / m$) |
  | $N$ | Total number of periods to maturity |
  | *Significance*: Values bonds with periodic coupon payments—sum of present values of coupons and par value. |  |

- **5. Perpetual Bond Price**
  $$PV_{\text{perpetual}} = \frac{PMT}{r}$$
  *Significance*: Values bonds with infinite coupon payments (e.g., consols)—price is coupon divided by discount rate (no par value repayment).

- **6. Annuity Payment (Level Payment)**
  $$A = \frac{r \times PV}{1 - (1 + r)^{-t}}$$

  | Variable | Definition |
  | --- | --- |
  | $A$ | Periodic annuity payment |
  | $t$ | Number of payment periods |
  | *Significance*: Calculates fixed periodic payments for loans (e.g., mortgages) or investments (e.g., annuities). |  |

- **7. Preferred Stock Price (Perpetual Fixed Dividend)**
  $$PV_{\text{preferred}} = \frac{D}{r}$$

  | Variable | Definition |
  | --- | --- |
  | $D$ | Fixed annual dividend |
  | $r$ | Required return on preferred stock |
  | *Significance*: Values preferred stock (hybrid security) with fixed, perpetual dividends. |  |

- **8. Common Stock Price (Constant Growth DDM)**
  $$PV_0 = \frac{D_1}{r - g} = \frac{D_0 \times (1 + g)}{r - g} \quad (r &gt; g)$$

  | Variable | Definition |
  | --- | --- |
  | $D_0$ | Most recent dividend |
  | $D_1$ | Next period’s dividend ($= D_0 \times (1 + g)$) |
  | $g$ | Constant dividend growth rate |
  | $r$ | Required return on equity |
  | *Significance*: Values stocks with perpetual, constant dividend growth (Gordon Growth Model)—requires $r &gt; g$ to avoid infinite price. |  |

- **9. Required Return on Equity (Constant Growth)**
  $$r = \frac{D_1}{PV_0} + g$$
  *Significance*: Breaks down equity return into dividend yield ($D_1/PV_0$) and capital gains yield ($g$).

- **10. Two-Stage DDM**
  $$PV_0 = \sum_{t=1}^{n} \frac{D_0 \times (1 + g_s)^t}{(1 + r)^t} + \frac{D_{n+1}}{(r - g_L) \times (1 + r)^n}$$

  | Variable | Definition |
  | --- | --- |
  | $g_s$ | Short-term (high) growth rate |
  | $g_L$ | Long-term (stable) growth rate |
  | $n$ | Length of short-term growth phase |
  | $D_{n+1}$ | Dividend at start of long-term phase ($= D_0 \times (1 + g_s)^n \times (1 + g_L)$) |
  | *Significance*: Values stocks with two growth phases (e.g., high-growth startups transitioning to stable growth). |  |

- **11. Forward Rate (1-Year Forward 1-Year From Now)**
  $$F_{1,1} = \frac{(1 + r_2)^2}{(1 + r_1)} - 1$$

  | Variable | Definition |
  | --- | --- |
  | $F_{1,1}$ | 1-year forward rate starting in 1 year |
  | $r_1$ | 1-year spot rate |
  | $r_2$ | 2-year spot rate |
  | *Significance*: Derives implied future interest rates from spot rates—used in fixed income and derivatives. |  |

##### **Learning Module 3: Statistical Measures of Asset Returns**

- **1. Sample Mean**
  $$\overline{X} = \frac{1}{n} \sum_{i=1}^{n} X_i$$

  | Variable | Definition |
  | --- | --- |
  | $X_i$ | $i$-th observation |
  | $n$ | Sample size |
  | *Significance*: Measures central tendency—average of sample data. |  |

- **2. Median Position**
  $$\text{Median Position} = \frac{n + 1}{2}$$
  *Significance*: Middle value of ordered data—robust to outliers (unlike mean).

- **3. Interquartile Range (IQR)**
  $$IQR = Q_3 - Q_1$$

  | Variable | Definition |
  | --- | --- |
  | $Q_1$ | 1st quartile (25th percentile) |
  | $Q_3$ | 3rd quartile (75th percentile) |
  | *Significance*: Measures dispersion of middle 50% of data—robust to outliers. |  |

- **4. Box-and-Whisker Fences**
  $$\text{Upper Fence} = Q_3 + 1.5 \times IQR$$
  $$\text{Lower Fence} = Q_1 - 1.5 \times IQR$$
  *Significance*: Identifies outliers (data beyond fences = potential outliers).

- **5. Mean Absolute Deviation (MAD)**
  $$MAD = \frac{1}{n} \sum_{i=1}^{n} |X_i - \overline{X}|$$
  *Significance*: Measures average absolute deviation from mean—easy to interpret but not used in portfolio theory.

- **6. Sample Variance**
  $$s^2 = \frac{1}{n - 1} \sum_{i=1}^{n} (X_i - \overline{X})^2$$
  *Significance*: Measures squared dispersion from mean—divides by $n-1$ to correct for sample bias (unbiased estimator).

- **7. Sample Standard Deviation**
  $$s = \sqrt{\frac{1}{n - 1} \sum_{i=1}^{n} (X_i - \overline{X})^2}$$
  *Significance*: Square root of variance—expressed in original units (e.g., % return)—used to measure total risk.

- **8. Target Semideviation**
  $$s_{\text{target}} = \sqrt{\frac{1}{n - 1} \sum_{X_i \leq B} (X_i - B)^2}$$

  | Variable | Definition |
  | --- | --- |
  | $B$ | Target return (e.g., minimum acceptable return) |
  | *Significance*: Measures downside risk (only returns below target)—relevant for risk-averse investors. |  |

- **9. Coefficient of Variation (CV)**
  $$CV = \frac{s}{\overline{X}}$$
  *Significance*: Risk per unit of return—used to compare risk-adjusted returns across assets with different means.

- **10. Sample Skewness**
  $$\text{Skewness} \approx \frac{1}{n} \times \frac{\sum_{i=1}^{n} (X_i - \overline{X})^3}{s^3}$$
  *Significance*: Measures asymmetry of distribution—positive (right-skewed: few high returns), negative (left-skewed: few low returns).

- **11. Sample Excess Kurtosis**
  $$K_E \approx \frac{1}{n} \times \frac{\sum_{i=1}^{n} (X_i - \overline{X})^4}{s^4} - 3$$
  *Significance*: Measures "tailedness" relative to normal distribution—positive (leptokurtic: fat tails, more extreme returns), negative (platykurtic: thin tails).

- **12. Sample Covariance**
  $$s_{XY} = \frac{1}{n - 1} \sum_{i=1}^{n} (X_i - \overline{X})(Y_i - \overline{Y})$$

  | Variable | Definition |
  | --- | --- |
  | $X, Y$ | Two assets/returns |
  | *Significance*: Measures linear relationship between two variables—positive (move together), negative (move opposite). |  |

- **13. Sample Correlation Coefficient**
  $$r_{XY} = \frac{s_{XY}}{s_X \times s_Y}$$
  *Significance*: Standardized covariance (-1 ≤ $r_{XY}$ ≤ 1)—measures strength of linear relationship (0 = no linear relationship).

##### **Learning Module 4: Probability Trees and Conditional Expectations**

- **1. Expected Value (Discrete Random Variable)**
  $$E(X) = \sum_{i=1}^{n} P(X_i) \times X_i$$

  | Variable | Definition |
  | --- | --- |
  | $P(X_i)$ | Probability of $X_i$ |
  | $X_i$ | $i$-th outcome of $X$ |
  | *Significance*: Weighted average of outcomes—expected future value of a random variable. |  |

- **2. Variance (Random Variable)**
  $$\sigma^2(X) = E\left[ (X - E(X))^2 \right] = \sum_{i=1}^{n} P(X_i) \times (X_i - E(X))^2$$
  *Significance*: Measures dispersion of outcomes around expected value—total risk of the variable.

- **3. Conditional Expected Value**
  $$E(X | S) = \sum_{i=1}^{n} P(X_i | S) \times X_i$$

  | Variable | Definition |
  | --- | --- |
  | $P(X_i | S)$ |
  | *Significance*: Expected value of $X$ when event $S$ occurs—incorporates new information. |  |

- **4. Total Probability Rule (Expectation)**
  $$E(X) = \sum_{i=1}^{n} E(X | S_i) \times P(S_i)$$

  | Variable | Definition |
  | --- | --- |
  | $S_1, ..., S_n$ | Mutually exclusive, exhaustive events |
  | *Significance*: Calculates expected value by partitioning the sample space into smaller events. |  |

- **5. Bayes’ Formula**
  $$P(A | B) = \frac{P(B | A) \times P(A)}{P(B)}$$
  *Significance*: Updates probabilities based on new information (e.g., updating default probability after a credit rating change).

##### **Learning Module 5: Portfolio Mathematics**

- **1. Expected Portfolio Return (n Assets)**
  $$E(R_P) = \sum_{i=1}^{n} w_i \times E(R_i)$$

  | Variable | Definition |
  | --- | --- |
  | $w_i$ | Weight of asset $i$ (sum to 1) |
  | $E(R_i)$ | Expected return of asset $i$ |
  | *Significance*: Weighted average of individual asset returns—linear in weights. |  |

- **2. Portfolio Variance (n Assets)**
  $$\sigma^2(R_P) = \sum_{i=1}^{n} \sum_{j=1}^{n} w_i w_j \times Cov(R_i, R_j)$$

  | Variable | Definition |
  | --- | --- |
  | $Cov(R_i, R_j)$ | Covariance between $R_i$ and $R_j$ |
  | *Significance*: Measures portfolio total risk—depends on individual variances and covariances (diversification comes from low covariances). |  |

- **3. Two-Asset Portfolio Variance**
  $$\sigma^2(R_P) = w_1^2 \sigma_1^2 + w_2^2 \sigma_2^2 + 2 w_1 w_2 \times \rho_{12} \sigma_1 \sigma_2$$

  | Variable | Definition |
  | --- | --- |
  | $\rho_{12}$ | Correlation between $R_1$ and $R_2$ |
  | *Significance*: Simplified variance for two assets—shows how correlation reduces risk (lower $\rho$ = lower variance). |  |

- **4. Safety-First Ratio (SFRatio)**
  $$SFRatio = \frac{E(R_P) - R_L}{\sigma_P}$$

  | Variable | Definition |
  | --- | --- |
  | $R_L$ | Investor’s threshold return (minimum acceptable) |
  | *Significance*: Measures excess return over threshold per unit of risk—higher = lower shortfall risk. |  |

- **5. Shortfall Risk**
  $$\text{Shortfall Risk} = P(E(R_P) &lt; R_L) = N(-SFRatio)$$

  | Variable | Definition |
  | --- | --- |
  | $N(\cdot)$ | CDF of standard normal distribution |
  | *Significance*: Probability of returns below threshold—critical for risk-averse investors (e.g., retirees). |  |

##### **Learning Module 6: Simulation Methods**

- **1. Lognormal Distribution (Mean)**
  $$\mu_L = e^{\mu + 0.5 \sigma^2}$$

- **2. Lognormal Distribution (Variance)**
  $$\sigma_L^2 = e^{2\mu + \sigma^2} \times (e^{\sigma^2} - 1)$$

  | Variable | Definition |
  | --- | --- |
  | $\mu$ | Mean of underlying normal distribution |
  | $\sigma^2$ | Variance of underlying normal distribution |
  | *Significance*: Models asset prices (cannot be negative)—log returns are normally distributed, so prices are lognormal. |  |

- **3. Continuously Compounded Returns (I.I.D.)**
  If $r_{t,t+1}$ are i.i.d. (independent, identically distributed):
  $$E(r_{0,T}) = \mu T$$
  $$\sigma^2(r_{0,T}) = \sigma^2 T$$
  $$\sigma(r_{0,T}) = \sigma \sqrt{T}$$
  *Significance*: Volatility scales with square root of time—critical for risk management (e.g., VaR calculation).

##### **Learning Module 7: Estimation and Inference**

- **1. Sharpe Ratio**
  $$SR = \frac{R_P - R_f}{\sigma_P}$$

  | Variable | Definition |
  | --- | --- |
  | $R_f$ | Risk-free rate |
  | *Significance*: Risk-adjusted return per unit of total risk—used to compare portfolios with different risk levels. |  |

- **2. Standard Error of Sample Mean**
  $$SE(\overline{X}) = \frac{\sigma}{\sqrt{n}} \quad (\text{if } \sigma \text{ known}) \quad ; \quad SE(\overline{X}) = \frac{s}{\sqrt{n}} \quad (\text{if } \sigma \text{ unknown})$$
  *Significance*: Measures precision of sample mean—smaller = more precise estimate.

- **3. Bootstrap Resampling (Standard Error)**
  $$s_{\overline{X}} = \sqrt{\frac{1}{B - 1} \sum_{b=1}^{B} (\hat{\theta}_b - \overline{\theta})^2}$$

  | Variable | Definition |
  | --- | --- |
  | $B$ | Number of resamples |
  | $\hat{\theta}_b$ | Mean of resample $b$ |
  | $\overline{\theta}$ | Mean of all resample means |
  | *Significance*: Estimates standard error without assuming a distribution—used for non-normal data. |  |

##### **Learning Module 8: Hypothesis Testing**

- **1. Key Definitions**

  - Confidence Level: $1 - \alpha$ (α = Type I error probability: reject true null)
  - Test Power: $1 - \beta$ (β = Type II error probability: fail to reject false null)

- **2. Test of Single Mean (t-Test)**
  $$t = \frac{\overline{X} - \mu_0}{s / \sqrt{n}} \quad ; \quad df = n - 1$$

  | Variable | Definition |
  | --- | --- |
  | $\mu_0$ | Hypothesized population mean |
  | $df$ | Degrees of freedom |
  | *Significance*: Tests if sample mean differs from hypothesized mean (used when population variance is unknown). |  |

- **3. Confidence Interval for Mean**
  $$\overline{X} \pm t_{\alpha/2, df} \times \frac{s}{\sqrt{n}}$$
  *Significance*: Range of values likely to contain the true population mean (e.g., 95% CI = 95% chance of containing $\mu$).

- **4. Test of Difference in Means (Pooled t-Test)**
  $$t = \frac{(\overline{X}_1 - \overline{X}_2) - (\mu_1 - \mu_2)}{s_p \sqrt{\frac{1}{n_1} + \frac{1}{n_2}}} \quad ; \quad df = n_1 + n_2 - 2$$
  $$s_p^2 = \frac{(n_1 - 1)s_1^2 + (n_2 - 1)s_2^2}{n_1 + n_2 - 2}$$

  | Variable | Definition |
  | --- | --- |
  | $s_p^2$ | Pooled variance (assumes equal variances) |
  | *Significance*: Tests if means of two independent samples differ (e.g., returns of two mutual funds). |  |

- **5. Test of Mean of Differences (Paired t-Test)**
  $$t = \frac{\overline{d} - \mu_{d0}}{s_{\overline{d}}} \quad ; \quad df = n - 1$$

  | Variable | Definition |
  | --- | --- |
  | $\overline{d}$ | Mean of paired differences |
  | $\mu_{d0}$ | Hypothesized mean difference |
  | *Significance*: Tests if mean difference between paired observations differs from zero (e.g., before/after returns). |  |

- **6. Test of Single Variance (Chi-Square Test)**
  $$\chi^2 = \frac{(n - 1)s^2}{\sigma_0^2} \quad ; \quad df = n - 1$$

  | Variable | Definition |
  | --- | --- |
  | $\sigma_0^2$ | Hypothesized population variance |
  | *Significance*: Tests if sample variance differs from hypothesized variance (e.g., testing if a fund’s risk has changed). |  |

- **7. Test of Difference in Variances (F-Test)**
  $$F = \frac{s_1^2}{s_2^2} \quad ; \quad df_1 = n_1 - 1, df_2 = n_2 - 1$$
  *Significance*: Tests if variances of two samples differ (e.g., comparing risk of two assets).

- **8. Test of Correlation (t-Test)**
  $$t = \frac{r \sqrt{n - 2}}{\sqrt{1 - r^2}} \quad ; \quad df = n - 2$$

  | Variable | Definition |
  | --- | --- |
  | $r$ | Sample correlation coefficient |
  | *Significance*: Tests if correlation between two variables is zero (no linear relationship). |  |

- **9. Test of Independence (Chi-Square Test)**
  $$\chi^2 = \sum_{i=1}^{m} \sum_{j=1}^{k} \frac{(O_{ij} - E_{ij})^2}{E_{ij}} \quad ; \quad df = (r - 1)(c - 1)$$

  | Variable | Definition |
  | --- | --- |
  | $O_{ij}$ | Observed frequency in cell (i,j) |
  | $E_{ij}$ | Expected frequency ($= \frac{\text{Row Total} \times \text{Column Total}}{\text{Grand Total}}$) |
  | $r$ | Number of rows |
  | $c$ | Number of columns |
  | *Significance*: Tests if two categorical variables are independent (e.g., credit rating and default status). |  |

##### **Learning Module 9: Parametric & Non-Parametric Tests of Independence**

- **1. Pearson Correlation**
  $$r_{XY} = \frac{s_{XY}}{s_X s_Y}$$
  *Significance*: Measures linear relationship between continuous variables (parametric—assumes normality).

- **2. Spearman Rank Correlation**
  $$r_S = 1 - \frac{6 \sum_{i=1}^{n} d_i^2}{n(n^2 - 1)}$$

  | Variable | Definition |
  | --- | --- |
  | $d_i$ | Difference in ranks of $X_i$ and $Y_i$ |
  | *Significance*: Measures monotonic relationship (non-parametric—no normality assumption; used for ordinal data). |  |

##### **Learning Module 10: Simple Linear Regression**

- **1. Regression Model**
  Population: $$Y_i = b_0 + b_1 X_i + \varepsilon_i$$
  Estimated: $$\hat{Y}_i = \hat{b}_0 + \hat{b}_1 X_i + e_i$$

  | Variable | Definition |
  | --- | --- |
  | $Y_i$ | Dependent variable |
  | $X_i$ | Independent variable |
  | $b_0$ | Population intercept |
  | $b_1$ | Population slope |
  | $\varepsilon_i$ | Population error term |
  | $\hat{b}_0$ | Estimated intercept |
  | $\hat{b}_1$ | Estimated slope |
  | $e_i$ | Residual ($= Y_i - \hat{Y}_i$) |
  | *Significance*: Models linear relationship between $X$ and $Y$—predicts $Y$ from $X$. |  |

- **2. Estimated Slope**
  $$\hat{b}*1 = \frac{\sum*{i=1}^{n} (X_i - \overline{X})(Y_i - \overline{Y})}{\sum_{i=1}^{n} (X_i - \overline{X})^2} = \frac{s_{XY}}{s_X^2}$$
  *Significance*: Measures change in $Y$ for a 1-unit change in $X$ (marginal effect).

- **3. Estimated Intercept**
  $$\hat{b}_0 = \overline{Y} - \hat{b}_1 \overline{X}$$
  *Significance*: Value of $Y$ when $X = 0$ (interpret with caution if $X=0$ is not meaningful).

- **4. Sum of Squares**

  - Total (SST): $$SST = \sum_{i=1}^{n} (Y_i - \overline{Y})^2 \quad (\text{total variation in } Y)$$
  - Regression (SSR): $$SSR = \sum_{i=1}^{n} (\hat{Y}_i - \overline{Y})^2 \quad (\text{variation explained by } X)$$
  - Error (SSE): $$SSE = \sum_{i=1}^{n} (Y_i - \hat{Y}_i)^2 \quad (\text{unexplained variation})$$
    Relationship: $$SST = SSR + SSE$$

- **5. Coefficient of Determination ($R^2$)**
  $$R^2 = \frac{SSR}{SST} = 1 - \frac{SSE}{SST}$$
  *Significance*: % of variation in $Y$ explained by $X$ (0 ≤ $R^2$ ≤ 1; higher = better fit).

- **6. ANOVA F-Test (Overall Significance)**
  $$F = \frac{MSR}{MSE} \quad ; \quad MSR = \frac{SSR}{k}, MSE = \frac{SSE}{n - k - 1}$$

  | Variable | Definition |
  | --- | --- |
  | $k$ | Number of independent variables (1 for simple regression) |
  | *Significance*: Tests if the regression model is significant (i.e., $b_1 \neq 0$). |  |

- **7. Hypothesis Test of Slope**
  $$t = \frac{\hat{b}*1 - B_1}{s*{\hat{b}*1}} \quad ; \quad df = n - k - 1$$
  $$s*{\hat{b}*1} = \frac{s_e}{\sqrt{\sum*{i=1}^{n} (X_i - \overline{X})^2}}$$

  | Variable | Definition |
  | --- | --- |
  | $B_1$ | Hypothesized slope (usually 0) |
  | $s_e$ | Standard error of estimate ($\sqrt{MSE}$) |
  | *Significance*: Tests if slope is different from hypothesized value (e.g., $B_1 = 0$ = no linear effect). |  |

- **8. Prediction Interval**
  $$\hat{Y}*f \pm t*{\alpha/2, df} \times s_f$$
  $$s_f = s_e \sqrt{1 + \frac{1}{n} + \frac{(X_f - \overline{X})^2}{\sum_{i=1}^{n} (X_i - \overline{X})^2}}$$

  | Variable | Definition |
  | --- | --- |
  | $X_f$ | Forecasted $X$ value |
  | *Significance*: Range of values likely to contain the true $Y_f$ (wider than confidence interval for mean $Y_f$). |  |

##### **Learning Module 11: Introduction to Big Data Techniques**

- No formulas—focuses on concepts (e.g., structured vs. unstructured data, machine learning basics).

#### **VOLUME 2: ECONOMICS**

##### **Learning Module 1: The Firm and Market Structures**

- **1. Profit Definitions**

  - Economic Profit: $$\pi_{\text{economic}} = TR - TC_{\text{economic}} \quad (TC_{\text{economic}} = \text{Explicit} + \text{Implicit Costs})$$
  - Accounting Profit: $$\pi_{\text{accounting}} = TR - TC_{\text{accounting}} \quad (TC_{\text{accounting}} = \text{Explicit Costs Only})$$

- **2. Total Revenue (TR)**
  $$TR = P \times Q$$

  - Average Revenue (AR): $$AR = \frac{TR}{Q} = P$$
  - Marginal Revenue (MR): $$MR = \frac{\Delta TR}{\Delta Q}$$

- **3. Cost Measures**

  - Total Cost (TC): $$TC = TFC + TVC$$
  - Marginal Cost (MC): $$MC = \frac{\Delta TC}{\Delta Q}$$
  - Average Total Cost (ATC): $$ATC = \frac{TC}{Q} = AFC + AVC$$
  - Average Fixed Cost (AFC): $$AFC = \frac{TFC}{Q}$$
  - Average Variable Cost (AVC): $$AVC = \frac{TVC}{Q}$$
    | Variable | Definition |
    |----------|------------|
    | $TFC$ | Total Fixed Costs (constant with Q) |
    | $TVC$ | Total Variable Costs (varies with Q) |
    *Significance*: Helps firms determine profit-maximizing output (where $MR = MC$).

- **4. Market Concentration**

  - Concentration Ratio: $$CR_n = \sum_{i=1}^{n} \text{Market Share}_i$$
  - Herfindahl-Hirschman Index (HHI): $$HHI = \sum_{i=1}^{n} (\text{Market Share}_i)^2$$
    *Significance*: Measures market power—higher CR/HHI = more concentrated market (e.g., monopoly has HHI = 10,000).

##### **Learning Module 2: Understanding Business Cycles**

- No formulas—focuses on concepts (e.g., business cycle phases, leading/coincident/lagging indicators).

##### **Learning Module 3: Fiscal Policy**

- **1. Budget Surplus/Deficit**
  $$\text{Budget Balance} = G - T + B$$

  | Variable | Definition |
  | --- | --- |
  | $G$ | Government spending |
  | $T$ | Taxes |
  | $B$ | Transfer payments |
  | *Significance*: Measures government’s fiscal position (positive = surplus, negative = deficit). |  |

- **2. Disposable Income (YD)**
  $$YD = Y - NT = Y(1 - t)$$

  | Variable | Definition |
  | --- | --- |
  | $Y$ | GDP/Income |
  | $NT$ | Net Taxes ($= T - B$) |
  | $t$ | Net tax rate |

- **3. Fiscal Multiplier**
  $$\text{Fiscal Multiplier} = \frac{1}{1 - c(1 - t)}$$

  | Variable | Definition |
  | --- | --- |
  | $c$ | Marginal Propensity to Consume (MPC) |
  | *Significance*: Measures how much GDP changes for a $1 change in government spending/taxes (higher c = higher multiplier). |  |

##### **Learning Module 4: Monetary Policy**

- **1. Neutral Rate**
  $$r_{\text{neutral}} = \text{Trend GDP Growth} + \text{Inflation Target}$$
  *Significance*: Interest rate where monetary policy is neither expansionary nor contractionary (used by central banks like the Fed).

##### **Learning Modules 5-6: Geopolitics & International Trade**

- No formulas—concepts (e.g., trade barriers, comparative advantage).

##### **Learning Module 7: Capital Flows and the FX Market**

- **1. Real Exchange Rate**
  $$q_{d/f} = S_{d/f} \times \frac{P_f}{P_d}$$

  | Variable | Definition |
  | --- | --- |
  | $q_{d/f}$ | Real exchange rate (d = domestic, f = foreign) |
  | $S_{d/f}$ | Nominal spot rate (d per f) |
  | $P_f$ | Foreign price level |
  | $P_d$ | Domestic price level |
  | *Significance*: Measures purchasing power of currency—higher $q$ = domestic goods more expensive relative to foreign. |  |

- **2. % Change in Real Exchange Rate**
  $$% \Delta q_{d/f} \approx % \Delta S_{d/f} + % \Delta P_f - % \Delta P_d$$
  *Significance*: Decomposes real exchange rate changes into nominal rate and inflation differences.

##### **Learning Module 8: Exchange Rate Calculations**

- **1. Cross Rate**
  $$\frac{A}{B} = \frac{A}{C} \times \frac{C}{B}$$
  *Significance*: Calculates exchange rate between two currencies using a third (e.g., EUR/GBP using EUR/USD and USD/GBP).

- **2. Forward Rate**
  $$F_{A/B} = S_{A/B} \times \frac{1 + r_A \times T}{1 + r_B \times T}$$

  | Variable | Definition |
  | --- | --- |
  | $F_{A/B}$ | Forward rate (A per B) |
  | $r_A$ | Interest rate in currency A |
  | $r_B$ | Interest rate in currency B |
  | $T$ | Time to maturity (years) |
  | *Significance*: Derives forward rate from spot rate and interest rates (covered interest parity). |  |

- **3. Forward Points**
  $$\text{Forward Points} = F_{A/B} - S_{A/B} = S_{A/B} \times \frac{r_A - r_B}{1 + r_B} \times T$$
  *Significance*: Expresses forward rate difference from spot rate in basis points (used in FX markets).

#### **VOLUME 3: CORPORATE ISSUERS**

##### **Learning Module 1-2: Organizational Forms & Stakeholders**

- No formulas—concepts (e.g., sole proprietorship vs. corporation, stakeholder theory).

##### **Learning Module 3: Working Capital and Liquidity**

- **1. Cash Conversion Cycle (CCC)**
  $$CCC = DOH + DSO - DPO$$

  | Variable | Definition |
  | --- | --- |
  | $DOH$ | Days of Inventory on Hand |
  | $DSO$ | Days Sales Outstanding |
  | $DPO$ | Days Payables Outstanding |
  | *Significance*: Measures time to convert inventory to cash—shorter = better liquidity. |  |

- **2. Financing Cost (Trade Credit)**
  $$\text{Financing Cost} = \left(1 + \frac{\text{Discount}%}{100% - \text{Discount}%}\right)^{\frac{365}{\text{Payment Period} - \text{Discount Period}}} - 1$$
  *Significance*: Cost of forgoing trade discount (e.g., 2/10 net 30 = cost of paying on day 30 instead of day 10).

- **3. Working Capital Definitions**

  - Total Working Capital: $$\text{Total WC} = \text{Current Assets} - \text{Current Liabilities}$$
  - Net Working Capital: $$\text{Net WC} = (\text{Current Assets} - \text{Cash} - \text{Marketable Securities}) - (\text{Current Liabilities} - \text{Short-Term Debt})$$

- **4. Liquidity Ratios**

  - Current Ratio: $$\text{Current Ratio} = \frac{\text{Current Assets}}{\text{Current Liabilities}}$$
  - Quick Ratio: $$\text{Quick Ratio} = \frac{\text{Cash} + \text{Marketable Securities} + \text{Receivables}}{\text{Current Liabilities}}$$
  - Cash Ratio: $$\text{Cash Ratio} = \frac{\text{Cash} + \text{Marketable Securities}}{\text{Current Liabilities}}$$
    *Significance*: Measure short-term solvency—higher = better ability to meet current obligations.

##### **Learning Module 4: Corporate Governance**

- No formulas—concepts (e.g., agency conflicts, board of directors).

##### **Learning Module 5: Capital Investments and Capital Allocation**

- **1. Net Present Value (NPV)**
  $$NPV = \sum_{t=0}^{T} \frac{CF_t}{(1 + r)^t}$$

  | Variable | Definition |
  | --- | --- |
  | $CF_t$ | After-tax cash flow at time $t$ ($CF_0$ = initial outlay) |
  | $r$ | Required return (cost of capital) |
  | *Significance*: Measures value added by investment—NPV &gt; 0 = accept (increases firm value). |  |

- **2. Internal Rate of Return (IRR)**
  $$\sum_{t=0}^{T} \frac{CF_t}{(1 + IRR)^t} = 0$$
  *Significance*: Discount rate where NPV = 0—accept if IRR &gt; required return (but has flaws for non-conventional cash flows).

- **3. Return on Invested Capital (ROIC)**
  $$ROIC = \frac{\text{After-Tax Operating Profit}}{\text{Average Invested Capital}} = \frac{\text{After-Tax Operating Profit}}{\text{Sales}} \times \frac{\text{Sales}}{\text{Average Invested Capital}}$$
  *Significance*: Measures efficiency of capital use—higher = better capital allocation.

##### **Learning Module 6: Capital Structure**

- **1. Weighted Average Cost of Capital (WACC)**
  $$WACC = w_d r_d (1 - t) + w_e r_e$$

  | Variable | Definition |
  | --- | --- |
  | $w_d$ | Weight of debt ($= \frac{D}{D + E}$) |
  | $w_e$ | Weight of equity ($= \frac{E}{D + E}$) |
  | $r_d$ | Pre-tax cost of debt |
  | $t$ | Marginal tax rate |
  | $r_e$ | Cost of equity |
  | *Significance*: Average cost of capital for firm—used as discount rate for capital budgeting. |  |

- **2. Modigliani-Miller Proposition (With Taxes)**

  - Firm Value: $$V_L = V_U + tD$$
  - Cost of Equity: $$r_e = r_0 + (r_0 - r_d)(1 - t)\frac{D}{E}$$
    | Variable | Definition |
    |----------|------------|
    | $V_L$ | Value of levered firm |
    | $V_U$ | Value of unlevered firm |
    | $r_0$ | Cost of equity for unlevered firm |
    *Significance*: Shows debt adds value due to tax shield (interest is tax-deductible).

- **3. Static Trade-Off Theory**
  $$V_L = V_U + tD - PV(\text{Financial Distress Costs})$$
  *Significance*: Balances tax benefits of debt with costs of financial distress (optimal capital structure = where marginal tax benefit = marginal distress cost).

##### **Learning Module 7: Business Models**

- No formulas—concepts (e.g., cost leadership, differentiation).

#### **VOLUME 4: FINANCIAL STATEMENT ANALYSIS**

##### **Learning Module 1: Introduction**

- No formulas—concepts (e.g., financial statement objectives).

##### **Learning Module 2: Analyzing Income Statements**

- **1. Profit Metrics**

  - Gross Profit: $$\text{Gross Profit} = \text{Revenue} - \text{COGS}$$
  - Operating Income: $$\text{Operating Income} = \text{Gross Profit} - \text{SGA Expenses}$$
  - Net Income: $$\text{Net Income} = \text{Operating Income} - \text{Interest} - \text{Taxes}$$

- **2. Retained Earnings**
  $$\text{Ending RE} = \text{Beginning RE} + \text{Net Income} - \text{Dividends}$$

- **3. Earnings Per Share (EPS)**

  - Basic EPS: $$\text{Basic EPS} = \frac{\text{Net Income} - \text{Preferred Dividends}}{\text{Weighted Avg Common Shares Outstanding}}$$
  - Diluted EPS (Convertible Preferred): $$\text{Diluted EPS} = \frac{\text{Net Income}}{\text{Weighted Avg Shares} + \text{New Shares from Conversion}}$$
    *Significance*: Measures earnings per common share—diluted EPS is lower (more conservative).

##### **Learning Module 3: Analyzing Balance Sheets**

- **1. Working Capital**
  $$\text{Working Capital} = \text{Current Assets} - \text{Current Liabilities}$$

- **2. Solvency Ratios**

  - Debt-to-Equity: $$\frac{\text{Total Debt}}{\text{Total Equity}}$$
  - Financial Leverage: $$\frac{\text{Total Assets}}{\text{Total Equity}}$$
    *Significance*: Measure long-term solvency—higher = more financial risk.

##### **Learning Module 4-5: Analyzing Cash Flows**

- **1. Cash Flow from Operations (CFO)**
  $$CFO = \text{Net Income} + \text{Non-Cash Charges} - \text{WC Investments}$$

- **2. Free Cash Flow to Firm (FCFF)**
  $$FCFF = CFO + \text{Interest}(1 - t) - \text{FCInv}$$

  | Variable | Definition |
  | --- | --- |
  | $FCInv$ | Capital expenditures |

- **3. Free Cash Flow to Equity (FCFE)**
  $$FCFE = CFO - \text{FCInv} + \text{Net Borrowing}$$
  *Significance*: FCFF = cash flow for all investors; FCFE = cash flow for equity holders (used in valuation).

##### **Learning Module 6: Analysis of Inventories**

- **1. Inventory Valuation**

  - IFRS: $$\text{Inventory} = \text{Lower of Cost or Net Realizable Value (NRV)}$$
  - US GAAP (LIFO/Retail): $$\text{Inventory} = \text{Lower of Cost or Market}$$
    $$\text{Market} = \text{Replacement Cost} \quad (\text{NRV} - \text{Normal Profit} \leq \text{Market} \leq \text{NRV})$$

- **2. Inventory Turnover**
  $$\text{Inventory Turnover} = \frac{\text{COGS}}{\text{Average Inventory}}$$
  $$\text{DOH} = \frac{365}{\text{Inventory Turnover}}$$
  *Significance*: Measures inventory efficiency—higher turnover = faster inventory sales.

##### **Learning Module 7: Analysis of Long-Term Assets**

- **1. Straight-Line Depreciation**
  $$\text{Annual Depreciation} = \frac{\text{Cost} - \text{Salvage Value}}{\text{Useful Life}}$$

- **2. Fixed Asset Turnover**
  $$\text{Fixed Asset Turnover} = \frac{\text{Revenue}}{\text{Average Net PP&E}}$$
  *Significance*: Measures efficiency of PP&E use—higher = better asset utilization.

##### **Learning Module 8: Long-Term Liabilities & Equity**

- **1. Lease Accounting (IFRS Finance Lease)**
  - Interest Expense: $$\text{Interest Expense} = \text{Implied Rate} \times \text{Beginning Lease Liability}$$
  - Principal Payment: $$\text{Principal Payment} = \text{Lease Payment} - \text{Interest Expense}$$

##### **Learning Module 9: Analysis of Income Taxes**

- **1. Deferred Tax Asset/Liability**

  - Assets: $$\text{Deferred Tax Asset/Liability} = t \times (\text{Carrying Amount} - \text{Tax Base})$$
  - Liabilities: $$\text{Deferred Tax Asset/Liability} = t \times (\text{Tax Base} - \text{Carrying Amount})$$
    | Variable | Definition |
    |----------|------------|
    | $t$ | Tax rate |
    *Significance*: Arises from temporary differences between accounting and tax treatment.

- **2. Effective Tax Rate**
  $$\text{Effective Tax Rate} = \frac{\text{Income Tax Expense}}{\text{Pre-Tax Income}}$$
  *Significance*: Actual tax rate paid (differs from statutory rate due to permanent differences).

##### **Learning Module 10: Financial Reporting Quality**

- **1. Depreciation Methods**
  - Double-Declining Balance: $$\text{Depreciation} = \frac{2}{\text{Useful Life}} \times (\text{Cost} - \text{Accumulated Depreciation})$$
  - Units-of-Production: $$\text{Depreciation} = \frac{\text{Units Produced}}{\text{Total Units}} \times (\text{Cost} - \text{Salvage Value})$$

##### **Learning Module 11: Financial Analysis Techniques**

- **1. Activity Ratios**

  - Receivables Turnover: $$\frac{\text{Revenue}}{\text{Average Receivables}}$$
  - DSO: $$\frac{365}{\text{Receivables Turnover}}$$
  - Payables Turnover: $$\frac{\text{Purchases}}{\text{Average Payables}}$$
  - DPO: $$\frac{365}{\text{Payables Turnover}}$$

- **2. Profitability Ratios**

  - Gross Margin: $$\frac{\text{Gross Profit}}{\text{Revenue}}$$
  - Operating Margin: $$\frac{\text{Operating Income}}{\text{Revenue}}$$
  - Net Margin: $$\frac{\text{Net Income}}{\text{Revenue}}$$
  - ROE: $$\frac{\text{Net Income}}{\text{Average Equity}}$$

- **3. DuPont Analysis**
  $$ROE = \text{Net Margin} \times \text{Total Asset Turnover} \times \text{Financial Leverage}$$
  *Significance*: Breaks down ROE into profitability, efficiency, and leverage components—identifies drivers of returns.

#### **VOLUME 5: EQUITY INVESTMENTS**

##### **Learning Module 1: Market Organization and Structure**

- **1. Margin Call Price**
  $$P_{\text{margin call}} = \frac{P_0 (1 - \text{Initial Margin})}{1 - \text{Maintenance Margin}}$$ 

  | Variable | Definition |
  | --- | --- |
  | $P_0$ | Initial purchase price |
  | *Significance*: Price at which investor must deposit more funds to meet maintenance margin. |  |

##### **Learning Module 2: Security Market Indexes**

- **1. Price Return Index**
  $$V_{PRI} = \frac{\sum_{i=1}^{N} n_i P_i}{D}$$

  | Variable | Definition |
  | --- | --- |
  | $n_i$ | Units of security $i$ |
  | $D$ | Divisor (adjusted for corporate actions) |

- **2. Total Return Index**
  $$V_{TRI} = V_{PRI} + \frac{\text{Total Income}}{\text{Divisor}}$$
  *Significance*: Includes income (dividends/coupons)—better measures total return from index.

- **3. Index Weighting**

  - Price Weighted: $$w_i^P = \frac{P_i}{\sum P_j}$$
  - Market-Cap Weighted: $$w_i^M = \frac{Q_i P_i}{\sum Q_j P_j}$$
  - Equal Weighted: $$w_i^E = \frac{1}{N}$$
    *Significance*: Different weighting schemes affect index performance (e.g., price-weighted overweights high-price stocks).

##### **Learning Module 3: Market Efficiency**

- No formulas—concepts (e.g., weak/semi-strong/strong form efficiency).

##### **Learning Module 4: Overview of Equity Securities**

- **1. ROE (Book Value)**
  $$ROE_t = \frac{NI_t}{(BVE_t + BVE_{t-1})/2}$$ 

  | Variable | Definition |
  | --- | --- |
  | $BVE$ | Book Value of Equity |

##### **Learning Module 5: Company Analysis**

- **1. Degree of Operating Leverage (DOL)**
  $$DOL = \frac{% \Delta \text{Operating Income}}{% \Delta \text{Sales}} = \frac{Q(P - VC)}{Q(P - VC) - FC}$$

  | Variable | Definition |
  | --- | --- |
  | $Q$ | Units sold |
  | $P$ | Price per unit |
  | $VC$ | Variable cost per unit |
  | $FC$ | Fixed costs |
  | *Significance*: Measures sensitivity of operating income to sales—higher = more operating risk. |  |

- **2. Degree of Financial Leverage (DFL)**
  $$DFL = \frac{% \Delta \text{Net Income}}{% \Delta \text{Operating Income}} = \frac{EBIT}{EBIT - Interest}$$
  *Significance*: Measures sensitivity of net income to operating income—higher = more financial risk.

##### **Learning Module 8: Equity Valuation**

- **1. Dividend Discount Model (DDM)**
  $$V_0 = \sum_{t=1}^{T} \frac{D_t}{(1 + r)^t} + \frac{P_T}{(1 + r)^T}$$

  | Variable | Definition |
  | --- | --- |
  | $P_T$ | Terminal value at time $T$ |

- **2. FCFE Valuation**
  $$V_0 = \sum_{t=1}^{\infty} \frac{FCFE_t}{(1 + r)^t}$$
  $$FCFE = CFO - FCInv + \text{Net Borrowing}$$

- **3. Sustainable Growth Rate**
  $$g = b \times ROE$$

  | Variable | Definition |
  | --- | --- |
  | $b$ | Retention rate ($= 1 - \text{Payout Ratio}$) |
  | *Significance*: Maximum growth rate without external equity financing—higher b/ROE = higher g. |  |

#### **VOLUME 6: FIXED INCOME**

##### **Learning Module 1: Fixed-Income Instrument Features**

- **1. Current Yield**
  $$\text{Current Yield} = \frac{\text{Annual Coupon}}{\text{Bond Price}}$$
  *Significance*: Simplified yield measure—ignores capital gains/losses.

- **2. Bond Price**
  $$PV = \sum_{t=1}^{n} \frac{PMT}{(1 + r)^t} + \frac{FV}{(1 + r)^n}$$

##### **Learning Module 2: Fixed-Income Cash Flows**

- **1. Fully Amortizing Loan Payment**
  $$A = \frac{r \times \text{Principal}}{1 - (1 + r)^{-N}}$$

- **2. Convertible Bond Metrics**

  - Conversion Ratio: $$\text{Conversion Ratio} = \frac{\text{Par Value}}{\text{Conversion Price}}$$
  - Conversion Value: $$\text{Conversion Value} = \text{Conversion Ratio} \times \text{Stock Price}$$

##### **Learning Module 4: Fixed-Income Markets for Corporate Issuers**

- **1. Repurchase Agreement (Repo) Price**
  $$\text{Repo Price} = \text{Bond Price} \times \left(1 + \text{Repo Rate} \times \frac{\text{Repo Days}}{360}\right)$$

##### **Learning Module 6: Bond Valuation: Prices and Yields**

- **1. Full vs. Flat Price**
  $$PV_{\text{Full}} = PV_{\text{Flat}} + \text{Accrued Interest}$$
  $$\text{Accrued Interest} = \frac{t}{T} \times PMT$$ 

  | Variable | Definition |
  | --- | --- |
  | $t$ | Days since last coupon |
  | $T$ | Days in coupon period |
  | *Significance*: Full price = price investor pays; flat price = quoted price (excludes accrued interest). |  |

##### **Learning Module 7: Yield and Yield Spreads**

- **1. Yield to Call (YTC)**
  $$PV = \sum_{t=1}^{N} \frac{PMT}{(1 + YTC)^t} + \frac{\text{Call Price}}{(1 + YTC)^N}$$
  *Significance*: Yield if bond is called before maturity—relevant for callable bonds.

- **2. Z-Spread**
  $$PV = \sum_{t=1}^{N} \frac{PMT}{(1 + z_t + Z)^t} + \frac{FV}{(1 + z_N + Z)^N}$$

  | Variable | Definition |
  | --- | --- |
  | $z_t$ | Spot rate for period $t$ |
  | $Z$ | Z-spread |
  | *Significance*: Constant spread added to spot rates to match bond price—includes credit and liquidity risk. |  |

##### **Learning Module 9: Term Structure of Interest Rates**

- **1. Forward Rate (IFR)**
  $$(1 + z_B)^B = (1 + z_A)^A \times (1 + IFR_{A,B-A})^{B-A}$$ 

  | Variable | Definition |
  | --- | --- |
  | $z_A, z_B$ | Spot rates for periods $A, B$ |
  | $IFR_{A,B-A}$ | Forward rate for $B-A$ periods starting at $A$ |

##### **Learning Module 10-13: Interest Rate Risk (Duration/Convexity)**

- **1. Macaulay Duration**
  $$MacDur = \sum_{t=1}^{N} t \times \frac{PV_t}{PV_{\text{Full}}}$$
  *Significance*: Weighted average time to receive cash flows—measures interest rate risk (higher = more risk).

- **2. Modified Duration**
  $$ModDur = \frac{MacDur}{1 + r}$$
  $$% \Delta PV \approx -ModDur \times \Delta r$$

- **3. Convexity**
  $$Convexity = \sum_{t=1}^{N} t(t+1) \times \frac{PV_t}{PV_{\text{Full}} \times (1 + r)^2}$$
  $$% \Delta PV \approx -ModDur \times \Delta r + 0.5 \times Convexity \times (\Delta r)^2$$
  *Significance*: Adjusts duration for non-linear price-yield relationship—higher convexity = less price loss when rates rise.

##### **Learning Module 14: Credit Risk**

- **1. Expected Loss (EL)**
  $$EL = LGD \times POD$$
  $$LGD = EE \times (1 - RR)$$ 

  | Variable | Definition |
  | --- | --- |
  | $POD$ | Probability of Default |
  | $LGD$ | Loss Given Default |
  | $EE$ | Expected Exposure |
  | $RR$ | Recovery Rate |
  | *Significance*: Expected credit loss—used to price credit risk (credit spreads). |  |

#### **VOLUME 7: DERIVATIVES**

##### **Learning Module 2: Forward Commitments**

- **1. Forward Contract Payoff**

  - Long: $$Payoff = S_T - F_0(T)$$
  - Short: $$Payoff = F_0(T) - S_T$$
    | Variable | Definition |
    |----------|------------|
    | $S_T$ | Spot price at maturity |
    | $F_0(T)$ | Forward price |

- **2. Futures Mark-to-Market**

  - Long Daily: $$\Delta = f_t(T) - f_{t-1}(T)$$
  - Short Daily: $$\Delta = f_{t-1}(T) - f_t(T)$$

- **3. Option Payoff/Profit**

  - Long Call: $$Payoff = \max(0, S_T - X) \quad ; \quad Profit = \max(0, S_T - X) - c_0$$
  - Long Put: $$Payoff = \max(0, X - S_T) \quad ; \quad Profit = \max(0, X - S_T) - p_0$$
    | Variable | Definition |
    |----------|------------|
    | $X$ | Strike price |
    | $c_0, p_0
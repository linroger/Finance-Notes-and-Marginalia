 **CFA Formula Sheet (2025) – Complete & Corrected**
 **2. CFA Level 1**
 **VOLUME 1: QUANTITATIVE METHODS**
 **Learning Module 1: Rates and Returns**
- **1.1 Determinants of Interest Rates**
  - Corrected Formula:
    $$r = r_{\text{real risk-free}} + \pi + r_{\text{default}} + r_{\text{maturity}} + r_{\text{liquidity}}$$
    - Where:
      - $r_{\text{real risk-free}}$: Return with no inflation/risk
      - $\pi$: Inflation premium (compensates for purchasing power loss)
      - $r_{\text{default}}$: Compensates for default risk (e.g., corporate vs govt bonds)
      - $r_{\text{maturity}}$: Compensates for longer time horizon risk
      - $r_{\text{liquidity}}$: Compensates for difficulty in selling quickly
    - **Significance**: Breaks down interest rates into fundamental components; core for understanding bond yields.

  - Nominal vs Real Risk-Free Rate:
    $$(1 + r_{\text{nominal risk-free}}) = (1 + r_{\text{real risk-free}}) \times (1 + \pi)$$
    - Simplified (for small $\pi$): $r_{\text{nominal risk-free}} \approx r_{\text{real risk-free}} + \pi$
    - **Purpose**: Adjusts nominal rates for inflation to get "real" purchasing power return.

  - Maturity Premium:
    $$r_{\text{maturity}} = r_{\text{long-term Treasury}} - r_{\text{short-term Treasury}}$$
    - **Purpose**: Quantifies the extra return for holding longer-maturity government bonds.

- **1.2 Holding Period Return (HPR)**
  - Single Period:
    $$R = \frac{P_1 - P_0 + I_1}{P_0}$$
    - Where: $P_0$ = Initial price, $P_1$ = Final price, $I_1$ = Income (dividends/coupons)
    - **Purpose**: Calculates total return over one period (price appreciation + income).

  - Multi Period:
    $$R = \prod_{t=1}^{T} (1 + R_t) - 1$$
    - **Purpose**: Accounts for compounding; accurate for returns over multiple periods.

- **1.3 Return Averages**
  - Arithmetic Mean:
    $$\overline{R}_A = \frac{1}{T} \sum_{t=1}^{T} R_t$$
    - **Purpose**: Simple average; used for estimating future single-period returns.

  - Geometric Mean:
    $$\overline{R}_G = \left( \prod_{t=1}^{T} (1 + R_t) \right)^{1/T} - 1$$
    - **Purpose**: Reflects compounding; better for multi-period return estimation (e.g., 5-year stock returns).

  - Harmonic Mean:
    $$\overline{R}_H = \frac{T}{\sum_{t=1}^{T} \frac{1}{R_t}} \quad (R_t > 0)$$
    - **Purpose**: Used for average price per unit (e.g., average cost of shares bought at different prices).

  - Relationship (2-period only):
    $$(\overline{R}_G)^2 = \overline{R}_A \times \overline{R}_H$$
    - **Note**: Does not hold for >2 periods; a simplification for CFA Level 1.

- **1.4 Money-Weighted Return (MWR)**
  - Formula:
    $$\sum_{t=0}^{T} \frac{CF_t}{(1 + MWR)^t} = 0$$
    - Where: $CF_t$ = Cash flows (outflows = negative, inflows = positive)
    - **Purpose**: Accounts for timing/size of cash flows; equals Internal Rate of Return (IRR) for portfolios.

- **1.5 Time-Weighted Return (TWR)**
  - Annualized (T > 1 year):
    $$\text{Annualized TWR} = \left( \prod_{t=1}^{T} (1 + R_t) \right)^{1/T} - 1$$
    - **Purpose**: Eliminates impact of cash flows; used to evaluate manager performance (fairer than MWR).

- **1.6 Non-Annual Compounding**
  - Present Value:
    $$PV = FV_N \times \left(1 + \frac{R_s}{m}\right)^{-mN}$$
    - Where: $R_s$ = Quoted annual rate, $m$ = Compounding periods/year, $N$ = Years
    - **Purpose**: Adjusts for non-annual compounding (e.g., monthly, quarterly) to find present value.

- **1.7 Annualizing Returns**
  - Weekly → Annual: $$R_{\text{annual}} = (1 + R_{\text{weekly}})^{52} - 1$$
  - Monthly → Annual: $$R_{\text{annual}} = (1 + R_{\text{monthly}})^{12} - 1$$
  - Daily → Annual: $$R_{\text{annual}} = (1 + R_{\text{daily}})^{252} - 1 \quad (\text{252 trading days/year})$$
  - **Purpose**: Standardizes returns to annual basis for comparison.

- **1.8 Continuously Compounded Returns**
  - Price Formula: $$P_t = P_0 e^{r_{0,T}}$$
  - Return Calculation: $$r_{0,T} = \ln\left( \frac{P_t}{P_0} \right)$$
  - Additivity: $$r_{0,T} = r_{0,1} + r_{1,2} + \dots + r_{T-1,T}$$
  - **Purpose**: Useful for derivatives pricing and statistical analysis (normal distribution property).

- **1.9 Real Returns**
  - Formula: $$(1 + r_{\text{real}}) = \frac{1 + r_{\text{nominal}}}{1 + \pi}$$
  - **Purpose**: Adjusts nominal return for inflation to measure true purchasing power gain/loss.

- **1.10 After-Tax Returns**
  - After-Tax Nominal: $$r_{\text{after-tax nominal}} = r_{\text{pre-tax nominal}} \times (1 - t)$$
  - After-Tax Real: $$r_{\text{after-tax real}} = \frac{1 + r_{\text{pre-tax nominal}} \times (1 - t)}{1 + \pi} - 1$$
  - Where: $t$ = Marginal tax rate
  - **Purpose**: Reflects actual return kept after taxes; critical for personal investing decisions.

- **1.11 Leveraged Return**
  - Formula: $$R_L = R_P + \frac{V_B}{V_E} (R_P - r_D)$$
  - Where: $R_P$ = Unleveraged portfolio return, $V_B$ = Debt, $V_E$ = Equity, $r_D$ = Debt cost
  - **Purpose**: Calculates return on equity when using leverage; amplifies gains/losses.


 **Learning Module 2: Time Value of Money (TVM) in Finance**
- **2.1 Single Cash Flow (Discrete Compounding)**
  - Future Value: $$FV_t = PV \times (1 + r)^t$$
  - Present Value: $$PV = \frac{FV_t}{(1 + r)^t}$$
  - Where: $r$ = Discount rate per period, $t$ = Number of periods
  - **Purpose**: Core TVM formulas; used for valuing lump sums (e.g., savings, bonds).

- **2.2 Continuous Compounding**
  - Future Value: $$FV_t = PV \times e^{rt}$$
  - Present Value: $$PV = FV_t \times e^{-rt}$$
  - **Purpose**: Used for assets with continuous compounding (e.g., some derivatives, savings accounts).

- **2.3 Zero-Coupon Bond Valuation**
  - Price: $$PV = \frac{FV}{(1 + r)^t}$$
  - Yield: $$r = \left( \frac{FV}{PV} \right)^{1/t} - 1$$
  - Where: $FV$ = Face value, $r$ = Market discount rate, $t$ = Maturity (years)
  - **Purpose**: Values bonds with no coupon payments (pure discount bonds).

- **2.4 Coupon Bond Valuation**
  - Price: $$PV = \sum_{t=1}^{N} \frac{PMT}{(1 + r)^t} + \frac{FV}{(1 + r)^N}$$
  - Where: $PMT$ = Periodic coupon ($\text{Coupon rate} \times FV / m$), $N$ = Total periods ($t \times m$)
  - **Purpose**: Values bonds with regular coupon payments; fundamental for fixed income.

- **2.5 Perpetual Bond Valuation**
  - Price: $$PV = \frac{PMT}{r}$$
  - **Purpose**: Values bonds with infinite coupon payments (e.g., UK Consols); no maturity.

- **2.6 Annuities (Level Payments)**
  - Periodic Payment (e.g., Mortgage): $$A = \frac{r \times PV}{1 - (1 + r)^{-t}}$$
  - Where: $A$ = Periodic payment, $t$ = Number of payments
  - **Purpose**: Calculates fixed payments for loans (mortgages) or savings plans (annuities).

- **2.7 Preferred Stock Valuation**
  - Perpetual (Non-Callable): $$PV = \frac{D}{r}$$
  - Where: $D$ = Fixed dividend, $r$ = Required return
  - **Purpose**: Values preferred stock (fixed dividends, priority over common stock).

- **2.8 Common Stock Valuation**
  - Constant Growth Model (Gordon Growth):
    $$PV_0 = \frac{D_1}{r - g} = \frac{D_0 (1 + g)}{r - g} \quad (r > g)$$
    - Where: $D_0$ = Recent dividend, $D_1 = D_0(1+g)$, $g$ = Constant growth rate
    - **Purpose**: Values stocks with stable dividend growth (e.g., mature companies).

  - Expected Return: $$r = \frac{D_1}{PV_0} + g$$
    - **Purpose**: Estimates required return for equity investors.

  - P/E Ratios:
    - Trailing: $$\frac{PV_0}{E_0} = \frac{(D_0/E_0)(1 + g)}{r - g}$$
    - Forward: $$\frac{PV_0}{E_1} = \frac{D_1/E_1}{r - g}$$
    - **Purpose**: Relates stock price to earnings; used for relative valuation.

  - Two-Stage DDM:
    $$PV_0 = \sum_{t=1}^{n} \frac{D_0 (1 + g_s)^t}{(1 + r)^t} + \frac{D_0 (1 + g_s)^n (1 + g_L)}{(r - g_L)(1 + r)^n}$$
    - Where: $g_s$ = Short-term growth, $g_L$ = Long-term growth ($g_L < r$)
    - **Purpose**: Values stocks with high initial growth (e.g., tech companies) that stabilizes.

- **2.9 Forward Rate (1-Year Forward 1-Year From Now)**
  - Formula: $$F_{1,1} = \frac{(1 + r_2)^2}{(1 + r_1)} - 1$$
  - Where: $r_1$ = 1-year spot rate, $r_2$ = 2-year spot rate
  - **Purpose**: Calculates implied future interest rates; used in term structure analysis.


 **Learning Module 3: Statistical Measures of Asset Returns**
- **3.1 Central Tendency**
  - Sample Mean: $$\overline{X} = \frac{1}{n} \sum_{i=1}^{n} X_i$$
  - **Purpose**: Average value of observations; measures "center" of data.

  - Median Position: $$\text{Position} = \frac{n + 1}{2}$$
  - **Purpose**: Middle value; robust to outliers (unlike mean).

  - Interquartile Range (IQR): $$IQR = Q_3 - Q_1$$
  - Where: $Q_1$ = 25th percentile, $Q_3$ = 75th percentile
  - **Purpose**: Measures spread of middle 50% of data; reduces outlier impact.

- **3.2 Box and Whisker Plot**
  - Upper Fence: $$Q_3 + 1.5 \times IQR$$
  - Lower Fence: $$Q_1 - 1.5 \times IQR$$
  - **Purpose**: Identifies outliers (values beyond fences); visualizes data distribution.

- **3.3 Dispersion Measures**
  - Range: $$\text{Range} = \text{Max value} - \text{Min value}$$
  - **Purpose**: Simple spread measure; sensitive to outliers.

  - Mean Absolute Deviation (MAD):
    $$MAD = \frac{1}{n} \sum_{i=1}^{n} |X_i - \overline{X}|$$
    - **Purpose**: Average absolute deviation from mean; avoids canceling positive/negative deviations.

  - Sample Variance: $$s^2 = \frac{1}{n - 1} \sum_{i=1}^{n} (X_i - \overline{X})^2$$
  - Sample Standard Deviation: $$s = \sqrt{s^2}$$
    - **Purpose**: Measures volatility; $n-1$ corrects for sample bias (unbiased estimator).

  - Target Semideviation: $$s_{\text{target}} = \sqrt{\frac{1}{n - 1} \sum_{X_i \leq B} (X_i - B)^2}$$
    - Where: $B$ = Target return
    - **Purpose**: Measures downside risk (only returns below target); critical for risk-averse investors.

  - Coefficient of Variation (CV): $$CV = \frac{s}{\overline{X}}$$
    - **Purpose**: Risk per unit of return; compares volatility across assets with different returns.

- **3.4 Distribution Shape**
  - Sample Skewness:
    $$\text{Skewness} \approx \frac{1}{n} \sum_{i=1}^{n} \frac{(X_i - \overline{X})^3}{s^3}$$
    - **Interpretation**: Positive = Right-skewed (few high values), Negative = Left-skewed (few low values).

  - Sample Excess Kurtosis:
    $$K_E \approx \frac{1}{n} \sum_{i=1}^{n} \frac{(X_i - \overline{X})^4}{s^4} - 3$$
    - **Interpretation**: Positive = Leptokurtic (fat tails, more extreme values), Negative = Platykurtic (thin tails).

- **3.5 Correlation & Covariance**
  - Sample Covariance:
    $$s_{XY} = \frac{1}{n - 1} \sum_{i=1}^{n} (X_i - \overline{X})(Y_i - \overline{Y})$$
    - **Purpose**: Measures linear relationship direction/magnitude (units depend on X/Y).

  - Sample Correlation Coefficient:
    $$r_{XY} = \frac{s_{XY}}{s_X s_Y}$$
    - **Range**: $-1 \leq r_{XY} \leq 1$; **Purpose**: Standardized covariance (no units); measures strength of linear relationship.


 **Learning Module 4: Probability Trees and Conditional Expectations**
- **4.1 Expected Value (Discrete Random Variable)**
  - Formula: $$E(X) = \sum_{i=1}^{n} P(X_i) X_i$$
  - Where: $P(X_i)$ = Probability of $X_i$, $X_i$ = Possible values
  - **Purpose**: Weighted average of outcomes; predicts "expected" result.

- **4.2 Variance (Random Variable)**
  - Formula: $$\sigma^2(X) = E\left[ (X - E(X))^2 \right] = \sum_{i=1}^{n} P(X_i) (X_i - E(X))^2$$
  - **Purpose**: Measures spread of outcomes around expected value; quantifies risk.

- **4.3 Conditional Expected Value**
  - Formula: $$E(X | S) = \sum_{i=1}^{n} P(X_i | S) X_i$$
  - Where: $P(X_i | S)$ = Probability of $X_i$ given event $S$
  - **Purpose**: Expected value of X when additional information (S) is known.

- **4.4 Conditional Variance**
  - Formula: $$\sigma^2(X | S) = \sum_{i=1}^{n} P(X_i | S) (X_i - E(X | S))^2$$
  - **Purpose**: Variance of X given event S; adjusts risk based on new information.

- **4.5 Total Probability Rule for Expectation**
  - Formula: $$E(X) = \sum_{i=1}^{n} E(X | S_i) P(S_i)$$
  - Where: $S_1, ..., S_n$ = Mutually exclusive, exhaustive events
  - **Purpose**: Calculates expected value by breaking into smaller, known scenarios.

- **4.6 Bayes’ Formula**
  - Basic: $$P(A | B) = \frac{P(B | A) P(A)}{P(B)}$$
  - General: $$P(\text{Event} | \text{Info}) = \frac{P(\text{Info} | \text{Event}) P(\text{Event})}{P(\text{Info})}$$
  - **Purpose**: Updates probabilities based on new information (e.g., updating default probability after credit rating change).


 **Learning Module 5: Portfolio Mathematics**
- **5.1 Expected Portfolio Return (n Assets)**
  - Formula: $$E(R_P) = \sum_{i=1}^{n} w_i E(R_i)$$
  - Where: $w_i$ = Weight of asset $i$ ($\sum w_i = 1$), $E(R_i)$ = Expected return of $i$
  - **Purpose**: Calculates portfolio return as weighted average of asset returns.

- **5.2 Portfolio Variance (n Assets)**
  - Formula: $$\sigma^2(R_P) = \sum_{i=1}^{n} \sum_{j=1}^{n} w_i w_j \text{Cov}(R_i, R_j)$$
  - **Requirement**: $n$ variances + $\frac{n(n-1)}{2}$ covariances
  - **Purpose**: Measures portfolio risk; accounts for asset correlations (diversification).

- **5.3 Covariance Calculation**
  - Formula: $$\text{Cov}(R_i, R_j) = \frac{1}{n - 1} \sum_{t=1}^{n} (R_{i,t} - \overline{R}_i)(R_{j,t} - \overline{R}_j)$$
  - **Relationship to Correlation**: $$\text{Cov}(R_i, R_j) = \rho_{i,j} \sigma_i \sigma_j$$
    - Where: $\rho_{i,j}$ = Correlation between $i$ and $j$
  - **Purpose**: Input for portfolio variance; measures co-movement.

- **5.4 Two-Asset Portfolio**
  - Variance: $$\sigma^2(R_P) = w_1^2 \sigma_1^2 + w_2^2 \sigma_2^2 + 2 w_1 w_2 \rho_{1,2} \sigma_1 \sigma_2$$
  - **Key Insight**: Diversification works if $\rho_{1,2} < 1$ (reduces portfolio variance).

- **5.5 Three-Asset Portfolio**
  - Variance:
    $$\sigma^2(R_P) = w_1^2 \sigma_1^2 + w_2^2 \sigma_2^2 + w_3^2 \sigma_3^2 + 2 w_1 w_2 \text{Cov}(1,2) + 2 w_1 w_3 \text{Cov}(1,3) + 2 w_2 w_3 \text{Cov}(2,3)$$
  - **Purpose**: Extends two-asset case; shows increasing complexity with more assets.

- **5.6 Safety-First Ratio (SFRatio)**
  - Formula: $$\text{SFRatio} = \frac{E(R_P) - R_L}{\sigma_P}$$
  - Shortfall Risk: $$\text{Pr}(E(R_P) < R_L) = N(-\text{SFRatio})$$
    - Where: $R_L$ = Threshold return, $N(\cdot)$ = Standard normal CDF
  - **Purpose**: Evaluates portfolios for risk-averse investors (minimizes shortfall risk below $R_L$).


 **Learning Module 6: Simulation Methods**
- **6.1 Lognormal Distribution (for Asset Prices)**
  - Mean: $$\mu_L = e^{\mu + 0.5 \sigma^2}$$
  - Variance: $$\sigma_L^2 = e^{2\mu + \sigma^2} (e^{\sigma^2} - 1)$$
    - Where: $\mu$ = Mean of underlying normal variable (log returns), $\sigma^2$ = Variance of normal variable
  - **Purpose**: Models asset prices (cannot be negative; right-skewed, like real prices).

- **6.2 Continuously Compounded Returns (i.i.d.)**
  - Price: $$P_T = P_0 e^{r_{0,T}}$$
  - Additivity: $$r_{0,T} = r_{0,1} + r_{1,2} + \dots + r_{T-1,T}$$
  - Mean Return: $$E(r_{0,T}) = \mu T$$
  - Variance: $$\sigma^2(r_{0,T}) = \sigma^2 T$$
  - Standard Deviation: $$\sigma(r_{0,T}) = \sigma \sqrt{T}$$
  - **Purpose**: Simplifies multi-period return calculations; used in Monte Carlo simulations.


 **Learning Module 7: Estimation and Inference**
- **7.1 Sharpe Ratio**
  - Formula: $$\text{Sharpe Ratio} = \frac{R_P - R_F}{\sigma_P}$$
  - Where: $R_F$ = Risk-free rate
  - **Purpose**: Measures risk-adjusted return (excess return per unit of total risk); compares portfolios.

- **7.2 Sampling Distribution (Sample Mean)**
  - Variance: $$\sigma_{\overline{X}}^2 = \frac{\sigma^2}{n}$$
  - Standard Error (SE): $$\sigma_{\overline{X}} = \frac{\sigma}{\sqrt{n}}$$
    - **Note**: If $\sigma$ (population SD) unknown, use $s$ (sample SD)
  - **Purpose**: Measures variability of sample mean; critical for hypothesis testing/confidence intervals.

- **7.3 Bootstrap Resampling (Standard Error)**
  - Formula: $$s_{\overline{X}} = \sqrt{\frac{1}{B - 1} \sum_{b=1}^{B} (\hat{\theta}_b - \overline{\theta})^2}$$
    - Where: $B$ = Number of resamples, $\hat{\theta}_b$ = Mean of resample $b$, $\overline{\theta}$ = Mean of all resample means
  - **Purpose**: Estimates SE when population distribution is unknown (non-parametric).


 **Learning Module 8: Hypothesis Testing**
- **8.1 Key Definitions**
  - Confidence Level: $$1 - \alpha$$ ($\alpha$ = Type I error probability: reject true null)
  - Test Power: $$1 - \beta$$ ($\beta$ = Type II error probability: fail to reject false null)

- **8.2 Test of Single Mean (t-Test)**
  - Test Statistic: $$t = \frac{\overline{X} - \mu_0}{s / \sqrt{n}}$$
  - Degrees of Freedom (df): $$n - 1$$
  - Confidence Interval: $$\overline{X} \pm t_{\alpha/2, df} \times \frac{s}{\sqrt{n}}$$
  - **Purpose**: Tests if sample mean differs from hypothesized population mean (e.g., "Is stock return > 5%?").

- **8.3 Test of Difference in Means (Pooled Variance t-Test)**
  - Test Statistic: $$t = \frac{(\overline{X}_1 - \overline{X}_2) - (\mu_1 - \mu_2)}{\sqrt{\frac{s_p^2}{n_1} + \frac{s_p^2}{n_2}}}$$
  - Pooled Variance: $$s_p^2 = \frac{(n_1 - 1)s_1^2 + (n_2 - 1)s_2^2}{n_1 + n_2 - 2}$$
  - df: $$n_1 + n_2 - 2$$
  - **Purpose**: Tests if means of two independent samples differ (e.g., "Do returns of two funds differ?").

- **8.4 Test of Mean of Differences (Paired t-Test)**
  - Test Statistic: $$t = \frac{\overline{d} - \mu_{d0}}{s_{\overline{d}}}$$
  - Where: $\overline{d}$ = Mean of paired differences, $s_{\overline{d}} = s_d / \sqrt{n}$
  - df: $$n - 1$$
  - **Purpose**: Tests if mean difference between paired observations is zero (e.g., "Did returns change after policy?").

- **8.5 Test of Single Variance (Chi-Square Test)**
  - Test Statistic: $$\chi^2 = \frac{(n - 1)s^2}{\sigma_0^2}$$
  - df: $$n - 1$$
  - **Purpose**: Tests if population variance differs from hypothesized value (e.g., "Is fund volatility > 15%?").

- **8.6 Test of Difference in Variances (F-Test)**
  - Test Statistic: $$F = \frac{s_1^2}{s_2^2}$$ (always $s_{\text{larger}}^2 / s_{\text{smaller}}^2$ for one-tailed test)
  - df: $$df_1 = n_1 - 1, df_2 = n_2 - 1$$
  - **Purpose**: Tests if variances of two populations differ (e.g., "Is volatility of Fund A > Fund B?").

- **8.7 Test of Correlation (t-Test)**
  - Test Statistic: $$t = \frac{r \sqrt{n - 2}}{\sqrt{1 - r^2}}$$
  - df: $$n - 2$$
  - **Purpose**: Tests if population correlation is zero (e.g., "Is there a linear relationship between stock and bond returns?").

- **8.8 Test of Independence (Chi-Square Test)**
  - Test Statistic: $$\chi^2 = \sum_{i,j} \frac{(O_{ij} - E_{ij})^2}{E_{ij}}$$
  - Where: $O_{ij}$ = Observed count, $E_{ij} = \frac{\text{Row Total}_i \times \text{Column Total}_j}{\text{Grand Total}}$
  - df: $$(r - 1)(c - 1)$$ ($r$ = Rows, $c$ = Columns)
  - **Purpose**: Tests if two categorical variables are independent (e.g., "Is credit rating independent of industry?").


 **Learning Module 9: Parametric and Non-Parametric Tests of Independence**
- **9.1 Test of Correlation (Same as Module 8.7)**
  - t-Test Statistic: $$t = \frac{r \sqrt{n - 2}}{\sqrt{1 - r^2}}$$
  - **Purpose**: Parametric test for linear correlation (assumes normal distribution).

- **9.2 Pearson Correlation Coefficient**
  - Formula: $$r_{XY} = \frac{s_{XY}}{s_X s_Y}$$
  - **Purpose**: Measures linear correlation (parametric; requires continuous data, normality).

- **9.3 Spearman Rank Correlation Coefficient**
  - Formula: $$r_S = 1 - \frac{6 \sum_{i=1}^{n} d_i^2}{n(n^2 - 1)}$$
  - Where: $d_i$ = Difference in ranks of $X_i$ and $Y_i$
  - **Purpose**: Non-parametric test for monotonic relationship (no normality assumption; uses ranks).

- **9.4 Test of Independence (Chi-Square, Same as Module 8.8)**
  - **Purpose**: Non-parametric test for categorical variables (no distribution assumptions).

- **9.5 Standardized Residual**
  - Formula: $$\text{Standardized Residual} = \frac{O_{ij} - E_{ij}}{\sqrt{E_{ij}}}$$
  - **Purpose**: Identifies cells driving Chi-Square test results (values > 2 or < -2 are significant).


 **Learning Module 10: Simple Linear Regression**
- **10.1 Regression Model**
  - Population Model: $$Y_i = b_0 + b_1 X_i + \varepsilon_i$$
  - Estimated Model: $$\hat{Y}_i = \hat{b}_0 + \hat{b}_1 X_i + e_i$$
    - Where: $Y$ = Dependent variable, $X$ = Independent variable, $\hat{b}_0$ = Intercept, $\hat{b}_1$ = Slope, $e_i = Y_i - \hat{Y}_i$ = Residual
  - **Purpose**: Models linear relationship between $X$ and $Y$ (e.g., "Does GDP growth predict stock returns?").

- **10.2 Slope and Intercept Calculation**
  - Slope: $$\hat{b}_1 = \frac{\text{Cov}(X,Y)}{\text{Var}(X)} = \frac{\sum_{i=1}^{n} (X_i - \overline{X})(Y_i - \overline{Y})}{\sum_{i=1}^{n} (X_i - \overline{X})^2}$$
  - Intercept: $$\hat{b}_0 = \overline{Y} - \hat{b}_1 \overline{X}$$
  - **Interpretation**: $\hat{b}_1$ = Change in $Y$ for 1-unit change in $X$; $\hat{b}_0$ = $Y$ when $X=0$.

- **10.3 Sum of Squares**
  - Total (SST): $$SST = \sum_{i=1}^{n} (Y_i - \overline{Y})^2 = SSR + SSE$$
  - Regression (SSR): $$SSR = \sum_{i=1}^{n} (\hat{Y}_i - \overline{Y})^2$$ (explained variation)
  - Error (SSE): $$SSE = \sum_{i=1}^{n} (Y_i - \hat{Y}_i)^2$$ (unexplained variation)

- **10.4 Coefficient of Determination ($R^2$)**
  - Formula: $$R^2 = \frac{SSR}{SST} = 1 - \frac{SSE}{SST}$$
  - **Interpretation**: % of $Y$ variation explained by $X$; $0 \leq R^2 \leq 1$.

- **10.5 Correlation Coefficient**
  - Formula: $$r = \sqrt{R^2} \times \text{sign}(\hat{b}_1)$$
  - **Interpretation**: Same sign as slope; measures strength of linear relationship.

- **10.6 ANOVA F-Test (Overall Significance)**
  - Mean Square Regression (MSR): $$MSR = \frac{SSR}{k}$$ ($k$ = Number of independent variables)
  - Mean Square Error (MSE): $$MSE = \frac{SSE}{n - k - 1}$$
  - F-Statistic: $$F = \frac{MSR}{MSE}$$
  - **Purpose**: Tests if at least one independent variable explains $Y$ (null: $b_1 = 0$).

- **10.7 Standard Error of Estimate ($s_e$)**
  - Formula: $$s_e = \sqrt{MSE} = \sqrt{\frac{SSE}{n - k - 1}}$$
  - **Purpose**: Measures average prediction error; lower = better model fit.

- **10.8 Hypothesis Test of Slope**
  - t-Statistic: $$t = \frac{\hat{b}_1 - B_1}{s_{\hat{b}_1}}$$
  - Where: $s_{\hat{b}_1} = \frac{s_e}{\sqrt{\sum_{i=1}^{n} (X_i - \overline{X})^2}}$ (SE of slope)
  - df: $$n - k - 1$$
  - **Purpose**: Tests if slope is zero (no linear relationship).

- **10.9 Prediction Interval**
  - Formula: $$\hat{Y}_f \pm t_{\alpha/2, df} \times s_f$$
  - Where: $s_f = s_e \sqrt{1 + \frac{1}{n} + \frac{(X_f - \overline{X})^2}{(n - 1)s_X^2}}$ (SE of forecast)
  - **Purpose**: Range of likely $Y$ values for a given $X_f$ (wider than confidence interval for mean $Y$).

- **10.10 Regression Model Forms**
  - Log-Lin: $$\ln(Y_i) = b_0 + b_1 X_i$$ (X affects Y growth rate)
  - Lin-Log: $$Y_i = b_0 + b_1 \ln(X_i)$$ (X% change affects Y level)
  - Log-Log: $$\ln(Y_i) = b_0 + b_1 \ln(X_i)$$ (X% change affects Y% change; elasticity = $b_1$)


 **Learning Module 11: Introduction to Big Data Techniques**
- **No Formulas**
- **Key Concepts**: Structured vs Unstructured Data, Machine Learning (Supervised/Unsupervised), Big Data Challenges (Volume, Velocity, Variety), Data Preprocessing (Cleaning, Normalization).


 **VOLUME 2: ECONOMICS**
 **Learning Module 1: The Firm and Market Structures**
- **1.1 Profit Calculations**
  - Total Profit: $$\text{Total Profit} = \text{Total Revenue (TR)} - \text{Total Cost (TC)}$$
  - Economic Profit: $$\text{Economic Profit} = TR - \text{Total Economic Costs (TC + Opportunity Costs)}$$
  - Accounting Profit: $$\text{Accounting Profit} = TR - \text{Accounting Costs (Explicit Costs)}$$
  - **Key Difference**: Economic profit includes opportunity costs (e.g., owner’s time); accounting profit does not.

- **1.2 Revenue & Cost Metrics**
  - Total Revenue: $$TR = P \times Q$$
  - Average Revenue (AR): $$AR = \frac{TR}{Q} = P$$
  - Marginal Cost (MC): $$MC = \frac{\Delta TC}{\Delta Q}$$ (cost of last unit produced)
  - Average Variable Cost (AVC): $$AVC = \frac{\text{Total Variable Cost (TVC)}}{Q}$$
  - Average Fixed Cost (AFC): $$AFC = \frac{\text{Total Fixed Cost (TFC)}}{Q}$$
  - Total Cost: $$TC = TFC + TVC$$
  - Average Total Cost (ATC): $$ATC = AFC + AVC$$

- **1.3 Market Concentration**
  - Concentration Ratio (CRn): $$CR_n = \sum_{i=1}^{n} \text{Market Share}_i$$
    - **Purpose**: Measures market power of top n firms (e.g., CR4 = top 4 firms).
  - Herfindahl-Hirschman Index (HHI): $$HHI = \sum_{i=1}^{n} (\text{Market Share}_i)^2$$
    - **Interpretation**: Higher = more concentrated (e.g., HHI > 2500 = Highly Concentrated).


 **Learning Module 2: Understanding Business Cycles**
- **No Formulas**
- **Key Concepts**: Business Cycle Phases (Expansion, Peak, Contraction, Trough), Leading/Lagging/Coincident Indicators (e.g., Leading: ISM New Orders, Lagging: Unemployment Rate), Economic Growth Drivers (Labor, Capital, TFP).


 **Learning Module 3: Fiscal Policy**
- **3.1 Budget Surplus/Deficit**
  - Formula: $$\text{Budget Surplus/Deficit} = G - T + B$$
  - Where: $G$ = Government Spending, $T$ = Taxes, $B$ = Transfer Payments
  - **Interpretation**: Positive = Surplus, Negative = Deficit.

- **3.2 Disposable Income (YD)**
  - Formula: $$YD = Y - NT = (1 - t)Y$$
  - Where: $Y$ = Income, $NT$ = Net Taxes ($T - B$), $t$ = Net Tax Rate
  - **Purpose**: Income available for consumption/savings.

- **3.3 Fiscal Multiplier**
  - Formula: $$\text{Fiscal Multiplier} = \frac{1}{1 - c(1 - t)}$$
  - Where: $c$ = Marginal Propensity to Consume (MPC: % of YD spent), $t$ = Tax Rate
  - **Interpretation**: Measures impact of $1 change in G/T on GDP (e.g., multiplier = 2 → $1 G increase → $2 GDP increase).


 **Learning Module 4: Monetary Policy**
- **4.1 Neutral Rate**
  - Formula: $$\text{Neutral Rate} = \text{Trend GDP Growth} + \text{Inflation Target}$$
  - **Purpose**: Interest rate where monetary policy is neither expansionary nor contractionary (Taylor Rule input).

- **4.2 Taylor Rule (Extended)**
  - Formula: $$i^* = r_{\text{neutral}} + \pi_e + 0.5(\pi_e - \pi_{\text{target}}) + 0.5(Y_e - Y_{\text{trend}})$$
  - Where: $i^*$ = Target Policy Rate, $\pi_e$ = Expected Inflation, $Y_e$ = Expected GDP, $Y_{\text{trend}}$ = Trend GDP
  - **Purpose**: Guides central bank policy (e.g., raise rates if inflation > target or GDP > trend).


 **Learning Module 5: Introduction to Geopolitics**
- **No Formulas**
- **Key Concepts**: Geopolitical Risks (War, Sanctions, Trade Barriers), Impact on Markets (Commodity Prices, Currency Volatility), Geopolitical Strategy (Diversification, Risk Hedging).


 **Learning Module 6: International Trade**
- **No Formulas**
- **Key Concepts**: Comparative Advantage (Ricardo), Absolute Advantage (Smith), Trade Barriers (Tariffs, Quotas), Trade Agreements (Free Trade Areas, Customs Unions), Balance of Payments (Current Account, Capital Account).


 **Learning Module 7: Capital Flows and the FX Market**
- **7.1 Real Exchange Rate**
  - Formula: $$\text{Real Exchange Rate}_{d/f} = S_{d/f} \times \frac{P_f}{P_d}$$
  - Where: $S_{d/f}$ = Nominal Spot Rate (Domestic/ Foreign), $P_f$ = Foreign Price Level, $P_d$ = Domestic Price Level
  - **Purpose**: Measures purchasing power of currency (e.g., real appreciation = domestic goods more expensive).

- **7.2 % Change in Real Exchange Rate**
  - Approximation: $$\% \Delta \text{Real Rate} \approx \% \Delta S_{d/f} + \% \Delta P_f - \% \Delta P_d$$
  - **Purpose**: Captures inflation-adjusted currency movement.

- **7.3 % Change in Base Currency**
  - Formula: $$\% \Delta S_{d/f} = \frac{E(S_{d/f}) - S_{d/f}}{S_{d/f}}$$
  - **Interpretation**: Positive = Base currency (f) appreciates vs Domestic (d).


 **Learning Module 8: Exchange Rate Calculations**
- **8.1 Cross Rate**
  - Formula: $$\frac{A}{B} = \frac{A}{C} \times \frac{C}{B}$$
  - **Purpose**: Calculates exchange rate between two currencies using a third (e.g., $A/B$ using $A/C$ and $C/B$).

- **8.2 Forward Rate**
  - Formula: $$F_{A/B} = S_{A/B} \times \frac{1 + r_A \times T}{1 + r_B \times T}$$
  - Forward Points: $$\text{Forward Points} = F_{A/B} - S_{A/B} = S_{A/B} \times \frac{r_A - r_B}{1 + r_B} \times T$$
    - Where: $r_A$ = Interest Rate (Currency A), $r_B$ = Interest Rate (Currency B), $T$ = Time to Maturity (years)
  - **Purpose**: Locks in future exchange rate; based on Interest Rate Parity (IRP).


 **VOLUME 3: CORPORATE ISSUERS**
 **Learning Module 1: Organizational Forms, Corporate Issuer Features, and Ownership**
- **No Formulas**
- **Key Concepts**: Organizational Forms (Sole Proprietorship, Partnership, Corporation), Corporate Governance (Board of Directors, Shareholder Rights), Ownership Structures (Public vs Private, Concentrated vs Diffused).


 **Learning Module 2: Investors and Other Stakeholders**
- **No Formulas**
- **Key Concepts**: Stakeholders (Shareholders, Creditors, Employees, Customers), Agency Conflicts (Shareholder-Manager, Shareholder-Creditor), Mechanisms to Mitigate Conflicts (Executive Compensation, Debt Covenants).


 **Learning Module 3: Working Capital and Liquidity**
- **3.1 Cash Conversion Cycle (CCC)**
  - Formula: $$CCC = \text{Days of Inventory on Hand (DOH)} + \text{Days Sales Outstanding (DSO)} - \text{Days Payables Outstanding (DPO)}$$
  - Where:
    - $DOH = \frac{365}{\text{Inventory Turnover}}$, $DSO = \frac{365}{\text{Receivables Turnover}}$, $DPO = \frac{365}{\text{Payables Turnover}}$
  - **Purpose**: Measures time to convert inventory to cash (shorter = better liquidity).

- **3.2 Financing Cost (Trade Credit)**
  - Formula: $$\text{Financing Cost} = \left(1 + \frac{\text{Discount\%}}{100\% - \text{Discount\%}}\right)^{\frac{365}{\text{Payment Period} - \text{Discount Period}}} - 1$$
  - **Purpose**: Cost of forgoing early payment discount (e.g., "2/10 net 30" → cost of paying on day 30).

- **3.3 Working Capital Definitions**
  - Total Working Capital: $$\text{Total Working Capital} = \text{Current Assets} - \text{Current Liabilities}$$
  - Net Working Capital (NWC): $$NWC = (\text{Current Assets} - \text{Cash} - \text{Marketable Securities}) - (\text{Current Liabilities} - \text{Short-Term Debt})$$
  - **Purpose**: Measures short-term liquidity (NWC excludes non-operating items).

- **3.4 Cash Flow Metrics**
  - Cash Flow from Operations (CFO):
    $$CFO = \text{Cash from Customers} + \text{Interest/Dividends Received} - \text{Cash to Employees/Suppliers} - \text{Taxes Paid} - \text{Interest Paid}$$
  - Free Cash Flow (FCF): $$FCF = CFO - \text{Investments in Long-Term Assets}$$
  - **Purpose**: FCF is cash available for distribution to investors.

- **3.5 Liquidity Ratios**
  - Current Ratio: $$\text{Current Ratio} = \frac{\text{Current Assets}}{\text{Current Liabilities}}$$
    - **Interpretation**: >1 = Can cover short-term obligations.
  - Quick Ratio (Acid-Test): $$\text{Quick Ratio} = \frac{\text{Cash} + \text{Marketable Securities} + \text{Receivables}}{\text{Current Liabilities}}$$
    - **Interpretation**: Excludes inventory (less liquid); stricter than current ratio.
  - Cash Ratio: $$\text{Cash Ratio} = \frac{\text{Cash} + \text{Marketable Securities}}{\text{Current Liabilities}}$$
    - **Interpretation**: Strictest liquidity measure (only most liquid assets).


 **Learning Module 4: Corporate Governance: Conflicts, Mechanisms, Risks, and Benefits**
- **No Formulas**
- **Key Concepts**: Agency Problems (Managerial Entrenchment, Empire Building), Governance Mechanisms (Independent Directors, Audit Committees, Shareholder Voting), Benefits of Good Governance (Lower Cost of Capital, Higher Valuation).


 **Learning Module 5: Capital Investments and Capital Allocation**
- **5.1 Net Present Value (NPV)**
  - Formula: $$NPV = \sum_{t=0}^{T} \frac{CF_t}{(1 + r)^t}$$
  - Where: $CF_t$ = After-tax cash flow ( $CF_0$ = Initial Outlay, negative), $r$ = Required Return
  - **Purpose**: Primary capital budgeting tool; Accept if NPV > 0 (adds value to firm).

- **5.2 Internal Rate of Return (IRR)**
  - Formula: $$\sum_{t=0}^{T} \frac{CF_t}{(1 + IRR)^t} = 0$$
  - **Purpose**: Discount rate where NPV = 0; Accept if IRR > Required Return (caveat: multiple IRRs for non-conventional CFs).

- **5.3 Return on Invested Capital (ROIC)**
  - Basic: $$ROIC = \frac{\text{After-Tax Operating Profit}}{\text{Average Invested Capital}}$$
  - DuPont: $$ROIC = \frac{\text{After-Tax Operating Profit}}{\text{Sales}} \times \frac{\text{Sales}}{\text{Average Invested Capital}}$$
  - **Purpose**: Measures efficiency of capital allocation (higher = better use of capital).

- **5.4 Real Options in Capital Budgeting**
  - Formula: $$NPV_{\text{with Option}} = NPV_{\text{without Option}} - \text{Option Cost} + \text{Option Value}$$
  - **Purpose**: Adjusts NPV for flexibility (e.g., expand, abandon, delay project).


 **Learning Module 6: Capital Structure**
- **6.1 Weighted Average Cost of Capital (WACC)**
  - Formula: $$WACC = w_d r_d (1 - t) + w_e r_e$$
  - Where:
    - $w_d = \frac{D}{D + E}$, $w_e = \frac{E}{D + E}$ (target weights),
    - $r_d$ = Pre-tax Cost of Debt, $t$ = Marginal Tax Rate,
    - $r_e$ = Cost of Equity
  - **Purpose**: Discount rate for firm cash flows (WACC reflects all capital providers).

- **6.2 Operating Leverage**
  - Formula: $$\text{Operating Leverage} = \frac{\text{Fixed Costs}}{\text{Total Costs}}$$
  - **Interpretation**: Higher = more sensitive to sales changes (e.g., high fixed costs → small sales drop → large profit drop).

- **6.3 Interest Coverage Ratio**
  - Formula: $$\text{Interest Coverage} = \frac{\text{EBIT}}{\text{Interest Expense}}$$
  - **Purpose**: Measures ability to cover interest payments (higher = lower default risk).

- **6.4 Modigliani-Miller (M&M) Propositions (With Taxes)**
  - Proposition 1 (Firm Value): $$V_L = V_U + tD$$
    - Where: $V_L$ = Levered Value, $V_U$ = Unlevered Value, $tD$ = Tax Shield (interest is tax-deductible)
    - **Significance**: Debt increases firm value due to tax shield.
  - Proposition 2 (Cost of Equity): $$r_e = r_0 + (r_0 - r_d)(1 - t)\frac{D}{E}$$
    - Where: $r_0$ = Cost of Equity (Unlevered)
    - **Significance**: Cost of equity increases with leverage (compensates for higher risk).

- **6.5 Static Trade-Off Theory**
  - Formula: $$V_L = V_U + tD - PV(\text{Costs of Financial Distress})$$
  - **Purpose**: Balances tax shield of debt against bankruptcy costs (optimal leverage where marginal benefit = marginal cost).


 **Learning Module 7: Business Models**
- **No Formulas**
- **Key Concepts**: Business Model Types (Asset-Light, Subscription, Marketplace), Revenue Streams (Product Sales, Licensing, Advertising), Cost Structures (Fixed vs Variable), Competitive Advantage (Moats).


 **VOLUME 4: FINANCIAL STATEMENT ANALYSIS**
 **Learning Module 1: Introduction to Financial Statement Analysis**
- **No Formulas**
- **Key Concepts**: Financial Statements (Income Statement, Balance Sheet, Cash Flow Statement), IFRS vs US GAAP Differences, Analysis Framework (State Purpose, Gather Data, Process Data, Analyze, Report).


 **Learning Module 2: Analyzing Income Statements**
- **2.1 Profit Calculations**
  - Gross Profit: $$\text{Gross Profit} = \text{Revenue} - \text{Cost of Goods Sold (COGS)}$$
  - Operating Income (EBIT): $$\text{EBIT} = \text{Gross Profit} - \text{Selling, General, Administrative (SG&A) Expenses}$$
  - Taxable Income (EBT): $$\text{EBT} = \text{EBIT} - \text{Interest Expense}$$
  - Net Income: $$\text{Net Income} = \text{EBT} - \text{Income Taxes}$$

- **2.2 Equity and Retained Earnings**
  - Ending Shareholders’ Equity:
    $$\text{Ending Equity} = \text{Beginning Equity} + \text{Net Income} + \text{Other Comprehensive Income} - \text{Dividends}$$
  - Ending Retained Earnings:
    $$\text{Ending Retained Earnings} = \text{Beginning Retained Earnings} + \text{Net Income} - \text{Dividends}$$

- **2.3 Profitability Metrics**
  - Return on Equity (ROE): $$ROE = \frac{\text{Net Income}}{\text{Average Shareholders’ Equity}}$$
    - **Purpose**: Measures return to equity investors.
  - Net Profit Margin: $$\text{Net Profit Margin} = \frac{\text{Net Income}}{\text{Revenue}}$$
    - **Purpose**: % of revenue retained as net income.

- **2.4 Earnings Per Share (EPS)**
  - Basic EPS: $$\text{Basic EPS} = \frac{\text{Net Income} - \text{Preferred Dividends}}{\text{Weighted Average Shares Outstanding (WASO)}}$$
    - **Purpose**: Earnings per common share (excludes preferred dividends).
  - Diluted EPS (Convertible Preferred):
    $$\text{Diluted EPS} = \frac{\text{Net Income}}{\text{WASO} + \text{New Shares from Conversion}}$$
  - Diluted EPS (Convertible Debt):
    $$\text{Diluted EPS} = \frac{\text{Net Income} - \text{Preferred Dividends} + \text{After-Tax Interest Expense}}{\text{WASO} + \text{New Shares from Conversion}}$$
  - Diluted EPS (Options/Warrants – Treasury Stock Method):
    $$\text{Diluted EPS} = \frac{\text{Net Income} - \text{Preferred Dividends}}{\text{WASO} + (\text{Option Shares} - \text{Repurchased Shares})}$$
    - Where: $\text{Repurchased Shares} = \frac{\text{Option Proceeds}}{\text{Average Share Price}}$
    - **Purpose**: Reflects potential dilution from convertible securities/options.


 **Learning Module 3: Analyzing Balance Sheets**
- **3.1 Working Capital**
  - Formula: $$\text{Working Capital} = \text{Current Assets} - \text{Current Liabilities}$$
  - **Purpose**: Measures short-term liquidity.

- **3.2 Liquidity Ratios (Same as Volume 3 Module 3)**
  - Current Ratio, Quick Ratio, Cash Ratio.

- **3.3 Solvency Ratios**
  - Long-Term Debt-to-Equity: $$\frac{\text{Long-Term Debt}}{\text{Total Equity}}$$
    - **Purpose**: Measures long-term leverage (lower = less risk).
  - Debt-to-Equity (D/E): $$\frac{\text{Total Debt}}{\text{Total Equity}}$$
    - **Purpose**: Overall leverage (higher = more financial risk).
  - Debt-to-Asset: $$\frac{\text{Total Debt}}{\text{Total Assets}}$$
    - **Purpose**: % of assets funded by debt.
  - Financial Leverage: $$\frac{\text{Total Assets}}{\text{Total Equity}}$$
    - **Purpose**: Amplifies ROE (higher = more leverage).


 **Learning Module 4: Analyzing Statements of Cash Flows I**
- **4.1 Key Cash Flow Relationships**
  - Accounts Receivable (A/R):
    $$\text{Ending A/R} = \text{Beginning A/R} + \text{Revenue} - \text{Cash Collected from Customers}$$
    - **Purpose**: Derive cash collected (indirect method).
  - Inventory:
    $$\text{Ending Inventory} = \text{Beginning Inventory} + \text{Purchases} - \text{COGS}$$
  - Accounts Payable (A/P):
    $$\text{Ending A/P} = \text{Beginning A/P} + \text{Purchases} - \text{Cash Paid to Suppliers}$$
  - PP&E:
    $$\text{Ending PP&E} = \text{Beginning PP&E} + \text{Equipment Purchased} - \text{Equipment Sold} - \text{Depreciation}$$
  - Gain on Sale of Asset:
    $$\text{Gain on Sale} = \text{Cash from Sale} - \text{Book Value of Asset}$$
    - Where: $\text{Book Value} = \text{Historical Cost} - \text{Accumulated Depreciation}$


 **Learning Module 5: Analyzing Statements of Cash Flows II**
- **5.1 Free Cash Flow to Firm (FCFF)**
  - Formula 1: $$FCFF = \text{NI} + \text{NCC} + \text{Int}(1 - t) - \text{FCInv} - \text{WCInv}$$
  - Formula 2: $$FCFF = \text{CFO} + \text{Int}(1 - t) - \text{FCInv}$$
    - Where:
      - $\text{NI}$ = Net Income, $\text{NCC}$ = Non-Cash Charges (Depreciation),
      - $\text{Int}$ = Interest Expense, $\text{FCInv}$ = Capital Expenditures,
      - $\text{WCInv}$ = Working Capital Investments, $\text{CFO}$ = Cash Flow from Operations
    - **Purpose**: Cash flow available to debt and equity investors.

- **5.2 Free Cash Flow to Equity (FCFE)**
  - Formula: $$FCFE = \text{CFO} - \text{FCInv} + \text{Net Borrowing}$$
    - Where: $\text{Net Borrowing} = \text{Debt Issued} - \text{Debt Repaid}$
    - **Purpose**: Cash flow available to equity investors.

- **5.3 Cash Flow Ratios**
  - Performance Ratios:
    - Cash Flow to Revenue: $$\frac{\text{CFO}}{\text{Revenue}}$$
    - Cash Return on Assets: $$\frac{\text{CFO}}{\text{Average Total Assets}}$$
    - Cash Return on Equity: $$\frac{\text{CFO}}{\text{Average Equity}}$$
    - Cash to Income: $$\frac{\text{CFO}}{\text{Operating Income}}$$ (quality of earnings: >1 = good)
    - Cash Flow per Share: $$\frac{\text{CFO} - \text{Preferred Dividends}}{\text{Common Shares Outstanding}}$$
  - Coverage Ratios:
    - Debt Coverage: $$\frac{\text{CFO}}{\text{Total Debt}}$$
    - Interest Coverage: $$\frac{\text{CFO} + \text{Interest Paid} + \text{Taxes Paid}}{\text{Interest Paid}}$$
    - Dividend Payment: $$\frac{\text{CFO}}{\text{Dividends Paid}}$$ (ability to sustain dividends).


 **Learning Module 6: Analysis of Inventories**
- **6.1 Inventory Valuation Standards**
  - IFRS: $$\text{Inventories} = \text{Lower of Cost and Net Realizable Value (NRV)}$$
    - Where: $\text{NRV} = \text{Estimated Selling Price} - \text{Costs to Complete/Sell}$
  - US GAAP (LIFO/Retail): $$\text{Inventories} = \text{Lower of Cost and Market}$$
    - Where: $\text{Market} = \text{Replacement Cost}$ (bounded by NRV (upper) and NRV - Normal Profit (lower))

- **6.2 Inventory Turnover Metrics**
  - Inventory Turnover: $$\text{Inventory Turnover} = \frac{\text{COGS}}{\text{Average Inventory}}$$
    - **Purpose**: Measures how quickly inventory is sold (higher = more efficient).
  - Days of Inventory on Hand (DOH): $$DOH = \frac{365}{\text{Inventory Turnover}}$$
    - **Purpose**: Days inventory is held (lower = more efficient).

- **6.3 FIFO-LIFO Conversion**
  - FIFO Ending Inventory: $$\text{FIFO Ending Inventory} = \text{LIFO Ending Inventory} + \text{LIFO Reserve}$$
  - FIFO COGS: $$\text{FIFO COGS} = \text{LIFO COGS} - \Delta \text{LIFO Reserve}$$
    - **Purpose**: Compare firms using FIFO vs LIFO (LIFO Reserve adjusts for method difference).


 **Learning Module 7: Analysis of Long-Term Assets**
- **7.1 Book Value and Gain/Loss on Sale**
  - Net Book Value (NBV): $$\text{NBV} = \text{Historical Cost} - \text{Accumulated Depreciation}$$
  - Gain on Sale: $$\text{Gain on Sale} = \text{Sale Proceeds} - \text{NBV}$$
  - Loss on Sale: $$\text{Loss on Sale} = \text{NBV} - \text{Sale Proceeds}$$

- **7.2 Asset Life Estimates**
  - Total Useful Life: $$\text{Total Useful Life} = \frac{\text{Gross PP&E}}{\text{Annual Depreciation Expense}}$$
  - Estimated Age: $$\text{Estimated Age} = \frac{\text{Accumulated Depreciation}}{\text{Annual Depreciation Expense}}$$
  - Remaining Life: $$\text{Remaining Life} = \frac{\text{Net PP&E}}{\text{Annual Depreciation Expense}}$$

- **7.3 Depreciation Methods**
  - Straight-Line (SL): $$\text{Annual Depreciation} = \frac{\text{Cost} - \text{Salvage Value}}{\text{Useful Life}}$$
    - **Purpose**: Equal depreciation each year (simple, widely used).
  - Double-Declining Balance (DDB): $$\text{Depreciation} = \frac{2}{\text{Useful Life}} \times \text{NBV}$$
    - **Purpose**: Accelerated depreciation (higher expense early years).
  - Units-of-Production (UOP): $$\text{Depreciation} = \frac{\text{Units Produced}}{\text{Total Units}} \times (\text{Cost} - \text{Salvage Value})$$
    - **Purpose**: Depreciation based on usage (matches expense to production).

- **7.4 Fixed Asset Turnover**
  - Formula: $$\text{Fixed Asset Turnover} = \frac{\text{Revenue}}{\text{Average Net PP&E}}$$
  - **Purpose**: Measures efficiency of using fixed assets to generate revenue (higher = better).

- **7.5 Asset Impairment**
  - IFRS: $$\text{Impairment Loss} = \text{Carrying Amount} - \text{Recoverable Amount}$$
    - Where: $\text{Recoverable Amount} = \max(\text{Fair Value} - \text{Costs to Sell}, \text{Value in Use})$
  - US GAAP: If $\text{Carrying Amount} > \text{Undiscounted Future Cash Flows}$,
    $$\text{Impairment Loss} = \text{Carrying Amount} - \text{Fair Value}$$
  - **Purpose**: Write down asset if value is permanently impaired.


 **Learning Module 8: Topics in Long-Term Liabilities and Equity**
- **8.1 Lessee Accounting (IFRS Finance Lease)**
  - Interest Expense: $$\text{Interest Expense} = \text{Implied Interest Rate} \times \text{Beginning Lease Liability}$$
  - Principal Payment: $$\text{Principal Payment} = \text{Lease Payment} - \text{Interest Expense}$$
  - Ending Lease Liability: $$\text{Ending Liability} = \text{Beginning Liability} + \text{Interest Expense} - \text{Lease Payment}$$
  - ROU Asset Amortization (SL): $$\text{Amortization} = \frac{\text{Initial ROU Asset} - \text{Salvage Value}}{\text{Lease Term}}$$
  - Ending ROU Asset: $$\text{Ending ROU} = \text{Beginning ROU} - \text{Amortization}$$

- **8.2 Lessee Accounting (US GAAP Operating Lease)**
  - Amortization Expense: $$\text{Amortization Expense} = \text{Lease Payment} - \text{Interest Expense}$$
  - Ending ROU Asset: $$\text{Ending ROU} = \text{Beginning ROU} - \text{Amortization Expense}$$
  - Ending Lease Liability: $$\text{Ending Liability} = \text{Beginning Liability} - \text{Amortization Expense}$$

- **8.3 Stock Options (Compensation Expense)**
  - Formula: $$\text{Compensation Expense} = \frac{\text{Fair Value of Options Granted}}{\text{Vesting Period}}$$
  - **Purpose**: Recognize expense over vesting period (fair value at grant date).


 **Learning Module 9: Analysis of Income Taxes**
- **9.1 Deferred Tax Asset/Liability (DTA/DTL)**
  - For Assets: $$\text{DTA/DTL} = \text{Tax Rate} \times (\text{Carrying Amount} - \text{Tax Base})$$
    - If $\text{Carrying Amount} > \text{Tax Base}$ → DTL (taxable temporary difference).
    - If $\text{Carrying Amount} < \text{Tax Base}$ → DTA (deductible temporary difference).
  - For Liabilities: $$\text{DTA/DTL} = \text{Tax Rate} \times (\text{Tax Base} - \text{Carrying Amount})$$
    - If $\text{Carrying Amount} > \text{Tax Base}$ → DTA (deductible temporary difference).
    - If $\text{Carrying Amount} < \text{Tax Base}$ → DTL (taxable temporary difference).

- **9.2 Income Tax Expense**
  - Formula: $$\text{Income Tax Expense} = \text{Income Tax Payable} + \Delta \text{DTL} - \Delta \text{DTA}$$
  - **Purpose**: Total tax expense (current + deferred).

- **9.3 Effective and Cash Tax Rates**
  - Effective Tax Rate: $$\frac{\text{Income Tax Expense}}{\text{Pretax Income}}$$
    - **Purpose**: Actual tax rate paid (includes deferred taxes).
  - Cash Tax Rate: $$\frac{\text{Cash Paid
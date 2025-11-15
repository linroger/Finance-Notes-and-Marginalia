---
aliases:
- Change-on-Change
- Level-on-Level
- Regression Models
- Bond pricing and yield curves
- Duration and convexity hedging
- Credit spreads and bond valuation
- Fixed income securities and markets
- Bond valuation and yield calculation
- Credit analysis and spread decomposition
- Financial econometrics and regression
- Time series analysis in finance
- Volatility modeling (GARCH)
- Efficient market hypothesis
- Market anomalies and patterns
- Price discovery and information
- Option pricing theory and Black-Scholes model
- Options Greeks and risk management
- Call and put option strategies
- Level Versus Change Regressions and financial analysis
- Level Versus Change Regressions in modern finance
- Applications of Level Versus Change Regressions
- 'Case study: Level Versus Change Regressions'
last_enhanced: '2025-11-06 08:42:36'
- statistical
- bond
- fixed-income
- market-efficiency
- regression
- alpha
- bonds
- options
- delta
- beta
- yield
- call
tags:
- bid-ask
- bond
- case-study
- crisis-analysis
- derivative-pricing
- derivatives
- duration
- econometric
- empirical-analysis
- fixed-income
- graduate-level
- hedging
- institutional-quality
- learning-from-crisis
- market-efficiency
- mathematical-finance
- professional-standard
- provision
- quantitative-analysis
- quantitative-methods
- real-world-example
- sec-regulation
- securitization
- spread
- statistical-model
- stress-test
- volatility
- yield-curve

key_concepts:
- Banking and Financial Intermediation
- Case Study Methodology
- Crisis Case Study Design
- Econometric Analysis
- Empirical Analysis of Financial Events
- Empirical Finance Research
- Financial Crisis Case Studies
- Financial Econometrics
- Financial Markets and Institutions
- Historical Financial Analysis
- Institutional-Quality Financial Education
- Learning from Financial Crises
- Mathematical Finance Applications
- Mathematical Modeling
- Quantitative Analysis in Finance
- Quantitative Methods in Finance
- Quantitative Risk Management
- Real-World Financial Examples
- Risk Management and Hedging Strategies
- Statistical Finance
- Statistical Modeling

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







# 6.3 LEVEL VERSUS CHANGE REGRESSIONS  

When estimating regression-based hedges, most practitioners regress changes in yields on changes in yields, as in the previous sections, but some regress yields on yields. Mathematically, in the single-variable case, the level-on-level regression with dependent variable. $y$ and independent variable $x$ is,  
$$
y_{t}=\alpha+\beta x_{t}+\epsilon_{t}
$$  

while the change-on-change regression is,3  
$$
\begin{array}{c}{{y_{t}-y_{t-1}=\beta(x_{t}-x_{t-1})+\epsilon_{t}-\epsilon_{t-1}}}\ {{\Delta y_{t}=\beta\Delta x_{t}+\Delta\epsilon_{t}}}\end{array}
$$  

If the assumptions of least-squares estimation, mentioned earlier, hold true for the level model (6.22), then they also hold for the change model (6.24), and least-squares estimates from both specifications are unbiased, consistent, and efficient. If, however, the assumption about the independence of the error terms is violated in either specification, then the least-squares estimates from that specification may not be efficient, but they are still unbiased and consistent.  

To discuss the economics behind the assumption that error terms are independent, say that $\alpha=0$ , that $\beta=1$ , and that $y$ and $x$ are the yields of two different bonds. Say further that the yield of the. $x$ -bond is constant at $5\%$ , while the yield of the $y$ -bond was $1\%$ yesterday. The level regression, in Equation (6.22), predicts that the yield of the. $y$ -bond will be. $5\%$ today, despite its having been $1\%$ yesterday. It is more likely, however, that the. yield of the. $y$ -bond today will be closer to $1\%$ than to $5\%$ , and that the.. model error today will be closer to its value yesterday, of. $-4\%$ , than to zero.. In other words, the error terms of the level regression are not likely to be independent of each other, but rather persistent, correlated over time, or serially correlated.  

In this same scenario, because the change in the yield of the $x$ -bond is zero, the change-on-change regression in Equation (6.24) predicts that the change in the yield of the $y$ -bond is zero as well and that its yield remains at $1\%$ . While more plausible than the level-on-level prediction that the yield of the $y$ -bond suddenly jumps to $5\%$ , it is more likely that the yield of the $y$ -bond will gradually trend from its current value of $1\%$ to its model value of $5\%$ . Hence, the error terms in the change-on-change regression are likely to be positive for some time, and, as such, serially correlated.  

This discussion suggests an alternate model, which would capture, in the. scenario just discussed, that the yield of the. $y$ -bond moves gradually from $1\%$ to $5\%$ . In particular, assume the level-on-level model, but with error dynamics,  
$$
\epsilon_{t}=\rho\epsilon_{t-1}+\nu_{t}
$$  

for some $\rho<1$ . In this model, with say, $\rho=75\%$ , yesterday's error of. $-4\%$ would fall, on average, to an error of $75\%$ times $-4\%$ , or $-3\%$ today, thus giving an expected $y$ -bond yield today of. $2\%$ . In this way, the error structure in Equation (6.25) gradually pushes the yield of the $y$ -bond up from its starting point of. $1\%$ to its model value, that is, the $5\%$ yield of the. $x$ -bond. The procedure for estimating (6.22) with the error structure in (6.25) is given in many statistical texts.

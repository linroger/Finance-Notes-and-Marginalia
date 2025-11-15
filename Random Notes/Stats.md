---
tags:
- financial-instruments/irs
- financial-markets/beta
- quantitative-methods/regression
- quantitative-methods/var
- mathematical-finance/continuous
- mathematical-finance/discrete
- mathematics/mean
- mathematics/normal
- educational-level/intermediate
key_concepts:
- value at risk and tail risk measurement
- financial mathematics and quantitative analysis
- derivatives and structured products
- risk management and portfolio optimization
- stochastic processes in finance
- mathematical modeling and simulation
type: note
status: active
academic_level: graduate
professional_application: practical
institutional_standard: true
---

Got it, let's start by understanding the first part: deriving the logistic function from the log-odds. The user's notes show the steps for logit to probability, so let's go through that carefully. Then, we need to cover expected value, variance, and normal distribution properties. Let's break it down.


### Part 1: Simplifying the Logistic Regression Probability (Logit to Probability)
The logit function is defined as the natural log of the odds:  
$$ \log\left( \frac{p}{1-p} \right) = \beta_0 + \beta_1 X_1 + \dots + \beta_n X_n $$  

Let's denote the linear predictor as $\eta = \beta_0 + \beta_1 X_1 + \dots + \beta_n X_n$. So:  
$$ \log\left( \frac{p}{1-p} \right) = \eta $$  

**Step 1: Exponentiate both sides** to eliminate the log:  
$$ \frac{p}{1-p} = e^\eta $$  

**Step 2: Solve for $p$**. Multiply both sides by $(1-p)$:  
$$ p = e^\eta (1 - p) $$  

**Step 3: Expand the right-hand side**  
$$ p = e^\eta - p e^\eta $$  

**Step 4: Collect terms with $p$** on the left:  
$$ p + p e^\eta = e^\eta $$  

**Step 5: Factor out $p$** on the left:  
$$ p(1 + e^\eta) = e^\eta $$  

**Step 6: Divide both sides by $(1 + e^\eta)$** to solve for $p$:  
$$ p = \frac{e^\eta}{1 + e^\eta} $$  

We can also write this as:  
$$ p = \frac{1}{1 + e^{-\eta}} $$  
(by dividing numerator and denominator by $e^\eta$: $\frac{e^\eta}{1 + e^\eta} = \frac{1}{e^{-\eta} + 1} = \frac{1}{1 + e^{-\eta}}$)  


### Part 2: Expected Value (Mean) - Mathematical Properties
The **expected value** (or mean) of a random variable $X$ is a measure of central tendency. Let's define it for discrete and continuous cases.  

#### Discrete Random Variable  
If $X$ is discrete with possible values $x_1, x_2, \dots, x_k$ and probabilities $P(X = x_i) = p_i$, then:  
$$ \mathbb{E}[X] = \sum_{i=1}^k x_i p_i $$  

#### Continuous Random Variable  
If $X$ is continuous with probability density function (pdf) $f(x)$, then:  
$$ \mathbb{E}[X] = \int_{-\infty}^{\infty} x f(x) \, dx $$  

**Key Properties of Expected Value**:  
1. **Linearity**: For constants $a, b$ 
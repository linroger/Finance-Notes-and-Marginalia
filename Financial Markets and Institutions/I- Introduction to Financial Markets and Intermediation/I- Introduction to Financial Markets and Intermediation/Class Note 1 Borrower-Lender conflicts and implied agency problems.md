---
aliases:
- Borrower-Lender Conflicts
- Debt and Incentives
- Asset Substitution Theory
cssclasses: academia
key_concepts:
- Bond pricing and fixed income securities valuation
- Ito's lemma and stochastic calculus applications
- Credit risk modeling and default probability estimation
- Credit default swaps and counterparty risk analysis
- Interest rate swaps and term structure modeling
- Interest rate caps, floors, and swaptions
tags:
- bonds
- correlation
- credit-risk
- fixed_income
title: Class Note 1 Borrower-Lender Conflicts and Implied Agency Problems
---


# Class Note 1 Borrower-Lender Conflicts and Implied Agency Problems

The amount of leverage has an impact on the incentives of someone who maximizes the value of the residual equity claim. This "asset substitution theory" is a popular theory of capital structure, but it is not too plausible for large firms. It makes the most sense for owner-managed firms, where the manager is the stockholder. If the owner and manager differ, one needs to examine the manager's incentive contract to learn his/her incentives. We will see later that the owner's and manager's incentives are naturally aligned for nearly insolvent firms and for some financial institutions that have government deposit insurance.

The example illustrates how divided ownership of different parts of the cash flow distribution distorts capital budgeting decisions.

Debt holders own the lower tail of the distribution of firm value, and equity owners the upper tail. This is the cause of the conflict of interest because some decisions hurt the lower tail and help the upper tail (and can help or hurt the overall value of the firm).

## 1. No debt

Two projects, the riskier one also has a lower expected return. Each has only two possible outcomes, one if a depression (D), one if prosperity (P). The probability of each outcome is 1/2. Each project requires the an initial outlay of $800.

 | Project | Value in D | Value in P | Expected Value | Expected Return | 
 | --------- | ------------ | ------------ | ---------------- | ----------------- | 
 | 1 | 500 | 1500 | 1000 | $\frac{200}{800} = 25\%$ | 
 | 2 | 0 | 1551 | 775.5 | $\frac{-24.5}{800} = -3.06\%$ | 

We could get fancy and use the states model to take account of the positive "beta" of each project (each pays off more in prosperity). Project 2 has a higher beta, implying that it should require a higher discount rate than project 1. It is sufficient for our purposes to use the expected returns to see the incentive problem with debt.

Clearly, project 1 is the best investment. An owner-managed firm with no debt would select it, since all require the same initial outlay.

## 2. What about a firm with debt with face $600 in place?

The fixed payment of $600 is a sunk cost. If the firm is going to default, then it does not care "how big" the default is. It wants to make more when not in default.

### Cash flows to equity when debt of $600 is in place

 | Project | Cash Flow if D | Cash Flow if P (Debt = 600) | Expected Value | 
 | --------- | ---------------- | --------------------------- | ---------------- | 
 | 1 | 0 | 1500 - 600 = 900 | 450 | 
 | 2 | 0 | 1551 - 600 = 951 | 475.5 | 

The levered firm would select project number 2, despite its lower net present value, because it has a higher present value conditional on not leading to bankruptcy. The equity owner owns the upper tail, and is only concerned with the returns he owns. Note that no matter how the equity owner values the cash flows if P, he prefers project 2 since both have identical cash flows if D and project 2 has higher payments if P.

This does not mean that firms "want" to go bankrupt. Instead, it is a statement about debt capacity. If the debt face value gets too high, then these perverse incentive effects of debt increase. This can lead the firm to tilt its decisions toward excessively risky projects, with a lower net present value. Potential bond holders can put themselves into the owner's shoes, and take this into account when deciding what interest rate to charge on the bond. The lender can predict what the borrower will do, but there is a problem because the lender cannot directly observe the project choice.

## Debt Capacity Calculation

What is the debt capacity of the firm? What is the highest face value, F, that the borrower prefers project 1?

The borrower's equity payoff from Project 1 with debt of face F is:
- $\frac{1}{2}(500-F) + \frac{1}{2}(1500-F) = 1000-F$ (for F ≤ 500)
- $\frac{1}{2}(0) + \frac{1}{2}(1500-F) = 750-F/2$ (for F between 500 and 1500)
- 0 (for F > 1500)

The borrower's equity payoff from Project 2 with debt of face F is:
- $\frac{1}{2}(0) + \frac{1}{2}(1551-F) = 775.5-F/2$ (for F < 1551)
- 0 (for F ≥ 1551)

The debt capacity must be less than 500, because if the firm will certainly default in Depression, all that matters is what it is worth in Prosperity.

For F ≤ 500, Project 1 is preferred for all F that satisfy $1000-F > 775.5-F/2$, which solves out to F < 449. As a result, 449 is the debt capacity in face value.

Suppose lenders require an expected return of r for investing in any security of the firm. If the firm issued debt with face value 448 debt, it would choose project 1, and then the debt could raise up to $\frac{448}{1+r}$. (Project 1 is also selected for face 449, because the borrower will not hurt the lender if it does not help himself.) If the firm issued debt with face 449.5, it would lead to project 2 and raise $\frac{0.5 \times 449.5}{1+r}$.

Risky debt (debt with a positive probability of bankruptcy) distorts capital budgeting decisions. It provides incentives to make tradeoffs between cash in bankruptcy and not in bankruptcy that differ from the ones that maximize the value of the firm.

The potential bond holders will require a high enough interest rate to give themselves a competitive rate of return, for example r. Thus, any reductions in the value of the capital budgeting program of the firm will come out of the owner's pockets. If the firm selected too high a leverage ratio, it would be giving itself a perverse incentive contract. It would not do this in the first place, if it had alternatives. Thus, we might not expect a firm to choose a capital structure with as much debt as our example if it faced an unobservable choice between these projects.

## Unanswered Questions

This leaves us with some unanswered questions:
A. How can these bad effects of debt be reduced?
B. How do bank asset services help reduce these bad effects?
C. If debt is so bad, why is it so common, especially for smaller firms? Why not use another financial contract?

### Question A: Reducing Bad Effects of Debt

Beginning with question A, we examine problems with bond covenants, contractual provisions in bond or loan indentures. See the Wruck paper in the packet for a description of typical covenants.

- Just prohibiting an action in a bond covenant does not prevent it from happening. The lender needs to know about the violation before it happens or soon thereafter. In addition, the lender must have some bargaining power over the borrower in order to stop a "crime in progress."

- Enforcement requires effort and monitoring of the borrower. Without substantial monitoring, the contract cannot depend on anything except the grossest public information.

- If not all contingencies are spelled out, contracts must be renegotiated over time. This too requires the lender to have lots of information about the borrower's situation.

- If the lender is not one individual, but many small bond holders, the bond covenants can be difficult to enforce. There can be either duplication of effort if each lender monitors the situation carefully, or more likely, a "free rider" problem, where none of the small bond holders find it worthwhile to bother to monitor. Without monitoring, covenants will not be renegotiated or contain much detail. If there is no monitoring, covenants will be written contingent only on the grossest public information.

- This gives an advantage to having a single lender, rather than many lenders. We will see that this is a part of the argument why asset services of banks and other intermediaries are important.

- The US Federal Trust Indenture Act prohibits majority voting to restructure debt contracts that reduce principal or interest or extend the debt maturity. A 100% vote required to change these "key covenants." Thus, even if public bond holders had the information, they probably could not use it. Changes to other covenants in bonds require a 2/3 vote in dollar value, and 50% measured in the fraction of bond holders (not weighted by dollar value).

## Key Takeaways

- Debt can distort capital budgeting decisions and provide perverse incentives to the firm
- Risky debt provides an advantage to the lender, but can lead to monitoring problems
- Bond covenants may not be effective in preventing bad behavior by the borrower if they are not enforceable or contain too little detail
- Asset services of banks and other intermediaries are important because they provide a single point of contact for borrowers and lenders, making it easier to monitor and enforce contracts
- Debt may be common for smaller firms because they have limited access to capital markets or face higher costs of borrowing

---
cssclasses:
- academia
title: 'Class Note 4: Restructuring Debt Outside Bankruptcy'
tags:
- banking-regulation
- basel-accord
- binomial-model
- black-scholes-model
- capital-adequacy
- caplet
- cds
- coherent-risk-measure
- conditional-var
- continuous-time-pricing
- convexity-adjustment
- counterparty-risk
- credit-default-swap
- credit-derivatives
- credit-modeling
aliases:
- Bank Debt
- Class Note 4
- Restructuring Outside Bankruptcy
- Debt Renegotiation
key_concepts:
- Black-Scholes option pricing model and continuous-time finance
- Options Greeks and sensitivity analysis for risk management
- Duration analysis and interest rate risk management
- Convexity adjustments and yield curve sensitivity
- Credit default swaps (CDS) and credit risk modeling
- Value at Risk (VaR) and tail risk measurement
- Expected shortfall and coherent risk measures
- Basel accords and banking regulation framework
- Risk preference theory and utility functions
type: note
status: active
academic_level: graduate
professional_application: theoretical
---



# Class Note 4: Restructuring Debt Outside Bankruptcy

**Course:** Financial Markets and Institutions
**Professor:** Douglas W. Diamond
**Class Note 4:** Restructuring Debt Outside Bankruptcy

We have seen that because public bondholders cannot make informed concessions outside bankruptcy, a structure of all public debt will get into bankruptcy court too often. The reasons are the individual bondholders' lack of information and the U.S. Federal trust indenture act. In practice,  there is almost never a successful vote on these issues on public bond issues in the United States.

All private placement debt with a single lender would avoid this problem. However, the single bank lender solution is sometimes too expensive because of bank operating costs and reserve requirement type taxes on intermediation. In addition, for large borrowers, the single bank lender solution cannot be used because individual banks have a lending limit of 100% (or less) of their capital to a single borrower.

Further, with only one lender, that lender may have too much power, from the borrower's point of view. In practice, large borrowers have both public and bank debt. We now examine how the inability to renegotiate public debt outside bankruptcy influences the bankruptcy decision for borrowers with public and bank debt. There are two lenders: one bank,  one public.

## 1. No Public Debt Concessions At All

The easiest case is when the public can never make a concession. This implies the use of bankruptcy court and possibly liquidation whenever there is a default. The only party who can make concessions outside bankruptcy is the bank lender. In practice, the bank loans are short term and senior, the public is long term and junior to the bank. Later in the course, we will examine why this is the structure that is commonly used. For now, we will just look at the structure's implications for restructuring debt outside bankruptcy. If the public never makes a concession, the bank decides whether to make a concession of its own to stay out of bankruptcy, or instead to force the borrower into bankruptcy. If the bank forces bankruptcy, then it is paid from the bankruptcy proceeds by its specified priority (it is senior). The bank debt is maturing today and needs to be refinanced. The public debt is long-term, and matures in the future.

The future ("date 2") value of the firm is 2,  1,  or 0,  with probability $q_2$,  $q_1$,  and $q_0$ respectively. The current going concern value of the firm is then $2q_2 + q_1$.
Let $q_2=0.2$,  $q_1=0.6$,  and $q_0=0.2$. The going concern value $V_{GO}$ is:
$$V_{GO} = 2(0.2) + 0.6(1) = 1.0$$

If the firm gets into bankruptcy court, some going-concern value is destroyed. Let $L$ be the value if the firm gets into bankruptcy. This can be interpreted as the value that the firm will sell for if liquidated, or the value under current management net of direct and indirect costs of bankruptcy.

The face value of maturing bank debt is $B$, and the face value of public debt (which matures in the future, on date 2) is $P$.

## Example 1: Going Concern Value May Be Lost

Let the value in bankruptcy be $L = 0.4$ (this example holds for all $L$ exceeding 0.26).

The going concern value, $V_{GO}$, is 1, but this can be achieved only if the bank does not force bankruptcy now. There are *two ways the firm can avoid bankruptcy*: it can fully repay the bank, or it can convince the bank to make a concession.

- The bank is owed $B = 0.3$,  and the loan matures today.
- The public is owed $P = 1.6$,  maturing on date 2.
- There is no current interest payment owed to the public (it has already been paid).

If the firm gets into bankruptcy court, the firm will be worth only $L = 0.4$. The difference $V_{GO} - L = 1 - 0.4 = 0.6$ is the going concern value at risk if no agreement can be reached outside bankruptcy.

- Suppose that the bank extends the maturity of its loan to date 2 and keeps the face value equal to $0.3$.
  - It is senior and gets paid $0.3$ when the firm is worth $1$ or $2$.
  - Therefore,  it will get $0.3$ with a probability of $0.8$,  and the claim is worth $0.8(0.3) = 0.24$.

However,  the bank would not accept this because it can get paid in full by forcing bankruptcy (it is senior,  and $L$ exceeds $B$). There is a third option: to extend maturity and increase the face value of the debt (increase the interest rate). However,  the existence of the public debt limits how much the bank can obtain by increasing the face value. The public debt has a covenant that prohibits issuing future debt that is senior to it (sometimes called a "me first" rule). Although the bank debt is senior to the public debt,  the me first rule limits the part of the future cash that can go to the bank.

- The bank has a senior claim of $B = 0.3$,  and the public has a claim on $P = 1.6$.
- Any new claims that the borrower issues (to the bank or to other lenders) must be junior to the public.
  - This implies that the most the bank can receive from the borrower at date 2 is $0.4$.
  - It can get $0.3$ by extending the maturity of the senior claim that it already has.
  - Any other claim would be junior to the public.

The public's claim of $1.6$,  plus the bank's senior claim of $0.3$,  adds up to $1.9$. The maximum value of the firm is $2$,  implying that at most an additional $2 - 1.9 = 0.1$ can be paid to the bank. This $0.1$,  plus the $0.3$ senior claim,  adds up to $0.4$.

If the bank took this junior claim on $0.1$ in addition to its senior claim on $0.3$,  its payoff would be as follows:

- If the firm is worth $1$,  it would get $0.3$ (because its junior claim would be worthless).
- If the firm is worth $2$,  it would get $0.4$. The expected value of its claim is then:
$$0.2(0.4) + 0.6(0.3) = 0.26$$

Because the bank can get $B = 0.3$ (which is more than $0.26$) from forcing bankruptcy,  it will force bankruptcy and destroy the going concern value.

The public can make no concessions. Therefore,  the public cannot prevent the bank from forcing bankruptcy,  and the going concern value will be destroyed.

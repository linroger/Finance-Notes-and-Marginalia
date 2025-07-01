---
cssclasses: academia
linter-yaml-title-alias: Lecture Slides 1 - Debt Contracts
title: Lecture Slides 1 - Debt Contracts
tags:
  - bank_runs
  - bankruptcy
  - capital_structure
  - debt_contracts
  - financial_crisis
  - liquidity
  - securitization
  - debt_pricing
  - agency_costs
  - trust_indenture_act
aliases:
  - Debt Contracts
  - Debt and Bankruptcy
  - Debt and Liquidity
  - Lecture 1
  - Strategic Effects of Debt Slides
key_concepts:
  - Bailouts and government crises
  - Banks and financial engineering
  - Capital structure choice
  - Debt contracts and bankruptcy
  - Financial panics and debt
  - Liquidity in markets
  - Securitization structures
  - Strategic effects of debt
  - Trust Indenture Act restrictions
  - Debt capacity calculations
---

# Lecture Slides 1 - Debt Contracts

## 1. The Details of Debt Contracts and Bankruptcy

- Strategic effects of debt. How much is too much?
- Bankruptcy & Reorganization: bargaining and strategy
- Debt contract renegotiation
- Debt Exchange Offers when bankruptcy is the alternative
- Primer on Distressed Investing (especially during a financial crisis)
- Capital structure is more than debt versus equity: it is a choice of source of funds: who holds and enforces the terms of securities that a firm issues

## 2. How the Problems and Benefits of Debt Contracts are Related to Banking

- Banks as the original form of "financial engineering." Pooling and Tranching

## 3. Securitization Structures

- The structure of some securitizations and why they are that way

## 4. Liquidity (What Is It?)

- Liquidity provided by markets
- Liquidity provided by institutions
- How are banks and financial panics related to liquidity?

## 5. Panics and Meltdowns (Their Relation to Debt and to Liquidity)

- Bank runs (US and other, in history)
- The Asian Debt Crisis
- Long-Term Capital Management (one possible explanation)
- Subprime and securitization panic (2007-2008)
- Restructuring financial institutions out of bankruptcy (CIT finance company)
- 1980s run on Continental Bank. Similarities to SVB run in 2023
- Runs on Money Market Funds
- Runs on Stable Coins (Terra and Luna) in 2022

## 6. Bailouts and the Role of Government in Crises

- 1980s run on Continental Bank. Similarities to SVB run in 2023
- Bear Sterns, Lehman Brothers and the Federal Reserve (if time)
- COVID-19 (if time)

!500
!500
!500
US versus OECD Countries, external funds Non-financial businesses, 1970-85

## F Nonfinancial Corporate Business

Billions of dollars; quarterly figures are seasonally adjusted annual rates

!500

!500

## Introduction to Topic 1: Capital Structure and the Choice of the Sources of Funds

What are the consequences of capital structure choice? What might change?

- Probability of default
- Payoffs to equity
- Payoffs to manager (possibly if tied to debt or equity)
- Tax Payments
- Control over corporate decisions

Does it matter who owns a firm's debt or equity?
- The public: small diffuse holders
- Large individual investors
- Large institutional investors = Financial Intermediaries
- Other publicly-held firms (Suppliers, customers, etc.)

We begin with the simplest case: owner managed firms issuing debt (bonds) to outside small "public" holders. In practice, it is rare for owner-managed firms to issue bonds directly. This will be Class Note 1.

!7_image_0.png

Business 35202 slides. From Class Note 1. Douglas W Diamond

## 1. No Debt

Two projects, the riskier one also has a lower expected return. Each has only two possible outcomes, one if a depression (D), one if prosperity (P). The probability of each outcome is ½. Each project requires an initial outlay of $800.

 | Project | Value in D | Value in P | Expected value | Expected return | 
 | --------- | ----------- | ----------- | ---------------- | ----------------- | 
 | 1 | 500 | 1500 | 1000 | 200/800 = 25% | 
 | 2 | 0 | 1551 | 775.5 | -24.5/800 = -3.06% | 

An unlevered firm will choose Project 1

## 2. What About a Firm With Debt With Face $600 in Place?

The fixed payment of $600 is a sunk cost. If the firm is going to default, then it does not care "how big" the default is. It wants to make more when not in default. Equity gets the residual claim in excess of 600, or zero if the firm value is less than 600.

### Contingent Cash Flows to Equity When Debt of $600 is in Place

 | Project | Value if D | Value if P | Expected Value | 
 | --------- | ----------- | ---------------- | ---------------- | 
 | 1 | 0 | 1500-600 = 900 | 450 | 
 | 2 | 0 | 1551-600 = 951 | 475.5 | 

An owner-managed firm with debt of 600 in place will choose project 2, despite its negative net present value, because the "piece of the action" that goes to the equity is worth more than with project 1. Face value of 600 exceeds the debt capacity of the firm, because it removes incentives for proper investment.

### What is the Debt Capacity of the Firm?

What is the highest face value, F, that the borrower prefers project 1?

The borrower's equity payoff from Project 1 with debt of face F is:

½(1500-F) + ½(500-F) = 1000 - F (for F≤500)

½(1500-F) + ½(0) (for F between 500 and 1500), 0 for F>1500.

The borrower's equity payoff from Project 2 with debt of face F is:

½(1551 - F) + ½(0) for F<1551
0 for F> 1551.

The debt capacity must be less than 500, because if the firm will certainly default in Depression, all that matters is what it is worth in prosperity.

For F < 500, Project 1 is preferred for all F that satisfy 1000-F ≥ ½(1551-F), which solves out to F≤ 449. As a result, 449 is the debt capacity in face value.

## Debt Pricing

Suppose lenders require an expected return of r for investing in any security of the firm. If the firm issued debt with face value 448 debt, it would choose project 1, and then the debt could raise up to $\frac{448}{1+r}$. (Project 1 is also selected for face 449, because the borrower will not hurt the lender if it does not help himself.) If the firm issued debt with face F>449, it would lead to project 2 and raise $\frac{½F + ½(0)}{1+r}$.

## This Leaves Us With Some Unanswered Questions

A- *How can these bad effects of debt be reduced?*
B- *How do bank asset services help reduce these bad effects?*

Next Class

C- If debt is so bad, why is it so common, especially for smaller firms?

Why not use another financial contract?

Next Class

A. Let's have some suggestions for how to get out of this situation of Risky Project 2?

- We will discuss and evaluate.

## The US Federal Trust Indenture Act

- The US Federal Trust Indenture Act prohibits majority voting to restructure debt contracts that reduce principal, interest or extend the debt maturity.
- A 100% vote required to change these "key covenants."
- Thus, even if public bondholders had the information, they probably could not use it.
- Changes to other covenants in bonds require a 2/3 vote in dollar value, and 50% measured in the fraction of bondholders (not weighted by dollar value).

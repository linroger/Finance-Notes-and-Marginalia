---
aliases:
- Financial Institutions Lecture Notes
- Financial Markets Lecture Notes
- Markets and Institutions Notes
cssclasses: academia
enhanced: true
enhancement_date: '2025-11-06'
key_concepts:
- Risk-neutral measures and martingale pricing
- Bond pricing and fixed income securities valuation
- Ito's lemma and stochastic calculus applications
- Credit risk modeling and default probability estimation
- Interest rate caps, floors, and swaptions
- Arbitrage opportunities and no-arbitrage pricing
tags:
- arbitrage
- correlation
- credit-risk
- martingale
- no-arbitrage
- risk-management
- risk-neutral
title: Financial Markets and Institutions Lecture Notes
---


# Financial Markets and Institutions Lecture Notes

# Borrower-Lender conflicts and implied agency problems

The amount of leverage has an impact on the incentives of someone who maximizes the value of the residual equity claim. This "asset substitution theory" is a popular theory of capital structure, but it is not too plausible for large firms. It makes the most sense for owner managed firms, where the manager is the stockholder. If the owner and manager differ, one needs to examine the manager's incentive contract to learn his/her incentives. We will see later that the owner's and manager's incentives are naturally aligned for nearly insolvent firms and for some financial institutions that have government deposit insurance.

The example illustrates how divided ownership of different parts of the cash flow distribution distorts capital budgeting decisions.

Debt holders own the lower tail of the distribution of firm value, and equity owners the upper tail. This is the cause of the conflict of interest because some decisions hurt the lower tail and help the upper tail (and can help or hurt the overall value of the firm).

# 1. No debt

Two projects, the riskier one also has a lower expected return. Each has only two possible outcomes, one if a depression (D), one if prosperity (P). The probability of each outcome is 1/2. Each project requires the an initial outlay of 300.

!Pasted image 20241125205607.png]]

We could get fancy and use the states model to take account of the positive "beta" of each project (each pays off more in prosperity). Project 2 has a higher beta, implying that it should require a higher discount rate than project 1. It is sufficient for our purposes to use the expected returns to see the incentive problem with debt.

Clearly, project 1 is the best investment. An owner-managed firm with no debt would select it, since all require the same initial outlay.

# 2. What about a firm with debt with face 600 in place?

The fixed payment of 600 is a sunk cost. If the firm is going to default, then it does not care "how big" the default is. It wants to make more when not in default.

# Cash flows to equity when debt of 600 is in place

!Pasted image 20241125205633.png]]

The levered firm would select project number 2, despite its lower net present value, because it has a higher present value conditional on not leading to bankruptcy. The equity owner owns the upper tail, and is only concerned with the returns he owns. Note that no matter how the equity owner values the cash flows if P, he prefers project 2 since both have identical cash flows if D and project 2 has higher payments if P.

This does not mean that firms "want" to go bankrupt. Instead, it is a statement about debt capacity. If the debt face value gets too high, then these perverse incentive effects of debt increase. This can lead the firm to tilt its decisions toward excessively risky projects, with a lower net present value. Potential bond holders can put themselves into the owner's shoes, and take this into account when deciding what interest rate to charge on the bond. The lender can predict what the borrower will do, but there is a problem because the lender cannot directly observe the project choice.

What is the debt capacity of the firm? What is the highest face value, F, that the borrower prefers project 1?

The borrower's equity payoff from Project 1 with debt of face F is:

$\frac{1}{2}(500-F) + \frac{1}{2}(1500-F) = 1000-F$ (for F ≤ 500)

$\frac{1}{2}(0) + \frac{1}{2}(1500-F) = 750-F/2$ (for F between 500 and 1500), 0 for F > 1500.

# The borrower's equity payoff from Project 2 with debt of face F is

$\frac{1}{2}(0) + \frac{1}{2}(1551-F) = 775.5-F/2$ (for F < 1551) 0 (for F ≥ 1551)

The debt capacity must be less than 500, because if the firm will certainly default in Depression, all that matters is what it is worth in Prosperity.

For F ≤ 500, Project 1 is preferred for all F that satisfy 1000-F > 775.5-F/2, which solves out to F < 449. As a result, 449 is the debt capacity in face value.

Suppose lenders require an expected return of r for investing in any security of the firm. If the firm issued debt with face value 448 debt, it would choose project 1, and then the debt could raise up to $\frac{448}{1+r}$. (Project 1 is also selected for face 449, because the borrower will not hurt the lender if it does not help himself.) If the firm issued debt with face 449.5, it would lead to project 2 and raise $\frac{0.5*449.5}{1+r}$.

Risky debt (debt with a positive probability of bankruptcy) distorts capital budgeting decisions. It provides incentives to make tradeoffs between cash in bankruptcy and not in bankruptcy that differ from the ones that maximize the value of the firm.

The potential bond holders will require a high enough interest rate to give themselves a competitive rate of return, for example r. Thus, any reductions in the value of the capital budgeting program of the firm will come out of the owner's pockets. If the firm selected too high a leverage ratio, it would be giving itself a perverse incentive contract. It would not do this in the first place, if it had alternatives. Thus, we might not expect a firm to choose a capital structure with as much debt as our example if it faced an unobservable choice between these projects.

This leaves us with some unanswered questions: AHow can these bad effects of debt be reduced? BHow do bank asset services help reduce these bad effects? CIf debt is so bad, why is it so common, especially for smaller firms? Why not use another financial contract?

Beginning with question a, we examine problems with bond covenants, contractual provisions in bond or loan indentures. See the Wruck paper in the packet for a description of typical covenants.

-Just prohibiting an action in a bond covenant does not prevent it from happening. The lender needs to know about the violation before it happens or soon thereafter. In addition, the lender must have some bargaining power over the borrower in order to stop a "crime in progress."

-Enforcement requires effort and monitoring of the borrower. Without substantial monitoring, the contract cannot depend on anything except the grossest public information.

-If not all contingencies are spelled out, contracts must be renegotiated over time. This too requires the lender to have lots of information about the borrower's situation.

-If the lender is not one individual, but many small bond holders, the bond covenants can be difficult to enforce. There can be either duplication of effort if each lender monitors the situation carefully, or more likely, a "free rider" problem, where none of the small bond holders find it worthwhile to bother to monitor. Without monitoring, covenants will not be renegotiated or contain much detail. If there is no monitoring, covenants will be written contingent only on the grossest public information.

-This gives an advantage to having a single lender, rather than many lenders. We will see that this is a part of the argument why asset services of banks and other intermediaries are important.

-The US Federal Trust Indenture Act prohibits majority voting to restructure debt contracts that reduce principal or interest or extend the debt maturity. A 100% vote required to change these "key covenants." Thus, even if public bond holders had the information, they probably could not use it. Changes to other covenants in bonds require a 2/3 vote in dollar value, and 50% measured in the fraction of bond holders (not weighted by dollar value).

# University of Chicago Chicago Booth School of Business

# Class Note 2

# Debt contracts due to the lack of information: Debt as a promise and a threat

This is our initial view of the role of debt in corporate control. This is simple but abstract. This will not be our only view of this issue.

Consider a borrower who needs to raise a large quantity of capital. All lenders and borrowers are risk neutral. The borrower has no capital and needs to raise 1 ($1 million).

Outside investors do not observe the borrower's operations directly, not even its sales or cash flows. How can the lenders write a contract where they do not need to monitor this information?

Contract: The entrepreneur promises to pay 1 at time 1. If not, the borrower hands over the assets to the lender(s).

It is costly for the lender to take over the assets. In liquidation, the assets are worth 0.5. The entrepreneur is managing the firm. He/she decides what cash flows to show, but is limited by the threat of liquidation if he/she does not pay what is promised.

Time lines:
  time =                 0              1

Lender gives 1
Entrepreneur starts business      
                                  Lender is repaid 1

# CASE 1

Entrepreneur observes cash flows. Will not show more than 1 to lender (since showing more means giving more), so shows 1 if cash flows ≥ 1, or all if less than 1.

Lender liquidates if cash < 1 is observed. Therefore, lender's payoff is: = min(CF,1)with probability 1/2
                                                  = 0.5 with probability 1/2

The lender's expected payoff is 3/4, so the lender loses money on the loan.

The entrepreneur has expected payoff 1 - 3/4 = 1/4. This is positive, so the borrower wants to do the project.

This case is not feasible since the lender will not provide the funds.

# CASE 2

Suppose the business payoffs were better (perhaps the entrepreneur is different). In this case, the probability of low cash flows is 1/3 and the probability of high cash flows is 2/3.

Lender's expected payoff = 1/3(0.5) + 2/3(1) = 5/6

Entrepreneur's expected payoff = 1/3(0) + 2/3(1) = 2/3

The interest rate on the loan is (1 - 5/6)/(5/6) = 1/5 = 20%. This is quite high given that the lender and borrower do not care about risk. The reason for the high rate is that the financing involves deadweight liquidation expenses. This loan is feasible since both parties make money.

Neither case involves financial intermediation.

# CASE 3

Consider the case where the borrower's project requires a initial investment of size 1. The borrower has wealth A < 1. In addition, suppose the project has discrete payoffs of either 0 or X with equal probability. If the borrower raises outside capital from a bond issue, the debt holders will require a rate of return of r > 0. Let I be the amount of money raised from bond holders where I + A = 1. The face value of debt is F = I(1+r).

Case 3a: F < X. The bond is riskless.
Case 3b: F > X. The bond is risky and bankruptcy occurs in state 0.

In case 3a, the borrower has equity payoffs: 0 and X - F. His expected return is:

E(Return) = 1/2(0) + 1/2(X-F) - A = X/2 - F/2 - A

Substituting for F:

E(Return) = X/2 - (1-A)(1+r)/2 - A = X/2 - (1+r)/2 + rA/2

For E(Return) > 0, we need: X > 1+r, i.e., project's return exceeds required return.

In case 3b, with risky debt, the debt holders require compensation for default risk. Their expected payoff is 1/2(0) + 1/2(X) = X/2. They lend I and require F such that:

X/2 = I(1+r) = (1-A)(1+r)

This gives: X = 2(1-A)(1+r)

For the project to be feasible: X > 2(1-A)(1+r)

Key insight: With information asymmetry, debt contracts can be optimal even with deadweight costs, as they minimize the need for costly state verification.

# Class Note 3

# Financial Intermediation and Delegated Loan Monitoring: Bank Asset Services

Banks and other financial institutions provide services on both sides of their balance sheet. We begin by describing services provided on the asset side.

Asset-side services include:
- Monitoring borrowers 
- Renegotiating contracts when needed
- Enforcing covenants
- Managing collateral
- Screening new borrowers

Banks act as delegated monitors on behalf of many small depositors/investors. This avoids duplication of monitoring costs and solves the free-rider problem inherent in public debt markets.

The Diamond (1984) model shows how banks can credibly commit to monitor borrowers on behalf of depositors:

[^1]: Bank invests depositors' funds in many loans
[^2]: Bank monitors each borrower at cost K per loan
[^3]: If bank doesn't monitor, borrowers misbehave and loans default
[^4]: Bank promises depositors a fixed return
[^5]: Bank's own capital provides incentive to monitor

Key insight: Diversification across many loans makes bank's promise to depositors credible, as monitoring becomes necessary for bank survival.

# Class Note 4

# Debt Restructuring Outside Bankruptcy

When a firm faces financial distress but wants to avoid bankruptcy, it may attempt to restructure its debt outside of court. This involves negotiating with creditors to:

- Reduce principal amounts
- Lower interest rates  
- Extend maturity dates
- Exchange debt for equity

## Exchange Offers

Public debt can be restructured through exchange offers, where the firm offers to exchange existing bonds for new securities with different terms. Key features:

[^1]: Voluntary participation - bondholders choose whether to tender
[^2]: Often involves exchanging debt for combination of:
   - New debt with lower face value
   - Equity in the restructured firm
   - Cash payment
   - Warrants or other securities

## Hold-out Problem

The main challenge in voluntary restructurings is the hold-out problem:

- Each bondholder has incentive to refuse the exchange
- Hold-outs hope to get paid in full while others take losses
- Can lead to failure of the restructuring attempt

## Solutions to Hold-out Problem

[^1]: **Exit Consents**: Bondholders who tender also vote to strip covenants from remaining bonds
[^2]: **Minimum Participation Requirements**: Exchange only proceeds if high percentage tender
[^3]: **Prepackaged Bankruptcy**: Negotiate terms outside court, then file for quick bankruptcy
[^4]: **Credible Bankruptcy Threat**: Make clear that failure leads to Chapter 11

Example: In the 1980s-1990s, many leveraged buyouts required debt restructurings. Firms like RJR Nabisco successfully used exchange offers to reduce debt burdens.

## Legal Constraints

The Trust Indenture Act restricts modifications to payment terms outside bankruptcy:

- Cannot reduce principal or interest without unanimous consent
- Cannot extend maturity without unanimous consent  
- Other covenant changes require lower thresholds (typically 2/3 by value)

This makes out-of-court restructurings more difficult for public debt compared to bank debt.

# Class Note 5

# Private Information, Liquidity, and Securitization 

Markets can fail to provide liquidity when there is significant private information. The Akerlof "lemons" problem illustrates how adverse selection can cause market breakdown.

## Bid-Ask Spreads with Private Information

When some traders have private information, market makers must protect themselves by widening bid-ask spreads. The Glosten-Milgrom model shows:

[^1]: Market makers face informed and uninformed traders
[^2]: Informed traders only trade when prices are favorable to them
[^3]: Market makers lose money to informed traders
[^4]: Spreads must be wide enough to compensate for these losses

The bid price B and ask price A satisfy:

B = E[V | Sell order]
A = E[V | Buy order]

Where V is the true asset value. The spread A - B increases with:
- Probability of informed trading
- Degree of information asymmetry
- Volatility of the asset

## Securitization as a Solution

Securitization can reduce information problems by:

[^1]: Creating senior tranches that are information-insensitive
[^2]: Concentrating information sensitivity in junior tranches
[^3]: Allowing informed investors to hold junior tranches
[^4]: Enabling uninformed investors to hold senior tranches safely

Example: Mortgage-backed securities create AAA tranches that are relatively safe even if some mortgages default, while subordinated tranches absorb initial losses.

# Class Note 6

# Bank Runs, Deposit Insurance, and Liquidity Creation

Banks create liquidity by funding illiquid loans with liquid deposits. This maturity transformation creates value but also creates fragility.

## Diamond-Dybvig Model

The Diamond-Dybvig (1983) model shows how banks are vulnerable to runs:

[^1]: Banks invest in long-term projects
[^2]: Depositors have uncertain liquidity needs
[^3]: Banks offer demand deposits (withdraw anytime)
[^4]: If too many withdraw early, bank must liquidate projects at a loss
[^5]: This can create self-fulfilling panic

There are two equilibria:
- **Good equilibrium**: Only those with true liquidity needs withdraw
- **Bank run equilibrium**: Everyone withdraws fearing others will

## Deposit Insurance

Government deposit insurance can prevent runs by:
- Guaranteeing deposits up to a limit
- Removing incentive to withdraw in panic
- Allowing banks to continue maturity transformation

However, deposit insurance creates moral hazard:
- Banks may take excessive risks
- Depositors stop monitoring banks
- Requires regulation and supervision

## Modern Bank Runs

The 2008 financial crisis showed that runs can occur in:
- Money market funds
- Repo markets
- Commercial paper markets
- Shadow banking system

These "wholesale funding runs" can be as destabilizing as traditional deposit runs.

Example: Reserve Primary Fund "broke the buck" in 2008 after Lehman bankruptcy, triggering massive withdrawals from money market funds.

## Policy Responses

[^1]: Expand deposit insurance temporarily
[^2]: Provide liquidity facilities (Fed's discount window)
[^3]: Asset purchase programs
[^4]: Guarantee programs for money market funds
[^5]: Enhanced regulation of shadow banking

Key lesson: Any institution engaged in maturity transformation faces run risk, not just traditional banks.

# Class Note 7

# Commercial Paper, Repo Markets, and the Financial Crisis

The 2007-2008 financial crisis demonstrated how runs can occur in wholesale funding markets, particularly commercial paper (CP) and repurchase agreement (repo) markets.

## Commercial Paper Markets

Commercial paper is short-term debt (typically 1-270 days) issued by corporations and financial institutions:

- **Asset-Backed Commercial Paper (ABCP)**: Backed by pools of assets
- **Financial CP**: Issued by financial institutions
- **Corporate CP**: Issued by non-financial corporations

### ABCP Crisis

In 2007, concerns about mortgage assets led to:
[^1]: Investors refusing to roll over ABCP
[^2]: Conduits unable to fund their assets
[^3]: Banks forced to provide liquidity support
[^4]: Significant disruption to corporate funding

## Repo Markets

Repurchase agreements are short-term collateralized loans:
[^1]: Borrower sells securities to lender
[^2]: Agrees to repurchase at slightly higher price
[^3]: Difference is effectively interest

### Repo Run Dynamics

During the crisis:
- Haircuts increased dramatically
- Some collateral types became unacceptable
- Repo funding dried up for many institutions
- Bear Stearns and Lehman Brothers faced acute repo runs

### Mechanics of a Repo Run

Unlike traditional bank runs, repo runs involve:
[^1]: Increasing haircuts (margin requirements)
[^2]: Shortening of terms (overnight only)
[^3]: Rejection of certain collateral types
[^4]: Demands for cash collateral substitution

Example: Haircuts on AAA private-label MBS went from 3-5% to over 25% during the crisis.

## Case Studies

### Northern Rock (2007)
- UK mortgage lender dependent on wholesale funding
- First bank run in UK in 150 years
- Triggered by:
  - Inability to securitize mortgages
  - Frozen wholesale funding markets
  - BBC news report of Bank of England support

### Bear Stearns (2008)
- Lost repo funding over several days
- Clients withdrew prime brokerage assets
- Fed arranged emergency sale to JPMorgan

### Lehman Brothers (2008)
- Experienced accelerating repo run
- Fed declined to provide support
- Bankruptcy triggered:
  - Reserve Primary Fund breaking the buck
  - Freeze in CP markets
  - Global financial panic

## Policy Interventions

[^1]: **Term Auction Facility (TAF)**: Fed lending to banks
[^2]: **Primary Dealer Credit Facility (PDCF)**: Fed lending to broker-dealers
[^3]: **Asset-Backed Commercial Paper Money Market Mutual Fund Liquidity Facility (AMLF)**
[^4]: **Commercial Paper Funding Facility (CPFF)**: Fed purchases of CP
[^5]: **Term Asset-Backed Securities Loan Facility (TALF)**

These programs aimed to:
- Replace private funding with government funding
- Restore confidence in short-term markets
- Prevent fire sales of assets

## Lessons Learned

[^1]: Any maturity transformation creates run risk
[^2]: Wholesale funding more fragile than retail deposits
[^3]: Collateral values crucial in secured funding
[^4]: Central bank tools needed updating for market-based system
[^5]: International coordination essential

The crisis revealed the "shadow banking" system's vulnerability and led to significant regulatory changes including enhanced liquidity requirements and stress testing.

# Class Note 8

# LTCM Crisis, Arbitrage, and Market Meltdowns

The 1998 collapse of Long-Term Capital Management (LTCM) illustrates how leverage, crowded trades, and market dynamics can create systemic risk.

## LTCM Background

Founded in 1994 by:
- John Meriwether (former Salomon Brothers trader)
- Robert Merton and Myron Scholes (Nobel laureates)
- Team of prominent traders and academics

Strategy focused on:
- Fixed income arbitrage
- Convergence trades
- Market neutral positions
- High leverage to amplify small spreads

## The Trades

LTCM's positions included:

[^1]: **On-the-run/Off-the-run Treasury arbitrage**
   - Long older Treasuries (off-the-run)
   - Short newer Treasuries (on-the-run)
   - Betting on convergence of yields

[^2]: **Equity volatility trades**
   - Selling long-dated options
   - Believing implied volatility too high

[^3]: **Emerging market debt**
   - Long high-yield debt
   - Hedged with shorts in other markets

[^4]: **Merger arbitrage**
   - Long target companies
   - Short acquirers

## The Crisis Unfolds

August 1998 Russian default triggered:

[^1]: **Flight to quality**
   - Investors fled to liquid assets
   - Spread widening instead of convergence

[^2]: **Margin calls**
   - Prime brokers demanded more collateral
   - LTCM forced to reduce positions

[^3]: **Market impact**
   - Liquidations moved prices against them
   - Other funds in similar trades amplified moves

[^4]: **Correlation breakdown**
   - Previously uncorrelated assets moved together
   - Diversification benefits disappeared

## The Numbers

- Assets: $125 billion
- Equity: $4.8 billion (before crisis)
- Leverage: 25:1 on balance sheet
- Notional derivatives: Over $1 trillion
- Loss: $4.6 billion in weeks

## Systemic Risk

LTCM's collapse threatened because:

[^1]: **Counterparty exposure**
   - Major banks had large exposures
   - Potential cascade of failures

[^2]: **Common positions**
   - Many funds in similar trades
   - Disorderly unwinding would impact all

[^3]: **Market functioning**
   - Key arbitrage relationships breaking down
   - Price discovery impaired

## The Rescue

September 1998: Fed-orchestrated bailout
- 14 banks invested $3.6 billion
- Avoided forced liquidation
- Gradual unwinding of positions

Fed's reasoning:
- Not bailing out LTCM per se
- Preventing disorderly markets
- Maintaining financial stability

## Lessons for Risk Management

[^1]: **Leverage amplifies everything**
   - Small losses become large quickly
   - Liquidity crucial in crisis

[^2]: **Crowded trades dangerous**
   - Many funds in same positions
   - Exit becomes impossible

[^3]: **Correlations unstable**
   - Historical relationships break down
   - Stress scenarios essential

[^4]: **Model risk**
   - Models assume normal markets
   - Tail events more common than expected

[^5]: **Liquidity risk**
   - Funding can disappear
   - Asset liquidity evaporates in crisis

## Modern Applications

Similar dynamics in:
- 2007 Quant Equity meltdown
- 2020 COVID-19 market stress
- Archegos collapse (2021)

Key insight: Sophisticated models and Nobel prizes don't eliminate fundamental risks of leverage and crowded positions.

# Class Note 9

# Bailouts and Bank Failures

Bank failures and government interventions raise fundamental questions about moral hazard, systemic risk, and optimal policy responses.

## Continental Illinois (1984)

First major "too big to fail" case:

Background:
- 7th largest US bank
- Aggressive growth strategy
- Large portfolio of bad energy loans
- Heavy reliance on wholesale funding

The Crisis:
[^1]: Rumors about loan losses
[^2]: Wholesale funding runs
[^3]: Unable to access markets
[^4]: Fed/FDIC intervention

The Bailout:
- FDIC guaranteed all deposits (beyond $100k limit)
- Fed provided unlimited liquidity
- Government took 80% ownership
- Management replaced

Precedent set: Some banks too big to fail

## Policy Tools for Bank Failures

### 1. Purchase & Assumption (P&A)
- FDIC finds healthy bank to buy failed bank
- Acquiring bank takes deposits and good assets
- FDIC retains bad assets
- Least disruptive to depositors

### 2. Deposit Payoff
- FDIC pays insured depositors directly
- Uninsured depositors get receivership certificates
- Bank closed and liquidated
- Most disruptive option

### 3. Open Bank Assistance
- Bank remains open
- Government provides capital/guarantees
- Management usually replaced
- Used for systemic institutions

### 4. Bridge Bank
- FDIC operates bank temporarily
- Maintains banking services
- Prepares for sale/resolution
- Buys time for orderly resolution

## Modern Crisis Management

### 2008 Financial Crisis Responses

**Bear Stearns**: Facilitated acquisition
- Fed loan to JPMorgan
- $30 billion in asset guarantees
- Avoided bankruptcy

**Lehman Brothers**: Allowed to fail
- No buyer found
- Fed declined support
- Bankruptcy triggered panic

**AIG**: Bailout
- $85 billion Fed loan
- Government took 79.9% ownership
- Systemic risk from derivatives

**TARP Program**
- $700 billion authorized
- Capital injections to banks
- Helped stabilize system
- Most funds eventually repaid

## Deposit Insurance Design

Key parameters:
[^1]: **Coverage limit**: Balance between protection and moral hazard
[^2]: **Premium structure**: Risk-based vs flat rate
[^3]: **Funding**: Ex ante vs ex post
[^4]: **Scope**: Which institutions covered

International variations:
- US: $250,000 per depositor
- EU: €100,000 harmonized
- Some countries: unlimited during crisis

## Resolution Frameworks

### Dodd-Frank Act (2010)
Created new resolution tools:

[^1]: **Orderly Liquidation Authority (OLA)**
   - FDIC can resolve systemic non-banks
   - Shareholders/creditors bear losses
   - No taxpayer bailouts

[^2]: **Living Wills**
   - Large banks must plan for failure
   - Identify critical operations
   - Facilitate orderly resolution

[^3]: **Total Loss-Absorbing Capacity (TLAC)**
   - Large banks hold bail-in-able debt
   - Converts to equity in failure
   - Protects depositors/taxpayers

### Single Point of Entry (SPOE)
Resolution strategy for large banks:
[^1]: Holding company enters receivership
[^2]: Operating subsidiaries continue
[^3]: Losses pushed to holdco creditors
[^4]: Recapitalized and returned to private hands

## Lessons from Banking Crises

[^1]: **Speed matters**: Quick action prevents contagion
[^2]: **Clarity helps**: Clear rules reduce uncertainty
[^3]: **Credibility essential**: Markets must believe in backstops
[^4]: **International coordination**: Cross-border issues complex
[^5]: **Political constraints**: Bailouts unpopular but sometimes necessary

## Ongoing Debates

[^1]: **Too Big to Fail**: Still exists despite reforms?
[^2]: **Bail-in credibility**: Will it work in crisis?
[^3]: **Ring-fencing**: Protect retail from investment banking?
[^4]: **Central bank role**: Lender of last resort expansion?
[^5]: **Crypto/DeFi**: How to handle new forms of banking?

The optimal policy balances:
- Protecting financial stability
- Minimizing moral hazard
- Reducing taxpayer exposure
- Maintaining market discipline

History suggests this balance shifts with each crisis, as regulators learn new lessons and markets find new vulnerabilities.

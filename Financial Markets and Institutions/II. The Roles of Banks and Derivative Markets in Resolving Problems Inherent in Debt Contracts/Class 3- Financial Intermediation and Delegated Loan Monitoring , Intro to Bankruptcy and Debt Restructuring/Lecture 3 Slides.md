---
aliases:
- Debt Without Monitoring
- Lender and Borrower
- Optimal Contract
key_concepts:
- Bond pricing and fixed income securities valuation
- Ito's lemma and stochastic calculus applications
- Credit risk modeling and default probability estimation
- Credit default swaps and counterparty risk analysis
- Interest rate caps, floors, and swaptions
linter-yaml-title-alias: Direct Finance Without Monitoring
tags:
- correlation
- credit-risk
title: Direct Finance Without Monitoring
---


Financial Intermediation and Delegated Monitoring Business 35202 Class 3 1

# Lecture 3 Slides

!CleanShot 2024-09-23 -002834@2x.png

# Example From Last Class

!!Obsidian 2024-09-25 20.15.20.png

Actual cash flow not observed by lenders,  who observe only the amount repaid.
!CleanShot 2024-09-23 -002835@2x.png

# Example From Last Class

Actual cash flow not observed by lenders,  who observe only the amount repaid.
!CleanShot 2024-09-23 -002836@2x.png

# Debt Without Monitoring

 Optimal contract is a debt contract with face value f,  and liquidation if less is paid.
 What is the optimal face value,  f?
  We saw last time that f=1.3125 when the borrower must default 20% of the time and liquidation gives a recovery of zero.

!CleanShot 2024-09-23 -002837@2x.png

Costly Ex-post Information Used to renegotiate loans For example,  sometimes a lender should take less than is promised because that is all that a borrower must pay.

However,  the lender should not accept less than the borrower has available to pay.

 If ability to pay is costly to monitor,  then without monitoring,  the lender must demand a constant payment and liquidate if less is paid.

Delegated Monitoring by a bank
!CleanShot 2024-09-23 -002838@2x.png

Monitoring and Control

Intermediation Avoids Duplicated Outside

bank?

# Monitoring,  Delegation And

Incentives Loan Monitoring by a banker To avoid duplication of effort or a free rider problem,  loan monitoring must be delegated to one agent,  who turns out to use (debt deposit) contracts that make him a banker.

# Optimal Contract Without Monitoring Is Debt

 Liquidate as a sanction. Borrower,  lender risk neutral and the borrower has no other assets or collateral.

 Optimal state contingent contract based on observable payment to lender is to impose the sanction for low payments and not for those greater than or equal to f.

 f is interpreted as the face value of one period debt.

# Two State Example From Last Class

 Borrower has cash of V,  with realizations 1 or 1.4.

 Probability that 1.4 is 0.8.

 Realized cash flow,  V,  is observed only by borrower Borrower can steal or retain any cash not paid to lender.

 Lender requires expected repayment of 1+r=1.05 to make the loan.

### Monitoring needed due to uncertainty about the cash known only by borrower

Actual cash flow not observed by lenders,  who observe only the amount repaid.

!CleanShot 2024-09-23 -002839@2x.png

### Impose Liquidation Monitoring to renegotiate and avoid liquidation can do much better

Actual cash flow not observed by lenders,  who observe only the amount repaid.
!CleanShot 2024-09-23 -002840@2x.png

### If no uncertainty,  no private info. of borrower,  nothing to monitor/renegotiate

 Actual cash flow not observed by lenders,  who observe only the amount repaid.
!CleanShot 2024-09-23 -002841@2x.png

### If less uncertainty,  less private info. of borrower,  less need to monitor/renegot

Actual cash flow not observed by lenders,  who observe only the amount repaid
!CleanShot 2024-09-23 -002842@2x.png

### We will see that a diversified bank can reduce uncertainty to this amount

Actual cash flow not observed by lenders,  who observe only the amount repaid.
!CleanShot 2024-09-23 -002843@2x.png

- Face=1.09375

## Loan Monitoring
 - If a lender incurs a cost k,  the lender can monitor the borrower's cash flow.
 - The simplest interpretation is that the lender can observe the realized cash flow,  V,  and if V=1 the lender can unilaterally reduce the face value of debt down to f=1 (this requires the lender to have all the bargaining power to make concessions)

## Costly Monitoring
 - Without monitoring,  the best contract has value destroyed with probability 0.2.
- Monitoring costs k>0.
- If monitoring costs,  k,  are less than 0.2 (assuming the cost must be paid in advance,  by establishing a relationship,  for example),  it will be better to monitor.

### With many lenders (N in number),  the cost of monitoring is too high (=Nk)

!CleanShot 2024-09-23 -002844@2x.png

the best contract has no
monitoring

# Many Small Lenders
- Suppose the loan requires 10,  000 lenders (who have $100 and loan amount is in units of $1 Million) due to project scale and monitoring costs each,  monitoring does not pay (total is $2 M).
- Want to delegate it to one lender.
- But others will not freely observe what was monitored by the monitor.

# Don't Monitor the Monitor…
 - To avoid duplication of effort,  other lenders do not monitor the monitor
 - As a result monitor and borrower might get together,  and collude so that the other lenders do not benefit from the monitoring.
 - Need to provide incentives for delegated monitoring.
!CleanShot 2024-09-23 -002845@2x.png

Monitoring and Control Common Information No Information

Intermediation Avoids Duplicated Outside

bank?

### Intermediation Avoids Duplicated Outside

Monitoring and Control
!CleanShot 2024-09-23 -002846@2x.png

### Incentives for delegated monitoring: Bank Issues debt with face value B,  per loan
- Liquidate the bank for zero (all get 0) if bank pays out less than B (per loan).
 - Monitor/bank has no assets of its own.
 - Gets cash by collecting and negotiating the loan to borrower,  with face f.
 - When borrower has 1 bank can pay at most 1 then.
 - **Monitor be liquidated in same situations as the borrower with unmonitored debt.

# One Loan Per Bank

!CleanShot 2024-09-23 -002847@2x.png

 | Public  bond  with face  1.3125  receives | Amount bank can |  |  |  |  |  |
 | --------------------------------------------- | ---------------------------- | -------------------------------- | ----------------------------------- | ----- | ---- | ---- | ---- | 
 | Bond | extract by |  |  |  |  |  |
 | Distress | renegotiation of debt |  |  |  |  |  |
 | Cost | Probability with face f | One loan  Bank  Distress  cost | Saving  compared  to bond  issue? |  |  |  |
| Can the  bank Pay  B>1.05? |  |  |  |  |  |
 | 1.3125 | 0 | 0.8 | f | Yes | 0 | no |
 | 1 | 0 | 1 | 0.2 | 1 | No | 1 | no | 

# The One Loan Bank,  With Total Deposits Of B (B/N Each; Sanctions For Paying Less)

!CleanShot 2024-09-23-002848@2x.png

# The One Loan Bank Can't Survive
- A monitor who is liquidated in exactly the same sitiuations (and at the same cost) as the borrower who borrowed directly can't survive.
- The costs of liquidation are the same as borrowing direct,  and a monitoring cost in incurred.
- But a diversified monitor can implement delegated monitoring.

# The Two Loan Bank

!CleanShot 2024-09-23 -002849@2x.png
Each investor owed 2B/20,  000 = B/10,  000

# Diversification: Bank Contracts As Financial Engineering
- Example of "two loan bank."
- Makes and monitors two loans,  to 2 borrowers with independent and identically distributed projects
- Collects 1+f when only one loan defaults (2f when none default,  and 2 when both default).
- Bank fails only when both loans default (with probability (0.2)2=0.04. Reduces chance of penalty or inefficient liquidation

# The Two Loan Bank,  with Deposits Of 2B In Total

!CleanShot 2024-09-23 -002850@2x.png

# The Two Loan Bank,  with deposits of 2B (sanctions to bank for smaller payment)

!CleanShot 2024-09-23 -002851@2x.png

# Both Borrowers Return H,  Pay F

!CleanShot 2024-09-23 -002852@2x.png

# Both Borrowers Return 1; Collects 1+1=2

!CleanShot 2024-09-23 -002853@2x.png

# One Borrower Returns 1.4,  The Other 1

!CleanShot 2024-09-23 -002854@2x.png
!34_image_0.png

"Works out" bad loans,  collects good

# If the bank can avoid default when it collects 1+f,  it fails with prob 0.04
- Actual cash flow not observed by invesors,  who observe only the amount repaid.
!CleanShot 2024-09-23 -002855@2x.png
Face per loan=B=1.09375

# The 2-Loan Bank Can Survive

 Bank raises 2 in deposits,  promises 2B=2(1.09375)=2.1875 to depositors
 Bank can lend to each borrower at f=1.19 (19%),  Note that 1+f=2.19>2.1875.
 Collects f when V=1.4,  and 1 when V=1.
 1+f=2.19>2B=2.1875. Bank fails only if both default (Prob$=0.2^{2}=0.04$).
!CleanShot 2024-09-23 -002856@2x.png

|  |  |  |  | Distress cost |  |  |  |
 | ------------ | --------------------------------- | -------------------------- | --------------------------------------------- | ------------------------------ | ------------- | -------- | --------------------- | --- | --- | 
|  |  |  |  | 2B<1+f | per loan |  |  |
 | (1.4,             1.4) | 0 | 2f | 0.64 | 2B | No | 0 | No | 0 | 0 | 
 | (1.4,            1) | 1 | f+1 | 0.16 | 2B | Yes | 1+f | No | 0 | 0 | 
 | (1,            1.4) | 1 | 1+f | 0.16 | 2B | Yes | 1+f | No | 0 | 0 | 
 | (1,            1) | 2 | 2 | 0.04 | 2B | Yes | 2 | Yes | 2 | 1 | 
| Total  Distress  costs if  2B<1+f | Distress  cost per  loan | Payment | Deposit |  |  |  |  |
|  |  | received by  payment if  depositors 2B=2.1875 | Value of bank equity if f=1.19 |  |  |  |  |
| probability | Distress cost  times prob. |  | 2(1.19)2.1875 =  0.1925 |  |  |  |  |
 | (1.4,             1.4) | 0.64 | 0 | 0 | 0 | 2B | 2.1875 | 2.18752.1875 =  0.025 |  |
 | (1.4,            1) | 0.16 | 0 | 0 | 0 | 2B | 2.1875 |  |  |
 | (1,            1.4) | 0.16 | 0 | 0 | 0 | 2B | 2.1875 | 2.18752.1875 =  0.025 |  |
 | (1,            1) | 0.04 | 2 | 1 | 0.04 | 0 | 0 | 0 |  |
|  |  | (2B)=2(1.05),             2B= 2.1875 B=1.05/= 1.09375 |  |  |  |  |  |
|  |  |  |  | 38 |  |  |  |

# All Are Weakly Better Off
- Bank charges 19% (vs 31.25 % for unmonitored)
 - Pays 9.375% on deposits (gives depositors a 5% expected rate of return)
!CleanShot 2024-09-23 -002857@2x.png
 - Banker gets (2f-2B) + (1+f-2B)=
 =(2.38-2.1875) + (2.19-2.1875)
=0.124 > cost of monitoring
=(2()=0.0004)

# Further Diversification
 - As bank becomes well diversified (N∞),  it converges to a bank where 80% of loans pay f and 20% pay 1. It (almost) never fails. It just needs to cover its cost of capital (5%) and of monitoring (%).
 - Let 1 + 0.05 + = f + (1),  or f= 1.06275. This allows bank to break even.
- The well diversified bank can make loans at 6.275% and pay 5% on deposits and earn zero profits.
- Can out compete less diversified banks.
- Can earn profits if not fully competitive.

# Role Of Diversification
 - Diversified banks as original form of "Financial Engineering."
 - Transform loans that need monitoring into deposits that do not
 - Used in securitization today
- ("pooling" (diversification) and "tranching.md)" (selling off only senior claims)

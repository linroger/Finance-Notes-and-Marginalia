---
cssclasses:
- academia
linter-yaml-title-alias: Class SlIdes On Repurchase Agreements
title: Class Slides On Repurchase Agreements
tags:
- artificial-intelligence
- banking
- cdo
- collateralized-debt-obligation
- counterparty-risk
- credit
- credit-derivatives
- dva
- haircut
- haircuts
- interest-rate-derivatives
- interest_calculation
- lending
- ma
- margin
- market-value
- markets
- options
- options-pricing
- repo
- repo_transaction
- repurchase-agreements
- repurchase_agreements
aliases:
- Repo Slides
- Repurchase Agreements
key_concepts:
- Agricultural futures and seasonality
- Alternative investments and hedge fund strategies
- Asset swaps and spread-lock strategies
- Bank asset-liability management (ALM) strategies
- Bank capital adequacy and Basel III compliance
- Bank stress testing and CCAR requirements
- Barrier options and knock-in/knock-out structures
- Basel III capital requirements and risk metrics
- Basis swaps and cross-currency basis adjustments
- Basis swaps and floating rate correlations
- Behavioral finance and market anomalies
- Best execution and regulatory requirements
- Bid-ask spreads and market making profitability
- Black-Litterman model and portfolio optimization
- Borrowing a security
- CDO structuring and tranche allocation methodologies
- CDO-squared structures and correlation trading
- CDS spread curves and hazard rate modeling
- Calendar spreads and roll strategies
- Capital Asset Pricing Model (CAPM) and beta estimation
- Capital expenditure planning and depreciation
- Central bank digital currencies (CBDCs)
- Central clearing and CCP risk management
- Commodity futures and convenience yields
- Commodity swaps and energy derivatives
- Crack spreads in energy markets
- Credit default swaps (CDS) pricing
- Credit default swaps and credit protection mechanisms
- Credit risk assessment and loan pricing
- Credit valuation adjustment (CVA) and counterparty risk
- Cryptocurrency valuation and blockchain technology
- Currency swaps and cross-currency basis
- Dark pools and alternative trading venues
- DeFi protocols and decentralized finance
- Deposit insurance and systemic risk
- Discounted cash flow (DCF) valuation methodologies
- Duration and convexity for bond price sensitivity
- ESG investing and sustainability metrics
- Enterprise value and equity value relationships
- Equity swaps and total return swaps
- Exotic derivatives and path-dependent options
- Expected Shortfall (ES) and coherent risk measures
- Extreme value theory and tail risk modeling
- FX futures and currency hedging
- Fama-French three-factor and five-factor models
- Fintech disruption and digital banking
- Forward contract pricing and cost of carry
- GARCH models for volatility forecasting
- Gamma trading and convexity adjustments
- Green bonds and climate risk assessment
- HJM and forward rate model frameworks
- High frequency trading and algorithmic strategies
- Historical simulation and parametric VaR approaches
- Hull-White and Black-Karasinski short rate models
- IPO pricing and underpricing analysis
- Implied volatility and volatility surface modeling
- Inflation-linked swaps and CPI adjustments
- Interest calculation
- Interest rate derivatives and forward rate agreements
- Interest rate models and term structure
- Interest rate swaps and swap spread decomposition
- Key rate duration and curve risk decomposition
- Liquidity-adjusted VaR and liquidity horizons
- Margin or haircut
- Margin requirements and collateral optimization
- Market impact and transaction cost analysis
- Mean reversion in interest rate processes
- Mergers and acquisitions due diligence
- Metal futures and industrial commodities
- Model backtesting and validation procedures
- Momentum and reversal investment strategies
- Mortgage-backed securities and prepayment modeling
- Multi-factor interest rate models
- Negative interest rates and floor/cap structures
- Net interest margin and banking profitability
- Netting agreements and close-out procedures
- Non-deliverable forwards and emerging market instruments
- OIS discounting and collateralized interest rate derivatives
- Option-adjusted spread (OAS) analysis
- Options on futures and forward-starting options
- Payment systems and settlement risk
- Prime brokerage and securities lending
- Private credit and direct lending
- Project finance and syndicated lending
- Recovery rate modeling and loss given default
- Repo markets and securities lending
- Repo transaction example
- Risk factor decomposition and sensitivity analysis
- Risk parity and risk budgeting strategies
- Selling the security
- Shadow banking and non-bank intermediation
- Smart beta and alternative indexing approaches
- Stochastic volatility in interest rate markets
- Stress testing and scenario analysis frameworks
- Subprime mortgage crisis and structured finance risks
- Swaptions and interest rate option pricing
- Swaptions and option volatility surfaces
- Synthetic CDOs and credit-linked note structures
- Terminal value modeling and exit multiples
- 'The Greeks: Delta, Gamma, Vega, Theta, and Rho sensitivity analysis'
- Too-big-to-fail policies and resolution regimes
- Treasury futures and bond basis
- Treasury securities and government bond markets
- VIX futures and volatility trading
- Value at Risk (VaR) and expected shortfall methodologies
- Value vs growth investing frameworks
- Vasicek and CIR interest rate models
- Volatility smile and skew patterns in option markets
- Weighted average cost of capital (WACC) calculations
- Working capital and cash conversion cycle
- Wrong-way risk and correlation adjustments
enhanced: true
enhancement_date: '2025-11-06'
enhancement_id: batch04-078877
---




Class Note 12 Part 2 Repos

# Class Slides On Repurchase Agreements

#### I. Introduction to Repos
- **Example of a Repo Transaction**:
  - Suppose I have a security with a market value of $V$,  say \$1 M.
  - We can enter into the following agreement (Bilateral Repo):
	- Today,  I sell you my security for $V - m$.
	  - Say: $\$1 M - \$50 K = \$950 K$
	  - We refer to $\frac{m}{V}$,  $5\%$ in this case,  as the margin or haircut.
	- Today,  I also agree to repurchase the security tomorrow for:
	  - $V - m$,  i.e.,  the amount I sold it to you for,  plus
	  - Interest on $V - m$ at a negotiated rate,  say $1\%$ per year.
		- So the interest would be:
		  $$ 
          \text{Interest} = 950K \cdot \left(\frac{1}{360}\right) \cdot (1\%) = 26.38 
          $$ 
		- This is how interest is calculated: loan amount (\$950 K) times the number of days divided by 360 $(\frac{1}{360})$ times the annual rate $(1\%)$.
	- So tomorrow,  I am supposed to pay you:
	  $$
      950K + 26.38 = 950,  026.38
      $$ 
	  - And you are supposed to give me my security back.

#### II. Key Points of the Transaction
- I am simultaneously:
  - Lending a security.
  - Borrowing money (i.e.,  the \$950 K),  on which I pay interest.
- Simultaneously,  you are:
  - Borrowing a security.
  - Lending money,  on which you earn interest.
- If I default on my obligation to repurchase the security,  then you can try to make yourself whole by selling the security:
  - Since the security was originally worth $5\%$ more than the loan,  it will be sufficient to make you whole unless its value dropped by more than $5\%$ during that day.
- If you default on your obligation to sell the security back to me for the negotiated price of \$950,  026.38,  then I keep that amount:
  - Since the security was worth more than the loan amount,  I lose money in this situation unless the security's value dropped by more than $5\%$,  in which case I'm better off with the cash than the security.

#### III. Understanding Repo Agreements
- Think of a repo as collateralized borrowing of cash:
  - I am borrowing against the value of my security by simultaneously selling it and contracting to repurchase it tomorrow (or any other agreed-upon day).
- You can equivalently think of it as collateralized borrowing of the security by the other side of the repo.

##### Key Elements of a Repo Agreement
- The margin (5% in our example).
- The term (1 day in our example).
- The interest rate (1% in our example).

#### IV. Repos in Securities Trading
- Repos are fundamental to how institutions engaged in securities trading and financing themselves.
- If I wanted to buy the security for \$1 M from someone,  say Albert,  I could do the following:
  1. Agree with Albert to buy the security for \$1 M.
  1. Arrange with Bob for a repo of this security with the terms discussed above.
  1. Simultaneously,  the following things happen:
	 - Albert gives me the security.
	 - I pass it on to Bob.
	 - Bob gives me \$950 K.
	 - I add \$50 K from my own pocket to the \$950 K,  giving a total of \$1 M to Albert.
  - At this point,  Albert is out of the picture; he has delivered his security and received his \$1 M.
  - My remaining relationship is with Bob,  from whom I'm borrowing money at $1\%$.

#### V. Selling the Security
- The next day,  let’s say I want to sell the security to Charles,  who offers \$1.1 M for it:
  1. I can agree to sell it to Charles for \$1.1 M.
  1. Simultaneously:
	 - Bob gives me the security.
	 - I pass it on to Charles.
	 - Charles gives me \$1.1 M.
	 - Out of the \$1.1 M,  I pay \$950,  026.38 to Bob.
	   - Leaving me with:
		 $$
         1.1M - 950,  026.38 = 149,  973.62
         $$
	   - My net profit is:
		 $$
         149,  973.62 - 50,  000 = 99,  973.62
         $$
- Notice that,  as long as Bob and I end our repo according to the contract,  Bob is not exposed to the value of the security. The rise (or fall) of its market value accrues completely to me.
- The margin negotiated with Bob determines how much cash I need for this transaction. With a 5% margin,  I'm paying only 5% of the purchase price.

#### VI. Run on the Repo Market
- If you are lending money in a repo transaction,  the margin protects against:
  1. Your counterparty failing to repurchase the security.
  1. The security’s price dropping.
- If you believe the scenario is unlikely,  you might not require margin. But if you become anxious about your counterparty or the security's risk,  you start requiring more margin.
- If the security is a subprime mortgage-backed security and you decide that $5\%$ margin isn't enough,  you may want $10\%$.

#### VII. Increased Margin Impact
- When I return to repurchase the security as contracted,  you say,  "Sure,  as long as we increase the margin to $10\%$."
  - $10\%$ margin on a $\$1 M$ security is $\$100 K$,   so I must pay in an additional $\$50 K$.
- If I don't have the extra $\$50 K$,   I can't do the repo,   and if everyone else demands $10\%$,  I'll have to sell the security today,  even without a ready buyer.
- If I sell the security for $\$960 K$ instead of $\$1 M$:
  - Lenders will say,  "This security is now worth $\$960 K$,   not \$1 M."
  - Now,  they will loan only:
	$$
    960K \cdot 90\% = 864K
    $$
  - They are marking the security to market.

#### VIII. Contagion Effects
- Everybody borrowing against it now has to put up the $10\%$ margin and pay more cash to cover the decrease in mark-to-market value.
- Some may not have enough cash and will be forced to sell.
- Forced sales push mark-to-market value down further,  leading to more selling.
- Lenders respond to the increased risk of securities by increasing margin,  adding stress to investors.

##### Bank Run Analogy
- This situation is similar to a bank run,  but with a twist:
  - If my lenders aren't nervous but Fred's lenders are,  and they force Fred to sell at a bad price,  that price affects my lenders' decisions.
  - This leads to a chain reaction,  reducing market prices further.

#### IX. Graph: Margins Over Time

Here’s a graph showing margins (i.e.,  haircuts) of different quality mortgage-backed securities.md) over time:

 !Margins Over Time

- Margins are zero until the summer of 2007.
- Then they increase significantly,  with margin on subprime eventually reaching $100\%$ (meaning no lending against subprime collateral).

#### X. Repo-Haircut Index

 !Repo-Haircut Index

- The repo-haircut index is the equally weighted average haircut for all nine asset classes.
- As the need for cash increased to hold mortgage-backed securities.md),  particularly subprime,  investors had to either recapitalize,  sell their securities,  or potentially go bankrupt.

#### XI. Tri-Party Repo
- Much of the repo market is tri-party repo,  involving a third party.
- If I want to do a repo but don’t trust Bob,  and we both trust JP Morgan,  we can do a repo with JP Morgan:
  - I do the same repo as before,  but with JP Morgan instead of Bob,  at $1.25\%$.
  - Bob does the same with JP Morgan instead of me,  at $0.75\%$.

#### XII. Advantages of Tri-Party Repo
- I pay $0.25\%$ more interest for more security (less worry about counterparty default).
- Bob gets $0.25\%$ less interest but also more security.
- JP Morgan makes a spread of $0.50\%$ for bearing our counterparty risk.

##### Haircut Adjustments
- Haircuts in this market do not adjust quickly.
- If haircuts increase for a borrower,  they may get shut out of the tri-party repo market.
- This happened to Lehman and Bear Stearns.

#### XIII. Graph: Differences in Haircuts

  !Differences in Haircuts

- The difference is calculated as repo median minus tri-party median for each asset class.
- The dotted black line represents zero.

#### XIV. Lehman Brothers' Tri-Party Book

  !Lehman Brothers' Tri-Party Book

#### XV. Number of Cash Investors in Lehman Brothers

  !Number of Cash Investors

- The red line corresponds to Lehman bankruptcy filing.

#### XVI. Structural Problems in Tri-Party Market
- Structural issues existed in the tri-party market before 2010.
- A "morning unwind" provided security to cash investors if the borrower was having trouble rolling over.
- Tri-party repos are more subject to runs than bilateral repos due to this structure.

#### XVII. Fed Intervention
- The Fed introduced the Primary Dealer Credit Facility to loan money to dealers,  using securities as collateral.
- These loans are not repos but are similar in nature,  totaling around \$20 B.

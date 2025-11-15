---
aliases:
- Control Rights
- Kohler Co Valuation
- Marketability Discount Analysis
- Private Company Valuation Methods
- Family Firm Governance
cssclasses: academia
date created: Tuesday, November 26th 2024, 7:45:23 pm
enhanced: true
enhancement_date: '2025-11-06'
enhancement_id: batch03-557bee
key_concepts:
- Extensions to multi-factor CAPM models
- private benefits consumption
- investor protection importance
- capital markets and issuance
- minority discount methodology
- Extreme value theory and tail risk modeling
- Credit risk modeling and default probability estimation
- valuing private companies
- pyramidal ownership structures
- Capital Asset Pricing Model and expected returns
- Historical simulation vs. parametric VaR models
- Credit portfolio diversification and concentration
- DV01 calculation and interest rate risk hedging
- dcf and wacc application
- Swap spread and credit risk considerations
- Mathematical Finance
- control enhancing mechanisms
- GARCH models and volatility forecasting
- Monte Carlo VaR for complex portfolios
- cost of capital estimation
- governance premium valuation
- total beta approach
- Stress testing and scenario analysis
- Key rate duration and curve risk
- corporate governance analysis
- related party transactions
- Fixed-for-floating swap cash flows and valuation
- Course Material
- Security Market Line and beta measurement
- Value at Risk (VaR) methodologies and backtesting
- Risk-neutral pricing methodology for derivative securities
- Case Study
- Dividend Policy
- Generally Accepted Accounting Principles
- fundamental valuation methods
- control rights valuation
- Expected Shortfall and coherent risk measures
- Interest rate swap pricing and valuation
- Variance swaps and volatility trading strategies
- Credit exposure measurement and EAD
- Kohler family case study
- Wrong-way risk in derivative transactions
- systematic risk and market exposure
- insider ownership impact
- Value-at-Risk calculation using historical simulation
- Quantitative Implementation
- Credit risk migration matrices and rating transition
- control premium calculation
- Credit risk modeling and portfolio correlation analysis
- Backtesting procedures for risk models
- illiquidity cost of capital
- Cross-currency basis swaps and funding
- Duration and convexity measures for bond portfolios
- Price sensitivity to interest rate changes
- Loss given default and recovery rates
- Market portfolio and risk-free rate assumptions
- Modified duration vs. Macaulay duration
- lack of marketability discount
- Empirical tests and anomalies in CAPM
linter-yaml-title-alias: Week 7 - Private, Family and Closely-held Firms - Analysis
  and Valuation
tags:
- corporate-governance
- dividend-policy
- capm
- case-study
- value-at-risk
- credit-risk
- dcf_valuation
- private_firms
- duration-convexity
- solution
- wacc
- wacc_calculation
- closely_held_firms
- cost-of-capital
- kohler_case
- insider_ownership
- valuation_methods
- total_beta
- corporate_governance
- municipal-bonds
- expected-shortfall
- institutional_environment
- family_business
- emerging_markets
- garch-models
- interest-rate-swaps
- mathematical-finance
- course-material
- audit
- impairment
- quantitative-implementation
- stress-testing
- emerging-markets
- exotic-options
- dcf-valuation
- gaap
- harvard-business-review
- monte-carlo
title: Week 7 - Private, Family and Closely-held Firms - Analysis and Valuation
---

# Week 7 - Private, Family and Closely-held Firms - Analysis and Valuation

## File Information
- **Course**: Advanced Financial Analysis and Valuation
- **Week**: 7
- **Topic**: Private and Family Firm Valuation
- **Instructor**: Pervin Shroff

## Overview

- More than 60% of global GDP driven by "closely held" public or private firms
- Analyzing and valuing private companies
  - Relevant in many contexts (IPO, M&A, VC, PE, tax purposes, etc.)
  - Key issues:
    - No traded equity
    - Control rights
- Control rights also matter great deal for listed firms with families or when closely-held
  - Founders or family want to keep control
- Determining the control premium (or minority discount) and liquidity premium
- Kohler case study
- Analyzing corporate governance
  - Closely-held firms and governance
  - Does governance matter for valuation?

## U.S. Private Firms: Big and Growing in Numbers

!Private firm growth trends

[^1]: Unique U.S.-based common stock PERMCO on CRSP as of December of each year per monthly file
[^2]: Number of corporations per IRS SOI aggregate data. Excludes partnerships

## U.S. Private Firms (Continued)

MEDIUM-TO-LARGE PRIVATE U.S. COMPANIES BY INDUSTRY

!Industry distribution of private firms

N = 70,425 non-financial firms filing 1120, 1120-S, or 1065 and also filing Schedule M-3 (> $10 million in assets) but not filing with SEC

!Private firm characteristics

## Private Firms: Examples

Important consideration for valuation of private firms:
- Value (Share) = Value (Cash Flows) + Value (Control)
- Value of control can be substantial

## Closely-held (but Public) Firms: Examples

Important consideration for valuation "closely held" firms:
- Value (Share) = Value (Cash Flows) + Value (Control)
- Value of shares for controlling shareholders can be very different from noncontrolling ones

!Closely-held firm examples

# Valuing Private Companies

## Central Issue: Information

- U.S. private companies are not required to provide audited GAAP financials
  - Different in many parts of the world that have statutory reporting requirements
- But even when required, information for private companies tends to be much more limited
  - Owners are often secretive
  - Less information production by analysts, investors, etc.
  - Market prices aggregate a lot of information (including implications of macroeconomic news)
- How to account for information problems?
  - Adjust cash flows or cost of capital?
  - We come back to this at the end and next week

## Valuation Challenges for Private (and Closely-held) Firms

What do we need to think about?
- Control (or lack thereof)
- Lack of marketability (or liquidity)
- Under-diversification of owners
- Institutional environment (as it interacts with above)

Put differently, how should we account for?
- Value of control
- No or little liquidity
- Diversification: How should we determine beta?
- Institutional risks (e.g., poor investor protection)

## What Comes with Control? A Few Examples

Setting company policy:
- Power to acquire and dispose of business assets
- Power to select vendors and suppliers
- M&A

Financial policy:
- Going public (or staying private)
- Power to determine dividend policy

Appointing management and determining compensation

Important: With control also comes power to block any of the above (and more)

There are also intangible benefits of control
- E.g., keeping firm in family

## Why Is There a Control Premium?

Control rights clearly have value (previous slide)
- But why does it matter who controls?

There are conflicts of interest:
- Ability to make decisions that benefit insiders (private benefits)
- Link between control premium and private control benefits (show later)
- Greater information access

Control premium can be sizeable
- On average, control premium is around 20-30%

Control premium is not likely to be the same across firms – Why?
- Governance & management quality
- Legal protection and institutional environment
- It matters what insiders could do with their control

## Control Premium and Minority Discount

Control premium and minority discount are inversely related:

$$\text{Minority Discount \%} = 1 - \left(\frac{1}{1 + \text{Control Premium \%}}\right)$$

$$V_c = V_m \times (1 + CP) \quad V_m = V_c \times (1 - MD)$$

E.g., CP = 25% relative to minority shares is equivalent to minority shares valued at MD = 20% relative to controlling shares

Discount (or premium) is applied to base valuation

> [!NOTE]
> "Often there is more money at stake in determining what discounts or premiums are applicable to some business valuations than there is arriving at the base value." (S. Pratt, Business Valuations and Discounts, 2001)

## Marketability (or Liquidity) - Lack of Marketability (Discount)

- There is general agreement that the value of shares in an illiquid company should be lower – Ability to trade adds value
- Large variation in the average discount: approx. 20-40%
  - Probably much smaller today (at least in the U.S.)

> [!NOTE]
> "Lack of marketability, more often than not, is the largest dollar discount factor in the valuation of a business interest, particularly a minority interest." (S. Pratt, Business Valuations and Discounts, 2001)

- CONTROL PREMIUM AND LIQUIDITY PREMIUM ARE NOT INDEPENDENT
  - There are reasons why control stakes are illiquid
- DISCOUNT FOR LACK OF MARKETABILITY COULD BE DIFFERENT FOR CONTROLLING AND NONCONTROLLING INTEREST
  - WHY?
  - Controlling insiders could change the lack of marketability (i.e., go public)

## Example

It is common practice that minority and marketability discounts are applied in multiplicative rather than in additive fashion
- They are taken in sequence

Here, assume a 30% minority discount and a 40% marketability discount
- Assume a $10 value per share for controlling owner

 | Value | Description | 
 | --------- | -------------------------------------------------- | 
 | $10.00 | Control value | 
 | (3.00) | Less minority discount (30% × $10) | 
 | 7.00 | Minority value if shares were marketable | 
 | (2.80) | Less marketability discount (40% × $7) | 
 | $4.20 | Value per share of non-marketable minority share | 

## Adjustments to Valuation: Summary

Control premium or minority discount:
$$\text{Minority Discount} = \frac{1}{1 + \text{Control Premium}}$$

Liquidity premium or lack of marketability discount
- Associated with limited marketability of the shares

Is there something else?
- Wealth of Kohler family is tied to the company

Lack of diversification
- Kohler family is exposed not only to systematic risk (measured by beta) but also to idiosyncratic risk
- Use "total beta" instead of usual market beta:
- Because Kohler Co is private, need to use comparable companies to estimate market or total beta

## Illiquidity vs. Diversification

What is the difference between lack of marketability discount and the total beta approach for lack of diversification?
- Beta recognizes diversification
- Total beta is lack of diversification of the owner (it is about price of risk)
- Marketability is about your ability to trade the asset (irrespective of whether or not its risks are diversifiable)

Illiquidity can increase the cost of capital even for publicly-traded firms
- Transaction costs: bid-ask spread
- Information asymmetry and adverse selection
- Asset pricing models can include illiquidity factor (e.g., Pastor & Stambaugh, 2003)
- This increase is in same spirit as lack of marketability discount

If you discount the private firm value for illiquidity, do not also adjust cost of capital
- Be careful about double counting

# Kohler Case

## Purpose of the Case

Illustrates valuation of later-generation, large private and family-run firm
- Founding families' desire to retain control results in being less diversified
- Control benefits and family interests could be in conflict with minority shareholders
- Lack of marketability and illiquidity discount

Great review of DCF and WACC in time for final project

Questions:
[^1]: Why does Herbert Kohler want the recapitalization?
[^2]: What are the key differences to valuing public companies? (already covered)
[^3]: Which discounts would you apply?
[^4]: What discounts would get you to $55,400?

# Closely-held and Family Firms

## Closely-held and (Publicly Traded) Family Firms

Both are very common around the world

> [!NOTE]
> A growing number of family-owned businesses in emerging markets could hit $1bn in sales from 2010-2025

- Dispersed shareholder base is the exception, rather than the norm
- Ownership is typically concentrated around the world

!Family ownership patterns globally

As with private firms:
- Insiders have control
- Controlling blocks are illiquid

*Source: McKinsey*

## Insider Ownership Around the World

!Insider ownership by country

*Kho et al. / Journal of Accounting Research, Vol. 47 No. 2 May 2009*

## Insider Ownership Around the World (Continued)

!Additional insider ownership data

## Evolution of Ownership Concentration

!Ownership concentration trends over time

*Source: Aminadav & Papaioannou, Journal of Finance, 2020*

## Insider Ownership and Corporate Governance

With concentrated ownership, the governance (or agency) problem between managers and shareholders is less of an issue
- Why?

Instead, a different conflict of interest arises
- Conflict between controlling and minority shareholders (or insiders & outsiders)
  - Controlling insiders could make decisions that are in their interest rather than all shareholders
  - Private benefits consumption, keeping control in the family
  - Incentives for wealth transfers, tunneling and related-party transactions
  - Outside investors are much less informed

Incentives to consume private benefits depend on investment opportunities
- Need to raise outside finance disciplines insiders

## Control Premium and Private Control Benefits

Issue: Controlling insiders can consume cash flows that are no longer available to minority owners
- Company is not run to maximize value but to benefit controlling insiders

What would you bid as an outsider for 51% vs. 49%?
- Value of the firm run optimally, say $150M
- Value of the firm with incumbent management, say $100M
  - Consume $50M as private control benefits

The difference in values between the 51% and 49% shares is:
- Value (Control) = 51% × ValueMax = 51% × $150M = $76.5M
- Value (No-Control) = 49% × ValueStatus-Quo = 49% × $100M = $49M

Majority ownership is not necessary for control:
- Shareholder can control a company with 20% stake, if base is sufficiently dispersed
- Separation of control & cash flow rights: Pyramids, superior voting rights

## Control Enhancing Mechanisms

How to exercise control:
- Ownership
- Voting rights
- Board positions
- Management

Commonly used structures to enhance control:
- Dual share classes
- Enhanced (or super) voting rights
- Pyramids

!Control enhancement structures

## Example: Renong Berhad

OWNERSHIP STRUCTURE OF FIRMS CONTROLLED BY RENONG BERHAD

!Renong Berhad ownership pyramid

- UEM bought shares in parent, Renong Berhad, for an artificially high price
  - Renong shares purchased were held by family members in UEM's and Renong's management who wanted to 'get out'
- Prosecutors and courts initially said they would intervene, but ended up doing nothing

*(Source: Lemmon and Lins (2003) Journal of Finance)*

## Example: Caterpillar Buys ERA Mining Machinery Ltd

- Caterpillar announced tender offer for Hong Kong-listed ERA Mining Machinery in late 2011
- ERA was the holding company of Siwei, one of China's biggest makers of hydraulic coal-mine roof supports
  - Idea was to gain traction in China's heavy machinery market and the world's largest coal industry
  - Deal closed for $677 million in June 2012

Outcome:
- Nov 2012, during the integration process, Caterpillar uncovered discrepancy between the inventory on the books of Siwei and its actual physical inventory
- Prompted further investigations uncovered "deliberate, multi-year, coordinated accounting misconduct" by the Siwei management
- Jan 2013, Caterpillar took impairment charge of US$580m (86% purchase price)
- Red flags (e.g., Hong Kong listing via reverse takeover, unusual transactions between directors and Siwei) were overlooked during the due diligence process

## Investor Protection

COUNTRIES DIFFER A LOT IN HOW THEY PROTECT OUTSIDE INVESTORS
- When legal protection of outside investors is weak, investors fear governance problems and expropriation → price protect
- Evidence that family-controlled firms perform worse than widely-held firms or firms with (non-family) blockholders (in countries with weak protection)
- Differences in investor protection and disclosure regulation are associated with firms' cost of capital (and valuations)

WHAT DOES THIS IMPLY?
- Make sure to understand the ownership structure of a target firm
- Adjust the valuation for the effects of insider control:
  - Subtract cash flows consumed by insiders for private benefits
  - Consider cost of capital adjustments (see Week 8 for adjustments)
- Pay attention to related-party transactions

## Evidence on Price Protection by Outsiders

Outside investors recognize their 'disadvantage'
- Protect by paying less (or more if governance is good)

McKinsey 2002 survey of >200 institutional investors managing $2 trillion
- Large premia for strong governance:
  - 12-14% in North America & Western Europe
  - 20-25% in Asia & Latin America
  - >30% in Eastern Europe
- Governance "as important as financial performance" in investment decisions

Institutional Shareholder Services (ISS) survey in 2006: 70% of respondents think a firm's corporate governance is either extremely or very important

Survey results are consistent with holding patterns of U.S. investors
- Leuz, Lins and Warnock (RFS 2008):
U.S. investors stay away from stocks with "problematic ownership structures", particularly in countries with weak legal systems and when information flows are poor

Evidence that governance is priced by markets (in valuations & even returns)

## Investor Protection & Governance in Emerging Markets

!Institutional and governance scores by country

Considering the institutional & governance scores, what would be your valuation of Company if it were located / listed in each of the below emerging markets?

## Investor Protection & Governance in EMs (Continued)

!Cost of equity by emerging market

What cost of equity would you apply to Company if it were located and listed in each of the emerging markets below?

Survey respondents tend to incorporate higher premiums in their cost of equity estimates than what was implied in their valuation discounts (on previous slide)
- "Exponential growth bias"
- Underestimate the implications of compounding

*Source: ST Investor Protection and Governance in the Valuation of Emerging Markets survey*

## How Could You Incorporate Corporate Governance?

Apply valuation adjustment at the end?
- Like a minority discount

Adjust components of valuation model
- Increase cost of capital
- Adjust cash flows

Adjusting cash flows:
- Would it make sense to use better governed firms as a benchmark
  - How?
- Use value drivers: They often already reflect the governance structure
  - Low margins due to inefficient management
  - Higher reinvestment rates due to value-destroying investments or private benefits
- Same applies for multiples

Be careful about double-counting

## Example: Beware of Double Counting

!Double counting example

## Appendix: Related-Party Transactions Rules

In the US (ASC 850): Firms are required to disclose material related-party transactions
- PCAOB Auditing Standard No. 2410 requires auditors of public companies to review related-party transactions and communicate them to the audit committee

In the EU, the Shareholder Rights Directive rules require companies to publicly announce "material" related-party transactions in advance and to provide information about their fairness
- Member states had to adopt their versions of these rules by June 2019

Related-party transactions are particularly relevant in family firms, as such transactions often have the potential to negatively affect minority investors
- "In Hong Kong, most companies are family-owned, so we have to put our corporate governance emphasis on connected transactions between the major shareholders and the companies. This is different from the Western world where they have a more diversified shareholding structure, so their corporate governance measures focus on management behavior." – Paul Chow, CEO of the Hong Kong Exchanges and Clearing Limited (HKEx), 2004
- Cheung et al. (2006 JFE) and the HK Institute for Monetary Research found that about 66% of 328 related-party disclosures involved transactions that were likely to result in the expropriation of minority shareholders

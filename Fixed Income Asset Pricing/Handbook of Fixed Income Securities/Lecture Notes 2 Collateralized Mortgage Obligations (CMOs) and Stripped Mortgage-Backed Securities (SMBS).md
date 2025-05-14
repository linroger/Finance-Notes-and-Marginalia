---
title: Lecture Notes 2 Collateralized Mortgage Obligations (CMOs) and Stripped Mortgage-Backed
  Securities (SMBS)
cssclasses: academia
tags:
  - cmo
  - mortgage_backed_securities
  - prepayment_risk
  - smbs
  - structured_securities
aliases:
  - CMOs
  - Collateralized Mortgage Obligations
  - SMBS
  - Stripped MBS
key_concepts:
  - 'CMOs: structured securities'
  - 'IOs: interest only'
  - 'PAC: stable cash flows'
  - 'POs: principal only'
  - 'SMBS: interest/principal split'
  - 'Support bonds: variable cash flows'
---

# Lecture Notes 2 Collateralized Mortgage Obligations (CMOs) and Stripped Mortgage-Backed Securities (SMBS)

## 1. Introduction to CMOs and SMBS
- **Definition and Purpose**:
  - [[Other MBS|Collateralized Mortgage Obligations]] (CMOs) are [[A Simple Classification of Structured Notes|structured securities]] created by pooling mortgage pass-through securities and dividing them into tranches with varying risk,  return,  and maturity profiles.
  - Stripped [[Fremont Financial Corp. (b)|Mortgage-Backed Securities]] (SMBS) are [[Chapter 9 Arbitrage and Hedging With Options|derivatives]] of [[Fremont Financial Corp. (b)|mortgage-backed securities]] (MBS) that separate [[Notes on Currency Swaps|interest and principal]] cash flows into distinct securities,  such as Interest-Only (IO) and Principal-Only (PO) tranches.
- **Historical Context**:
  - CMOs were introduced by Freddie Mac in 1983 to address investor needs for tailored risk and maturity profiles.
  - SMBS were introduced by Fannie Mae in 1986 to allow investors to take specific positions on prepayment and interest rate movements.

## 2. Types of CMO Tranches
- **Planned Amortization Class (PAC)**:
  - Designed to provide stable cash flows within a predefined prepayment band.
  - Offers reduced extension and contraction risk compared to other tranches.
  - **Analysis**:
	- PACs are attractive for investors seeking cash-flow stability.
	- Broken PACs (when prepayment speeds fall outside the PAC band) may trade at wider spreads,  offering relative value opportunities.
- **PAC 2**:
  - A secondary PAC class with tighter PAC bands.
  - Higher yield than PACs but greater exposure to extension and call risk.
  - **Example**:
	- Exhibit 23-6 illustrates a PAC 2 bond with a tight PAC band,  showing no cash-flow stability in ±100 bp scenarios.
- **Support Bonds (Companions)**:
  - Absorb excess principal payments after PAC bonds are paid.
  - High yield but highly variable cash flows.
  - **Example**:
	- Exhibit 23-7 demonstrates the wide variability in average life for a support bond.
- **Targeted Amortization Class (TAC)**:
  - Similar to PACs but with one-sided call protection.
  - Significant extension risk if prepayments slow.
  - **Example**:
	- Exhibit 23-8 shows a TAC bond with extension risk extending durations to 20+ years under slow prepayment scenarios.
- **PACquential**:
  - Combines features of PACs and sequential tranches.
  - Offers a PAC band but with more extension risk.
  - **Example**:
	- Exhibit 23-9 shows a PACquential bond with a PAC band of 150–360 PSA and minimal extension risk at 120 PSA.
- **Z-Bonds**:
  - Interest accrues and is added to principal during the initial phase,  similar to zero-coupon bonds.
  - Long [[Key Rates O1s Durations and Hedging|duration]] and sensitive to [[How Countries Go Broke-Chapter 12 to Chapter 14|interest rate changes]].
  - **Example**:
	- Exhibit 23-10 illustrates a Z-bond with wide average life variability and an OAD of 19.5.
- **Very Accurately Determined Maturity (VADM)**:
  - Structured for short,  stable final maturities.
  - Resistant to extension risk but exposed to call risk.
  - **Example**:
	- Exhibit 23-11 shows a VADM bond with a 5.95-year average life even at zero prepayments.
- **Floaters and Inverse Floaters**:
  - Floaters have [[Interest Rate Quotations|interest rates]] tied to an index (e.g.,  SOFR),  with [[Interest Rate Derivatives-An Introduction to the  Pricing of Caps and Floors|caps and floors]].
  - Inverse floaters have [[Interest Rate Quotations|interest rates]] that move inversely to the index.
  - **Examples**:
	- Exhibit 23-12 shows a floating-rate bond with high cash-flow variability.
	- Exhibit 23-13 illustrates an [[Interest Rate and Yield Curve-Based Structured|inverse floater]] with high yields and significant [[Key Rates O1s Durations and Hedging|duration]] sensitivity.
- **Interest-Only (IO) and Principal-Only (PO) Tranches**:
  - IOs receive only interest payments and benefit from slower prepayments.
  - POs receive only principal payments and benefit from faster prepayments.
  - **Examples**:
	- Exhibit 23-16 shows an IO with high negative OAD.
	- Exhibit 23-17 shows a PO with [[Convexity|positive convexity]] and sensitivity to prepayment speeds.

## 3. Analysis of CMO Tranches
- **Cash-Flow Analysis**:
  - Examines sensitivity to prepayment speeds and [[How Countries Go Broke-Chapter 12 to Chapter 14|interest rate changes]].
  - Identifies [[Mortgage Pricing Spreads and Duration|negative convexity]] and potential extension risks.
- **Option-Adjusted Spread (OAS) Analysis**:
  - Evaluates relative value by comparing spreads over a [[Spread Duration and Dvo1|benchmark curve]] (e.g.,  Treasury or [[Determining the Expression for the Fair Value of the Swap Spread|swap curve]]).
  - Accounts for prepayment and interest rate variability.
- **[[Key Rates O1s Durations and Hedging|Hedging]]**:
  - [[Key Rates O1s Durations and Hedging|Duration]]-based [[Key Rates O1s Durations and Hedging|hedging]] is common for standard tranches.
  - Wide-window sequentials may require multi-point yield-curve [[Key Rates O1s Durations and Hedging|hedging]].
- **Investor Goals and Constraints**:
  - Banks prioritize shorter durations and manageable extension risks.
  - Insurance companies seek structured bonds to match liabilities.
  - Money managers focus on OAS and [[Class Note 10 Liquidity and Class Note 10 Liquidity and Liquidity Managementliquidity management|liquidity]].
  - [[Basis Trade Explainer|Hedge funds]] may engage in complex trades involving [[Chapter 9 Arbitrage and Hedging With Options|derivatives]].

## 4. Stripped Mortgage-Backed Securities (SMBS)
- **Types of SMBS**:
  - **Trust IOs and POs**:
	- Receive only interest or principal cash flows from underlying collateral.
  - **Structured IOs and POs**:
	- Created within CMO deals with synthetic high coupon rates.
- **[[An Asset Allocation Primer|Investment]] Characteristics**:
  - **POs**:
	- Bullish instruments that outperform in declining interest rate environments.
	- Sensitive to prepayment speeds.
  - **IOs**:
	- Bearish instruments that hedge against rising [[Interest Rate Quotations|interest rates]].
	- Negative [[Key Rates O1s Durations and Hedging|duration]] and sensitive to prepayment assumptions.
- **Prepayment Sensitivity**:
  - Exhibit 24-2 illustrates how prepayment speeds affect principal and interest cash flows.
  - Faster prepayments reduce interest cash flows but increase the present value of principal.
- **Price Performance**:
  - Exhibit 24-6 shows projected price paths for IOs and POs under parallel interest rate shifts.
  - IOs exhibit negative [[Key Rates O1s Durations and Hedging|duration]] initially,  while POs have large positive durations.
- **Effective [[An Analytical Decomposition of Forward Rates|Duration and Convexity]]**:
  - Exhibit 24-7 and Exhibit 24-8 demonstrate the [[An Analytical Decomposition of Forward Rates|duration and convexity]] profiles of IOs and POs.
  - [[PSET II Fixed Income Asset Pricing 1|Convexity]] indicates the rate of change in [[Key Rates O1s Durations and Hedging|duration]],  providing insights into price trends.
- **Option-Adjusted Spread (OAS) [[Arbitrage Pricing of Derivatives|Pricing]]**:
  - OAS analysis incorporates probabilistic methods to evaluate securities under varying interest rate paths.
  - The option cost reflects the impact of prepayment variability on the security's value.

## 5. Key Takeaways
- CMOs and SMBS offer tailored [[An Asset Allocation Primer|investment]] opportunities with varying risk,  return,  and cash-flow profiles.
- Prepayment behavior is a critical determinant of value and performance for both CMOs and SMBS.
- Analytical tools such as OAS,  [[Key Rates O1s Durations and Hedging|duration]],  and [[PSET II Fixed Income Asset Pricing 1|convexity]] are essential for evaluating these securities.
- [[Risk Preferences|Investor preferences]] and constraints drive the selection of specific tranches or structures.
- Understanding the interplay between [[Interest Rate Quotations|interest rates]],  prepayments,  and cash flows is crucial for effective [[An Asset Allocation Primer|investment]] and [[Financial Mathematics Course|risk management]].

This concludes the lecture notes on CMOs and SMBS. The next session will focus on advanced modeling techniques for prepayment and [[Forward Bond Yield|interest rate sensitivity]] analysis.

# Lecture Notes: Option Costs in Mortgage-Backed Securities (MBS) and Nonagency RMBS

## 1. Introduction to Option Costs in MBS
- **Definition of Option Costs**:
  - Option cost in the context of MBS refers to the impact of interest rate and prepayment variability on the value of the security.
  - It reflects the embedded prepayment option held by borrowers,  which allows them to refinance or prepay their mortgages when [[Interest Rate Quotations|interest rates]] decline.
- **Key Effects of Interest Rate and Prepayment Variations**:
  - **Effect 1: Callable Security Dynamics**:
	- When a callable security is prepaid in a low-interest-rate environment,  the principal is returned to the investor at par.
	- This is typically adverse for the investor because the principal would have been worth more than par in a low-rate environment.
	- The reinvestment of the returned principal occurs at lower yields,  reducing the investor's return.
	- **Exception**: [[Prepayment Modeling|Mortgage prepayments]] due to housing turnover may not align with economic incentives,  as they are driven by life events rather than interest rate movements.
  - **Effect 2: Discount or Premium [[Arbitrage Pricing of Derivatives|Pricing]]**:
	- For MBS priced at a discount or premium,  changes in prepayment speeds affect the timing of the discount or premium realization.
	- Faster prepayments result in earlier realization of the discount or premium,  while slower prepayments delay it.
	- This effect can either mitigate or amplify the adverse call effect discussed in Effect 1.
	- **Example**: Deep-discount securities like Principal-Only (PO) strips may benefit from faster prepayments,  as the earlier return of principal outweighs the negative call effect.
- **Relative Importance of the Two Effects**:
  - The first effect (call dynamics) is generally more significant than the second (timing of discount/premium realization).
  - However,  for certain securities like POs,  the second effect can dominate under specific conditions.

## 2. Option Costs in Different MBS Structures
- **Principal-Only (PO) Securities**:
  - POs benefit from faster prepayments because the principal is returned sooner,  increasing the present value of cash flows.
  - The option cost for POs is typically **negative**,  meaning they gain from [[Fixed Income Versus Equity Derivatives|interest rate volatility]].
  - **Key Insight**: The benefits of faster principal return outweigh the generic negative effects of being called in a low-rate environment.
- **Interest-Only (IO) Securities**:
  - IOs are highly sensitive to prepayment speeds,  as they receive only the interest portion of cash flows.
  - Faster prepayments reduce the interest cash flows,  leading to significant losses for IO investors.
  - The option cost for IOs is typically **positive** and large,  as they lose value in declining rate environments due to increased prepayments.
  - **Key Insight**: IOs gain little from rising rates (prepayments do not decrease significantly) but lose substantially from falling rates.
- **Underlying Collateral**:
  - The option cost for the underlying collateral is generally **positive**,  though smaller for discount collateral.
  - The negative effects of being called in low-rate environments outweigh the benefits of faster principal return.

## 3. Analysis of Option Costs Using Exhibit 24-9
- **Exhibit 24-9 [[Overview of Financial Markets|Overview]]**:
  - The exhibit illustrates the characteristics of SMBS backed by premium collateral,  such as FNMA IOs and POs.
  - Premium collateral introduces potential for both increases and decreases in prepayment speeds,  depending on the prevailing mortgage rates and coupon levels.
- **Option Costs for Premium Collateral**:
  - **Seasoned Premiums**:
	- Limited potential for substantial increases in prepayment speeds.
	- POs backed by seasoned premiums may exhibit a small but positive option cost.
  - **IOs Backed by Premium Collateral**:
	- Typically have a more positive option cost due to the asymmetric nature of prepayment changes.
- **Implications for [[Arbitrage Pricing of Derivatives|Pricing]]**:
  - Traditional yield-to-maturity measures are of limited relevance for SMBS.
  - [[Arbitrage Pricing of Derivatives|Pricing]] is typically conducted using Option-Adjusted Spread (OAS) analysis,  which accounts for prepayment variability and interest rate paths.

## 4. Key Takeaways on Option Costs
- **Prepayment Behavior**:
  - Prepayment speeds are the most critical determinant of MBS and SMBS value.
  - The asymmetric nature of prepayment changes creates distinct option cost profiles for IOs and POs.
- **Effective [[An Analytical Decomposition of Forward Rates|Duration and Convexity]]**:
  - POs exhibit large positive effective durations,  benefiting from declining rates.
  - IOs exhibit large negative effective durations,  losing value in declining rate environments.
- **[[An Asset Allocation Primer|Investment]] Strategies**:
  - POs are suitable for bullish interest rate environments,  where rates are expected to decline.
  - IOs are used as hedges against rising rates or as speculative instruments in bearish rate environments.
- **[[Arbitrage Pricing of Derivatives|Pricing]] Methodologies**:
  - OAS analysis is the preferred method for evaluating MBS and SMBS,  as it incorporates the probabilistic nature of prepayment and [[How Countries Go Broke-Chapter 12 to Chapter 14|interest rate changes]].

## 5. Example Problem: Option Costs in POs and IOs

:::{.callout-note}

#### Example: Option Costs in POs and IOs
**Problem Statement**:
Consider a Principal-Only (PO) and an Interest-Only (IO) security backed by the same pool of mortgages. The pool has a Weighted Average Coupon (WAC) of 5% and is currently priced at par. Analyze the impact of a 100 basis point decline in [[Interest Rate Quotations|interest rates]] on the option costs of the PO and IO securities.
:::

### Solution
1. **Breakdown of the Problem**:
   - Analyze the impact of a 100 bp decline in rates on prepayment speeds.
   - Assess how changes in prepayment speeds affect the cash flows of the PO and IO securities.
   - Calculate the option costs for each security.

1. **Step-by-Step Analysis**:
   - **Step 1: Impact on Prepayment Speeds**:
	 - A 100 bp decline in rates increases the incentive for borrowers to refinance,  leading to faster prepayments.
	 - Assume prepayment speeds increase from 10% CPR to 20% CPR.
   - **Step 2: Impact on PO Cash Flows**:
	 - Faster prepayments result in earlier return of principal for the PO security.
	 - The present value of cash flows increases due to the earlier timing,  benefiting the PO investor.
	 - **Option Cost for PO**: Negative,  as the PO gains value from increased prepayment speeds.
   - **Step 3: Impact on IO Cash Flows**:
	 - Faster prepayments reduce the interest cash flows received by the IO security.
	 - The present value of cash flows decreases significantly,  leading to losses for the IO investor.
	 - **Option Cost for IO**: Positive,  as the IO loses value from increased prepayment speeds.

1. **Mathematical Representation**:
   - Let the initial cash flows for the PO and IO securities be denoted as $$CF_{PO}$$ and $$CF_{IO}$$,  respectively.
   - The change in cash flows due to faster prepayments can be expressed as:
	 $$\Delta CF_{PO} = \text{Increase in Present Value of Principal Payments}$$
	 $$\Delta CF_{IO} = \text{Decrease in Present Value of Interest Payments}$$

1. **Conclusion**:
   - The PO security benefits from the 100 bp rate decline,  resulting in a negative option cost.
   - The IO security suffers losses,  resulting in a positive option cost.

## 6. Broader Implications
- **[[Financial Mathematics Course|Risk Management]]**:
  - Understanding option costs is critical for managing prepayment and interest rate risks in MBS portfolios.
  - Investors can use IOs and POs strategically to hedge against specific rate environments.
- **Market Dynamics**:
  - The asymmetric nature of prepayment changes creates opportunities for relative value trades between IOs,  POs,  and the underlying collateral.
- **Future Research**:
  - Explore the impact of non-linear [[Prepayment Modeling|prepayment models]] on option cost estimation.
  - Investigate the role of macroeconomic factors,  such as housing turnover and unemployment,  in shaping prepayment behavior.

This concludes the lecture notes on option costs in MBS and their implications for [[An Asset Allocation Primer|investment]] strategies. The next session will focus on the capital structures of nonagency RMBS and their role in managing credit and prepayment risks.

# Lecture Notes: Advanced Topics in Nonagency RMBS,  Covered Bonds,  and CMBS

## 1. Nonagency RMBS: Credit Enhancements and Collateral Performance Triggers

### 1.1 Credit Enhancements in Nonagency RMBS
- **Internal Credit Enhancements**:
  - Overcollateralization (OC): Excess collateral relative to the bond principal.
  - Excess Spread (XS): The difference between the interest earned on the collateral and the interest paid to bondholders.
  - Subordination: Junior tranches absorb losses before senior tranches.
- **External Credit Enhancements**:
  - **Pool Insurance**:
	- Covers losses due to fraud,  special hazards,  or [[Course Notes/HBR Notes/A Strategic Perspective on Bankruptcy|bankruptcy]] cramdowns.
	- Paid by lenders at the pool level.
  - **Letters of Credit (LOC)**:
	- Financial guarantees provided by banks.
	- Rarely used in recent years due to high costs.
  - **Reserve Funds**:
	- Cash deposits from issuance proceeds,  invested in money market instruments.
	- Common in auto ABS but less frequent in nonagency RMBS.
  - **Bond Insurance**:
	- Guarantees timely payment of principal and interest.
	- Provided by monoline insurers like MBIA,  Ambac,  and FGIC.
	- Covers implied write-downs,  where collateral value falls below bond principal.

### 1.2 Collateral Performance Triggers
- **Delinquency and Cumulative Loss Triggers**:
  - Designed to protect senior tranches by redirecting cash flows if performance deteriorates.
  - Common triggers include:
	- Delinquency rates exceeding a threshold.
	- Cumulative losses surpassing a predefined percentage.
- **Step-Down Date Mechanics**:
  - Junior bonds do not receive principal until:
	- The step-down date is reached.
	- Performance triggers are passed.
  - If triggers are breached,  cash flows are redirected to senior tranches.
  - **Real-World Implications**:
	- Many junior and mezzanine tranches were wiped out during the [[Squam Lake Group Letter|financial crisis]] due to large losses.

### 1.3 Complexity of OC/XS Structures
- **Comparison to Six-Pack Deals**:
  - OC/XS structures are more complex,  with additional triggers and volatile cash flows.
  - Small changes in collateral performance can lead to significant swings in [[Preview of the Book|cash flow]] waterfalls.
- **Floating-Rate Bonds**:
  - Introduce additional complications due to interest rate mismatches and [[Key Rates O1s Durations and Hedging|hedging]] requirements.
  - Increased uncertainty in [[Preview of the Book|cash flow]] projections makes analysis challenging.
- **Post-Crisis Trends**:
  - OC/XS structures have not been used in new issuances since the [[Squam Lake Group Letter|financial crisis]].

## 2. Housing Market Dynamics and Nonagency RMBS Performance

### 2.1 Housing Market as a Key Driver
- **Price Appreciation and Sales Volume**:
  - Home Price Appreciation (HPA) and Existing Home Sales (EHS) are critical indicators.
  - Early 2000s: Rapid growth with annualized HPA exceeding 10%.
  - Mid-2006: Sales slowed,  and prices began to decline,  leading to the housing bust.
- **Vicious Cycles During the Crisis**:
  - Declining prices discouraged buyers,  increasing distressed supply.
  - [[Class Note 10 Liquidity and Class Note 10 Liquidity and Liquidity Managementliquidity management|Liquidity]] crunch further weakened the market.
  - Resulted in the worst housing downturn in post-war U.S. history.

### 2.2 Geographic and Tier Segmentation
- **Geographic Segmentation**:
  - Home prices and sales vary significantly across regions,  states,  and metropolitan areas.
  - Historically low correlations between regions provided [[Week 8 Opportunities And Risks Of Investing Internationally|diversification benefits]].
  - During the crisis,  correlations spiked,  leading to fat-[[Lecture 6-[[Lecture 6-Leverage, Tail Risk, Volatility Products|Leverage]], Tail Risk, Volatility Products#6.6 [[Key Rates O1s Durations and Hedging|Hedging]] tail risks|tail risks]].
- **Property Tier Segmentation**:
  - Low-price homes appreciated faster but also depreciated more during the downturn.
  - High-price homes experienced less volatility,  contributing to lower delinquency rates in prime jumbo RMBS.

## 3. Covered Bonds: Structure,  Features,  and Global Adoption

### 3.1 Overview of Covered Bonds
- **Definition**:
  - Hybrid between [[Class Notes 2 – Corporate Bond Contracts|Corporate Bonds]] and [[Fremont Financial Corp. (b)|mortgage-backed securities]].
  - Dual recourse: Investors have claims on both the issuer and the collateral pool.
- **Historical Context**:
  - Originated in Europe (e.g.,  Germany's Pfandbriefe in 1769).
  - Gained popularity post-2008 as a robust alternative to MBS.

### 3.2 Types of Covered Bonds
- **Legislative Covered Bonds**:
  - Backed by specific laws granting [[Course Notes/HBR Notes/A Strategic Perspective on Bankruptcy|bankruptcy]] protection to collateral assets.
  - Example: German Pfandbrief Act ensures covered assets are excluded from insolvency proceedings.
- **Structured Covered Bonds**:
  - Use SPEs to achieve [[Course Notes/HBR Notes/A Strategic Perspective on Bankruptcy|bankruptcy]] protection in jurisdictions without specific legislation.
  - SPE guarantees bond repayment and holds legal title to the collateral pool.

### 3.3 Key Features
- **Credit Enhancements**:
  - Overcollateralization ensures asset value exceeds bond principal.
  - Dynamic cover pools allow for asset replacement to maintain [[Wellman Inc the Importance of Loan Covenants|credit quality]].
- **Maturity Structures**:
  - Hard Bullet: Fixed maturity date.
  - Soft Bullet: Allows maturity extension upon trigger events.
  - Conditional Pass-Through (CPT): Converts to pass-through structure upon issuer default.
- **Asset/Liability Mismatches**:
  - Controlled mismatches reduce [[Asset Backed Commercial Paper Understanding the Risks|liquidity risk]] and enhance ratings.

## 4. Commercial Mortgage-Backed Securities (CMBS)

### 4.1 CMBS Overview
- **Definition**:
  - [[Preview of the Book|Structured products]] providing [[Contemporary Financial Intermediation Notes|debt financing]] to the commercial real estate market.
  - Transfers [[Quantitative Trading Strategies Lecture Notes|credit risk]] of underlying loans to CMBS investors.
- **Types of CMBS**:
  - **Private-Label CMBS**:
	- Includes conduit transactions,  SASB deals,  and CRE Close.
  - **Agency CMBS**:
	- Issued by GSEs like Fannie Mae and Freddie Mac,  with government guarantees for senior tranches.

### 4.2 Valuation Techniques for Underlying Properties
- **Direct Capitalization Method**:
  - Property Value = Net [[BMW Valuation|Operating Income]] (NOI) / Cap Rate.
  - Cap rates vary by property type (e.g.,  multifamily properties have the lowest cap rates).
- **[[Lehman Brothers Option Adjusted Spread|Discounted Cash Flow]] (DCF) Analysis**:
  - Discounts future NOI using the weighted average cost of capital.
  - Less commonly used by CMBS investors due to data limitations.
- **Comparable Sales Method**:
  - Values properties based on recent sales of similar assets.
- **Replacement Cost Method**:
  - Values properties based on land and construction costs minus depreciation.

### 4.3 Loan Structures and Features
- **Key Metrics**:
  - Loan-to-Value (LTV): Typically 55%-75% post-crisis.
  - [[Notes on Currency Swaps|Debt Service]] Coverage Ratio (DSCR): Minimum of 1.2x.
  - Debt Yield: Annual NOI divided by loan balance,  typically 9%-10%.
- **Structural Features**:
  - Single-purpose entities isolate collateral.
  - Reserve accounts for taxes,  insurance,  and property improvements.
  - Lockbox structures manage cash flows and mitigate borrower risks.
  - Prepayment restrictions include defeasance or yield maintenance charges.

### 4.4 CMBS Trust Structure
- **Participants**:
  - Trustee: Administers trust assets and distributes payments.
  - Master Servicer: Manages loan collections and escrows.
  - Special Servicer: Handles distressed loans and loss mitigation.
  - Operating Advisor: Provides oversight of the special servicer.
- **[[Introduction to Corporate Finance|Capital Structure]]**:
  - Post-crisis CMBS have simplified structures with thicker tranches to withstand defaults.
  - Subordination levels provide credit protection to senior tranches.

## 5. Key Takeaways

### 5.1 Nonagency RMBS
- Credit enhancements and performance triggers are critical for managing prepayment and credit risks.
- [[US Debt Crisis and Adjustment (2007–2011)|Housing market]] dynamics,  including geographic and tier segmentation,  significantly impact RMBS performance.

### 5.2 Covered Bonds
- Provide a robust alternative to MBS with dual recourse and controlled asset/liability mismatches.
- Legislative and structured covered bonds cater to different jurisdictions.

### 5.3 CMBS
- Valuation of underlying properties and loan structures are essential for credit [[Week 3 [[Week 3 Financial Risk Analysis|Financial Risk Analysis]]|[[Week 3 Financial Risk Analysis|risk analysis]]]].
- Post-crisis CMBS structures emphasize simplicity and resilience to defaults.

This concludes the lecture notes on advanced topics in nonagency RMBS,  covered bonds,  and CMBS. The next session will focus on prepayment modeling and [[Banks' Bonds Playing Role as I|risk management strategies]] in [[A Primer on Structured Finance|structured finance]].

# Lecture Notes: CMBS,  Credit Card ABS,  and Non-Mortgage ABS

## 1. Introduction to CMBS (Commercial Mortgage-Backed Securities)
- **Definition and Purpose**:
  - CMBS are securities backed by commercial real estate loans,  providing [[Contemporary Financial Intermediation Notes|debt financing]] to the commercial real estate market.
  - They [[Credit Default Swaps|transfer credit risk]] from lenders to investors,  offering a structured way to invest in commercial real estate debt.
- **Historical Context**:
  - The CMBS market emerged in the early 1990s to dispose of commercial real estate loans owned by the Resolution Trust Corporation (RTC) after the savings and loan crisis.
  - The market grew rapidly,  peaking in 2007 before the [[Squam Lake Group Letter|financial crisis]] caused a significant contraction.

## 2. CMBS Transaction Features
- **Standard Features**:
  - CMBS transactions generally include features such as subordination,  risk retention,  and priority of payments.
  - These features have evolved since the 1990s to meet investor demands and regulatory requirements.

### 2.1 Subordination and Risk Retention
- **[[Introduction to Corporate Finance|Capital Structure]]**:
  - CMBS certificates are structured along time and credit dimensions to create a "capital stack" with varying [[Lecture 7-Risk and Return of Bonds|risk and return]] profiles.
  - Senior certificates have priority for principal payments and are the shortest in maturity,  while junior certificates absorb losses first.
- **Subordination Rates**:
  - Defined as the percentage of the collateral balance that must experience a complete principal write-down before a certificate is exposed to loss.
  - Senior certificates have the highest subordination rates,  providing greater credit protection.
- **Risk Retention ([[Note on The [[Credit Derivative Indexes|Dodd-Frank Act]] and Its Impact|[[Note on The Dodd-Frank Act and Its Impact|Dodd-Frank]]]] Act)**:
  - Requires sponsors to retain 5% of the market value of a transaction to align their interests with investors.
  - Retention methods include:
	- Vertical: Retaining a piece of every security in the [[Introduction to Corporate Finance|capital structure]].
	- Horizontal: Retaining the most junior 5% first-loss tranche.
	- L-shaped: A combination of vertical and horizontal retention.

### 2.2 Priority of Payments
- **Waterfall Structure**:
  - Principal payments are allocated sequentially from the top of the [[Introduction to Corporate Finance|capital structure]] to the bottom.
  - Losses are allocated in reverse order,  starting from the bottom of the capital stack.
- **Interest Payments**:
  - Allocated pro-rata to senior AAA certificates and the IO tranche,  then sequentially to other certificates.

### 2.3 Interest-Only (IO) Certificates
- **Characteristics**:
  - IO tranches receive excess interest from the collateral pool after all non-IO tranches have been paid.
  - The notional balance of IO tranches may be based on the aggregate balance of AAA tranches or the entire transaction.

## 3. CMBS Market Development
- **Growth and Contraction**:
  - The CMBS market grew rapidly in the 1990s and early 2000s,  peaking at $228 billion in issuance in 2007.
  - The [[Squam Lake Group Letter|financial crisis]] caused a sharp decline,  with no private-label transactions issued until late 2009.
- **Post-Crisis Trends**:
  - The private-label CMBS market has stabilized at $70–$100 billion annually but has not returned to pre-crisis levels.
  - Agency CMBS,  backed by government-sponsored entities,  has gained market share.

## 4. Credit Card ABS (Asset-Backed Securities)
- **Definition and Purpose**:
  - Credit card ABS are securities backed by credit card receivables,  providing funding for credit card issuers.
  - They allow issuers to diversify funding sources and remove assets from their balance sheets.

### 4.1 Structure of Credit Card ABS
- **Master Trust Structure**:
  - A single trust accepts periodic additions of accounts and issues multiple series of securities.
  - All securities are supported by the [[Notes on Currency Swaps|interest and principal]] collections from the entire collateral pool.
- **Revolving and Amortization Periods**:
  - During the revolving period,  principal collections are reinvested in new receivables.
  - In the amortization period,  principal collections are used to repay investors.

### 4.2 Credit Enhancement
- **Excess Spread**:
  - The first line of defense against losses,  calculated as the finance charge [[Preview of the Book|cash flow]] remaining after covering bond coupons,  servicing fees,  and charge-offs.
- **Subordination**:
  - Junior tranches provide [[Class Note On Securitization(1)|credit enhancement]] for senior tranches.
- **Cash Collateral Accounts (CCA)**:
  - Reserve accounts funded at closing to cover shortfalls in [[Preview of the Book|cash flow]].

### 4.3 Key Variables for Analysis
- **[[An Asset Allocation Primer|Portfolio]] Yield**:
  - Measures income generated by the receivables,  driven by APR,  fees,  and usage patterns.
- **Charge-Off Rate**:
  - Represents credit losses,  typically taken when accounts are 180 days past due.
- **Monthly Payment Rate (MPR)**:
  - Indicates the percentage of principal repaid each month,  with higher MPRs providing implied [[Class Note On Securitization(1)|credit enhancement]].

## 5. Non-Mortgage ABS: Auto Loans,  Equipment Loans,  and Student Loans
- **Definition and Purpose**:
  - Non-mortgage ABS are securities backed by financial assets such as auto loans,  equipment leases,  and student loans.
  - They provide issuers with direct access to capital markets while isolating assets from [[Course Notes/HBR Notes/A Strategic Perspective on Bankruptcy|bankruptcy]] risk.

### 5.1 Securitization Process
- **[[Collateralized Debt Obligations|Special Purpose Vehicle]] (SPV)**:
  - Assets are sold to an SPV to achieve [[Course Notes/HBR Notes/A Strategic Perspective on Bankruptcy|bankruptcy]] remoteness.
  - The SPV issues securities backed by the cash flows from the assets.
- **[[Class Note On Securitization(1)|Credit Enhancement]]**:
  - Includes excess spread,  subordination,  and reserve accounts to absorb potential losses.

### 5.2 Key Asset Classes
- **Auto Loans and Leases**:
  - Backed by prime and subprime auto loans,  with varying levels of [[Class Note On Securitization(1)|credit enhancement]] based on expected losses.
- **Equipment Loans and Leases**:
  - Backed by loans and leases for equipment,  often with strong collateral values.
- **Student Loans**:
  - Backed by private and government-guaranteed student loans,  with performance influenced by borrower repayment behavior.

## 6. Key Takeaways
- **CMBS**:
  - CMBS transactions are structured to protect senior investors while providing flexibility in [[Preview of the Book|cash flow]] allocation.
  - The market has evolved significantly since the [[Squam Lake Group Letter|financial crisis]],  with increased regulatory oversight and simplified structures.
- **Credit Card ABS**:
  - Credit card ABS rely on master trust structures to manage the revolving nature of receivables.
  - Excess spread and subordination are critical for [[Class Note On Securitization(1)|credit enhancement]] and investor protection.
- **Non-Mortgage ABS**:
  - [[10. Other Topics in Quantitative Finance|Securitization]] provides issuers with access to capital markets while isolating assets from [[Course Notes/HBR Notes/A Strategic Perspective on Bankruptcy|bankruptcy]] risk.
  - [[Class Note On Securitization(1)|Credit enhancement]] and asset quality are key determinants of ABS performance.

This concludes the lecture notes on CMBS,  Credit Card ABS,  and Non-Mortgage ABS. The next session will focus on advanced modeling techniques for analyzing ABS cash flows and credit risks.

# Lecture Notes: Asset-Backed Securities (ABS) and Credit Enhancement Mechanisms

## 1. Introduction to Asset-Backed Securities (ABS)
- **Definition and Purpose**:
  - [[Asset Backed Commercial Paper Understanding the Risks|Asset-Backed]] Securities (ABS) are [[A Practical Guide for Actuaries and other Business Professionals.|financial instruments]] backed by pools of loans,  leases,  or receivables,  such as auto loans,  credit card receivables,  equipment leases,  and student loans.
  - The [[Teaching Note 6 Mortgage Backed Securities|securitization process]] transforms [[Class Note 10 Liquidity and Class Note 10 Liquidity and Liquidity Managementliquidity management|illiquid assets]] into tradable securities,  providing issuers with funding and investors with diversified [[An Asset Allocation Primer|investment]] opportunities.
- **Key Features**:
  - ABS transactions are structured to isolate the underlying assets from the originator's [[Course Notes/HBR Notes/A Strategic Perspective on Bankruptcy|bankruptcy]] risk,  enabling the securities to achieve higher credit ratings than the originator.
  - [[Class Note On Securitization(1)|Credit enhancement]] mechanisms are employed to protect investors from losses and ensure timely payments.

## 2. Credit Enhancement in ABS Transactions
- **[[Overview of Financial Markets|Overview]]**:
  - [[Class Note On Securitization(1)|Credit enhancement]] refers to techniques used to reduce the risk of loss to investors in ABS transactions.
  - It can be categorized into **internal sources** and **external sources**.

### 2.1 External Credit Enhancement
- **Definition**:
  - External [[Class Note On Securitization(1)|credit enhancement]] involves third-party guarantees or insurance to protect investors.
- **Types**:
  - **Bond Insurance**:
	- Guarantees timely payment of principal and interest.
	- Links the ABS rating to the credit rating of the guarantor.
	- Fell out of favor after the 2008–2009 [[Squam Lake Group Letter|financial crisis]] due to stress on insurers.
  - **Corporate Guarantees**:
	- Provided by the originator or a third party.
	- Links the ABS rating to the guarantor's creditworthiness.
- **Decline in Usage**:
  - The [[Squam Lake Group Letter|financial crisis]] exposed vulnerabilities in external [[Class Note On Securitization(1)|credit enhancement]],  leading to a shift toward internal mechanisms.

### 2.2 Internal Credit Enhancement
- **Definition**:
  - Internal [[Class Note On Securitization(1)|credit enhancement]] relies on structural features within the ABS deal to absorb losses.
- **Types**:
  - **Excess Spread**:
	- The difference between the interest collected on the collateral and the interest paid to bondholders,  after covering expenses.
	- Acts as the first line of defense against losses.
	- Unused excess spread may be trapped in a reserve account or returned to the servicer.
  - **Cash Reserve Account**:
	- A reserve fund established at closing or funded over time using excess spread.
	- Provides [[Class Note 10 Liquidity and Class Note 10 Liquidity and Liquidity Managementliquidity management|liquidity]] to cover shortfalls in interest or principal payments.
	- May include release conditions tied to credit performance metrics.
  - **Overcollateralization (OC)**:
	- The value of the collateral pool exceeds the value of the ABS issued.
	- Example:
	  - If the collateral pool is $500 million and the ABS issued is $450 million,  the OC is $50 million (10% of the pool).
	- Represents the "first loss" piece,  aligning the originator's interests with investors.
  - **Subordination**:
	- Junior tranches absorb losses before senior tranches.
	- Allows issuers to tailor securities to investors with different risk appetites.
	- Subordinated tranches are often rated from AA to BBB,  with BB-rated tranches at the bottom of the [[Introduction to Corporate Finance|capital structure]].

## 3. Credit Analysis of ABS
- **Focus Areas**:
  - The primary focus is on the performance of the collateral pool,  though the originator's servicing capabilities are also important.
- **Key Metrics**:
  - **Delinquency Rates**:
	- Signal potential future losses,  especially for loans delinquent for more than 60 days.
  - **Defaults and Net Losses**:
	- Used to determine [[Class Note On Securitization(1)|credit enhancement]] levels.
  - **Loss Severity/Recovery Rates**:
	- Measure the extent of losses after defaults.
  - **[[Mortgage Pools|Prepayment Rates]]**:
	- Variations from expected prepayment levels can significantly affect ABS valuation.
  - **Clean-Up Call**:
	- Allows the issuer to call the collateral pool when its balance falls below a predetermined level (e.g.,  5%–15% of the original balance).
	- Reduces servicing costs for the issuer.

## 4. Auto Loans and Leases
- **[[Overview of Financial Markets|Overview]]**:
  - Auto ABS is one of the earliest and most active [[10. Other Topics in Quantitative Finance|securitization]] sectors,  with issuance averaging $80 billion annually since 2012.
  - Includes loans and leases to both prime and subprime borrowers.
- **Key Trends**:
  - Growth in subprime auto loans and auto lease ABS.
  - Subprime auto ABS outstanding increased from $16.3 billion in 2011 to $52.3 billion in 2018.
  - Auto lease ABS outstanding rose from $12.7 billion in 2011 to $25.0 billion in 2018.

### 4.1 Auto ABS Structure
- **Owner Trust Structure**:
  - Allows for time [[Class Note On Securitization(1)|tranching]] of senior classes and credit [[Class Note On Securitization(1)|tranching]] of subordinated debt.
  - Senior classes are divided into sequential tranches with varying maturities.
- **Example Structure**:
  - Class A1: Short average life,  eligible for money market investors.
  - Class A2: Largest tranche,  with a principal payment window of 8–16 months.
  - Last [[Preview of the Book|Cash Flow]] (LCF) Senior Bond: Longer average life,  subject to greater variability.
  - Subordinated Classes: Rated from AA to BBB,  absorbing losses before senior classes.
- **Prepayment and Default Risks**:
  - Monthly principal payments create "payment windows" for each tranche.
  - Prepayments,  defaults,  and clean-up calls affect the return of principal to investors.

### 4.2 Subprime Auto ABS
- **Characteristics**:
  - Higher [[Class Note On Securitization(1)|credit enhancement]] levels due to increased [[Default Risk and Credit Derivatives 183|default risk]].
  - Example:
	- Prime auto loan ABS may require 35% [[Class Note On Securitization(1)|credit enhancement]] for a AAA rating.
	- Subprime auto loan ABS may require up to 65% [[Class Note On Securitization(1)|credit enhancement]].
  - Servicer risk is significant,  as subprime lenders often rely heavily on ABS funding.

## 5. Auto Lease ABS
- **[[Overview of Financial Markets|Overview]]**:
  - Leasing has become more popular due to rising vehicle prices and financing costs.
  - Lease penetration rates increased to 30% in 2018–2019 from less than 20% before 2008.
- **Key Risks**:
  - **Residual Value Risk**:
	- The primary risk is the realization of residual values at lease maturity.
	- Residual collections account for more than 50% of cash flows in auto lease ABS.
	- Stress scenarios include a decline in used car prices by 11%–12%.
  - **[[Class Note On Securitization(1)|Credit Enhancement]]**:
	- Sized to account for potential residual value declines.
	- Auto lease ABS typically price at a concession to auto loan ABS due to residual value risk.

## 6. Equipment Loans and Leases
- **[[Overview of Financial Markets|Overview]]**:
  - Equipment ABS includes loans and leases for small-ticket,  mid-ticket,  and large-ticket equipment.
  - Outstanding equipment ABS rose from $37.1 billion in 2011 to $64.3 billion in 2018.
- **Key Risks**:
  - Residual value risk is significant for lease transactions.
  - Servicer risk is higher for smaller specialty finance firms.
- **Categories**:
  - **Small-Ticket Equipment**:
	- Includes items like computers and copiers,  with diverse pools.
  - **Mid-Ticket Equipment**:
	- Includes medical equipment and heavy-duty trucks,  with some obligor concentration.
  - **Large-Ticket Equipment**:
	- Includes agricultural and construction equipment,  with lower net loss rates.

## 7. Student Loans
- **[[Overview of Financial Markets|Overview]]**:
  - Student loan ABS became the largest ABS sector in 2010,  driven by government-guaranteed loans under the Federal Family Education Loan Program (FFELP).
  - Outstanding student loan ABS declined to $171 billion in 2018 after the FFELP program ended.
- **Categories**:
  - **Government-Guaranteed Loans**:
	- Carry a federal guarantee covering up to 97% of the loan balance.
	- Include Stafford,  PLUS,  and consolidation loans.
  - **Private Student Loans**:
	- Carry no federal guarantee and are more similar to consumer credit.
	- Higher risk due to direct-to-consumer disbursement and lack of [[Course Notes/HBR Notes/A Strategic Perspective on Bankruptcy|bankruptcy]] discharge.
- **Key Risks**:
  - **[[Quantitative Trading Strategies Lecture Notes|Credit Risk]]**:
	- Mitigated by excess spread,  overcollateralization,  and subordination.
  - **[[Asset Backed Commercial Paper Understanding the Risks|Liquidity Risk]]**:
	- Addressed through capitalized interest accounts and reserve funds.
  - **Interest Rate and [[Lessons From The Crisis|Basis Risk]]**:
	- Arises from mismatches between loan and ABS [[Interest Rate Quotations|interest rates]].
  - **Servicer Risk**:
	- Critical for both government-guaranteed and private student loans.

## 8. Key Takeaways
- **[[Class Note On Securitization(1)|Credit Enhancement]]**:
  - Internal mechanisms like excess spread,  cash reserve accounts,  overcollateralization,  and subordination are critical for protecting ABS investors.
- **Sector-Specific Risks**:
  - Auto ABS: Prepayment and residual value risks.
  - Equipment ABS: Residual value and servicer risks.
  - Student Loan ABS: [[Class Note 10 Liquidity and Class Note 10 Liquidity and Liquidity Managementliquidity management|Liquidity]],  interest rate,  and servicer risks.
- **Market Trends**:
  - Growth in subprime auto loans and private student loans reflects changing consumer credit dynamics.
  - Credit analysis remains focused on collateral performance and structural protections.

This concludes the lecture notes on ABS and [[Class Note On Securitization(1)|credit enhancement]] mechanisms. The next session will focus on collateralized loan obligations (Close) and their structural features.

# Lecture Notes: Yield-Curve Analysis and Forward Rate Applications

## 1. Introduction to Yield-Curve Analysis
- **Definition and Importance**:
  - The yield curve represents the relationship between bond yields and their maturities. It is a critical tool for understanding [[Forward Rate|market expectations]],  risk premiums,  and the [[PSET II Fixed Income Asset Pricing 1|convexity]] bias.
  - Forward rates,  derived from the yield curve,  provide insights into [[Forward Rate|market expectations]] for future [[Interest Rate Quotations|interest rates]] and are essential for active [[The Impact of Option Strategies in Financial  Portfolios Performance|portfolio management]] and yield-curve trades.
- **Key Determinants of the Yield Curve**:
  - **[[UNDERSTANDING THE YIELD CURVE- PART 2|Market Rate Expectations]]**:
	- [[FORWARD RATES AND TERM STRUCTURE|Expectations]] about future [[Interest Rate Quotations|interest rates]] are the primary driver of the yield curve's shape.
	- Rising rate [[FORWARD RATES AND TERM STRUCTURE|expectations]] lead to an upward-sloping curve,  while falling rate [[FORWARD RATES AND TERM STRUCTURE|expectations]] result in an inverted curve.
  - **Bond Risk Premiums**:
	- Investors demand higher [[Assets|returns]] for holding longer-term bonds due to increased risk,  contributing to an upward-sloping curve.
  - **[[PSET II Fixed Income Asset Pricing 1|Convexity]] Bias**:
	- The non-linear relationship between bond prices and yields makes high-[[PSET II Fixed Income Asset Pricing 1|convexity]] bonds more valuable,  influencing the curve's shape,  especially at long maturities.
- **Practical Applications**:
  - Forward rates can be used for break-even analysis,  identifying cheap maturity sectors,  and constructing relative-value trades.

## 2. Forward Rates as Break-Even Rates
- **Concept**:
  - Forward rates represent the break-even future rates at which an investor neither gains nor loses money relative to the current yield curve.
  - They incorporate the impact of carry (the income earned from holding a bond) on trade profitability.
- **Application**:
  - **Bearish [[An Asset Allocation Primer|Portfolio]] Position**:
	- A manager should take a bearish position only if they expect rates to rise more than implied by forward rates.
  - **Bullish [[An Asset Allocation Primer|Portfolio]] Position**:
	- If rates are expected to rise but by less than the forward rates imply,  a bullish position is more profitable due to positive carry.
- **Key Insights**:
  - Forward rates provide an objective benchmark for evaluating subjective yield-curve scenarios.
  - They are independent of assumptions about [[FORWARD RATES AND TERM STRUCTURE|expectations]],  risk premiums,  or [[PSET II Fixed Income Asset Pricing 1|convexity]] bias.
- **Example**:
  - If forward rates imply a 50 basis point rise in yields over the next year,  a bearish position is profitable only if the manager expects rates to rise by more than 50 basis points.

## 3. Forward Rates as Indicators of Cheap Maturity Sectors
- **Concept**:
  - Forward rates magnify differences in value across maturity sectors,  making it easier to identify cheap or rich sectors compared to spot or par rates.
- **Application**:
  - **Identifying Cheap Sectors**:
	- High forward rates indicate cheap sectors,  while low forward rates suggest rich sectors.
  - **Exploiting Cheapness**:
	- Investors can buy bonds maturing at the end of a cheap sector and sell bonds maturing at the beginning,  capturing the higher [[Forward Points in Currency|forward rate]].
- **Example**:
  - In August 2000,  the par yield curve was flat,  but forward rates revealed the 9to 12-year sector as cheap. A trade buying 12-year bonds and selling 9-year bonds would exploit this cheapness.
- **Considerations**:
  - Forward rates may reflect temporary local cheapness,  which can lead to capital gains as the forward curve flattens and the cheap sector richens.

## 4. Forward Rates as Relative-Value Tools for Yield-Curve Trades
- **Concept**:
  - Forward rates can be used to construct quantitative indicators for [[Key Rates O1s Durations and Hedging|duration]]-neutral trades,  such as barbell-bullet trades.
- **Application**:
  - **[[Key Rates O1s Durations and Hedging|Duration]] Extensions**:
	- When the yield curve is steep,  long-term bonds' yield advantage provides a cushion against rising rates,  making [[Key Rates O1s Durations and Hedging|duration]] extensions "cheap."
  - **Curve-Flattening Trades**:
	- When the yield curve is concave,  flattening trades earn a negative carry,  and higher concavity indicates less attractive terms for flattening trades.
- **Example**:
  - In October 2003,  high yield-curve curvature implied strong flattening [[FORWARD RATES AND TERM STRUCTURE|expectations]]. However,  a steepener (bullet) outperformed a barbell due to its initial carry and rolldown advantage,  despite subsequent curve flattening.

## 5. Decomposing Forward Rates into Determinants
- **Components of Forward Rates**:
  - **Rate [[FORWARD RATES AND TERM STRUCTURE|Expectations]]**:
	- Reflect the market's view of future [[Interest Rate Quotations|interest rates]].
  - **Bond Risk Premium**:
	- The additional return required by investors for holding long-term bonds.
  - **[[PSET II Fixed Income Asset Pricing 1|Convexity]] Bias**:
	- The impact of [[PSET II Fixed Income Asset Pricing 1|convexity]] on bond prices,  especially at long maturities.
- **Mathematical Decomposition**:
  - The one-period [[Forward Points in Currency|forward rate]] can be expressed as:
	$$ f_{n-1,  n} \approx \text{short rate} + \text{duration} \times \mathbb{E}(\Delta s_{n-1}) + \text{bond risk premium} + \text{convexity bias} $$

- **Example**:
  - Using [[Theory Meets Data - Asset Pricing Puzzles|historical average returns]] and volatilities,  forward rates can be decomposed to infer [[Forward Rate|market expectations]],  risk premiums,  and [[PSET II Fixed Income Asset Pricing 1|convexity]] bias.

## 6. Practical Applications of Forward Rates
- **[[Week 4 Valuing Young and High‐Growth Companies|Scenario Analysis]]**:
  - Forward rates can be used to evaluate bond positions under different yield-curve scenarios.
  - Example: A [[An Asset Allocation Primer|portfolio]] of zero-coupon bonds can be analyzed for expected [[Assets|returns]] under parallel shifts,  curve flattening,  or steepening scenarios.
- **[[Lecture 1- Probability Distributions of Returns|Expected Return]] Decomposition**:
  - The [[Lecture 1- Probability Distributions of Returns|expected return]] of a bond can be broken into:
	- Yield income
	- Rolldown return
	- Value of [[PSET II Fixed Income Asset Pricing 1|convexity]]
	- [[Key Rates O1s Durations and Hedging|Duration]] impact of rate views
  - Example: A barbell strategy combining shortand long-[[Key Rates O1s Durations and Hedging|duration]] bonds can be evaluated for its [[Lecture 1- Probability Distributions of Returns|expected return]] components.
- **Relative-Value Analysis**:
  - Forward rates provide a framework for comparing bonds based on their expected [[Assets|returns]] rather than just yield spreads.
  - Example: A five-term [[Lecture 1- Probability Distributions of Returns|expected return]] measure includes yield income,  rolldown return,  [[PSET II Fixed Income Asset Pricing 1|convexity]] value,  [[Key Rates O1s Durations and Hedging|duration]] impact,  and local rich/cheap effects.

## 7. Key Takeaways
- **Forward Rates as Tools**:
  - Forward rates are essential for break-even analysis,  identifying cheap sectors,  and constructing relative-value trades.
  - They provide a systematic framework for analyzing yield-curve trades and expected [[Assets|returns]].
- **Yield-Curve Determinants**:
  - The shape of the yield curve reflects a combination of rate [[FORWARD RATES AND TERM STRUCTURE|expectations]],  bond risk premiums,  and [[PSET II Fixed Income Asset Pricing 1|convexity]] bias.
  - Understanding these determinants is critical for interpreting forward rates and making informed [[An Asset Allocation Primer|investment]] decisions.
- **Practical Implications**:
  - Investors can use forward rates to align their [[Lecture Notes Bonds,  Preferred Stock,  and Structured Products|portfolio strategies]] with [[Forward Rate|market expectations]] and exploit relative value opportunities.
  - [[Week 4 Valuing Young and High‐Growth Companies|Scenario analysis]] and [[Lecture 1- Probability Distributions of Returns|expected return]] decomposition provide deeper insights into bond positions and their drivers of return.

This concludes the lecture notes on yield-curve analysis and [[Forward Points in Currency|forward rate]] applications. The next session will focus on advanced techniques for modeling yield-curve dynamics and their implications for [[The Impact of Option Strategies in Financial  Portfolios Performance|portfolio management]].

# Lecture Notes: Yield-Curve Analysis,  Forward Rates,  and Principal Component Analysis

## 1. Introduction to Yield-Curve Analysis
- **Definition and Importance**:
  - The yield curve represents the relationship between bond yields and their maturities. It is a critical tool for understanding [[Forward Rate|market expectations]],  risk premiums,  and [[PSET II Fixed Income Asset Pricing 1|convexity]] bias.
  - Forward rates,  derived from the yield curve,  provide insights into [[Forward Rate|market expectations]] for future [[Interest Rate Quotations|interest rates]] and are essential for active [[The Impact of Option Strategies in Financial  Portfolios Performance|portfolio management]] and yield-curve trades.
- **Key Determinants of the Yield Curve**:
  - **[[UNDERSTANDING THE YIELD CURVE- PART 2|Market Rate Expectations]]**:
	- [[FORWARD RATES AND TERM STRUCTURE|Expectations]] about future [[Interest Rate Quotations|interest rates]] are the primary driver of the yield curve's shape.
	- Rising rate [[FORWARD RATES AND TERM STRUCTURE|expectations]] lead to an upward-sloping curve,  while falling rate [[FORWARD RATES AND TERM STRUCTURE|expectations]] result in an inverted curve.
  - **Bond Risk Premiums**:
	- Investors demand higher [[Assets|returns]] for holding longer-term bonds due to increased risk,  contributing to an upward-sloping curve.
  - **[[PSET II Fixed Income Asset Pricing 1|Convexity]] Bias**:
	- The non-linear relationship between bond prices and yields makes high-[[PSET II Fixed Income Asset Pricing 1|convexity]] bonds more valuable,  influencing the curve's shape,  especially at long maturities.
- **Practical Applications**:
  - Forward rates can be used for break-even analysis,  identifying cheap maturity sectors,  and constructing relative-value trades.

## 2. Forward Rates and Their Decomposition
- **Forward Rates as Break-Even Rates**:
  - Forward rates represent the break-even future rates at which an investor neither gains nor loses money relative to the current yield curve.
  - They incorporate the impact of carry (the income earned from holding a bond) on trade profitability.
- **Mathematical Representation**:
  - The [[Forward Points in Currency|forward rate]] between two maturities,  $$f_{m,  n}$$,  can be derived from spot rates $$s_m$$ and $$s_n$$ using the formula:
	$$ \left(1 + \frac{f_{m,  n}}{100}\right)^{n-m} = \frac{\left(1 + \frac{s_n}{100}\right)^n}{\left(1 + \frac{s_m}{100}\right)^m} $$

- **Components of Forward Rates**:
  - **Rate [[FORWARD RATES AND TERM STRUCTURE|Expectations]]**:
	- Reflect the market's view of future [[Interest Rate Quotations|interest rates]].
  - **Bond Risk Premium**:
	- The additional return required by investors for holding long-term bonds.
  - **[[PSET II Fixed Income Asset Pricing 1|Convexity]] Bias**:
	- The impact of [[PSET II Fixed Income Asset Pricing 1|convexity]] on bond prices,  especially at long maturities.
- **[[Lecture 1- Probability Distributions of Returns|Expected Return]] Decomposition**:
  - The [[Lecture 1- Probability Distributions of Returns|expected return]] of a bond can be broken into:
	- Yield income
	- Rolldown return
	- Value of [[PSET II Fixed Income Asset Pricing 1|convexity]]
	- [[Key Rates O1s Durations and Hedging|Duration]] impact of rate views

## 3. Principal Component Analysis (PCA) of Yield-Curve Dynamics
- **[[Overview of Financial Markets|Overview]] of PCA**:
  - PCA is a statistical method used to identify the dominant patterns (or "vibration modes") in yield-curve movements.
  - It simplifies the analysis of yield-curve dynamics by reducing the dimensionality of the data.
- **Key Findings from PCA**:
  - **First Principal Component (Level Shift)**:
	- Explains the majority of the variance in bond yields (e.g.,  92% for U.S. Treasury yields).
	- Represents a nearly parallel shift in the yield curve.
  - **Second Principal Component (Slope Shift)**:
	- Explains a smaller portion of the variance (e.g.,  5%).
	- Represents a steepening or flattening of the yield curve.
  - **Third Principal Component (Curvature Shift)**:
	- Explains even less variance (e.g.,  1%).
	- Represents a hump-shaped shift,  often peaking at intermediate maturities.
- **Empirical Observations**:
  - The first two [[Principal Component Analysis|principal components]] are relatively stable over time and across countries.
  - The third and higher-order components are less stable and more dependent on the specific dataset.
- **Applications of PCA**:
  - **[[Financial Mathematics Course|Risk Management]]**:
	- The first two components capture most of the yield-curve risk,  allowing for simplified risk measures like [[Key Rates O1s Durations and Hedging|duration]] and slope [[Key Rates O1s Durations and Hedging|duration]].
  - **[[Exercises|Portfolio Construction]]**:
	- PCA helps identify the key drivers of bond [[An Asset Allocation Primer|portfolio]] [[Assets|returns]] and informs [[Key Rates O1s Durations and Hedging|hedging]] strategies.

## 4. Example Problem: Decomposing Forward Rates into Components

:::{.callout-note}

#### Example: Decomposing Forward Rates
**Problem Statement**:
Given a one-year [[Forward Points in Currency|forward rate]] $$f_{n-1,  n}$$,  decompose it into its components: bond risk premium,  rate [[FORWARD RATES AND TERM STRUCTURE|expectations]],  and [[PSET II Fixed Income Asset Pricing 1|convexity]] bias. Assume the following:
- $$f_{n-1,  n} = 3.5\%$$
- $$s_1 = 2.0\%$$ (one-year [[The Foreign Exchange Market Annotations|spot rate]])
- $$\mathrm{dur}_{n-1} = 5$$ ([[Key Rates O1s Durations and Hedging|duration]] of the bond at the end of the horizon)
- $$\mathrm{vol}(\Delta s_{n-1}) = 0.2\%$$ (volatility of the yield change)
- $$E(\Delta s_{n-1}) = -0.1\%$$ (expected yield change)
- $$C x_{n-1} = 0.8$$ ([[PSET II Fixed Income Asset Pricing 1|convexity]] of the bond at the end of the horizon)
:::

### Solution
1. **Breakdown of the Problem**:
   - Decompose $$f_{n-1,  n}$$ into:
	 - Bond risk premium ($$BRP_n$$)
	 - Rate [[FORWARD RATES AND TERM STRUCTURE|expectations]] ($$E(\Delta s_{n-1})$$)
	 - [[PSET II Fixed Income Asset Pricing 1|Convexity]] bias ($$CB_n$$)

1. **Mathematical Representation**:
   - The forward-spot premium is given by:
	 $$ FSP_n = BRP_n + \left(1 + \frac{f_{n-1,  n}}{100}\right)\left[\mathrm{dur}_{n-1}E(\Delta s_{n-1}) - 0.5C x_{n-1}\mathrm{vol}(\Delta s_{n-1})^2\right] $$

1. **Substitute the Given Values**:
   - $$f_{n-1,  n} = 3.5\%$$
   - $$s_1 = 2.0\%$$
   - $$\mathrm{dur}_{n-1} = 5$$
   - $$\mathrm{vol}(\Delta s_{n-1}) = 0.2\%$$
   - $$E(\Delta s_{n-1}) = -0.1\%$$
   - $$C x_{n-1} = 0.8$$

   First,  calculate the [[PSET II Fixed Income Asset Pricing 1|convexity]] bias:

   $$ CB_n = -0.5 \cdot C x_{n-1} \cdot \mathrm{vol}(\Delta s_{n-1})^2 $$

   $$ CB_n = -0.5 \cdot 0.8 \cdot (0.002)^2 $$

   $$ CB_n = -0.5 \cdot 0.8 \cdot 0.000004 $$

   $$ CB_n = -0.0000016 = -0.00016\% $$

   Next,  calculate the rate [[FORWARD RATES AND TERM STRUCTURE|expectations]] component:

   $$ \mathrm{dur}_{n-1}E(\Delta s_{n-1}) = 5 \cdot (-0.001) $$

   $$ \mathrm{dur}_{n-1}E(\Delta s_{n-1}) = -0.005 = -0.5\% $$

   Combine these components:

   $$ FSP_n = f_{n-1,  n} - s_1 $$

   $$ FSP_n = 3.5\% - 2.0\% = 1.5\% $$

   Rearrange to solve for $$BRP_n$$:

   $$ BRP_n = FSP_n - \left(1 + \frac{f_{n-1,  n}}{100}\right)\left[\mathrm{dur}_{n-1}E(\Delta s_{n-1}) - CB_n\right] $$

   Substitute values:

   $$ BRP_n = 1.5\% - \left(1 + \frac{3.5}{100}\right)\left[-0.5\% - (-0.00016\%)\right] $$

   $$ BRP_n = 1.5\% - (1.035)\left[-0.5\% + 0.00016\%\right] $$

   $$ BRP_n = 1.5\% - (1.035)(-0.49984\%) $$

   $$ BRP_n = 1.5\% + 0.517\% $$

   $$ BRP_n = 2.017\% $$

1. **Conclusion**:
   - Bond risk premium: $$BRP_n = 2.017\%$$
   - Rate [[FORWARD RATES AND TERM STRUCTURE|expectations]]: $$E(\Delta s_{n-1}) = -0.5\%$$
   - [[PSET II Fixed Income Asset Pricing 1|Convexity]] bias: $$CB_n = -0.00016\%$$

## 5. Key Takeaways
- **Forward Rates**:
  - Forward rates can be decomposed into bond risk premiums,  rate [[FORWARD RATES AND TERM STRUCTURE|expectations]],  and [[PSET II Fixed Income Asset Pricing 1|convexity]] bias.
  - These components provide insights into the drivers of bond [[Assets|returns]] and the shape of the yield curve.
- **Principal Component Analysis**:
  - PCA identifies the dominant yield-curve shifts (level,  slope,  and curvature) and simplifies [[Financial Mathematics Course|risk management]].
  - The first two components capture most of the yield-curve risk,  while higher-order components are less stable and more dataset-dependent.
- **Practical Implications**:
  - Investors can use forward rates and PCA to align their [[Lecture Notes Bonds,  Preferred Stock,  and Structured Products|portfolio strategies]] with [[Forward Rate|market expectations]] and exploit relative value opportunities.
  - Risk measures like [[Key Rates O1s Durations and Hedging|duration]] and slope [[Key Rates O1s Durations and Hedging|duration]] are essential for managing yield-curve exposure,  but [[A Guide to Duration DV01 and Yield Curve|key rate durations]] provide additional granularity.

This concludes the lecture notes on yield-curve analysis,  forward rates,  and principal component analysis. The next session will focus on advanced modeling techniques for yield-curve dynamics and their implications for [[The Impact of Option Strategies in Financial  Portfolios Performance|portfolio management]].

# Lecture Notes: Advanced Interest Rate Models and Relative Value Trading

## 1. Introduction to Interest Rate Models
- **Purpose and Importance**:
  - Interest rate models are essential tools for [[Arbitrage Pricing of Derivatives|pricing]] fixed-income securities,  valuing interest rate [[Chapter 9 Arbitrage and Hedging With Options|derivatives]],  and managing risk.
  - These models capture the stochastic behavior of [[Interest Rate Quotations|interest rates]] and are used to construct [[Arbitrage Pricing of Derivatives|arbitrage]]-free valuation frameworks.
- **Key Features of Interest Rate Models**:
  - **Stochastic Differential Equations**:
	- Models specify the dynamics of the [[An Overview of the Vasicek Short Rate Model|short rate]] through stochastic differential equations.
  - **Distributional Assumptions**:
	- Early models (e.g.,  Ho-Lee,  Hull-White) assume normally distributed short rates,  allowing for negative rates.
	- Later models (e.g.,  Kalotay-Williams-Fabozzi,  Black-Karasinski,  Black-Derman-Toy) assume lognormal distributions,  restricting rates to positive values.
  - **[[The Ornstein-Uhlenbeck (OU) Process|Mean Reversion]]**:
	- Some models incorporate [[The Ornstein-Uhlenbeck (OU) Process|mean reversion]],  where rates tend toward a long-term target.
  - **No-[[Arbitrage Pricing of Derivatives|Arbitrage]] Property**:
	- Models are calibrated to match the current [[The Vasicek Model|term structure]],  ensuring [[6. A Brief Introduction to Stochastic Calculus|arbitrage-free pricing]].

## 2. Overview of Key Interest Rate Models

### 2.1 Ho-Lee Model
- **Process**:
  $$ dr = \theta(t) dt + \sigma dz $$
  - The [[An Overview of the Vasicek Short Rate Model|short rate]] is normally distributed and unbounded,  allowing for negative rates.
- **Key Features**:
  - Simple and tractable.
  - Drift term is proportional to the slope of the [[The Vasicek Model|term structure]].
  - Rates are symmetrical around the mean in [[A Real-Life Option Pricing Exercise|binomial]] lattices.
- **Limitations**:
  - Negative rates are economically unrealistic.
  - Unbounded growth of rates.

### 2.2 Kalotay-Williams-Fabozzi (KWF) Model
- **Process**:
  $$ d\ln(r) = \phi dt + \sigma dz $$
  - The [[An Overview of the Vasicek Short Rate Model|short rate]] follows a lognormal distribution,  ensuring positivity.
- **Key Features**:
  - Rates grow unbounded when $\phi > 0$ and decay toward zero when $\phi < 0$.
  - Lognormal distribution skews rates toward higher values.
- **Comparison to Ho-Lee**:
  - Avoids negative rates.
  - Smaller spread of rates at the same volatility level.

### 2.3 Black-Karasinski Model
- **Process**:
  $$ d\ln(r) = (\theta - \phi \ln(r)) dt + \sigma dz $$
  - Incorporates [[The Ornstein-Uhlenbeck (OU) Process|mean reversion]],  where $\phi$ controls the speed of reversion.
- **Key Features**:
  - Rates are lognormally distributed and mean-reverting.
  - Extension of the KWF model with [[The Ornstein-Uhlenbeck (OU) Process|mean reversion]].
- **Comparison to Hull-White**:
  - Hull-White assumes normal distribution; Black-Karasinski assumes lognormal distribution.

### 2.4 Black-Derman-Toy (BDT) Model
- **Process**:
  $$ d\ln(r) = \left(\theta(t) + \frac{\sigma'(t)}{\sigma(t)} \ln(r)\right) dt + \sigma(t) dz $$
  - [[The Ornstein-Uhlenbeck (OU) Process|Mean reversion]] is endogenous,  driven by the slope of the volatility curve.
- **Key Features**:
  - Rates are lognormally distributed.
  - [[The Ornstein-Uhlenbeck (OU) Process|Mean reversion]] depends on the volatility structure.
  - Reduces to the KWF model when volatility is constant.

## 3. Binomial and Trinomial Lattices
- **Purpose**:
  - Lattices represent the evolution of [[Interest Rate Quotations|interest rates]] over discrete time steps.
  - Used for [[Arbitrage Pricing of Derivatives|pricing]] bonds,  [[Chapter 9 Arbitrage and Hedging With Options|derivatives]],  and other interest rate-sensitive instruments.
- **Key Features**:
  - **Recombination**:
	- Lattices recombine,  ensuring that an up-step followed by a down-step leads to the same rate as a down-step followed by an up-step.
  - **No-[[Arbitrage Pricing of Derivatives|Arbitrage]] Property**:
	- Lattices are calibrated to match the current [[The Vasicek Model|term structure]],  ensuring [[6. A Brief Introduction to Stochastic Calculus|arbitrage-free pricing]].
- **Examples**:
  - **Ho-Lee Lattice**:
	- Rates are normally distributed,  allowing for negative values.
	- Spread between high and low rates increases with time and volatility.
  - **KWF Lattice**:
	- Rates are lognormally distributed,  ensuring positivity.
	- Spread is smaller than in the Ho-Lee model and skewed toward higher rates.
  - **BDT Lattice**:
	- [[The Ornstein-Uhlenbeck (OU) Process|Mean reversion]] is driven by the volatility structure.
	- Decreasing volatility increases [[The Ornstein-Uhlenbeck (OU) Process|mean reversion]],  reducing the spread of rates.

## 4. Relative Value (RV) Trading in Fixed Income

### 4.1 Definition and Importance
- **Relative Value Trading**:
  - Exploits [[Arbitrage Pricing of Derivatives|pricing]] inefficiencies between securities to generate alpha.
  - Less dependent on the absolute level of yields compared to directional trades.
- **Advantages**:
  - Lower [[Lecture 6-[[Lecture 6-Leverage, Tail Risk, Volatility Products|Leverage]], Tail Risk, Volatility Products#6.6 [[Key Rates O1s Durations and Hedging|Hedging]] tail risks|tail risk]] compared to macro trading.
  - Focuses on spreads between securities rather than outright market moves.

### 4.2 Building a Fair Value Baseline
- **Fair Value Curve**:
  - Represents the baseline against which securities are compared.
  - Constructed using bootstrapping or spline interpolation methods.
- **Recent Practices**:
  - Multi-curve frameworks (e.g.,  Is,  SOFR) have replaced LIBOR-based curves.
  - Monotone convex spline interpolation preserves geometric properties.

## 5. Key Metrics in RV Trading

### 5.1 Z-Score
- **Definition**:
  - Measures the deviation of a security's yield from its historical mean in standard deviations.
  $$ \text{Z-Score} = \frac{\text{Current Value} - \text{Mean Value}}{\text{Standard Deviation}} $$
- **Interpretation**:
  - High absolute Z-scores indicate strong signals for [[The Ornstein-Uhlenbeck (OU) Process|mean reversion]].

### 5.2 Mean Reversion
- **Assumption**:
  - Prices or yields will revert to their historical mean over time.
- **Limitations**:
  - Structural changes or market shocks can violate [[The Ornstein-Uhlenbeck (OU) Process|mean reversion]].

### 5.3 Carry and Roll Down
- **Carry**:
  - Return from [[Realized Returns|coupon payments]] minus funding costs.
  - Positive carry occurs when the coupon exceeds funding costs.
- **Roll Down**:
  - Return from changes in yield as a bond matures.
  - Positive roll down occurs on an upward-sloping yield curve.

### 5.4 Total Return
- **Formula**:
  $$ \text{Total Return} = \text{Expected Return} + \text{Carry} + \text{Roll Down} $$
- **Importance**:
  - Combines all components of return to evaluate trades holistically.

## 6. RV Models: Market-Based vs. Model-Based

### 6.1 Market-Based Models
- **Examples**:
  - **[[Chapter 37 - Equity Swaps|Asset Swap]] Spread (ASW)**:
	- Spread between bond yield and matched maturity [[Teaching Note 4 Interest Rate Derivatives|swap rate]].
  - **True Spread**:
	- Spread calculated by matching bond and [[Chapter 34 - Pricing Interest Rate Swaps|swap cash flows]].
  - **[[Relative Value Analysis|Z-Spread]]**:
	- Constant spread added to the yield curve to match bond price.
- **Advantages**:
  - Directly tradable.
  - Based on observable market data.

### 6.2 Model-Based Models
- **Examples**:
  - **Constant Maturity Treasury (CMT) Curve**:
	- Baseline curve fitted using all Treasury bonds.
  - **Hull-White Two-[[Pricing Factors in a One-Period Framework|Factor Model]]**:
	- Captures shortand long-term rate dynamics.
- **Advantages**:
  - Incorporates theoretical insights.
  - Useful for benchmarking and [[Week 4 Valuing Young and High‐Growth Companies|scenario analysis]].

## 7. Constructing RV Trades
- **Spread Trades**:
  - Long one bond and short another to exploit relative mispricing.
  - Reduces [[Key Rates O1s Durations and Hedging|duration]] risk by being DV01 neutral.
- **Butterfly Trades**:
  - Long the middle bond and short the wings (or vice versa) to capture relative value.

## 8. Scenario and Horizontal Analysis
- **[[Week 4 Valuing Young and High‐Growth Companies|Scenario Analysis]]**:
  - Evaluates [[An Asset Allocation Primer|portfolio]] performance under specific market changes (e.g.,  parallel shifts,  curvature changes).
- **Horizontal Analysis**:
  - Extends [[Week 4 Valuing Young and High‐Growth Companies|scenario analysis]] to multiple time periods and scenarios.

## 9. Automation and the Future of RV Trading
- **Big Data and Machine Learning**:
  - Automates trade identification and [[Arbitrage-Free Interest Rate Models|model calibration]].
  - Enhances efficiency and accuracy in RV analysis.
- **Quantum Computing**:
  - Potential to revolutionize [[Mathematics of the Financial Markets|financial modeling]] with [[Multi-Dimensional Processes|multi-dimensional analysis]].

## 10. Key Takeaways
- **Interest Rate Models**:
  - Understanding model assumptions (e.g.,  distribution,  [[The Ornstein-Uhlenbeck (OU) Process|mean reversion]]) is critical for effective application.
- **Relative Value Trading**:
  - Combines theoretical models and market data to identify mispriced securities.
- **[[Financial Mathematics Course|Risk Management]]**:
  - Proper controls and awareness of model limitations are essential to avoid catastrophic losses (e.g.,  [[Class Note 13 The [[Risk Management Lessons From Long Term Capital Management|LTCM Meltdown]]|LTCM]]).

This concludes the lecture notes on advanced interest rate models and relative value trading. The next session will focus on the valuation of bonds with embedded options using lattice methodologies.

# Lecture Notes: Valuation of Bonds with Embedded Options and Mortgage-Backed Securities (MBS)

## 1. Introduction to Valuation of Bonds with Embedded Options
- **Definition and Importance**:
  - Bonds with embedded options,  such as callable and putable bonds,  have cash flows that depend on [[Forward Rate|future interest rate]] levels and volatility.
  - The valuation of these bonds requires specialized models,  such as [[A Real-Life Option Pricing Exercise|binomial]] [[Lecture Notes 10- Interest Rate Derivatives|interest rate trees]],  to account for the optionality embedded in the bond structure.
- **Key Concepts**:
  - **Callable Bonds**: Allow the issuer to redeem the bond before maturity,  typically when [[Interest Rate Quotations|interest rates]] decline.
  - **Putable Bonds**: Allow the bondholder to sell the bond back to the issuer before maturity,  typically when [[Interest Rate Quotations|interest rates]] rise.
  - **Option-Adjusted Spread (OAS)**: The spread added to the benchmark yield curve to equate the model value of a bond with its market price.
  - **Effective [[An Analytical Decomposition of Forward Rates|Duration and Convexity]]**: Measures of [[Forward Bond Yield|interest rate sensitivity]] that account for the impact of embedded options.

## 2. Valuation Using Binomial Interest Rate Trees
- **[[Overview of Financial Markets|Overview]]**:
  - A [[A Real-Life Option Pricing Exercise|binomial]] interest [[Rate and Price Trees|rate tree]] is a lattice structure that models the evolution of [[Interest Rate Quotations|interest rates]] over time.
  - The tree is calibrated to the current yield curve and assumes a specific level of [[Fixed Income Versus Equity Derivatives|interest rate volatility]].

### 2.1 Constructing the Interest Rate Tree
- **Step 1: Root Rate**:
  - The root rate ($r_0$) is the current one-year rate.
  - Example: If the current one-year rate is 3.5%,  then $r_0 = 3.5\%$.
- **Step 2: Forward Rates**:
  - At each node,  the higher and lower one-year rates are calculated using the relationship:
	$$ r_{i,  H} = r_{i,  L} \cdot e^{2\sigma} $$
	$$ r_{i,  L} = r_{i,  H} \cdot e^{-2\sigma} $$
  - Example: If $r_{1,  L} = 4.75\%$ and $\sigma = 10\%$,  then:
	$$ r_{1,  H} = 4.75\% \cdot e^{2 \cdot 0.10} = 5.8017\% $$

- **Step 3: [[Credit Markets Session 4|Calibration]]**:
  - The tree is calibrated to ensure that it prices option-free bonds at par.
  - This involves iteratively adjusting the rates until the bond value matches its market price.

### 2.2 Valuing a Bond at a Node
- **Recursive Valuation**:
  - The value at a node is the present value of the [[Week 6 Assignment Review|expected cash flows]] from the higher and lower rate states:
	$$ V_{\text{node}} = \frac{1}{2} \left( \frac{V_H + C}{1 + r^*} + \frac{V_L + C}{1 + r^*} \right) $$
  - Where:
	- $V_H$: Value in the higher rate state.
	- $V_L$: Value in the lower rate state.
	- $C$: Coupon payment.
	- $r^*$: One-year rate at the node.
- **Example**:
  - If $V_H = 98.486$,  $V_L = 99.475$,  $C = 4.2$,  and $r^* = 3.5\%$,  then:
	$$ V_{\text{node}} = \frac{1}{2} \left( \frac{98.486 + 4.2}{1.035} + \frac{99.475 + 4.2}{1.035} \right) = 99.691 $$

## 3. Valuation of Callable and Putable Bonds
- **Callable Bonds**:
  - The issuer will call the bond if the present value of [[Advanced Derivatives Pricing Methodology|future cash flows]] exceeds the call price.
  - At each node:
	$$ V_t = \min(\text{Call Price},   \text{PV of Future Cash Flows}) $$

- **Putable Bonds**:
  - The bondholder will put the bond if the present value of [[Advanced Derivatives Pricing Methodology|future cash flows]] is less than the put price.
  - At each node:
	$$ V_t = \max(\text{Put Price},   \text{PV of Future Cash Flows}) $$

- **Example**:
  - For a callable bond with a call price of $100$,  if the PV of [[Advanced Derivatives Pricing Methodology|future cash flows]] at a node is $100.315$,  the bond will be called,  and the value at the node is set to $100$.

## 4. Option-Adjusted Spread (OAS)
- **Definition**:
  - The OAS is the fixed spread added to the benchmark rates in the interest [[Rate and Price Trees|rate tree]] to equate the model value of a bond with its market price.
- **Calculation**:
  - Iteratively adjust the spread until the model value matches the market price.
  - Example: If the market price of a callable bond is $102.218$ and the model value is $102.899$,  the OAS is calculated as the spread that reduces the model value to $102.218$.

## 5. Effective Duration and Convexity
- **Effective [[Key Rates O1s Durations and Hedging|Duration]]**:
  - Measures the percentage change in bond price for a parallel shift in the yield curve:
	$$ \text{Effective Duration} = \frac{V_- - V_+}{2V_0 \Delta r} $$

- **Effective [[PSET II Fixed Income Asset Pricing 1|Convexity]]**:
  - Measures the curvature of the price-yield relationship:
	$$ \text{Effective Convexity} = \frac{V_+ + V_- - 2V_0}{2V_0 (\Delta r)^2} $$

- **Example**:
  - For a callable bond:
	- $V_+ = 101.621$,  $V_- = 102.765$,  $V_0 = 102.218$,  $\Delta r = 0.0025$.
	- Effective [[Key Rates O1s Durations and Hedging|Duration]]:
	  $$ \text{Effective Duration} = \frac{102.765 - 101.621}{2 \cdot 102.218 \cdot 0.0025} = 2.24 $$
	- Effective [[PSET II Fixed Income Asset Pricing 1|Convexity]]:
	  $$ \text{Effective Convexity} = \frac{101.621 + 102.765 - 2 \cdot 102.218}{2 \cdot 102.218 \cdot (0.0025)^2} = -39.1321 $$

## 6. Valuation of Mortgage-Backed Securities (MBS)
- **Challenges**:
  - [[Mortgage Pricing Spreads and Duration|MBS cash flows]] are sensitive to [[How Countries Go Broke-Chapter 12 to Chapter 14|interest rate changes]] and prepayment behavior.
  - Prepayments introduce path dependency,  requiring advanced modeling techniques.

### 6.1 Monte Carlo Simulation
- **[[Overview of Financial Markets|Overview]]**:
  - [[Pricing a Callable Leveraged Constant Maturity Swap Spread Note|Monte Carlo simulation]] generates multiple interest rate paths to account for [[Fixed Income Versus Equity Derivatives|interest rate volatility]] and prepayment behavior.
  - The MBS price is the average of discounted cash flows across all paths.
- **Steps**:
  1. **Select an [[An Overview of the Vasicek Short Rate Model|Interest Rate Model]]**:
	 - Example: [[A Guide to the Front End and [[Basis Swaps|Basis Swap]] Markets#[[Short-Term Rates and the Transition from LIBOR|London Interbank Offered Rate]] (LIBOR)|LIBOR]] Market Model (LMM) for realistic [[Teaching Note 4 Interest Rate Derivatives|swap rate]] dynamics.
  1. **Calibrate the Model**:
	 - Use market data (e.g.,  swaption prices) to determine model parameters.
  1. **Generate Interest Rate Paths**:
	 - Simulate correlated random numbers to construct [[Arbitrage Pricing of Derivatives|arbitrage]]-free paths.
  1. **Project Cash Flows**:
	 - Use a prepayment model to estimate cash flows along each path.
  1. **Discount Cash Flows**:
	 - Calculate the present value of cash flows for each path and average them.

## 7. Prepayment Modeling
- **Sources of Prepayments**:
  - **Rate-Driven Refinancings**: Borrowers refinance when rates decline.
  - **Cashout Refinancings**: Borrowers extract equity from their homes.
  - **Credit-Driven Refinancings**: Borrowers refinance due to improved credit profiles.
  - **Housing Turnover**: Prepayments due to property sales.
  - **Curtailments**: Partial prepayments to reduce loan balances.
  - **Involuntary Prepayments**: Prepayments due to defaults and foreclosures.
- **Key Drivers**:
  - Interest rate levels and volatility.
  - Home price appreciation (HPA).
  - Borrower credit profiles and loan-to-value (LTV) ratios.

## 8. Key Takeaways
- **Valuation of Bonds with Embedded Options**:
  - Requires [[Lecture Notes 10- Interest Rate Derivatives|interest rate trees]] and recursive valuation techniques.
  - OAS and effective [[Key Rates O1s Durations and Hedging|duration]]/[[PSET II Fixed Income Asset Pricing 1|convexity]] are critical for [[Financial Mathematics Course|risk management]].
- **Valuation of MBS**:
  - [[Pricing a Callable Leveraged Constant Maturity Swap Spread Note|Monte Carlo simulation]] is essential to account for [[Fixed Income Versus Equity Derivatives|interest rate volatility]] and prepayment behavior.
  - Prepayment modeling is both an art and a science,  requiring careful consideration of borrower behavior and macroeconomic factors.
- **Practical Implications**:
  - Advanced models and computational techniques are necessary for accurate valuation and [[Financial Mathematics Course|risk management]] of complex fixed-income securities.

This concludes the lecture notes on the valuation of bonds with embedded options and [[Fremont Financial Corp. (b)|mortgage-backed securities]]. The next session will focus on advanced prepayment modeling techniques and their applications in [[A Primer on Structured Finance|structured finance]].

# Lecture Notes: Mortgage-Backed Securities (MBS) Valuation and Convertible Securities

## 1. Introduction to Mortgage-Backed Securities (MBS) Valuation
- **Definition and Importance**:
  - [[Fremont Financial Corp. (b)|Mortgage-Backed Securities]] (MBS) are fixed-income securities backed by pools of mortgage loans. Their valuation is complex due to embedded prepayment options and path-dependent cash flows.
  - MBS valuation requires advanced modeling techniques to account for interest rate dynamics,  prepayment behavior,  and [[US Debt Crisis and Adjustment (2007–2011)|housing market]] [[Week 2 Fundamentals Of Forecasting|fundamentals]].

## 2. Path Dependence in MBS
- **Definition**:
  - Path dependence means that the [[Advanced Derivatives Pricing Methodology|future cash flows]] of an MBS depend not only on the current level of [[Interest Rate Quotations|interest rates]] but also on the historical path of [[Interest Rate Quotations|interest rates]] and other variables.
- **Implications**:
  - Path dependence necessitates the use of [[Pricing a Callable Leveraged Constant Maturity Swap Spread Note|Monte Carlo simulation]] or other advanced methodologies for valuation,  as [[Chapter 40 - Pricing Fixed Income Options: Black’s Model and MCS|closed-form solutions]] and lattice-based methods are insufficient.
- **Examples**:
  - **Burnout Effect**:
	- Borrowers who have had multiple opportunities to refinance in the past are less likely to refinance again,  reducing prepayment responsiveness.
  - **Interaction of Prepayments and Defaults**:
	- Faster early prepayments reduce the number of loans outstanding,  which in turn lowers the pool's future [[Default Risk and Credit Derivatives 183|default risk]].

## 3. Housing Market Fundamentals and MBS Valuation
- **Key Drivers**:
  - **Home Price Appreciation (HPA)**:
	- Determines current loan-to-value (LTV) ratios,  a key driver of defaults and loss severity.
	- Influences cash-out refinancing activity and turnover speeds.
  - **Turnover Speeds**:
	- Estimated as the ratio of existing home sales to the total single-family housing stock.
	- Affected by housing inventory levels,  home price trends,  and mortgage credit availability.
- **Market Dynamics**:
  - Strong HPA encourages trade-ups and faster turnover,  while limited housing inventory can constrain turnover and refinancing activity.

## 4. Cash-Flow Modeling for MBS
- **Steps in Cash-Flow Modeling**:
  1. **Project Cash Flows on the [[Risk Neutral Pricing of Options|Underlying Asset]] Pool**:
	 - Use prepayment and default models to estimate principal and interest payments.
  1. **Model the Waterfall Structure**:
	 - Define the rules for distributing cash flows to various tranches in the deal.
	 - Structures range from simple [[Mortgage Pass-Through Securities|pass-throughs]] to complex multi-tranche arrangements.
- **Output**:
  - The projected cash flows are used to compute valuation metrics such as yield,  weighted average life (WAL),  and option-adjusted spread (OAS).

## 5. Option-Adjusted Valuation Metrics
- **Option-Adjusted Spread (OAS)**:
  - **Definition**:
	- The spread over forward rates that equates the model price of an MBS to its market price.
  - **Calculation**:
	- Iteratively adjust the OAS until the model price matches the market price.
	- Formula:
	  $$ P = E\left[\sum_{n=1}^{N} \frac{CF_n}{\prod_{m=1}^{n} (1 + f_m + OAS)}\right] $$
  - **Option Cost**:
	- Calculated as the difference between the [[Relative Value Analysis|Z-spread]] and the OAS:
	  $$ \text{Option Cost} = Z - OAS $$
	- A positive option cost indicates the investor is short the prepayment option.
  - **Applications**:
	- OAS is used to assess relative value and excess [[Assets|returns]] over Treasuries or swaps.
	- It is highly model-dependent and should only be compared within a consistent modeling framework.
- **Effective [[An Analytical Decomposition of Forward Rates|Duration and Convexity]]**:
  - **Effective [[Key Rates O1s Durations and Hedging|Duration]]**:
	- Measures the sensitivity of MBS price to parallel shifts in the yield curve,  accounting for changes in cash flows due to prepayments.
	- Formula:
	  $$ \text{Effective Duration} = \frac{P_- - P_+}{2P_0 \Delta r} $$
  - **Effective [[PSET II Fixed Income Asset Pricing 1|Convexity]]**:
	- Measures the curvature of the price-yield relationship,  accounting for the impact of prepayments.
	- Formula:
	  $$ \text{Effective Convexity} = \frac{P_+ - 2P_0 + P_-}{P_0 (\Delta r)^2} $$
  - **[[Mortgage Pricing Spreads and Duration|Negative Convexity]]**:
	- MBS often exhibit [[Mortgage Pricing Spreads and Duration|negative convexity]] due to the embedded prepayment option,  leading to price compression when rates fall.

## 6. Extensions to Effective Duration
- **Partial Effective Durations**:
  - Measure the sensitivity of MBS price to specific factors,  such as changes in individual yield curve tenors,  volatility,  or spreads.
  - Formula:
	$$ \text{Effective Partial Duration} = \frac{P_-^F - P_+^F}{2P_0 \Delta F} $$
- **[[A Guide to Duration DV01 and Yield Curve|Key Rate Durations]] (KRD)**:
  - Measure sensitivity to shifts in specific segments of the yield curve.
- **Volatility and Spread Durations**:
  - Volatility [[Key Rates O1s Durations and Hedging|duration]] measures sensitivity to changes in [[Fixed Income Versus Equity Derivatives|interest rate volatility]].
  - [[Spread Duration and Dvo1|Spread duration]] measures sensitivity to changes in the OAS.

## 7. Analytical Example: Fannie Mae 30-Year 3.0s of 2019
- **Process**:
  1. Select a [[The Vasicek Model|term structure]] model (e.g.,  shifted lognormal LMM or normal LMM).
  1. Generate [[Teaching Note 7-Exotic Options And Derivative Pricing By Monte Carlo Simulation|Monte Carlo]] interest rate paths.
  1. Use a prepayment model to project cash flows along each path.
  1. Compute valuation metrics such as yield,  WAL,  [[Relative Value Analysis|Z-spread]],  and OAS.
- **Key Insights**:
  - The choice of [[The Vasicek Model|term structure]] model significantly impacts OAS and effective [[Key Rates O1s Durations and Hedging|duration]].
  - Consistency in the analytical framework is critical for meaningful comparisons.

## 8. Convertible Securities
- **Definition**:
  - Convertible securities are hybrid instruments that combine features of [[Class Note 1- Borrower-Lender conflicts and implied agency problems|debt and equity]],  allowing the holder to convert the security into shares of the issuer's stock.
- **Types**:
  - Convertible notes,  mandatory convertible preferred shares,  and perpetual convertible preferred shares.

### 8.1 Convertible Note Example: Tesla 2's of 2024
- **Key Terms**:
  - **Issue Size**: $1.84 billion.
  - **Coupon Rate**: 2.0% per annum.
  - **Conversion Price**: $309.83 per share (27.5% premium over the reference price of $243).
  - **Initial Conversion Ratio**: 3.2276 shares per note.
  - **Redemption**: Non-callable for life unless a fundamental change occurs.
  - **Settlement**: Physical,  cash,  or a combination.
- **Valuation**:
  - Combines the value of a straight bond with the value of the embedded conversion option.
  - Theoretical valuation considers factors such as [[Interest Rate Quotations|interest rates]],  credit spreads,  [[Option Risk|stock volatility]],  and dividend yield.

### 8.2 Convertible Note as a Contingent Claim
- **[[7. Black Scholes Model|Put-Call Parity]]**:
  - A convertible note can be viewed as a combination of a straight bond and a call option on the issuer's stock.
  - Formula:
	$$ S_t = C_t - P_t + K e^{-r(T-t)} $$
- **Stages of a Convertible Note**:
  - **Balanced Convertibles**: Moderate delta,  appealing to outright investors.
  - **Equity Substitutes**: High delta,  behave like equity.
  - **Busted Converts**: Deep out-of-the-money,  behave like straight debt.
  - **Distressed Converts**: High [[Quantitative Trading Strategies Lecture Notes|credit risk]],  require specialized expertise.

## 9. Key Takeaways
- **MBS Valuation**:
  - Requires advanced modeling techniques to account for path dependence,  prepayment behavior,  and interest rate dynamics.
  - Option-adjusted analytics,  such as OAS and effective [[Key Rates O1s Durations and Hedging|duration]],  provide a more accurate assessment of value and risk than static metrics.
- **Convertible Securities**:
  - Offer a spectrum of risk-return profiles,  from equity-like to bond-like behavior.
  - Valuation depends on the interplay of [[Interest Rate Quotations|interest rates]],  credit spreads,  [[Option Risk|stock volatility]],  and embedded options.
- **Practical Implications**:
  - Consistency in analytical frameworks is critical for meaningful comparisons and relative value assessments.
  - Investors should understand the strengths and limitations of different valuation metrics and use a combination of techniques to build intuition about the drivers of return and risk.

This concludes the lecture notes on MBS valuation and convertible securities. The next session will focus on advanced modeling techniques for prepayment behavior and the valuation of [[Preview of the Book|structured products]].

# Lecture Notes: Advanced Credit Analysis and Convertible Bond Valuation

## 1. Introduction to Credit Analysis and Convertible Bonds
- **Purpose of Credit Analysis**:
  - Credit analysis evaluates the likelihood of a bond issuer meeting its debt obligations,  focusing on both [[Default Risk and Credit Derivatives 183|default risk]] and changes in [[Wellman Inc the Importance of Loan Covenants|credit quality]].
  - Modern credit analysis incorporates both traditional financial ratios and market-based indicators,  such as equity volatility and credit spreads.
- **Convertible Bonds**:
  - Convertible bonds (CBs) are hybrid securities that combine [[Class Note 1- Borrower-Lender conflicts and implied agency problems|debt and equity]] features,  allowing bondholders to convert their bonds into shares of the issuer's stock.
  - CB valuation requires advanced modeling techniques to account for embedded options,  [[Quantitative Trading Strategies Lecture Notes|credit risk]],  and equity [[Chapter 47 - Asset Price Dynamics|price dynamics]].

## 2. Credit Analysis Framework
### 2.1 Traditional Credit Analysis
- **[[Default Risk and Credit Derivatives 183|Default Risk]]**:
  - Focuses on the issuer's ability to meet scheduled [[Notes on Currency Swaps|interest and principal]] payments.
  - Key financial ratios include:
	- **Fixed Charge Coverage**: Measures the ability to cover fixed obligations with [[BMW Valuation|operating income]].
	- **[[Lecture 6-Leverage, Tail Risk, Volatility Products|Leverage]] Ratios**: Assess the proportion of debt in the [[Introduction to Corporate Finance|capital structure]].
	- **Funds Flow/Total Debt**: Indicates the ability to generate [[Preview of the Book|cash flow]] to service debt.
- **Buy-and-Hold Perspective**:
  - Historically,  bond investors prioritized [[Default Risk and Credit Derivatives 183|default risk]],  as bonds were held to maturity.
  - Market value fluctuations were less relevant under stable interest rate environments.

### 2.2 Modern Credit Analysis
- **Market-Based Indicators**:
  - Incorporates equity market data,  such as [[Black-Scholes Model and Extensions|stock price volatility]] and equity cushion,  to assess [[Quantitative Trading Strategies Lecture Notes|credit risk]].
  - **Equity Cushion**:
	- Represents the buffer between the value of a company's assets and its liabilities.
	- A larger equity cushion reduces [[Default Risk and Credit Derivatives 183|default risk]],  while higher equity volatility increases it.
  - **Equity-Debt Consistency**:
	- The intrinsic value of equity and debt derives from the same cash flows,  linking their valuations.
- **Active Bond Management**:
  - Investors now trade bonds actively,  seeking profits from changes in [[Interest Rate Quotations|interest rates]] and [[Wellman Inc the Importance of Loan Covenants|credit quality]].
  - Credit analysis must address both [[Default Risk and Credit Derivatives 183|default risk]] and the likelihood of credit rating changes.

## 3. Convertible Bond Valuation
### 3.1 Key Features of Convertible Bonds
- **Debt-Equity Hybrid**:
  - CBs provide bondholders with [[Equity Linked Note|downside protection]] (debt) and upside potential (equity conversion).
- **Embedded Options**:
  - CBs include a call option for the bondholder to convert the bond into equity.
  - Some CBs also include issuer call or put provisions.
- **Soft Bond Floor**:
  - The bond floor represents the minimum value of the CB,  determined by its debt component.
  - A "soft" bond floor adjusts downward as the issuer's [[Wellman Inc the Importance of Loan Covenants|credit quality]] deteriorates.

### 3.2 Valuation Techniques
- **[[Mathematical Modeling of Derivative Pricing|Black-Scholes]] Framework**:
  - CB valuation often extends the [[Mathematical Modeling of Derivative Pricing|Black-Scholes]] option [[Arbitrage Pricing of Derivatives|pricing]] model to account for [[Quantitative Trading Strategies Lecture Notes|credit risk]] and equity dynamics.
  - The partial differential equation for CB valuation is:
	$$ \frac{\partial V}{\partial t} + \left(r_t - q + \lambda(S,   t)\right)S\frac{\partial V}{\partial S} + \frac{1}{2}\sigma^2 S^2 \frac{\partial^2 V}{\partial S^2} = \left(r_t + \lambda(S,   t)\right)V - \lambda(S,   t)R $$
	- \( V \): CB value.
	- \( \lambda(S,  t) \): [[A Poisson Model of Single Issuer Default|Default intensity]].
	- \( R \): Recovery value in default.
	- \( \sigma \): Equity volatility.
- **Numerical Methods**:
  - Finite difference techniques solve the PDE numerically,  incorporating [[Appendix 21.C Solutions for Black-Scholes PDE|boundary conditions]] for [[Realized Returns|coupon payments]],  conversion features,  and default triggers.

## 4. Credit Spread and Default Intensity
### 4.1 Default Intensity Models
- **Power Law Intensity**:
  - [[A Poisson Model of Single Issuer Default|Default intensity]] is modeled as:
	$$ \lambda(S,   t) = a(t) \left(\frac{S(0)}{S(t)}\right)^p $$
	- \( a(t) \): Time-dependent scaling factor.
	- \( p \): Power law exponent,  typically \( 1.0 < p < 2.0 \).
  - As the [[Chapter 16 - Black–Scholes Model|stock price]] \( S(t) \) decreases,  [[A Poisson Model of Single Issuer Default|default intensity]] \( \lambda(S,  t) \) increases,  reflecting higher [[Quantitative Trading Strategies Lecture Notes|credit risk]].
- **[[Credit Markets Session 4|Calibration]]**:
  - Parameters \( a(t) \) and \( p \) are calibrated using market data,  such as CDS spreads or bond prices.
  - Exhibit 39-2 illustrates the relationship between equity prices and calibrated default intensities for various issuers.

### 4.2 Credit Spread Determination
- **Three Scenarios**:
  1. **Traded CDS**:
	 - Use observed CDS spreads directly,  adjusted for seniority.
  1. **Vanilla Bonds**:
	 - Infer synthetic CDS spreads from bond z-spreads,  adjusted for basis and seniority.
  1. **No Traded Instruments**:
	 - Map to an index proxy or similar issuers by industry,  geography,  and rating.

## 5. Convertible Bond Sensitivities
### 5.1 Delta,  Vega,  and Rho
- **Delta (\( \Delta \))**:
  - Measures sensitivity to equity price changes:
	$$ \Delta = \frac{\partial V}{\partial S} $$
  - For low stock prices,  delta can exceed the conversion ratio due to heightened [[Default Risk and Credit Derivatives 183|default risk]].
- **Vega (\( \nu \))**:
  - Measures sensitivity to equity volatility:
	$$ \nu = \frac{\partial V}{\partial \sigma} $$
  - Vega can be negative for high stock prices,  reflecting the impact of volatility on [[Quantitative Trading Strategies Lecture Notes|credit risk]].
- **Rho (\( \rho \))**:
  - Measures sensitivity to [[Interest Rate Quotations|interest rates]]:
	$$ \rho = \frac{\partial V}{\partial r} $$
  - Typically negligible for CBs,  as [[Quantitative Trading Strategies Lecture Notes|credit risk]] dominates [[Forward Bond Yield|interest rate sensitivity]].

### 5.2 Gamma and Theta
- **Gamma (\( \Gamma \))**:
  - Measures the rate of change of delta with respect to [[Chapter 16 - Black–Scholes Model|stock price]]:
	$$ \Gamma = \frac{\partial \Delta}{\partial S} $$
  - CBs often exhibit negative gamma for low stock prices,  reflecting the soft bond floor's sensitivity to equity movements.
- **Theta (\( \Theta \))**:
  - Measures time decay:
	$$ \Theta = \frac{\partial V}{\partial t} $$
  - Theta is typically negative,  representing the cost of holding the CB.

## 6. Convertible Bond Arbitrage
### 6.1 Arbitrage Strategy
- **Delta-Hedged Position**:
  - Short the underlying equity against the CB to create a delta-neutral position.
  - Profit from gamma trading as the [[Chapter 16 - Black–Scholes Model|stock price]] fluctuates.
- **Challenges**:
  - CB gamma is often too weak to monetize for long-dated positions.
  - Negative gamma and vega for distressed issuers complicate [[Key Rates O1s Durations and Hedging|hedging]] strategies.

### 6.2 Alternative Strategies
- **[[Cds-Equivalent Bond Spread|Credit Spread]] Tightening**:
  - For distressed CBs,  profit from anticipated [[Cds-Equivalent Bond Spread|credit spread]] tightening as the issuer's financial condition improves.
- **Volatility [[Arbitrage Pricing of Derivatives|Arbitrage]]**:
  - Exploit discrepancies between CB-implied volatilities and exchange-traded option volatilities.

## 7. Key Takeaways
- **Credit Analysis**:
  - Modern credit analysis integrates traditional financial ratios with market-based indicators,  such as equity volatility and credit spreads.
  - The equity cushion and its volatility are critical determinants of [[Default Risk and Credit Derivatives 183|default risk]].
- **Convertible Bond Valuation**:
  - CB valuation requires advanced models to account for embedded options,  [[Quantitative Trading Strategies Lecture Notes|credit risk]],  and equity dynamics.
  - The soft bond floor and power law [[A Poisson Model of Single Issuer Default|default intensity]] are essential for capturing CB price behavior.
- **Convertible Bond [[Arbitrage Pricing of Derivatives|Arbitrage]]**:
  - [[Purpose and Structure of Financial Markets 1|Arbitrage strategies]] must account for the complex interplay between equity,  credit,  and volatility risks.
  - Negative gamma and vega challenge traditional gamma trading approaches,  requiring alternative strategies.

This concludes the lecture notes on advanced credit analysis and convertible bond valuation. The next session will focus on credit scoring models and their applications in identifying potential default risks.

# Lecture Notes: Industry and Financial Analysis for Credit Evaluation

## 1. Introduction to Industry Analysis
- **Purpose**:
  - [[Porter's Five Forces|Industry analysis]] is critical for understanding the competitive dynamics,  regulatory environment,  and operational challenges that influence a company's [[Wellman Inc the Importance of Loan Covenants|credit quality]].
  - It provides the foundation for evaluating a company's [[Gordon Bargain Stores B|financial performance]] and risk profile.

## 2. Key Industry Variables
### 2.1 Research and Development (R&D)
- **Short-Term vs. Long-Term Impact**:
  - Companies with below-average R&D spending may achieve short-term gains through expanded margins.
  - However,  long-term success depends on correctly assessing industry trends and investing in the right technologies.
- **Risks of Misaligned R&D**:
  - Misallocation of R&D capital can lead to [[Case Study the London Whale|credit deterioration]],  as seen in the decline of mainframe-focused computer companies.
  - Industries like software and telecommunications face frequent technological disruptions,  making R&D direction critical.

### 2.2 Competition
- **Factors Influencing Competition**:
  - Price,  product quality,  brand recognition,  distribution,  and customer relationships.
  - Patents and trademarks can provide competitive advantages but may lead to revenue loss upon expiration (e.g.,  pharmaceutical patents).
- **[[Chapter 1-[[Chapter 1-Introduction to Globalization|Introduction to Globalization]]|Globalization]]**:
  - Competition is increasingly global,  with [[Forwards and Futures Notes|currency]] fluctuations and regional growth potential influencing outcomes.
  - Companies must adapt to international markets and diversify geographically to mitigate regional [[How the Eggheads Cracked|economic downturns]].
- **[[Market Structure and Size|Market Structure]]**:
  - Monopolies can maximize profits with [[Arbitrage Pricing of Derivatives|pricing]] flexibility,  while oligopolies often follow [[Arbitrage Pricing of Derivatives|pricing]] leaders.
  - Smaller companies in oligopolistic industries may face cost disadvantages and price wars,  as seen in the [[BMW Valuation|automotive industry]].

### 2.3 Sources of Supply
- **Self-Sufficiency**:
  - Companies that control their production inputs and can pass on cost increases to customers are in a stronger position.
- **Overcapacity**:
  - Overcapacity in an industry often leads to price wars,  deteriorating [[Gordon Bargain Stores B|financial performance]] across the sector.

### 2.4 Regulation
- **Regulated Monopolies**:
  - [[Arbitrage Pricing of Derivatives|Pricing]] is determined by government bodies to ensure fair [[Assets|returns]] while preventing excess profits.
  - Regulatory responsiveness to cost increases varies by state and can impact earnings stability.
- **Non-Monopoly Industries**:
  - Compliance with labor,  safety,  and environmental regulations can impose significant costs.
  - Stricter domestic regulations may disadvantage companies relative to foreign competitors.

### 2.5 Labor
- **Unionization**:
  - High unionization can lead to inflexible labor costs and strike risks.
  - Non-unionized companies often have cost advantages but may face unionization threats.
- **Work Rules**:
  - Efficiency is more influenced by work rules than wage rates,  as seen in the automotive supply industry.
- **Turnover and Talent Retention**:
  - High turnover of skilled professionals can weaken a company's competitive position.

### 2.6 Accounting Practices
- **Industry-Specific Practices**:
  - Analysts must understand unique accounting practices (e.g.,  insurance or utilities) and reconcile non-GAAP results with GAAP.
- **Adjustments and Trends**:
  - Historical adjustments for discontinued operations or accounting changes can obscure unfavorable trends.
  - Analysts should evaluate both adjusted and unadjusted results for a complete picture.

### 2.7 Event Risk
- **Definition**:
  - Event risk refers to major disruptions,  such as [[Note on LBO [[Introduction to Corporate Finance|Capital Structure]] Module Note|Note On LBO [[Introduction to Corporate Finance|Capital Structure]]|leveraged buyouts]],  natural disasters,  or accounting fraud.
- **Examples**:
  - The COVID-19 pandemic caused a 65%-75% drop in business for Envision Healthcare,  leading to a credit downgrade.
- **Assessment**:
  - While shocks are unforeseeable,  analysts can evaluate a company's exposure to potential risks like environmental liabilities or product recalls.

## 3. Financial Analysis
### 3.1 Traditional [[Week 1 Ratio Analysis + Valuation Review|Ratio Analysis]]
- **Key Ratios**:
  - Pretax interest coverage,  [[Lecture 6-Leverage, Tail Risk, Volatility Products|leverage]],  [[Preview of the Book|cash flow]],  net assets,  [[Week 5 Accounting Recap- R&D, Intangibles, M&A & Goodwill#[[Week 5 Accounting Recap- R&D, Intangibles, M&A & Goodwill|INTANGIBLE AMORTIZATION]] AND NON‐GAAP REPORTING|intangibles]] ,  unfunded pension liabilities,  plant age,  and working capital.
- **Industry-Specific Considerations**:
  - Ratios should be compared to industry benchmarks,  as absolute levels may vary significantly across sectors.

#### Pretax Interest Coverage
- **Definition**:
  - Measures the ability to cover interest charges with pretax income.
  - Formula:
	$$ \text{Pretax Interest Coverage} = \frac{\text{Pretax Income + Interest Expense}}{\text{Interest Expense}} $$
- **Interpretation**:
  - Coverage below 1x indicates reliance on borrowing or asset sales to meet interest payments.
  - Industry benchmarks vary (e.g.,  3.0x for utilities may indicate an A rating,  while the same for a drug company suggests a lower rating).

#### Leverage
- **Definition**:
  - Commonly measured as long-term debt as a percentage of total capitalization.
  - Market-adjusted [[Lecture 6-Leverage, Tail Risk, Volatility Products|leverage]] uses market value of equity instead of book value.
- **Considerations**:
  - High [[Lecture 6-Leverage, Tail Risk, Volatility Products|leverage]] increases fixed obligations and financial risk.
  - Analysts should evaluate the maturity structure,  [[Uses of Interest Rate Swaps|floating-rate debt]] exposure,  and off-balance-sheet obligations like operating leases.

#### Cash Flow
- **Definition**:
  - [[Preview of the Book|Cash flow]] as a percentage of total debt indicates the ability to service debt from operations.
  - Formula:
	$$ \text{Cash Flow} = \text{Net Income + Depreciation + Amortization + Deferred Taxes} $$
- **Adjustments**:
  - Exclude non-cash contributions and extraordinary items to focus on sustainable [[Preview of the Book|cash flow]].

#### Net Assets
- **Definition**:
  - Measures the ability to repay debt through asset liquidation.
  - Analysts must account for discrepancies between book value and liquidation value,  especially for illiquid or specialized assets.

## 4. Analysis of Return on Equity (ROE)
- **Decomposition**:
  - ROE is broken into four components: pretax margins,  asset turnover,  [[Lecture 6-Leverage, Tail Risk, Volatility Products|leverage]],  and tax rate.
  - Formula:
	$$ \text{ROE} = \left(\frac{\text{Net Income}}{\text{Sales}}\right) \times \left(\frac{\text{Sales}}{\text{Assets}}\right) \times \left(\frac{\text{Assets}}{\text{Equity}}\right) \times (1 - \text{Tax Rate}) $$
- **Trend Analysis**:
  - Examine trends over at least one [[Business Cycles- Introduction, Characteristics, and History|business cycle]] and compare to industry norms.
  - Deviations from industry standards may indicate unique management strategies or operational issues.

## 5. Non-Financial Factors
### 5.1 Foreign Exposure
- **Geographic Risks**:
  - Revenue concentration in unstable regions increases risk.
  - [[Forwards and Futures Notes|Currency]] fluctuations can impact profitability; [[Key Rates O1s Durations and Hedging|hedging]] strategies should be evaluated.

### 5.2 Management Quality
- **Evaluation Criteria**:
  - Strategic direction,  financial philosophy,  conservatism,  track record,  succession planning,  and control systems.
- **Corporate Governance**:
  - Analysts should assess the strength of governance practices and the role of the board of directors.

### 5.3 Ownership
- **Impact on Strategy**:
  - Family or closely held companies may be overly conservative.
  - Financial buyers may prioritize short-term gains,  increasing [[Quantitative Trading Strategies Lecture Notes|credit risk]] in [[Note on LBO [[Introduction to Corporate Finance|Capital Structure]] Module Note|Note On LBO [[Introduction to Corporate Finance|Capital Structure]]|leveraged buyouts]].

## 6. Combining Financial and Non-Financial Analysis
- **Integrated Approach**:
  - [[Wellman Inc the Importance of Loan Covenants|Credit quality]] is determined by both financial and business risk profiles.
  - Standard & Poor’s uses a matrix to integrate these factors,  with six levels of business risk (e.g.,  "excellent" to "vulnerable") and six levels of financial risk (e.g.,  "minimal" to "highly leveraged").
- **Example**:
  - A company with "satisfactory" business risk and "intermediate" financial risk may be rated between BB+ and BBB-.

## 7. Indenture Provisions
### 7.1 Purpose
- **Legal Framework**:
  - Defines the rights and obligations of issuers and bondholders.
  - Includes payment terms,  restrictive covenants,  and enforcement mechanisms.

### 7.2 Key Covenants
- **Debt Covenant**:
  - Limits additional borrowings,  often tied to financial ratios like debt-to-EBITDA.
- **Negative Pledge**:
  - Prevents securing new debt without equally securing existing bonds.
- **Restricted Payments**:
  - Limits dividends and stock buybacks to preserve capital.
- **Change of Control**:
  - Allows bondholders to sell bonds back to the issuer at a premium upon a change in ownership.

### 7.3 Enforcement
- **Default Scenarios**:
  - Payment defaults allow bondholders or trustees to sue for repayment.
  - Covenant breaches may lead to consent solicitations,  amendments,  or litigation.

## 8. Key Takeaways
- **[[Porter's Five Forces|Industry Analysis]]**:
  - Understanding industry dynamics is essential for evaluating a company's competitive position and [[Quantitative Trading Strategies Lecture Notes|credit risk]].
- **Financial Ratios**:
  - Traditional ratios like interest coverage,  [[Lecture 6-Leverage, Tail Risk, Volatility Products|leverage]],  and [[Preview of the Book|cash flow]] provide insights into financial health but must be interpreted in context.
- **Non-Financial Factors**:
  - Management quality,  foreign exposure,  and governance practices can significantly influence [[Wellman Inc the Importance of Loan Covenants|credit quality]].
- **Integrated Analysis**:
  - Combining financial and non-financial factors provides a comprehensive view of [[Quantitative Trading Strategies Lecture Notes|credit risk]].
- **Covenants**:
  - Indenture provisions play a critical role in protecting bondholders and influencing credit ratings.

This concludes the lecture notes on industry and [[Week 1 [[Squam Lake Group Introduction|Introduction]] to [[BMW Valuation|Financial Analysis]]|[[BMW Valuation|financial analysis]]]]  for credit evaluation. The next session will focus on advanced techniques for modeling [[Quantitative Trading Strategies Lecture Notes|credit risk]] and assessing [[Credit Markets Session 3|default probabilities]].

# Lecture Notes: Asset Quality Analysis in Finance Companies

## 1. Introduction to Asset Quality in Finance Companies
- **Contextual Analysis**:
  - Variables in finance companies should not be viewed in isolation but rather within the broader context of the relationship between the finance company and its parent company.
  - This interconnected view provides a more comprehensive understanding of the company's financial health and risk profile.
- **Importance of Asset Quality**:
  - Asset quality is the most critical variable in analyzing a finance company.
  - It directly impacts the company's profitability,  risk exposure,  and long-term sustainability.
  - While there is no definitive way to measure asset quality,  a combination of variables can provide a reliable indication of [[An Asset Allocation Primer|portfolio]] quality.

## 2. Key Variables in Assessing Asset Quality
### 2.1 Diversification
- **Definition**:
  - Diversification refers to the spread of a company's loan [[An Asset Allocation Primer|portfolio]] across different types of loans,  industries,  or geographic regions.
- **Importance**:
  - A [[Chapter 5 - Index Futures|diversified portfolio]] reduces risk by minimizing exposure to specific economic,  industry,  or regional downturns.
- **Types of Diversification**:
  - **Loan Type Diversification**:
	- A [[An Asset Allocation Primer|portfolio]] that includes a mix of consumer loans,  commercial loans,  and real estate loans is less risky than one concentrated in a single loan type.
  - **Geographic Diversification**:
	- Geographic spread mitigates the risk of localized [[How the Eggheads Cracked|economic downturns]].
	- Example:
	  - A company dealing exclusively in consumer loans in the economically sensitive Detroit area would be viewed less favorably than a company with broad geographic diversification across multiple regions.

### 2.2 Accounting Quality
- **Definition**:
  - Accounting quality refers to the accuracy,  transparency,  and reliability of a company's financial reporting practices.
- **Importance**:
  - High accounting quality ensures that the reported asset values and loan performance metrics accurately reflect the underlying economic reality.
- **Indicators of Accounting Quality**:
  - Conservative loan loss provisioning.
  - Transparent disclosure of non-performing loans (NPLs) and charge-offs.
  - Consistent application of accounting standards across reporting periods.

### 2.3 Loan Security
- **Definition**:
  - Loan security refers to the collateral or guarantees backing the loans in the [[An Asset Allocation Primer|portfolio]].
- **Importance**:
  - The stronger the underlying security,  the higher the quality of the loan.
  - Secured loans are less risky than unsecured loans because the collateral can be liquidated to recover losses in case of default.
- **Examples**:
  - **High-Quality Security**:
	- Loans secured by real estate,  vehicles,  or other tangible assets.
  - **Low-Quality Security**:
	- Unsecured loans or loans backed by [[Week 5 Accounting Recap- R&D, Intangibles, M&A & Goodwill#[[Week 5 Accounting Recap- R&D, Intangibles, M&A & Goodwill|INTANGIBLE AMORTIZATION]] AND NON‐GAAP REPORTING|intangible]] assets with limited resale value.

### 2.4 Loan Levels and Risk
- **Definition**:
  - Loan levels refer to the size and composition of the loan [[An Asset Allocation Primer|portfolio]] relative to similar companies in the industry.
- **Importance**:
  - Analysts should compare the company's loan levels with industry benchmarks to assess whether the company is overexposed to risky lending practices.
- **[[10. Other Topics in Quantitative Finance|Risk Assessment]]**:
  - The risk involved in the type of lending is a critical factor.
  - Example:
	- Direct unsecured loans typically have higher expected loan losses compared to secured loans.

## 3. Practical Considerations in Asset Quality Analysis
### 3.1 Aggregate View of Variables
- **Holistic Assessment**:
  - No single variable can definitively measure asset quality.
  - Analysts should consider all relevant variables—diversification,  accounting quality,  loan security,  and loan levels—in aggregate to form a comprehensive view of asset quality.

### 3.2 Industry and Economic Context
- **Economic Sensitivity**:
  - The performance of certain loan types is closely tied to [[US Debt Crisis and Adjustment (2007–2011)|economic conditions]].
  - Example:
	- Consumer loans in economically sensitive regions are more vulnerable to downturns.
- **Industry Benchmarks**:
  - Comparing the company's asset quality metrics with those of similar companies provides valuable context for evaluation.

## 4. Key Takeaways
- **Interconnected Variables**:
  - Asset quality should be analyzed within the broader context of the finance company–parent company relationship.
  - Diversification,  accounting quality,  loan security,  and loan levels are interrelated variables that collectively determine asset quality.
- **Risk Mitigation**:
  - A [[Chapter 5 - Index Futures|diversified portfolio]],  strong accounting practices,  and secured loans are key factors in mitigating risk and enhancing asset quality.
- **Comparative Analysis**:
  - Analysts should benchmark the company's asset quality metrics against industry standards and consider the economic environment to draw meaningful conclusions.
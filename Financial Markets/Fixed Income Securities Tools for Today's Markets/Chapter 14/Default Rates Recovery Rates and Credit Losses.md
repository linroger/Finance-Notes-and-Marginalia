---
tags:
  - bond_recovery
  - credit_losses
  - credit_risk
  - default_rates
  - hertz_bonds
  - investment_grade
  - recovery_rates
  - senior_unsecured_bonds
  - seniority
  - speculative_grade
aliases:
  - Bond Credit Risk
  - Credit Loss
  - Credit Risk Analysis
  - Default and Recovery
  - Hertz Bankruptcy
key_concepts:
  - Bond Recovery Rates
  - Credit Losses
  - Credit Risk Over Time
  - Default Rates
  - Hertz Bond Prices
  - Impact of Seniority
  - Investment Grade Bonds
  - Recovery Rates
  - Senior Unsecured Bonds
  - Speculative Grade Bonds
---

# 14.2 DEFAULT RATES, RECOVERY RATES, AND CREDIT LOSSES  

While investors in nearly risk-free government bonds can focus exclusively on [interest rate risk](../../../Fixed%20Income%20Asset%20Pricing/Analysis%20of%20Fixed%20Income%20Securities.md), investors in corporate securities have to focus on [credit risk](../../../Course%20Notes/Quantitative%20Trading%20Strategies%20Lecture%20Notes.md) as well, often expressed in terms of [default rates](.md), recovery rates, and credit losses. After analysis, an investor might estimate that, over a five-year horizon, a particular [portfolio](../../../Advanced%20Investments/An%20Asset%20Allocation%20Primer.md) of bonds will experience a default rate of $10\%$ , meaning that, for every. $\$100$ of face amount, $\$10$ will default. Further-. more, the investor might estimate that the defaulting bonds in the [portfolio](../../../Advanced%20Investments/An%20Asset%20Allocation%20Primer.md) will experience a [recovery rate](../../../Credit%20Markets/Credit%20Markets%20Session%203.md) of. $40\%$ of face amount, or, equivalently, will suffer a loss equal to the remaining $60\%$ of face amount. Putting these two estimates together, the investor expects, over a five-year horizon, that credit losses on the [portfolio](../../../Advanced%20Investments/An%20Asset%20Allocation%20Primer.md) will be $10\%\times(1-40\%)=6\%$  

Table 14.4 shows average historical values for these quantities, over. the period 1983-2020, for senior unsecured bonds, by rating. The results. are useful for appreciating the average magnitude of [credit risk](../../../Course%20Notes/Quantitative%20Trading%20Strategies%20Lecture%20Notes.md). For. [investment](../../../Advanced%20Investments/An%20Asset%20Allocation%20Primer.md)-grade senior unsecured bonds, the average five-year [default rates](.md) and recovery rates are $0.9\%$ and $44.5\%$ , respectively, giving an average [credit loss](.md) of $0.5\%$ . For speculative-grade senior unsecured bonds,. the average default rate is much higher, at $19.6\%$ , though the average [recovery rate](../../../Credit%20Markets/Credit%20Markets%20Session%203.md) is only marginally lower, at $38.3\%$ . Combining these two averages gives a much higher [credit loss](.md) of. $12.2\%$ . The standard assumption. in the industry that recovery rates are about. $40\%$ is justified by historical. data like those presented in Table 14.4.4  

While historical averages are useful in thinking about [credit risk](../../../Course%20Notes/Quantitative%20Trading%20Strategies%20Lecture%20Notes.md), credit conditions can vary dramatically over time. For example, extending the sample of Table 14.4 to include the years after the [Great Depression](../../../International%20Finance/Bridgewater/Chapters/US%20Debt%20Crisis%20and%20Adjustment%201928-1937.md) raises the five-year default rate on [investment](../../../Advanced%20Investments/An%20Asset%20Allocation%20Primer.md)-grade debt from $0.9\%$ to $1.4\%$ . And within the sample period of the table, Figure 14.1 shows the variability of credit losses for [investment](../../../Advanced%20Investments/An%20Asset%20Allocation%20Primer.md)-grade and high-yield bonds. High-yield losses were particularly high in the late 1980s, following the rapid growth in that market; in 2000-2002, which included the "dot-com" crash and the failures of Enron and WorldCom; in the [financial crisis](../../../Financial%20Markets%20and%20Institutions/III.%20Liquidity%20of%20Assets/Class%209-%20Bailouts%20and%20Bank%20Failures/Squam%20Lake%20Group%20Letter.md) of 2007-2009; in 2016, from stresses caused by low prices in energy markets; and, most recently, during the pandemic and economic shutdowns of 2020.  

TABLE 14.4 Average Five-Year [Default Rates](.md), Senior Unsecured Bond Recovery. Rates, and Credit Losses, 1983-2020. All Entries Are in Percent.   


<html><body><table><tr><td>Rating</td><td>Default Rate</td><td>[Recovery Rate](../../../Credit%20Markets/Credit%20Markets%20Session%203.md)</td><td>[Credit Loss](.md)</td></tr><tr><td>[Investment](../../../Advanced%20Investments/An%20Asset%20Allocation%20Primer.md) tGrade</td><td>0.9</td><td>44.5</td><td>0.5</td></tr><tr><td>Speculative Grade</td><td>19.6</td><td>38.3</td><td>12.2</td></tr><tr><td>All</td><td>7.4</td><td>38.9</td><td>4.6</td></tr></table></body></html>

Source: Moody's Investors Service  

![](7100c4ab25220fd7e141b7f626c1effd82004d80b78cdc53da82fff4a6441a51.jpg)  
FIGURE 14.1 Credit Losses for Senior Unsecured Bonds, 1983-2020. Source: Moody's Investors Service.  

Table 14.4 and Figure 14.1 report credit losses for senior unsecured bonds. [Investment](../../../Advanced%20Investments/An%20Asset%20Allocation%20Primer.md) outcomes vary significantly, however, across loans and bonds of different seniority. Over the same sample period as in the table and figure, Moody's reports that bond recovery rates were $22\%$ for junior sub-. ordinated; $38\%$ for senior unsecured; and $54\%$ for first lien (i.e., the highest priority secured claim). For bank loans, average recovery rates were $46\%$ for senior unsecured; $65\%$ for first lien; and. $32\%$ for second lien..  

A recent example of the [impact of seniority](.md), illustrated in Table 14.5, is the price behavior of Hertz bonds through its bankruptcy filing on May 22, 2020. Before the pandemic, as of February 21, 2020, when default was a remote contingency, the prices of Hertz' secured and unsecured bonds were above par, with the higher price of the unsecured reflecting its longer maturity at an above-market coupon. By May 14, 2020, after the pandemic and shutdowns devastated the rental car business, the prices of Hertz bonds plummeted, with the price of the secured bond now significantly higher: with default imminent, the seniority of the secured bonds was much more important than the seemingly distant prospect of the unsecured bond's cash flows through 2028. Soon after, however, in the wake of the economy's rapid recovery, Hertz's bond prices recovered dramatically as well. There was still much uncertainty as to the bonds' creditworthiness, however. The June 15, 2020, prices in the table show that the secured bonds still sold at a significant premium to the unsecured. By way of epilogue, Hertz emerged from bankruptcy at the end of June 2021, and its bonds recovered their full principal value.  

TABLE 14.5 Hertz Corporation, Selected Bond Prices on Three Dates in 2020.   


<html><body><table><tr><td>Priority</td><td>Coupon</td><td>Maturity</td><td>Feb 21</td><td>May 14</td><td>Jun 15</td></tr><tr><td>Sr. Secured 2nd Lien</td><td>7.625</td><td>06/01/2022</td><td>103.10</td><td>19.97</td><td>77.00</td></tr><tr><td>Sr. Unsecured</td><td>6.000</td><td>01/15/2028</td><td>104.29</td><td>11.25</td><td>43.50</td></tr></table></body></html>  

Potential credit losses are directly relevant for investors expecting to. hold bonds to maturity. Investors with shorter horizons, however, are also concerned about [credit deterioration](Case%20Study%20the%20London%20Whale.md), which causes bond prices to fall before a realized default and [credit loss](.md). One manifestation of credit changes are rating transitions, in which a rating agency upgrades or downgrades a rating. Table 14.6 gives average historical one-year transition rates, or, more specifically, the rates at which bonds starting at a particular rating, over the follow-. ing year, are upgraded, experience no change, are downgraded (including defaults), or become unrated. Becoming unrated may be a negative [credit event](../../../Financial%20Engineering/Valuation%20of%20Credit%20Default%20Swaps.md) but could also indicate a credit-neutral event like an acquisition. In any case, the table shows that downgrades over a one-year horizon are not uncommon, averaging from about $4\%$ to $10\%$ for bonds rated B or above, and over $28\%$ for CCC/C-rated bonds. Upgrades occur as well, but with less frequency. Though not shown in the table, upgrades and downgrades vary with the [business cycle](../../../International%20Finance/Economic%20Stabilization%20Notes/Business%20Cycles-%20Introduction,%20Characteristics,%20and%20History.md), like the credit losses in Figure 14.1.  

TABLE 14.6  Average One-Year Transition Rates, 1981-2020. All Entries Are in Percent.   


<html><body><table><tr><td>Rating</td><td>Upgrade</td><td>No Change</td><td>Downgrade</td><td>No Rating</td></tr><tr><td>AAA</td><td>0.0</td><td>87.1</td><td>9.8</td><td>3.1</td></tr><tr><td>AA</td><td>0.5</td><td>87.2</td><td>8.4</td><td>3.9</td></tr><tr><td>A</td><td>1.6</td><td>88.6</td><td>5.4</td><td>4.4</td></tr><tr><td>BBB</td><td>3.3</td><td>86.5</td><td>4.3</td><td>5.9</td></tr><tr><td>BB</td><td>4.7</td><td>77.8</td><td>8.0</td><td>9.5</td></tr><tr><td>B</td><td>4.8</td><td>74.6</td><td>8.3</td><td>12.3</td></tr><tr><td>CCC/C</td><td>13.3</td><td>43.1</td><td>28.3</td><td>15.3</td></tr></table></body></html>

Source: S&P Global Ratings; and Author Calculations  
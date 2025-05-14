---
tags:
  - american_futures_options
  - bond_futures
  - bond_futures_options
  - bsm_model
  - term_structure_model
aliases:
  - Bond Futures Options
  - Futures Options
key_concepts:
  - BSM approach
  - Bond futures options
  - Early exercise
  - European option
  - Term structure models
---

# 16.3 BOND FUTURES OPTIONS  

Bond [[Futures Not Subject to Cash-And-Carry|futures]] in the United States are discussed in Chapter 11. Options on these [[Mathematics of the Financial Markets|futures contracts]] are traditional or equity-style options, which means that, like options on stocks, purchasers of options pay a premium at the time of purchase and, if exercised, realize their intrinsic values.  

Options on bond [[Futures Not Subject to Cash-And-Carry|futures]] can be valued with [[Financial Mathematics Course|term structure models]]. In a [[Profit and Loss Attribution with an OAS|one-factor model]], for example, after creating a risk-neutral tree for the [[Futures Price and the Quality Option Before E|futures price]], the value of a [[Futures Not Subject to Cash-And-Carry|futures]] option can be computed by starting from the maturity date of the option and working backwards, using the rule that. the value of the option at each node is the maximum of the value of holding. the option and of exercising it immediately. Of course, because the delivery options embedded in bond [[Futures Not Subject to Cash-And-Carry|futures]] may not be modeled adequately by a. [[Profit and Loss Attribution with an OAS|one-factor model]], multi-factor approaches might be preferred..  

While simple conceptually, it is apparent from Chapter 11 that build-. ing a [[Futures Not Subject to Cash-And-Carry|futures]] model takes a good deal of effort. Therefore, practitioners who do not otherwise need such a model tend to use a [[Bond Futures Options|BSM approach]] for bond [[Futures Not Subject to Cash-And-Carry|futures]] options. The required assumptions are that: the option is European; the [[Discount Factors|discount factor]] to option expiration is uncorrelated with the underlying [[Futures Price and the Quality Option Before E|futures price]]; and the [[Futures Price and the Quality Option Before E|futures price]] is lognormal with constant volatility. The assumption that the option is European, that is, that [[Bond Futures Options|early exercise]] is not optimal, is reasonable in practice. [[Bond Futures Options|Early exercise]] of an equitystyle [[Futures Not Subject to Cash-And-Carry|futures]] option may be optimal if interest earned on the realized intrinsic value exceeds the time value of the option, but this is rarely the case. For some intuition on this point, note that [[Bond Futures Options|early exercise]] of a put on a stock may be optimal, because of the potential of earning interest on the entire [[Call and Put Payoffs at Expiry|strike price]], not just on its intrinsic value. The assumption that the [[Discount Factors|discount factor]] is uncorrelated with the bond [[Futures Price and the Quality Option Before E|futures price]] is not bad in practice. Bond [[Futures Not Subject to Cash-And-Carry|futures]] options typically mature in a few months or less, while the bond underlying the [[Futures Not Subject to Cash-And-Carry|futures]] contract typically matures in many years. Hence, the correlation is typically weak between the [[Discount Factors|discount factor]], which depends on very [[Volatility and Convexity|short-term rates]], and the bond [[Futures Price and the Quality Option Before E|futures price]], which depends on longer-term rates. The assumption of constant [[Black Models for Bond Price Options Capsfloors|price volatility]], however, essentially assumes away the delivery options of bond [[Futures Not Subject to Cash-And-Carry|futures]]: as rates change and the [[Tba and Specified Pools Markets|cheapest-to-deliver]] bond changes, the Dv01 and, therefore, the [[Black Models for Bond Price Options Capsfloors|price volatility]] of the [[Futures Not Subject to Cash-And-Carry|futures]] changes as well. (See Chapter 11.) While perhaps acceptable when [[Interest Rate Quotations|interest rates]] are low relative to the contract's notional coupon, ignoring the delivery option seems to undercut one of the main motivations for using BSM in the first place, namely, to obtain accurate deltas. Nevertheless, BSM is used in practice in this context.  

Under the assumptions listed in the previous paragraph, Appendix. A16.3 shows that calls and puts on US Treasury note and bond [[Mathematics of the Financial Markets|futures contracts]] are given by, respectively,.  
$$
\begin{array}{c}{{\S N\times d_{0}(T)\times\xi^{L N}(S_{0},T,K,\sigma)/100}}\ {{\S N\times d_{0}(T)\times\pi^{L N}(S_{0},T,K,\sigma)/100}}\end{array}
$$  

TABLE 16.4 A Call Option on the June 10-Year. [[Mechanics of Us Treasury Note and Bond Futures|Treasury Note Futures]] Contract, as of February 28, 2022. The [[Futures Not Subject to Cash-And-Carry|Futures]] Contract and Option Mature on. June 21, 2022.   


<html><body><table><tr><td>Quantity Value</td></tr><tr><td>So 126.3438</td></tr><tr><td>113 =0.3096</td></tr><tr><td>T 365</td></tr><tr><td>K 126.5 5.655%</td></tr><tr><td>d(T) 0.9979%</td></tr><tr><td>gLN(So, T, K,α) 1.50996</td></tr><tr><td>V。 = $100,000 × do(T)× gLN/100 $1,509.96</td></tr></table></body></html>  

where $N$ is the face amount of bonds per contract;. $S_{0}$ is the [[Futures Price and the Quality Option Before E|futures price]]; $T$ is the time to option expiration; $K$ is the [[Call and Put Payoffs at Expiry|strike price]]; $\sigma$ is the lognormal or percentage [[Black Models for Bond Price Options Capsfloors|price volatility]]; and. $d_{0}(T)$ is the [[Discount Factors|discount factor]] to option expiration. Table 16.4 applies Equation (16.6) to a call option on the June 10-year US [[Mechanics of Us Treasury Note and Bond Futures|Treasury note futures]] contract as of the end of February 2022, where both the [[Futures Not Subject to Cash-And-Carry|futures]] and option contracts expire on June 21, 2022. Note that there are 113 days from February 28, 2022, to June 21, 2022.  
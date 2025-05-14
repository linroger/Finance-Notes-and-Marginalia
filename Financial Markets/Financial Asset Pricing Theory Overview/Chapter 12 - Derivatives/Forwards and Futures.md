---
tags:
  - asset_pricing
  - forward_price
  - forwards_futures
  - futures_price
  - risk_neutral
  - zero_coupon_bond
aliases:
  - Forward Contracts
  - Forwards
  - Futures
key_concepts:
  - Forward price definition
  - Futures contract payoff
  - Risk-neutral probability measure
  - Underlying asset price
  - Zero-coupon bond pricing
---

# 12.2 Forwards and futures  

# 12.2.1 General results on forward prices and futures prices  

A forward with maturity date $T$ and delivery price $K$ provides a dividend of $P_{T}-K$ at time $T$ where $P$ is the underlying variable, typically the price of an asset or a specific interest rate. If you plan to buy a unit of an asset at time $T$ , you can lock in the effective purchase price with a forward on that asset. Conversely, if you plan to sell a unit of an asset, you can lock in the effective selling price by taking a short position in a forward on the asset, which will give a terminal dividend of $K-P_{T}$ . Of course, [[Forwards and Futures|forwards]] can also be used for speculation. If you believe in high values of $P_{T}$ you can take a [[Chapter 4 - Futures: Hedging and Speculation|long position]] in a forward. If you believe in low values of $P_{T}$ , you can take a short position in a forward.  

In terms of a [[Pricing Forwards, Futures, Bonds, Swaps, Swaptions, Caps and Floors under No-Arbitrage and Risk-Neutral Pricing|risk-neutral probability measure]] $\mathbb{Q}$ , the time $t$ value of such a future payoff can be. written as  
$$
\begin{array}{r l}&{V_{t}=\mathrm{E}_{t}^{\mathbb{Q}}\left[\left(R_{t,T}^{f}\right)^{-1}\left(P_{T}-K\right)\right]}\ &{\quad=\mathrm{E}_{t}^{\mathbb{Q}}\left[\left(R_{t,T}^{f}\right)^{-1}P_{T}\right]-K\mathrm{E}_{t}^{\mathbb{Q}}\left[\left(R_{t,T}^{f}\right)^{-1}\right]}\ &{\quad=\mathrm{E}_{t}^{\mathbb{Q}}\left[\left(R_{t,T}^{f}\right)^{-1}P_{T}\right]-K B_{t}^{T},}\end{array}
$$  

where $B_{t}^{T}=\mathrm{E}_{t}^{\Psi}[(R_{t,T}^{f})^{-1}]$ is the price of the zero-coupon bond maturing at time $T$ with a unit. payment. Here $R_{t,T}^{f}$ is the gross return between time $t$ and $T$ on the bank account, i.e. a roll-over in short risk-free investments, cf. the discussion in Section 11.3.  

For [[Forwards and Futures|forwards]] contracted upon at time $t$ , the delivery price $K$ is typically set so that the value of. the forward at time $t$ is zero. This value of. $K$ is called the [[Forward Contracts and Forward Prices|forward price]] at time $t$ (for the delivery date $T$ ) and is denoted by $F_{t}^{\prime I^{\prime}}$ . We define the terminal [[Forward Contracts and Forward Prices|forward price]] to be $F_{T}^{T}=P_{T}$ , the only  

reasonable price for immediate delivery. Solving the equation $V_{t}=0$ , we get that the [[Forward Contracts and Forward Prices|forward price]]. is given by  
$$
F_{t}^{T}=\frac{\mathrm{E}_{t}^{\mathbb{Q}}\left[\left(R_{t,T}^{f}\right)^{-1}P_{T}\right]}{B_{t}^{T}}.
$$  

If the underlying variable is the price of a traded asset with no payments in the period $[t,T]$ , we have  
$$
\begin{array}{r}{\mathrm{E}_{t}^{\mathbb{Q}}\left[\left(R_{t,T}^{f}\right)^{-1}P_{T}\right]=P_{t},}\end{array}
$$  

so that the [[Forward Contracts and Forward Prices|forward price]] can be written as $F_{t}^{\prime I^{\prime}}=P_{t}/B_{t}^{\prime I^{\prime}}$ . Applying a well-known property of.   
covariances, we have that.  
$$
\begin{array}{r l}&{\mathrm{E}_{t}^{\mathbb{Q}}\left[\left(R_{t,T}^{f}\right)^{-1}P_{T}\right]=\mathrm{Cov}_{t}^{\mathbb{Q}}\left[\left(R_{t,T}^{f}\right)^{-1},P_{T}\right]+\mathrm{E}_{t}^{\mathbb{Q}}\left[\left(R_{t,T}^{f}\right)^{-1}\right]\mathrm{E}_{t}^{\mathbb{Q}}[P_{T}]}\ &{\qquad=\mathrm{Cov}_{t}^{\mathbb{Q}}\left[\left(R_{t,T}^{f}\right)^{-1},P_{T}\right]+B_{t}^{T}\mathrm{E}_{t}^{\mathbb{Q}}[P_{T}]}\end{array}
$$  

and therefore  
$$
F_{t}^{T}=\mathrm{E}_{t}^{\mathbb{Q}}[P_{T}]+\frac{\operatorname{Cov}_{t}^{\mathbb{Q}}\left[\left(R_{t,T}^{f}\right)^{-1},P_{T}\right]}{B_{t}^{T}}.
$$  

We can also characterize the [[Forward Contracts and Forward Prices|forward price]] in terms of the forward measure for maturity $T$ . The [[Forward Contracts and Forward Prices|forward price]] process for contracts with delivery date. $T$ is a $\mathbb{Q}^{T}$ -martingale. This is clear from the following considerations. With $B_{t}^{T^{\prime}}$ as the numeraire, we have that the [[Forward Contracts and Forward Prices|forward price]]. $F_{t}^{\prime I^{\prime}}$ is set so that  
$$
\frac{0}{B_{t}^{T}}=\mathrm{E}_{t}^{\mathbb{Q}^{T}}\left[\frac{P_{T}-F_{t}^{T}}{B_{T}^{T}}\right]
$$  

and hence  
$$
{\boldsymbol{F}}_{t}^{T}={\mathrm{E}}_{t}^{\mathbb{Q}^{T}}[P_{T}]={\mathrm{E}}_{t}^{Q^{T}}[F_{T}^{T}],
$$  

which implies that the [[Forward Contracts and Forward Prices|forward price]] $F_{t}^{T}$ is a $\mathbb{Q}^{T}$ - martingale.  

We summarize our findings in the following theorem.  

Theorem 12.1 The [[Forward Contracts and Forward Prices|forward price]] for delivery at time $T$ is given by  
$$
F_{t}^{T}=\frac{\boldsymbol{\mathrm{E}}_{t}^{\mathbb{Q}}\left[\left(R_{t,T}^{f}\right)^{-1}P_{T}\right]}{\boldsymbol{B}_{t}^{T}}=\boldsymbol{\mathrm{E}}_{t}^{\mathbb{Q}^{T}}[P_{T}].
$$  

If the underlying variable is the price of a traded asset with no payments in the period $\lfloor t,T\rfloor$ , the [[Forward Contracts and Forward Prices|forward price]] can be written as  
$$
F_{t}^{T}=\frac{P_{t}}{B_{t}^{T}}.
$$  

Note that when (12.3) holds, the [[Forward Contracts and Forward Prices|forward price]] of an asset follows immediately from the spot price of the asset and the price of the zero-coupon bond maturing at the delivery date. No model for the [[Chapter 47 - Asset Price Dynamics|price dynamics]] of the [[Risk Neutral Pricing of Options|underlying asset]] is needed. This is because the forward is perfectly replicated by a [[An Asset Allocation Primer|portfolio]] of one unit of the [[Risk Neutral Pricing of Options|underlying asset]] and a short position in $K$ zero-coupon bonds maturing at the delivery date of the forward.  

Consider now a [[Futures Not Subject to Cash-And-Carry|futures]] contract with final settlement at time. $T$ . The marking-to-market at a. given date involves the payment of the change in the so-called [[Futures Price and the Quality Option Before E|futures price]] of the contract relative to the previous settlement date.Let $\Phi_{t}^{T}$ be the [[Futures Price and the Quality Option Before E|futures price]] at time $t$ .The [[Futures Price and the Quality Option Before E|futures price]] at the settlement time is by definition equal to the price of the underlying security, $\Phi_{T}^{I^{\prime}}=P_{T}$ .At maturity of the contract the [[Futures Not Subject to Cash-And-Carry|futures]] thus gives a payoff equal to the difference between the price of the [[Risk Neutral Pricing of Options|underlying asset]] at that date and the [[Futures Price and the Quality Option Before E|futures price]] at the previous settlement date. After the last settlement before maturity, the [[Futures Not Subject to Cash-And-Carry|futures]] is therefore indistinguishable from the corresponding [[Forward Points in Currency|forward contract]], so the values of the [[Futures Not Subject to Cash-And-Carry|futures]] and the forward at that settlement date must be identical. At the next-to-last settlement date before maturity, the [[Futures Price and the Quality Option Before E|futures price]] is set to that value that ensures that the net present value of the upcoming settlement at the last settlement date before maturity (which depends on this [[Futures Price and the Quality Option Before E|futures price]]) and the final payoff is equal to zero. Similarly at earlier settlement dates. We assume that the [[Futures Not Subject to Cash-And-Carry|futures]] is marked-to-market at every trading date considered in the model. In the [[Multi-Period Valuation Models|discrete-time framework]], the dividend from the [[Futures Not Subject to Cash-And-Carry|futures]] at time $t+1$ is therefore $\Phi_{t+1}^{T}-\Phi_{t}^{T}$ . In a [[The Continuous-Time Framework|continuous-time setting]], the dividend over any infinitesimal interval $[t,t+d t]$ is $d\Phi_{t}^{T}$ . The following theorem characterizes the [[Futures Price and the Quality Option Before E|futures price]]:  

Theorem 12.2 The [[Futures Price and the Quality Option Before E|futures price]]. $\Phi_{t}^{T}$ is a martingale under the [[Pricing Forwards, Futures, Bonds, Swaps, Swaptions, Caps and Floors under No-Arbitrage and Risk-Neutral Pricing|risk-neutral probability measure]] $\mathbb{Q}$ In particular,  
$$
\Phi_{t}^{T}=\operatorname{E}_{t}^{\mathbb{Q}}\left[P_{T}\right].
$$  

Proof: We give a proof in the [[Multi-Period Valuation Models|discrete-time framework]], a proof originally due to Cox, Ingersoll, and Ross (1981b). Then the continuous-time version of the result follows by taking a limit. For a proof based on the same idea but formulated directly in continuous time, see Duffie and Stanton (1992).  

Consider a discrete-time setting in which positions can be changed and the [[Mathematics of the Financial Markets|futures contracts]] marked-to-market at times $t,t+\Delta t,t+2\Delta t,...,t+N\Delta t\equiv T$ . Let $R_{t}^{f}$ denote the risk-free gross retun between t and t + At and let R,+nst = R R+4t  R+(n-1)st: The idea is to set up a self-financing strategy that requires an initial [[An Asset Allocation Primer|investment]] at time $t$ equal to the [[Futures Price and the Quality Option Before E|futures price]] $\Phi_{t}^{T}$ . Hence, at time. $t$ $\Phi_{t}^{T}$ is invested in the bank account. In addition, $R_{t}^{f}$ [[Mathematics of the Financial Markets|futures contracts]] are acquired (at a price of zero).  

At time $t+\Delta t$ , the deposit at the bank account has grown to $R_{t}^{f}\Phi_{t}^{T}$ . The marking-to-market of. the [[Futures Not Subject to Cash-And-Carry|futures]] position yields a payoff of $R_{t}^{f}\left(\Phi_{t+\Delta t}^{T}-\Phi_{t}^{T}\right)$ , which is deposited at the bank account,. so that the balance of the ccount becomes $R_{t}^{f}\Phi_{t+\Delta t}^{T}$ . The position in futuesi ncresed (at no extra costs) toa total of $R_{t}^{f}R_{t+\Delta t}^{f}=R_{t,t+2\Delta t}^{f}$ contracts.  

At time $t+2\Delta t$ , the deposit has grown to. $R_{t,t+2\Delta t}^{f}\Phi_{t+\Delta t}^{T}$ , which together with the marking-tomarket payment ofd $R_{t,t+2\Delta t}^{f}\left(\Phi_{t+2\Delta t}^{T}-\Phi_{t+\Delta t}^{T}\right)$ gives a total ofd $R_{t,t+2\Delta t}^{f}\Phi_{t+2\Delta t}^{T}$  

Continuing this way, the balance of the bank account at time $T=t+N\Delta t$ will be  
$$
R_{t,t+N\Delta t}^{f}\Phi_{t+N\Delta t}^{T}=R_{t,T}^{f}\Phi_{T}^{T}=R_{t,T}^{f}P_{T}.
$$  

This is true for any value of $\Delta t$ and $\Delta t=1$ covers our standard [[Multi-Period Valuation Models|discrete-time framework]] and $\Delta t\rightarrow0$ gives the continuous-time limit.  

So a [[Arbitrage|self-financing trading strategy]] with an initial time $t$ [[An Asset Allocation Primer|investment]] of. $\Phi_{t}^{T}$ will give a dividend of $R_{t,T}^{f}P_{T}$ at time $T$ . On the other hand, we can value the time $T$ dividend by multiplying by $(R_{t,T}^{f})^{-1}$ and taking the [[Risk-Neutral Probabilities|risk-neutral expectation]]. Hence,  
$$
\boldsymbol{\Phi}_{t}^{T}=\mathrm{E}_{t}^{\mathbb{Q}}\left[\left(R_{t,T}^{f}\right)^{-1}R_{t,T}^{f}P_{T}\right]=\mathrm{E}_{t}^{\mathbb{Q}}[P_{T}],
$$  

as was to be shown.  

Note that in order to compute the [[Futures Price and the Quality Option Before E|futures price]] of an asset we generally have to model the dynamics of the underlying spot price..  

Comparing (12.4) with (11.12), we see that we can think of the [[Futures Price and the Quality Option Before E|futures price]] as the price of a traded asset with a [[Hedging Strategies with Forwards|continuous dividend]] given by the product of the current price and the shortterm interest rate.  

From (12.1) and (12.4) we get that the difference between the [[Forward Contracts and Forward Prices|forward price]] $F_{t}^{T}$ and the [[Futures Price and the Quality Option Before E|futures price]] $\Phi_{t}^{T}$ is given by  
$$
F_{t}^{T}-\Phi_{t}^{T}=\frac{\mathrm{Cov}_{t}^{\mathbb{Q}}\left[\left(R_{t,T}^{f}\right)^{-1},P_{T}\right]}{B_{t}^{T}}.
$$  

The [[Forward Contracts and Forward Prices|forward price]] and the [[Futures Price and the Quality Option Before E|futures price]] will only be identical if the two random variables $P_{T}$ and $(R_{t,T}^{f})^{-1}$ are uncorrelated under the [[Pricing Forwards, Futures, Bonds, Swaps, Swaptions, Caps and Floors under No-Arbitrage and Risk-Neutral Pricing|risk-neutral probability measure]]. In particular, this is true if. the short-term [[Black Scholes Derivation|risk-free rate]] is constant or deterministic..  

The [[Forward Contracts and Forward Prices|forward price]] is larger [smaller] than the [[Futures Price and the Quality Option Before E|futures price]] if the variables $(R_{t,T}^{f})^{-1}$ and $P_{T}$ are positively [negatively] correlated under the [[Pricing Forwards, Futures, Bonds, Swaps, Swaptions, Caps and Floors under No-Arbitrage and Risk-Neutral Pricing|risk-neutral probability measure]]. An intuitive,. heuristic argument for this goes as follows. If the [[Forward Contracts and Forward Prices|forward price]] and the [[Futures Price and the Quality Option Before E|futures price]] are identical,. the total undiscounted payments from the [[Futures Not Subject to Cash-And-Carry|futures]] contract will be equal to the terminal payment. of the forward. Suppose the interest rate and the spot price of the [[Risk Neutral Pricing of Options|underlying asset]] are positively. correlated, which ought to be the case whenever. $(R_{t,T}^{f})^{-1}$ and $P_{T}$ are negatively correlated. Then the marking-to-market payments of the [[Futures Not Subject to Cash-And-Carry|futures]] tend to be positive when the interest rate is high. and negative when the interest rate is low. So positive payments can be reinvested at a high interest rate, whereas negative payments can be financed at a low interest rate. With such a correlation, the [[Futures Not Subject to Cash-And-Carry|futures]] contract is clearly more attractive than a [[Forward Points in Currency|forward contract]] when the [[Futures Price and the Quality Option Before E|futures price]] and the [[Forward Contracts and Forward Prices|forward price]] are identical. To maintain a zero initial value of both contracts, the [[Futures Price and the Quality Option Before E|futures price]]. has to be larger than the [[Forward Contracts and Forward Prices|forward price]]. Conversely, if the sign of the correlation is reversed..  

If the [[Risk Neutral Pricing of Options|underlying asset]] has a constant or deterministic volatility and pays no dividends before time $T$ , we can write the risk-neutral [[Chapter 47 - Asset Price Dynamics|price dynamics]] as.  
$$
d P_{t}=P_{t}\left[r_{t}d t+\sigma(t)d z_{t}^{\mathbb{Q}}\right],
$$  

where $z^{\mathbb{Q}}=(z_{t}^{\mathbb{Q}})$ is a standard [[Continuous-Time Stochastic Processes|Brownian motion]] under the [[Verifying Martingale Property with Q|risk-neutral measure]] $\mathbb{Q}$ . If, furthermore, the short-term [[Black Scholes Derivation|risk-free rate]] is constant or follows a Gaussian process as for example in the [[Vasicek Short Rate Model|Vasicek model]] introduced in Section 10.5.1, the future values of $P_{T}$ will be lognormally distributed under the [[Verifying Martingale Property with Q|risk-neutral measure]]. In that case, the [[Futures Price and the Quality Option Before E|futures price]] can be stated in closed form. In. Exercise 12.6 you are asked to compute and compare the [[Forward Contracts and Forward Prices|forward price]] and the [[Futures Price and the Quality Option Before E|futures price]] on a. zero-coupon bond under the assumptions of the [[Vasicek Short Rate Model|Vasicek model]] of interest rate dynamics introduced. in Section 10.5.1.  

# 12.2.2 Interest rates forwards and futures  

Forward [[Interest Rate Quotations|interest rates]] are rates for a future period relative to the time where the rate is set. Many. participants in the [[Financial Markets and Institutions Lecture Notes|financial markets]] may on occasion be interested in \*locking in' an interest rate. for a future period, either in order to hedge risk involved with varying [[Interest Rate Quotations|interest rates]] or to speculate in specific changes in [[Interest Rate Quotations|interest rates]]. In the money markets the agents can lock in an interest rate by entering a [[Forward Points in Currency|forward rate]] agreement (FRA). Suppose the relevant future period is the time interval between $T$ and $S$ , where $S>T$ .In principle, a [[Forward Points in Currency|forward rate]] agreement with a face value $H$ and a contract rate of $K$ involves two payments: a payment of. $-H$ at time $T$ and a payment of $H[1+(S-T)K]$ at time $S$ . (Of course, the payments to the other part of the agreement are $H$ at time $T$ and $-H[1+(S-T)K]$ at time $S$ .) In practice, the contract is typically settled at time $T$ so that the two payments are replaced by a single payment of $B_{T}^{S}H[1+(S-T)K]-H$ at time $T$ Usually the contract rate $K$ is set so that the present value of the future payment(s) is zero at the time the contract is made. Suppose the contract is made at time $t<T$ . Then the time. $t$ value of the two future payments of the contract is equal to $-H B_{t}^{I^{\prime}}+H[1+(S-T)K]B_{t}^{S}$ . This is zero. if and only if.  
$$
K=\frac{1}{S-T}\left(\frac{B_{t}^{T}}{B_{t}^{S}}-1\right)=L_{t}^{T,S},
$$  

cf. (10.6), i.e. when the contract rate equals the [[Forward Points in Currency|forward rate]] prevailing at time $t$ for the period bet ween $T$ and $S$ . For this contract rate, we can think of the [[Forward Points in Currency|forward rate]] agreement having a single payment at time $T$ , which is given by.  
$$
B_{T}^{S}H[1+(S-T)K]-H=H\left(\frac{1+(S-T)L_{t}^{T,S}}{1+(S-T)l_{T}^{S}}-1\right)=\frac{(S-T)(L_{t}^{T,S}-l_{T}^{S})H}{1+(S-T)l_{T}^{S}}.
$$  

The numerator is exactly the interest lost by lending out. $H$ from time $T$ to time $S$ at the [[Forward Points in Currency|forward rate]] given by the FRA rather than the realized [[The Foreign Exchange Market Annotations|spot rate]]. Of course, this amount may be negative, so that a gain is realized. The division by. $1+(S-T)l_{T}^{S}$ corresponds to discounting the gain/loss from time $S$ back to time $T$  

[[Chapter 12 - Hedging with Interest Rate Futures|Interest rate futures]] trade with a very high volume at several international exchanges, e.g. CME (Chicago Mercantile Exchange), LIFFE (London [[Lecture Notes on International Finance|International Financial]] [[Futures Not Subject to Cash-And-Carry|Futures]] $\&$ Options Exchange), and MATIF (Marche a Terme International de France). The CME [[Chapter 12 - Hedging with Interest Rate Futures|interest rate futures]] involve the three-month Eurodollar deposit rate and are called [[Convexity-Adjusted Models for LIBOR Forwards Qu|Eurodollar futures]]. The interest rate involved in the [[Mathematics of the Financial Markets|futures contracts]] traded at LIFFE and MATIF is the three-month LIBOR rate on the Euro [[Forwards and Futures Notes|currency]]. We shall simply refer to all these contracts as [[Convexity-Adjusted Models for LIBOR Forwards Qu|Eurodollar futures]] and refer to the underlying interest rate as the three-month LIBOR rate, whose value at time. $t$ we denote by lt+0.25  

The price quotation of [[Convexity-Adjusted Models for LIBOR Forwards Qu|Eurodollar futures]] is a bit complicated since the amounts paid in the marking-to-market settlements are not exactly the changes in the quoted [[Futures Price and the Quality Option Before E|futures price]]. We must therefore distinguish between the quoted [[Futures Price and the Quality Option Before E|futures price]], $\ddot{\mathcal{E}}_{t}^{T}$ , and the actual [[Futures Price and the Quality Option Before E|futures price]], $\mathcal{E}_{t}^{T}$ , with the settlements being equal to changes in the actual [[Futures Price and the Quality Option Before E|futures price]]. At the maturity date of the contract, $T$ , the quoted [[Convexity-Adjusted Models for LIBOR Forwards Qu|Eurodollar futures]] price is defined in terms of the prevailing three-month LIBOR rate according to the relation  
$$
\tilde{\mathcal{E}}_{T}^{T}=100\left(1-l_{T}^{T+0.25}\right),
$$  

which using (10.5) on page 246 can be rewritten as  
$$
\tilde{\mathcal{E}}_{T}^{T}=100\left(1-4\left(\frac{1}{B_{T}^{T+0.25}}-1\right)\right)=500-400\frac{1}{B_{T}^{T+0.25}}.
$$  

Traders and analysts typically transform the [[Convexity-Adjusted Models for LIBOR Forwards Qu|Eurodollar futures]] price to an interest rate, the socalled LIBOR [[Futures Not Subject to Cash-And-Carry|futures]] rate, which we denote by. $\varphi_{t}^{T}$ and define by  
$$
\varphi_{t}^{T}=1-\frac{\tilde{\mathcal{E}}_{t}^{T}}{100}\quad\Leftrightarrow\quad\tilde{\mathcal{E}}_{t}^{T}=100\left(1-\varphi_{t}^{T}\right).
$$  

It follows from (12.7) that the LIBOR [[Futures Not Subject to Cash-And-Carry|futures]] rate converges to the three-month LIBOR [[The Foreign Exchange Market Annotations|spot rate]], as the maturity of the [[Futures Not Subject to Cash-And-Carry|futures]] contract approaches.  

The actual [[Convexity-Adjusted Models for LIBOR Forwards Qu|Eurodollar futures]] price is given by  
$$
\mathcal{E}_{t}^{T}=100-0.25\big(100-\tilde{\mathcal{E}}_{t}^{T}\big)=\frac{1}{4}\left(300+\tilde{\mathcal{E}}_{t}^{T}\right)=100-25\varphi_{t}^{T}
$$  

per 100 dollars of nominal value. It is the change in the actual [[Futures Price and the Quality Option Before E|futures price]] which is exchanged. in the marking-to-market settlements. At the CME the nominal value of the [[Convexity-Adjusted Models for LIBOR Forwards Qu|Eurodollar futures]] is 1 million dollars. A quoted [[Futures Price and the Quality Option Before E|futures price]] of. $\dot{\mathcal{E}}_{t}^{T}=94.47\$ corresponds to a LIBOR [[Futures Not Subject to Cash-And-Carry|futures]] rate of $5.53\%$ and an actual [[Futures Price and the Quality Option Before E|futures price]] of  
$$
{\frac{1000000}{100}}\cdot[100-25\cdot0.0553]=986175.
$$  

If the quoted [[Futures Price and the Quality Option Before E|futures price]] increases to 94.48 the next day, corresponding to a drop in the LIBOR [[Futures Not Subject to Cash-And-Carry|futures]] rate of one basis point (0.01 percentage points), the actual [[Futures Price and the Quality Option Before E|futures price]] becomes.  
$$
{\frac{1000000}{100}}\cdot[100-25\cdot0.0552]=986200.
$$  

An investor with a [[Chapter 4 - Futures: Hedging and Speculation|long position]] will therefore receive $986200-986175=25$ dollars at the settlement at the end of that day..  

If we simply sum up the individual settlements without discounting them to the terminal date, the total gain on a [[Chapter 4 - Futures: Hedging and Speculation|long position]] in a [[Convexity-Adjusted Models for LIBOR Forwards Qu|Eurodollar futures]] contract from $t$ to expiration at $T$ is given by  
$$
\mathcal{E}_{T}^{T}-\mathcal{E}_{t}^{T}=\left(100-25\varphi_{T}^{T}\right)-\left(100-25\varphi_{t}^{T}\right)=-25\left(\varphi_{T}^{T}-\varphi_{t}^{T}\right)
$$  

per 100 dollars of nominal value, i.e. the total gain on a contract with nominal value $H$ is equal to $-0.25\left(\varphi_{T}^{T}-\varphi_{t}^{T}\right)H$ . The gain will be positive if the three-month [[The Foreign Exchange Market Annotations|spot rate]] at expiration turns. out to be below the [[Futures Not Subject to Cash-And-Carry|futures]] rate when the position was taken. Conversely for a short position. The gain/loss on a [[Convexity-Adjusted Models for LIBOR Forwards Qu|Eurodollar futures]] contract is closely related to the gain/loss on a [[Forward Points in Currency|forward rate]] agreement, as can be seen from substituting. $S=T+0.25$ into (12.6). Recall that the rates $\varphi_{T}^{T}$ and $l_{T}^{T+0.25}$ are identical. However, it should be emphasized that in general the [[Futures Not Subject to Cash-And-Carry|futures]] rate $\varphi_{t}^{T}$ and the [[Forward Points in Currency|forward rate]] $L_{t}^{T,T+0.25}$ will be different due to the marking-to-market of the [[Futures Not Subject to Cash-And-Carry|futures]] contract.  

The final settlement is based on the terminal actual [[Futures Price and the Quality Option Before E|futures price]]  
$$
\begin{array}{l}{{\mathcal{E}_{T}^{T}\equiv100-0.25\left(100-\tilde{\mathcal{E}}_{T}^{T}\right)}}\ {{\mathrm{~}=100-0.25\left(400\left[(B_{T}^{T+0.25})^{-1}-1\right]\right)}}\ {{\mathrm{~}=100\left[2-(B_{T}^{T+0.25})^{-1}\right].}}\end{array}
$$  

It follows from Theorem 12.2 that the actual [[Futures Price and the Quality Option Before E|futures price]] at any earlier point in time $t$ can be computed as  
$$
\mathcal{E}_{t}^{T}=\mathrm{E}_{t}^{\mathbb{Q}}\left[\mathcal{E}_{T}^{T}\right]=100\left(2-\mathrm{E}_{t}^{\mathbb{Q}}\left[(B_{T}^{T+0.25})^{-1}\right]\right).
$$  

The quoted [[Futures Price and the Quality Option Before E|futures price]] is therefore  
$$
\tilde{\mathcal{E}}_{t}^{T}=4\mathcal{E}_{t}^{T}-300=500-400\mathrm{E}_{t}^{\mathbb{Q}}\left[(B_{T}^{T+0.25})^{-1}\right].
$$  

In several models of interest rate dynamics and bond prices, including the [[The Vasicek Model|Vasicek]] and CoxIngersoll-Ross models introduced in Chapter 10, the expectation in (12.8) can be computed in closed form; see, e.g., Munk (2005).  
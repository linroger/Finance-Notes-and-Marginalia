---
title: Pricing Forwards, Futures, Bonds, Swaps, Swaptions, Caps And Floors Under No-Arbitrage And Risk-Neutral Pricing
tags:
  - complete_market
  - derivative_pricing
  - financial_instruments
  - no_arbitrage_pricing
  - risk_neutral_valuation
aliases:
  - Derivative Valuation
  - No-Arbitrage Pricing
  - Pricing Derivatives
  - Risk-Neutral Valuation
key_concepts:
  - Expected payoffs, discounting
  - Fundamental theorem
  - Law of one price
  - No-arbitrage, riskless profit
  - Pricing PDE
  - Replicating portfolio
  - Risk-neutral probability measure

 
---
# **Introduction**

In modern financial theory, **[[Pricing Forwards, Futures, Bonds, Swaps, Swaptions, Caps and Floors under No-Arbitrage and Risk-Neutral Pricing|no-arbitrage pricing]]** and **risk-neutral valuation** form the cornerstone for valuing derivative instruments. _No-arbitrage_ means there are no opportunities to make a riskless profit with zero net [[An Asset Allocation Primer|investment]] – put simply, markets adjust so that no “free lunch” is possible . Under this principle, the price of any financial instrument is constrained by the _law of one price_: two portfolios with identical future payoffs must have the same current price. The **[[Pricing Forwards, Futures, Bonds, Swaps, Swaptions, Caps and Floors under No-Arbitrage and Risk-Neutral Pricing|fundamental theorem]] of [[Fixed Income Asset Pricing|asset pricing]]** formalizes this: a market is [[Arbitrage Pricing of Derivatives|arbitrage]]-free if and only if there exists at least one **[[Pricing Forwards, Futures, Bonds, Swaps, Swaptions, Caps and Floors under No-Arbitrage and Risk-Neutral Pricing|risk-neutral probability measure]]** (also called an equivalent martingale measure) under which discounted asset prices follow a martingale (have _fair game_ expected changes) . Intuitively, a _risk-neutral measure_ is a set of probabilities such that all assets earn the [[Black Scholes Derivation|risk-free rate]] $r$ – investors are “indifferent to risk” under this measure, so expected [[Assets|returns]] in the [[Arbitrage Pricing of Derivatives|pricing]] model equal $r$. [[Pricing Forwards, Futures, Bonds, Swaps, Swaptions, Caps and Floors under No-Arbitrage and Risk-Neutral Pricing|Pricing derivatives]] in an [[Exercises|arbitrage-free market]] can thus be done by taking _expected payoffs under the [[Financial Instruments|risk-neutral probabilities]] and discounting at the risk-free rate_. This is the essence of **[[Financial Mathematics Course|risk-neutral pricing]]** .

  

**Risk-Neutral Valuation:** If $X_T$ is a payoff at future time $T$, and $B(0,T)=e^{-rT}$ is the [[Discount Factors|discount factor]] (for constant $r$), then the [[Exercises|no-arbitrage price]] at time 0 is given by the discounted [[Risk-Neutral Probabilities|risk-neutral expectation]]: $$V_0 = B(0,T);\mathbb{E}^Q[X_T] = e^{-rT},\mathbb{E}^Q[X_T],,$$ where $\mathbb{E}^Q$ denotes expectation under the [[Verifying Martingale Property with Q|risk-neutral measure]] $Q$. For example, the [[Appendix 5.A Taxes and the Forward Price|no-arbitrage forward price]] $F_0(T)$ of an asset for delivery at time $T$ must equal $\mathbb{E}^Q[S_T]$ grown at $r$, so $F_0(T)=S_0 e^{rT}$ (we will derive this shortly). Similarly, the [[Exercises|no-arbitrage price]] of a call option is $C_0 = e^{-rT},\mathbb{E}^Q[(S_T - K)_+]$ . These results hold _regardless of investors’ risk aversion_, relying only on [[Forward Contracts and Forward Prices|arbitrage arguments]] and [[Forward and Futures Contracts|replication]]. In a **complete market** (one where every payoff can be replicated by trading [[Rate and Price Trees|underlying securities]]), the [[Verifying Martingale Property with Q|risk-neutral measure]] is unique, and thus derivative prices are uniquely determined by no-[[Arbitrage Pricing of Derivatives|arbitrage]].

  

**[[Forward and Futures Contracts|Replication]] and [[Arbitrage Pricing of Derivatives|Pricing]]:** [[Pricing Forwards, Futures, Bonds, Swaps, Swaptions, Caps and Floors under No-Arbitrage and Risk-Neutral Pricing|No-arbitrage pricing]] can be approached via two dual perspectives: (1) constructing a **[[Pricing Forwards, Futures, Bonds, Swaps, Swaptions, Caps and Floors under No-Arbitrage and Risk-Neutral Pricing|replicating portfolio]]** that perfectly replicates the derivative’s payoff and equating its cost to the derivative’s price (the classic approach used in the Black–Scholes derivation), or (2) directly computing the **risk-neutral expected payoff** and discounting. Both approaches yield the same result when markets are [[Arbitrage Pricing of Derivatives|arbitrage]]-free. In continuous time, [[Forward and Futures Contracts|replication]] leads to a **[[Pricing Forwards, Futures, Bonds, Swaps, Swaptions, Caps and Floors under No-Arbitrage and Risk-Neutral Pricing|pricing PDE]]** (e.g. the Black–Scholes equation), while risk-neutral valuation uses probabilistic tools (e.g. martingales and expectation under $Q$). In practice, [[Financial Mathematics Course|risk-neutral pricing]] is often more convenient for complex [[Chapter 9 Arbitrage and Hedging With Options|derivatives]]: one assumes the [[Risk Neutral Pricing of Options|underlying asset]]’s **drift** under $Q$ is the [[Black Scholes Derivation|risk-free rate]] $r$, simulates or analytically evaluates the payoff’s expectation, then discounts. Below, we will apply these principles to price a range of instruments: [[Forwards and Futures|forwards]], [[Futures Not Subject to Cash-And-Carry|futures]], bonds, swaps, swaptions, caps, [[Caps and Floors|floors]], and related [[Chapter 9 Arbitrage and Hedging With Options|derivatives]]. We develop formal [[Arbitrage Pricing of Derivatives|pricing]] formulas with **step-by-step derivations**, using consistent notation and an academic tone. Key results from foundational texts (Hull, Shreve, Duffie, etc.) and seminal papers (Black–Scholes 1973, Black 1976) are highlighted along the way.

  

**Notation:** We let $S_t$ denote the spot price of an [[Risk Neutral Pricing of Options|underlying asset]] (stock, commodity, etc.) at time $t$. $P(t,T)$ denotes the price at time $t$ of a zero-coupon bond paying $1 at maturity $T$ (so $P(0,T)=e^{-rT}$ if $r$ is constant). We write $B(t)$ for the **money-market account** (bank account) accruing at the risk-free rate, so $B(t)=e^{rt}$ under continuous compounding. For stochastic interest rates, $P(t,T)=e^{-\int_t^T f(t,u),du}$ is determined by the yield curve or short-rate model (we assume deterministic $r$ for simplicity unless stated). Expectations $\mathbb{E}^Q[\cdot]$ are under the risk-neutral measure $Q$. For options, $(x)^+ = \max{x,0}$ indicates the positive part. We use $\Phi(\cdot)$ for the standard normal CDF, and will present formulas in **LaTeX** for precision. Each section ends with a summary of key results, and a final section provides further reading from classic references for deeper study.

  

**No-[[Arbitrage Pricing of Derivatives|Arbitrage]] and Risk-Neutral Foundations**

  

Before diving into specific instruments, we review the theoretical foundation that underpins all [[Arbitrage Pricing of Derivatives|pricing]] results: **no-[[Forward Contracts and Forward Prices|arbitrage arguments]]** and **[[Financial Mathematics Course|risk-neutral pricing]]**. In an [[Exercises|arbitrage-free market]], every derivative’s price can be derived by assuming the existence of a [[Verifying Martingale Property with Q|risk-neutral measure]] $Q$ under which all asset prices (when discounted) are martingales. Formally, if $V(t)$ is the price process of any tradable asset, then $$\frac{V(t)}{B(t)} \text{ is a martingale under } Q, ;\text{i.e.}; \mathbb{E}^Q!\left[\frac{V(T)}{B(T)} \Big| \mathcal{F}_t\right] = \frac{V(t)}{B(t)}$$ for all $T \ge t$. This implies $\mathbb{E}^Q[V(T)] = V(t)\frac{B(T)}{B(t)}$, meaning the expected growth of $V$ is the [[Black Scholes Derivation|risk-free rate]]. In particular, for any **[[Forward Contracts and Forward Prices|forward price]]** $F_t(T)$ (the price at time $t$ for future delivery at $T$), we must have $F_t(T) = \mathbb{E}^Q[S_T,|,\mathcal{F}_t]$ (because entering a forward requires no initial outlay, so its discounted value is a martingale). And since $\mathbb{E}^Q[S_T] = S_t e^{r(T-t)}$ under $Q$ when $r$ is constant, we get the classic [[PSET 1-Financial Instruments|forward pricing formula]] $F_t(T)=S_t e^{r(T-t)}$ . More generally, the _First [[Pricing Forwards, Futures, Bonds, Swaps, Swaptions, Caps and Floors under No-Arbitrage and Risk-Neutral Pricing|Fundamental Theorem]] of Asset Pricing_ guarantees that _no [[Arbitrage Pricing of Derivatives|arbitrage]] $\iff$ existence of a risk-neutral measure_ , so we can confidently use risk-neutral [[FORWARD RATES AND TERM STRUCTURE|expectations]] for [[Arbitrage Pricing of Derivatives|pricing]] as long as we rule out [[Arbitrage Pricing of Derivatives|arbitrage]].

  

**State Prices and DF:** Another useful viewpoint is via **state-price deflators** or **Arrow–Debreu prices**. Let $\pi(t,T)$ be the time-$t$ price of a security paying $1 if a specific state of the world at time $T$ occurs (and 0 otherwise). The collection of these prices (for all states) defines a **state-price density** (or stochastic discount factor) $\xi_T$ such that any payoff $X_T$ has price $V_0 = \mathbb{E}[\xi_T X_T]$. In a risk-neutral world, $\xi_T = e^{-rT} \frac{dQ}{dP}$, and $\mathbb{E}[\xi_T X_T]$ reduces to $e^{-rT}\mathbb{E}^Q[X_T]$. Thus [[Financial Mathematics Course|risk-neutral pricing]] is effectively a [[Change of Probability Measure|change of measure]] that embeds the [[Discount Factors|discount factor]]. All methods – [[Forward and Futures Contracts|replication]], state prices, [[Risk-Neutral Probabilities|risk-neutral expectation]] – yield the same [[Exercises|no-arbitrage price]] if applied correctly.

  

**[[Arbitrage Pricing of Derivatives|Pricing]] Algorithm ([[Teaching Note 7-Exotic Options And Derivative Pricing By Monte Carlo Simulation|Monte Carlo]]):** While analytical formulas will be derived for each instrument, it’s worth noting a general algorithm for [[Arbitrage Pricing of Derivatives|pricing]] via simulation, to illustrate risk-neutral valuation in practice:
```
**Algorithm: Monte Carlo Risk-Neutral Pricing**
1. Simulate $M$ independent sample paths for the underlying risk factors under the risk-neutral measure $Q$ (e.g. simulate $S_T$ such that its drift = $r$).
2. For each simulation $i$, compute the payoff $X_T^{(i)}$ of the derivative at maturity $T$.
3. Take the average payoff across simulations: $\overline{X}_T = \frac{1}{M}\sum_{i=1}^M X_T^{(i)}$.
4. Discount this average at the risk-free rate: $V_0 \approx e^{-rT}\,\overline{X}_T$.
```

As $M \to \infty$, $V_0$ converges to the true [[Exercises|no-arbitrage price]] $e^{-rT}\mathbb{E}^Q[X_T]$. This algorithm underscores that once we specify dynamics under $Q$, [[Arbitrage Pricing of Derivatives|pricing]] is “just” an expectation – albeit one often computed via elegant math rather than brute force.

  

With these foundations in mind, we now proceed to analyze and derive [[Arbitrage Pricing of Derivatives|pricing]] formulas for specific instruments, starting with forward and [[Mathematics of the Financial Markets|futures contracts]].

  

**Forward and [[Mathematics of the Financial Markets|Futures Contracts]]**

  

**Forward Contracts:** A **[[Forward Points in Currency|forward contract]]** is an agreement entered at time $t$ to buy or sell an [[Risk Neutral Pricing of Options|underlying asset]] for a fixed **[[Forward Contracts and Forward Prices|forward price]]** $F_t(T)$ at a specified future date $T$. For example, a gold forward might lock in the purchase of 1 oz. of gold at $F_0(T)$ dollars, with delivery in 3 months. Importantly, no money changes hands initially for a forward (ignoring any collateral), so the contract’s initial value is set to zero by no-[[Arbitrage Pricing of Derivatives|arbitrage]]. We consider a forward from the perspective of the **long** side (buyer at maturity) unless stated otherwise.

  

**[[Forward Contracts and Forward Prices|Forward Price]] Derivation:** To find the [[Arbitrage Pricing of Derivatives|arbitrage]]-free [[Forward Contracts and Forward Prices|forward price]] $F_0(T)$ at inception, we use a classic [[Arbitrage Pricing of Derivatives|arbitrage]] argument under the assumption of constant [[Black Scholes Derivation|risk-free rate]] $r$ and no carrying costs or income on the asset. Let $S_0$ be the current spot price of the underlying. Consider two strategies starting at time 0 and ending at time $T$:

• **Strategy A (Synthetic Forward):** Borrow $S_0$ dollars at the [[Black Scholes Derivation|risk-free rate]] $r$ (so owe $S_0 e^{rT}$ at $T$) and buy one unit of the asset now for $S_0$. This results in owning the asset at $T$ with a net outflow at maturity of $S_0 e^{rT}$.

• **Strategy B (Forward):** Enter a [[Forward Rates Agreement|long forward]] contract to buy one unit at time $T$ for the [[Forward Contracts and Forward Prices|forward price]] $F_0(T)$. No [[Preview of the Book|cash flow]] now, and pay $F_0(T)$ at $T$ to receive the asset.

  

At time $T$, both strategies yield the same asset. Strategy A’s net cost at $T$ is $S_0 e^{rT}$ (loan repayment), while Strategy B’s net cost is $F_0(T)$. For no [[Arbitrage Pricing of Derivatives|arbitrage]], these total costs must be equal – otherwise one could profit by choosing the cheaper strategy and [[Short Selling|shorting]] the more expensive one. Thus we require: $$F_0(T) = S_0 e^{rT},.$$ If $F_0(T)$ were higher, one could short the forward (lock in selling at $F_0$), and execute Strategy A (borrow and buy asset) to deliver into the forward, pocketing a riskless profit $F_0 - S_0 e^{rT}$ . If $F_0(T)$ were lower, one could do the opposite: short-sell the asset and invest the proceeds $S_0$ at $r$, and take a [[Forward Rates Agreement|long forward]] to buy back at $F_0(T)$, yielding [[Arbitrage Pricing of Derivatives|arbitrage]] profit $S_0 e^{rT} - F_0$ at $T$ . In summary, **the [[Forward Contracts and Forward Prices|forward price]] must equal the future value of the spot price** under no-[[Arbitrage Pricing of Derivatives|arbitrage]] (when the asset has no income or storage cost).

  

More generally, if the [[Risk Neutral Pricing of Options|underlying asset]] provides cash flows or has [[Primary vs. Secondary Commodities|storage costs]], the [[PSET 1-Financial Instruments|forward pricing formula]] adjusts for the **cost of carry**. For instance, if the asset pays a [[Hedging Strategies with Forwards|continuous dividend]] yield $q$ (or foreign interest rate in the case of a [[Forwards and Futures Notes|currency]]), then the [[Forward Contracts and Forward Prices|forward price]] is: $$F_0(T) = S_0 e^{(r - q)T},,$$ which subtracts the present value of dividends from the cost . If the asset yields a known cash income of present value $I$ over $[0,T]$, then $F_0(T) = (S_0 - I),e^{rT}$; whereas if there are known [[Primary vs. Secondary Commodities|storage costs]] with present value $U$, then $F_0(T) = (S_0 + U),e^{rT}$. All of these are derived by constructing [[Purpose and Structure of Financial Markets 1|arbitrage strategies]] that include the income or cost streams appropriately (treating dividends like a negative cost, and storage as a positive cost). As a special case, a **[[Forward Points in Currency|forward rate]] agreement (FRA)** – a [[Forward Points in Currency|forward contract]] on an interest rate – will have a [[Forward Points in Currency|forward rate]] determined by the difference between [[Swaps Types|borrowing and lending]] (we discuss FRAs implicitly when covering swaps, as a swap is essentially a string of FRAs).

  

**Forward Value During the Contract:** Once a forward is entered at the fair price $F_0(T)$, its **value** at inception is zero to both long and short. However, as the underlying price moves and time passes, the [[Forward Points in Currency|forward contract]] acquires a non-zero **mark-to-market value** (the amount one side would pay to exit the contract). Suppose at time $t$ (before maturity) the underlying spot is $S_t$ and the [[Forward Contracts and Forward Prices|forward price]] for maturity $T$ (for a new contract) is now $F_t(T)$. Consider a [[Forward Points in Currency|forward contract]] struck at the original price $K=F_0(T)$. The **[[Forward Points in Currency|forward contract]] value** to the long at time $t$ is the difference between locking in purchase at $K$ and the current fair price $F_t(T)$, appropriately discounted. Specifically, the [[Forward Rates Agreement|long forward]]’s time-$t$ value $V_t^{(forward)}$ is:
$$V_t = S_t - K e^{-r(T-t)},,$$

assuming [[Interest Rate Quotations|continuous compounding]]. This can be derived by recognizing that a forward can be replicated by holding the underlying ($+S_t$) and borrowing $K e^{-r(T-t)}$ (so that $K$ with interest will be paid at $T$) . The difference $S_t - K e^{-r(T-t)}$ is the net value. When $K = F_t(T)$ ([[Forward Contracts and Forward Prices|forward price]] is reset to fair), this value is zero (as expected). If $K$ is less than the current [[Chapter 3 - Forward and Futures Prices|fair forward price]], the [[Forward Rates Agreement|long forward]] is “in the money” (positive value), since they locked in a cheaper purchase than the market forward; if $K$ is above market $F_t$, the forward has negative value to the long.

  

**Example:** If you entered a 6-month forward to buy a stock at $K=100$ and after 3 months the [[Chapter 16 - Black–Scholes Model|stock price]] is $S_{3m}=105$ with 3-month remaining [[Forward Contracts and Forward Prices|forward price]] $F_{3m}(6m)=106$ (assuming some dividends or rates), then the value of your [[Forward Points in Currency|forward contract]] at 3 months is $105 - 100e^{-r(0.25)} \approx 105 - 100e^{-0.25r}$. If $r=0$, that’s simply $+5$ (you’d have a $5 gain, since you locked in at 100 while a new forward costs 105).

  

**[[Mathematics of the Financial Markets|Futures Contracts]]:** A **[[Futures Not Subject to Cash-And-Carry|futures]] contract** is similar to a forward in that it obligates the purchase or sale of an asset at a future date for a set price. However, [[Futures Not Subject to Cash-And-Carry|futures]] are exchange-traded, standardized, and **marked-to-market daily**. Mark-to-market means that gains and losses on a [[Futures Not Subject to Cash-And-Carry|futures]] position are settled in cash each day, and the [[Futures Price and the Quality Option Before E|futures price]] is reset to a new level until delivery. Despite these differences, if [[Interest Rate Quotations|interest rates]] are constant and there are no other frictions, the **[[Forward Contracts and Forward Prices|forward price]] equals the [[Futures Price and the Quality Option Before E|futures price]]** for the same maturity . Intuitively, with deterministic $r$, the interim cash flows from marking-to-market can be reinvested at the [[Black Scholes Derivation|risk-free rate]], leaving no difference in present value.

  

When [[Interest Rate Quotations|interest rates]] are **stochastic**, forward and [[Futures Not Subject to Cash-And-Carry|futures]] prices can diverge slightly. The [[Pricing and Hedging Implications of Daily Sett|daily settlement]] feature of [[Futures Not Subject to Cash-And-Carry|futures]] means that if [[A Preview of Alternative Formulations|asset price]] movements are positively correlated with [[How Countries Go Broke-Chapter 12 to Chapter 14|interest rate changes]], a long [[Futures Not Subject to Cash-And-Carry|futures]] tends to earn gains when rates are high (which can be reinvested at a high rate) and losses when rates are low, making the [[Futures Not Subject to Cash-And-Carry|futures]] more attractive than a forward. Conversely, negative correlation makes [[Forwards and Futures|forwards]] slightly more valuable. In fact, **if $\text{Corr}(S_t, r_t) > 0$ then [[Futures Price and the Quality Option Before E|futures price]] $>$ [[Forward Contracts and Forward Prices|forward price]]; if $\text{Corr} < 0$ then [[Futures Not Subject to Cash-And-Carry|futures]] $<$ forward** . These differences are second-order in many cases, and practitioners often assume forward $\approx$ [[Futures Price and the Quality Option Before E|futures price]] unless dealing with long-dated contracts or significant rate volatility. We will generally not distinguish between forward and [[Futures Not Subject to Cash-And-Carry|futures]] prices in the formulas below (taking that assumption, or using $F$ for both), unless noted.

  

**[[Arbitrage Pricing of Derivatives|Pricing]] via [[Risk-Neutral Probabilities|Risk-Neutral Expectation]]:** The [[Chapter 3 - Forward and Futures Prices|forward pricing]] result can be alternatively obtained by risk-neutral valuation. Under the [[Verifying Martingale Property with Q|risk-neutral measure]] $Q$, the **expected spot price** at time $T$ grows at rate $r$: $\mathbb{E}^Q[S_T]=S_0 e^{rT}$. Because a [[Forward Points in Currency|forward contract]] has zero initial cost, its [[Forward Contracts and Forward Prices|forward price]] must satisfy $F_0(T) = \mathbb{E}^Q[S_T]$ (otherwise an [[Arbitrage Pricing of Derivatives|arbitrage]] via long/[[Forward Rates Agreement|short forward]] vs. underlying would exist). Thus $F_0(T)=S_0 e^{rT}$, consistent with our [[Arbitrage Pricing of Derivatives|arbitrage]] derivation. In fact, we can express the _time-$t$ forward price_ as $$F_t(T) = \frac{\mathbb{E}^Q[S_T,|,\mathcal{F}_t]}{\mathbb{E}^Q[B(T)/B(t),|,\mathcal{F}_t]} = \frac{\mathbb{E}^Q[S_T,|,\mathcal{F}_t]}{e^{r(T-t)}},$$ which again yields $S_t e^{r(T-t)}$ in the simple case. For [[Futures Not Subject to Cash-And-Carry|futures]], because of [[Pricing and Hedging Implications of Daily Sett|daily settlement]], one shows $\displaystyle F^{\text{fut}}_t(T) = \mathbb{E}^Q[S_T,|,\mathcal{F}_t]$ (the expectation under $Q$ without discounting, since each day’s gains are realized immediately). If $r$ is constant, this equals the [[Forward Contracts and Forward Prices|forward price]] after accounting for discounting day by day, but if $r$ is random, $\mathbb{E}^Q[S_T] e^{-r(T-t)} \neq \mathbb{E}^Q[S_T]$ in general, hence forward $\neq$ [[Futures Not Subject to Cash-And-Carry|futures]] in that scenario.

  

**Summary ([[Forwards and Futures|Forwards]]/[[Futures Not Subject to Cash-And-Carry|Futures]]):** A [[Forward Points in Currency|forward contract]]’s no-[[Arbitrage Pricing of Derivatives|arbitrage]] delivery **price** at inception is $F_t(T)=S_t e^{(r+c-q)(T-t)}$ (where $c$ is storage cost and $q$ yield). The **value** of an existing forward ([[Chapter 4 - Futures: Hedging and Speculation|long position]]) is $V_t = S_t e^{-q(T-t)} - K e^{-r(T-t)}$, which at $t=0$ reduces to $0$ when $K=F_0(T)$. [[Futures Not Subject to Cash-And-Carry|Futures]] prices are generally equal to forward prices under the simple assumptions of constant [[Interest Rate Quotations|interest rates]] and no correlations. Both [[Part I-Basis Trading|forward and futures pricing]] illustrate that the expectation under the [[Verifying Martingale Property with Q|risk-neutral measure]] – adjusted for any cost-of-carry – determines the fair price. These instruments have linear payoffs and thus are easier to price; we now move to [[Valuing Callable Bonds Using QuantLib Python|fixed income instruments]] where [[Interest Rate Quotations|interest rates]] play a central role.

  

**Zero-Coupon Bonds and the [[The Vasicek Model|Term Structure]]**

  

A **zero-coupon bond** (or **discount bond**) maturing at date $T$ is the simplest fixed-income instrument: it pays a single unit of [[Forwards and Futures Notes|currency]] (e.g. $1) at $T$ and nothing before. Let $P(t,T)$ denote the time-$t$ price of this bond. By definition, $P(T,T)=1$ (at maturity it’s worth its face value). Absent default risk, a bond is essentially a risk-free asset if held to maturity. However, when interest rates are not constant, $P(t,T)$ will fluctuate as rates move – it’s a traded asset whose price reveals the **term structure of interest rates**. The _continuously-compounded yield_ $y(t,T)$ for maturity $T$ is defined via $P(t,T)=e^{-y(t,T),(T-t)}$. In particular, $y(0,T)$ is the **zero-coupon yield** for maturity $T$. The function $T \mapsto y(0,T)$ is the initial yield curve.

  

**No-[[Arbitrage Pricing of Derivatives|Arbitrage]] for Bonds:** Bonds with different maturities are linked by no-[[Arbitrage Pricing of Derivatives|arbitrage]]: there should be no way to use short-term bonds to [[Arbitrage Pricing of Derivatives|arbitrage]] long-term bonds and vice versa. In practice, an entire yield curve is fitted to market prices of bonds, Treasury bills, swaps, etc., to ensure consistency. A common procedure is **bootstrapping**: starting from the shortest maturities (where yields are directly observed) and solving for longer-term discount factors that match observed coupon bond prices. A **coupon bond** paying semiannual coupons, for example, can be seen as a [[An Asset Allocation Primer|portfolio]] of zero-coupon bonds (each coupon and principal is a [[Preview of the Book|cash flow]] at a known date). No-[[Arbitrage Pricing of Derivatives|arbitrage]] demands that the bond’s price equals the sum of the present values of each [[Preview of the Book|cash flow]] using the appropriate zero-coupon rates for each period. If not, an arbitrageur could strip the bond into zeros or reconstitute it to exploit mispricings. Thus, _coupon bond [[Arbitrage Pricing of Derivatives|pricing]] requires a consistent set of discount factors $P(0,T_i)$ for all [[Preview of the Book|cash flow]] dates ${T_i}$_.

  

In a deterministic interest rate environment, $P(0,T)=e^{-rT}$ (with $r$ constant) or more generally $P(0,T)=e^{-\int_0^T r(u),du}$ for a time-varying rate $r(u)$. Under [[Appendix 5.C Forward And Futures Prices When Interest Rates Are Random|stochastic interest rates]], the price is given by a [[Risk-Neutral Probabilities|risk-neutral expectation]]:
$$P(t,T) = \mathbb{E}^Q!\bigg[\exp!\Big(-\int_t^T r(s)ds\Big)\Big|,\mathcal{F}_t\bigg],,$$

which is the discounted expected value of $1. This formula comes from considering a money-market account as numeraire (the _Girsanov theorem_ can be applied to show bond prices are martingales under the appropriate measure). In practice, specific **short-rate models** (Vasicek, Cox–Ingersoll–Ross, etc.) or **forward rate models** (HJM) are used to model $P(t,T)$. But without delving into those, we will assume we know the term structure $P(0,T)$, or equivalently zero rates, as inputs.

  

**Forward Rates:** A useful derived quantity is the **[[Forward Rate|forward interest rate]]** for borrowing between $T_1$ and $T_2$ as seen today. Denoted $f(0;T_1,T_2)$, it is defined via the relation
$$P(0,T_1) = P(0,T_2),\exp!\big(-f(0;T_1,T_2),(T_2-T_1)\big),,$$

so that $f(0;T_1,T_2)$ is the rate that makes an [[An Asset Allocation Primer|investment]] from $0$ to $T_2$ equivalent to investing until $T_1$ then rolling into a loan from $T_1$ to $T_2$. Solving, $f(0;T_1,T_2) = \frac{\ln P(0,T_1) - \ln P(0,T_2)}{T_2 - T_1}$. If [[Interest Rate Quotations|interest rates]] are continuous, this is also related to the instantaneous **[[Forward Points in Currency|forward rate]]** $f(0,T)$ via $P(0,T)=\exp(-\int_0^T f(0,u),du)$. In a no-[[Arbitrage Pricing of Derivatives|arbitrage]] setting, forward rates extracted from bond prices are consistent with forward contracts on [[Interest Rate Quotations|interest rates]] (FRAs). Indeed, the [[Exercises|no-arbitrage price]] of a **[[Forward Points in Currency|forward rate]] agreement** that fixes the rate for $[T_1,T_2]$ at $K$ can be found by considering lending/borrowing strategies in bonds: one can show the present value of the payoff is $(f(0;T_1,T_2)-K),(T_2-T_1)P(0,T_2)$ (which is analogous to the [[Forward Points in Currency|forward contract]] value formula $S - K e^{-rT}$, with $S$ replaced by [[Forward Points in Currency|forward rate]] and discount by $P$). We won’t derive FRA [[Arbitrage Pricing of Derivatives|pricing]] in detail, as it will be subsumed by the discussion of swaps.

  

**[[Financial Mathematics Course|Risk-Neutral Pricing]] for Bonds:** By treating the bond as the asset and the [[Appendix 5.C Forward And Futures Prices When Interest Rates Are Random|money-market account]] as numeraire, one can derive that _each $P(t,T)$ must equal the [[Risk-Neutral Probabilities|risk-neutral expectation]] of its payoff 1, discounted by $B(T)/B(t)$._ This yields the earlier expectation formula. It also implies that [[Quantitative Trading Strategies Lecture Notes|trading strategies]] involving bonds must satisfy no-[[Arbitrage Pricing of Derivatives|arbitrage]]; for instance, a **rolling over strategy** of short-term bonds cannot outgun a long-term bond if the forward rates are set properly.

  

**Summary (Bonds):** Zero-coupon bond prices $P(0,T)$ encode the discount factors for [[Advanced Derivatives Pricing Methodology|future cash flows]] and determine the [[6. A Brief Introduction to Stochastic Calculus|term structure of interest rates]]. [[Arbitrage Pricing of Derivatives|Arbitrage]] considerations enforce that coupon bond prices equal the sum of zero-coupon bond equivalents. Forward [[Interest Rate Quotations|interest rates]] are derived from zero prices and coincide with FRA rates under no-[[Arbitrage Pricing of Derivatives|arbitrage]]. We now use these concepts as building blocks for [[Arbitrage Pricing of Derivatives|pricing]] **interest rate swaps**, which are essentially exchanges of fixed and floating [[1. DeterministicCashFlows|cash flow streams]] and heavily depend on the [[The Vasicek Model|term structure]].

  

**Interest Rate Swaps**

  

An **[[Primer on Interest Rate Swaps|interest rate swap]]** is a derivative in which two parties [[Fundamentals of Swaps|exchange cash flows]] of two different types of interest payments on a [[Fundamentals of Swaps|notional principal]] amount. The most common type is a **plain vanilla [[Primer on Interest Rate Swaps|interest rate swap]]**: one party pays a [[Chapter 36 - Currency Swaps|fixed interest rate]] $R_{\text{fixed}}$ on the notional and receives a floating rate (such as LIBOR or SOFR) from the other party (who does the opposite). These payments occur periodically (e.g. semiannually) over a term of the swap. No principal is exchanged in a vanilla swap; only the net interest difference is paid each period. Swaps allow conversion between fixed-rate and floating-rate exposures and are fundamental in [[Analysis of Fixed Income Securities|interest rate risk]] management.

  

**Swap as Exchange of Bonds:** A useful way to conceptualize a [[Swaptions|fixed-for-floating swap]] is as the difference between two bond positions. Consider a **payer swap** (the party who pays fixed and receives floating): this position can be replicated by (i) **short** a fixed-rate bond (paying coupons $R_{\text{fixed}}$ and principal) and (ii) **long** a floating-rate note of the same notional and maturity. A floating-rate note (FRN) typically pays the benchmark rate (e.g. LIBOR) each period and is reset such that it always trades at par at coupon dates (assuming no [[Quantitative Trading Strategies Lecture Notes|credit risk]]). Thus, at coupon reset dates, the FRN’s value [[Assets|returns]] to the notional. If we assume the [[Pricing Interest Rate Swaps|floating leg]] is tied to a risk-free benchmark, the present value of receiving floating over each period plus getting back notional at end is just the notional amount (because one could just hold that cash risk-free). In fact, at swap initiation (time 0), the **present value of the [[Pricing Interest Rate Swaps|floating leg]]** (for the full swap term) equals the [[Fundamentals of Swaps|notional principal]] _by construction_ when using the current forward rates. Meanwhile, the present value of the [[Pricing Interest Rate Swaps|fixed leg]] is the present value of a fixed coupon bond paying $R_{\text{fixed}}$ per period plus principal. For the swap to have zero initial value (a **[[Determining the Expression for the Fair Value of the Swap Spread|par swap]]**), these two present values must be equal. Therefore, the fixed rate $R_{\text{fixed}}$ is chosen such that the _fixed leg PV = notional_ (since the [[Pricing Interest Rate Swaps|floating leg]] PV is notional). This unique rate is called the **swap [[Pricing Interest Rate Swaps|par rate]]** $S(0,T)$ for the swap’s maturity $T$.

  

**[[Citi-Guide to Swaps|Swap Pricing]] (at Initiation):** Suppose the swap pays fixed $R$ at times $T_1, T_2, \dots, T_N = T$ (with $T_0=0$) and floating payments of the prevailing [[Forward Points in Currency|forward rate]] for each period (so effectively the [[Pricing Interest Rate Swaps|floating leg]] will realize forward rates in expectation). Let $\Delta_i = T_i - T_{i-1}$ be year-fractions for each period. The present value of the [[Pricing Interest Rate Swaps|fixed leg]] (per notional $1) is:
$$PV_{\text{fixed}} = R \sum_{i=1}^N \Delta_i,P(0,T_i) + P(0,T_N),,$$

which is the [[Realized Returns|coupon payments]] plus the notional returned at $T_N$. (We include $P(0,T_N)$ as the PV of receiving $1 at maturity, if the swap is structured to exchange notional at the end – in a plain vanilla interest swap typically notional is not exchanged, but conceptually the floating leg’s final interest plus return to par can be viewed as receiving notional; equivalently, one of the $P(0,T_i)$ terms could be interpreted as including the principal.) The present value of the [[Pricing Interest Rate Swaps|floating leg]] is:
$$PV_{\text{float}} = P(0,T_0) - P(0,T_N) + \sum_{i=1}^N P(0,T_i) - P(0,T_{i}),,$$

which telescopes to $P(0,T_0) - P(0,T_N) = 1 - P(0,T_N)$ (since $P(0,T_0)=1$). In other words, $PV_{\text{float}} = 1 - P(0,T_N)$ for $1 notional (this result holds if the first floating payment is known or negligible; a more precise approach shows it equals the difference between par at start and discount factor to end, effectively the same). Setting $PV_{\text{fixed}} = PV_{\text{float}}$ for a par swap, we solve for $R$:
$$R,\sum_{i=1}^N \Delta_i P(0,T_i) + P(0,T_N) = 1 \implies R,\sum_{i=1}^N \Delta_i P(0,T_i) = 1 - P(0,T_N),. $$

Thus the **[[Determining the Expression for the Fair Value of the Swap Spread|par swap]] fixed rate** is
$$R^* = \frac{1 - P(0,T_N)}{\sum_{i=1}^N \Delta_i,P(0,T_i)},.$$

This $R$ is the_ **_swap rate_** _that makes the swap’s initial value zero_ _. Each $P(0,T_i)$ is readily obtained from the zero curve. For example, if $T_N=5$ years with semiannual payments, $R$ is such that the PV of five years of semiannual $R_{2}$ payments plus $P(0,5)$ equals 1. If yield curve is flat at, say, 3% continuously, then ${} R \approx 3\%$ as expected. If the yield curve is upward sloping, $R^*$ will be higher than the [[An Overview of the Vasicek Short Rate Model|short rate]] but lower than long-term rates, roughly an average.



**Swap Valuation (After Initiation):** Once a swap is in place, its value may become positive or negative to a party as rates change. The **value of a swap** at time $t$ (to the fixed-rate payer) can be computed as the difference between the present value of remaining floating payments and remaining fixed payments. Let $R_{\text{fixed}}$ be the original fixed rate on the swap, and let $R_{\text{new}}(t)$ be the current [[Determining the Expression for the Fair Value of the Swap Spread|par swap]] rate for the remaining term (i.e. the [[Teaching Note 4 Interest Rate Derivatives|swap rate]] one would get on a new swap from $t$ to $T_N$). Then the **swap value** to the fixed payer (who pays $R_{\text{fixed}}$) at $t$ (per $1 notional) is:
$$V_t^{\text{payer}} = (R_{\text{new}}(t) - R_{\text{fixed}}),\sum_{i=k+1}^N \Delta_i P(t,T_i),,$$

where $T_k$ is the last payment date passed (so payments $k+1$ to $N$ remain) . Here $\sum_{i=k+1}^N \Delta_i P(t,T_i)$ is the **annuity factor** (present value of \$1 paid each period over remaining dates). If the payer locked in a higher rate than current ($R_{\text{fixed}} > R_{\text{new}}$), then this value is negative (the fixed payer is paying above-market, a disadvantage). If rates have risen ($R_{\text{fixed}} < R_{\text{new}}$), the payer swap gains value (positive $V_t$). Equivalently, one can compute the value for the fixed-rate **receiver** as $V_t^{\text{receiver}} = (R_{\text{fixed}} - R_{\text{new}}(t)) \sum \Delta_i P(t,T_i)$ – the opposite sign. This formula comes directly from considering a portfolio of bonds: after initiation, the fixed leg is like a bond with coupon $R_{\text{fixed}}$, and the floating leg is like a FRN that is worth par. So the swap’s value is like long a bond with coupon $R_{\text{new}}$ and short a bond with coupon $R_{\text{fixed}}$, scaled by notional. This results in $(R_{\text{new}} - R_{\text{fixed}})$ times the bond’s **duration-weighted PV**, which is exactly the annuity factor $\sum \Delta_i P(t,T_i)$ .

  

Another way: one can imagine terminating (or initiating an offsetting swap) at time $t$. To do so, one would pay/receive the net present value difference. Thus $V_t$ can be found by computing $PV_{\text{fixed,old}}(t) - PV_{\text{fixed,new}}(t)$ (for the same [[Pricing Interest Rate Swaps|floating leg]]), which yields the above result since $PV_{\text{fixed,new}}(t)$ would equal the [[Pricing Interest Rate Swaps|floating leg]]’s PV.

  

**Example:** Suppose two years ago you entered a 7-year swap to pay fixed 3% and receive 6-month LIBOR, on $100 million. Now 2 years have passed (5 years remaining). Using today’s discount factors, you find the annuity $\sum_{i=1}^{10} \Delta_i P(0,T_i) = 4.8161$ (for 10 semiannual periods left) . Also, the current 5-year swap rate is calculated as ${} R_{\text{new}} = (1 - P(0,5))/4.8161 = 1.59\%$ . Your swap’s value as fixed payer is $(0.0159 - 0.03) \times 4.8161 \times \$100\text{M} = -  6.79\text{M}$ . It’s negative because you are paying 3% which is high relative to the new 1.59% market rate – you’d have to pay $6.79MM to transfer your swap to someone else (i.e. to receive fixed at 3% when market is 1.59%, the counterparty would demand compensation). Conversely, the fixed-rate receiver has a +$6.79MM position.

  

**Risk-Neutral View:** Under a [[Pricing Forwards, Futures, Bonds, Swaps, Swaptions, Caps and Floors under No-Arbitrage and Risk-Neutral Pricing|no-arbitrage pricing]] measure, each forward LIBOR rate (the underlying for each floating payment) has an expectation equal to its forward value. A [[Determining the Expression for the Fair Value of the Swap Spread|par swap]] initially has zero value because the [[Pricing Interest Rate Swaps|fixed leg]]’s promised payments are set exactly equal to the sequence of implied forward floating payments. As time evolves, the realization of [[Interest Rate Quotations|interest rates]] will make the [[Pricing Interest Rate Swaps|fixed leg]] too high or too low relative to forward rates, creating value. One could price a swap by modeling the joint evolution of the [[An Overview of the Vasicek Short Rate Model|short rate]] or forward rates and taking [[FORWARD RATES AND TERM STRUCTURE|expectations]] of the net present value of payments, but the linearity of swap payoffs allows the simpler “deterministic PV” approach above. Indeed, a vanilla swap has _no optionality_, so its price is just the difference of two bond portfolios, and one can compute it by deterministic cashflow discounting with the current zero curve (no need for complex optionality modeling). This is why swaps are often used to infer the _risk-free zero curve itself_ from swap rates in the market.

  

**Summary (Swaps):** The [[Pricing Interest Rate Swaps|fixed leg]] of a swap is priced as an annuity whose rate is set such that its initial PV equals the notional (the [[Pricing Interest Rate Swaps|floating leg]]’s PV). The swap [[Pricing Interest Rate Swaps|par rate]] $S(0,T)$ is given by the ratio of “1 minus last [[Discount Factors|discount factor]]” to “sum of discount factors” . The mark-to-market value of a swap during its life is proportional to the difference between the original fixed rate and current [[Pricing Interest Rate Swaps|par rate]], times the remaining annuity factor . Swaps are thus very convenient to price given a yield curve, and they facilitate the market’s bootstrapping of that curve. Next, we turn to **swaptions** – options on swaps – which introduce optionality and require a further step of risk-neutral valuation (often using the [[Black Models for Bond Price Options Capsfloors|Black model]]).

  

**Swaptions (Swap Options)**

  

A **swaption** is an option granting the right, but not the obligation, to enter an [[Primer on Interest Rate Swaps|interest rate swap]] at a specified future date. There are two types: a **[[Chapter 39 - Swaptions, Forward Swaps, and MBS|payer swaption]]** gives the right to _pay fixed, receive floating_ (i.e. become the fixed-rate payer in a swap), while a **receiver swaption** gives the right to _receive fixed, pay floating_. For example, a 5Y5Y [[Chapter 39 - Swaptions, Forward Swaps, and MBS|payer swaption]] is an option (exercisable in 5 years) to enter a 5-year swap as fixed payer. Swaptions are widely used to hedge or speculate on [[Forward Rate|future interest rate]] moves and to add optionality to swap-based products.

  

**Swaption Payoff:** Consider a [[Chapter 39 - Swaptions, Forward Swaps, and MBS|payer swaption]] expiring at time $T$ on a swap that would run from $T$ to $T_N$ (with coupon dates $T_{j}$, $j=1\dots N$, $T_0=T$). Let $K$ be the agreed fixed rate (swaption strike). At exercise (time $T$), if the swaption holder chooses to exercise and enter the swap as fixed payer, they will pay fixed $K$ and receive floating. The _market swap rate_ $S(T)$ for that $T$–$T_N$ swap ([[Pricing Interest Rate Swaps|par rate]] at $T$ for maturity $T_N$) will determine whether exercise is favorable. The **intrinsic value** of a [[Chapter 39 - Swaptions, Forward Swaps, and MBS|payer swaption]] at expiry is the present value of the difference between the swap at the market rate $S(T)$ and the swap at the strike $K$, floored at zero (since one wouldn’t exercise if it’s negative). In other words, the payoff is the **swap’s value to the payer** at $T$, clipped at zero:
$$\Pi_{payer}(T) = \Big( S(T) - K \Big)^+ \sum_{i=1}^N \Delta_i P(T, T_i),,$$

times the notional. Here $\sum_{i=1}^N \Delta_i P(T,T_i)$ is the **annuity factor at $T$** (present value at $T$ of $1 per period over the swap, essentially $= \sum_{i=1}^N \Delta_i e^{-r(T_i-T)}$ under deterministic rates). This factor converts a rate difference into a monetary value. If $S(T) > K$, the payer swaption is in the money (payer can enter a swap paying $K$ when market demands a higher rate $S(T)$, a favorable deal), and the payoff equals the PV of receiving $(S(T)-K)$ over each period. If $S(T)\le K$, payoff is zero (better not to enter the swap). A **receiver swaption** similarly has payoff $\Big(K - S(T)\Big)^+ \sum_{i=1}^N \Delta_i P(T,T_i)$ (nonzero when $K >$ current [[Teaching Note 4 Interest Rate Derivatives|swap rate]], since receiver would then get above-market fixed rate).

  

**[[Arbitrage Pricing of Derivatives|Pricing]] Swaptions:** Swaptions are more complex to price because the payoff depends on the entire set of [[Interest Rate Quotations|interest rates]] at $T$ (through $S(T)$ or the collection of bond prices $P(T,T_i)$). A full treatment requires an [[An Overview of the Vasicek Short Rate Model|interest rate model]] (e.g. Black’s model, [[Continuous-Time Stochastic Processes|Bachelier model]], or a short-rate/forward-rate model like Hull–White, LIBOR market model, etc.). However, a common market approach is to use an analog of the Black–Scholes formula known as **Black’s 1976 model** for swaptions . Black’s model assumes the **[[Chapter 39 - Swaptions, Forward Swaps, and MBS|forward swap]] rate** $S(t)$ for the underlying swap follows a lognormal process under its appropriate forward measure (with a certain volatility $\sigma$). Under these assumptions, the swaption price can be expressed in closed form, similar to a call option on a forward asset.

  

In Black’s formula for a **[[Chapter 39 - Swaptions, Forward Swaps, and MBS|payer swaption]]**, the price at time 0 is given by:
$$V_0^{\text{payer swaption}} = A(0),\Big[,F_S \Phi(d_1);-;K,\Phi(d_2)\Big],,$$

where:

• $F_S$ is the **[[Chapter 39 - Swaptions, Forward Swaps, and MBS|forward swap]] rate** (today’s [[Pricing Interest Rate Swaps|par rate]] for the swap starting at $T$), essentially $R^*$ for that swap starting in future;

• $A(0) = \sum_{i=1}^N \Delta_i P(0,T_i)$ is the **annuity factor** (present value of $1 per swap period, from 0);

• $\Phi$ is the standard normal CDF;

• $d_{1,2} = \frac{\ln(F_S/K) \pm \frac{1}{2}\sigma^2 T}{\sigma\sqrt{T}},$;

• $\sigma$ is the implied **[[Swaption Skew|swaption volatility]]** (assumed constant);

• $T$ is the swaption expiration.

  

This formula is directly analogous to Black–Scholes: $A(0)$ plays the role of a [[Discount Factors|discount factor]] and size scaling, $F_S$ is like a [[Forward Contracts and Forward Prices|forward price]], and $K$ the strike. In fact, it can be derived by noting the swaption payoff is $A(T)(S(T)-K)^+$ for payer, and treating $A(T)$ as approximately constant (or using the annuity as numeraire, which leads to $S(t)$ being martingale under the _swap measure_). Black’s 1976 paper originally presented the formula for options on [[Futures Not Subject to Cash-And-Carry|futures]] , but it’s applied to swaptions by analogous reasoning. If we account for discrete compounding conventions, a more precise formula is:
$$V_0^{\text{payer}} = \frac{1 - (1+F_S/m)^{-mN}}{F_S};e^{-rT}\big[F_S\Phi(d_1) - K\Phi(d_2)\big],,$$

where $m$ is payments per year (this factor $\frac{1-(1+F_S/m)^{-mN}}{F_S}$ is essentially $A(0)$ in another guise) . The receiver swaption price by [[7. Black Scholes Model|put-call parity]] is
$$V_0^{\text{receiver}} = A(0),\big[K\Phi(-d_2) - F_S \Phi(-d_1)\big],,$$

or simply the payer formula with $K$ and $F_S$ swapped in sign inside the $\Phi$ arguments.

  

**Modeling Considerations:** The [[Financial Mathematics Course|risk-neutral pricing]] of swaptions can also be done using _Jamshidian’s trick_ in one-factor models (decomposing a swaption into a [[An Asset Allocation Primer|portfolio]] of bond options), or [[Teaching Note 7-Exotic Options And Derivative Pricing By Monte Carlo Simulation|Monte Carlo]] under a LIBOR market model where each LIBOR [[Forward Points in Currency|forward rate]] is lognormal (the industry standard for consistent caplet and swaption volatilities). The Black swaption formula is widely used to quote swaption implied volatilities. It assumes lognormal [[Teaching Note 4 Interest Rate Derivatives|swap rate]] distribution; in low-rate or negative-rate environments, sometimes a normal assumption ([[Continuous-Time Stochastic Processes|Bachelier model]]) is used instead.

  

**Cap/Floor Parity with Swaptions:** Interestingly, there is a connection between swaptions and [[Chapter 38 - T-Bond Option, Caps, Floors and Collar|interest rate caps]]/[[Caps and Floors|floors]] (described next) via parity relationships. A [[Chapter 39 - Swaptions, Forward Swaps, and MBS|payer swaption]] (right to pay fixed) can be shown to be equivalent to a [[An Asset Allocation Primer|portfolio]] of caplets (a cap) with the same strike, and a receiver swaption equals a [[An Asset Allocation Primer|portfolio]] of floorlets (a floor), under certain assumptions. Alternatively, one can say: **Cap – Floor = Swap**, which implies by [[Arbitrage Pricing of Derivatives|arbitrage]] that **Cap price – Floor price = PV of fixed-floating difference** . Indeed, if you hold a cap and short a floor (same strike $K$), you will receive payments whenever LIBOR $- K$ is positive (from the cap) and pay when $K - \text{LIBOR}$ is positive (due to the short floor), which net replicates paying floating vs $K$. This is exactly a swap with fixed $K$. Thus, **Cap(K) – Floor(K) = PV(\text{receive floating – pay fixed $K$})**, which is the [[Determining the Expression for the Fair Value of the Swap Spread|par swap]] value if $K$ equals the [[Pricing Interest Rate Swaps|par rate]] (zero at inception) . If $K$ differs from par, the difference in cap and floor prices equals the market value of a payer swap with rate $K$. These relationships ensure consistency across the [[Arbitrage Pricing of Derivatives|pricing]] of caps, [[Caps and Floors|floors]], and swaptions.

  

**Summary (Swaptions):** Swaptions add optionality to swaps, with payoffs contingent on future swap rates. They are commonly priced via the **Black-76 model**, treating the swap’s fixed rate as the underlying instrument . The [[Chapter 39 - Swaptions, Forward Swaps, and MBS|payer swaption]] formula resembles a call option on the [[Chapter 39 - Swaptions, Forward Swaps, and MBS|forward swap]] rate, scaled by the annuity factor. While we provided Black’s formula (ubiquitous in practice), rigorous [[Arbitrage Pricing of Derivatives|pricing]] can be done with [[Financial Mathematics Course|term structure models]] under the [[Verifying Martingale Property with Q|risk-neutral measure]]. Swaption contracts allow [[Key Rates O1s Durations and Hedging|hedging]] of [[Fixed Income Versus Equity Derivatives|interest rate volatility]] and are closely related to [[Interest Rate Derivatives-An Introduction to the  Pricing of Caps and Floors|caps and floors]], which we discuss next.

  

**[[Interest Rate Derivatives-An Introduction to the  Pricing of Caps and Floors|Caps and Floors]] (Interest Rate Options)**

  

An **interest rate cap** is essentially a [[An Asset Allocation Primer|portfolio]] of call options on a [[The Gauss Model|short-term interest rate]], often designed to limit a borrower’s floating interest payments. Conversely, an **interest rate floor** is a [[An Asset Allocation Primer|portfolio]] of put options on a rate, limiting a lender’s minimum received rate. [[Interest Rate Derivatives-An Introduction to the  Pricing of Caps and Floors|Caps and floors]] are quoted in terms of their strike rate $K$ (the cap rate or floor rate) and typically reference a LIBOR-like index over a schedule of reset dates.

  

**Cap Definition:** A cap provides payoff in each period the reference interest rate exceeds $K$. For example, consider a cap on 3-month LIBOR with quarterly reset dates $T_1, T_2, \dots, T_N$. At each reset $T_i$ (when the new LIBOR $L_{i-1}(=L(T_{i-1},T_i))$ for $[T_{i-1},T_i]$ is determined), the cap will, at the next payment date $T_i$, pay the excess interest: $(L_{i-1} - K)^+ \Delta_i \cdot \text{Notional}$, where $\Delta_i$ is the [[Intra-Year Compounding and Day-Count|day-count]] fraction for that period . In other words, if LIBOR ends up higher than $K$, the caplet pays the difference * times the period length and notional (the additional interest cost). If LIBOR $\le K$, the caplet pays zero (the borrower’s rate is at or below the cap). The collection of these call-option-like payoffs for $i=1$ to $N$ constitutes the cap. Each individual option is called a **caplet**.

  

**Floor Definition:** Similarly, a floor pays $(K - L_{i-1})^+ \Delta_i$ on each period $i$ – paying out when LIBOR falls below $K$, thus guaranteeing a minimum rate $K$ to the investor. Each piece is a **floorlet** (put option on the rate).

  

**Caplet [[Arbitrage Pricing of Derivatives|Pricing]]:** Each caplet is effectively a European call option on the interest rate $L_{i-1}$ set at time $T_{i-1}$ for payment at $T_i$. To price a caplet, one usually uses a **forward measure**: for caplet on $L(T_{i-1},T_i)$, it is convenient to use the $T_i$-forward measure (with numeraire $P(t,T_i)$). Under this measure, the forward LIBOR for that period, $F_{i-1}(t) \approx L(t;T_{i-1},T_i)$, behaves like a martingale. Black’s model assumes $L_{i-1}$ (or equivalently $F_{i-1}$) is lognormal under this forward measure with volatility $\sigma_i$. Then the **Black formula for a caplet** (at time 0) is:
$$V_0^{\text{caplet}} = P(0,T_i),\Delta_i,\big[,F_{i-1}(0)\Phi(d_1) - K\Phi(d_2),\big],,$$

where $F_{i-1}(0)$ is the current [[Forward Points in Currency|forward rate]] for $[T_{i-1},T_i]$, and
$d_{1,2} = \frac{\ln(F_{i-1}(0)/K) \pm \frac{1}{2}\sigma_i^2 T_{i-1}}{\sigma_i \sqrt{T_{i-1}}},$ (assuming caplet decision is effectively at $T_{i-1}$). We also multiplied by $\Delta_i$ because the payoff is $(L-K)\Delta_i$ . This formula is directly analogous to an option on a [[Forward Points in Currency|forward rate]] agreement. The factor $P(0,T_i)$ is the discount to the payment date. In practice, market quotes cap implied volatilities for different maturities and strikes, and uses Black’s formula to price each caplet accordingly (with interpolation for intermediate).

  

A key point: Because each caplet payoff occurs at $T_i$ but is determined by $L$ fixed at $T_{i-1}$, using $T_i$ as numeraire simplifies the payoff to something like $\frac{1}{1+L\Delta}$ times a simple difference . The standard Black formula accounts for the required [[Chapter 10 - Bonds: Duration and Convexity|convexity adjustment]] via the $\Delta_i$ factor and discounting.

  

**Cap = Sum of Caplets:** The total cap price is the sum of the present values of all its caplets:
$$V_0^{\text{cap}} = \sum_{i=1}^N V_0^{\text{caplet, }i}, = \sum_{i=1}^{N} P(0,T_i),\Delta_i,\big[F_{i-1}(0)\Phi(d_{1,i}) - K\Phi(d_{2,i})\big],,$$

with appropriate $d_{1,i}, d_{2,i}$ for each caplet expiring $T_{i-1}$ . Similarly a floor price is the sum of floorlets:
$$V_0^{\text{floor}} = \sum_{i=1}^{N} P(0,T_i),\Delta_i,\big[K\Phi(-d_{2,i}) - F_{i-1}(0)\Phi(-d_{1,i})\big],.$$

The decomposition into caplets/floorlets is possible because LIBOR resets for different periods are independent under their respective forward measures (in a one-factor setting), and because the payoff is linear in these separate pieces. In multi-factor models, one must be careful, but by definition of a cap as a series of individual options, this additivity holds for [[Arbitrage Pricing of Derivatives|pricing]].

  

**Cap-Floor Parity:** As mentioned earlier, a long cap and long floor with the same strike $K$ on the same dates replicate a fixed rate guarantee: cap pays when rates above $K$, floor pays when below, so together they ensure you effectively always either receive or pay adjustments to achieve rate $K$. In fact, **Long Cap + Long Floor = [[Chapter 38 - T-Bond Option, Caps, Floors and Collar|Interest Rate Collar]]** that locks the rate at $K$. The cost of this collar equals the cost of a swap that would pay fixed $K$ (because achieving exactly $K$ payments is a fixed-rate bond). Thus, $V_0^{\text{cap}}(K) - V_0^{\text{floor}}(K) = V_0^{\text{payer swap}}(K)$ (the value of paying fixed $K$ vs floating) . If $K$ is set to the current swap [[Pricing Interest Rate Swaps|par rate]], $V_0^{\text{payer swap}}(K)=0$, so the cap and floor have the same price. This is an important consistency check in interest rate models.

  

**Use Cases:** A cap can protect a borrower with a floating-rate loan by capping the maximum interest rate they pay (beyond which the cap payouts compensate the extra interest). A floor can ensure a minimum interest income for a lender on a floating-rate [[An Asset Allocation Primer|investment]]. [[Interest Rate Derivatives-An Introduction to the  Pricing of Caps and Floors|Caps and floors]] are often structured with notional amortization schedules to match specific loan principals. They trade actively in the [[Chapter 9 Arbitrage and Hedging With Options|derivatives]] market (e.g. caps on 3M LIBOR for various maturities), and their implied volatilities form the **[[7. Black Scholes Model|volatility surface]]/skew** for [[Interest Rate Quotations|interest rates]].

  

**Summary ([[Black Models for Bond Price Options Capsfloors|Caps/Floors]]):** An interest rate cap is equivalent to a series of European call options on the interest rate for each period (caplets), and a floor is analogous with put options. Under no-[[Arbitrage Pricing of Derivatives|arbitrage]], the cap’s price is the sum of caplet prices, often computed with Black’s 1976 model . The [[Black Models for Bond Price Options Capsfloors|Black model]] formulas for caplets are akin to Black–Scholes, with forward LIBOR as underlying and discount bond as numeraire. Caps, [[Caps and Floors|floors]], and swaps satisfy parity relationships (cap – floor = swap) that must hold to avoid [[Arbitrage Pricing of Derivatives|arbitrage]]. These instruments allow market participants to trade and hedge [[Fixed Income Versus Equity Derivatives|interest rate volatility]] and to tailor risk profiles (e.g. a collar strategy, which is long a cap and short a floor, can set an interest rate band).

  

**Conclusion and Further Reading**

  

In these notes, we’ve systematically derived the [[Arbitrage Pricing of Derivatives|pricing]] of various [[A Practical Guide for Actuaries and other Business Professionals.|financial instruments]] – [[Forwards and Futures|forwards]], [[Futures Not Subject to Cash-And-Carry|futures]], bonds, swaps, swaptions, caps, and [[Caps and Floors|floors]] – using the twin principles of no [[Arbitrage Pricing of Derivatives|arbitrage]] and risk-neutral valuation. We started from the foundation that in an [[Exercises|arbitrage-free market]] there exists a [[Verifying Martingale Property with Q|risk-neutral measure]] enabling simple expected-value [[Arbitrage Pricing of Derivatives|pricing]] of discounted payoffs . We applied this to determine forward and [[Futures Not Subject to Cash-And-Carry|futures]] prices, seeing that forward prices are essentially expected future [[Contango And Backwardation In Arbitrage-Free Futures-Markets|spot prices]] grossed-up at the [[Black Scholes Derivation|risk-free rate]]. We then covered bond [[Arbitrage Pricing of Derivatives|pricing]] and the [[The Vasicek Model|term structure]], emphasizing how discount factors ensure consistency across maturities. Building on that, we priced interest rate swaps by equating fixed and floating-leg present values , and showed how a swap’s value evolves with changes in the [[Teaching Note 4 Interest Rate Derivatives|swap rate]] . Swaptions introduced optionality on swaps, and we presented Black’s formula as a convenient closed-form solution . Finally, we detailed [[Interest Rate Derivatives-An Introduction to the  Pricing of Caps and Floors|caps and floors]], breaking them into caplets/floorlets and again leveraging Black’s model for tractable [[Arbitrage Pricing of Derivatives|pricing]] . Throughout, we highlighted [[Purpose and Structure of Financial Markets 1|arbitrage strategies]] and intuitive reasoning (e.g. constructing replicating portfolios or using parity relations) to reinforce why the [[Arbitrage Pricing of Derivatives|pricing]] formulas take the form they do.

  

For further study, the following resources are recommended:

• **John C. Hull – Options, [[Futures Not Subject to Cash-And-Carry|Futures]], and Other [[Chapter 9 Arbitrage and Hedging With Options|Derivatives]]** (often updated, e.g. 10th edition, 2017): A comprehensive text covering [[Mathematics of the Financial Markets|derivatives pricing]] with an intuitive approach. Hull’s chapters on swaps, [[Futures Not Subject to Cash-And-Carry|futures]], and options provide concrete examples and additional context (e.g. [[Day-Count Conventions|day-count conventions]], collateral, etc.) beyond the idealized formulas.

• **Steven Shreve – [[6. A Brief Introduction to Stochastic Calculus|Stochastic Calculus]] for Finance II: [[Financial Mathematics Course|Continuous-Time Models]] (2004)**: This graduate-level text rigorously develops the [[Financial Mathematics Course|risk-neutral pricing]] framework with [[Continuous-Time Stochastic Processes|Brownian motion]] and martingales. It is an excellent reference for the theoretical foundations (including the Black–Scholes derivation, Girsanov’s theorem, and the fundamental theorems of [[Fixed Income Asset Pricing|asset pricing]]) that underlie the methods used in these notes.

• **Darrell Duffie – Dynamic [[Mean-Variance Efficient Returns and Pricing Fac|Asset Pricing Theory]] (3rd ed., 2001)**: A more abstract and advanced treatment of [[Risk-Neutral Pricing|arbitrage pricing]] in a general state-space setting. Duffie’s text is ideal for those interested in measure-theoretic foundations and the most general statements of the [[Pricing Forwards, Futures, Bonds, Swaps, Swaptions, Caps and Floors under No-Arbitrage and Risk-Neutral Pricing|no-arbitrage pricing]] theorems, as well as advanced topics like [[Lecture Notes on International Finance|incomplete markets]].

• **Fischer Black and Myron Scholes (1973), “The [[Arbitrage Pricing of Derivatives|Pricing]] of Options and Corporate Liabilities,” Journal of Political Economy**: The seminal paper introducing the Black–Scholes formula, which underpins much of risk-neutral option [[Arbitrage Pricing of Derivatives|pricing]]. While focused on equity options, the methodology is foundational for understanding how no-[[Forward Contracts and Forward Prices|arbitrage arguments]] can lead to partial differential equations and [[Chapter 40 - Pricing Fixed Income Options: Black’s Model and MCS|closed-form solutions]].

• **Fischer Black (1976), “The [[Arbitrage Pricing of Derivatives|Pricing]] of Commodity Contracts,” Journal of Financial Economics**: Black’s paper extends Black–Scholes to options on [[Futures Not Subject to Cash-And-Carry|futures]], which became the basis for [[Arbitrage Pricing of Derivatives|pricing]] caps, [[Caps and Floors|floors]], and swaptions (Black–76 model). It’s a short but insightful read to see how the formula we used for swaptions and caplets was originally derived for [[Futures Not Subject to Cash-And-Carry|futures]] options.

• **Damiano Brigo and Fabio Mercurio – Interest Rate Models: Theory and Practice (2nd ed., 2006)**: A thorough text specifically on interest rate [[Chapter 9 Arbitrage and Hedging With Options|derivatives]]. It covers the [[Arbitrage Pricing of Derivatives|pricing]] of caps, [[Caps and Floors|floors]], and swaptions in depth, examining the [[Black Models for Bond Price Options Capsfloors|Black model]] as well as more sophisticated models (Hull–White, LIBOR Market Model, etc.) for [[Interest Rate Quotations|interest rates]]. This is excellent for understanding the limitations of Black’s model and how one calibrates to cap/floor volatilities and swaption volatilities in practice.

• **Leif B. G. Andersen and Vladimir Piterbarg – [[Arbitrage-Free Interest Rate Models|Interest Rate Modeling]] (3-volume set, 2010)**: An advanced and encyclopedic resource on interest rate models, including detailed discussions on [[Swaptions|swaption pricing]], [[Arbitrage-Free Interest Rate Models|model calibration]], and the mathematics of no-[[Arbitrage Pricing of Derivatives|arbitrage]] [[Financial Mathematics Course|term structure models]]. Volume I lays the foundations and vanilla models, while Volume III goes into products and [[Financial Mathematics Course|risk management]].

• **Harrison & Kreps (1979) and Harrison & Pliska (1981)**: These papers formally develop the concept of equivalent [[Financial Mathematics Course|martingale measures]] and [[Financial Mathematics Course|risk-neutral pricing]] in both discrete and continuous time. They are the classic references for the fundamental theorems of [[Fixed Income Asset Pricing|asset pricing]] in academic finance.

  

By consulting these materials, one can deepen their understanding of both the practical formulas and the theoretical mechanisms behind them. Each of the instruments discussed has further nuances ([[Quantitative Trading Strategies Lecture Notes|credit risk]], collateralization, multi-curves for different interest rate benchmarks, etc.) which become important in real-world contexts. However, the no-[[Arbitrage Pricing of Derivatives|arbitrage]], [[Financial Mathematics Course|risk-neutral pricing]] paradigm remains the unifying theme that ensures different market prices all fit into a coherent, [[Arbitrage Pricing of Derivatives|arbitrage]]-free framework.
---
tags:
- archimedean_axiom
- artificial-intelligence
- continuity_property
- defi
- ma
- monotonicity
- mpt
- options
- preference_relation
- utility_index
aliases:
- Axiom 5.1
- Axiom 5.2
- Preference
- Utility Index
key_concepts:
- Agricultural futures and seasonality
- Alternative investments and hedge fund strategies
- Archimedean axiom
- Asset swaps and spread-lock strategies
- Barrier options and knock-in/knock-out structures
- Basis swaps and cross-currency basis adjustments
- Basis swaps and floating rate correlations
- Behavioral finance and market anomalies
- Best execution and regulatory requirements
- Bid-ask spreads and market making profitability
- Black-Litterman model and portfolio optimization
- CDO structuring and tranche allocation methodologies
- CDO-squared structures and correlation trading
- Calendar spreads and roll strategies
- Central clearing and CCP risk management
- Commodity futures and convenience yields
- Commodity swaps and energy derivatives
- Continuity property preference
- Crack spreads in energy markets
- Cryptocurrency valuation and blockchain technology
- Currency swaps and cross-currency basis
- Dark pools and alternative trading venues
- DeFi protocols and decentralized finance
- Deposit insurance and systemic risk
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
- Liquidity-adjusted VaR and liquidity horizons
- Margin requirements and collateral optimization
- Market impact and transaction cost analysis
- Mean reversion in interest rate processes
- Mergers and acquisitions due diligence
- Metal futures and industrial commodities
- Model backtesting and validation procedures
- Momentum and reversal investment strategies
- Monotonicity axiom
- Mortgage-backed securities and prepayment modeling
- Netting agreements and close-out procedures
- Non-deliverable forwards and emerging market instruments
- OIS discounting and collateralized interest rate derivatives
- Options on futures and forward-starting options
- Payment systems and settlement risk
- Preference relation
- Prime brokerage and securities lending
- Private credit and direct lending
- Project finance and syndicated lending
- Real estate investment trusts (REITs)
- Repo markets and securities lending
- Risk parity and risk budgeting strategies
- Shadow banking and non-bank intermediation
- Smart beta and alternative indexing approaches
- Stochastic volatility in interest rate markets
- Stress testing and scenario analysis frameworks
- Strictly increasing transformation
- Swaptions and interest rate option pricing
- Swaptions and option volatility surfaces
- Synthetic CDOs and credit-linked note structures
- Terminal value modeling and exit multiples
- 'The Greeks: Delta, Gamma, Vega, Theta, and Rho sensitivity analysis'
- Too-big-to-fail policies and resolution regimes
- Treasury futures and bond basis
- Treasury securities and government bond markets
- Utility index function
- VIX futures and volatility trading
- Value at Risk (VaR) and expected shortfall methodologies
- Value vs growth investing frameworks
- Vasicek and CIR interest rate models
- Vasicek and Cox-Ingersoll-Ross models
- Volatility smile and skew patterns in option markets
- Weighted average cost of capital (WACC) calculations
- Working capital and cash conversion cycle
- Wrong-way risk and correlation adjustments
enhanced: true
enhancement_date: '2025-11-06'
enhancement_id: batch04-161855
---




# 5.3 Utility indices  

A utility index for a given preference relation $\succeq$ is a function $\mathcal{U}:\mathcal{P}(Z)\to\mathbb{R}$ that to each probability distribution over consumption levels attaches a real-valued number such that  
$$
\pi_{1}\succeq\pi_{2}\quad\Leftrightarrow\quad\mathbb{U}(\pi_{1})\geq\mathbb{U}(\pi_{2}).
$$  

Note that a utility index is only unique up to a strictly increasing transformation. If $\mathrm{\mathcal{U}}$ is a utility index and $f:\mathbb{R}\to\mathbb{R}$ is any strictly increasing function, then the composite function $\mathcal{V}=f\circ\mathcal{U}$ defined by $\mathcal{V}(\pi)=f\left(\mathcal{U}(\pi)\right)$ , is also a utility index for the same preference relation.  

We will show below that a utility index exists under the following two axiomatic assumptions on the preference relation $\succeq$  

Axiom 5.1 (Monotonicity) Suppose that $\pi_{1},\pi_{2}\in\mathcal{P}(Z)$ with $\pi_{1}\succ\pi_{2}$ and let $a,b\in[0,1]$ .The preference relation $\succeq$ has the property that.  
$$
a>b\quad\Leftrightarrow\quad a\pi_{1}+(1-a)\pi_{2}\succ b\pi_{1}+(1-b)\pi_{2}.
$$  

This is certainly a very natural assumption on preferences. If you consider a weighted average of two probability distributions, you will prefer a high weight on the best of the two distributions.  

Axiom 5.2 (Archimedean) The preference relation $\succeq$ has the property that for any three probability distributions $\pi_{1},\pi_{2},\pi_{3}\in\mathcal{P}(Z)$ with $\pi_{1}\succ\pi_{2}\succ\pi_{3}$ , numbers $a,b\in(0,1)$ exist such that  
$$
a\pi_{1}+(1-a)\pi_{3}\succ\pi_{2}\succ b\pi_{1}+(1-b)\pi_{3}.
$$  

The axiom basically says that no matter how good a probability distribution $\pi_{1}$ is, it is so that for any $\pi_{2}\succ\pi_{3}$ we can find some mixed distribution of $\pi_{1}$ and $\pi_{3}$ to which $\pi_{2}$ is preferred. We just have to put a sufficiently low weight on $\pi_{1}$ in the mixed distribution. Similarly, no matter how bad a probability distribution $\pi_{3}$ is, it is so that for any $\pi_{1}\succ\pi_{2}$ we can find some mixed distribution of $\mathbf{\nabla}^{\prime}/{\mathfrak{I}}_{1}$ and $\pi_{3}$ that is preferred to $\pi_{2}$ . We just have to put a sufficiently low weight on $\pi_{3}$ in the mixed distribution.  

We shall say that a preference relation has the continuity property if for any three probability distributions $\pi_{1},\pi_{2},\pi_{3}\in\mathcal{P}(Z)$ with $\pi_{1}\succ\pi_{2}\succ\pi_{3}$ , a unique number $\alpha\in(0,1)$ exists such that  
$$
\pi_{2}\sim\alpha\pi_{1}+(1-\alpha)\pi_{3}.
$$  

We can easily extend this to the case where either $\pi_{1}\sim\pi_{2}$ or $\pi_{2}\sim\pi_{3}$ . For $\pi_{1}\sim\pi_{2}\succ\pi_{3}$ $\pi_{2}\sim1\pi_{1}+(1-1)\pi_{3}$ corresponding to $\alpha=1$ . For $\pi_{1}\succ\pi_{2}\sim\pi_{3}$ $\pi_{2}\sim0\pi_{1}+(1-0)\pi_{3}$ corresponding to $\alpha=0$ . In words the continuity property means that for any three probability distributions there is a unique combination of the best and the worst distribution so that the individual is indifferent between the third "middle' distribution and this combination of the other two. This appears to be closely related to the Archimedean Axiom and, in fact, the next lemma shows that the Monotonicity Axiom and the Archimedean Axiom imply continuity of preferences.  

Lemma 5.1 $L e t\succeq b e$ a preference relation satisfying the Monotonicity Axiom and the Archimedean Axiom. Then it has the continuity property.  

Proof: Given $\pi_{1}\succ\pi_{2}\succ\pi_{3}$ . Define the number $\alpha$ by  
$$
\alpha=\operatorname*{sup}\{k\in[0,1]\mid\pi_{2}\succ k\pi_{1}+(1-k)\pi_{3}\}.
$$  

By the Monotonicity Axiom we have that $\pi_{2}\succ k\pi_{1}+(1-k)\pi_{3}$ for all $k<\alpha$ and that $k\pi_{1}+$ $(1-k)\pi_{3}\succeq\pi_{2}$ for all $k>\alpha$ .We want to show that. $\pi_{2}\sim\alpha\pi_{1}+(1-\alpha)\pi_{3}$ . Note that by the.  

Archimedean Axiom, there is some $k>0$ such that $\pi_{2}\succ k\pi_{1}+(1-k)\pi_{3}$ and some $k<1$ such that $k\pi_{1}+(1-k)\pi_{3}\succ\pi_{2}$ . Consequently, $\alpha$ is in the open interval $(0,1)$  

Suppose that $\pi_{2}\succ\alpha\pi_{1}+(1-\alpha)\pi_{3}$ . Then according to the Archimedean Axiom we can find a number $b\in(0,1)$ such that $\pi_{2}\succ b\pi_{1}+(1-b)\{\alpha\pi_{1}+(1-\alpha)\pi_{3}\}$ . The mixed distribution on. the right-hand side has a total weight of. $k=b+(1-b)\alpha=\alpha+(1-\alpha)b>\alpha$ on $\pi_{1}$ . Hence we have found some. $k>\alpha$ for which $\pi_{2}\succ k\pi_{1}+(1-k)\pi_{3}$ . This contradicts the definition of $\alpha$ Consequently, we must have that. $\pi_{2}\not\vdash\alpha\pi_{1}+(1-\alpha)\pi_{3}$  

Now suppose that $\alpha\pi_{1}+(1-\alpha)\pi_{3}\succ\pi_{2}$ . Then we know from the Archimedean Axiom that a number $a\in(0,1)$ exists such that $a\{\alpha\pi_{1}+(1-\alpha)\pi_{3}\}+(1-a)\pi_{3}\succ\pi_{2}$ . The mixed distribution on the left-hand side has a total weight of $a\alpha<\alpha$ on $\pi_{1}$ . Hence we have found some $k<\alpha$ for which $k\pi_{1}+(1-k)\pi_{3}\succ\pi_{2}$ . This contradicts the definition of. $\alpha$ . We can therefore also conclude. that $\alpha\pi_{1}+(1-\alpha)\pi_{3}\not\vdash\pi_{2}$ . In sum, we have $\pi_{2}\sim\alpha\pi_{1}+(1-\alpha)\pi_{3}$  

The next result states that a preference relation which satisfies the Monotonicity Axiom and has the continuity property can always be represented by a utility index. In particular this is true when $\succeq$ satisfies the Monotonicity Axiom and the Archimedean Axiom.  

Theorem 5.1 $L e t\succeq b e$ a preference relation which satisfies the Monotonicity Axiom and has the continuity property. Then it can be represented by a utility index. $\mathrm{\mathcal{U}}$ , i.e. a function $\mathcal{U}:\mathcal{P}(Z)\to\mathbb{R}$ with the property that.  
$$
\pi_{1}\succeq\pi_{2}\quad\Leftrightarrow\quad\mathcal{U}(\pi_{1})\succeq\mathcal{U}(\pi_{2}).
$$  

Proof: Recall that we have assumed a best probability distribution $\mathbf{1}_{z^{u}}$ and a worst probability distribution $\mathbf{1}_{z^{l}}$ in the sense that  
$$
\succ{\mathbf{1}}_{z^{l}}\mathrm{or}{\mathbf{1}}_{z^{u}}\sim\pi\succ{\mathbf{1}}_{z^{l}}\mathrm{or}{\mathbf{1}}_{z^{u}}\succ\pi\sim{\mathbf{1}}_{z}
$$  

for any $\pi\in{\mathcal{P}}(Z)$ . For any $\pi\in{\mathcal{P}}(Z)$ we know from the continuity property that a unique number $\alpha_{\pi}\in[0,1]$ exists such that  
$$
\boldsymbol{\pi}\sim\alpha_{\pi}\mathbf{1}_{z^{u}}+(1-\alpha_{\pi})\mathbf{1}_{z^{l}}.
$$  

If ${\mathbf{1}}_{z^{u}}\sim\pi\succ{\mathbf{1}}_{z^{l}}$ $\alpha_{\pi}=1$ . If ${\mathbf{1}}_{z^{u}}\succ\pi\sim{\mathbf{1}}_{z^{l}}$ $\alpha_{\pi}=0$ . If $\mathbf{1}_{z^{u}}\succ\pi\succ\mathbf{1}_{z^{l}}$ $\alpha_{\pi}\in(0,1)$  

We define the function $\mathcal{U}:\mathcal{P}(Z)\to\mathbb{R}$ by $\mathcal{U}(\pi)=\alpha_{\pi}$ . By the Monotonicity Axiom we know that $\mathcal{U}(\pi_{1})\geq\\\\\mathcal{U}(\pi_{2})$ if and only if  
$$
\mathcal{U}(\pi_{1})\mathbf{1}_{z^{u}}+\left(1-\mathcal{U}(\pi_{1})\right)\mathbf{1}_{z^{l}}\succeq\mathcal{U}(\pi_{2})\mathbf{1}_{z^{u}}+\left(1-\mathcal{U}(\pi_{2})\right)\mathbf{1}_{z^{l}},
$$  

and hence if and only if $\pi_{1}\succeq\pi_{2}$ . It follows that. $\mathrm{\mathcal{U}}$ is a utility index..

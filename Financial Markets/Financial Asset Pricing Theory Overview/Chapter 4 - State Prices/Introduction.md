---
tags:
- dividend
- pricing
- distribution
- expected_returns
- continuous_time
- apt
- arbitrage
- put
- call
- financial-engineering
- financial-markets
- valuation
- pricing_rule
- present_value
- state_price_deflator
aliases:
- Pricing Assets
- State-Price Deflator
key_concepts:
- Arbitrage theory and no-arbitrage pricing
- Risk-neutral measures and martingale pricing
- Financial markets and securities trading
- Capital market instruments and their characteristics
- Modern portfolio theory and asset pricing
- Financial engineering and structured products
- Investment analysis and decision-making
- Financial regulation and market oversight
- Arbitrage pricing theory and no-arbitrage principle
- Financial markets and instrument analysis
- Quantitative finance and mathematical modeling
- Risk management and hedging strategies
- Investment analysis and portfolio theory
- Capital markets and trading strategies
- Financial engineering and product innovation
- Regulatory frameworks and compliance
- Market dynamics and behavioral finance
enhanced: true
enhancement_date: '2025-11-06'
enhancement_id: batch08-000419
batch: BATCH_AH
processing_agent: Enhancement Agent 8
---



# 4.1 Introduction  

If you want to price a set of assets, you could take them one by one and evaluate the dividends of each asset separately. However, to evaluate all assets in a consistent way (e.g. avoiding arbitrage). it is a better strategy first to figure out what your general pricing rule should be and subsequently you can apply that to any given dividend stream. The general pricing rule can be represented by a state-price deflator, which is the topic of this chapter. Basically, a state-price deflator contains information about the valuation of additional payments in different states and at different points in time. Combining that with the state- and time-dependent dividends of any asset, you can compute. a value or price of that asset..  

Section 4.2 defines the state-price deflator in each of our general frameworks (one-period, discrete-. time, continuous-time) and derives some immediate consequences for prices and expected returns.. Further important properties of state-price deflators are obtained in Section 4.3. Section 4.4 con-. tains examples of concrete distributional assumptions on the state-price deflator and the dividends that will lead to a closed-form expression for the present value of the dividends. Section 4.5 ex-. plains the difference between real and nominal state-price deflators. Finally, Section 4.6 gives a preview of some alternative ways of representing the information in a state-price deflator. These alternatives are preferable for some purposes and will be studied in more detail in later chapters..  

The concept of state prices was introduced and studied by Arrow (1951, 1953, 1971), Debreu (1954), Negishi (1960), and Ross (1978).

---
enhanced: true
enhancement_date: '2025-11-06'
enhancement_id: batch09-000182
key_concepts:
- Futures and forwards contract mechanics
- Cash-and-carry arbitrage
- Basis trading and roll strategies
- Untitled 5 and financial analysis
- Untitled 5 in modern finance
- Applications of Untitled 5
- 'Case study: Untitled 5'
- Financial markets and institutions
- Credit Risk Management and Default Probability
- Expected Loss and Loss Given Default Models
- Risk Measurement and VaR Backtesting
- Value at Risk and Expected Shortfall
- Credit Spreads and Rating Migration Analysis
- Stress Testing and Extreme Value Analysis
tags:
- roll
- futu
- recovery-rate
- expected-shortfall
- parametric-var
- conditional-var
- extreme-value-theory
- var-methodologies
- historical-var
- ' exposure-at-default'
- stress-testing
- unexpected-loss
- rating-migration
- expected-loss
- investment-analysis
- credit-migration
- default-probability
- value-at-risk
- credit-spreads
- financial-markets
- probabilty-of-default
- loss-given-default
- monte-carlo-var
- var-backtesting
---
--

```latex
\begin{longtable}[]{@{}lllll@{}} \toprule\noalign{} \endhead \bottomrule\noalign{} \endlastfoot \multirow{3}{=}{} & \multicolumn{4}{l@{}}{% Year ended March 31,} \\ & 2023 & 2024 & \multicolumn{2}{l@{}}{% 2025} \\ & RMB & RMB & RMB & US\$ \\ & \multicolumn{4}{l@{}}{% (in millions, except per share data)} \\ Revenue & 868,687 & 941,168 & 996,347 & 137,300 \\ Cost of revenue & (549,695) & (586,323) & (598,285) & (82,446) \\ Product development expenses & (56,744) & (52,256) & (57,151) & (7,876) \\ Sales and marketing expenses & (103,496) & (115,141) & (144,021) & (19,847) \\ General and administrative expenses & (42,183) & (41,985) & (44,239) & (6,096) \\ Amortization and impairment of intangible assets & (13,504) & (21,592) & (6,336) & (873) \\ Impairment of goodwill & (2,714) & (10,521) & (6,171) & (850) \\ Other gains, net & --- & --- & 761 & 105 \\ Income from operations & 100,351 & 113,350 & 140,905 & 19,417 \\ Interest and investment income, net & (11,071) & (9,964) & 20,759 & 2,861 \\ Interest expense & (5,918) & (7,947) & (9,596) & (1,323) \\ Other income, net & 5,823 & 6,157 & 3,387 & 467 \\ Income before income tax and share of results of equity method investees & 89,185 & 101,596 & 155,455 & 21,422 \\ Income tax expenses & (15,549) & (22,529) & (35,445) & (4,884) \\ Share of results of equity method investees & (8,063) & (7,735) & 5,966 & 822 \\ Net income & 65,573 & 71,332 & 125,976 & 17,360 \\ Net loss attributable to noncontrolling interests & 7,210 & 8,677 & 4,133 & 569 \\ Net income attributable to Alibaba Group Holding Limited & 72,783 & 80,009 & 130,109 & 17,929 \\ Accretion of mezzanine equity & (274) & (268) & (639) & (88) \\ Net income attributable to ordinary shareholders & 72,509 & 79,741 & 129,470 & 17,841 \\ Earnings per share attributable to ordinary shareholders(1) & & & & \\ Basic & 3.46 & 3.95 & 6.89 & 0.95 \\ Diluted & 3.43 & 3.91 & 6.70 & 0.92 \\ Earnings per ADS attributable to ordinary shareholders(1) & & & & \\ Basic & 27.65 & 31.61 & 55.12 & 7.60 \\ Diluted & 27.46 & 31.24 & 53.59 & 7.38 \\ \end{longtable}
```
$$\begin{longtable}[]{@{}lllll@{}} \toprule\noalign{} \endhead \bottomrule\noalign{} \endlastfoot \multirow{3}{=}{} & \multicolumn{4}{l@{}}{ Year ended March 31,} \\ & 2023 & 2024 & \multicolumn{2}{l@{}}{ 2025} \\ & RMB & RMB & RMB & US\$ \\ & \multicolumn{4}{l@{}}{ (in millions, except per share data)} \\ Revenue & 868,687 & 941,168 & 996,347 & 137,300 \\ Cost of revenue & (549,695) & (586,323) & (598,285) & (82,446) \\ Product development expenses & (56,744) & (52,256) & (57,151) & (7,876) \\ Sales and marketing expenses & (103,496) & (115,141) & (144,021) & (19,847) \\ General and administrative expenses & (42,183) & (41,985) & (44,239) & (6,096) \\ Amortization and impairment of intangible assets & (13,504) & (21,592) & (6,336) & (873) \\ Impairment of goodwill & (2,714) & (10,521) & (6,171) & (850) \\ Other gains, net & --- & --- & 761 & 105 \\ Income from operations & 100,351 & 113,350 & 140,905 & 19,417 \\ Interest and investment income, net & (11,071) & (9,964) & 20,759 & 2,861 \\ Interest expense & (5,918) & (7,947) & (9,596) & (1,323) \\ Other income, net & 5,823 & 6,157 & 3,387 & 467 \\ Income before income tax and share of results of equity method investees & 89,185 & 101,596 & 155,455 & 21,422 \\ Income tax expenses & (15,549) & (22,529) & (35,445) & (4,884) \\ Share of results of equity method investees & (8,063) & (7,735) & 5,966 & 822 \\ Net income & 65,573 & 71,332 & 125,976 & 17,360 \\ Net loss attributable to noncontrolling interests & 7,210 & 8,677 & 4,133 & 569 \\ Net income attributable to Alibaba Group Holding Limited & 72,783 & 80,009 & 130,109 & 17,929 \\ Accretion of mezzanine equity & (274) & (268) & (639) & (88) \\ Net income attributable to ordinary shareholders & 72,509 & 79,741 & 129,470 & 17,841 \\ Earnings per share attributable to ordinary shareholders(1) & & & & \\ Basic & 3.46 & 3.95 & 6.89 & 0.95 \\ Diluted & 3.43 & 3.91 & 6.70 & 0.92 \\ Earnings per ADS attributable to ordinary shareholders(1) & & & & \\ Basic & 27.65 & 31.61 & 55.12 & 7.60 \\ Diluted & 27.46 & 31.24 & 53.59 & 7.38 \\ \end{longtable}$$

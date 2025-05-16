---
tags:
  - basis_trade
  - financial_crisis
  - repo_market
  - treasury_futures
  - treasury_yields
aliases:
  - JPMorgan
  - Odd Lots
  - basis trade
  - hedge funds
key_concepts:
  - 2008 financial crisis
  - Basis trade explained
  - Hedge fund returns
  - Repo market funding
  - Treasury yields spike
---
# Basis Trade Explainer
I remember when the [basis trade](.md) first burst into the market’s collective consciousness.

It was March of 2020. The [stock market](../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20III%20THE%20PLAYERS/Chapter%2012%20-%20Hedge%20Fund%20Strategies/Hedge%20Fund%20Strategies.md) was crashing and Treasury yields had spiked to 1.19%. Now, as yields now surge to 4.46%, that doesn’t seem like a very big deal. But the direction of travel was unusual; when the [stock market](../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20III%20THE%20PLAYERS/Chapter%2012%20-%20Hedge%20Fund%20Strategies/Hedge%20Fund%20Strategies.md) crashes investors typically run to the perceived safety of [US Treasuries](../Credit%20Markets/Credit%20Market%20PSETS/Credit%20Market%20Homework%201.md). Now, in the depths of the pandemic, they were suddenly *running away*.

What was going on? Josh Younger, a favorite *[Odd Lots](.md)* guest who was then working at [JPMorgan](.md), published a note. I was head of the Asia News Desk at the time, and commissioned the talented [Stephen Spratt](https://archive.is/o/DIpfw/https://x.com/stephenspratt?lang=ar) (now at SocGen) to write the story. The [basis trade](.md) was blowing up.

That article was the first, to my knowledge, to really explain just what was going on (thank you Asia time zone). Since then the controversy over the [basis trade](.md) has only grown, with regulators occasionally threatening to clamp down on it but never really getting around to actually *doing* anything. And so, here we are five years later and the [basis trade](.md) is in the news again.

**Basis trades for dummies**

It’s worth taking a detour to explain just what the [basis trade](.md) is, and why it became so popular. To do that, we need to go back even further than the dark days of 2020 — all the way to the aftermath of the 2008 [financial crisis](../Financial%20Markets%20and%20Institutions/III.%20Liquidity%20of%20Assets/Class%209-%20Bailouts%20and%20Bank%20Failures/Squam%20Lake%20Group%20Letter.md).

Scarred by the near-collapse of the [financial system](../Contemporary%20Financial%20Intermediation%20Notes/Contemporary%20Financial%20Intermediation%20Notes.md), policymakers moved to make banks safer. They demanded the lenders hold more capital against potential losses, and that they carry big buffers of high-quality assets that could be easily sold to raise emergency money (that included [US Treasuries](../Credit%20Markets/Credit%20Market%20PSETS/Credit%20Market%20Homework%201.md)).

The upside of all these measures was a safer [banking system](../Financial%20Markets%20and%20Institutions/II.%20The%20Roles%20of%20Banks%20and%20Derivative%20Markets%20in%20Resolving%20Problems%20Inherent%20in%20Debt%20Contracts/Class%203-%20Financial%20Intermediation%20and%20Delegated%20Loan%20Monitoring%20,%20Intro%20to%20Bankruptcy%20and%20Debt%20Restructuring/Class%20Slide%203%20Financial%20Intermediation%20and%20Delegated%20Monitoring.md). The downside was shrinking bank balance sheets, diminished [liquidity](../Financial%20Markets%20and%20Institutions/III.%20Liquidity%20of%20Assets/Class%205-%20Private%20Information,%20Liquidity,%20and%20Securitization/Class%20Note%2010%20Liquidity%20and%20Class%20Note%2010%20Liquidity%20and%20Liquidity%20Managementliquidity%20management.md) and risk-taking appetite in the [banking system](../Financial%20Markets%20and%20Institutions/II.%20The%20Roles%20of%20Banks%20and%20Derivative%20Markets%20in%20Resolving%20Problems%20Inherent%20in%20Debt%20Contracts/Class%203-%20Financial%20Intermediation%20and%20Delegated%20Loan%20Monitoring%20,%20Intro%20to%20Bankruptcy%20and%20Debt%20Restructuring/Class%20Slide%203%20Financial%20Intermediation%20and%20Delegated%20Monitoring.md). It was harder and more expensive for big investors (clients) to borrow from the banks (broker-dealers). Without [leverage](../Advanced%20Investments/Lecture%206-Leverage,%20Tail%20Risk,%20Volatility%20Products.md), it was harder for clients to juice their [returns](../Financial%20Markets/Financial%20Asset%20Pricing%20Theory%20Overview/Chapter%203%20-%20%20Assets,%20Portfolios,%20and%20Arbitrage/Assets.md). This was also a problem for the banks; less balance sheet means less room to effectively rent risk to investors — that meant fewer fees.

But market participants are nothing if not creative (some might say they are a little *too* creative). And they found a fix for this problem: enter the [basis trade](.md).

The trade allowed investors — primarily [hedge funds](.md) and other active managers — to do two important things. The [basis trade](.md) involves betting on the difference between prices of cash Treasuries and Treasury [futures](../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%203%20-%20Futures%20Markets/Futures%20Not%20Subject%20to%20Cash-And-Carry.md). To do this, they effectively go long the cash bond and short the synthetic [futures](../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%203%20-%20Futures%20Markets/Futures%20Not%20Subject%20to%20Cash-And-Carry.md) contract.

This cash bond purchase is financed through the vast repo market — where market participants get their wholesale funding and short-term [liquidity](../Financial%20Markets%20and%20Institutions/III.%20Liquidity%20of%20Assets/Class%205-%20Private%20Information,%20Liquidity,%20and%20Securitization/Class%20Note%2010%20Liquidity%20and%20Class%20Note%2010%20Liquidity%20and%20Liquidity%20Managementliquidity%20management.md) by tapping those broker-dealers. The profit is the difference between prices paid for the cash bond and the simultaneous [futures](../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%203%20-%20Futures%20Markets/Futures%20Not%20Subject%20to%20Cash-And-Carry.md) contract *minus* financing costs. Financing costs for [US Treasuries](../Credit%20Markets/Credit%20Market%20PSETS/Credit%20Market%20Homework%201.md) — ostensibly one of the safest types of bonds out there — were pretty cheap!

The trade has the added benefit of amplifying [returns](../Financial%20Markets/Financial%20Asset%20Pricing%20Theory%20Overview/Chapter%203%20-%20%20Assets,%20Portfolios,%20and%20Arbitrage/Assets.md) for [hedge funds](.md). Because the difference between Treasury cash and [futures](../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%203%20-%20Futures%20Markets/Futures%20Not%20Subject%20to%20Cash-And-Carry.md) is normally tiny, borrowing overnight (effectively levering up the trade) means bigger payouts for the funds. Do it in enough volume and there was a sizeable profit to be made.

For broker dealers, the trade looked pretty sweet too. Post-2008 regulatory reform meant they had to be more strategic in how they used their balance sheet.

Here’s Josh Younger, writing back in March of 2020:

> “\[The [basis trade](.md)\] has been a common alpha-seeking strategy among actively managed funds for many decades. But more recently, it has grown due to regulatory constraints among dealers which incentivize large dealers to plan their balance sheet usage months in advance, which frequently takes the form of ‘use-it-or-lose-it’ allocations to end users. One way to occupy that sheet with limited downside is buying the [futures basis](Fixed%20Income%20Derivatives/Part%20II-Basis%20Trading%20and%20the%20Implied%20Repo%20Rate.md), in which the cash CTD is funded in overnight or term repo and paired with a short position in the contact, which in principle limits downside by allowing the fund to deliver these securities into the short [futures](../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%203%20-%20Futures%20Markets/Futures%20Not%20Subject%20to%20Cash-And-Carry.md) position. The CTD cash/[futures basis](Fixed%20Income%20Derivatives/Part%20II-Basis%20Trading%20and%20the%20Implied%20Repo%20Rate.md) has also generally traded with limited MTM volatility as well, which makes for an ideal way to preserve balance sheet allocations.”

[JPMorgan](.md) estimated that the [basis trade](.md) stood at nearly $400 billion dollars (proxied by the amount of short interest across Treasury [futures](../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%203%20-%20Futures%20Markets/Futures%20Not%20Subject%20to%20Cash-And-Carry.md) that didn’t seem to have much to do with economic bets. It’s not a perfect proxy but a [lack of transparency](../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20III%20THE%20PLAYERS/Chapter%2012%20-%20Hedge%20Fund%20Strategies/Hedge%20Fund%20Replication%20and%20Strategy%20Indexes.md) is a hallmark of the hedge fund industry. It’s hard to tell what they’re doing).

**The blow-up in basis**

But as markets came crashing down in March 2020, the [basis trade](.md) transformed into a problem instead of a solution. Suddenly renting out balance sheet to clients in this way didn’t look like such a great deal for banks. Sure, they were paid for this service, but they were in the process of de-risking and balance sheet was scarcer than ever.

And so, banks rushed for the exit. And they did so all at once.

This left [hedge funds](.md) in a bit of a basis bother (say that three times fast). Sure, they could hold their positions until maturity, which would give them some breathing room to realize losses. But as banks ratcheted down risk *en masse*, they could no longer roll over their positions. They now had to liquidate their basis trades.

To do this, they sold the cash Treasuries. With banks unable to warehouse additional inventory as they de-risked, the market hit an air pocket. Yields on the benchmark promptly 10-year spiked as investors shed their positions.

The Treasury market crash was only halted when the Federal Reserve stepped in with a raft of measures to stabilize the bond market. It bought some [$1 trillion worth of bonds](https://archive.is/o/DIpfw/https://www.bis.org/publ/work966.htm%23:~:text=Abstract,T%20of%20Treasuries%20in%202020Q1.) in that period. It started buying corporate bonds. There was an alphabet soup of backstops: CPFF, MML, PMCCF, SMCCF, PDCF, PPLE, and MSLF. The list goes on.

It’s worth emphasizing what a departure this was for the central bank. Citigroup analysts talked about how the measures had changed the corporate bond market forever; when things got really bad, the assumption was now that the central bank would step in. The same can be said of the Treasury market and the [basis trade](.md). There’s a belief that [the Fed](../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Front%20Matter/Monetary%20Policy%20with%20Abundantreserves.md) will always be there, hovering in the background, to provide that backstop for bonds even as regulators simultaneously debated the safety of these trades.

Why didn’t they move? Basis trades have the added effect of lubricating the Treasury market. Arbitraging the difference between cash and [futures](../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%203%20-%20Futures%20Markets/Futures%20Not%20Subject%20to%20Cash-And-Carry.md) keeps the spread low. Snapping up loads of cash bonds also means there’s an added demand for debt at tricky times. When [the Fed](../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Front%20Matter/Monetary%20Policy%20with%20Abundantreserves.md) started tightening its own balance sheet in 2017, this extra layer of absorption [was pretty useful](https://archive.is/o/DIpfw/https://www.federalreserve.gov/econres/notes/feds-notes/quantifying-treasury-cash-[futures](../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%203%20-%20Futures%20Markets/Futures%20Not%20Subject%20to%20Cash-And-Carry.md)-basis-trades-20240308.html). Killing off the [basis trade](.md) meant killing off a source of additional demand for Treasuries and [liquidity](../Financial%20Markets%20and%20Institutions/III.%20Liquidity%20of%20Assets/Class%205-%20Private%20Information,%20Liquidity,%20and%20Securitization/Class%20Note%2010%20Liquidity%20and%20Class%20Note%2010%20Liquidity%20and%20Liquidity%20Managementliquidity%20management.md) in the bond market.

**Back to the future with basis trades**

Today, basis trades are bigger than ever, estimated to be worth $800 billion [according to Apollo’s Torsten Slok](https://archive.is/o/DIpfw/https://www.apolloacademy.com/what-is-the-basis-trade/). You can see the rather stunning growth in this Federal Reserve chart, from 2024:

![](Attachments/9007c58eba723437721ec02663d565fe0a22fa76.webp)

Source: Federal Reserve

But basis trades aren’t the only things going on in bonds. Trump’s presidential win set in motion another dynamic: the expectation that banks would suddenly be free (er) from onerous regulatory requirements. This meant betting that cash Treasuries would outperform interest-rate swaps. Interest rate swaps allow investors to exchange fixed rates for floating rates. They are useful for [hedging](../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%205/Key%20Rates%20O1s%20Durations%20and%20Hedging.md) [interest rate exposure](../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20III%20THE%20PLAYERS/Chapter%2013%20-%20Banks%20Asset-Liability%20Management/Duration%20Gap%20Management.md). But as dreams of bank deregulation quickly began to die, they also meant that banks could warehouse risk ([duration](../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%205/Key%20Rates%20O1s%20Durations%20and%20Hedging.md)) without keeping bonds on their balance sheets.

Now, with the Trump administration not looking so bank-friendly and lenders rushing to de-risk, this trade is also blowing up. Swap spreads, which encapsulate the relationship between [US Treasuries](../Credit%20Markets/Credit%20Market%20PSETS/Credit%20Market%20Homework%201.md) and interest rate swaps, have plummeted. As [discussed in this space last year](https://archive.is/o/DIpfw/https://www.bloomberg.com/news/newsletters/2024-11-11/the-deregulation-trade-reaches-the-bond-market), the spreads had started surging back in November as Trump looked more and more likely to win and traders placed what was in effect a deregulation and [duration](../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%205/Key%20Rates%20O1s%20Durations%20and%20Hedging.md) trade.

![](Attachments/076668e170fc1a70324b296abc8e0823d49d8bf0.webp)

Source: Bloomberg

More generally, there has long been concern over [just who will buy [US Treasuries](../Credit%20Markets/Credit%20Market%20PSETS/Credit%20Market%20Homework%201.md)](https://archive.is/o/DIpfw/https://www.bloomberg.com/news/articles/2022-10-03/[jpmorgan](.md)-is-worried-about-who-s-going-to-buy-all-the-bonds) to help finance the America’s soaring deficit. The three main buyers of [US Treasuries](../Credit%20Markets/Credit%20Market%20PSETS/Credit%20Market%20Homework%201.md) — commercial banks, foreign governments, and the central bank itself — have all had their own special reasons for backing away from the market. The worry is that they’re backing away all at the same time. Balance sheet constraints mean banks can’t handle holding all these bonds at the same time if Treasuries are really being sold at scale.

By tightening post-2008 [banking regulation](../Advanced%20Financial%20Analysis%20and%20Valuation/Lecture%20Notes%20Advanced%20Financial%20Analysis%20and%20Valuation/Week%206/Week%206%20Bank%20Business%20Model,%20Regulation,%20and%20Accounting%20Rules.md), policymakers helped to shift risk out of the [banking system](../Financial%20Markets%20and%20Institutions/II.%20The%20Roles%20of%20Banks%20and%20Derivative%20Markets%20in%20Resolving%20Problems%20Inherent%20in%20Debt%20Contracts/Class%203-%20Financial%20Intermediation%20and%20Delegated%20Loan%20Monitoring%20,%20Intro%20to%20Bankruptcy%20and%20Debt%20Restructuring/Class%20Slide%203%20Financial%20Intermediation%20and%20Delegated%20Monitoring.md) and make it safer. But they did so at the cost of [liquidity in markets](../Financial%20Markets%20and%20Institutions/I-%20Introduction%20to%20Financial%20Markets%20and%20Intermediation/I-%20Introduction%20to%20Financial%20Markets%20and%20Intermediation/Lecture%20Note%201-%20Debt%20Pricing.md), which ultimately necessitated emergency moves from [the Fed](../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Front%20Matter/Monetary%20Policy%20with%20Abundantreserves.md). Policymakers helped create the problem, but they also came up with a solution.

Here’s Josh, writing in 2020 again:

> “The Covid-19 market pandemic arguably shows that the bank regulatory structure erected after 2008 can substitute a [liquidity crisis](../Financial%20Markets%20and%20Institutions/III.%20Liquidity%20of%20Assets/Class%207-%20CP,%20Repo,%20and%20the%20Crisis/Deciphering%20the%20Liquidity%20and%20Credit%20Crunch%202007–2008.md) for a [credit crisis](../Financial%20Markets%20and%20Institutions/III.%20Liquidity%20of%20Assets/Class%207-%20CP,%20Repo,%20and%20the%20Crisis/The%20Credit%20Crisis-Conjectures%20About%20Causes%20And%20Remedies.md). This is desirable in as much as central banks and other authorities have much more effective tools to deal with the former, provided they are deployed with sufficient speed and scale. **In that sense, forceful intervention by [the Fed](../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Front%20Matter/Monetary%20Policy%20with%20Abundantreserves.md) was arguably required by the post-GFC regulatory framework. Thankfully, they have done just that and, more importantly, have demonstrated they will act in the future.**”

Will they though? We know that [the Fed](../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Front%20Matter/Monetary%20Policy%20with%20Abundantreserves.md) is still worried about [inflation](../International%20Finance/Bridgewater/Principles%20For%20Navigating%20Big%20Debt%20Cycles/Part%20II%20Detailed%20Case%20Studies/German%20Debt%20Crisis%20andHyperinflation%20(1918–1924)/War%20Economies%20and%20Hyperinflation.md), especially as Trump’s tariffs look set to push up the price of good in the short-term (before growth slows and demand destruction kicks in). The central bank has been busy shrinking its balance sheet, and may be unwilling to start expanding it once again

This, I think, is the key difference with 2020. We know that [the Fed](../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Front%20Matter/Monetary%20Policy%20with%20Abundantreserves.md) does care about bond markets. They’re the benchmark rate for all other borrowing, and if they go up it puts real strains on the economy. The difficulty is, in the current climate, it’s hard to predict just when [the Fed](../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Front%20Matter/Monetary%20Policy%20with%20Abundantreserves.md) will respond to already-unpredictable trade policy.

So far, the deleveraging looks okay-ish. We haven’t seen rates in the repo market blow out just yet, but they are moving up. And things can change pretty fast in overnight markets. As another *[Odd Lots](.md)* favorite likes to say, lack of [liquidity](../Financial%20Markets%20and%20Institutions/III.%20Liquidity%20of%20Assets/Class%205-%20Private%20Information,%20Liquidity,%20and%20Securitization/Class%20Note%2010%20Liquidity%20and%20Class%20Note%2010%20Liquidity%20and%20Liquidity%20Managementliquidity%20management.md) “[kills you quick](https://archive.is/o/DIpfw/https://www.bloomberg.com/news/articles/2019-12-20/repo-oracle-zoltan-pozsar-expects-even-more-turmoil).” And in trying to make sure 2008 never happens again, policymakers have exchanged [credit risk](../Course%20Notes/Quantitative%20Trading%20Strategies%20Lecture%20Notes.md) for [liquidity risk](../Financial%20Markets%20and%20Institutions/III.%20Liquidity%20of%20Assets/Class%207-%20CP,%20Repo,%20and%20the%20Crisis/Asset%20Backed%20Commercial%20Paper%20Understanding%20the%20Risks.md).

![](Attachments/b10ede80348ce999ba7b84ad079732d35c52d83e.webp)

Source: Bloomberg

That’s not necessarily a bad thing! A key function of central banks is providing [liquidity](../Financial%20Markets%20and%20Institutions/III.%20Liquidity%20of%20Assets/Class%205-%20Private%20Information,%20Liquidity,%20and%20Securitization/Class%20Note%2010%20Liquidity%20and%20Class%20Note%2010%20Liquidity%20and%20Liquidity%20Managementliquidity%20management.md). That’s why we’ve all been quoting Bagehot’s dictum for more than 150 years. Central banks should lend freely against good collateral — and [US Treasuries](../Credit%20Markets/Credit%20Market%20PSETS/Credit%20Market%20Homework%201.md) are still the best form of collateral out there.

But things really are different this time. News coming out of the White House is erratic. The US seems to be trying to divorce from the rest of the world. The economy is in a different place and [the Fed](../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Front%20Matter/Monetary%20Policy%20with%20Abundantreserves.md) might be thinking of policy trade-offs in a different way.

It’s true that the very possibility of [the Fed](../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Front%20Matter/Monetary%20Policy%20with%20Abundantreserves.md) stepping into the bond market again may be enough to calm investors jangly nerves and keep a lid on the worst potential market moves. But so far, markets are getting spooked instead of soothed. There’s a real risk we go from spooked to downright scared.

### What Joe is thinking about

  
[As Tracy wrote about yesterday](https://archive.is/o/DIpfw/https://www.bloomberg.com/news/newsletters/2025-04-08/the-worst-defense-of-trump-s-tariffs), one of the crazy things about this market situation is that we know exactly where the problem is coming from: The White House.

Five minutes on the day’s stock markets winners and losers. And so people are gaming out all kinds of different scenarios for how the turmoil could come to an end. Maybe [the Fed](../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Front%20Matter/Monetary%20Policy%20with%20Abundantreserves.md) acts soon and that eases the market stress in some way (though no amount of Fed cutting will make industrial manufacturing capacity suddenly exist in the US). Maybe Congress removes Trump’s power to unilaterally impose tariffs. It’s not 100% inconceivable, I guess. A few senators here and there have talked about it. But at least right now, on April 9, 2025, I literally cannot envision House Speaker Mike Johnson bringing something like that to the floor.

But of course, the other possibility is that Trump just snaps his fingers and makes it all go away.

Just think! All Trump has to do is snap his fingers and this could all go away.  
  
And if he rescinded the tariffs, then we could go back to talking about how DeepSeek has kneecapped the booming AI business models that had been underpinning the [stock market](../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20III%20THE%20PLAYERS/Chapter%2012%20-%20Hedge%20Fund%20Strategies/Hedge%20Fund%20Strategies.md) rally.

If Trump rescinded the tariffs, we could go back to a world where America’s leading industrial company — Tesla — is seeing its global market share collapse in the face of steep competition and a brand that’s been deeply tarnished.

If Trump rescinds the tariffs, we can go back to a world where our closest trading partner — Canada — has massively changed its view on the US, with its citizens significantly less likely to travel here.

If Trump rescinds the tariffs, we can go back to talking about how Chinese biotech is rapidly winning market share from American ones, and how in spite of this, the US is cutting money for basic scientific research.

And finally, if Trump rescinds the tariffs, we can go back to a world where countries around the world are worried about Trump imposing tariffs again, making them more reluctant to enter into any kind of commercial or defense deal.

We can have all that if Trump snaps his fingers and reverses the tariffs.
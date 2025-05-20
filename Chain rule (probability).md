# Chain rule (probability)

In [probability theory](https://en.wikipedia.org/wiki/Probability_theory "Probability theory"), the **chain rule**[[1]](https://en.wikipedia.org/wiki/Chain_rule_\(probability\)#cite_note-1) (also called the **general product rule**[[2]](https://en.wikipedia.org/wiki/Chain_rule_\(probability\)#cite_note-2)[[3]](https://en.wikipedia.org/wiki/Chain_rule_\(probability\)#cite_note-3)) describes how to calculate the probability of the intersection of, not necessarily [independent](https://en.wikipedia.org/wiki/Independence_\(probability_theory\) "Independence (probability theory)"), events or the [joint distribution](https://en.wikipedia.org/wiki/Joint_distribution "Joint distribution") of [random variables](https://en.wikipedia.org/wiki/Random_variables "Random variables") respectively, using [conditional probabilities](https://en.wikipedia.org/wiki/Conditional_probabilities "Conditional probabilities"). This rule allows one to express a joint probability in terms of only conditional probabilities.[[4]](https://en.wikipedia.org/wiki/Chain_rule_\(probability\)#cite_note-4) The rule is notably used in the context of discrete [stochastic processes](https://en.wikipedia.org/wiki/Stochastic_process "Stochastic process") and in applications, e.g. the study of [Bayesian networks](https://en.wikipedia.org/wiki/Bayesian_network "Bayesian network"), which describe a [probability distribution](https://en.wikipedia.org/wiki/Probability_distribution "Probability distribution") in terms of conditional probabilities.

## Chain rule for events

### Two events

For two [events](https://en.wikipedia.org/wiki/Event_\(probability_theory\) "Event (probability theory)") $ A $ and $ B $, the chain rule states that

$ \mathbb {P} (A\cap B)=\mathbb {P} (B\mid A)\mathbb {P} (A) $,

where $ \mathbb {P} (B\mid A) $ denotes the [conditional probability](https://en.wikipedia.org/wiki/Conditional_probabilities "Conditional probabilities") of $ B $ given $ A $.

#### Example

An Urn A has 1 black ball and 2 white balls and another Urn B has 1 black ball and 3 white balls. Suppose we pick an urn at random and then select a ball from that urn. Let event $ A $ be choosing the first urn, i.e. $ \mathbb {P} (A)=\mathbb {P} ({\overline {A}})=1/2 $, where $ {\overline {A}} $ is the [complementary event](https://en.wikipedia.org/wiki/Complementary_event "Complementary event") of $ A $. Let event $ B $ be the chance we choose a white ball. The chance of choosing a white ball, given that we have chosen the first urn, is $ \mathbb {P} (B|A)=2/3. $ The intersection $ A\cap B $ then describes choosing the first urn and a white ball from it. The probability can be calculated by the chain rule as follows:

$ \mathbb {P} (A\cap B)=\mathbb {P} (B\mid A)\mathbb {P} (A)={\frac {2}{3}}\cdot {\frac {1}{2}}={\frac {1}{3}}. $

### Finitely many events

For events $ A_{1},\ldots ,A_{n} $ whose intersection has not probability zero, the chain rule states

$ {\begin{aligned}\mathbb {P} \left(A_{1}\cap A_{2}\cap \ldots \cap A_{n}\right)&=\mathbb {P} \left(A_{n}\mid A_{1}\cap \ldots \cap A_{n-1}\right)\mathbb {P} \left(A_{1}\cap \ldots \cap A_{n-1}\right)\\&=\mathbb {P} \left(A_{n}\mid A_{1}\cap \ldots \cap A_{n-1}\right)\mathbb {P} \left(A_{n-1}\mid A_{1}\cap \ldots \cap A_{n-2}\right)\mathbb {P} \left(A_{1}\cap \ldots \cap A_{n-2}\right)\\&=\mathbb {P} \left(A_{n}\mid A_{1}\cap \ldots \cap A_{n-1}\right)\mathbb {P} \left(A_{n-1}\mid A_{1}\cap \ldots \cap A_{n-2}\right)\cdot \ldots \cdot \mathbb {P} (A_{3}\mid A_{1}\cap A_{2})\mathbb {P} (A_{2}\mid A_{1})\mathbb {P} (A_{1})\\&=\mathbb {P} (A_{1})\mathbb {P} (A_{2}\mid A_{1})\mathbb {P} (A_{3}\mid A_{1}\cap A_{2})\cdot \ldots \cdot \mathbb {P} (A_{n}\mid A_{1}\cap \dots \cap A_{n-1})\\&=\prod _{k=1}^{n}\mathbb {P} (A_{k}\mid A_{1}\cap \dots \cap A_{k-1})\\&=\prod _{k=1}^{n}\mathbb {P} \left(A_{k}\,{\Bigg |}\,\bigcap _{j=1}^{k-1}A_{j}\right).\end{aligned}} $

#### Example 1

For $ n=4 $, i.e. four events, the chain rule reads

$ {\begin{aligned}\mathbb {P} (A_{1}\cap A_{2}\cap A_{3}\cap A_{4})&=\mathbb {P} (A_{4}\mid A_{3}\cap A_{2}\cap A_{1})\mathbb {P} (A_{3}\cap A_{2}\cap A_{1})\\&=\mathbb {P} (A_{4}\mid A_{3}\cap A_{2}\cap A_{1})\mathbb {P} (A_{3}\mid A_{2}\cap A_{1})\mathbb {P} (A_{2}\cap A_{1})\\&=\mathbb {P} (A_{4}\mid A_{3}\cap A_{2}\cap A_{1})\mathbb {P} (A_{3}\mid A_{2}\cap A_{1})\mathbb {P} (A_{2}\mid A_{1})\mathbb {P} (A_{1})\end{aligned}} $.

#### Example 2

We randomly draw 4 cards (one at a time) without replacement from deck with 52 cards. What is the probability that we have picked 4 aces?

First, we set $ {\textstyle A_{n}:=\left\{{\text{draw an ace in the }}n^{\text{th}}{\text{ try}}\right\}} $. Obviously, we get the following probabilities

$ \mathbb {P} (A_{1})={\frac {4}{52}},\qquad \mathbb {P} (A_{2}\mid A_{1})={\frac {3}{51}},\qquad \mathbb {P} (A_{3}\mid A_{1}\cap A_{2})={\frac {2}{50}},\qquad \mathbb {P} (A_{4}\mid A_{1}\cap A_{2}\cap A_{3})={\frac {1}{49}} $.

Applying the chain rule,

$ \mathbb {P} (A_{1}\cap A_{2}\cap A_{3}\cap A_{4})={\frac {4}{52}}\cdot {\frac {3}{51}}\cdot {\frac {2}{50}}\cdot {\frac {1}{49}}={\frac {24}{6497400}} $.

### Statement of the theorem and proof

Let $ (\Omega ,{\mathcal {A}},\mathbb {P} ) $ be a probability space. Recall that the [conditional probability](https://en.wikipedia.org/wiki/Conditional_probability "Conditional probability") of an $ A\in {\mathcal {A}} $ given $ B\in {\mathcal {A}} $ is defined as 

$ {\begin{aligned}\mathbb {P} (A\mid B):={\begin{cases}{\frac {\mathbb {P} (A\cap B)}{\mathbb {P} (B)}},&\mathbb {P} (B)>0,\\0&\mathbb {P} (B)=0.\end{cases}}\end{aligned}} $

Then we have the following theorem.

**Chain rule**— Let $ (\Omega ,{\mathcal {A}},\mathbb {P} ) $ be a probability space. Let $ A_{1},...,A_{n}\in {\mathcal {A}} $. Then

$ {\begin{aligned}\mathbb {P} \left(A_{1}\cap A_{2}\cap \ldots \cap A_{n}\right)&=\mathbb {P} (A_{1})\mathbb {P} (A_{2}\mid A_{1})\mathbb {P} (A_{3}\mid A_{1}\cap A_{2})\cdot \ldots \cdot \mathbb {P} (A_{n}\mid A_{1}\cap \dots \cap A_{n-1})\\&=\mathbb {P} (A_{1})\prod _{j=2}^{n}\mathbb {P} (A_{j}\mid A_{1}\cap \dots \cap A_{j-1}).\end{aligned}} $

**Proof**

The formula follows immediately by recursion

$ {\begin{aligned}(1)&&&\mathbb {P} (A_{1})\mathbb {P} (A_{2}\mid A_{1})&=&\qquad \mathbb {P} (A_{1}\cap A_{2})\\(2)&&&\mathbb {P} (A_{1})\mathbb {P} (A_{2}\mid A_{1})\mathbb {P} (A_{3}\mid A_{1}\cap A_{2})&=&\qquad \mathbb {P} (A_{1}\cap A_{2})\mathbb {P} (A_{3}\mid A_{1}\cap A_{2})\\&&&&=&\qquad \mathbb {P} (A_{1}\cap A_{2}\cap A_{3}),\end{aligned}} $

where we used the definition of the conditional probability in the first step.

## Chain rule for discrete random variables

### Two random variables

For two discrete random variables $ X,Y $, we use the events$ A:=\{X=x\} $ and $ B:=\{Y=y\} $ in the definition above, and find the joint distribution as

$ \mathbb {P} (X=x,Y=y)=\mathbb {P} (X=x\mid Y=y)\mathbb {P} (Y=y), $

or 

$ \mathbb {P} _{(X,Y)}(x,y)=\mathbb {P} _{X\mid Y}(x\mid y)\mathbb {P} _{Y}(y), $

where $ \mathbb {P} _{X}(x):=\mathbb {P} (X=x) $ is the [probability distribution](https://en.wikipedia.org/wiki/Probability_distribution "Probability distribution") of $ X $ and $ \mathbb {P} _{X\mid Y}(x\mid y) $[conditional probability distribution](https://en.wikipedia.org/wiki/Conditional_probability_distribution "Conditional probability distribution") of $ X $ given $ Y $.

### Finitely many random variables

Let $ X_{1},\ldots ,X_{n} $ be random variables and $ x_{1},\dots ,x_{n}\in \mathbb {R} $. By the definition of the conditional probability,

$ \mathbb {P} \left(X_{n}=x_{n},\ldots ,X_{1}=x_{1}\right)=\mathbb {P} \left(X_{n}=x_{n}|X_{n-1}=x_{n-1},\ldots ,X_{1}=x_{1}\right)\mathbb {P} \left(X_{n-1}=x_{n-1},\ldots ,X_{1}=x_{1}\right) $

and using the chain rule, where we set $ A_{k}:=\{X_{k}=x_{k}\} $, we can find the joint distribution as

$ {\begin{aligned}\mathbb {P} \left(X_{1}=x_{1},\ldots X_{n}=x_{n}\right)&=\mathbb {P} \left(X_{1}=x_{1}\mid X_{2}=x_{2},\ldots ,X_{n}=x_{n}\right)\mathbb {P} \left(X_{2}=x_{2},\ldots ,X_{n}=x_{n}\right)\\&=\mathbb {P} (X_{1}=x_{1})\mathbb {P} (X_{2}=x_{2}\mid X_{1}=x_{1})\mathbb {P} (X_{3}=x_{3}\mid X_{1}=x_{1},X_{2}=x_{2})\cdot \ldots \\&\qquad \cdot \mathbb {P} (X_{n}=x_{n}\mid X_{1}=x_{1},\dots ,X_{n-1}=x_{n-1})\\\end{aligned}} $

### Example

For $ n=3 $, i.e. considering three random variables. Then, the chain rule reads

$ {\begin{aligned}\mathbb {P} _{(X_{1},X_{2},X_{3})}(x_{1},x_{2},x_{3})&=\mathbb {P} (X_{1}=x_{1},X_{2}=x_{2},X_{3}=x_{3})\\&=\mathbb {P} (X_{3}=x_{3}\mid X_{2}=x_{2},X_{1}=x_{1})\mathbb {P} (X_{2}=x_{2},X_{1}=x_{1})\\&=\mathbb {P} (X_{3}=x_{3}\mid X_{2}=x_{2},X_{1}=x_{1})\mathbb {P} (X_{2}=x_{2}\mid X_{1}=x_{1})\mathbb {P} (X_{1}=x_{1})\\&=\mathbb {P} _{X_{3}\mid X_{2},X_{1}}(x_{3}\mid x_{2},x_{1})\mathbb {P} _{X_{2}\mid X_{1}}(x_{2}\mid x_{1})\mathbb {P} _{X_{1}}(x_{1}).\end{aligned}} $
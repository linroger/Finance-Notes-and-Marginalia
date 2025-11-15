---
tags:
- financial-instruments/call
- financial-instruments/cap
- quantitative-models/stochastic
- quantitative-methods/var
- mathematical-finance/discrete
- mathematics/probability
- mathematics/stochastic
- stochastic-calculus
- educational-level/intermediate
key_concepts:
- stochastic calculus and Ito processes
- value at risk and tail risk measurement
- financial mathematics and quantitative analysis
- derivatives and structured products
- risk management and portfolio optimization
- stochastic processes in finance
- mathematical modeling and simulation
type: note
status: active
academic_level: graduate
professional_application: practical
institutional_standard: true
---

# Chain rule (probability)

In [probability theory](https://en.wikipedia.org/wiki/Probability_theory "Probability theory"), the **chain rule**[[1]](https://en.wikipedia.org/wiki/Chain_rule_\(probability\)#cite_note-1) (also called the **general product rule**[[2]](https://en.wikipedia.org/wiki/Chain_rule_\(probability\)#cite_note-2)[[3]](https://en.wikipedia.org/wiki/Chain_rule_\(probability\)#cite_note-3)) describes how to calculate the probability of the intersection of, not necessarily [independent](https://en.wikipedia.org/wiki/Independence_\(probability_theory\) "Independence (probability theory)"), events or the [joint distribution](https://en.wikipedia.org/wiki/Joint_distribution "Joint distribution") of [random variables](https://en.wikipedia.org/wiki/Random_variables "Random variables") respectively, using [conditional probabilities](https://en.wikipedia.org/wiki/Conditional_probabilities "Conditional probabilities"). This rule allows one to express a joint probability in terms of only conditional probabilities.[[4]](https://en.wikipedia.org/wiki/Chain_rule_\(probability\)#cite_note-4) The rule is notably used in the context of discrete [stochastic processes](https://en.wikipedia.org/wiki/Stochastic_process "Stochastic process") and in applications, e.g. the study of [Bayesian networks](https://en.wikipedia.org/wiki/Bayesian_network "Bayesian network"), which describe a [probability distribution](https://en.wikipedia.org/wiki/Probability_distribution "Probability distribution") in terms of conditional probabilities.

## Chain rule for events

### Two events

For two [events](https://en.wikipedia.org/wiki/Event_\(probability_theory\) "Event (probability theory)")$A$and$B$, the chain rule states that

$\mathbb {P} (A\cap B)=\mathbb {P} (B\mid A)\mathbb {P} (A)$,

where$\mathbb {P} (B\mid A)$denotes the [conditional probability](https://en.wikipedia.org/wiki/Conditional_probabilities "Conditional probabilities") of$B$given$A$.

#### Example

An Urn A has 1 black ball and 2 white balls and another Urn B has 
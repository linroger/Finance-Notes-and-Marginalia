---
tags:
  - cubic_spline
  - curve_fitting
  - interest_rates
  - market_practitioners
  - term_structure
aliases:
  - Cubic Spline Implementation
  - Fitting Interest Rates
  - Term Structure Modeling
key_concepts:
  - cubic spline method
  - fitting discount function
  - market practitioners valuation
  - parametric vs spline methods
  - term structure interest rates
---

# [](../1.%20DeterministicCashFlows.md#3%20The%20Term%20Structure%20Of%20Interest%20Rates|Fitting%20the%20Term%20Structure%20of%20Interest%20Rates)
# [](../1.%20DeterministicCashFlows.md#3%20The%20Term%20Structure%20Of%20Interest%20Rates|Fitting%20the%20Term%20Structure%20of%20Interest%20Rates): The Practical Implementation  of  Cubic Spline Methodology
# INTRODUCTION

# Fitting the term structure of interest rates

The [term structure of interest rates](../6.%20A%20Brief%20Introduction%20to%20Stochastic%20Calculus.md) defines the set of spot or zero-coupon rates that exist in a  debt capital market, of default-free bonds, distinguished only by their term to maturity. In  practice the [term structure](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%209/The%20Vasicek%20Model.md) is defined as the array of discount factors on the same maturity  term. Extracting the [term structure](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%209/The%20Vasicek%20Model.md) from market [interest rates](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%202/Interest%20Rate%20Quotations.md) has been the focus of extensive  research, reflecting its importance in the field of finance.

The [term structure](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%209/The%20Vasicek%20Model.md) is used by market practitioners for valuation purposes and by central banks  for [forecasting](../../Advanced%20Financial%20Analysis%20and%20Valuation/Lecture%20Notes%20Advanced%20Financial%20Analysis%20and%20Valuation/Week%202/Week%202%20Fundamentals%20Of%20Forecasting.md) purposes. The accurate fitting of the [term structure](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%209/The%20Vasicek%20Model.md) is vital to the smooth  functioning of the market. A number of approaches have been proposed with which to  undertake this, and the method chosen is governed by the user’s requirements. Practitioners  desire an approach that is accessible, straightforward to implement and as accurate as  possible. In general there are two classes of curve fitting techniques; the  parametric  methods,  so-called because they attempt to model the yield curve using a parametric function; and the  spline  methods.  Parametric methods include the [Nelson-Siegel model](../../Credit%20Markets/Credit%20Market%20PSETS/Advanced%20Usage%20of%20QuantLib%20analytics%20library.md) and a modification of  this proposed by Svensson (1994, 1995), as well as models described by Wiseman (1994) and  Bjork and Christensen (1997).  James and Webber (2000) suggest that these methods produce  a satisfactory overall shape for the [term structure](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%209/The%20Vasicek%20Model.md) but are suitable only where good accuracy is  not required.  Market practitioners instead generally prefer an approach that gives a  reasonable trade-off between accuracy and ease of implementation, an issue we explore in this  article.

The cubic spline process presents no conceptual problems, and is an approximation of the  market [discount function](../../Financial%20Markets/Financial%20Asset%20Pricing%20Theory%20Overview/Chapter%2010%20-%20The%20Economics%20of%20the%20Term%20Structure%20of%20Interest%20Rates/Basic%20Interest%20Rate%20Concepts%20and%20Relations.md). McCulloch (1975) uses cubic splines and Beim (1992) states that  this approach performs at least as satisfactorily as other methods.  Although the basic  approach can lead to unrealistic shapes for the forward curve (for example, see [Vasicek](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%209/The%20Vasicek%20Model.md) and  Fong (1982) and their suggested improvement on the approach using exponential splines), it  is an accessible method and one that gives reasonable accuracy for the [spot rate](../../International%20Finance/The%20Foreign%20Exchange%20Market%20Annotations.md) curve. Adams  and Van Deventer (1994) illustrate using the technique to obtain maximum smoothness for  forward curves (and an extension to  quartic  splines), while the basic technique has been  improved as described by Fisher, Nychka and Zervos (1995), Waggoner (1997) and Anderson  and Sleath (1999). These references are considered later.

Splines are a non-parametric polynomial interpolation method.  There is more than one way  of fitting them. The simplest method is an ordinary least squares regression spline, but this  approach produces wildly oscillating curves. The more satisfactory is a smoothing splines  method. We consider the basic approach and how to implement it in this article.
# Cubic Splines

# Fitting a discount function

In mathematics a spline is a piecewise polynomial function, made up of individual polynomial  sections or segments that are joined together at (user-selected) points known as  knot points .  Splines used in [term structure](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%209/The%20Vasicek%20Model.md) modelling are generally made up with cubic polynomials, and  the reason for cubic polynomials, as opposed to polynomials of order say, two or five, is  explained in straightforward fashion by de la Grandville (2001).  A cubic spline is a function  of order three, and a piecewise cubic polynomial that is twice differentiable at each knot  point. At each knot point the slope and curvature of the curve on either side must match. We  employ the cubic spline approach to fit a smooth curve to bond prices (yields) given by the  term discount factors.

A polynomial of sufficiently high order may be used to approximate to varying degrees of  accuracy any continuous function, which is why a polynomial approximation of a yield curve  may be attempted. For example James and Webber (2000) state that given a set of  m  points  with distinct values, a Lagrange polynomial of degree  m  will pass through every point.   However the fit can be very wild with extreme behaviour at the long end. We will  demonstrate how a cubic spline approximation can be used to obtain better results.

This paper provides a discussion of piecewise cubic spline interpolation methodology and its  application to the [term structure](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%209/The%20Vasicek%20Model.md). The authors’ intent is to provide a comprehensive and  accessible approach to cubic spline interpolation for implementation by practitioners. At the  end of this paper the reader should have a full understanding of how cubic splines are  calculated and the implications of using piecewise cubic spline interpolation methods. In  addition the user can employ the approach shown to implement the methodology for their  own applications, including constructing spot and forward yield curves from marketdetermined [interest rates](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%202/Interest%20Rate%20Quotations.md). We recommend a cubic spline technique because this ensures that  the curve passes through all the selected (market determined) node points. This enables  practitioners to fit a yield curve to observed market rates (Libor or bond yields) reasonably  accurately  and produces a satisfactory zero coupon curve under most circumstances.

Our starting point is a set of zero curve tenors (or discount factors) obtained from a collection  of market instruments such as cash deposits, [futures](../../Financial%20Markets/Financial%20Engineering%20and%20Arbitrage%20in%20the%20Financial%20Markets/PART%20I%20RELATIVE%20VALUE%20BUILDING%20BLOCKS/Chapter%203%20-%20Futures%20Markets/Futures%20Not%20Subject%20to%20Cash-And-Carry.md), swaps or coupon bonds. We therefore  have a set of tenor points and their respective zero rates (or discount factors). The  mathematics of cubic splines is straightforward but we assume a basic understanding of  calculus and a familiarity with solving simultaneous linear equations by substitution. An  account of the methods analysed in this paper is given in Burden and Faires (1997), which has  very accessible text on cubic spline interpolation.
# Background on cubic splines

When fitting a curve by interpolating between nodes or tenor points, the user must consider  conflicting issues. There is a need to balance between simplicity and correctness, and hence a  trade off between ease of use and the accuracy of the result. In certain cases practitioners will  accept a lower degree of accuracy at the nodes, in favour of smoothness across the curve. In  the cubic spline approach the primary aim is smoothness. In an attempt to create a smooth and  accurate measurement at the nodes however, we may be confronted by oscillation in the  curve. Although linear interpolation is a reasonable calculation method, interest rate markets  are not linear environments made up of coupled straight lines. The point between two tenors  cannot be accurately estimated using a straight line.

Although there are a number of alternative methods available to the practitioner, a reasonable  approach is to stick with the concept of piecewise interpolation but to abandon the use of  straight lines. The reason that we do not depart from piecewise interpolation, is that this  method of curve smoothing provides accuracy at the nodes because each piecewise function  touches a node. Accuracy at the nodes can be an important consideration when a [pricing](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%207/Arbitrage%20Pricing%20of%20Derivatives.md)  methodology based on the elimination of [arbitrage](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%207/Arbitrage%20Pricing%20of%20Derivatives.md) is employed. Thus we continue with  piecewise fitting, but instead of applying a linear fitting technique, we apply a cubic  polynomial to each piece of the interpolation. Cubic splines provide a great deal of flexibility  in creating a continuous smooth curve both between and at tenor points.

# CUBIC SPLINE METHODOLOGY

We assume that the practitioner has already calculated a set of nodes using a yield curve  construction technique such as boots trapping. A zero curve is then fitted using the cubic  spline methodology by interpolating between nodes using individual cubic polynomials. Each  polynomial has its own parameters but are constructed in such a way that their ends touch  each node at the start and end of the polynomial. The set of splines, which touch at the nodes,  therefore form a continuous curve. Our objective is to produce a continuous curve, joining  market observed rates as smoothly as possible, which is the most straightforward means by  which we can deduce meaningful data on the correct [interest rate term structure](../../Course%20Notes/Python/QuantLib-Python/Valuing%20Interest%20Rate%20Caps%20and%20Floors%20Using%20QuantLib%20Python.md) in the market.

 ![500](Attachments/500-458.jpg)
Exhibit 1
In Exhibit 1 we can see that two cubic polynomials which join at point  $x_{N+I}$   are used to form a  continuous curve. However, it is also clear from the curves in figure 1 that the two  polynomials do not result in a smooth curve. In order to have a smooth curve we need to  establish “smoothing” criteria for each spline. To do this we must first ensure that the  polynomials touch or join together at the nodes. Secondly we must ensure that where the  polynomials touch that the curve is smooth. Finally we ensure that the curve is continuously  differentiable, or in other words, the curve has a smooth rate of change at and between tenor  points. The required criteria to meet these conditions are:

Requirement 1 : the value of each polynomial is equal at tenor points;

Requirement 2 : the first differential of each polynomial is equal at tenor points;

Requirement 3 : the second differential of each polynomial is equal at tenor points; and

Requirement 4 : the second differential of each polynomial is continuous between tenor  points.

Considering a polynomial of the form   $y\ \ =\ \ a x^{3}\!+\!b x^{2}\!+\!c x\!+\!d,$  ,  the second differential    $y\,^{\ast}\!\!=\,6a x\;+\;2b$   is a linear function and by its very definition is continuous between tenor  points. The fourth requirement is therefore always met and this paper will not deal with this  requirement in any further detail. The rest of this paper will refer to the first three  requirements and how they are met at the nodes.

# THE HYPOTHESIS

Assuming the final solution is unknown at this stage, it seems plausible that an almost infinite  set of parameters   $a,~b$    and   $c$   can be found which will result in all of our cubic spline  requirements being met.

 ![500](Attachments/500-459.jpg)
Exhibit 2

We observe in Exhibit 2 three imaginary curves, all of which would meet our requirements  that the:

  first differential of each spline is equal at tenor points; and

   second differential of each spline is equal at tenor points.
Admittedly we have considered nodes that are sitting in a straight line but even where the  nodes do not line up it may be possible to find a range of possible solutions. Taking this  further, spline A and spline B as shown in Exhibit 3 are valid solutions yet it is intuitive,  given our knowledge of interest rate markets, that A is likely to be more suitable for our  purposes of yield curve interpolation.

 ![500](Attachments/500-453.jpg)
Exhibit 3

The issue to determine therefore, is, is there an infinite set of parameters each of which would  meet our requirements for fitting the curve; or is it possible to determine a single solution? Of  course our requirement is in a single solution; moreover, a solution that can be found quickly  from any set of market rates.

# PRACTICAL APPROACH

# A working environment

By splitting the yield curve into individual node/tenor pairs, we may work with individual  lines within each tenor. A cubic polynomial can then be added to each line to provide the  cubic spline. For ease of illustration, we take this one step further and imagine an alternative  horizontal axis. This is referred to as  ‘capital’  $X$  as shown in Exhibit 4. Assume that between  each node pair that this horizontal axis  $X$   runs from  $\boldsymbol{\theta}$   (at  $x_{N}$  ) to  $x_{N+I}\,-\,x_{N}$    (at  $x_{N+l.}\,$  ).
 ![500](Attachments/500-440.jpg)
Exhibit 4

In Exhibit 4 the  $X$   axis is a calculated value determined from the  $x$   axis. The points  $x_{N}$  and  $x_{N+I}$    are isolated for spline   $S_{N}$  . It is then assumed that   $X_{\theta}$   equals zero at   $x_{N}$   and stretches to   $X_{N}$    which equals   $(x_{N+I}–x_{N})$   on the  $X$   axis. If these lines are fully isolated then a cubic polynomial,  of the form  $y=a X^{3}+b X^{2}+c X+d$  , can be constructed to touch the points  $x_{N}$   and  $x_{N+I}$  .

# The first requirement

In order for the polynomial to touch the nodes then a cubic polynomial must be constructed so  that at point   $X_{\theta}$    the polynomial provides a results that is equal to   $y_{N.}$  .  This is very easy to  achieve. Since  $X$   is equal to zero at its starting point, the polynomial takes the following form :
$$
\begin{array}{l c r}{{y_{_N}=a_{_N}0^{3}+b_{_N}0^{2}+c_{_N}0+d_{_N}}}\\ {{y_{_N}=d_{_N}}}\end{array}
$$

So as long as  $d_{N}$   is equal to  $y_{N}$   then our polynomial will touch the node at  $X_{\theta}$  .

In order for the polynomial to touch the second node, the node at point   $x_{N+I}$  ,   then the  polynomial must take the following form at point  $X_{N}$  :
$$
y_{N+1}=a_{N}(x_{N+1}-x_{N})^{3}+b_{N}(x_{N+1}-x_{N})^{2}+c_{N}(x_{N+1}-x_{N})+d_{N}
$$

OR
$$
\boxed{d_{\scriptscriptstyle{N+1}}=a_{\scriptscriptstyle{N}}{X_{\scriptscriptstyle{N}}}^{3}+b_{\scriptscriptstyle{N}}{X_{\scriptscriptstyle{N}}}^{2}+c_{\scriptscriptstyle{N}}X_{\scriptscriptstyle{N}}+d_{\scriptscriptstyle{N}}}
$$

where:  $X_{N}=x_{N+l}-x_{N}$
It is worth noting that at this point in our process we do not know what the values of   $a$  ,   $b$   or  $c$    are. These will be derived below from our other requirements.

# The second requirement

To meet the second requirement of a cubic spline, the first differential  ${y_{N}}^{,}$     must equal the first  differential  $y_{N+I}$  ’   at the tenor point  $x_{N+I}$  .

In other words at node  $x_{N+I}$  :
$$
3a_{_{N}}X{_{_{N}}}^{2}+2b_{_{N}}X_{_{N}}+c_{_{N}}=3a_{_{N+1}}X{_{_{N+1}}}^{2}+2b_{_{N+1}}X_{_{N+1}}+c_{_{N+1}}
$$

We know from our conditional working environment that at node  $x_{N+I}$   for function  ${y_{N}}^{*}$   that  $X$   $=(x_{N+l}-x_{N})$  . We also know from the same assumption that   $X=\,\theta$   at the start of the next  polynomial, i.e. for function  $y_{N+I}$  ’ . Therefore:
$$
3a_{_{N+1}}0^{2}+2b_{_{N+1}}0+c_{_{N+1}}=3a_{_{N}}{X_{_{N}}}^{2}+2b_{_{N}}X_{_{N}}+c_{_{N}}
$$

so that

 ![500](Attachments/500-453.jpg)

# Third requirement

To meet the third requirement of a cubic spline, the second differential   $y_{N}$  ”   assessed at the  point  $x_{N+I}$   should equal the second differential  $y_{N+l}\,,$  .

In other words at node  $x_{N+l}$  :
$$
6a_{\scriptscriptstyle N}X_{\scriptscriptstyle N}+2b_{\scriptscriptstyle N}=6a_{\scriptscriptstyle N+1}X_{\scriptscriptstyle N+1}+2b_{\scriptscriptstyle N+1}
$$

We know from our conditions that at node  $x_{N+l}$   for function  $y_{N}$  ”  that  $X=(x_{N+l}-x_{N})$  . We also  know from the same assumption that  $X=\theta$   for function  ${y_{N+l}}^{,}$  . Therefore:
$$
\begin{array}{l}{{6a_{_N}X_{_N}+2b_{_N}=6a_{_{N+1}}0+2b_{_{N+1}}}}\\ {{6a_{_N}X_{_N}=2b_{_{N+1}}-2b_{_N}}}\end{array}
$$
$$
\boxed{a_{N}=\frac{b_{N+1}-b_{N}}{3X_{N}}}
$$

# Meeting all requirements simultaneously

We now have equations which ensure that each of the requirement can be met. We now need  a solution that will ensure that all requirements are met at the same time. By substitution a set  of calculations can be performed which meet both requirements and reduce these equations  down to a factor of parameter  $b$   only.
Using equation (4) as a substitute for   $a$   in equation (3) we obtain:
$$
\begin{array}{l}{{c_{N+1}}=3{a_{N}}{X_{N}}^{2}+2{b_{N}}{X_{N}}+{c_{N}}}\\ {{c_{N+1}}=\displaystyle\frac{3(b_{N+1}-b_{N})}{3{X_{N}}}{X_{N}}^{2}+2b_{N}X_{N}+{c_{N}}}\\ {{c_{N+1}}=(b_{N+1}-b_{N})X_{N}+2b_{N}X_{N}+{c_{N}}}\\ {\boxed{c_{N+1}=X_{N}(b_{N+1}+b_{N})+c_{N}}}\end{array}
$$

Using equation (4) as a substitute for   $a$   in equation (1) we get:
$$
\begin{array}{l}{{d_{_{N+1}}=\displaystyle\frac{(b_{_{N+1}}-b_{_{N}})}{3X_{_{N}}}{X_{_{N}}}^{3}+b_{_{N}}{X_{_{N}}}^{2}+c_{_{N}}X_{_{N}}+d_{_{N}}}}\\ {{d_{_{N+1}}=\displaystyle\frac{(b_{_{N+1}}-b_{_{N}})}{3}{X_{_{N}}}^{2}+b_{_{N}}{X_{_{N}}}^{2}+c_{_{N}}X_{_{N}}+d_{_{N}}}}\\ {{c_{_{N}}X_{_{N}}=\displaystyle-\frac{(b_{_{N+1}}-b_{_{N}})}{3}{X_{_{N}}}^{2}-b_{_{N}}{X_{_{N}}}^{2}+d_{_{N+1}}-d_{_{N}}}}\end{array}
$$
$$
\boxed{c_{_{N}}=-X_{_{N}}\frac{(b_{_{N+1}}+2b_{_{N}})}{3}\,+\,\frac{(d_{_{N+1}}-d_{_{N}})}{X_{_{N}}}}
$$

Taking this solution one step further we can substitute equation (6) into equation (5) as  follows:
$$
\begin{array}{l}{{\displaystyle(d_{N+2}-d_{N+1})-X_{N+1}\,{\frac{(b_{N+2}+2b_{N+1})}{3}}=X_{N}\,(b_{N+1}+b_{N})-X_{N}\,{\frac{(b_{N+1}+2b_{N})}{3}}+\displaystyle{\frac{(d_{N+1}-d_{N})}{X_{_N}}}}\\ {{\displaystyle-\,X_{N+1}(b_{N+2}+2b_{N+1})=3X_{N}\,(b_{N+1}+b_{N})-X_{N}\,(b_{N+1}+2b_{N})+3\displaystyle{\frac{(d_{N+1}-d_{N})}{X_{_N}}}-3\displaystyle{\frac{(d_{N+2}-d_{N+1})}{X_{_{N+1}}}}}\\ {{\displaystyle-\,X_{N+1}(b_{N+2}+2b_{N+1})=X_{N}\,(2b_{N+1}+b_{N})+3\displaystyle{\frac{(d_{N+1}-d_{N})}{X_{_N}}}-3\displaystyle{\frac{(d_{N+2}-d_{N+1})}{X_{_{N+1}}}}}\\ {{\displaystyle_{\texttt{X-1}}\quad,\qquad\qquad\texttt{K-2}(d_{N+1}-d_{N})\quad,\quad(d_{N+2}-d_{N+1})\quad\texttt{2}(d_{N+1}-d_{N})\quad,}}\end{array}
$$
$$
X_{N+1}b_{N+2}=-X_{N}(2b_{N+1}+b_{N})-3\frac{(d_{N+1}-d_{N})}{X_{N}}+3\frac{(d_{N+2}-d_{N+1})}{X_{N+1}}-2X_{N+1}b_{N+1}
$$

 ![500](Attachments/500-441.jpg)
# A unique solution

For clarity and ease of illustration, the results of these equations are set out as a table of  related formulas shown below in Table 1.

 ![500](Attachments/500-448.jpg)

It is simple matter to determine the values of parameters   $a,b,c$   and  $d$   at each node  $n$   by using  the formulas set out in the table. Each node (from  $n>2$  ) is directly or indirectly dependent on  the values of previous parameters and can be determined from those previous parameters.  This is an important result, and means that any errors in the calculation early on are replicated  and magnified throughout the analysis. However, the first two occurrences of   $b$   (  $b_{\theta}$   and  $b_{I}$  ) do  not have previous nodes from which to determine their values. In other words the only values  for which we do not have solutions are those for  $b_{\theta}$   and  $b_{I}$  .

Depending on the values assumed for   $b_{\theta}$    and  $b_{I}$  , the result is  usually  an oscillating   $b$   and ever  increasing   $|b|$  . This means that the slope of the spline gets steeper at each tenor as the absolute  value of the first differential increases, so the slope of the curve oscillates.

 ![500](Attachments/500-453.jpg)
Exhibit 5
This systematic wave, shown in Exhibit 5 above, is clearly not the kind of behaviour that is  commonly observed in a yield curve and should therefore not be modelled into the curve.  Furthermore, we have no unique solution at this stage. An infinite number of values can be  assigned to  $b_{\ell}$   and   $b_{I}$   and therefore an infinite number of solutions can be obtained (most of  which exhibit the depicted oscillation effect). So this is still not what we seek.

We need an additional restriction that allows us to find a single solution and which eliminates  the oscillation of the output. The restriction that we put in place is to set the second  differential of the first spline   ${y_{0}}^{\mathrm{,}}$   and last spline   $y_{N}{}^{\mathrm{,,}}$  equal to a constant. We will use a  constant of zero for now, but we come back to this constant at a later stage. Creating this  additional restriction means that we are left with only one unknown, parameter   $b_{2}$  .  This is  demonstrated, using the constant zero, in Table 2 below.

 ![500](Attachments/500-447.jpg)

If we find a value for   $b_{2}$   that results in a final value of zero for   $b_{N}$   then we have a single  solution and this solution should eliminate the oscillation shown above. We can determine  this  solution using two different methods:

  iteration; or

   Gaussian Elimination of a tri-diagonal matrix.

Before we consider each of these solution techniques we consider first the requirement of a  boundary condition in order to obtain a unique solution for a cubic spline. In our discussion  above we ordained a boundary condition of   $b_{\ell}=b_{N}=0$  . In practise two [boundary conditions](../Appendices/Appendix%2021.C%20Solutions%20for%20Black-Scholes%20PDE.md)  have become widely accepted:

# 1. Natural spline

In a natural spline the second differential at  $x_{0}$   and  $x_{N}$   is set to zero.   In other words  $y_{O}\mathrm{{}^{\prime\prime}}={y_{N}}\mathrm{{}^{\prime\prime}}=0$  .
# 2. Clamped spline

In a clamped spline the first differential of the function that produced the nodes and the  first derivative of the spline are set equal. In other words  $y_{0},=f\!\!\left(x_{0}\right),$   and  $y_{N},=f(x_{N})\,\mathrm{,}$  . It is  immediately apparent when we construct a yield curve that we do not have a function that  can be used to replicate the nodes. The first differential of this function is therefore not  available. A reasonable approximation can be used based on the slope of the linear  interpolation function between the first two and the last two nodes.

Although this provides a reasonable approximation in most circumstances it is not always  an appropriate measure. An incorrect choice of boundary values could result in spurious  and oscillating results at the short and/or long end of the curve.

An example using the same input data but different (albeit rather extreme) boundary values is  shown below in Exhibit 6. The natural boundary uses values zero and zero. In the clamped  boundary we have used  $-50$   and  $-50$   as boundary values. Although these boundary values are  extreme, they do illustrate the effect that inappropriate boundary values can have on spline  results.

 ![500](Attachments/500-438.jpg)
Exhibit 6

These results are not unexpected. Readers may question the practical difference between  having a natural boundary condition against having a boundary condition that is obviously  inappropriate. Both approaches may lead to oscillation and an incorrect result. The sole  practical difference is that where we set our own boundary value, however inappropriate, the  extent of the error is under our own control. For this reason users may prefer this approach.

# The solution

We now consider each approach to obtaining the solution.

Iterative solution

A solution for   $b_{I}$   can be obtained by iteration. This “trial-and-error” style approach is  straightforward to understand but is not without its limitations.
When a cubic spline solution is solved by iteration for a single parameter, the degree of  accuracy required is very high. In test solutions the authors found that a higher degree of  accuracy was required for a higher number of nodes. A calculation for fifteen nodes or more  required the solution to be accurate to at least eight decimal places. Even apparently  negligible differences in decimal accuracy can result in strange spline parameters and in turn  produce the same oscillation observed above when no boundary values were set. This is  particularly evident at the long end of the curve as the error becomes compounded by  previous inaccuracies, thus leading to yield curves of limited practical application when  anything longer than the medium-term maturity range is modelled.

A fictional set of numbers have been used to demonstrate this point in Table 3 below. The  “Date” column holds the maturity dates for each rate, while the “Rate” column is of course  the set of [interest rates](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%202/Interest%20Rate%20Quotations.md) for each particular term to maturity.

 ![500](Attachments/500-450.jpg)
Table 3

This data is illustrated graphically at Exhibit 7 below.
 ![500](Attachments/500-446.jpg)
Exhibit7

In Table 3 above, an accuracy of eight decimal places is shown but in fact a much higher level  (over 15 decimal places) of accuracy was required to calculate the results. When we adjust the  level of accuracy, just on parameter   $b_{I}$  , to seven decimal places the results are significantly  flawed, as shown in Table 4 below.

 ![500](Attachments/500-451.jpg)
# Table 4

It can be seen that within the long dates, parameter   $b$   starts to oscillate and grow in an  exponential manner. A graphical representation of the rates as a result of this flawed data is  shown at Exhibit 8 below. Note that the oscillation error is highly pronounced.

 ![500](Attachments/500-449.jpg)
Exhibit 8

The degree of accuracy obtained through iteration is dependent on the starting point for the  first calculation and the number of iterations allowed as a maximum. There is no way of  ensuring that the required degree of accuracy will be obtained without undertaking very high  magnitude (and process intensive) calculations in the iterative algorithm. Without the comfort  of extensive manual review of the results by a person with a clear understanding of the  calculation and its implications, we do not recommend the use of the iteration approach to  derive a solution.

Solving for a system of linear equations by elimination

We now consider again equation (7) derived above, and re-arrange it slightly as (8).
$$
\begin{array}{r}{X_{_{N+1}}b_{_{N+2}}+2(X_{_{N}}+X_{_{N+1}})b_{_{N+1}}+X_{_{N}}b_{_{N}}=-3\frac{(d_{_{N+1}}-d_{_{N}})}{X_{_{N}}}+3\frac{(d_{_{N+2}}-d_{_{N+1}})}{X_{_{N+1}}}}\end{array}
$$

It can be seen that all parameters   $X$   and   $d$   can be obtained by reference to values that are  already known at the nodes. These are in fact node (or time-to-maturity) dependent constants.  In other words we have a system of linear equations from node 1 to  $N.$  . Readers will know that  simultaneous linear equations can be solved by substitution. This method of solving linear  equation can be applied to larger sets of linear equations, although we require increased  processing power.
The [system of equations](A%20Primer%20on%20Probability%20Theory%20and%20Stochastic%20%20Modelling.md) can be represented in a  N -2 by  $N{+}1$   matrix as follows:

 ![500](Attachments/500-442.jpg)

In essence, if you look at the parameters   $b$   for which we are attempting to solve, this can be  laid over the above matrix as follows:

 ![500](Attachments/500-435.jpg)

In other words we are looking for a set of values for   $b_{\theta}$   to  $b_{N}$   that will solve the linear system  for each and every node  $N.$  .

Our basic limitation imposed above is not lifted. We set   $b_{\theta}$    and  $b_{N}$   equal to 0 in order to apply  the natural boundary condition. We can then substitute our solution for equation/row 1 into  equation/row 2. We perform a similar continuous set of substitutions until we have a solution  for  $b_{N-I}$  . This solution can then be substituted backward through the solved equations to obtain  a solution for  $b_{I}$  .

A matrix of this form, that is, an upper and lower triangular quadrant for which no value is  required (observed by the grey shaded area) is also known as a  tri-diagonal matrix . More  advanced methods of solving matrices (and in particular tri-diagonal types) are available. It is  outside the scope of this article to cover these methods in detail; interested readers may wish  to consult Burden and Faires (1997).  For the purposes of illustration however, we have  prepared a simple example solution for a small matrix of values, and this appears as an   Appendix  to this article.

The same values used for the iterative solution were processed using the elimination solution.  The results and their illustrative chart are set out in Table 5 and Exhibit 9 respectively below.
 ![500](Attachments/500-452.jpg)

 ![500](Attachments/500-445.jpg)
Exhibit 9
On first observation these values appear to be identical to those obtained using the iterative  solution. In fact even at the highest level of accuracy possible in our iterative solution we  notice a difference in the values for parameter  c  when we look at the dates 1 Jan 2014  onwards (which appear in the grey boxes in Table 5 above). Although this is not apparent in  the chart, the results in the table where numbers appear with greater accuracy, show these and  other small differences not shown in Exhibit 9.

Based on these results we conclude that the technique of solving for a system of linear  equations is superior to an iterative solution. This is because:

  no starting point for the calculation needs to be determined by the user or the system;

   the accuracy of the solution is not dependent on the number of iterative calculations  performed; and

   the results do not need the same degree of review to assess their accuracy.

This is not to say that this method is flawless. Even a tri-diagonal methodology is reliant on  the degree of precision applied in its calculation. Modern computing hardware and software  has limitations in the size or length of the floating point numbers that it can process. However  if programmed with care, a typical application can deal with significantly large numbers.

# EMPIRICAL PROOF OF PRECISION

In our cubic spline application   $(\mathrm{{CUBED}}^{3})$  ) we have chosen  $\mathrm{C++}$   as the programming language  and we have used the   $\mathrm{C++}$   ‘long double’ variable type to store and process our values. A long  double is usually anything between a 74 and 128 bit place holder, depending on the compiler  and the system on which the calculations are performed. Applying some basic binary  mathematics and allowing 1 bit for sign storage we can calculate:
$$
2^{71}=2{,}361{,}183{,}241{,}434{,}820{,}000{,}000
$$

This should be sufficient to provide an adequate level of accuracy for most cubic spline  calculations required of a zero curve application.  To test this we have performed empirical  testing to corroborate our conclusion using a completely fictitious set of data that was  designed to provide an extreme testing environment and data that is more sensitive to  calculation anomalies than any likely to occur in real life.  Our fake input values were chosen  to include:

  a large number of nodes (over 100);

   high oscillations at various points in the curve; and

   various points of flat data.
A large number of tenors was chosen to compound any rounding errors that might occur as  part of the elimination multiplier. Oscillation at various points in the curve are used to set up  waves that can continue when they subsequently flow into areas of flat data and which would  highlight errors, if they occur. Flat sections of the curve are used so that any errors become  highly visible.

A graph of this extreme test data is set out in Exhibit 10 below:

 ![500](Attachments/500-455.jpg)

# Exhibit 10

The resulting smooth graph after the cubic spline parameter have been calculated and applied  looks as follows:

 ![500](Attachments/500-454.jpg)

# Exhibit 11

Two areas on the graph with relatively flat or consistent data values have been highlighted in  Exhibit 11 as potential areas where calculation error may be observed. These areas of the  graph are isolated and shown at Exhibit 12 and Exhibit 13 below.
 ![500](Attachments/500-433.jpg)
Exhibit 12

In the first area we observe some oscillation. However, this is not oscillation as a result of  calculation errors. This is a smoothing effect that is required to meet the requirements of a  cubic spline and to ensure a smooth curve. The data between points 63 and 71 is consistently  downward sloping but the data then slopes upward again at point 72. The curve starts to  “adapt” at an earlier stage in order to facilitate this change in direction. Therefore this  behaviour is unavoidable, but under most applications for the [spot curve](../../Fixed%20Income%20Asset%20Pricing/Fixed%20Income%20Lecture%20Notes/Teaching%20Note%204%20Interest%20Rate%20Derivatives.md) does not present a  material problem.

 ![500](Attachments/500-439.jpg)
Exhibit 13

The second area of the curve provides another typical cubic spline example as the curve  “adapts” to its new parameters. Once again this is a natural spline phenomenon and not an  error in the calculated values.
Empirical data does not prove beyond a doubt that a [cubic spline method](.md), applied using an  appropriate solution technique and precise software, will always produce accurate results.  Nonetheless we believe that it is reasonable to assume from the test data set out above that the  cubic spline methodology, used in conjunction with appropriate calculation tools, provides  accurate zero curve results in most [fixed income](../../Fixed%20Income%20Asset%20Pricing/Lecture%20Notes%20Bonds,%20%20Preferred%20Stock,%20%20and%20Structured%20Products.md) market conditions.

# A LOOK AT FORWARD RATES

Previous literature has highlighted the use of the cubic spline approach to model forward  curves, and its limitations. Certainly a cubic spline discussion would be incomplete without a  look at its application to forward rates. We will use our empirical data to highlight typical  [forward rate](../../Clippings/Forward%20Points%20in%20Currency.md) behaviour under the cubic spline technique. Our sample data does not reflect  actual market conditions and is an extreme data set, to say the least. However, it does  highlight a point with regards to forward rates that can often be observed sometimes under  normal market conditions. To this end we isolate the last sub-set of the data, as shown above,  and plot the forward rates for that data set.

 ![500](Attachments/500-443.jpg)
Exhibit 14

From data that was interpolated using the linear method versus data interpolated using the  cubic spline, a comparison of [forwards](../../Financial%20Markets/Financial%20Asset%20Pricing%20Theory%20Overview/Chapter%2012%20-%20Derivatives/Forwards%20and%20Futures.md) shows how the [forwards](../../Financial%20Markets/Financial%20Asset%20Pricing%20Theory%20Overview/Chapter%2012%20-%20Derivatives/Forwards%20and%20Futures.md) in a cubic spline environment  can oscillate. As expected, the relatively minor oscillations observed first in the zero rates  curve are compounded excessively in the [forward rate](../../Clippings/Forward%20Points%20in%20Currency.md) calculation. The linear interpolation  approach, shown for comparison purposes at Exhibit X, eliminates much of the oscillation but  of course is not a smooth curve, which is as undesirable. The user is confronted with the need  to balance the conflicting requirements; a trade-off is called for and for most practical  applications the cubic spline approach and its smoothing results is preferred. It remains  important however that the user reviews cubic spline data by looking at both the zero and  forward rates.

Using the actual United Kingdom 10-year zero curve for 2 January 2000, the forward rates  have been calculated using cubic spline and linear interpolation and compared in Exhibit 15  and Exhibit 16 respectively below. There is no observed reason to favour the latter approach  over the former.
 ![500](Attachments/500-454.jpg)
Exhibit 15

 ![500](Attachments/500-462.jpg)
Exhibit 16

Improvements to the basic approach

As a result of the drawback when fitting the forward curve,  the basic technique has been  improved to remove the oscillation effect at longer maturities. As we saw from the test results  presented earlier, the oscillation of a spline is partly a function of the number of nodes used.  The paradox with this factor is that in practice, at very long maturities the forward (and also  the spot) curve would be expected to be reasonably flat. To remove the oscillation, as  described first by Fisher, Nychka and Zervos (1995), this involves the addition of a  roughness  penalty  when minimising the sums of squares.  Waggoner (1997) introduced a  variable  roughness penalty , which enabled the approach to retain the flexibility at the short end and  reduce oscillation at the long end.  Using the Waggoner approach enables users to retain the  flexibility and ease of the cubic spline approach as well as a more realistic forward curve.  Anderson and Sleath (1999) state that the advantage of the spline approach over parametric  methods is that separate segments of the spline can be adjusted independently of each other.   The significance of this is that a change in market levels at one of the [term structure](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%209/The%20Vasicek%20Model.md) will not  affect significantly at other parts of the curve. This is a drawback of the parametric methods.  Ironically Anderson and Sleath modify the Waggoner model in a way that would appear to  incorporate elements of the parametric approach, and their results appear to improve on the  earlier works.
# CONCLUSION

The purpose of this paper has been to present an accessible account of how the cubic spline  methodology of [term structure](../../Financial%20Markets/Fixed%20Income%20Securities%20Tools%20for%20Today's%20Markets/Chapter%209/The%20Vasicek%20Model.md) estimation could be implemented by users involved in any area  of the debt capital markets. The technique is straightforward and quick, and is valid for a  number of applications, most of which are “normal” or conventional yield curves. For  example users are recommended to use it when curves are positively sloping, or when the  long end of the curve is not downward sloping. The existence of humps along the short or  medium terms of the curve can cause excessive oscillation in the forward curve but the zero  curve may still be used for valuation or relative value purposes.

Oscillation is a natural effect of the cubic spline methodology and its existence does not  impair its effectiveness under many conditions. If observed rates produce very humped  curves, the fitted zero-curve using cubic spline does not produce usable results. For policy  making purposes, for example as used in central banks, and also for certain  market valuation  purposes, users require forward rates with minimal oscillation.  In such cases however the  Waggoner or Anderson-Sleath models will overcome this problem. We therefore recommend  the cubic spline approach under most market conditions.
# APPENDIX

Example matrix solution based on Gaussian elimination.

We will solve for the following values (where the values of   $X$   have already been calculated).

 ![500](Attachments/500-436.jpg)

Firstly we construct our matrix as follows.

 ![500](Attachments/500-444.jpg)

Where  $b_{I}$   is set to zero this provides the values.

 ![500](Attachments/500-437.jpg)

In turn we can substitute row 1 into row 2 to obtain.

 ![500](Attachments/500-434.jpg)

Similar substitutions, and the fact that  $b_{7}$   is constrained as zero, yield the matrix below.
 ![500](Attachments/500-461.jpg)

This means that we can solve for  $b_{6}$  . Once we have a solution for  $b_{6}\mathrm{We}$   can solve for  $b_{5}$    and so  on. As a final result we get the following values for parameter  $b$  .

 ![500](Attachments/500-454.jpg)

Parameters  $a$   and  $c$   can be determined directly from the values of   $b$   above.
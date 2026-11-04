# Separable CQC violations for every MUB pair in all qubit–qudit dimensions n ≥ 4

Working theorem and complete proof, 1 November 2026. This document is an intermediate research artifact for the parent agent. It does **not** claim the unresolved 2×3 CQC conjecture is settled. Its substantive improvement over Qian arXiv:2608.14806v2 is a universal statement over **every** prescribed MUB pair, where Qian's Theorem 4.1 establishes that quantifier only for n ≥ 164. Existing existential counterexamples in dimensions n ≥ 4 are prior art.

## 1. Definitions

Use natural logarithms. For a bipartite density operator ρ define

\[
G(\rho)=I(A:B)_\rho-I(Q_A:Q_B)_\rho-I(R_A:R_B)_\rho.
\]

The CQC inequality is G(ρ) ≥ 0. On Alice the prescribed two mutually unbiased qubit bases can, after a local unitary and outcome relabellings, be represented by Pauli Z and X. On Bob, Q and R are any prescribed rank-one projective MUBs of dimension n.

### Main theorem

For every integer n ≥ 4 and **every** ordered pair of rank-one projective MUBs on C^n, there exists a separable state on C²⊗C^n with G(ρ) < 0. There also exist full-rank separable states with the same property for the same prescribed measurement bases.

For every n ≥ 4 a construction with the dimension-independent parameters r = 1/3 and t = 1/100 works. It has rank four and satisfies the explicit conservative bound

\[
G(\rho)<-\frac{17117}{114\,750\,000\,000}\quad\text{nats}.
\]

For n = 4 there is also a rank-two separable construction for every MUB pair.

## 2. Binary projective compression

Choose arbitrary vectors q₀∈Q and r₀∈R. Adjust the physically irrelevant phase of r₀ so that ⟨q₀,r₀⟩ = n^{-1/2}. Let

\[
W=\operatorname{span}\{q_0,r_0\},\qquad P=P_W,
\]

and regard W as a qubit. On W define the two traceless Hermitian involutions

\[
B_1=2|q_0\rangle\langle q_0|-P,\qquad
B_2=P-2|r_0\rangle\langle r_0|.
\]

Their Bloch overlap is

\[
c=\frac12\operatorname{Tr}_W(B_1B_2)=1-\frac2n.
\]

Every Q basis vector except q₀ has its projection into W parallel to the line W∩q₀^⊥. Therefore Q, restricted to states supported in W, is exactly a projective measurement of B₁ followed by random subdivision of the outcome corresponding to W∩q₀^⊥. The subdivision distribution is independent of Alice and of the input state. Conversely, the binary B₁ outcome is a deterministic function of the fine Q outcome. It follows that, for every joint state supported in C²⊗W,

\[
I(Z_A:Q_B)=I(Z_A:B_1).
\]

The same argument for R gives I(X_A:R_B) = I(X_A:B₂); the sign choice in B₂ only relabels its binary outcomes. No invariance of W under any Fourier transform is assumed or needed.

This compression is already implicit and explicitly stated at the frame level in Qian, Proposition 6.9. The new ingredient below is a different state family exploiting the entropy curvature of the compressed two-qubit problem.

## 3. A general curvature mechanism for two binary measurements

Let B₁,B₂ be arbitrary traceless qubit involutions with

\[
c=\frac12\operatorname{Tr}(B_1B_2)\in[0,1].
\]

The sign of either observable can be changed without changing mutual information, so the nonnegative overlap covers |c|.

Define

\[
U=\frac{X+Z}{\sqrt2},\quad V=\frac{Z-X}{\sqrt2},\quad
\alpha_r=\frac{I+rU}{2},\quad
\sigma_r=\alpha_r\otimes\frac I2,
\]

\[
\delta=\frac14(Z\otimes B_1-X\otimes B_2),\qquad
\rho_{r,t}=\sigma_r+t\delta.
\]

Both partial traces of δ vanish, so the marginals of ρ_{r,t} are fixed. Separability is explicit. Write Π_{j,b}=(I+bB_j)/2 for b=±1. Then

\[
\rho_{r,t}=\frac14\sum_{b=\pm1}\left[
(\alpha_r+btZ)\otimes\Pi_{1,b}
+(\alpha_r-btX)\otimes\Pi_{2,b}\right].
\tag{S}
\]

Each Alice factor in (S) has trace one and a Bloch vector of norm at most r+2|t|. Thus (S) is a convex decomposition into four product density operators whenever r+2|t|≤1. Embedding Bob's qubit into W preserves this decomposition, with Π_{j,b}=(P+bB_j)/2. No PPT sufficiency theorem is needed.

As a redundant check, ρ_{r,t}^{T_A}=ρ_{r,t}, because all Alice factors I,X,Z are real symmetric.

Because \|δ\|≤1/2, positivity follows whenever

\[
|t|<\frac{1-r}{2}.
\]

For 0≤c<1 define orthogonal Bob Pauli observables

\[
C=\frac{B_1-B_2}{\sqrt{2(1-c)}},\qquad
D=\frac{B_1+B_2}{\sqrt{2(1+c)}}.
\]

Then

\[
4\rho_{r,t}=I+rU\otimes I+
t\sqrt{1-c}\,U\otimes C+
t\sqrt{1+c}\,V\otimes D.
\]

The four eigenvalues are explicitly

\[
\lambda_{\eta,\xi}
=\frac{1+\eta t\sqrt{1-c}+\xi\sqrt{r^2+(1+c)t^2}}4,
\qquad\eta,\xi\in\{-1,1\}.
\]

Indeed U⊗C commutes with both U⊗I and V⊗D, while the latter two anticommute. The displayed spectrum also extends continuously to c=1.

The two binary classical tables, after an outcome relabelling, coincide and have cells

\[
p_{ab}(t)=\frac{1+a r/\sqrt2+abt}{4},\qquad a,b\in\{-1,1\}.
\]

Thus the gap is an explicit one-variable entropy expression. If h(p)=−p log p−(1−p)log(1−p), then

\[
G(r,c,t)=h\!\left(\frac{1+r}{2}\right)+\log2
-H\bigl(\{\lambda_{\eta,\xi}\}\bigr)
-2h\!\left(\frac{1+r/\sqrt2}{2}\right)
+h\!\left(\frac{1+r/\sqrt2+t}{2}\right)
+h\!\left(\frac{1+r/\sqrt2-t}{2}\right).
\]

### Exact second derivative

The gap is even in t. One proof is to conjugate Bob by a Pauli observable perpendicular to both B₁ and B₂, which sends t to −t while preserving the marginal and exchanging the two outcomes of each Bob measurement. In particular G(0)=G′(0)=G‴(0)=0.

The exact Hessian is

\[
Q(r,c):=\left.\frac{\partial^2G(r,c,t)}{\partial t^2}\right|_{t=0}
=\frac{1-c}{1-r^2}+(1+c)\frac{\operatorname{arctanh}r}{r}
-\frac{2}{1-r^2/2}.
\tag{1}
\]

Here arctanh(r)/r is interpreted as 1 at r=0.

To verify (1) independently of differentiating the eigenvalues, use the Hessian of quantum relative entropy:

\[
\frac{d^2}{dt^2}D(\sigma_r+t\delta\Vert\sigma_r)\big|_0
=\operatorname{Tr}\delta\,\Omega_{\sigma_r}^{-1}(\delta).
\]

On the Alice eigenbasis of U, the diagonal inverse logarithmic mean gives
Tr[UΩ_{α_r}^{−1}(U)] = 4/(1−r²), while the off-diagonal part gives
Tr[VΩ_{α_r}^{−1}(V)] = 4 arctanh(r)/r. Since the Bob marginal is I/2, Ω_{σ_r}^{−1} contributes an additional factor 2. The two Bob factors B₁−B₂ and B₁+B₂ have squared Hilbert–Schmidt norms 4(1−c) and 4(1+c). Combining them with the factor 1/(4√2) in δ gives the first two terms of (1). Each classical mutual information has second derivative 1/(1−r²/2), giving the last term.

Expansion at r=0 gives

\[
Q(r,c)=\frac{1-2c}{3}\,r^2+O(r^4).
\tag{2}
\]

Hence **every binary compression with |c|>1/2 produces separable CQC violations arbitrarily close to a product state**: choose sufficiently small fixed r>0, and then sufficiently small nonzero t.

The threshold is exact within this second-variation family. Indeed, for |r|<1,

\[
Q(r,c)=\sum_{k\ge1}\left[(1-c)+\frac{1+c}{2k+1}-2^{1-k}\right]r^{2k}.
\]

At c=1/2 the k=1 coefficient is zero and every coefficient for k≥2 is strictly positive: it equals 1/2+3/[2(2k+1)]−2^{1−k}. Every coefficient decreases with c. Hence Q(r,c)≥0 for every r∈[0,1) if and only if c≤1/2. This is an exact classification of when the displayed family has a negative product-state Hessian.

It is a sufficient geometric criterion for global CQC failure. We have not established that c≤1/2 is sufficient for a global CQC inequality over every two-qubit state; that separate claim must not be inferred from the family-level classification.

## 4. Uniform exact witness for every n ≥ 5 and every MUB pair

For n≥5 the compression in Section 2 gives c=1−2/n≥3/5. Set r=1/3. Formula (1) becomes

\[
Q(1/3,c)=\frac98(1-c)+\frac32(1+c)\log2-\frac{36}{17}.
\]

It decreases with c, because (3/2)log2 < 9/8. Thus

\[
Q(1/3,c)\le Q(1/3,3/5)
=\frac{12}{5}\log2-\frac{567}{340}.
\]

An entirely rational estimate suffices. From the arctanh series,

\[
\log2=2\sum_{k\ge0}\frac{1}{(2k+1)3^{2k+1}}
<\frac23+\frac{2}{81}+\frac{1}{540}
=\frac{1123}{1620}<\frac{25}{36}.
\]

The tail bound used here is
2Σ_{k≥2}3^{−(2k+1)}/(2k+1) ≤ (2/5)Σ_{k≥2}3^{−(2k+1)} = 1/540; it is strict because not all denominators equal 5. Therefore

\[
Q(1/3,c)<-\frac{181}{45900}<-\frac1{1020}.
\tag{3}
\]

### A finite t requiring no numerical logarithm evaluation

We now take t=1/100 and prove a strict negative gap by a fourth-derivative bound.

For |s|≤1/12,

\[
\lambda_{\min}(\rho_{1/3,s})\ge\frac16-\frac{|s|}{2}\ge\frac18.
\]

For our perturbation,

\[
\|\delta\|_F^2=\frac12,\qquad
\|\delta\|^2=\frac{1+\sqrt{1-c^2}}8\le\frac9{40}
\quad(c\ge3/5).
\]

Let f(s)=Tr[ρ_{1/3,s}logρ_{1/3,s}] on the four-dimensional support. The resolvent formula gives

\[
f^{(4)}(s)=6\int_0^\infty
\operatorname{Tr}\bigl[(\delta(\rho_{1/3,s}+uI)^{-1})^4\bigr]\,du.
\]

Writing the trace with the Hermitian conjugate
(ρ+uI)^{-1/2}δ(ρ+uI)^{-1/2} and using Tr A⁴≤\|A\|²\|A\|_F² yields

\[
0\le f^{(4)}(s)
\le \frac{2\|\delta\|^2\|\delta\|_F^2}
{\lambda_{\min}(\rho_{1/3,s})^3}
\le\frac{576}{5}.
\]

Both classical mutual informations J(s) are even, and their fourth derivatives are nonnegative: their marginals are fixed and each nonconstant cell contributes
(p log p)^{(4)} = 2(p′)^4/p³ ≥0. Therefore J(s)≥J″(0)s²/2. The quantum term is also even, so Taylor's theorem and (3) give

\[
G(1/3,c,t)
< -\frac{181t^2}{91800}+\frac{24}{5}t^4.
\]

At t=1/100 this is

\[
G(\rho)<-\frac{17117}{114\,750\,000\,000}<0.
\]

All inputs are exact. The small bound is deliberately conservative; no floating point optimisation or entropy computation is a premise.

The witness written directly on C²⊗C^n is

\[
\boxed{\displaystyle
\rho=\frac14\left[
\left(I+\frac{X+Z}{3\sqrt2}\right)\otimes P
+\frac1{100}(Z\otimes B_1-X\otimes B_2)
\right].}
\]

It is positive of rank four on C²⊗W, has trace one, is separable, and violates CQC for the original full measurement tables by Section 2.

## 5. Every MUB pair in dimension four

By the known classification of 4×4 complex Hadamard matrices, any prescribed MUB pair is, up to simultaneous unitary conjugation, basis-vector phases, and outcome permutations, the computational basis and the columns of

\[
H(a)=\frac12\begin{pmatrix}
1&1&1&1\\
1&a&-1&-a\\
1&-1&1&-1\\
1&-a&-1&a
\end{pmatrix},\qquad |a|=1.
\]

Take

\[
u=\frac{(1,0,1,0)^T}{\sqrt2},\qquad
v=\frac{(0,1,0,-1)^T}{\sqrt2}.
\]

Their computational supports are disjoint. Also

\[
H(a)^*u=\frac{(1,0,1,0)^T}{\sqrt2},\qquad
H(a)^*v=\frac{(0,\bar a,0,-\bar a)^T}{\sqrt2},
\]

so their second-basis supports are disjoint as well. Thus both Bob measurements identify perfectly which of u and v was prepared.

The established double-readout state

\[
\tau=\frac12|0,u\rangle\langle0,u|
+\frac12|+,v\rangle\langle+,v|
\]

is separable of rank two. Its excess is independent of a:

\[
-G(\tau)
=2h(3/4)-\log2-h\!\left(\frac{1+1/\sqrt2}{2}\right)
\approx0.0150275779779839>0.
\]

The strict sign is also supplied in Qian's exact double-readout computation (Appendix A.3, equations (69)–(70)). Alternatively one can use the uniform construction from Section 4 with this compressed pair B₁=B₂ (c=1), avoiding a separate entropy-sign evaluation entirely. The latter gives a rank-four witness with the same conservative gap bound. Transforming back through the known equivalences proves the universal statement for the originally prescribed MUB pair.

## 6. Full rank and scope

For either witness ρ, let

\[
\rho_\varepsilon=(1-\varepsilon)\rho+\varepsilon\frac{I_{2n}}{2n}.
\]

This is full rank and separable for every ε∈(0,1). The fixed finite-dimensional von Neumann and classical entropies are continuous, so G(ρ_ε)<0 for all sufficiently small ε>0. This step does not claim a dimension-independent allowable noise fraction.

The theorem covers every prescribed MUB pair for n≥4. It does not settle global CQC at 2×3. At n=3 the two-vector compression has c=1/3, and the above curvature mechanism is nonnegative for small r; this is a limitation of the construction, not a proof of the remaining conjecture.

## 7. Sources inspected and bounded novelty status

1. Lilong Qian, *Separable Counterexamples to Complementary Quantum Correlations, and Why Random Search Missed Them*, arXiv:2608.14806v2, 19 August 2026, 29 pages. Official PDF https://arxiv.org/pdf/2608.14806 inspected. Theorem 4.1, p. 4 gives the universal-over-MUB-pairs result only for n≥164; Theorem 5.1 gives existential choices below that; Proposition 6.9, p. 9 gives the two-vector compression; §7 gives numerical 2×5 product-anchor violations; §11 retains 2×3 as the global open case. Web references available to parent: turn138view0, turn138view2, turn138view3.
2. Wojciech Tadej and Karol Życzkowski, *A concise guide to complex Hadamard matrices*, Open Systems & Information Dynamics 13 (2006), 133–177, doi:10.1007/s11080-006-8220-2. arXiv:quant-ph/0512154v2 https://arxiv.org/pdf/quant-ph/0512154 inspected. Section 5.4, pp. 17–18 of the preprint, equations (62)–(65), states the exhaustive order-four family. It attributes the classification to Haagerup. Web references turn143view0 and turn144view0.
3. An earlier derivation used the standard 2×2 PPT criterion. The explicit decomposition (S) eliminates this external dependency completely.

Bounded search on 1 November 2026 has not identified a later universal-all-MUB n≥4 or n≥5 statement, or the exact curvature family (1). The two-vector compression itself is prior art, and the four-dimensional Hadamard classification is classical. The apparent residual contribution is the explicit mixed separable perturbation, its sharp small-r curvature threshold c>1/2, and the universal prescribed-basis conclusion. This needs the parent's independent algebraic review and final novelty search; no categorical priority claim is made here.

# Every prescribed MUB pair fails CQC when both dimensions are at least three

Companion elementary extension to `all_mub_theorem.md`, 1 November 2026. Existing existential CQC failures at m,n≥3 are prior art. The residual claims here are universality over every prescribed pair of local MUBs and a dimension-independent lower bound on the excess.

## Theorem

Let m,n≥3. For any prescribed rank-one projective MUB pair (Q_A,R_A) on C^m and any prescribed such pair (Q_B,R_B) on C^n, there is a separable rank-two state ρ satisfying

\[
I(Q_A:Q_B)+I(R_A:R_B)-I(A:B)_\rho
\ge\frac1{2\pi^4}>0.
\]

There are also full-rank separable states with strictly positive excess for the same prescribed bases.

## Proof

On a local space C^d, d≥3, choose three distinct vectors q₀,q₁,q₂ from Q. Let u=q₀ and

\[
v_\theta=\frac{q_1+e^{i\theta}q_2}{\sqrt2}.
\]

The R measurement on u has the uniform law p(k)=1/d. Mutual unbiasedness gives phases z_k of modulus one for which the R law on v_θ is

\[
q_\theta(k)=\frac{1+\operatorname{Re}(e^{i\theta}z_k)}d.
\]

Consequently

\[
\frac1{2\pi}\int_0^{2\pi}\|q_\theta-p\|_1\,d\theta
=\frac1d\sum_{k=0}^{d-1}\frac1{2\pi}\int_0^{2\pi}
|\operatorname{Re}(e^{i\theta}z_k)|\,d\theta
=\frac2\pi.
\]

Choose θ attaining at least this average. Perform this choice independently on Alice and Bob, and set

\[
\rho=\frac12|u_Au_B\rangle\langle u_Au_B|
+\frac12|v_Av_B\rangle\langle v_Av_B|.
\]

The two product rays are locally orthogonal. Therefore ρ and both marginals have nonzero spectrum (1/2,1/2), giving I(A:B)=log2. Each Q measurement identifies the latent mixture label exactly, and conditional on that label the local outcomes are independent. Hence I(Q_A:Q_B)=log2 as well. The entire excess is the mutual information of the R outcomes.

Write p_A,p_B for their conditional uniform laws and q_A,q_B for their other conditional laws. Their joint distribution and product of marginals obey

\[
P=\frac12p_A\otimes p_B+\frac12q_A\otimes q_B,
\]

\[
P-P_A\otimes P_B
=\frac14(p_A-q_A)\otimes(p_B-q_B).
\]

Thus

\[
\|P-P_A\otimes P_B\|_1
=\frac14\|p_A-q_A\|_1\|p_B-q_B\|_1
\ge\frac1{\pi^2}.
\]

Pinsker's inequality with natural logarithms gives

\[
I(R_A:R_B)=D(P\Vert P_A\otimes P_B)
\ge\frac12\|P-P_A\otimes P_B\|_1^2
\ge\frac1{2\pi^4}.
\]

For completeness, the needed form of Pinsker follows by coarsening the distributions into the event {P>Q} and its complement, using the log-sum inequality. If a−b=\|P−Q\|₁/2, the resulting binary relative entropy is at least 2(a−b)²: its second derivative in a is 1/[a(1−a)]≥4 and its value and first derivative vanish at a=b.

Finally mix ρ with sufficiently little maximally mixed noise. Convexity preserves separability, the noise supplies full rank, and continuity preserves a strictly positive excess. ∎

## A finite choice without phase optimisation

Because |Re z|+|Im z|≥1 for |z|=1, one of θ=0 or θ=π/2 already gives \|q_θ−p\|₁≥1/2. Restricting each party to these two choices produces the fully finite constructive lower bound

\[
I(Q_A:Q_B)+I(R_A:R_B)-I(A:B)\ge\frac1{512}.
\]

The averaging construction gives the stronger 1/(2π⁴) bound; the two-choice version avoids optimisation altogether.

## Relation to inspected prior art

Qian arXiv:2608.14806v2, Theorem 3.1, gives the same basic locally orthogonal classical-label mechanism for canonical computational/Fourier pairs, with the fixed two-spoke vector (q₁+q₂)/√2 and lower bound 1/(8m²n²). The phase-averaging adjustment above works for arbitrary prescribed MUBs and gives a dimension-independent bound. It is an elementary extension of that mechanism, not a new original refutation of CQC. Its novelty should be stated with that limitation.

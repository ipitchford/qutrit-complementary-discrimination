# Proof outline: sharp discrimination and prescribed-basis counterexamples

**Track I — informal and computer-assisted mathematics.** This outline concerns the integrated draft in `paper/manuscript.tex` and `paper/sections/correlation.tex`, inspected on 1 November 2026. It explains the existing argument without changing either source.

## Statement

The paper proves a sharp distinguishability inequality for two orthogonal qutrit signal states, and separate counterexample theorems for complementary quantum correlations. The two parts have different quantifiers and different proof methods.

**Sharp qutrit discrimination, Theorem 2.1.** If $Q,R$ are mutually unbiased orthonormal bases of $\mathbb C^3$, and $u,v$ are orthonormal, then

\[
\mathcal S_{Q,R}(u,v):=
\sum_j\frac{(|\langle q_j,u\rangle|^2-|\langle q_j,v\rangle|^2)^2}
{|\langle q_j,u\rangle|^2+|\langle q_j,v\rangle|^2}
+\sum_k\frac{(|\langle r_k,u\rangle|^2-|\langle r_k,v\rangle|^2)^2}
{|\langle r_k,u\rangle|^2+|\langle r_k,v\rangle|^2}
\le\frac83,
\]

where a zero-denominator summand is zero. Equality holds exactly when, for some $j,k$,

\[
W=\operatorname{span}(u,v)=\operatorname{span}(q_j,r_k),\qquad
P_u-P_v=\pm\sqrt{3/2}\,(P_{q_j}-P_{r_k}).
\]

For the computational/Fourier pair, the nine complementary rays are cyclic permutations of $(0,1,-\omega^k)/\sqrt2$, $k=0,1,2$. Corollary 2.2 gives an exact classical-to-quantum Fisher-information ratio of at most $2/3$, specifically at the equal mixture of the two fixed orthogonal states, with the randomly chosen setting retained. Corollary 3.3 gives the lower bound $0.100496952115340\ldots$ nats for the explicitly stated equal-prior orthogonal two-ray CQC family.

**Every prescribed qubit–qudit measurement pair, Theorem 4.1.** For every $n\ge4$, every prescribed ordered qubit MUB pair, and every prescribed ordered MUB pair on $\mathbb C^n$, there exists a separable rank-four state satisfying

\[
G:=I(A:B)-I(Q_A:Q_B)-I(R_A:R_B)
<-\frac{9}{20000000}
\quad(\text{revised; the earlier constant }-17117/114750000000\text{ also follows}).
\]

The state may depend on the prescribed measurements. Full-rank separable violations also exist for those same measurements, with sufficiently small maximally mixed noise; a noise tolerance uniform in dimension is not claimed.

**Higher local dimensions, Theorem 4.5.** For every $m,n\ge3$ and every prescribed local MUB pair on each party, a rank-two separable state, diagonal in a local product basis, has CQC excess at least $1/(2\pi^4)$ nats. Full-rank separable violations follow by continuity.

These are not proofs of the full $2\times3$ CQC conjecture. Proposition 4.3 establishes an exact sign threshold $c>1/2$ for the Hessian of its displayed product-state family; it does not establish global CQC positivity for arbitrary states when $c\le1/2$, or even positivity for every admissible $t$ within that family.

## Idea

The qutrit part compresses the two measurements to a two-dimensional support, where their distinguishability is a quadratic form on a three-dimensional real Bloch space. A trace identity reduces the sharp bound to the sign of one determinant. Clearing its denominators produces a degree-twelve polynomial whose global nonnegativity is certified by four exact positive rational Gram matrices; sparse zero-set witnesses then turn the certificate into a complete equality classification. The counterexample part uses the same support compression differently: the restricted measurements become binary observables with overlap $c=1-2/n$. A separable perturbation of a product state has negative CQC curvature exactly when $c>1/2$; a fourth-derivative estimate converts that local sign into one finite witness for all $n\ge5$, and an order-four Hadamard argument handles $n=4$. For both local dimensions at least three, phase averaging strengthens the existing shared-classical-label mechanism to every prescribed basis pair.

## Outline

1. **[standard] Normalize the qutrit basis pair.** Every order-three complex Hadamard matrix is equivalent to $F_3$, so proving the computational/Fourier case proves the arbitrary-MUB statement. **Location:** §2, immediately after Theorem 2.1; cited Tadej–Życzkowski classification.

2. **[standard] Replace orthogonal state pairs by a Bloch quadratic form.** For fixed $W$, the state differences are exactly the traceless Hermitians with squared Hilbert–Schmidt norm two, so $\max\mathcal S=2\lambda_{\max}(A_W)$. The polarized identity gives $A_W\succeq0$, $\operatorname{Tr}A_W=2$, and the determinant criterion. **Location:** Lemma 3.1 and equations (3.2)–(3.3); this reduction is attributed to Qian.

3. **[routine] Encode the determinant as a rational polynomial.** The coordinates $w=(r,a+i\sqrt3b,c+i\sqrt3d)$ keep the Fourier calculations rational after expansion. Principal minors of the six-vector Gram matrix give the degree-twelve polynomial $\mathcal P$, with the exact positive-factor identity (3.8). **Location:** §3.2, equations (3.4)–(3.9); exact polynomial divisions are checked by the verifier.

4. **[the point] Prove global polynomial nonnegativity with a rational certificate.** The identity $\mathcal P=\sum b_j^TG_jb_j$ is verified coefficient by coefficient. Rational LDL checks and entrywise perturbation bounds prove $G_j\succeq207I/1000$. **Location:** Lemma 3.2, the JSON proof supplement, and `verify_qutrit_sos.py`. This is the main load-bearing computational step; the large certificate is an essential part of the proof.

5. **[routine] Restore the exceptional planes.** Zero denominators occur at six measurement rays, and each original discrimination summand extends continuously there. **Location:** paragraph following Lemma 3.2. The later explicit spectrum $(1,1/2,1/2)$ also shows these planes are strict for the sharp bound.

6. **[the point] Extract all equality cases from the certificate's kernel.** Strict Gram positivity forces all sextic components to vanish. Six exact membership identities imply $h_1=h_2=h_3=0$; in a nonzero-coordinate chart, their roots are only the computational/Fourier rays and the nine Hesse rays. The principal eigendirection then fixes $P_u-P_v$, rather than merely its support. **Location:** §3.4, equation (3.11) and the equality-witness data.

7. **[routine] Translate the sharp bound into its stated consequences.** Direct differentiation gives classical Fisher information $\mathcal S/4$ at the equal mixture and quantum Fisher information one. Substitution into Qian's entropy envelope gives the restricted two-ray gap. **Location:** Corollaries 2.2 and 3.3. Neither consequence broadens the state family to arbitrary $2\times3$ states.

8. **[standard] Compress an arbitrary qudit MUB pair to binary readouts.** On $W=\operatorname{span}(q_0,r_0)$, every other projected vector in each basis lies on one complementary ray. The fine outcomes are fixed subdivisions of a binary projective outcome, preserving mutual information, with overlap $c=1-2/n$. **Location:** Lemma 4.2, equations (4.3)–(4.5); the support geometry is attributed to Qian's Proposition 6.9.

9. **[the point] Choose a perturbation with an explicit separable decomposition.** The family $\rho_{r,t}=\alpha_r\otimes I/2+t(Z\otimes B_1-X\otimes B_2)/4$ has fixed marginals and is separable whenever $r+2|t|\le1$. Its four-product decomposition removes any need to infer separability merely from a numerical spectrum. **Location:** Proposition 4.3, equations (4.7)–(4.10).

10. **[the point] Compute the exact local threshold.** The two classical tables and the Kubo–Mori Hessian give

    \[
    Q(r,c)=\frac{1-c}{1-r^2}+(1+c)\frac{\operatorname{arctanh}r}{r}
    -\frac2{1-r^2/2}.
    \]

    Its $r^2$ coefficient is $(1-2c)/3$; the remaining coefficient argument proves that a negative value exists exactly for $c>1/2$. **Location:** Proposition 4.3, equations (4.9), (4.12)–(4.13). This is a family-level second-variation theorem.

11. **[the point] Turn local negativity into a uniform finite violation.** At $r=1/3$ and $c\ge3/5$, a rational upper bound on $\log 2$ gives $Q<-181/45900$. Positivity along $|s|\le1/12$, a resolvent fourth-derivative estimate, and nonnegative classical fourth derivatives yield a quartic remainder bound. Taking $t=1/100$ gives the exact rational margin. **Location:** Lemma 4.4, equations (4.15)–(4.20). The parameters simultaneously satisfy negative curvature, separability, and the remainder estimate.

12. **[the point] Cover all prescribed pairs from dimension four upward.** For $n\ge5$, compression gives $c\ge3/5$. For $n=4$, the exhaustive Hadamard normal form supplies two vectors with disjoint supports in both measurements, giving $c=1$. **Location:** proof of Theorem 4.1, equations (4.21)–(4.22). This case split is necessary: the generic two-ray compression would give only $c=1/2$ at $n=4$.

13. **[standard] Obtain full-rank separable violations.** Mix the supported separable witness with sufficiently little maximally mixed noise and use continuity of finite-dimensional entropy. **Location:** final paragraph of the proof of Theorem 4.1 and the corresponding paragraph of Theorem 4.5. The finite rank-four margin and the full-rank existence assertion are separate claims.

14. **[the point] Choose phases that work for any higher-dimensional MUB pair.** The $R$-outcome law of a two-coordinate superposition differs from the uniform law by $\operatorname{Re}(e^{i\theta}z_k)/d$. Its phase-averaged $\ell_1$ distance is $2/\pi$, independent of the prescribed basis pair and dimension. **Location:** proof of Theorem 4.5, equation (4.24). This is an extension of the existing classical-bit mechanism, not a separate discovery of CQC failure.

15. **[standard] Convert retained classical correlation into a quantitative excess.** The first setting already reads the latent bit completely. The second joint law differs from the product of its marginals by one quarter of an outer product; Pinsker's inequality then gives the excess $1/(2\pi^4)$. **Location:** remainder of Theorem 4.5, with a short proof of the required Pinsker inequality supplied immediately afterward.

## New components

- **The exact qutrit positivity certificate.** It proves a fixed sharp inequality already conjectured in the source. Its statement is deliberately specific; the polynomial derivation and verification strategy are reusable, while the numerical entries are not a general-purpose lemma.
- **The complete equality argument.** The six small polynomial witnesses turn a large positivity certificate into a finite algebraic classification. This technique—strict Gram positivity plus explicit ideal-membership witnesses—is reusable beyond this example; the particular sextics encode these fifteen cleared-polynomial zero rays.
- **The explicit separable curvature family.** Proposition 4.3 is stated for arbitrary binary overlap $c\in[0,1]$, not only the values $1-2/n$ used later. That generality exposes the mechanism and makes the threshold quotable separately.
- **The uniform finite witness.** Lemma 4.4 makes the local argument quantitative and supplies a single pair $r=1/3,t=1/100$ throughout the required overlap interval. Its fourth-derivative control is more reusable than the conservative final rational constant.
- **The stronger prescribed-basis quantifier.** Theorem 4.1 combines known compression/classification results with the new mixed-state family to cover every pair for all $n\ge4$. It is stronger than producing a violation for one convenient Fourier pair.
- **The phase-average extension.** Theorem 4.5 retains the previously known shared-label construction but proves a dimension-independent lower bound for every prescribed pair. Its role is a secondary extension with explicit prior-work attribution.

## Prior work

[Qian (2026), version 2](https://arxiv.org/abs/2608.14806v2) supplies the explicit sharp-qutrit open problem, the compressed frame and determinant reduction, the attained support configuration, the entropy envelope, the older all-bases threshold $n\ge164$, and the product-state second-variation framework. [Schneeloch, Broadbent and Howell (2014)](https://doi.org/10.1103/PhysRevA.90.062119) is the original CQC proposal. [Wang, Wang and Chen (2026a), version 3](https://arxiv.org/abs/2608.03828v3) and Qian provide the existing classical-bit counterexample mechanism. [Wang, Wang and Chen (2026b), version 1](https://arxiv.org/abs/2608.04916v1) proves the previously known arbitrary-two-qubit theorem for prescribed local MUB pairs. [Tadej and Życzkowski (2006)](https://arxiv.org/abs/quant-ph/0512154) supplies the exhaustive order-three and order-four complex-Hadamard normal forms. [Stacey (2016)](https://doi.org/10.3390/math4020036) is cited for the already known Hesse configuration.

The bounded searches and their source/version checks are recorded in `scout_qutrit/novelty_report.md` and the structural rerun in `scout_cqc/novelty_gate.md`. This digest does not infer historical priority from search absence. Qian's version 2 was read directly; the other source-scope comparisons follow the paper's prior-work section, which supersedes this outline.

## Verification status

The exact qutrit checker passed with exit status zero (most recently on 3 November 2026, in 23.9 s normally and 23.4 s under `python -O`; see `scout_qutrit/verify_qutrit_sos.log`). It checked four positive rational Gram blocks, all 1,820 degree-twelve coefficients, six equality identities, and a fresh direct-Gram-minor derivation of the target polynomial. `scout_qutrit/negative_controls.py` confirms that corrupted certificates are rejected in both modes. This is exact computer-assisted algebra with an inspected human-readable reduction; it is not proof-assistant verification or independent human peer review.

The analytic counterexample argument was re-derived in this digest from its displayed formulas: separability, compression, the Hessian, its threshold, the resolvent remainder constants, the $n=4$ supports, and the phase-average/Pinsker bound. The existing regression log checks Fourier dimensions $5,6,7,11,20$, three order-four Hadamard parameters, the spectrum, complete measurement tables, product decomposition, and the final rational arithmetic. Those finite numerical checks are supporting diagnostics; the universal theorem rests on the analytic argument.

Per the task instruction, no settled checker or build was rerun for this documentation pass. Existing logs were inspected and the source/certificate hashes were recorded. No claim is made that a program has checked the full $2\times3$ problem, global positivity for $c\le1/2$, historical novelty, or the entire manuscript in a proof assistant.

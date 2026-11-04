# Bounded novelty gate: complementary quantum correlations at 2×3

Date: 1 November 2026. This is a working note, not a mathematical solution. Prior-art credit (including the O'Connor and AlperTheKing repositories, and Iqbal) is stated in the paper, which supersedes this note.

## Frozen target

For every density matrix ρ on C²⊗C³, let Q be the computational measurement on each side, and R the Pauli-X measurement on the qubit and the canonical Fourier measurement on the qutrit. Decide whether

    G(ρ)=S(ρ_A)+S(ρ_B)−S(ρ)−I(Q_A:Q_B)−I(R_A:R_B) ≥ 0.

All quantities use one common logarithm base. The fixed pair is a normal form for arbitrary local mutually unbiased rank-one projective pairs in these dimensions, by local unitary changes and equivalence of order-three complex Hadamard matrices.

## Inspected original sources

1. Lilong Qian, *Separable Counterexamples to Complementary Quantum Correlations, and Why Random Search Missed Them*, arXiv:2608.14806v2, 19 August 2026, 29 pages. The [original PDF](https://arxiv.org/pdf/2608.14806) was successfully retrieved by following the PDF link from the [Pith paper page](https://pith.science/paper/2608.14806). Direct versioned PDF/HTML retrieval attempts failed; these failures were not used as evidence of absence. The native arXiv API separately verified title, author and latest version. The abstract exposed through the metadata API is stale relative to the v2 PDF, and should not be used to infer that 2×5 remains unresolved.

   - §5: states CQC true at 2×2 by Wang et al.; false at all pairs m, n ≥ 3 and at 2×n except n = 3; 2×5 is treated separately in §7.2.
   - §6.6: a restricted equal-prior separable two-ray family at 2×3 is covered computationally. This is not a proof for arbitrary 2×3 states.
   - §7.1, Lemma 7.1 and Definition 7.2: at a faithful product σ = α⊗β and marginal-free Hermitian δ, the gap's second derivative is Qσ(δ) = ⟨δ, Ωσ⁻¹δ⟩ − χ²_{ΔQσ}(ΔQδ) − χ²_{ΔRσ}(ΔRδ). ACC₂×₃ is the nonnegativity of this form for all such anchors and directions. Its failure would refute full CQC.
   - §7.2, Theorem 7.7: reports a negative second variation at 2×5 and a full-rank PPT counterexample. The printed anchor gives α's Bloch vector and β's spectrum but not its eigenbasis or the perturbation vector. Thus the numerical witness was not independently reproduced in this audit; the report is prior art and bars any claim that the 2×5 second-variation mechanism is new.
   - §7.3: expressly states that ACC₂×₃ remains unresolved after structured and multistart searches. It warns against cancellation artefacts from nearly singular anchors.
   - §11(1), printed p. 24: explicitly requests deciding CQC at 2×3, separating local anchor convexity from the possibility of violations far from product states.
   - §11(3) and (4), printed p. 24: separately leaves open the two-ray discrimination bound S ≤ S* ≈ 3.8265583 at d = 5 and the sharp qutrit inequality S ≤ 8/3.

2. Hasan Iqbal, *On the CQC conjecture: a sufficient condition and an extension*, Quantum Information Processing 25, 250 (10 July 2026), DOI 10.1007/s11128-026-05258-2. The [full publisher HTML](https://link.springer.com/article/10.1007/s11128-026-05258-2) was inspected. The broad CQC and extended CQC conjectures there have already received higher-dimensional counterexamples. They are not fresh targets.

3. Qian v1, 15 August 2026, [full original text hosted by ResearchGate](https://www.researchgate.net/publication/412348485_Separable_Counterexamples_to_Complementary_Quantum_Correlations_and_Why_Random_Search_Missed_Them). Initially inspected before v2 retrieval. The v1 leaves 2×5 unresolved; v2 supersedes that statement. Do not conflate the versions.

## Bounded search and collision findings

Exact-title and formula/topic searches used both search engines, including `CQC qubit-qutrit`, `CQC 2×3`, `CQC 2 x 3 quantum`, `CQC 2×5`, `2608.14806`, `triangular discrimination mutually unbiased`, `qutrit 8/3 uncertainty`, and corresponding Evidence Press domain filters. No later resolution of the 2×3 case or the sharp S ≤ 8/3 subproblem was found in this boundary. This is not a global historical-priority certification.

Wang, Wang and Chen's [arXiv:2608.03828](https://arxiv.org/abs/2608.03828) refutes the original equal-dimensional CQC for d ≥ 3; [arXiv:2608.04916](https://arxiv.org/abs/2608.04916) reports the 2×2 theorem. Those broad contribution units collide. At this initial gate, the remaining 2×3 cell and the explicit S subproblems were clear to investigate within the inspected boundary. The 2×5 product-anchor method is existing work.

## Independent exploratory computation

`search_rank2.py` parameterises arbitrary mixtures of two pure product states, including arbitrary priors, general Alice rays and nonorthogonal Bob rays. One thousand local optimisation restarts each at 2×3 and 2×5 found no strict violation beyond floating-point noise. This is evidence from a restricted family only, not a proof.

`product_hessian.py` uses an algebraically reduced Gram test. For each of the two measurement settings choose correlation observables O_i = A_i⊗B_i whose factors are centred and classically whitened under α and β. There are 2(n−1) such observables at 2×n. Then Ωσ(O_i) is marginal free: tracing either factor gives the corresponding centred expectation zero. The local criterion is equivalent to λ_max([Tr O_i Ωσ(O_j)]_{ij}) ≤ 1. If λ > 1 has unit eigenvector c, setting δ = Ωσ(Σ_i c_i O_i) gives Qσ(δ) = λ − λ² < 0 before optional normalisation. This exploratory computational reformulation has not separately been independently reviewed or claimed novel. It avoids directly subtracting matrices with entries of order 1/λ_min(σ).

Any strict candidate must be checked by a separate direct entropy implementation, at higher precision and with positive definiteness verified, before being called a counterexample.

## Structural rerun: fixed-measurement universality, 1 November 2026

The numerical product-anchor search was simplified to a four-dimensional supported family. Freeze its identity as follows. On a two-dimensional Bob support, take Pauli involutions B₁, B₂ with c = |Tr(B₁B₂)|/2 and Alice α_r = (I + r(X+Z)/√2)/2. The marginal-free perturbation is δ = (Z⊗B₁ − X⊗B₂)/4. The exact gap Hessian is

    Q(r,c)=(1−c)/(1−r²)+(1+c)atanh(r)/r−2/(1−r²/2).

Its small-r sign changes precisely at c = 1/2, and power-series coefficients show that some r has Q < 0 if and only if c > 1/2 within this family. Four explicit product terms certify separability. For r = 1/3, c ≥ 3/5 and t = 1/100, an exact logarithm-series bound and a resolvent fourth-derivative estimate prove a strictly negative finite gap with a uniform rational margin. These are not floating-point premises.

The compression W = span{q₀, r₀} for two selected MUB rays is **prior art**, Qian's Proposition 6.9. It makes the fine measurements binary projective readouts on W with overlap c = 1 − 2/n, for **every** MUB pair, without a Fourier-invariance assumption. Combining this old compression with the new mixed-state family yields a new residual statement: every prescribed MUB pair at 2×n, n ≥ 5, admits a separable violation. The exhaustive order-four Hadamard normal form then gives n = 4 as well. The relevant comparison is the all-MUB threshold n ≥ 164 in Qian's Theorem 4.1; the existence of some pair and some counterexample in n ≥ 4 was already known and is not claimed anew.

### Contribution units and collisions

| Unit | Existing source / object identity | Assessment within inspected boundary |
|---|---|---|
| Original CQC refutation | Wang–Wang–Chen, arXiv:2608.03828; Qian, arXiv:2608.14806 | Full collision; no new claim |
| Existence of a 2×5 counterexample | Qian v2, §7.2, product-anchor Hessian | Full collision; exact example alone is a simplification |
| Product-state second variation | Qian v2, Lemma 7.1, Kubo–Mori metric | Full collision as a method; new state is a specialisation |
| Two-ray support compressing an arbitrary MUB pair | Qian v2, Proposition 6.9 | Exact collision; explicitly attributed |
| Four-dimensional Hadamard classification | Tadej–Życzkowski (2006), §5.4, citing Haagerup | Classical dependency; not new |
| Explicit family Q(r,c), exact threshold c > 1/2 | No exact match found in bounded search | Candidate residual contribution; family-level only |
| Every prescribed MUB pair in all 2×n, n ≥ 4, finite rational witness and explicit separability | Qian's Theorem 4.1 gives every pair only for n ≥ 164; Theorem 5.1 is existential below that threshold | Candidate substantive residual contribution |
| Every prescribed pair for m, n ≥ 3, uniform excess 1/(2π⁴) | Original latent-label mechanism from Wang and Qian, previously displayed for Fourier choices | Elementary attributed extension, secondary contribution |
| Global CQC at 2×3 | Qian v2, §11(1), printed p. 24: remains open | Not solved by these constructions |

### Search log for the structural rerun

Both engines used exact formulas and quantifier variants, including: `"complementary quantum correlations" "every" "MUB" "4"`; `"CQC" "all-MUB" "5"`; `"complementary quantum correlations" "nonorthogonal" "curvature"`; `"CQC" "arctanh" "overlap"`; `"complementary quantum correlations" "all" "bases" counterexamples`; `"quantum correlations" "164" "5" mutually unbiased counterexamples`. Time-filtered searches covered the latest 100 days to 1 November 2026. Results returned the Qian paper and Wang papers, with no later exact quantified result identified. Stale search-index abstracts were not substituted for the inspected v2 text.

Qian's [official v2 PDF](https://arxiv.org/pdf/2608.14806) was re-inspected at Theorems 4.1 and 3.1, Proposition 6.9, and §11 (printed p. 24). The [original Tadej–Życzkowski arXiv preprint, quant-ph/0512154v2](https://arxiv.org/pdf/quant-ph/0512154), was inspected at §5.4, pp. 17–18 of the preprint, equations (62)–(65). It gives exactly the exhaustive H(a) family used in the four-dimensional argument.

An independent source check inspected the latest original [Wang–Wang–Chen arXiv:2608.03828v3 PDF](https://arxiv.org/pdf/2608.03828) (25 September 2026), titled *When Complementary Measurements Count the Same Classical Bit Twice: Counterexamples to CQC, ECQC, and Complementarity-Based Certification*. The main CQC theorem and Appendix A use computational/Fourier bases and equal local dimension d. The introduction explains a more general coarse-graining mechanism, but no every-MUB-pair quantifier or phase-averaged uniform lower bound appears. The higher-dimensional corollary must be described as an extension of that established mechanism, not as a separate first refutation.

### Independent checks and disposition

The product-Hessian Gram code reproduced a robust 2×5 negative anchor. An independent direct entropy calculation agreed with the Hessian sign and small-t asymptotic. The exact family was then checked independently against the closed-form spectrum and direct 10×10 density-matrix entropy. The n ≥ 4 proofs themselves are analytic and do not require those numerics.

The final separable construction and its quantified conclusions are proved analytically in the paper. The exploratory searches and computational reformulations above are not proved results, and this note is not a certification of historical priority.

Disposition: proceed with the explicitly bounded residual claims. The gate does not certify worldwide historical priority, and it does not upgrade an elementary extension to a major original result. No current evidence supports claiming that the remaining 2×3 global conjecture is solved.

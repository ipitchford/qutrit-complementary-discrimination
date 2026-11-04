# Bounded novelty audit: sharp qutrit triangular discrimination

## Claim and contribution units

The precise target is the inequality `S(u,v) ≤ 8/3` for orthonormal vectors in `C^3`, where `S` is the sum of the two triangular discriminations in a mutually unbiased basis pair. The source already states this candidate constant and proves its attainment on nine special support planes. Accordingly, the contribution is **a complete proof and exhaustive equality classification**, not invention of the constant, the frame operator, or the known Hesse SIC configuration.

The complete complementary-quantum-correlations inequality for arbitrary `2×3` states is excluded from the claim.

## Source and normalization audit

- Qian Lilong, arXiv:2608.14806v2, dated 19 August 2026, primary PDF inspected on 1 November 2026: <https://arxiv.org/pdf/2608.14806>. The sharp qutrit bound remains explicitly open in §11(4), p. 24; the introductory evidence taxonomy and the sharp-constant discussion in §6 distinguish the numerical candidate from a proved universal upper bound.
- The ResearchGate full-text mirror was inspected first. It carries v1, where the same question is §10(3): <https://www.researchgate.net/publication/412348485_Separable_Counterexamples_to_Complementary_Quantum_Correlations_and_Why_Random_Search_Missed_Them>.
- The source's Fourier matrix uses columns `ω^(jk)/sqrt(3)`, and measurement amplitudes are obtained with its adjoint. Replacing the adjoint by the Fourier matrix only permutes the three outcomes.
- The divergence has no factor `1/2`. Each divergence ranges from zero to two. The exact frame identity is `max S = 2 λmax(A_W)`, with `Tr(A_W)=2`.
- The source already proves attainment when `W` contains one vector from each basis. That statement concerns the maximum over orthonormal bases of `W`; it does not say every basis of that plane attains the maximum.

## Fingerprints prepared before or during the proof search

The target and normalizations are frozen in `target.yaml`. Three exact finite fingerprints are:

- `w=e0`: frame spectrum `(1,1/2,1/2)`, maximum `S=2`.
- `w=(1,1,1)/sqrt(3)`: the same spectrum and maximum.
- `w=(0,1,-1)/sqrt(2)`: frame spectrum `(4/3,2/3,0)`, maximum `S=8/3`.

For the single-basis frame, with `p_i=|w_i|²`, the trace is one, rank is at most two, and its second elementary symmetric invariant is `2 p0 p1 p2 / [(1-p0)(1-p1)(1-p2)]`.

The completed proof reveals a homogeneous degree-twelve real gate polynomial with 671 monomials, or 169 monomials in a complex bidegree `(6,6)` representation. Its zero set consists of the six basis rays and nine Hesse SIC rays; the first six are removable zeros introduced by clearing denominators. The proof uses a rational real sum-of-squares certificate, not a holomorphic sum-of-squares representation.

## Search corpus and actual query families

Searches used both available web engines on 1 November 2026. Recent-event queries used the stronger engine with a 120-day filter. The following literal query families were run:

1. `"triangular discrimination" "Fourier" "qutrit"`
2. `"Qian" "sharp qutrit" "8/3"`
3. `"mutually unbiased" "triangular discrimination"`
4. `"qutrit" "triangular" "discrimination" "8/3"`
5. `"triangular discrimination" "mutually unbiased" inequality`
6. `"Fourier" "orthonormal" "8/3" discrimination`
7. `"Hesse" "triangular discrimination"`
8. `"qutrit" "Fisher information" "mutually unbiased" rank`
9. `"Hesse SIC" "uncertainty" "8/3"`
10. `"qutrit" "compressed" "POVM" "Fisher"`
11. `"qutrit" "triangular-discrimination" "sharp"`
12. `"Qian" "8/3" "Fourier" qutrit`
13. `"Hesse SIC" "triangular" inequality`
14. `"2608.14806" "qutrit" proof`

The latter four reran the gate after the Hesse/SOS structure became visible. Translated aliases included Vincze–Le Cam divergence, a compressed qubit POVM, classical Fisher information of a measurement frame, Fourier complementarity, and orthogonal quantum-state discrimination.

The direct formula searches returned Qian's source and mirrors. Broader searches located existing Hesse SIC, Fisher-information, POVM, and quantum triangular-discrimination literature, but no matching sharp two-basis inequality or proof was found in the inspected result set. A primary Hesse-SIC article was located at <https://www.mdpi.com/1099-4300/20/1/16>, but its full-page fetch returned HTTP 429; its naming is therefore not used as evidence of priority. The ordinary identification of the nine explicit rays with the Hesse SIC is not claimed as new.

## Adjudication and limits

- **Statement:** known conjectural target in the inspected August 2026 primary source.
- **Proof:** no prior proof found in the bounded searches listed here. The exact certificate supplies a complete proof, independently rerun by another agent; it is not a historical-priority certificate.
- **Equality classification:** exhaustive orientation and support classification proved by the certificate and the six exact membership identities. The equality support geometry itself was already exhibited by the source, and the Hesse SIC is a previously known configuration.
- **Artefact:** a reproducible exact verification bundle, with no optimization solver required at verification time.

The appropriate outcome is **clear to prove within the recorded boundary, with bounded historical uncertainty**. Permitted wording is “we prove the sharp bound posed in Qian's §11(4)” and “we classify all equality cases.” Wording such as “the first-ever proof” is not supported by this search.

This audit is not exhaustive across unpublished work, nonindexed manuscripts, or private correspondence. No author enquiry was sent. Later searches (GitHub, Zenodo) found additional prior public statements, which the paper credits; the paper supersedes this note.

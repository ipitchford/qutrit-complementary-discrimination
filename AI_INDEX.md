# AI index: sharp qutrit discrimination and complementary correlation bounds (v0.1.0-candidate)

Machine-oriented map of claims, evidence and limits. Human readers should start with
[README.md](README.md) and the paper [paper/manuscript.pdf](paper/manuscript.pdf)
(sources [paper/manuscript.tex](paper/manuscript.tex) and [paper/sections/correlation.tex](paper/sections/correlation.tex)).
Version DOI 10.5281/zenodo.23933731; concept DOI 10.5281/zenodo.23933730. This archive is the locator
the paper cites for its exact certificate.

## Notation

MUB: mutually unbiased ("complementary") bases, |<q_j, r_k>|^2 = 1/d. Triangular discrimination
Delta(p,q) = sum_j (p_j - q_j)^2 / (p_j + q_j), no factor 1/2, so 0 <= Delta <= 2.
S_{Q,R}(u,v) = Delta in basis Q + Delta in basis R for orthonormal u, v; trivial ceiling 4.
CQC (Schneeloch, Broadbent and Howell 2014): I(A:B) >= I(Q_A:Q_B) + I(R_A:R_B); gap G(rho) = I(A:B) - I(Q_A:Q_B) - I(R_A:R_B),
natural logarithms (nats); a negative gap is a violation. Qian = arXiv:2608.14806v2.

## Claims and where they are proved

| ID | Claim | Location | Evidence type |
|---|---|---|---|
| C1 | For every MUB pair in C^3 and orthonormal u, v: S_{Q,R}(u,v) <= 8/3 (answers Qian Section 11(4)) | Theorem 2.1; Section 3 | human-readable frame reduction (Lemma 3.1, from Qian Section 6) plus exact rational SOS certificate (Lemma 3.2) |
| C2 | Equality iff span{u,v} = span{q_j, r_k} and the state difference is +-sqrt(3/2) times the projector difference; for computational/Fourier bases tied to the nine Hesse SIC rays | Theorem 2.1; Section 3 Step 4 | proof plus exact equality identities checked by the verifier |
| C3 | Choosing one of the two complementary settings at random recovers at most 2/3 of the quantum Fisher information for a two-state mixture weight; attained only at the C2 configurations | Corollary 2.2 | proof from C1 |
| C4 | Qian's two-ray qubit-qutrit family obeys CQC with gap at least 0.1005 nats (previously 0.0120) | Corollary 3.3 | proof from C1 and Qian Theorem 6.3 |
| C5 | For n >= 4 and every prescribed MUB pair on C^2 and C^n, a separable state violates CQC with uniform certified gap below -9/20000000 nats; per-n margins tabulated (e.g. -1.058e-4 at n = 4); previously every-pair known only for n >= 164 | Theorem 4.1; Lemmas 4.2, 4.4, 4.5; Proposition 4.3 | analytic proof with exact rational bounds (certified_margin.py) |
| C6 | Earlier cruder constant -17117/114750000000 also follows | Remark 4.6 | hand-checkable; also checked by certified_margin.py |
| C7 | Both local dimensions at least three: every prescribed pair admits a separable violation with a dimension-free margin | Theorem 4.7 | analytic proof (phase-averaged shared-label mechanism; earlier unchecked equal-dimension every-pair statement by O'Connor credited) |
| C8 | Not claimed: the full 2 x 3 CQC question (open); a rigorous sharp constant in d = 5 (numerics only) | Discussion | statement of scope |

## Verification artefacts

- [scout_qutrit/exact_sos_certificate.json](scout_qutrit/exact_sos_certificate.json) (660,609 bytes, SHA-256
  825bb8108096d38a44f63f1bc91964405d189ad57b5f568530b5d8e27d598c2f): essential proof data for Lemma 3.2.
- [scout_qutrit/verify_qutrit_sos.py](scout_qutrit/verify_qutrit_sos.py): standalone exact verifier (SymPy 1.14.0,
  python-flint 0.9.0, see [requirements-exact.txt](requirements-exact.txt)). Rebuilds the degree-12 target polynomial from the six
  measurement vectors, checks all 1,820 coefficients, strict positivity of four Gram blocks by exact LDL^T and a rational norm
  bound, and the equality identities. No assert; every check exits 1 with REJECTED on failure, so `-O` does not weaken it.
  Logs: [scout_qutrit/verify_qutrit_sos.log](scout_qutrit/verify_qutrit_sos.log), [scout_qutrit/verify_qutrit_sos_optimised.log](scout_qutrit/verify_qutrit_sos_optimised.log).
- [scout_qutrit/negative_controls.py](scout_qutrit/negative_controls.py): five corrupted certificates must be rejected under
  `python -B` and `python -B -O`, genuine accepted in both. Log: [scout_qutrit/negative_controls.log](scout_qutrit/negative_controls.log).
- [scout_qutrit/PROOF_README.md](scout_qutrit/PROOF_README.md), [scout_qutrit/target.yaml](scout_qutrit/target.yaml): certificate explanation and frozen target.
- [scout_cqc/certified_margin.py](scout_cqc/certified_margin.py): standard library Fraction arithmetic proof of the uniform and
  per-n margins of Lemma 4.5 and Remark 4.6; part of the proof. Logs: [scout_cqc/certified_margin.log](scout_cqc/certified_margin.log),
  [scout_cqc/certified_margin_optimised.log](scout_cqc/certified_margin_optimised.log).
- [scout_cqc/check_final_family.py](scout_cqc/check_final_family.py): NumPy cross-checks only, not proof premises
  ([requirements-numerical.txt](requirements-numerical.txt)). Logs: [scout_cqc/check_final_family.log](scout_cqc/check_final_family.log),
  [scout_cqc/check_final_family_optimised.log](scout_cqc/check_final_family_optimised.log).
- Proof notes: [review/proof_outline.md](review/proof_outline.md), [scout_cqc/all_mub_theorem.md](scout_cqc/all_mub_theorem.md),
  [scout_cqc/all_mub_higher_dimensions.md](scout_cqc/all_mub_higher_dimensions.md) (the manuscript controls if notation differs).
- Replay commands: [README.md](README.md); CI: [.github/workflows/replay.yml](.github/workflows/replay.yml).

## Sources, novelty and provenance

- [refs.bib](refs.bib) and [refs/records/](refs/records/): bibliography and the Crossref, arXiv, GitHub and Zenodo records it was copied from.
- [scout_qutrit/novelty_report.md](scout_qutrit/novelty_report.md), [scout_cqc/novelty_gate.md](scout_cqc/novelty_gate.md): dated, bounded audits.
- [RESEARCH_GATES.json](RESEARCH_GATES.json): contribution map, sources read, limitation triage.
- Integrity: [MANIFEST.sha256](MANIFEST.sha256). Licences: [LICENSE](LICENSE) (text, data and records CC0-1.0; code MIT).
  Citation: [CITATION.cff](CITATION.cff); archive metadata: [.zenodo.json](.zenodo.json).

## Limits

Unrefereed candidate: internal AI-assisted review only; no human peer review, independent reproduction or proof-assistant
formalisation. The qutrit proof is computer-assisted exact rational arithmetic and depends on the certificate file. The
correlation margins are tiny and structural, not experimentally useful. The full qubit-qutrit CQC question and the sharp
d = 5 constant remain open. Priority holds only within bounded searches current to 3 November 2026.

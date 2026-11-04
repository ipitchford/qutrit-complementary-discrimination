# Sharp qutrit discrimination and complementary correlation bounds

Research and verification package, version 0.1.0-candidate (revised 3 November 2026, archived 4 November 2026). Author: Anonymous.

Version DOI [10.5281/zenodo.23933731](https://doi.org/10.5281/zenodo.23933731); concept DOI (all versions) [10.5281/zenodo.23933730](https://doi.org/10.5281/zenodo.23933730). Unrefereed candidate; internal AI-assisted review only.

Licence: the paper text is released under CC0-1.0; the code in this bundle is released under the MIT licence.

## Results in brief

The complementary quantum correlation (CQC) inequality of Schneeloch, Broadbent and Howell (2014) says that the classical correlations seen in two complementary measurement tables never add up to more than the quantum mutual information of the shared state. It is now known to fail in most dimensions; it holds for two qubits, and the qubit–qutrit case is open.

1. **Sharp qutrit bound.** For two orthogonal qutrit states, the summed triangular discrimination in any pair of complementary bases is at most 8/3:

   \[
   \Delta(|u|^2,|v|^2)+\Delta(|F_3^*u|^2,|F_3^*v|^2)\le 8/3,
   \qquad \Delta(p,q)=\sum_i\frac{(p_i-q_i)^2}{p_i+q_i}.
   \]

   Every equality case is classified. This answers the question posed in Qian, arXiv:2608.14806v2, §11(4). The proof is computer-assisted, with an exact rational certificate supplied here.
2. **Every prescribed measurement pair, qubit–qudit.** For every \(n\ge4\) and every prescribed pair of complementary measurements on each side, there is a separable state on \(\mathbb C^2\otimes\mathbb C^n\) that violates CQC, with a uniform certified gap below \(-9/20000000=-4.5\times10^{-7}\) nats (larger certified margins for each \(n\), e.g. \(-1.058\times10^{-4}\) at \(n=4\), are tabulated in the paper). An earlier version stated the cruder, hand-checkable constant \(-17117/114750000000\); it also follows and is kept as a remark. Previously this every-pair statement was known only for \(n\ge164\).
3. **Both dimensions at least three.** A phase-averaging extension of the known shared-label mechanism covers every prescribed pair, with a dimension-free margin. An earlier, unchecked every-pair statement for equal dimensions appears in E. O'Connor's public repository (Zenodo 10.5281/zenodo.21499722) and is credited in the paper.

The full CQC question for arbitrary states on \(\mathbb C^2\otimes\mathbb C^3\) remains open.

## Start here

| File | Purpose |
|---|---|
| `paper/manuscript.pdf` | The research article, with both main proofs and their scope. |
| `paper/manuscript.tex`, `paper/sections/correlation.tex` | LaTeX sources. |
| `review/proof_outline.md` | Tagged proof map and dependency structure. |
| `scout_qutrit/PROOF_README.md` | Detailed explanation of the exact qutrit certificate. |
| `scout_qutrit/exact_sos_certificate.json` | Essential rational certificate data; this is part of the proof. |
| `scout_qutrit/verify_qutrit_sos.py` | Standalone exact verifier. |
| `scout_qutrit/negative_controls.py` | Checks that corrupted certificates are rejected, with and without `-O`. |
| `scout_cqc/certified_margin.py` | Exact rational (stdlib-only) check of the certified uniform and per-\(n\) margins; part of the proof of Lemma 4.5. |
| `scout_cqc/check_final_family.py` | Numerical cross-checks of the correlation constructions (not proof premises). |
| `scout_cqc/all_mub_theorem.md`, `scout_cqc/all_mub_higher_dimensions.md` | Working proofs of the correlation theorems. |
| `scout_qutrit/novelty_report.md`, `scout_cqc/novelty_gate.md` | Bounded literature and object-identity audits (working notes). |
| `AI_INDEX.md` | Machine-oriented map of claims, evidence and limits. |
| `RESEARCH_GATES.json` | Contribution map, sources read and limitation triage. |
| `refs.bib`, `refs/records/` | The bibliography as BibTeX, copied from the retained Crossref, arXiv, GitHub and Zenodo records. |
| `CITATION.cff`, `.zenodo.json`, `LICENSE` | Citation, archive metadata and licences (text CC0-1.0, code MIT). |
| `.github/workflows/replay.yml` | CI replay of the exact checks with and without `-O`. |
| `MANIFEST.sha256` | Checksums for every other file in this package. |

The manuscript and its certificate must be kept together. The paper cites this archive, DOI [10.5281/zenodo.23933731](https://doi.org/10.5281/zenodo.23933731), as the locator of the certificate and verifier.

## Reproduce the exact proof

From the bundle directory, with Python 3.11 or 3.12:

```sh
python -m pip install -r requirements-exact.txt
python -B scout_qutrit/verify_qutrit_sos.py scout_qutrit/exact_sos_certificate.json
```

or, with `uv`:

```sh
uv run --with sympy==1.14.0 --with python-flint==0.9.0 python3 -I -B scout_qutrit/verify_qutrit_sos.py scout_qutrit/exact_sos_certificate.json
```

A valid run ends with:

```text
All 1,820 degree-12 monomial coefficients agree exactly.
All six equality-classification identities agree exactly.
Independent exact Gram-minor derivation matches the gate polynomial.
VERIFIED: exact SOS, strict Gram positivity, gate normalization, and equality witnesses.
```

Every check in the verifier is an unconditional test that exits with status 1 and a `REJECTED:` message on failure; none uses Python's `assert`. The result is therefore the same under `python -O` or `PYTHONOPTIMIZE`.

Measured on 3 November 2026 (Python 3.11.14, SymPy 1.14.0, python-flint 0.9.0): 23.9 s normally and 23.4 s under `-O` (logs: `scout_qutrit/verify_qutrit_sos.log`, `scout_qutrit/verify_qutrit_sos_optimised.log`). Expect roughly 25–45 s on a laptop. No semidefinite solver, numerical eigenvalue computation, random search, pickle file or certificate-generation script is required. The verifier derives the target polynomial independently from the six measurement vectors rather than trusting the stored polynomial.

### Negative controls

```sh
uv run --with sympy==1.14.0 --with python-flint==0.9.0 python3 -I -B scout_qutrit/negative_controls.py scout_qutrit/exact_sos_certificate.json
```

This writes five corrupted copies of the certificate to a temporary directory (one target coefficient; one Gram entry; one auxiliary-matrix diagonal entry that makes the exact LDL test fail; one equality-witness coefficient; one basis monomial) and requires the verifier to reject each of them under both `python -B` and `python -B -O`. It also requires the genuine certificate to be accepted in both modes. The log is `scout_qutrit/negative_controls.log`; all ten corrupted runs were rejected.

The proof checks every polynomial coefficient in rational arithmetic and proves strict positivity of all four Gram blocks by exact rational elimination and a rational norm bound. Floating-point optimisation helped find the certificate but is not a premise of its verification. This is not a formalisation in Lean or another proof assistant.

Essential file hashes:

```text
825bb8108096d38a44f63f1bc91964405d189ad57b5f568530b5d8e27d598c2f  exact_sos_certificate.json
ed0dd4b41edeb77d85e3a1dc6787d68ae635bcd6f0918b0a2fc29d3a6b5f2162  verify_qutrit_sos.py
```

The certificate is 660,609 bytes.

## Certified correlation margins

```sh
python -B scout_cqc/certified_margin.py
```

Standard library only, exact `Fraction` arithmetic, no `assert` (fail-closed under `-O`). It proves the uniform margin \(-9/20000000\) at \((r,t)=(61/200,421/20000)\) for all overlaps \(c\in[3/5,1]\), the per-\(n\) table, and that the earlier constant also follows. Runs in under a second; logs `scout_cqc/certified_margin.log` and `scout_cqc/certified_margin_optimised.log` (`-O`).

## Optional numerical cross-checks

The correlation theorems are proved analytically. These checks are supplementary:

```sh
python -m pip install -r requirements-numerical.txt
python -B scout_cqc/check_final_family.py
```

or `uv run --python 3.12 --with numpy==2.5.4 python3 -I -B scout_cqc/check_final_family.py`. The script uses no `assert` and behaves identically under `-O`. It compares the full density-matrix entropy calculation, closed-form spectrum, explicit separable decomposition and original fine-outcome tables against the compressed binary tables. It covers canonical Fourier pairs (n = 5, 6, 7, 11, 20), the order-four Hadamard family, random non-canonical prescribed pairs at n = 4 (built from an arbitrary frame V = U D1 P1, as in the proof), and random prescribed pairs at n = 5–8 (including the non-Fourier class F2⊗F2⊗F2 at n = 8), with random complementary pairs on the qubit side. The witness checked is the new one, \((r,t)=(61/200,421/20000)\), against the margin \(9/20000000\). Each run took about 0.3 s (Python 3.12, NumPy 2.5.4); logs: `scout_cqc/check_final_family.log` and `scout_cqc/check_final_family_optimised.log`.

## Rebuild the paper

With a standard TeX installation, run `pdflatex manuscript.tex` twice from the `paper` directory.

## Provenance

This work was produced with AI assistance. The working notes in `scout_qutrit/` and `scout_cqc/` record bounded searches and earlier exploratory directions; some refer to discovery scripts outside this bundle that are not needed to verify any theorem. The manuscript controls the theorem statements if a working note uses different notation. Literature searches, including arXiv, GitHub and Zenodo, were current to 3 November 2026 and are bounded.

Primary problem source: Qian, L. (2026). *Separable counterexamples to complementary quantum correlations, and why random search missed them* (Version 2). https://arxiv.org/abs/2608.14806v2

The TeX build transcript of the working bundle is not included (it records local paths only).

## How to cite

Anonymous (2026). *Sharp qutrit discrimination and unavoidable correlation overcounting for complementary measurements*. Version 0.1.0-candidate. Evidence Press, unrefereed candidate. https://doi.org/10.5281/zenodo.23933731

- Version DOI: [10.5281/zenodo.23933731](https://doi.org/10.5281/zenodo.23933731); concept DOI (all versions): [10.5281/zenodo.23933730](https://doi.org/10.5281/zenodo.23933730)
- Repository: <https://github.com/ipitchford/qutrit-complementary-discrimination>; release page: <https://evidencepress.org/releases/qutrit-complementary-discrimination/>

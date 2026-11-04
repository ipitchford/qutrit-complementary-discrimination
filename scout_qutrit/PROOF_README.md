# Exact certificate for the sharp qutrit triangular-discrimination bound

**Date:** 1 November 2026.

This bundle proves the sharp bound requested in Qian, *Separable Counterexamples to Complementary Quantum Correlations, and Why Random Search Missed Them*, arXiv:2608.14806v2, 19 August 2026, §11(4), p. 24. The inspected v1 mirror labels it §10(3). The source is [arXiv:2608.14806](https://arxiv.org/pdf/2608.14806).

The proof is an exact computer-assisted algebra proof. Numerical semidefinite optimization was used to discover the certificate; verification uses rational arithmetic and symbolic polynomial identities only.

## 1. The theorem and its equality cases

Let \(u,v\in\mathbb C^3\) be orthonormal, and let \(F_{jk}=\omega^{jk}/\sqrt3\), \(\omega=e^{2\pi i/3}\), with indices \(0,1,2\). For probability vectors define

\[
\Delta(p,q)=\sum_i\frac{(p_i-q_i)^2}{p_i+q_i},\qquad 0/0:=0.
\]

Then

\[
S(u,v):=\Delta(|u|^2,|v|^2)+\Delta(|F^*u|^2,|F^*v|^2)\le\frac83.
\]

The constant is attained. Equality holds precisely as follows. Choose a computational basis vector \(q\) and a Fourier basis vector \(f\). Put \(W=\operatorname{span}\{q,f\}\), and let \(P_W\) be its orthogonal projector. The unordered pair of rank-one projectors \(\{P_u,P_v\}\) must be

\[
P_u=\frac12(P_W+J),\qquad P_v=\frac12(P_W-J),\qquad
J=\sqrt{\frac32}(P_q-P_f).
\]

Exchanging \(u,v\) changes the sign of \(J\). Phases of individual vectors do not matter. Thus merely having \(W\) contain one vector from each basis is necessary for equality, but the basis \(u,v\) inside \(W\) must also have the stated orientation.

Equivalently, the complement \(W^\perp\) is one of the nine rays obtained by cyclically permuting

\[
\frac1{\sqrt2}(0,1,-\omega^k),\qquad k=0,1,2.
\]

These are the usual Hesse SIC rays. The result also holds for every pair of mutually unbiased bases of \(\mathbb C^3\). Indeed, after dephasing a \(3\times3\) complex Hadamard matrix, a nonfirst row has form \((1,x,y)\) with \(|x|=|y|=1\) and \(1+x+y=0\), forcing \(\{x,y\}=\{\omega,\omega^2\}\). The remaining row is then forced by orthogonality. Row/column phases and permutations do not change the claim.

## 2. Reduction to a three-dimensional Gram matrix

Write \(W=w^\perp\), \(P=P_W\), and \(J=P_u-P_v\). On the real three-dimensional space of traceless Hermitian operators supported on \(W\), use the inner product \(\operatorname{Tr}(XY)\). Then \(\operatorname{Tr}J^2=2\).

For each of the six measurement vectors \(e\), put

\[
g_e=\langle e,Pe\rangle,\qquad
H_e=P|e\rangle\langle e|P-\frac{g_e}{2}P.
\]

Let \(A_W\) be the positive semidefinite frame operator of the six vectors \(H_e/\sqrt{g_e}\); a zero vector is assigned when \(g_e=0\). Then

\[
S(u,v)=\langle J,A_WJ\rangle,\qquad
\max_{u,v\text{ spanning }W}S(u,v)=2\lambda_{\max}(A_W),
\qquad \operatorname{Tr}A_W=2.
\]

The last identity follows from \(\|H_e\|_{\rm HS}^2=g_e^2/2\) and \(\sum_e g_e=4\). Since \(A_W\succeq0\) and has trace two,

\[
\lambda_{\max}(A_W)\le\frac43
\quad\Longleftrightarrow\quad
\det\left(\frac43I-A_W\right)\ge0.
\]

To see the nontrivial direction, if one eigenvalue exceeded \(4/3\), the other two would each be below \(2/3\); the determinant would have exactly one negative factor.

## 3. Exact polynomial normalization

Global phase allows the exhaustive parametrization

\[
w=(r,a+i\sqrt3\,b,c+i\sqrt3\,d),\qquad
n=\|w\|^2=r^2+a^2+3b^2+c^2+3d^2>0.
\]

The projector is \(P=I-ww^*/n\). No division by \(r\) is used for the inequality; the parametrization also covers \(r=0\).

Use unnormalized measurement vectors

\[
E_0,E_1,E_2=e_0,e_1,e_2,
\qquad E_{3+j}=(1,\omega^j,\omega^{2j}),
\]

with squared lengths \(\ell_i=1\) or \(3\). Define

\[
C_{ij}=n\langle E_i,E_j\rangle-\langle E_i,w\rangle\langle w,E_j\rangle,
\quad B_i=C_{ii},\quad D_i=\ell_iB_i,
\quad M_{ij}=|C_{ij}|^2-\frac12B_iB_j.
\]

The six-by-six frame Gram matrix is

\[
K_{ij}=\frac{M_{ij}}{n\sqrt{D_iD_j}}.
\]

Its three potentially nonzero eigenvalues are those of \(A_W\). In particular, its order-two and order-three principal minors give \(e_2(A_W)\) and \(e_3(A_W)\). Expanding these minors and cancelling exact factors gives the homogeneous degree-twelve polynomial \(Q(r,a,b,c,d)\) in the certificate, with 671 nonzero monomials and the identity

\[
\boxed{\displaystyle
Q=\frac12\left(\prod_{i=0}^5D_i\right)
\det\left(\frac43I-A_W\right)
=\frac{729}{2}n^6\left(\prod_e g_e\right)
\det\left(\frac43I-A_W\right).}
\]

All quantities in the prefactor are positive away from the six computational/Fourier rays for \(w\). The standalone verifier independently derives this identity from the direct two-by-two and three-by-three Gram-minor formulas; it does not trust a previously generated polynomial file.

## 4. The rational sum-of-squares certificate

The JSON file supplies four vectors \(Z_\nu\) of rational homogeneous sextics, of lengths \(43,41,40,41\), and four rational symmetric matrices \(G_\nu\), such that

\[
Q=\sum_{\nu=1}^4 Z_\nu^TG_\nu Z_\nu.
\]

The verifier expands the right side and checks every coefficient exactly, including all coefficients that must be zero. The four blocks correspond to simultaneous complex conjugation \((b,d)\mapsto(-b,-d)\) and exchange \((a,b)\leftrightarrow(c,d)\).

Each block comes with a simpler rational matrix \(G_{0,\nu}\). Exact rational LDL decomposition proves

\[
G_{0,\nu}-\tfrac14I\succ0.
\]

The verifier also checks, entry by entry, that

\[
|(G_\nu-G_{0,\nu})_{ij}|\le\frac1{1000}.
\]

As every block has size at most 43, symmetry and the maximum absolute row-sum bound imply

\[
\|G_\nu-G_{0,\nu}\|_2\le\frac{43}{1000},\qquad
G_\nu\succeq\frac{207}{1000}I\succ0.
\]

Consequently \(Q\ge0\) for all real \(r,a,b,c,d\). The polynomial identity proves the determinant inequality wherever the denominators are nonzero. The original summands extend continuously at zero denominators because \(|\langle e,Je\rangle|\le g_e\), so the summand is bounded by \(g_e\). Alternatively, at each exceptional ray one computes \(\operatorname{spec}A_W=(1,1/2,1/2)\), which gives \(S\le2\). This completes the inequality proof.

## 5. Exact classification of equality

Strict positivity of all four Gram matrices implies that \(Q=0\) forces every component of every \(Z_\nu\) to vanish. The certificate additionally records exact linear-combination identities showing that the real and imaginary parts of these three holomorphic sextics lie in their span:

\[
\begin{aligned}
h_1&=r^2z(z^3+r^3-2rzt),\\
h_2&=r^2t(t^3+r^3-2rzt),\\
h_3&=r^2zt(zt-r^2),
\end{aligned}
\qquad z=a+i\sqrt3b,\quad t=c+i\sqrt3d.
\]

For the block decomposition the identities use \(\operatorname{Re}(h_1\pm h_2)\), \(\operatorname{Im}(h_1\pm h_2)/\sqrt3\), \(\operatorname{Re}h_3\), and \(\operatorname{Im}h_3/\sqrt3\). The standalone verifier checks all six identities exactly.

In a chart with \(r\ne0\), scale \(r=1\). Then \(h_3=0\) gives \(zt=0\) or \(zt=1\). In the former case, both coordinates zero give a computational ray, while exactly one nonzero coordinate has cube \(-1\), giving one of the six SIC rays in this chart. In the latter case, \(h_1=h_2=0\) force \(z^3=t^3=1\) and \(zt=1\), giving the three Fourier rays. Every permutation of three computational coordinates preserves the computational/Fourier measurement pair, up to phases and outcome permutations, so choosing a nonzero coordinate as the first one covers the remaining chart.

The six computational/Fourier rays are strict for the original bound. Thus equality requires exactly one of the nine SIC complements. In such a plane \(W=\operatorname{span}(q,f)\), the two single-basis frame operators are rank-one projectors whose Bloch axes have inner product \(-1/3\). Their sum has spectrum \((4/3,2/3,0)\). The simple largest eigendirection is precisely \(J=\pm\sqrt{3/2}(P_q-P_f)\), proving the equality statement in §1.

## 6. Reproduction and files

The complete verification needs only:

- `exact_sos_certificate.json`: exact rational data, 660,609 bytes.
- `verify_qutrit_sos.py`: independent verifier; no optimization package is required.
- `negative_controls.py`: optional; confirms that five kinds of corrupted certificate are rejected under both `python -B` and `python -B -O`.

Tested with Python **3.12.14**, SymPy **1.14.0**, and python-flint **0.9.0**. Run:

```sh
python verify_qutrit_sos.py exact_sos_certificate.json
```

If these packages are not installed, install `sympy==1.14.0` and `python-flint==0.9.0` in the environment used to run the script. Every check in the verifier is unconditional, so the result is the same with or without `-O`. The 3 November 2026 runs (Python 3.11.14, SymPy 1.14.0, python-flint 0.9.0) took 23.9 s normally and 23.4 s under `-O`, and printed:

```text
VERIFIED: exact SOS, strict Gram positivity, gate normalization, and equality witnesses.
```

SHA-256 hashes:

```text
825bb8108096d38a44f63f1bc91964405d189ad57b5f568530b5d8e27d598c2f  exact_sos_certificate.json
ed0dd4b41edeb77d85e3a1dc6787d68ae635bcd6f0918b0a2fc29d3a6b5f2162  verify_qutrit_sos.py
```

The other scripts in the research directory document discovery and rational reconstruction. They are not needed to verify the theorem.

## 7. Scope and immediate consequence

This resolves the source's sharp triangular-discrimination problem and classifies its equality cases. It does **not** prove the general complementary-quantum-correlations inequality for arbitrary states on \(\mathbb C^2\otimes\mathbb C^3\).

For the source's equal-prior orthogonal two-ray family, combining the proved bound with its existing entropy envelope gives the explicit gap

\[
G\ge h(1/\sqrt2)-\frac32\log\frac43+\frac16\log2
=0.1004969521153402778\ldots\ \text{nats},
\]

where \(h(t)=H((1+t)/2,(1-t)/2)\). This strengthens the source's certified gap for that particular family. The gap constant here is a consequence of the envelope and is not asserted to be the sharp entropy-gap constant.

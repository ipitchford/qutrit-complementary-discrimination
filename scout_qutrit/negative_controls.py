#!/usr/bin/env python3
"""Negative controls for verify_qutrit_sos.py.

Each control writes one deliberately corrupted copy of the certificate to a
temporary directory, runs the verifier on it in a fresh interpreter, and
requires the verifier to reject it (nonzero exit status and a REJECTED line).
Every control is run twice: under ``python -B`` and under ``python -B -O``.
The untouched certificate is also run under both modes and must be accepted.

Run: python negative_controls.py [exact_sos_certificate.json] [--tmpdir DIR]

Standard library only, apart from the verifier's own dependencies
(sympy, python-flint), which the verifier subprocess imports.
"""
import argparse
import copy
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import time

HERE = Path(__file__).resolve().parent
VERIFIER = HERE / 'verify_qutrit_sos.py'


def require(condition, message):
    if not condition:
        raise SystemExit('NEGATIVE CONTROL FAILURE: ' + message)


def bump(value):
    """Return a different rational string."""
    num, _, den = value.partition('/')
    den = den or '1'
    return '%d/%s' % (int(num) + 1, den)


def corrupt_target(cert):
    cert['polynomial'][0][1] = bump(cert['polynomial'][0][1])
    return 'target polynomial coefficient'


def corrupt_gram(cert):
    block = cert['blocks'][0]
    block['gram_upper'][1] = bump(block['gram_upper'][1])
    return 'one off-diagonal Gram entry (exact matrix)'


def corrupt_ground(cert):
    # Diagonal entry (0,0) of the auxiliary matrix set to 0, so the first LDL
    # pivot of H - I/4 equals -1/4.
    cert['blocks'][0]['ground_upper'][0] = '0'
    return 'one auxiliary (ground) diagonal entry; LDL must fail'


def corrupt_witness(cert):
    witness = cert['equality_witnesses'][0]
    for k, value in enumerate(witness['coefficients']):
        if value != '0':
            witness['coefficients'][k] = bump(value)
            break
    return 'one equality-witness coefficient'


def corrupt_basis(cert):
    # Replace the exponent of the first monomial of the first basis sextic by
    # a different degree-6 monomial absent from that sextic.
    poly = cert['blocks'][0]['basis'][0]
    present = {tuple(e) for e, _ in poly}
    for candidate in ([6, 0, 0, 0, 0], [0, 6, 0, 0, 0], [0, 0, 0, 6, 0],
                      [5, 1, 0, 0, 0], [0, 0, 6, 0, 0]):
        if tuple(candidate) not in present:
            poly[0][0] = candidate
            return 'one basis monomial exponent'
    raise SystemExit('could not construct basis corruption')


CONTROLS = [corrupt_target, corrupt_gram, corrupt_ground, corrupt_witness,
            corrupt_basis]


def run(path, optimise):
    flags = ['-I', '-B'] + (['-O'] if optimise else [])
    started = time.monotonic()
    proc = subprocess.run([sys.executable] + flags + [str(VERIFIER), str(path)],
                          capture_output=True, text=True)
    return proc, time.monotonic() - started


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('certificate', nargs='?', type=Path,
                        default=HERE / 'exact_sos_certificate.json')
    parser.add_argument('--tmpdir', type=Path, default=None,
                        help='parent directory for temporary corrupted files')
    args = parser.parse_args()
    original = json.loads(args.certificate.read_text())
    with tempfile.TemporaryDirectory(dir=args.tmpdir) as tmp:
        tmp = Path(tmp)
        for optimise in (False, True):
            mode = 'python -B -O' if optimise else 'python -B'
            proc, secs = run(args.certificate, optimise)
            require(proc.returncode == 0 and 'VERIFIED' in proc.stdout,
                    'genuine certificate not accepted under ' + mode)
            print('[%s] genuine certificate: ACCEPTED (%.1f s)' % (mode, secs),
                  flush=True)
            for control in CONTROLS:
                cert = copy.deepcopy(original)
                label = control(cert)
                path = tmp / (control.__name__ + '.json')
                path.write_text(json.dumps(cert))
                proc, secs = run(path, optimise)
                reason = [ln for ln in (proc.stderr + proc.stdout).splitlines()
                          if 'REJECTED' in ln]
                require(proc.returncode != 0, label + ' accepted under ' + mode)
                require('VERIFIED' not in proc.stdout,
                        label + ' printed VERIFIED under ' + mode)
                require(bool(reason), label + ' failed without a REJECTED message')
                print('[%s] %s: rejected, exit %d (%.1f s): %s'
                      % (mode, label, proc.returncode, secs, reason[-1]),
                      flush=True)
    print('ALL NEGATIVE CONTROLS PASSED: 5 corruptions rejected in both modes; '
          'genuine certificate accepted in both modes.')


if __name__ == '__main__':
    main()

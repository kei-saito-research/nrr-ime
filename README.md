# NRR-IME: Structure-Aware Optimization for Stateful Reasoning on Stateless LLM APIs

Reference implementation package for the NRR-IME study (pre-public moderation phase).

Part of the Non-Resolution Reasoning (NRR) research program.
Program Map (series hub): https://github.com/kei-saito-research/nrr-core/blob/main/PROGRAM_MAP.md

NRR is not an anti-LLM framework.
NRR does not replace standard LLM use.
NRR optimizes when to commit and when to defer, under explicit conditions.

## DOI

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.18793316.svg)](https://doi.org/10.5281/zenodo.18793316)

## Publication handling

- This repository is maintained in pre-public mode while IME is under moderation.
- Manuscript text artifacts (`.tex`, `.pdf`) are not included.
- Full run outputs and generated figure PNGs are not included before public release.

## Repository Structure

```
nrr-ime/
|-- README.md
|-- LICENSE
|-- requirements.txt
|-- reproducibility.md
|-- experiments/
|   |-- phase_comparison.py
|   `-- scaling_validation.py
`-- .gitignore
```

## Quick Start

```bash
pip install -r requirements.txt
python3 experiments/phase_comparison.py
python3 experiments/scaling_validation.py
```

## Reproducibility

See `reproducibility.md` for fixed settings and pre-submission output policy.

## Related Repositories

- https://github.com/kei-saito-research/nrr-core
- https://github.com/kei-saito-research/nrr-phi
- https://github.com/kei-saito-research/nrr-transfer

## License

CC BY 4.0. See `LICENSE`.

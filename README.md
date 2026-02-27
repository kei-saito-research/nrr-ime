# NRR-IME: Structure-Aware Optimization for Stateful Reasoning on Stateless LLM APIs

NRR-IME provides a pre-public implementation package for **ambiguity-preserving inference** under stateless LLM API constraints. The engineering objective is to reduce **premature commitment in LLM decoding** and limit downstream rework caused by **semantic collapse**. The control policy is **defer vs commit** under explicit conditions: maintain compatible alternatives while evidence is weak, then commit when action boundaries are clear. This repository intentionally ships a minimal reproducibility surface (scripts and protocol notes) during moderation, without manuscript text or full result artifacts. It is intended for operational benchmarking of structure-aware updates, not for over-claiming universal superiority. The emphasis is auditability and safe scope: explicit assumptions, fixed protocol hooks, and visible limits before public manuscript release.

**Quick links**
- arXiv: pending (under moderation; no public URL yet)
- [Positioning (NRR vs related approaches)](./docs/positioning.md)
- [Search Keywords and Weekly Rank Log](./docs/keywords.md)

**EN/JA query terms**
- `early commitment` = `早期確定`
- `ambiguity-preserving inference` = `曖昧性保持推論`

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

## Collaboration Style

I support written technical Q&A, concept clarification, and small evaluation design.

Typical flow:
1. you send questions and context,
2. I return a structured technical response,
3. if needed, I provide an English-ready version for external sharing.

Scope: research interpretation and evaluation planning.  
Out of scope: production integration, implementation outsourcing, ongoing operations, and SLA/deadline commitments.  
Contact: kei.saito.research@gmail.com

## License

CC BY 4.0. See `LICENSE`.

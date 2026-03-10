# NRR-IME: Interface Decomposition for Stable State Transitions on Stateless LLM APIs

NRR-IME provides an interface-structure package for **ambiguity-preserving inference** under stateless LLM API constraints. The engineering objective is to reduce **premature commitment in LLM decoding** and limit downstream rework caused by **semantic collapse**. The control policy is **defer vs commit** under explicit conditions: maintain compatible alternatives while evidence is weak, then commit when action boundaries are clear. This repository includes the current manuscript snapshot and reproducibility assets for benchmarking which interface decomposition yields stable state transitions, with explicit protocol constraints and condition-bounded claims.

**Quick links**
- Manuscript snapshot: `manuscript/current/paper4-nrr-ime-v67.tex` / `paper4-nrr-ime-v67.pdf`
- [Positioning (NRR vs related approaches)](./docs/positioning.md)
- [Search Keywords and Weekly Rank Log](./docs/keywords.md)

**EN/JA query terms**
- `early commitment` = `早期確定`
- `ambiguity-preserving inference` = `曖昧性保持推論`

Part of the Non-Resolution Reasoning (NRR) research program.

## NRR Series Hub (Start here)

For the cross-paper map and current series links, start here:
- [NRR Series Hub](https://github.com/kei-saito-research/nrr-series-hub)

NRR is not an anti-LLM framework.
NRR does not replace standard LLM use.
NRR optimizes when to commit and when to defer, under explicit conditions.
Series numbering policy: `paper3` is permanently skipped and never reused.

## DOI

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.18793316.svg)](https://doi.org/10.5281/zenodo.18793316)

## Manuscript Artifacts

Current manuscript snapshot:
- `manuscript/current/paper4-nrr-ime-v67.tex`
- `manuscript/current/paper4-nrr-ime-v67.pdf`
- `manuscript/current/fig1_design_space.png`
- `manuscript/current/fig2_bangbang.png`
- `manuscript/current/fig3_comparative.png`
- `manuscript/current/fig4_stability.png`
- `manuscript/current/checksums_sha256.txt`

Publication posting timeline may differ by platform availability.

## Repository Structure

```
nrr-ime/
|-- README.md
|-- LICENSE
|-- requirements.txt
|-- reproducibility.md
|-- manuscript/
|   `-- current/
|       |-- paper4-nrr-ime-v67.tex
|       |-- paper4-nrr-ime-v67.pdf
|       |-- fig1_design_space.png
|       |-- fig2_bangbang.png
|       |-- fig3_comparative.png
|       |-- fig4_stability.png
|       `-- checksums_sha256.txt
|-- experiments/
|   |-- experimental_data.json
|   |-- generate_figures.py
|   |-- paper4_crossmodel_v5.ipynb
|   |-- phase_comparison.py
|   `-- scaling_validation.py
`-- .gitignore
```

## Quick Start

```bash
pip install -r requirements.txt
bash scripts/generate_manuscript_figures.sh
python3 experiments/phase_comparison.py
python3 experiments/scaling_validation.py
```

The bundled `experiments/experimental_data.json` is the merged Paper 4 experiment
dataset used for the current manuscript line. It includes the 135 run-level records
used by the repository comparison scripts. Full provider-side infrastructure logs are
not bundled in this snapshot.

`experiments/generate_figures.py` regenerates the four manuscript figure PNGs from
the bundled merged dataset. The stable wrapper writes to a temp output directory by
default so the tracked review package remains unchanged.

The main experiment implementation used for this dataset is bundled as
`experiments/paper4_crossmodel_v5.ipynb`.

## Reproducibility

See `reproducibility.md` for fixed settings and artifact mapping.

Stable review-package entrypoints:
- `bash scripts/generate_manuscript_figures.sh`
- `bash scripts/build_current_manuscript.sh`
- `bash scripts/verify_current_package.sh`

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

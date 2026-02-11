# NRR-IME: Structure-Aware Optimization for Stateful Reasoning on Stateless LLM APIs

Reference implementation for the paper:

**"NRR-IME: Structure-Aware Optimization for Stateful Reasoning on Stateless LLM APIs"**  
Kei Saito (2026)  
*Manuscript in preparation* (arXiv submission pending)

Part of the Non-Resolution Reasoning (NRR) research program.
Program Map (series hub): [NRR Program Map](https://github.com/kei-saito-research/nrr-core/blob/main/PROGRAM_MAP.md)

---

## Overview

This repository contains the experimental validation code for NRR-IME (Interpretation Management Engine), demonstrating:

- **135 experimental runs** (45 configurations x 3 trials) across Claude Sonnet 4, GPT-4o-mini, and Gemini 2.0 Flash
- **Phase 1.5 reliability**: 100% operator extraction across all 9 model-scenario combinations (27 runs)
- **Structural stability** at temperature 0.3: max observed std = 0.5 tokens (all other configurations std = 0)
- **Cross-scenario stability**: 89.8-110.8 tokens/turn across Bank/Spring/Court (all models, std ≤ 0.5)

---

## Repository Structure

```
nrr-ime/
├── README.md                    # This file
├── requirements.txt             # Python dependencies
├── experiments/
│   ├── phase_comparison.py      # Phase 1.0 vs 1.5 vs 3.0 comparison
│   ├── scaling_validation.py    # Cross-scenario validation
│   └── experimental_data.json   # Complete experimental results
└── figures/
    ├── generate_fig1.py         # Phase comparison chart
    └── generate_fig2.py         # Scaling validation chart
```

---

## Quick Start

### Installation

```bash
pip install -r requirements.txt
```

### Run Experiments

**Phase Comparison (Bank scenario):**
```bash
python experiments/phase_comparison.py
```

**Scaling Validation (3 scenarios):**
```bash
python experiments/scaling_validation.py
```

### Generate Figures

```bash
python figures/generate_fig1.py  # Phase comparison chart
python figures/generate_fig2.py  # Scaling validation chart
```

Figures will be saved in the `figures/` directory.

---

## Experimental Data

All experimental results are stored in `experiments/experimental_data.json`:

- 135 runs (45 configurations x 3 trials)
- Three scenarios (Bank, Spring, Court) across three models
- Turn-by-turn token consumption and variance
- Operator extraction statistics and phase-wise failure modes

---

## Key Results (Paper-Aligned)

- **Protocol**: 135 runs (45 configurations x 3 trials), 3 models, temperature 0.3
- **Phase 1.5 extraction**: 100% across all 9 model-scenario combinations (27 runs)
- **Structural stability**: max observed std = 0.5 tokens (all others std = 0)
- **Phase 1.5 per-turn band**: 89.8-110.8 tokens/turn across all model-scenario combinations

### Phase 1.5 Totals by Model (mean ± std, 3 trials)

| Model | Bank (5t) | Spring (10t) | Court (12t) | Extract |
|-------|-----------|--------------|-------------|---------|
| Claude | 513 ± 0 | 1108 ± 0 | 1316 ± 0 | 100% |
| GPT | 449 ± 0 | 987 ± 0 | 1181 ± 0 | 100% |
| Gemini | 458 ± 0 | 978 ± 0 | 1179.3 ± 0.5 | 100% |

### Comparative Summary (Bank scenario, Claude, mean across 3 trials)

| Phase | Tokens | Std | Extract | NRR OK? | Failure mode |
|------|--------|-----|---------|---------|--------------|
| 1.0 | 734 | ±29 | --- | Partial | Output variance |
| 1.3 | 448 | ±0 | 100% | No | Bang-bang oscillation |
| 1.5 | 513 | ≤0.5 | 100% | Yes | None |
| 1.6 | 707 | ±54 | 0% | No | Extraction failure |
| 2.0 | 429 | ±0 | --- | No | Semantic collapse |
| 3.0e | 102 | ±0 | 80%* | Conditional | Input dependency |
| 3.0a | 525 | ±0 | 0%* | Yes | Reverts to 1.5 |

*For Phase 3.0, extraction indicates automation rate, not operator extraction.

---

## Citation

If you use this code, please cite:

```bibtex
@article{saito2026ime,
  title={NRR-IME: Structure-Aware Optimization for Stateful Reasoning on Stateless LLM APIs},
  author={Saito, Kei},
  journal={arXiv preprint},
  year={2026},
  note={Manuscript in preparation}
}
```

---

## Related Repositories

- [NRR-Core](https://github.com/kei-saito-research/nrr-core) - Foundational framework
- [NRR-Phi](https://github.com/kei-saito-research/nrr-phi) - Text-to-state mapping
- [NRR-Transfer](https://github.com/kei-saito-research/nrr-transfer) - Cross-domain transfer validation

---

## Reproducibility

See [`reproducibility.md`](./reproducibility.md) for environment, fixed settings, runnable commands, and artifact mapping.

---

## Commercial Use

If you plan to use this in a commercial or production setting,
a short message would be appreciated.

## License

CC BY 4.0 License. See [LICENSE](LICENSE).

---

## Reproduction & Issue Reports

If you reproduce results, find discrepancies, or hit bugs, please open an issue:
- https://github.com/kei-saito-research/nrr-ime/issues

Please include:
- environment (OS, Python version)
- command you ran
- commit hash (if applicable)
- observed output/error logs

---

## Contact

Kei Saito  
Independent Researcher, Japan  
ORCID: [0009-0006-4715-9176](https://orcid.org/0009-0006-4715-9176)  
Email: kei.saito.research@gmail.com

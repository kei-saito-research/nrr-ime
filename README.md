# NRR-IME: Interpretation Management Engine

Reference implementation for Non-Resolution Reasoning (NRR) Interpretation Management Engine (IME) from:

**Saito, K. (2026). Computational Efficiency of Non-Resolution Reasoning: Structure-Aware Optimization for Stateless LLM APIs.** *arXiv preprint* arXiv:XXXX.XXXXX.

## Overview

This repository provides experimental validation for Phase 1.5 (Operator-based NRR) architecture, demonstrating **69.5% token reduction** compared to naive implementation while maintaining ambiguity preservation.

### Key Results

- **Phase 1.0 (Naive)**: 1431 tokens → 286.2 tokens/turn
- **Phase 1.5 (Operator)**: 436 tokens → **87.2 tokens/turn** (-69.5%)
- **Phase 3.0 (Hybrid)**: 56 tokens → 11.2 tokens/turn (domain-specific only)

## Experimental Scenarios

### IME Domain (Ambiguous Word Disambiguation)
1. **Bank** (5 turns): financial institution / riverbank / verb
2. **Spring** (10 turns): season / water source / mechanical spring
3. **Court** (12 turns): legal court / sports court / royal court

## Repository Structure
```
nrr-ime/
├── experiments/
│   ├── phase_comparison.ipynb       # Phase 1.0-3.0 comparison
│   ├── phase15_vs_30.ipynb          # Phase 1.5 vs 3.0 detailed analysis
│   └── README.md
├── data/
│   ├── phase_comparison.json        # Full experimental results
│   └── phase15_vs_30.json           # Phase comparison data
└── README.md
```

## Quick Start

### View Experimental Results
```bash
# Clone repository
git clone https://github.com/kei-saito-research/nrr-ime.git
cd nrr-ime

# Open Jupyter notebooks
jupyter notebook experiments/phase_comparison.ipynb
```

### Key Findings

1. **Operator abstraction** enables 69.5% token reduction
2. **Phase 1.5 stability**: Consistent performance across all ambiguity types
3. **Phase 3.0 fragility**: 100% LLM fallback with ambiguous expressions

## Data Files

- `phase_comparison.json`: Complete Phase 1.0-3.0 experimental data
- `phase15_vs_30.json`: Explicit vs ambiguous expression comparison

## Citation
```bibtex
@article{saito2026ime,
  title={Computational Efficiency of Non-Resolution Reasoning: Structure-Aware Optimization for Stateless LLM APIs},
  author={Saito, Kei},
  journal={arXiv preprint arXiv:XXXX.XXXXX},
  year={2026}
}
```

## License

CC BY 4.0

## Related Papers

- **Paper 1**: [arXiv:2512.13478](https://arxiv.org/abs/2512.13478) - NRR Framework
- **Paper 2**: [arXiv:2601.19933](https://arxiv.org/abs/2601.19933) - Text-to-State Mapping
- **Paper 3**: arXiv:XXXX.XXXXX - Operator Design Principles
- **Paper 4**: arXiv:XXXX.XXXXX (this paper) - Computational Efficiency
- **Paper 5**: arXiv:XXXX.XXXXX - Cross-Domain Generalization

## Related Repositories

- [nrr-operators](https://github.com/kei-saito-research/nrr-operators) - Operator implementation (Paper 3)
- [nrr-phase15](https://github.com/kei-saito-research/nrr-phase15) - Cross-domain validation (Paper 5)

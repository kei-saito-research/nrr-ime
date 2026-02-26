# Reproducibility

## Environment
- Python: 3.13.7 (`python3`)
- Main libraries: NumPy >= 1.21.0, Matplotlib >= 3.5.0
- OS: Darwin 25.2.0 arm64

## Fixed settings
- model: Claude Sonnet 4, GPT-4o-mini, Gemini 2.0 Flash (paper protocol)
- seed: N/A (dataset replay from fixed experimental logs)
- temperature: main = 0.3 (Phase 1.5); comparative settings included in dataset
- trials: 3 trials per configuration in the published dataset

## Run commands
```bash
pip install -r requirements.txt
python3 experiments/phase_comparison.py
python3 experiments/scaling_validation.py
python3 figures/generate_fig1.py
python3 figures/generate_fig2.py
```

## Artifact map
| Table/Figure | Command | Output file |
|---|---|---|
| Phase comparison figure (repo figure set) | `python3 figures/generate_fig1.py` | `figures/figure1_phase_comparison.png` |
| Scaling validation figure (repo figure set) | `python3 figures/generate_fig2.py` | `figures/figure2_scaling_validation.png` |
| Phase comparison summary table values | `python3 experiments/phase_comparison.py` | `stdout` (use terminal log) |
| Moderation manuscript source snapshot | N/A (tracked artifact) | `manuscript/v61/paper4-nrr-ime-v61.tex` |
| Moderation manuscript figure snapshot | N/A (tracked artifact) | `manuscript/v61/fig1_design_space.png` ... `manuscript/v61/fig4_stability.png` |

## Known limitations
- Experimental scripts replay fixed JSON logs; they do not re-query external APIs.
- Provider tokenizer/version drift is not re-measured by this offline package.

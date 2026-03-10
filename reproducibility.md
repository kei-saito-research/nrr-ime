# Reproducibility (NRR-IME snapshot)

## Scope

This repository snapshot provides experiment scripts plus the current manuscript package.
Primary manuscript artifacts are in `manuscript/current/`.

## Environment
- Python: 3.10+
- Libraries: `requirements.txt`
  - numpy
  - matplotlib

## Fixed protocol summary
- Models in the IME study: Claude Sonnet 4, GPT-4o-mini, Gemini 2.0 Flash
- Main temperature setting in manuscript protocol: 0.3
- Trial design in manuscript protocol: 3 trials per configuration

## Run commands
```bash
pip install -r requirements.txt
bash scripts/generate_manuscript_figures.sh
python3 experiments/phase_comparison.py
python3 experiments/scaling_validation.py
```

## Bundled experiment data
- `experiments/experimental_data.json` contains the merged Paper 4 experiment dataset for the current manuscript line.
- `experiments/paper4_crossmodel_v5.ipynb` contains the main experiment runner used to generate that dataset.
- `experiments/generate_figures.py` regenerates the four manuscript figure PNGs from the bundled dataset.
- The included scripts reproduce repository comparison outputs from those 135 run-level records.
- This snapshot does not bundle provider-side infrastructure logs outside the merged dataset.

## Field name mapping

| Manuscript term | JSON field | JSON level |
|---|---|---|
| semantic collapse rate | `single_rate` | experiment |
| weight volatility | `weight_volatility` | experiment |
| operator / target | `operator`, `target` | turn |
| returned single | `returned_single` | turn (Phase 2.0) |

## Manuscript package
- Main TeX: `manuscript/current/paper4-nrr-ime-v67.tex`
- PDF snapshot: `manuscript/current/paper4-nrr-ime-v67.pdf`
- Figures: `manuscript/current/fig1_design_space.png` to `fig4_stability.png`
- Checksums: `manuscript/current/checksums_sha256.txt`

Stable review-package commands:
- Figure sync: `bash scripts/generate_manuscript_figures.sh`
- Build current manuscript to temp output: `bash scripts/build_current_manuscript.sh`
- Verify current package checksums: `bash scripts/verify_current_package.sh`

## Artifact map
| Artifact | Command | Output |
|---|---|---|
| Figure 1-4 regeneration | `bash scripts/generate_manuscript_figures.sh` | `/tmp/nrr-ime_current_figures/fig1_design_space.png` to `fig4_stability.png` |
| Phase comparison summary | `python3 experiments/phase_comparison.py` | stdout summary from `experiments/experimental_data.json` |
| Scaling validation summary | `python3 experiments/scaling_validation.py` | stdout summary from `experiments/experimental_data.json` |
| Current manuscript build | `bash scripts/build_current_manuscript.sh` | `/tmp/nrr-ime_current_build/paper4-nrr-ime-v67.pdf` |
| Current package checksum verification | `bash scripts/verify_current_package.sh` | stdout verification for `manuscript/current/checksums_sha256.txt` |

## Output policy
- The current manuscript package bundles a fixed snapshot of Figure 1-4 under `manuscript/current/`.
- Local figure reruns may produce PNG files that are visually aligned but not bit-for-bit identical to the bundled snapshot, so the stable wrapper writes reruns to `/tmp/nrr-ime_current_figures` by default.
- Generated outputs from local execution beyond the bundled figure snapshot are not included in this repository snapshot.
- Full raw run logs may be hosted separately from this repository.

## Known limitations
- Scripts in this snapshot run against the bundled merged experiment dataset.
- Figure regeneration is supported from the bundled dataset, but PNG byte-level output can vary slightly across local environments.
- Provider-side model updates may affect rerun values.

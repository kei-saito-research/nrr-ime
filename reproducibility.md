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
python3 experiments/phase_comparison.py
python3 experiments/scaling_validation.py
```

## Bundled experiment data
- `experiments/experimental_data.json` contains the merged Paper 4 experiment dataset for the current manuscript line.
- The included scripts reproduce repository comparison outputs from those 135 run-level records.
- This snapshot does not bundle provider-side infrastructure logs outside the merged dataset.

## Manuscript package
- Main TeX: `manuscript/current/paper4-nrr-ime-v67.tex`
- PDF snapshot: `manuscript/current/paper4-nrr-ime-v67.pdf`
- Figures: `manuscript/current/fig1_design_space.png` to `fig4_stability.png`
- Checksums: `manuscript/current/checksums_sha256.txt`

## Output policy
- Generated outputs from local execution are not bundled in this repository snapshot.
- Full raw run logs may be hosted separately from this repository.

## Known limitations
- Scripts in this snapshot run against the bundled merged experiment dataset.
- Provider-side model updates may affect rerun values.

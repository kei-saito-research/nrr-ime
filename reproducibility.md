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

## Manuscript package
- Main TeX: `manuscript/current/paper4-nrr-ime-v64.tex`
- PDF snapshot: `manuscript/current/paper4-nrr-ime-v64.pdf`
- Figures: `manuscript/current/fig1_design_space.png` to `fig4_stability.png`
- Checksums: `manuscript/current/checksums_sha256.txt`

## Output policy
- Generated outputs from local execution are not bundled in this repository snapshot.
- Full raw run logs may be hosted separately from this repository.

## Known limitations
- Scripts in this snapshot do not include bundled full result logs.
- Provider-side model updates may affect rerun values.

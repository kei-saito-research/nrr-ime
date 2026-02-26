# Reproducibility (NRR-IME pre-submission snapshot)

## Scope

This repository snapshot provides core experiment scripts only.
Manuscript text files and full result artifacts are intentionally excluded while IME is under moderation.

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

## Output policy
- Generated outputs from local execution are private pre-submission artifacts.
- Public release of full outputs is deferred until IME moderation/publication is resolved.

## Known limitations
- Scripts in this snapshot do not include bundled full result logs.
- Provider-side model updates may affect rerun values.

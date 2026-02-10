#!/usr/bin/env python3
"""
Phase Comparison: Phase 1.0 vs 1.5 vs 3.0
Bank scenario (5 turns), Claude mean across 3 trials
"""

import json
import os
from statistics import mean


def load_experimental_data():
    data_path = os.path.join(os.path.dirname(__file__), 'experimental_data.json')
    with open(data_path, 'r', encoding='utf-8') as f:
        return json.load(f)


def select_runs(data, phase, scenario, model='claude', mode=None):
    runs = []
    for exp in data.get('experiments', []):
        if exp.get('phase') != phase:
            continue
        if exp.get('scenario') != scenario:
            continue
        if exp.get('model') != model:
            continue
        if mode is not None and exp.get('mode') != mode:
            continue
        runs.append(exp)
    if not runs:
        raise ValueError(f'No runs for phase={phase}, scenario={scenario}, model={model}, mode={mode}')
    return runs


def summarize_runs(runs):
    totals = [r['total_tokens'] for r in runs]
    avgs = [r['avg_per_turn'] for r in runs]
    return {
        'total_tokens_mean': mean(totals),
        'avg_per_turn_mean': mean(avgs),
        'n_trials': len(runs),
    }


def compare_phases():
    data = load_experimental_data()

    phase_10 = summarize_runs(select_runs(data, phase='1.0', scenario='bank', model='claude'))
    phase_15 = summarize_runs(select_runs(data, phase='1.5', scenario='bank', model='claude'))
    phase_30 = summarize_runs(select_runs(data, phase='3.0', scenario='bank', model='claude', mode='explicit'))

    tokens_10 = phase_10['total_tokens_mean']
    tokens_15 = phase_15['total_tokens_mean']
    tokens_30 = phase_30['total_tokens_mean']

    reduction_15 = (tokens_10 - tokens_15) / tokens_10 * 100
    reduction_30 = (tokens_10 - tokens_30) / tokens_10 * 100

    print('=' * 60)
    print('Phase Comparison: Bank Scenario (Claude, mean across 3 trials)')
    print('=' * 60)
    print()

    print('Phase 1.0 (Naive):')
    print(f"  Total tokens: {tokens_10:.1f}")
    print(f"  Avg per turn: {phase_10['avg_per_turn_mean']:.1f}")
    print()

    print('Phase 1.5 (Operators):')
    print(f"  Total tokens: {tokens_15:.1f}")
    print(f"  Avg per turn: {phase_15['avg_per_turn_mean']:.1f}")
    print(f"  Reduction: -{reduction_15:.1f}%")
    print()

    print('Phase 3.0 (Zero-LLM Explicit):')
    print(f"  Total tokens: {tokens_30:.1f}")
    print(f"  Avg per turn: {phase_30['avg_per_turn_mean']:.1f}")
    print(f"  Reduction: -{reduction_30:.1f}%")
    print()

    print('=' * 60)
    print('Summary')
    print('=' * 60)
    print(f'Phase 1.0 -> 1.5: {reduction_15:.1f}% reduction')
    print(f'Phase 1.0 -> 3.0: {reduction_30:.1f}% reduction')
    print()

    return {
        'phase_10': tokens_10,
        'phase_15': tokens_15,
        'phase_30': tokens_30,
        'reduction_15': reduction_15,
        'reduction_30': reduction_30,
    }


if __name__ == '__main__':
    compare_phases()

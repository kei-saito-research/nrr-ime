#!/usr/bin/env python3
"""
Generate Figure 1: Phase Comparison Chart
Bank scenario, Claude mean across 3 trials
"""

import json
import os
from statistics import mean

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt


def load_experimental_data():
    exp_path = os.path.join(os.path.dirname(__file__), '..', 'experiments', 'experimental_data.json')
    with open(exp_path, 'r', encoding='utf-8') as f:
        return json.load(f)


def select_mean_total(data, phase, scenario, model='claude', mode=None):
    vals = []
    for exp in data.get('experiments', []):
        if exp.get('phase') != phase:
            continue
        if exp.get('scenario') != scenario:
            continue
        if exp.get('model') != model:
            continue
        if mode is not None and exp.get('mode') != mode:
            continue
        vals.append(exp['total_tokens'])
    if not vals:
        raise ValueError(f'No values for phase={phase}, scenario={scenario}, model={model}, mode={mode}')
    return mean(vals)


def generate_figure1():
    data = load_experimental_data()

    phase_10 = select_mean_total(data, '1.0', 'bank', model='claude')
    phase_15 = select_mean_total(data, '1.5', 'bank', model='claude')
    phase_30 = select_mean_total(data, '3.0', 'bank', model='claude', mode='explicit')

    reduction_15 = (phase_10 - phase_15) / phase_10 * 100
    reduction_30 = (phase_10 - phase_30) / phase_10 * 100

    fig, ax = plt.subplots(1, 1, figsize=(10, 6))

    phases = ['Phase 1.0\n(Naive)', 'Phase 1.5\n(Operators)', 'Phase 3.0\n(Zero-LLM\nExplicit)']
    tokens = [phase_10, phase_15, phase_30]
    colors = ['#e74c3c', '#3498db', '#2ecc71']

    bars = ax.bar(phases, tokens, color=colors, alpha=0.8, edgecolor='black', linewidth=1.5)

    for bar, token in zip(bars, tokens):
        height = bar.get_height()
        ax.text(
            bar.get_x() + bar.get_width() / 2.0,
            height + 30,
            f'{token:.0f}\ntokens',
            ha='center',
            va='bottom',
            fontsize=12,
            fontweight='bold',
        )

    ax.text(
        0.5,
        phase_10 * 0.6,
        f'-{reduction_15:.1f}%',
        ha='center',
        fontsize=14,
        fontweight='bold',
        color='white',
        bbox=dict(boxstyle='round', facecolor='#3498db', alpha=0.8),
    )

    ax.text(
        1.5,
        phase_10 * 0.3,
        f'-{reduction_30:.1f}%',
        ha='center',
        fontsize=14,
        fontweight='bold',
        color='white',
        bbox=dict(boxstyle='round', facecolor='#2ecc71', alpha=0.8),
    )

    ax.set_ylabel('Total Tokens (5 turns)', fontsize=14, fontweight='bold')
    ax.set_title('IME Token Consumption: Phase Comparison (Bank Scenario, Claude mean)', fontsize=16, fontweight='bold', pad=20)
    ax.set_ylim(0, 1400)
    ax.grid(axis='y', alpha=0.3, linestyle='--')

    plt.tight_layout()

    output_path = os.path.join(os.path.dirname(__file__), 'figure1_phase_comparison.png')
    plt.savefig(output_path, dpi=300, bbox_inches='tight')
    print(f'✓ Figure 1 saved to {output_path}')
    plt.close()


if __name__ == '__main__':
    generate_figure1()

#!/usr/bin/env python3
"""
Generate Figure 2: Scaling Validation Chart
Phase 1.5, Claude mean across 3 trials
"""

import json
import os
from statistics import mean

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np


def load_experimental_data():
    exp_path = os.path.join(os.path.dirname(__file__), '..', 'experiments', 'experimental_data.json')
    with open(exp_path, 'r', encoding='utf-8') as f:
        return json.load(f)


def select_runs(data, phase, scenario, model='claude'):
    return [
        exp for exp in data.get('experiments', [])
        if exp.get('phase') == phase
        and exp.get('scenario') == scenario
        and exp.get('model') == model
    ]


def mean_totals_and_avgs(runs):
    if not runs:
        raise ValueError('No runs found')
    return mean([r['total_tokens'] for r in runs]), mean([r['avg_per_turn'] for r in runs])


def generate_figure2():
    data = load_experimental_data()

    scenarios = ['bank', 'spring', 'court']
    labels = ['Bank\n(5 turns)', 'Spring\n(10 turns)', 'Court\n(12 turns)']

    scenario_tokens = []
    avg_per_turn = []
    for sc in scenarios:
        runs = select_runs(data, phase='1.5', scenario=sc, model='claude')
        total_m, avg_m = mean_totals_and_avgs(runs)
        scenario_tokens.append(total_m)
        avg_per_turn.append(avg_m)

    fig, ax = plt.subplots(1, 1, figsize=(10, 6))

    x = np.arange(len(labels))
    width = 0.35

    bars1 = ax.bar(
        x - width / 2,
        scenario_tokens,
        width,
        label='Total Tokens',
        color='#3498db',
        alpha=0.8,
        edgecolor='black',
        linewidth=1.5,
    )
    ax2 = ax.twinx()
    ax2.plot(
        x,
        avg_per_turn,
        'o-',
        color='#e74c3c',
        linewidth=3,
        markersize=12,
        label='Avg per Turn',
        markeredgecolor='black',
        markeredgewidth=1.5,
    )

    for i, (bar, token, avg) in enumerate(zip(bars1, scenario_tokens, avg_per_turn)):
        height = bar.get_height()
        ax.text(bar.get_x() + bar.get_width() / 2.0, height + 30, f'{token:.0f}', ha='center', va='bottom', fontsize=11, fontweight='bold')
        ax2.text(i, avg + 2, f'{avg:.1f}', ha='center', va='bottom', fontsize=11, fontweight='bold', color='#c0392b')

    ax.set_xlabel('Scenario', fontsize=14, fontweight='bold')
    ax.set_ylabel('Total Tokens', fontsize=14, fontweight='bold', color='#3498db')
    ax2.set_ylabel('Avg Tokens per Turn', fontsize=14, fontweight='bold', color='#e74c3c')
    ax.set_title('Phase 1.5 Scaling Validation (Claude mean across 3 trials)', fontsize=16, fontweight='bold', pad=20)
    ax.set_xticks(x)
    ax.set_xticklabels(labels)
    ax.tick_params(axis='y', labelcolor='#3498db')
    ax2.tick_params(axis='y', labelcolor='#e74c3c')
    ax.set_ylim(0, 1400)
    ax2.set_ylim(0, 130)
    ax.grid(axis='y', alpha=0.3, linestyle='--')

    lines1, labels1 = ax.get_legend_handles_labels()
    lines2, labels2 = ax2.get_legend_handles_labels()
    ax.legend(lines1 + lines2, labels1 + labels2, loc='upper left', fontsize=11)

    plt.tight_layout()

    output_path = os.path.join(os.path.dirname(__file__), 'figure2_scaling_validation.png')
    plt.savefig(output_path, dpi=300, bbox_inches='tight')
    print(f'✓ Figure 2 saved to {output_path}')
    plt.close()


if __name__ == '__main__':
    generate_figure2()

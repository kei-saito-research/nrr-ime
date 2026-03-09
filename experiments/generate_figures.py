#!/usr/bin/env python3
"""
Generate manuscript figures (fig1-fig4) from experimental_data.json.

Usage:
    python3 experiments/generate_figures.py
    python3 experiments/generate_figures.py --output-dir experiments

Reads:
    experiments/experimental_data.json

Writes by default:
    manuscript/current/fig1_design_space.png
    manuscript/current/fig2_bangbang.png
    manuscript/current/fig3_comparative.png
    manuscript/current/fig4_stability.png
"""

from __future__ import annotations

import argparse
import json
import math
import os
import sys
from collections import defaultdict
from pathlib import Path
from statistics import mean

import matplotlib.patches as mpatches
import matplotlib.pyplot as plt
import numpy as np


SCRIPT_DIR = Path(__file__).resolve().parent
REPO_ROOT = SCRIPT_DIR.parent
DATA_PATH = SCRIPT_DIR / "experimental_data.json"
DEFAULT_OUTPUT_DIR = REPO_ROOT / "manuscript" / "current"


def load_data() -> dict:
    with DATA_PATH.open("r", encoding="utf-8") as f:
        return json.load(f)


def group_experiments(data: dict) -> dict:
    groups = defaultdict(list)
    for experiment in data["experiments"]:
        key = (
            experiment["phase"],
            experiment["model"],
            experiment["scenario"],
            experiment.get("mode", ""),
        )
        groups[key].append(experiment)
    return groups


def pop_stats(values: list[float]) -> tuple[float, float]:
    if not values:
        return 0.0, 0.0
    mu = mean(values)
    var = sum((x - mu) ** 2 for x in values) / len(values)
    return mu, math.sqrt(var)


MODEL_COLORS = {
    "claude": "#7c3aed",
    "gpt": "#0ea5e9",
    "gemini": "#f59e0b",
}

MODEL_LABELS = {
    "claude": "Claude Sonnet 4",
    "gpt": "GPT-4o-mini",
    "gemini": "Gemini 2.0 Flash",
}

MODELS = ["claude", "gpt", "gemini"]


plt.rcParams.update(
    {
        "font.size": 11,
        "font.family": "serif",
        "axes.labelsize": 12,
        "axes.titlesize": 13,
        "figure.dpi": 300,
    }
)


def generate_fig1(output_dir: Path) -> None:
    fig, ax = plt.subplots(figsize=(9, 4.2))
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis("off")

    phases = [
        ("1.0", "Full JSON", "Full JSON", "Output variance", "fail"),
        ("1.3", "Labels only", "Numeric weights", "Bang-bang oscillation", "partial"),
        ("1.5", "Labels only", "Binary operator", "None (Optimal)", "optimal"),
        ("1.6", "Minimal", "Binary operator", "Extraction failure", "fail"),
        ("2.0", "Labels only", "Single interp.", "Semantic collapse", "partial"),
        ("3.0", "Keywords+LLM", "Auto / Operator", "Input dependency", "partial"),
    ]

    status_colors = {
        "optimal": ("#d3f9d8", "#2b8a3e"),
        "partial": ("#fff3e0", "#e67e22"),
        "fail": ("#ffebee", "#c0392b"),
    }

    col_x = [0.03, 0.15, 0.37, 0.59, 0.82]
    y_header = 0.94
    row_h = 0.125
    y_first = y_header - 0.07

    headers = ["Phase", "State Sent", "LLM Returns", "Failure Mode"]
    for txt, cx in zip(headers, col_x):
        ax.text(
            cx,
            y_header,
            txt,
            fontweight="bold",
            fontsize=10.5,
            va="top",
            transform=ax.transAxes,
        )
    ax.plot(
        [0.01, 0.99],
        [y_header - 0.04, y_header - 0.04],
        color="#333",
        linewidth=1.2,
        transform=ax.transAxes,
    )

    for i, (phase, sent, returns, failure, status) in enumerate(phases):
        y_top = y_first - i * row_h
        y_bot = y_top - row_h + 0.02
        y_mid = (y_top + y_bot) / 2
        bg, edge = status_colors[status]

        rect = mpatches.FancyBboxPatch(
            (0.01, y_bot),
            0.98,
            row_h - 0.02,
            boxstyle="round,pad=0.008",
            facecolor=bg,
            edgecolor=edge if status == "optimal" else "#999",
            linewidth=2.0 if status == "optimal" else 0.8,
            transform=ax.transAxes,
        )
        ax.add_patch(rect)

        weight = "bold" if status == "optimal" else "normal"
        ax.text(
            col_x[0],
            y_mid,
            f"Phase {phase}",
            fontweight="bold",
            fontsize=10,
            va="center",
            transform=ax.transAxes,
        )
        ax.text(
            col_x[1],
            y_mid,
            sent,
            fontweight=weight,
            fontsize=10,
            va="center",
            transform=ax.transAxes,
        )
        ax.text(
            col_x[2],
            y_mid,
            returns,
            fontweight=weight,
            fontsize=10,
            va="center",
            transform=ax.transAxes,
        )
        ax.text(
            col_x[3],
            y_mid,
            failure,
            fontsize=10,
            va="center",
            color=edge,
            fontweight=weight,
            fontstyle="italic",
            transform=ax.transAxes,
        )

    legend_y = 0.03
    legend_items = [
        (0.28, "Optimal", "#d3f9d8", "#2b8a3e"),
        (0.46, "Partial failure", "#fff3e0", "#e67e22"),
        (0.68, "Complete failure", "#ffebee", "#c0392b"),
    ]
    for lx, label, fc, ec in legend_items:
        rect = mpatches.FancyBboxPatch(
            (lx - 0.02, legend_y - 0.01),
            0.025,
            0.025,
            boxstyle="round,pad=0.003",
            facecolor=fc,
            edgecolor=ec,
            transform=ax.transAxes,
        )
        ax.add_patch(rect)
        ax.text(lx + 0.015, legend_y, label, fontsize=9, va="center", transform=ax.transAxes)

    ax.set_title(
        "Figure 1: Design Space of Implementation Strategies",
        fontsize=13,
        fontweight="bold",
        pad=12,
    )

    out = output_dir / "fig1_design_space.png"
    plt.savefig(out, dpi=300, bbox_inches="tight", facecolor="white")
    plt.close()
    print(f"  {out}")


def generate_fig2(groups: dict, output_dir: Path) -> None:
    fig, axes = plt.subplots(1, 3, figsize=(12, 3.5), sharey=True)
    fig.suptitle(
        "Figure 2: Phase 1.3 Weight Trajectories (Bang-Bang Oscillation)",
        fontsize=13,
        fontweight="bold",
    )

    for idx, model in enumerate(MODELS):
        ax = axes[idx]
        experiments = groups.get(("1.3", model, "bank", ""), [])
        trial1 = [e for e in experiments if e.get("trial") == 1]
        if not trial1:
            continue
        experiment = trial1[0]

        turns_data = experiment["turns"]
        turn_nums = [turn["turn"] for turn in turns_data]
        fin_weights = [turn["parsed_weights"]["financial"] for turn in turns_data]
        riv_weights = [turn["parsed_weights"]["river"] for turn in turns_data]

        color = MODEL_COLORS[model]
        ax.plot(
            turn_nums,
            fin_weights,
            "o-",
            color=color,
            label="financial",
            linewidth=2,
            markersize=7,
        )
        ax.plot(
            turn_nums,
            riv_weights,
            "s--",
            color=color,
            label="river",
            linewidth=2,
            markersize=7,
            alpha=0.6,
        )
        ax.axhline(y=0.5, color="#aaa", linestyle=":", linewidth=0.8)

        vols = [exp.get("weight_volatility", 0) for exp in experiments]
        vol_mean, _ = pop_stats(vols)
        ax.set_title(f"{MODEL_LABELS[model]}\nvolatility={vol_mean:.2f}", fontsize=10)
        ax.set_xlabel("Turn")
        ax.set_ylim(-0.05, 1.05)
        ax.set_xticks(range(1, 6))
        if idx == 0:
            ax.set_ylabel("Weight")
            ax.legend(fontsize=8, loc="center right")

    plt.tight_layout()
    out = output_dir / "fig2_bangbang.png"
    plt.savefig(out, dpi=300, bbox_inches="tight", facecolor="white")
    plt.close()
    print(f"  {out}")


def generate_fig3(groups: dict, output_dir: Path) -> None:
    fig, ax = plt.subplots(figsize=(10, 5))

    phases_plot = ["1.0", "1.3", "1.5", "1.6", "2.0"]
    x = np.arange(len(phases_plot))
    width = 0.25

    for i, model in enumerate(MODELS):
        means, stds = [], []
        for phase in phases_plot:
            experiments = groups.get((phase, model, "bank", ""), [])
            totals = [exp["total_tokens"] for exp in experiments]
            mu, sd = pop_stats(totals)
            means.append(mu)
            stds.append(sd)
        ax.bar(
            x + i * width,
            means,
            width,
            yerr=stds,
            label=MODEL_LABELS[model],
            color=MODEL_COLORS[model],
            alpha=0.85,
            capsize=3,
            edgecolor="white",
            linewidth=0.5,
        )

    annotations = {
        0: ("Output\nvariance", "#c0392b"),
        1: ("Bang-bang\noscillation", "#e67e22"),
        3: ("Extraction\nfailure", "#c0392b"),
        4: ("Semantic\ncollapse", "#e67e22"),
    }
    for idx, (text, color) in annotations.items():
        ax.annotate(
            text,
            xy=(idx + width, 50),
            fontsize=7.5,
            ha="center",
            color=color,
            fontweight="bold",
            fontstyle="italic",
        )

    ax.axvspan(1.7, 3.3, alpha=0.08, color="green")
    ax.annotate("OPTIMAL", xy=(2 + width, 560), fontsize=9, ha="center", color="#2b8a3e", fontweight="bold")

    ax.set_xlabel("Phase")
    ax.set_ylabel("Total Tokens (Bank, 5 turns)")
    ax.set_title("Figure 3: Token Consumption by Phase (mean +/- std, n=3)", fontsize=13, fontweight="bold")
    ax.set_xticks(x + width)
    ax.set_xticklabels([f"Phase {phase}" for phase in phases_plot])
    ax.legend(loc="upper right")
    ax.set_ylim(0, 1000)

    plt.tight_layout()
    out = output_dir / "fig3_comparative.png"
    plt.savefig(out, dpi=300, bbox_inches="tight", facecolor="white")
    plt.close()
    print(f"  {out}")


def generate_fig4(groups: dict, output_dir: Path) -> None:
    scenarios = ["bank", "spring", "court"]
    scenario_labels = [
        "Bank\n(5t, 2 interp)",
        "Spring\n(10t, 4 interp)",
        "Court\n(12t, 4 interp)",
    ]

    fig, ax = plt.subplots(figsize=(9, 5))
    x = np.arange(len(scenarios))
    width = 0.22
    gap = 0.03

    all_vals: dict[str, list[float]] = {}
    for i, model in enumerate(MODELS):
        avgs = []
        for scenario in scenarios:
            experiments = groups.get(("1.5", model, scenario, ""), [])
            vals = [exp["avg_per_turn"] for exp in experiments]
            mu, _ = pop_stats(vals)
            avgs.append(mu)
        offset = (i - 1) * (width + gap)
        ax.bar(
            x + offset,
            avgs,
            width,
            label=MODEL_LABELS[model],
            color=MODEL_COLORS[model],
            alpha=0.85,
            edgecolor="white",
            linewidth=0.5,
        )
        all_vals[model] = avgs

    for i, model in enumerate(MODELS):
        offset = (i - 1) * (width + gap)
        for j, value in enumerate(all_vals[model]):
            ax.text(
                x[j] + offset,
                value - 4,
                f"{value:.1f}",
                ha="center",
                va="top",
                fontsize=8,
                fontweight="bold",
                color="white",
            )

    ax.axhspan(89.8, 110.8, alpha=0.07, color="green", zorder=0)
    ax.annotate(
        "Stability band: 89.8 - 110.8 tok/turn\n(all std < 0.5 across 3 trials)",
        xy=(0.98, 0.97),
        xycoords="axes fraction",
        fontsize=9,
        ha="right",
        va="top",
        color="#2b8a3e",
        fontstyle="italic",
        bbox=dict(
            boxstyle="round,pad=0.4",
            facecolor="#d3f9d8",
            edgecolor="#2b8a3e",
            alpha=0.85,
        ),
    )

    ax.set_xlabel("Scenario")
    ax.set_ylabel("Avg Tokens / Turn")
    ax.set_title("Figure 4: Phase 1.5 Per-Turn Stability Across Scenarios", fontsize=13, fontweight="bold")
    ax.set_xticks(x)
    ax.set_xticklabels(scenario_labels)
    ax.legend(loc="lower left", fontsize=9, framealpha=0.9)
    ax.set_ylim(0, 135)

    plt.tight_layout()
    out = output_dir / "fig4_stability.png"
    plt.savefig(out, dpi=300, bbox_inches="tight", facecolor="white")
    plt.close()
    print(f"  {out}")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Generate IME manuscript figures from bundled experiment data.")
    parser.add_argument(
        "--output-dir",
        default=str(DEFAULT_OUTPUT_DIR),
        help="Directory for generated PNG files (default: manuscript/current).",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()

    if not DATA_PATH.exists():
        print(f"Error: {DATA_PATH} not found", file=sys.stderr)
        return 1

    output_dir = Path(args.output_dir).expanduser().resolve()
    output_dir.mkdir(parents=True, exist_ok=True)

    data = load_data()
    groups = group_experiments(data)

    print(f"Loaded {len(data['experiments'])} experiments from {DATA_PATH}")
    print(f"Writing figures to {output_dir}")

    generate_fig1(output_dir)
    generate_fig2(groups, output_dir)
    generate_fig3(groups, output_dir)
    generate_fig4(groups, output_dir)

    print("Done.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

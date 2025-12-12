"""
Visualization utilities for booking data.
These functions are intentionally minimal and act as placeholders
for participants to extend during PatchFest.
"""

import matplotlib.pyplot as plt
import pandas as pd
from pathlib import Path


PLOTS_DIR = Path("plots")


def plot_daily_booking_trend(df, date_col="date", count_col="count"):
    """
    Creates a simple line plot of booking counts over time.
    Parameters:
        df (pd.DataFrame): Data with date & count columns.
    """
    if date_col not in df.columns or count_col not in df.columns:
        print(f"[WARN] Columns '{date_col}' or '{count_col}' not found in dataframe.")
        return

    df_sorted = df.sort_values(date_col)
    plt.figure(figsize=(10, 4))
    plt.plot(df_sorted[date_col], df_sorted[count_col], linewidth=1.5)
    plt.title("Daily Booking Trend")
    plt.xlabel("Date")
    plt.ylabel("Ticket Count")
    plt.tight_layout()

    PLOTS_DIR.mkdir(exist_ok=True)
    output_path = PLOTS_DIR / "daily_trend.png"

    try:
        plt.savefig(output_path)
        print(f"[INFO] Plot saved at {output_path}")
    except Exception as e:
        print(f"[ERROR] Could not save plot: {e}")

    plt.close()


def plot_missing_value_heatmap(df):
    """
    Very minimal placeholder for missing-value visualization.
    Participants should enhance this (heatmap, colorbars, etc.).
    """
    missing = df.isna().mean()

    plt.figure(figsize=(8, 3))
    missing.plot(kind="bar")
    plt.title("Missing Value Ratio per Feature")
    plt.ylabel("Ratio")
    plt.tight_layout()

    output_path = PLOTS_DIR / "missing_value_ratio.png"
    PLOTS_DIR.mkdir(exist_ok=True)

    try:
        plt.savefig(output_path)
    except Exception:
        pass

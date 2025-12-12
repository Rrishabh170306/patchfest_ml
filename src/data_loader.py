"""
Basic data loading utilities for ticket data.
These functions are intentionally simplistic and require participants
to strengthen validation, error handling, and extensibility.
"""

import pandas as pd
from pathlib import Path


DATA_DIR = Path("data")
RAW_DIR = DATA_DIR / "raw"
PROCESSED_DIR = DATA_DIR / "processed"


def load_raw_images():
    """
    Returns a list of image file paths from data/raw/.
    Participants should extend this for validation and filtering.
    """
    if not RAW_DIR.exists():
        print(f"[WARN] Raw directory not found: {RAW_DIR}")
        return []

    image_files = []
    for ext in ("*.jpg", "*.png", "*.jpeg"):
        image_files.extend(RAW_DIR.glob(ext))

    return image_files


def load_processed_csv(filename="structured.csv"):
    """
    Loads processed CSV data.
    Participants must extend this for type casting & schema validation.
    """
    file_path = PROCESSED_DIR / filename

    if not file_path.exists():
        print(f"[WARN] Processed file not found: {file_path}")
        return pd.DataFrame()

    try:
        df = pd.read_csv(file_path)
        return df
    except Exception as e:
        print(f"[ERROR] Could not read CSV: {e}")
        return pd.DataFrame()


def generate_data_report(df, output_path="reports/data_summary.txt"):
    """
    Creates a lightweight data report.
    Participants need to improve formatting, feature summaries, etc.
    """
    report = []

    report.append(f"Row Count: {len(df)}")
    report.append(f"Column Count: {len(df.columns)}")
    report.append("\nMissing Values:")
    report.append(str(df.isna().sum()))

    try:
        Path(output_path).parent.mkdir(exist_ok=True)
        with open(output_path, "w") as f:
            f.write("\n".join(report))

        print(f"[INFO] Report generated at {output_path}")
    except Exception as e:
        print(f"[ERROR] Failed to write report: {e}")

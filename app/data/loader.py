from pathlib import Path

import pandas as pd

PROJECT_ROOT = Path(__file__).resolve().parents[2]

CSV_PATH = (
    PROJECT_ROOT
    / "data"
    / "raw"
    / "indian_car_parts_pricing_2026_v2.csv"
)

def load_csv(file_path: Path = CSV_PATH) -> pd.DataFrame:
    """
    Load the car spare-parts pricing CSV

    Args:
        file_path: Location of the CSV file.

    Returns:
        Pandas DataFrame containing the records.
    
    """

    if not file_path.exists():
        raise FileNotFoundError(
            f"CSV file not found: {file_path}"
        )

    df = pd.read_csv(file_path)

    return df


import pandas as pd
from pathlib import Path

DATA_PATH = Path(__file__).resolve().parents[1] / "data"

def load_raw_anime(filename: str = "Anime.csv") -> pd.DataFrame:
    """Carga el dataset original de anime."""
    return pd.read_csv(DATA_PATH / filename)

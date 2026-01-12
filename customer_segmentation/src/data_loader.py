import pandas as pd
from pathlib import Path

def load_data(path: str) -> pd.DataFrame:
    """Carica il dataset clienti."""
    file_path = Path(path)
    if not file_path.exists():
        raise FileNotFoundError(f"File non trovato: {path}")
    return pd.read_csv(file_path)

# =============================================================================
# Carga e preparação dos dados
# -----------------------------------------------------------------------------
# Lê o CSV bruto (data/raw), confere se ele está no formato esperado e gera
# os resumos usados na análise (data/processed).
# =============================================================================
from pathlib import Path

import pandas as pd

from dashvendas import config

# Colunas que o CSV precisa ter
EXPECTED_COLUMNS = [
    "InvoiceNo", "Description", "OrderValue", "Quantity", "CustomerID", "Country",
]


def load_sales(path: Path = config.RAW_SALES_FILE) -> pd.DataFrame:
    """Lê o CSV de vendas e valida as colunas."""
    df = pd.read_csv(path)

    missing = set(EXPECTED_COLUMNS) - set(df.columns)
    if missing:
        raise ValueError(f"Colunas ausentes em {path.name}: {sorted(missing)}")

    if (df["OrderValue"] < 0).any():
        raise ValueError("A coluna OrderValue não pode ter valores negativos.")

    return df[EXPECTED_COLUMNS]


def total_by_country(df: pd.DataFrame) -> pd.DataFrame:
    """Soma o valor dos pedidos por país, do maior para o menor."""
    return (
        df.groupby("Country", as_index=False)["OrderValue"]
        .sum()
        .round({"OrderValue": 2})  # evita sobras de ponto flutuante (ex.: 3131.0099999)
        .sort_values("OrderValue", ascending=False, ignore_index=True)
    )


def save_processed(df: pd.DataFrame, name: str) -> Path:
    """Salva um DataFrame tratado em data/processed/<name>.csv."""
    config.PROCESSED_DATA_DIR.mkdir(parents=True, exist_ok=True)
    path = config.PROCESSED_DATA_DIR / f"{name}.csv"
    df.to_csv(path, index=False)
    return path

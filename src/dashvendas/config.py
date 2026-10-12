# =============================================================================
# Configurações do projeto
# -----------------------------------------------------------------------------
# Centraliza os caminhos das pastas e as variáveis do .env, para que nenhum
# outro arquivo precise "adivinhar" onde estão os dados.
# =============================================================================
import os
from pathlib import Path

from dotenv import load_dotenv

# Raiz do projeto: sobe de src/dashvendas/config.py até Plotly/
PROJECT_ROOT = Path(__file__).resolve().parents[2]

# Lê o arquivo .env (se existir) e joga as variáveis no ambiente
load_dotenv(PROJECT_ROOT / ".env")

# Pastas de dados
DATA_DIR = PROJECT_ROOT / "data"
RAW_DATA_DIR = DATA_DIR / "raw"              # dados originais, nunca editados
PROCESSED_DATA_DIR = DATA_DIR / "processed"  # dados tratados pelo código

# Pastas de saída
REPORTS_DIR = PROJECT_ROOT / "reports"
FIGURES_DIR = REPORTS_DIR / "figures"

# Arquivos principais
RAW_SALES_FILE = RAW_DATA_DIR / "ecom_sales.csv"
FIGURE_FILE = FIGURES_DIR / "vendas_por_pais.png"

# Servidor do dashboard (valores padrão caso o .env não exista)
DASH_HOST = os.getenv("DASH_HOST", "127.0.0.1")
DASH_PORT = int(os.getenv("DASH_PORT", "8050"))
DASH_DEBUG = os.getenv("DASH_DEBUG", "false").lower() == "true"

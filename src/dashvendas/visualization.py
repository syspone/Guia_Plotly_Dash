# =============================================================================
# Gráficos
# -----------------------------------------------------------------------------
# Funções que recebem um DataFrame e devolvem figuras do Plotly. Ficam aqui
# para que o notebook, as aulas e o dashboard usem exatamente o mesmo gráfico.
# =============================================================================
from pathlib import Path

import pandas as pd
import plotly.express as px
from plotly.graph_objects import Figure

from dashvendas import config


def sales_by_country_chart(df_totals: pd.DataFrame) -> Figure:
    """Barras horizontais: total de vendas de cada país (saída de total_by_country)."""
    fig = px.bar(
        df_totals,
        x="OrderValue",
        y="Country",
        orientation="h",
        title="Total de Vendas por País",
        labels={"OrderValue": "Total de Vendas", "Country": "País"},
    )
    fig.update_layout(
        bargap=0.5,                                  # barras mais finas
        yaxis={"categoryorder": "total ascending"},  # maior venda no topo
    )
    return fig


def save_figure(fig: Figure, path: Path = config.FIGURE_FILE) -> Path:
    """Exporta a figura como PNG (usa o Kaleido)."""
    path.parent.mkdir(parents=True, exist_ok=True)
    fig.write_image(path, width=1000, height=600, scale=2)
    return path

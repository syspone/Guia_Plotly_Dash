# =============================================================================
# Pipeline de dados
# -----------------------------------------------------------------------------
# Roda todas as etapas de ponta a ponta, sem precisar abrir notebook:
#     python -m dashvendas.pipeline
# 1) lê data/raw  2) gera o resumo em data/processed  3) exporta o gráfico
# =============================================================================
from dashvendas.data import load_sales, save_processed, total_by_country
from dashvendas.visualization import sales_by_country_chart, save_figure


def main() -> None:
    df = load_sales()
    print(f"Dados carregados: {len(df)} registros")

    totals = total_by_country(df)
    path = save_processed(totals, "total_by_country")
    print(f"Resumo salvo em {path}")

    path = save_figure(sales_by_country_chart(totals))
    print(f"Gráfico salvo em {path}")


if __name__ == "__main__":
    main()

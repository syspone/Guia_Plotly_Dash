# =============================================================================
# Dashboard web com Dash
# -----------------------------------------------------------------------------
# Monta a página e liga o servidor. Para rodar:
#     python -m dashvendas.dashboard
# e abra http://127.0.0.1:8050 no navegador (porta configurável no .env).
# =============================================================================
from dash import Dash, dcc, html

from dashvendas import config
from dashvendas.data import load_sales, total_by_country
from dashvendas.visualization import sales_by_country_chart


def create_app() -> Dash:
    """Cria o app Dash com o layout da página."""
    totals = total_by_country(load_sales())

    app = Dash(__name__, title="Dashboard Vendas")
    app.layout = html.Div([
        html.H1("Vendas por País"),
        dcc.Graph(figure=sales_by_country_chart(totals)),
    ])
    return app


def main() -> None:
    app = create_app()
    # use_reloader=False impede que o script rode duas vezes no modo debug
    app.run(
        host=config.DASH_HOST,
        port=config.DASH_PORT,
        debug=config.DASH_DEBUG,
        use_reloader=False,
    )


if __name__ == "__main__":
    main()

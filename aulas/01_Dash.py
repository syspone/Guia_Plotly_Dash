# =============================================================================
# Autor.........: Cristian Matias de Souza
# Cargo/Nível...: Analista de Dados (N3)
# Criado em.....: 07/09/2026 18:29
# Versão........: 1.0
# -----------------------------------------------------------------------------
# Descrição.....: Aula 01 - primeiro app Dash com o gráfico de vendas
# Dependências..: Python 3.14
# =============================================================================
from dashvendas.data import load_sales, total_by_country
from dashvendas.visualization import sales_by_country_chart
import dash
from dash import dcc, html

# O gráfico vem do pacote dashvendas (o mesmo usado no dashboard e no notebook)
bar_fig = sales_by_country_chart(total_by_country(load_sales()))

app = dash.Dash()

# ===== Com componentes do Dash ====
# app.layout = dcc.Graph(
#     id = 'example-graph',
#     figure = bar_fig
# )


# ==== Com componentes HTML =====
app.layout = html.Div(
    children=[
        html.H1('Sales by Country'),
        dcc.Graph(
            id= 'example-graph',
            figure= bar_fig
        )
    ]
)



if __name__ == '__main__':
    app.run(debug=True)

# =============================================================================
# Autor.........: Cristian Matias de Souza
# Cargo/Nível...: Analista de Dados (N3)
# Criado em.....: 07/09/2026 22:31
# Versão........: 1.0
# -----------------------------------------------------------------------------
# Descrição.....: Aula 02 - componentes HTML do Dash (imagem, texto, quebras)
# Dependências..: Python 3.14
# =============================================================================
import dash
from dash import dcc, html
from datetime import datetime
app = dash.Dash()
app.layout = html.Div(
    children=[
        html.Img(src='https://avatars.githubusercontent.com/u/48097255?v=4', style={'height': '150px'}), # Retorna foto
        html.Hr(),
        html.H1('Testando Dash com HTML'),
        html.Span(
            children= [
                f'Hoje é {datetime.now().strftime("%d/%m/%Y %H:%M:%S")}',
                html.Br(),                   # Quebra de linha
                'Desenvolvido por', html.B('Cristian Souza'),
                html.Br(),
                html.I('Analista e Desenvolvedor')
            ]
        )
    ]
)

if __name__ == '__main__':
    app.run(debug=True)
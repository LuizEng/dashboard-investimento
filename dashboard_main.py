import dash
import dash_html_components as html
import analyser

app = dash.Dash(__name__)


tempo_medio = f"Tempo Médio: {analyser.get_tempo_medio_operacao()} minutos"
total_operacoes = f"Total de Operações: {analyser.get_total_operacoes()} operações"
capital_inicial = f"Capital Inicial: R$ {analyser.get_capital_inicial()}"
capital_atual = f"Capital Inicial: R$ {analyser.get_capital_atual()}"
percentual_acerto = f"Percentual de acertos: {analyser.get_taxa_de_acerto()}"

app.layout = html.Div([
    html.H1("Dados Operações"),
    html.P(id='tempo_medio', children=tempo_medio),
    html.P(id='total_operacoes', children=total_operacoes),    
    html.P(id='capital_inicial', children=capital_inicial),
    html.P(id='capital_atual', children=capital_atual),    
    html.P(id='percentual_acerto', children=percentual_acerto),        
])

# Execute o aplicativo
if __name__ == '__main__':
    app.run_server(debug=True)
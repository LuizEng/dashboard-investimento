import dash
import dash_html_components as html
import analyser

app = dash.Dash(__name__)


tempo_medio = analyser.get_tempo_medio_operacao()  
media_text = f"Tempo Médio: {tempo_medio} minutos"
total_operacoes = analyser.get_total_operacoes()
media_total = f"Total de Operações: {total_operacoes} operações"

app.layout = html.Div([
    html.H1("Média de tempo de operação"),
    html.P(id='media-text', children=media_text),
    html.P(id='media-text', children=media_total),
])

# Execute o aplicativo
if __name__ == '__main__':
    app.run_server(debug=True)
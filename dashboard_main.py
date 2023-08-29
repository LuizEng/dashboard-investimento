import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

app = dash.Dash(__name__)

app.layout = html.Div([
    dcc.Graph(id='graph'),
    dcc.Slider(
        id='slider',
        min=0,
        max=10,
        step=0.1,
        value=5
    )
])

@app.callback(
    Output('graph', 'figure'),
    [Input('slider', 'value')]
)
def update_graph(selected_value):    
    figure = ... 
    return figure


if __name__ == '__main__':
    app.run_server(debug=True)
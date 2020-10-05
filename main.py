import dash
import dash_core_components as dcc
import dash_html_components as html
#import dash_dangerously_set_inner_html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output
from modules.widgets import *


app = dash.Dash(__name__, external_stylesheets=[dbc.themes.CYBORG])

app.layout = html.Div([
    dbc.Row(
        [
            dbc.Col(
                html.Div("title column bar"),
                width={"size":3, "order":1},
            ),

            dbc.Col(
                dcc.Tabs(id='tabs-example', value='tab-1', children=[
                    dcc.Tab(label='Tab one', value='tab-1'),
                    dcc.Tab(label='Tab two', value='tab-2'),
                    ]), width={"size":6, "order":2},
            ),

            
        ]
    ),

    dbc.Row(
        dbc.Col(
            html.Div(id='tabs-example-content'),
            ),
    ),

])






tab_1_content = html.Div([

    
    dbc.Row(
        [
            dbc.Col(
                html.Iframe(srcDoc=graph_widget("NASDAQ:AAPL"), width="100%", height="630", style={"border":"none"}),
                width={"size":8, "order":1},
            ),
            dbc.Col(
                html.Iframe(srcDoc=alternate_calendar_widget(), width="100%", height="630", style={"border":"none"}),
                width={"size":4, "order":2},
            ),

        ],
        no_gutters=True,


    ),

    dbc.Row(
        [
        dbc.Col(
            html.Iframe(srcDoc=mini_graph_widget("EURUSD"), width="360", height="240", style={"border":"none"}),
            width={"size":2, "order":1},
        ),

        dbc.Col(
            html.Iframe(srcDoc=mini_graph_widget("EURGBP"), width="360", height="240", style={"border":"none"}),
            width={"size":2, "order":2},
        ),

        dbc.Col(
            html.Iframe(srcDoc=mini_graph_widget("EURCHF"), width="360", height="240", style={"border":"none"}),
            width={"size":2, "order":3},
        ),

        dbc.Col(
            html.Iframe(srcDoc=mini_graph_widget("EURJPY"), width="360", height="240", style={"border":"none"}),
        width={"size":2, "order":4},
        ),

        dbc.Col(
            html.Iframe(srcDoc=mini_graph_widget("EURBTC"), width="360", height="240", style={"border":"none"}),
            width={"size":2, "order":3},
        ),

        dbc.Col(
            html.Iframe(srcDoc=mini_graph_widget("GBPUSD"), width="360", height="240", style={"border":"none"}),
        width={"size":2, "order":4},
        ),

        ],justify="start",
        
    ),

    dbc.Row(
        [
        dbc.Col(
            html.Iframe(srcDoc=mini_graph_widget("EURUSD"), width="360", height="240", style={"border":"none"}),
            width={"size":2, "order":1},
        ),

        dbc.Col(
            html.Iframe(srcDoc=mini_graph_widget("EURGBP"), width="360", height="240", style={"border":"none"}),
            width={"size":2, "order":2},
        ),

        dbc.Col(
            html.Iframe(srcDoc=mini_graph_widget("EURCHF"), width="360", height="240", style={"border":"none"}),
            width={"size":2, "order":3},
        ),

        dbc.Col(
            html.Iframe(srcDoc=mini_graph_widget("EURJPY"), width="360", height="240", style={"border":"none"}),
        width={"size":2, "order":4},
        ),

        dbc.Col(
            html.Iframe(srcDoc=mini_graph_widget("EURBTC"), width="360", height="240", style={"border":"none"}),
            width={"size":2, "order":3},
        ),

        dbc.Col(
            html.Iframe(srcDoc=mini_graph_widget("GBPUSD"), width="360", height="240", style={"border":"none"}),
        width={"size":2, "order":4},
        ),

        ],
        
    ),





], className="container-fluid")



tab_2_content = html.Div([







])









@app.callback(Output('tabs-example-content', 'children'),
              [Input('tabs-example', 'value')])
def render_content(tab):
    if tab == 'tab-1':
        return tab_1_content
    elif tab == 'tab-2':
        return html.Div([
            html.H3('Tab content 2')
        ])





if __name__ == '__main__':
    app.run_server(debug=True)
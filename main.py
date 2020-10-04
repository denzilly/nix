import dash
import dash_core_components as dcc
import dash_html_components as html
#import dash_dangerously_set_inner_html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output
from modules.widgets import graph_widget,mini_graph_widget,calendar_widget


app = dash.Dash(__name__, external_stylesheets=[dbc.themes.CYBORG])

app.layout = html.Div([

    dbc.Row(
        dbc.Col(
            html.Div("title column bar")
        )
    ),
    dbc.Row(
        [
            dbc.Col(
                html.Iframe(srcDoc=graph_widget("NASDAQ:AAPL"), width="1020", height="650", style={"border":"none"}),
                width={"size":8, "order":1},
            ),

            dbc.Col(
                html.Iframe(srcDoc=calendar_widget(), width="530", height="620", style={"border":"none"}),
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

        ],
        no_gutters=True,
    ),





])




if __name__ == '__main__':
    app.run_server(debug=True)
import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_dangerously_set_inner_html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output


app = dash.Dash(__name__, external_stylesheets=[dbc.themes.CYBORG])

app.layout = html.Div([
    html.Iframe(srcDoc="""<!-- TradingView Widget BEGIN -->
<div class="tradingview-widget-container">
  <div id="tradingview_0a7ea"></div>
  <div class="tradingview-widget-copyright"><a href="https://www.tradingview.com/symbols/NASDAQ-AAPL/" rel="noopener" target="_blank"><span class="blue-text">AAPL Chart</span></a> by TradingView</div>
  <script type="text/javascript" src="https://s3.tradingview.com/tv.js"></script>
  <script type="text/javascript">
  new TradingView.widget(
  {
  "width": 980,
  "height": 610,
  "symbol": "NASDAQ:AAPL",
  "interval": "D",
  "timezone": "Etc/UTC",
  "theme": "dark",
  "style": "1",
  "locale": "en",
  "toolbar_bg": "#f1f3f6",
  "enable_publishing": false,
  "allow_symbol_change": true,
  "container_id": "tradingview_0a7ea"
}
  );
  </script>
</div>
<!-- TradingView Widget END -->""", width="1020", height="650"


    ),
])




if __name__ == '__main__':
    app.run_server(debug=True)
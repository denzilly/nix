



def graph_widget(ticker):

    widget = f"""<!-- TradingView Widget BEGIN -->
<div class="tradingview-widget-container">
  <div id="tradingview_0a7ea"></div>
  <div class="tradingview-widget-copyright"><a href="https://www.tradingview.com/symbols/{ticker}/" rel="noopener" target="_blank"><span class="blue-text">AAPL Chart</span></a> by TradingView</div>
  <script type="text/javascript" src="https://s3.tradingview.com/tv.js"></script>
  <script type="text/javascript">
  new TradingView.widget(
  {{
  "width": 980,
  "height": 610,
  "symbol": "{ticker}",
  "interval": "D",
  "timezone": "Etc/UTC",
  "theme": "dark",
  "style": "1",
  "locale": "en",
  "toolbar_bg": "#f1f3f6",
  "enable_publishing": false,
  "allow_symbol_change": true,
  "container_id": "tradingview_0a7ea"
}}
  );
  </script>
</div>
<!-- TradingView Widget END -->"""

    return widget


def mini_graph_widget(ticker):

    widget = f"""<!-- TradingView Widget BEGIN -->
<div class="tradingview-widget-container">
  <div class="tradingview-widget-container__widget"></div>
  <div class="tradingview-widget-copyright"><a href="https://www.tradingview.com/symbols/{ticker}/?exchange=FX" rel="noopener" target="_blank"><span class="blue-text">EURUSD Rates</span></a> by TradingView</div>
  <script type="text/javascript" src="https://s3.tradingview.com/external-embedding/embed-widget-mini-symbol-overview.js" async>
  {{
  "symbol": "FX:{ticker}",
  "width": 250,
  "height": 200,
  "locale": "en",
  "dateRange": "1D",
  "colorTheme": "dark",
  "trendLineColor": "rgba(255, 152, 0, 1)",
  "underLineColor": "rgba(255, 152, 0, 0.24)",
  "isTransparent": false,
  "autosize": false,
  "largeChartUrl": ""
}}
  </script>
</div>
<!-- TradingView Widget END -->"""

    return widget



def calendar_widget():

    widget = """<!-- TradingView Widget BEGIN -->
<div class="tradingview-widget-container">
  <div class="tradingview-widget-container__widget"></div>
  <div class="tradingview-widget-copyright"><a href="https://www.tradingview.com/markets/currencies/economic-calendar/" rel="noopener" target="_blank"><span class="blue-text">Economic Calendar</span></a> by TradingView</div>
  <script type="text/javascript" src="https://s3.tradingview.com/external-embedding/embed-widget-events.js" async>
  {
  "colorTheme": "dark",
  "isTransparent": false,
  "width": "510",
  "height": "600",
  "locale": "en",
  "importanceFilter": "-1,0,1"
}
  </script>
</div>
<!-- TradingView Widget END -->"""

    return widget
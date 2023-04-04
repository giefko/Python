import requests
import json
import plotly.graph_objs as go
from datetime import datetime

# Define the API URL and parameters
url = "https://api.pro.coinbase.com/products/{currency}-USD/candles"
params = {
    "granularity": 60,  # 1 minute intervals
    "limit": 1000  # Maximum number of data points
}

# Define the cryptocurrencies to track
cryptocurrencies = ["BTC", "ETH", "LTC"]

# Retrieve the data from the API and parse it
data = {}
for currency in cryptocurrencies:
    response = requests.get(url.format(currency=currency), params=params)
    response.raise_for_status()
    candles = json.loads(response.text)
    data[currency] = {
        "dates": [datetime.fromtimestamp(c[0]) for c in candles],
        "open": [c[3] for c in candles],
        "high": [c[2] for c in candles],
        "low": [c[1] for c in candles],
        "close": [c[4] for c in candles]
    }

# Create the candlestick chart
fig = go.Figure()
for currency in cryptocurrencies:
    fig.add_trace(go.Candlestick(
        x=data[currency]["dates"],
        open=data[currency]["open"],
        high=data[currency]["high"],
        low=data[currency]["low"],
        close=data[currency]["close"],
        name=currency
    ))

# Customize the layout and display the chart
fig.update_layout(
    title="Live Crypto Prices",
    yaxis_title="USD",
    xaxis_rangeslider_visible=False
)
fig.show()

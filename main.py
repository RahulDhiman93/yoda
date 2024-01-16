from kite_trade import *
import plotly.graph_objects as go

from datetime import datetime

kite = KiteApp()

import datetime

instrument_token = 5195009
from_datetime = datetime.datetime.now() - datetime.timedelta(days=200)
to_datetime = datetime.datetime.now()
interval = "30minute"
# print()
data = kite.historical_data(instrument_token, from_datetime, to_datetime, interval, continuous=False, oi=False)
print(data)

def plot_candlestick(data):
    dates = [entry['date'] for entry in data]
    opens = [entry['open'] for entry in data]
    highs = [entry['high'] for entry in data]
    lows = [entry['low'] for entry in data]
    closes = [entry['close'] for entry in data]

    fig = go.Figure(data=[go.Candlestick(x=dates,
                                         open=opens,
                                         high=highs,
                                         low=lows,
                                         close=closes,
                                         increasing_line_color='green',
                                         decreasing_line_color='red')])

    fig.update_layout(xaxis_rangeslider_visible=False, title='Stock Price Data')
    fig.show()

# Assuming data is a list of dictionaries with keys 'date', 'open', 'high', 'low', 'close'
plot_candlestick(data)
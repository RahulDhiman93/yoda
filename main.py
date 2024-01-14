from kite_trade import *
import matplotlib.pyplot as plt
from datetime import datetime

kite = KiteApp()

import datetime

instrument_token = 738561
from_datetime = datetime.datetime.now() - datetime.timedelta(days=60)  # From last & days
to_datetime = datetime.datetime.now()
interval = "60minute"
# print()
data = kite.historical_data(instrument_token, from_datetime, to_datetime, interval, continuous=False, oi=False)


def plotgraph(data):
    dates = [entry['date'] for entry in data]
    opens = [entry['open'] for entry in data]
    highs = [entry['high'] for entry in data]
    lows = [entry['low'] for entry in data]
    closes = [entry['close'] for entry in data]

    plt.plot(dates, opens, label='Open')
    plt.plot(dates, highs, label='High')
    plt.plot(dates, lows, label='Low')
    plt.plot(dates, closes, label='Close')

    plt.xlabel('Date and Time')
    plt.ylabel('Stock Price')
    plt.title('Stock Price Data')
    plt.legend()
    plt.show()


plotgraph(data)

from kite_trade import *
import csv

kite = KiteApp()

data = kite.instruments("NSE")

csv_file_path = 'stocks_data.csv'

with open(csv_file_path, 'w', newline='') as csv_file:
    fieldnames = data[0].keys()
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(data)

print(f'CSV file created at: {csv_file_path}')

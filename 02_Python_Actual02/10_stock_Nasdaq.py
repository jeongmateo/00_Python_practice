import yahoo_fin.stock_info as si

AAPL = si.get_stats('IIVI')
print(AAPL)
import yfinance as yf

ticker = yf.Ticker('PETR4.SA')
print(ticker.history(period='max'))
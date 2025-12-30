import yfinance as yf
from datetime import datetime

def fetch_stock_data(ticker: str):
    stock = yf.Ticker(ticker)
    hist = stock.history(period="1d")

    if hist.empty:
        raise ValueError("Invalid ticker or no data available")

    row = hist.iloc[-1]
    return {
        "ticker": ticker,
        "timestamp": datetime.utcnow().isoformat(),
        "open": float(row["Open"]),
        "high": float(row["High"]),
        "low": float(row["Low"]),
        "close": float(row["Close"]),
        "volume": int(row["Volume"])
    }

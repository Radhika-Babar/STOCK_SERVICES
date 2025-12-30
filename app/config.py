import os

DEFAULT_TICKER = os.getenv("DEFAULT_TICKER", "TSLA")
DB_PATH = os.getenv("DB_PATH", "data/stocks.db")
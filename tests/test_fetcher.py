from unittest.mock import patch
from app.fetcher import fetch_stock_data


@patch("app.fetcher.yf.Ticker")
def test_fetch_stock_data(mock_ticker):
    mock_history = mock_ticker.return_value.history
    mock_history.return_value.empty = False

    mock_history.return_value.iloc = [{
        "Open": 10,
        "High": 15,
        "Low": 8,
        "Close": 12,
        "Volume": 1000
    }]

    result = fetch_stock_data("TSLA")

    assert result["ticker"] == "TSLA"
    assert "open" in result

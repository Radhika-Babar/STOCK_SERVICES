from pydantic import BaseModel

class StockResponse(BaseModel):
    ticker: str
    timestamp: str
    open: float
    high: float
    low: float
    close: float
    volume: int

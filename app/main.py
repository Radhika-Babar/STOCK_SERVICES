from fastapi import FastAPI, HTTPException
from app.fetcher import fetch_stock_data
from app.repository import insert_stock, get_last, get_history
from app.database import init_db
from app.config import DEFAULT_TICKER

app = FastAPI(title="Stock Market Service")

init_db()

@app.post("/fetch")
def fetch(ticker: str = DEFAULT_TICKER):
    try:
        data = fetch_stock_data(ticker)
        insert_stock(data)
        return {"status": "success", "data": data}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.get("/last")
def last():
    row = get_last()
    if not row:
        raise HTTPException(status_code=404, detail="No data found")
    return row

@app.get("/history")
def history(ticker: str):
    return get_history(ticker)

@app.get("/")
def root():
    return {
        "message": "Stock Service is running",
        "docs": "/docs"
    }

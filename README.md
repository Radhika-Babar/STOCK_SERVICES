Stock Market Data Service (Python Intern Assignment)
This project is a Python-based backend service that fetches stock market data using Yahoo Finance, stores it locally in a SQLite database, and exposes the data through a REST API built with FastAPI.

The application demonstrates:
Clean project structure
Separation of concerns
API development
Database handling
Basic testing and configuration

Tech Stack
Python 3.9+
FastAPI – Web framework
Uvicorn – ASGI server
yfinance – Stock market data
SQLite – Local database
Pytest – Unit testing

Run the Application
uvicorn app.main:app --reload

API Documentation (Swagger UI)
http://127.0.0.1:8000/docs

Fetch & Store Stock Data
POST /fetch?ticker=TSLA
Fetches the latest stock data and stores it in the database.

Get Latest Stored Record
GET /last

Get Stock History
GET /history?ticker=TSLA

Important Design Note
Yahoo Finance provides delayed or end-of-day stock data.
As a result:
Multiple fetches within the same day may return identical OHLCV values
To prevent duplicate entries, the database uses a unique timestamp constraint
Duplicate records are ignored intentionally to maintain data integrity

Design Decisions & Trade-offs
SQLite chosen for simplicity and portability
FastAPI used for rapid API development and built-in documentation
Repository pattern improves maintainability and testability
No background scheduler to keep the service lightweight

Limitations
Data is not real-time
Designed for learning and demonstration purposes
Single-user local database

Extension Questions
How would this scale to handle 10 tickers concurrently?
To handle multiple tickers concurrently, I would introduce asynchronous fetching using background tasks or async workers. Each ticker fetch would run independently, and results would be stored in the database with proper indexing on the ticker and timestamp. For higher scale, a task queue (e.g., Celery or a lightweight job runner) could be used to parallelize fetch operations without blocking API requests.

How would you avoid API rate limits?
API rate limits can be mitigated by implementing:
Caching to avoid repeated fetches for the same ticker within a short time window
Request throttling and exponential backoff on failures
Batching requests where supported
Storing previously fetched data and serving it from the database instead of hitting the API repeatedly
This reduces unnecessary external API calls and improves reliability.

What’s the first architectural change you’d make for production?

The first change would be replacing SQLite with a production-grade database such as PostgreSQL and moving fetch operations to background workers. This decouples API responsiveness from data ingestion and allows the system to scale horizontally while maintaining data consistency and reliability.

What’s a trading-related pitfall of using this setup as-is?
Yahoo Finance data is delayed and not guaranteed to be real-time or fully accurate. Using this setup directly for trading decisions could lead to incorrect assumptions, stale prices, and execution at unfavorable market conditions. This service is suitable for analysis and learning, but not for live trading systems.
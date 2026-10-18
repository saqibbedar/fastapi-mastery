# FastAPI Project 5 (Postgresql based)

We are using async-first fastapi application and psycopg(v3). You need to install/setup postgresql first on your machine. Once it is installed on your local machine you can then follow following steps.

```bash
# Initial commands
uv add "psycopg[binary]" sqlalchemy fastapi uvicorn python-dotenv         # note: you must have postgresql installed on your machine

# If cloned
uv sync
```
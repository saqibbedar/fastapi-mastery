# Guide to run project

```bash
# create virtual environment & activate it
uv venv .venv
source .venv/bin/activate

# install dependencies
uv sync

# run the project
uv run uvicorn src.main:app --reload

# view docs
# Swagger UI
http://127.0.0.1:8000/docs

# ReDoc
http://127.0.0.1:8000/redoc

# OpenAPI Schema
http://127.0.0.1:8000/openapi.json
```
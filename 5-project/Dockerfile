# Python official image
FROM python:3.15-slim

# Install uv inside container
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

# Environment settings for uv
ENV UV_COMPILE_BYTECODE=1 \
    UV_LINK_MODE=copy

# Set the working directory inside container
WORKDIR /app

# 1. Copy dependency files first (improves caching speed)
COPY pyproject.toml uv.lock ./

# 2. Install dependencies only (without installing the project itself)
RUN uv sync --frozen --no-install-project

# 3. Copy application code
COPY . .

# 4. Sync project code
RUN uv sync --frozen

# Place the virtual environment on PATH
ENV PATH="/app/.venv/bin:$PATH"

# Expose the port FastAPI will run on
EXPOSE 8000

# Start Uvicorn directly from the virtual environment
CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000"]
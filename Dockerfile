# Stage 1: Build frontend
FROM node:20-alpine AS frontend-builder
WORKDIR /app/frontend
COPY frontend/package*.json ./
RUN npm ci --silent
COPY frontend/ ./
RUN npm run build

# Stage 2: Python application
FROM python:3.11-slim AS runtime

# Install system dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Install uv
COPY --from=ghcr.io/astral-sh/uv:latest /uv /usr/local/bin/uv

WORKDIR /app

# Copy dependency files
COPY pyproject.toml uv.lock ./

# Install dependencies (production only)
RUN uv sync --frozen --no-dev --no-editable

# Copy application code
COPY l0l1/ ./l0l1/
COPY --from=frontend-builder /app/frontend/dist ./frontend/dist

# Create non-root user
RUN useradd -m -u 1000 l0l1user && \
    mkdir -p /app/data /app/workspaces && \
    chown -R l0l1user:l0l1user /app

USER l0l1user

# Expose port
EXPOSE 8000

# Health check
HEALTHCHECK --interval=30s --timeout=10s --start-period=5s --retries=3 \
    CMD curl -f http://localhost:8000/health || exit 1

# Default environment variables
ENV L0L1_API_HOST=0.0.0.0
ENV L0L1_API_PORT=8000
ENV L0L1_LOG_LEVEL=INFO

# Start server
CMD ["uv", "run", "uvicorn", "l0l1.api.main:app", "--host", "0.0.0.0", "--port", "8000"]

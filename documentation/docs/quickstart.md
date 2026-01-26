# Quick Start

Get up and running with l0l1 in minutes.

## Prerequisites

- Python 3.11 or higher
- [uv](https://docs.astral.sh/uv/) package manager (recommended)
- OpenAI or Anthropic API key

## Installation

### Using uv (Recommended)

```bash
# Clone the repository
git clone https://github.com/skelf-research/l0l1-api.git
cd l0l1-api

# Install dependencies
uv sync

# Install with all optional dependencies
uv sync --all-extras
```

### Using pip

```bash
pip install l0l1
```

## Configuration

Create a `.env` file in your project root:

```bash
# Copy the example
cp .env.example .env

# Edit with your API key
OPENAI_API_KEY=sk-your-api-key
```

Or set environment variables directly:

```bash
export OPENAI_API_KEY="sk-your-api-key"
```

## Your First Commands

### Validate a Query

```bash
uv run l0l1 validate "SELECT * FROM users WHERE id = 1"
```

Example output:
```
Query Validation Result
=======================
Status: Valid
Issues: None
Suggestions:
  - Consider adding LIMIT clause for large tables
```

### Explain a Query

```bash
uv run l0l1 explain "SELECT u.name, COUNT(o.id) as order_count
FROM users u
JOIN orders o ON u.id = o.user_id
GROUP BY u.name
HAVING COUNT(o.id) > 5"
```

### Check for PII

```bash
uv run l0l1 check-pii "SELECT * FROM customers WHERE email = 'john.doe@example.com' AND ssn = '123-45-6789'"
```

Example output:
```
PII Detection Result
====================
PII Found: Yes

Detected Entities:
  - EMAIL_ADDRESS: john.doe@example.com (confidence: 0.95)
  - SSN: 123-45-6789 (confidence: 0.99)

Anonymized Query:
  SELECT * FROM customers WHERE email = '<EMAIL>' AND ssn = '<SSN>'
```

## Start the API Server

```bash
# Start with default settings
uv run l0l1-serve

# Or with custom host/port
L0L1_API_HOST=0.0.0.0 L0L1_API_PORT=8080 uv run l0l1-serve
```

Access the API:
- API: http://localhost:8000
- Interactive Docs: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

### API Example

```bash
# Validate a query via API
curl -X POST http://localhost:8000/sql/validate \
  -H "Content-Type: application/json" \
  -d '{"query": "SELECT * FROM users"}'
```

## Jupyter Integration

```python
# In a Jupyter notebook
from l0l1.integrations.jupyter import sql_magic

# Load the magic command
%load_ext l0l1.integrations.jupyter.magic

# Use the magic command
%%sql_validate
SELECT * FROM users WHERE id = 1
```

## Using Docker

```bash
# Build and run
docker-compose up -d

# Check health
curl http://localhost:8000/health
```

## What's Next?

- [Full Installation Guide](getting-started.md) - Detailed setup for different environments
- [Configuration Reference](configuration.md) - All configuration options
- [CLI Reference](cli.md) - Complete command documentation
- [API Reference](api.md) - REST API endpoints
- [Jupyter Guide](guides/jupyter.md) - Notebook integration details

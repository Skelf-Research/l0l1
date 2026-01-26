# l0l1

**SQL that learns. AI that validates. Privacy that protects.**

l0l1 is a developer toolkit for SQL analysis that combines AI-powered validation with continuous learning. It detects PII, suggests improvements, and gets smarter from your successful queries.

## Features

<div class="grid cards" markdown>

-   :material-brain:{ .lg .middle } **AI-Powered Analysis**

    ---

    Multi-provider support (OpenAI, Anthropic) for query validation, explanation, and completion

    [:octicons-arrow-right-24: REST API](api.md)

-   :material-shield-check:{ .lg .middle } **PII Detection**

    ---

    Presidio-powered detection and anonymization of personally identifiable information

    [:octicons-arrow-right-24: PII Guide](guides/pii-learning.md)

-   :material-school:{ .lg .middle } **Continuous Learning**

    ---

    Graph-based pattern learning from successful queries improves suggestions over time

    [:octicons-arrow-right-24: Learning Guide](guides/graph-learning.md)

-   :material-view-grid:{ .lg .middle } **Multi-Interface**

    ---

    CLI, REST API, Jupyter notebooks, and VS Code extension with LSP

    [:octicons-arrow-right-24: CLI Reference](cli.md)

</div>

## Quick Start

### Installation

```bash
# Clone and install with uv (recommended)
git clone https://github.com/skelf-research/l0l1-api.git
cd l0l1-api
uv sync

# Configure
export OPENAI_API_KEY="sk-..."
```

### CLI Usage

```bash
# Validate a SQL query
l0l1 validate "SELECT * FROM users WHERE id = 1"

# Explain a query
l0l1 explain "SELECT u.name, COUNT(o.id) FROM users u JOIN orders o ON u.id = o.user_id GROUP BY u.name"

# Check for PII
l0l1 check-pii "SELECT * FROM users WHERE email = 'john@example.com'"
```

### API Server

```bash
# Start the API server
uv run l0l1-serve

# Or use uvicorn directly with hot reload
uv run uvicorn l0l1.api.main:app --reload
```

The API is available at `http://localhost:8000` with interactive docs at `/docs`.

### Python SDK

```python
from l0l1.models.factory import ModelFactory
from l0l1.services.pii_detector import PIIDetector

# Initialize
model = ModelFactory.get_default_model()
pii_detector = PIIDetector()

# Validate
result = await model.validate_sql_query(
    "SELECT * FROM users WHERE id = 1",
    schema_context="users(id, name, email)"
)

# Check PII
pii_findings = pii_detector.detect_pii("SELECT * FROM users WHERE email = 'john@example.com'")
```

## Architecture

```
l0l1/
├── api/           # FastAPI REST API
├── cli/           # Typer CLI
├── core/          # Configuration
├── models/        # AI providers (OpenAI, Anthropic)
├── services/      # Core services
│   ├── pii_detector.py      # PII detection (Presidio)
│   ├── learning_service.py  # Pattern learning
│   ├── database_service.py  # DB connections
│   └── schema_service.py    # Schema management
└── integrations/
    ├── jupyter/   # Notebook integration
    └── ide/       # LSP server
```

## Next Steps

- [Installation Guide](getting-started.md) - Complete setup instructions
- [Configuration](configuration.md) - Environment variables and settings
- [CLI Reference](cli.md) - Command line interface
- [REST API](api.md) - API endpoints and usage
- [Jupyter Guide](guides/jupyter.md) - Notebook integration
- [VS Code Extension](guides/vscode-extension.md) - IDE integration

## License

l0l1 is released under the [MIT License](https://github.com/skelf-research/l0l1-api/blob/main/LICENSE).

---

Built by [Skelf Research](https://skelfresearch.com)

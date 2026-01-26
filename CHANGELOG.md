# Changelog

All notable changes to l0l1 will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Changed
- Migrated from Flask to FastAPI for improved performance and async support
- Migrated from Click CLI to Typer for better developer experience
- Replaced Marshmallow schemas with Pydantic models
- Updated CORS configuration to use environment variables

### Removed
- Removed legacy Flask code, templates, and blueprints
- Removed Flask-SQLAlchemy in favor of async SQLAlchemy

### Security
- Fixed CORS configuration to use environment variables (L0L1_CORS_ORIGINS)
- Removed hardcoded localhost references, now configurable via environment

## [0.2.0] - 2024-01-26

### Added
- FastAPI REST API with OpenAPI documentation
- Typer-based CLI with rich output
- Multi-provider AI support (OpenAI, Anthropic)
- PII detection and anonymization with Presidio
- Continuous learning from successful queries
- Graph-based pattern learning for query suggestions
- Jupyter notebook integration with magic commands and widgets
- VS Code extension with LSP support
- Database connection management (PostgreSQL, MySQL, SQLite, DuckDB)
- Schema version management and migration generation
- Knowledge graph for query pattern learning
- Multi-tenant workspace isolation
- Background task processing with Dramatiq

### Changed
- Improved query validation with schema context
- Enhanced completion suggestions using learned patterns

## [0.1.0] - 2024-01-01

### Added
- Initial release with Flask backend
- Basic SQL validation
- Simple CLI interface

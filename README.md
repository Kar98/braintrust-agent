# Opinionated Agentic Bootstrap (ADK)

An opinionated starting bootstrap for Google's ADK using GCP's Vertex AI Agent Engine.

## Development

### Setup

1. Install GCloud CLI from [Google's source](https://docs.cloud.google.com/sdk/docs/install-sdk)
2. Authorise your account with the GCloud CLI `gcloud auth application-default login`. 
3. Open the project inside the devcontainer in your chosen IDE. See [Developing inside a Container](https://code.visualstudio.com/docs/devcontainers/containers) for more information.
4. Run `docker compose up --detach --wait` to start up all services in development mode.
5. Open `http://localhost:8000` in a browser to interact with your basic agent.

### Commands

```bash
# Install all dependencies
just sync

# Run linting, formatting check, and type checking
just check

# Auto-fix lint issues and format code
just fix

# Type check only
just typecheck
```

### Tools

This project uses:
- **[ty](https://astral.sh/blog/ty)** - Astral's next-generation type checker and language server for Python
- **[Ruff](https://docs.astral.sh/ruff/)** - Fast Python linter and formatter
- **[uv](https://docs.astral.sh/uv/)** - Fast Python package installer and resolver

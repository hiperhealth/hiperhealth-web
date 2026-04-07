# Development Guide

## Contributing

Thank you for your interest in contributing to HiperHealth Web!

## Development Setup

1. Clone the repository
2. Install dependencies:
   ```bash
   conda env create -f conda/dev.yaml
   conda activate hiperhealth
   ./scripts/install-dev.sh
   ```

## Code Quality

This project uses several tools to maintain code quality:

- **ruff**: Linting and formatting
- **mypy**: Static type checking
- **bandit**: Security analysis
- **vulture**: Dead code detection
- **pre-commit**: Automated checks before commits

### Running Pre-commit Hooks

```bash
pre-commit install
pre-commit run --all-files
```

## Testing

Run tests with:

```bash
pytest tests/
```

## Documentation

Build documentation locally:

```bash
makim docs.build
```

## Pull Request Process

1. Create a new branch for your changes
2. Make your changes
3. Ensure all pre-commit hooks pass
4. Push your branch and create a pull request
5. Wait for review and address any feedback

For more details, see the
[Pull Request Template](https://github.com/hiperhealth/hiperhealth-web/blob/main/.github/PULL_REQUEST_TEMPLATE.md).

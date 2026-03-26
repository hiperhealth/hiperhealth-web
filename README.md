# hiperhealth-web

`hiperhealth-web` is a physician-facing web application for running structured
consultations with AI-assisted diagnostics and exam suggestions.

It includes:

- A FastAPI backend (`src/research/backend`)
- A React + Vite frontend (`src/research/frontend`)
- A local SQLite database for persistence

## Features

- Multi-step clinical workflow (demographics, lifestyle, symptoms, mental
  health, reports, wearable data, diagnosis, exams)
- AI differential diagnosis and exam recommendations via the `hiperhealth`
  package
- Medical report upload and extraction
- Wearable data upload and parsing
- De-identification before final persistence

## Repository Layout

- `src/research/backend`: FastAPI API, models, schemas, repository logic
- `src/research/frontend`: React/Vite client
- `scripts`: utility scripts (build, migrations helpers, codegen)
- `tests`: pytest setup and fixtures
- `conda/dev.yaml`: reproducible development environment

## Prerequisites

- Python `>=3.10,<4`
- Node.js (LTS recommended)
- `uv` (optional, for faster Python package installation)
- `tesseract` and `libmagic` (used by extraction workflows)
- `OPENAI_API_KEY` for AI-powered endpoints

## Local Setup

1. Create and activate the conda environment:

```bash
conda env create -f conda/dev.yaml -n hiperhealth-web
conda activate hiperhealth-web
```

2. Install Python dependencies:

```bash
pip install -e ".[dev]"
```

3. Install frontend dependencies:

```bash
cd src/research/frontend
npm install
cd ../../..
```

4. Configure environment variables:

```bash
cp .envs/.env.tpl .envs/.env
mkdir -p src/.envs
cp .envs/.env src/.envs/.env
```

Set `OPENAI_API_KEY` in `.envs/.env` (and keep `src/.envs/.env` in sync).

## Run the Application

1. Initialize the database:

```bash
makim db.setup
```

2. Start backend API:

```bash
makim research.backend
```

3. Start frontend (new terminal):

```bash
makim research.frontend
```

Default dev URLs:

- Backend: `http://localhost:8000`
- Frontend: `http://localhost:5173`

## CLI Mode

For a terminal-based consultation flow:

```bash
cd src/research/backend
python cli.py consult
```

Saved CLI records are written to `~/config/.hiperhealth/records`.

## API Workflow

Typical physician flow:

1. `POST /api/patients`
2. `POST /api/consultations/{patient_id}/demographics`
3. `POST /api/consultations/{patient_id}/lifestyle`
4. `POST /api/consultations/{patient_id}/symptoms`
5. `POST /api/consultations/{patient_id}/mental`
6. `POST /api/consultations/{patient_id}/medical-reports/upload` (or `/skip`)
7. `POST /api/consultations/{patient_id}/wearable-data/upload` (or `/skip`)
8. `GET /api/consultations/{patient_id}/diagnosis` then `POST /diagnosis`
9. `GET /api/consultations/{patient_id}/exams` then `POST /exams`

Useful utility endpoints:

- `GET /api/health`
- `GET /api/patients`
- `GET /api/consultations/{patient_id}/status`
- `DELETE /api/patients/{patient_id}`

## Data Storage

The backend creates SQLite data automatically at:

- `src/research/backend/data/db.sqlite`

## Development Commands

Run tests:

```bash
pytest -vv
```

Run quality checks:

```bash
pre-commit run --all-files
ruff check .
mypy .
```

Serve docs:

```bash
mkdocs serve --watch docs --config-file mkdocs.yaml
```

## Troubleshooting

- `ModuleNotFoundError: No module named 'dotenv'`: install it with
  `pip install python-dotenv`.
- AI endpoints fail or return provider errors: verify `OPENAI_API_KEY` in your
  `.env` files.
- Upload extraction errors: confirm `tesseract` and `libmagic` are installed in
  your environment.

## License

BSD 3-Clause. See `LICENSE`.

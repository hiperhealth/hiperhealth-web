# Deep Exploration Report — Web + Repository (2026-03-18)

This report summarizes a deep exploration of the `hiperhealth-web` codebase and related web references.

## 1) Scope and Coverage

- Repository root scanned: `d:/hiperhealth-web`
- Tracked files discovered: **158**
- Total tracked lines traversed via `wc -l` across all tracked files: **48,569**
- Per-file line-count manifest generated at runtime: `/tmp/repo_linecount_all_files.txt`
- Dominant file types: `.py` (34), `.jsx` (32), `.md` (15), `.json` (12), `.yaml` (9), `.js` (9)

## 2) High-Level Architecture Map

### Core areas

- `src/research/backend`: FastAPI API, SQLAlchemy-backed persistence, report/wearable processing, AI workflow orchestration.
- `src/research/frontend`: React + Vite physician workflow UI, dashboard, consultation step forms, context state.
- `tests`: pytest fixtures and unit-level backend/schema/middleware tests.
- `migrations`: Alembic env + migration versions (includes very large normalized-schema migration).
- `docs`: user/dev docs and informed consent materials.
- `src/research-poc`: proof-of-concept parallel app (backend + frontend) with separate implementation.

### Top-size hotspots (selected)

- `src/research/frontend/package-lock.json` (3333)
- `src/research-poc/frontend/package-lock.json` (3322)
- `migrations/versions/2cbf5c81b941_add_normalized_tables_for_research_app.py` (2587)
- `src/research/backend/app/main.py` (910)
- `src/research/frontend/src/components/consultation/Diagnosis.jsx` (595)
- `src/research/frontend/src/components/consultation/Exam.jsx` (594)

## 3) Backend Deep Read

### API surface

Backend endpoint declarations are centralized in `src/research/backend/app/main.py` and include:

- Health, patient CRUD, consultation status
- Step-wise consultation writes: demographics → lifestyle → symptoms → mental
- Medical reports upload/list/skip
- Wearable upload/skip
- AI diagnosis GET+submit
- AI exams GET+submit

### Persistence and session

- DB engine/session configured in `src/research/backend/app/database.py` with SQLite file under `src/research/backend/data/db.sqlite`.
- Repository pattern implemented in `src/research/backend/app/models/repositories.py`.
- Multiple commits happen inside repository helper methods (`create_patient_and_consultation`, `get_or_create_*`, `update_consultation`).

### Data modeling and schema

- API contracts in `src/research/backend/app/schemas.py`.
- Normalized ORM entities in `src/research/backend/app/models/ui.py`.
- FHIR report extraction helpers in `src/research/backend/app/reports.py`.

## 4) Frontend Deep Read

### Route-level flow

- App routes in `src/research/frontend/src/App.jsx` map to consultation wizard + dashboard + patient detail.
- Consultation step components are large and self-contained (`Demographics`, `Lifestyle`, `Symptoms`, `Mental`, `MedicalReport`, `Wearable`, `Diagnosis`, `Exam`, `Confirmation`).

### Client API and state

- API service in `src/research/frontend/src/services/api.js` wraps all backend routes.
- Global state managed via `ConsultationContext.jsx` + `ConsultationReducer.js`.
- Local storage persistence currently stores only early-step form subsets.

## 5) Tests and Quality Signals

### Existing tests

- Schema table existence test: `tests/test_research_schema.py`
- Repository behavior tests: `tests/test_repositories.py`, `tests/test_research_db.py`
- Middleware body-size test: `tests/test_body_size_middleware.py`
- Shared fixtures and in-memory DB session in `tests/conftest.py`

### Gaps observed

- No frontend unit/integration tests found for API adapters/components.
- No end-to-end workflow tests for full consultation path.
- Current shell environment lacked `pytest` binary (`Command 'pytest' not found`).

## 6) Concrete Findings (Evidence-Backed)

1. **CORS wildcard mixed with credentials**
   - `src/research/backend/app/main.py` lines ~121-122
   - `allow_origins` includes `'*'` while `allow_credentials=True`.

2. **Patient creation timestamp is UTC naive string**
   - `src/research/backend/app/main.py` line ~427
   - Uses `datetime.utcnow().isoformat()`.

3. **Wearable upload reads whole file into memory**
   - `src/research/backend/app/main.py` line ~745 (`await file.read()`)
   - Potential pressure for larger files.

4. **File size validation depends on `file.size` attr**
   - `src/research/backend/app/main.py` line ~740
   - `UploadFile.size` may not be consistently present across interfaces.

5. **Latest consultation selection is inconsistent**
   - Multiple `consultations[-1]` usages in `main.py` (~167, ~377, ~487, etc.)
   - Separate deterministic helper exists (`max(..., key=timestamp)`) at ~252.

6. **Patient summary schema/UI expect language, list builder may omit it**
   - API list builder: `main.py` ~432, ~442
   - UI uses `patient.lang`: `Dashboard.jsx` ~349
   - `PatientSummary` class location near `schemas.py` ~313.

7. **Diagnosis/Exam ratings documented as 1–10 but unconstrained**
   - `schemas.py` ~190, ~250, ~254
   - Missing explicit numeric bounds (`ge/le`).

8. **Mental health error message typo**
   - `src/research/frontend/src/services/api.js` ~196 (`menatl`).

9. **Medical report skip error message has broken interpolation**
   - `src/research/frontend/src/services/api.js` ~245
   - Uses single-quoted string with `${response.status}` literal.

10. **Wearable upload payload contract mismatch risk**
    - `Wearable.jsx` creates FormData and passes to API (`~143`, `~158`)
    - `api.js` creates another FormData and appends argument as `file` (`~271`, `~273`).

11. **Medical report upload has same pattern mismatch risk**
    - `MedicalReport.jsx` builds FormData and passes it (`~153`, `~169`)
    - `api.js` expects iterable `files` and builds FormData (`~208`, `~210`).

12. **UI copy vs validator mismatch in medical reports step**
    - `maxFileSize` says 20MB (`MedicalReport.jsx` ~50)
    - Error text says 10MB (`~84`)
    - Help text lists DOC/DOCX though validator allows only PDF/JPG/PNG (`~265`).

13. **UI copy vs accepted formats mismatch in wearable step**
    - Accepted formats/extensions CSV+JSON (`Wearable.jsx` ~44, ~49)
    - UI text claims CSV/JSON/PDF/XLSX/ZIP (`~280`).

14. **Patient view exposes raw JSON debug panel by default**
    - `PatientView.jsx` comment and rendering at ~249 and ~267.

15. **Consultation localStorage persistence is partial**
    - `ConsultationContext.jsx` stateToSave block ~42-50
    - Persists only demographics/lifestyle/symptoms/mental subsets.

16. **Single large backend module**
    - `src/research/backend/app/main.py` is ~910 lines with endpoints + helpers + config.
    - Suggests opportunity to split routers/services.

17. **Large form components in frontend**
    - `Diagnosis.jsx` (~595), `Exam.jsx` (~594), `Wearable.jsx` (~468), `MedicalReport.jsx` (~446).
    - Complexity likely concentrated in UI state and validation logic.

18. **Minimal TODO debt markers found**
    - `src/research/frontend/src/services/api.js` ~274 (`TODO: add multiple file upload`)
    - `pyproject.toml` has TODO in lint config comment.

19. **Repository has active recent maintenance cadence**
    - Recent commits include docs, lint/type cleanup, CI path fixes.

20. **Frontend has no visible API call retry/timeout strategy**
    - Fetch wrappers in `api.js` perform direct `fetch` with status checks only.

## 7) Web Exploration Notes

Reviewed public pages:

- GitHub project page: confirms structure, language split (JS/Python), active PR/issues metadata.
- FastAPI CORS docs: explicitly advise not using wildcards with credentialed requests.
- SQLAlchemy Session Basics: reinforces scoped session lifecycle + commit/rollback framing patterns.
- React docs: component/state patterns are consistent with current architecture but suggest opportunities for reducing large component complexity.

## 8) Suggested Next Inspection Pass (Prioritized)

1. Normalize frontend upload API contracts (`File` vs `FormData`) and add tests.
2. Add schema-level numeric constraints to consultation inputs/ratings.
3. Align UI upload copy with validator reality.
4. Replace ad-hoc `consultations[-1]` with deterministic latest-consultation helper everywhere.
5. Gate debug JSON output behind dev flag.
6. Expand resume persistence model for later consultation steps.
7. Split oversized modules into smaller route/service units.

## 9) Important Limitation

This exploration includes exhaustive automated traversal of all tracked files and focused deep reads of core modules.
For true “line-by-line commentary” on every line, a generated annotated dump would be extremely large and should be produced in segmented batches (e.g., backend pass, frontend pass, tests pass) to stay reviewable.

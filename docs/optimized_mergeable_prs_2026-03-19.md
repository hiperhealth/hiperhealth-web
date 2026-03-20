# Optimized, Unique, Mergeable PR Backlog (2026-03-19)

This backlog is designed for fast review, low conflict risk, and measurable performance/reliability gains.

## PR-01 — Fix multipart upload contract and remove double FormData wrapping

**Title**
- fix(frontend): normalize upload payload contract for medical and wearable endpoints

**Why this is high value**
- Prevents malformed multipart requests and reduces upload failures.

**Scope**
- Standardize API helper signatures in `src/research/frontend/src/services/api.js`.
- Update callers in consultation components to pass `File[]` or `File` (not prebuilt `FormData`).
- Add defensive validation for empty payloads.

**Acceptance criteria**
- Medical and wearable uploads work with valid fixtures.
- No nested `FormData` payloads are emitted.
- Clear error messages for invalid or empty uploads.

**Validation**
- Add API service unit tests for request body shape.

**Risk**
- Low (isolated to upload code paths).

---

## PR-02 — Add strict schema constraints for numeric medical inputs

**Title**
- fix(backend): enforce bounded numeric validation in consultation schemas

**Why this is high value**
- Rejects invalid clinical input early, improving data quality and reducing downstream model noise.

**Scope**
- Add `ge/le` constraints for ratings and clinical numeric fields in `src/research/backend/app/schemas.py`.
- Keep response format stable.

**Acceptance criteria**
- Out-of-range values return `422` with field-level errors.
- Valid payloads remain unchanged.

**Validation**
- Add boundary tests in `tests/` for min/max and invalid types.

**Risk**
- Low-medium (stricter input may expose invalid frontend assumptions).

---

## PR-03 — Deterministic latest consultation selection and query efficiency

**Title**
- refactor(backend): replace ad-hoc consultations[-1] with deterministic latest consultation resolver

**Why this is high value**
- Prevents incorrect step/status decisions when relationship ordering is not guaranteed.

**Scope**
- Introduce a single latest-consultation resolver in repository/service layer.
- Replace repeated direct indexing in endpoint flow.

**Acceptance criteria**
- Status and progression are correct for out-of-order timestamps.
- No functional change for normal cases.

**Validation**
- Add regression test with two consultations inserted in non-chronological order.

**Risk**
- Medium (touches multiple endpoints).

---

## PR-04 — Transaction optimization in repository writes

**Title**
- perf(backend): collapse multi-commit repository writes into single transactional units

**Why this is high value**
- Reduces DB round trips and improves consistency under failure.

**Scope**
- In `src/research/backend/app/models/repositories.py`, reduce commit frequency in:
  - `create_patient_and_consultation`
  - `update_consultation`
  - helper create-or-get flows
- Use `flush` where IDs are needed before final commit.

**Acceptance criteria**
- Equivalent persisted data for existing flows.
- Fewer commits per request path.

**Validation**
- Existing repository tests pass.
- Add one transactional rollback test for induced failure.

**Risk**
- Medium (transaction boundary changes).

---

## PR-05 — Secure and environment-driven CORS policy

**Title**
- chore(backend): env-configured explicit CORS origins with credential-safe defaults

**Why this is high value**
- Aligns with FastAPI/Starlette CORS rules and production security practices.

**Scope**
- Replace hardcoded wildcard-plus-credentials combination in `src/research/backend/app/main.py`.
- Add env parser for allowed origins.
- Document `.env` key usage.

**Acceptance criteria**
- Credentialed requests work for configured origins.
- Disallowed origins are rejected at preflight level.

**Validation**
- Add CORS middleware tests with allowed/disallowed origin cases.

**Risk**
- Medium (deployment config coordination required).

---

## PR-06 — Upload pipeline performance hardening (streaming + size guardrails)

**Title**
- perf(backend): stream upload processing and enforce robust size checks

**Why this is high value**
- Improves memory behavior and resilience under large uploads.

**Scope**
- Harden wearable/report upload paths in `src/research/backend/app/main.py` and `src/research/backend/app/reports.py`.
- Avoid full in-memory reads where possible.
- Normalize size validation behavior and error surface.

**Acceptance criteria**
- Oversized files fail fast with clear `413/422` semantics.
- Valid files process successfully.

**Validation**
- Add tests for large payload rejection and normal upload success.

**Risk**
- Medium (touches async file handling).

---

## PR-07 — Frontend consultation state persistence v2

**Title**
- feat(frontend): persist full consultation resume metadata across all steps

**Why this is high value**
- Prevents data loss on refresh/navigation and improves completion rate.

**Scope**
- Extend persistence model in `src/research/frontend/src/context/ConsultationContext.jsx`.
- Include diagnosis/exams/medical/wearable metadata (not binary content).
- Add backward-compatible migration from old storage shape.

**Acceptance criteria**
- Refresh/resume restores wizard state consistently across later steps.
- Old localStorage entries still load safely.

**Validation**
- Add reducer/context serialization tests.

**Risk**
- Low-medium.

---

## PR-08 — Dashboard scalability: server-side pagination and lightweight summary API

**Title**
- perf(fullstack): paginate patient list at API level and reduce dashboard payload

**Why this is high value**
- Avoids fetching all patients on every dashboard load; scales better with record growth.

**Scope**
- Add query params (`limit`, `offset`, optional sort) to `GET /api/patients`.
- Return compact summary fields and total count.
- Update dashboard to consume paginated API.

**Acceptance criteria**
- Dashboard renders from paginated response.
- Existing UX (page controls, resume/view/delete) remains intact.

**Validation**
- Add API tests for pagination boundaries.
- Add frontend integration test for page navigation state.

**Risk**
- Medium (API contract extension).

---

## PR-09 — AI call optimization: idempotent cache for diagnosis/exams suggestions

**Title**
- perf(backend): cache diagnosis/exam suggestions by consultation fingerprint

**Why this is high value**
- Reduces repeated AI calls and improves response latency/cost.

**Scope**
- Compute a stable consultation fingerprint (selected fields + language).
- Reuse prior generated suggestions when fingerprint unchanged.
- Keep manual “refresh suggestions” path opt-in.

**Acceptance criteria**
- Repeated calls for unchanged consultation return cached payload.
- Changed inputs invalidate cache and recompute.

**Validation**
- Add tests for cache hit/miss behavior.

**Risk**
- Medium-high (requires careful invalidation rules).

---

## PR-10 — Production safety cleanup and low-noise observability

**Title**
- chore(fullstack): hide raw debug JSON in production and add request-id logging

**Why this is high value**
- Reduces accidental data exposure and improves incident triage.

**Scope**
- Gate JSON debug panel in patient view by environment flag.
- Add request-id middleware/log enrichment in backend.
- Ensure error responses include correlation id (non-sensitive).

**Acceptance criteria**
- Debug panel not visible in prod builds.
- Logs include request-id across endpoint failures.

**Validation**
- Add middleware test for request-id header propagation.

**Risk**
- Low-medium.

---

## Recommended Merge Order (Conflict-Minimized)

1. PR-01 upload contract
2. PR-02 schema constraints
3. PR-03 latest consultation resolver
4. PR-04 transaction optimization
5. PR-05 CORS policy
6. PR-06 upload streaming guardrails
7. PR-07 state persistence v2
8. PR-08 dashboard pagination
9. PR-10 prod safety + observability
10. PR-09 AI caching (last, because it depends on stable contracts)

## “Mergeable” Definition Used

Each PR above is scoped to:
- One primary problem statement
- Limited cross-module touchpoints
- Explicit acceptance criteria
- Backward-safe rollout path
- Dedicated validation plan

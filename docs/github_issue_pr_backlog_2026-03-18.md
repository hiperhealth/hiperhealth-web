# GitHub Issue + PR Backlog (Curated)

This backlog was derived from direct codebase exploration and focuses on **fixable, review-friendly, mergeable** slices.

---

## 1) Fix wearable upload contract mismatch (FormData double-wrap)

### Issue Draft
**Title:** `frontend: wearable upload sends FormData object instead of File`

**Problem**
The wearable upload flow constructs `FormData` in the component and then sends it to an API helper that constructs a second `FormData`. This causes the backend payload to contain an invalid value (`[object FormData]`) instead of a file stream.

**Evidence**
- `src/research/frontend/src/components/consultation/Wearable.jsx` lines ~143 and ~158
- `src/research/frontend/src/services/api.js` lines ~271-273

**Expected behavior**
`uploadWearableData` should receive a `File` (or `Blob`) and submit exactly one multipart body.

**Acceptance criteria**
- Component passes a `File` to API helper (or helper accepts prebuilt `FormData`, but only one strategy is used).
- Upload works for valid CSV/JSON fixtures.
- Error handling still displays backend validation message.
- Add/adjust a frontend unit/integration test for API helper payload shape.

### PR Draft
**Title:** `fix(frontend): correct wearable multipart payload contract`

**Changes**
- Unify upload contract between `Wearable.jsx` and `api.js`.
- Add a small reusable utility for multipart upload payload building (optional but scoped).
- Add regression test to prevent nested `FormData` submissions.

---

## 2) Harden CORS configuration for credentialed requests

### Issue Draft
**Title:** `backend: remove wildcard origin when credentials are enabled`

**Problem**
CORS config currently combines `allow_credentials=True` with wildcard `*` in origins, which is unsafe and non-compliant for credentialed browser requests.

**Evidence**
- `src/research/backend/app/main.py` lines ~121-122

**Expected behavior**
Allowed origins should be explicit and environment-driven for dev/prod.

**Acceptance criteria**
- `allow_origins` comes from env/config and never mixes `*` with credentials.
- Default local dev origins remain functional.
- Add test(s) for preflight response headers under configured origins.
- Update docs for `CORS_ALLOWED_ORIGINS`.

### PR Draft
**Title:** `feat(backend): env-driven CORS origins with secure defaults`

**Changes**
- Introduce config parser for comma-separated origins.
- Replace hard-coded wildcard list.
- Add tests for allowed/disallowed origin behavior.

---

## 3) Add strict numeric validation for clinical ratings and biometrics

### Issue Draft
**Title:** `backend: enforce domain bounds in Pydantic schemas`

**Problem**
Several fields are documented with expected ranges (e.g., rating 1-10) but do not enforce constraints in schema validation.

**Evidence**
- `src/research/backend/app/schemas.py` lines ~190, ~250, ~254 (ratings)
- `src/research/backend/app/schemas.py` line ~64 (`sleep_hours`), and demographics numeric fields

**Expected behavior**
Invalid values should be rejected at request validation stage with clear `422` messages.

**Acceptance criteria**
- Use `Field(ge=..., le=...)` for rating fields.
- Add practical bounds for demographics/lifestyle numerics (age, weight, height, sleep).
- Add API tests for boundary pass/fail cases.
- No behavior regression for valid payloads.

### PR Draft
**Title:** `fix(api): enforce numeric bounds for consultation schema inputs`

**Changes**
- Add schema constraints and message consistency.
- Add tests covering lower/upper bound and type errors.

---

## 4) Fix patient summary contract mismatch (`lang` missing in API response)

### Issue Draft
**Title:** `backend/frontend: patient summary list omits language required by schema/UI`

**Problem**
`PatientSummary` requires `lang`, dashboard renders `patient.lang`, but `/api/patients` response construction does not provide `lang`.

**Evidence**
- API builder: `src/research/backend/app/main.py` lines ~432 and ~442
- Schema requires lang: `src/research/backend/app/schemas.py` lines ~310-313
- UI expects lang: `src/research/frontend/src/components/dashboard/Dashboard.jsx` lines ~334 and ~349

**Expected behavior**
Patient summaries consistently include language and never rely on fallback `N/A` for known records.

**Acceptance criteria**
- `/api/patients` returns `lang` from latest consultation metadata.
- Endpoint satisfies response model without validation risk.
- Add test for patient summary payload completeness.

### PR Draft
**Title:** `fix(api): include language in patient summary payload`

**Changes**
- Add `lang` assignment in patient summary creation.
- Add regression test for `/api/patients` schema compliance.

---

## 5) Remove PHI-heavy raw JSON dump from production patient view

### Issue Draft
**Title:** `frontend: gate raw patient JSON debug panel behind dev mode`

**Problem**
The patient view currently renders full raw JSON, which can expose sensitive data in UI screenshots and operator workflows.

**Evidence**
- `src/research/frontend/src/components/dashboard/PatientView.jsx` lines ~249 and ~267

**Expected behavior**
Raw JSON should be hidden in production by default and only enabled in development/debug mode.

**Acceptance criteria**
- Debug panel only renders when `import.meta.env.DEV` (or explicit feature flag) is true.
- No impact on normal patient tab rendering.
- Optional: add compact toggle for debug visibility in dev.

### PR Draft
**Title:** `chore(frontend): hide patient raw JSON panel outside dev mode`

**Changes**
- Condition guard around debug block.
- Optional env flag (`VITE_SHOW_PATIENT_DEBUG`) for explicit override.

---

## 6) Make consultation “latest record” selection deterministic

### Issue Draft
**Title:** `backend: replace ad-hoc consultations[-1] usage with deterministic latest selector`

**Problem**
The API uses `consultations[-1]` in many places, while one helper uses `max(..., key=timestamp)`. Without explicit relationship ordering, this can produce inconsistent behavior.

**Evidence**
- Repeated `consultations[-1]`: `src/research/backend/app/main.py` lines ~167, ~377, ~444, ~487, ~530, ~555, ~582, ~606, ~631, ~682, ~705, ~738, ~775, ~806, ~868
- Deterministic helper exists separately: `src/research/backend/app/main.py` line ~252
- Similar pattern in repository: `src/research/backend/app/models/repositories.py` line ~86

**Expected behavior**
All endpoints should use a single deterministic method to retrieve the latest consultation.

**Acceptance criteria**
- Introduce/reuse one helper for latest consultation selection.
- Replace direct `[-1]` lookups in endpoint logic.
- Add test with out-of-order timestamps ensuring correct latest consultation is used.

### PR Draft
**Title:** `refactor(backend): unify latest-consultation selection across endpoints`

**Changes**
- Remove ad-hoc indexing patterns.
- Add deterministic selection tests.

---

## 7) Align file validation copy vs real allowed formats/sizes

### Issue Draft
**Title:** `frontend: fix contradictory file upload constraints shown to users`

**Problem**
UI copy advertises formats/sizes that differ from actual accepted types and limits.

**Evidence**
- Medical report max says 20MB in code but 10MB in messages/UI: `src/research/frontend/src/components/consultation/MedicalReport.jsx` lines ~50, ~84, ~265
- Wearable UI advertises PDF/XLSX/ZIP but only accepts CSV/JSON: `src/research/frontend/src/components/consultation/Wearable.jsx` lines ~44, ~49, ~280

**Expected behavior**
All visible copy and runtime validation should be consistent.

**Acceptance criteria**
- Single source constants for accepted extensions and max size.
- Drag/drop text and error messages match actual validation.
- Add small unit tests for validator messaging.

### PR Draft
**Title:** `fix(frontend): sync upload constraints between UI copy and validators`

**Changes**
- Consolidate validation constants per step.
- Update text and error messages.
- Add tests for consistency.

---

## 8) Preserve full consultation context across refresh/resume

### Issue Draft
**Title:** `frontend: localStorage hydration persists only early-step formData`

**Problem**
Context persistence only stores demographics/lifestyle/symptoms/mental, causing data loss for later steps when users refresh or resume.

**Evidence**
- `src/research/frontend/src/context/ConsultationContext.jsx` lines ~42-50

**Expected behavior**
All step data relevant to resume (medical reports metadata, wearable metadata, diagnosis/exam selections) should persist safely.

**Acceptance criteria**
- Persist full `formData` subset needed for resume UX.
- Keep payload minimal (avoid storing heavy binary data).
- Ensure `Dashboard` resume logic hydrates later steps when applicable.
- Add tests for serialization/deserialization correctness.

### PR Draft
**Title:** `feat(frontend): robust consultation state persistence across all steps`

**Changes**
- Expand persistence schema and migration for existing localStorage keys.
- Hydrate diagnosis/exam/wearable/medical report metadata on resume.
- Add tests for backward-compatible hydration.

---

## Suggested sequencing for mergeability

1. #1 wearable multipart contract (high impact, narrow scope)
2. #4 patient summary language contract fix
3. #7 upload copy/validation consistency
4. #3 numeric schema bounds + tests
5. #5 debug JSON gating
6. #6 deterministic latest consultation refactor
7. #8 full localStorage persistence
8. #2 CORS hardening (may need deployment env coordination)

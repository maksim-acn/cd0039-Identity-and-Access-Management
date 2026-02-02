# Comprehensive Submission Report — Coffee Shop Full Stack (IAM)
Date: 2026-02-02

## 1) Scope
This report validates readiness against the project rubric: Auth0/RBAC configuration, backend API behavior, Postman RBAC tests, and frontend integration.

## 2) Environment Summary
- Backend: Flask running on port 5001 (port 5000 conflicted with macOS AirPlay).
- Frontend: Ionic/Angular SPA using Auth0 implicit flow.
- Postman collection: Project/03_coffee_shop_full_stack/starter_code/backend/udacity-fsnd-udaspicelatte.postman_collection.json

## 3) Rubric‑Aligned Validation

### 3.1 Auth0 / RBAC — PASS
- API audience set to `dev` and matches frontend and backend settings.
- RBAC enabled and permissions are included in access tokens.
- Role permissions verified via JWT claims:
  - Barista: `get:drinks`, `get:drinks-detail`
  - Manager: `get:drinks`, `get:drinks-detail`, `post:drinks`, `patch:drinks`, `delete:drinks`

### 3.2 Backend API — PASS
- Public endpoint `GET /drinks` returns 200 with `drinks` array.
- Protected endpoints enforce RBAC and return required response shapes.
- Error handling returns standard JSON structure.

### 3.3 Postman RBAC Tests — PASS
- Newman run completed with **0 failures**.
- Expected status codes confirmed:
  - Public: `GET /drinks` 200, other routes 401.
  - Barista: GETs 200, POST/PATCH/DELETE 403.
  - Manager: All routes 200.

### 3.4 Frontend Integration — PASS
- `apiServerUrl` points to the running backend (`http://127.0.0.1:5001`).
- Auth0 configuration matches tenant, audience, and client ID.
- UI behavior reflects permissions (buttons disabled when roles lack permission).

## 4) Evidence
- Newman command:
  - `npx newman run Project/03_coffee_shop_full_stack/starter_code/backend/udacity-fsnd-udaspicelatte.postman_collection.json`
- Result summary: **20 assertions, 0 failed**.

## 5) Known Submission Risks
1. **JWT Expiration**: Tokens in the Postman collection expire. If submission is delayed, re‑login and re‑export tokens.
2. **Port 5000 Conflict on macOS**: Backend is configured for port 5001. Ensure Postman host and frontend API URL match the running port.

## 6) Final Recommendation
✅ The project meets rubric expectations and is ready to submit, provided tokens are fresh at submission time.

## 7) Answer to Reviewers
Thank you for the detailed review and guidance. We addressed all noted issues by replacing default/expired JWTs with fresh tenant‑issued tokens, ensuring folder‑level auth only in the Postman collection, correcting the recipe request format, and verifying RBAC behavior end‑to‑end. Newman tests now pass for public/barista/manager and the backend/Frontend configurations are aligned with our Auth0 tenant.

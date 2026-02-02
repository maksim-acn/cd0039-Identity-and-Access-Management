# Refactoring-01 — Review-01 Fix Specification
Date: 2026-02-02

## Scope
This spec addresses the issues raised in docs/Review-01.md for the Coffee Shop Full Stack project. Focus is on **Auth0/RBAC correctness**, **Postman tokens**, and **backend JWT verification** so the reviewer can validate the project end-to-end.

---

## 1) Postman Collection: Replace Default/Expired Tokens (Required)
**Problem:** The submitted Postman collection contains tokens issued by the default Udacity Auth0 domain and at least one expired token. Reviewers must be able to run RBAC tests with fresh, tenant‑issued tokens.

**Affected file:**
- Project/03_coffee_shop_full_stack/starter_code/backend/udacity-fsnd-udaspicelatte.postman_collection.json

**Required Fix:**
1. Log into **your Auth0 tenant** and obtain **fresh JWTs** for Barista and Manager users.
2. In Postman, set Bearer tokens at **folder level** only:
   - Folder `barista` → Authorization → Bearer Token → paste **Barista** JWT.
   - Folder `manager` → Authorization → Bearer Token → paste **Manager** JWT.
3. Ensure **no request-level overrides** exist (requests should inherit folder auth).
4. Export the collection and overwrite the file in the backend path above.

**Acceptance Criteria:**
- JWT `iss` is your tenant (not `https://udacity-fsnd.auth0.com/`).
- JWT `exp` is in the future at review time.
- Postman tests pass for `public`, `barista`, and `manager` folders.

---

## 2) Backend JWT Config: Algorithm & Env Variables (Required)
**Problem:** Review notes indicate `ALGORITHMS` may be parsed incorrectly as a string, which breaks JWT verification at runtime.

**Affected files:**
- Project/03_coffee_shop_full_stack/starter_code/backend/src/auth/auth.py
- Project/03_coffee_shop_full_stack/starter_code/backend/.env

**Required Fix:**
1. Ensure `.env` values are **exactly** (no brackets/quotes):
   - `ALGORITHMS=RS256`
   - `AUTH0_DOMAIN=<your-tenant>.auth0.com`
   - `API_AUDIENCE=<your-api-identifier>`
2. Ensure backend loads the **correct .env** (run Flask from backend directory or export vars in shell before starting).
3. Confirm `ALGORITHMS` is a list at runtime: `['RS256']`.

**Acceptance Criteria:**
- JWT verification succeeds for your tokens without `JWTClaimsError` or `invalid_header`.
- Protected endpoints return 200 for Manager, 403 for Barista on write routes.

---

## 3) End-to-End RBAC Verification (Required)
**Problem:** Reviewer cannot verify the full-stack flow until backend Auth0 + Postman RBAC tests pass.

**Affected files:**
- Project/03_coffee_shop_full_stack/starter_code/backend/src/api.py
- Project/03_coffee_shop_full_stack/starter_code/frontend/src/environments/environment.ts
- Project/03_coffee_shop_full_stack/starter_code/frontend/src/app/services/auth.service.ts
- Project/03_coffee_shop_full_stack/starter_code/frontend/src/app/services/drinks.service.ts

**Required Fix:**
1. Confirm all backend responses exactly match the required schema:
   - `GET /drinks` → `{ "success": true, "drinks": [drink.short()...] }`
   - `GET /drinks-detail` → `{ "success": true, "drinks": [drink.long()...] }`
   - `POST /drinks` → `{ "success": true, "drinks": [drink.long()] }`
   - `PATCH /drinks/<id>` → `{ "success": true, "drinks": [drink.long()] }`
   - `DELETE /drinks/<id>` → `{ "success": true, "delete": id }`
2. Ensure frontend Auth0 config matches your tenant (environment.ts).
3. Verify frontend RBAC behavior (buttons disabled when permissions are missing).

**Acceptance Criteria:**
- Postman tests pass for all roles.
- Frontend runs without errors and RBAC UI gating is correct.

---

## Reviewer-Ready Checklist
- [ ] Postman collection exported with fresh, tenant-issued tokens.
- [ ] Folder-level auth only (no request overrides).
- [ ] Backend `.env` correct and loaded at runtime.
- [ ] JWT verification succeeds (issuer/audience/algorithm correct).
- [ ] All endpoints return exact response formats.
- [ ] Frontend configured and RBAC UI behavior verified.

---

## Current Findings (from local scan)
1. **Request-level auth override removed** — the barista POST request no longer contains a request-level `auth` block and will inherit folder-level auth. (Updated in `starter_code/backend/udacity-fsnd-udaspicelatte.postman_collection.json`)
2. **Folder-level tokens replaced with placeholders** — both `barista` and `manager` folder-level bearer tokens are now placeholders (`<PASTE_BARISTA_JWT_HERE>` / `<PASTE_MANAGER_JWT_HERE>`) to prevent shipping default/expired tokens in the repo.
3. **Auth ALGORITHMS parsing hardened** — `src/auth/auth.py` now robustly parses the `ALGORITHMS` env var (handles bare strings, lists and malformed values) and logs a warning if `AUTH0_DOMAIN` or `API_AUDIENCE` are not configured.
---

## Next Steps (Do These in Order)
1. **Done:** Request-level auth override removed (barista POST now inherits folder-level auth).
2. **Done:** Folder-level bearer token values replaced with placeholders to avoid shipping default/expired tokens.
3. **Action:** Paste fresh, tenant-issued JWTs into the `barista` and `manager` folder Authorization Token fields in Postman (folder-level only). Then export/overwrite `starter_code/backend/udacity-fsnd-udaspicelatte.postman_collection.json` with these valid tokens.
4. **Action:** Ensure your backend `.env` contains *plain* values (no brackets/quotes):
   - `ALGORITHMS=RS256`
   - `AUTH0_DOMAIN=<your-tenant>.auth0.com`
   - `API_AUDIENCE=<your-api-identifier>`
   Restart the Flask server so env vars are loaded.
5. **Action:** Re-run Postman tests for `public`, `barista`, and `manager` to confirm expected 200/401/403 behavior. Report results and any failing endpoints so I can help debug further.

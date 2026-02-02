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
1. **Request-level auth override exists** on the barista POST request and must be removed so it inherits folder auth. (See [Project/03_coffee_shop_full_stack/starter_code/backend/udacity-fsnd-udaspicelatte.postman_collection.json](Project/03_coffee_shop_full_stack/starter_code/backend/udacity-fsnd-udaspicelatte.postman_collection.json#L256-L280))
2. **Folder-level tokens** for both `barista` and `manager` use the default Udacity issuer and are expired. (See [barista token](Project/03_coffee_shop_full_stack/starter_code/backend/udacity-fsnd-udaspicelatte.postman_collection.json#L350-L371) and [manager token](Project/03_coffee_shop_full_stack/starter_code/backend/udacity-fsnd-udaspicelatte.postman_collection.json#L582-L602))

---

## Next Steps (Do These in Order)
1. **Action:** Remove the request-level `auth` block from the barista POST request so it inherits folder-level auth.
2. **Action:** Paste fresh, tenant-issued JWTs into the `barista` and `manager` folder Authorization Token fields in Postman (folder-level only).
3. **Action:** Re-export/overwrite `starter_code/backend/udacity-fsnd-udaspicelatte.postman_collection.json` with those updated folder tokens (no request-level overrides).
4. **Action:** Ensure your backend `.env` contains *plain* values (no brackets/quotes):
  - `ALGORITHMS=RS256`
  - `AUTH0_DOMAIN=<your-tenant>.auth0.com`
  - `API_AUDIENCE=<your-api-identifier>`
  Restart the Flask server so env vars are loaded.
5. **Action:** Re-run Postman tests for `public`, `barista`, and `manager` to confirm expected 200/401/403 behavior. Report results and any failing endpoints so I can help debug further.

---

## JWT & Postman — Options and portable workflow 💡
This section documents how to obtain tokens and apply them in Postman so the reviewer can validate RBAC.

### A — How to obtain valid Barista & Manager JWTs
- Recommended (local frontend):
  1. Start the frontend (in `Project/03_coffee_shop_full_stack/starter_code/frontend`):
     - `ionic serve`
  2. Log in as the **Barista** user → open DevTools → Application → Local Storage → copy `access_token`.
  3. Repeat for **Manager**.

- Alternative (Auth0 Dashboard):
  - Use the Auth0 "Log in as user" / Try features if available, then inspect the browser session for the `access_token`. Avoid machine-to-machine tokens for RBAC testing.

### B — Apply tokens to Postman and export (portable steps)
1. Open Postman → Right-click `barista` folder → Edit → Authorization → Type **Bearer Token** → paste Barista JWT → Save.
2. Repeat for `manager`.
3. Double-check **no request-level Authorization** overrides exist.
4. Export collection: File → Export → overwrite `starter_code/backend/udacity-fsnd-udaspicelatte.postman_collection.json` and commit.

### C — Backend `.env` and runtime checks (portable)
- Ensure `.env` contains plain values (no brackets/quotes):
  - `ALGORITHMS=RS256`
  - `AUTH0_DOMAIN=<your-tenant>.auth0.com`
  - `API_AUDIENCE=<your-api-identifier>`
- Start the backend from `starter_code/backend/src` so `python-dotenv` loads `.env` values, or export the env values into the shell session before running `flask run`.

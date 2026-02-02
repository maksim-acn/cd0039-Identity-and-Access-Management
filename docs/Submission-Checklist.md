# Submission Checklist — Coffee Shop Full Stack (IAM)
Date: 2026-02-02

## 1) Auth0 / RBAC Setup
- [ ] Auth0 API identifier (audience) set and matches `API_AUDIENCE` / frontend `auth0.audience`
- [ ] RBAC enabled and **Add Permissions in Access Token** enabled
- [ ] Permissions created: `get:drinks`, `get:drinks-detail`, `post:drinks`, `patch:drinks`, `delete:drinks`
- [ ] Roles created: **Barista** (get endpoints) and **Manager** (all permissions)
- [ ] Test users assigned to Barista and Manager roles

## 2) Backend Config & Health
- [ ] Backend runs with correct env vars (`AUTH0_DOMAIN`, `API_AUDIENCE`, `ALGORITHMS=RS256`)
- [ ] Backend running on port **5001** (if port 5000 is blocked)
- [ ] Public GET `/drinks` returns 200 with `drinks` array

## 3) Postman Collection (Required)
- [ ] Collection file updated: `Project/03_coffee_shop_full_stack/starter_code/backend/udacity-fsnd-udaspicelatte.postman_collection.json`
- [ ] Tokens set at **folder level** only (no request-level overrides)
- [ ] Tokens are **fresh** and issued by your Auth0 tenant (not Udacity default)
- [ ] Host variable matches backend port (`localhost:5001` if applicable)
- [ ] Newman run passes all folders (public/barista/manager)

## 4) Frontend Config
- [ ] `apiServerUrl` points to backend (e.g., `http://127.0.0.1:5001`)
- [ ] `auth0` settings match your tenant (`url`, `audience`, `clientId`, `callbackURL`)
- [ ] UI behavior matches RBAC (disabled buttons when permission missing)

## 5) Final Verification
- [ ] Postman tests pass (public 200/401, barista 200/403, manager 200 for all)
- [ ] No expired tokens in submission
- [ ] All required files committed

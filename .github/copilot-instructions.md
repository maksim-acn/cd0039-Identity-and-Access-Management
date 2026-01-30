# Copilot Instructions for Coffee Shop Full Stack Project

## Project Goal
Complete the "Coffee Shop" full-stack app for the Udacity Full Stack Nanodegree **Identity & Access Management** module. Focus is on implementing **Auth0 JWT verification** and **RBAC (Role-Based Access Control)** in the Flask backend.

## Project Structure
```
Project/03_coffee_shop_full_stack/starter_code/
├── backend/src/
│   ├── api.py              # Flask routes - IMPLEMENT @TODO endpoints
│   ├── auth/auth.py        # JWT verification - IMPLEMENT @TODO functions
│   └── database/models.py  # Drink model (provided)
└── frontend/               # Ionic/Angular app (mostly complete)
```

## Auth0 Setup (Required Before Coding)
1. Create Auth0 account → create tenant → create Single Page Application
2. Create API with identifier (audience), enable **RBAC** and **Add Permissions in Access Token**
3. Add permissions: `get:drinks`, `get:drinks-detail`, `post:drinks`, `patch:drinks`, `delete:drinks`
4. Create roles: **Barista** (`get:drinks`, `get:drinks-detail`) and **Manager** (all permissions)
5. Register test users and assign roles
6. Update `frontend/src/environments/environment.ts` with your Auth0 credentials

See [backend/README.md](Project/03_coffee_shop_full_stack/starter_code/backend/README.md) for detailed Auth0 setup steps.

## Development Commands

### Backend
```bash
cd Project/03_coffee_shop_full_stack/starter_code/backend
pip install -r requirements.txt
cd src && export FLASK_APP=api.py && flask run --reload  # http://127.0.0.1:5000
```

### Frontend
```bash
cd Project/03_coffee_shop_full_stack/starter_code/frontend
npm install
export NODE_OPTIONS=--openssl-legacy-provider  # Required for Node 17+
ionic serve  # http://localhost:8100
```

## Backend Implementation Tasks

### 1. Auth Module (`src/auth/auth.py`)
Implement these functions (see constants at top: `AUTH0_DOMAIN`, `ALGORITHMS`, `API_AUDIENCE`):

| Function | Purpose |
|----------|---------|
| `get_token_auth_header()` | Extract Bearer token from `Authorization` header |
| `check_permissions(permission, payload)` | Verify permission exists in JWT `permissions` claim |
| `verify_decode_jwt(token)` | Fetch JWKS from Auth0, validate and decode JWT |

**AuthError pattern** - raise for auth failures:
```python
raise AuthError({'code': 'authorization_header_missing', 'description': 'Authorization header is expected.'}, 401)
```

### 2. API Endpoints (`src/api.py`)

| Endpoint | Method | Auth | Permission | Response Format |
|----------|--------|------|------------|-----------------|
| `/drinks` | GET | None | Public | `{"success": true, "drinks": [drink.short()...]}` |
| `/drinks-detail` | GET | Required | `get:drinks-detail` | `{"success": true, "drinks": [drink.long()...]}` |
| `/drinks` | POST | Required | `post:drinks` | `{"success": true, "drinks": [drink.long()]}` |
| `/drinks/<id>` | PATCH | Required | `patch:drinks` | `{"success": true, "drinks": [drink.long()]}` |
| `/drinks/<id>` | DELETE | Required | `delete:drinks` | `{"success": true, "delete": id}` |

**POST/PATCH request body:**
```json
{"title": "Water", "recipe": [{"name": "water", "color": "blue", "parts": 1}]}
```

**Error response format (all errors):**
```python
jsonify({"success": False, "error": 404, "message": "resource not found"}), 404
```

### 3. Drink Model Methods
- `drink.short()` → `{id, title, recipe: [{color, parts}]}` (no ingredient names - public)
- `drink.long()` → `{id, title, recipe: [{name, color, parts}]}` (full details - authenticated)
- `drink.insert()`, `drink.update()`, `drink.delete()` for persistence

## Key Patterns

### Protected Route Decorator
```python
@app.route('/drinks-detail')
@requires_auth('get:drinks-detail')
def get_drinks_detail(payload):  # payload = decoded JWT
    drinks = Drink.query.all()
    return jsonify({"success": True, "drinks": [d.long() for d in drinks]})
```

### Recipe Storage
Recipes stored as JSON string in DB: `'[{"name": "milk", "color": "grey", "parts": 1}]'`

## Frontend Integration Notes
- `auth.service.ts` handles Auth0 login flow and stores JWT in localStorage
- `auth.can(permission)` checks JWT claims - used in templates: `[disabled]="!auth.can('delete:drinks')"`
- `drinks.service.ts` calls backend with `Authorization: Bearer <token>` header
- Frontend expects exact response formats above; deviations break the UI

## Testing
1. **First run**: Uncomment `db_drop_and_create_all()` in `api.py` to initialize SQLite database
2. **Postman**: Import `backend/udacity-fsnd-udaspicelatte.postman_collection.json`
   - Update JWT tokens in collection Authorization tabs (tokens expire)
   - Collection has `public`, `barista`, `manager` folders testing different permission levels
3. **Expected test results**:
   - Public: `/drinks` returns 200, protected routes return 401
   - Barista: GET routes return 200, POST/PATCH/DELETE return 403
   - Manager: All routes return 200

## Common Issues
- **CORS**: Already configured via Flask-Cors
- **SSL errors with urlopen**: See `verify_decode_jwt` docstring for certificate fix
- **Node/npm**: May need `npm install node-sass@4.14.1` for native dependencies

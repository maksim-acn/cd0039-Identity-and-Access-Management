# Implementation Plan

[Overview]
The goal is to complete the Coffee Shop Full Stack project, a learning task focused on Identity and Access Management (IAM) with Auth0 integration. The project includes a Flask backend API with role-based access control (RBAC) and an Ionic frontend for managing a coffee shop menu.

The application must:
1. Display drink graphics showing ingredient ratios
2. Allow public users to view drink names and graphics
3. Allow baristas to see recipe information
4. Allow managers to create and edit drinks

This implementation will complete all the @TODO comments in the backend codebase and configure the frontend with the necessary Auth0 settings.

[Types]
The project uses the following main data types:

1. **Drink Model**:
   - id: Integer (primary key)
   - title: String (unique, 80 characters max)
   - recipe: String (JSON blob storing ingredients as [{name, color, parts}])

2. **Auth0 Configuration**:
   - AUTH0_DOMAIN: String (Auth0 tenant domain)
   - ALGORITHMS: Array of strings (JWT signing algorithms)
   - API_AUDIENCE: String (API identifier)

3. **JWT Payload**:
   - iss: String (issuer)
   - sub: String (subject)
   - aud: String (audience)
   - iat: Integer (issued at timestamp)
   - exp: Integer (expiration timestamp)
   - permissions: Array of strings (RBAC permissions)

[Files]
**New Files to Create:**
- None

**Existing Files to Modify:**
1. `Project/03_coffee_shop_full_stack/starter_code/backend/src/auth/auth.py`
   - Implement `get_token_auth_header()`
   - Implement `check_permissions()`
   - Implement `verify_decode_jwt()`
   - Implement `requires_auth()` decorator

2. `Project/03_coffee_shop_full_stack/starter_code/backend/src/api.py`
   - Uncomment database initialization
   - Implement GET /drinks endpoint (public)
   - Implement GET /drinks-detail endpoint (requires get:drinks-detail permission)
   - Implement POST /drinks endpoint (requires post:drinks permission)
   - Implement PATCH /drinks/<id> endpoint (requires patch:drinks permission)
   - Implement DELETE /drinks/<id> endpoint (requires delete:drinks permission)
   - Implement error handlers for 404 and AuthError

3. `Project/03_coffee_shop_full_stack/starter_code/frontend/src/environments/environment.ts`
   - Configure Auth0 variables (url, audience, clientId)
   - Configure API server URL

**Files to Delete or Move:**
- None

**Configuration File Updates:**
- `Project/03_coffee_shop_full_stack/starter_code/backend/requirements.txt` - already includes necessary dependencies

[Functions]
**New Functions:**
- `get_token_auth_header()` - Extracts JWT from Authorization header
- `check_permissions()` - Validates required permissions in JWT payload
- `verify_decode_jwt()` - Verifies and decodes JWT using Auth0 JWKS
- `requires_auth()` - Decorator to protect API endpoints with RBAC

**Modified Functions:**
- None in existing code (all new functions are implementing @TODO comments)

**Removed Functions:**
- None

[Classes]
**New Classes:**
- None

**Modified Classes:**
- None (Drink model is already implemented)

**Removed Classes:**
- None

[Dependencies]
**New Packages:**
- None (all required dependencies are listed in requirements.txt)

**Version Changes:**
- None

**Integration Requirements:**
- Auth0 account with configured API, permissions, and roles
- Postman for testing endpoints with JWT tokens

[Testing]
**Test File Requirements:**
- Import and use the provided Postman collection: `udacity-fsnd-udaspicelatte.postman_collection.json`
- Configure JWT tokens for Barista and Manager roles

**Existing Test Modifications:**
- Update Postman collection with valid JWT tokens

**Validation Strategies (TDD Approach):**
1. **Write tests first** for all endpoints and authentication functions
2. Test public endpoint (GET /drinks) without authentication
3. Test endpoints with Barista role (get:drinks, get:drinks-detail)
4. Test endpoints with Manager role (all permissions)
5. Test error handling for invalid tokens, missing permissions, etc.
6. **Run tests** before implementing each feature to see failures
7. **Implement features** to fix failing tests
8. **Refactor and optimize** code after tests pass
9. **Re-run tests** to ensure refactoring didn't break functionality

**Test-Driven Development Best Practices:**
- Write small, focused tests that test one thing at a time
- Use descriptive test names that explain the expected behavior
- Ensure tests are independent of each other
- Run tests after every code change to catch regressions early
- Keep tests fast and reliable to maintain developer productivity
- Document test scenarios and expected outcomes

[Implementation Order]
1. Write tests for all endpoints and authentication functions
2. Implement authentication functions in `auth.py` to fix failing tests
3. Implement API endpoints in `api.py` to fix failing tests
4. Configure Auth0 account and update frontend environment variables
5. Test endpoints using Postman with different roles
6. Verify frontend functionality with ionic serve
7. Refactor and optimize code as needed
8. Re-run all tests to ensure functionality is preserved

# Auth0 Setup Guide for Coffee Shop Application

This guide will walk you through creating your own Auth0 account and configuring it for the Coffee Shop Full Stack application.

## Prerequisites
- Email address: skazo4ny@gmail.com (you will use this to create your Auth0 account)

## Step 1: Create an Auth0 Account
1. Visit [Auth0.com](https://auth0.com/)
2. Click "Sign Up"
3. Enter your email address: skazo4ny@gmail.com
4. Create a strong password
5. Click "Sign Up" to create your account
6. Verify your email address by clicking the link sent to skazo4ny@gmail.com

## Step 2: Set Up Your Auth0 Tenant
1. Once logged in, you'll be directed to the Auth0 dashboard
2. You'll see your tenant domain (it will look like `your-tenant.auth0.com`)
3. Make note of this domain - you'll need it later

## Step 3: Create an Application
1. From the dashboard, click "Applications" in the left sidebar
2. Click "Create Application"
3. Name your application "Coffee Shop"
4. Select "Single Page Web Applications" as the application type
5. Click "Create"

## Step 4: Configure Application Settings
1. In your application settings, find the "Domain" and "Client ID" fields
2. Make note of both values - you'll need them later
3. Scroll down to the "Allowed Callback URLs" section
4. Add: `http://localhost:8100`
5. Scroll down to the "Allowed Logout URLs" section
6. Add: `http://localhost:8100`
7. Scroll down to the "Allowed Web Origins" section
8. Add: `http://localhost:8100`
9. Click "Save Changes"

## Step 5: Create an API
1. From the dashboard, click "APIs" in the left sidebar
2. Click "Create API"
3. Name your API "Coffee Shop API"
4. Set the "Identifier" to `dev` (or any unique identifier you prefer)
5. Set the "Signing Algorithm" to RS256
6. Click "Create"

## Step 6: Configure API Settings
1. In your API settings, click the "Permissions" tab
2. Add the following permissions:
   - `get:drinks`
   - `get:drinks-detail`
   - `post:drinks`
   - `patch:drinks`
   - `delete:drinks`
3. Click "Save"

## Step 7: Enable RBAC in API
1. In your API settings, click the "Settings" tab
2. Scroll down to "RBAC Settings"
3. Enable "Enable RBAC"
4. Enable "Add Permissions in the Access Token"
5. Click "Save Changes"

## Step 8: Create Roles
1. From the dashboard, click "User Management" > "Roles" in the left sidebar
2. Click "Create Role"
3. Create a "Barista" role:
   - Name: Barista
   - Description: Can view drinks and drink details
   - Click "Create"
4. Click on the "Permissions" tab for the Barista role
5. Add the following permissions:
   - `get:drinks`
   - `get:drinks-detail`
6. Create a "Manager" role:
   - Name: Manager
   - Description: Can perform all drink operations
   - Click "Create"
7. Click on the "Permissions" tab for the Manager role
8. Add all 5 permissions:
   - `get:drinks`
   - `get:drinks-detail`
   - `post:drinks`
   - `patch:drinks`
   - `delete:drinks`

## Step 9: Create Test Users
1. From the dashboard, click "User Management" > "Users" in the left sidebar
2. Click "Create User"
3. Create a Barista user:
   - Email: barista@coffeeshop.com
   - Password: Create a strong password
   - Connection: Username-Password-Authentication
4. Create a Manager user:
   - Email: manager@coffeeshop.com
   - Password: Create a strong password
   - Connection: Username-Password-Authentication
5. After creating the users, click on each user and assign them to the appropriate role

## Step 10: Update Application Configuration
Your application is now configured with the following Auth0 credentials:

1. Backend: `/Project/03_coffee_shop_full_stack/starter_code/backend/.env`
   - `AUTH0_DOMAIN`: dev-biseljjjloqgmufv.us.auth0.com
   - `API_AUDIENCE`: dev
2. Frontend: `/Project/03_coffee_shop_full_stack/starter_code/frontend/src/environments/environment.ts`
   - `auth0.url`: dev-biseljjjloqgmufv.us.auth0.com
   - `auth0.audience`: dev
   - `auth0.clientId`: 7leSthHeQWR43WD169aYgjTK0CiyNvH7

## Step 11: Install Dependencies
1. Backend: Navigate to the backend directory and run:
   ```bash
   pip install -r requirements.txt
   ```
2. Frontend: Navigate to the frontend directory and run:
   ```bash
   npm install
   ```

## Step 12: Test Authentication
1. Run your backend server:
   ```bash
   cd Project/03_coffee_shop_full_stack/starter_code/backend
   pip install -r requirements.txt
   export FLASK_APP=src/api.py
   export FLASK_ENV=development
   flask run
   ```
2. Run your frontend server:
   ```bash
   cd Project/03_coffee_shop_full_stack/starter_code/frontend
   npm install
   npm run start
   ```
3. Use Postman to test the endpoints with different user roles:
   - Import the Postman collection: `Project/03_coffee_shop_full_stack/starter_code/backend/udacity-fsnd-udaspicelatte.postman_collection.json`
   - Test endpoints with Barista and Manager roles
4. Verify that each endpoint returns the expected results based on user permissions

## Troubleshooting
- If you encounter issues with authentication, check your Auth0 configuration
- Make sure all URLs in the application settings are correct
- Verify that users are assigned to the appropriate roles
- Check that permissions are correctly configured in the API

## Additional Resources
- [Auth0 Documentation](https://auth0.com/docs/)
- [Auth0 Quick Start Guides](https://auth0.com/docs/quickstart)
- [Auth0 API Documentation](https://auth0.com/docs/api)
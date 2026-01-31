# Review Summary 🌟
Date: Jan 30, 2026

Thanks for your submission. Unfortunately, this submission does not fulfill the required rubric items, so it is not reviewable as a complete project and I couldn’t grade it end-to-end.

Key required components are missing or not in a review-ready state (e.g., fully completed REST requirements, valid Auth0/RBAC setup with working Postman tests, and a verifiable end-to-end flow). Because these core requirements can’t be verified from the submitted materials, the project cannot be assessed against the rubric at this time.

Please re-submit with all required files and configurations in place so the backend, RBAC tests, and full-stack flow can be successfully validated.

## Reviewer Note 1
Not yet passing ❌ — The Postman collection includes a token issued by the default Udacity Auth0 domain, and one token is clearly expired, which means tests will fail during review.

Feedback
What you did right (keep it):

Your collection includes JWTs and role-like permission sets ✅
There are tokens that appear to include the correct permissions claims ✅
What causes the FAIL (must fix):

At least one JWT in the collection has:
iss: "https://udacity-fsnd.auth0.com/" ❌ (default course issuer)
and it is expired (exp timestamp is years old) ❌
The rubric specifically says if the issuer is the default Udacity domain, the student did not properly export updated tokens.
Required fix (use the rubric’s wording expectation):

Re-export the collection to:
./starter_code/backend/udacity-fsnd-udaspicelatte.postman_collection.json
Ensure barista + manager folders have valid tokens set at the folder auth level, with no request-level overrides.

## Reviewer Note 2

Not yet passing ❌ — The Postman collection includes a token issued by the default Udacity Auth0 domain, and one token is clearly expired, which means tests will fail during review.

Feedback
What you did right (keep it):

Your collection includes JWTs and role-like permission sets ✅
There are tokens that appear to include the correct permissions claims ✅
What causes the FAIL (must fix):

At least one JWT in the collection has:
iss: "https://udacity-fsnd.auth0.com/" ❌ (default course issuer)
and it is expired (exp timestamp is years old) ❌
The rubric specifically says if the issuer is the default Udacity domain, the student did not properly export updated tokens.
Required fix (use the rubric’s wording expectation):

Re-export the collection to:
./starter_code/backend/udacity-fsnd-udaspicelatte.postman_collection.json
Ensure barista + manager folders have valid tokens set at the folder auth level, with no request-level overrides.
Roles and permission tables are configured in Auth0. The JWT includes the RBAC permission claims.

Barista access is limited:

can get drinks
can get drink-details
Manager access is limited

can get drinks
can get drink details
can post drinks
can patch drinks
can delete drinks
The provided postman collection passes all tests when configured with valid JWT tokens.

You must update and export the postman collection to ./starter_code/backend/udacity-fsnd-udaspicelatte.postman_collection.json with your JWTs configured by right-clicking the collection folder for barista and manager, navigating to the authorization tab, and including the JWT in the token field. Please note that the token will expire in 8 hours. Therefore, please allow sufficient time to avoid submitting expired token before the project reviewer complete the review.

## Reviewer Note 3

Not yet passing ❌ — The backend structure is present, but it likely cannot satisfy all required requests end-to-end because the Auth/JWT configuration is not reliably correct as submitted.

Feedback
Why this fails:

Your protected endpoints (e.g., GET /drinks-detail, POST/PATCH/DELETE) depend on JWT decoding.
Your algorithm configuration is likely wrong (ALGORITHMS loaded as a string instead of a list), which can cause JWT verification to fail at runtime.
What to fix:

Ensure ALGORITHMS becomes ['RS256'] in Python (not the string "['RS256']").
Work across the stack (ionic serve)
Not yet passing ❌ — Even though the frontend config is filled, RBAC/Postman validation fails and backend Auth0 config isn’t reviewer-ready, so end-to-end full-stack behavior can’t be verified.

Feedback
What causes the FAIL:

Postman RBAC tests can’t pass due to default/expired tokens.
Backend secured endpoints depend on runtime env vars and may fail if not correctly set.
The frontend can be run locally with no errors with ionic serve and displays the expected results.